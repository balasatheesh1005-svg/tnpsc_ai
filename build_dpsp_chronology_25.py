import json
import os

q_data = []

def make_q(q_id, difficulty, q_en, q_ta, events_list, options_list, ca, exp_en, exp_ta, wno_dict, trap_en, trap_ta, fact_en, fact_ta, bloom="Understand", est_time=60, pyq="High", tags=None):
    if tags is None:
        tags = ["Polity", "Directive Principles of State Policy", "Chronology"]
    
    events = []
    for idx, (e_en, e_ta) in enumerate(events_list, 1):
        events.append({"id": str(idx), "en": e_en, "ta": e_ta})
        
    options = []
    options_en = []
    options_ta = []
    for opt_id, opt_str in zip(["A", "B", "C", "D"], options_list):
        options.append({"id": opt_id, "en": opt_str, "ta": opt_str})
        options_en.append(opt_str)
        options_ta.append(opt_str)
        
    wno = {}
    for letter in ["A", "B", "C", "D"]:
        wno[letter] = {
            "en": wno_dict[letter][0],
            "ta": wno_dict[letter][1]
        }
        
    obj = {
        "id": q_id,
        "subject": "Polity",
        "topic": "Directive Principles of State Policy",
        "difficulty": difficulty,
        "question_type": "Chronology",
        "question": {"en": q_en, "ta": q_ta},
        "events": events,
        "options": options,
        "correct_answer": ca,
        "explanation": {"en": exp_en, "ta": exp_ta},
        "why_not_others": wno,
        "tnpsc_tip": {"en": f"TNPSC Trap: {trap_en}", "ta": f"TNPSC பொறி: {trap_ta}"},
        "revision_fact": {"en": fact_en, "ta": fact_ta},
        "source_reference": ["M. Laxmikanth - Indian Polity", "NCERT", "Samacheer Kalvi"],
        "bloom_level": bloom,
        "estimated_time_sec": est_time,
        "pyq_similarity": pyq,
        "tags": tags,
        "question_en": q_en,
        "question_ta": q_ta,
        "options_en": options_en,
        "options_ta": options_ta,
        "answer": ca.lower(),
        "explanation_en": exp_en,
        "explanation_ta": exp_ta
    }
    return obj

# Q1 (Easy - A)
q_data.append(make_q(
    "DPSP_CHRONO_001", "Easy",
    "Arrange the following landmark Supreme Court judgments regarding the hierarchy between Fundamental Rights and Directive Principles in correct chronological order (earliest to latest):\n\n1. State of Madras v. Champakam Dorairajan (DPSP made subsidiary to Fundamental Rights)\n2. Golaknath v. State of Punjab (Fundamental Rights declared transcendental and unamendable)\n3. Kesavananda Bharati v. State of Kerala (Upheld validity of 1st part of Article 31C)\n4. Minerva Mills v. Union of India (Balance between Part III and Part IV declared Basic Structure)",
    "அடிப்படை உரிமைகள் மற்றும் அரசு நெறிமுறைப்படுத்தும் கோட்பாடுகளுக்கு இடையேயான முக்கியத்துவத்தைப் பற்றிய உச்சநீதிமன்றத் தீர்ப்புகளைச் சரியான காலவரிசைப்படி (முந்தையது முதல் பிந்தையது வரை) வரிசைப்படுத்தவும்:\n\n1. மதராஸ் மாநிலம் எதிராக செம்பகம் துரைராஜன் (அரசு நெறிமுறைக் கோட்பாடுகள் அடிப்படை உரிமைகளுக்கு துணையானவை)\n2. கோலக்நாத் எதிராக பஞ்சாப் மாநிலம் (அடிப்படை உரிமைகள் மாற்ற முடியாத உன்னதமானவை எனத் தீர்ப்பு)\n3. கேசவாநந்த பாரதி எதிராக கேரள மாநிலம் (பிரிவு 31C-ன் முதல் பகுதியின் செல்லுபடித்ன்மை உறுதி செய்யப்பட்டது)\n4. மினர்வா மில்ஸ் எதிராக இந்திய யூனியன் (பகுதி III மற்றும் பகுதி IV இடையேயான சமநிலை அடிப்படை அமைப்பாக அறிவிக்கப்பட்டது)",
    [
        ("State of Madras v. Champakam Dorairajan (DPSP made subsidiary to Fundamental Rights)", "மதராஸ் மாநிலம் எதிராக செம்பகம் துரைராஜன் (அரசு நெறிமுறைக் கோட்பாடுகள் அடிப்படை உரிமைகளுக்கு துணையானவை)"),
        ("Golaknath v. State of Punjab (Fundamental Rights declared transcendental and unamendable)", "கோலக்நாத் எதிராக பஞ்சாப் மாநிலம் (அடிப்படை உரிமைகள் மாற்ற முடியாத உன்னதமானவை எனத் தீர்ப்பு)"),
        ("Kesavananda Bharati v. State of Kerala (Upheld validity of 1st part of Article 31C)", "கேசவாநந்த பாரதி எதிராக கேரள மாநிலம் (பிரிவு 31C-ன் முதல் பகுதியின் செல்லுபடித்ன்மை உறுதி செய்யப்பட்டது)"),
        ("Minerva Mills v. Union of India (Balance between Part III and Part IV declared Basic Structure)", "மினர்வா மில்ஸ் எதிராக இந்திய யூனியன் (பகுதி III மற்றும் பகுதி IV இடையேயான சமநிலை அடிப்படை அமைப்பாக அறிவிக்கப்பட்டது)")
    ],
    ["1 -> 2 -> 3 -> 4", "2 -> 1 -> 4 -> 3", "3 -> 1 -> 2 -> 4", "4 -> 2 -> 1 -> 3"],
    "A",
    "Correct Chronological Sequence: 1. Champakam Dorairajan (1951) -> 2. Golaknath (1967) -> 3. Kesavananda Bharati (1973) -> 4. Minerva Mills (1980).",
    "சரியான காலவரிசை: 1. செம்பகம் துரைராஜன் (1951) -> 2. கோலக்நாத் (1967) -> 3. கேசவாநந்த பாரதி (1973) -> 4. மினர்வா மில்ஸ் (1980).",
    {
        "A": ("Correct. 1951 -> 1967 -> 1973 -> 1980 follows the historic evolution of judicial interpretation of FR vs DPSP.", "சரி. 1951 -> 1967 -> 1973 -> 1980 என்பது அடிப்படை உரிமைகள் மற்றும் நெறிமுறைக் கோட்பாடுகளின் வரலாற்று நீதித்துறை பரிணாமத்தைப் பின்பற்றுகிறது."),
        "B": ("Incorrect. Golaknath (1967) came after Champakam Dorairajan (1951).", "தவறு. கோலக்நாத் (1967) செம்பகம் துரைராஜன் (1951) வழக்கிற்குப் பிறகே வந்தது."),
        "C": ("Incorrect. Kesavananda Bharati (1973) was decided after Golaknath (1967).", "தவறு. கேசவாநந்த பாரதி (1973) கோலக்நாத் வழக்கிற்குப் பிறகே தீர்ப்பளிக்கப்பட்டது."),
        "D": ("Incorrect. Kesavananda Bharati (1973) came after both Champakam Dorairajan and Golaknath.", "தவறு. கேசவாநந்த பாரதி (1973) செம்பகம் துரைராஜன் மற்றும் கோலக்நாத் ஆகிய இரண்டு வழக்குகளுக்கும் பிறகே வந்தது.")
    },
    "Do not confuse Golaknath (1967) and Kesavananda Bharati (1973). Parliament enacted the 24th and 25th Amendments (1971) in response to Golaknath before Kesavananda Bharati was decided in 1973.",
    "கோலக்நாத் (1967) மற்றும் கேசவாநந்த பாரதி (1973) வரிசையைக் குழப்பிக் கொள்ளக் கூடாது. கோலக்நாத் வழக்கிற்குப் பிறகே 24 மற்றும் 25-வது திருத்தங்கள் (1971) கொண்டு வரப்பட்டன.",
    "In Minerva Mills (1980), the SC emphasized that Part III (FR) and Part IV (DPSP) are two wheels of a chariot, and harmony between them is part of the Basic Structure.",
    "மினர்வா மில்ஸ் (1980) வழக்கில், பகுதி III மற்றும் பகுதி IV ஆகியவை ஒரு தேரின் இரு சக்கரங்கள் என்றும், அவற்றிற்கிடையேயான இணக்கமே அடிப்படை அமைப்பின் பகுதி என்றும் உச்சநீதிமன்றம் வலியுறுத்தியது."
))

# Q2 (Easy - B)
q_data.append(make_q(
    "DPSP_CHRONO_002", "Easy",
    "Arrange the following Constitutional Amendment Acts introducing or modifying Directive Principles of State Policy in correct chronological order:\n\n1. 42nd Constitutional Amendment Act (Added Art 39A, Art 43A, Art 48A, and modified Art 39(f))\n2. 44th Constitutional Amendment Act (Added Art 38(2) to minimise inequalities in income and status)\n3. 86th Constitutional Amendment Act (Substituted Art 45 for early childhood care and education)\n4. 97th Constitutional Amendment Act (Added Art 43B for promotion of Co-operative Societies)",
    "அரசு நெறிமுறைப்படுத்தும் கோட்பாடுகளை அறிமுகப்படுத்திய அல்லது திருத்திய பின்வரும் அரசியலமைப்பு திருத்தச் சட்டங்களைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:\n\n1. 42-வது அரசியலமைப்பு திருத்தச் சட்டம் (பிரிவுகள் 39A, 43A, 48A சேர்க்கப்பட்டு 39(f) திருத்தப்பட்டது)\n2. 44-வது அரசியலமைப்பு திருத்தச் சட்டம் (வருமானம் மற்றும் அந்தஸ்தில் உள்ள ஏற்றத்தாழ்வுகளைக் குறைக்க பிரிவு 38(2) சேர்க்கப்பட்டது)\n3. 86-வது அரசியலமைப்பு திருத்தச் சட்டம் (ஆரம்பகால குழந்தை பராமரிப்புக்காக பிரிவு 45 மாற்றியமைக்கப்பட்டது)\n4. 97-வது அரசியலமைப்பு திருத்தச் சட்டம் (கூட்டுறவு சங்கங்களை ஊக்குவிக்க பிரிவு 43B சேர்க்கப்பட்டது)",
    [
        ("42nd Constitutional Amendment Act (Added Art 39A, Art 43A, Art 48A, and modified Art 39(f))", "42-வது அரசியலமைப்பு திருத்தச் சட்டம் (பிரிவுகள் 39A, 43A, 48A சேர்க்கப்பட்டு 39(f) திருத்தப்பட்டது)"),
        ("44th Constitutional Amendment Act (Added Art 38(2) to minimise inequalities in income and status)", "44-வது அரசியலமைப்பு திருத்தச் சட்டம் (வருமானம் மற்றும் அந்தஸ்தில் உள்ள ஏற்றத்தாழ்வுகளைக் குறைக்க பிரிவு 38(2) சேர்க்கப்பட்டது)"),
        ("86th Constitutional Amendment Act (Substituted Art 45 for early childhood care and education)", "86-வது அரசியலமைப்பு திருத்தச் சட்டம் (ஆரம்பகால குழந்தை பராமரிப்புக்காக பிரிவு 45 மாற்றியமைக்கப்பட்டது)"),
        ("97th Constitutional Amendment Act (Added Art 43B for promotion of Co-operative Societies)", "97-வது அரசியலமைப்பு திருத்தச் சட்டம் (கூட்டுறவு சங்கங்களை ஊக்குவிக்க பிரிவு 43B சேர்க்கப்பட்டது)")
    ],
    ["2 -> 1 -> 4 -> 3", "1 -> 2 -> 3 -> 4", "3 -> 1 -> 2 -> 4", "4 -> 3 -> 1 -> 2"],
    "B",
    "Correct Chronological Sequence: 1. 42nd Amendment (1976) -> 2. 44th Amendment (1978) -> 3. 86th Amendment (2002) -> 4. 97th Amendment (2011).",
    "சரியான காலவரிசை: 1. 42-வது திருத்தம் (1976) -> 2. 44-வது திருத்தம் (1978) -> 3. 86-வது திருத்தம் (2002) -> 4. 97-வது திருத்தம் (2011).",
    {
        "A": ("Incorrect. 42nd Amendment (1976) came before 44th Amendment (1978).", "தவறு. 42-வது திருத்தம் (1976) 44-வது திருத்தத்திற்கு (1978) முன்பே வந்தது."),
        "B": ("Correct. 1976 -> 1978 -> 2002 -> 2011 matches the exact enactment years of DPSP constitutional amendments.", "சரி. 1976 -> 1978 -> 2002 -> 2011 DPSP அரசியலமைப்பு திருத்தங்களின் சரியான ஆண்டுகளைப் பின்பற்றுகிறது."),
        "C": ("Incorrect. 44th Amendment (1978) preceded 86th Amendment (2002).", "தவறு. 44-வது திருத்தம் (1978) 86-வது திருத்தத்திற்கு (2002) முந்தையது."),
        "D": ("Incorrect. 97th Amendment was passed in 2011, making it the latest among the list.", "தவறு. 97-வது திருத்தம் 2011-ல் நிறைவேற்றப்பட்டதால் பட்டியலில் பிந்தையது.")
    },
    "Remember that 42nd Amendment (1976) added four new DPSP provisions (39(f), 39A, 43A, 48A), while 44th Amendment (1978) added one DPSP (Article 38(2)).",
    "42-வது திருத்தம் (1976) நான்கு புதிய நெறிமுறைகளைச் சேர்த்தது (39(f), 39A, 43A, 48A), ஆனால் 44-வது திருத்தம் (1978) ஒரே ஒரு நெறிமுறையைச் சேர்த்தது (பிரிவு 38(2)).",
    "Four Constitutional Amendments (42nd, 44th, 86th, and 97th) modified Part IV of the Indian Constitution.",
    "நான்கு அரசியலமைப்பு திருத்தங்கள் (42, 44, 86 மற்றும் 97) இந்திய அரசியலமைப்பின் பகுதி IV-ஐ மாற்றியமைத்தன."
))

# Q3 (Easy - C)
q_data.append(make_q(
    "DPSP_CHRONO_003", "Easy",
    "Arrange the following DPSP constitutional developments in REVERSE chronological order (latest to earliest):\n\n1. 97th Constitutional Amendment Act (Article 43B - Co-operative Societies)\n2. 86th Constitutional Amendment Act (Article 45 substitution - Early childhood care)\n3. 73rd Constitutional Amendment Act (Article 40 implementation - Part IX Panchayati Raj)\n4. 42nd Constitutional Amendment Act (Article 39A - Free Legal Aid)",
    "பின்வரும் அரசு நெறிமுறைக் கோட்பாடு சார்ந்த அரசியலமைப்பு மாற்றங்களைத் தலைகீழ் காலவரிசைப்படி (பிந்தையது முதல் முந்தையது வரை) வரிசைப்படுத்தவும்:\n\n1. 97-வது அரசியலமைப்பு திருத்தச் சட்டம் (பிரிவு 43B - கூட்டுறவு சங்கங்கள்)\n2. 86-வது அரசியலமைப்பு திருத்தச் சட்டம் (பிரிவு 45 மாற்றம் - ஆரம்பகால குழந்தை பராமரிப்பு)\n3. 73-வது அரசியலமைப்பு திருத்தச் சட்டம் (பிரிவு 40 அமலாக்கம் - பகுதி IX பஞ்சாயத்து ராஜ்)\n4. 42-வது அரசியலமைப்பு திருத்தச் சட்டம் (பிரிவு 39A - இலவச சட்ட உதவி)",
    [
        ("97th Constitutional Amendment Act (Article 43B - Co-operative Societies)", "97-வது அரசியலமைப்பு திருத்தச் சட்டம் (பிரிவு 43B - கூட்டுறவு சங்கங்கள்)"),
        ("86th Constitutional Amendment Act (Article 45 substitution - Early childhood care)", "86-வது அரசியலமைப்பு திருத்தச் சட்டம் (பிரிவு 45 மாற்றம் - ஆரம்பகால குழந்தை பராமரிப்பு)"),
        ("73rd Constitutional Amendment Act (Article 40 implementation - Part IX Panchayati Raj)", "73-வது அரசியலமைப்பு திருத்தச் சட்டம் (பிரிவு 40 அமலாக்கம் - பகுதி IX பஞ்சாயத்து ராஜ்)"),
        ("42nd Constitutional Amendment Act (Article 39A - Free Legal Aid)", "42-வது அரசியலமைப்பு திருத்தச் சட்டம் (பிரிவு 39A - இலவச சட்ட உதவி)")
    ],
    ["4 -> 3 -> 2 -> 1", "2 -> 4 -> 1 -> 3", "1 -> 2 -> 3 -> 4", "3 -> 1 -> 4 -> 2"],
    "C",
    "Correct Reverse Chronological Sequence (Latest to Earliest): 1. 97th Amendment (2011) -> 2. 86th Amendment (2002) -> 3. 73rd Amendment (1992) -> 4. 42nd Amendment (1976).",
    "சரியான தலைகீழ் காலவரிசை (பிந்தையது முதல் முந்தையது வரை): 1. 97-வது திருத்தம் (2011) -> 2. 86-வது திருத்தம் (2002) -> 3. 73-வது திருத்தம் (1992) -> 4. 42-வது திருத்தம் (1976).",
    {
        "A": ("Incorrect. 4 -> 3 -> 2 -> 1 represents earliest to latest, not reverse chronological order.", "தவறு. 4 -> 3 -> 2 -> 1 என்பது முந்தையது முதல் பிந்தையது வரையிலான வரிசை, தலைகீழ் வரிசை அல்ல."),
        "B": ("Incorrect. 73rd Amendment (1992) is older than 86th Amendment (2002).", "தவறு. 73-வது திருத்தம் (1992) 86-வது திருத்தத்தை (2002) விட முந்தையது."),
        "C": ("Correct. 2011 (97th) -> 2002 (86th) -> 1992 (73rd) -> 1976 (42nd) correctly follows latest to earliest order.", "சரி. 2011 (97-வது) -> 2002 (86-வது) -> 1992 (73-வது) -> 1976 (42-வது) சரியான தலைகீழ் காலவரிசையைப் பின்பற்றுகிறது."),
        "D": ("Incorrect. 86th Amendment (2002) came before 97th Amendment (2011).", "தவறு. 86-வது திருத்தம் (2002) 97-வது திருத்தத்திற்கு (2011) முன்பே வந்தது.")
    },
    "Always check whether the question asks for 'earliest to latest' or 'latest to earliest' (reverse chronology).",
    "கேள்வி 'முந்தையது முதல் பிந்தையது வரை' அல்லது 'தலைகீழ் காலவரிசை (பிந்தையது முதல் முந்தையது)' எனக் கேட்கிறதா என்பதை எப்போதும் கவனமாகச் சரிபார்க்கவும்.",
    "The 73rd Amendment Act 1992 gave constitutional framework to Article 40 by adding Part IX and 11th Schedule to the Constitution.",
    "73-வது திருத்தச் சட்டம் 1992 அரசியலமைப்பில் பகுதி IX மற்றும் 11-வது அட்டவணையைச் சேர்த்து பிரிவு 40-க்கு அரசியலமைப்பு அந்தஸ்தை வழங்கியது."
))

