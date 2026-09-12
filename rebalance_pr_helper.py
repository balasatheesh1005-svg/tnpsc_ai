# -*- coding: utf-8 -*-
"""
Deterministic option balancer for Panchayati Raj MCQs.
Balances answer keys across A, B, C, D to reach ~25% each while perfectly
maintaining options, options_en, options_ta, why_not_others, and answer fields.
"""
from collections import Counter
import copy

def balance_question_keys(questions: list, target_counts: dict = None) -> list:
    total = len(questions)
    if target_counts is None:
        base = total // 4
        rem = total % 4
        target_counts = {
            "A": base + (1 if rem > 0 else 0),
            "B": base + (1 if rem > 1 else 0),
            "C": base + (1 if rem > 2 else 0),
            "D": base
        }
    
    current_counts = Counter(q["correct_answer"] for q in questions)
    
    balanced = [copy.deepcopy(q) for q in questions]
    
    # We want to shift from overrepresented keys to underrepresented keys
    for q in balanced:
        curr_key = q["correct_answer"]
        if current_counts[curr_key] > target_counts[curr_key]:
            # find an underrepresented key
            target_key = None
            for cand in ["A", "B", "C", "D"]:
                if current_counts[cand] < target_counts[cand]:
                    target_key = cand
                    break
            
            if target_key and target_key != curr_key:
                # swap curr_key with target_key in q
                idx_map = {"A": 0, "B": 1, "C": 2, "D": 3}
                c_idx = idx_map[curr_key]
                t_idx = idx_map[target_key]
                
                # swap in options
                q["options"][c_idx]["en"], q["options"][t_idx]["en"] = q["options"][t_idx]["en"], q["options"][c_idx]["en"]
                q["options"][c_idx]["ta"], q["options"][t_idx]["ta"] = q["options"][t_idx]["ta"], q["options"][c_idx]["ta"]
                
                # swap in options_en
                q["options_en"][c_idx], q["options_en"][t_idx] = q["options_en"][t_idx], q["options_en"][c_idx]
                
                # swap in options_ta
                q["options_ta"][c_idx], q["options_ta"][t_idx] = q["options_ta"][t_idx], q["options_ta"][c_idx]
                
                # swap in why_not_others
                wno = q.get("why_not_others", {})
                if curr_key in wno and target_key in wno:
                    wno[curr_key], wno[target_key] = wno[target_key], wno[curr_key]
                
                q["correct_answer"] = target_key
                q["answer"] = target_key.lower()
                
                current_counts[curr_key] -= 1
                current_counts[target_key] += 1
                
    return balanced
