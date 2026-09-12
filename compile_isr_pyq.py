# -*- coding: utf-8 -*-
"""
Compiler and validator for inter_state_relations_pyq.json (50 questions)
"""
import json
import os
from collections import Counter
from pathlib import Path

from build_isr_pyq_part1 import get_pyq_part1
from build_isr_pyq_part2 import get_pyq_part2
from tools.nova_content_engine.validator import ContentValidator

def main():
    q1 = get_pyq_part1()
    q2 = get_pyq_part2()
    all_q = q1 + q2

    print(f"[COMPILER] Total PYQ questions loaded: {len(all_q)}")
    assert len(all_q) == 50, f"Expected 50 questions, got {len(all_q)}"

    # Check key distribution
    keys = Counter(q["correct_answer"] for q in all_q)
    print(f"[COMPILER] PYQ Answer Key Distribution: {dict(keys)}")

    # Check IDs
    ids = [q["id"] for q in all_q]
    assert len(set(ids)) == 50, "Duplicate IDs found in PYQ!"
    expected_ids = [f"ISR_PYQ_{i:03d}" for i in range(1, 51)]
    assert ids == expected_ids, f"ID mismatch in PYQ! Got {ids[:5]}... Expected {expected_ids[:5]}..."

    # Check against Part 1 and Statement-Based for duplicate stems
    existing_stems = set()
    for cat in ["easy", "medium", "hard", "statement_based"]:
        fp = f"data/questions/polity/inter_state_relations_{cat}.json"
        if os.path.exists(fp):
            with open(fp, "r", encoding="utf-8") as f:
                data = json.load(f)
            for item in data:
                existing_stems.add(item["question_en"].strip().lower())

    collisions = []
    for q in all_q:
        s_en = q["question_en"].strip().lower()
        if s_en in existing_stems:
            collisions.append((q["id"], s_en[:60]))
    if collisions:
        print(f"[ERROR] Collisions with existing files: {collisions}")
        raise ValueError("Stem collisions detected in PYQ!")
    else:
        print("[COMPILER] 0 collisions with existing files. All 50 PYQ stems are completely unique!")

    # Write to target path
    out_dir = Path("data/questions/polity")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "inter_state_relations_pyq.json"

    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(all_q, f, indent=2, ensure_ascii=False)

    print(f"[COMPILER] Saved 50 questions to {out_file}")

    # Validate with ContentValidator
    report = ContentValidator.validate_file(str(out_file), expected_count=50, expected_prefix="ISR_PYQ_")
    print(report.summary())
    assert report.is_valid, "Validation failed!"
    print("[COMPILER] PYQ Validation PASSED!")

if __name__ == "__main__":
    main()