# Q4 (Easy - D)
q_data.append(make_q(
    "DPSP_CHRONO_004", "Easy",
    "Arrange the following Supreme Court landmark judgments connected with DPSP in correct chronological order:\n\n1. State of Bombay v. F.N. Balsara (Article 47 prohibition upheld as reasonable restriction)\n2. Kesavananda Bharati v. State of Kerala (Basic structure doctrine & Article 31C limit)\n3. Minerva Mills v. Union of India (Harmony between Part III and Part IV)\n4. Unni Krishnan v. State of Andhra Pradesh (Right to education up to age 14 derived from Article 45)",
    "அரசு நெறிமுறைப்படுத்தும் கோட்பாடுகளுடன் தொடர்புடைய உச்சநீதிமன்ற முக்கியத் தீர்ப்புகளைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:\n\n1. பம்பாய் மாநிலம் எதிராக F.N. பால்சாரா (பிரிவு 47 மதுவிலக்கு நியாயமான கட்டுப்பாடாக உறுதி செய்யப்பட்டது)\n2. கேசவாநந்த பாரதி எதிராக கேரள மாநிலம் (அடிப்படை அமைப்புக் கோட்பாடு & பிரிவு 31C வரம்பு)\n3. மினர்வா மில்ஸ் எதிராக இந்திய யூனியன் (பகுதி III மற்றும் பகுதி IV இடையேயான இணக்கம்)\n4. உன்னிகிருஷ்ணன் எதிராக ஆந்திரப் பிரதேச மாநிலம் (பிரிவு 45-லிருந்து 14 வயது வரையிலான கல்வி உரிமை பெறப்பட்டது)",
    [
        ("State of Bombay v. F.N. Balsara (Article 47 prohibition upheld as reasonable restriction)", "பம்பாய் மாநிலம் எதிராக F.N. பால்சாரா (பிரிவு 47 மதுவிலக்கு நியாயமான கட்டுப்பாடாக உறுதி செய்யப்பட்டது)"),
        ("Kesavananda Bharati v. State of Kerala (Basic structure doctrine & Article 31C limit)", "கேசவாநந்த பாரதி எதிராக கேரள மாநிலம் (அடிப்படை அமைப்புக் கோட்பாடு & பிரிவு 31C வரம்பு)"),
        ("Minerva Mills v. Union of India (Harmony between Part III and Part IV)", "மினர்வா மில்ஸ் எதிராக இந்திய யூனியன் (பகுதி III மற்றும் பகுதி IV இடையேயான இணக்கம்)"),
        ("Unni Krishnan v. State of Andhra Pradesh (Right to education up to age 14 derived from Article 45)", "உன்னிகிருஷ்ணன் எதிராக ஆந்திரப் பிரதேச மாநிலம் (பிரிவு 45-லிருந்து 14 வயது வரையிலான கல்வி உரிமை பெறப்பட்டது)")
    ],
    ["2 -> 1 -> 4 -> 3", "3 -> 1 -> 2 -> 4", "4 -> 2 -> 1 -> 3", "1 -> 2 -> 3 -> 4"],
    "D",
    "Correct Chronological Sequence: 1. F.N. Balsara (1951) -> 2. Kesavananda Bharati (1973) -> 3. Minerva Mills (1980) -> 4. Unni Krishnan (1993).",
    "சரியான காலவரிசை: 1. எஃப்.என். பால்சாரா (1951) -> 2. கேசவாநந்த பாரதி (1973) -> 3. மினர்வா மில்ஸ் (1980) -> 4. உன்னிகிருஷ்ணன் (1993).",
    {
        "A": ("Incorrect. F.N. Balsara (1951) was decided much before Kesavananda Bharati (1973).", "தவறு. எஃப்.என். பால்சாரா (1951) கேசவாநந்த பாரதி (1973) வழக்கிற்கு பல ஆண்டுகளுக்கு முன்பே தீர்ப்பளிக்கப்பட்டது."),
        "B": ("Incorrect. Kesavananda Bharati (1973) preceded Minerva Mills (1980).", "தவறு. கேசவாநந்த பாரதி (1973) மினர்வா மில்ஸ் (1980) வழக்கிற்கு முந்தையது."),
        "C": ("Incorrect. Minerva Mills (1980) came after Balsara (1951) and Kesavananda Bharati (1973).", "தவறு. மினர்வா மில்ஸ் (1980) பால்சாரா மற்றும் கேசவாநந்த பாரதி வழக்குகளுக்குப் பிறகே வந்தது."),
        "D": ("Correct. 1951 -> 1973 -> 1980 -> 1993 follows the verified chronological sequence of DPSP case law.", "சரி. 1951 -> 1973 -> 1980 -> 1993 DPSP தொடர்பான வழக்குத் தீர்ப்புகளின் சரியான காலவரிசையைப் பின்பற்றுகிறது.")
    },
    "In F.N. Balsara (1951), the SC held that enforcing prohibition under Article 47 constitutes a reasonable restriction under Article 19(6).",
    "எஃப்.என். பால்சாரா (1951) வழக்கில், பிரிவு 47-ன் கீழ் மதுவிலக்கை அமல்படுத்துவது பிரிவு 19(6)-ன் கீழ் நியாயமான கட்டுப்பாடு என உச்சநீதிமன்றம் தீர்ப்பளித்தது.",
    "Unni Krishnan (1993) directly paved the way for the 86th Amendment Act 2002 and Article 21A.",
    "உன்னிகிருஷ்ணன் (1993) வழக்கு 86-வது திருத்தச் சட்டம் 2002 மற்றும் பிரிவு 21A உருவாக்கத்திற்கு நேரடியாக வழிவகுத்தது."
))

# Q5 (Easy - A)
q_data.append(make_q(
    "DPSP_CHRONO_005", "Easy",
    "Arrange the following historic foundations and developments of DPSP in correct chronological sequence:\n\n1. Sapru Committee Report (Recommended non-justiciable directive rights)\n2. Objectives Resolution moved by Jawaharlal Nehru (Formulated social-economic justice goals)\n3. Adoption of Constitution of India (Enactment of Part IV Directive Principles)\n4. 42nd Constitutional Amendment Act (Added socialist directives Art 39A and Art 43A)",
    "அரசு நெறிமுறைப்படுத்தும் கோட்பாடுகளின் வரலாற்று தொடக்கம் மற்றும் வளர்ச்சியைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:\n\n1. சப்ரு குழு அறிக்கை (நீதிமன்றத்தால் அமல்படுத்த முடியாத நெறிமுறை உரிமைகளைப் பரிந்துரைத்தது)\n2. ஜவஹர்லால் நேருவால் கொண்டுவரப்பட்ட குறிக்கோள்கள் தீர்மானம் (சமூக-பொருளாதார நீதி இலக்குகளை உருவாக்கியது)\n3. இந்திய அரசியலமைப்பு ஏற்றுக்கொள்ளப்படுதல் (பகுதி IV அரசு நெறிமுறைக் கோட்பாடுகள் இயற்றப்படல்)\n4. 42-வது அரசியலமைப்பு திருத்தச் சட்டம் (சோசலிச நெறிமுறைகளான பிரிவு 39A மற்றும் 43A சேர்க்கப்படல்)",
    [
        ("Sapru Committee Report (Recommended non-justiciable directive rights)", "சப்ரு குழு அறிக்கை (நீதிமன்றத்தால் அமல்படுத்த முடியாத நெறிமுறை உரிமைகளைப் பரிந்துரைத்தது)"),
        ("Objectives Resolution moved by Jawaharlal Nehru (Formulated social-economic justice goals)", "ஜவஹர்லால் நேருவால் கொண்டுவரப்பட்ட குறிக்கோள்கள் தீர்மானம் (சமூக-பொருளாதார நீதி இலக்குகளை உருவாக்கியது)"),
        ("Adoption of Constitution of India (Enactment of Part IV Directive Principles)", "இந்திய அரசியலமைப்பு ஏற்றுக்கொள்ளப்படுதல் (பகுதி IV அரசு நெறிமுறைக் கோட்பாடுகள் இயற்றப்படல்)"),
        ("42nd Constitutional Amendment Act (Added socialist directives Art 39A and Art 43A)", "42-வது அரசியலமைப்பு திருத்தச் சட்டம் (சோசலிச நெறிமுறைகளான பிரிவு 39A மற்றும் 43A சேர்க்கப்படல்)")
    ],
    ["1 -> 2 -> 3 -> 4", "2 -> 1 -> 4 -> 3", "3 -> 2 -> 1 -> 4", "4 -> 1 -> 3 -> 2"],
    "A",
    "Correct Chronological Sequence: 1. Sapru Committee Report (1945) -> 2. Objectives Resolution (Dec 1946) -> 3. Adoption of Constitution (Nov 1949 / Jan 1950) -> 4. 42nd Amendment (1976).",
    "சரியான காலவரிசை: 1. சப்ரு குழு அறிக்கை (1945) -> 2. குறிக்கோள்கள் தீர்மானம் (டிசம்பர் 1946) -> 3. அரசியலமைப்பு ஏற்றுக்கொள்ளப்படுதல் (1949/1950) -> 4. 42-வது திருத்தம் (1976).",
    {
        "A": ("Correct. 1945 -> 1946 -> 1950 -> 1976 follows the exact historic trajectory of DPSP conceptualisation.", "சரி. 1945 -> 1946 -> 1950 -> 1976 அரசு நெறிமுறைக் கோட்பாடுகளின் கருத்து உருவாக்கத்தின் சரியான வரலாற்றுப் பாதையைப் பின்பற்றுகிறது."),
        "B": ("Incorrect. Sapru Committee Report (1945) came before Nehru's Objectives Resolution (Dec 1946).", "தவறு. சப்ரு குழு அறிக்கை (1945) நேருவின் குறிக்கோள்கள் தீர்மானத்திற்கு (டிசம்பர் 1946) முன்பே வந்தது."),
        "C": ("Incorrect. Objectives Resolution (1946) preceded the adoption of the Constitution in 1949/1950.", "தவறு. குறிக்கோள்கள் தீர்மானம் (1946) அரசியலமைப்பு ஏற்றுக்கொள்ளப்பட்டதற்கு (1949/1950) முந்தையது."),
        "D": ("Incorrect. Sapru Committee Report (1945) was published long before the Constitution was adopted.", "தவறு. சப்ரு குழு அறிக்கை (1945) அரசியலமைப்பு ஏற்றுக்கொள்ளப்படுவதற்கு முன்பே வெளியிடப்பட்டது.")
    },
    "Sir Tej Bahadur Sapru Committee (1945) recommended dividing fundamental rights into two classes: justiciable (Part III) and non-justiciable (Part IV).",
    "சர் தேஜ் பகதூர் சப்ரு குழு (1945) அடிப்படை உரிமைகளை இரண்டு பிரிவுகளாகப் பிரிக்க பரிந்துரைத்தது: நீதிமன்றத்தால் அமல்படுத்தக்கூடியவை (பகுதி III) மற்றும் நீதிமன்றத்தால் அமல்படுத்த முடியாதவை (பகுதி IV).",
    "The DPSP framework was modeled after the Irish Constitution of 1937, which had copied it from the Spanish Constitution.",
    "அரசு நெறிமுறைப்படுத்தும் கோட்பாடுகள் 1937-ம் ஆண்டின் அயர்லாந்து அரசியலமைப்பிலிருந்து பெறப்பட்டவை."
))

# Q6 (Medium - B)
q_data.append(make_q(
    "DPSP_CHRONO_006", "Medium",
    "Arrange the following Constitutional Amendments introducing new Articles into Part IV in correct chronological order:\n\n1. 25th Amendment Act (Inserted Article 31C giving primacy to Article 39(b) and (c))\n2. 42nd Amendment Act (Inserted Articles 39A, 43A, and 48A into Part IV)\n3. 44th Amendment Act (Inserted Article 38(2) directing State to minimise inequalities)\n4. 97th Amendment Act (Inserted Article 43B promoting Co-operative Societies)",
    "பகுதி IV-ல் புதிய பிரிவுகளை அறிமுகப்படுத்திய பின்வரும் அரசியலமைப்பு திருத்தங்களைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:\n\n1. 25-வது திருத்தச் சட்டம் (பிரிவு 39(b) மற்றும் (c)-க்கு முதன்மை அளிக்கும் பிரிவு 31C சேர்க்கப்பட்டது)\n2. 42-வது திருத்தச் சட்டம் (பகுதி IV-ல் பிரிவுகள் 39A, 43A மற்றும் 48A சேர்க்கப்பட்டன)\n3. 44-வது திருத்தச் சட்டம் (ஏற்றத்தாழ்வுகளைக் குறைக்க அரசைப் பணிக்கும் பிரிவு 38(2) சேர்க்கப்பட்டது)\n4. 97-வது திருத்தச் சட்டம் (கூட்டுறவு சங்கங்களை ஊக்குவிக்கும் பிரிவு 43B சேர்க்கப்பட்டது)",
    [
        ("25th Amendment Act (Inserted Article 31C giving primacy to Article 39(b) and (c))", "25-வது திருத்தச் சட்டம் (பிரிவு 39(b) மற்றும் (c)-க்கு முதன்மை அளிக்கும் பிரிவு 31C சேர்க்கப்பட்டது)"),
        ("42nd Amendment Act (Inserted Articles 39A, 43A, and 48A into Part IV)", "42-வது திருத்தச் சட்டம் (பகுதி IV-ல் பிரிவுகள் 39A, 43A மற்றும் 48A சேர்க்கப்பட்டன)"),
        ("44th Amendment Act (Inserted Article 38(2) directing State to minimise inequalities)", "44-வது திருத்தச் சட்டம் (ஏற்றத்தாழ்வுகளைக் குறைக்க அரசைப் பணிக்கும் பிரிவு 38(2) சேர்க்கப்பட்டது)"),
        ("97th Amendment Act (Inserted Article 43B promoting Co-operative Societies)", "97-வது திருத்தச் சட்டம் (கூட்டுறவு சங்கங்களை ஊக்குவிக்கும் பிரிவு 43B சேர்க்கப்பட்டது)")
    ],
    ["2 -> 1 -> 4 -> 3", "1 -> 2 -> 3 -> 4", "3 -> 1 -> 2 -> 4", "4 -> 2 -> 1 -> 3"],
    "B",
    "Correct Chronological Sequence: 1. 25th Amendment (1971) -> 2. 42nd Amendment (1976) -> 3. 44th Amendment (1978) -> 4. 97th Amendment (2011).",
    "சரியான காலவரிசை: 1. 25-வது திருத்தம் (1971) -> 2. 42-வது திருத்தம் (1976) -> 3. 44-வது திருத்தம் (1978) -> 4. 97-வது திருத்தம் (2011).",
    {
        "A": ("Incorrect. 25th Amendment (1971) preceded the 42nd Amendment (1976).", "தவறு. 25-வது திருத்தம் (1971) 42-வது திருத்தத்திற்கு (1976) முந்தையது."),
        "B": ("Correct. 1971 -> 1976 -> 1978 -> 2011 represents the exact sequence of amendments modifying Part IV.", "சரி. 1971 -> 1976 -> 1978 -> 2011 என்பது பகுதி IV-ஐ மாற்றியமைத்த திருத்தங்களின் சரியான வரிசையாகும்."),
        "C": ("Incorrect. 42nd Amendment (1976) came before 44th Amendment (1978).", "தவறு. 42-வது திருத்தம் (1976) 44-வது திருத்தத்திற்கு (1978) முன்பே வந்தது."),
        "D": ("Incorrect. 44th Amendment (1978) came after 25th Amendment (1971).", "தவறு. 44-வது திருத்தம் (1978) 25-வது திருத்தத்திற்கு (1971) பிறகே வந்தது.")
    },
    "Do not confuse 25th Amendment (1971) with 42nd Amendment (1976). The 25th Amendment introduced Article 31C to protect laws enforcing Article 39(b) and (c).",
    "25-வது திருத்தம் (1971) மற்றும் 42-வது திருத்தம் (1976) ஆகியவற்றை குழப்பிக் கொள்ளக் கூடாது. 25-வது திருத்தம் பிரிவு 39(b) மற்றும் (c)-ஐ அமல்படுத்தும் சட்டங்களைப் பாதுகாக்க பிரிவு 31C-ஐ அறிமுகப்படுத்தியது.",
    "Article 31C created an exception to Articles 14 and 19 by stating that no law giving effect to Article 39(b) or (c) shall be declared void on ground of violating Article 14 or 19.",
    "பிரிவு 39(b) அல்லது (c)-ஐ அமல்படுத்தும் எந்தவொரு சட்டமும் பிரிவு 14 அல்லது 19-ஐ மீறுகிறது என்ற அடிப்படையில் செல்லாது என அறிவிக்க முடியாது என்ற விலக்கை பிரிவு 31C உருவாக்கியது."
))

