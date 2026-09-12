# -*- coding: utf-8 -*-
"""
Emergency Provisions Grand Test Builder (100 MCQs: EP_GT_001 to EP_GT_100)
Strictly adheres to:
1. 24-field schema verified by ContentValidator
2. Bilingual parity (English and Tamil)
3. Balanced answer distribution: exactly A: 25, B: 25, C: 25, D: 25
4. 100% unique question stems
5. Realistic TNPSC Group 1 / Group 2 Prelims Grand Test standard
"""

import json
import os
from collections import Counter
from tools.nova_content_engine.validator import ContentValidator

from build_ep_gt_batch1 import get_gt_batch1
from build_ep_gt_batch2 import get_gt_batch2
from build_ep_gt_batch3 import get_gt_batch3
from build_ep_gt_batch4 import get_gt_batch4

def build_and_validate_grand_test():
    qs = get_gt_batch1() + get_gt_batch2() + get_gt_batch3() + get_gt_batch4()
    
    print(f"[Grand Test] Total questions: {len(qs)}")
    assert len(qs) == 100, f"Expected 100 questions, got {len(qs)}"

    # Check key distribution
    dist = dict(Counter([q["correct_answer"] for q in qs]))
    print(f"[Grand Test] Key Distribution: {dist}")
    assert dist == {"A": 25, "B": 25, "C": 25, "D": 25}, f"Distribution mismatch: {dist}"

    # Check stem uniqueness
    stems = [q["question_en"].strip().lower() for q in qs]
    assert len(stems) == len(set(stems)), f"Duplicate stems found! Unique: {len(set(stems))}, Total: {len(stems)}"
    print("[Grand Test] Stems are 100% unique.")

    out_file = "data/questions/polity/emergency_provisions_grand_test.json"
    os.makedirs(os.path.dirname(out_file), exist_ok=True)
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2, ensure_ascii=False)
    print(f"[Grand Test] Saved to {out_file}")

    # Run ContentValidator
    rep = ContentValidator.validate_file(out_file, expected_count=100, expected_prefix="EP_GT_")
    print(f"[Grand Test] Validator Status: {'PASS' if rep.is_valid else 'FAIL'} | Audited: {rep.total_audited}")
    if rep.issues:
        for iss in rep.issues:
            print(f"  [{iss.severity}] {iss.question_id}: {iss.message}")
        assert False, "Grand Test Validation failed!"
    print("[Grand Test] Validation PASSED with 0 issues!")

if __name__ == "__main__":
    build_and_validate_grand_test()
