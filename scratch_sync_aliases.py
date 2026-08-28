import json
import shutil
import os

pairs = [
    ("data/questions/polity/president_statement.json", "data/questions/polity/president_statement_based.json"),
    ("data/questions/polity/president_reasoning.json", "data/questions/polity/president_assertion_reason.json"),
    ("data/questions/polity/president_match.json", "data/questions/polity/president_match_the_following.json")
]

for src, dst in pairs:
    if os.path.exists(src):
        shutil.copyfile(src, dst)
        print(f"Synced {src} -> {dst}")
