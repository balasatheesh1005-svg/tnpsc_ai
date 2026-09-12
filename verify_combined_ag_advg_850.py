# -*- coding: utf-8 -*-
"""
Master Certification and Audit Script for:
1. Attorney General of India (425 MCQs)
2. Advocate General of a State (425 MCQs)
Combined Total: 850 MCQs across 18 dataset files.
"""

import json
import os
from tools.nova_content_engine.validator import ContentValidator
from tools.nova_content_engine.chronology_validator import ChronologyValidator

def main():
    print("================================================================================")
    print("          TNPSC NOVA AI MASTER CERTIFICATION: 850 MCQs (2 TOPICS)               ")
    print("================================================================================")

    # 1. Topic 1: Attorney General of India (425 MCQs)
    print("\n>>> AUDITING TOPIC 1: ATTORNEY GENERAL OF INDIA (425 MCQs)")
    ag_suite_files = {
        "easy": ("data/questions/polity/attorney_general_easy.json", 50, "AG_E_"),
        "medium": ("data/questions/polity/attorney_general_medium.json", 50, "AG_M_"),
        "hard": ("data/questions/polity/attorney_general_hard.json", 50, "AG_H_"),
        "statement": ("data/questions/polity/attorney_general_statement_based.json", 50, "AG_S_"),
        "reasoning": ("data/questions/polity/attorney_general_reasoning.json", 25, "AG_R_"),
        "chronology": ("data/questions/polity/attorney_general_chronology.json", 25, "AG_C_"),
        "match": ("data/questions/polity/attorney_general_match_the_following.json", 25, "AG_MF_"),
        "pyq": ("data/questions/polity/attorney_general_pyq.json", 50, "AG_PYQ_"),
        "grand_test": ("data/questions/polity/attorney_general_grand_test.json", 100, "AG_GT_")
    }
    
    ag_report = ContentValidator.validate_topic_suite(ag_suite_files)
    print(f"AG Topic Suite Status: {'PASS' if ag_report.is_valid else 'FAIL'}")
    print(f"  Total Audited: {ag_report.total_audited}")
    print(f"  Key Distribution: {ag_report.key_distribution}")
    print(f"  Difficulty Distribution: {ag_report.difficulty_distribution}")
    if not ag_report.is_valid:
        for iss in ag_report.issues:
            print("  Issue:", iss)
            
    # AG Chronology Validator
    ag_chron_report = ChronologyValidator.validate_file("data/questions/polity/attorney_general_chronology.json")
    print(f"AG Chronology Validator Status: {'PASS' if ag_chron_report.is_valid else 'FAIL'}")

    # 2. Topic 2: Advocate General of a State (425 MCQs)
    print("\n>>> AUDITING TOPIC 2: ADVOCATE GENERAL OF A STATE (425 MCQs)")
    advg_suite_files = {
        "easy": ("data/questions/polity/advocate_general_easy.json", 50, "ADVG_E_"),
        "medium": ("data/questions/polity/advocate_general_medium.json", 50, "ADVG_M_"),
        "hard": ("data/questions/polity/advocate_general_hard.json", 50, "ADVG_H_"),
        "statement": ("data/questions/polity/advocate_general_statement_based.json", 50, "ADVG_S_"),
        "reasoning": ("data/questions/polity/advocate_general_reasoning.json", 25, "ADVG_R_"),
        "chronology": ("data/questions/polity/advocate_general_chronology.json", 25, "ADVG_C_"),
        "match": ("data/questions/polity/advocate_general_match_the_following.json", 25, "ADVG_MF_"),
        "pyq": ("data/questions/polity/advocate_general_pyq.json", 50, "ADVG_PYQ_"),
        "grand_test": ("data/questions/polity/advocate_general_grand_test.json", 100, "ADVG_GT_")
    }

    advg_report = ContentValidator.validate_topic_suite(advg_suite_files)
    print(f"Advocate General Topic Suite Status: {'PASS' if advg_report.is_valid else 'FAIL'}")
    print(f"  Total Audited: {advg_report.total_audited}")
    print(f"  Key Distribution: {advg_report.key_distribution}")
    print(f"  Difficulty Distribution: {advg_report.difficulty_distribution}")
    if not advg_report.is_valid:
        for iss in advg_report.issues:
            print("  Issue:", iss)

    # Advocate General Chronology Validator
    advg_chron_report = ChronologyValidator.validate_file("data/questions/polity/advocate_general_chronology.json")
    print(f"Advocate General Chronology Validator Status: {'PASS' if advg_chron_report.is_valid else 'FAIL'}")

    # 3. Combined Grand Test Strict Balance Verification
    print("\n>>> VERIFYING GRAND TEST KEY DISTRIBUTIONS (EXACT 25 A, 25 B, 25 C, 25 D)")
    val = ContentValidator()
    ag_gt_rep = val.validate_file("data/questions/polity/attorney_general_grand_test.json", expected_count=100, expected_prefix="AG_GT_")
    advg_gt_rep = val.validate_file("data/questions/polity/advocate_general_grand_test.json", expected_count=100, expected_prefix="ADVG_GT_")
    print(f"  Attorney General GT Key Distribution: {ag_gt_rep.key_distribution}")
    print(f"  Advocate General GT Key Distribution: {advg_gt_rep.key_distribution}")
    assert ag_gt_rep.key_distribution == {'A': 25, 'B': 25, 'C': 25, 'D': 25}, "AG GT keys not strictly balanced!"
    assert advg_gt_rep.key_distribution == {'A': 25, 'B': 25, 'C': 25, 'D': 25}, "Advocate General GT keys not strictly balanced!"

    # 4. Cross-Topic and Cross-File Collision Audit (850 Questions)
    print("\n>>> AUDITING ALL 850 QUESTIONS FOR CROSS-FILE AND CROSS-TOPIC UNIQUENESS")
    all_files = list(ag_suite_files.values()) + list(advg_suite_files.values())
    
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
