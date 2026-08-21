import os
import json

def test_fd_chronology_ui_flow():
    # Verify that the common repository exists
    repo_file = "data/questions/polity/fundamental_duties_chronology.json"
    assert os.path.exists(repo_file), f"Repository missing: {repo_file}"
    
    with open(repo_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    assert len(data) == 25, f"Expected 25 questions, got {len(data)}"
    
    # Verify mapping in polity_structure.json
    struct_file = "data/structure/polity_structure.json"
    with open(struct_file, "r", encoding="utf-8") as f:
        struct = json.load(f)
        
    part_topics = [
        "polity_fundamental_duties_part_1",
        "polity_fundamental_duties_part_2",
        "polity_fundamental_duties_part_3"
    ]
    
    for topic_id in part_topics:
        matched = [t for t in struct["topics"] if t["topic_id"] == topic_id]
        assert len(matched) == 1, f"Topic {topic_id} not found in polity_structure.json"
        repo_id = matched[0]["repository_id"]
        assert repo_id == "polity_fundamental_duties", f"Mismatch repository_id for {topic_id}: {repo_id}"
        
        # When mode is 'chronology', repository_id 'polity_fundamental_duties' resolves to 'fundamental_duties_chronology.json'
        inferred_filename = f"{repo_id.replace('polity_', '')}_chronology.json"
        target_path = os.path.join("data", "questions", "polity", inferred_filename)
        assert os.path.exists(target_path), f"Inferred chronology file for {topic_id} does not exist: {target_path}"
        assert os.path.samefile(target_path, repo_file), f"File mismatch for {topic_id}"
        
    print("UI Practice Mapping Flow Check Passed Successfully!")
    print("Part 1, Part 2, Part 3 Practice -> Chronology ALL map to the SAME 25-question repository!")

if __name__ == "__main__":
    test_fd_chronology_ui_flow()
