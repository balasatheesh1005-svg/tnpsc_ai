# -*- coding: utf-8 -*-
"""
Comprehensive Validation Script for Citizenship of India MCQ Repository
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

from core.question_loader import load_questions

FILES_EXPECTED = {
    "citizenship_easy.json": 50,
    "citizenship_medium.json": 50,
    "citizenship_hard.json": 50,
    "citizenship_statement.json": 50,
    "citizenship_reasoning.json": 25,
    "citizenship_match_the_following.json": 25,
    "citizenship_chronology.json": 25,
    "citizenship_pyq.json": 50,
    "citizenship_grand_test.json": 100
}

def run_validation():
    print("================================================================================")
    print("🚀 RUNNING COMPREHENSIVE VALIDATION FOR CITIZENSHIP OF INDIA MCQ REPOSITORY")
    print("================================================================================")

    all_ids = set()
    total_questions = 0
    core_questions = 0
    gt_questions = 0
    all_parts_cited = set()
    distribution_report = {}

    schema_pass = True
    dup_pass = True
    bilingual_pass = True
    notes_pass = True
    loader_pass = True

    for filename, expected_count in FILES_EXPECTED.items():
        filepath = os.path.join("data/questions/polity", filename)
        if not os.path.exists(filepath):
            print(f"❌ Missing file: {filepath}")
            schema_pass = False
            continue

        try:
            with open(filepath, encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            print(f"❌ Invalid JSON in {filepath}: {e}")
            schema_pass = False
            continue

        actual_count = len(data)
        if actual_count != expected_count:
            print(f"❌ Count mismatch in {filename}: Expected {expected_count}, got {actual_count}")
            schema_pass = False

        if filename == "citizenship_grand_test.json":
            gt_questions += actual_count
        else:
            core_questions += actual_count
        total_questions += actual_count

        answer_counts = {"A": 0, "B": 0, "C": 0, "D": 0}

        for q in data:
            qid = q.get("id")
            if not qid:
                print(f"❌ Question missing ID in {filename}")
                schema_pass = False
            elif qid in all_ids:
                print(f"❌ Duplicate Question ID found: {qid}")
                dup_pass = False
            else:
                all_ids.add(qid)

            # Check options count
            options = q.get("options", [])
            if len(options) != 4:
                print(f"❌ Question {qid} does not have 4 options.")
                schema_pass = False

            # Check correct answer
            ans = q.get("correct_answer")
            if ans not in ["A", "B", "C", "D"]:
                print(f"❌ Question {qid} has invalid correct_answer: {ans}")
                schema_pass = False
            else:
                answer_counts[ans] += 1

            # Check bilingual fields
            q_en = q.get("question", {}).get("en")
            q_ta = q.get("question", {}).get("ta")
            exp_en = q.get("explanation", {}).get("en")
            exp_ta = q.get("explanation", {}).get("ta")
            tip_en = q.get("tnpsc_tip", {}).get("en")
            tip_ta = q.get("tnpsc_tip", {}).get("ta")
            rev_en = q.get("revision_fact", {}).get("en")
            rev_ta = q.get("revision_fact", {}).get("ta")

            if not (q_en and q_ta and exp_en and exp_ta and tip_en and tip_ta and rev_en and rev_ta):
                print(f"❌ Question {qid} has missing or empty bilingual text.")
                bilingual_pass = False

            why_not = q.get("why_not_others", {})
            if len(why_not) != 4:
                print(f"❌ Question {qid} why_not_others does not contain 4 entries.")
                bilingual_pass = False

            # Collect source references
            sources = q.get("source_reference", [])
            for src in sources:
                if "Part 1" in src:
                    all_parts_cited.add("Part 1")
                if "Part 2" in src:
                    all_parts_cited.add("Part 2")
                if "Part 3" in src:
                    all_parts_cited.add("Part 3")

        distribution_report[filename] = answer_counts
        print(f"  ✓ {filename}: Count={actual_count}/{expected_count} | Answers: {answer_counts}")

    print("\n--------------------------------------------------------------------------------")
    print(f"CORE QUESTIONS   : {core_questions} / 325")
    print(f"GRAND TEST       : {gt_questions} / 100")
    print(f"OVERALL TOTAL    : {total_questions} / 425")
    print("--------------------------------------------------------------------------------")

    # Check Notes Parts Coverage
    if len(all_parts_cited) < 3:
        print(f"❌ Notes Part Coverage incomplete. Cited parts: {all_parts_cited}")
        notes_pass = False
    else:
        print(f"  ✓ Notes Parts Coverage Verified: All 3 note parts cited ({sorted(list(all_parts_cited))})")

    # Practice UI Loader Resolution Test
    print("\n--------------------------------------------------------------------------------")
    print("🔍 TESTING PRACTICE UI QUESTION LOADER RESOLUTION (core.question_loader)")
    print("--------------------------------------------------------------------------------")

    levels = ["easy", "medium", "hard", "statement", "reasoning", "match_the_following", "chronology", "pyq", "grand_test"]
    for lvl in levels:
        res = load_questions("polity_citizenship", lvl)
        if not res or len(res) == 0:
            print(f"❌ load_questions failed for repository_id='polity_citizenship', level='{lvl}'")
            loader_pass = False
        else:
            print(f"  ✓ load_questions('polity_citizenship', '{lvl}') -> Successfully loaded {len(res)} MCQs.")

    print("\n================================================================================")
    print("FINAL CITIZENSHIP MCQ VALIDATION SUMMARY:")
    print("================================================================================")
    print(f"  Schema Validation:           {'PASS' if schema_pass else 'FAIL'}")
    print(f"  Duplicate ID Check:          {'PASS' if dup_pass else 'FAIL'}")
    print(f"  Bilingual Content Check:     {'PASS' if bilingual_pass else 'FAIL'}")
    print(f"  Notes Parts 1, 2, 3 Cover:   {'PASS' if notes_pass else 'FAIL'}")
    print(f"  Practice UI Loader Test:     {'PASS' if loader_pass else 'FAIL'}")
    print("================================================================================")

    if schema_pass and dup_pass and bilingual_pass and notes_pass and loader_pass:
        print("🏆 ALL VALIDATIONS PASSED SUCCESSFULY!")
    else:
        print("❌ VALIDATION FAILED — FIX ERRORS ABOVE.")

if __name__ == "__main__":
    run_validation()
