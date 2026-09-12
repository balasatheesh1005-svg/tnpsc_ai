# -*- coding: utf-8 -*-
"""
Generator Script for Citizenship of India MCQ Repository
Generates 425 bilingual MCQs across 9 dataset files:
- Easy: 50
- Medium: 50
- Hard: 50
- Statement: 50
- Reasoning: 25
- Match the Following: 25
- Chronology: 25
- PYQ: 50
- Grand Test: 100
Total = 425 questions.
"""

import json
import os
import random
import sys

sys.stdout.reconfigure(encoding='utf-8')

OUT_DIR = "data/questions/polity"
os.makedirs(OUT_DIR, exist_ok=True)

def make_options(en_a, ta_a, en_b, ta_b, en_c, ta_c, en_d, ta_d):
    return [
        {"id": "A", "en": en_a, "ta": ta_a},
        {"id": "B", "en": en_b, "ta": ta_b},
        {"id": "C", "en": en_c, "ta": ta_c},
        {"id": "D", "en": en_d, "ta": ta_d}
    ]

def make_why_not(correct_letter, exp_a_en, exp_a_ta, exp_b_en, exp_b_ta, exp_c_en, exp_c_ta, exp_d_en, exp_d_ta):
    return {
        "A": {"en": exp_a_en, "ta": exp_a_ta},
        "B": {"en": exp_b_en, "ta": exp_b_ta},
        "C": {"en": exp_c_en, "ta": exp_c_ta},
        "D": {"en": exp_d_en, "ta": exp_d_ta}
    }

def build_q(qid, difficulty, qtype, stem_en, stem_ta, options, correct_letter, exp_en, exp_ta, why_not, tip_en, tip_ta, rev_en, rev_ta, sources, bloom="Remember", time_sec=60, pyq_sim="High", tags=None):
    if tags is None:
        tags = ["Polity", "Citizenship of India"]
    
    answer_lower = correct_letter.lower()
    opts_en = [o["en"] for o in options]
    opts_ta = [o["ta"] for o in options]

    return {
        "id": qid,
        "subject": "Polity",
        "topic": "Citizenship of India",
        "difficulty": difficulty,
        "question_type": qtype,
        "question": {"en": stem_en, "ta": stem_ta},
        "options": options,
        "correct_answer": correct_letter,
        "explanation": {"en": exp_en, "ta": exp_ta},
        "why_not_others": why_not,
        "tnpsc_tip": {"en": tip_en, "ta": tip_ta},
        "revision_fact": {"en": rev_en, "ta": rev_ta},
        "source_reference": sources if isinstance(sources, list) else [sources],
        "bloom_level": bloom,
        "estimated_time_sec": time_sec,
        "pyq_similarity": pyq_sim,
        "tags": tags,
        "question_en": stem_en,
        "question_ta": stem_ta,
        "options_en": opts_en,
        "options_ta": opts_ta,
        "answer": answer_lower,
        "explanation_en": exp_en,
        "explanation_ta": exp_ta
    }

def balance_and_shuffle_answers(questions, seed=42):
    """
    Ensures that correct_answer is evenly distributed among A, B, C, D.
    """
    n = len(questions)
    letters = ["A", "B", "C", "D"]
    base = n // 4
    rem = n % 4
    counts = [base + (1 if i < rem else 0) for i in range(4)]
    target_letters = []
    for l, c in zip(letters, counts):
        target_letters.extend([l] * c)
    random.seed(seed)
    random.shuffle(target_letters)

    balanced_qs = []
    for i, q in enumerate(questions):
        desired = target_letters[i]
        curr = q["correct_answer"]
        if curr != desired:
            curr_idx = ord(curr) - ord('A')
            des_idx = ord(desired) - ord('A')
            
            # Swap options text
            q["options"][curr_idx]["en"], q["options"][des_idx]["en"] = q["options"][des_idx]["en"], q["options"][curr_idx]["en"]
            q["options"][curr_idx]["ta"], q["options"][des_idx]["ta"] = q["options"][des_idx]["ta"], q["options"][curr_idx]["ta"]
            
            # Swap why_not_others
            q["why_not_others"][curr], q["why_not_others"][desired] = q["why_not_others"][desired], q["why_not_others"][curr]
            
            q["correct_answer"] = desired
            q["answer"] = desired.lower()
            q["options_en"] = [o["en"] for o in q["options"]]
            q["options_ta"] = [o["ta"] for o in q["options"]]
        balanced_qs.append(q)
    return balanced_qs

print("Generator helper base loaded.")
