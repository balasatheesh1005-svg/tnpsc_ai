# Grand Test Constitutional Amendments - Part 2 (Q26 to Q50)
# Target Answer Key Distribution: 7 A, 6 B, 6 C, 6 D = 25 Total

part2_questions = []

def add_p2(q_id, difficulty, q_type, q_en, q_ta,
           opt_a_en, opt_a_ta, opt_b_en, opt_b_ta, opt_c_en, opt_c_ta, opt_d_en, opt_d_ta,
           correct_ans, exp_en, exp_ta,
           why_a_en, why_a_ta, why_b_en, why_b_ta, why_c_en, why_c_ta, why_d_en, why_d_ta,
           tip_en, tip_ta, fact_en, fact_ta, bloom, pyq_sim, tags):
    part2_questions.append({
        "id": q_id,
        "subject": "Polity",
        "topic": "Constitutional Amendments",
        "difficulty": difficulty,
        "question_type": q_type,
        "question": {"en": q_en, "ta": q_ta},
        "options": [
            {"id": "A", "en": opt_a_en, "ta": opt_a_ta},
            {"id": "B", "en": opt_b_en, "ta": opt_b_ta},
            {"id": "C", "en": opt_c_en, "ta": opt_c_ta},
            {"id": "D", "en": opt_d_en, "ta": opt_d_ta}
        ],
        "correct_answer": correct_ans,
        "explanation": {"en": exp_en, "ta": exp_ta},
        "why_not_others": {
            "A": {"en": why_a_en, "ta": why_a_ta},
            "B": {"en": why_b_en, "ta": why_b_ta},
            "C": {"en": why_c_en, "ta": why_c_ta},
            "D": {"en": why_d_en, "ta": why_d_ta}
        },
        "tnpsc_tip": {"en": tip_en, "ta": tip_ta},
        "revision_fact": {"en": fact_en, "ta": fact_ta},
        "source_reference": [
            "M. Laxmikanth — Indian Polity (Constitutional Amendments)",
            "TNPSC Nova AI Notes — Constitutional Amendments (Part 2)",
            "NCERT Class XI - Indian Constitution at Work"
        ],
        "bloom_level": bloom,
        "estimated_time_sec": 60,
        "pyq_similarity": pyq_sim,
        "tags": tags
    })

# Q26 - Ans: A
add_p2(
    "polity_amendments_gt_026", "Medium", "statement",
    "Consider the following statements regarding the 1st Constitutional Amendment Act, 1951:\n1. It added the Ninth Schedule to protect land reforms and agrarian legislation from judicial review.\n2. It added three more grounds of reasonable restriction on freedom of speech and expression: public order, friendly relations with foreign states, and incitement to an offence.\nWhich of the statements given above is/are correct?",
    "1951-ஆம் ஆண்டின் 1-வது அரசியலமைப்பு திருத்தச் சட்டம் குறித்த பின்வரும் கூற்றுகளை ஆராய்க:\n1. நிலசீர்திருத்தங்கள் மற்றும் விவசாயச் சட்டங்களை நீதிமன்ற ஆய்விலிருந்து பாதுகாக்க இது ஒன்பதாவது அட்டவணையைச் சேர்த்தது.\n2. பேச்சு மற்றும் கருத்துச் சுதந்திரத்திற்கான நியாயமான கட்டுப்பாடுகளின் கீழ் பொது அமைதி, வெளிநாட்டு நாடுகளுடனான நட்பு உறவுகள், குற்றத்திற்குத் தூண்டுதல் ஆகிய மூன்று புதிய காரணங்களை இது சேர்த்தது.\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானது?",
    "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
    "1 only", "1 மட்டுமே",
    "2 only", "2 மட்டுமே",
    "Neither 1 nor 2", "1 அல்லது 2 இரண்டும் இல்லை",
    "A",
    "📚 Core Explanation:\nBoth statements 1 and 2 are CORRECT regarding the 1st Constitutional Amendment Act, 1951 (enacted by the Provisional Parliament under Nehru):\n1. Added 9th Schedule along with Article 31A and 31B to protect land reforms.\n2. Added three new grounds of restriction to Article 19(2): Public order, friendly relations with foreign states, and incitement to an offence.",
    "📚 முதன்மை விளக்கம்:\n1-வது திருத்தச் சட்டம் (1951) தொடர்பான இரு கூற்றுகளும் சரியானவை:\n1. நிலசீர்திருத்தங்களைப் பாதுகாக்க 9-வது அட்டவணையைச் சேர்த்தது.\n2. சரத்து 19(2)-ன் கீழ் பொது அமைதி, வெளிநாட்டு நட்பு உறவுகள், குற்றத்திற்குத் தூண்டுதல் ஆகிய 3 புதிய கட்டுப்பாட்டுக் காரணங்களைச் சேர்த்தது.",
    "Option A is correct because both statements 1 and 2 are true.", "விருப்பம் A சரியானது.",
    "Option B is incomplete.", "விருப்பம் B அரைகுறையானது.",
    "Option C is incomplete.", "விருப்பம் C அரைகுறையானது.",
    "Option D is incorrect.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: The 1st Amendment was passed by the Provisional Parliament before the first general elections.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: முதல் பொதுத் தேர்தலுக்கு முன்பே தற்காலிக நாடாளுமன்றத்தால் 1-வது திருத்தம் நிறைவேற்றப்பட்டது.",
    "📖 Revision Fact: 1st Amendment Act also empowered state to make special provisions for advancement of socially and educationally backward classes (Art 15(4)).",
    "📖 திருத்தல் செய்தி: பிற்படுத்தப்பட்ட வகுப்பினருக்கான சிறப்பு விதிகளை உருவாக்க 1-வது திருத்தம் அதிகாரம் அளித்தது (சரத்து 15(4)).",
    "Understand", "High", ["1st Amendment", "Ninth Schedule", "Article 19"]
)

# Q27 - Ans: A
add_p2(
    "polity_amendments_gt_027", "Medium", "single_choice",
    "Which Constitutional Amendment Act provided for the establishment of a Common High Court for two or more States and Union Territories?",
    "இரண்டு அல்லது அதற்கு மேற்பட்ட மாநிலங்கள் மற்றும் ஒன்றிய பிரதேசங்களுக்கு ஒரு பொதுவான உயர்நீதிமன்றத்தை நிறுவ வழிவகை செய்த அரசியலமைப்பு திருத்தச் சட்டம் எது?",
    "7th Constitutional Amendment Act, 1956", "7-வது அரசியலமைப்பு திருத்தச் சட்டம், 1956",
    "15th Constitutional Amendment Act, 1963", "15-வது அரசியலமைப்பு திருத்தச் சட்டம், 1963",
    "42nd Constitutional Amendment Act, 1976", "42-வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
    "44th Constitutional Amendment Act, 1978", "44-வது அரசியலமைப்பு திருத்தச் சட்டம், 1978",
    "A",
    "📚 Core Explanation:\nThe 7th Constitutional Amendment Act, 1956 implemented the State Reorganisation Plan. Among other key changes, it provided for the establishment of a Common High Court for two or more States (Article 231) and appointment of additional and acting judges.",
    "📚 முதன்மை விளக்கம்:\n1956-ஆம் ஆண்டின் 7-வது அரசியலமைப்பு திருத்தச் சட்டம் மாநில மறுசீரமைப்புத் திட்டத்தை அமல்படுத்தியது. இது இரண்டு அல்லது அதற்கு மேற்பட்ட மாநிலங்களுக்கு ஒரு பொதுவான உயர்நீதிமன்றத்தை (சரத்து 231) நிறுவ வழிவகை செய்தது.",
    "Option A is correct; 7th Amendment provided for common High Courts.", "விருப்பம் A சரியானது.",
    "Option B is incorrect; 15th Amendment raised High Court judges retirement age from 60 to 62.", "விருப்பம் B தவறானது.",
    "Option C is incorrect; 42nd Amendment introduced tribunals.", "விருப்பம் C தவறானது.",
    "Option D is incorrect; 44th Amendment restored High Court powers post-emergency.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: 7th Amendment abolished the classification of states into Part A, B, C, D and created 14 States & 6 UTs.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: 7-வது திருத்தம் மாநிலங்களின் Part A, B, C, D பிரிவுகளை நீக்கி 14 மாநிலங்கள் & 6 ஒன்றிய பிரதேசங்களை உருவாக்கியது.",
    "📖 Revision Fact: Example of Common High Courts: Punjab & Haryana High Court, Bombay High Court, Gauhati High Court.",
    "📖 திருத்தல் செய்தி: பொதுவான உயர்நீதிமன்றங்கள்: பஞ்சாப் & அரியானா, பம்பாய், கவுகாத்தி உயர்நீதிமன்றங்கள்.",
    "Remember", "High", ["7th Amendment", "Common High Court", "State Reorganisation"]
)

