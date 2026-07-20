import json
import sys
import re
from pathlib import Path

target_path = Path(r"c:\Users\Home\Desktop\tnpsc_ai\data\questions\polity\historical_background_medium.json")

# Define make_q in main environment
def make_q(q_id, q_type, q_en, q_ta, opt_a_en, opt_a_ta, opt_b_en, opt_b_ta, opt_c_en, opt_c_ta, opt_d_en, opt_d_ta,
           correct_ans, exp_en, exp_ta, wno_a_en, wno_a_ta, wno_b_en, wno_b_ta, wno_c_en, wno_c_ta, wno_d_en, wno_d_ta,
           tip_en, tip_ta, rev_en, rev_ta, bloom, est_time, tags):
    opts = [
        {"id": "A", "en": opt_a_en, "ta": opt_a_ta},
        {"id": "B", "en": opt_b_en, "ta": opt_b_ta},
        {"id": "C", "en": opt_c_en, "ta": opt_c_ta},
        {"id": "D", "en": opt_d_en, "ta": opt_d_ta}
    ]
    opts_en = [opt_a_en, opt_b_en, opt_c_en, opt_d_en]
    opts_ta = [opt_a_ta, opt_b_ta, opt_c_ta, opt_d_ta]
    
    return {
        "id": q_id,
        "subject": "Polity",
        "topic": "Historical Background",
        "difficulty": "Medium",
        "question_type": q_type,
        "question": {"en": q_en, "ta": q_ta},
        "options": opts,
        "correct_answer": correct_ans,
        "explanation": {"en": exp_en, "ta": exp_ta},
        "why_not_others": {
            "A": {"en": wno_a_en, "ta": wno_a_ta},
            "B": {"en": wno_b_en, "ta": wno_b_ta},
            "C": {"en": wno_c_en, "ta": wno_c_ta},
            "D": {"en": wno_d_en, "ta": wno_d_ta}
        },
        "tnpsc_tip": {"en": tip_en, "ta": tip_ta},
        "revision_fact": {"en": rev_en, "ta": rev_ta},
        "source_reference": ["M. Laxmikanth - Indian Polity", "NCERT", "Samacheer Kalvi"],
        "bloom_level": bloom,
        "estimated_time_sec": est_time,
        "pyq_similarity": "High",
        "tags": tags,
        "question_en": q_en,
        "question_ta": q_ta,
        "options_en": opts_en,
        "options_ta": opts_ta,
        "answer": correct_ans.lower(),
        "explanation_en": exp_en,
        "explanation_ta": exp_ta
    }

questions_dict = {}

def process_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # find all questions.append(make_q(...)) blocks
    matches = re.findall(r"questions\.append\(make_q\((.*?)\)\)", content, re.DOTALL)
    for m in matches:
        try:
            # eval the argument list
            q_obj = eval(f"make_q({m})")
            questions_dict[q_obj["id"]] = q_obj
        except Exception as e:
            print(f"Error evaluating match in {filepath}: {e}")

process_file(Path(r"c:\Users\Home\Desktop\tnpsc_ai\scratch_generate_hb_medium_full.py"))
process_file(Path(r"c:\Users\Home\Desktop\tnpsc_ai\scratch_generate_hb_medium_part2.py"))
process_file(Path(r"c:\Users\Home\Desktop\tnpsc_ai\scratch_generate_hb_medium_part3.py"))

sorted_ids = sorted(questions_dict.keys())
print(f"Successfully processed {len(sorted_ids)} unique questions.")
print("IDs found:", sorted_ids)

final_50 = [questions_dict[k] for k in sorted_ids]

assert len(final_50) == 50, f"Expected 50 questions, found {len(final_50)}"

# Save to JSON
target_path.parent.mkdir(parents=True, exist_ok=True)
with open(target_path, "w", encoding="utf-8") as f:
    json.dump(final_50, f, ensure_ascii=False, indent=2)

print(f"Saved 50 questions to {target_path}")

# Run schema validation
sys.path.insert(0, r"c:\Users\Home\Desktop\tnpsc_ai")
from core.question_engine.validators import validate_questions
val_res = validate_questions(final_50)
print(f"Schema Validation Passed: {val_res.valid}")
if val_res.errors:
    print("Errors:", val_res.errors)
if val_res.warnings:
    print("Warnings:", val_res.warnings)
