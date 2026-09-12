# scratch_validate_governor_part2.py
import json, os, sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

print("Starting validation of Governor Part 2 MCQ Bank (175 Items)...")

files = {
    "Statement Based": "data/questions/polity/governor_statement_based.json",
    "Reasoning": "data/questions/polity/governor_reasoning.json",
    "Match the Following": "data/questions/polity/governor_match_the_following.json",
    "Chronology": "data/questions/polity/governor_chronology.json",
    "PYQ": "data/questions/polity/governor_pyq.json"
}

expected_counts = {
    "Statement Based": 50,
    "Reasoning": 25,
    "Match the Following": 25,
    "Chronology": 25,
    "PYQ": 50
}

total_questions = 0
all_ids = set()
all_stems_en = set()
all_stems_ta = set()
duplicate_stems_en = 0
duplicate_stems_ta = 0

report = {}

for model, path in files.items():
    if not os.path.exists(path):
        print(f"ERROR: File {path} missing!")
        sys.exit(1)
        
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    count = len(data)
    total_questions += count
    
    ans_dist = {"A": 0, "B": 0, "C": 0, "D": 0}
    
    for item in data:
        item_id = item.get("id")
        if item_id in all_ids:
            print(f"ERROR: Duplicate ID found: {item_id}")
        all_ids.add(item_id)
        
        ans = item.get("correct_answer")
        if ans in ans_dist:
            ans_dist[ans] += 1
        else:
            print(f"ERROR: Invalid correct_answer {ans} in {item_id}")
            
        q_en = item.get("question", {}).get("en", "").strip()
        q_ta = item.get("question", {}).get("ta", "").strip()
        
        if q_en in all_stems_en:
            duplicate_stems_en += 1
        all_stems_en.add(q_en)
        
        if q_ta in all_stems_ta:
            duplicate_stems_ta += 1
        all_stems_ta.add(q_ta)
        
        # Schema checks
        assert "options" in item and len(item["options"]) == 4, f"Options missing in {item_id}"
        assert "options_en" in item and len(item["options_en"]) == 4, f"options_en missing in {item_id}"
        assert "options_ta" in item and len(item["options_ta"]) == 4, f"options_ta missing in {item_id}"
        assert "why_not_others" in item and len(item["why_not_others"]) == 4, f"why_not_others missing in {item_id}"
        assert "tnpsc_tip" in item and "en" in item["tnpsc_tip"] and "ta" in item["tnpsc_tip"], f"tnpsc_tip missing in {item_id}"
        assert "revision_fact" in item and "en" in item["revision_fact"] and "ta" in item["revision_fact"], f"revision_fact missing in {item_id}"
        
    report[model] = {
        "file": path,
        "count": count,
        "expected": expected_counts[model],
        "answer_distribution": ans_dist
    }

print("\n================ VALIDATION REPORT ================")
print(f"Total Files Checked: {len(files)}")
print(f"Total MCQs Generated: {total_questions} (Target: 175)")
print(f"Unique Question IDs: {len(all_ids)}")
print(f"Duplicate English Stems: {duplicate_stems_en}")
print(f"Duplicate Tamil Stems: {duplicate_stems_ta}")

for model, info in report.items():
    print(f"\n{model} ({info['file']}):")
    print(f"  Count: {info['count']} / {info['expected']}")
    print(f"  Answer Distribution: {info['answer_distribution']}")

if total_questions == 175 and duplicate_stems_en == 0 and duplicate_stems_ta == 0:
    print("\nSUCCESS: All 175 Governor Part 2 MCQs validated successfully!")
else:
    print("\nWARNING: Validation checks encountered discrepancies.")
