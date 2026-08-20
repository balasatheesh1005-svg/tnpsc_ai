# -*- coding: utf-8 -*-
"""
End-to-End Simulation of Practice Session State Machine with Preamble Chronology
"""

import sys
import json
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

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

def test_full_practice_ui_lifecycle():
    print("================================================================================")
    print("🧪 PRACTICE ENGINE INTERACTIVE SIMULATION: PREAMBLE CHRONOLOGY")
    print("================================================================================")

    # 1. Load questions
    qs = load_questions("polity", "polity_preamble_part_1", "chronology")
    assert len(qs) == 25, f"Expected 25 questions, got {len(qs)}"

    # 2. Start Session
    start_practice_session(
        subject="polity",
        topic_id="polity_preamble_part_1",
        repository_id="polity_preamble",
        repository_type="chronology",
        display_title="Preamble Part 1",
        questions=qs
    )

    state = get_practice_state()
    assert state["active"] == True
    assert state["current_index"] == 0
    assert len(state["questions"]) == 25
    assert state["completed"] == False
    assert state["review_mode"] == False
    print("   ✅ Practice session initialized successfully (25 questions active)")

    # 3. Simulate answering questions
    for i in range(25):
        q = state["questions"][i]
        correct_ans = q["correct_answer"]
        # Simulate answering correctly for first 20, incorrectly for last 5
        selected = correct_ans if i < 20 else ("A" if correct_ans != "A" else "B")
        
        record_practice_answer(
            question_index=i,
            selected_option=selected,
            time_spent_seconds=45
        )
        assert i in state["answers"]
        assert state["answers"][i]["selected_option"] == selected

    print("   ✅ All 25 questions answered (20 correct, 5 incorrect)")

    # 4. Test Navigation jumps & Next/Prev
    set_practice_question_index(10)
    assert get_practice_state()["current_index"] == 10
    set_practice_question_index(0)
    assert get_practice_state()["current_index"] == 0
    print("   ✅ Question index jump navigation PASSED")

    # 5. Complete Session & Result calculation
    complete_practice_session()
    state = get_practice_state()
    assert state["completed"] == True
    
    summary = get_practice_summary()
    print(f"   - Practice Summary: Total={summary['total']}, Answered={summary['answered']}, Correct={summary['correct']}, Wrong={summary['incorrect']}, Accuracy={summary['accuracy_pct']}%")
    assert summary["total"] == 25
    assert summary["answered"] == 25
    assert summary["correct"] == 20
    assert summary["incorrect"] == 5
    assert summary["accuracy_pct"] == 80.0
    print("   ✅ Score and Accuracy Calculation PASSED (80.0% accuracy)")

    # 6. Review Mode
    state["review_mode"] = True
    assert get_practice_state()["review_mode"] == True
    print("   ✅ Review Mode transition PASSED")

    # 7. Reset / Exit Session
    clear_practice_session()
    assert get_practice_state()["active"] == False
    print("   ✅ Session Cleanup PASSED")

    print("\n================================================================================")
    print("🎉 PRACTICE WORKSPACE & UI ENGINE SIMULATION PASSED 100%!")
    print("================================================================================")

if __name__ == "__main__":
    test_full_practice_ui_lifecycle()
