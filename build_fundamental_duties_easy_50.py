# -*- coding: utf-8 -*-
"""
Script to build 50 High-Yield Easy MCQs for Fundamental Duties with Balanced Answer Distribution (A, B, C, D)
Target File: data/questions/polity/fundamental_duties_easy.json
"""

import json
import os

# 50 Easy Questions with balanced A, B, C, D answer keys
questions_data = [
    {
        "id": "FD_E_001",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Direct",
        "question": {
            "en": "Which Part of the Constitution of India contains the Fundamental Duties?",
            "ta": "இந்திய அரசியலமைப்பின் எந்தப் பகுதியில் அடிப்படை கடமைகள் இடம்பெற்றுள்ளன?"
        },
        "options": [
            {"id": "A", "en": "Part IVA", "ta": "பகுதி IVA"},
            {"id": "B", "en": "Part III", "ta": "பகுதி III"},
            {"id": "C", "en": "Part IV", "ta": "பகுதி IV"},
            {"id": "D", "en": "Part V", "ta": "பகுதி V"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Part IVA of the Constitution of India contains the Fundamental Duties under Article 51A.",
            "ta": "இந்திய அரசியலமைப்பின் பகுதி IVA-ல் உறுப்பு 51A-ன் கீழ் அடிப்படை கடமைகள் பொறிக்கப்பட்டுள்ளன."
        },
        "why_not_others": {
            "A": {"en": "Correct. Part IVA contains Fundamental Duties.", "ta": "சரி. பகுதி IVA அடிப்படை கடமைகளைக் கொண்டுள்ளது."},
            "B": {"en": "Part III contains Fundamental Rights (Articles 12-35).", "ta": "பகுதி III அடிப்படை உரிமைகளைக் கொண்டுள்ளது (உறுப்புகள் 12-35)."},
            "C": {"en": "Part IV contains Directive Principles of State Policy (Articles 36-51).", "ta": "பகுதி IV அரசு வழிகாட்டு நெறிமுறைகளைக் கொண்டுள்ளது (உறுப்புகள் 36-51)."},
            "D": {"en": "Part V deals with The Union Government (Articles 52-151).", "ta": "பகுதி V ஒன்றிய அரசாங்கம் பற்றியது (உறுப்புகள் 52-151)."}
        },
        "tnpsc_tip": {
            "en": "Part IVA was inserted into the Constitution by the 42nd Amendment Act, 1976.",
            "ta": "1976-ன் 42வது திருத்தச் சட்டத்தின் மூலம் பகுதி IVA அரசியலமைப்பில் சேர்க்கப்பட்டது."
        }
    },
    {
        "id": "FD_E_002",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Article-based",
        "question": {
            "en": "Which Article of the Indian Constitution enumerates the Fundamental Duties of citizens?",
            "ta": "இந்திய அரசியலமைப்பின் எந்த உறுப்பு குடிமக்களின் அடிப்படை கடமைகளைப் பட்டியலிடுகிறது?"
        },
        "options": [
            {"id": "A", "en": "Article 51", "ta": "உறுப்பு 51"},
            {"id": "B", "en": "Article 51A", "ta": "உறுப்பு 51A"},
            {"id": "C", "en": "Article 32", "ta": "உறுப்பு 32"},
            {"id": "D", "en": "Article 45", "ta": "உறுப்பு 45"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "Article 51A is the sole Article in Part IVA that lists all the Fundamental Duties of Indian citizens.",
            "ta": "பகுதி IVA-ல் உள்ள ஒரே உறுப்பான உறுப்பு 51A இந்தியக் குடிமக்களின் அனைத்து அடிப்படை கடமைகளையும் பட்டியலிடுகிறது."
        },
        "why_not_others": {
            "A": {"en": "Article 51 deals with Promotion of international peace and security (DPSP).", "ta": "உறுப்பு 51 சர்வதேச அமைதி மற்றும் பாதுகாப்பை மேம்படுத்துவது பற்றியது (DPSP)."},
            "B": {"en": "Correct. Article 51A enumerates Fundamental Duties.", "ta": "சரி. உறுப்பு 51A அடிப்படை கடமைகளைப் பட்டியலிடுகிறது."},
            "C": {"en": "Article 32 provides Writs for enforcement of Fundamental Rights.", "ta": "உறுப்பு 32 அடிப்படை உரிமைகளை அமல்படுத்துவதற்கான பேராணைகளை வழங்குகிறது."},
            "D": {"en": "Article 45 deals with early childhood care and education below 6 years (DPSP).", "ta": "உறுப்பு 45 6 வயதிற்குட்பட்ட குழந்தைகளுக்கான முன்பருவக் கல்வி பற்றியது (DPSP)."}
        },
        "tnpsc_tip": {
            "en": "Article 51A originally had 10 clauses (a to j); clause (k) was added in 2002.",
            "ta": "உறுப்பு 51A-ல் முதலில் 10 உட்பிரிவுகள் (a முதல் j வரை) இருந்தன; உட்பிரிவு (k) 2002-ல் சேர்க்கப்பட்டது."
        }
    },
    {
        "id": "FD_E_003",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Amendment-based",
        "question": {
            "en": "Which Constitutional Amendment Act incorporated Part IVA and Article 51A into the Constitution of India?",
            "ta": "எந்த அரசியலமைப்பு திருத்தச் சட்டம் பகுதி IVA மற்றும் உறுப்பு 51A ஆகியவற்றை இந்திய அரசியலமைப்பில் சேர்த்தது?"
        },
        "options": [
            {"id": "A", "en": "44th Amendment Act, 1978", "ta": "44வது திருத்தச் சட்டம், 1978"},
            {"id": "B", "en": "86th Amendment Act, 2002", "ta": "86வது திருத்தச் சட்டம், 2002"},
            {"id": "C", "en": "42nd Amendment Act, 1976", "ta": "42வது திருத்தச் சட்டம், 1976"},
            {"id": "D", "en": "73rd Amendment Act, 1992", "ta": "73வது திருத்தச் சட்டம், 1992"}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "The 42nd Constitutional Amendment Act, 1976 introduced Part IVA and Article 51A containing 10 Fundamental Duties.",
            "ta": "1976-ன் 42வது அரசியலமைப்பு திருத்தச் சட்டம் 10 அடிப்படை கடமைகளைக் கொண்ட பகுதி IVA மற்றும் உறுப்பு 51A ஐ அறிமுகப்படுத்தியது."
        },
        "why_not_others": {
            "A": {"en": "44th Amendment 1978 deleted Right to Property from Fundamental Rights.", "ta": "44வது திருத்தம் 1978 சொத்து உரிமையை அடிப்படை உரிமைகளிலிருந்து நீக்கியது."},
            "B": {"en": "86th Amendment 2002 added the 11th duty [Art 51A(k)].", "ta": "86வது திருத்தம் 2002 11வது கடமையைச் சேர்த்தது [உறுப்பு 51A(k)]."},
            "C": {"en": "Correct. 42nd Amendment 1976 added Part IVA.", "ta": "சரி. 42வது திருத்தம் 1976 பகுதி IVA-ஐச் சேர்த்தது."},
            "D": {"en": "73rd Amendment 1992 gave constitutional status to Panchayati Raj.", "ta": "73வது திருத்தம் 1992 பஞ்சாயத்து ராஜிற்கு அரசியலமைப்பு அந்தஸ்து அளித்தது."}
        },
        "tnpsc_tip": {
            "en": "The 42nd Amendment Act, 1976 is also known as the 'Mini-Constitution'.",
            "ta": "42வது திருத்தச் சட்டம், 1976 'குறு அரசியலமைப்பு' என்றும் அழைக்கப்படுகிறது."
        }
    },
    {
        "id": "FD_E_004",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Direct",
        "question": {
            "en": "How many Fundamental Duties were originally added to the Constitution by the 42nd Constitutional Amendment Act, 1976?",
            "ta": "1976-ன் 42வது அரசியலமைப்பு திருத்தச் சட்டத்தின் மூலம் அரசியலமைப்பில் முதலில் எத்தனை அடிப்படை கடமைகள் சேர்க்கப்பட்டன?"
        },
        "options": [
            {"id": "A", "en": "8 Duties", "ta": "8 கடமைகள்"},
            {"id": "B", "en": "11 Duties", "ta": "11 கடமைகள்"},
            {"id": "C", "en": "12 Duties", "ta": "12 கடமைகள்"},
            {"id": "D", "en": "10 Duties", "ta": "10 கடமைகள்"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "The 42nd Amendment Act 1976 added TEN (10) Fundamental Duties to the Constitution in 1976.",
            "ta": "42வது திருத்தச் சட்டம் 1976-ல் அரசியலமைப்பில் பத்து (10) அடிப்படை கடமைகளைச் சேர்த்தது."
        },
        "why_not_others": {
            "A": {"en": "8 duties were recommended by Swaran Singh Committee, but Parliament enacted 10.", "ta": "ஸ்வரன் சிங் குழு 8 கடமைகளைப் பரிந்துரைத்தது, ஆனால் நாடாளுமன்றம் 10 இயற்றியது."},
            "B": {"en": "11 is the PRESENT count after 86th Amendment 2002.", "ta": "86வது திருத்தம் 2002க்கு பின் தற்போதைய எண்ணிக்கை 11 ஆகும்."},
            "C": {"en": "Incorrect option.", "ta": "தவறான விருப்பம்."},
            "D": {"en": "Correct. Originally 10 duties were added in 1976.", "ta": "சரி. 1976-ல் முதலில் 10 கடமைகள் சேர்க்கப்பட்டன."}
        },
        "tnpsc_tip": {
            "en": "Do not confuse the recommended count (8) with the enacted count (10).",
            "ta": "பரிந்துரைக்கப்பட்ட எண்ணிக்கையையும் (8) இயற்றப்பட்ட எண்ணிக்கையையும் (10) குழப்பிக் கொள்ள வேண்டாம்."
        }
    },
    {
        "id": "FD_E_005",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Direct",
        "question": {
            "en": "What is the present total number of Fundamental Duties in the Constitution of India?",
            "ta": "இந்திய அரசியலமைப்பில் தற்போதைய மொத்த அடிப்படை கடமைகளின் எண்ணிக்கை என்ன?"
        },
        "options": [
            {"id": "A", "en": "11 Duties", "ta": "11 கடமைகள்"},
            {"id": "B", "en": "10 Duties", "ta": "10 கடமைகள்"},
            {"id": "C", "en": "9 Duties", "ta": "9 கடமைகள்"},
            {"id": "D", "en": "12 Duties", "ta": "12 கடமைகள்"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "There are presently ELEVEN (11) Fundamental Duties in Article 51A of the Indian Constitution.",
            "ta": "இந்திய அரசியலமைப்பின் உறுப்பு 51A-ல் தற்போது பதினொன்று (11) அடிப்படை கடமைகள் உள்ளன."
        },
        "why_not_others": {
            "A": {"en": "Correct. Present total is 11 Duties.", "ta": "சரி. தற்போதைய மொத்தம் 11 கடமைகள் ஆகும்."},
            "B": {"en": "10 was the original count in 1976.", "ta": "10 என்பது 1976-ன் அசல் எண்ணிக்கையாகும்."},
            "C": {"en": "Incorrect count.", "ta": "தவறான எண்ணிக்கை."},
            "D": {"en": "Incorrect count.", "ta": "தவறான எண்ணிக்கை."}
        },
        "tnpsc_tip": {
            "en": "The 11th Duty was added by the 86th Constitutional Amendment Act, 2002.",
            "ta": "11வது கடமை 2002-ன் 86வது அரசியலமைப்பு திருத்தச் சட்டத்தால் சேர்க்கப்பட்டது."
        }
    },
    {
        "id": "FD_E_006",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Direct",
        "question": {
            "en": "Which Committee recommended the inclusion of Fundamental Duties in the Constitution of India?",
            "ta": "இந்திய அரசியலமைப்பில் அடிப்படை கடமைகளைச் சேர்க்கப் பரிந்துரைத்த குழு எது?"
        },
        "options": [
            {"id": "A", "en": "Sarkaria Commission", "ta": "சர்க்காரியா ஆணையம்"},
            {"id": "B", "en": "Sardar Swaran Singh Committee", "ta": "சர்தார் ஸ்வரன் சிங் குழு"},
            {"id": "C", "en": "Balwant Rai Mehta Committee", "ta": "பல்வந்த் ராய் மேத்தா குழு"},
            {"id": "D", "en": "Kothari Commission", "ta": "கோத்தாரி ஆணையம்"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "The Sardar Swaran Singh Committee (1976) recommended the incorporation of Fundamental Duties into the Constitution.",
            "ta": "சர்தார் ஸ்வரன் சிங் குழு (1976) அரசியலமைப்பில் அடிப்படை கடமைகளை இணைக்கப் பரிந்துரைத்தது."
        },
        "why_not_others": {
            "A": {"en": "Sarkaria Commission dealt with Centre-State relations (1983).", "ta": "சர்க்காரியா ஆணையம் மத்திய-மாநில உறவுகள் பற்றியது (1983)."},
            "B": {"en": "Correct. Swaran Singh Committee recommended Fundamental Duties.", "ta": "சரி. ஸ்வரன் சிங் குழு அடிப்படை கடமைகளைப் பரிந்துரைத்தது."},
            "C": {"en": "Balwant Rai Mehta Committee dealt with Panchayati Raj (1957).", "ta": "பல்வந்த் ராய் மேத்தா குழு பஞ்சாயத்து ராஜ் பற்றியது (1957)."},
            "D": {"en": "Kothari Commission dealt with Education policy (1964).", "ta": "கோத்தாரி ஆணையம் கல்விக் கொள்கை பற்றியது (1964)."}
        },
        "tnpsc_tip": {
            "en": "Swaran Singh Committee was set up by Congress Government in 1976 during Emergency.",
            "ta": "ஸ்வரன் சிங் குழு 1976 அவசரநிலையின் போது காங்கிரஸ் அரசால் அமைக்கப்பட்டது."
        }
    },
    {
        "id": "FD_E_007",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Amendment-based",
        "question": {
            "en": "Which Constitutional Amendment Act added the 11th Fundamental Duty [Article 51A(k)] to the Constitution?",
            "ta": "எந்த அரசியலமைப்பு திருத்தச் சட்டம் அரசியலமைப்பில் 11வது அடிப்படை கடமையை [உறுப்பு 51A(k)] சேர்த்தது?"
        },
        "options": [
            {"id": "A", "en": "42nd Amendment Act, 1976", "ta": "42வது திருத்தச் சட்டம், 1976"},
            {"id": "B", "en": "44th Amendment Act, 1978", "ta": "44வது திருத்தச் சட்டம், 1978"},
            {"id": "C", "en": "86th Amendment Act, 2002", "ta": "86வது திருத்தச் சட்டம், 2002"},
            {"id": "D", "en": "91st Amendment Act, 2003", "ta": "91வது திருத்தச் சட்டம், 2003"}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "The 86th Constitutional Amendment Act, 2002 added the 11th Fundamental Duty [Art 51A(k)] obligating parents to provide education opportunities to children aged 6-14.",
            "ta": "86வது அரசியலமைப்பு திருத்தச் சட்டம், 2002 6-14 வயது குழந்தைகளுக்குக் கல்வி வாய்ப்பளிக்கப் பெற்றோருக்குக் கடமையாக்கும் 11வது அடிப்படை கடமையைச் சேர்த்தது."
        },
        "why_not_others": {
            "A": {"en": "42nd Amendment 1976 added the original 10 duties.", "ta": "42வது திருத்தம் 1976 அசல் 10 கடமைகளைச் சேர்த்தது."},
            "B": {"en": "44th Amendment 1978 modified Emergency provisions & Right to Property.", "ta": "44வது திருத்தம் 1978 அவசரநிலை விதிகள் & சொத்து உரிமையை மாற்றியது."},
            "C": {"en": "Correct. 86th Amendment 2002 added the 11th duty.", "ta": "சரி. 86வது திருத்தம் 2002 11வது கடமையைச் சேர்த்தது."},
            "D": {"en": "91st Amendment 2003 limited Council of Ministers size to 15%.", "ta": "91வது திருத்தம் 2003 அமைச்சரவை அளவை 15% ஆகக் கட்டுப்படுத்தியது."}
        },
        "tnpsc_tip": {
            "en": "86th CAA 2002 simultaneously added Art 21A (FR), Art 51A(k) (FD), and modified Art 45 (DPSP).",
            "ta": "86வது திருத்தம் 2002 ஒரே நேரத்தில் உறுப்பு 21A (FR), உறுப்பு 51A(k) (FD) ஆகியவற்றைச் சேர்த்து உறுப்பு 45 (DPSP) ஐ மாற்றியது."
        }
    },
    {
        "id": "FD_E_008",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Direct",
        "question": {
            "en": "The concept of Fundamental Duties in the Indian Constitution was borrowed from the constitution of which nation?",
            "ta": "இந்திய அரசியலமைப்பில் உள்ள அடிப்படை கடமைகள் என்ற தத்துவம் எந்த நாட்டின் அரசியலமைப்பிலிருந்து பெறப்பட்டது?"
        },
        "options": [
            {"id": "A", "en": "USA (United States of America)", "ta": "அமெரிக்கா"},
            {"id": "B", "en": "Ireland", "ta": "அயர்லாந்து"},
            {"id": "C", "en": "Australia", "ta": "ஆஸ்திரேலியா"},
            {"id": "D", "en": "USSR (Former Soviet Union)", "ta": "சோவியத் யூனியன் (USSR)"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "Fundamental Duties in the Indian Constitution were borrowed from the Constitution of the former USSR (Soviet Union).",
            "ta": "இந்திய அரசியலமைப்பில் உள்ள அடிப்படை கடமைகள் முன்னாள் சோவியத் யூனியன் (USSR) அரசியலமைப்பிலிருந்து பெறப்பட்டவை."
        },
        "why_not_others": {
            "A": {"en": "USA inspired Fundamental Rights (Bill of Rights).", "ta": "அமெரிக்கா அடிப்படை உரிமைகளை (உரிமைகள் மசோதா) ஈர்த்தது."},
            "B": {"en": "Ireland inspired Directive Principles of State Policy (DPSP).", "ta": "அயர்லாந்து அரசு வழிகாட்டு நெறிமுறைகளை (DPSP) ஈர்த்தது."},
            "C": {"en": "Australia inspired Concurrent List and Joint Sitting of Parliament.", "ta": "ஆஸ்திரேலியா பொதுப் பட்டியல் மற்றும் நாடாளுமன்றக் கூட்டுக் கூட்டத்தை ஈர்த்தது."},
            "D": {"en": "Correct. Borrowed from USSR Constitution.", "ta": "சரி. சோவியத் யூனியன் அரசியலமைப்பிலிருந்து பெறப்பட்டது."}
        },
        "tnpsc_tip": {
            "en": "Major democratic constitutions like US, Canada, France do not contain explicit duties, but USSR did.",
            "ta": "அமெரிக்கா, கனடா, பிரான்ஸ் போன்ற முக்கிய ஜனநாயக அரசியலமைப்புகளில் கடமைகள் இல்லை, ஆனால் சோவியத் யூனியனில் இருந்தது."
        }
    },
    {
        "id": "FD_E_009",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Direct",
        "question": {
            "en": "How many Fundamental Duties were contained in the original Constitution of India enacted in 1950?",
            "ta": "1950-ல் இயற்றப்பட்ட அசல் இந்திய அரசியலமைப்பில் எத்தனை அடிப்படை கடமைகள் இருந்தன?"
        },
        "options": [
            {"id": "A", "en": "Zero (None)", "ta": "பூஜ்ஜியம் (எதுவுமில்லை)"},
            {"id": "B", "en": "8 Duties", "ta": "8 கடமைகள்"},
            {"id": "C", "en": "10 Duties", "ta": "10 கடமைகள்"},
            {"id": "D", "en": "11 Duties", "ta": "11 கடமைகள்"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "The original Constitution of India (1950) contained ZERO Fundamental Duties. They were introduced in 1976.",
            "ta": "அசல் இந்திய அரசியலமைப்பில் (1950) எந்தவொரு அடிப்படை கடமையும் இல்லை. அவை 1976-ல் தான் அறிமுகப்படுத்தப்பட்டன."
        },
        "why_not_others": {
            "A": {"en": "Correct. Original Constitution had no Fundamental Duties.", "ta": "சரி. அசல் அரசியலமைப்பில் அடிப்படை கடமைகள் இல்லை."},
            "B": {"en": "8 was recommended by Swaran Singh Committee in 1976.", "ta": "8 என்பது 1976-ல் ஸ்வரன் சிங் குழு பரிந்துரைத்தது."},
            "C": {"en": "10 duties were added in 1976.", "ta": "10 கடமைகள் 1976-ல் சேர்க்கப்பட்டன."},
            "D": {"en": "11 is the present total count.", "ta": "11 என்பது தற்போதைய மொத்த எண்ணிக்கை."}
        },
        "tnpsc_tip": {
            "en": "Framers of 1950 Constitution assumed citizens would voluntarily discharge duties.",
            "ta": "1950 அரசியலமைப்பை உருவாக்கியவர்கள் குடிமக்கள் தாமாகவே கடமைகளைச் செய்வார்கள் என்று நம்பினர்."
        }
    },
    {
        "id": "FD_E_010",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Direct",
        "question": {
            "en": "How many Fundamental Duties were originally recommended by the Sardar Swaran Singh Committee in 1976?",
            "ta": "1976-ல் சர்தார் ஸ்வரன் சிங் குழுவால் முதலில் எத்தனை அடிப்படை கடமைகள் பரிந்துரைக்கப்பட்டன?"
        },
        "options": [
            {"id": "A", "en": "10 Duties", "ta": "10 கடமைகள்"},
            {"id": "B", "en": "8 Duties", "ta": "8 கடமைகள்"},
            {"id": "C", "en": "11 Duties", "ta": "11 கடமைகள்"},
            {"id": "D", "en": "15 Duties", "ta": "15 கடமைகள்"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "The Swaran Singh Committee recommended EIGHT (8) Fundamental Duties. Parliament later expanded this to 10 duties in the 42nd Amendment Act.",
            "ta": "ஸ்வரன் சிங் குழு எட்டு (8) அடிப்படை கடமைகளைப் பரிந்துரைத்தது. நாடாளுமன்றம் பின்னர் 42வது திருத்தச் சட்டத்தில் இதை 10 கடமைகளாக விரிவாக்கியது."
        },
        "why_not_others": {
            "A": {"en": "10 was the number enacted by Parliament in 42nd CAA.", "ta": "10 என்பது 42வது திருத்தத்தில் நாடாளுமன்றத்தால் இயற்றப்பட்ட எண்ணிக்கை."},
            "B": {"en": "Correct. Swaran Singh Committee recommended 8 duties.", "ta": "சரி. ஸ்வரன் சிங் குழு 8 கடமைகளைப் பரிந்துரைத்தது."},
            "C": {"en": "11 is the present total count.", "ta": "11 என்பது தற்போதைய மொத்த எண்ணிக்கை."},
            "D": {"en": "Incorrect option.", "ta": "தவறான விருப்பம்."}
        },
        "tnpsc_tip": {
            "en": "Swaran Singh Committee recommended 8 duties, but 42nd Amendment enacted 10 duties.",
            "ta": "ஸ்வரன் சிங் குழு 8 கடமைகளைப் பரிந்துரைத்தது, ஆனால் 42வது திருத்தம் 10 கடமைகளை இயற்றியது."
        }
    },
    {
        "id": "FD_E_011",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "TNPSC Trap",
        "question": {
            "en": "Which of the following proposals recommended by the Swaran Singh Committee was REJECTED by Parliament and NOT included in Article 51A?",
            "ta": "ஸ்வரன் சிங் குழுவால் பரிந்துரைக்கப்பட்டு நாடாளுமன்றத்தால் நிராகரிக்கப்பட்டதால் உறுப்பு 51A-ல் சேர்க்கப்படாத முன்மொழிவு எது?"
        },
        "options": [
            {"id": "A", "en": "Duty to abide by the Constitution", "ta": "அரசியலமைப்புக்குக் கீழ்ப்படியும் கடமை"},
            {"id": "B", "en": "Duty to defend the country", "ta": "தேசத்தைப் பாதுகாக்கும் கடமை"},
            {"id": "C", "en": "Duty to pay taxes", "ta": "வரி செலுத்தும் கடமை"},
            {"id": "D", "en": "Duty to promote brotherhood", "ta": "சகோதரத்துவத்தை வளர்க்கும் கடமை"}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "The 'Duty to pay taxes' was recommended by Swaran Singh Committee but REJECTED by Parliament and NOT included in Article 51A.",
            "ta": "'வரி செலுத்தும் கடமை' ஸ்வரன் சிங் குழுவால் பரிந்துரைக்கப்பட்டது, ஆனால் நாடாளுமன்றத்தால் நிராகரிக்கப்பட்டு உறுப்பு 51A-ல் சேர்க்கப்படவில்லை."
        },
        "why_not_others": {
            "A": {"en": "Abiding by Constitution was accepted and included in Art 51A(a).", "ta": "அரசியலமைப்புக்குக் கீழ்ப்படிவது ஏற்றுக்கொள்ளப்பட்டு உறுப்பு 51A(a)-ல் சேர்க்கப்பட்டது."},
            "B": {"en": "Defending the country was accepted and included in Art 51A(d).", "ta": "தேசத்தைப் பாதுகாப்பது ஏற்றுக்கொள்ளப்பட்டு உறுப்பு 51A(d)-ல் சேர்க்கப்பட்டது."},
            "C": {"en": "Correct. Duty to pay taxes was rejected by Parliament.", "ta": "சரி. வரி செலுத்தும் கடமை நாடாளுமன்றத்தால் நிராகரிக்கப்பட்டது."},
            "D": {"en": "Promoting brotherhood was accepted and included in Art 51A(e).", "ta": "சகோதரத்துவத்தை வளர்ப்பது ஏற்றுக்கொள்ளப்பட்டு உறுப்பு 51A(e)-ல் சேர்க்கப்பட்டது."}
        },
        "tnpsc_tip": {
            "en": "Paying taxes is a statutory duty under Tax Laws, NOT a constitutional Fundamental Duty under Article 51A.",
            "ta": "வரி செலுத்துவது வரிச் சட்டங்களின் கீழ் உள்ள சட்டப்பூர்வ கடமையே தவிர, உறுப்பு 51A-ன் கீழ் உள்ள அரசியலமைப்பு அடிப்படை கடமை அல்ல."
        }
    },
    {
        "id": "FD_E_012",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Basic Conceptual",
        "question": {
            "en": "To whom do the Fundamental Duties enshrined in Part IVA of the Constitution apply?",
            "ta": "அரசியலமைப்பின் பகுதி IVA-ல் பொறிக்கப்பட்டுள்ள அடிப்படை கடமைகள் யாருக்குப் பொருந்தும்?"
        },
        "options": [
            {"id": "A", "en": "All persons residing in India including foreigners", "ta": "வெளிநாட்டினர் உட்பட இந்தியாவில் வசிக்கும் அனைத்து நபர்களுக்கும்"},
            {"id": "B", "en": "Only to Government Officials and Servants", "ta": "அரசு அதிகாரிகள் மற்றும் ஊழியர்களுக்கு மட்டுமே"},
            {"id": "C", "en": "Only to Members of Parliament and State Assemblies", "ta": "நாடாளுமன்ற மற்றும் மாநிலச் சட்டமன்ற உறுப்பினர்களுக்கு மட்டுமே"},
            {"id": "D", "en": "Exclusively to Citizens of India", "ta": "இந்தியக் குடிமக்களுக்கு மட்டுமே"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "Fundamental Duties under Article 51A apply EXCLUSIVELY to the Citizens of India. Foreigners are not bound by Article 51A.",
            "ta": "உறுப்பு 51A-ன் கீழ் உள்ள அடிப்படை கடமைகள் இந்தியக் குடிமக்களுக்கு மட்டுமே பொருந்தும். வெளிநாட்டினருக்கு உறுப்பு 51A பொருந்தாது."
        },
        "why_not_others": {
            "A": {"en": "Certain FRs (like Art 14, 21) apply to foreigners, but FDs apply ONLY to citizens.", "ta": "சில உரிமைகள் (உறுப்பு 14, 21 போன்றவை) வெளிநாட்டினருக்குப் பொருந்தும், ஆனால் கடமைகள் குடிமக்களுக்கு மட்டுமே."},
            "B": {"en": "FDs apply to ALL citizens, not just government officials.", "ta": "கடமைகள் அனைத்துக் குடிமக்களுக்கும் பொருந்தும், அரசு அதிகாரிகளுக்கு மட்டுமல்ல."},
            "C": {"en": "FDs apply to every individual citizen of India.", "ta": "கடமைகள் இந்தியாவின் ஒவ்வொரு தனிநபர் குடிமகனுக்கும் பொருந்தும்."},
            "D": {"en": "Correct. FDs apply exclusively to Indian Citizens.", "ta": "சரி. கடமைகள் இந்தியக் குடிமக்களுக்கு மட்டுமே பொருந்தும்."}
        },
        "tnpsc_tip": {
            "en": "Text of Article 51A begins with: 'It shall be the duty of EVERY CITIZEN OF INDIA...'",
            "ta": "உறுப்பு 51A-ன் உரை: 'இந்தியாவின் ஒவ்வொரு குடிமகனின் கடமையாவது...' எனத் தொடங்குகிறது."
        }
    },
    {
        "id": "FD_E_013",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Basic Conceptual",
        "question": {
            "en": "What is the legal nature of Fundamental Duties in the Constitution of India?",
            "ta": "இந்திய அரசியலமைப்பில் உள்ள அடிப்படை கடமைகளின் சட்டப்பூர்வ இயல்பு என்ன?"
        },
        "options": [
            {"id": "A", "en": "Justiciable and directly enforceable by Supreme Court writs", "ta": "நீதிமன்றத்தால் நேரடியாகப் பேராணைகள் மூலம் அமல்படுத்தக் கூடியவை"},
            {"id": "B", "en": "Non-justiciable and cannot be directly enforced by courts without a law", "ta": "நீதிமன்றங்களால் நேரடியாகச் சட்டமின்றி அமல்படுத்த முடியாதவை"},
            {"id": "C", "en": "Self-executing penal laws attracting immediate imprisonment", "ta": "உடனடி சிறைத்தண்டனையை ஈர்க்கும் தானாக அமலாகும் குற்றவியல் சட்டங்கள்"},
            {"id": "D", "en": "Enforceable only by international courts", "ta": "சர்வதேச நீதிமன்றங்களால் மட்டுமே அமல்படுத்தக் கூடியவை"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "Fundamental Duties are non-justiciable in nature. There is no direct writ remedy for their violation unless Parliament has enacted a specific supporting law.",
            "ta": "அடிப்படை கடமைகள் நீதிமன்றங்களால் நேரடியாக அமல்படுத்த முடியாத இயல்புடையவை. நாடாளுமன்றம் ஆதரவுச் சட்டம் இயற்றாவிட்டால் அவற்றின் மீறலுக்கு நேரடி பேராணை பரிகாரம் இல்லை."
        },
        "why_not_others": {
            "A": {"en": "Fundamental Rights are justiciable; Fundamental Duties are non-justiciable.", "ta": "அடிப்படை உரிமைகள் அமல்படுத்தக்கூடியவை; அடிப்படை கடமைகள் அமல்படுத்த முடியாதவை."},
            "B": {"en": "Correct. Fundamental Duties are non-justiciable in nature.", "ta": "சரி. அடிப்படை கடமைகள் நீதிமன்றங்களால் நேரடியாக அமல்படுத்த முடியாதவை."},
            "C": {"en": "FDs are not self-executing penal laws.", "ta": "கடமைகள் தானாக அமலாகும் குற்றவியல் சட்டங்கள் அல்ல."},
            "D": {"en": "Domestic constitutional provisions are governed by national courts.", "ta": "உள்நாட்டு அரசியலமைப்பு விதிகள் தேசிய நீதிமன்றங்களால் நெறிப்படுத்தப்படுகின்றன."}
        },
        "tnpsc_tip": {
            "en": "Parliament can pass laws to enforce duties (e.g. Flag Code 2002, Wildlife Protection Act 1972).",
            "ta": "கடமைகளை அமல்படுத்த நாடாளுமன்றம் சட்டங்களை இயற்றலாம் (எ.கா. கொடி குறியீடு 2002, வனவிலங்கு பாதுகாப்புச் சட்டம் 1972)."
        }
    },
    {
        "id": "FD_E_014",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Article-based",
        "question": {
            "en": "According to Article 51A(a), every citizen has a duty to abide by the Constitution and respect its ideals, institutions, and which national symbols?",
            "ta": "உறுப்பு 51A(a)-ன் படி, ஒவ்வொரு குடிமகனும் அரசியலமைப்புக்குக் கீழ்ப்படிந்து அதன் லட்சியங்கள், நிறுவனங்கள் மற்றும் எந்த தேசிய சின்னங்களை மதிக்கக் கடமைப்பட்டுள்ளனர்?"
        },
        "options": [
            {"id": "A", "en": "National Flag and National Anthem", "ta": "தேசியக் கொடி மற்றும் தேசியக் கீதம்"},
            {"id": "B", "en": "National Animal and National Bird", "ta": "தேசிய விலங்கு மற்றும் தேசியப் பறவை"},
            {"id": "C", "en": "National Flower and National Tree", "ta": "தேசிய மலர் மற்றும் தேசிய மரம்"},
            {"id": "D", "en": "National River and National Emblem", "ta": "தேசிய ஆறு மற்றும் தேசிய இலச்சினை"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Article 51A(a) mandates respecting the Constitution, its ideals and institutions, the National Flag and the National Anthem.",
            "ta": "உறுப்பு 51A(a) அரசியலமைப்பு, அதன் லட்சியங்கள், நிறுவனங்கள், தேசியக் கொடி மற்றும் தேசியக் கீதத்தை மதிக்க ஆணையிடுகிறது."
        },
        "why_not_others": {
            "A": {"en": "Correct. National Flag and National Anthem are explicitly mentioned in Art 51A(a).", "ta": "சரி. தேசியக் கொடி மற்றும் தேசியக் கீதம் உறுப்பு 51A(a)-ல் வெளிப்படையாகக் குறிப்பிடப்பட்டுள்ளன."},
            "B": {"en": "Wildlife is covered generally under Art 51A(g), not Art 51A(a).", "ta": "வனவிலங்குகள் உறுப்பு 51A(g)-ல் பொதுவாகக் கவர் செய்யப்பட்டுள்ளன."},
            "C": {"en": "Not mentioned in Art 51A(a).", "ta": "உறுப்பு 51A(a)-ல் குறிப்பிடப்படவில்லை."},
            "D": {"en": "Rivers are under Art 51A(g); Emblem is under statutory acts.", "ta": "ஆறுகள் உறுப்பு 51A(g)-ல் உள்ளன; இலச்சினை சட்டப்பூர்வச் சட்டங்களில் உள்ளது."}
        },
        "tnpsc_tip": {
            "en": "Enforced statutorily by the Prevention of Insults to National Honour Act, 1971.",
            "ta": "1971-ன் தேசிய கௌரவ அவமதிப்பு தடுப்புச் சட்டம் மூலம் சட்டப்பூர்வமாக அமல்படுத்தப்படுகிறது."
        }
    },
    {
        "id": "FD_E_015",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Article-based",
        "question": {
            "en": "Article 51A(b) commands Indian citizens to cherish and follow the noble ideals which inspired what historical movement?",
            "ta": "உறுப்பு 51A(b) இந்தியக் குடிமக்களை எந்த வரலாற்று இயக்கத்திற்கு ஊக்கமளித்த உயரிய லட்சியங்களைப் பேணிப் பின்பற்றக் கட்டளையிடுகிறது?"
        },
        "options": [
            {"id": "A", "en": "Industrial Revolution", "ta": "தொழில்துறை புரட்சி"},
            {"id": "B", "en": "National struggle for freedom", "ta": "தேசிய சுதந்திரப் போராட்டம்"},
            {"id": "C", "en": "French Revolution", "ta": "பிரெஞ்சு புரட்சி"},
            {"id": "D", "en": "Russian Revolution", "ta": "ரஷ்ய புரட்சி"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "Article 51A(b) directs citizens: 'To cherish and follow the noble ideals which inspired our national struggle for freedom.'",
            "ta": "உறுப்பு 51A(b) குடிமக்களுக்கு ஆணையிடுகிறது: 'நமது தேசிய சுதந்திரப் போராட்டத்திற்கு ஊக்கமளித்த உயரிய லட்சியங்களைப் பேணிப் பின்பற்றுதல்.'"
        },
        "why_not_others": {
            "A": {"en": "Industrial Revolution took place in Britain.", "ta": "தொழில்துறை புரட்சி பிரிட்டனில் நடந்தது."},
            "B": {"en": "Correct. National struggle for freedom.", "ta": "சரி. தேசிய சுதந்திரப் போராட்டம்."},
            "C": {"en": "French Revolution inspired Preamble ideals of Liberty, Equality, Fraternity.", "ta": "பிரெஞ்சு புரட்சி முகப்புரையின் சுதந்திரம், சமத்துவம், சகோதரத்துவத்தை ஈர்த்தது."},
            "D": {"en": "Russian Revolution inspired Socialism in DPSP & Preamble.", "ta": "ரஷ்ய புரட்சி DPSP & முகப்புரையில் சமதர்மத்தை ஈர்த்தது."}
        },
        "tnpsc_tip": {
            "en": "Noble ideals include Ahimsa, truth, secularism, unity, and self-reliance espoused by freedom fighters.",
            "ta": "உயரிய லட்சியங்களில் சுதந்திரப் போராட்ட வீரர்கள் போற்றிய அகிம்சை, உண்மை, மதச்சார்பின்மை, ஒற்றுமை அடங்கும்."
        }
    },
    {
        "id": "FD_E_016",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Article-based",
        "question": {
            "en": "Article 51A(c) directs every citizen of India to uphold and protect which three paramount values of the nation?",
            "ta": "உறுப்பு 51A(c) இந்தியாவின் ஒவ்வொரு குடிமகனும் தேசத்தின் எந்த மூன்று முக்கிய மதிப்புகளைப் பேணிப் பாதுகாக்க வழிகாட்டுகிறது?"
        },
        "options": [
            {"id": "A", "en": "Liberty, Equality, and Fraternity", "ta": "சுதந்திரம், சமத்துவம் மற்றும் சகோதரத்துவம்"},
            {"id": "B", "en": "Justice, Democracy, and Republic", "ta": "நீதி, ஜனநாயகம் மற்றும் குடியரசு"},
            {"id": "C", "en": "Sovereignty, Unity, and Integrity of India", "ta": "இந்தியாவின் இறையாண்மை, ஒற்றுமை மற்றும் ஒருமைப்பாடு"},
            {"id": "D", "en": "Secularism, Socialism, and Federalism", "ta": "மதச்சார்பின்மை, சமதர்மம் மற்றும் கூட்டாட்சி"}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "Article 51A(c) states: 'To uphold and protect the sovereignty, unity and integrity of India.'",
            "ta": "உறுப்பு 51A(c) கூறுகிறது: 'இந்தியாவின் இறையாண்மை, ஒற்றுமை மற்றும் ஒருமைப்பாட்டைப் பேணிப் பாதுகாத்தல்.'"
        },
        "why_not_others": {
            "A": {"en": "Liberty, Equality, Fraternity are Preamble ideals derived from French Revolution.", "ta": "சுதந்திரம், சமத்துவம், சகோதரத்துவம் பிரெஞ்சு புரட்சியிலிருந்து பெறப்பட்ட முகப்புரை லட்சியங்கள்."},
            "B": {"en": "Preamble key terms.", "ta": "முகப்புரையின் முக்கிய சொற்கள்."},
            "C": {"en": "Correct. Sovereignty, Unity, and Integrity are specified in Art 51A(c).", "ta": "சரி. இறையாண்மை, ஒற்றுமை மற்றும் ஒருமைப்பாடு உறுப்பு 51A(c)-ல் குறிப்பிடப்பட்டுள்ளன."},
            "D": {"en": "Preamble and Basic Structure concepts.", "ta": "முகப்புரை மற்றும் அடிப்படை அமைப்புக் கருத்துகள்."}
        },
        "tnpsc_tip": {
            "en": "Upholding sovereignty, unity and integrity is considered one of the most paramount duties.",
            "ta": "இறையாண்மை, ஒற்றுமை மற்றும் ஒருமைப்பாட்டைப் பேணுவது மிகவும் முதன்மையான கடமைகளில் ஒன்றாகக் கருதப்படுகிறது."
        }
    },
    {
        "id": "FD_E_017",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Article-based",
        "question": {
            "en": "Which sub-clause of Article 51A commands citizens 'To defend the country and render national service when called upon to do so'?",
            "ta": "உறுப்பு 51A-ன் எந்த உட்பிரிவு குடிமக்களுக்கு 'தேசத்தைப் பாதுகாத்தலும், தேவைப்படும்போது தேசிய சேவை ஆற்றுதலும்' எனக் கட்டளையிடுகிறது?"
        },
        "options": [
            {"id": "A", "en": "Article 51A(a)", "ta": "உறுப்பு 51A(a)"},
            {"id": "B", "en": "Article 51A(g)", "ta": "உறுப்பு 51A(g)"},
            {"id": "C", "en": "Article 51A(j)", "ta": "உறுப்பு 51A(j)"},
            {"id": "D", "en": "Article 51A(d)", "ta": "உறுப்பு 51A(d)"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "Article 51A(d) specifies the duty to defend the country and render national service when called upon by the State.",
            "ta": "உறுப்பு 51A(d) அரசால் அழைக்கப்படும் போது தேசத்தைப் பாதுகாக்கும் மற்றும் தேசிய சேவை ஆற்றும் கடமையைக் குறிப்பிடுகிறது."
        },
        "why_not_others": {
            "A": {"en": "51A(a) deals with Constitution, Flag, Anthem.", "ta": "51A(a) அரசியலமைப்பு, கொடி, கீதம் பற்றியது."},
            "B": {"en": "51A(g) deals with Environment and Wildlife.", "ta": "51A(g) சுற்றுச்சூழல் மற்றும் வனவிலங்குகள் பற்றியது."},
            "C": {"en": "51A(j) deals with Striving for Excellence.", "ta": "51A(j) சிறப்பினை நோக்கி முயலுதல் பற்றியது."},
            "D": {"en": "Correct. 51A(d) covers defending country and rendering national service.", "ta": "சரி. 51A(d) தேசத்தைப் பாதுகாத்தல் மற்றும் தேசிய சேவை ஆற்றுதலை உள்ளடக்கியது."}
        },
        "tnpsc_tip": {
            "en": "Provides the constitutional basis for conscription (compulsory military service) during emergency/war.",
            "ta": "போர்/அவசரநிலையின் போது கட்டாய ராணுவ சேவைக்கான அரசியலமைப்பு அடித்தளத்தை வழங்குகிறது."
        }
    },
    {
        "id": "FD_E_018",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Article-based",
        "question": {
            "en": "Renouncing practices derogatory to the dignity of women is a Fundamental Duty under which Article clause?",
            "ta": "பெண்களின் கண்ணியத்திற்கு இழுக்கு விளைவிக்கும் பழக்கங்களைக் கைவிடுவது எந்த உறுப்பு உட்பிரிவின் கீழ் உள்ள அடிப்படை கடமையாகும்?"
        },
        "options": [
            {"id": "A", "en": "Article 51A(c)", "ta": "உறுப்பு 51A(c)"},
            {"id": "B", "en": "Article 51A(h)", "ta": "உறுப்பு 51A(h)"},
            {"id": "C", "en": "Article 51A(e)", "ta": "உறுப்பு 51A(e)"},
            {"id": "D", "en": "Article 51A(k)", "ta": "உறுப்பு 51A(k)"}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "Article 51A(e) contains two parts: promoting harmony/brotherhood and renouncing practices derogatory to the dignity of women.",
            "ta": "உறுப்பு 51A(e) இரண்டு பகுதிகளைக் கொண்டுள்ளது: நல்லிணக்கம்/சகோதரத்துவத்தை வளர்த்தல் மற்றும் பெண்களின் கண்ணியத்தைக் குறைக்கும் பழக்கங்களைக் கைவிடுதல்."
        },
        "why_not_others": {
            "A": {"en": "51A(c) deals with Sovereignty, Unity, Integrity.", "ta": "51A(c) இறையாண்மை, ஒற்றுமை, ஒருமைப்பாடு பற்றியது."},
            "B": {"en": "51A(h) deals with Scientific temper.", "ta": "51A(h) அறிவியல் மனப்பான்மை பற்றியது."},
            "C": {"en": "Correct. 51A(e) covers dignity of women.", "ta": "சரி. 51A(e) பெண்களின் கண்ணியம் பற்றியது."},
            "D": {"en": "51A(k) deals with Child education duty.", "ta": "51A(k) குழந்தைகள் கல்விக் கடமை பற்றியது."}
        },
        "tnpsc_tip": {
            "en": "Statutory support includes Dowry Prohibition Act 1961 and Domestic Violence Act 2005.",
            "ta": "சட்டப்பூர்வ ஆதரவில் வரதட்சணை தடைச் சட்டம் 1961 மற்றும் குடும்ப வன்முறைச் சட்டம் 2005 அடங்கும்."
        }
    },
    {
        "id": "FD_E_019",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Article-based",
        "question": {
            "en": "Which Article clause commands citizens to promote harmony and the spirit of common brotherhood transcending religious, linguistic, and regional diversities?",
            "ta": "மதம், மொழி, பிராந்திய வேறுபாடுகளைக் கடந்து நல்லிணக்கத்தையும் சகோதரத்துவத்தையும் வளர்க்க எந்த உறுப்பு உட்பிரிவு குடிமக்களுக்கு ஆணையிடுகிறது?"
        },
        "options": [
            {"id": "A", "en": "Article 51A(e)", "ta": "உறுப்பு 51A(e)"},
            {"id": "B", "en": "Article 51A(f)", "ta": "உறுப்பு 51A(f)"},
            {"id": "C", "en": "Article 51A(i)", "ta": "உறுப்பு 51A(i)"},
            {"id": "D", "en": "Article 51A(j)", "ta": "உறுப்பு 51A(j)"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Article 51A(e) directs citizens to promote harmony and common brotherhood transcending all diversities.",
            "ta": "உறுப்பு 51A(e) அனைத்து வேறுபாடுகளையும் கடந்து நல்லிணக்கத்தையும் பொதுவான சகோதரத்துவத்தையும் வளர்க்கக் குடிமக்களுக்கு வழிகாட்டுகிறது."
        },
        "why_not_others": {
            "A": {"en": "Correct. Art 51A(e) covers harmony and brotherhood.", "ta": "சரி. உறுப்பு 51A(e) நல்லிணக்கம் மற்றும் சகோதரத்துவத்தை உள்ளடக்கியது."},
            "B": {"en": "51A(f) covers Composite culture.", "ta": "51A(f) கூட்டுப் பண்பாட்டை உள்ளடக்கியது."},
            "C": {"en": "51A(i) covers Public property.", "ta": "51A(i) பொதுச் சொத்தை உள்ளடக்கியது."},
            "D": {"en": "51A(j) covers Excellence.", "ta": "51A(j) சிறப்பினை உள்ளடக்கியது."}
        },
        "tnpsc_tip": {
            "en": "Reinforces the Preamble ideal of 'Fraternity' assuring the dignity of individual.",
            "ta": "தனிநபர் கண்ணியத்தை உறுதிப்படுத்தும் முகப்புரையின் 'சகோதரத்துவம்' என்ற லட்சியத்தை வலுப்படுத்துகிறது."
        }
    },
    {
        "id": "FD_E_020",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Article-based",
        "question": {
            "en": "Valuing and preserving the rich heritage of India's 'composite culture' is enshrined in which sub-clause of Article 51A?",
            "ta": "இந்தியாவின் 'கூட்டுப் பண்பாட்டின்' வளமான பாரம்பரியத்தை மதித்து பேணிப் பாதுகாத்தல் உறுப்பு 51A-ன் எந்த உட்பிரிவில் பொறிக்கப்பட்டுள்ளது?"
        },
        "options": [
            {"id": "A", "en": "Article 51A(b)", "ta": "உறுப்பு 51A(b)"},
            {"id": "B", "en": "Article 51A(f)", "ta": "உறுப்பு 51A(f)"},
            {"id": "C", "en": "Article 51A(d)", "ta": "உறுப்பு 51A(d)"},
            {"id": "D", "en": "Article 51A(h)", "ta": "உறுப்பு 51A(h)"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "Article 51A(f) mandates: 'To value and preserve the rich heritage of our composite culture.'",
            "ta": "உறுப்பு 51A(f) கட்டாயமாக்குகிறது: 'நமது கூட்டுப் பண்பாட்டின் வளமான பாரம்பரியத்தை மதித்து பேணிப் பாதுகாத்தல்.'"
        },
        "why_not_others": {
            "A": {"en": "51A(b) covers freedom struggle ideals.", "ta": "51A(b) சுதந்திரப் போராட்ட லட்சியங்களை உள்ளடக்கியது."},
            "B": {"en": "Correct. 51A(f) covers composite culture.", "ta": "சரி. 51A(f) கூட்டுப் பண்பாட்டை உள்ளடக்கியது."},
            "C": {"en": "51A(d) covers defending country.", "ta": "51A(d) தேசத்தைப் பாதுகாத்தலை உள்ளடக்கியது."},
            "D": {"en": "51A(h) covers scientific temper.", "ta": "51A(h) அறிவியல் மனப்பான்மையை உள்ளடக்கியது."}
        },
        "tnpsc_tip": {
            "en": "Composite culture refers to the syncretic synthesis evolved across diverse traditions in India.",
            "ta": "கூட்டுப் பண்பாடு என்பது இந்தியாவில் பல்வேறு பாரம்பரியங்களின் சேர்க்கையைக் குறிக்கிறது."
        }
    },
    {
        "id": "FD_E_021",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Article-based",
        "question": {
            "en": "Article 51A(g) explicitly mandates protecting and improving the natural environment including which four specified natural elements?",
            "ta": "உறுப்பு 51A(g) எந்த நான்கு குறிப்பிட்ட இயற்கை கூறுகள் உட்பட இயற்கை சுற்றுச்சூழலைப் பாதுகாத்து மேம்படுத்த வெளிப்படையாகக் கட்டளையிடுகிறது?"
        },
        "options": [
            {"id": "A", "en": "Forests, Lakes, Rivers, and Wildlife", "ta": "காடுகள், ஏரிகள், ஆறுகள் மற்றும் வனவிலங்குகள்"},
            {"id": "B", "en": "Mountains, Oceans, Minerals, and Soil", "ta": "மலைகள், பெருங்கடல்கள், கனிமங்கள் மற்றும் மண்"},
            {"id": "C", "en": "Air, Solar Energy, Groundwater, and Agriculture", "ta": "காற்று, சூரிய ஆற்றல், நிலத்தடி நீர் மற்றும் விவசாயம்"},
            {"id": "D", "en": "Ponds, Hills, Climate, and Pastures", "ta": "குளங்கள், குன்றுகள், காலநிலை மற்றும் மேய்ச்சல் நிலங்கள்"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Article 51A(g) explicitly mentions four natural elements: Forests, Lakes, Rivers, and Wildlife.",
            "ta": "உறுப்பு 51A(g) நான்கு இயற்கை கூறுகளை வெளிப்படையாகக் குறிப்பிடுகிறது: காடுகள், ஏரிகள், ஆறுகள் மற்றும் வனவிலங்குகள்."
        },
        "why_not_others": {
            "A": {"en": "Correct. Forests, Lakes, Rivers, Wildlife are the 4 specified elements.", "ta": "சரி. காடுகள், ஏரிகள், ஆறுகள், வனவிலங்குகள் 4 குறிப்பிட்ட கூறுகள்."},
            "B": {"en": "Mountains and Oceans are not explicitly named in Art 51A(g).", "ta": "மலைகள் மற்றும் பெருங்கடல்கள் உறுப்பு 51A(g)-ல் பெயரிடப்படவில்லை."},
            "C": {"en": "Not the exact constitutional text of Art 51A(g).", "ta": "உறுப்பு 51A(g)-ன் சரியான உரை அல்ல."},
            "D": {"en": "Incorrect components.", "ta": "தவறான கூறுகள்."}
        },
        "tnpsc_tip": {
            "en": "Remember the exact 4 elements in Art 51A(g): Forests, Lakes, Rivers, Wildlife.",
            "ta": "உறுப்பு 51A(g)-ல் உள்ள 4 கூறுகளை நினைவில் கொள்க: காடுகள், ஏரிகள், ஆறுகள், வனவிலங்குகள்."
        }
    },
    {
        "id": "FD_E_022",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Article-based",
        "question": {
            "en": "Having 'compassion for living creatures' is enumerated as a Fundamental Duty under which Article clause?",
            "ta": "'உயிரினங்கள் மீது கருணை காட்டுதல்' எந்த உறுப்பு உட்பிரிவின் கீழ் அடிப்படை கடமையாகப் பட்டியலிடப்பட்டுள்ளது?"
        },
        "options": [
            {"id": "A", "en": "Article 51A(e)", "ta": "உறுப்பு 51A(e)"},
            {"id": "B", "en": "Article 51A(i)", "ta": "உறுப்பு 51A(i)"},
            {"id": "C", "en": "Article 51A(g)", "ta": "உறுப்பு 51A(g)"},
            {"id": "D", "en": "Article 51A(k)", "ta": "உறுப்பு 51A(k)"}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "Article 51A(g) mandates protecting the environment and having 'compassion for living creatures'.",
            "ta": "உறுப்பு 51A(g) சுற்றுச்சூழலைப் பாதுகாக்கவும் 'உயிரினங்கள் மீது கருணை காட்டவும்' கட்டாயமாக்குகிறது."
        },
        "why_not_others": {
            "A": {"en": "51A(e) covers brotherhood and women's dignity.", "ta": "51A(e) சகோதரத்துவம் மற்றும் பெண்கள் கண்ணியத்தை உள்ளடக்கியது."},
            "B": {"en": "51A(i) covers public property and non-violence.", "ta": "51A(i) பொதுச் சொத்து மற்றும் வன்முறையின்மையை உள்ளடக்கியது."},
            "C": {"en": "Correct. 51A(g) covers compassion for living creatures.", "ta": "சரி. 51A(g) உயிரினங்கள் மீதான கருணையை உள்ளடக்கியது."},
            "D": {"en": "51A(k) covers child education duty.", "ta": "51A(k) குழந்தைகள் கல்விக் கடமையை உள்ளடக்கியது."}
        },
        "tnpsc_tip": {
            "en": "Supreme Court invoked Art 51A(g) in Animal Welfare Board v. A. Nagaraja (2014) [Jallikattu case].",
            "ta": "உச்ச நீதிமன்றம் 2014 ஏ. நாகராஜா (ஜல்லிக்கட்டு) வழக்கில் உறுப்பு 51A(g)-ஐப் பயன்படுத்தியது."
        }
    },
    {
        "id": "FD_E_023",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Article-based",
        "question": {
            "en": "Developing scientific temper, humanism, and the spirit of inquiry and reform is a Fundamental Duty under which Article clause?",
            "ta": "அறிவியல் மனப்பான்மை, மனிதநேயம், ஆராய்ச்சி மற்றும் சீர்திருத்த உணர்வை வளர்த்தல் எந்த உறுப்பு உட்பிரிவின் கீழ் அடிப்படை கடமையாகும்?"
        },
        "options": [
            {"id": "A", "en": "Article 51A(f)", "ta": "உறுப்பு 51A(f)"},
            {"id": "B", "en": "Article 51A(j)", "ta": "உறுப்பு 51A(j)"},
            {"id": "C", "en": "Article 51A(k)", "ta": "உறுப்பு 51A(k)"},
            {"id": "D", "en": "Article 51A(h)", "ta": "உறுப்பு 51A(h)"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "Article 51A(h) directs citizens: 'To develop the scientific temper, humanism and the spirit of inquiry and reform.'",
            "ta": "உறுப்பு 51A(h) குடிமக்களுக்கு ஆணையிடுகிறது: 'அறிவியல் மனப்பான்மை, மனிதநேயம், ஆராய்ச்சி மற்றும் சீர்திருத்த உணர்வை வளர்த்தல்.'"
        },
        "why_not_others": {
            "A": {"en": "51A(f) covers composite culture.", "ta": "51A(f) கூட்டுப் பண்பாட்டை உள்ளடக்கியது."},
            "B": {"en": "51A(j) covers striving for excellence.", "ta": "51A(j) சிறப்பினை நோக்கி முயலுதலை உள்ளடக்கியது."},
            "C": {"en": "51A(k) covers child education.", "ta": "51A(k) குழந்தைகள் கல்வியை உள்ளடக்கியது."},
            "D": {"en": "Correct. 51A(h) covers scientific temper & humanism.", "ta": "சரி. 51A(h) அறிவியல் மனப்பான்மை & மனிதநேயத்தை உள்ளடக்கியது."}
        },
        "tnpsc_tip": {
            "en": "Four pillars of Art 51A(h): Scientific Temper, Humanism, Spirit of Inquiry, Spirit of Reform.",
            "ta": "உறுப்பு 51A(h)-ன் 4 தூண்கள்: அறிவியல் மனப்பான்மை, மனிதநேயம், ஆராய்ச்சி உணர்வு, சீர்திருத்த உணர்வு."
        }
    },
    {
        "id": "FD_E_024",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Article-based",
        "question": {
            "en": "Article 51A(i) mandates citizens to safeguard which property and to abjure what negative action?",
            "ta": "உறுப்பு 51A(i) குடிமக்களை எந்தச் சொத்தைப் பாதுகாக்கவும் எந்த எதிர்மறைச் செயலைக் கைவிடவும் கட்டாயமாக்குகிறது?"
        },
        "options": [
            {"id": "A", "en": "Safeguard Private property and abjure Taxes", "ta": "தனிநபர் சொத்தைப் பாதுகாத்தல் & வரிகளைக் கைவிடுதல்"},
            {"id": "B", "en": "Safeguard Public property and abjure Violence", "ta": "பொதுச் சொத்தைப் பாதுகாத்தல் & வன்முறையைக் கைவிடுதல்"},
            {"id": "C", "en": "Safeguard Ancestral property and abjure Protests", "ta": "பூர்வீகச் சொத்தைப் பாதுகாத்தல் & போராட்டங்களைக் கைவிடுதல்"},
            {"id": "D", "en": "Safeguard Foreign property and abjure Strikes", "ta": "வெளிநாட்டுச் சொத்தைப் பாதுகாத்தல் & வேலைநிறுத்தங்களைக் கைவிடுதல்"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "Article 51A(i) states: 'To safeguard public property and to abjure violence.'",
            "ta": "உறுப்பு 51A(i) கூறுகிறது: 'பொதுச் சொத்தைப் பாதுகாத்தலும், வன்முறையைக் கைவிடுதலும்.'"
        },
        "why_not_others": {
            "A": {"en": "Private property is not specified in Art 51A(i).", "ta": "தனிநபர் சொத்து உறுப்பு 51A(i)-ல் குறிப்பிடப்படவில்லை."},
            "B": {"en": "Correct. Safeguard Public property and abjure Violence.", "ta": "சரி. பொதுச் சொத்தைப் பாதுகாத்தல் மற்றும் வன்முறையைக் கைவிடுதல்."},
            "C": {"en": "Ancestral property is under civil law.", "ta": "பூர்வீகச் சொத்து சிவில் சட்டத்தில் உள்ளது."},
            "D": {"en": "Incorrect options.", "ta": "தவறான விருப்பங்கள்."}
        },
        "tnpsc_tip": {
            "en": "'Abjure' means to solemnly renounce or abandon upon oath.",
            "ta": "'Abjure' என்றால் வன்முறையை முற்றிலுமாகக் கைவிடுதல் அல்லது நிராகரித்தல் ஆகும்."
        }
    },
    {
        "id": "FD_E_025",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Article-based",
        "question": {
            "en": "Striving towards excellence in all spheres of individual and collective activity is enshrined under which sub-clause of Article 51A?",
            "ta": "தனிநபர் மற்றும் கூட்டுச் செயல்பாடுகளின் அனைத்துத் துறைகளிலும் சிறப்பினை நோக்கி முயலுதல் உறுப்பு 51A-ன் எந்த உட்பிரிவில் பொறிக்கப்பட்டுள்ளது?"
        },
        "options": [
            {"id": "A", "en": "Article 51A(g)", "ta": "உறுப்பு 51A(g)"},
            {"id": "B", "en": "Article 51A(h)", "ta": "உறுப்பு 51A(h)"},
            {"id": "C", "en": "Article 51A(j)", "ta": "உறுப்பு 51A(j)"},
            {"id": "D", "en": "Article 51A(k)", "ta": "உறுப்பு 51A(k)"}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "Article 51A(j) commands striving towards excellence in individual and collective activity so that the nation constantly rises to higher levels.",
            "ta": "உறுப்பு 51A(j) தேசம் தொடர்ச்சியாக உயரத் தனிநபர் மற்றும் கூட்டுச் செயல்பாடுகளில் சிறப்பினை நோக்கி முயல ஆணையிடுகிறது."
        },
        "why_not_others": {
            "A": {"en": "51A(g) deals with Environment.", "ta": "51A(g) சுற்றுச்சூழல் பற்றியது."},
            "B": {"en": "51A(h) deals with Scientific temper.", "ta": "51A(h) அறிவியல் மனப்பான்மை பற்றியது."},
            "C": {"en": "Correct. 51A(j) deals with Striving for Excellence.", "ta": "சரி. 51A(j) சிறப்பினை நோக்கி முயலுதல் பற்றியது."},
            "D": {"en": "51A(k) deals with Child education.", "ta": "51A(k) குழந்தைகள் கல்வி பற்றியது."}
        },
        "tnpsc_tip": {
            "en": "Covers two spheres: Individual activity and Collective activity.",
            "ta": "இரண்டு பிரிவுகளை உள்ளடக்கியது: தனிநபர் செயல்பாடு மற்றும் கூட்டுச் செயல்பாடு."
        }
    },
    {
        "id": "FD_E_026",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Article-based",
        "question": {
            "en": "Article 51A(k) mandates providing opportunities for education to a child or ward belonging to which age group?",
            "ta": "உறுப்பு 51A(k) எந்த வயதுக் குழுவைச் சேர்ந்த குழந்தைக்குக் கல்வி வாய்ப்புகளை வழங்குவதைக் கட்டாயமாக்குகிறது?"
        },
        "options": [
            {"id": "A", "en": "0 to 6 years", "ta": "0 முதல் 6 வயது வரை"},
            {"id": "B", "en": "6 to 14 years", "ta": "6 முதல் 14 வயது வரை"},
            {"id": "C", "en": "6 to 18 years", "ta": "6 முதல் 18 வயது வரை"},
            {"id": "D", "en": "14 to 18 years", "ta": "14 முதல் 18 வயது வரை"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "Article 51A(k) applies specifically to children between the age of SIX and FOURTEEN (6 to 14) years.",
            "ta": "உறுப்பு 51A(k) குறிப்பாக ஆறு முதல் பதினான்கு (6 முதல் 14) வயது வரையிலான குழந்தைகளுக்குப் பொருந்தும்."
        },
        "why_not_others": {
            "A": {"en": "0 to 6 years is covered under DPSP Article 45.", "ta": "0 முதல் 6 வயது வரை DPSP உறுப்பு 45-ன் கீழ் வருகிறது."},
            "B": {"en": "Correct. 6 to 14 years is the age group in Art 51A(k) and Art 21A.", "ta": "சரி. 6 முதல் 14 வயது வரை என்பது உறுப்பு 51A(k) மற்றும் 21A-ன் வயதுக் குழுவாகும்."},
            "C": {"en": "6 to 18 years is under POCSO Act / Child Rights Convention, not Art 51A(k).", "ta": "6 முதல் 18 வயது என்பது போக்சோ சட்டத்தில் உள்ளதே தவிர உறுப்பு 51A(k)-ல் இல்லை."},
            "D": {"en": "Incorrect age group.", "ta": "தவறான வயதுக் குழு."}
        },
        "tnpsc_tip": {
            "en": "Both Article 21A (FR) and Article 51A(k) (FD) target the EXACT same 6-14 age group.",
            "ta": "உறுப்பு 21A (FR) மற்றும் உறுப்பு 51A(k) (FD) ஆகிய இரண்டும் ஒரே 6-14 வயதுக் குழுவையே இலக்காகக் கொண்டுள்ளன."
        }
    },
    {
        "id": "FD_E_027",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Article-based",
        "question": {
            "en": "Who bears the Fundamental Duty under Article 51A(k) to provide education opportunities to a child aged 6 to 14 years?",
            "ta": "6 முதல் 14 வயது வரையிலான குழந்தைக்குக் கல்வி வாய்ப்புகளை வழங்க உறுப்பு 51A(k)-ன் கீழ் அடிப்படை கடமையைக் கொண்டிருப்பவர் யார்?"
        },
        "options": [
            {"id": "A", "en": "Parent or Guardian", "ta": "பெற்றோர் அல்லது பாதுகாவலர்"},
            {"id": "B", "en": "The State Government", "ta": "மாநில அரசாங்கம்"},
            {"id": "C", "en": "The Central Government", "ta": "மத்திய அரசாங்கம்"},
            {"id": "D", "en": "School Principal", "ta": "பள்ளி முதல்வர்"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Article 51A(k) places the Fundamental Duty on the PARENT or GUARDIAN of the child.",
            "ta": "உறுப்பு 51A(k) બાળக்கின் பெற்றோர் அல்லது பாதுகாவலர் மீது அடிப்படை கடமையை விதிக்கிறது."
        },
        "why_not_others": {
            "A": {"en": "Correct. Parent or Guardian bears the duty under Art 51A(k).", "ta": "சரி. பெற்றோர் அல்லது பாதுகாவலர் உறுப்பு 51A(k)-ன் கீழ் கடமையைக் கொண்டுள்ளனர்."},
            "B": {"en": "State Government duty is under Article 21A (Fundamental Right).", "ta": "மாநில அரசின் கடமை உறுப்பு 21A-ன் கீழ் உள்ளது (அடிப்படை உரிமை)."},
            "C": {"en": "Central Government obligation is under Art 21A / RTE Act.", "ta": "மத்திய அரசின் பொறுப்பு உறுப்பு 21A / RTE சட்டத்தில் உள்ளது."},
            "D": {"en": "School principal has administrative duties under RTE Act.", "ta": "பள்ளி முதல்வருக்கு RTE சட்டத்தில் நிர்வாகக் கடமைகள் உள்ளன."}
        },
        "tnpsc_tip": {
            "en": "Art 21A commands the STATE | Art 51A(k) commands the PARENT/GUARDIAN.",
            "ta": "உறுப்பு 21A அரசுக்கு ஆணையிடுகிறது | உறுப்பு 51A(k) பெற்றோர்/பாதுகாவலருக்கு ஆணையிடுகிறது."
        }
    },
    {
        "id": "FD_E_028",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Comparison",
        "question": {
            "en": "Which Article of Part III makes free and compulsory education for children aged 6 to 14 years a Fundamental Right guaranteed by the State?",
            "ta": "6 முதல் 14 வயது வரையிலான குழந்தைகளுக்கு இலவச மற்றும் கட்டாயக் கல்வியை அரசால் உத்தரவாதம் அளிக்கப்பட்ட அடிப்படை உரிமையாக பகுதி III-ன் எந்த உறுப்பு மாற்றுகிறது?"
        },
        "options": [
            {"id": "A", "en": "Article 21A", "ta": "உறுப்பு 21A"},
            {"id": "B", "en": "Article 45", "ta": "உறுப்பு 45"},
            {"id": "C", "en": "Article 51A(k)", "ta": "உறுப்பு 51A(k)"},
            {"id": "D", "en": "Article 19(1)(a)", "ta": "உறுப்பு 19(1)(a)"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Article 21A in Part III is a Fundamental Right obligating the State to provide free and compulsory education to children aged 6 to 14 years.",
            "ta": "பகுதி III-ல் உள்ள உறுப்பு 21A 6 முதல் 14 வயது வரையிலான குழந்தைகளுக்கு இலவச கட்டாயக் கல்வி வழங்க அரசைப் பொறுப்பாக்கும் அடிப்படை உரிமையாகும்."
        },
        "why_not_others": {
            "A": {"en": "Correct. Article 21A is the Fundamental Right for education.", "ta": "சரி. உறுப்பு 21A கல்விக்கான அடிப்படை உரிமை ஆகும்."},
            "B": {"en": "Article 45 is a DPSP for early childhood care below 6 years.", "ta": "உறுப்பு 45 6 வயதிற்குட்பட்டோருக்கான DPSP ஆகும்."},
            "C": {"en": "Article 51A(k) is a Fundamental Duty of parents.", "ta": "உறுப்பு 51A(k) பெற்றோரின் அடிப்படை கடமை ஆகும்."},
            "D": {"en": "Article 19(1)(a) guarantees freedom of speech and expression.", "ta": "உறுப்பு 19(1)(a) பேச்சுரிமையை உத்தரவாதம் செய்கிறது."}
        },
        "tnpsc_tip": {
            "en": "Inserted by the 86th Constitutional Amendment Act, 2002.",
            "ta": "2002-ன் 86வது அரசியலமைப்பு திருத்தச் சட்டத்தால் சேர்க்கப்பட்டது."
        }
    },
    {
        "id": "FD_E_029",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Comparison",
        "question": {
            "en": "Which Article of Directive Principles of State Policy (Part IV) directs the State to provide early childhood care and education for children until they complete the age of six years?",
            "ta": "குழந்தைகள் ஆறு வயதை நிறைவு செய்யும் வரை முன்பருவப் பராமரிப்பு மற்றும் கல்வியை வழங்க அரசு வழிகாட்டு நெறிமுறைகளின் (பகுதி IV) எந்த உறுப்பு அரசுக்கு வழிகாட்டுகிறது?"
        },
        "options": [
            {"id": "A", "en": "Article 39(f)", "ta": "உறுப்பு 39(f)"},
            {"id": "B", "en": "Article 45", "ta": "உறுப்பு 45"},
            {"id": "C", "en": "Article 47", "ta": "உறுப்பு 47"},
            {"id": "D", "en": "Article 51A(k)", "ta": "உறுப்பு 51A(k)"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "Article 45 in Part IV (DPSP) directs the State to provide early childhood care and education for all children until they complete six years.",
            "ta": "பகுதி IV-ல் உள்ள உறுப்பு 45 (DPSP) அனைத்துக் குழந்தைகளுக்கும் ஆறு வயது வரையில் முன்பருவப் பராமரிப்பு மற்றும் கல்வியை வழங்க அரசுக்கு வழிகாட்டுகிறது."
        },
        "why_not_others": {
            "A": {"en": "Art 39(f) directs opportunities for healthy development of children.", "ta": "உறுப்பு 39(f) குழந்தைகள் ஆரோக்கியமான வளர்ச்சிக்கு வாய்ப்பளிக்க வழிகாட்டுகிறது."},
            "B": {"en": "Correct. Article 45 covers early childhood care below 6 years.", "ta": "சரி. உறுப்பு 45 6 வயதிற்குட்பட்ட முன்பருவப் பராமரிப்பை உள்ளடக்கியது."},
            "C": {"en": "Art 47 deals with nutrition, public health and prohibition.", "ta": "உறுப்பு 47 சத்துணவு, பொது சுகாதாரம் மற்றும் மதுவிலக்கு பற்றியது."},
            "D": {"en": "Art 51A(k) is a Fundamental Duty for 6-14 years.", "ta": "உறுப்பு 51A(k) 6-14 வயதுக்கான அடிப்படை கடமை."}
        },
        "tnpsc_tip": {
            "en": "Substituted by 86th CAA 2002 when Art 21A was created for 6-14 age group.",
            "ta": "86வது திருத்தம் 2002 மூலம் 6-14 வயதுக் குழுவிற்கு உறுப்பு 21A உருவாக்கப்பட்ட போது இது மாற்றப்பட்டது."
        }
    },
    {
        "id": "FD_E_030",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Comparison",
        "question": {
            "en": "Which Article of Directive Principles of State Policy (Part IV) obligates the STATE to protect and improve the environment and safeguard forests and wildlife?",
            "ta": "சுற்றுச்சூழலைப் பாதுகாத்து மேம்படுத்தவும், காடுகள் மற்றும் வனவிலங்குகளைப் பேணவும் அரசைப் பொறுப்பாக்கும் அரசு வழிகாட்டு நெறிமுறைகளின் (பகுதி IV) உறுப்பு எது?"
        },
        "options": [
            {"id": "A", "en": "Article 48A", "ta": "உறுப்பு 48A"},
            {"id": "B", "en": "Article 51A(g)", "ta": "உறுப்பு 51A(g)"},
            {"id": "C", "en": "Article 49", "ta": "உறுப்பு 49"},
            {"id": "D", "en": "Article 50", "ta": "உறுப்பு 50"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Article 48A (DPSP) obligates the State to protect and improve the environment and safeguard forests and wildlife.",
            "ta": "உறுப்பு 48A (DPSP) சுற்றுச்சூழலைப் பாதுகாத்து மேம்படுத்தவும் காடுகள் மற்றும் வனவிலங்குகளைப் பேணவும் அரசைப் பொறுப்பாக்குகிறது."
        },
        "why_not_others": {
            "A": {"en": "Correct. Article 48A is the DPSP environment directive for State.", "ta": "சரி. உறுப்பு 48A என்பது அரசுக்கான DPSP சுற்றுச்சூழல் வழிகாட்டுதலாகும்."},
            "B": {"en": "Article 51A(g) is the Fundamental Duty for Citizens.", "ta": "உறுப்பு 51A(g) என்பது குடிமக்களுக்கான அடிப்படை கடமை."},
            "C": {"en": "Article 49 deals with protection of monuments of national importance.", "ta": "உறுப்பு 49 தேசிய முக்கியத்துவம் வாய்ந்த நினைவுச் சின்னங்களைப் பாதுகாப்பது பற்றியது."},
            "D": {"en": "Article 50 deals with separation of Judiciary from Executive.", "ta": "உறுப்பு 50 நீதித்துறையை நிர்வாகத்துறையிலிருந்து பிரிப்பது பற்றியது."}
        },
        "tnpsc_tip": {
            "en": "Both Article 48A (DPSP) and Article 51A(g) (FD) were added by the 42nd Amendment Act 1976.",
            "ta": "உறுப்பு 48A (DPSP) மற்றும் உறுப்பு 51A(g) (FD) ஆகிய இரண்டும் 42வது திருத்தச் சட்டம் 1976 மூலம் சேர்க்கப்பட்டன."
        }
    },
    {
        "id": "FD_E_031",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Comparison",
        "question": {
            "en": "What is the primary difference between Article 48A and Article 51A(g) regarding environmental protection?",
            "ta": "சுற்றுச்சூழல் பாதுகாப்பைப் பொறுத்தவரை உறுப்பு 48A மற்றும் உறுப்பு 51A(g) இடையே உள்ள முதன்மை வேறுபாடு என்ன?"
        },
        "options": [
            {"id": "A", "en": "Article 48A is a DPSP for State; Article 51A(g) is a Fundamental Duty for Citizens", "ta": "உறுப்பு 48A என்பது அரசுக்கான DPSP; உறுப்பு 51A(g) என்பது குடிமக்களுக்கான அடிப்படை கடமை"},
            {"id": "B", "en": "Article 48A applies to citizens; Article 51A(g) applies to foreigners", "ta": "உறுப்பு 48A குடிமக்களுக்குப் பொருந்தும்; உறுப்பு 51A(g) வெளிநாட்டினருக்குப் பொருந்தும்"},
            {"id": "C", "en": "Article 48A is justiciable in court; Article 51A(g) is not justiciable", "ta": "உறுப்பு 48A நீதிமன்றத்தால் அமல்படுத்தக் கூடியது; உறுப்பு 51A(g) அமல்படுத்த முடியாதது"},
            {"id": "D", "en": "Article 48A was added in 2002; Article 51A(g) was added in 1950", "ta": "உறுப்பு 48A 2002-ல் சேர்க்கப்பட்டது; உறுப்பு 51A(g) 1950-ல் சேர்க்கப்பட்டது"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Article 48A (Part IV DPSP) commands the STATE to protect environment, while Article 51A(g) (Part IVA FD) commands EVERY CITIZEN to protect environment.",
            "ta": "உறுப்பு 48A (DPSP) அரசைச் சுற்றுச்சூழலைப் பாதுகாக்க ஆணையிடுகிறது, ஆனால் உறுப்பு 51A(g) (FD) ஒவ்வொரு குடிமகனையும் சுற்றுச்சூழலைப் பாதுகாக்க ஆணையிடுகிறது."
        },
        "why_not_others": {
            "A": {"en": "Correct. Art 48A = State DPSP; Art 51A(g) = Citizen Duty.", "ta": "சரி. உறுப்பு 48A = அரசு DPSP; உறுப்பு 51A(g) = குடிமகன் கடமை."},
            "B": {"en": "Both provisions apply domestically within India.", "ta": "இரு விதிகளும் இந்தியாவிற்குள் பொருந்தும்."},
            "C": {"en": "Neither DPSP nor FD is directly justiciable without supporting laws.", "ta": "ஆதரவுச் சட்டங்கள் இன்றி DPSP அல்லது FD நேரடியாக அமல்படுத்தக்கூடியவை அல்ல."},
            "D": {"en": "Both were added by 42nd Amendment in 1976.", "ta": "இரண்டும் 1976-ல் 42வது திருத்தத்தால் சேர்க்கப்பட்டன."}
        },
        "tnpsc_tip": {
            "en": "High-yield statement trap! Always check whether the question asks for State duty or Citizen duty.",
            "ta": "முக்கியக் கூற்றுப் பொறி! கேள்வி அரசு கடமையைக் கேட்கிறதா அல்லது குடிமகன் கடமையைக் கேட்கிறதா என்பதை எப்போதும் சரிபார்க்கவும்."
        }
    },
    {
        "id": "FD_E_032",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Direct",
        "question": {
            "en": "On which date did Part IVA (Fundamental Duties) introduced by the 42nd Constitutional Amendment Act come into force?",
            "ta": "42வது அரசியலமைப்பு திருத்தச் சட்டத்தால் அறிமுகப்படுத்தப்பட்ட பகுதி IVA (அடிப்படை கடமைகள்) எந்த நாளில் அமலுக்கு வந்தது?"
        },
        "options": [
            {"id": "A", "en": "26th January 1950", "ta": "26 ஜனவரி 1950"},
            {"id": "B", "en": "15th August 1947", "ta": "15 ஆகஸ்ட் 1947"},
            {"id": "C", "en": "3rd January 1977", "ta": "3 ஜனவரி 1977"},
            {"id": "D", "en": "12th December 2002", "ta": "12 டிசம்பர் 2002"}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "Part IVA containing Fundamental Duties came into force on 3rd January 1977 following the 42nd CAA 1976.",
            "ta": "அடிப்படை கடமைகளைக் கொண்ட பகுதி IVA 42வது திருத்தம் 1976-ஐத் தொடர்ந்து 1977 ஜனவரி 3 அன்று அமலுக்கு வந்தது."
        },
        "why_not_others": {
            "A": {"en": "26th January 1950 is Republic Day (Commencement of Constitution).", "ta": "26 ஜனவரி 1950 குடியரசு நாள் (அரசியலமைப்பு அமலாக்கம்)."},
            "B": {"en": "15th August 1947 is Independence Day.", "ta": "15 ஆகஸ்ட் 1947 சுதந்திர நாள்."},
            "C": {"en": "Correct. 3rd January 1977 is the enforcement date of Part IVA.", "ta": "சரி. 3 ஜனவரி 1977 என்பது பகுதி IVA அமலுக்கு வந்த நாளாகும்."},
            "D": {"en": "2002 is the year of 86th Amendment Act.", "ta": "2002 என்பது 86வது திருத்தச் சட்டத்தின் ஆண்டு."}
        },
        "tnpsc_tip": {
            "en": "3rd January is observed by some institutions as 'Fundamental Duties Day' in India.",
            "ta": "ஜனவரி 3 இந்தியாவில் சில நிறுவனங்களால் 'அடிப்படை கடமைகள் நாளாக' அனுசரிக்கப்படுகிறது."
        }
    },
    {
        "id": "FD_E_033",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Direct",
        "question": {
            "en": "What is the meaning of the word 'abjure' used in Article 51A(i) ['To safeguard public property and to abjure violence']?",
            "ta": "உறுப்பு 51A(i)-ல் பயன்படுத்தப்பட்ட 'abjure' என்ற சொல்லின் பொருள் என்ன ['பொதுச் சொத்தைப் பாதுகாத்தலும் வன்முறையைக் கைவிடுதலும்']?"
        },
        "options": [
            {"id": "A", "en": "To promote or encourage actively", "ta": "தீவிரமாக ஊக்குவித்தல் அல்லது தூண்டுதல்"},
            {"id": "B", "en": "To postpone for a short period", "ta": "குறுகிய காலத்திற்கு ஒத்திவைத்தல்"},
            {"id": "C", "en": "To compromise with conditions", "ta": "நிபந்தனைகளுடன் சமரசம் செய்தல்"},
            {"id": "D", "en": "To solemnly renounce, abandon or reject", "ta": "சத்தியப் பிரமாணத்தின் மூலம் கைவிடுதல் அல்லது நிராகரித்தல்"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "'Abjure' means to solemnly renounce, give up, or reject upon oath. Citizens are commanded to completely renounce violence.",
            "ta": "'Abjure' என்றால் வன்முறையை முற்றிலுமாகக் கைவிடுதல், துறத்தல் அல்லது நிராகரித்தல் ஆகும். வன்முறையை முற்றிலுமாகக் கைவிடக் குடிமக்களுக்கு ஆணையிடப்படுகிறது."
        },
        "why_not_others": {
            "A": {"en": "Abjure means the opposite of promote.", "ta": "Abjure என்பது ஊக்குவிப்பதற்கு எதிரான சொல்."},
            "B": {"en": "Incorrect meaning.", "ta": "தவறான பொருள்."},
            "C": {"en": "Incorrect meaning.", "ta": "தவறான பொருள்."},
            "D": {"en": "Correct. Abjure means to solemnly renounce or abandon.", "ta": "சரி. Abjure என்றால் கைவிடுதல் அல்லது நிராகரித்தல்."}
        },
        "tnpsc_tip": {
            "en": "Article 51A(i) pairs safeguarding public property directly with abjuring violence.",
            "ta": "உறுப்பு 51A(i) பொதுச் சொத்தைப் பாதுகாப்பதை வன்முறையைக் கைவிடுவதோடு நேரடியாக இணைக்கிறது."
        }
    },
    {
        "id": "FD_E_034",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Direct",
        "question": {
            "en": "Which Parliamentary Act penalizes disrespect to the National Flag, National Anthem, and Constitution of India under Article 51A(a)?",
            "ta": "உறுப்பு 51A(a)-ன் கீழ் தேசியக் கொடி, தேசியக் கீதம் மற்றும் அரசியலமைப்பை அவமதிப்பதைத் தண்டிக்கும் நாடாளுமன்றச் சட்டம் எது?"
        },
        "options": [
            {"id": "A", "en": "Protection of Civil Rights Act, 1955", "ta": "சிவில் உரிமைகள் பாதுகாப்புச் சட்டம், 1955"},
            {"id": "B", "en": "Prevention of Insults to National Honour Act, 1971", "ta": "தேசிய கௌரவ அவமதிப்பு தடுப்புச் சட்டம், 1971"},
            {"id": "C", "en": "Unlawful Activities (Prevention) Act, 1967", "ta": "சட்டவிரோத நடவடிக்கைகள் தடுப்புச் சட்டம், 1967"},
            {"id": "D", "en": "Representation of the People Act, 1951", "ta": "மக்கள் பிரதிநிதித்துவச் சட்டம், 1951"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "The Prevention of Insults to National Honour Act, 1971 penalizes disrespect or insults to the National Flag, Constitution, and National Anthem.",
            "ta": "1971-ன் தேசிய கௌரவ அவமதிப்பு தடுப்புச் சட்டம் தேசியக் கொடி, அரசியலமைப்பு மற்றும் தேசியக் கீதத்தை அவமதிப்பதைத் தண்டிக்கிறது."
        },
        "why_not_others": {
            "A": {"en": "Civil Rights Act 1955 penalizes untouchability offenses.", "ta": "சிவில் உரிமைகள் பாதுகாப்புச் சட்டம் 1955 தீண்டாமை குற்றங்களைத் தண்டிக்கிறது."},
            "B": {"en": "Correct. Prevention of Insults to National Honour Act 1971.", "ta": "சரி. தேசிய கௌரவ அவமதிப்பு தடுப்புச் சட்டம் 1971."},
            "C": {"en": "UAPA 1967 deals with anti-national unlawful activities.", "ta": "UAPA 1967 தேசவிரோதச் சட்டவிரோத நடவடிக்கைகள் பற்றியது."},
            "D": {"en": "RPA 1951 deals with elections.", "ta": "RPA 1951 தேர்தல்கள் பற்றியது."}
        },
        "tnpsc_tip": {
            "en": "Statutory law providing criminal enforcement for Article 51A(a).",
            "ta": "உறுப்பு 51A(a)-க்கு குற்றவியல் அமலாக்கத்தை வழங்கும் சட்டப்பூர்வச் சட்டம்."
        }
    },
    {
        "id": "FD_E_035",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Direct",
        "question": {
            "en": "In which landmark Supreme Court case was it held that standing up respectfully during the National Anthem fulfills Article 51A(a), and non-singing due to genuine religious faith is protected under Article 19(1)(a) and 25?",
            "ta": "தேசியக் கீதத்தின் போது மரியாதையுடன் எழுந்து நிற்பதே உறுப்பு 51A(a)-ஐப் பூர்த்தி செய்கிறது என்றும், உண்மையான மத நம்பிக்கையால் பாடாமல் இருப்பது உறுப்புகள் 19(1)(a) & 25-ன் கீழ் பாதுகாக்கப்படுகிறது என்றும் தீர்ப்பளிக்கப்பட்ட முக்கிய உச்ச நீதிமன்ற வழக்கு எது?"
        },
        "options": [
            {"id": "A", "en": "Kesavananda Bharati v. State of Kerala (1973)", "ta": "கேசவாநந்த பாரதி vs கேரளா மாநிலம் (1973)"},
            {"id": "B", "en": "Bijoe Emmanuel v. State of Kerala (1986)", "ta": "பிஜோய் இம்மானுவேல் vs கேரளா மாநிலம் (1986)"},
            {"id": "C", "en": "Minerva Mills v. Union of India (1980)", "ta": "மினர்வா மில்ஸ் vs இந்திய யூனியன் (1980)"},
            {"id": "D", "en": "Maneka Gandhi v. Union of India (1978)", "ta": "மேனகா காந்தி vs இந்திய யூனியன் (1978)"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "In Bijoe Emmanuel v. State of Kerala (1986) [National Anthem Case], SC ruled that standing respectfully fulfills Art 51A(a), and right to remain silent is protected.",
            "ta": "பிஜோய் இம்மானுவேல் vs கேரளா மாநிலம் (1986) [தேசிய கீத வழக்கு] வழக்கில், மரியாதையுடன் எழுந்து நிற்பதே உறுப்பு 51A(a)-ஐப் பூர்த்தி செய்கிறது என்றும் அமைதியாக இருக்கும் உரிமை பாதுகாக்கப்படுகிறது என்றும் உச்ச நீதிமன்றம் தீர்ப்பளித்தது."
        },
        "why_not_others": {
            "A": {"en": "Kesavananda Bharati case established Basic Structure doctrine.", "ta": "கேசவாநந்த பாரதி வழக்கு அடிப்படை அமைப்புக் கோட்பாட்டை நிறுவியது."},
            "B": {"en": "Correct. Bijoe Emmanuel v. State of Kerala 1986.", "ta": "சரி. பிஜோய் இம்மானுவேல் vs கேரளா மாநிலம் 1986."},
            "C": {"en": "Minerva Mills balanced FRs and DPSP.", "ta": "மினர்வா மில்ஸ் FR மற்றும் DPSP-ஐ சமநிலைப்படுத்தியது."},
            "D": {"en": "Maneka Gandhi expanded Article 21 Personal Liberty.", "ta": "மேனகா காந்தி உறுப்பு 21 தனிநபர் சுதந்திரத்தை விரிவாக்கியது."}
        },
        "tnpsc_tip": {
            "en": "Popularly known as the 'Jehovah's Witnesses National Anthem Case'.",
            "ta": "பிரபலமாக 'யெகோவாவின் சாட்சிகள் தேசிய கீத வழக்கு' என அழைக்கப்படுகிறது."
        }
    },
    {
        "id": "FD_E_036",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Direct",
        "question": {
            "en": "What is the core distinction between 'Scientific Temper' [Article 51A(h)] and 'Scientific Knowledge'?",
            "ta": "அறிவியல் மனப்பான்மை [உறுப்பு 51A(h)] மற்றும் அறிவியல் அறிவு ஆகியவற்றிற்கு இடையேயான முதன்மை வேறுபாடு என்ன?"
        },
        "options": [
            {"id": "A", "en": "Scientific Temper is a rational attitude of mind; Scientific Knowledge is academic data and degrees", "ta": "அறிவியல் மனப்பான்மை என்பது பகுத்தறிவு மனநிலை; அறிவியல் அறிவு என்பது கல்வித் தரவுகள் மற்றும் பட்டங்கள்"},
            {"id": "B", "en": "Scientific Temper is acquired from books; Scientific Knowledge is born naturally", "ta": "அறிவியல் மனப்பான்மை புத்தகங்களிலிருந்து பெறப்படுகிறது; அறிவியல் அறிவு இயற்கையாகப் பிறக்கிறது"},
            {"id": "C", "en": "Scientific Temper applies only to scientists; Scientific Knowledge applies to all citizens", "ta": "அறிவியல் மனப்பான்மை விஞ்ஞானிகளுக்கு மட்டுமே பொருந்தும்; அறிவியல் அறிவு அனைத்துக் குடிமக்களுக்கும் பொருந்தும்"},
            {"id": "D", "en": "There is no difference between the two terms", "ta": "இவ்விரண்டு சொற்களுக்கும் இடையே எந்த வேறுபாடும் இல்லை"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Scientific Temper is a rational attitude of mind that relies on logic, empirical evidence, and rejects superstition. Scientific Knowledge consists of academic data or technical degrees.",
            "ta": "அறிவியல் மனப்பான்மை என்பது தர்க்கம், ஆதாரங்களின் அடிப்படையில் இயங்கும் மூடநம்பிக்கைகளை நிராகரிக்கும் பகுத்தறிவு மனநிலையாகும். அறிவியல் அறிவு என்பது கல்வித் தரவுகள் அல்லது பட்டங்கள் ஆகும்."
        },
        "why_not_others": {
            "A": {"en": "Correct. Scientific Temper is rational mindset; Knowledge is academic data.", "ta": "சரி. அறிவியல் மனப்பான்மை என்பது பகுத்தறிவு மனநிலை; அறிவு என்பது கல்வித் தரவு."},
            "B": {"en": "Incorrect definition.", "ta": "தவறான வரையறை."},
            "C": {"en": "Art 51A(h) commands EVERY citizen to develop scientific temper.", "ta": "உறுப்பு 51A(h) ஒவ்வொரு குடிமகனையும் அறிவியல் மனப்பான்மையை வளர்க்க ஆணையிடுகிறது."},
            "D": {"en": "There is a clear conceptual distinction.", "ta": "தெளிவான தத்துவார்த்த வேறுபாடு உள்ளது."}
        },
        "tnpsc_tip": {
            "en": "Jawaharlal Nehru popularized the phrase 'Scientific Temper' in his book 'Discovery of India'.",
            "ta": "ஜவஹர்லால் நேரு தனது 'டிஸ்கவரி ஆஃப் இந்தியா' புத்தகத்தில் 'அறிவியல் மனப்பான்மை' என்ற சொற்றொடரைப் பிரபலப்படுத்தினார்."
        }
    },
    {
        "id": "FD_E_037",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Comparison",
        "question": {
            "en": "Article 51A(f) (Duty to value and preserve rich heritage of composite culture) complements which Articles of Fundamental Rights?",
            "ta": "உறுப்பு 51A(f) (கூட்டுப் பண்பாட்டின் வளமான பாரம்பரியத்தைப் பேணும் கடமை) அடிப்படை உரிமைகளின் எந்த உறுப்புகளுக்குத் துணையாக நிற்கிறது?"
        },
        "options": [
            {"id": "A", "en": "Articles 14 and 15", "ta": "உறுப்புகள் 14 மற்றும் 15"},
            {"id": "B", "en": "Articles 29 and 30", "ta": "உறுப்புகள் 29 மற்றும் 30"},
            {"id": "C", "en": "Articles 32 and 226", "ta": "உறுப்புகள் 32 மற்றும் 226"},
            {"id": "D", "en": "Articles 23 and 24", "ta": "உறுப்புகள் 23 மற்றும் 24"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "Article 51A(f) (Composite culture duty) complements Articles 29 and 30 (Cultural and Educational Rights of minorities/sections).",
            "ta": "உறுப்பு 51A(f) (கூட்டுப் பண்பாட்டுக் கடமை) உறுப்புகள் 29 மற்றும் 30 (சிறுபான்மையினரின் பண்பாட்டு மற்றும் கல்வி உரிமைகள்) ஆகியவற்றுக்குத் துணையாக நிற்கிறது."
        },
        "why_not_others": {
            "A": {"en": "Articles 14 and 15 deal with Equality.", "ta": "உறுப்புகள் 14 மற்றும் 15 சமத்துவம் பற்றியவை."},
            "B": {"en": "Correct. Articles 29 and 30 deal with Cultural Rights.", "ta": "சரி. உறுப்புகள் 29 மற்றும் 30 பண்பாட்டு உரிமைகள் பற்றியவை."},
            "C": {"en": "Articles 32 and 226 deal with Writ Remedies.", "ta": "உறுப்புகள் 32 மற்றும் 226 பேராணை பரிகாரங்கள் பற்றியவை."},
            "D": {"en": "Articles 23 and 24 deal with Right against Exploitation.", "ta": "உறுப்புகள் 23 மற்றும் 24 சுரண்டலுக்கு எதிரான உரிமை பற்றியவை."}
        },
        "tnpsc_tip": {
            "en": "Arts 29-30 protect minority distinct culture; Art 51A(f) commands all citizens to preserve overall composite culture.",
            "ta": "உறுப்புகள் 29-30 சிறுபான்மையினரின் பண்பாட்டைப் பாதுகாக்கின்றன; உறுப்பு 51A(f) அனைத்துக் குடிமக்களையும் கூட்டுப் பண்பாட்டைப் பேண ஆணையிடுகிறது."
        }
    },
    {
        "id": "FD_E_038",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Direct",
        "question": {
            "en": "Which Part of the Constitution of India contains Fundamental Rights?",
            "ta": "இந்திய அரசியலமைப்பின் எந்தப் பகுதியில் அடிப்படை உரிமைகள் இடம்பெற்றுள்ளன?"
        },
        "options": [
            {"id": "A", "en": "Part II", "ta": "பகுதி II"},
            {"id": "B", "en": "Part IV", "ta": "பகுதி IV"},
            {"id": "C", "en": "Part III", "ta": "பகுதி III"},
            {"id": "D", "en": "Part IVA", "ta": "பகுதி IVA"}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "Part III of the Constitution contains Fundamental Rights from Articles 12 to 35.",
            "ta": "அரசியலமைப்பின் பகுதி III உறுப்புகள் 12 முதல் 35 வரை அடிப்படை உரிமைகளைக் கொண்டுள்ளது."
        },
        "why_not_others": {
            "A": {"en": "Part II deals with Citizenship (Articles 5-11).", "ta": "பகுதி II குடியுரிமை பற்றியது (உறுப்புகள் 5-11)."},
            "B": {"en": "Part IV deals with DPSP (Articles 36-51).", "ta": "பகுதி IV DPSP பற்றியது (உறுப்புகள் 36-51)."},
            "C": {"en": "Correct. Part III contains Fundamental Rights.", "ta": "சரி. பகுதி III அடிப்படை உரிமைகளைக் கொண்டுள்ளது."},
            "D": {"en": "Part IVA deals with Fundamental Duties (Article 51A).", "ta": "பகுதி IVA அடிப்படை கடமைகள் பற்றியது (உறுப்பு 51A)."}
        },
        "tnpsc_tip": {
            "en": "Part III = FR (Justiciable) | Part IV = DPSP (Non-justiciable) | Part IVA = FD (Non-justiciable).",
            "ta": "பகுதி III = FR (அமல்படுத்தக் கூடியவை) | பகுதி IV = DPSP (அமல்படுத்த முடியாதவை) | பகுதி IVA = FD (அமல்படுத்த முடியாதவை)."
        }
    },
    {
        "id": "FD_E_039",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Direct",
        "question": {
            "en": "Which Part of the Constitution of India contains the Directive Principles of State Policy (DPSP)?",
            "ta": "இந்திய அரசியலமைப்பின் எந்தப் பகுதியில் அரசு வழிகாட்டு நெறிமுறைகள் (DPSP) இடம்பெற்றுள்ளன?"
        },
        "options": [
            {"id": "A", "en": "Part III", "ta": "பகுதி III"},
            {"id": "B", "en": "Part IVA", "ta": "பகுதி IVA"},
            {"id": "C", "en": "Part IV", "ta": "பகுதி IV"},
            {"id": "D", "en": "Part IX", "ta": "பகுதி IX"}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "Part IV of the Constitution contains the Directive Principles of State Policy (Articles 36 to 51).",
            "ta": "அரசியலமைப்பின் பகுதி IV அரசு வழிகாட்டு நெறிமுறைகளைக் கொண்டுள்ளது (உறுப்புகள் 36 முதல் 51 வரை)."
        },
        "why_not_others": {
            "A": {"en": "Part III deals with Fundamental Rights.", "ta": "பகுதி III அடிப்படை உரிமைகள் பற்றியது."},
            "B": {"en": "Part IVA deals with Fundamental Duties.", "ta": "பகுதி IVA அடிப்படை கடமைகள் பற்றியது."},
            "C": {"en": "Correct. Part IV contains DPSP.", "ta": "சரி. பகுதி IV DPSP-ஐக் கொண்டுள்ளது."},
            "D": {"en": "Part IX deals with Panchayats.", "ta": "பகுதி IX பஞ்சாயத்துகள் பற்றியது."}
        },
        "tnpsc_tip": {
            "en": "DPSP is addressed to the STATE, whereas Fundamental Duties are addressed to CITIZENS.",
            "ta": "DPSP அரசுக்கு ஆணையிடுகிறது, ஆனால் அடிப்படை கடமைகள் குடிமக்களுக்கு ஆணையிடுகின்றன."
        }
    },
    {
        "id": "FD_E_040",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Direct",
        "question": {
            "en": "Which major democratic country is a rare exception having explicit Fundamental Duties enumerated in its Constitution?",
            "ta": "தனது அரசியலமைப்பில் வெளிப்படையான அடிப்படை கடமைகளைக் கொண்டுள்ள ஒரு அரிதான விதிவிலக்கான முக்கிய ஜனநாயக நாடு எது?"
        },
        "options": [
            {"id": "A", "en": "United States of America", "ta": "அமெரிக்கா"},
            {"id": "B", "en": "United Kingdom", "ta": "ஐக்கிய இராச்சியம்"},
            {"id": "C", "en": "Canada", "ta": "கனடா"},
            {"id": "D", "en": "Japan", "ta": "ஜப்பான்"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "Japan is one of the very few major democratic countries whose Constitution contains a specific list of duties of citizens.",
            "ta": "ஜப்பான் தனது அரசியலமைப்பில் குடிமக்களின் கடமைகளின் குறிப்பிட்ட பட்டியலைக் கொண்டுள்ள மிகச்சில முக்கிய ஜனநாயக நாடுகளில் ஒன்றாகும்."
        },
        "why_not_others": {
            "A": {"en": "US Constitution contains Bill of Rights but no explicit duties chapter.", "ta": "அமெரிக்க அரசியலமைப்பில் உரிமைகள் மசோதா உள்ளது ஆனால் கடமைகள் அத்தியாயம் இல்லை."},
            "B": {"en": "UK does not have a written constitution.", "ta": "பிரிட்டனுக்கு எழுதப்பட்ட அரசியலமைப்பு இல்லை."},
            "C": {"en": "Canadian Charter contains rights, not enumerated duties.", "ta": "கனடிய சாசனம் உரிமைகளைக் கொண்டுள்ளது, பட்டியலிடப்பட்ட கடமைகளை அல்ல."},
            "D": {"en": "Correct. Japanese Constitution contains explicit duties.", "ta": "சரி. ஜப்பானிய அரசியலமைப்பில் வெளிப்படையான கடமைகள் உள்ளன."}
        },
        "tnpsc_tip": {
            "en": "India borrowed duties from socialist USSR, but Japan is a democratic precedent.",
            "ta": "இந்தியா சமதர்ம சோவியத் யூனியனிலிருந்து கடமைகளைப் பெற்றது, ஆனால் ஜப்பான் ஒரு ஜனநாயக முன்மாதிரியாகும்."
        }
    },
    {
        "id": "FD_E_041",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Direct",
        "question": {
            "en": "Does non-performance of a Fundamental Duty directly attract criminal penalty under the Constitution of India itself?",
            "ta": "அடிப்படை கடமையைச் செய்யத் தவறுவது இந்திய அரசியலமைப்பின் கீழேயே напрямуюக் குற்றவியல் தண்டனையை ஈர்க்குமா?"
        },
        "options": [
            {"id": "A", "en": "No, non-performance is not directly punishable under Constitution unless Parliament enacts a specific law", "ta": "இல்லை, நாடாளுமன்றம் ஒரு குறிப்பிட்ட சட்டத்தை இயற்றாவிட்டால் அரசியலமைப்பின் கீழ் நேரடியாகத் தண்டனைக்குரியது அல்ல"},
            {"id": "B", "en": "Yes, it automatically results in immediate arrest and imprisonment under Article 51A", "ta": "ஆம், அது உறுப்பு 51A-ன் கீழ் தானாகவே உடனடிக் கைது மற்றும் சிறைத்தண்டனையை விளைவிக்கும்"},
            {"id": "C", "en": "Yes, it results in automatic cancellation of Indian citizenship", "ta": "ஆம், அது இந்தியக் குடியுரிமையைத் தானாகவே ரத்து செய்ய விளைவிக்கும்"},
            {"id": "D", "en": "Yes, but only during National Emergency", "ta": "ஆம், ஆனால் தேசிய அவசரநிலையின் போது மட்டுமே"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Fundamental Duties are non-justiciable. Article 51A itself does not prescribe direct penal punishments unless Parliament enacts specific legislation.",
            "ta": "அடிப்படை கடமைகள் நீதிமன்றங்களால் நேரடியாக அமல்படுத்த முடியாதவை. நாடாளுமன்றம் குறிப்பிட்ட சட்டத்தை இயற்றாவிட்டால் உறுப்பு 51A நேரடியாகத் தண்டனை விதிப்பதில்லை."
        },
        "why_not_others": {
            "A": {"en": "Correct. Parliament must pass specific enabling laws for penalties.", "ta": "சரி. தண்டனைகளுக்கு நாடாளுமன்றம் குறிப்பிட்ட சட்டங்களை இயற்ற வேண்டும்."},
            "B": {"en": "Article 51A contains no direct penal sanctions.", "ta": "உறுப்பு 51A-ல் நேரடி குற்றவியல் தண்டனைகள் இல்லை."},
            "C": {"en": "Citizenship cancellation is governed by Citizenship Act 1955.", "ta": "குடியுரிமை ரத்து 1955 குடியுரிமைச் சட்டத்தால் நெறிப்படுத்தப்படுகிறது."},
            "D": {"en": "Incorrect option.", "ta": "தவறான விருப்பம்."}
        },
        "tnpsc_tip": {
            "en": "Examples of parliamentary penalty laws: Prevention of Insults to National Honour Act 1971, Wildlife Act 1972.",
            "ta": "நாடாளுமன்றத் தண்டனைச் சட்டங்களின் உதாரணங்கள்: 1971 தேசிய கௌரவ அவமதிப்பு தடுப்புச் சட்டம், 1972 வனவிலங்கு சட்டம்."
        }
    },
    {
        "id": "FD_E_042",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Direct",
        "question": {
            "en": "The Justice J.S. Verma Committee (1999) was constituted for which primary purpose related to Fundamental Duties?",
            "ta": "அடிப்படை கடமைகள் தொடர்பாக எந்த முதன்மை நோக்கத்திற்காக நீதிபதி ஜே.எஸ். வர்மா குழு (1999) அமைக்கப்பட்டது?"
        },
        "options": [
            {"id": "A", "en": "To recommend deleting Fundamental Duties from the Constitution", "ta": "அரசியலமைப்பிலிருந்து அடிப்படை கடமைகளை நீக்கப் பரிந்துரைக்க"},
            {"id": "B", "en": "To draft the 42nd Constitutional Amendment Act", "ta": "42வது அரசியலமைப்பு திருத்தச் சட்டத்தை வரையறுக்க"},
            {"id": "C", "en": "To identify existing legal provisions enforcing Fundamental Duties and teach them in schools", "ta": "அடிப்படை கடமைகளை அமல்படுத்தும் நிலவும் சட்ட விதிகளைக் கண்டறிந்து பள்ளிகளில் கற்பிக்க"},
            {"id": "D", "en": "To make Fundamental Duties justiciable in Supreme Court", "ta": "அடிப்படை கடமைகளை உச்ச நீதிமன்றத்தில் அமல்படுத்தக் கூடியதாக மாற்ற"}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "The Verma Committee (1999) identified non-operationalized legal provisions enforcing duties and recommended teaching duties in educational institutions.",
            "ta": "வர்மா குழு (1999) கடமைகளை அமல்படுத்தும் நிலவும் சட்ட விதிகளைக் கண்டறிந்து கல்வி நிறுவனங்களில் கடமைகளைக் கற்பிக்கப் பரிந்துரைத்தது."
        },
        "why_not_others": {
            "A": {"en": "Verma Committee supported expanding awareness of Fundamental Duties.", "ta": "வர்மா குழு அடிப்படை கடமைகள் பற்றிய விழிப்புணர்வை விரிவாக்குவதை ஆதரித்தது."},
            "B": {"en": "42nd CAA was drafted in 1976.", "ta": "42வது திருத்தம் 1976-ல் வரைவு செய்யப்பட்டது."},
            "C": {"en": "Correct. Identified legal provisions enforcing duties.", "ta": "சரி. கடமைகளை அமல்படுத்தும் சட்ட விதிகளைக் கண்டறிந்தது."},
            "D": {"en": "Incorrect objective.", "ta": "தவறான நோக்கம்."}
        },
        "tnpsc_tip": {
            "en": "Verma Committee listed statutes like IPC, Wildlife Act, Civil Rights Act enforcing Art 51A duties.",
            "ta": "வர்மா குழு உறுப்பு 51A கடமைகளை அமல்படுத்தும் IPC, வனவிலங்கு சட்டம், சிவில் உரிமைகள் சட்டம் போன்ற சட்டங்களைப் பட்டியலிட்டது."
        }
    },
    {
        "id": "FD_E_043",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Direct",
        "question": {
            "en": "The term 'Integrity' was added to the Preamble of the Constitution of India by which Constitutional Amendment Act?",
            "ta": "'ஒருமைப்பாடு' என்ற சொல் இந்திய அரசியலமைப்பின் முகப்புரையில் எந்த அரசியலமைப்பு திருத்தச் சட்டத்தால் சேர்க்கப்பட்டது?"
        },
        "options": [
            {"id": "A", "en": "44th Amendment Act, 1978", "ta": "44வது திருத்தச் சட்டம், 1978"},
            {"id": "B", "en": "86th Amendment Act, 2002", "ta": "86வது திருத்தச் சட்டம், 2002"},
            {"id": "C", "en": "1st Amendment Act, 1951", "ta": "1வது திருத்தச் சட்டம், 1951"},
            {"id": "D", "en": "42nd Amendment Act, 1976", "ta": "42வது திருத்தச் சட்டம், 1976"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "The 42nd Amendment Act 1976 added three words to Preamble: Socialist, Secular, and Integrity (also appearing in Art 51A(c)).",
            "ta": "42வது திருத்தச் சட்டம் 1976 முகப்புரையில் மூன்று சொற்களைச் சேர்த்தது: சமதர்ம, மதச்சார்பற்ற, மற்றும் ஒருமைப்பாடு (உறுப்பு 51A(c)-லும் உள்ளது)."
        },
        "why_not_others": {
            "A": {"en": "44th Amendment modified Emergency laws.", "ta": "44வது திருத்தம் அவசரநிலைச் சட்டங்களை மாற்றியது."},
            "B": {"en": "86th Amendment dealt with education.", "ta": "86வது திருத்தம் கல்வி பற்றியது."},
            "C": {"en": "1st Amendment 1951 added 9th Schedule.", "ta": "1வது திருத்தம் 1951 9வது அட்டவணையைச் சேர்த்தது."},
            "D": {"en": "Correct. 42nd Amendment 1976 added 'Integrity' to Preamble.", "ta": "சரி. 42வது திருத்தம் 1976 முகப்புரையில் 'ஒருமைப்பாடு' என்ற சொல்லைச் சேர்த்தது."}
        },
        "tnpsc_tip": {
            "en": "Article 51A(c) commands upholding 'Sovereignty, Unity and Integrity of India'.",
            "ta": "உறுப்பு 51A(c) 'இந்தியாவின் இறையாண்மை, ஒற்றுமை மற்றும் ஒருமைப்பாட்டைப் பேண' ஆணையிடுகிறது."
        }
    },
    {
        "id": "FD_E_044",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Direct",
        "question": {
            "en": "In AIIMS Students Union v. AIIMS (2002), what did the Supreme Court hold regarding the importance of Fundamental Duties?",
            "ta": "AIIMS மாணவர் சங்கம் vs AIIMS (2002) வழக்கில், அடிப்படை கடமைகளின் முக்கியத்துவம் குறித்து உச்ச நீதிமன்றம் என்ன தீர்ப்பளித்தது?"
        },
        "options": [
            {"id": "A", "en": "Fundamental Duties are equally important as Fundamental Rights and cannot be ignored during statutory interpretation", "ta": "அடிப்படை கடமைகள் அடிப்படை உரிமைகளுக்குச் சமமான முக்கியத்துவம் வாய்ந்தவை, சட்ட விளக்கத்தின் போது அவற்றைப் புறக்கணிக்க முடியாது"},
            {"id": "B", "en": "Fundamental Duties are inferior to DPSP and can be ignored", "ta": "அடிப்படை கடமைகள் DPSP-ஐ விடக் கீழானவை, அவற்றைப் புறக்கணிக்கலாம்"},
            {"id": "C", "en": "Fundamental Duties apply only to AIIMS medical students", "ta": "அடிப்படை கடமைகள் AIIMS மருத்துவ மாணவர்களுக்கு மட்டுமே பொருந்தும்"},
            {"id": "D", "en": "Fundamental Duties are unconstitutional", "ta": "அடிப்படை கடமைகள் அரசியலமைப்பிற்கு எதிரானவை"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "In AIIMS Students Union v. AIIMS (2002), SC held that Fundamental Duties, though non-justiciable, are equally as important as Fundamental Rights.",
            "ta": "AIIMS மாணவர் சங்கம் vs AIIMS (2002) வழக்கில், அடிப்படை கடமைகள் அமல்படுத்த முடியாதவை என்றாலும் அடிப்படை உரிமைகளுக்குச் சமமான முக்கியத்துவம் வாய்ந்தவை என உச்ச நீதிமன்றம் தீர்ப்பளித்தது."
        },
        "why_not_others": {
            "A": {"en": "Correct. FDs are equally important as FRs in constitutional interpretation.", "ta": "சரி. அரசியலமைப்பு விளக்கத்தில் கடமைகள் உரிமைகளுக்குச் சமமான முக்கியத்துவம் வாய்ந்தவை."},
            "B": {"en": "SC held duties cannot be ignored.", "ta": "கடமைகளைப் புறக்கணிக்க முடியாது என உச்ச நீதிமன்றம் கூறியது."},
            "C": {"en": "FDs apply to all citizens of India.", "ta": "கடமைகள் அனைத்து இந்தியக் குடிமக்களுக்கும் பொருந்தும்."},
            "D": {"en": "FDs are part of Part IVA of the Constitution.", "ta": "கடமைகள் அரசியலமைப்பின் பகுதி IVA-ன் பகுதியாகும்."}
        },
        "tnpsc_tip": {
            "en": "Harmonious balance between Rights, DPSP, and Duties forms constitutional bedrock.",
            "ta": "உரிமைகள், DPSP, கடமைகள் இடையேயான இணக்கமான சமநிலையே அரசியலமைப்பின் அடித்தளமாகும்."
        }
    },
    {
        "id": "FD_E_045",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Comparison",
        "question": {
            "en": "Right to a clean and wholesome environment is judicially recognized as a Fundamental Right under which Article of Part III?",
            "ta": "தூய்மையான மற்றும் ஆரோக்கியமான சுற்றுச்சூழலுக்கான உரிமை பகுதி III-ன் எந்த உறுப்பின் கீழ் நீதித்துறையால் அங்கீகரிக்கப்பட்ட அடிப்படை உரிமையாகும்?"
        },
        "options": [
            {"id": "A", "en": "Article 14", "ta": "உறுப்பு 14"},
            {"id": "B", "en": "Article 19", "ta": "உறுப்பு 19"},
            {"id": "C", "en": "Article 21", "ta": "உறுப்பு 21"},
            {"id": "D", "en": "Article 32", "ta": "உறுப்பு 32"}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "Supreme Court expanded Article 21 (Right to Life and Personal Liberty) to include the Right to a clean, wholesome, pollution-free environment.",
            "ta": "உச்ச நீதிமன்றம் உறுப்பு 21-ஐ (வாழும் உரிமை மற்றும் தனிநபர் சுதந்திரம்) தூய்மையான, மாசற்ற சுற்றுச்சூழலுக்கான உரிமையாக விரிவாக்கியுள்ளது."
        },
        "why_not_others": {
            "A": {"en": "Article 14 guarantees Equality before law.", "ta": "உறுப்பு 14 சட்டத்தின் முன் சமத்துவத்தை உத்தரவாதம் செய்கிறது."},
            "B": {"en": "Article 19 guarantees Six Freedoms.", "ta": "உறுப்பு 19 ஆறு சுதந்திரங்களை உத்தரவாதம் செய்கிறது."},
            "C": {"en": "Correct. Article 21 covers Right to Clean Environment.", "ta": "சரி. உறுப்பு 21 தூய்மையான சுற்றுச்சூழலுக்கான உரிமையை உள்ளடக்கியது."},
            "D": {"en": "Article 32 provides Constitutional Remedies.", "ta": "உறுப்பு 32 அரசியலமைப்பு பரிகாரங்களை வழங்குகிறது."}
        },
        "tnpsc_tip": {
            "en": "Art 21 (Clean Env Right) <-> Art 48A (State Env DPSP) <-> Art 51A(g) (Citizen Env FD).",
            "ta": "உறுப்பு 21 (சுற்றுச்சூழல் உரிமை) <-> உறுப்பு 48A (அரசு DPSP) <-> உறுப்பு 51A(g) (குடிமகன் FD)."
        }
    },
    {
        "id": "FD_E_046",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Article-based",
        "question": {
            "en": "Which sub-clause of Article 51A commands citizens to defend the country and render national service when called upon to do so?",
            "ta": "உறுப்பு 51A-ன் எந்த உட்பிரிவு குடிமக்களுக்குத் தேசத்தைப் பாதுகாக்கவும், தேவைப்படும்போது தேசிய சேவை ஆற்றவும் கட்டளையிடுகிறது?"
        },
        "options": [
            {"id": "A", "en": "Article 51A(b)", "ta": "உறுப்பு 51A(b)"},
            {"id": "B", "en": "Article 51A(d)", "ta": "உறுப்பு 51A(d)"},
            {"id": "C", "en": "Article 51A(f)", "ta": "உறுப்பு 51A(f)"},
            {"id": "D", "en": "Article 51A(h)", "ta": "உறுப்பு 51A(h)"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "Article 51A(d) obligates citizens 'To defend the country and render national service when called upon to do so.'",
            "ta": "உறுப்பு 51A(d) குடிமக்களுக்குக் கடமையாக்குகிறது: 'தேசத்தைப் பாதுகாத்தலும், தேவைப்படும்போது தேசிய சேவை ஆற்றுதலும்.'"
        },
        "why_not_others": {
            "A": {"en": "51A(b) covers freedom struggle ideals.", "ta": "51A(b) சுதந்திரப் போராட்ட லட்சியங்களை உள்ளடக்கியது."},
            "B": {"en": "Correct. 51A(d) covers defending country and rendering national service.", "ta": "சரி. 51A(d) தேசத்தைப் பாதுகாத்தல் மற்றும் தேசிய சேவை ஆற்றுதலை உள்ளடக்கியது."},
            "C": {"en": "51A(f) covers composite culture.", "ta": "51A(f) கூட்டுப் பண்பாட்டை உள்ளடக்கியது."},
            "D": {"en": "51A(h) covers scientific temper.", "ta": "51A(h) அறிவியல் மனப்பான்மையை உள்ளடக்கியது."}
        },
        "tnpsc_tip": {
            "en": "Memory tip: 'd' for 'defend country'.",
            "ta": "நினைவுக் குறிப்பு: 'd' என்பது 'defend country' (தேசத்தைப் பாதுகாத்தல்)."
        }
    },
    {
        "id": "FD_E_047",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Comparison",
        "question": {
            "en": "Protecting monuments and places of national importance is a State responsibility under which Article of Directive Principles of State Policy (Part IV)?",
            "ta": "தேசிய முக்கியத்துவம் வாய்ந்த நினைவுச் சின்னங்கள் மற்றும் இடங்களைப் பாதுகாப்பது அரசு வழிகாட்டு நெறிமுறைகளின் (பகுதி IV) எந்த உறுப்பின் கீழ் அரசின் பொறுப்பாகும்?"
        },
        "options": [
            {"id": "A", "en": "Article 48A", "ta": "உறுப்பு 48A"},
            {"id": "B", "en": "Article 49", "ta": "உறுப்பு 49"},
            {"id": "C", "en": "Article 50", "ta": "உறுப்பு 50"},
            {"id": "D", "en": "Article 51A(f)", "ta": "உறுப்பு 51A(f)"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "Article 49 (DPSP) obligates the State to protect monuments, places and objects of artistic or historic interest declared to be of national importance.",
            "ta": "உறுப்பு 49 (DPSP) தேசிய முக்கியத்துவம் வாய்ந்த கலை அல்லது வரலாற்றுச் சிறப்புமிக்க நினைவுச் சின்னங்கள் மற்றும் இடங்களைப் பாதுகாக்க அரசைப் பொறுப்பாக்குகிறது."
        },
        "why_not_others": {
            "A": {"en": "Article 48A deals with Environment, Forests & Wildlife.", "ta": "உறுப்பு 48A சுற்றுச்சூழல், காடுகள் & வனவிலங்குகள் பற்றியது."},
            "B": {"en": "Correct. Article 49 covers Monuments protection by State.", "ta": "சரி. உறுப்பு 49 அரசால் நினைவுச் சின்னங்கள் பாதுகாப்பை உள்ளடக்கியது."},
            "C": {"en": "Article 50 deals with Separation of Judiciary.", "ta": "உறுப்பு 50 நீதித்துறைப் பிரிப்பு பற்றியது."},
            "D": {"en": "Article 51A(f) is a Fundamental Duty for Citizens to preserve composite culture.", "ta": "உறுப்பு 51A(f) கூட்டுப் பண்பாட்டைப் பேண குடிமக்களுக்கான அடிப்படை கடமை."}
        },
        "tnpsc_tip": {
            "en": "Art 49 = State DPSP for Monuments | Art 51A(f) = Citizen FD for Composite Heritage.",
            "ta": "உறுப்பு 49 = நினைவுச் சின்னங்களுக்கான அரசு DPSP | உறுப்பு 51A(f) = கூட்டுப் பாரம்பரியத்திற்கான குடிமகன் FD."
        }
    },
    {
        "id": "FD_E_048",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Basic Conceptual",
        "question": {
            "en": "Fundamental Duties complement Fundamental Rights because Rights and Duties are conceptually:",
            "ta": "உரிமைகளும் கடமைகளும் தத்துவார்த்தமாக எவ்வாறு அமைந்திருப்பதால் அடிப்படை கடமைகள் அடிப்படை உரிமைகளுக்குத் துணையாக நிற்கின்றன?"
        },
        "options": [
            {"id": "A", "en": "Completely independent and unrelated to each other", "ta": "முற்றிலும் சுயாதீனமானவை மற்றும் ஒன்றோடொன்று தொடர்பில்லாதவை"},
            {"id": "B", "en": "Mutually destructive of each other", "ta": "ஒன்றையொன்று அழித்துக் கொள்பவை"},
            {"id": "C", "en": "Correlative, complementary, and inseverable", "ta": "ஒன்றோடொன்று தொடர்புடையவை, பரஸ்பரத் துணையானவை மற்றும் பிரிக்க முடியாதவை"},
            {"id": "D", "en": "Applicable only during National Emergency", "ta": "தேசிய அவசரநிலையின் போது மட்டுமே பொருந்தக்கூடியவை"}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "Rights and Duties are correlative, complementary, and inseverable. As Mahatma Gandhi stated, duty is the true source of rights.",
            "ta": "உரிமைகளும் கடமைகளும் ஒன்றோடொன்று தொடர்புடையவை, பரஸ்பரத் துணையானவை மற்றும் பிரிக்க முடியாதவை. மகாத்மா காந்தி கூறியது போல, கடமையே உரிமைகளின் உண்மையான ஊற்றுக்கண் ஆகும்."
        },
        "why_not_others": {
            "A": {"en": "Rights and duties are deeply interrelated.", "ta": "உரிமைகளும் கடமைகளும் ஆழமான தொடர்புடையவை."},
            "B": {"en": "They do not destroy each other; they support each other.", "ta": "அவை ஒன்றையொன்று அழிப்பதில்லை; ஒன்றையொன்று ஆதரிக்கின்றன."},
            "C": {"en": "Correct. Rights and Duties are correlative and inseverable.", "ta": "சரி. உரிமைகளும் கடமைகளும் தொடர்புடையவை மற்றும் பிரிக்க முடியாதவை."},
            "D": {"en": "They apply continuously during normal peacetime as well.", "ta": "சாதாரண அமைதிக்காலத்திலும் அவை தொடர்ச்சியாகப் பொருந்தும்."}
        },
        "tnpsc_tip": {
            "en": "Democratic citizenship requires enjoying rights while simultaneously performing duties.",
            "ta": "ஜனநாயகக் குடியுரிமைக்கு உரிமைகளை அனுபவிக்கும் அதே வேளையில் கடமைகளையும் செய்வது அவசியம்."
        }
    },
    {
        "id": "FD_E_049",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Article-based",
        "question": {
            "en": "Striving towards excellence under Article 51A(j) applies to which two spheres of activity?",
            "ta": "உறுப்பு 51A(j)-ன் கீழ் சிறப்பினை நோக்கி முயலுதல் எந்த இரு பிரிவு செயல்பாடுகளுக்குப் பொருந்தும்?"
        },
        "options": [
            {"id": "A", "en": "Individual and Collective activity", "ta": "தனிநபர் மற்றும் கூட்டுச் செயல்பாடு"},
            {"id": "B", "en": "Political and Commercial activity", "ta": "அரசியல் மற்றும் வணிகச் செயல்பாடு"},
            {"id": "C", "en": "Judicial and Legislative activity", "ta": "நீதித்துறை மற்றும் சட்டமன்றச் செயல்பாடு"},
            {"id": "D", "en": "Domestic and Foreign activity", "ta": "உள்நாட்டு மற்றும் வெளிநாட்டுச் செயல்பாடு"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Article 51A(j) commands: 'To strive towards excellence in all spheres of INDIVIDUAL and COLLECTIVE activity...'",
            "ta": "உறுப்பு 51A(j) ஆணையிடுகிறது: 'தனிநபர் மற்றும் கூட்டுச் செயல்பாடுகளின் அனைத்துத் துறைகளிலும் சிறப்பினை நோக்கி முயலுதல்...'"
        },
        "why_not_others": {
            "A": {"en": "Correct. Individual and Collective activity are the 2 specified spheres.", "ta": "சரி. தனிநபர் மற்றும் கூட்டுச் செயல்பாடு 2 குறிப்பிட்ட பிரிவுகள்."},
            "B": {"en": "Incorrect categories.", "ta": "தவறான பிரிவுகள்."},
            "C": {"en": "Relates to branches of government.", "ta": "அரசாங்கத்தின் கிளைகள் பற்றியது."},
            "D": {"en": "Incorrect categories.", "ta": "தவறான பிரிவுகள்."}
        },
        "tnpsc_tip": {
            "en": "Individual excellence = personal achievements; Collective excellence = teamwork & organizational progress.",
            "ta": "தனிநபர் சிறப்பு = தனிநபர் சாதனைகள்; கூட்டுச் சிறப்பு = குழுப்பணி & நிறுவன முன்னேற்றம்."
        }
    },
    {
        "id": "FD_E_050",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Amendment-based",
        "question": {
            "en": "The 86th Constitutional Amendment Act, 2002 made simultaneous amendments related to education across which three Parts of the Constitution?",
            "ta": "86வது அரசியலமைப்பு திருத்தச் சட்டம், 2002 கல்வி தொடர்பான ஒரே நேரத்திலான திருத்தங்களை அரசியலமைப்பின் எந்த மூன்று பகுதிகளில் செய்தது?"
        },
        "options": [
            {"id": "A", "en": "Part I, Part II, and Part III", "ta": "பகுதி I, பகுதி II, மற்றும் பகுதி III"},
            {"id": "B", "en": "Part V, Part VI, and Part VII", "ta": "பகுதி V, பகுதி VI, மற்றும் பகுதி VII"},
            {"id": "C", "en": "Part IX, Part IXA, and Part IXB", "ta": "பகுதி IX, பகுதி IXA, மற்றும் பகுதி IXB"},
            {"id": "D", "en": "Part III (Art 21A), Part IV (Art 45), and Part IVA (Art 51A(k))", "ta": "பகுதி III (உறுப்பு 21A), பகுதி IV (உறுப்பு 45), மற்றும் பகுதி IVA (உறுப்பு 51A(k))"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "The 86th CAA 2002 simultaneously inserted Art 21A in Part III (FR), modified Art 45 in Part IV (DPSP), and inserted Art 51A(k) in Part IVA (FD).",
            "ta": "86வது திருத்தம் 2002 ஒரே நேரத்தில் பகுதி III-ல் உறுப்பு 21A (FR) ஐச் சேர்த்தது, பகுதி IV-ல் உறுப்பு 45 (DPSP) ஐ மாற்றியது, மற்றும் பகுதி IVA-ல் உறுப்பு 51A(k) (FD) ஐச் சேர்த்தது."
        },
        "why_not_others": {
            "A": {"en": "Part I deals with Territory, Part II with Citizenship.", "ta": "பகுதி I நிலப்பரப்பு, பகுதி II குடியுரிமை பற்றியது."},
            "B": {"en": "Deals with Union, States, and repealed Part B states.", "ta": "ஒன்றியம், மாநிலங்கள் பற்றியது."},
            "C": {"en": "Deals with Panchayats, Municipalities, and Co-operative societies.", "ta": "பஞ்சாயத்துகள், நகராட்சிகள், கூட்டுறவுச் சங்கங்கள் பற்றியது."},
            "D": {"en": "Correct. Part III (Art 21A), Part IV (Art 45), and Part IVA (Art 51A(k)).", "ta": "சரி. பகுதி III (உறுப்பு 21A), பகுதி IV (உறுப்பு 45), மற்றும் பகுதி IVA (உறுப்பு 51A(k))."}
        },
        "tnpsc_tip": {
            "en": "Remember the tripartite educational amendments of the 86th CAA 2002!",
            "ta": "86வது திருத்தச் சட்டம் 2002-ன் மூன்று தரப்பு கல்வித் திருத்தங்களை நினைவில் கொள்க!"
        }
    }
]

target_file = "data/questions/polity/fundamental_duties_easy.json"
os.makedirs(os.path.dirname(target_file), exist_ok=True)

with open(target_file, "w", encoding="utf-8") as f:
    json.dump(questions_data, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {len(questions_data)} Easy questions in {target_file}")
