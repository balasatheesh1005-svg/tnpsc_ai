# -*- coding: utf-8 -*-
"""
Local Validation Script for Supreme Court Part 2 MCQs (175 Questions)
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

def validate():
    base_dir = "data/questions/polity"
    
    stmt_file = os.path.join(base_dir, "supreme_court_statement.json")
    reas_file = os.path.join(base_dir, "supreme_court_reasoning.json")
    match_file = os.path.join(base_dir, "supreme_court_match.json")
    chrono_file = os.path.join(base_dir, "supreme_court_chronology.json")
    pyq_file = os.path.join(base_dir, "supreme_court_pyq.json")

    assert os.path.exists(stmt_file), f"Missing {stmt_file}"
    assert os.path.exists(reas_file), f"Missing {reas_file}"
    assert os.path.exists(match_file), f"Missing {match_file}"
    assert os.path.exists(chrono_file), f"Missing {chrono_file}"
    assert os.path.exists(pyq_file), f"Missing {pyq_file}"

    with open(stmt_file, "r", encoding="utf-8") as f:
        stmt_qs = json.load(f)

    with open(reas_file, "r", encoding="utf-8") as f:
        reas_qs = json.load(f)

    with open(match_file, "r", encoding="utf-8") as f:
        match_qs = json.load(f)

    with open(chrono_file, "r", encoding="utf-8") as f:
        chrono_qs = json.load(f)

    with open(pyq_file, "r", encoding="utf-8") as f:
        pyq_qs = json.load(f)

    print("==================================================")
    print("RUNNING LOCAL VALIDATION FOR SUPREME COURT PART 2")
    print("==================================================")

    print(f"✓ Statement Questions Count : {len(stmt_qs)}")
    print(f"✓ Reasoning Questions Count : {len(reas_qs)}")
    print(f"✓ Match Questions Count     : {len(match_qs)}")
    print(f"✓ Chronology Questions Count: {len(chrono_qs)}")
    print(f"✓ PYQ Questions Count        : {len(pyq_qs)}")

    assert len(stmt_qs) == 50, f"Expected 50 Statement questions, got {len(stmt_qs)}"
    assert len(reas_qs) == 25, f"Expected 25 Reasoning questions, got {len(reas_qs)}"
    assert len(match_qs) == 25, f"Expected 25 Match questions, got {len(match_qs)}"
    assert len(chrono_qs) == 25, f"Expected 25 Chronology questions, got {len(chrono_qs)}"
    assert len(pyq_qs) == 50, f"Expected 50 PYQ questions, got {len(pyq_qs)}"

    all_qs = stmt_qs + reas_qs + match_qs + chrono_qs + pyq_qs
    assert len(all_qs) == 175, f"Expected 175 total questions, got {len(all_qs)}"

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

        # 4. Question type verification
        qtype = q.get("question_type")
        assert qtype in ["Statement", "Reasoning", "Match", "Chronology", "Direct", "PYQ"], f"Invalid question_type '{qtype}' in {qid}"

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

    print("\n--- Answer Key Distribution Across All 175 Part 2 Questions ---")
    for letter in ["A", "B", "C", "D"]:
        c = ans_counts[letter]
        pct = (c / 175) * 100
        print(f"  Option {letter}: {c} questions ({pct:.1f}%)")
        assert 40 <= c <= 48, f"Option {letter} count {c} is out of target range [40, 48]"

    print("\n==================================================")
    print("ALL LOCAL VALIDATION CHECKS FOR PART 2 PASSED PERFECTLY!")
    print("==================================================")

if __name__ == "__main__":
    validate()
