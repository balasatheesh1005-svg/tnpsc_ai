import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

def q(q_id, diff, q_type, q_en, q_ta, ass_en, ass_ta, rea_en, rea_ta, opt_a_en, opt_a_ta, opt_b_en, opt_b_ta, opt_c_en, opt_c_ta, opt_d_en, opt_d_ta, ca, exp_en, exp_ta, wno_a_en, wno_a_ta, wno_b_en, wno_b_ta, wno_c_en, wno_c_ta, wno_d_en, wno_d_ta, tip_en, tip_ta, fact_en, fact_ta, src, sim="High", bloom="Analyze", time_sec=50):
    options = [
        {"id": "A", "en": opt_a_en, "ta": opt_a_ta},
        {"id": "B", "en": opt_b_en, "ta": opt_b_ta},
        {"id": "C", "en": opt_c_en, "ta": opt_c_ta},
        {"id": "D", "en": opt_d_en, "ta": opt_d_ta}
    ]
    options_en = [opt_a_en, opt_b_en, opt_c_en, opt_d_en]
    options_ta = [opt_a_ta, opt_b_ta, opt_c_ta, opt_d_ta]
    
    why_not_others = {
        "A": {"en": f"Correct. {wno_a_en}" if ca == "A" else f"Incorrect. {wno_a_en}", "ta": f"சரி. {wno_a_ta}" if ca == "A" else f"தவறு. {wno_a_ta}"},
        "B": {"en": f"Correct. {wno_b_en}" if ca == "B" else f"Incorrect. {wno_b_en}", "ta": f"சரி. {wno_b_ta}" if ca == "B" else f"தவறு. {wno_b_ta}"},
        "C": {"en": f"Correct. {wno_c_en}" if ca == "C" else f"Incorrect. {wno_c_en}", "ta": f"சரி. {wno_c_ta}" if ca == "C" else f"தவறு. {wno_c_ta}"},
        "D": {"en": f"Correct. {wno_d_en}" if ca == "D" else f"Incorrect. {wno_d_en}", "ta": f"சரி. {wno_d_ta}" if ca == "D" else f"தவறு. {wno_d_ta}"}
    }

    return {
        "id": q_id,
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": diff,
        "question_type": q_type,
        "question": {"en": q_en, "ta": q_ta},
        "assertion": {"en": ass_en, "ta": ass_ta} if ass_en else {},
        "reason": {"en": rea_en, "ta": rea_ta} if rea_en else {},
        "options": options,
        "correct_answer": ca,
        "explanation": {"en": exp_en, "ta": exp_ta},
        "why_not_others": why_not_others,
        "tnpsc_tip": {"en": tip_en, "ta": tip_ta},
        "revision_fact": {"en": fact_en, "ta": fact_ta},
        "source_reference": src,
        "bloom_level": bloom,
        "estimated_time_sec": time_sec,
        "pyq_similarity": sim,
        "tags": ["Polity", "Fundamental Duties", "Grand Test"],
        "question_en": q_en,
        "question_ta": q_ta,
        "options_en": options_en,
        "options_ta": options_ta,
        "answer": ca.lower(),
        "explanation_en": exp_en,
        "explanation_ta": exp_ta
    }

print("Loaded generator function.")
