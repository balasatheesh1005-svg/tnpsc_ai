import json
import os
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from core.topics_loader import get_topic_metadata_by_id
from core.navigation_v2.navigation_state import check_repository_availability
from core.question_loader import load_questions

def test_preamble_medium_suite():
    print("==================================================")
    print("RUNNING PREAMBLE MEDIUM 50 PRACTICE VERIFICATION SUITE")
    print("==================================================")

    # 1. File existence & JSON parsing
    file_path = "data/questions/polity/preamble_medium.json"
    assert os.path.exists(file_path), f"File {file_path} does not exist!"

    with open(file_path, encoding="utf-8") as f:
        questions = json.load(f)

    print(f"\n1. JSON File Load ({file_path}):")
    print(f"   - Total Questions Loaded: {len(questions)}")
    assert len(questions) == 50, f"Expected 50 questions, got {len(questions)}"
    print("   [OK] Total count = 50 PASSED")

    # 2. Schema & Difficulty Audit
    print("\n2. Dual-Schema & Key Audit:")
    ids = []
    ans_list = []
    for idx, q in enumerate(questions):
        q_id = q.get("id")
        ids.append(q_id)
        ans = q.get("correct_answer")
        ans_list.append(ans)

        # Audit difficulty
        assert q.get("difficulty") == "Medium", f"Question {q_id} difficulty is not Medium!"

        # Audit dual schema keys
        assert q_id, f"Question index {idx} missing ID"
        assert "question" in q and "en" in q["question"] and "ta" in q["question"], f"Missing question dict in {q_id}"
        assert "options" in q and len(q["options"]) == 4, f"Options missing or not 4 in {q_id}"
        assert ans in ["A", "B", "C", "D"], f"Invalid correct_answer in {q_id}"
        assert "explanation" in q and "en" in q["explanation"] and "ta" in q["explanation"], f"Missing explanation dict in {q_id}"
        assert "question_en" in q and "question_ta" in q, f"Missing flat question in {q_id}"
        assert "options_en" in q and len(q["options_en"]) == 4, f"Missing flat options_en in {q_id}"
        assert "options_ta" in q and len(q["options_ta"]) == 4, f"Missing flat options_ta in {q_id}"
        assert "answer" in q and q["answer"] in ["a", "b", "c", "d"], f"Missing flat answer in {q_id}"
        assert "explanation_en" in q and "explanation_ta" in q, f"Missing flat explanation in {q_id}"

    assert len(set(ids)) == 50, "Duplicate question IDs detected!"
    print("   [OK] All 50 questions pass dual-schema and difficulty validation")

    # 3. Answer Distribution Audit
    print("\n3. Answer Key Distribution:")
    counts = Counter(ans_list)
    for k in sorted(counts.keys()):
        print(f"   - Option {k}: {counts[k]}")
    assert all(counts[k] >= 10 for k in ["A", "B", "C", "D"]), "Answer key distribution is imbalanced!"
    print("   [OK] Answer Key Distribution PASSED")

    # 4. Navigation & Availability Test - Part 1
    print("\n4. Testing Topic Navigation - Preamble Part 1 (Medium):")
    avail_p1 = check_repository_availability("polity", "polity_preamble_part_1")
    print(f"   - polity_preamble_part_1 availability: {avail_p1}")
    assert avail_p1.get("medium") == True, "Medium repository should be available for Preamble Part 1!"

    qs_p1 = load_questions("polity", "polity_preamble_part_1", "medium")
    print(f"   - Loaded questions for Part 1: {len(qs_p1)}")
    assert len(qs_p1) == 50, f"Expected 50 questions for Part 1, got {len(qs_p1)}"
    print("   [OK] Part 1 Navigation & Question Loading PASSED")

    # 5. Navigation & Availability Test - Part 2
    print("\n5. Testing Topic Navigation - Preamble Part 2 (Medium):")
    avail_p2 = check_repository_availability("polity", "polity_preamble_part_2")
    print(f"   - polity_preamble_part_2 availability: {avail_p2}")
    assert avail_p2.get("medium") == True, "Medium repository should be available for Preamble Part 2!"

    qs_p2 = load_questions("polity", "polity_preamble_part_2", "medium")
    print(f"   - Loaded questions for Part 2: {len(qs_p2)}")
    assert len(qs_p2) == 50, f"Expected 50 questions for Part 2, got {len(qs_p2)}"
    assert qs_p1[0]["id"] == qs_p2[0]["id"], "Part 1 and Part 2 should load the common Preamble Medium repository!"
    print("   [OK] Part 2 Navigation & Shared Repository Load PASSED")

    # 6. Regression Testing Other Topics & Easy Repo
    print("\n6. Regression Verification of Existing Repositories:")
    other_topics = [
        ("polity", "polity_historical_background_part1", "medium"),
        ("polity", "polity_making_of_indian_constitution_part_1", "medium"),
        ("polity", "polity_salient_features_of_the_indian_constitution_part_1", "medium"),
        ("polity", "polity_preamble_part_1", "easy")
    ]
    for subj, top_id, level in other_topics:
        avail = check_repository_availability(subj, top_id)
        assert avail.get(level) == True, f"{level} repo broken for {top_id}"
        loaded = load_questions(subj, top_id, level)
        assert len(loaded) >= 50, f"Question count insufficient for {top_id} ({level})"
        print(f"   [OK] {top_id} ({level}) loads {len(loaded)} questions cleanly.")

    print("\n==================================================")
    print("ALL PREAMBLE MEDIUM 50 PRACTICE VERIFICATION CHECKS PASSED SUCCESSFULLY!")
    print("==================================================")

if __name__ == "__main__":
    test_preamble_medium_suite()
