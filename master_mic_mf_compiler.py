import json
import sys
import importlib
from pathlib import Path

target_path = Path(r"c:\Users\Home\Desktop\tnpsc_ai\data\questions\polity\making_of_indian_constitution_match_the_following.json")
target_path.parent.mkdir(parents=True, exist_ok=True)

all_questions = []

parts = [
    "mic_mf_part1",
    "mic_mf_part2",
    "mic_mf_part3"
]

for part in parts:
    try:
        mod = importlib.import_module(part)
        if hasattr(mod, "questions"):
            print(f"Loaded {len(mod.questions)} questions from {part}")
            all_questions.extend(mod.questions)
    except Exception as e:
        print(f"Error loading {part}: {e}")

# Deduplicate by ID
seen_ids = set()
unique_questions = []
for q in all_questions:
    if q["id"] not in seen_ids:
        seen_ids.add(q["id"])
        unique_questions.append(q)

unique_questions.sort(key=lambda x: x["id"])

print(f"Total Unique Questions: {len(unique_questions)}")
print("IDs:", [q["id"] for q in unique_questions])

# Save to target_path
with open(target_path, "w", encoding="utf-8") as f:
    json.dump(unique_questions, f, ensure_ascii=False, indent=2)

print(f"Successfully saved {len(unique_questions)} questions to {target_path}")

# Run validation
sys.path.insert(0, r"c:\Users\Home\Desktop\tnpsc_ai")
from core.question_engine.validators import validate_questions
val_res = validate_questions(unique_questions)
print(f"Validation Result: Valid={val_res.valid}")
if val_res.errors:
    print("Validation Errors:", val_res.errors)
if val_res.warnings:
    print("Validation Warnings:", val_res.warnings)
