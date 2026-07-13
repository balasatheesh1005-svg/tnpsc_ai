"""Write the standard V2 JSON reports."""
import json
from pathlib import Path
from collections import Counter


def generate(work_dir, summary):
    directory = Path(work_dir)
    directory.mkdir(parents=True, exist_ok=True)
    questions = summary.get("questions", [])
    reports = {
        "import_summary.json": {"input_pdf": summary.get("input_pdf"), "extracted_blocks": summary.get("extracted_blocks", 0), "parsed_questions": summary.get("parsed_questions", 0), "imported_count": len(questions), "status": summary.get("status")},
        "validation_report.json": summary.get("validation", {}),
        "duplicate_report.json": summary.get("duplicate", {}),
        "subject_report.json": {"counts": dict(Counter(row.get("subject", "") for row in questions))},
        "topic_report.json": {"counts": dict(Counter(row.get("topic", "") for row in questions))},
        "difficulty_report.json": {"counts": dict(Counter(row.get("difficulty", "") for row in questions))},
        "answerkey_report.json": summary.get("answer_key", {}),
        "repository_report.json": summary.get("repository", {}),
    }
    paths = {}
    for name, payload in reports.items():
        path = directory / name
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        paths[name] = str(path)
    return paths
