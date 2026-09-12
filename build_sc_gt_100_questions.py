# -*- coding: utf-8 -*-
"""
Full Generator for Supreme Court Grand Test (100 Questions)
"""

import json
import os
import random
import sys

sys.stdout.reconfigure(encoding='utf-8')

def create_100_mcqs():
    # We will generate 100 questions covering all target topics
    # with balanced options A, B, C, D (25 each)
    
    questions = []
    
    def add_mcq(q_id, diff, q_type, q_en, q_ta, opts_en, opts_ta, correct, exp_en, exp_ta, trap_en, trap_ta, tip_en, tip_ta, fact_en, fact_ta):
        opts = []
        for k in ["A", "B", "C", "D"]:
            opts.append({"id": k, "en": opts_en[k], "ta": opts_ta[k]})
        
        wn = {}
        for k in ["A", "B", "C", "D"]:
            if k == correct:
                wn[k] = {"en": f"✅ Correct. {opts_en[k]} is constitutionally accurate.", "ta": f"✅ சரியானது. {opts_ta[k]} அரசியலமைப்பு ரீதியாக சரியானது."}
            else:
                wn[k] = {"en": f"❌ Incorrect option.", "ta": f"❌ தவறான தெரிவு."}

        questions.append({
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

    print("Building 100 Grand Test Questions...")
    
    # We will write the full data dictionary for 100 questions here
    return questions

if __name__ == "__main__":
    qs = create_100_mcqs()
    print("Skeleton initialized.")
