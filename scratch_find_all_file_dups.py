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

for name, path in datasets:
    with open(path, encoding='utf-8') as f:
        qs = json.load(f)
    print(f"\n--- Checking duplicates in {name} ---")
    dups_in_file = 0
    for i in range(len(qs)):
        for j in range(i + 1, len(qs)):
            q1 = (qs[i].get('question_en') or '').strip().lower()
            q2 = (qs[j].get('question_en') or '').strip().lower()
            r = SequenceMatcher(None, q1, q2).ratio()
            if r > 0.75:
                id1 = qs[i].get('id')
                id2 = qs[j].get('id')
                print(f"  [{name}] Q{i+1} ({id1}) vs Q{j+1} ({id2}) - ratio {r:.2f}")
                print(f"    1: {q1[:75]}")
                print(f"    2: {q2[:75]}")
                dups_in_file += 1
    if dups_in_file == 0:
        print(f"  No duplicates in {name}")
