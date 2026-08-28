# -*- coding: utf-8 -*-
"""
Deep UI rendering simulation test for Prime Minister Notes Parts 1, 2, and 3.
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

import streamlit as st
def dummy_dec(func): return func
st.cache_data = dummy_dec
st.sidebar = type('Dummy', (), {'markdown': lambda *a, **k: None, 'button': lambda *a, **k: False, 'selectbox': lambda *a, **k: 'Option'})()
st.tabs = lambda tab_list: [type('DummyTab', (), {'__enter__': lambda s: None, '__exit__': lambda s, *a: None})() for _ in tab_list]

from ui.notes.renderer import render_notes_engine
from ui.pages.notes import render_2_minute_revision_card, load_note

def run_ui_simulation():
    print("================================================================================")
    print("🧪 PRIME MINISTER NOTES PART 1, PART 2, PART 3 FULL UI RENDERING SIMULATION")
    print("================================================================================")

    pm_files = [
        ("Prime Minister Part 1", "data/notes/polity/prime_minister_part_1.json", 1),
        ("Prime Minister Part 2", "data/notes/polity/prime_minister_part_2.json", 2),
        ("Prime Minister Part 3", "data/notes/polity/prime_minister_part_3.json", 3),
    ]

    for title, path, expected_part in pm_files:
        print(f"\n▶ Testing UI Rendering: {title} ({path})...")
        assert os.path.exists(path), f"File missing: {path}"
        
        data = load_note(path)
        assert data is not None, f"Failed to parse JSON: {path}"
        
        meta = data.get("meta") or data.get("metadata") or {}
        assert meta.get("part") == expected_part, f"Part mismatch: expected {expected_part}, got {meta.get('part')}"
        assert meta.get("total_parts") == 3, f"Total parts mismatch: expected 3, got {meta.get('total_parts')}"
        
        # Test main engine renderer
        try:
            render_notes_engine(data)
            print(f"  ✅ render_notes_engine rendered cleanly with 0 exceptions")
        except Exception as e:
            print(f"  ❌ render_notes_engine failed with error: {e}")
            raise e

        # Test revision card renderer
        try:
            render_2_minute_revision_card(data, meta.get("display_title", title), "polity")
            print(f"  ✅ render_2_minute_revision_card rendered cleanly with 0 exceptions")
        except Exception as e:
            print(f"  ❌ render_2_minute_revision_card failed with error: {e}")
            raise e

    print("\n================================================================================")
    print("🎉 ALL 3 PRIME MINISTER NOTES PARTS PASSED FULL UI RENDERING SIMULATION 100%!")
    print("================================================================================")

if __name__ == "__main__":
    run_ui_simulation()
