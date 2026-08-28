import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/notes/polity/president_part_1.json', encoding='utf-8') as f:
    data = json.load(f)

print("=== PRESIDENT PART 1 KEYS ===")
print("Top keys:", list(data.keys()))
print("Meta:", data.get("meta"))
content = data.get("content", {})
print("Content keys:", list(content.keys()))
for k, v in content.items():
    if isinstance(v, dict):
        print(f"  Content['{k}']: dict with keys {list(v.keys())}")
    elif isinstance(v, list):
        print(f"  Content['{k}']: list of {len(v)} items (item 0 type: {type(v[0]).__name__ if v else None})")
    else:
        print(f"  Content['{k}']: {type(v).__name__}")
