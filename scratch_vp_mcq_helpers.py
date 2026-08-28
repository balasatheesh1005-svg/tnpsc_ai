import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("==================================================")
print("VICE-PRESIDENT MCQ GENERATION ENGINE — BATCH GENERATOR")
print("==================================================")

# Helper function to format option dicts and why_not_others
def make_options(opt_a_en, opt_a_ta, opt_b_en, opt_b_ta, opt_c_en, opt_c_ta, opt_d_en, opt_d_ta):
    return [
        {"id": "A", "en": opt_a_en, "ta": opt_a_ta},
        {"id": "B", "en": opt_b_en, "ta": opt_b_ta},
        {"id": "C", "en": opt_c_en, "ta": opt_c_ta},
        {"id": "D", "en": opt_d_en, "ta": opt_d_ta}
    ]

def make_wno(corr, a_en, a_ta, b_en, b_ta, c_en, c_ta, d_en, d_ta):
    wno = {}
    m = {"A": (a_en, a_ta), "B": (b_en, b_ta), "C": (c_en, c_ta), "D": (d_en, d_ta)}
    for k, (en_t, ta_t) in m.items():
        if k == corr:
            wno[k] = {
                "en": f"Correct. {en_t}",
                "ta": f"சரி. {ta_t}"
            }
        else:
            wno[k] = {
                "en": f"Incorrect. {en_t}",
                "ta": f"தவறு. {ta_t}"
            }
    return wno

def build_q(qid, diff, qtype, q_en, q_ta, opts, corr, exp_en, exp_ta, wno, tip_en, tip_ta, trap_en, trap_ta, src):
    opts_en = [o["en"] for o in opts]
    opts_ta = [o["ta"] for o in opts]
    return {
        "id": qid,
        "subject": "Indian Polity",
        "topic": "Vice-President of India",
        "difficulty": diff,
        "question_type": qtype,
        "question": {"en": q_en, "ta": q_ta},
        "question_en": q_en,
        "question_ta": q_ta,
        "options": opts,
        "options_en": opts_en,
        "options_ta": opts_ta,
        "correct_answer": corr,
        "answer": corr,
        "explanation": {"en": exp_en, "ta": exp_ta},
        "explanation_en": exp_en,
        "explanation_ta": exp_ta,
        "why_not_others": wno,
        "tnpsc_tip": {"en": tip_en, "ta": tip_ta},
        "trap_point": {"en": trap_en, "ta": trap_ta},
        "source_reference": src,
        "tags": ["Polity", "Vice-President", "TNPSC Group 1"],
        "metadata": {
            "bloom_level": "Understand",
            "estimated_time_sec": 60,
            "pyq_similarity": "Standard"
        }
    }

print("Helper functions initialized successfully.")
