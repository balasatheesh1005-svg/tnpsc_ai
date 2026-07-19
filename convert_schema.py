import json
from pathlib import Path

# Paths
repo_path = Path(r"c:\Users\Home\Desktop\tnpsc_ai\group1_2021_official.json")
repo_pyq_path = Path(r"c:\Users\Home\Desktop\tnpsc_ai\data\pyq\group1\group1_2021_official.json")

# Read current JSON
with repo_path.open("r", encoding="utf-8") as f:
    questions = json.load(f)

print(f"Original question count: {len(questions)}")

# Convert schema
converted_questions = []
for q in questions:
    q_en = q["language"]["en"]
    q_ta = q["language"]["ta"]
    
    new_q = {
        "id": q["id"],
        "year": q["year"],
        "exam": q["exam"],
        "paper_code": q["paper_code"],
        "question_number": q["question_number"],
        "question_en": q_en,
        "question_ta": q_ta,
        "options": {
            "A": f"{q['options']['A']['en']}\n{q['options']['A']['ta']}",
            "B": f"{q['options']['B']['en']}\n{q['options']['B']['ta']}",
            "C": f"{q['options']['C']['en']}\n{q['options']['C']['ta']}",
            "D": f"{q['options']['D']['en']}\n{q['options']['D']['ta']}"
        },
        "correct_answers": q["correct_answers"],
        "answer_status": q["answer_status"],
        "subject": q["subject"],
        "topic": q["topic"],
        "subtopic": q["subtopic"],
        "difficulty": q["difficulty"],
        "question_type": q["question_type"],
        "related_notes": q["related_notes"],
        "tags": q["tags"]
    }
    converted_questions.append(new_q)

# Overwrite files
with repo_path.open("w", encoding="utf-8") as f:
    json.dump(converted_questions, f, ensure_ascii=False, indent=2)
    f.write("\n")
print(f"Overwrote {repo_path}")

repo_pyq_path.parent.mkdir(parents=True, exist_ok=True)
with repo_pyq_path.open("w", encoding="utf-8") as f:
    json.dump(converted_questions, f, ensure_ascii=False, indent=2)
    f.write("\n")
print(f"Overwrote {repo_pyq_path}")

# Run validation checks on converted questions
validation_passed = True
missing_fields = []
questions_converted = len(converted_questions)

for idx, q in enumerate(converted_questions):
    q_id = q["id"]
    
    # Check required fields
    required = [
        "id", "year", "exam", "paper_code", "question_number", 
        "question_en", "question_ta", "options", "correct_answers", 
        "answer_status", "subject", "topic", "subtopic", 
        "difficulty", "question_type", "related_notes", "tags"
    ]
    for r in required:
        if r not in q:
            missing_fields.append(f"{q_id}: missing field '{r}'")
            validation_passed = False
            
    # Check no language key is left
    if "language" in q:
        validation_passed = False
        missing_fields.append(f"{q_id}: language key still present")
        
    # Check options are strings
    for o in ("A", "B", "C", "D"):
        if o not in q["options"]:
            validation_passed = False
            missing_fields.append(f"{q_id}: option {o} missing")
        elif not isinstance(q["options"][o], str):
            validation_passed = False
            missing_fields.append(f"{q_id}: option {o} is not a string")
        elif "\n" not in q["options"][o]:
            validation_passed = False
            missing_fields.append(f"{q_id}: option {o} missing bilingual separator")

print(f"Validation passed: {validation_passed}")
if missing_fields:
    print(f"Errors found ({len(missing_fields)}):")
    for err in missing_fields[:10]:
        print(err)
