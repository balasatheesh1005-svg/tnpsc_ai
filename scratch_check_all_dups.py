import json
import os
import sys
from difflib import SequenceMatcher

sys.stdout.reconfigure(encoding='utf-8')

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

print("=== CHECKING INTRA-FILE DUPLICATES & NEAR-DUPLICATES ===")
for name, path in datasets:
    with open(path, encoding='utf-8') as f:
        qs = json.load(f)
        
    for i in range(len(qs)):
        for j in range(i + 1, len(qs)):
            q1_en = (qs[i].get('question_en') or (qs[i].get('question', {}).get('en') if isinstance(qs[i].get('question'), dict) else '')).strip().lower()
            q2_en = (qs[j].get('question_en') or (qs[j].get('question', {}).get('en') if isinstance(qs[j].get('question'), dict) else '')).strip().lower()
            
            ratio = SequenceMatcher(None, q1_en, q2_en).ratio()
            if ratio > 0.85:
                print(f"[{name}] High similarity ({ratio:.2f}):")
                print(f"  Q{i+1} ({qs[i].get('id')}): {q1_en[:80]}")
                print(f"  Q{j+1} ({qs[j].get('id')}): {q2_en[:80]}")
