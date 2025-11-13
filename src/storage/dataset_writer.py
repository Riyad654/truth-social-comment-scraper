thonimport json
import logging
import os
from typing import Any, Dict, Iterable, List

from .json_exporter import export_json
from .csv_exporter import export_csv

logger = logging.getLogger("storage.dataset_writer")

class DatasetWriter:
    """
    Thin abstraction over JSON and CSV exporters.
    """

    SUPPORTED_FORMATS = ("json", "csv")

    def write_dataset(self, comments: Iterable[Dict[str, Any]], output_path: str, fmt: str = "json") -> str:
        if fmt not in self.SUPPORTED_FORMATS:
            raise ValueError(f"Unsupported output format: {fmt!r}. Supported: {self.SUPPORTED_FORMATS}")

        os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)

        comments_list: List[Dict[str, Any]] = list(comments)

        logger.info("Writing %d comments to %s (format=%s)", len(comments_list), output_path, fmt)

        if fmt == "json":
            export_json(comments_list, output_path)
        elif fmt == "csv":
            export_csv(comments_list, output_path)

        # Additionally write a small metadata sidecar for traceability.
        meta_path = f"{output_path}.meta.json"
        metadata = {
            "count": len(comments_list),
            "format": fmt,
            "output_path": os.path.abspath(output_path),
        }
        with open(meta_path, "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=2)

        logger.info("Wrote metadata to %s", meta_path)
        return output_path