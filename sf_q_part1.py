# sf_q_part1.py - Questions 1 to 25 for Salient Features Grand Test
from scratch_sf_helper import make_q

def get_part1_questions():
    qs = []
    
    # Q1 - Direct MCQ - Easy - Ans D
    qs.append(make_q(
        q_id="SF_GT_001", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Easy", question_type="Direct MCQ",
        q_en="Which feature of the Indian Constitution was primarily borrowed from the Government of India Act of 1935?",
        q_ta="இந்திய அரசியலமைப்பின் எந்த அம்சம் முதன்மையாக 1935 ஆம் ஆண்டின் இந்திய அரசுச் சட்டத்திலிருந்து பெறப்பட்டது?",
        opts_en=[
            "Fundamental Rights and Judicial Review",
            "Directive Principles of State Policy",
            "Cabinet System and Parliamentary Privileges",
            "Federal Scheme and Office of Governor"
        ],
        opts_ta=[
            "அடிப்படை உரிமைகள் மற்றும் நீதித்துறை மறுஆய்வு",
            "அரசு நெறிமுறைப்படுத்தும் கோட்பாடுகள்",
            "அமைச்சரவை முறை மற்றும் நாடாளுமன்ற சலுகைகள்",
            "கூட்டாட்சி திட்டம் மற்றும் ஆளுநர் பதவி"
        ],
        correct_ans="D",
        exp_en="Historical Context: The Government of India Act 1935 served as the structural backbone for the Indian Constitution.\nReason: Federal scheme, Office of Governor, Judiciary, Public Service Commissions, Emergency provisions, and administrative details were borrowed from the 1935 Act.\nConstitutional Impact: Over 250 provisions of the 1935 Act were incorporated directly or with modifications.\nExam Trap: Do not confuse the Office of Governor (1935 Act) with the Appointment of Governor by Centre (Canadian Constitution).\nMemory Trick: GOI Act 1935 = Structural Skeleton of Constitution.",
        exp_ta="வரலாற்றுப் பின்னணி: 1935 ஆம் ஆண்டின் இந்திய அரசுச் சட்டம் இந்திய அரசியலமைப்பின் கட்டமைப்பு முதுகெலும்பாக செயல்பட்டது.\nகாரணம்: கூட்டாட்சி திட்டம், ஆளுநர் பதவி, நீதித்துறை, அரசுப் பணியாளர் தேர்வாணையங்கள், அவசரக்கால விதிகளும் 1935 சட்டத்திலிருந்து பெறப்பட்டன.\nஅரசியலமைப்பு தாக்கம்: 1935 சட்டத்தின் 250 க்கும் மேற்பட்ட விதிகள் நேரடியாகவோ அல்லது மாற்றங்களுடனோ சேர்க்கப்பட்டன.\nதேர்வுப் பொறி: ஆளுநர் பதவியை (1935 சட்டம்) மையத்தால் ஆளுநர் நியமனத்துடன் (கனடா அரசியலமைப்பு) குழப்ப வேண்டாம்.\nநினைவுச் சூத்திரம்: 1935 அரசுச் சட்டம் = அரசியலமைப்பின் கட்டமைப்புச் சட்டகம்.",
        wno_dict={
            "A": {"en": "Incorrect. Fundamental Rights and Judicial Review were borrowed from US Constitution.", "ta": "தவறு. அடிப்படை உரிமைகள் மற்றும் நீதித்துறை மறுஆய்வு அமெரிக்க அரசியலமைப்பிலிருந்து பெறப்பட்டவை."},
            "B": {"en": "Incorrect. Directive Principles of State Policy were borrowed from Irish Constitution.", "ta": "தவறு. அரசு நெறிமுறைப்படுத்தும் கோட்பாடுகள் அயர்லாந்து அரசியலமைப்பிலிருந்து பெறப்பட்டவை."},
            "C": {"en": "Incorrect. Cabinet System and Parliamentary Privileges were borrowed from British Constitution.", "ta": "தவறு. அமைச்சரவை முறை மற்றும் நாடாளுமன்ற சலுகைகள் பிரிட்டிஷ் அரசியலமைப்பிலிருந்து பெறப்பட்டவை."},
            "D": {"en": "Correct. Federal scheme and Office of Governor were borrowed from 1935 Act.", "ta": "சரி. கூட்டாட்சி திட்டம் மற்றும் ஆளுநர் பதவி 1935 சட்டத்திலிருந்து பெறப்பட்டது."}
        },
        tip_en="TNPSC Trap: Office of Governor is from 1935 Act, but Governor's appointment by the Centre is from Canada.",
        tip_ta="TNPSC பொறி: ஆளுநர் பதவி 1935 சட்டத்திலிருந்து பெறப்பட்டது, ஆனால் ஆளுநரை மைய அரசு நியமிப்பது கனடாவிலிருந்து பெறப்பட்டது.",
        rev_en="1935 Act provided Federal Scheme, Office of Governor, Judiciary, PSCs, and Emergency Provisions.",
        rev_ta="1935 சட்டம் கூட்டாட்சி திட்டம், ஆளுநர் பதவி, நீதித்துறை, PSCs மற்றும் அவசரக்கால விதிகளை வழங்கியது.",
        sources=["M. Laxmikanth - Indian Polity", "NCERT Class XI - Indian Constitution at Work"],
        bloom="Remember", est_sec=45, pyq_sim="High", tags=["Borrowed Features", "GOI Act 1935", "Federal Scheme"]
    ))

    # Q2 - Conceptual - Medium - Ans B
    qs.append(make_q(
        q_id="SF_GT_002", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="Conceptual",
        q_en="Why is the Indian Constitution described as a 'blend of rigidity and flexibility'?",
        q_ta="இந்திய அரசியலமைப்பு ஏன் 'நெகிழும் மற்றும் நெகிழாத் தன்மையின் கலவை' என்று விவரிக்கப்படுகிறது?",
        opts_en=[
            "Because all parts of the Constitution can be amended by a simple majority of Parliament.",
            "Because some provisions require simple majority, some require special majority, and some require state ratification under Article 368.",
            "Because the Supreme Court has absolute power to alter constitutional text whenever needed.",
            "Because the Constitution can only be amended through a national referendum."
        ],
        opts_ta=[
            "ஏனெனில் அரசியலமைப்பின் அனைத்துப் பகுதிகளையும் நாடாளுமன்றத்தின் சாதாரண பெரும்பான்மையால் திருத்த முடியும்.",
            "ஏனெனில் சில விதிகள் சாதாரண பெரும்பான்மையையும், சில சிறப்பு பெரும்பான்மையையும், சில உறுப்பு 368 இன் கீழ் மாநில ஒப்புதலையும் கோருகின்றன.",
            "ஏனெனில் உச்ச நீதிமன்றத்திற்கு தேவைப்படும்போதெல்லாம் அரசியலமைப்பு உரையை மாற்ற முழு அதிகாரம் உள்ளது.",
            "ஏனெனில் அரசியலமைப்பை தேசிய பொதுவாக்கெடுப்பு மூலம் மட்டுமே திருத்த முடியும்."
        ],
        correct_ans="B",
        exp_en="Historical Context: A rigid Constitution requires a special procedure for amendment (like USA), while a flexible Constitution can be amended like ordinary laws (like UK).\nReason: India synthesizes both: Art 368 provides two types of amendments (Special Majority, Special Majority + State Ratification), while some provisions can be amended by Simple Majority outside Art 368.\nConstitutional Impact: Ensures stability while allowing adaptation to social and economic changes.\nExam Trap: Simple majority amendments are NOT considered amendments under Article 368.\nMemory Trick: Rigidity = USA, Flexibility = UK, India = Perfect Balance.",
        exp_ta="வரலாற்றுப் பின்னணி: ஒரு நெகிழா அரசியலமைப்புக்கு திருத்தத்திற்கு சிறப்பு நடைமுறை தேவைப்படுகிறது (அமெரிக்கா போன்றது), அதே நேரத்தில் நெகிழும் அரசியலமைப்பு சாதாரண சட்டங்களைப் போல திருத்தப்படலாம் (இங்கிலாந்து போன்றது).\nகாரணம்: இந்தியா இரண்டையும் இணைக்கிறது: உறுப்பு 368 இரண்டு வகையான திருத்தங்களை வழங்குகிறது, அதே நேரத்தில் உறுப்பு 368 க்கு வெளியே சில விதிகளை சாதாரண பெரும்பான்மையால் திருத்தலாம்.\nஅரசியலமைப்பு தாக்கம்: சமூக மற்றும் பொருளாதார மாற்றங்களுக்கு ஏற்ப மாற்றியமைக்க அனுமதிக்கும் அதே வேளையில் ஸ்திரத்தன்மையை உறுதி செய்கிறது.\nதேர்வுப் பொறி: சாதாரண பெரும்பான்மை திருத்தங்கள் உறுப்பு 368 இன் கீழ் திருத்தங்களாகக் கருதப்படுவதில்லை.\nநினைவுச் சூத்திரம்: நெகிழாத் தன்மை = அமெரிக்கா, நெகிழும் தன்மை = இங்கிலாந்து, இந்தியா = சரியான சமநிலை.",
        wno_dict={
            "A": {"en": "Incorrect. All parts cannot be amended by simple majority; most require special majority.", "ta": "தவறு. அனைத்துப் பகுதிகளையும் சாதாரண பெரும்பான்மையால் திருத்த முடியாது; பெரும்பாலனவற்றிக்கு சிறப்பு பெரும்பான்மை தேவை."},
            "B": {"en": "Correct. Synthesis of simple, special, and special with state ratification.", "ta": "சரி. சாதாரண, சிறப்பு மற்றும் மாநில ஒப்புதலுடன் கூடிய சிறப்பு பெரும்பான்மையின் கலவை."},
            "C": {"en": "Incorrect. The Supreme Court interprets Constitution, it cannot rewrite constitutional text.", "ta": "தவறு. உச்ச நீதிமன்றம் அரசியலமைப்பை விளக்குகிறது, அரசியலமைப்பு உரையை மீண்டும் எழுத முடியாது."},
            "D": {"en": "Incorrect. India does not use national referendum for constitutional amendments.", "ta": "தவறு. அரசியலமைப்பு திருத்தங்களுக்கு இந்தியா தேசிய பொதுவாக்கெடுப்பைப் பயன்படுத்துவதில்லை."}
        },
        tip_en="TNPSC Tip: Amendments under Article 368 require either Special Majority OR Special Majority + 50% State Legislature Ratification.",
        tip_ta="TNPSC குறிப்பு: உறுப்பு 368 இன் கீழ் திருத்தங்களுக்கு சிறப்பு பெரும்பான்மை அல்லது சிறப்பு பெரும்பான்மை + 50% மாநில சட்டமன்ற ஒப்புதல் தேவை.",
        rev_en="Article 368 contains 2 amendment types; simple majority amendments fall outside Article 368.",
        rev_ta="உறுப்பு 368 இரண்டு திருத்த வகைகளைக் கொண்டுள்ளது; சாதாரண பெரும்பான்மை திருத்தங்கள் உறுப்பு 368 க்கு வெளியே வருகின்றன.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Understand", est_sec=60, pyq_sim="High", tags=["Rigidity and Flexibility", "Article 368", "Amendment"]
    ))

    # Q3 - Assertion & Reason - Hard - Ans A
    qs.append(make_q(
        q_id="SF_GT_003", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Hard", question_type="Assertion & Reason",
        q_en="Given below are two statements, one labeled as Assertion (A) and the other labeled as Reason (R):\n\nAssertion (A): The Indian Constitution contains genuine Federal features like a Written Constitution and Division of Powers.\nReason (R): Single Citizenship and an Integrated Judiciary are Unitary features that strengthen central authority over the federation.",
        q_ta="கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிக்கப்பட்டுள்ளது:\n\nகூற்று (A): இந்திய அரசியலமைப்பு எழுதப்பட்ட அரசியலமைப்பு மற்றும் அதிகாரப் பகிர்வு போன்ற உண்மையான கூட்டாட்சி அம்சங்களைக் கொண்டுள்ளது.\nகாரணம் (R): ஒற்றைக் குடியுரிமை மற்றும் ஒருங்கிணைந்த நீதித்துறை ஆகியவை கூட்டாட்சியின் மீது மத்திய அதிகாரத்தை வலுப்படுத்தும் ஒற்றையாட்சி அம்சங்களாகும்.",
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
        exp_en="Historical Context: Indian Constitution incorporates both Federal and Unitary features.\nReason: Both (A) and (R) are true. Federal features include Written Constitution & Division of Powers. Unitary features include Single Citizenship & Integrated Judiciary.\nConstitutional Impact: Creates a Quasi-Federal structure.\nExam Trap: Do not confuse Federal features with Unitary features.",
        exp_ta="வரலாற்றுப் பின்னணி: இந்திய அரசியலமைப்பு கூட்டாட்சி மற்றும் ஒற்றையாட்சி அம்சங்கள் இரண்டையும் உள்ளடக்கியுள்ளது.\nகாரணம்: (A) மற்றும் (R) இரண்டும் சரி. கூட்டாட்சி அம்சங்களில் எழுதப்பட்ட அரசியலமைப்பு & அதிகாரப் பகிர்வு அடங்கும். ஒற்றையாட்சி அம்சங்களில் ஒற்றைக் குடியுரிமை & ஒருங்கிணைந்த நீதித்துறை அடங்கும்.\nஅரசியலமைப்பு தாக்கம்: ஒரு அரை-கூட்டாட்சி அமைப்பை உருவாக்குகிறது.\nதேர்வுப் பொறி: கூட்டாட்சி அம்சங்களை ஒற்றையாட்சி அம்சங்களுடன் குழப்ப வேண்டாம்.",
        wno_dict={
            "A": {"en": "Correct. Both statements are true and (R) accurately contrasts unitary features with federal ones.", "ta": "சரி. இரு கூற்றுகளும் சரி, மற்றும் (R) ஒற்றையாட்சி அம்சங்களைக் கூட்டாட்சி அம்சங்களுடன் துல்லியமாக வேறுபடுத்துகிறது."},
            "B": {"en": "Incorrect. (R) explains the dual nature of Indian federalism.", "ta": "தவறு. (R) இந்திய கூட்டாட்சியின் இரட்டைத் தன்மையை விளக்குகிறது."},
            "C": {"en": "Incorrect. (R) is true.", "ta": "தவறு. (R) உண்மை."},
            "D": {"en": "Incorrect. (A) is true.", "ta": "தவறு. (A) உண்மை."}
        },
        tip_en="TNPSC Tip: Federal = Division of powers, Written Constitution, Bicameralism; Unitary = Single Citizenship, Integrated Judiciary.",
        tip_ta="TNPSC குறிப்பு: கூட்டாட்சி = அதிகாரப் பகிர்வு, எழுதப்பட்ட அரசியலமைப்பு, ஈரவை முறை; ஒற்றையாட்சி = ஒற்றைக் குடியுரிமை, ஒருங்கிணைந்த நீதித்துறை.",
        rev_en="Federal features (Written Constitution, Division of Powers) vs Unitary features (Single Citizenship, Integrated Judiciary).",
        rev_ta="கூட்டாட்சி அம்சங்கள் (எழுதப்பட்ட அரசியலமைப்பு, அதிகாரப் பகிர்வு) vs ஒற்றையாட்சி அம்சங்கள் (ஒற்றைக் குடியுரிமை, ஒருங்கிணைந்த நீதித்துறை).",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Analyze", est_sec=60, pyq_sim="High", tags=["Federal Features", "Unitary Features", "Assertion Reason"]
    ))

    # Q4 - Assertion & Reason - Medium - Ans A
    qs.append(make_q(
        q_id="SF_GT_004", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="Assertion & Reason",
        q_en="Given below are two statements, one labeled as Assertion (A) and the other labeled as Reason (R):\n\nAssertion (A): The Indian Parliamentary system differs significantly from the British Parliamentary system.\nReason (R): India has an elected Head of State (Republic) and Indian Parliament is not a sovereign body.",
        q_ta="கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிக்கப்பட்டுள்ளது:\n\nகூற்று (A): இந்திய நாடாளுமன்ற முறை பிரிட்டிஷ் நாடாளுமன்ற முறையிலிருந்து கணிசமாக வேறுபடுகிறது.\nகாரணம் (R): இந்தியாவில் தேர்ந்தெடுக்கப்பட்ட நாட்டின் தலைவர் (குடியரசு) உள்ளார் மற்றும் இந்திய நாடாளுமன்றம் ஒரு இறையாண்மை கொண்ட அமைப்பு அல்ல.",
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
        exp_en="Historical Context: India adopted the British Westminster model of Parliamentary government but introduced major adaptations.\nReason: Unlike Britain's hereditary monarchy, India is a Republic with an elected President. Unlike Britain's sovereign Parliament, Indian Parliament is subject to a written Constitution and Judicial Review.\nConstitutional Impact: Synthesis of Parliamentary democracy with Constitutional Supremacy.\nExam Trap: Do not assume Parliamentary system implies total parliamentary sovereignty as in UK.\nMemory Trick: UK = Monarchy + Sovereign Parliament; India = Republic + Constitutional Supremacy.",
        exp_ta="வரலாற்றுப் பின்னணி: இந்தியா பிரித்தானிய வெஸ்ட்மின்ஸ்டர் நாடாளுமன்ற ஆட்சி முறையை ஏற்றுக்கொண்டது, ஆனால் முக்கிய மாற்றங்களை அறிமுகப்படுத்தியது.\nகாரணம்: பிரித்தானியாவின் வம்சாவளி முடியாட்சி போலல்லாமல், இந்தியா தேர்ந்தெடுக்கப்பட்ட குடியரசுத் தலைவரைக் கொண்ட ஒரு குடியரசாகும். பிரித்தானியாவின் இறையாண்மை கொண்ட நாடாளுமன்றத்தைப் போலல்லாமல், இந்திய நாடாளுமன்றம் எழுதப்பட்ட அரசியலமைப்பு மற்றும் நீதித்துறை மறுஆய்வுக்கு உட்பட்டது.\nஅரசியலமைப்பு தாக்கம்: நாடாளுமன்ற ஜனநாயகத்தை அரசியலமைப்பு மேலாதிக்கத்துடன் இணைத்தல்.\nதேர்வுப் பொறி: இங்கிலாந்தைப்போல நாடாளுமன்ற முறை என்றால் நாடாளுமன்ற இறையாண்மை இருக்கும் என்று கருதவேண்டாம்.\nநினைவுச் சூத்திரம்: இங்கிலாந்து = முடியாட்சி + இறையாண்மை நாடாளுமன்றம்; இந்தியா = குடியரசு + அரசியலமைப்பு மேலாதிக்கம்.",
        wno_dict={
            "A": {"en": "Correct. Both (A) and (R) are true, and (R) explains why the two systems differ.", "ta": "சரி. (A) மற்றும் (R) இரண்டும் சரி, மற்றும் (R) இரு அமைப்புகளும் எவ்வாறு வேறுபடுகின்றன என்பதை விளக்குகிறது."},
            "B": {"en": "Incorrect. (R) is indeed the direct reason for (A).", "ta": "தவறு. (R) என்பது (A)-க்கான நேரடி காரணம்."},
            "C": {"en": "Incorrect. (R) is completely true.", "ta": "தவறு. (R) முற்றிலும் உண்மை."},
            "D": {"en": "Incorrect. (A) is true, not false.", "ta": "தவறு. (A) உண்மையானது, தவறானது அல்ல."}
        },
        tip_en="TNPSC Tip: British Parliament is sovereign; Indian Parliament is limited by written constitution and fundamental rights.",
        tip_ta="TNPSC குறிப்பு: பிரிட்டிஷ் நாடாளுமன்றம் இறையாண்மை கொண்டது; இந்திய நாடாளுமன்றம் எழுதப்பட்ட அரசியலமைப்பு மற்றும் அடிப்படை உரிமைகளால் வரம்பிற்கு உட்பட்டது.",
        rev_en="India = Republic (elected President) + Non-sovereign Parliament (bound by Constitution).",
        rev_ta="இந்தியா = குடியரசு (தேர்ந்தெடுக்கப்பட்ட குடியரசுத் தலைவர்) + இறையாண்மையற்ற நாடாளுமன்றம் (அரசியலமைப்பிற்கு கட்டுப்பட்டது).",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Evaluate", est_sec=75, pyq_sim="High", tags=["Parliamentary System", "Republic", "Constitutional Supremacy"]
    ))

    # Q5 - Match the Following - Medium - Ans D
    qs.append(make_q(
        q_id="SF_GT_005", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="Match the Following",
        q_en="Match List-I (Borrowed Features) with List-II (Source Country) and select the correct answer using the codes given below:\n\nList-I:\n(a) Advisory Jurisdiction of Supreme Court\n(b) Concurrent List\n(c) Nomination of Members to Rajya Sabha\n(d) Cabinet System\n\nList-II:\n1. Irish Constitution\n2. British Constitution\n3. Canadian Constitution\n4. Australian Constitution",
        q_ta="பட்டியல்-I (பெறப்பட்ட அம்சங்கள்) உடன் பட்டியல்-II (மூல நாடு) ஐப் பொருத்தி, கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான பதிலதைத் தேர்ந்தெடுக்கவும்:\n\nபட்டியல்-I:\n(a) உச்ச நீதிமன்றத்தின் ஆலோசனைக் அதிகார வரம்பு\n(b) பொதுப் பட்டியல்\n(c) மாநிலங்களவை உறுப்பினர்கள் நியமனம்\n(d) அமைச்சரவை முறை\n\nபட்டியல்-II:\n1. அயர்லாந்து அரசியலமைப்பு\n2. பிரிட்டிஷ் அரசியலமைப்பு\n3. கனடா அரசியலமைப்பு\n4. ஆஸ்திரேலியா அரசியலமைப்பு",
        opts_en=[
            "(a)-4, (b)-3, (c)-2, (d)-1",
            "(a)-3, (b)-1, (c)-4, (d)-2",
            "(a)-1, (b)-4, (c)-3, (d)-2",
            "(a)-3, (b)-4, (c)-1, (d)-2"
        ],
        opts_ta=[
            "(a)-4, (b)-3, (c)-2, (d)-1",
            "(a)-3, (b)-1, (c)-4, (d)-2",
            "(a)-1, (b)-4, (c)-3, (d)-2",
            "(a)-3, (b)-4, (c)-1, (d)-2"
        ],
        correct_ans="D",
        exp_en="Historical Context: Framing of Indian Constitution involved borrowing provisions from diverse global democratic constitutions.\nReason: Advisory Jurisdiction of SC = Canada (3); Concurrent List = Australia (4); Nomination of RS Members = Ireland (1); Cabinet System = Britain (2).\nConstitutional Impact: Adapted proven international constitutional principles to suit Indian needs.\nExam Trap: Do not confuse Nomination of RS Members (Ireland) with Election of RS Members (South Africa).\nMemory Trick: Canada Advisory, Australia Concurrent, Ireland Nomination, Britain Cabinet.",
        exp_ta="வரலாற்றுப் பின்னணி: இந்திய அரசியலமைப்பை உருவாக்குவது பல்வேறு உலகளாவிய ஜனநாயக அரசியலமைப்புகளிலிருந்து விதிகளைப் பெறுவதை உள்ளடக்கியது.\nகாரணம்: உச்ச நீதிமன்ற ஆலோசனைக் வரம்பு = கனடா (3); பொதுப் பட்டியல் = ஆஸ்திரேலியா (4); மாநிலங்களவை உறுப்பினர்கள் நியமனம் = அயர்லாந்து (1); அமைச்சரவை முறை = இங்கிலாந்து (2).\nஅரசியலமைப்பு தாக்கம்: இந்திய தேவைகளுக்கு ஏற்ப நிரூபிக்கப்பட்ட சர்வதேச அரசியலமைப்பு கோட்பாடுகளை மாற்றியமைத்தது.\nதேர்வுப் பொறி: மாநிலங்களவை உறுப்பினர் நியமனத்தையும் (அயர்லாந்து) மாநிலங்களவை உறுப்பினர் தேர்தலையும் (தென்னாப்பிரிக்கா) குழப்ப வேண்டாம்.\nநினைவுச் சூத்திரம்: கனடா ஆலோசனை, ஆஸ்திரேலியா பொதுப்பட்டியல், அயர்லாந்து நியமனம், இங்கிலாந்து அமைச்சரவை.",
        wno_dict={
            "A": {"en": "Incorrect. Advisory jurisdiction is Canada (3), not Australia (4).", "ta": "தவறு. ஆலோசனைக் அதிகார வரம்பு கனடா (3), ஆஸ்திரேலியா (4) அல்ல."},
            "B": {"en": "Incorrect. Concurrent list is Australia (4), not Ireland (1).", "ta": "தவறு. பொதுப் பட்டியல் ஆஸ்திரேலியா (4), அயர்லாந்து (1) அல்ல."},
            "C": {"en": "Incorrect. Advisory jurisdiction is Canada (3), not Ireland (1).", "ta": "தவறு. ஆலோசனைக் அதிகார வரம்பு கனடா (3), அயர்லாந்து (1) அல்ல."},
            "D": {"en": "Correct. (a)-3, (b)-4, (c)-1, (d)-2 matches all borrowed features accurately.", "ta": "சரி. (a)-3, (b)-4, (c)-1, (d)-2 அனைத்து பெறப்பட்ட அம்சங்களையும் துல்லியமாகப் பொருத்துகிறது."}
        },
        tip_en="TNPSC Trap: RS Nomination = Ireland; RS Election = South Africa.",
        tip_ta="TNPSC பொறி: மாநிலங்களவை நியமனம் = அயர்லாந்து; மாநிலங்களவை தேர்தல் = தென்னாப்பிரிக்கா.",
        rev_en="Advisory SC Jurisdiction (Canada), Concurrent List (Australia), RS Nomination (Ireland), Cabinet (UK).",
        rev_ta="உச்ச நீதிமன்ற ஆலோசனை வரம்பு (கனடா), பொதுப் பட்டியல் (ஆஸ்திரேலியா), மாநிலங்களவை நியமனம் (அயர்லாந்து), அமைச்சரவை (இங்கிலாந்து).",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Remember", est_sec=60, pyq_sim="High", tags=["Borrowed Features", "Match the Following", "Sources"]
    ))

    # Q6 - Chronology - Hard - Ans D
    qs.append(make_q(
        q_id="SF_GT_006", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Hard", question_type="Chronology",
        q_en="Arrange the following Constitutional Amendments in chronological order of their enactment:\n1. 61st Amendment Act (Reduction of voting age to 18 years)\n2. 42nd Amendment Act (Addition of Fundamental Duties)\n3. 44th Amendment Act (Removal of Right to Property as FR)\n4. 86th Amendment Act (Addition of 11th Fundamental Duty)",
        q_ta="பின்வரும் அரசியலமைப்பு திருத்தங்களை அவை இயற்றப்பட்ட காலவரிசைப்படி வரிசைப்படுத்தவும்:\n1. 61வது திருத்தச் சட்டம் (வாக்களிக்கும் வயதை 18 ஆகக் குறைத்தல்)\n2. 42வது திருத்தச் சட்டம் (அடிப்படை கடமைகள் சேர்ப்பு)\n3. 44வது திருத்தச் சட்டம் (சொத்து உரிமையை அடிப்படை உரிமையிலிருந்து நீக்குதல்)\n4. 86வது திருத்தச் சட்டம் (11வது அடிப்படை கடமை சேர்ப்பு)",
        opts_en=[
            "2 - 1 - 3 - 4",
            "3 - 2 - 1 - 4",
            "2 - 3 - 4 - 1",
            "2 - 3 - 1 - 4"
        ],
        opts_ta=[
            "2 - 1 - 3 - 4",
            "3 - 2 - 1 - 4",
            "2 - 3 - 4 - 1",
            "2 - 3 - 1 - 4"
        ],
        correct_ans="D",
        exp_en="Historical Context: Constitutional amendment trajectory reflects evolving democratic priorities.\nReason:\n2. 42nd Amendment Act: Enacted in 1976 (Mini-Constitution, added Part IVA FD).\n3. 44th Amendment Act: Enacted in 1978 (Removed Right to Property from Part III).\n1. 61st Amendment Act: Enacted in 1988 (Reduced voting age from 21 to 18, enforced 1989).\n4. 86th Amendment Act: Enacted in 2002 (Right to Education Art 21A & 11th Duty).\nSequence: 2 (1976) -> 3 (1978) -> 1 (1988) -> 4 (2002).\nExam Trap: 61st Amendment was passed in 1988, not in the 1970s.",
        exp_ta="வரலாற்றுப் பின்னணி: அரசியலமைப்பு திருத்தங்களின் வளர்ச்சி வளர்ந்து வரும் ஜனநாயக முன்னுரிமைகளைப் பிரதிபலிக்கிறது.\nகாரணம்:\n2. 42வது திருத்தச் சட்டம்: 1976 இல் இயற்றப்பட்டது (குறு-அரசியலமைப்பு, பகுதி IVA அடிப்படை கடமைகளைச் சேர்த்தது).\n3. 44வது திருத்தச் சட்டம்: 1978 இல் இயற்றப்பட்டது (பகுதி III லிருந்து சொத்து உரிமையை நீக்கியது).\n1. 61வது திருத்தச் சட்டம்: 1988 இல் இயற்றப்பட்டது (வாக்களிக்கும் வயதை 21 லிருந்து 18 ஆகக் குறைத்தது, 1989 இல் நடைமுறைக்கு வந்தது).\n4. 86வது திருத்தச் சட்டம்: 2002 இல் இயற்றப்பட்டது (கல்வி உரிமை உறுப்பு 21A & 11வது அடிப்படை கடமை).\nவரிசை: 2 (1976) -> 3 (1978) -> 1 (1988) -> 4 (2002).",
        wno_dict={
            "A": {"en": "Incorrect. 44th Amendment (1978) came BEFORE 61st Amendment (1988).", "ta": "தவறு. 44வது திருத்தம் (1978) 61வது திருத்தத்திற்கு (1988) முன்பே வந்தது."},
            "B": {"en": "Incorrect. 42nd Amendment (1976) came BEFORE 44th Amendment (1978).", "ta": "தவறு. 42வது திருத்தம் (1976) 44வது திருத்தத்திற்கு (1978) முன்பே வந்தது."},
            "C": {"en": "Incorrect. 86th Amendment (2002) came AFTER 61st Amendment (1988).", "ta": "தவறு. 86வது திருத்தம் (2002) 61வது திருத்தத்திற்கு (1988) பிந்தையது."},
            "D": {"en": "Correct. 42nd (1976) -> 44th (1978) -> 61st (1988) -> 86th (2002).", "ta": "சரி. 42வது (1976) -> 44வது (1978) -> 61வது (1988) -> 86வது (2002)."}
        },
        tip_en="TNPSC Tip: Remember years: 42nd (1976), 44th (1978), 61st (1988), 86th (2002).",
        tip_ta="TNPSC குறிப்பு: ஆண்டுகளை நினைவில் கொள்க: 42வது (1976), 44வது (1978), 61வது (1988), 86வது (2002).",
        rev_en="42nd (1976) added FDs; 44th (1978) removed Prop FR; 61st (1988) voting age 18; 86th (2002) RTE.",
        rev_ta="42வது (1976) FDகளைச் சேர்த்தது; 44வது (1978) சொத்து உரிமையை நீக்கியது; 61வது (1988) வாக்கு வயது 18; 86வது (2002) RTE.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Analyze", est_sec=90, pyq_sim="High", tags=["Amendments", "Chronology", "Fundamental Duties"]
    ))

    # Q7 - Hard / Analytical - Hard - Ans C
    qs.append(make_q(
        q_id="SF_GT_007", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Hard", question_type="Hard / Analytical",
        q_en="Which of the following observers characterized the Indian Constitution as a 'Federation with strong centralizing tendency'?",
        q_ta="பின்வரும் பார்வையாளர்களில் யார் இந்திய அரசியலமைப்பை 'வலுவான மையப்போக்கு கொண்ட கூட்டாட்சி' (Federation with strong centralizing tendency) என்று வகைப்படுத்தினார்?",
        opts_en=[
            "K.C. Wheare",
            "Granville Austin",
            "Sir Ivor Jennings",
            "Morris Jones"
        ],
        opts_ta=[
            "கே.சி. வேர்",
            "கிரான்வில் ஆஸ்டின்",
            "சர் ஐவர் ஜென்னிங்ஸ்",
            "மோரிஸ் ஜோன்ஸ்"
        ],
        correct_ans="C",
        exp_en="Historical Context: Constitutional scholars have described the unique nature of Indian federalism using distinct analytical terminology.\nReason: Sir Ivor Jennings termed it a 'Federation with strong centralizing tendency'. K.C. Wheare called it 'Quasi-Federal'. Granville Austin termed it 'Cooperative Federalism'. Morris Jones described it as 'Bargaining Federalism'.\nConstitutional Impact: Highlights that Indian federalism is centralist by design to preserve national integrity.\nExam Trap: Match each constitutional scholar directly with their precise quotation.\nMemory Trick: Jennings = Centralizing tendency, Wheare = Quasi-federal, Austin = Cooperative, Jones = Bargaining.",
        exp_ta="வரலாற்றுப் பின்னணி: அரசியலமைப்பு அறிஞர்கள் இந்தியக் கூட்டாட்சியின் தனித்துவமான தன்மையை வேறுபட்ட பகுப்பாய்வு சொற்களைப் பயன்படுத்தி விவரித்துள்ளனர்.\nகாரணம்: சர் ஐவர் ஜென்னிங்ஸ் அதை 'வலுவான மையப்போக்கு கொண்ட கூட்டாட்சி' என்று அழைத்தார். கே.சி. வேர் அதை 'அரை-கூட்டாட்சி' (Quasi-Federal) என்று அழைத்தார். கிரான்வில் ஆஸ்டின் 'கூட்டுறவு கூட்டாட்சி' என்று அழைத்தார். மோரிஸ் ஜோன்ஸ் அதை 'பேரப் பேச்சு கூட்டாட்சி' என்று விவரித்தார்.\nஅரசியலமைப்பு தாக்கம்: தேசிய ஒருமைப்பாட்டைப் பேணுவதற்காக இந்தியக் கூட்டாட்சி மையப்படுத்தப்பட்ட வடிவமைப்பைக் கொண்டுள்ளது என்பதைச் சுட்டிக்காட்டுகிறது.\nதேர்வுப் பொறி: ஒவ்வொரு அரசியலமைப்பு அறிஞரையும் அவர்களின் துல்லியமான மேற்கோளுடன் நேரடியாகப் பொருத்துங்கள்.\nநினைவுச் சூத்திரம்: ஜென்னிங்ஸ் = மையப்போக்கு, வேர் = அரை-கூட்டாட்சி, ஆஸ்டின் = கூட்டுறவு, ஜோன்ஸ் = பேரம்பேசுதல்.",
        wno_dict={
            "A": {"en": "Incorrect. K.C. Wheare described it as 'Quasi-Federal'.", "ta": "தவறு. கே.சி. வேர் அதை 'அரை-கூட்டாட்சி' என்று விவரித்தார்."},
            "B": {"en": "Incorrect. Granville Austin called it 'Cooperative Federalism'.", "ta": "தவறு. கிரான்வில் ஆஸ்டின் அதை 'கூட்டுறவு கூட்டாட்சி' என்று அழைத்தார்."},
            "C": {"en": "Correct. Sir Ivor Jennings termed it 'Federation with strong centralizing tendency'.", "ta": "சரி. சர் ஐவர் ஜென்னிங்ஸ் அதை 'வலுவான மையப்போக்கு கொண்ட கூட்டாட்சி' என்று குறிப்பிட்டார்."},
            "D": {"en": "Incorrect. Morris Jones characterized it as 'Bargaining Federalism'.", "ta": "தவறு. மோரிஸ் ஜோன்ஸ் அதை 'பேரப் பேச்சு கூட்டாட்சி' என்று வகைப்படுத்தினார்."}
        },
        tip_en="TNPSC Trap: Jennings = Centralizing tendency; Wheare = Quasi-federal; Austin = Cooperative; Jones = Bargaining.",
        tip_ta="TNPSC பொறி: ஜென்னிங்ஸ் = மையப்போக்கு; வேர் = அரை-கூட்டாட்சி; ஆஸ்டின் = கூட்டுறவு; ஜோன்ஸ் = பேரம்பேசுதல்.",
        rev_en="Four Scholar Quotes: Jennings (Centralizing), Wheare (Quasi-federal), Austin (Cooperative), Jones (Bargaining).",
        rev_ta="நான்கு அறிஞர் மேற்கோள்கள்: ஜென்னிங்ஸ் (மையப்போக்கு), வேர் (அரை-கூட்டாட்சி), ஆஸ்டின் (கூட்டுறவு), ஜோன்ஸ் (பேரம்பேசுதல்).",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Analyze", est_sec=60, pyq_sim="High", tags=["Federalism", "Scholar Descriptions", "Sir Ivor Jennings"]
    ))

    # Q8 - Direct MCQ - Easy - Ans D
    qs.append(make_q(
        q_id="SF_GT_008", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Easy", question_type="Direct MCQ",
        q_en="Which Part of the Indian Constitution contains the Fundamental Rights of citizens?",
        q_ta="இந்திய அரசியலமைப்பின் எந்தப் பகுதியில் குடிமக்களின் அடிப்படை உரிமைகள் உள்ளன?",
        opts_en=[
            "Part II",
            "Part IV",
            "Part IVA",
            "Part III"
        ],
        opts_ta=[
            "பகுதி II",
            "பகுதி IV",
            "பகுதி IVA",
            "பகுதி III"
        ],
        correct_ans="D",
        exp_en="Historical Context: Part III of the Constitution is described as the 'Magna Carta of India'.\nReason: Fundamental Rights are enshrined in Part III from Articles 12 to 35.\nConstitutional Impact: Ensures political democracy and protects citizens from arbitrary state executive and legislative action.\nExam Trap: Part II is Citizenship, Part III is Fundamental Rights, Part IV is DPSP, Part IVA is Fundamental Duties.\nMemory Trick: Part III = 3 words = Magna Carta India.",
        exp_ta="வரலாற்றுப் பின்னணி: அரசியலமைப்பின் பகுதி III இந்தியாவின் 'மகா சாசனம்' (Magna Carta of India) என்று விவரிக்கப்படுகிறது.\nகாரணம்: அடிப்படை உரிமைகள் உறுப்பு 12 முதல் 35 வரை பகுதி III இல் சேர்க்கப்பட்டுள்ளன.\nஅரசியலமைப்பு தாக்கம்: அரசியல் ஜனநாயகத்தை உறுதிசெய்து, தன்னிச்சையான அரசு நிர்வாக மற்றும் சட்டமன்ற நடவடிக்கைகளிலிருந்து குடிமக்களைப் பாதுகாக்கிறது.\nதேர்வுப் பொறி: பகுதி II குடியுரிமை, பகுதி III அடிப்படை உரிமைகள், பகுதி IV அரசு நெறிமுறை கோட்பாடுகள், பகுதி IVA அடிப்படை கடமைகள்.\nநினைவுச் சூத்திரம்: பகுதி III = 3 சொற்கள் = மகா சாசனம் இந்தியா.",
        wno_dict={
            "A": {"en": "Incorrect. Part II deals with Citizenship (Articles 5-11).", "ta": "தவறு. பகுதி II குடியுரிமை பற்றியது (உறுப்புகள் 5-11)."},
            "B": {"en": "Incorrect. Part IV deals with Directive Principles of State Policy (Articles 36-51).", "ta": "தவறு. பகுதி IV அரசு நெறிமுறை கோட்பாடுகள் பற்றியது (உறுப்புகள் 36-51)."},
            "C": {"en": "Incorrect. Part IVA deals with Fundamental Duties (Article 51A).", "ta": "தவறு. பகுதி IVA அடிப்படை கடமைகள் பற்றியது (உறுப்பு 51A)."},
            "D": {"en": "Correct. Part III contains Fundamental Rights (Articles 12-35).", "ta": "சரி. பகுதி III அடிப்படை உரிமைகளைக் கொண்டுள்ளது (உறுப்புகள் 12-35)."}
        },
        tip_en="TNPSC Tip: Part III = Fundamental Rights (12-35); Part IV = DPSP (36-51); Part IVA = Fundamental Duties (51A).",
        tip_ta="TNPSC குறிப்பு: பகுதி III = அடிப்படை உரிமைகள் (12-35); பகுதி IV = DPSP (36-51); பகுதி IVA = அடிப்படை கடமைகள் (51A).",
        rev_en="Part III = Fundamental Rights (Articles 12-35), Magna Carta of India.",
        rev_ta="பகுதி III = அடிப்படை உரிமைகள் (உறுப்புகள் 12-35), இந்தியாவின் மகா சாசனம்.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Remember", est_sec=30, pyq_sim="High", tags=["Fundamental Rights", "Part III", "Magna Carta"]
    ))

    # Q9 - PYQ Pattern - Medium - Ans A
    qs.append(make_q(
        q_id="SF_GT_009", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="PYQ Pattern",
        q_en="By which Constitutional Amendment Act was the voting age reduced from 21 years to 18 years in India?",
        q_ta="எந்த அரசியலமைப்பு திருத்தச் சட்டத்தின் மூலம் இந்தியாவில் வாக்களிக்கும் வயது 21 லிருந்து 18 ஆகக் குறைக்கப்பட்டது?",
        opts_en=[
            "61st Constitutional Amendment Act, 1988",
            "42nd Constitutional Amendment Act, 1976",
            "44th Constitutional Amendment Act, 1978",
            "73rd Constitutional Amendment Act, 1992"
        ],
        opts_ta=[
            "61வது அரசியலமைப்பு திருத்தச் சட்டம், 1988",
            "42வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
            "44வது அரசியலமைப்பு திருத்தச் சட்டம், 1978",
            "73வது அரசியலமைப்பு திருத்தச் சட்டம், 1992"
        ],
        correct_ans="A",
        exp_en="Historical Context: Universal Adult Franchise was further democratized by expanding political rights to youth.\nReason: The 61st Constitutional Amendment Act, 1988 (enforced in March 1989) amended Article 326 to reduce the voting age from 21 to 18 years during Rajiv Gandhi's tenure.\nConstitutional Impact: Significantly widened the electorate and enhanced political participation.\nExam Trap: Passed in 1988, came into force on March 28, 1989.\nMemory Trick: 61st Amendment = 6+1=7... 18 years vote power.",
        exp_ta="வரலாற்றுப் பின்னணி: இளைஞர்களுக்கு அரசியல் உரிமைகளை விரிவாக்குவதன் மூலம் உலகளாவிய வயதுவந்தோர் வாக்குரிமை மேலும் ஜனநாயகப்படுத்தப்பட்டது.\nகாரணம்: 61வது அரசியலமைப்பு திருத்தச் சட்டம், 1988 (மார்ச் 1989 இல் நடைமுறைக்கு வந்தது) ராஜீவ் காந்தி ஆட்சிக் காலத்தில் வாக்களிக்கும் வயதை 21 லிருந்து 18 ஆகக் குறைக்க உறுப்பு 326 ஐத் திருத்தியது.\nஅரசியலமைப்பு தாக்கம்: வாக்காளர் பட்டியலை கணிசமாக விரிவுபடுத்தி அரசியல் பங்கேற்பை அதிகரித்தது.\nதேர்வுப் பொறி: 1988 இல் நிறைவேற்றப்பட்டது, மார்ச் 28, 1989 இல் நடைமுறைக்கு வந்தது.\nநினைவுச் சூத்திரம்: 61வது திருத்தம் = 18 வயது வாக்கு அதிகாரம்.",
        wno_dict={
            "A": {"en": "Correct. 61st Amendment Act, 1988 reduced voting age to 18.", "ta": "சரி. 61வது திருத்தச் சட்டம், 1988 வாக்களிக்கும் வயதை 18 ஆகக் குறைத்தது."},
            "B": {"en": "Incorrect. 42nd Amendment 1976 added Fundamental Duties, Preamble changes, etc.", "ta": "தவறு. 42வது திருத்தம் 1976 அடிப்படை கடமைகள், முகவுரை மாற்றங்கள் போன்றவற்றைச் சேர்த்தது."},
            "C": {"en": "Incorrect. 44th Amendment 1978 modified emergency rules and right to property.", "ta": "தவறு. 44வது திருத்தம் 1978 அவசரக்கால விதிகள் மற்றும் சொத்து உரிமையை மாற்றியமைத்தது."},
            "D": {"en": "Incorrect. 73rd Amendment 1992 granted constitutional status to Panchayati Raj.", "ta": "தவறு. 73வது திருத்தம் 1992 பஞ்சாயத்து ராஜிற்கு அரசியலமைப்பு அந்தஸ்தை வழங்கியது."}
        },
        tip_en="TNPSC Tip: Article 326 deals with Universal Adult Franchise and was amended by 61st Amendment 1988.",
        tip_ta="TNPSC குறிப்பு: உறுப்பு 326 உலகளாவிய வயதுவந்தோர் வாக்குரிமை பற்றியது மற்றும் 61வது திருத்தம் 1988 மூலம் திருத்தப்பட்டது.",
        rev_en="Article 326 amended by 61st Amendment Act 1988 (effective 1989): Voting age 21 -> 18.",
        rev_ta="உறுப்பு 326 61வது திருத்தச் சட்டம் 1988 மூலம் திருத்தப்பட்டது (1989 முதல் நடைமுறை): வாக்கு வயது 21 -> 18.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Remember", est_sec=30, pyq_sim="Direct PYQ", tags=["Universal Adult Franchise", "Article 326", "61st Amendment"]
    ))

    # Q10 - TNPSC Trap - Hard - Ans B
    qs.append(make_q(
        q_id="SF_GT_010", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Hard", question_type="TNPSC Trap",
        q_en="Which of the following statements regarding the Right to Property is TRULY accurate in the current constitutional framework?",
        q_ta="தற்போதைய அரசியலமைப்பு அமைப்பில் சொத்து உரிமை தொடர்பான பின்வரும் கூற்றுகளில் எது உண்மையிலேயே துல்லியமானது?",
        opts_en=[
            "It is a Fundamental Right guaranteed under Article 31 in Part III.",
            "It is a Constitutional / Legal Right under Article 300A in Part XII.",
            "It is a Directive Principle of State Policy under Article 39 in Part IV.",
            "It is a Fundamental Duty under Article 51A in Part IVA."
        ],
        opts_ta=[
            "இது பகுதி III இல் உறுப்பு 31 இன் கீழ் உத்தரவாதம் அளிக்கப்பட்ட ஒரு அடிப்படை உரிமையாகும்.",
            "இது பகுதி XII இல் உறுப்பு 300A இன் கீழ் உள்ள ஒரு அரசியலமைப்பு / சட்ட உரிமையாகும்.",
            "இது பகுதி IV இல் உறுப்பு 39 இன் கீழ் உள்ள ஒரு அரசு நெறிமுறை கோட்பாடாகும்.",
            "இது பகுதி IVA இல் உறுப்பு 51A இன் கீழ் உள்ள ஒரு அடிப்படை கடமையாகும்."
        ],
        correct_ans="B",
        exp_en="Historical Context: Right to Property was originally a Fundamental Right under Articles 19(1)(f) and 31.\nReason: The 44th Constitutional Amendment Act, 1978 deleted Right to Property from Part III and created Article 300A in Part XII, making it a Legal/Constitutional Right.\nConstitutional Impact: State can acquire private property for public purpose with statutory backing, but citizens cannot approach SC directly under Art 32 for property deprivation.\nExam Trap: Do not mistake it for a fundamental right; it is a legal right under Article 300A (Part XII).\nMemory Trick: 44th Amendment = 4+4=8 (1978) -> Property shifted to 300A.",
        exp_ta="வரலாற்றுப் பின்னணி: சொத்து உரிமை ஆரம்பத்தில் உறுப்புகள் 19(1)(f) மற்றும் 31 இன் கீழ் ஒரு அடிப்படை உரிமையாக இருந்தது.\nகாரணம்: 44வது அரசியலமைப்பு திருத்தச் சட்டம், 1978 பகுதி III லிருந்து சொத்து உரிமையை நீக்கி பகுதி XII இல் உறுப்பு 300A ஐ உருவாக்கியது, அதை சட்டப்பூர்வ/அரசியலமைப்பு உரிமையாக மாற்றியது.\nஅரசியலமைப்பு தாக்கம்: சட்டப்பூர்வ ஆதரவுடன் பொது நோக்கத்திற்காக அரசு தனிநபர் சொத்தை கையகப்படுத்தலாம், ஆனால் சொத்து இழப்பிற்கு குடிமக்கள் நேரடியாக உறுப்பு 32 இன் கீழ் உச்ச நீதிமன்றத்தை அணுக முடியாது.\nதேர்வுப் பொறி: இதை ஒரு அடிப்படை உரிமை என்று தவறாக நினைக்க வேண்டாம்; இது உறுப்பு 300A (பகுதி XII) இன் கீழ் ஒரு சட்ட உரிமையாகும்.\nநினைவுச் சூத்திரம்: 44வது திருத்தம் (1978) -> சொத்து 300A க்கு மாற்றப்பட்டது.",
        wno_dict={
            "A": {"en": "Incorrect. Article 31 was deleted from Part III by 44th Amendment 1978.", "ta": "தவறு. உறுப்பு 31 44வது திருத்தம் 1978 மூலம் பகுதி III லிருந்து நீக்கப்பட்டது."},
            "B": {"en": "Correct. Right to Property is a Legal/Constitutional Right under Article 300A in Part XII.", "ta": "சரி. சொத்து உரிமை என்பது பகுதி XII இல் உறுப்பு 300A இன் கீழ் ஒரு சட்ட/அரசியலமைப்பு உரிமையாகும்."},
            "C": {"en": "Incorrect. Article 39 deals with DPSP, not Right to Property directly.", "ta": "தவறு. உறுப்பு 39 DPSP பற்றியது, நேரடியாக சொத்து உரிமை பற்றியது அல்ல."},
            "D": {"en": "Incorrect. It is not a Fundamental Duty.", "ta": "தவறு. இது ஒரு அடிப்படை கடமை அல்ல."}
        },
        tip_en="TNPSC Trap: 44th Amendment (1978) shifted Right to Property to Art 300A (Part XII) as a Legal Right.",
        tip_ta="TNPSC பொறி: 44வது திருத்தம் (1978) சொத்து உரிமையை சட்ட உரிமையாக உறுப்பு 300A (பகுதி XII) க்கு மாற்றியது.",
        rev_en="Right to Property: Formerly FR (Art 31), now Legal Right (Art 300A, Part XII) via 44th Amendment 1978.",
        rev_ta="சொத்து உரிமை: முன்பு அடிப்படை உரிமை (உறுப்பு 31), இப்போது 44வது திருத்தம் 1978 மூலம் சட்ட உரிமை (உறுப்பு 300A, பகுதி XII).",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Analyze", est_sec=60, pyq_sim="High", tags=["Right to Property", "Article 300A", "44th Amendment", "TNPSC Trap"]
    ))

    # Q11 - Conceptual - Medium - Ans C
    qs.append(make_q(
        q_id="SF_GT_011", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="Conceptual",
        q_en="What does the principle of 'Collective Responsibility' in the Indian Parliamentary system signify?",
        q_ta="இந்திய நாடாளுமன்ற ஆட்சி முறையில் 'கூட்டுப் பொறுப்பு' (Collective Responsibility) கோட்பாடு எதனைக் குறிக்கிறது?",
        opts_en=[
            "The Executive is collectively responsible to the President of India.",
            "The Judiciary is collectively responsible to the Parliament.",
            "The Council of Ministers is collectively responsible to the Lok Sabha (House of the People).",
            "The State Cabinet is collectively responsible to the Rajya Sabha."
        ],
        opts_ta=[
            "நிர்வாகத் துறை இந்தியக் குடியரசுத் தலைவருக்கு கூட்டாகப் பொறுப்பேற்கிறது.",
            "நீதித்துறை நாடாளுமன்றத்திற்கு கூட்டாகப் பொறுப்பேற்கிறது.",
            "அமைச்சரவை மக்களவைக்கு (House of the People) கூட்டாகப் பொறுப்பேற்கிறது.",
            "மாநில அமைச்சரவை மாநிலங்களவைக்கு கூட்டாகப் பொறுப்பேற்கிறது."
        ],
        correct_ans="C",
        exp_en="Historical Context: Collective responsibility is the bedrock of parliamentary democracy under Article 75(3).\nReason: Under Article 75(3), the Council of Ministers is collectively responsible to the Lok Sabha. They sink or swim together. If a no-confidence motion is passed in Lok Sabha, all ministers must resign.\nConstitutional Impact: Enforces legislative control and democratic accountability over executive power.\nExam Trap: CoM is responsible to LOK SABHA, not to Parliament as a whole, nor to Rajya Sabha.\nMemory Trick: Sink or swim together in Lok Sabha.",
        exp_ta="வரலாற்றுப் பின்னணி: கூட்டுப் பொறுப்பு என்பது உறுப்பு 75(3) இன் கீழ் நாடாளுமன்ற ஜனநாயகத்தின் அடித்தளமாகும்.\nகாரணம்: உறுப்பு 75(3) இன் கீழ், அமைச்சரவை மக்களவைக்குக் கூட்டாகப் பொறுப்பேற்கிறது. அவர்கள் ஒன்றாக மூழ்குகிறார்கள் அல்லது நீந்துகிறார்கள். மக்களவையில் நம்பிக்கையில்லா தீர்மானம் நிறைவேற்றப்பட்டால், அனைத்து அமைச்சர்களும் ராஜினாமா செய்ய வேண்டும்.\nஅரசியலமைப்பு தாக்கம்: நிர்வாக அதிகாரத்தின் மீது சட்டமன்றக் கட்டுப்பாடு மற்றும் ஜனநாயகப் பொறுப்புணர்வை நடைமுறைப்படுத்துகிறது.\nதேர்வுப் பொறி: அமைச்சரவை மக்களவைக்கு பொறுப்பானது, ஒட்டுமொத்த நாடாளுமன்றத்திற்கும் அல்ல, மாநிலங்களவைக்கும் அல்ல.\nநினைவுச் சூத்திரம்: மக்களவையில் ஒன்றாக நீந்துதல் அல்லது மூழ்குதல்.",
        wno_dict={
            "A": {"en": "Incorrect. Ministers hold office during the pleasure of President, but are collectively responsible to Lok Sabha.", "ta": "தவறு. அமைச்சர்கள் குடியரசுத் தலைவரின் விருப்பம் வரை பதவியில் இருப்பார்கள், ஆனால் மக்களவைக்கே கூட்டாகப் பொறுப்பாவார்கள்."},
            "B": {"en": "Incorrect. Judiciary is independent and not collectively responsible to Parliament.", "ta": "தவறு. நீதித்துறை சுதந்திரமானது மற்றும் நாடாளுமன்றத்திற்கு கூட்டாகப் பொறுப்பல்ல."},
            "C": {"en": "Correct. Article 75(3) states Council of Ministers is collectively responsible to Lok Sabha.", "ta": "சரி. உறுப்பு 75(3) அமைச்சரவை மக்களவைக்குக் கூட்டாகப் பொறுப்பேற்கிறது என்று கூறுகிறது."},
            "D": {"en": "Incorrect. State cabinet is responsible to State Legislative Assembly (Vidhan Sabha).", "ta": "தவறு. மாநில அமைச்சரவை மாநில சட்டமன்றத்திற்கு (விதான சபா) பொறுப்பானது."}
        },
        tip_en="TNPSC Trap: Article 75(3): Council of Ministers is collectively responsible specifically to LOK SABHA (not Parliament/Rajya Sabha).",
        tip_ta="TNPSC பொறி: உறுப்பு 75(3): அமைச்சரவை குறிப்பாக மக்களவைக்கு (நாடாளுமன்றம்/மாநிலங்களவைக்கு அல்ல) கூட்டாகப் பொறுப்பேற்கிறது.",
        rev_en="Article 75(3): Collective Responsibility of Council of Ministers to Lok Sabha.",
        rev_ta="உறுப்பு 75(3): அமைச்சரவையின் கூட்டுப் பொறுப்பு மக்களவைக்கு மட்டுமே.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Understand", est_sec=45, pyq_sim="High", tags=["Parliamentary System", "Collective Responsibility", "Article 75"]
    ))

    # Q12 - Hard / Analytical - Hard - Ans D
    qs.append(make_q(
        q_id="SF_GT_012", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Hard", question_type="Hard / Analytical",
        q_en="Which of the following describes the key origin and nature of the Directive Principles of State Policy (DPSP)?\n1. They are enshrined in Part IV from Articles 36 to 51.\n2. They were borrowed from the Irish Constitution, which had copied them from Spain.\n3. Article 37 explicitly declares DPSPs to be non-justiciable in courts.",
        q_ta="அரசு நெறிமுறைப்படுத்தும் கோட்பாடுகளின் (DPSP) முக்கிய தோற்றம் மற்றும் தன்மையை பின்வருவனவற்றில் எது விவரிக்கிறது?\n1. அவை பகுதி IV இல் உறுப்புகள் 36 முதல் 51 வரை சேர்க்கப்பட்டுள்ளன.\n2. அவை அயர்லாந்து அரசியலமைப்பிலிருந்து பெறப்பட்டவை, அயர்லாந்து அவற்றை ஸ்பெயினிலிருந்து நகலெடுத்தது.\n3. உறுப்பு 37 DPSP-கள் நீதிமன்றங்களில் நிலைநிறுத்த முடியாதவை என வெளிப்படையாக அறிவிக்கிறது.",
        opts_en=[
            "1 and 2 only",
            "1 and 3 only",
            "2 and 3 only",
            "1, 2 and 3"
        ],
        opts_ta=[
            "1 மற்றும் 2 மட்டும்",
            "1 மற்றும் 3 மட்டும்",
            "2 மற்றும் 3 மட்டும்",
            "1, 2 மற்றும் 3"
        ],
        correct_ans="D",
        exp_en="Historical Context: DPSPs aim to establish social and economic democracy and a Welfare State.\nReason:\nStatement 1 is correct: Enshrined in Part IV, Articles 36-51.\nStatement 2 is correct: Borrowed from Irish Constitution (1937), which copied it from Spanish Constitution.\nStatement 3 is correct: Article 37 explicitly states DPSPs are non-justiciable, but fundamental in the governance of the country.\nConstitutional Impact: Guides the State in law-making for social welfare.\nExam Trap: Remember Ireland copied DPSP from Spain.",
        exp_ta="வரலாற்றுப் பின்னணி: DPSP-கள் சமூக மற்றும் பொருளாதார ஜனநாயகம் மற்றும் நலன்புரி அரசை (Welfare State) நிறுவுவதை நோக்கமாகக் கொண்டுள்ளன.\nகாரணம்:\nகூற்று 1 சரி: பகுதி IV, உறுப்புகள் 36-51 இல் சேர்க்கப்பட்டுள்ளது.\nகூற்று 2 சரி: அயர்லாந்து அரசியலமைப்பிலிருந்து பெறப்பட்டது (1937), அயர்லாந்து அதை ஸ்பானிய அரசியலமைப்பிலிருந்து நகலெடுத்தது.\nகூற்று 3 சரி: உறுப்பு 37 DPSP-கள் நீதிமன்றங்களால் நிலைநிறுத்த முடியாதவை, ஆனால் நாட்டின் ஆட்சியில் அடிப்படை கொள்கைகள் என்று வெளிப்படையாகக் கூறுகிறது.\nஅரசியலமைப்பு தாக்கம்: சமூக நலனுக்கான சட்டங்களை உருவாக்குவதில் அரசுக்கு வழிகாட்டுகிறது.\nதேர்வுப் பொறி: அயர்லாந்து DPSP-ஐ ஸ்பெயினில் இருந்து நகலெடுத்தது என்பதை நினைவில் கொள்க.",
        wno_dict={
            "A": {"en": "Incorrect. Statement 3 is also correct.", "ta": "தவறு. கூற்று 3-ம் சரியானது."},
            "B": {"en": "Incorrect. Statement 2 is also correct.", "ta": "தவறு. கூற்று 2-ம் சரியானது."},
            "C": {"en": "Incorrect. Statement 1 is also correct.", "ta": "தவறு. கூற்று 1-ம் சரியானது."},
            "D": {"en": "Correct. All three statements 1, 2, and 3 are correct.", "ta": "சரி. 1, 2 மற்றும் 3 ஆகிய மூன்று கூற்றுகளும் சரியானவை."}
        },
        tip_en="TNPSC Tip: Ireland borrowed DPSP from Spain; India borrowed DPSP from Ireland.",
        tip_ta="TNPSC குறிப்பு: அயர்லாந்து DPSP-ஐ ஸ்பெயினிலிருந்து பெற்றது; இந்தியா DPSP-ஐ அயர்லாந்திலிருந்து பெற்றது.",
        rev_en="Part IV DPSPs (Arts 36-51): From Ireland (originally Spain), non-justiciable (Art 37).",
        rev_ta="பகுதி IV DPSP (உறுப்புகள் 36-51): அயர்லாந்திலிருந்து (மூலம் ஸ்பெயின்), நீதிமன்றங்களால் நிலைநிறுத்த முடியாதவை (உறுப்பு 37).",
        sources=["M. Laxmikanth - Indian Polity", "NCERT Class XI"],
        bloom="Analyze", est_sec=75, pyq_sim="High", tags=["DPSP", "Part IV", "Non-justiciable", "Borrowed Features"]
    ))

    # Q13 - Direct MCQ - Easy - Ans A
    qs.append(make_q(
        q_id="SF_GT_013", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Easy", question_type="Direct MCQ",
        q_en="Under which Article of the Indian Constitution can a citizen move the Supreme Court directly for the enforcement of Fundamental Rights?",
        q_ta="இந்திய அரசியலமைப்பின் எந்த உறுப்பின் கீழ் ஒரு குடிமகன் அடிப்படை உரிமைகளை அமல்படுத்துவதற்காக நேரடியாக உச்ச நீதிமன்றத்தை அணுக முடியும்?",
        opts_en=[
            "Article 32",
            "Article 226",
            "Article 136",
            "Article 143"
        ],
        opts_ta=[
            "உறுப்பு 32",
            "உறுப்பு 226",
            "உறுப்பு 136",
            "உறுப்பு 143"
        ],
        correct_ans="A",
        exp_en="Historical Context: Dr. B.R. Ambedkar termed Article 32 as the 'Heart and Soul' of the Indian Constitution.\nReason: Article 32 guarantees the Right to Constitutional Remedies, empowering citizens to approach the Supreme Court for writs (Habeas Corpus, Mandamus, Prohibition, Quo-Warranto, Certiorari).\nConstitutional Impact: Makes Fundamental Rights justiciable and real rather than mere paper declarations.\nExam Trap: Article 32 is for SC; Article 226 is for HC. Article 32 itself is a Fundamental Right.\nMemory Trick: Art 32 = Supreme Court FR enforcement.",
        exp_ta="வரலாற்றுப் பின்னணி: டாக்டர் பி.ஆர். அம்பேத்கர் உறுப்பு 32 ஐ இந்திய அரசியலமைப்பின் 'இதயம் மற்றும் ஆன்மா' என்று குறிப்பிட்டார்.\nகாரணம்: உறுப்பு 32 அரசியலமைப்பு தீர்வுகளுக்கான உரிமைக்கு உத்தரவாதம் அளிக்கிறது, குடிமக்கள் பேராணைகளுக்காக (ஆட்கொணர் பேராணை, கட்டளையுறுத்தும் பேராணை, தடையுறுத்தும் பேராணை, தகுதி வினவு பேராணை, ஆவணக் கேட்பு பேராணை) உச்ச நீதிமன்றத்தை அணுக அதிகாரம் அளிக்கிறது.\nஅரசியலமைப்பு தாக்கம்: அடிப்படை உரிமைகளை வெறும் காகித அறிவிப்புகளாக இல்லாமல் நீதிமன்றத்தால் நிலைநிறுத்தக்கூடியதாக ஆக்குகிறது.\nதேர்வுப் பொறி: உறுப்பு 32 உச்ச நீதிமன்றத்திற்கு; உறுப்பு 226 உயர் நீதிமன்றத்திற்கு. உறுப்பு 32 자체가 ஒரு அடிப்படை உரிமையாகும்.\nநினைவுச் சூத்திரம்: உறுப்பு 32 = உச்ச நீதிமன்ற அடிப்படை உரிமை அமலாக்கம்.",
        wno_dict={
            "A": {"en": "Correct. Article 32 provides remedy from SC for FR violation.", "ta": "சரி. உறுப்பு 32 அடிப்படை உரிமை மீறலுக்கு உச்ச நீதிமன்றத்திலிருந்து தீர்வை வழங்குகிறது."},
            "B": {"en": "Incorrect. Article 226 provides writ remedies from High Courts.", "ta": "தவறு. உறுப்பு 226 உயர் நீதிமன்றங்களிலிருந்து பேராணை தீர்வுகளை வழங்குகிறது."},
            "C": {"en": "Incorrect. Article 136 deals with Special Leave Petition (SLP).", "ta": "தவறு. உறுப்பு 136 சிறப்பு விடுப்பு மனு (SLP) பற்றியது."},
            "D": {"en": "Incorrect. Article 143 deals with Advisory Jurisdiction of the President to SC.", "ta": "தவறு. உறுப்பு 143 உச்ச நீதிமன்றத்திற்கு குடியரசுத் தலைவரின் ஆலோசனைக் அதிகார வரம்பு பற்றியது."}
        },
        tip_en="TNPSC Tip: Art 32 = SC FR enforcement (itself a FR); Art 226 = HC Writ jurisdiction (broader than Art 32).",
        tip_ta="TNPSC குறிப்பு: உறுப்பு 32 = உச்ச நீதிமன்ற அடிப்படை உரிமை அமலாக்கம்; உறுப்பு 226 = உயர் நீதிமன்ற பேராணை அதிகாரம்.",
        rev_en="Article 32 = Right to Constitutional Remedies, Heart & Soul of Constitution (Ambedkar).",
        rev_ta="உறுப்பு 32 = அரசியலமைப்பு தீர்வுகளுக்கான உரிமை, அரசியலமைப்பின் இதயம் மற்றும் ஆன்மா (அம்பேத்கர்).",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Remember", est_sec=30, pyq_sim="High", tags=["Article 32", "Constitutional Remedies", "Fundamental Rights"]
    ))

    # Q14 - Conceptual - Hard - Ans B
    qs.append(make_q(
        q_id="SF_GT_014", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Hard", question_type="Conceptual",
        q_en="What does the concept of 'Integrated Judiciary' signify in the Indian Constitutional system?",
        q_ta="இந்திய அரசியலமைப்பு அமைப்பில் 'ஒருங்கிணைந்த நீதித்துறை' (Integrated Judiciary) என்ற கருத்து எதனைக் குறிக்கிறது?",
        opts_en=[
            "High Courts are completely independent state bodies with no judicial oversight from the Supreme Court.",
            "A single hierarchy of courts enforces both Central (Federal) and State laws throughout the country.",
            "Judicial officers are appointed directly by the Union Parliament without executive intervention.",
            "The judicial branch is merged with the executive branch to streamline legal administration."
        ],
        opts_ta=[
            "உயர் நீதிமன்றங்கள் உச்ச நீதிமன்றத்தின் நீதித்துறை மேற்பார்வை இல்லாத முற்றிலும் சுதந்திரமான மாநில அமைப்புகளாகும்.",
            "நாடு முழுவதும் மத்திய (கூட்டாட்சி) மற்றும் மாநில சட்டங்கள் இரண்டையும் ஒரே வரிசைமுறை நீதிமன்றங்கள் அமல்படுத்துகின்றன.",
            "நிர்வாகத் தலையீடு இன்றி நாடாளுமன்றத்தால் நீதிபதிகள் நேரடியாக நியமிக்கப்படுகிறார்கள்.",
            "சட்ட நிர்வாகத்தை சீரமைக்க நீதித்துறை நிர்வாகத் துறையுடன் இணைக்கப்பட்டுள்ளது."
        ],
        correct_ans="B",
        exp_en="Historical Context: Unlike the dual judicial system of the USA (where federal courts enforce federal laws and state courts enforce state laws), India adopted an integrated judiciary.\nReason: In India, a single tree of courts with Supreme Court at top, High Courts in middle, and Subordinate Courts below enforces both Central and State laws.\nConstitutional Impact: Maintains judicial uniformity and legal integration across the country.\nExam Trap: USA has Dual Judiciary; India has Single Integrated Judiciary despite being a federation.\nMemory Trick: US = Dual Judiciary, India = Single Integrated Judiciary.",
        exp_ta="வரலாற்றுப் பின்னணி: அமெரிக்காவின் இரட்டை நீதித்துறை அமைப்பைப் போலல்லாமல் (அங்கு கூட்டாட்சி நீதிமன்றங்கள் கூட்டாட்சி சட்டங்களையும் மாநில நீதிமன்றங்கள் மாநில சட்டங்களையும் அமல்படுத்துகின்றன), இந்தியா ஒரு ஒருங்கிணைந்த நீதித்துறையை ஏற்றுக்கொண்டது.\nகாரணம்: இந்தியாவில், உச்சத்தில் உச்ச நீதிமன்றம், நடுவில் உயர் நீதிமன்றங்கள் மற்றும் கீழே சார்பு நீதிமன்றங்களைக் கொண்ட ஒற்றைக் குடும்ப நீதிமன்றங்கள் மத்திய மற்றும் மாநில சட்டங்கள் இரண்டையும் அமல்படுத்துகின்றன.\nஅரசியலமைப்பு தாக்கம்: நாடு முழுவதும் நீதித்துறை சீரான தன்மையையும் சட்ட ஒருமைப்பாட்டையும் பேணுகிறது.\nதேர்வுப் பொறி: அமெரிக்கா இரட்டை நீதித்துறையைக் கொண்டுள்ளது; கூட்டாட்சியாக இருந்தபோதிலும் இந்தியா ஒற்றை ஒருங்கிணைந்த நீதித்துறையைக் கொண்டுள்ளது.\nநினைவுச் சூத்திரம்: அமெரிக்கா = இரட்டை நீதித்துறை, இந்தியா = ஒற்றை ஒருங்கிணைந்த நீதித்துறை.",
        wno_dict={
            "A": {"en": "Incorrect. SC has appellate and supervisory control over High Courts.", "ta": "தவறு. உயர் நீதிமன்றங்கள் மீது உச்ச நீதிமன்றத்திற்கு மேல்முறையீடு மற்றும் மேற்பார்வைக் கட்டுப்பாடு உள்ளது."},
            "B": {"en": "Correct. Single court system enforcing both central and state laws.", "ta": "சரி. மத்திய மற்றும் மாநில சட்டங்கள் இரண்டையும் அமல்படுத்தும் ஒற்றை நீதிமன்ற முறை."},
            "C": {"en": "Incorrect. Judges are appointed by President / collegium system, not Parliament.", "ta": "தவறு. நீதிபதிகள் நாடாளுமன்றத்தால் அல்ல, குடியரசுத் தலைவர் / கொலீஜியம் அமைப்பால் நியமிக்கப்படுகிறார்கள்."},
            "D": {"en": "Incorrect. Article 50 explicitly mandates Separation of Judiciary from Executive.", "ta": "தவறு. உறுப்பு 50 நிர்வாகத்திலிருந்து நீதித்துறையைப் பிரிப்பதை வெளிப்படையாக ஆணையிடுகிறது."}
        },
        tip_en="TNPSC Trap: Integrated Judiciary = Unitary Feature of Indian Constitution (Single system for Union & State laws).",
        tip_ta="TNPSC பொறி: ஒருங்கிணைந்த நீதித்துறை = இந்திய அரசியலமைப்பின் ஒற்றையாட்சி அம்சம் (மத்திய & மாநில சட்டங்களுக்கு ஒரே அமைப்பு).",
        rev_en="Integrated Judiciary: Supreme Court -> High Courts -> Subordinate Courts enforce both Union and State laws.",
        rev_ta="ஒருங்கிணைந்த நீதித்துறை: உச்ச நீதிமன்றம் -> உயர் நீதிமன்றங்கள் -> சார்பு நீதிமன்றங்கள் மத்திய மற்றும் மாநில சட்டங்களை அமல்படுத்துகின்றன.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Understand", est_sec=60, pyq_sim="High", tags=["Integrated Judiciary", "Unitary Feature", "Supreme Court"]
    ))

    # Q15 - Match the Following - Medium - Ans C
    qs.append(make_q(
        q_id="SF_GT_015", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="Match the Following",
        q_en="Match List-I (Constitutional Provisions) with List-II (Corresponding Articles) and select the correct answer:\n\nList-I:\n(a) Universal Adult Franchise\n(b) Protection of Fundamental Rights via SC Writs\n(c) Fundamental Duties\n(d) Establishment of Finance Commission\n\nList-II:\n1. Article 51A\n2. Article 280\n3. Article 326\n4. Article 32",
        q_ta="பட்டியல்-I (அரசியலமைப்பு விதிகளை) பட்டியல்-II (தொடர்புடைய உறுப்புகள்) உடன் பொருத்தி சரியான பதிலதைத் தேர்ந்தெடுக்கவும்:\n\nபட்டியல்-I:\n(a) உலகளாவிய வயதுவந்தோர் வாக்குரிமை\n(b) உச்ச நீதிமன்ற பேராணைகள் மூலம் அடிப்படை உரிமைகள் பாதுகாப்பு\n(c) அடிப்படை கடமைகள்\n(d) நிதி ஆணையத்தை அமைத்தல்\n\nபட்டியல்-II:\n1. உறுப்பு 51A\n2. உறுப்பு 280\n3. உறுப்பு 326\n4. உறுப்பு 32",
        opts_en=[
            "(a)-3, (b)-1, (c)-4, (d)-2",
            "(a)-4, (b)-3, (c)-1, (d)-2",
            "(a)-3, (b)-4, (c)-1, (d)-2",
            "(a)-2, (b)-4, (c)-1, (d)-3"
        ],
        opts_ta=[
            "(a)-3, (b)-1, (c)-4, (d)-2",
            "(a)-4, (b)-3, (c)-1, (d)-2",
            "(a)-3, (b)-4, (c)-1, (d)-2",
            "(a)-2, (b)-4, (c)-1, (d)-3"
        ],
        correct_ans="C",
        exp_en="Historical Context: Matching core articles with key constitutional features tests article mastery.\nReason:\n(a) Adult Franchise = Article 326 (3)\n(b) SC Writs for FRs = Article 32 (4)\n(c) Fundamental Duties = Article 51A (1)\n(d) Finance Commission = Article 280 (2)\nMatching: (a)-3, (b)-4, (c)-1, (d)-2.",
        exp_ta="வரலாற்றுப் பின்னணி: முக்கிய அரசியலமைப்பு அம்சங்களுடன் முக்கிய உறுப்புகளைப் பொருத்துவது தேர்வரின் உறுப்பு அறிவை சோதிக்கிறது.\nகாரணம்:\n(a) வயதுவந்தோர் வாக்குரிமை = உறுப்பு 326 (3)\n(b) அடிப்படை உரிமைகளுக்கான உச்ச நீதிமன்ற பேராணைகள் = உறுப்பு 32 (4)\n(c) அடிப்படை கடமைகள் = உறுப்பு 51A (1)\n(d) நிதி ஆணையம் = உறுப்பு 280 (2)\nபொருத்துதல்: (a)-3, (b)-4, (c)-1, (d)-2.",
        wno_dict={
            "A": {"en": "Incorrect. SC Writs is Art 32 (4), not Art 51A (1).", "ta": "தவறு. உச்ச நீதிமன்ற பேராணைகள் உறுப்பு 32 (4), உறுப்பு 51A (1) அல்ல."},
            "B": {"en": "Incorrect. Adult Franchise is Art 326 (3), not Art 32 (4).", "ta": "தவறு. வயதுவந்தோர் வாக்குரிமை உறுப்பு 326 (3), உறுப்பு 32 (4) அல்ல."},
            "C": {"en": "Correct. All four pairs matched accurately: (a)-3, (b)-4, (c)-1, (d)-2.", "ta": "சரி. நான்கு இணைகளும் துல்லியமாகப் பொருந்தின: (a)-3, (b)-4, (c)-1, (d)-2."},
            "D": {"en": "Incorrect. Adult Franchise is Art 326 (3), not Art 280 (2).", "ta": "தவறு. வயதுவந்தோர் வாக்குரிமை உறுப்பு 326 (3), உறுப்பு 280 (2) அல்ல."}
        },
        tip_en="TNPSC Tip: Art 326 (Adult Franchise), Art 32 (SC Writs), Art 51A (FDs), Art 280 (Finance Commission).",
        tip_ta="TNPSC குறிப்பு: உறுப்பு 326 (வாக்குரிமை), உறுப்பு 32 (பேராணைகள்), உறுப்பு 51A (அடிப்படை கடமைகள்), உறுப்பு 280 (நிதி ஆணையம்).",
        rev_en="Art 326 (Adult Franchise), Art 32 (SC Remedies), Art 51A (FDs), Art 280 (Finance Commission).",
        rev_ta="உறுப்பு 326 (வாக்குரிமை), உறுப்பு 32 (தீர்வு), உறுப்பு 51A (கடமைகள்), உறுப்பு 280 (நிதி ஆணையம்).",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Remember", est_sec=60, pyq_sim="High", tags=["Articles", "Match the Following", "Constitutional Bodies"]
    ))

    # Q16 - Assertion & Reason - Medium - Ans A
    qs.append(make_q(
        q_id="SF_GT_016", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="Assertion & Reason",
        q_en="Given below are two statements, one labeled as Assertion (A) and the other labeled as Reason (R):\n\nAssertion (A): The Indian Constitution establishes a Single Citizenship for the entire country despite having a federal structure.\nReason (R): Single Citizenship was adopted to promote national integration, brotherhood, and eliminate regional animosities among citizens.",
        q_ta="கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிக்கப்பட்டுள்ளது:\n\nகூற்று (A): கூட்டாட்சி அமைப்பைக் கொண்டிருந்தபோதிலும் இந்திய அரசியலமைப்பு முழு நாட்டிற்கும் ஒற்றைக் குடியுரிமையை நிறுவுகிறது.\nகாரணம் (R): தேசிய ஒருமைப்பாடு, சகோதரத்துவத்தை மேம்படுத்தவும் குடிமக்களிடையே பிராந்திய பகைமையை ஒழிக்கவும் ஒற்றைக் குடியுரிமை ஏற்றுக்கொள்ளப்பட்டது.",
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
        exp_en="Historical Context: Unlike USA which has dual citizenship (national + state), India chose single Indian citizenship.\nReason: Framers chose single citizenship to build a unified nation from diverse linguistic and regional groups, ensuring equal rights across state borders.\nConstitutional Impact: Fosters national brotherhood as emphasized in the Preamble.\nExam Trap: USA = Dual Citizenship; India = Single Citizenship.",
        exp_ta="வரலாற்றுப் பின்னணி: இரட்டை குடியுரிமையைக் கொண்ட அமெரிக்காவைப் போலல்லாமல் (தேசிய + மாநில), இந்தியா ஒற்றை இந்தியக் குடியுரிமையைத் தேர்ந்தெடுத்தது.\nகாரணம்: பல்வேறு மொழி மற்றும் பிராந்தியக் குழுக்களிலிருந்து ஒரு ஒருங்கிணைந்த தேசத்தை உருவாக்கவும், மாநில எல்லைகளைத் தாண்டி சம உரிமைகளை உறுதிப்படுத்தவும் உருவாக்கிகள் ஒற்றைக் குடியுரிமையைத் தேர்ந்தெடுத்தனர்.\nஅரசியலமைப்பு தாக்கம்: முகவுரையில் வலியுறுத்தப்பட்டுள்ளபடி தேசிய சகோதரத்துவத்தை வளர்க்கிறது.\nதேர்வுப் பொறி: அமெரிக்கா = இரட்டை குடியுரிமை; இந்தியா = ஒற்றைக் குடியுரிமை.",
        wno_dict={
            "A": {"en": "Correct. Both statements are true and (R) explains why single citizenship was preferred.", "ta": "சரி. இரு கூற்றுகளும் சரி, மற்றும் (R) ஏன் ஒற்றைக் குடியுரிமை விரும்பப்பட்டது என்பதை விளக்குகிறது."},
            "B": {"en": "Incorrect. (R) is the exact justification for (A).", "ta": "தவறு. (R) என்பது (A)-ற்கான துல்லியமான விளக்கமாகும்."},
            "C": {"en": "Incorrect. (R) is true.", "ta": "தவறு. (R) உண்மை."},
            "D": {"en": "Incorrect. (A) is true.", "ta": "தவறு. (A) உண்மை."}
        },
        tip_en="TNPSC Tip: Single citizenship is a Unitary feature designed to foster national integration.",
        tip_ta="TNPSC குறிப்பு: ஒற்றைக் குடியுரிமை என்பது தேசிய ஒருமைப்பாட்டை வளர்க்க வடிவமைக்கப்பட்ட ஒற்றையாட்சி அம்சமாகும்.",
        rev_en="Single Citizenship = Unitary feature promoting brotherhood & national integration.",
        rev_ta="ஒற்றைக் குடியுரிமை = சகோதரத்துவம் & தேசிய ஒருமைப்பாட்டை ஊக்குவிக்கும் ஒற்றையாட்சி அம்சம்.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Evaluate", est_sec=60, pyq_sim="High", tags=["Single Citizenship", "Unitary Feature", "Assertion Reason"]
    ))

    # Q17 - Hard / Analytical - Hard - Ans D
    qs.append(make_q(
        q_id="SF_GT_017", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Hard", question_type="Hard / Analytical",
        q_en="Which of the following constitutional provisions underscores the 'Secular' character of the Indian State?",
        q_ta="பின்வரும் அரசியலமைப்பு விதிகளில் எது இந்திய அரசின் 'மதச்சார்பற்ற' தன்மையை அடிக்கோடிட்டுக் காட்டுகிறது?",
        opts_en=[
            "Articles 25 to 28 guaranteeing Freedom of Religion",
            "Article 15 prohibiting discrimination on grounds of religion",
            "Article 27 barring taxation for promotion of any particular religion",
            "All of the above"
        ],
        opts_ta=[
            "சமய சுதந்திரத்தை உத்தரவாதம் செய்யும் உறுப்புகள் 25 முதல் 28 வரை",
            "மதத்தின் அடிப்படையில் பாகுபாடு காட்டுவதைத் தடுக்கும் உறுப்பு 15",
            "எந்தவொரு குறிப்பிட்ட மதத்தையும் ஊக்குவிப்பதற்காக வரி விதிப்பதைத் தடுக்கும் உறுப்பு 27",
            "மேற்கூறிய அனைத்தும்"
        ],
        correct_ans="D",
        exp_en="Historical Context: The word 'Secular' was added to the Preamble by the 42nd Amendment Act 1976, but secularism was already embedded in constitutional provisions.\nReason: Indian Secularism means equal respect for all religions (Sarva Dharma Sambhava). Articles 14, 15, 16, 25, 26, 27, 28, 29, 30, 44 collectively mandate secularism.\nConstitutional Impact: Supreme Court declared Secularism as a Basic Structure feature in the S.R. Bommai case (1994).\nExam Trap: Do not think secularism is contained ONLY in Articles 25-28 or Preamble.",
        exp_ta="வரலாற்றுப் பின்னணி: 'மதச்சார்பற்ற' என்ற சொல் 1976 இன் 42வது திருத்தச் சட்டத்தின் மூலம் முகவுரையில் சேர்க்கப்பட்டது, ஆனால் மதச்சார்பின்மை ஏற்கனவே அரசியலமைப்பு விதிகளில் பதிந்திருந்தது.\nகாரணம்: இந்திய மதச்சார்பின்மை என்பது அனைத்து மதங்களுக்கும் சமமான மரியாதையைக் குறிக்கிறது (சர்வ தர்ம சம்பவ). உறுப்புகள் 14, 15, 16, 25, 26, 27, 28, 29, 30, 44 ஆகியவை கூட்டாக மதச்சார்பின்மையை ஆணையிடுகின்றன.\nஅரசியலமைப்பு தாக்கம்: உச்ச நீதிமன்றம் எஸ்.ஆர். பொம்மை வழக்கில் (1994) மதச்சார்பின்மையை அடிப்படை அமைப்பின் அம்சமாக அறிவித்தது.\nதேர்வுப் பொறி: மதச்சார்பின்மை உறுப்புகள் 25-28 அல்லது முகவுரையில் மட்டுமே உள்ளது என்று நினைக்க வேண்டாம்.",
        wno_dict={
            "A": {"en": "Incorrect. Option A is true, but Options B and C are also true.", "ta": "தவறு. விருப்பம் A சரி, ஆனால் விருப்பங்கள் B மற்றும் C-ம் சரியானவை."},
            "B": {"en": "Incorrect. Option B is true, but A and C are also true.", "ta": "தவறு. விருப்பம் B சரி, ஆனால் A மற்றும் C-ம் சரியானவை."},
            "C": {"en": "Incorrect. Option C is true, but A and B are also true.", "ta": "தவறு. விருப்பம் C சரி, ஆனால் A மற்றும் B-ம் சரியானவை."},
            "D": {"en": "Correct. All listed provisions (Articles 15, 25-28, 27) reflect the secular character of India.", "ta": "சரி. பட்டியலிடப்பட்ட அனைத்து விதிகளும் (உறுப்புகள் 15, 25-28, 27) இந்தியாவின் மதச்சார்பற்ற தன்மையைப் பிரதிபலிக்கின்றன."}
        },
        tip_en="TNPSC Tip: Secularism in India = Positive Secularism (equal treatment of all religions), declared Basic Structure in S.R. Bommai Case 1994.",
        tip_ta="TNPSC குறிப்பு: இந்தியாவில் மதச்சார்பின்மை = நேர்மறை மதச்சார்பின்மை (அனைத்து மதங்களுக்கும் சமமான சிகிச்சை), எஸ்.ஆர்.பொம்மை வழக்கு 1994 இல் அடிப்படை கட்டமைப்பாக அறிவிக்கப்பட்டது.",
        rev_en="Indian Secularism = Positive Concept (Sarva Dharma Sambhava); Basic Structure (S.R. Bommai 1994).",
        rev_ta="இந்திய மதச்சார்பின்மை = நேர்மறை கருத்து (சர்வ தர்ம சம்பவ); அடிப்படை அமைப்பு (எஸ்.ஆர்.பொம்மை 1994).",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Analyze", est_sec=60, pyq_sim="High", tags=["Secularism", "Basic Structure", "S.R. Bommai Case"]
    ))

    # Q18 - Direct MCQ - Easy - Ans A
    qs.append(make_q(
        q_id="SF_GT_018", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Easy", question_type="Direct MCQ",
        q_en="By which Constitutional Amendment Act were Fundamental Duties incorporated into Part IVA of the Indian Constitution?",
        q_ta="எந்த அரசியலமைப்பு திருத்தச் சட்டத்தின் மூலம் இந்திய அரசியலமைப்பின் பகுதி IVA இல் அடிப்படை கடமைகள் சேர்க்கப்பட்டன?",
        opts_en=[
            "42nd Constitutional Amendment Act, 1976",
            "44th Constitutional Amendment Act, 1978",
            "86th Constitutional Amendment Act, 2002",
            "91st Constitutional Amendment Act, 2003"
        ],
        opts_ta=[
            "42வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
            "44வது அரசியலமைப்பு திருத்தச் சட்டம், 1978",
            "86வது அரசியலமைப்பு திருத்தச் சட்டம், 2002",
            "91வது அரசியலமைப்பு திருத்தச் சட்டம், 2003"
        ],
        correct_ans="A",
        exp_en="Historical Context: Recommended by the Swaran Singh Committee during internal emergency.\nReason: The 42nd Amendment Act 1976 introduced Part IVA and Article 51A containing 10 Fundamental Duties.\nConstitutional Impact: Reminds citizens of their civic responsibilities alongside their fundamental rights.\nExam Trap: Original Constitution contained NO Fundamental Duties. 42nd Amendment added 10; 86th Amendment added the 11th duty.\nMemory Trick: 42nd Amendment 1976 = 10 Duties added.",
        exp_ta="வரலாற்றுப் பின்னணி: உள்நாட்டு அவசரநிலையின் போது ஸ்வரன் சிங் குழுவால் பரிந்துரைக்கப்பட்டது.\nகாரணம்: 42வது திருத்தச் சட்டம் 1976, பகுதி IVA மற்றும் உறுப்பு 51A ஐ அறிமுகப்படுத்தி 10 அடிப்படை கடமைகளைக் கொண்டிருந்தது.\nஅரசியலமைப்பு தாக்கம்: குடிமக்களுக்கு அவர்களின் அடிப்படை உரிமைகளுடன் அவர்களின் குடிமைப் பொறுப்புகளையும் நினைவூட்டுகிறது.\nதேர்வுப் பொறி: அசல் அரசியலமைப்பில் அடிப்படை கடமைகள் இல்லை. 42வது திருத்தம் 10 ஐச் சேர்த்தது; 86வது திருத்தம் 11வது கடமையைச் சேர்த்தது.\nநினைவுச் சூத்திரம்: 42வது திருத்தம் 1976 = 10 கடமைகள் சேர்க்கப்பட்டன.",
        wno_dict={
            "A": {"en": "Correct. 42nd Amendment 1976 introduced Part IVA (Article 51A) with 10 Fundamental Duties.", "ta": "சரி. 42வது திருத்தம் 1976 பகுதி IVA (உறுப்பு 51A) 10 அடிப்படை கடமைகளுடன் அறிமுகப்படுத்தியது."},
            "B": {"en": "Incorrect. 44th Amendment 1978 modified emergency rules and right to property.", "ta": "தவறு. 44வது திருத்தம் 1978 அவசரக்கால விதிகள் மற்றும் சொத்து உரிமையை மாற்றியமைத்தது."},
            "C": {"en": "Incorrect. 86th Amendment 2002 added the 11th duty (education for children 6-14 yrs).", "ta": "தவறு. 86வது திருத்தம் 2002 11வது கடமையைச் சேர்த்தது (6-14 வயது குழந்தைகளுக்கு கல்வி)."},
            "D": {"en": "Incorrect. 91st Amendment 2003 capped the size of Council of Ministers to 15%.", "ta": "தவறு. 91வது திருத்தம் 2003 அமைச்சரவையின் அளவை 15% ஆகக் குறைத்தது."}
        },
        tip_en="TNPSC Tip: Swaran Singh Committee (1976) recommended FDs. 42nd Amendment added 10 duties; 86th Amendment (2002) added 11th duty.",
        tip_ta="TNPSC குறிப்பு: ஸ்வரன் சிங் குழு (1976) FDகளைப் பரிந்துரைத்தது. 42வது திருத்தம் 10 கடமைகளைச் சேர்த்தது; 86வது திருத்தம் (2002) 11வது கடமையைச் சேர்த்தது.",
        rev_en="Part IVA (Art 51A) added by 42nd Amendment 1976 on Swaran Singh Committee recommendation.",
        rev_ta="ஸ்வரன் சிங் குழு பரிந்துரையின் பேரில் 42வது திருத்தம் 1976 மூலம் பகுதி IVA (உறுப்பு 51A) சேர்க்கப்பட்டது.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Remember", est_sec=30, pyq_sim="High", tags=["Fundamental Duties", "42nd Amendment", "Swaran Singh Committee"]
    ))

    # Q19 - Conceptual - Medium - Ans B
    qs.append(make_q(
        q_id="SF_GT_019", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="Conceptual",
        q_en="Which feature distinguishes a 'Republic' from a 'Constitutional Monarchy'?",
        q_ta="ஒரு 'குடியரசு' (Republic) என்பதை 'அரசியலமைப்பு முடியாட்சி' (Constitutional Monarchy) என்பதிலிருந்து வேறுபடுத்தும் அம்சம் எது?",
        opts_en=[
            "Presence of a written Constitution.",
            "Elected Head of State for a fixed tenure instead of a hereditary monarch.",
            "Existence of an independent Supreme Court.",
            "Bicameral system of Parliament."
        ],
        opts_ta=[
            "எழுதப்பட்ட அரசியலமைப்பின் இருப்பு.",
            "பரம்பரை மன்னருக்குப் பதிலாக நிலையான காலவரையறைக்கு தேர்ந்தெடுக்கப்பட்ட நாட்டின் தலைவர்.",
            "சுதந்திரமான உச்ச நீதிமன்றத்தின் இருப்பு.",
            "ஈரவை நாடாளுமன்ற முறை."
        ],
        correct_ans="B",
        exp_en="Historical Context: India chose to be a Democratic Republic on January 26, 1950.\nReason: A Republic has an elected head of state (President of India, elected for 5 years). In contrast, a Constitutional Monarchy (like UK) has a hereditary head of state (King/Queen).\nConstitutional Impact: Vests political sovereignty in the people; no privileged hereditary office exists.\nExam Trap: Having a Prime Minister or Parliament does NOT make a nation a republic; an ELECTED head of state does.\nMemory Trick: Republic = Public elects the Head.",
        exp_ta="வரலாற்றுப் பின்னணி: இந்தியா ஜனவரி 26, 1950 அன்று ஜனநாயகக் குடியரசாகத் தேர்ந்தெடுக்கப்பட்டது.\nகாரணம்: ஒரு குடியரசு தேர்ந்தெடுக்கப்பட்ட நாட்டின் தலைவரைக் கொண்டுள்ளது (இந்தியக் குடியரசுத் தலைவர், 5 ஆண்டுகளுக்குத் தேர்ந்தெடுக்கப்படுகிறார்). மாறாக, ஒரு அரசியலமைப்பு முடியாட்சி (இங்கிலாந்து போன்றவை) பரம்பரை நாட்டின் தலைவரைக் கொண்டுள்ளது (மன்னர்/ராணி).\nஅரசியலமைப்பு தாக்கம்: அரசியல் இறையாண்மையை மக்களுக்கு வழங்குகிறது; சலுகை பெற்ற பரம்பரை பதவி எதுவும் இல்லை.\nதேர்வுப் பொறி: ஒரு பிரதமர் அல்லது நாடாளுமன்றத்தைக் கொண்டிருப்பது ஒரு தேசத்தைக் குடியரசாக மாற்றாது; தேர்ந்தெடுக்கப்பட்ட நாட்டின் தலைவர் மட்டுமே மாற்றும்.\nநினைவுச் சூத்திரம்: குடியரசு = பொதுமக்கள் தலைவரைத் தேர்ந்தெடுக்கிறார்கள்.",
        wno_dict={
            "A": {"en": "Incorrect. Both republics and constitutional monarchies can have written constitutions.", "ta": "தவறு. குடியரசுகள் மற்றும் அரசியலமைப்பு முடியாட்சிகள் இரண்டிலும் எழுதப்பட்ட அரசியலமைப்புகள் இருக்கலாம்."},
            "B": {"en": "Correct. An elected head of state (Republic) vs hereditary head (Monarchy).", "ta": "சரி. தேர்ந்தெடுக்கப்பட்ட நாட்டின் தலைவர் (குடியரசு) vs வம்சாவளி தலைவர் (முடியாட்சி)."},
            "C": {"en": "Incorrect. Independent courts exist in constitutional monarchies too (e.g., UK).", "ta": "தவறு. அரசியலமைப்பு முடியாட்சிகளிலும் சுதந்திரமான நீதிமன்றங்கள் உள்ளன (எ.கா., இங்கிலாந்து)."},
            "D": {"en": "Incorrect. Bicameral parliament exists in both systems.", "ta": "தவறு. ஈரவை நாடாளுமன்றம் இரு அமைப்புகளிலும் உள்ளது."}
        },
        tip_en="TNPSC Tip: Republic = Elected Head of State (President) + Political Sovereignty in People + Public offices open to all.",
        tip_ta="TNPSC குறிப்பு: குடியரசு = தேர்ந்தெடுக்கப்பட்ட நாட்டின் தலைவர் (குடியரசுத் தலைவர்) + மக்களிடம் அரசியல் இறையாண்மை + பொதுப் பதவிகள் அனைவருக்கும் திறந்திருக்கும்.",
        rev_en="Republic: Head of State is elected for a fixed term (India) vs Hereditary monarch (UK).",
        rev_ta="குடியரசு: நாட்டின் தலைவர் ஒரு குறிப்பிட்ட காலத்திற்கு தேர்ந்தெடுக்கப்படுகிறார் (இந்தியா) vs வம்சாவளி மன்னர் (இங்கிலாந்து).",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Understand", est_sec=45, pyq_sim="High", tags=["Republic", "Democracy", "Head of State"]
    ))

    # Q20 - Statement-Based - Medium - Ans C
    qs.append(make_q(
        q_id="SF_GT_020", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="Statement-Based",
        q_en="Consider the following statements regarding the Emergency Provisions in the Indian Constitution:\n1. Article 352 deals with National Emergency declared on grounds of war, external aggression, or armed rebellion.\n2. Article 356 deals with President's Rule imposed due to failure of constitutional machinery in states.\n3. Article 360 deals with Financial Emergency, which has been invoked twice in India so far.\n\nWhich of the statements given above is/are CORRECT?",
        q_ta="இந்திய அரசியலமைப்பில் உள்ள அவசரக்கால விதிகள் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. உறுப்பு 352 போர், வெளியார் ஆக்கிரமிப்பு அல்லது ஆயுதமேந்திய கிளர்ச்சி ஆகிய காரணங்களின் அடிப்படையில் அறிவிக்கப்படும் தேசிய அவசரநிலையைக் கையாள்கிறது.\n2. உறுப்பு 356 மாநிலங்களில் அரசியலமைப்பு இயந்திரத்தின் தோல்வி காரணமாக விதிக்கப்படும் குடியரசுத் தலைவர் ஆட்சியைக் கையாள்கிறது.\n3. உறுப்பு 360 நிதி அவசரநிலையைக் கையாள்கிறது, இது இந்தியாவில் இதுவரை இரண்டு முறை பயன்படுத்தப்பட்டுள்ளது.\n\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானவை?",
        opts_en=[
            "1 and 3 only",
            "2 and 3 only",
            "1 and 2 only",
            "1, 2 and 3"
        ],
        opts_ta=[
            "1 மற்றும் 3 மட்டும்",
            "2 மற்றும் 3 மட்டும்",
            "1 மற்றும் 2 மட்டும்",
            "1, 2 மற்றும் 3"
        ],
        correct_ans="C",
        exp_en="Historical Context: Part XVIII of Constitution contains Emergency Provisions (Articles 352-360).\nReason:\nStatement 1 is correct: Article 352 covers National Emergency (war, external aggression, armed rebellion).\nStatement 2 is correct: Article 356 covers President's Rule in States.\nStatement 3 is INCORRECT: Article 360 covers Financial Emergency, but it has NEVER been invoked in India so far.\nExam Trap: Financial Emergency (Art 360) has NEVER been declared in India (not even during 1991 crisis).",
        exp_ta="வரலாற்றுப் பின்னணி: அரசியலமைப்பின் பகுதி XVIII அவசரக்கால விதிகளைக் கொண்டுள்ளது (உறுப்புகள் 352-360).\nகாரணம்:\nகூற்று 1 சரி: உறுப்பு 352 தேசிய அவசரநிலையை உள்ளடக்கியது (போர், வெளியார் ஆக்கிரமிப்பு, ஆயுதமேந்திய கிளர்ச்சி).\nகூற்று 2 சரி: உறுப்பு 356 மாநிலங்களில் குடியரசுத் தலைவர் ஆட்சியை உள்ளடக்கியது.\nகூற்று 3 தவறு: உறுப்பு 360 நிதி அவசரநிலையை உள்ளடக்கியது, ஆனால் இது இந்தியாவில் இதுவரை ஒருமுறை கூட பயன்படுத்தப்படவில்லை.\nதேர்வுப் பொறி: நிதி அவசரநிலை (உறுப்பு 360) இந்தியாவில் இதுவரை ஒருபோதும் அறிவிக்கப்படவில்லை (1991 நிதி நெருக்கடியின் போது கூட இல்லை).",
        wno_dict={
            "A": {"en": "Incorrect. Statement 3 is wrong (Financial Emergency has never been declared).", "ta": "தவறு. கூற்று 3 தவறு (நிதி அவசரநிலை இதுவரை அறிவிக்கப்படவில்லை)."},
            "B": {"en": "Incorrect. Statement 3 is wrong.", "ta": "தவறு. கூற்று 3 தவறு."},
            "C": {"en": "Correct. Statements 1 and 2 are correct; statement 3 is false.", "ta": "சரி. கூற்றுகள் 1 மற்றும் 2 சரி; கூற்று 3 தவறு."},
            "D": {"en": "Incorrect. Statement 3 is false.", "ta": "தவறு. கூற்று 3 தவறு."}
        },
        tip_en="TNPSC Trap: Financial Emergency under Article 360 has NEVER been declared in India.",
        tip_ta="TNPSC பொறி: உறுப்பு 360 இன் கீழ் நிதி அவசரநிலை இந்தியாவில் இதுவரை ஒருபோதும் அறிவிக்கப்பட்டதில்லை.",
        rev_en="Emergency Articles: 352 (National), 356 (State/President's Rule), 360 (Financial - Never used).",
        rev_ta="அவசரக்கால உறுப்புகள்: 352 (தேசியம்), 356 (மாநிலம்/குடியரசுத் தலைவர் ஆட்சி), 360 (நிதி - பயன்படுத்தப்படவில்லை).",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Analyze", est_sec=60, pyq_sim="High", tags=["Emergency Provisions", "Article 360", "Financial Emergency"]
    ))

    # Q21 - PYQ Pattern - Easy - Ans D
    qs.append(make_q(
        q_id="SF_GT_021", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Easy", question_type="PYQ Pattern",
        q_en="The 73rd and 74th Constitutional Amendment Acts of 1992 added which tier of government to the Indian Constitution?",
        q_ta="1992 இன் 73வது மற்றும் 74வது அரசியலமைப்பு திருத்தச் சட்டங்கள் இந்திய அரசியலமைப்பில் அரசாங்கத்தின் எந்த அடுக்கைச் சேர்த்தன?",
        opts_en=[
            "Central Tier",
            "State Tier",
            "Regional Council Tier",
            "Third Tier (Local Self-Government)"
        ],
        opts_ta=[
            "மத்திய அடுக்கு",
            "மாநில அடுக்கு",
            "பிராந்திய கவுன்சில் அடுக்கு",
            "மூன்றாவது அடுக்கு (உள்ளாட்சி சுயராஜ்யம்)"
        ],
        correct_ans="D",
        exp_en="Historical Context: Originally, the Constitution provided a two-tier federal framework (Centre and States).\nReason: 73rd Amendment (Panchayats - Part IX) and 74th Amendment (Municipalities - Part IXA) added a 3rd tier of Local Self-Government in 1992.\nConstitutional Impact: Institutionalized democratic decentralization at grassroot level.\nExam Trap: Original Constitution had 2 tiers; 1992 amendments made it a 3-tier system.\nMemory Trick: 73 + 74 = 3rd Tier (Panchayats & Municipalities).",
        exp_ta="வரலாற்றுப் பின்னணி: ஆரம்பத்தில், அரசியலமைப்பு இரண்டு அடுக்கு கூட்டாட்சி அமைப்பை (மத்திய மற்றும் மாநிலங்கள்) வழங்கியது.\nகாரணம்: 73வது திருத்தம் (பஞ்சாயத்துகள் - பகுதி IX) மற்றும் 74வது திருத்தம் (நகராட்சிகள் - பகுதி IXA) 1992 இல் உள்ளாட்சி சுயராஜ்யத்தின் 3வது அடுக்கைச் சேர்த்தன.\nஅரசியலமைப்பு தாக்கம்: அடித்தள மட்டத்தில் ஜனநாயக பரவலாக்கத்தை நிறுவனமயமாக்கியது.\nதேர்வுப் பொறி: அசல் அரசியலமைப்பில் 2 அடுக்குகள் இருந்தன; 1992 திருத்தங்கள் அதை 3 அடுக்கு அமைப்பாக மாற்றின.\nநினைவுச் சூத்திரம்: 73 + 74 = 3வது அடுக்கு (பஞ்சாயத்துகள் & நகராட்சிகள்).",
        wno_dict={
            "A": {"en": "Incorrect. Central tier existed since 1950.", "ta": "தவறு. மத்திய அடுக்கு 1950 முதல் இருந்தது."},
            "B": {"en": "Incorrect. State tier existed since 1950.", "ta": "தவறு. மாநில அடுக்கு 1950 முதல் இருந்தது."},
            "C": {"en": "Incorrect. Zonal councils are statutory, not constitutional tiers.", "ta": "தவறு. மண்டல கவுன்சில்கள் சட்டப்பூர்வமானவை, அரசியலமைப்பு அடுக்குகள் அல்ல."},
            "D": {"en": "Correct. Added Third Tier of government (Panchayats and Municipalities).", "ta": "சரி. அரசாங்கத்தின் மூன்றாவது அடுக்கைச் சேர்த்தது (பஞ்சாயத்துகள் மற்றும் நகராட்சிகள்)."}
        },
        tip_en="TNPSC Tip: India has a unique 3-tier government system (Union, State, Local bodies) not found in other major federations.",
        tip_ta="TNPSC குறிப்பு: மற்ற முக்கிய கூட்டாட்சிகளில் காணப்படாத தனித்துவமான 3-அடுக்கு அரசு அமைப்பை (மத்திய, மாநில, உள்ளாட்சிகள்) இந்தியா கொண்டுள்ளது.",
        rev_en="73rd & 74th Amendments (1992): Added Part IX (Panchayats) & Part IXA (Municipalities) creating 3-tier government.",
        rev_ta="73வது & 74வது திருத்தங்கள் (1992): பகுதி IX (பஞ்சாயத்துகள்) & பகுதி IXA (நகராட்சிகள்) சேர்த்து 3-அடுக்கு அரசை உருவாக்கியது.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Remember", est_sec=30, pyq_sim="Direct PYQ", tags=["Three-Tier Government", "73rd Amendment", "74th Amendment"]
    ))

    # Q22 - TNPSC Trap - Medium - Ans A
    qs.append(make_q(
        q_id="SF_GT_022", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="TNPSC Trap",
        q_en="Which of the following is NOT an independent Constitutional Body under the Indian Constitution?",
        q_ta="பின்வருவனவற்றில் எது இந்திய அரசியலமைப்பின் கீழ் ஒரு சுதந்திரமான அரசியலமைப்பு அமைப்பு (Constitutional Body) அல்ல?",
        opts_en=[
            "NITI Aayog",
            "Election Commission of India",
            "Comptroller and Auditor General of India",
            "Union Public Service Commission"
        ],
        opts_ta=[
            "நிதி ஆயோக் (NITI Aayog)",
            "இந்தியத் தேர்தல் ஆணையம்",
            "இந்திய தலைமை தணிக்கை அதிகாரி (CAG)",
            "மத்திய அரசுப் பணியாளர் தேர்வாணையம் (UPSC)"
        ],
        correct_ans="A",
        exp_en="Historical Context: Constitutional bodies derive their powers directly from specific articles in the Constitution.\nReason: NITI Aayog is a non-constitutional, extra-constitutional, non-statutory executive body created by a Cabinet resolution in 2015 (replacing Planning Commission). EC (Art 324), CAG (Art 148), UPSC (Art 315) are Constitutional Bodies.\nConstitutional Impact: NITI Aayog serves as an advisory policy think-tank.\nExam Trap: NITI Aayog is NEITHER constitutional NOR statutory.",
        exp_ta="வரலாற்றுப் பின்னணி: அரசியலமைப்பு அமைப்புகள் தங்களின் அதிகாரங்களை அரசியலமைப்பின் குறிப்பிட்ட உறுப்புகளிலிருந்து நேரடியாகப் பெறுகின்றன.\nகாரணம்: நிதி ஆயோக் என்பது 2015 இல் அமைச்சரவைத் தீர்மானத்தின் மூலம் உருவாக்கப்பட்ட ஒரு அரசியலமைப்பற்ற, சட்டப்பூர்வமற்ற நிர்வாக அமைப்பாகும் (திட்டக் குழுவிற்குப் பதிலாக). தேர்தல் ஆணையம் (உறுப்பு 324), CAG (உறுப்பு 148), UPSC (உறுப்பு 315) ஆகியவை அரசியலமைப்பு அமைப்புகளாகும்.\nஅரசியலமைப்பு தாக்கம்: நிதி ஆயோக் ஒரு ஆலோசனைக் கொள்கை சிந்தனைக் குழுவாகச் செயல்படுகிறது.\nதேர்வுப் பொறி: நிதி ஆயோக் அரசியலமைப்பு அமைப்பும் அல்ல, சட்டப்பூர்வ அமைப்பும் அல்ல.",
        wno_dict={
            "A": {"en": "Correct. NITI Aayog is an executive body created by cabinet resolution, NOT a constitutional body.", "ta": "சரி. நிதி ஆயோக் என்பது அமைச்சரவைத் தீர்மானத்தால் உருவாக்கப்பட்ட ஒரு நிர்வாக அமைப்பாகும், அரசியலமைப்பு அமைப்பு அல்ல."},
            "B": {"en": "Incorrect. Election Commission is a Constitutional Body under Article 324.", "ta": "தவறு. தேர்தல் ஆணையம் உறுப்பு 324 இன் கீழ் ஒரு அரசியலமைப்பு அமைப்பாகும்."},
            "C": {"en": "Incorrect. CAG is a Constitutional Body under Article 148.", "ta": "தவறு. CAG உறுப்பு 148 இன் கீழ் ஒரு அரசியலமைப்பு அமைப்பாகும்."},
            "D": {"en": "Incorrect. UPSC is a Constitutional Body under Article 315.", "ta": "தவறு. UPSC உறுப்பு 315 இன் கீழ் ஒரு அரசியலமைப்பு அமைப்பாகும்."}
        },
        tip_en="TNPSC Trap: NITI Aayog, NHRC, CIC, Central Vigilance Commission are NOT Constitutional Bodies; EC, UPSC, CAG, FC ARE Constitutional Bodies.",
        tip_ta="TNPSC பொறி: நிதி ஆயோக், NHRC, CIC, CVC ஆகியவை அரசியலமைப்பு அமைப்புகள் அல்ல; தேர்தல் ஆணையம், UPSC, CAG, நிதி ஆணையம் ஆகியவை அரசியலமைப்பு அமைப்புகளாகும்.",
        rev_en="NITI Aayog = Executive Body (Cabinet resolution 2015); EC (324), CAG (148), UPSC (315) = Constitutional Bodies.",
        rev_ta="நிதி ஆயோக் = நிர்வாக அமைப்பு (2015); தேர்தல் ஆணையம் (324), CAG (148), UPSC (315) = அரசியலமைப்பு அமைப்புகள்.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Understand", est_sec=45, pyq_sim="High", tags=["Constitutional Bodies", "NITI Aayog", "TNPSC Trap"]
    ))

    # Q23 - Chronology - Medium - Ans B
    qs.append(make_q(
        q_id="SF_GT_023", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="Chronology",
        q_en="Arrange the following landmark judgments related to the Basic Structure Doctrine in chronological order:\n1. Golaknath Case\n2. Kesavananda Bharati Case\n3. Indira Nehru Gandhi Case\n4. Minerva Mills Case",
        q_ta="அடிப்படை கட்டமைப்பு கோட்பாடு தொடர்பான பின்வரும் வரலாற்றுச் சிறப்புமிக்க தீர்ப்புகளை காலவரிசைப்படி வரிசைப்படுத்தவும்:\n1. கோலக்நாத் வழக்கு\n2. கேசவாநந்த பாரதி வழக்கு\n3. இந்திரா நேரு காந்தி வழக்கு\n4. மினர்வா மில்ஸ் வழக்கு",
        opts_en=[
            "2 - 1 - 3 - 4",
            "1 - 2 - 3 - 4",
            "1 - 3 - 2 - 4",
            "2 - 3 - 1 - 4"
        ],
        opts_ta=[
            "2 - 1 - 3 - 4",
            "1 - 2 - 3 - 4",
            "1 - 3 - 2 - 4",
            "2 - 3 - 1 - 4"
        ],
        correct_ans="B",
        exp_en="Historical Context: Evolution of judicial stance on Basic Structure Doctrine.\nReason:\n1. Golaknath Case: 1967.\n2. Kesavananda Bharati Case: April 1973 (Basic Structure introduced).\n3. Indira Nehru Gandhi Case: 1975 (Election case, applied Basic Structure to invalidate 39th Amendment).\n4. Minerva Mills Case: 1980 (Reaffirmed Basic Structure).\nSequence: 1 (1967) -> 2 (1973) -> 3 (1975) -> 4 (1980).",
        exp_ta="வரலாற்றுப் பின்னணி: அடிப்படை கட்டமைப்பு கோட்பாட்டின் மீதான நீதித்துறை நிலப்பாட்டின் வளர்ச்சி.\nகாரணம்:\n1. கோலக்நாத் வழக்கு: 1967.\n2. கேசவாநந்த பாரதி வழக்கு: ஏப்ரல் 1973 (அடிப்படை கட்டமைப்பு அறிமுகப்படுத்தப்பட்டது).\n3. இந்திரா நேரு காந்தி வழக்கு: 1975 (தேர்தல் வழக்கு, 39வது திருத்தத்தை செல்லாததாக்க அடிப்படை அமைப்பைப் பயன்படுத்தியது).\n4. மினர்வா மில்ஸ் வழக்கு: 1980 (அடிப்படை அமைப்பை மீண்டும் உறுதிப்படுத்தியது).\nவரிசை: 1 (1967) -> 2 (1973) -> 3 (1975) -> 4 (1980).",
        wno_dict={
            "A": {"en": "Incorrect. Golaknath (1967) came BEFORE Kesavananda (1973).", "ta": "தவறு. கோலக்நாத் (1967) கேசவாநந்தாவிற்கு (1973) முன்பே வந்தது."},
            "B": {"en": "Correct. 1 (1967) -> 2 (1973) -> 3 (1975) -> 4 (1980).", "ta": "சரி. 1 (1967) -> 2 (1973) -> 3 (1975) -> 4 (1980)."},
            "C": {"en": "Incorrect. Kesavananda (1973) came BEFORE Indira Nehru Gandhi (1975).", "ta": "தவறு. கேசவாநந்தா (1973) இந்திரா நேரு காந்திக்கு (1975) முன்பே வந்தது."},
            "D": {"en": "Incorrect. Golaknath (1967) was first.", "ta": "தவறு. கோலக்நாத் (1967) முதன்மையானது."}
        },
        tip_en="TNPSC Tip: Chronology: Golaknath (1967) -> Kesavananda (1973) -> Indira Gandhi (1975) -> Minerva Mills (1980).",
        tip_ta="TNPSC குறிப்பு: காலவரிசை: கோலக்நாத் (1967) -> கேசவாநந்தா (1973) -> இந்திரா காந்தி (1975) -> மினர்வா மில்ஸ் (1980).",
        rev_en="Basic Structure Timeline: Golaknath (1967), Kesavananda (1973), Indira Gandhi (1975), Minerva Mills (1980).",
        rev_ta="அடிப்படை கட்டமைப்பு காலவரிசை: கோலக்நாத் (1967), கேசவாநந்தா (1973), இந்திரா காந்தி (1975), மினர்வா மில்ஸ் (1980).",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Analyze", est_sec=60, pyq_sim="High", tags=["Chronology", "Basic Structure", "Landmark Cases"]
    ))

    # Q24 - Conceptual - Hard - Ans C
    qs.append(make_q(
        q_id="SF_GT_024", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Hard", question_type="Conceptual",
        q_en="What is the key difference between 'Procedure Established by Law' and 'Due Process of Law' as applicable in the Indian Judicial System?",
        q_ta="இந்திய நீதித்துறை அமைப்பில் பொருந்தும் 'சட்டத்தால் நிறுவப்பட்ட நடைமுறை' (Procedure Established by Law) மற்றும் 'சட்டத்தின் உரிய நடைமுறை' (Due Process of Law) ஆகியவற்றிற்கு இடையே உள்ள முக்கிய வேறுபாடு என்ன?",
        opts_en=[
            "'Procedure Established by Law' checks both procedural correctness and fairness of law, whereas 'Due Process' checks only procedural correctness.",
            "'Due Process of Law' applies only to financial matters, while 'Procedure Established by Law' applies to fundamental rights.",
            "'Procedure Established by Law' checks whether a law was enacted following proper procedure, while 'Due Process of Law' also checks if the law is just, fair, and reasonable.",
            "There is no practical difference between the two terms in Indian constitutional jurisprudence."
        ],
        opts_ta=[
            "'சட்டத்தால் நிறுவப்பட்ட நடைமுறை' நடைமுறைச் சரி மற்றும் சட்டத்தின் நியாயத்தன்மை ஆகிய இரண்டையும் சரிபார்க்கிறது, அதே நேரத்தில் 'உரிய நடைமுறை' நடைமுறைச் சரியை மட்டுமே சரிபார்க்கிறது.",
            "'சட்டத்தின் உரிய நடைமுறை' நிதி விஷயங்களுக்கு மட்டுமே பொருந்தும், அதே நேரத்தில் 'சட்டத்தால் நிறுவப்பட்ட நடைமுறை' அடிப்படை உரிமைகளுக்குப் பொருந்தும்.",
            "'சட்டத்தால் நிறுவப்பட்ட நடைமுறை' ஒரு சட்டம் சரியான நடைமுறையைப் பின்பற்றி இயற்றப்பட்டதா என்பதைச் சரிபார்க்கிறது, அதே நேரத்தில் 'சட்டத்தின் உரிய நடைமுறை' அச்சட்டம் நீதியானதா, நியாயமானதா மற்றும் ஏதுவானதா என்பதையும் சரிபார்க்கிறது.",
            "இந்திய அரசியலமைப்புச் சட்ட அமைப்பில் இவ்விரு சொற்களுக்கும் இடையே நடைமுறை வேறுபாடு எதுவும் இல்லை."
        ],
        correct_ans="C",
        exp_en="Historical Context: Article 21 originally used 'Procedure Established by Law' (borrowed from Japan). Maneka Gandhi case (1978) expanded it to include 'Due Process of Law' (US concept).\nReason: 'Procedure Established by Law' protects against arbitrary executive action only. 'Due Process of Law' protects against BOTH arbitrary executive action AND arbitrary legislative action.\nConstitutional Impact: Supreme Court ensures laws infringing life and liberty under Art 21 are just, fair, and reasonable.\nExam Trap: Maneka Gandhi Case 1978 introduced 'Due Process' principles into Article 21.\nMemory Trick: Procedure = How law made; Due Process = How law made + Is law fair?",
        exp_ta="வரலாற்றுப் பின்னணி: உறுப்பு 21 ஆரம்பத்தில் 'சட்டத்தால் நிறுவப்பட்ட நடைமுறை' (ஜப்பானிலிருந்து பெறப்பட்டது) என்பதைப் பயன்படுத்தியது. மேனகா காந்தி வழக்கு (1978) அதை 'சட்டத்தின் உரிய நடைமுறை' (அமெரிக்க கருத்து) என விரிவுபடுத்தியது.\nகாரணம்: 'சட்டத்தால் நிறுவப்பட்ட நடைமுறை' தன்னிச்சையான நிர்வாக நடவடிக்கையிலிருந்து மட்டுமே பாதுகாக்கிறது. 'சட்டத்தின் உரிய நடைமுறை' தன்னிச்சையான நிர்வாக நடவடிக்கை மற்றும் தன்னிச்சையான சட்டமன்ற நடவடிக்கை ஆகிய இரண்டிலிருந்தும் பாதுகாக்கிறது.\nஅரசியலமைப்பு தாக்கம்: உறுப்பு 21 இன் கீழ் வாழ்வு மற்றும் சுதந்திரத்தைப் பாதிக்கும் சட்டங்கள் நீதியானவை, நியாயமானவை மற்றும் ஏதுவானவை என்பதை உச்ச நீதிமன்றம் உறுதி செய்கிறது.\nதேர்வுப் பொறி: மேனகா காந்தி வழக்கு 1978 உறுப்பு 21 இல் 'உரிய நடைமுறை' கோட்பாடுகளை அறிமுகப்படுத்தியது.\nநினைவுச் சூத்திரம்: நடைமுறை = சட்டம் எப்படி உருவாக்கப்பட்டது; உரிய நடைமுறை = சட்டம் எப்படி உருவாக்கப்பட்டது + சட்டம் நியாயமானதா?",
        wno_dict={
            "A": {"en": "Incorrect. It is the exact reverse: Due Process checks fairness, Procedure checks enactment steps.", "ta": "தவறு. இது தலைகீழானது: உரிய நடைமுறை நியாயத்தன்மையை சரிபார்க்கிறது, நிறுவப்பட்ட நடைமுறை இயற்றும் படிகளை சரிபார்க்கிறது."},
            "B": {"en": "Incorrect. Neither concept is restricted to financial matters.", "ta": "தவறு. எந்தவொரு கருத்தும் நிதி விஷயங்களுக்கு மட்டும் வரம்பிற்குட்பட்டது அல்ல."},
            "C": {"en": "Correct. Procedure checks legal enactment procedure; Due Process checks substantive fairness & reasonableness.", "ta": "சரி. நிறுவப்பட்ட நடைமுறை சட்டப்பூர்வ இயற்றும் நடைமுறையைச் சரிபார்க்கிறது; உரிய நடைமுறை சட்டத்தின் நியாயத்தன்மையை சரிபார்க்கிறது."},
            "D": {"en": "Incorrect. There is a profound constitutional distinction between the two.", "ta": "தவறு. இரண்டிற்கும் இடையே ஆழமான அரசியலமைப்பு வேறுபாடு உள்ளது."}
        },
        tip_en="TNPSC Tip: Maneka Gandhi Case (1978) read 'Due Process of Law' into Article 21 ('Procedure Established by Law').",
        tip_ta="TNPSC குறிப்பு: மேனகா காந்தி வழக்கு (1978) உறுப்பு 21 இல் ('சட்டத்தால் நிறுவப்பட்ட நடைமுறை') 'சட்டத்தின் உரிய நடைமுறை' கொள்கையை இணைத்தது.",
        rev_en="Procedure Established by Law (Japan) vs Due Process of Law (USA, imported via Maneka Gandhi 1978).",
        rev_ta="சட்டத்தால் நிறுவப்பட்ட நடைமுறை (ஜப்பான்) vs சட்டத்தின் உரிய நடைமுறை (அமெரிக்கா, மேனகா காந்தி 1978 மூலம் சேர்க்கப்பட்டது).",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Analyze", est_sec=75, pyq_sim="High", tags=["Procedure Established by Law", "Due Process of Law", "Article 21"]
    ))

    # Q25 - Statement-Based - Medium - Ans A
    qs.append(make_q(
        q_id="SF_GT_025", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="Statement-Based",
        q_en="Consider the following statements regarding the Rule of Law in India:\n1. The concept of 'Rule of Law' was borrowed from the British Constitution as expounded by A.V. Dicey.\n2. In India, Constitutional Supremacy prevails, and even the Parliament is subject to the Constitution.\n3. The Supreme Court has declared 'Rule of Law' as a Basic Feature of the Constitution that cannot be abrogated.\n\nWhich of the statements given above is/are CORRECT?",
        q_ta="இந்தியாவில் சட்டத்தின் ஆட்சி (Rule of Law) தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 'சட்டத்தின் ஆட்சி' என்ற கருத்து ஏ.வி. டைசி விவரித்தபடி பிரிட்டிஷ் அரசியலமைப்பிலிருந்து பெறப்பட்டது.\n2. இந்தியாவில், அரசியலமைப்பு மேலாதிக்கம் நிலவுகிறது, மேலும் நாடாளுமன்றமும் அரசியலமைப்பிற்கு உட்பட்டது.\n3. உச்ச நீதிமன்றம் 'சட்டத்தின் ஆட்சியை' அரசியலமைப்பின் அடிப்படை அம்சமாக அறிவித்துள்ளது, அதை ரத்து செய்ய முடியாது.\n\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானவை?",
        opts_en=[
            "1, 2 and 3",
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only"
        ],
        opts_ta=[
            "1, 2 மற்றும் 3",
            "1 மற்றும் 2 மட்டும்",
            "2 மற்றும் 3 மட்டும்",
            "1 மற்றும் 3 மட்டும்"
        ],
        correct_ans="A",
        exp_en="Historical Context: Rule of Law is enshrined in Article 14 and pervades the entire Indian constitutional scheme.\nReason:\nStatement 1 is correct: Dicey's Rule of Law (absence of arbitrary power, equality before law) is borrowed from Britain.\nStatement 2 is correct: India follows Constitutional Supremacy rather than Parliamentary Sovereignty.\nStatement 3 is correct: Supreme Court held Rule of Law as part of the Basic Structure in Indira Nehru Gandhi case (1975).\nConstitutional Impact: Protects citizens against arbitrary governance.\nExam Trap: Dicey's 3rd element (primacy of individual rights from judge-made law) does NOT apply to India.",
        exp_ta="வரலாற்றுப் பின்னணி: சட்டத்தின் ஆட்சி உறுப்பு 14 இல் சேர்க்கப்பட்டு முழு இந்திய அரசியலமைப்பு திட்டத்திலும் பரவியுள்ளது.\nகாரணம்:\nகூற்று 1 சரி: டைசியின் சட்டத்தின் ஆட்சி (தன்னிச்சையான அதிகாரம் இல்லாதது, சட்டத்தின் முன் சமநிலை) இங்கிலாந்திலிருந்து பெறப்பட்டது.\nகூற்று 2 சரி: இந்தியா நாடாளுமன்ற இறையாண்மையை விட அரசியலமைப்பு மேலாதிக்கத்தைப் பின்பற்றுகிறது.\nகூற்று 3 சரி: இந்திரா நேரு காந்தி வழக்கில் (1975) உச்ச நீதிமன்றம் சட்டத்தின் ஆட்சியை அடிப்படை அமைப்பின் ஒரு பகுதியாக அறிவித்தது.\nஅரசியலமைப்பு தாக்கம்: தன்னிச்சையான ஆட்சியிலிருந்து குடிமக்களைப் பாதுகாக்கிறது.\nதேர்வுப் பொறி: டைசியின் 3வது கூறு (நீதிபதி உருவாக்கிய சட்டத்திலிருந்து தனிநபர் உரிமைகளின் முதன்மை) இந்தியாவிற்குப் பொருந்தாது.",
        wno_dict={
            "A": {"en": "Correct. Statements 1, 2, and 3 are all correct.", "ta": "சரி. கூற்றுகள் 1, 2 மற்றும் 3 அனைத்தும் சரியானவை."},
            "B": {"en": "Incorrect. Statement 3 is also correct.", "ta": "தவறு. கூற்று 3-ம் சரியானது."},
            "C": {"en": "Incorrect. Statement 1 is also correct.", "ta": "தவறு. கூற்று 1-ம் சரியானது."},
            "D": {"en": "Incorrect. Statement 2 is also correct.", "ta": "தவறு. கூற்று 2-ம் சரியானது."}
        },
        tip_en="TNPSC Tip: Rule of Law is a Basic Structure element (Indira Nehru Gandhi case 1975) embodied in Article 14.",
        tip_ta="TNPSC குறிப்பு: சட்டத்தின் ஆட்சி என்பது உறுப்பு 14 இல் பொதிந்துள்ள ஒரு அடிப்படை கட்டமைப்பு கூறு ஆகும் (இந்திரா நேரு காந்தி வழக்கு 1975).",
        rev_en="Rule of Law (A.V. Dicey, UK) = Basic Structure of Constitution (Article 14).",
        rev_ta="சட்டத்தின் ஆட்சி (ஏ.வி. டைசி, இங்கிலாந்து) = அரசியலமைப்பின் அடிப்படை அமைப்பு (உறுப்பு 14).",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Analyze", est_sec=60, pyq_sim="High", tags=["Rule of Law", "A.V. Dicey", "Basic Structure", "Article 14"]
    ))

    return qs
