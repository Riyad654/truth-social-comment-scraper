thonimport logging
import re
from typing import Any, Dict, List, Optional
from urllib.parse import urlparse

import requests

logger = logging.getLogger("truth_social.client")

class TruthSocialClient:
    """
    Lightweight HTTP client for interacting with Truth Social's Mastodon-compatible API.

    This client intentionally focuses on the subset of functionality needed for scraping
    comments from a single post.
    """

    def __init__(
        self,
        base_url: str = "https://truthsocial.com",
        timeout: int = 15,
        proxies: Optional[Dict[str, str]] = None,
        verify_ssl: bool = True,
        session: Optional[requests.Session] = None,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.proxies = proxies
        self.verify_ssl = verify_ssl
        self.session = session or requests.Session()

    def resolve_post_id(self, post_id_or_url: str) -> str:
        """
        Accepts either a raw post ID or a full Truth Social URL and returns the post ID.
        """
        if re.fullmatch(r"\d+", post_id_or_url.strip()):
            return post_id_or_url.strip()

        parsed = urlparse(post_id_or_url)
        path_parts = [p for p in parsed.path.split("/") if p]
        if not path_parts:
            raise ValueError(f"Unable to resolve post id from URL: {post_id_or_url!r}")
        post_id = path_parts[-1]
        if not re.fullmatch(r"\d+", post_id):
            raise ValueError(f"Resolved post id does not look numeric: {post_id!r}")
        return post_id

    def _request(self, method: str, url: str, **kwargs: Any) -> requests.Response:
        kwargs.setdefault("timeout", self.timeout)
        if self.proxies is not None:
            kwargs.setdefault("proxies", self.proxies)
        kwargs.setdefault("verify", self.verify_ssl)

        logger.debug("HTTP %s %s kwargs=%s", method, url, kwargs)
        response = self.session.request(method, url, **kwargs)
        try:
            response.raise_for_status()
        except requests.HTTPError:
            logger.error(
                "HTTP error response from Truth Social API: %s %s - %s",
                method,
                url,
                response.text[:500],
            )
            raise
        return response

    def fetch_comments_context(
        self,
        post_id: str,
        params: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Fetch the context for a given post ID.

        For Mastodon-compatible APIs, the endpoint:
            GET /api/v1/statuses/{id}/context
        returns `ancestors` and `descendants` (replies).
        """
        url = f"{self.base_url}/api/v1/statuses/{post_id}/context"
        response = self._request("GET", url, params=params or {})
        data = response.json()
        if not isinstance(data, dict):
            raise ValueError("Unexpected context API response type (expected object).")
        return data

    def fetch_comments(
        self,
        post_id: str,
        limit: Optional[int] = None,
        sort: str = "newest",
    ) -> List[Dict[str, Any]]:
        """
        Fetch comment list (descendants) for a given post ID.

        Sorting and limit are performed client-side.
        """
        context = self.fetch_comments_context(post_id, params={})
        descendants = context.get("descendants", [])
        if not isinstance(descendants, list):
            raise ValueError("Unexpected descendants data type (expected list).")

        logger.info("Fetched %d raw descendants from API", len(descendants))

        comments = descendants
        if sort == "newest":
            comments = sorted(comments, key=lambda c: c.get("created_at", ""), reverse=True)
        elif sort == "oldest":
            comments = sorted(comments, key=lambda c: c.get("created_at", ""))
        elif sort == "popular":
            comments = sorted(
                comments,
                key=lambda c: (
                    c.get("replies_count", 0),
                    c.get("reblogs_count", 0),
                    c.get("favourites_count", 0),
                ),
                reverse=True,
            )

        if limit is not None and limit > 0:
            comments = comments[:limit]

        return comments