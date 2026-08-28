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

suspicious = []

for name, path, expected_count, diff_type in datasets:
    if not os.path.exists(path):
        continue
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
        
    for i, q in enumerate(data):
        q_id = q.get('id') or q.get('question_id')
        q_en = q.get('question_en') or (q.get('question', {}).get('en') if isinstance(q.get('question'), dict) else '')
        exp_en = q.get('explanation_en') or (q.get('explanation', {}).get('en') if isinstance(q.get('explanation'), dict) else '')
        opts = q.get('options', [])
        ans_letter = q.get('correct_answer')
        
        correct_opt_text = ""
        for o in opts:
            if o.get('id') == ans_letter:
                correct_opt_text = o.get('en', '')
                
        full_text = f"{q_en} | Option {ans_letter}: {correct_opt_text} | Exp: {exp_en}"
        
        # 1. Qualified veto check: Does any question say President of India has qualified veto?
        if "qualified veto" in full_text.lower():
            if "possesses qualified veto" in full_text.lower() or "exercised qualified veto" in full_text.lower() or ("qualified veto" in correct_opt_text.lower() and not "not" in q_en.lower() and not "does not" in q_en.lower()):
                suspicious.append((name, q_id, "Qualified Veto check: Indian President does NOT have qualified veto! Check context.", full_text))
                
        # 2. Veto on Constitutional Amendment Bill check
        if "constitutional amendment bill" in full_text.lower() and "veto" in full_text.lower():
            if "can reject" in correct_opt_text.lower() or "can withhold" in correct_opt_text.lower() or "suspensive veto" in correct_opt_text.lower():
                suspicious.append((name, q_id, "CAA Veto check: Assent is mandatory under 24th CAA 1971; President cannot veto CAA Bill!", full_text))
                
        # 3. Suspensive Veto on Money Bill check
        if "money bill" in full_text.lower() and "suspensive veto" in full_text.lower():
            if "can return" in correct_opt_text.lower() or "suspensive veto applies" in correct_opt_text.lower():
                suspicious.append((name, q_id, "Money Bill Veto check: Suspensive veto does NOT apply to Money Bills!", full_text))
                
        # 4. Impeachment voters check: Nominated vs Elected, MLAs vs MPs
        if "impeachment" in full_text.lower() and "nominated" in full_text.lower():
            if "nominated members do not participate" in correct_opt_text.lower() or "nominated members cannot vote" in correct_opt_text.lower():
                suspicious.append((name, q_id, "Impeachment check: Nominated members of Parliament CAN participate in impeachment!", full_text))
                
        if "impeachment" in full_text.lower() and "legislative assembly" in full_text.lower():
            if "mlas participate" in correct_opt_text.lower() or "mlas vote in impeachment" in correct_opt_text.lower():
                suspicious.append((name, q_id, "Impeachment check: MLAs of States DO NOT participate in impeachment!", full_text))
                
        # 5. Electoral College check: Nominated members or Legislative Councils
        if "electoral college" in full_text.lower() and ("nominated" in correct_opt_text.lower() or "legislative council" in correct_opt_text.lower()):
            if not "not" in q_en.lower() and not "except" in q_en.lower() and not "does not" in q_en.lower() and not "excluded" in full_text.lower():
                suspicious.append((name, q_id, "Electoral College check: Nominated members & MLCs are EXCLUDED from Presidential Electoral College!", full_text))

        # 6. Fundamental Rights suspension check
        if "all fundamental rights" in full_text.lower() and "suspended" in full_text.lower():
            if "all fundamental rights are automatically suspended" in correct_opt_text.lower():
                suspicious.append((name, q_id, "FR Suspension check: Articles 20 & 21 can NEVER be suspended!", full_text))

        # 7. Governor pardoning death sentence check
        if "governor" in full_text.lower() and "pardon" in full_text.lower() and "death sentence" in full_text.lower():
            if "governor can pardon death sentence" in correct_opt_text.lower():
                suspicious.append((name, q_id, "Governor Pardon check: Governor CANNOT pardon death sentence (only President can)! Governor can only suspend/remit/commute.", full_text))

print(f"Total Suspicious Constitutional Flags: {len(suspicious)}")
for file_name, qid, reason, text in suspicious:
    print(f"\n- [{file_name}] {qid}: {reason}")
    print(f"  Snippet: {text[:200]}...")