# Q7 (Medium - C)
q_data.append(make_q(
    "DPSP_CHRONO_007", "Medium",
    "Arrange the following events concerning the constitutional evolution of Article 31C and DPSP primacy in correct chronological order:\n\n1. Enactment of 25th Amendment Act (Inserted 1st part of Article 31C protecting Art 39(b) & (c))\n2. Kesavananda Bharati Judgment (Upheld 1st part of Art 31C, struck down 2nd part excluding judicial review)\n3. Enactment of 42nd Amendment Act (Attempted to extend Art 31C protection to ALL Directive Principles)\n4. Minerva Mills Judgment (Struck down 42nd Amendment extension to Art 31C as unconstitutional)",
    "பிரிவு 31C மற்றும் அரசு நெறிமுறைக் கோட்பாடுகளின் முதன்மைத்தன்மை பற்றிய அரசியலமைப்பு மாற்றங்களைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:\n\n1. 25-வது திருத்தச் சட்டம் இயற்றப்படல் (பிரிவு 39(b) & (c)-ஐப் பாதுகாக்கும் பிரிவு 31C-ன் முதல் பகுதி சேர்க்கப்பட்டது)\n2. கேசவாநந்த பாரதி தீர்ப்பு (பிரிவு 31C-ன் முதல் பகுதியை உறுதி செய்து, நீதிமன்ற ஆய்வைத் தடுக்கும் 2-வது பகுதியை ரத்து செய்தது)\n3. 42-வது திருத்தச் சட்டம் இயற்றப்படல் (அனைத்து அரசு நெறிமுறைக் கோட்பாடுகளுக்கும் பிரிவு 31C பாதுகாப்பை விரிவாக்க முயன்றது)\n4. மினர்வா மில்ஸ் தீர்ப்பு (பிரிவு 31C-ன் 42-வது திருத்த விரிவாக்கத்தை அரசியலமைப்புக்கு எதிரானது என ரத்து செய்தது)",
    [
        ("Enactment of 25th Amendment Act (Inserted 1st part of Article 31C protecting Art 39(b) & (c))", "25-வது திருத்தச் சட்டம் இயற்றப்படல் (பிரிவு 39(b) & (c)-ஐப் பாதுகாக்கும் பிரிவு 31C-ன் முதல் பகுதி சேர்க்கப்பட்டது)"),
        ("Kesavananda Bharati Judgment (Upheld 1st part of Art 31C, struck down 2nd part excluding judicial review)", "கேசவாநந்த பாரதி தீர்ப்பு (பிரிவு 31C-ன் முதல் பகுதியை உறுதி செய்து, நீதிமன்ற ஆய்வைத் தடுக்கும் 2-வது பகுதியை ரத்து செய்தது)"),
        ("Enactment of 42nd Amendment Act (Attempted to extend Art 31C protection to ALL Directive Principles)", "42-வது திருத்தச் சட்டம் இயற்றப்படல் (அனைத்து அரசு நெறிமுறைக் கோட்பாடுகளுக்கும் பிரிவு 31C பாதுகாப்பை விரிவாக்க முயன்றது)"),
        ("Minerva Mills Judgment (Struck down 42nd Amendment extension to Art 31C as unconstitutional)", "மினர்வா மில்ஸ் தீர்ப்பு (பிரிவு 31C-ன் 42-வது திருத்த விரிவாக்கத்தை அரசியலமைப்புக்கு எதிரானது என ரத்து செய்தது)")
    ],
    ["2 -> 1 -> 4 -> 3", "3 -> 1 -> 2 -> 4", "1 -> 2 -> 3 -> 4", "4 -> 2 -> 1 -> 3"],
    "C",
    "Correct Chronological Sequence: 1. 25th Amendment (1971) -> 2. Kesavananda Bharati (1973) -> 3. 42nd Amendment (1976) -> 4. Minerva Mills (1980).",
    "சரியான காலவரிசை: 1. 25-வது திருத்தம் (1971) -> 2. கேசவாநந்த பாரதி (1973) -> 3. 42-வது திருத்தம் (1976) -> 4. மினர்வா மில்ஸ் (1980).",
    {
        "A": ("Incorrect. 25th Amendment (1971) came before Kesavananda Bharati (1973).", "தவறு. 25-வது திருத்தம் (1971) கேசவாநந்த பாரதி (1973) வழக்கிற்கு முன்பே வந்தது."),
        "B": ("Incorrect. 42nd Amendment (1976) was passed after Kesavananda Bharati (1973).", "தவறு. 42-வது திருத்தம் (1976) கேசவாநந்த பாரதி (1973) வழக்கிற்குப் பிறகே நிறைவேற்றப்பட்டது."),
        "C": ("Correct. 1971 -> 1973 -> 1976 -> 1980 represents the true interplay of constitutional amendments and Supreme Court rulings on Article 31C.", "சரி. 1971 -> 1973 -> 1976 -> 1980 பிரிவு 31C பற்றிய அரசியலமைப்பு திருத்தங்கள் மற்றும் உச்சநீதிமன்றத் தீர்ப்புகளின் சரியான தொடர்பைப் பிரதிபலிக்கிறது."),
        "D": ("Incorrect. 42nd Amendment (1976) came after 25th Amendment (1971).", "தவறு. 42-வது திருத்தம் (1976) 25-வது திருத்தத்திற்கு (1971) பிறகே வந்தது.")
    },
    "In Kesavananda Bharati (1973), the SC held that judicial review is part of the Basic Structure, so the second clause of Article 31C ('no law containing such declaration shall be called in question in any court') was declared invalid.",
    "கேசவாநந்த பாரதி (1973) வழக்கில், நீதிமன்ற ஆய்வு அடிப்படை அமைப்பின் பகுதி எனத் தீர்ப்பளிக்கப்பட்டதால், பிரிவு 31C-ன் இரண்டாவது வாக்கியம் ரத்து செய்யப்பட்டது.",
    "Presently, Article 31C protects ONLY laws implementing Article 39(b) and Article 39(c) against Articles 14 and 19.",
    "தற்போது, பிரிவு 31C பிரிவு 39(b) மற்றும் பிரிவு 39(c)-ஐ அமல்படுத்தும் சட்டங்களை மட்டுமே பிரிவுகள் 14 மற்றும் 19-க்கு எதிராகப் பாதுகாக்கிறது."
))

# Q8 (Medium - D)
q_data.append(make_q(
    "DPSP_CHRONO_008", "Medium",
    "Arrange the following landmark Supreme Court judgments expanding socio-economic DPSP goals into Article 21 in correct chronological order:\n\n1. Hussainara Khatoon v. Home Secretary, Bihar (Right to free legal aid under Art 39A integrated into Art 21)\n2. Randhir Singh v. Union of India (Equal Pay for Equal Work under Art 39(d) read with Art 14 & 21)\n3. Bandhua Mukti Morcha v. Union of India (Humane working conditions under Art 42 integrated into Art 21)\n4. Olga Tellis v. Bombay Municipal Corporation (Right to livelihood derived from Art 39(a) and Art 41)",
    "அரசு நெறிமுறைக் கோட்பாடுகளின் சமூக-பொருளாதார இலக்குகளைப் பிரிவு 21-ல் விரிவுபடுத்திய முக்கிய உச்சநீதிமன்றத் தீர்ப்புகளைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:\n\n1. ஹுசைனாரா கதூன் எதிராக பீகார் உள்துறைச் செயலர் (பிரிவு 39A-ன் இலவச சட்ட உதவி பிரிவு 21-ல் இணைக்கப்பட்டது)\n2. ரந்தீர் சிங் எதிராக இந்திய யூனியன் (பிரிவு 39(d)-ன் சம வேலைக்கு சம ஊதியம் பிரிவு 14 & 21 உடன் இணைக்கப்பட்டது)\n3. பந்துவா முக்தி மோர்ச்சா எதிராக இந்திய யூனியன் (பிரிவு 42-ன் மனிதத்தன்மையான பணிச்சூழல் பிரிவு 21-ல் இணைக்கப்பட்டது)\n4. ஓல்கா டெல்லிஸ் எதிராக பம்பாய் மாநகராட்சி (பிரிவு 39(a) மற்றும் 41-லிருந்து வாழ்வாதார உரிமை பெறப்பட்டது)",
    [
        ("Hussainara Khatoon v. Home Secretary, Bihar (Right to free legal aid under Art 39A integrated into Art 21)", "ஹுசைனாரா கதூன் எதிராக பீகார் உள்துறைச் செயலர் (பிரிவு 39A-ன் இலவச சட்ட உதவி பிரிவு 21-ல் இணைக்கப்பட்டது)"),
        ("Randhir Singh v. Union of India (Equal Pay for Equal Work under Art 39(d) read with Art 14 & 21)", "ரந்தீர் சிங் எதிராக இந்திய யூனியன் (பிரிவு 39(d)-ன் சம வேலைக்கு சம ஊதியம் பிரிவு 14 & 21 உடன் இணைக்கப்பட்டது)"),
        ("Bandhua Mukti Morcha v. Union of India (Humane working conditions under Art 42 integrated into Art 21)", "பந்துவா முக்தி மோர்ச்சா எதிராக இந்திய யூனியன் (பிரிவு 42-ன் மனிதத்தன்மையான பணிச்சூழல் பிரிவு 21-ல் இணைக்கப்பட்டது)"),
        ("Olga Tellis v. Bombay Municipal Corporation (Right to livelihood derived from Art 39(a) and Art 41)", "ஓல்கா டெல்லிஸ் எதிராக பம்பாய் மாநகராட்சி (பிரிவு 39(a) மற்றும் 41-லிருந்து வாழ்வாதார உரிமை பெறப்பட்டது)")
    ],
    ["2 -> 1 -> 4 -> 3", "3 -> 1 -> 2 -> 4", "4 -> 2 -> 1 -> 3", "1 -> 2 -> 3 -> 4"],
    "D",
    "Correct Chronological Sequence: 1. Hussainara Khatoon (1979) -> 2. Randhir Singh (1982) -> 3. Bandhua Mukti Morcha (1984) -> 4. Olga Tellis (1985).",
    "சரியான காலவரிசை: 1. ஹுசைனாரா கதூன் (1979) -> 2. ரந்தீர் சிங் (1982) -> 3. பந்துவா முக்தி மோர்ச்சா (1984) -> 4. ஓல்கா டெல்லிஸ் (1985).",
    {
        "A": ("Incorrect. Hussainara Khatoon (1979) was decided before Randhir Singh (1982).", "தவறு. ஹுசைனாரா கதூன் (1979) ரந்தீர் சிங் (1982) வழக்கிற்கு முன்பே தீர்ப்பளிக்கப்பட்டது."),
        "B": ("Incorrect. Bandhua Mukti Morcha (1984) came after Randhir Singh (1982).", "தவறு. பந்துவா முக்தி மோர்ச்சா (1984) ரந்தீர் சிங் (1982) வழக்கிற்குப் பிறகே வந்தது."),
        "C": ("Incorrect. Bandhua Mukti Morcha (1984) came after Hussainara Khatoon (1979).", "தவறு. பந்துவா முக்தி மோர்ச்சா (1984) ஹுசைனாரா கதூன் (1979) வழக்கிற்குப் பிறகே வந்தது."),
        "D": ("Correct. 1979 -> 1982 -> 1984 -> 1985 matches the exact sequence of judicial decisions reading DPSP into Fundamental Rights under Article 21.", "சரி. 1979 -> 1982 -> 1984 -> 1985 அரசு நெறிமுறைக் கோட்பாடுகளைப் பிரிவு 21-ன் கீழ் அடிப்படை உரிமைகளாகப் படித்த உச்சநீதிமன்றத்தின் சரியான தீர்ப்பு வரிசையாகும்.")
    },
    "In Randhir Singh (1982), Supreme Court held that 'Equal Pay for Equal Work' is not a mere DPSP slogan but a constitutional goal enforceable through Article 14 and Article 21.",
    "ரந்தீர் சிங் (1982) வழக்கில், 'சம வேலைக்கு சம ஊதியம்' என்பது வெறும் அரசு நெறிமுறைக் கோட்பாட்டு முழக்கம் மட்டுமல்ல, அது பிரிவு 14 மற்றும் 21 மூலம் அமல்படுத்தக்கூடிய அரசியலமைப்பு இலக்கு என உச்சநீதிமன்றம் தீர்ப்பளித்தது.",
    "In Olga Tellis (1985), the Supreme Court ruled that the right to life in Article 21 includes the right to livelihood, deriving support from Articles 39(a) and 41.",
    "ஓல்கா டெல்லிஸ் (1985) வழக்கில், பிரிவு 21-ன் வாழ்வுரிமையில் வாழ்வாதார உரிமையும் அடங்கும் என பிரிவுகள் 39(a) மற்றும் 41-ன் அடிப்படையில் உச்சநீதிமன்றம் தீர்ப்பளித்தது."
))

# Q9 (Medium - A)
q_data.append(make_q(
    "DPSP_CHRONO_009", "Medium",
    "Arrange the following milestones in the historical evolution of Article 45 and Right to Education in correct chronological order:\n\n1. Inclusion of original Article 45 in Constitution (Free & compulsory education for children up to 14 years within 10 years)\n2. Unni Krishnan Judgment (Supreme Court held Right to Education is a Fundamental Right up to age 14 derived from Article 45)\n3. 86th Constitutional Amendment Act (Substituted Article 45 for early childhood care and added Article 21A)\n4. Enactment of Right to Education (RTE) Act (Statutory enforcement of Article 21A)",
    "பிரிவு 45 மற்றும் கல்வி உரிமையின் வரலாற்று வளர்ச்சியில் உள்ள பின்வரும் மைல்கற்களைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:\n\n1. அரசியலமைப்பில் மூலப் பிரிவு 45 சேர்க்கப்படல் (10 ஆண்டுகளுக்குள் 14 வயது வரையிலான குழந்தைகளுக்கு இலவச கட்டாயக் கல்வி)\n2. உன்னிகிருஷ்ணன் வழக்கு தீர்ப்பு (பிரிவு 45-லிருந்து 14 வயது வரையிலான கல்வி உரிமை அடிப்படை உரிமை என உச்சநீதிமன்றம் தீர்ப்பு)\n3. 86-வது அரசியலமைப்பு திருத்தச் சட்டம் (ஆரம்பகால குழந்தை பராமரிப்புக்காக பிரிவு 45 மாற்றப்பட்டு பிரிவு 21A சேர்க்கப்பட்டது)\n4. இலவச கட்டாயக் கல்வி உரிமை (RTE) சட்டம் இயற்றப்படல் (பிரிவு 21A-ன் சட்டப்பூர்வ அமலாக்கம்)",
    [
        ("Inclusion of original Article 45 in Constitution (Free & compulsory education for children up to 14 years within 10 years)", "அரசியலமைப்பில் மூலப் பிரிவு 45 சேர்க்கப்படல் (10 ஆண்டுகளுக்குள் 14 வயது வரையிலான குழந்தைகளுக்கு இலவச கட்டாயக் கல்வி)"),
        ("Unni Krishnan Judgment (Supreme Court held Right to Education is a Fundamental Right up to age 14 derived from Article 45)", "உன்னிகிருஷ்ணன் வழக்கு தீர்ப்பு (பிரிவு 45-லிருந்து 14 வயது வரையிலான கல்வி உரிமை அடிப்படை உரிமை என உச்சநீதிமன்றம் தீர்ப்பு)"),
        ("86th Constitutional Amendment Act (Substituted Article 45 for early childhood care and added Article 21A)", "86-வது அரசியலமைப்பு திருத்தச் சட்டம் (ஆரம்பகால குழந்தை பராமரிப்புக்காக பிரிவு 45 மாற்றப்பட்டு பிரிவு 21A சேர்க்கப்பட்டது)"),
        ("Enactment of Right to Education (RTE) Act (Statutory enforcement of Article 21A)", "இலவச கட்டாயக் கல்வி உரிமை (RTE) சட்டம் இயற்றப்படல் (பிரிவு 21A-ன் சட்டப்பூர்வ அமலாக்கம்)")
    ],
    ["1 -> 2 -> 3 -> 4", "2 -> 1 -> 4 -> 3", "3 -> 1 -> 2 -> 4", "4 -> 3 -> 1 -> 2"],
    "A",
    "Correct Chronological Sequence: 1. Original Constitution (1950) -> 2. Unni Krishnan Case (1993) -> 3. 86th Amendment (2002) -> 4. RTE Act (2009).",
    "சரியான காலவரிசை: 1. மூல அரசியலமைப்பு (1950) -> 2. உன்னிகிருஷ்ணன் வழக்கு (1993) -> 3. 86-வது திருத்தம் (2002) -> 4. RTE சட்டம் (2009).",
    {
        "A": ("Correct. 1950 -> 1993 -> 2002 -> 2009 traces the exact transformation of Article 45 directive into Article 21A Fundamental Right.", "சரி. 1950 -> 1993 -> 2002 -> 2009 என்பது பிரிவு 45 நெறிமுறை பிரிவு 21A அடிப்படை உரிமையாக மாறிய சரியான வரலாற்றுப் பாதையாகும்."),
        "B": ("Incorrect. Unni Krishnan case was decided in 1993, long after the Constitution was enacted in 1950.", "தவறு. உன்னிகிருஷ்ணன் வழக்கு 1993-ல் தீர்ப்பளிக்கப்பட்டது, இது 1950 அரசியலமைப்பு இயற்றப்பட்டதற்கு பல ஆண்டுகளுக்குப் பிந்தையது."),
        "C": ("Incorrect. 86th Amendment (2002) was enacted after the Unni Krishnan decision (1993).", "தவறு. 86-வது திருத்தம் (2002) உன்னிகிருஷ்ணன் தீர்ப்பிற்குப் (1993) பிறகே இயற்றப்பட்டது."),
        "D": ("Incorrect. 86th Amendment (2002) came after 1950 and 1993.", "தவறு. 86-வது திருத்தம் (2002) 1950 மற்றும் 1993-க்கு பிறகே வந்தது.")
    },
    "Notice the shift in Article 45: Original Article 45 covered education up to 14 years. After 86th Amendment (2002), Article 45 covers early childhood care and education below 6 years, while 6 to 14 years moved to Article 21A.",
    "பிரிவு 45-ன் மாற்றத்தைக் கவனிக்கவும்: மூலப் பிரிவு 45 14 வயது வரையிலான கல்வியைக் குறித்தது. 86-வது திருத்தத்திற்கு (2002) பிறகு, பிரிவு 45 6 வயதிற்குட்பட்ட குழந்தை பராமரிப்பைக் குறிக்கிறது, 6 முதல் 14 வயது வரை பிரிவு 21A-க்கு மாற்றப்பட்டது.",
    "The Right of Children to Free and Compulsory Education (RTE) Act was enacted in 2009 and came into force on April 1, 2010.",
    "இலவச கட்டாயக் கல்வி உரிமைச் சட்டம் 2009-ல் இயற்றப்பட்டு ஏப்ரல் 1, 2010 அன்று அமலுக்கு வந்தது."
))

