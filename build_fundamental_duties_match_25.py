# -*- coding: utf-8 -*-
"""
Script to build 25 High-Yield Match the Following MCQs for Fundamental Duties
Target Files:
  - data/questions/polity/fundamental_duties_match.json
  - data/questions/polity/fundamental_duties_match_the_following.json
"""

import json
import os

questions_data = [
    {
        "id": "FD_MTH_001",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Match the Following",
        "question": {
            "en": "Match List I (Article 51A Clauses a to d) with List II (Fundamental Duty Provisions) and select the correct code:",
            "ta": "பட்டியல் I-ஐ (உறுப்பு 51A பிரிவுகள் a முதல் d வரை) பட்டியல் II உடன் (அடிப்படை கடமை விதிகள்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:"
        },
        "list_1": [
            {"id": "A", "en": "Article 51A(a)", "ta": "உறுப்பு 51A(a)"},
            {"id": "B", "en": "Article 51A(b)", "ta": "உறுப்பு 51A(b)"},
            {"id": "C", "en": "Article 51A(c)", "ta": "உறுப்பு 51A(c)"},
            {"id": "D", "en": "Article 51A(d)", "ta": "உறுப்பு 51A(d)"}
        ],
        "list_2": [
            {"id": "1", "en": "Abide by Constitution, National Flag & Anthem", "ta": "அரசியலமைப்பு, தேசியக் கொடி & கீதத்திற்குப் பணிதல்"},
            {"id": "2", "en": "Cherish noble ideals of freedom struggle", "ta": "சுதந்திரப் போராட்டத்தின் உயரிய லட்சியங்களைப் போற்றுதல்"},
            {"id": "3", "en": "Uphold sovereignty, unity & integrity of India", "ta": "இந்தியாவின் இறையாண்மை, ஒற்றுமை & ஒருமைப்பாட்டைப் பேணுதல்"},
            {"id": "4", "en": "Defend country and render national service", "ta": "தேசத்தைப் பாதுகாத்தல் & தேசியச் சேவை ஆற்றுதல்"}
        ],
        "options": [
            {"id": "A", "en": "A-1, B-2, C-3, D-4", "ta": "A-1, B-2, C-3, D-4"},
            {"id": "B", "en": "A-2, B-1, C-4, D-3", "ta": "A-2, B-1, C-4, D-3"},
            {"id": "C", "en": "A-3, B-4, C-1, D-2", "ta": "A-3, B-4, C-1, D-2"},
            {"id": "D", "en": "A-4, B-3, C-2, D-1", "ta": "A-4, B-3, C-2, D-1"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "A-1: Art 51A(a) covers Constitution, Flag & Anthem. B-2: Art 51A(b) covers freedom struggle ideals. C-3: Art 51A(c) covers sovereignty, unity & integrity. D-4: Art 51A(d) covers national defense & service.",
            "ta": "A-1: உறுப்பு 51A(a) அரசியலமைப்பு, கொடி & கீதத்தை உள்ளடக்கியது. B-2: உறுப்பு 51A(b) சுதந்திரப் போராட்ட லட்சியங்களை உள்ளடக்கியது. C-3: உறுப்பு 51A(c) இறையாண்மை, ஒற்றுமை & ஒருமைப்பாட்டை உள்ளடக்கியது. D-4: உறுப்பு 51A(d) தேசிய பாதுகாப்பு & சேவையை உள்ளடக்கியது."
        },
        "why_not_others": {
            "A": {"en": "Correct matching sequence.", "ta": "சரியான பொருத்தும் வரிசை."},
            "B": {"en": "Incorrect. Article 51A(a) matches 1, not 2.", "ta": "தவறு. உறுப்பு 51A(a) பொருத்தம் 1 ஆகும்."},
            "C": {"en": "Incorrect. Article 51A(a) matches 1, not 3.", "ta": "தவறு. உறுப்பு 51A(a) பொருத்தம் 1 ஆகும்."},
            "D": {"en": "Incorrect. Article 51A(a) matches 1, not 4.", "ta": "தவறு. உறுப்பு 51A(a) பொருத்தம் 1 ஆகும்."}
        },
        "tnpsc_tip": {
            "en": "Art 51A(a) to 51A(d) form the core national loyalty obligations.",
            "ta": "உறுப்பு 51A(a) முதல் 51A(d) வரை தேசிய விசுவாசத்தின் முக்கியக் கடமைகளாகும்."
        }
    },
    {
        "id": "FD_MTH_002",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Match the Following",
        "question": {
            "en": "Match List I (Article 51A Clauses e to h) with List II (Specific Fundamental Duty Text) and select the correct code:",
            "ta": "பட்டியல் I-ஐ (உறுப்பு 51A பிரிவுகள் e முதல் h வரை) பட்டியல் II உடன் (குறிப்பிட்ட அடிப்படை கடமை உரை) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:"
        },
        "list_1": [
            {"id": "A", "en": "Article 51A(e)", "ta": "உறுப்பு 51A(e)"},
            {"id": "B", "en": "Article 51A(f)", "ta": "உறுப்பு 51A(f)"},
            {"id": "C", "en": "Article 51A(g)", "ta": "உறுப்பு 51A(g)"},
            {"id": "D", "en": "Article 51A(h)", "ta": "உறுப்பு 51A(h)"}
        ],
        "list_2": [
            {"id": "1", "en": "Promote harmony & renounce practices derogatory to women", "ta": "நல்லிணக்கத்தை ஊக்குவித்தல் & பெண்கள் கண்ணியத்தைக் குறைக்கும் பழக்கங்களைக் கைவிடுதல்"},
            {"id": "2", "en": "Value & preserve rich heritage of composite culture", "ta": "கூட்டுப் பண்பாட்டின் வளமான பாரம்பரியத்தை மதித்துப் பேணுதல்"},
            {"id": "3", "en": "Protect & improve natural environment & compassion for living creatures", "ta": "இயற்கை சுற்றுச்சூழலைப் பாதுகாத்து மேம்படுத்தல் & உயிரினங்கள் மீது கருணை"},
            {"id": "4", "en": "Develop scientific temper, humanism, inquiry & reform", "ta": "அறிவியல் மனப்பான்மை, மனிதநேயம், ஆராய்ச்சி & சீர்திருத்தத்தை வளர்த்தல்"}
        ],
        "options": [
            {"id": "A", "en": "A-2, B-1, C-3, D-4", "ta": "A-2, B-1, C-4, D-3"},
            {"id": "B", "en": "A-1, B-2, C-3, D-4", "ta": "A-1, B-2, C-3, D-4"},
            {"id": "C", "en": "A-3, B-4, C-1, D-2", "ta": "A-3, B-4, C-1, D-2"},
            {"id": "D", "en": "A-4, B-3, C-2, D-1", "ta": "A-4, B-3, C-2, D-1"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "A-1: Art 51A(e) covers harmony & women's dignity. B-2: Art 51A(f) covers composite culture. C-3: Art 51A(g) covers environment & compassion. D-4: Art 51A(h) covers scientific temper.",
            "ta": "A-1: உறுப்பு 51A(e) நல்லிணக்கம் & பெண்கள் கண்ணியத்தை உள்ளடக்கியது. B-2: உறுப்பு 51A(f) கூட்டுப் பண்பாட்டை உள்ளடக்கியது. C-3: உறுப்பு 51A(g) சுற்றுச்சூழல் & கருணையை உள்ளடக்கியது. D-4: உறுப்பு 51A(h) அறிவியல் மனப்பான்மையை உள்ளடக்கியது."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Article 51A(e) matches 1, not 2.", "ta": "தவறு. உறுப்பு 51A(e) பொருத்தம் 1 ஆகும்."},
            "B": {"en": "Correct matching sequence.", "ta": "சரியான பொருத்தும் வரிசை."},
            "C": {"en": "Incorrect. Article 51A(e) matches 1, not 3.", "ta": "தவறு. உறுப்பு 51A(e) பொருத்தம் 1 ஆகும்."},
            "D": {"en": "Incorrect. Article 51A(e) matches 1, not 4.", "ta": "தவறு. உறுப்பு 51A(e) பொருத்தம் 1 ஆகும்."}
        },
        "tnpsc_tip": {
            "en": "Art 51A(e) explicitly pairs common brotherhood with women's dignity.",
            "ta": "உறுப்பு 51A(e) சகோதரத்துவத்தை வெளிப்படையாகப் பெண்களின் கண்ணியத்துடன் இணைக்கிறது."
        }
    },
    {
        "id": "FD_MTH_003",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Easy",
        "question_type": "Match the Following",
        "question": {
            "en": "Match List I (Article 51A Clauses i, j, k, a) with List II (Core Civic Duty Focus) and select the correct code:",
            "ta": "பட்டியல் I-ஐ (உறுப்பு 51A பிரிவுகள் i, j, k, a) பட்டியல் II உடன் (முக்கியக் குடிமை கடமை மையம்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:"
        },
        "list_1": [
            {"id": "A", "en": "Article 51A(i)", "ta": "உறுப்பு 51A(i)"},
            {"id": "B", "en": "Article 51A(j)", "ta": "உறுப்பு 51A(j)"},
            {"id": "C", "en": "Article 51A(k)", "ta": "உறுப்பு 51A(k)"},
            {"id": "D", "en": "Article 51A(a)", "ta": "உறுப்பு 51A(a)"}
        ],
        "list_2": [
            {"id": "1", "en": "Safeguard public property & abjure violence", "ta": "பொதுச் சொத்தைப் பாதுகாத்தல் & வன்முறையைக் கைவிடுதல்"},
            {"id": "2", "en": "Strive towards excellence in all individual & collective spheres", "ta": "தனிநபர் & கூட்டுச் செயல்பாடுகளில் சிறப்பினை நோக்கி முயலுதல்"},
            {"id": "3", "en": "Parent/guardian duty for child education (6-14 years)", "ta": "குழந்தைக் கல்விக்கான பெற்றோர்/பாதுகாவலர் கடமை (6-14 வயது)"},
            {"id": "4", "en": "Abide by Constitution, Flag & Anthem", "ta": "அரசியலமைப்பு, கொடி & கீதத்திற்குப் பணிதல்"}
        ],
        "options": [
            {"id": "A", "en": "A-2, B-1, C-4, D-3", "ta": "A-2, B-1, C-4, D-3"},
            {"id": "B", "en": "A-4, B-3, C-2, D-1", "ta": "A-4, B-3, C-2, D-1"},
            {"id": "C", "en": "A-1, B-2, C-3, D-4", "ta": "A-1, B-2, C-3, D-4"},
            {"id": "D", "en": "A-3, B-4, C-1, D-2", "ta": "A-3, B-4, C-1, D-2"}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "A-1: Art 51A(i) covers public property. B-2: Art 51A(j) covers excellence. C-3: Art 51A(k) covers child education duty (added 2002). D-4: Art 51A(a) covers Constitution & symbols.",
            "ta": "A-1: உறுப்பு 51A(i) பொதுச் சொத்தை உள்ளடக்கியது. B-2: உறுப்பு 51A(j) சிறப்பினை உள்ளடக்கியது. C-3: உறுப்பு 51A(k) குழந்தைக் கல்விக் கடமையை உள்ளடக்கியது (2002-ல் சேர்க்கப்பட்டது). D-4: உறுப்பு 51A(a) அரசியலமைப்பு & சின்னங்களை உள்ளடக்கியது."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Article 51A(i) matches 1, not 2.", "ta": "தவறு. உறுப்பு 51A(i) பொருத்தம் 1 ஆகும்."},
            "B": {"en": "Incorrect. Article 51A(i) matches 1, not 4.", "ta": "தவறு. உறுப்பு 51A(i) பொருத்தம் 1 ஆகும்."},
            "C": {"en": "Correct matching sequence.", "ta": "சரியான பொருத்தும் வரிசை."},
            "D": {"en": "Incorrect. Article 51A(i) matches 1, not 3.", "ta": "தவறு. உறுப்பு 51A(i) பொருத்தம் 1 ஆகும்."}
        },
        "tnpsc_tip": {
            "en": "Art 51A(k) was added by the 86th CAA, 2002.",
            "ta": "உறுப்பு 51A(k) 2002-ன் 86வது திருத்தத்தால் சேர்க்கப்பட்டது."
        }
    },
    {
        "id": "FD_MTH_004",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Match the Following",
        "question": {
            "en": "Match List I (Selected Duty Clauses g, h, e, c) with List II (Key Constitutional Term) and select the correct code:",
            "ta": "பட்டியல் I-ஐ (தேர்ந்தெடுக்கப்பட்ட கடமைப் பிரிவுகள் g, h, e, c) பட்டியல் II உடன் (முக்கிய அரசியலமைப்புச் சொல்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:"
        },
        "list_1": [
            {"id": "A", "en": "Article 51A(g)", "ta": "உறுப்பு 51A(g)"},
            {"id": "B", "en": "Article 51A(h)", "ta": "உறுப்பு 51A(h)"},
            {"id": "C", "en": "Article 51A(e)", "ta": "உறுப்பு 51A(e)"},
            {"id": "D", "en": "Article 51A(c)", "ta": "உறுப்பு 51A(c)"}
        ],
        "list_2": [
            {"id": "1", "en": "Compassion for living creatures", "ta": "உயிரினங்கள் மீது கருணை"},
            {"id": "2", "en": "Spirit of inquiry and reform", "ta": "ஆராய்ச்சி மற்றும் சீர்திருத்த உணர்வு"},
            {"id": "3", "en": "Renounce practices derogatory to dignity of women", "ta": "பெண்கள் கண்ணியத்தைக் குறைக்கும் பழக்கங்களைக் கைவிடுதல்"},
            {"id": "4", "en": "Sovereignty, unity and integrity", "ta": "இறையாண்மை, ஒற்றுமை மற்றும் ஒருமைப்பாடு"}
        ],
        "options": [
            {"id": "A", "en": "A-2, B-1, C-4, D-3", "ta": "A-2, B-1, C-4, D-3"},
            {"id": "B", "en": "A-3, B-4, C-1, D-2", "ta": "A-3, B-4, C-1, D-2"},
            {"id": "C", "en": "A-4, B-3, C-2, D-1", "ta": "A-4, B-3, C-2, D-1"},
            {"id": "D", "en": "A-1, B-2, C-3, D-4", "ta": "A-1, B-2, C-3, D-4"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "A-1: Art 51A(g) contains compassion. B-2: Art 51A(h) contains spirit of inquiry. C-3: Art 51A(e) contains women's dignity. D-4: Art 51A(c) contains sovereignty, unity, integrity.",
            "ta": "A-1: உறுப்பு 51A(g) கருணையைக் கொண்டுள்ளது. B-2: உறுப்பு 51A(h) ஆராய்ச்சி உணர்வைக் கொண்டுள்ளது. C-3: உறுப்பு 51A(e) பெண்கள் கண்ணியத்தைக் கொண்டுள்ளது. D-4: உறுப்பு 51A(c) இறையாண்மை, ஒற்றுமை, ஒருமைப்பாட்டைக் கொண்டுள்ளது."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Article 51A(g) matches 1, not 2.", "ta": "தவறு. உறுப்பு 51A(g) பொருத்தம் 1 ஆகும்."},
            "B": {"en": "Incorrect. Article 51A(g) matches 1, not 3.", "ta": "தவறு. உறுப்பு 51A(g) பொருத்தம் 1 ஆகும்."},
            "C": {"en": "Incorrect. Article 51A(g) matches 1, not 4.", "ta": "தவறு. உறுப்பு 51A(g) பொருத்தம் 1 ஆகும்."},
            "D": {"en": "Correct matching sequence.", "ta": "சரியான பொருத்தும் வரிசை."}
        },
        "tnpsc_tip": {
            "en": "Pay close attention to key terms like 'compassion' (51A(g)) vs 'humanism' (51A(h)).",
            "ta": "'கருணை' (51A(g)) vs 'மனிதநேயம்' (51A(h)) போன்ற முக்கிய சொற்களைக் கவனிக்கவும்."
        }
    },
    {
        "id": "FD_MTH_005",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Match the Following",
        "question": {
            "en": "Match List I (Constitutional Amendment Act) with List II (Key Modification in Duties Framework) and select the correct code:",
            "ta": "பட்டியல் I-ஐ (அரசியலமைப்பு திருத்தச் சட்டம்) பட்டியல் II உடன் (கடமை கட்டமைப்பில் முக்கிய மாற்றம்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:"
        },
        "list_1": [
            {"id": "A", "en": "42nd CAA, 1976", "ta": "42வது திருத்தம், 1976"},
            {"id": "B", "en": "86th CAA, 2002", "ta": "86வது திருத்தம், 2002"},
            {"id": "C", "en": "16th CAA, 1963", "ta": "16வது திருத்தம், 1963"},
            {"id": "D", "en": "44th CAA, 1978", "ta": "44வது திருத்தம், 1978"}
        ],
        "list_2": [
            {"id": "1", "en": "Inserted Part IVA containing 10 Fundamental Duties", "ta": "10 அடிப்படை கடமைகளைக் கொண்ட பகுதி IVA-ஐச் சேர்த்தது"},
            {"id": "2", "en": "Added 11th Fundamental Duty [Article 51A(k)]", "ta": "11வது அடிப்படை கடமையைச் சேர்த்தது [உறுப்பு 51A(k)]"},
            {"id": "3", "en": "Added 'sovereignty and integrity' to Article 19(2)", "ta": "உறுப்பு 19(2)-ல் 'இறையாண்மை மற்றும் ஒருமைப்பாடு' என்பதைச் சேர்த்தது"},
            {"id": "4", "en": "Restored civil liberties post-Emergency while retaining Part IVA", "ta": "பகுதி IVA-ஐத் தக்கவைத்து அவசரநிலைக்குப் பிந்தைய உரிமைகளை மீட்டெடுத்தது"}
        ],
        "options": [
            {"id": "A", "en": "A-1, B-2, C-3, D-4", "ta": "A-1, B-2, C-3, D-4"},
            {"id": "B", "en": "A-2, B-1, C-4, D-3", "ta": "A-2, B-1, C-4, D-3"},
            {"id": "C", "en": "A-3, B-4, C-1, D-2", "ta": "A-3, B-4, C-1, D-2"},
            {"id": "D", "en": "A-4, B-3, C-2, D-1", "ta": "A-4, B-3, C-2, D-1"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "A-1: 42nd CAA added Part IVA (10 duties). B-2: 86th CAA added 11th duty. C-3: 16th CAA added integrity to Art 19(2). D-4: 44th CAA retained Part IVA while removing 42nd CAA excesses.",
            "ta": "A-1: 42வது திருத்தம் பகுதி IVA (10 கடமைகள்) சேர்த்தது. B-2: 86வது திருத்தம் 11வது கடமையைச் சேர்த்தது. C-3: 16வது திருத்தம் உறுப்பு 19(2)-ல் ஒருமைப்பாட்டைச் சேர்த்தது. D-4: 44வது திருத்தம் பகுதி IVA-ஐத் தக்கவைத்தது."
        },
        "why_not_others": {
            "A": {"en": "Correct matching sequence.", "ta": "சரியான பொருத்தும் வரிசை."},
            "B": {"en": "Incorrect. 42nd CAA matches 1, not 2.", "ta": "தவறு. 42வது திருத்தம் பொருத்தம் 1 ஆகும்."},
            "C": {"en": "Incorrect. 42nd CAA matches 1, not 3.", "ta": "தவறு. 42வது திருத்தம் பொருத்தம் 1 ஆகும்."},
            "D": {"en": "Incorrect. 42nd CAA matches 1, not 4.", "ta": "தவறு. 42வது திருத்தம் பொருத்தம் 1 ஆகும்."}
        },
        "tnpsc_tip": {
            "en": "Note: Janata Govt in 44th CAA 1978 retained Part IVA introduced by 42nd CAA 1976.",
            "ta": "குறிப்பு: 44வது திருத்தம் 1978-ல் ஜனதா அரசு 42வது திருத்தம் சேர்த்த பகுதி IVA-ஐத் தக்கவைத்தது."
        }
    },
    {
        "id": "FD_MTH_006",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Match the Following",
        "question": {
            "en": "Match List I (Committee / Commission) with List II (Key Relation to Fundamental Duties) and select the correct code:",
            "ta": "பட்டியல் I-ஐ (குழு / ஆணையம்) பட்டியல் II உடன் (அடிப்படை கடமைகளுடனான தொடர்பு) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:"
        },
        "list_1": [
            {"id": "A", "en": "Sardar Swaran Singh Committee (1976)", "ta": "சர்தார் ஸ்வரன் சிங் குழு (1976)"},
            {"id": "B", "en": "Justice J.S. Verma Committee (1999)", "ta": "நீதிபதி ஜே.எஸ். வர்மா குழு (1999)"},
            {"id": "C", "en": "NCRWC (Venkatachaliah 2002)", "ta": "NCRWC (வெங்கடாசலையா 2002)"},
            {"id": "D", "en": "Sarkaria Commission (1988)", "ta": "சர்க்காரியா ஆணையம் (1988)"}
        ],
        "list_2": [
            {"id": "1", "en": "Recommended inclusion of 8 Fundamental Duties in Constitution", "ta": "அரசியலமைப்பில் 8 அடிப்படை கடமைகளைச் சேர்க்கப் பரிந்துரைத்தது"},
            {"id": "2", "en": "Identified existing statutory penal laws enforcing Fundamental Duties", "ta": "அடிப்படை கடமைகளை அமல்படுத்தும் நிலவும் சட்டப்பூர்வ குற்றவியல் சட்டங்களைக் கண்டறிந்தது"},
            {"id": "3", "en": "Recommended adding duty to vote and duty to pay taxes", "ta": "வாக்களிக்கும் கடமை & வரி செலுத்தும் கடமையைச் சேர்க்கப் பரிந்துரைத்தது"},
            {"id": "4", "en": "Reviewed Centre-State relations (outside Part IVA direct scope)", "ta": "மத்திய-மாநில உறவுகளை மறுஆய்வு செய்தது (பகுதி IVA வரம்பிற்கு வெளியே)"}
        ],
        "options": [
            {"id": "A", "en": "A-2, B-1, C-4, D-3", "ta": "A-2, B-1, C-4, D-3"},
            {"id": "B", "en": "A-1, B-2, C-3, D-4", "ta": "A-1, B-2, C-3, D-4"},
            {"id": "C", "en": "A-3, B-4, C-1, D-2", "ta": "A-3, B-4, C-1, D-2"},
            {"id": "D", "en": "A-4, B-3, C-2, D-1", "ta": "A-4, B-3, C-2, D-1"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "A-1: Swaran Singh Committee (1976) proposed 8 duties. B-2: Verma Committee (1999) mapped statutory penal backup. C-3: NCRWC (2002) proposed voting & tax duties. D-4: Sarkaria Commission reviewed Centre-State relations.",
            "ta": "A-1: ஸ்வரன் சிங் குழு (1976) 8 கடமைகளைப் பரிந்துரைத்தது. B-2: வர்மா குழு (1999) சட்டப்பூர்வக் குற்றவியல் ஆதரவை வரைபடமாக்கியது. C-3: NCRWC (2002) வாக்களிக்கும் & வரி செலுத்தும் கடமைகளைப் பரிந்துரைத்தது. D-4: சர்க்காரியா ஆணையம் மத்திய-மாநில உறவுகளை மறுஆய்வு செய்தது."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Swaran Singh Committee matches 1, not 2.", "ta": "தவறு. ஸ்வரன் சிங் குழு பொருத்தம் 1 ஆகும்."},
            "B": {"en": "Correct matching sequence.", "ta": "சரியான பொருத்தும் வரிசை."},
            "C": {"en": "Incorrect. Swaran Singh Committee matches 1, not 3.", "ta": "தவறு. ஸ்வரன் சிங் குழு பொருத்தம் 1 ஆகும்."},
            "D": {"en": "Incorrect. Swaran Singh Committee matches 1, not 4.", "ta": "தவறு. ஸ்வரன் சிங் குழு பொருத்தம் 1 ஆகும்."}
        },
        "tnpsc_tip": {
            "en": "Swaran Singh = Original recommendation (1976) | Verma = Legal mapping (1999).",
            "ta": "ஸ்வரன் சிங் = அசல் பரிந்துரை (1976) | வர்மா = சட்டப்பூர்வ வரைபடமாக்கம் (1999)."
        }
    },
    {
        "id": "FD_MTH_007",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Match the Following",
        "question": {
            "en": "Match List I (Duty Sub-clauses Grouping) with List II (Thematic Classification) and select the correct code:",
            "ta": "பட்டியல் I-ஐ (கடமை உட்பிரிவுகள் குழுவாக்கம்) பட்டியல் II உடன் (தலைப்பு வாரியான வகைப்பாடு) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:"
        },
        "list_1": [
            {"id": "A", "en": "Article 51A(a) & (c)", "ta": "உறுப்பு 51A(a) & (c)"},
            {"id": "B", "en": "Article 51A(e)", "ta": "உறுப்பு 51A(e)"},
            {"id": "C", "en": "Article 51A(f) & (g)", "ta": "உறுப்பு 51A(f) & (g)"},
            {"id": "D", "en": "Article 51A(h) & (i)", "ta": "உறுப்பு 51A(h) & (i)"}
        ],
        "list_2": [
            {"id": "1", "en": "National Loyalty & Sovereignty Protection", "ta": "தேசிய விசுவாசம் & இறையாண்மை பாதுகாப்பு"},
            {"id": "2", "en": "Social Harmony & Gender Justice", "ta": "சமூக நல்லிணக்கம் & பாலின நீதி"},
            {"id": "3", "en": "Cultural & Natural Heritage Preservation", "ta": "பண்பாட்டு & இயற்கை பாரம்பரிய பேணல்"},
            {"id": "4", "en": "Civic Responsibility & Rational Mindset", "ta": "குடிமைப் பொறுப்பு & பகுத்தறிவு மனநிலை"}
        ],
        "options": [
            {"id": "A", "en": "A-2, B-1, C-4, D-3", "ta": "A-2, B-1, C-4, D-3"},
            {"id": "B", "en": "A-3, B-4, C-1, D-2", "ta": "A-3, B-4, C-1, D-2"},
            {"id": "C", "en": "A-1, B-2, C-3, D-4", "ta": "A-1, B-2, C-3, D-4"},
            {"id": "D", "en": "A-4, B-3, C-2, D-1", "ta": "A-4, B-3, C-2, D-1"}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "A-1: Symbols & Sovereignty = National Loyalty. B-2: Brotherhood & Women = Social Harmony. C-3: Composite Culture & Environment = Heritage. D-4: Scientific Temper & Public Property = Civic Rationality.",
            "ta": "A-1: சின்னங்கள் & இறையாண்மை = தேசிய விசுவாசம். B-2: சகோதரத்துவம் & பெண்கள் = சமூக நல்லிணக்கம். C-3: கூட்டுப் பண்பாடு & சுற்றுச்சூழல் = பாரம்பரியம். D-4: அறிவியல் மனப்பான்மை & பொதுச் சொத்து = குடிமைப் பகுத்தறிவு."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Article 51A(a)&(c) matches 1, not 2.", "ta": "தவறு. உறுப்பு 51A(a)&(c) பொருத்தம் 1 ஆகும்."},
            "B": {"en": "Incorrect. Article 51A(a)&(c) matches 1, not 3.", "ta": "தவறு. உறுப்பு 51A(a)&(c) பொருத்தம் 1 ஆகும்."},
            "C": {"en": "Correct matching sequence.", "ta": "சரியான பொருத்தும் வரிசை."},
            "D": {"en": "Incorrect. Article 51A(a)&(c) matches 1, not 4.", "ta": "தவறு. உறுப்பு 51A(a)&(c) பொருத்தம் 1 ஆகும்."}
        },
        "tnpsc_tip": {
            "en": "Grouping duties by theme helps solve conceptual statement & match questions.",
            "ta": "தலைப்பு வாரியாக கடமைகளைக் குழுவாக்குவது கருத்துப் வினாக்களுக்கு எளிதில் விடையளிக்க உதவும்."
        }
    },
    {
        "id": "FD_MTH_008",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Match the Following",
        "question": {
            "en": "Match List I (Fundamental Duty Sub-clause) with List II (Corresponding Fundamental Right under Part III) and select the correct code:",
            "ta": "பட்டியல் I-ஐ (அடிப்படை கடமை உட்பிரிவு) பட்டியல் II உடன் (பகுதி III-ன் இணையான அடிப்படை உரிமை) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:"
        },
        "list_1": [
            {"id": "A", "en": "Article 51A(a)", "ta": "உறுப்பு 51A(a)"},
            {"id": "B", "en": "Article 51A(d)", "ta": "உறுப்பு 51A(d)"},
            {"id": "C", "en": "Article 51A(g)", "ta": "உறுப்பு 51A(g)"},
            {"id": "D", "en": "Article 51A(k)", "ta": "உறுப்பு 51A(k)"}
        ],
        "list_2": [
            {"id": "1", "en": "Article 19(1)(a) Freedom of Expression (Right to fly National Flag)", "ta": "உறுப்பு 19(1)(a) பேச்சு சுதந்திரம் (தேசியக் கொடி பறக்கவிடும் உரிமை)"},
            {"id": "2", "en": "Article 23(2) Compulsory service exception to Forced Labour", "ta": "உறுப்பு 23(2) கட்டாய வேலைக்கு எதிரான விலக்காகக் கட்டாய சேவை"},
            {"id": "3", "en": "Article 21 Right to Life (Wholesome environment judicial expansion)", "ta": "உறுப்பு 21 வாழும் உரிமை (ஆரோக்கியமான சுற்றுச்சூழல் விரிவாக்கம்)"},
            {"id": "4", "en": "Article 21A Right to Free & Compulsory Education (6-14 years)", "ta": "உறுப்பு 21A இலவச & கட்டாயக் கல்வி உரிமை (6-14 வயது)"}
        ],
        "options": [
            {"id": "A", "en": "A-2, B-1, C-4, D-3", "ta": "A-2, B-1, C-4, D-3"},
            {"id": "B", "en": "A-3, B-4, C-1, D-2", "ta": "A-3, B-4, C-1, D-2"},
            {"id": "C", "en": "A-4, B-3, C-2, D-1", "ta": "A-4, B-3, C-2, D-1"},
            {"id": "D", "en": "A-1, B-2, C-3, D-4", "ta": "A-1, B-2, C-3, D-4"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "A-1: Flag respect in 51A(a) correlates with Art 19(1)(a) expression (Naveen Jindal case). B-2: National defense in 51A(d) connects to Art 23(2). C-3: Environment duty in 51A(g) connects to Art 21 right to wholesome environment. D-4: Parent duty in 51A(k) connects to Art 21A right.",
            "ta": "A-1: 51A(a) கொடி மரியாதை உறுப்பு 19(1)(a) பேச்சு சுதந்திரத்துடன் இணைந்தது. B-2: 51A(d) தேசிய பாதுகாப்பு உறுப்பு 23(2) உடன் இணைந்தது. C-3: 51A(g) சுற்றுச்சூழல் கடமை உறுப்பு 21 உடன் இணைந்தது. D-4: 51A(k) பெற்றோர் கடமை உறுப்பு 21A உடன் இணைந்தது."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Article 51A(a) matches 1, not 2.", "ta": "தவறு. உறுப்பு 51A(a) பொருத்தம் 1 ஆகும்."},
            "B": {"en": "Incorrect. Article 51A(a) matches 1, not 3.", "ta": "தவறு. உறுப்பு 51A(a) பொருத்தம் 1 ஆகும்."},
            "C": {"en": "Incorrect. Article 51A(a) matches 1, not 4.", "ta": "தவறு. உறுப்பு 51A(a) பொருத்தம் 1 ஆகும்."},
            "D": {"en": "Correct matching sequence.", "ta": "சரியான பொருத்தும் வரிசை."}
        },
        "tnpsc_tip": {
            "en": "Part III Fundamental Rights and Part IVA Fundamental Duties are correlative and inseverable.",
            "ta": "பகுதி III அடிப்படை உரிமைகளும் பகுதி IVA அடிப்படை கடமைகளும் ஒன்றோடொன்று தொடர்புடையவை."
        }
    },
    {
        "id": "FD_MTH_009",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Match the Following",
        "question": {
            "en": "Match List I (Fundamental Duty Sub-clause) with List II (Corresponding DPSP Article under Part IV) and select the correct code:",
            "ta": "பட்டியல் I-ஐ (அடிப்படை கடமை உட்பிரிவு) பட்டியல் II உடன் (பகுதி IV-ன் இணையான DPSP உறுப்பு) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:"
        },
        "list_1": [
            {"id": "A", "en": "Article 51A(g)", "ta": "உறுப்பு 51A(g)"},
            {"id": "B", "en": "Article 51A(k)", "ta": "உறுப்பு 51A(k)"},
            {"id": "C", "en": "Article 51A(f)", "ta": "உறுப்பு 51A(f)"},
            {"id": "D", "en": "Article 51A(b)", "ta": "உறுப்பு 51A(b)"}
        ],
        "list_2": [
            {"id": "1", "en": "Article 48A Protection & Improvement of Environment", "ta": "உறுப்பு 48A சுற்றுச்சூழல் பாதுகாப்பு & மேம்பாடு"},
            {"id": "2", "en": "Article 45 Early Childhood Care (<6 years)", "ta": "உறுப்பு 45 முன்பருவக் குழந்தைகள் பராமரிப்பு (<6 வயது)"},
            {"id": "3", "en": "Article 49 Protection of Monuments & Objects of Artistic/Historic interest", "ta": "உறுப்பு 49 கலை/வரலாற்றுச் சின்னங்கள் & பொருட்கள் பாதுகாப்பு"},
            {"id": "4", "en": "Article 38 Social Order for Promotion of Welfare of People", "ta": "உறுப்பு 38 மக்கள் நலனை ஊக்குவிக்கும் சமூக ஒழுங்கு"}
        ],
        "options": [
            {"id": "A", "en": "A-1, B-2, C-3, D-4", "ta": "A-1, B-2, C-3, D-4"},
            {"id": "B", "en": "A-2, B-1, C-4, D-3", "ta": "A-2, B-1, C-4, D-3"},
            {"id": "C", "en": "A-3, B-4, C-1, D-2", "ta": "A-3, B-4, C-1, D-2"},
            {"id": "D", "en": "A-4, B-3, C-2, D-1", "ta": "A-4, B-3, C-2, D-1"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "A-1: Art 51A(g) citizen environment duty mirrors Art 48A state DPSP. B-2: Art 51A(k) parent duty (6-14 yrs) complements Art 45 DPSP (<6 yrs). C-3: Art 51A(f) culture duty complements Art 49 monument protection DPSP. D-4: Art 51A(b) freedom struggle ideals aligns with Art 38 welfare state values.",
            "ta": "A-1: 51A(g) குடிமகன் சுற்றுச்சூழல் கடமை உறுப்பு 48A அரசு DPSP-ஐ பிரதிபலிக்கிறது. B-2: 51A(k) பெற்றோர் கடமை உறுப்பு 45 DPSP-ஐ நிரப்புகிறது. C-3: 51A(f) பண்பாட்டுக் கடமை உறுப்பு 49 சின்னங்கள் பாதுகாப்பை நிரப்புகிறது. D-4: 51A(b) சுதந்திர லட்சியங்கள் உறுப்பு 38 நலன்புரி மதிப்புகளுடன் சீரமைகிறது."
        },
        "why_not_others": {
            "A": {"en": "Correct matching sequence.", "ta": "சரியான பொருத்தும் வரிசை."},
            "B": {"en": "Incorrect. Article 51A(g) matches 1, not 2.", "ta": "தவறு. உறுப்பு 51A(g) பொருத்தம் 1 ஆகும்."},
            "C": {"en": "Incorrect. Article 51A(g) matches 1, not 3.", "ta": "தவறு. உறுப்பு 51A(g) பொருத்தம் 1 ஆகும்."},
            "D": {"en": "Incorrect. Article 51A(g) matches 1, not 4.", "ta": "தவறு. உறுப்பு 51A(g) பொருத்தம் 1 ஆகும்."}
        },
        "tnpsc_tip": {
            "en": "Art 48A (DPSP) and Art 51A(g) (FD) were both added together by the 42nd CAA 1976.",
            "ta": "உறுப்பு 48A (DPSP) மற்றும் உறுப்பு 51A(g) (FD) ஆகிய இரண்டும் 1976-ன் 42வது திருத்தத்தால் ஒன்றாகச் சேர்க்கப்பட்டன."
        }
    },
    {
        "id": "FD_MTH_010",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Hard",
        "question_type": "Match the Following",
        "question": {
            "en": "Match List I (Landmark Supreme Court Case) with List II (Established Legal Ruling on Fundamental Duties) and select the correct code:",
            "ta": "பட்டியல் I-ஐ (முக்கிய உச்ச நீதிமன்ற வழக்கு) பட்டியல் II உடன் (அடிப்படை கடமைகள் பற்றிய சட்டத் தீர்ப்பு) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:"
        },
        "list_1": [
            {"id": "A", "en": "Bijoe Emmanuel v. State of Kerala (1986)", "ta": "பிஜோய் இம்மானுவேல் vs கேரளா மாநிலம் (1986)"},
            {"id": "B", "en": "Shyam Narayan Chouksey v. UOI (2018)", "ta": "ஷ்யாம் நாராயண் சௌக்சே vs இந்திய யூனியன் (2018)"},
            {"id": "C", "en": "AIIMS Students Union v. AIIMS (2002)", "ta": "AIIMS மாணவர் சங்கம் vs AIIMS (2002)"},
            {"id": "D", "en": "Aruna Roy v. Union of India (2002)", "ta": "அருணா ராய் vs இந்திய யூனியன் (2002)"}
        ],
        "list_2": [
            {"id": "1", "en": "Standing respectfully during National Anthem satisfies Art 51A(a); singing compulsory is not required", "ta": "தேசியக் கீதத்தின் போது மரியாதையுடன் நிற்பது உறுப்பு 51A(a)-ஐப் பூர்த்தி செய்கிறது; பாடுவது கட்டாயமில்லை"},
            {"id": "2", "en": "Playing National Anthem in cinema halls is optional, but proper respect under Art 51A(a) is mandatory whenever played", "ta": "திரையரங்குகளில் தேசியக் கீதம் இசைப்பது விருப்பத்தேர்வு, ஆனால் இசைக்கப்படும் போது 51A(a) மரியாதை கட்டாயம்"},
            {"id": "3", "en": "Duties under Art 51A(j) balance FRs; merit & excellence cannot be destroyed by excessive quota", "ta": "51A(j) கடமைகள் உரிமைகளைச் சமன் செய்கின்றன; தகுதி & சிறப்பு அதிகப்படியான ஒதுக்கீடால் அழிக்கப்படக்கூடாது"},
            {"id": "4", "en": "Value-based education promoting humanism & ethics under Art 51A(h) is consistent with secularism", "ta": "51A(h)-ன் கீழ் மனிதநேயம் & தர்மத்தை ஊக்குவிக்கும் மதிப்புக் கல்வி மதச்சார்பின்மைக்கு உடன்பாடானது"}
        ],
        "options": [
            {"id": "A", "en": "A-2, B-1, C-4, D-3", "ta": "A-2, B-1, C-4, D-3"},
            {"id": "B", "en": "A-1, B-2, C-3, D-4", "ta": "A-1, B-2, C-3, D-4"},
            {"id": "C", "en": "A-3, B-4, C-1, D-2", "ta": "A-3, B-4, C-1, D-2"},
            {"id": "D", "en": "A-4, B-3, C-2, D-1", "ta": "A-4, B-3, C-2, D-1"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "A-1: Bijoe Emmanuel protected silent standing under Art 51A(a). B-2: Shyam Narayan Chouksey made cinema anthem playing optional in 2018. C-3: AIIMS case used Art 51A(j) to strike down 33% institutional quota. D-4: Aruna Roy case upheld value education using Art 51A(h).",
            "ta": "A-1: பிஜோய் இம்மானுவேல் 51A(a)-ன் கீழ் அமைதியாக நிற்பதைப் பாதுகாத்தது. B-2: ஷ்யாம் நாராயண் சௌக்சே 2018-ல் திரையரங்க இசைப்பை விருப்பத்தேர்வாக்கியது. C-3: AIIMS வழக்கு 51A(j)-ஐப் பயன்படுத்தி 33% நிறுவன ஒதுக்கீட்டை ரத்து செய்தது. D-4: அருணா ராய் வழக்கு 51A(h)-ஐப் பயன்படுத்தி மதிப்புக் கல்வியை நிலைநிறுத்தியது."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Bijoe Emmanuel matches 1, not 2.", "ta": "தவறு. பிஜோய் இம்மானுவேல் பொருத்தம் 1 ஆகும்."},
            "B": {"en": "Correct matching sequence.", "ta": "சரியான பொருத்தும் வரிசை."},
            "C": {"en": "Incorrect. Bijoe Emmanuel matches 1, not 3.", "ta": "தவறு. பிஜோய் இம்மானுவேல் பொருத்தம் 1 ஆகும்."},
            "D": {"en": "Incorrect. Bijoe Emmanuel matches 1, not 4.", "ta": "தவறு. பிஜோய் இம்மானுவேல் பொருத்தம் 1 ஆகும்."}
        },
        "tnpsc_tip": {
            "en": "Remember case years: Bijoe Emmanuel (1986) | AIIMS (2002) | Aruna Roy (2002) | Chouksey (2018).",
            "ta": "வழக்கு ஆண்டுகளை நினைவில் கொள்க: பிஜோய் இம்மானுவேல் (1986) | AIIMS (2002) | அருணா ராய் (2002) | சௌக்சே (2018)."
        }
    },
    {
        "id": "FD_MTH_011",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Hard",
        "question_type": "Match the Following",
        "question": {
            "en": "Match List I (Landmark Judicial Ruling II) with List II (Specific Constitutional Integration of Article 51A) and select the correct code:",
            "ta": "பட்டியல் I-ஐ (முக்கிய நீதித்துறை தீர்ப்பு II) பட்டியல் II உடன் (உறுப்பு 51A-ன் குறிப்பிட்ட அரசியலமைப்பு இணைப்பு) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:"
        },
        "list_1": [
            {"id": "A", "en": "A. Nagaraja v. AWBI (2014)", "ta": "ஏ. நாகராஜா vs AWBI (2014)"},
            {"id": "B", "en": "Union of India v. Naveen Jindal (2004)", "ta": "இந்திய யூனியன் vs நவீன் ஜிண்டால் (2004)"},
            {"id": "C", "en": "Sachidanand Pandey v. State of W.B. (1987)", "ta": "சச்சிதானந்த் பாண்டே vs மேற்கு வங்காள மாநிலம் (1987)"},
            {"id": "D", "en": "Mohan Kumar Singhania v. UOI (1992)", "ta": "மோகன் குமார் சிங்கானியா vs இந்திய யூனியன் (1992)"}
        ],
        "list_2": [
            {"id": "1", "en": "Animal compassion duty under Art 51A(g) expands Art 21 Right to Life to animals", "ta": "51A(g) விலங்கு கருணைக் கடமை உறுப்பு 21 வாழும் உரிமையை விலங்குகளுக்கு விரிவாக்குகிறது"},
            {"id": "2", "en": "Right to fly National Flag under Art 19(1)(a) is bounded by Art 51A(a) duty of respect", "ta": "உறுப்பு 19(1)(a)-ன் கீழ் கொடி பறக்கவிடும் உரிமை உறுப்பு 51A(a) மரியாதைக் கடமைக்கு உட்பட்டது"},
            {"id": "3", "en": "Courts are duty-bound to examine ecological matters under Arts 48A & 51A(g)", "ta": "உறுப்புகள் 48A & 51A(g)-ன் கீழ் சுற்றுச்சூழல் விஷயங்களை ஆராய நீதிமன்றங்கள் கடமைப்பட்டுள்ளன"},
            {"id": "4", "en": "Civil service probation training regulations upheld under Art 51A(j) excellence", "ta": "அரசுப் பணிப் பயிற்சி விதிகளை உறுப்பு 51A(j) சிறப்பின் கீழ் நீதிமன்றம் நிலைநிறுத்தியது"}
        ],
        "options": [
            {"id": "A", "en": "A-2, B-1, C-4, D-3", "ta": "A-2, B-1, C-4, D-3"},
            {"id": "B", "en": "A-3, B-4, C-1, D-2", "ta": "A-3, B-4, C-1, D-2"},
            {"id": "C", "en": "A-1, B-2, C-3, D-4", "ta": "A-1, B-2, C-3, D-4"},
            {"id": "D", "en": "A-4, B-3, C-2, D-1", "ta": "A-4, B-3, C-2, D-1"}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "A-1: A. Nagaraja integrated animal rights with Art 51A(g) compassion. B-2: Naveen Jindal linked Flag flying to Art 19(1)(a) & 51A(a). C-3: Sachidanand Pandey enforced judicial review under Arts 48A & 51A(g). D-4: Mohan Kumar Singhania linked Art 51A(j) to civil service efficiency.",
            "ta": "A-1: ஏ. நாகராஜா விலங்கு உரிமைகளை 51A(g) கருணையுடன் இணைத்தது. B-2: நவீன் ஜிண்டால் கொடி பறக்கவிடுவதை 19(1)(a) & 51A(a) உடன் இணைத்தது. C-3: சச்சிதானந்த் பாண்டே 48A & 51A(g)-ன் கீழ் நீதித்துறை ஆய்வை அமல்படுத்தியது. D-4: மோகன் குமார் சிங்கானியா 51A(j)-ஐ அரசுப் பணித் திறனுடன் இணைத்தது."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. A. Nagaraja matches 1, not 2.", "ta": "தவறு. ஏ. நாகராஜா பொருத்தம் 1 ஆகும்."},
            "B": {"en": "Incorrect. A. Nagaraja matches 1, not 3.", "ta": "தவறு. ஏ. நாகராஜா பொருத்தம் 1 ஆகும்."},
            "C": {"en": "Correct matching sequence.", "ta": "சரியான பொருத்தும் வரிசை."},
            "D": {"en": "Incorrect. A. Nagaraja matches 1, not 4.", "ta": "தவறு. ஏ. நாகராஜா பொருத்தம் 1 ஆகும்."}
        },
        "tnpsc_tip": {
            "en": "A. Nagaraja (2014) is a landmark TNPSC case on animal welfare & Art 51A(g).",
            "ta": "ஏ. நாகராஜா (2014) விலங்கு நலன் & உறுப்பு 51A(g) பற்றிய முக்கிய டிஎன்பிஎஸ்சி வழக்காகும."
        }
    },
    {
        "id": "FD_MTH_012",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Match the Following",
        "question": {
            "en": "Match List I (Statutory Penal Law) with List II (Enforced Fundamental Duty) and select the correct code:",
            "ta": "பட்டியல் I-ஐ (சட்டப்பூர்வ குற்றவியல் சட்டம்) பட்டியல் II உடன் (அமல்படுத்தப்பட்ட அடிப்படை கடமை) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:"
        },
        "list_1": [
            {"id": "A", "en": "Prevention of Insults to National Honour Act, 1971", "ta": "தேசிய கௌரவ அவமதிப்பு தடுப்புச் சட்டம், 1971"},
            {"id": "B", "en": "Prevention of Damage to Public Property Act, 1984", "ta": "பொதுச் சொத்துச் சேதத் தடுப்புச் சட்டம், 1984"},
            {"id": "C", "en": "Wild Life (Protection) Act, 1972", "ta": "வனவிலங்கு (பாதுகாப்பு) சட்டம், 1972"},
            {"id": "D", "en": "Representation of the People Act, 1951", "ta": "மக்கள் பிரதிநிதித்துவச் சட்டம், 1951"}
        ],
        "list_2": [
            {"id": "1", "en": "Article 51A(a) Abide by Flag, Anthem & Constitution", "ta": "உறுப்பு 51A(a) கொடி, கீதம் & அரசியலமைப்புக்குக் கீழ்ப்படிதல்"},
            {"id": "2", "en": "Article 51A(i) Safeguard public property & abjure violence", "ta": "உறுப்பு 51A(i) பொதுச் சொத்தைப் பாதுகாத்தல் & வன்முறையைக் கைவிடுதல்"},
            {"id": "3", "en": "Article 51A(g) Protect environment, forests & wildlife", "ta": "உறுப்பு 51A(g) சுற்றுச்சூழல், காடுகள் & வனவிலங்குகளைப் பாதுகாத்தல்"},
            {"id": "4", "en": "Article 51A(c) & Electoral integrity (disqualifies candidates violating national honor)", "ta": "உறுப்பு 51A(c) & தேர்தல் ஒருமைப்பாடு (தேசிய கௌரவத்தை மீறுவோரைத் தகுதிநீக்கம் செய்தல்)"}
        ],
        "options": [
            {"id": "A", "en": "A-2, B-1, C-4, D-3", "ta": "A-2, B-1, C-4, D-3"},
            {"id": "B", "en": "A-3, B-4, C-1, D-2", "ta": "A-3, B-4, C-1, D-2"},
            {"id": "C", "en": "A-4, B-3, C-2, D-1", "ta": "A-4, B-3, C-2, D-1"},
            {"id": "D", "en": "A-1, B-2, C-3, D-4", "ta": "A-1, B-2, C-3, D-4"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "A-1: 1971 Act enforces Art 51A(a). B-2: 1984 Act enforces Art 51A(i). C-3: 1972 Act enforces Art 51A(g). D-4: RPA 1951 Section 8 disqualifies candidates violating National Symbols under Art 51A(a)/(c).",
            "ta": "A-1: 1971 சட்டம் உறுப்பு 51A(a)-ஐ அமல்படுத்துகிறது. B-2: 1984 சட்டம் உறுப்பு 51A(i)-ஐ அமல்படுத்துகிறது. C-3: 1972 சட்டம் உறுப்பு 51A(g)-ஐ அமல்படுத்துகிறது. D-4: RPA 1951 பிரிவு 8 51A(a)/(c) மீறுவோரைத் தகுதிநீக்கம் செய்கிறது."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. 1971 Act matches 1, not 2.", "ta": "தவறு. 1971 சட்டம் பொருத்தம் 1 ஆகும்."},
            "B": {"en": "Incorrect. 1971 Act matches 1, not 3.", "ta": "தவறு. 1971 சட்டம் பொருத்தம் 1 ஆகும்."},
            "C": {"en": "Incorrect. 1971 Act matches 1, not 4.", "ta": "தவறு. 1971 சட்டம் பொருத்தம் 1 ஆகும்."},
            "D": {"en": "Correct matching sequence.", "ta": "சரியான பொருத்தும் வரிசை."}
        },
        "tnpsc_tip": {
            "en": "Statutory penal backing is how non-justiciable Fundamental Duties gain legal enforcement.",
            "ta": "சட்டப்பூர்வ குற்றவியல் ஆதரவே அமல்படுத்த முடியாத கடமைகளுக்குச் சட்ட அமலாக்கத்தை வழங்குகிறது."
        }
    },
    {
        "id": "FD_MTH_013",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Match the Following",
        "question": {
            "en": "Match List I (86th CAA 2002 Educational Component) with List II (Constitutional Part & Provision) and select the correct code:",
            "ta": "பட்டியல் I-ஐ (86வது திருத்தம் 2002 கல்விக் கூறு) பட்டியல் II உடன் (அரசியலமைப்புப் பகுதி & விதி) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:"
        },
        "list_1": [
            {"id": "A", "en": "Article 21A", "ta": "உறுப்பு 21A"},
            {"id": "B", "en": "Article 45", "ta": "உறுப்பு 45"},
            {"id": "C", "en": "Article 51A(k)", "ta": "உறுப்பு 51A(k)"},
            {"id": "D", "en": "RTE Act, 2009", "ta": "RTE சட்டம், 2009"}
        ],
        "list_2": [
            {"id": "1", "en": "Part III Fundamental Right of Child (6-14 years)", "ta": "பகுதி III બાળக்கின் அடிப்படை உரிமை (6-14 வயது)"},
            {"id": "2", "en": "Part IV DPSP for Early Childhood Care (<6 years)", "ta": "பகுதி IV முன்பருவக் குழந்தைகள் பராமரிப்புக்கான DPSP (<6 வயது)"},
            {"id": "3", "en": "Part IVA Fundamental Duty of Parent/Guardian (6-14 years)", "ta": "பகுதி IVA பெற்றோர்/பாதுகாவலரின் அடிப்படை கடமை (6-14 வயது)"},
            {"id": "4", "en": "Statutory Act operationalizing Art 21A and Art 51A(k)", "ta": "உறுப்பு 21A & 51A(k)-ஐச் செயல்படுத்தும் சட்டப்பூர்வச் சட்டம்"}
        ],
        "options": [
            {"id": "A", "en": "A-1, B-2, C-3, D-4", "ta": "A-1, B-2, C-3, D-4"},
            {"id": "B", "en": "A-2, B-1, C-4, D-3", "ta": "A-2, B-1, C-4, D-3"},
            {"id": "C", "en": "A-3, B-4, C-1, D-2", "ta": "A-3, B-4, C-1, D-2"},
            {"id": "D", "en": "A-4, B-3, C-2, D-1", "ta": "A-4, B-3, C-2, D-1"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "A-1: Art 21A is Part III FR (6-14 yrs). B-2: Art 45 is Part IV DPSP (<6 yrs). C-3: Art 51A(k) is Part IVA FD (6-14 yrs). D-4: RTE Act 2009 gives statutory force to Arts 21A & 51A(k).",
            "ta": "A-1: உறுப்பு 21A பகுதி III FR (6-14 வயது). B-2: உறுப்பு 45 பகுதி IV DPSP (<6 வயது). C-3: உறுப்பு 51A(k) பகுதி IVA FD (6-14 வயது). D-4: RTE சட்டம் 2009 உறுப்புகள் 21A & 51A(k)-க்குச் சட்ட பலம் அளிக்கிறது."
        },
        "why_not_others": {
            "A": {"en": "Correct matching sequence.", "ta": "சரியான பொருத்தும் வரிசை."},
            "B": {"en": "Incorrect. Article 21A matches 1, not 2.", "ta": "தவறு. உறுப்பு 21A பொருத்தம் 1 ஆகும்."},
            "C": {"en": "Incorrect. Article 21A matches 1, not 3.", "ta": "தவறு. உறுப்பு 21A பொருத்தம் 1 ஆகும்."},
            "D": {"en": "Incorrect. Article 21A matches 1, not 4.", "ta": "தவறு. உறுப்பு 21A பொருத்தம் 1 ஆகும்."}
        },
        "tnpsc_tip": {
            "en": "The 86th CAA 2002 amended Part III, Part IV, and Part IVA simultaneously.",
            "ta": "86வது திருத்தம் 2002 ஒரே நேரத்தில் பகுதி III, பகுதி IV, மற்றும் பகுதி IVA ஆகியவற்றைத் திருத்தியது."
        }
    },
    {
        "id": "FD_MTH_014",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Hard",
        "question_type": "Match the Following",
        "question": {
            "en": "Match List I (Environmental Law Triad Component) with List II (Constitutional Nature & Function) and select the correct code:",
            "ta": "பட்டியல் I-ஐ (சுற்றுச்சூழல் சட்ட முக்கோணக் கூறு) பட்டியல் II உடன் (அரசியலமைப்பு இயல்பு & செயல்பாடு) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:"
        },
        "list_1": [
            {"id": "A", "en": "Article 21", "ta": "உறுப்பு 21"},
            {"id": "B", "en": "Article 48A", "ta": "உறுப்பு 48A"},
            {"id": "C", "en": "Article 51A(g)", "ta": "உறுப்பு 51A(g)"},
            {"id": "D", "en": "Environment (Protection) Act, 1986", "ta": "சுற்றுச்சூழல் (பாதுகாப்பு) சட்டம், 1986"}
        ],
        "list_2": [
            {"id": "1", "en": "Judicially declared Fundamental Right to a wholesome environment", "ta": "ஆரோக்கியமான சுற்றுச்சூழலுக்கான நீதித்துறை அறிவித்த அடிப்படை உரிமை"},
            {"id": "2", "en": "Directive Principle guiding State policy for environmental protection", "ta": "சுற்றுச்சூழல் பாதுகாப்பிற்கான அரசுக் கொள்கையை வழிகாட்டும் DPSP"},
            {"id": "3", "en": "Fundamental Duty binding every Citizen to protect environment & show compassion", "ta": "சுற்றுச்சூழலைப் பாதுகாக்கவும் கருணை காட்டவும் குடிமகனைக் கட்டுப்படுத்தும் கடமை"},
            {"id": "4", "en": "Statutory umbrella legislation providing penal enforcement for environmental duties", "ta": "சுற்றுச்சூழல் கடமைகளுக்குக் குற்றவியல் அமலாக்கம் வழங்கும் சட்டப்பூர்வக் குடைச் சட்டம்"}
        ],
        "options": [
            {"id": "A", "en": "A-2, B-1, C-4, D-3", "ta": "A-2, B-1, C-4, D-3"},
            {"id": "B", "en": "A-1, B-2, C-3, D-4", "ta": "A-1, B-2, C-3, D-4"},
            {"id": "C", "en": "A-3, B-4, C-1, D-2", "ta": "A-3, B-4, C-1, D-2"},
            {"id": "D", "en": "A-4, B-3, C-2, D-1", "ta": "A-4, B-3, C-2, D-1"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "A-1: Art 21 is FR right to clean environment. B-2: Art 48A is DPSP state directive. C-3: Art 51A(g) is citizen duty. D-4: EPA 1986 is umbrella statutory law.",
            "ta": "A-1: உறுப்பு 21 சுத்தமான சுற்றுச்சூழலுக்கான FR உரிமை. B-2: உறுப்பு 48A அரசு DPSP வழிகாட்டுதல். C-3: உறுப்பு 51A(g) குடிமகன் கடமை. D-4: EPA 1986 குடைச் சட்டப்பூர்வச் சட்டம்."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Article 21 matches 1, not 2.", "ta": "தவறு. உறுப்பு 21 பொருத்தம் 1 ஆகும்."},
            "B": {"en": "Correct matching sequence.", "ta": "சரியான பொருத்தும் வரிசை."},
            "C": {"en": "Incorrect. Article 21 matches 1, not 3.", "ta": "தவறு. உறுப்பு 21 பொருத்தம் 1 ஆகும்."},
            "D": {"en": "Incorrect. Article 21 matches 1, not 4.", "ta": "தவறு. உறுப்பு 21 பொருத்தம் 1 ஆகும்."}
        },
        "tnpsc_tip": {
            "en": "Arts 21, 48A, and 51A(g) form the SC's Environmental Law Triangle.",
            "ta": "உறுப்புகள் 21, 48A, மற்றும் 51A(g) ஆகியவை உச்ச நீதிமன்றத்தின் சுற்றுச்சூழல் சட்ட முக்கோணத்தை உருவாக்குகின்றன."
        }
    },
    {
        "id": "FD_MTH_015",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Match the Following",
        "question": {
            "en": "Match List I (Key Expression in Article 51A f, h, i, b) with List II (Sub-clause Identifier) and select the correct code:",
            "ta": "பட்டியல் I-ஐ (உறுப்பு 51A f, h, i, b-ல் உள்ள முக்கியச் சொல்) பட்டியல் II உடன் (உட்பிரிவு அடையாளம்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:"
        },
        "list_1": [
            {"id": "A", "en": "Composite Culture", "ta": "கூட்டுப் பண்பாடு"},
            {"id": "B", "en": "Scientific Temper & Humanism", "ta": "அறிவியல் மனப்பான்மை & மனிதநேயம்"},
            {"id": "C", "en": "Abjure Violence & Safeguard Public Property", "ta": "வன்முறையைக் கைவிடுதல் & பொதுச் சொத்தைப் பாதுகாத்தல்"},
            {"id": "D", "en": "Freedom Struggle Noble Ideals", "ta": "சுதந்திரப் போராட்ட உயரிய லட்சியங்கள்"}
        ],
        "list_2": [
            {"id": "1", "en": "Article 51A(f)", "ta": "உறுப்பு 51A(f)"},
            {"id": "2", "en": "Article 51A(h)", "ta": "உறுப்பு 51A(h)"},
            {"id": "3", "en": "Article 51A(i)", "ta": "உறுப்பு 51A(i)"},
            {"id": "4", "en": "Article 51A(b)", "ta": "உறுப்பு 51A(b)"}
        ],
        "options": [
            {"id": "A", "en": "A-2, B-1, C-4, D-3", "ta": "A-2, B-1, C-4, D-3"},
            {"id": "B", "en": "A-3, B-4, C-1, D-2", "ta": "A-3, B-4, C-1, D-2"},
            {"id": "C", "en": "A-1, B-2, C-3, D-4", "ta": "A-1, B-2, C-3, D-4"},
            {"id": "D", "en": "A-4, B-3, C-2, D-1", "ta": "A-4, B-3, C-2, D-1"}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "A-1: Composite culture is in 51A(f). B-2: Scientific temper & humanism are in 51A(h). C-3: Abjuring violence is in 51A(i). D-4: Freedom struggle ideals are in 51A(b).",
            "ta": "A-1: கூட்டுப் பண்பாடு 51A(f)-ல் உள்ளது. B-2: அறிவியல் மனப்பான்மை & மனிதநேயம் 51A(h)-ல் உள்ளன. C-3: வன்முறை துறப்பு 51A(i)-ல் உள்ளது. D-4: சுதந்திரப் போராட்ட லட்சியங்கள் 51A(b)-ல் உள்ளன."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Composite Culture matches 1, not 2.", "ta": "தவறு. கூட்டுப் பண்பாடு பொருத்தம் 1 ஆகும்."},
            "B": {"en": "Incorrect. Composite Culture matches 1, not 3.", "ta": "தவறு. கூட்டுப் பண்பாடு பொருத்தம் 1 ஆகும்."},
            "C": {"en": "Correct matching sequence.", "ta": "சரியான பொருத்தும் வரிசை."},
            "D": {"en": "Incorrect. Composite Culture matches 1, not 4.", "ta": "தவறு. கூட்டுப் பண்பாடு பொருத்தம் 1 ஆகும்."}
        },
        "tnpsc_tip": {
            "en": "Memorize the sub-clause alphabetical index: (f)=culture, (h)=science, (i)=property/non-violence.",
            "ta": "உட்பிரிவு வரிசையை மனனம் செய்க: (f)=பண்பாடு, (h)=அறிவியல், (i)=சொத்து/வன்முறை இன்மையாகும்."
        }
    },
    {
        "id": "FD_MTH_016",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Hard",
        "question_type": "Match the Following",
        "question": {
            "en": "Match List I (Duty Concept / Recommendation) with List II (Enactment / Recommendation Status) and select the correct code:",
            "ta": "பட்டியல் I-ஐ (கடமைக் கருத்து / பரிந்துரை) பட்டியல் II உடன் (இயற்றல் / பரிந்துரை நிலை) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:"
        },
        "list_1": [
            {"id": "A", "en": "Duty to Pay Taxes", "ta": "வரி செலுத்தும் கடமை"},
            {"id": "B", "en": "Duty to Vote in Elections", "ta": "தேர்தலில் வாக்களிக்கும் கடமை"},
            {"id": "C", "en": "Duty to Protect Environment & Compassion", "ta": "சுற்றுச்சூழலைப் பாதுகாக்கும் & கருணைக் கடமை"},
            {"id": "D", "en": "Duty of Parent for Child Education (6-14 yrs)", "ta": "குழந்தைக் கல்விக்கான பெற்றோர் கடமை (6-14 வயது)"}
        ],
        "list_2": [
            {"id": "1", "en": "Recommended by Swaran Singh Committee 1976 (NOT enacted into Art 51A)", "ta": "ஸ்வரன் சிங் குழு 1976 பரிந்துரைத்தது (உறுப்பு 51A-ல் இயற்றப்படவில்லை)"},
            {"id": "2", "en": "Recommended by NCRWC 2002 (NOT enacted into Art 51A)", "ta": "NCRWC 2002 பரிந்துரைத்தது (உறுப்பு 51A-ல் இயற்றப்படவில்லை)"},
            {"id": "3", "en": "Enacted into Constitution by 42nd CAA 1976 [Article 51A(g)]", "ta": "42வது திருத்தம் 1976 மூலம் அரசியலமைப்பில் இயற்றப்பட்டது [உறுப்பு 51A(g)]"},
            {"id": "4", "en": "Enacted into Constitution by 86th CAA 2002 [Article 51A(k)]", "ta": "86வது திருத்தம் 2002 மூலம் அரசியலமைப்பில் இயற்றப்பட்டது [உறுப்பு 51A(k)]"}
        ],
        "options": [
            {"id": "A", "en": "A-2, B-1, C-4, D-3", "ta": "A-2, B-1, C-4, D-3"},
            {"id": "B", "en": "A-3, B-4, C-1, D-2", "ta": "A-3, B-4, C-1, D-2"},
            {"id": "C", "en": "A-4, B-3, C-2, D-1", "ta": "A-4, B-3, C-2, D-1"},
            {"id": "D", "en": "A-1, B-2, C-3, D-4", "ta": "A-1, B-2, C-3, D-4"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "A-1: Tax duty was proposed by Swaran Singh but rejected by Parliament. B-2: Voting duty was proposed by NCRWC but not added. C-3: Environment duty was enacted in 1976 (51A(g)). D-4: Child education duty was enacted in 2002 (51A(k)).",
            "ta": "A-1: வரி கடமை ஸ்வரன் சிங்கால் முன்மொழியப்பட்டு நாடாளுமன்றத்தால் நிராகரிக்கப்பட்டது. B-2: வாக்களிக்கும் கடமை NCRWC ஆல் முன்மொழியப்பட்டுச் சேர்க்கப்படவில்லை. C-3: சுற்றுச்சூழல் கடமை 1976-ல் இயற்றப்பட்டது (51A(g)). D-4: குழந்தைக் கல்விக் கடமை 2002-ல் இயற்றப்பட்டது (51A(k))."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Duty to Pay Taxes matches 1, not 2.", "ta": "தவறு. வரி செலுத்தும் கடமை பொருத்தம் 1 ஆகும்."},
            "B": {"en": "Incorrect. Duty to Pay Taxes matches 1, not 3.", "ta": "தவறு. வரி செலுத்தும் கடமை பொருத்தம் 1 ஆகும்."},
            "C": {"en": "Incorrect. Duty to Pay Taxes matches 1, not 4.", "ta": "தவறு. வரி செலுத்தும் கடமை பொருத்தம் 1 ஆகும்."},
            "D": {"en": "Correct matching sequence.", "ta": "சரியான பொருத்தும் வரிசை."}
        },
        "tnpsc_tip": {
            "en": "TNPSC classic trap: Duty to pay taxes is NOT in Article 51A.",
            "ta": "டிஎன்பிஎஸ்சி பொறி: வரி செலுத்தும் கடமை உறுப்பு 51A-ல் இல்லை."
        }
    },
    {
        "id": "FD_MTH_017",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Match the Following",
        "question": {
            "en": "Match List I (Four Natural Elements in Article 51A(g)) with List II (Corresponding Environmental Domain) and select the correct code:",
            "ta": "பட்டியல் I-ஐ (உறுப்பு 51A(g)-ல் உள்ள நான்கு இயற்கை கூறுகள்) பட்டியல் II உடன் (இணையான சுற்றுச்சூழல் களம்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:"
        },
        "list_1": [
            {"id": "A", "en": "Forests", "ta": "காடுகள்"},
            {"id": "B", "en": "Lakes", "ta": "ஏரிகள்"},
            {"id": "C", "en": "Rivers", "ta": "ஆறுகள்"},
            {"id": "D", "en": "Wildlife", "ta": "வனவிலங்குகள்"}
        ],
        "list_2": [
            {"id": "1", "en": "Terrestrial flora & green cover preservation", "ta": "நிலவாழ் தாவரங்கள் & பசுமைப் பரப்பு பேணல்"},
            {"id": "2", "en": "Inland fresh waterbodies & wetland conservation", "ta": "உள்நாட்டு நன்னீர்நிலைகள் & சதுப்புநிலப் பாதுகாப்பு"},
            {"id": "3", "en": "Lotic riverine ecosystems & running water pollution control", "ta": "ஓடும் நதிச் சூழலமைப்புகள் & ஆற்று மாசு கட்டுப்பாடு"},
            {"id": "4", "en": "Wild fauna, animal species & biodiversity protection", "ta": "வன விலங்கினங்கள் & பல்லுயிர் பாதுகாப்பு"}
        ],
        "options": [
            {"id": "A", "en": "A-1, B-2, C-3, D-4", "ta": "A-1, B-2, C-3, D-4"},
            {"id": "B", "en": "A-2, B-1, C-4, D-3", "ta": "A-2, B-1, C-4, D-3"},
            {"id": "C", "en": "A-3, B-4, C-1, D-2", "ta": "A-3, B-4, C-1, D-2"},
            {"id": "D", "en": "A-4, B-3, C-2, D-1", "ta": "A-4, B-3, C-2, D-1"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "A-1: Forests = Green flora. B-2: Lakes = Inland waterbodies. C-3: Rivers = Riverine systems. D-4: Wildlife = Fauna protection. All four are explicitly listed in Article 51A(g).",
            "ta": "A-1: காடுகள் = பசுமைத் தாவரங்கள். B-2: ஏரிகள் = உள்நாட்டு நீர்நிலைகள். C-3: ஆறுகள் = நதி அமைப்புகள். D-4: வனவிலங்குகள் = விலங்கினப் பாதுகாப்பு. நான்கு கூறுகளும் 51A(g)-ல் வெளிப்படையாகப் பட்டியலிடப்பட்டுள்ளன."
        },
        "why_not_others": {
            "A": {"en": "Correct matching sequence.", "ta": "சரியான பொருத்தும் வரிசை."},
            "B": {"en": "Incorrect. Forests matches 1, not 2.", "ta": "தவறு. காடுகள் பொருத்தம் 1 ஆகும்."},
            "C": {"en": "Incorrect. Forests matches 1, not 3.", "ta": "தவறு. காடுகள் பொருத்தம் 1 ஆகும்."},
            "D": {"en": "Incorrect. Forests matches 1, not 4.", "ta": "தவறு. காடுகள் பொருத்தம் 1 ஆகும்."}
        },
        "tnpsc_tip": {
            "en": "Article 51A(g) explicitly names Forests, Lakes, Rivers, Wildlife + Compassion for living creatures.",
            "ta": "உறுப்பு 51A(g) காடுகள், ஏரிகள், ஆறுகள், வனவிலங்குகள் + உயிரினங்கள் மீது கருணையை வெளிப்படையாகக் குறிப்பிடுகிறது."
        }
    },
    {
        "id": "FD_MTH_018",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Match the Following",
        "question": {
            "en": "Match List I (Four Core Values of Article 51A(h)) with List II (Philosophical Definition) and select the correct code:",
            "ta": "பட்டியல் I-ஐ (உறுப்பு 51A(h)-ன் நான்கு முக்கிய மதிப்புகள்) பட்டியல் II உடன் (தத்துவ வரையறை) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:"
        },
        "list_1": [
            {"id": "A", "en": "Scientific Temper", "ta": "அறிவியல் மனப்பான்மை"},
            {"id": "B", "en": "Humanism", "ta": "மனிதநேயம்"},
            {"id": "C", "en": "Spirit of Inquiry", "ta": "ஆராய்ச்சி உணர்வு"},
            {"id": "D", "en": "Spirit of Reform", "ta": "சீர்திருத்த உணர்வு"}
        ],
        "list_2": [
            {"id": "1", "en": "Rational attitude questioning dogma, superstition & unverified claims", "ta": "கோட்பாடுகள், மூடநம்பிக்கை & சான்றற்றக் கூற்றுகளைக் கேள்வி கேட்கும் பகுத்தறிவு மனநிலை"},
            {"id": "2", "en": "Active value prioritizing human welfare, dignity & social justice", "ta": "மனித நலன், கண்ணியம் & சமூக நீதிக்கு முன்னுரிமை அளிக்கும் செயலில் உள்ள மதிப்பு"},
            {"id": "3", "en": "Scientific curiosity and desire to investigate truth through evidence", "ta": "ஆதாரங்கள் மூலம் உண்மையைக் கண்டறியும் அறிவியல் ஆர்வம்"},
            {"id": "4", "en": "Commitment to progressive social change and eradication of social evils", "ta": "முற்போக்கு சமூக மாற்றம் & சமூகக் தீமைகளை ஒழிப்பதற்கான அர்ப்பணிப்பு"}
        ],
        "options": [
            {"id": "A", "en": "A-2, B-1, C-4, D-3", "ta": "A-2, B-1, C-4, D-3"},
            {"id": "B", "en": "A-1, B-2, C-3, D-4", "ta": "A-1, B-2, C-3, D-4"},
            {"id": "C", "en": "A-3, B-4, C-1, D-2", "ta": "A-3, B-4, C-1, D-2"},
            {"id": "D", "en": "A-4, B-3, C-2, D-1", "ta": "A-4, B-3, C-2, D-1"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "A-1: Scientific temper = rational questioning. B-2: Humanism = human welfare & dignity. C-3: Inquiry = investigation of truth. D-4: Reform = progressive social change.",
            "ta": "A-1: அறிவியல் மனப்பான்மை = பகுத்தறிவு வினா. B-2: மனிதநேயம் = மனித நலன் & கண்ணியம். C-3: ஆராய்ச்சி = உண்மை ஆய்வு. D-4: சீர்திருத்தம் = முற்போக்கு சமூக மாற்றம்."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Scientific Temper matches 1, not 2.", "ta": "தவறு. அறிவியல் மனப்பான்மை பொருத்தம் 1 ஆகும்."},
            "B": {"en": "Correct matching sequence.", "ta": "சரியான பொருத்தும் வரிசை."},
            "C": {"en": "Incorrect. Scientific Temper matches 1, not 3.", "ta": "தவறு. அறிவியல் மனப்பான்மை பொருத்தம் 1 ஆகும்."},
            "D": {"en": "Incorrect. Scientific Temper matches 1, not 4.", "ta": "தவறு. அறிவியல் மனப்பான்மை பொருத்தம் 1 ஆகும்."}
        },
        "tnpsc_tip": {
            "en": "India is the ONLY Constitution in the world specifying 'Scientific Temper' as a fundamental duty.",
            "ta": "'அறிவியல் மனப்பான்மை'யை அடிப்படை கடமையாகக் குறிப்பிட்ட உலகிலேயே ஒரே அரசியலமைப்பு இந்தியா மட்டுமே."
        }
    },
    {
        "id": "FD_MTH_019",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Hard",
        "question_type": "Match the Following",
        "question": {
            "en": "Match List I (Constitutional Characteristic of Part IVA) with List II (Legal Feature Detail) and select the correct code:",
            "ta": "பட்டியல் I-ஐ (பகுதி IVA-ன் அரசியலமைப்பு இயல்பு) பட்டியல் II உடன் (சட்ட அம்ச விவரம்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:"
        },
        "list_1": [
            {"id": "A", "en": "Non-justiciability", "ta": "அமல்படுத்த முடியாத தன்மை"},
            {"id": "B", "en": "Exclusivity to Citizens", "ta": "குடிமக்களுக்கு மட்டுமே உரித்தானது"},
            {"id": "C", "en": "Operational during Emergency", "ta": "அவசரநிலையின் போதும் செயல்பாட்டில் இருப்பது"},
            {"id": "D", "en": "Amendment Procedure", "ta": "திருத்த முறை"}
        ],
        "list_2": [
            {"id": "1", "en": "No direct writ remedy lies for enforcement without enabling statute", "ta": "சட்டப்பூர்வச் சட்டமின்றி நேரடி பேராணைப் பரிகாரம் இல்லை"},
            {"id": "2", "en": "Binds Indian citizens only; does not extend to foreign nationals", "ta": "இந்தியக் குடிமக்களை மட்டுமே கட்டுப்படுத்தும்; வெளிநாட்டினருக்கு இல்லை"},
            {"id": "3", "en": "Part IVA duties are never suspended during Proclamation of Emergency under Art 352", "ta": "உறுப்பு 352 அவசரநிலையின் போது பகுதி IVA கடமைகள் ஒருபோதும் நிறுத்தப்படாது"},
            {"id": "4", "en": "Requires formal Constitutional Amendment under Article 368", "ta": "உறுப்பு 368-ன் கீழ் முறையான அரசியலமைப்பு திருத்தம் தேவை"}
        ],
        "options": [
            {"id": "A", "en": "A-2, B-1, C-4, D-3", "ta": "A-2, B-1, C-4, D-3"},
            {"id": "B", "en": "A-3, B-4, C-1, D-2", "ta": "A-3, B-4, C-1, D-2"},
            {"id": "C", "en": "A-1, B-2, C-3, D-4", "ta": "A-1, B-2, C-3, D-4"},
            {"id": "D", "en": "A-4, B-3, C-2, D-1", "ta": "A-4, B-3, C-2, D-1"}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "A-1: Non-justiciable = no direct writ. B-2: Exclusive = citizens only. C-3: Emergency = Part IVA never suspended. D-4: Amendment = Art 368 procedure required.",
            "ta": "A-1: அமல்படுத்த முடியாதவை = நேரடி பேராணை இல்லை. B-2: பிரத்யேகமானது = குடிமக்களுக்கு மட்டுமே. C-3: அவசரநிலை = பகுதி IVA நிறுத்தப்படாது. D-4: திருத்தம் = உறுப்பு 368 முறை தேவை."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Non-justiciability matches 1, not 2.", "ta": "தவறு. அமல்படுத்த முடியாத தன்மை பொருத்தம் 1 ஆகும்."},
            "B": {"en": "Incorrect. Non-justiciability matches 1, not 3.", "ta": "தவறு. அமல்படுத்த முடியாத தன்மை பொருத்தம் 1 ஆகும்."},
            "C": {"en": "Correct matching sequence.", "ta": "சரியான பொருத்தும் வரிசை."},
            "D": {"en": "Incorrect. Non-justiciability matches 1, not 4.", "ta": "தவறு. அமல்படுத்த முடியாத தன்மை பொருத்தம் 1 ஆகும்."}
        },
        "tnpsc_tip": {
            "en": "Emergency suspends Fundamental Rights against State; it NEVER suspends Fundamental Duties of Citizens.",
            "ta": "அவசரநிலை அரசுக்கு எதிரான உரிமைகளை நிறுத்துகிறது; ஆனால் குடிமக்கள் கடமைகளை ஒருபோதும் நிறுத்துவதில்லை."
        }
    },
    {
        "id": "FD_MTH_020",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Hard",
        "question_type": "Match the Following",
        "question": {
            "en": "Match List I (Supreme Court Landmark Ruling III) with List II (Enforced Article 51A Sub-clause) and select the correct code:",
            "ta": "பட்டியல் I-ஐ (உச்ச நீதிமன்ற வரலாற்றுத் தீர்ப்பு III) பட்டியல் II உடன் (அமல்படுத்தப்பட்ட உறுப்பு 51A உட்பிரிவு) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:"
        },
        "list_1": [
            {"id": "A", "en": "Bijoe Emmanuel (1986)", "ta": "பிஜோய் இம்மானுவேல் (1986)"},
            {"id": "B", "en": "Destruction of Public Properties Case (2009)", "ta": "பொதுச் சொத்துக்கள் சேத வழக்கு (2009)"},
            {"id": "C", "en": "A. Nagaraja Jallikattu Case (2014)", "ta": "ஏ. நாகராஜா ஜல்லிக்கட்டு வழக்கு (2014)"},
            {"id": "D", "en": "Mohan Kumar Singhania (1992)", "ta": "மோகன் குமார் சிங்கானியா (1992)"}
        ],
        "list_2": [
            {"id": "1", "en": "Article 51A(a) Respect for National Anthem", "ta": "உறுப்பு 51A(a) தேசியக் கீதத்திற்கு மரியாதை"},
            {"id": "2", "en": "Article 51A(i) Safeguard public property & abjure violence", "ta": "உறுப்பு 51A(i) பொதுச் சொத்தைப் பாதுகாத்தல் & வன்முறையைக் கைவிடுதல்"},
            {"id": "3", "en": "Article 51A(g) Compassion for living creatures", "ta": "உறுப்பு 51A(g) உயிரினங்கள் மீது கருணை"},
            {"id": "4", "en": "Article 51A(j) Striving towards excellence in public service", "ta": "உறுப்பு 51A(j) பொதுப் பணியில் சிறப்பினை நோக்கி முயலுதல்"}
        ],
        "options": [
            {"id": "A", "en": "A-2, B-1, C-4, D-3", "ta": "A-2, B-1, C-4, D-3"},
            {"id": "B", "en": "A-3, B-4, C-1, D-2", "ta": "A-3, B-4, C-1, D-2"},
            {"id": "C", "en": "A-4, B-3, C-2, D-1", "ta": "A-4, B-3, C-2, D-1"},
            {"id": "D", "en": "A-1, B-2, C-3, D-4", "ta": "A-1, B-2, C-3, D-4"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "A-1: Bijoe Emmanuel = Art 51A(a). B-2: Public Property 2009 = Art 51A(i). C-3: A. Nagaraja = Art 51A(g). D-4: Mohan Kumar Singhania = Art 51A(j).",
            "ta": "A-1: பிஜோய் இம்மானுவேல் = உறுப்பு 51A(a). B-2: பொதுச் சொத்து 2009 = உறுப்பு 51A(i). C-3: ஏ. நாகராஜா = உறுப்பு 51A(g). D-4: மோகன் குமார் சிங்கானியா = உறுப்பு 51A(j)."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Bijoe Emmanuel matches 1, not 2.", "ta": "தவறு. பிஜோய் இம்மானுவேல் பொருத்தம் 1 ஆகும்."},
            "B": {"en": "Incorrect. Bijoe Emmanuel matches 1, not 3.", "ta": "தவறு. பிஜோய் இம்மானுவேல் பொருத்தம் 1 ஆகும்."},
            "C": {"en": "Incorrect. Bijoe Emmanuel matches 1, not 4.", "ta": "தவறு. பிஜோய் இம்மானுவேல் பொருத்தம் 1 ஆகும்."},
            "D": {"en": "Correct matching sequence.", "ta": "சரியான பொருத்தும் வரிசை."}
        },
        "tnpsc_tip": {
            "en": "Matching SC case law with specific sub-clauses is a frequent TNPSC Group 1 question style.",
            "ta": "உச்ச நீதிமன்ற வழக்குகளைச் குறிப்பிட்ட உட்பிரிவுகளுடன் பொருத்துவது டிஎன்பிஎஸ்சி குரூப் 1 பாணியாகும்."
        }
    },
    {
        "id": "FD_MTH_021",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Match the Following",
        "question": {
            "en": "Match List I (Statute Supporting Article 51A(e) Dignity of Women) with List II (Specific Legislative Objective) and select the correct code:",
            "ta": "பட்டியல் I-ஐ (உறுப்பு 51A(e) பெண்கள் கண்ணியத்தை ஆதரிக்கும் சட்டம்) பட்டியல் II உடன் (குறிப்பிட்ட சட்ட நோக்கம்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:"
        },
        "list_1": [
            {"id": "A", "en": "Dowry Prohibition Act, 1961", "ta": "வரதட்சணை தடைச் சட்டம், 1961"},
            {"id": "B", "en": "Domestic Violence Act, 2005", "ta": "குடும்ப வன்முறை தடைச் சட்டம், 2005"},
            {"id": "C", "en": "Indecent Representation of Women Act, 1986", "ta": "பெண்கள் ஒழுக்கக்கேடான சித்தரிப்பு தடைச் சட்டம், 1986"},
            {"id": "D", "en": "POSH Act, 2013", "ta": "பணியிடத்தில் பெண்கள் பாலியல் வன்கொடுமை தடைச் சட்டம், 2013"}
        ],
        "list_2": [
            {"id": "1", "en": "Penalizes demanding or giving dowry", "ta": "வரதட்சணை கேட்பதை அல்லது கொடுப்பதைத் தண்டிக்கிறது"},
            {"id": "2", "en": "Protects women from physical & mental abuse within home", "ta": "வீட்டுக்குள்ளான உடல் & மனத் துன்புறுத்தலிலிருந்து பெண்களைப் பாதுகாக்கிறது"},
            {"id": "3", "en": "Prohibits derogatory depiction of women in media & publications", "ta": "ஊடகங்களில் பெண்களைக் கேவலமாகச் சித்தரிப்பதைத் தடை செய்கிறது"},
            {"id": "4", "en": "Ensures safe workplace environment for women (Vishaka guidelines)", "ta": "பெண்களுக்குப் பாதுகாப்பான பணியிட சூழலை உறுதி செய்கிறது"}
        ],
        "options": [
            {"id": "A", "en": "A-1, B-2, C-3, D-4", "ta": "A-1, B-2, C-3, D-4"},
            {"id": "B", "en": "A-2, B-1, C-4, D-3", "ta": "A-2, B-1, C-4, D-3"},
            {"id": "C", "en": "A-3, B-4, C-1, D-2", "ta": "A-3, B-4, C-1, D-2"},
            {"id": "D", "en": "A-4, B-3, C-2, D-1", "ta": "A-4, B-3, C-2, D-1"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "A-1: Dowry Act 1961. B-2: Domestic Violence Act 2005. C-3: Indecent Representation Act 1986. D-4: POSH Act 2013. All these statutes reinforce the Art 51A(e) duty to renounce practices derogatory to women.",
            "ta": "A-1: வரதட்சணை சட்டம் 1961. B-2: குடும்ப வன்முறை சட்டம் 2005. C-3: ஒழுக்கக்கேடான சித்தரிப்பு சட்டம் 1986. D-4: POSH சட்டம் 2013. இவை அனைத்தும் உறுப்பு 51A(e) பெண்கள் கண்ணியத்தைக் காக்கும் கடமையை வலுப்படுத்துகின்றன."
        },
        "why_not_others": {
            "A": {"en": "Correct matching sequence.", "ta": "சரியான பொருத்தும் வரிசை."},
            "B": {"en": "Incorrect. Dowry Act matches 1, not 2.", "ta": "தவறு. வரதட்சணை சட்டம் பொருத்தம் 1 ஆகும்."},
            "C": {"en": "Incorrect. Dowry Act matches 1, not 3.", "ta": "தவறு. வரதட்சணை சட்டம் பொருத்தம் 1 ஆகும்."},
            "D": {"en": "Incorrect. Dowry Act matches 1, not 4.", "ta": "தவறு. வரதட்சணை சட்டம் பொருத்தம் 1 ஆகும்."}
        },
        "tnpsc_tip": {
            "en": "Article 51A(e) provides the constitutional foundation for all gender-justice laws.",
            "ta": "உறுப்பு 51A(e) அனைத்து பாலின-நீதிச் சட்டங்களுக்கும் அரசியலமைப்பு அடித்தளமாக அமைகிறது."
        }
    },
    {
        "id": "FD_MTH_022",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Hard",
        "question_type": "Match the Following",
        "question": {
            "en": "Match List I (Constitutional Segment Parts III, IV, IVA, Preamble) with List II (Primary Constitutional Function) and select the correct code:",
            "ta": "பட்டியல் I-ஐ (அரசியலமைப்புப் பகுதிகள் III, IV, IVA, முகப்புரை) பட்டியல் II உடன் (முதன்மை அரசியலமைப்புச் செயல்பாடு) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:"
        },
        "list_1": [
            {"id": "A", "en": "Part III Fundamental Rights", "ta": "பகுதி III அடிப்படை உரிமைகள்"},
            {"id": "B", "en": "Part IV Directive Principles", "ta": "பகுதி IV வழிகாட்டு நெறிமுறைகள்"},
            {"id": "C", "en": "Part IVA Fundamental Duties", "ta": "பகுதி IVA அடிப்படை கடமைகள்"},
            {"id": "D", "en": "Preamble", "ta": "முகப்புரை"}
        ],
        "list_2": [
            {"id": "1", "en": "Enforceable claims against State establishing Political Democracy", "ta": "அரசியல் ஜனநாயகத்தை நிறுவும் அரசுக்கு எதிரான அமல்படுத்தக்கூடிய உரிமைகள்"},
            {"id": "2", "en": "Non-justiciable directives to State establishing Socio-Economic Democracy", "ta": "சமூக-பொருளாதார ஜனநாயகத்தை நிறுவும் அரசுக்கான அமல்படுத்த முடியாத வழிகாட்டல்கள்"},
            {"id": "3", "en": "Non-justiciable moral obligations on Citizens promoting Civic Discipline", "ta": "குடிமை ஒழுங்கை ஊக்குவிக்கும் குடிமக்கள் மீதான அமல்படுத்த முடியாத கடமைகள்"},
            {"id": "4", "en": "Overarching constitutional vision, goals and philosophy", "ta": "ஒட்டுமொத்த அரசியலமைப்புப் பார்வை, இலக்குகள் & தத்துவம்"}
        ],
        "options": [
            {"id": "A", "en": "A-2, B-1, C-4, D-3", "ta": "A-2, B-1, C-4, D-3"},
            {"id": "B", "en": "A-1, B-2, C-3, D-4", "ta": "A-1, B-2, C-3, D-4"},
            {"id": "C", "en": "A-3, B-4, C-1, D-2", "ta": "A-3, B-4, C-1, D-2"},
            {"id": "D", "en": "A-4, B-3, C-2, D-1", "ta": "A-4, B-3, C-2, D-1"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "A-1: Part III = Political Democracy. B-2: Part IV = Socio-Economic Democracy. C-3: Part IVA = Civic Discipline. D-4: Preamble = Constitutional Philosophy.",
            "ta": "A-1: பகுதி III = அரசியல் ஜனநாயகம். B-2: பகுதி IV = சமூக-பொருளாதார ஜனநாயகம். C-3: பகுதி IVA = குடிமை ஒழுக்கம். D-4: முகப்புரை = அரசியலமைப்புத் தத்துவம்."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Part III matches 1, not 2.", "ta": "தவறு. பகுதி III பொருத்தம் 1 ஆகும்."},
            "B": {"en": "Correct matching sequence.", "ta": "சரியான பொருத்தும் வரிசை."},
            "C": {"en": "Incorrect. Part III matches 1, not 3.", "ta": "தவறு. பகுதி III பொருத்தம் 1 ஆகும்."},
            "D": {"en": "Incorrect. Part III matches 1, not 4.", "ta": "தவறு. பகுதி III பொருத்தம் 1 ஆகும்."}
        },
        "tnpsc_tip": {
            "en": "Part III + Part IV + Part IVA = Complete Indian Constitutional Triad.",
            "ta": "பகுதி III + பகுதி IV + பகுதி IVA = முழுமையான இந்திய அரசியலமைப்பு முக்கோணம்."
        }
    },
    {
        "id": "FD_MTH_023",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Medium",
        "question_type": "Match the Following",
        "question": {
            "en": "Match List I (Historical Timeline Milestone 1950-2002) with List II (Number of Fundamental Duties in Constitution) and select the correct code:",
            "ta": "பட்டியல் I-ஐ (வரலாற்று காலவரிசை மைல்கல் 1950-2002) பட்டியல் II உடன் (அரசியலமைப்பில் உள்ள அடிப்படை கடமைகளின் எண்ணிக்கை) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:"
        },
        "list_1": [
            {"id": "A", "en": "1950 Original Constitution", "ta": "1950 அசல் அரசியலமைப்பு"},
            {"id": "B", "en": "1976 Swaran Singh Committee Recommendation", "ta": "1976 ஸ்வரன் சிங் குழுவின் பரிந்துரை"},
            {"id": "C", "en": "1976 42nd Constitutional Amendment Enactment", "ta": "1976 42வது அரசியலமைப்பு திருத்த இயற்றல்"},
            {"id": "D", "en": "2002 86th Constitutional Amendment Enactment", "ta": "2002 86வது அரசியலமைப்பு திருத்த இயற்றல்"}
        ],
        "list_2": [
            {"id": "1", "en": "0 Duties (Zero duties in original text)", "ta": "0 கடமைகள் (அசல் உரையில் கடமைகள் ஏதுமில்லை)"},
            {"id": "2", "en": "8 Duties recommended", "ta": "8 கடமைகள் பரிந்துரைக்கப்பட்டன"},
            {"id": "3", "en": "10 Duties enacted into Art 51A(a)-(j)", "ta": "10 கடமைகள் உறுப்பு 51A(a)-(j)-ல் இயற்றப்பட்டன"},
            {"id": "4", "en": "11 Duties present in total [Art 51A(a)-(k)]", "ta": "மொத்தம் 11 கடமைகள் நிலவுகின்றன [உறுப்பு 51A(a)-(k)]"}
        ],
        "options": [
            {"id": "A", "en": "A-2, B-1, C-4, D-3", "ta": "A-2, B-1, C-4, D-3"},
            {"id": "B", "en": "A-3, B-4, C-1, D-2", "ta": "A-3, B-4, C-1, D-2"},
            {"id": "C", "en": "A-1, B-2, C-3, D-4", "ta": "A-1, B-2, C-3, D-4"},
            {"id": "D", "en": "A-4, B-3, C-2, D-1", "ta": "A-4, B-3, C-2, D-1"}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "A-1: Original 1950 text had 0 duties. B-2: Swaran Singh recommended 8 duties. C-3: 42nd CAA 1976 enacted 10 duties. D-4: 86th CAA 2002 added the 11th duty, making total 11 duties.",
            "ta": "A-1: 1950 அசல் உரையில் 0 கடமைகள் இருந்தன. B-2: ஸ்வரன் சிங் 8 கடமைகளைப் பரிந்துரைத்தார். C-3: 42வது திருத்தம் 1976 10 கடமைகளை இயற்றியது. D-4: 86வது திருத்தம் 2002 11வது கடமையைச் சேர்த்து மொத்தம் 11 கடமைகளாக்கியது."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. 1950 Original text matches 1, not 2.", "ta": "தவறு. 1950 அசல் உரை பொருத்தம் 1 ஆகும்."},
            "B": {"en": "Incorrect. 1950 Original text matches 1, not 3.", "ta": "தவறு. 1950 அசல் உரை பொருத்தம் 1 ஆகும்."},
            "C": {"en": "Correct matching sequence.", "ta": "சரியான பொருத்தும் வரிசை."},
            "D": {"en": "Incorrect. 1950 Original text matches 1, not 4.", "ta": "தவறு. 1950 அசல் உரை பொருத்தம் 1 ஆகும்."}
        },
        "tnpsc_tip": {
            "en": "Evolution sequence: 0 (1950) -> 8 (rec 1976) -> 10 (42nd CAA 1976) -> 11 (86th CAA 2002).",
            "ta": "வளர்ச்சி வரிசை: 0 (1950) -> 8 (பரிந்துரை 1976) -> 10 (42வது திருத்தம் 1976) -> 11 (86வது திருத்தம் 2002)."
        }
    },
    {
        "id": "FD_MTH_024",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Hard",
        "question_type": "Match the Following",
        "question": {
            "en": "Match List I (Article 51A Sub-clause a, e, i, k) with List II (Target Recipient / Institution of Duty) and select the correct code:",
            "ta": "பட்டியல் I-ஐ (உறுப்பு 51A உட்பிரிவு a, e, i, k) பட்டியல் II உடன் (கடமையின் இலக்குக் குழு / நிறுவனம்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:"
        },
        "list_1": [
            {"id": "A", "en": "Article 51A(a)", "ta": "உறுப்பு 51A(a)"},
            {"id": "B", "en": "Article 51A(e)", "ta": "உறுப்பு 51A(e)"},
            {"id": "C", "en": "Article 51A(i)", "ta": "உறுப்பு 51A(i)"},
            {"id": "D", "en": "Article 51A(k)", "ta": "உறுப்பு 51A(k)"}
        ],
        "list_2": [
            {"id": "1", "en": "National Flag, Anthem & Constitutional Institutions", "ta": "தேசியக் கொடி, கீதம் & அரசியலமைப்பு நிறுவனங்கள்"},
            {"id": "2", "en": "Dignity of Women & Inter-sectional People of India", "ta": "பெண்கள் கண்ணியம் & இந்திய அனைத்துப் பிரிவு மக்கள்"},
            {"id": "3", "en": "Public Assets & Non-violent Civic Order", "ta": "பொதுச் சொத்துக்கள் & வன்முறையற்ற குடிமை ஒழுங்கு"},
            {"id": "4", "en": "Children between 6 and 14 years of age", "ta": "6 முதல் 14 வயது வரையிலான குழந்தைகள்"}
        ],
        "options": [
            {"id": "A", "en": "A-2, B-1, C-4, D-3", "ta": "A-2, B-1, C-4, D-3"},
            {"id": "B", "en": "A-3, B-4, C-1, D-2", "ta": "A-3, B-4, C-1, D-2"},
            {"id": "C", "en": "A-4, B-3, C-2, D-1", "ta": "A-4, B-3, C-2, D-1"},
            {"id": "D", "en": "A-1, B-2, C-3, D-4", "ta": "A-1, B-2, C-3, D-4"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "A-1: 51A(a) targets symbols & institutions. B-2: 51A(e) targets women & brotherhood. C-3: 51A(i) targets public assets & non-violence. D-4: 51A(k) targets children (6-14 yrs).",
            "ta": "A-1: 51A(a) சின்னங்கள் & நிறுவனங்களை இலக்காகக் கொண்டது. B-2: 51A(e) பெண்கள் & சகோதரத்துவத்தை இலக்காகக் கொண்டது. C-3: 51A(i) பொதுச் சொத்துக்கள் & வன்முறை இன்மையை இலக்காகக் கொண்டது. D-4: 51A(k) குழந்தைகளை (6-14 வயது) இலக்காகக் கொண்டது."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Article 51A(a) matches 1, not 2.", "ta": "தவறு. உறுப்பு 51A(a) பொருத்தம் 1 ஆகும்."},
            "B": {"en": "Incorrect. Article 51A(a) matches 1, not 3.", "ta": "தவறு. உறுப்பு 51A(a) பொருத்தம் 1 ஆகும்."},
            "C": {"en": "Incorrect. Article 51A(a) matches 1, not 4.", "ta": "தவறு. உறுப்பு 51A(a) பொருத்தம் 1 ஆகும்."},
            "D": {"en": "Correct matching sequence.", "ta": "சரியான பொருத்தும் வரிசை."}
        },
        "tnpsc_tip": {
            "en": "Art 51A(k) uniquely addresses parents/guardians with respect to children.",
            "ta": "உறுப்பு 51A(k) குழந்தைகள் தொடர்பில் பெற்றோர்கள்/பாதுகாவலர்களை மட்டுமே குறிக்கிறது."
        }
    },
    {
        "id": "FD_MTH_025",
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": "Hard",
        "question_type": "Match the Following",
        "question": {
            "en": "Match List I (Global Constitutional Source / Legal Report) with List II (Influence on Indian Fundamental Duties) and select the correct code:",
            "ta": "பட்டியல் I-ஐ (உலகளாவிய அரசியலமைப்பு மூலம் / சட்ட அறிக்கை) பட்டியல் II உடன் (இந்திய அடிப்படை கடமைகள் மீதான செல்வாக்கு) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:"
        },
        "list_1": [
            {"id": "A", "en": "USSR / Socialist Constitutions", "ta": "USSR / சமதர்ம அரசியலமைப்புகள்"},
            {"id": "B", "en": "Japanese Constitution", "ta": "ஜப்பானிய அரசியலமைப்பு"},
            {"id": "C", "en": "Western Democratic Constitutions (USA/UK/France)", "ta": "மேலைநாட்டு ஜனநாயக அரசியலமைப்புகள் (USA/UK/பிரான்ஸ்)"},
            {"id": "D", "en": "Justice Verma Committee Report (1999)", "ta": "நீதிபதி வர்மா குழு அறிக்கை (1999)"}
        ],
        "list_2": [
            {"id": "1", "en": "Primary ideological inspiration for borrowing duties into Part IVA in 1976", "ta": "1976-ல் பகுதி IVA-ல் கடமைகளைப் பெற முதன்மை தத்துவார்த்த உத்வேகம்"},
            {"id": "2", "en": "Prominent democratic precedent explicitly embodying duties of citizens", "ta": "வெளிப்படையான குடிமக்கள் கடமைகளைக் கொண்ட முக்கிய ஜனநாயக முன்மாதிரி"},
            {"id": "3", "en": "Focus primarily on Rights without explicit constitutional citizen duties chapter", "ta": "வெளிப்படையான அரசியலமைப்பு கடமைகள் அத்தியாயமின்றி முதன்மையாக உரிமைகளில் கவனம்"},
            {"id": "4", "en": "Comprehensive mapping of statutory penal acts enforcing Part IVA duties", "ta": "பகுதி IVA கடமைகளை அமல்படுத்தும் சட்டப்பூர்வக் குற்றவியல் சட்டங்களின் விரிவான வரைபடமாக்கம்"}
        ],
        "options": [
            {"id": "A", "en": "A-1, B-2, C-3, D-4", "ta": "A-1, B-2, C-3, D-4"},
            {"id": "B", "en": "A-2, B-1, C-4, D-3", "ta": "A-2, B-1, C-4, D-3"},
            {"id": "C", "en": "A-3, B-4, C-1, D-2", "ta": "A-3, B-4, C-1, D-2"},
            {"id": "D", "en": "A-4, B-3, C-2, D-1", "ta": "A-4, B-3, C-2, D-1"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "A-1: USSR Constitution was the primary source for 1976 duties. B-2: Japan is the major democratic precedent with explicit duties. C-3: Western democracies lack explicit duties chapters. D-4: Verma Report mapped Indian statutory enforcement.",
            "ta": "A-1: 1976 கடமைகளுக்கு USSR அரசியலமைப்பே முதன்மை மூலமாகும். B-2: ஜப்பான் வெளிப்படையான கடமைகளைக் கொண்ட முக்கிய ஜனநாயக முன்மாதிரி. C-3: மேலைநாட்டு ஜனநாயகங்களில் வெளிப்படையான கடமைகள் அத்தியாயமில்லை. D-4: வர்மா அறிக்கை இந்தியச் சட்டப்பூர்வ அமலாக்கத்தை வரைபடமாக்கியது."
        },
        "why_not_others": {
            "A": {"en": "Correct matching sequence.", "ta": "சரியான பொருத்தும் வரிசை."},
            "B": {"en": "Incorrect. USSR matches 1, not 2.", "ta": "தவறு. USSR பொருத்தம் 1 ஆகும்."},
            "C": {"en": "Incorrect. USSR matches 1, not 3.", "ta": "தவறு. USSR பொருத்தம் 1 ஆகும்."},
            "D": {"en": "Incorrect. USSR matches 1, not 4.", "ta": "தவறு. USSR பொருத்தம் 1 ஆகும்."}
        },
        "tnpsc_tip": {
            "en": "Source: Former Soviet Union (USSR) | Democratic precedent: Japan.",
            "ta": "மூலம்: முன்னாள் சோவியத் யூனியன் (USSR) | ஜனநாயக முன்மாதிரி: ஜப்பான்."
        }
    }
]

target_files = [
    "data/questions/polity/fundamental_duties_match.json",
    "data/questions/polity/fundamental_duties_match_the_following.json"
]

for target_file in target_files:
    os.makedirs(os.path.dirname(target_file), exist_ok=True)
    with open(target_file, "w", encoding="utf-8") as f:
        json.dump(questions_data, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {len(questions_data)} Match the Following questions in {target_files[0]} and {target_files[1]}")
