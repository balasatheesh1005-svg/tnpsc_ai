# -*- coding: utf-8 -*-
"""
Populate Grand Test 100 Questions for Supreme Court of India
"""

import json
import os
import random
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Import our builder functions or construct directly
def make_gt_100():
    qs = []

    def add(q_id, diff, q_type, q_en, q_ta, opts_en, opts_ta, correct, exp_en, exp_ta, trap_en, trap_ta, tip_en, tip_ta, fact_en, fact_ta):
        opts = []
        for k in ["A", "B", "C", "D"]:
            opts.append({"id": k, "en": opts_en[k], "ta": opts_ta[k]})
        
        wn = {}
        for k in ["A", "B", "C", "D"]:
            if k == correct:
                wn[k] = {"en": f"✅ Correct. {opts_en[k]} is constitutionally accurate.", "ta": f"✅ சரியானது. {opts_ta[k]} அரசியலமைப்பு ரீதியாக சரியானது."}
            else:
                wn[k] = {"en": f"❌ Incorrect option.", "ta": f"❌ தவறான தெரிவு."}

        qs.append({
            "id": q_id,
            "subject": "Polity",
            "topic": "Supreme Court of India",
            "difficulty": diff,
            "question_type": q_type,
            "question": {"en": q_en, "ta": q_ta},
            "question_en": q_en,
            "question_ta": q_ta,
            "options": opts,
            "options_en": opts_en,
            "options_ta": opts_ta,
            "correct_answer": correct,
            "explanation": {"en": exp_en, "ta": exp_ta},
            "explanation_en": exp_en,
            "explanation_ta": exp_ta,
            "why_not_others": wn,
            "trap_point": {"en": trap_en, "ta": trap_ta},
            "tnpsc_tip": {"en": tip_en, "ta": tip_ta},
            "high_yield_fact": {"en": fact_en, "ta": fact_ta},
            "source_reference": ["M. Laxmikanth – Indian Polity", "NCERT Class XI - Indian Constitution at Work"]
        })

    # Add 100 questions here
    return qs

if __name__ == "__main__":
    print("Populate module created.")
