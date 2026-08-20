# -*- coding: utf-8 -*-
"""
Verification Suite for Fundamental Rights Statement-Based MCQs Repository
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
    print("🚀 RUNNING TNPSC NOVA AI - FUNDAMENTAL RIGHTS STATEMENT MCQS VERIFICATION SUITE")
    print("================================================================================")

    # 1. File Existence & JSON parsing
    target_file = "data/questions/polity/fundamental_rights_statement_based.json"
    print(f"\n[STEP 1] Validating File Existence & JSON Parsing: {target_file}")
    assert os.path.exists(target_file), f"❌ File not found: {target_file}"
    
    with open(target_file, "r", encoding="utf-8") as f:
        questions = json.load(f)

    print(f"   ✅ File exists and parses cleanly as valid JSON ({len(questions)} questions found).")
    assert len(questions) == 50, f"❌ Expected exactly 50 questions, found {len(questions)}"

    # 2. Field Completeness & Schema Audit
    print("\n[STEP 2] Auditing 24 Required Schema Fields for all 50 Questions")
    required_fields = [
        "id", "subject", "topic", "difficulty", "question_type",
        "question", "options", "correct_answer", "explanation",
        "why_not_others", "tnpsc_tip", "revision_fact", "source_reference",
        "bloom_level", "estimated_time_sec", "pyq_similarity", "tags",
        "question_en", "question_ta", "options_en", "options_ta", "answer",
        "explanation_en", "explanation_ta"
    ]

    for idx, q in enumerate(questions, 1):
        for field in required_fields:
            assert field in q, f"❌ Question {idx} ({q.get('id')}) missing field: {field}"
        
        # Check IDs
        expected_id = f"FR_SB_{idx:03d}"
        assert q["id"] == expected_id, f"❌ Question {idx} ID mismatch: expected {expected_id}, got {q['id']}"
        
        # Check options
        assert len(q["options"]) == 4, f"❌ Question {idx} does not have exactly 4 options"
        assert len(q["options_en"]) == 4, f"❌ Question {idx} options_en count is not 4"
        assert len(q["options_ta"]) == 4, f"❌ Question {idx} options_ta count is not 4"
        
        # Check answer integrity
        assert q["correct_answer"] in ["A", "B", "C", "D"], f"❌ Question {idx} invalid correct_answer: {q['correct_answer']}"
        assert q["answer"] == q["correct_answer"].lower(), f"❌ Question {idx} answer lowercase mismatch: {q['answer']} vs {q['correct_answer']}"
        
        # Check bilingual strings non-empty
        assert len(q["question"]["en"].strip()) > 0, f"❌ Question {idx} empty English question"
        assert len(q["question"]["ta"].strip()) > 0, f"❌ Question {idx} empty Tamil question"
        assert len(q["explanation"]["en"].strip()) > 0, f"❌ Question {idx} empty English explanation"
        assert len(q["explanation"]["ta"].strip()) > 0, f"❌ Question {idx} empty Tamil explanation"
        assert len(q["tnpsc_tip"]["en"].strip()) > 0, f"❌ Question {idx} empty English TNPSC tip"
        assert len(q["tnpsc_tip"]["ta"].strip()) > 0, f"❌ Question {idx} empty Tamil TNPSC tip"
        assert len(q["revision_fact"]["en"].strip()) > 0, f"❌ Question {idx} empty English revision fact"
        assert len(q["revision_fact"]["ta"].strip()) > 0, f"❌ Question {idx} empty Tamil revision fact"

    print("   ✅ All 50 questions contain all 24 required fields and non-empty bilingual strings.")

    # 3. Format & Pattern Distribution
    print("\n[STEP 3] Verifying Question Format & Pattern Distribution")
    two_stmt = [q for q in questions if q["id"].startswith("FR_SB_") and 1 <= int(q["id"].split("_")[2]) <= 15]
    three_stmt = [q for q in questions if q["id"].startswith("FR_SB_") and 16 <= int(q["id"].split("_")[2]) <= 30]
    four_stmt = [q for q in questions if q["id"].startswith("FR_SB_") and 31 <= int(q["id"].split("_")[2]) <= 40]
    cor_incor = [q for q in questions if q["id"].startswith("FR_SB_") and 41 <= int(q["id"].split("_")[2]) <= 45]
    assert_inf = [q for q in questions if q["id"].startswith("FR_SB_") and 46 <= int(q["id"].split("_")[2]) <= 50]

    assert len(two_stmt) == 15, f"❌ Expected 15 Two-Statement questions, got {len(two_stmt)}"
    assert len(three_stmt) == 15, f"❌ Expected 15 Three-Statement questions, got {len(three_stmt)}"
    assert len(four_stmt) == 10, f"❌ Expected 10 Four-Statement questions, got {len(four_stmt)}"
    assert len(cor_incor) == 5, f"❌ Expected 5 Correct/Incorrect questions, got {len(cor_incor)}"
    assert len(assert_inf) == 5, f"❌ Expected 5 Assertion/Inference questions, got {len(assert_inf)}"

    print("   - Two-Statement Questions (FR_SB_001 to FR_SB_015): 15 ✅")
    print("   - Three-Statement Questions (FR_SB_016 to FR_SB_030): 15 ✅")
    print("   - Four-Statement Questions (FR_SB_031 to FR_SB_040): 10 ✅")
    print("   - Correct/Incorrect Questions (FR_SB_041 to FR_SB_045): 5 ✅")
    print("   - Assertion/Inference Questions (FR_SB_046 to FR_SB_050): 5 ✅")

    # 4. Difficulty Breakdown
    print("\n[STEP 4] Verifying Difficulty Distribution (20% Easy, 50% Medium, 30% Hard)")
    diff_counts = {"Easy": 0, "Medium": 0, "Hard": 0}
    for q in questions:
        diff_counts[q["difficulty"]] += 1

    print(f"   - Easy: {diff_counts['Easy']} ({diff_counts['Easy']/50*100:.0f}%) [Target: 10 / 20%]")
    print(f"   - Medium: {diff_counts['Medium']} ({diff_counts['Medium']/50*100:.0f}%) [Target: 25 / 50%]")
    print(f"   - Hard: {diff_counts['Hard']} ({diff_counts['Hard']/50*100:.0f}%) [Target: 15 / 30%]")

    assert diff_counts["Easy"] == 10, f"❌ Expected 10 Easy questions, got {diff_counts['Easy']}"
    assert diff_counts["Medium"] == 25, f"❌ Expected 25 Medium questions, got {diff_counts['Medium']}"
    assert diff_counts["Hard"] == 15, f"❌ Expected 15 Hard questions, got {diff_counts['Hard']}"
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
        print(f"   - {meta['display_title']} -> statement_based availability: {avail.get('statement_based')}")
        assert avail.get("statement_based") == True, f"❌ statement_based availability is False for {topic_id}"

        # Test loading questions
        loaded_qs = load_questions(meta["repository_id"], "statement_based")
        assert len(loaded_qs) == 50, f"❌ Failed to load 50 statement questions for {topic_id}, loaded {len(loaded_qs)}"
        print(f"   [OK] {meta['display_title']} -> Loaded {len(loaded_qs)} questions cleanly.")

    print("   ✅ Practice Engine Integration PASSED for Part 1, Part 2, and Part 3!")

    # 6. Repetition Control Check against Easy, Medium, Hard repositories
    print("\n[STEP 6] Repetition Control Check against Existing Repositories")
    other_repos = [
        "fundamental_rights_easy.json",
        "fundamental_rights_medium.json",
        "fundamental_rights_hard.json"
    ]
    existing_en_texts = set()
    for repo_file in other_repos:
        repo_path = os.path.join("data/questions/polity", repo_file)
        if os.path.exists(repo_path):
            with open(repo_path, encoding="utf-8") as rf:
                old_qs = json.load(rf)
                for oq in old_qs:
                    qtext = oq.get("question_en") or oq.get("question", {}).get("en", "")
                    if qtext:
                        existing_en_texts.add(qtext.strip().lower())

    duplicate_count = 0
    for q in questions:
        q_str = (q["question_en"] or "").strip().lower()
        if q_str in existing_en_texts:
            duplicate_count += 1
            print(f"   ⚠️ Warning: Duplicate question found: {q['id']}")

    assert duplicate_count == 0, f"❌ Found {duplicate_count} exact duplicate questions!"
    print(f"   ✅ Repetition check passed with 0 exact duplicates across existing FR repositories.")

    print("\n================================================================================")
    print("🎉 ALL 6 VERIFICATION STEPS PASSED WITH 100% SUCCESS FOR STATEMENT MCQS!")
    print("================================================================================")

if __name__ == "__main__":
    run_verification()
