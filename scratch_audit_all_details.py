import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

def audit_match():
    path = 'data/questions/polity/president_match.json'
    with open(path, encoding='utf-8') as f:
        qs = json.load(f)
    print(f"=== MATCH.JSON AUDIT ({len(qs)} questions) ===")
    issues = []
    for i, q in enumerate(qs):
        qid = q.get('id')
        q_en = q.get('question_en') or ''
        opts = q.get('options', [])
        ans = q.get('correct_answer')
        
        # Check if List I and List II are present in question text
        if "list i" not in q_en.lower() and "list 1" not in q_en.lower() and "match" not in q_en.lower():
            issues.append(f"{qid}: Question text missing List I / List II header/structure")
            
        opt_codes = [o.get('en', '').strip() for o in opts]
        if len(set(opt_codes)) < 4:
            issues.append(f"{qid}: Duplicate option codes: {opt_codes}")
            
    print(f"Match issues found: {len(issues)}")
    for iss in issues:
        print(" -", iss)

def audit_chronology():
    path = 'data/questions/polity/president_chronology.json'
    with open(path, encoding='utf-8') as f:
        qs = json.load(f)
    print(f"\n=== CHRONOLOGY.JSON AUDIT ({len(qs)} questions) ===")
    issues = []
    for i, q in enumerate(qs):
        qid = q.get('id')
        opts = q.get('options', [])
        opt_codes = [o.get('en', '').strip() for o in opts]
        if len(set(opt_codes)) < 4:
            issues.append(f"{qid}: Duplicate option codes in Chronology: {opt_codes}")
            
    print(f"Chronology issues found: {len(issues)}")
    for iss in issues:
        print(" -", iss)

def audit_statement():
    path = 'data/questions/polity/president_statement.json'
    with open(path, encoding='utf-8') as f:
        qs = json.load(f)
    print(f"\n=== STATEMENT.JSON AUDIT ({len(qs)} questions) ===")
    issues = []
    for i, q in enumerate(qs):
        qid = q.get('id')
        q_en = q.get('question_en') or ''
        exp_en = q.get('explanation_en') or ''
        
        # Check if question text has numbered statements 1., 2. or 1), 2)
        if not ("1." in q_en or "1)" in q_en or "Statement 1" in q_en or "1:" in q_en):
            issues.append(f"{qid}: Question text missing statement 1 marker")
            
    print(f"Statement issues found: {len(issues)}")
    for iss in issues:
        print(" -", iss)

def audit_reasoning():
    path = 'data/questions/polity/president_reasoning.json'
    with open(path, encoding='utf-8') as f:
        qs = json.load(f)
    print(f"\n=== REASONING.JSON AUDIT ({len(qs)} questions) ===")
    issues = []
    for i, q in enumerate(qs):
        qid = q.get('id')
        q_en = q.get('question_en') or ''
        
        if "assertion" not in q_en.lower() and "reason" not in q_en.lower() and "(a)" not in q_en.lower():
            issues.append(f"{qid}: Missing Assertion (A) / Reason (R) format in question text")
            
    print(f"Reasoning issues found: {len(issues)}")
    for iss in issues:
        print(" -", iss)

audit_match()
audit_chronology()
audit_statement()
audit_reasoning()
