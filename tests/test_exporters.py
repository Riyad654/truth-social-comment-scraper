thonimport json
import os
import sys

import pytest

# Ensure src/ is on sys.path for imports when running tests from repository root
CURRENT_DIR = os.path.dirname(__file__)
SRC_DIR = os.path.join(CURRENT_DIR, "..", "src")
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from storage.dataset_writer import DatasetWriter  # noqa: E402
from storage.csv_exporter import CORE_FIELDS  # noqa: E402

@pytest.fixture
def sample_comments():
    return [
        {
            "id": "1",
            "created_at": "2025-01-01T00:00:00+00:00",
            "edited_at": None,
            "language": "en",
            "url": "https://truthsocial.com/@user/1",
            "content_text": "First comment",
            "replies_count": 0,
            "reblogs_count": 0,
            "favourites_count": 0,
            "account_username": "user1",
            "account_display_name": "User One",
            "account_followers_count": 10,
        },
        {
            "id": "2",
            "created_at": "2025-01-02T00:00:00+00:00",
            "edited_at": None,
            "language": "en",
            "url": "https://truthsocial.com/@user/2",
            "content_text": "Second comment",
            "replies_count": 1,
            "reblogs_count": 2,
            "favourites_count": 3,
            "account_username": "user2",
            "account_display_name": "User Two",
            "account_followers_count": 20,
        },
    ]

def test_dataset_writer_json(tmp_path, sample_comments):
    output_path = tmp_path / "comments.json"
    writer = DatasetWriter()
    writer.write_dataset(sample_comments, str(output_path), fmt="json")

    assert output_path.exists()
    with output_path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    assert isinstance(data, list)
    assert len(data) == 2
    assert data[0]["id"] == "1"

    meta_path = tmp_path / "comments.json.meta.json"
    assert meta_path.exists()
    with meta_path.open("r", encoding="utf-8") as f:
        meta = json.load(f)
    assert meta["count"] == 2
    assert meta["format"] == "json"

def test_dataset_writer_csv(tmp_path, sample_comments):
    output_path = tmp_path / "comments.csv"
    writer = DatasetWriter()
    writer.write_dataset(sample_comments, str(output_path), fmt="csv")

    assert output_path.exists()
    with output_path.open("r", encoding="utf-8") as f:
        lines = f.read().strip().splitlines()
    header = lines[0].split(",")
    for field in CORE_FIELDS:
        assert field in header

    assert len(lines) == 3  # header + 2 rows