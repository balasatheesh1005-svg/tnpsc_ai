# -*- coding: utf-8 -*-
"""
Builder for Part 2B of Constitutional Schedules (75 MCQs):
- 25 Reasoning MCQs (SCH_R_001 to SCH_R_025)
- 25 Match the Following MCQs (SCH_MF_001 to SCH_MF_025)
- 25 Chronology MCQs (SCH_C_001 to SCH_C_025)
"""
import json
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.insert(0, os.path.dirname(__file__))

from sch_mcq_helper import balance_question_keys
from schedules_reasoning_data import get_reasoning_questions
from schedules_match_data import get_match_questions
from schedules_chronology_data import get_chronology_questions

def main():
    reasoning_qs = get_reasoning_questions()
    match_qs = get_match_questions()
    chron_qs = get_chronology_questions()

    print(f"Loaded: Reasoning={len(reasoning_qs)}, Match={len(match_qs)}, Chronology={len(chron_qs)}")
    assert len(reasoning_qs) == 25, f"Expected 25 Reasoning, got {len(reasoning_qs)}"
    assert len(match_qs) == 25, f"Expected 25 Match, got {len(match_qs)}"
    assert len(chron_qs) == 25, f"Expected 25 Chronology, got {len(chron_qs)}"

    # Balance and shuffle answer keys with anti-block rule
    reasoning_balanced = balance_question_keys(reasoning_qs, seed=606)
    match_balanced = balance_question_keys(match_qs, seed=707)
    chron_balanced = balance_question_keys(chron_qs, seed=808)

    out_dir = os.path.join(os.path.dirname(__file__), "..", "data", "questions", "polity")
    os.makedirs(out_dir, exist_ok=True)

    files = [
        ("constitutional_schedules_reasoning.json", reasoning_balanced),
        ("constitutional_schedules_match_the_following.json", match_balanced),
        ("constitutional_schedules_chronology.json", chron_balanced)
    ]

    for fname, data in files:
        fpath = os.path.join(out_dir, fname)
        with open(fpath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Saved {len(data)} questions to {fpath}")

if __name__ == "__main__":
    main()
