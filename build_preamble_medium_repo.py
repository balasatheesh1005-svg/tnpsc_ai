# build_preamble_medium_repo.py
import json
import os
from collections import Counter
from preamble_medium_q1_25 import get_medium_q1_25
from preamble_medium_q26_50 import get_medium_q26_50

def assemble_and_save_medium():
    q1_25 = get_medium_q1_25()
    q26_50 = get_medium_q26_50()

    all_qs = q1_25 + q26_50
    print(f"Total Questions Assembled: {len(all_qs)}")
    assert len(all_qs) == 50, f"Expected 50 questions, got {len(all_qs)}"

    # Audit IDs
    ids = [q["id"] for q in all_qs]
    unique_ids = set(ids)
    assert len(unique_ids) == 50, f"Duplicate IDs found! Unique count = {len(unique_ids)}"

    # Audit Answer Distribution
    answers = [q["correct_answer"] for q in all_qs]
    ans_counts = Counter(answers)
    print("\nAnswer Key Distribution:")
    for key in sorted(ans_counts.keys()):
        print(f"   Option {key}: {ans_counts[key]}")

    # Audit dual-schema keys
    for i, q in enumerate(all_qs):
        req_keys = [
            "id", "subject", "topic", "difficulty", "question_type",
            "question", "options", "correct_answer", "explanation",
            "why_not_others", "tnpsc_tip", "revision_fact", "source_reference",
            "bloom_level", "estimated_time_sec", "pyq_similarity", "tags",
            "question_en", "question_ta", "options_en", "options_ta",
            "answer", "explanation_en", "explanation_ta"
        ]
        for rk in req_keys:
            assert rk in q, f"Question {q['id']} missing key: {rk}"

    out_dir = r"c:\Users\Home\Desktop\tnpsc_ai\data\questions\polity"
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "preamble_medium.json")

    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(all_qs, f, ensure_ascii=False, indent=2)

    print(f"\nSUCCESSFULLY SAVED PREAMBLE MEDIUM 50 REPOSITORY AT:")
    print(f"   {out_file}")

if __name__ == "__main__":
    assemble_and_save_medium()
