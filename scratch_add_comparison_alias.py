import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

for p in ['president_part_1.json', 'president_part_2.json', 'president_part_3.json']:
    path = f'data/notes/polity/{p}'
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    content = data.get("content", {})
    if isinstance(content, dict):
        if "comparison_tables" in content and "comparison" not in content:
            content["comparison"] = content["comparison_tables"]
            print(f"Added 'comparison' key to {p} (count: {len(content['comparison'])})")
            
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

print("President notes comparison alias sync complete.")
