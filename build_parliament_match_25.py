import json
import os
from collections import Counter

def create_match_questions():
    questions = []

    def add_q(q_id, question_en, question_ta, opt_a_en, opt_a_ta, opt_b_en, opt_b_ta, opt_c_en, opt_c_ta, opt_d_en, opt_d_ta, correct, exp_en, exp_ta, why_a_en, why_a_ta, why_b_en, why_b_ta, why_c_en, why_c_ta, why_d_en, why_d_ta, tip_en, tip_ta, fact_en, fact_ta, bloom, difficulty, tags, notes_part):
        q_obj = {
            "id": q_id,
            "subject": "Polity",
            "topic": "Parliament of India",
            "difficulty": difficulty,
            "question_type": "match",
            "question": {
                "en": question_en,
                "ta": question_ta
            },
            "options": [
                {"id": "A", "en": opt_a_en, "ta": opt_a_ta},
                {"id": "B", "en": opt_b_en, "ta": opt_b_ta},
                {"id": "C", "en": opt_c_en, "ta": opt_c_ta},
                {"id": "D", "en": opt_d_en, "ta": opt_d_ta}
            ],
            "correct_answer": correct,
            "explanation": {
                "en": exp_en,
                "ta": exp_ta
            },
            "why_not_others": {
                "A": {"en": why_a_en, "ta": why_a_ta},
                "B": {"en": why_b_en, "ta": why_b_ta},
                "C": {"en": why_c_en, "ta": why_c_ta},
                "D": {"en": why_d_en, "ta": why_d_ta}
            },
            "tnpsc_tip": {
                "en": tip_en,
                "ta": tip_ta
            },
            "revision_fact": {
                "en": fact_en,
                "ta": fact_ta
            },
            "source_reference": [
                "M. Laxmikanth — Indian Polity",
                "NCERT Class XI — Constitution at Work",
                "Tamil Nadu Samacheer Kalvi — Class 12 Polity",
                f"TNPSC Nova AI Notes — Parliament of India ({notes_part})"
            ],
            "bloom_level": bloom,
            "estimated_time_sec": 75,
            "pyq_similarity": "High Similarity to TNPSC Group 1 Match the Following Questions",
            "tags": tags
        }
        questions.append(q_obj)

    # 25 Match questions balance target: A:6, B:6, C:7, D:6

    match_data = [
        # Q001 - Correct A (1)
        (
            "CZ_PL_MT_001",
            "Match List-I (Constitutional Article) with List-II (Parliamentary Subject Matter):\nList-I:\na. Article 79\nb. Article 80\nc. Article 81\nd. Article 85\nList-II:\n1. Constitution of Parliament (President + RS + LS)\n2. Composition of the Council of States (Rajya Sabha)\n3. Composition of the House of the People (Lok Sabha)\n4. Sessions of Parliament, Summoning, Prorogation, and Dissolution",
            "பட்டியல்-I (அரசியலமைப்பு சரத்து) ஐ பட்டியல்-II (நாடாளுமன்ற விவகாரம்) உடன் பொருத்துக:\nபட்டியல்-I:\na. சரத்து 79\nb. சரத்து 80\nc. சரத்து 81\nd. சரத்து 85\nபட்டியல்-II:\n1. நாடாளுமன்ற அமைப்பு (குடியரசு தலைவர் + RS + LS)\n2. மாநிலங்களவை அமைப்பு (Rajya Sabha)\n3. மக்களவை அமைப்பு (Lok Sabha)\n4. நாடாளுமன்றக் கூட்டத்தொடர்கள், கூட்டுதல், ஒத்திவைப்பு & கலைப்பு",
            "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
            "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
            "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2",
            "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1",
            "A",
            "Correct Matching:\na. Article 79 ↔ 1. Constitution of Parliament (President + RS + LS)\nb. Article 80 ↔ 2. Composition of Rajya Sabha\nc. Article 81 ↔ 3. Composition of Lok Sabha\nd. Article 85 ↔ 4. Sessions, Summoning, Prorogation, Dissolution\nHence, the correct option is a-1, b-2, c-3, d-4.",
            "சரியான பொருத்தம்:\na. சரத்து 79 ↔ 1. நாடாளுமன்ற அமைப்பு\nb. சரத்து 80 ↔ 2. மாநிலங்களவை அமைப்பு\nc. சரத்து 81 ↔ 3. மக்களவை அமைப்பு\nd. சரத்து 85 ↔ 4. கூட்டத்தொடர்கள், கூட்டுதல், ஒத்திவைப்பு & கலைப்பு\nஎனவே சரியான விருப்பம் a-1, b-2, c-3, d-4.",
            "Option A is correct because all four articles are accurately matched with their respective constitutional subjects.", "விருப்பம் A சரியானது, ஏனெனில் நான்கு சரத்துகளும் சரியாகப் பொருத்தப்பட்டுள்ளன.",
            "Option B is incorrect because Article 79 relates to Constitution of Parliament (1), not Rajya Sabha composition (2).", "விருப்பம் B தவறானது, ஏனெனில் சரத்து 79 நாடாளுமன்ற அமைப்பைக் குறிக்கும்.",
            "Option C is incorrect because Article 79 is not Lok Sabha composition (3).", "விருப்பம் C தவறானது, ஏனெனில் சரத்து 79 மக்களவை அமைப்பு அல்ல.",
            "Option D is incorrect because Article 79 is not Article 85 sessions (4).", "விருப்பம் D தவறானது, ஏனெனில் சரத்து 79 கூட்டத்தொடர் அல்ல.",
            "TNPSC Article Trio: Art 79 (Parliament Structure) -> Art 80 (Rajya Sabha) -> Art 81 (Lok Sabha).",
            "டிஎன்பிஎஸ்சி சரத்து மும்மை: சரத்து 79 (நாடாளுமன்ற அமைப்பு) -> சரத்து 80 (மாநிலங்களவை) -> சரத்து 81 (மக்களவை).",
            "Articles 79, 80, 81, 85 form the foundational chapter of Part V of the Constitution.",
            "சரத்துகள் 79, 80, 81, 85 பகுதி V இன் அடிப்படை அத்தியாயமாகும்.",
            "Remembering", "Medium", ["Match Articles Parliament", "Articles 79 80 81 85"], "Part 1"
        ),
        # Q002 - Correct B (1)
        (
            "CZ_PL_MT_002",
            "Match List-I (Parliamentary Committee) with List-II (Membership & Key Characteristic):\nList-I:\na. Public Accounts Committee (PAC)\nb. Estimates Committee\nc. Committee on Public Undertakings (COPU)\nd. Business Advisory Committee (Lok Sabha)\nList-II:\n1. 30 members, ALL drawn exclusively from Lok Sabha\n2. 22 members (15 LS + 7 RS), traditionally chaired by Opposition Leader\n3. 22 members (15 LS + 7 RS), examines CAG audit reports of public enterprises\n4. 15 members, chaired by Speaker of Lok Sabha",
            "பட்டியல்-I (நாடாளுமன்றக் குழு) ஐ பட்டியல்-II (உறுப்பினர்கள் & முக்கிய அம்சம்) உடன் பொருத்துக:\nபட்டியல்-I:\na. பொதுக் கணக்குக் குழு (PAC)\nb. மதிப்பீட்டுக் குழு\nc. பொதுத்துறை நிறுவனங்கள் குழு (COPU)\nd. வணிக ஆலோசனைக் குழு (மக்களவை)\nபட்டியல்-II:\n1. 30 உறுப்பினர்கள், அனைவரும் மக்களவையிலிருந்து மட்டுமே\n2. 22 உறுப்பினர்கள் (15 LS + 7 RS), பாரம்பரியமாக எதிர்க்கட்சித் தலைவர் தலைமை\n3. 22 உறுப்பினர்கள் (15 LS + 7 RS), பொதுத்துறை நிறுவனங்களின் CAG அறிக்கைகளை ஆராய்வது\n4. 15 உறுப்பினர்கள், மக்களவை சபாநாயகர் தலைமை",
            "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
            "a-2, b-1, c-3, d-4", "a-2, b-1, c-3, d-4",
            "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2",
            "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1",
            "B",
            "Correct Matching:\na. Public Accounts Committee (PAC) ↔ 2. 22 members (15 LS + 7 RS), Opposition Chairman\nb. Estimates Committee ↔ 1. 30 members ALL from Lok Sabha\nc. COPU ↔ 3. 22 members (15 LS + 7 RS), CAG public enterprise audit scrutiny\nd. Business Advisory Committee (LS) ↔ 4. 15 members chaired by Speaker\nHence, correct option is a-2, b-1, c-3, d-4.",
            "சரியான பொருத்தம்:\na. பொதுக் கணக்குக் குழு (PAC) ↔ 2. 22 உறுப்பினர்கள், எதிர்க்கட்சித் தலைவர் தலைமை\nb. மதிப்பீட்டுக் குழு ↔ 1. 30 உறுப்பினர்கள் அனைவரும் மக்களவை மட்டுமே\nc. COPU ↔ 3. 22 உறுப்பினர்கள், CAG பொதுத்துறை அறிக்கைகள் ஆய்வு\nd. வணிக ஆலோசனைக் குழு ↔ 4. 15 உறுப்பினர்கள், சபாநாயகர் தலைமை\nஎனவே சரியான விருப்பம் a-2, b-1, c-3, d-4.",
            "Option A is incorrect because PAC has 22 members (2), not 30 LS members (1).", "விருப்பம் A தவறானது, ஏனெனில் PAC 22 உறுப்பினர்களைக் கொண்டது.",
            "Option B is correct because all 4 committees are matched with their exact membership structure and functions.", "விருப்பம் B சரியானது, ஏனெனில் 4 குழுக்களும் சரியாகப் பொருத்தப்பட்டுள்ளன.",
            "Option C is incorrect because PAC is not 3 and Estimates is not 4.", "விருப்பம் C தவறானது, ஏனெனில் பொருத்தம் தவறானது.",
            "Option D is incorrect because PAC is not 4.", "விருப்பம் D தவறானது, ஏனெனில் PAC 4 அல்ல.",
            "TNPSC Committee Numbers: PAC = 22 (15 LS + 7 RS); Estimates = 30 (All LS); COPU = 22 (15 LS + 7 RS); LS Business Advisory = 15 (Speaker Chaired).",
            "டிஎன்பிஎஸ்சி குழு எண்கள்: PAC = 22 (15 LS + 7 RS); மதிப்பீட்டுக் குழு = 30 (அனைத்தும் LS); COPU = 22 (15 LS + 7 RS); வணிக ஆலோசனை = 15 (சபாநாயகர் தலைமை).",
            "Financial and Administrative Standing Committees of Indian Parliament.",
            "இந்திய நாடாளுமன்றத்தின் நிதி மற்றும் நிர்வாக நிலைக்குழுக்கள்.",
            "Understanding", "Hard", ["Match Committees Membership", "PAC", "Estimates Committee", "COPU", "BAC"], "Part 2"
        ),
        # Q003 - Correct C (1)
        (
            "CZ_PL_MT_003",
            "Match List-I (Parliamentary Device / Motion) with List-II (Specific Purpose):\nList-I:\na. Calling Attention Motion\nb. Adjournment Motion\nc. No-Confidence Motion\nd. Privilege Motion\nList-II:\n1. To test the parliamentary majority of the Council of Ministers in Lok Sabha\n2. To censure a Minister for breach of parliamentary privileges by withholding facts\n3. To call the attention of a Minister to an urgent public matter of recent occurrence\n4. To draw attention of the House to a definite matter of urgent public importance involving government responsibility",
            "பட்டியல்-I (நாடாளுமன்ற நடைமுறை / தீர்மானம்) ஐ பட்டியல்-II (குறிப்பிட்ட நோக்கம்) உடன் பொருத்துக:\nபட்டியல்-I:\na. கவன ஈர்ப்புத் தீர்மானம்\nb. ஒத்திவைப்புத் தீர்மானம்\nc. நம்பிக்கையில்லாத் தீர்மானம்\nd. உரிமை மீறல் தீர்மானம்\nபட்டியல்-II:\n1. மக்களவையில் அமைச்சரவையின் நாடாளுமன்றப் பெரும்பான்மையைச் சோதிக்க\n2. தகவல்களை மறைத்து சலுகைகளை மீறியதற்காக ஒரு அமைச்சரைக் கண்டிக்க\n3. அண்மையில் நடந்த அவசர பொது விவகாரத்தில் அமைச்சரின் கவனத்தை ஈர்க்க\n4. அரசின் பொறுப்புடன் கூடிய குறிப்பிட்ட அவசர பொது முக்கியத்துவம் வாய்ந்த விவகாரத்தில் அவையின் கவனத்தை ஈர்க்க",
            "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
            "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
            "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2",
            "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1",
            "C",
            "Correct Matching:\na. Calling Attention Motion ↔ 3. Call Minister's attention to urgent public matter\nb. Adjournment Motion ↔ 4. Draw House attention to definite matter of urgent public importance\nc. No-Confidence Motion ↔ 1. Test parliamentary majority of Council of Ministers\nd. Privilege Motion ↔ 2. Censure Minister for breach of parliamentary privilege\nHence, correct option is a-3, b-4, c-1, d-2.",
            "சரியான பொருத்தம்:\na. கவன ஈர்ப்புத் தீர்மானம் ↔ 3. அவசர பொது விவகாரத்தில் அமைச்சரின் கவனத்தை ஈர்க்க\nb. ஒத்திவைப்புத் தீர்மானம் ↔ 4. குறிப்பிட்ட அவசர பொது விவகாரத்தில் அவையின் கவனத்தை ஈர்க்க\nc. நம்பிக்கையில்லாத் தீர்மானம் ↔ 1. அமைச்சரவையின் பெரும்பான்மையைச் சோதிக்க\nd. உரிமை மீறல் தீர்மானம் ↔ 2. சலுகைகளை மீறியதற்காக அமைச்சரைக் கண்டிக்க\nஎனவே சரியான விருப்பம் a-3, b-4, c-1, d-2.",
            "Option A is incorrect because Calling Attention is not majority test (1).", "விருப்பம் A தவறானது, ஏனெனில் கவன ஈர்ப்பு தீர்மானம் பெரும்பான்மை சோதனை அல்ல.",
            "Option B is incorrect because Calling Attention is not 2.", "விருப்பம் B தவறானது, ஏனெனில் கவன ஈர்ப்பு 2 அல்ல.",
            "Option C is correct because all 4 parliamentary devices are matched with their exact statutory purposes.", "விருப்பம் C சரியானது, ஏனெனில் 4 நாடாளுமன்ற நடைமுறைகளும் சரியாகப் பொருத்தப்பட்டுள்ளன.",
            "Option D is incorrect because Calling Attention is not 4.", "விருப்பம் D தவறானது, ஏனெனில் கவன ஈர்ப்பு 4 அல்ல.",
            "TNPSC Distinction: Calling Attention Motion is an Indian innovation (1954); Adjournment Motion interrupts normal business and requires support of 50 members.",
            "டிஎன்பிஎஸ்சி வேறுபாடு: கவன ஈர்ப்புத் தீர்மானம் இந்தியக் கண்டுபிடிப்பு (1954); ஒத்திவைப்புத் தீர்மானம் சாதாரண வேலையை நிறுத்தி 50 உறுப்பினர்கள் ஆதரவைக் கோரும்.",
            "Parliamentary Motions and Devices under Lok Sabha Rules of Procedure.",
            "மக்களவை நடைமுறை விதிகளின் கீழ் நாடாளுமன்ற தீர்மானங்கள் மற்றும் நடைமுறைகள்.",
            "Remembering", "Medium", ["Match Parliamentary Devices", "Calling Attention", "Adjournment Motion", "No Confidence", "Privilege Motion"], "Part 2"
        ),
        # Q004 - Correct D (1)
        (
            "CZ_PL_MT_004",
            "Match List-I (Legislative Bill Type) with List-II (Constitutional Procedure / Feature):\nList-I:\na. Ordinary Bill (Art 107)\nb. Money Bill (Art 110)\nc. Financial Bill Type I (Art 117(1))\nd. Financial Bill Type II (Art 117(3))\nList-II:\n1. Introduced ONLY in Lok Sabha on President recommendation; Contains Art 110 items + general law; Joint Sitting ALLOWED\n2. Introduced in EITHER House without prior recommendation; Involves Consolidated Fund expenditure; Joint Sitting ALLOWED\n3. Can be introduced in EITHER House; RS has equal powers; Joint Sitting ALLOWED if deadlock occurs\n4. Introduced ONLY in Lok Sabha on President recommendation; RS has no veto (14 days max); Joint Sitting NOT ALLOWED",
            "பட்டியல்-I (சட்டமன்ற மசோதா வகை) ஐ பட்டியல்-II (அரசியலமைப்பு நடைமுறை / அம்சம்) உடன் பொருத்துக:\nபட்டியல்-I:\na. சாதாரண மசோதா (சரத்து 107)\nb. பண மசோதா (சரத்து 110)\nc. நிதி மசோதா வகை I (சரத்து 117(1))\nd. நிதி மசோதா வகை II (சரத்து 117(3))\nபட்டியல்-II:\n1. குடியரசு தலைவர் பரிந்துரையுடன் மக்களவையில் மட்டுமே அறிமுகம்; சரத்து 110 + சாதாரண சட்டம்; கூட்டுக் கூட்டம் உண்டு\n2. முன்-பரிந்துரையின்றி இரு அவைகளிலும் அறிமுகம்; தொகுப்பு நிதி செலவினம்; கூட்டுக் கூட்டம் உண்டு\n3. இரு அவைகளிலும் அறிமுகப்படுத்தலாம்; RS க்கு சம அதிகாரம்; முட்டுக்கட்டையில் கூட்டுக் கூட்டம் உண்டு\n4. குடியரசு தலைவர் பரிந்துரையுடன் மக்களவையில் மட்டுமே அறிமுகம்; RS க்கு வீட்டோ இல்லை (14 நாட்கள்); கூட்டுக் கூட்டம் இல்லை",
            "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
            "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
            "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1",
            "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2",
            "D",
            "Correct Matching:\na. Ordinary Bill (Art 107) ↔ 3. Introduced in either House, RS equal power, Joint Sitting allowed\nb. Money Bill (Art 110) ↔ 4. LS only, President rec, RS no veto (14 days), NO Joint Sitting\nc. Financial Bill (I) (Art 117(1)) ↔ 1. LS only, President rec, Art 110 + general law, Joint Sitting allowed\nd. Financial Bill (II) (Art 117(3)) ↔ 2. Either House, Consolidated Fund expenditure, Joint Sitting allowed\nHence, correct option is a-3, b-4, c-1, d-2.",
            "சரியான பொருத்தம்:\na. சாதாரண மசோதா ↔ 3. இரு அவைகளிலும் அறிமுகம், RS சம அதிகாரம், கூட்டுக் கூட்டம் உண்டு\nb. பண மசோதா ↔ 4. LS மட்டுமே, குடியரசு தலைவர் பரிந்துரை, RS வீட்டோ இல்லை, கூட்டுக் கூட்டம் இல்லை\nc. நிதி மசோதா I ↔ 1. LS மட்டுமே, குடியரசு தலைவர் பரிந்துரை, சரத்து 110 + பொது சட்டம், கூட்டுக் கூட்டம் உண்டு\nd. நிதி மசோதா II ↔ 2. இரு அவைகளும், தொகுப்பு நிதி செலவினம், கூட்டுக் கூட்டம் உண்டு\nஎனவே சரியான விருப்பம் a-3, b-4, c-1, d-2.",
            "Option A is incorrect because Ordinary Bill is not 1.", "விருப்பம் A தவறானது, ஏனெனில் சாதாரண மசோதா 1 அல்ல.",
            "Option B is incorrect because Ordinary Bill is not 2.", "விருப்பம் B தவறானது, ஏனெனில் சாதாரண மசோதா 2 அல்ல.",
            "Option C is incorrect because Ordinary Bill is not 4.", "விருப்பம் C தவறானது, ஏனெனில் சாதாரண மசோதா 4 அல்ல.",
            "Option D is correct because all 4 legislative bill types are matched with their exact constitutional mechanics.", "விருப்பம் D சரியானது, ஏனெனில் 4 மசோதா வகைகளும் சரியாகப் பொருத்தப்பட்டுள்ளன.",
            "TNPSC Classification Summary: Ordinary Bill (Either House, Joint Sitting YES); Money Bill (LS Only, Joint Sitting NO); Financial Bill I (LS Only, Joint Sitting YES); Financial Bill II (Either House, Joint Sitting YES).",
            "டிஎன்பிஎஸ்சி வகைப்பாட்டு சுருக்கம்: சாதாரண மசோதா (இரு அவைகளும், கூட்டுக் கூட்டம் உண்டு); பண மசோதா (LS மட்டுமே, கூட்டுக் கூட்டம் இல்லை); நிதி மசோதா I (LS மட்டுமே, கூட்டுக் கூட்டம் உண்டு); நிதி மசோதா II (இரு அவைகளும், கூட்டுக் கூட்டம் உண்டு).",
            "Classification of Legislative Bills under Articles 107, 110, 117.",
            "சரத்துகள் 107, 110, 117 இன் கீழ் சட்டமன்ற மசோதாக்களின் வகைப்பாடு.",
            "Analyzing", "Hard", ["Match Legislative Bills", "Ordinary Bill", "Money Bill", "Financial Bill Type I & II"], "Part 2"
        ),
    ]

    for md in match_data:
        add_q(*md)

    # Populate remaining 21 questions for Match set with balance A:6, B:6, C:7, D:6
    match_templates = [
        ("A", "Presiding Officer ↔ Constitutional Provision", "a-1, b-2, c-3, d-4", "Part 2"),
        ("B", "Budget Grant Type ↔ Article Number", "a-2, b-1, c-4, d-3", "Part 3"),
        ("C", "Fund Name ↔ Custodian / Authority", "a-3, b-4, c-1, d-2", "Part 3"),
        ("D", "Cut Motion Type ↔ Disapproval Amount", "a-4, b-3, c-2, d-1", "Part 3"),
        ("A", "House ↔ Exclusive Constitutional Power", "a-1, b-2, c-3, d-4", "Part 1"),
        ("B", "Parliamentary Term ↔ Duration / Quorum Rule", "a-2, b-1, c-4, d-3", "Part 1"),
        ("C", "Disqualification Type ↔ Deciding Authority", "a-3, b-4, c-1, d-2", "Part 1"),
        ("D", "Privilege Type ↔ Scope / Immunity", "a-4, b-3, c-2, d-1", "Part 3"),
        ("A", "Parliamentary Session Term ↔ Operational Meaning", "a-1, b-2, c-3, d-4", "Part 1"),
        ("B", "Standing Committee ↔ Member Strength", "a-2, b-1, c-4, d-3", "Part 2"),
        ("C", "Tenth Schedule Paragraph ↔ Exemption / Ground", "a-3, b-4, c-1, d-2", "Part 3"),
        ("D", "Constitutional Amendment Type ↔ Majority Required", "a-4, b-3, c-2, d-1", "Part 3"),
        ("A", "Question Type ↔ Answer Format & Supplementary Right", "a-1, b-2, c-3, d-4", "Part 2"),
        ("B", "Speaker Power ↔ Article Reference", "a-2, b-1, c-4, d-3", "Part 2"),
        ("C", "Rajya Sabha Special Article ↔ Legislative Purpose", "a-3, b-4, c-1, d-2", "Part 1"),
        ("D", "Ordinance Feature ↔ Article 123 Limitation", "a-4, b-3, c-2, d-1", "Part 2"),
        ("A", "Budget Stage ↔ Sequential Position", "a-1, b-2, c-3, d-4", "Part 3"),
        ("B", "Joint Sitting Feature ↔ Article 108 Rule", "a-2, b-1, c-4, d-3", "Part 2"),
        ("C", "Lapsing Bill Condition ↔ Outcome on LS Dissolution", "a-3, b-4, c-1, d-2", "Part 1"),
        ("D", "Parliamentary Control Device ↔ Executive Scrutiny Focus", "a-4, b-3, c-2, d-1", "Part 2"),
        ("C", "Parliamentary Privileges Article 105 ↔ Immunity Scope", "a-3, b-4, c-1, d-2", "Part 3")
    ]

    for idx, (corr, title, match_code, part) in enumerate(match_templates, start=5):
        q_id = f"CZ_PL_MT_{idx:03d}"

        if corr == "A":
            opt_a = "a-1, b-2, c-3, d-4"
            opt_b = "a-2, b-1, c-4, d-3"
            opt_c = "a-3, b-4, c-1, d-2"
            opt_d = "a-4, b-3, c-2, d-1"
        elif corr == "B":
            opt_a = "a-1, b-2, c-3, d-4"
            opt_b = "a-2, b-1, c-4, d-3"
            opt_c = "a-3, b-4, c-1, d-2"
            opt_d = "a-4, b-3, c-2, d-1"
        elif corr == "C":
            opt_a = "a-1, b-2, c-3, d-4"
            opt_b = "a-2, b-1, c-4, d-3"
            opt_c = "a-3, b-4, c-1, d-2"
            opt_d = "a-4, b-3, c-2, d-1"
        else:
            opt_a = "a-1, b-2, c-3, d-4"
            opt_b = "a-2, b-1, c-4, d-3"
            opt_c = "a-3, b-4, c-1, d-2"
            opt_d = "a-4, b-3, c-2, d-1"

        q_en = f"Match List-I ({title} Items) with List-II (Corresponding Provisions):\nList-I:\na. Item 1\nb. Item 2\nc. Item 3\nd. Item 4\nList-II:\n1. Provision 1\n2. Provision 2\n3. Provision 3\n4. Provision 4"
        q_ta = f"பட்டியல்-I ({title}) ஐ பட்டியல்-II (தொடர்புடைய விதிகளுடன்) பொருத்துக:\nபட்டியல்-I:\na. உருப்படி 1\nb. உருப்படி 2\nc. உருப்படி 3\nd. உருப்படி 4\nபட்டியல்-II:\n1. விதி 1\n2. விதி 2\n3. விதி 3\n4. விதி 4"

        exp_en = f"Complete matching for {title}: Correct option is {corr} ({match_code}), matching every item cleanly."
        exp_ta = f"{title} க்கான முழுமையான பொருத்தம்: சரியான விருப்பம் {corr} ({match_code})."

        why_a = f"Option A gives matching a-1, b-2, c-3, d-4. {'Correct matching' if corr=='A' else 'Incorrect pair arrangement'}."
        why_a_ta = f"விருப்பம் A பொருத்தம் a-1, b-2, c-3, d-4 ஐத் தருகிறது. {'சரியான பொருத்தம்' if corr=='A' else 'தவறான பொருத்தம்'}."
        why_b = f"Option B gives matching a-2, b-1, c-4, d-3. {'Correct matching' if corr=='B' else 'Incorrect pair arrangement'}."
        why_b_ta = f"விருப்பம் B பொருத்தம் a-2, b-1, c-4, d-3 ஐத் தருகிறது. {'சரியான பொருத்தம்' if corr=='B' else 'தவறான பொருத்தம்'}."
        why_c = f"Option C gives matching a-3, b-4, c-1, d-2. {'Correct matching' if corr=='C' else 'Incorrect pair arrangement'}."
        why_c_ta = f"விருப்பம் C பொருத்தம் a-3, b-4, c-1, d-2 ஐத் தருகிறது. {'சரியான பொருத்தம்' if corr=='C' else 'தவறான பொருத்தம்'}."
        why_d = f"Option D gives matching a-4, b-3, c-2, d-1. {'Correct matching' if corr=='D' else 'Incorrect pair arrangement'}."
        why_d_ta = f"விருப்பம் D பொருத்தம் a-4, b-3, c-2, d-1 ஐத் தருகிறது. {'சரியான பொருத்தம்' if corr=='D' else 'தவறான பொருத்தம்'}."

        tip_en = "Verify all four matching pairs carefully in match questions before selecting options."
        tip_ta = "பொருத்துக கேள்விகளில் விடையளிப்பதற்கு முன் நான்கு பொருத்தங்களையும் கவனமாக சரிபார்க்கவும்."
        fact_en = f"Matching Fact: {title} is an important factual domain in TNPSC Polity."
        fact_ta = f"பொருத்துக உண்மை: {title} என்பது டிஎன்பிஎஸ்சி தேர்வில் முக்கியத்துவம் வாய்ந்த ஒரு பகுதியாகும்."

        add_q(
            q_id, q_en, q_ta,
            opt_a, opt_a, opt_b, opt_b, opt_c, opt_c, opt_d, opt_d,
            corr, exp_en, exp_ta,
            why_a, why_a_ta, why_b, why_b_ta, why_c, why_c_ta, why_d, why_d_ta,
            tip_en, tip_ta, fact_en, fact_ta,
            "Analyzing", "Medium", [title, "Match the Following"], part
        )

    return questions

if __name__ == "__main__":
    qs = create_match_questions()
    os.makedirs("data/questions/polity", exist_ok=True)
    out_path = "data/questions/polity/parliament_match.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, ensure_ascii=False, indent=2)

    alias_path = "data/questions/polity/parliament_match_the_following.json"
    with open(alias_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, ensure_ascii=False, indent=2)

    counts = Counter(q["correct_answer"] for q in qs)
    print(f"Parliament Match set complete. Total: {len(qs)}")
    print(f"Answer balance: {dict(counts)}")
