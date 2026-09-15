# -*- coding: utf-8 -*-
"""
Full Verification & Quality Assurance Suite for DPSP Grand Test (100 MCQs)
"""

import sys
import json
import os
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

from core.question_loader import load_questions
from core.navigation_v2.navigation_state import check_repository_availability
from ui.question_engine.parser import UniversalQuestionAdapter, NormalizedQuestion

def test_dpsp_grand_test_suite():
    print("================================================================================")
    print("🧪 DPSP GRAND TEST (100 MCQs) — END-TO-END VERIFICATION SUITE")
    print("================================================================================")

    # 1. File existence & JSON integrity
    target_files = [
        "data/questions/polity/directive_principles_grand_test.json",
        "data/questions/polity/directive_principles_grand.json",
        "data/questions/polity/dpsp_grand_test.json",
        "data/questions/polity/directive_principles_of_state_policy_grand_test.json",
    ]

    print("\n[PHASE 1] Checking Target Question Files:")
    for path in target_files:
        assert os.path.exists(path), f"❌ File missing: {path}"
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        assert len(data) == 100, f"❌ Expected 100 questions in {path}, got {len(data)}"
        print(f"  ✅ {os.path.basename(path)}: Exists, valid UTF-8, exactly {len(data)} items")

    # 2. Schema & Bilingual Completeness
    print("\n[PHASE 2] Auditing Schema & Bilingual Content Integrity:")
    with open("data/questions/polity/directive_principles_grand_test.json", "r", encoding="utf-8") as f:
        questions = json.load(f)

    seen_ids = set()
    stems_en = set()
    stems_ta = set()
    key_counts = Counter()
    diff_counts = Counter()

    for idx, q in enumerate(questions, 1):
        # ID check
        qid = q.get("id")
        assert qid and qid.startswith("DPSP_GT_"), f"❌ Q{idx}: Invalid ID: {qid}"
        assert qid not in seen_ids, f"❌ Q{idx}: Duplicate ID found: {qid}"
        seen_ids.add(qid)

        # Required fields
        for f in ["subject", "topic", "difficulty", "question_type", "question", "options", "correct_answer", "explanation", "why_not_others", "tnpsc_tip"]:
            assert f in q, f"❌ Q{idx} ({qid}) missing required field: {f}"

        # Topic & Subject
        assert q["subject"] == "Polity"
        assert q["topic"] == "Directive Principles of State Policy"

        # Stems
        q_en = q["question"]["en"].strip()
        q_ta = q["question"]["ta"].strip()
        assert len(q_en) > 5, f"❌ Q{idx} empty or short English stem"
        assert len(q_ta) > 5, f"❌ Q{idx} empty or short Tamil stem"
        assert q_en not in stems_en, f"❌ Q{idx} duplicate EN stem: {q_en[:40]}"
        assert q_ta not in stems_ta, f"❌ Q{idx} duplicate TA stem: {q_ta[:40]}"
        stems_en.add(q_en)
        stems_ta.add(q_ta)

        # Options
        opts = q["options"]
        assert len(opts) == 4, f"❌ Q{idx} does not have 4 options"
        opt_ids = [o["id"] for o in opts]
        assert opt_ids == ["A", "B", "C", "D"], f"❌ Q{idx} invalid option IDs: {opt_ids}"
        for opt in opts:
            assert len(opt["en"].strip()) > 0, f"❌ Q{idx} option {opt['id']} EN is empty"
            assert len(opt["ta"].strip()) > 0, f"❌ Q{idx} option {opt['id']} TA is empty"

        # Correct answer
        ca = q["correct_answer"]
        assert ca in ["A", "B", "C", "D"], f"❌ Q{idx} invalid correct_answer: {ca}"
        key_counts[ca] += 1

        # Explanation
        exp = q["explanation"]
        assert len(exp["en"].strip()) > 5, f"❌ Q{idx} explanation EN is empty"
        assert len(exp["ta"].strip()) > 5, f"❌ Q{idx} explanation TA is empty"

        # Why not others
        wno = q["why_not_others"]
        for letter in ["A", "B", "C", "D"]:
            assert letter in wno, f"❌ Q{idx} why_not_others missing {letter}"
            assert len(wno[letter]["en"].strip()) > 0, f"❌ Q{idx} wno[{letter}] EN empty"
            assert len(wno[letter]["ta"].strip()) > 0, f"❌ Q{idx} wno[{letter}] TA empty"

        # TNPSC Tip
        tip = q["tnpsc_tip"]
        assert len(tip["en"].strip()) > 0, f"❌ Q{idx} tnpsc_tip EN empty"
        assert len(tip["ta"].strip()) > 0, f"❌ Q{idx} tnpsc_tip TA empty"

        # Normalization via UniversalQuestionAdapter
        norm: NormalizedQuestion = UniversalQuestionAdapter.normalize(q)
        assert norm.id == qid
        assert len(norm.options) == 4

        diff_counts[q["difficulty"]] += 1

    print(f"  ✅ All 100 questions verified: 100% bilingual, 0 empty fields, 0 duplicates")

    # 3. Answer Key Distribution
    print(f"\n[PHASE 3] Verifying Answer Key Parity:")
    print(f"  Distribution: {dict(key_counts)}")
    assert key_counts == {"A": 25, "B": 25, "C": 25, "D": 25}, f"❌ Answer key not balanced: {key_counts}"
    print("  ✅ Answer key is perfectly balanced (25 A, 25 B, 25 C, 25 D)")

    # 4. Difficulty Calibration
    print(f"\n[PHASE 4] Verifying Difficulty Distribution:")
    print(f"  Distribution: {dict(diff_counts)}")
    assert diff_counts == {"Easy": 20, "Medium": 50, "Hard": 30}, f"❌ Difficulty not calibrated: {diff_counts}"
    print("  ✅ Difficulty perfectly calibrated (20 Easy, 50 Medium, 30 Hard)")

    # 5. Availability & Navigation Resolver
    print(f"\n[PHASE 5] Testing UI Availability Engine:")
    queries = [
        "polity_directive_principles",
        "directive_principles",
        "Directive Principles of State Policy",
        "directive_principles_of_state_policy",
        "dpsp",
    ]
    for q_id in queries:
        avail = check_repository_availability("polity", q_id)
        assert avail["grand_test"] is True, f"❌ Grand Test marked False for query '{q_id}'"
        print(f"  ✅ Query '{q_id}': grand_test=True, notes={avail['notes']}, parts={avail['parts_found']}")

    # 6. Question Loader Multi-Signature Resolution
    print(f"\n[PHASE 6] Testing Question Loader Signatures:")
    signatures = [
        ("load_questions('polity_directive_principles', 'grand_test')", lambda: load_questions("polity_directive_principles", "grand_test")),
        ("load_questions('polity', 'directive_principles', 'grand_test')", lambda: load_questions("polity", "directive_principles", "grand_test")),
        ("load_questions('polity', 'Directive Principles of State Policy', 'grand_test')", lambda: load_questions("polity", "Directive Principles of State Policy", "grand_test")),
        ("load_questions('polity_dpsp', 'grand_test')", lambda: load_questions("polity_dpsp", "grand_test")),
        ("load_questions('polity', 'dpsp', 'grand_test')", lambda: load_questions("polity", "dpsp", "grand_test")),
    ]
    for desc, loader_fn in signatures:
        loaded = loader_fn()
        assert len(loaded) == 100, f"❌ Failed on {desc}: got {len(loaded)} questions"
        print(f"  ✅ {desc} -> 100 questions loaded successfully")

    print("\n================================================================================")
    print("🎉 ALL PHASES PASSED WITH ZERO REGRESSIONS (100% PASS)")
    print("================================================================================")

if __name__ == "__main__":
    test_dpsp_grand_test_suite()
