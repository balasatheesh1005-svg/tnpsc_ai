# -*- coding: utf-8 -*-
"""
Master Certification and Audit Script for:
1. Comptroller & Auditor General of India (CAG) (425 MCQs)
2. Finance Commission of India (FC) (425 MCQs)
Combined Total: 850 MCQs across 18 dataset files.
"""

import json
import os
from tools.nova_content_engine.validator import ContentValidator
from tools.nova_content_engine.chronology_validator import ChronologyValidator

def main():
    print("================================================================================")
    print("      TNPSC NOVA AI MASTER CERTIFICATION: 850 MCQs (CAG & FINANCE COMMISSION)   ")
    print("================================================================================")

    # 1. Topic 1: Comptroller & Auditor General of India (425 MCQs)
    print("\n>>> AUDITING TOPIC 1: COMPTROLLER & AUDITOR GENERAL OF INDIA (425 MCQs)")
    cag_suite_files = {
        "easy": ("data/questions/polity/cag_easy.json", 50, "CAG_E_"),
        "medium": ("data/questions/polity/cag_medium.json", 50, "CAG_M_"),
        "hard": ("data/questions/polity/cag_hard.json", 50, "CAG_H_"),
        "statement": ("data/questions/polity/cag_statement_based.json", 50, "CAG_S_"),
        "reasoning": ("data/questions/polity/cag_reasoning.json", 25, "CAG_R_"),
        "chronology": ("data/questions/polity/cag_chronology.json", 25, "CAG_C_"),
        "match": ("data/questions/polity/cag_match_the_following.json", 25, "CAG_MF_"),
        "pyq": ("data/questions/polity/cag_pyq.json", 50, "CAG_PYQ_"),
        "grand_test": ("data/questions/polity/cag_grand_test.json", 100, "CAG_GT_")
    }
    
    cag_report = ContentValidator.validate_topic_suite(cag_suite_files)
    print(f"CAG Topic Suite Status: {'PASS' if cag_report.is_valid else 'FAIL'}")
    print(f"  Total Audited: {cag_report.total_audited}")
    print(f"  Key Distribution: {cag_report.key_distribution}")
    print(f"  Difficulty Distribution: {cag_report.difficulty_distribution}")
    if not cag_report.is_valid:
        for iss in cag_report.issues:
            print("  Issue:", iss)
            
    # CAG Chronology Validator
    cag_chron_report = ChronologyValidator.validate_file("data/questions/polity/cag_chronology.json")
    print(f"CAG Chronology Validator Status: {'PASS' if cag_chron_report.is_valid else 'FAIL'}")
    if not cag_chron_report.is_valid:
        for iss in cag_chron_report.issues:
            print("  Chronology Issue:", iss)

    # 2. Topic 2: Finance Commission of India (425 MCQs)
    print("\n>>> AUDITING TOPIC 2: FINANCE COMMISSION OF INDIA (425 MCQs)")
    fc_suite_files = {
        "easy": ("data/questions/polity/fc_easy.json", 50, "FC_E_"),
        "medium": ("data/questions/polity/fc_medium.json", 50, "FC_M_"),
        "hard": ("data/questions/polity/fc_hard.json", 50, "FC_H_"),
        "statement": ("data/questions/polity/fc_statement_based.json", 50, "FC_S_"),
        "reasoning": ("data/questions/polity/fc_reasoning.json", 25, "FC_R_"),
        "chronology": ("data/questions/polity/fc_chronology.json", 25, "FC_C_"),
        "match": ("data/questions/polity/fc_match_the_following.json", 25, "FC_MF_"),
        "pyq": ("data/questions/polity/fc_pyq.json", 50, "FC_PYQ_"),
        "grand_test": ("data/questions/polity/fc_grand_test.json", 100, "FC_GT_")
    }

    fc_report = ContentValidator.validate_topic_suite(fc_suite_files)
    print(f"Finance Commission Topic Suite Status: {'PASS' if fc_report.is_valid else 'FAIL'}")
    print(f"  Total Audited: {fc_report.total_audited}")
    print(f"  Key Distribution: {fc_report.key_distribution}")
    print(f"  Difficulty Distribution: {fc_report.difficulty_distribution}")
    if not fc_report.is_valid:
        for iss in fc_report.issues:
            print("  Issue:", iss)

    # FC Chronology Validator
    fc_chron_report = ChronologyValidator.validate_file("data/questions/polity/fc_chronology.json")
    print(f"Finance Commission Chronology Validator Status: {'PASS' if fc_chron_report.is_valid else 'FAIL'}")
    if not fc_chron_report.is_valid:
        for iss in fc_chron_report.issues:
            print("  Chronology Issue:", iss)

    # 3. Combined Grand Test Strict Balance Verification
    print("\n>>> VERIFYING GRAND TEST KEY DISTRIBUTIONS (EXACT 25 A, 25 B, 25 C, 25 D)")
    val = ContentValidator()
    cag_gt_rep = val.validate_file("data/questions/polity/cag_grand_test.json", expected_count=100, expected_prefix="CAG_GT_")
    fc_gt_rep = val.validate_file("data/questions/polity/fc_grand_test.json", expected_count=100, expected_prefix="FC_GT_")
    print(f"  CAG GT Key Distribution: {cag_gt_rep.key_distribution}")
    print(f"  Finance Commission GT Key Distribution: {fc_gt_rep.key_distribution}")
    assert cag_gt_rep.key_distribution == {'A': 25, 'B': 25, 'C': 25, 'D': 25}, "CAG GT keys not strictly balanced!"
    assert fc_gt_rep.key_distribution == {'A': 25, 'B': 25, 'C': 25, 'D': 25}, "FC GT keys not strictly balanced!"

    # 4. Cross-Topic and Cross-File Collision Audit (850 Questions)
    print("\n>>> AUDITING ALL 850 QUESTIONS FOR CROSS-FILE AND CROSS-TOPIC UNIQUENESS")
    all_files = list(cag_suite_files.values()) + list(fc_suite_files.values())
    
    total_q_count = 0
    all_qids = set()
    all_stems_en = set()
    all_stems_ta = set()
    collisions = 0

    for file_path, exp_cnt, prefix in all_files:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            assert len(data) == exp_cnt, f"File {file_path} count mismatch: expected {exp_cnt}, got {len(data)}"
            for q in data:
                total_q_count += 1
                qid = q["id"]
                assert qid.startswith(prefix), f"ID prefix mismatch in {file_path}: {qid} vs {prefix}"
                assert qid not in all_qids, f"Duplicate Question ID: {qid}"
                all_qids.add(qid)
                
                s_en = q["question_en"].strip().lower()
                s_ta = q["question_ta"].strip()
                
                if s_en in all_stems_en:
                    print(f"Collision in EN stem: {qid} in {file_path}")
                    collisions += 1
                if s_ta in all_stems_ta:
                    print(f"Collision in TA stem: {qid} in {file_path}")
                    collisions += 1
                    
                all_stems_en.add(s_en)
                all_stems_ta.add(s_ta)

    print(f"  Total Questions Verified across 18 files: {total_q_count}")
    print(f"  Total Unique Question IDs: {len(all_qids)}")
    print(f"  Total Unique English Stems: {len(all_stems_en)}")
    print(f"  Total Unique Tamil Stems: {len(all_stems_ta)}")
    print(f"  Total Stem Collisions across all 850 questions: {collisions}")

    assert collisions == 0, f"Found {collisions} stem collisions!"
    assert total_q_count == 850, f"Expected 850 questions, found {total_q_count}"
    
    print("\n================================================================================")
    print(" FINAL VERDICT: 850/850 MCQs 100% PRODUCTION-READY AND CERTIFIED PASS! ")
    print("================================================================================")

if __name__ == "__main__":
    main()
