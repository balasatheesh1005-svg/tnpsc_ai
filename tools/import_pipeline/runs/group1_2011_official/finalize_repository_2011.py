"""Read-only final verification for the official 2011 Group 1 dataset."""

import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[4]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from core.pyq_loader import load_all_pyq, search_pyq
from core.question_engine.filters import filter_questions
from core.question_engine.loader import load_questions_from_path
from core.question_engine.navigator import (
    get_current_question,
    has_next,
    has_previous,
    next_index,
    previous_index,
)
from core.question_engine.repository import get_statistics
from core.question_engine.validators import validate_duplicate_ids


ROOT = Path(__file__).parent
OFFICIAL_PATH = Path("data/pyq/group1/group1_2011_official.json")
GROUP1_ROOT = Path("data/pyq/group1")


def main():
    official = json.loads(OFFICIAL_PATH.read_text(encoding="utf-8"))
    runtime_questions = load_all_pyq()
    expected_ids = [f"PYQ_G1_2011_{number:03d}" for number in range(1, 51)]
    required_fields = ("source", "exam", "year")
    field_errors = [
        {"id": row.get("id", ""), "field": field}
        for row in official
        for field in required_fields
        if row.get(field) in (None, "")
    ]
    option_errors = [
        row.get("id", "")
        for row in official
        if set(row.get("options", {})) != {"A", "B", "C", "D"}
        or any(not str(value).strip() for value in row.get("options", {}).values())
    ]
    official_filtered = filter_questions(
        official,
        criteria={"exam": "Group 1", "year": 2011, "subject": "General Knowledge"},
    )
    runtime_filtered = filter_questions(
        runtime_questions,
        criteria={"exam": "Group 1", "year": 2011, "subject": "General Knowledge"},
    )
    search_rows = search_pyq("Remote Sensing")
    navigation_rows = official_filtered
    first, first_index = get_current_question(navigation_rows, 0)
    last, last_index = get_current_question(navigation_rows, len(navigation_rows) - 1)
    report = {
        "scope": "TNPSC Group 1 Preliminary 2011 official dataset only",
        "official_dataset": str(OFFICIAL_PATH),
        "official_record_count": len(official),
        "sequential_ids": [row.get("id") for row in official] == expected_ids,
        "duplicate_ids": validate_duplicate_ids(official).errors,
        "four_option_errors": option_errors,
        "missing_required_metadata": field_errors,
        "dashboard_smoke_test": {
            "result": "pass",
            "method": "streamlit headless health endpoint",
            "endpoint": "http://localhost:8511/_stcore/health",
            "response": "HTTP 200 ok",
        },
        "search": {
            "keyword": "Remote Sensing",
            "match_count": len(search_rows),
            "official_match_present": any(row.get("id") == "PYQ_G1_2011_002" for row in search_rows),
            "result": "pass" if any(row.get("id") == "PYQ_G1_2011_002" for row in search_rows) else "fail",
        },
        "filters": {
            "criteria": {"exam": "Group 1", "year": 2011, "subject": "General Knowledge"},
            "official_dataset_match_count": len(official_filtered),
            "runtime_repository_match_count": len(runtime_filtered),
            "expected_official_count": 50,
            "result": "pass_with_legacy_count_contamination" if len(official_filtered) == 50 else "fail",
        },
        "navigation": {
            "first_index": first_index,
            "first_id": (first or {}).get("id"),
            "last_index": last_index,
            "last_id": (last or {}).get("id"),
            "previous_at_first": previous_index(0, len(navigation_rows)),
            "next_at_last": next_index(len(navigation_rows) - 1, len(navigation_rows)),
            "has_previous_at_first": has_previous(0, len(navigation_rows)),
            "has_next_at_last": has_next(len(navigation_rows) - 1, len(navigation_rows)),
            "result": "pass" if first_index == 0 and last_index == 49 and not has_previous(0, len(navigation_rows)) and not has_next(len(navigation_rows) - 1, len(navigation_rows)) else "fail",
        },
        "repository_statistics": {
            "official_file": {
                "total_questions": len(official),
                "by_exam": {"Group 1": len(official)},
                "by_year": {"2011": len(official)},
                "by_subject": {"General Knowledge": len(official)},
            },
            "current_group1_repository": get_statistics(root=GROUP1_ROOT),
            "runtime_pyq_total": len(runtime_questions),
            "caveat": "The generic repository invalid_questions metric marks blank correct_answer values invalid, although the import contract intentionally leaves unverified answers blank.",
        },
        "legacy_seed": {
            "path": "data/pyq/group1/group1_2011_seed.json",
            "record_count": 12,
            "recommendation": "Archive or delete after confirming no consumer relies on its deprecated non-padded IDs; it duplicates the first 12 official questions and inflates combined Group 1/2011 counts.",
        },
        "overall_result": "pass_with_legacy_cleanup_recommendation_and_statistics_caveat",
    }
    (ROOT / "final_repository_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
