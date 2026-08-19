# -*- coding: utf-8 -*-
"""
Validation & Verification Test Suite for DPSP Part 1 Notes
"""

import sys
import json
import os
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

from core.topics_loader import get_topic_metadata_by_id
from core.navigation_v2.navigation_state import check_repository_availability

def test_dpsp_part1_notes_flow():
    print("================================================================================")
    print("🚀 RUNNING TNPSC NOVA AI - DPSP PART 1 NOTES VERIFICATION SUITE")
    print("================================================================================")

    # 1. File existence & JSON parsing
    note_path = "data/notes/polity/directive_principles_part_1.json"
    print(f"\n[STEP 1] Checking Note File Existence: {note_path}")
    assert os.path.exists(note_path), f"❌ File not found: {note_path}"

    with open(note_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert isinstance(data, dict), "❌ Notes JSON top-level is not a dict!"
    print("   ✅ File exists and JSON is valid.")

    # 2. Meta & Metadata Verification
    print("\n[STEP 2] Verifying Meta & Metadata Blocks")
    meta = data.get("meta", {})
    assert meta.get("topic_id") == "polity_directive_principles_part_1", f"❌ Invalid topic_id: {meta.get('topic_id')}"
    assert meta.get("part") == 1, f"❌ Invalid part: {meta.get('part')}"
    assert meta.get("total_parts") == 3, f"❌ Invalid total_parts: {meta.get('total_parts')}"
    assert meta.get("subject") == "polity", f"❌ Invalid subject: {meta.get('subject')}"
    print("   ✅ Meta block verified (part = 1, total_parts = 3).")

    # 3. Learning Outcomes & Keywords
    print("\n[STEP 3] Verifying Learning Outcomes & Keywords")
    keywords = data.get("keywords", [])
    assert len(keywords) >= 10, f"❌ Insufficient keywords: {len(keywords)}"
    
    outcomes = data.get("learning_outcomes", {})
    for level in ["Understand", "Remember", "Analyze", "Apply"]:
        assert level in outcomes, f"❌ Missing outcome level: {level}"
        assert "en" in outcomes[level] and "ta" in outcomes[level]
        assert len(outcomes[level]["en"]) > 0, f"❌ Empty EN outcomes for {level}"
        assert len(outcomes[level]["ta"]) > 0, f"❌ Empty TA outcomes for {level}"
    print("   ✅ Learning outcomes & keywords verified.")

    # 4. Mandatory Sections Audit
    print("\n[STEP 4] Content & Mandatory Sections Audit")
    content = data.get("content", {})
    assert "definition" in content and "en" in content["definition"] and "ta" in content["definition"]
    assert "introduction" in content and "en" in content["introduction"] and "ta" in content["introduction"]

    # Check key section blocks
    required_sec_keys = [
        "sec_dpsp_overview", "sec_article_36", "sec_article_37", "sec_article_38",
        "sec_article_39", "sec_article_39a", "sec_dpsp_classification",
        "sec_cases_amendments", "sec_traps_revision"
    ]
    for s_key in required_sec_keys:
        assert s_key in content, f"❌ Missing section content: {s_key}"
        assert isinstance(content[s_key], list) and len(content[s_key]) > 0
        for block in content[s_key]:
            assert "title" in block and "points" in block
            assert "en" in block["points"] and "ta" in block["points"]
            assert len(block["points"]["en"]) > 0, f"❌ Empty EN points in {s_key}"
            assert len(block["points"]["ta"]) > 0, f"❌ Empty TA points in {s_key}"
    print("   ✅ All 9 detailed content sections verified.")

    # 5. Mandatory Comparison Tables Audit (8 Tables)
    print("\n[STEP 5] Verifying Mandatory 8 Comparison Tables")
    tables = content.get("tables", [])
    assert len(tables) == 8, f"❌ Expected 8 comparison tables, found {len(tables)}"
    for idx, tbl in enumerate(tables, 1):
        assert "title_en" in tbl and "title_ta" in tbl
        assert "headers_en" in tbl and "headers_ta" in tbl
        assert "rows_en" in tbl and "rows_ta" in tbl
        assert len(tbl["headers_en"]) >= 2, f"❌ Table {idx} missing headers_en"
        assert len(tbl["headers_ta"]) >= 2, f"❌ Table {idx} missing headers_ta"
        assert len(tbl["rows_en"]) >= 2, f"❌ Table {idx} insufficient rows_en"
        assert len(tbl["rows_ta"]) >= 2, f"❌ Table {idx} insufficient rows_ta"
        print(f"   - Table {idx}: '{tbl['title_en']}' ({len(tbl['rows_en'])} rows) -> PASSED")
    print("   ✅ All 8 comparison tables verified.")

    # 6. Mind Map Audit
    print("\n[STEP 6] Verifying Mind Map Structure")
    mind_map = content.get("mind_map", [])
    assert len(mind_map) > 0, "❌ Mind map is empty!"
    root_node = mind_map[0]
    assert "title" in root_node and "children" in root_node
    assert len(root_node["children"]) >= 3, "❌ Mind map root missing expected branches!"
    print("   ✅ Mind map structure verified.")

    # 7. TNPSC Traps & Quick Revision Audit
    print("\n[STEP 7] Verifying TNPSC Traps & Quick Revision")
    traps = content.get("tnpsc_traps", [])
    assert len(traps) >= 5, f"❌ Expected at least 5 TNPSC trap blocks, found {len(traps)}"
    for trap in traps:
        assert "title" in trap and "points" in trap
        assert "en" in trap["points"] and "ta" in trap["points"]
        assert len(trap["points"]["en"]) > 0 and len(trap["points"]["ta"]) > 0
    print(f"   - Validated {len(traps)} bilingual TNPSC trap blocks.")

    q_rev = content.get("quick_revision", {})
    assert "en" in q_rev and "ta" in q_rev
    assert len(q_rev["en"]) >= 8 and len(q_rev["ta"]) >= 8
    print("   ✅ TNPSC Traps & 2-Minute Quick Revision verified.")

    # 8. Navigation & Availability Integration
    print("\n[STEP 8] Verifying Navigation & Topic Registration Integration")
    topic_meta = get_topic_metadata_by_id("polity", "polity_directive_principles_part_1")
    assert topic_meta is not None, "❌ Failed to load topic metadata for polity_directive_principles_part_1"
    assert topic_meta["part"] == 1 and topic_meta["total_parts"] == 3

    avail = check_repository_availability("polity", "polity_directive_principles_part_1")
    print(f"   - Topic Availability: {avail}")
    assert avail.get("notes") == True, "❌ Notes not reported available by check_repository_availability!"
    print("   ✅ Topic registration & availability check PASSED.")

    print("\n================================================================================")
    print("🏆 ALL VERIFICATION CHECKS PASSED FOR DPSP PART 1 NOTES!")
    print("================================================================================")

if __name__ == "__main__":
    test_dpsp_part1_notes_flow()
