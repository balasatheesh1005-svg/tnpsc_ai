import json
import os
import sys
import re

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

errors = []

for name, path in datasets:
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
        
    for idx, q in enumerate(data):
        qid = q.get('id') or f"{name}_Q{idx}"
        q_en = q.get('question_en') or (q.get('question', {}).get('en') if isinstance(q.get('question'), dict) else '')
        exp_en = q.get('explanation_en') or (q.get('explanation', {}).get('en') if isinstance(q.get('explanation'), dict) else '')
        ans = q.get('correct_answer')
        opts = q.get('options', [])
        
        opt_map = {o.get('id'): o.get('en', '') for o in opts if isinstance(o, dict)}
        ans_text = opt_map.get(ans, '')
        
        # 1. Article matching checks
        # Check Article 52
        if "article 52" in q_en.lower() and "president of india" in q_en.lower():
            if "vice-president" in ans_text.lower() or "prime minister" in ans_text.lower():
                errors.append(f"[{name}] {qid}: Article 52 mismatch in answer: {ans_text}")
                
        # Check Article 54 Electoral College
        if "article 54" in q_en.lower() or "electoral college" in q_en.lower():
            # If question asks who is included in electoral college:
            if "includes" in q_en.lower() or "member" in q_en.lower():
                if "nominated" in ans_text.lower() and not "not" in ans_text.lower() and not "excluded" in ans_text.lower() and not "except" in q_en.lower():
                    errors.append(f"[{name}] {qid}: Nominated members wrongly included in Electoral College answer!")
                    
        # Check Article 58 age qualification
        if "article 58" in q_en.lower() or "minimum age" in q_en.lower():
            if "35 years" not in ans_text and "35 years" not in exp_en and "30 years" in ans_text:
                errors.append(f"[{name}] {qid}: Age qualification mismatch in answer or explanation!")

        # Check Article 61 Impeachment majority
        if "article 61" in q_en.lower() and "majority" in q_en.lower():
            if "simple majority" in ans_text.lower() and not "not" in q_en.lower():
                errors.append(f"[{name}] {qid}: Impeachment requires 2/3rd total membership, not simple majority!")

        # Check Article 123 Ordinance maximum duration
        if "article 123" in q_en.lower() and "maximum duration" in q_en.lower():
            if "6 months" in ans_text and "6 weeks" not in ans_text and "6 months and 6 weeks" not in exp_en and "42 days" not in exp_en:
                errors.append(f"[{name}] {qid}: Ordinance max duration must specify 6 months and 6 weeks / 42 days!")

        # Check Article 352 National Emergency approval duration
        if "article 352" in q_en.lower() and "approval" in q_en.lower() and "within" in q_en.lower():
            if "2 months" in ans_text and "1 month" not in ans_text:
                errors.append(f"[{name}] {qid}: National Emergency approval period is 1 month (after 44th CAA), not 2 months!")

        # Check Article 356 President's Rule approval duration
        if "article 356" in q_en.lower() and "approval" in q_en.lower() and "within" in q_en.lower():
            if "1 month" in ans_text and "2 months" not in ans_text:
                errors.append(f"[{name}] {qid}: President's Rule approval period is 2 months, not 1 month!")

        # Check Article 360 Financial Emergency maximum duration
        if "article 360" in q_en.lower() and "maximum duration" in q_en.lower():
            if "3 years" in ans_text or "1 year" in ans_text:
                errors.append(f"[{name}] {qid}: Financial emergency has NO maximum duration specified in Constitution!")

print(f"Total Deep Fact Check Errors Found: {len(errors)}")
for err in errors:
    print(" -", err)