# Q28 - Ans: B
add_p2(
    "polity_amendments_gt_028", "Hard", "single_choice",
    "Which article was inserted into the Constitution by the 25th Amendment Act, 1971 to protect laws implementing Directive Principles specified in Article 39(b) and 39(c) from being challenged under Articles 14, 19, or 31?",
    "சரத்து 39(b) மற்றும் 39(c)-ல் குறிப்பிடப்பட்டுள்ள அரசு நெறிமுறையுறுத்தும் கோட்பாடுகளை அமல்படுத்தும் சட்டங்களை சரத்து 14, 19 அல்லது 31-ன் கீழ் சவால் செய்வதிலிருந்து பாதுகாக்க 25-வது திருத்தச் சட்டத்தால் அரசியலமைப்பில் சேர்க்கப்பட்ட சரத்து எது?",
    "Article 31A", "சரத்து 31A",
    "Article 31C", "சரத்து 31C",
    "Article 31B", "சரத்து 31B",
    "Article 300A", "சரத்து 300A",
    "B",
    "📚 Core Explanation:\nThe 25th Constitutional Amendment Act, 1971 added Article 31C to the Constitution. It provided that no law giving effect to the Directive Principles contained in Article 39(b) and 39(c) shall be declared void on the ground of inconsistency with Fundamental Rights under Article 14, 19, or 31.",
    "📚 முதன்மை விளக்கம்:\n1971-ஆம் ஆண்டின் 25-வது அரசியலமைப்பு திருத்தச் சட்டம் சரத்து 31C-ஐச் சேர்த்தது. இது சரத்து 39(b) மற்றும் 39(c)-ல் உள்ள அரசு நெறிமுறையுறுத்தும் கோட்பாடுகளை அமல்படுத்தும் சட்டங்களை சரத்து 14, 19, 31-ன் அடிப்படையில் செல்லாது என அறிவிக்க முடியாது என வகைசெய்தது.",
    "Option A is incorrect; Article 31A was added by 1st Amendment (1951).", "விருப்பம் A தவறானது.",
    "Option B is correct; 25th Amendment inserted Article 31C.", "விருப்பம் B சரியானது.",
    "Option C is incorrect; Article 31B was added by 1st Amendment (1951).", "விருப்பம் C தவறானது.",
    "Option D is incorrect; Article 300A was added by 44th Amendment (1978).", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: SC in Kesavananda Bharati (1973) upheld 1st part of Art 31C but struck down 2nd part (which barred judicial review).",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: கேசவாநந்த பாரதி வழக்கில் சரத்து 31C-ன் முதல் பகுதி உறுதியளிக்கப்பட்டு, 2-வது பகுதி ரத்து செய்யப்பட்டது.",
    "📖 Revision Fact: Famous dictum: 'Where Article 31C comes in, Article 14 goes out.'",
    "📖 திருத்தல் செய்தி: 'சரத்து 31C உள்நுழையும் இடத்தில் சரத்து 14 வெளியேறுகிறது.'",
    "Understand", "High", ["25th Amendment", "Article 31C", "DPSP Directive"]
)

# Q29 - Ans: A
add_p2(
    "polity_amendments_gt_029", "Medium", "match_the_following",
    "Match List-I (Constitutional Amendment) with List-II (Subject / Purpose) and select the correct code:\nList-I:\nA. 52nd Amendment Act, 1985\nB. 61st Amendment Act, 1988\nC. 73rd Amendment Act, 1992\nD. 86th Amendment Act, 2002\nList-II:\n1. Lowering voting age to 18 years\n2. Anti-Defection Law (10th Schedule)\n3. Right to Education (Article 21A)\n4. Panchayati Raj Institutions (Part IX)",
    "பட்டியல்-I (அரசியலமைப்பு திருத்தம்) பட்டியல்-II (பொருள் / நோக்கம்) உடன் பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்க:\nபட்டியல்-I:\nA. 52-வது திருத்தச் சட்டம், 1985\nB. 61-வது திருத்தச் சட்டம், 1988\nC. 73-வது திருத்தச் சட்டம், 1992\nD. 86-வது திருத்தச் சட்டம், 2002\nபட்டியல்-II:\n1. வாக்குரிமை வயதை 18 ஆகக் குறைத்தல்\n2. கட்சித் தாவல் தடைச் சட்டம் (10-வது அட்டவணை)\n3. கல்வி உரிமை (சரத்து 21A)\n4. பஞ்சாயத்து ராஜ் அமைப்புகள் (பகுதி IX)",
    "A-2, B-1, C-4, D-3", "A-2, B-1, C-4, D-3",
    "A-1, B-2, C-4, D-3", "A-1, B-2, C-4, D-3",
    "A-2, B-4, C-1, D-3", "A-2, B-4, C-1, D-3",
    "A-3, B-1, C-4, D-2", "A-3, B-1, C-4, D-2",
    "A",
    "📚 Core Explanation:\n- 52nd Amendment Act (1985) = Anti-Defection Law (A-2).\n- 61st Amendment Act (1988) = Lowering voting age to 18 (B-1).\n- 73rd Amendment Act (1992) = Panchayati Raj Institutions (C-4).\n- 86th Amendment Act (2002) = Right to Education Art 21A (D-3).\nCorrect match: A-2, B-1, C-4, D-3.",
    "📚 முதன்மை விளக்கம்:\n- 52-வது திருத்தம் (1985) = கட்சித் தாவல் தடைச் சட்டம் (A-2).\n- 61-வது திருத்தம் (1988) = வாக்குரிமை வயது 18 ஆகக் குறைப்பு (B-1).\n- 73-வது திருத்தம் (1992) = பஞ்சாயத்து ராஜ் (C-4).\n- 86-வது திருத்தம் (2002) = கல்வி உரிமை சரத்து 21A (D-3).",
    "Option A is correct as all matches align accurately.", "விருப்பம் A சரியானது.",
    "Option B is incorrect.", "விருப்பம் B தவறானது.",
    "Option C is incorrect.", "விருப்பம் C தவறானது.",
    "Option D is incorrect.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: 52nd = Defection, 61st = Voting Age, 73rd = Panchayats, 86th = Education.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: 52-வது = கட்சித் தாவல், 61-வது = வாக்குரிமை வயது, 73-வது = பஞ்சாயத்து, 86-வது = கல்வி.",
    "📖 Revision Fact: 52nd added 10th Schedule, 73rd added 11th Schedule.",
    "📖 திருத்தல் செய்தி: 52-வது 10-வது அட்டவணை, 73-வது 11-வது அட்டவணை.",
    "Understand", "High", ["Match the Following", "52nd Amendment", "61st Amendment", "86th Amendment"]
)

# Q30 - Ans: C
add_p2(
    "polity_amendments_gt_030", "Hard", "single_choice",
    "Which Supreme Court case invalidated Clause (4) of the 39th Amendment Act, 1975, which had placed the election of the Prime Minister and Speaker beyond judicial review?",
    "பிரதமர் மற்றும் சபாநாயகரின் தேர்தலை நீதிமன்ற ஆய்விலிருந்து விலக்கி வைத்த 39-வது திருத்தச் சட்டத்தின் பிரிவு (4)-ஐ ரத்து செய்த உச்சநீதிமன்ற வழக்கு எது?",
    "Kesavananda Bharati v. State of Kerala (1973)", "கேசவாநந்த பாரதி எதிர் கேரள மாநிலம் (1973)",
    "Minerva Mills v. Union of India (1980)", "மினெர்வா மில்ஸ் எதிர் இந்திய ஒன்றியம் (1980)",
    "Indira Nehru Gandhi v. Raj Narain (1975)", "இந்திரா நேரு காந்தி எதிர் ராஜ் நாராயண் (1975)",
    "Maneka Gandhi v. Union of India (1978)", "மேனகா காந்தி எதிர் இந்திய ஒன்றியம் (1978)",
    "C",
    "📚 Core Explanation:\nIn Indira Nehru Gandhi v. Raj Narain (1975), the Supreme Court applied the Basic Structure doctrine for the first time after Kesavananda Bharati to strike down Clause (4) of the 39th Amendment Act, 1975, holding that free and fair elections, rule of law, and judicial review are basic structure features.",
    "📚 முதன்மை விளக்கம்:\nஇந்திரா நேரு காந்தி எதிர் ராஜ் நாராயண் வழக்கில் (1975), கேசவாநந்த பாரதி தீர்ப்பிற்குப் பிறகு முதன்முறையாக அடிப்படை கட்டமைப்பு கோட்பாட்டைப் பயன்படுத்தி 39-வது திருத்தச் சட்டத்தின் பிரிவு (4)-ஐ உச்சநீதிமன்றம் ரத்து செய்தது.",
    "Option A is incorrect; Kesavananda Bharati (1973) established the doctrine.", "விருப்பம் A தவறானது.",
    "Option B is incorrect; Minerva Mills (1980) struck down Art 368(4)&(5).", "விருப்பம் B தவறானது.",
    "Option C is correct; Indira Gandhi v. Raj Narain struck down 39th Amendment Clause 4.", "விருப்பம் C சரியானது.",
    "Option D is incorrect; Maneka Gandhi (1978) expanded Article 21 due process.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: In Indira Gandhi case (1975), SC added Democracy, Free & Fair Elections, and Rule of Law to Basic Structure.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: இந்திரா காந்தி வழக்கில் ஜனநாயகம், சுதந்திரமான தேர்தல், சட்டத்தின் ஆட்சி ஆகியவை அடிப்படை கட்டமைப்பில் சேர்க்கப்பட்டன.",
    "📖 Revision Fact: 39th Amendment was passed during 1975 Emergency specifically to protect PM Indira Gandhi's election.",
    "📖 திருத்தல் செய்தி: 39-வது திருத்தம் பிரதமர் தேர்தலில் இந்திரா காந்தியைக் காப்பாற்ற 1975 அவசரநிலையின் போது நிறைவேற்றப்பட்டது.",
    "Analyze", "High", ["Indira Gandhi Case", "39th Amendment", "Basic Structure Application"]
)

