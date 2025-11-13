thonimport os
import sys
from urllib.parse import urlparse

import pytest

# Ensure src/ is on sys.path for imports when running tests from repository root
CURRENT_DIR = os.path.dirname(__file__)
SRC_DIR = os.path.join(CURRENT_DIR, "..", "src")
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from truth_social.client import TruthSocialClient  # noqa: E402

class DummySession:
    def __init__(self, response_json):
        self._response_json = response_json
        self.last_request = None

    class _Resp:
        def __init__(self, json_data):
            self._json_data = json_data
            self.status_code = 200
            self.text = "OK"

        def raise_for_status(self):
            return None

        def json(self):
            return self._json_data

    def request(self, method, url, **kwargs):
        self.last_request = (method, url, kwargs)
        return DummySession._Resp(self._response_json)

def test_resolve_post_id_from_numeric():
    client = TruthSocialClient()
    assert client.resolve_post_id("123456") == "123456"

def test_resolve_post_id_from_url():
    client = TruthSocialClient()
    url = "https://truthsocial.com/@user/123456"
    post_id = client.resolve_post_id(url)
    assert post_id == "123456"

def test_resolve_post_id_invalid_url():
    client = TruthSocialClient()
    with pytest.raises(ValueError):
        client.resolve_post_id("https://truthsocial.com/@user/not-an-id")

def test_fetch_comments_uses_context_endpoint():
    fake_json = {
        "ancestors": [],
        "descendants": [
            {"id": "1", "created_at": "2025-01-01T00:00:00Z"},
            {"id": "2", "created_at": "2025-01-02T00:00:00Z"},
        ],
    }
    session = DummySession(fake_json)
    client = TruthSocialClient(session=session)
    comments = client.fetch_comments("123456", sort="newest")
    assert [c["id"] for c in comments] == ["2", "1"]

    method, url, kwargs = session.last_request
    parsed = urlparse(url)
    assert method == "GET"
    assert parsed.path.endswith("/api/v1/statuses/123456/context")