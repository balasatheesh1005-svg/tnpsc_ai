import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from core.topics_loader import get_topic_metadata_by_id, get_topic_metadata_list
from core.navigation_v2.navigation_state import check_repository_availability
from ui.pages.notes import load_note

def test_preamble_part2():
    print("==================================================")
    print("RUNNING PREAMBLE PART 2 NOTES VERIFICATION SUITE")
    print("==================================================")

    subject = "polity"
    topic_id = "polity_preamble_part_2"

    # 1. Metadata resolution test
    meta = get_topic_metadata_by_id(subject, topic_id)
    assert meta is not None, f"Metadata resolution failed for {topic_id}"
    print(f"\n1. Metadata Resolution:")
    print(f"   - topic_id: {meta.get('topic_id')}")
    print(f"   - repository_id: {meta.get('repository_id')}")
    print(f"   - display_title: {meta.get('display_title')}")
    print(f"   - part: {meta.get('part')} / {meta.get('total_parts')}")
    
    assert meta["topic_id"] == "polity_preamble_part_2", "topic_id mismatch!"
    assert meta["repository_id"] == "polity_preamble", "repository_id mismatch!"
    print("   [OK] Metadata test PASSED")

    # 2. Availability Check Test
    avail = check_repository_availability(subject, meta["topic_id"])
    print(f"\n2. Repository Availability Check:")
    print(f"   - notes: {avail.get('notes')}")
    assert avail.get("notes") == True, "Notes should be available for Preamble Part 2!"
    print("   [OK] Availability check PASSED")

    # 3. Load Notes JSON Payload
    file_path = "data/notes/polity/preamble_part_2.json"
    assert os.path.exists(file_path), f"File {file_path} does not exist!"

    data = load_note(file_path)
    assert data is not None, "Failed to load preamble_part_2.json payload!"
    print(f"\n3. Notes Payload Loaded Successfully ({file_path})")

    # 4. Content Completeness Verification
    print("\n4. Content Completeness Verification:")

    # Check Required Top Level Keys
    assert "meta" in data or "metadata" in data, "Missing metadata object"
    assert "keywords" in data and len(data["keywords"]) > 5, "Missing keywords"
    assert "learning_outcomes" in data, "Missing learning_outcomes"
    assert "sections" in data and len(data["sections"]) >= 10, "Missing or insufficient sections"
    assert "content" in data, "Missing content payload"
    assert "important_facts" in data, "Missing important_facts"
    assert "tnpsc_traps" in data and len(data["tnpsc_traps"]) >= 8, "Missing or insufficient tnpsc_traps"
    assert "tables" in data and len(data["tables"]) >= 2, "Missing comparison or case tables"
    assert "revision_cards" in data and len(data["revision_cards"]) >= 5, "Missing revision cards"

    content_str = json.dumps(data, ensure_ascii=False)

    scope_checks = [
        ("Constitutional Status", "Constitutional Status"),
        ("Berubari Union Case 1960", "Berubari"),
        ("Kesavananda Bharati Case 1973", "Kesavananda"),
        ("LIC of India Case 1995", "LIC"),
        ("S.R. Bommai Case 1994", "Bommai"),
        ("42nd Amendment Act 1976", "42nd"),
        ("Socialist", "Socialist"),
        ("Secular", "Secular"),
        ("Integrity", "Integrity"),
        ("Amendability under Article 368", "Article 368"),
        ("Basic Structure Doctrine", "Basic Structure"),
        ("Non-Justiciable Nature", "Non-Justiciable"),
        ("Interpretive Guide", "Interpretive"),
        ("Fundamental Rights Connection", "Fundamental Rights"),
        ("DPSP Connection", "DPSP"),
        ("Fundamental Duties Connection", "Fundamental Duties"),
        ("Do Not Confuse Section", "Confuse"),
        ("Bilingual Tamil Content", "முகவுரை"),
    ]

    for label, needle in scope_checks:
        assert needle.lower() in content_str.lower(), f"Scope check failed for: {label}"
        print(f"   [OK] Covered: {label}")

    # 5. UI Compatibility Test
    print("\n5. Testing Notes Engine Compatibility:")
    assert "ui_type" in data and data["ui_type"] == "polity", "ui_type should be 'polity'"
    print("   [OK] UI compatibility structure PASSED")

    # 6. Verify Existing Topics Compatibility (Part 1 and other topics)
    print("\n6. Verifying Existing Topics Compatibility:")
    existing_topics = [
        "polity_preamble_part_1",
        "polity_historical_background_part1",
        "polity_making_of_indian_constitution_part_1",
        "polity_salient_features_of_the_indian_constitution_part_1"
    ]
    for top_id in existing_topics:
        top_meta = get_topic_metadata_by_id(subject, top_id)
        assert top_meta is not None, f"Existing topic {top_id} metadata broken"
        top_avail = check_repository_availability(subject, top_id)
        assert top_avail.get("notes") == True, f"Existing topic {top_id} notes unavailable"
        print(f"   [OK] Existing topic '{top_meta['display_title']}' functional.")

    print("\n==================================================")
    print("ALL PREAMBLE PART 2 NOTES VERIFICATION CHECKS PASSED SUCCESSFULLY!")
    print("==================================================")

if __name__ == "__main__":
    test_preamble_part2()
