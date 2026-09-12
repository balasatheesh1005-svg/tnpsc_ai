# -*- coding: utf-8 -*-
"""
Assembler and Validator for Grand Test (100 Questions: UT_GT_001 to UT_GT_100)
on Union & Its Territory (polity_union_territory).
Checks zero duplicate stems against all 325 Core questions, balances keys (25 each),
and runs ContentValidator.
"""
import json
import os
import sys
from build_ut_gt_part1 import get_gt_part1
from build_ut_gt_part2 import get_gt_part2
from ut_mcq_helper import balance_question_keys
from tools.nova_content_engine.validator import ContentValidator

def main():
    part1 = get_gt_part1()
    part2 = get_gt_part2()
    all_gt = part1 + part2
    print(f"Total Grand Test questions loaded: {len(all_gt)}")
    
    if len(all_gt) != 100:
        print(f"ERROR: Expected 100 questions, got {len(all_gt)}")
        sys.exit(1)
        
    for idx, q in enumerate(all_gt, 1):
        q["id"] = f"UT_GT_{idx:03d}"
        
    # Check for duplicate stems within Grand Test
    gt_stems = {}
    for q in all_gt:
        stem = q["question_en"].strip().lower()
        if stem in gt_stems:
            print(f"ERROR: Duplicate stem in GT: {q['id']} and {gt_stems[stem]}")
            sys.exit(1)
        gt_stems[stem] = q["id"]
        
    # Check against all 325 Core questions
    core_dir = os.path.join("data", "questions", "polity")
    core_files = [
        "union_territory_easy.json",
        "union_territory_medium.json",
        "union_territory_hard.json",
        "union_territory_statement_based.json",
        "union_territory_pyq.json",
        "union_territory_reasoning.json",
        "union_territory_match_the_following.json",
        "union_territory_chronology.json"
    ]
    
    core_stems = {}
    total_core = 0
    for fname in core_files:
        fpath = os.path.join(core_dir, fname)
        if not os.path.exists(fpath):
            print(f"ERROR: Missing core file: {fpath}")
            sys.exit(1)
        with open(fpath, "r", encoding="utf-8") as f:
            qs = json.load(f)
            total_core += len(qs)
            for q in qs:
                stem = q.get("question_en", "").strip().lower()
                core_stems[stem] = q.get("id")
                
    print(f"Loaded {total_core} Core questions for independence cross-check.")
    
    collision_count = 0
    for q in all_gt:
        stem = q["question_en"].strip().lower()
        if stem in core_stems:
            print(f"COLLISION: GT question {q['id']} matches Core question {core_stems[stem]}!")
            collision_count += 1
            
    if collision_count > 0:
        print(f"FAILED: Found {collision_count} stem collisions with Core!")
        sys.exit(1)
    else:
        print("PASS: 100% independence confirmed! Zero duplicate stems between Core and Grand Test.")
        
    # Balance keys across A, B, C, D (25 each)
    balanced_gt = balance_question_keys(all_gt)
    
    # Save to grand_test file
    out_file = os.path.join(core_dir, "union_territory_grand_test.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(balanced_gt, f, ensure_ascii=False, indent=2)
    print(f"Saved 100 questions to {out_file}")
    
    # Run ContentValidator
    res = ContentValidator.validate_file(out_file, expected_count=100, expected_prefix="UT_GT_")
    print("\n--- ContentValidator Summary ---")
    print(res.summary())
    if not res.is_valid:
        print("Issues found:")
        for issue in res.issues:
            print(f" - [{issue.severity}] {issue.field}: {issue.message}")
        sys.exit(1)
    else:
        print("\nALL 100 GRAND TEST QUESTIONS VALIDATED PERFECTLY! (PASS)")

if __name__ == "__main__":
    main()
