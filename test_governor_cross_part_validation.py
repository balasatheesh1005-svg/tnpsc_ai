# -*- coding: utf-8 -*-
"""
Cross-Part Basic Validation & Non-Regression Suite for Governor of a State Notes
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

def test_governor_cross_part_validation():
    print("================================================================================")
    print("🧪 CROSS-PART BASIC VALIDATION SUITE — GOVERNOR OF A STATE NOTES (PARTS 1–3)")
    print("================================================================================")

    parts_files = [
        ("data/notes/polity/governor_part_1.json", 1, 6),
        ("data/notes/polity/governor_part_2.json", 2, 6),
        ("data/notes/polity/governor_part_3.json", 3, 8)
    ]

    all_passed = True

    for fpath, expected_part, min_tables in parts_files:
        print(f"\n▶ Testing File: {fpath} (Part {expected_part})...")
        assert os.path.exists(fpath), f"❌ File missing: {fpath}"
        
        with open(fpath, "r", encoding="utf-8") as f:
            data = json.load(f)

        # 1. Check Root Schema & Meta
        meta = data.get("meta", {})
        assert meta.get("part") == expected_part, f"Part mismatch: expected {expected_part}, got {meta.get('part')}"
        assert meta.get("total_parts") == 3, f"Total parts mismatch: expected 3, got {meta.get('total_parts')}"
        assert meta.get("subject") == "polity"

        content = data.get("content", {})
        assert isinstance(content, dict), "Content payload must be a dict"

        # 2. Check Comparison Tables
        tables = content.get("comparison_tables", [])
        assert len(tables) >= min_tables, f"Expected at least {min_tables} tables, got {len(tables)}"
        for idx, tbl in enumerate(tables, 1):
            assert tbl.get("title_en") and tbl.get("title_ta"), f"Table {idx} missing titles"
            h_en = tbl.get("headers_en", [])
            h_ta = tbl.get("headers_ta", [])
            r_en = tbl.get("rows_en", [])
            r_ta = tbl.get("rows_ta", [])

            assert len(h_en) >= 2 and len(h_ta) >= 2, f"Table {idx} ({tbl.get('id')}) insufficient headers"
            assert len(r_en) >= 3 and len(r_ta) >= 3, f"Table {idx} ({tbl.get('id')}) insufficient rows"
            assert len(r_en) == len(r_ta), f"Table {idx} ({tbl.get('id')}) row count mismatch between EN and TA"

            for row_idx, row in enumerate(r_en):
                assert len(row) == len(h_en), f"Table {idx} row {row_idx} cell count mismatch with headers"
                for cell in row:
                    assert cell and str(cell).strip(), f"Table {idx} row {row_idx} contains empty cell"

        # 3. Check Mind Map, Traps, Revision
        assert "mind_map" in content and content["mind_map"], "Missing mind_map"
        assert "tnpsc_traps" in content and content["tnpsc_traps"], "Missing tnpsc_traps"
        assert "quick_revision" in content and content["quick_revision"], "Missing quick_revision"
        assert "must_remember" in content and content["must_remember"], "Missing must_remember"

        print(f"  ✅ Part {expected_part}: PASSED 100% (Contains {len(tables)} valid tables, mind map, traps, and bilingual content)")

    # 4. Non-Regression Check: Ensure President, VP, PM notes still load
    print("\n--- NON-REGRESSION CHECK FOR EXISTING NOTES ---")
    other_topics = [
        "data/notes/polity/president_part_1.json",
        "data/notes/polity/vice_president_part_1.json",
        "data/notes/polity/prime_minister_part_1.json"
    ]
    for ot in other_topics:
        assert os.path.exists(ot), f"Existing file missing: {ot}"
        with open(ot, encoding="utf-8") as f:
            ot_data = json.load(f)
            assert ot_data.get("meta", {}).get("part") == 1
        print(f"  ✅ {os.path.basename(ot)}: Loaded cleanly without regression.")

    print("\n================================================================================")
    print("🎉 ALL GOVERNOR NOTES (PARTS 1–3) PASSED CROSS-PART VALIDATION & NON-REGRESSION 100%!")
    print("================================================================================")
    return True

if __name__ == "__main__":
    test_governor_cross_part_validation()
