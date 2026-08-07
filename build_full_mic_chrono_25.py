import json
import sys
from pathlib import Path

target_path = Path(r"c:\Users\Home\Desktop\tnpsc_ai\data\questions\polity\making_of_indian_constitution_chronology.json")
target_path.parent.mkdir(parents=True, exist_ok=True)

def make_chrono_q(q_id, q_type, q_en, q_ta, events_en, events_ta,
                  opt_a, opt_b, opt_c, opt_d, correct_ans, exp_en, exp_ta,
                  wno_a_en, wno_a_ta, wno_b_en, wno_b_ta, wno_c_en, wno_c_ta, wno_d_en, wno_d_ta,
                  tip_en, tip_ta, rev_en, rev_ta, bloom, est_time, tags):
    opts = [
        {"id": "A", "en": opt_a, "ta": opt_a},
        {"id": "B", "en": opt_b, "ta": opt_b},
        {"id": "C", "en": opt_c, "ta": opt_c},
        {"id": "D", "en": opt_d, "ta": opt_d}
    ]
    opts_en = [opt_a, opt_b, opt_c, opt_d]
    opts_ta = [opt_a, opt_b, opt_c, opt_d]
    
    events_objs = [{"id": str(i+1), "en": events_en[i], "ta": events_ta[i]} for i in range(len(events_en))]

    return {
        "id": q_id,
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Hard",
        "question_type": "Chronology",
        "question": {"en": q_en, "ta": q_ta},
        "events": events_objs,
        "options": opts,
        "correct_answer": correct_ans,
        "explanation": {"en": exp_en, "ta": exp_ta},
        "why_not_others": {
            "A": {"en": wno_a_en, "ta": wno_a_ta},
            "B": {"en": wno_b_en, "ta": wno_b_ta},
            "C": {"en": wno_c_en, "ta": wno_c_ta},
            "D": {"en": wno_d_en, "ta": wno_d_ta}
        },
        "tnpsc_tip": {"en": tip_en, "ta": tip_ta},
        "revision_fact": {"en": rev_en, "ta": rev_ta},
        "source_reference": ["M. Laxmikanth - Indian Polity", "NCERT Class 11 - Indian Constitution at Work", "Constituent Assembly Debates"],
        "bloom_level": bloom,
        "estimated_time_sec": est_time,
        "pyq_similarity": "High",
        "tags": tags,
        "question_en": q_en,
        "question_ta": q_ta,
        "options_en": opts_en,
        "options_ta": opts_ta,
        "answer": correct_ans.lower(),
        "explanation_en": exp_en,
        "explanation_ta": exp_ta
    }

questions = []

print("Chronology builder helper created.")
