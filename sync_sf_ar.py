import json
import shutil
import os

src = r"c:\Users\Home\Desktop\tnpsc_ai\data\questions\polity\salient_features_of_the_indian_constitution_reasoning.json"
dst = r"c:\Users\Home\Desktop\tnpsc_ai\data\questions\polity\salient_features_of_the_indian_constitution_assertion_reason.json"

assert os.path.exists(src), f"Source file does not exist: {src}"

shutil.copyfile(src, dst)

with open(dst, encoding="utf-8") as f:
    qs = json.load(f)

print(f"Successfully copied reasoning file to assertion_reason file!")
print(f"Total questions in {dst}: {len(qs)}")