# Q31 - Ans: D
add_p2(
    "polity_amendments_gt_031", "Medium", "statement",
    "Consider the following transfers of subjects made from the State List to the Concurrent List by the 42nd Constitutional Amendment Act, 1976:\n1. Education\n2. Forests\n3. Weights and measures\n4. Protection of wild animals and birds\n5. Administration of justice (constitution and organisation of all courts except SC and HCs)\nWhich of the subjects listed above were transferred to the Concurrent List by the 42nd Amendment?",
    "1976-ஆம் ஆண்டின் 42-வது அரசியலமைப்பு திருத்தச் சட்டத்தின் மூலம் மாநிலப் பட்டியலிலிருந்து பொதுப் பட்டியலுக்கு மாற்றப்பட்ட பின்வரும் தலைப்புகளை ஆராய்க:\n1. கல்வி\n2. காடுகள்\n3. எடைகள் மற்றும் அளவீடுகள்\n4. வனவிலங்குகள் மற்றும் பறவைகள் பாதுகாப்பு\n5. நீதி நிர்வாகம் (உச்ச மற்றும் உயர்நீதிமன்றங்கள் தவிர்ந்த அனைத்து நீதிமன்றங்களின் அமைப்பு)\nமேற்கண்ட தலைப்புகளில் எவை 42-வது திருத்தத்தால் பொதுப் பட்டியலுக்கு மாற்றப்பட்டன?",
    "1, 2 and 4 only", "1, 2 மற்றும் 4 மட்டுமே",
    "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
    "2, 3, 4 and 5 only", "2, 3, 4 மற்றும் 5 மட்டுமே",
    "1, 2, 3, 4 and 5", "1, 2, 3, 4 மற்றும் 5",
    "D",
    "📚 Core Explanation:\nThe 42nd Constitutional Amendment Act, 1976 transferred FIVE subjects from the State List (List II) to the Concurrent List (List III):\n1. Education\n2. Forests\n3. Weights and Measures (except standard specification)\n4. Protection of Wild Animals and Birds\n5. Administration of Justice (constitution and organisation of courts except SC & HC).",
    "📚 முதன்மை விளக்கம்:\n1976-ஆம் ஆண்டின் 42-வது அரசியலமைப்பு திருத்தச் சட்டம் மாநிலப் பட்டியலிலிருந்து பொதுப் பட்டியலுக்கு 5 தலைப்புகளை மாற்றியது: 1. கல்வி, 2. காடுகள், 3. எடைகள் & அளவீடுகள், 4. வனவிலங்குகள் & பறவைகள் பாதுகாப்பு, 5. நீதி நிர்வாகம்.",
    "Option A is incomplete.", "விருப்பம் A அரைகுறையானது.",
    "Option B is incomplete.", "விருப்பம் B அரைகுறையானது.",
    "Option C is incomplete.", "விருப்பம் C அரைகுறையானது.",
    "Option D is correct as all 5 listed subjects were transferred.", "விருப்பம் D சரியானது.",
    "💡 TNPSC Tip: Mnemonic for 5 transferred subjects: E-F-W-A-J (Education, Forests, Weights, Animals, Justice).",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: 5 மாற்றப்பட்ட தலைப்புகளின் நினைவுக் குறிப்பு: கல்வி, காடுகள், எடைகள், விலங்குகள், நீதி நிர்வாகம்.",
    "📖 Revision Fact: Before 1976, Education was an exclusive State subject.",
    "📖 திருத்தல் செய்தி: 1976-க்கு முன் கல்வி பிரத்யேக மாநிலத் தலைப்பாக இருந்தது.",
    "Remember", "High", ["42nd Amendment", "Concurrent List", "Education and Forests"]
)

# Q32 - Ans: B
add_p2(
    "polity_amendments_gt_032", "Easy", "single_choice",
    "Which Constitutional Amendment Act inserted Part IV-A (Fundamental Duties) containing Article 51A into the Constitution of India?",
    "இந்திய அரசியலமைப்பில் சரத்து 51A கொண்ட பகுதி IV-A-ஐ (அடிப்படை கடமைகள்) சேர்த்த அரசியலமைப்பு திருத்தச் சட்டம் எது?",
    "24th Constitutional Amendment Act, 1971", "24-வது அரசியலமைப்பு திருத்தச் சட்டம், 1971",
    "42nd Constitutional Amendment Act, 1976", "42-வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
    "44th Constitutional Amendment Act, 1978", "44-வது அரசியலமைப்பு திருத்தச் சட்டம், 1978",
    "86th Constitutional Amendment Act, 2002", "86-வது அரசியலமைப்பு திருத்தச் சட்டம், 2002",
    "B",
    "📚 Core Explanation:\nThe 42nd Constitutional Amendment Act, 1976 added Part IV-A (Article 51A) introducing 10 Fundamental Duties on the recommendation of Swaran Singh Committee.",
    "📚 முதன்மை விளக்கம்:\n1976-ஆம் ஆண்டின் 42-வது அரசியலமைப்பு திருத்தச் சட்டம் ஸ்வரன் சிங் குழுவின் பரிந்துரையின் பேரில் 10 அடிப்படைக் கடமைகளை உள்ளடக்கிய பகுதி IV-A-ஐச் சேர்த்தது.",
    "Option A is incorrect; 24th Amendment dealt with Art 368.", "விருப்பம் A தவறானது.",
    "Option B is correct; 42nd Amendment introduced Part IV-A.", "விருப்பம் B சரியானது.",
    "Option C is incorrect; 44th Amendment restored democratic balance.", "விருப்பம் C தவறானது.",
    "Option D is incorrect; 86th Amendment added the 11th Fundamental Duty (51A(k)).", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: Swaran Singh Committee recommended 8 duties, but 42nd Amendment inserted 10 duties.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: ஸ்வரன் சிங் குழு 8 கடமைகளைப் பரிந்துரைத்தது, ஆனால் 42-வது திருத்தம் 10 கடமைகளைச் சேர்த்தது.",
    "📖 Revision Fact: 86th Amendment Act 2002 added the 11th Fundamental Duty.",
    "📖 திருத்தல் செய்தி: 86-வது திருத்தச் சட்டம் 2002 11-வது அடிப்படைக் கடமையைச் சேர்த்தது.",
    "Remember", "High", ["42nd Amendment", "Part IV-A", "Fundamental Duties"]
)

# Q33 - Ans: B
add_p2(
    "polity_amendments_gt_033", "Medium", "single_choice",
    "Which Constitutional Amendment Act substituted the word 'Odia' for 'Oriya' in the Eighth Schedule of the Constitution?",
    "அரசியலமைப்பின் எட்டாவது அட்டவணையில் 'ஒரியா' (Oriya) என்ற சொல்லிற்குப் பதிலாக 'ஒடியா' (Odia) என மாற்றிய அரசியலமைப்பு திருத்தச் சட்டம் எது?",
    "92nd Constitutional Amendment Act, 2003", "92-வது அரசியலமைப்பு திருத்தச் சட்டம், 2003",
    "96th Constitutional Amendment Act, 2011", "96-வது அரசியலமைப்பு திருத்தச் சட்டம், 2011",
    "97th Constitutional Amendment Act, 2011", "97-வது அரசியலமைப்பு திருத்தச் சட்டம், 2011",
    "100th Constitutional Amendment Act, 2015", "100-வது அரசியலமைப்பு திருத்தச் சட்டம், 2015",
    "B",
    "📚 Core Explanation:\nThe 96th Constitutional Amendment Act, 2011 substituted 'Odia' for 'Oriya' in the Eighth Schedule of the Constitution. Consequently, Oriya language was renamed as Odia.",
    "📚 முதன்மை விளக்கம்:\n2011-ஆம் ஆண்டின் 96-வது அரசியலமைப்பு திருத்தச் சட்டம் எட்டாவது அட்டவணையில் 'ஒரியா' என்பதற்குப் பதிலாக 'ஒடியா' என மாற்றியது.",
    "Option A is incorrect; 92nd Amendment added Bodo, Dogri, Maithili, Santhali.", "விருப்பம் A தவறானது.",
    "Option B is correct; 96th Amendment renamed Oriya to Odia.", "விருப்பம் B சரியானது.",
    "Option C is incorrect; 97th Amendment related to Co-operative Societies.", "விருப்பம் C தவறானது.",
    "Option D is incorrect; 100th Amendment related to Land Boundary Agreement with Bangladesh.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: 96th Amendment did NOT add a new language; it only renamed an existing language (Oriya to Odia).",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: 96-வது திருத்தம் புதிய மொழியைச் சேர்க்கவில்லை; பெயர் மாற்றம் மட்டுமே செய்தது.",
    "📖 Revision Fact: 96th Amendment Act was enacted in 2011.",
    "📖 திருத்தல் செய்தி: 96-வது திருத்தச் சட்டம் 2011-ல் இயற்றப்பட்டது.",
    "Remember", "High", ["96th Amendment", "Odia Language", "Eighth Schedule"]
)

# Q34 - Ans: B
add_p2(
    "polity_amendments_gt_034", "Easy", "single_choice",
    "Which Constitutional Amendment Act gave effect to the 1974 Land Boundary Agreement and its 2011 Protocol between India and Bangladesh?",
    "இந்தியா மற்றும் வங்காளதேசத்திற்கு இடையிலான 1974 நில எல்லை ஒப்பந்தம் மற்றும் அதன் 2011 நெறிமுறைக்கு வடிவம் கொடுத்த அரசியலமைப்பு திருத்தச் சட்டம் எது?",
    "99th Constitutional Amendment Act, 2014", "99-வது அரசியலமைப்பு திருத்தச் சட்டம், 2014",
    "100th Constitutional Amendment Act, 2015", "100-வது அரசியலமைப்பு திருத்தச் சட்டம், 2015",
    "101st Constitutional Amendment Act, 2016", "101-வது அரசியலமைப்பு திருத்தச் சட்டம், 2016",
    "102nd Constitutional Amendment Act, 2018", "102-வது அரசியலமைப்பு திருத்தச் சட்டம், 2018",
    "B",
    "📚 Core Explanation:\nThe 100th Constitutional Amendment Act, 2015 ratified the Land Boundary Agreement (LBA) between India and Bangladesh, transferring 111 enclaves to Bangladesh and acquiring 51 enclaves from Bangladesh.",
    "📚 முதன்மை விளக்கம்:\n2015-ஆம் ஆண்டின் 100-வது அரசியலமைப்பு திருத்தச் சட்டம் இந்தியா மற்றும் வங்காளதேசத்திற்கு இடையிலான நில எல்லை ஒப்பந்தத்தை (LBA) அமல்படுத்தியது. இதன் மூலம் 111 இடாஞ்சல்கள் வங்காளதேசத்திற்கும், 51 இடாஞ்சல்கள் இந்தியாவிற்கும் மாற்றப்பட்டன.",
    "Option A is incorrect; 99th Amendment established NJAC (struck down).", "விருப்பம் A தவறானது.",
    "Option B is correct; 100th Amendment enacted Land Boundary Agreement.", "விருப்பம் B சரியானது.",
    "Option C is incorrect; 101st Amendment introduced GST.", "விருப்பம் C தவறானது.",
    "Option D is incorrect; 102nd Amendment gave status to NCBC.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: 100th Amendment modified the 1st Schedule of the Constitution covering Assam, West Bengal, Meghalaya, and Tripura territories.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: 100-வது திருத்தம் அசாம், மேற்கு வங்காளம், மேகாயா, திரிபுரா பகுதிகளைக் கொண்ட முதல் அட்டவணையை திருத்தியது.",
    "📖 Revision Fact: In Berubari Union Case (1960), SC held that ceding Indian territory requires Constitutional Amendment under Art 368.",
    "📖 திருத்தல் செய்தி: பெருபாரி யூனியன் வழக்கில் (1960) இந்திய நிலப்பகுதியை ஒப்படைக்க சரத்து 368 திருத்தம் தேவை எனக் கூறப்பட்டது.",
    "Remember", "High", ["100th Amendment", "Land Boundary Agreement", "Bangladesh"]
)

