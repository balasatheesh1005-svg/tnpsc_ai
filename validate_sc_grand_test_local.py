# -*- coding: utf-8 -*-
"""
Local Validator for Supreme Court Grand Test (data/questions/polity/supreme_court_grand_test.json)
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

def validate_supreme_court_gt():
    file_path = "data/questions/polity/supreme_court_grand_test.json"
    
    if not os.path.exists(file_path):
        print(f"❌ Error: File {file_path} does not exist!")
        sys.exit(1)

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    print("=== LOCAL VALIDATION FOR SUPREME COURT GRAND TEST ===")
    print(f"File Path: {file_path}")
    print(f"Total Questions Count: {len(data)}")

    assert len(data) == 100, f"Expected 100 questions, found {len(data)}"

    ids = set()
    questions_en = set()
    questions_ta = set()
    key_counts = {"A": 0, "B": 0, "C": 0, "D": 0}
    diff_counts = {}
    type_counts = {}

    req_fields = [
        "id", "subject", "topic", "difficulty", "question_type",
        "question", "question_en", "question_ta", "options", "options_en", "options_ta",
        "correct_answer", "explanation", "explanation_en", "explanation_ta",
        "why_not_others", "trap_point", "tnpsc_tip", "high_yield_fact", "source_reference"
    ]

    for idx, item in enumerate(data, start=1):
        # 1. Field presence check
        for field in req_fields:
            assert field in item, f"Q{idx} missing field: {field}"

        # 2. Unique ID check
        q_id = item["id"]
        assert q_id not in ids, f"Duplicate ID found: {q_id}"
        ids.add(q_id)

        # 3. Unique Question text check
        q_en = item["question_en"].strip()
        q_ta = item["question_ta"].strip()
        assert q_en not in questions_en, f"Q{idx} duplicate English question stem"
        assert q_ta not in questions_ta, f"Q{idx} duplicate Tamil question stem"
        questions_en.add(q_en)
        questions_ta.add(q_ta)

        # 4. Options check
        options = item["options"]
        assert len(options) == 4, f"Q{idx} does not have exactly 4 options"
        opt_keys = [opt["id"] for opt in options]
        assert opt_keys == ["A", "B", "C", "D"], f"Q{idx} invalid option keys: {opt_keys}"

        opts_en = item["options_en"]
        opts_ta = item["options_ta"]
        assert len(opts_en) == 4 and len(opts_ta) == 4, f"Q{idx} options_en or options_ta missing keys"

        # 5. Correct answer check
        correct = item["correct_answer"]
        assert correct in ["A", "B", "C", "D"], f"Q{idx} invalid correct_answer: {correct}"
        key_counts[correct] += 1

        # 6. Bilingual presence check
        assert item["explanation_en"].strip(), f"Q{idx} missing explanation_en"
        assert item["explanation_ta"].strip(), f"Q{idx} missing explanation_ta"

        why_not = item["why_not_others"]
        for k in ["A", "B", "C", "D"]:
            assert k in why_not, f"Q{idx} why_not_others missing key {k}"
            assert "en" in why_not[k] and why_not[k]["en"].strip(), f"Q{idx} why_not_others[{k}] missing English"
            assert "ta" in why_not[k] and why_not[k]["ta"].strip(), f"Q{idx} why_not_others[{k}] missing Tamil"

        assert item["trap_point"]["en"].strip() and item["trap_point"]["ta"].strip(), f"Q{idx} trap_point incomplete"
        assert item["tnpsc_tip"]["en"].strip() and item["tnpsc_tip"]["ta"].strip(), f"Q{idx} tnpsc_tip incomplete"
        assert item["high_yield_fact"]["en"].strip() and item["high_yield_fact"]["ta"].strip(), f"Q{idx} high_yield_fact incomplete"

        # Stats collection
        diff = item["difficulty"]
        diff_counts[diff] = diff_counts.get(diff, 0) + 1

        q_type = item["question_type"]
        type_counts[q_type] = type_counts.get(q_type, 0) + 1

    print("\n✓ Valid JSON Format")
    print("✓ Exactly 100 MCQs")
    print("✓ All 100 Unique IDs (POLITY_SC_GT_001 to POLITY_SC_GT_100)")
    print("✓ All 100 Question stems unique in English and Tamil")
    print("✓ All required OLD schema fields present")

    print("\n--- Answer Key Balance ---")
    for k, v in key_counts.items():
        print(f"  Key {k}: {v}")
        assert 23 <= v <= 27, f"Key {k} count {v} outside target range 23-27"

    print("\n--- Difficulty Distribution ---")
    for k, v in diff_counts.items():
        print(f"  {k}: {v}")

    print("\n--- Question Model Distribution ---")
    for k, v in type_counts.items():
        print(f"  {k}: {v}")

    print("\n🎉 ALL LOCAL VALIDATION CHECKS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    validate_supreme_court_gt()
