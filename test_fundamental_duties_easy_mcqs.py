# -*- coding: utf-8 -*-
"""
Validation & Verification Test Suite for Fundamental Duties Easy 50 MCQs
"""

import sys
import json
import os

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

from core.question_loader import load_questions

def test_fundamental_duties_easy_mcqs_flow():
    print("================================================================================")
    print("🚀 RUNNING TNPSC NOVA AI - FUNDAMENTAL DUTIES EASY 50 MCQs VERIFICATION SUITE")
    print("================================================================================")

    # 1. File existence & JSON parsing
    q_path = "data/questions/polity/fundamental_duties_easy.json"
    print(f"\n[STEP 1] Checking Question File Existence: {q_path}")
    assert os.path.exists(q_path), f"❌ File not found: {q_path}"

    with open(q_path, "r", encoding="utf-8") as f:
        questions = json.load(f)

    assert isinstance(questions, list), "❌ Top-level JSON is not a list!"
    assert len(questions) == 50, f"❌ Expected exactly 50 questions, found {len(questions)}"
    print("   ✅ Question file exists and contains exactly 50 questions.")

    # 2. Detailed Schema & Metadata Audit
    print("\n[STEP 2] Auditing Question Schema & Field Integrity")
    stems_en = set()
    stems_ta = set()
    key_counts = {"A": 0, "B": 0, "C": 0, "D": 0}

    for idx, q in enumerate(questions, 1):
        # Check required keys
        req_keys = ["id", "subject", "topic", "difficulty", "question_type", "question", "options", "correct_answer", "explanation", "why_not_others", "tnpsc_tip"]
        for k in req_keys:
            assert k in q, f"❌ Question {idx} ({q.get('id')}) missing key: {k}"

        # Difficulty & Topic
        assert q["difficulty"] == "Easy", f"❌ Question {idx} invalid difficulty: {q['difficulty']}"
        assert q["topic"] == "Fundamental Duties", f"❌ Question {idx} invalid topic: {q['topic']}"

        # Question text
        q_en = q["question"]["en"].strip()
        q_ta = q["question"]["ta"].strip()
        assert len(q_en) > 0 and len(q_ta) > 0, f"❌ Question {idx} has empty stem"
        
        # Check duplicates
        assert q_en not in stems_en, f"❌ Duplicate EN question stem found at Q{idx}: {q_en[:30]}..."
        assert q_ta not in stems_ta, f"❌ Duplicate TA question stem found at Q{idx}: {q_ta[:30]}..."
        stems_en.add(q_en)
        stems_ta.add(q_ta)

        # Options audit
        opts = q["options"]
        assert len(opts) == 4, f"❌ Question {idx} does not have 4 options!"
        opt_ids = [opt["id"] for opt in opts]
        assert opt_ids == ["A", "B", "C", "D"], f"❌ Question {idx} invalid option IDs: {opt_ids}"

        for opt in opts:
            assert len(opt["en"].strip()) > 0, f"❌ Question {idx} option {opt['id']} EN is empty"
            assert len(opt["ta"].strip()) > 0, f"❌ Question {idx} option {opt['id']} TA is empty"

        # Correct answer audit
        ans = q["correct_answer"]
        assert ans in ["A", "B", "C", "D"], f"❌ Question {idx} invalid correct_answer: {ans}"
        key_counts[ans] += 1

        # Explanation & why_not_others audit
        exp = q["explanation"]
        assert len(exp["en"].strip()) > 0 and len(exp["ta"].strip()) > 0, f"❌ Question {idx} empty explanation"

        wno = q["why_not_others"]
        for o_id in ["A", "B", "C", "D"]:
            assert o_id in wno, f"❌ Question {idx} why_not_others missing {o_id}"
            assert len(wno[o_id]["en"].strip()) > 0 and len(wno[o_id]["ta"].strip()) > 0

        # TNPSC Tip/Trap audit
        tip = q["tnpsc_tip"]
        assert len(tip["en"].strip()) > 0 and len(tip["ta"].strip()) > 0, f"❌ Question {idx} empty tnpsc_tip"

    print("   ✅ All 50 question objects passed schema and non-empty bilingual audit.")

    # 3. Answer Key Distribution
    print(f"\n[STEP 3] Verifying Answer Key Distribution: {key_counts}")
    assert key_counts["A"] >= 8 and key_counts["B"] >= 8 and key_counts["C"] >= 8 and key_counts["D"] >= 8, "❌ Unbalanced answer distribution!"
    print("   ✅ Answer key distribution balanced.")

    # 4. Cross-part Navigation Loader Resolution Test
    print("\n[STEP 4] Testing Cross-part Question Loader Resolution")
    for part_num in [1, 2, 3]:
        t_id = f"polity_fundamental_duties_part_{part_num}"
        loaded_qs = load_questions("polity", t_id, "easy")
        assert loaded_qs is not None, f"❌ Failed to load easy questions for {t_id}"
        assert len(loaded_qs) == 50, f"❌ Loaded {len(loaded_qs)} questions for {t_id}, expected 50!"
        assert loaded_qs[0]["id"] == "FD_E_001", f"❌ Mismatched repository loaded for {t_id}!"
        print(f"   - Part {part_num} (`{t_id}`) -> Loaded 50 questions from common repository -> PASSED")

    print("\n================================================================================")
    print("🏆 ALL VERIFICATION CHECKS PASSED FOR FUNDAMENTAL DUTIES EASY 50 MCQs!")
    print("================================================================================")

if __name__ == "__main__":
    test_fundamental_duties_easy_mcqs_flow()
