# -*- coding: utf-8 -*-
"""
Master builder for 50 Municipalities PYQ MCQs (MUN_PYQ_001 to MUN_PYQ_050).
Strictly adheres to 24-field schema, balanced keys, and authentic Tamil translation.
"""
import json
import os
from build_mun_pyq_1_25 import get_pyq_1_25
from build_mun_pyq_26_50 import get_pyq_26_50
from rebalance_mun_helper import balance_question_keys

def main():
    q1 = get_pyq_1_25()
    q2 = get_pyq_26_50()
    questions = q1 + q2
    assert len(questions) == 50, f"Expected 50 questions, got {len(questions)}"
    
    # Deterministically balance keys across A, B, C, D (~12-13 each)
    balanced = balance_question_keys(questions)
    
    out_dir = os.path.join("data", "questions", "polity")
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "municipalities_pyq.json")
    
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)
        
    print(f"[SUCCESS] Wrote {len(balanced)} PYQs to {out_file}")

if __name__ == "__main__":
    main()
