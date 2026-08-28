import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("==================================================")
print("TNPSC NOVA AI MCQ VALIDATION ENGINE — FULL SUITE")
print("==================================================")

datasets_to_check = [
    ("easy.json", "data/questions/polity/president_easy.json", 50),
    ("medium.json", "data/questions/polity/president_medium.json", 50),
    ("hard.json", "data/questions/polity/president_hard.json", 50),
    ("statement.json", "data/questions/polity/president_statement.json", 50),
    ("reasoning.json", "data/questions/polity/president_reasoning.json", 25),
    ("chronology.json", "data/questions/polity/president_chronology.json", 25),
    ("match.json", "data/questions/polity/president_match.json", 25),
    ("grand_test.json", "data/questions/polity/president_grand_test.json", 100)
]

# Track overall metrics
all_question_ids = set()
all_question_hashes = set()
total_questions_processed = 0
validation_errors = []
corrections_made = 0

# Check each file
for name, filepath, expected_count in datasets_to_check:
    print(f"\n--- Checking {name} ({filepath}) ---")
    if not os.path.exists(filepath):
        validation_errors.append(f"File missing: {filepath}")
        continue

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            q_list = json.load(f)
    except Exception as e:
        validation_errors.append(f"JSON Parse Error in {name}: {str(e)}")
        continue

    q_count = len(q_list)
    print(f"File exists, parsed valid JSON. Question count: {q_count} (Expected: {expected_count})")
    if q_count != expected_count:
        validation_errors.append(f"Count mismatch in {name}: expected {expected_count}, found {q_count}")

    total_questions_processed += q_count

    # Check individual questions
    for idx, q in enumerate(q_list):
        q_id = q.get("id")
        if not q_id:
            validation_errors.append(f"Question at index {idx} in {name} lacks 'id'")
        elif q_id in all_question_ids:
            validation_errors.append(f"Duplicate ID '{q_id}' found in {name}")
        else:
            all_question_ids.add(q_id)

        # Mandatory fields
        req_fields = ["subject", "topic", "difficulty", "question_type", "correct_answer", "source_reference", "trap_point"]
        for rf in req_fields:
            if not q.get(rf):
                validation_errors.append(f"Question {q_id} in {name} missing required field '{rf}'")

        # Options check
        opts = q.get("options", [])
        if len(opts) != 4:
            validation_errors.append(f"Question {q_id} in {name} has {len(opts)} options, expected 4")
        else:
            opt_ids = [opt.get("id") for opt in opts]
            if opt_ids != ["A", "B", "C", "D"]:
                validation_errors.append(f"Question {q_id} in {name} option IDs are {opt_ids}, expected ['A', 'B', 'C', 'D']")
            
            # Check for non-empty text in both languages
            for opt in opts:
                if not opt.get("en") or not opt.get("ta"):
                    validation_errors.append(f"Question {q_id} option {opt.get('id')} has missing English/Tamil text")

        # Correct answer validity
        corr = q.get("correct_answer")
        if corr not in ["A", "B", "C", "D"]:
            validation_errors.append(f"Question {q_id} in {name} has invalid correct_answer '{corr}'")

        # Bilingual check
        q_text = q.get("question")
        if isinstance(q_text, dict):
            if not q_text.get("en") or not q_text.get("ta"):
                validation_errors.append(f"Question {q_id} missing bilingual question text")
            h_str = q_text.get("en", "")
        else:
            if not q.get("question_en") or not q.get("question_ta"):
                validation_errors.append(f"Question {q_id} missing flat question_en/ta")
            h_str = q.get("question_en", "")

        exp_text = q.get("explanation")
        if isinstance(exp_text, dict):
            if not exp_text.get("en") or not exp_text.get("ta"):
                validation_errors.append(f"Question {q_id} missing bilingual explanation")
        elif not q.get("explanation_en") or not q.get("explanation_ta"):
            validation_errors.append(f"Question {q_id} missing flat explanation_en/ta")

        # Duplicate question detection (ignoring ID prefix differences)
        clean_h = h_str.strip().lower()
        if clean_h in all_question_hashes and name != "grand_test.json":
            # Note: Grand Test can test similar concepts from different angles, but check if duplicate hash
            validation_errors.append(f"Duplicate question text detected in {name}: '{h_str[:50]}...'")
        else:
            all_question_hashes.add(clean_h)

        # Match specific checks
        if q.get("question_type") == "Match":
            opt_texts = [opt.get("en") for opt in opts]
            if len(set(opt_texts)) != 4:
                validation_errors.append(f"Match Question {q_id} has duplicate/non-unique option codes: {opt_texts}")

        # Chronology specific checks
        if q.get("question_type") == "Chronology":
            opt_texts = [opt.get("en") for opt in opts]
            if len(set(opt_texts)) != 4:
                validation_errors.append(f"Chronology Question {q_id} has duplicate/non-unique sequence options: {opt_texts}")

print("\n==================================================")
print("VALIDATION RESULTS SUMMARY")
print("==================================================")
print(f"Total Files Checked: {len(datasets_to_check)}")
print(f"Total Questions Processed: {total_questions_processed} / 375")
print(f"Total Unique IDs: {len(all_question_ids)}")

if not validation_errors:
    print("\n✅ STATIC VALIDATION RESULT: 100% PASS! NO ERRORS FOUND.")
else:
    print(f"\n❌ STATIC VALIDATION RESULT: FOUND {len(validation_errors)} ERRORS:")
    for err in validation_errors:
        print(f"  - {err}")
