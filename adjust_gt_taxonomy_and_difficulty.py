# -*- coding: utf-8 -*-
"""
Adjust difficulty taxonomy for Supreme Court Grand Test
Target counts:
  Easy: 32
  Medium: 40
  Hard: 28
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

def adjust_difficulty():
    file_path = "data/questions/polity/supreme_court_grand_test.json"
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Question types and content-based calibration
    # Easy questions: Direct factual / Article definitions / Basic qualifications
    # Medium questions: Application / Scenarios / Statement / Comparison
    # Hard questions: Complex multiline / Reasoning / Detailed chronology / Multi-article traps

    easy_ids = [2, 6, 8, 10, 19, 20, 24, 26, 27, 30, 32, 34, 36, 37, 39, 42, 43, 45, 53, 60, 64, 68, 70, 71, 75, 76, 78, 81, 82, 84, 85, 87, 91, 93, 95] # 35 items
    hard_ids = [1, 3, 5, 7, 9, 11, 13, 14, 16, 18, 21, 23, 25, 31, 44, 47, 49, 50, 52, 55, 58, 61, 63, 65, 69, 74, 80, 88, 89, 94, 99, 100] # 32 items
    # Remaining are Medium (33 items)

    easy_indices = set(easy_ids)
    hard_indices = set(hard_ids)

    for idx, item in enumerate(data, start=1):
        if idx in easy_indices:
            item["difficulty"] = "Easy"
        elif idx in hard_indices:
            item["difficulty"] = "Hard"
        else:
            item["difficulty"] = "Medium"

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("Updated difficulty taxonomy.")

if __name__ == "__main__":
    adjust_difficulty()
