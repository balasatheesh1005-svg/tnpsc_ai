def make_pyq_q(q_id, q_type, q_en, q_ta, opts_en, opts_ta, correct_ans, exp_en, exp_ta,
               wno_a_en, wno_a_ta, wno_b_en, wno_b_ta, wno_c_en, wno_c_ta, wno_d_en, wno_d_ta,
               tip_en, tip_ta, rev_en, rev_ta, difficulty, bloom, est_time, tags,
               list_1=None, list_2=None, events=None):
    opts = [{"id": chr(65+i), "en": opts_en[i], "ta": opts_ta[i]} for i in range(4)]
    
    q_obj = {
        "id": q_id,
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": difficulty,
        "question_type": q_type,
        "question": {"en": q_en, "ta": q_ta},
        "options": opts,
        "correct_answer": correct_ans,
        "explanation": {"en": exp_en, "ta": exp_ta},
        "why_not_others": {
            "A": {"en": wno_a_en, "ta": wno_a_ta},
            "B": {"en": wno_b_en, "ta": wno_b_ta},
            "C": {"en": wno_c_en, "ta": wno_c_ta},
            "D": {"en": wno_d_en, "ta": wno_d_ta}
        },
        "tnpsc_tip": {"en": tip_en, "ta": tip_ta},
        "revision_fact": {"en": rev_en, "ta": rev_ta},
        "source_reference": ["TNPSC Group 1 PYQ Pattern", "M. Laxmikanth - Indian Polity", "NCERT Class 11"],
        "bloom_level": bloom,
        "estimated_time_sec": est_time,
        "pyq_similarity": "High",
        "tags": tags,
        "question_en": q_en,
        "question_ta": q_ta,
        "options_en": opts_en,
        "options_ta": opts_ta,
        "answer": correct_ans.lower(),
        "explanation_en": exp_en,
        "explanation_ta": exp_ta
    }
    if list_1:
        q_obj["list_1"] = list_1
    if list_2:
        q_obj["list_2"] = list_2
    if events:
        q_obj["events"] = events
    return q_obj

questions = []

# MIC_PYQ_001 (Direct PYQ)
questions.append(make_pyq_q(
    "MIC_PYQ_001", "Direct MCQ",
    "Who among the following first put forward the idea of a Constituent Assembly for India in 1934?",
    "1934 இல் முதன்முதலில் இந்தியாவிற்கான அரசியலமைப்பு நிர்ணய அவைக் கருத்தை முன்வைத்தவர் யார்?",
    ["M.N. Roy", "Jawaharlal Nehru", "Mahatma Gandhi", "Subhash Chandra Bose"],
    ["எம்.என். ராய்", "ஜவகர்லால் நேரு", "மகாத்மா காந்தி", "சுபாஷ் சந்திர போஸ்"],
    "A",
    "M.N. Roy, a pioneer of the communist movement in India and advocate of radical democracy, was the first to put forward the idea of a Constituent Assembly for India in 1934.",
    "இந்தியாவில் கம்யூனிச இயக்கத்தின் முன்னோடியான எம்.என். ராய், 1934 இல் முதன்முதலில் இந்தியாவிற்கான அரசியலமைப்பு நிர்ணய அவைக் கருத்தை முன்வைத்தார்.",
    "Correct. M.N. Roy proposed the idea in 1934.", "சரி. எம்.என். ராய் 1934 இல் இந்த யோசனையை முன்வைத்தார்.",
    "Incorrect. Nehru declared the adult franchise demand in 1938.", "தவறு. நேரு 1938 இல் வயதுவந்தோர் வாக்குரிமைக் கோரிக்கையை அறிவித்தார்.",
    "Incorrect. Gandhiji demanded Swaraj in 1922.", "தவறு. காந்தியடிகள் 1922 இல் சுயராஜ்யத்தைக் கோரினார்.",
    "Incorrect. Bose was leader of Forward Bloc/INA.", "தவறு. போஸ் ஃபார்வர்டு பிளாக்/ஐஎன்ஏ தலைவராவார்.",
    "TNPSC Trap: M.N. Roy (1934) -> INC Official Demand (1935) -> Nehru Demand (1938).",
    "TNPSC பொறி: எம்.என். ராய் (1934) -> காங்கிரஸ் கோரிக்கை (1935) -> நேரு கோரிக்கை (1938).",
    "M.N. Roy was also the founder of the Mexican Communist Party and Radical Democratic Party.",
    "எம்.என். ராய் மெக்சிகன் கம்யூனிஸ்ட் கட்சியையும் தீவிர ஜனநாயகக் கட்சியையும் நிறுவியவர்.",
    "Easy", "Remember", 45, ["Polity", "Making of Indian Constitution", "Demand for Constituent Assembly", "M.N. Roy"]
))

