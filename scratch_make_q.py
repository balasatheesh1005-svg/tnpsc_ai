import json
import os

def make_q(qid, diff, bloom, est_time, q_en, q_ta, opt_a_en, opt_a_ta, opt_b_en, opt_b_ta, opt_c_en, opt_c_ta, opt_d_en, opt_d_ta, corr, exp_en, exp_ta, wno_a_en, wno_a_ta, wno_b_en, wno_b_ta, wno_c_en, wno_c_ta, wno_d_en, wno_d_ta, tip_en, tip_ta, rev_en, rev_ta):
    corr = corr.upper()
    ans = corr.lower()
    return {
        "id": qid,
        "subject": "Polity",
        "topic": "Chief Minister & State Council of Ministers",
        "difficulty": diff,
        "question_type": diff,
        "question": {
            "en": q_en,
            "ta": q_ta
        },
        "question_en": q_en,
        "question_ta": q_ta,
        "options": [
            {"id": "A", "en": opt_a_en, "ta": opt_a_ta},
            {"id": "B", "en": opt_b_en, "ta": opt_b_ta},
            {"id": "C", "en": opt_c_en, "ta": opt_c_ta},
            {"id": "D", "en": opt_d_en, "ta": opt_d_ta}
        ],
        "options_en": [opt_a_en, opt_b_en, opt_c_en, opt_d_en],
        "options_ta": [opt_a_ta, opt_b_ta, opt_c_ta, opt_d_ta],
        "correct_answer": corr,
        "answer": ans,
        "explanation": {
            "en": exp_en,
            "ta": exp_ta
        },
        "explanation_en": exp_en,
        "explanation_ta": exp_ta,
        "why_not_others": {
            "A": {"en": wno_a_en, "ta": wno_a_ta},
            "B": {"en": wno_b_en, "ta": wno_b_ta},
            "C": {"en": wno_c_en, "ta": wno_c_ta},
            "D": {"en": wno_d_en, "ta": wno_d_ta}
        },
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
        "pyq_similarity": "Standard",
        "tags": ["Chief Minister", "State Council of Ministers", "Polity"]
    }

print("make_q function defined successfully.")
