import json
import os
import sys

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

print("==================================================")
print("AUDITING EXPLANATION QUALITY ACROSS ALL 8 DATASETS")
print("==================================================")

for name, path in datasets:
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
        
    generic_wno_count = 0
    generic_tip_count = 0
    short_exp_count = 0
    
    for i, q in enumerate(data):
        qid = q.get('id') or q.get('question_id')
        
        # Check distractor analysis
        wno = q.get('why_not_others', {})
        if isinstance(wno, dict):
            for k in ['A', 'B', 'C', 'D']:
                val = wno.get(k, {})
                en_txt = val.get('en', '') if isinstance(val, dict) else str(val)
                if 'is incorrect' in en_txt.lower() and len(en_txt.split()) <= 4:
                    generic_wno_count += 1
                    break
        else:
            generic_wno_count += 1
            
        # Check TNPSC tip
        tip = q.get('tnpsc_tip') or q.get('trap_point')
        if isinstance(tip, dict):
            en_tip = tip.get('en', '')
            if 'remember article reference' in en_tip.lower() or 'read carefully' in en_tip.lower() or len(en_tip.split()) <= 6:
                generic_tip_count += 1
        elif isinstance(tip, str):
            if 'remember' in tip.lower() and len(tip.split()) <= 6:
                generic_tip_count += 1
        else:
            generic_tip_count += 1

        # Check core explanation
        exp_en = q.get('explanation_en') or (q.get('explanation', {}).get('en') if isinstance(q.get('explanation'), dict) else '')
        if len(exp_en.split()) < 10:
            short_exp_count += 1

    print(f"[{name}] Total Qs: {len(data)}")
    print(f"  - Generic Distractor Analysis: {generic_wno_count} / {len(data)}")
    print(f"  - Generic TNPSC Tips: {generic_tip_count} / {len(data)}")
    print(f"  - Short/Weak Core Explanations: {short_exp_count} / {len(data)}")
