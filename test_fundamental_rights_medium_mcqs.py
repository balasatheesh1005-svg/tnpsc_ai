# -*- coding: utf-8 -*-
"""
Verification Suite for Fundamental Rights Medium 50 MCQs
"""

import sys
import json
import os

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

from core.question_loader import load_questions
from core.topics_loader import get_topic_metadata_by_id

def run_fr_medium_mcq_verification():
    print("================================================================================")
    print("🚀 RUNNING TNPSC NOVA AI - FUNDAMENTAL RIGHTS MEDIUM 50 MCQs VERIFICATION SUITE")
    print("================================================================================")

    # 1. File Existence & JSON Parsing
    file_path = "data/questions/polity/fundamental_rights_medium.json"
    print(f"\n[STEP 1] Validating File Existence & JSON Parsing: {file_path}")
    assert os.path.exists(file_path), f"❌ File not found: {file_path}"

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    print("   ✅ File exists and parses cleanly as valid JSON.")

    # 2. Question Count Audit
    print("\n[STEP 2] Question Count Audit")
    assert len(data) == 50, f"❌ Expected exactly 50 questions, found {len(data)}"
    print("   ✅ Exactly 50 questions present.")

    # 3. ID Uniqueness & Metadata Audit
    print("\n[STEP 3] ID Uniqueness & Metadata Audit")
    q_ids = [q["id"] for q in data]
    assert len(q_ids) == len(set(q_ids)), "❌ Duplicate question IDs found!"
    assert q_ids[0] == "FR_M_001" and q_ids[-1] == "FR_M_050", "❌ Incorrect ID range"
    print("   ✅ All 50 IDs are unique and follow FR_M_001 to FR_M_050 convention.")

    # 4. Question Structure & Bilingual Audit
    print("\n[STEP 4] Structure, Option Count & Bilingual Audit")
    ans_dist = {"A": 0, "B": 0, "C": 0, "D": 0}
    type_dist = {}

    for idx, q in enumerate(data, start=1):
        qid = q["id"]
        assert q.get("subject") == "Polity", f"❌ [{qid}] Invalid subject"
        assert q.get("topic") == "Fundamental Rights", f"❌ [{qid}] Invalid topic"
        assert q.get("difficulty") == "Medium", f"❌ [{qid}] Invalid difficulty"
        
        qtype = q.get("question_type", "Unknown")
        type_dist[qtype] = type_dist.get(qtype, 0) + 1

        # Question text
        qtext = q.get("question", {})
        assert "en" in qtext and len(qtext["en"].strip()) > 0, f"❌ [{qid}] Missing English question"
        assert "ta" in qtext and len(qtext["ta"].strip()) > 0, f"❌ [{qid}] Missing Tamil question"

        # Options
        opts = q.get("options", [])
        assert len(opts) == 4, f"❌ [{qid}] Must have exactly 4 options"
        opt_ids = [o["id"] for o in opts]
        assert opt_ids == ["A", "B", "C", "D"], f"❌ [{qid}] Option IDs must be A, B, C, D"
        
        for o in opts:
            assert len(o["en"].strip()) > 0, f"❌ [{qid}] Option {o['id']} missing English"
            assert len(o["ta"].strip()) > 0, f"❌ [{qid}] Option {o['id']} missing Tamil"

        # Correct Answer
        ca = q.get("correct_answer")
        assert ca in ["A", "B", "C", "D"], f"❌ [{qid}] Invalid correct_answer: {ca}"
        ans_dist[ca] += 1

        # Explanation
        exp = q.get("explanation", {})
        assert "en" in exp and len(exp["en"].strip()) > 0, f"❌ [{qid}] Missing English explanation"
        assert "ta" in exp and len(exp["ta"].strip()) > 0, f"❌ [{qid}] Missing Tamil explanation"

        # Why not others
        wno = q.get("why_not_others", {})
        for key in ["A", "B", "C", "D"]:
            assert key in wno, f"❌ [{qid}] Missing why_not_others for option {key}"
            assert "en" in wno[key] and "ta" in wno[key], f"❌ [{qid}] why_not_others for {key} must be bilingual"

        # TNPSC tip / takeaway
        tip = q.get("tnpsc_tip") or q.get("tnpsc_takeaway")
        assert tip is not None and "en" in tip and "ta" in tip, f"❌ [{qid}] Missing bilingual TNPSC tip/takeaway"

    print("   ✅ All 50 questions pass strict structural and bilingual audit.")
    print(f"   - Answer Distribution: {ans_dist}")
    print(f"   - Question Type Distribution: {type_dist}")

    # Verify distribution of question types
    assert type_dist.get("Conceptual Distinction", 0) >= 12, "❌ Missing Conceptual Distinction questions"
    assert type_dist.get("Article/Provision Based", 0) >= 8, "❌ Missing Article/Provision Based questions"
    assert type_dist.get("Application/Inference", 0) >= 6, "❌ Missing Application/Inference questions"
    assert type_dist.get("Case / Amendment", 0) >= 5, "❌ Missing Case / Amendment questions"
    assert type_dist.get("Elimination-Based", 0) >= 4, "❌ Missing Elimination-Based questions"
    assert type_dist.get("TNPSC Trap", 0) >= 4, "❌ Missing TNPSC Trap questions"

    # 5. Question Loader & Common Repository Integration Audit
    print("\n[STEP 5] Question Loader & Common Repository Integration Audit")
    
    # Test loading via repo ID
    q_main = load_questions("polity_fundamental_rights", "medium")
    assert len(q_main) == 50, f"❌ Loader failed to load 50 questions for repo_id 'polity_fundamental_rights', got {len(q_main)}"
    print("   ✅ load_questions('polity_fundamental_rights', 'medium') -> Loaded 50 questions!")

    # Test loading via Part 1, Part 2, Part 3 topic IDs
    parts = ["polity_fundamental_rights_part_1", "polity_fundamental_rights_part_2", "polity_fundamental_rights_part_3"]
    for p_topic in parts:
        p_questions = load_questions("polity", p_topic, "medium")
        assert len(p_questions) == 50, f"❌ Failed loading Medium repo for {p_topic}"
        assert p_questions[0]["id"] == "FR_M_001", f"❌ Incorrect first question ID for {p_topic}"
        print(f"   [OK] {p_topic} -> Practice -> Medium loads the SAME 50 questions!")

    # 6. Regression Check on Existing Medium Repositories
    print("\n[STEP 6] Regression Check on Existing Medium Repositories")
    reg_repos = [
        ("polity_historical_background", "medium"),
        ("polity_making_of_indian_constitution", "medium"),
        ("polity_preamble", "medium"),
        ("polity_salient_features_of_the_indian_constitution", "medium")
    ]
    for r_id, r_type in reg_repos:
        r_q = load_questions(r_id, r_type)
        assert len(r_q) > 0, f"❌ Regression failure for {r_id} ({r_type})"
        print(f"   [OK] {r_id} ({r_type}) -> Loaded {len(r_q)} questions.")

    print("\n================================================================================")
    print("🎉 ALL 6 VERIFICATION STEPS PASSED WITH 100% SUCCESS FOR MEDIUM MCQs!")
    print("================================================================================")

if __name__ == "__main__":
    run_fr_medium_mcq_verification()
