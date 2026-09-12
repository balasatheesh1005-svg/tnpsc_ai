# -*- coding: utf-8 -*-
"""
Helper for building Inter-State Relations Grand Test Questions
"""

import json
import glob

def load_core_stems():
    stems = set()
    for f in glob.glob("data/questions/polity/inter_state_relations_*.json"):
        if "grand_test" in f:
            continue
        data = json.load(open(f, encoding="utf-8"))
        for q in data:
            stems.add(q["question_en"].strip().lower())
    return stems

def make_q(num, diff, qtype, subtopic,
           en_stem, ta_stem,
           en_a, ta_a,
           en_b, ta_b,
           en_c, ta_c,
           en_d, ta_d,
           correct_key,
           exp_en, exp_ta,
           why_a_en, why_a_ta,
           why_b_en, why_b_ta,
           why_c_en, why_c_ta,
           why_d_en, why_d_ta,
           tip_en, tip_ta,
           fact_en, fact_ta):
    
    qid = f"ISR_GT_{num:03d}"
    options = [
        {"id": "A", "en": en_a, "ta": ta_a},
        {"id": "B", "en": en_b, "ta": ta_b},
        {"id": "C", "en": en_c, "ta": ta_c},
        {"id": "D", "en": en_d, "ta": ta_d}
    ]
    
    bloom = "Remember" if diff == "Easy" else ("Understand" if diff == "Medium" else "Analyze")
    
    return {
        "id": qid,
        "subject": "polity",
        "topic": "Inter-State Relations",
        "subtopic": subtopic,
        "difficulty": diff,
        "question_type": qtype,
        "question": {
            "en": en_stem,
            "ta": ta_stem
        },
        "question_en": en_stem,
        "question_ta": ta_stem,
        "options": options,
        "options_en": [en_a, en_b, en_c, en_d],
        "options_ta": [ta_a, ta_b, ta_c, ta_d],
        "correct_answer": correct_key,
        "answer": correct_key.lower(),
        "explanation": {
            "en": exp_en,
            "ta": exp_ta
        },
        "explanation_en": exp_en,
        "explanation_ta": exp_ta,
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
        "source_reference": "Laxmikanth Indian Polity, 7th Edition, Inter-State Relations",
        "bloom_level": bloom,
        "estimated_time_sec": 45 if diff == "Easy" else (60 if diff == "Medium" else 75),
        "pyq_similarity": 0.0,
        "tags": ["polity", "inter_state_relations", "grand_test"],
        "source": "Laxmikanth Indian Polity, D.D. Basu, Indian Constitution",
        "verified": True
    }
