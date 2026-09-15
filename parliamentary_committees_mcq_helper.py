# -*- coding: utf-8 -*-
"""
Parliamentary Committees MCQ Helper Module
TNPSC Nova AI Content Engine

Provides make_pc_q to generate 100% compliant, 24-field bilingual MCQs
covering Articles 105(3) & 118(1), Rules of Procedure of Lok Sabha and Rajya Sabha,
Financial Committees (Public Accounts Committee, Estimates Committee, Committee on Public Undertakings),
Departmentally Related Standing Committees (DRSCs - 24 committees, 16 LS + 8 RS),
Committees to Inquire, Scrutinize & Control (Privileges, Petitions, Assurances, Subordinate Legislation, Government Assurances),
House Keeping Committees (Business Advisory Committee, Rules Committee, General Purposes Committee),
Ad Hoc Committees (Select & Joint Committees on Bills, Joint Parliamentary Committees - JPC),
and Consultative Committees.
"""
from typing import Dict, List, Optional, Any


def make_pc_q(
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
    source_ref: str = "Constitution of India (Articles 105, 118), Rules of Procedure and Conduct of Business in Lok Sabha & Rajya Sabha, TN Samacheer Kalvi, M. Laxmikanth"
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
        tags = ["polity", "parliamentary_committees", diff.lower(), subtopic.lower().replace(" ", "_")]

    return {
        "id": qid,
        "subject": "polity",
        "topic": "Parliamentary Committees",
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
