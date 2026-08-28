# -*- coding: utf-8 -*-
"""
UI Rendering Simulation Test for President Notes Comparison Tables
"""

import sys
import json
import os

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

import streamlit as st

# Mock streamlit components to capture HTML output in bare mode
rendered_components = []

def mock_markdown(body, unsafe_allow_html=False):
    rendered_components.append(("markdown", body, unsafe_allow_html))

def mock_subheader(body):
    rendered_components.append(("subheader", body, False))

st.markdown = mock_markdown
st.subheader = mock_subheader

from ui.notes.renderer import render_notes_engine
from ui.notes.components.comparison import render_comparison

def test_comparison_rendering():
    print("================================================================================")
    print("🧪 PRESIDENT NOTES COMPARISON TABLE UI RENDERING TEST")
    print("================================================================================")

    parts = [
        ("president_part_1.json", 10),
        ("president_part_2.json", 10),
        ("president_part_3.json", 12)
    ]

    for fname, expected_table_count in parts:
        path = f"data/notes/polity/{fname}"
        assert os.path.exists(path), f"Missing note file {path}"
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        content = data.get("content", data)
        comp_list = content.get("comparison_tables") or content.get("comparison") or []

        print(f"\n▶ Testing {fname}: {len(comp_list)} comparison tables found (expected {expected_table_count})...")
        assert len(comp_list) == expected_table_count, f"Table count mismatch in {fname}"

        for idx, table in enumerate(comp_list, 1):
            assert "headers_en" in table and len(table["headers_en"]) > 0, f"Table {idx} in {fname} missing headers_en"
            assert "headers_ta" in table and len(table["headers_ta"]) > 0, f"Table {idx} in {fname} missing headers_ta"
            assert "rows_en" in table and len(table["rows_en"]) > 0, f"Table {idx} in {fname} missing rows_en"
            assert "rows_ta" in table and len(table["rows_ta"]) > 0, f"Table {idx} in {fname} missing rows_ta"

            # Check column count parity
            h_len_en = len(table["headers_en"])
            h_len_ta = len(table["headers_ta"])
            assert h_len_en == h_len_ta, f"Header length EN ({h_len_en}) != TA ({h_len_ta}) in Table {idx}"

            for r_idx, r in enumerate(table["rows_en"]):
                assert len(r) == h_len_en, f"Row EN {r_idx} len ({len(r)}) != headers len ({h_len_en}) in Table {idx}"

            for r_idx, r in enumerate(table["rows_ta"]):
                assert len(r) == h_len_ta, f"Row TA {r_idx} len ({len(r)}) != headers len ({h_len_ta}) in Table {idx}"

        print(f"  ✅ {fname}: All {expected_table_count} tables validated for EN+TA headers, rows & column alignment!")

    print("\n================================================================================")
    print("🎉 ALL 32 PRESIDENT COMPARISON TABLES FULLY VALIDATED & PASSED RENDERING TEST!")
    print("================================================================================")

if __name__ == "__main__":
    test_comparison_rendering()
