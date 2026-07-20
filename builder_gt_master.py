import json
import os
from gt_part1 import get_part1_questions
from gt_part2 import get_part2_questions
from gt_part3 import get_part3_questions
from gt_part4 import get_part4_questions

def build_grand_test_repo():
    print("Gathering questions from all 4 modules...")
    p1 = get_part1_questions()
    p2 = get_part2_questions()
    p3 = get_part3_questions()
    p4 = get_part4_questions()
    
    all_questions = p1 + p2 + p3 + p4
    
    print(f"Total questions gathered: {len(all_questions)}")
    
    # Audit checks
    ans_counts = {"A": 0, "B": 0, "C": 0, "D": 0}
    diff_counts = {}
    type_counts = {}
    multi_act_count = 0
    
    for i, q in enumerate(all_questions, 1):
        # Enforce exact ID format
        q["id"] = f"HB_GT_{i:03d}"
        
        ans = q["correct_answer"]
        ans_counts[ans] = ans_counts.get(ans, 0) + 1
        
        diff = q["difficulty"]
        diff_counts[diff] = diff_counts.get(diff, 0) + 1
        
        qtype = q["question_type"]
        type_counts[qtype] = type_counts.get(qtype, 0) + 1
        
        if "Multi-Act" in qtype or "Multi-Act" in q.get("tags", []):
            multi_act_count += 1

    print("\n--- DATASET AUDIT RESULTS ---")
    print(f"Total Count: {len(all_questions)}")
    print(f"Answer Key Balance: {ans_counts}")
    print(f"Difficulty Breakdown: {diff_counts}")
    print(f"Question Type Breakdown: {type_counts}")
    print(f"Multi-Act Questions Count: {multi_act_count}")

    output_dir = r"c:\Users\Home\Desktop\tnpsc_ai\data\questions\polity"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "historical_background_grand_test.json")

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(all_questions, f, ensure_ascii=False, indent=2)

    print(f"\nSUCCESSFULLY BUILT GRAND TEST REPOSITORY AT:\n{output_path}")

if __name__ == "__main__":
    build_grand_test_repo()
