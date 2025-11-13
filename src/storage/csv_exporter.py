thonimport csv
from typing import Any, Dict, Iterable, List

CORE_FIELDS = [
    "id",
    "created_at",
    "edited_at",
    "language",
    "url",
    "content_text",
    "replies_count",
    "reblogs_count",
    "favourites_count",
    "account_username",
    "account_display_name",
    "account_followers_count",
]

def _flatten_comment(comment: Dict[str, Any]) -> Dict[str, Any]:
    """
    Flatten a single parsed comment into a dict compatible with CSV writing.
    Only the CORE_FIELDS are included.
    """
    flat: Dict[str, Any] = {}
    for field in CORE_FIELDS:
        flat[field] = comment.get(field)
    return flat

def export_csv(comments: Iterable[Dict[str, Any]], output_path: str) -> None:
    """
    Export the given comments as a CSV file with a defined subset of fields.
    """
    comments_list: List[Dict[str, Any]] = list(comments)

    with open(output_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=CORE_FIELDS)
        writer.writeheader()
        for comment in comments_list:
            writer.writerow(_flatten_comment(comment))