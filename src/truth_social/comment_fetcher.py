thonimport logging
from typing import Dict, List, Optional

from .client import TruthSocialClient
from .rate_limiter import RateLimiter

logger = logging.getLogger("truth_social.comment_fetcher")

def fetch_comments_for_post(
    client: TruthSocialClient,
    post_id_or_url: str,
    limit: Optional[int] = None,
    sort: str = "newest",
    rate_limiter: Optional[RateLimiter] = None,
) -> List[Dict]:
    """
    High-level helper to fetch all comments for a given post identifier or URL.

    Currently uses a single call to the context endpoint, which returns all
    descendants (replies). Rate limiter is applied once for defensive purposes,
    but can be extended to multi-page fetching if needed.
    """
    if rate_limiter is not None:
        rate_limiter.wait()

    post_id = client.resolve_post_id(post_id_or_url)
    logger.info("Resolved post id: %s", post_id)

    comments = client.fetch_comments(post_id=post_id, limit=limit, sort=sort)
    logger.info("Retrieved %d comments for post %s", len(comments), post_id)
    return comments