# -*- coding: utf-8 -*-
"""
Helper module for generating high-quality, fully bilingual Municipalities MCQs
strictly conforming to the 24-field TNPSC Nova AI schema.
"""

def make_mun_q(
    qid: str,
    diff: str,
    qtype: str,
    subtopic: str,
    en_stem: str,
    ta_stem: str,
    en_a: str,
    ta_a: str,
    en_b: str,
    ta_b: str,
    en_c: str,
    ta_c: str,
    en_d: str,
    ta_d: str,
    correct_key: str,
    exp_en: str,
    exp_ta: str,
    why_a_en: str,
    why_a_ta: str,
    why_b_en: str,
    why_b_ta: str,
    why_c_en: str,
    why_c_ta: str,
    why_d_en: str,
    why_d_ta: str,
    tip_en: str,
    tip_ta: str,
    fact_en: str,
    fact_ta: str,
    tags: list = None,
    source_ref: str = "M. Laxmikanth – Indian Polity (74th Constitutional Amendment Act), NCERT Class XI, TN Samacheer Kalvi"
):
    correct_key = correct_key.strip().upper()
    diff = diff.capitalize()
    bloom = "Remember" if diff == "Easy" else ("Understand" if diff == "Medium" else "Analyze")
    
    options = [
        {"id": "A", "en": en_a, "ta": ta_a},
        {"id": "B", "en": en_b, "ta": ta_b},
        {"id": "C", "en": en_c, "ta": ta_c},
        {"id": "D", "en": en_d, "ta": ta_d}
    ]
    
    if tags is None:
        tags = ["polity", "municipalities", diff.lower()]
    
    return {
        "id": qid,
        "subject": "polity",
        "topic": "Local Government – Municipalities",
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
        "source_reference": source_ref,
        "bloom_level": bloom,
        "estimated_time_sec": 45 if diff == "Easy" else (60 if diff == "Medium" else 75),
        "pyq_similarity": "High",
        "tags": tags
    }
