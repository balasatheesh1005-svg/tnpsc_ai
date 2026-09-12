# -*- coding: utf-8 -*-
"""
Supreme Court Grand Test 100 Generator & Option Balancer
Generates data/questions/polity/supreme_court_grand_test.json
"""

import json
import os
import random
import sys

sys.stdout.reconfigure(encoding='utf-8')

from gt_sc_block1 import get_block1
from gt_sc_block2 import get_block2
from gt_sc_block3 import get_block3
from gt_sc_block4 import get_block4

def generate_and_balance_sc_gt_100():
    raw_qs = []
    raw_qs.extend(get_block1())
    raw_qs.extend(get_block2())
    raw_qs.extend(get_block3())
    raw_qs.extend(get_block4())

    print(f"Loaded {len(raw_qs)} raw MCQs.")

    # Target keys: 25 A, 25 B, 25 C, 25 D
    target_keys = ["A"] * 25 + ["B"] * 25 + ["C"] * 25 + ["D"] * 25
    random.seed(42)
    random.shuffle(target_keys)

    final_questions = []

    for i, item in enumerate(raw_qs):
        target_correct = target_keys[i]
        orig_correct = item["correct_key"]

        opts_en = dict(item["opts_en"])
        opts_ta = dict(item["opts_ta"])

        # If current correct != target_correct, swap them
        if orig_correct != target_correct:
            # Swap option text between orig_correct and target_correct
            opts_en[orig_correct], opts_en[target_correct] = opts_en[target_correct], opts_en[orig_correct]
            opts_ta[orig_correct], opts_ta[target_correct] = opts_ta[target_correct], opts_ta[orig_correct]

        # Construct options list
        options_list = []
        for k in ["A", "B", "C", "D"]:
            options_list.append({
                "id": k,
                "en": opts_en[k],
                "ta": opts_ta[k]
            })

        # Construct why_not_others
        why_not_others = {}
        for k in ["A", "B", "C", "D"]:
            if k == target_correct:
                why_not_others[k] = {
                    "en": f"✅ Correct. {opts_en[k]} is constitutionally accurate.",
                    "ta": f"✅ சரியானது. {opts_ta[k]} அரசியலமைப்பு ரீதியாக சரியானது."
                }
            else:
                why_not_others[k] = {
                    "en": f"❌ Incorrect. {opts_en[k]} is constitutionally inaccurate or incomplete.",
                    "ta": f"❌ தவறானது. {opts_ta[k]} அரசியலமைப்பு ரீதியாக தவறானது அல்லது முழுமையற்றது."
                }

        q_id = f"POLITY_SC_GT_{i+1:03d}"

        final_mcq = {
            "id": q_id,
            "subject": "Polity",
            "topic": "Supreme Court of India",
            "difficulty": item["difficulty"],
            "question_type": item["question_type"],
            "question": {
                "en": item["question_en"],
                "ta": item["question_ta"]
            },
            "question_en": item["question_en"],
            "question_ta": item["question_ta"],
            "options": options_list,
            "options_en": opts_en,
            "options_ta": opts_ta,
            "correct_answer": target_correct,
            "explanation": {
                "en": item["exp_en"],
                "ta": item["exp_ta"]
            },
            "explanation_en": item["exp_en"],
            "explanation_ta": item["exp_ta"],
            "why_not_others": why_not_others,
            "trap_point": {
                "en": item["trap_en"],
                "ta": item["trap_ta"]
            },
            "tnpsc_tip": {
                "en": item["tip_en"],
                "ta": item["tip_ta"]
            },
            "high_yield_fact": {
                "en": item["fact_en"],
                "ta": item["fact_ta"]
            },
            "source_reference": [
                "M. Laxmikanth – Indian Polity",
                "NCERT Class XI - Indian Constitution at Work"
            ]
        }

        final_questions.append(final_mcq)

    output_file = "data/questions/polity/supreme_court_grand_test.json"
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(final_questions, f, ensure_ascii=False, indent=2)

    print(f"Successfully generated and saved {len(final_questions)} MCQs to {output_file}")
    return final_questions

if __name__ == "__main__":
    generate_and_balance_sc_gt_100()
