# Master Validation & Consolidation Script for Constitutional Amendments MCQs
# Part 1/3 (Core: 50 Easy, 50 Medium, 50 Hard = 150) + GT Verification (100)

import json
import os
import sys

def run_master_validation():
    print("=" * 60)
    print("TNPSC NOVA AI -- CONSTITUTIONAL AMENDMENTS MASTER VALIDATOR")
    print("=" * 60)

    files_to_check = {
        "Easy": ("data/questions/polity/constitutional_amendments_easy.json", 50),
        "Medium": ("data/questions/polity/constitutional_amendments_medium.json", 50),
        "Hard": ("data/questions/polity/constitutional_amendments_hard.json", 50),
        "Grand Test": ("data/questions/polity/constitutional_amendments_grand_test.json", 100)
    }

    all_ids = set()
    all_question_texts = set()
    total_core = 0
    total_gt = 0

    for cat, (filepath, expected_count) in files_to_check.items():
        if not os.path.exists(filepath):
            print(f"[-] ERROR: File {filepath} does not exist!")
            sys.exit(1)

        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        actual_count = len(data)
        print(f"\n[+] Category: {cat}")
        print(f"    File: {filepath}")
        print(f"    Questions Count: {actual_count} (Expected: {expected_count})")

        if actual_count != expected_count:
            print(f"[-] ERROR: Count mismatch in {cat}! Expected {expected_count}, got {actual_count}")
            sys.exit(1)

        if cat in ["Easy", "Medium", "Hard"]:
            total_core += actual_count
        else:
            total_gt += actual_count

        # Check Answer Key Distribution
        from collections import Counter
        ans_dist = Counter(q["correct_answer"] for q in data)
        print(f"    Answer Distribution: {dict(ans_dist)}")

        # Check fields and duplicates
        for i, q in enumerate(data):
            q_id = q.get("id")
            if not q_id:
                print(f"[-] ERROR: Question at index {i} in {cat} missing 'id'")
                sys.exit(1)

            if q_id in all_ids:
                print(f"[-] ERROR: Duplicate ID '{q_id}' found in {cat}!")
                sys.exit(1)
            all_ids.add(q_id)

            q_text_en = q.get("question", {}).get("en", "").strip().lower()
            if not q_text_en:
                print(f"[-] ERROR: Empty English question in {q_id}")
                sys.exit(1)

            if q_text_en in all_question_texts:
                print(f"[-] WARNING: Potential duplicate question text in {q_id}: {q['question']['en'][:50]}...")
            all_question_texts.add(q_text_en)

            # Schema validation
            required_keys = [
                "id", "subject", "topic", "difficulty", "question_type",
                "question", "options", "correct_answer", "explanation",
                "why_not_others", "tnpsc_tip", "revision_fact",
                "source_reference", "bloom_level", "estimated_time_sec",
                "pyq_similarity", "tags"
            ]

            for key in required_keys:
                if key not in q:
                    print(f"[-] ERROR: Question {q_id} missing key '{key}'")
                    sys.exit(1)

            # Check Options
            opts = q.get("options", [])
            if len(opts) != 4:
                print(f"[-] ERROR: Question {q_id} does not have exactly 4 options!")
                sys.exit(1)

            opt_ids = [opt["id"] for opt in opts]
            if opt_ids != ["A", "B", "C", "D"]:
                print(f"[-] ERROR: Question {q_id} option IDs are not A, B, C, D!")
                sys.exit(1)

            if q["correct_answer"] not in ["A", "B", "C", "D"]:
                print(f"[-] ERROR: Question {q_id} correct_answer invalid: {q['correct_answer']}")
                sys.exit(1)

            # Check why_not_others options
            why = q.get("why_not_others", {})
            for opt_key in ["A", "B", "C", "D"]:
                if opt_key not in why:
                    print(f"[-] ERROR: Question {q_id} missing why_not_others for option {opt_key}")
                    sys.exit(1)
                if not why[opt_key].get("en") or not why[opt_key].get("ta"):
                    print(f"[-] ERROR: Question {q_id} option {opt_key} missing en or ta why_not_others explanation")
                    sys.exit(1)

            # Check bilingual fields
            for bf in ["question", "explanation", "tnpsc_tip", "revision_fact"]:
                val = q.get(bf, {})
                if not val.get("en") or not val.get("ta"):
                    print(f"[-] ERROR: Question {q_id} missing bilingual {bf}")
                    sys.exit(1)

    print("\n" + "=" * 60)
    print(f"[+] VALIDATION SUCCESSFUL!")
    print(f"    Core Questions Total: {total_core} (50 Easy, 50 Medium, 50 Hard)")
    print(f"    Grand Test Questions: {total_gt}")
    print(f"    Overall Topic Total:  {total_core + total_gt}")
    print(f"    Unique IDs Checked:   {len(all_ids)}")
    print("=" * 60)

    # Test UI Loader integration
    try:
        from core.question_loader import load_questions
        easy_loaded = load_questions("polity_constitutional_amendments", "easy")
        medium_loaded = load_questions("polity_constitutional_amendments", "medium")
        hard_loaded = load_questions("polity_constitutional_amendments", "hard")
        gt_loaded = load_questions("polity_constitutional_amendments", "grand_test")
        print("\n[+] UI Loader Test Passed:")
        print(f"    Loaded Easy:       {len(easy_loaded)}")
        print(f"    Loaded Medium:     {len(medium_loaded)}")
        print(f"    Loaded Hard:       {len(hard_loaded)}")
        print(f"    Loaded Grand Test: {len(gt_loaded)}")
    except Exception as e:
        print(f"[!] UI Loader Test Warning / Error: {e}")

if __name__ == "__main__":
    run_master_validation()
