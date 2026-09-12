# -*- coding: utf-8 -*-
"""
Answer Key Randomizer and Anti-Pattern Engine.
Enforces the CRITICAL ANSWER POSITION RULE:
- Balanced counts (e.g., 12-13 for 50 MCQs, 6-7 for 25 MCQs, exactly 25 each for 100 Grand Test)
- Shuffled positions across the entire question set (no blocks, no AAAAA/BBBBB/CCCCC/DDDDD)
- No repeating cycles (no ABCDABCD or ABABAB)
- Maximum consecutive identical answers <= 2
- Balanced distribution across test quartiles
- Full pedagogical synchronization across options, options_en, options_ta, why_not_others, correct_answer, and answer.
"""
import copy
import random
from collections import Counter
from typing import Dict, List, Optional, Tuple


def generate_shuffled_key_pool(
    count: int,
    counts: Optional[Dict[str, int]] = None,
    seed: Optional[int] = None
) -> List[str]:
    """
    Generates a non-periodic, naturally shuffled pool of answer keys (A, B, C, D)
    meeting strict TNPSC anti-predictability constraints.
    """
    rng = random.Random(seed) if seed is not None else random.Random()
    
    if counts is None:
        base = count // 4
        rem = count % 4
        keys = ["A", "B", "C", "D"]
        rng.shuffle(keys)
        counts = {k: base + (1 if k in keys[:rem] else 0) for k in keys}
        
    attempts = 0
    max_attempts = 20000
    while attempts < max_attempts:
        attempts += 1
        pool = []
        for k in ["A", "B", "C", "D"]:
            pool.extend([k] * counts.get(k, 0))
        rng.shuffle(pool)
        
        # 1. Max consecutive run <= 2
        has_long_run = False
        curr_run = 1
        for i in range(1, len(pool)):
            if pool[i] == pool[i-1]:
                curr_run += 1
                if curr_run > 2:
                    has_long_run = True
                    break
            else:
                curr_run = 1
        if has_long_run:
            continue
            
        # 2. No repeating cycles of length 2, 3, 4 repeated 3+ times
        has_cycle = False
        for L in [2, 3, 4]:
            for i in range(len(pool) - 3*L + 1):
                if pool[i:i+L] == pool[i+L:i+2*L] == pool[i+2*L:i+3*L]:
                    has_cycle = True
                    break
            if has_cycle:
                break
        if has_cycle:
            continue
            
        # 3. Quartile balance
        q_len = max(1, count // 4)
        min_per_q = 1 if count <= 30 else (2 if count <= 60 else 4)
        has_unbalanced_quartile = False
        for q_idx in range(4):
            quarter = pool[q_idx*q_len : (q_idx+1)*q_len if q_idx < 3 else count]
            q_counts = Counter(quarter)
            for k in ["A", "B", "C", "D"]:
                if q_counts[k] < min_per_q:
                    has_unbalanced_quartile = True
                    break
            if has_unbalanced_quartile:
                break
        if has_unbalanced_quartile:
            continue
            
        return pool
        
    raise RuntimeError(f"Failed to generate non-periodic key pool for count={count} after {max_attempts} attempts")


def audit_answer_pattern(keys: List[str], count: Optional[int] = None) -> Tuple[bool, List[str]]:
    """
    Audits a sequence of answer keys against the CRITICAL ANSWER POSITION RULE:
    - No block distribution
    - Max consecutive identical <= 2
    - No repeating cycles
    - Balanced counts
    - Quartile presence
    """
    issues = []
    if count is None:
        count = len(keys)
        
    if len(keys) != count:
        issues.append(f"Expected {count} keys, got {len(keys)}")
        
    upper_keys = [k.upper() for k in keys]
        
    # Check counts
    key_counts = Counter(upper_keys)
    if count == 100:
        for k in ["A", "B", "C", "D"]:
            if key_counts[k] != 25:
                issues.append(f"Grand test key {k} count is {key_counts[k]}, expected 25")
    elif count == 50:
        for k in ["A", "B", "C", "D"]:
            if not (12 <= key_counts[k] <= 13):
                issues.append(f"Key {k} count is {key_counts[k]}, expected 12 or 13 for 50 MCQs")
    elif count == 25:
        for k in ["A", "B", "C", "D"]:
            if not (6 <= key_counts[k] <= 7):
                issues.append(f"Key {k} count is {key_counts[k]}, expected 6 or 7 for 25 MCQs")

    # Check consecutive run (max 2)
    curr_run = 1
    for i in range(1, len(upper_keys)):
        if upper_keys[i] == upper_keys[i-1]:
            curr_run += 1
        else:
            if curr_run > 2:
                issues.append(f"Consecutive identical run of {curr_run} at index {i-curr_run}-{i-1} (Key '{upper_keys[i-1]}')")
            curr_run = 1
    if curr_run > 2:
        issues.append(f"Consecutive identical run of {curr_run} at index {len(upper_keys)-curr_run}-{len(upper_keys)-1} (Key '{upper_keys[-1]}')")
            
    # Check repeating cycles (L=2, 3, 4)
    for L in [2, 3, 4]:
        for i in range(len(upper_keys) - 3*L + 1):
            if upper_keys[i:i+L] == upper_keys[i+L:i+2*L] == upper_keys[i+2*L:i+3*L]:
                pattern = "".join(upper_keys[i:i+L])
                issues.append(f"Repeating pattern cycle '{pattern}' repeated 3+ times at index {i}")
                
    # Check quartile distribution
    q_len = max(1, count // 4)
    min_per_q = 1 if count <= 30 else (2 if count <= 60 else 3)
    for q_idx in range(4):
        quarter = upper_keys[q_idx*q_len : (q_idx+1)*q_len if q_idx < 3 else count]
        q_counts = Counter(quarter)
        for k in ["A", "B", "C", "D"]:
            if q_counts[k] < min_per_q:
                issues.append(f"Quartile {q_idx+1} lacks balance: key {k} appears only {q_counts[k]} time(s)")
                
    return len(issues) == 0, issues


def apply_target_key(q: dict, target_key: str) -> dict:
    """
    Safely shifts the correct answer of question q to target_key, maintaining
    bilingual option texts and why_not_others pedagogical alignments.
    """
    target_key = target_key.upper()
    curr_key = q.get("correct_answer", "A").upper()
    if curr_key == target_key:
        return q
        
    idx_map = {"A": 0, "B": 1, "C": 2, "D": 3}
    c_idx = idx_map[curr_key]
    t_idx = idx_map[target_key]
    
    # 1. Swap content in options list
    q["options"][c_idx]["en"], q["options"][t_idx]["en"] = q["options"][t_idx]["en"], q["options"][c_idx]["en"]
    q["options"][c_idx]["ta"], q["options"][t_idx]["ta"] = q["options"][t_idx]["ta"], q["options"][c_idx]["ta"]
    
    # 2. Swap in options_en
    q["options_en"][c_idx], q["options_en"][t_idx] = q["options_en"][t_idx], q["options_en"][c_idx]
    
    # 3. Swap in options_ta
    q["options_ta"][c_idx], q["options_ta"][t_idx] = q["options_ta"][t_idx], q["options_ta"][c_idx]
    
    # 4. Swap in why_not_others
    wno = q.get("why_not_others", {})
    if isinstance(wno, dict) and curr_key in wno and target_key in wno:
        wno[curr_key], wno[target_key] = wno[target_key], wno[curr_key]
        
    # 5. Set correct_answer and answer
    q["correct_answer"] = target_key
    q["answer"] = target_key.lower()
    
    return q


def randomize_and_balance_dataset(
    questions: list,
    target_counts: Optional[Dict[str, int]] = None,
    seed: Optional[int] = None
) -> list:
    """
    Applies a randomized, non-periodic, balanced answer distribution across an entire question list.
    """
    count = len(questions)
    pool = generate_shuffled_key_pool(count, counts=target_counts, seed=seed)
    
    # Pattern audit the pool
    is_valid, issues = audit_answer_pattern(pool, count)
    if not is_valid:
        raise RuntimeError(f"Generated key pool failed pattern audit: {issues}")
        
    balanced = [copy.deepcopy(q) for q in questions]
    for idx, q in enumerate(balanced):
        apply_target_key(q, pool[idx])
        
    return balanced
