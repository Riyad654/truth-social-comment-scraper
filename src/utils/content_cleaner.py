thonimport html
import re
from typing import Optional

HTML_TAG_RE = re.compile(r"<[^>]+>")

def clean_html_content(content: Optional[str]) -> str:
    """
    Very small helper that strips HTML tags and unescapes HTML entities, leaving
    a plain-text representation of the comment content.
    """
    if not content:
        return ""
    text = HTML_TAG_RE.sub(" ", content)
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text).strip()
    return text