import json
import os

q_data = []

def make_q(q_id, difficulty, qtype, q_en, q_ta, options_list, ca, exp_en, exp_ta, wno_dict, trap_en, trap_ta, fact_en, fact_ta, source_list, is_exact_pyq=False, bloom="Remember", est_time=45, tags=None):
    if tags is None:
        tags = ["Polity", "Directive Principles of State Policy", "PYQ"]
        
    options = []
    options_en = []
    options_ta = []
    for opt_id, (opt_en, opt_ta) in zip(["A", "B", "C", "D"], options_list):
        options.append({"id": opt_id, "en": opt_en, "ta": opt_ta})
        options_en.append(opt_en)
        options_ta.append(opt_ta)
        
    wno = {}
    for letter in ["A", "B", "C", "D"]:
        wno[letter] = {
            "en": wno_dict[letter][0],
            "ta": wno_dict[letter][1]
        }
        
    pyq_sim = "Exact PYQ" if is_exact_pyq else "PYQ Pattern"
    
    obj = {
        "id": q_id,
        "subject": "Polity",
        "topic": "Directive Principles of State Policy",
        "difficulty": difficulty,
        "question_type": qtype,
        "question": {"en": q_en, "ta": q_ta},
        "options": options,
        "correct_answer": ca,
        "explanation": {"en": exp_en, "ta": exp_ta},
        "why_not_others": wno,
        "tnpsc_tip": {"en": f"TNPSC Trap: {trap_en}", "ta": f"TNPSC பொறி: {trap_ta}"},
        "revision_fact": {"en": fact_en, "ta": fact_ta},
        "source_reference": source_list,
        "bloom_level": bloom,
        "estimated_time_sec": est_time,
        "pyq_similarity": pyq_sim,
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

# Q1 (Exact PYQ - Group 1 2022) - Answer C
q_data.append(make_q(
    "DPSP_PYQ_001", "Easy", "Direct MCQ",
    "Which Part of the Constitution of India contains the Directive Principles of State Policy (Articles 36 to 51)?",
    "இந்திய அரசியலமைப்பின் எந்தப் பகுதியில் அரசு நெறிமுறைப்படுத்தும் கோட்பாடுகள் (பிரிவுகள் 36 முதல் 51 வரை) இடம் பெற்றுள்ளன?",
    [
        ("Part II", "பகுதி II"),
        ("Part III", "பகுதி III"),
        ("Part IV", "பகுதி IV"),
        ("Part V", "பகுதி V")
    ],
    "C",
    "Part IV of the Indian Constitution (Articles 36 to 51) deals with the Directive Principles of State Policy.",
    "இந்திய அரசியலமைப்பின் பகுதி IV (பிரிவுகள் 36 முதல் 51) அரசு நெறிமுறைப்படுத்தும் கோட்பாடுகளைக் கையாள்கிறது.",
    {
        "A": ("Incorrect. Part II deals with Citizenship (Articles 5-11).", "தவறு. பகுதி II குடியுரிமையைக் கையாள்கிறது (பிரிவுகள் 5-11)."),
        "B": ("Incorrect. Part III deals with Fundamental Rights (Articles 12-35).", "தவறு. பகுதி III அடிப்படை உரிமைகளைக் கையாள்கிறது (பிரிவுகள் 12-35)."),
        "C": ("Correct. Part IV contains DPSP from Articles 36 to 51.", "சரி. பகுதி IV பிரிவுகள் 36 முதல் 51 வரையிலான DPSP-ஐக் கொண்டுள்ளது."),
        "D": ("Incorrect. Part V deals with the Union Government (Articles 52-151).", "தவறு. பகுதி V மத்திய அரசாங்கத்தைக் கையாள்கிறது (பிரிவுகள் 52-151).")
    },
    "Part III = Fundamental Rights. Part IV = Directive Principles of State Policy. Part IVA = Fundamental Duties.",
    "பகுதி III = அடிப்படை உரிமைகள். பகுதி IV = அரசு நெறிமுறைக் கோட்பாடுகள். பகுதி IVA = அடிப்படைக் கடமைகள்.",
    "Part IV was inspired by the Constitution of Ireland (1937).",
    "பகுதி IV 1937-ம் ஆண்டின் அயர்லாந்து அரசியலமைப்பிலிருந்து ஈர்க்கப்பட்டது.",
    ["TNPSC Group 1 2022 PYQ", "M. Laxmikanth - Indian Polity"],
    is_exact_pyq=True
))

# Q2 (Exact PYQ - Group 1 2019) - Answer B
q_data.append(make_q(
    "DPSP_PYQ_002", "Easy", "Direct MCQ",
    "The Directive Principles of State Policy in the Indian Constitution were borrowed from the Constitution of which country?",
    "இந்திய அரசியலமைப்பில் உள்ள அரசு நெறிமுறைப்படுத்தும் கோட்பாடுகள் எந்த நாட்டின் அரசியலமைப்பிலிருந்து பெறப்பட்டன?",
    [
        ("United States of America", "அமெரிக்க ஐக்கிய நாடுகள்"),
        ("Ireland", "அயர்லாந்து"),
        ("USSR (Russia)", "ரஷ்யா"),
        ("Australia", "ஆஸ்திரேலியா")
    ],
    "B",
    "The Directive Principles of State Policy were borrowed from the Irish Constitution of 1937, which had copied them from the Spanish Constitution.",
    "அரசு நெறிமுறைப்படுத்தும் கோட்பாடுகள் 1937-ம் ஆண்டின் அயர்லாந்து அரசியலமைப்பிலிருந்து பெறப்பட்டவை.",
    {
        "A": ("Incorrect. Fundamental Rights and Judicial Review were borrowed from the USA.", "தவறு. அடிப்படை உரிமைகள் அமெரிக்காவிலிருந்து பெறப்பட்டவை."),
        "B": ("Correct. DPSP was explicitly borrowed from Ireland.", "சரி. DPSP அயர்லாந்திலிருந்து பெறப்பட்டது."),
        "C": ("Incorrect. Fundamental Duties were borrowed from USSR.", "தவறு. அடிப்படைக் கடமைகள் ரஷ்யாவிலிருந்து பெறப்பட்டவை."),
        "D": ("Incorrect. Concurrent List and Joint Sitting were borrowed from Australia.", "தவறு. பொதுப்பட்டியல் ஆஸ்திரேலியாவிலிருந்து பெறப்பட்டது.")
    },
    "Ireland copied DPSP from Spain, and India copied DPSP from Ireland.",
    "அயர்லாந்து DPSP-ஐ ஸ்பெயினிலிருந்து பெற்றது, இந்தியா DPSP-ஐ அயர்லாந்திலிருந்து பெற்றது.",
    "B.N. Rau, Constitutional Advisor, recommended incorporating DPSP from the Irish model.",
    "அரசியலமைப்பு ஆலோசகர் பி.என். ராவ் அயர்லாந்து மாதிரியிலிருந்து DPSP-ஐ சேர்க்க பரிந்துரைத்தார்.",
    ["TNPSC Group 1 2019 PYQ", "M. Laxmikanth - Indian Polity"],
    is_exact_pyq=True
))

# Q3 (Exact PYQ - Group 1 2017) - Answer B
q_data.append(make_q(
    "DPSP_PYQ_003", "Easy", "Direct MCQ",
    "Who among the following described the Directive Principles of State Policy as a 'Novel Feature' of the Constitution of India?",
    "பின்வருபவர்களில் யார் அரசு நெறிமுறைப்படுத்தும் கோட்பாடுகளை இந்திய அரசியலமைப்பின் 'புதுமையான அம்சம்' என்று விவரித்தார்?",
    [
        ("Jawaharlal Nehru", "ஜவஹர்லால் நேரு"),
        ("Dr. B.R. Ambedkar", "டாக்டர் பி.ஆர். அம்பேத்கர்"),
        ("Sardar Vallabhbhai Patel", "சர்தார் வல்லபாய் படேல்"),
        ("Dr. Rajendra Prasad", "டாக்டர் ராஜேந்திர பிரசாத்")
    ],
    "B",
    "Dr. B.R. Ambedkar described the Directive Principles of State Policy as a 'novel feature' of the Constitution of India.",
    "டாக்டர் பி.ஆர். அம்பேத்கர் அரசு நெறிமுறைப்படுத்தும் கோட்பாடுகளை இந்திய அரசியலமைப்பின் 'புதுமையான அம்சம்' என்று விவரித்தார்.",
    {
        "A": ("Incorrect. Jawaharlal Nehru introduced the Objectives Resolution.", "தவறு. ஜவஹர்லால் நேரு குறிக்கோள்கள் தீர்மானத்தைக் கொண்டுவந்தார்."),
        "B": ("Correct. Dr. B.R. Ambedkar coined the phrase 'novel feature' for DPSP.", "சரி. டாக்டர் பி.ஆர். அம்பேத்கர் DPSP-ஐ 'புதுமையான அம்சம்' என்று அழைத்தார்."),
        "C": ("Incorrect. Patel headed the Advisory Committee on Fundamental Rights.", "தவறு. படேல் அடிப்படை உரிமைகள் ஆலோசனைக் குழுவின் தலைவராக இருந்தார்."),
        "D": ("Incorrect. Dr. Rajendra Prasad was the President of Constituent Assembly.", "தவறு. டாக்டர் ராஜேந்திர பிரசாத் நிர்ணய அவையின் தலைவராக இருந்தார்.")
    },
    "Granville Austin called DPSP and Fundamental Rights the 'Conscience of the Constitution'. Ambedkar called DPSP a 'Novel Feature'.",
    "கிரான்வில் ஆஸ்டின் DPSP மற்றும் அடிப்படை உரிமைகளை 'அரசியலமைப்பின் மனசாட்சி' என்று அழைத்தார். அம்பேத்கர் DPSP-ஐ 'புதுமையான அம்சம்' என்று அழைத்தார்.",
    "DPSP along with Fundamental Rights contain the philosophy of the Constitution.",
    "DPSP அடிப்படை உரிமைகளுடன் சேர்ந்து அரசியலமைப்பின் தத்துவத்தைக் கொண்டுள்ளது.",
    ["TNPSC Group 1 2017 PYQ", "M. Laxmikanth - Indian Polity"],
    is_exact_pyq=True
))

# Q4 (Exact PYQ - Group 1 2015) - Answer B
q_data.append(make_q(
    "DPSP_PYQ_004", "Easy", "Direct MCQ",
    "Which Article of the Constitution of India declares that Directive Principles are non-justiciable in courts but fundamental in the governance of the country?",
    "இந்திய அரசியலமைப்பின் எந்தப் பிரிவு அரசு நெறிமுறைக் கோட்பாடுகள் நீதிமன்றத்தால் அமல்படுத்தப்பட முடியாதவை என்றாலும் நாட்டின் ஆட்சியில் அடிப்படைத் தன்மையானவை என அறிவிக்கிறது?",
    [
        ("Article 36", "பிரிவு 36"),
        ("Article 37", "பிரிவு 37"),
        ("Article 38", "பிரிவு 38"),
        ("Article 39", "பிரிவு 39")
    ],
    "B",
    "Article 37 explicitly states that Directive Principles are non-justiciable in any court, but they are fundamental in the governance of the country and it shall be the duty of the State to apply them in making laws.",
    "பிரிவு 37 நெறிமுறைகள் நீதிமன்றத்தால் அமல்படுத்தப்பட முடியாதவை என்றாலும், நாட்டின் ஆட்சியில் அடிப்படைத் தன்மையானவை எனத் தெளிவாகக் குறிப்பிடுகிறது.",
    {
        "A": ("Incorrect. Article 36 defines the term 'State' for Part IV.", "தவறு. பிரிவு 36 பகுதி IV-க்கான 'அரசு' வரையறையைக் அளிக்கிறது."),
        "B": ("Correct. Article 37 declares non-justiciability and fundamental nature in governance.", "சரி. பிரிவு 37 நீதிமன்ற அமலாக்கமின்மை மற்றும் ஆட்சியில் அடிப்படைத் தன்மையை அறிவிக்கிறது."),
        "C": ("Incorrect. Article 38 directs the State to secure a social order for the welfare of the people.", "தவறு. பிரிவு 38 மக்கள் நலனுக்கான சமூக அமைப்பை உறுதி செய்யப் பணிக்கிறது."),
        "D": ("Incorrect. Article 39 secures specific principles of policy.", "தவறு. பிரிவு 39 கொள்கையின் குறிப்பிட்ட நெறிமுறைகளைப் பாதுகாக்கிறது.")
    },
    "Article 36 = Definition of State. Article 37 = Non-justiciable but Fundamental in Governance.",
    "பிரிவு 36 = அரசு வரையறை. பிரிவு 37 = நீதிமன்ற அமலாக்கமின்மை மற்றும் ஆட்சியில் அடிப்படை.",
    "Sir Tej Bahadur Sapru Committee (1945) recommended dividing rights into justiciable (Part III) and non-justiciable (Part IV).",
    "சப்ரு குழு (1945) உரிமைகளை அமல்படுத்தக்கூடியவை (பகுதி III) மற்றும் அமல்படுத்த முடியாதவை (பகுதி IV) எனப் பிரிக்க பரிந்துரைத்தது.",
    ["TNPSC Group 1 2015 PYQ", "M. Laxmikanth - Indian Polity"],
    is_exact_pyq=True
))

# Q5 (Exact PYQ - Group 1 2021) - Answer A
q_data.append(make_q(
    "DPSP_PYQ_005", "Easy", "Direct MCQ",
    "Article 40 of the Constitution of India directs the State to take steps to organise which of the following?",
    "இந்திய அரசியலமைப்பின் பிரிவு 40 பின்வருவனவற்றில் எதனை அமைக்க அரசு நடவடிக்கை எடுக்க வேண்டும் எனப் பணிக்கிறது?",
    [
        ("Village Panchayats", "கிராம பஞ்சாயத்துகள்"),
        ("Co-operative Societies", "கூட்டுறவு சங்கங்கள்"),
        ("Municipal Corporations", "மாநகராட்சிகள்"),
        ("Cottage Industries", "குடிசைத் தொழில்கள்")
    ],
    "A",
    "Article 40 directs the State to organize Village Panchayats and endow them with such powers and authority as may be necessary to enable them to function as units of self-government.",
    "பிரிவு 40 கிராம பஞ்சாயத்துகளை அமைத்து அவை சுயராஜ்ய அலகுகளாகச் செயல்படத் தேவையான அதிகாரங்களை வழங்க அரசைப் பணிக்கிறது.",
    {
        "A": ("Correct. Article 40 is the Gandhian directive for Village Panchayats.", "சரி. பிரிவு 40 கிராம பஞ்சாயத்துகளுக்கான காந்திய நெறிமுறையாகும்."),
        "B": ("Incorrect. Co-operative Societies are under Article 43B.", "தவறு. கூட்டுறவு சங்கங்கள் பிரிவு 43B-ன் கீழ் உள்ளன."),
        "C": ("Incorrect. Municipalities are provided under Part IXA (74th Amendment).", "தவறு. நகராட்சிகள் பகுதி IXA-ன் கீழ் உள்ளன."),
        "D": ("Incorrect. Cottage Industries are under Article 43.", "தவறு. குடிசைத் தொழில்கள் பிரிவு 43-ன் கீழ் உள்ளன.")
    },
    "Article 40 = Village Panchayats. Article 43 = Cottage Industries. Article 43B = Co-operative Societies.",
    "பிரிவு 40 = கிராம பஞ்சாயத்துகள். பிரிவு 43 = குடிசைத் தொழில்கள். பிரிவு 43B = கூட்டுறவு சங்கங்கள்.",
    "The 73rd Constitutional Amendment Act 1992 operationalized Article 40 by adding Part IX.",
    "73-வது திருத்தச் சட்டம் 1992 பகுதி IX-ஐச் சேர்த்து பிரிவு 40-ஐ அமல்படுத்தியது.",
    ["TNPSC Group 1 2021 PYQ", "M. Laxmikanth - Indian Polity"],
    is_exact_pyq=True
))

# Q6 (Exact PYQ - Group 2 2018) -> Adjust options so Answer is D
q_data.append(make_q(
    "DPSP_PYQ_006", "Medium", "Direct MCQ",
    "Which Constitutional Amendment Act added Article 39A (Equal Justice and Free Legal Aid) to Part IV of the Constitution?",
    "அரசியலமைப்பின் பகுதி IV-ல் பிரிவு 39A-ஐ (சம நீதி மற்றும் இலவச சட்ட உதவி) சேர்த்த அரசியலமைப்பு திருத்தச் சட்டம் எது?",
    [
        ("24th Amendment Act 1971", "24-வது திருத்தச் சட்டம் 1971"),
        ("44th Amendment Act 1978", "44-வது திருத்தச் சட்டம் 1978"),
        ("86th Amendment Act 2002", "86-வது திருத்தச் சட்டம் 2002"),
        ("42nd Amendment Act 1976", "42-வது திருத்தச் சட்டம் 1976")
    ],
    "D",
    "The 42nd Constitutional Amendment Act 1976 added Article 39A to provide equal justice and free legal aid to the poor.",
    "42-வது அரசியலமைப்பு திருத்தச் சட்டம் 1976 ஏழைகளுக்கு சம நீதி மற்றும் இலவச சட்ட உதவி வழங்க பிரிவு 39A-ஐச் சேர்த்தது.",
    {
        "A": ("Incorrect. 24th Amendment 1971 affirmed Parliament's power to amend Fundamental Rights.", "தவறு. 24-வது திருத்தம் அடிப்படை உரிமைகளைத் திருத்தும் அதிகாரத்தை உறுதிப்படுத்தியது."),
        "B": ("Incorrect. 44th Amendment 1978 added Article 38(2).", "தவறு. 44-வது திருத்தம் 1978 பிரிவு 38(2)-ஐச் சேர்த்தது."),
        "C": ("Incorrect. 86th Amendment 2002 substituted Article 45.", "தவறு. 86-வது திருத்தம் 2002 பிரிவு 45-ஐ மாற்றியமைத்தது."),
        "D": ("Correct. 42nd Amendment 1976 added Article 39A, 43A, and 48A.", "சரி. 42-வது திருத்தம் 1976 பிரிவு 39A, 43A மற்றும் 48A-ஐச் சேர்த்தது.")
    },
    "42nd Amendment 1976 added 4 DPSP provisions: 39(f), 39A, 43A, 48A.",
    "42-வது திருத்தம் 1976 4 DPSP பிரிவுகளைச் சேர்த்தது: 39(f), 39A, 43A, 48A.",
    "Legal Services Authorities Act was passed in 1987 to give statutory effect to Article 39A.",
    "பிரிவு 39A-க்கு சட்டப்பூர்வ அந்தஸ்து வழங்க 1987-ல் சட்டப் பணிகள் ஆணைக்குழுச் சட்டம் நிறைவேற்றப்பட்டது.",
    ["TNPSC Group 2 2018 PYQ", "M. Laxmikanth - Indian Polity"],
    is_exact_pyq=True
))

# Q7 (Exact PYQ - Group 1 2019) -> Answer C
q_data.append(make_q(
    "DPSP_PYQ_007", "Easy", "Direct MCQ",
    "Separation of Judiciary from Executive is mentioned in which part of the Constitution of India under Article 50?",
    "பிரிவு 50-ன் கீழ் நிர்வாகத்திலிருந்து நீதித்துறையைப் பிரித்தல் என்பது இந்திய அரசியலமைப்பின் எந்தப் பகுதியில் குறிப்பிடப்பட்டுள்ளது?",
    [
        ("Preamble", "முகவுரை"),
        ("Fundamental Rights", "அடிப்படை உரிமைகள்"),
        ("Directive Principles of State Policy", "அரசு நெறிமுறைப்படுத்தும் கோட்பாடுகள்"),
        ("Seventh Schedule", "ஏழாவது அட்டவணை")
    ],
    "C",
    "Article 50 under Directive Principles of State Policy (Part IV) directs the State to take steps to separate the judiciary from the executive in the public services of the State.",
    "அரசு நெறிமுறைப்படுத்தும் கோட்பாடுகளின் (பகுதி IV) பிரிவு 50 மாநிலத்தின் பொதுப்பணிகளில் நிர்வாகத்திலிருந்து நீதித்துறையைப் பிரிக்க நடவடிக்கை எடுக்கப் பணிக்கிறது.",
    {
        "A": ("Incorrect. Preamble sets out objectives of Justice, Liberty, Equality, Fraternity.", "தவறு. முகவுரை நீதி, சுதந்திரம், சமத்துவம் ஆகியவற்றைக் குறிப்பிடுகிறது."),
        "B": ("Incorrect. Fundamental Rights are under Part III (Articles 12-35).", "தவறு. அடிப்படை உரிமைகள் பகுதி III-ன் கீழ் உள்ளன."),
        "C": ("Correct. Article 50 is a Directive Principle in Part IV.", "சரி. பிரிவு 50 என்பது பகுதி IV-ல் உள்ள அரசு நெறிமுறையாகும்."),
        "D": ("Incorrect. Seventh Schedule deals with Union, State, and Concurrent legislative lists.", "தவறு. 7-வது அட்டவணை அதிகாரப் பகிர்வுப் பட்டியல்களைக் கையாள்கிறது.")
    },
    "Article 50 = Separation of Judiciary from Executive. Article 51 = International Peace.",
    "பிரிவு 50 = நிர்வாகத்திலிருந்து நீதித்துறை பிரிப்பு. பிரிவு 51 = சர்வதேச அமைதி.",
    "Code of Criminal Procedure 1973 (CrPC) separated judicial functions from executive magistrates.",
    "குற்றவியல் நடைமுறைச் சட்டம் 1973 (CrPC) நிர்வாக நடுவர்களிடமிருந்து நீதித்துறை பணிகளைப் பிரித்தது.",
    ["TNPSC Group 1 2019 PYQ", "M. Laxmikanth - Indian Polity"],
    is_exact_pyq=True
))

# Q8 (Exact PYQ - Group 1 2022) -> Adjust options so Answer is D
q_data.append(make_q(
    "DPSP_PYQ_008", "Easy", "Direct MCQ",
    "Article 44 of the Constitution of India directs the State to endeavour to secure for citizens which of the following?",
    "இந்திய அரசியலமைப்பின் பிரிவு 44 குடிமக்களுக்கு பின்வருவனவற்றில் எதனை உறுதி செய்ய அரசு முயல வேண்டும் எனப் பணிக்கிறது?",
    [
        ("Right to Work and Education", "வேலை மற்றும் கல்வி உரிமை"),
        ("Free and Compulsory Primary Education", "இலவச கட்டாய ஆரம்பக் கல்வி"),
        ("Prohibition of Intoxicating Drinks", "மதுவிலக்கு"),
        ("Uniform Civil Code", "பொது சிவில் சட்டம்")
    ],
    "D",
    "Article 44 directs the State to endeavour to secure for citizens a Uniform Civil Code throughout the territory of India.",
    "பிரிவு 44 இந்தியா முழுவதிலும் உள்ள குடிமக்களுக்கு ஒரே மாதிரியான சிவில் சட்டத்தை உறுதி செய்ய அரசு முயல வேண்டும் எனப் பணிக்கிறது.",
    {
        "A": ("Incorrect. Right to work and education is under Article 41.", "தவறு. வேலை மற்றும் கல்வி உரிமை பிரிவு 41-ன் கீழ் உள்ளது."),
        "B": ("Incorrect. Early childhood care is under Article 45.", "தவறு. ஆரம்பகால குழந்தை பராமரிப்பு பிரிவு 45-ன் கீழ் உள்ளது."),
        "C": ("Incorrect. Prohibition of liquor is under Article 47.", "தவறு. மதுவிலக்கு பிரிவு 47-ன் கீழ் உள்ளது."),
        "D": ("Correct. Article 44 specifically deals with Uniform Civil Code.", "சரி. பிரிவு 44 பொது சிவில் சட்டத்தைப் பிரத்யேகமாகக் கையாள்கிறது.")
    },
    "Article 44 = Uniform Civil Code. Goa is the only State in India having a Uniform Civil Code.",
    "பிரிவு 44 = பொது சிவில் சட்டம். கோவா இந்தியாவில் பொது சிவில் சட்டம் உள்ள ஒரே மாநிலமாகும்.",
    "Shah Bano case (1985) and Sarla Mudgal case (1995) urged the implementation of Article 44.",
    "ஷா பானோ (1985) மற்றும் சர்லா முத்கல் (1995) வழக்குகள் பிரிவு 44-ஐ அமல்படுத்த வலியுறுத்தின.",
    ["TNPSC Group 1 2022 PYQ", "M. Laxmikanth - Indian Polity"],
    is_exact_pyq=True
))

# Q9 (Exact PYQ - Group 2 2019) -> Answer B
q_data.append(make_q(
    "DPSP_PYQ_009", "Medium", "Direct MCQ",
    "Which Article of Part IV instructs the State to protect and improve the environment and to safeguard forests and wildlife?",
    "சுற்றுச்சூழலைப் பாதுகாக்கவும் மேம்படுத்தவும் வனங்கள் மற்றும் வனவிலங்குகளைப் பாதுகாக்கவும் அரசுக்கு அறிவுறுத்தும் பகுதி IV-ன் பிரிவு எது?",
    [
        ("Article 48", "பிரிவு 48"),
        ("Article 48A", "பிரிவு 48A"),
        ("Article 49", "பிரிவு 49"),
        ("Article 50", "பிரிவு 50")
    ],
    "B",
    "Article 48A (inserted by 42nd Amendment Act 1976) explicitly directs the State to protect and improve the environment and to safeguard the forests and wildlife of the country.",
    "பிரிவு 48A (42-வது திருத்தம் 1976-ல் சேர்க்கப்பட்டது) சுற்றுச்சூழலைப் பாதுகாக்கவும் மேம்படுத்தவும் காடுகள் மற்றும் வனவிலங்குகளைப் பாதுகாக்கவும் அரசைப் பணிக்கிறது.",
    {
        "A": ("Incorrect. Article 48 deals with agriculture and animal husbandry.", "தவறு. பிரிவு 48 வேளாண்மை மற்றும் கால்நடை வளர்ப்பைக் கையாள்கிறது."),
        "B": ("Correct. Article 48A explicitly deals with environment, forests, and wildlife.", "சரி. பிரிவு 48A சுற்றுச்சூழல் மற்றும் வனவிலங்கு பாதுகாப்பைக் கையாள்கிறது."),
        "C": ("Incorrect. Article 49 deals with protection of monuments.", "தவறு. பிரிவு 49 வரலாற்றுச் சின்னங்களைப் பாதுகாப்பதைக் கையாள்கிறது."),
        "D": ("Incorrect. Article 50 deals with separation of judiciary from executive.", "தவறு. பிரிவு 50 நிர்வாகத்திலிருந்து நீதித்துறையைப் பிரிப்பதைக் கையாள்கிறது.")
    },
    "Article 48 = Agriculture & Animal Husbandry. Article 48A = Protection of Environment & Wildlife.",
    "பிரிவு 48 = வேளாண்மை & கால்நடை பராமரிப்பு. பிரிவு 48A = சுற்றுச்சூழல் & வனவிலங்கு பாதுகாப்பு.",
    "Wildlife Protection Act 1972 and Forest Conservation Act 1980 fulfill Article 48A.",
    "வனவிலங்கு பாதுகாப்புச் சட்டம் 1972 மற்றும் வனப் பாதுகாப்புச் சட்டம் 1980 ஆகியவை பிரிவு 48A-ஐ நிறைவேற்றுகின்றன.",
    ["TNPSC Group 2 2019 PYQ", "M. Laxmikanth - Indian Polity"],
    is_exact_pyq=True
))

# Q10 (Exact PYQ - Group 1 2014) -> Answer C
q_data.append(make_q(
    "DPSP_PYQ_010", "Medium", "Direct MCQ",
    "Which Constitutional Amendment Act substituted Article 45 to provide early childhood care and education for children below the age of six years?",
    "ஆறு வயதிற்குட்பட்ட குழந்தைகளுக்கு ஆரம்பகால பராமரிப்பு மற்றும் கல்வி வழங்க பிரிவு 45-ஐ மாற்றியமைத்த அரசியலமைப்பு திருத்தச் சட்டம் எது?",
    [
        ("42nd Amendment Act 1976", "42-வது திருத்தச் சட்டம் 1976"),
        ("44th Amendment Act 1978", "44-வது திருத்தச் சட்டம் 1978"),
        ("86th Amendment Act 2002", "86-வது திருத்தச் சட்டம் 2002"),
        ("97th Amendment Act 2011", "97-வது திருத்தச் சட்டம் 2011")
    ],
    "C",
    "The 86th Constitutional Amendment Act 2002 substituted Article 45 to direct early childhood care and education for children below six years, while moving education for 6-14 years to Fundamental Right under Article 21A.",
    "86-வது அரசியலமைப்பு திருத்தச் சட்டம் 2002 பிரிவு 45-ஐ 6 வயதிற்குட்பட்ட குழந்தைகளுக்கான பராமரிப்பாக மாற்றியது, 6-14 வயதுக் கல்வியை பிரிவு 21A-க்கு மாற்றியது.",
    {
        "A": ("Incorrect. 42nd Amendment added Art 39A, 43A, 48A.", "தவறு. 42-வது திருத்தம் பிரிவு 39A, 43A, 48A-ஐச் சேர்த்தது."),
        "B": ("Incorrect. 44th Amendment added Art 38(2).", "தவறு. 44-வது திருத்தம் பிரிவு 38(2)-ஐச் சேர்த்தது."),
        "C": ("Correct. 86th Amendment 2002 substituted Article 45.", "சரி. 86-வது திருத்தம் 2002 பிரிவு 45-ஐ மாற்றியமைத்தது."),
        "D": ("Incorrect. 97th Amendment added Art 43B.", "தவறு. 97-வது திருத்தம் பிரிவு 43B-ஐச் சேர்த்தது.")
    },
    "Present Article 45 = Below 6 years (DPSP). Article 21A = 6 to 14 years (Fundamental Right).",
    "தற்போதைய பிரிவு 45 = 6 வயதிற்குட்பட்டவை (DPSP). பிரிவு 21A = 6 முதல் 14 வயது வரை (அடிப்படை உரிமை).",
    "RTE Act 2009 was enacted to implement Article 21A.",
    "இலவச கட்டாயக் கல்வி உரிமைச் சட்டம் 2009 பிரிவு 21A-ஐ அமல்படுத்த இயற்றப்பட்டது.",
    ["TNPSC Group 1 2014 PYQ", "M. Laxmikanth - Indian Polity"],
    is_exact_pyq=True
))

# Q11 (PYQ Pattern) -> Answer B
q_data.append(make_q(
    "DPSP_PYQ_011", "Easy", "Direct MCQ",
    "The Directive Principles of State Policy in Part IV of the Constitution aim at establishing which of the following ideal concepts?",
    "அரசியலமைப்பின் பகுதி IV-ல் உள்ள அரசு நெறிமுறைப்படுத்தும் கோட்பாடுகள் பின்வரும் எந்த உன்னதக் கருத்தை நிறுவுவதை நோக்கமாகக் கொண்டுள்ளன?",
    [
        ("Capitalist State", "முதலாளித்துவ அரசு"),
        ("Welfare State and Social-Economic Democracy", "நல அரசு மற்றும் சமூக-பொருளாதார ஜனநாயகம்"),
        ("Theocratic State", "மதசார்புடைய அரசு"),
        ("Totalitarian Police State", "சர்வாதிகாரக் காவல் அரசு")
    ],
    "B",
    "Directive Principles aim at establishing a Welfare State and achieving Social and Economic Democracy in India.",
    "அரசு நெறிமுறைப்படுத்தும் கோட்பாடுகள் இந்தியாவில் நல அரசை நிறுவுவதையும் சமூக மற்றும் பொருளாதார ஜனநாயகத்தை அடைவதையும் நோக்கமாகக் கொண்டுள்ளன.",
    {
        "A": ("Incorrect. DPSP opposes capitalist exploitation.", "தவறு. DPSP முதலாளித்துவ சுரண்டலை எதிர்க்கிறது."),
        "B": ("Correct. DPSP aims to build a Welfare State and Social-Economic Democracy.", "சரி. DPSP நல அரசு மற்றும் சமூக-பொருளாதார ஜனநாயகத்தை அமைப்பதை நோக்கமாகக் கொண்டுள்ளது."),
        "C": ("Incorrect. India is a secular state.", "தவறு. இந்தியா ஒரு மதச்சார்பற்ற நாடாகும்."),
        "D": ("Incorrect. Police state is opposite of welfare state.", "தவறு. காவல் அரசு நல அரசுக்கு எதிரானது.")
    },
    "Fundamental Rights establish Political Democracy; DPSP establishes Social and Economic Democracy.",
    "அடிப்படை உரிமைகள் அரசியல் ஜனநாயகத்தை நிறுவுகின்றன; DPSP சமூக மற்றும் பொருளாதார ஜனநாயகத்தை நிறுவுகிறது.",
    "Preamble and DPSP together reflect the vision of a Welfare State.",
    "முகவுரை மற்றும் DPSP இரண்டும் சேர்ந்து நல அரசின் பார்வையை வெளிப்படுத்துகின்றன.",
    ["TNPSC Group 1 PYQ Pattern", "M. Laxmikanth - Indian Polity"]
))

# Q12 (PYQ Pattern) -> Adjust options so Answer is C
q_data.append(make_q(
    "DPSP_PYQ_012", "Medium", "Direct MCQ",
    "According to Dr. B.R. Ambedkar, DPSP in the Constitution of India resemble the 'Instruments of Instructions' issued to the Governor-General under which colonial Act?",
    "டாக்டர் பி.ஆர். அம்பேத்கரின் கூற்றுப்படி, DPSP எந்தக் காலனித்துவ சட்டத்தின் கீழ் ஆளுநர் ஜெனரலுக்கு வழங்கப்பட்ட 'அறிவுறுத்தல் கருவிகளை' ஒத்திருக்கிறது?",
    [
        ("Indian Councils Act 1892", "இந்தியக் கவுன்சில்கள் சட்டம் 1892"),
        ("Government of India Act 1919", "இந்திய அரசுச் சட்டம் 1919"),
        ("Government of India Act 1935", "இந்திய அரசுச் சட்டம் 1935"),
        ("Indian Independence Act 1947", "இந்திய சுதந்திரச் சட்டம் 1947")
    ],
    "C",
    "Dr. B.R. Ambedkar stated in the Constituent Assembly that Directive Principles are like the 'Instruments of Instructions' issued to the Governor-General and Governors under the Government of India Act 1935.",
    "டாக்டர் பி.ஆர். அம்பேத்கர் DPSP 1935-ம் ஆண்டு இந்திய அரசுச் சட்டத்தின் கீழ் ஆளுநர் ஜெனரலுக்கு வழங்கப்பட்ட 'அறிவுறுத்தல் கருவிகள்' போன்றவை எனக் குறிப்பிட்டார்.",
    {
        "A": ("Incorrect. 1892 Act introduced indirect elections.", "தவறு. 1892 சட்டம் மறைமுகத் தேர்தலை அறிமுகப்படுத்தியது."),
        "B": ("Incorrect. 1919 Act introduced Dyarchy in Provinces.", "தவறு. 1919 சட்டம் மாகாணங்களில் இரட்டை ஆட்சியை அறிமுகப்படுத்தியது."),
        "C": ("Correct. DPSP resembles Instruments of Instructions of GOI Act 1935.", "சரி. DPSP 1935 சட்டத்தின் அறிவுறுத்தல் கருவிகளை ஒத்துள்ளது."),
        "D": ("Incorrect. 1947 Act granted independence.", "தவறு. 1947 சட்டம் சுதந்திரம் வழங்கியது.")
    },
    "The only difference is that DPSP are instructions addressed to the Legislature and Executive of free India.",
    "ஒரே வித்தியாசம் என்னவென்றால், DPSP சுதந்திர இந்தியாவின் சட்டமன்றம் மற்றும் நிர்வாகத்திற்கான அறிவுறுத்தல்களாகும்.",
    "GOI Act 1935 was the major structural source of the Indian Constitution.",
    "1935 அரசுச் சட்டம் இந்திய அரசியலமைப்பின் முக்கிய அமைப்பியல் ஆதாரமாகும்.",
    ["TNPSC Group 1 PYQ Pattern", "M. Laxmikanth - Indian Polity"]
))

# Q13 (PYQ Pattern) -> Answer A
q_data.append(make_q(
    "DPSP_PYQ_013", "Hard", "Direct MCQ",
    "Which landmark Supreme Court judgment first established that Fundamental Rights take precedence over Directive Principles of State Policy in case of conflict?",
    "முரண்பாடு ஏற்படும் போது அரசு நெறிமுறைக் கோட்பாடுகளை விட அடிப்படை உரிமைகளே முதன்மை பெறுகின்றன என்று முதலில் தீர்ப்பளித்த உச்சநீதிமன்ற வழக்கு எது?",
    [
        ("State of Madras v. Champakam Dorairajan (1951)", "மதராஸ் மாநிலம் எதிராக செம்பகம் துரைராஜன் (1951)"),
        ("Golaknath v. State of Punjab (1967)", "கோலக்நாத் எதிராக பஞ்சாப் மாநிலம் (1967)"),
        ("Kesavananda Bharati v. State of Kerala (1973)", "கேசவாநந்த பாரதி எதிராக കേരള மாநிலம் (1973)"),
        ("Minerva Mills v. Union of India (1980)", "மினர்வா மில்ஸ் எதிராக இந்திய யூனியன் (1980)")
    ],
    "A",
    "In State of Madras v. Champakam Dorairajan (1951), the Supreme Court ruled that in case of any conflict between Fundamental Rights and Directive Principles, Fundamental Rights would prevail, declaring DPSP subsidiary to Part III.",
    "செம்பகம் துரைராஜன் (1951) வழக்கில், அடிப்படை உரிமைகள் மற்றும் நெறிமுறைக் கோட்பாடுகளுக்கு இடையே முரண்பாடு ஏற்பட்டால் அடிப்படை உரிமைகளே முதன்மை பெறும் என உச்சநீதிமன்றம் தீர்ப்பளித்தது.",
    {
        "A": ("Correct. Champakam Dorairajan (1951) first declared FR primacy over DPSP.", "சரி. செம்பகம் துரைராஜன் (1951) வழக்கு DPSP-ஐ விட அடிப்படை உரிமைகள் முதன்மை வாய்ந்தவை என முதலில் தீர்ப்பளித்தது."),
        "B": ("Incorrect. Golaknath (1967) declared FR transcendental.", "தவறு. கோலக்நாத் (1967) அடிப்படை உரிமைகள் மாற்ற முடியாதவை எனக் கூறியது."),
        "C": ("Incorrect. Kesavananda Bharati (1973) introduced Basic Structure doctrine.", "தவறு. கேசவாநந்த பாரதி (1973) அடிப்படை அமைப்புக் கோட்பாட்டை அறிமுகப்படுத்தியது."),
        "D": ("Incorrect. Minerva Mills (1980) established balance between FR and DPSP as Basic Structure.", "தவறு. மினர்வா மில்ஸ் (1980) உரிமைகள் மற்றும் நெறிமுறைகளுக்கு இடையே சமநிலையை நிறுவியது.")
    },
    "1st Amendment Act 1951 inserted Article 15(4) to overcome the Champakam Dorairajan ruling.",
    "செம்பகம் துரைராஜன் தீர்ப்பை முறியடிக்க 1-வது திருத்தச் சட்டம் 1951 மூலம் பிரிவு 15(4) சேர்க்கப்பட்டது.",
    "Presently, Article 31C protects Article 39(b) & (c) over Articles 14 & 19.",
    "தற்போது, பிரிவு 31C பிரிவு 39(b) & (c)-ஐ பிரிவுகள் 14 & 19-லிருந்து பாதுகாக்கிறது.",
    ["TNPSC Group 1 PYQ Pattern", "M. Laxmikanth - Indian Polity"]
))

# Q14 (PYQ Pattern) -> Adjust options so Answer is D
q_data.append(make_q(
    "DPSP_PYQ_014", "Medium", "Direct MCQ",
    "Which Article of Part IV directs the State to minimise inequalities in income, status, facilities, and opportunities, inserted by the 44th Constitutional Amendment Act 1978?",
    "வருமானம், அந்தஸ்து, வசதிகள் மற்றும் வாய்ப்புகளில் உள்ள ஏற்றத்தாழ்வுகளைக் குறைக்க அரசைப் பணிக்கும் 44-வது திருத்தச் சட்டம் 1978 மூலம் சேர்க்கப்பட்ட பிரிவு எது?",
    [
        ("Article 38(1)", "பிரிவு 38(1)"),
        ("Article 39(a)", "பிரிவு 39(a)"),
        ("Article 39(b)", "பிரிவு 39(b)"),
        ("Article 38(2)", "பிரிவு 38(2)")
    ],
    "D",
    "Article 38(2) was inserted by the 44th Constitutional Amendment Act 1978 directing the State to strive to minimise inequalities in income, status, facilities and opportunities.",
    "44-வது திருத்தச் சட்டம் 1978 மூலம் பிரிவு 38(2) சேர்க்கப்பட்டு வருமானம் மற்றும் அந்தஸ்தில் உள்ள ஏற்றத்தாழ்வுகளைக் குறைக்க அரசைப் பணிக்கிறது.",
    {
        "A": ("Incorrect. Article 38(1) was in the original 1950 Constitution.", "தவறு. பிரிவு 38(1) 1950 மூல அரசியலமைப்பிலேயே இருந்தது."),
        "B": ("Incorrect. Article 39(a) deals with right to adequate means of livelihood.", "தவறு. பிரிவு 39(a) போதுமான வாழ்வாதார உரிமையைக் கையாள்கிறது."),
        "C": ("Incorrect. Article 39(b) deals with distribution of material resources.", "தவறு. பிரிவு 39(b) பருப்பொருள் வளங்களின் விநியோகத்தைக் கையாள்கிறது."),
        "D": ("Correct. Article 38(2) was added by 44th Amendment Act 1978.", "சரி. பிரிவு 38(2) 44-வது திருத்தச் சட்டம் 1978 மூலம் சேர்க்கப்பட்டது.")
    },
    "44th Amendment 1978 added Article 38(2) to Part IV.",
    "44-வது திருத்தம் 1978 பகுதி IV-ல் பிரிவு 38(2)-ஐச் சேர்த்தது.",
    "Article 38(2) applies to both individuals and groups of people.",
    "பிரிவு 38(2) தனிநபர்கள் மற்றும் மக்கள் குழுக்கள் ஆகிய இருவருக்கும் பொருந்தும்.",
    ["TNPSC Group 1 PYQ Pattern", "M. Laxmikanth - Indian Polity"]
))

# Q15 (PYQ Pattern) -> Answer C
q_data.append(make_q(
    "DPSP_PYQ_015", "Hard", "Direct MCQ",
    "Which Constitutional Amendment Act introduced Article 31C to protect laws implementing Article 39(b) and Article 39(c) directives from challenge under Articles 14, 19, and 31?",
    "பிரிவு 39(b) மற்றும் 39(c) நெறிமுறைகளை அமல்படுத்தும் சட்டங்களை பிரிவுகள் 14, 19 மற்றும் 31-லிருந்து பாதுகாக்க பிரிவு 31C-ஐ அறிமுகப்படுத்திய அரசியலமைப்பு திருத்தச் சட்டம் எது?",
    [
        ("1st Amendment Act 1951", "1-வது திருத்தச் சட்டம் 1951"),
        ("24th Amendment Act 1971", "24-வது திருத்தச் சட்டம் 1971"),
        ("25th Amendment Act 1971", "25-வது திருத்தச் சட்டம் 1971"),
        ("42nd Amendment Act 1976", "42-வது திருத்தச் சட்டம் 1976")
    ],
    "C",
    "The 25th Constitutional Amendment Act 1971 introduced Article 31C, giving immunity to laws implementing Article 39(b) and 39(c) directives against Articles 14, 19, and 31.",
    "25-வது அரசியலமைப்பு திருத்தச் சட்டம் 1971 பிரிவு 31C-ஐ அறிமுகப்படுத்தி, பிரிவு 39(b) மற்றும் 39(c)-ஐ அமல்படுத்தும் சட்டங்களுக்கு பாதுகாப்பு அளித்தது.",
    {
        "A": ("Incorrect. 1st Amendment 1951 added Ninth Schedule and Articles 31A & 31B.", "தவறு. 1-வது திருத்தம் 1951 9-வது அட்டவணையைச் சேர்த்தது."),
        "B": ("Incorrect. 24th Amendment 1971 amended Article 13 and 368.", "தவறு. 24-வது திருத்தம் 1971 பிரிவு 13 மற்றும் 368-ஐத் திருத்தியது."),
        "C": ("Correct. 25th Amendment 1971 inserted Article 31C.", "சரி. 25-வது திருத்தம் 1971 பிரிவு 31C-ஐச் சேர்த்தது."),
        "D": ("Incorrect. 42nd Amendment 1976 attempted to extend Art 31C to all DPSP.", "தவறு. 42-வது திருத்தம் 1976 பிரிவு 31C-ஐ விரிவாக்க முயன்றது.")
    },
    "Kesavananda Bharati (1973) upheld the 1st part of Article 31C protecting Art 39(b) & (c).",
    "கேசவாநந்த பாரதி (1973) பிரிவு 39(b) & (c)-ஐப் பாதுகாக்கும் பிரிவு 31C-ன் 1-வது பகுதியை உறுதி செய்தது.",
    "Minerva Mills (1980) struck down 42nd Amendment extension to all DPSP.",
    "மினர்வா மில்ஸ் (1980) அனைத்து DPSP-க்கும் பிரிவு 31C விரிவாக்கத்தை ரத்து செய்தது.",
    ["TNPSC Group 1 PYQ Pattern", "M. Laxmikanth - Indian Polity"]
))

# Q16 (PYQ Pattern) -> Answer A
q_data.append(make_q(
    "DPSP_PYQ_016", "Medium", "Match the Following",
    "Match the Articles of Part IV with their respective subject matters:\n\n1. Article 39A – a. Free Legal Aid\n2. Article 40 – b. Village Panchayats\n3. Article 43A – c. Workers' Participation in Management\n4. Article 48A – d. Environment Protection",
    "பகுதி IV-ன் பிரிவுகளை அவற்றின் பொருளுடன் பொருத்துக:\n\n1. பிரிவு 39A – a. இலவச சட்ட உதவி\n2. பிரிவு 40 – b. கிராம பஞ்சாயத்துகள்\n3. பிரிவு 43A – c. மேலாண்மையில் தொழிலாளர் பங்கேற்பு\n4. பிரிவு 48A – d. சுற்றுச்சூழல் பாதுகாப்பு",
    [
        ("1-a, 2-b, 3-c, 4-d", "1-a, 2-b, 3-c, 4-d"),
        ("1-b, 2-a, 3-d, 4-c", "1-b, 2-a, 3-d, 4-c"),
        ("1-c, 2-d, 3-a, 4-b", "1-c, 2-d, 3-a, 4-b"),
        ("1-d, 2-c, 3-b, 4-a", "1-d, 2-c, 3-b, 4-a")
    ],
    "A",
    "Correct Matching: Article 39A -> Free Legal Aid; Article 40 -> Village Panchayats; Article 43A -> Workers' Participation in Management; Article 48A -> Environment Protection.",
    "சரியான பொருத்தம்: பிரிவு 39A -> இலவச சட்ட உதவி; பிரிவு 40 -> கிராம பஞ்சாயத்துகள்; பிரிவு 43A -> மேலாண்மையில் தொழிலாளர் பங்கேற்பு; பிரிவு 48A -> சுற்றுச்சூழல் பாதுகாப்பு.",
    {
        "A": ("Correct. 1-a, 2-b, 3-c, 4-d matches all 4 DPSP articles accurately.", "சரி. 1-a, 2-b, 3-c, 4-d அனைத்து பிரிவுகளையும் துல்லியமாகப் பொருத்துகிறது."),
        "B": ("Incorrect.", "தவறு."),
        "C": ("Incorrect.", "தவறு."),
        "D": ("Incorrect.", "தவறு.")
    },
    "Articles 39A, 43A, 48A were all added by the 42nd Amendment Act 1976.",
    "பிரிவுகள் 39A, 43A, 48A அனைத்தும் 42-வது திருத்தச் சட்டம் 1976 மூலம் சேர்க்கப்பட்டவை.",
    "Article 40 was in the original 1950 Constitution.",
    "பிரிவு 40 1950 மூல அரசியலமைப்பிலேயே இருந்தது.",
    ["TNPSC Group 1 PYQ Pattern", "M. Laxmikanth - Indian Polity"]
))

# Q17 (PYQ Pattern) -> Answer D
q_data.append(make_q(
    "DPSP_PYQ_017", "Hard", "Direct MCQ",
    "Which landmark Supreme Court judgment declared that the harmony and balance between Part III (Fundamental Rights) and Part IV (DPSP) is an essential feature of the Basic Structure of the Constitution?",
    "பகுதி III (அடிப்படை உரிமைகள்) மற்றும் பகுதி IV (DPSP) இடையேயான இணக்கமும் சமநிலையும் அரசியலமைப்பின் அடிப்படை அமைப்பின் முக்கிய அம்சம் எனத் தீர்ப்பளித்த வழக்கு எது?",
    [
        ("Champakam Dorairajan v. State of Madras (1951)", "செம்பகம் துரைராஜன் வழக்கு (1951)"),
        ("Golaknath v. State of Punjab (1967)", "கோலக்நாத் வழக்கு (1967)"),
        ("Kesavananda Bharati v. State of Kerala (1973)", "கேசவாநந்த பாரதி வழக்கு (1973)"),
        ("Minerva Mills v. Union of India (1980)", "மினர்வா மில்ஸ் எதிராக இந்திய யூனியன் (1980)")
    ],
    "D",
    "In Minerva Mills v. Union of India (1980), Chief Justice Y.V. Chandrachud ruled that harmony and balance between Part III and Part IV is part of the Basic Structure.",
    "மினர்வா மில்ஸ் (1980) வழக்கில், பகுதி III மற்றும் பகுதி IV இடையேயான சமநிலை அடிப்படை அமைப்பின் பகுதி என உச்சநீதிமன்றம் தீர்ப்பளித்தது.",
    {
        "A": ("Incorrect. Champakam Dorairajan (1951) declared DPSP subordinate.", "தவறு. செம்பகம் துரைராஜன் வழக்கு நெறிமுறைகளைக் கீழ்ப்படுத்தியது."),
        "B": ("Incorrect. Golaknath (1967) restricted Parliament from amending Part III.", "தவறு. கோலக்நாத் வழக்கு நாடாளுமன்ற அதிகாரத்தைக் கட்டுப்படுத்தியது."),
        "C": ("Incorrect. Kesavananda Bharati (1973) introduced Basic Structure doctrine.", "தவறு. கேசவாநந்த பாரதி வழக்கு அடிப்படை அமைப்புக் கோட்பாட்டை அறிமுகப்படுத்தியது."),
        "D": ("Correct. Minerva Mills (1980) declared FR-DPSP harmony as Basic Structure.", "சரி. மினர்வா மில்ஸ் (1980) உரிமைகள் மற்றும் நெறிமுறைகளின் சமநிலையை அடிப்படை அமைப்பாக அறிவித்தது.")
    },
    "Minerva Mills case (1980): 'Part III and Part IV are like two wheels of a chariot.'",
    "மினர்வா மில்ஸ் வழக்கு (1980): 'பகுதி III மற்றும் பகுதி IV ஆகியவை ஒரு தேரின் இரு சக்கரங்கள் போன்றவை.'",
    "Section 4 of 42nd Amendment was struck down in this case.",
    "இந்த வழக்கில் 42-வது திருத்தத்தின் பிரிவு 4 ரத்து செய்யப்பட்டது.",
    ["TNPSC Group 1 PYQ Pattern", "M. Laxmikanth - Indian Polity"]
))

# Q18 (PYQ Pattern) -> Adjust options so Answer is A
q_data.append(make_q(
    "DPSP_PYQ_018", "Easy", "Direct MCQ",
    "Which Article of Part IV directs the State to make provision for securing just and humane conditions of work and for maternity relief?",
    "நியாயமான மற்றும் மனிதத்தன்மையான பணிச்சூழலையும் மகப்பேறு உதவியையும் உறுதி செய்ய அரசு வழிவகை செய்ய வேண்டும் எனப் பணிக்கும் பகுதி IV-ன் பிரிவு எது?",
    [
        ("Article 42", "பிரிவு 42"),
        ("Article 41", "பிரிவு 41"),
        ("Article 43", "பிரிவு 43"),
        ("Article 43A", "பிரிவு 43A")
    ],
    "A",
    "Article 42 directs the State to make provision for securing just and humane conditions of work and for maternity relief.",
    "பிரிவு 42 நியாயமான பணிச்சூழலையும் மகப்பேறு உதவியையும் உறுதி செய்ய அரசைப் பணிக்கிறது.",
    {
        "A": ("Correct. Article 42 specifically covers maternity relief and humane conditions of work.", "சரி. பிரிவு 42 மகப்பேறு உதவியைக் கையாள்கிறது."),
        "B": ("Incorrect. Article 41 deals with right to work and public assistance.", "தவறு. பிரிவு 41 வேலை உரிமையைக் கையாள்கிறது."),
        "C": ("Incorrect. Article 43 deals with living wage and cottage industries.", "தவறு. பிரிவு 43 வாழ்வாதார ஊதியத்தைக் கையாள்கிறது."),
        "D": ("Incorrect. Article 43A deals with workers' participation in management.", "தவறு. பிரிவு 43A மேலாண்மையில் தொழிலாளர் பங்கேற்பைக் கையாள்கிறது.")
    },
    "Maternity Benefit Act 1961 was enacted to implement Article 42.",
    "பிரிவு 42-ஐ அமல்படுத்த 1961 மகப்பேறு நலச் சட்டம் இயற்றப்பட்டது.",
    "Article 42 is classified under Socialistic Principles.",
    "பிரிவு 42 சோசலிசக் கோட்பாடுகளின் கீழ் வகைப்படுத்தப்பட்டுள்ளது.",
    ["TNPSC Group 1 PYQ Pattern", "M. Laxmikanth - Indian Polity"]
))

# Q19 (PYQ Pattern) -> Answer D
q_data.append(make_q(
    "DPSP_PYQ_019", "Medium", "Direct MCQ",
    "Article 43B was added to Part IV of the Constitution by which Constitutional Amendment Act to promote autonomous functioning of Co-operative Societies?",
    "கூட்டுறவு சங்கங்களின் தன்னாட்சி செயல்பாட்டை ஊக்குவிக்க எந்த அரசியலமைப்பு திருத்தச் சட்டம் மூலம் பிரிவு 43B பகுதி IV-ல் சேர்க்கப்பட்டது?",
    [
        ("42nd Amendment Act 1976", "42-வது திருத்தச் சட்டம் 1976"),
        ("44th Amendment Act 1978", "44-வது திருத்தச் சட்டம் 1978"),
        ("86th Amendment Act 2002", "86-வது திருத்தச் சட்டம் 2002"),
        ("97th Amendment Act 2011", "97-வது திருத்தச் சட்டம் 2011")
    ],
    "D",
    "The 97th Constitutional Amendment Act 2011 added Article 43B in Part IV directing the State to promote voluntary formation, autonomous functioning, democratic control, and professional management of co-operative societies.",
    "97-வது அரசியலமைப்பு திருத்தச் சட்டம் 2011 கூட்டுறவு சங்கங்களை ஊக்குவிக்க பிரிவு 43B-ஐ பகுதி IV-ல் சேர்த்தது.",
    {
        "A": ("Incorrect. 42nd Amendment added Art 39A, 43A, 48A.", "தவறு. 42-வது திருத்தம் பிரிவு 39A, 43A, 48A-ஐச் சேர்த்தது."),
        "B": ("Incorrect. 44th Amendment added Art 38(2).", "தவறு. 44-வது திருத்தம் பிரிவு 38(2)-ஐச் சேர்த்தது."),
        "C": ("Incorrect. 86th Amendment substituted Art 45.", "தவறு. 86-வது திருத்தம் பிரிவு 45-ஐ மாற்றியது."),
        "D": ("Correct. 97th Amendment 2011 inserted Article 43B.", "சரி. 97-வது திருத்தம் 2011 பிரிவு 43B-ஐச் சேர்த்தது.")
    },
    "97th Amendment 2011 added Article 19(1)(c) (co-operatives FR), Article 43B (DPSP), and Part IXB.",
    "97-வது திருத்தம் 2011 பிரிவு 19(1)(c), பிரிவு 43B மற்றும் பகுதி IXB-ஐச் சேர்த்தது.",
    "Article 43B is classified under Gandhian/Liberal-Intellectual Principles.",
    "பிரிவு 43B காந்திய/தாராளமய நெறிமுறைகளின் கீழ் வகைப்படுத்தப்பட்டுள்ளது.",
    ["TNPSC Group 1 PYQ Pattern", "M. Laxmikanth - Indian Polity"]
))

# Q20 (PYQ Pattern) -> Adjust options so Answer is A
q_data.append(make_q(
    "DPSP_PYQ_020", "Easy", "Direct MCQ",
    "Which of the following Directive Principles of State Policy is classified under **Gandhian Principles**?",
    "பின்வரும் அரசு நெறிமுறைப் பிரிவுகளில் எது **காந்தியக் கோட்பாடுகளின்** கீழ் வகைப்படுத்தப்பட்டுள்ளது?",
    [
        ("Article 40 (Village Panchayats)", "பிரிவு 40 (கிராம பஞ்சாயத்துகள்)"),
        ("Article 39A (Free Legal Aid)", "பிரிவு 39A (இலவச சட்ட உதவி)"),
        ("Article 44 (Uniform Civil Code)", "பிரிவு 44 (பொது சிவில் சட்டம்)"),
        ("Article 50 (Separation of Judiciary)", "பிரிவு 50 (நிர்வாகத்திலிருந்து நீதித்துறை பிரிப்பு)")
    ],
    "A",
    "Article 40 (Organisation of Village Panchayats) is a classic Gandhian Principle reflecting Mahatma Gandhi's vision of Gram Swaraj.",
    "பிரிவு 40 (கிராம பஞ்சாயத்துகள்) என்பது கிராம சுயராஜ்யம் பற்றிய காந்தியின் கனவைப் பிரதிபலிக்கும் காந்தியக் கோட்பாடாகும்.",
    {
        "A": ("Correct. Article 40 is a Gandhian Principle.", "சரி. பிரிவு 40 ஒரு காந்தியக் கோட்பாடாகும்."),
        "B": ("Incorrect. Article 39A is a Socialistic Principle.", "தவறு. பிரிவு 39A ஒரு சோசலிசக் கோட்பாடாகும்."),
        "C": ("Incorrect. Article 44 is a Liberal-Intellectual Principle.", "தவறு. பிரிவு 44 ஒரு தாராளமய-அறிவுசார் கோட்பாடாகும்."),
        "D": ("Incorrect. Article 50 is a Liberal-Intellectual Principle.", "தவறு. பிரிவு 50 ஒரு தாராளமய-அறிவுசார் கோட்பாடாகும்.")
    },
    "Gandhian Principles in DPSP: Articles 40, 43, 43B, 46, 47 (prohibition), 48 (cow slaughter prohibition).",
    "DPSP-ல் உள்ள காந்தியக் கோட்பாடுகள்: பிரிவுகள் 40, 43, 43B, 46, 47 (மதுவிலக்கு), 48 (பசு வதைத் தடை).",
    "Socialistic Principles focus on welfare state and economic equality.",
    "சோசலிசக் கோட்பாடுகள் நல அரசு மற்றும் பொருளாதார சமத்துவத்தில் கவனம் செலுத்துகின்றன.",
    ["TNPSC Group 1 PYQ Pattern", "M. Laxmikanth - Indian Polity"]
))

# Q21 (PYQ Pattern) -> Adjust options so Answer is D
q_data.append(make_q(
    "DPSP_PYQ_021", "Medium", "Direct MCQ",
    "Under Article 47, the State is instructed to bring about prohibition of the consumption except for medicinal purposes of which of the following?",
    "பிரிவு 47-ன் கீழ் மருத்துவ நோக்கங்களைத் தவிர எவற்றைப் பயன்படுத்துவதைத் தடுக்க அரசு அறிவுறுத்தப்படுகிறது?",
    [
        ("Cigarettes and Tobacco products", "சிகரெட்டுகள் மற்றும் புகையிலைப் பொருட்கள்"),
        ("Fast food and carbonated beverages", "ஃபாஸ்ட் ஃபுட் மற்றும் குளிர்பானங்கள்"),
        ("Single-use plastics and polythene", "ஒருமுறை பயன்படுத்தும் நெகிழிகள்"),
        ("Intoxicating drinks and drugs harmful to health", "ஆரோக்கியத்திற்கு தீங்கு விளைவிக்கும் மதுபானங்கள் மற்றும் போதைமருந்துகள்")
    ],
    "D",
    "Article 47 explicitly directs the State to endeavour to bring about prohibition of the consumption except for medicinal purposes of intoxicating drinks and of drugs which are injurious to health.",
    "பிரிவு 47 மருத்துவ நோக்கங்களைத் தவிர ஆரோக்கியத்திற்கு தீங்கு விளைவிக்கும் மதுபானங்கள் மற்றும் போதைமருந்துகளைப் பயன்படுத்துவதைத் தடுக்க முயல வேண்டும் எனப் பணிக்கிறது.",
    {
        "A": ("Incorrect. Tobacco is regulated by COTPA Act, but Article 47 specifies intoxicating drinks and harmful drugs.", "தவறு. பிரிவு 47 மதுபானங்கள் மற்றும் போதைமருந்துகளைக் குறிப்பிடுகிறது."),
        "B": ("Incorrect. Fast food is not mentioned in Article 47.", "தவறு. ஃபாஸ்ட் ஃபுட் பிரிவு 47-ல் குறிப்பிடப்படவில்லை."),
        "C": ("Incorrect. Plastics are under environment laws, not Article 47.", "தவறு. நெகிழிகள் சுற்றுச்சூழல் சட்டங்களின் கீழ் உள்ளன."),
        "D": ("Correct. Article 47 explicitly mentions intoxicating drinks and harmful drugs except for medicinal use.", "சரி. பிரிவு 47 மதுபானங்கள் மற்றும் போதைமருந்துகளை பிரத்யேகமாகக் குறிப்பிடுகிறது.")
    },
    "State of Bombay v. F.N. Balsara (1951) upheld prohibition under Article 47.",
    "பால்சாரா (1951) வழக்கு பிரிவு 47-ன் கீழ் மதுவிலக்கை உறுதி செய்தது.",
    "Article 47 contains both Socialistic (nutrition, public health) and Gandhian (prohibition) elements.",
    "பிரிவு 47 சோசலிச மற்றும் காந்திய கூறுகள் இரண்டையும் கொண்டுள்ளது.",
    ["TNPSC Group 1 PYQ Pattern", "M. Laxmikanth - Indian Polity"]
))

# Q22 (PYQ Pattern) -> Answer A
q_data.append(make_q(
    "DPSP_PYQ_022", "Hard", "Direct MCQ",
    "In Randhir Singh v. Union of India (1982), the Supreme Court derived the constitutional principle of 'Equal Pay for Equal Work' by reading Article 39(d) with which Fundamental Rights?",
    "ரந்தீர் சிங் (1982) வழக்கில், பிரிவு 39(d)-ஐ எந்த அடிப்படை உரிமைகளுடன் இணைத்து ஓதுக்கி 'சம வேலைக்கு சம ஊதியம்' என்ற தத்துவத்தை உச்சநீதிமன்றம் பெற்றது?",
    [
        ("Article 14 and Article 21", "பிரிவு 14 மற்றும் பிரிவு 21"),
        ("Article 19 and Article 20", "பிரிவு 19 மற்றும் பிரிவு 20"),
        ("Article 25 and Article 26", "பிரிவு 25 மற்றும் பிரிவு 26"),
        ("Article 32 and Article 226", "பிரிவு 32 மற்றும் பிரிவு 226")
    ],
    "A",
    "In Randhir Singh (1982), the Supreme Court held that 'Equal Pay for Equal Work' under Article 39(d) is a constitutional goal enforceable through Article 14 and Article 21.",
    "ரந்தீர் சிங் (1982) வழக்கில், பிரிவு 39(d)-ன் 'சம வேலைக்கு சம ஊதியம்' என்பது பிரிவு 14 மற்றும் 21 மூலம் அமல்படுத்தப்பட வேண்டிய அரசியலமைப்பு இலக்கு என உச்சநீதிமன்றம் தீர்ப்பளித்தது.",
    {
        "A": ("Correct. Equal Pay for Equal Work was derived by reading Art 39(d) with Art 14 and Art 21.", "சரி. பிரிவு 39(d)-ஐ பிரிவுகள் 14 மற்றும் 21 உடன் இணைத்துப் படித்து சம ஊதிய உரிமை பெறப்பட்டது."),
        "B": ("Incorrect.", "தவறு."),
        "C": ("Incorrect.", "தவறு."),
        "D": ("Incorrect.", "தவறு.")
    },
    "Equal Remuneration Act 1976 provides statutory backing to Article 39(d).",
    "சம ஊதியச் சட்டம் 1976 பிரிவு 39(d)-க்கு சட்டப்பூர்வ ஆதரவை வழங்குகிறது.",
    "Equal pay applies to both temporary and regular employees doing equal work.",
    "சம வேலை செய்யும் தற்காலிக மற்றும் நிரந்தரப் பணியாளர்கள் இருவருக்கும் சம ஊதியம் பொருந்தும்.",
    ["TNPSC Group 1 PYQ Pattern", "M. Laxmikanth - Indian Polity"]
))

# Q23 (PYQ Pattern) -> Answer D
q_data.append(make_q(
    "DPSP_PYQ_023", "Easy", "Direct MCQ",
    "Which Article obligates the State to protect every monument or place or object of artistic or historic interest declared by Parliament to be of national importance?",
    "நாடாளுமன்றச் சட்டத்தால் தேசிய முக்கியத்துவம் வாய்ந்தது என அறிவிக்கப்பட்ட வரலாற்று அல்லது கலைச் சிறப்புமிக்க ஒவ்வொரு சின்னத்தையும் இடத்தையும் பாதுகாப்பது அரசின் கடமை எனக் கூறும் பிரிவு எது?",
    [
        ("Article 47", "பிரிவு 47"),
        ("Article 48", "பிரிவு 48"),
        ("Article 48A", "பிரிவு 48A"),
        ("Article 49", "பிரிவு 49")
    ],
    "D",
    "Article 49 imposes an obligation on the State to protect every monument or place or object of artistic or historic interest declared by Parliament to be of national importance.",
    "பிரிவு 49 தேசிய முக்கியத்துவம் வாய்ந்த வரலாற்று அல்லது கலைச் சிறப்புமிக்க ஒவ்வொரு சின்னத்தையும் இடத்தையும் பாதுகாப்பது அரசின் கடமை எனக் கூறுகிறது.",
    {
        "A": ("Incorrect. Article 47 deals with public health and prohibition.", "தவறு. பிரிவு 47 பொது சுகாதாரத்தைக் கையாள்கிறது."),
        "B": ("Incorrect. Article 48 deals with agriculture and animal husbandry.", "தவறு. பிரிவு 48 வேளாண்மையைக் கையாள்கிறது."),
        "C": ("Incorrect. Article 48A deals with environment and wildlife.", "தவறு. பிரிவு 48A சுற்றுச்சூழலைக் கையாள்கிறது."),
        "D": ("Correct. Article 49 explicitly mandates protection of national monuments.", "சரி. பிரிவு 49 தேசிய வரலாற்றுச் சின்னங்களைப் பாதுகாப்பதைப் பணிக்கிறது.")
    },
    "Ancient Monuments and Archaeological Sites and Remains Act 1958 implements Article 49.",
    "பழங்காலச் சின்னங்கள் மற்றும் தொல்பொருள் இடங்கள் சட்டம் 1958 பிரிவு 49-ஐ அமல்படுத்துகிறது.",
    "Article 49 is classified under Liberal-Intellectual Principles.",
    "பிரிவு 49 தாராளமய-அறிவுசார் கோட்பாடுகளின் கீழ் உள்ளது.",
    ["TNPSC Group 1 PYQ Pattern", "M. Laxmikanth - Indian Polity"]
))

# Q24 (PYQ Pattern) -> Answer D
q_data.append(make_q(
    "DPSP_PYQ_024", "Easy", "Direct MCQ",
    "Which Article of Part IV contains the directive for promoting international peace and security, maintaining just relations between nations, and settlement of international disputes by arbitration?",
    "சர்வதேச அமைதி மற்றும் பாதுகாப்பை மேம்படுத்துதல், நாடுகளுக்கிடையே நியாயமான உறவுகளைப் பராமரித்தல் மற்றும் தகராறுகளை மத்தியஸ்தம் மூலம் தீர்ப்பதற்கான நெறிமுறையைக் கொண்டுள்ள பகுதி IV-ன் பிரிவு எது?",
    [
        ("Article 48", "பிரிவு 48"),
        ("Article 49", "பிரிவு 49"),
        ("Article 50", "பிரிவு 50"),
        ("Article 51", "பிரிவு 51")
    ],
    "D",
    "Article 51 directs the State to promote international peace and security, maintain just and honourable relations between nations, foster respect for international law, and encourage settlement of international disputes by arbitration.",
    "பிரிவு 51 சர்வதேச அமைதி மற்றும் பாதுகாப்பை மேம்படுத்தவும், நாடுகளுக்கிடையே நியாயமான உறவுகளைப் பராமரிக்கவும் அரசைப் பணிக்கிறது.",
    {
        "A": ("Incorrect. Article 48 deals with agriculture and animal husbandry.", "தவறு. பிரிவு 48 வேளாண்மையைக் கையாள்கிறது."),
        "B": ("Incorrect. Article 49 deals with monuments protection.", "தவறு. பிரிவு 49 வரலாற்றுச் சின்னங்களைப் பாதுகாப்பதைக் கையாள்கிறது."),
        "C": ("Incorrect. Article 50 deals with separation of judiciary.", "தவறு. பிரிவு 50 நீதித்துறை பிரிப்பைக் கையாள்கிறது."),
        "D": ("Correct. Article 51 explicitly covers international peace and foreign policy.", "சரி. பிரிவு 51 சர்வதேச அமைதி மற்றும் வெளியுறவுக் கொள்கையைக் கையாள்கிறது.")
    },
    "Article 51 is the LAST Directive Principle in Part IV.",
    "பிரிவு 51 என்பது பகுதி IV-ல் உள்ள கடைசி நெறிமுறையாகும்.",
    "Article 51 forms the constitutional bedrock of India's Foreign Policy (Panchsheel, Non-Alignment).",
    "பிரிவு 51 இந்தியாவின் வெளியுறவுக் கொள்கையின் அரசியலமைப்பு அடித்தளமாகும்.",
    ["TNPSC Group 1 PYQ Pattern", "M. Laxmikanth - Indian Polity"]
))

# Q25 (PYQ Pattern) -> Answer D
q_data.append(make_q(
    "DPSP_PYQ_025", "Medium", "Statement Based",
    "Consider the following statements regarding Directive Principles of State Policy:\n\n1. They are non-justiciable and cannot be directly enforced in courts.\n2. They were borrowed from the Constitution of Ireland.\n3. They are declared fundamental in the governance of the country.\n\nWhich of the above statements are correct?",
    "அரசு நெறிமுறைப்படுத்தும் கோட்பாடுகள் பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n\n1. அவை நீதிமன்றத்தால் அமல்படுத்தப்பட முடியாதவை.\n2. அவை அயர்லாந்து அரசியலமைப்பிலிருந்து பெறப்பட்டவை.\n3. அவை நாட்டின் ஆட்சியில் அடிப்படைத் தன்மையானவை என அறிவிக்கப்பட்டுள்ளன.\n\nமேற்கண்ட கூற்றுகளில் எவை சரியானவை?",
    [
        ("1 and 2 only", "1 மற்றும் 2 மட்டும்"),
        ("2 and 3 only", "2 மற்றும் 3 மட்டும்"),
        ("1 and 3 only", "1 மற்றும் 3 மட்டும்"),
        ("1, 2 and 3", "1, 2 மற்றும் 3")
    ],
    "D",
    "All three statements are correct: DPSPs are non-justiciable (Art 37), borrowed from Ireland (1937), and declared fundamental in governance (Art 37).",
    "மூன்று கூற்றுகளும் சரியானவை: நெறிமுறைகள் நீதிமன்றத்தால் அமல்படுத்த முடியாதவை (பிரிவு 37), அயர்லாந்திலிருந்து பெறப்பட்டவை, மற்றும் ஆட்சியில் அடிப்படைத் தன்மையானவை.",
    {
        "A": ("Incorrect. Statement 3 is also correct.", "தவறு. கூற்று 3-ம் சரியானது."),
        "B": ("Incorrect. Statement 1 is also correct.", "தவறு. கூற்று 1-ம் சரியானது."),
        "C": ("Incorrect. Statement 2 is also correct.", "தவறு. கூற்று 2-ம் சரியானது."),
        "D": ("Correct. All 3 statements are factually and constitutionally true.", "சரி. 3 கூற்றுகளும் சரியானவை.")
    },
    "Article 37 explicitly contains both Statement 1 (non-justiciable) and Statement 3 (fundamental in governance).",
    "பிரிவு 37 கூற்று 1 மற்றும் கூற்று 3 இரண்டையும் தெளிவாகக் கொண்டுள்ளது.",
    "DPSP are contained in Part IV from Articles 36 to 51.",
    "DPSP பகுதி IV-ல் பிரிவுகள் 36 முதல் 51 வரை உள்ளது.",
    ["TNPSC Group 1 PYQ Pattern", "M. Laxmikanth - Indian Polity"]
))

# Q26 (PYQ Pattern) -> Adjust options so Answer is A
q_data.append(make_q(
    "DPSP_PYQ_026", "Medium", "Direct MCQ",
    "Granville Austin described the Directive Principles of State Policy along with Fundamental Rights as which of the following?",
    "கிரான்வில் ஆஸ்டின் அரசு நெறிமுறைப்படுத்தும் கோட்பாடுகளை அடிப்படை உரிமைகளுடன் சேர்த்து பின்வருவனவற்றில் எவ்வாறு விவரித்தார்?",
    [
        ("Conscience of the Constitution", "அரசியலமைப்பின் மனசாட்சி"),
        ("Heart and Soul of the Constitution", "அரசியலமைப்பின் இதயமும் ஆன்மாவும்"),
        ("Magna Carta of India", "இந்தியாவின் மகா சாசனம்"),
        ("Instrument of Instructions", "அறிவுறுத்தல் கருவி")
    ],
    "A",
    "Granville Austin described Part III (Fundamental Rights) and Part IV (Directive Principles) together as the 'Conscience of the Constitution'.",
    "கிரான்வில் ஆஸ்டின் பகுதி III மற்றும் பகுதி IV ஆகிய இரண்டையும் சேர்த்து 'அரசியலமைப்பின் மனசாட்சி' என்று விவரித்தார்.",
    {
        "A": ("Correct. Granville Austin called DPSP + FR the 'Conscience of the Constitution'.", "சரி. கிரான்வில் ஆஸ்டின் DPSP + FR-ஐ 'அரசியலமைப்பின் மனசாட்சி' என்று அழைத்தார்."),
        "B": ("Incorrect. Ambedkar called Article 32 the 'Heart and Soul of the Constitution'.", "தவறு. அம்பேத்கர் பிரிவு 32-ஐ 'இதயமும் ஆன்மாவும்' என்றார்."),
        "C": ("Incorrect. Part III alone is called the 'Magna Carta of India'.", "தவறு. பகுதி III மட்டுமே 'இந்தியாவின் மகா சாசனம்' எனப்படுகிறது."),
        "D": ("Incorrect. Instrument of Instructions refers to GOI Act 1935 context.", "தவறு. அறிவுறுத்தல் கருவி என்பது 1935 சட்டத்தைக் குறிக்கிறது.")
    },
    "Ambedkar = 'Novel Feature' (DPSP). Granville Austin = 'Conscience of the Constitution' (FR + DPSP). Ambedkar = 'Heart & Soul' (Art 32).",
    "அம்பேத்கர் = 'புதுமையான அம்சம்' (DPSP). கிரான்வில் ஆஸ்டின் = 'மனசாட்சி' (FR + DPSP). அம்பேத்கர் = 'இதயமும் ஆன்மாவும்' (பிரிவு 32).",
    "Granville Austin was an eminent American historian of the Indian Constitution.",
    "கிரான்வில் ஆஸ்டின் இந்திய அரசியலமைப்பின் புகழ்பெற்ற வரலாற்று ஆசிரியர் ஆவார்.",
    ["TNPSC Group 1 PYQ Pattern", "M. Laxmikanth - Indian Polity"]
))

# Q27 (PYQ Pattern) -> Adjust options so Answer is A
q_data.append(make_q(
    "DPSP_PYQ_027", "Easy", "Direct MCQ",
    "Article 39(f) was modified by the 42nd Constitutional Amendment Act 1976 to ensure that children are given opportunities and facilities to develop in a healthy manner and in conditions of freedom and dignity.",
    "குழந்தைகள் சுதந்திரம் மற்றும் கண்ணியமான சூழலில் ஆரோக்கியமாக வளர வாய்ப்புகளும் வசதிகளும் வழங்கப்படுவதை உறுதி செய்ய 42-வது திருத்தச் சட்டம் 1976 மூலம் பிரிவு 39(f) திருத்தப்பட்டது. இக்கூற்று சரியா தவறா?",
    [
        ("True", "சரி"),
        ("False", "தவறு"),
        ("Partially True", "பகுதி சரி"),
        ("None of the above", "எதுவும் இல்லை")
    ],
    "A",
    "Statement is TRUE. The 42nd Amendment Act 1976 modified Article 39(f) to direct the State to secure that children are given opportunities and facilities to develop in a healthy manner and in conditions of freedom and dignity.",
    "கூற்று சரியானது. 42-வது திருத்தச் சட்டம் 1976 பிரிவு 39(f)-ஐத் திருத்தி குழந்தைகள் ஆரோக்கியமாக வளர வாய்ப்புகளை வழங்க அரசைப் பணித்தது.",
    {
        "A": ("Correct. Article 39(f) was indeed modified by the 42nd Amendment 1976.", "சரி. பிரிவு 39(f) 42-வது திருத்தம் 1976 மூலம் திருத்தப்பட்டது."),
        "B": ("Incorrect.", "தவறு."),
        "C": ("Incorrect.", "தவறு."),
        "D": ("Incorrect.", "தவறு.")
    },
    "Original Article 39(f) was modified by 42nd Amendment 1976 to protect youth and childhood against exploitation.",
    "மூல பிரிவு 39(f) இளைஞர்கள் மற்றும் குழந்தைகளைப் பாதுகாக்க 42-வது திருத்தம் 1976 மூலம் திருத்தப்பட்டது.",
    "Child Labour Prohibition Act 1986 implements Article 39(f).",
    "குழந்தைகள் தொழிலாளர் தடைச் சட்டம் 1986 பிரிவு 39(f)-ஐ அமல்படுத்துகிறது.",
    ["TNPSC Group 1 PYQ Pattern", "M. Laxmikanth - Indian Polity"]
))

# Q28 (PYQ Pattern) -> Adjust options so Answer is D
q_data.append(make_q(
    "DPSP_PYQ_028", "Medium", "Direct MCQ",
    "Which Parliamentary Act was passed in 1987 to operationalize Article 39A (Equal Justice and Free Legal Aid)?",
    "பிரிவு 39A-ஐ (சம நீதி மற்றும் இலவச சட்ட உதவி) செயல்படுத்துவதற்காக 1987-ல் நாடாளுமன்றத்தால் இயற்றப்பட்ட சட்டம் எது?",
    [
        ("Advocates Act 1961", "வழக்கறிஞர்கள் சட்டம் 1961"),
        ("Code of Civil Procedure 1908", "உரிமையியல் நடைமுறைச் சட்டம் 1908"),
        ("Protection of Human Rights Act 1993", "மனித உரிமைகள் பாதுகாப்புச் சட்டம் 1993"),
        ("Legal Services Authorities Act 1987", "சட்டப் பணிகள் ஆணைக்குழுச் சட்டம் 1987")
    ],
    "D",
    "The Legal Services Authorities Act 1987 was passed by Parliament to fulfill Article 39A, establishing NALSA and Lok Adalats to provide free and competent legal services to the weaker sections.",
    "பிரிவு 39A-ஐ நிறைவேற்ற 1987-ல் சட்டப் பணிகள் ஆணைக்குழுச் சட்டம் நிறைவேற்றப்பட்டு NALSA மற்றும் லோக் அதாலத்துகள் அமைக்கப்பட்டன.",
    {
        "A": ("Incorrect. Advocates Act 1961 regulates legal practitioners.", "தவறு. வழக்கறிஞர்கள் சட்டம் 1961 வழக்கறிஞர்களை முறைப்படுத்துகிறது."),
        "B": ("Incorrect. CPC regulates civil trials.", "தவறு. CPC சிவில் வழக்குகளை முறைப்படுத்துகிறது."),
        "C": ("Incorrect. Protection of Human Rights Act 1993 established NHRC.", "தவறு. மனித உரிமைகள் பாதுகாப்புச் சட்டம் NHRC-ஐ நிறுவியது."),
        "D": ("Correct. Legal Services Authorities Act 1987 operationalized Article 39A.", "சரி. சட்டப் பணிகள் ஆணைக்குழுச் சட்டம் 1987 பிரிவு 39A-ஐ அமல்படுத்தியது.")
    },
    "NALSA came into force on November 9, 1995 (celebrated as National Legal Services Day).",
    "NALSA நவம்பர் 9, 1995 அன்று அமலுக்கு வந்தது (தேசிய சட்டப் பணிகள் தினமாகக் கொண்டாடப்படுகிறது).",
    "Lok Adalats have statutory status under Legal Services Authorities Act 1987.",
    "லோக் அதாலத்துகள் 1987 சட்டத்தின் கீழ் சட்டப்பூர்வ அந்தஸ்தைப் பெற்றுள்ளன.",
    ["TNPSC Group 1 PYQ Pattern", "M. Laxmikanth - Indian Polity"]
))

# Q29 (PYQ Pattern) -> Adjust options so Answer is A
q_data.append(make_q(
    "DPSP_PYQ_029", "Medium", "Direct MCQ",
    "Which Committee appointed in 1957 was the first to recommend a 3-tier Panchayati Raj system to implement Article 40 of DPSP?",
    "பிரிவு 40-ஐ அமல்படுத்த 3 அடுக்கு பஞ்சாயத்து ராஜ் முறையைப் பரிந்துரைத்த முதல் குழு எது (1957-ல் அமைக்கப்பட்டது)?",
    [
        ("Balwant Rai Mehta Committee (1957)", "பல்வந்த் ராய் மேத்தா குழு (1957)"),
        ("Ashok Mehta Committee (1977)", "அசோக் மேத்தா குழு (1977)"),
        ("G.V.K. Rao Committee (1985)", "ஜி.வி.கே. ராவ் குழு (1985)"),
        ("L.M. Singhvi Committee (1986)", "எல்.எம். சிங்வி குழு (1986)")
    ],
    "A",
    "Balwant Rai Mehta Committee (1957) recommended the establishment of a 3-tier Panchayati Raj system (Gram Panchayat, Panchayat Samiti, Zilla Parishad) to implement Article 40.",
    "பல்வந்த் ராய் மேத்தா குழு (1957) பிரிவு 40-ஐ அமல்படுத்த 3 அடுக்கு பஞ்சாயத்து ராஜ் முறையைப் பரிந்துரைத்தது.",
    {
        "A": ("Correct. Balwant Rai Mehta Committee 1957 recommended 3-tier Panchayati Raj.", "சரி. பல்வந்த் ராய் மேத்தா குழு 1957 3 அடுக்கு முறையைப் பரிந்துரைத்தது."),
        "B": ("Incorrect. Ashok Mehta Committee 1977 recommended 2-tier system.", "தவறு. அசோக் மேத்தா குழு 1977 2 அடுக்கு முறையைப் பரிந்துரைத்தது."),
        "C": ("Incorrect. G.V.K. Rao Committee 1985 focused on administrative arrangements.", "தவறு. ஜி.வி.கே. ராவ் குழு 1985 நிர்வாக அமைப்புகளில் கவனம் செலுத்தியது."),
        "D": ("Incorrect. L.M. Singhvi Committee 1986 recommended constitutional status.", "தவறு. எல்.எம். சிங்வி குழு 1986 அரசியலமைப்பு அந்தஸ்தைப் பரிந்துரைத்தது.")
    },
    "Rajasthan was the first State to establish Panchayati Raj (Nagaur district, Oct 2, 1959).",
    "ராஜஸ்தான் பஞ்சாயத்து ராஜை நிறுவிய முதல் மாநிலமாகும் (நாகவுர் மாவட்டம், அக்டோபர் 2, 1959).",
    "73rd Amendment Act 1992 constitutionalized Panchayati Raj.",
    "73-வது திருத்தச் சட்டம் 1992 பஞ்சாயத்து ராஜிற்கு அரசியலமைப்பு அந்தஸ்து வழங்கியது.",
    ["TNPSC Group 1 PYQ Pattern", "M. Laxmikanth - Indian Polity"]
))

# Q30 (PYQ Pattern) -> Adjust options so Answer is C
q_data.append(make_q(
    "DPSP_PYQ_030", "Easy", "Direct MCQ",
    "Which Article of Part IV directs the State to endeavour to secure to all workers a living wage, a decent standard of life, and the promotion of cottage industries?",
    "தொழிலாளர்களுக்கு வாழ்வாதார ஊதியம், கண்ணியமான வாழ்க்கைத்தரம் மற்றும் குடிசைத் தொழில்களை ஊக்குவிப்பதை உறுதி செய்யப் பணிக்கும் பகுதி IV-ன் பிரிவு எது?",
    [
        ("Article 41", "பிரிவு 41"),
        ("Article 42", "பிரிவு 42"),
        ("Article 43", "பிரிவு 43"),
        ("Article 44", "பிரிவு 44")
    ],
    "C",
    "Article 43 directs the State to endeavour to secure to all workers a living wage, a decent standard of life, and full enjoyment of leisure, and to promote cottage industries on an individual or co-operative basis in rural areas.",
    "பிரிவு 43 தொழிலாளர்களுக்கு வாழ்வாதார ஊதியம், கண்ணியமான வாழ்க்கைத்தரம் மற்றும் குடிசைத் தொழில்களை ஊக்குவிப்பதை உறுதி செய்யப் பணிக்கிறது.",
    {
        "A": ("Incorrect. Article 41 deals with right to work and education.", "தவறு. பிரிவு 41 வேலை உரிமையைக் கையாள்கிறது."),
        "B": ("Incorrect. Article 42 deals with maternity relief.", "தவறு. பிரிவு 42 மகப்பேறு உதவியைக் கையாள்கிறது."),
        "C": ("Correct. Article 43 explicitly covers living wage and cottage industries.", "சரி. பிரிவு 43 வாழ்வாதார ஊதியம் மற்றும் குடிசைத் தொழில்களைக் கையாள்கிறது."),
        "D": ("Incorrect. Article 44 deals with Uniform Civil Code.", "தவறு. பிரிவு 44 பொது சிவில் சட்டத்தைக் கையாள்கிறது.")
    },
    "Minimum Wages Act 1948 was enacted to fulfill Article 43.",
    "குறைந்தபட்ச ஊதியச் சட்டம் 1948 பிரிவு 43-ஐ நிறைவேற்ற இயற்றப்பட்டது.",
    "Article 43 contains both Socialistic (living wage) and Gandhian (cottage industries) elements.",
    "பிரிவு 43 சோசலிச மற்றும் காந்திய கூறுகள் இரண்டையும் கொண்டுள்ளது.",
    ["TNPSC Group 1 PYQ Pattern", "M. Laxmikanth - Indian Polity"]
))

# Q31 (PYQ Pattern) -> Adjust options so Answer is D
q_data.append(make_q(
    "DPSP_PYQ_031", "Medium", "Direct MCQ",
    "The 42nd Constitutional Amendment Act 1976 inserted Article 43A to secure the participation of workers in the management of which of the following?",
    "42-வது திருத்தச் சட்டம் 1976 தொழிலாளர்களின் பங்கேற்பை எந்தத் துறையின் மேலாண்மையில் உறுதி செய்ய பிரிவு 43A-ஐச் சேர்த்தது?",
    [
        ("Political Parties and Electoral Reforms", "அரசியல் கட்சிகள் மற்றும் தேர்தல் சீர்திருத்தங்கள்"),
        ("Panchayati Raj Bodies and Municipalities", "பஞ்சாயத்து ராஜ் அமைப்புகள் மற்றும் நகராட்சிகள்"),
        ("Educational institutions and Universities", "கல்வி நிறுவனங்கள் மற்றும் பல்கலைக்கழகங்கள்"),
        ("Undertakings, establishments, or other organisations engaged in industry", "தொழில்துறையில் ஈடுபட்டுள்ள நிறுவனங்கள் அல்லது அமைப்புகள்")
    ],
    "D",
    "Article 43A states: 'The State shall take steps, by suitable legislation or in any other way, to secure the participation of workers in the management of undertakings, establishments or other organisations engaged in any industry.'",
    "பிரிவு 43A: 'தொழில்துறையில் ஈடுபட்டுள்ள நிறுவனங்களின் மேலாண்மையில் தொழிலாளர்களின் பங்கேற்பை உறுதி செய்ய அரசு நடவடிக்கை எடுக்க வேண்டும்' எனக் கூறுகிறது.",
    {
        "A": ("Incorrect.", "தவறு."),
        "B": ("Incorrect.", "தவறு."),
        "C": ("Incorrect.", "தவறு."),
        "D": ("Correct. Article 43A specifies participation of workers in industrial management.", "சரி. பிரிவு 43A தொழிற்துறை மேலாண்மையில் தொழிலாளர் பங்கேற்பைக் குறிப்பிடுகிறது.")
    },
    "Article 43A is a Socialistic Principle added by the 42nd Amendment Act 1976.",
    "பிரிவு 43A என்பது 42-வது திருத்தச் சட்டம் 1976 மூலம் சேர்க்கப்பட்ட ஒரு சோசலிசக் கோட்பாடாகும்.",
    "Industrial Disputes Act and Joint Management Councils operationalize Article 43A.",
    "தொழில்தகராறுகள் சட்டம் மற்றும் இணை மேலாண்மைக் குழுக்கள் பிரிவு 43A-ஐச் செயல்படுத்துகின்றன.",
    ["TNPSC Group 1 PYQ Pattern", "M. Laxmikanth - Indian Polity"]
))

# Q32 (PYQ Pattern) -> Adjust options so Answer is C
q_data.append(make_q(
    "DPSP_PYQ_032", "Easy", "Direct MCQ",
    "Which State in India currently has an operational Uniform Civil Code as per the vision of Article 44?",
    "பிரிவு 44-ன் பார்வையின்படி தற்போது எந்த இந்திய மாநிலத்தில் பொது சிவில் சட்டம் அமலில் உள்ளது?",
    [
        ("Kerala", "கேரளா"),
        ("Tamil Nadu", "தமிழ்நாடு"),
        ("Goa", "கோவா"),
        ("Maharashtra", "மகாராஷ்டிரா")
    ],
    "C",
    "Goa is the only State in India that has a Uniform Civil Code (Goa Civil Code 1867), retained post-liberation in 1961.",
    "கோவா இந்தியாவில் பொது சிவில் சட்டம் (கோவா சிவில் சட்டம் 1867) அமலில் உள்ள ஒரே மாநிலமாகும்.",
    {
        "A": ("Incorrect.", "தவறு."),
        "B": ("Incorrect.", "தவறு."),
        "C": ("Correct. Goa has a Uniform Civil Code applied to all communities.", "சரி. கோவாவில் அனைத்து சமூகங்களுக்கும் பொது சிவில் சட்டம் அமலில் உள்ளது."),
        "D": ("Incorrect.", "தவறு.")
    },
    "Goa Civil Code 1867 was introduced during Portuguese rule and continued post-1961.",
    "கோவா சிவில் சட்டம் 1867 போர்த்துகீசிய ஆட்சியில் அறிமுகப்படுத்தப்பட்டு 1961க்குப் பிறகும் தொடர்ந்தது.",
    "Uttarakhand passed a Uniform Civil Code Bill in 2024.",
    "உத்தரகாண்ட் 2024-ல் பொது சிவில் சட்ட மசோதாவை நிறைவேற்றியது.",
    ["TNPSC Group 1 PYQ Pattern", "M. Laxmikanth - Indian Polity"]
))

# Q33 (PYQ Pattern) -> Adjust options so Answer is A
q_data.append(make_q(
    "DPSP_PYQ_033", "Hard", "Direct MCQ",
    "Article 46 directs the State to promote the educational and economic interests of SCs, STs, and weaker sections. Which Amendment Act introduced Article 15(4) to enable special provisions fulfilling Article 46?",
    "பிரிவு 46-ஐ நிறைவேற்ற சிறப்பு விதிகளை உருவாக்க வழிவகுக்கும் பிரிவு 15(4)-ஐ அறிமுகப்படுத்திய அரசியலமைப்பு திருத்தச் சட்டம் எது?",
    [
        ("1st Amendment Act 1951", "1-வது திருத்தச் சட்டம் 1951"),
        ("7th Amendment Act 1956", "7-வது திருத்தச் சட்டம் 1956"),
        ("24th Amendment Act 1971", "24-வது திருத்தச் சட்டம் 1971"),
        ("42nd Amendment Act 1976", "42-வது திருத்தச் சட்டம் 1976")
    ],
    "A",
    "The 1st Constitutional Amendment Act 1951 inserted Article 15(4) into Part III to allow the State to make special provisions for the advancement of socially and educationally backward classes or SCs/STs, directly implementing Article 46.",
    "1-வது திருத்தச் சட்டம் 1951 பிரிவு 15(4)-ஐச் சேர்த்து, பிரிவு 46-ஐ நிறைவேற்றும் வகையில் பிற்படுத்தப்பட்ட வகுப்பினருக்கு சிறப்பு விதிகளை உருவாக்க அரசை அனுமதித்தது.",
    {
        "A": ("Correct. 1st Amendment 1951 inserted Article 15(4) following Champakam Dorairajan ruling.", "சரி. 1-வது திருத்தம் 1951 பிரிவு 15(4)-ஐச் சேர்த்தது."),
        "B": ("Incorrect.", "தவறு."),
        "C": ("Incorrect.", "தவறு."),
        "D": ("Incorrect.", "தவறு.")
    },
    "Champakam Dorairajan (1951) case led directly to the 1st Amendment Act 1951.",
    "செம்பகம் துரைராஜன் (1951) வழக்கு 1-வது திருத்தச் சட்டம் 1951-க்கு நேரடியாக வழிவகுத்தது.",
    "Article 46 is a Gandhian Directive Principle.",
    "பிரிவு 46 ஒரு காந்திய நெறிமுறையாகும்.",
    ["TNPSC Group 1 PYQ Pattern", "M. Laxmikanth - Indian Polity"]
))

# Q34 (PYQ Pattern) -> Adjust options so Answer is C
q_data.append(make_q(
    "DPSP_PYQ_034", "Medium", "Direct MCQ",
    "State of Bombay v. F.N. Balsara (1951) upheld statutory liquor prohibition as a reasonable restriction on trade under Article 19(6) based on which DPSP?",
    "பால்சாரா (1951) வழக்கில், எந்த அரசு நெறிமுறையின் அடிப்படையில் சட்டப்பூர்வ மதுவிலக்கை பிரிவு 19(6)-ன் கீழ் நியாயமான கட்டுப்பாடாக உச்சநீதிமன்றம் உறுதி செய்தது?",
    [
        ("Article 39", "பிரிவு 39"),
        ("Article 43", "பிரிவு 43"),
        ("Article 47", "பிரிவு 47"),
        ("Article 50", "பிரிவு 50")
    ],
    "C",
    "In State of Bombay v. F.N. Balsara (1951), the Supreme Court held that enforcing prohibition under Article 47 forms a reasonable restriction under Article 19(6).",
    "பால்சாரா (1951) வழக்கில், பிரிவு 47-ன் கீழ் மதுவிலக்கை அமல்படுத்துவது பிரிவு 19(6)-ன் கீழ் நியாயமான கட்டுப்பாடு என உச்சநீதிமன்றம் தீர்ப்பளித்தது.",
    {
        "A": ("Incorrect.", "தவறு."),
        "B": ("Incorrect.", "தவறு."),
        "C": ("Correct. Article 47 directive for prohibition was upheld in F.N. Balsara case.", "சரி. பால்சாரா வழக்கில் பிரிவு 47 மதுவிலக்கு நெறிமுறை உறுதி செய்யப்பட்டது."),
        "D": ("Incorrect.", "தவறு.")
    },
    "Article 47 directs prohibition of intoxicating drinks except for medicinal purposes.",
    "பிரிவு 47 மருத்துவ நோக்கங்களைத் தவிர மதுவிலக்கை அமல்படுத்தப் பணிக்கிறது.",
    "Prohibition is a Gandhian Directive Principle.",
    "மதுவிலக்கு ஒரு காந்திய நெறிமுறையாகும்.",
    ["TNPSC Group 1 PYQ Pattern", "M. Laxmikanth - Indian Polity"]
))

# Q35 (PYQ Pattern) -> Adjust options so Answer is D
q_data.append(make_q(
    "DPSP_PYQ_035", "Hard", "Direct MCQ",
    "State of Gujarat v. Mirzapur Moti Kureshi Kassab Jamat (2005) upheld total ban on cow slaughter based on Article 48. What was the Bench Strength of the Supreme Court in this case?",
    "மிர்சாபூர் மோதி குரேஷி (2005) வழக்கில் பிரிவு 48-ன் கீழ் பசு வதை முழுத் தடையை உச்சநீதிமன்றம் உறுதி செய்தது. இவ்வழக்கை விசாரித்த அமர்வில் எத்தனை நீதிபதிகள் இருந்தனர்?",
    [
        ("3-judge bench", "3 நீதிபதிகள் அமர்வு"),
        ("5-judge Constitution Bench", "5 நீதிபதிகள் அரசியலமைப்பு அமர்வு"),
        ("9-judge bench", "9 நீதிபதிகள் அமர்வு"),
        ("7-judge Constitution Bench", "7 நீதிபதிகள் அரசியலமைப்பு அமர்வு")
    ],
    "D",
    "In State of Gujarat v. Mirzapur Moti Kureshi (2005), a 7-judge Constitution Bench of the Supreme Court upheld total ban on slaughter of cows and their progeny under Article 48 and Article 48A.",
    "மிர்சாபூர் மோதி குரேஷி (2005) வழக்கில் 7 நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வு பிரிவு 48 & 48A-ன் கீழ் பசு வதை முழுத் தடையை உறுதி செய்தது.",
    {
        "A": ("Incorrect.", "தவறு."),
        "B": ("Incorrect.", "தவறு."),
        "C": ("Incorrect.", "தவறு."),
        "D": ("Correct. 7-judge Constitution Bench decided Mirzapur Moti Kureshi case in 2005.", "சரி. 7 நீதிபதிகள் கொண்ட அமர்வு மிர்சாபூர் மோதி குரேஷி வழக்கில் தீர்ப்பளித்தது.")
    },
    "Mirzapur case (2005) overruled previous narrower rulings and upheld total ban on cow slaughter.",
    "மிர்சாபூர் வழக்கு (2005) முந்தைய தீர்ப்புகளை ரத்து செய்து பசு வதை முழுத் தடையை உறுதி செய்தது.",
    "Articles 48 and 48A were read together with Fundamental Duties (Art 51A(g)).",
    "பிரிவுகள் 48 மற்றும் 48A அடிப்படைக் கடமைகளுடன் (பிரிவு 51A(g)) சேர்த்துப் படிக்கப்பட்டன.",
    ["TNPSC Group 1 PYQ Pattern", "M. Laxmikanth - Indian Polity"]
))

# Q36 (PYQ Pattern) -> Adjust options so Answer is A
q_data.append(make_q(
    "DPSP_PYQ_036", "Easy", "Direct MCQ",
    "Which Constitutional Amendment added Article 48A (Environment, forests, and wildlife protection) to Part IV?",
    "பகுதி IV-ல் பிரிவு 48A-ஐ (சுற்றுச்சூழல், காடுகள் மற்றும் வனவிலங்கு பாதுகாப்பு) சேர்த்த அரசியலமைப்பு திருத்தம் எது?",
    [
        ("42nd Amendment 1976", "42-வது திருத்தம் 1976"),
        ("25th Amendment 1971", "25-வது திருத்தம் 1971"),
        ("44th Amendment 1978", "44-வது திருத்தம் 1978"),
        ("86th Amendment 2002", "86-வது திருத்தம் 2002")
    ],
    "A",
    "The 42nd Constitutional Amendment Act 1976 inserted Article 48A into Part IV directing the State to protect and improve the environment.",
    "42-வது திருத்தச் சட்டம் 1976 பகுதி IV-ல் பிரிவு 48A-ஐச் சேர்த்து சுற்றுச்சூழலைப் பாதுகாக்க அரசைப் பணிக்கிறது.",
    {
        "A": ("Correct. 42nd Amendment 1976 added Article 48A.", "சரி. 42-வது திருத்தம் 1976 பிரிவு 48A-ஐச் சேர்த்தது."),
        "B": ("Incorrect.", "தவறு."),
        "C": ("Incorrect.", "தவறு."),
        "D": ("Incorrect.", "தவறு.")
    },
    "Article 48A works together with Article 51A(g) (Fundamental Duty for environment).",
    "பிரிவு 48A பிரிவு 51A(g) உடன் இணைந்து செயல்படுகிறது.",
    "Both Article 48A and 51A(g) were added by 42nd Amendment 1976.",
    "பிரிவு 48A மற்றும் 51A(g) இரண்டும் 42-வது திருத்தம் 1976 மூலம் சேர்க்கப்பட்டவை.",
    ["TNPSC Group 1 PYQ Pattern", "M. Laxmikanth - Indian Polity"]
))

# Q37 (PYQ Pattern) -> Adjust options so Answer is D
q_data.append(make_q(
    "DPSP_PYQ_037", "Medium", "Direct MCQ",
    "Which Code revised in 1973 implemented Article 50 by separating Judicial Magistrates from Executive Magistrates under High Court control?",
    "உயர்நீதிமன்றக் கட்டுப்பாட்டின் கீழ் நீதித்துறை நடுவர்களை நிர்வாக நடுவர்களிடமிருந்து பிரித்து பிரிவு 50-ஐ அமல்படுத்திய 1973-ல் திருத்தப்பட்ட சட்டம் எது?",
    [
        ("Indian Penal Code 1860", "இந்திய தண்டனைச் சட்டம் 1860"),
        ("Indian Evidence Act 1872", "இந்திய சாட்சியச் சட்டம் 1872"),
        ("Civil Procedure Code 1908", "உரிமையியல் நடைமுறைச் சட்டம் 1908"),
        ("Code of Criminal Procedure 1973 (CrPC)", "குற்றவியல் நடைமுறைச் சட்டம் 1973 (CrPC)")
    ],
    "D",
    "The Code of Criminal Procedure 1973 (CrPC) effected a structural separation of Judicial Magistrates from Executive Magistrates under the High Court, fulfilling Article 50.",
    "குற்றவியல் நடைமுறைச் சட்டம் 1973 (CrPC) நீதித்துறை நடுவர்களை நிர்வாக நடுவர்களிடமிருந்து பிரித்து பிரிவு 50-ஐ நிறைவேற்றியது.",
    {
        "A": ("Incorrect.", "தவறு."),
        "B": ("Incorrect.", "தவறு."),
        "C": ("Incorrect.", "தவறு."),
        "D": ("Correct. CrPC 1973 implemented Article 50 separation of judiciary.", "சரி. CrPC 1973 பிரிவு 50 நீதித்துறை பிரிப்பை அமல்படுத்தியது.")
    },
    "CrPC 1973 came into force on April 1, 1974.",
    "CrPC 1973 ஏப்ரல் 1, 1974 அன்று அமலுக்கு வந்தது.",
    "Article 50 is a Liberal-Intellectual Directive Principle.",
    "பிரிவு 50 ஒரு தாராளமய-அறிவுசார் நெறிமுறையாகும்.",
    ["TNPSC Group 1 PYQ Pattern", "M. Laxmikanth - Indian Polity"]
))

# Q38 (PYQ Pattern) -> Adjust options so Answer is D
q_data.append(make_q(
    "DPSP_PYQ_038", "Hard", "Direct MCQ",
    "In Bandhua Mukti Morcha v. Union of India (1984), Supreme Court held that Right to Live with Human Dignity (Art 21) derives its life breath from which DPSP Articles guarding workers and children?",
    "பந்துவா முக்தி மோர்ச்சா (1984) வழக்கில், பிரிவு 21-ன் கீழ் கண்ணியமான வாழ்வுரிமை தொழிலாளர் மற்றும் குழந்தைகளைப் பாதுகாக்கும் எந்த அரசு நெறிமுறைகளிலிருந்து உயிர் பெறுகிறது எனத் தீர்ப்பளிக்கப்பட்டது?",
    [
        ("Article 38 & Article 40", "பிரிவு 38 & பிரிவு 40"),
        ("Article 44 & Article 45", "பிரிவு 44 & பிரிவு 45"),
        ("Article 48 & Article 50", "பிரிவு 48 & பிரிவு 50"),
        ("Article 39(e) & Article 39(f)", "பிரிவு 39(e) & பிரிவு 39(f)")
    ],
    "D",
    "In Bandhua Mukti Morcha (1984), Justice P.N. Bhagwati held that Right to Live with Human Dignity under Article 21 derives its life breath from Articles 39(e) and 39(f).",
    "பந்துவா முக்தி மோர்ச்சா (1984) வழக்கில், பிரிவு 21-ன் வாழ்வுரிமை பிரிவு 39(e) மற்றும் 39(f) நெறிமுறைகளிலிருந்தே உயிர் பெறுகிறது என உச்சநீதிமன்றம் தீர்ப்பளித்தது.",
    {
        "A": ("Incorrect.", "தவறு."),
        "B": ("Incorrect.", "தவறு."),
        "C": ("Incorrect.", "தவறு."),
        "D": ("Correct. Articles 39(e) and 39(f) were linked to Article 21 in Bandhua Mukti Morcha case.", "சரி. பிரிவுகள் 39(e) மற்றும் 39(f) பிரிவு 21 உடன் இணைக்கப்பட்டன.")
    },
    "Bandhua Mukti Morcha case dealt with bonded labor abolition.",
    "பந்துவா முக்தி மோர்ச்சா வழக்கு கொத்தடிமை தொழிலாளர் ஒழிப்பைக் கையாண்டது.",
    "Child Labour Act 1986 implements Article 39(e) and 39(f).",
    "குழந்தைகள் தொழிலாளர் சட்டம் 1986 பிரிவுகள் 39(e) மற்றும் 39(f)-ஐ அமல்படுத்துகிறது.",
    ["TNPSC Group 1 PYQ Pattern", "M. Laxmikanth - Indian Polity"]
))

# Q39 (PYQ Pattern) -> Adjust options so Answer is A
q_data.append(make_q(
    "DPSP_PYQ_039", "Easy", "Direct MCQ",
    "Article 36 states that 'the State' in Part IV has the same meaning as defined in which Article of Part III?",
    "பகுதி IV-ல் உள்ள 'அரசு' என்பது பகுதி III-ன் எந்தப் பிரிவில் வரையறுக்கப்பட்டுள்ள அதே பொருளைக் கொண்டது என பிரிவு 36 குறிப்பிடுகிறது?",
    [
        ("Article 12", "பிரிவு 12"),
        ("Article 13", "பிரிவு 13"),
        ("Article 14", "பிரிவு 14"),
        ("Article 32", "பிரிவு 32")
    ],
    "A",
    "Article 36 explicitly states that unless the context otherwise requires, 'the State' in Part IV has the same meaning as in Part III (Article 12).",
    "பிரிவு 36 பகுதி IV-ல் உள்ள 'அரசு' என்பது பகுதி III-ல் (பிரிவு 12) வரையறுக்கப்பட்டுள்ள அதே பொருளைக் கொண்டது எனக் குறிப்பிடுகிறது.",
    {
        "A": ("Correct. Article 36 references Article 12 definition of State.", "சரி. பிரிவு 36 பிரிவு 12-ன் அரசு வரையறையைக் குறிப்பிடுகிறது."),
        "B": ("Incorrect. Article 13 defines laws inconsistent with FR.", "தவறு. பிரிவு 13 சட்டங்கள் செல்லாது என்பதைக் கையாள்கிறது."),
        "C": ("Incorrect. Article 14 guarantees Equality before Law.", "தவறு. பிரிவு 14 சமத்துவ உரிமையைக் கையாள்கிறது."),
        "D": ("Incorrect. Article 32 provides Constitutional Remedies.", "தவறு. பிரிவு 32 அரசியலமைப்பு தீர்வுகளைக் கையாள்கிறது.")
    },
    "State under Article 12 includes GOI, Parliament, State Governments, State Legislatures, and local authorities.",
    "பிரிவு 12-ன் கீழ் அரசு என்பதில் மத்திய, மாநில அரசுகள் மற்றும் உள்ளாட்சி அமைப்புகள் அடங்கும்.",
    "Therefore, DPSP are instructions addressed to all executive and legislative authorities.",
    "எனவே, DPSP அனைத்து நிர்வாக மற்றும் சட்டமன்ற அமைப்புகளுக்குமான அறிவுறுத்தல்களாகும்.",
    ["TNPSC Group 1 PYQ Pattern", "M. Laxmikanth - Indian Polity"]
))

# Q40 (PYQ Pattern) -> Adjust options so Answer is D
q_data.append(make_q(
    "DPSP_PYQ_040", "Easy", "Direct MCQ",
    "Which of the following Directive Principles is classified under **Socialistic Principles** of DPSP?",
    "பின்வரும் அரசு நெறிமுறைப் பிரிவுகளில் எது **சோசலிசக் கோட்பாடுகளின்** கீழ் வகைப்படுத்தப்பட்டுள்ளது?",
    [
        ("Article 40 (Village Panchayats)", "பிரிவு 40 (கிராம பஞ்சாயத்துகள்)"),
        ("Article 44 (Uniform Civil Code)", "பிரிவு 44 (பொது சிவில் சட்டம்)"),
        ("Article 48A (Environment Protection)", "பிரிவு 48A (சுற்றுச்சூழல் பாதுகாப்பு)"),
        ("Article 39A (Free Legal Aid)", "பிரிவு 39A (இலவச சட்ட உதவி)")
    ],
    "D",
    "Article 39A (Equal Justice and Free Legal Aid) is classified under Socialistic Principles aimed at securing socio-economic justice.",
    "பிரிவு 39A (சம நீதி மற்றும் இலவச சட்ட உதவி) சமூக-பொருளாதார நீதியை உறுதி செய்யும் சோசலிசக் கோட்பாட்டின் கீழ் உள்ளது.",
    {
        "A": ("Incorrect. Article 40 is a Gandhian Principle.", "தவறு. பிரிவு 40 ஒரு காந்தியக் கோட்பாடாகும்."),
        "B": ("Incorrect. Article 44 is a Liberal-Intellectual Principle.", "தவறு. பிரிவு 44 ஒரு தாராளமய கோட்பாடாகும்."),
        "C": ("Incorrect. Article 48A is a Liberal-Intellectual Principle.", "தவறு. பிரிவு 48A ஒரு தாராளமய கோட்பாடாகும்."),
        "D": ("Correct. Article 39A is a Socialistic Principle.", "சரி. பிரிவு 39A ஒரு சோசலிசக் கோட்பாடாகும்.")
    },
    "Socialistic Principles: Articles 38, 39, 39A, 41, 42, 43, 43A, 47 (nutrition).",
    "சோசலிசக் கோட்பாடுகள்: பிரிவுகள் 38, 39, 39A, 41, 42, 43, 43A, 47 (ஊட்டச்சத்து).",
    "Socialistic principles aim to build a Welfare State.",
    "சோசலிசக் கோட்பாடுகள் நல அரசை அமைப்பதை நோக்கமாகக் கொண்டுள்ளன.",
    ["TNPSC Group 1 PYQ Pattern", "M. Laxmikanth - Indian Polity"]
))

# Q41 (PYQ Pattern) -> Adjust options so Answer is C
q_data.append(make_q(
    "DPSP_PYQ_041", "Easy", "Direct MCQ",
    "Which of the following Directive Principles is classified under **Liberal-Intellectual Principles** of DPSP?",
    "பின்வரும் அரசு நெறிமுறைப் பிரிவுகளில் எது **தாராளமய-அறிவுசார் கோட்பாடுகளின்** கீழ் வகைப்படுத்தப்பட்டுள்ளது?",
    [
        ("Article 38 (Social Order)", "பிரிவு 38 (சமூக அமைப்பு)"),
        ("Article 43 (Cottage Industries)", "பிரிவு 43 (குடிசைத் தொழில்கள்)"),
        ("Article 44 (Uniform Civil Code)", "பிரிவு 44 (பொது சிவில் சட்டம்)"),
        ("Article 47 (Prohibition of Liquor)", "பிரிவு 47 (மதுவிலக்கு)")
    ],
    "C",
    "Article 44 (Uniform Civil Code) is classified under Liberal-Intellectual Principles.",
    "பிரிவு 44 (பொது சிவில் சட்டம்) தாராளமய-அறிவுசார் கோட்பாடுகளின் கீழ் வகைப்படுத்தப்பட்டுள்ளது.",
    {
        "A": ("Incorrect. Article 38 is Socialistic.", "தவறு. பிரிவு 38 சோசலிசக் கோட்பாடாகும்."),
        "B": ("Incorrect. Article 43 cottage industries is Gandhian.", "தவறு. பிரிவு 43 குடிசைத் தொழில்கள் காந்தியக் கோட்பாடாகும்."),
        "C": ("Correct. Article 44 is Liberal-Intellectual.", "சரி. பிரிவு 44 தாராளமய-அறிவுசார் கோட்பாடாகும்."),
        "D": ("Incorrect. Article 47 liquor prohibition is Gandhian.", "தவறு. பிரிவு 47 மதுவிலக்கு காந்தியக் கோட்பாடாகும்.")
    },
    "Liberal-Intellectual Principles: Articles 44, 45, 48, 48A, 49, 50, 51.",
    "தாராளமய-அறிவுசார் கோட்பாடுகள்: பிரிவுகள் 44, 45, 48, 48A, 49, 50, 51.",
    "These principles reflect modern liberal democratic ideas.",
    "இக்கோட்பாடுகள் நவீன தாராளமய ஜனநாயகக் கருத்துக்களைப் பிரதிபலிக்கின்றன.",
    ["TNPSC Group 1 PYQ Pattern", "M. Laxmikanth - Indian Polity"]
))

# Q42 (PYQ Pattern) -> Adjust options so Answer is C
q_data.append(make_q(
    "DPSP_PYQ_042", "Medium", "Direct MCQ",
    "In Unni Krishnan v. State of Andhra Pradesh (1993), Supreme Court derived Right to Education up to 14 years from Article 45, which paved way for which Constitutional Amendment?",
    "உன்னிகிருஷ்ணன் (1993) வழக்கில் பிரிவு 45-லிருந்து 14 வயது வரையிலான கல்வி உரிமையை உச்சநீதிமன்றம் பெற்றது, இது எந்த அரசியலமைப்பு திருத்தத்திற்கு வழிவகுத்தது?",
    [
        ("42nd Amendment 1976", "42-வது திருத்தம் 1976"),
        ("73rd Amendment 1992", "73-வது திருத்தம் 1992"),
        ("86th Amendment 2002", "86-வது திருத்தம் 2002"),
        ("97th Amendment 2011", "97-வது திருத்தம் 2011")
    ],
    "C",
    "Unni Krishnan judgment (1993) derived Right to Education from Article 45, which inspired the 86th Constitutional Amendment Act 2002 inserting Article 21A.",
    "உன்னிகிருஷ்ணன் வழக்கு (1993) 86-வது திருத்தச் சட்டம் 2002 மூலம் பிரிவு 21A சேர்க்கப்பட நேரடித் தூண்டுதலாக அமைந்தது.",
    {
        "A": ("Incorrect.", "தவறு."),
        "B": ("Incorrect.", "தவறு."),
        "C": ("Correct. Unni Krishnan case paved way for 86th Amendment 2002.", "சரி. உன்னிகிருஷ்ணன் வழக்கு 86-வது திருத்தம் 2002-க்கு வழிவகுத்தது."),
        "D": ("Incorrect.", "தவறு.")
    },
    "86th Amendment 2002 created Article 21A (FR) and modified Article 45 (DPSP).",
    "86-வது திருத்தம் 2002 பிரிவு 21A-ஐ உருவாக்கி பிரிவு 45-ஐ மாற்றியமைத்தது.",
    "Right to Education (RTE) Act was passed in 2009.",
    "இலவச கட்டாயக் கல்வி உரிமைச் சட்டம் 2009-ல் நிறைவேற்றப்பட்டது.",
    ["TNPSC Group 1 PYQ Pattern", "M. Laxmikanth - Indian Polity"]
))

# Q43 (PYQ Pattern) -> Adjust options so Answer is B
q_data.append(make_q(
    "DPSP_PYQ_043", "Medium", "Direct MCQ",
    "The 44th Constitutional Amendment Act 1978 added Article 38(2) to Part IV. Who was the Prime Minister of India at that time?",
    "44-வது திருத்தச் சட்டம் 1978 பிரிவு 38(2)-ஐ பகுதி IV-ல் சேர்த்தது. அப்போது இந்தியாவின் பிரதமராக இருந்தவர் யார்?",
    [
        ("Indira Gandhi", "இந்திரா காந்தி"),
        ("Morarji Desai", "மொரார்ஜி தேசாய்"),
        ("Rajiv Gandhi", "ராஜீவ் காந்தி"),
        ("V.P. Singh", "வி.பி. சிங்")
    ],
    "B",
    "The 44th Constitutional Amendment Act 1978 was enacted by the Janata Party Government headed by Prime Minister Morarji Desai.",
    "44-வது திருத்தச் சட்டம் 1978 பிரதமர் மொரார்ஜி தேசாய் தலைமையிலான ஜனதா கட்சி அரசாங்கத்தால் இயற்றப்பட்டது.",
    {
        "A": ("Incorrect. Indira Gandhi passed 42nd Amendment 1976.", "தவறு. இந்திரா காந்தி 42-வது திருத்தம் 1976-ஐ நிறைவேற்றினார்."),
        "B": ("Correct. Morarji Desai was PM during 44th Amendment 1978.", "சரி. 44-வது திருத்தம் 1978-ன் போது மொரார்ஜி தேசாய் பிரதமராக இருந்தார்."),
        "C": ("Incorrect. Rajiv Gandhi enacted 52nd Anti-Defection Act 1985.", "தவறு. ராஜீவ் காந்தி 52-வது திருத்தத்தை நிறைவேற்றினார்."),
        "D": ("Incorrect. V.P. Singh implemented Mandal Commission in 1990.", "தவறு. வி.பி. சிங் மண்டல் பரிந்துரைகளை அமல்படுத்தினார்.")
    },
    "42nd Amendment (1976) = Indira Gandhi Govt. 44th Amendment (1978) = Morarji Desai Govt.",
    "42-வது திருத்தம் (1976) = இந்திரா காந்தி அரசு. 44-வது திருத்தம் (1978) = மொரார்ஜி தேசாய் அரசு.",
    "44th Amendment reversed several provisions of 42nd Amendment.",
    "44-வது திருத்தம் 42-வது திருத்தத்தின் பல விதிகளை மாற்றியமைத்தது.",
    ["TNPSC Group 1 PYQ Pattern", "M. Laxmikanth - Indian Polity"]
))

# Q44 (PYQ Pattern) -> Adjust options so Answer is B
q_data.append(make_q(
    "DPSP_PYQ_044", "Hard", "Direct MCQ",
    "Sanjeev Coke Manufacturing Co. v. Bharat Coking Coal Ltd (1983) reaffirmed the constitutionality of Article 31C protecting laws implementing which DPSP directives?",
    "சஞ்சீவ் கோக் (1983) வழக்கின் தீர்ப்பு எந்த அரசு நெறிமுறைகளை அமல்படுத்தும் சட்டங்களைப் பாதுகாக்கும் பிரிவு 31C-ன் செல்லுபடித் தன்மையை மீண்டும் உறுதிப்படுத்தியது?",
    [
        ("Article 38(1) & (2)", "பிரிவு 38(1) & (2)"),
        ("Article 39(b) & 39(c)", "பிரிவு 39(b) & 39(c)"),
        ("Article 40 & 44", "பிரிவு 40 & 44"),
        ("Article 48A & 51", "பிரிவு 48A & 51")
    ],
    "B",
    "In Sanjeev Coke (1983), the Supreme Court reaffirmed that Article 31C validly protects laws enacted to implement Article 39(b) and 39(c) directives from Articles 14 and 19.",
    "சஞ்சீவ் கோக் (1983) வழக்கில் பிரிவு 39(b) மற்றும் 39(c)-ஐ அமல்படுத்தும் சட்டங்களுக்கு பிரிவு 31C அளிக்கும் பாதுகாப்பை உச்சநீதிமன்றம் மீண்டும் உறுதி செய்தது.",
    {
        "A": ("Incorrect.", "தவறு."),
        "B": ("Correct. Sanjeev Coke (1983) upheld Article 31C immunity for Article 39(b) & (c).", "சரி. சஞ்சீவ் கோக் வழக்கு பிரிவு 39(b) & (c)-க்கான பிரிவு 31C பாதுகாப்பை உறுதி செய்தது."),
        "C": ("Incorrect.", "தவறு."),
        "D": ("Incorrect.", "தவறு.")
    },
    "Article 39(b) deals with distribution of material resources.",
    "பிரிவு 39(b) பருப்பொருள் வளங்களின் விநியோகத்தைக் கையாள்கிறது.",
    "Article 39(c) deals with preventing concentration of wealth.",
    "பிரிவு 39(c) செல்வம் குவிவதைத் தடுப்பதைக் கையாள்கிறது.",
    ["TNPSC Group 1 PYQ Pattern", "M. Laxmikanth - Indian Polity"]
))

# Q45 (PYQ Pattern) -> Adjust options so Answer is D
q_data.append(make_q(
    "DPSP_PYQ_045", "Easy", "Direct MCQ",
    "Which Article of DPSP directs the State to secure right to work, to education, and to public assistance in cases of unemployment, old age, sickness and disablement?",
    "வேலையின்மை, முதியோர் நிலை, நோய் மற்றும் ஊனம் ஆகியவற்றில் வேலை உரிமை, கல்வி உரிமை மற்றும் பொது உதவியை உறுதி செய்யப் பணிக்கும் DPSP பிரிவு எது?",
    [
        ("Article 39", "பிரிவு 39"),
        ("Article 42", "பிரிவு 42"),
        ("Article 43", "பிரிவு 43"),
        ("Article 41", "பிரிவு 41")
    ],
    "D",
    "Article 41 directs the State to make effective provision for securing the right to work, to education and to public assistance in cases of unemployment, old age, sickness and disablement.",
    "பிரிவு 41 வேலையின்மை, முதியோர் நிலை, நோய் ஆகியவற்றில் வேலை உரிமை, கல்வி உரிமை மற்றும் பொது உதவியை உறுதி செய்யப் பணிக்கிறது.",
    {
        "A": ("Incorrect. Article 39 deals with specific social policy principles.", "தவறு. பிரிவு 39 கொள்கையின் குறிப்பிட்ட நெறிமுறைகளைக் கையாள்கிறது."),
        "B": ("Incorrect. Article 42 deals with maternity relief.", "தவறு. பிரிவு 42 மகப்பேறு உதவியைக் கையாள்கிறது."),
        "C": ("Incorrect. Article 43 deals with living wage.", "தவறு. பிரிவு 43 வாழ்வாதார ஊதியத்தைக் கையாள்கிறது."),
        "D": ("Correct. Article 41 covers right to work, education, and public assistance.", "சரி. பிரிவு 41 வேலை உரிமை, கல்வி மற்றும் பொது உதவியைக் கையாள்கிறது.")
    },
    "National Social Assistance Programme (NSAP) implements Article 41.",
    "தேசிய சமூக உதவித் திட்டம் (NSAP) பிரிவு 41-ஐ அமல்படுத்துகிறது.",
    "Article 41 is a Socialistic Principle.",
    "பிரிவு 41 ஒரு சோசலிசக் கோட்பாடாகும்.",
    ["TNPSC Group 1 PYQ Pattern", "M. Laxmikanth - Indian Polity"]
))

# Q46 (PYQ Pattern) -> Adjust options so Answer is C
q_data.append(make_q(
    "DPSP_PYQ_046", "Easy", "Direct MCQ",
    "Which Article of Part IV instructs the State to endeavour to organise agriculture and animal husbandry on modern and scientific lines?",
    "வேளாண்மை மற்றும் கால்நடை வளர்ப்பை நவீன அறிவியல் முறையில் அமைக்க முயல வேண்டும் என அரசுக்கு அறிவுறுத்தும் பகுதி IV-ன் பிரிவு எது?",
    [
        ("Article 46", "பிரிவு 46"),
        ("Article 47", "பிரிவு 47"),
        ("Article 48", "பிரிவு 48"),
        ("Article 48A", "பிரிவு 48A")
    ],
    "C",
    "Article 48 directs the State to endeavour to organise agriculture and animal husbandry on modern and scientific lines.",
    "பிரிவு 48 வேளாண்மை மற்றும் கால்நடை வளர்ப்பை நவீன அறிவியல் முறையில் அமைக்க முயல வேண்டும் என அரசைப் பணிக்கிறது.",
    {
        "A": ("Incorrect. Article 46 deals with SC/ST interests.", "தவறு. பிரிவு 46 பட்டியல் சாதியினர் நலன்களைக் கையாள்கிறது."),
        "B": ("Incorrect. Article 47 deals with public health and prohibition.", "தவறு. பிரிவு 47 பொது சுகாதாரத்தைக் கையாள்கிறது."),
        "C": ("Correct. Article 48 explicitly covers agriculture and animal husbandry.", "சரி. பிரிவு 48 வேளாண்மை மற்றும் கால்நடை வளர்ப்பைக் கையாள்கிறது."),
        "D": ("Incorrect. Article 48A deals with environment protection.", "தவறு. பிரிவு 48A சுற்றுச்சூழல் பாதுகாப்பைக் கையாள்கிறது.")
    },
    "Article 48 also directs prohibiting slaughter of cows, calves, and draft cattle.",
    "பிரிவு 48 பசுக்கள் மற்றும் கன்றுகளை வதை செய்வதைத் தடுக்கவும் பணிக்கிறது.",
    "Article 48 contains both Liberal (modern agriculture) and Gandhian (cow prohibition) elements.",
    "பிரிவு 48 தாராளமய மற்றும் காந்திய கூறுகள் இரண்டையும் கொண்டுள்ளது.",
    ["TNPSC Group 1 PYQ Pattern", "M. Laxmikanth - Indian Polity"]
))

# Q47 (PYQ Pattern) -> Adjust options so Answer is A
q_data.append(make_q(
    "DPSP_PYQ_047", "Medium", "Direct MCQ",
    "Sapru Committee Report (1945) recommended dividing individual rights into two categories: justiciable and non-justiciable. Who was the Chairman of this Committee?",
    "உரிமைகளை நீதிமன்றத்தால் அமல்படுத்தக்கூடியவை மற்றும் அமல்படுத்த முடியாதவை என இரண்டு பிரிவுகளாகப் பிரிக்க 1945-ல் பரிந்துரைத்த குழுவின் தலைவர் யார்?",
    [
        ("Sir Tej Bahadur Sapru", "சர் தேஜ் பகதூர் சப்ரு"),
        ("Motilal Nehru", "மோதிலால் நேரு"),
        ("Sir B.N. Rau", "சர் பி.என். ராவ்"),
        ("K.M. Munshi", "கே.எம். முன்ஷி")
    ],
    "A",
    "Sir Tej Bahadur Sapru Committee Report (1945) recommended dividing fundamental rights into justiciable (Part III) and non-justiciable (Part IV) categories.",
    "சர் தேஜ் பகதூர் சப்ரு குழு (1945) உரிமைகளை அமல்படுத்தக்கூடியவை (பகுதி III) மற்றும் அமல்படுத்த முடியாதவை (பகுதி IV) எனப் பிரிக்க பரிந்துரைத்தது.",
    {
        "A": ("Correct. Sir Tej Bahadur Sapru headed the 1945 Non-Party Conference Committee.", "சரி. சர் தேஜ் பகதூர் சப்ரு 1945 குழுவின் தலைவராக இருந்தார்."),
        "B": ("Incorrect. Motilal Nehru drafted Nehru Report 1928.", "தவறு. மோதிலால் நேரு 1928 நேரு அறிக்கையைத் தயாரித்தார்."),
        "C": ("Incorrect. B.N. Rau was Constitutional Advisor.", "தவறு. பி.என். ராவ் அரசியலமைப்பு ஆலோசகராக இருந்தார்."),
        "D": ("Incorrect. K.M. Munshi was a member of Drafting Committee.", "தவறு. கே.எம். முன்ஷி வரைவுக் குழுவின் உறுப்பினராக இருந்தார்.")
    },
    "Sapru Committee Report 1945 laid the foundation for dividing rights into Part III and Part IV.",
    "1945 சப்ரு குழு அறிக்கை உரிமைகளை பகுதி III மற்றும் பகுதி IV எனப் பிரிப்பதற்கு அடித்தளம் அமைத்தது.",
    "Irish Constitution 1937 also influenced this non-justiciable directive approach.",
    "1937 அயர்லாந்து அரசியலமைப்பும் இந்த அணுகுமுறையை பாதித்தது.",
    ["TNPSC Group 1 PYQ Pattern", "M. Laxmikanth - Indian Polity"]
))

# Q48 (PYQ Pattern) -> Adjust options so Answer is B
q_data.append(make_q(
    "DPSP_PYQ_048", "Hard", "Direct MCQ",
    "Under Article 39(a), the State is directed to ensure adequate means of livelihood. Which landmark Supreme Court case derived Right to Livelihood from Article 21 read with Article 39(a)?",
    "பிரிவு 39(a)-ன் கீழ் போதுமான வாழ்வாதாரத்தை உறுதி செய்ய அரசு பணிக்கப்படுகிறது. பிரிவு 21-ஐ பிரிவு 39(a) உடன் சேர்த்துப் படித்து 'வாழ்வாதார உரிமையை' வெளிப்படுத்திய வழக்கு எது?",
    [
        ("Champakam Dorairajan v. State of Madras (1951)", "செம்பகம் துரைராஜன் வழக்கு (1951)"),
        ("Olga Tellis v. Bombay Municipal Corporation (1985)", "ஓல்கா டெல்லிஸ் எதிராக பம்பாய் மாநகராட்சி (1985)"),
        ("Randhir Singh v. Union of India (1982)", "ரந்தீர் சிங் வழக்கு (1982)"),
        ("Minerva Mills v. Union of India (1980)", "மினர்வா மில்ஸ் வழக்கு (1980)")
    ],
    "B",
    "In Olga Tellis v. Bombay Municipal Corporation (1985), the Supreme Court ruled that the Right to Life under Article 21 includes the Right to Livelihood, deriving support from Article 39(a) and Article 41.",
    "ஓல்கா டெல்லிஸ் (1985) வழக்கில், பிரிவு 21-ன் வாழ்வுரிமையில் வாழ்வாதார உரிமையும் அடங்கும் என பிரிவு 39(a) மற்றும் 41-ன் உதவியுடன் உச்சநீதிமன்றம் தீர்ப்பளித்தது.",
    {
        "A": ("Incorrect.", "தவறு."),
        "B": ("Correct. Olga Tellis (1985) case derived Right to Livelihood from Article 21 read with Article 39(a).", "சரி. ஓல்கா டெல்லிஸ் (1985) வழக்கு வாழ்வாதார உரிமையை பிரிவு 21 உடன் பிரிவு 39(a)-ஐ இணைத்துப் படித்து அளித்தது."),
        "C": ("Incorrect. Randhir Singh (1982) derived Equal Pay for Equal Work.", "தவறு. ரந்தீர் சிங் சம ஊதிய உரிமையைப் பெற்றது."),
        "D": ("Incorrect. Minerva Mills (1980) established Basic Structure balance.", "தவறு. மினர்வா மில்ஸ் அடிப்படை அமைப்பை நிறுவியது.")
    },
    "Olga Tellis case dealt with pavement dwellers in Mumbai.",
    "ஓல்கா டெல்லிஸ் வழக்கு மும்பை நடைபாதைவாசிகளின் உரிமையைக் கையாண்டது.",
    "Right to livelihood cannot be deprived without just, fair and reasonable procedure.",
    "நியாயமான நடைமுறையின்றி வாழ்வாதார உரிமையைப் பறிக்க முடியாது.",
    ["TNPSC Group 1 PYQ Pattern", "M. Laxmikanth - Indian Polity"]
))

# Q49 (PYQ Pattern) -> Adjust options so Answer is C
q_data.append(make_q(
    "DPSP_PYQ_049", "Easy", "Direct MCQ",
    "Which Directive Principle instructs the State to take steps to separate the judiciary from the executive in the public services of the State?",
    "மாநிலத்தின் பொதுப்பணிகளில் நிர்வாகத்திலிருந்து நீதித்துறையைப் பிரிக்க நடவடிக்கை எடுக்க வேண்டும் என அரசுக்கு அறிவுறுத்தும் நெறிமுறைப் பிரிவு எது?",
    [
        ("Article 48", "பிரிவு 48"),
        ("Article 49", "பிரிவு 49"),
        ("Article 50", "பிரிவு 50"),
        ("Article 51", "பிரிவு 51")
    ],
    "C",
    "Article 50 states: 'The State shall take steps to separate the judiciary from the executive in the public services of the State.'",
    "பிரிவு 50: 'மாநிலத்தின் பொதுப்பணிகளில் நிர்வாகத்திலிருந்து நீதித்துறையைப் பிரிக்க அரசு நடவடிக்கை எடுக்க வேண்டும்' எனக் கூறுகிறது.",
    {
        "A": ("Incorrect. Article 48 deals with agriculture.", "தவறு. பிரிவு 48 வேளாண்மையைக் கையாள்கிறது."),
        "B": ("Incorrect. Article 49 deals with monuments.", "தவறு. பிரிவு 49 வரலாற்றுச் சின்னங்களைக் கையாள்கிறது."),
        "C": ("Correct. Article 50 deals with separation of judiciary.", "சரி. பிரிவு 50 நீதித்துறை பிரிப்பைக் கையாள்கிறது."),
        "D": ("Incorrect. Article 51 deals with international peace.", "தவறு. பிரிவு 51 சர்வதேச அமைதியைக் கையாள்கிறது.")
    },
    "Article 50 protects judicial independence and rule of law.",
    "பிரிவு 50 நீதித்துறை சுதந்திரத்தையும் சட்டத்தின் ஆட்சியையும் பாதுகாக்கிறது.",
    "CrPC 1973 implemented Article 50.",
    "CrPC 1973 பிரிவு 50-ஐ அமல்படுத்தியது.",
    ["TNPSC Group 1 PYQ Pattern", "M. Laxmikanth - Indian Polity"]
))

# Q50 (PYQ Pattern) -> Adjust options so Answer is D
q_data.append(make_q(
    "DPSP_PYQ_050", "Hard", "Statement Based",
    "Consider the following statements regarding Constitutional Amendments modifying Part IV DPSP:\n\n1. 42nd Amendment Act 1976 added Articles 39A, 43A, and 48A.\n2. 44th Amendment Act 1978 added Article 38(2).\n3. 86th Amendment Act 2002 substituted Article 45.\n4. 97th Amendment Act 2011 added Article 43B.\n\nWhich of the above statements are correct?",
    "பகுதி IV DPSP-ஐ மாற்றியமைத்த அரசியலமைப்பு திருத்தங்கள் பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n\n1. 42-வது திருத்தச் சட்டம் 1976 பிரிவுகள் 39A, 43A மற்றும் 48A-ஐச் சேர்த்தது.\n2. 44-வது திருத்தச் சட்டம் 1978 பிரிவு 38(2)-ஐச் சேர்த்தது.\n3. 86-வது திருத்தச் சட்டம் 2002 பிரிவு 45-ஐ மாற்றியமைத்தது.\n4. 97-வது திருத்தச் சட்டம் 2011 பிரிவு 43B-ஐச் சேர்த்தது.\n\nமேற்கண்ட கூற்றுகளில் எவை சரியானவை?",
    [
        ("1 and 2 only", "1 மற்றும் 2 மட்டும்"),
        ("2 and 3 only", "2 மற்றும் 3 மட்டும்"),
        ("1, 3 and 4 only", "1, 3 மற்றும் 4 மட்டும்"),
        ("1, 2, 3 and 4", "1, 2, 3 மற்றும் 4")
    ],
    "D",
    "All four statements are correct. Part IV DPSP was modified by four major Constitutional Amendment Acts: 42nd (1976 - Arts 39(f), 39A, 43A, 48A), 44th (1978 - Art 38(2)), 86th (2002 - Art 45), and 97th (2011 - Art 43B).",
    "நான்கு கூற்றுகளும் சரியானவை. பகுதி IV DPSP நான்கு முக்கிய திருத்தங்களால் மாற்றியமைக்கப்பட்டது: 42-வது (1976), 44-வது (1978), 86-வது (2002) மற்றும் 97-வது (2011).",
    {
        "A": ("Incorrect. Statements 3 and 4 are also correct.", "தவறு. கூற்றுகள் 3 மற்றும் 4-ம் சரியானவை."),
        "B": ("Incorrect. Statements 1 and 4 are also correct.", "தவறு. கூற்றுகள் 1 மற்றும் 4-ம் சரியானவை."),
        "C": ("Incorrect. Statement 2 is also correct.", "தவறு. கூற்று 2-ம் சரியானது."),
        "D": ("Correct. All four statements accurately summarize the amendment history of Part IV DPSP.", "சரி. நான்கு கூற்றுகளும் DPSP-ன் திருத்த வரலாற்றை துல்லியமாகச் சுருக்குகின்றன.")
    },
    "42nd (1976) = 39(f), 39A, 43A, 48A. 44th (1978) = 38(2). 86th (2002) = 45. 97th (2011) = 43B.",
    "42-வது (1976) = 39(f), 39A, 43A, 48A. 44-வது (1978) = 38(2). 86-வது (2002) = 45. 97-வது (2011) = 43B.",
    "Only these four Constitutional Amendments modified Part IV of the Indian Constitution.",
    "இந்த நான்கு அரசியலமைப்பு திருத்தங்கள் மட்டுமே இந்திய அரசியலமைப்பின் பகுதி IV-ஐ மாற்றியமைத்தன.",
    ["TNPSC Group 1 PYQ Pattern", "M. Laxmikanth - Indian Polity"]
))

out_path_1 = 'data/questions/polity/directive_principles_pyq.json'
out_path_2 = 'data/questions/polity/directive_principles_pyq_practice.json'

os.makedirs(os.path.dirname(out_path_1), exist_ok=True)

with open(out_path_1, 'w', encoding='utf-8') as f:
    json.dump(q_data, f, ensure_ascii=False, indent=2)

with open(out_path_2, 'w', encoding='utf-8') as f:
    json.dump(q_data, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {len(q_data)} questions in {out_path_1} and {out_path_2}.")
