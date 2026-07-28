import sys
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).parent))

from core.topics_loader import get_topic_metadata_by_id
from core.navigation_v2.navigation_state import check_repository_availability
from core.question_loader import load_questions
from ui.pages.notes import load_note

def test_architecture():
    print("==================================================")
    print("RUNNING ARCHITECTURE VERIFICATION TEST")
    print("==================================================")

    subject = "polity"
    topic_query = "Historical Background Part 1"

    # 1. Metadata resolution test
    meta = get_topic_metadata_by_id(subject, topic_query)
    print(f"\n1. Metadata Resolution for '{topic_query}':")
    print(f"   - topic_id: {meta.get('topic_id')}")
    print(f"   - repository_id: {meta.get('repository_id')}")
    print(f"   - display_title: {meta.get('display_title')}")
    print(f"   - part: {meta.get('part')} / {meta.get('total_parts')}")

    assert meta["topic_id"] == "polity_historical_background_part1", "topic_id mismatch!"
    assert meta["repository_id"] == "polity_historical_background", "repository_id mismatch!"
    assert meta["display_title"] == "Historical Background Part 1", "display_title mismatch!"
    print("   [OK] Metadata test PASSED")

    # 2. Availability Check Test
    avail = check_repository_availability(subject, meta["topic_id"])
    print("\n2. Repository Availability Check:")
    for k, v in avail.items():
        print(f"   - {k}: {v}")

    assert avail.get("notes") == True, "Notes should be available for Part 1"
    assert avail.get("easy") == True, "Easy repo should be available for Historical Background"
    assert avail.get("medium") == True, "Medium repo should be available for Historical Background"
    assert avail.get("hard") == True, "Hard repo should be available for Historical Background"
    assert avail.get("grand_test") == True, "Grand Test repo should be available for Historical Background"
    print("   [OK] Repository availability test PASSED (No 'Repository Not Available' bug!)")

    # 3. Question Loader Test (New signature)
    easy_qs = load_questions("polity_historical_background", "easy")
    gt_qs = load_questions("polity_historical_background", "grand_test")
    print("\n3. Question Loader Test:")
    print(f"   - Easy questions loaded: {len(easy_qs)}")
    print(f"   - Grand test questions loaded: {len(gt_qs)}")

    assert len(easy_qs) > 0, "Easy questions should load successfully"
    assert len(gt_qs) > 0, "Grand test questions should load successfully"
    print("   [OK] Question loader test PASSED")

    # 4. Notes Loader Test
    note_path = f"data/notes/polity/historical_background_part_1.json"
    note_payload = load_note(note_path)
    print("\n4. Notes Payload Loader Test:")
    print(f"   - Note file '{note_path}' loaded: {note_payload is not None}")
    assert note_payload is not None, "Note payload should load successfully"
    print("   [OK] Notes payload loader test PASSED")

    print("\n==================================================")
    print("ALL ARCHITECTURE VERIFICATION TESTS PASSED SUCCESSFULLY!")
    print("==================================================")

if __name__ == "__main__":
    test_architecture()
