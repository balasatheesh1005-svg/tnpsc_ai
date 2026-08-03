import sys
import json
import os

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

from core.topics_loader import get_topic_metadata_by_id
from core.navigation_v2.navigation_state import check_repository_availability
from core.question_loader import load_questions

print("=== VERIFYING HISTORICAL BACKGROUND VS MAKING OF INDIAN CONSTITUTION FLOW ===")

# Test 1: Structure Metadata Check
hb_parts = ["polity_historical_background_part1", "polity_historical_background_part2", "polity_historical_background_part3", "polity_historical_background_part4"]
mic_parts = ["polity_making_of_indian_constitution_part_1", "polity_making_of_indian_constitution_part_2", "polity_making_of_indian_constitution_part_3"]

print("\n--- 1. Historical Background Metadata Mappings ---")
for hb in hb_parts:
    meta = get_topic_metadata_by_id("polity", hb)
    print(f"Topic ID: {meta['topic_id']} -> Repository ID: {meta['repository_id']} (Display: {meta['display_title']})")
    assert meta["repository_id"] == "polity_historical_background", f"HB Mismatch for {hb}"

print("\n--- 2. Making of Indian Constitution Metadata Mappings ---")
for mic in mic_parts:
    meta = get_topic_metadata_by_id("polity", mic)
    print(f"Topic ID: {meta['topic_id']} -> Repository ID: {meta['repository_id']} (Display: {meta['display_title']})")
    assert meta["repository_id"] == "polity_making_of_indian_constitution", f"MIC Mismatch for {mic}"

print("\n--- 3. Availability Check for Making of Indian Constitution Parts ---")
for mic in mic_parts:
    avail = check_repository_availability("polity", mic)
    print(f"{mic} -> Notes Available: {avail['notes']}, Easy MCQs Available: {avail['easy']}")
    assert avail["notes"] == True, f"Notes missing for {mic}"
    assert avail["easy"] == True, f"Easy MCQs missing for {mic}"

print("\n--- 4. Question Loading Verification for All Parts ---")
for idx, mic in enumerate(mic_parts, 1):
    meta = get_topic_metadata_by_id("polity", mic)
    qs = load_questions(meta["repository_id"], "easy")
    print(f"Part {idx} ({meta['display_title']}) -> Loaded {len(qs)} questions from '{meta['repository_id']}_easy.json'")
    assert len(qs) == 50, f"Expected 50 questions for {mic}, got {len(qs)}"

print("\n[OK] ALL VERIFICATIONS PASSED SUCCESSFULLY!")
