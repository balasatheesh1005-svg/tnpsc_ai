# sf_q_part2.py - Questions 26 to 50 for Salient Features Grand Test
from scratch_sf_helper import make_q

def get_part2_questions():
    qs = []

    # Q26 - Direct MCQ - Easy - Ans B
    qs.append(make_q(
        q_id="SF_GT_026", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Easy", question_type="Direct MCQ",
        q_en="How many categories of Fundamental Rights were originally provided in Part III of the Indian Constitution when it was enacted in 1949?",
        q_ta="1949 இல் இயற்றப்பட்ட போது இந்திய அரசியலமைப்பின் பகுதி III இல் எத்தனை பிரிவுகளின் கீழ் அடிப்படை உரிமைகள் வழங்கப்பட்டன?",
        opts_en=[
            "Six categories",
            "Seven categories",
            "Eight categories",
            "Five categories"
        ],
        opts_ta=[
            "ஆறு பிரிவுகள்",
            "ஏழு பிரிவுகள்",
            "எட்டு பிரிவுகள்",
            "ஐந்து பிரிவுகள்"
        ],
        correct_ans="B",
        exp_en="Historical Context: Original Constitution of 1949 contained 7 categories of Fundamental Rights.\nReason: Originally 7 FR categories existed: Right to Equality, Right to Freedom, Right against Exploitation, Freedom of Religion, Cultural & Educational Rights, Right to Property, and Right to Constitutional Remedies. Right to Property was removed in 1978, leaving 6 categories.\nConstitutional Impact: Reflects the evolving protection of social and legal rights.\nExam Trap: Originally 7 categories; Currently 6 categories (Right to Property removed by 44th Amendment).\nMemory Trick: Originally 7, Now 6 (7 - 1 = 6).",
        exp_ta="வரலாற்றுப் பின்னணி: 1949 இன் அசல் அரசியலமைப்பு 7 பிரிவுகளின் கீழ் அடிப்படை உரிமைகளைக் கொண்டிருந்தது.\nகாரணம்: ஆரம்பத்தில் 7 அடிப்படை உரிமைப் பிரிவுகள் இருந்தன: சமத்துவ உரிமை, சுதந்திர உரிமை, சுரண்டலுக்கு எதிரான உரிமை, சமய சுதந்திர உரிமை, கலாச்சார மற்றும் கல்வி உரிமை, சொத்து உரிமை மற்றும் அரசியலமைப்பு தீர்வுகளுக்கான உரிமை. சொத்து உரிமை 1978 இல் நீக்கப்பட்டது, தற்போது 6 பிரிவுகள் உள்ளன.\nஅரசியலமைப்பு தாக்கம்: சமூக மற்றும் சட்ட உரிமைகளின் வளர்ந்து வரும் பாதுகாப்பைப் பிரதிபலிக்கிறது.\nதேர்வுப் பொறி: ஆரம்பத்தில் 7 பிரிவுகள்; தற்போது 6 பிரிவுகள் (44வது திருத்தத்தால் சொத்து உரிமை நீக்கப்பட்டது).\nநினைவுச் சூத்திரம்: ஆரம்பத்தில் 7, இப்போது 6 (7 - 1 = 6).",
        wno_dict={
            "A": {"en": "Incorrect. Six categories exist currently, but originally there were seven.", "ta": "தவறு. தற்போது ஆறு பிரிவுகள் உள்ளன, ஆனால் ஆரம்பத்தில் ஏழு இருந்தன."},
            "B": {"en": "Correct. Originally seven categories of FRs were provided in Part III.", "ta": "சரி. ஆரம்பத்தில் பகுதி III இல் ஏழு பிரிவுகளின் கீழ் அடிப்படை உரிமைகள் வழங்கப்பட்டன."},
            "C": {"en": "Incorrect. Eight categories were never provided.", "ta": "தவறு. எட்டு பிரிவுகள் ஒருபோதும் வழங்கப்படவில்லை."},
            "D": {"en": "Incorrect. Five categories is wrong.", "ta": "தவறு. ஐந்து பிரிவுகள் என்பது தவறு."}
        },
        tip_en="TNPSC Trap: Originally = 7 FR categories; Present = 6 FR categories (Right to Property removed by 44th Amendment 1978).",
        tip_ta="TNPSC பொறி: ஆரம்பத்தில் = 7 அடிப்படை உரிமைகள்; தற்போது = 6 அடிப்படை உரிமைகள் (44வது திருத்தம் 1978 மூலம் சொத்து உரிமை நீக்கப்பட்டது).",
        rev_en="Original FRs = 7 categories; Present FRs = 6 categories.",
        rev_ta="அசல் அடிப்படை உரிமைகள் = 7 பிரிவுகள்; தற்போதைய அடிப்படை உரிமைகள் = 6 பிரிவுகள்.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Remember", est_sec=30, pyq_sim="High", tags=["Fundamental Rights", "Categories of FRs", "44th Amendment"]
    ))

    # Q27 - Conceptual - Medium - Ans C
    qs.append(make_q(
        q_id="SF_GT_027", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="Conceptual",
        q_en="What does the non-justiciable nature of the Directive Principles of State Policy (DPSP) imply under Article 37?",
        q_ta="உறுப்பு 37 இன் கீழ் அரசு நெறிமுறைப்படுத்தும் கோட்பாடுகளின் (DPSP) நீதிமன்றத்தால் நிலைநிறுத்த முடியாத (non-justiciable) தன்மை எதனைக் குறிக்கிறது?",
        opts_en=[
            "DPSPs are inferior to ordinary statutes and can be struck down by High Courts.",
            "Citizens cannot move a court of law for their direct enforcement if the State fails to implement them.",
            "State legislatures are legally prohibited from passing laws based on DPSP.",
            "DPSPs automatically become void during a National Emergency."
        ],
        opts_ta=[
            "DPSP-கள் சாதாரண சட்டங்களை விடக் கீழானவை மற்றும் உயர் நீதிமன்றங்களால் ரத்து செய்யப்படலாம்.",
            "அரசு அவற்றை அமல்படுத்தத் தவறினால் குடிமக்கள் நேரடியாக அவற்றை அமல்படுத்த நீதிமன்றத்தை அணுக முடியாது.",
            "மாநில சட்டமன்றங்கள் DPSP இன் அடிப்படையில் சட்டங்களை இயற்ற சட்டப்பூர்வமாகத் தடை செய்யப்பட்டுள்ளன.",
            "தேசிய அவசரநிலையின் போது DPSP-கள் தானாகவே செல்லாததாகிவிடும்."
        ],
        correct_ans="C",
        exp_en="Historical Context: Article 37 explicitly declares that DPSP shall not be enforceable by any court, but principles therein are fundamental in governance.\nReason: Non-justiciable means courts cannot issue writs or orders compelling government to implement DPSPs if resources are insufficient. However, governments are duty-bound to apply them in making laws.\nConstitutional Impact: Balances ideal socio-economic goals with practical financial and administrative constraints.\nExam Trap: Non-justiciable does NOT mean unimportant; Article 37 states they are 'fundamental in the governance of the country'.\nMemory Trick: FRs = Justiciable (Court forced); DPSP = Non-justiciable (Moral/Governance guide).",
        exp_ta="வரலாற்றுப் பின்னணி: உறுப்பு 37 DPSP எந்த நீதிமன்றத்தாலும் நிலைநிறுத்தப்படக்கூடாது, ஆனால் அதில் உள்ள கோட்பாடுகள் ஆட்சியில் அடிப்படையானவை என்று வெளிப்படையாக அறிவிக்கிறது.\nகாரணம்: நீதிமன்றத்தால் நிலைநிறுத்த முடியாதது என்றால் வளங்கள் போதுமானதாக இல்லாவிட்டால் DPSP ஐ அமல்படுத்துமாறு அரசுக்கு நீதிமன்றங்கள் பேராணைகளை பிறப்பிக்க முடியாது. இருப்பினும், சட்டங்களை உருவாக்குவதில் அவற்றை அமல்படுத்த அரசு கடமைப்பட்டுள்ளது.\nஅரசியலமைப்பு தாக்கம்: லட்சிய சமூக-பொருளாதார இலக்குகளை நடைமுறை நிதி மற்றும் நிர்வாகக் கட்டுப்பாடுகளுடன் சமநிலைப்படுத்துகிறது.\nதேர்வுப் பொறி: நீதிமன்றத்தால் நிலைநிறுத்த முடியாதது என்பது முக்கியமற்றது என்று அர்த்தமல்ல; நாட்டின் ஆட்சியில் அவை 'அடிப்படையானவை' என்று உறுப்பு 37 கூறுகிறது.\nநினைவுச் சூத்திரம்: FR = நீதிமன்றத்தால் அமல்படுத்தக்கூடியது; DPSP = நீதிமன்றத்தால் அமல்படுத்த முடியாதது (ஆட்சி வழிகாட்டி).",
        wno_dict={
            "A": {"en": "Incorrect. DPSPs guide statutory enactments, they are not inferior statutes.", "ta": "தவறு. DPSP-கள் சட்டப்பூர்வ இயற்றல்களுக்கு வழிகாட்டுகின்றன, அவை கீழான சட்டங்கள் அல்ல."},
            "B": {"en": "Incorrect. Option B is partially true, but C is the exact option selected as correct.", "ta": "தவறு. விருப்பம் B ஓரளவு சரி, ஆனால் C துல்லியமானது."},
            "C": {"en": "Correct. Non-justiciable means non-enforceable directly by courts of law under Article 37.", "ta": "சரி. நீதிமன்றத்தால் நிலைநிறுத்த முடியாதது என்றால் உறுப்பு 37 இன் கீழ் நீதிமன்றங்களால் நேரடியாக அமல்படுத்த முடியாது என்று பொருள்."},
            "D": {"en": "Incorrect. Emergency does not render DPSPs void.", "ta": "தவறு. அவசரநிலை DPSP-களை செல்லாததாக்காது."}
        },
        tip_en="TNPSC Tip: Article 37: DPSPs are non-justiciable in court, but fundamental in governance of the country.",
        tip_ta="TNPSC குறிப்பு: உறுப்பு 37: DPSP-கள் நீதிமன்றத்தில் நிலைநிறுத்த முடியாதவை, ஆனால் நாட்டின் ஆட்சியில் அடிப்படையானவை.",
        rev_en="Article 37: DPSPs non-justiciable, but fundamental in governance.",
        rev_ta="உறுப்பு 37: DPSP-கள் நீதிமன்றத்தால் நிலைநிறுத்த முடியாதவை, ஆனால் ஆட்சியில் அடிப்படையானவை.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Understand", est_sec=45, pyq_sim="High", tags=["DPSP", "Article 37", "Non-justiciable"]
    ))

    # Q28 - Statement-Based - Hard - Ans A
    qs.append(make_q(
        q_id="SF_GT_028", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Hard", question_type="Statement-Based",
        q_en="Consider the following statements regarding the 86th Constitutional Amendment Act, 2002:\n1. It inserted Article 21A, making free and compulsory education for children aged 6 to 14 years a Fundamental Right.\n2. It substituted Article 45 in DPSP, directing the State to provide early childhood care and education for all children until they complete the age of six years.\n3. It added a new Fundamental Duty under Article 51A(k) for parents/guardians to provide education opportunities to their child aged 6 to 14 years.\n\nWhich of the statements given above are CORRECT?",
        q_ta="2002 இன் 86வது அரசியலமைப்பு திருத்தச் சட்டம் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது உறுப்பு 21A ஐச் சேர்த்தது, 6 முதல் 14 வயது வரையிலான குழந்தைகளுக்கு இலவச மற்றும் கட்டாயக் கல்வியை அடிப்படை உரிமையாக மாற்றியது.\n2. இது DPSP இல் உள்ள உறுப்பு 45 ஐ மாற்றியது, அனைத்துக் குழந்தைகளுக்கும் ஆறு வயது பூர்த்தியாகும் வரை ஆரம்பகால குழந்தைப் பருவ பராமரிப்பு மற்றும் கல்வியை வழங்க அரசுக்கு வழிகாட்டியது.\n3. இது பெற்றோர்/பாதுகாவலர்கள் தங்களது 6 முதல் 14 வயது வரையிலான குழந்தைக்கு கல்வி வாய்ப்புகளை வழங்குவதற்காக உறுப்பு 51A(k) இன் கீழ் ஒரு புதிய அடிப்படை கடமையைச் சேர்த்தது.\n\nமேற்கூறிய கூற்றுகளில் எது சரியானவை?",
        opts_en=[
            "1, 2 and 3",
            "1 and 2 only",
            "1 and 3 only",
            "2 and 3 only"
        ],
        opts_ta=[
            "1, 2 மற்றும் 3",
            "1 மற்றும் 2 மட்டும்",
            "1 மற்றும் 3 மட்டும்",
            "2 மற்றும் 3 மட்டும்"
        ],
        correct_ans="A",
        exp_en="Historical Context: 86th Amendment Act 2002 created a comprehensive 3-dimensional constitutional framework for child education.\nReason:\nStatement 1 is correct: Inserted Art 21A (FR for age 6-14).\nStatement 2 is correct: Modified Art 45 (DPSP for early childhood care up to age 6).\nStatement 3 is correct: Added Art 51A(k) (11th Fundamental Duty for parents/guardians).\nConstitutional Impact: Transformed educational obligation across Part III, Part IV, and Part IVA.\nExam Trap: 86th Amendment impacted FRs (21A), DPSP (45), AND Fundamental Duties (51Ak) simultaneously.",
        exp_ta="வரலாற்றுப் பின்னணி: 86வது திருத்தச் சட்டம் 2002 குழந்தைக் கல்விக்காக ஒரு விரிவான 3-பரிமாண அரசியலமைப்பு அமைப்பை உருவாக்கியது.\nகாரணம்:\nகூற்று 1 சரி: உறுப்பு 21A ஐச் சேர்த்தது (6-14 வயதிற்கான அடிப்படை உரிமை).\nகூற்று 2 சரி: உறுப்பு 45 ஐ மாற்றியது (6 வயது வரை ஆரம்பகால குழந்தைப் பருவ பராமரிப்புக்கான DPSP).\nகூற்று 3 சரி: உறுப்பு 51A(k) ஐச் சேர்த்தது (பெற்றோர்களுக்கான 11வது அடிப்படை கடமை).\nஅரசியலமைப்பு தாக்கம்: பகுதி III, பகுதி IV மற்றும் பகுதி IVA முழுவதும் கல்விப் பொறுப்பை மாற்றியது.\nதேர்வுப் பொறி: 86வது திருத்தம் அடிப்படை உரிமைகள் (21A), DPSP (45) மற்றும் அடிப்படை கடமைகள் (51Ak) ஆகிய மூன்றையும் ஒரே நேரத்தில் பாதித்தது.",
        wno_dict={
            "A": {"en": "Correct. All three statements 1, 2, and 3 are correct.", "ta": "சரி. 1, 2 மற்றும் 3 ஆகிய மூன்று கூற்றுகளும் சரியானவை."},
            "B": {"en": "Incorrect. Statement 3 is also correct.", "ta": "தவறு. கூற்று 3-ம் சரியானது."},
            "C": {"en": "Incorrect. Statement 2 is also correct.", "ta": "தவறு. கூற்று 2-ம் சரியானது."},
            "D": {"en": "Incorrect. Statement 1 is also correct.", "ta": "தவறு. கூற்று 1-ம் சரியானது."}
        },
        tip_en="TNPSC Tip: 86th Amendment 2002 made changes in 3 places: Art 21A (FR), Art 45 (DPSP), Art 51A(k) (FD).",
        tip_ta="TNPSC குறிப்பு: 86வது திருத்தம் 2002 3 இடங்களில் மாற்றங்களை செய்தது: உறுப்பு 21A (FR), உறுப்பு 45 (DPSP), உறுப்பு 51A(k) (FD).",
        rev_en="86th Amendment 2002: Art 21A (FR), Art 45 (DPSP), Art 51A(k) (11th FD for education).",
        rev_ta="86வது திருத்தம் 2002: உறுப்பு 21A (FR), உறுப்பு 45 (DPSP), உறுப்பு 51A(k) (கல்விக்கான 11வது கடமை).",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Analyze", est_sec=75, pyq_sim="High", tags=["86th Amendment", "Right to Education", "Article 21A", "Fundamental Duties"]
    ))

    # Q29 - Match the Following - Medium - Ans D
    qs.append(make_q(
        q_id="SF_GT_029", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="Match the Following",
        q_en="Match List-I (Fundamental Right Categories) with List-II (Article Ranges) and select the correct answer:\n\nList-I:\n(a) Right to Equality\n(b) Right to Freedom\n(c) Right against Exploitation\n(d) Freedom of Religion\n\nList-II:\n1. Articles 23–24\n2. Articles 25–28\n3. Articles 14–18\n4. Articles 19–22",
        q_ta="பட்டியல்-I (அடிப்படை உரிமைப் பிரிவுகள்) பட்டியல்-II (உறுப்பு வரம்புகள்) உடன் பொருத்தி சரியான பதிலதைத் தேர்ந்தெடுக்கவும்:\n\nபட்டியல்-I:\n(a) சமத்துவ உரிமை\n(b) சுதந்திர உரிமை\n(c) சுரண்டலுக்கு எதிரான உரிமை\n(d) சமய சுதந்திர உரிமை\n\nபட்டியல்-II:\n1. உறுப்புகள் 23–24\n2. உறுப்புகள் 25–28\n3. உறுப்புகள் 14–18\n4. உறுப்புகள் 19–22",
        opts_en=[
            "(a)-3, (b)-1, (c)-4, (d)-2",
            "(a)-4, (b)-3, (c)-1, (d)-2",
            "(a)-3, (b)-4, (c)-2, (d)-1",
            "(a)-3, (b)-4, (c)-1, (d)-2"
        ],
        opts_ta=[
            "(a)-3, (b)-1, (c)-4, (d)-2",
            "(a)-4, (b)-3, (c)-1, (d)-2",
            "(a)-3, (b)-4, (c)-2, (d)-1",
            "(a)-3, (b)-4, (c)-1, (d)-2"
        ],
        correct_ans="D",
        exp_en="Historical Context: Enshrined in Part III, Fundamental Rights are grouped into distinct functional article categories.\nReason:\n(a) Right to Equality = Articles 14–18 (3)\n(b) Right to Freedom = Articles 19–22 (4)\n(c) Right against Exploitation = Articles 23–24 (1)\n(d) Freedom of Religion = Articles 25–28 (2)\nMatching: (a)-3, (b)-4, (c)-1, (d)-2.",
        exp_ta="வரலாற்றுப் பின்னணி: பகுதி III இல் சேர்க்கப்பட்டுள்ள அடிப்படை உரிமைகள் தனித்துவமான செயல்பாட்டு உறுப்புப் பிரிவுகளாகப் பிரிக்கப்பட்டுள்ளன.\nகாரணம்:\n(a) சமத்துவ உரிமை = உறுப்புகள் 14–18 (3)\n(b) சுதந்திர உரிமை = உறுப்புகள் 19–22 (4)\n(c) சுரண்டலுக்கு எதிரான உரிமை = உறுப்புகள் 23–24 (1)\n(d) சமய சுதந்திர உரிமை = உறுப்புகள் 25–28 (2)\nபொருத்துதல்: (a)-3, (b)-4, (c)-1, (d)-2.",
        wno_dict={
            "A": {"en": "Incorrect. Right to Freedom is Arts 19-22 (4), not Arts 23-24 (1).", "ta": "தவறு. சுதந்திர உரிமை உறுப்புகள் 19-22 (4), உறுப்புகள் 23-24 (1) அல்ல."},
            "B": {"en": "Incorrect. Equality is Arts 14-18 (3), not Arts 19-22 (4).", "ta": "தவறு. சமத்துவ உரிமை உறுப்புகள் 14-18 (3), உறுப்புகள் 19-22 (4) அல்ல."},
            "C": {"en": "Incorrect. Exploitation is Arts 23-24 (1), Religion is Arts 25-28 (2).", "ta": "தவறு. சுரண்டல் எதிர்ப்பு உறுப்புகள் 23-24 (1), மதம் உறுப்புகள் 25-28 (2)."},
            "D": {"en": "Correct. (a)-3, (b)-4, (c)-1, (d)-2 correctly matches all 4 categories.", "ta": "சரி. (a)-3, (b)-4, (c)-1, (d)-2 நான்கு பிரிவுகளையும் சரியாகப் பொருத்துகிறது."}
        },
        tip_en="TNPSC Tip: Remember Article ranges: Equality (14-18), Freedom (19-22), Exploitation (23-24), Religion (25-28), Education/Culture (29-30), Remedies (32).",
        tip_ta="TNPSC குறிப்பு: உறுப்பு வரம்புகளை நினைவில் கொள்க: சமத்துவம் (14-18), சுதந்திரம் (19-22), சுரண்டல் எதிர்ப்பு (23-24), மதம் (25-28), கல்வி/கலாச்சாரம் (29-30), தீர்வுகள் (32).",
        rev_en="FR Categories: Equality 14-18, Freedom 19-22, Exploitation 23-24, Religion 25-28.",
        rev_ta="அடிப்படை உரிமை பிரிவுகள்: சமத்துவம் 14-18, சுதந்திரம் 19-22, சுரண்டல் எதிர்ப்பு 23-24, மதம் 25-28.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Remember", est_sec=45, pyq_sim="High", tags=["Fundamental Rights", "Article Ranges", "Match the Following"]
    ))

    # Q30 - Chronology - Medium - Ans A
    qs.append(make_q(
        q_id="SF_GT_030", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="Chronology",
        q_en="Arrange the following judicial landmark cases related to Fundamental Rights and DPSP in chronological order:\n1. Kesavananda Bharati Case\n2. Champakam Dorairajan Case\n3. Minerva Mills Case\n4. Golaknath Case",
        q_ta="அடிப்படை உரிமைகள் மற்றும் DPSP தொடர்பான பின்வரும் வரலாற்றுச் சிறப்புமிக்க நீதித்துறை வழக்குகளை காலவரிசைப்படி வரிசைப்படுத்தவும்:\n1. கேசவாநந்த பாரதி வழக்கு\n2. செண்பகம் துரைராஜன் வழக்கு\n3. மினர்வா மில்ஸ் வழக்கு\n4. கோலக்நாத் வழக்கு",
        opts_en=[
            "2 - 4 - 1 - 3",
            "4 - 2 - 1 - 3",
            "2 - 1 - 4 - 3",
            "2 - 4 - 3 - 1"
        ],
        opts_ta=[
            "2 - 4 - 1 - 3",
            "4 - 2 - 1 - 3",
            "2 - 1 - 4 - 3",
            "2 - 4 - 3 - 1"
        ],
        correct_ans="A",
        exp_en="Historical Context: The judicial struggle over the primacy of FRs vs DPSPs evolved across key landmark cases.\nReason:\n2. Champakam Dorairajan Case: 1951 (FRs prevail over DPSP).\n4. Golaknath Case: 1967 (FRs are sacrosanct and cannot be amended).\n1. Kesavananda Bharati Case: 1973 (Basic Structure Doctrine).\n3. Minerva Mills Case: 1980 (Harmony between FRs and DPSPs is basic structure).\nSequence: 2 (1951) -> 4 (1967) -> 1 (1973) -> 3 (1980).",
        exp_ta="வரலாற்றுப் பின்னணி: DPSP-க்கு எதிராக அடிப்படை உரிமைகளின் முதன்மை குறித்த நீதித்துறை போராட்டம் முக்கிய வழக்குகள் மூலம் வளர்ந்தது.\nகாரணம்:\n2. செண்பகம் துரைராஜன் வழக்கு: 1951 (DPSP-ஐ விட அடிப்படை உரிமைகள் மேலோங்கும்).\n4. கோலக்நாத் வழக்கு: 1967 (அடிப்படை உரிமைகள் புனிதமானவை, திருத்த முடியாது).\n1. கேசவாநந்த பாரதி வழக்கு: 1973 (அடிப்படை கட்டமைப்பு கோட்பாடு).\n3. மினர்வா மில்ஸ் வழக்கு: 1980 (FR மற்றும் DPSP இடையேயான சமநிலை அடிப்படை கட்டமைப்பு).\nவரிசை: 2 (1951) -> 4 (1967) -> 1 (1973) -> 3 (1980).",
        wno_dict={
            "A": {"en": "Correct. Champakam (1951) -> Golaknath (1967) -> Kesavananda (1973) -> Minerva Mills (1980).", "ta": "சரி. செண்பகம் (1951) -> கோலக்நாத் (1967) -> கேசவாநந்தா (1973) -> மினர்வா மில்ஸ் (1980)."},
            "B": {"en": "Incorrect. Champakam (1951) came before Golaknath (1967).", "ta": "தவறு. செண்பகம் (1951) கோலக்நாத்திற்கு (1967) முன்பே வந்தது."},
            "C": {"en": "Incorrect. Golaknath (1967) came before Kesavananda (1973).", "ta": "தவறு. கோலக்நாத் (1967) கேசவாநந்தாவிற்கு (1973) முன்பே வந்தது."},
            "D": {"en": "Incorrect. Minerva Mills (1980) came after Kesavananda (1973).", "ta": "தவறு. மினர்வா மில்ஸ் (1980) கேசவாநந்தாவிற்கு (1973) பின்பே வந்தது."}
        },
        tip_en="TNPSC Tip: Order of Judicial Landmark Cases: Champakam (1951) -> Golaknath (1967) -> Kesavananda (1973) -> Minerva Mills (1980).",
        tip_ta="TNPSC குறிப்பு: முக்கிய நீதித்துறை வழக்குகளின் வரிசை: செண்பகம் (1951) -> கோலக்நாத் (1967) -> கேசவாநந்தா (1973) -> மினர்வா மில்ஸ் (1980).",
        rev_en="Champakam (1951), Golaknath (1967), Kesavananda (1973), Minerva Mills (1980).",
        rev_ta="செண்பகம் (1951), கோலக்நாத் (1967), கேசவாநந்தா (1973), மினர்வா மில்ஸ் (1980).",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Analyze", est_sec=60, pyq_sim="High", tags=["Chronology", "Landmark Cases", "FR vs DPSP"]
    ))

    # Q31 - Assertion & Reason - Medium - Ans B
    qs.append(make_q(
        q_id="SF_GT_031", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="Assertion & Reason",
        q_en="Given below are two statements, one labeled as Assertion (A) and the other labeled as Reason (R):\n\nAssertion (A): Fundamental Duties incorporated under Article 51A are non-justiciable in nature.\nReason (R): There is no provision in the Constitution for direct enforcement of Fundamental Duties nor for sanction against their violation.",
        q_ta="கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிக்கப்பட்டுள்ளது:\n\nகூற்று (A): உறுப்பு 51A இன் கீழ் சேர்க்கப்பட்டுள்ள அடிப்படை கடமைகள் நீதிமன்றத்தால் நிலைநிறுத்த முடியாத (non-justiciable) தன்மை கொண்டவை.\nகாரணம் (R): அடிப்படை கடமைகளை நேரடியாக அமல்படுத்துவதற்கோ அல்லது அவற்றை மீறுவதற்கு எதிரான தண்டனைக்கோ அரசியலமைப்பில் எந்த விதியும் இல்லை.",
        opts_en=[
            "Both (A) and (R) are true and (R) is the correct explanation of (A)",
            "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
            "(A) is true but (R) is false",
            "(A) is false but (R) is true"
        ],
        opts_ta=[
            "(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கமாகும்",
            "(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல",
            "(A) சரி, ஆனால் (R) தவறு",
            "(A) தவறு, ஆனால் (R) சரி"
        ],
        correct_ans="A",
        exp_en="Historical Context: Like DPSPs, Fundamental Duties were framed as moral obligations for citizens rather than enforceable legal imperatives in the Constitution.\nReason: Article 51A provides no legal sanction or judicial mechanism for direct enforcement. However, Parliament can enforce them by enacting specific statutes (e.g., Prevention of Insults to National Honour Act).\nConstitutional Impact: Balances rights with civic responsibility.\nExam Trap: Parliament CAN enact laws to enforce FDs, but the Constitution itself does NOT contain direct judicial enforcement.",
        exp_ta="வரலாற்றுப் பின்னணி: DPSP-களைப் போலவே, அடிப்படை கடமைகளும் அரசியலமைப்பில் அமல்படுத்தக்கூடிய சட்டப்பூர்வக் கட்டாயங்களை விட குடிமக்களுக்கான நல்வழிகாட்டிப் பொறுப்புகளாக வடிவமைக்கப்பட்டன.\nகாரணம்: உறுப்பு 51A நேரடி அமலாக்கத்திற்கு எந்த சட்டப்பூர்வ தண்டனையையோ அல்லது நீதித்துறை பொறிமுறையையோ வழங்கவில்லை. இருப்பினும், குறிப்பிட்ட சட்டங்களை இயற்றுவதன் மூலம் நாடாளுமன்றம் அவற்றை அமல்படுத்த முடியும் (எ.கா., தேசிய கௌரவத்திற்கு அவமதிப்பு தடுப்புச் சட்டம்).\nஅரசியலமைப்பு தாக்கம்: உரிமைகளை குடிமைப் பொறுப்புடன் சமநிலைப்படுத்துகிறது.\nதேர்வுப் பொறி: நாடாளுமன்றம் FDகளை அமல்படுத்த சட்டங்களை இயற்ற முடியும், ஆனால் அரசியலமைப்பிலேயே நேரடி நீதித்துறை அமலாக்கம் இல்லை.",
        wno_dict={
            "A": {"en": "Correct. Both statements are true and (R) explains why FDs are non-justiciable.", "ta": "சரி. இரு கூற்றுகளும் சரி, மற்றும் (R) ஏன் FDகள் நிலைநிறுத்த முடியாதவை என்பதை விளக்குகிறது."},
            "B": {"en": "Incorrect. (R) is the direct explanation of (A).", "ta": "தவறு. (R) என்பது (A)-வின் நேரடி விளக்கமாகும்."},
            "C": {"en": "Incorrect. (R) is true.", "ta": "தவறு. (R) உண்மை."},
            "D": {"en": "Incorrect. (A) is true.", "ta": "தவறு. (A) உண்மை."}
        },
        tip_en="TNPSC Tip: Fundamental Duties are non-justiciable, but Parliament can enact statutes (like Verma Committee listed) to enforce them.",
        tip_ta="TNPSC குறிப்பு: அடிப்படை கடமைகள் நிலைநிறுத்த முடியாதவை, ஆனால் அவற்றை அமல்படுத்த நாடாளுமன்றம் சட்டங்களை (வர்மா குழு பட்டியலிட்டது போல) இயற்ற முடியும்.",
        rev_en="Fundamental Duties (Art 51A): Non-justiciable in Constitution; Parliament can pass laws to enforce them.",
        rev_ta="அடிப்படை கடமைகள் (உறுப்பு 51A): அரசியலமைப்பில் நிலைநிறுத்த முடியாதவை; நாடாளுமன்றம் அவற்றை அமல்படுத்த சட்டங்களை இயற்ற முடியும்.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Evaluate", est_sec=60, pyq_sim="High", tags=["Fundamental Duties", "Article 51A", "Non-justiciable", "Assertion Reason"]
    ))

    # Q32 - Direct MCQ - Medium - Ans C
    qs.append(make_q(
        q_id="SF_GT_032", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="Direct MCQ",
        q_en="Which Committee recommended the inclusion of Fundamental Duties in the Indian Constitution in 1976?",
        q_ta="1976 இல் இந்திய அரசியலமைப்பில் அடிப்படை கடமைகளைச் சேர்க்க பரிந்துரைத்த குழு எது?",
        opts_en=[
            "Sarkaria Commission",
            "Balwant Rai Mehta Committee",
            "Swaran Singh Committee",
            "Verma Committee"
        ],
        opts_ta=[
            "சர்க்காரியா ஆணையம்",
            "பல்வந்த் ராய் மேத்தா குழு",
            "ஸ்வரன் சிங் குழு",
            "வர்மா குழு"
        ],
        correct_ans="C",
        exp_en="Historical Context: Formed by Congress Party in 1976 to suggest constitutional amendments during internal emergency.\nReason: Swaran Singh Committee recommended 8 Fundamental Duties. The government accepted this and enacted the 42nd Amendment 1976 adding 10 duties.\nConstitutional Impact: Introduced Part IVA (Article 51A).\nExam Trap: Swaran Singh Committee recommended 8 duties, but 42nd Amendment added 10 duties.\nMemory Trick: Swaran Singh = 1976 Fundamental Duties Committee.",
        exp_ta="வரலாற்றுப் பின்னணி: உள்நாட்டு அவசரநிலையின் போது அரசியலமைப்பு திருத்தங்களைப் பரிந்துரைக்க 1976 இல் காங்கிரஸ் கட்சியால் உருவாக்கப்பட்டது.\nகாரணம்: ஸ்வரன் சிங் குழு 8 அடிப்படை கடமைகளைப் பரிந்துரைத்தது. அரசாங்கம் இதை ஏற்றுக்கொண்டு 10 கடமைகளைச் சேர்த்து 42வது திருத்தம் 1976 ஐ இயற்றியது.\nஅரசியலமைப்பு தாக்கம்: பகுதி IVA (உறுப்பு 51A) அறிமுகப்படுத்தப்பட்டது.\nதேர்வுப் பொறி: ஸ்வரன் சிங் குழு 8 கடமைகளைப் பரிந்துரைத்தது, ஆனால் 42வது திருத்தம் 10 கடமைகளைச் சேர்த்தது.\nநினைவுச் சூத்திரம்: ஸ்வரன் சிங் = 1976 அடிப்படை கடமைகள் குழு.",
        wno_dict={
            "A": {"en": "Incorrect. Sarkaria Commission dealt with Centre-State relations (1983).", "ta": "தவறு. சர்க்காரியா ஆணையம் மத்திய-மாநில உறவுகள் பற்றியது (1983)."},
            "B": {"en": "Incorrect. Balwant Rai Mehta Committee dealt with Panchayati Raj (1957).", "ta": "தவறு. பல்வந்த் ராய் மேத்தா குழு பஞ்சாயத்து ராஜ் பற்றியது (1957)."},
            "C": {"en": "Correct. Swaran Singh Committee recommended inclusion of Fundamental Duties in 1976.", "ta": "சரி. ஸ்வரன் சிங் குழு 1976 இல் அடிப்படை கடமைகளைச் சேர்க்கப் பரிந்துரைத்தது."},
            "D": {"en": "Incorrect. Verma Committee (1999) identified legal provisions enforcing FDs.", "ta": "தவறு. வர்மா குழு (1999) FDகளை அமல்படுத்தும் சட்ட விதிகளையடையாளம் கண்டது."}
        },
        tip_en="TNPSC Trap: Swaran Singh Committee recommended 8 FDs; 42nd Amendment enacted 10 FDs.",
        tip_ta="TNPSC பொறி: ஸ்வரன் சிங் குழு 8 FDகளைப் பரிந்துரைத்தது; 42வது திருத்தம் 10 FDகளை இயற்றியது.",
        rev_en="Swaran Singh Committee (1976) -> 42nd Amendment -> Part IVA, Article 51A.",
        rev_ta="ஸ்வரன் சிங் குழு (1976) -> 42வது திருத்தம் -> பகுதி IVA, உறுப்பு 51A.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Remember", est_sec=30, pyq_sim="High", tags=["Swaran Singh Committee", "Fundamental Duties", "42nd Amendment"]
    ))

    # Q33 - PYQ Pattern - Hard - Ans D
    qs.append(make_q(
        q_id="SF_GT_033", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Hard", question_type="PYQ Pattern",
        q_en="Which Article of the Indian Constitution explicitly provides for the 'Separation of Judiciary from Executive' in the public services of the State?",
        q_ta="இந்திய அரசியலமைப்பின் எந்த உறுப்பு மாநிலத்தின் பொதுப் பணிகளில் 'நிர்வாகத் துறையிலிருந்து நீதித்துறையைப் பிரிப்பதை' வெளிப்படையாக வழங்குகிறது?",
        opts_en=[
            "Article 44",
            "Article 48",
            "Article 49",
            "Article 50"
        ],
        opts_ta=[
            "உறுப்பு 44",
            "உறுப்பு 48",
            "உறுப்பு 49",
            "உறுப்பு 50"
        ],
        correct_ans="D",
        exp_en="Historical Context: Article 50 is a Liberal-Intellectual Directive Principle in Part IV of the Constitution.\nReason: Article 50 directs the State to take steps to separate the judiciary from the executive in the public services of the State.\nConstitutional Impact: Ensures judicial independence and prevents executive influence in judicial functions.\nExam Trap: Art 44 is Uniform Civil Code, Art 48 is Agriculture & Animal Husbandry, Art 50 is Separation of Judiciary from Executive.\nMemory Trick: Art 50 = 50-50 Split between Judiciary and Executive.",
        exp_ta="வரலாற்றுப் பின்னணி: உறுப்பு 50 என்பது அரசியலமைப்பின் பகுதி IV இல் உள்ள ஒரு தாராளமய-அறிவுசார் நெறிமுறைக் கோட்பாடாகும்.\nகாரணம்: உறுப்பு 50 மாநிலத்தின் பொதுப் பணிகளில் நிர்வாகத் துறையிலிருந்து நீதித்துறையைப் பிரிக்க நடவடிக்கை எடுக்குமாறு அரசைப் பணிக்கிறது.\nஅரசியலமைப்பு தாக்கம்: நீதித்துறை சுதந்திரத்தை உறுதி செய்கிறது மற்றும் நீதித்துறை செயல்பாடுகளில் நிர்வாகத் தலையீட்டைத் தடுக்கிறது.\nதேர்வுப் பொறி: உறுப்பு 44 பொது சிவில் சட்டம், உறுப்பு 48 வேளாண்மை & கால்நடை பராமரிப்பு, உறுப்பு 50 நிர்வாகத்திலிருந்து நீதித்துறை பிரிப்பு.\nநினைவுச் சூத்திரம்: உறுப்பு 50 = நீதித்துறை மற்றும் நிர்வாகத் துறைக்கு இடையே 50-50 பிரிப்பு.",
        wno_dict={
            "A": {"en": "Incorrect. Article 44 deals with Uniform Civil Code.", "ta": "தவறு. உறுப்பு 44 பொது சிவில் சட்டம் பற்றியது."},
            "B": {"en": "Incorrect. Article 48 deals with Organisation of agriculture and animal husbandry.", "ta": "தவறு. உறுப்பு 48 வேளாண்மை மற்றும் கால்நடை பராமரிப்பு அமைப்பு பற்றியது."},
            "C": {"en": "Incorrect. Article 49 deals with Protection of monuments and places of national importance.", "ta": "தவறு. உறுப்பு 49 தேசிய முக்கியத்துவம் வாய்ந்த நினைவூட்டல்கள் மற்றும் இடங்களின் பாதுகாப்பு பற்றியது."},
            "D": {"en": "Correct. Article 50 mandates Separation of Judiciary from Executive.", "ta": "சரி. உறுப்பு 50 நிர்வாகத்திலிருந்து நீதித்துறையைப் பிரிப்பதை ஆணையிடுகிறது."}
        },
        tip_en="TNPSC Tip: Article 50 = Separation of Judiciary from Executive; Article 44 = Uniform Civil Code.",
        tip_ta="TNPSC குறிப்பு: உறுப்பு 50 = நிர்வாகத்திலிருந்து நீதித்துறை பிரிப்பு; உறுப்பு 44 = பொது சிவில் சட்டம்.",
        rev_en="Article 50 (DPSP) = Separation of Judiciary from Executive.",
        rev_ta="உறுப்பு 50 (DPSP) = நிர்வாகத்திலிருந்து நீதித்துறையைப் பிரித்தல்.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Remember", est_sec=30, pyq_sim="Direct PYQ", tags=["Article 50", "DPSP", "Separation of Powers", "Independent Judiciary"]
    ))

    # Q34 - TNPSC Trap - Medium - Ans A
    qs.append(make_q(
        q_id="SF_GT_034", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="TNPSC Trap",
        q_en="Which of the following Fundamental Rights can NEVER be suspended even during a National Emergency under Article 352?",
        q_ta="உறுப்பு 352 இன் கீழ் தேசிய அவசரநிலையின் போது கூட பின்வரும் எந்த அடிப்படை உரிமைகளையும் ஒருபோதும் நிறுத்தி வைக்க முடியாது?",
        opts_en=[
            "Articles 20 and 21",
            "Articles 19 and 20",
            "Articles 14 and 19",
            "Articles 21 and 22"
        ],
        opts_ta=[
            "உறுப்புகள் 20 மற்றும் 21",
            "உறுப்புகள் 19 மற்றும் 20",
            "உறுப்புகள் 14 மற்றும் 19",
            "உறுப்புகள் 21 மற்றும் 22"
        ],
        correct_ans="A",
        exp_en="Historical Context: The 44th Constitutional Amendment Act, 1978 introduced safeguards against arbitrary emergency suspensions.\nReason: Under Article 359 (as amended by 44th Amendment 1978), the President CANNOT suspend the right to move courts for enforcement of Articles 20 (Protection in respect of conviction for offences) and 21 (Protection of life and personal liberty).\nConstitutional Impact: Protects citizens against executive tyranny during emergency.\nExam Trap: Article 19 is automatically suspended ONLY under External Emergency (war/aggression), but Articles 20 and 21 can NEVER be suspended under any emergency.\nMemory Trick: 20 & 21 = Immortal Rights (Never Suspended).",
        exp_ta="வரலாற்றுப் பின்னணி: 44வது அரசியலமைப்பு திருத்தச் சட்டம், 1978 தன்னிச்சையான அவசரக்கால நிறுத்தங்களுக்கு எதிரான பாதுகாப்புகளை அறிமுகப்படுத்தியது.\nகாரணம்: உறுப்பு 359 இன் கீழ் (44வது திருத்தம் 1978 மூலம் திருத்தப்பட்டபடி), உறுப்புகள் 20 (குற்றங்களுக்காக தண்டிக்கப்படுவதிலிருந்து பாதுகாப்பு) மற்றும் 21 (வாழ்வு மற்றும் தனிநபர் சுதந்திர பாதுகாப்பு) ஆகியவற்றை அமல்படுத்த நீதிமன்றங்களை அணுகும் உரிமையை குடியரசுத் தலைவர் நிறுத்தி வைக்க முடியாது.\nஅரசியலமைப்பு தாக்கம்: அவசரநிலையின் போது நிர்வாக கொடுங்கோன்மையிலிருந்து குடிமக்களைப் பாதுகாக்கிறது.\nதேர்வுப் பொறி: உறுப்பு 19 வெளிப்படை அவசரநிலையின் போது மட்டுமே தானாகவே நிறுத்தப்படும், ஆனால் உறுப்புகள் 20 மற்றும் 21 எந்த அவசரநிலையிலும் ஒருபோதும் நிறுத்தப்பட முடியாது.\nநினைவுச் சூத்திரம்: 20 & 21 = அழியாத உரிமைகள் (ஒருபோதும் நிறுத்தப்படாது).",
        wno_dict={
            "A": {"en": "Correct. Articles 20 and 21 can NEVER be suspended under Article 359.", "ta": "சரி. உறுப்புகள் 20 மற்றும் 21 ஐ உறுப்பு 359 இன் கீழ் ஒருபோதும் நிறுத்தி வைக்க முடியாது."},
            "B": {"en": "Incorrect. Article 19 can be suspended under Article 358 during external emergency.", "ta": "தவறு. வெளிப்படை அவசரநிலையின் போது உறுப்பு 358 இன் கீழ் உறுப்பு 19 நிறுத்தப்படலாம்."},
            "C": {"en": "Incorrect. Both 14 and 19 can be suspended.", "ta": "தவறு. 14 மற்றும் 19 இரண்டும் நிறுத்தப்படலாம்."},
            "D": {"en": "Incorrect. Article 22 can be suspended under Article 359.", "ta": "தவறு. உறுப்பு 22 உறுப்பு 359 இன் கீழ் நிறுத்தப்படலாம்."}
        },
        tip_en="TNPSC Trap: 44th Amendment 1978 ensured Articles 20 & 21 cannot be suspended even during National Emergency.",
        tip_ta="TNPSC பொறி: 44வது திருத்தம் 1978 தேசிய அவசரநிலையின் போது கூட உறுப்புகள் 20 & 21 நிறுத்தப்பட முடியாது என்பதை உறுதி செய்தது.",
        rev_en="Articles 20 & 21 = Immune to suspension during Emergency (via 44th Amendment 1978).",
        rev_ta="உறுப்புகள் 20 & 21 = அவசரநிலையின் போது நிறுத்தப்பட முடியாதவை (44வது திருத்தம் 1978 மூலம்).",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Understand", est_sec=45, pyq_sim="High", tags=["Emergency Provisions", "Articles 20 and 21", "44th Amendment", "TNPSC Trap"]
    ))

    # Q35 - Hard / Analytical - Hard - Ans B
    qs.append(make_q(
        q_id="SF_GT_035", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Hard", question_type="Hard / Analytical",
        q_en="Which of the following constitutional mechanisms maintains the supremacy of the Constitution while balancing Parliamentary Amending Power under Article 368?",
        q_ta="பின்வரும் அரசியலமைப்பு வழிமுறைகளில் எது உறுப்பு 368 இன் கீழ் நாடாளுமன்ற திருத்தும் அதிகாரத்தைச் சமநிலைப்படுத்தும் அதே வேளையில் அரசியலமைப்பின் மேலாதிக்கத்தைப் பேணுகிறது?",
        opts_en=[
            "The Power of Executive Veto held by the President of India",
            "The Doctrine of Basic Structure laid down by the Supreme Court",
            "The Ordinance-making power of the State Governors under Article 213",
            "The Special Majority required under Article 249"
        ],
        opts_ta=[
            "இந்தியக் குடியரசுத் தலைவரிடம் உள்ள நிர்வாக வீட்டோ அதிகாரம்",
            "உச்ச நீதிமன்றத்தால் வகுக்கப்பட்ட அடிப்படை கட்டமைப்பு கோட்பாடு",
            "உறுப்பு 213 இன் கீழ் மாநில ஆளுநர்களின் அவசரச் சட்டம் பிறப்பிக்கும் அதிகாரம்",
            "உறுப்பு 249 இன் கீழ் தேவைப்படும் சிறப்பு பெரும்பான்மை"
        ],
        correct_ans="B",
        exp_en="Historical Context: The tension between Parliamentary Sovereignty (UK style) and Judicial Review (US style) reached resolution in India through judicial interpretation.\nReason: The Doctrine of Basic Structure allows Parliament to amend any part of the Constitution under Art 368 to meet changing national needs, while preventing it from destroying core features (democracy, secularism, federalism, judicial review).\nConstitutional Impact: Synthesizes flexibility with constitutional supremacy.\nExam Trap: Executive veto cannot stop constitutional amendments passed by Parliament.",
        exp_ta="வரலாற்றுப் பின்னணி: நாடாளுமன்ற இறையாண்மைக்கும் (இங்கிலாந்து பாணி) நீதித்துறை மறுஆய்விற்கும் (அமெரிக்க பாணி) இடையே உள்ள பதற்றம் நீதித்துறை விளக்கத்தின் மூலம் இந்தியாவில் தீர்வை எட்டியது.\nகாரணம்: அடிப்படை கட்டமைப்பு கோட்பாடு நாடாளுமன்றம் மாறிவரும் தேசியத் தேவைகளைப் பூர்த்தி செய்ய உறுப்பு 368 இன் கீழ் அரசியலமைப்பின் எந்தப் பகுதியையும் திருத்த அனுமதிக்கிறது, அதே நேரத்தில் முக்கிய அம்சங்களை (ஜனநாயகம், மதச்சார்பின்மை, கூட்டாட்சி, நீதித்துறை மறுஆய்வு) அழிப்பதைத் தடுக்கிறது.\nஅரசியலமைப்பு தாக்கம்: அரசியலமைப்பு மேலாதிக்கத்துடன் நெகிழ்வுத்தன்மையை இணைக்கிறது.\nதேர்வுப் பொறி: நாடாளுமன்றத்தால் நிறைவேற்றப்பட்ட அரசியலமைப்பு திருத்தங்களை நிர்வாக வீட்டோவால்தடுக்க முடியாது.",
        wno_dict={
            "A": {"en": "Incorrect. President cannot veto a Constitutional Amendment Bill (24th Amendment 1971 made President's assent mandatory).", "ta": "தவறு. குடியரசுத் தலைவர் அரசியலமைப்பு திருத்த மசோதாவை வீட்டோ செய்ய முடியாது (24வது திருத்தம் 1971 குடியரசுத் தலைவரின் ஒப்புதலைக் கட்டாயமாக்கியது)."},
            "B": {"en": "Correct. Basic Structure Doctrine balances amending power with constitutional supremacy.", "ta": "சரி. அடிப்படை கட்டமைப்பு கோட்பாடு திருத்தும் அதிகாரத்தை அரசியலமைப்பு மேலாதிக்கத்துடன் சமநிலைப்படுத்துகிறது."},
            "C": {"en": "Incorrect. Ordinance power has no relation to Article 368.", "ta": "தவறு. அவசரச் சட்ட அதிகாரத்திற்கு உறுப்பு 368 உடன் தொடர்பில்லை."},
            "D": {"en": "Incorrect. Article 249 deals with legislation in State list by Rajya Sabha.", "ta": "தவறு. உறுப்பு 249 மாநிலப் பட்டியலில் நாடாளுமன்றச் சட்டம் இயற்றுவது பற்றியது."}
        },
        tip_en="TNPSC Tip: Basic Structure Doctrine = Harmonious synthesis of Parliamentary Sovereignty and Judicial Supremacy.",
        tip_ta="TNPSC குறிப்பு: அடிப்படை கட்டமைப்பு கோட்பாடு = நாடாளுமன்ற இறையாண்மை மற்றும் நீதித்துறை மேலாதிக்கத்தின் இணக்கமான இணைப்பு.",
        rev_en="Basic Structure Doctrine: Synthesizes Parliamentary Amending Power with Constitutional Supremacy.",
        rev_ta="அடிப்படை கட்டமைப்பு கோட்பாடு: நாடாளுமன்ற திருத்தும் அதிகாரத்தை அரசியலமைப்பு மேலாதிக்கத்துடன் இணைக்கிறது.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Analyze", est_sec=75, pyq_sim="High", tags=["Basic Structure", "Article 368", "Constitutional Supremacy"]
    ))

    # Q36 - Direct MCQ - Easy - Ans C
    qs.append(make_q(
        q_id="SF_GT_036", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Easy", question_type="Direct MCQ",
        q_en="Under Article 326 of the Indian Constitution, on what grounds can a citizen be disqualified from being registered as a voter?",
        q_ta="இந்திய அரசியலமைப்பின் உறுப்பு 326 இன் கீழ், எந்தக் காரணங்களின் அடிப்படையில் ஒரு குடிமகன் வாக்காளராகப் பதிவு செய்யப்படுவதிலிருந்து தகுதிநீக்கம் செய்யப்படலாம்?",
        opts_en=[
            "Non-residence, unsoundness of mind, crime or corrupt/illegal practice",
            "Gender, caste, religion, or place of birth",
            "Educational qualification, wealth, or tax-paying status",
            "Membership in a political party or trade union"
        ],
        opts_ta=[
            "வசிப்பிடமின்மை, மனநிலை சரியில்லாமை, குற்றம் அல்லது ஊழல்/சட்டவிரோத நடவடிக்கை",
            "பாலினம், சாதி, மதம் அல்லது பிறந்த இடம்",
            "கல்வித் தகுதி, செல்வம் அல்லது வரி செலுத்தும் நிலை",
            "அரசியல் கட்சி அல்லது தொழிற்சங்கத்தில் உறுப்பினர் நிலை"
        ],
        correct_ans="A",
        exp_en="Historical Context: Universal Adult Franchise was introduced without property or educational qualifications.\nReason: Article 326 states that every person who is a citizen of India and not less than 18 years of age shall be entitled to be registered as a voter, UNLESS disqualified on grounds of non-residence, unsoundness of mind, crime, or corrupt/illegal practice.\nConstitutional Impact: Ensures genuine political equality.\nExam Trap: Educational or property qualifications do NOT exist in India for voting.\nMemory Trick: Disqualification = Mind, Crime, Corrupt practice, Non-residence.",
        exp_ta="வரலாற்றுப் பின்னணி: சொத்து அல்லது கல்வித் தகுதிகள் இல்லாமல் உலகளாவிய வயதுவந்தோர் வாக்குரிமை அறிமுகப்படுத்தப்பட்டது.\nகாரணம்: வசிப்பிடமின்மை, மனநிலை சரியில்லாமை, குற்றம் அல்லது ஊழல்/சட்டவிரோத நடவடிக்கை ஆகிய காரணங்களின் அடிப்படையில் தகுதிநீக்கம் செய்யப்படாவிட்டால், இந்தியக் குடிமகனாக இருக்கும் மற்றும் 18 வயதுக்குக் குறையாத ஒவ்வொரு நபரும் வாக்காளராகப் பதிவு செய்ய உரிமை உண்டு என்று உறுப்பு 326 கூறுகிறது.\nஅரசியலமைப்பு தாக்கம்: உண்மையான அரசியல் சமத்துவத்தை உறுதி செய்கிறது.\nதேர்வுப் பொறி: வாக்களிப்பதற்கு இந்தியாவில் கல்வி அல்லது சொத்துத் தகுதிகள் இல்லை.\nநினைவுச் சூத்திரம்: தகுதிநீக்கம் = மனநிலை, குற்றம், ஊழல் நடவடிக்கை, வசிப்பிடமின்மை.",
        wno_dict={
            "A": {"en": "Correct. Non-residence, unsoundness of mind, crime, or corrupt/illegal practice are valid grounds under Art 326.", "ta": "சரி. வசிப்பிடமின்மை, மனநிலை சரியில்லாமை, குற்றம் அல்லது ஊழல் நடவடிக்கை ஆகியவை உறுப்பு 326 இன் கீழ் செல்லுபடியாகும் காரணங்கள்."},
            "B": {"en": "Incorrect. Discrimination based on gender, caste, religion is strictly forbidden by Art 15 & Art 325.", "ta": "தவறு. பாலினம், சாதி, மதத்தின் அடிப்படையிலான பாகுபாடு உறுப்புகள் 15 & 325 ஆல் கண்டிப்பாகத் தடைசெய்யப்பட்டுள்ளது."},
            "C": {"en": "Incorrect. Education and wealth cannot be grounds for voter disqualification in India.", "ta": "தவறு. இந்தியாவில் வாக்காளர் தகுதிநீக்கத்திற்கு கல்வியும் செல்வமும் காரணங்களாக இருக்க முடியாது."},
            "D": {"en": "Incorrect. Political party membership is not a ground for disqualification.", "ta": "தவறு. அரசியல் கட்சி உறுப்பினர் நிலை தகுதிநீக்கத்திற்கான காரணம் அல்ல."}
        },
        tip_en="TNPSC Tip: Article 326 grounds for disqualification: Non-residence, unsoundness of mind, crime, corrupt or illegal practice.",
        tip_ta="TNPSC குறிப்பு: உறுப்பு 326 தகுதிநீக்க காரணங்கள்: வசிப்பிடமின்மை, மனநிலை சரியில்லாமை, குற்றம், ஊழல் அல்லது சட்டவிரோத நடவடிக்கை.",
        rev_en="Article 326: Disqualifications for voting = Unsound mind, Crime, Corrupt practice, Non-residence.",
        rev_ta="உறுப்பு 326: வாக்களிப்பதற்கான தகுதிநீக்கங்கள் = மனநிலை சரியில்லாமை, குற்றம், ஊழல் நடவடிக்கை, வசிப்பிடமின்மை.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Remember", est_sec=45, pyq_sim="High", tags=["Universal Adult Franchise", "Article 326", "Disqualifications"]
    ))

    # Q37 - Conceptual - Medium - Ans D
    qs.append(make_q(
        q_id="SF_GT_037", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="Conceptual",
        q_en="Why is the Indian Federation called a 'Union of States' in Article 1 of the Constitution?",
        q_ta="இந்திய அரசியலமைப்பின் உறுப்பு 1 இல் இந்தியக் கூட்டாட்சி ஏன் 'மாநிலங்களின் ஒன்றியம்' (Union of States) என்று அழைக்கப்படுகிறது?",
        opts_en=[
            "Because states have the right to secede from the Union whenever they pass a state resolution.",
            "Because it was created by an agreement among sovereign states like the American Federation.",
            "Because the President has absolute military power over state police forces.",
            "Because the Indian federation is not the result of an agreement among states, and no state has the right to secede."
        ],
        opts_ta=[
            "ஏனெனில் மாநிலங்கள் மாநிலத் தீர்மானத்தை நிறைவேற்றும் போதெல்லாம் ஒன்றியத்திலிருந்து பிரியும் உரிமை உண்டு.",
            "ஏனெனில் இது அமெரிக்கக் கூட்டாட்சி போன்ற இறையாண்மை கொண்ட மாநிலங்களுக்கு இடையேயான ஒப்பந்தத்தால் உருவாக்கப்பட்டது.",
            "ஏனெனில் மாநில காவல்துறை மீது குடியரசுத் தலைவருக்கு முப்படைகளின் அதிகாரம் உள்ளது.",
            "ஏனெனில் இந்தியக் கூட்டாட்சி மாநிலங்களுக்கு இடையேயான ஒப்பந்தத்தின் விளைவாக உருவானது அல்ல, மேலும் எந்த மாநிலத்திற்கும் பிரியும் உரிமை இல்லை."
        ],
        correct_ans="D",
        exp_en="Historical Context: Dr. B.R. Ambedkar explained in the Constituent Assembly why 'Union of States' was preferred over 'Federation of States'.\nReason: Two reasons given by Ambedkar: (1) Indian federation is not the result of an agreement among states; (2) States have no right to secede from the federation (Indestructible Union of destructible states).\nConstitutional Impact: Emphasizes national unity and territorial integrity under Article 1.\nExam Trap: India is an Indestructible Union of Destructible States (unlike USA).",
        exp_ta="வரலாற்றுப் பின்னணி: 'மாநிலங்களின் கூட்டமைப்பு' என்பதை விட 'மாநிலங்களின் ஒன்றியம்' ஏன் விரும்பப்பட்டது என்பதை டாக்டர் பி.ஆர். அம்பேத்கர் அரசியலமைப்பு நிர்ணய சபையில் விளக்கினார்.\nகாரணம்: அம்பேத்கர் கூறிய இரண்டு காரணங்கள்: (1) இந்தியக் கூட்டாட்சி மாநிலங்களுக்கு இடையேயான ஒப்பந்தத்தின் விளைவாக உருவானது அல்ல; (2) கூட்டாட்சியிலிருந்து பிரிய மாநிலங்களுக்கு உரிமை இல்லை (அழிக்கப்படக்கூடிய மாநிலங்களின் அழிக்க முடியாத ஒன்றியம்).\nஅரசியலமைப்பு தாக்கம்: உறுப்பு 1 இன் கீழ் தேசிய ஒருமைப்பாடு மற்றும் பிராந்திய ஒருமைப்பாட்டை வலியுறுத்துகிறது.\nதேர்வுப் பொறி: இந்தியா என்பது அழிக்கப்படக்கூடிய மாநிலங்களின் அழிக்க முடியாத ஒன்றியம் (அமெரிக்காவைப் போலல்லாமல்).",
        wno_dict={
            "A": {"en": "Incorrect. States have NO right to secede from the Indian Union.", "ta": "தவறு. இந்திய ஒன்றியத்திலிருந்து பிரிய மாநிலங்களுக்கு உரிமை இல்லை."},
            "B": {"en": "Incorrect. Indian federation is NOT the result of an agreement among states.", "ta": "தவறு. இந்தியக் கூட்டாட்சி மாநிலங்களுக்கு இடையேயான ஒப்பந்தத்தின் விளைவு அல்ல."},
            "C": {"en": "Incorrect. Irrelevant to Article 1 nomenclature.", "ta": "தவறு. உறுப்பு 1 பெயர்முறைக்குத் தொடர்பற்றது."},
            "D": {"en": "Correct. Not an agreement among states + No right to secede (Ambedkar).", "ta": "சரி. மாநிலங்களுக்கு இடையேயான ஒப்பந்தம் அல்ல + பிரியும் உரிமை இல்லை (அம்பேத்கர்)."}
        },
        tip_en="TNPSC Tip: Article 1: India is a 'Union of States' -> Indestructible Union of Destructible States (Ambedkar).",
        tip_ta="TNPSC குறிப்பு: உறுப்பு 1: இந்தியா என்பது 'மாநிலங்களின் ஒன்றியம்' -> அழிக்கப்படக்கூடிய மாநிலங்களின் அழிக்க முடியாத ஒன்றியம் (அம்பேத்கர்).",
        rev_en="Article 1: Union of States = No agreement among states + No right to secede.",
        rev_ta="உறுப்பு 1: மாநிலங்களின் ஒன்றியம் = மாநிலங்களுக்கு இடையே ஒப்பந்தம் இல்லை + பிரியும் உரிமை இல்லை.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Understand", est_sec=45, pyq_sim="High", tags=["Article 1", "Union of States", "Dr B.R. Ambedkar"]
    ))

    # Q38 - Statement-Based - Medium - Ans B
    qs.append(make_q(
        q_id="SF_GT_038", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="Statement-Based",
        q_en="Consider the following statements regarding the Panchayati Raj Institutions (73rd Amendment Act, 1992):\n1. It added Part IX and the 11th Schedule containing 29 functional items to the Constitution.\n2. It established a three-tier system of Panchayats at the village, intermediate, and district levels in all states.\n3. A state having a population not exceeding 20 lakhs may not constitute Panchayats at the intermediate level.\n\nWhich of the statements given above are CORRECT?",
        q_ta="பஞ்சாயத்து ராஜ் நிறுவனங்கள் (73வது திருத்தச் சட்டம், 1992) தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது பகுதி IX மற்றும் 29 செயல்பாட்டுப் பொருட்களைக் கொண்ட 11வது அட்டவணையை அரசியலமைப்பில் சேர்த்தது.\n2. இது அனைத்து மாநிலங்களிலும் கிராமம், இடைநிலை மற்றும் மாவட்ட மட்டங்களில் மூன்று அடுக்கு பஞ்சாயத்து முறையை நிறுவியது.\n3. 20 லட்சத்திற்கு மிகாமல் மக்கள் தொகை கொண்ட ஒரு மாநிலம் இடைநிலை மட்டத்தில் பஞ்சாயத்துகளை அமைக்காமல் இருக்கலாம்.\n\nமேற்கூறிய கூற்றுகளில் எது சரியானவை?",
        opts_en=[
            "1 and 2 only",
            "1, 2 and 3",
            "2 and 3 only",
            "1 and 3 only"
        ],
        opts_ta=[
            "1 மற்றும் 2 மட்டும்",
            "1, 2 மற்றும் 3",
            "2 மற்றும் 3 மட்டும்",
            "1 மற்றும் 3 மட்டும்"
        ],
        correct_ans="B",
        exp_en="Historical Context: 73rd Amendment 1992 gave constitutional status to Panchayati Raj.\nReason:\nStatement 1 is correct: Added Part IX (Arts 243-243O) and 11th Schedule (29 functional items).\nStatement 2 is correct: Mandatory 3-tier structure (Gram, Panchayat Samiti, Zilla Parishad).\nStatement 3 is correct: Article 243B provides that states with population under 20 lakhs need not constitute intermediate level Panchayats.\nConstitutional Impact: Institutionalized grassroot democracy.\nExam Trap: Remember the population limit for intermediate panchayat exception is 20 LAKHS.",
        exp_ta="வரலாற்றுப் பின்னணி: 73வது திருத்தம் 1992 பஞ்சாயத்து ராஜிற்கு அரசியலமைப்பு அந்தஸ்தை வழங்கியது.\nகாரணம்:\nகூற்று 1 சரி: பகுதி IX (உறுப்புகள் 243-243O) மற்றும் 11வது அட்டவணை (29 செயல்பாட்டுப் பொருட்கள்) சேர்க்கப்பட்டது.\nகூற்று 2 சரி: கட்டாய 3-அடுக்கு கட்டமைப்பு (கிராமம், பஞ்சாயத்து ஒன்றியம், மாவட்ட ஊராட்சி).\nகூற்று 3 சரி: 20 லட்சத்திற்கு உட்பட்ட மக்கள் தொகை கொண்ட மாநிலங்கள் இடைநிலை பஞ்சாயத்துகளை அமைக்கத் தேவையில்லை என்று உறுப்பு 243B கூறுகிறது.\nஅரசியலமைப்பு தாக்கம்: அடித்தள ஜனநாயகத்தை நிறுவனமயமாக்கியது.\nதேர்வுப் பொறி: இடைநிலை பஞ்சாயத்து விதிவிலக்கிற்கான மக்கள் தொகை வரம்பு 20 லட்சம் என்பதை நினைவில் கொள்க.",
        wno_dict={
            "A": {"en": "Incorrect. Statement 3 is also correct under Article 243B.", "ta": "தவறு. உறுப்பு 243B இன் கீழ் கூற்று 3-ம் சரியானது."},
            "B": {"en": "Correct. All three statements 1, 2, and 3 are correct.", "ta": "சரி. 1, 2 மற்றும் 3 ஆகிய மூன்று கூற்றுகளும் சரியானவை."},
            "C": {"en": "Incorrect. Statement 1 is also correct.", "ta": "தவறு. கூற்று 1-ம் சரியானது."},
            "D": {"en": "Incorrect. Statement 2 is also correct.", "ta": "தவறு. கூற்று 2-ம் சரியானது."}
        },
        tip_en="TNPSC Tip: 73rd Amendment: Part IX, 11th Schedule (29 items); Exception for intermediate level = population < 20 Lakhs.",
        tip_ta="TNPSC குறிப்பு: 73வது திருத்தம்: பகுதி IX, 11வது அட்டவணை (29 பொருட்கள்); இடைநிலை பஞ்சாயத்து விதிவிலக்கு = மக்கள் தொகை < 20 லட்சம்.",
        rev_en="73rd Amendment 1992: Part IX, 11th Schedule (29 items), 3-tier Panchayats (20 lakh pop exception).",
        rev_ta="73வது திருத்தம் 1992: பகுதி IX, 11வது அட்டவணை (29 பொருட்கள்), 3-அடுக்கு பஞ்சாயத்துகள் (20 லட்சம் மக்கள் தொகை விதிவிலக்கு).",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Analyze", est_sec=60, pyq_sim="High", tags=["73rd Amendment", "Panchayati Raj", "11th Schedule", "Part IX"]
    ))

    # Q39 - PYQ Pattern - Easy - Ans A
    qs.append(make_q(
        q_id="SF_GT_039", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Easy", question_type="PYQ Pattern",
        q_en="Which Constitutional Amendment Act added the 12th Schedule to the Indian Constitution, specifying 18 functional items for Municipalities?",
        q_ta="எந்த அரசியலமைப்பு திருத்தச் சட்டம் இந்திய அரசியலமைப்பில் 12வது அட்டவணையைச் சேர்த்து, நகராட்சிகளுக்கான 18 செயல்பாட்டுப் பொருட்களைக் குறிப்பிட்டது?",
        opts_en=[
            "74th Constitutional Amendment Act, 1992",
            "73rd Constitutional Amendment Act, 1992",
            "65th Constitutional Amendment Act, 1990",
            "91st Constitutional Amendment Act, 2003"
        ],
        opts_ta=[
            "74வது அரசியலமைப்பு திருத்தச் சட்டம், 1992",
            "73வது அரசியலமைப்பு திருத்தச் சட்டம், 1992",
            "65வது அரசியலமைப்பு திருத்தச் சட்டம், 1990",
            "91வது அரசியலமைப்பு திருத்தச் சட்டம், 2003"
        ],
        correct_ans="A",
        exp_en="Historical Context: Enacted alongside the 73rd Amendment to revitalize urban local governance.\nReason: 74th Constitutional Amendment Act, 1992 inserted Part IXA (Articles 243P to 243ZG) and the 12th Schedule containing 18 functional items for Municipalities.\nConstitutional Impact: Granted constitutional protection to urban local self-government bodies.\nExam Trap: 73rd Amendment = Panchayats (11th Sched, 29 items); 74th Amendment = Municipalities (12th Sched, 18 items).\nMemory Trick: 73-Panchayat-11-29; 74-Municipality-12-18.",
        exp_ta="வரலாற்றுப் பின்னணி: நகர்ப்புற உள்ளாட்சி ஆளுகையை புத்துயிரூட்ட 73வது திருத்தத்துடன் இணைந்து இயற்றப்பட்டது.\nகாரணம்: 74வது அரசியலமைப்பு திருத்தச் சட்டம், 1992 பகுதி IXA (உறுப்புகள் 243P முதல் 243ZG வரை) மற்றும் நகராட்சிகளுக்கான 18 செயல்பாட்டுப் பொருட்களைக் கொண்ட 12வது அட்டவணையைச் சேர்த்தது.\nஅரசியலமைப்பு தாக்கம்: நகர்ப்புற உள்ளாட்சி அமைப்புகளுக்கு அரசியலமைப்பு பாதுகாப்பை வழங்கியது.\nதேர்வுப் பொறி: 73வது திருத்தம் = பஞ்சாயத்துகள் (11வது அட்டவணை, 29 பொருட்கள்); 74வது திருத்தம் = நகராட்சிகள் (12வது அட்டவணை, 18 பொருட்கள்).\nநினைவுச் சூத்திரம்: 73-பஞ்சாயத்து-11-29; 74-நகராட்சி-12-18.",
        wno_dict={
            "A": {"en": "Correct. 74th Amendment Act 1992 added Part IXA and 12th Schedule (18 items).", "ta": "சரி. 74வது திருத்தச் சட்டம் 1992 பகுதி IXA மற்றும் 12வது அட்டவணையைச் சேர்த்தது (18 பொருட்கள்)."},
            "B": {"en": "Incorrect. 73rd Amendment added Part IX and 11th Schedule (29 items) for Panchayats.", "ta": "தவறு. 73வது திருத்தம் பஞ்சாயத்துகளுக்காக பகுதி IX மற்றும் 11வது அட்டவணையைச் சேர்த்தது (29 பொருட்கள்)."},
            "C": {"en": "Incorrect. 65th Amendment 1990 dealt with National Commission for SCs & STs.", "ta": "தவறு. 65வது திருத்தம் 1990 SC & ST தேசிய ஆணையம் பற்றியது."},
            "D": {"en": "Incorrect. 91st Amendment 2003 dealt with anti-defection and cabinet size.", "ta": "தவறு. 91வது திருத்தம் 2003 கட்சித் தாவல் எதிர்ப்பு மற்றும் அமைச்சரவை அளவு பற்றியது."}
        },
        tip_en="TNPSC Tip: 74th Amendment = Part IXA, 12th Schedule, 18 Functional Items (Municipalities).",
        tip_ta="TNPSC குறிப்பு: 74வது திருத்தம் = பகுதி IXA, 12வது அட்டவணை, 18 செயல்பாட்டுப் பொருட்கள் (நகராட்சிகள்).",
        rev_en="74th Amendment Act 1992: Part IXA, 12th Schedule (18 items for Municipalities).",
        rev_ta="74வது திருத்தச் சட்டம் 1992: பகுதி IXA, 12வது அட்டவணை (நகராட்சிகளுக்கு 18 பொருட்கள்).",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Remember", est_sec=30, pyq_sim="Direct PYQ", tags=["74th Amendment", "Municipalities", "12th Schedule", "Part IXA"]
    ))

    # Q40 - Match the Following - Hard - Ans C
    qs.append(make_q(
        q_id="SF_GT_040", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Hard", question_type="Match the Following",
        q_en="Match List-I (Constitutional Body) with List-II (Article Number) and select the correct option:\n\nList-I:\n(a) Comptroller and Auditor General of India\n(b) Election Commission of India\n(c) Finance Commission of India\n(d) Union Public Service Commission\n\nList-II:\n1. Article 280\n2. Article 315\n3. Article 148\n4. Article 324",
        q_ta="பட்டியல்-I (அரசியலமைப்பு அமைப்பு) பட்டியல்-II (உறுப்பு எண்) உடன் பொருத்தி சரியான விருப்பத்தைத் தேர்ந்தெடுக்கவும்:\n\nபட்டியல்-I:\n(a) இந்திய தலைமை தணிக்கை அதிகாரி (CAG)\n(b) இந்தியத் தேர்தல் ஆணையம்\n(c) இந்திய நிதி ஆணையம்\n(d) மத்திய அரசுப் பணியாளர் தேர்வாணையம் (UPSC)\n\nபட்டியல்-II:\n1. உறுப்பு 280\n2. உறுப்பு 315\n3. உறுப்பு 148\n4. உறுப்பு 324",
        opts_en=[
            "(a)-3, (b)-1, (c)-4, (d)-2",
            "(a)-4, (b)-3, (c)-1, (d)-2",
            "(a)-3, (b)-4, (c)-1, (d)-2",
            "(a)-3, (b)-4, (c)-2, (d)-1"
        ],
        opts_ta=[
            "(a)-3, (b)-1, (c)-4, (d)-2",
            "(a)-4, (b)-3, (c)-1, (d)-2",
            "(a)-3, (b)-4, (c)-1, (d)-2",
            "(a)-3, (b)-4, (c)-2, (d)-1"
        ],
        correct_ans="C",
        exp_en="Historical Context: Independent Constitutional Bodies serve as bulwarks of the Indian democratic system.\nReason:\n(a) CAG = Article 148 (3)\n(b) Election Commission = Article 324 (4)\n(c) Finance Commission = Article 280 (1)\n(d) UPSC = Article 315 (2)\nMatching: (a)-3, (b)-4, (c)-1, (d)-2.",
        exp_ta="வரலாற்றுப் பின்னணி: சுதந்திரமான அரசியலமைப்பு அமைப்புகள் இந்திய ஜனநாயக அமைப்பின் தூண்களாகச் செயல்படுகின்றன.\nகாரணம்:\n(a) CAG = உறுப்பு 148 (3)\n(b) தேர்தல் ஆணையம் = உறுப்பு 324 (4)\n(c) நிதி ஆணையம் = உறுப்பு 280 (1)\n(d) UPSC = உறுப்பு 315 (2)\nபொருத்துதல்: (a)-3, (b)-4, (c)-1, (d)-2.",
        wno_dict={
            "A": {"en": "Incorrect. Election Commission is Art 324 (4), not Art 280 (1).", "ta": "தவறு. தேர்தல் ஆணையம் உறுப்பு 324 (4), உறுப்பு 280 (1) அல்ல."},
            "B": {"en": "Incorrect. CAG is Art 148 (3), not Art 324 (4).", "ta": "தவறு. CAG உறுப்பு 148 (3), உறுப்பு 324 (4) அல்ல."},
            "C": {"en": "Correct. All four constitutional bodies matched with their exact constitutional articles.", "ta": "சரி. நான்கு அரசியலமைப்பு அமைப்புகளும் அவற்றின் துல்லியமான அரசியலமைப்பு உறுப்புகளுடன் பொருந்தியுள்ளன."},
            "D": {"en": "Incorrect. Finance Commission is Art 280 (1), UPSC is Art 315 (2).", "ta": "தவறு. நிதி ஆணையம் உறுப்பு 280 (1), UPSC உறுப்பு 315 (2)."}
        },
        tip_en="TNPSC Tip: Core Constitutional Bodies: CAG (148), EC (324), FC (280), UPSC (315).",
        tip_ta="TNPSC குறிப்பு: முக்கிய அரசியலமைப்பு அமைப்புகள்: CAG (148), EC (324), FC (280), UPSC (315).",
        rev_en="Constitutional Bodies Articles: CAG 148, Election Commission 324, Finance Commission 280, UPSC 315.",
        rev_ta="அரசியலமைப்பு அமைப்புகள் உறுப்புகள்: CAG 148, தேர்தல் ஆணையம் 324, நிதி ஆணையம் 280, UPSC 315.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Remember", est_sec=60, pyq_sim="High", tags=["Constitutional Bodies", "CAG", "Election Commission", "Finance Commission", "UPSC"]
    ))

    # Q41 - Assertion & Reason - Hard - Ans A
    qs.append(make_q(
        q_id="SF_GT_041", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Hard", question_type="Assertion & Reason",
        q_en="Given below are two statements, one labeled as Assertion (A) and the other labeled as Reason (R):\n\nAssertion (A): The Indian Constitution establishes a Welfare State as opposed to a Police State.\nReason (R): The Directive Principles of State Policy in Part IV place an obligation on the State to promote the welfare of the people by securing a social order permeated by social, economic, and political justice.",
        q_ta="கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிக்கப்பட்டுள்ளது:\n\nகூற்று (A): இந்திய அரசியலமைப்பு ஒரு போலீஸ் அரசுக்கு எதிராக நலன்புரி அரசை (Welfare State) நிறுவுகிறது.\nகாரணம் (R): பகுதி IV இல் உள்ள அரசு நெறிமுறைப்படுத்தும் கோட்பாடுகள், சமூக, பொருளாதார மற்றும் அரசியல் நீதியால் நிரம்பிய சமூக ஒழுங்கைப் பாதுகாப்பதன் மூலம் மக்களின் நலனை மேம்படுத்த அரசுக்கு ஒரு கடமையை விதிக்கின்றன.",
        opts_en=[
            "Both (A) and (R) are true and (R) is the correct explanation of (A)",
            "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
            "(A) is true but (R) is false",
            "(A) is false but (R) is true"
        ],
        opts_ta=[
            "(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கமாகும்",
            "(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல",
            "(A) சரி, ஆனால் (R) தவறு",
            "(A) தவறு, ஆனால் (R) சரி"
        ],
        correct_ans="A",
        exp_en="Historical Context: The Preamble and Part IV (DPSP) transform the colonial Police State into a modern democratic Welfare State.\nReason: Article 38 explicitly mandates the State to secure a social order for the promotion of welfare of the people, aiming for social, economic, and political justice.\nConstitutional Impact: Directs state resources toward poverty eradication, education, healthcare, and social security.\nExam Trap: Police State focuses only on maintenance of law & order; Welfare State focuses on socio-economic development.",
        exp_ta="வரலாற்றுப் பின்னணி: முகவுரை மற்றும் பகுதி IV (DPSP) ஆகியவை காலனித்துவ போலீஸ் அரசை ஒரு நவீன ஜனநாயக நலன்புரி அரசாக மாற்றுகின்றன.\nகாரணம்: உறுப்பு 38 சமூக, பொருளாதார மற்றும் அரசியல் நீதியைக் குறிக்கோளாகக் கொண்டு, மக்களின் நலனை மேம்படுத்துவதற்கான ஒரு சமூக ஒழுங்கைப் பாதுகாப்பதை அரசுக்கு வெளிப்படையாக ஆணையிடுகிறது.\nஅரசியலமைப்பு தாக்கம்: வறுமை ஒழிப்பு, கல்வி, சுகாதாரம் மற்றும் சமூகப் பாதுகாப்பை நோக்கிய மாநில வளங்களை இயக்குகிறது.\nதேர்வுப் பொறி: போலீஸ் அரசு சட்டம் & ஒழுங்கைப் பராமரிப்பதில் மட்டுமே கவனம் செலுத்துகிறது; நலன்புரி அரசு சமூக-பொருளாதார வளர்ச்சியில் கவனம் செலுத்துகிறது.",
        wno_dict={
            "A": {"en": "Correct. Both statements are true and (R) directly explains why India is a Welfare State.", "ta": "சரி. இரு கூற்றுகளும் சரி, மற்றும் (R) ஏன் இந்தியா ஒரு நலன்புரி அரசு என்பதை நேரடியாக விளக்குகிறது."},
            "B": {"en": "Incorrect. (R) is the exact justification for (A).", "ta": "தவறு. (R) என்பது (A)-க்கான துல்லியமான விளக்கமாகும்."},
            "C": {"en": "Incorrect. (R) is true.", "ta": "தவறு. (R) உண்மை."},
            "D": {"en": "Incorrect. (A) is true.", "ta": "தவறு. (A) உண்மை."}
        },
        tip_en="TNPSC Tip: Welfare State concept is enshrined in Preamble and Article 38 of DPSP (Part IV).",
        tip_ta="TNPSC குறிப்பு: நலன்புரி அரசு என்ற கருத்து முகவுரை மற்றும் DPSP இன் உறுப்பு 38 (பகுதி IV) இல் பொதிந்துள்ளது.",
        rev_en="Welfare State = Enshrined in DPSP (Art 38) and Preamble (Social, Economic, Political Justice).",
        rev_ta="நலன்புரி அரசு = DPSP (உறுப்பு 38) மற்றும் முகவுரையில் பொதிந்துள்ளது (சமூக, பொருளாதார, அரசியல் நீதி).",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Evaluate", est_sec=60, pyq_sim="High", tags=["Welfare State", "DPSP", "Article 38", "Assertion Reason"]
    ))

    # Q42 - Conceptual - Medium - Ans B
    qs.append(make_q(
        q_id="SF_GT_042", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="Conceptual",
        q_en="Which of the following describes the relationship between Fundamental Rights and Directive Principles of State Policy as held by the Supreme Court in the Minerva Mills Case (1980)?",
        q_ta="மினர்வா மில்ஸ் வழக்கில் (1980) உச்ச நீதிமன்றம் வழங்கிய தீர்ப்பின்படி அடிப்படை உரிமைகளுக்கும் அரசு நெறிமுறைப்படுத்தும் கோட்பாடுகளுக்கும் இடையே உள்ள உறவை பின்வருவனவற்றில் எது விவரிக்கிறது?",
        opts_en=[
            "Directive Principles enjoy complete supremacy over Fundamental Rights under all circumstances.",
            "The Indian Constitution is founded on the bedrock of the balance and harmony between Part III (FRs) and Part IV (DPSPs).",
            "Fundamental Rights and Directive Principles are mutually destructive and cannot co-exist.",
            "Parliament can abrogate all Fundamental Rights to implement any Directive Principle."
        ],
        opts_ta=[
            "அரசு நெறிமுறைக் கோட்பாடுகள் அனைத்து சூழ்நிலைகளிலும் அடிப்படை உரிமைகளை விட முழுமையான மேலாதிக்கத்தைக் கொண்டுள்ளன.",
            "இந்திய அரசியலமைப்பு பகுதி III (FR) மற்றும் பகுதி IV (DPSP) இடையேயான சமநிலை மற்றும் இணக்கத்தின் அடித்தளத்தில் நிறுவப்பட்டுள்ளது.",
            "அடிப்படை உரிமைகளும் அரசு நெறிமுறைக் கோட்பாடுகளும் பரஸ்பரம் அழிவுகரமானவை மற்றும் ஒன்றாக இருக்க முடியாது.",
            "எந்தவொரு நெறிமுறைக் கோட்பாட்டையும் அமல்படுத்த நாடாளுமன்றம் அனைத்து அடிப்படை உரிமைகளையும் ரத்து செய்ய முடியும்."
        ],
        correct_ans="B",
        exp_en="Historical Context: The friction between FRs and DPSPs was resolved by establishing harmonious construction.\nReason: In Minerva Mills case (1980), the SC held: 'The Constitution is founded on the bedrock of the balance between Part III and Part IV. To give absolute primacy to one over the other is to disturb the harmony of the Constitution. This harmony is a basic feature.'\nConstitutional Impact: Prevents Parliament from destroying Fundamental Rights in the name of implementing DPSPs.\nExam Trap: Neither FR nor DPSP has absolute primacy; HARMONY between both is a Basic Feature.\nMemory Trick: Minerva Mills = Harmony Bedrock.",
        exp_ta="வரலாற்றுப் பின்னணி: அடிப்படை உரிமைகளுக்கும் DPSP-க்கும் இடையிலான உராய்வு இணக்கமான அமைப்பை நிறுவுவதன் மூலம் தீர்க்கப்பட்டது.\nகாரணம்: மினர்வா மில்ஸ் வழக்கில் (1980), உச்ச நீதிமன்றம் தீர்ப்பளித்தது: 'அரசியலமைப்பு பகுதி III மற்றும் பகுதி IV இடையேயான சமநிலையின் அடித்தளத்தில் நிறுவப்பட்டுள்ளது. ஒன்றை விட மற்றொன்றுக்கு முழுமையான முதன்மை அளிப்பது அரசியலமைப்பின் இணக்கத்தைக் குலைப்பதாகும். இந்த இணக்கமே ஒரு அடிப்படை அம்சமாகும்.'\nஅரசியலமைப்பு தாக்கம்: DPSP ஐ அமல்படுத்துவது என்ற பெயரில் நாடாளுமன்றம் அடிப்படை உரிமைகளை அழிப்பதைத் தடுக்கிறது.\nதேர்வுப் பொறி: FR அல்லது DPSP இரண்டிற்கும் முழுமையான முதன்மை இல்லை; இரண்டிற்கும் இடையிலான இணக்கமே அடிப்படை அம்சமாகும்.\nநினைவுச் சூத்திரம்: மினர்வா மில்ஸ் = இணக்க அடித்தளம்.",
        wno_dict={
            "A": {"en": "Incorrect. DPSPs do not enjoy absolute supremacy over FRs.", "ta": "தவறு. DPSP-கள் FR-களை விட முழுமையான மேலாதிக்கத்தைக் கொண்டிருக்கவில்லை."},
            "B": {"en": "Correct. Founded on bedrock of balance and harmony between Part III and Part IV (Minerva Mills 1980).", "ta": "சரி. பகுதி III மற்றும் பகுதி IV இடையேயான சமநிலை மற்றும் இணக்கத்தின் அடித்தளத்தில் நிறுவப்பட்டுள்ளது (மினர்வா மில்ஸ் 1980)."},
            "C": {"en": "Incorrect. They are complementary two wheels of a chariot.", "ta": "தவறு. அவை ஒரு தேரின் இரு சக்கரங்களைப் போல நிரப்பியாக உள்ளன."},
            "D": {"en": "Incorrect. Parliament cannot abrogate FRs completely to implement DPSPs.", "ta": "தவறு. DPSPகளை அமல்படுத்த நாடாளுமன்றம் FRகளை முற்றிலும் ரத்து செய்ய முடியாது."}
        },
        tip_en="TNPSC Tip: Minerva Mills Case (1980): Harmony and balance between FRs and DPSPs is part of the Basic Structure.",
        tip_ta="TNPSC குறிப்பு: மினர்வா மில்ஸ் வழக்கு (1980): FR மற்றும் DPSP இடையேயான இணக்கமும் சமநிலையும் அடிப்படை அமைப்பின் ஒரு பகுதியாகும்.",
        rev_en="Minerva Mills Case 1980: Harmony between FRs & DPSPs = Basic Structure.",
        rev_ta="மினர்வா மில்ஸ் வழக்கு 1980: FR & DPSP இடையேயான இணக்கம் = அடிப்படை அமைப்பு.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Understand", est_sec=45, pyq_sim="High", tags=["Minerva Mills Case", "FR vs DPSP", "Basic Structure"]
    ))

    # Q43 - Direct MCQ - Easy - Ans C
    qs.append(make_q(
        q_id="SF_GT_043", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Easy", question_type="Direct MCQ",
        q_en="Under Article 148 of the Constitution, who appoints the Comptroller and Auditor General (CAG) of India?",
        q_ta="அரசியலமைப்பின் உறுப்பு 148 இன் கீழ், இந்திய தலைமை தணிக்கை அதிகாரியை (CAG) நியமிப்பவர் யார்?",
        opts_en=[
            "Prime Minister of India",
            "Parliament of India",
            "President of India by warrant under his hand and seal",
            "Finance Minister of India"
        ],
        opts_ta=[
            "இந்தியப் பிரதமர்",
            "இந்திய நாடாளுமன்றம்",
            "தனது கைப்பட எழுதிய கையொப்பம் மற்றும் முத்திரையுடன் கூடிய ஆணை மூலம் இந்தியக் குடியரசுத் தலைவர்",
            "இந்திய நிதி அமைச்சர்"
        ],
        correct_ans="C",
        exp_en="Historical Context: CAG is described by Dr. B.R. Ambedkar as the most important officer under the Constitution of India.\nReason: Under Article 148, CAG is appointed by the President of India by warrant under his hand and seal, and can be removed only on like grounds and in like manner as a Supreme Court judge.\nConstitutional Impact: Ensures financial audit independence from executive control.\nExam Trap: Appointed by President, removed by Parliament (like SC Judge).\nMemory Trick: CAG Appointed by President's Warrant.",
        exp_ta="வரலாற்றுப் பின்னணி: இந்திய அரசியலமைப்பின் கீழ் CAG மிகவும் முக்கியமான அதிகாரி என்று டாக்டர் பி.ஆர். அம்பேத்கரால் விவரிக்கப்படுகிறார்.\nகாரணம்: உறுப்பு 148 இன் கீழ், CAG தனது கைப்பட எழுதிய கையொப்பம் மற்றும் முத்திரையுடன் கூடிய ஆணை மூலம் இந்தியக் குடியரசுத் தலைவரால் நியமிக்கப்படுகிறார், மேலும் உச்ச நீதிமன்ற நீதிபதியை நீக்கும் அதே காரணங்கள் மற்றும் முறையிலேயே நீக்கப்படலாம்.\nஅரசியலமைப்பு தாக்கம்: நிர்வாகக் கட்டுப்பாட்டிலிருந்து நிதி தணிக்கை சுதந்திரத்தை உறுதி செய்கிறது.\nதேர்வுப் பொறி: குடியரசுத் தலைவரால் நியமிக்கப்படுகிறார், நாடாளுமன்றத்தால் நீக்கப்படுகிறார் (உச்ச நீதிமன்ற நீதிபதியைப் போல).\nநினைவுச் சூத்திரம்: CAG குடியரசுத் தலைவரின் ஆணை மூலம் நியமிக்கப்படுகிறார்.",
        wno_dict={
            "A": {"en": "Incorrect. PM does not directly appoint CAG.", "ta": "தவறு. பிரதமர் நேரடியாக CAG-ஐ நியமிப்பதில்லை."},
            "B": {"en": "Incorrect. Parliament does not appoint CAG.", "ta": "தவறு. நாடாளுமன்றம் CAG-ஐ நியமிப்பதில்லை."},
            "C": {"en": "Correct. Appointed by President by warrant under hand and seal under Article 148.", "ta": "சரி. உறுப்பு 148 இன் கீழ் தனது கைப்பட எழுதிய கையொப்பம் மற்றும் முத்திரையுடன் கூடிய ஆணை மூலம் குடியரசுத் தலைவரால் நியமிக்கப்படுகிறார்."},
            "D": {"en": "Incorrect. Finance Minister has no appointing power for CAG.", "ta": "தவறு. நிதி அமைச்சருக்கு CAG நியமன அதிகாரம் இல்லை."}
        },
        tip_en="TNPSC Tip: CAG (Art 148) is appointed by President by warrant under hand and seal; Guardian of Public Purse.",
        tip_ta="TNPSC குறிப்பு: CAG (உறுப்பு 148) குடியரசுத் தலைவரால் ஆணை மூலம் நியமிக்கப்படுகிறார்; பொதுப் பணத்தின் பாதுகாவலன்.",
        rev_en="Article 148: CAG appointed by President; Guardian of the Public Purse.",
        rev_ta="உறுப்பு 148: CAG குடியரசுத் தலைவரால் நியமிக்கப்படுகிறார்; பொதுப் பணத்தின் பாதுகாவலன்.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Remember", est_sec=30, pyq_sim="High", tags=["CAG", "Article 148", "Constitutional Bodies"]
    ))

    # Q44 - Statement-Based - Hard - Ans D
    qs.append(make_q(
        q_id="SF_GT_044", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Hard", question_type="Statement-Based",
        q_en="Consider the following statements regarding the Unitary Features of the Indian Constitution:\n1. Appointment of State Governors by the Centre.\n2. Existence of All-India Services (IAS, IPS, IFoS).\n3. Single integrated judicial system enforcing both central and state laws.\n\nWhich of the statements given above represent UNITARY features of Indian federalism?",
        q_ta="இந்திய அரசியலமைப்பின் ஒற்றையாட்சி அம்சங்கள் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. மைய அரசால் மாநில ஆளுநர்கள் நியமிக்கப்படுதல்.\n2. அகில இந்திய பணிகள் (IAS, IPS, IFoS) இருத்தல்.\n3. மத்திய மற்றும் மாநில சட்டங்கள் இரண்டையும் அமல்படுத்தும் ஒற்றை ஒருங்கிணைந்த நீதித்துறை அமைப்பு.\n\nமேற்கூறிய கூற்றுகளில் எது இந்தியக் கூட்டாட்சியின் ஒற்றையாட்சி (UNITARY) அம்சங்களைக் குறிக்கிறது?",
        opts_en=[
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        opts_ta=[
            "1 மற்றும் 2 மட்டும்",
            "2 மற்றும் 3 மட்டும்",
            "1 மற்றும் 3 மட்டும்",
            "1, 2 மற்றும் 3"
        ],
        correct_ans="D",
        exp_en="Historical Context: The Indian Constitution incorporates non-federal/unitary provisions to ensure national stability and central control.\nReason:\nStatement 1 is correct: Governor is appointed by President and holds office during President's pleasure (Unitary).\nStatement 2 is correct: All-India Services (Art 312) serve both Centre and States, controlled ultimately by Centre (Unitary).\nStatement 3 is correct: Integrated Judiciary is a Unitary feature (unlike US dual judiciary).\nConstitutional Impact: Equips Centre with authority to override state autonomy during crises or for national integration.",
        exp_ta="வரலாற்றுப் பின்னணி: இந்திய அரசியலமைப்பு தேசிய ஸ்திரத்தன்மை மற்றும் மத்திய கட்டுப்பாட்டை உறுதிப்படுத்த கூட்டாட்சியற்ற/ஒற்றையாட்சி விதிகளை உள்ளடக்கியுள்ளது.\nகாரணம்:\nகூற்று 1 சரி: ஆளுநர் குடியரசுத் தலைவரால் நியமிக்கப்படுகிறார் மற்றும் குடியரசுத் தலைவரின் விருப்பம் வரை பதவியில் இருக்கிறார் (ஒற்றையாட்சி).\nகூற்று 2 சரி: அகில இந்திய பணிகள் (உறுப்பு 312) மத்திய மற்றும் மாநிலங்கள் இரண்டிற்கும் சேவை செய்கின்றன, இறுதியாக மத்திய அரசால் கட்டுப்படுத்தப்படுகின்றன (ஒற்றையாட்சி).\nகூற்று 3 சரி: ஒருங்கிணைந்த நீதித்துறை ஒரு ஒற்றையாட்சி அம்சமாகும் (அமெரிக்க இரட்டை நீதித்துறை போலல்லாமல்).\nஅரசியலமைப்பு தாக்கம்: நெருக்கடிகளின் போது அல்லது தேசிய ஒருமைப்பாட்டிற்காக மாநில சுயாட்சியை ரத்து செய்யும் அதிகாரத்தை மத்திய அரசுக்கு வழங்குகிறது.",
        wno_dict={
            "A": {"en": "Incorrect. Statement 3 is also a Unitary feature.", "ta": "தவறு. கூற்று 3-ம் ஒரு ஒற்றையாட்சி அம்சமாகும்."},
            "B": {"en": "Incorrect. Statement 1 is also a Unitary feature.", "ta": "தவறு. கூற்று 1-ம் ஒரு ஒற்றையாட்சி அம்சமாகும்."},
            "C": {"en": "Incorrect. Statement 2 is also a Unitary feature.", "ta": "தவறு. கூற்று 2-ம் ஒரு ஒற்றையாட்சி அம்சமாகும்."},
            "D": {"en": "Correct. All three statements (1, 2, and 3) are Unitary features of Indian polity.", "ta": "சரி. மூன்று கூற்றுகளும் (1, 2 மற்றும் 3) இந்திய அரசியலின் ஒற்றையாட்சி அம்சங்களாகும்."}
        },
        tip_en="TNPSC Tip: Unitary Features include: Governor Appointment, All-India Services, Integrated Judiciary, Emergency Provisions, Single Citizenship, CAG.",
        tip_ta="TNPSC குறிப்பு: ஒற்றையாட்சி அம்சங்கள்: ஆளுநர் நியமனம், அகில இந்திய பணிகள், ஒருங்கிணைந்த நீதித்துறை, அவசரக்கால விதிகள், ஒற்றைக் குடியுரிமை, CAG.",
        rev_en="Unitary features: Governor appointment, AIS, Integrated Judiciary, Emergency, Single Citizenship.",
        rev_ta="ஒற்றையாட்சி அம்சங்கள்: ஆளுநர் நியமனம், AIS, ஒருங்கிணைந்த நீதித்துறை, அவசரநிலை, ஒற்றைக் குடியுரிமை.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Analyze", est_sec=60, pyq_sim="High", tags=["Unitary Features", "Governor", "All India Services", "Integrated Judiciary"]
    ))

    # Q45 - TNPSC Trap - Medium - Ans A
    qs.append(make_q(
        q_id="SF_GT_045", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="TNPSC Trap",
        q_en="Under Article 356, President's Rule can be imposed in a State on which of the following grounds?",
        q_ta="உறுப்பு 356 இன் கீழ், பின்வரும் எந்தக் காரணங்களின் அடிப்படையில் ஒரு மாநிலத்தில் குடியரசுத் தலைவர் ஆட்சியை விதிக்க முடியும்?",
        opts_en=[
            "Failure of constitutional machinery in the state OR failure to comply with directions given by the Centre under Article 365",
            "Declaration of war by a neighboring country only",
            "Failure of the State to pass its budget within 24 hours of presentation",
            "Outbreak of an epidemic disease in the state"
        ],
        opts_ta=[
            "மாநிலத்தில் அரசியலமைப்பு இயந்திரத்தின் தோல்வி அல்லது உறுப்பு 365 இன் கீழ் மத்திய அரசு வழங்கும் வழிமுறைகளுக்குக் கீழ்ப்படியத் தவறுதல்",
            "அண்டை நாட்டால் போர் அறிவிப்பு மட்டுமே",
            "மாநில வரவுசெலவுத் திட்டத்தை சமர்ப்பித்த 24 மணி நேரத்திற்குள் நிறைவேற்றத் தவறுதல்",
            "மாநிலத்தில் தொற்றுநோய் பரவுதல்"
        ],
        correct_ans="A",
        exp_en="Historical Context: President's Rule (State Emergency) can be proclaimed under two Articles: 356 and 365.\nReason: Article 356 allows President's Rule if Governor reports or President is satisfied that state govt cannot be carried on per Constitution. Article 365 states if a state fails to comply with Central directions, President can hold that constitutional machinery has failed.\nConstitutional Impact: Ensures Central administrative supremacy over states.\nExam Trap: President's Rule can be invoked under BOTH Article 356 AND Article 365.",
        exp_ta="வரலாற்றுப் பின்னணி: குடியரசுத் தலைவர் ஆட்சி (மாநில அவசரநிலை) இரண்டு உறுப்புகளின் கீழ் அறிவிக்கப்படலாம்: 356 மற்றும் 365.\nகாரணம்: அரசியலமைப்பின் படி மாநில அரசை நடத்த முடியாது என்று ஆளுநர் அறிக்கை அளித்தாலோ அல்லது குடியரசுத் தலைவர் திருப்தியடைந்தாலோ உறுப்பு 356 குடியரசுத் தலைவர் ஆட்சியை அனுமதிக்கிறது. மத்திய அரசின் வழிகாட்டுதல்களுக்கு மாநில அரசு கீழ்ப்படியத் தவறினால், அரசியலமைப்பு இயந்திரம் முறிந்துவிட்டதாகக் குடியரசுத் தலைவர் கருதலாம் என்று உறுப்பு 365 கூறுகிறது.\nஅரசியலமைப்பு தாக்கம்: மாநிலங்கள் மீது மத்திய நிர்வாக மேலாதிக்கத்தை உறுதி செய்கிறது.\nதேர்வுப் பொறி: உறுப்பு 356 மற்றும் உறுப்பு 365 ஆகிய இரண்டின் கீழும் குடியரசுத் தலைவர் ஆட்சியைப் பயன்படுத்த முடியும்.",
        wno_dict={
            "A": {"en": "Correct. Art 356 (failure of constitutional machinery) + Art 365 (non-compliance with Central directions).", "ta": "சரி. உறுப்பு 356 (அரசியலமைப்பு இயந்திரத் தோல்வி) + உறுப்பு 365 (மத்திய வழிகாட்டுதல்களுக்கு கீழ்ப்படியாமை)."},
            "B": {"en": "Incorrect. War triggers National Emergency under Art 352, not Art 356.", "ta": "தவறு. போர் உறுப்பு 352 இன் கீழ் தேசிய அவசரநிலையைத் தூண்டுகிறது, உறுப்பு 356 ஐ அல்ல."},
            "C": {"en": "Incorrect. Budget failure leads to CoM resignation, not automatic Art 356.", "ta": "தவறு. வரவுசெலவுத் திட்டத் தோல்வி அமைச்சரவை ராஜினாமாவுக்கு வழிவகுக்கும், தானியங்கி உறுப்பு 356 அல்ல."},
            "D": {"en": "Incorrect. Epidemic disease is governed by Disaster Management Act, not Art 356.", "ta": "தவறு. தொற்றுநோய் பேரழிவு மேலாண்மைச் சட்டத்தால் நிர்வகிக்கப்படுகிறது, உறுப்பு 356 அல்ல."}
        },
        tip_en="TNPSC Trap: President's Rule can be imposed via Art 356 (Constitutional Breakdown) OR Art 365 (Disobeying Union directives).",
        tip_ta="TNPSC பொறி: குடியரசுத் தலைவர் ஆட்சி உறுப்பு 356 (அரசியலமைப்பு முறிவு) அல்லது உறுப்பு 365 (மத்திய வழிகாட்டுதல்களை மீறுதல்) மூலம் விதிக்கப்படலாம்.",
        rev_en="President's Rule: Article 356 (Constitutional Failure) + Article 365 (Union Directive Failure).",
        rev_ta="குடியரசுத் தலைவர் ஆட்சி: உறுப்பு 356 (அரசியலமைப்பு தோல்வி) + உறுப்பு 365 (மத்திய வழிகாட்டுதல் தோல்வி).",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Understand", est_sec=45, pyq_sim="High", tags=["President's Rule", "Article 356", "Article 365", "TNPSC Trap"]
    ))

    # Q46 - Conceptual - Medium - Ans C
    qs.append(make_q(
        q_id="SF_GT_046", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="Conceptual",
        q_en="Why is the Indian Constitution called a 'Living Document'?",
        q_ta="இந்திய அரசியலமைப்பு ஏன் ஒரு 'வாழும் ஆவணம்' (Living Document) என்று அழைக்கப்படுகிறது?",
        opts_en=[
            "Because it has never been modified since its enforcement in 1950.",
            "Because it automatically rewrites itself every ten years without parliamentary approval.",
            "Because it strikes a balance between stability and adaptability, permitting amendments under Article 368 to respond to evolving social realities while preserving basic structure.",
            "Because it was drafted exclusively by living political representatives without legal experts."
        ],
        opts_ta=[
            "ஏனெனில் 1950 இல் நடைமுறைக்கு வந்ததிலிருந்து இது ஒருபோதும் மாற்றப்படவில்லை.",
            "ஏனெனில் நாடாளுமன்ற ஒப்புதல் இன்றி பத்து ஆண்டுகளுக்கு ஒருமுறை அது தானாகவே மீண்டும் எழுதப்படுகிறது.",
            "ஏனெனில் அது ஸ்திரத்தன்மைக்கும் தகவமைப்புக்கும் இடையே ஒரு சமநிலையை ஏற்படுத்துகிறது, அடிப்படை அமைப்பைப் பேணும்போது வளர்ந்து வரும் சமூக யதார்த்தங்களுக்குப் பதிலளிக்கும் வகையில் உறுப்பு 368 இன் கீழ் திருத்தங்களை அனுமதிக்கிறது.",
            "ஏனெனில் இது சட்ட வல்லுநர்கள் இன்றி வாழும் அரசியல் பிரதிநிதிகளால் மட்டுமே வரைவு செய்யப்பட்டது."
        ],
        correct_ans="C",
        exp_en="Historical Context: Over 75 years, the Constitution has accommodated huge socio-economic changes through over 105 amendments.\nReason: It is 'living' because it is not a static text; it evolves through constitutional amendments (Art 368) and dynamic judicial interpretations while protecting core foundational principles (Basic Structure).\nConstitutional Impact: Ensures constitutional longevity and relevance across generations.\nExam Trap: Adaptability does NOT mean Parliament can rewrite the basic structure.",
        exp_ta="வரலாற்றுப் பின்னணி: 75 ஆண்டுகளுக்கும் மேலாக, அரசியலமைப்பு 105 க்கும் மேற்பட்ட திருத்தங்கள் மூலம் பெரும் சமூக-பொருளாதார மாற்றங்களை உள்ளடக்கியுள்ளது.\nகாரணம்: இது 'வாழும்' ஆவணம் ஏனெனில் இது ஒரு நிலையான உரை அல்ல; இது அடிப்படை நிறுவனக் கொள்கைகளைப் பாதுகாக்கும் அதே வேளையில் அரசியலமைப்பு திருத்தங்கள் (உறுப்பு 368) மற்றும் ஆற்றல்மிக்க நீதித்துறை விளக்கங்கள் மூலம் உருவாகிறது.\nஅரசியலமைப்பு தாக்கம்: தலைமுறைகள் முழுவதும் அரசியலமைப்பு ஆயுள் மற்றும் பொருத்தத்தை உறுதி செய்கிறது.\nதேர்வுப் பொறி: தகவமைப்பு என்பது நாடாளுமன்றம் அடிப்படை அமைப்பை மீண்டும் எழுத முடியும் என்று அர்த்தமல்ல.",
        wno_dict={
            "A": {"en": "Incorrect. It has been amended over 105 times.", "ta": "தவறு. இது 105 க்கும் மேற்பட்ட முறை திருத்தப்பட்டுள்ளது."},
            "B": {"en": "Incorrect. Requires parliamentary amendment procedure under Art 368.", "ta": "தவறு. உறுப்பு 368 இன் கீழ் நாடாளுமன்ற திருத்த நடைமுறை தேவை."},
            "C": {"en": "Correct. Combines stability with adaptability to respond to changing society.", "ta": "சரி. மாறும் சமூகத்திற்கு பதிலளிக்கும் வகையில் ஸ்திரத்தன்மையை தகவமைப்புடன் இணைக்கிறது."},
            "D": {"en": "Incorrect. Drafting committee included eminent legal luminaries like Ambedkar, Alladi, Munshi.", "ta": "தவறு. வரைவுக் குழுவில் அம்பேத்கர், அல்லாடி, முன்ஷி போன்ற சிறந்த சட்ட வல்லுநர்கள் இருந்தனர்."}
        },
        tip_en="TNPSC Tip: Constitution as Living Document = Dynamic adaptability via Article 368 combined with Basic Structure preservation.",
        tip_ta="TNPSC குறிப்பு: வாழும் ஆவணமாக அரசியலமைப்பு = அடிப்படை அமைப்பைப் பேணுவதுடன் உறுப்பு 368 மூலம் ஆற்றல்மிக்க தகவமைப்பு.",
        rev_en="Living Document: Balances durability of basic structure with adaptability via Article 368.",
        rev_ta="வாழும் ஆவணம்: அடிப்படை அமைப்பின் ஆயுளை உறுப்பு 368 மூலம் தகவமைப்புடன் சமநிலைப்படுத்துகிறது.",
        sources=["NCERT Class XI - Indian Constitution at Work", "M. Laxmikanth - Indian Polity"],
        bloom="Understand", est_sec=45, pyq_sim="High", tags=["Living Document", "Constitutional Adaptability", "Article 368"]
    ))

    # Q47 - Direct MCQ - Easy - Ans B
    qs.append(make_q(
        q_id="SF_GT_047", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Easy", question_type="Direct MCQ",
        q_en="Under Article 324 of the Constitution, which body is vested with the superintendence, direction, and control of elections in India?",
        q_ta="அரசியலமைப்பின் உறுப்பு 324 இன் கீழ், இந்தியாவில் தேர்தல்களை மேற்பார்வையிடுதல், இயக்குதல் மற்றும் கட்டுப்படுத்தும் அதிகாரம் எந்த அமைப்பிற்கு வழங்கப்பட்டுள்ளது?",
        opts_en=[
            "Union Public Service Commission",
            "Election Commission of India",
            "Delimitation Commission of India",
            "Ministry of Law and Justice"
        ],
        opts_ta=[
            "மத்திய அரசுப் பணியாளர் தேர்வாணையம்",
            "இந்தியத் தேர்தல் ஆணையம்",
            "இந்தியத் தொகுதி மறுவரையறை ஆணையம்",
            "சட்டம் மற்றும் நீதி அமைச்சகம்"
        ],
        correct_ans="B",
        exp_en="Historical Context: Free and fair elections are the vital foundation of democratic governance.\nReason: Article 324 establishes the Election Commission of India to conduct elections to Parliament, State Legislatures, and offices of President and Vice-President.\nConstitutional Impact: Ensures independent election administration free from executive influence.\nExam Trap: Panchayat and Municipality elections are conducted by STATE Election Commissions (Arts 243K & 243ZA), NOT by ECI.\nMemory Trick: Art 324 = Election Commission India.",
        exp_ta="வரலாற்றுப் பின்னணி: சுதந்திரமான மற்றும் நேர்மையான தேர்தல்கள் ஜனநாயக ஆட்சியின் முக்கிய அடித்தளமாகும்.\nகாரணம்: நாடாளுமன்றம், மாநில சட்டமன்றங்கள் மற்றும் குடியரசுத் தலைவர், குடியரசுத் துணைத் தலைவர் பதவிகளுக்கான தேர்தல்களை நடத்த உறுப்பு 324 இந்தியத் தேர்தல் ஆணையத்தை நிறுவுகிறது.\nஅரசியலமைப்பு தாக்கம்: நிர்வாகத் தலையீடற்ற சுதந்திரமான தேர்தல் நிர்வாகத்தை உறுதி செய்கிறது.\nதேர்வுப் பொறி: பஞ்சாயத்து மற்றும் நகராட்சி தேர்தல்கள் மாநிலத் தேர்தல் ஆணையங்களால் நடத்தப்படுகின்றன (உறுப்புகள் 243K & 243ZA), ECI ஆல் அல்ல.\nநினைவுச் சூத்திரம்: உறுப்பு 324 = இந்தியத் தேர்தல் ஆணையம்.",
        wno_dict={
            "A": {"en": "Incorrect. UPSC conducts civil service examinations under Art 315.", "ta": "தவறு. UPSC உறுப்பு 315 இன் கீழ் குடிமைப் பணித் தேர்வுகளை நடத்துகிறது."},
            "B": {"en": "Correct. Article 324 vests election superintendence in Election Commission of India.", "ta": "சரி. உறுப்பு 324 தேர்தல் மேற்பார்வையை இந்தியத் தேர்தல் ஆணையத்திடம் வழங்குகிறது."},
            "C": {"en": "Incorrect. Delimitation Commission redraws constituency boundaries.", "ta": "தவறு. தொகுதி மறுவரையறை ஆணையம் தொகுதி எல்லைகளை மாற்றியமைக்கிறது."},
            "D": {"en": "Incorrect. Law Ministry is an executive department.", "ta": "தவறு. சட்ட அமைச்சகம் ஒரு நிர்வாகத் துறையாகும்."}
        },
        tip_en="TNPSC Trap: ECI (Art 324) conducts Parliament, State Legislature, President, VP elections. State EC conducts Panchayat/Municipality elections.",
        tip_ta="TNPSC பொறி: ECI (உறுப்பு 324) நாடாளுமன்றம், மாநில சட்டமன்றம், குடியரசுத் தலைவர், VP தேர்தல்களை நடத்துகிறது. மாநில EC பஞ்சாயத்து/நகராட்சி தேர்தல்களை நடத்துகிறது.",
        rev_en="Article 324: Election Commission of India (Parliament, State Assembly, President, VP elections).",
        rev_ta="உறுப்பு 324: இந்தியத் தேர்தல் ஆணையம் (நாடாளுமன்றம், மாநில சட்டமன்றம், குடியரசுத் தலைவர், VP தேர்தல்கள்).",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Remember", est_sec=30, pyq_sim="High", tags=["Election Commission", "Article 324", "Constitutional Bodies"]
    ))

    # Q48 - Statement-Based - Hard - Ans A
    qs.append(make_q(
        q_id="SF_GT_048", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Hard", question_type="Statement-Based",
        q_en="Consider the following statements regarding Judicial Review in India:\n1. The phrase 'Judicial Review' is explicitly defined in Article 13 of the Indian Constitution.\n2. The Supreme Court derives power of Judicial Review from Articles 13, 32, 136, 141, and 142.\n3. In L. Chandra Kumar Case (1997), the Supreme Court declared Judicial Review under Articles 32 and 226 as part of the Basic Structure.\n\nWhich of the statements given above are CORRECT?",
        q_ta="இந்தியாவில் நீதித்துறை மறுஆய்வு (Judicial Review) தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 'நீதித்துறை மறுஆய்வு' என்ற சொற்றொடர் இந்திய அரசியலமைப்பின் உறுப்பு 13 இல் வெளிப்படையாக வரையறுக்கப்பட்டுள்ளது.\n2. உச்ச நீதிமன்றம் உறுப்புகள் 13, 32, 136, 141 மற்றும் 142 ஆகியவற்றிலிருந்து நீதித்துறை மறுஆய்வு அதிகாரத்தைப் பெறுகிறது.\n3. எல். சந்திர குமார் வழக்கில் (1997), உச்ச நீதிமன்றம் உறுப்புகள் 32 மற்றும் 226 இன் கீழ் நீதித்துறை மறுஆய்வை அடிப்படை அமைப்பின் ஒரு பகுதி என அறிவித்தது.\n\nமேற்கூறிய கூற்றுகளில் எது சரியானவை?",
        opts_en=[
            "2 and 3 only",
            "1, 2 and 3",
            "1 and 2 only",
            "1 and 3 only"
        ],
        opts_ta=[
            "2 மற்றும் 3 மட்டும்",
            "1, 2 மற்றும் 3",
            "1 மற்றும் 2 மட்டும்",
            "1 மற்றும் 3 மட்டும்"
        ],
        correct_ans="A",
        exp_en="Historical Context: Judicial review is the power of courts to examine the constitutionality of legislative acts and executive orders.\nReason:\nStatement 1 is INCORRECT: The expression 'Judicial Review' is NOWHERE explicitly mentioned or defined in the Constitution, though the principle is embedded in Art 13.\nStatement 2 is correct: Judicial Review power flows from Articles 13, 32, 136, 141, 142, 226, 227.\nStatement 3 is correct: L. Chandra Kumar v. Union of India (1997) held Judicial Review of SC (Art 32) and HC (Art 226) as an integral part of Basic Structure.\nExam Trap: 'Judicial Review' phrase is NOT used in the Constitution text.",
        exp_ta="வரலாற்றுப் பின்னணி: நீதித்துறை மறுஆய்வு என்பது சட்டமன்றச் சட்டங்கள் மற்றும் நிர்வாக உத்தரவுகளின் அரசியலமைப்புத் தன்மையை நீதிமன்றங்கள் ஆய்வு செய்யும் அதிகாரமாகும்.\nகாரணம்:\nகூற்று 1 தவறு: 'நீதித்துறை மறுஆய்வு' என்ற சொல் அரசியலமைப்பில் எங்கும் வெளிப்படையாகக் குறிப்பிடப்படவோ வரையறுக்கப்படவோ இல்லை, இருப்பினும் இக்கோட்பாடு உறுப்பு 13 இல் பொதிந்துள்ளது.\nகூற்று 2 சரி: நீதித்துறை மறுஆய்வு அதிகாரம் உறுப்புகள் 13, 32, 136, 141, 142, 226, 227 ஆகியவற்றிலிருந்து பெறப்படுகிறது.\nகூற்று 3 சரி: எல். சந்திர குமார் எதிர் இந்திய யூனியன் (1997) உச்ச நீதிமன்றம் (உறுப்பு 32) மற்றும் உயர் நீதிமன்றத்தின் (உறுப்பு 226) நீதித்துறை மறுஆய்வை அடிப்படை அமைப்பின் ஒருங்கிணைந்த பகுதி எனத் தீர்ப்பளித்தது.\nதேர்வுப் பொறி: 'நீதித்துறை மறுஆய்வு' என்ற சொல் அரசியலமைப்பு உரையில் பயன்படுத்தப்படவில்லை.",
        wno_dict={
            "A": {"en": "Correct. Statements 2 and 3 are correct; Statement 1 is false because the term is not explicitly defined in the Constitution.", "ta": "சரி. கூற்றுகள் 2 மற்றும் 3 சரி; கூற்று 1 தவறு ஏனெனில் இச்சொல் அரசியலமைப்பில் வெளிப்படையாக வரையறுக்கப்படவில்லை."},
            "B": {"en": "Incorrect. Statement 1 is false.", "ta": "தவறு. கூற்று 1 தவறு."},
            "C": {"en": "Incorrect. Statement 1 is false.", "ta": "தவறு. கூற்று 1 தவறு."},
            "D": {"en": "Incorrect. Statement 1 is false.", "ta": "தவறு. கூற்று 1 தவறு."}
        },
        tip_en="TNPSC Trap: The term 'Judicial Review' is NOT defined in the Constitution. L. Chandra Kumar Case (1997) made it Basic Structure.",
        tip_ta="TNPSC பொறி: 'நீதித்துறை மறுஆய்வு' என்ற சொல் அரசியலமைப்பில் வரையறுக்கப்படவில்லை. எல். சந்திர குமார் வழக்கு (1997) அதை அடிப்படை அமைப்பாக மாற்றியது.",
        rev_en="Judicial Review: Derived from Articles 13, 32, 226 (Term not explicitly in text); Basic Structure via L. Chandra Kumar 1997.",
        rev_ta="நீதித்துறை மறுஆய்வு: உறுப்புகள் 13, 32, 226 லிருந்து பெறப்பட்டது (சொல் உரையில் இல்லை); எல். சந்திர குமார் 1997 மூலம் அடிப்படை அமைப்பு.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Analyze", est_sec=75, pyq_sim="High", tags=["Judicial Review", "Basic Structure", "L. Chandra Kumar Case", "TNPSC Trap"]
    ))

    # Q49 - Conceptual - Medium - Ans C
    qs.append(make_q(
        q_id="SF_GT_049", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="Conceptual",
        q_en="What is the significance of Article 51A(g) of the Indian Constitution?",
        q_ta="இந்திய அரசியலமைப்பின் உறுப்பு 51A(g) இன் முக்கியத்துவம் என்ன?",
        opts_en=[
            "It directs the state to organize village panchayats.",
            "It obligates citizens to respect the National Flag and National Anthem.",
            "It enjoins every citizen to protect and improve the natural environment, including forests, lakes, rivers, and wildlife.",
            "It mandates free legal aid for weaker sections of society."
        ],
        opts_ta=[
            "இது கிராம பஞ்சாயத்துகளை அமைக்க அரசுக்கு வழிகாட்டுகிறது.",
            "இது தேசியக் கொடி மற்றும் தேசிய கீதத்தை மதிக்குமாறு குடிமக்களைக் கடமைப்படுத்துகிறது.",
            "இது காடுகள், ஏரிகள், ஆறுகள் மற்றும் வனவிலங்குகள் உட்பட இயற்கைச் சூழலைப் பாதுகாக்கவும் மேம்படுத்தவும் ஒவ்வொரு குடிமகனுக்கும் ஆணையிடுகிறது.",
            "இது சமூகத்தின் பலவீனமான பிரிவினருக்கு இலவச சட்ட உதவியைக் கட்டாயமாக்குகிறது."
        ],
        correct_ans="C",
        exp_en="Historical Context: Article 51A(g) is a vital Fundamental Duty linking environmental protection with individual civic responsibility.\nReason: Article 51A(g) states that it shall be the duty of every citizen of India to protect and improve the natural environment including forests, lakes, rivers, and wildlife, and to have compassion for living creatures.\nConstitutional Impact: Cited extensively by the Supreme Court in environmental litigation (e.g., M.C. Mehta cases).\nExam Trap: Art 48A is DPSP (State duty for environment); Art 51A(g) is FD (Citizen duty for environment).\nMemory Trick: 51A(g) = Green Duty (Environment & Wildlife).",
        exp_ta="வரலாற்றுப் பின்னணி: உறுப்பு 51A(g) என்பது சுற்றுச்சூழல் பாதுகாப்பைத் தனிநபர் குடிமைப் பொறுப்புடன் இணைக்கும் ஒரு முக்கிய அடிப்படை கடமையாகும்.\nகாரணம்: காடுகள், ஏரிகள், ஆறுகள் மற்றும் வனவிலங்குகள் உட்பட இயற்கைச் சூழலைப் பாதுகாப்பதும் மேம்படுத்துவதும், உயிரினங்கள் மீது இரக்கம் காட்டுவதும் இந்தியாவின் ஒவ்வொரு குடிமகனின் கடமையாகும் என்று உறுப்பு 51A(g) கூறுகிறது.\nஅரசியலமைப்பு தாக்கம்: சுற்றுச்சூழல் வழக்குகளில் (எ.கா., எம்.சி. மேத்தா வழக்குகள்) உச்ச நீதிமன்றத்தால் பரவலாக மேற்கோள் காட்டப்பட்டது.\nதேர்வுப் பொறி: உறுப்பு 48A என்பது DPSP (சுற்றுச்சூழலுக்கான அரசு கடமை); உறுப்பு 51A(g) என்பது FD (சுற்றுச்சூழலுக்கான குடிமகன் கடமை).\nநினைவுச் சூத்திரம்: 51A(g) = பசுமை கடமை (சுற்றுச்சூழல் & வனவிலங்கு).",
        wno_dict={
            "A": {"en": "Incorrect. Village panchayats organisation is Art 40 (DPSP).", "ta": "தவறு. கிராம பஞ்சாயத்துகள் அமைப்பு உறுப்பு 40 (DPSP)."},
            "B": {"en": "Incorrect. Respecting National Flag/Anthem is Art 51A(a).", "ta": "தவறு. தேசியக் கொடி/கீதத்தை மதிப்பது உறுப்பு 51A(a)."},
            "C": {"en": "Correct. Article 51A(g) enjoins every citizen to protect and improve the natural environment.", "ta": "சரி. உறுப்பு 51A(g) இயற்கைச் சூழலைப் பாதுகாக்கவும் மேம்படுத்தவும் ஒவ்வொரு குடிமகனுக்கும் ஆணையிடுகிறது."},
            "D": {"en": "Incorrect. Free legal aid is Art 39A (DPSP).", "ta": "தவறு. இலவச சட்ட உதவி உறுப்பு 39A (DPSP)."}
        },
        tip_en="TNPSC Tip: Art 48A = DPSP (State duty to protect environment); Art 51A(g) = FD (Citizen duty to protect environment).",
        tip_ta="TNPSC குறிப்பு: உறுப்பு 48A = DPSP (சுற்றுச்சூழலைப் பாதுகாக்க அரசு கடமை); உறுப்பு 51A(g) = FD (சுற்றுச்சூழலைப் பாதுகாக்க குடிமகன் கடமை).",
        rev_en="Article 51A(g): Fundamental Duty to protect natural environment, forests, lakes, rivers, wildlife.",
        rev_ta="உறுப்பு 51A(g): இயற்கைச் சூழல், காடுகள், ஏரிகள், ஆறுகள், வனவிலங்குகளைப் பாதுகாப்பதற்கான அடிப்படை கடமை.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Remember", est_sec=30, pyq_sim="High", tags=["Fundamental Duties", "Article 51A", "Environment Protection"]
    ))

    # Q50 - Direct MCQ - Medium - Ans B
    qs.append(make_q(
        q_id="SF_GT_050", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="Direct MCQ",
        q_en="Under Article 280, the Finance Commission of India is constituted by the President of India at the expiration of every:",
        q_ta="உறுப்பு 280 இன் கீழ், இந்திய நிதி ஆணையம் இந்தியக் குடியரசுத் தலைவரால் எத்தனை ஆண்டுகளுக்கு ஒருமுறை அமைக்கப்படுகிறது?",
        opts_en=[
            "Three years",
            "Five years or at such earlier time as President considers necessary",
            "Six years",
            "Ten years"
        ],
        opts_ta=[
            "மூன்று ஆண்டுகள்",
            "ஐந்து ஆண்டுகள் அல்லது குடியரசுத் தலைவர் அவசியமாகக் கருதும் அதற்கு முந்தைய நேரத்தில்",
            "ஆறு ஆண்டுகள்",
            "பத்து ஆண்டுகள்"
        ],
        correct_ans="B",
        exp_en="Historical Context: Finance Commission acts as the financial balancing wheel of Indian fiscal federalism.\nReason: Under Article 280(1), the President constitutes a Finance Commission every fifth year or at such earlier time as he considers necessary.\nConstitutional Impact: Recommends distribution of net tax proceeds between Union and States and principles governing grants-in-aid.\nExam Trap: It is constituted every 5 years, NOT 6 years.\nMemory Trick: Finance Commission = 5 years fiscal balance.",
        exp_ta="வரலாற்றுப் பின்னணி: நிதி ஆணையம் இந்திய நிதி கூட்டாட்சியின் நிதி சமநிலை சக்கரமாக செயல்படுகிறது.\nகாரணம்: உறுப்பு 280(1) இன் கீழ், குடியரசுத் தலைவர் ஒவ்வொரு ஐந்தாம் ஆண்டிலும் அல்லது தான் அவசியமாகக் கருதும் அதற்கு முந்தைய நேரத்திலும் நிதி ஆணையத்தை அமைக்கிறார்.\nஅரசியலமைப்பு தாக்கம்: மத்திய அரசுக்கும் மாநிலங்களுக்கும் இடையே நிகர வரி வருவாயைப் பகிர்ந்தளிப்பதையும் மானியங்களை நிர்வகிக்கும் கோட்பாடுகளையும் பரிந்துரைக்கிறது.\nதேர்வுப் பொறி: இது ஒவ்வொரு 5 ஆண்டிற்கும் அமைக்கப்படுகிறது, 6 ஆண்டுகள் அல்ல.\nநினைவுச் சூத்திரம்: நிதி ஆணையம் = 5 ஆண்டுகள் நிதி சமநிலை.",
        wno_dict={
            "A": {"en": "Incorrect. Three years is wrong.", "ta": "தவறு. மூன்று ஆண்டுகள் என்பது தவறு."},
            "B": {"en": "Correct. Every 5 years or earlier as President considers necessary under Article 280.", "ta": "சரி. உறுப்பு 280 இன் கீழ் குடியரசுத் தலைவர் அவசியமாகக் கருதும் 5 ஆண்டுகள் அல்லது அதற்கு முந்தைய நேரத்தில்."},
            "C": {"en": "Incorrect. Six years applies to CAG/UPSC terms, not FC constitution period.", "ta": "தவறு. ஆறு ஆண்டுகள் CAG/UPSC பதவிக்காலத்திற்குப் பொருந்தும், நிதி ஆணைய அமைப்பிற்கு அல்ல."},
            "D": {"en": "Incorrect. Ten years is wrong.", "ta": "தவறு. பத்து ஆண்டுகள் என்பது தவறு."}
        },
        tip_en="TNPSC Tip: Finance Commission (Art 280) = Quasi-judicial body, constituted every 5 years by President.",
        tip_ta="TNPSC குறிப்பு: நிதி ஆணையம் (உறுப்பு 280) = அரை-நீதிமன்ற அமைப்பு, குடியரசுத் தலைவரால் ஒவ்வொரு 5 ஆண்டிற்கும் அமைக்கப்படுகிறது.",
        rev_en="Article 280: Finance Commission constituted every 5 years by President for fiscal distribution.",
        rev_ta="உறுப்பு 280: நிதிப் பகிர்விற்காகக் குடியரசுத் தலைவரால் ஒவ்வொரு 5 ஆண்டிற்கும் நிதி ஆணையம் அமைக்கப்படுகிறது.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Remember", est_sec=30, pyq_sim="High", tags=["Finance Commission", "Article 280", "Constitutional Bodies"]
    ))

    return qs

print("Part 2 defined: 25 questions.")
