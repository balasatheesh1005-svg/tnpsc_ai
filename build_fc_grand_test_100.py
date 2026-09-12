# -*- coding: utf-8 -*-
"""
Build 100 Grand Test MCQs for Finance Commission of India
ID range: FC_GT_001 to FC_GT_100
Strict requirements:
- Exactly 25 A, 25 B, 25 C, 25 D
- 0 stem collision with Core 325 questions
- 0 internal collisions
- 100% 24-field schema compliance
- Certified by ContentValidator
"""

import json
import os
from build_fc_gt_part1 import raw_gt_p1
from build_fc_gt_part2 import raw_gt_p2
from fc_mcq_helper import make_fc_q
from rebalance_er_helper import balance_question_keys
from tools.nova_content_engine.validator import ContentValidator

def convert_raw_items_to_questions():
    all_raw = []
    for item in raw_gt_p1:
        all_raw.append(item)
    for item in raw_gt_p2:
        all_raw.append(item)
        
    questions = []
    for idx, item in enumerate(all_raw, start=1):
        qid = f"FC_GT_{idx:03d}"
        key = item["key"].upper()
        
        opt_map = {
            "A": item["a"],
            "B": item["b"],
            "C": item["c"],
            "D": item["d"]
        }
        
        why_en = {}
        why_ta = {}
        for k in ["A", "B", "C", "D"]:
            opt = opt_map[k]
            if k == key:
                why_en[k] = f"Option {k} is correct: {item['exp_en']}"
                why_ta[k] = f"தெரிவு {k} சரி: {item['exp_ta']}"
            else:
                why_en[k] = f"Option {k} ({opt[0]}) is incorrect in this constitutional context."
                why_ta[k] = f"தெரிவு {k} ({opt[1]}) இந்த அரசியலமைப்புச் சூழலில் தவறானதாகும்."
                
        q = make_fc_q(
            qid=qid,
            diff="Hard",
            qtype="Single Choice",
            subtopic=item["subtopic"],
            en_stem=item["en_stem"],
            ta_stem=item["ta_stem"],
            en_a=opt_map["A"][0], ta_a=opt_map["A"][1],
            en_b=opt_map["B"][0], ta_b=opt_map["B"][1],
            en_c=opt_map["C"][0], ta_c=opt_map["C"][1],
            en_d=opt_map["D"][0], ta_d=opt_map["D"][1],
            correct_key=key,
            exp_en=item["exp_en"],
            exp_ta=item["exp_ta"],
            why_a_en=why_en["A"], why_a_ta=why_ta["A"],
            why_b_en=why_en["B"], why_b_ta=why_ta["B"],
            why_c_en=why_en["C"], why_c_ta=why_ta["C"],
            why_d_en=why_en["D"], why_d_ta=why_ta["D"],
            tip_en=item["tip_en"],
            tip_ta=item["tip_ta"],
            fact_en=item["fact_en"],
            fact_ta=item["fact_ta"],
            tags=["polity", "finance_commission", "grand_test", item["subtopic"].lower().replace(" ", "_")],
            bloom="Evaluate",
            time_sec=75,
            pyq_sim="High"
        )
        questions.append(q)
    return questions

def build_grand_test():
    combined = convert_raw_items_to_questions()
    assert len(combined) == 100, f"Expected 100 questions, got {len(combined)}"
    
    # Load all core stems
    core_files = [
        "data/questions/polity/fc_easy.json",
        "data/questions/polity/fc_medium.json",
        "data/questions/polity/fc_hard.json",
        "data/questions/polity/fc_statement_based.json",
        "data/questions/polity/fc_reasoning.json",
        "data/questions/polity/fc_chronology.json",
        "data/questions/polity/fc_match_the_following.json",
        "data/questions/polity/fc_pyq.json"
    ]
    core_stems = {}
    for cf in core_files:
        with open(cf, "r", encoding="utf-8") as f:
            cdata = json.load(f)
        for cq in cdata:
            cstem = cq.get("question_en", "").strip().lower()
            core_stems[cstem] = cq.get("id")
            
    print(f"Loaded {len(core_stems)} unique Core stems.")
    
    # Check for collisions with core or internal collisions
    gt_stems = {}
    for q in combined:
        stem = q.get("question_en", "").strip().lower()
        qid = q.get("id")
        if stem in core_stems:
            raise ValueError(f"Grand Test question {qid} collides with Core question {core_stems[stem]}: {stem[:60]}...")
        if stem in gt_stems:
            raise ValueError(f"Grand Test question {qid} collides internally with {gt_stems[stem]}: {stem[:60]}...")
        gt_stems[stem] = qid
        
    print("Grand Test collision audit: 100% PASS! 0 Core collisions, 0 internal collisions.")
    
    # Exactly balance keys: 25 A, 25 B, 25 C, 25 D
    target_counts = {"A": 25, "B": 25, "C": 25, "D": 25}
    balanced_qs = balance_question_keys(combined, target_counts=target_counts)
        
    # Verify counts
    key_counts = {}
    for q in balanced_qs:
        k = q["correct_answer"]
        key_counts[k] = key_counts.get(k, 0) + 1
    print(f"Grand Test key distribution: {key_counts}")
    assert key_counts == {"A": 25, "B": 25, "C": 25, "D": 25}, f"Distribution mismatch: {key_counts}"
    
    return balanced_qs

if __name__ == "__main__":
    gt_qs = build_grand_test()
    out_path = os.path.join("data", "questions", "polity", "fc_grand_test.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(gt_qs, f, ensure_ascii=False, indent=2)
    print(f"Saved 100 Grand Test MCQs to {out_path}")
    
    val = ContentValidator()
    report = val.validate_file(out_path, expected_count=100, expected_prefix="FC_GT_")
    print(f"Validation Report: {'PASS' if report.is_valid else 'FAIL'} | Total: {report.total_audited}")
    if not report.is_valid:
        for iss in report.issues[:10]:
            print(f"  Issue: {iss}")
    print(f"Key Distribution: {report.key_distribution}")