# Q35 - Ans: B
add_p2(
    "polity_amendments_gt_035", "Medium", "single_choice",
    "Which Constitutional Amendment Act accorded constitutional status to the National Commission for Backward Classes (NCBC) under Article 338B?",
    "சரத்து 338B-ன் கீழ் தேசிய பிற்படுத்தப்பட்டோர் ஆணையத்திற்கு (NCBC) அரசியலமைப்பு அந்தஸ்து வழங்கிய அரசியலமைப்பு திருத்தச் சட்டம் எது?",
    "101st Constitutional Amendment Act, 2016", "101-வது அரசியலமைப்பு திருத்தச் சட்டம், 2016",
    "102nd Constitutional Amendment Act, 2018", "102-வது அரசியலமைப்பு திருத்தச் சட்டம், 2018",
    "103rd Constitutional Amendment Act, 2019", "103-வது அரசியலமைப்பு திருத்தச் சட்டம், 2019",
    "104th Constitutional Amendment Act, 2020", "104-வது அரசியலமைப்பு திருத்தச் சட்டம், 2020",
    "B",
    "📚 Core Explanation:\nThe 102nd Constitutional Amendment Act, 2018 granted constitutional status to the National Commission for Backward Classes (NCBC) by inserting Article 338B. It also inserted Article 342A.",
    "📚 முதன்மை விளக்கம்:\n2018-ஆம் ஆண்டின் 102-வது அரசியலமைப்பு திருத்தச் சட்டம் சரத்து 338B-ஐச் சேர்த்து தேசிய பிற்படுத்தப்பட்டோர் ஆணையத்திற்கு (NCBC) அரசியலமைப்பு அந்தஸ்து வழங்கியது.",
    "Option A is incorrect; 101st Amendment introduced GST.", "விருப்பம் A தவறானது.",
    "Option B is correct; 102nd Amendment constitutionalized NCBC.", "விருப்பம் B சரியானது.",
    "Option C is incorrect; 103rd Amendment introduced EWS reservation.", "விருப்பம் C தவறானது.",
    "Option D is incorrect; 104th Amendment extended SC/ST reservation.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: Prior to 2018, NCBC was a statutory body set up under NCBC Act 1993 following Indira Sawhney case judgment.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: 2018-க்கு முன் NCBC இந்திரா சாவ்னி தீர்ப்பைத் தொடர்ந்து 1993 சட்டத்தின் கீழ் அமைக்கப்பட்ட சட்டப்பூர்வ அமைப்பாக இருந்தது.",
    "📖 Revision Fact: Three Constitutional Commissions: Art 338 (NCSC), Art 338A (NCST), Art 338B (NCBC).",
    "📖 திருத்தல் செய்தி: மூன்று அரசியலமைப்பு ஆணையங்கள்: சரத்து 338 (NCSC), 338A (NCST), 338B (NCBC).",
    "Remember", "High", ["102nd Amendment", "NCBC", "Article 338B"]
)

# Q36 - Ans: B
add_p2(
    "polity_amendments_gt_036", "Medium", "single_choice",
    "Which Constitutional Amendment Act introduced 33% reservation for women in Lok Sabha, State Legislative Assemblies, and Delhi Legislative Assembly (Nari Shakti Vandan Adhiniyam)?",
    "மக்களவை, மாநில சட்டப்பேரவைகள் மற்றும் தில்லி சட்டமன்றத்தில் மகளிருக்கு 33% இடஒதுக்கீட்டை அறிமுகப்படுத்திய அரசியலமைப்பு திருத்தச் சட்டம் (நாரி சக்தி வந்தன் அதினியம்) எது?",
    "103rd Constitutional Amendment Act, 2019", "103-வது அரசியலமைப்பு திருத்தச் சட்டம், 2019",
    "106th Constitutional Amendment Act, 2023", "106-வது அரசியலமைப்பு திருத்தச் சட்டம், 2023",
    "104th Constitutional Amendment Act, 2020", "104-வது அரசியலமைப்பு திருத்தச் சட்டம், 2020",
    "105th Constitutional Amendment Act, 2021", "105-வது அரசியலமைப்பு திருத்தச் சட்டம், 2021",
    "B",
    "📚 Core Explanation:\nThe 106th Constitutional Amendment Act, 2023 (Nari Shakti Vandan Adhiniyam) provides 33% (one-third) reservation for women in Lok Sabha, State Legislative Assemblies, and the National Capital Territory of Delhi Assembly for a period of 15 years.",
    "📚 முதன்மை விளக்கம்:\n2023-ஆம் ஆண்டின் 106-வது அரசியலமைப்பு திருத்தச் சட்டம் (நாரி சக்தி வந்தன் அதினியம்) மக்களவை, மாநில சட்டமன்றங்கள் மற்றும் தில்லி சட்டமன்றத்தில் மகளிருக்கு 33% இடஒதுக்கீட்டை 15 ஆண்டுகளுக்கு வழங்குகிறது.",
    "Option A is incorrect; 103rd Amendment introduced EWS reservation.", "விருப்பம் A தவறானது.",
    "Option B is correct; 106th Amendment introduced Women's Reservation.", "விருப்பம் B சரியானது.",
    "Option C is incorrect; 104th Amendment extended SC/ST reservation.", "விருப்பம் C தவறானது.",
    "Option D is incorrect; 105th Amendment restored state OBC lists.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: 106th Amendment inserted Articles 330A, 332A, and 334A.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: 106-வது திருத்தம் சரத்துகள் 330A, 332A, 334A ஆகியவற்றைச் சேர்த்தது.",
    "📖 Revision Fact: The reservation will come into effect after the publication of census conducted after the commencement of the Act and subsequent delimitation.",
    "📖 திருத்தல் செய்தி: இச்சட்டம் அமலுக்கு வந்தபின் நடத்தப்படும் மக்கள் தொகை கணக்கெடுப்பு மற்றும் தொகுதி மறுசீரமைப்பிற்குப் பின் இது அமலாகும்.",
    "Remember", "High", ["106th Amendment", "Women Reservation", "Nari Shakti Vandan"]
)

# Q37 - Ans: C
add_p2(
    "polity_amendments_gt_037", "Hard", "statement",
    "Consider the following Constitutional Amendment Acts relating to reservations in public employment:\n1. 77th Amendment Act, 1995: Added Article 16(4A) for reservation in promotion for SCs and STs.\n2. 81st Amendment Act, 2000: Added Article 16(4B) to treat backlog reserved vacancies as a separate class not subject to the 50% cap.\n3. 85th Amendment Act, 2001: Provided for consequential seniority in promotion for SC/ST government servants with retrospective effect.\nWhich of the statements given above are correct?",
    "பொது வேலைவாய்ப்பில் இடஒதுக்கீடு தொடர்பான பின்வரும் அரசியலமைப்பு திருத்தச் சட்டங்களை ஆராய்க:\n1. 77-வது திருத்தச் சட்டம் 1995: SC மற்றும் ST-க்கு பதவி உயர்வில் இடஒதுக்கீடு வழங்க சரத்து 16(4A)-ஐச் சேர்த்தது.\n2. 81-வது திருத்தச் சட்டம் 2000: நிலுவையில் உள்ள இடஒதுக்கீட்டு காலிப்பணியிடங்களை 50% வரம்பிற்கு அப்பாற்பட்ட தனி வகுப்பாகக் கருத சரத்து 16(4B)-ஐச் சேர்த்தது.\n3. 85-வது திருத்தச் சட்டம் 2001: SC/ST அரசு ஊழியர்களுக்கு பதவி உயர்வில் தொடர்ச்சியான பணிமூப்பு (consequential seniority) வழங்கி முன்செல்லும் தேதியிலிருந்து அமல்படுத்தியது.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
    "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
    "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "1 and 3 only", "1 மற்றும் 3 மட்டுமே",
    "C",
    "📚 Core Explanation:\nAll three statements are CORRECT regarding the series of amendments enacted to overturn judicial restrictions on SC/ST reservation in promotions (post-Indira Sawhney 1992 verdict).\n- 77th Amendment (1995): Art 16(4A) - Reservation in promotion.\n- 81st Amendment (2000): Art 16(4B) - Carry forward of backlog vacancies exempted from 50% ceiling.\n- 85th Amendment (2001): Consequential seniority for SC/ST promoted officers (retrospective from 1995).\nThese amendments were upheld by SC in M. Nagaraj v. Union of India (2006).",
    "📚 முதன்மை விளக்கம்:\nமூன்று கூற்றுகளும் சரியானவை: 77-வது (பதவி உயர்வு இடஒதுக்கீடு), 81-வது (நிலுவை காலிப்பணியிட 50% விலக்கு), 85-வது (பணிமூப்பு உயர்வு). எம். நாகராஜ் வழக்கில் (2006) உச்சநீதிமன்றம் இவற்றை உறுதி செய்தது.",
    "Option A is incomplete.", "விருப்பம் A அரைகுறையானது.",
    "Option B is incomplete.", "விருப்பம் B அரைகுறையானது.",
    "Option C is correct as statements 1, 2, and 3 are all true.", "விருப்பம் C சரியானது.",
    "Option D is incomplete.", "விருப்பம் D அரைகுறையானது.",
    "💡 TNPSC Tip: Nagaraj Case (2006) upheld 77th, 81st, 82nd, and 85th Amendments subject to quantifiable data on backwardness & efficiency.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: எம். நாகராஜ் வழக்கு 77, 81, 82, 85-வது திருத்தங்களை உறுதி செய்தது.",
    "📖 Revision Fact: 82nd Amendment (2000) added proviso to Article 335 allowing relaxation of qualifying marks for SCs/STs in promotion exams.",
    "📖 திருத்தல் செய்தி: 82-வது திருத்தம் சரத்து 335-ல் பதவி உயர்வுத் தேர்வுகளில் தகுதி மதிப்பெண் தளர்வு அளித்தது.",
    "Analyze", "High", ["77th Amendment", "81st Amendment", "85th Amendment", "M Nagaraj Case"]
)

