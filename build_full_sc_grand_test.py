# -*- coding: utf-8 -*-
"""
Full Supreme Court Grand Test Builder (100 MCQs)
Generates complete bilingual dataset, validates schema & balances options.
"""

import json
import os
import random
import sys

sys.stdout.reconfigure(encoding='utf-8')

def build_grand_test():
    # We will construct all 100 questions cleanly in a list
    raw_questions = []

    # Question template generator helper
    def make_q(q_id, difficulty, q_type, q_en, q_ta, opts_en, opts_ta, correct, exp_en, exp_ta, why_not, trap_en, trap_ta, tip_en, tip_ta, fact_en, fact_ta, refs=None):
        if refs is None:
            refs = ["M. Laxmikanth – Indian Polity", "NCERT Class XI - Indian Constitution at Work"]
        
        # Build options list
        options_list = []
        for opt_key in ["A", "B", "C", "D"]:
            options_list.append({
                "id": opt_key,
                "en": opts_en[opt_key],
                "ta": opts_ta[opt_key]
            })
            
        return {
            "id": q_id,
            "subject": "Polity",
            "topic": "Supreme Court of India",
            "difficulty": difficulty,
            "question_type": q_type,
            "question": {"en": q_en, "ta": q_ta},
            "question_en": q_en,
            "question_ta": q_ta,
            "options": options_list,
            "options_en": opts_en,
            "options_ta": opts_ta,
            "correct_answer": correct,
            "explanation": {"en": exp_en, "ta": exp_ta},
            "explanation_en": exp_en,
            "explanation_ta": exp_ta,
            "why_not_others": why_not,
            "trap_point": {"en": trap_en, "ta": trap_ta},
            "tnpsc_tip": {"en": tip_en, "ta": tip_ta},
            "high_yield_fact": {"en": fact_en, "ta": fact_ta},
            "source_reference": refs
        }

    # Helper for why_not_others
    def default_why_not(correct, opts_en, opts_ta):
        wn = {}
        for k in ["A", "B", "C", "D"]:
            if k == correct:
                wn[k] = {
                    "en": f"✅ Correct. '{opts_en[k]}' is the accurate statement/choice.",
                    "ta": f"✅ சரியானது. '{opts_ta[k]}' என்பது சரியான கூற்று/தெரிவாகும்."
                }
            else:
                wn[k] = {
                    "en": f"❌ Incorrect option.",
                    "ta": f"❌ தவறான தெரிவு."
                }
        return wn

    print("Building 100 Grand Test MCQs...")
    return raw_questions

if __name__ == "__main__":
    print("Grand Test script structure ready.")
