import json
import os
import sys

def validate_part2():
    print("============================================================")
    print("TNPSC NOVA AI -- CONSTITUTIONAL AMENDMENTS PART 2 VALIDATOR")
    print("============================================================")

    part2_files = {
        "Statement": ("data/questions/polity/constitutional_amendments_statement.json", 50),
        "Reasoning": ("data/questions/polity/constitutional_amendments_reasoning.json", 25),
        "Chronology": ("data/questions/polity/constitutional_amendments_chronology.json", 25),
        "Match": ("data/questions/polity/constitutional_amendments_match.json", 25),
        "PYQ": ("data/questions/polity/constitutional_amendments_pyq.json", 50)
    }

    all_ids = set()
    total_part2_count = 0

    for cat, (filepath, expected_count) in part2_files.items():
        if not os.path.exists(filepath):
            print(f"[-] ERROR: Missing file {filepath}")
            sys.exit(1)

        with open(filepath, encoding="utf-8") as f:
            qs = json.load(f)

        actual_count = len(qs)
        total_part2_count += actual_count

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

            # Schema validation
            required_keys = [
                "id", "subject", "topic", "difficulty", "question_type",
                "question", "options", "correct_answer", "explanation",
                "why_not_others", "tnpsc_tip", "revision_fact", "source_reference"
            ]
            for rk in required_keys:
                if rk not in q:
                    print(f"[-] ERROR: Missing key '{rk}' in {q_id}")
                    sys.exit(1)

            # Options check
            opts = q["options"]
            if len(opts) != 4:
                print(f"[-] ERROR: Option count != 4 in {q_id}")
                sys.exit(1)

            # Option IDs check
            opt_ids = [o["id"] for o in opts]
            if opt_ids != ["A", "B", "C", "D"]:
                print(f"[-] ERROR: Invalid option IDs {opt_ids} in {q_id}")
                sys.exit(1)

            # Correct answer check
            if q["correct_answer"] not in ["A", "B", "C", "D"]:
                print(f"[-] ERROR: Invalid correct answer {q['correct_answer']} in {q_id}")
                sys.exit(1)

            # Distractor check
            for opt_letter in ["A", "B", "C", "D"]:
                if opt_letter not in q["why_not_others"]:
                    print(f"[-] ERROR: Missing why_not_others for option {opt_letter} in {q_id}")
                    sys.exit(1)

    print("\n============================================================")
    print("[+] PART 2 VALIDATION SUCCESSFUL!")
    print(f"    Part 2 Questions Total: {total_part2_count}")
    print(f"    Statement:  50")
    print(f"    Reasoning:  25")
    print(f"    Chronology: 25")
    print(f"    Match:      25")
    print(f"    PYQ:        50")
    print("============================================================")

    # Check Cumulative Core Total (Part 1 + Part 2)
    part1_files = [
        "data/questions/polity/constitutional_amendments_easy.json",
        "data/questions/polity/constitutional_amendments_medium.json",
        "data/questions/polity/constitutional_amendments_hard.json"
    ]
    p1_total = 0
    for p1f in part1_files:
        with open(p1f, encoding="utf-8") as f:
            p1_total += len(json.load(f))

    cum_total = p1_total + total_part2_count
    print(f"\n[+] Cumulative Core Total: {cum_total} (Expected: 325)")

    # Test UI Question Loader
    from core.question_loader import load_questions
    st_q = load_questions("polity_constitutional_amendments", "statement")
    rs_q = load_questions("polity_constitutional_amendments", "reasoning")
    ch_q = load_questions("polity_constitutional_amendments", "chronology")
    mt_q = load_questions("polity_constitutional_amendments", "match")
    py_q = load_questions("polity_constitutional_amendments", "pyq")

    print("\n[+] UI Question Loader Tests:")
    print(f"    Loaded Statement:  {len(st_q)}")
    print(f"    Loaded Reasoning:  {len(rs_q)}")
    print(f"    Loaded Chronology: {len(ch_q)}")
    print(f"    Loaded Match:      {len(mt_q)}")
    print(f"    Loaded PYQ:        {len(py_q)}")

if __name__ == "__main__":
    validate_part2()
