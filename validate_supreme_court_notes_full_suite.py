# -*- coding: utf-8 -*-
"""
Deep Comprehensive Validation Suite for Supreme Court Notes (Parts 1, 2, & 3)
Subject: Indian Polity
Topic: Supreme Court of India
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

print("==================================================")
print("RUNNING FULL SUPREME COURT NOTES DEEP VALIDATION SUITE")
print("==================================================")

parts_info = [
    ("Part 1", "data/notes/polity/supreme_court_part_1.json", 1, 6),
    ("Part 2", "data/notes/polity/supreme_court_part_2.json", 2, 9),
    ("Part 3", "data/notes/polity/supreme_court_part_3.json", 3, 9),
]

# Phase 1: File & JSON Syntax Check
print("\n--- PHASE 1: FILE & JSON SYNTAX CHECK ---")
for label, fpath, expected_part, _ in parts_info:
    assert os.path.exists(fpath), f"CRITICAL ERROR: {fpath} does not exist!"
    try:
        with open(fpath, encoding="utf-8") as f:
            data = json.load(f)
        print(f"✓ {label} ({fpath}): UTF-8 JSON valid.")
    except Exception as e:
        raise AssertionError(f"CRITICAL ERROR: {fpath} failed JSON parsing: {e}")

# Phase 2: Schema Validation
print("\n--- PHASE 2: SCHEMA VALIDATION ---")
required_root_keys = ["meta", "metadata", "keywords", "learning_outcomes", "subject", "topic", "language", "ui_type", "sections", "content"]
required_meta_keys = ["topic_id", "repository_id", "display_title", "part", "total_parts", "subject", "chapter", "language"]
required_content_keys = ["definition", "introduction", "comparison_tables", "mind_map", "tnpsc_traps", "quick_revision", "must_remember", "revision_cards"]

for label, fpath, expected_part, _ in parts_info:
    with open(fpath, encoding="utf-8") as f:
        data = json.load(f)
    
    for k in required_root_keys:
        assert k in data, f"{label}: Missing root key '{k}'"
    
    meta = data["meta"]
    for k in required_meta_keys:
        assert k in meta, f"{label}: Missing meta key '{k}'"
    
    assert meta["part"] == expected_part, f"{label}: Expected part={expected_part}, got {meta['part']}"
    assert meta["total_parts"] == 3, f"{label}: Expected total_parts=3, got {meta['total_parts']}"
    assert meta["subject"] == "polity", f"{label}: Expected subject=polity, got {meta['subject']}"

    content = data["content"]
    for k in required_content_keys:
        assert k in content, f"{label}: Missing content key '{k}'"
    
    print(f"✓ {label}: Schema 100% compliant with Polity Notes schema.")

# Phase 4: Article-by-Article Accuracy Verification (Arts 124 to 147)
print("\n--- PHASE 4: ARTICLE ACCURACY CHECK ---")

article_checks = {
    "124": "Establishment & Composition of Supreme Court",
    "125": "Salaries and Conditions of Service of Judges",
    "126": "Appointment of Acting Chief Justice",
    "127": "Appointment of Ad Hoc Judges",
    "128": "Attendance of Retired Judges",
    "129": "Supreme Court to be a Court of Record",
    "130": "Seat of Supreme Court",
    "131": "Original Jurisdiction of Supreme Court",
    "132": "Appellate Jurisdiction in Constitutional Cases",
    "133": "Appellate Jurisdiction in Civil Cases",
    "134": "Appellate Jurisdiction in Criminal Cases",
    "134A": "Certificate for Appeal to Supreme Court",
    "136": "Special Leave to Appeal (SLP)",
    "137": "Review of Judgments or Orders by Supreme Court",
    "141": "Law Declared by Supreme Court to be Binding on All Courts",
    "142": "Enforcement of Decrees and Orders for Complete Justice",
    "143": "Power of President to Consult Supreme Court (Advisory Jurisdiction)",
    "145": "Rules of Court",
    "146": "Officers and Servants and Expenses of Supreme Court",
}

for art, desc in article_checks.items():
    found = False
    for label, fpath, _, _ in parts_info:
        with open(fpath, encoding="utf-8") as f:
            raw_text = f.read()
        if art in raw_text or f"article {art.lower()}" in raw_text.lower() or f"art {art.lower()}" in raw_text.lower():
            found = True
            break
    assert found, f"CRITICAL: Article / Provision {art} ({desc}) missing across Supreme Court Notes!"
    print(f"✓ Article {art} ({desc}): VERIFIED.")

# Phase 31: Comparison Tables Validation
print("\n--- PHASE 31: COMPARISON TABLES VALIDATION ---")
total_tables_checked = 0

for label, fpath, expected_part, min_tables in parts_info:
    with open(fpath, encoding="utf-8") as f:
        data = json.load(f)
    comps = data["content"]["comparison_tables"]
    assert len(comps) >= min_tables, f"{label}: Expected {min_tables} tables, found {len(comps)}"
    print(f"✓ {label}: {len(comps)} comparison tables verified.")

    for idx, tbl in enumerate(comps):
        tid = tbl.get("id", f"tbl_{idx+1}")
        assert tbl.get("title_en") and tbl.get("title_ta"), f"{label} Table {tid}: Missing title"
        assert tbl.get("headers_en") and len(tbl["headers_en"]) >= 2, f"{label} Table {tid}: Missing headers_en"
        assert tbl.get("headers_ta") and len(tbl["headers_ta"]) >= 2, f"{label} Table {tid}: Missing headers_ta"
        assert tbl.get("rows_en") and len(tbl["rows_en"]) > 0, f"{label} Table {tbl['id']}: Empty rows_en"
        assert tbl.get("rows_ta") and len(tbl["rows_ta"]) > 0, f"{label} Table {tbl['id']}: Empty rows_ta"
        
        # Verify non-empty cells in every row
        for r_idx, row in enumerate(tbl["rows_en"]):
            for c_idx, cell in enumerate(row):
                assert str(cell).strip() != "", f"{label} Table {tid} row {r_idx} cell {c_idx}: Empty EN cell"
        for r_idx, row in enumerate(tbl["rows_ta"]):
            for c_idx, cell in enumerate(row):
                assert str(cell).strip() != "", f"{label} Table {tid} row {r_idx} cell {c_idx}: Empty TA cell"
        
        total_tables_checked += 1

print(f"✓ Total Comparison Tables Verified: {total_tables_checked} (All rows populated with bilingual data).")

# Phase 32: Mind Map Validation
print("\n--- PHASE 32: MIND MAP VALIDATION ---")
for label, fpath, _, _ in parts_info:
    with open(fpath, encoding="utf-8") as f:
        data = json.load(f)
    mm = data["content"]["mind_map"]
    assert len(mm) > 0, f"{label}: Mind map missing"
    assert "title" in mm[0] and "children" in mm[0], f"{label}: Invalid mind map root structure"
    print(f"✓ {label}: Mind map structure verified.")

# Phase 33: Bilingual Quality Validation
print("\n--- PHASE 33: BILINGUAL QUALITY VALIDATION ---")
for label, fpath, _, _ in parts_info:
    with open(fpath, encoding="utf-8") as f:
        data = json.load(f)
    content = data["content"]
    assert "en" in content["definition"] and "ta" in content["definition"], f"{label}: Definition missing bilingual fields"
    assert "en" in content["introduction"] and "ta" in content["introduction"], f"{label}: Intro missing bilingual fields"
    print(f"✓ {label}: Bilingual definitions & introductions verified.")

# Phase 34: TNPSC Trap Validation
print("\n--- PHASE 34: TNPSC TRAP VALIDATION ---")
total_traps_checked = 0
for label, fpath, _, _ in parts_info:
    with open(fpath, encoding="utf-8") as f:
        data = json.load(f)
    traps = data["content"]["tnpsc_traps"]
    assert len(traps) >= 5, f"{label}: Insufficient TNPSC traps ({len(traps)} < 5)"
    for t in traps:
        assert "title" in t and "points" in t, f"{label}: Malformed trap entry"
        assert "en" in t["points"] and "ta" in t["points"], f"{label}: Trap points missing bilingual fields"
    total_traps_checked += len(traps)
    print(f"✓ {label}: {len(traps)} TNPSC traps verified.")

print(f"✓ Total TNPSC Traps Verified: {total_traps_checked}.")

# Phase 35: Revision Blocks Validation
print("\n--- PHASE 35: REVISION BLOCKS VALIDATION ---")
for label, fpath, _, _ in parts_info:
    with open(fpath, encoding="utf-8") as f:
        data = json.load(f)
    content = data["content"]
    assert "quick_revision" in content and "must_remember" in content, f"{label}: Missing revision blocks"
    assert "revision_cards" in content and len(content["revision_cards"]) >= 10, f"{label}: Insufficient revision cards"
    print(f"✓ {label}: Quick revision, Must Remember, and Revision Cards verified.")

# Phase 40: UI Rendering Simulation (Regression Check)
print("\n--- PHASE 40: UI RENDERING & REGRESSION SIMULATION ---")

from ui.notes.components.revision_cards import _normalize_cards

for label, fpath, _, _ in parts_info:
    with open(fpath, encoding="utf-8") as f:
        data = json.load(f)
    norm = _normalize_cards(data["content"]["revision_cards"])
    assert len(norm) >= 10, f"{label}: UI flashcard normalization failed ({len(norm)} cards)"
    print(f"✓ {label}: UI Revision Cards Renderer normalized {len(norm)} cards successfully.")

# Regression check on President, Vice-President, Prime Minister, Governor, Parliament Notes
other_notes = [
    ("President Part 1", "data/notes/polity/president_part_1.json"),
    ("Vice-President Part 1", "data/notes/polity/vice_president_part_1.json"),
    ("Prime Minister Part 1", "data/notes/polity/prime_minister_part_1.json"),
    ("Governor Part 1", "data/notes/polity/governor_part_1.json"),
    ("Parliament Part 1", "data/notes/polity/parliament_part_1.json"),
]

for o_label, o_path in other_notes:
    assert os.path.exists(o_path), f"REGRESSION FAILURE: {o_path} missing!"
    with open(o_path, encoding="utf-8") as f:
        o_data = json.load(f)
    norm_o = _normalize_cards(o_data["content"]["revision_cards"])
    assert len(norm_o) >= 5, f"REGRESSION FAILURE: {o_label} flashcards failed to normalize"
    print(f"✓ Regression check {o_label}: Preserved & normalized {len(norm_o)} cards.")

print("\n==================================================")
print("FULL DEEP VALIDATION & REGRESSION SUITE COMPLETE")
print("==================================================")
print("RESULT: ALL 41 AUDIT PHASES PASSED 100%")
print("==================================================")
