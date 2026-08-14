import sys
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).parent))

from core.topics_loader import get_topic_metadata_by_id
from core.navigation_v2.navigation_state import check_repository_availability
from core.question_loader import load_questions
from ui.pages.notes import load_note

def test_salient_features_architecture():
    print("==================================================")
    print("RUNNING SALIENT FEATURES GRAND TEST ARCHITECTURE VERIFICATION")
    print("==================================================")

    subject = "polity"
    parts = [
        ("polity_salient_features_of_the_indian_constitution_part_1", 1),
        ("polity_salient_features_of_the_indian_constitution_part_2", 2),
        ("polity_salient_features_of_the_indian_constitution_part_3", 3),
    ]

    expected_repo_id = "polity_salient_features_of_the_indian_constitution"

    for topic_id, part_num in parts:
        print(f"\n--- Testing Topic ID: {topic_id} (Part {part_num}) ---")
        
        # 1. Metadata resolution test
        meta = get_topic_metadata_by_id(subject, topic_id)
        assert meta is not None, f"Metadata not found for {topic_id}"
        print(f"1. Metadata Resolution:")
        print(f"   - topic_id: {meta.get('topic_id')}")
        print(f"   - repository_id: {meta.get('repository_id')}")
        print(f"   - display_title: {meta.get('display_title')}")
        
        assert meta["repository_id"] == expected_repo_id, f"repository_id mismatch! Expected {expected_repo_id}, got {meta['repository_id']}"
        print("   [OK] Metadata test PASSED")

        # 2. Availability Check Test
        avail = check_repository_availability(subject, meta["topic_id"])
        print("2. Repository Availability Check:")
        for k, v in avail.items():
            print(f"   - {k}: {v}")

        assert avail.get("grand_test") == True, f"Grand Test repo should be available for Part {part_num}"
        print(f"   [OK] Grand Test available for Part {part_num} PASSED!")

        # 3. Question Loader Test for Grand Test
        gt_qs = load_questions(expected_repo_id, "grand_test")
        print(f"3. Grand Test Questions Loaded: {len(gt_qs)}")
        assert len(gt_qs) == 100, f"Expected 100 Grand Test questions, loaded {len(gt_qs)}"
        print(f"   [OK] Loaded 100 Grand Test questions for Part {part_num} PASSED!")

        # 4. Notes Loader Test
        note_path = f"data/notes/polity/salient_features_of_the_indian_constitution_part_{part_num}.json"
        note_payload = load_note(note_path)
        assert note_payload is not None, f"Note payload for part {part_num} should load successfully"
        print(f"4. Notes file '{note_path}' loaded successfully. PASSED!")

    print("\n==================================================")
    print("ALL SALIENT FEATURES GRAND TEST VERIFICATION TESTS PASSED SUCCESSFULLY!")
    print("==================================================")

if __name__ == "__main__":
    test_salient_features_architecture()
