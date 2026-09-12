# -*- coding: utf-8 -*-
"""
Audit all 8 Core Finance Commission MCQ files (325 MCQs) for stem collisions and schema integrity.
"""
import json
import os
from collections import Counter

files = [
    ("Easy", "data/questions/polity/fc_easy.json", 50, "FC_E_"),
    ("Medium", "data/questions/polity/fc_medium.json", 50, "FC_M_"),
    ("Hard", "data/questions/polity/fc_hard.json", 50, "FC_H_"),
    ("Statement", "data/questions/polity/fc_statement_based.json", 50, "FC_S_"),
    ("Reasoning", "data/questions/polity/fc_reasoning.json", 25, "FC_R_"),
    ("Chronology", "data/questions/polity/fc_chronology.json", 25, "FC_C_"),
    ("Match", "data/questions/polity/fc_match_the_following.json", 25, "FC_MF_"),
    ("PYQ", "data/questions/polity/fc_pyq.json", 50, "FC_PYQ_"),
]

all_qs = []
all_stems = set()
collisions = []
all_keys = Counter()

print("--- AUDITING FINANCE COMMISSION CORE 325 MCQS ---")
for name, fpath, expected_count, prefix in files:
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"{name:12}: {len(data)} questions (expected {expected_count})")
    assert len(data) == expected_count, f"Mismatch in {name}: expected {expected_count}, got {len(data)}"
    for q in data:
        qid = q["id"]
        assert qid.startswith(prefix), f"Invalid prefix for {qid} in {name}"
        stem = q["question_en"].strip().lower()
        if stem in all_stems:
            collisions.append((qid, stem))
        all_stems.add(stem)
        all_qs.append(q)
        all_keys[q["correct_answer"]] += 1

print(f"\nTotal Core Questions: {len(all_qs)}")
print(f"Unique Stems: {len(all_stems)}")
print(f"Collisions: {len(collisions)}")
if collisions:
    for c in collisions:
        print(f"  Collision: {c}")
else:
    print("Zero Collisions in Core 325 MCQs! 100% Unique Stems.")

print(f"Overall Key Distribution across Core 325: {dict(all_keys)}")