# Q10 (Medium - B)
q_data.append(make_q(
    "DPSP_CHRONO_010", "Medium",
    "Arrange the following judicial rulings on Directive Principles interpretation in correct chronological order:\n\n1. Minerva Mills v. Union of India (Harmony between Part III and Part IV as basic structure)\n2. Bandhua Mukti Morcha v. Union of India (Bonded labor abolition under Art 21 read with Art 39(e)/42)\n3. Unni Krishnan v. State of Andhra Pradesh (Free education up to 14 years derived from Art 45)\n4. State of Gujarat v. Mirzapur Moti Kureshi Kassab Jamat (Total ban on cow slaughter upheld under Art 48 & 48A)",
    "அரசு நெறிமுறைப்படுத்தும் கோட்பாடுகள் விளக்கம் தொடர்பான பின்வரும் நீதிமன்றத் தீர்ப்புகளைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:\n\n1. மினர்வா மில்ஸ் எதிராக இந்திய யூனியன் (பகுதி III மற்றும் IV இடையேயான இணக்கம் அடிப்படை அமைப்பு)\n2. பந்துவா முக்தி மோர்ச்சா எதிராக இந்திய யூனியன் (பிரிவு 39(e)/42 உடன் இணைந்து பிரிவு 21-ன் கீழ் கொத்தடிமை ஒழிப்பு)\n3. உன்னிகிருஷ்ணன் எதிராக ஆந்திரப் பிரதேச மாநிலம் (பிரிவு 45-லிருந்து 14 வயது வரையிலான இலவசக் கல்வி)\n4. குஜராத் மாநிலம் எதிராக மிர்சாபூர் மோதி குரேஷி கசாப் ஜமாத் (பிரிவு 48 & 48A-ன் கீழ் பசு வதை முழு தடை உறுதிப்படுத்தப்படல்)",
    [
        ("Minerva Mills v. Union of India (Harmony between Part III and Part IV as basic structure)", "மினர்வா மில்ஸ் எதிராக இந்திய யூனியன் (பகுதி III மற்றும் IV இடையேயான இணக்கம் அடிப்படை அமைப்பு)"),
        ("Bandhua Mukti Morcha v. Union of India (Bonded labor abolition under Art 21 read with Art 39(e)/42)", "பந்துவா முக்தி மோர்ச்சா எதிராக இந்திய யூனியன் (பிரிவு 39(e)/42 உடன் இணைந்து பிரிவு 21-ன் கீழ் கொத்தடிமை ஒழிப்பு)"),
        ("Unni Krishnan v. State of Andhra Pradesh (Free education up to 14 years derived from Art 45)", "உன்னிகிருஷ்ணன் எதிராக ஆந்திரப் பிரதேச மாநிலம் (பிரிவு 45-லிருந்து 14 வயது வரையிலான இலவசக் கல்வி)"),
        ("State of Gujarat v. Mirzapur Moti Kureshi Kassab Jamat (Total ban on cow slaughter upheld under Art 48 & 48A)", "குஜராத் மாநிலம் எதிராக மிர்சாபூர் மோதி குரேஷி கசாப் ஜமாத் (பிரிவு 48 & 48A-ன் கீழ் பசு வதை முழு தடை உறுதிப்படுத்தப்படல்)")
    ],
    ["2 -> 1 -> 4 -> 3", "1 -> 2 -> 3 -> 4", "3 -> 1 -> 2 -> 4", "4 -> 3 -> 1 -> 2"],
    "B",
    "Correct Chronological Sequence: 1. Minerva Mills (1980) -> 2. Bandhua Mukti Morcha (1984) -> 3. Unni Krishnan (1993) -> 4. Mirzapur Moti Kureshi (2005).",
    "சரியான காலவரிசை: 1. மினர்வா மில்ஸ் (1980) -> 2. பந்துவா முக்தி மோர்ச்சா (1984) -> 3. உன்னிகிருஷ்ணன் (1993) -> 4. மிர்சாபூர் மோதி குரேஷி (2005).",
    {
        "A": ("Incorrect. Minerva Mills (1980) was decided before Bandhua Mukti Morcha (1984).", "தவறு. மினர்வா மில்ஸ் (1980) பந்துவா முக்தி மோர்ச்சா (1984) வழக்கிற்கு முன்பே தீர்ப்பளிக்கப்பட்டது."),
        "B": ("Correct. 1980 -> 1984 -> 1993 -> 2005 follows the exact chronological progression of landmark DPSP cases.", "சரி. 1980 -> 1984 -> 1993 -> 2005 முக்கிய அரசு நெறிமுறைக் கோட்பாட்டு வழக்குகளின் சரியான காலவரிசையைப் பின்பற்றுகிறது."),
        "C": ("Incorrect. Bandhua Mukti Morcha (1984) preceded Unni Krishnan (1993).", "தவறு. பந்துவா முக்தி மோர்ச்சா (1984) உன்னிகிருஷ்ணன் (1993) வழக்கிற்கு முந்தையது."),
        "D": ("Incorrect. Mirzapur Moti Kureshi was decided in 2005, making it the latest in the series.", "தவறு. மிர்சாபூர் மோதி குரேஷி 2005-ல் தீர்ப்பளிக்கப்பட்டதால் வரிசையில் பிந்தையது.")
    },
    "In Mirzapur Moti Kureshi Case (2005), a 7-judge Constitution Bench held that a total ban on slaughter of cows and their progeny was constitutional under Articles 48 and 48A, overruling previous narrower rulings.",
    "மிர்சாபூர் மோதி குரேஷி வழக்கில் (2005), 7 நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வு, பசுக்கள் மற்றும் அவற்றின் சந்ததிகளை வதை செய்ய விதிக்கப்பட்ட முழு தடை பிரிவுகள் 48 மற்றும் 48A-ன் கீழ் செல்லுபடியாகும் எனத் தீர்ப்பளித்தது.",
    "Articles 48 (agriculture & animal husbandry) and 48A (environment & wildlife) work together for ecological and economic protection.",
    "பிரிவு 48 (வேளாண்மை & கால்நடை பராமரிப்பு) மற்றும் 48A (சுற்றுச்சூழல் & வனவிலங்குகள்) ஆகியவை சுற்றுச்சூழல் மற்றும் பொருளாதாரப் பாதுகாப்பிற்கு ஒன்றாகச் செயல்படுகின்றன."
))

# Q11 (Medium - C)
q_data.append(make_q(
    "DPSP_CHRONO_011", "Medium",
    "Arrange the following Parliamentary Acts enacted to implement specific Directive Principles in correct chronological order:\n\n1. Minimum Wages Act (Implementation of living wage directive under Article 43)\n2. Maternity Benefit Act (Implementation of maternity relief directive under Article 42)\n3. Wildlife Protection Act (Implementation of wildlife protection directive under Article 48A)\n4. Equal Remuneration Act (Implementation of equal pay directive under Article 39(d))",
    "குறிப்பிட்ட அரசு நெறிமுறைப்படுத்தும் கோட்பாடுகளை அமல்படுத்த நாடாளுமன்றத்தால் இயற்றப்பட்ட பின்வரும் சட்டங்களைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:\n\n1. குறைந்தபட்ச ஊதியச் சட்டம் (பிரிவு 43-ன் வாழ்வாதார ஊதிய நெறிமுறை அமலாக்கம்)\n2. மகப்பேறு நலச் சட்டம் (பிரிவு 42-ன் மகப்பேறு உதவி நெறிமுறை அமலாக்கம்)\n3. வனவிலங்கு பாதுகாப்புச் சட்டம் (பிரிவு 48A-ன் வனவிலங்கு பாதுகாப்பு நெறிமுறை அமலாக்கம்)\n4. சம ஊதியச் சட்டம் (பிரிவு 39(d)-ன் சம வேலைக்கு சம ஊதிய நெறிமுறை அமலாக்கம்)",
    [
        ("Minimum Wages Act (Implementation of living wage directive under Article 43)", "குறைந்தபட்ச ஊதியச் சட்டம் (பிரிவு 43-ன் வாழ்வாதார ஊதிய நெறிமுறை அமலாக்கம்)"),
        ("Maternity Benefit Act (Implementation of maternity relief directive under Article 42)", "மகப்பேறு நலச் சட்டம் (பிரிவு 42-ன் மகப்பேறு உதவி நெறிமுறை அமலாக்கம்)"),
        ("Wildlife Protection Act (Implementation of wildlife protection directive under Article 48A)", "வனவிலங்கு பாதுகாப்புச் சட்டம் (பிரிவு 48A-ன் வனவிலங்கு பாதுகாப்பு நெறிமுறை அமலாக்கம்)"),
        ("Equal Remuneration Act (Implementation of equal pay directive under Article 39(d))", "சம ஊதியச் சட்டம் (பிரிவு 39(d)-ன் சம வேலைக்கு சம ஊதிய நெறிமுறை அமலாக்கம்)")
    ],
    ["2 -> 1 -> 4 -> 3", "3 -> 1 -> 2 -> 4", "1 -> 2 -> 3 -> 4", "4 -> 2 -> 1 -> 3"],
    "C",
    "Correct Chronological Sequence: 1. Minimum Wages Act (1948) -> 2. Maternity Benefit Act (1961) -> 3. Wildlife Protection Act (1972) -> 4. Equal Remuneration Act (1976).",
    "சரியான காலவரிசை: 1. குறைந்தபட்ச ஊதியச் சட்டம் (1948) -> 2. மகப்பேறு நலச் சட்டம் (1961) -> 3. வனவிலங்கு பாதுகாப்புச் சட்டம் (1972) -> 4. சம ஊதியச் சட்டம் (1976).",
    {
        "A": ("Incorrect. Minimum Wages Act (1948) was enacted before Maternity Benefit Act (1961).", "தவறு. குறைந்தபட்ச ஊதியச் சட்டம் (1948) மகப்பேறு நலச் சட்டத்திற்கு (1961) முன்பே இயற்றப்பட்டது."),
        "B": ("Incorrect. Maternity Benefit Act (1961) preceded Wildlife Protection Act (1972).", "தவறு. மகப்பேறு நலச் சட்டம் (1961) வனவிலங்கு பாதுகாப்புச் சட்டத்திற்கு (1972) முந்தையது."),
        "C": ("Correct. 1948 -> 1961 -> 1972 -> 1976 follows the exact legislative enactment years of DPSP implementing statutes.", "சரி. 1948 -> 1961 -> 1972 -> 1976 அரசு நெறிமுறைக் கோட்பாடுகளை அமல்படுத்தும் சட்டங்களின் சரியான இயற்றப்பட்ட ஆண்டுகளைப் பின்பற்றுகிறது."),
        "D": ("Incorrect. Wildlife Protection Act (1972) came after Minimum Wages Act (1948).", "தவறு. வனவிலங்கு பாதுகாப்புச் சட்டம் (1972) குறைந்தபட்ச ஊதியச் சட்டத்திற்குப் (1948) பிறகே வந்தது.")
    },
    "Notice that the Wildlife Protection Act was passed in 1972, four years BEFORE Article 48A was inserted into the Constitution by the 42nd Amendment in 1976.",
    "வனவிலங்கு பாதுகாப்புச் சட்டம் 1972-ல் இயற்றப்பட்டது, இது 1976-ல் 42-வது திருத்தத்தால் பிரிவு 48A அரசியலமைப்பில் சேர்க்கப்படுவதற்கு நான்கு ஆண்டுகளுக்கு முன்பாகும்.",
    "The Equal Remuneration Act 1976 implements Article 39(d) by providing for equal remuneration to men and women workers.",
    "சம ஊதியச் சட்டம் 1976 ஆண் மற்றும் பெண் தொழிலாளர்களுக்குச் சம ஊதியம் வழங்குவதன் மூலம் பிரிவு 39(d)-ஐ அமல்படுத்துகிறது."
))

# Q12 (Medium - D)
q_data.append(make_q(
    "DPSP_CHRONO_012", "Medium",
    "Arrange the following environment protection laws and constitutional developments aligned with Article 48A in correct chronological order:\n\n1. Wildlife Protection Act (Passed to protect wild animals, birds and plants)\n2. 42nd Constitutional Amendment Act (Explicitly added Article 48A to Part IV)\n3. Forest Conservation Act (Enacted to check deforestation and conserve forest land)\n4. Environment Protection Act (Omnibus environmental legislation enacted post-Bhopal gas tragedy)",
    "பிரிவு 48A உடன் இணைந்த பின்வரும் சுற்றுச்சூழல் பாதுகாப்பு சட்டங்கள் மற்றும் அரசியலமைப்பு மாற்றங்களைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:\n\n1. வனவிலங்கு பாதுகாப்புச் சட்டம் (வனவிலங்குகள், பறவைகள் மற்றும் தாவரங்களைப் பாதுகாக்க இயற்றப்பட்டது)\n2. 42-வது அரசியலமைப்பு திருத்தச் சட்டம் (பகுதி IV-ல் பிரிவு 48A தெளிவாக்கச் சேர்க்கப்பட்டது)\n3. வனப் பாதுகாப்புச் சட்டம் (காடழிப்பைக் கட்டுப்படுத்தவும் வனநிலத்தைப் பாதுகாக்கவும் இயற்றப்பட்டது)\n4. சுற்றுச்சூழல் பாதுகாப்புச் சட்டம் (போபால் வாயு பேரிடருக்குப் பின் இயற்றப்பட்ட விரிவான சுற்றுச்சூழல் சட்டம்)",
    [
        ("Wildlife Protection Act (Passed to protect wild animals, birds and plants)", "வனவிலங்கு பாதுகாப்புச் சட்டம் (வனவிலங்குகள், பறவைகள் மற்றும் தாவரங்களைப் பாதுகாக்க இயற்றப்பட்டது)"),
        ("42nd Constitutional Amendment Act (Explicitly added Article 48A to Part IV)", "42-வது அரசியலமைப்பு திருத்தச் சட்டம் (பகுதி IV-ல் பிரிவு 48A தெளிவாக்கச் சேர்க்கப்பட்டது)"),
        ("Forest Conservation Act (Enacted to check deforestation and conserve forest land)", "வனப் பாதுகாப்புச் சட்டம் (காடழிப்பைக் கட்டுப்படுத்தவும் வனநிலத்தைப் பாதுகாக்கவும் இயற்றப்பட்டது)"),
        ("Environment Protection Act (Omnibus environmental legislation enacted post-Bhopal gas tragedy)", "சுற்றுச்சூழல் பாதுகாப்புச் சட்டம் (போபால் வாயு பேரிடருக்குப் பின் இயற்றப்பட்ட விரிவான சுற்றுச்சூழல் சட்டம்)")
    ],
    ["2 -> 1 -> 4 -> 3", "3 -> 1 -> 2 -> 4", "4 -> 2 -> 1 -> 3", "1 -> 2 -> 3 -> 4"],
    "D",
    "Correct Chronological Sequence: 1. Wildlife Protection Act (1972) -> 2. 42nd Amendment (1976) -> 3. Forest Conservation Act (1980) -> 4. Environment Protection Act (1986).",
    "சரியான காலவரிசை: 1. வனவிலங்கு பாதுகாப்புச் சட்டம் (1972) -> 2. 42-வது திருத்தம் (1976) -> 3. வனப் பாதுகாப்புச் சட்டம் (1980) -> 4. சுற்றுச்சூழல் பாதுகாப்புச் சட்டம் (1986).",
    {
        "A": ("Incorrect. Wildlife Protection Act (1972) was passed before the 42nd Amendment (1976).", "தவறு. வனவிலங்கு பாதுகாப்புச் சட்டம் (1972) 42-வது திருத்தத்திற்கு (1976) முன்பே நிறைவேற்றப்பட்டது."),
        "B": ("Incorrect. 42nd Amendment (1976) was passed before the Forest Conservation Act (1980).", "தவறு. 42-வது திருத்தம் (1976) வனப் பாதுகாப்புச் சட்டத்திற்கு (1980) முன்பே நிறைவேற்றப்பட்டது."),
        "C": ("Incorrect. Forest Conservation Act (1980) came after Wildlife Protection Act (1972).", "தவறு. வனப் பாதுகாப்புச் சட்டம் (1980) வனவிலங்கு பாதுகாப்புச் சட்டத்திற்குப் (1972) பிறகே வந்தது."),
        "D": ("Correct. 1972 -> 1976 -> 1980 -> 1986 correctly represents the evolution of environmental statutory and constitutional measures under Article 48A.", "சரி. 1972 -> 1976 -> 1980 -> 1986 என்பது பிரிவு 48A-ன் கீழ் சுற்றுச்சூழல் சட்ட மற்றும் அரசியலமைப்பு நடவடிக்கைகளின் சரியான வளர்ச்சியைக் குறிக்கிறது.")
    },
    "Article 48A directs that 'The State shall endeavour to protect and improve the environment and to safeguard the forests and wildlife of the country.'",
    "பிரிவு 48A 'நாட்டின் சுற்றுச்சூழலைப் பாதுகாக்கவும் மேம்படுத்தவும், காடுகள் மற்றும் வனவிலங்குகளைப் பாதுகாக்கவும் அரசு முயல வேண்டும்' எனக் கூறுகிறது.",
    "The Environment Protection Act 1986 was enacted under Article 253 of the Constitution to implement decisions made at the 1972 Stockholm Conference.",
    "சுற்றுச்சூழல் பாதுகாப்புச் சட்டம் 1986, 1972 ஸ்டாக்ஹோம் மாநாட்டின் முடிவுகளை அமல்படுத்த அரசியலமைப்பின் பிரிவு 253-ன் கீழ் இயற்றப்பட்டது."
))

# Q13 (Medium - A)
q_data.append(make_q(
    "DPSP_CHRONO_013", "Medium",
    "Arrange the following milestones in the evolution of Panchayati Raj directives under Article 40 in correct chronological order:\n\n1. Inclusion of Article 40 in original Constitution (Directive to organise Village Panchayats)\n2. Balwant Rai Mehta Committee Report (Recommended 3-tier Panchayati Raj system)\n3. Ashok Mehta Committee Report (Recommended 2-tier Panchayati Raj system)\n4. 73rd Constitutional Amendment Act (Granted constitutional status and Part IX to Panchayati Raj)",
    "பிரிவு 40-ன் கீழ் பஞ்சாயத்து ராஜ் நெறிமுறைகளின் வளர்ச்சியிலுள்ள மைல்கற்களைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:\n\n1. மூல அரசியலமைப்பில் பிரிவு 40 சேர்க்கப்படல் (கிராம பஞ்சாயத்துகளை அமைக்க அரசுக்கு நெறிமுறை)\n2. பல்வந்த் ராய் மேத்தா குழு அறிக்கை (3 அடுக்கு பஞ்சாயத்து ராஜ் முறையைப் பரிந்துரைத்தது)\n3. அசோக் மேத்தா குழு அறிக்கை (2 அடுக்கு பஞ்சாயத்து ராஜ் முறையைப் பரிந்துரைத்தது)\n4. 73-வது அரசியலமைப்பு திருத்தச் சட்டம் (பஞ்சாயத்து ராஜிற்கு அரசியலமைப்பு அந்தஸ்து மற்றும் பகுதி IX வழங்கல்)",
    [
        ("Inclusion of Article 40 in original Constitution (Directive to organise Village Panchayats)", "மூல அரசியலமைப்பில் பிரிவு 40 சேர்க்கப்படல் (கிராம பஞ்சாயத்துகளை அமைக்க அரசுக்கு நெறிமுறை)"),
        ("Balwant Rai Mehta Committee Report (Recommended 3-tier Panchayati Raj system)", "பல்வந்த் ராய் மேத்தா குழு அறிக்கை (3 அடுக்கு பஞ்சாயத்து ராஜ் முறையைப் பரிந்துரைத்தது)"),
        ("Ashok Mehta Committee Report (Recommended 2-tier Panchayati Raj system)", "அசோக் மேத்தா குழு அறிக்கை (2 அடுக்கு பஞ்சாயத்து ராஜ் முறையைப் பரிந்துரைத்தது)"),
        ("73rd Constitutional Amendment Act (Granted constitutional status and Part IX to Panchayati Raj)", "73-வது அரசியலமைப்பு திருத்தச் சட்டம் (பஞ்சாயத்து ராஜிற்கு அரசியலமைப்பு அந்தஸ்து மற்றும் பகுதி IX வழங்கல்)")
    ],
    ["1 -> 2 -> 3 -> 4", "2 -> 1 -> 4 -> 3", "3 -> 1 -> 2 -> 4", "4 -> 3 -> 1 -> 2"],
    "A",
    "Correct Chronological Sequence: 1. Original Constitution (1950) -> 2. Balwant Rai Mehta Committee (1957) -> 3. Ashok Mehta Committee (1977) -> 4. 73rd Amendment Act (1992).",
    "சரியான காலவரிசை: 1. மூல அரசியலமைப்பு (1950) -> 2. பல்வந்த் ராய் மேத்தா குழு (1957) -> 3. அசோக் மேத்தா குழு (1977) -> 4. 73-வது திருத்தச் சட்டம் (1992).",
    {
        "A": ("Correct. 1950 -> 1957 -> 1977 -> 1992 follows the historical trajectory of Article 40 implementation.", "சரி. 1950 -> 1957 -> 1977 -> 1992 பிரிவு 40 அமலாக்கத்தின் வரலாற்றுப் பாதையைப் பின்பற்றுகிறது."),
        "B": ("Incorrect. Balwant Rai Mehta Committee (1957) was appointed after the Constitution came into force in 1950.", "தவறு. பல்வந்த் ராய் மேத்தா குழு (1957) 1950 அரசியலமைப்பு அமலுக்கு வந்த பிறகே அமைக்கப்பட்டது."),
        "C": ("Incorrect. Ashok Mehta Committee (1977) came 20 years after Balwant Rai Mehta Committee (1957).", "தவறு. அசோக் மேத்தா குழு (1977) பல்வந்த் ராய் மேத்தா குழுவிற்கு (1957) 20 ஆண்டுகளுக்குப் பிறகே வந்தது."),
        "D": ("Incorrect. Ashok Mehta Committee was set up in 1977, long after 1950.", "தவறு. அசோக் மேத்தா குழு 1977-ல் அமைக்கப்பட்டது, இது 1950-க்கு பல ஆண்டுகளுக்குப் பிந்தையது.")
    },
    "Article 40 is a Gandhian Directive Principle directing the State to organise village panchayats and endow them with necessary powers to function as units of self-government.",
    "பிரிவு 40 என்பது காந்திய நெறிமுறையாகும், இது கிராம பஞ்சாயத்துகளை அமைத்து சுயராஜ்ய அலகுகளாகச் செயல்படத் தேவையான அதிகாரங்களை வழங்க அரசைப் பணிக்கிறது.",
    "The 73rd Constitutional Amendment Act 1992 came into force on April 24, 1993, celebrated as National Panchayati Raj Day.",
    "73-வது அரசியலமைப்பு திருத்தச் சட்டம் 1992 ஏப்ரல் 24, 1993 அன்று அமலுக்கு வந்தது, இது தேசிய பஞ்சாயத்து ராஜ் தினமாகக் கொண்டாடப்படுகிறது."
))

