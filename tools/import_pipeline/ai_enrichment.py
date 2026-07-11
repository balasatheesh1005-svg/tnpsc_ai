"""Stage 5: create empty AI enrichment placeholders only."""

import json
from pathlib import Path
from typing import Any, Dict, List


def enrich_placeholders(input_path, output_path=None) -> Dict[str, Any]:
    """Add empty enrichment fields without calling external APIs."""
    summary = {
        "input_path": str(input_path or ""),
        "output_path": str(output_path or "enriched_questions.json"),
        "question_count": 0,
        "errors": [],
    }

    try:
        rows = _load_questions(Path(input_path))
        enriched = []
        for question in rows:
            row = dict(question)
            row["topic"] = row.get("topic") or ""
            row["subtopic"] = row.get("subtopic") or ""
            row["difficulty"] = row.get("difficulty") or ""
            row["related_notes"] = row.get("related_notes") or ""
            row["related_note"] = row.get("related_note") or ""
            row["tags"] = row.get("tags") if isinstance(row.get("tags"), list) else []
            row["ai_trick"] = row.get("ai_trick") or ""
            row["english_explanation"] = row.get("english_explanation") or ""
            row["tamil_explanation"] = row.get("tamil_explanation") or ""
            row["explanation"] = _normalize_explanation(row.get("explanation"))
            enriched.append(row)

        output = Path(output_path or "enriched_questions.json")
        _write_json(output, {"questions": enriched})
        summary["output_path"] = str(output)
        summary["question_count"] = len(enriched)
        return summary
    except Exception as exc:
        summary["errors"].append(f"unexpected AI placeholder error: {exc}")
        _safe_write_empty(output_path or "enriched_questions.json")
        return summary


def _normalize_explanation(value: Any) -> Dict[str, str]:
    if isinstance(value, dict):
        return {
            "en": str(value.get("en") or value.get("english") or ""),
            "ta": str(value.get("ta") or value.get("tamil") or ""),
        }
    return {"en": "", "ta": ""}


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


def _write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        json.dump(payload, file, ensure_ascii=False, indent=2)
        file.write("\n")


def _safe_write_empty(output_path) -> None:
    try:
        _write_json(Path(output_path), {"questions": []})
    except Exception:
        return
