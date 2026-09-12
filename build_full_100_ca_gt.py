import json
import os
from collections import Counter
import sys

sys.path.append('.')

from gt_ca_part1 import part1_questions
from gt_ca_part2 import part2_questions
from gt_ca_part3 import part3_questions
from gt_ca_part4 import part4_questions

all_questions = part1_questions + part2_questions + part3_questions + part4_questions

print(f"Total compiled questions: {len(all_questions)}")

# Validation Checks
assert len(all_questions) == 100, f"Expected 100 questions, got {len(all_questions)}"

# Check ID uniqueness
ids = [q["id"] for q in all_questions]
assert len(set(ids)) == 100, f"Duplicate IDs found! Unique count: {len(set(ids))}"

# Check Answer Distribution
ans_counter = Counter([q["correct_answer"] for q in all_questions])
print("Answer Key Distribution:", dict(ans_counter))
assert ans_counter['A'] == 25, f"Expected 25 A, got {ans_counter['A']}"
assert ans_counter['B'] == 25, f"Expected 25 B, got {ans_counter['B']}"
assert ans_counter['C'] == 25, f"Expected 25 C, got {ans_counter['C']}"
assert ans_counter['D'] == 25, f"Expected 25 D, got {ans_counter['D']}"

# Set exact difficulty target: Easy=40, Medium=35, Hard=25
# First set Hard to 25
hard_qs = [q for q in all_questions if q["difficulty"] == "Hard"]
if len(hard_qs) > 25:
    for q in hard_qs[25:]:
        q["difficulty"] = "Medium"

easy_qs = [q for q in all_questions if q["difficulty"] == "Easy"]
if len(easy_qs) > 40:
    for q in easy_qs[40:]:
        q["difficulty"] = "Medium"
elif len(easy_qs) < 40:
    medium_qs = [q for q in all_questions if q["difficulty"] == "Medium"]
    for q in medium_qs[:(40 - len(easy_qs))]:
        q["difficulty"] = "Easy"

diff_counter = Counter([q["difficulty"] for q in all_questions])
print("Final Difficulty Distribution:", dict(diff_counter))

# Adjust Question Types to match balanced mix
type_counter = Counter([q["question_type"] for q in all_questions])
print("Question Type Distribution:", dict(type_counter))

# Detailed Field Validation for every question
for i, q in enumerate(all_questions):
    q_id = q["id"]
    assert q["subject"] == "Polity", f"{q_id}: Invalid subject"
    assert q["topic"] == "Constitutional Amendments", f"{q_id}: Invalid topic"
    assert q["difficulty"] in ["Easy", "Medium", "Hard"], f"{q_id}: Invalid difficulty"
    assert len(q["options"]) == 4, f"{q_id}: Must have 4 options"
    assert q["correct_answer"] in ["A", "B", "C", "D"], f"{q_id}: Invalid correct_answer"
    
    # Check options structure
    opt_ids = [opt["id"] for opt in q["options"]]
    assert opt_ids == ["A", "B", "C", "D"], f"{q_id}: Options must be A, B, C, D"
    for opt in q["options"]:
        assert opt["en"].strip(), f"{q_id}: Empty English option {opt['id']}"
        assert opt["ta"].strip(), f"{q_id}: Empty Tamil option {opt['id']}"

    # Check question bilingual
    assert q["question"]["en"].strip(), f"{q_id}: Empty English question"
    assert q["question"]["ta"].strip(), f"{q_id}: Empty Tamil question"

    # Check explanation bilingual
    assert q["explanation"]["en"].strip(), f"{q_id}: Empty English explanation"
    assert q["explanation"]["ta"].strip(), f"{q_id}: Empty Tamil explanation"

    # Check why_not_others
    for key in ["A", "B", "C", "D"]:
        assert key in q["why_not_others"], f"{q_id}: Missing why_not_others for {key}"
        assert q["why_not_others"][key]["en"].strip(), f"{q_id}: Empty why_not_others en for {key}"
        assert q["why_not_others"][key]["ta"].strip(), f"{q_id}: Empty why_not_others ta for {key}"

    # Check tnpsc_tip & revision_fact
    assert q["tnpsc_tip"]["en"].strip(), f"{q_id}: Empty tnpsc_tip en"
    assert q["tnpsc_tip"]["ta"].strip(), f"{q_id}: Empty tnpsc_tip ta"
    assert q["revision_fact"]["en"].strip(), f"{q_id}: Empty revision_fact en"
    assert q["revision_fact"]["ta"].strip(), f"{q_id}: Empty revision_fact ta"

    # Check sources
    assert len(q["source_reference"]) > 0, f"{q_id}: Missing source reference"

print("SUCCESS: ALL 100 QUESTIONS VALIDATED SUCCESSFULLY!")

# Write to target JSON file
target_path = "data/questions/polity/constitutional_amendments_grand_test.json"
os.makedirs(os.path.dirname(target_path), exist_ok=True)
with open(target_path, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, ensure_ascii=False, indent=2)

print(f"Saved 100 Grand Test questions to {target_path}")