# Q38 - Ans: C
add_p2(
    "polity_amendments_gt_038", "Medium", "single_choice",
    "By which Constitutional Amendment Act was the freeze on the total number of seats in the Lok Sabha and State Legislative Assemblies extended until the year 2026?",
    "மக்களவை மற்றும் மாநில சட்டமன்றங்களின் மொத்த இடங்களின் எண்ணிக்கை மீதான முடக்கம் எந்த அரசியலமைப்பு திருத்தச் சட்டத்தின் மூலம் 2026 வரை நீட்டிக்கப்பட்டது?",
    "42nd Constitutional Amendment Act, 1976", "42-வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
    "84th Constitutional Amendment Act, 2001", "84-வது அரசியலமைப்பு திருத்தச் சட்டம், 2001",
    "87th Constitutional Amendment Act, 2003", "87-வது அரசியலமைப்பு திருத்தச் சட்டம், 2003",
    "91st Constitutional Amendment Act, 2003", "91-வது அரசியலமைப்பு திருத்தச் சட்டம், 2003",
    "C",
    "📚 Core Explanation:\nThe 84th Constitutional Amendment Act, 2001 extended the freeze on reallocation of seats in the Lok Sabha and State Assemblies till the first census after 2026. Initially, the 42nd Amendment had frozen seat allocation till 2001 based on 1971 census.",
    "📚 முதன்மை விளக்கம்:\n2001-ஆம் ஆண்டின் 84-வது அரசியலமைப்பு திருத்தச் சட்டம் மக்களவை மற்றும் மாநில சட்டமன்றங்களின் மொத்த இடங்களின் எண்ணிக்கை மீதான முடக்கத்தை 2026-க்குப் பிந்தைய முதல் மக்கள் தொகை கணக்கெடுப்பு வரை நீட்டித்தது.",
    "Option A is incorrect; 42nd Amendment froze seats till 2001.", "விருப்பம் A தவறானது.",
    "Option B is incorrect; 87th Amendment permitted internal delimitation based on 2001 census.", "விருப்பம் B தவறானது.",
    "Option C is correct as 84th Amendment extended the freeze till 2026.", "விருப்பம் C சரியானது.",
    "Option D is incorrect; 91st Amendment limited council of ministers.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: 84th Amendment extended the 2026 freeze based on 1991 census; later 87th Amendment (2003) allowed delimitation within states based on 2001 census without changing total seat count.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: 84-வது திருத்தம் 2026 வரை முடக்கியது; 87-வது திருத்தம் 2001 கணக்கெடுப்பின்படி உள் மறுசீரமைப்பை அனுமதித்தது.",
    "📖 Revision Fact: Original seat freeze was enacted by 42nd Amendment in 1976 to encourage family planning measures.",
    "📖 திருத்தல் செய்தி: குடும்பக் கட்டுப்பாடு நடவடிக்கைகளை ஊக்குவிக்க 42-வது திருத்தம் 1976-ல் முதன்முதலில் இடங்களை முடக்கியது.",
    "Remember", "High", ["84th Amendment", "Delimitation", "2026 Freeze"]
)

# Q39 - Ans: C
add_p2(
    "polity_amendments_gt_039", "Medium", "single_choice",
    "Which of the following official languages was NOT among the four languages added to the Eighth Schedule by the 92nd Constitutional Amendment Act, 2003?",
    "2003-ஆம் ஆண்டின் 92-வது அரசியலமைப்பு திருத்தச் சட்டத்தின் மூலம் எட்டாவது அட்டவணையில் சேர்க்கப்பட்ட நான்கு மொழிகளில் பின்வரும் எந்த மொழி இடம் பெறவில்லை?",
    "Bodo", "போடோ",
    "Dogri", "டோக்ரி",
    "Manipuri", "மணிப்பூரி",
    "Santhali", "சந்தாலி",
    "C",
    "📚 Core Explanation:\nThe 92nd Constitutional Amendment Act, 2003 added FOUR languages to the Eighth Schedule: Bodo, Dogri, Maithili, and Santhali (Mnemonic: BDMS). Manipuri was added earlier by the 71st Amendment Act, 1992 (along with Konkani and Nepali).",
    "📚 முதன்மை விளக்கம்:\n2003-ஆம் ஆண்டின் 92-வது அரசியலமைப்பு திருத்தச் சட்டம் போடோ, டோக்ரி, மைதிலி, சந்தாலி ஆகிய 4 மொழிகளை எட்டாவது அட்டவணையில் சேர்த்தது. மணிப்பூரி மொழி 1992-ன் 71-வது திருத்தச் சட்டத்தால் ஏற்கனவே சேர்க்கப்பட்டது.",
    "Option A is incorrect; Bodo was added by 92nd Amendment.", "விருப்பம் A தவறானது.",
    "Option B is incorrect; Dogri was added by 92nd Amendment.", "விருப்பம் B தவறானது.",
    "Option C is correct as Manipuri was added by 71st Amendment, not 92nd.", "விருப்பம் C சரியானது.",
    "Option D is incorrect; Santhali was added by 92nd Amendment.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: Mnemonic for 92nd Amendment languages: BDMS (Bodo, Dogri, Maithili, Santhali).",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: 92-வது திருத்த மொழிகளின் நினைவுக் குறிப்பு: BDMS (போடோ, டோக்ரி, மைதிலி, சந்தாலி).",
    "📖 Revision Fact: Total official languages in Eighth Schedule expanded from 18 to 22 following 92nd Amendment.",
    "📖 திருத்தல் செய்தி: 92-வது திருத்திற்குப் பின் எட்டாவது அட்டவணை மொழிகள் 18-லிருந்து 22 ஆக உயர்ந்தன.",
    "Understand", "High", ["92nd Amendment", "Eighth Schedule", "Languages"]
)

# Q40 - Ans: C
add_p2(
    "polity_amendments_gt_040", "Easy", "single_choice",
    "Which Article of the Constitution lays down the procedure for the abolition or creation of Legislative Councils in States, which can be amended by a Simple Majority of Parliament?",
    "மாநிலங்களில் சட்ட மேலவைகளை ஒழித்தல் அல்லது உருவாக்குவதற்கான நடைமுறையைக் கூறும் மற்றும் நாடாளுமன்றத்தின் எளிய பெரும்பான்மையால் திருத்தப்படக்கூடிய அரசியலமைப்பு சரத்து எது?",
    "Article 168", "சரத்து 168",
    "Article 170", "சரத்து 170",
    "Article 169", "சரத்து 169",
    "Article 171", "சரத்து 171",
    "C",
    "📚 Core Explanation:\nArticle 169 lays down that Parliament can abolish or create a Legislative Council in a State by a simple majority if the Legislative Assembly of the concerned State passes a resolution to that effect by a special majority. Such a law is explicitly declared NOT to be an amendment under Article 368.",
    "📚 முதன்மை விளக்கம்:\nசரத்து 169-ன் படி, சம்பந்தப்பட்ட மாநில சட்டமன்றம் சிறப்பு பெரும்பான்மையுடன் தீர்மானம் நிறைவேற்றினால், நாடாளுமன்றம் எளிய பெரும்பான்மையால் மாநிலத்தில் சட்ட மேலவையை உருவாக்கலாம் அல்லது ஒழிக்கலாம். இது சரத்து 368-ன் கீழ் திருத்தமாகக் கருதப்படாது.",
    "Option A is incorrect; Article 168 defines constitution of legislatures in states.", "விருப்பம் A தவறானது.",
    "Option B is incorrect; Article 170 deals with composition of Legislative Assemblies.", "விருப்பம் B தவறானது.",
    "Option C is correct as Article 169 prescribes creation/abolition procedure.", "விருப்பம் C சரியானது.",
    "Option D is incorrect; Article 171 deals with composition of Legislative Councils.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: State Assembly resolution under Art 169 requires Special Majority, but Parliament passing the law requires only Simple Majority.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: மாநில சட்டமன்றத் தீர்மானத்திற்கு சிறப்பு பெரும்பான்மை தேவை, ஆனால் நாடாளுமன்றச் சட்டத்திற்கு எளிய பெரும்பான்மையே போதுமானது.",
    "📖 Revision Fact: Tamil Nadu Legislative Council was abolished in 1986 under M.G. Ramachandran government.",
    "📖 திருத்தல் செய்தி: தமிழ்நாடு சட்ட மேலவை 1986-ல் எம்.ஜி.ஆர் ஆட்சிக்காலத்தில் ஒழிக்கப்பட்டது.",
    "Remember", "High", ["Article 169", "Legislative Council", "Simple Majority"]
)

# Q41 - Ans: C
add_p2(
    "polity_amendments_gt_041", "Medium", "single_choice",
    "Which Constitutional Amendment Act extended the tenure of Lok Sabha and State Legislative Assemblies from 5 years to 6 years, which was later restored back to 5 years by the 44th Amendment Act?",
    "மக்களவை மற்றும் மாநில சட்டமன்றங்களின் பதவிக் காலத்தை 5 ஆண்டுகளிலிருந்து 6 ஆண்டுகளாக உயர்த்திய திருத்தச் சட்டம் எது (பின்னர் 44-வது திருத்தத்தால் மீண்டும் 5 ஆண்டுகளாக மாற்றப்பட்டது)?",
    "24th Constitutional Amendment Act, 1971", "24-வது அரசியலமைப்பு திருத்தச் சட்டம், 1971",
    "38th Constitutional Amendment Act, 1975", "38-வது அரசியலமைப்பு திருத்தச் சட்டம், 1975",
    "42nd Constitutional Amendment Act, 1976", "42-வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
    "52nd Constitutional Amendment Act, 1985", "52-வது அரசியலமைப்பு திருத்தச் சட்டம், 1985",
    "C",
    "📚 Core Explanation:\nThe 42nd Constitutional Amendment Act, 1976 extended the duration of Lok Sabha and Legislative Assemblies from 5 to 6 years. Subsequently, the 44th Constitutional Amendment Act, 1978 restored their original 5-year tenure.",
    "📚 முதன்மை விளக்கம்:\n1976-ஆம் ஆண்டின் 42-வது அரசியலமைப்பு திருத்தச் சட்டம் மக்களவை மற்றும் சட்டமன்றங்களின் பதவிக்காலத்தை 5-லிருந்து 6 ஆண்டுகளாக உயர்த்தியது. பின்னர் 1978-ன் 44-வது திருத்தச் சட்டம் மீண்டும் 5 ஆண்டுகளாகக் குறைத்தது.",
    "Option A is incorrect.", "விருப்பம் A தவறானது.",
    "Option B is incorrect.", "விருப்பம் B தவறானது.",
    "Option C is correct; 42nd Amendment increased tenure to 6 years.", "விருப்பம் C சரியானது.",
    "Option D is incorrect.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: 5th Lok Sabha (1971-1977) was the only Lok Sabha whose duration extended beyond 5 years (lasted 5 years 10 months).",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: 5-வது மக்களவை (1971-1977) மட்டுமே 5 ஆண்டுகளுக்கு மேல் நீடித்த ஒரே மக்களவை ஆகும்.",
    "📖 Revision Fact: 44th Amendment Act 1978 restored normal 5-year term.",
    "📖 திருத்தல் செய்தி: 44-வது திருத்தச் சட்டம் 1978 மீண்டும் 5 ஆண்டு காலவரம்பை மீட்டெடுத்தது.",
    "Remember", "High", ["42nd Amendment", "Lok Sabha Tenure", "44th Amendment"]
)

