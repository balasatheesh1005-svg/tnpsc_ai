import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

def audit_president_part1():
    print("==========================================================================")
    print("🚀 AUDITING PRESIDENT PART 1 NOTES JSON & UI LOAD")
    print("==========================================================================")

    filepath = "data/notes/polity/president_part_1.json"
    assert os.path.exists(filepath), f"❌ File missing: {filepath}"

    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 1. Meta check
    meta = data.get("meta", {})
    assert meta.get("topic_id") == "polity_president_part_1", f"❌ Invalid topic_id: {meta.get('topic_id')}"
    assert meta.get("part") == 1, f"❌ Invalid part: {meta.get('part')}"
    assert meta.get("total_parts") == 3, f"❌ Invalid total_parts: {meta.get('total_parts')}"
    print("✅ Meta tags verified!")

    # 2. Section check
    sections = data.get("sections", [])
    assert len(sections) == 12, f"❌ Expected 12 sections, got {len(sections)}"
    print(f"✅ Verified {len(sections)} section definitions!")

    # 3. Content check
    content = data.get("content", {})
    required_content_keys = [
        "definition", "introduction", "sec_constitutional_position",
        "sec_electoral_college", "sec_value_of_votes", "sec_method_of_election",
        "sec_qualifications", "sec_conditions_of_office", "sec_oath_affirmation",
        "sec_term_resignation_re-election", "sec_vacancy_impeachment",
        "comparison_tables", "mind_map", "tnpsc_traps",
        "important_facts", "quick_revision", "revision_cards"
    ]
    for key in required_content_keys:
        assert key in content, f"❌ Missing content key: {key}"
    print("✅ All required content keys present!")

    # 4. Comparison tables check
    tables = content.get("comparison_tables", [])
    assert len(tables) == 10, f"❌ Expected 10 comparison tables, got {len(tables)}"
    for idx, tbl in enumerate(tables, 1):
        assert "headers_en" in tbl and "headers_ta" in tbl, f"❌ Table {idx} missing headers"
        assert "rows_en" in tbl and "rows_ta" in tbl, f"❌ Table {idx} missing rows"
        assert len(tbl["rows_en"]) == len(tbl["rows_ta"]), f"❌ Table {idx} row count mismatch"
    print(f"✅ Verified all 10 comparison tables (EN + TA)!")

    # 5. Mind map check
    mind_map = content.get("mind_map", [])
    assert len(mind_map) > 0, "❌ Mind map empty"
    print("✅ Mind map structure verified!")

    # 6. TNPSC Traps check
    traps = content.get("tnpsc_traps", [])
    assert len(traps) == 10, f"❌ Expected 10 TNPSC trap points, got {len(traps)}"
    for idx, tr in enumerate(traps, 1):
        pts = tr.get("points", {})
        assert len(pts.get("en", [])) > 0, f"❌ Trap {idx} missing EN points"
        assert len(pts.get("ta", [])) > 0, f"❌ Trap {idx} missing TA points"
    print("✅ Verified 10 bilingual TNPSC trap points!")

    # 7. Candidate resolution check
    topic_id = "polity_president_part_1"
    subject = "polity"
    note_basename = topic_id[len(subject) + 1:] # president_part_1
    cand_path = f"data/notes/{subject}/{note_basename}.json"
    assert os.path.exists(cand_path), f"❌ UI Resolution path failed: {cand_path}"
    print(f"✅ UI Notes resolution path confirmed: {cand_path}")

    print("\nSUCCESS: President Part 1 Notes static and UI validation PASSED!")

if __name__ == "__main__":
    audit_president_part1()
