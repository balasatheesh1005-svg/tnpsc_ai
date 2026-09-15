# -*- coding: utf-8 -*-
"""
Official Language - Part 3: Grand Test (100 MCQs)
TNPSC Nova AI Content Engine

Assembles 100 comprehensive Grand Test questions covering Articles 343-351,
Eighth Schedule, Classical Languages, and Statutory Enactments.
Ensures:
- 0 stem duplicates against all 325 Core questions
- Exact 25/25/25/25 answer key distribution with no consecutive runs > 2
- 24-field bilingual schema compliance
"""
import os
import json
from collections import Counter
from typing import List, Dict, Any

from tools.nova_content_engine.duplicate_index import TopicDuplicateIndex
from tools.nova_content_engine.answer_randomizer import randomize_and_balance_dataset
from tools.nova_content_engine.validator import ContentValidator
from official_language_mcq_helper import make_ol_q
from ol_gt_batch1 import get_gt_batch1
from ol_gt_batch2 import get_gt_batch2


def build_grand_test_file():
    b1 = get_gt_batch1()
    b2 = get_gt_batch2()
    all_raw = b1 + b2
    print(f"Loaded {len(all_raw)} raw Grand Test questions ({len(b1)} batch1 + {len(b2)} batch2).")
    assert len(all_raw) == 100, f"Expected 100 items, got {len(all_raw)}"

    # 1. Verify 0 duplicate collisions against Core 325 questions
    core_files = [
        "data/questions/polity/official_language_easy.json",
        "data/questions/polity/official_language_medium.json",
        "data/questions/polity/official_language_hard.json",
        "data/questions/polity/official_language_statement_based.json",
        "data/questions/polity/official_language_pyq.json",
        "data/questions/polity/official_language_reasoning.json",
        "data/questions/polity/official_language_match_the_following.json",
        "data/questions/polity/official_language_chronology.json",
    ]
    dup_idx = TopicDuplicateIndex("polity_official_language")
    loaded = dup_idx.load_from_files(core_files)
    print(f"Loaded {loaded} Core questions into Duplicate Index.")

    dups = []
    for i, item in enumerate(all_raw, start=1):
        is_dup, reason = dup_idx.check_duplicate(item["stem_en"], item["stem_ta"])
        if is_dup:
            dups.append((i, item["stem_en"][:60], reason))
    if dups:
        print(f"CRITICAL: Found {len(dups)} collisions with Core questions!")
        for d in dups:
            print(f"  Item {d[0]}: {d[1]} -> {d[2]}")
        raise ValueError(f"Found {len(dups)} duplicate collisions with Core questions.")
    print("Zero duplicate collisions with Core questions: PASS")

    # 2. Build 24-field Question Objects
    questions = []
    for idx, item in enumerate(all_raw, start=1):
        qid = f"OL_GT_{idx:03d}"
        if idx <= 30:
            diff = "Easy"
        elif idx <= 70:
            diff = "Medium"
        else:
            diff = "Hard"

        opts = item["options"]
        correct_key = item["correct_key"]

        q = make_ol_q(
            qid=qid,
            diff=diff,
            qtype="Direct MCQ",
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
            why_a_en=item["why_a_en"],
            why_a_ta=item["why_a_ta"],
            why_b_en=item["why_b_en"],
            why_b_ta=item["why_b_ta"],
            why_c_en=item["why_c_en"],
            why_c_ta=item["why_c_ta"],
            why_d_en=item["why_d_en"],
            why_d_ta=item["why_d_ta"],
            tip_en=item["tip_en"],
            tip_ta=item["tip_ta"],
            fact_en=item["fact_en"],
            fact_ta=item["fact_ta"],
            tags=["polity", "official_language", "grand_test", item["subtopic"].lower().replace(" ", "_")]
        )
        questions.append(q)

    # 3. Apply Answer Key Randomizer (Exact 25 each: A, B, C, D)
    balanced = randomize_and_balance_dataset(questions, seed=101)
    key_dist = Counter(q["correct_answer"] for q in balanced)
    print(f"Balanced Grand Test Key Distribution: {dict(key_dist)}")

    out_dir = os.path.join("data", "questions", "polity")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "official_language_grand_test.json")

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)
    print(f"Saved balanced Grand Test MCQs to {out_path}")

    # 4. ContentValidator verification
    rep = ContentValidator.validate_file(out_path, expected_count=100, expected_prefix="OL_GT_")
    print(f"Validation: {'PASS' if rep.is_valid else 'FAIL'} | Total: {rep.total_audited}")
    print(f"Keys: {rep.key_distribution}")
    print(f"Difficulties: {rep.difficulty_distribution}")
    if not rep.is_valid:
        for iss in rep.issues:
            print("  Issue:", iss.severity, iss.field_name, iss.message)
    return rep.is_valid


if __name__ == "__main__":
    success = build_grand_test_file()
    if not success:
        exit(1)