# Q42 - Ans: D
add_p2(
    "polity_amendments_gt_042", "Hard", "statement",
    "Consider the following statements regarding the Basic Structure Doctrine:\n1. The phrase 'Basic Structure' is explicitly defined in Part XX of the Indian Constitution.\n2. The Supreme Court in Waman Rao Case (1981) held that the Basic Structure doctrine applies prospectively to all amendments enacted after April 24, 1973.\n3. In I.R. Coelho Case (2007), a 9-judge bench ruled that laws placed in the 9th Schedule after April 24, 1973 are open to judicial review if they violate basic structure rights.\nWhich of the statements given above are correct?",
    "அடிப்படை கட்டமைப்பு கோட்பாடு குறித்த பின்வரும் கூற்றுகளை ஆராய்க:\n1. 'அடிப்படை கட்டமைப்பு' என்ற சொல்லாடல் இந்திய அரசியலமைப்பின் பகுதி XX-ல் தெளிவாக வரையறுக்கப்பட்டுள்ளது.\n2. வாமன் ராவ் வழக்கில் (1981) ஏப்ரல் 24, 1973-க்குப் பிறகு இயற்றப்பட்ட அனைத்து திருத்தங்களுக்கும் அடிப்படை கட்டமைப்பு கோட்பாடு எதிர்கால நோக்கில் பொருந்தும் என உச்சநீதிமன்றம் தீர்ப்பளித்தது.\n3. ஐ.ஆர். கோயல்ஹோ வழக்கில் (2007) 9 நீதிபதிகள் அமர்வு ஏப்ரல் 24, 1973-க்குப் பிறகு 9-வது அட்டவணையில் சேர்க்கப்பட்ட சட்டங்கள் அடிப்படை உரிமைகளை மீறினால் நீதிமன்ற ஆய்வுக்கு உட்பட்டவை எனத் தீர்ப்பளித்தது.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
    "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
    "1 and 3 only", "1 மற்றும் 3 மட்டுமே",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
    "D",
    "📚 Core Explanation:\nStatement 1 is INCORRECT: The phrase 'Basic Structure' is NOT defined anywhere in the Constitution; it is a judicial innovation.\nStatement 2 is CORRECT: Waman Rao (1981) set the cutoff date as April 24, 1973 (Kesavananda verdict date).\nStatement 3 is CORRECT: I.R. Coelho (2007) affirmed that post-April 24, 1973 additions to 9th Schedule can be challenged for basic structure violations.",
    "📚 முதன்மை விளக்கம்:\nகூற்று 1 தவறு: 'அடிப்படை கட்டமைப்பு' என்ற சொல் அரசியலமைப்பில் எங்கும் வரையறுக்கப்படவில்லை; அது நீதித்துறையின் கண்டுபிடிப்பு.\nகூற்று 2 சரி: வாமன் ராவ் வழக்கு ஏப்ரல் 24, 1973-ஐ வரம்புத் தேதியாக நிர்ணயித்தது.\nகூற்று 3 சரி: ஐ.ஆர். கோயல்ஹோ வழக்கு 9-வது அட்டவணைச் சட்டங்களின் நீதிமன்ற ஆய்வை உறுதிப்படுத்தியது.",
    "Option A is incorrect because 1 is false.", "விருப்பம் A தவறானது.",
    "Option B is incorrect because 1 is false.", "விருப்பம் B தவறானது.",
    "Option C is incorrect because 1 is false.", "விருப்பம் C தவறானது.",
    "Option D is correct as statements 2 and 3 are true while 1 is false.", "விருப்பம் D சரியானது.",
    "💡 TNPSC Tip: Cut-off date for Basic Structure applicability is April 24, 1973 (the date of Kesavananda Bharati verdict).",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: அடிப்படை கட்டமைப்பு கோட்பாட்டின் வரம்புத் தேதி ஏப்ரல் 24, 1973 ஆகும்.",
    "📖 Revision Fact: I.R. Coelho case was decided by a unanimous 9-judge Constitution bench in 2007.",
    "📖 திருத்தல் செய்தி: ஐ.ஆர். கோயல்ஹோ வழக்கு 2007-ல் 9 நீதிபதிகள் கொண்ட அமர்வால் தீர்ப்பளிக்கப்பட்டது.",
    "Analyze", "High", ["Basic Structure", "Waman Rao Case", "IR Coelho Case"]
)

# Q43 - Ans: D
add_p2(
    "polity_amendments_gt_043", "Medium", "single_choice",
    "Which Constitutional Amendment Act granted constitutional recognition to the Union Territory of Delhi as the 'National Capital Territory of Delhi' (NCT) and created a Legislative Assembly for it?",
    "தில்லி ஒன்றிய பிரதேசத்திற்கு 'தேசிய தலைநகர் பகுதி' (NCT) என்ற அரசியலமைப்பு அங்கீகாரத்தையும் சட்டமன்றத்தையும் உருவாக்கிய திருத்தச் சட்டம் எது?",
    "52nd Constitutional Amendment Act, 1985", "52-வது அரசியலமைப்பு திருத்தச் சட்டம், 1985",
    "61st Constitutional Amendment Act, 1988", "61-வது அரசியலமைப்பு திருத்தச் சட்டம், 1988",
    "73rd Constitutional Amendment Act, 1992", "73-வது அரசியலமைப்பு திருத்தச் சட்டம், 1992",
    "69th Constitutional Amendment Act, 1991", "69-வது அரசியலமைப்பு திருத்தச் சட்டம், 1991",
    "D",
    "📚 Core Explanation:\nThe 69th Constitutional Amendment Act, 1991 inserted Articles 239AA and 239AB into the Constitution, designating the Union Territory of Delhi as the National Capital Territory of Delhi and providing for a 70-member Legislative Assembly and a 7-member Council of Ministers.",
    "📚 முதன்மை விளக்கம்:\n1991-ஆம் ஆண்டின் 69-வது அரசியலமைப்பு திருத்தச் சட்டம் சரத்துகள் 239AA மற்றும் 239AB-ஐச் சேர்த்து தில்லியை தேசிய தலைநகர் பகுதியாக அறிவித்ததுடன் 70 உறுப்பினர்களைக் கொண்ட சட்டமன்றத்தை உருவாக்கியது.",
    "Option A is incorrect; 52nd Amendment introduced Anti-Defection Law.", "விருப்பம் A தவறானது.",
    "Option B is incorrect; 61st Amendment lowered voting age.", "விருப்பம் B தவறானது.",
    "Option C is incorrect; 73rd Amendment related to Panchayati Raj.", "விருப்பம் C தவறானது.",
    "Option D is correct; 69th Amendment provided special status to Delhi (Art 239AA).", "விருப்பம் D சரியானது.",
    "💡 TNPSC Tip: Under Art 239AA, Delhi Assembly has legislative power over State List items EXCEPT Public Order, Police, and Land.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: தில்லி சட்டமன்றத்திற்கு பொது அமைதி, காவல்துறை, நிலம் ஆகிய 3 விஷயங்களைத் தவிர மற்றவற்றில் அதிகாரமுண்டு.",
    "📖 Revision Fact: Council of Ministers in Delhi is capped at 10% of assembly strength (7 ministers including CM).",
    "📖 திருத்தல் செய்தி: தில்லியில் அமைச்சரவை அளவு 10% (முதலமைச்சர் உட்பட 7 அமைச்சர்கள்) என வரம்பிடப்பட்டுள்ளது.",
    "Remember", "High", ["69th Amendment", "Delhi NCT", "Article 239AA"]
)

# Q44 - Ans: D
add_p2(
    "polity_amendments_gt_044", "Easy", "single_choice",
    "Which Constitutional Amendment Act introduced a 10% reservation in educational institutions and public employment for Economically Weaker Sections (EWS) among unreserved categories?",
    "பொதுப் பிரிவினரிடையே உள்ள பொருளாதாரத்தில் நலிவடைந்த பிரிவினருக்கு (EWS) கல்வி நிறுவனங்கள் மற்றும் வேலைவாய்ப்பில் 10% இடஒதுக்கீட்டை அறிமுகப்படுத்திய திருத்தச் சட்டம் எது?",
    "100th Constitutional Amendment Act, 2015", "100-வது அரசியலமைப்பு திருத்தச் சட்டம், 2015",
    "101st Constitutional Amendment Act, 2016", "101-வது அரசியலமைப்பு திருத்தச் சட்டம், 2016",
    "102nd Constitutional Amendment Act, 2018", "102-வது அரசியலமைப்பு திருத்தச் சட்டம், 2018",
    "103rd Constitutional Amendment Act, 2019", "103-வது அரசியலமைப்பு திருத்தச் சட்டம், 2019",
    "D",
    "📚 Core Explanation:\nThe 103rd Constitutional Amendment Act, 2019 introduced 10% reservation for Economically Weaker Sections (EWS) by inserting Articles 15(6) and 16(6) into the Constitution.",
    "📚 முதன்மை விளக்கம்:\n2019-ஆம் ஆண்டின் 103-வது அரசியலமைப்பு திருத்தச் சட்டம் சரத்துகள் 15(6) மற்றும் 16(6)-ஐச் சேர்த்து EWS பிரிவினருக்கு 10% இடஒதுக்கீட்டை அறிமுகப்படுத்தியது.",
    "Option A is incorrect; 100th Amendment was Land Boundary Agreement.", "விருப்பம் A தவறானது.",
    "Option B is incorrect; 101st Amendment was GST.", "விருப்பம் B தவறானது.",
    "Option C is incorrect; 102nd Amendment was NCBC status.", "விருப்பம் C தவறானது.",
    "Option D is correct; 103rd Amendment introduced 10% EWS reservation.", "விருப்பம் D சரியானது.",
    "💡 TNPSC Tip: In Janhit Abhiyan v. Union of India (2022), a 5-judge SC bench (3:2) upheld the validity of 103rd EWS Amendment.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: ஜன்ஹித் அபியான் வழக்கில் (2022) 5 நீதிபதிகள் அமர்வு 103-வது EWS திருத்தத்தை உறுதி செய்தது.",
    "📖 Revision Fact: EWS reservation applies over and above the existing 50% reservation for SCs, STs, and OBCs.",
    "📖 திருத்தல் செய்தி: EWS இடஒதுக்கீடு ஏற்கனவே உள்ள 50% இடஒதுக்கீட்டிற்கு கூடுதலாகப் பொருந்தும்.",
    "Remember", "High", ["103rd Amendment", "EWS Reservation", "Janhit Abhiyan Case"]
)

