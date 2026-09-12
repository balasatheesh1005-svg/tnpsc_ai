import json
import os

# Helper script to assemble 100 Grand Test questions for Constitutional Amendments
# Subject: Polity
# Topic: Constitutional Amendments
# File: data/questions/polity/constitutional_amendments_grand_test.json

questions = []

# Define helper to construct question dictionary easily and cleanly
def make_q(
    q_id, difficulty, q_type, q_en, q_ta,
    opt_a_en, opt_a_ta,
    opt_b_en, opt_b_ta,
    opt_c_en, opt_c_ta,
    opt_d_en, opt_d_ta,
    correct_ans,
    exp_en, exp_ta,
    why_a_en, why_a_ta,
    why_b_en, why_b_ta,
    why_c_en, why_c_ta,
    why_d_en, why_d_ta,
    tip_en, tip_ta,
    fact_en, fact_ta,
    sources, bloom, pyq_sim, tags
):
    return {
        "id": q_id,
        "subject": "Polity",
        "topic": "Constitutional Amendments",
        "difficulty": difficulty,
        "question_type": q_type,
        "question": {
            "en": q_en,
            "ta": q_ta
        },
        "options": [
            {"id": "A", "en": opt_a_en, "ta": opt_a_ta},
            {"id": "B", "en": opt_b_en, "ta": opt_b_ta},
            {"id": "C", "en": opt_c_en, "ta": opt_c_ta},
            {"id": "D", "en": opt_d_en, "ta": opt_d_ta}
        ],
        "correct_answer": correct_ans,
        "explanation": {
            "en": exp_en,
            "ta": exp_ta
        },
        "why_not_others": {
            "A": {"en": why_a_en, "ta": why_a_ta},
            "B": {"en": why_b_en, "ta": why_b_ta},
            "C": {"en": why_c_en, "ta": why_c_ta},
            "D": {"en": why_d_en, "ta": why_d_ta}
        },
        "tnpsc_tip": {
            "en": tip_en,
            "ta": tip_ta
        },
        "revision_fact": {
            "en": fact_en,
            "ta": fact_ta
        },
        "source_reference": sources,
        "bloom_level": bloom,
        "estimated_time_sec": 60,
        "pyq_similarity": pyq_sim,
        "tags": tags
    }

print("Helper defined.")
