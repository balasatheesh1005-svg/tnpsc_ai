import json
import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

datasets = [
    ('easy.json', 'data/questions/polity/president_easy.json', 50, 'easy'),
    ('medium.json', 'data/questions/polity/president_medium.json', 50, 'medium'),
    ('hard.json', 'data/questions/polity/president_hard.json', 50, 'hard'),
    ('statement.json', 'data/questions/polity/president_statement.json', 50, 'statement'),
    ('reasoning.json', 'data/questions/polity/president_reasoning.json', 25, 'reasoning'),
    ('chronology.json', 'data/questions/polity/president_chronology.json', 25, 'chronology'),
    ('match.json', 'data/questions/polity/president_match.json', 25, 'match'),
    ('grand_test.json', 'data/questions/polity/president_grand_test.json', 100, 'grand_test')
]

print("==================================================")
print("DEEP AUDIT OF ALL 375 PRESIDENT MCQs")
print("==================================================")

mismatches = []
match_issues = []
chrono_issues = []
statement_issues = []
bilingual_issues = []

for name, path, expected_count, diff_type in datasets:
    if not os.path.exists(path):
        continue
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
        
    for i, q in enumerate(data):
        q_id = q.get('id') or q.get('question_id')
        opts = q.get('options', [])
        ans_letter = q.get('correct_answer')
        
        # Get correct option text
        correct_opt = None
        for o in opts:
            if o.get('id') == ans_letter:
                correct_opt = o
                break
                
        q_en = q.get('question_en') or (q.get('question', {}).get('en') if isinstance(q.get('question'), dict) else '')
        q_ta = q.get('question_ta') or (q.get('question', {}).get('ta') if isinstance(q.get('question'), dict) else '')
        exp_en = q.get('explanation_en') or (q.get('explanation', {}).get('en') if isinstance(q.get('explanation'), dict) else '')
        exp_ta = q.get('explanation_ta') or (q.get('explanation', {}).get('ta') if isinstance(q.get('explanation'), dict) else '')

        # Check answer letter vs explanation agreement
        if exp_en:
            # Check if explanation mentions "Option A", "Option B", "Option C", "Option D" or "Correct Option: X" or "(a)", "(b)", etc.
            # Look for explicit option mentions in explanation
            opt_mentions = re.findall(r'(?:correct\s+answer|correct\s+option|option)\s*:?\s*([A-D])\b', exp_en, re.IGNORECASE)
            if opt_mentions:
                mentioned_letter = opt_mentions[0].upper()
                if mentioned_letter != ans_letter:
                    mismatches.append(f"[{name}] {q_id}: correct_answer is {ans_letter}, but explanation mentions Option {mentioned_letter}")
                    
        # Match type checks
        if diff_type == 'match' or q.get('question_type') == 'Match':
            # Check options uniqueness
            opt_texts = [o.get('en', '').strip() for o in opts]
            if len(set(opt_texts)) < 4:
                match_issues.append(f"[{name}] {q_id}: Non-unique options in Match question: {opt_texts}")
                
        # Chronology type checks
        if diff_type == 'chronology' or q.get('question_type') == 'Chronology':
            opt_texts = [o.get('en', '').strip() for o in opts]
            if len(set(opt_texts)) < 4:
                chrono_issues.append(f"[{name}] {q_id}: Non-unique options in Chronology question: {opt_texts}")
                
        # Tamil check
        if not q_ta or len(q_ta.strip()) < 5:
            bilingual_issues.append(f"[{name}] {q_id}: Empty or very short Tamil question")
        if not exp_ta or len(exp_ta.strip()) < 5:
            bilingual_issues.append(f"[{name}] {q_id}: Empty or very short Tamil explanation")
            
        for o in opts:
            if not o.get('ta') or len(o.get('ta').strip()) < 1:
                bilingual_issues.append(f"[{name}] {q_id}: Option {o.get('id')} missing Tamil text")

print(f"\n1. Answer vs Explanation Mismatches: {len(mismatches)}")
for m in mismatches:
    print("  -", m)

print(f"\n2. Match Question Issues: {len(match_issues)}")
for m in match_issues:
    print("  -", m)

print(f"\n3. Chronology Question Issues: {len(chrono_issues)}")
for c in chrono_issues:
    print("  -", c)

print(f"\n4. Bilingual Issues: {len(bilingual_issues)}")
for b in bilingual_issues:
    print("  -", b)
