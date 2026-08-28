import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

def audit_president_part3():
    print("==========================================================================")
    print("🚀 AUDITING PRESIDENT PART 3 NOTES JSON & UI LOAD")
    print("==========================================================================")

    # 1. Part 1 & Part 2 safety check
    p1_path = "data/notes/polity/president_part_1.json"
    p2_path = "data/notes/polity/president_part_2.json"
    assert os.path.exists(p1_path), f"❌ President Part 1 file missing! {p1_path}"
    assert os.path.exists(p2_path), f"❌ President Part 2 file missing! {p2_path}"
    print("✅ Part 1 and Part 2 files intact!")

    # 2. Part 3 check
    filepath = "data/notes/polity/president_part_3.json"
    assert os.path.exists(filepath), f"❌ File missing: {filepath}"

    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    meta = data.get("meta", {})
    assert meta.get("topic_id") == "polity_president_part_3", f"❌ Invalid topic_id: {meta.get('topic_id')}"
    assert meta.get("part") == 3, f"❌ Invalid part: {meta.get('part')}"
    assert meta.get("total_parts") == 3, f"❌ Invalid total_parts: {meta.get('total_parts')}"
    print("✅ Meta tags verified!")

    sections = data.get("sections", [])
    assert len(sections) == 12, f"❌ Expected 12 sections, got {len(sections)}"
    print(f"✅ Verified {len(sections)} section definitions!")

    content = data.get("content", {})
    required_content_keys = [
        "definition", "introduction", "sec_discretion_and_govt_formation",
        "sec_hung_house_and_floor_test", "sec_emergency_overview_and_352",
        "sec_art_358_359_fr_suspension", "sec_presidents_rule_art_356",
        "sec_financial_emergency_art_360", "sec_impeachment_procedure_art_61",
        "sec_vacancy_acting_president_succession", "sec_constitutional_crisis_scenarios",
        "comparison_tables", "mind_map", "tnpsc_traps",
        "important_facts", "quick_revision", "master_map", "revision_cards"
    ]
    for key in required_content_keys:
        assert key in content, f"❌ Missing content key: {key}"
    print("✅ All required content keys present!")

    tables = content.get("comparison_tables", [])
    assert len(tables) >= 10, f"❌ Expected at least 10 comparison tables, got {len(tables)}"
    for idx, tbl in enumerate(tables, 1):
        assert "headers_en" in tbl and "headers_ta" in tbl, f"❌ Table {idx} missing headers"
        assert "rows_en" in tbl and "rows_ta" in tbl, f"❌ Table {idx} missing rows"
        assert len(tbl["rows_en"]) == len(tbl["rows_ta"]), f"❌ Table {idx} row count mismatch"
    print(f"✅ Verified all {len(tables)} comparison tables (EN + TA)!")

    mind_map = content.get("mind_map", [])
    assert len(mind_map) > 0, "❌ Mind map empty"
    print("✅ Mind map structure verified!")

    traps = content.get("tnpsc_traps", [])
    assert len(traps) >= 10, f"❌ Expected at least 10 TNPSC trap points, got {len(traps)}"
    for idx, tr in enumerate(traps, 1):
        pts = tr.get("points", {})
        assert len(pts.get("en", [])) > 0, f"❌ Trap {idx} missing EN points"
        assert len(pts.get("ta", [])) > 0, f"❌ Trap {idx} missing TA points"
    print(f"✅ Verified all {len(traps)} bilingual TNPSC trap points!")

    # Revision checks
    assert "en" in content["important_facts"] and "ta" in content["important_facts"], "❌ Missing important_facts bilingual"
    assert "en" in content["quick_revision"] and "ta" in content["quick_revision"], "❌ Missing quick_revision bilingual"
    assert "en" in content["master_map"] and "ta" in content["master_map"], "❌ Missing master_map bilingual"
    print("✅ Verified Must Remember, 2-Minute Revision, and Master Map!")

    # Candidate resolution check
    topic_id = "polity_president_part_3"
    subject = "polity"
    note_basename = topic_id[len(subject) + 1:] # president_part_3
    cand_path = f"data/notes/{subject}/{note_basename}.json"
    assert os.path.exists(cand_path), f"❌ UI Resolution path failed: {cand_path}"
    print(f"✅ UI Notes resolution path confirmed: {cand_path}")

    print("\nSUCCESS: President Part 3 Notes static and UI validation PASSED!")

if __name__ == "__main__":
    audit_president_part3()
