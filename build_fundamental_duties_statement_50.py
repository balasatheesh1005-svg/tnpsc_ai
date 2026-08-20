# -*- coding: utf-8 -*-
"""
Script to build 50 High-Yield Statement MCQs for Fundamental Duties
Target File: data/questions/polity/fundamental_duties_statement.json
"""

import json
import os

questions_data = [
    {
        "id": "FD_S_001",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Statement",
        "question": {
            "en": "Consider the following statements regarding the constitutional location and introduction of Fundamental Duties:\n1. Fundamental Duties were incorporated into Part IVA of the Constitution by the 42nd Constitutional Amendment Act, 1976.\n2. Article 51A is the sole article contained in Part IVA of the Indian Constitution.\nWhich of the statements given above is/are CORRECT?",
            "ta": "அடிப்படை கடமைகளின் அரசியலமைப்பு இடம் மற்றும் அறிமுகம் பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. 1976-ன் 42வது அரசியலமைப்பு திருத்தச் சட்டத்தின் மூலம் அரசியலமைப்பின் பகுதி IVA-ல் அடிப்படை கடமைகள் சேர்க்கப்பட்டன.\n2. இந்திய அரசியலமைப்பின் பகுதி IVA-ல் உள்ள ஒரே உறுப்பு உறுப்பு 51A மட்டுமே ஆகும்.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 only", "ta": "1 மட்டுமே"},
            {"id": "B", "en": "2 only", "ta": "2 மட்டுமே"},
            {"id": "C", "en": "Both 1 and 2", "ta": "1 மற்றும் 2 இரண்டும்"},
            {"id": "D", "en": "Neither 1 nor 2", "ta": "1-ம் இல்லை 2-ம் இல்லை"}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "Both statements 1 and 2 are CORRECT. The 42nd CAA 1976 added Part IVA consisting solely of Article 51A, which originally enumerated 10 Fundamental Duties.",
            "ta": "கூற்றுகள் 1 மற்றும் 2 இரண்டும் சரியானவை. 42வது திருத்தச் சட்டம் 1976 உறுப்பு 51A-ஐ மட்டுமே கொண்ட பகுதி IVA-ஐச் சேர்த்தது, அது ஆரம்பத்தில் 10 அடிப்படை கடமைகளைப் பட்டியலிட்டது."
        },
        "why_not_others": {
            "A": {"en": "Statement 2 is also correct.", "ta": "கூற்று 2-ம் சரியானது."},
            "B": {"en": "Statement 1 is also correct.", "ta": "கூற்று 1-ம் சரியானது."},
            "C": {"en": "Correct. Both statements 1 and 2 are correct.", "ta": "சரி. கூற்றுகள் 1 மற்றும் 2 இரண்டும் சரியானவை."},
            "D": {"en": "Both statements are true.", "ta": "இரண்டு கூற்றுகளும் உண்மை."}
        },
        "tnpsc_tip": {
            "en": "Part IVA contains only ONE Article (Article 51A).",
            "ta": "பகுதி IVA ஒரே ஒரு உறுப்பை மட்டுமே (உறுப்பு 51A) கொண்டுள்ளது."
        }
    },
    {
        "id": "FD_S_002",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Hard",
        "question_type": "Statement",
        "question": {
            "en": "Consider the following statements regarding the Sardar Swaran Singh Committee (1976):\n1. The Committee recommended 8 Fundamental Duties to be added to the Constitution.\n2. The Committee recommended that Parliament should impose penalty or punishment for non-compliance with any duty.\n3. Parliament accepted all 8 recommendations of the Committee without any rejection or addition.\nWhich of the statements given above are CORRECT?",
            "ta": "சர்தார் ஸ்வரன் சிங் குழு (1976) பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. அரசியலமைப்பில் 8 அடிப்படை கடமைகளைச் சேர்க்கக் குழு பரிந்துரைத்தது.\n2. எந்தவொரு கடமையையும் மீறுவதற்கு நாடாளுமன்றம் தண்டனை அல்லது அபராதம் விதிக்க வேண்டும் என்று குழு பரிந்துரைத்தது.\n3. நாடாளுமன்றம் குழுவின் 8 பரிந்துரைகளையும் எவ்வித நிராகரிப்போ அல்லது சேர்க்கையோ இன்றி ஏற்றுக்கொண்டது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 and 2 only", "ta": "1 மற்றும் 2 மட்டும்"},
            {"id": "B", "en": "2 and 3 only", "ta": "2 மற்றும் 3 மட்டும்"},
            {"id": "C", "en": "1 and 3 only", "ta": "1 மற்றும் 3 மட்டும்"},
            {"id": "D", "en": "1, 2 and 3", "ta": "1, 2 மற்றும் 3"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Statements 1 and 2 are CORRECT. Statement 3 is INCORRECT because Parliament rejected key recommendations (such as duty to pay taxes and immunity of penalty laws) and enacted 10 duties instead of 8.",
            "ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறு, ஏனெனில் நாடாளுமன்றம் சில முக்கிய பரிந்துரைகளை (வரி செலுத்தும் கடமை போன்றவை) நிராகரித்தது மற்றும் 8-க்கு பதிலாக 10 கடமைகளை இயற்றியது."
        },
        "why_not_others": {
            "A": {"en": "Correct. Statements 1 and 2 are true, while Statement 3 is false.", "ta": "சரி. கூற்றுகள் 1 மற்றும் 2 உண்மை, கூற்று 3 தவறு."},
            "B": {"en": "Statement 3 is false.", "ta": "கூற்று 3 தவறானது."},
            "C": {"en": "Statement 3 is false.", "ta": "கூற்று 3 தவறானது."},
            "D": {"en": "Statement 3 is false.", "ta": "கூற்று 3 தவறானது."}
        },
        "tnpsc_tip": {
            "en": "Swaran Singh Committee recommended 8 duties; 42nd Amendment enacted 10 duties.",
            "ta": "ஸ்வரன் சிங் குழு 8 கடமைகளைப் பரிந்துரைத்தது; 42வது திருத்தம் 10 கடமைகளை இயற்றியது."
        }
    },
    {
        "id": "FD_S_003",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Statement",
        "question": {
            "en": "Consider the following statements regarding the numerical growth of Fundamental Duties:\n1. The original 1950 Constitution contained 10 Fundamental Duties.\n2. The 42nd Constitutional Amendment Act 1976 introduced 10 Fundamental Duties.\n3. The 86th Constitutional Amendment Act 2002 added the 11th Fundamental Duty under Article 51A(k).\n4. Presently, Article 51A enumerates a total of 11 Fundamental Duties.\nWhich of the statements given above are CORRECT?",
            "ta": "அடிப்படை கடமைகளின் எண்ணிக்கை வளர்ச்சி பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. அசல் 1950 அரசியலமைப்பு 10 அடிப்படை கடமைகளைக் கொண்டிருந்தது.\n2. 1976-ன் 42வது அரசியலமைப்பு திருத்தச் சட்டம் 10 அடிப்படை கடமைகளை அறிமுகப்படுத்தியது.\n3. 2002-ன் 86வது அரசியலமைப்பு திருத்தச் சட்டம் உறுப்பு 51A(k)-ன் கீழ் 11வது அடிப்படை கடமையைச் சேர்த்தது.\n4. தற்போது, உறுப்பு 51A மொத்தம் 11 அடிப்படை கடமைகளைப் பட்டியலிடுகிறது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1, 2 and 3 only", "ta": "1, 2 மற்றும் 3 மட்டும்"},
            {"id": "B", "en": "2, 3 and 4 only", "ta": "2, 3 மற்றும் 4 மட்டும்"},
            {"id": "C", "en": "1 and 4 only", "ta": "1 மற்றும் 4 மட்டும்"},
            {"id": "D", "en": "1, 2, 3 and 4", "ta": "1, 2, 3 மற்றும் 4"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "Statements 2, 3, and 4 are CORRECT. Statement 1 is INCORRECT because the original 1950 Constitution contained ZERO Fundamental Duties.",
            "ta": "கூற்றுகள் 2, 3, மற்றும் 4 சரியானவை. கூற்று 1 தவறு, ஏனெனில் அசல் 1950 அரசியலமைப்பில் அடிப்படை கடமைகள் ஏதும் இருக்கவில்லை."
        },
        "why_not_others": {
            "A": {"en": "Statement 1 is false.", "ta": "கூற்று 1 தவறானது."},
            "B": {"en": "Correct. Statements 2, 3, and 4 are true, while Statement 1 is false.", "ta": "சரி. கூற்றுகள் 2, 3, மற்றும் 4 உண்மை, கூற்று 1 தவறு."},
            "C": {"en": "Statement 1 is false.", "ta": "கூற்று 1 தவறானது."},
            "D": {"en": "Statement 1 is false.", "ta": "கூற்று 1 தவறானது."}
        },
        "tnpsc_tip": {
            "en": "Original Constitution (1950) = 0 | 42nd CAA (1976) = 10 | 86th CAA (2002) = 11.",
            "ta": "அசல் அரசியலமைப்பு (1950) = 0 | 42வது திருத்தம் (1976) = 10 | 86வது திருத்தம் (2002) = 11."
        }
    },
    {
        "id": "FD_S_004",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Statement",
        "question": {
            "en": "Consider the following statements regarding Article 51A(a):\n1. It obligates every citizen to abide by the Constitution and respect its ideals and institutions, the National Flag and National Anthem.\n2. The National Song (Vande Mataram) is explicitly mentioned alongside the National Anthem in Article 51A(a).\nWhich of the statements given above is/are CORRECT?",
            "ta": "உறுப்பு 51A(a) பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. இது ஒவ்வொரு குடிமகனும் அரசியலமைப்புக்குக் கீழ்ப்படிந்து அதன் லட்சியங்கள், நிறுவனங்கள், தேசியக் கொடி மற்றும் தேசியக் கீதத்தை மதிக்கக் கடமைப்படுத்துகிறது.\n2. தேசியப் பாடல் (வந்தே மாதரம்) உறுப்பு 51A(a)-ல் தேசியக் கீதத்துடன் வெளிப்படையாகக் குறிப்பிடப்பட்டுள்ளது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 only", "ta": "1 மட்டுமே"},
            {"id": "B", "en": "2 only", "ta": "2 மட்டுமே"},
            {"id": "C", "en": "Both 1 and 2", "ta": "1 மற்றும் 2 இரண்டும்"},
            {"id": "D", "en": "Neither 1 nor 2", "ta": "1-ம் இல்லை 2-ம் இல்லை"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Statement 1 is CORRECT. Statement 2 is INCORRECT because Article 51A(a) mentions only the National Flag and National Anthem; Vande Mataram (National Song) is NOT mentioned.",
            "ta": "கூற்று 1 சரியானது. கூற்று 2 தவறு, ஏனெனில் உறுப்பு 51A(a) தேசியக் கொடி மற்றும் தேசியக் கீதத்தை மட்டுமே குறிப்பிடுகிறது; வந்தே மாதரம் (தேசியப் பாடல்) குறிப்பிடப்படவில்லை."
        },
        "why_not_others": {
            "A": {"en": "Correct. Statement 1 is true, while Statement 2 is false.", "ta": "சரி. கூற்று 1 உண்மை, கூற்று 2 தவறு."},
            "B": {"en": "Statement 2 is false.", "ta": "கூற்று 2 தவறானது."},
            "C": {"en": "Statement 2 is false.", "ta": "கூற்று 2 தவறானது."},
            "D": {"en": "Statement 1 is true.", "ta": "கூற்று 1 உண்மையாகும்."}
        },
        "tnpsc_tip": {
            "en": "Classic TNPSC trap: Vande Mataram is NOT listed in Article 51A(a).",
            "ta": "பிரபலமான டிஎன்பிஎஸ்சி பொறி: வந்தே மாதரம் உறுப்பு 51A(a)-ல் பட்டியலிடப்படவில்லை."
        }
    },
    {
        "id": "FD_S_005",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Statement",
        "question": {
            "en": "Consider the following statements regarding Articles 51A(b) and 51A(c):\n1. Article 51A(b) mandates cherishing and following the noble ideals that inspired our national struggle for freedom.\n2. Article 51A(c) mandates upholding and protecting the sovereignty, unity, and integrity of India.\n3. The word 'Integrity' was present in Article 51A(c) when it was introduced in 1976.\nWhich of the statements given above are CORRECT?",
            "ta": "உறுப்புகள் 51A(b) மற்றும் 51A(c) பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. உறுப்பு 51A(b) நமது தேசிய சுதந்திரப் போராட்டத்திற்கு ஊக்கமளித்த உயரிய லட்சியங்களைப் போற்றிப் பின்பற்றுமாறு ஆணையிடுகிறது.\n2. உறுப்பு 51A(c) இந்தியாவின் இறையாண்மை, ஒற்றுமை மற்றும் ஒருமைப்பாட்டைப் பேணிப் பாதுகாக்குமாறு ஆணையிடுகிறது.\n3. 1976-ல் அறிமுகப்படுத்தப்பட்ட போது 'ஒருமைப்பாடு' (Integrity) என்ற சொல் உறுப்பு 51A(c)-ல் இருந்தது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 and 2 only", "ta": "1 மற்றும் 2 மட்டும்"},
            {"id": "B", "en": "2 and 3 only", "ta": "2 மற்றும் 3 மட்டும்"},
            {"id": "C", "en": "1 and 3 only", "ta": "1 மற்றும் 3 மட்டும்"},
            {"id": "D", "en": "1, 2 and 3", "ta": "1, 2 மற்றும் 3"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "All three statements are CORRECT. Article 51A(b) covers freedom ideals, Art 51A(c) covers sovereignty, unity, and integrity, and the word 'integrity' was included from inception in 1976.",
            "ta": "மூன்று கூற்றுகளும் சரியானவை. உறுப்பு 51A(b) சுதந்திர லட்சியங்களையும், உறுப்பு 51A(c) இறையாண்மை, ஒற்றுமை, ஒருமைப்பாட்டையும் உள்ளடக்கியுள்ளது, மேலும் 'ஒருமைப்பாடு' என்ற சொல் 1976 முதலே சேர்க்கப்பட்டது."
        },
        "why_not_others": {
            "A": {"en": "Statement 3 is also correct.", "ta": "கூற்று 3-ம் சரியானது."},
            "B": {"en": "Statement 1 is also correct.", "ta": "கூற்று 1-ம் சரியானது."},
            "C": {"en": "Statement 2 is also correct.", "ta": "கூற்று 2-ம் சரியானது."},
            "D": {"en": "Correct. All statements 1, 2, and 3 are correct.", "ta": "சரி. 1, 2 மற்றும் 3 ஆகிய அனைத்துக் கூற்றுகளும் சரி."}
        },
        "tnpsc_tip": {
            "en": "Article 51A(c) combines all three: Sovereignty, Unity, and Integrity.",
            "ta": "உறுப்பு 51A(c) மூன்றையும் இணைக்கிறது: இறையாண்மை, ஒற்றுமை, மற்றும் ஒருமைப்பாடு."
        }
    },
    {
        "id": "FD_S_006",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Hard",
        "question_type": "Statement",
        "question": {
            "en": "Consider the following statements regarding Article 51A(d) and compulsory national service:\n1. Article 51A(d) commands citizens to defend the country and render national service when called upon to do so.\n2. Article 23(2) prohibits the State from imposing compulsory service for public purposes under any circumstances.\nWhich of the statements given above is/are CORRECT?",
            "ta": "உறுப்பு 51A(d) மற்றும் கட்டாயத் தேசிய சேவை பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. உறுப்பு 51A(d) தேசத்தைப் பாதுகாக்கவும், தேவைப்படும் போது தேசியச் சேவை ஆற்றுவதற்கும் குடிமக்களுக்கு ஆணையிடுகிறது.\n2. உறுப்பு 23(2) எந்தச் சூழ்நிலையிலும் பொது நோக்கங்களுக்காகக் கட்டாயச் சேவையை விதிக்க அரசைத் தடை செய்கிறது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 only", "ta": "1 மட்டுமே"},
            {"id": "B", "en": "2 only", "ta": "2 மட்டுமே"},
            {"id": "C", "en": "Both 1 and 2", "ta": "1 மற்றும் 2 இரண்டும்"},
            {"id": "D", "en": "Neither 1 nor 2", "ta": "1-ம் இல்லை 2-ம் இல்லை"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Statement 1 is CORRECT. Statement 2 is INCORRECT because Article 23(2) explicitly PERMITS the State to impose compulsory service for public purposes without discrimination.",
            "ta": "கூற்று 1 சரியானது. கூற்று 2 தவறு, ஏனெனில் உறுப்பு 23(2) பாகுபாடின்றி பொது நோக்கங்களுக்காகக் கட்டாயச் சேவையை விதிக்க அரசுக்கு வெளிப்படையாக அனுமதி அளிக்கிறது."
        },
        "why_not_others": {
            "A": {"en": "Correct. Statement 1 is true, while Statement 2 is false.", "ta": "சரி. கூற்று 1 உண்மை, கூற்று 2 தவறு."},
            "B": {"en": "Statement 2 is false.", "ta": "கூற்று 2 தவறானது."},
            "C": {"en": "Statement 2 is false.", "ta": "கூற்று 2 தவறானது."},
            "D": {"en": "Statement 1 is true.", "ta": "கூற்று 1 உண்மையாகும்."}
        },
        "tnpsc_tip": {
            "en": "Article 23(2) exception directly enables Article 51A(d) compulsory national service.",
            "ta": "உறுப்பு 23(2) விலக்கு உறுப்பு 51A(d) கட்டாயத் தேசிய சேவையை நேரடியாகச் சாத்தியமாக்குகிறது."
        }
    },
    {
        "id": "FD_S_007",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Statement",
        "question": {
            "en": "Consider the following statements regarding Article 51A(e):\n1. It commands promoting harmony and the spirit of common brotherhood amongst all the people of India.\n2. It requires transcending religious, linguistic, and regional or sectional diversities.\n3. It commands renouncing practices derogatory to the dignity of women.\nWhich of the statements given above are CORRECT?",
            "ta": "உறுப்பு 51A(e) பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. இது அனைத்து இந்திய மக்களிடையேயும் நல்லிணக்கத்தையும் சகோதரத்துவ உணர்வையும் ஊக்குவிக்க ஆணையிடுகிறது.\n2. இது மத, மொழி மற்றும் பிராந்திய அல்லது பிரிவு வேறுபாடுகளைக் கடந்து நிற்பதைக் கோருகிறது.\n3. இது பெண்களின் கண்ணியத்தைக் குறைக்கும் பழக்கங்களைக் கைவிட ஆணையிடுகிறது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 and 2 only", "ta": "1 மற்றும் 2 மட்டும்"},
            {"id": "B", "en": "2 and 3 only", "ta": "2 மற்றும் 3 மட்டும்"},
            {"id": "C", "en": "1 and 3 only", "ta": "1 மற்றும் 3 மட்டும்"},
            {"id": "D", "en": "1, 2 and 3", "ta": "1, 2 மற்றும் 3"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "All three statements are CORRECT. Article 51A(e) has two main limbs: (1) Promoting harmony and common brotherhood across diversities, and (2) Renouncing practices derogatory to women's dignity.",
            "ta": "மூன்று கூற்றுகளும் சரியானவை. உறுப்பு 51A(e) இரண்டு முக்கியப் பிரிவுகளைக் கொண்டுள்ளது: (1) வேறுபாடுகளைக் கடந்து நல்லிணக்கம் மற்றும் சகோதரத்துவத்தை ஊக்குவித்தல், மற்றும் (2) பெண்கள் கண்ணியத்தைக் குறைக்கும் பழக்கங்களைக் கைவிடுதல்."
        },
        "why_not_others": {
            "A": {"en": "Statement 3 is also correct.", "ta": "கூற்று 3-ம் சரியானது."},
            "B": {"en": "Statement 1 is also correct.", "ta": "கூற்று 1-ம் சரியானது."},
            "C": {"en": "Statement 2 is also correct.", "ta": "கூற்று 2-ம் சரியானது."},
            "D": {"en": "Correct. All statements 1, 2, and 3 are correct.", "ta": "சரி. 1, 2 மற்றும் 3 ஆகிய அனைத்துக் கூற்றுகளும் சரி."}
        },
        "tnpsc_tip": {
            "en": "Article 51A(e) explicitly protects women's dignity in addition to communal harmony.",
            "ta": "உறுப்பு 51A(e) சமூக நல்லிணக்கத்துடன் கூடுதலாகப் பெண்களின் கண்ணியத்தையும் வெளிப்படையாகப் பாதுகாக்கிறது."
        }
    },
    {
        "id": "FD_S_008",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Hard",
        "question_type": "Statement",
        "question": {
            "en": "Consider the following statements comparing Article 51A(f) and Articles 29-30:\n1. Article 51A(f) mandates ONLY minority communities to preserve India's composite culture.\n2. Articles 29 and 30 grant fundamental cultural and educational rights primarily to minority sections.\nWhich of the statements given above is/are CORRECT?",
            "ta": "உறுப்பு 51A(f) மற்றும் உறுப்புகள் 29-30 ஆகியவற்றை ஒப்பிடும் பின்வரும் கூற்றுகளைக் கருதுக:\n1. உறுப்பு 51A(f) சிறுபான்மைச் சமூகங்கள் மட்டுமே இந்தியாவின் கூட்டுப் பண்பாட்டைப் பேண ஆணையிடுகிறது.\n2. உறுப்புகள் 29 மற்றும் 30 முதன்மையாகச் சிறுபான்மைப் பிரிவினருக்கு அடிப்படை பண்பாட்டு மற்றும் கல்வி உரிமைகளை வழங்குகின்றன.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 only", "ta": "1 மட்டுமே"},
            {"id": "B", "en": "2 only", "ta": "2 மட்டுமே"},
            {"id": "C", "en": "Both 1 and 2", "ta": "1 மற்றும் 2 இரண்டும்"},
            {"id": "D", "en": "Neither 1 nor 2", "ta": "1-ம் இல்லை 2-ம் இல்லை"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "Statement 2 is CORRECT. Statement 1 is INCORRECT because Article 51A(f) binds ALL citizens of India, not just minority communities.",
            "ta": "கூற்று 2 சரியானது. கூற்று 1 தவறு, ஏனெனில் உறுப்பு 51A(f) சிறுபான்மையினரை மட்டுமே இன்றி இந்தியாவின் அனைத்துக் குடிமக்களையும் கட்டுப்படுத்துகிறது."
        },
        "why_not_others": {
            "A": {"en": "Statement 1 is false.", "ta": "கூற்று 1 தவறானது."},
            "B": {"en": "Correct. Statement 2 is true, while Statement 1 is false.", "ta": "சரி. கூற்று 2 உண்மை, கூற்று 1 தவறு."},
            "C": {"en": "Statement 1 is false.", "ta": "கூற்று 1 தவறானது."},
            "D": {"en": "Statement 2 is true.", "ta": "கூற்று 2 உண்மையாகும்."}
        },
        "tnpsc_tip": {
            "en": "Article 51A(f) uses the term 'composite culture' (சம்பிரதாய / கூட்டுப் பண்பாடு).",
            "ta": "உறுப்பு 51A(f) 'கூட்டுப் பண்பாடு' என்ற வார்த்தையைப் பயன்படுத்துகிறது."
        }
    },
    {
        "id": "FD_S_009",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Statement",
        "question": {
            "en": "Consider the following statements regarding Article 51A(g):\n1. It commands citizens to protect and improve the natural environment.\n2. It explicitly lists four natural elements: forests, lakes, rivers, and wildlife.\n3. It commands citizens to have compassion for living creatures.\n4. It applies only to government officers in the Ministry of Environment.\nWhich of the statements given above are CORRECT?",
            "ta": "உறுப்பு 51A(g) பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. இது இயற்கை சுற்றுச்சூழலைப் பாதுகாத்து மேம்படுத்தக் குடிமக்களுக்கு ஆணையிடுகிறது.\n2. இது காடுகள், ஏரிகள், ஆறுகள், மற்றும் வனவிலங்குகள் ஆகிய நான்கு இயற்கை கூறுகளை வெளிப்படையாகப் பட்டியலிடுகிறது.\n3. இது உயிரினங்கள் மீது கருணை காட்டக் குடிமக்களுக்கு ஆணையிடுகிறது.\n4. இது சுற்றுச்சூழல் அமைச்சகத்தில் உள்ள அரசு அதிகாரிகளுக்கு மட்டுமே பொருந்தும்.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1, 2 and 3 only", "ta": "1, 2 மற்றும் 3 மட்டும்"},
            {"id": "B", "en": "1 and 4 only", "ta": "1 மற்றும் 4 மட்டும்"},
            {"id": "C", "en": "2, 3 and 4 only", "ta": "2, 3 மற்றும் 4 மட்டும்"},
            {"id": "D", "en": "1, 2, 3 and 4", "ta": "1, 2, 3 மற்றும் 4"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Statements 1, 2, and 3 are CORRECT. Statement 4 is INCORRECT because Article 51A(g) applies to EVERY citizen of India.",
            "ta": "கூற்றுகள் 1, 2, மற்றும் 3 சரியானவை. கூற்று 4 தவறு, ஏனெனில் உறுப்பு 51A(g) இந்தியாவின் ஒவ்வொரு குடிமகனுக்கும் பொருந்தும்."
        },
        "why_not_others": {
            "A": {"en": "Correct. Statements 1, 2, and 3 are true, while Statement 4 is false.", "ta": "சரி. கூற்றுகள் 1, 2, மற்றும் 3 உண்மை, கூற்று 4 தவறு."},
            "B": {"en": "Statement 4 is false.", "ta": "கூற்று 4 தவறானது."},
            "C": {"en": "Statement 4 is false.", "ta": "கூற்று 4 தவறானது."},
            "D": {"en": "Statement 4 is false.", "ta": "கூற்று 4 தவறானது."}
        },
        "tnpsc_tip": {
            "en": "Remember the 4 elements in Art 51A(g): Forests, Lakes, Rivers, Wildlife.",
            "ta": "உறுப்பு 51A(g)-ல் உள்ள 4 கூறுகளை நினைவில் கொள்க: காடுகள், ஏரிகள், ஆறுகள், வனவிலங்குகள்."
        }
    },
    {
        "id": "FD_S_010",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Statement",
        "question": {
            "en": "Consider the following statements regarding Article 51A(h):\n1. It commands developing scientific temper.\n2. It commands developing humanism.\n3. It commands developing the spirit of inquiry and reform.\nWhich of the statements given above are CORRECT?",
            "ta": "உறுப்பு 51A(h) பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. இது அறிவியல் மனப்பான்மையை வளர்க்க ஆணையிடுகிறது.\n2. இது மனிதநேயத்தை வளர்க்க ஆணையிடுகிறது.\n3. இது ஆராய்ச்சி மற்றும் சீர்திருத்த உணர்வை வளர்க்க ஆணையிடுகிறது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 and 2 only", "ta": "1 மற்றும் 2 மட்டும்"},
            {"id": "B", "en": "2 and 3 only", "ta": "2 மற்றும் 3 மட்டும்"},
            {"id": "C", "en": "1 and 3 only", "ta": "1 மற்றும் 3 மட்டும்"},
            {"id": "D", "en": "1, 2 and 3", "ta": "1, 2 மற்றும் 3"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "All three statements are CORRECT. Article 51A(h) contains 4 core values: Scientific temper, Humanism, Spirit of inquiry, and Spirit of reform.",
            "ta": "மூன்று கூற்றுகளும் சரியானவை. உறுப்பு 51A(h) 4 முக்கிய மதிப்புகளைக் கொண்டுள்ளது: அறிவியல் மனப்பான்மை, மனிதநேயம், ஆராய்ச்சி உணர்வு, மற்றும் சீர்திருத்த உணர்வு."
        },
        "why_not_others": {
            "A": {"en": "Statement 3 is also correct.", "ta": "கூற்று 3-ம் சரியானது."},
            "B": {"en": "Statement 1 is also correct.", "ta": "கூற்று 1-ம் சரியானது."},
            "C": {"en": "Statement 2 is also correct.", "ta": "கூற்று 2-ம் சரியானது."},
            "D": {"en": "Correct. All statements 1, 2, and 3 are correct.", "ta": "சரி. 1, 2 மற்றும் 3 ஆகிய அனைத்துக் கூற்றுகளும் சரி."}
        },
        "tnpsc_tip": {
            "en": "Art 51A(h) formula: Scientific Temper + Humanism + Inquiry + Reform.",
            "ta": "உறுப்பு 51A(h) வாய்ப்பாடு: அறிவியல் மனப்பான்மை + மனிதநேயம் + ஆராய்ச்சி + சீர்திருத்தம்."
        }
    },
    {
        "id": "FD_S_011",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Statement",
        "question": {
            "en": "Consider the following statements regarding Article 51A(i):\n1. It commands citizens to safeguard public property.\n2. It commands citizens to abjure violence.\n3. The Prevention of Damage to Public Property Act, 1984 gives statutory backing to this duty.\nWhich of the statements given above are CORRECT?",
            "ta": "உறுப்பு 51A(i) பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. இது பொதுச் சொத்தைப் பாதுகாக்கக் குடிமக்களுக்கு ஆணையிடுகிறது.\n2. இது வன்முறையைக் கைவிடக் குடிமக்களுக்கு ஆணையிடுகிறது.\n3. 1984-ன் பொதுச் சொத்துச் சேதத் தடுப்புச் சட்டம் இக்கடமைக்குச் சட்டப்பூர்வ ஆதரவை வழங்குகிறது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 and 2 only", "ta": "1 மற்றும் 2 மட்டும்"},
            {"id": "B", "en": "2 and 3 only", "ta": "2 மற்றும் 3 மட்டும்"},
            {"id": "C", "en": "1 and 3 only", "ta": "1 மற்றும் 3 மட்டும்"},
            {"id": "D", "en": "1, 2 and 3", "ta": "1, 2 மற்றும் 3"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "All three statements are CORRECT. Art 51A(i) covers public property protection and non-violence, supported statutorily by PDPP Act 1984.",
            "ta": "மூன்று கூற்றுகளும் சரியானவை. உறுப்பு 51A(i) பொதுச் சொத்து பாதுகாப்பு மற்றும் வன்முறை இன்மையை உள்ளடக்கியது, PDPP சட்டம் 1984 மூலம் சட்டப்பூர்வமாக ஆதரிக்கப்படுகிறது."
        },
        "why_not_others": {
            "A": {"en": "Statement 3 is also correct.", "ta": "கூற்று 3-ம் சரியானது."},
            "B": {"en": "Statement 1 is also correct.", "ta": "கூற்று 1-ம் சரியானது."},
            "C": {"en": "Statement 2 is also correct.", "ta": "கூற்று 2-ம் சரியானது."},
            "D": {"en": "Correct. All statements 1, 2, and 3 are correct.", "ta": "சரி. 1, 2 மற்றும் 3 ஆகிய அனைத்துக் கூற்றுகளும் சரி."}
        },
        "tnpsc_tip": {
            "en": "Article 51A(i) combines safeguarding public property AND abjuring violence.",
            "ta": "உறுப்பு 51A(i) பொதுச் சொத்தைப் பாதுகாத்தல் மற்றும் வன்முறையைக் கைவிடுதல் ஆகிய இரண்டையும் இணைக்கிறது."
        }
    },
    {
        "id": "FD_S_012",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Statement",
        "question": {
            "en": "Consider the following statements regarding Article 51A(j):\n1. It commands striving towards excellence in all spheres of individual and collective activity.\n2. Its objective is ensuring that the nation constantly rises to higher levels of endeavor and achievement.\nWhich of the statements given above is/are CORRECT?",
            "ta": "உறுப்பு 51A(j) பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. இது தனிநபர் மற்றும் கூட்டுச் செயல்பாடுகளின் அனைத்துத் துறைகளிலும் சிறப்பினை நோக்கி முயலுமாறு ஆணையிடுகிறது.\n2. தேசம் தொடர்ச்சியாக முயல்வு மற்றும் சாதனைகளின் உயர் மட்டங்களுக்கு உயர்வதை உறுதி செய்வதே இதன் நோக்கமாகும்.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 only", "ta": "1 மட்டுமே"},
            {"id": "B", "en": "2 only", "ta": "2 மட்டுமே"},
            {"id": "C", "en": "Both 1 and 2", "ta": "1 மற்றும் 2 இரண்டும்"},
            {"id": "D", "en": "Neither 1 nor 2", "ta": "1-ம் இல்லை 2-ம் இல்லை"}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "Both statements 1 and 2 are CORRECT. Article 51A(j) targets excellence in both individual and collective domains to drive national progress.",
            "ta": "கூற்றுகள் 1 மற்றும் 2 இரண்டும் சரியானவை. உறுப்பு 51A(j) தேசிய வளர்ச்சியை உந்தத் தனிநபர் மற்றும் கூட்டு களங்கள் இரண்டிலும் சிறப்பை இலக்காகக் கொள்கிறது."
        },
        "why_not_others": {
            "A": {"en": "Statement 2 is also correct.", "ta": "கூற்று 2-ம் சரியானது."},
            "B": {"en": "Statement 1 is also correct.", "ta": "கூற்று 1-ம் சரியானது."},
            "C": {"en": "Correct. Both statements 1 and 2 are correct.", "ta": "சரி. கூற்றுகள் 1 மற்றும் 2 இரண்டும் சரியானவை."},
            "D": {"en": "Both statements are true.", "ta": "இரண்டு கூற்றுகளும் உண்மை."}
        },
        "tnpsc_tip": {
            "en": "Article 51A(j) covers BOTH 'individual' and 'collective' activity.",
            "ta": "உறுப்பு 51A(j) 'தனிநபர்' மற்றும் 'கூட்டு' செயல்பாடுகள் இரண்டையும் உள்ளடக்கியது."
        }
    },
    {
        "id": "FD_S_013",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Hard",
        "question_type": "Statement",
        "question": {
            "en": "Consider the following statements regarding the Educational Triad created by the 86th Constitutional Amendment Act, 2002:\n1. Article 21A created a Fundamental Right of the child against the State for 6 to 14 years.\n2. Article 45 DPSP directs the State to provide early childhood care and education for children below 6 years.\n3. Article 51A(k) created a Fundamental Duty of parents/guardians for children aged 6 to 14 years.\nWhich of the statements given above are CORRECT?",
            "ta": "2002-ன் 86வது அரசியலமைப்பு திருத்தச் சட்டத்தால் உருவாக்கப்பட்ட கல்விக் முக்கோணம் பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. உறுப்பு 21A 6 முதல் 14 வயதுக் குழந்தைகளுக்கு அரசுக்கு எதிராக அடிப்படை உரிமையை உருவாக்கியது.\n2. உறுப்பு 45 DPSP 6 வயதிற்குட்பட்ட குழந்தைகளுக்கு முன்பருவப் பராமரிப்பு மற்றும் கல்வியை வழங்க அரசுக்கு வழிகாட்டுகிறது.\n3. உறுப்பு 51A(k) 6 முதல் 14 வயது வரையிலான குழந்தைகளுக்குப் பெற்றோர்/பாதுகாவலர்களின் அடிப்படை கடமையை உருவாக்கியது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 and 2 only", "ta": "1 மற்றும் 2 மட்டும்"},
            {"id": "B", "en": "2 and 3 only", "ta": "2 மற்றும் 3 மட்டும்"},
            {"id": "C", "en": "1 and 3 only", "ta": "1 மற்றும் 3 மட்டும்"},
            {"id": "D", "en": "1, 2 and 3", "ta": "1, 2 மற்றும் 3"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "All three statements are CORRECT. The 86th CAA 2002 amended Part III (Art 21A), Part IV (Art 45), and Part IVA (Art 51A(k)) simultaneously.",
            "ta": "மூன்று கூற்றுகளும் சரியானவை. 86வது திருத்தச் சட்டம் 2002 ஒரே நேரத்தில் பகுதி III (உறுப்பு 21A), பகுதி IV (உறுப்பு 45), மற்றும் பகுதி IVA (உறுப்பு 51A(k)) ஆகியவற்றைத் திருத்தியது."
        },
        "why_not_others": {
            "A": {"en": "Statement 3 is also correct.", "ta": "கூற்று 3-ம் சரியானது."},
            "B": {"en": "Statement 1 is also correct.", "ta": "கூற்று 1-ம் சரியானது."},
            "C": {"en": "Statement 2 is also correct.", "ta": "கூற்று 2-ம் சரியானது."},
            "D": {"en": "Correct. All statements 1, 2, and 3 are correct.", "ta": "சரி. 1, 2 மற்றும் 3 ஆகிய அனைத்துக் கூற்றுகளும் சரி."}
        },
        "tnpsc_tip": {
            "en": "Age breakdown: Art 21A (6-14 yrs) | Art 45 (<6 yrs) | Art 51A(k) (6-14 yrs).",
            "ta": "வயதுப் பிரிவு: உறுப்பு 21A (6-14 வயது) | உறுப்பு 45 (<6 வயது) | உறுப்பு 51A(k) (6-14 வயது)."
        }
    },
    {
        "id": "FD_S_014",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Hard",
        "question_type": "Statement",
        "question": {
            "en": "Consider the following statements regarding the Justice J.S. Verma Committee (1999):\n1. It was appointed to operationalize teaching of Fundamental Duties in educational institutions.\n2. It identified existing parliamentary penal laws that enforce various Fundamental Duties.\n3. It identified the Representation of the People Act 1951, Protection of Civil Rights Act 1955, and IPC as duty-enforcing statutes.\n4. It recommended declaring all Fundamental Duties directly justiciable by High Court writs.\nWhich of the statements given above are CORRECT?",
            "ta": "நீதிபதி ஜே.எஸ். வர்மா குழு (1999) பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. கல்வி நிறுவனங்களில் அடிப்படை கடமைகளைக் கற்பிப்பதை நடைமுறைப்படுத்த இது நியமிக்கப்பட்டது.\n2. பல்வேறு அடிப்படை கடமைகளை அமல்படுத்தும் நிலவும் நாடாளுமன்றக் குற்றவியல் சட்டங்களை இது கண்டறிந்தது.\n3. மக்கள் பிரதிநிதித்துவச் சட்டம் 1951, சிவில் உரிமைகள் பாதுகாப்புச் சட்டம் 1955, மற்றும் IPC ஆகியவற்றை கடமையை அமல்படுத்தும் சட்டங்களாக இது கண்டறிந்தது.\n4. அனைத்து அடிப்படை கடமைகளையும் உயர் நீதிமன்ற பேராணைகள் மூலம் நேரடியாக அமல்படுத்தக்கூடியதாக அறிவிக்க இது பரிந்துரைத்தது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1, 2 and 3 only", "ta": "1, 2 மற்றும் 3 மட்டும்"},
            {"id": "B", "en": "1 and 4 only", "ta": "1 மற்றும் 4 மட்டும்"},
            {"id": "C", "en": "2, 3 and 4 only", "ta": "2, 3 மற்றும் 4 மட்டும்"},
            {"id": "D", "en": "1, 2, 3 and 4", "ta": "1, 2, 3 மற்றும் 4"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Statements 1, 2, and 3 are CORRECT. Statement 4 is INCORRECT because the Verma Committee advocated statutory penal enforcement and educational pedagogy, NOT direct writ justiciability.",
            "ta": "கூற்றுகள் 1, 2, மற்றும் 3 சரியானவை. கூற்று 4 தவறு, ஏனெனில் வர்மா குழு சட்டப்பூர்வ அமலாக்கம் மற்றும் கல்வியையே வலியுறுத்தியது, நேரடி பேராணை அமலாக்கத்தை அல்ல."
        },
        "why_not_others": {
            "A": {"en": "Correct. Statements 1, 2, and 3 are true, while Statement 4 is false.", "ta": "சரி. கூற்றுகள் 1, 2, மற்றும் 3 உண்மை, கூற்று 4 தவறு."},
            "B": {"en": "Statement 4 is false.", "ta": "கூற்று 4 தவறானது."},
            "C": {"en": "Statement 4 is false.", "ta": "கூற்று 4 தவறானது."},
            "D": {"en": "Statement 4 is false.", "ta": "கூற்று 4 தவறானது."}
        },
        "tnpsc_tip": {
            "en": "Verma Committee (1999) focused on non-statutory awareness + existing statutory penal provisions.",
            "ta": "வர்மா குழு (1999) சட்டப்பூர்வமற்ற விழிப்புணர்வு + நிலவும் சட்டப்பூர்வ குற்றவியல் விதிகள் மீது கவனம் செலுத்தியது."
        }
    },
    {
        "id": "FD_S_015",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Hard",
        "question_type": "Assertion & Reason",
        "question": {
            "en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Fundamental Duties under Article 51A are non-justiciable in courts by themselves.\nReason (R): The Constitution does not provide for direct enforcement of Fundamental Duties through writs without specific enabling legislation passed by Parliament.\nIn the context of the above statements, which one of the following is correct?",
            "ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): உறுப்பு 51A-ன் கீழ் உள்ள அடிப்படை கடமைகள் நீதிமன்றங்களில் தாமாகவே அமல்படுத்த முடியாதவை ஆகும்.\nகாரணம் (R): நாடாளுமன்றத்தால் நிறைவேற்றப்படும் குறிப்பிட்ட சட்டமின்றி பேராணைகள் மூலம் அடிப்படை கடமைகளை நேரடியாக அமல்படுத்த அரசியலமைப்பு வழிவகை செய்யவில்லை.\nமேற்கண்ட கூற்றுகளின் அடிப்படையில் பின்வருவனவற்றில் எது சரியானது?"
        },
        "options": [
            {"id": "A", "en": "Both A and R are correct and R is the correct explanation of A", "ta": "A மற்றும் R ஆகிய இரண்டும் சரி, மேலும் R என்பது A-வின் சரியான விளக்கமாகும்"},
            {"id": "B", "en": "Both A and R are correct but R is NOT the correct explanation of A", "ta": "A மற்றும் R ஆகிய இரண்டும் சரி, ஆனால் R என்பது A-வின் சரியான விளக்கம் அல்ல"},
            {"id": "C", "en": "A is correct but R is incorrect", "ta": "A சரி ஆனால் R தவறு"},
            {"id": "D", "en": "A is incorrect but R is correct", "ta": "A தவறு ஆனால் R சரி"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Both A and R are true. Reason R accurately explains Assertion A: duties cannot be enforced directly via writs unless Parliament passes specific penal/statutory laws.",
            "ta": "A மற்றும் R ஆகிய இரண்டும் உண்மை. காரணம் R சரியாகக் கூற்று A-வை விளக்குகிறது: நாடாளுமன்றம் குறிப்பிட்ட சட்டங்களை நிறைவேற்றினாலன்றி கடமைகளைப் பேராணைகள் மூலம் நேரடியாக அமல்படுத்த முடியாது."
        },
        "why_not_others": {
            "A": {"en": "Correct. R directly explains why duties are non-justiciable by themselves.", "ta": "சரி. ஏன் கடமைகள் தாமாகவே அமல்படுத்த முடியாதவை என்பதை R நேரடியாக விளக்குகிறது."},
            "B": {"en": "R is the direct explanation of A.", "ta": "R என்பது A-விற்கான நேரடி விளக்கமாகும்."},
            "C": {"en": "R is true.", "ta": "R உண்மையாகும்."},
            "D": {"en": "A is true.", "ta": "A உண்மையாகும்."}
        },
        "tnpsc_tip": {
            "en": "Non-justiciable = No direct writ remedy without parliamentary enabling statute.",
            "ta": "அமல்படுத்த முடியாதவை = நாடாளுமன்றச் சட்டமின்றி நேரடி பேராணைப் பரிகாரம் இல்லை."
        }
    },
    {
        "id": "FD_S_016",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Statement",
        "question": {
            "en": "Consider the following statements regarding the applicability of Article 51A:\n1. Article 51A applies exclusively to citizens of India.\n2. Non-citizens living in India are constitutionally bound by Article 51A.\nWhich of the statements given above is/are CORRECT?",
            "ta": "உறுப்பு 51A-ன் பயன்பாடு பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. உறுப்பு 51A இந்தியக் குடிமக்களுக்கு மட்டுமே பொருந்தும்.\n2. இந்தியாவில் வாழும் குடிமக்கள் அல்லாதோர் அரசியலமைப்பு ரீதியாக உறுப்பு 51A-வால் கட்டுப்படுத்தப்படுகிறார்கள்.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 only", "ta": "1 மட்டுமே"},
            {"id": "B", "en": "2 only", "ta": "2 மட்டுமே"},
            {"id": "C", "en": "Both 1 and 2", "ta": "1 மற்றும் 2 இரண்டும்"},
            {"id": "D", "en": "Neither 1 nor 2", "ta": "1-ம் இல்லை 2-ம் இல்லை"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Statement 1 is CORRECT. Statement 2 is INCORRECT because Article 51A opens with 'It shall be the duty of every citizen of India', excluding non-citizens.",
            "ta": "கூற்று 1 சரியானது. கூற்று 2 தவறு, ஏனெனில் உறுப்பு 51A 'இந்தியாவின் ஒவ்வொரு குடிமகனின் கடமையாகும்' எனத் தொடங்குவதால் குடிமக்கள் அல்லாதோரை விலக்குகிறது."
        },
        "why_not_others": {
            "A": {"en": "Correct. Statement 1 is true, while Statement 2 is false.", "ta": "சரி. கூற்று 1 உண்மை, கூற்று 2 தவறு."},
            "B": {"en": "Statement 2 is false.", "ta": "கூற்று 2 தவறானது."},
            "C": {"en": "Statement 2 is false.", "ta": "கூற்று 2 தவறானது."},
            "D": {"en": "Statement 1 is true.", "ta": "கூற்று 1 உண்மையாகும்."}
        },
        "tnpsc_tip": {
            "en": "Fundamental Rights: Some to all persons, some to citizens only | Fundamental Duties: ONLY to citizens.",
            "ta": "அடிப்படை உரிமைகள்: சில அனைவருக்கும், சில குடிமக்களுக்கு மட்டுமே | அடிப்படை கடமைகள்: குடிமக்களுக்கு மட்டுமே."
        }
    },
    {
        "id": "FD_S_017",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Hard",
        "question_type": "Statement",
        "question": {
            "en": "Consider the following statements regarding Bijoe Emmanuel v. State of Kerala (1986):\n1. Jehovah's Witnesses students were expelled for refusing to stand up during school assembly.\n2. The Supreme Court held that standing up respectfully without singing does NOT show disrespect to the National Anthem.\nWhich of the statements given above is/are CORRECT?",
            "ta": "பிஜோய் இம்மானுவேல் vs கேரளா மாநிலம் (1986) பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. பள்ளி வழிபாட்டின் போது நிற்க மறுத்ததற்காக யெகோவாவின் சாட்சிகள் மாணவர்கள் நீக்கப்பட்டனர்.\n2. பாடாமல் மரியாதையுடன் எழுந்து நிற்பது தேசியக் கீதத்திற்கு அவமரியாதையைக் காட்டாது என உச்ச நீதிமன்றம் தீர்ப்பளித்தது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 only", "ta": "1 மட்டுமே"},
            {"id": "B", "en": "2 only", "ta": "2 மட்டுமே"},
            {"id": "C", "en": "Both 1 and 2", "ta": "1 மற்றும் 2 இரண்டும்"},
            {"id": "D", "en": "Neither 1 nor 2", "ta": "1-ம் இல்லை 2-ம் இல்லை"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "Statement 2 is CORRECT. Statement 1 is INCORRECT because the students DID stand up respectfully; they only refused to sing.",
            "ta": "கூற்று 2 சரியானது. கூற்று 1 தவறு, ஏனெனில் மாணவர்கள் மரியாதையுடன் எழுந்து நின்றனர்; பாட மட்டுமே மறுத்தனர்."
        },
        "why_not_others": {
            "A": {"en": "Statement 1 is false.", "ta": "கூற்று 1 தவறானது."},
            "B": {"en": "Correct. Statement 2 is true, while Statement 1 is false.", "ta": "சரி. கூற்று 2 உண்மை, கூற்று 1 தவறு."},
            "C": {"en": "Statement 1 is false.", "ta": "கூற்று 1 தவறானது."},
            "D": {"en": "Statement 2 is true.", "ta": "கூற்று 2 உண்மையாகும்."}
        },
        "tnpsc_tip": {
            "en": "Bijoe Emmanuel 1986: Standing respectfully satisfies Art 51A(a); compulsory singing violates Art 19(1)(a) and Art 25.",
            "ta": "பிஜோய் இம்மானுவேல் 1986: மரியாதையுடன் நிற்பது உறுப்பு 51A(a)-ஐப் பூர்த்தி செய்கிறது; கட்டாயமாகப் பாடுவது உறுப்பு 19(1)(a) மற்றும் 25-ஐ மீறுகிறது."
        }
    },
    {
        "id": "FD_H_018",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Hard",
        "question_type": "Statement",
        "question": {
            "en": "Consider the following statements regarding Shyam Narayan Chouksey v. Union of India (2018):\n1. The Supreme Court made playing the National Anthem in cinema halls mandatory in all circumstances.\n2. The Court affirmed that whenever National Anthem is played, citizens must show proper respect under Article 51A(a).\nWhich of the statements given above is/are CORRECT?",
            "ta": "ஷ்யாம் நாராயண் சௌக்சே vs இந்திய யூனியன் (2018) பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. உச்ச நீதிமன்றம் திரையரங்குகளில் தேசியக் கீதத்தை இசைப்பதை அனைத்துச் சூழ்நிலைகளிலும் கட்டாயமாக்கியது.\n2. தேசியக் கீதம் இசைக்கப்படும் போதெல்லாம், குடிமக்கள் உறுப்பு 51A(a)-ன் கீழ் தகுந்த மரியாதை செலுத்த வேண்டும் என்பதை நீதிமன்றம் உறுதிப்படுத்தியது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 only", "ta": "1 மட்டுமே"},
            {"id": "B", "en": "2 only", "ta": "2 மட்டுமே"},
            {"id": "C", "en": "Both 1 and 2", "ta": "1 மற்றும் 2 இரண்டும்"},
            {"id": "D", "en": "Neither 1 nor 2", "ta": "1-ம் இல்லை 2-ம் இல்லை"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "Statement 2 is CORRECT. Statement 1 is INCORRECT because in 2018 SC modified its earlier interim order and made playing the anthem optional/discretionary.",
            "ta": "கூற்று 2 சரியானது. கூற்று 1 தவறு, ஏனெனில் 2018-ல் உச்ச நீதிமன்றம் தனது முந்தைய இடைக்கால உத்தரவை மாற்றி கீதத்தை இசைப்பதைத் விருப்பத்தேர்வாக்கியது."
        },
        "why_not_others": {
            "A": {"en": "Statement 1 is false.", "ta": "கூற்று 1 தவறானது."},
            "B": {"en": "Correct. Statement 2 is true, while Statement 1 is false.", "ta": "சரி. கூற்று 2 உண்மை, கூற்று 1 தவறு."},
            "C": {"en": "Statement 1 is false.", "ta": "கூற்று 1 தவறானது."},
            "D": {"en": "Statement 2 is true.", "ta": "கூற்று 2 உண்மையாகும்."}
        },
        "tnpsc_tip": {
            "en": "Cinema playing: Optional | Respect if played: Mandatory under Art 51A(a).",
            "ta": "திரையரங்க இசைப்பு: விருப்பத்தேர்வு | இசைக்கப்பட்டால் மரியாதை: உறுப்பு 51A(a)-ன் கீழ் கட்டாயம்."
        }
    },
    {
        "id": "FD_S_019",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Hard",
        "question_type": "Statement",
        "question": {
            "en": "Consider the following statements regarding Environmental Protection litigation in Supreme Court:\n1. Article 21 guarantees the Fundamental Right to a wholesome environment.\n2. Article 48A directs State policy to protect and improve the environment.\n3. Article 51A(g) mandates citizen duty to protect environment and show compassion for living creatures.\nWhich of the statements given above are CORRECT?",
            "ta": "உச்ச நீதிமன்றத்தில் சுற்றுச்சூழல் பாதுகாப்பு வழக்குகள் பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. உறுப்பு 21 ஆரோக்கியமான சுற்றுச்சூழலுக்கான அடிப்படை உரிமையை உத்தரவாதம் செய்கிறது.\n2. உறுப்பு 48A சுற்றுச்சூழலைப் பாதுகாத்து மேம்படுத்த அரசுக் கொள்கைக்கு வழிகாட்டுகிறது.\n3. உறுப்பு 51A(g) சுற்றுச்சூழலைப் பாதுகாக்கவும் உயிரினங்கள் மீது கருணை காட்டவும் குடிமகன் கடமையை ஆணையிடுகிறது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 and 2 only", "ta": "1 மற்றும் 2 மட்டும்"},
            {"id": "B", "en": "2 and 3 only", "ta": "2 மற்றும் 3 மட்டும்"},
            {"id": "C", "en": "1 and 3 only", "ta": "1 மற்றும் 3 மட்டும்"},
            {"id": "D", "en": "1, 2 and 3", "ta": "1, 2 மற்றும் 3"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "All three statements are CORRECT. The SC repeatedly holds that Arts 21, 48A, and 51A(g) form the Environmental Law Triangle of the Constitution.",
            "ta": "மூன்று கூற்றுகளும் சரியானவை. உறுப்புகள் 21, 48A, மற்றும் 51A(g) ஆகியவை அரசியலமைப்பின் சுற்றுச்சூழல் சட்ட முக்கோணத்தை உருவாக்குகின்றன என உச்ச நீதிமன்றம் மீண்டும் மீண்டும் கூறுகிறது."
        },
        "why_not_others": {
            "A": {"en": "Statement 3 is also correct.", "ta": "கூற்று 3-ம் சரியானது."},
            "B": {"en": "Statement 1 is also correct.", "ta": "கூற்று 1-ம் சரியானது."},
            "C": {"en": "Statement 2 is also correct.", "ta": "கூற்று 2-ம் சரியானது."},
            "D": {"en": "Correct. All statements 1, 2, and 3 are correct.", "ta": "சரி. 1, 2 மற்றும் 3 ஆகிய அனைத்துக் கூற்றுகளும் சரி."}
        },
        "tnpsc_tip": {
            "en": "Environmental Triad: Art 21 (FR) <-> Art 48A (DPSP) <-> Art 51A(g) (FD).",
            "ta": "சுற்றுச்சூழல் முக்கோணம்: உறுப்பு 21 (FR) <-> உறுப்பு 48A (DPSP) <-> உறுப்பு 51A(g) (FD)."
        }
    },
    {
        "id": "FD_S_020",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Hard",
        "question_type": "Assertion & Reason",
        "question": {
            "en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): In Animal Welfare Board of India v. A. Nagaraja (2014), the Supreme Court struck down traditional bull-taming sports like Jallikattu.\nReason (R): The Court held that animal cruelty violates Article 21 right to life of animals read with citizen duty of compassion under Article 51A(g).\nIn the context of the above statements, which one of the following is correct?",
            "ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): இந்திய விலங்கு நல வாரியம் vs ஏ. நாகராஜா (2014) வழக்கில், ஜல்லிக்கட்டு போன்ற பாரம்பரிய எருது தழுவுதல் விளையாட்டுக்களை உச்ச நீதிமன்றம் தடை செய்தது.\nகாரணம் (R): உறுப்பு 51A(g)-ன் கீழ் உள்ள குடிமகனின் கருணைக் கடமையுடன் இணைத்துப் படிக்கப்படும் உறுப்பு 21 விலங்குகளின் வாழும் உரிமையை விலங்கு கொடுமை மீறுகிறது என நீதிமன்றம் கருதியது.\nமேற்கண்ட கூற்றுகளின் அடிப்படையில் பின்வருவனவற்றில் எது சரியானது?"
        },
        "options": [
            {"id": "A", "en": "Both A and R are correct and R is the correct explanation of A", "ta": "A மற்றும் R ஆகிய இரண்டும் சரி, மேலும் R என்பது A-வின் சரியான விளக்கமாகும்"},
            {"id": "B", "en": "Both A and R are correct but R is NOT the correct explanation of A", "ta": "A மற்றும் R ஆகிய இரண்டும் சரி, ஆனால் R என்பது A-வின் சரியான விளக்கம் அல்ல"},
            {"id": "C", "en": "A is correct but R is incorrect", "ta": "A சரி ஆனால் R தவறு"},
            {"id": "D", "en": "A is incorrect but R is correct", "ta": "A தவறு ஆனால் R சரி"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Both A and R are true. In A. Nagaraja (2014), SC relied on Art 51A(g) compassion duty and Art 21 to strike down Jallikattu (before state legislative amendment in 2017).",
            "ta": "A மற்றும் R ஆகிய இரண்டும் உண்மை. ஏ. நாகராஜா (2014) வழக்கில், உறுப்பு 51A(g) கருணைக் கடமை மற்றும் உறுப்பு 21-ஐச் சார்ந்து உச்ச நீதிமன்றம் ஜல்லிக்கட்டைத் தடை செய்தது (2017 மாநிலச் சட்டமன்றத் திருத்தத்திற்கு முன்)."
        },
        "why_not_others": {
            "A": {"en": "Correct. R directly explains why SC banned Jallikattu in 2014.", "ta": "சரி. 2014-ல் ஏன் உச்ச நீதிமன்றம் ஜல்லிக்கட்டைத் தடை செய்தது என்பதை R நேரடியாக விளக்குகிறது."},
            "B": {"en": "R is the direct explanation of A.", "ta": "R என்பது A-விற்கான நேரடி விளக்கமாகும்."},
            "C": {"en": "R is true.", "ta": "R உண்மையாகும்."},
            "D": {"en": "A is true.", "ta": "A உண்மையாகும்."}
        },
        "tnpsc_tip": {
            "en": "A. Nagaraja 2014 integrated animal rights into Article 21 using Article 51A(g).",
            "ta": "ஏ. நாகராஜா 2014 வழக்கு உறுப்பு 51A(g)-ஐப் பயன்படுத்தி உறுப்பு 21-ல் விலங்கு உரிமைகளை ஒருங்கிணைத்தது."
        }
    },
    {
        "id": "FD_S_021",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Hard",
        "question_type": "Statement",
        "question": {
            "en": "Consider the following statements regarding AIIMS Students Union v. AIIMS (2002):\n1. The Supreme Court upheld 100% institute candidate reservation in post-graduate medical courses.\n2. The Court placed heavy reliance on Article 51A(j) to hold that merit and excellence cannot be completely obliterated under reservation policies.\nWhich of the statements given above is/are CORRECT?",
            "ta": "AIIMS மாணவர் சங்கம் vs AIIMS (2002) பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. முதுகலை மருத்துவப் படிப்புகளில் 100% நிறுவன இடஒதுக்கீட்டை உச்ச நீதிமன்றம் நிலைநிறுத்தியது.\n2. இடஒதுக்கீட்டுக் கொள்கைகளின் கீழ் தகுதியையும் சிறப்பையும் முற்றிலுமாக அழிக்க முடியாது எனத் தீர்ப்பளிக்க உறுப்பு 51A(j)-ஐ நீதிமன்றம் பெரிதும் சார்ந்திருந்தது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 only", "ta": "1 மட்டுமே"},
            {"id": "B", "en": "2 only", "ta": "2 மட்டுமே"},
            {"id": "C", "en": "Both 1 and 2", "ta": "1 மற்றும் 2 இரண்டும்"},
            {"id": "D", "en": "Neither 1 nor 2", "ta": "1-ம் இல்லை 2-ம் இல்லை"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "Statement 2 is CORRECT. Statement 1 is INCORRECT because the Supreme Court STRUCK DOWN excessive institutional reservation as violative of merit under Art 51A(j).",
            "ta": "கூற்று 2 சரியானது. கூற்று 1 தவறு, ஏனெனில் அதிகப்படியான நிறுவன இடஒதுக்கீட்டை உறுப்பு 51A(j)-ன் கீழ் தகுதியை மீறுவதாக உச்ச நீதிமன்றம் ரத்து செய்தது."
        },
        "why_not_others": {
            "A": {"en": "Statement 1 is false.", "ta": "கூற்று 1 தவறானது."},
            "B": {"en": "Correct. Statement 2 is true, while Statement 1 is false.", "ta": "சரி. கூற்று 2 உண்மை, கூற்று 1 தவறு."},
            "C": {"en": "Statement 1 is false.", "ta": "கூற்று 1 தவறானது."},
            "D": {"en": "Statement 2 is true.", "ta": "கூற்று 2 உண்மையாகும்."}
        },
        "tnpsc_tip": {
            "en": "AIIMS 2002 case established that Fundamental Duties can invalidate unconstitutional reservation quotas.",
            "ta": "AIIMS 2002 வழக்கு அடிப்படை கடமைகள் அரசியலமைப்பிற்கு எதிரான இடஒதுக்கீட்டுக் ஒதுக்கீடுகளை ரத்து செய்ய முடியும் என்பதை நிறுவியது."
        }
    },
    {
        "id": "FD_S_022",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Hard",
        "question_type": "Statement",
        "question": {
            "en": "Consider the following statements regarding Aruna Roy v. Union of India (2002):\n1. The NCFSE 2000 syllabus was struck down for teaching religious dogma.\n2. The Supreme Court upheld value education, relying on Article 51A(h) to rule that teaching moral values and scientific temper is consistent with secularism.\nWhich of the statements given above is/are CORRECT?",
            "ta": "அருணா ராய் vs இந்திய யூனியன் (2002) பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. மதக் கோட்பாடுகளைக் கற்பித்ததற்காக NCFSE 2000 பாடத்திட்டம் ரத்து செய்யப்பட்டது.\n2. தார்மீக மதிப்புகள் மற்றும் அறிவியல் மனப்பான்மையைக் கற்பிப்பது மதச்சார்பின்மைக்கு உடன்பாடானது எனத் தீர்ப்பளிக்க உறுப்பு 51A(h)-ஐச் சார்ந்து உச்ச நீதிமன்றம் மதிப்புக் கல்வியை நிலைநிறுத்தியது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 only", "ta": "1 மட்டுமே"},
            {"id": "B", "en": "2 only", "ta": "2 மட்டுமே"},
            {"id": "C", "en": "Both 1 and 2", "ta": "1 மற்றும் 2 இரண்டும்"},
            {"id": "D", "en": "Neither 1 nor 2", "ta": "1-ம் இல்லை 2-ம் இல்லை"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "Statement 2 is CORRECT. Statement 1 is INCORRECT because SC UPHELD the syllabus, ruling it was value education rather than religious instruction.",
            "ta": "கூற்று 2 சரியானது. கூற்று 1 தவறு, ஏனெனில் உச்ச நீதிமன்றம் பாடத்திட்டத்தை நிலைநிறுத்தியது, அது மதப் போதனையன்றி மதிப்புக் கல்வி எனத் தீர்ப்பளித்தது."
        },
        "why_not_others": {
            "A": {"en": "Statement 1 is false.", "ta": "கூற்று 1 தவறானது."},
            "B": {"en": "Correct. Statement 2 is true, while Statement 1 is false.", "ta": "சரி. கூற்று 2 உண்மை, கூற்று 1 தவறு."},
            "C": {"en": "Statement 1 is false.", "ta": "கூற்று 1 தவறானது."},
            "D": {"en": "Statement 2 is true.", "ta": "கூற்று 2 உண்மையாகும்."}
        },
        "tnpsc_tip": {
            "en": "Aruna Roy 2002 case: Value-based education = Secular, supported by Art 51A(h).",
            "ta": "அருணா ராய் 2002 வழக்கு: மதிப்புக் கல்வி = மதச்சார்பற்றது, உறுப்பு 51A(h) ஆல் ஆதரிக்கப்படுகிறது."
        }
    },
    {
        "id": "FD_S_023",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Hard",
        "question_type": "Statement",
        "question": {
            "en": "Consider the following statements regarding the Basic Structure doctrine and Fundamental Duties:\n1. In Minerva Mills (1980), SC held that harmony between Rights and DPSP forms Part of Basic Structure.\n2. Courts have extended this harmony doctrine to include Fundamental Duties (Part IVA).\n3. Elevating Rights while obliterating Duties damages constitutional equilibrium.\n4. Fundamental Duties can be altered by ordinary executive orders without constitutional amendment.\nWhich of the statements given above are CORRECT?",
            "ta": "அடிப்படை அமைப்பு தத்துவம் மற்றும் அடிப்படை கடமைகள் பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. மினர்வா மில்ஸ் (1980) வழக்கில், உரிமைகள் மற்றும் DPSP இடையேயான இணக்கம் அடிப்படை அமைப்பின் ஒரு பகுதி என உச்ச நீதிமன்றம் கருதியது.\n2. நீதிமன்றங்கள் இந்த இணக்க தத்துவத்தை அடிப்படை கடமைகளுக்கும் (பகுதி IVA) விரிவாக்கியுள்ளன.\n3. கடமைகளை அழித்து உரிமைகளை உயர்த்துவது அரசியலமைப்பு சமநிலையைச் சேதப்படுத்துகிறது.\n4. அரசியலமைப்பு திருத்தமின்றி சாதாரண நிர்வாக உத்தரவுகள் மூலம் அடிப்படை கடமைகளை மாற்ற முடியும்.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1, 2 and 3 only", "ta": "1, 2 மற்றும் 3 மட்டும்"},
            {"id": "B", "en": "1 and 4 only", "ta": "1 மற்றும் 4 மட்டும்"},
            {"id": "C", "en": "2, 3 and 4 only", "ta": "2, 3 மற்றும் 4 மட்டும்"},
            {"id": "D", "en": "1, 2, 3 and 4", "ta": "1, 2, 3 மற்றும் 4"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Statements 1, 2, and 3 are CORRECT. Statement 4 is INCORRECT because amending Article 51A requires a formal Constitutional Amendment under Article 368.",
            "ta": "கூற்றுகள் 1, 2, மற்றும் 3 சரியானவை. கூற்று 4 தவறு, ஏனெனில் உறுப்பு 51A-ஐ மாற்றுவதற்கு உறுப்பு 368-ன் கீழ் முறையான அரசியலமைப்பு திருத்தம் தேவை."
        },
        "why_not_others": {
            "A": {"en": "Correct. Statements 1, 2, and 3 are true, while Statement 4 is false.", "ta": "சரி. கூற்றுகள் 1, 2, மற்றும் 3 உண்மை, கூற்று 4 தவறு."},
            "B": {"en": "Statement 4 is false.", "ta": "கூற்று 4 தவறானது."},
            "C": {"en": "Statement 4 is false.", "ta": "கூற்று 4 தவறானது."},
            "D": {"en": "Statement 4 is false.", "ta": "கூற்று 4 தவறானது."}
        },
        "tnpsc_tip": {
            "en": "Part III + Part IV + Part IVA = Constitutional Equilibrium.",
            "ta": "பகுதி III + பகுதி IV + பகுதி IVA = அரசியலமைப்பு சமநிலை."
        }
    },
    {
        "id": "FD_S_024",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Statement",
        "question": {
            "en": "Consider the following statements regarding the 86th Constitutional Amendment Act, 2002:\n1. It inserted Article 21A in Part III.\n2. It substituted Article 45 in Part IV.\n3. It inserted clause (k) in Article 51A of Part IVA.\nWhich of the statements given above are CORRECT?",
            "ta": "2002-ன் 86வது அரசியலமைப்பு திருத்தச் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. இது பகுதி III-ல் உறுப்பு 21A-ஐச் சேர்த்தது.\n2. இது பகுதி IV-ல் உறுப்பு 45-ஐ மாற்றியமைத்தது.\n3. இது பகுதி IVA-ன் உறுப்பு 51A-ல் பிரிவு (k)-ஐச் சேர்த்தது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 and 2 only", "ta": "1 மற்றும் 2 மட்டும்"},
            {"id": "B", "en": "2 and 3 only", "ta": "2 மற்றும் 3 மட்டும்"},
            {"id": "C", "en": "1 and 3 only", "ta": "1 மற்றும் 3 மட்டும்"},
            {"id": "D", "en": "1, 2 and 3", "ta": "1, 2 மற்றும் 3"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "All three statements are CORRECT. 86th CAA 2002 introduced changes in all three key Parts (Part III, Part IV, Part IVA) related to education.",
            "ta": "மூன்று கூற்றுகளும் சரியானவை. 86வது திருத்தச் சட்டம் 2002 கல்வி தொடர்பான மூன்று முக்கியப் பகுதிகளிலும் (பகுதி III, பகுதி IV, பகுதி IVA) மாற்றங்களை அறிமுகப்படுத்தியது."
        },
        "why_not_others": {
            "A": {"en": "Statement 3 is also correct.", "ta": "கூற்று 3-ம் சரியானது."},
            "B": {"en": "Statement 1 is also correct.", "ta": "கூற்று 1-ம் சரியானது."},
            "C": {"en": "Statement 2 is also correct.", "ta": "கூற்று 2-ம் சரியானது."},
            "D": {"en": "Correct. All statements 1, 2, and 3 are correct.", "ta": "சரி. 1, 2 மற்றும் 3 ஆகிய அனைத்துக் கூற்றுகளும் சரி."}
        },
        "tnpsc_tip": {
            "en": "86th CAA 2002 is the ONLY amendment to add a Fundamental Duty after 1976.",
            "ta": "1976-க்குப் பிறகு ஒரு அடிப்படை கடமையைச் சேர்த்த ஒரே திருத்தம் 86வது திருத்தம் 2002 ஆகும்."
        }
    },
    {
        "id": "FD_S_025",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Statement",
        "question": {
            "en": "Consider the following statements regarding global constitutional comparison of Fundamental Duties:\n1. USA Constitution contains an entire chapter dedicated to citizen duties.\n2. Japanese Constitution includes explicit duties of citizens.\nWhich of the statements given above is/are CORRECT?",
            "ta": "அடிப்படை கடமைகளின் உலகளாவிய அரசியலமைப்பு ஒப்பீடு பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. அமெரிக்க அரசியலமைப்பு குடிமக்கள் கடமைகளுக்காக ஒரு முழு அத்தியாயத்தைக் கொண்டுள்ளது.\n2. ஜப்பானிய அரசியலமைப்பு குடிமக்களின் வெளிப்படையான கடமைகளை உள்ளடக்கியுள்ளது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 only", "ta": "1 மட்டுமே"},
            {"id": "B", "en": "2 only", "ta": "2 மட்டுமே"},
            {"id": "C", "en": "Both 1 and 2", "ta": "1 மற்றும் 2 இரண்டும்"},
            {"id": "D", "en": "Neither 1 nor 2", "ta": "1-ம் இல்லை 2-ம் இல்லை"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "Statement 2 is CORRECT. Statement 1 is INCORRECT because the USA Constitution does NOT contain an explicit chapter on citizen duties.",
            "ta": "கூற்று 2 சரியானது. கூற்று 1 தவறு, ஏனெனில் அமெரிக்க அரசியலமைப்பில் குடிமக்கள் கடமைகள் பற்றிய வெளிப்படையான அத்தியாயம் இல்லை."
        },
        "why_not_others": {
            "A": {"en": "Statement 1 is false.", "ta": "கூற்று 1 தவறானது."},
            "B": {"en": "Correct. Statement 2 is true, while Statement 1 is false.", "ta": "சரி. கூற்று 2 உண்மை, கூற்று 1 தவறு."},
            "C": {"en": "Statement 1 is false.", "ta": "கூற்று 1 தவறானது."},
            "D": {"en": "Statement 2 is true.", "ta": "கூற்று 2 உண்மையாகும்."}
        },
        "tnpsc_tip": {
            "en": "Japan is the prominent democratic precedent for explicit constitutional duties.",
            "ta": "வெளிப்படையான அரசியலமைப்பு கடமைகளுக்கான முக்கிய ஜனநாயக முன்மாதிரி ஜப்பான் ஆகும்."
        }
    },
    {
        "id": "FD_S_026",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Hard",
        "question_type": "Assertion & Reason",
        "question": {
            "en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Fundamental Duties under Article 51A remain fully in force and are NOT suspended during a National Emergency under Article 352.\nReason (R): Articles 358 and 359 provide for the suspension of Fundamental Rights in Part III, but no provision in the Constitution permits suspending Part IVA duties.\nIn the context of the above statements, which one of the following is correct?",
            "ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): உறுப்பு 352-ன் கீழ் தேசிய அவசரநிலையின் போது உறுப்பு 51A-ன் கீழ் உள்ள அடிப்படை கடமைகள் முழுமையாகச் செயல்பாட்டில் இருக்கும் மற்றும் அவை நிறுத்தி வைக்கப்பட மாட்டாது.\nகாரணம் (R): உறுப்புகள் 358 மற்றும் 359 பகுதி III அடிப்படை உரிமைகளை நிறுத்தி வைக்க வழிவகை செய்கின்றன, ஆனால் அரசியலமைப்பில் உள்ள எந்த விதியும் பகுதி IVA கடமைகளை நிறுத்தி வைக்க அனுமதிக்கவில்லை.\nமேற்கண்ட கூற்றுகளின் அடிப்படையில் பின்வருவனவற்றில் எது சரியானது?"
        },
        "options": [
            {"id": "A", "en": "Both A and R are correct and R is the correct explanation of A", "ta": "A மற்றும் R ஆகிய இரண்டும் சரி, மேலும் R என்பது A-வின் சரியான விளக்கமாகும்"},
            {"id": "B", "en": "Both A and R are correct but R is NOT the correct explanation of A", "ta": "A மற்றும் R ஆகிய இரண்டும் சரி, ஆனால் R என்பது A-வின் சரியான விளக்கம் அல்ல"},
            {"id": "C", "en": "A is correct but R is incorrect", "ta": "A சரி ஆனால் R தவறு"},
            {"id": "D", "en": "A is incorrect but R is correct", "ta": "A தவறு ஆனால் R சரி"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Both A and R are true. Reason R directly explains why duties remain operational during an Emergency: there is no constitutional suspension mechanism for Part IVA.",
            "ta": "A மற்றும் R ஆகிய இரண்டும் உண்மை. அவசரநிலையின் போது கடமைகள் ஏன் செயல்பாட்டில் உள்ளன என்பதை காரணம் R நேரடியாக விளக்குகிறது: பகுதி IVA-க்கு அரசியலமைப்பு நிறுத்தி வைப்பு அமைப்பு ஏதும் இல்லை."
        },
        "why_not_others": {
            "A": {"en": "Correct. R directly explains why duties cannot be suspended during Emergency.", "ta": "சரி. ஏன் அவசரநிலையின் போது கடமைகளை நிறுத்த முடியாது என்பதை R நேரடியாக விளக்குகிறது."},
            "B": {"en": "R is the direct explanation of A.", "ta": "R என்பது A-விற்கான நேரடி விளக்கமாகும்."},
            "C": {"en": "R is true.", "ta": "R உண்மையாகும்."},
            "D": {"en": "A is true.", "ta": "A உண்மையாகும்."}
        },
        "tnpsc_tip": {
            "en": "Emergency suspends Rights against State; Emergency NEVER suspends Duties of Citizens.",
            "ta": "அவசரநிலை அரசுக்கு எதிரான உரிமைகளை நிறுத்துகிறது; அவசரநிலை ஒருபோதும் குடிமக்கள் கடமைகளை நிறுத்துவதில்லை."
        }
    },
    {
        "id": "FD_S_027",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Hard",
        "question_type": "Statement",
        "question": {
            "en": "Consider the following statements regarding the 16th Constitutional Amendment Act, 1963:\n1. It added the words 'sovereignty and integrity of India' to Article 19(2).\n2. It amended the forms of Oath in the Third Schedule to include upholding sovereignty and integrity.\nWhich of the statements given above is/are CORRECT?",
            "ta": "1963-ன் 16வது அரசியலமைப்பு திருத்தச் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. இது உறுப்பு 19(2)-ல் 'இந்தியாவின் இறையாண்மை மற்றும் ஒருமைப்பாடு' என்ற சொற்களைச் சேர்த்தது.\n2. இறையாண்மை மற்றும் ஒருமைப்பாட்டைப் பேணுவதைச் சேர்க்க 3வது அட்டவணையில் உள்ள உறுதிமொழி படிவங்களை இது திருத்தியது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 only", "ta": "1 மட்டுமே"},
            {"id": "B", "en": "2 only", "ta": "2 மட்டுமே"},
            {"id": "C", "en": "Both 1 and 2", "ta": "1 மற்றும் 2 இரண்டும்"},
            {"id": "D", "en": "Neither 1 nor 2", "ta": "1-ம் இல்லை 2-ம் இல்லை"}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "Both statements 1 and 2 are CORRECT. The 16th CAA 1963 introduced 'sovereignty and integrity' into Art 19(2) and Third Schedule oaths, pre-dating Article 51A(c).",
            "ta": "கூற்றுகள் 1 மற்றும் 2 இரண்டும் சரியானவை. 16வது திருத்தச் சட்டம் 1963 உறுப்பு 51A(c)-க்கு முன்னதாகவே உறுப்பு 19(2) மற்றும் 3வது அட்டவணை உறுதிமொழிகளில் 'இறையாண்மை மற்றும் ஒருமைப்பாடு' என்பதை அறிமுகப்படுத்தியது."
        },
        "why_not_others": {
            "A": {"en": "Statement 2 is also correct.", "ta": "கூற்று 2-ம் சரியானது."},
            "B": {"en": "Statement 1 is also correct.", "ta": "கூற்று 1-ம் சரியானது."},
            "C": {"en": "Correct. Both statements 1 and 2 are correct.", "ta": "சரி. கூற்றுகள் 1 மற்றும் 2 இரண்டும் சரியானவை."},
            "D": {"en": "Both statements are true.", "ta": "இரண்டு கூற்றுகளும் உண்மை."}
        },
        "tnpsc_tip": {
            "en": "16th CAA 1963 introduced 'sovereignty and integrity' into Article 19(2).",
            "ta": "16வது திருத்தம் 1963 உறுப்பு 19(2)-ல் 'இறையாண்மை மற்றும் ஒருமைப்பாடு' என்பதை அறிமுகப்படுத்தியது."
        }
    },
    {
        "id": "FD_S_028",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Statement",
        "question": {
            "en": "Consider the following statements regarding the Prevention of Insults to National Honour Act, 1971:\n1. It penalizes disrespect to National Symbols.\n2. Disrespect under this Act attracts imprisonment up to 10 years.\nWhich of the statements given above is/are CORRECT?",
            "ta": "1971-ன் தேசிய கௌரவ அவமதிப்பு தடுப்புச் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. இது தேசிய சின்னங்களை அவமதிப்பதைத் தண்டிக்கிறது.\n2. இச்சட்டத்தின் கீழ் அவமதிப்பது 10 ஆண்டுகள் வரை சிறைத்தண்டனையை ஈர்க்கும்.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 only", "ta": "1 மட்டுமே"},
            {"id": "B", "en": "2 only", "ta": "2 மட்டுமே"},
            {"id": "C", "en": "Both 1 and 2", "ta": "1 மற்றும் 2 இரண்டும்"},
            {"id": "D", "en": "Neither 1 nor 2", "ta": "1-ம் இல்லை 2-ம் இல்லை"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Statement 1 is CORRECT. Statement 2 is INCORRECT because the maximum imprisonment under the Act is 3 years (not 10 years).",
            "ta": "கூற்று 1 சரியானது. கூற்று 2 தவறு, ஏனெனில் இச்சட்டத்தின் கீழ் அதிகபட்ச சிறைத்தண்டனை 3 ஆண்டுகள் ஆகும் (10 ஆண்டுகள் அல்ல)."
        },
        "why_not_others": {
            "A": {"en": "Correct. Statement 1 is true, while Statement 2 is false.", "ta": "சரி. கூற்று 1 உண்மை, கூற்று 2 தவறு."},
            "B": {"en": "Statement 2 is false.", "ta": "கூற்று 2 தவறானது."},
            "C": {"en": "Statement 2 is false.", "ta": "கூற்று 2 தவறானது."},
            "D": {"en": "Statement 1 is true.", "ta": "கூற்று 1 உண்மையாகும்."}
        },
        "tnpsc_tip": {
            "en": "Insult to National Symbols = Up to 3 years imprisonment.",
            "ta": "தேசிய சின்னங்கள் அவமதிப்பு = 3 ஆண்டுகள் வரை சிறைத்தண்டனை."
        }
    },
    {
        "id": "FD_S_029",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Statement",
        "question": {
            "en": "Consider the following statements regarding Article 51A:\n1. It includes a duty to pay income tax on time.\n2. It includes a duty to cast vote in elections.\nWhich of the statements given above is/are CORRECT?",
            "ta": "உறுப்பு 51A பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. வருமான வரியைத் தகுந்த நேரத்தில் செலுத்தும் கடமையை இது கொண்டுள்ளது.\n2. தேர்தலில் வாக்களிக்கும் கடமையை இது கொண்டுள்ளது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 only", "ta": "1 மட்டுமே"},
            {"id": "B", "en": "2 only", "ta": "2 மட்டுமே"},
            {"id": "C", "en": "Both 1 and 2", "ta": "1 மற்றும் 2 இரண்டும்"},
            {"id": "D", "en": "Neither 1 nor 2", "ta": "1-ம் இல்லை 2-ம் இல்லை"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "Both statements are INCORRECT. Duty to pay taxes and duty to vote were recommended by Swaran Singh Committee / NCRWC but were NOT added to Article 51A.",
            "ta": "இரண்டு கூற்றுகளும் தவறானவை. வரி செலுத்தும் கடமை மற்றும் வாக்களிக்கும் கடமை ஆகியவை பரிந்துரைக்கப்பட்ட போதிலும் உறுப்பு 51A-ல் சேர்க்கப்படவில்லை."
        },
        "why_not_others": {
            "A": {"en": "Statement 1 is false.", "ta": "கூற்று 1 தவறானது."},
            "B": {"en": "Statement 2 is false.", "ta": "கூற்று 2 தவறானது."},
            "C": {"en": "Both statements are false.", "ta": "இரண்டு கூற்றுகளும் தவறானவை."},
            "D": {"en": "Correct. Neither duty is present in Article 51A.", "ta": "சரி. எந்தக் கடமையும் உறுப்பு 51A-ல் இல்லை."}
        },
        "tnpsc_tip": {
            "en": "Duty to vote & duty to pay taxes are NOT in Article 51A.",
            "ta": "வாக்களிக்கும் கடமை & வரி செலுத்தும் கடமை ஆகியவை உறுப்பு 51A-ல் இல்லை."
        }
    },
    {
        "id": "FD_S_030",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Hard",
        "question_type": "Statement",
        "question": {
            "en": "Consider the following statements regarding 'Scientific Temper' under Article 51A(h):\n1. Scientific temper is a rational mental attitude that questions dogma, superstition, and unverified claims.\n2. Merely owning modern electronic devices without rational thinking constitutes scientific temper.\nWhich of the statements given above is/are CORRECT?",
            "ta": "உறுப்பு 51A(h)-ன் கீழ் உள்ள 'அறிவியல் மனப்பான்மை' பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. அறிவியல் மனப்பான்மை என்பது கோட்பாடுகள், மூடநம்பிக்கை, மற்றும் சான்றற்றக் கூற்றுகளைக் கேள்வி கேட்கும் பகுத்தறிவு மனநிலையாகும்.\n2. பகுத்தறிவுச் சிந்தனையின்றி நவீன மின்னணு சாதனங்களை வைத்திருப்பது மட்டுமே அறிவியல் மனப்பான்மையாகும்.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 only", "ta": "1 மட்டுமே"},
            {"id": "B", "en": "2 only", "ta": "2 மட்டுமே"},
            {"id": "C", "en": "Both 1 and 2", "ta": "1 மற்றும் 2 இரண்டும்"},
            {"id": "D", "en": "Neither 1 nor 2", "ta": "1-ம் இல்லை 2-ம் இல்லை"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Statement 1 is CORRECT. Statement 2 is INCORRECT because gadget ownership is NOT scientific temper.",
            "ta": "கூற்று 1 சரியானது. கூற்று 2 தவறு, ஏனெனில் கருவி உரிமையாளராக இருப்பது அறிவியல் மனப்பான்மை அல்ல."
        },
        "why_not_others": {
            "A": {"en": "Correct. Statement 1 is true, while Statement 2 is false.", "ta": "சரி. கூற்று 1 உண்மை, கூற்று 2 தவறு."},
            "B": {"en": "Statement 2 is false.", "ta": "கூற்று 2 தவறானது."},
            "C": {"en": "Statement 2 is false.", "ta": "கூற்று 2 தவறானது."},
            "D": {"en": "Statement 1 is true.", "ta": "கூற்று 1 உண்மையாகும்."}
        },
        "tnpsc_tip": {
            "en": "Scientific temper = Rational mindset & Anti-superstition attitude.",
            "ta": "அறிவியல் மனப்பான்மை = பகுத்தறிவு மனநிலை & மூடநம்பிக்கை எதிர்ப்பு மனப்பான்மை."
        }
    },
    {
        "id": "FD_S_031",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Statement",
        "question": {
            "en": "Consider the following statements regarding statutory laws supporting Article 51A(e) [Dignity of Women]:\n1. Dowry Prohibition Act, 1961 penalizes demanding dowry.\n2. Protection of Women from Domestic Violence Act, 2005 protects women from domestic abuse.\n3. Indecent Representation of Women (Prohibition) Act, 1986 penalizes indecent media depiction.\nWhich of the statements given above are CORRECT?",
            "ta": "உறுப்பு 51A(e) [பெண்கள் கண்ணியம்] ஐ ஆதரிக்கும் சட்டப்பூர்வச் சட்டங்கள் பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. வரதட்சணை தடைச் சட்டம் 1961 வரதட்சணை கேட்பதைத் தண்டிக்கிறது.\n2. குடும்ப வன்முறையிலிருந்து பெண்களைப் பாதுகாக்கும் சட்டம் 2005 பெண்களைக் குடும்பத் துன்புறுத்தலிலிருந்து பாதுகாக்கிறது.\n3. பெண்கள் ஒழுக்கக்கேடான சித்தரிப்பு (தடை) சட்டம் 1986 ஊடகங்களில் ஒழுக்கக்கேடான சித்தரிப்பதைத் தண்டிக்கிறது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 and 2 only", "ta": "1 மற்றும் 2 மட்டும்"},
            {"id": "B", "en": "2 and 3 only", "ta": "2 மற்றும் 3 மட்டும்"},
            {"id": "C", "en": "1 and 3 only", "ta": "1 மற்றும் 3 மட்டும்"},
            {"id": "D", "en": "1, 2 and 3", "ta": "1, 2 மற்றும் 3"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "All three statements are CORRECT statutory enactments translating Article 51A(e) into enforceable prohibitions.",
            "ta": "மூன்று கூற்றுகளும் உறுப்பு 51A(e)-ஐ அமல்படுத்தக்கூடிய தடைகளாக மாற்றும் சரியான சட்டப்பூர்வச் சட்டங்கள் ஆகும்."
        },
        "why_not_others": {
            "A": {"en": "Statement 3 is also correct.", "ta": "கூற்று 3-ம் சரியானது."},
            "B": {"en": "Statement 1 is also correct.", "ta": "கூற்று 1-ம் சரியானது."},
            "C": {"en": "Statement 2 is also correct.", "ta": "கூற்று 2-ம் சரியானது."},
            "D": {"en": "Correct. All statements 1, 2, and 3 are correct.", "ta": "சரி. 1, 2 மற்றும் 3 ஆகிய அனைத்துக் கூற்றுகளும் சரி."}
        },
        "tnpsc_tip": {
            "en": "Article 51A(e) forms the constitutional foundation for all gender-justice laws.",
            "ta": "உறுப்பு 51A(e) அனைத்து பாலின-நீதிச் சட்டங்களுக்கும் அரசியலமைப்பு அடித்தளமாக அமைகிறது."
        }
    },
    {
        "id": "FD_S_032",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Hard",
        "question_type": "Assertion & Reason",
        "question": {
            "en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Courts will not issue a writ of Mandamus directing Parliament to pass a law enforcing a Fundamental Duty.\nReason (R): Lawmaking is a discretionary sovereign legislative power, and courts cannot compel the legislature to enact specific legislation.\nIn the context of the above statements, which one of the following is correct?",
            "ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): அடிப்படை கடமையை அமல்படுத்தும் சட்டத்தை நிறைவேற்றுமாறு நாடாளுமன்றத்திற்கு வழிகாட்டி நீதிமன்றங்கள் செயலாற்றல் பேராணையை (Mandamus) பிறப்பிக்காது.\nகாரணம் (R): சட்டம் இயற்றுவது ஒரு தன்னாட்சிச் சட்டமன்ற அதிகாரம் என்பதால், ஒரு குறிப்பிட்ட சட்டத்தை இயற்றுமாறு சட்டமன்றத்தை நீதிமன்றங்கள் வற்புறுத்த முடியாது.\nமேற்கண்ட கூற்றுகளின் அடிப்படையில் பின்வருவனவற்றில் எது சரியானது?"
        },
        "options": [
            {"id": "A", "en": "Both A and R are correct and R is the correct explanation of A", "ta": "A மற்றும் R ஆகிய இரண்டும் சரி, மேலும் R என்பது A-வின் சரியான விளக்கமாகும்"},
            {"id": "B", "en": "Both A and R are correct but R is NOT the correct explanation of A", "ta": "A மற்றும் R ஆகிய இரண்டும் சரி, ஆனால் R என்பது A-வின் சரியான விளக்கம் அல்ல"},
            {"id": "C", "en": "A is correct but R is incorrect", "ta": "A சரி ஆனால் R தவறு"},
            {"id": "D", "en": "A is incorrect but R is correct", "ta": "A தவறு ஆனால் R சரி"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Both A and R are true. Mandamus cannot direct Parliament to enact laws (R), explaining why courts refuse PILs seeking Mandamus to pass duty laws (A).",
            "ta": "A மற்றும் R ஆகிய இரண்டும் உண்மை. சட்டம் இயற்ற நாடாளுமன்றத்திற்குப் பேராணை பிறப்பிக்க முடியாது (R), எனவேதான் கடமைச் சட்டங்களை நிறைவேற்றப் பேராணை கோரும் பொதுநல வழக்குகளை நீதிமன்றங்கள் மறுக்கின்றன (A)."
        },
        "why_not_others": {
            "A": {"en": "Correct. R directly explains Assertion A.", "ta": "சரி. R நேரடியாகக் கூற்று A-வை விளக்குகிறது."},
            "B": {"en": "R is the direct explanation of A.", "ta": "R என்பது A-விற்கான நேரடி விளக்கமாகும்."},
            "C": {"en": "R is true.", "ta": "R உண்மையாகும்."},
            "D": {"en": "A is true.", "ta": "A உண்மையாகும்."}
        },
        "tnpsc_tip": {
            "en": "Mandamus lies against executive/administrative bodies, NOT to direct Parliament to pass laws.",
            "ta": "செயலாற்றல் பேராணை நிர்வாக அமைப்புகளுக்கு எதிராகவே அமையும், சட்டம் இயற்ற நாடாளுமன்றத்திற்கு வழிகாட்ட அல்ல."
        }
    },
    {
        "id": "FD_S_033",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Hard",
        "question_type": "Statement",
        "question": {
            "en": "Consider the following statements comparing Article 39(f) [DPSP] and Article 51A(k) [FD]:\n1. Article 39(f) places a direct duty on parents to send children to school.\n2. Article 51A(k) obligates parents/guardians to provide education opportunities for children aged 6-14.\nWhich of the statements given above is/are CORRECT?",
            "ta": "உறுப்பு 39(f) [DPSP] மற்றும் உறுப்பு 51A(k) [FD] ஆகியவற்றை ஒப்பிடும் பின்வரும் கூற்றுகளைக் கருதுக:\n1. உறுப்பு 39(f) குழந்தைகளைப் பள்ளிக்கு அனுப்பும் நேரடிக் கடமையைப் பெற்றோர் மீது சுமத்துகிறது.\n2. உறுப்பு 51A(k) 6-14 வயதுக் குழந்தைகளுக்குக் கல்வி வாய்ப்புகளை வழங்கப் பெற்றோர்/பாதுகாவலர்களைக் கடமைப்படுத்துகிறது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 only", "ta": "1 மட்டுமே"},
            {"id": "B", "en": "2 only", "ta": "2 மட்டுமே"},
            {"id": "C", "en": "Both 1 and 2", "ta": "1 மற்றும் 2 இரண்டும்"},
            {"id": "D", "en": "Neither 1 nor 2", "ta": "1-ம் இல்லை 2-ம் இல்லை"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "Statement 2 is CORRECT. Statement 1 is INCORRECT because Article 39(f) is a State directive for child health, NOT a parent duty.",
            "ta": "கூற்று 2 சரியானது. கூற்று 1 தவறு, ஏனெனில் உறுப்பு 39(f) என்பது குழந்தைகள் ஆரோக்கியத்திற்கான அரசு வழிகாட்டுதலே தவிர பெற்றோர் கடமை அல்ல."
        },
        "why_not_others": {
            "A": {"en": "Statement 1 is false.", "ta": "கூற்று 1 தவறானது."},
            "B": {"en": "Correct. Statement 2 is true, while Statement 1 is false.", "ta": "சரி. கூற்று 2 உண்மை, கூற்று 1 தவறு."},
            "C": {"en": "Statement 1 is false.", "ta": "கூற்று 1 தவறானது."},
            "D": {"en": "Statement 2 is true.", "ta": "கூற்று 2 உண்மையாகும்."}
        },
        "tnpsc_tip": {
            "en": "Art 39(f) = State policy for child health | Art 51A(k) = Parent duty for child education.",
            "ta": "உறுப்பு 39(f) = குழந்தைகள் ஆரோக்கியத்திற்கான அரசுக் கொள்கை | உறுப்பு 51A(k) = குழந்தைகள் கல்விக்கான பெற்றோர் கடமை."
        }
    },
    {
        "id": "FD_S_034",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Statement",
        "question": {
            "en": "Consider the following statements regarding statutory environmental acts enforcing Article 51A(g):\n1. Water (Prevention and Control of Pollution) Act, 1974 penalizes river and water body pollution.\n2. Air (Prevention and Control of Pollution) Act, 1981 penalizes air pollution.\n3. Environment (Protection) Act, 1986 is an umbrella legislation for environmental preservation.\nWhich of the statements given above are CORRECT?",
            "ta": "உறுப்பு 51A(g)-ஐ அமல்படுத்தும் சட்டப்பூர்வ சுற்றுச்சூழல் சட்டங்கள் பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. நீர் (மாசு தடுப்பு மற்றும் கட்டுப்பாடு) சட்டம் 1974 ஆறு மற்றும் நீர்நிலை மாசைத் தண்டிக்கிறது.\n2. காற்று (மாசு தடுப்பு மற்றும் கட்டுப்பாடு) சட்டம் 1981 காற்று மாசைத் தண்டிக்கிறது.\n3. சுற்றுச்சூழல் (பாதுகாப்பு) சட்டம் 1986 சுற்றுச்சூழல் பேணலுக்கான ஒரு விரிவான குடைச் சட்டமாகும்.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 and 2 only", "ta": "1 மற்றும் 2 மட்டும்"},
            {"id": "B", "en": "2 and 3 only", "ta": "2 மற்றும் 3 மட்டும்"},
            {"id": "C", "en": "1 and 3 only", "ta": "1 மற்றும் 3 மட்டும்"},
            {"id": "D", "en": "1, 2 and 3", "ta": "1, 2 மற்றும் 3"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "All three statements are CORRECT statutory enactments giving penal teeth to Article 51A(g).",
            "ta": "மூன்று கூற்றுகளும் உறுப்பு 51A(g)-க்குக் குற்றவியல் பலத்தை வழங்கும் சரியான சட்டப்பூர்வச் சட்டங்கள் ஆகும்."
        },
        "why_not_others": {
            "A": {"en": "Statement 3 is also correct.", "ta": "கூற்று 3-ம் சரியானது."},
            "B": {"en": "Statement 1 is also correct.", "ta": "கூற்று 1-ம் சரியானது."},
            "C": {"en": "Statement 2 is also correct.", "ta": "கூற்று 2-ம் சரியானது."},
            "D": {"en": "Correct. All statements 1, 2, and 3 are correct.", "ta": "சரி. 1, 2 மற்றும் 3 ஆகிய அனைத்துக் கூற்றுகளும் சரி."}
        },
        "tnpsc_tip": {
            "en": "Environmental legislative trio (Water 1974, Air 1981, EPA 1986) operationalizes Art 51A(g).",
            "ta": "சுற்றுச்சூழல் சட்ட மூவர் (நீர் 1974, காற்று 1981, EPA 1986) உறுப்பு 51A(g)-ஐச் செயல்படுத்துகிறது."
        }
    },
    {
        "id": "FD_S_035",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Hard",
        "question_type": "Statement",
        "question": {
            "en": "Consider the following statements regarding Article 51A(c) and national security statutes:\n1. Article 51A(c) mandates protecting sovereignty, unity, and integrity of India.\n2. Unlawful Activities (Prevention) Act, 1967 penalizes activities assisting secession or dismemberment of India.\n3. Section 124A IPC and offences against the State penalize threats to sovereignty.\nWhich of the statements given above are CORRECT?",
            "ta": "உறுப்பு 51A(c) மற்றும் தேசியப் பாதுகாப்புச் சட்டங்கள் பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. உறுப்பு 51A(c) இந்தியாவின் இறையாண்மை, ஒற்றுமை, மற்றும் ஒருமைப்பாட்டைப் பாதுகாக்குமாறு ஆணையிடுகிறது.\n2. சட்டவிரோத நடவடிக்கைகள் தடுப்புச் சட்டம் 1967 இந்தியப் பிரிவினையை ஆதரிக்கும் செயல்பாடுகளைத் தண்டிக்கிறது.\n3. IPC பிரிவு 124A மற்றும் அரசுக்கு எதிரான குற்றங்கள் இறையாண்மைக்கு வரும் அச்சுறுத்தல்களைத் தண்டிக்கின்றன.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 and 2 only", "ta": "1 மற்றும் 2 மட்டும்"},
            {"id": "B", "en": "2 and 3 only", "ta": "2 மற்றும் 3 மட்டும்"},
            {"id": "C", "en": "1 and 3 only", "ta": "1 மற்றும் 3 மட்டும்"},
            {"id": "D", "en": "1, 2 and 3", "ta": "1, 2 மற்றும் 3"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "All three statements are CORRECT. UAPA 1967 and IPC State offences provide statutory enforcement for Article 51A(c).",
            "ta": "மூன்று கூற்றுகளும் சரியானவை. UAPA 1967 மற்றும் IPC அரசு குற்றங்கள் உறுப்பு 51A(c)-க்குச் சட்டப்பூர்வ அமலாக்கத்தை வழங்குகின்றன."
        },
        "why_not_others": {
            "A": {"en": "Statement 3 is also correct.", "ta": "கூற்று 3-ம் சரியானது."},
            "B": {"en": "Statement 1 is also correct.", "ta": "கூற்று 1-ம் சரியானது."},
            "C": {"en": "Statement 2 is also correct.", "ta": "கூற்று 2-ம் சரியானது."},
            "D": {"en": "Correct. All statements 1, 2, and 3 are correct.", "ta": "சரி. 1, 2 மற்றும் 3 ஆகிய அனைத்துக் கூற்றுகளும் சரி."}
        },
        "tnpsc_tip": {
            "en": "UAPA 1967 is the primary anti-secession statute reinforcing Article 51A(c).",
            "ta": "UAPA 1967 என்பது உறுப்பு 51A(c)-ஐ வலுப்படுத்தும் முதன்மைப் பிரிவினைவாத எதிர்ப்புச் சட்டமாகும்."
        }
    },
    {
        "id": "FD_S_036",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Hard",
        "question_type": "Statement",
        "question": {
            "en": "Consider the following statements regarding Sachidanand Pandey v. State of West Bengal (1987):\n1. Justice O. Chinnappa Reddy held that courts must consider Articles 48A and 51A(g) whenever ecological issues are raised.\n2. The Court held that environmental duties can be completely ignored if industrial profits are involved.\nWhich of the statements given above is/are CORRECT?",
            "ta": "சச்சிதானந்த் பாண்டே vs மேற்கு வங்காள மாநிலம் (1987) பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. சுற்றுச்சூழல் பிரச்சினைகள் எழும் போதெல்லாம் நீதிமன்றங்கள் உறுப்புகள் 48A மற்றும் 51A(g)-ஐக் கருத வேண்டும் என நீதிபதி ஓ. சின்னப்ப ரெட்டி தீர்ப்பளித்தார்.\n2. தொழில்துறை லாபங்கள் சம்பந்தப்பட்டிருந்தால் சுற்றுச்சூழல் கடமைகளை முற்றிலுமாகப் புறக்கணிக்கலாம் என நீதிமன்றம் கருதியது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 only", "ta": "1 மட்டுமே"},
            {"id": "B", "en": "2 only", "ta": "2 மட்டுமே"},
            {"id": "C", "en": "Both 1 and 2", "ta": "1 மற்றும் 2 இரண்டும்"},
            {"id": "D", "en": "Neither 1 nor 2", "ta": "1-ம் இல்லை 2-ம் இல்லை"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Statement 1 is CORRECT. Statement 2 is INCORRECT because ecological considerations under Arts 48A and 51A(g) cannot be bypassed for commercial gain.",
            "ta": "கூற்று 1 சரியானது. கூற்று 2 தவறு, ஏனெனில் வர்த்தக லாபத்திற்காக உறுப்புகள் 48A மற்றும் 51A(g)-ன் கீழ் உள்ள சுற்றுச்சூழல் பரிசீலனைகளைப் புறக்கணிக்க முடியாது."
        },
        "why_not_others": {
            "A": {"en": "Correct. Statement 1 is true, while Statement 2 is false.", "ta": "சரி. கூற்று 1 உண்மை, கூற்று 2 தவறு."},
            "B": {"en": "Statement 2 is false.", "ta": "கூற்று 2 தவறானது."},
            "C": {"en": "Statement 2 is false.", "ta": "கூற்று 2 தவறானது."},
            "D": {"en": "Statement 1 is true.", "ta": "கூற்று 1 உண்மையாகும்."}
        },
        "tnpsc_tip": {
            "en": "Sachidanand Pandey 1987: Non-justiciability is no defense against judicial review of ecological issues.",
            "ta": "சச்சிதானந்த் பாண்டே 1987: சுற்றுச்சூழல் பிரச்சினைகளின் நீதித்துறை ஆய்விற்கு அமல்படுத்த முடியாதது என்பது தற்காப்பு அல்ல."
        }
    },
    {
        "id": "FD_S_037",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Statement",
        "question": {
            "en": "Consider the following statements regarding Mohan Kumar Singhania v. Union of India (1992):\n1. The Supreme Court cited Article 51A(j) to uphold mandatory training regulations for civil service probationers.\n2. The Court held that striving for excellence under Article 51A(j) promotes efficiency in public administration.\nWhich of the statements given above is/are CORRECT?",
            "ta": "மோகன் குமார் சிங்கானியா vs இந்திய யூனியன் (1992) பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. அரசுப் பணிப் பயிற்சியாளர்களுக்கான கட்டாயப் பயிற்சி விதிகளை நிலைநிறுத்த உச்ச நீதிமன்றம் உறுப்பு 51A(j)-ஐ மேற்கோள் காட்டியது.\n2. உறுப்பு 51A(j)-ன் கீழ் சிறப்பினை நோக்கி முயலுவது பொது நிர்வாகத்தில் திறமையை ஊக்குவிக்கிறது என நீதிமன்றம் கருதியது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 only", "ta": "1 மட்டுமே"},
            {"id": "B", "en": "2 only", "ta": "2 மட்டுமே"},
            {"id": "C", "en": "Both 1 and 2", "ta": "1 மற்றும் 2 இரண்டும்"},
            {"id": "D", "en": "Neither 1 nor 2", "ta": "1-ம் இல்லை 2-ம் இல்லை"}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "Both statements 1 and 2 are CORRECT. SC used Article 51A(j) to support professional training and performance standards in public service.",
            "ta": "கூற்றுகள் 1 மற்றும் 2 இரண்டும் சரியானவை. பொதுப் பணிகளில் தொழில்முறைப் பயிற்சி மற்றும் செயல்திறன் தரங்களை ஆதரிக்க உச்ச நீதிமன்றம் உறுப்பு 51A(j)-ஐப் பயன்படுத்தியது."
        },
        "why_not_others": {
            "A": {"en": "Statement 2 is also correct.", "ta": "கூற்று 2-ம் சரியானது."},
            "B": {"en": "Statement 1 is also correct.", "ta": "கூற்று 1-ம் சரியானது."},
            "C": {"en": "Correct. Both statements 1 and 2 are correct.", "ta": "சரி. கூற்றுகள் 1 மற்றும் 2 இரண்டும் சரியானவை."},
            "D": {"en": "Both statements are true.", "ta": "இரண்டு கூற்றுகளும் உண்மை."}
        },
        "tnpsc_tip": {
            "en": "Article 51A(j) is linked with administrative efficiency and civil service excellence.",
            "ta": "உறுப்பு 51A(j) நிர்வாகத் திறமை மற்றும் அரசுப் பணிச் சிறப்புடன் இணைக்கப்பட்டுள்ளது."
        }
    },
    {
        "id": "FD_S_038",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Hard",
        "question_type": "Assertion & Reason",
        "question": {
            "en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Parliamentary legislation giving effect to a Fundamental Duty under Article 51A is generally treated by courts as imposing a 'reasonable restriction' under Article 19.\nReason (R): Fundamental Rights and Fundamental Duties are correlative and inseverable, forming a balanced code of civic rights and responsibilities.\nIn the context of the above statements, which one of the following is correct?",
            "ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): உறுப்பு 51A-ன் கீழ் உள்ள அடிப்படை கடமையை அமல்படுத்தும் நாடாளுமன்றச் சட்டம் வழக்கமாக உறுப்பு 19-ன் கீழ் 'நியாயமான கட்டுப்பாட்டை' விதிப்பதாக நீதிமன்றங்களால் கருதப்படுகிறது.\nகாரணம் (R): அடிப்படை உரிமைகளும் அடிப்படை கடமைகளும் ஒன்றோடொன்று தொடர்புடையவை மற்றும் பிரிக்க முடியாதவை, அவை குடிமை உரிமைகள் மற்றும் பொறுப்புகளின் சமநிலையான விதியை உருவாக்குகின்றன.\nமேற்கண்ட கூற்றுகளின் அடிப்படையில் பின்வருவனவற்றில் எது சரியானது?"
        },
        "options": [
            {"id": "A", "en": "Both A and R are correct and R is the correct explanation of A", "ta": "A மற்றும் R ஆகிய இரண்டும் சரி, மேலும் R என்பது A-வின் சரியான விளக்கமாகும்"},
            {"id": "B", "en": "Both A and R are correct but R is NOT the correct explanation of A", "ta": "A மற்றும் R ஆகிய இரண்டும் சரி, ஆனால் R என்பது A-வின் சரியான விளக்கம் அல்ல"},
            {"id": "C", "en": "A is correct but R is incorrect", "ta": "A சரி ஆனால் R தவறு"},
            {"id": "D", "en": "A is incorrect but R is correct", "ta": "A தவறு ஆனால் R சரி"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Both A and R are true. Reason R provides the underlying jurisprudence explaining why duty-enforcing laws are treated as reasonable restrictions under Article 19.",
            "ta": "A மற்றும் R ஆகிய இரண்டும் உண்மை. ஏன் கடமையை அமல்படுத்தும் சட்டங்கள் உறுப்பு 19-ன் கீழ் நியாயமான கட்டுப்பாடுகளாகக் கருதப்படுகின்றன என்பதை விளக்கும் அடிப்படையான சட்டவியல் தத்துவத்தை R வழங்குகிறது."
        },
        "why_not_others": {
            "A": {"en": "Correct. R directly explains Assertion A.", "ta": "சரி. R நேரடியாகக் கூற்று A-வை விளக்குகிறது."},
            "B": {"en": "R is the direct explanation of A.", "ta": "R என்பது A-விற்கான நேரடி விளக்கமாகும்."},
            "C": {"en": "R is true.", "ta": "R உண்மையாகும்."},
            "D": {"en": "A is true.", "ta": "A உண்மையாகும்."}
        },
        "tnpsc_tip": {
            "en": "Duties provide constitutional justification for 'reasonableness' of restrictions on Article 19 rights.",
            "ta": "உறுப்பு 19 உரிமைகள் மீதான கட்டுப்பாடுகளின் 'நியாயத் தன்மைக்கு' கடமைகள் அரசியலமைப்பு நியாயத்தை வழங்குகின்றன."
        }
    },
    {
        "id": "FD_S_039",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Statement",
        "question": {
            "en": "Consider the following statements regarding 'Humanism' under Article 51A(h):\n1. Humanism is an active rational value prioritizing human welfare and dignity above dogmatic traditions.\n2. Humanism is identical to passive religious tolerance without active rational reform.\nWhich of the statements given above is/are CORRECT?",
            "ta": "உறுப்பு 51A(h)-ன் கீழ் உள்ள 'மனிதநேயம்' பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. மனிதநேயம் என்பது கோட்பாட்டுப் பாரம்பரியங்களுக்கு மேலாக மனித நலன் மற்றும் கண்ணியத்திற்கு முன்னுரிமை அளிக்கும் ஒரு செயலில் உள்ள பகுத்தறிவு மதிப்பாகும்.\n2. மனிதநேயம் என்பது செயலில் உள்ள பகுத்தறிவுச் சீர்திருத்தமின்றி சாதாரண மதச் சகிப்புத்தன்மைக்குச் சமமானது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 only", "ta": "1 மட்டுமே"},
            {"id": "B", "en": "2 only", "ta": "2 மட்டுமே"},
            {"id": "C", "en": "Both 1 and 2", "ta": "1 மற்றும் 2 இரண்டும்"},
            {"id": "D", "en": "Neither 1 nor 2", "ta": "1-ம் இல்லை 2-ம் இல்லை"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Statement 1 is CORRECT. Statement 2 is INCORRECT because Humanism goes beyond passive tolerance by actively advocating rational reform and anti-superstition.",
            "ta": "கூற்று 1 சரியானது. கூற்று 2 தவறு, ஏனெனில் மனிதநேயம் பகுத்தறிவுச் சீர்திருத்தம் மற்றும் மூடநம்பிக்கை எதிர்ப்பைச் செயலில் ஆதரிப்பதன் மூலம் சாதாரணச் சகிப்புத்தன்மையைத் தாண்டிச் செல்கிறது."
        },
        "why_not_others": {
            "A": {"en": "Correct. Statement 1 is true, while Statement 2 is false.", "ta": "சரி. கூற்று 1 உண்மை, கூற்று 2 தவறு."},
            "B": {"en": "Statement 2 is false.", "ta": "கூற்று 2 தவறானது."},
            "C": {"en": "Statement 2 is false.", "ta": "கூற்று 2 தவறானது."},
            "D": {"en": "Statement 1 is true.", "ta": "கூற்று 1 உண்மையாகும்."}
        },
        "tnpsc_tip": {
            "en": "Humanism in Art 51A(h) is an active, rational, social reform value.",
            "ta": "உறுப்பு 51A(h)-ல் உள்ள மனிதநேயம் என்பது ஒரு செயலில் உள்ள, பகுத்தறிவு, சமூகச் சீர்திருத்த மதிப்பாகும்."
        }
    },
    {
        "id": "FD_S_040",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Statement",
        "question": {
            "en": "Consider the following statements regarding Union of India v. Naveen Jindal (2004):\n1. Flying the National Flag with respect is a Fundamental Right under Article 19(1)(a).\n2. Flying the National Flag must comply with the Flag Code of India and Article 51A(a) duty of respect.\nWhich of the statements given above is/are CORRECT?",
            "ta": "இந்திய யூனியன் vs நவீன் ஜிண்டால் (2004) பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. மரியாதையுடன் தேசியக் கொடியைப் பறக்கவிடுவது உறுப்பு 19(1)(a)-ன் கீழ் ஒரு அடிப்படை உரிமையாகும்.\n2. தேசியக் கொடியைப் பறக்கவிடுவது இந்தியக் கொடி குறியீடு மற்றும் உறுப்பு 51A(a) மரியாதைக் கடமைக்கு உட்பட வேண்டும்.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 only", "ta": "1 மட்டுமே"},
            {"id": "B", "en": "2 only", "ta": "2 மட்டுமே"},
            {"id": "C", "en": "Both 1 and 2", "ta": "1 மற்றும் 2 இரண்டும்"},
            {"id": "D", "en": "Neither 1 nor 2", "ta": "1-ம் இல்லை 2-ம் இல்லை"}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "Both statements 1 and 2 are CORRECT. SC held that citizens have a right to fly the National Flag under Art 19(1)(a), subject to Flag Code guidelines and Art 51A(a) duty.",
            "ta": "கூற்றுகள் 1 மற்றும் 2 இரண்டும் சரியானவை. கொடி குறியீடு வழிகாட்டுதல்கள் மற்றும் உறுப்பு 51A(a) கடமைக்கு உட்பட்டு, குடிமக்களுக்கு உறுப்பு 19(1)(a)-ன் கீழ் தேசியக் கொடியைப் பறக்கவிட உரிமை உண்டு என உச்ச நீதிமன்றம் தீர்ப்பளித்தது."
        },
        "why_not_others": {
            "A": {"en": "Statement 1 is also correct.", "ta": "கூற்று 1-ம் சரியானது."},
            "B": {"en": "Statement 2 is also correct.", "ta": "கூற்று 2-ம் சரியானது."},
            "C": {"en": "Correct. Both statements 1 and 2 are correct.", "ta": "சரி. கூற்றுகள் 1 மற்றும் 2 இரண்டும் சரியானவை."},
            "D": {"en": "Both statements are true.", "ta": "இரண்டு கூற்றுகளும் உண்மை."}
        },
        "tnpsc_tip": {
            "en": "Naveen Jindal 2004: Flying National Flag = Art 19(1)(a) Right + Art 51A(a) Duty.",
            "ta": "நவீன் ஜிண்டால் 2004: தேசியக் கொடி பறக்கவிடுவது = உறுப்பு 19(1)(a) உரிமை + உறுப்பு 51A(a) கடமை."
        }
    },
    {
        "id": "FD_S_041",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Hard",
        "question_type": "Statement",
        "question": {
            "en": "Consider the following statements regarding the Constituent Assembly (1946-1949) and Fundamental Duties:\n1. The original Constituent Assembly did not include a separate chapter on Fundamental Duties in 1950.\n2. Framers assumed that citizens in free India would naturally perform civic duties without constitutional compulsion.\nWhich of the statements given above is/are CORRECT?",
            "ta": "அரசியல் நிர்ணய சபை (1946-1949) மற்றும் அடிப்படை கடமைகள் பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. அசல் அரசியல் நிர்ணய சபை 1950-ல் அடிப்படை கடமைகள் பற்றிய தனி அத்தியாயத்தைச் சேர்க்கவில்லை.\n2. சுதந்திர இந்தியாவின் குடிமக்கள் அரசியலமைப்பு வற்புறுத்தலின்றி இயல்பாகவே குடிமை கடமைகளைச் செய்வார்கள் என உருவாக்குநர்கள் கருதினர்.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 only", "ta": "1 மட்டுமே"},
            {"id": "B", "en": "2 only", "ta": "2 மட்டுமே"},
            {"id": "C", "en": "Both 1 and 2", "ta": "1 மற்றும் 2 இரண்டும்"},
            {"id": "D", "en": "Neither 1 nor 2", "ta": "1-ம் இல்லை 2-ம் இல்லை"}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "Both statements 1 and 2 are CORRECT. The framers relied on moral tradition and civic consciousness, omitting an explicit duties chapter until 1976.",
            "ta": "கூற்றுகள் 1 மற்றும் 2 இரண்டும் சரியானவை. உருவாக்குநர்கள் தார்மீகப் பாரம்பரியம் மற்றும் குடிமை உணர்வை நம்பினர், 1976 வரை வெளிப்படையான கடமைகள் அத்தியாயத்தை விடுத்தனர்."
        },
        "why_not_others": {
            "A": {"en": "Statement 1 is also correct.", "ta": "கூற்று 1-ம் சரியானது."},
            "B": {"en": "Statement 2 is also correct.", "ta": "கூற்று 2-ம் சரியானது."},
            "C": {"en": "Correct. Both statements 1 and 2 are correct.", "ta": "சரி. கூற்றுகள் 1 மற்றும் 2 இரண்டும் சரியானவை."},
            "D": {"en": "Both statements are true.", "ta": "இரண்டு கூற்றுகளும் உண்மை."}
        },
        "tnpsc_tip": {
            "en": "Absence of duties in 1950 was due to faith in voluntary civic tradition.",
            "ta": "1950-ல் கடமைகள் இல்லாதிருந்ததற்குக் காரணம் தன்னார்வக் குடிமைப் பாரம்பரியத்தின் மீதான நம்பிக்கையே ஆகும்."
        }
    },
    {
        "id": "FD_S_042",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Hard",
        "question_type": "Statement",
        "question": {
            "en": "Consider the following statements regarding the duty to abide by the Constitution under Article 51A(a):\n1. It commands obedience to Constitutional Supremacy and Rule of Law.\n2. It obligates citizens to blindly obey illegal or unconstitutional executive orders.\nWhich of the statements given above is/are CORRECT?",
            "ta": "உறுப்பு 51A(a)-ன் கீழ் அரசியலமைப்புக்குக் கீழ்ப்படியும் கடமை பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. இது அரசியலமைப்பு மேலாதிக்கம் மற்றும் சட்டத்தின் ஆட்சிக்குக் கீழ்ப்படிய ஆணையிடுகிறது.\n2. இது சட்டவிரோத அல்லது அரசியலமைப்பிற்கு எதிரான நிர்வாக உத்தரவுகளுக்குக் குருட்டுத்தனமாகக் கீழ்ப்படியக் குடிமக்களைக் கடமைப்படுத்துகிறது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 only", "ta": "1 மட்டுமே"},
            {"id": "B", "en": "2 only", "ta": "2 மட்டுமே"},
            {"id": "C", "en": "Both 1 and 2", "ta": "1 மற்றும் 2 இரண்டும்"},
            {"id": "D", "en": "Neither 1 nor 2", "ta": "1-ம் இல்லை 2-ம் இல்லை"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Statement 1 is CORRECT. Statement 2 is INCORRECT because abiding by the Constitution requires upholding Constitutional Supremacy, NOT obeying unconstitutional or illegal orders.",
            "ta": "கூற்று 1 சரியானது. கூற்று 2 தவறு, ஏனெனில் அரசியலமைப்புக்குக் கீழ்ப்படிவது அரசியலமைப்பு மேலாதிக்கத்தை நிலைநிறுத்துவதைக் கோருகிறதே தவிர, அரசியலமைப்பிற்கு எதிரான அல்லது சட்டவிரோத உத்தரவுகளுக்குக் கீழ்ப்படிவதை அல்ல."
        },
        "why_not_others": {
            "A": {"en": "Correct. Statement 1 is true, while Statement 2 is false.", "ta": "சரி. கூற்று 1 உண்மை, கூற்று 2 தவறு."},
            "B": {"en": "Statement 2 is false.", "ta": "கூற்று 2 தவறானது."},
            "C": {"en": "Statement 2 is false.", "ta": "கூற்று 2 தவறானது."},
            "D": {"en": "Statement 1 is true.", "ta": "கூற்று 1 உண்மையாகும்."}
        },
        "tnpsc_tip": {
            "en": "Abiding by Constitution = Respecting Rule of Law & Constitutional Values.",
            "ta": "அரசியலமைப்புக்குக் கீழ்ப்படிவது = சட்டத்தின் ஆட்சி & அரசியலமைப்பு மதிப்புகளை மதிக்கிறது."
        }
    },
    {
        "id": "FD_S_043",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Statement",
        "question": {
            "en": "Consider the following statements regarding Verma Committee (1999) educational recommendations:\n1. Printing Fundamental Duties on the back cover of school textbooks across India.\n2. Teacher training programs to impart civic values to students.\n3. Creating mandatory military service for all high school graduates.\nWhich of the statements given above are CORRECT?",
            "ta": "வர்மா குழுவின் (1999) கல்விப் பரிந்துரைகள் பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. இந்தியா முழுவதும் உள்ள பள்ளி பாடப்புத்தகங்களின் பின்பக்கத்தில் அடிப்படை கடமைகளை அச்சிடுதல்.\n2. மாணவர்களுக்குக் குடிமை மதிப்புகளை வழங்க ஆசிரியர் பயிற்சித் திட்டங்கள்.\n3. அனைத்து உயர்நிலைப் பள்ளி பட்டதாரிகளுக்கும் கட்டாய ராணுவச் சேவையை உருவாக்குதல்.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 and 2 only", "ta": "1 மற்றும் 2 மட்டும்"},
            {"id": "B", "en": "2 and 3 only", "ta": "2 மற்றும் 3 மட்டும்"},
            {"id": "C", "en": "1 and 3 only", "ta": "1 மற்றும் 3 மட்டும்"},
            {"id": "D", "en": "1, 2 and 3", "ta": "1, 2 மற்றும் 3"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Statements 1 and 2 are CORRECT recommendations of the Verma Committee. Statement 3 is INCORRECT because compulsory military service was NOT recommended.",
            "ta": "கூற்றுகள் 1 மற்றும் 2 ஆகியவை வர்மா குழுவின் சரியான பரிந்துரைகள் ஆகும். கூற்று 3 தவறு, ஏனெனில் கட்டாய ராணுவ சேவை பரிந்துரைக்கப்படவில்லை."
        },
        "why_not_others": {
            "A": {"en": "Correct. Statements 1 and 2 are true, while Statement 3 is false.", "ta": "சரி. கூற்றுகள் 1 மற்றும் 2 உண்மை, கூற்று 3 தவறு."},
            "B": {"en": "Statement 3 is false.", "ta": "கூற்று 3 தவறானது."},
            "C": {"en": "Statement 3 is false.", "ta": "கூற்று 3 தவறானது."},
            "D": {"en": "Statement 3 is false.", "ta": "கூற்று 3 தவறானது."}
        },
        "tnpsc_tip": {
            "en": "Verma Committee advocated pedagogical integration (textbooks + teacher orientation).",
            "ta": "வர்மா குழு கற்பித்தல் ஒருங்கிணைப்பை (பாடப்புத்தகங்கள் + ஆசிரியர் வழிகாட்டுதல்) ஆதரித்தது."
        }
    },
    {
        "id": "FD_S_044",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Hard",
        "question_type": "Assertion & Reason",
        "question": {
            "en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Mahatma Gandhi emphasized that the true source of rights is duty performed.\nReason (R): If we all discharge our duties, rights will not be far to seek, but if we run after rights without performing duties, they will escape us like a will-o'-the-wisp.\nIn the context of the above statements, which one of the following is correct?",
            "ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): உரிமைகளின் உண்மையான ஆதாரம் செய்யப்பட்ட கடமையே என்று மகாத்மா காந்தி வலியுறுத்தினார்.\nகாரணம் (R): நாம் அனைவரும் நமது கடமைகளைச் செய்தால், உரிமைகள் தொலைவில் இருக்காது, ஆனால் கடமைகளைச் செய்யாமல் உரிமைகளைப் பின்தொடர்ந்தால், அவை கானல் நீர் போல நம்மை விட்டுத் தப்பிவிடும்.\nமேற்கண்ட கூற்றுகளின் அடிப்படையில் பின்வருவனவற்றில் எது சரியானது?"
        },
        "options": [
            {"id": "A", "en": "Both A and R are correct and R is the correct explanation of A", "ta": "A மற்றும் R ஆகிய இரண்டும் சரி, மேலும் R என்பது A-வின் சரியான விளக்கமாகும்"},
            {"id": "B", "en": "Both A and R are correct but R is NOT the correct explanation of A", "ta": "A மற்றும் R ஆகிய இரண்டும் சரி, ஆனால் R என்பது A-வின் சரியான விளக்கம் அல்ல"},
            {"id": "C", "en": "A is correct but R is incorrect", "ta": "A சரி ஆனால் R தவறு"},
            {"id": "D", "en": "A is incorrect but R is correct", "ta": "A தவறு ஆனால் R சரி"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Both A and R are true. Reason R is the exact quotation and philosophy of Mahatma Gandhi regarding the organic link between Rights and Duties.",
            "ta": "A மற்றும் R ஆகிய இரண்டும் உண்மை. காரணம் R என்பது உரிமைகள் மற்றும் கடமைகளுக்கு இடையேயான பிணைப்பு பற்றிய மகாத்மா காந்தியின் சரியான மேற்கோள் மற்றும் தத்துவமாகும்."
        },
        "why_not_others": {
            "A": {"en": "Correct. R directly explains Gandhian philosophy behind Assertion A.", "ta": "சரி. R நேரடியாகக் கூற்று A-வின் பின்னால் உள்ள காந்தியத் தத்துவத்தை விளக்குகிறது."},
            "B": {"en": "R is the direct explanation of A.", "ta": "R என்பது A-விற்கான நேரடி விளக்கமாகும்."},
            "C": {"en": "R is true.", "ta": "R உண்மையாகும்."},
            "D": {"en": "A is true.", "ta": "A உண்மையாகும்."}
        },
        "tnpsc_tip": {
            "en": "Gandhian philosophy: Performance of duty creates the ethical foundation for claiming rights.",
            "ta": "காந்தியத் தத்துவம்: கடமையைச் செய்வது உரிமைகளைக் கோருவதற்கான தார்மீக அடித்தளத்தை உருவாக்குகிறது."
        }
    },
    {
        "id": "FD_S_045",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Statement",
        "question": {
            "en": "Consider the following statements comparing Article 48A and Article 51A(g):\n1. Article 48A (DPSP Part IV) directs the STATE to protect and improve the environment.\n2. Article 51A(g) (FD Part IVA) mandates every CITIZEN to protect and improve the natural environment.\n3. Both provisions were added to the Constitution by the 42nd Constitutional Amendment Act, 1976.\nWhich of the statements given above are CORRECT?",
            "ta": "உறுப்பு 48A மற்றும் உறுப்பு 51A(g) ஆகியவற்றை ஒப்பிடும் பின்வரும் கூற்றுகளைக் கருதுக:\n1. உறுப்பு 48A (DPSP பகுதி IV) சுற்றுச்சூழலைப் பாதுகாத்து மேம்படுத்த அரசுக்கு வழிகாட்டுகிறது.\n2. உறுப்பு 51A(g) (FD பகுதி IVA) இயற்கை சுற்றுச்சூழலைப் பாதுகாத்து மேம்படுத்த ஒவ்வொரு குடிமகனையும் கடமைப்படுத்துகிறது.\n3. இரண்டு விதிகளும் 1976-ன் 42வது அரசியலமைப்பு திருத்தச் சட்டத்தால் அரசியலமைப்பில் சேர்க்கப்பட்டன.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 and 2 only", "ta": "1 மற்றும் 2 மட்டும்"},
            {"id": "B", "en": "2 and 3 only", "ta": "2 மற்றும் 3 மட்டும்"},
            {"id": "C", "en": "1 and 3 only", "ta": "1 மற்றும் 3 மட்டும்"},
            {"id": "D", "en": "1, 2 and 3", "ta": "1, 2 மற்றும் 3"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "All three statements are CORRECT. 42nd CAA 1976 added both Article 48A (State DPSP) and Article 51A(g) (Citizen FD) simultaneously.",
            "ta": "மூன்று கூற்றுகளும் சரியானவை. 42வது திருத்தச் சட்டம் 1976 ஒரே நேரத்தில் உறுப்பு 48A (அரசு DPSP) மற்றும் உறுப்பு 51A(g) (குடிமகன் FD) இரண்டையும் சேர்த்தது."
        },
        "why_not_others": {
            "A": {"en": "Statement 3 is also correct.", "ta": "கூற்று 3-ம் சரியானது."},
            "B": {"en": "Statement 1 is also correct.", "ta": "கூற்று 1-ம் சரியானது."},
            "C": {"en": "Statement 2 is also correct.", "ta": "கூற்று 2-ம் சரியானது."},
            "D": {"en": "Correct. All statements 1, 2, and 3 are correct.", "ta": "சரி. 1, 2 மற்றும் 3 ஆகிய அனைத்துக் கூற்றுகளும் சரி."}
        },
        "tnpsc_tip": {
            "en": "Both Article 48A and Article 51A(g) were added by the 42nd CAA in 1976.",
            "ta": "உறுப்பு 48A மற்றும் உறுப்பு 51A(g) ஆகிய இரண்டும் 1976-ல் 42வது திருத்தத்தால் சேர்க்கப்பட்டன."
        }
    },
    {
        "id": "FD_S_046",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Statement",
        "question": {
            "en": "Consider the following statements regarding the Right to Free and Compulsory Education Act, 2009 (RTE Act):\n1. It gives statutory effect to Article 21A Fundamental Right.\n2. It provides operational mechanisms for parents to fulfill their Article 51A(k) duty.\nWhich of the statements given above is/are CORRECT?",
            "ta": "இலவச கட்டாயக் கல்விச் சட்டம் 2009 (RTE சட்டம்) பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. இது உறுப்பு 21A அடிப்படை உரிமைக்குச் சட்டப்பூர்வ விளைவை வழங்குகிறது.\n2. பெற்றோர் தங்கள் உறுப்பு 51A(k) கடமையை நிறைவேற்ற இது செயல்பாட்டு அமைப்புகளை வழங்குகிறது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 only", "ta": "1 மட்டுமே"},
            {"id": "B", "en": "2 only", "ta": "2 மட்டுமே"},
            {"id": "C", "en": "Both 1 and 2", "ta": "1 மற்றும் 2 இரண்டும்"},
            {"id": "D", "en": "Neither 1 nor 2", "ta": "1-ம் இல்லை 2-ம் இல்லை"}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "Both statements 1 and 2 are CORRECT. RTE Act 2009 operationalizes the child's Right under Art 21A and the parent's Duty under Art 51A(k).",
            "ta": "கூற்றுகள் 1 மற்றும் 2 இரண்டும் சரியானவை. RTE சட்டம் 2009 உறுப்பு 21A-ன் கீழ் બાળக்கின் உரிமையையும் உறுப்பு 51A(k)-ன் கீழ் பெற்றோர் கடமையையும் செயல்படுத்துகிறது."
        },
        "why_not_others": {
            "A": {"en": "Statement 2 is also correct.", "ta": "கூற்று 2-ம் சரியானது."},
            "B": {"en": "Statement 1 is also correct.", "ta": "கூற்று 1-ம் சரியானது."},
            "C": {"en": "Correct. Both statements 1 and 2 are correct.", "ta": "சரி. கூற்றுகள் 1 மற்றும் 2 இரண்டும் சரியானவை."},
            "D": {"en": "Both statements are true.", "ta": "இரண்டு கூற்றுகளும் உண்மை."}
        },
        "tnpsc_tip": {
            "en": "RTE Act 2009 bridges Article 21A (FR) and Article 51A(k) (FD).",
            "ta": "RTE சட்டம் 2009 உறுப்பு 21A (FR) மற்றும் உறுப்பு 51A(k) (FD) ஆகியவற்றை இணைக்கிறது."
        }
    },
    {
        "id": "FD_S_047",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Statement",
        "question": {
            "en": "Consider the following statements regarding the 42nd Amendment Act, 1976:\n1. It added Part IVA to the Constitution.\n2. It added Article 51A enumerating 10 Fundamental Duties.\n3. It added Article 48A to Part IV (Protection of Environment).\nWhich of the statements given above are CORRECT?",
            "ta": "1976-ன் 42வது திருத்தச் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. இது அரசியலமைப்பில் பகுதி IVA-ஐச் சேர்த்தது.\n2. இது 10 அடிப்படை கடமைகளைப் பட்டியலிடும் உறுப்பு 51A-ஐச் சேர்த்தது.\n3. இது பகுதி IV-ல் உறுப்பு 48A-ஐச் (சுற்றுச்சூழல் பாதுகாப்பு) சேர்த்தது.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 and 2 only", "ta": "1 மற்றும் 2 மட்டும்"},
            {"id": "B", "en": "2 and 3 only", "ta": "2 மற்றும் 3 மட்டும்"},
            {"id": "C", "en": "1 and 3 only", "ta": "1 மற்றும் 3 மட்டும்"},
            {"id": "D", "en": "1, 2 and 3", "ta": "1, 2 மற்றும் 3"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "All three statements are CORRECT. The 42nd CAA 1976 added Part IVA (Art 51A) as well as DPSP Art 48A.",
            "ta": "மூன்று கூற்றுகளும் சரியானவை. 42வது திருத்தச் சட்டம் 1976 பகுதி IVA (உறுப்பு 51A) மற்றும் DPSP உறுப்பு 48A ஆகிய இரண்டையும் சேர்த்தது."
        },
        "why_not_others": {
            "A": {"en": "Statement 3 is also correct.", "ta": "கூற்று 3-ம் சரியானது."},
            "B": {"en": "Statement 1 is also correct.", "ta": "கூற்று 1-ம் சரியானது."},
            "C": {"en": "Statement 2 is also correct.", "ta": "கூற்று 2-ம் சரியானது."},
            "D": {"en": "Correct. All statements 1, 2, and 3 are correct.", "ta": "சரி. 1, 2 மற்றும் 3 ஆகிய அனைத்துக் கூற்றுகளும் சரி."}
        },
        "tnpsc_tip": {
            "en": "42nd CAA 1976 is often called the 'Mini-Constitution' due to extensive additions.",
            "ta": "விரிவான சேர்க்கைகள் காரணமாக 42வது திருத்தம் 1976 பெரும்பாலும் 'குறு-அரசியலமைப்பு' என அழைக்கப்படுகிறது."
        }
    },
    {
        "id": "FD_S_048",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Hard",
        "question_type": "Assertion & Reason",
        "question": {
            "en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Fundamental Duties in Article 51A do not extend to foreign nationals residing in India.\nReason (R): Political allegiance to the Republic of India is a constitutional prerequisite for the imposition of Fundamental Duties.\nIn the context of the above statements, which one of the following is correct?",
            "ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): உறுப்பு 51A-ல் உள்ள அடிப்படை கடமைகள் இந்தியாவில் வசிக்கும் வெளிநாட்டு குடிமக்களுக்கு விரிவாக்கப்படவில்லை.\nகாரணம் (R): இந்தியக் குடியரசிற்கான அரசியல் விசுவாசமே அடிப்படை கடமைகளை விதிப்பதற்கான அரசியலமைப்பு முன்நிபந்தனையாகும்.\nமேற்கண்ட கூற்றுகளின் அடிப்படையில் பின்வருவனவற்றில் எது சரியானது?"
        },
        "options": [
            {"id": "A", "en": "Both A and R are correct and R is the correct explanation of A", "ta": "A மற்றும் R ஆகிய இரண்டும் சரி, மேலும் R என்பது A-வின் சரியான விளக்கமாகும்"},
            {"id": "B", "en": "Both A and R are correct but R is NOT the correct explanation of A", "ta": "A மற்றும் R ஆகிய இரண்டும் சரி, ஆனால் R என்பது A-வின் சரியான விளக்கம் அல்ல"},
            {"id": "C", "en": "A is correct but R is incorrect", "ta": "A சரி ஆனால் R தவறு"},
            {"id": "D", "en": "A is incorrect but R is correct", "ta": "A தவறு ஆனால் R சரி"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Both A and R are true. Reason R accurately explains why Assertion A is true: duties bind citizens because citizenship entails political allegiance to the Indian Nation.",
            "ta": "A மற்றும் R ஆகிய இரண்டும் உண்மை. ஏன் கூற்று A உண்மை என்பதை காரணம் R சரியாக விளக்குகிறது: குடியுரிமை என்பது இந்திய தேசத்திற்கான அரசியல் விசுவாசத்தைக் குறிப்பதால் கடமைகள் குடிமக்களைக் கட்டுப்படுத்துகின்றன."
        },
        "why_not_others": {
            "A": {"en": "Correct. R directly explains Assertion A.", "ta": "சரி. R நேரடியாகக் கூற்று A-வை விளக்குகிறது."},
            "B": {"en": "R is the direct explanation of A.", "ta": "R என்பது A-விற்கான நேரடி விளக்கமாகும்."},
            "C": {"en": "R is true.", "ta": "R உண்மையாகும்."},
            "D": {"en": "A is true.", "ta": "A உண்மையாகும்."}
        },
        "tnpsc_tip": {
            "en": "Citizenship + Allegiance = Applicability of Article 51A Duties.",
            "ta": "குடியுரிமை + விசுவாசம் = உறுப்பு 51A கடமைகளின் பயன்பாடு."
        }
    },
    {
        "id": "FD_S_049",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Hard",
        "question_type": "Statement",
        "question": {
            "en": "Consider the following statements regarding Supreme Court guidelines in Destruction of Public Properties case (2009):\n1. High Courts can take suo motu cognisance of public property destruction during violent strikes.\n2. Courts can appoint Claims Commissioners to assess damages.\n3. Financial damages can be recovered directly from protest organizers to enforce Article 51A(i).\nWhich of the statements given above are CORRECT?",
            "ta": "பொதுச் சொத்துக்கள் சேத வழக்கில் (2009) உச்ச நீதிமன்ற வழிகாட்டுதல்கள் பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. வன்முறைப் போராட்டங்களின் போது பொதுச் சொத்து சேதமடைவது குறித்து உயர் நீதிமன்றங்கள் தாமாக முன்வந்து வழக்குப்பதிவு செய்யலாம்.\n2. சேதங்களை மதிப்பிட நீதிமன்றங்கள் உரிமைகோரல் ஆணையர்களை நியமிக்கலாம்.\n3. உறுப்பு 51A(i)-ஐ அமல்படுத்தப் போராட்ட அமைப்பாளர்களிடமிருந்து நிதி இழப்பீட்டை நேரடியாக வசூலிக்கலாம்.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 and 2 only", "ta": "1 மற்றும் 2 மட்டும்"},
            {"id": "B", "en": "2 and 3 only", "ta": "2 மற்றும் 3 மட்டும்"},
            {"id": "C", "en": "1 and 3 only", "ta": "1 மற்றும் 3 மட்டும்"},
            {"id": "D", "en": "1, 2 and 3", "ta": "1, 2 மற்றும் 3"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "All three statements are CORRECT guidelines issued by Supreme Court in 2009 relying on Article 51A(i).",
            "ta": "மூன்று கூற்றுகளும் உறுப்பு 51A(i)-ஐச் சார்ந்து 2009-ல் உச்ச நீதிமன்றத்தால் வெளியிடப்பட்ட சரியான வழிகாட்டுதல்கள் ஆகும்."
        },
        "why_not_others": {
            "A": {"en": "Statement 3 is also correct.", "ta": "கூற்று 3-ம் சரியானது."},
            "B": {"en": "Statement 1 is also correct.", "ta": "கூற்று 1-ம் சரியானது."},
            "C": {"en": "Statement 2 is also correct.", "ta": "கூற்று 2-ம் சரியானது."},
            "D": {"en": "Correct. All statements 1, 2, and 3 are correct.", "ta": "சரி. 1, 2 மற்றும் 3 ஆகிய அனைத்துக் கூற்றுகளும் சரி."}
        },
        "tnpsc_tip": {
            "en": "SC 2009 guidelines rely on Art 51A(i) to recover protest damages from organizers.",
            "ta": "உச்ச நீதிமன்ற 2009 வழிகாட்டுதல்கள் அமைப்பாளர்களிடமிருந்து போராட்ட இழப்பீட்டை வசூலிக்க உறுப்பு 51A(i)-ஐச் சார்ந்திருக்கின்றன."
        }
    },
    {
        "id": "FD_S_050",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Hard",
        "question_type": "Statement",
        "question": {
            "en": "Consider the following statements regarding the harmonious synthesis of Part III, Part IV, and Part IVA:\n1. Fundamental Rights provide political democracy, Directive Principles provide socio-economic democracy, and Fundamental Duties provide civic discipline.\n2. All three Parts must be read together to achieve the constitutional vision stated in the Preamble.\nWhich of the statements given above is/are CORRECT?",
            "ta": "பகுதி III, பகுதி IV, மற்றும் பகுதி IVA ஆகியவைகளின் இணக்கமான இணைப்பு பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. அடிப்படை உரிமைகள் அரசியல் ஜனநாயகத்தையும், வழிகாட்டு நெறிமுறைகள் சமூக-பொருளாதார ஜனநாயகத்தையும், அடிப்படை கடமைகள் குடிமை ஒழுக்கத்தையும் வழங்குகின்றன.\n2. முகப்புரையில் கூறப்பட்டுள்ள அரசியலமைப்புப் பார்வையை அடைய மூன்று பகுதிகளையும் இணைத்தே படிக்க வேண்டும்.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 only", "ta": "1 மட்டுமே"},
            {"id": "B", "en": "2 only", "ta": "2 மட்டுமே"},
            {"id": "C", "en": "Both 1 and 2", "ta": "1 மற்றும் 2 இரண்டும்"},
            {"id": "D", "en": "Neither 1 nor 2", "ta": "1-ம் இல்லை 2-ம் இல்லை"}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "Both statements 1 and 2 are CORRECT. They summarize the complete Indian constitutional philosophy synthesizing Rights, DPSPs, and Fundamental Duties.",
            "ta": "கூற்றுகள் 1 மற்றும் 2 இரண்டும் சரியானவை. அவை உரிமைகள், DPSP-கள், மற்றும் அடிப்படை கடமைகளை இணைக்கும் முழுமையான இந்திய அரசியலமைப்புத் தத்துவத்தைச் சுருக்கமாகக் கூறுகின்றன."
        },
        "why_not_others": {
            "A": {"en": "Statement 2 is also correct.", "ta": "கூற்று 2-ம் சரியானது."},
            "B": {"en": "Statement 1 is also correct.", "ta": "கூற்று 1-ம் சரியானது."},
            "C": {"en": "Correct. Both statements 1 and 2 are correct.", "ta": "சரி. கூற்றுகள் 1 மற்றும் 2 இரண்டும் சரியானவை."},
            "D": {"en": "Both statements are true.", "ta": "இரண்டு கூற்றுகளும் உண்மை."}
        },
        "tnpsc_tip": {
            "en": "Part III + Part IV + Part IVA = Complete Indian Constitutional Democracy.",
            "ta": "பகுதி III + பகுதி IV + பகுதி IVA = முழுமையான இந்திய அரசியலமைப்பு ஜனநாயகம்."
        }
    }
]

target_file = "data/questions/polity/fundamental_duties_statement.json"
os.makedirs(os.path.dirname(target_file), exist_ok=True)

with open(target_file, "w", encoding="utf-8") as f:
    json.dump(questions_data, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {len(questions_data)} Statement questions in {target_file}")
