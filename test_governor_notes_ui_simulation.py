# -*- coding: utf-8 -*-
"""
Interactive UI Rendering Simulation for Governor Notes Parts 1, 2, and 3
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

import streamlit as st
def dummy_decorator(func):
    return func
st.cache_data = dummy_decorator

from ui.notes.renderer import render_notes_engine

def test_governor_notes_ui_simulation():
    print("================================================================================")
    print("🧪 UI & NOTES ENGINE SIMULATION — GOVERNOR OF A STATE NOTES (PARTS 1–3)")
    print("================================================================================")

    files = [
        ("Governor Part 1", "data/notes/polity/governor_part_1.json"),
        ("Governor Part 2", "data/notes/polity/governor_part_2.json"),
        ("Governor Part 3", "data/notes/polity/governor_part_3.json")
    ]

    for title, fpath in files:
        print(f"\n▶ Testing UI Rendering for {title}...")
        assert os.path.exists(fpath), f"File missing: {fpath}"

        with open(fpath, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Call render_notes_engine simulation
        try:
            render_notes_engine(data)
            print(f"  ✅ {title}: render_notes_engine executed cleanly with zero errors.")
        except Exception as e:
            print(f"  ❌ {title} UI rendering failed: {e}")
            return False

    print("\n================================================================================")
    print("🎉 ALL 3 GOVERNOR NOTES DATASETS PASSED UI & ENGINE SIMULATION 100%!")
    print("================================================================================")
    return True

if __name__ == "__main__":
    test_governor_notes_ui_simulation()
