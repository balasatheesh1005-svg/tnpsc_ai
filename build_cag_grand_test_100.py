# -*- coding: utf-8 -*-
"""
Build 100 Grand Test MCQs for CAG (Comptroller & Auditor General of India)
ID range: CAG_GT_001 to CAG_GT_100
Strict requirements:
- Exactly 25 A, 25 B, 25 C, 25 D
- 0 stem collision with Core 325 questions
- 0 internal collisions
- 100% 24-field schema compliance
- Certified by ContentValidator
"""

import json
import os
from build_cag_gt_part1 import get_gt_part1_questions
from build_cag_gt_part2 import get_gt_part2_questions
from rebalance_er_helper import balance_question_keys
from tools.nova_content_engine.validator import ContentValidator

def build_grand_test():
    p1 = get_gt_part1_questions()
    p2 = get_gt_part2_questions()
    combined = p1 + p2
    assert len(combined) == 100, f"Expected 100 questions, got {len(combined)}"
    
    # Load all core stems
    core_files = [
        "data/questions/polity/cag_easy.json",
        "data/questions/polity/cag_medium.json",
        "data/questions/polity/cag_hard.json",
        "data/questions/polity/cag_statement_based.json",
        "data/questions/polity/cag_reasoning.json",
        "data/questions/polity/cag_chronology.json",
        "data/questions/polity/cag_match_the_following.json",
        "data/questions/polity/cag_pyq.json"
    ]
    core_stems = {}
    for cf in core_files:
        with open(cf, "r", encoding="utf-8") as f:
            cdata = json.load(f)
        for cq in cdata:
            cstem = cq.get("question_en", "").strip().lower()
            core_stems[cstem] = cq.get("id")
            
    print(f"Loaded {len(core_stems)} unique Core stems.")
    
    # Check for collisions with core or internal collisions
    gt_stems = {}
    for q in combined:
        stem = q.get("question_en", "").strip().lower()
        qid = q.get("id")
        if stem in core_stems:
            raise ValueError(f"Grand Test question {qid} collides with Core question {core_stems[stem]}: {stem[:60]}...")
        if stem in gt_stems:
            raise ValueError(f"Grand Test question {qid} collides internally with {gt_stems[stem]}: {stem[:60]}...")
        gt_stems[stem] = qid
        
    print(f"Grand Test collision audit: 100% PASS! 0 Core collisions, 0 internal collisions.")
    
    # Exactly balance keys: 25 A, 25 B, 25 C, 25 D
    target_counts = {"A": 25, "B": 25, "C": 25, "D": 25}
    balanced_qs = balance_question_keys(combined, target_counts=target_counts)
        
    # Verify counts
    key_counts = {}
    for q in balanced_qs:
        k = q["correct_answer"]
        key_counts[k] = key_counts.get(k, 0) + 1
    print(f"Grand Test key distribution: {key_counts}")
    assert key_counts == {"A": 25, "B": 25, "C": 25, "D": 25}, f"Distribution mismatch: {key_counts}"
    
    return balanced_qs

if __name__ == "__main__":
    gt_qs = build_grand_test()
    out_path = os.path.join("data", "questions", "polity", "cag_grand_test.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(gt_qs, f, ensure_ascii=False, indent=2)
    print(f"Saved 100 Grand Test MCQs to {out_path}")
    
    val = ContentValidator()
    report = val.validate_file(out_path, expected_count=100, expected_prefix="CAG_GT_")
    print(f"Validation Report: {'PASS' if report.is_valid else 'FAIL'} | Total: {report.total_audited}")
    if not report.is_valid:
        for iss in report.issues[:10]:
            print(f"  Issue: {iss}")
    print(f"Key Distribution: {report.key_distribution}")
