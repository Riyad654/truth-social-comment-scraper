thonimport logging
from typing import Any, Callable, Dict, Iterable, List, Optional

logger = logging.getLogger("truth_social.pagination")

FetchPageFunc = Callable[[Optional[str]], Dict[str, Any]]

def paginate(
    fetch_page: FetchPageFunc,
    start_cursor: Optional[str] = None,
    max_pages: Optional[int] = None,
) -> Iterable[Dict[str, Any]]:
    """
    Generic cursor-based pagination helper.

    `fetch_page` must accept a cursor token (or None for the first page) and return
    a dictionary that includes:

        - "items": a list of results
        - "next_cursor": cursor token for the next page or None

    This is currently not used by the default Truth Social client, but is kept as a
    utility for more advanced pagination strategies.
    """
    cursor = start_cursor
    pages = 0

    while True:
        logger.debug("Fetching page with cursor=%s", cursor)
        page = fetch_page(cursor)

        items = page.get("items", [])
        next_cursor = page.get("next_cursor")

        if not isinstance(items, list):
            raise ValueError("fetch_page must return a mapping with an 'items' list.")

        yield from items

        pages += 1
        if max_pages is not None and pages >= max_pages:
            logger.debug("Reached max_pages=%d", max_pages)
            break

        if not next_cursor:
            logger.debug("No next_cursor; stopping pagination.")
            break

        cursor = next_cursor