import json
import sys
from pathlib import Path

# Load questions directly from the python code files by stripping out the file I/O blocks properly

target_path = Path(r"c:\Users\Home\Desktop\tnpsc_ai\data\questions\polity\historical_background_medium.json")

def clean_code(code_str):
    lines = code_str.split("\n")
    cleaned = []
    skip = False
    for line in lines:
        if "with open(" in line:
            skip = True
            continue
        if skip and ("json.dump(" in line or "questions = json.load(" in line):
            skip = False
            continue
        if not skip:
            # remove lone print statements if any
            if line.strip().startswith("print("):
                continue
            cleaned.append(line)
    return "\n".join(cleaned)

all_q_map = {}

# 1. full (Q1 to Q20)
with open(Path(r"c:\Users\Home\Desktop\tnpsc_ai\scratch_generate_hb_medium_full.py"), "r", encoding="utf-8") as f:
    c1 = clean_code(f.read())
s1 = {}
exec(c1, s1)
for q in s1.get("questions", []):
    all_q_map[q["id"]] = q

# 2. part2 (Q21 to Q30)
with open(Path(r"c:\Users\Home\Desktop\tnpsc_ai\scratch_generate_hb_medium_part2.py"), "r", encoding="utf-8") as f:
    c2 = clean_code(f.read())
s2 = {"questions": []}
exec(c2, s2)
for q in s2.get("questions", []):
    all_q_map[q["id"]] = q

# 3. part3 (Q31 to Q50)
with open(Path(r"c:\Users\Home\Desktop\tnpsc_ai\scratch_generate_hb_medium_part3.py"), "r", encoding="utf-8") as f:
    c3 = clean_code(f.read())
s3 = {"questions": []}
exec(c3, s3)
for q in s3.get("questions", []):
    all_q_map[q["id"]] = q

sorted_keys = sorted(all_q_map.keys())
print(f"Total unique IDs found: {len(sorted_keys)}")
print("IDs:", sorted_keys)

final_50 = [all_q_map[k] for k in sorted_keys]

assert len(final_50) == 50, f"Expected 50, got {len(final_50)}"

# Save to target JSON
target_path.parent.mkdir(parents=True, exist_ok=True)
with open(target_path, "w", encoding="utf-8") as f:
    json.dump(final_50, f, ensure_ascii=False, indent=2)

print(f"Successfully saved all 50 questions to {target_path}")

# Run schema validation
sys.path.insert(0, r"c:\Users\Home\Desktop\tnpsc_ai")
from core.question_engine.validators import validate_questions
val_res = validate_questions(final_50)
print(f"Schema Validation Passed: {val_res.valid}")
if val_res.errors:
    print("Errors:", val_res.errors)
if val_res.warnings:
    print("Warnings:", val_res.warnings)
