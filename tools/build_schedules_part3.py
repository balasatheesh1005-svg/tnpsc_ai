# -*- coding: utf-8 -*-
"""
Builder for Part 3 of Constitutional Schedules (100 MCQs):
- 100 Grand Test MCQs (SCH_GT_001 to SCH_GT_100)
- 100% independent from Core questions (zero duplicate English stems).
- Balanced answer distribution: exactly 25 A, 25 B, 25 C, 25 D.
- Anti-block rule: Max consecutive identical answers <= 2.
"""
import json
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.insert(0, os.path.dirname(__file__))

from sch_mcq_helper import balance_question_keys
from schedules_grand_test_data import get_grand_test_questions
from tools.nova_content_engine.answer_randomizer import audit_answer_pattern
from tools.nova_content_engine.validator import ContentValidator

def main():
    qs = get_grand_test_questions()
    print(f"Loaded {len(qs)} Grand Test questions.")
    assert len(qs) == 100, f"Expected 100 questions, got {len(qs)}"

    # Check stem uniqueness within Grand Test
    stems = [q["question_en"].strip().lower() for q in qs]
    assert len(stems) == len(set(stems)), "Duplicate English stems found within Grand Test questions!"

    # Balance and shuffle answer keys with anti-block rule (25 A, 25 B, 25 C, 25 D)
    target_counts = {"A": 25, "B": 25, "C": 25, "D": 25}
    balanced_qs = balance_question_keys(qs, target_counts=target_counts, seed=909)

    # Audit answer patterns
    keys = [q["correct_answer"] for q in balanced_qs]
    passed, issues = audit_answer_pattern(keys)
    print(f"Pattern audit result: passed={passed}, issues={issues}")
    assert passed, f"Pattern audit failed: {issues}"

    # Verify counts
    keys = [q["correct_answer"] for q in balanced_qs]
    counts = {k: keys.count(k) for k in "ABCD"}
    print(f"Answer key distribution: {counts}")
    assert counts == target_counts, f"Counts do not match target: {counts} vs {target_counts}"

    # Check max consecutive identical
    max_consec = 1
    cur_consec = 1
    for i in range(1, len(keys)):
        if keys[i] == keys[i - 1]:
            cur_consec += 1
            if cur_consec > max_consec:
                max_consec = cur_consec
        else:
            cur_consec = 1
    print(f"Max consecutive identical answer keys: {max_consec}")
    assert max_consec <= 2, f"Max consecutive keys exceeds 2: {max_consec}"

    # Write out to data/questions/polity/constitutional_schedules_grand_test.json
    out_dir = os.path.join(os.path.dirname(__file__), "..", "data", "questions", "polity")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "constitutional_schedules_grand_test.json")

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(balanced_qs, f, ensure_ascii=False, indent=2)
    print(f"Successfully saved {len(balanced_qs)} questions to {out_path}")

    # Validate with ContentValidator
    validator = ContentValidator()
    report = validator.validate_file(out_path)
    print(report.summary())
    if not report.is_valid:
        raise RuntimeError(f"Validation failed with {len(report.issues)} issues!")
    print("ContentValidator PASSED with 0 issues!")

if __name__ == "__main__":
    main()
