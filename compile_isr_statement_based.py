# -*- coding: utf-8 -*-
"""
Compiler and validator for inter_state_relations_statement_based.json (50 questions)
"""
import json
import os
from collections import Counter
from pathlib import Path

from build_isr_sb_part1 import get_sb_part1
from build_isr_sb_part2 import get_sb_part2
from tools.nova_content_engine.validator import ContentValidator

def main():
    q1 = get_sb_part1()
    q2 = get_sb_part2()
    all_q = q1 + q2

    print(f"[COMPILER] Total Statement-based questions loaded: {len(all_q)}")
    assert len(all_q) == 50, f"Expected 50 questions, got {len(all_q)}"

    # Check key distribution
    keys = Counter(q["correct_answer"] for q in all_q)
    print(f"[COMPILER] Answer Key Distribution: {dict(keys)}")

    # Check IDs
    ids = [q["id"] for q in all_q]
    assert len(set(ids)) == 50, "Duplicate IDs found!"
    expected_ids = [f"ISR_S_{i:03d}" for i in range(1, 51)]
    assert ids == expected_ids, f"ID mismatch! Got {ids[:5]}... Expected {expected_ids[:5]}..."

    # Check against Part 1 files for duplicate stems
    stems = set()
    for diff in ["easy", "medium", "hard"]:
        fp = f"data/questions/polity/inter_state_relations_{diff}.json"
        if os.path.exists(fp):
            with open(fp, "r", encoding="utf-8") as f:
                data = json.load(f)
            for item in data:
                stems.add(item["question_en"].strip().lower())

    # Check statement questions against stems
    collisions = []
    for q in all_q:
        s_en = q["question_en"].strip().lower()
        if s_en in stems:
            collisions.append((q["id"], s_en[:60]))
    if collisions:
        print(f"[ERROR] Collisions with existing Part 1: {collisions}")
        raise ValueError("Stem collisions detected!")
    else:
        print("[COMPILER] 0 collisions with existing Part 1 questions. Stems are completely unique!")

    # Write to target path
    out_dir = Path("data/questions/polity")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "inter_state_relations_statement_based.json"

    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(all_q, f, indent=2, ensure_ascii=False)

    print(f"[COMPILER] Saved 50 questions to {out_file}")

    # Validate with ContentValidator
    report = ContentValidator.validate_file(str(out_file), expected_count=50, expected_prefix="ISR_S_")
    print(report.summary())
    assert report.is_valid, "Validation failed!"
    print("[COMPILER] Validation PASSED!")

if __name__ == "__main__":
    main()
