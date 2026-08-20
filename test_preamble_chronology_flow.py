# -*- coding: utf-8 -*-
"""
Comprehensive Validation & Practice Engine Flow Verification Suite for Preamble Chronology (25 MCQs)
"""

import sys
import json
import os
from collections import Counter
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

from core.topics_loader import get_topic_metadata_by_id
from core.navigation_v2.navigation_state import check_repository_availability
from core.question_loader import load_questions
from ui.question_engine.parser import UniversalQuestionAdapter, NormalizedQuestion

def run_preamble_chronology_verification():
    print("================================================================================")
    print("🚀 RUNNING TNPSC NOVA AI - PREAMBLE CHRONOLOGY (25 MCQs) VERIFICATION SUITE")
    print("================================================================================")

    # -------------------------------------------------------------------------
    # 1. File Existence & Total Count Validation
    # -------------------------------------------------------------------------
    file_path = "data/questions/polity/preamble_chronology.json"
    print(f"\n[STEP 1] Validating File Existence & JSON Parsing: {file_path}")
    assert os.path.exists(file_path), f"❌ File not found: {file_path}"
    
    with open(file_path, "r", encoding="utf-8") as f:
        questions = json.load(f)

    print(f"   - Total Questions Loaded: {len(questions)}")
    assert len(questions) == 25, f"❌ Expected exactly 25 questions, found {len(questions)}"
    print("   ✅ Total Count = 25 PASSED")

    # -------------------------------------------------------------------------
    # 2. Schema Audit & Metadata Validation
    # -------------------------------------------------------------------------
    print("\n[STEP 2] Dual-Schema & Complete Metadata Audit")
    required_fields = [
        "id", "subject", "topic", "difficulty", "question_type",
        "question", "events", "options", "correct_answer",
        "explanation", "why_not_others", "tnpsc_tip", "revision_fact",
        "source_reference", "bloom_level", "estimated_time_sec", "pyq_similarity",
        "tags", "question_en", "question_ta", "options_en", "options_ta", "answer",
        "explanation_en", "explanation_ta"
    ]

    ids = []
    answers = []
    for idx, q in enumerate(questions, 1):
        q_id = q.get("id")
        ids.append(q_id)
        assert q_id == f"PRE_CHRONO_{idx:03d}", f"❌ Invalid ID pattern: {q_id} at index {idx}"

        for field in required_fields:
            assert field in q, f"❌ Question {q_id} missing required field: '{field}'"

        # Check nested structures
        assert isinstance(q["question"], dict) and "en" in q["question"] and "ta" in q["question"]
        assert isinstance(q["explanation"], dict) and "en" in q["explanation"] and "ta" in q["explanation"]
        assert isinstance(q["tnpsc_tip"], dict) and "en" in q["tnpsc_tip"] and "ta" in q["tnpsc_tip"]
        assert isinstance(q["revision_fact"], dict) and "en" in q["revision_fact"] and "ta" in q["revision_fact"]
        
        # Check events
        assert isinstance(q["events"], list) and len(q["events"]) >= 3, f"❌ Events array malformed in {q_id}"
        for ev in q["events"]:
            assert "id" in ev and "en" in ev and "ta" in ev, f"❌ Event dict malformed in {q_id}"

        # Check options
        assert isinstance(q["options"], list) and len(q["options"]) == 4, f"❌ Options array != 4 in {q_id}"
        for opt in q["options"]:
            assert "id" in opt and "en" in opt and "ta" in opt, f"❌ Option dict malformed in {q_id}"
            assert opt["id"] in ["A", "B", "C", "D"], f"❌ Option ID not A-D in {q_id}"

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

        # Check flat fields
        assert isinstance(q["options_en"], list) and len(q["options_en"]) == 4
        assert isinstance(q["options_ta"], list) and len(q["options_ta"]) == 4
        assert len(q["question_en"].strip()) > 0
        assert len(q["question_ta"].strip()) > 0
        assert len(q["explanation_en"].strip()) > 0
        assert len(q["explanation_ta"].strip()) > 0

    assert len(set(ids)) == 25, "❌ Duplicate IDs found!"
    print(f"   - Unique Sequential IDs: {ids[0]} -> {ids[-1]}")
    print("   ✅ Full Schema & Metadata Audit PASSED")

    # -------------------------------------------------------------------------
    # 3. Answer Key Distribution
    # -------------------------------------------------------------------------
    print("\n[STEP 3] Answer Key Distribution Analysis")
    counts = Counter(answers)
    for k in sorted(counts.keys()):
        print(f"   - Option {k}: {counts[k]} ({counts[k]/25*100:.1f}%)")
    assert all(counts[k] >= 5 for k in ["A", "B", "C", "D"]), "❌ Imbalanced answer distribution!"
    print("   ✅ Answer Key Distribution Balanced PASSED")

    # -------------------------------------------------------------------------
    # 4. Navigation & Availability Verification (Part 1 & Part 2 Common Loading)
    # -------------------------------------------------------------------------
    print("\n[STEP 4] Navigation & Topic Hub Availability Verification")
    
    # Part 1 check
    avail_p1 = check_repository_availability("polity", "polity_preamble_part_1")
    print(f"   - Preamble Part 1 Availability: {avail_p1}")
    assert avail_p1.get("chronology") == True, "❌ Chronology repo should be available for Preamble Part 1!"
    qs_p1 = load_questions("polity", "polity_preamble_part_1", "chronology")
    assert len(qs_p1) == 25, f"❌ Expected 25 questions for Part 1, got {len(qs_p1)}"
    print(f"   ✅ Preamble Part 1 loads {len(qs_p1)} Chronology questions successfully")

    # Part 2 check
    avail_p2 = check_repository_availability("polity", "polity_preamble_part_2")
    print(f"   - Preamble Part 2 Availability: {avail_p2}")
    assert avail_p2.get("chronology") == True, "❌ Chronology repo should be available for Preamble Part 2!"
    qs_p2 = load_questions("polity", "polity_preamble_part_2", "chronology")
    assert len(qs_p2) == 25, f"❌ Expected 25 questions for Part 2, got {len(qs_p2)}"
    print(f"   ✅ Preamble Part 2 loads {len(qs_p2)} Chronology questions successfully")

    # Common repository identity check
    assert qs_p1[0]["id"] == qs_p2[0]["id"] == "PRE_CHRONO_001", "❌ Part 1 and Part 2 must load identical repository!"
    assert qs_p1[-1]["id"] == qs_p2[-1]["id"] == "PRE_CHRONO_025", "❌ Part 1 and Part 2 end ID mismatch!"
    print("   ✅ Common Topic-Level Repository Shared Load PASSED")

    # Direct repository_id call check
    qs_direct = load_questions("polity_preamble", "chronology")
    assert len(qs_direct) == 25, "❌ Direct load_questions('polity_preamble', 'chronology') failed!"
    print(f"   ✅ Direct load_questions('polity_preamble', 'chronology') PASSED ({len(qs_direct)} questions)")

    # -------------------------------------------------------------------------
    # 5. Question Engine Adapter & Practice Simulation
    # -------------------------------------------------------------------------
    print("\n[STEP 5] Universal Question Engine Adapter & Practice Simulation")
    for idx, q_raw in enumerate(questions):
        norm_q = UniversalQuestionAdapter.normalize(q_raw)
        assert isinstance(norm_q, NormalizedQuestion)
        assert norm_q.id == f"PRE_CHRONO_{idx+1:03d}"
        assert norm_q.subject == "Polity"
        assert "Preamble" in norm_q.topic
        assert norm_q.question_type == "Chronology"
        assert len(norm_q.options) == 4
        assert norm_q.correct_answer in ["A", "B", "C", "D"]
        assert len(norm_q.explanation.en) > 0
        assert len(norm_q.explanation.ta) > 0

    print("   ✅ Universal Question Adapter normalized all 25 questions successfully")

    # -------------------------------------------------------------------------
    # 6. Regression Testing Across Existing Repositories
    # -------------------------------------------------------------------------
    print("\n[STEP 6] Regression Verification of Existing Repositories")
    regression_checks = [
        ("polity", "polity_historical_background_part1", "chronology", 25),
        ("polity", "polity_making_of_indian_constitution_part_1", "chronology", 25),
        ("polity", "polity_salient_features_of_the_indian_constitution_part_1", "chronology", 25),
        ("polity", "polity_preamble_part_1", "easy", 50),
        ("polity", "polity_preamble_part_1", "medium", 50),
        ("polity", "polity_preamble_part_1", "hard", 50),
        ("polity", "polity_preamble_part_1", "statement_based", 50),
        ("polity", "polity_preamble_part_1", "match_the_following", 25)
    ]

    for subj, top_id, r_type, expected_min in regression_checks:
        avail = check_repository_availability(subj, top_id)
        assert avail.get(r_type) == True, f"❌ Availability broken for {top_id} - {r_type}"
        loaded = load_questions(subj, top_id, r_type)
        assert len(loaded) >= expected_min, f"❌ Loaded count {len(loaded)} < expected {expected_min} for {top_id} - {r_type}"
        print(f"   [OK] {top_id} -> {r_type.upper()}: {len(loaded)} items loaded cleanly.")

    print("\n================================================================================")
    print("🎉 ALL 6 VERIFICATION STEPS PASSED WITH 100% SUCCESS!")
    print("================================================================================")

if __name__ == "__main__":
    run_preamble_chronology_verification()
