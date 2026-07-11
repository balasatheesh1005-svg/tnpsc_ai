"""Stage 3: validate normalized questions with existing validators."""

import json
from pathlib import Path
from typing import Any, Dict, List

from core.question_engine.constants import PYQ_REQUIRED_FIELDS
from core.question_engine.validators import validate_duplicate_ids, validate_question_schema


PIPELINE_REQUIRED_FIELDS = tuple(
    field
    for field in PYQ_REQUIRED_FIELDS
    if field not in {"correct_answer", "question_ta", "topic", "difficulty"}
)


def validate_questions_file(input_path, output_path=None, report_path=None) -> Dict[str, Any]:
    """Validate normalized questions and write validated_questions.json."""
    summary = {
        "input_path": str(input_path or ""),
        "output_path": str(output_path or "validated_questions.json"),
        "report_path": str(report_path or "validation_report.json"),
        "valid_count": 0,
        "invalid_count": 0,
        "duplicate_ids": [],
        "errors": [],
    }

    try:
        rows = _load_questions(Path(input_path))
        duplicate_result = validate_duplicate_ids(rows)
        duplicate_ids = _extract_duplicate_ids(duplicate_result.errors)
        summary["duplicate_ids"] = duplicate_ids

        valid_rows = []
        invalid_rows = []
        for index, question in enumerate(rows, start=1):
            row_errors = []
            if str(question.get("id") or "").strip() in duplicate_ids:
                row_errors.append("duplicate id")

            result = validate_question_schema(question, required_fields=PIPELINE_REQUIRED_FIELDS)
            row_errors.extend(result.errors)

            if row_errors:
                invalid_rows.append(
                    {
                        "index": index,
                        "id": question.get("id", ""),
                        "errors": row_errors,
                    }
                )
            else:
                valid_rows.append(question)

        output = Path(output_path or "validated_questions.json")
        report = Path(report_path or "validation_report.json")
        _write_json(output, {"questions": valid_rows})
        _write_json(
            report,
            {
                "valid_count": len(valid_rows),
                "invalid_count": len(invalid_rows),
                "duplicate_ids": duplicate_ids,
                "invalid_rows": invalid_rows,
            },
        )

        summary["output_path"] = str(output)
        summary["report_path"] = str(report)
        summary["valid_count"] = len(valid_rows)
        summary["invalid_count"] = len(invalid_rows)
        return summary
    except Exception as exc:
        summary["errors"].append(f"unexpected validator error: {exc}")
        _safe_write_empty(output_path or "validated_questions.json")
        return summary


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


def _extract_duplicate_ids(errors: List[str]) -> List[str]:
    ids = []
    for error in errors or []:
        if "duplicate IDs:" in error:
            ids.extend(item.strip() for item in error.split("duplicate IDs:", 1)[1].split(","))
    return sorted(item for item in ids if item)


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
