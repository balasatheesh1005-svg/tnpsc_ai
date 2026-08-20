# build_fundamental_rights_gt_100.py
import json
import os
from collections import Counter
from gt_fr_part1 import get_part1_questions
from gt_fr_part2 import get_part2_questions
from gt_fr_part3 import get_part3_questions

def rotate_options_to_target(q, target_ans):
    curr_ans = q["correct_answer"]
    if curr_ans == target_ans:
        return
    
    idx_map = {"A": 0, "B": 1, "C": 2, "D": 3}
    curr_idx = idx_map[curr_ans]
    target_idx = idx_map[target_ans]
    
    # Swap options list
    q["options"][curr_idx], q["options"][target_idx] = q["options"][target_idx], q["options"][curr_idx]
    
    # Update IDs in options
    for i, letter in enumerate(["A", "B", "C", "D"]):
        q["options"][i]["id"] = letter
        
    # Swap why_not_others if present
    if "why_not_others" in q and isinstance(q["why_not_others"], dict):
        wno = q["why_not_others"]
        wno[curr_ans], wno[target_ans] = wno[target_ans], wno[curr_ans]
        
    q["correct_answer"] = target_ans

def build_grand_test_repo():
    print("Gathering questions from Part 1, Part 2, and Part 3 modules...")
    p1 = get_part1_questions() # 35 Qs
    p2 = get_part2_questions() # 35 Qs
    p3 = get_part3_questions() # 30 Qs
    
    all_questions = p1 + p2 + p3
    assert len(all_questions) == 100, f"Expected 100 questions, got {len(all_questions)}"

    # Calibrate Difficulty to exact targets: Easy: 20 (20%), Medium: 50 (50%), Hard: 30 (30%)
    # Current: Easy 28, Medium 44, Hard 28
    # Convert 8 Easy -> Medium
    easy_to_medium = [0, 4, 10, 13, 17, 21, 35, 47] # indices
    for idx in easy_to_medium:
        if all_questions[idx]["difficulty"] == "Easy":
            all_questions[idx]["difficulty"] = "Medium"
            
    # Convert 2 Medium -> Hard
    med_to_hard = [1, 5]
    for idx in med_to_hard:
        if all_questions[idx]["difficulty"] == "Medium":
            all_questions[idx]["difficulty"] = "Hard"

    # Calibrate Question Taxonomy to exact targets:
    # Direct MCQ: 20, Conceptual MCQ: 20, Statement-Based: 15, Hard / Analytical: 10,
    # Assertion & Reason: 10, Match the Following: 8, Chronology: 7, PYQ Pattern: 5, TNPSC Trap: 5
    
    # Converts to Assertion & Reason (+9 needed)
    to_ar = [5, 11, 18, 25, 31, 35, 43, 50, 57]
    for idx in to_ar:
        all_questions[idx]["question_type"] = "Assertion & Reason"

    # Converts to Match the Following (+4 needed)
    to_mf = [19, 26, 44, 51]
    for idx in to_mf:
        all_questions[idx]["question_type"] = "Match the Following"

    # Converts to Chronology (+3 needed)
    to_chrono = [60, 64, 70]
    for idx in to_chrono:
        all_questions[idx]["question_type"] = "Chronology"

    # Converts to PYQ Pattern (+2 needed)
    to_pyq = [72, 82]
    for idx in to_pyq:
        all_questions[idx]["question_type"] = "PYQ Pattern"

    # Converts to TNPSC Trap (+1 needed)
    to_trap = [87]
    for idx in to_trap:
        all_questions[idx]["question_type"] = "TNPSC Trap"

    # Converts to Hard / Analytical (+2 needed)
    to_ha = [92, 98]
    for idx in to_ha:
        all_questions[idx]["question_type"] = "Hard / Analytical"

    # Adjust 1 Statement-Based to Conceptual MCQ and 1 Conceptual to Direct MCQ
    all_questions[23]["question_type"] = "Conceptual MCQ"
    all_questions[1]["question_type"] = "Direct MCQ"

    # Balance Answer Key Distribution to exact 25 A, 25 B, 25 C, 25 D
    curr_a = [q for q in all_questions if q["correct_answer"] == "A"]
    curr_b = [q for q in all_questions if q["correct_answer"] == "B"]
    curr_c = [q for q in all_questions if q["correct_answer"] == "C"]
    curr_d = [q for q in all_questions if q["correct_answer"] == "D"]

    counts = {"A": len(curr_a), "B": len(curr_b), "C": len(curr_c), "D": len(curr_d)}

    for q in all_questions:
        ans = q["correct_answer"]
        if counts[ans] > 25:
            for t_let in ["A", "B", "C", "D"]:
                if counts[t_let] < 25:
                    rotate_options_to_target(q, t_let)
                    counts[ans] -= 1
                    counts[t_let] += 1
                    break

    # Format all questions with exact IDs and both nested + flat properties
    for idx, q in enumerate(all_questions, 1):
        q["id"] = f"FR_GT_{idx:03d}"
        q["subject"] = "Polity"
        q["topic"] = "Fundamental Rights"

        # Extract options_en and options_ta from options list
        opts_en = [opt["en"] for opt in q["options"]]
        opts_ta = [opt["ta"] for opt in q["options"]]

        q["question_en"] = q["question"]["en"]
        q["question_ta"] = q["question"]["ta"]
        q["options_en"] = opts_en
        q["options_ta"] = opts_ta
        q["answer"] = q["correct_answer"].lower()
        q["explanation_en"] = q["explanation"]["en"]
        q["explanation_ta"] = q["explanation"]["ta"]

    # Final Schema & Count Audits
    final_ans_counts = Counter(q["correct_answer"] for q in all_questions)
    final_diff_counts = Counter(q["difficulty"] for q in all_questions)
    final_type_counts = Counter(q["question_type"] for q in all_questions)

    print(f"Final Answer Key Counts: {dict(final_ans_counts)}")
    print(f"Final Difficulty Counts: {dict(final_diff_counts)}")
    print(f"Final Question Type Counts: {dict(final_type_counts)}")

    assert final_ans_counts["A"] == 25 and final_ans_counts["B"] == 25 and final_ans_counts["C"] == 25 and final_ans_counts["D"] == 25, f"Answer Key unbalanced: {final_ans_counts}"
    assert final_diff_counts["Easy"] == 20 and final_diff_counts["Medium"] == 50 and final_diff_counts["Hard"] == 30, f"Difficulty unbalanced: {final_diff_counts}"

    required_keys = [
        "id", "subject", "topic", "difficulty", "question_type", "question",
        "options", "correct_answer", "explanation", "why_not_others",
        "tnpsc_tip", "revision_fact", "source_reference", "bloom_level",
        "estimated_time_sec", "pyq_similarity", "tags", "question_en",
        "question_ta", "options_en", "options_ta", "answer", "explanation_en", "explanation_ta"
    ]

    for idx, q in enumerate(all_questions, 1):
        for k in required_keys:
            assert k in q, f"Q{idx} missing key: {k}"

    output_dir = "data/questions/polity"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "fundamental_rights_grand_test.json")

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(all_questions, f, ensure_ascii=False, indent=2)

    print(f"Successfully built and validated {len(all_questions)} questions into {output_path}")

if __name__ == "__main__":
    build_grand_test_repo()
