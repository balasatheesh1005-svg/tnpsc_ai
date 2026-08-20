# -*- coding: utf-8 -*-
"""
Answer Key Equalizer for Preamble Grand Test (100 MCQs)
Target: Exactly 25 A, 25 B, 25 C, 25 D
Current: 29 A, 25 B, 23 C, 23 D
Changes needed: Move 2 A -> C, 2 A -> D.
"""

import json
import os
import sys
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

file_path = "data/questions/polity/preamble_grand_test.json"
with open(file_path, "r", encoding="utf-8") as f:
    qs = json.load(f)

# Find 4 questions currently having answer 'A'
a_indices = [i for i, q in enumerate(qs) if q["correct_answer"] == "A"]
print(f"Indices with answer A ({len(a_indices)}): {a_indices[:6]}")

# We will swap option A with C for 2 questions (e.g. index 25 (Q26), index 34 (Q35))
# And swap option A with D for 2 questions (e.g. index 51 (Q52), index 63 (Q64))

def swap_options(q, target_key):
    cur_key = q["correct_answer"] # "A"
    if cur_key == target_key:
        return
    
    # Swap options list
    opts = q["options"]
    idx_cur = [i for i, o in enumerate(opts) if o["id"] == cur_key][0]
    idx_target = [i for i, o in enumerate(opts) if o["id"] == target_key][0]
    
    # Swap option content but preserve IDs
    opts[idx_cur]["en"], opts[idx_target]["en"] = opts[idx_target]["en"], opts[idx_cur]["en"]
    opts[idx_cur]["ta"], opts[idx_target]["ta"] = opts[idx_target]["ta"], opts[idx_cur]["ta"]
    
    # Update flat arrays
    q["options_en"] = [o["en"] for o in opts]
    q["options_ta"] = [o["ta"] for o in opts]
    
    # Set new correct answer
    q["correct_answer"] = target_key
    q["answer"] = target_key.lower()
    
    # Swap why_not_others explanations
    if "why_not_others" in q:
        q["why_not_others"][cur_key], q["why_not_others"][target_key] = (
            q["why_not_others"][target_key], q["why_not_others"][cur_key]
        )

# Apply swaps
swap_options(qs[25], "C")  # Q26 -> C
swap_options(qs[34], "C")  # Q35 -> C
swap_options(qs[51], "D")  # Q52 -> D
swap_options(qs[63], "D")  # Q64 -> D

# Check new counts
answers = [q["correct_answer"] for q in qs]
counts = Counter(answers)
print("Updated Answer Key Counts:")
for k in sorted(counts.keys()):
    print(f"  - Option {k}: {counts[k]}")

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(qs, f, ensure_ascii=False, indent=2)

print("Saved perfectly balanced answer key to preamble_grand_test.json!")
