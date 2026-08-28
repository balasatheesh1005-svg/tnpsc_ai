# -*- coding: utf-8 -*-
"""
Helper functions for generating TNPSC Prime Minister MCQs with strict quality standards.
"""

def make_options(en_a, ta_a, en_b, ta_b, en_c, ta_c, en_d, ta_d):
    return [
        {"id": "A", "en": en_a, "ta": ta_a},
        {"id": "B", "en": en_b, "ta": ta_b},
        {"id": "C", "en": en_c, "ta": ta_c},
        {"id": "D", "en": en_d, "ta": ta_d}
    ]

def make_distractor(correct_letter, *args):
    """
    Supports:
    - 8 positional args: exp_a_en, exp_a_ta, exp_b_en, exp_b_ta, exp_c_en, exp_c_ta, exp_d_en, exp_d_ta
    - 12 positional args: exp_a_en, exp_a_ta, trap_a, exp_b_en, exp_b_ta, trap_b, ...
    """
    if len(args) == 8:
        exp_a_en, exp_a_ta, exp_b_en, exp_b_ta, exp_c_en, exp_c_ta, exp_d_en, exp_d_ta = args
        trap_a = "Correct constitutional provision" if correct_letter == "A" else "Common distractor / misconception"
        trap_b = "Correct constitutional provision" if correct_letter == "B" else "Common distractor / misconception"
        trap_c = "Correct constitutional provision" if correct_letter == "C" else "Common distractor / misconception"
        trap_d = "Correct constitutional provision" if correct_letter == "D" else "Common distractor / misconception"
    elif len(args) == 12:
        exp_a_en, exp_a_ta, trap_a, exp_b_en, exp_b_ta, trap_b, exp_c_en, exp_c_ta, trap_c, exp_d_en, exp_d_ta, trap_d = args
    else:
        raise ValueError(f"make_distractor expects 8 or 12 positional arguments after correct_letter, got {len(args)}")

    analysis = {
        "A": {
            "status": "CORRECT" if correct_letter == "A" else "INCORRECT",
            "explanation_english": exp_a_en,
            "explanation_tamil": exp_a_ta,
            "trap": trap_a
        },
        "B": {
            "status": "CORRECT" if correct_letter == "B" else "INCORRECT",
            "explanation_english": exp_b_en,
            "explanation_tamil": exp_b_ta,
            "trap": trap_b
        },
        "C": {
            "status": "CORRECT" if correct_letter == "C" else "INCORRECT",
            "explanation_english": exp_c_en,
            "explanation_tamil": exp_c_ta,
            "trap": trap_c
        },
        "D": {
            "status": "CORRECT" if correct_letter == "D" else "INCORRECT",
            "explanation_english": exp_d_en,
            "explanation_tamil": exp_d_ta,
            "trap": trap_d
        }
    }
    
    why_not = {
        "A": {"en": exp_a_en, "ta": exp_a_ta},
        "B": {"en": exp_b_en, "ta": exp_b_ta},
        "C": {"en": exp_c_en, "ta": exp_c_ta},
        "D": {"en": exp_d_en, "ta": exp_d_ta}
    }
    
    return analysis, why_not

def build_q(qid, difficulty, qtype,
            stem_en, stem_ta,
            options, correct_answer,
            exp_en, exp_ta,
            distractor_tuple,
            tip_en, tip_ta,
            arg13=None, arg14=None, arg15=None, arg16=None, arg17=None):
    
    distractor_analysis, why_not_others = distractor_tuple
    
    opts_en = [o["en"] for o in options]
    opts_ta = [o["ta"] for o in options]

    # Handle variable argument counts gracefully
    if arg17 is not None:
        hy_en, hy_ta, trap_en, trap_ta, sources = arg13, arg14, arg15, arg16, arg17
    elif arg15 is not None and isinstance(arg15, list):
        # 15 args passed: tip_en, tip_ta, trap_en, trap_ta, sources
        trap_en, trap_ta, sources = arg13, arg14, arg15
        hy_en = f"High-Yield Fact: {exp_en}"
        hy_ta = f"முக்கியக் குறிப்பு: {exp_ta}"
    elif arg13 is not None:
        hy_en = arg13 if isinstance(arg13, str) else f"High-Yield Fact: {exp_en}"
        hy_ta = arg14 if isinstance(arg14, str) else f"முக்கியக் குறிப்பு: {exp_ta}"
        trap_en = "Confusing constitutional provisions"
        trap_ta = "அரசியலமைப்பு விதிகளைக் குழப்பிக் கொள்ளுதல்"
        sources = ["Prime Minister Notes"]
    else:
        hy_en = f"High-Yield Fact: {exp_en}"
        hy_ta = f"முக்கியக் குறிப்பு: {exp_ta}"
        trap_en = "Confusing constitutional provisions"
        trap_ta = "அரசியலமைப்பு விதிகளைக் குழப்பிக் கொள்ளுதல்"
        sources = ["Prime Minister Notes"]
    
    return {
        "id": qid,
        "question_id": qid,
        "subject": "Indian Polity",
        "topic": "Prime Minister of India",
        "difficulty": difficulty,
        "question_type": qtype,
        "question": {
            "en": stem_en,
            "ta": stem_ta
        },
        "question_en": stem_en,
        "question_ta": stem_ta,
        "options": options,
        "options_en": opts_en,
        "options_ta": opts_ta,
        "correct_answer": correct_answer,
        "answer": correct_answer,
        "explanation": {
            "en": exp_en,
            "ta": exp_ta
        },
        "explanation_en": exp_en,
        "explanation_ta": exp_ta,
        "distractor_analysis": distractor_analysis,
        "why_not_others": why_not_others,
        "tnpsc_expert_tip": {
            "en": tip_en,
            "ta": tip_ta
        },
        "tnpsc_tip": {
            "en": tip_en,
            "ta": tip_ta
        },
        "high_yield_revision_fact": {
            "en": hy_en,
            "ta": hy_ta
        },
        "high_yield_fact": {
            "en": hy_en,
            "ta": hy_ta
        },
        "trap_point": {
            "en": trap_en,
            "ta": trap_ta
        },
        "source_reference": sources if isinstance(sources, list) else [sources],
        "tags": ["Polity", "Prime Minister", "TNPSC Group 1"],
        "metadata": {
            "bloom_level": "Understand" if difficulty == "Easy" else ("Apply" if difficulty in ["Medium", "Statement"] else "Analyze"),
            "estimated_time_sec": 60 if difficulty == "Easy" else (90 if difficulty in ["Medium", "Statement"] else 120),
            "pyq_similarity": "High"
        }
    }
