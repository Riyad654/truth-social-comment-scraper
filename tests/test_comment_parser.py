thonimport json
import os
import sys

# Ensure src/ is on sys.path for imports when running tests from repository root
CURRENT_DIR = os.path.dirname(__file__)
SRC_DIR = os.path.join(CURRENT_DIR, "..", "src")
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from truth_social.comment_parser import parse_comment  # noqa: E402

def load_sample_comment():
    data_path = os.path.join(CURRENT_DIR, "..", "data", "sample-output.json")
    with open(data_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data[0]

def test_parse_comment_basic_fields():
    raw = load_sample_comment()
    parsed = parse_comment(raw, clean_content=True)

    assert parsed["id"] == raw["id"]
    assert parsed["url"] == raw["url"]
    assert parsed["account_username"] == raw["account"]["username"]
    assert parsed["account_followers_count"] == raw["account"]["followers_count"]
    assert isinstance(parsed["replies_count"], int)
    assert "content_text" in parsed
    assert parsed["content_text"] != ""

def test_parse_comment_handles_missing_fields():
    raw = {
        "id": "abc",
        "created_at": None,
        "content": None,
        "account": {},
    }
    parsed = parse_comment(raw, clean_content=True)
    assert parsed["id"] == "abc"
    assert parsed["created_at"] is None
    assert parsed["content_text"] == ""