thonimport argparse
import json
import logging
import logging.config
import os
import sys
from typing import Any, Dict, List, Optional

from truth_social.client import TruthSocialClient
from truth_social.comment_fetcher import fetch_comments_for_post
from truth_social.comment_parser import parse_comments
from truth_social.rate_limiter import RateLimiter
from storage.dataset_writer import DatasetWriter
from utils.filters import (
    apply_language_filter,
    apply_min_engagement_filter,
    apply_sorting,
    apply_limit,
)

DEFAULT_CONFIG_PATH = os.path.join(
    os.path.dirname(__file__), "config", "settings.example.json"
)
DEFAULT_LOGGING_CONF = os.path.join(
    os.path.dirname(__file__), "config", "logging.conf"
)

def load_config(path: Optional[str]) -> Dict[str, Any]:
    config_path = path or DEFAULT_CONFIG_PATH
    if not os.path.exists(config_path):
        return {}
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)

def setup_logging(path: Optional[str], log_level: Optional[str]) -> None:
    logging_conf = path or DEFAULT_LOGGING_CONF
    if os.path.exists(logging_conf):
        logging.config.fileConfig(logging_conf, disable_existing_loggers=False)
    else:
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
        )

    if log_level:
        level = getattr(logging, log_level.upper(), logging.INFO)
        logging.getLogger().setLevel(level)

def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Truth Social Comment Scraper CLI",
    )
    parser.add_argument(
        "--post",
        required=True,
        help="Truth Social post URL or ID to scrape comments from.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Maximum number of comments to collect.",
    )
    parser.add_argument(
        "--sort",
        choices=["newest", "oldest", "popular"],
        default="newest",
        help="Sorting strategy for comments.",
    )
    parser.add_argument(
        "--language",
        default=None,
        help="Filter comments by language code (e.g., 'en'). Use comma-separated list for multiple.",
    )
    parser.add_argument(
        "--min-replies",
        type=int,
        default=0,
        help="Minimum replies count to keep a comment.",
    )
    parser.add_argument(
        "--min-reblogs",
        type=int,
        default=0,
        help="Minimum reblogs/retruths count to keep a comment.",
    )
    parser.add_argument(
        "--min-favourites",
        type=int,
        default=0,
        help="Minimum favourites/likes count to keep a comment.",
    )
    parser.add_argument(
        "--output",
        default="data/comments.json",
        help="Output file path for exported comments.",
    )
    parser.add_argument(
        "--format",
        choices=["json", "csv"],
        default="json",
        help="Output format.",
    )
    parser.add_argument(
        "--clean-content",
        action="store_true",
        help="If set, HTML content will be cleaned to plain text.",
    )
    parser.add_argument(
        "--config",
        default=None,
        help="Path to JSON configuration file (overridden by CLI flags).",
    )
    parser.add_argument(
        "--log-config",
        default=None,
        help="Path to logging configuration file.",
    )
    parser.add_argument(
        "--log-level",
        default=None,
        help="Override root log level (e.g., INFO, DEBUG, WARNING).",
    )
    parser.add_argument(
        "--base-url",
        default=None,
        help="Override Truth Social base URL.",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=None,
        help="HTTP timeout in seconds.",
    )
    parser.add_argument(
        "--max-requests-per-minute",
        type=int,
        default=None,
        help="Maximum number of HTTP requests per minute.",
    )
    return parser

def merge_config(cli_args: argparse.Namespace, file_config: Dict[str, Any]) -> Dict[str, Any]:
    config: Dict[str, Any] = {}
    config.update(file_config or {})

    def override_if_not_none(key: str, value: Any) -> None:
        if value is not None:
            config[key] = value

    override_if_not_none("post", cli_args.post)
    override_if_not_none("limit", cli_args.limit)
    override_if_not_none("sort", cli_args.sort)
    override_if_not_none("language", cli_args.language)
    override_if_not_none("min_replies", cli_args.min_replies)
    override_if_not_none("min_reblogs", cli_args.min_reblogs)
    override_if_not_none("min_favourites", cli_args.min_favourites)
    override_if_not_none("output", cli_args.output)
    override_if_not_none("format", cli_args.format)
    override_if_not_none("clean_content", cli_args.clean_content)
    override_if_not_none("base_url", cli_args.base_url)
    override_if_not_none("timeout", cli_args.timeout)
    override_if_not_none("max_requests_per_minute", cli_args.max_requests_per_minute)

    return config

def run(config: Dict[str, Any]) -> int:
    logger = logging.getLogger("cli")

    base_url = config.get("base_url", "https://truthsocial.com")
    timeout = int(config.get("timeout", 15))
    max_rpm = int(config.get("max_requests_per_minute", 60))

    client = TruthSocialClient(base_url=base_url, timeout=timeout)
    rate_limiter = RateLimiter(calls_per_minute=max_rpm)

    post = config["post"]
    limit = config.get("limit")
    sort = config.get("sort", "newest")
    clean_content = bool(config.get("clean_content", False))

    logger.info("Starting comment fetch for post: %s", post)

    try:
        raw_comments: List[dict] = fetch_comments_for_post(
            client=client,
            post_id_or_url=post,
            limit=limit,
            sort=sort,
            rate_limiter=rate_limiter,
        )
    except Exception as exc:  # pragma: no cover - defensive
        logger.exception("Failed to fetch comments: %s", exc)
        return 1

    logger.info("Fetched %d raw comments", len(raw_comments))

    parsed_comments = parse_comments(raw_comments, clean_content=clean_content)
    logger.info("Parsed %d comments", len(parsed_comments))

    languages = config.get("language")
    if isinstance(languages, str) and languages.strip():
        allowed_languages = [lang.strip() for lang in languages.split(",")]
        parsed_comments = apply_language_filter(parsed_comments, allowed_languages)
        logger.info("Filtered comments by language %s -> %d remaining", allowed_languages, len(parsed_comments))

    parsed_comments = apply_min_engagement_filter(
        parsed_comments,
        min_replies=config.get("min_replies", 0),
        min_reblogs=config.get("min_reblogs", config.get("min_retruths", 0)),
        min_favourites=config.get("min_favourites", config.get("min_likes", 0)),
    )

    logger.info("Filtered by engagement -> %d remaining", len(parsed_comments))

    parsed_comments = apply_sorting(parsed_comments, sort)
    parsed_comments = apply_limit(parsed_comments, limit)
    logger.info("After sorting and limiting -> %d comments", len(parsed_comments))

    output_path = config.get("output", "data/comments.json")
    output_format = config.get("format", "json")

    writer = DatasetWriter()
    try:
        writer.write_dataset(parsed_comments, output_path, output_format)
    except Exception as exc:  # pragma: no cover - defensive
        logger.exception("Failed to write dataset: %s", exc)
        return 1

    logger.info("Exported %d comments to %s (%s)", len(parsed_comments), output_path, output_format)
    return 0

def main(argv: Optional[List[str]] = None) -> int:
    parser = build_arg_parser()
    args = parser.parse_args(argv)

    setup_logging(args.log_config, args.log_level)
    file_config = load_config(args.config)
    config = merge_config(args, file_config)

    if not config.get("post"):
        logging.getLogger("cli").error("A post URL or ID must be specified via --post or in the config file.")
        return 1

    return run(config)

if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())