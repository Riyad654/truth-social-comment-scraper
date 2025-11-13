thonimport json
from typing import Any, Dict, Iterable, List

def export_json(comments: Iterable[Dict[str, Any]], output_path: str) -> None:
    """
    Export the given comments as a JSON array.
    """
    comments_list: List[Dict[str, Any]] = list(comments)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(comments_list, f, indent=2, ensure_ascii=False)