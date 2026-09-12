# -*- coding: utf-8 -*-
"""
Builder and Assembler for Municipalities Grand Test (100 Questions)
Merges sub-modules 1-25, 26-50, 51-75, and 76-100, balances answer keys,
saves to data/questions/polity/municipalities_grand_test.json, and runs ContentValidator.
"""
import json
import os
from collections import Counter
from build_mun_gt_1_25 import get_gt_1_25
from build_mun_gt_26_50 import get_gt_26_50
from build_mun_gt_51_75 import get_gt_51_75
from build_mun_gt_76_100 import get_gt_76_100
from rebalance_mun_helper import balance_question_keys
from tools.nova_content_engine.validator import ContentValidator

def main():
    q1 = get_gt_1_25()
    q2 = get_gt_26_50()
    q3 = get_gt_51_75()
    q4 = get_gt_76_100()

    print(f"Loaded: Q1-25 ({len(q1)}), Q26-50 ({len(q2)}), Q51-75 ({len(q3)}), Q76-100 ({len(q4)})")
    all_questions = q1 + q2 + q3 + q4
    assert len(all_questions) == 100, f"Expected 100 questions, got {len(all_questions)}"

    # Ensure IDs are sequential MUN_GT_001 to MUN_GT_100
    for idx, q in enumerate(all_questions, 1):
        expected_id = f"MUN_GT_{idx:03d}"
        q["id"] = expected_id

    # Check initial key counts
    counts_before = Counter(q["correct_answer"] for q in all_questions)
    print("Key counts before balancing:", dict(counts_before))

    # Balance keys (25 each for A, B, C, D)
    balanced_questions = balance_question_keys(all_questions, target_counts={"A": 25, "B": 25, "C": 25, "D": 25})
    counts_after = Counter(q["correct_answer"] for q in balanced_questions)
    print("Key counts after balancing:", dict(counts_after))

    output_path = os.path.join("data", "questions", "polity", "municipalities_grand_test.json")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(balanced_questions, f, ensure_ascii=False, indent=2)

    print(f"Saved {len(balanced_questions)} questions to {output_path}")

    # Validate
    result = ContentValidator.validate_file(output_path, expected_count=100, expected_prefix="MUN_GT_")
    print("\n--- ContentValidator Summary ---")
    print(result.summary())
    if not result.is_valid:
        print("\nValidation Errors:")
        for err in result.errors:
            print(" -", err)
        for issue in result.issues:
            print(" - [Issue]:", issue)
    else:
        print("\nALL GRAND TEST QUESTIONS VALIDATED PERFECTLY! (PASS)")

if __name__ == "__main__":
    main()
