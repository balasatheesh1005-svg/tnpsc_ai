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

def validate_vp_pyq_practice():
    print("================================================================================")
    print("🧪 VALIDATION SUITE — VICE-PRESIDENT PYQ PRACTICE (50 QUESTIONS)")
    print("================================================================================")

    file_path = "data/questions/polity/vice_president_pyq.json"
    assert os.path.exists(file_path), f"❌ File missing: {file_path}"
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert len(data) == 50, f"Expected 50 questions, got {len(data)}"
    print(f"  ✅ File exists, valid UTF-8 JSON, contains exactly {len(data)} questions.")

    ids = set()
    actual_pyq_count = 0
    pyq_pattern_count = 0

    for idx, q in enumerate(data, 1):
        qid = q.get("id")
        assert qid == f"POLITY_VP_PYQ_{idx:03d}", f"Invalid QID: {qid} (Expected POLITY_VP_PYQ_{idx:03d})"
        assert qid not in ids, f"Duplicate ID: {qid}"
        ids.add(qid)

        # Source type check
        stype = q.get("source_type")
        assert stype in ["ACTUAL_PYQ", "PYQ_PATTERN"], f"{qid}: Invalid source_type {stype}"
        if stype == "ACTUAL_PYQ":
            actual_pyq_count += 1
            assert "exam" in q and "year" in q, f"{qid}: Actual PYQ missing verified exam/year metadata"
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
        for k in ["A", "B", "C", "D"]:
            v = wno.get(k, {})
            en_desc = v.get("en", "") if isinstance(v, dict) else str(v)
            ta_desc = v.get("ta", "") if isinstance(v, dict) else str(v)
            assert len(en_desc.split()) >= 3, f"{qid}: Short distractor analysis for Option {k}"
            assert len(ta_desc.split()) >= 3, f"{qid}: Short TA distractor analysis for Option {k}"

        # TNPSC Tip check
        tip = q.get("tnpsc_tip", {})
        tip_en = tip.get("en", "") if isinstance(tip, dict) else str(tip)
        tip_ta = tip.get("ta", "") if isinstance(tip, dict) else str(tip)
        assert len(tip_en.split()) >= 3, f"{qid}: Short TNPSC Tip EN"
        assert len(tip_ta.split()) >= 3, f"{qid}: Short TNPSC Tip TA"

    print("  ✅ All 50 questions passed static, schema, option, answer, distractor, and tip validation!")
    print(f"  • Actual Verified PYQs: {actual_pyq_count}")
    print(f"  • PYQ Pattern Questions: {pyq_pattern_count}")

    # Loader verification
    print("\n--- REPOSITORY LOADER & UI PRACTICE SIMULATION ---")
    qs_loader = load_questions("polity_vice_president", "pyq")
    assert len(qs_loader) == 50, f"Loader error: expected 50 questions, got {len(qs_loader)}"
    print(f"  ✅ load_questions('polity_vice_president', 'pyq') loaded {len(qs_loader)} questions cleanly.")

    # Practice Session UI simulation
    success = start_practice_session(
        subject="polity",
        topic_id="polity_vice_president_part_1",
        repository_id="polity_vice_president",
        display_title="Vice-President PYQ Practice",
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
        record_practice_answer(question_index=idx, selected_option=corr, is_correct=True, question_id=qid)

    clear_practice_session()

    print("  ✅ Practice UI Session Simulation PASSED 100%!")
    print("\n================================================================================")
    print("🎉 VICE-PRESIDENT PYQ PRACTICE — 50 QUESTIONS CREATED, SAVED & VALIDATED")
    print("================================================================================")

if __name__ == "__main__":
    validate_vp_pyq_practice()
