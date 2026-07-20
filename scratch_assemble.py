import json
import sys
from pathlib import Path

target_path = Path(r"c:\Users\Home\Desktop\tnpsc_ai\data\questions\polity\historical_background_medium.json")
target_path.parent.mkdir(parents=True, exist_ok=True)
with open(target_path, "w", encoding="utf-8") as f:
    json.dump([], f)

# Part 1 & 2 (Q1 to Q30)
with open(Path(r"c:\Users\Home\Desktop\tnpsc_ai\scratch_generate_hb_medium_part2.py"), "r", encoding="utf-8") as f:
    code_part2 = f.read()

scope_part2 = {}
exec(code_part2, scope_part2)
q1_to_30 = scope_part2["questions"]

# Part 3 (Q31 to Q50)
with open(Path(r"c:\Users\Home\Desktop\tnpsc_ai\scratch_generate_hb_medium_part3.py"), "r", encoding="utf-8") as f:
    code_part3 = f.read()

# Remove file read lines from part3
lines = code_part3.split("\n")
clean_lines = []
skip = False
for line in lines:
    if "with open(target_path" in line:
        skip = True
        continue
    if skip and "questions = json.load(f)" in line:
        skip = False
        continue
    if not skip:
        clean_lines.append(line)

scope_part3 = {"questions": list(q1_to_30)}
exec("\n".join(clean_lines), scope_part3)

final_questions = scope_part3["questions"]

print(f"Total questions collected: {len(final_questions)}")

with open(target_path, "w", encoding="utf-8") as f:
    json.dump(final_questions, f, ensure_ascii=False, indent=2)

print(f"Successfully saved {len(final_questions)} questions to {target_path}")

# Run schema validation
sys.path.insert(0, r"c:\Users\Home\Desktop\tnpsc_ai")
from core.question_engine.validators import validate_questions
val_res = validate_questions(final_questions)
print(f"Validation Result: Valid={val_res.valid}")
if val_res.errors:
    print("Validation Errors:", val_res.errors)
if val_res.warnings:
    print("Validation Warnings:", val_res.warnings)
