import json
import os

q_data = []

def make_q(q_id, difficulty, qtype, q_en, q_ta, options_list, ca, exp_en, exp_ta, wno_dict, trap_en, trap_ta, fact_en, fact_ta, source_list, is_exact_pyq=False, bloom="Understand", est_time=45, tags=None):
    if tags is None:
        tags = ["Polity", "Directive Principles of State Policy", "Grand Test"]
        
    options = []
    options_en = []
    options_ta = []
    for opt_id, (opt_en, opt_ta) in zip(["A", "B", "C", "D"], options_list):
        options.append({"id": opt_id, "en": opt_en, "ta": opt_ta})
        options_en.append(opt_en)
        options_ta.append(opt_ta)
        
    wno = {}
    for letter in ["A", "B", "C", "D"]:
        wno[letter] = {
            "en": wno_dict[letter][0],
            "ta": wno_dict[letter][1]
        }
        
    pyq_sim = "Exact PYQ" if is_exact_pyq else "High"
    
    obj = {
        "id": q_id,
        "subject": "Polity",
        "topic": "Directive Principles of State Policy",
        "difficulty": difficulty,
        "question_type": qtype,
        "question": {"en": q_en, "ta": q_ta},
        "options": options,
        "correct_answer": ca,
        "explanation": {"en": exp_en, "ta": exp_ta},
        "why_not_others": wno,
        "tnpsc_tip": {"en": f"TNPSC Trap: {trap_en}", "ta": f"TNPSC பொறி: {trap_ta}"},
        "revision_fact": {"en": fact_en, "ta": fact_ta},
        "source_reference": source_list,
        "bloom_level": bloom,
        "estimated_time_sec": est_time,
        "pyq_similarity": pyq_sim,
        "tags": tags,
        "question_en": q_en,
        "question_ta": q_ta,
        "options_en": options_en,
        "options_ta": options_ta,
        "answer": ca.lower(),
        "explanation_en": exp_en,
        "explanation_ta": exp_ta
    }
    return obj

# Exec generator chunks to build 100 questions
exec(open("scratch/dpsp_gt_part1.py", encoding="utf-8").read())
exec(open("scratch/dpsp_gt_part2.py", encoding="utf-8").read())
exec(open("scratch/dpsp_gt_part3.py", encoding="utf-8").read())
exec(open("scratch/dpsp_gt_part4.py", encoding="utf-8").read())

out_path_1 = 'data/questions/polity/directive_principles_grand_test.json'
out_path_2 = 'data/questions/polity/directive_principles_grand.json'

os.makedirs(os.path.dirname(out_path_1), exist_ok=True)

with open(out_path_1, 'w', encoding='utf-8') as f:
    json.dump(q_data, f, ensure_ascii=False, indent=2)

with open(out_path_2, 'w', encoding='utf-8') as f:
    json.dump(q_data, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {len(q_data)} questions in {out_path_1} and {out_path_2}.")