# MIC_PYQ_002 (Direct PYQ)
questions.append(make_pyq_q(
    "MIC_PYQ_002", "Direct MCQ",
    "Under which scheme/plan was the Constituent Assembly of India constituted in November 1946?",
    "நவம்பர் 1946 இல் எந்தத் திட்டம்/திட்டத்தின் கீழ் இந்திய அரசியலமைப்பு நிர்ணய அவை உருவாக்கப்பட்டது?",
    ["Cabinet Mission Plan", "Cripps Mission", "Mountbatten Plan", "Wavell Plan"],
    ["கேபினட் தூதுக்குழு திட்டம்", "கிரிப்ஸ் திட்டம்", "மவுண்ட்பேட்டன் திட்டம்", "வேவல் திட்டம்"],
    "A",
    "The Constituent Assembly of India was constituted in November 1946 under the scheme formulated by the Cabinet Mission Plan of 1946.",
    "1946 ஆம் ஆண்டின் கேபினட் தூதுக்குழு திட்டத்தின் கீழ் நவம்பர் 1946 இல் இந்திய அரசியலமைப்பு நிர்ணய அவை அமைக்கப்பட்டது.",
    "Correct. Cabinet Mission Plan formulated the scheme for Constituent Assembly.", "சரி. கேபினட் தூதுக்குழு திட்டம் அவைக்கான திட்டத்தை வகுத்தது.",
    "Incorrect. Cripps Mission (1942) proposals were rejected.", "தவறு. கிரிப்ஸ் திட்டம் (1942) நிராகரிக்கப்பட்டது.",
    "Incorrect. Mountbatten Plan (1947) dealt with partition.", "தவறு. மவுண்ட்பேட்டன் திட்டம் (1947) பிரிவினையைப் பற்றியது.",
    "Incorrect. Wavell Plan was proposed at Shimla Conference 1945.", "தவறு. வேவல் திட்டம் 1945 சிம்லா மாநாட்டில் முன்வைக்கப்பட்டது.",
    "TNPSC Trap: Cabinet Mission arrived in March 1946; announced plan on May 16, 1946; Assembly constituted in Nov 1946.",
    "TNPSC பொறி: கேபினட் தூதுக்குழு மார்ச் 1946 இல் வந்தது; மே 16, 1946 இல் திட்டத்தை அறிவித்தது; நவம்பர் 1946 இல் அவை அமைக்கப்பட்டது.",
    "Cabinet Mission members: Lord Pethick-Lawrence, Sir Stafford Cripps, A.V. Alexander.",
    "கேபினட் தூதுக்குழு உறுப்பினர்கள்: பெதிக்-லாரன்ஸ், கிரிப்ஸ், ஏ.வி. அலெக்சாண்டர்.",
    "Easy", "Remember", 45, ["Polity", "Making of Indian Constitution", "Cabinet Mission Plan", "Constituent Assembly Formation"]
))

# MIC_PYQ_003 (Direct PYQ)
questions.append(make_pyq_q(
    "MIC_PYQ_003", "Direct MCQ",
    "Who among the following was elected as the Temporary President of the Constituent Assembly in its first meeting on December 9, 1946?",
    "டிசம்பர் 9, 1946 அன்று நடந்த முதல் கூட்டத்தில் அரசியலமைப்பு நிர்ணய அவையின் தற்காலிகத் தலைவராகத் தேர்ந்தெடுக்கப்பட்டவர் யார்?",
    ["Dr. Sachchidananda Sinha", "Dr. Rajendra Prasad", "H.C. Mookherjee", "Dr. B.R. Ambedkar"],
    ["டாக்டர் சச்சிதானந்த சின்ஹா", "டாக்டர் ராஜேந்திர பிரசாத்", "எச்.சி. முகர்ஜி", "டாக்டர் பி.ஆர். அம்பேத்கர்"],
    "A",
    "Following the French practice, Dr. Sachchidananda Sinha, the oldest member of the Assembly, was elected as the Temporary President for the first meeting on December 9, 1946.",
    "பிரெஞ்சு நடைமுறையைப் பின்பற்றி, அவையின் மூத்த உறுப்பினரான டாக்டர் சச்சிதானந்த சின்ஹா டிசம்பர் 9, 1946 அன்று தற்காலிகத் தலைவராகத் தேர்ந்தெடுக்கப்பட்டார்.",
    "Correct. Dr. Sachchidananda Sinha was Temporary President.", "சரி. டாக்டர் சச்சிதானந்த சின்ஹா தற்காலிகத் தலைவர்.",
    "Incorrect. Dr. Rajendra Prasad was elected Permanent President on Dec 11, 1946.", "தவறு. ராஜேந்திர பிரசாத் டிசம்பர் 11 இல் நிரந்தரத் தலைவரானார்.",
    "Incorrect. H.C. Mookherjee was elected Vice-President.", "தவறு. எச்.சி. முகர்ஜி துணைத் தலைவரானார்.",
    "Incorrect. Ambedkar was Chairman of Drafting Committee.", "தவறு. அம்பேத்கர் வரைவுக் குழுத் தலைவராவார்.",
    "TNPSC Trap: Temporary President = Dr. Sachchidananda Sinha (Dec 9). Permanent President = Dr. Rajendra Prasad (Dec 11). Vice-Presidents = H.C. Mookherjee and V.T. Krishnamachari.",
    "TNPSC பொறி: தற்காலிகத் தலைவர் = சச்சிதானந்த சின்ஹா (டிச 9). நிரந்தரத் தலைவர் = ராஜேந்திர பிரசாத் (டிச 11). துணைத் தலைவர்கள் = எச்.சி. முகர்ஜி & வி.டி. கிருஷ்ணமாச்சாரி.",
    "Selecting the oldest member as temporary chairman is a traditional French parliamentary practice.",
    "மூத்த உறுப்பினரைத் தற்காலிகத் தலைவராகத் தேர்ந்தெடுப்பது பிரெஞ்சு நாடாளுமன்ற நடைமுறையாகும்.",
    "Easy", "Remember", 45, ["Polity", "Making of Indian Constitution", "Temporary President", "First Meeting"]
))

