# -*- coding: utf-8 -*-
"""
Builder for Part 2A of Constitutional Schedules (100 MCQs):
- 50 Statement-based MCQs (SCH_S_001 to SCH_S_050)
- 50 PYQ MCQs (SCH_PYQ_001 to SCH_PYQ_050)
"""
import json
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.insert(0, os.path.dirname(__file__))

from sch_mcq_helper import balance_question_keys
from schedules_statement_data import get_statement_questions
from schedules_pyq_data import get_pyq_questions

def main():
    statement_qs = get_statement_questions()
    pyq_qs = get_pyq_questions()

    print(f"Loaded: Statement={len(statement_qs)}, PYQ={len(pyq_qs)}")
    assert len(statement_qs) == 50, f"Expected 50 Statement, got {len(statement_qs)}"
    assert len(pyq_qs) == 50, f"Expected 50 PYQ, got {len(pyq_qs)}"

    # Balance and shuffle answer keys with anti-block rule
    statement_balanced = balance_question_keys(statement_qs, seed=404)
    pyq_balanced = balance_question_keys(pyq_qs, seed=505)

    out_dir = os.path.join(os.path.dirname(__file__), "..", "data", "questions", "polity")
    os.makedirs(out_dir, exist_ok=True)

    files = [
        ("constitutional_schedules_statement_based.json", statement_balanced),
        ("constitutional_schedules_pyq.json", pyq_balanced)
    ]

    for fname, data in files:
        fpath = os.path.join(out_dir, fname)
        with open(fpath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Saved {len(data)} questions to {fpath}")

if __name__ == "__main__":
    main()
