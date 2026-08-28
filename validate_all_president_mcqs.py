import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("==================================================")
print("FINAL CROSS-DATASET VALIDATION: PRESIDENT MCQs")
print("==================================================")

datasets = [
    ("easy.json", "data/questions/polity/president_easy.json", 50),
    ("medium.json", "data/questions/polity/president_medium.json", 50),
    ("hard.json", "data/questions/polity/president_hard.json", 50),
    ("statement.json", "data/questions/polity/president_statement.json", 50),
    ("reasoning.json", "data/questions/polity/president_reasoning.json", 25),
    ("chronology.json", "data/questions/polity/president_chronology.json", 25),
    ("match.json", "data/questions/polity/president_match.json", 25),
    ("grand_test.json", "data/questions/polity/president_grand_test.json", 100)
]

all_ids = set()
all_question_titles = set()
total_questions = 0

passed_all = True
results = {}

for name, path, expected_count in datasets:
    if not os.path.exists(path):
        print(f"❌ FAIL: File missing: {path}")
        passed_all = False
        continue
        
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"❌ FAIL: Invalid JSON in {path}: {e}")
        passed_all = False
        continue
        
    q_count = len(data)
    total_questions += q_count
    
    if q_count != expected_count:
        print(f"❌ FAIL: {name} count mismatch! Expected {expected_count}, got {q_count}")
        passed_all = False
    else:
        print(f"  {name}: {q_count} questions (Matches expected {expected_count})")
        
    for idx, q in enumerate(data):
        q_id = q.get("id")
        if not q_id:
            print(f"❌ FAIL: Question at index {idx} in {name} missing ID!")
            passed_all = False
        elif q_id in all_ids:
            print(f"❌ FAIL: Duplicate ID found: {q_id}")
            passed_all = False
        else:
            all_ids.add(q_id)
            
        # Options check
        opts = q.get("options", [])
        if len(opts) != 4:
            print(f"❌ FAIL: Question {q_id} in {name} does not have exactly 4 options!")
            passed_all = False
            
        opt_ids = [opt.get("id") for opt in opts]
        if opt_ids != ["A", "B", "C", "D"]:
            print(f"❌ FAIL: Question {q_id} in {name} option IDs are not A, B, C, D! Got {opt_ids}")
            passed_all = False
            
        corr = q.get("correct_answer")
        if corr not in ["A", "B", "C", "D"]:
            print(f"❌ FAIL: Question {q_id} in {name} has invalid correct_answer: {corr}")
            passed_all = False
            
        # Bilingual check
        q_text = q.get("question")
        if isinstance(q_text, dict):
            if not q_text.get("en") or not q_text.get("ta"):
                print(f"❌ FAIL: Question {q_id} missing bilingual text in dict!")
                passed_all = False
            title_str = q_text.get("en")
        else:
            if not q.get("question_en") or not q.get("question_ta"):
                print(f"❌ FAIL: Question {q_id} missing flat question_en/ta!")
                passed_all = False
            title_str = q.get("question_en")
            
        # Explanation check
        exp = q.get("explanation")
        if isinstance(exp, dict):
            if not exp.get("en") or not exp.get("ta"):
                print(f"❌ FAIL: Question {q_id} missing bilingual explanation!")
                passed_all = False
        elif not q.get("explanation_en") or not q.get("explanation_ta"):
            print(f"❌ FAIL: Question {q_id} missing flat explanation_en/ta!")
            passed_all = False
            
        # Trap point check
        trap = q.get("trap_point")
        if not trap:
            print(f"❌ FAIL: Question {q_id} missing trap_point!")
            passed_all = False
            
        # Match specific check
        if q.get("question_type") == "Match":
            opt_ens = [opt.get("en") for opt in opts]
            if len(set(opt_ens)) != 4:
                print(f"❌ FAIL: Match Question {q_id} has non-unique options: {opt_ens}")
                passed_all = False

print("\n--------------------------------------------------")
print(f"Total Questions Verified: {total_questions} / 375")
print(f"Total Unique IDs Verified: {len(all_ids)}")

if passed_all and total_questions == 375:
    print("SUCCESS: ALL 8 DATASETS PASSED MANDATORY CROSS-DATASET VALIDATION!")
else:
    print("FAILED: CROSS-DATASET VALIDATION ISSUES DETECTED!")
