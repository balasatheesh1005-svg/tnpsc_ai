# -*- coding: utf-8 -*-
"""
Verification suite for Prime Minister Notes Parts 1, 2, and 3 loading in the application.
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

import streamlit as st
def dummy_dec(func): return func
st.cache_data = dummy_dec

from core.topics_loader import get_topic_metadata_by_id
from ui.pages.notes import load_note

def test_pm_notes_loading():
    print("================================================================================")
    print("🧪 VERIFYING PRIME MINISTER NOTES PART 1, PART 2, PART 3 LOADING & ROUTING")
    print("================================================================================")

    test_cases = [
        ("polity", "polity_prime_minister_part_1", "data/notes/polity/prime_minister_part_1.json", 1),
        ("polity", "polity_prime_minister_part_2", "data/notes/polity/prime_minister_part_2.json", 2),
        ("polity", "polity_prime_minister_part_3", "data/notes/polity/prime_minister_part_3.json", 3),
        ("polity", "Prime Minister of India – Part 1", "data/notes/polity/prime_minister_part_1.json", 1),
        ("polity", "Prime Minister of India – Part 2", "data/notes/polity/prime_minister_part_2.json", 2),
        ("polity", "Prime Minister of India – Part 3", "data/notes/polity/prime_minister_part_3.json", 3),
        ("polity", "polity_president_part_1", "data/notes/polity/president_part_1.json", 1),
        ("polity", "polity_vice_president_part_1", "data/notes/polity/vice_president_part_1.json", 1),
    ]

    all_passed = True
    for subj, topic_query, expected_file, expected_part in test_cases:
        meta = get_topic_metadata_by_id(subj, topic_query)
        topic_id = meta["topic_id"]
        
        note_basename = topic_id
        if note_basename.startswith(f"{subj}_"):
            note_basename = note_basename[len(subj) + 1:]

        candidate_files = [
            f"data/notes/{subj}/{note_basename}.json",
            f"data/notes/{subj}/{note_basename}_part_1.json",
            f"data/notes/{subj}/{note_basename}_part1.json",
            f"data/notes/{subj}/{note_basename.replace('part', 'part_')}.json" if "part" in note_basename and "part_" not in note_basename else f"data/notes/{subj}/{note_basename}.json",
        ]

        loaded_path = None
        data = None
        for cand in candidate_files:
            if os.path.exists(cand):
                data = load_note(cand)
                if data is not None:
                    loaded_path = cand
                    break

        if data is None:
            print(f"❌ FAIL: Query '{topic_query}' failed to load any note file!")
            all_passed = False
            continue

        meta_block = data.get("meta") or data.get("metadata") or {}
        actual_part = meta_block.get("part")
        
        is_ok = (loaded_path == expected_file) and (actual_part == expected_part)
        status = "✅ PASS" if is_ok else "❌ FAIL"
        if not is_ok:
            all_passed = False

        print(f"  {status}: Query='{topic_query}' -> Resolved File='{loaded_path}' | Part={actual_part}")

    print("--------------------------------------------------------------------------------")
    if all_passed:
        print("🎉 ALL TEST CASES PASSED 100%! Prime Minister Notes Parts 1-3 load correctly.")
    else:
        print("❌ SOME TEST CASES FAILED!")

if __name__ == "__main__":
    test_pm_notes_loading()
