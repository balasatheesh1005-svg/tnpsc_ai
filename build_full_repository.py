import json
import sys
from pathlib import Path

target_path = Path(r"c:\Users\Home\Desktop\tnpsc_ai\data\questions\polity\historical_background_medium.json")
target_path.parent.mkdir(parents=True, exist_ok=True)

# Step 1: Run part 2 script to create Q1 to Q30 in historical_background_medium.json
print("Executing part 2 script (Q1-Q30)...")
with open(Path(r"c:\Users\Home\Desktop\tnpsc_ai\scratch_generate_hb_medium_part2.py"), "r", encoding="utf-8") as f:
    code_part2 = f.read()

exec(code_part2, {})

# Verify Q1-30 written
with open(target_path, "r", encoding="utf-8") as f:
    q_step1 = json.load(f)
print(f"Step 1 finished. Questions in file: {len(q_step1)}")

# Step 2: Run part 3 script to append Q31 to Q50
print("Executing part 3 script (Q31-Q50)...")
with open(Path(r"c:\Users\Home\Desktop\tnpsc_ai\scratch_generate_hb_medium_part3.py"), "r", encoding="utf-8") as f:
    code_part3 = f.read()

exec(code_part3, {})

# Verify Q1-50 written
with open(target_path, "r", encoding="utf-8") as f:
    q_final = json.load(f)
print(f"Step 2 finished. Final questions count in file: {len(q_final)}")

# Step 3: Run schema validation from core/question_engine/validators.py
sys.path.insert(0, r"c:\Users\Home\Desktop\tnpsc_ai")
from core.question_engine.validators import validate_questions
val_res = validate_questions(q_final)
print(f"Validation Passed: {val_res.valid}")
if val_res.errors:
    print("Errors:", val_res.errors)
if val_res.warnings:
    print("Warnings:", val_res.warnings)
