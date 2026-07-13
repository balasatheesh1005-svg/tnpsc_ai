"""Validate the official Group 1 2011 answer key through public helpers."""

import json
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[4]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from core.question_engine.answer_key import (
    answer_key_exists,
    get_correct_answer,
    load_answer_key,
    refresh_answer_key_cache,
    verify_answer,
)
from core.question_engine.progress import is_correct_answer
from ui.question_engine.components import _format_official_answers


KEY_PATH = Path("data/official/answer_keys/group1/group1_2011_answer_key.json")
REPORT_PATH = Path("data/official/answer_keys/group1/answer_key_validation_report.json")
OPTION_KEYS = {"A", "B", "C", "D"}


def main():
    payload = json.loads(KEY_PATH.read_text(encoding="utf-8"))
    rows = payload.get("answers", {})
    expected_ids = [f"PYQ_G1_2011_{number:03d}" for number in range(1, 51)]
    actual_ids = list(rows)
    missing_ids = [question_id for question_id in expected_ids if question_id not in rows]
    unexpected_ids = [question_id for question_id in actual_ids if question_id not in expected_ids]
    duplicate_ids = [] if len(actual_ids) == len(set(actual_ids)) else sorted(
        question_id for question_id in set(actual_ids) if actual_ids.count(question_id) > 1
    )
    invalid_answers = []
    multi_answer_ids = []
    for question_id, row in rows.items():
        answers = row.get("correct_answers") if isinstance(row, dict) else None
        if not isinstance(answers, list) or not answers or any(answer not in OPTION_KEYS for answer in answers):
            invalid_answers.append(question_id)
        elif len(set(answers)) != len(answers):
            invalid_answers.append(question_id)
        elif len(answers) > 1:
            multi_answer_ids.append(question_id)

    refresh_answer_key_cache()
    helper_mismatches = []
    accepted_failures = []
    rejected_failures = []
    rejected_checks = 0
    for question_id in expected_ids:
        expected = rows.get(question_id, {}).get("correct_answers", [])
        resolved = get_correct_answer(question_id)
        if resolved != expected:
            helper_mismatches.append({"id": question_id, "expected": expected, "actual": resolved})
        for answer in expected:
            if verify_answer(question_id, answer) is not True or not is_correct_answer(answer, resolved):
                accepted_failures.append({"id": question_id, "answer": answer})
        rejected = next((answer for answer in sorted(OPTION_KEYS) if answer not in expected), None)
        if rejected:
            rejected_checks += 1
            if verify_answer(question_id, rejected) is not False or is_correct_answer(rejected, resolved):
                rejected_failures.append({"id": question_id, "answer": rejected})

    resolved_key = load_answer_key("Group 1", 2011)
    report = {
        "answer_key": str(KEY_PATH),
        "total_answers": len(rows),
        "single_answer_questions": len(rows) - len(multi_answer_ids),
        "ambiguous_question_ids": multi_answer_ids,
        "missing_answers": missing_ids,
        "unexpected_ids": unexpected_ids,
        "duplicate_ids": duplicate_ids,
        "invalid_option_answers": invalid_answers,
        "validation_result": "pass" if not (missing_ids or unexpected_ids or duplicate_ids or invalid_answers) else "fail",
        "answer_key_helper": {
            "named_key_path_resolves": bool(resolved_key),
            "answer_key_exists": answer_key_exists("Group 1", 2011),
            "resolution_mismatches": helper_mismatches,
        },
        "verification_result": {
            "all_50_question_ids_resolve": len(helper_mismatches) == 0,
            "accepted_option_checks": sum(len(row["correct_answers"]) for row in rows.values()),
            "accepted_option_failures": accepted_failures,
            "rejected_option_checks": rejected_checks,
            "rejected_option_failures": rejected_failures,
            "all_accepted_options_return_correct": not accepted_failures,
            "all_rejected_options_return_wrong": not rejected_failures,
            "all_option_questions_note": "Q4 and Q17 accept all A/B/C/D options, so no valid rejected option exists for those two official exceptions.",
        },
        "ui_contract": {
            "normal_question_example": _format_official_answers(get_correct_answer("PYQ_G1_2011_001")),
            "ambiguous_question_example": _format_official_answers(get_correct_answer("PYQ_G1_2011_015")),
            "normal_display": "Correct Answer: B",
            "ambiguous_display": "Official TNPSC Final Key accepts multiple answers: A, B",
        },
    }
    report["verification_result"]["result"] = "pass" if not (
        helper_mismatches or accepted_failures or rejected_failures
    ) else "fail"
    REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
