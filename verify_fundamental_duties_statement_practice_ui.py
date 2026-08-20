# -*- coding: utf-8 -*-
"""
Practice UI Loader Verification for Fundamental Duties Statement 50 MCQs
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

from core.question_loader import load_questions

def verify_practice_ui_loader():
    print("================================================================================")
    print("🚀 RUNNING FUNDAMENTAL DUTIES STATEMENT PRACTICE UI LOADER VERIFICATION")
    print("================================================================================")

    parts = [
        "polity_fundamental_duties_part_1",
        "polity_fundamental_duties_part_2",
        "polity_fundamental_duties_part_3"
    ]

    for note_id in parts:
        questions = load_questions("polity", note_id, "statement")
        print(f"\n[CHECK] Loading 'statement' practice set for note: {note_id}")
        assert questions is not None, f"❌ Failed to load questions for {note_id}"
        assert len(questions) == 50, f"❌ Expected 50 questions, got {len(questions)}"

        # Validate first and last question structure
        first_q = questions[0]
        last_q = questions[-1]

        assert first_q["id"] == "FD_S_001", f"❌ Unexpected first question ID: {first_q['id']}"
        assert last_q["id"] == "FD_S_050", f"❌ Unexpected last question ID: {last_q['id']}"

        print(f"   ✅ Successfully loaded 50 Statement MCQs for {note_id} (FD_S_001 to FD_S_050)")

    print("\n================================================================================")
    print("🏆 PRACTICE UI LOADER VERIFICATION SUCCESSFUL ACROSS ALL 3 PARTS!")
    print("================================================================================")

if __name__ == "__main__":
    verify_practice_ui_loader()
