import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

def test_part3():
    print("==================================================")
    print("VALIDATING VICE-PRESIDENT PART 3 NOTES")
    print("==================================================")
    
    path = "data/notes/polity/vice_president_part_3.json"
    assert os.path.exists(path), f"❌ File missing: {path}"
    
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    meta = data.get("meta", {})
    assert meta.get("topic_id") == "polity_vice_president_part_3", f"Invalid topic_id: {meta.get('topic_id')}"
    assert meta.get("part") == 3, f"Invalid part: {meta.get('part')}"
    assert meta.get("total_parts") == 3, f"Invalid total_parts: {meta.get('total_parts')}"
    print("  ✅ Meta tags validated: part = 3, total_parts = 3")
    
    content = data.get("content", {})
    tables = content.get("comparison_tables") or content.get("comparison") or []
    assert len(tables) == 8, f"Expected 8 master comparison tables, got {len(tables)}"
    for idx, t in enumerate(tables, 1):
        assert "headers_en" in t and len(t["headers_en"]) > 0, f"Table {idx} missing headers_en"
        assert "headers_ta" in t and len(t["headers_ta"]) > 0, f"Table {idx} missing headers_ta"
        assert "rows_en" in t and len(t["rows_en"]) > 0, f"Table {idx} missing rows_en"
        assert "rows_ta" in t and len(t["rows_ta"]) > 0, f"Table {idx} missing rows_ta"
        assert len(t["rows_en"]) == len(t["rows_ta"]), f"Table {idx} row count mismatch"
        for r_idx, r in enumerate(t["rows_en"]):
            assert len(r) == len(t["headers_en"]), f"Table {idx} Row EN {r_idx} len mismatch"
        for r_idx, r in enumerate(t["rows_ta"]):
            assert len(r) == len(t["headers_ta"]), f"Table {idx} Row TA {r_idx} len mismatch"
    print(f"  ✅ All {len(tables)} master comparison tables validated for headers, rows & column alignment!")
    
    mind_map = content.get("mind_map", [])
    assert len(mind_map) > 0, "Mind map missing"
    print("  ✅ Mind map validated!")
    
    traps = content.get("tnpsc_traps", [])
    assert len(traps) >= 6, f"Expected at least 6 TNPSC traps, got {len(traps)}"
    print(f"  ✅ All {len(traps)} TNPSC traps validated!")
    
    rev = content.get("revision_cards", [])
    assert len(rev) == 12, f"Expected 12 revision cards, got {len(rev)}"
    print(f"  ✅ All {len(rev)} revision cards validated!")
    
    print("==================================================")
    print("PART 3 VALIDATION SUCCESS: PASSED 100%")
    print("==================================================")

if __name__ == "__main__":
    test_part3()
