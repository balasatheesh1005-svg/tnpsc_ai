# -*- coding: utf-8 -*-
"""
Generator and Assembler for Election Commission Grand Test 100 MCQs (EC_GT_001 to EC_GT_100).
Strictly adheres to the 24-field schema:
- 100 questions covering all facets of Election Commission & Electoral System.
- 0 stem collisions with the 325 Core questions.
- Balanced answer keys: exactly 25 A, 25 B, 25 C, 25 D.
- Fully bilingual (English & Tamil).
"""

import json
import os
from collections import Counter
from rebalance_ec_helper import balance_question_keys
from build_ec_gt_part1 import get_gt_part1
from build_ec_gt_part2 import get_gt_part2
from build_ec_gt_part3 import get_gt_part3
from build_ec_gt_part4 import get_gt_part4
from tools.nova_content_engine.validator import ContentValidator

OUTPUT_PATH = os.path.join("data", "questions", "polity", "election_commission_grand_test.json")

CORE_FILES = [
    os.path.join("data", "questions", "polity", "election_commission_easy.json"),
    os.path.join("data", "questions", "polity", "election_commission_medium.json"),
    os.path.join("data", "questions", "polity", "election_commission_hard.json"),
    os.path.join("data", "questions", "polity", "election_commission_statement_based.json"),
    os.path.join("data", "questions", "polity", "election_commission_reasoning.json"),
    os.path.join("data", "questions", "polity", "election_commission_chronology.json"),
    os.path.join("data", "questions", "polity", "election_commission_match_the_following.json"),
    os.path.join("data", "questions", "polity", "election_commission_pyq.json")
]

def load_core_stems():
    stems = set()
    for cf in CORE_FILES:
        if os.path.exists(cf):
            with open(cf, "r", encoding="utf-8") as f:
                qs = json.load(f)
                for q in qs:
                    s = (q.get("question_en") or q.get("question", "")).strip().lower()
                    stems.add(s)
    return stems

def main():
    p1 = get_gt_part1()
    p2 = get_gt_part2()
    p3 = get_gt_part3()
    p4 = get_gt_part4()
    
    all_gt = p1 + p2 + p3 + p4
    print(f"Total Grand Test questions assembled: {len(all_gt)}")
    assert len(all_gt) == 100, f"Expected 100 questions, got {len(all_gt)}"
    
    # 1. Check ID uniqueness and sequential ordering
    ids = [q["id"] for q in all_gt]
    assert len(set(ids)) == 100, f"Duplicate IDs detected: {len(set(ids))} unique out of 100"
    for i in range(1, 101):
        expected_id = f"EC_GT_{i:03d}"
        assert ids[i-1] == expected_id, f"ID mismatch at index {i-1}: expected {expected_id}, got {ids[i-1]}"
        
    # 2. Check Intra-GT stem uniqueness
    gt_stems = [(q.get("question_en") or q.get("question", "")).strip().lower() for q in all_gt]
    assert len(set(gt_stems)) == 100, f"Duplicate stems within Grand Test: {len(set(gt_stems))} unique out of 100"
    
    # 3. Check GT vs Core stems independence
    core_stems = load_core_stems()
    overlap = set(gt_stems) & core_stems
    if overlap:
        print(f"ERROR: {len(overlap)} stem collisions between GT and Core questions:")
        for s in overlap:
            print(" -", s[:80])
        raise ValueError("Grand Test stems must have 0 collisions with Core files!")
    else:
        print("PASS: 0 collisions between Grand Test and Core questions (100% independent).")
        
    # 4. Balance answer keys to exactly 25 A, 25 B, 25 C, 25 D
    balanced_gt = balance_question_keys(all_gt, target_counts={"A": 25, "B": 25, "C": 25, "D": 25})
    key_counts = Counter(q["correct_answer"] for q in balanced_gt)
    print("Balanced Answer Keys:", dict(key_counts))
    assert key_counts == {"A": 25, "B": 25, "C": 25, "D": 25}, f"Key counts not balanced: {key_counts}"
    
    # 5. Write to output file
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(balanced_gt, f, ensure_ascii=False, indent=2)
    print(f"Grand Test saved to {OUTPUT_PATH}")
    
    # 6. Validate single file
    validator = ContentValidator()
    report = validator.validate_file(OUTPUT_PATH, expected_count=100, expected_prefix="EC_GT_")
    print("\n--- Grand Test File Validation Report ---")
    print(report.summary())
    assert report.is_valid, "Grand Test file validation failed!"

if __name__ == "__main__":
    main()
