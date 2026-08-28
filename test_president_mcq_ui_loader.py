import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

# Mock Streamlit cache_data decorator
import streamlit as st
def dummy_decorator(func):
    return func
st.cache_data = dummy_decorator

from core.question_loader import load_questions

levels = [
    ("easy", 50),
    ("medium", 50),
    ("hard", 50),
    ("statement", 50),
    ("reasoning", 25),
    ("chronology", 25),
    ("match", 25),
    ("grand_test", 100)
]

print("==================================================")
print("TESTING QUESTION LOADER FOR PRESIDENT DATASETS")
print("==================================================")

passed = True

for lvl, expected_count in levels:
    # Test new signature
    qs = load_questions("polity_president", lvl)
    if len(qs) != expected_count:
        print(f"❌ FAIL: load_questions('polity_president', '{lvl}') returned {len(qs)}, expected {expected_count}")
        passed = False
    else:
        print(f"  [polity_president, {lvl}]: SUCCESS ({len(qs)} loaded)")

    # Test legacy signature
    qs_leg = load_questions("polity", "President Part 1", lvl)
    if len(qs_leg) != expected_count:
        print(f"❌ FAIL: load_questions('polity', 'President Part 1', '{lvl}') returned {len(qs_leg)}, expected {expected_count}")
        passed = False
    else:
        print(f"  [polity, President Part 1, {lvl}]: SUCCESS ({len(qs_leg)} loaded)")

if passed:
    print("\nSUCCESS: ALL PRESIDENT DATASETS LOAD CLEANLY THROUGH UI QUESTION LOADER!")
else:
    print("\nFAILED: QUESTION LOADER ERROR DETECTED!")
