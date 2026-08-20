# -*- coding: utf-8 -*-
"""
Master Builder for 100 TNPSC Group 1 Standard Grand Test MCQs
Topic: Preamble of the Constitution of India
Target: data/questions/polity/preamble_grand_test.json
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# We will construct all 100 questions
questions_list = []

def make_q(idx, qtype, diff, ans, q_en, q_ta, opts, exp_en, exp_ta, tip_en=None, tip_ta=None, fact_en=None, fact_ta=None, list1=None, list2=None, events=None):
    q_id = f"PRE_GT_{idx:03d}"
    
    why_not = {}
    for o in opts:
        okey = o["id"]
        if okey == ans:
            why_not[okey] = {
                "en": f"Correct. {o['en']} is the correct answer.",
                "ta": f"சரி. {o['ta']} என்பது சரியான விடையாகும்."
            }
        else:
            why_not[okey] = {
                "en": f"Incorrect. {o['en']} is not the correct choice.",
                "ta": f"தவறு. {o['ta']} என்பது சரியான தேர்வு அல்ல."
            }
            
    q_obj = {
        "id": q_id,
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": diff,
        "question_type": qtype,
        "question": {"en": q_en, "ta": q_ta},
        "options": opts,
        "correct_answer": ans,
        "explanation": {"en": exp_en, "ta": exp_ta},
        "why_not_others": why_not,
        "tnpsc_tip": {
            "en": tip_en or "Focus on constitutional principles, case law evolution, and accurate keyword sequences.",
            "ta": tip_ta or "அரசியலமைப்பு விதிகள், வழக்கு தீர்ப்புகள் மற்றும் சொற்களின் சரியான வரிசையில் கவனம் செலுத்துங்கள்."
        },
        "revision_fact": {
            "en": fact_en or "The Preamble encapsulates the philosophy and fundamental objectives of the Indian Constitution.",
            "ta": fact_ta or "முகவுரை இந்திய அரசியலமைப்பின் தத்துவம் மற்றும் அடிப்படைக் குறிக்கோள்களைத் தன்னுள் கொண்டுள்ளது."
        },
        "source_reference": ["M. Laxmikanth - Indian Polity", "NCERT Class XI - Indian Constitution at Work", "TNPSC Grand Test Series"],
        "bloom_level": "Understand" if diff == "Easy" else ("Analyze" if diff == "Hard" else "Apply"),
        "estimated_time_sec": 45 if diff == "Easy" else (75 if diff == "Hard" else 60),
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "Grand Test", "TNPSC Group 1"],
        
        # Flat legacy fields
        "question_en": q_en,
        "question_ta": q_ta,
        "options_en": [o["en"] for o in opts],
        "options_ta": [o["ta"] for o in opts],
        "answer": ans.lower(),
        "explanation_en": exp_en,
        "explanation_ta": exp_ta
    }
    
    if list1 and list2:
        q_obj["list_1"] = list1
        q_obj["list_2"] = list2
    if events:
        q_obj["events"] = events
        
    return q_obj

print("Initializing 100 Grand Test questions compilation...")
