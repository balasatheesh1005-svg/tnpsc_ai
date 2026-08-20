# -*- coding: utf-8 -*-
"""
Verification Suite for Fundamental Rights Reasoning MCQs Repository
"""

import sys
import json
import os

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

from core.topics_loader import get_topic_metadata_by_id
from core.navigation_v2.navigation_state import check_repository_availability
from core.question_loader import load_questions

def run_verification():
    print("================================================================================")
    print("🚀 RUNNING TNPSC NOVA AI - FUNDAMENTAL RIGHTS REASONING MCQS VERIFICATION SUITE")
    print("================================================================================")

    # 1. File Existence & JSON parsing
    target_files = [
        "data/questions/polity/fundamental_rights_reasoning.json",
        "data/questions/polity/fundamental_rights_assertion_reason.json"
    ]

    for target_file in target_files:
        print(f"\n[STEP 1] Validating File Existence & JSON Parsing: {target_file}")
        assert os.path.exists(target_file), f"❌ File not found: {target_file}"

        with open(target_file, "r", encoding="utf-8") as f:
            questions = json.load(f)

        print(f"   ✅ File exists and parses cleanly as valid JSON ({len(questions)} questions found).")
        assert len(questions) == 25, f"❌ Expected exactly 25 questions, found {len(questions)}"

    # 2. Field Completeness & Schema Audit
    print("\n[STEP 2] Auditing Reasoning Schema Fields for all 25 Questions")
    required_fields = [
        "id", "subject", "topic", "difficulty", "question_type",
        "question", "assertion", "reason", "options", "correct_answer", "explanation",
        "why_not_others", "tnpsc_tip", "revision_fact", "source_reference",
        "bloom_level", "estimated_time_sec", "pyq_similarity", "tags",
        "question_en", "question_ta", "options_en", "options_ta", "answer",
        "explanation_en", "explanation_ta"
    ]

    ans_dist = {"A": 0, "B": 0, "C": 0, "D": 0}

    for idx, q in enumerate(questions, 1):
        for field in required_fields:
            assert field in q, f"❌ Question {idx} ({q.get('id')}) missing field: {field}"

        # Check IDs
        expected_id = f"FR_R_{idx:03d}"
        assert q["id"] == expected_id, f"❌ Question {idx} ID mismatch: expected {expected_id}, got {q['id']}"

        # Check options structure
        assert len(q["options"]) == 4, f"❌ Question {idx} does not have exactly 4 options"
        assert len(q["options_en"]) == 4, f"❌ Question {idx} options_en count is not 4"
        assert len(q["options_ta"]) == 4, f"❌ Question {idx} options_ta count is not 4"

        # Check answer integrity
        ca = q["correct_answer"]
        assert ca in ["A", "B", "C", "D"], f"❌ Question {idx} invalid correct_answer: {ca}"
        assert q["answer"] == ca.lower(), f"❌ Question {idx} answer lowercase mismatch: {q['answer']} vs {ca}"

        ans_dist[ca] += 1

        # Check WNO indicator for correct option
        wno_ca = q["why_not_others"][ca]
        assert "Correct" in wno_ca["en"] or wno_ca["en"].startswith("Correct"), f"❌ Question {idx} WNO EN for correct_answer {ca} does not indicate Correct"
        assert "சரி" in wno_ca["ta"] or wno_ca["ta"].startswith("சரி"), f"❌ Question {idx} WNO TA for correct_answer {ca} does not indicate Correct"

        # Check non-empty bilingual strings
        assert len(q["question"]["en"].strip()) > 0, f"❌ Question {idx} empty English question"
        assert len(q["question"]["ta"].strip()) > 0, f"❌ Question {idx} empty Tamil question"
        assert len(q["explanation"]["en"].strip()) > 0, f"❌ Question {idx} empty English explanation"
        assert len(q["explanation"]["ta"].strip()) > 0, f"❌ Question {idx} empty Tamil explanation"

    print("   ✅ All 25 questions contain valid Reasoning structures and required fields.")

    # 3. Answer Distribution Breakdown
    print("\n[STEP 3] Verifying Answer Distribution across A, B, C, D")
    print(f"   - A: {ans_dist['A']} [Target: 6]")
    print(f"   - B: {ans_dist['B']} [Target: 6]")
    print(f"   - C: {ans_dist['C']} [Target: 6]")
    print(f"   - D: {ans_dist['D']} [Target: 7]")

    assert ans_dist["A"] == 6, f"❌ Expected 6 A answers, got {ans_dist['A']}"
    assert ans_dist["B"] == 6, f"❌ Expected 6 B answers, got {ans_dist['B']}"
    assert ans_dist["C"] == 6, f"❌ Expected 6 C answers, got {ans_dist['C']}"
    assert ans_dist["D"] == 7, f"❌ Expected 7 D answers, got {ans_dist['D']}"
    print("   ✅ Answer distribution matches target breakdown exactly!")

    # 4. Difficulty Distribution Breakdown
    print("\n[STEP 4] Verifying Difficulty Distribution (20% Easy, 50% Medium, 30% Hard)")
    diff_counts = {"Easy": 0, "Medium": 0, "Hard": 0}
    for q in questions:
        diff_counts[q["difficulty"]] += 1

    print(f"   - Easy: {diff_counts['Easy']} ({diff_counts['Easy']/25*100:.0f}%) [Target: 5 / 20%]")
    print(f"   - Medium: {diff_counts['Medium']} ({diff_counts['Medium']/25*100:.0f}%) [Target: 13 / 52%]")
    print(f"   - Hard: {diff_counts['Hard']} ({diff_counts['Hard']/25*100:.0f}%) [Target: 7 / 28%]")

    assert diff_counts["Easy"] == 5, f"❌ Expected 5 Easy questions, got {diff_counts['Easy']}"
    assert diff_counts["Medium"] == 13, f"❌ Expected 13 Medium questions, got {diff_counts['Medium']}"
    assert diff_counts["Hard"] == 7, f"❌ Expected 7 Hard questions, got {diff_counts['Hard']}"
    print("   ✅ Difficulty distribution matches target breakdown exactly!")

    # 5. Practice Engine Integration & Availability Test for All 3 Notes Parts
    print("\n[STEP 5] Testing Topic Discovery & Practice Loading across Part 1, Part 2, Part 3")
    fr_topics = [
        "polity_fundamental_rights_part_1",
        "polity_fundamental_rights_part_2",
        "polity_fundamental_rights_part_3"
    ]

    for topic_id in fr_topics:
        meta = get_topic_metadata_by_id("polity", topic_id)
        assert meta is not None, f"❌ Topic {topic_id} not found by topics_loader!"
        assert meta["repository_id"] == "polity_fundamental_rights", f"❌ Topic {topic_id} repo mismatch: {meta['repository_id']}"

        # Check navigation availability
        avail = check_repository_availability("polity", topic_id)
        print(f"   - {meta['display_title']} -> assertion_reason availability: {avail.get('assertion_reason')}")
        assert avail.get("assertion_reason") == True, f"❌ assertion_reason availability is False for {topic_id}"

        # Test loading questions for both 'reasoning' and 'assertion_reason'
        for q_type in ["reasoning", "assertion_reason"]:
            loaded_qs = load_questions(meta["repository_id"], q_type)
            assert len(loaded_qs) == 25, f"❌ Failed to load 25 {q_type} questions for {topic_id}, loaded {len(loaded_qs)}"
            print(f"   [OK] {meta['display_title']} -> Loaded {len(loaded_qs)} {q_type} questions cleanly.")

    print("   ✅ Practice Engine Integration PASSED for Part 1, Part 2, and Part 3!")

    print("\n================================================================================")
    print("🎉 ALL VERIFICATION STEPS PASSED WITH 100% SUCCESS FOR REASONING MCQS!")
    print("================================================================================")

if __name__ == "__main__":
    run_verification()
