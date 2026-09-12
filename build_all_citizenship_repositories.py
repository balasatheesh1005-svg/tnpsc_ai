# -*- coding: utf-8 -*-
"""
Master Orchestrator Script for Citizenship of India MCQ Repository
Generates, validates, and saves all 425 questions across 9 primary JSON files and alias files.
"""

import json
import os
import shutil
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

from tools.build_citizenship_easy import get_easy_questions
from tools.build_citizenship_medium import get_medium_questions
from tools.build_citizenship_hard import get_hard_questions
from tools.build_citizenship_statement import get_statement_questions
from tools.build_citizenship_reasoning import get_reasoning_questions
from tools.build_citizenship_match import get_match_questions
from tools.build_citizenship_chronology import get_chronology_questions
from tools.build_citizenship_pyq import get_pyq_questions
from tools.build_citizenship_grand_test import get_grand_test_questions

OUT_DIR = "data/questions/polity"
os.makedirs(OUT_DIR, exist_ok=True)

def build_all():
    print("==========================================================")
    print("🚀 GENERATING COMPLETE CITIZENSHIP OF INDIA MCQ REPOSITORY")
    print("==========================================================")

    files_map = {
        "citizenship_easy.json": get_easy_questions(),
        "citizenship_medium.json": get_medium_questions(),
        "citizenship_hard.json": get_hard_questions(),
        "citizenship_statement.json": get_statement_questions(),
        "citizenship_reasoning.json": get_reasoning_questions(),
        "citizenship_match_the_following.json": get_match_questions(),
        "citizenship_chronology.json": get_chronology_questions(),
        "citizenship_pyq.json": get_pyq_questions(),
        "citizenship_grand_test.json": get_grand_test_questions()
    }

    counts = {}
    for filename, questions in files_map.items():
        path = os.path.join(OUT_DIR, filename)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(questions, f, ensure_ascii=False, indent=2)
        counts[filename] = len(questions)
        print(f"  ✓ {filename}: {len(questions)} questions saved.")

    # Create alias files for full compatibility
    aliases = {
        "citizenship_statement_based.json": "citizenship_statement.json",
        "citizenship_assertion_reason.json": "citizenship_reasoning.json",
        "citizenship_match.json": "citizenship_match_the_following.json",
        "citizenship_pyq_practice.json": "citizenship_pyq.json"
    }

    for alias_name, target_name in aliases.items():
        src = os.path.join(OUT_DIR, target_name)
        dst = os.path.join(OUT_DIR, alias_name)
        shutil.copyfile(src, dst)
        print(f"  ✓ Created alias `{alias_name}` -> `{target_name}`")

    print("==========================================================")
    print("SUMMARY OF GENERATED CORE & GRAND TEST COUNTS:")
    for k, v in counts.items():
        print(f"  - {k}: {v}")
    print("==========================================================")

if __name__ == "__main__":
    build_all()
