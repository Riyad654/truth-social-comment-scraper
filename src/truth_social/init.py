"""
Core Truth Social client and scraping utilities.
"""

from .client import TruthSocialClient
from .comment_fetcher import fetch_comments_for_post

__all__ = ["TruthSocialClient", "fetch_comments_for_post"]

__version__ = "0.1.0"