# MIC_PYQ_004 (Direct PYQ)
questions.append(make_pyq_q(
    "MIC_PYQ_004", "Direct MCQ",
    "On which date was the historic 'Objectives Resolution' moved in the Constituent Assembly by Pandit Jawaharlal Nehru?",
    "அரசியலமைப்பு நிர்ணய அவையில் பண்டித ஜவகர்லால் நேருவால் வரலாற்றுச் சிறப்புமிக்க 'குறிக்கோள்கள் தீர்மானம்' எந்தத் தேதியில் முன்மொழியப்பட்டது?",
    ["December 13, 1946", "December 9, 1946", "January 22, 1947", "November 26, 1949"],
    ["டிசம்பர் 13, 1946", "டிசம்பர் 9, 1946", "ஜனவரி 22, 1947", "நவம்பர் 26, 1949"],
    "A",
    "Pandit Jawaharlal Nehru moved the historic 'Objectives Resolution' in the Constituent Assembly on December 13, 1946. It laid down the fundamentals and philosophy of the constitutional structure.",
    "பண்டித ஜவகர்லால் நேரு டிசம்பர் 13, 1946 அன்று அரசியலமைப்பு நிர்ணய அவையில் வரலாற்றுச் சிறப்புமிக்க 'குறிக்கோள்கள் தீர்மானத்தை' முன்மொழிந்தார்.",
    "Correct. Objectives Resolution was moved on Dec 13, 1946.", "சரி. குறிக்கோள்கள் தீர்மானம் டிசம்பர் 13, 1946 இல் முன்மொழியப்பட்டது.",
    "Incorrect. Dec 9, 1946 was the date of the First Meeting.", "தவறு. டிசம்பர் 9, 1946 முதல் கூட்டத் தேதியாகும்.",
    "Incorrect. Jan 22, 1947 was the date when Objectives Resolution was unanimously ADOPTED.", "தவறு. ஜனவரி 22, 1947 தீர்மானம் ஒருமனதாக ஏற்கப்பட்ட தேதியாகும்.",
    "Incorrect. Nov 26, 1949 was the date of Constitution adoption.", "தவறு. நவம்பர் 26, 1949 அரசியலமைப்பு ஏற்கப்பட்ட தேதியாகும்.",
    "TNPSC Trap: Moved on Dec 13, 1946; Adopted on Jan 22, 1947. Do NOT confuse the two dates!",
    "TNPSC பொறி: முன்மொழியப்பட்ட நாள் = டிசம்பர் 13, 1946; ஏற்றுக்கொள்ளப்பட்ட நாள் = ஜனவரி 22, 1947.",
    "The modified version of the Objectives Resolution forms the Preamble of the present Constitution.",
    "குறிக்கோள்கள் தீர்மானத்தின் திருத்தப்பட்ட வடிவமே தற்போதைய அரசியலமைப்பின் முகப்புரையாகும்.",
    "Easy", "Remember", 45, ["Polity", "Making of Indian Constitution", "Objectives Resolution", "Jawaharlal Nehru"]
))

# MIC_PYQ_005 (Direct PYQ)
questions.append(make_pyq_q(
    "MIC_PYQ_005", "Direct MCQ",
    "Who among the following served as the Constitutional Adviser (Legal Adviser) to the Constituent Assembly?",
    "அரசியலமைப்பு நிர்ணய அவையின் அரசியலமைப்பு ஆலோசகராக (சட்ட ஆலோசகர்) பணியாற்றியவர் யார்?",
    ["Sir B.N. Rau", "Dr. B.R. Ambedkar", "K.M. Munshi", "Sardar Vallabhbhai Patel"],
    ["சர் பி.என். ராவ்", "டாக்டர் பி.ஆர். அம்பேத்கர்", "கே.எம். முன்ஷி", "சர்தார் வல்லபாய் படேல்"],
    "A",
    "Sir B.N. Rau (Benegal Narsing Rau) was appointed as the Constitutional Adviser to the Constituent Assembly. He prepared the initial draft of the Constitution containing 243 Articles.",
    "சர் பி.என். ராவ் அரசியலமைப்பு அவையின் அரசியலமைப்பு ஆலோசகராக நியமிக்கப்பட்டார். அவர் 243 சரத்துகளைக் கொண்ட தொடக்க வரைவைத் தயாரித்தார்.",
    "Correct. Sir B.N. Rau was Constitutional Adviser.", "சரி. சர் பி.என். ராவ் அரசியலமைப்பு ஆலோசகர்.",
    "Incorrect. Dr. Ambedkar was Chairman of Drafting Committee.", "தவறு. அம்பேத்கர் வரைவுக் குழுத் தலைவர்.",
    "Incorrect. K.M. Munshi was member of Drafting Committee & Chair of Order of Business Committee.", "தவறு. கே.எம். முன்ஷி வரைவுக் குழு உறுப்பினர்.",
    "Incorrect. Patel was Chair of Provincial Constitution & Advisory Committees.", "தவறு. படேல் மாகாண அரசியலமைப்பு மற்றும் ஆலோசனைக் குழுத் தலைவர்.",
    "TNPSC Trap: B.N. Rau was Constitutional Adviser (NOT an elected member of CA); Ambedkar was Drafting Committee Chairman.",
    "TNPSC பொறி: பி.என். ராவ் அரசியலமைப்பு ஆலோசகர் (அவையின் தேர்ந்தெடுக்கப்பட்ட உறுப்பினர் அல்ல); அம்பேத்கர் வரைவுக் குழுத் தலைவர்.",
    "B.N. Rau also drafted the Constitution of Burma (Myanmar) in 1947.",
    "பி.என். ராவ் 1947 இல் பர்மாவின் (மியான்மர்) அரசியலமைப்பையும் வரைந்தார்.",
    "Easy", "Remember", 45, ["Polity", "Making of Indian Constitution", "B. N. Rau", "Constitutional Adviser"]
))

