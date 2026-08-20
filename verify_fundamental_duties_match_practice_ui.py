# -*- coding: utf-8 -*-
"""
Practice UI Loader Verification for Fundamental Duties Match the Following 25 MCQs
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

from core.question_loader import load_questions

def verify_practice_ui_loader():
    print("================================================================================")
    print("🚀 RUNNING FUNDAMENTAL DUTIES MATCH THE FOLLOWING PRACTICE UI LOADER VERIFICATION")
    print("================================================================================")

    parts = [
        "polity_fundamental_duties_part_1",
        "polity_fundamental_duties_part_2",
        "polity_fundamental_duties_part_3"
    ]

    for note_id in parts:
        for match_type in ["match", "match_the_following"]:
            questions = load_questions("polity", note_id, match_type)
            print(f"\n[CHECK] Loading '{match_type}' practice set for note: {note_id}")
            assert questions is not None, f"❌ Failed to load questions for {note_id}"
            assert len(questions) == 25, f"❌ Expected 25 questions, got {len(questions)}"

            # Validate first and last question structure
            first_q = questions[0]
            last_q = questions[-1]

            assert first_q["id"] == "FD_MTH_001", f"❌ Unexpected first question ID: {first_q['id']}"
            assert last_q["id"] == "FD_MTH_025", f"❌ Unexpected last question ID: {last_q['id']}"

            # Check list_1 and list_2 presence
            assert "list_1" in first_q and len(first_q["list_1"]) == 4
            assert "list_2" in first_q and len(first_q["list_2"]) == 4

            print(f"   ✅ Successfully loaded 25 Match the Following MCQs for {note_id} ({match_type}) (FD_MTH_001 to FD_MTH_025)")

    print("\n================================================================================")
    print("🏆 PRACTICE UI LOADER VERIFICATION SUCCESSFUL ACROSS ALL 3 PARTS!")
    print("================================================================================")

if __name__ == "__main__":
    verify_practice_ui_loader()
