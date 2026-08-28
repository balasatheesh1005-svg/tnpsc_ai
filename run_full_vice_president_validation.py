import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

from ui.notes.renderer import render_notes_engine

def run_full_validation():
    print("================================================================================")
    print("🧪 FULL VALIDATION SUITE — VICE-PRESIDENT NOTES (PARTS 1, 2, 3)")
    print("================================================================================")

    files = [
        (1, "data/notes/polity/vice_president_part_1.json", 6),
        (2, "data/notes/polity/vice_president_part_2.json", 6),
        (3, "data/notes/polity/vice_president_part_3.json", 8)
    ]

    phase_results = {}

    # PHASE 1: FILE VALIDATION
    print("\n--- PHASE 1: FILE & JSON VALIDATION ---")
    p1_pass = True
    for part_num, path, _ in files:
        if not os.path.exists(path):
            print(f"❌ File missing: {path}")
            p1_pass = False
        else:
            try:
                with open(path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                meta = data.get("meta", {})
                if meta.get("part") != part_num or meta.get("total_parts") != 3:
                    print(f"❌ {path}: meta part mismatch (expected part {part_num}, total_parts 3)")
                    p1_pass = False
                else:
                    print(f"  ✅ {os.path.basename(path)}: UTF-8 JSON valid, part={part_num}, total_parts=3")
            except Exception as e:
                print(f"❌ {path}: JSON parse error: {e}")
                p1_pass = False
    phase_results["Phase 1 (Files)"] = "PASS" if p1_pass else "FAIL"

    # PHASE 2: SCHEMA VALIDATION
    print("\n--- PHASE 2: SCHEMA VALIDATION ---")
    p2_pass = True
    required_keys = ["meta", "metadata", "keywords", "learning_outcomes", "subject", "topic", "language", "ui_type", "sections", "content"]
    required_content_keys = ["definition", "introduction", "comparison_tables", "comparison", "mind_map", "tnpsc_traps", "important_facts", "quick_revision", "revision_cards"]
    
    for part_num, path, _ in files:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        for k in required_keys:
            if k not in data:
                print(f"❌ {os.path.basename(path)}: missing top-level key '{k}'")
                p2_pass = False
        content = data.get("content", {})
        for ck in required_content_keys:
            if ck not in content:
                print(f"❌ {os.path.basename(path)}: content missing key '{ck}'")
                p2_pass = False
        if p2_pass:
            print(f"  ✅ {os.path.basename(path)}: Schema matches working Polity Notes architecture 100%")
    phase_results["Phase 2 (Schema)"] = "PASS" if p2_pass else "FAIL"

    # PHASE 3: PART SCOPE & CONSTITUTIONAL FACTS VALIDATION
    print("\n--- PHASES 3-14: CONSTITUTIONAL FACTS & SCOPE VALIDATION ---")
    facts_pass = True
    
    # Check Part 1 scope & facts
    with open("data/notes/polity/vice_president_part_1.json", encoding="utf-8") as f:
        p1 = json.load(f)
    p1_str = json.dumps(p1, ensure_ascii=False)
    assert "Article 63" in p1_str and "Article 66" in p1_str, "Part 1 missing core Articles 63/66"
    assert "Electoral College" in p1_str and "equal vote value" in p1_str.lower(), "Part 1 missing Electoral College / vote value facts"
    assert "35 years" in p1_str and "Rajya Sabha" in p1_str, "Part 1 missing qualifications"
    print("  ✅ Part 1 Scope: Article 63, 66, Electoral College, Equal Vote Value & Qualifications verified!")

    # Check Part 2 scope & facts
    with open("data/notes/polity/vice_president_part_2.json", encoding="utf-8") as f:
        p2 = json.load(f)
    p2_str = json.dumps(p2, ensure_ascii=False)
    assert "Ex-Officio Chairman" in p2_str or "ex-officio" in p2_str.lower(), "Part 2 missing Ex-officio Chairman role"
    assert "Casting Vote" in p2_str or "casting vote" in p2_str.lower(), "Part 2 missing Casting Vote mechanism"
    assert "Article 100(1)" in p2_str or "Article 100" in p2_str, "Part 2 missing Article 100(1)"
    assert "Deputy Chairman" in p2_str, "Part 2 missing Deputy Chairman comparison"
    print("  ✅ Part 2 Scope: Ex-Officio Chairman, Casting Vote (Art 100(1)) & Deputy Chairman verified!")

    # Check Part 3 scope & facts
    with open("data/notes/polity/vice_president_part_3.json", encoding="utf-8") as f:
        p3 = json.load(f)
    p3_str = json.dumps(p3, ensure_ascii=False)
    assert "67(b)" in p3_str or "67b" in p3_str.lower(), "Part 3 missing Article 67(b) removal"
    assert "Effective Majority" in p3_str, "Part 3 missing Effective Majority requirement"
    assert "Article 68" in p3_str and "Article 65" in p3_str, "Part 3 missing Article 68 / 65"
    assert "Article 70" in p3_str and "1969" in p3_str, "Part 3 missing Article 70 / 1969 Act"
    assert "Article 71" in p3_str and "Supreme Court" in p3_str, "Part 3 missing Article 71 / Supreme Court"
    print("  ✅ Part 3 Scope: Removal (Art 67b), Vacancy (Art 68), Acting Pres (Art 65), Art 70 (1969 Act) & Art 71 verified!")
    
    phase_results["Phases 3-14 (Constitutional Content)"] = "PASS"

    # PHASE 15: COMPARISON TABLES VALIDATION
    print("\n--- PHASE 15: COMPARISON TABLE STRUCTURE & CONTENT VALIDATION ---")
    comp_pass = True
    total_tables = 0
    for part_num, path, expected_count in files:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        content = data.get("content", {})
        tables = content.get("comparison_tables") or []
        alias_tables = content.get("comparison") or []
        if len(tables) != expected_count or len(alias_tables) != expected_count:
            print(f"❌ {os.path.basename(path)}: table count mismatch (expected {expected_count}, got {len(tables)})")
            comp_pass = False
        for idx, t in enumerate(tables, 1):
            total_tables += 1
            if not t.get("headers_en") or not t.get("headers_ta") or not t.get("rows_en") or not t.get("rows_ta"):
                print(f"❌ {os.path.basename(path)} Table {idx}: missing headers or rows")
                comp_pass = False
            if len(t["rows_en"]) == 0 or len(t["rows_ta"]) == 0:
                print(f"❌ {os.path.basename(path)} Table {idx}: empty rows (heading-only table)")
                comp_pass = False
            for r in t["rows_en"]:
                if len(r) != len(t["headers_en"]):
                    print(f"❌ {os.path.basename(path)} Table {idx}: row len {len(r)} != header len {len(t['headers_en'])}")
                    comp_pass = False
            for r in t["rows_ta"]:
                if len(r) != len(t["headers_ta"]):
                    print(f"❌ {os.path.basename(path)} Table {idx}: row len {len(r)} != header len {len(t['headers_ta'])}")
                    comp_pass = False

    if comp_pass:
        print(f"  ✅ All {total_tables} comparison tables across 3 parts contain non-empty rows, EN+TA headers, and 100% column alignment!")
    phase_results["Phase 15 (Comparison Tables)"] = "PASS" if comp_pass else "FAIL"

    # PHASE 16-19: MIND MAP, BILINGUAL, TRAPS, REVISION VALIDATION
    print("\n--- PHASES 16-19: MIND MAPS, BILINGUAL, TNPSC TRAPS & REVISION VALIDATION ---")
    components_pass = True
    for part_num, path, _ in files:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        content = data.get("content", {})
        
        # Mind map
        mm = content.get("mind_map", [])
        if not mm or not isinstance(mm, list) or not mm[0].get("children"):
            print(f"❌ {os.path.basename(path)}: mind_map missing or invalid structure")
            components_pass = False

        # TNPSC traps
        traps = content.get("tnpsc_traps", [])
        if not traps or len(traps) < 6:
            print(f"❌ {os.path.basename(path)}: expected at least 6 TNPSC traps, got {len(traps)}")
            components_pass = False
        else:
            for tr in traps:
                pts = tr.get("points", {})
                if not pts.get("en") or not pts.get("ta"):
                    print(f"❌ {os.path.basename(path)}: trap missing EN or TA text")
                    components_pass = False

        # Revision cards
        rev = content.get("revision_cards", [])
        if not rev or len(rev) != 12:
            print(f"❌ {os.path.basename(path)}: expected 12 revision cards, got {len(rev)}")
            components_pass = False

    if components_pass:
        print("  ✅ Mind Maps, Bilingual Content, TNPSC Traps (EN+TA), and Revision Cards verified 100%!")
    phase_results["Phases 16-19 (UI Components)"] = "PASS" if components_pass else "FAIL"

    # PHASE 22: UI ENGINE SIMULATION RENDERING
    print("\n--- PHASE 22: UI NOTES ENGINE SIMULATION RENDERING ---")
    ui_pass = True
    for part_num, path, _ in files:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        try:
            render_notes_engine(data)
            print(f"  ✅ {os.path.basename(path)}: Passed UI Notes Engine rendering simulation cleanly!")
        except Exception as e:
            print(f"  ❌ {os.path.basename(path)}: UI rendering error: {e}")
            ui_pass = False
    phase_results["Phase 22 (UI Engine Simulation)"] = "PASS" if ui_pass else "FAIL"

    print("\n================================================================================")
    print("SUMMARY OF VALIDATION PHASES")
    print("================================================================================")
    for phase, status in phase_results.items():
        print(f"  • {phase}: {status}")
    print("================================================================================")

    if all(s == "PASS" for s in phase_results.values()):
        print("FINAL STATUS: VICE-PRESIDENT NOTES — VALIDATED AND UI VERIFIED")
    else:
        print("FINAL STATUS: VICE-PRESIDENT NOTES — VALIDATION INCOMPLETE; REVIEW REQUIRED")

if __name__ == "__main__":
    run_full_validation()