# MIC_PYQ_006 (Direct PYQ)
questions.append(make_pyq_q(
    "MIC_PYQ_006", "Direct MCQ",
    "How many members were there in the Drafting Committee of the Indian Constitution, including its Chairman Dr. B.R. Ambedkar?",
    "அதன் தலைவர் டாக்டர் பி.ஆர். அம்பேத்கர் உட்பட இந்திய அரசியலமைப்பு வரைவுக் குழுவில் மொத்தம் எத்தனை உறுப்பினர்கள் இருந்தனர்?",
    ["7 Members", "9 Members", "11 Members", "15 Members"],
    ["7 உறுப்பினர்கள்", "9 உறுப்பினர்கள்", "11 உறுப்பினர்கள்", "15 உறுப்பினர்கள்"],
    "A",
    "The Drafting Committee set up on August 29, 1947 consisted of 7 members: Dr. B.R. Ambedkar (Chairman), N. Gopalaswamy Ayyangar, Alladi Krishnaswamy Ayyar, Dr. K.M. Munshi, Syed Mohammad Saadullah, N. Madhava Rau (replaced B.L. Mitter), and T.T. Krishnamachari (replaced D.P. Khaitan).",
    "ஆகஸ்ட் 29, 1947 இல் அமைக்கப்பட்ட வரைவுக் குழு டாக்டர் பி.ஆர். அம்பேத்கர் உட்பட 7 உறுப்பினர்களைக் கொண்டிருந்தது.",
    "Correct. Drafting Committee had 7 members.", "சரி. வரைவுக் குழு 7 உறுப்பினர்களைக் கொண்டிருந்தது.",
    "Incorrect. Not 9 members.", "தவறு. 9 உறுப்பினர்கள் அல்ல.",
    "Incorrect. Not 11 members.", "தவறு. 11 உறுப்பினர்கள் அல்ல.",
    "Incorrect. Not 15 members.", "தவறு. 15 உறுப்பினர்கள் அல்ல.",
    "TNPSC Trap: Total members = 7 (Chairman + 6 members). B.L. Mitter was replaced by N. Madhava Rau; D.P. Khaitan was replaced by T.T. Krishnamachari.",
    "TNPSC பொறி: மொத்த உறுப்பினர்கள் = 7 (தலைவர் + 6 உறுப்பினர்கள்). மிட்டருக்குப் பதிலாக மாதவ ராவ்; கைத்தானுக்குப் பதிலாக டி.டி. கிருஷ்ணமாச்சாரி.",
    "The Drafting Committee took less than 6 months to prepare its first draft.",
    "வரைவுக் குழு தனது முதல் வரைவைத் தயாரிக்க 6 மாதங்களுக்கும் குறைவான காலத்தையே எடுத்துக்கொண்டது.",
    "Easy", "Remember", 45, ["Polity", "Making of Indian Constitution", "Drafting Committee", "Ambedkar"]
))

# MIC_PYQ_007 (Direct PYQ)
questions.append(make_pyq_q(
    "MIC_PYQ_007", "Direct MCQ",
    "On which date was the National Flag of India officially adopted by the Constituent Assembly?",
    "இந்திய தேசியக் கொடி அரசியலமைப்பு அவையால் எந்தத் தேதியில் அதிகாரப்பூர்வமாக ஏற்றுக்கொள்ளப்பட்டது?",
    ["July 22, 1947", "August 15, 1947", "January 24, 1950", "January 26, 1950"],
    ["ஜூலை 22, 1947", "ஆகஸ்ட் 15, 1947", "ஜனவரி 24, 1950", "ஜனவரி 26, 1950"],
    "A",
    "The Constituent Assembly adopted the National Flag of India on July 22, 1947. It was designed by Pingali Venkayya.",
    "அரசியலமைப்பு நிர்ணய அவை ஜூலை 22, 1947 அன்று இந்திய தேசியக் கொடியை ஏற்றுக்கொண்டது. இதை பிங்கலி வெங்கையா வடிவமைத்தார்.",
    "Correct. July 22, 1947 was National Flag adoption date.", "சரி. ஜூலை 22, 1947 தேசியக் கொடி ஏற்கப்பட்ட தேதியாகும்.",
    "Incorrect. Aug 15, 1947 was Independence Day.", "தவறு. ஆகஸ்ட் 15, 1947 சுதந்திர தினமாகும்.",
    "Incorrect. Jan 24, 1950 was adoption of National Anthem & Song.", "தவறு. ஜனவரி 24, 1950 தேசிய கீதம் & பாடல் ஏற்கப்பட்ட நாளாகும்.",
    "Incorrect. Jan 26, 1950 was Republic Day & Emblem adoption.", "தவறு. ஜனவரி 26, 1950 குடியரசு தினமாகும்.",
    "TNPSC Trap: Flag Adoption = July 22, 1947. Anthem & Song Adoption = Jan 24, 1950. State Emblem = Jan 26, 1950.",
    "TNPSC பொறி: கொடி ஏற்பு = ஜூலை 22, 1947. கீதம் & பாடல் ஏற்பு = ஜனவரி 24, 1950. அரசு முத்திரை = ஜனவரி 26, 1950.",
    "The ratio of width to length of the National Flag is 2:3 (Length to width 3:2).",
    "தேசியக் கொடியின் நீள அகல விகிதம் 3:2 ஆகும்.",
    "Easy", "Remember", 45, ["Polity", "Making of Indian Constitution", "National Flag adoption"]
))

