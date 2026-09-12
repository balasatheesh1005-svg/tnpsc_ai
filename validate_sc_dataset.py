# -*- coding: utf-8 -*-
"""
Local Validation Script for Supreme Court Part 1 MCQs (150 Questions)
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

def validate():
    base_dir = "data/questions/polity"
    easy_file = os.path.join(base_dir, "supreme_court_easy.json")
    medium_file = os.path.join(base_dir, "supreme_court_medium.json")
    hard_file = os.path.join(base_dir, "supreme_court_hard.json")

    assert os.path.exists(easy_file), f"Missing {easy_file}"
    assert os.path.exists(medium_file), f"Missing {medium_file}"
    assert os.path.exists(hard_file), f"Missing {hard_file}"

    with open(easy_file, "r", encoding="utf-8") as f:
        easy_qs = json.load(f)

    with open(medium_file, "r", encoding="utf-8") as f:
        medium_qs = json.load(f)

    with open(hard_file, "r", encoding="utf-8") as f:
        hard_qs = json.load(f)

    print("==================================================")
    print("RUNNING LOCAL VALIDATION FOR SUPREME COURT PART 1")
    print("==================================================")

    print(f"✓ Easy Questions Count  : {len(easy_qs)}")
    print(f"✓ Medium Questions Count: {len(medium_qs)}")
    print(f"✓ Hard Questions Count  : {len(hard_qs)}")

    assert len(easy_qs) == 50, f"Expected 50 Easy questions, got {len(easy_qs)}"
    assert len(medium_qs) == 50, f"Expected 50 Medium questions, got {len(medium_qs)}"
    assert len(hard_qs) == 50, f"Expected 50 Hard questions, got {len(hard_qs)}"

    all_qs = easy_qs + medium_qs + hard_qs
    assert len(all_qs) == 150, f"Expected 150 total questions, got {len(all_qs)}"

    seen_ids = set()
    seen_stems_en = set()
    seen_stems_ta = set()
    ans_counts = {"A": 0, "B": 0, "C": 0, "D": 0}
    pattern_sequence = []

    for idx, q in enumerate(all_qs):
        # 1. Unique ID
        qid = q.get("id")
        assert qid, f"Question at index {idx} missing 'id'"
        assert qid not in seen_ids, f"Duplicate ID: {qid}"
        seen_ids.add(qid)

        # 2. Subject & Topic
        assert q.get("subject") == "Polity", f"Invalid subject in {qid}"
        assert q.get("topic") == "Supreme Court of India", f"Invalid topic in {qid}"

        # 3. Question text uniqueness & non-empty
        stem_en = q.get("question", {}).get("en", "").strip()
        stem_ta = q.get("question", {}).get("ta", "").strip()
        assert stem_en and stem_ta, f"Missing question stem text in {qid}"
        assert stem_en.lower() not in seen_stems_en, f"Duplicate English question text in {qid}: {stem_en}"
        assert stem_ta not in seen_stems_ta, f"Duplicate Tamil question text in {qid}: {stem_ta}"
        seen_stems_en.add(stem_en.lower())
        seen_stems_ta.add(stem_ta)

        # 4. Check question type is Direct (No Statement / Reasoning / Match / Chronology)
        qtype = q.get("question_type", "Direct")
        assert qtype == "Direct", f"Non-direct question type '{qtype}' in {qid}"
        assert not stem_en.startswith("Statement I:"), f"Statement type question found in {qid}"
        assert not stem_en.startswith("Assertion (A):"), f"Reasoning type question found in {qid}"
        assert "Match List-I" not in stem_en and "பொருத்துக" not in stem_ta, f"Match type question found in {qid}"

        # 5. Options verification
        options = q.get("options", [])
        assert len(options) == 4, f"Question {qid} does not have exactly 4 options"
        opt_ids = [o.get("id") for o in options]
        assert opt_ids == ["A", "B", "C", "D"], f"Question {qid} option IDs invalid: {opt_ids}"

        for opt in options:
            assert opt.get("en") and opt.get("ta"), f"Question {qid} option {opt.get('id')} missing text"

        # 6. Correct Answer verification
        corr = q.get("correct_answer")
        assert corr in ["A", "B", "C", "D"], f"Question {qid} invalid correct_answer: {corr}"
        ans_counts[corr] += 1
        pattern_sequence.append(corr)

        # 7. Explanation verification
        exp = q.get("explanation", {})
        assert exp.get("en") and exp.get("ta"), f"Question {qid} missing explanation"

        # 8. Schema flat fields compatibility check
        assert q.get("question_en") == stem_en, f"Question {qid} question_en mismatch"
        assert q.get("question_ta") == stem_ta, f"Question {qid} question_ta mismatch"
        assert len(q.get("options_en", [])) == 4, f"Question {qid} options_en mismatch"
        assert len(q.get("options_ta", [])) == 4, f"Question {qid} options_ta mismatch"
        assert q.get("explanation_en") == exp.get("en"), f"Question {qid} explanation_en mismatch"
        assert q.get("explanation_ta") == exp.get("ta"), f"Question {qid} explanation_ta mismatch"

        # 9. why_not_others check
        why = q.get("why_not_others", {})
        for letter in ["A", "B", "C", "D"]:
            assert letter in why, f"Question {qid} why_not_others missing key {letter}"
            assert why[letter].get("en") and why[letter].get("ta"), f"Question {qid} why_not_others[{letter}] missing text"

        # 10. trap_point, tnpsc_tip, high_yield_fact, source_reference
        assert q.get("trap_point", {}).get("en") and q.get("trap_point", {}).get("ta"), f"Question {qid} missing trap_point"
        assert q.get("tnpsc_tip", {}).get("en") and q.get("tnpsc_tip", {}).get("ta"), f"Question {qid} missing tnpsc_tip"
        assert q.get("high_yield_fact", {}).get("en") and q.get("high_yield_fact", {}).get("ta"), f"Question {qid} missing high_yield_fact"
        assert len(q.get("source_reference", [])) > 0, f"Question {qid} missing source_reference"

    # Check repeating pattern ABCDABCD
    pattern_str = "".join(pattern_sequence)
    assert "ABCDABCDABCD" not in pattern_str, "Obvious repeating pattern ABCDABCD... detected!"

    print("\n--- Answer Key Distribution Across All 150 Questions ---")
    for letter in ["A", "B", "C", "D"]:
        c = ans_counts[letter]
        pct = (c / 150) * 100
        print(f"  Option {letter}: {c} questions ({pct:.1f}%)")
        assert 35 <= c <= 40, f"Option {letter} count {c} is out of target range [35, 40]"

    print("\n==================================================")
    print("ALL 16 LOCAL VALIDATION CHECKS PASSED PERFECTLY!")
    print("==================================================")

if __name__ == "__main__":
    validate()
