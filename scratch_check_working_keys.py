import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

notes_dir = 'data/notes/polity'
for fname in sorted(os.listdir(notes_dir)):
    if not fname.endswith('.json'):
        continue
    path = os.path.join(notes_dir, fname)
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    content = data.get("content", data)
    keys = list(content.keys()) if isinstance(content, dict) else []
    comp_keys = [k for k in keys if 'comp' in k or 'table' in k]
    if comp_keys:
        print(f"{fname}: {comp_keys}")
