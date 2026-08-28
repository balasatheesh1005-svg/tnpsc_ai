import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

files = [
    'fundamental_rights_part_1.json',
    'directive_principles_part_1.json',
    'preamble_part_1.json',
    'president_part_1.json',
    'president_part_2.json',
    'president_part_3.json'
]

for p in files:
    path = f'data/notes/polity/{p}'
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    print(f"\n==========================================")
    print(f"FILE: {p}")
    print(f"==========================================")
    print("Top-level keys:", list(data.keys()))
    content = data.get("content", data)
    if isinstance(content, dict):
        print("Content keys:", list(content.keys()))
        for k in content.keys():
            if 'comp' in k or 'table' in k:
                val = content[k]
                print(f"  Content Key '{k}': type={type(val).__name__}")
                if isinstance(val, list):
                    print(f"  Count: {len(val)}")
                    for idx, item in enumerate(val):
                        if isinstance(item, dict):
                            print(f"    Item {idx} keys: {list(item.keys())}")
                            print(f"    Item {idx} sample: {json.dumps(item, ensure_ascii=False)[:250]}")
    # Also check inside sections if present
    sections = data.get("sections", [])
    if sections:
        print(f"Sections count: {len(sections)}")
        for s_idx, sec in enumerate(sections):
            if isinstance(sec, dict):
                for sk in sec.keys():
                    if 'comp' in sk or 'table' in sk:
                        val = sec[sk]
                        print(f"  Section {s_idx} Key '{sk}': type={type(val).__name__}")
                        if isinstance(val, list):
                            for idx, item in enumerate(val):
                                if isinstance(item, dict):
                                    print(f"    Item {idx} keys: {list(item.keys())}")
                                    print(f"    Item {idx} sample: {json.dumps(item, ensure_ascii=False)[:250]}")
