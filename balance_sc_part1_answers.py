# -*- coding: utf-8 -*-
"""
Answer Key Balancer for Supreme Court Part 1 MCQs
Balances correct answers across A, B, C, D for:
- supreme_court_easy.json (50 questions: A=13, B=13, C=12, D=12)
- supreme_court_medium.json (50 questions: A=13, B=13, C=12, D=12)
- supreme_court_hard.json (50 questions: A=12, B=12, C=13, D=13)
Total 150 questions: A=38, B=38, C=37, D=37
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

def balance_file(filepath, target_pattern):
    with open(filepath, "r", encoding="utf-8") as f:
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

            # 3. Swap why_not_others contents as well
            why = q["why_not_others"]
            old_why_en = why[old_corr]["en"]
            old_why_ta = why[old_corr]["ta"]

            new_why_en = why[new_corr]["en"]
            new_why_ta = why[new_corr]["ta"]

            # Fix checkmarks / crossmarks
            def set_prefix(text, is_correct):
                clean_text = text.replace("✅ ", "").replace("❌ ", "").strip()
                return f"✅ {clean_text}" if is_correct else f"❌ {clean_text}"

            why[old_corr]["en"] = set_prefix(new_why_en, False)
            why[old_corr]["ta"] = set_prefix(new_why_ta, False)

            why[new_corr]["en"] = set_prefix(old_why_en, True)
            why[new_corr]["ta"] = set_prefix(old_why_ta, True)

            # 4. Set new correct answer
            q["correct_answer"] = new_corr

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)

    print(f"✅ Successfully balanced {filepath}")

def main():
    base_dir = "data/questions/polity"
    
    # 50 targets for Easy (A=13, B=13, C=12, D=12) - pseudo random order
    easy_target = ["A", "B", "C", "D", "B", "A", "D", "C", "A", "C", "B", "D", "D", "A", "B", "C", "A", "B", "C", "D", "B", "D", "A", "C", "C", "A", "B", "D", "A", "B", "C", "D", "B", "A", "D", "C", "A", "C", "B", "D", "A", "B", "C", "D", "B", "A", "C", "D", "A", "B"]
    
    # 50 targets for Medium (A=13, B=13, C=12, D=12) - pseudo random order
    medium_target = ["C", "D", "A", "B", "D", "C", "B", "A", "B", "A", "D", "C", "C", "B", "A", "D", "B", "A", "D", "C", "A", "C", "B", "D", "D", "B", "A", "C", "B", "A", "C", "D", "C", "D", "A", "B", "D", "C", "B", "A", "A", "B", "C", "D", "A", "B", "C", "D", "A", "B"]

    # 50 targets for Hard (A=12, B=12, C=13, D=13) - pseudo random order
    hard_target = ["D", "C", "B", "A", "C", "D", "A", "B", "A", "B", "C", "D", "B", "A", "D", "C", "D", "C", "B", "A", "C", "D", "A", "B", "A", "D", "C", "B", "C", "D", "A", "B", "D", "C", "B", "A", "B", "A", "D", "C", "C", "D", "A", "B", "C", "D", "A", "B", "C", "D"]

    balance_file(os.path.join(base_dir, "supreme_court_easy.json"), easy_target)
    balance_file(os.path.join(base_dir, "supreme_court_medium.json"), medium_target)
    balance_file(os.path.join(base_dir, "supreme_court_hard.json"), hard_target)

if __name__ == "__main__":
    main()
