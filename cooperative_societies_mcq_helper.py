# -*- coding: utf-8 -*-
"""
Co-operative Societies MCQ Helper Module
TNPSC Nova AI Content Engine

Provides make_coop_q to generate 100% compliant, 24-field bilingual MCQs
covering Part IX-B (Articles 243ZH to 243ZT), Article 19(1)(c), Article 43B,
97th Constitutional Amendment Act 2011, Multi-State Co-operative Societies Act 2002,
Union of India v. Rajendra N. Shah (2021) Supreme Court doctrine,
Seventh Schedule distribution (List II Entry 32 vs List I Entry 44),
and Tamil Nadu Co-operative Societies Act 1983 context.
"""
from typing import Dict, List, Optional, Any


def make_coop_q(
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
    tags: Optional[List[str]] = None,
    source_ref: str = "Constitution of India (Part IX-B, Arts 243ZH-243ZT, 19(1)(c), 43B, 368(2)), 97th CAA 2011, Union of India v. Rajendra N. Shah (2021), MSCS Act 2002, TN Co-operative Societies Act 1983, M. Laxmikanth, TN Samacheer Kalvi"
) -> Dict[str, Any]:
    correct_key = correct_key.strip().upper()
    diff = diff.strip().capitalize()
    bloom = "Remember" if diff == "Easy" else ("Understand" if diff == "Medium" else "Analyze")

    options = [
        {"id": "A", "en": en_a, "ta": ta_a},
        {"id": "B", "en": en_b, "ta": ta_b},
        {"id": "C", "en": en_c, "ta": ta_c},
        {"id": "D", "en": en_d, "ta": ta_d}
    ]

    if tags is None:
        tags = ["polity", "cooperative_societies", diff.lower(), subtopic.lower().replace(" ", "_")]

    return {
        "id": qid,
        "subject": "polity",
        "topic": "Co-operative Societies",
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
        "pyq_similarity": 0.85 if "pyq" in qid.lower() or "pyq" in qtype.lower() else 0.40,
        "tags": tags
    }


# Alias for convenience
make_cs_q = make_coop_q