# Q14 (Medium - B)
q_data.append(make_q(
    "DPSP_CHRONO_014", "Medium",
    "Arrange the following events in the evolution of Legal Aid and Equal Justice (Article 39A) in correct chronological order:\n\n1. Enactment of 42nd Amendment Act (Inserted Article 39A into Part IV)\n2. Hussainara Khatoon Judgment (Supreme Court held free legal aid under Art 39A is part of Art 21)\n3. Enactment of Legal Services Authorities Act (Statutory framework for free legal services & Lok Adalats)\n4. Constitution of NALSA (National Legal Services Authority became fully operational)",
    "சட்ட உதவி மற்றும் சம நீதி (பிரிவு 39A) வளர்ச்சியிலுள்ள நிகழ்வுகளைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:\n\n1. 42-வது திருத்தச் சட்டம் இயற்றப்படல் (பகுதி IV-ல் பிரிவு 39A சேர்க்கப்பட்டது)\n2. ஹுசைனாரா கதூன் வழக்கு தீர்ப்பு (பிரிவு 39A-ன் இலவச சட்ட உதவி பிரிவு 21-ன் பகுதி என உச்சநீதிமன்றம் தீர்ப்பு)\n3. சட்டப் பணிகள் ஆணைக்குழு சட்டம் இயற்றப்படல் (இலவச சட்ட உதவி மற்றும் லோக் அதாலத்துகளுக்கான சட்டப்பூர்வ கட்டமைப்பு)\n4. NALSA உருவாக்கப்படுதல் (தேசிய சட்டப் பணிகள் ஆணைக்குழு முழுமையாகச் செயல்படத் தொடங்குதல்)",
    [
        ("Enactment of 42nd Amendment Act (Inserted Article 39A into Part IV)", "42-வது திருத்தச் சட்டம் இயற்றப்படல் (பகுதி IV-ல் பிரிவு 39A சேர்க்கப்பட்டது)"),
        ("Hussainara Khatoon Judgment (Supreme Court held free legal aid under Art 39A is part of Art 21)", "ஹுசைனாரா கதூன் வழக்கு தீர்ப்பு (பிரிவு 39A-ன் இலவச சட்ட உதவி பிரிவு 21-ன் பகுதி என உச்சநீதிமன்றம் தீர்ப்பு)"),
        ("Enactment of Legal Services Authorities Act (Statutory framework for free legal services & Lok Adalats)", "சட்டப் பணிகள் ஆணைக்குழு சட்டம் இயற்றப்படல் (இலவச சட்ட உதவி மற்றும் லோக் அதாலத்துகளுக்கான சட்டப்பூர்வ கட்டமைப்பு)"),
        ("Constitution of NALSA (National Legal Services Authority became fully operational)", "NALSA உருவாக்கப்படுதல் (தேசிய சட்டப் பணிகள் ஆணைக்குழு முழுமையாகச் செயல்படத் தொடங்குதல்)")
    ],
    ["2 -> 1 -> 4 -> 3", "1 -> 2 -> 3 -> 4", "3 -> 1 -> 2 -> 4", "4 -> 3 -> 1 -> 2"],
    "B",
    "Correct Chronological Sequence: 1. 42nd Amendment (1976) -> 2. Hussainara Khatoon (1979) -> 3. Legal Services Authorities Act (1987) -> 4. NALSA constituted (1995).",
    "சரியான காலவரிசை: 1. 42-வது திருத்தம் (1976) -> 2. ஹுசைனாரா கதூன் (1979) -> 3. சட்டப் பணிகள் ஆணைக்குழு சட்டம் (1987) -> 4. NALSA உருவாக்கப்படுதல் (1995).",
    {
        "A": ("Incorrect. 42nd Amendment (1976) introduced Article 39A before Hussainara Khatoon (1979).", "தவறு. 42-வது திருத்தம் (1976) ஹுசைனாரா கதூன் (1979) வழக்கிற்கு முன்பே பிரிவு 39A-ஐ அறிமுகப்படுத்தியது."),
        "B": ("Correct. 1976 -> 1979 -> 1987 -> 1995 traces the exact constitutional, judicial, and statutory timeline of Article 39A.", "சரி. 1976 -> 1979 -> 1987 -> 1995 பிரிவு 39A-ன் சரியான அரசியலமைப்பு, நீதித்துறை மற்றும் சட்டப்பூர்வ காலவரிசையைக் குறிக்கிறது."),
        "C": ("Incorrect. Hussainara Khatoon judgment (1979) preceded the Legal Services Authorities Act (1987).", "தவறு. ஹுசைனாரா கதூன் தீர்ப்பு (1979) சட்டப் பணிகள் ஆணைக்குழு சட்டத்திற்கு (1987) முந்தையது."),
        "D": ("Incorrect. NALSA was constituted in 1995, long after the 42nd Amendment (1976).", "தவறு. NALSA 1995-ல் அமைக்கப்பட்டது, இது 42-வது திருத்தத்திற்கு (1976) பல ஆண்டுகளுக்குப் பிந்தையது.")
    },
    "Article 39A directs the State to secure that the operation of the legal system promotes justice on a basis of equal opportunity and to provide free legal aid by suitable legislation.",
    "சம வாய்ப்பின் அடிப்படையில் நீதி வழங்கப்படுவதை உறுதி செய்யவும், தகுந்த சட்டத்தின் மூலம் இலவச சட்ட உதவியை வழங்கவும் பிரிவு 39A அரசைப் பணிக்கிறது.",
    "The Legal Services Authorities Act was passed in 1987, but came into force on November 9, 1995, establishing NALSA.",
    "சட்டப் பணிகள் ஆணைக்குழு சட்டம் 1987-ல் நிறைவேற்றப்பட்டது, ஆனால் நவம்பர் 9, 1995 அன்று அமலுக்கு வந்து NALSA-வை நிறுவியது."
))

# Q15 (Medium - C)
q_data.append(make_q(
    "DPSP_CHRONO_015", "Medium",
    "Arrange the following Acts passed to fulfill various Directive Principles in REVERSE chronological order (latest to earliest):\n\n1. Right to Education (RTE) Act (Implementation of education directive)\n2. Legal Services Authorities Act (Implementation of equal justice and free legal aid)\n3. Equal Remuneration Act (Implementation of equal pay for equal work directive)\n4. Maternity Benefit Act (Implementation of maternity relief directive)",
    "பல்வேறு அரசு நெறிமுறைக் கோட்பாடுகளை நிறைவேற்ற இயற்றப்பட்ட பின்வரும் சட்டங்களைத் தலைகீழ் காலவரிசைப்படி (பிந்தையது முதல் முந்தையது வரை) வரிசைப்படுத்தவும்:\n\n1. இலவச கட்டாயக் கல்வி உரிமை (RTE) சட்டம் (கல்வி நெறிமுறை அமலாக்கம்)\n2. சட்டப் பணிகள் ஆணைக்குழு சட்டம் (சம நீதி மற்றும் இலவச சட்ட உதவி நெறிமுறை அமலாக்கம்)\n3. சம ஊதியச் சட்டம் (சம வேலைக்கு சம ஊதிய நெறிமுறை அமலாக்கம்)\n4. மகப்பேறு நலச் சட்டம் (மகப்பேறு உதவி நெறிமுறை அமலாக்கம்)",
    [
        ("Right to Education (RTE) Act (Implementation of education directive)", "இலவச கட்டாயக் கல்வி உரிமை (RTE) சட்டம் (கல்வி நெறிமுறை அமலாக்கம்)"),
        ("Legal Services Authorities Act (Implementation of equal justice and free legal aid)", "சட்டப் பணிகள் ஆணைக்குழு சட்டம் (சம நீதி மற்றும் இலவச சட்ட உதவி நெறிமுறை அமலாக்கம்)"),
        ("Equal Remuneration Act (Implementation of equal pay for equal work directive)", "சம ஊதியச் சட்டம் (சம வேலைக்கு சம ஊதிய நெறிமுறை அமலாக்கம்)"),
        ("Maternity Benefit Act (Implementation of maternity relief directive)", "மகப்பேறு நலச் சட்டம் (மகப்பேறு உதவி நெறிமுறை அமலாக்கம்)")
    ],
    ["4 -> 3 -> 2 -> 1", "2 -> 4 -> 1 -> 3", "1 -> 2 -> 3 -> 4", "3 -> 1 -> 4 -> 2"],
    "C",
    "Correct Reverse Chronological Sequence (Latest to Earliest): 1. RTE Act (2009) -> 2. Legal Services Authorities Act (1987) -> 3. Equal Remuneration Act (1976) -> 4. Maternity Benefit Act (1961).",
    "சரியான தலைகீழ் காலவரிசை (பிந்தையது முதல் முந்தையது வரை): 1. RTE சட்டம் (2009) -> 2. சட்டப் பணிகள் ஆணைக்குழு சட்டம் (1987) -> 3. சம ஊதியச் சட்டம் (1976) -> 4. மகப்பேறு நலச் சட்டம் (1961).",
    {
        "A": ("Incorrect. 4 -> 3 -> 2 -> 1 represents earliest to latest order.", "தவறு. 4 -> 3 -> 2 -> 1 என்பது முந்தையது முதல் பிந்தையது வரையிலான வரிசை."),
        "B": ("Incorrect. Equal Remuneration Act (1976) was passed before Legal Services Authorities Act (1987).", "தவறு. சம ஊதியச் சட்டம் (1976) சட்டப் பணிகள் ஆணைக்குழு சட்டத்திற்கு (1987) முன்பே நிறைவேற்றப்பட்டது."),
        "C": ("Correct. 2009 -> 1987 -> 1976 -> 1961 correctly arranges the implementing statutes from latest to earliest.", "சரி. 2009 -> 1987 -> 1976 -> 1961 சட்டங்களை பிந்தையது முதல் முந்தையது வரை சரியாக வரிசைப்படுத்துகிறது."),
        "D": ("Incorrect. RTE Act (2009) is the most recent act among the four.", "தவறு. RTE சட்டம் (2009) நான்கில் மிகவும் சமீபத்திய சட்டமாகும்.")
    },
    "Do not confuse the Maternity Benefit Act (1961) with the Equal Remuneration Act (1976). Maternity Benefit Act was passed 15 years earlier.",
    "மகப்பேறு நலச் சட்டம் (1961) மற்றும் சம ஊதியச் சட்டம் (1976) ஆகியவற்றை குழப்பிக் கொள்ளக் கூடாது. மகப்பேறு நலச் சட்டம் 15 ஆண்டுகளுக்கு முன்பே நிறைவேற்றப்பட்டது.",
    "Maternity Benefit Act implements Article 42 which mandates 'just and humane conditions of work and maternity relief'.",
    "மகப்பேறு நலச் சட்டம் 'நியாயமான மற்றும் மனிதத்தன்மையான பணிச்சூழல் மற்றும் மகப்பேறு உதவி'யைப் பணிக்கும் பிரிவு 42-ஐ அமல்படுத்துகிறது."
))

# Q16 (Medium - D)
q_data.append(make_q(
    "DPSP_CHRONO_016", "Medium",
    "Arrange the following judicial rulings concerning the implementation of Article 39(b) and 39(c) directive principles in correct chronological order:\n\n1. Champakam Dorairajan Case (DPSP declared subsidiary to Part III Fundamental Rights)\n2. Golaknath Case (Parliament cannot curtail Part III rights to implement Part IV)\n3. Sanjeev Coke Case (Re-affirmed primacy of Article 39(b) and 39(c) over Articles 14 and 19)\n4. State of TN v. Abu Kavur Bai (Upheld nationalisation of transport schemes under Art 39(b) and 39(c))",
    "பிரிவு 39(b) மற்றும் 39(c) நெறிமுறைகளை அமல்படுத்துவது தொடர்பான பின்வரும் நீதிமன்றத் தீர்ப்புகளைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:\n\n1. செம்பகம் துரைராஜன் வழக்கு (அரசு நெறிமுறைக் கோட்பாடுகள் பகுதி III-க்கு துணையானவை என அறிவிப்பு)\n2. கோலக்நாத் வழக்கு (பகுதி IV-ஐ அமல்படுத்த நாடாளுமன்றம் பகுதி III உரிமைகளைக் குறைக்க முடியாது)\n3. சஞ்சீவ் கோக் வழக்கு (பிரிவுகள் 14 மற்றும் 19-க்கு மேல் பிரிவு 39(b) மற்றும் 39(c)-ன் முதன்மை மீண்டும் உறுதி செய்யப்பட்டது)\n4. தமிழ்நாடு மாநிலம் எதிராக அபு கவூர் பாய் (பிரிவு 39(b) மற்றும் 39(c)-ன் கீழ் போக்குவரத்து தேசியமயமாக்கல் திட்டங்கள் உறுதி செய்யப்படல்)",
    [
        ("Champakam Dorairajan Case (DPSP declared subsidiary to Part III Fundamental Rights)", "செம்பகம் துரைராஜன் வழக்கு (அரசு நெறிமுறைக் கோட்பாடுகள் பகுதி III-க்கு துணையானவை என அறிவிப்பு)"),
        ("Golaknath Case (Parliament cannot curtail Part III rights to implement Part IV)", "கோலக்நாத் வழக்கு (பகுதி IV-ஐ அமல்படுத்த நாடாளுமன்றம் பகுதி III உரிமைகளைக் குறைக்க முடியாது)"),
        ("Sanjeev Coke Case (Re-affirmed primacy of Article 39(b) and 39(c) over Articles 14 and 19)", "சஞ்சீவ் கோக் வழக்கு (பிரிவுகள் 14 மற்றும் 19-க்கு மேல் பிரிவு 39(b) மற்றும் 39(c)-ன் முதன்மை மீண்டும் உறுதி செய்யப்பட்டது)"),
        ("State of TN v. Abu Kavur Bai (Upheld nationalisation of transport schemes under Art 39(b) and 39(c))", "தமிழ்நாடு மாநிலம் எதிராக அபு கவூர் பாய் (பிரிவு 39(b) மற்றும் 39(c)-ன் கீழ் போக்குவரத்து தேசியமயமாக்கல் திட்டங்கள் உறுதி செய்யப்படல்)")
    ],
    ["2 -> 1 -> 4 -> 3", "3 -> 1 -> 2 -> 4", "4 -> 2 -> 1 -> 3", "1 -> 2 -> 3 -> 4"],
    "D",
    "Correct Chronological Sequence: 1. Champakam Dorairajan (1951) -> 2. Golaknath (1967) -> 3. Sanjeev Coke (1983) -> 4. Abu Kavur Bai (1984).",
    "சரியான காலவரிசை: 1. செம்பகம் துரைராஜன் (1951) -> 2. கோலக்நாத் (1967) -> 3. சஞ்சீவ் கோக் (1983) -> 4. அபு கவூர் பாய் (1984).",
    {
        "A": ("Incorrect. Champakam Dorairajan (1951) was decided before Golaknath (1967).", "தவறு. செம்பகம் துரைராஜன் (1951) கோலக்நாத் (1967) வழக்கிற்கு முன்பே தீர்ப்பளிக்கப்பட்டது."),
        "B": ("Incorrect. Sanjeev Coke (1983) came after Golaknath (1967).", "தவறு. சஞ்சீவ் கோக் (1983) கோலக்நாத் (1967) வழக்கிற்குப் பிறகே வந்தது."),
        "C": ("Incorrect. Sanjeev Coke (1983) came long after Champakam Dorairajan (1951).", "தவறு. சஞ்சீவ் கோக் (1983) செம்பகம் துரைராஜன் (1951) வழக்கிற்கு பல ஆண்டுகளுக்குப் பிறகே வந்தது."),
        "D": ("Correct. 1951 -> 1967 -> 1983 -> 1984 represents the true chronological order of cases discussing Article 39(b) and (c) directives.", "சரி. 1951 -> 1967 -> 1983 -> 1984 பிரிவு 39(b) மற்றும் (c) நெறிமுறைகளைப் விவாதிக்கும் வழக்குகளின் சரியான காலவரிசையாகும்.")
    },
    "In Sanjeev Coke (1983) and Abu Kavur Bai (1984), the Supreme Court firmly sustained laws nationalising coal mines and transport schemes under Article 31C as valid implementations of Article 39(b) and (c).",
    "சஞ்சீவ் கோக் (1983) மற்றும் அபு கவூர் பாய் (1984) வழக்குகளில், நிலக்கரி சுரங்கங்கள் மற்றும் போக்குவரத்துத் திட்டங்களை தேசியமயமாக்கும் சட்டங்களை பிரிவு 31C-ன் கீழ் பிரிவு 39(b) மற்றும் (c)-ன் செல்லுபடியாகும் அமலாக்கமாக உச்சநீதிமன்றம் உறுதி செய்தது.",
    "Article 39(b) deals with ownership and control of material resources for common good, and 39(c) prevents concentration of wealth.",
    "பிரிவு 39(b) பொது நலனுக்காக வளங்களின் உரிமையைக் கையாள்கிறது, பிரிவு 39(c) செல்வம் குவிவதைத் தடுக்கிறது."
))