# MIC_PYQ_008 (Direct PYQ)
questions.append(make_pyq_q(
    "MIC_PYQ_008", "Direct MCQ",
    "Following the partition of India under the Mountbatten Plan, what was the reduced total strength of the Constituent Assembly of India on December 31, 1947?",
    "மவுண்ட்பேட்டன் திட்டத்தின் கீழ் இந்தியா பிரிக்கப்பட்டதைத் தொடர்ந்து, டிசம்பர் 31, 1947 அன்று இந்திய அரசியலமைப்பு அவையின் குறைக்கப்பட்ட மொத்த உறுப்பினர் எண்ணிக்கை என்ன?",
    ["299 Members", "389 Members", "292 Members", "229 Members"],
    ["299 உறுப்பினர்கள்", "389 உறுப்பினர்கள்", "292 உறுப்பினர்கள்", "229 உறுப்பினர்கள்"],
    "A",
    "Due to partition, the total strength of the Constituent Assembly came down to 299 on December 31, 1947 (from original 389). Provincial seats were reduced from 292 to 229, and Princely State seats from 93 to 70.",
    "பிரிவினை காரணமாக, டிசம்பர் 31, 1947 அன்று அவையின் மொத்த எண்ணிக்கை 299 ஆகக் குறைந்தது (அசல் 389 இலிருந்து). மாகாண இடங்கள் 229 ஆகவும் சமஸ்தான இடங்கள் 70 ஆகவும் குறைந்தன.",
    "Correct. Reduced strength was 299 members.", "சரி. குறைக்கப்பட்ட எண்ணிக்கை 299 உறுப்பினர்கள்.",
    "Incorrect. 389 was the pre-partition strength.", "தவறு. 389 பிரிவினைக்கு முந்தைய எண்ணிக்கை.",
    "Incorrect. 292 was pre-partition Provincial strength.", "தவறு. 292 பிரிவினைக்கு முந்தைய மாகாண எண்ணிக்கை.",
    "Incorrect. 229 was post-partition Provincial strength only.", "தவறு. 229 பிரிவினைக்குப் பிந்தைய மாகாண எண்ணிக்கை மட்டுமே.",
    "TNPSC Trap: Post-partition Total = 299. Post-partition Indian Provinces = 229. Post-partition Princely States = 70.",
    "TNPSC பொறி: பிரிவினைக்குப் பின் மொத்தம் = 299. மாகாணங்கள் = 229. சமஸ்தானங்கள் = 70.",
    "Out of 299 members, 284 members were actually present and signed the Constitution on January 24, 1950.",
    "299 உறுப்பினர்களில் 284 உறுப்பினர்கள் ஜனவரி 24, 1950 அன்று கையெழுத்திட்டனர்.",
    "Medium", "Remember", 50, ["Polity", "Making of Indian Constitution", "Partition impact", "Reduction from 389 to 299 members"]
))

# MIC_PYQ_009 (Direct PYQ)
questions.append(make_pyq_q(
    "MIC_PYQ_009", "Direct MCQ",
    "How long did the Constituent Assembly take to complete the historic task of drafting the Constitution of India?",
    "இந்திய அரசியலமைப்பை வரைவு செய்யும் வரலாற்றுப் பணியை முடிக்க அரசியலமைப்பு நிர்ணய அவை எவ்வளவு காலம் எடுத்துக்கொண்டது?",
    ["2 Years, 11 Months, and 18 Days", "3 Years, 10 Months, and 12 Days", "2 Years, 9 Months, and 15 Days", "1 Year, 11 Months, and 18 Days"],
    ["2 ஆண்டுகள், 11 மாதங்கள் மற்றும் 18 நாட்கள்", "3 ஆண்டுகள், 10 மாதங்கள் மற்றும் 12 நாட்கள்", "2 ஆண்டுகள், 9 மாதங்கள் மற்றும் 15 நாட்கள்", "1 ஆண்டு, 11 மாதங்கள் மற்றும் 18 நாட்கள்"],
    "A",
    "The Constituent Assembly took exactly 2 years, 11 months, and 18 days (covering 11 sessions spanning 165 days of sittings) to complete the drafting of the Constitution.",
    "அரசியலமைப்பு அவை 2 ஆண்டுகள், 11 மாதங்கள் மற்றும் 18 நாட்கள் (11 அமர்வுகள், 165 நாட்கள்) எடுத்துக்கொண்டு அரசியலமைப்பை உருவாக்கியது.",
    "Correct. 2 Years, 11 Months, 18 Days.", "சரி. 2 ஆண்டுகள், 11 மாதங்கள், 18 நாட்கள்.",
    "Incorrect. Not 3 years.", "தவறு. 3 ஆண்டுகள் அல்ல.",
    "Incorrect. Not 9 months.", "தவறு. 9 மாதங்கள் அல்ல.",
    "Incorrect. Not 1 year.", "தவறு. 1 ஆண்டு அல்ல.",
    "TNPSC Trap: 2 Yrs 11 Mos 18 Days total duration; held 11 sessions; scrutinized constitutions of 60 countries; total cost ₹64 lakh.",
    "TNPSC பொறி: 2 ஆண்டுகள் 11 மாதங்கள் 18 நாட்கள் காலம்; 11 அமர்வுகள்; 60 நாடுகளின் அரசியலமைப்புகள் ஆய்வு; மொத்த செலவு ₹64 லட்சம்.",
    "The Constitution makers considered drafts of about 60 countries.",
    "அரசியலமைப்பு உருவாக்குநர்கள் சுமார் 60 நாடுகளின் வரைவுகளை ஆராய்ந்தனர்.",
    "Easy", "Remember", 45, ["Polity", "Making of Indian Constitution", "Constitutional Facts", "Interesting Constitutional Facts"]
))

