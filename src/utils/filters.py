thonfrom typing import Any, Dict, Iterable, List, Optional

def apply_language_filter(
    comments: Iterable[Dict[str, Any]],
    allowed_languages: Optional[List[str]],
) -> List[Dict[str, Any]]:
    if not allowed_languages:
        return list(comments)

    normalized = {lang.lower() for lang in allowed_languages}
    filtered: List[Dict[str, Any]] = []
    for c in comments:
        lang = (c.get("language") or "").lower()
        if not lang or lang in normalized:
            filtered.append(c)
    return filtered

def apply_min_engagement_filter(
    comments: Iterable[Dict[str, Any]],
    min_replies: int = 0,
    min_reblogs: int = 0,
    min_favourites: int = 0,
) -> List[Dict[str, Any]]:
    filtered: List[Dict[str, Any]] = []
    for c in comments:
        replies = int(c.get("replies_count") or 0)
        reblogs = int(c.get("reblogs_count") or 0)
        favourites = int(c.get("favourites_count") or 0)

        if replies < min_replies:
            continue
        if reblogs < min_reblogs:
            continue
        if favourites < min_favourites:
            continue

        filtered.append(c)
    return filtered

def apply_sorting(comments: Iterable[Dict[str, Any]], sort: str) -> List[Dict[str, Any]]:
    items = list(comments)
    if sort == "newest":
        return sorted(items, key=lambda c: c.get("created_at") or "", reverse=True)
    if sort == "oldest":
        return sorted(items, key=lambda c: c.get("created_at") or "")
    if sort == "popular":
        return sorted(
            items,
            key=lambda c: (
                int(c.get("replies_count") or 0),
                int(c.get("reblogs_count") or 0),
                int(c.get("favourites_count") or 0),
            ),
            reverse=True,
        )
    return items

def apply_limit(comments: Iterable[Dict[str, Any]], limit: Optional[int]) -> List[Dict[str, Any]]:
    items = list(comments)
    if limit is None or limit <= 0:
        return items
    return items[:limit]