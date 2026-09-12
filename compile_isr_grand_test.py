# -*- coding: utf-8 -*-
"""
Compiler for Inter-State Relations Grand Test (100 Questions)
Combines batches 1 to 4, performs comprehensive validations, and saves to
data/questions/polity/inter_state_relations_grand_test.json
"""

import json
from collections import Counter
from generate_isr_gt_batch1 import get_batch1
from generate_isr_gt_batch2 import get_batch2
from generate_isr_gt_batch3 import get_batch3
from generate_isr_gt_batch4 import get_batch4
from isr_gt_helper import load_core_stems
from tools.nova_content_engine.validator import ContentValidator

def compile_grand_test():
    b1 = get_batch1()
    b2 = get_batch2()
    b3 = get_batch3()
    b4 = get_batch4()
    
    all_qs = b1 + b2 + b3 + b4
    print(f"[GRAND TEST] Total compiled questions: {len(all_qs)}")
    assert len(all_qs) == 100, f"Expected 100, got {len(all_qs)}"
    
    # 1. Check ID sequence
    expected_ids = [f"ISR_GT_{i:03d}" for i in range(1, 101)]
    actual_ids = [q["id"] for q in all_qs]
    assert actual_ids == expected_ids, "ID sequence mismatch!"
    print("[GRAND TEST] ID sequence ISR_GT_001 to ISR_GT_100: PERFECT")
    
    # 2. Check Key Distribution
    key_dist = dict(Counter([q["correct_answer"] for q in all_qs]))
    print(f"[GRAND TEST] Key Distribution: {key_dist}")
    assert key_dist == {"A": 25, "B": 25, "C": 25, "D": 25}, f"Key distribution must be 25 each, got {key_dist}"
    
    # 3. Check Difficulty Distribution
    diff_dist = dict(Counter([q["difficulty"] for q in all_qs]))
    print(f"[GRAND TEST] Difficulty Distribution: {diff_dist}")
    assert diff_dist == {"Easy": 30, "Medium": 40, "Hard": 30}, f"Difficulty distribution mismatch: {diff_dist}"
    
    # 4. Check Intra-file Stems
    stems = [q["question_en"].strip().lower() for q in all_qs]
    assert len(stems) == len(set(stems)), "Intra-file duplicate stems found!"
    print("[GRAND TEST] Intra-file uniqueness: 100/100 UNIQUE")
    
    # 5. Check Cross-file Independence with Core 325 questions
    core_stems = load_core_stems()
    collisions = [q["id"] for q in all_qs if q["question_en"].strip().lower() in core_stems]
    print(f"[GRAND TEST] Collisions with Core (325 Qs): {len(collisions)}")
    assert len(collisions) == 0, f"Found collisions with Core: {collisions}"
    print("[GRAND TEST] Independence from Core: 100% INDEPENDENT (0 collisions)")
    
    # 6. Save JSON
    out_file = "data/questions/polity/inter_state_relations_grand_test.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)
    print(f"[GRAND TEST] Successfully saved to {out_file}")
    
    # 7. Validate with ContentValidator
    rep = ContentValidator.validate_file(out_file, expected_count=100, expected_prefix="ISR_GT_")
    print(f"[GRAND TEST] Validator Result: {'PASS' if rep.is_valid else 'FAIL'} | Audited: {rep.total_audited}")
    if rep.issues:
        for iss in rep.issues:
            print(f"  [{iss.severity}] {iss.question_id}: {iss.message}")
        assert False, "Validation failed!"
    print("[GRAND TEST] Validation PASSED with 0 issues!")

if __name__ == "__main__":
    compile_grand_test()