# MIC_PYQ_010 (Direct PYQ)
questions.append(make_pyq_q(
    "MIC_PYQ_010", "Direct MCQ",
    "Who chaired the Assembly sittings when the Constituent Assembly met as a Legislative Body (Provisional Parliament)?",
    "அரசியலமைப்பு அவை சட்டமன்றமாக (தற்காலிக நாடாளுமன்றம்) கூடிய போது அவை அமர்வுகளுக்குத் தலைமை தாங்கியவர் யார்?",
    ["G.V. Mavlankar", "Dr. Rajendra Prasad", "Dr. B.R. Ambedkar", "Ananthasayanam Ayyangar"],
    ["ஜி.வி. மாவ்லங்கார்", "டாக்டர் ராஜேந்திர பிரசாத்", "டாக்டர் பி.ஆர். அம்பேத்கர்", "அனந்தசயனம் அய்யங்கார்"],
    "A",
    "When the Constituent Assembly met as a Legislative Body, it was chaired by G.V. Mavlankar (who was elected Speaker on Nov 17, 1947). When it met as a Constituent Body, it was chaired by Dr. Rajendra Prasad.",
    "அவை சட்டமன்றமாகக் கூடிய போது ஜி.வி. மாவ்லங்கார் தலைமை தாங்கினார். அரசியலமைப்பு அவையாகக் கூடிய போது டாக்டர் ராஜேந்திர பிரசாத் தலைமை தாங்கினார்.",
    "Correct. G.V. Mavlankar chaired legislative sittings.", "சரி. ஜி.வி. மாவ்லங்கார் சட்டமன்றக் கூட்டங்களுக்குத் தலைமை தாங்கினார்.",
    "Incorrect. Dr. Rajendra Prasad chaired constituent sittings.", "தவறு. ராஜேந்திர பிரசாத் அரசியலமைப்பு அவைக் கூட்டங்களுக்குத் தலைமை தாங்கினார்.",
    "Incorrect. Ambedkar was Chairman of Drafting Committee.", "தவறு. அம்பேத்கர் வரைவுக் குழுத் தலைவர்.",
    "Incorrect. Ananthasayanam Ayyangar succeeded Mavlankar as Speaker later.", "தவறு. அனந்தசயனம் அய்யங்கார் பின்னர் சபாநாயகரானார்.",
    "TNPSC Trap: Constituent Body Chair = Dr. Rajendra Prasad. Legislative Body Chair = G.V. Mavlankar. Dual functions began Nov 17, 1947.",
    "TNPSC பொறி: அரசியலமைப்பு அவையின் தலைவர் = ராஜேந்திர பிரசாத். சட்டமன்றத் தலைவர் = ஜி.வி. மாவ்லங்கார். இரட்டைப் பணி தொடங்கியது = நவம்பர் 17, 1947.",
    "G.V. Mavlankar became the 1st Speaker of the Lok Sabha in 1952.",
    "ஜி.வி. மாவ்லங்கார் 1952 இல் மக்களவையின் 1வது சபாநாயகரானார்.",
    "Medium", "Remember", 50, ["Polity", "Making of Indian Constitution", "Constituent Assembly as Legislature", "G. V. Mavlankar"]
))

# MIC_PYQ_011 (Direct PYQ)
questions.append(make_pyq_q(
    "MIC_PYQ_011", "Direct MCQ",
    "Who among the following chaired the Provincial Constitution Committee of the Constituent Assembly?",
    "அரசியலமைப்பு அவையின் மாகாண அரசியலமைப்புக்குழுவின் தலைவராக இருந்தவர் யார்?",
    ["Sardar Vallabhbhai Patel", "Jawaharlal Nehru", "Dr. B.R. Ambedkar", "Dr. Rajendra Prasad"],
    ["சர்தார் வல்லபாய் படேல்", "ஜவகர்லால் நேரு", "டாக்டர் பி.ஆர். அம்பேத்கர்", "டாக்டர் ராஜேந்திர பிரசாத்"],
    "A",
    "Sardar Vallabhbhai Patel was the Chairman of the Provincial Constitution Committee as well as the Advisory Committee on Fundamental Rights, Minorities and Tribal Areas.",
    "சர்தார் வல்லபாய் படேல் மாகாண அரசியலமைப்புக்குழு மற்றும் அடிப்படை உரிமைகள் ஆலோசனைக் குழு ஆகியவற்றின் தலைவராக இருந்தார்.",
    "Correct. Sardar Patel chaired Provincial Constitution Committee.", "சரி. சர்தார் படேல் மாகாண அரசியலமைப்புக்குழு தலைவர்.",
    "Incorrect. Nehru chaired Union Powers & Union Constitution Committees.", "தவறு. நேரு மத்திய அதிகாரக் குழுத் தலைவர்.",
    "Incorrect. Ambedkar chaired Drafting Committee.", "தவறு. அம்பேத்கர் வரைவுக் குழுத் தலைவர்.",
    "Incorrect. Rajendra Prasad chaired Steering & Rules Committees.", "தவறு. ராஜேந்திர பிரசாத் வழிநடத்தல் குழுத் தலைவர்.",
    "TNPSC Trap: Provincial Constitution Committee = Sardar Patel. Union Constitution Committee = Jawaharlal Nehru.",
    "TNPSC பொறி: மாகாண அரசியலமைப்புக்குழு = சர்தார் படேல். மத்திய அரசியலமைப்புக்குழு = ஜவகர்லால் நேரு.",
    "Sardar Patel also led the integration of 565 Princely States into the Indian Union.",
    "சர்தார் படேல் 565 சுதேச சமஸ்தானங்களை இந்திய ஒன்றியத்துடன் இணைப்பதை வழிநடத்தினார்.",
    "Easy", "Remember", 45, ["Polity", "Making of Indian Constitution", "Provincial Constitution Committee", "Important Committees"]
))

