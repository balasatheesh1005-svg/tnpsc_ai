"""Stage 6: import enriched questions into the JSON question repository."""

import json
import re
from pathlib import Path
from typing import Any, Dict, List

from core.question_engine.constants import DEFAULT_QUESTION_ROOT, SOURCE_JSON
from core.question_engine.loader import refresh_question_cache
from core.question_engine.repository import get_questions


def import_to_repository(input_path, repository_root=DEFAULT_QUESTION_ROOT, output_file=None) -> Dict[str, Any]:
    """Import enriched questions into the repository without crashing."""
    summary = {
        "input_path": str(input_path or ""),
        "repository_root": str(repository_root),
        "output_file": "",
        "imported_count": 0,
        "skipped_count": 0,
        "duplicate_count": 0,
        "errors": [],
    }

    try:
        rows = _load_questions(Path(input_path))
        root = Path(repository_root)
        existing_ids = _load_existing_ids(root)

        importable = []
        for row in rows:
            question_id = str(row.get("id") or "").strip()
            if not question_id:
                summary["skipped_count"] += 1
                summary["errors"].append("skipped row with missing id")
                continue
            if question_id in existing_ids:
                summary["duplicate_count"] += 1
                summary["skipped_count"] += 1
                summary["errors"].append(f"duplicate id skipped: {question_id}")
                continue
            importable.append(row)
            existing_ids.add(question_id)

        target = Path(output_file) if output_file else _default_output_file(root, importable)
        if importable:
            _write_repository_file(target, importable)
            refresh_question_cache()

        summary["output_file"] = str(target)
        summary["imported_count"] = len(importable)
        return summary
    except Exception as exc:
        summary["errors"].append(f"unexpected repository import error: {exc}")
        return summary


def _load_existing_ids(root: Path) -> set:
    try:
        return {
            str(question.get("id") or "").strip()
            for question in get_questions(source=SOURCE_JSON, root=root)
            if str(question.get("id") or "").strip()
        }
    except Exception:
        return set()


def _default_output_file(root: Path, rows: List[Dict[str, Any]]) -> Path:
    first = rows[0] if rows else {}
    exam = _slug(first.get("exam") or "imported")
    year = str(first.get("year") or "unknown")
    return root / exam / f"{exam}_{year}_import_pipeline.json"


def _write_repository_file(path: Path, rows: List[Dict[str, Any]]) -> None:
    existing = []
    if path.exists():
        try:
            with path.open("r", encoding="utf-8") as file:
                data = json.load(file)
            if isinstance(data, dict) and isinstance(data.get("questions"), list):
                existing = [row for row in data["questions"] if isinstance(row, dict)]
            elif isinstance(data, list):
                existing = [row for row in data if isinstance(row, dict)]
        except Exception:
            existing = []

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        json.dump(existing + rows, file, ensure_ascii=False, indent=2)
        file.write("\n")


def _load_questions(path: Path) -> List[Dict[str, Any]]:
    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)
        if isinstance(data, dict) and isinstance(data.get("questions"), list):
            return [row for row in data["questions"] if isinstance(row, dict)]
        if isinstance(data, list):
            return [row for row in data if isinstance(row, dict)]
    except Exception:
        return []
    return []


def _slug(value: Any) -> str:
    text = str(value or "").strip().lower()
    text = re.sub(r"[^a-z0-9]+", "", text)
    return text or "imported"
