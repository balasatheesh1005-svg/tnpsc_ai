# -*- coding: utf-8 -*-
"""
Comprehensive Validation & Practice Engine Flow Verification Suite for Fundamental Rights Grand Test (100 MCQs)
"""

import sys
import json
import os
import glob
from collections import Counter
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

from core.topics_loader import get_topic_metadata_by_id
from core.navigation_v2.navigation_state import check_repository_availability
from core.question_loader import load_questions
from ui.question_engine.parser import UniversalQuestionAdapter, NormalizedQuestion

def run_fundamental_rights_grand_test_verification():
    print("================================================================================")
    print("🚀 RUNNING TNPSC NOVA AI - FUNDAMENTAL RIGHTS GRAND TEST (100 MCQs) VERIFICATION")
    print("================================================================================")

    # -------------------------------------------------------------------------
    # 1. File Existence & Total Count Validation
    # -------------------------------------------------------------------------
    file_path = "data/questions/polity/fundamental_rights_grand_test.json"
    print(f"\n[STEP 1] Validating File Existence & JSON Parsing: {file_path}")
    assert os.path.exists(file_path), f"❌ File not found: {file_path}"
    
    with open(file_path, "r", encoding="utf-8") as f:
        questions = json.load(f)

    print(f"   - Total Questions Loaded: {len(questions)}")
    assert len(questions) == 100, f"❌ Expected exactly 100 questions, found {len(questions)}"
    print("   ✅ Total Count = 100 PASSED")

    # -------------------------------------------------------------------------
    # 2. Schema Audit & Metadata Validation
    # -------------------------------------------------------------------------
    print("\n[STEP 2] Dual-Schema & Complete Metadata Audit")
    required_fields = [
        "id", "subject", "topic", "difficulty", "question_type",
        "question", "options", "correct_answer",
        "explanation", "why_not_others", "tnpsc_tip", "revision_fact",
        "source_reference", "bloom_level", "estimated_time_sec", "pyq_similarity",
        "tags", "question_en", "question_ta", "options_en", "options_ta", "answer",
        "explanation_en", "explanation_ta"
    ]

    ids = []
    answers = []
    types_counter = Counter()
    diff_counter = Counter()

    for idx, q in enumerate(questions, 1):
        q_id = q.get("id")
        ids.append(q_id)
        assert q_id == f"FR_GT_{idx:03d}", f"❌ Invalid ID pattern: {q_id} at index {idx}"

        for field in required_fields:
            assert field in q, f"❌ Question {q_id} missing required field: '{field}'"

        types_counter[q["question_type"]] += 1
        diff_counter[q["difficulty"]] += 1

        # Check nested structures
        assert isinstance(q["question"], dict) and "en" in q["question"] and "ta" in q["question"]
        assert isinstance(q["explanation"], dict) and "en" in q["explanation"] and "ta" in q["explanation"]
        assert isinstance(q["tnpsc_tip"], dict) and "en" in q["tnpsc_tip"] and "ta" in q["tnpsc_tip"]
        assert isinstance(q["revision_fact"], dict) and "en" in q["revision_fact"] and "ta" in q["revision_fact"]

        # Check non-empty bilingual content
        assert len(q["question"]["en"].strip()) > 5, f"❌ Question {q_id} question.en empty!"
        assert len(q["question"]["ta"].strip()) > 5, f"❌ Question {q_id} question.ta empty!"
        assert len(q["explanation"]["en"].strip()) > 5, f"❌ Question {q_id} explanation.en empty!"
        assert len(q["explanation"]["ta"].strip()) > 5, f"❌ Question {q_id} explanation.ta empty!"
        assert len(q["tnpsc_tip"]["en"].strip()) > 5, f"❌ Question {q_id} tnpsc_tip.en empty!"
        assert len(q["tnpsc_tip"]["ta"].strip()) > 5, f"❌ Question {q_id} tnpsc_tip.ta empty!"
        assert len(q["revision_fact"]["en"].strip()) > 5, f"❌ Question {q_id} revision_fact.en empty!"
        assert len(q["revision_fact"]["ta"].strip()) > 5, f"❌ Question {q_id} revision_fact.ta empty!"

        # Check options
        assert isinstance(q["options"], list) and len(q["options"]) == 4, f"❌ Options array != 4 in {q_id}"
        for opt in q["options"]:
            assert "id" in opt and "en" in opt and "ta" in opt, f"❌ Option dict malformed in {q_id}"
            assert opt["id"] in ["A", "B", "C", "D"], f"❌ Option ID not A-D in {q_id}"
            assert len(opt["en"].strip()) > 0, f"❌ Option {opt['id']} EN empty in {q_id}"
            assert len(opt["ta"].strip()) > 0, f"❌ Option {opt['id']} TA empty in {q_id}"

        # Check answers
        ans = q["correct_answer"]
        answers.append(ans)
        assert ans in ["A", "B", "C", "D"], f"❌ Invalid correct_answer: {ans} in {q_id}"
        assert q["answer"] == ans.lower(), f"❌ Flat answer mismatch: {q['answer']} vs {ans} in {q_id}"

        # Check why_not_others
        assert isinstance(q["why_not_others"], dict)
        for opt_key in ["A", "B", "C", "D"]:
            assert opt_key in q["why_not_others"], f"❌ Missing why_not_others for option {opt_key} in {q_id}"
            assert "en" in q["why_not_others"][opt_key] and "ta" in q["why_not_others"][opt_key]
            assert len(q["why_not_others"][opt_key]["en"].strip()) > 0, f"❌ why_not_others {opt_key} EN empty in {q_id}"
            assert len(q["why_not_others"][opt_key]["ta"].strip()) > 0, f"❌ why_not_others {opt_key} TA empty in {q_id}"

        # Check flat fields
        assert isinstance(q["options_en"], list) and len(q["options_en"]) == 4
        assert isinstance(q["options_ta"], list) and len(q["options_ta"]) == 4
        assert len(q["question_en"].strip()) > 0
        assert len(q["question_ta"].strip()) > 0
        assert len(q["explanation_en"].strip()) > 0
        assert len(q["explanation_ta"].strip()) > 0

        # Adapter Normalization test
        norm = UniversalQuestionAdapter.normalize(q)
        assert isinstance(norm, NormalizedQuestion), f"❌ Failed to normalize {q_id}"
        assert norm.correct_answer == ans, f"❌ Normalized answer mismatch in {q_id}"

    assert len(set(ids)) == 100, "❌ Duplicate IDs found!"
    print(f"   - Unique Sequential IDs: {ids[0]} -> {ids[-1]}")
    print("   ✅ Full Dual-Schema, Metadata & Adapter Normalization Audit PASSED")

    # -------------------------------------------------------------------------
    # 3. Question Mix & Difficulty Analysis
    # -------------------------------------------------------------------------
    print("\n[STEP 3] Question Mix & Difficulty Breakdown")
    print("   Taxonomy Breakdown:")
    for t_name, t_cnt in types_counter.most_common():
        print(f"     * {t_name}: {t_cnt} questions")
    
    print("\n   Difficulty Breakdown:")
    for d_name in ["Easy", "Medium", "Hard"]:
        d_cnt = diff_counter[d_name]
        print(f"     * {d_name}: {d_cnt} questions ({d_cnt/100*100:.1f}%)")

    assert diff_counter["Easy"] == 20, f"❌ Expected 20 Easy, got {diff_counter['Easy']}"
    assert diff_counter["Medium"] == 50, f"❌ Expected 50 Medium, got {diff_counter['Medium']}"
    assert diff_counter["Hard"] == 30, f"❌ Expected 30 Hard, got {diff_counter['Hard']}"
    print("   ✅ Difficulty Distribution (20% Easy, 50% Medium, 30% Hard) PASSED")

    # -------------------------------------------------------------------------
    # 4. Answer Key Distribution
    # -------------------------------------------------------------------------
    print("\n[STEP 4] Answer Key Distribution Analysis")
    counts = Counter(answers)
    for k in sorted(counts.keys()):
        print(f"   - Option {k}: {counts[k]} ({counts[k]/100*100:.1f}%)")
    assert counts["A"] == 25 and counts["B"] == 25 and counts["C"] == 25 and counts["D"] == 25, "❌ Answer key is not perfectly 25-25-25-25 balanced!"
    print("   ✅ Answer Key Distribution (25 A, 25 B, 25 C, 25 D) PERFECTLY BALANCED")

    # -------------------------------------------------------------------------
    # 5. Navigation & Availability Verification (Part 1, Part 2 & Part 3 Common Loading)
    # -------------------------------------------------------------------------
    print("\n[STEP 5] Navigation & Topic Hub Availability Verification")
    
    for part_num in [1, 2, 3]:
        topic_id = f"polity_fundamental_rights_part_{part_num}"
        meta = get_topic_metadata_by_id("polity", topic_id)
        assert meta["repository_id"] == "polity_fundamental_rights", f"❌ Topic {topic_id} repository_id mismatch!"

        avail = check_repository_availability("polity", topic_id)
        print(f"   - Part {part_num} Availability: {avail}")
        assert avail.get("grand_test") == True, f"❌ Grand Test repo should be available for Part {part_num}!"

        qs_part = load_questions("polity", topic_id, "grand_test")
        assert len(qs_part) == 100, f"❌ Expected 100 questions for Part {part_num}, got {len(qs_part)}"
        print(f"   ✅ Part {part_num} ({topic_id}) loads {len(qs_part)} Grand Test questions successfully")

    # Direct load check
    qs_direct = load_questions("polity_fundamental_rights", "grand_test")
    assert len(qs_direct) == 100, f"❌ Direct load_questions('polity_fundamental_rights', 'grand_test') failed! Got {len(qs_direct)}"
    print(f"   ✅ Direct load_questions('polity_fundamental_rights', 'grand_test') PASSED ({len(qs_direct)} questions)")

    # -------------------------------------------------------------------------
    # 6. Repetition Control & Uniqueness Audit
    # -------------------------------------------------------------------------
    print("\n[STEP 6] Repetition Control & Duplicate Audit against existing FR Repositories")
    gt_stems = set(q["question_en"].strip().lower() for q in questions)
    assert len(gt_stems) == 100, "❌ Duplicate question stems found within Grand Test!"

    other_fr_files = [f for f in glob.glob("data/questions/polity/fundamental_rights_*.json") if "grand_test" not in f]
    print(f"   - Checking against {len(other_fr_files)} existing Fundamental Rights repositories...")

    existing_stems = set()
    for o_file in other_fr_files:
        with open(o_file, "r", encoding="utf-8") as f:
            o_qs = json.load(f)
            for o_q in o_qs:
                stem = o_q.get("question_en") or (o_q.get("question", {}).get("en") if isinstance(o_q.get("question"), dict) else "")
                if stem:
                    existing_stems.add(stem.strip().lower())

    overlap = gt_stems.intersection(existing_stems)
    print(f"   - Overlapping question stems count: {len(overlap)}")
    assert len(overlap) == 0, f"❌ Direct duplicate questions found with existing repositories! Overlapping: {overlap}"
    print("   ✅ Zero Duplicate Stems Audit PASSED")

    print("\n================================================================================")
    print("🏆 ALL VERIFICATION CHECKS PASSED FOR FUNDAMENTAL RIGHTS GRAND TEST (100 MCQs)!")
    print("================================================================================")

if __name__ == "__main__":
    run_fundamental_rights_grand_test_verification()
