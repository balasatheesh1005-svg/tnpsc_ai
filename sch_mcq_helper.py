# -*- coding: utf-8 -*-
"""
Helper module for generating high-quality, fully bilingual Constitutional Schedules MCQs
strictly conforming to the 24-field TNPSC Nova AI schema.
Includes factory function make_sch_q and answer key randomization.
"""
from tools.nova_content_engine.answer_randomizer import randomize_and_balance_dataset, audit_answer_pattern

def make_sch_q(
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
    tip_en: str = "",
    tip_ta: str = "",
    fact_en: str = None,
    fact_ta: str = None,
    tags: list = None,
    source_ref: str = "M. Laxmikanth – Indian Polity (Schedules of the Constitution), Constitution of India (Articles 1-395, Schedules 1-12), TN Samacheer Kalvi"
):
    if fact_en is None:
        fact_en = tip_en
    if fact_ta is None:
        fact_ta = tip_ta

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
        tags = ["polity", "constitutional_schedules", diff.lower()]
    
    return {
        "id": qid,
        "subject": "polity",
        "topic": "Constitutional Schedules",
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

def balance_question_keys(questions: list, target_counts: dict = None, seed: int = None) -> list:
    """
    Randomly and non-periodically balance and shuffle answer keys across A, B, C, D
    strictly conforming to the CRITICAL ANSWER POSITION RULE:
    - No block distribution
    - Max consecutive identical <= 2
    - No repeating cycles
    - Balanced counts
    """
    return randomize_and_balance_dataset(questions, target_counts=target_counts, seed=seed)
