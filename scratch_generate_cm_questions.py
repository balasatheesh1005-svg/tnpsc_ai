import json
import os

# Helper to construct a question dictionary
def make_q(qid, diff, qtype, bloom, est_time, pyq_sim, q_en, q_ta, opt_list, corr, exp_en, exp_ta, wno_dict, tip_en, tip_ta, rev_en, rev_ta, tags=None):
    if tags is None:
        tags = ["Chief Minister", "State Council of Ministers", "Polity"]
    
    # opt_list is list of tuples: [("A", en, ta), ("B", en, ta), ("C", en, ta), ("D", en, ta)]
    options_arr = []
    options_en = []
    options_ta = []
    for opt_id, en, ta in opt_list:
        options_arr.append({"id": opt_id, "en": en, "ta": ta})
        options_en.append(en)
        options_ta.append(ta)
        
    why_not_formatted = {}
    for opt_id in ["A", "B", "C", "D"]:
        if opt_id in wno_dict:
            why_not_formatted[opt_id] = {
                "en": wno_dict[opt_id]["en"],
                "ta": wno_dict[opt_id]["ta"]
            }
        else:
            why_not_formatted[opt_id] = {
                "en": f"Option {opt_id} is incorrect.",
                "ta": f"தேர்வு {opt_id} தவறானது."
            }

    return {
        "id": qid,
        "subject": "Polity",
        "topic": "Chief Minister & State Council of Ministers",
        "difficulty": diff,
        "question_type": qtype,
        "question": {
            "en": q_en,
            "ta": q_ta
        },
        "question_en": q_en,
        "question_ta": q_ta,
        "options": options_arr,
        "options_en": options_en,
        "options_ta": options_ta,
        "correct_answer": corr.upper(),
        "answer": corr.lower(),
        "explanation": {
            "en": exp_en,
            "ta": exp_ta
        },
        "explanation_en": exp_en,
        "explanation_ta": exp_ta,
        "why_not_others": why_not_formatted,
        "tnpsc_tip": {
            "en": tip_en,
            "ta": tip_ta
        },
        "revision_fact": {
            "en": rev_en,
            "ta": rev_ta
        },
        "source_reference": [
            "M. Laxmikanth – Indian Polity",
            "NCERT",
            "Samacheer Kalvi"
        ],
        "bloom_level": bloom,
        "estimated_time_sec": est_time,
        "pyq_similarity": pyq_sim,
        "tags": tags
    }

print("Helper script initialized.")
