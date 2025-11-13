thonfrom __future__ import annotations

import logging
from typing import Any, Dict, Iterable, List, Optional

from utils.content_cleaner import clean_html_content
from utils.time_helpers import parse_iso8601

logger = logging.getLogger("truth_social.comment_parser")

def _safe_int(value: Any) -> Optional[int]:
    try:
        if value is None:
            return None
        return int(value)
    except (TypeError, ValueError):
        return None

def _safe_bool(value: Any) -> Optional[bool]:
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        if value.lower() in ("true", "1", "yes", "y"):
            return True
        if value.lower() in ("false", "0", "no", "n"):
            return False
    return None

def parse_comment(raw: Dict[str, Any], clean_content: bool = False) -> Dict[str, Any]:
    """
    Normalize a raw Truth Social / Mastodon status object into a flattened schema
    suitable for analytics and storage.
    """

    account = raw.get("account") or {}
    created_at = parse_iso8601(raw.get("created_at"))
    edited_at = parse_iso8601(raw.get("edited_at")) if raw.get("edited_at") else None

    content_html = raw.get("content", "") or ""
    if clean_content:
        text_content = clean_html_content(content_html)
    else:
        text_content = raw.get("text") or clean_html_content(content_html)

    parsed: Dict[str, Any] = {
        "id": raw.get("id"),
        "created_at": created_at.isoformat() if created_at else None,
        "edited_at": edited_at.isoformat() if edited_at else None,
        "in_reply_to_id": raw.get("in_reply_to_id"),
        "in_reply_to_account_id": raw.get("in_reply_to_account_id"),
        "sensitive": _safe_bool(raw.get("sensitive")),
        "spoiler_text": raw.get("spoiler_text") or "",
        "visibility": raw.get("visibility"),
        "language": raw.get("language"),
        "uri": raw.get("uri"),
        "url": raw.get("url"),
        "content_html": content_html,
        "content_text": text_content,
        "replies_count": _safe_int(raw.get("replies_count")) or 0,
        "reblogs_count": _safe_int(raw.get("reblogs_count")) or 0,
        "favourites_count": _safe_int(raw.get("favourites_count")) or 0,
        "favourited": _safe_bool(raw.get("favourited")),
        "reblogged": _safe_bool(raw.get("reblogged")),
        "muted": _safe_bool(raw.get("muted")),
        "bookmarked": _safe_bool(raw.get("bookmarked")),
        "tombstone": raw.get("tombstone"),
        "version": raw.get("version"),
        "mentions": raw.get("mentions") or [],
        "tags": raw.get("tags") or [],
        "poll": raw.get("poll"),
        "quote": raw.get("quote"),
        "in_reply_to": raw.get("in_reply_to"),
        "group": raw.get("group"),
        "media_attachments": raw.get("media_attachments") or [],
        # Flattened account fields:
        "account_id": account.get("id"),
        "account_username": account.get("username"),
        "account_acct": account.get("acct"),
        "account_display_name": account.get("display_name"),
        "account_locked": _safe_bool(account.get("locked")),
        "account_bot": _safe_bool(account.get("bot")),
        "account_discoverable": _safe_bool(account.get("discoverable")),
        "account_group": _safe_bool(account.get("group")),
        "account_created_at": account.get("created_at"),
        "account_note_html": account.get("note"),
        "account_url": account.get("url"),
        "account_avatar": account.get("avatar"),
        "account_avatar_static": account.get("avatar_static"),
        "account_header": account.get("header"),
        "account_header_static": account.get("header_static"),
        "account_followers_count": _safe_int(account.get("followers_count")) or 0,
        "account_following_count": _safe_int(account.get("following_count")) or 0,
        "account_statuses_count": _safe_int(account.get("statuses_count")) or 0,
        "account_last_status_at": account.get("last_status_at"),
        "account_verified": _safe_bool(account.get("verified")),
        "account_location": account.get("location"),
        "account_website": account.get("website"),
        "account_accepting_messages": _safe_bool(account.get("accepting_messages")),
        "account_chats_onboarded": _safe_bool(account.get("chats_onboarded")),
        "account_feeds_onboarded": _safe_bool(account.get("feeds_onboarded")),
        "account_tv_onboarded": _safe_bool(account.get("tv_onboarded")),
        "account_bookmarks_onboarded": _safe_bool(account.get("bookmarks_onboarded")),
        "account_show_nonmember_group_statuses": _safe_bool(
            account.get("show_nonmember_group_statuses")
        ),
        "account_suspended": _safe_bool(account.get("suspended")),
        "account_tv_account": _safe_bool(account.get("tv_account")),
        "account_receive_only_follow_mentions": _safe_bool(
            account.get("receive_only_follow_mentions")
        ),
        "account_emojis": account.get("emojis") or [],
        "account_fields": account.get("fields") or [],
    }

    return parsed

def parse_comments(raw_comments: Iterable[Dict[str, Any]], clean_content: bool = False) -> List[Dict[str, Any]]:
    parsed_list: List[Dict[str, Any]] = []
    for raw in raw_comments:
        try:
            parsed_list.append(parse_comment(raw, clean_content=clean_content))
        except Exception as exc:  # pragma: no cover - defensive fallback
            logger.warning("Failed to parse comment with id=%s: %s", raw.get("id"), exc)
    return parsed_list