# -*- coding: utf-8 -*-
"""
Practice Questions UI Simulation Test for Citizenship of India
"""

import sys
import json
import os

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

from core.topics_loader import get_topic_metadata_by_id
from core.question_loader import load_questions

def test_citizenship_ui_simulation():
    print("================================================================================")
    print("🚀 RUNNING PRACTICE UI SIMULATION FOR CITIZENSHIP OF INDIA")
    print("================================================================================")

    # 1. Test topic resolution in topics_loader
    meta = get_topic_metadata_by_id("polity", "polity_citizenship")
    assert meta is not None, "❌ Failed to resolve metadata for polity_citizenship"
    assert meta["display_title"] == "Citizenship of India"
    assert meta["total_parts"] == 3
    print(f"  ✓ Topic Metadata Resolved: {meta['display_title']} (Parts: {meta['total_parts']})")

    # 2. Test Question Loader for all 9 categories
    categories = {
        "easy": 50,
        "medium": 50,
        "hard": 50,
        "statement": 50,
        "reasoning": 25,
        "match_the_following": 25,
        "chronology": 25,
        "pyq": 50,
        "grand_test": 100
    }

    for cat, expected_count in categories.items():
        qs = load_questions("polity_citizenship", cat)
        assert len(qs) == expected_count, f"❌ Category {cat} expected {expected_count}, got {len(qs)}"

        # Validate render fields for first question in each category
        q0 = qs[0]
        assert "id" in q0 and q0["id"].startswith("CZ_")
        assert "question" in q0 and "en" in q0["question"] and "ta" in q0["question"]
        assert len(q0["options"]) == 4
        for opt in q0["options"]:
            assert "id" in opt and "en" in opt and "ta" in opt
        assert "correct_answer" in q0 and q0["correct_answer"] in ["A", "B", "C", "D"]
        assert "explanation" in q0 and "en" in q0["explanation"] and "ta" in q0["explanation"]
        assert "why_not_others" in q0 and len(q0["why_not_others"]) == 4
        assert "tnpsc_tip" in q0 and "en" in q0["tnpsc_tip"] and "ta" in q0["tnpsc_tip"]
        assert "revision_fact" in q0 and "en" in q0["revision_fact"] and "ta" in q0["revision_fact"]
        assert "source_reference" in q0 and len(q0["source_reference"]) > 0

        print(f"  ✓ Practice Engine Category `{cat}`: {len(qs)} MCQs loaded & UI fields validated.")

    print("\n================================================================================")
    print("🏆 PRACTICE QUESTION UI SIMULATION PASSED FOR CITIZENSHIP OF INDIA!")
    print("================================================================================")

if __name__ == "__main__":
    test_citizenship_ui_simulation()
