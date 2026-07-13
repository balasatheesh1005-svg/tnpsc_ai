"""Final integrity checks for the imported 2011 dataset."""

import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[4]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from core.question_engine.validators import validate_questions


ROOT = Path(__file__).parent
DATASET = Path("data/pyq/group1/group1_2011_official.json")


def main():
    rows = json.loads(DATASET.read_text(encoding="utf-8"))
    schema = validate_questions(
        rows,
        required_fields=("id", "exam", "year", "subject", "question_en", "options", "explanation"),
    )
    expected_ids = [f"PYQ_G1_2011_{number:03d}" for number in range(1, 51)]
    field_errors = []
    if [row.get("id") for row in rows] != expected_ids:
        field_errors.append("id sequence mismatch")
    if [row.get("question_number") for row in rows] != list(range(1, 51)):
        field_errors.append("question number sequence mismatch")
    for row in rows:
        for field in ("correct_answer", "topic", "subtopic", "difficulty", "related_notes", "related_note", "ai_trick"):
            if row.get(field, "") not in ("", None):
                field_errors.append(f"{row.get('id')}: nonblank {field}")
        if row.get("explanation") != {"en": "", "ta": ""}:
            field_errors.append(f"{row.get('id')}: nonblank explanation")
        options = row.get("options", {})
        if set(options) != {"A", "B", "C", "D"} or any(not str(value).strip() for value in options.values()):
            field_errors.append(f"{row.get('id')}: invalid options")
    report = {
        "valid_count": len(rows) if schema.valid and not field_errors else 0,
        "invalid_count": len(field_errors),
        "duplicate_ids": [],
        "invalid_rows": [],
        "schema_errors": schema.errors,
        "schema_warnings": schema.warnings,
        "field_contract_errors": field_errors,
        "checks": {
            "record_count": len(rows),
            "sequential_ids": "id sequence mismatch" not in field_errors,
            "sequential_question_numbers": "question number sequence mismatch" not in field_errors,
            "all_options_complete": not any("invalid options" in error for error in field_errors),
            "verification_dependent_fields_blank": not any("nonblank" in error for error in field_errors),
        },
    }
    (ROOT / "validation_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
