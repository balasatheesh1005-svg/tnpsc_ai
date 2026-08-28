import json
import os
import sys

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

issues = []
all_q_texts = {}

for name, path, expected_count, diff_type in datasets:
    if not os.path.exists(path):
        issues.append(f'[{name}] File missing: {path}')
        continue
    try:
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        issues.append(f'[{name}] JSON parse error: {e}')
        continue
    
    if len(data) != expected_count:
        issues.append(f'[{name}] Count mismatch: expected {expected_count}, got {len(data)}')
        
    for i, q in enumerate(data):
        q_id = q.get('id') or q.get('question_id')
        
        # Check required fields
        for field in ['id', 'subject', 'topic', 'difficulty', 'question_type', 'options', 'correct_answer']:
            if not q.get(field):
                issues.append(f'[{name}] Q{i} ({q_id}): missing required field "{field}"')
                
        # Check bilingual question
        q_en = q.get('question_en') or (q.get('question', {}).get('en') if isinstance(q.get('question'), dict) else '')
        q_ta = q.get('question_ta') or (q.get('question', {}).get('ta') if isinstance(q.get('question'), dict) else '')
        if not q_en or not q_ta:
            issues.append(f'[{name}] Q{i} ({q_id}): missing bilingual question (en={bool(q_en)}, ta={bool(q_ta)})')
            
        # Store for duplication check
        norm_q_en = q_en.strip().lower()
        if norm_q_en in all_q_texts:
            all_q_texts[norm_q_en].append((name, q_id))
        else:
            all_q_texts[norm_q_en] = [(name, q_id)]

        # Check bilingual explanation
        exp_en = q.get('explanation_en') or (q.get('explanation', {}).get('en') if isinstance(q.get('explanation'), dict) else '')
        exp_ta = q.get('explanation_ta') or (q.get('explanation', {}).get('ta') if isinstance(q.get('explanation'), dict) else '')
        if not exp_en or not exp_ta:
            issues.append(f'[{name}] Q{i} ({q_id}): missing bilingual explanation (en={bool(exp_en)}, ta={bool(exp_ta)})')
            
        # Check trap point
        trap = q.get('trap_point') or q.get('tnpsc_tip')
        if not trap:
            issues.append(f'[{name}] Q{i} ({q_id}): missing trap_point/tnpsc_tip')
            
        # Check options
        opts = q.get('options', [])
        if not isinstance(opts, list) or len(opts) != 4:
            issues.append(f'[{name}] Q{i} ({q_id}): invalid options length {len(opts) if isinstance(opts, list) else None}')
        else:
            opt_ids = [o.get('id') for o in opts if isinstance(o, dict)]
            if opt_ids != ['A', 'B', 'C', 'D']:
                issues.append(f'[{name}] Q{i} ({q_id}): option ids are {opt_ids}')
            for o in opts:
                if not isinstance(o, dict) or not o.get('en') or not o.get('ta'):
                    issues.append(f'[{name}] Q{i} ({q_id}): option missing text in {o}')
            # Check duplicate options in same question
            opt_ens = [o.get('en', '').strip().lower() for o in opts if isinstance(o, dict)]
            if len(set(opt_ens)) < 4:
                issues.append(f'[{name}] Q{i} ({q_id}): duplicate option texts: {opt_ens}')
                
        # Check correct answer valid letter
        ans = q.get('correct_answer')
        if ans not in ['A', 'B', 'C', 'D']:
            issues.append(f'[{name}] Q{i} ({q_id}): invalid correct_answer "{ans}"')

print(f'Total structural/field issues found: {len(issues)}')
for iss in issues:
    print(' -', iss)

print('\nChecking exact question text duplicates across datasets...')
dup_count = 0
for text, occurrences in all_q_texts.items():
    if len(occurrences) > 1:
        dup_count += 1
        print(f'Duplicate Question ({len(occurrences)} times):')
        print(f'  Text snippet: {text[:80]}...')
        for file_name, qid in occurrences:
            print(f'    -> {file_name}: {qid}')

print(f'\nTotal Exact Duplicate Questions Found: {dup_count}')
