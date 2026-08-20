# -*- coding: utf-8 -*-
"""
Full Complete Builder script for 50 TNPSC Group 1 Standard PYQ Practice MCQs
Topic: Preamble of the Constitution of India
Target Files:
  - data/questions/polity/preamble_pyq.json
  - data/questions/polity/preamble_pyq_practice.json
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

questions_data = [
    # Q1 (A)
    {
        "id": "PRE_PYQ_001",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Easy",
        "question_type": "Direct PYQ Pattern",
        "question": {
            "en": "Which date is explicitly mentioned in the Preamble of the Constitution of India as the date of its adoption, enactment, and giving to themselves?",
            "ta": "இந்திய அரசியலமைப்பின் முகவுரையில் அரசியலமைப்பு ஏற்றுக்கொள்ளப்பட்ட, இயற்றப்பட்ட மற்றும் நமக்கு நாமே வழங்கப்பட்ட நாளாக வெளிப்படையாகக் குறிப்பிடப்பட்டுள்ள தேதி எது?"
        },
        "options": [
            {"id": "A", "en": "26th November 1949", "ta": "26 நவம்பர் 1949"},
            {"id": "B", "en": "26th January 1950", "ta": "26 ஜனவரி 1950"},
            {"id": "C", "en": "15th August 1947", "ta": "15 ஆகஸ்ட் 1947"},
            {"id": "D", "en": "9th December 1946", "ta": "9 டிசம்பர் 1946"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "The Preamble concludes with: '...in our Constituent Assembly this twenty-sixth day of November, 1949, do hereby adopt, enact and give to ourselves this Constitution.'",
            "ta": "முகவுரையின் இறுதியில்: '...1949 நவம்பர் இருபத்தாறாம் நாளாகிய இன்று, நமது அரசியலமைப்பு நிர்ணய அவையில் இந்த அரசியலமைப்பை ஏற்று, இயற்றி, நமக்கு நாமே வழங்கிக் கொள்கிறோம்' எனக் குறிப்பிடப்பட்டுள்ளது."
        },
        "why_not_others": {
            "A": {"en": "Correct. 26th November 1949 is the date of adoption mentioned in the Preamble.", "ta": "சரி. 26 நவம்பர் 1949 என்பது முகவுரையில் குறிப்பிடப்பட்டுள்ள ஏற்றுக்கொள்ளப்பட்ட தேதியாகும்."},
            "B": {"en": "Incorrect. 26th January 1950 is the date of commencement of the Constitution.", "ta": "தவறு. 26 ஜனவரி 1950 என்பது அரசியலமைப்பு நடைமுறைக்கு வந்த தேதியாகும்."},
            "C": {"en": "Incorrect. 15th August 1947 is Indian Independence Day.", "ta": "தவறு. 15 ஆகஸ்ட் 1947 இந்தியாவின் சுதந்திர தினமாகும்."},
            "D": {"en": "Incorrect. 9th December 1946 was the first meeting of Constituent Assembly.", "ta": "தவறு. 9 டிசம்பர் 1946 அரசியலமைப்பு நிர்ணய அவையின் முதல் கூட்டமாகும்."}
        },
        "tnpsc_tip": {"en": "TNPSC Distinction: Date of Adoption = Nov 26, 1949. Date of Commencement = Jan 26, 1950.", "ta": "TNPSC வேறுபாடு: ஏற்றுக்கொள்ளப்பட்ட தேதி = நவம்பர் 26, 1949. நடைமுறைக்கு வந்த தேதி = ஜனவரி 26, 1950."},
        "revision_fact": {"en": "Nov 26 is celebrated as Constitution Day (Samvidhan Divas) in India since 2015.", "ta": "நவம்பர் 26 ஆம் தேதி 2015 முதல் இந்தியாவில் அரசியலமைப்பு தினமாக (சம்விதான் திவாஸ்) கொண்டாடப்படுகிறது."},
        "source_reference": ["TNPSC Group 1 PYQ", "Text of the Preamble"],
        "bloom_level": "Remember",
        "estimated_time_sec": 40,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "Date of Adoption", "26 November 1949"]
    },

    # Q2 (B)
    {
        "id": "PRE_PYQ_002",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Easy",
        "question_type": "Direct PYQ Pattern",
        "question": {
            "en": "The Preamble of the Indian Constitution is based on which historic resolution introduced in the Constituent Assembly?",
            "ta": "இந்திய அரசியலமைப்பின் முகவுரை அரசியலமைப்பு நிர்ணய அவையில் அறிமுகப்படுத்தப்பட்ட எந்த வரலாற்றுச் சிறப்புமிக்க தீர்மானத்தை அடிப்படையாகக் கொண்டது?"
        },
        "options": [
            {"id": "A", "en": "Quit India Resolution", "ta": "வெள்ளையனே வெளியேறு தீர்மானம்"},
            {"id": "B", "en": "Objectives Resolution", "ta": "குறிக்கோள் தீர்மானம்"},
            {"id": "C", "en": "Poorna Swaraj Resolution", "ta": "பூரண சுயராஜ்ய தீர்மானம்"},
            {"id": "D", "en": "Mountbatten Plan", "ta": "மவுண்ட்பேட்டன் திட்டம்"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "The Preamble is based on the 'Objectives Resolution', drafted and moved by Pandit Jawaharlal Nehru on December 13, 1946, and adopted on January 22, 1947.",
            "ta": "முகவுரை என்பது பண்டித ஜவஹர்லால் நேருவால் டிசம்பர் 13, 1946 இல் முன்மொழியப்பட்டு ஜனவரி 22, 1947 இல் ஏற்றுக்கொள்ளப்பட்ட 'குறிக்கோள் தீர்மானத்தை' அடிப்படையாகக் கொண்டது."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Quit India Resolution was passed in August 1942.", "ta": "தவறு. வெள்ளையனே வெளியேறு தீர்மானம் ஆகஸ்ட் 1942 இல் நிறைவேற்றப்பட்டது."},
            "B": {"en": "Correct. Objectives Resolution moved by Nehru is the foundation of Preamble.", "ta": "சரி. நேருவால் முன்மொழியப்பட்ட குறிக்கோள் தீர்மானமே முகவுரையின் அடித்தளமாகும்."},
            "C": {"en": "Incorrect. Poorna Swaraj Resolution was adopted in Lahore session 1929.", "ta": "தவறு. பூரண சுயராஜ்ய தீர்மானம் 1929 லாகூர் மாநாட்டில் ஏற்றுக்கொள்ளப்பட்டது."},
            "D": {"en": "Incorrect. Mountbatten Plan was the partition plan of June 3, 1947.", "ta": "தவறு. மவுண்ட்பேட்டன் திட்டம் என்பது ஜூன் 3, 1947 இன் பிரிவினை திட்டமாகும்."}
        },
        "tnpsc_tip": {"en": "Objectives Resolution moved = Dec 13, 1946; Adopted = Jan 22, 1947.", "ta": "குறிக்கோள் தீர்மானம் முன்மொழியப்பட்டது = டிசம்பர் 13, 1946; ஏற்கப்பட்டது = ஜனவரி 22, 1947."},
        "revision_fact": {"en": "The modified version of Objectives Resolution forms the present Preamble.", "ta": "குறிக்கோள் தீர்மானத்தின் திருத்தப்பட்ட வடிவமே தற்போதைய முகவுரையாக உள்ளது."},
        "source_reference": ["TNPSC Group 1 PYQ", "M. Laxmikanth - Indian Polity"],
        "bloom_level": "Remember",
        "estimated_time_sec": 45,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "Objectives Resolution", "Jawaharlal Nehru"]
    },

    # Q3 (C)
    {
        "id": "PRE_PYQ_003",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Easy",
        "question_type": "Direct PYQ Pattern",
        "question": {
            "en": "How many times has the Preamble of the Constitution of India been amended since its enactment in 1949?",
            "ta": "1949 இல் இயற்றப்பட்டதிலிருந்து இந்திய அரசியலமைப்பின் முகவுரை இதுவரை எத்தனை முறை திருத்தப்பட்டுள்ளது?"
        },
        "options": [
            {"id": "A", "en": "Three times", "ta": "மூன்று முறை"},
            {"id": "B", "en": "Two times", "ta": "இரண்டு முறை"},
            {"id": "C", "en": "Only once", "ta": "ஒரே ஒரு முறை மட்டுமே"},
            {"id": "D", "en": "Never amended", "ta": "ஒருபோதும் திருத்தப்படவில்லை"}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "The Preamble has been amended only once so far, by the 42nd Constitutional Amendment Act of 1976.",
            "ta": "முகவுரை இதுவரை 1976 ஆம் ஆண்டின் 42வது அரசியலமைப்புத் திருத்தச் சட்டத்தின் மூலம் ஒரே ஒரு முறை மட்டுமே திருத்தப்பட்டுள்ளது."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. It has not been amended 3 times.", "ta": "தவறு. இது 3 முறை திருத்தப்படவில்லை."},
            "B": {"en": "Incorrect. It has not been amended twice.", "ta": "தவறு. இது இரண்டு முறை திருத்தப்படவில்லை."},
            "C": {"en": "Correct. Preamble has been amended only once in 1976.", "ta": "சரி. முகவுரை 1976-ல் ஒரே ஒரு முறை மட்டுமே திருத்தப்பட்டது."},
            "D": {"en": "Incorrect. It was amended in 1976.", "ta": "தவறு. இது 1976 இல் திருத்தப்பட்டது."}
        },
        "tnpsc_tip": {"en": "TNPSC Frequent Fact: Preamble amended ONLY ONCE by 42nd Amendment Act 1976.", "ta": "TNPSC அடிக்கடி கேட்கும் உண்மை: முகவுரை 1976-ன் 42வது திருத்தச் சட்டத்தால் ஒரே ஒரு முறை மட்டுமே திருத்தப்பட்டது."},
        "revision_fact": {"en": "42nd Constitutional Amendment Act 1976 added three new words: Socialist, Secular, Integrity.", "ta": "42வது அரசியலமைப்புத் திருத்தச் சட்டம் 1976 மூன்று புதிய சொற்களைச் சேர்த்தது: சமதர்ம, மதச்சார்பற்ற, ஒருமைப்பாடு."},
        "source_reference": ["TNPSC Group 1 PYQ", "Constitution of India"],
        "bloom_level": "Remember",
        "estimated_time_sec": 30,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "42nd Amendment", "Amendments Count"]
    },

    # Q4 (D)
    {
        "id": "PRE_PYQ_004",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Easy",
        "question_type": "Direct PYQ Pattern",
        "question": {
            "en": "Which Constitutional Amendment Act inserted the words 'Socialist', 'Secular', and 'Integrity' into the Preamble?",
            "ta": "எந்த அரசியலமைப்புத் திருத்தச் சட்டம் 'சமதர்ம' (Socialist), 'மதச்சார்பற்ற' (Secular) மற்றும் 'ஒருமைப்பாடு' (Integrity) ஆகிய சொற்களை முகவுரையில் சேர்த்தது?"
        },
        "options": [
            {"id": "A", "en": "44th Constitutional Amendment Act, 1978", "ta": "44வது அரசியலமைப்புத் திருத்தச் சட்டம், 1978"},
            {"id": "B", "en": "24th Constitutional Amendment Act, 1971", "ta": "24வது அரசியலமைப்புத் திருத்தச் சட்டம், 1971"},
            {"id": "C", "en": "86th Constitutional Amendment Act, 2002", "ta": "86வது அரசியலமைப்புத் திருத்தச் சட்டம், 2002"},
            {"id": "D", "en": "42nd Constitutional Amendment Act, 1976", "ta": "42வது அரசியலமைப்புத் திருத்தச் சட்டம், 1976"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "The 42nd Constitutional Amendment Act, 1976 added three words to the Preamble: 'Socialist', 'Secular', and 'Integrity'.",
            "ta": "1976-ன் 42வது அரசியலமைப்புத் திருத்தச் சட்டம் முகவுரையில் மூன்று சொற்களைச் சேர்த்தது: 'சமதர்ம', 'மதச்சார்பற்ற' மற்றும் 'ஒருமைப்பாடு'."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. 44th Amendment 1978 reversed several provisions of 42nd Amendment and removed Right to Property from Part III.", "ta": "தவறு. 44வது திருத்தம் 1978 சொத்துரிமையை அடிப்படை உரிமைகளிலிருந்து நீக்கியது."},
            "B": {"en": "Incorrect. 24th Amendment 1971 affirmed Parliament's power to amend Fundamental Rights.", "ta": "தவறு. 24வது திருத்தம் 1971 அடிப்படை உரிமைகளைத் திருத்தும் அதிகாரத்தை உறுதிப்படுத்தியது."},
            "C": {"en": "Incorrect. 86th Amendment 2002 added Right to Education (Art 21A).", "ta": "தவறு. 86வது திருத்தம் 2002 கல்வி உரிமையைச் சேர்த்தது (உறுப்பு 21A)."},
            "D": {"en": "Correct. 42nd Amendment Act 1976 inserted Socialist, Secular, and Integrity into Preamble.", "ta": "சரி. 42வது திருத்தச் சட்டம் 1976 முகவுரையில் சமதர்ம, மதச்சார்பற்ற, ஒருமைப்பாடு சொற்களைச் சேர்த்தது."}
        },
        "tnpsc_tip": {"en": "Remember the mnemonic: SSI = Socialist, Secular, Integrity added by 42nd Amendment in 1976.", "ta": "நினைவில் கொள்ள: SSI = சமதர்ம (Socialist), மதச்சார்பற்ற (Secular), ஒருமைப்பாடு (Integrity) - 42வது திருத்தம் 1976."}
    }
]

print(f"Base setup with {len(questions_data)} questions.")
