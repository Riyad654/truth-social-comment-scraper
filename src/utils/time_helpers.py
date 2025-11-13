thonfrom __future__ import annotations

from datetime import datetime, timezone
from typing import Optional

def parse_iso8601(value: Optional[str]) -> Optional[datetime]:
    """
    Parse a subset of ISO-8601 timestamps commonly seen in APIs.

    This covers patterns like:
        - 2025-02-04T03:40:19.675Z
        - 2024-01-07T03:04:09.098+00:00
    """
    if not value:
        return None

    value = value.strip()
    if value.endswith("Z"):
        value = value[:-1] + "+00:00"

    try:
        return datetime.fromisoformat(value)
    except ValueError:
        return None

def now_utc() -> datetime:
    return datetime.now(timezone.utc)