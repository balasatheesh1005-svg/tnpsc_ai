# -*- coding: utf-8 -*-
"""
Helper module for generating 24-field schema compliant MCQs for Finance Commission of India.
Ensures full fidelity:
id, subject, topic, subtopic, difficulty, question_type,
question, question_en, question_ta,
options, options_en, options_ta,
correct_answer, answer,
explanation, explanation_en, explanation_ta,
why_not_others (keys A, B, C, D in English and Tamil),
tnpsc_tip, revision_fact, source_reference,
bloom_level, estimated_time_sec, pyq_similarity, tags
"""

def make_fc_q(
    qid: str,
    diff: str,
    qtype: str,
    subtopic: str,
    en_stem: str,
    ta_stem: str,
    en_a: str, ta_a: str,
    en_b: str, ta_b: str,
    en_c: str, ta_c: str,
    en_d: str, ta_d: str,
    correct_key: str,
    exp_en: str,
    exp_ta: str,
    why_a_en: str, why_a_ta: str,
    why_b_en: str, why_b_ta: str,
    why_c_en: str, why_c_ta: str,
    why_d_en: str, why_d_ta: str,
    tip_en: str, tip_ta: str,
    fact_en: str, fact_ta: str,
    tags: list = None,
    bloom: str = "Understand",
    time_sec: int = 45,
    pyq_sim: str = "Medium"
) -> dict:
    if tags is None:
        tags = ["polity", "finance_commission", subtopic.lower().replace(" ", "_")]
    
    return {
        "id": qid,
        "subject": "polity",
        "topic": "Finance Commission of India",
        "subtopic": subtopic,
        "difficulty": diff,
        "question_type": qtype,
        "question": {
            "en": en_stem,
            "ta": ta_stem
        },
        "question_en": en_stem,
        "question_ta": ta_stem,
        "options": [
            {"id": "A", "en": en_a, "ta": ta_a},
            {"id": "B", "en": en_b, "ta": ta_b},
            {"id": "C", "en": en_c, "ta": ta_c},
            {"id": "D", "en": en_d, "ta": ta_d}
        ],
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
        "source_reference": "Constitution of India, Article 280 & 281; Finance Commission Act 1951; Reports of 1st to 16th Finance Commissions; Laxmikanth Indian Polity (7th Ed.)",
        "bloom_level": bloom,
        "estimated_time_sec": time_sec,
        "pyq_similarity": pyq_sim,
        "tags": tags
    }
