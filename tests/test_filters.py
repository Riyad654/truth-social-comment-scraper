thonimport os
import sys

# Ensure src/ is on sys.path for imports when running tests from repository root
CURRENT_DIR = os.path.dirname(__file__)
SRC_DIR = os.path.join(CURRENT_DIR, "..", "src")
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from utils.filters import (  # noqa: E402
    apply_language_filter,
    apply_min_engagement_filter,
    apply_sorting,
    apply_limit,
)

def make_comments():
    return [
        {
            "id": "1",
            "created_at": "2025-01-01T00:00:00+00:00",
            "language": "en",
            "replies_count": 0,
            "reblogs_count": 0,
            "favourites_count": 0,
        },
        {
            "id": "2",
            "created_at": "2025-01-02T00:00:00+00:00",
            "language": "es",
            "replies_count": 2,
            "reblogs_count": 1,
            "favourites_count": 5,
        },
        {
            "id": "3",
            "created_at": "2025-01-03T00:00:00+00:00",
            "language": "en",
            "replies_count": 1,
            "reblogs_count": 2,
            "favourites_count": 3,
        },
    ]

def test_apply_language_filter():
    comments = make_comments()
    filtered = apply_language_filter(comments, ["en"])
    ids = {c["id"] for c in filtered}
    assert ids == {"1", "3"}

def test_apply_min_engagement_filter():
    comments = make_comments()
    filtered = apply_min_engagement_filter(comments, min_replies=1, min_reblogs=1, min_favourites=3)
    ids = {c["id"] for c in filtered}
    assert ids == {"2", "3"}

def test_apply_sorting_newest():
    comments = make_comments()
    sorted_comments = apply_sorting(comments, "newest")
    assert [c["id"] for c in sorted_comments] == ["3", "2", "1"]

def test_apply_sorting_popular():
    comments = make_comments()
    sorted_comments = apply_sorting(comments, "popular")
    # Comment 2 has highest favourites_count; comment 3 next; then 1.
    assert [c["id"] for c in sorted_comments] == ["2", "3", "1"]

def test_apply_limit():
    comments = make_comments()
    limited = apply_limit(comments, 2)
    assert len(limited) == 2
    assert [c["id"] for c in limited] == ["1", "2"]