import json
import os
import sys

def validate_parliament_part1():
    print("============================================================")
    print("TNPSC NOVA AI -- PARLIAMENT OF INDIA PART 1 MASTER VALIDATOR")
    print("============================================================")

    files_map = {
        "Easy": ("data/questions/polity/parliament_easy.json", 50),
        "Medium": ("data/questions/polity/parliament_medium.json", 50),
        "Hard": ("data/questions/polity/parliament_hard.json", 50)
    }

    all_ids = set()
    total_count = 0

    for cat, (filepath, expected_count) in files_map.items():
        if not os.path.exists(filepath):
            print(f"[-] ERROR: Missing file {filepath}")
            sys.exit(1)

        with open(filepath, encoding="utf-8") as f:
            qs = json.load(f)

        actual_count = len(qs)
        total_count += actual_count

        from collections import Counter
        ans_counts = dict(Counter(q["correct_answer"] for q in qs))

        print(f"\n[+] Category: {cat}")
        print(f"    File: {filepath}")
        print(f"    Questions Count: {actual_count} (Expected: {expected_count})")
        print(f"    Answer Distribution: {ans_counts}")

        if actual_count != expected_count:
            print(f"[-] ERROR: Count mismatch in {cat}! Expected {expected_count}, got {actual_count}")
            sys.exit(1)

        for q in qs:
            q_id = q["id"]
            if q_id in all_ids:
                print(f"[-] ERROR: Duplicate question ID {q_id}")
                sys.exit(1)
            all_ids.add(q_id)

            required_keys = [
                "id", "subject", "topic", "difficulty", "question_type",
                "question", "options", "correct_answer", "explanation",
                "why_not_others", "tnpsc_tip", "revision_fact", "source_reference"
            ]
            for rk in required_keys:
                if rk not in q:
                    print(f"[-] ERROR: Missing key '{rk}' in {q_id}")
                    sys.exit(1)

            opts = q["options"]
            if len(opts) != 4:
                print(f"[-] ERROR: Option count != 4 in {q_id}")
                sys.exit(1)

            opt_ids = [o["id"] for o in opts]
            if opt_ids != ["A", "B", "C", "D"]:
                print(f"[-] ERROR: Invalid option IDs {opt_ids} in {q_id}")
                sys.exit(1)

            if q["correct_answer"] not in ["A", "B", "C", "D"]:
                print(f"[-] ERROR: Invalid correct answer {q['correct_answer']} in {q_id}")
                sys.exit(1)

            for opt_letter in ["A", "B", "C", "D"]:
                if opt_letter not in q["why_not_others"]:
                    print(f"[-] ERROR: Missing why_not_others for option {opt_letter} in {q_id}")
                    sys.exit(1)

    print("\n============================================================")
    print("[+] PARLIAMENT PART 1 VALIDATION SUCCESSFUL!")
    print(f"    Core Questions Total: {total_count} (50 Easy, 50 Medium, 50 Hard)")
    print(f"    Unique IDs Checked:   {len(all_ids)}")
    print("============================================================")

    # Test UI Question Loader
    sys.path.insert(0, ".")
    from core.question_loader import load_questions
    easy_loaded = len(load_questions("polity_parliament", "easy"))
    med_loaded = len(load_questions("polity_parliament", "medium"))
    hard_loaded = len(load_questions("polity_parliament", "hard"))

    print("\n[+] UI Question Loader Tests:")
    print(f"    Loaded Easy:   {easy_loaded}")
    print(f"    Loaded Medium: {med_loaded}")
    print(f"    Loaded Hard:   {hard_loaded}")

if __name__ == "__main__":
    validate_parliament_part1()
