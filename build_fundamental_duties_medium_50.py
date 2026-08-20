# -*- coding: utf-8 -*-
"""
Script to build 50 High-Yield Medium MCQs for Fundamental Duties
Target File: data/questions/polity/fundamental_duties_medium.json
"""

import json
import os

questions_data = [
    {
        "id": "FD_M_001",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Statement-based",
        "question": {
            "en": "Consider the following statements regarding the legal nature of Fundamental Duties under Part IVA of the Constitution of India:\n1. Fundamental Duties are non-justiciable and cannot be directly enforced by courts through writs.\n2. Fundamental Duties apply to all persons residing in India, including foreign tourists and non-citizens.\nWhich of the statements given above is/are correct?",
            "ta": "இந்திய அரசியலமைப்பின் பகுதி IVA-ன் கீழ் உள்ள அடிப்படை கடமைகளின் சட்டப்பூர்வ இயல்பு பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. அடிப்படை கடமைகள் நீதிமன்றங்களால் நேரடியாகப் பேராணைகள் மூலம் அமல்படுத்த முடியாதவை.\n2. அடிப்படை கடமைகள் வெளிநாட்டு சுற்றுலாப் பயணிகள் உட்பட இந்தியாவில் வசிக்கும் அனைத்து நபர்களுக்கும் பொருந்தும்.\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 only", "ta": "1 மட்டும்"},
            {"id": "B", "en": "2 only", "ta": "2 மட்டும்"},
            {"id": "C", "en": "Both 1 and 2", "ta": "1 மற்றும் 2 ஆகிய இரண்டும்"},
            {"id": "D", "en": "Neither 1 nor 2", "ta": "1 மற்றும் 2 ஆகிய இரண்டும் இல்லை"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Statement 1 is correct: Fundamental Duties are non-justiciable in court without enabling statutes. Statement 2 is incorrect: Article 51A duties apply EXCLUSIVELY to Citizens of India, not to foreigners.",
            "ta": "கூற்று 1 சரி: சட்டப்பூர்வ ஆதரவு இன்றி அடிப்படை கடமைகள் நீதிமன்றங்களால் நேரடியாக அமல்படுத்த முடியாதவை. கூற்று 2 தவறு: உறுப்பு 51A கடமைகள் இந்தியக் குடிமக்களுக்கு மட்டுமே பொருந்தும், வெளிநாட்டினருக்கு அல்ல."
        },
        "why_not_others": {
            "A": {"en": "Correct. Statement 1 is correct, while Statement 2 is incorrect.", "ta": "சரி. கூற்று 1 சரி, கூற்று 2 தவறு."},
            "B": {"en": "Statement 2 is wrong because duties do not apply to foreigners.", "ta": "கடமைகள் வெளிநாட்டினருக்குப் பொருந்தாததால் கூற்று 2 தவறு."},
            "C": {"en": "Statement 2 is false.", "ta": "கூற்று 2 தவறானது."},
            "D": {"en": "Statement 1 is factually true.", "ta": "கூற்று 1 உண்மையாகும்."}
        },
        "tnpsc_tip": {
            "en": "Always remember: Fundamental Duties in Art 51A are restricted EXCLUSIVELY to Citizens.",
            "ta": "எப்போதும் நினைவில் கொள்க: உறுப்பு 51A-ல் உள்ள அடிப்படை கடமைகள் குடிமக்களுக்கு மட்டுமே பொருந்தும்."
        }
    },
    {
        "id": "FD_M_002",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Assertion & Reason",
        "question": {
            "en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Article 51A(g) and Article 48A together form a harmonious constitutional framework for environmental protection.\nReason (R): Article 48A imposes a directive duty on the State, while Article 51A(g) imposes a Fundamental Duty on every citizen to protect and improve the natural environment.\nIn the context of the above statements, which one of the following is correct?",
            "ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): உறுப்பு 51A(g) மற்றும் உறுப்பு 48A ஆகியவை இணைந்து சுற்றுச்சூழல் பாதுகாப்பிற்கான இணக்கமான அரசியலமைப்பு கட்டமைப்பை உருவாக்குகின்றன.\nகாரணம் (R): உறுப்பு 48A அரசுக்கு வழிகாட்டு கடமையை விதிக்கிறது, அதே வேளையில் உறுப்பு 51A(g) இயற்கை சுற்றுச்சூழலைப் பாதுகாத்து மேம்படுத்த ஒவ்வொரு குடிமகனுக்கும் அடிப்படை கடமையை விதிக்கிறது.\nமேற்கண்ட கூற்றுகளின் அடிப்படையில் பின்வருவனவற்றில் எது சரியானது?"
        },
        "options": [
            {"id": "A", "en": "Both A and R are correct and R is the correct explanation of A", "ta": "A மற்றும் R ஆகிய இரண்டும் சரி, மேலும் R என்பது A-வின் சரியான விளக்கமாகும்"},
            {"id": "B", "en": "Both A and R are correct but R is NOT the correct explanation of A", "ta": "A மற்றும் R ஆகிய இரண்டும் சரி, ஆனால் R என்பது A-வின் சரியான விளக்கம் அல்ல"},
            {"id": "C", "en": "A is correct but R is incorrect", "ta": "A சரி ஆனால் R தவறு"},
            {"id": "D", "en": "A is incorrect but R is correct", "ta": "A தவறு ஆனால் R சரி"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Both A and R are true. Article 48A obligates the State (DPSP) and Article 51A(g) obligates citizens (FD), together creating a dual constitutional environment framework as explained in R.",
            "ta": "A மற்றும் R ஆகிய இரண்டும் உண்மை. உறுப்பு 48A அரசைப் பொறுப்பாக்குகிறது (DPSP) மற்றும் உறுப்பு 51A(g) குடிமக்களைப் பொறுப்பாக்குகிறது (FD), இரண்டும் இணைந்து இரட்டை அரசியலமைப்பு சுற்றுச்சூழல் கட்டமைப்பை உருவாக்குகிறது."
        },
        "why_not_others": {
            "A": {"en": "Correct. R correctly explains why A forms a harmonious framework.", "ta": "சரி. R ஏன் A இணக்கமான கட்டமைப்பை உருவாக்குகிறது என்பதைச் சரியாக விளக்குகிறது."},
            "B": {"en": "R is indeed the direct reason for A.", "ta": "R என்பது A-விற்கான நேரடிக் காரணமாகும்."},
            "C": {"en": "R is completely correct.", "ta": "R முற்றிலும் சரியானது."},
            "D": {"en": "A is true.", "ta": "A உண்மையாகும்."}
        },
        "tnpsc_tip": {
            "en": "Both 48A and 51A(g) were introduced together by the 42nd Amendment Act 1976.",
            "ta": "48A மற்றும் 51A(g) ஆகிய இரண்டும் 1976-ன் 42வது திருத்தச் சட்டத்தின் மூலம் ஒன்றாக அறிமுகப்படுத்தப்பட்டன."
        }
    },
    {
        "id": "FD_M_003",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Conceptual Comparison",
        "question": {
            "en": "Consider the following statements regarding the Education Triad in the Constitution of India:\n1. Article 21A makes free and compulsory education for 6-14 age group a justiciable Fundamental Right of the child against the State.\n2. Article 45 directs the State to provide early childhood care and education for children below six years of age.\n3. Article 51A(k) places a Fundamental Duty on parents or guardians to provide education opportunities to their child aged 6 to 14 years.\nWhich of the statements given above are correct?",
            "ta": "இந்திய அரசியலமைப்பில் உள்ள கல்வி முக்கோணம் பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. உறுப்பு 21A 6-14 வயதுக் குழுவினருக்கு அரசுக்கு எதிராக இலவச கட்டாயக் கல்வியை அமல்படுத்தக்கூடிய அடிப்படை உரிமையாக மாற்றுகிறது.\n2. உறுப்பு 45 6 வயதிற்குட்பட்ட குழந்தைகளுக்கு முன்பருவப் பராமரிப்பு மற்றும் கல்வியை வழங்க அரசுக்கு வழிகாட்டுகிறது.\n3. உறுப்பு 51A(k) 6 முதல் 14 வயது வரையிலான தங்கள் குழந்தைக்குக் கல்வி வாய்ப்புகளை வழங்கப் பெற்றோர் அல்லது பாதுகாவலர்கள் மீது அடிப்படை கடமையை விதிக்கிறது.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 and 2 only", "ta": "1 மற்றும் 2 மட்டும்"},
            {"id": "B", "en": "2 and 3 only", "ta": "2 மற்றும் 3 மட்டும்"},
            {"id": "C", "en": "1 and 3 only", "ta": "1 மற்றும் 3 மட்டும்"},
            {"id": "D", "en": "1, 2 and 3", "ta": "1, 2 மற்றும் 3"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "All three statements are correct. The 86th CAA 2002 structured education across Part III (Art 21A - FR), Part IV (Art 45 - DPSP), and Part IVA (Art 51A(k) - FD).",
            "ta": "மூன்று கூற்றுகளும் சரியானவை. 86வது திருத்தம் 2002 கல்வியைப் பகுதி III (உறுப்பு 21A - FR), பகுதி IV (உறுப்பு 45 - DPSP), மற்றும் பகுதி IVA (உறுப்பு 51A(k) - FD) முழுவதும் கட்டமைத்தது."
        },
        "why_not_others": {
            "A": {"en": "Statement 3 is also correct.", "ta": "கூற்று 3-ம் சரியானது."},
            "B": {"en": "Statement 1 is also correct.", "ta": "கூற்று 1-ம் சரியானது."},
            "C": {"en": "Statement 2 is also correct.", "ta": "கூற்று 2-ம் சரியானது."},
            "D": {"en": "Correct. All 1, 2 and 3 statements are true.", "ta": "சரி. 1, 2 மற்றும் 3 ஆகிய அனைத்துக் கூற்றுகளும் உண்மை."}
        },
        "tnpsc_tip": {
            "en": "All three provisions were amended/inserted simultaneously by the 86th Amendment Act, 2002.",
            "ta": "மூன்று விதிகளும் 2002-ன் 86வது திருத்தச் சட்டத்தால் ஒரே நேரத்தில் திருத்தப்பட்டன/சேர்க்கப்பட்டன."
        }
    },
    {
        "id": "FD_M_004",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Statement-based",
        "question": {
            "en": "With reference to the Swaran Singh Committee (1976) recommendations on Fundamental Duties, consider the following statements:\n1. The Committee recommended the inclusion of 8 Fundamental Duties in the Constitution.\n2. The Committee recommended that Parliament should prescribe penalties or punishment for non-compliance with any Fundamental Duty.\n3. The recommendation to impose a 'Duty to pay taxes' was accepted by Parliament and incorporated into Article 51A.\nWhich of the statements given above is/are correct?",
            "ta": "அடிப்படை கடமைகள் பற்றிய ஸ்வரன் சிங் குழுவின் (1976) பரிந்துரைகளைக் குறிப்பிட்டு, பின்வரும் கூற்றுகளை ஆராய்க:\n1. அத்தியாயத்தில் 8 அடிப்படை கடமைகளைச் சேர்க்கக் குழு பரிந்துரைத்தது.\n2. எந்தவொரு அடிப்படை கடமையையும் மீறுவதற்கு நாடாளுமன்றம் அபராதம் அல்லது தண்டனையை விதிக்க வேண்டும் என்று குழு பரிந்துரைத்தது.\n3. 'வரி செலுத்தும் கடமை'யை விதிக்கும் பரிந்துரை நாடாளுமன்றத்தால் ஏற்றுக்கொள்ளப்பட்டு உறுப்பு 51A-ல் சேர்க்கப்பட்டது.\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 and 2 only", "ta": "1 மற்றும் 2 மட்டும்"},
            {"id": "B", "en": "1 and 3 only", "ta": "1 மற்றும் 3 மட்டும்"},
            {"id": "C", "en": "2 and 3 only", "ta": "2 மற்றும் 3 மட்டும்"},
            {"id": "D", "en": "1, 2 and 3", "ta": "1, 2 மற்றும் 3"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Statements 1 and 2 are correct. Statement 3 is incorrect because Parliament REJECTED the recommendation to include 'Duty to pay taxes' under Article 51A.",
            "ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறு, ஏனெனில் உறுப்பு 51A-ன் கீழ் 'வரி செலுத்தும் கடமை'யைச் சேர்க்கும் பரிந்துரையை நாடாளுமன்றம் நிராகரித்தது."
        },
        "why_not_others": {
            "A": {"en": "Correct. Statements 1 and 2 are true, while 3 is false.", "ta": "சரி. கூற்றுகள் 1 மற்றும் 2 உண்மை, கூற்று 3 தவறு."},
            "B": {"en": "Statement 3 is incorrect.", "ta": "கூற்று 3 தவறானது."},
            "C": {"en": "Statement 3 is incorrect.", "ta": "கூற்று 3 தவறானது."},
            "D": {"en": "Statement 3 is false.", "ta": "கூற்று 3 தவறானது."}
        },
        "tnpsc_tip": {
            "en": "Swaran Singh Committee recommended 8 duties and penalties for non-compliance, but Parliament enacted 10 duties WITHOUT automatic penalties.",
            "ta": "ஸ்வரன் சிங் குழு 8 கடமைகளையும் தண்டனைகளையும் பரிந்துரைத்தது, ஆனால் நாடாளுமன்றம் தானியங்கி தண்டனைகள் இன்றி 10 கடமைகளை இயற்றியது."
        }
    },
    {
        "id": "FD_M_005",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Article-based",
        "question": {
            "en": "Which of the following pairs of Article 51A clauses and their core constitutional mandates is INCORRECTLY matched?",
            "ta": "உறுப்பு 51A உட்பிரிவுகள் மற்றும் அவற்றின் முதன்மை அரசியலமைப்புக் கட்டளைகளில் பின்வரும் எந்த ஜோடி தவறாகப் பொருந்தியுள்ளது?"
        },
        "options": [
            {"id": "A", "en": "Article 51A(a) – Abide by Constitution, respect Flag and Anthem", "ta": "உறுப்பு 51A(a) – அரசியலமைப்புக்குக் கீழ்ப்படிதல், கொடி மற்றும் கீதத்தை மதித்தல்"},
            {"id": "B", "en": "Article 51A(c) – Uphold and protect Sovereignty, Unity and Integrity of India", "ta": "உறுப்பு 51A(c) – இந்தியாவின் இறையாண்மை, ஒற்றுமை மற்றும் ஒருமைப்பாட்டைப் பேணிப் பாதுகாத்தல்"},
            {"id": "C", "en": "Article 51A(e) – Protect and improve forests, lakes, rivers, and wildlife", "ta": "உறுப்பு 51A(e) – காடுகள், ஏரிகள், ஆறுகள் மற்றும் வனவிலங்குகளைப் பாதுகாத்து மேம்படுத்துதல்"},
            {"id": "D", "en": "Article 51A(d) – Defend the country and render national service when called upon", "ta": "உறுப்பு 51A(d) – தேசத்தைப் பாதுகாத்தல் மற்றும் தேவைப்படும்போது தேசிய சேவை ஆற்றுதல்"}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "Pair C is INCORRECTLY matched. Protecting environment, forests, lakes, rivers, and wildlife is under Article 51A(g), NOT Article 51A(e) [which deals with Brotherhood and Women's dignity].",
            "ta": "ஜோடி C தவறாகப் பொருந்தியுள்ளது. சுற்றுச்சூழல், காடுகள், ஏரிகள், ஆறுகள், வனவிலங்குகளைப் பாதுகாப்பது உறுப்பு 51A(g)-ல் உள்ளது, உறுப்பு 51A(e)-ல் அல்ல [இது சகோதரத்துவம் மற்றும் பெண்கள் கண்ணியம் பற்றியது]."
        },
        "why_not_others": {
            "A": {"en": "Pair A is correctly matched.", "ta": "ஜோடி A சரியாகப் பொருந்தியுள்ளது."},
            "B": {"en": "Pair B is correctly matched.", "ta": "ஜோடி B சரியாகப் பொருந்தியுள்ளது."},
            "C": {"en": "Correct response. 51A(e) is for Brotherhood; 51A(g) is for Environment.", "ta": "சரி. 51A(e) சகோதரத்துவத்திற்கு; 51A(g) சுற்றுச்சூழலுக்கு."},
            "D": {"en": "Pair D is correctly matched.", "ta": "ஜோடி D சரியாகப் பொருந்தியுள்ளது."}
        },
        "tnpsc_tip": {
            "en": "Memorize the clause letters: (a) Symbols, (c) Sovereignty, (d) Defence, (e) Brotherhood, (g) Environment.",
            "ta": "உட்பிரிவு எழுத்துகளை நினைவில் கொள்க: (a) சின்னங்கள், (c) இறையாண்மை, (d) பாதுகாப்பு, (e) சகோதரத்துவம், (g) சுற்றுச்சூழல்."
        }
    },
    {
        "id": "FD_E_006_M",
        "id_override": "FD_M_006",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Statement-based",
        "question": {
            "en": "Consider the following statements regarding the 86th Constitutional Amendment Act, 2002:\n1. It added the 11th Fundamental Duty under Article 51A(k).\n2. It made free and compulsory education for children aged 6 to 14 years a Fundamental Right under Article 21A.\n3. It substituted the language of Article 45 DPSP to focus on early childhood care for children below six years.\nWhich of the statements given above are correct?",
            "ta": "2002-ன் 86வது அரசியலமைப்பு திருத்தச் சட்டம் பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. இது உறுப்பு 51A(k)-ன் கீழ் 11வது அடிப்படை கடமையைச் சேர்த்தது.\n2. இது 6 முதல் 14 வயது வரையிலான குழந்தைகளுக்கு இலவச கட்டாயக் கல்வியை உறுப்பு 21A-ன் கீழ் அடிப்படை உரிமையாக்கியது.\n3. இது 6 வயதிற்குட்பட்ட குழந்தைகளுக்கான முன்பருவப் பராமரிப்பில் கவனம் செலுத்த உறுப்பு 45 DPSP-ன் உரையை மாற்றியது.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 and 2 only", "ta": "1 மற்றும் 2 மட்டும்"},
            {"id": "B", "en": "2 and 3 only", "ta": "2 மற்றும் 3 மட்டும்"},
            {"id": "C", "en": "1 and 3 only", "ta": "1 மற்றும் 3 மட்டும்"},
            {"id": "D", "en": "1, 2 and 3", "ta": "1, 2 மற்றும் 3"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "All three statements are correct. The 86th CAA 2002 simultaneously amended Part III (Art 21A), Part IV (Art 45), and Part IVA (Art 51A(k)).",
            "ta": "மூன்று கூற்றுகளும் சரியானவை. 86வது திருத்தம் 2002 ஒரே நேரத்தில் பகுதி III (உறுப்பு 21A), பகுதி IV (உறுப்பு 45), மற்றும் பகுதி IVA (உறுப்பு 51A(k)) ஆகியவற்றைத் திருத்தியது."
        },
        "why_not_others": {
            "A": {"en": "Statement 3 is also true.", "ta": "கூற்று 3-ம் உண்மையாகும்."},
            "B": {"en": "Statement 1 is also true.", "ta": "கூற்று 1-ம் உண்மையாகும்."},
            "C": {"en": "Statement 2 is also true.", "ta": "கூற்று 2-ம் உண்மையாகும்."},
            "D": {"en": "Correct. All statements 1, 2, and 3 are correct.", "ta": "சரி. 1, 2 மற்றும் 3 ஆகிய அனைத்துக் கூற்றுகளும் சரி."}
        },
        "tnpsc_tip": {
            "en": "86th CAA 2002 is the single most important amendment relating to educational rights and duties in India.",
            "ta": "86வது திருத்தம் 2002 இந்தியாவில் கல்வி உரிமைகள் மற்றும் கடமைகள் தொடர்பான மிக முக்கியமான திருத்தமாகும்."
        }
    },
    {
        "id": "FD_M_007",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Case Law",
        "question": {
            "en": "In Bijoe Emmanuel v. State of Kerala (1986), what specific principle was established by the Supreme Court regarding Article 51A(a) and the National Anthem?",
            "ta": "பிஜோய் இம்மானுவேல் vs கேரளா மாநிலம் (1986) வழக்கில், உறுப்பு 51A(a) மற்றும் தேசியக் கீதம் தொடர்பாக உச்ச நீதிமன்றத்தால் நிறுவப்பட்ட குறிப்பிட்ட தத்துவம் என்ன?"
        },
        "options": [
            {"id": "A", "en": "Every citizen must loudly sing the National Anthem whenever played in public", "ta": "பொதுவெளியில் இசைக்கப்படும் போதெல்லாம் ஒவ்வொரு குடிமகனும் உரத்த குரலில் தேசியக் கீதத்தைப் பாட வேண்டும்"},
            {"id": "B", "en": "Standing up respectfully during the National Anthem satisfies Article 51A(a), and remaining silent out of religious faith does not constitute disrespect", "ta": "தேசியக் கீதத்தின் போது மரியாதையுடன் எழுந்து நிற்பதே உறுப்பு 51A(a)-ஐப் பூர்த்தி செய்கிறது, மத நம்பிக்கையால் அமைதியாக இருப்பது அவமதிப்பாகாது"},
            {"id": "C", "en": "Playing National Anthem in cinema halls is a non-negotiable mandatory duty under Art 51A(a)", "ta": "திரையரங்குகளில் தேசியக் கீதத்தை இசைப்பது உறுப்பு 51A(a)-ன் கீழ் பேச்சுவார்த்தைக்கு இடமில்லாத கட்டாயக் கடமையாகும்"},
            {"id": "D", "en": "Article 51A(a) overrides Fundamental Rights under Articles 19 and 25", "ta": "உறுப்பு 51A(a) உறுப்புகள் 19 மற்றும் 25-ன் கீழ் உள்ள அடிப்படை உரிமைகளை மிஞ்சுகிறது"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "The Supreme Court held that standing up respectfully during National Anthem shows proper respect required by Art 51A(a). Silent standing due to religious conscience is protected under Arts 19(1)(a) & 25.",
            "ta": "தேசியக் கீதத்தின் போது மரியாதையுடன் எழுந்து நிற்பதே உறுப்பு 51A(a) கோரும் சரியான மரியாதையைக் காட்டுகிறது என உச்ச நீதிமன்றம் தீர்ப்பளித்தது. மத நம்பிக்கையால் அமைதியாக நிற்பது உறுப்புகள் 19(1)(a) & 25-ன் கீழ் பாதுகாக்கப்படுகிறது."
        },
        "why_not_others": {
            "A": {"en": "Singing loudly is not mandatory if standing respectfully.", "ta": "மரியாதையுடன் நிற்கும் போது உரக்கப் பாடுவது கட்டாயமில்லை."},
            "B": {"en": "Correct. Standing respectfully satisfies Art 51A(a).", "ta": "சரி. மரியாதையுடன் எழுந்து நிற்பதே உறுப்பு 51A(a)-ஐப் பூர்த்தி செய்கிறது."},
            "C": {"en": "Cinema hall mandatory playing was modified in Shyam Narayan Chouksey (2018).", "ta": "திரையரங்கக் கட்டாயம் 2018 ஷ்யாம் நாராயண் சௌக்சே வழக்கில் மாற்றப்பட்டது."},
            "D": {"en": "Duties do not override Fundamental Rights.", "ta": "கடமைகள் அடிப்படை உரிமைகளை மிஞ்சுவதில்லை."}
        },
        "tnpsc_tip": {
            "en": "Proper respect to National Anthem is shown by standing up, not necessarily singing.",
            "ta": "தேசியக் கீதத்திற்குச் சரியான மரியாதை என்பது எழுந்து நிற்பதன் மூலம் காட்டப்படுகிறதே தவிர, கட்டாயம் பாடுவதன் மூலம் அல்ல."
        }
    },
    {
        "id": "FD_M_008",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Assertion & Reason",
        "question": {
            "en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Courts can take assistance from Fundamental Duties while determining the 'reasonableness' of restrictions on Fundamental Rights under Article 19.\nReason (R): Non-justiciable constitutional provisions are legally relevant in statutory construction and constitutional interpretation.\nIn the context of the above statements, which one of the following is correct?",
            "ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): உறுப்பு 19-ன் கீழ் அடிப்படை உரிமைகள் மீதான கட்டுப்பாடுகளின் 'நியாயத் தன்மையை' நிர்ணயிக்கும் போது நீதிமன்றங்கள் அடிப்படை கடமைகளின் உதவியைப் பெறலாம்.\nகாரணம் (R): அமல்படுத்த முடியாத அரசியலமைப்பு விதிகள் சட்ட வரைவு விளக்கம் மற்றும் அரசியலமைப்பு விளக்கத்தில் சட்டப்பூர்வமாகத் தொடர்புடையவை.\nமேற்கண்ட கூற்றுகளின் அடிப்படையில் பின்வருவனவற்றில் எது சரியானது?"
        },
        "options": [
            {"id": "A", "en": "Both A and R are correct and R is the correct explanation of A", "ta": "A மற்றும் R ஆகிய இரண்டும் சரி, மேலும் R என்பது A-வின் சரியான விளக்கமாகும்"},
            {"id": "B", "en": "Both A and R are correct but R is NOT the correct explanation of A", "ta": "A மற்றும் R ஆகிய இரண்டும் சரி, ஆனால் R என்பது A-வின் சரியான விளக்கம் அல்ல"},
            {"id": "C", "en": "A is correct but R is incorrect", "ta": "A சரி ஆனால் R தவறு"},
            {"id": "D", "en": "A is incorrect but R is correct", "ta": "A தவறு ஆனால் R சரி"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Both A and R are true. Because non-justiciable duties are legally relevant for interpretation (R), courts rely on them to judge whether a law restricting Art 19 rights is 'reasonable' in public interest (A).",
            "ta": "A மற்றும் R ஆகிய இரண்டும் உண்மை. அமல்படுத்த முடியாத கடமைகள் விளக்கத்திற்குச் சட்டப்பூர்வமாகத் தொடர்புடையவை என்பதால் (R), உறுப்பு 19 உரிமைகளைக் கட்டுப்படுத்தும் சட்டம் பொது நலனில் 'நியாயமானதா' என்பதைத் தீர்மானிக்க நீதிமன்றங்கள் அவற்றைச் சார்ந்திருக்கின்றன (A)."
        },
        "why_not_others": {
            "A": {"en": "Correct. R is the exact legal foundation for A.", "ta": "சரி. R என்பது A-விற்கான சரியான சட்டப்பூர்வ அடித்தளமாகும்."},
            "B": {"en": "R directly explains A.", "ta": "R நேரடியாக A-வை விளக்குகிறது."},
            "C": {"en": "R is true.", "ta": "R உண்மையாகும்."},
            "D": {"en": "A is true.", "ta": "A உண்மையாகும்."}
        },
        "tnpsc_tip": {
            "en": "A law aiming to give effect to a Fundamental Duty is usually held 'reasonable' under Article 19.",
            "ta": "அடிப்படை கடமையை அமல்படுத்த முனையும் சட்டம் வழக்கமாக உறுப்பு 19-ன் கீழ் 'நியாயமானது' என நிலைநிறுத்தப்படும்."
        }
    },
    {
        "id": "FD_M_009",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Conceptual Comparison",
        "question": {
            "en": "Consider the following statements comparing Article 51A(f) with Articles 29 and 30:\n1. Articles 29 and 30 grant justiciable cultural and educational rights primarily to minority sections of citizens.\n2. Article 51A(f) imposes a Fundamental Duty on EVERY citizen to value and preserve the rich heritage of India's composite culture.\nWhich of the statements given above is/are correct?",
            "ta": "உறுப்பு 51A(f)-ஐ உறுப்புகள் 29 மற்றும் 30 உடன் ஒப்பிடும் பின்வரும் கூற்றுகளை ஆராய்க:\n1. உறுப்புகள் 29 மற்றும் 30 முதன்மையாகச் சிறுபான்மைப் பிரிவு குடிமக்களுக்கு அமல்படுத்தக்கூடிய பண்பாட்டு மற்றும் கல்வி உரிமைகளை வழங்குகின்றன.\n2. உறுப்பு 51A(f) ஒவ்வொரு குடிமகனுக்கும் இந்தியாவின் கூட்டுப் பண்பாட்டின் வளமான பாரம்பரியத்தை மதித்துப் பேண அடிப்படை கடமையை விதிக்கிறது.\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 only", "ta": "1 மட்டும்"},
            {"id": "B", "en": "2 only", "ta": "2 மட்டும்"},
            {"id": "C", "en": "Both 1 and 2", "ta": "1 மற்றும் 2 ஆகிய இரண்டும்"},
            {"id": "D", "en": "Neither 1 nor 2", "ta": "1 மற்றும் 2 ஆகிய இரண்டும் இல்லை"}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "Both statements 1 and 2 are correct. Arts 29-30 protect distinct minority cultures (FR), while Art 51A(f) mandates all citizens to preserve overall composite culture (FD).",
            "ta": "கூற்றுகள் 1 மற்றும் 2 ஆகிய இரண்டும் சரியானவை. உறுப்புகள் 29-30 சிறுபான்மைப் பண்பாட்டைப் பாதுகாக்கின்றன (FR), ஆனால் உறுப்பு 51A(f) அனைத்துக் குடிமக்களையும் கூட்டுப் பண்பாட்டைப் பேண ஆணையிடுகிறது (FD)."
        },
        "why_not_others": {
            "A": {"en": "Statement 2 is also true.", "ta": "கூற்று 2-ம் உண்மையாகும்."},
            "B": {"en": "Statement 1 is also true.", "ta": "கூற்று 1-ம் உண்மையாகும்."},
            "C": {"en": "Correct. Both statements 1 and 2 are correct.", "ta": "சரி. 1 மற்றும் 2 ஆகிய இரண்டு கூற்றுகளும் சரி."},
            "D": {"en": "Both statements are true.", "ta": "இரண்டு கூற்றுகளும் உண்மை."}
        },
        "tnpsc_tip": {
            "en": "Arts 29-30 are Right-conferring (Part III); Art 51A(f) is Duty-imposing (Part IVA).",
            "ta": "உறுப்புகள் 29-30 உரிமைகளை வழங்குபவை (பகுதி III); உறுப்பு 51A(f) கடமையை விதிப்பது (பகுதி IVA)."
        }
    },
    {
        "id": "FD_M_010",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Article-based",
        "question": {
            "en": "Which of the following natural elements are EXPLICITLY mentioned in the text of Article 51A(g)?\n1. Forests\n2. Lakes\n3. Rivers\n4. Wildlife\nSelect the correct answer using the code given below:",
            "ta": "உறுப்பு 51A(g)-ன் உரையில் பின்வரும் எந்த இயற்கை கூறுகள் வெளிப்படையாகக் குறிப்பிடப்பட்டுள்ளன?\n1. காடுகள்\n2. ஏரிகள்\n3. ஆறுகள்\n4. வனவிலங்குகள்\nகீழே கொடுக்கப்பட்டுள்ள குறியீட்டைப் பயன்படுத்தி சரியான பதிலைத் தேர்ந்தெடுக்கவும்:"
        },
        "options": [
            {"id": "A", "en": "1 and 4 only", "ta": "1 மற்றும் 4 மட்டும்"},
            {"id": "B", "en": "1, 3 and 4 only", "ta": "1, 3 மற்றும் 4 மட்டும்"},
            {"id": "C", "en": "2, 3 and 4 only", "ta": "2, 3 மற்றும் 4 மட்டும்"},
            {"id": "D", "en": "1, 2, 3 and 4", "ta": "1, 2, 3 மற்றும் 4"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "The exact constitutional text of Article 51A(g) explicitly names all four: 'forests, lakes, rivers and wild life, and to have compassion for living creatures.'",
            "ta": "உறுப்பு 51A(g)-ன் சரியான அரசியலமைப்பு உரை நான்கையும் வெளிப்படையாகப் பெயரிடுகிறது: 'காடுகள், ஏரிகள், ஆறுகள் மற்றும் வனவிலங்குகள், மற்றும் உயிரினங்கள் மீது கருணை காட்டுதல்.'"
        },
        "why_not_others": {
            "A": {"en": "Lakes and Rivers are also explicitly mentioned.", "ta": "ஏரிகள் மற்றும் ஆறுகளும் வெளிப்படையாகக் குறிப்பிடப்பட்டுள்ளன."},
            "B": {"en": "Lakes is omitted in this option.", "ta": "இந்த விருப்பத்தில் ஏரிகள் விடுவிக்கப்பட்டுள்ளது."},
            "C": {"en": "Forests is omitted in this option.", "ta": "இந்த விருப்பத்தில் காடுகள் விடுவிக்கப்பட்டுள்ளது."},
            "D": {"en": "Correct. All four elements (Forests, Lakes, Rivers, Wildlife) are explicitly listed.", "ta": "சரி. நான்கு கூறுகளும் (காடுகள், ஏரிகள், ஆறுகள், வனவிலங்குகள்) வெளிப்படையாகப் பட்டியலிடப்பட்டுள்ளன."}
        },
        "tnpsc_tip": {
            "en": "Memory acronym: FLRW (Forests, Lakes, Rivers, Wildlife) + Compassion for living creatures.",
            "ta": "நினைவுச் சொல்: FLRW (காடுகள், ஏரிகள், ஆறுகள், வனவிலங்குகள்) + உயிரினங்கள் மீது கருணை."
        }
    },
    {
        "id": "FD_M_011",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Article-based",
        "question": {
            "en": "Article 51A(h) commands citizens to develop four rational values. Which of the following is NOT one of those four values?",
            "ta": "உறுப்பு 51A(h) நான்கு பகுத்தறிவு மதிப்புகளை வளர்க்கக் குடிமக்களுக்கு ஆணையிடுகிறது. பின்வருவனவற்றில் எது அந்த நான்கு மதிப்புகளில் ஒன்று அல்ல?"
        },
        "options": [
            {"id": "A", "en": "Scientific Temper", "ta": "அறிவியல் மனப்பான்மை"},
            {"id": "B", "en": "Humanism", "ta": "மனிதநேயம்"},
            {"id": "C", "en": "Blind Dogmatism", "ta": "குருட்டு கோட்பாட்டுவாதம்"},
            {"id": "D", "en": "Spirit of Inquiry and Reform", "ta": "ஆராய்ச்சி மற்றும் சீர்திருத்த உணர்வு"}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "The four values under Article 51A(h) are: Scientific Temper, Humanism, Spirit of Inquiry, and Spirit of Reform. Blind Dogmatism is the exact opposite of scientific temper.",
            "ta": "உறுப்பு 51A(h)-ன் கீழ் உள்ள 4 மதிப்புகள்: அறிவியல் மனப்பான்மை, மனிதநேயம், ஆராய்ச்சி உணர்வு, மற்றும் சீர்திருத்த உணர்வு. குருட்டு கோட்பாட்டுவாதம் அறிவியல் மனப்பான்மைக்கு முற்றிலும் எதிரானது."
        },
        "why_not_others": {
            "A": {"en": "Scientific Temper is explicitly mentioned.", "ta": "அறிவியல் மனப்பான்மை வெளிப்படையாக உள்ளது."},
            "B": {"en": "Humanism is explicitly mentioned.", "ta": "மனிதநேயம் வெளிப்படையாக உள்ளது."},
            "C": {"en": "Correct. Blind Dogmatism is NOT in Art 51A(h).", "ta": "சரி. குருட்டு கோட்பாட்டுவாதம் உறுப்பு 51A(h)-ல் இல்லை."},
            "D": {"en": "Spirit of Inquiry and Reform is explicitly mentioned.", "ta": "ஆராய்ச்சி மற்றும் சீர்திருத்த உணர்வு வெளிப்படையாக உள்ளது."}
        },
        "tnpsc_tip": {
            "en": "Art 51A(h) is India's unique constitutional commitment to secular rationality and anti-superstition.",
            "ta": "உறுப்பு 51A(h) மதச்சார்பற்ற பகுத்தறிவு மற்றும் மூடநம்பிக்கை எதிர்ப்பிற்கான இந்தியாவின் தனித்துவமான அரசியலமைப்பு உறுதியாகும்."
        }
    },
    {
        "id": "FD_M_012",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Statement-based",
        "question": {
            "en": "Consider the following statements regarding Article 51A(i) and public property:\n1. Article 51A(i) obligates citizens to safeguard public property and to abjure violence.\n2. In 2009, the Supreme Court laid down guidelines allowing recovery of damages from organizers of violent bandhs/protests that destroy public property.\nWhich of the statements given above is/are correct?",
            "ta": "உறுப்பு 51A(i) மற்றும் பொதுச் சொத்து பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. உறுப்பு 51A(i) பொதுச் சொத்தைப் பாதுகாக்கவும் வன்முறையைக் கைவிடவும் குடிமக்களுக்குக் கடமையாக்குகிறது.\n2. 2009-ல், பொதுச் சொத்தைச் சேதப்படுத்தும் வன்முறை பந்த்கள்/போராட்ட அமைப்பாளர்களிடமிருந்து இழப்பீடு வசூலிக்க உச்ச நீதிமன்றம் வழிகாட்டுதல்களை வழங்கியது.\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 only", "ta": "1 மட்டும்"},
            {"id": "B", "en": "2 only", "ta": "2 மட்டும்"},
            {"id": "C", "en": "Both 1 and 2", "ta": "1 மற்றும் 2 ஆகிய இரண்டும்"},
            {"id": "D", "en": "Neither 1 nor 2", "ta": "1 மற்றும் 2 ஆகிய இரண்டும் இல்லை"}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "Both statements are correct. In Destruction of Public Properties, In re (2009), SC invoked Art 51A(i) to authorize recovery of damages from violent protesters.",
            "ta": "இரண்டு கூற்றுகளும் சரியானவை. பொதுச் சொத்துக்கள் சேதம் தொடர்பான 2009 வழக்கில், வன்முறைப் போராளிகளிடமிருந்து இழப்பீடு வசூலிக்க உறுப்பு 51A(i)-ஐ உச்ச நீதிமன்றம் பயன்படுத்தியது."
        },
        "why_not_others": {
            "A": {"en": "Statement 2 is also correct.", "ta": "கூற்று 2-ம் சரியானது."},
            "B": {"en": "Statement 1 is also correct.", "ta": "கூற்று 1-ம் சரியானது."},
            "C": {"en": "Correct. Both statements 1 and 2 are correct.", "ta": "சரி. 1 மற்றும் 2 ஆகிய இரண்டு கூற்றுகளும் சரி."},
            "D": {"en": "Both statements are true.", "ta": "இரண்டு கூற்றுகளும் உண்மை."}
        },
        "tnpsc_tip": {
            "en": "Damage to public property during strikes is punishable under PDPP Act 1984, backed by Art 51A(i).",
            "ta": "வேலைநிறுத்தங்களின் போது பொதுச் சொத்து சேதம் PDPP சட்டம் 1984-ன் கீழ் தண்டனைக்குரியது, இது உறுப்பு 51A(i) ஆல் ஆதரிக்கப்படுகிறது."
        }
    },
    {
        "id": "FD_M_013",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Conceptual Distinction",
        "question": {
            "en": "Article 51A(j) commands striving towards excellence in both individual and collective activity. What is the stated constitutional purpose of this duty?",
            "ta": "உறுப்பு 51A(j) தனிநபர் மற்றும் கூட்டுச் செயல்பாடுகள் இரண்டிலும் சிறப்பினை நோக்கி முயல ஆணையிடுகிறது. இக்கடமையின் குறிப்பிடப்பட்ட அரசியலமைப்பு நோக்கம் என்ன?"
        },
        "options": [
            {"id": "A", "en": "So that India can win maximum gold medals in the Olympic Games", "ta": "இந்தியா ஒலிம்பிக் போட்டிகளில் அதிகபட்ச தங்கப் பதக்கங்களை வெல்வதற்காக"},
            {"id": "B", "en": "So that the nation constantly rises to higher levels of endeavor and achievement", "ta": "தேசம் தொடர்ச்சியாக முயற்சி மற்றும் சாதனைகளின் உயர் நிலைகளுக்கு உயர்வதற்காக"},
            {"id": "C", "en": "So that all private companies achieve maximum profit tax revenue", "ta": "அனைத்துத் தனியார் நிறுவனங்களும் அதிகபட்ச லாப வரி வருவாயைப் பெறுவதற்காக"},
            {"id": "D", "en": "So that civil servants receive rapid promotion", "ta": "அரசு ஊழியர்கள் விரைவான உயர்வைப் பெறுவதற்காக"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "The exact constitutional text of Article 51A(j) ends with the purpose: 'so that the nation constantly rises to higher levels of endeavour and achievement.'",
            "ta": "உறுப்பு 51A(j)-ன் சரியான அரசியலமைப்பு உரை நோக்கத்துடன் முடிகிறது: 'தேசம் தொடர்ச்சியாக முயற்சி மற்றும் சாதனைகளின் உயர் நிலைகளுக்கு உயர்வதற்காக.'"
        },
        "why_not_others": {
            "A": {"en": "Olympics is a specific example, not the constitutional text.", "ta": "ஒலிம்பிக் ஒரு குறிப்பிட்ட உதாரணம், அரசியலமைப்பு உரை அல்ல."},
            "B": {"en": "Correct. Exact text of Art 51A(j).", "ta": "சரி. உறுப்பு 51A(j)-ன் சரியான உரை."},
            "C": {"en": "Tax revenue is not the purpose of Art 51A(j).", "ta": "வரி வருவாய் உறுப்பு 51A(j)-ன் நோக்கம் அல்ல."},
            "D": {"en": "Incorrect option.", "ta": "தவறான விருப்பம்."}
        },
        "tnpsc_tip": {
            "en": "Art 51A(j) links personal excellence directly to overall national progress.",
            "ta": "உறுப்பு 51A(j) தனிநபர் சிறப்பை ஒட்டுமொத்த தேசிய முன்னேற்றத்துடன் நேரடியாக இணைக்கிறது."
        }
    },
    {
        "id": "FD_M_014",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Assertion & Reason",
        "question": {
            "en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Fundamental Duties cannot be directly enforced through a writ of Mandamus issued by the Supreme Court.\nReason (R): Fundamental Duties are non-justiciable and require an enabling parliamentary statute to prescribe penalties for non-compliance.\nIn the context of the above statements, which one of the following is correct?",
            "ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): உச்ச நீதிமன்றத்தால் பிறப்பிக்கப்படும் செயலாற்றல் பேராணை (Mandamus) மூலம் அடிப்படை கடமைகளை நேரடியாக அமல்படுத்த முடியாது.\nகாரணம் (R): அடிப்படை கடமைகள் நீதிமன்றங்களால் நேரடியாக அமல்படுத்த முடியாதவை மற்றும் கடமை மீறலுக்குத் தண்டனை விதிக்க நாடாளுமன்ற ஆதரவுச் சட்டம் தேவைப்படுகிறது.\nமேற்கண்ட கூற்றுகளின் அடிப்படையில் பின்வருவனவற்றில் எது சரியானது?"
        },
        "options": [
            {"id": "A", "en": "Both A and R are correct and R is the correct explanation of A", "ta": "A மற்றும் R ஆகிய இரண்டும் சரி, மேலும் R என்பது A-வின் சரியான விளக்கமாகும்"},
            {"id": "B", "en": "Both A and R are correct but R is NOT the correct explanation of A", "ta": "A மற்றும் R ஆகிய இரண்டும் சரி, ஆனால் R என்பது A-வின் சரியான விளக்கம் அல்ல"},
            {"id": "C", "en": "A is correct but R is incorrect", "ta": "A சரி ஆனால் R தவறு"},
            {"id": "D", "en": "A is incorrect but R is correct", "ta": "A தவறு ஆனால் R சரி"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Both A and R are correct. A writ of Mandamus cannot be issued directly to enforce a Fundamental Duty because duties are non-justiciable without enabling parliamentary legislation.",
            "ta": "A மற்றும் R ஆகிய இரண்டும் சரி. நாடாளுமன்றச் சட்டம் இன்றி கடமைகள் அமல்படுத்த முடியாதவை என்பதால் அடிப்படை கடமையை அமல்படுத்தச் செயலாற்றல் பேராணையை நேரடியாகப் பிறப்பிக்க முடியாது."
        },
        "why_not_others": {
            "A": {"en": "Correct. R correctly explains why Mandamus cannot issue for duties.", "ta": "சரி. கடமைகளுக்கு ஏன் பேராணை பிறப்பிக்க முடியாது என்பதை R சரியாக விளக்குகிறது."},
            "B": {"en": "R is the direct reason for A.", "ta": "R என்பது A-விற்கான நேரடிக் காரணமாகும்."},
            "C": {"en": "R is true.", "ta": "R உண்மையாகும்."},
            "D": {"en": "A is true.", "ta": "A உண்மையாகும்."}
        },
        "tnpsc_tip": {
            "en": "Writs under Art 32/226 lie to enforce Fundamental Rights, NOT standalone Fundamental Duties.",
            "ta": "உறுப்பு 32/226-ன் கீழ் பேராணைகள் அடிப்படை உரிமைகளை அமல்படுத்தவே பயன்படுகின்றன, தனித்த அடிப்படை கடமைகளுக்கு அல்ல."
        }
    },
    {
        "id": "FD_M_015",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Statement-based",
        "question": {
            "en": "With reference to the Justice J.S. Verma Committee (1999) report on Fundamental Duties, consider the following statements:\n1. The Committee identified non-operationalized legal provisions in statutes like IPC, Wildlife Act, and Flag Code that enforce Fundamental Duties.\n2. The Committee recommended making Fundamental Duties justiciable by adding criminal penalty clauses directly inside Article 51A.\nWhich of the statements given above is/are correct?",
            "ta": "அடிப்படை கடமைகள் பற்றிய நீதிபதி ஜே.எஸ். வர்மா குழு (1999) அறிக்கையைக் குறிப்பிட்டு, பின்வரும் கூற்றுகளை ஆராய்க:\n1. அடிப்படை கடமைகளை அமல்படுத்தும் IPC, வனவிலங்கு சட்டம் மற்றும் கொடி குறியீடு போன்ற சட்டங்களில் உள்ள நிலவும் விதிகளை குழு கண்டறிந்தது.\n2. உறுப்பு 51A-க்குள் நேரடியாகக் குற்றவியல் தண்டனைக் பிரிவுகளைச் சேர்த்து அடிப்படை கடமைகளை நீதிமன்றத்தால் அமல்படுத்தக்கூடியதாக மாற்றக் குழு பரிந்துரைத்தது.\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 only", "ta": "1 மட்டும்"},
            {"id": "B", "en": "2 only", "ta": "2 மட்டும்"},
            {"id": "C", "en": "Both 1 and 2", "ta": "1 மற்றும் 2 ஆகிய இரண்டும்"},
            {"id": "D", "en": "Neither 1 nor 2", "ta": "1 மற்றும் 2 ஆகிய இரண்டும் இல்லை"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Statement 1 is correct: Verma Committee mapped existing parliamentary laws implementing duties. Statement 2 is incorrect: The Committee recommended awareness and educational inclusion, NOT adding criminal penal clauses inside Art 51A.",
            "ta": "கூற்று 1 சரி: வர்மா குழு கடமைகளை அமல்படுத்தும் நிலவும் நாடாளுமன்றச் சட்டங்களைப் பட்டியலிட்டது. கூற்று 2 தவறு: குழு விழிப்புணர்வு மற்றும் கல்விச் சேர்ப்பைப் பரிந்துரைத்ததே தவிர உறுப்பு 51A-க்குள் குற்றவியல் தண்டனைப் பிரிவுகளைச் சேர்ப்பதை அல்ல."
        },
        "why_not_others": {
            "A": {"en": "Correct. Statement 1 is correct, while Statement 2 is incorrect.", "ta": "சரி. கூற்று 1 சரி, கூற்று 2 தவறு."},
            "B": {"en": "Statement 2 is false.", "ta": "கூற்று 2 தவறானது."},
            "C": {"en": "Statement 2 is false.", "ta": "கூற்று 2 தவறானது."},
            "D": {"en": "Statement 1 is true.", "ta": "கூற்று 1 உண்மையாகும்."}
        },
        "tnpsc_tip": {
            "en": "Verma Committee advocated teaching Fundamental Duties in schools and universities across India.",
            "ta": "வர்மா குழு இந்தியா முழுவதும் உள்ள பள்ளிகள் மற்றும் பல்கலைக்கழகங்களில் அடிப்படை கடமைகளைக் கற்பிக்க பரிந்துரைத்தது."
        }
    },
    {
        "id": "FD_M_016",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Case Law",
        "question": {
            "en": "In AIIMS Students Union v. AIIMS (2002), the Supreme Court laid down an important constitutional principle regarding Part IVA. What was it?",
            "ta": "AIIMS மாணவர் சங்கம் vs AIIMS (2002) வழக்கில், பகுதி IVA தொடர்பாக உச்ச நீதிமன்றம் ஒரு முக்கியமான அரசியலமைப்புத் தத்துவத்தை வழங்கியது. அது என்ன?"
        },
        "options": [
            {"id": "A", "en": "Fundamental Duties are subservient to Fundamental Rights and can be disregarded", "ta": "அடிப்படை கடமைகள் அடிப்படை உரிமைகளுக்குக் கீழானவை, அவற்றைப் புறக்கணிக்கலாம்"},
            {"id": "B", "en": "Fundamental Duties are as important as Fundamental Rights, and duties cannot be ignored while interpreting statutes or evaluating constitutional validity", "ta": "அடிப்படை கடமைகள் அடிப்படை உரிமைகளுக்குச் சமமான முக்கியத்துவம் வாய்ந்தவை, சட்டங்களை விளக்கும் போது கடமைகளைப் புறக்கணிக்க முடியாது"},
            {"id": "C", "en": "Fundamental Duties apply only during National Emergency", "ta": "அடிப்படை கடமைகள் தேசிய அவசரநிலையின் போது மட்டுமே பொருந்தும்"},
            {"id": "D", "en": "Fundamental Duties can be deleted by Presidential Order", "ta": "குடியரசுத் தலைவர் ஆணை மூலம் அடிப்படை கடமைகளை நீக்கலாம்"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "In AIIMS Students Union v. AIIMS (2002), SC held that Fundamental Duties are equally important as Fundamental Rights and cannot be brushed aside during judicial interpretation.",
            "ta": "AIIMS மாணவர் சங்கம் vs AIIMS (2002) வழக்கில், அடிப்படை கடமைகள் அடிப்படை உரிமைகளுக்குச் சமமான முக்கியத்துவம் வாய்ந்தவை, நீதித்துறை விளக்கத்தின் போது அவற்றைத் தள்ளிவைக்க முடியாது என உச்ச நீதிமன்றம் தீர்ப்பளித்தது."
        },
        "why_not_others": {
            "A": {"en": "SC held duties are NOT subservient to rights.", "ta": "கடமைகள் உரிமைகளுக்குக் கீழானவை அல்ல என நீதிமன்றம் கூறியது."},
            "B": {"en": "Correct. FDs are as important as FRs in interpretation.", "ta": "சரி. விளக்கத்தில் கடமைகள் உரிமைகளுக்குச் சமமான முக்கியத்துவம் வாய்ந்தவை."},
            "C": {"en": "Duties apply at all times.", "ta": "கடமைகள் எக்காலத்திலும் பொருந்தும்."},
            "D": {"en": "Constitutional provisions require constitutional amendment under Art 368.", "ta": "அரசியலமைப்பு விதிகளுக்கு உறுப்பு 368-ன் கீழ் திருத்தம் தேவை."}
        },
        "tnpsc_tip": {
            "en": "Highlighting AIIMS (2002): Fundamental Rights and Fundamental Duties are two sides of the same constitutional coin.",
            "ta": "AIIMS (2002) தீர்ப்பு: அடிப்படை உரிமைகளும் அடிப்படை கடமைகளும் ஒரே அரசியலமைப்பு நாணயத்தின் இரு பக்கங்கள்."
        }
    },
    {
        "id": "FD_M_017",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Conceptual Comparison",
        "question": {
            "en": "Consider the following statements comparing Part III, Part IV, and Part IVA of the Constitution of India:\n1. Part III contains justiciable rights enjoyed by individuals against State action.\n2. Part IV contains non-justiciable policy directives guiding the State in governance.\n3. Part IVA contains non-justiciable civic responsibilities commanded to Indian citizens.\nWhich of the statements given above are correct?",
            "ta": "இந்திய அரசியலமைப்பின் பகுதி III, பகுதி IV, மற்றும் பகுதி IVA ஆகியவற்றை ஒப்பிடும் பின்வரும் கூற்றுகளை ஆராய்க:\n1. பகுதி III அரசு நடவடிக்கைக்கு எதிராகத் தனிநபர்கள் அனுபவிக்கும் அமல்படுத்தக்கூடிய உரிமைகளைக் கொண்டுள்ளது.\n2. பகுதி IV ஆட்சியில் அரசை வழிநடத்தும் அமல்படுத்த முடியாத கொள்கை வழிகாட்டுதல்களைக் கொண்டுள்ளது.\n3. பகுதி IVA இந்தியக் குடிமக்களுக்கு ஆணையிடப்பட்ட அமல்படுத்த முடியாத குடிமைப் பொறுப்புகளைக் கொண்டுள்ளது.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 and 2 only", "ta": "1 மற்றும் 2 மட்டும்"},
            {"id": "B", "en": "2 and 3 only", "ta": "2 மற்றும் 3 மட்டும்"},
            {"id": "C", "en": "1 and 3 only", "ta": "1 மற்றும் 3 மட்டும்"},
            {"id": "D", "en": "1, 2 and 3", "ta": "1, 2 மற்றும் 3"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "All three statements are correct. Part III = FR (Individual Rights, Justiciable), Part IV = DPSP (State Policy, Non-justiciable), Part IVA = FD (Citizen Duties, Non-justiciable).",
            "ta": "மூன்று கூற்றுகளும் சரியானவை. பகுதி III = FR (தனிநபர் உரிமைகள், அமல்படுத்தக் கூடியவை), பகுதி IV = DPSP (அரசு கொள்கை, அமல்படுத்த முடியாதவை), பகுதி IVA = FD (குடிமகன் கடமைகள், அமல்படுத்த முடியாதவை)."
        },
        "why_not_others": {
            "A": {"en": "Statement 3 is also true.", "ta": "கூற்று 3-ம் உண்மையாகும்."},
            "B": {"en": "Statement 1 is also true.", "ta": "கூற்று 1-ம் உண்மையாகும்."},
            "C": {"en": "Statement 2 is also true.", "ta": "கூற்று 2-ம் உண்மையாகும்."},
            "D": {"en": "Correct. All statements 1, 2, and 3 are correct.", "ta": "சரி. 1, 2 மற்றும் 3 ஆகிய அனைத்துக் கூற்றுகளும் சரி."}
        },
        "tnpsc_tip": {
            "en": "Master the 3-part constitutional architecture: Rights (Part III) -> DPSP (Part IV) -> Duties (Part IVA).",
            "ta": "3-பகுதி அரசியலமைப்பு அமைப்பில் தேர்ச்சி பெறுக: உரிமைகள் (பகுதி III) -> DPSP (பகுதி IV) -> கடமைகள் (பகுதி IVA)."
        }
    },
    {
        "id": "FD_M_018",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Amendment-based",
        "question": {
            "en": "With reference to the 42nd Constitutional Amendment Act, 1976, consider the following statements:\n1. It added Part IVA and Article 51A to the Constitution of India.\n2. It enacted 10 Fundamental Duties upon the recommendation of Swaran Singh Committee.\n3. It introduced Article 48A (Environmental protection directive) in Part IV DPSP simultaneously.\nWhich of the statements given above are correct?",
            "ta": "1976-ன் 42வது அரசியலமைப்பு திருத்தச் சட்டத்தைக் குறிப்பிட்டு, பின்வரும் கூற்றுகளை ஆராய்க:\n1. இது இந்திய அரசியலமைப்பில் பகுதி IVA மற்றும் உறுப்பு 51A ஐச் சேர்த்தது.\n2. இது ஸ்வரன் சிங் குழுவின் பரிந்துரையின் பேரில் 10 அடிப்படை கடமைகளை இயற்றியது.\n3. இது பகுதி IV DPSP-ல் உறுப்பு 48A (சுற்றுச்சூழல் பாதுகாப்பு வழிகாட்டுதல்) ஐ ஒரே நேரத்தில் அறிமுகப்படுத்தியது.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 and 2 only", "ta": "1 மற்றும் 2 மட்டும்"},
            {"id": "B", "en": "2 and 3 only", "ta": "2 மற்றும் 3 மட்டும்"},
            {"id": "C", "en": "1 and 3 only", "ta": "1 மற்றும் 3 மட்டும்"},
            {"id": "D", "en": "1, 2 and 3", "ta": "1, 2 மற்றும் 3"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "All three statements are correct. The 42nd CAA 1976 added Part IVA (Art 51A with 10 duties) and added Art 48A in DPSP.",
            "ta": "மூன்று கூற்றுகளும் சரியானவை. 42வது திருத்தம் 1976 பகுதி IVA (10 கடமைகளுடன் உறுப்பு 51A) மற்றும் DPSP-ல் உறுப்பு 48A ஐச் சேர்த்தது."
        },
        "why_not_others": {
            "A": {"en": "Statement 3 is also true.", "ta": "கூற்று 3-ம் உண்மையாகும்."},
            "B": {"en": "Statement 1 is also true.", "ta": "கூற்று 1-ம் உண்மையாகும்."},
            "C": {"en": "Statement 2 is also true.", "ta": "கூற்று 2-ம் உண்மையாகும்."},
            "D": {"en": "Correct. All statements 1, 2, and 3 are correct.", "ta": "சரி. 1, 2 மற்றும் 3 ஆகிய அனைத்துக் கூற்றுகளும் சரி."}
        },
        "tnpsc_tip": {
            "en": "42nd CAA 1976 reshaped environmental and civic obligation framework in India.",
            "ta": "42வது திருத்தம் 1976 இந்தியாவில் சுற்றுச்சூழல் மற்றும் குடிமைப் பொறுப்பு கட்டமைப்பை மீண்டும் வடிவமைத்தது."
        }
    },
    {
        "id": "FD_M_019",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Conceptual Comparison",
        "question": {
            "en": "What is the key functional distinction between Article 49 (DPSP) and Article 51A(f) (Fundamental Duty)?",
            "ta": "உறுப்பு 49 (DPSP) மற்றும் உறுப்பு 51A(f) (அடிப்படை கடமை) ஆகியவற்றுக்கு இடையே உள்ள முதன்மைச் செயல்பாட்டு வேறுபாடு என்ன?"
        },
        "options": [
            {"id": "A", "en": "Article 49 obligates the State to protect monuments of national importance; Article 51A(f) obligates Citizens to value and preserve rich heritage of composite culture", "ta": "உறுப்பு 49 தேசிய முக்கியத்துவம் வாய்ந்த நினைவுச் சின்னங்களைப் பாதுகாக்க அரசைப் பொறுப்பாக்குகிறது; உறுப்பு 51A(f) கூட்டுப் பண்பாட்டின் வளமான பாரம்பரியத்தை மதித்துப் பேணக் குடிமக்களைப் பொறுப்பாக்குகிறது"},
            {"id": "B", "en": "Article 49 applies to citizens; Article 51A(f) applies to State governments", "ta": "உறுப்பு 49 குடிமக்களுக்குப் பொருந்தும்; உறுப்பு 51A(f) மாநில அரசாங்கங்களுக்குப் பொருந்தும்"},
            {"id": "C", "en": "Article 49 is justiciable; Article 51A(f) is non-justiciable", "ta": "உறுப்பு 49 அமல்படுத்தக் கூடியது; உறுப்பு 51A(f) அமல்படுத்த முடியாதது"},
            {"id": "D", "en": "Article 49 was added in 2002; Article 51A(f) was added in 1950", "ta": "உறுப்பு 49 2002-ல் சேர்க்கப்பட்டது; உறுப்பு 51A(f) 1950-ல் சேர்க்கப்பட்டது"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Article 49 (DPSP) directs the STATE to protect physical monuments of historic interest. Article 51A(f) (FD) commands CITIZENS to preserve India's intangible and tangible composite cultural heritage.",
            "ta": "உறுப்பு 49 (DPSP) வரலாற்றுச் சிறப்புமிக்க நினைவுச் சின்னங்களைப் பாதுகாக்க அரசுக்கு வழிகாட்டுகிறது. உறுப்பு 51A(f) (FD) இந்தியாவின் கூட்டுப் பண்பாட்டுப் பாரம்பரியத்தைப் பேணக் குடிமக்களுக்கு ஆணையிடுகிறது."
        },
        "why_not_others": {
            "A": {"en": "Correct. Art 49 = State Monument Duty; Art 51A(f) = Citizen Composite Culture Duty.", "ta": "சரி. உறுப்பு 49 = அரசு நினைவுச் சின்னக் கடமை; உறுப்பு 51A(f) = குடிமகன் கூட்டுப் பண்பாட்டுக் கடமை."},
            "B": {"en": "Incorrect duty bearers.", "ta": "தவறான கடமைப் பொறுப்பாளிகள்."},
            "C": {"en": "Neither DPSP nor FD is directly justiciable.", "ta": "DPSP அல்லது FD இரண்டும் நேரடியாக அமல்படுத்தக்கூடியவை அல்ல."},
            "D": {"en": "Art 49 was in 1950 original text; Art 51A(f) was added in 1976.", "ta": "உறுப்பு 49 1950 அசல் உரையில் இருந்தது; உறுப்பு 51A(f) 1976-ல் சேர்க்கப்பட்டது."}
        },
        "tnpsc_tip": {
            "en": "Monuments protection by State = Art 49 DPSP | Composite culture preservation by Citizen = Art 51A(f) FD.",
            "ta": "அரசால் நினைவுச் சின்னங்கள் பாதுகாப்பு = உறுப்பு 49 DPSP | குடிமகனால் கூட்டுப் பண்பாட்டுப் பாதுகாப்பு = உறுப்பு 51A(f) FD."
        }
    },
    {
        "id": "FD_M_020",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Statement-based",
        "question": {
            "en": "Consider the following Parliamentary Acts and their corresponding Fundamental Duty implementations:\n1. Prevention of Insults to National Honour Act, 1971 -> Enforces Article 51A(a) [National Flag & Anthem].\n2. Wildlife Protection Act, 1972 -> Enforces Article 51A(g) [Forests & Wildlife].\n3. Protection of Civil Rights Act, 1955 -> Enforces Article 51A(e) [Brotherhood & Caste Equality].\nWhich of the pairs given above are correctly matched?",
            "ta": "பின்வரும் நாடாளுமன்றச் சட்டங்கள் மற்றும் அவற்றின் இணையான அடிப்படை கடமை அமலாக்கங்களை ஆராய்க:\n1. தேசிய கௌரவ அவமதிப்பு தடுப்புச் சட்டம், 1971 -> உறுப்பு 51A(a)-ஐ அமல்படுத்துகிறது [தேசியக் கொடி & கீதம்].\n2. வனவிலங்கு பாதுகாப்புச் சட்டம், 1972 -> உறுப்பு 51A(g)-ஐ அமல்படுத்துகிறது [காடுகள் & வனவிலங்குகள்].\n3. சிவில் உரிமைகள் பாதுகாப்புச் சட்டம், 1955 -> உறுப்பு 51A(e)-ஐ அமல்படுத்துகிறது [சகோதரத்துவம் & சாதி சமத்துவம்].\nமேற்கூறிய ஜோடிகளில் எவை சரியாகப் பொருந்தியுள்ளன?"
        },
        "options": [
            {"id": "A", "en": "1 and 2 only", "ta": "1 மற்றும் 2 மட்டும்"},
            {"id": "B", "en": "2 and 3 only", "ta": "2 மற்றும் 3 மட்டும்"},
            {"id": "C", "en": "1 and 3 only", "ta": "1 மற்றும் 3 மட்டும்"},
            {"id": "D", "en": "1, 2 and 3", "ta": "1, 2 மற்றும் 3"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "All three pairs are correctly matched. As identified by the Justice Verma Committee (1999), these statutes provide criminal penal enforcement for various Fundamental Duties.",
            "ta": "மூன்று ஜோடிகளும் சரியாகப் பொருந்தியுள்ளன. நீதிபதி வர்மா குழு (1999) சுட்டிக்காட்டியபடி, இச்சட்டங்கள் பல்வேறு அடிப்படை கடமைகளுக்குக் குற்றவியல் அமலாக்கத்தை வழங்குகின்றன."
        },
        "why_not_others": {
            "A": {"en": "Pair 3 is also correct.", "ta": "ஜோடி 3-ம் சரியானது."},
            "B": {"en": "Pair 1 is also correct.", "ta": "ஜோடி 1-ம் சரியானது."},
            "C": {"en": "Pair 2 is also correct.", "ta": "ஜோடி 2-ம் சரியானது."},
            "D": {"en": "Correct. All 1, 2, and 3 pairs are correctly matched.", "ta": "சரி. 1, 2 மற்றும் 3 ஆகிய அனைத்து ஜோடிகளும் சரியாகப் பொருந்தியுள்ளன."}
        },
        "tnpsc_tip": {
            "en": "Remember: Parliamentary statutes provide the 'teeth' (legal enforcement) for non-justiciable Fundamental Duties.",
            "ta": "நினைவில் கொள்க: நாடாளுமன்றச் சட்டங்களே அமல்படுத்த முடியாத அடிப்படை கடமைகளுக்குச் சட்டப்பூர்வ அமலாக்கத்தை வழங்குகின்றன."
        }
    },
    {
        "id": "FD_M_021",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Case Law",
        "question": {
            "en": "In Animal Welfare Board of India v. A. Nagaraja (2014), the Supreme Court relied on Article 51A(g) to deliver a historic judgment. What was the core ruling?",
            "ta": "இந்திய விலங்கு நல வாரியம் vs ஏ. நாகராஜா (2014) வழக்கில், வரலாற்றுச் சிறப்புமிக்க தீர்ப்பை வழங்க உச்ச நீதிமன்றம் உறுப்பு 51A(g)-ஐச் சார்ந்திருந்தது. அத்தீர்ப்பின் முக்கிய அம்சம் என்ன?"
        },
        "options": [
            {"id": "A", "en": "Animals have a constitutional right to life under Article 21, and Article 51A(g) mandates human compassion towards living creatures", "ta": "உறுப்பு 21-ன் கீழ் விலங்குகளுக்கு வாழும் உரிமை உள்ளது, மேலும் உறுப்பு 51A(g) உயிரினங்கள் மீது மனிதக் கருணையைக் கட்டாயமாக்குகிறது"},
            {"id": "B", "en": "Jallikattu is declared a Fundamental Right of citizens under Article 29", "ta": "ஜல்லிக்கட்டு உறுப்பு 29-ன் கீழ் குடிமக்களின் அடிப்படை உரிமையாக அறிவிக்கப்படுகிறது"},
            {"id": "C", "en": "Article 51A(g) applies only to national parks and sanctuaries", "ta": "உறுப்பு 51A(g) தேசிய பூங்காக்கள் மற்றும் சரணாலயங்களுக்கு மட்டுமே பொருந்தும்"},
            {"id": "D", "en": "Forest officials are exempt from Fundamental Duties", "ta": "வனத்துறையினருக்கு அடிப்படை கடமைகளிலிருந்து விலக்கு அளிக்கப்பட்டுள்ளது"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "In A. Nagaraja (2014) [Jallikattu verdict], SC held that animals have intrinsic dignity and right to life under Art 21, enforced through citizen duty of compassion under Art 51A(g).",
            "ta": "ஏ. நாகராஜா (2014) வழக்கில், விலங்குகளுக்குத் தன்னாட்சி கண்ணியமும் உறுப்பு 21-ன் கீழ் வாழும் உரிமையும் உள்ளது என்றும், இது உறுப்பு 51A(g) கருணைக் கடமையின் மூலம் நிலைநாட்டப்படுகிறது என்றும் உச்ச நீதிமன்றம் தீர்ப்பளித்தது."
        },
        "why_not_others": {
            "A": {"en": "Correct. SC linked animal dignity with Art 21 and Art 51A(g) compassion duty.", "ta": "சரி. உச்ச நீதிமன்றம் விலங்கு கண்ணியத்தை உறுப்பு 21 மற்றும் உறுப்பு 51A(g) கருணைக் கடமையுடன் இணைத்தது."},
            "B": {"en": "Court banned Jallikattu in 2014 (later state act was passed).", "ta": "2014-ல் நீதிமன்றம் ஜல்லிக்கட்டுக்குத் தடை விதித்தது."},
            "C": {"en": "Art 51A(g) applies everywhere across India.", "ta": "உறுப்பு 51A(g) இந்தியா முழுவதும் பொருந்தும்."},
            "D": {"en": "Incorrect option.", "ta": "தவறான விருப்பம்."}
        },
        "tnpsc_tip": {
            "en": "Nagaraja 2014 case established that Art 51A(g) 'compassion for living creatures' extends to animal rights.",
            "ta": "நாகராஜா 2014 வழக்கு உறுப்பு 51A(g) 'உயிரினங்கள் மீதான கருணை' விலங்குகள் உரிமைகளுக்கும் நீட்டிக்கப்படுகிறது என்பதை நிறுவியது."
        }
    },
    {
        "id": "FD_M_022",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Assertion & Reason",
        "question": {
            "en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): The framers of the original 1950 Constitution did not incorporate a separate chapter on Fundamental Duties.\nReason (R): They believed that citizens of free India, having won independence through sacrifice, would voluntarily perform their duties without constitutional compulsion.\nIn the context of the above statements, which one of the following is correct?",
            "ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): அசல் 1950 அரசியலமைப்பை உருவாக்கியவர்கள் அடிப்படை கடமைகள் பற்றித் தனி அத்தியாயத்தைச் சேர்க்கவில்லை.\nகாரணம் (R): தியாகத்தின் மூலம் சுதந்திரம் பெற்ற சுதந்திர இந்தியாவின் குடிமக்கள் அரசியலமைப்பு வற்புறுத்தல் இன்றித் தாமாகவே தங்கள் கடமைகளைச் செய்வார்கள் என்று அவர்கள் நம்பினர்.\nமேற்கண்ட கூற்றுகளின் அடிப்படையில் பின்வருவனவற்றில் எது சரியானது?"
        },
        "options": [
            {"id": "A", "en": "Both A and R are correct and R is the correct explanation of A", "ta": "A மற்றும் R ஆகிய இரண்டும் சரி, மேலும் R என்பது A-வின் சரியான விளக்கமாகும்"},
            {"id": "B", "en": "Both A and R are correct but R is NOT the correct explanation of A", "ta": "A மற்றும் R ஆகிய இரண்டும் சரி, ஆனால் R என்பது A-வின் சரியான விளக்கம் அல்ல"},
            {"id": "C", "en": "A is correct but R is incorrect", "ta": "A சரி ஆனால் R தவறு"},
            {"id": "D", "en": "A is incorrect but R is correct", "ta": "A தவறு ஆனால் R சரி"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Both A and R are true. The Constituent Assembly omitted duties assuming voluntary civic consciousness in post-independence India as explained in R.",
            "ta": "A மற்றும் R ஆகிய இரண்டும் உண்மை. சுதந்திரத்திற்குப் பிந்தைய இந்தியாவில் தன்னார்வக் குடிமை விழிப்புணர்வு இருக்கும் என்ற நம்பிக்கையில் அரசியல் நிர்ணய சபை கடமைகளை விடுத்தது."
        },
        "why_not_others": {
            "A": {"en": "Correct. R correctly explains why the 1950 Constitution omitted duties.", "ta": "சரி. 1950 அரசியலமைப்பு ஏன் கடமைகளை விடுத்தது என்பதை R சரியாக விளக்குகிறது."},
            "B": {"en": "R is the direct explanation for A.", "ta": "R என்பது A-விற்கான நேரடி விளக்கமாகும்."},
            "C": {"en": "R is true.", "ta": "R உண்மையாகும்."},
            "D": {"en": "A is true.", "ta": "A உண்மையாகும்."}
        },
        "tnpsc_tip": {
            "en": "By 1976 during Emergency, Congress Government realized voluntary compliance was insufficient, leading to 42nd CAA.",
            "ta": "1976 அவசரநிலையின் போது, தன்னார்வக் கீழ்ப்படிதல் போதாது என்பதை உணர்ந்து 42வது திருத்தம் கொண்டுவரப்பட்டது."
        }
    },
    {
        "id": "FD_M_023",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Article-based",
        "question": {
            "en": "Article 51A(e) contains two distinct mandates. Which pair represents those two mandates correctly?",
            "ta": "உறுப்பு 51A(e) இரண்டு வெவ்வேறு கட்டளைகளைக் கொண்டுள்ளது. பின்வரும் எந்த ஜோடி அந்த இரண்டு கட்டளைகளைச் சரியாகப் பிரதிநிதித்துவப்படுத்துகிறது?"
        },
        "options": [
            {"id": "A", "en": "1. Promote harmony & common brotherhood; 2. Renounce practices derogatory to the dignity of women", "ta": "1. நல்லிணக்கம் & பொதுவான சகோதரத்துவத்தை வளர்த்தல்; 2. பெண்களின் கண்ணியத்தைக் குறைக்கும் பழக்கங்களைக் கைவிடுதல்"},
            {"id": "B", "en": "1. Defend the country; 2. Safeguard public property", "ta": "1. தேசத்தைப் பாதுகாத்தல்; 2. பொதுச் சொத்தைப் பாதுகாத்தல்"},
            {"id": "C", "en": "1. Develop scientific temper; 2. Protect rivers and lakes", "ta": "1. அறிவியல் மனப்பான்மையை வளர்த்தல்; 2. ஆறுகள் மற்றும் ஏரிகளைப் பாதுகாத்தல்"},
            {"id": "D", "en": "1. Provide education to child; 2. Respect National Anthem", "ta": "1. குழந்தைக்குக் கல்வி அளித்தல்; 2. தேசியக் கீதத்தை மதித்தல்"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Article 51A(e) has two limbs: 1. Promoting harmony and common brotherhood transcending diversities; 2. Renouncing practices derogatory to dignity of women.",
            "ta": "உறுப்பு 51A(e) இரண்டு பகுதிகளைக் கொண்டுள்ளது: 1. வேறுபாடுகளைக் கடந்து நல்லிணக்கம் மற்றும் பொதுவான சகோதரத்துவத்தை வளர்த்தல்; 2. பெண்களின் கண்ணியத்தைக் குறைக்கும் பழக்கங்களைக் கைவிடுதல்."
        },
        "why_not_others": {
            "A": {"en": "Correct. These are the 2 limbs of Art 51A(e).", "ta": "சரி. இவை உறுப்பு 51A(e)-ன் 2 பகுதிகள்."},
            "B": {"en": "Defend country is 51A(d); Public property is 51A(i).", "ta": "தேசத்தைப் பாதுகாப்பது 51A(d); பொதுச் சொத்து 51A(i)."},
            "C": {"en": "Scientific temper is 51A(h); Rivers is 51A(g).", "ta": "அறிவியல் மனப்பான்மை 51A(h); ஆறுகள் 51A(g)."},
            "D": {"en": "Education is 51A(k); Anthem is 51A(a).", "ta": "கல்வி 51A(k); கீதம் 51A(a)."}
        },
        "tnpsc_tip": {
            "en": "Remember: Article 51A(e) is the ONLY Fundamental Duty clause explicitly focusing on Women's Dignity.",
            "ta": "நினைவில் கொள்க: உறுப்பு 51A(e) என்பது பெண்களின் கண்ணியத்தில் வெளிப்படையாகக் கவனம் செலுத்தும் ஒரே அடிப்படை கடமை உட்பிரிவாகும்."
        }
    },
    {
        "id": "FD_M_024",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Case Law",
        "question": {
            "en": "In Aruna Roy v. Union of India (2002), the Supreme Court upheld the introduction of value-based education in school curricula. Which Fundamental Duties were cited to justify value education?",
            "ta": "அருணா ராய் vs இந்திய யூனியன் (2002) வழக்கில், பள்ளிக் பாடத்திட்டத்தில் மதிப்பு சார்ந்த கல்வியை அறிமுகப்படுத்துவதை உச்ச நீதிமன்றம் உறுதி செய்தது. மதிப்புக் கல்வியை நியாயப்படுத்த எந்த அடிப்படை கடமைகள் மேற்கோள் காட்டப்பட்டன?"
        },
        "options": [
            {"id": "A", "en": "Article 51A(a) and Article 51A(c)", "ta": "உறுப்பு 51A(a) மற்றும் உறுப்பு 51A(c)"},
            {"id": "B", "en": "Article 51A(e) and Article 51A(h)", "ta": "உறுப்பு 51A(e) மற்றும் உறுப்பு 51A(h)"},
            {"id": "C", "en": "Article 51A(d) and Article 51A(i)", "ta": "உறுப்பு 51A(d) மற்றும் உறுப்பு 51A(i)"},
            {"id": "D", "en": "Article 51A(f) and Article 51A(j)", "ta": "உறுப்பு 51A(f) மற்றும் உறுப்பு 51A(j)"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "In Aruna Roy (2002), SC held that teaching moral and value education in schools promotes common brotherhood [51A(e)] and scientific temper/humanism [51A(h)] and is not anti-secular.",
            "ta": "அருணா ராய் (2002) வழக்கில், பள்ளிகளில் தார்மீக மற்றும் மதிப்புக் கல்வியைக் கற்பிப்பது பொதுவான சகோதரத்துவத்தையும் [51A(e)] அறிவியல் மனப்பான்மை/மனிதநேயத்தையும் [51A(h)] வளர்க்கிறது என்றும் அது மதச்சார்பின்மைக்கு எதிரானது அல்ல என்றும் உச்ச நீதிமன்றம் தீர்ப்பளித்தது."
        },
        "why_not_others": {
            "A": {"en": "Arts 51A(a) & (c) deal with flag and sovereignty.", "ta": "உறுப்புகள் 51A(a) & (c) கொடி மற்றும் இறையாண்மை பற்றியவை."},
            "B": {"en": "Correct. Arts 51A(e) & (h) were cited in Aruna Roy case.", "ta": "சரி. அருணா ராய் வழக்கில் உறுப்புகள் 51A(e) & (h) மேற்கோள் காட்டப்பட்டன."},
            "C": {"en": "Arts 51A(d) & (i) deal with defence and public property.", "ta": "உறுப்புகள் 51A(d) & (i) பாதுகாப்பு மற்றும் பொதுச் சொத்து பற்றியவை."},
            "D": {"en": "Arts 51A(f) & (j) deal with culture and excellence.", "ta": "உறுப்புகள் 51A(f) & (j) பண்பாடு மற்றும் சிறப்பு பற்றியவை."}
        },
        "tnpsc_tip": {
            "en": "Aruna Roy case affirmed that value education fostering secular ethics is supported by Part IVA.",
            "ta": "அருணா ராய் வழக்கு மதச்சார்பற்ற நெறிமுறைகளை வளர்க்கும் மதிப்புக் கல்விக்கு பகுதி IVA ஆதரவளிக்கிறது என்பதை உறுதிப்படுத்தியது."
        }
    },
    {
        "id": "FD_M_025",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Statement-based",
        "question": {
            "en": "Consider the following statements regarding the 6-fold thematic classification of Fundamental Duties:\n1. The thematic grouping (Loyalty, Harmony, Environment, Rationality, Excellence, Education) is a conventional academic study classification.\n2. The Constitution of India explicitly divides Article 51A into six numbered chapters.\nWhich of the statements given above is/are correct?",
            "ta": "அடிப்படை கடமைகளின் 6 வகை தலைப்பு வாரியான வகைப்பாடு பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. தலைப்பு வாரியப் பிரிவுகள் (விசுவாசம், நல்லிணக்கம், சுற்றுச்சூழல், பகுத்தறிவு, சிறப்பு, கல்வி) என்பது ஒரு மரபுவழி கல்விப் படிப்பு வகைபாடாகும்.\n2. இந்திய அரசியலமைப்பு வெளிப்படையாக உறுப்பு 51A-ஐ ஆறு எண்ணிடப்பட்ட அத்தியாயங்களாகப் பிரிக்கிறது.\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 only", "ta": "1 மட்டும்"},
            {"id": "B", "en": "2 only", "ta": "2 மட்டும்"},
            {"id": "C", "en": "Both 1 and 2", "ta": "1 மற்றும் 2 ஆகிய இரண்டும்"},
            {"id": "D", "en": "Neither 1 nor 2", "ta": "1 மற்றும் 2 ஆகிய இரண்டும் இல்லை"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Statement 1 is correct: Thematic grouping is an academic study framework. Statement 2 is incorrect: The Constitution presents Art 51A as a single continuous list of clauses (a) to (k) WITHOUT thematic sub-chapters.",
            "ta": "கூற்று 1 சரி: தலைப்பு வாரியப் பிரிவுகள் ஒரு கல்விப் படிப்பு கட்டமைப்பாகும். கூற்று 2 தவறு: அரசியலமைப்பு உறுப்பு 51A-ஐ தலைப்பு வாரிய உட்பிரிவுகள் இன்றி (a) முதல் (k) வரையிலான ஒரே தொடர்ச்சியான பட்டியலாக வழங்குகிறது."
        },
        "why_not_others": {
            "A": {"en": "Correct. Statement 1 is correct, while Statement 2 is incorrect.", "ta": "சரி. கூற்று 1 சரி, கூற்று 2 தவறு."},
            "B": {"en": "Statement 2 is false.", "ta": "கூற்று 2 தவறானது."},
            "C": {"en": "Statement 2 is false.", "ta": "கூற்று 2 தவறானது."},
            "D": {"en": "Statement 1 is true.", "ta": "கூற்று 1 உண்மையாகும்."}
        },
        "tnpsc_tip": {
            "en": "Classic TNPSC trap! Academic classifications are study tools, not explicit constitutional text.",
            "ta": "செம்மையான டிஎன்பிஎஸ்சி பொறி! கல்வி வகைப்பாடுகள் படிப்பு கருவிகளே தவிர, வெளிப்படையான அரசியலமைப்பு உரை அல்ல."
        }
    },
    {
        "id": "FD_M_026",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Article-based",
        "question": {
            "en": "Article 51A(c) obligates citizens to uphold and protect 'Sovereignty, Unity and Integrity of India'. Which other component of the Constitution contains the exact word 'Integrity'?",
            "ta": "உறுப்பு 51A(c) குடிமக்களை 'இந்தியாவின் இறையாண்மை, ஒற்றுமை மற்றும் ஒருமைப்பாட்டைப் பேணிப் பாதுகாக்க' கடமைப்படுத்துகிறது. அரசியலமைப்பின் எந்த வேறு பகுதி 'ஒருமைப்பாடு' (Integrity) என்ற அதே சொல்லைக் கொண்டுள்ளது?"
        },
        "options": [
            {"id": "A", "en": "The Preamble", "ta": "முகப்புரை"},
            {"id": "B", "en": "Schedule 1", "ta": "அட்டவணை 1"},
            {"id": "C", "en": "Article 368", "ta": "உறுப்பு 368"},
            {"id": "D", "en": "Part II Citizenship", "ta": "பகுதி II குடியுரிமை"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "The Preamble to the Constitution of India contains the phrase 'Unity and Integrity of the Nation' (inserted by 42nd CAA 1976). Article 51A(c) aligns directly with this Preamble ideal.",
            "ta": "இந்திய அரசியலமைப்பின் முகப்புரை 'தேசத்தின் ஒற்றுமை மற்றும் ஒருமைப்பாடு' என்ற சொற்றொடரைக் கொண்டுள்ளது (1976-ன் 42வது திருத்தத்தால் சேர்க்கப்பட்டது). உறுப்பு 51A(c) இந்த முகப்புரை லட்சியத்துடன் நேரடியாக ஒத்துப்போகிறது."
        },
        "why_not_others": {
            "A": {"en": "Correct. Preamble contains 'Unity and Integrity of the Nation'.", "ta": "சரி. முகப்புரையில் 'தேசத்தின் ஒற்றுமை மற்றும் ஒருமைப்பாடு' உள்ளது."},
            "B": {"en": "Schedule 1 lists States and UTs names.", "ta": "அட்டவணை 1 மாநிலங்கள் மற்றும் யூனியன் பிரதேசங்களின் பெயர்களைப் பட்டியலிடுகிறது."},
            "C": {"en": "Art 368 deals with Amendment procedure.", "ta": "உறுப்பு 368 திருத்த நடைமுறை பற்றியது."},
            "D": {"en": "Part II deals with Citizenship Articles 5-11.", "ta": "பகுதி II உறுப்புகள் 5-11 குடியுரிமை பற்றியது."}
        },
        "tnpsc_tip": {
            "en": "Both Preamble 'Integrity' and Article 51A(c) 'Integrity' were shaped by the 42nd CAA 1976.",
            "ta": "முகப்புரை 'ஒருமைப்பாடு' மற்றும் உறுப்பு 51A(c) 'ஒருமைப்பாடு' ஆகிய இரண்டும் 1976-ன் 42வது திருத்தத்தால் அமைக்கப்பட்டன."
        }
    },
    {
        "id": "FD_M_027",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Assertion & Reason",
        "question": {
            "en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Parliament can enact legislation imposing compulsory military service (conscription) during national emergency.\nReason (R): Article 51A(d) imposes a Fundamental Duty on citizens to defend the country and render national service when called upon to do so.\nIn the context of the above statements, which one of the following is correct?",
            "ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): தேசிய அவசரநிலையின் போது கட்டாய ராணுவ சேவையை (conscription) விதிக்கும் சட்டத்தை நாடாளுமன்றம் இயற்றலாம்.\nகாரணம் (R): உறுப்பு 51A(d) அரசால் அழைக்கப்படும் போது தேசத்தைப் பாதுகாக்கவும் தேசிய சேவை ஆற்றவும் குடிமக்களுக்கு அடிப்படை கடமையை விதிக்கிறது.\nமேற்கண்ட கூற்றுகளின் அடிப்படையில் பின்வருவனவற்றில் எது சரியானது?"
        },
        "options": [
            {"id": "A", "en": "Both A and R are correct and R is the correct explanation of A", "ta": "A மற்றும் R ஆகிய இரண்டும் சரி, மேலும் R என்பது A-வின் சரியான விளக்கமாகும்"},
            {"id": "B", "en": "Both A and R are correct but R is NOT the correct explanation of A", "ta": "A மற்றும் R ஆகிய இரண்டும் சரி, ஆனால் R என்பது A-வின் சரியான விளக்கம் அல்ல"},
            {"id": "C", "en": "A is correct but R is incorrect", "ta": "A சரி ஆனால் R தவறு"},
            {"id": "D", "en": "A is incorrect but R is correct", "ta": "A தவறு ஆனால் R சரி"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Both A and R are true. Under Article 23(2) and Article 51A(d), the State can impose compulsory service for public purposes, providing constitutional backing for conscription laws.",
            "ta": "A மற்றும் R ஆகிய இரண்டும் உண்மை. உறுப்பு 23(2) மற்றும் உறுப்பு 51A(d)-ன் கீழ், அரசு பொது நோக்கங்களுக்காகக் கட்டாய சேவையை விதிக்கலாம், இது கட்டாய ராணுவ சேவைச் சட்டங்களுக்கு அரசியலமைப்பு ஆதரவை வழங்குகிறது."
        },
        "why_not_others": {
            "A": {"en": "Correct. R provides the explicit duty foundation for A.", "ta": "சரி. R என்பது A-விற்கான வெளிப்படையான கடமை அடித்தளத்தை வழங்குகிறது."},
            "B": {"en": "R directly explains A.", "ta": "R நேரடியாக A-வை விளக்குகிறது."},
            "C": {"en": "R is true.", "ta": "R உண்மையாகும்."},
            "D": {"en": "A is true.", "ta": "A உண்மையாகும்."}
        },
        "tnpsc_tip": {
            "en": "Article 23(2) allows State to impose compulsory public service without discrimination on grounds of religion, race, caste or class.",
            "ta": "உறுப்பு 23(2) மதம், இனம், சாதி அல்லது வகுப்பின் அடிப்படையில் பாகுபாடின்றி கட்டாயப் பொது சேவையை விதிக்க அரசுக்கு அனுமதி அளிக்கிறது."
        }
    },
    {
        "id": "FD_M_028",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Article-based",
        "question": {
            "en": "Which of the following sub-clauses of Article 51A is specifically aimed at preserving spiritual and moral memory of the Indian Freedom Struggle?",
            "ta": "உறுப்பு 51A-ன் பின்வரும் எந்த உட்பிரிவு குறிப்பாக இந்திய சுதந்திரப் போராட்டத்தின் ஆன்மீக மற்றும் தார்மீக நினைவைப் பேண நோக்கமாகக் கொண்டுள்ளது?"
        },
        "options": [
            {"id": "A", "en": "Article 51A(a)", "ta": "உறுப்பு 51A(a)"},
            {"id": "B", "en": "Article 51A(b)", "ta": "உறுப்பு 51A(b)"},
            {"id": "C", "en": "Article 51A(c)", "ta": "உறுப்பு 51A(c)"},
            {"id": "D", "en": "Article 51A(e)", "ta": "உறுப்பு 51A(e)"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "Article 51A(b) explicitly mandates: 'To cherish and follow the noble ideals which inspired our national struggle for freedom.'",
            "ta": "உறுப்பு 51A(b) வெளிப்படையாகக் கட்டளையிடுகிறது: 'நமது தேசிய சுதந்திரப் போராட்டத்திற்கு ஊக்கமளித்த உயரிய லட்சியங்களைப் பேணிப் பின்பற்றுதல்.'"
        },
        "why_not_others": {
            "A": {"en": "51A(a) deals with Constitution, Flag, Anthem.", "ta": "51A(a) அரசியலமைப்பு, கொடி, கீதம் பற்றியது."},
            "B": {"en": "Correct. 51A(b) covers freedom struggle ideals.", "ta": "சரி. 51A(b) சுதந்திரப் போராட்ட லட்சியங்களை உள்ளடக்கியது."},
            "C": {"en": "51A(c) deals with Sovereignty and Unity.", "ta": "51A(c) இறையாண்மை மற்றும் ஒற்றுமை பற்றியது."},
            "D": {"en": "51A(e) deals with Brotherhood and Women's dignity.", "ta": "51A(e) சகோதரத்துவம் மற்றும் பெண்கள் கண்ணியம் பற்றியது."}
        },
        "tnpsc_tip": {
            "en": "Noble ideals: Non-violence, truth, communal harmony, anti-untouchability, and Swadeshi.",
            "ta": "உயரிய லட்சியங்கள்: அகிம்சை, உண்மை, சமூக நல்லிணக்கம், தீண்டாமை எதிர்ப்பு, மற்றும் சுதேசி."
        }
    },
    {
        "id": "FD_M_029",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Statement-based",
        "question": {
            "en": "Consider the following statements comparing Article 21A and Article 51A(k):\n1. Article 21A places an obligation on the STATE to provide free and compulsory education.\n2. Article 51A(k) places an obligation on the PARENT OR GUARDIAN to provide education opportunities.\n3. Both Article 21A and Article 51A(k) apply to the exact same age group of 6 to 14 years.\nWhich of the statements given above are correct?",
            "ta": "உறுப்பு 21A மற்றும் உறுப்பு 51A(k) ஆகியவற்றை ஒப்பிடும் பின்வரும் கூற்றுகளை ஆராய்க:\n1. உறுப்பு 21A இலவச கட்டாயக் கல்வியை வழங்க அரசு மீது பொறுப்பை விதிக்கிறது.\n2. உறுப்பு 51A(k) கல்வி வாய்ப்புகளை வழங்கப் பெற்றோர் அல்லது பாதுகாவலர் மீது பொறுப்பை விதிக்கிறது.\n3. உறுப்பு 21A மற்றும் உறுப்பு 51A(k) ஆகிய இரண்டும் 6 முதல் 14 வயது வரையிலான ஒரே வயதுக் குழுவிற்குப் பொருந்தும்.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 and 2 only", "ta": "1 மற்றும் 2 மட்டும்"},
            {"id": "B", "en": "2 and 3 only", "ta": "2 மற்றும் 3 மட்டும்"},
            {"id": "C", "en": "1 and 3 only", "ta": "1 மற்றும் 3 மட்டும்"},
            {"id": "D", "en": "1, 2 and 3", "ta": "1, 2 மற்றும் 3"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "All three statements are correct. Art 21A (FR State Duty) and Art 51A(k) (FD Parent Duty) work in tandem for children aged 6 to 14 years.",
            "ta": "மூன்று கூற்றுகளும் சரியானவை. உறுப்பு 21A (FR அரசு கடமை) மற்றும் உறுப்பு 51A(k) (FD பெற்றோர் கடமை) ஆகிய இரண்டும் 6 முதல் 14 வயதுக் குழந்தைகளுக்காக இணைந்து செயல்படுகின்றன."
        },
        "why_not_others": {
            "A": {"en": "Statement 3 is also true.", "ta": "கூற்று 3-ம் உண்மையாகும்."},
            "B": {"en": "Statement 1 is also true.", "ta": "கூற்று 1-ம் உண்மையாகும்."},
            "C": {"en": "Statement 2 is also true.", "ta": "கூற்று 2-ம் உண்மையாகும்."},
            "D": {"en": "Correct. All statements 1, 2, and 3 are correct.", "ta": "சரி. 1, 2 மற்றும் 3 ஆகிய அனைத்துக் கூற்றுகளும் சரி."}
        },
        "tnpsc_tip": {
            "en": "State constructs schools and funds education (Art 21A); Parents actually send children to school (Art 51A(k)).",
            "ta": "அரசு பள்ளிகளைக் கட்டி கல்விக்கு நிதியளிக்கிறது (உறுப்பு 21A); பெற்றோர்கள் குழந்தைகளைப் பள்ளிக்கு அனுப்புகிறார்கள் (உறுப்பு 51A(k))."
        }
    },
    {
        "id": "FD_M_030",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Conceptual Comparison",
        "question": {
            "en": "The Supreme Court in M.C. Mehta cases linked Article 21, Article 48A, and Article 51A(g). What is the operational relationship between these three Articles?",
            "ta": "எம்.சி. மேத்தா வழக்குகளில் உச்ச நீதிமன்றம் உறுப்பு 21, உறுப்பு 48A, மற்றும் உறுப்பு 51A(g) ஆகியவற்றை இணைத்தது. இந்த மூன்று உறுப்புகளுக்கு இடையே உள்ள செயல்பாட்டுத் தொடர்பு என்ன?"
        },
        "options": [
            {"id": "A", "en": "Art 21 guarantees Right to Clean Environment; Art 48A directs State policy; Art 51A(g) obligates citizen protection", "ta": "உறுப்பு 21 தூய்மை சுற்றுச்சூழல் உரிமையை உத்தரவாதம் செய்கிறது; உறுப்பு 48A அரசுக் கொள்கையை வழிநடத்துகிறது; உறுப்பு 51A(g) குடிமகன் பாதுகாப்பைப் பொறுப்பாக்குகிறது"},
            {"id": "B", "en": "Art 21 applies to citizens; Art 48A applies to foreigners; Art 51A(g) applies to corporates", "ta": "உறுப்பு 21 குடிமக்களுக்குப் பொருந்தும்; உறுப்பு 48A வெளிநாட்டினருக்குப் பொருந்தும்; உறுப்பு 51A(g) நிறுவனங்களுக்குப் பொருந்தும்"},
            {"id": "C", "en": "Art 48A overrides Art 21 during Emergency", "ta": "அவசரநிலையின் போது உறுப்பு 48A உறுப்பு 21-ஐ மிஞ்சுகிறது"},
            {"id": "D", "en": "Art 51A(g) is justiciable while Art 21 is non-justiciable", "ta": "உறுப்பு 51A(g) அமல்படுத்தக் கூடியது, உறுப்பு 21 அமல்படுத்த முடியாதது"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "The Environmental Triangle: Art 21 creates the Fundamental Right, Art 48A mandates State policy (DPSP), and Art 51A(g) mandates Citizen responsibility (FD).",
            "ta": "சுற்றுச்சூழல் முக்கோணம்: உறுப்பு 21 அடிப்படை உரிமையை உருவாக்குகிறது, உறுப்பு 48A அரசுக் கொள்கையை விதிக்கிறது (DPSP), மற்றும் உறுப்பு 51A(g) குடிமகன் பொறுப்பை விதிக்கிறது (FD)."
        },
        "why_not_others": {
            "A": {"en": "Correct. Environmental Triangle relationship.", "ta": "சரி. சுற்றுச்சூழல் முக்கோணத் தொடர்பு."},
            "B": {"en": "Incorrect applicability.", "ta": "தவறான பொருந்தும் எல்லை."},
            "C": {"en": "Art 21 cannot be suspended even during Emergency.", "ta": "அவசரநிலையிலும் உறுப்பு 21-ஐ நிறுத்தி வைக்க முடியாது."},
            "D": {"en": "Art 21 is justiciable; Art 51A(g) is non-justiciable.", "ta": "உறுப்பு 21 அமல்படுத்தக் கூடியது; உறுப்பு 51A(g) அமல்படுத்த முடியாதது."}
        },
        "tnpsc_tip": {
            "en": "Taj Trapezium case (1997) relied on this exact Environmental Triangle.",
            "ta": "தாஜ் ட்ரேபீசியம் வழக்கு (1997) இந்தச் சுற்றுச்சூழல் முக்கோணத்தையே சார்ந்தது."
        }
    },
    {
        "id": "FD_M_031",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Assertion & Reason",
        "question": {
            "en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Parliament did not include the 'Duty to pay taxes' recommended by Swaran Singh Committee into Article 51A.\nReason (R): Tax liability is already comprehensively enforced through specific taxation statutes (like Income Tax Act) with stringent civil and criminal penal provisions.\nIn the context of the above statements, which one of the following is correct?",
            "ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\n<ctrl42>கூற்று (A): ஸ்வரன் சிங் குழுவால் பரிந்துரைக்கப்பட்ட 'வரி செலுத்தும் கடமை'யை நாடாளுமன்றம் உறுப்பு 51A-ல் சேர்க்கவில்லை.\nகாரணம் (R): வரிப் பொறுப்பு ஏற்கனவே கடுமையான சிவில் மற்றும் குற்றவியல் தண்டனை விதிகளுடன் கூடிய குறிப்பிட்ட வரிச் சட்டங்கள் (வருமான வரிச் சட்டம் போன்றவை) மூலம் விரிவாக அமல்படுத்தப்படுகிறது.\nமேற்கண்ட கூற்றுகளின் அடிப்படையில் பின்வருவனவற்றில் எது சரியானது?"
        },
        "options": [
            {"id": "A", "en": "Both A and R are correct and R is the correct explanation of A", "ta": "A மற்றும் R ஆகிய இரண்டும் சரி, மேலும் R என்பது A-வின் சரியான விளக்கமாகும்"},
            {"id": "B", "en": "Both A and R are correct but R is NOT the correct explanation of A", "ta": "A மற்றும் R ஆகிய இரண்டும் சரி, ஆனால் R என்பது A-வின் சரியான விளக்கம் அல்ல"},
            {"id": "C", "en": "A is correct but R is incorrect", "ta": "A சரி ஆனால் R தவறு"},
            {"id": "D", "en": "A is incorrect but R is correct", "ta": "A தவறு ஆனால் R சரி"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Both A and R are true. Parliament omitted tax duty from Art 51A because taxation is already an enforced statutory obligation rather than a non-justiciable moral civic duty.",
            "ta": "A மற்றும் R ஆகிய இரண்டும் உண்மை. வரி விதிப்பு ஏற்கனவே அமல்படுத்தப்பட்ட சட்டப்பூர்வப் பொறுப்பாக இருப்பதால், நாடாளுமன்றம் வரி செலுத்தும் கடமையை உறுப்பு 51A-லிருந்து விடுத்தது."
        },
        "why_not_others": {
            "A": {"en": "Correct. R explains why Parliament saw no need to put tax duty in non-justiciable Part IVA.", "ta": "சரி. ஏன் நாடாளுமன்றம் அமல்படுத்த முடியாத பகுதி IVA-ல் வரியைச் சேர்க்கத் தேவையில்லை எனக் கருதியது என்பதை R விளக்குகிறது."},
            "B": {"en": "R directly explains A.", "ta": "R நேரடியாக A-வை விளக்குகிறது."},
            "C": {"en": "R is true.", "ta": "R உண்மையாகும்."},
            "D": {"en": "A is true.", "ta": "A உண்மையாகும்."}
        },
        "tnpsc_tip": {
            "en": "Paying taxes is a legal obligation under statutory laws, not a non-justiciable constitutional duty.",
            "ta": "வரி செலுத்துவது சட்டப்பூர்வச் சட்டங்களின் கீழ் உள்ள சட்டப் பொறுப்பே தவிர, அமல்படுத்த முடியாத அரசியலமைப்பு கடமை அல்ல."
        }
    },
    {
        "id": "FD_M_032",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Statement-based",
        "question": {
            "en": "Consider the following statements regarding the application of Fundamental Duties to non-citizens:\n1. A foreign tourist visiting India cannot be prosecuted directly under Article 51A for not showing compassion to living creatures.\n2. A foreign national in India can be prosecuted under specific parliamentary statutes like Wildlife Protection Act 1972 if they commit an animal cruelty offense.\nWhich of the statements given above is/are correct?",
            "ta": "வெளிநாட்டினருக்கு அடிப்படை கடமைகள் பொருந்துவது பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. இந்தியாவிற்கு வரும் வெளிநாட்டு சுற்றுலாப் பயணி உயிரினங்கள் மீது கருணை காட்டாததற்காக உறுப்பு 51A-ன் கீழ் நேரடியாகத் தண்டிக்கப்பட முடியாது.\n2. இந்தியாவில் உள்ள வெளிநாட்டவர் விலங்குகள் கொடுமை குற்றத்தைச் செய்தால் வனவிலங்கு பாதுகாப்புச் சட்டம் 1972 போன்ற குறிப்பிட்ட நாடாளுமன்றச் சட்டங்களின் கீழ் தண்டிக்கப்படலாம்.\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 only", "ta": "1 மட்டும்"},
            {"id": "B", "en": "2 only", "ta": "2 மட்டும்"},
            {"id": "C", "en": "Both 1 and 2", "ta": "1 மற்றும் 2 ஆகிய இரண்டும்"},
            {"id": "D", "en": "Neither 1 nor 2", "ta": "1 மற்றும் 2 ஆகிய இரண்டும் இல்லை"}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "Both statements are correct. Art 51A does not apply to foreigners (Statement 1), but penal statutory laws of the land apply to everyone within Indian territory (Statement 2).",
            "ta": "இரண்டு கூற்றுகளும் சரியானவை. உறுப்பு 51A வெளிநாட்டினருக்குப் பொருந்தாது (கூற்று 1), ஆனால் நாட்டின் குற்றவியல் சட்டப்பூர்வச் சட்டங்கள் இந்திய நிலப்பரப்பிற்குள் உள்ள அனைவருக்கும் பொருந்தும் (கூற்று 2)."
        },
        "why_not_others": {
            "A": {"en": "Statement 2 is also correct.", "ta": "கூற்று 2-ம் சரியானது."},
            "B": {"en": "Statement 1 is also correct.", "ta": "கூற்று 1-ம் சரியானது."},
            "C": {"en": "Correct. Both statements 1 and 2 are correct.", "ta": "சரி. 1 மற்றும் 2 ஆகிய இரண்டு கூற்றுகளும் சரி."},
            "D": {"en": "Both statements are true.", "ta": "இரண்டு கூற்றுகளும் உண்மை."}
        },
        "tnpsc_tip": {
            "en": "Constitutional duties apply to Citizens | Statutory penal laws apply to All Persons in India.",
            "ta": "அரசியலமைப்பு கடமைகள் குடிமக்களுக்குப் பொருந்தும் | சட்டப்பூர்வ குற்றவியல் சட்டங்கள் இந்தியாவில் உள்ள அனைத்து நபர்களுக்கும் பொருந்தும்."
        }
    },
    {
        "id": "FD_M_033",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Direct",
        "question": {
            "en": "Which of the following comparative statements regarding constitutional duties in global democracies is correct?",
            "ta": "உலகளாவிய ஜனநாயகங்களில் உள்ள அரசியலமைப்பு கடமைகள் பற்றிய பின்வரும் ஒப்பீட்டுக் கூற்றுகளில் எது சரியானது?"
        },
        "options": [
            {"id": "A", "en": "The US Constitution contains a detailed chapter on Fundamental Duties in its Bill of Rights", "ta": "அமெரிக்க அரசியலமைப்பு தனது உரிமைகள் மசோதாவில் அடிப்படை கடமைகள் பற்றிய விரிவான அத்தியாயத்தைக் கொண்டுள்ளது"},
            {"id": "B", "en": "Western democratic constitutions (like US, Canada, France) generally focus on rights and do not enumerate citizen duties, unlike Japan and India", "ta": "மேற்கத்திய ஜனநாயக அரசியலமைப்புகள் (அமெரிக்கா, கனடா, பிரான்ஸ் போன்றவை) ஜப்பான் மற்றும் இந்தியாவைப் போலன்றி பொதுவாக உரிமைகளில் கவனம் செலுத்துகின்றன, குடிமகன் கடமைகளைப் பட்டியலிடுவதில்லை"},
            {"id": "C", "en": "The British Constitution was the first to introduce justiciable duties in 1950", "ta": "பிரிட்டிஷ் அரசியலமைப்பு 1950-ல் முதன்முதலில் அமல்படுத்தக்கூடிய கடமைகளை அறிமுகப்படுத்தியது"},
            {"id": "D", "en": "Socialist constitutions traditionally had no mention of citizen duties", "ta": "சமதர்ம அரசியலமைப்புகள் பாரம்பரியமாகக் குடிமகன் கடமைகளைக் குறிப்பிடவில்லை"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "Western democracies (US, Canada, UK, France) traditionally relied on unwritten civic duties without explicit constitutional duty chapters. Socialist constitutions (USSR) and Japan/India are exceptions.",
            "ta": "மேற்கத்திய ஜனநாயக நாடுகள் (அமெரிக்கா, கனடா, பிரிட்டன், பிரான்ஸ்) பாரம்பரியமாக வெளிப்படையான அரசியலமைப்பு கடமை அத்தியாயங்கள் இன்றி எழுதப்படாத குடிமை கடமைகளைச் சார்ந்திருந்தன. சமதர்ம அரசியலமைப்புகள் (USSR) மற்றும் ஜப்பான்/இந்தியா ஆகியவை விதிவிலக்குகள்."
        },
        "why_not_others": {
            "A": {"en": "US Bill of Rights contains only rights.", "ta": "அமெரிக்க உரிமைகள் மசோதாவில் உரிமைகள் மட்டுமே உள்ளன."},
            "B": {"en": "Correct statement.", "ta": "சரியான கூற்று."},
            "C": {"en": "UK does not have a written constitution.", "ta": "பிரிட்டனுக்கு எழுதப்பட்ட அரசியலமைப்பு இல்லை."},
            "D": {"en": "Socialist constitutions emphasized duties heavily.", "ta": "சமதர்ம அரசியலமைப்புகள் கடமைகளை பெரிதும் வலியுறுத்தின."}
        },
        "tnpsc_tip": {
            "en": "Japanese Constitution is a rare democratic precedent for explicit citizen duties.",
            "ta": "ஜப்பானிய அரசியலமைப்பு வெளிப்படையான குடிமகன் கடமைகளுக்கான ஒரு அரிதான ஜனநாயக முன்மாதிரியாகும்."
        }
    },
    {
        "id": "FD_M_034",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Statement-based",
        "question": {
            "en": "Consider the following statements regarding the Prevention of Insults to National Honour Act, 1971:\n1. It penalizes burning, defacing, or trampling upon the Indian National Flag in public.\n2. It penalizes intentionally preventing the singing of the National Anthem or causing disturbance to an assembly engaged in such singing.\nWhich of the statements given above is/are correct?",
            "ta": "1971-ன் தேசிய கௌரவ அவமதிப்பு தடுப்புச் சட்டம் பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. இது பொதுவெளியில் இந்திய தேசியக் கொடியை எரிப்பது, சிதைப்பது அல்லது மிதிப்பதைத் தண்டிக்கிறது.\n2. இது தேசியக் கீதம் பாடுவதைத் வேண்டுமென்றே தடுப்பது அல்லது பாடும் கூட்டத்திற்கு இடையூறு விளைவிப்பதைத் தண்டிக்கிறது.\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 only", "ta": "1 மட்டும்"},
            {"id": "B", "en": "2 only", "ta": "2 மட்டும்"},
            {"id": "C", "en": "Both 1 and 2", "ta": "1 மற்றும் 2 ஆகிய இரண்டும்"},
            {"id": "D", "en": "Neither 1 nor 2", "ta": "1 மற்றும் 2 ஆகிய இரண்டும் இல்லை"}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "Both statements are correct. The 1971 Act penalizes insults to the National Flag, Constitution, and National Anthem, enforcing Article 51A(a).",
            "ta": "இரண்டு கூற்றுகளும் சரியானவை. 1971-ன் சட்டம் தேசியக் கொடி, அரசியலமைப்பு மற்றும் தேசியக் கீதத்தை அவமதிப்பதைத் தண்டித்து, உறுப்பு 51A(a)-ஐ அமல்படுத்துகிறது."
        },
        "why_not_others": {
            "A": {"en": "Statement 2 is also correct.", "ta": "கூற்று 2-ம் சரியானது."},
            "B": {"en": "Statement 1 is also correct.", "ta": "கூற்று 1-ம் சரியானது."},
            "C": {"en": "Correct. Both statements 1 and 2 are correct.", "ta": "சரி. 1 மற்றும் 2 ஆகிய இரண்டு கூற்றுகளும் சரி."},
            "D": {"en": "Both statements are true.", "ta": "இரண்டு கூற்றுகளும் உண்மை."}
        },
        "tnpsc_tip": {
            "en": "This Act gives statutory penal backing to Article 51A(a).",
            "ta": "இச்சட்டம் உறுப்பு 51A(a)-க்குச் சட்டப்பூர்வ குற்றவியல் அமலாக்கத்தை வழங்குகிறது."
        }
    },
    {
        "id": "FD_M_035",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Case Law",
        "question": {
            "en": "In M.C. Mehta v. Union of India (1997) [Taj Trapezium case], how did the Supreme Court apply Article 51A(g)?",
            "ta": "எம்.சி. மேத்தா vs இந்திய யூனியன் (1997) [தாஜ் ட்ரேபீசியம் வழக்கு] வழக்கில், உச்ச நீதிமன்றம் உறுப்பு 51A(g)-ஐ எவ்வாறு பயன்படுத்தியது?"
        },
        "options": [
            {"id": "A", "en": "The Court ordered closure/relocation of polluting industries around Taj Mahal to enforce environmental duties under Art 51A(g) along with Art 48A and Art 21", "ta": "தாஜ் மஹாலைச் சுற்றியுள்ள மாசுபடுத்தும் தொழிற்சாலைகளை மூட/இடம்மாற்ற உத்தரவிட்டு, உறுப்புகள் 48A மற்றும் 21 உடன் உறுப்பு 51A(g) சுற்றுச்சூழல் கடமைகளை அமல்படுத்தியது"},
            {"id": "B", "en": "The Court held that economic profits of industries override environmental duties under Art 51A(g)", "ta": "தொழிற்சாலைகளின் பொருளாதார லாபம் உறுப்பு 51A(g)-ன் கீழ் உள்ள சுற்றுச்சூழல் கடமைகளை விட மேலானது என நீதிமன்றம் தீர்ப்பளித்தது"},
            {"id": "C", "en": "The Court ruled that Taj Mahal is not covered under composite culture under Art 51A(f)", "ta": "தாஜ்மஹால் உறுப்பு 51A(f)-ன் கீழ் உள்ள கூட்டுப் பண்பாட்டில் வரவில்லை என நீதிமன்றம் தீர்ப்பளித்தது"},
            {"id": "D", "en": "The Court declared Art 51A(g) unconstitutional", "ta": "நீதிமன்றம் உறுப்பு 51A(g)-ஐ அரசியலமைப்பிற்கு எதிரானது என அறிவித்தது"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "In Taj Trapezium case (1997), SC invoked Art 51A(g) (Citizen Duty), Art 48A (State DPSP), and Art 21 (Right to Clean Environment) to protect Taj Mahal from industrial pollution.",
            "ta": "தாஜ் ட்ரேபீசியம் வழக்கில் (1997), தாஜ் மஹாலைத் தொழில் மாசிலிருந்து பாதுகாக்க உச்ச நீதிமன்றம் உறுப்பு 51A(g) (குடிமகன் கடமை), உறுப்பு 48A (அரசு DPSP), மற்றும் உறுப்பு 21 (தூய்மை சுற்றுச்சூழல் உரிமை) ஆகியவற்றைப் பயன்படுத்தியது."
        },
        "why_not_others": {
            "A": {"en": "Correct. SC applied Art 51A(g) to shut down polluting foundries near Taj Mahal.", "ta": "சரி. தாஜ் மஹால் அருகே உள்ள மாசுபடுத்தும் தொழிற்சாலைகளை மூட உச்ச நீதிமன்றம் உறுப்பு 51A(g)-ஐப் பயன்படுத்தியது."},
            "B": {"en": "Environment was given priority over industrial pollution.", "ta": "தொழில் மாசை விட சுற்றுச்சூழலுக்கு முன்னுரிமை அளிக்கப்பட்டது."},
            "C": {"en": "Incorrect statement.", "ta": "தவறான கூற்று."},
            "D": {"en": "Art 51A(g) is a valid constitutional duty.", "ta": "உறுப்பு 51A(g) ஒரு செல்லுபடியாகும் அரசியலமைப்பு கடமையாகும்."}
        },
        "tnpsc_tip": {
            "en": "Landmark illustration of judicial reliance on Fundamental Duties for environmental protection.",
            "ta": "சுற்றுச்சூழல் பாதுகாப்பிற்கு அடிப்படை கடமைகளை நீதிமன்றங்கள் சார்ந்திருப்பதற்கான முக்கிய உதாரணம்."
        }
    },
    {
        "id": "FD_M_036",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Assertion & Reason",
        "question": {
            "en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): An individual citizen cannot file a writ petition in the High Court under Article 226 seeking a writ of Mandamus to compel another citizen to perform their Fundamental Duty under Article 51A.\nReason (R): Writs under Article 226 lie primarily against the State or public authorities for breach of legal/constitutional rights, not against private citizens for non-performance of non-justiciable duties.\nIn the context of the above statements, which one of the following is correct?",
            "ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): மற்றொரு குடிமகன் உறுப்பு 51A-ன் கீழ் தனது அடிப்படை கடமையைச் செய்ய வற்புறுத்த ஒரு தனிநபர் குடிமகன் உறுப்பு 226-ன் கீழ் உயர் நீதிமன்றத்தில் செயலாற்றல் பேராணை (Mandamus) மனுவைத் தாக்கல் செய்ய முடியாது.\nகாரணம் (R): உறுப்பு 226-ன் கீழ் உள்ள பேராணைகள் முதன்மையாகச் சட்டப்/அரசியலமைப்பு உரிமைகள் மீறலுக்காக அரசு அல்லது பொது அதிகாரிகளுக்கு எதிராகவே அமையும், அமல்படுத்த முடியாத கடமைகளைச் செய்யாத தனியார் குடிமக்களுக்கு எதிராக அல்ல.\nமேற்கண்ட கூற்றுகளின் அடிப்படையில் பின்வருவனவற்றில் எது சரியானது?"
        },
        "options": [
            {"id": "A", "en": "Both A and R are correct and R is the correct explanation of A", "ta": "A மற்றும் R ஆகிய இரண்டும் சரி, மேலும் R என்பது A-வின் சரியான விளக்கமாகும்"},
            {"id": "B", "en": "Both A and R are correct but R is NOT the correct explanation of A", "ta": "A மற்றும் R ஆகிய இரண்டும் சரி, ஆனால் R என்பது A-வின் சரியான விளக்கம் அல்ல"},
            {"id": "C", "en": "A is correct but R is incorrect", "ta": "A சரி ஆனால் R தவறு"},
            {"id": "D", "en": "A is incorrect but R is correct", "ta": "A தவறு ஆனால் R சரி"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Both A and R are true. High Courts cannot issue writs to private individuals for failing to perform non-justiciable duties (R), making Assertion A correct.",
            "ta": "A மற்றும் R ஆகிய இரண்டும் உண்மை. அமல்படுத்த முடியாத கடமைகளைத் தவறவிட்ட தனியார் தனிநபர்களுக்கு உயர் நீதிமன்றங்கள் பேராணைகளைப் பிறப்பிக்க முடியாது (R), எனவே கூற்று A சரியானது."
        },
        "why_not_others": {
            "A": {"en": "Correct. R explains why Mandamus does not lie against private citizens for duties.", "ta": "சரி. கடமைகளுக்காகத் தனியார் குடிமக்களுக்கு எதிராக ஏன் செயலாற்றல் பேராணை அமையாது என்பதை R விளக்குகிறது."},
            "B": {"en": "R directly explains A.", "ta": "R நேரடியாக A-வை விளக்குகிறது."},
            "C": {"en": "R is true.", "ta": "R உண்மையாகும்."},
            "D": {"en": "A is true.", "ta": "A உண்மையாகும்."}
        },
        "tnpsc_tip": {
            "en": "Writs are public law remedies directed against 'State' action or public statutory duties.",
            "ta": "பேராணைகள் என்பது 'அரசு' நடவடிக்கை அல்லது பொதுச் சட்டப்பூர்வக் கடமைகளுக்கு எதிராகப் பயன்படுத்தப்படும் பொதுச் சட்டப் பரிகாரங்கள் ஆகும்."
        }
    },
    {
        "id": "FD_M_037",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Statement-based",
        "question": {
            "en": "Consider the following statements regarding the addition of Fundamental Duties:\n1. The 42nd Amendment Act 1976 added 10 duties covering clauses (a) to (j) of Article 51A.\n2. The 86th Amendment Act 2002 added 1 duty under clause (k) of Article 51A.\n3. The 44th Amendment Act 1978 added 2 duties under clauses (l) and (m) of Article 51A.\nWhich of the statements given above are correct?",
            "ta": "அடிப்படை கடமைகளைச் சேர்ப்பது பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. 42வது திருத்தச் சட்டம் 1976 உறுப்பு 51A-ன் உட்பிரிவுகள் (a) முதல் (j) வரை 10 கடமைகளைச் சேர்த்தது.\n2. 86வது திருத்தச் சட்டம் 2002 உறுப்பு 51A-ன் உட்பிரிவு (k)-ன் கீழ் 1 கடமையைச் சேர்த்தது.\n3. 44வது திருத்தச் சட்டம் 1978 உறுப்பு 51A-ன் உட்பிரிவுகள் (l) மற்றும் (m)-ன் கீழ் 2 கடமைகளைச் சேர்த்தது.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 and 2 only", "ta": "1 மற்றும் 2 மட்டும்"},
            {"id": "B", "en": "2 and 3 only", "ta": "2 மற்றும் 3 மட்டும்"},
            {"id": "C", "en": "1 and 3 only", "ta": "1 மற்றும் 3 மட்டும்"},
            {"id": "D", "en": "1, 2 and 3", "ta": "1, 2 மற்றும் 3"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Statements 1 and 2 are correct. Statement 3 is INCORRECT because the 44th Amendment 1978 added NO Fundamental Duties, and there are NO clauses (l) or (m) in Article 51A.",
            "ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறு, ஏனெனில் 44வது திருத்தம் 1978 எந்தவொரு அடிப்படை கடமையையும் சேர்க்கவில்லை, மேலும் உறுப்பு 51A-ல் (l) அல்லது (m) உட்பிரிவுகள் இல்லை."
        },
        "why_not_others": {
            "A": {"en": "Correct. Statements 1 and 2 are true, while Statement 3 is false.", "ta": "சரி. கூற்றுகள் 1 மற்றும் 2 உண்மை, கூற்று 3 தவறு."},
            "B": {"en": "Statement 3 is false.", "ta": "கூற்று 3 தவறானது."},
            "C": {"en": "Statement 3 is false.", "ta": "கூற்று 3 தவறானது."},
            "D": {"en": "Statement 3 is false.", "ta": "கூற்று 3 தவறானது."}
        },
        "tnpsc_tip": {
            "en": "Article 51A stops at clause (k). There are no clauses beyond (k).",
            "ta": "உறுப்பு 51A உட்பிரிவு (k) உடன் முடிகிறது. (k)க்கு அப்பால் உட்பிரிவுகள் இல்லை."
        }
    },
    {
        "id": "FD_M_038",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Conceptual Distinction",
        "question": {
            "en": "Which of the following scenarios best exemplifies a citizen exercising 'Scientific Temper' under Article 51A(h)?",
            "ta": "பின்வரும் எந்தச் சூழல் உறுப்பு 51A(h)-ன் கீழ் ஒரு குடிமகன் 'அறிவியல் மனப்பான்மையை' செயல்படுத்துவதை மிகச்சிறப்பாக உவமானப்படுத்துகிறது?"
        },
        "options": [
            {"id": "A", "en": "Memorizing all chemical formulas in a textbook without questioning", "ta": "கேள்வி கேட்காமல் பாடப்புத்தகத்தில் உள்ள அனைத்து வேதியியல் சூத்திரங்களையும் மனப்பாடம் செய்தல்"},
            {"id": "B", "en": "Rejecting superstitious practices like human sacrifice or unscientific medical cures in favor of empirical evidence and rational enquiry", "ta": "ஆதாரங்கள் மற்றும் பகுத்தறிவு ஆய்வின் ஆதரவில் மனித பலி அல்லது அறிவியலற்ற மருத்துவக் குணங்களை போன்ற மூடநம்பிக்கைப் பழக்கங்களை நிராகரித்தல்"},
            {"id": "C", "en": "Buying an expensive telescope to decorate a living room", "ta": "வரவேற்பறையை அலங்கரிக்க விலையுயர்ந்த தொலைநோக்கியை வாங்குதல்"},
            {"id": "D", "en": "Attaining a Master's degree in Engineering", "ta": "பொறியியலில் முதுகலை பட்டம் பெறுதல்"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "Scientific Temper is an attitude of mind questioning superstitions and relying on logic, empirical proof, and humanism (B). Degrees or memorization (A, D) represent academic knowledge, not necessarily scientific temper.",
            "ta": "அறிவியல் மனப்பான்மை என்பது மூடநம்பிக்கைகளைக் கேள்விக்குட்படுத்தி தர்க்கம், சான்றுகள் மற்றும் மனிதநேயத்தைச் சார்ந்திருக்கும் மனநிலையாகும் (B). பட்டங்கள் அல்லது மனப்பாடம் (A, D) கல்வி அறிவைக் குறிக்கிறதே தவிர, அறிவியல் மனப்பான்மையைக் குறிக்க வேண்டியதில்லை."
        },
        "why_not_others": {
            "A": {"en": "Rote memorization lacks spirit of inquiry.", "ta": "மனப்பாடம் செய்வதில் ஆராய்ச்சி உணர்வு இல்லை."},
            "B": {"en": "Correct. Rejecting superstition via logic is scientific temper.", "ta": "சரி. தர்க்கம் மூலம் மூடநம்பிக்கையை நிராகரிப்பதே அறிவியல் மனப்பான்மை."},
            "C": {"en": "Showy purchase is not scientific temper.", "ta": "ஆடம்பரக் கொள்முதல் அறிவியல் மனப்பான்மை அல்ல."},
            "D": {"en": "Degrees equal knowledge, not necessarily rational attitude.", "ta": "பட்டங்கள் அறிவிற்குச் சமம், பகுத்தறிவு மனநிலைக்கு அல்ல."}
        },
        "tnpsc_tip": {
            "en": "Scientific temper is about RATIONAL ATTITUDE and HUMANISM, not academic degrees.",
            "ta": "அறிவியல் மனப்பான்மை என்பது பகுத்தறிவு மனநிலை மற்றும் மனிதநேயம் பற்றியதே தவிர, கல்விப் பட்டங்கள் பற்றியது அல்ல."
        }
    },
    {
        "id": "FD_M_039",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Statement-based",
        "question": {
            "en": "Consider the following statements regarding the Supreme Court 2009 guidelines on damage to public property [Article 51A(i)]:\n1. High Courts can take suo motu cognisance of public property destruction during strikes.\n2. A sitting or retired High Court judge can be appointed as Claims Commissioner to assess damages.\n3. The damages assessed can be recovered from political leaders/organizers who called the strike.\nWhich of the statements given above are correct?",
            "ta": "பொதுச் சொத்துச் சேதம் [உறுப்பு 51A(i)] பற்றிய 2009 உச்ச நீதிமன்ற வழிகாட்டுதல்கள் தொடர்பான பின்வரும் கூற்றுகளை ஆராய்க:\n1. வேலைநிறுத்தங்களின் போது பொதுச் சொத்து சேதத்தை உயர் நீதிமன்றங்கள் தாமாக முன்வந்து (suo motu) விசாரணைக்கு எடுத்துக்கொள்ளலாம்.\n2. சேதங்களை மதிப்பிடப் பணியில் உள்ள அல்லது ஓய்வுபெற்ற உயர் நீதிமன்ற நீதிபதி உரிமைகோரல் ஆணையராக (Claims Commissioner) நியமிக்கப்படலாம்.\n3. மதிப்பிடப்பட்ட சேதங்களை வேலைநிறுத்தத்திற்கு அழைப்பு விடுத்த அரசியல் தலைவர்கள்/அமைப்பாளர்களிடமிருந்து வசூலிக்கலாம்.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 and 2 only", "ta": "1 மற்றும் 2 மட்டும்"},
            {"id": "B", "en": "2 and 3 only", "ta": "2 மற்றும் 3 மட்டும்"},
            {"id": "C", "en": "1 and 3 only", "ta": "1 மற்றும் 3 மட்டும்"},
            {"id": "D", "en": "1, 2 and 3", "ta": "1, 2 மற்றும் 3"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "All three statements are correct. In Destruction of Public Properties, In re (2009), SC set up Claims Commissioners and authorized recovery from organizers to enforce Art 51A(i).",
            "ta": "மூன்று கூற்றுகளும் சரியானவை. பொதுச் சொத்துக்கள் சேதம் தொடர்பான 2009 வழக்கில், உறுப்பு 51A(i)-ஐ அமல்படுத்த உரிமைகோரல் ஆணையர்களை உச்ச நீதிமன்றம் அமைத்து அமைப்பாளர்களிடமிருந்து வசூலிக்க அனுமதித்தது."
        },
        "why_not_others": {
            "A": {"en": "Statement 3 is also correct.", "ta": "கூற்று 3-ம் சரியானது."},
            "B": {"en": "Statement 1 is also correct.", "ta": "கூற்று 1-ம் சரியானது."},
            "C": {"en": "Statement 2 is also correct.", "ta": "கூற்று 2-ம் சரியானது."},
            "D": {"en": "Correct. All statements 1, 2, and 3 are true.", "ta": "சரி. 1, 2 மற்றும் 3 ஆகிய அனைத்துக் கூற்றுகளும் உண்மை."}
        },
        "tnpsc_tip": {
            "en": "This SC guideline established financial accountability for violent mobs damaging buses and public buildings.",
            "ta": "இந்த உச்ச நீதிமன்ற வழிகாட்டுதல் பேருந்துகள் மற்றும் பொதுக் கட்டிடங்களைச் சேதப்படுத்தும் வன்முறைக் கூட்டத்திற்கு நிதிப் பொறுப்பை நிறுவியது."
        }
    },
    {
        "id": "FD_M_040",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Conceptual Comparison",
        "question": {
            "en": "Which of the following features accurately distinguishes Fundamental Rights (Part III) from Fundamental Duties (Part IVA)?",
            "ta": "அடிப்படை உரிமைகளை (பகுதி III) அடிப்படை கடமைகளிலிருந்து (பகுதி IVA) துல்லியமாக வேறுபடுத்தும் அம்சம் எது?"
        },
        "options": [
            {"id": "A", "en": "Fundamental Rights are justiciable commands protecting individual liberties; Fundamental Duties are non-justiciable commands promoting responsible citizenship", "ta": "அடிப்படை உரிமைகள் தனிநபர் சுதந்திரங்களைப் பாதுகாக்கும் அமல்படுத்தக்கூடிய கட்டளைகள்; அடிப்படை கடமைகள் பொறுப்பான குடியுரிமையை ஊக்குவிக்கும் அமல்படுத்த முடியாத கட்டளைகள்"},
            {"id": "B", "en": "Fundamental Rights were added in 1976; Fundamental Duties were present in 1950", "ta": "அடிப்படை உரிமைகள் 1976-ல் சேர்க்கப்பட்டன; அடிப்படை கடமைகள் 1950-ல் இருந்தன"},
            {"id": "C", "en": "Fundamental Rights apply only to citizens; Fundamental Duties apply to all aliens", "ta": "அடிப்படை உரிமைகள் குடிமக்களுக்கு மட்டுமே பொருந்தும்; அடிப்படை கடமைகள் அனைத்து வெளிநாட்டினருக்கும் பொருந்தும்"},
            {"id": "D", "en": "Fundamental Rights cannot be amended by Parliament; Fundamental Duties can be amended easily by executive order", "ta": "அடிப்படை உரிமைகளை நாடாளுமன்றத்தால் திருத்த முடியாது; அடிப்படை கடமைகளை நிர்வாக ஆணையால் எளிதில் திருத்தலாம்"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Statement A captures the exact functional distinction: Part III FRs are justiciable individual protections; Part IVA FDs are non-justiciable citizen responsibilities.",
            "ta": "கூற்று A சரியான செயல்பாட்டு வேறுபாட்டைப் பிடிக்கிறது: பகுதி III FRs என்பது அமல்படுத்தக்கூடிய தனிநபர் பாதுகாப்புகள்; பகுதி IVA FDs என்பது அமல்படுத்த முடியாத குடிமகன் பொறுப்புகள்."
        },
        "why_not_others": {
            "A": {"en": "Correct distinction.", "ta": "சரியான வேறுபாடு."},
            "B": {"en": "Reversed: FRs were present in 1950; FDs added in 1976.", "ta": "தலைகீழ்: FRs 1950-ல் இருந்தது; FDs 1976-ல் சேர்க்கப்பட்டது."},
            "C": {"en": "FDs apply exclusively to citizens.", "ta": "கடமைகள் குடிமக்களுக்கு மட்டுமே பொருந்தும்."},
            "D": {"en": "Both require constitutional amendments under Art 368.", "ta": "இரண்டிற்கும் உறுப்பு 368-ன் கீழ் அரசியலமைப்பு திருத்தங்கள் தேவை."}
        },
        "tnpsc_tip": {
            "en": "Part III = Individual Rights vs State | Part IVA = Citizen Duties towards Nation.",
            "ta": "பகுதி III = அரசுக்கு எதிராகத் தனிநபர் உரிமைகள் | பகுதி IVA = தேசத்தை நோக்கி குடிமகன் கடமைகள்."
        }
    },
    {
        "id": "FD_M_041",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Assertion & Reason",
        "question": {
            "en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Article 51A(j) requires every citizen to strive towards excellence in all spheres of individual and collective activity.\nReason (R): Individual excellence automatically leads to collective progress, causing the nation to constantly rise to higher levels of endeavor and achievement.\nIn the context of the above statements, which one of the following is correct?",
            "ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): உறுப்பு 51A(j) ஒவ்வொரு குடிமகனும் தனிநபர் மற்றும் கூட்டுச் செயல்பாடுகளின் அனைத்துத் துறைகளிலும் சிறப்பினை நோக்கி முயலக் கோருகிறது.\nகாரணம் (R): தனிநபர் சிறப்பு தானாகவே கூட்டு முன்னேற்றத்திற்கு வழிவகுத்து, தேசம் தொடர்ச்சியாக முயற்சி மற்றும் சாதனைகளின் உயர் நிலைகளுக்கு உயரக் காரணமாகிறது.\nமேற்கண்ட கூற்றுகளின் அடிப்படையில் பின்வருவனவற்றில் எது சரியானது?"
        },
        "options": [
            {"id": "A", "en": "Both A and R are correct and R is the correct explanation of A", "ta": "A மற்றும் R ஆகிய இரண்டும் சரி, மேலும் R என்பது A-வின் சரியான விளக்கமாகும்"},
            {"id": "B", "en": "Both A and R are correct but R is NOT the correct explanation of A", "ta": "A மற்றும் R ஆகிய இரண்டும் சரி, ஆனால் R என்பது A-வின் சரியான விளக்கம் அல்ல"},
            {"id": "C", "en": "A is correct but R is incorrect", "ta": "A சரி ஆனால் R தவறு"},
            {"id": "D", "en": "A is incorrect but R is correct", "ta": "A தவறு ஆனால் R சரி"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Both A and R are true. Reason R provides the explicit constitutional objective stated in Article 51A(j) for striving towards individual and collective excellence (A).",
            "ta": "A மற்றும் R ஆகிய இரண்டும் உண்மை. காரணம் R என்பது தனிநபர் மற்றும் கூட்டுச் சிறப்பை நோக்கி முயல்வதற்காக உறுப்பு 51A(j)-ல் கூறப்பட்டுள்ள வெளிப்படையான அரசியலமைப்பு நோக்கத்தை வழங்குகிறது (A)."
        },
        "why_not_others": {
            "A": {"en": "Correct. R is the exact reason for A.", "ta": "சரி. R என்பது A-விற்கான சரியான காரணமாகும்."},
            "B": {"en": "R directly explains A.", "ta": "R நேரடியாக A-வை விளக்குகிறது."},
            "C": {"en": "R is true.", "ta": "R உண்மையாகும்."},
            "D": {"en": "A is true.", "ta": "A உண்மையாகும்."}
        },
        "tnpsc_tip": {
            "en": "Art 51A(j) connects personal mastery with nation building.",
            "ta": "உறுப்பு 51A(j) தனிநபர் திறமையைத் தேச உருவாக்கத்துடன் இணைக்கிறது."
        }
    },
    {
        "id": "FD_M_042",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Statement-based",
        "question": {
            "en": "Consider the following statements regarding Fundamental Duties during a National Emergency under Article 352:\n1. Fundamental Duties under Article 51A are automatically suspended during a National Emergency.\n2. Fundamental Duties remain in operation during a National Emergency, and citizens are expected to maintain national discipline.\nWhich of the statements given above is/are correct?",
            "ta": "உறுப்பு 352-ன் கீழ் தேசிய அவசரநிலையின் போது அடிப்படை கடமைகள் பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. தேசிய அவசரநிலையின் போது உறுப்பு 51A-ன் கீழ் உள்ள அடிப்படை கடமைகள் தானாகவே நிறுத்தி வைக்கப்படும்.\n2. தேசிய அவசரநிலையின் போது அடிப்படை கடமைகள் தொடர்ந்து செயல்பாட்டில் இருக்கும், மேலும் குடிமக்கள் தேசிய ஒழுக்கத்தைப் பேணுவார்கள் என்று எதிர்பார்க்கப்படுகிறது.\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 only", "ta": "1 மட்டும்"},
            {"id": "B", "en": "2 only", "ta": "2 மட்டும்"},
            {"id": "C", "en": "Both 1 and 2", "ta": "1 மற்றும் 2 ஆகிய இரண்டும்"},
            {"id": "D", "en": "Neither 1 nor 2", "ta": "1 மற்றும் 2 ஆகிய இரண்டும் இல்லை"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "Statement 1 is incorrect: Fundamental Duties are NEVER suspended during Emergency. Statement 2 is correct: Duties operate continuously, especially during emergency situations when national defence [51A(d)] is paramount.",
            "ta": "கூற்று 1 தவறு: அவசரநிலையின் போது அடிப்படை கடமைகள் ஒருபோதும் நிறுத்தி வைக்கப்படுவதில்லை. கூற்று 2 சரி: கடமைகள் தொடர்ச்சியாகச் செயல்படுகின்றன, குறிப்பாக தேசியப் பாதுகாப்பு [51A(d)] முதன்மையாக இருக்கும் அவசரநிலைக் காலங்களில்."
        },
        "why_not_others": {
            "A": {"en": "Duties are not suspended during Emergency.", "ta": "அவசரநிலையின் போது கடமைகள் நிறுத்தி வைக்கப்படுவதில்லை."},
            "B": {"en": "Correct. Statement 2 is correct, while Statement 1 is incorrect.", "ta": "சரி. கூற்று 2 சரி, கூற்று 1 தவறு."},
            "C": {"en": "Statement 1 is false.", "ta": "கூற்று 1 தவறானது."},
            "D": {"en": "Statement 2 is true.", "ta": "கூற்று 2 உண்மையாகும்."}
        },
        "tnpsc_tip": {
            "en": "Fundamental Rights can be suspended under Arts 358/359 during Emergency, but Fundamental Duties are NEVER suspended.",
            "ta": "அவசரநிலையின் போது உறுப்புகள் 358/359-ன் கீழ் அடிப்படை உரிமைகள் நிறுத்தி வைக்கப்படலாம், ஆனால் அடிப்படை கடமைகள் ஒருபோதும் நிறுத்தி வைக்கப்படுவதில்லை."
        }
    },
    {
        "id": "FD_M_043",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Case Law",
        "question": {
            "en": "In Sachidanand Pandey v. State of West Bengal (1987), what principle did the Supreme Court state regarding Article 51A(g)?",
            "ta": "சச்சிதானந்த் பாண்டே vs மேற்கு வங்காள மாநிலம் (1987) வழக்கில், உறுப்பு 51A(g) தொடர்பாக உச்ச நீதிமன்றம் கூறிய தத்துவம் என்ன?"
        },
        "options": [
            {"id": "A", "en": "Whenever an ecological problem is brought before the court, the court is bound to bear in mind Article 48A and Article 51A(g)", "ta": "நீதிமன்றத்தின் முன் ஒரு சுற்றுச்சூழல் பிரச்சினை கொண்டு வரப்படும் போதெல்லாம், நீதிமன்றம் உறுப்பு 48A மற்றும் உறுப்பு 51A(g)-ஐ மனதில்கொள்ளக் கடமைப்பட்டுள்ளது"},
            {"id": "B", "en": "Environmental duties apply only to central government projects", "ta": "சுற்றுச்சூழல் கடமைகள் மத்திய அரசின் திட்டங்களுக்கு மட்டுமே பொருந்தும்"},
            {"id": "C", "en": "Courts cannot interfere in ecological matters as duties are non-justiciable", "ta": "கடமைகள் அமல்படுத்த முடியாதவை என்பதால் சுற்றுச்சூழல் விவகாரங்களில் நீதிமன்றங்கள் தலையிட முடியாது"},
            {"id": "D", "en": "Article 51A(g) was declared obsolete", "ta": "உறுப்பு 51A(g) காலாவதியானது என அறிவிக்கப்பட்டது"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "In Sachidanand Pandey (1987), SC held that whenever ecology is challenged, courts must keep Arts 48A and 51A(g) in mind when exercising judicial review.",
            "ta": "சச்சிதானந்த் பாண்டே (1987) வழக்கில், சுற்றுச்சூழல் சவாலுக்குட்படும் போதெல்லாம், நீதித்துறை ஆய்வைப் பயன்படுத்தும் போது நீதிமன்றங்கள் உறுப்புகள் 48A மற்றும் 51A(g)-ஐ மனதில்கொள்ள வேண்டும் என உச்ச நீதிமன்றம் தீர்ப்பளித்தது."
        },
        "why_not_others": {
            "A": {"en": "Correct. SC held courts are bound to consider Art 48A and Art 51A(g).", "ta": "சரி. நீதிமன்றங்கள் உறுப்பு 48A மற்றும் உறுப்பு 51A(g)-ஐக் கருதக் கடமைப்பட்டுள்ளன என உச்ச நீதிமன்றம் கூறியது."},
            "B": {"en": "Applies to all ecological issues.", "ta": "அனைத்து சுற்றுச்சூழல் பிரச்சினைகளுக்கும் பொருந்தும்."},
            "C": {"en": "Courts routinely interfere in ecological issues.", "ta": "சுற்றுச்சூழல் விவகாரங்களில் நீதிமன்றங்கள் வழக்கமாகத் தலையிடுகின்றன."},
            "D": {"en": "Art 51A(g) is an active provision.", "ta": "உறுப்பு 51A(g) ஒரு செயல்பாட்டில் உள்ள விதியாகும்."}
        },
        "tnpsc_tip": {
            "en": "Early milestone case where SC used Art 51A(g) to guide environmental judicial review.",
            "ta": "சுற்றுச்சூழல் நீதித்துறை ஆய்வை வழிநடத்த உச்ச நீதிமன்றம் உறுப்பு 51A(g)-ஐப் பயன்படுத்திய ஆரம்பகால மைல்கல் வழக்கு."
        }
    },
    {
        "id": "FD_M_044",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Statement-based",
        "question": {
            "en": "Consider the following statements regarding the term 'Integrity' in the Constitution:\n1. The word 'Integrity' was added to the Preamble by the 42nd Amendment Act 1976.\n2. The word 'Integrity' appears explicitly in Article 51A(c) ['To uphold and protect sovereignty, unity and integrity of India'].\nWhich of the statements given above is/are correct?",
            "ta": "அரசியலமைப்பில் 'ஒருமைப்பாடு' (Integrity) என்ற சொல் பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. 'ஒருமைப்பாடு' என்ற சொல் 42வது திருத்தச் சட்டம் 1976 மூலம் முகப்புரையில் சேர்க்கப்பட்டது.\n2. 'ஒருமைப்பாடு' என்ற சொல் உறுப்பு 51A(c)-ல் வெளிப்படையாக இடம்பெற்றுள்ளது ['இந்தியாவின் இறையாண்மை, ஒற்றுமை மற்றும் ஒருமைப்பாட்டைப் பேணிப் பாதுகாத்தல்'].\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 only", "ta": "1 மட்டும்"},
            {"id": "B", "en": "2 only", "ta": "2 மட்டும்"},
            {"id": "C", "en": "Both 1 and 2", "ta": "1 மற்றும் 2 ஆகிய இரண்டும்"},
            {"id": "D", "en": "Neither 1 nor 2", "ta": "1 மற்றும் 2 ஆகிய இரண்டும் இல்லை"}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "Both statements are correct. The 42nd Amendment 1976 introduced 'Integrity' into the Preamble and inserted Article 51A(c) containing 'Integrity'.",
            "ta": "இரண்டு கூற்றுகளும் சரியானவை. 42வது திருத்தம் 1976 முகப்புரையில் 'ஒருமைப்பாடு' என்பதை அறிமுகப்படுத்தியது மற்றும் 'ஒருமைப்பாடு' உள்ள உறுப்பு 51A(c)-ஐச் சேர்த்தது."
        },
        "why_not_others": {
            "A": {"en": "Statement 2 is also correct.", "ta": "கூற்று 2-ம் சரியானது."},
            "B": {"en": "Statement 1 is also correct.", "ta": "கூற்று 1-ம் சரியானது."},
            "C": {"en": "Correct. Both statements 1 and 2 are correct.", "ta": "சரி. 1 மற்றும் 2 ஆகிய இரண்டு கூற்றுகளும் சரி."},
            "D": {"en": "Both statements are true.", "ta": "இரண்டு கூற்றுகளும் உண்மை."}
        },
        "tnpsc_tip": {
            "en": "'Integrity' reinforces territorial and emotional oneness of the Indian nation.",
            "ta": "'ஒருமைப்பாடு' என்பது இந்திய தேசத்தின் நிலப்பரப்பு மற்றும் உணர்வுப்பூர்வமான ஒன்றுபட்ட தன்மையை வலுப்படுத்துகிறது."
        }
    },
    {
        "id": "FD_M_045",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Conceptual Distinction",
        "question": {
            "en": "How does 'Humanism' under Article 51A(h) conceptually differ from passive tolerance?",
            "ta": "உறுப்பு 51A(h)-ன் கீழ் உள்ள 'மனிதநேயம்' (Humanism) என்பது செயலற்ற சகிப்புத்தன்மையிலிருந்து தத்துவார்த்தமாக எவ்வாறு வேறுபடுகிறது?"
        },
        "options": [
            {"id": "A", "en": "Humanism is an active positive value emphasizing human dignity and welfare, whereas passive tolerance is merely enduring differences without active concern", "ta": "மனிதநேயம் என்பது மனித கண்ணியம் மற்றும் நலனை வலியுறுத்தும் செயலில் உள்ள நேர்மறை மதிப்பாகும், ஆனால் செயலற்ற சகிப்புத்தன்மை என்பது செயலில் உள்ள அக்கறையின்றி வேறுபாடுகளைப் பொறுத்துக் கொள்வது மட்டுமே"},
            {"id": "B", "en": "Humanism applies only to government servants, while tolerance applies to citizens", "ta": "மனிதநேயம் அரசு ஊழியர்களுக்கு மட்டுமே பொருந்தும், சகிப்புத்தன்மை குடிமக்களுக்குப் பொருந்தும்"},
            {"id": "C", "en": "Humanism is banned under Article 25", "ta": "உறுப்பு 25-ன் கீழ் மனிதநேயம் தடை செய்யப்பட்டுள்ளது"},
            {"id": "D", "en": "There is no conceptual difference between humanism and tolerance", "ta": "மனிதநேயத்திற்கும் சகிப்புத்தன்மைக்கும் இடையே தத்துவார்த்த வேறுபாடு இல்லை"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Humanism under Art 51A(h) is an active, positive value prioritizing human welfare, reason, and compassion, whereas passive tolerance is merely refraining from conflict.",
            "ta": "உறுப்பு 51A(h)-ன் கீழ் உள்ள மனிதநேயம் என்பது மனித நலன், பகுத்தறிவு மற்றும் கருணைக்கு முன்னுரிமை அளிக்கும் செயலில் உள்ள நேர்மறை மதிப்பாகும், ஆனால் செயலற்ற சகிப்புத்தன்மை என்பது மோதலைத் தவிர்ப்பது மட்டுமே."
        },
        "why_not_others": {
            "A": {"en": "Correct conceptual distinction.", "ta": "சரியான தத்துவார்த்த வேறுபாடு."},
            "B": {"en": "Applies to all citizens.", "ta": "அனைத்துக் குடிமக்களுக்கும் பொருந்தும்."},
            "C": {"en": "Art 25 guarantees freedom of conscience.", "ta": "உறுப்பு 25 மனச்சாட்சி சுதந்திரத்தை உத்தரவாதம் செய்கிறது."},
            "D": {"en": "There is a distinct difference.", "ta": "தெளிவான வேறுபாடு உள்ளது."}
        },
        "tnpsc_tip": {
            "en": "Art 51A(h) pairs Humanism with Scientific Temper and Reform.",
            "ta": "உறுப்பு 51A(h) மனிதநேயத்தை அறிவியல் மனப்பான்மை மற்றும் சீர்திருத்தத்துடன் இணைக்கிறது."
        }
    },
    {
        "id": "FD_M_046",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Assertion & Reason",
        "question": {
            "en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Mahatma Gandhi emphasized that the true source of rights is duty.\nReason (R): If we all discharge our duties, rights will not be far to seek, but if we run after rights without performing duties, they will escape us like a will-o'-the-wisp.\nIn the context of the above statements, which one of the following is correct?",
            "ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): உரிமைகளின் உண்மையான ஊற்றுக்கண் கடமையே என்று மகாத்மா காந்தி வலியுறுத்தினார்.\nகாரணம் (R): நாம் அனைவரும் நம் கடமைகளைச் செய்தால், உரிமைகள் வெகு தொலைவில் இருக்காது, ஆனால் கடமைகளைச் செய்யாமல் உரிமைகளின் பின்னால் ஓடினால், அவை எம்மை விட்டு விலகிச் செல்லும்.\nமேற்கண்ட கூற்றுகளின் அடிப்படையில் பின்வருவனவற்றில் எது சரியானது?"
        },
        "options": [
            {"id": "A", "en": "Both A and R are correct and R is the correct explanation of A", "ta": "A மற்றும் R ஆகிய இரண்டும் சரி, மேலும் R என்பது A-வின் சரியான விளக்கமாகும்"},
            {"id": "B", "en": "Both A and R are correct but R is NOT the correct explanation of A", "ta": "A மற்றும் R ஆகிய இரண்டும் சரி, ஆனால் R என்பது A-வின் சரியான விளக்கம் அல்ல"},
            {"id": "C", "en": "A is correct but R is incorrect", "ta": "A சரி ஆனால் R தவறு"},
            {"id": "D", "en": "A is incorrect but R is correct", "ta": "A தவறு ஆனால் R சரி"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Both A and R are true. Reason R is the exact philosophical quote of Mahatma Gandhi explaining why duty is the source of rights (A).",
            "ta": "A மற்றும் R ஆகிய இரண்டும் உண்மை. காரணம் R என்பது ஏன் கடமை உரிமைகளின் ஊற்றுக்கண் என்பதை விளக்கும் மகாத்மா காந்தியின் சரியான தத்துவார்த்த மேற்கோளாகும் (A)."
        },
        "why_not_others": {
            "A": {"en": "Correct. R is Gandhi's exact quote explaining A.", "ta": "சரி. R என்பது A-வை விளக்கும் காந்தியின் சரியான மேற்கோளாகும்."},
            "B": {"en": "R directly explains A.", "ta": "R நேரடியாக A-வை விளக்குகிறது."},
            "C": {"en": "R is true.", "ta": "R உண்மையாகும்."},
            "D": {"en": "A is true.", "ta": "A உண்மையாகும்."}
        },
        "tnpsc_tip": {
            "en": "Gandhian philosophy heavily inspired the inclusion of civic duty balance in Indian polity.",
            "ta": "காந்தியத் தத்துவம் இந்திய ஆட்சியில் குடிமை கடமை சமநிலையைச் சேர்ப்பதற்கு பெரிதும் ஊக்கமளித்தது."
        }
    },
    {
        "id": "FD_M_047",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Statement-based",
        "question": {
            "en": "Consider the following statements regarding the Justice Verma Committee (1999) recommendations:\n1. It recommended that 3rd January should be celebrated nationwide as Fundamental Duties Day.\n2. It recommended that duty-awareness modules should be integrated into school textbooks and teacher training programs.\nWhich of the statements given above is/are correct?",
            "ta": "நீதிபதி வர்மா குழு (1999) பரிந்துரைகள் பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. ஜனவரி 3 நாடு முழுவதும் அடிப்படை கடமைகள் நாளாகக் கொண்டாடப்பட வேண்டும் என்று அது பரிந்துரைத்தது.\n2. கடமை விழிப்புணர்வு தொகுதிகள் பள்ளி பாடப்புத்தகங்கள் மற்றும் ஆசிரியர் பயிற்சி திட்டங்களில் ஒருங்கிணைக்கப்பட வேண்டும் என்று அது பரிந்துரைத்தது.\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 only", "ta": "1 மட்டும்"},
            {"id": "B", "en": "2 only", "ta": "2 மட்டும்"},
            {"id": "C", "en": "Both 1 and 2", "ta": "1 மற்றும் 2 ஆகிய இரண்டும்"},
            {"id": "D", "en": "Neither 1 nor 2", "ta": "1 மற்றும் 2 ஆகிய இரண்டும் இல்லை"}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "Both statements are correct. Verma Committee (1999) recommended observing 3rd January (enforcement date of 42nd CAA) and integrating duty awareness into educational curricula.",
            "ta": "இரண்டு கூற்றுகளும் சரியானவை. வர்மா குழு (1999) ஜனவரி 3-ஐ (42வது திருத்தம் அமலான நாள்) அனுசரிக்கவும் கல்விப் பாடத்திட்டத்தில் கடமை விழிப்புணர்வை ஒருங்கிணைக்கவும் பரிந்துரைத்தது."
        },
        "why_not_others": {
            "A": {"en": "Statement 2 is also correct.", "ta": "கூற்று 2-ம் சரியானது."},
            "B": {"en": "Statement 1 is also correct.", "ta": "கூற்று 1-ம் சரியானது."},
            "C": {"en": "Correct. Both statements 1 and 2 are correct.", "ta": "சரி. 1 மற்றும் 2 ஆகிய இரண்டு கூற்றுகளும் சரி."},
            "D": {"en": "Both statements are true.", "ta": "இரண்டு கூற்றுகளும் உண்மை."}
        },
        "tnpsc_tip": {
            "en": "Verma Committee focused heavily on educational and pedagogical dissemination of Fundamental Duties.",
            "ta": "வர்மா குழு அடிப்படை கடமைகளைக் கல்வி மற்றும் கற்பித்தல் மூலம் பரப்புவதில் பெரிதும் கவனம் செலுத்தியது."
        }
    },
    {
        "id": "FD_M_048",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Comparison",
        "question": {
            "en": "Which of the following correctly pairs the age limits specified in Article 45 DPSP and Article 51A(k) Fundamental Duty?",
            "ta": "உறுப்பு 45 DPSP மற்றும் உறுப்பு 51A(k) அடிப்படை கடமை ஆகியவற்றில் குறிப்பிடப்பட்டுள்ள வயது வரம்புகளைப் பின்வருவனவற்றில் எது சரியாக ஜோடியாகக் காட்டுகிறது?"
        },
        "options": [
            {"id": "A", "en": "Article 45: Below 6 years | Article 51A(k): 6 to 14 years", "ta": "உறுப்பு 45: 6 வயதிற்குட்பட்டோர் | உறுப்பு 51A(k): 6 முதல் 14 வயது வரை"},
            {"id": "B", "en": "Article 45: 6 to 14 years | Article 51A(k): Below 6 years", "ta": "உறுப்பு 45: 6 முதல் 14 வயது வரை | உறுப்பு 51A(k): 6 வயதிற்குட்பட்டோர்"},
            {"id": "C", "en": "Article 45: 0 to 18 years | Article 51A(k): 14 to 18 years", "ta": "உறுப்பு 45: 0 முதல் 18 வயது வரை | உறுப்பு 51A(k): 14 முதல் 18 வயது வரை"},
            {"id": "D", "en": "Both Articles specify the exact same age limit of 0 to 14 years", "ta": "இரண்டு உறுப்புகளுமே 0 முதல் 14 வயது என்ற ஒரே மாதிரியான வயது வரம்பைக் குறிப்பிடுகின்றன"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Following the 86th CAA 2002, Article 45 DPSP specifies early childhood care for children BELOW 6 years, while Article 51A(k) FD specifies education opportunities for children AGED 6 TO 14 years.",
            "ta": "86வது திருத்தம் 2002க்கு பின், உறுப்பு 45 DPSP 6 வயதிற்குட்பட்ட குழந்தைகளுக்கான முன்பருவப் பராமரிப்பைக் குறிப்பிடுகிறது, ஆனால் உறுப்பு 51A(k) FD 6 முதல் 14 வயது வரையிலான குழந்தைகளுக்கான கல்வி வாய்ப்புகளைக் குறிப்பிடுகிறது."
        },
        "why_not_others": {
            "A": {"en": "Correct age pairing.", "ta": "சரியான வயது ஜோடி."},
            "B": {"en": "Reversed age limits.", "ta": "தலைகீழ் வயது வரம்புகள்."},
            "C": {"en": "Incorrect age limits.", "ta": "தவறான வயது வரம்புகள்."},
            "D": {"en": "They have distinct non-overlapping age brackets.", "ta": "அவை வெவ்வேறு பிளவற்ற வயதுப் பிரிவுகளைக் கொண்டுள்ளன."}
        },
        "tnpsc_tip": {
            "en": "Art 45 = Below 6 yrs | Art 21A & 51A(k) = 6 to 14 yrs.",
            "ta": "உறுப்பு 45 = 6 வயதிற்குட்பட்டோர் | உறுப்பு 21A & 51A(k) = 6 முதல் 14 வயது வரை."
        }
    },
    {
        "id": "FD_M_049",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Statement-based",
        "question": {
            "en": "Consider the following statements regarding statutory enforcement of Fundamental Duties:\n1. A Fundamental Duty itself cannot be used by a citizen as a direct cause of action to file a civil suit for damages against another citizen.\n2. Parliament can create specific statutory offenses and civil liabilities to punish non-compliance with the principles contained in Article 51A.\nWhich of the statements given above is/are correct?",
            "ta": "அடிப்படை கடமைகளின் சட்டப்பூர்வ அமலாக்கம் பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. மற்றொரு குடிமகனுக்கு எதிராக நஷ்டஈடு கோரி சிவில் வழக்கு தொடர ஒரு குடிமகன் அடிப்படை கடமையை நேரடியாகப் பயன்படுத்த முடியாது.\n2. உறுப்பு 51A-ல் உள்ள தத்துவங்களை மீறுவதற்குத் தண்டனை வழங்க நாடாளுமன்றம் குறிப்பிட்ட சட்டப்பூர்வ குற்றங்களையும் சிவில் பொறுப்புகளையும் உருவாக்கலாம்.\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 only", "ta": "1 மட்டும்"},
            {"id": "B", "en": "2 only", "ta": "2 மட்டும்"},
            {"id": "C", "en": "Both 1 and 2", "ta": "1 மற்றும் 2 ஆகிய இரண்டும்"},
            {"id": "D", "en": "Neither 1 nor 2", "ta": "1 மற்றும் 2 ஆகிய இரண்டும் இல்லை"}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "Both statements are correct. Art 51A duties are non-justiciable between private individuals directly (Statement 1), but Parliament has plenary power to enact statutes penalizing non-compliance (Statement 2).",
            "ta": "இரண்டு கூற்றுகளும் சரியானவை. உறுப்பு 51A கடமைகள் தனியார் தனிநபர்களுக்கு இடையே நேரடியாக அமல்படுத்த முடியாதவை (கூற்று 1), ஆனால் மீறுபவர்களைத் தண்டிக்கச் சட்டங்களை இயற்ற நாடாளுமன்றத்திற்கு அதிகாரம் உண்டு (கூற்று 2)."
        },
        "why_not_others": {
            "A": {"en": "Statement 2 is also correct.", "ta": "கூற்று 2-ம் சரியானது."},
            "B": {"en": "Statement 1 is also correct.", "ta": "கூற்று 1-ம் சரியானது."},
            "C": {"en": "Correct. Both statements 1 and 2 are correct.", "ta": "சரி. 1 மற்றும் 2 ஆகிய இரண்டு கூற்றுகளும் சரி."},
            "D": {"en": "Both statements are true.", "ta": "இரண்டு கூற்றுகளும் உண்மை."}
        },
        "tnpsc_tip": {
            "en": "Non-justiciability means duties need a statutory bridge passed by Parliament to become enforceable law.",
            "ta": "அமல்படுத்த முடியாதது என்றால் கடமைகள் அமல்படுத்தக்கூடிய சட்டமாக மாற நாடாளுமன்றம் நிறைவேற்றிய சட்டப்பூர்வ பாலம் தேவை."
        }
    },
    {
        "id": "FD_M_050",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Case Law",
        "question": {
            "en": "In Minerva Mills v. Union of India (1980), the Supreme Court laid down a foundational doctrine regarding Part III, Part IV, and Part IVA. What is that doctrine?",
            "ta": "மினர்வா மில்ஸ் vs இந்திய யூனியன் (1980) வழக்கில், பகுதி III, பகுதி IV, மற்றும் பகுதி IVA தொடர்பாக உச்ச நீதிமன்றம் ஒரு அடித்தளக் கோட்பாட்டை வழங்கியது. அந்த கோட்பாடு என்ன?"
        },
        "options": [
            {"id": "A", "en": "The harmony and balance between Fundamental Rights, DPSP, and Fundamental Duties forms an essential feature of the Basic Structure of the Constitution", "ta": "அடிப்படை உரிமைகள், DPSP, மற்றும் அடிப்படை கடமைகள் இடையேயான இணக்கம் மற்றும் சமநிலை அரசியலமைப்பின் அடிப்படை அமைப்பின் அத்தியாவசிய அம்சமாகும்"},
            {"id": "B", "en": "Fundamental Rights completely destroy DPSP and Fundamental Duties during conflict", "ta": "முரண்பாட்டின் போது அடிப்படை உரிமைகள் DPSP மற்றும் அடிப்படை கடமைகளை முற்றிலுமாக அழிக்கின்றன"},
            {"id": "C", "en": "Fundamental Duties override Fundamental Rights in all circumstances", "ta": "அனைத்துச் சூழல்களிலும் அடிப்படை கடமைகள் அடிப்படை உரிமைகளை மிஞ்சுகின்றன"},
            {"id": "D", "en": "Part IVA was declared void by Minerva Mills judgment", "ta": "மினர்வா மில்ஸ் தீர்ப்பால் பகுதி IVA செல்லாததாக்கப்பட்டது"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "In Minerva Mills (1980), SC held that harmony and balance between Part III (Rights), Part IV (DPSP), and Part IVA (Duties) is an essential element of the Basic Structure of the Indian Constitution.",
            "ta": "மினர்வா மில்ஸ் (1980) வழக்கில், பகுதி III (உரிமைகள்), பகுதி IV (DPSP), மற்றும் பகுதி IVA (கடமைகள்) இடையேயான இணக்கம் மற்றும் சமநிலை இந்திய அரசியலமைப்பின் அடிப்படை அமைப்பின் அத்தியாவசிய அம்சமாகும் என உச்ச நீதிமன்றம் தீர்ப்பளித்தது."
        },
        "why_not_others": {
            "A": {"en": "Correct. Fundamental harmony forms part of Basic Structure.", "ta": "சரி. அடிப்படை இணக்கம் அடிப்படை அமைப்பின் பகுதியாகும்."},
            "B": {"en": "They do not destroy each other; they balance each other.", "ta": "அவை ஒன்றை ஒன்று அழிப்பதில்லை; ஒன்றை ஒன்று சமநிலைப்படுத்துகின்றன."},
            "C": {"en": "Duties do not override rights.", "ta": "கடமைகள் உரிமைகளை மிஞ்சுவதில்லை."},
            "D": {"en": "Part IVA was upheld.", "ta": "பகுதி IVA நிலைநிறுத்தப்பட்டது."}
        },
        "tnpsc_tip": {
            "en": "Minerva Mills 1980 established that no single Part of the Constitution should be elevated to destroy another.",
            "ta": "மினர்வா மில்ஸ் 1980 அரசியலமைப்பின் எந்தவொரு தனிப் பகுதியையும் மற்றொன்றை அழிக்கும் வகையில் உயர்த்தக் கூடாது என்பதை நிறுவியது."
        }
    }
]

target_file = "data/questions/polity/fundamental_duties_medium.json"
os.makedirs(os.path.dirname(target_file), exist_ok=True)

with open(target_file, "w", encoding="utf-8") as f:
    json.dump(questions_data, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {len(questions_data)} Medium questions in {target_file}")