# Q17 (Medium - A)
q_data.append(make_q(
    "DPSP_CHRONO_017", "Medium",
    "Arrange the following Constitutional Amendments affecting agrarian reforms, socio-economic equality, and co-operatives in correct chronological order:\n\n1. 1st Amendment Act (Inserted Art 31A & 31B to protect land reform laws fulfilling Art 39(b) & (c))\n2. 25th Amendment Act (Inserted Art 31C protecting Art 39(b) & (c) directives from Art 14, 19, 31)\n3. 44th Amendment Act (Inserted Art 38(2) for minimising inequalities in income and opportunities)\n4. 97th Amendment Act (Inserted Art 43B for promotion of autonomous functioning of co-operative societies)",
    "வேளாண் சீர்திருத்தங்கள், சமூக-பொருளாதார சமத்துவம் மற்றும் கூட்டுறவு சங்கங்களைப் பாதித்த பின்வரும் அரசியலமைப்பு திருத்தங்களைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:\n\n1. 1-வது திருத்தச் சட்டம் (பிரிவு 39(b) & (c)-ஐ நிறைவேற்றும் நிலசீர்திருத்த சட்டங்களைப் பாதுகாக்க பிரிவு 31A & 31B சேர்க்கப்பட்டது)\n2. 25-வது திருத்தச் சட்டம் (பிரிவுகள் 14, 19, 31-லிருந்து பிரிவு 39(b) & (c) நெறிமுறைகளைப் பாதுகாக்கும் பிரிவு 31C சேர்க்கப்பட்டது)\n3. 44-வது திருத்தச் சட்டம் (வருமானம் மற்றும் அந்தஸ்தில் உள்ள ஏற்றத்தாழ்வுகளைக் குறைக்க பிரிவு 38(2) சேர்க்கப்பட்டது)\n4. 97-வது திருத்தச் சட்டம் (கூட்டுறவு சங்கங்களின் தன்னாட்சி செயல்பாட்டை ஊக்குவிக்க பிரிவு 43B சேர்க்கப்பட்டது)",
    [
        ("1st Amendment Act (Inserted Art 31A & 31B to protect land reform laws fulfilling Art 39(b) & (c))", "1-வது திருத்தச் சட்டம் (பிரிவு 39(b) & (c)-ஐ நிறைவேற்றும் நிலசீர்திருத்த சட்டங்களைப் பாதுகாக்க பிரிவு 31A & 31B சேர்க்கப்பட்டது)"),
        ("25th Amendment Act (Inserted Art 31C protecting Art 39(b) & (c) directives from Art 14, 19, 31)", "25-வது திருத்தச் சட்டம் (பிரிவுகள் 14, 19, 31-லிருந்து பிரிவு 39(b) & (c) நெறிமுறைகளைப் பாதுகாக்கும் பிரிவு 31C சேர்க்கப்பட்டது)"),
        ("44th Amendment Act (Inserted Art 38(2) for minimising inequalities in income and opportunities)", "44-வது திருத்தச் சட்டம் (வருமானம் மற்றும் அந்தஸ்தில் உள்ள ஏற்றத்தாழ்வுகளைக் குறைக்க பிரிவு 38(2) சேர்க்கப்பட்டது)"),
        ("97th Amendment Act (Inserted Art 43B for promotion of autonomous functioning of co-operative societies)", "97-வது திருத்தச் சட்டம் (கூட்டுறவு சங்கங்களின் தன்னாட்சி செயல்பாட்டை ஊக்குவிக்க பிரிவு 43B சேர்க்கப்பட்டது)")
    ],
    ["1 -> 2 -> 3 -> 4", "2 -> 1 -> 4 -> 3", "3 -> 2 -> 1 -> 4", "4 -> 3 -> 1 -> 2"],
    "A",
    "Correct Chronological Sequence: 1. 1st Amendment (1951) -> 2. 25th Amendment (1971) -> 3. 44th Amendment (1978) -> 4. 97th Amendment (2011).",
    "சரியான காலவரிசை: 1. 1-வது திருத்தம் (1951) -> 2. 25-வது திருத்தம் (1971) -> 3. 44-வது திருத்தம் (1978) -> 4. 97-வது திருத்தம் (2011).",
    {
        "A": ("Correct. 1951 -> 1971 -> 1978 -> 2011 matches the exact historic order of constitutional amendments modifying social and economic directives.", "சரி. 1951 -> 1971 -> 1978 -> 2011 சமூக மற்றும் பொருளாதார நெறிமுறைகளை மாற்றியமைத்த திருத்தங்களின் சரியான வரலாற்று வரிசையாகும்."),
        "B": ("Incorrect. 1st Amendment (1951) came long before 25th Amendment (1971).", "தவறு. 1-வது திருத்தம் (1951) 25-வது திருத்தத்திற்கு (1971) பல ஆண்டுகளுக்கு முன்பே வந்தது."),
        "C": ("Incorrect. 25th Amendment (1971) preceded 44th Amendment (1978).", "தவறு. 25-வது திருத்தம் (1971) 44-வது திருத்தத்திற்கு (1978) முந்தையது."),
        "D": ("Incorrect. 44th Amendment (1978) came after 1st Amendment (1951).", "தவறு. 44-வது திருத்தம் (1978) 1-வது திருத்தத்திற்கு (1951) பிறகே வந்தது.")
    },
    "The 1st Amendment Act (1951) added Articles 31A and 31B along with the Ninth Schedule specifically to protect land reform laws implementing DPSP goals.",
    "1-வது திருத்தச் சட்டம் (1951) DPSP இலக்குகளை அமல்படுத்தும் நிலச்சீர்திருத்தச் சட்டங்களைப் பாதுகாக்கவே 9-வது அட்டவணையுடன் பிரிவுகள் 31A மற்றும் 31B-ஐச் சேர்த்தது.",
    "97th Constitutional Amendment Act 2011 added Article 43B in Part IV and inserted Part IXB into the Constitution.",
    "97-வது அரசியலமைப்பு திருத்தச் சட்டம் 2011 பகுதி IV-ல் பிரிவு 43B-ஐயும் அரசியலமைப்பில் பகுதி IXB-ஐயும் சேர்த்தது."
))

# Q18 (Hard - B)
q_data.append(make_q(
    "DPSP_CHRONO_018", "Hard",
    "Arrange the following complex sequence of judicial rulings and constitutional amendments regarding DPSP primacy and Basic Structure in correct chronological order:\n\n1. Champakam Dorairajan Ruling (DPSP made subordinate to Part III Fundamental Rights)\n2. 25th Constitutional Amendment Act (Inserted 1st clause of Art 31C protecting Art 39(b) & (c))\n3. 42nd Constitutional Amendment Act (Substituted all DPSP in Art 31C)\n4. Sanjeev Coke Judgment (Re-affirmed constitutionality of Art 31C as restricted to Art 39(b) & (c))",
    "அரசு நெறிமுறைக் கோட்பாடுகளின் முதன்மைத்தன்மை மற்றும் அடிப்படை அமைப்பு பற்றிய நீதிமன்றத் தீர்ப்புகள் மற்றும் அரசியலமைப்பு திருத்தங்களின் சிக்கலான வரிசையைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:\n\n1. செம்பகம் துரைராஜன் தீர்ப்பு (அரசு நெறிமுறைக் கோட்பாடுகள் பகுதி III-க்கு கீழ்ப்பட்டவை எனத் தீர்ப்பு)\n2. 25-வது அரசியலமைப்பு திருத்தச் சட்டம் (பிரிவு 39(b) & (c)-ஐப் பாதுகாக்கும் பிரிவு 31C-ன் 1-வது வாக்கியம் சேர்க்கப்பட்டது)\n3. 42-வது அரசியலமைப்பு திருத்தச் சட்டம் (பிரிவு 31C-ல் அனைத்து நெறிமுறைக் கோட்பாடுகளும் மாற்றீடு செய்யப்பட்டன)\n4. சஞ்சீவ் கோக் தீர்ப்பு (பிரிவு 39(b) & (c)-க்கு மட்டுமே வரையறுக்கப்பட்ட பிரிவு 31C-ன் செல்லுபடித்ன்மை மீண்டும் உறுதி செய்யப்பட்டது)",
    [
        ("Champakam Dorairajan Ruling (DPSP made subordinate to Part III Fundamental Rights)", "செம்பகம் துரைராஜன் தீர்ப்பு (அரசு நெறிமுறைக் கோட்பாடுகள் பகுதி III-க்கு கீழ்ப்பட்டவை எனத் தீர்ப்பு)"),
        ("25th Constitutional Amendment Act (Inserted 1st clause of Art 31C protecting Art 39(b) & (c))", "25-வது அரசியலமைப்பு திருத்தச் சட்டம் (பிரிவு 39(b) & (c)-ஐப் பாதுகாக்கும் பிரிவு 31C-ன் 1-வது வாக்கியம் சேர்க்கப்பட்டது)"),
        ("42nd Constitutional Amendment Act (Substituted all DPSP in Art 31C)", "42-வது அரசியலமைப்பு திருத்தச் சட்டம் (பிரிவு 31C-ல் அனைத்து நெறிமுறைக் கோட்பாடுகளும் மாற்றீடு செய்யப்பட்டன)"),
        ("Sanjeev Coke Judgment (Re-affirmed constitutionality of Art 31C as restricted to Art 39(b) & (c))", "சஞ்சீவ் கோக் தீர்ப்பு (பிரிவு 39(b) & (c)-க்கு மட்டுமே வரையறுக்கப்பட்ட பிரிவு 31C-ன் செல்லுபடித்ன்மை மீண்டும் உறுதி செய்யப்பட்டது)")
    ],
    ["2 -> 1 -> 4 -> 3", "1 -> 2 -> 3 -> 4", "3 -> 1 -> 2 -> 4", "4 -> 3 -> 1 -> 2"],
    "B",
    "Correct Chronological Sequence: 1. Champakam Dorairajan (1951) -> 2. 25th Amendment (1971) -> 3. 42nd Amendment (1976) -> 4. Sanjeev Coke (1983).",
    "சரியான காலவரிசை: 1. செம்பகம் துரைராஜன் (1951) -> 2. 25-வது திருத்தம் (1971) -> 3. 42-வது திருத்தம் (1976) -> 4. சஞ்சீவ் கோக் (1983).",
    {
        "A": ("Incorrect. Champakam Dorairajan (1951) was decided 20 years before 25th Amendment (1971).", "தவறு. செம்பகம் துரைராஜன் (1951) 25-வது திருத்தத்திற்கு (1971) 20 ஆண்டுகளுக்கு முன்பே தீர்ப்பளிக்கப்பட்டது."),
        "B": ("Correct. 1951 -> 1971 -> 1976 -> 1983 follows the precise chronological order of amendments and judgments.", "சரி. 1951 -> 1971 -> 1976 -> 1983 திருத்தங்கள் மற்றும் தீர்ப்புகளின் துல்லியமான காலவரிசையைப் பின்பற்றுகிறது."),
        "C": ("Incorrect. 42nd Amendment (1976) was enacted after 25th Amendment (1971).", "தவறு. 42-வது திருத்தம் (1976) 25-வது திருத்தத்திற்கு (1971) பிறகே இயற்றப்பட்டது."),
        "D": ("Incorrect. Sanjeev Coke was decided in 1983, long after Champakam Dorairajan (1951).", "தவறு. சஞ்சீவ் கோக் 1983-ல் தீர்ப்பளிக்கப்பட்டது, இது செம்பகம் துரைராஜன் (1951) வழக்கிற்கு பல ஆண்டுகளுக்குப் பிந்தையது.")
    },
    "In Sanjeev Coke (1983), Justice O. Chinnappa Reddy upheld Article 31C as enacted by the 25th Amendment, holding that laws advancing Article 39(b) and (c) take precedence over Articles 14 and 19.",
    "சஞ்சீவ் கோக் (1983) வழக்கில், 25-வது திருத்தத்தால் இயற்றப்பட்ட பிரிவு 31C-ஐ உச்சநீதிமன்றம் உறுதி செய்தது.",
    "The balance between Fundamental Rights and DPSP is part of the Basic Structure of the Indian Constitution.",
    "அடிப்படை உரிமைகள் மற்றும் அரசு நெறிமுறைக் கோட்பாடுகளுக்கு இடையேயான சமநிலை இந்திய அரசியலமைப்பின் அடிப்படை அமைப்பின் பகுதியாகும்."
))

# Q19 (Hard - C)
q_data.append(make_q(
    "DPSP_CHRONO_019", "Hard",
    "Arrange the following key historical milestones in the complete evolution of DPSP in India in correct chronological order:\n\n1. Government of India Act 1935 (Contained 'Instruments of Instructions' issued to Governor-General)\n2. Enactment of Constitution of India (Part IV Articles 36-51 incorporated into Supreme Law)\n3. 42nd Constitutional Amendment Act (Added Article 43A for participation of workers in management)\n4. 86th Constitutional Amendment Act (Substituted Article 45 to focus strictly on early childhood care below 6 years)",
    "இந்தியாவில் அரசு நெறிமுறைப்படுத்தும் கோட்பாடுகளின் முழுமையான வளர்ச்சியிலுள்ள முக்கிய வரலாற்று மைல்கற்களைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:\n\n1. இந்திய அரசுச் சட்டம் 1935 (ஆளுநர் ஜெனரலுக்கு வழங்கப்பட்ட 'அறிவுறுத்தல் கருவிகள்' அடங்கியது)\n2. இந்திய அரசியலமைப்பு இயற்றப்படல் (பகுதி IV பிரிவுகள் 36-51 உச்ச சட்டத்தில் சேர்க்கப்படல்)\n3. 42-வது அரசியலமைப்பு திருத்தச் சட்டம் (மேலாண்மையில் தொழிலாளர்களின் பங்கேற்பிற்காக பிரிவு 43A சேர்க்கப்படல்)\n4. 86-வது அரசியலமைப்பு திருத்தச் சட்டம் (பிரிவு 45 6 வயதிற்குட்பட்ட குழந்தை பராமரிப்பாக மாற்றப்படல்)",
    [
        ("Government of India Act 1935 (Contained 'Instruments of Instructions' issued to Governor-General)", "இந்திய அரசுச் சட்டம் 1935 (ஆளுநர் ஜெனரலுக்கு வழங்கப்பட்ட 'அறிவுறுத்தல் கருவிகள்' அடங்கியது)"),
        ("Enactment of Constitution of India (Part IV Articles 36-51 incorporated into Supreme Law)", "இந்திய அரசியலமைப்பு இயற்றப்படல் (பகுதி IV பிரிவுகள் 36-51 உச்ச சட்டத்தில் சேர்க்கப்படல்)"),
        ("42nd Constitutional Amendment Act (Added Article 43A for participation of workers in management)", "42-வது அரசியலமைப்பு திருத்தச் சட்டம் (மேலாண்மையில் தொழிலாளர்களின் பங்கேற்பிற்காக பிரிவு 43A சேர்க்கப்படல்)"),
        ("86th Constitutional Amendment Act (Substituted Article 45 to focus strictly on early childhood care below 6 years)", "86-வது அரசியலமைப்பு திருத்தச் சட்டம் (பிரிவு 45 6 வயதிற்குட்பட்ட குழந்தை பராமரிப்பாக மாற்றப்படல்)")
    ],
    ["2 -> 1 -> 4 -> 3", "3 -> 1 -> 2 -> 4", "1 -> 2 -> 3 -> 4", "4 -> 2 -> 1 -> 3"],
    "C",
    "Correct Chronological Sequence: 1. GOI Act 1935 -> 2. Enactment of Constitution (1950) -> 3. 42nd Amendment (1976) -> 4. 86th Amendment (2002).",
    "சரியான காலவரிசை: 1. இந்திய அரசுச் சட்டம் 1935 -> 2. அரசியலமைப்பு இயற்றப்படல் (1950) -> 3. 42-வது திருத்தம் (1976) -> 4. 86-வது திருத்தம் (2002).",
    {
        "A": ("Incorrect. GOI Act 1935 came before the Constitution of India (1950).", "தவறு. இந்திய அரசுச் சட்டம் 1935 இந்திய அரசியலமைப்புக்கு (1950) முந்தையது."),
        "B": ("Incorrect. Constitution was enacted in 1950, long before 42nd Amendment in 1976.", "தவறு. அரசியலமைப்பு 1950-ல் இயற்றப்பட்டது, இது 1976-ல் 42-வது திருத்தத்திற்கு பல ஆண்டுகளுக்கு முந்தையது."),
        "C": ("Correct. 1935 -> 1950 -> 1976 -> 2002 matches the full historical evolution of DPSP.", "சரி. 1935 -> 1950 -> 1976 -> 2002 அரசு நெறிமுறைக் கோட்பாடுகளின் முழு வரலாற்று வளர்ச்சியைப் பிரதிபலிக்கிறது."),
        "D": ("Incorrect. 42nd Amendment (1976) came after 1935 and 1950.", "தவறு. 42-வது திருத்தம் (1976) 1935 மற்றும் 1950-க்கு பிறகே வந்தது.")
    },
    "B.R. Ambedkar explicitly noted in Constituent Assembly that DPSP are like the 'Instruments of Instructions' issued to the Governor-General and Governors by the British Government under GOI Act 1935.",
    "அரசியலமைப்பு நிர்ணய சபையில் பி.ஆர். அம்பேத்கர், அரசு நெறிமுறைக் கோட்பாடுகள் 1935-ம் ஆண்டு இந்திய அரசுச் சட்டத்தின் கீழ் பிரிட்டிஷ் அரசாங்கத்தால் ஆளுநர் ஜெனரலுக்கு வழங்கப்பட்ட 'அறிவுறுத்தல் கருவிகள்' போன்றவை எனக் குறிப்பிட்டுக் கூறினார்.",
    "The only difference is that DPSP are instructions addressed to the Legislature and Executive of free India.",
    "ஒரே வித்தியாசம் என்னவென்றால், DPSP சுதந்திர இந்தியாவின் சட்டமன்றம் மற்றும் நிர்வாகத்திற்கு வழங்கப்பட்ட அறிவுறுத்தல்களாகும்."
))

