import json
import sys
import streamlit as st

# Mock streamlit functions if needed or run in bare mode
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

from ui.notes.renderer import render_notes_engine

for p in ['president_part_1.json', 'president_part_2.json', 'president_part_3.json']:
    path = f'data/notes/polity/{p}'
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    print(f"\n==========================================")
    print(f"Testing render for {p}")
    print(f"==========================================")
    # We test loading data content
    content = data.get("content", data)
    keys = list(content.keys())
    print("Content keys:", keys)
