import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

from core.question_loader import load_questions
from core.topics_loader import get_topic_metadata_by_id

def test_part_loading():
    print("==========================================================")
    print("Testing DPSP Repository Loading across Part 1, Part 2, Part 3")
    print("==========================================================")
    
    parts = ["polity_directive_principles_part_1", "polity_directive_principles_part_2", "polity_directive_principles_part_3"]
    
    loaded_counts = []
    first_q_ids = []
    
    for part in parts:
        meta = get_topic_metadata_by_id("polity", part)
        repo_id = meta["repository_id"]
        print(f"\nTopic ID: {part} -> Repository ID: {repo_id}")
        
        # Load Chronology type questions
        qs = load_questions(repo_id, "chronology")
        print(f"Loaded {len(qs)} Chronology questions for {part}")
        
        assert len(qs) == 25, f"Expected 25 questions for {part}, got {len(qs)}"
        loaded_counts.append(len(qs))
        first_q_ids.append(qs[0]["id"])
        
    print("\n--- SUMMARY ---")
    print("Part 1 Loaded Count:", loaded_counts[0], "| First Q:", first_q_ids[0])
    print("Part 2 Loaded Count:", loaded_counts[1], "| First Q:", first_q_ids[1])
    print("Part 3 Loaded Count:", loaded_counts[2], "| First Q:", first_q_ids[2])
    
    assert loaded_counts[0] == loaded_counts[1] == loaded_counts[2] == 25
    assert first_q_ids[0] == first_q_ids[1] == first_q_ids[2] == "DPSP_CHRONO_001"
    
    print("\nSUCCESS! All three Notes Parts load the SAME 25-question repository!")

if __name__ == "__main__":
    test_part_loading()