# Q20 (Hard - D)
q_data.append(make_q(
    "DPSP_CHRONO_020", "Hard",
    "Arrange the following landmark Supreme Court decisions linking DPSP to Fundamental Rights under Article 21 in correct chronological order:\n\n1. State of Bombay v. F.N. Balsara (Prohibition directive under Art 47 used as benchmark for reasonable restrictions)\n2. Randhir Singh v. Union of India (Equal pay for equal work under Art 39(d) enforced via Art 14 & 21)\n3. Olga Tellis v. Bombay Municipal Corporation (Right to livelihood under Art 39(a) integrated into Art 21)\n4. Unni Krishnan v. State of Andhra Pradesh (Right to education up to age 14 under Art 45 integrated into Art 21)",
    "பிரிவு 21-ன் கீழ் அடிப்படை உரிமைகளுடன் அரசு நெறிமுறைப்படுத்தும் கோட்பாடுகளை இணைத்த பின்வரும் உச்சநீதிமன்ற முக்கியத் தீர்ப்புகளைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:\n\n1. பம்பாய் மாநிலம் எதிராக F.N. பால்சாரா (பிரிவு 47 மதுவிலக்கு நெறிமுறை நியாயமான கட்டுப்பாடுகளுக்கான அளவுகோலாகப் பயன்படுத்தப்படல்)\n2. ரந்தீர் சிங் எதிராக இந்திய யூனியன் (பிரிவு 39(d)-ன் சம வேலைக்கு சம ஊதியம் பிரிவு 14 & 21 மூலம் அமல்படுத்தப்படல்)\n3. ஓல்கா டெல்லிஸ் எதிராக பம்பாய் மாநகராட்சி (பிரிவு 39(a)-ன் வாழ்வாதார உரிமை பிரிவு 21-ல் இணைக்கப்படல்)\n4. உன்னிகிருஷ்ணன் எதிராக ஆந்திரப் பிரதேச மாநிலம் (பிரிவு 45-ன் 14 வயது வரையிலான கல்வி உரிமை பிரிவு 21-ல் இணைக்கப்படல்)",
    [
        ("State of Bombay v. F.N. Balsara (Prohibition directive under Art 47 used as benchmark for reasonable restrictions)", "பம்பாய் மாநிலம் எதிராக F.N. பால்சாரா (பிரிவு 47 மதுவிலக்கு நெறிமுறை நியாயமான கட்டுப்பாடுகளுக்கான அளவுகோலாகப் பயன்படுத்தப்படல்)"),
        ("Randhir Singh v. Union of India (Equal pay for equal work under Art 39(d) enforced via Art 14 & 21)", "ரந்தீர் சிங் எதிராக இந்திய யூனியன் (பிரிவு 39(d)-ன் சம வேலைக்கு சம ஊதியம் பிரிவு 14 & 21 மூலம் அமல்படுத்தப்படல்)"),
        ("Olga Tellis v. Bombay Municipal Corporation (Right to livelihood under Art 39(a) integrated into Art 21)", "ஓல்கா டெல்லிஸ் எதிராக பம்பாய் மாநகராட்சி (பிரிவு 39(a)-ன் வாழ்வாதார உரிமை பிரிவு 21-ல் இணைக்கப்படல்)"),
        ("Unni Krishnan v. State of Andhra Pradesh (Right to education up to age 14 under Art 45 integrated into Art 21)", "உன்னிகிருஷ்ணன் எதிராக ஆந்திரப் பிரதேச மாநிலம் (பிரிவு 45-ன் 14 வயது வரையிலான கல்வி உரிமை பிரிவு 21-ல் இணைக்கப்படல்)")
    ],
    ["2 -> 1 -> 4 -> 3", "3 -> 1 -> 2 -> 4", "4 -> 2 -> 1 -> 3", "1 -> 2 -> 3 -> 4"],
    "D",
    "Correct Chronological Sequence: 1. F.N. Balsara (1951) -> 2. Randhir Singh (1982) -> 3. Olga Tellis (1985) -> 4. Unni Krishnan (1993).",
    "சரியான காலவரிசை: 1. எஃப்.என். பால்சாரா (1951) -> 2. ரந்தீர் சிங் (1982) -> 3. ஓல்கா டெல்லிஸ் (1985) -> 4. உன்னிகிருஷ்ணன் (1993).",
    {
        "A": ("Incorrect. F.N. Balsara (1951) was decided 31 years before Randhir Singh (1982).", "தவறு. எஃப்.என். பால்சாரா (1951) ரந்தீர் சிங் (1982) வழக்கிற்கு 31 ஆண்டுகளுக்கு முன்பே தீர்ப்பளிக்கப்பட்டது."),
        "B": ("Incorrect. Randhir Singh (1982) was decided before Olga Tellis (1985).", "தவறு. ரந்தீர் சிங் (1982) ஓல்கா டெல்லிஸ் (1985) வழக்கிற்கு முன்பே தீர்ப்பளிக்கப்பட்டது."),
        "C": ("Incorrect. Olga Tellis (1985) was decided after Balsara (1951) and Randhir Singh (1982).", "தவறு. ஓல்கா டெல்லிஸ் (1985) பால்சாரா மற்றும் ரந்தீர் சிங் வழக்குகளுக்குப் பிறகே வந்தது."),
        "D": ("Correct. 1951 -> 1982 -> 1985 -> 1993 strictly follows the historic sequence of cases expanding Article 21 using Part IV directives.", "சரி. 1951 -> 1982 -> 1985 -> 1993 பகுதி IV நெறிமுறைகளைப் பயன்படுத்தி பிரிவு 21-ஐ விரிவுபடுத்திய வழக்குகளின் சரியான காலவரிசையைப் பின்பற்றுகிறது.")
    },
    "Since the late 1970s, the SC adopted the doctrine of harmonisation, reading DPSP into Part III to broaden the scope of fundamental rights.",
    "1970-களின் பிற்பகுதியிலிருந்து, உச்சநீதிமன்றம் இணக்கக் கோட்பாட்டை ஏற்றுக்கொண்டு, அடிப்படை உரிமைகளின் வரம்பை விரிவுபடுத்த பகுதி IV நெறிமுறைகளைப் பகுதி III-ல் சேர்த்துப் படித்தது.",
    "This judicial innovation transformed non-justiciable directives into enforceable rights under Article 21.",
    "இந்த நீதித்துறை விசித்திரம் நீதிமன்றத்தால் அமல்படுத்த முடியாத நெறிமுறைகளைப் பிரிவு 21-ன் கீழ் அமல்படுத்தக்கூடிய உரிமைகளாக மாற்றியது."
))

# Q21 (Hard - A)
q_data.append(make_q(
    "DPSP_CHRONO_021", "Hard",
    "Arrange the following Constitutional Amendments introducing modern socio-economic directives into Part IV in correct chronological order:\n\n1. 42nd Amendment Act (Added Article 43A - Workers' participation in management of industries)\n2. 44th Amendment Act (Added Article 38(2) - Minimising inequalities in status, facilities & opportunities)\n3. 86th Amendment Act (Substituted Article 45 - Focus on early childhood care & education for children under 6 years)\n4. 97th Amendment Act (Added Article 43B - Promotion of voluntary formation of co-operative societies)",
    "பகுதி IV-ல் நவீன சமூக-பொருளாதார நெறிமுறைகளை அறிமுகப்படுத்திய பின்வரும் அரசியலமைப்பு திருத்தங்களைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:\n\n1. 42-வது திருத்தச் சட்டம் (பிரிவு 43A சேர்க்கப்பட்டது - தொழிற்துறை மேலாண்மையில் தொழிலாளர்களின் பங்கேற்பு)\n2. 44-வது திருத்தச் சட்டம் (பிரிவு 38(2) சேர்க்கப்பட்டது - அந்தஸ்து, வசதிகள் & வாய்ப்புகளில் ஏற்றத்தாழ்வுகளைக் குறைத்தல்)\n3. 86-வது திருத்தச் சட்டம் (பிரிவு 45 மாற்றப்பட்டது - 6 வயதிற்குட்பட்ட குழந்தைகளுக்கு ஆரம்பகால குழந்தை பராமரிப்பு & கல்வி)\n4. 97-வது திருத்தச் சட்டம் (பிரிவு 43B சேர்க்கப்பட்டது - கூட்டுறவு சங்கங்களின் தன்னாட்சி உருவாக்கத்தை ஊக்குவித்தல்)",
    [
        ("42nd Amendment Act (Added Article 43A - Workers' participation in management of industries)", "42-வது திருத்தச் சட்டம் (பிரிவு 43A சேர்க்கப்பட்டது - தொழிற்துறை மேலாண்மையில் தொழிலாளர்களின் பங்கேற்பு)"),
        ("44th Amendment Act (Added Article 38(2) - Minimising inequalities in status, facilities & opportunities)", "44-வது திருத்தச் சட்டம் (பிரிவு 38(2) சேர்க்கப்பட்டது - அந்தஸ்து, வசதிகள் & வாய்ப்புகளில் ஏற்றத்தாழ்வுகளைக் குறைத்தல்)"),
        ("86th Amendment Act (Substituted Article 45 - Focus on early childhood care & education for children under 6 years)", "86-வது திருத்தச் சட்டம் (பிரிவு 45 மாற்றப்பட்டது - 6 வயதிற்குட்பட்ட குழந்தைகளுக்கு ஆரம்பகால குழந்தை பராமரிப்பு & கல்வி)"),
        ("97th Amendment Act (Added Article 43B - Promotion of voluntary formation of co-operative societies)", "97-வது திருத்தச் சட்டம் (பிரிவு 43B சேர்க்கப்பட்டது - கூட்டுறவு சங்கங்களின் தன்னாட்சி உருவாக்கத்தை ஊக்குவித்தல்)")
    ],
    ["1 -> 2 -> 3 -> 4", "2 -> 1 -> 4 -> 3", "3 -> 1 -> 2 -> 4", "4 -> 3 -> 1 -> 2"],
    "A",
    "Correct Chronological Sequence: 1. 42nd Amendment (1976) -> 2. 44th Amendment (1978) -> 3. 86th Amendment (2002) -> 4. 97th Amendment (2011).",
    "சரியான காலவரிசை: 1. 42-வது திருத்தம் (1976) -> 2. 44-வது திருத்தம் (1978) -> 3. 86-வது திருத்தம் (2002) -> 4. 97-வது திருத்தம் (2011).",
    {
        "A": ("Correct. 1976 -> 1978 -> 2002 -> 2011 correctly arranges the modern constitutional amendments to Part IV.", "சரி. 1976 -> 1978 -> 2002 -> 2011 பகுதி IV-ல் செய்யப்பட்ட நவீன அரசியலமைப்பு திருத்தங்களைச் சரியாக வரிசைப்படுத்துகிறது."),
        "B": ("Incorrect. 42nd Amendment (1976) came before 44th Amendment (1978).", "தவறு. 42-வது திருத்தம் (1976) 44-வது திருத்தத்திற்கு (1978) முன்பே வந்தது."),
        "C": ("Incorrect. 44th Amendment (1978) was enacted before 86th Amendment (2002).", "தவறு. 44-வது திருத்தம் (1978) 86-வது திருத்தத்திற்கு (2002) முன்பே இயற்றப்பட்டது."),
        "D": ("Incorrect. 86th Amendment (2002) was passed long after the 42nd Amendment (1976).", "தவறு. 86-வது திருத்தம் (2002) 42-வது திருத்தத்திற்கு (1976) பல ஆண்டுகளுக்குப் பிறகே நிறைவேற்றப்பட்டது.")
    },
    "Do not confuse Article 43A (Workers' participation in management - added by 42nd Amendment 1976) with Article 43B (Co-operative societies - added by 97th Amendment 2011).",
    "பிரிவு 43A (மேலாண்மையில் தொழிலாளர் பங்கேற்பு - 42-வது திருத்தம் 1976) மற்றும் பிரிவு 43B (கூட்டுறவு சங்கங்கள் - 97-வது திருத்தம் 2011) ஆகியவற்றை குழப்பிக் கொள்ளக் கூடாது.",
    "Article 43A belongs to Socialistic Directives, whereas Article 43B belongs to Gandhian/Liberal-Intellectual Directives.",
    "பிரிவு 43A சோசலிச நெறிமுறைகளைச் சேர்ந்தது, அதே வேளையில் பிரிவு 43B காந்திய/தாராளமய-அறிவுசார் நெறிமுறைகளைச் சேர்ந்தது."
))

# Q22 (Hard - B)
q_data.append(make_q(
    "DPSP_CHRONO_022", "Hard",
    "Arrange the following Supreme Court judgments interpreting Directive Principles in REVERSE chronological order (latest to earliest):\n\n1. State of Gujarat v. Mirzapur Moti Kureshi Kassab Jamat (Upheld total ban on cow slaughter under Art 48 & 48A)\n2. Unni Krishnan v. State of Andhra Pradesh (Declared Right to Education up to age 14 a Fundamental Right under Art 21)\n3. Minerva Mills v. Union of India (Declared harmony between Part III and Part IV a Basic Structure)\n4. State of Madras v. Champakam Dorairajan (Declared DPSP subsidiary to Fundamental Rights)",
    "அரசு நெறிமுறைப்படுத்தும் கோட்பாடுகளை விளக்கிய உச்சநீதிமன்றத் தீர்ப்புகளைத் தலைகீழ் காலவரிசைப்படி (பிந்தையது முதல் முந்தையது வரை) வரிசைப்படுத்தவும்:\n\n1. குஜராத் மாநிலம் எதிராக மிர்சாபூர் மோதி குரேஷி கசாப் ஜமாத் (பிரிவு 48 & 48A-ன் கீழ் பசு வதை முழு தடை உறுதிப்பாட்டுத் தீர்ப்பு)\n2. உன்னிகிருஷ்ணன் எதிராக ஆந்திரப் பிரதேச மாநிலம் (பிரிவு 21-ன் கீழ் 14 வயது வரையிலான கல்வி உரிமை அடிப்படை உரிமை எனத் தீர்ப்பு)\n3. மினர்வா மில்ஸ் எதிராக இந்திய யூனியன் (பகுதி III மற்றும் பகுதி IV இடையேயான இணக்கம் அடிப்படை அமைப்பு எனத் தீர்ப்பு)\n4. மதராஸ் மாநிலம் எதிராக செம்பகம் துரைராஜன் (அரசு நெறிமுறைக் கோட்பாடுகள் அடிப்படை உரிமைகளுக்கு துணையானவை எனத் தீர்ப்பு)",
    [
        ("State of Gujarat v. Mirzapur Moti Kureshi Kassab Jamat (Upheld total ban on cow slaughter under Art 48 & 48A)", "குஜராத் மாநிலம் எதிராக மிர்சாபூர் மோதி குரேஷி கசாப் ஜமாத் (பிரிவு 48 & 48A-ன் கீழ் பசு வதை முழு தடை உறுதிப்பாட்டுத் தீர்ப்பு)"),
        ("Unni Krishnan v. State of Andhra Pradesh (Declared Right to Education up to age 14 a Fundamental Right under Art 21)", "உன்னிகிருஷ்ணன் எதிராக ஆந்திரப் பிரதேச மாநிலம் (பிரிவு 21-ன் கீழ் 14 வயது வரையிலான கல்வி உரிமை அடிப்படை உரிமை எனத் தீர்ப்பு)"),
        ("Minerva Mills v. Union of India (Declared harmony between Part III and Part IV a Basic Structure)", "மினர்வா மில்ஸ் எதிராக இந்திய யூனியன் (பகுதி III மற்றும் பகுதி IV இடையேயான இணக்கம் அடிப்படை அமைப்பு எனத் தீர்ப்பு)"),
        ("State of Madras v. Champakam Dorairajan (Declared DPSP subsidiary to Fundamental Rights)", "மதராஸ் மாநிலம் எதிராக செம்பகம் துரைராஜன் (அரசு நெறிமுறைக் கோட்பாடுகள் அடிப்படை உரிமைகளுக்கு துணையானவை எனத் தீர்ப்பு)")
    ],
    ["4 -> 3 -> 2 -> 1", "1 -> 2 -> 3 -> 4", "2 -> 4 -> 1 -> 3", "3 -> 1 -> 4 -> 2"],
    "B",
    "Correct Reverse Chronological Sequence (Latest to Earliest): 1. Mirzapur Moti Kureshi (2005) -> 2. Unni Krishnan (1993) -> 3. Minerva Mills (1980) -> 4. Champakam Dorairajan (1951).",
    "சரியான தலைகீழ் காலவரிசை (பிந்தையது முதல் முந்தையது வரை): 1. மிர்சாபூர் மோதி குரேஷி (2005) -> 2. உன்னிகிருஷ்ணன் (1993) -> 3. மினர்வா மில்ஸ் (1980) -> 4. செம்பகம் துரைராஜன் (1951).",
    {
        "A": ("Incorrect. 4 -> 3 -> 2 -> 1 represents earliest to latest sequence.", "தவறு. 4 -> 3 -> 2 -> 1 என்பது முந்தையது முதல் பிந்தையது வரையிலான வரிசையாகும்."),
        "B": ("Correct. 2005 (Mirzapur) -> 1993 (Unni Krishnan) -> 1980 (Minerva Mills) -> 1951 (Champakam) follows latest to earliest sequence.", "சரி. 2005 (மிர்சாபூர்) -> 1993 (உன்னிகிருஷ்ணன்) -> 1980 (மினர்வா மில்ஸ்) -> 1951 (செம்பகம்) பிந்தையது முதல் முந்தையது வரையிலான வரிசையைப் பின்பற்றுகிறது."),
        "C": ("Incorrect. Mirzapur Moti Kureshi (2005) was decided after Unni Krishnan (1993).", "தவறு. மிர்சாபூர் மோதி குரேஷி (2005) உன்னிகிருஷ்ணன் (1993) வழக்கிற்குப் பிறகே தீர்ப்பளிக்கப்பட்டது."),
        "D": ("Incorrect. Minerva Mills (1980) was decided before Mirzapur Moti Kureshi (2005).", "தவறு. மினர்வா மில்ஸ் (1980) மிர்சாபூர் மோதி குரேஷி (2005) வழக்கிற்கு முன்பே தீர்ப்பளிக்கப்பட்டது.")
    },
    "In Mirzapur Moti Kureshi (2005), the SC highlighted that Directive Principles and Fundamental Duties (Article 51A(g)) must be read together to determine the reasonableness of restrictions under Article 19.",
    "மிர்சாபூர் மோதி குரேஷி (2005) வழக்கில், பிரிவு 19-ன் கீழ் நியாயமான கட்டுப்பாடுகளைத் தீர்மானிக்க அரசு நெறிமுறைக் கோட்பாடுகளையும் அடிப்படை கடமைகளையும் (பிரிவு 51A(g)) ஒன்றாகப் படிக்க வேண்டும் என உச்சநீதிமன்றம் சுட்டிக்காட்டியது.",
    "This judgment established that restrictions imposed to implement DPSP Article 48 and 48A are presumptively reasonable.",
    "பிரிவு 48 மற்றும் 48A DPSP-ஐ அமல்படுத்த விதிக்கப்படும் கட்டுப்பாடுகள் நியாயமானவை என்ற அனுமானத்தை இந்தத் தீர்ப்பு நிறுவியது."
))