# Q45 - Ans: D
add_p2(
    "polity_amendments_gt_045", "Medium", "single_choice",
    "Under Article 368, which of the following actions can be taken by the President when a Constitutional Amendment Bill passed by Parliament is presented to him?",
    "நாடாளுமன்றத்தால் நிறைவேற்றப்பட்ட அரசியலமைப்பு திருத்த மசோதா குடியரசுத் தலைவரிடம் சமர்ப்பிக்கப்படும் போது சரத்து 368-ன் கீழ் அவர் என்ன நடவடிக்கை எடுக்க முடியும்?",
    "He can withhold his assent to the Bill.", "அவர் மசோதாவிற்கான ஒப்புதலை நிறுத்தி வைக்கலாம்.",
    "He can return the Bill for reconsideration of Parliament.", "அவர் மசோதாவை நாடாளுமன்றத்தின் மறுபரிசீலனைக்குத் திருப்பியனுப்பலாம்.",
    "He can keep the Bill pending indefinitely using Pocket Veto.", "பாக்கெட் வீட்டோவைப் பயன்படுத்தி மசோதாவை காலவரையின்றி நிலுவையில் வைக்கலாம்.",
    "He MUST give his assent to the Bill without withholding or returning it.", "அவர் ஒப்புதலை நிறுத்தவோ அல்லது திருப்பியனுப்பவோ செய்யாமல் கட்டாயமாக ஒப்புதல் அளிக்க வேண்டும்.",
    "D",
    "📚 Core Explanation:\nUnder Article 368 (as amended by the 24th Amendment Act, 1971), when a Constitutional Amendment Bill is presented to the President, he MUST give his assent to the Bill. He can neither withhold assent nor return the bill for reconsideration.",
    "📚 முதன்மை விளக்கம்:\nசரத்து 368-ன் படி (24-வது திருத்தத்தால் திருத்தப்பட்டது), அரசியலமைப்பு திருத்த மசோதா குடியரசுத் தலைவரிடம் சமர்ப்பிக்கப்படும் போது அவர் கட்டாயமாக ஒப்புதல் அளிக்க வேண்டும். அவர் ஒப்புதலை நிறுத்தவோ அல்லது திருப்பியனுப்பவோ முடியாது.",
    "Option A is incorrect because President cannot withhold assent.", "விருப்பம் A தவறானது.",
    "Option B is incorrect because President cannot return amendment bills.", "விருப்பம் B தவறானது.",
    "Option C is incorrect because Pocket Veto is not applicable to amendment bills.", "விருப்பம் C தவறானது.",
    "Option D is correct as Presidential assent is mandatory.", "விருப்பம் D சரியானது.",
    "💡 TNPSC Tip: Contrast: President CAN return Ordinary Bills once, but CANNOT return Money Bills or Constitutional Amendment Bills.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: குடியரசுத் தலைவர் சாதாரண மசோதாவைத் திருப்புக அனுப்பலாம், ஆனால் பண மசோதா மற்றும் அரசியலமைப்பு திருத்த மசோதாவைத் திருப்பியனுப்ப முடியாது.",
    "📖 Revision Fact: 24th Amendment substituted 'shall give his assent' in Article 368.",
    "📖 திருத்தல் செய்தி: 24-வது திருத்தம் 'ஒப்புதல் அளிக்க வேண்டும்' என சரத்து 368-ல் மாற்றியது.",
    "Understand", "High", ["Article 368", "Presidential Veto Disallowed", "Mandatory Assent"]
)

# Q46 - Ans: D
add_p2(
    "polity_amendments_gt_046", "Hard", "statement",
    "Consider the following comparison between an Ordinary Bill and a Constitutional Amendment Bill:\n1. An Ordinary Bill requires a simple majority in Parliament, whereas a Constitutional Amendment Bill under Article 368 requires a special majority.\n2. Prior recommendation of the President is required for introducing a Money Bill, but NOT for a Constitutional Amendment Bill.\n3. In case of a deadlock between Lok Sabha and Rajya Sabha, a Joint Sitting can be called for an Ordinary Bill, but CANNOT be called for a Constitutional Amendment Bill.\nWhich of the statements given above are correct?",
    "சாதாரண மசோதா மற்றும் அரசியலமைப்பு திருத்த மசோதாவிற்கு இடையிலான ஒப்பீடு குறித்த பின்வரும் கூற்றுகளை ஆராய்க:\n1. சாதாரண மசோதாவிற்கு எளிய பெரும்பான்மை போதுமானது, ஆனால் சரத்து 368-ன் கீழ் திருத்த மசோதாவிற்கு சிறப்பு பெரும்பான்மை தேவை.\n2. பண மசோதாவை அறிமுகப்படுத்த குடியரசுத் தலைவரின் முன் பரிந்துரை தேவை, ஆனால் அரசியலமைப்பு திருத்த மசோதாவிற்கு தேவையில்லை.\n3. மக்களவை மற்றும் மாநிலங்களவை இடையே முட்டுக்கட்டை ஏற்பட்டால், சாதாரண மசோதாவிற்கு கூட்டு அமர்வு கூட்டப்படலாம், ஆனால் அரசியலமைப்பு திருத்த மசோதாவிற்கு கூட்ட முடியாது.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
    "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
    "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
    "1 and 3 only", "1 மற்றும் 3 மட்டுமே",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "D",
    "📚 Core Explanation:\nAll three statements are CORRECT comparison points between Ordinary Bills / Money Bills and Constitutional Amendment Bills.",
    "📚 முதன்மை விளக்கம்:\nமூன்று கூற்றுகளும் சாதாரண/பண மசோதாக்கள் மற்றும் அரசியலமைப்பு திருத்த மசோதாக்களுக்கு இடையிலான சரியான ஒப்பீடுகளாகும்.",
    "Option A is incomplete.", "விருப்பம் A அரைகுறையானது.",
    "Option B is incomplete.", "விருப்பம் B அரைகுறையானது.",
    "Option C is incomplete.", "விருப்பம் C அரைகுறையானது.",
    "Option D is correct as all three statements are true.", "விருப்பம் D சரியானது.",
    "💡 TNPSC Tip: Both Houses have equal powers regarding Constitutional Amendment Bills.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: அரசியலமைப்பு திருத்த மசோதாக்களில் இரு அவைகளுக்கும் சம அதிகாரம் உண்டு.",
    "📖 Revision Fact: Private members can introduce Constitutional Amendment Bills.",
    "📖 திருத்தல் செய்தி: தனிநபர் உறுப்பினர்களும் திருத்த மசோதாக்களை அறிமுகப்படுத்தலாம்.",
    "Analyze", "High", ["Ordinary Bill vs Amendment Bill", "Procedural Differences"]
)

# Q47 - Ans: A
add_p2(
    "polity_amendments_gt_047", "Medium", "single_choice",
    "In which historic case did an 11-judge bench of the Supreme Court rule by a 6:5 majority that Parliament CANNOT amend Fundamental Rights, giving them a 'transcendental' position?",
    "அடிப்படை உரிமைகளுக்கு 'உன்னதமான' (transcendental) அந்தஸ்தை வழங்கி, நாடாளுமன்றம் அடிப்படை உரிமைகளைத் திருத்த முடியாது என்று 11 நீதிபதிகள் அமர்வு 6:5 பெரும்பான்மையில் தீர்ப்பளித்த வரலாற்றுச் சிறப்புமிக்க வழக்கு எது?",
    "Golaknath v. State of Punjab (1967)", "கோலக்நாத் எதிர் பஞ்சாப் மாநிலம் (1967)",
    "Shankari Prasad v. Union of India (1951)", "சங்கரி பிரசாத் எதிர் இந்திய ஒன்றியம் (1951)",
    "Sajjan Singh v. State of Rajasthan (1965)", "சஜ்ஜன் சிங் எதிர் ராஜஸ்தான் மாநிலம் (1965)",
    "Kesavananda Bharati v. State of Kerala (1973)", "கேசவாநந்த பாரதி எதிர் கேரள மாநிலம் (1973)",
    "A",
    "📚 Core Explanation:\nIn Golaknath v. State of Punjab (1967), an 11-judge bench (6:5 majority) reversed its earlier decisions (Shankari Prasad & Sajjan Singh) and held that Fundamental Rights are given a transcendental and inviolable position, so Parliament cannot amend Part III.",
    "📚 முதன்மை விளக்கம்:\nகோலக்நாத் எதிர் பஞ்சாப் மாநில வழக்கில் (1967), 11 நீதிபதிகள் கொண்ட அமர்வு (6:5 பெரும்பான்மை) அடிப்படை உரிமைகள் உன்னதமானவை என்றும், பகுதி III-ஐ நாடாளுமன்றம் திருத்த முடியாது என்றும் தீர்ப்பளித்தது.",
    "Option A is correct; Golaknath case declared FRs unamendable.", "விருப்பம் A சரியானது.",
    "Option B is incorrect; Shankari Prasad (1951) held Parliament CAN amend FRs.", "விருப்பம் B தவறானது.",
    "Option C is incorrect; Sajjan Singh (1965) upheld Shankari Prasad.", "விருப்பம் C தவறானது.",
    "Option D is incorrect; Kesavananda Bharati (1973) overruled Golaknath.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: 24th Amendment Act 1971 was passed specifically to nullify the Golaknath verdict.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: கோலக்நாத் தீர்ப்பை ரத்து செய்யவே 24-வது திருத்தச் சட்டம் 1971 கொண்டுவரப்பட்டது.",
    "📖 Revision Fact: Golaknath decision was prospectively overruled by Kesavananda Bharati case in 1973.",
    "📖 திருத்தல் செய்தி: கோலக்நாத் தீர்ப்பு 1973-ல் கேசவாநந்த பாரதி வழக்கால் மாற்றியமைக்கப்பட்டது.",
    "Remember", "High", ["Golaknath Case", "Fundamental Rights", "Transcendental Position"]
)

