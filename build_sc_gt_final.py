# -*- coding: utf-8 -*-
"""
Supreme Court Grand Test (100 Questions) Full Generator & Balancer
"""

import json
import os
import random
import sys

sys.stdout.reconfigure(encoding='utf-8')

def get_questions_part1():
    # Questions 1 to 25
    qs = []
    
    # Q1
    qs.append({
        "id": "POLITY_SC_GT_001",
        "subject": "Polity",
        "topic": "Supreme Court of India",
        "difficulty": "Medium",
        "question_type": "Statement",
        "question": {
            "en": "Consider the following statements regarding the appointment of judges to the Supreme Court of India:\n1. The Chief Justice of India is appointed by the President after consultation with such judges of the Supreme Court and High Courts as the President deems necessary.\n2. In the Third Judges Case (1998), the Supreme Court held that the recommendation of CJI without consulting a collegium of four senior-most judges of the SC is not binding on the Government.\n3. The seniority rule for appointing the senior-most judge of the SC as CJI has been strictly followed without exception since 1950.\nWhich of the statements given above is/are correct?",
            "ta": "இந்திய உச்ச நீதிமன்ற நீதிபதிகள் நியமனம் குறித்த பின்வரும் கூற்றுகளைக் கருதுக:\n1. குடியரசுத் தலைவரால் தேவையானதாகக் கருதப்படும் உச்ச நீதிமன்ற மற்றும் உயர் நீதிமன்ற நீதிபதிகளுடன் ஆலோசித்த பிறகே இந்திய தலைமை நீதிபதி நியமிக்கப்படுகிறார்.\n2. மூன்றாவது நீதிபதிகள் வழக்கில் (1998), உச்ச நீதிமன்றத்தின் நான்கு மூத்த நீதிபதிகள் கொண்ட குழுவைக் கலந்தாலோசிக்காமல் தலைமை நீதிபதி அளிக்கும் பரிந்துரை அரசைக்கட்டுப்படுத்தாது என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது.\n3. 1950 முதல் எந்தவித விதிவிலக்கும் இன்றி உச்ச நீதிமன்றத்தின் மிக மூத்த நீதிபதியை தலைமை நீதிபதியாக நியமிக்கும் மூப்பு விதி கண்டிப்பாக பின்பற்றப்பட்டு வருகிறது.\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானது?"
        },
        "question_en": "Consider the following statements regarding the appointment of judges to the Supreme Court of India:\n1. The Chief Justice of India is appointed by the President after consultation with such judges of the Supreme Court and High Courts as the President deems necessary.\n2. In the Third Judges Case (1998), the Supreme Court held that the recommendation of CJI without consulting a collegium of four senior-most judges of the SC is not binding on the Government.\n3. The seniority rule for appointing the senior-most judge of the SC as CJI has been strictly followed without exception since 1950.\nWhich of the statements given above is/are correct?",
        "question_ta": "இந்திய உச்ச நீதிமன்ற நீதிபதிகள் நியமனம் குறித்த பின்வரும் கூற்றுகளைக் கருதுக:\n1. குடியரசுத் தலைவரால் தேவையானதாகக் கருதப்படும் உச்ச நீதிமன்ற மற்றும் உயர் நீதிமன்ற நீதிபதிகளுடன் ஆலோசித்த பிறகே இந்திய தலைமை நீதிபதி நியமிக்கப்படுகிறார்.\n2. மூன்றாவது நீதிபதிகள் வழக்கில் (1998), உச்ச நீதிமன்றத்தின் நான்கு மூத்த நீதிபதிகள் கொண்ட குழுவைக் கலந்தாலோசிக்காமல் தலைமை நீதிபதி அளிக்கும் பரிந்துரை அரசைக்கட்டுப்படுத்தாது என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது.\n3. 1950 முதல் எந்தவித விதிவிலக்கும் இன்றி உச்ச நீதிமன்றத்தின் மிக மூத்த நீதிபதியை தலைமை நீதிபதியாக நியமிக்கும் மூப்பு விதி கண்டிப்பாக பின்பற்றப்பட்டு வருகிறது.\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            {"id": "A", "en": "1 and 2 only", "ta": "1 மற்றும் 2 மட்டும்"},
            {"id": "B", "en": "2 and 3 only", "ta": "2 மற்றும் 3 மட்டும்"},
            {"id": "C", "en": "1 and 3 only", "ta": "1 மற்றும் 3 மட்டும்"},
            {"id": "D", "en": "1, 2 and 3", "ta": "1, 2 மற்றும் 3"}
        ],
        "options_en": {"A": "1 and 2 only", "B": "2 and 3 only", "C": "1 and 3 only", "D": "1, 2 and 3"},
        "options_ta": {"A": "1 மற்றும் 2 மட்டும்", "B": "2 மற்றும் 3 மட்டும்", "C": "1 மற்றும் 3 மட்டும்", "D": "1, 2 மற்றும் 3"},
        "correct_answer": "A",
        "explanation": {
            "en": "Statements 1 and 2 are correct. Under Article 124(2), judges are appointed by the President. In the 3rd Judges Case (1998), CJI must consult a collegium of 4 senior-most SC judges. Statement 3 is incorrect because the seniority rule was violated twice: A.N. Ray (1973) superseding 3 senior judges and M.U. Beg (1977) superseding H.R. Khanna.",
            "ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. சரத்து 124(2)-ன் படி நீதிபதிகளை குடியரசுத் தலைவர் நியமிக்கிறார். 3வது நீதிபதிகள் வழக்கில் (1998) 4 மூத்த நீதிபதிகள் கொண்ட கொலீஜியத்தைக் கலந்தாலோசிக்க வேண்டும் என தீர்ப்பளிக்கப்பட்டது. கூற்று 3 தவறானது, ஏனெனில் 1973-ல் ஏ.என். ரே மற்றும் 1977-ல் எம்.யு. பேக் நியமனத்தின் போது மூப்பு விதி மீறப்பட்டது."
        },
        "explanation_en": "Statements 1 and 2 are correct. Under Article 124(2), judges are appointed by the President. In the 3rd Judges Case (1998), CJI must consult a collegium of 4 senior-most SC judges. Statement 3 is incorrect because the seniority rule was violated twice: A.N. Ray (1973) superseding 3 senior judges and M.U. Beg (1977) superseding H.R. Khanna.",
        "explanation_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. சரத்து 124(2)-ன் படி நீதிபதிகளை குடியரசுத் தலைவர் நியமிக்கிறார். 3வது நீதிபதிகள் வழக்கில் (1998) 4 மூத்த நீதிபதிகள் கொண்ட கொலீஜியத்தைக் கலந்தாலோசிக்க வேண்டும் என தீர்ப்பளிக்கப்பட்டது. கூற்று 3 தவறானது, ஏனெனில் 1973-ல் ஏ.என். ரே மற்றும் 1977-ல் எம்.யு. பேக் நியமனத்தின் போது மூப்பு விதி மீறப்பட்டது.",
        "why_not_others": {
            "A": {"en": "✅ Correct choice.", "ta": "✅ சரியான தெரிவு."},
            "B": {"en": "❌ Incorrect choice.", "ta": "❌ தவறான தெரிவு."},
            "C": {"en": "❌ Incorrect choice.", "ta": "❌ தவறான தெரிவு."},
            "D": {"en": "❌ Incorrect choice.", "ta": "❌ தவறான தெரிவு."}
        },
        "trap_point": {"en": "Seniority rule was broken twice (1973, 1977).", "ta": "மூப்பு விதி இருமுறை மீறப்பட்டது (1973, 1977)."},
        "tnpsc_tip": {"en": "3rd Judges Case expanded Collegium to CJI + 4.", "ta": "3வது நீதிபதிகள் வழக்கு கொலீஜியத்தை CJI + 4 என விரிவுபடுத்தியது."},
        "high_yield_fact": {"en": "Article 124(2) governs SC judge appointments.", "ta": "சரத்து 124(2) உச்ச நீதிமன்ற நீதிபதிகள் நியமனத்தைக் நிர்வகிக்கிறது."},
        "source_reference": ["M. Laxmikanth – Indian Polity"]
    })

    # Q2
    qs.append({
        "id": "POLITY_SC_GT_002",
        "subject": "Polity",
        "topic": "Supreme Court of India",
        "difficulty": "Easy",
        "question_type": "Direct",
        "question": {
            "en": "Under Article 130 of the Constitution, who is authorized to appoint other place or places as the seat of the Supreme Court of India?",
            "ta": "அரசியலமைப்பின் சரத்து 130 இன் படி, உச்ச நீதிமன்றத்தின் அமர்வை டெல்லி தவிர பிற இடங்களுக்கு மாற்றும் அதிகாரம் யாருக்கு உள்ளது?"
        },
        "question_en": "Under Article 130 of the Constitution, who is authorized to appoint other place or places as the seat of the Supreme Court of India?",
        "question_ta": "அரசியலமைப்பின் சரத்து 130 இன் படி, உச்ச நீதிமன்றத்தின் அமர்வை டெல்லி தவிர பிற இடங்களுக்கு மாற்றும் அதிகாரம் யாருக்கு உள்ளது?",
        "options": [
            {"id": "A", "en": "The Parliament by enacting a law", "ta": "சட்டம் இயற்றுவதன் மூலம் நாடாளுமன்றத்திற்கு"},
            {"id": "B", "en": "The Chief Justice of India with the approval of the President", "ta": "குடியரசுத் தலைவரின் ஒப்புதலுடன் இந்திய தலைமை நீதிபதிக்கு"},
            {"id": "C", "en": "The President of India on the advice of the Union Cabinet", "ta": "மத்திய அமைச்சரவையின் ஆலோசனையின் பேரில் குடியரசுத் தலைவருக்கு"},
            {"id": "D", "en": "The Law Commission of India", "ta": "இந்திய சட்ட ஆணையத்திற்கு"}
        ],
        "options_en": {
            "A": "The Parliament by enacting a law",
            "B": "The Chief Justice of India with the approval of the President",
            "C": "The President of India on the advice of the Union Cabinet",
            "D": "The Law Commission of India"
        },
        "options_ta": {
            "A": "சட்டம் இயற்றுவதன் மூலம் நாடாளுமன்றத்திற்கு",
            "B": "குடியரசுத் தலைவரின் ஒப்புதலுடன் இந்திய தலைமை நீதிபதிக்கு",
            "C": "மத்திய அமைச்சரவையின் ஆலோசனையின் பேரில் குடியரசுத் தலைவருக்கு",
            "D": "இந்திய சட்ட ஆணையத்திற்கு"
        },
        "correct_answer": "B",
        "explanation": {
            "en": "Article 130 authorizes CJI with President's approval to appoint other places as SC seat.",
            "ta": "சரத்து 130 குடியரசுத் தலைவர் ஒப்புதலுடன் பிற இடங்களை அமர்வாக நியமிக்க CJI-க்கு அதிகாரம் அளிக்கிறது."
        },
        "explanation_en": "Article 130 authorizes CJI with President's approval to appoint other places as SC seat.",
        "explanation_ta": "சரத்து 130 குடியரசுத் தலைவர் ஒப்புதலுடன் பிற இடங்களை அமர்வாக நியமிக்க CJI-க்கு அதிகாரம் அளிக்கிறது.",
        "why_not_others": {
            "A": {"en": "❌ Incorrect choice.", "ta": "❌ தவறான தெரிவு."},
            "B": {"en": "✅ Correct choice.", "ta": "✅ சரியான தெரிவு."},
            "C": {"en": "❌ Incorrect choice.", "ta": "❌ தவறான தெரிவு."},
            "D": {"en": "❌ Incorrect choice.", "ta": "❌ தவறான தெரிவு."}
        },
        "trap_point": {"en": "It is CJI with President approval, not Parliament by law.", "ta": "நாடாளுமன்றச் சட்டம் அல்ல, குடியரசுத் தலைவர் ஒப்புதலுடன் CJI."},
        "tnpsc_tip": {"en": "Seat of SC = Article 130.", "ta": "அமர்வு = சரத்து 130."},
        "high_yield_fact": {"en": "Delhi is the seat of SC under Art 130.", "ta": "சரத்து 130-ன் கீழ் டெல்லி அமர்வாக உள்ளது."},
        "source_reference": ["M. Laxmikanth – Indian Polity"]
    })

    return qs

if __name__ == "__main__":
    q1_25 = get_questions_part1()
    print(f"Loaded {len(q1_25)} questions in part 1.")