# Q23 (Hard - C)
q_data.append(make_q(
    "DPSP_CHRONO_023", "Hard",
    "Arrange the following landmark Supreme Court cases involving DPSP interpretation in correct chronological order:\n\n1. Champakam Dorairajan v. State of Madras (1951 - DPSP subordinated to Fundamental Rights)\n2. Kesavananda Bharati v. State of Kerala (1973 - Basic structure doctrine & Article 31C part-invalidation)\n3. Hussainara Khatoon v. Home Secretary, Bihar (1979 - Free legal aid under Art 39A read into Art 21)\n4. State of Tamil Nadu v. L. Abu Kavur Bai (1984 - Protection of transport nationalisation scheme under Art 31C)",
    "அரசு நெறிமுறைக் கோட்பாடுகள் விளக்கத்தை உள்ளடக்கிய பின்வரும் முக்கிய உச்சநீதிமன்ற வழக்குகளைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:\n\n1. மதராஸ் மாநிலம் எதிராக செம்பகம் துரைராஜன் (1951 - நெறிமுறைக் கோட்பாடுகள் அடிப்படை உரிமைகளுக்கு கீழ்ப்படுத்தப்படல்)\n2. கேசவாநந்த பாரதி எதிராக கேரள மாநிலம் (1973 - அடிப்படை அமைப்புக் கோட்பாடு & பிரிவு 31C பகுதி ரத்து)\n3. ஹுசைனாரா கதூன் எதிராக பீகார் உள்துறைச் செயலர் (1979 - பிரிவு 39A-ன் இலவச சட்ட உதவி பிரிவு 21-ல் படிக்கப்படல்)\n4. தமிழ்நாடு மாநிலம் எதிராக எல். அபு கவூர் பாய் (1984 - பிரிவு 31C-ன் கீழ் போக்குவரத்து தேசியமயமாக்கல் திட்டப் பாதுகாப்பு)",
    [
        ("Champakam Dorairajan v. State of Madras (1951 - DPSP subordinated to Fundamental Rights)", "மதராஸ் மாநிலம் எதிராக செம்பகம் துரைராஜன் (1951 - நெறிமுறைக் கோட்பாடுகள் அடிப்படை உரிமைகளுக்கு கீழ்ப்படுத்தப்படல்)"),
        ("Kesavananda Bharati v. State of Kerala (1973 - Basic structure doctrine & Article 31C part-invalidation)", "கேசவாநந்த பாரதி எதிராக கேரள மாநிலம் (1973 - அடிப்படை அமைப்புக் கோட்பாடு & பிரிவு 31C பகுதி ரத்து)"),
        ("Hussainara Khatoon v. Home Secretary, Bihar (1979 - Free legal aid under Art 39A read into Art 21)", "ஹுசைனாரா கதூன் எதிராக பீகார் உள்துறைச் செயலர் (1979 - பிரிவு 39A-ன் இலவச சட்ட உதவி பிரிவு 21-ல் படிக்கப்படல்)"),
        ("State of Tamil Nadu v. L. Abu Kavur Bai (1984 - Protection of transport nationalisation scheme under Art 31C)", "தமிழ்நாடு மாநிலம் எதிராக எல். அபு கவூர் பாய் (1984 - பிரிவு 31C-ன் கீழ் போக்குவரத்து தேசியமயமாக்கல் திட்டப் பாதுகாப்பு)")
    ],
    ["2 -> 1 -> 4 -> 3", "3 -> 1 -> 2 -> 4", "1 -> 2 -> 3 -> 4", "4 -> 2 -> 1 -> 3"],
    "C",
    "Correct Chronological Sequence: 1. Champakam Dorairajan (1951) -> 2. Kesavananda Bharati (1973) -> 3. Hussainara Khatoon (1979) -> 4. Abu Kavur Bai (1984).",
    "சரியான காலவரிசை: 1. செம்பகம் துரைராஜன் (1951) -> 2. கேசவாநந்த பாரதி (1973) -> 3. ஹுசைனாரா கதூன் (1979) -> 4. அபு கவூர் பாய் (1984).",
    {
        "A": ("Incorrect. Champakam Dorairajan (1951) was decided long before Kesavananda Bharati (1973).", "தவறு. செம்பகம் துரைராஜன் (1951) கேசவாநந்த பாரதி (1973) வழக்கிற்கு பல ஆண்டுகளுக்கு முன்பே தீர்ப்பளிக்கப்பட்டது."),
        "B": ("Incorrect. Kesavananda Bharati (1973) preceded Hussainara Khatoon (1979).", "தவறு. கேசவாநந்த பாரதி (1973) ஹுசைனாரா கதூன் (1979) வழக்கிற்கு முந்தையது."),
        "C": ("Correct. 1951 -> 1973 -> 1979 -> 1984 represents the exact chronological progression of DPSP case law.", "சரி. 1951 -> 1973 -> 1979 -> 1984 அரசு நெறிமுறைக் கோட்பாட்டு வழக்குகளின் சரியான காலவரிசையைப் பிரதிபலிக்கிறது."),
        "D": ("Incorrect. Hussainara Khatoon (1979) was decided after Champakam Dorairajan (1951).", "தவறு. ஹுசைனாரா கதூன் (1979) செம்பகம் துரைராஜன் (1951) வழக்கிற்குப் பிறகே தீர்ப்பளிக்கப்பட்டது.")
    },
    "In Abu Kavur Bai (1984), a 5-judge Constitution Bench held that Tamil Nadu Stage Carriages (Acquisition) Act was enacted to distribute material resources under Article 39(b) & (c) and thus enjoyed Article 31C immunity.",
    "அபு கவூர் பாய் (1984) வழக்கில், 5 நீதிபதிகள் கொண்ட அமர்வு, தமிழ்நாடு பேருந்து (கையகப்படுத்துதல்) சட்டம் பிரிவு 39(b) & (c)-ன் கீழ் வளங்களை விநியோகிக்க இயற்றப்பட்டதால் பிரிவு 31C பாதுகாப்பைப் பெறுகிறது எனத் தீர்ப்பளித்தது.",
    "This judgment reaffirmed that state nationalisation schemes carrying out Article 39(b) directives cannot be challenged under Articles 14 or 19.",
    "பிரிவு 39(b) நெறிமுறைகளை நிறைவேற்றும் மாநில தேசியமயமாக்கல் திட்டங்களைப் பிரிவு 14 அல்லது 19-ன் கீழ் சவால் செய்ய முடியாது என்பதை இந்தத் தீர்ப்பு மீண்டும் உறுதிப்படுத்தியது."
))

# Q24 (Hard - D)
q_data.append(make_q(
    "DPSP_CHRONO_024", "Hard",
    "Arrange the following milestones in the evolution of Environmental Protection Directives in Part IV in correct chronological order:\n\n1. Adoption of original Constitution (Article 48 included directing state to organise agriculture and animal husbandry)\n2. Enactment of Wildlife Protection Act (Passed by Parliament prior to explicit environmental DPSP amendment)\n3. Enactment of 42nd Constitutional Amendment Act (Inserted Article 48A explicitly creating environmental duty for State)\n4. Enactment of Environment Protection Act (Passed by Parliament as umbrella legislation implementing Article 48A)",
    "பகுதி IV-ல் சுற்றுச்சூழல் பாதுகாப்பு நெறிமுறைகளின் வளர்ச்சியிலுள்ள மைல்கற்களைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:\n\n1. மூல அரசியலமைப்பு ஏற்றுக்கொள்ளப்படல் (வேளாண்மை மற்றும் கால்நடை பராமரிப்பை அமைக்க அரசைப் பணிக்கும் பிரிவு 48 சேர்க்கப்படல்)\n2. வனவிலங்கு பாதுகாப்புச் சட்டம் இயற்றப்படல் (தெளிவான சுற்றுச்சூழல் நெறிமுறை திருத்தத்திற்கு முன்பே நாடாளுமன்றத்தால் நிறைவேற்றப்படல்)\n3. 42-வது அரசியலமைப்பு திருத்தச் சட்டம் இயற்றப்படல் (அரசுக்கு சுற்றுச்சூழல் கடமையை உருவாக்கும் பிரிவு 48A தெளிவாக்கச் சேர்க்கப்படல்)\n4. சுற்றுச்சூழல் பாதுகாப்புச் சட்டம் இயற்றப்படல் (பிரிவு 48A-ஐ அமல்படுத்தும் குடைச் சட்டமாக நாடாளுமன்றத்தால் நிறைவேற்றப்படல்)",
    [
        ("Adoption of original Constitution (Article 48 included directing state to organise agriculture and animal husbandry)", "மூல அரசியலமைப்பு ஏற்றுக்கொள்ளப்படல் (வேளாண்மை மற்றும் கால்நடை பராமரிப்பை அமைக்க அரசைப் பணிக்கும் பிரிவு 48 சேர்க்கப்படல்)"),
        ("Enactment of Wildlife Protection Act (Passed by Parliament prior to explicit environmental DPSP amendment)", "வனவிலங்கு பாதுகாப்புச் சட்டம் இயற்றப்படல் (தெளிவான சுற்றுச்சூழல் நெறிமுறை திருத்தத்திற்கு முன்பே நாடாளுமன்றத்தால் நிறைவேற்றப்படல்)"),
        ("Enactment of 42nd Constitutional Amendment Act (Inserted Article 48A explicitly creating environmental duty for State)", "42-வது அரசியலமைப்பு திருத்தச் சட்டம் இயற்றப்படல் (அரசுக்கு சுற்றுச்சூழல் கடமையை உருவாக்கும் பிரிவு 48A தெளிவாக்கச் சேர்க்கப்படல்)"),
        ("Enactment of Environment Protection Act (Passed by Parliament as umbrella legislation implementing Article 48A)", "சுற்றுச்சூழல் பாதுகாப்புச் சட்டம் இயற்றப்படல் (பிரிவு 48A-ஐ அமல்படுத்தும் குடைச் சட்டமாக நாடாளுமன்றத்தால் நிறைவேற்றப்படல்)")
    ],
    ["2 -> 1 -> 4 -> 3", "3 -> 1 -> 2 -> 4", "4 -> 2 -> 1 -> 3", "1 -> 2 -> 3 -> 4"],
    "D",
    "Correct Chronological Sequence: 1. Original Constitution (1950) -> 2. Wildlife Protection Act (1972) -> 3. 42nd Amendment (1976) -> 4. Environment Protection Act (1986).",
    "சரியான காலவரிசை: 1. மூல அரசியலமைப்பு (1950) -> 2. வனவிலங்கு பாதுகாப்புச் சட்டம் (1972) -> 3. 42-வது திருத்தம் (1976) -> 4. சுற்றுச்சூழல் பாதுகாப்புச் சட்டம் (1986).",
    {
        "A": ("Incorrect. Wildlife Protection Act (1972) was passed after the Constitution came into force in 1950.", "தவறு. வனவிலங்கு பாதுகாப்புச் சட்டம் (1972) 1950-ல் அரசியலமைப்பு அமலுக்கு வந்த பிறகே நிறைவேற்றப்பட்டது."),
        "B": ("Incorrect. Wildlife Protection Act (1972) came before 42nd Amendment (1976).", "தவறு. வனவிலங்கு பாதுகாப்புச் சட்டம் (1972) 42-வது திருத்தத்திற்கு (1976) முன்பே வந்தது."),
        "C": ("Incorrect. 42nd Amendment (1976) was enacted after 1950 and 1972.", "தவறு. 42-வது திருத்தம் (1976) 1950 மற்றும் 1972-க்கு பிறகே இயற்றப்பட்டது."),
        "D": ("Correct. 1950 -> 1972 -> 1976 -> 1986 accurately follows the environmental protection directive timeline in India.", "சரி. 1950 -> 1972 -> 1976 -> 1986 இந்தியாவில் சுற்றுச்சூழல் பாதுகாப்பு நெறிமுறை காலவரிசையைத் துல்லியமாகப் பின்பற்றுகிறது.")
    },
    "Do not confuse Article 48 (Agriculture & Animal Husbandry - original 1950) with Article 48A (Protection of Environment, Forests & Wildlife - added by 42nd Amendment 1976).",
    "பிரிவு 48 (வேளாண்மை & கால்நடை பராமரிப்பு - மூல 1950) மற்றும் பிரிவு 48A (சுற்றுச்சூழல், காடுகள் & வனவிலங்கு பாதுகாப்பு - 42-வது திருத்தம் 1976) ஆகியவற்றை குழப்பிக் கொள்ளக் கூடாது.",
    "While Article 48 belongs to Gandhian and Agricultural Directives, Article 48A belongs to Liberal-Intellectual and Ecological Directives.",
    "பிரிவு 48 காந்திய மற்றும் வேளாண்மை நெறிமுறைகளைச் சேர்ந்தது, அதே வேளையில் பிரிவு 48A தாராளமய-அறிவுசார் மற்றும் சுற்றுச்சூழல் நெறிமுறைகளைச் சேர்ந்தது."
))

# Q25 (Hard - D)
q_data.append(make_q(
    "DPSP_CHRONO_025", "Hard",
    "Arrange the following comprehensive list of Constitutional Amendments modifying Part IV Directive Principles in correct chronological order:\n\n1. 1st Constitutional Amendment Act (Added Articles 31A & 31B protecting DPSP land reform laws)\n2. 42nd Constitutional Amendment Act (Added Articles 39A, 43A, 48A and modified Article 39(f))\n3. 73rd Constitutional Amendment Act (Added Part IX and 11th Schedule implementing Article 40)\n4. 86th Constitutional Amendment Act (Substituted Article 45 and inserted Article 21A)",
    "பகுதி IV அரசு நெறிமுறைக் கோட்பாடுகளை மாற்றியமைத்த பின்வரும் விரிவான அரசியலமைப்பு திருத்தங்களைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:\n\n1. 1-வது அரசியலமைப்பு திருத்தச் சட்டம் (DPSP நிலச்சீர்திருத்தச் சட்டங்களைப் பாதுகாக்கும் பிரிவுகள் 31A & 31B சேர்க்கப்படல்)\n2. 42-வது அரசியலமைப்பு திருத்தச் சட்டம் (பிரிவுகள் 39A, 43A, 48A சேர்க்கப்பட்டு பிரிவு 39(f) திருத்தப்படல்)\n3. 73-வது அரசியலமைப்பு திருத்தச் சட்டம் (பிரிவு 40-ஐ அமல்படுத்தும் பகுதி IX மற்றும் 11-வது அட்டவணை சேர்க்கப்படல்)\n4. 86-வது அரசியலமைப்பு திருத்தச் சட்டம் (பிரிவு 45 மாற்றப்பட்டு பிரிவு 21A சேர்க்கப்படல்)",
    [
        ("1st Constitutional Amendment Act (Added Articles 31A & 31B protecting DPSP land reform laws)", "1-வது அரசியலமைப்பு திருத்தச் சட்டம் (DPSP நிலச்சீர்திருத்தச் சட்டங்களைப் பாதுகாக்கும் பிரிவுகள் 31A & 31B சேர்க்கப்படல்)"),
        ("42nd Constitutional Amendment Act (Added Articles 39A, 43A, 48A and modified Article 39(f))", "42-வது அரசியலமைப்பு திருத்தச் சட்டம் (பிரிவுகள் 39A, 43A, 48A சேர்க்கப்பட்டு பிரிவு 39(f) திருத்தப்படல்)"),
        ("73rd Constitutional Amendment Act (Added Part IX and 11th Schedule implementing Article 40)", "73-வது அரசியலமைப்பு திருத்தச் சட்டம் (பிரிவு 40-ஐ அமல்படுத்தும் பகுதி IX மற்றும் 11-வது அட்டவணை சேர்க்கப்படல்)"),
        ("86th Constitutional Amendment Act (Substituted Article 45 and inserted Article 21A)", "86-வது அரசியலமைப்பு திருத்தச் சட்டம் (பிரிவு 45 மாற்றப்பட்டு பிரிவு 21A சேர்க்கப்படல்)")
    ],
    ["2 -> 1 -> 4 -> 3", "3 -> 1 -> 2 -> 4", "4 -> 2 -> 1 -> 3", "1 -> 2 -> 3 -> 4"],
    "D",
    "Correct Chronological Sequence: 1. 1st Amendment (1951) -> 2. 42nd Amendment (1976) -> 3. 73rd Amendment (1992) -> 4. 86th Amendment (2002).",
    "சரியான காலவரிசை: 1. 1-வது திருத்தம் (1951) -> 2. 42-வது திருத்தம் (1976) -> 3. 73-வது திருத்தம் (1992) -> 4. 86-வது திருத்தம் (2002).",
    {
        "A": ("Incorrect. 1st Amendment (1951) was passed before 42nd Amendment (1976).", "தவறு. 1-வது திருத்தம் (1951) 42-வது திருத்தத்திற்கு (1976) முன்பே நிறைவேற்றப்பட்டது."),
        "B": ("Incorrect. 42nd Amendment (1976) was passed before 73rd Amendment (1992).", "தவறு. 42-வது திருத்தம் (1976) 73-வது திருத்தத்திற்கு (1992) முன்பே நிறைவேற்றப்பட்டது."),
        "C": ("Incorrect. 73rd Amendment (1992) was enacted after 1st Amendment (1951).", "தவறு. 73-வது திருத்தம் (1992) 1-வது திருத்தத்திற்கு (1951) பிறகே இயற்றப்பட்டது."),
        "D": ("Correct. 1951 -> 1976 -> 1992 -> 2002 follows the exact enactment chronology of constitutional amendments implementing and modifying Part IV.", "சரி. 1951 -> 1976 -> 1992 -> 2002 பகுதி IV-ஐ அமல்படுத்திய மற்றும் மாற்றியமைத்த அரசியலமைப்பு திருத்தங்களின் சரியான காலவரிசையைப் பின்பற்றுகிறது.")
    },
    "Remember that 73rd Amendment (1992) implemented Article 40 (Panchayati Raj), while 86th Amendment (2002) implemented Article 45 (Education).",
    "73-வது திருத்தம் (1992) பிரிவு 40-ஐயும் (பஞ்சாயத்து ராஜ்), 86-வது திருத்தம் (2002) பிரிவு 45-ஐயும் (கல்வி) அமல்படுத்தியது என்பதை நினைவில் கொள்க.",
    "Together with the 44th (1978) and 97th (2011) Amendments, these form the complete constitutional amendment history of Part IV.",
    "44-வது (1978) மற்றும் 97-வது (2011) திருத்தங்களுடன் சேர்ந்து, இவை பகுதி IV-ன் முழுமையான அரசியலமைப்பு திருத்த வரலாற்றை உருவாக்குகின்றன."
))

out_path = 'data/questions/polity/directive_principles_chronology.json'
os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(q_data, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {len(q_data)} questions in {out_path}.")
