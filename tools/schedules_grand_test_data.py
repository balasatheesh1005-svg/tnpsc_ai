# -*- coding: utf-8 -*-
"""
Grand Test MCQs for Constitutional Schedules (100 questions: SCH_GT_001 to SCH_GT_100)
100% independent from Core questions (zero duplicate English stems).
Covers all 12 schedules comprehensively:
- First Schedule: SCH_GT_001 to 008
- Second Schedule: SCH_GT_009 to 016
- Third Schedule: SCH_GT_017 to 024
- Fourth Schedule: SCH_GT_025 to 032
- Fifth Schedule: SCH_GT_033 to 040
- Sixth Schedule: SCH_GT_041 to 048
- Seventh Schedule: SCH_GT_049 to 058
- Eighth Schedule: SCH_GT_059 to 068
- Ninth Schedule: SCH_GT_069 to 076
- Tenth Schedule: SCH_GT_077 to 084
- Eleventh Schedule: SCH_GT_085 to 092
- Twelfth Schedule: SCH_GT_093 to 100
"""
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.insert(0, os.path.dirname(__file__))

from schedules_gt_batch1 import get_batch1
from schedules_gt_batch2 import get_batch2
from schedules_gt_batch3 import get_batch3
from schedules_gt_batch4 import get_batch4

def get_grand_test_questions():
    b1 = get_batch1()
    b2 = get_batch2()
    b3 = get_batch3()
    b4 = get_batch4()
    
    all_qs = b1 + b2 + b3 + b4
    assert len(all_qs) == 100, f"Expected exactly 100 Grand Test questions, got {len(all_qs)}"
    return all_qs

if __name__ == "__main__":
    qs = get_grand_test_questions()
    print(f"Loaded {len(qs)} Grand Test questions successfully.")
    for i, q in enumerate(qs, 1):
        print(f"{i}. {q['id']} - {q['subtopic']}: {q['question_en'][:60]}...")
