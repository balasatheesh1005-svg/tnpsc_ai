# -*- coding: utf-8 -*-
"""
Verification Suite for Fundamental Rights Match the Following MCQs Repository
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
    print("🚀 RUNNING TNPSC NOVA AI - FUNDAMENTAL RIGHTS MATCH MCQS VERIFICATION SUITE")
    print("================================================================================")

    # 1. File Existence & JSON parsing
    target_file = "data/questions/polity/fundamental_rights_match_the_following.json"
    print(f"\n[STEP 1] Validating File Existence & JSON Parsing: {target_file}")
    assert os.path.exists(target_file), f"❌ File not found: {target_file}"
    
    with open(target_file, "r", encoding="utf-8") as f:
        questions = json.load(f)

    print(f"   ✅ File exists and parses cleanly as valid JSON ({len(questions)} questions found).")
    assert len(questions) == 25, f"❌ Expected exactly 25 questions, found {len(questions)}"

    # 2. Field Completeness & Schema Audit
    print("\n[STEP 2] Auditing Match the Following Schema Fields for all 25 Questions")
    required_fields = [
        "id", "subject", "topic", "difficulty", "question_type",
        "question", "list_1", "list_2", "options", "correct_answer", "explanation",
        "why_not_others", "tnpsc_tip", "revision_fact", "source_reference",
        "bloom_level", "estimated_time_sec", "pyq_similarity", "tags",
        "question_en", "question_ta", "options_en", "options_ta", "answer",
        "explanation_en", "explanation_ta"
    ]

    for idx, q in enumerate(questions, 1):
        for field in required_fields:
            assert field in q, f"❌ Question {idx} ({q.get('id')}) missing field: {field}"
        
        # Check IDs
        expected_id = f"FR_MF_{idx:03d}"
        assert q["id"] == expected_id, f"❌ Question {idx} ID mismatch: expected {expected_id}, got {q['id']}"
        
        # Check list structure
        assert len(q["list_1"]) == 4, f"❌ Question {idx} list_1 count is not 4"
        assert len(q["list_2"]) == 4, f"❌ Question {idx} list_2 count is not 4"
        assert len(q["options"]) == 4, f"❌ Question {idx} does not have exactly 4 options"
        assert len(q["options_en"]) == 4, f"❌ Question {idx} options_en count is not 4"
        assert len(q["options_ta"]) == 4, f"❌ Question {idx} options_ta count is not 4"
        
        # Check answer integrity
        assert q["correct_answer"] in ["A", "B", "C", "D"], f"❌ Question {idx} invalid correct_answer: {q['correct_answer']}"
        assert q["answer"] == q["correct_answer"].lower(), f"❌ Question {idx} answer lowercase mismatch: {q['answer']} vs {q['correct_answer']}"
        
        # Check non-empty bilingual strings
        assert len(q["question"]["en"].strip()) > 0, f"❌ Question {idx} empty English question"
        assert len(q["question"]["ta"].strip()) > 0, f"❌ Question {idx} empty Tamil question"
        assert len(q["explanation"]["en"].strip()) > 0, f"❌ Question {idx} empty English explanation"
        assert len(q["explanation"]["ta"].strip()) > 0, f"❌ Question {idx} empty Tamil explanation"

    print("   ✅ All 25 questions contain valid List I / List II structures and all required fields.")

    # 3. Difficulty Distribution Breakdown
    print("\n[STEP 3] Verifying Difficulty Distribution (20% Easy, 50% Medium, 30% Hard)")
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

    # 4. Practice Engine Integration & Availability Test for All 3 Notes Parts
    print("\n[STEP 4] Testing Topic Discovery & Practice Loading across Part 1, Part 2, Part 3")
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
        print(f"   - {meta['display_title']} -> match_the_following availability: {avail.get('match_the_following')}")
        assert avail.get("match_the_following") == True, f"❌ match_the_following availability is False for {topic_id}"

        # Test loading questions
        loaded_qs = load_questions(meta["repository_id"], "match_the_following")
        assert len(loaded_qs) == 25, f"❌ Failed to load 25 match questions for {topic_id}, loaded {len(loaded_qs)}"
        print(f"   [OK] {meta['display_title']} -> Loaded {len(loaded_qs)} Match questions cleanly.")

    print("   ✅ Practice Engine Integration PASSED for Part 1, Part 2, and Part 3!")

    print("\n================================================================================")
    print("🎉 ALL VERIFICATION STEPS PASSED WITH 100% SUCCESS FOR MATCH THE FOLLOWING MCQS!")
    print("================================================================================")

if __name__ == "__main__":
    run_verification()
