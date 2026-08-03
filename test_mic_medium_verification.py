import sys
import json
import os

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

from core.topics_loader import get_topic_metadata_by_id
from core.navigation_v2.navigation_state import check_repository_availability
from core.question_loader import load_questions

json_file = r"c:\Users\Home\Desktop\tnpsc_ai\data\questions\polity\making_of_indian_constitution_medium.json"

print("=== VALIDATING MAKING OF INDIAN CONSTITUTION MEDIUM MCQs ===")

# 1. Load JSON file directly
with open(json_file, "r", encoding="utf-8") as f:
    questions = json.load(f)

print(f"Total Questions Loaded: {len(questions)}")
assert len(questions) == 50, f"Expected 50 questions, got {len(questions)}"

# 2. Check fields and IDs
for i, q in enumerate(questions, 1):
    expected_id = f"MIC_M_{i:03d}"
    assert q["id"] == expected_id, f"Line {i}: Expected ID {expected_id}, got {q['id']}"
    assert q["subject"] == "Polity"
    assert q["topic"] == "Making of Indian Constitution"
    assert q["difficulty"] == "Medium"
    assert len(q["options"]) == 4, f"Question {q['id']} does not have 4 options"
    assert q["correct_answer"] in ["A", "B", "C", "D"], f"Question {q['id']} invalid correct_answer"
    assert "en" in q["explanation"] and "ta" in q["explanation"], f"Question {q['id']} missing explanation"

print("✓ All 50 question records passed schema & option quality validation!")

# 3. Test Question Loader
loaded = load_questions("polity_making_of_indian_constitution", "medium")
print(f"Question Loader loaded {len(loaded)} questions for repo 'polity_making_of_indian_constitution', type 'medium'")
assert len(loaded) == 50, "Question loader failed to load medium MCQs"

# 4. Test Repository Availability
avail = check_repository_availability("polity", "polity_making_of_indian_constitution_part_1")
print(f"Repository Availability Check -> Medium: {avail['medium']}")
assert avail["medium"] == True, "Repository availability check failed for medium"

print("\n[OK] ALL MEDIUM MCQ VERIFICATIONS PASSED SUCCESSFULLY!")
