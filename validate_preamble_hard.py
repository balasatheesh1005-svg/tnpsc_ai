import json
import os
import sys

filepath = "data/questions/polity/preamble_hard.json"

if not os.path.exists(filepath):
    print(f"Error: {filepath} does not exist!")
    sys.exit(1)

with open(filepath, "r", encoding="utf-8") as f:
    questions = json.load(f)

print(f"Validating {len(questions)} questions from {filepath}...\n")

if len(questions) != 50:
    print(f"❌ Failed: Total questions count is {len(questions)}, expected 50.")
    sys.exit(1)

required_keys = [
    "id", "subject", "topic", "difficulty", "question_type",
    "question", "options", "correct_answer", "explanation",
    "why_not_others", "tnpsc_tip", "revision_fact",
    "source_reference", "bloom_level", "estimated_time_sec",
    "pyq_similarity", "tags", "question_en", "question_ta",
    "options_en", "options_ta", "answer", "explanation_en", "explanation_ta"
]

ids_set = set()
errors = []

for idx, q in enumerate(questions, 1):
    q_id = q.get("id", f"Q_{idx}")
    
    # Check ID duplicate
    if q_id in ids_set:
        errors.append(f"Q#{idx}: Duplicate ID '{q_id}'")
    ids_set.add(q_id)
    
    # Check difficulty
    if q.get("difficulty") != "Hard":
        errors.append(f"{q_id}: Incorrect difficulty '{q.get('difficulty')}'")
        
    # Check required keys
    for k in required_keys:
        if k not in q:
            errors.append(f"{q_id}: Missing key '{k}'")
            
    # Check options count
    opts = q.get("options", [])
    if len(opts) != 4:
        errors.append(f"{q_id}: Options count is {len(opts)}, expected 4")
        
    # Check correct answer
    ans = q.get("correct_answer")
    if ans not in ["A", "B", "C", "D"]:
        errors.append(f"{q_id}: Invalid correct_answer '{ans}'")
        
    # Check why_not_others keys A, B, C, D
    wno = q.get("why_not_others", {})
    for opt_id in ["A", "B", "C", "D"]:
        if opt_id not in wno:
            errors.append(f"{q_id}: missing why_not_others[{opt_id}]")
        else:
            if "en" not in wno[opt_id] or "ta" not in wno[opt_id]:
                errors.append(f"{q_id}: why_not_others[{opt_id}] missing en/ta")

if errors:
    print(f"❌ Validation failed with {len(errors)} errors:")
    for e in errors[:10]:
        print("  -", e)
    sys.exit(1)

print("Validation PASSED 100%! All 50 MCQs strictly adhere to TNPSC Nova AI GOLD STANDARD JSON Schema.")
