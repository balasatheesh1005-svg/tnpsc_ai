# -*- coding: utf-8 -*-
"""
Answer Key Balancer for Supreme Court Part 2 MCQs (175 Questions)
Shuffles answer keys naturally to prevent repeating ABCD patterns.
Balances correct answers across A, B, C, D for:
- supreme_court_statement.json (50 questions: A=13, B=13, C=12, D=12)
- supreme_court_reasoning.json (25 questions: A=6, B=6, C=7, D=6)
- supreme_court_match.json (25 questions: A=6, B=6, C=6, D=7)
- supreme_court_chronology.json (25 questions: A=6, B=7, C=6, D=6)
- supreme_court_pyq.json (50 questions: A=13, B=12, C=12, D=13)
Total 175 questions: A=44, B=44, C=43, D=44
"""

import json
import os
import sys
import random

sys.stdout.reconfigure(encoding='utf-8')

def generate_shuffled_pattern(count_dict):
    items = []
    for letter, count in count_dict.items():
        items.extend([letter] * count)
    
    random.seed(42)  # Fixed seed for reproducibility
    while True:
        random.shuffle(items)
        pattern_str = "".join(items)
        if "ABCDABCD" not in pattern_str and "DCBADCBA" not in pattern_str:
            return items

def balance_file(filepaths, target_pattern):
    primary_path = filepaths[0]
    with open(primary_path, "r", encoding="utf-8") as f:
        questions = json.load(f)

    assert len(questions) == len(target_pattern), f"Length mismatch: {len(questions)} vs {len(target_pattern)}"

    for idx, q in enumerate(questions):
        old_corr = q["correct_answer"]
        new_corr = target_pattern[idx]

        if old_corr != new_corr:
            # 1. Swap option contents between old_corr and new_corr
            opts_dict = {o["id"]: o for o in q["options"]}
            
            old_opt_text_en = opts_dict[old_corr]["en"]
            old_opt_text_ta = opts_dict[old_corr]["ta"]

            new_opt_text_en = opts_dict[new_corr]["en"]
            new_opt_text_ta = opts_dict[new_corr]["ta"]

            # Swap text contents
            opts_dict[old_corr]["en"] = new_opt_text_en
            opts_dict[old_corr]["ta"] = new_opt_text_ta

            opts_dict[new_corr]["en"] = old_opt_text_en
            opts_dict[new_corr]["ta"] = old_opt_text_ta

            # 2. Update options list & flat options_en / options_ta
            q["options"] = [opts_dict["A"], opts_dict["B"], opts_dict["C"], opts_dict["D"]]
            q["options_en"] = [o["en"] for o in q["options"]]
            q["options_ta"] = [o["ta"] for o in q["options"]]

            # 3. Swap why_not_others contents
            why = q["why_not_others"]
            old_why_en = why[old_corr]["en"]
            old_why_ta = why[old_corr]["ta"]

            new_why_en = why[new_corr]["en"]
            new_why_ta = why[new_corr]["ta"]

            def set_prefix(text, is_correct):
                clean_text = text.replace("✅ ", "").replace("❌ ", "").strip()
                return f"✅ {clean_text}" if is_correct else f"❌ {clean_text}"

            why[old_corr]["en"] = set_prefix(new_why_en, False)
            why[old_corr]["ta"] = set_prefix(new_why_ta, False)

            why[new_corr]["en"] = set_prefix(old_why_en, True)
            why[new_corr]["ta"] = set_prefix(old_why_ta, True)

            # 4. Set new correct answer
            q["correct_answer"] = new_corr

    # Save to all specified filepaths
    for p in filepaths:
        with open(p, "w", encoding="utf-8") as f:
            json.dump(questions, f, ensure_ascii=False, indent=2)
        print(f"✅ Saved -> {p}")

def main():
    base_dir = "data/questions/polity"
    
    # Statement (50: A=13, B=13, C=12, D=12)
    stmt_target = generate_shuffled_pattern({"A": 13, "B": 13, "C": 12, "D": 12})
    
    # Reasoning (25: A=6, B=6, C=7, D=6)
    reas_target = generate_shuffled_pattern({"A": 6, "B": 6, "C": 7, "D": 6})

    # Match (25: A=6, B=6, C=6, D=7)
    match_target = generate_shuffled_pattern({"A": 6, "B": 6, "C": 6, "D": 7})

    # Chronology (25: A=6, B=7, C=6, D=6)
    chrono_target = generate_shuffled_pattern({"A": 6, "B": 7, "C": 6, "D": 6})

    # PYQ (50: A=13, B=12, C=12, D=13)
    pyq_target = generate_shuffled_pattern({"A": 13, "B": 12, "C": 12, "D": 13})

    balance_file([os.path.join(base_dir, "supreme_court_statement.json"), os.path.join(base_dir, "supreme_court_statement_based.json")], stmt_target)
    balance_file([os.path.join(base_dir, "supreme_court_reasoning.json"), os.path.join(base_dir, "supreme_court_assertion_reason.json")], reas_target)
    balance_file([os.path.join(base_dir, "supreme_court_match.json"), os.path.join(base_dir, "supreme_court_match_the_following.json")], match_target)
    balance_file([os.path.join(base_dir, "supreme_court_chronology.json")], chrono_target)
    balance_file([os.path.join(base_dir, "supreme_court_pyq.json"), os.path.join(base_dir, "supreme_court_pyq_practice.json")], pyq_target)

if __name__ == "__main__":
    main()