# MIC_PYQ_012 (Direct PYQ)
questions.append(make_pyq_q(
    "MIC_PYQ_012", "Direct MCQ",
    "Who among the following was the only Muslim woman member of the Constituent Assembly of India?",
    "இந்திய அரசியலமைப்பு நிர்ணய அவையில் இருந்த ஒரே முஸ்லிம் பெண் உறுப்பினர் யார்?",
    ["Begum Aizaz Rasul", "Sarojini Naidu", "Sucheta Kripalani", "Rajkumari Amrit Kaur"],
    ["பேகம் ஐசாஸ் ரசூல்", "சரோஜினி நாயுடு", "சுசேதா கிருபளானி", "ராஜ்குமாரி அம்ரித் கவுர்"],
    "A",
    "Begum Aizaz Rasul was the only Muslim woman member in the 299-member Constituent Assembly. She strongly opposed separate electorates during minority debates.",
    "299 உறுப்பினர்களைக் கொண்ட அரசியலமைப்பு அவையில் இருந்த ஒரே முஸ்லிம் பெண் உறுப்பினர் பேகம் ஐசாஸ் ரசூல் ஆவார்.",
    "Correct. Begum Aizaz Rasul was sole Muslim woman member.", "சரி. பேகம் ஐசாஸ் ரசூல் ஒரே முஸ்லிம் பெண் உறுப்பினர்.",
    "Incorrect. Sarojini Naidu was a prominent woman member (later UP Governor).", "தவறு. சரோஜினி நாயுடு முக்கிய பெண் உறுப்பினர்.",
    "Incorrect. Sucheta Kripalani became 1st woman Chief Minister of UP.", "தவறு. சுசேதா கிருபளானி 1வது பெண் முதல்வர்.",
    "Incorrect. Rajkumari Amrit Kaur became 1st Health Minister.", "தவறு. ராஜ்குமாரி அம்ரித் கவுர் 1வது சுகாதார அமைச்சர்.",
    "TNPSC Trap: Total women members in CA = 15. Only Muslim woman member = Begum Aizaz Rasul. Only Dalit woman member = Dakshayani Velayudhan.",
    "TNPSC பொறி: அவையில் மொத்தம் பெண் உறுப்பினர்கள் = 15. ஒரே முஸ்லிம் பெண் உறுப்பினர் = பேகம் ஐசாஸ் ரசூல். ஒரே தலித் பெண் உறுப்பினர் = தாக்ஷாயணி வேலாயுதன்.",
    "Begum Aizaz Rasul wrote an autobiography titled 'From Pavilion to PM's House'.",
    "பேகம் ஐசாஸ் ரசூல் 'From Pavilion to PM's House' என்ற சுயசரிதையை எழுதினார்.",
    "Medium", "Remember", 50, ["Polity", "Making of Indian Constitution", "Women's Representation", "Begum Aizaz Rasul"]
))

# MIC_PYQ_013 (Direct PYQ)
questions.append(make_pyq_q(
    "MIC_PYQ_013", "Direct MCQ",
    "Who was the Calligrapher who wrote the original English manuscript of the Constitution of India in a flowing italic style?",
    "இந்திய அரசியலமைப்பின் அசல் ஆங்கிலக் கையெழுத்துப் பிரதியை சாய்ந்த எழுத்து வடிவில் கையால் எழுதிய கையெழுத்துக் கலைஞர் யார்?",
    ["Prem Behari Narain Raizada", "Nandalal Bose", "Vasant Krishnan Vaidya", "Beohar Rammanohar Sinha"],
    ["பிரேம் பிஹாரி நரேன் ரைசாதா", "நந்தலால் போஸ்", "வசந்த் கிருஷ்ண வைத்யா", "பியோஹர் ராம்மனோஹர் சின்ஹா"],
    "A",
    "Prem Behari Narain Raizada was the calligrapher of the original Indian Constitution. He handwrote the entire English text in a flowing italic style without charging any fee.",
    "பிரேம் பிஹாரி நரேன் ரைசாதா அசல் இந்திய அரசியலமைப்பின் கையெழுத்துக் கலைஞர் ஆவார். அவர் எவ்விதக் கட்டணமும் பெறாமல் அசல் பிரதியை எழுதினார்.",
    "Correct. Prem Behari Narain Raizada was English calligrapher.", "சரி. பிரேம் பிஹாரி நரேன் ரைசாதா ஆங்கிலக் கையெழுத்துக் கலைஞர்.",
    "Incorrect. Nandalal Bose led Shantiniketan artists who decorated pages.", "தவறு. நந்தலால் போஸ் பக்கங்களை அலங்கரித்த ஓவியர் குழுத் தலைவர்.",
    "Incorrect. Vasant Krishnan Vaidya calligraphed the Hindi version.", "தவறு. வசந்த் கிருஷ்ண வைத்யா இந்திப் பிரதியை எழுதினார்.",
    "Incorrect. Beohar Rammanohar Sinha decorated the Preamble page.", "தவறு. பியோஹர் ராம்மனோஹர் சின்ஹா முகப்புரைப் பக்கத்தை வரைந்தார்.",
    "TNPSC Trap: English Calligrapher = Prem Behari Narain Raizada. Hindi Calligrapher = Vasant Krishnan Vaidya. Page Art Leader = Nandalal Bose.",
    "TNPSC பொறி: ஆங்கிலக் கையெழுத்து = பிரேம் பிஹாரி நரேன் ரைசாதா. இந்திக் கையெழுத்து = வசந்த் கிருஷ்ண வைத்யா. ஓவியக் குழுத் தலைவர் = நந்தலால் போஸ்.",
    "Raizada requested only that his name be inscribed on every page and his grandfather's name on the last page.",
    "ரைசாதா ஒவ்வொரு பக்கத்திலும் தனது பெயரையும் கடைசி பக்கத்தில் தனது தாத்தாவின் பெயரையும் எழுத மட்டுமே கோரினார்.",
    "Medium", "Remember", 50, ["Polity", "Making of Indian Constitution", "Prem Behari Narain Raizada", "Handwritten Constitution"]
))

