# -*- coding: utf-8 -*-
"""
Master Builder for Electoral Reforms Grand Test (100 MCQs: ER_GT_001 to ER_GT_100).
- Combines 50 questions from build_er_gt_part1 and 50 questions from build_er_gt_part2.
- Verifies zero stem collision with all 325 Core questions.
- Rebalances answer keys to exactly 25 A, 25 B, 25 C, 25 D.
- Validates file with ContentValidator.
- Runs full topic suite validation (425 MCQs).
"""
import json
import os
from build_er_gt_part1 import get_gt_part1_questions
from build_er_gt_part2 import get_gt_part2_questions
from rebalance_er_helper import balance_question_keys
from tools.nova_content_engine.validator import ContentValidator

def main():
    part1_qs = get_gt_part1_questions()
    part2_qs = get_gt_part2_questions()
    all_gt = part1_qs + part2_qs
    print(f"Total Grand Test questions compiled: {len(all_gt)}")
    
    # 1. Check collisions with Core files
    core_files = [
        "data/questions/polity/electoral_reforms_easy.json",
        "data/questions/polity/electoral_reforms_medium.json",
        "data/questions/polity/electoral_reforms_hard.json",
        "data/questions/polity/electoral_reforms_statement_based.json",
        "data/questions/polity/electoral_reforms_reasoning.json",
        "data/questions/polity/electoral_reforms_chronology.json",
        "data/questions/polity/electoral_reforms_match_the_following.json",
        "data/questions/polity/electoral_reforms_pyq.json"
    ]
    core_stems = set()
    core_count = 0
    for cf in core_files:
        with open(cf, "r", encoding="utf-8") as f:
            data = json.load(f)
            for q in data:
                core_stems.add(q["question_en"].strip().lower())
                core_count += 1
                
    print(f"Total Core questions loaded: {core_count} (Unique stems: {len(core_stems)})")
    
    gt_stems = set()
    collisions = 0
    for q in all_gt:
        s = q["question_en"].strip().lower()
        if s in core_stems:
            print(f"COLLISION with Core: {q['id']} - {s[:60]}...")
            collisions += 1
        if s in gt_stems:
            print(f"COLLISION within GT: {q['id']} - {s[:60]}...")
            collisions += 1
        gt_stems.add(s)
        
    print(f"GT Collisions detected: {collisions}")
    if collisions > 0:
        raise ValueError("Collisions detected between Grand Test and Core files!")
        
    # 2. Rebalance answer keys to exactly 25 A, 25 B, 25 C, 25 D
    target_keys = {"A": 25, "B": 25, "C": 25, "D": 25}
    balanced_gt = balance_question_keys(all_gt, target_keys)
    
    out_dir = "data/questions/polity"
    os.makedirs(out_dir, exist_ok=True)
    gt_file = os.path.join(out_dir, "electoral_reforms_grand_test.json")
    
    with open(gt_file, "w", encoding="utf-8") as f:
        json.dump(balanced_gt, f, indent=2, ensure_ascii=False)
    print(f"Saved balanced Grand Test to {gt_file}")
    
    # 3. Validate Grand Test file
    validator = ContentValidator()
    report = validator.validate_file(gt_file, expected_count=100, expected_prefix="ER_GT_")
    print(f"Grand Test Validation: {'PASS' if report.is_valid else 'FAIL'} | Total: {report.total_audited}")
    print(f"Key Distribution: {report.key_distribution}")
    if not report.is_valid:
        for iss in report.issues:
            print("Issue:", iss.message)
            
    # 4. Validate Full Topic Suite
    print("\n--- RUNNING TOPIC SUITE VALIDATION ---")
    suite_files = {
        "easy": ("data/questions/polity/electoral_reforms_easy.json", 50, "ER_E_"),
        "medium": ("data/questions/polity/electoral_reforms_medium.json", 50, "ER_M_"),
        "hard": ("data/questions/polity/electoral_reforms_hard.json", 50, "ER_H_"),
        "statement": ("data/questions/polity/electoral_reforms_statement_based.json", 50, "ER_S_"),
        "reasoning": ("data/questions/polity/electoral_reforms_reasoning.json", 25, "ER_R_"),
        "chronology": ("data/questions/polity/electoral_reforms_chronology.json", 25, "ER_C_"),
        "match": ("data/questions/polity/electoral_reforms_match_the_following.json", 25, "ER_MF_"),
        "pyq": ("data/questions/polity/electoral_reforms_pyq.json", 50, "ER_PYQ_"),
        "grand_test": ("data/questions/polity/electoral_reforms_grand_test.json", 100, "ER_GT_")
    }
    suite_report = ContentValidator.validate_topic_suite(suite_files)
    print(f"Suite Status: {'PASS' if suite_report.is_valid else 'FAIL'}")
    print(f"Total Audited: {suite_report.total_audited}")
    print(f"Key Distribution: {suite_report.key_distribution}")
    print(f"Difficulty Distribution: {suite_report.difficulty_distribution}")
    if not suite_report.is_valid:
        print("Suite Issues:")
        for iss in suite_report.issues:
            print(" -", iss.severity, ":", iss.message)
    else:
        print("\nSUCCESS! ALL 425 QUESTIONS FULLY CERTIFIED WITH ZERO ISSUES!")

if __name__ == "__main__":
    main()