# Q48 - Ans: A
add_p2(
    "polity_amendments_gt_048", "Easy", "single_choice",
    "Amending any of the Lists in the Seventh Schedule of the Constitution (Union List, State List, Concurrent List) requires which of the following procedures?",
    "அரசியலமைப்பின் ஏழாவது அட்டவணையில் உள்ள ஏதேனும் ஒரு பட்டியலை (மத்திய, மாநில, பொதுப் பட்டியல்) திருத்துவதற்கு பின்வரும் எந்த நடைமுறை தேவைப்படுகிறது?",
    "Special Majority of Parliament AND Ratification by at least half of the State Legislatures", "நாடாளுமன்றத்தின் சிறப்பு பெரும்பான்மை மற்றும் குறைந்தபட்சம் பாதியளவு மாநில சட்டமன்றங்களின் ஒப்புதல்",
    "Simple Majority of Parliament alone", "நாடாளுமன்றத்தின் எளிய பெரும்பான்மை மட்டுமே",
    "Special Majority of Parliament alone without State Ratification", "மாநில ஒப்புதல் இன்றி நாடாளுமன்றத்தின் சிறப்பு பெரும்பான்மை மட்டுமே",
    "Resolution passed by two-thirds of State Assemblies alone", "இரண்டு பங்கு மாநில சட்டமன்றங்களின் தீர்மானம் மட்டுமே",
    "A",
    "📚 Core Explanation:\nThe Seventh Schedule deals with the distribution of legislative powers between the Union and the States (federal division of powers). Therefore, amending any of the three Lists requires a Special Majority in Parliament along with Ratification by at least half of the State Legislatures by simple majority (Article 368 proviso).",
    "📚 முதன்மை விளக்கம்:\nஏழாவது அட்டவணை மத்திய-மாநில சட்டமன்ற அதிகாரப் பகிர்வைக் கையாள்கிறது. எனவே ஏதேனும் ஒரு பட்டியலைத் திருத்துவதற்கு நாடாளுமன்றத்தின் சிறப்பு பெரும்பான்மையுடன் குறைந்தபட்சம் பாதியளவு மாநில சட்டமன்றங்களின் ஒப்புதலும் தேவை.",
    "Option A is correct as Seventh Schedule affects federal structure.", "விருப்பம் A சரியானது.",
    "Option B is incorrect because simple majority is insufficient for federal provisions.", "விருப்பம் B தவறானது.",
    "Option C is incorrect because state ratification is mandatory for 7th schedule.", "விருப்பம் C தவறானது.",
    "Option D is incorrect because state assemblies alone cannot amend 7th Schedule.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: Federal features (7th Schedule, President election, SC/HC, Art 368) ALWAYS require state ratification.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: கூட்டாட்சி அம்சங்களுக்கு எப்போதும் மாநிலங்களின் ஒப்புதல் தேவை.",
    "📖 Revision Fact: 101st GST Amendment modified 7th Schedule and was ratified by state legislatures.",
    "📖 திருத்தல் செய்தி: 101-வது ஜிஎஸ்டி திருத்தம் 7-வது அட்டவணையைத் திருத்தியதால் மாநில ஒப்புதல் பெறப்பட்டது.",
    "Understand", "High", ["Seventh Schedule", "Federal Provisions", "State Ratification"]
)

# Q49 - Ans: A
add_p2(
    "polity_amendments_gt_049", "Medium", "single_choice",
    "Which of the following provisions of the Constitution can be amended by a SIMPLE MAJORITY of Parliament outside Article 368?",
    "சரத்து 368-க்கு வெளியே நாடாளுமன்றத்தின் எளிய பெரும்பான்மையால் திருத்தப்படக்கூடிய அரசியலமைப்பு விதி எது?",
    "Use of Official Language and Quorum in Parliament", "நாடாளுமன்றத்தில் அலுவல் மொழிப் பயன்பாடு மற்றும் அவைக் கூட்டம் (Quorum)",
    "Directive Principles of State Policy (Part IV)", "அரசு நெறிமுறையுறுத்தும் கோட்பாடுகள் (பகுதி IV)",
    "Extent of executive power of the Union and States", "மத்திய மற்றும் மாநில நிர்வாக அதிகார வரம்பு",
    "Election of the President and its manner", "குடியரசுத் தலைவர் தேர்தல் மற்றும் அதன் முறை",
    "A",
    "📚 Core Explanation:\nOfficial Language usage, Quorum in Parliament, Salaries of MPs, Citizenship rules, Rules of Procedure, and Parliamentary Privileges can all be amended by a SIMPLE MAJORITY of Parliament. These are explicitly excluded from Article 368 scope.",
    "📚 முதன்மை விளக்கம்:\nநாடாளுமன்றத்தில் அலுவல் மொழிப் பயன்பாடு, குவோரம் (அவைக் கூட்டம்), எம்பிக்கள் சம்பளம் போன்றவை நாடாளுமன்றத்தின் எளிய பெரும்பான்மையால் திருத்தப்படுபவை.",
    "Option A is correct as Official Language and Quorum require simple majority.", "விருப்பம் A சரியானது.",
    "Option B is incorrect; DPSP requires Special Majority under Art 368.", "விருப்பம் B தவறானது.",
    "Option C is incorrect; Executive power extent requires Special Majority + State Ratification.", "விருப்பம் C தவறானது.",
    "Option D is incorrect; President election requires Special Majority + State Ratification.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: Simple Majority amendments are NOT deemed to be amendments under Article 368.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: எளிய பெரும்பான்மை திருத்தங்கள் சரத்து 368-ன் கீழ் திருத்தங்களாகக் கருதப்பட மாட்டா.",
    "📖 Revision Fact: Quorum in Parliament is fixed at 1/10th of total members under Article 100(3).",
    "📖 திருத்தல் செய்தி: நாடாளுமன்றக் கூட்டம் நடத்த குறைந்தபட்ச உறுப்பினர் எண்ணிக்கை (Quorum) 1/10 பங்கு ஆகும்.",
    "Understand", "High", ["Simple Majority", "Quorum", "Article 368 Exception"]
)

# Q50 - Ans: A
add_p2(
    "polity_amendments_gt_050", "Medium", "chronology",
    "Arrange the following amendments related to Democratic Decentralisation and Local Self-Government in correct chronological order:\n1. 73rd Amendment Act (Panchayati Raj)\n2. 74th Amendment Act (Municipalities)\n3. 97th Amendment Act (Co-operative Societies)\nSelect the correct code:",
    "ஜனநாயக பரவலாக்கம் மற்றும் உள்ளாட்சி தொடர்பான பின்வரும் திருத்தங்களை சரியான காலவரிசைப்படி அமைக்கவும்:\n1. 73-வது திருத்தச் சட்டம் (பஞ்சாயத்து ராஜ்)\n2. 74-வது திருத்தச் சட்டம் (நகராட்சிகள்)\n3. 97-வது திருத்தச் சட்டம் (கூட்டுறவு சங்கங்கள்)\nசரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
    "1 - 2 - 3", "1 - 2 - 3",
    "2 - 1 - 3", "2 - 1 - 3",
    "1 - 3 - 2", "1 - 3 - 2",
    "3 - 1 - 2", "3 - 1 - 2",
    "A",
    "📚 Core Explanation:\n- 73rd Amendment Act was enacted in 1992 (Part IX, Panchayats).\n- 74th Amendment Act was enacted in 1992 (Part IX-A, Municipalities, came into force after 73rd).\n- 97th Amendment Act was enacted in 2011 (Part IX-B, Co-operatives).\nHence, correct chronological sequence is 1 - 2 - 3.",
    "📚 முதன்மை விளக்கம்:\n- 73-வது திருத்தச் சட்டம் 1992 (பஞ்சாயத்துகள்).\n- 74-வது திருத்தச் சட்டம் 1992 (நகராட்சிகள்).\n- 97-வது திருத்தச் சட்டம் 2011 (கூட்டுறவு சங்கங்கள்).\nசரியான காலவரிசை 1 - 2 - 3.",
    "Option A is correct as 1 (Panchayats 1992) -> 2 (Municipalities 1992) -> 3 (Co-operatives 2011).", "விருப்பம் A சரியானது.",
    "Option B is incorrect.", "விருப்பம் B தவறானது.",
    "Option C is incorrect.", "விருப்பம் C தவறானது.",
    "Option D is incorrect.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: 73rd Act came into force on 24 April 1993; 74th Act came into force on 1 June 1993; 97th Act came into force in 2012.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: 73-வது சட்டம் ஏப்ரல் 24, 1993; 74-வது சட்டம் ஜூன் 1, 1993 அன்று அமலுக்கு வந்தது.",
    "📖 Revision Fact: April 24 is celebrated annually as National Panchayati Raj Day in India.",
    "📖 திருத்தல் செய்தி: ஏப்ரல் 24 இந்தியாவில் தேசிய பஞ்சாயத்து ராஜ் தினமாகக் கொண்டாடப்படுகிறது.",
    "Apply", "High", ["Chronology", "73rd Amendment", "74th Amendment", "97th Amendment"]
)

print("Part 2 questions Q26 to Q50 loaded completely with add_p2.")
