import json
import os
import random

# We will build 100 distinct questions for Historical Background Grand Test.
# Let's ensure exact counts:
# Easy: 20, Medium: 35, Hard: 45
# Direct MCQ: 25, Conceptual MCQ: 20, Statement Based: 15, Assertion & Reason: 10, Match the Following: 10, Chronology: 10, Integrated PYQ Style: 10
# Answer distribution: 25 A, 25 B, 25 C, 25 D.

q_list = []

def make_q(id_num, diff, q_type, q_en, q_ta, opt_list, ans, exp_en, exp_ta, wno, tip_en, tip_ta, rf_en, rf_ta, tags, bloom="Understand", est_time=60):
    ans_upper = ans.upper()
    ans_lower = ans.lower()
    
    opts_dict = []
    opts_en = []
    opts_ta = []
    for opt_id, o_en, o_ta in opt_list:
        opts_dict.append({"id": opt_id, "en": o_en, "ta": o_ta})
        opts_en.append(o_en)
        opts_ta.append(o_ta)
        
    return {
        "id": f"HB_GT_{id_num:03d}",
        "subject": "Polity",
        "topic": "Historical Background of the Indian Constitution",
        "difficulty": diff,
        "question_type": q_type,
        "question": {"en": q_en, "ta": q_ta},
        "options": opts_dict,
        "correct_answer": ans_upper,
        "explanation": {"en": exp_en, "ta": exp_ta},
        "why_not_others": wno,
        "tnpsc_tip": {"en": tip_en, "ta": tip_ta},
        "revision_fact": {"en": rf_en, "ta": rf_ta},
        "source_reference": [
            "M. Laxmikanth - Indian Polity",
            "NCERT Class XI/XII - Indian Constitution at Work",
            "Samacheer Kalvi - Standard 11/12 Political Science"
        ],
        "bloom_level": bloom,
        "estimated_time_sec": est_time,
        "pyq_similarity": "High",
        "tags": tags,
        "question_en": q_en,
        "question_ta": q_ta,
        "options_en": opts_en,
        "options_ta": opts_ta,
        "answer": ans_lower,
        "explanation_en": exp_en,
        "explanation_ta": exp_ta
    }

print("Helper function defined.")
