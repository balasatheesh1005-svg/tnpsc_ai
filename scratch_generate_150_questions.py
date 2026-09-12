import json
import os

# Create polity folder if needed
os.makedirs("data/questions/polity", exist_ok=True)

easy_path = "data/questions/polity/chief_minister_state_council_of_ministers_easy.json"
medium_path = "data/questions/polity/chief_minister_state_council_of_ministers_medium.json"
hard_path = "data/questions/polity/chief_minister_state_council_of_ministers_hard.json"

def mk(qid, diff, bloom, sec, q_en, q_ta, a_en, a_ta, b_en, b_ta, c_en, c_ta, d_en, d_ta, corr, exp_en, exp_ta, w_a_en, w_a_ta, w_b_en, w_b_ta, w_c_en, w_c_ta, w_d_en, w_d_ta, tip_en, tip_ta, rev_en, rev_ta):
    corr = corr.upper()
    return {
        "id": qid,
        "subject": "Polity",
        "topic": "Chief Minister & State Council of Ministers",
        "difficulty": diff,
        "question_type": diff,
        "question": {"en": q_en, "ta": q_ta},
        "question_en": q_en,
        "question_ta": q_ta,
        "options": [
            {"id": "A", "en": a_en, "ta": a_ta},
            {"id": "B", "en": b_en, "ta": b_ta},
            {"id": "C", "en": c_en, "ta": c_ta},
            {"id": "D", "en": d_en, "ta": d_ta}
        ],
        "options_en": [a_en, b_en, c_en, d_en],
        "options_ta": [a_ta, b_ta, c_ta, d_ta],
        "correct_answer": corr,
        "answer": corr.lower(),
        "explanation": {"en": exp_en, "ta": exp_ta},
        "explanation_en": exp_en,
        "explanation_ta": exp_ta,
        "why_not_others": {
            "A": {"en": w_a_en, "ta": w_a_ta},
            "B": {"en": w_b_en, "ta": w_b_ta},
            "C": {"en": w_c_en, "ta": w_c_ta},
            "D": {"en": w_d_en, "ta": w_d_ta}
        },
        "tnpsc_tip": {"en": tip_en, "ta": tip_ta},
        "revision_fact": {"en": rev_en, "ta": rev_ta},
        "source_reference": ["M. Laxmikanth – Indian Polity", "NCERT", "Samacheer Kalvi"],
        "bloom_level": bloom,
        "estimated_time_sec": sec,
        "pyq_similarity": "Standard",
        "tags": ["Chief Minister", "State Council of Ministers", "Polity"]
    }

print("Generator helper function ready.")
