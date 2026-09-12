# -*- coding: utf-8 -*-
"""
Generator for Governor Part 1 Datasets (150 Questions)
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

EASY_PATH = r"data/questions/polity/governor_easy.json"
MEDIUM_PATH = r"data/questions/polity/governor_medium.json"
HARD_PATH = r"data/questions/polity/governor_hard.json"

def q(qid, diff, qtype, q_en, q_ta, opts_en, opts_ta, corr_idx, exp_en, exp_ta, wno, tip_en, tip_ta, fact_en, fact_ta, bloom="Understand", time_sec=60, pyq="Standard", tags=None):
    corr_letter = ["A", "B", "C", "D"][corr_idx]
    corr_lower = ["a", "b", "c", "d"][corr_idx]
    if tags is None:
        tags = ["Governor", "Polity", "State Executive", "Part VI"]

    return {
        "id": qid,
        "subject": "Polity",
        "topic": "Governor of a State",
        "difficulty": diff,
        "question_type": qtype,
        "question": {"en": q_en, "ta": q_ta},
        "question_en": q_en,
        "question_ta": q_ta,
        "options": [
            {"id": "A", "en": opts_en[0], "ta": opts_ta[0]},
            {"id": "B", "en": opts_en[1], "ta": opts_ta[1]},
            {"id": "C", "en": opts_en[2], "ta": opts_ta[2]},
            {"id": "D", "en": opts_en[3], "ta": opts_ta[3]}
        ],
        "options_en": opts_en,
        "options_ta": opts_ta,
        "correct_answer": corr_letter,
        "answer": corr_lower,
        "explanation": {"en": exp_en, "ta": exp_ta},
        "explanation_en": exp_en,
        "explanation_ta": exp_ta,
        "why_not_others": {
            "A": {"en": wno["A"]["en"], "ta": wno["A"]["ta"]},
            "B": {"en": wno["B"]["en"], "ta": wno["B"]["ta"]},
            "C": {"en": wno["C"]["en"], "ta": wno["C"]["ta"]},
            "D": {"en": wno["D"]["en"], "ta": wno["D"]["ta"]}
        },
        "distractor_analysis": {
            k: {
                "status": "Correct" if k == corr_letter else "Incorrect",
                "explanation_english": wno[k]["en"],
                "explanation_tamil": wno[k]["ta"]
            } for k in ["A", "B", "C", "D"]
        },
        "tnpsc_tip": {"en": tip_en, "ta": tip_ta},
        "tnpsc_expert_tip": f"{tip_en} / {tip_ta}",
        "revision_fact": {"en": fact_en, "ta": fact_ta},
        "high_yield_fact": f"{fact_en} / {fact_ta}",
        "source_reference": ["M. Laxmikanth – Indian Polity", "Samacheer Kalvi Class 12 Political Science"],
        "bloom_level": bloom,
        "estimated_time_sec": time_sec,
        "pyq_similarity": pyq,
        "tags": tags
    }

print("Base setup ready.")
