# -*- coding: utf-8 -*-
"""
UI Validation Script for Fundamental Duties Part 2 Notes Rendering Engine
"""

import sys
import json
import os

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

from ui.notes.registry import GLOBAL_REGISTRY

def test_ui_rendering_structure_part2():
    print("================================================================================")
    print("🚀 RUNNING UI RENDERING ENGINE VALIDATION FOR FUNDAMENTAL DUTIES PART 2")
    print("================================================================================")

    note_path = "data/notes/polity/fundamental_duties_part_2.json"
    with open(note_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    content = data.get("content", {})

    top_level_section_keys = [
        "definition",
        "learning_objectives",
        "introduction",
        "comparison",
        "tables",
        "important_facts",
        "quick_revision",
        "tnpsc_traps",
        "mind_map",
        "revision_cards"
    ]

    print("\n[STEP 1] Testing Component Registry Key Matches:")
    for key in top_level_section_keys:
        spec = GLOBAL_REGISTRY.match_key(key)
        assert spec is not None, f"❌ Key '{key}' failed to match any registered component spec!"
        print(f"   - Key '{key}' -> Matched Spec Order {spec.order} ({spec.display_title})")

    print("\n[STEP 2] Verifying Section Content Blocks Structure:")
    sections = data.get("sections", [])
    for sec in sections:
        sec_id = sec["id"]
        assert sec_id in content, f"❌ Section ID '{sec_id}' missing in content payload!"
        blocks = content[sec_id]
        print(f"   - Section '{sec['title_en']}' ({sec_id}): {len(blocks)} content block(s)")

    print("\n[STEP 3] Verifying Comparison Tables Structure:")
    tables = content.get("tables", [])
    assert len(tables) == 10, f"❌ Expected 10 tables, found {len(tables)}"
    for idx, tbl in enumerate(tables, 1):
        headers_en = tbl.get("headers_en", [])
        headers_ta = tbl.get("headers_ta", [])
        rows_en = tbl.get("rows_en", [])
        rows_ta = tbl.get("rows_ta", [])

        assert len(headers_en) > 0 and len(headers_ta) > 0, f"❌ Table {idx} headers missing!"
        assert len(rows_en) == len(rows_ta), f"❌ Table {idx} row counts mismatched between EN ({len(rows_en)}) and TA ({len(rows_ta)})!"
        print(f"   - Table {idx}: '{tbl['title_en']}' -> {len(rows_en)} bilingual rows ready for Streamlit HTML table tabs")

    print("\n[STEP 4] Verifying Mind Map Nodes Structure:")
    mind_map = content.get("mind_map", [])
    assert len(mind_map) > 0, "❌ Mind map payload missing!"
    root = mind_map[0]
    print(f"   - Root Node: '{root['title']}' with {len(root['children'])} top-level branches")

    print("\n================================================================================")
    print("🏆 UI RENDERING ENGINE VALIDATION PASSED SUCCESSFULLY FOR FUNDAMENTAL DUTIES PART 2!")
    print("================================================================================")

if __name__ == "__main__":
    test_ui_rendering_structure_part2()
