# -*- coding: utf-8 -*-
with open('gen_sc_medium.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    if '5 senior judges is not the exact count of associates.' in line:
        print(f"Found on line {idx+1}")
        lines[idx] = line.replace('("2 senior judges is the collegium composition for HIGH COURT judge appointments.", "2 மூத்த நீதிபதிகள் என்பது உயர் நீதிமன்ற நீதிபதி நியமனத்துக்கான கொலீஜியம்.", "3 is incorrect.", "3 என்பது தவறானது.", "4 senior-most judges + CJI (total 5) form the SC appointment Collegium.", "4 மூத்த நீதிபதிகள் + CJI (மொத்தம் 5) உச்ச நீதிமன்ற நியமன கொலீஜியம் ஆவர்.", "5 senior judges is not the exact count of associates.")', '("2 senior judges is the collegium composition for HIGH COURT judge appointments.", "2 மூத்த நீதிபதிகள் என்பது உயர் நீதிமன்ற நீதிபதி நியமனத்துக்கான கொலீஜியம்.", "3 is incorrect.", "3 என்பது தவறானது.", "4 senior-most judges + CJI (total 5) form the SC appointment Collegium.", "4 மூத்த நீதிபதிகள் + CJI (மொத்தம் 5) உச்ச நீதிமன்ற நியமன கொலீஜியம் ஆவர்.", "5 senior judges is not the exact count of associates.", "5 மூத்த நீதிபதிகள் என்பது தவறான எண்ணிக்கையாகும்.")')

with open('gen_sc_medium.py', 'w', encoding='utf-8') as f:
    f.writelines(lines)
print("Fix applied.")
