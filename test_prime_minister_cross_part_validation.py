import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

def run_cross_part_validation():
    print("================================================================================")
    print("🧪 PRIME MINISTER NOTES: CROSS-PART VALIDATION TEST")
    print("================================================================================")

    files = [
        (1, "data/notes/polity/prime_minister_part_1.json", 5),
        (2, "data/notes/polity/prime_minister_part_2.json", 5),
        (3, "data/notes/polity/prime_minister_part_3.json", 8)
    ]

    total_tables_checked = 0

    for expected_part, path, expected_tables in files:
        fname = os.path.basename(path)
        print(f"\n▶ Testing {fname} (Part {expected_part})...")
        
        assert os.path.exists(path), f"❌ File missing: {path}"
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        meta = data.get("meta", {})
        assert meta.get("part") == expected_part, f"Part mismatch in {fname}: expected {expected_part}, got {meta.get('part')}"
        assert meta.get("total_parts") == 3, f"total_parts mismatch in {fname}: expected 3, got {meta.get('total_parts')}"
        print(f"  ✅ {fname}: Meta verified (part = {expected_part}, total_parts = 3)")

        content = data.get("content", {})

        # Validate Comparison Tables
        tables = content.get("comparison_tables") or content.get("comparison") or []
        assert len(tables) == expected_tables, f"{fname}: Expected {expected_tables} tables, got {len(tables)}"
        
        for idx, tbl in enumerate(tables, 1):
            title = tbl.get("title_en") or tbl.get("id")
            headers_en = tbl.get("headers_en", [])
            headers_ta = tbl.get("headers_ta", [])
            rows_en = tbl.get("rows_en", [])
            rows_ta = tbl.get("rows_ta", [])

            assert len(headers_en) > 0, f"{fname} Table {idx} ('{title}'): headers_en empty!"
            assert len(headers_ta) > 0, f"{fname} Table {idx} ('{title}'): headers_ta empty!"
            assert len(rows_en) > 0, f"{fname} Table {idx} ('{title}'): rows_en empty (heading-only table)!"
            assert len(rows_ta) > 0, f"{fname} Table {idx} ('{title}'): rows_ta empty (heading-only table)!"
            assert len(rows_en) == len(rows_ta), f"{fname} Table {idx} ('{title}'): EN rows ({len(rows_en)}) != TA rows ({len(rows_ta)})!"

            for r_idx, row in enumerate(rows_en):
                assert len(row) == len(headers_en), f"{fname} Table {idx} Row EN {r_idx} len ({len(row)}) != headers_en ({len(headers_en)})"
            for r_idx, row in enumerate(rows_ta):
                assert len(row) == len(headers_ta), f"{fname} Table {idx} Row TA {r_idx} len ({len(row)}) != headers_ta ({len(headers_ta)})"

            total_tables_checked += 1

        print(f"  ✅ {fname}: All {len(tables)} comparison tables validated for non-empty rows and EN+TA alignment!")

        # Mind map check
        mind_map = content.get("mind_map", [])
        assert len(mind_map) > 0, f"{fname}: Mind map missing!"
        print(f"  ✅ {fname}: Mind map present and validated!")

        # Traps check
        traps = content.get("tnpsc_traps", [])
        assert len(traps) >= 6, f"{fname}: TNPSC traps count low ({len(traps)})!"
        print(f"  ✅ {fname}: {len(traps)} TNPSC traps validated!")

        # Revision check
        imp_facts = content.get("important_facts", {})
        quick_rev = content.get("quick_revision", {})
        rev_cards = content.get("revision_cards", [])
        assert len(imp_facts.get("en", [])) > 0 and len(imp_facts.get("ta", [])) > 0, f"{fname}: Important facts missing"
        assert len(quick_rev.get("en", [])) > 0 and len(quick_rev.get("ta", [])) > 0, f"{fname}: Quick revision missing"
        assert len(rev_cards) >= 10, f"{fname}: Revision cards count low ({len(rev_cards)})"
        print(f"  ✅ {fname}: MUST REMEMBER, 2-Min Revision & {len(rev_cards)} Revision Cards validated!")

    # Confirm President & Vice-President Notes still exist and load cleanly (regression check)
    print("\n▶ Running Quick Regression Check on Existing President & Vice-President Notes...")
    regression_files = [
        "data/notes/polity/president_part_1.json",
        "data/notes/polity/president_part_2.json",
        "data/notes/polity/president_part_3.json",
        "data/notes/polity/vice_president_part_1.json",
        "data/notes/polity/vice_president_part_2.json",
        "data/notes/polity/vice_president_part_3.json"
    ]
    for p_path in regression_files:
        assert os.path.exists(p_path), f"Regression file missing: {p_path}"
        with open(p_path, "r", encoding="utf-8") as f:
            p_data = json.load(f)
        assert "meta" in p_data or "metadata" in p_data
        print(f"  ✅ {os.path.basename(p_path)}: Loaded cleanly with 0 errors!")

    print("================================================================================")
    print(f"🎉 ALL 3 PRIME MINISTER PARTS & {total_tables_checked} COMPARISON TABLES PASSED VALIDATION 100%!")
    print("================================================================================")

if __name__ == "__main__":
    run_cross_part_validation()
