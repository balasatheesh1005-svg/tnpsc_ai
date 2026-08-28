import json
import os
import sys
import shutil

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

from scratch_enrich_helper import enrich_question

datasets = [
    ('easy.json', 'data/questions/polity/president_easy.json'),
    ('medium.json', 'data/questions/polity/president_medium.json'),
    ('hard.json', 'data/questions/polity/president_hard.json'),
    ('statement.json', 'data/questions/polity/president_statement.json'),
    ('reasoning.json', 'data/questions/polity/president_reasoning.json'),
    ('chronology.json', 'data/questions/polity/president_chronology.json'),
    ('match.json', 'data/questions/polity/president_match.json'),
    ('grand_test.json', 'data/questions/polity/president_grand_test.json')
]

print("==================================================")
print("ENRICHING EXPLANATIONS & DISTRACTORS FOR 375 MCQs")
print("==================================================")

total_processed = 0

for name, path in datasets:
    if not os.path.exists(path):
        print(f"❌ File missing: {path}")
        continue
        
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    count = len(data)
    print(f"Processing {name} ({count} questions)...")
    
    enriched_data = []
    for q in data:
        eq = enrich_question(q)
        enriched_data.append(eq)
        total_processed += 1
        
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(enriched_data, f, ensure_ascii=False, indent=2)
        
    print(f"  ✅ {name}: Enriched {len(enriched_data)} questions.")

# Sync secondary alias files
alias_pairs = [
    ("data/questions/polity/president_statement.json", "data/questions/polity/president_statement_based.json"),
    ("data/questions/polity/president_reasoning.json", "data/questions/polity/president_assertion_reason.json"),
    ("data/questions/polity/president_match.json", "data/questions/polity/president_match_the_following.json")
]

print("\nSyncing secondary alias files...")
for src, dst in alias_pairs:
    if os.path.exists(src):
        shutil.copyfile(src, dst)
        print(f"  ✅ Synced {src} -> {dst}")

print(f"\n==================================================")
print(f"SUCCESS: ENRICHED ALL {total_processed} QUESTIONS ACROSS ALL 8 DATASETS!")
print("==================================================")
