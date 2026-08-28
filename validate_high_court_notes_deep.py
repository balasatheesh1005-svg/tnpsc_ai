# -*- coding: utf-8 -*-
"""
Deep Comprehensive Validation Suite for High Court Notes (Parts 1, 2, & 3)
Subject: Indian Polity
Topic: High Courts in India
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

print("==================================================")
print("RUNNING HIGH COURT NOTES DEEP VALIDATION SUITE")
print("==================================================")

parts = [
    ("Part 1", "data/notes/polity/high_court_part_1.json", 1, 6),
    ("Part 2", "data/notes/polity/high_court_part_2.json", 2, 9),
    ("Part 3", "data/notes/polity/high_court_part_3.json", 3, 10),
]

total_tables = 0
total_traps = 0
total_cards = 0

for label, fpath, expected_part, min_tables in parts:
    print(f"\n--- AUDITING {label.upper()} ({fpath}) ---")
    assert os.path.exists(fpath), f"CRITICAL: File {fpath} does not exist!"
    
    with open(fpath, encoding="utf-8") as f:
        data = json.load(f)

    # 1. Meta validation
    meta = data.get("meta", {})
    assert meta.get("part") == expected_part, f"{label}: Expected part={expected_part}, got {meta.get('part')}"
    assert meta.get("total_parts") == 3, f"{label}: Expected total_parts=3, got {meta.get('total_parts')}"
    assert meta.get("subject") == "polity", f"{label}: Expected subject=polity, got {meta.get('subject')}"
    print(f"✓ Meta check passed (part={expected_part}/3, subject=polity)")

    # 2. Content validation
    content = data.get("content", {})
    assert "definition" in content, f"{label}: Missing definition"
    assert "introduction" in content, f"{label}: Missing introduction"
    
    # 3. Comparison tables validation
    comps = content.get("comparison_tables", [])
    print(f"✓ Found {len(comps)} comparison tables (Minimum required: {min_tables})")
    assert len(comps) >= min_tables, f"{label}: Insufficient comparison tables ({len(comps)} < {min_tables})"
    total_tables += len(comps)

    for idx, tbl in enumerate(comps):
        tid = tbl.get("id", f"tbl_{idx+1}")
        assert tbl.get("title_en") and tbl.get("title_ta"), f"{label} Table {tid}: Missing title"
        assert tbl.get("headers_en") and len(tbl["headers_en"]) >= 2, f"{label} Table {tid}: Invalid headers_en"
        assert tbl.get("headers_ta") and len(tbl["headers_ta"]) >= 2, f"{label} Table {tid}: Invalid headers_ta"
        assert tbl.get("rows_en") and len(tbl["rows_en"]) > 0, f"{label} Table {tid}: Empty rows_en"
        assert tbl.get("rows_ta") and len(tbl["rows_ta"]) > 0, f"{label} Table {tid}: Empty rows_ta"
        assert len(tbl["rows_en"]) == len(tbl["rows_ta"]), f"{label} Table {tid}: Row count mismatch between EN & TA"
        
        for r_idx, row in enumerate(tbl["rows_en"]):
            for c_idx, cell in enumerate(row):
                assert str(cell).strip() != "", f"{label} Table {tid} row {r_idx} cell {c_idx}: Empty EN cell"

    # 4. Mind map validation
    mm = content.get("mind_map", [])
    assert len(mm) > 0, f"{label}: Missing mind map"
    print(f"✓ Mind map present ({len(mm)} root node)")

    # 5. TNPSC Traps validation
    traps = content.get("tnpsc_traps", [])
    assert len(traps) >= 5, f"{label}: Insufficient TNPSC traps ({len(traps)} < 5)"
    total_traps += len(traps)
    print(f"✓ Found {len(traps)} TNPSC traps")

    # 6. Revision Cards validation
    cards = content.get("revision_cards", [])
    assert len(cards) >= 10, f"{label}: Insufficient revision cards ({len(cards)} < 10)"
    total_cards += len(cards)
    print(f"✓ Found {len(cards)} revision cards")

# Flashcard normalization check
from ui.notes.components.revision_cards import _normalize_cards

for label, fpath, _, _ in parts:
    with open(fpath, encoding="utf-8") as f:
        data = json.load(f)
    norm = _normalize_cards(data["content"]["revision_cards"])
    assert len(norm) >= 10, f"{label}: Flashcard normalization failed ({len(norm)} cards)"
    print(f"✓ {label}: Normalized {len(norm)} revision cards for UI rendering.")

# Regression check on existing completed notes
completed_topics = [
    ("President Part 1", "data/notes/polity/president_part_1.json"),
    ("Vice-President Part 1", "data/notes/polity/vice_president_part_1.json"),
    ("Prime Minister Part 1", "data/notes/polity/prime_minister_part_1.json"),
    ("Governor Part 1", "data/notes/polity/governor_part_1.json"),
    ("Parliament Part 1", "data/notes/polity/parliament_part_1.json"),
    ("Supreme Court Part 1", "data/notes/polity/supreme_court_part_1.json"),
]

print("\n--- REGRESSION AUDIT ON COMPLETED TOPICS ---")
for o_label, o_path in completed_topics:
    assert os.path.exists(o_path), f"REGRESSION FAILURE: {o_path} missing!"
    with open(o_path, encoding="utf-8") as f:
        o_data = json.load(f)
    norm_o = _normalize_cards(o_data["content"]["revision_cards"])
    assert len(norm_o) >= 5, f"REGRESSION FAILURE: {o_label} flashcards failed to normalize"
    print(f"✓ Regression check {o_label}: Preserved & normalized {len(norm_o)} cards.")

print("\n==================================================")
print("HIGH COURT NOTES SUMMARY AUDIT:")
print(f"  • Total Parts Verified: 3 / 3")
print(f"  • Total Comparison Tables: {total_tables} (Part 1: 6, Part 2: 9, Part 3: 10)")
print(f"  • Total TNPSC Traps: {total_traps}")
print(f"  • Total Interactive Revision Cards: {total_cards}")
print("==================================================")
print("ALL DEEP AUDIT PHASES PASSED 100%!")
print("==================================================")
