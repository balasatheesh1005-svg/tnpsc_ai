# -*- coding: utf-8 -*-
with open('gen_sc_medium.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    if 'Unrelated to appointment cases.' in line:
        print(f"Found on line {idx+1}")
        lines[idx] = line.replace(', "Unrelated to appointment cases.", "நியமன வழக்குகளுடன் தொடர்பற்றது."', '')

with open('gen_sc_medium.py', 'w', encoding='utf-8') as f:
    f.writelines(lines)
print("Fix 2 applied.")
