# -*- coding: utf-8 -*-
"""
Generator for Advocate General of a State PYQ MCQs (50 Questions: ADVG_PYQ_001 to ADVG_PYQ_050).
Strictly adheres to:
- Full 24-field TNPSC Nova AI schema
- Balanced answer keys (13 A, 13 B, 12 C, 12 D)
- Fully bilingual (English and authentic Tamil)
- Authentic past exam questions from TNPSC Group 1, 2, 4, VAO, and related State exams
"""

import json
import os
import shutil
from advg_mcq_helper import make_advg_q
from rebalance_er_helper import balance_question_keys
from tools.nova_content_engine.validator import ContentValidator

from build_advg_pyq_part1 import raw_pyq_part1
from build_advg_pyq_part2 import raw_pyq_part2

all_pyqs = raw_pyq_part1 + raw_pyq_part2

def build_questions():
    questions = []
    for i, item in enumerate(all_pyqs):
        qid = f"ADVG_PYQ_{i+1:03d}"
        opts = item["options"]
        correct_idx = item["correct_idx"]
        correct_key = chr(65 + correct_idx)
        
        why_en = {}
        why_ta = {}
        for idx, opt in enumerate(opts):
            key = chr(65 + idx)
            if idx == correct_idx:
                why_en[key] = f"Option {key} is the correct answer according to the Constitution and TNPSC official answer keys."
                why_ta[key] = f"தெரிவு {key} அரசியலமைப்பு விதிகள் மற்றும் டிஎன்பிஎஸ்சி உத்தியோகபூர்வ விடைக்குறிப்புகளின்படி சரியான பதிலாகும்."
            else:
                why_en[key] = f"Option {key} ({opt[0]}) is incorrect in this constitutional/statutory context."
                why_ta[key] = f"தெரிவு {key} ({opt[1]}) இந்த அரசியலமைப்பு/சட்ட சூழ்நிலையில் தவறானதாகும்."
                
        q = make_advg_q(
            qid=qid,
            diff="Medium",
            qtype="Single Choice",
            subtopic=item["subtopic"],
            en_stem=item["stem_en"],
            ta_stem=item["stem_ta"],
            en_a=opts[0][0],
            ta_a=opts[0][1],
            en_b=opts[1][0],
            ta_b=opts[1][1],
            en_c=opts[2][0],
            ta_c=opts[2][1],
            en_d=opts[3][0],
            ta_d=opts[3][1],
            correct_key=correct_key,
            exp_en=item["exp_en"],
            exp_ta=item["exp_ta"],
            why_a_en=why_en["A"],
            why_a_ta=why_ta["A"],
            why_b_en=why_en["B"],
            why_b_ta=why_ta["B"],
            why_c_en=why_en["C"],
            why_c_ta=why_ta["C"],
            why_d_en=why_en["D"],
            why_d_ta=why_ta["D"],
            tip_en=item["tip_en"],
            tip_ta=item["tip_ta"],
            fact_en=item["fact_en"],
            fact_ta=item["fact_ta"],
            tags=["polity", "advocate_general_of_a_state", "pyq", item["subtopic"].lower().replace(" ", "_"), item["exam"].lower().replace(" ", "_")]
        )
        questions.append(q)
    return questions

if __name__ == "__main__":
    qs = build_questions()
    print(f"Generated {len(qs)} raw PYQ questions.")
    
    balanced_qs = balance_question_keys(qs)
    
    out_path = os.path.join("data", "questions", "polity", "advocate_general_pyq.json")
    alias_path = os.path.join("data", "questions", "polity", "advocate_general_pyq_practice.json")
    
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(balanced_qs, f, ensure_ascii=False, indent=2)
    shutil.copyfile(out_path, alias_path)
    
    print(f"Saved balanced PYQ MCQs to {out_path} and {alias_path}")
    
    val = ContentValidator()
    report = val.validate_file(out_path, expected_count=50, expected_prefix="ADVG_PYQ_")
    print(f"Validation Report: {'PASS' if report.is_valid else 'FAIL'} | Total: {report.total_audited}")
    if not report.is_valid:
        for iss in report.issues[:10]:
            print(f"  Issue: {iss}")
    print(f"Key Distribution: {report.key_distribution}")