# MIC_PYQ_014 (Direct PYQ)
questions.append(make_pyq_q(
    "MIC_PYQ_014", "Direct MCQ",
    "Which animal was adopted as the official Symbol (Seal) of the Constituent Assembly of India?",
    "இந்திய அரசியலமைப்பு நிர்ணய அவையின் அதிகாரப்பூர்வ சின்னமான (முத்திரை) ஏற்றுக்கொள்ளப்பட்ட விலங்கு எது?",
    ["Elephant", "Tiger", "Lion", "Peacock"],
    ["யானை", "புலி", "சிங்கம்", "மயில்"],
    "A",
    "The Elephant was adopted as the official symbol (seal) of the Constituent Assembly of India, representing vast strength, wisdom, and the subcontinent's unity.",
    "யானை இந்திய அரசியலமைப்பு நிர்ணய அவையின் அதிகாரப்பூர்வ சின்னமாக (முத்திரை) ஏற்றுக்கொள்ளப்பட்டது.",
    "Correct. Elephant was Assembly seal.", "சரி. யானை அவையின் முத்திரையாகும்.",
    "Incorrect. Tiger is National Animal (1973).", "தவறு. புலி தேசிய விலங்கு (1973).",
    "Incorrect. Sarnath Lion Capital is State Emblem of India (1950).", "தவறு. சாரநாத் சிங்கம் இந்திய அரசு முத்திரையாகும்.",
    "Incorrect. Peacock is National Bird (1963).", "தவறு. மயில் தேசியப் பறவையாகும்.",
    "TNPSC Trap: Assembly Seal = Elephant. State Emblem of India = Sarnath Lion Capital.",
    "TNPSC பொறி: அவையின் முத்திரை = யானை. இந்திய அரசு முத்திரை = சாரநாத் சிங்கத் தூண்.",
    "H.V.R. Iengar was the Secretary to the Constituent Assembly.",
    "எச்.வி.ஆர். ஐயங்கார் அரசியலமைப்பு அவையின் செயலாளராக இருந்தார்.",
    "Easy", "Remember", 45, ["Polity", "Making of Indian Constitution", "Elephant Assembly Emblem", "Interesting Constitutional Facts"]
))

# MIC_PYQ_015 (Direct PYQ)
questions.append(make_pyq_q(
    "MIC_PYQ_015", "Direct MCQ",
    "Which Article of the Constitution of India explicitly repealed the Government of India Act, 1935 and the Indian Independence Act, 1947?",
    "இந்திய அரசியலமைப்பின் எந்தச் சரத்து 1935 இந்திய அரசுச் சட்டம் மற்றும் 1947 இந்திய சுதந்திரச் சட்டத்தை வெளிப்படையாக ரத்து செய்தது?",
    ["Article 395", "Article 394", "Article 393", "Article 368"],
    ["சரத்து 395", "சரத்து 394", "சரத்து 393", "சரத்து 368"],
    "A",
    "Article 395 of the Constitution explicitly repealed the Government of India Act 1935 and the Indian Independence Act 1947, together with all enactments amending or supplementing them, EXCEPT the Abolition of Privy Council Jurisdiction Act 1949.",
    "அரசியலமைப்பின் சரத்து 395 1935 இந்திய அரசுச் சட்டம் மற்றும் 1947 சுதந்திரச் சட்டத்தை வெளிப்படையாக ரத்து செய்தது.",
    "Correct. Article 395 performed legal repeals.", "சரி. சரத்து 395 சட்டபூர்வ ரத்துகளைச் செய்தது.",
    "Incorrect. Article 394 contains enforcement date provisions.", "தவறு. சரத்து 394 நடைமுறைத் தேதியை உடையது.",
    "Incorrect. Article 393 contains the Short Title ('Constitution of India').", "தவறு. சரத்து 393 குறுகிய தலைப்பை உடையது.",
    "Incorrect. Article 368 deals with Constitutional amendments.", "தவறு. சரத்து 368 அரசியலமைப்புத் திருத்தத்தைப் பற்றியது.",
    "TNPSC Trap: Article 393 = Short Title ('Constitution of India'). Article 394 = Commencement. Article 395 = Repeals.",
    "TNPSC பொறி: சரத்து 393 = குறுகிய தலைப்பு. சரத்து 394 = நடைமுறைப்படுத்தல். சரத்து 395 = சட்ட ரத்துகள்.",
    "The Abolition of Privy Council Jurisdiction Act 1949 was specifically saved from repeal under Article 395.",
    "1949 பிரிவி கவுன்சில் ஒழிப்புச் சட்டம் சரத்து 395 இன் கீழ் ரத்து செய்யப்படாமல் பாதுகாக்கப்பட்டது.",
    "Medium", "Remember", 50, ["Polity", "Making of Indian Constitution", "Article 395", "Enforcement of Constitution"]
))
