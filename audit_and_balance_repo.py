import json
import random
import os

def audit_and_balance():
    json_path = r"c:\Users\Home\Desktop\tnpsc_ai\data\questions\polity\historical_background_grand_test.json"
    with open(json_path, encoding="utf-8") as f:
        questions = json.load(f)

    print(f"Loaded {len(questions)} questions.")

    # 1. Audit & Fix Multi-Act Tags
    # Check each question to see if it tests multiple Acts (e.g. mentions multiple years like 1773, 1784, 1813, 1833, 1853, 1858, 1861, 1892, 1909, 1919, 1935, 1947, or mentions multiple Acts).
    multi_act_count = 0
    years = ["1773", "1781", "1784", "1793", "1813", "1833", "1853", "1858", "1861", "1892", "1909", "1919", "1927", "1932", "1935", "1947"]
    
    for q in questions:
        q_text = q["question"]["en"] + " " + q["explanation"]["en"]
        year_matches = set()
        for y in years:
            if y in q_text:
                year_matches.add(y)
        
        # If question mentions 2+ distinct years or has comparative keywords, tag as Multi-Act Integration
        is_multi = len(year_matches) >= 2 or "Multi-Act" in q["question_type"] or "Comparative" in q["question_type"] or "Evolution" in q["question_type"] or "versus" in q_text or "vs" in q_text
        if is_multi:
            multi_act_count += 1
            if "Multi-Act Integration" not in q["tags"]:
                q["tags"].append("Multi-Act Integration")

    print(f"Total Multi-Act Questions: {multi_act_count} ({multi_act_count}%)")

    # 2. Evenly Balance Answer Choices across A, B, C, D (25 each)
    target_answers = ["A"] * 25 + ["B"] * 25 + ["C"] * 25 + ["D"] * 25
    random.seed(100)
    random.shuffle(target_answers)

    for i, q in enumerate(questions):
        desired_ans = target_answers[i]
        curr_ans = q["correct_answer"]
        
        opts = q["options"] # list of dicts [{"id": "A", "en": "...", "ta": "..."}, ...]
        wno = q["why_not_others"] # {"A": {"en": "...", "ta": "..."}, ...}

        # Find the correct option dict
        correct_opt_dict = None
        for o in opts:
            if o["id"] == curr_ans:
                correct_opt_dict = o
                break
        
        # Other 3 option dicts
        other_opts = [o for o in opts if o["id"] != curr_ans]
        
        # Assign new letters
        letters = ["A", "B", "C", "D"]
        other_letters = [l for l in letters if l != desired_ans]
        
        new_opts_map = {} # letter -> opt_dict
        new_opts_map[desired_ans] = correct_opt_dict
        
        for idx, o_dict in enumerate(other_opts):
            new_opts_map[other_letters[idx]] = o_dict

        # Build new options list and why_not_others
        new_options_list = []
        new_options_en = []
        new_options_ta = []
        new_wno = {}

        for l in letters:
            orig_dict = new_opts_map[l]
            orig_id = orig_dict["id"]
            
            # create updated option dict
            updated_opt = {
                "id": l,
                "en": orig_dict["en"],
                "ta": orig_dict["ta"]
            }
            new_options_list.append(updated_opt)
            new_options_en.append(orig_dict["en"])
            new_options_ta.append(orig_dict["ta"])
            
            # Map why_not_others for this letter
            if orig_id in wno:
                new_wno[l] = wno[orig_id]
            else:
                new_wno[l] = {"en": f"Evaluation of Option {l}.", "ta": f"தெரிவு {l}-ன் மதிப்பீடு."}

        q["options"] = new_options_list
        q["options_en"] = new_options_en
        q["options_ta"] = new_options_ta
        q["correct_answer"] = desired_ans
        q["answer"] = desired_ans.lower()
        q["why_not_others"] = new_wno

    # Final Audit Check
    ans_counts = {"A": 0, "B": 0, "C": 0, "D": 0}
    diff_counts = {}
    type_counts = {}
    
    for q in questions:
        ans_counts[q["correct_answer"]] += 1
        diff_counts[q["difficulty"]] = diff_counts.get(q["difficulty"], 0) + 1
        type_counts[q["question_type"]] = type_counts.get(q["question_type"], 0) + 1

    print("\n--- BALANCED DATASET AUDIT ---")
    print(f"Total Questions: {len(questions)}")
    print(f"Answer Key Distribution: {ans_counts}")
    print(f"Difficulty Breakdown: {diff_counts}")
    print(f"Question Types: {type_counts}")

    # Write back to file
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)

    print("\nSUCCESSFULLY BALANCED AND WRITTEN GRAND TEST REPOSITORY.")

if __name__ == "__main__":
    audit_and_balance()
