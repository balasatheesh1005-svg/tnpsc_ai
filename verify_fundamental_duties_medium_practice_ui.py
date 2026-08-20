# -*- coding: utf-8 -*-
"""
UI Practice Engine Validation Script for Fundamental Duties Medium 50 MCQs
"""

import sys
import json
import os

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

from core.question_loader import load_questions

def test_practice_ui_loading():
    print("================================================================================")
    print("🚀 RUNNING PRACTICE UI RESOLUTION VALIDATION FOR FUNDAMENTAL DUTIES MEDIUM MCQS")
    print("================================================================================")

    for part_num in [1, 2, 3]:
        topic_id = f"polity_fundamental_duties_part_{part_num}"
        questions = load_questions("polity", topic_id, "medium")
        
        assert questions is not None, f"❌ Failed to load medium questions for {topic_id}"
        assert len(questions) == 50, f"❌ Loaded count {len(questions)} != 50 for {topic_id}"
        
        # Test first question structure
        q0 = questions[0]
        assert "id" in q0 and q0["id"] == "FD_M_001"
        assert "question" in q0 and "en" in q0["question"] and "ta" in q0["question"]
        assert len(q0["options"]) == 4
        assert "correct_answer" in q0 and q0["correct_answer"] in ["A", "B", "C", "D"]
        assert "explanation" in q0 and "why_not_others" in q0 and "tnpsc_tip" in q0
        
        print(f"   - Part {part_num} (`{topic_id}`) -> Successfully resolved and validated 50 Medium MCQs.")

    print("\n================================================================================")
    print("🏆 PRACTICE UI RESOLUTION VERIFICATION PASSED FOR ALL 3 PARTS!")
    print("================================================================================")

if __name__ == "__main__":
    test_practice_ui_loading()
