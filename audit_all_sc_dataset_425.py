# -*- coding: utf-8 -*-
"""
Supreme Court 425 MCQs Complete Audit & Validation Script (Robust Version)
"""

import glob
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

def run_full_audit():
    polity_dir = "data/questions/polity"
    notes_dir = "data/notes/polity"

    # Define the 8 primary dataset files representing the 425 MCQs
    part1_files = {
        "Easy": os.path.join(polity_dir, "supreme_court_easy.json"),
        "Medium": os.path.join(polity_dir, "supreme_court_medium.json"),
        "Hard": os.path.join(polity_dir, "supreme_court_hard.json")
    }

    part2_files = {
        "Statement": os.path.join(polity_dir, "supreme_court_statement.json"),
        "Reasoning": os.path.join(polity_dir, "supreme_court_reasoning.json"),
        "Match": os.path.join(polity_dir, "supreme_court_match.json"),
        "Chronology": os.path.join(polity_dir, "supreme_court_chronology.json"),
        "PYQ": os.path.join(polity_dir, "supreme_court_pyq.json")
    }

    part3_files = {
        "Grand Test": os.path.join(polity_dir, "supreme_court_grand_test.json")
    }

    notes_files = [
        os.path.join(notes_dir, "supreme_court_part_1.json"),
        os.path.join(notes_dir, "supreme_court_part_2.json"),
        os.path.join(notes_dir, "supreme_court_part_3.json")
    ]

    print("=== 1. FILE EXISTENCE & JSON VALIDITY AUDIT ===")
    all_target_files = {**part1_files, **part2_files, **part3_files}
    file_status = {}
    
    for category, fpath in all_target_files.items():
        exists = os.path.exists(fpath)
        valid_json = False
        count = 0
        if exists:
            try:
                data = json.load(open(fpath, encoding='utf-8'))
                valid_json = True
                count = len(data)
            except Exception as e:
                valid_json = False
        file_status[category] = {
            "path": fpath,
            "filename": os.path.basename(fpath),
            "exists": exists,
            "valid_json": valid_json,
            "count": count
        }
        print(f"  [{category}] {os.path.basename(fpath)}: Exists={exists}, ValidJSON={valid_json}, Count={count}")

    # Also check alias files
    alias_files = [
        "supreme_court_statement_based.json",
        "supreme_court_assertion_reason.json",
        "supreme_court_match_the_following.json",
        "supreme_court_pyq_practice.json"
    ]
    print("\n--- Checking Repository Aliases ---")
    for af in alias_files:
        af_path = os.path.join(polity_dir, af)
        if os.path.exists(af_path):
            data = json.load(open(af_path, encoding='utf-8'))
            print(f"  Alias file {af}: Exists=True, Count={len(data)}")

    print("\n=== 2. COUNT VALIDATION ===")
    expected_counts = {
        "Easy": 50, "Medium": 50, "Hard": 50,
        "Statement": 50, "Reasoning": 25, "Match": 25, "Chronology": 25, "PYQ": 50,
        "Grand Test": 100
    }
    
    total_expected = sum(expected_counts.values())
    total_actual = sum(info["count"] for info in file_status.values())

    print(f"{'Category':<15} | {'Expected':<10} | {'Actual':<10} | {'Status'}")
    print("-" * 50)
    for cat, exp in expected_counts.items():
        act = file_status[cat]["count"]
        status = "PASS" if exp == act else "FAIL"
        print(f"{cat:<15} | {exp:<10} | {act:<10} | {status}")
    print("-" * 50)
    print(f"{'TOTAL':<15} | {total_expected:<10} | {total_actual:<10} | {'PASS' if total_expected == total_actual else 'FAIL'}")

    # Load all 425 MCQs into a structured list
    all_425 = []

    for cat, info in file_status.items():
        if info["valid_json"]:
            data = json.load(open(info["path"], encoding='utf-8'))
            part_name = "Part 1" if cat in part1_files else ("Part 2" if cat in part2_files else "Part 3")
            for item in data:
                item["_file_cat"] = cat
                item["_file_name"] = info["filename"]
                item["_part"] = part_name
                all_425.append(item)

    print(f"\nLoaded total {len(all_425)} MCQs for deep audit.")

    print("\n=== 3. SCHEMA & MANDATORY FIELDS AUDIT ===")
    req_fields = [
        "id", "subject", "topic", "difficulty", "question_type",
        "question", "question_en", "question_ta", "options", "options_en", "options_ta",
        "correct_answer", "explanation", "explanation_en", "explanation_ta",
        "why_not_others", "trap_point", "tnpsc_tip", "high_yield_fact", "source_reference"
    ]

    schema_errors = []
    for q in all_425:
        q_id = q.get("id", "UNKNOWN")
        for f in req_fields:
            if f not in q:
                schema_errors.append((q["_file_name"], q_id, f, "Present", "Missing", "HIGH"))
            elif q[f] is None:
                schema_errors.append((q["_file_name"], q_id, f, "Non-Null", "Null", "HIGH"))

    print(f"Total Schema Errors found: {len(schema_errors)}")

    print("\n=== 4. ID UNICITY & REPOSITORY CONVENTION AUDIT ===")
    id_map = {}
    duplicate_ids = []
    invalid_id_format = []

    for q in all_425:
        q_id = q.get("id", "")
        if not q_id:
            invalid_id_format.append((q["_file_name"], "EMPTY", "Non-empty string", "Empty", "CRITICAL"))
        if q_id in id_map:
            duplicate_ids.append((q_id, id_map[q_id], q["_file_name"]))
        else:
            id_map[q_id] = q["_file_name"]

    print(f"Total Unique IDs: {len(id_map)} / 425")
    print(f"Total Duplicate IDs across 425 MCQs: {len(duplicate_ids)}")

    print("\n=== 5. OPTION STRUCTURE & ANSWER KEY BALANCING AUDIT ===")
    option_errors = []
    answer_dist_overall = {"A": 0, "B": 0, "C": 0, "D": 0}
    answer_dist_part = {
        "Part 1": {"A": 0, "B": 0, "C": 0, "D": 0},
        "Part 2": {"A": 0, "B": 0, "C": 0, "D": 0},
        "Part 3": {"A": 0, "B": 0, "C": 0, "D": 0}
    }

    for q in all_425:
        q_id = q.get("id", "UNKNOWN")
        correct = q.get("correct_answer", "")
        part = q["_part"]

        if correct in ["A", "B", "C", "D"]:
            answer_dist_overall[correct] += 1
            answer_dist_part[part][correct] += 1
        else:
            option_errors.append((q["_file_name"], q_id, "correct_answer", "A/B/C/D", correct, "CRITICAL"))

        opts = q.get("options", [])
        if len(opts) != 4:
            option_errors.append((q["_file_name"], q_id, "options_count", 4, len(opts), "CRITICAL"))

        opt_ids = [o.get("id") for o in opts if isinstance(o, dict)]
        if opt_ids != ["A", "B", "C", "D"]:
            option_errors.append((q["_file_name"], q_id, "option_keys", ["A", "B", "C", "D"], opt_ids, "HIGH"))

    print(f"Option Structure Errors: {len(option_errors)}")
    print("Answer Key Distribution Overall (425 MCQs):")
    for k, v in answer_dist_overall.items():
        pct = (v / len(all_425)) * 100
        print(f"  Option {k}: {v} ({pct:.1f}%)")

    print("\nAnswer Key Distribution by Part:")
    for part, dist in answer_dist_part.items():
        p_total = sum(dist.values())
        print(f"  {part} ({p_total} MCQs): A={dist['A']}, B={dist['B']}, C={dist['C']}, D={dist['D']}")

    print("\n=== 6. BILINGUAL CONTENT COMPLETENESS AUDIT ===")
    bilingual_errors = []
    for q in all_425:
        q_id = q.get("id", "UNKNOWN")

        # Check English question
        q_en = q.get("question_en", "") or (q.get("question", {}).get("en") if isinstance(q.get("question"), dict) else "")
        if not q_en or not str(q_en).strip():
            bilingual_errors.append((q["_file_name"], q_id, "question_en", "Non-empty string", "Empty", "CRITICAL"))

        # Check Tamil question
        q_ta = q.get("question_ta", "") or (q.get("question", {}).get("ta") if isinstance(q.get("question"), dict) else "")
        if not q_ta or not str(q_ta).strip():
            bilingual_errors.append((q["_file_name"], q_id, "question_ta", "Non-empty string", "Empty", "CRITICAL"))

        # Check options bilingual
        opts_en = q.get("options_en")
        opts_ta = q.get("options_ta")

        if isinstance(opts_en, dict):
            for k in ["A", "B", "C", "D"]:
                if not str(opts_en.get(k, "")).strip():
                    bilingual_errors.append((q["_file_name"], q_id, f"options_en[{k}]", "Non-empty", "Empty", "HIGH"))
        elif isinstance(opts_en, list):
            if len(opts_en) < 4:
                bilingual_errors.append((q["_file_name"], q_id, "options_en_len", 4, len(opts_en), "HIGH"))

        if isinstance(opts_ta, dict):
            for k in ["A", "B", "C", "D"]:
                if not str(opts_ta.get(k, "")).strip():
                    bilingual_errors.append((q["_file_name"], q_id, f"options_ta[{k}]", "Non-empty", "Empty", "HIGH"))
        elif isinstance(opts_ta, list):
            if len(opts_ta) < 4:
                bilingual_errors.append((q["_file_name"], q_id, "options_ta_len", 4, len(opts_ta), "HIGH"))

        # Check explanations
        exp_en = q.get("explanation_en", "") or (q.get("explanation", {}).get("en") if isinstance(q.get("explanation"), dict) else "")
        exp_ta = q.get("explanation_ta", "") or (q.get("explanation", {}).get("ta") if isinstance(q.get("explanation"), dict) else "")
        if not exp_en or not str(exp_en).strip():
            bilingual_errors.append((q["_file_name"], q_id, "explanation_en", "Non-empty", "Empty", "HIGH"))
        if not exp_ta or not str(exp_ta).strip():
            bilingual_errors.append((q["_file_name"], q_id, "explanation_ta", "Non-empty", "Empty", "HIGH"))

    print(f"Total Bilingual Completeness Errors: {len(bilingual_errors)}")

    print("\n=== 7. CROSS-PART DUPLICATE AUDIT (ALL 425 MCQs) ===")
    exact_duplicates = []
    near_duplicates = []

    # Map question text (normalized)
    seen_stems = {}

    for q in all_425:
        q_id = q.get("id", "UNKNOWN")
        q_en = q.get("question_en", "").strip().lower()
        q_clean = re.sub(r'\s+', ' ', q_en)

        if q_clean in seen_stems:
            other = seen_stems[q_clean]
            exact_duplicates.append({
                "id1": other["id"], "file1": other["_file_name"], "part1": other["_part"],
                "id2": q_id, "file2": q["_file_name"], "part2": q["_part"],
                "stem": q_en[:80]
            })
        else:
            seen_stems[q_clean] = q

    print(f"Exact Duplicate Question Stems across 425 MCQs: {len(exact_duplicates)}")
    if exact_duplicates:
        for dup in exact_duplicates[:10]:
            print(f"  Exact Duplicate: {dup['id1']} ({dup['part1']} - {dup['file1']}) <-> {dup['id2']} ({dup['part2']} - {dup['file2']})")
            print(f"    Stem: {dup['stem']}...")

    print("\n=== 8. MANDATORY 46 CONTENT TOPIC COVERAGE AUDIT ===")
    topics_keywords = {
        "1. Constitutional position": ["constitutional position", "part v", "supreme court", "highest judicial court", "apex court", "inauguration", "1950"],
        "2. Establishment and composition": ["article 124", "composition", "number of judges", "strength", "34", "parliament"],
        "3. Appointment of judges": ["appointment", "president", "collegium", "consultation", "article 124(2)"],
        "4. Collegium system": ["collegium", "first judges", "second judges", "third judges", "cji + 4", "cji + 2"],
        "5. NJAC and amendment": ["njac", "99th", "ninety-ninth", "fourth judges", "2015"],
        "6. Qualifications": ["qualification", "citizen", "5 years", "10 years", "distinguished jurist"],
        "7. Oath and affirmation": ["oath", "affirmation", "third schedule", "article 124(6)"],
        "8. Tenure and retirement": ["tenure", "65 years", "retirement age", "article 124(2)"],
        "9. Resignation": ["resignation", "addressed to president", "article 124(2)(a)"],
        "10. Removal of judges": ["removal", "impeachment", "judges inquiry act", "100 members", "50 members", "special majority"],
        "11. Salary and service conditions": ["salary", "article 125", "consolidated fund of india", "charged expenditure"],
        "12. Acting Chief Justice": ["acting chief justice", "acting cji", "article 126"],
        "13. Ad hoc judges": ["ad hoc", "article 127", "quorum", "high court judge"],
        "14. Retired judges": ["retired judges", "article 128", "consent"],
        "15. Original jurisdiction": ["original jurisdiction", "federal disputes", "article 131"],
        "16. Article 131": ["article 131", "centre", "state", "federal"],
        "17. Appellate jurisdiction": ["appellate jurisdiction", "article 132", "article 133", "article 134"],
        "18. Constitutional appeals": ["constitutional appeal", "article 132"],
        "19. Civil appeals": ["civil appeal", "article 133", "30th amendment"],
        "20. Criminal appeals": ["criminal appeal", "article 134", "death sentence"],
        "21. Writ jurisdiction": ["writ jurisdiction", "article 32", "writs"],
        "22. Article 32": ["article 32", "heart and soul", "fundamental right"],
        "23. Five writs": ["habeas corpus", "mandamus", "prohibition", "quo-warranto", "certiorari"],
        "24. Special Leave Petition": ["special leave petition", "slp", "article 136"],
        "25. Review jurisdiction": ["review jurisdiction", "article 137"],
        "26. Curative petition": ["curative petition", "rupa ashok hurra"],
        "27. Advisory jurisdiction": ["advisory jurisdiction", "article 143", "presidential reference"],
        "28. Transfer jurisdiction": ["transfer", "article 139a"],
        "29. Judicial review": ["judicial review", "basic feature"],
        "30. Judicial activism": ["judicial activism", "vr krishna iyer", "pn bhagwati"],
        "31. Public Interest Litigation": ["public interest litigation", "pil", "locus standi"],
        "32. Basic Structure Doctrine": ["basic structure", "kesavananda bharati", "1973"],
        "33. Independence of judiciary": ["independence of judiciary", "article 121", "article 211"],
        "34. Contempt of court": ["contempt of court", "article 129", "1971 act"],
        "35. Court of Record": ["court of record", "article 129"],
        "36. Seat and procedure": ["seat of supreme court", "article 130", "delhi"],
        "37. Binding nature": ["binding", "article 141", "law declared"],
        "38. Complete Justice": ["complete justice", "article 142"],
        "39. Article 144": ["article 144", "act in aid"],
        "40. Supreme Court administration": ["administration", "article 146", "officers and servants"],
        "41. Articles 124-147": ["article 124", "article 147", "part v"],
        "42. Landmark cases": ["kesavananda", "maneka gandhi", "minerva mills", "sr bommai"],
        "43. Relevant Amendments": ["42nd", "44th", "99th", "15th"],
        "44. Supreme Court vs High Court": ["high court", "supreme court vs high court", "article 226 vs 32"],
        "45. Common TNPSC traps": ["trap", "exception", "seniority rule"]
    }

    coverage_counts = {t: 0 for t in topics_keywords}

    for q in all_425:
        text_full = (q.get("question_en", "") + " " + q.get("explanation_en", "") + " " + str(q.get("source_reference", ""))).lower()
        for t, kw_list in topics_keywords.items():
            if any(kw in text_full for kw in kw_list):
                coverage_counts[t] += 1

    print(f"{'Topic Area':<35} | {'Questions Found':<15} | {'Coverage Status'}")
    print("-" * 65)
    well_covered = 0
    under_covered = 0
    missing = 0

    for t, cnt in coverage_counts.items():
        if cnt >= 5:
            status = "✓ WELL COVERED"
            well_covered += 1
        elif cnt >= 1:
            status = "⚠ UNDER-COVERED"
            under_covered += 1
        else:
            status = "❌ MISSING"
            missing += 1
        print(f"{t:<35} | {cnt:<15} | {status}")

    print("-" * 65)
    print(f"Summary: Well Covered: {well_covered}, Under-Covered: {under_covered}, Missing: {missing}")

    print("\n=== 9. ARTICLE ACCURACY AUDIT (Articles 124 to 147) ===")
    article_list = range(124, 148)
    art_counts = {art: 0 for art in article_list}

    for q in all_425:
        text_full = (q.get("question_en", "") + " " + q.get("explanation_en", "")).lower()
        for art in article_list:
            if f"article {art}" in text_full or f"art {art}" in text_full or f"art. {art}" in text_full or f"சரத்து {art}" in text_full:
                art_counts[art] += 1

    for art, cnt in art_counts.items():
        print(f"  Article {art}: {cnt} mentions")

    return {
        "file_status": file_status,
        "total_actual": total_actual,
        "schema_errors": len(schema_errors),
        "duplicate_ids": len(duplicate_ids),
        "option_errors": len(option_errors),
        "bilingual_errors": len(bilingual_errors),
        "exact_duplicates": len(exact_duplicates),
        "answer_dist_overall": answer_dist_overall,
        "coverage_summary": {"well_covered": well_covered, "under_covered": under_covered, "missing": missing}
    }

if __name__ == "__main__":
    run_full_audit()
