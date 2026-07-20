import json
import sys
from pathlib import Path

# Fix build_hard_repository.py, build_hard_part2.py, build_hard_part3.py execution
target_path = Path(r"c:\Users\Home\Desktop\tnpsc_ai\data\questions\polity\historical_background_hard.json")

# Let's execute build_hard_repository.py
import subprocess
print("Running build_hard_repository.py...")
res1 = subprocess.run([sys.executable, "build_hard_repository.py"], capture_output=True, text=True)
print(res1.stdout, res1.stderr)

# Now read q1-10
q_all = json.load(open(target_path, "r", encoding="utf-8"))
print(f"Loaded {len(q_all)} questions from step 1.")

# Modify build_hard_part2.py to not re-init empty list but read existing
print("Running build_hard_part2.py...")
res2 = subprocess.run([sys.executable, "build_hard_part2.py"], capture_output=True, text=True)
print(res2.stdout, res2.stderr)

q_all = json.load(open(target_path, "r", encoding="utf-8"))
print(f"Loaded {len(q_all)} questions from step 2.")

# Now read build_hard_part3.py questions function or run script that appends to file
