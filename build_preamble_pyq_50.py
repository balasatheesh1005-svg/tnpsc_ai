# -*- coding: utf-8 -*-
"""
Builder script for 50 TNPSC Group 1 Standard PYQ Practice MCQs
Topic: Preamble of the Constitution of India
Target Files:
  - data/questions/polity/preamble_pyq.json
  - data/questions/polity/preamble_pyq_practice.json
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# We will construct 50 distinct PYQ / PYQ-Pattern questions
questions = []

def add_q(q_dict):
    idx = len(questions) + 1
    q_dict["id"] = f"PRE_PYQ_{idx:03d}"
    q_dict["subject"] = "Polity"
    q_dict["topic"] = "Preamble of the Constitution of India"
    q_dict["answer"] = q_dict["correct_answer"].lower()
    
    # Ensure flat fields present
    q_dict["question_en"] = q_dict["question"]["en"]
    q_dict["question_ta"] = q_dict["question"]["ta"]
    q_dict["options_en"] = [opt["en"] for opt in q_dict["options"]]
    q_dict["options_ta"] = [opt["ta"] for opt in q_dict["options"]]
    q_dict["explanation_en"] = q_dict["explanation"]["en"]
    q_dict["explanation_ta"] = q_dict["explanation"]["ta"]
    
    questions.append(q_dict)

print("Starting build of 50 PYQ Practice MCQs...")
