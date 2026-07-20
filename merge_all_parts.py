import json
import sys
from pathlib import Path

target_path = Path(r"c:\Users\Home\Desktop\tnpsc_ai\data\questions\polity\historical_background_medium.json")

all_questions_dict = {}

# 1. From scratch_generate_hb_medium_full.py
with open(Path(r"c:\Users\Home\Desktop\tnpsc_ai\scratch_generate_hb_medium_full.py"), "r", encoding="utf-8") as f:
    code_full = f.read()

# strip write/open lines
lines = [l for l in code_full.split("\n") if "target_path" not in l and "with open" not in l and "json.dump" not in l]
scope_full = {}
exec("\n".join(lines), scope_full)
for q in scope_full.get("questions", []):
    all_questions_dict[q["id"]] = q

# 2. From scratch_generate_hb_medium_part2.py
with open(Path(r"c:\Users\Home\Desktop\tnpsc_ai\scratch_generate_hb_medium_part2.py"), "r", encoding="utf-8") as f:
    code_part2 = f.read()

lines = [l for l in code_part2.split("\n") if "target_path" not in l and "with open" not in l and "json.dump" not in l]
scope_part2 = {}
exec("\n".join(lines), scope_part2)
for q in scope_part2.get("questions", []):
    all_questions_dict[q["id"]] = q

# 3. From scratch_generate_hb_medium_part3.py
with open(Path(r"c:\Users\Home\Desktop\tnpsc_ai\scratch_generate_hb_medium_part3.py"), "r", encoding="utf-8") as f:
    code_part3 = f.read()

lines = [l for l in code_part3.split("\n") if "target_path" not in l and "with open" not in l and "json.dump" not in l]
scope_part3 = {}
exec("\n".join(lines), scope_part3)
for q in scope_part3.get("questions", []):
    all_questions_dict[q["id"]] = q

# Sort questions by ID HB_M_001 to HB_M_050
sorted_questions = [all_questions_dict[k] for k in sorted(all_questions_dict.keys())]

print(f"Total unique questions collected: {len(sorted_questions)}")
for q in sorted_questions:
    print(f"ID: {q['id']} | Type: {q['question_type']} | Correct: {q['correct_answer']}")

assert len(sorted_questions) == 50, f"Expected 50 questions, found {len(sorted_questions)}"

# Overwrite target JSON file
target_path.parent.mkdir(parents=True, exist_ok=True)
with open(target_path, "w", encoding="utf-8") as f:
    json.dump(sorted_questions, f, ensure_ascii=False, indent=2)

print(f"Successfully saved all 50 questions to {target_path}")

# Run schema validation
sys.path.insert(0, r"c:\Users\Home\Desktop\tnpsc_ai")
from core.question_engine.validators import validate_questions
val_res = validate_questions(sorted_questions)
print(f"Schema Validation Result: Valid={val_res.valid}")
if val_res.errors:
    print("Errors:", val_res.errors)
if val_res.warnings:
    print("Warnings:", val_res.warnings)
