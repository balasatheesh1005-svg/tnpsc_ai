import json
import sys
from pathlib import Path

target_path = Path(r"c:\Users\Home\Desktop\tnpsc_ai\data\questions\polity\historical_background_medium.json")

with open(target_path, "r", encoding="utf-8") as f:
    raw_questions = json.load(f)

# Deduplicate by ID
seen_ids = set()
unique_questions = []

for q in raw_questions:
    q_id = q.get("id")
    if q_id and q_id not in seen_ids:
        seen_ids.add(q_id)
        unique_questions.append(q)

# Sort by ID (HB_M_001 to HB_M_050)
unique_questions.sort(key=lambda x: x["id"])

print(f"Total unique questions: {len(unique_questions)}")
for q in unique_questions:
    print(f"ID: {q['id']} | Type: {q['question_type']} | Correct: {q['correct_answer']}")

# Verify count is exactly 50
assert len(unique_questions) == 50, f"Expected 50 questions, found {len(unique_questions)}"

# Overwrite target JSON file
with open(target_path, "w", encoding="utf-8") as f:
    json.dump(unique_questions, f, ensure_ascii=False, indent=2)

print(f"Successfully finalized {len(unique_questions)} questions to {target_path}")

# Run schema validation
sys.path.insert(0, r"c:\Users\Home\Desktop\tnpsc_ai")
from core.question_engine.validators import validate_questions
val_res = validate_questions(unique_questions)
print(f"Schema Validation Passed: {val_res.valid}")
if val_res.errors:
    print("Errors:", val_res.errors)
if val_res.warnings:
    print("Warnings:", val_res.warnings)
