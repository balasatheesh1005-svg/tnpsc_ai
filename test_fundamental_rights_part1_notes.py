# -*- coding: utf-8 -*-
"""
Verification Suite for Fundamental Rights - Part 1 Notes (Full Audit)
"""

import sys
import json
import os

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

from core.topics_loader import get_topic_metadata_by_id, get_topic_metadata_list
from core.navigation_v2.navigation_state import check_repository_availability

def run_fr_part1_notes_verification():
    print("================================================================================")
    print("🚀 RUNNING TNPSC NOVA AI - FUNDAMENTAL RIGHTS PART 1 NOTES VERIFICATION SUITE")
    print("================================================================================")

    # 1. File Existence & JSON parsing
    note_path = "data/notes/polity/fundamental_rights_part_1.json"
    print(f"\n[STEP 1] Validating File Existence & JSON Parsing: {note_path}")
    assert os.path.exists(note_path), f"❌ File not found: {note_path}"
    
    with open(note_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    print("   ✅ File exists and parses cleanly as valid JSON.")

    # 2. Metadata Audit
    print("\n[STEP 2] Meta & Metadata Block Audit")
    meta = data.get("meta", {})
    assert meta.get("topic_id") == "polity_fundamental_rights_part_1", "❌ Incorrect topic_id"
    assert meta.get("repository_id") == "polity_fundamental_rights", "❌ Incorrect repository_id"
    assert meta.get("part") == 1, "❌ Part must be 1"
    assert meta.get("total_parts") == 3, "❌ Total parts must be 3"
    assert meta.get("subject") == "polity", "❌ Subject must be polity"
    print("   ✅ Meta block values verified.")

    # 3. Section & Content Scope Audit
    print("\n[STEP 3] Section & Content Scope Audit")
    sections = data.get("sections", [])
    content = data.get("content", {})
    
    sec_ids = [s["id"] for s in sections]
    expected_sec_ids = [
        "sec_fr_overview", "sec_article_12", "sec_article_13", "sec_article_14",
        "sec_article_15", "sec_article_16", "sec_article_17", "sec_article_18",
        "sec_case_laws", "sec_traps_connections"
    ]
    for esid in expected_sec_ids:
        assert esid in sec_ids, f"❌ Missing section ID: {esid}"
        assert esid in content, f"❌ Missing section content key: {esid}"

    print(f"   - Verified all {len(expected_sec_ids)} core sections present.")

    # 4. Tables Audit (All 8 Mandatory Tables)
    print("\n[STEP 4] Comparison Tables Audit (8 Tables Required)")
    tables = data.get("tables", [])
    tbl_ids = [t["id"] for t in tables]
    expected_tbls = [
        "tbl_art12_vs_art13",
        "tbl_eq_law_vs_eq_protection",
        "tbl_art14_15_16_comparison",
        "tbl_art15_vs_art16",
        "tbl_art15_4_5_6_comparison",
        "tbl_art16_4_4a_4b_6_comparison",
        "tbl_severability_vs_eclipse",
        "tbl_art17_vs_art18"
    ]
    for etid in expected_tbls:
        assert etid in tbl_ids, f"❌ Missing comparison table: {etid}"

    for tbl in tables:
        assert "headers_en" in tbl and "headers_ta" in tbl
        assert "rows_en" in tbl and "rows_ta" in tbl
        assert len(tbl["rows_en"]) == len(tbl["rows_ta"])

    print(f"   ✅ All {len(expected_tbls)} required comparison tables present and structurally valid.")

    # 5. Concept Map & Revision Cards Audit
    print("\n[STEP 5] Concept Map & Revision Cards Audit")
    cmap = data.get("concept_map", [])
    rcards = data.get("revision_cards", [])
    assert len(cmap) >= 8, "❌ Concept map must have at least 8 nodes"
    assert len(rcards) >= 8, "❌ Revision cards must have at least 8 cards"
    print(f"   ✅ Concept map ({len(cmap)} nodes) and Revision Cards ({len(rcards)} cards) verified.")

    # 6. Important Facts & Traps Audit
    print("\n[STEP 6] Important Facts & TNPSC Traps Audit")
    facts = data.get("important_facts", {})
    traps = data.get("tnpsc_traps", [])
    assert len(facts.get("en", [])) >= 8, "❌ Missing English important facts"
    assert len(facts.get("ta", [])) >= 8, "❌ Missing Tamil important facts"
    assert len(traps) >= 6, "❌ TNPSC traps must have at least 6 items"
    print(f"   ✅ Important Facts ({len(facts['en'])} items) & TNPSC Traps ({len(traps)} items) verified.")

    # 7. Topic Discovery & Navigation Integration
    print("\n[STEP 7] Topic Discovery & Navigation Integration")
    meta_info = get_topic_metadata_by_id("polity", "polity_fundamental_rights_part_1")
    assert meta_info is not None, "❌ Topic not discovered by topics_loader!"
    assert meta_info["display_title"] == "Fundamental Rights – Part 1"
    
    nav_avail = check_repository_availability("polity", "polity_fundamental_rights_part_1")
    print(f"   - Availability State: {nav_avail}")
    assert nav_avail.get("notes") == True, "❌ Notes repository should show available!"
    print("   ✅ Topic Discovery & Navigation Availability PASSED")

    # 8. Regression Check on Existing Notes
    print("\n[STEP 8] Regression Check on Existing Notes")
    reg_topics = [
        "polity_historical_background_part1",
        "polity_making_of_indian_constitution_part_1",
        "polity_salient_features_of_the_indian_constitution_part_1",
        "polity_preamble_part_1"
    ]
    for rtop in reg_topics:
        t_meta = get_topic_metadata_by_id("polity", rtop)
        assert t_meta is not None, f"❌ Regression failure for {rtop}"
        t_avail = check_repository_availability("polity", rtop)
        assert t_avail.get("notes") == True, f"❌ Notes availability broken for {rtop}"
        print(f"   [OK] {rtop} -> Notes available.")

    print("\n================================================================================")
    print("🎉 ALL 8 VERIFICATION STEPS PASSED WITH 100% SUCCESS FOR PART 1!")
    print("================================================================================")

if __name__ == "__main__":
    run_fr_part1_notes_verification()
