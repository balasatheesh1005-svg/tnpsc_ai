# -*- coding: utf-8 -*-
"""
Validation Suite & Interactive UI Simulation for Prime Minister PYQ Practice (50 Questions)
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

import streamlit as st
def dummy_decorator(func):
    return func
st.cache_data = dummy_decorator

from core.question_loader import load_questions
from core.question_engine.practice_session import (
    start_practice_session,
    get_practice_state,
    record_practice_answer,
    clear_practice_session
)
from ui.question_engine.parser import UniversalQuestionAdapter

def validate_pm_pyq_practice():
    print("================================================================================")
    print("🧪 VALIDATION SUITE — PRIME MINISTER PYQ PRACTICE (50 QUESTIONS)")
    print("================================================================================")

    file_path = "data/questions/polity/prime_minister_pyq.json"
    assert os.path.exists(file_path), f"❌ File missing: {file_path}"
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert len(data) == 50, f"Expected 50 questions, got {len(data)}"
    print(f"  ✅ File exists, valid UTF-8 JSON, contains exactly {len(data)} questions.")

    ids = set()
    actual_pyq_count = 0
    pyq_pattern_count = 0

    # Load existing 375 PM MCQs to check for duplicate IDs or duplicate stems
    existing_stems = set()
    existing_files = [
        "data/questions/polity/prime_minister_easy.json",
        "data/questions/polity/prime_minister_medium.json",
        "data/questions/polity/prime_minister_hard.json",
        "data/questions/polity/prime_minister_statement.json",
        "data/questions/polity/prime_minister_reasoning.json",
        "data/questions/polity/prime_minister_chronology.json",
        "data/questions/polity/prime_minister_match.json",
        "data/questions/polity/prime_minister_grand_test.json"
    ]
    for ef in existing_files:
        if os.path.exists(ef):
            with open(ef, encoding="utf-8") as f:
                edf = json.load(f)
                for item in edf:
                    st_text = (item.get("question_en") or str(item.get("question"))).strip().lower()
                    existing_stems.add(st_text)

    print(f"  • Loaded {len(existing_stems)} existing non-PYQ Prime Minister question stems for duplicate control.")

    for idx, q in enumerate(data, 1):
        qid = q.get("id")
        expected_id = f"POLITY_PM_PYQ_{idx:03d}"
        assert qid == expected_id, f"Invalid QID: {qid} (Expected {expected_id})"
        assert qid not in ids, f"Duplicate ID: {qid}"
        ids.add(qid)

        # Duplicate check against existing non-PYQ MCQs (unless it's an Actual verified PYQ)
        st_en = (q.get("question_en") or str(q.get("question"))).strip().lower()
        if q.get("source_type") != "ACTUAL_PYQ":
            assert st_en not in existing_stems, f"{qid}: Duplicate question stem detected in existing PM datasets"

        # Source type check
        stype = q.get("source_type")
        assert stype in ["ACTUAL_PYQ", "PYQ_PATTERN"], f"{qid}: Invalid source_type {stype}"
        if stype == "ACTUAL_PYQ":
            actual_pyq_count += 1
            assert "exam" in q and "year" in q and "group" in q, f"{qid}: Actual PYQ missing verified exam/year/group metadata"
            assert "question_number" in q or "source_reference" in q, f"{qid}: Actual PYQ missing source reference"
        else:
            pyq_pattern_count += 1
            assert "pattern_basis" in q, f"{qid}: PYQ_PATTERN missing pattern_basis"

        # Options check
        opts = q.get("options", [])
        assert len(opts) == 4, f"{qid}: Expected 4 options"
        opt_ids = [o.get("id") for o in opts if isinstance(o, dict)]
        assert opt_ids == ["A", "B", "C", "D"], f"{qid}: Invalid option IDs {opt_ids}"

        # Answer check
        corr = q.get("correct_answer")
        assert corr in ["A", "B", "C", "D"], f"{qid}: Invalid correct_answer {corr}"

        # Explanations check
        exp_en = q.get("explanation_en") or (q.get("explanation", {}).get("en") if isinstance(q.get("explanation"), dict) else '')
        exp_ta = q.get("explanation_ta") or (q.get("explanation", {}).get("ta") if isinstance(q.get("explanation"), dict) else '')
        assert len(exp_en.split()) >= 4, f"{qid}: Weak EN explanation"
        assert len(exp_ta.split()) >= 4, f"{qid}: Weak TA explanation"

        # Distractor analysis check
        wno = q.get("why_not_others", {})
        assert isinstance(wno, dict) and len(wno) == 4, f"{qid}: Invalid why_not_others dict"
        da = q.get("distractor_analysis", {})
        assert isinstance(da, dict) and len(da) == 4, f"{qid}: Invalid distractor_analysis dict"

        for k in ["A", "B", "C", "D"]:
            v = wno.get(k, {})
            en_desc = v.get("en", "") if isinstance(v, dict) else str(v)
            ta_desc = v.get("ta", "") if isinstance(v, dict) else str(v)
            assert len(en_desc.split()) >= 3, f"{qid}: Short distractor analysis for Option {k}"
            assert len(ta_desc.split()) >= 3, f"{qid}: Short TA distractor analysis for Option {k}"

            # Ensure NO weak distractor analysis
            low_en = en_desc.lower()
            assert not (low_en == "option a is incorrect" or low_en == "option b is incorrect" or low_en == "option c is incorrect" or low_en == "option d is incorrect"), f"{qid}: Weak distractor text found for Option {k}"

        # TNPSC Tip check
        tip = q.get("tnpsc_expert_tip") or q.get("tnpsc_tip", {})
        tip_en = tip.get("en", "") if isinstance(tip, dict) else str(tip)
        tip_ta = tip.get("ta", "") if isinstance(tip, dict) else str(tip)
        assert len(tip_en.split()) >= 3, f"{qid}: Short TNPSC Tip EN"
        assert len(tip_ta.split()) >= 3, f"{qid}: Short TNPSC Tip TA"

        # High yield fact check
        hy = q.get("high_yield_revision_fact") or q.get("revision_fact", {})
        hy_en = hy.get("en", "") if isinstance(hy, dict) else str(hy)
        hy_ta = hy.get("ta", "") if isinstance(hy, dict) else str(hy)
        assert len(hy_en.split()) >= 3, f"{qid}: Short High Yield Fact EN"
        assert len(hy_ta.split()) >= 3, f"{qid}: Short High Yield Fact TA"

    print("  ✅ All 50 questions passed static, schema, option, answer, distractor, tip, and duplicate control validation!")
    print(f"  • Actual Verified PYQs: {actual_pyq_count}")
    print(f"  • PYQ Pattern Questions: {pyq_pattern_count}")

    # Loader verification
    print("\n--- REPOSITORY LOADER & UI PRACTICE SIMULATION ---")
    qs_loader = load_questions("polity_prime_minister", "pyq")
    assert len(qs_loader) == 50, f"Loader error: expected 50 questions, got {len(qs_loader)}"
    print(f"  ✅ load_questions('polity_prime_minister', 'pyq') loaded {len(qs_loader)} questions cleanly.")

    # Practice Session UI simulation
    success = start_practice_session(
        subject="polity",
        topic_id="polity_prime_minister_part_1",
        repository_id="polity_prime_minister",
        display_title="Prime Minister PYQ Practice",
        repository_type="pyq"
    )
    assert success == True, "start_practice_session returned False"

    state = get_practice_state()
    assert state["active"] == True
    assert len(state["questions"]) == 50

    for idx in range(50):
        q = state["questions"][idx]
        qid = q.get("id") or q.get("question_id")
        corr = q.get("correct_answer")

        # Test UniversalQuestionAdapter normalization
        norm_q = UniversalQuestionAdapter.normalize(q)
        assert norm_q.id == qid
        assert norm_q.correct_answer in ["A", "B", "C", "D"]
        assert len(norm_q.options) == 4

        record_practice_answer(question_index=idx, selected_option=corr, is_correct=True, question_id=qid)

    clear_practice_session()

    print("  ✅ Practice UI Session Simulation PASSED 100%!")
    print("\n================================================================================")
    print("🎉 PRIME MINISTER PYQ PRACTICE — 50 QUESTIONS CREATED, SAVED & VALIDATED")
    print("================================================================================")
    return True

if __name__ == "__main__":
    validate_pm_pyq_practice()
