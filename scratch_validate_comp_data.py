import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

for p in ['president_part_1.json', 'president_part_2.json', 'president_part_3.json']:
    path = f'data/notes/polity/{p}'
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    print(f"\n==========================================")
    print(f"CHECKING COMPARISON TABLES IN {p}")
    print(f"==========================================")
    content = data.get("content", data)
    tables = content.get("comparison_tables") or content.get("comparison") or content.get("tables") or []
    print(f"Total tables: {len(tables)}")
    for idx, t in enumerate(tables):
        if not isinstance(t, dict):
            print(f"  Table {idx}: INVALID (not a dict)")
            continue
        title_en = t.get("title_en") or t.get("title")
        title_ta = t.get("title_ta")
        h_en = t.get("headers_en", [])
        h_ta = t.get("headers_ta", [])
        r_en = t.get("rows_en", [])
        r_ta = t.get("rows_ta", [])
        
        print(f"  Table {idx+1}: '{title_en}'")
        print(f"    - Title TA: {bool(title_ta)}")
        print(f"    - Headers EN count: {len(h_en)}, Headers TA count: {len(h_ta)}")
        print(f"    - Rows EN count: {len(r_en)}, Rows TA count: {len(r_ta)}")
        
        # Check row lengths vs header lengths
        for r_idx, row in enumerate(r_en):
            if len(row) != len(h_en):
                print(f"    ⚠️ Row EN {r_idx} length mismatch: got {len(row)}, expected {len(h_en)} (headers)")
        for r_idx, row in enumerate(r_ta):
            if len(row) != len(h_ta):
                print(f"    ⚠️ Row TA {r_idx} length mismatch: got {len(row)}, expected {len(h_ta)} (headers)")
