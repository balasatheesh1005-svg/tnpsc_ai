import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

def audit_president_part2():
    print("==========================================================================")
    print("🚀 AUDITING PRESIDENT PART 2 NOTES JSON & UI LOAD")
    print("==========================================================================")

    # 1. Part 1 safety check
    p1_path = "data/notes/polity/president_part_1.json"
    assert os.path.exists(p1_path), f"❌ President Part 1 file missing! {p1_path}"
    print("✅ Part 1 file intact!")

    # 2. Part 2 check
    filepath = "data/notes/polity/president_part_2.json"
    assert os.path.exists(filepath), f"❌ File missing: {filepath}"

    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    meta = data.get("meta", {})
    assert meta.get("topic_id") == "polity_president_part_2", f"❌ Invalid topic_id: {meta.get('topic_id')}"
    assert meta.get("part") == 2, f"❌ Invalid part: {meta.get('part')}"
    assert meta.get("total_parts") == 3, f"❌ Invalid total_parts: {meta.get('total_parts')}"
    print("✅ Meta tags verified!")

    sections = data.get("sections", [])
    assert len(sections) == 12, f"❌ Expected 12 sections, got {len(sections)}"
    print(f"✅ Verified {len(sections)} section definitions!")

    content = data.get("content", {})
    required_content_keys = [
        "definition", "introduction", "sec_executive_powers",
        "sec_legislative_powers", "sec_president_and_bills", "sec_veto_powers",
        "sec_ordinance_power", "sec_financial_powers", "sec_judicial_powers",
        "sec_pardoning_power", "sec_diplomatic_military",
        "comparison_tables", "mind_map", "tnpsc_traps",
        "important_facts", "quick_revision", "revision_cards"
    ]
    for key in required_content_keys:
        assert key in content, f"❌ Missing content key: {key}"
    print("✅ All required content keys present!")

    tables = content.get("comparison_tables", [])
    assert len(tables) == 10, f"❌ Expected 10 comparison tables, got {len(tables)}"
    for idx, tbl in enumerate(tables, 1):
        assert "headers_en" in tbl and "headers_ta" in tbl, f"❌ Table {idx} missing headers"
        assert "rows_en" in tbl and "rows_ta" in tbl, f"❌ Table {idx} missing rows"
        assert len(tbl["rows_en"]) == len(tbl["rows_ta"]), f"❌ Table {idx} row count mismatch"
    print("✅ Verified all 10 comparison tables (EN + TA)!")

    mind_map = content.get("mind_map", [])
    assert len(mind_map) > 0, "❌ Mind map empty"
    print("✅ Mind map structure verified!")

    traps = content.get("tnpsc_traps", [])
    assert len(traps) == 10, f"❌ Expected 10 TNPSC trap points, got {len(traps)}"
    for idx, tr in enumerate(traps, 1):
        pts = tr.get("points", {})
        assert len(pts.get("en", [])) > 0, f"❌ Trap {idx} missing EN points"
        assert len(pts.get("ta", [])) > 0, f"❌ Trap {idx} missing TA points"
    print("✅ Verified 10 bilingual TNPSC trap points!")

    # Candidate resolution check
    topic_id = "polity_president_part_2"
    subject = "polity"
    note_basename = topic_id[len(subject) + 1:] # president_part_2
    cand_path = f"data/notes/{subject}/{note_basename}.json"
    assert os.path.exists(cand_path), f"❌ UI Resolution path failed: {cand_path}"
    print(f"✅ UI Notes resolution path confirmed: {cand_path}")

    print("\nSUCCESS: President Part 2 Notes static and UI validation PASSED!")

if __name__ == "__main__":
    audit_president_part2()
