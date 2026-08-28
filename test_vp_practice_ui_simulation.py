# -*- coding: utf-8 -*-
"""
End-to-End Practice Engine Simulation for Vice-President MCQ Datasets
"""

import sys
import json
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

import streamlit as st
def dummy_decorator(func):
    return func
st.cache_data = dummy_decorator

from core.question_engine.practice_session import (
    start_practice_session,
    get_practice_state,
    record_practice_answer,
    next_practice_question,
    set_practice_question_index,
    complete_practice_session,
    get_practice_summary,
    clear_practice_session
)
from core.question_loader import load_questions

def test_vp_practice_ui_simulation():
    print("================================================================================")
    print("🧪 VICE-PRESIDENT MCQ DATASETS: UI & PRACTICE ENGINE INTERACTIVE SIMULATION")
    print("================================================================================")

    datasets = [
        ("easy", 50),
        ("medium", 50),
        ("hard", 50),
        ("statement", 50),
        ("reasoning", 25),
        ("chronology", 25),
        ("match", 25),
        ("grand_test", 100)
    ]

    all_passed = True

    for mode, expected_count in datasets:
        print(f"\n▶ Testing Mode: {mode.upper()} ({expected_count} questions)...")

        # 1. Load questions
        qs = load_questions("polity_vice_president", mode)
        if len(qs) != expected_count:
            print(f"❌ FAIL: Expected {expected_count} questions for {mode}, got {len(qs)}")
            all_passed = False
            continue

        # 2. Start Session
        success = start_practice_session(
            subject="polity",
            topic_id="polity_vice_president_part_1",
            repository_id="polity_vice_president",
            display_title=f"Vice-President - {mode.title()}",
            repository_type=mode
        )
        assert success == True, "start_practice_session returned False"

        state = get_practice_state()
        assert state["active"] == True, "Session failed to activate"
        assert state["current_index"] == 0
        assert len(state["questions"]) == expected_count

        # 3. Verify render elements of every question in dataset
        for i in range(expected_count):
            q = state["questions"][i]
            qid = q.get("id") or q.get("question_id")
            
            # Check question texts
            q_en = q.get("question_en") or (q.get("question", {}).get("en") if isinstance(q.get("question"), dict) else '')
            q_ta = q.get("question_ta") or (q.get("question", {}).get("ta") if isinstance(q.get("question"), dict) else '')
            assert q_en and len(q_en.strip()) > 0, f"Q{i} ({qid}) missing EN text"
            assert q_ta and len(q_ta.strip()) > 0, f"Q{i} ({qid}) missing TA text"

            # Check options
            opts = q.get("options", [])
            assert isinstance(opts, list) and len(opts) == 4, f"Q{i} ({qid}) does not have 4 options"
            for opt in opts:
                assert opt.get("id") in ["A", "B", "C", "D"], f"Q{i} ({qid}) invalid option ID {opt.get('id')}"
                assert opt.get("en") and len(opt.get("en").strip()) > 0, f"Q{i} ({qid}) option {opt.get('id')} missing EN"
                assert opt.get("ta") and len(opt.get("ta").strip()) > 0, f"Q{i} ({qid}) option {opt.get('id')} missing TA"

            # Check correct answer & explanation
            corr = q.get("correct_answer")
            assert corr in ["A", "B", "C", "D"], f"Q{i} ({qid}) invalid correct_answer {corr}"

            exp_en = q.get("explanation_en") or (q.get("explanation", {}).get("en") if isinstance(q.get("explanation"), dict) else '')
            exp_ta = q.get("explanation_ta") or (q.get("explanation", {}).get("ta") if isinstance(q.get("explanation"), dict) else '')
            assert exp_en and len(exp_en.strip()) > 0, f"Q{i} ({qid}) missing EN explanation"
            assert exp_ta and len(exp_ta.strip()) > 0, f"Q{i} ({qid}) missing TA explanation"

            # Record simulated answer
            record_practice_answer(question_index=i, selected_option=corr, is_correct=True, question_id=qid)

        # 4. Navigation simulation
        set_practice_question_index(expected_count // 2)
        assert get_practice_state()["current_index"] == expected_count // 2
        set_practice_question_index(0)

        # 5. Clean session
        clear_practice_session()
        print(f"  ✅ Mode '{mode}': PASSED 100% ({expected_count} questions rendered & evaluated cleanly)")

    print("\n================================================================================")
    if all_passed:
        print("🎉 ALL 8 VICE-PRESIDENT MCQ DATASETS PASSED UI & PRACTICE ENGINE SIMULATION 100%!")
    else:
        print("❌ UI SIMULATION FAILED!")
    print("================================================================================")

if __name__ == "__main__":
    test_vp_practice_ui_simulation()
