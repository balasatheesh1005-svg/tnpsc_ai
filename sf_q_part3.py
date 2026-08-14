# sf_q_part3.py - Questions 51 to 75 for Salient Features Grand Test
from scratch_sf_helper import make_q

def get_part3_questions():
    qs = []

    # Q51 - Direct MCQ - Easy - Ans A
    qs.append(make_q(
        q_id="SF_GT_051", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Easy", question_type="Direct MCQ",
        q_en="Which Part of the Indian Constitution contains the Directive Principles of State Policy (DPSP)?",
        q_ta="இந்திய அரசியலமைப்பின் எந்தப் பகுதியில் அரசு நெறிமுறைப்படுத்தும் கோட்பாடுகள் (DPSP) உள்ளன?",
        opts_en=[
            "Part IV",
            "Part III",
            "Part IVA",
            "Part V"
        ],
        opts_ta=[
            "பகுதி IV",
            "பகுதி III",
            "பகுதி IVA",
            "பகுதி V"
        ],
        correct_ans="A",
        exp_en="Historical Context: DPSP was described by Dr. B.R. Ambedkar as 'novel features' of the Indian Constitution.\nReason: Part IV of the Constitution contains the Directive Principles of State Policy from Articles 36 to 51.\nConstitutional Impact: Aims to establish social and economic democracy and a Welfare State.\nExam Trap: Part III = Fundamental Rights; Part IV = DPSP; Part IVA = Fundamental Duties.\nMemory Trick: Part IV = DPSP (4 letters in DPSP).",
        exp_ta="வரலாற்றுப் பின்னணி: DPSP-ஐ டாக்டர் பி.ஆர். அம்பேத்கர் இந்திய அரசியலமைப்பின் 'நவீன அம்சங்கள்' (novel features) என்று விவரித்தார்.\nகாரணம்: அரசியலமைப்பின் பகுதி IV உறுப்புகள் 36 முதல் 51 வரை அரசு நெறிமுறைப்படுத்தும் கோட்பாடுகளைக் கொண்டுள்ளது.\nஅரசியலமைப்பு தாக்கம்: சமூக மற்றும் பொருளாதார ஜனநாயகம் மற்றும் நலன்புரி அரசை நிறுவுவதை நோக்கமாகக் கொண்டுள்ளது.\nதேர்வுப் பொறி: பகுதி III = அடிப்படை உரிமைகள்; பகுதி IV = DPSP; பகுதி IVA = அடிப்படை கடமைகள்.\nநினைவுச் சூத்திரம்: பகுதி IV = DPSP.",
        wno_dict={
            "A": {"en": "Correct. Part IV contains DPSP (Articles 36 to 51).", "ta": "சரி. பகுதி IV DPSP-ஐக் கொண்டுள்ளது (உறுப்புகள் 36 முதல் 51 வரை)."},
            "B": {"en": "Incorrect. Part III contains Fundamental Rights (Articles 12-35).", "ta": "தவறு. பகுதி III அடிப்படை உரிமைகளைக் கொண்டுள்ளது (உறுப்புகள் 12-35)."},
            "C": {"en": "Incorrect. Part IVA contains Fundamental Duties (Article 51A).", "ta": "தவறு. பகுதி IVA அடிப்படை கடமைகளைக் கொண்டுள்ளது (உறுப்பு 51A)."},
            "D": {"en": "Incorrect. Part V contains The Union Government (Articles 52-151).", "ta": "தவறு. பகுதி V மத்திய அரசைக் கொண்டுள்ளது (உறுப்புகள் 52-151)."}
        },
        tip_en="TNPSC Tip: Part IV = DPSP (Arts 36-51), non-justiciable, establishes Welfare State.",
        tip_ta="TNPSC குறிப்பு: பகுதி IV = DPSP (உறுப்புகள் 36-51), நிலைநிறுத்த முடியாதது, நலன்புரி அரசை நிறுவுகிறது.",
        rev_en="Part IV (Articles 36-51) = Directive Principles of State Policy.",
        rev_ta="பகுதி IV (உறுப்புகள் 36-51) = அரசு நெறிமுறைப்படுத்தும் கோட்பாடுகள்.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Remember", est_sec=30, pyq_sim="High", tags=["DPSP", "Part IV", "Welfare State"]
    ))

    # Q52 - Conceptual - Medium - Ans C
    qs.append(make_q(
        q_id="SF_GT_052", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="Conceptual",
        q_en="What happens to the federal structure of India when a National Emergency under Article 352 is proclaimed?",
        q_ta="உறுப்பு 352 இன் கீழ் தேசிய அவசரநிலை அறிவிக்கப்படும் போது இந்தியாவின் கூட்டாட்சி அமைப்புக்கு என்ன நிகழ்கிறது?",
        opts_en=[
            "The Constitution is formally amended by Parliament into a Unitary Constitution.",
            "State assemblies are automatically dissolved and state territories are merged with Union territories.",
            "The federal structure is converted into a unitary one without a formal amendment of the Constitution.",
            "The Supreme Court assumes executive control over all state governments."
        ],
        opts_ta=[
            "அரசியலமைப்பு நாடாளுமன்றத்தால் ஒரு ஒற்றையாட்சி அரசியலமைப்பாக முறைப்படி திருத்தப்படுகிறது.",
            "மாநில சட்டமன்றங்கள் தானாகவே கலைக்கப்பட்டு மாநிலப் பகுதிகள் யூனியன் பிரதேசங்களுடன் இணைக்கப்படுகின்றன.",
            "அரசியலமைப்பின் முறைப்படியான திருத்தம் இன்றி கூட்டாட்சி அமைப்பு ஒற்றையாட்சி அமைப்பாக மாறுகிறது.",
            "உச்ச நீதிமன்றம் அனைத்து மாநில அரசுகளின் மீதும் நிர்வாகக் கட்டுப்பாட்டை எடுத்துக் கொள்கிறது."
        ],
        correct_ans="C",
        exp_en="Historical Context: Dr. B.R. Ambedkar noted that Indian Constitution can be both federal and unitary according to requirements of time and circumstances.\nReason: During National Emergency (Art 352), Centre gets power to give executive directions to states on any matter, and Parliament can make laws on State List subjects. The system transforms into unitary WITHOUT amending the Constitution.\nConstitutional Impact: Unique constitutional adaptability during national crises.\nExam Trap: No formal constitutional amendment under Art 368 is required to transform the federation into a unitary state during emergency.",
        exp_ta="வரலாற்றுப் பின்னணி: நேரம் மற்றும் சூழ்நிலைகளின் தேவைகளுக்கு ஏற்ப இந்திய அரசியலமைப்பு கூட்டாட்சியாகவும் ஒற்றையாட்சியாகவும் இருக்க முடியும் என்று டாக்டர் பி.ஆர். அம்பேத்கர் குறிப்பிட்டார்.\nகாரணம்: தேசிய அவசரநிலையின் போது (உறுப்பு 352), எந்தவொரு விஷயத்திலும் மாநிலங்களுக்கு நிர்வாக வழிகாட்டுதல்களை வழங்க மத்திய அரசு அதிகாரம் பெறுகிறது, மேலும் நாடாளுமன்றம் மாநிலப் பட்டியல் தலைப்புகளில் சட்டங்களை இயற்ற முடியும். அரசியலமைப்பைத் திருத்தாமல் இந்த அமைப்பு ஒற்றையாட்சியாக மாறுகிறது.\nஅரசியலமைப்பு தாக்கம்: தேசிய நெருக்கடிகளின் போது தனித்துவமான அரசியலமைப்பு தகவமைப்பு.\nதேர்வுப் பொறி: அவசரநிலையின் போது கூட்டாட்சியை ஒற்றையாட்சி மாநிலமாக மாற்ற உறுப்பு 368 இன் கீழ் முறைப்படியான அரசியலமைப்பு திருத்தம் தேவையில்லை.",
        wno_dict={
            "A": {"en": "Incorrect. No formal constitutional amendment under Article 368 takes place.", "ta": "தவறு. உறுப்பு 368 இன் கீழ் முறைப்படியான அரசியலமைப்பு திருத்தம் எதுவும் நடைபெறவில்லை."},
            "B": {"en": "Incorrect. State assemblies are not automatically dissolved; state governments continue under Central direction.", "ta": "தவறு. மாநில சட்டமன்றங்கள் தானாக கலைக்கப்படுவதில்லை; மத்திய வழிகாட்டுதலின் கீழ் மாநில அரசுகள் தொடர்கின்றன."},
            "C": {"en": "Correct. Converted into a unitary system without formal constitutional amendment (Ambedkar).", "ta": "சரி. முறைப்படியான அரசியலமைப்பு திருத்தம் இன்றி ஒற்றையாட்சி அமைப்பாக மாறுகிறது (அம்பேத்கர்)."},
            "D": {"en": "Incorrect. Supreme Court does not assume executive control.", "ta": "தவறு. உச்ச நீதிமன்றம் நிர்வாகக் கட்டுப்பாட்டை எடுத்துக்கொள்வதில்லை."}
        },
        tip_en="TNPSC Tip: During Emergency under Art 352, federal setup converts to unitary setup WITHOUT formal constitutional amendment.",
        tip_ta="TNPSC குறிப்பு: உறுப்பு 352 இன் கீழ் அவசரநிலையின் போது, முறைப்படியான அரசியலமைப்பு திருத்தம் இன்றி கூட்டாட்சி அமைப்பு ஒற்றையாட்சி அமைப்பாக மாறுகிறது.",
        rev_en="Emergency transform: Federal to Unitary without formal Constitutional Amendment.",
        rev_ta="அவசரக்கால மாற்றம்: முறைப்படியான அரசியலமைப்பு திருத்தம் இன்றி கூட்டாட்சியிலிருந்து ஒற்றையாட்சிக்கு.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Understand", est_sec=60, pyq_sim="High", tags=["Emergency Provisions", "Article 352", "Federal to Unitary"]
    ))

    # Q53 - Statement-Based - Medium - Ans B
    qs.append(make_q(
        q_id="SF_GT_053", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="Statement-Based",
        q_en="Consider the following statements regarding the Comptroller and Auditor General of India (CAG):\n1. CAG audits all expenditure from the Consolidated Fund of India, Consolidated Fund of each State, and Union Territory having a Legislative Assembly.\n2. CAG holds office for a term of six years or until attaining the age of 65 years, whichever is earlier.\n3. CAG is eligible for further appointment under the Government of India or any State after relinquishing office.\n\nWhich of the statements given above are CORRECT?",
        q_ta="இந்திய தலைமை தணிக்கை அதிகாரி (CAG) தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. CAG இந்தியத் தொகுப்பு நிதி, ஒவ்வொரு மாநிலத்தின் தொகுப்பு நிதி மற்றும் சட்டமன்றம் கொண்ட யூனியன் பிரதேசத்தின் அனைத்துச் செலவுகளையும் தணிக்கை செய்கிறார்.\n2. CAG ஆறு ஆண்டுகள் அல்லது 65 வயதை அடையும் வரை, இதில் எது முந்தையதோ அதுவரை பதவியில் இருப்பார்.\n3. CAG பதவியிலிருந்து விலகிய பிறகு இந்திய அரசிலோ அல்லது எந்த மாநில அரசிலோ மேலும் நியமனத்திற்குத் தகுதியுடையவர்.\n\nமேற்கூறிய கூற்றுகளில் எது சரியானவை?",
        opts_en=[
            "1 and 3 only",
            "1 and 2 only",
            "2 and 3 only",
            "1, 2 and 3"
        ],
        opts_ta=[
            "1 மற்றும் 3 மட்டும்",
            "1 மற்றும் 2 மட்டும்",
            "2 மற்றும் 3 மட்டும்",
            "1, 2 மற்றும் 3"
        ],
        correct_ans="B",
        exp_en="Historical Context: CAG is the Guardian of the Public Purse and an independent bulwark of democracy.\nReason:\nStatement 1 is correct: CAG audits expenditure from Consolidated Funds of Centre, States, and UTs with Assembly.\nStatement 2 is correct: Tenure is 6 years or 65 years of age (whichever is earlier).\nStatement 3 is INCORRECT: Article 148(4) explicitly states CAG is NOT eligible for further office under the Government of India or any State after ceasing to hold office.\nConstitutional Impact: Ensures complete independence from post-retirement executive inducements.",
        exp_ta="வரலாற்றுப் பின்னணி: CAG பொதுப் பணத்தின் பாதுகாவலன் மற்றும் ஜனநாயகத்தின் சுதந்திரமான தூண் ஆவார்.\nகாரணம்:\nகூற்று 1 சரி: மத்திய அரசு, மாநிலங்கள் மற்றும் சட்டமன்றம் கொண்ட யூனியன் பிரதேசங்களின் தொகுப்பு நிதியிலிருந்து ஏற்படும் செலவினங்களை CAG தணிக்கை செய்கிறார்.\nகூற்று 2 சரி: பதவிக்காலம் 6 ஆண்டுகள் அல்லது 65 வயது (எது முந்தையதோ).\nகூற்று 3 தவறு: பதவிக்காலம் முடிந்த பிறகு இந்திய அரசிலோ அல்லது எந்த மாநில அரசிலோ CAG மேலும் பதவி வகிக்கத் தகுதியற்றவர் என்று உறுப்பு 148(4) வெளிப்படையாகக் கூறுகிறது.\nஅரசியலமைப்பு தாக்கம்: ஓய்வுக்குப் பிந்தைய நிர்வாக சலுகைகளிலிருந்து முழுமையான சுதந்திரத்தை உறுதி செய்கிறது.",
        wno_dict={
            "A": {"en": "Incorrect. Statement 3 is false under Article 148(4).", "ta": "தவறு. உறுப்பு 148(4) இன் கீழ் கூற்று 3 தவறு."},
            "B": {"en": "Correct. Statements 1 and 2 are correct; Statement 3 is false.", "ta": "சரி. கூற்றுகள் 1 மற்றும் 2 சரி; கூற்று 3 தவறு."},
            "C": {"en": "Incorrect. Statement 3 is false.", "ta": "தவறு. கூற்று 3 தவறு."},
            "D": {"en": "Incorrect. Statement 3 is false.", "ta": "தவறு. கூற்று 3 தவறு."}
        },
        tip_en="TNPSC Trap: CAG is NOT eligible for further appointment under Govt of India or State after retirement (Art 148(4)).",
        tip_ta="TNPSC பொறி: CAG ஓய்வு பெற்ற பிறகு இந்திய அரசு அல்லது மாநில அரசின் கீழ் மேலும் நியமனத்திற்குத் தகுதியற்றவர் (உறுப்பு 148(4)).",
        rev_en="CAG: Tenure 6 yrs / 65 yrs; NOT eligible for re-employment after retirement.",
        rev_ta="CAG: பதவிக்காலம் 6 ஆண்டுகள் / 65 வயது; ஓய்வுக்குப் பிறகு மறுநியமனத்திற்குத் தகுதியற்றவர்.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Analyze", est_sec=60, pyq_sim="High", tags=["CAG", "Article 148", "Constitutional Bodies", "TNPSC Trap"]
    ))

    # Q54 - Assertion & Reason - Hard - Ans D
    qs.append(make_q(
        q_id="SF_GT_054", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Hard", question_type="Assertion & Reason",
        q_en="Given below are two statements, one labeled as Assertion (A) and the other labeled as Reason (R):\n\nAssertion (A): The Indian Constitution provides for a system of Judicial Review, making courts the ultimate interpreters of constitutional validity.\nReason (R): Indian Parliament is a sovereign legislative body modeled strictly on the British doctrine of Parliamentary Sovereignty.",
        q_ta="கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிக்கப்பட்டுள்ளது:\n\nகூற்று (A): இந்திய அரசியலமைப்பு நீதித்துறை மறுஆய்வு முறையை வழங்குகிறது, நீதிமன்றங்களை அரசியலமைப்பு செல்லுபடியாகும் தன்மையின் இறுதியான வியாக்கியானிகளாக ஆக்குகிறது.\nகாரணம் (R): இந்திய நாடாளுமன்றம் பிரிட்டிஷ் நாடாளுமன்ற இறையாண்மைக் கோட்பாட்டின் அடிப்படையில் மட்டுமே மாதிரியாக வடிவமைக்கப்பட்ட ஒரு இறையாண்மை கொண்ட சட்டமன்ற அமைப்பாகும்.",
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
        correct_ans="C",
        exp_en="Historical Context: The Indian polity synthesizes American Judicial Supremacy with British Parliamentary Sovereignty.\nReason: Assertion (A) is TRUE: Judicial Review is an established Basic Feature in India. Reason (R) is FALSE: Indian Parliament is NOT sovereign; its powers are limited by a written Constitution, division of powers, and Fundamental Rights.\nConstitutional Impact: Ensures Constitutional Supremacy above both Legislature and Executive.\nExam Trap: British Parliament is Sovereign; Indian Parliament is NOT Sovereign.",
        exp_ta="வரலாற்றுப் பின்னணி: இந்திய அரசியல் அமைப்பு அமெரிக்க நீதித்துறை மேலாதிக்கத்தையும் பிரிட்டிஷ் நாடாளுமன்ற இறையாண்மையையும் இணைக்கிறது.\nகாரணம்: கூற்று (A) சரி: நீதித்துறை மறுஆய்வு இந்தியாவில் ஒரு நிறுவப்பட்ட அடிப்படை அம்சமாகும். காரணம் (R) தவறு: இந்திய நாடாளுமன்றம் இறையாண்மை கொண்டது அல்ல; அதன் அதிகாரங்கள் எழுதப்பட்ட அரசியலமைப்பு, அதிகாரப் பகிர்வு மற்றும் அடிப்படை உரிமைகளால் வரம்பிற்குட்பட்டவை.\nஅரசியலமைப்பு தாக்கம்: சட்டமன்றம் மற்றும் நிர்வாகத் துறை ஆகிய இரண்டிற்கும் மேலாக அரசியலமைப்பு மேலாதிக்கத்தை உறுதி செய்கிறது.\nதேர்வுப் பொறி: பிரிட்டிஷ் நாடாளுமன்றம் இறையாண்மை கொண்டது; இந்திய நாடாளுமன்றம் இறையாண்மை கொண்டது அல்ல.",
        wno_dict={
            "A": {"en": "Incorrect. (R) is completely false because Indian Parliament is not sovereign.", "ta": "தவறு. (R) முற்றிலும் தவறு ஏனெனில் இந்திய நாடாளுமன்றம் இறையாண்மை கொண்டது அல்ல."},
            "B": {"en": "Incorrect. (R) is false.", "ta": "தவறு. (R) தவறு."},
            "C": {"en": "Correct. (A) is true (Judicial Review exists) but (R) is false (Indian Parliament is NOT sovereign).", "ta": "சரி. (A) சரி (நீதித்துறை மறுஆய்வு உள்ளது) ஆனால் (R) தவறு (இந்திய நாடாளுமன்றம் இறையாண்மை கொண்டது அல்ல)."},
            "D": {"en": "Incorrect. (A) is true.", "ta": "தவறு. (A) உண்மை."}
        },
        tip_en="TNPSC Tip: Indian Parliament is NOT sovereign (unlike UK Parliament) because of written Constitution & Judicial Review.",
        tip_ta="TNPSC குறிப்பு: எழுதப்பட்ட அரசியலமைப்பு & நீதித்துறை மறுஆய்வு காரணமாக இந்திய நாடாளுமன்றம் இறையாண்மை கொண்டது அல்ல (இங்கிலாந்து நாடாளுமன்றத்தைப் போலல்லாமல்).",
        rev_en="Indian Parliament: Non-sovereign, bound by written Constitution & Judicial Review.",
        rev_ta="இந்திய நாடாளுமன்றம்: இறையாண்மையற்றது, எழுதப்பட்ட அரசியலமைப்பு & நீதித்துறை மறுஆய்வுக்கு கட்டுப்பட்டது.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Evaluate", est_sec=60, pyq_sim="High", tags=["Parliamentary Sovereignty", "Judicial Review", "Constitutional Supremacy"]
    ))

    # Q55 - Match the Following - Medium - Ans A
    qs.append(make_q(
        q_id="SF_GT_055", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="Match the Following",
        q_en="Match List-I (Emergency Type) with List-II (Article Number) and select the correct option:\n\nList-I:\n(a) National Emergency\n(b) President's Rule (State Emergency)\n(c) Financial Emergency\n(d) Constitutional Machinery Failure via Union Directions\n\nList-II:\n1. Article 356\n2. Article 365\n3. Article 352\n4. Article 360",
        q_ta="பட்டியல்-I (அவசரக்கால வகை) பட்டியல்-II (உறுப்பு எண்) உடன் பொருத்தி சரியான விருப்பத்தைத் தேர்ந்தெடுக்கவும்:\n\nபட்டியல்-I:\n(a) தேசிய அவசரநிலை\n(b) குடியரசுத் தலைவர் ஆட்சி (மாநில அவசரநிலை)\n(c) நிதி அவசரநிலை\n(d) மத்திய வழிகாட்டுதல்கள் மூலம் அரசியலமைப்பு இயந்திரத் தோல்வி\n\nபட்டியல்-II:\n1. உறுப்பு 356\n2. உறுப்பு 365\n3. உறுப்பு 352\n4. உறுப்பு 360",
        opts_en=[
            "(a)-3, (b)-1, (c)-4, (d)-2",
            "(a)-1, (b)-3, (c)-4, (d)-2",
            "(a)-3, (b)-4, (c)-1, (d)-2",
            "(a)-4, (b)-1, (c)-3, (d)-2"
        ],
        opts_ta=[
            "(a)-3, (b)-1, (c)-4, (d)-2",
            "(a)-1, (b)-3, (c)-4, (d)-2",
            "(a)-3, (b)-4, (c)-1, (d)-2",
            "(a)-4, (b)-1, (c)-3, (d)-2"
        ],
        correct_ans="A",
        exp_en="Historical Context: Emergency Provisions are contained in Part XVIII (Articles 352-360).\nReason:\n(a) National Emergency = Article 352 (3)\n(b) President's Rule = Article 356 (1)\n(c) Financial Emergency = Article 360 (4)\n(d) Union Directive Failure = Article 365 (2)\nMatching: (a)-3, (b)-1, (c)-4, (d)-2.",
        exp_ta="வரலாற்றுப் பின்னணி: அவசரக்கால விதிகள் பகுதி XVIII இல் உள்ளன (உறுப்புகள் 352-360).\nகாரணம்:\n(a) தேசிய அவசரநிலை = உறுப்பு 352 (3)\n(b) குடியரசுத் தலைவர் ஆட்சி = உறுப்பு 356 (1)\n(c) நிதி அவசரநிலை = உறுப்பு 360 (4)\n(d) மத்திய வழிகாட்டுதல் தோல்வி = உறுப்பு 365 (2)\nபொருத்துதல்: (a)-3, (b)-1, (c)-4, (d)-2.",
        wno_dict={
            "A": {"en": "Correct. (a)-3, (b)-1, (c)-4, (d)-2 correctly matches all emergency articles.", "ta": "சரி. (a)-3, (b)-1, (c)-4, (d)-2 அனைத்து அவசரக்கால உறுப்புகளையும் சரியாகப் பொருத்துகிறது."},
            "B": {"en": "Incorrect. National Emergency is Art 352 (3), not Art 356 (1).", "ta": "தவறு. தேசிய அவசரநிலை உறுப்பு 352 (3), உறுப்பு 356 (1) அல்ல."},
            "C": {"en": "Incorrect. Financial Emergency is Art 360 (4), not Art 356 (1).", "ta": "தவறு. நிதி அவசரநிலை உறுப்பு 360 (4), உறுப்பு 356 (1) அல்ல."},
            "D": {"en": "Incorrect. National Emergency is Art 352 (3), not Art 360 (4).", "ta": "தவறு. தேசிய அவசரநிலை உறுப்பு 352 (3), உறுப்பு 360 (4) அல்ல."}
        },
        tip_en="TNPSC Tip: Remember: 352 (National), 356 (President's Rule - State), 360 (Financial), 365 (Union direction failure).",
        tip_ta="TNPSC குறிப்பு: நினைவில் கொள்க: 352 (தேசியம்), 356 (குடியரசுத் தலைவர் ஆட்சி - மாநிலம்), 360 (நிதி), 365 (மத்திய வழிகாட்டுதல் தோல்வி).",
        rev_en="Emergency Articles: 352 (National), 356 (President's Rule), 360 (Financial), 365 (Disobeying Union).",
        rev_ta="அவசரக்கால உறுப்புகள்: 352 (தேசியம்), 356 (குடியரசுத் தலைவர் ஆட்சி), 360 (நிதி), 365 (மத்திய அரசை மீறுதல்).",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Remember", est_sec=60, pyq_sim="High", tags=["Emergency Provisions", "Article 352", "Article 356", "Article 360", "Article 365"]
    ))

    # Q56 - Chronology - Medium - Ans B
    qs.append(make_q(
        q_id="SF_GT_056", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="Chronology",
        q_en="Arrange the following historic events related to the evolution of the Indian Constitution in chronological order:\n1. Insertion of Fundamental Duties via 42nd Amendment Act\n2. Commencement of the Indian Constitution\n3. Enactment of 73rd and 74th Amendment Acts (Local Government)\n4. Reduction of voting age to 18 years via 61st Amendment Act",
        q_ta="இந்திய அரசியலமைப்பின் வளர்ச்சியுடன் தொடர்புடைய பின்வரும் வரலாற்றுச் நிகழ்வுகளைக் காலவரிசைப்படி வரிசைப்படுத்தவும்:\n1. 42வது திருத்தச் சட்டம் மூலம் அடிப்படை கடமைகள் சேர்ப்பு\n2. இந்திய அரசியலமைப்பின் நடைமுறை தொடக்கம்\n3. 73வது மற்றும் 74வது திருத்தச் சட்டங்கள் இயற்றப்படுதல் (உள்ளாட்சி அரசு)\n4. 61வது திருத்தச் சட்டம் மூலம் வாக்களிக்கும் வயது 18 ஆகக் குறைக்கப்படுதல்",
        opts_en=[
            "2 - 1 - 3 - 4",
            "2 - 1 - 4 - 3",
            "1 - 2 - 4 - 3",
            "2 - 4 - 1 - 3"
        ],
        opts_ta=[
            "2 - 1 - 3 - 4",
            "2 - 1 - 4 - 3",
            "1 - 2 - 4 - 3",
            "2 - 4 - 1 - 3"
        ],
        correct_ans="B",
        exp_en="Historical Context: Key constitutional milestones shaped the democratic structure of India over time.\nReason:\n2. Commencement of Constitution: January 26, 1950.\n1. 42nd Amendment Act (FDs added): 1976.\n4. 61st Amendment Act (Voting age 18): 1988.\n3. 73rd and 74th Amendment Acts (Panchayats & Municipalities): 1992.\nSequence: 2 (1950) -> 1 (1976) -> 4 (1988) -> 3 (1992).",
        exp_ta="வரலாற்றுப் பின்னணி: முக்கிய அரசியலமைப்பு மைல்கற்கள் காலப்போக்கில் இந்தியாவின் ஜனநாயகக் கட்டமைப்பை வடிவமைத்தன.\nகாரணம்:\n2. அரசியலமைப்பின் நடைமுறை தொடக்கம்: ஜனவரி 26, 1950.\n1. 42வது திருத்தச் சட்டம் (FDகள் சேர்க்கப்பட்டது): 1976.\n4. 61வது திருத்தச் சட்டம் (வாக்கு வயது 18): 1988.\n3. 73வது மற்றும் 74வது திருத்தச் சட்டங்கள் (பஞ்சாயத்துகள் & நகராட்சிகள்): 1992.\nவரிசை: 2 (1950) -> 1 (1976) -> 4 (1988) -> 3 (1992).",
        wno_dict={
            "A": {"en": "Incorrect. 61st Amendment (1988) came BEFORE 73rd/74th Amendments (1992).", "ta": "தவறு. 61வது திருத்தம் (1988) 73வது/74வது திருத்தங்களுக்கு (1992) முன்பே வந்தது."},
            "B": {"en": "Correct. 1950 -> 1976 -> 1988 -> 1992.", "ta": "சரி. 1950 -> 1976 -> 1988 -> 1992."},
            "C": {"en": "Incorrect. Commencement of Constitution (1950) came before 42nd Amendment (1976).", "ta": "தவறு. அரசியலமைப்பு தொடக்கம் (1950) 42வது திருத்தத்திற்கு (1976) முன்பே வந்தது."},
            "D": {"en": "Incorrect. 42nd Amendment (1976) came before 61st Amendment (1988).", "ta": "தவறு. 42வது திருத்தம் (1976) 61வது திருத்தத்திற்கு (1988) முன்பே வந்தது."}
        },
        tip_en="TNPSC Tip: Chronology order: 1950 (Commencement) -> 1976 (42nd) -> 1988 (61st) -> 1992 (73rd/74th).",
        tip_ta="TNPSC குறிப்பு: காலவரிசை: 1950 (தொடக்கம்) -> 1976 (42வது) -> 1988 (61வது) -> 1992 (73வது/74வது).",
        rev_en="Constitutional Timeline: 1950 (Enforcement), 1976 (FDs), 1988 (Voting Age 18), 1992 (Local Self-Govt).",
        rev_ta="அரசியலமைப்பு காலவரிசை: 1950 (அமலாக்கம்), 1976 (FDகள்), 1988 (வாக்கு வயது 18), 1992 (உள்ளாட்சி சுயாட்சி).",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Analyze", est_sec=60, pyq_sim="High", tags=["Chronology", "Constitutional Timeline", "Amendments"]
    ))

    # Q57 - Hard / Analytical - Hard - Ans C
    qs.append(make_q(
        q_id="SF_GT_057", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Hard", question_type="Hard / Analytical",
        q_en="Which of the following elements has NOT been declared by the Supreme Court as a part of the 'Basic Structure' of the Indian Constitution?",
        q_ta="பின்வரும் கூறுகளில் எதை உச்ச நீதிமன்றம் இந்திய அரசியலமைப்பின் 'அடிப்படை அமைப்பின்' (Basic Structure) ஒரு பகுதி அல்ல என அறிவித்துள்ளது?",
        opts_en=[
            "Supremacy of the Constitution and Secular character of the polity",
            "Rule of Law and Power of Judicial Review",
            "Absolute power of Union Parliament to amend any part of the Constitution without judicial scrutiny",
            "Free and fair elections and Independence of the Judiciary"
        ],
        opts_ta=[
            "அரசியலமைப்பின் மேலாதிக்கம் மற்றும் அரசியல் அமைப்பின் மதச்சார்பற்ற தன்மை",
            "சட்டத்தின் ஆட்சி மற்றும் நீதித்துறை மறுஆய்வு அதிகாரம்",
            "நீதித்துறை ஆய்வின்றி அரசியலமைப்பின் எந்தப் பகுதியையும் திருத்த மத்திய நாடாளுமன்றத்தின் முழுமையான அதிகாரம்",
            "சுதந்திரமான மற்றும் நேர்மையான தேர்தல்கள் மற்றும் நீதித்துறை சுதந்திரம்"
        ],
        correct_ans="C",
        exp_en="Historical Context: The Basic Structure Doctrine limits parliamentary amending power to protect constitutional democracy.\nReason: Absolute, unbridled amending power of Parliament is NOT part of the Basic Structure; in fact, the Supreme Court specifically struck down Section 55 of 42nd Amendment (which gave unlimited amending power to Parliament) in Minerva Mills Case (1980) as contrary to Basic Structure.\nConstitutional Impact: Limited amending power itself is a basic feature.\nExam Trap: Parliament's amending power under Art 368 is LIMITED, not absolute.",
        exp_ta="வரலாற்றுப் பின்னணி: அடிப்படை கட்டமைப்பு கோட்பாடு ஜனநாயகத்தைப் பாதுகாக்க நாடாளுமன்ற திருத்தும் அதிகாரத்தைக் கட்டுப்படுத்துகிறது.\nகாரணம்: நாடாளுமன்றத்தின் முழுமையான, தடையற்ற திருத்தும் அதிகாரம் அடிப்படை அமைப்பின் ஒரு பகுதி அல்ல; உண்மையில், மினர்வா மில்ஸ் வழக்கில் (1980) 42வது திருத்தத்தின் பிரிவு 55 ஐ (நாடாளுமன்றத்திற்கு வரம்பற்ற திருத்தும் அதிகாரத்தை வழங்கியது) அடிப்படை அமைப்பிற்கு எதிரானது என உச்ச நீதிமன்றம் ரத்து செய்தது.\nஅரசியலமைப்பு தாக்கம்: வரம்பிற்குட்பட்ட திருத்தும் அதிகாரமே ஒரு அடிப்படை அம்சமாகும்.\nதேர்வுப் பொறி: உறுப்பு 368 இன் கீழ் நாடாளுமன்றத்தின் திருத்தும் அதிகாரம் வரம்பிற்குட்பட்டது, முழுமையானது அல்ல.",
        wno_dict={
            "A": {"en": "Incorrect. Supremacy of Constitution and Secularism are confirmed Basic Structure features.", "ta": "தவறு. அரசியலமைப்பு மேலாதிக்கம் மற்றும் மதச்சார்பின்மை ஆகியவை உறுதிப்படுத்தப்பட்ட அடிப்படை அமைப்பின் அம்சங்கள்."},
            "B": {"en": "Incorrect. Rule of Law and Judicial Review are Basic Structure features.", "ta": "தவறு. சட்டத்தின் ஆட்சி மற்றும் நீதித்துறை மறுஆய்வு ஆகியவை அடிப்படை அமைப்பின் அம்சங்கள்."},
            "C": {"en": "Correct. Absolute unbridled amending power of Parliament is NOT part of Basic Structure (struck down in Minerva Mills 1980).", "ta": "சரி. நாடாளுமன்றத்தின் முழுமையான தடையற்ற திருத்தும் அதிகாரம் அடிப்படை அமைப்பின் பகுதி அல்ல (மினர்வா மில்ஸ் 1980 இல் ரத்து செய்யப்பட்டது)."},
            "D": {"en": "Incorrect. Free & fair elections and Judicial Independence are Basic Structure features.", "ta": "தவறு. சுதந்திரமான & நேர்மையான தேர்தல்கள் மற்றும் நீதித்துறை சுதந்திரம் ஆகியவை அடிப்படை அமைப்பின் அம்சங்கள்."}
        },
        tip_en="TNPSC Tip: Limited amending power of Parliament is a Basic Structure element (Minerva Mills Case 1980).",
        tip_ta="TNPSC குறிப்பு: நாடாளுமன்றத்தின் வரம்பிற்குட்பட்ட திருத்தும் அதிகாரமே ஒரு அடிப்படை கட்டமைப்பு கூறு ஆகும் (மினர்வா மில்ஸ் வழக்கு 1980).",
        rev_en="Basic Structure elements: Supremacy of Constitution, Secularism, Rule of Law, Judicial Review, Limited Amending Power.",
        rev_ta="அடிப்படை கட்டமைப்பு கூறுகள்: அரசியலமைப்பு மேலாதிக்கம், மதச்சார்பின்மை, சட்டத்தின் ஆட்சி, நீதித்துறை மறுஆய்வு, வரம்பிற்குட்பட்ட திருத்தும் அதிகாரம்.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Analyze", est_sec=60, pyq_sim="High", tags=["Basic Structure", "Minerva Mills Case", "Parliamentary Amending Power"]
    ))

    # Q58 - Direct MCQ - Easy - Ans D
    qs.append(make_q(
        q_id="SF_GT_058", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Easy", question_type="Direct MCQ",
        q_en="Under Article 315 of the Indian Constitution, Public Service Commissions are established for:",
        q_ta="இந்திய அரசியலமைப்பின் உறுப்பு 315 இன் கீழ், அரசுப் பணியாளர் தேர்வாணையங்கள் எதற்காக நிறுவப்படுகின்றன?",
        opts_en=[
            "The Union only",
            "The States only",
            "Joint Public Service Commissions only",
            "The Union and for each State"
        ],
        opts_ta=[
            "ஒன்றியத்திற்கு மட்டுமே",
            "மாநிலங்களுக்கு மட்டுமே",
            "கூட்டு அரசுப் பணியாளர் தேர்வாணையங்களுக்கு மட்டுமே",
            "ஒன்றியத்திற்கும் ஒவ்வொரு மாநிலத்திற்கும்"
        ],
        correct_ans="D",
        exp_en="Historical Context: Public Service Commissions serve as the merit watchdogs in civil service recruitment.\nReason: Article 315(1) mandates that there shall be a Public Service Commission for the Union (UPSC) and a Public Service Commission for each State (SPSC).\nConstitutional Impact: Ensures impartial merit-based recruitment to public services.\nExam Trap: Article 315 covers BOTH Union Public Service Commission and State Public Service Commissions.\nMemory Trick: Art 315 = UPSC + SPSC.",
        exp_ta="வரலாற்றுப் பின்னணி: அரசுப் பணியாளர் தேர்வாணையங்கள் குடிமைப் பணி நியமனங்களில் தகுதிப் பாதுகாவலர்களாகச் செயல்படுகின்றன.\nகாரணம்: உறுப்பு 315(1) ஒன்றியத்திற்கு ஒரு அரசுப் பணியாளர் தேர்வாணையமும் (UPSC) ஒவ்வொரு மாநிலத்திற்கும் ஒரு அரசுப் பணியாளர் தேர்வாணையமும் (SPSC) இருக்க வேண்டும் என ஆணையிடுகிறது.\nஅரசியலமைப்பு தாக்கம்: பொதுப் பணிகளுக்கு நடுநிலையான தகுதி அடிப்படையிலான நியமனத்தை உறுதி செய்கிறது.\nதேர்வுப் பொறி: உறுப்பு 315 மத்திய அரசுப் பணியாளர் தேர்வாணையம் மற்றும் மாநில அரசுப் பணியாளர் தேர்வாணையங்கள் இரண்டையும் உள்ளடக்கியது.\nநினைவுச் சூத்திரம்: உறுப்பு 315 = UPSC + SPSC.",
        wno_dict={
            "A": {"en": "Incorrect. Article 315 covers both Union and States.", "ta": "தவறு. உறுப்பு 315 ஒன்றியம் மற்றும் மாநிலங்கள் இரண்டையும் உள்ளடக்கியது."},
            "B": {"en": "Incorrect. Covers both Union and States.", "ta": "தவறு. ஒன்றியம் மற்றும் மாநிலங்கள் இரண்டையும் உள்ளடக்கியது."},
            "C": {"en": "Incorrect. Joint PSC is created by an Act of Parliament (statutory), not directly under Art 315(1).", "ta": "தவறு. கூட்டு PSC நாடாளுமன்றச் சட்டத்தால் உருவாக்கப்படுகிறது, நேரடியாக உறுப்பு 315(1) இன் கீழ் அல்ல."},
            "D": {"en": "Correct. Article 315 establishes PSCs for the Union and for each State.", "ta": "சரி. உறுப்பு 315 ஒன்றியத்திற்கும் ஒவ்வொரு மாநிலத்திற்கும் PSCகளை நிறுவுகிறது."}
        },
        tip_en="TNPSC Tip: Article 315 establishes Union Public Service Commission (UPSC) and State Public Service Commissions (SPSC).",
        tip_ta="TNPSC குறிப்பு: உறுப்பு 315 மத்திய அரசுப் பணியாளர் தேர்வாணையத்தையும் (UPSC) மாநில அரசுப் பணியாளர் தேர்வாணையங்களையும் (SPSC) நிறுவுகிறது.",
        rev_en="Article 315: UPSC for Union and SPSC for each State.",
        rev_ta="உறுப்பு 315: ஒன்றியத்திற்கு UPSC மற்றும் ஒவ்வொரு மாநிலத்திற்கும் SPSC.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Remember", est_sec=30, pyq_sim="High", tags=["Article 315", "UPSC", "SPSC", "Constitutional Bodies"]
    ))

    # Q59 - PYQ Pattern - Medium - Ans A
    qs.append(make_q(
        q_id="SF_GT_059", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="PYQ Pattern",
        q_en="Which Constitutional Amendment Act is popularly referred to as the 'Mini-Constitution' due to its comprehensive and sweeping changes?",
        q_ta="அதனுடைய விரிவான மற்றும் பரந்த மாற்றங்கள் காரணமாக 'குறு-அரசியலமைப்பு' (Mini-Constitution) என்று பிரபலமாகக் குறிப்பிடப்படும் அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        opts_en=[
            "42nd Constitutional Amendment Act, 1976",
            "44th Constitutional Amendment Act, 1978",
            "24th Constitutional Amendment Act, 1971",
            "73rd Constitutional Amendment Act, 1992"
        ],
        opts_ta=[
            "42வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
            "44வது அரசியலமைப்பு திருத்தச் சட்டம், 1978",
            "24வது அரசியலமைப்பு திருத்தச் சட்டம், 1971",
            "73வது அரசியலமைப்பு திருத்தச் சட்டம், 1992"
        ],
        correct_ans="A",
        exp_en="Historical Context: Enacted during internal emergency under Indira Gandhi government to implement recommendations of Swaran Singh Committee.\nReason: The 42nd Constitutional Amendment Act 1976 made massive changes to Preamble (added Socialist, Secular, Integrity), added Part IVA (Fundamental Duties), modified Articles 31C, 39, 39A, 43A, 48A, changed Lok Sabha duration to 6 yrs, etc., earning the title 'Mini-Constitution'.\nConstitutional Impact: Restructured large parts of the constitutional text.\nExam Trap: 42nd Amendment (1976) = Mini-Constitution; 44th Amendment (1978) = Undid many 42nd Amendment distortions.",
        exp_ta="வரலாற்றுப் பின்னணி: ஸ்வரன் சிங் குழுவின் பரிந்துரைகளை அமல்படுத்த இந்திரா காந்தி அரசாங்கத்தின் கீழ் உள்நாட்டு அவசரநிலையின் போது இயற்றப்பட்டது.\nகாரணம்: 42வது அரசியலமைப்பு திருத்தச் சட்டம் 1976 முகவுரையில் மிகப்பெரிய மாற்றங்களை செய்தது (சமதர்ம, மதச்சார்பற்ற, ஒருமைப்பாடு சேர்க்கப்பட்டது), பகுதி IVA ஐச் சேர்த்தது (அடிப்படை கடமைகள்), உறுப்புகள் 31C, 39, 39A, 43A, 48A ஐ மாற்றியது, மக்களவை காலத்தை 6 ஆண்டுகளாக மாற்றியது போன்ற காரணங்களால் 'குறு-அரசியலமைப்பு' என்ற பட்டத்தைப் பெற்றது.\nஅரசியலமைப்பு தாக்கம்: அரசியலமைப்பு உரையின் பெரும்பகுதியை மாற்றியமைத்தது.\nதேர்வுப் பொறி: 42வது திருத்தம் (1976) = குறு-அரசியலமைப்பு; 44வது திருத்தம் (1978) = 42வது திருத்தத்தின் பல மாற்றங்களை ரத்து செய்தது.",
        wno_dict={
            "A": {"en": "Correct. 42nd Amendment Act 1976 is known as the Mini-Constitution.", "ta": "சரி. 42வது திருத்தச் சட்டம் 1976 குறு-அரசியலமைப்பு என்று அழைக்கப்படுகிறது."},
            "B": {"en": "Incorrect. 44th Amendment 1978 corrected distortions made by 42nd Amendment.", "ta": "தவறு. 44வது திருத்தம் 1978 42வது திருத்தத்தால் செய்யப்பட்ட மாற்றங்களைச் சரிசெய்தது."},
            "C": {"en": "Incorrect. 24th Amendment 1971 affirmed Parliament's power to amend any part of Constitution.", "ta": "தவறு. 24வது திருத்தம் 1971 அரசியலமைப்பின் எந்தப் பகுதியையும் திருத்த நாடாளுமன்றத்தின் அதிகாரத்தை உறுதிப்படுத்தியது."},
            "D": {"en": "Incorrect. 73rd Amendment 1992 added Part IX for Panchayati Raj.", "ta": "தவறு. 73வது திருத்தம் 1992 பஞ்சாயத்து ராஜிற்காக பகுதி IX ஐச் சேர்த்தது."}
        },
        tip_en="TNPSC Tip: 42nd Constitutional Amendment Act 1976 = 'Mini-Constitution' (Swaran Singh Committee).",
        tip_ta="TNPSC குறிப்பு: 42வது அரசியலமைப்பு திருத்தச் சட்டம் 1976 = 'குறு-அரசியலமைப்பு' (ஸ்வரன் சிங் குழு).",
        rev_en="42nd Amendment Act 1976 = Mini-Constitution.",
        rev_ta="42வது திருத்தச் சட்டம் 1976 = குறு-அரசியலமைப்பு.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Remember", est_sec=30, pyq_sim="Direct PYQ", tags=["42nd Amendment", "Mini-Constitution", "Swaran Singh Committee"]
    ))

    # Q60 - TNPSC Trap - Medium - Ans B
    qs.append(make_q(
        q_id="SF_GT_060", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="TNPSC Trap",
        q_en="Which of the following features of the Indian Constitution is borrowed from the Constitution of South Africa?",
        q_ta="இந்திய அரசியலமைப்பின் பின்வரும் அம்சங்களில் எது தென்னாப்பிரிக்க அரசியலமைப்பிலிருந்து பெறப்பட்டது?",
        opts_en=[
            "Nomination of members to the Rajya Sabha and Directive Principles of State Policy",
            "Procedure for Amendment of the Constitution and Election of members of Rajya Sabha",
            "Joint sitting of the two Houses of Parliament and Concurrent List",
            "Advisory Jurisdiction of the Supreme Court and Residual Powers"
        ],
        opts_ta=[
            "மாநிலங்களவை உறுப்பினர்கள் நியமனம் மற்றும் அரசு நெறிமுறைப்படுத்தும் கோட்பாடுகள்",
            "அரசியலமைப்பு திருத்த நடைமுறை மற்றும் மாநிலங்களவை உறுப்பினர்கள் தேர்தல்",
            "நாடாளுமன்றத்தின் இரு அவைகளின் கூட்டு அமர்வு மற்றும் பொதுப் பட்டியல்",
            "உச்ச நீதிமன்றத்தின் ஆலோசனைக் அதிகார வரம்பு மற்றும் எஞ்சிய அதிகாரங்கள்"
        ],
        correct_ans="B",
        exp_en="Historical Context: The framing of the Constitution drew upon specific mechanisms from world constitutions.\nReason: South African Constitution provided: (1) Procedure for Amendment of Constitution under Article 368; (2) Election of members of Rajya Sabha by proportional representation.\nConstitutional Impact: Established structured democratic election for Rajya Sabha and formal amendment machinery.\nExam Trap: Nomination of RS members = Ireland; Election of RS members = South Africa.\nMemory Trick: South Africa = Amendment Procedure + RS Election.",
        exp_ta="வரலாற்றுப் பின்னணி: அரசியலமைப்பை உருவாக்குவது உலக அரசியலமைப்புகளிலிருந்து குறிப்பிட்ட வழிமுறைகளைப் பெற்றது.\nகாரணம்: தென்னாப்பிரிக்க அரசியலமைப்பு வழங்கியது: (1) உறுப்பு 368 இன் கீழ் அரசியலமைப்பு திருத்த நடைமுறை; (2) விகிதாச்சாரப் பிரதிநிதித்துவத்தின் மூலம் மாநிலங்களவை உறுப்பினர்கள் தேர்தல்.\nஅரசியலமைப்பு தாக்கம்: மாநிலங்களவைக்கான கட்டமைக்கப்பட்ட ஜனநாயகத் தேர்தலையும் முறைப்படியான திருத்த இயந்திரத்தையும் நிறுவியது.\nதேர்வுப் பொறி: மாநிலங்களவை உறுப்பினர் நியமனம் = அயர்லாந்து; மாநிலங்களவை உறுப்பினர் தேர்தல் = தென்னாப்பிரிக்கா.\nநினைவுச் சூத்திரம்: தென்னாப்பிரிக்கா = திருத்த நடைமுறை + மாநிலங்களவை தேர்தல்.",
        wno_dict={
            "A": {"en": "Incorrect. Nomination to RS and DPSP are borrowed from Ireland.", "ta": "தவறு. மாநிலங்களவை நியமனம் மற்றும் DPSP ஆகியவை அயர்லாந்திலிருந்து பெறப்பட்டவை."},
            "B": {"en": "Correct. Amendment procedure (Art 368) and Election of RS members are borrowed from South Africa.", "ta": "சரி. திருத்த நடைமுறை (உறுப்பு 368) மற்றும் மாநிலங்களவை உறுப்பினர் தேர்தல் ஆகியவை தென்னாப்பிரிக்காவிலிருந்து பெறப்பட்டவை."},
            "C": {"en": "Incorrect. Joint sitting and Concurrent List are borrowed from Australia.", "ta": "தவறு. கூட்டு அமர்வு மற்றும் பொதுப் பட்டியல் ஆகியவை ஆஸ்திரேலியாவிலிருந்து பெறப்பட்டவை."},
            "D": {"en": "Incorrect. Advisory jurisdiction and Residual powers are borrowed from Canada.", "ta": "தவறு. ஆலோசனைக் அதிகார வரம்பு மற்றும் எஞ்சிய அதிகாரங்கள் கனடாவிலிருந்து பெறப்பட்டவை."}
        },
        tip_en="TNPSC Trap: RS Nomination = Ireland; RS Election = South Africa. Amendment Procedure = South Africa.",
        tip_ta="TNPSC பொறி: மாநிலங்களவை நியமனம் = அயர்லாந்து; மாநிலங்களவை தேர்தல் = தென்னாப்பிரிக்கா. திருத்த நடைமுறை = தென்னாப்பிரிக்கா.",
        rev_en="South Africa borrowed features: Amendment procedure (Art 368) & Election of RS members.",
        rev_ta="தென்னாப்பிரிக்காவிலிருந்து பெறப்பட்ட அம்சங்கள்: திருத்த நடைமுறை (உறுப்பு 368) & மாநிலங்களவை உறுப்பினர் தேர்தல்.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Remember", est_sec=45, pyq_sim="High", tags=["Borrowed Features", "South Africa", "Rajya Sabha Election", "TNPSC Trap"]
    ))

    # Q61 - Conceptual - Hard - Ans C
    qs.append(make_q(
        q_id="SF_GT_061", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Hard", question_type="Conceptual",
        q_en="Why does the Indian Constitution adopt a 'Single Integrated Judiciary' instead of a Dual Judicial System like the United States?",
        q_ta="அமெரிக்காவைப் போன்ற இரட்டை நீதித்துறை அமைப்பிற்குப் பதிலாக இந்திய அரசியலமைப்பு ஏன் 'ஒற்றை ஒருங்கிணைந்த நீதித்துறையை' (Single Integrated Judiciary) ஏற்றுக்கொள்கிறது?",
        opts_en=[
            "To eliminate the Supreme Court's power of judicial review over state legislation.",
            "To ensure that state governments can appoint judges to High Courts without Central control.",
            "To maintain judicial uniformity and eliminate diversity in remedial procedures across Union and State laws.",
            "To merge lower courts into executive magistrate offices."
        ],
        opts_ta=[
            "மாநிலச் சட்டமன்றங்கள் மீதான உச்ச நீதிமன்றத்தின் நீதித்துறை மறுஆய்வு அதிகாரத்தை ஒழிக்க.",
            "மத்தியக் கட்டுப்பாடின்றி மாநில அரசுகள் உயர் நீதிமன்ற நீதிபதிகளை நியமிக்க முடியும் என்பதை உறுதிப்படுத்த.",
            "நீதித்துறை சீரான தன்மையைப் பேணவும், மத்திய மற்றும் மாநிலச் சட்டங்கள் முழுவதும் தீர்வு நடைமுறைகளில் உள்ள வேறுபாடுகளை ஒழிக்கவும்.",
            "கீழ் நீதிமன்றங்களை நிர்வாக நடுவர் அலுவலகங்களுடன் இணைக்க."
        ],
        correct_ans="C",
        exp_en="Historical Context: Dr. B.R. Ambedkar explicitly defended single integrated judiciary in the Constituent Assembly.\nReason: Ambedkar stated that dual judiciary in USA creates diversity in law and remedies. India adopted an integrated judiciary to eliminate diversity in legal standards and maintain judicial uniformity nationwide.\nConstitutional Impact: Ensures single supreme judicial authority for all laws (Central + State).\nExam Trap: Dual judiciary exists in USA; Single integrated judiciary exists in India.",
        exp_ta="வரலாற்றுப் பின்னணி: டாக்டர் பி.ஆர். அம்பேத்கர் அரசியலமைப்பு நிர்ணய சபையில் ஒற்றை ஒருங்கிணைந்த நீதித்துறையை வெளிப்படையாக ஆதரித்தார்.\nகாரணம்: அமெரிக்காவில் உள்ள இரட்டை நீதித்துறை சட்டம் மற்றும் தீர்வுகளில் வேறுபாட்டை உருவாக்குகிறது என்று அம்பேத்கர் கூறினார். சட்டத் தரங்களில் உள்ள வேறுபாடுகளை ஒழிப்பதற்கும் நாடு தழுவிய நீதித்துறை சீரான தன்மையைப் பேணுவதற்கும் இந்தியா ஒரு ஒருங்கிணைந்த நீதித்துறையை ஏற்றுக்கொண்டது.\nஅரசியலமைப்பு தாக்கம்: அனைத்து சட்டங்களுக்கும் (மத்திய + மாநில) ஒற்றை உச்ச நீதித்துறை அதிகாரத்தை உறுதி செய்கிறது.\nதேர்வுப் பொறி: அமெரிக்காவில் இரட்டை நீதித்துறை உள்ளது; இந்தியாவில் ஒற்றை ஒருங்கிணைந்த நீதித்துறை உள்ளது.",
        wno_dict={
            "A": {"en": "Incorrect. Integrated Judiciary strengthens SC judicial review over state laws.", "ta": "தவறு. ஒருங்கிணைந்த நீதித்துறை மாநில சட்டங்கள் மீதான உச்ச நீதிமன்ற நீதித்துறை மறுஆய்வை வலுப்படுத்துகிறது."},
            "B": {"en": "Incorrect. President appoints High Court judges (Central involvement).", "ta": "தவறு. குடியரசுத் தலைவர் உயர் நீதிமன்ற நீதிபதிகளை நியமிக்கிறார் (மத்திய ஈடுபாடு)."},
            "C": {"en": "Correct. Maintains judicial uniformity and eliminates legal diversity in remedies across Central and State laws (Ambedkar).", "ta": "சரி. மத்திய மற்றும் மாநில சட்டங்கள் முழுவதும் நீதித்துறை சீரான தன்மையைப் பேணுகிறது மற்றும் சட்ட வேறுபாடுகளை ஒழிக்கிறது (அம்பேத்கர்)."},
            "D": {"en": "Incorrect. Separation of judiciary from executive is mandated by Art 50.", "ta": "தவறு. நிர்வாகத்திலிருந்து நீதித்துறை பிரிப்பு உறுப்பு 50 ஆல் ஆணையிடப்பட்டுள்ளது."}
        },
        tip_en="TNPSC Tip: Single Integrated Judiciary = Uniformity in legal administration & enforcement of Central + State laws (Ambedkar).",
        tip_ta="TNPSC குறிப்பு: ஒற்றை ஒருங்கிணைந்த நீதித்துறை = சட்ட நிர்வாகத்தில் சீரான தன்மை & மத்திய + மாநில சட்டங்களின் அமலாக்கம் (அம்பேத்கர்).",
        rev_en="Integrated Judiciary: Ensures legal uniformity across Centre and States (Dr. Ambedkar).",
        rev_ta="ஒருங்கிணைந்த நீதித்துறை: மத்திய அரசு மற்றும் மாநிலங்களில் சட்ட சீரான தன்மையை உறுதி செய்கிறது (டாக்டர் அம்பேத்கர்).",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Understand", est_sec=60, pyq_sim="High", tags=["Integrated Judiciary", "Dr B.R. Ambedkar", "Judicial Uniformity"]
    ))

    # Q62 - Direct MCQ - Easy - Ans A
    qs.append(make_q(
        q_id="SF_GT_062", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Easy", question_type="Direct MCQ",
        q_en="Under which Article of the Constitution is the Union Public Service Commission (UPSC) required to present an annual report on its performance to the President?",
        q_ta="அரசியலமைப்பின் எந்த உறுப்பின் கீழ் மத்திய அரசுப் பணியாளர் தேர்வாணையம் (UPSC) தனது செயல்பாடுகள் குறித்த வருடாந்திர அறிக்கையைக் குடியரசுத் தலைவரிடம் சமர்ப்பிக்க வேண்டும்?",
        opts_en=[
            "Article 323",
            "Article 315",
            "Article 320",
            "Article 312"
        ],
        opts_ta=[
            "உறுப்பு 323",
            "உறுப்பு 315",
            "உறுப்பு 320",
            "உறுப்பு 312"
        ],
        correct_ans="A",
        exp_en="Historical Context: Annual reporting ensures legislative scrutiny over public service recruitment.\nReason: Under Article 323(1), UPSC presents annually to the President a report on the work done by the Commission. The President causes it to be laid before both Houses of Parliament.\nConstitutional Impact: Enforces democratic accountability of UPSC.\nExam Trap: Art 315 = Establishment of PSC; Art 320 = Functions of PSC; Art 323 = Reports of PSC.\nMemory Trick: Art 323 = Annual Report of PSC.",
        exp_ta="வரலாற்றுப் பின்னணி: வருடாந்திர அறிக்கை அளித்தல் பொதுப் பணி நியமனங்கள் மீது நாடாளுமன்றப் பரிசீலனையை உறுதி செய்கிறது.\nகாரணம்: உறுப்பு 323(1) இன் கீழ், UPSC ஆணைக்குழு செய்த பணிகள் குறித்த அறிக்கையை ஆண்டுதோறும் குடியரசுத் தலைவரிடம் சமர்ப்பிக்கிறது. குடியரசுத் தலைவர் அதை நாடாளுமன்றத்தின் இரு அவைகளின் முன்பும் சமர்ப்பிக்கச் செய்கிறார்.\nஅரசியலமைப்பு தாக்கம்: UPSC இன் ஜனநாயகப் பொறுப்புணர்வை நடைமுறைப்படுத்துகிறது.\nதேர்வுப் பொறி: உறுப்பு 315 = PSC உருவாக்கம்; உறுப்பு 320 = PSC செயல்பாடுகள்; உறுப்பு 323 = PSC அறிக்கைகள்.\nநினைவுச் சூத்திரம்: உறுப்பு 323 = PSC இன் வருடாந்திர அறிக்கை.",
        wno_dict={
            "A": {"en": "Correct. Article 323 deals with annual reports of Public Service Commissions.", "ta": "சரி. உறுப்பு 323 அரசுப் பணியாளர் தேர்வாணையங்களின் வருடாந்திர அறிக்கைகளைக் கையாள்கிறது."},
            "B": {"en": "Incorrect. Article 315 deals with Establishment of Public Service Commissions.", "ta": "தவறு. உறுப்பு 315 அரசுப் பணியாளர் தேர்வாணையங்களை நிறுவுவது பற்றியது."},
            "C": {"en": "Incorrect. Article 320 deals with Functions of Public Service Commissions.", "ta": "தவறு. உறுப்பு 320 அரசுப் பணியாளர் தேர்வாணையங்களின் செயல்பாடுகள் பற்றியது."},
            "D": {"en": "Incorrect. Article 312 deals with Creation of All-India Services.", "ta": "தவறு. உறுப்பு 312 அகில இந்திய பணிகளை உருவாக்குவது பற்றியது."}
        },
        tip_en="TNPSC Tip: Art 315 (Establishment), Art 320 (Functions), Art 323 (Annual Reports of UPSC/SPSC).",
        tip_ta="TNPSC குறிப்பு: உறுப்பு 315 (உருவாக்கம்), உறுப்பு 320 (செயல்பாடுகள்), உறுப்பு 323 (UPSC/SPSC வருடாந்திர அறிக்கைகள்).",
        rev_en="Article 323: Annual Reports of UPSC to President / SPSC to Governor.",
        rev_ta="உறுப்பு 323: குடியரசுத் தலைவரிடம் UPSC / ஆளுநரிடம் SPSC இன் வருடாந்திர அறிக்கைகள்.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Remember", est_sec=30, pyq_sim="High", tags=["UPSC", "Article 323", "Constitutional Bodies"]
    ))

    # Q63 - Statement-Based - Medium - Ans C
    qs.append(make_q(
        q_id="SF_GT_063", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="Statement-Based",
        q_en="Consider the following statements regarding the Emergency Provisions under Article 352:\n1. Proclamation of National Emergency must be approved by both Houses of Parliament within one month from the date of its issue.\n2. The resolution approving the emergency must be passed by a Special Majority in both Houses of Parliament.\n3. Once approved, the emergency continues for six months at a time, and can be extended indefinitely with parliamentary approval every six months.\n\nWhich of the statements given above are CORRECT?",
        q_ta="உறுப்பு 352 இன் கீழ் அவசரக்கால விதிகள் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. தேசிய அவசரநிலை அறிவிப்பு அது வெளியிடப்பட்ட தேதியிலிருந்து ஒரு மாதத்திற்குள் நாடாளுமன்றத்தின் இரு அவைகளாலும் அங்கீகரிக்கப்பட வேண்டும்.\n2. அவசரநிலையை அங்கீகரிக்கும் தீர்மானம் நாடாளுமன்றத்தின் இரு அவைகளிலும் சிறப்பு பெரும்பான்மையால் நிறைவேற்றப்பட வேண்டும்.\n3. அங்கீகரிக்கப்பட்டதும், அவசரநிலை ஒரு நேரத்தில் ஆறு மாதங்களுக்குத் தொடர்கிறது, மேலும் ஒவ்வொரு ஆறு மாதங்களுக்கும் நாடாளுமன்ற ஒப்புதலுடன் வரம்பின்றி நீட்டிக்கப்படலாம்.\n\nமேற்கூறிய கூற்றுகளில் எது சரியானவை?",
        opts_en=[
            "1 and 2 only",
            "2 and 3 only",
            "1, 2 and 3",
            "1 and 3 only"
        ],
        opts_ta=[
            "1 மற்றும் 2 மட்டும்",
            "2 மற்றும் 3 மட்டும்",
            "1, 2 மற்றும் 3",
            "1 மற்றும் 3 மட்டும்"
        ],
        correct_ans="C",
        exp_en="Historical Context: 44th Amendment 1978 introduced strict parliamentary safeguards for National Emergency approval.\nReason:\nStatement 1 is correct: Approved within 1 month (reduced from 2 months by 44th Amendment).\nStatement 2 is correct: Requires Special Majority (majority of total membership + 2/3rd present and voting).\nStatement 3 is correct: Continues for 6 months at a time, extendable indefinitely every 6 months.\nConstitutional Impact: Prevents indefinite executive emergency rule without parliamentary oversight.\nExam Trap: Art 352 = 1 month approval; Art 356 & Art 360 = 2 months approval.",
        exp_ta="வரலாற்றுப் பின்னணி: 44வது திருத்தம் 1978 தேசிய அவசரநிலை ஒப்புதலுக்காக கடுமையான நாடாளுமன்ற பாதுகாப்புகளை அறிமுகப்படுத்தியது.\nகாரணம்:\nகூற்று 1 சரி: 1 மாதத்திற்குள் அங்கீகரிக்கப்பட வேண்டும் (44வது திருத்தத்தால் 2 மாதங்களிலிருந்து குறைக்கப்பட்டது).\nகூற்று 2 சரி: சிறப்பு பெரும்பான்மை தேவை (மொத்த உறுப்பினர்களில் பெரும்பான்மை + 2/3 பங்கு வருகை தந்து வாக்களித்தல்).\nகூற்று 3 சரி: ஒரு நேரத்தில் 6 மாதங்களுக்கு தொடர்கிறது, ஒவ்வொரு 6 மாதங்களுக்கும் வரம்பின்றி நீட்டிக்கப்படலாம்.\nஅரசியலமைப்பு தாக்கம்: நாடாளுமன்ற மேற்பார்வையின்றி வரம்பற்ற நிர்வாக அவசரநிலை ஆட்சியைத் தடுக்கிறது.\nதேர்வுப் பொறி: உறுப்பு 352 = 1 மாத ஒப்புதல்; உறுப்பு 356 & உறுப்பு 360 = 2 மாத ஒப்புதல்.",
        wno_dict={
            "A": {"en": "Incorrect. Statement 3 is also correct.", "ta": "தவறு. கூற்று 3-ம் சரியானது."},
            "B": {"en": "Incorrect. Statement 1 is also correct.", "ta": "தவறு. கூற்று 1-ம் சரியானது."},
            "C": {"en": "Correct. All three statements 1, 2, and 3 are correct under Article 352 (44th Amendment 1978).", "ta": "சரி. உறுப்பு 352 இன் கீழ் (44வது திருத்தம் 1978) 1, 2 மற்றும் 3 ஆகிய மூன்று கூற்றுகளும் சரியானவை."},
            "D": {"en": "Incorrect. Statement 2 is also correct.", "ta": "தவறு. கூற்று 2-ம் சரியானது."}
        },
        tip_en="TNPSC Trap: Art 352 approval time = 1 Month (Special Majority). Art 356 & 360 approval time = 2 Months (Simple Majority).",
        tip_ta="TNPSC பொறி: உறுப்பு 352 ஒப்புதல் நேரம் = 1 மாதம் (சிறப்பு பெரும்பான்மை). உறுப்பு 356 & 360 ஒப்புதல் நேரம் = 2 மாதங்கள் (சாதாரண பெரும்பான்மை).",
        rev_en="Article 352 approval: 1 month, Special Majority, 6 months duration (extendable indefinitely).",
        rev_ta="உறுப்பு 352 ஒப்புதல்: 1 மாதம், சிறப்பு பெரும்பான்மை, 6 மாத காலம் (வரம்பின்றி நீட்டிக்கத்தக்கது).",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Analyze", est_sec=75, pyq_sim="High", tags=["National Emergency", "Article 352", "44th Amendment"]
    ))

    # Q64 - Direct MCQ - Easy - Ans B
    qs.append(make_q(
        q_id="SF_GT_064", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Easy", question_type="Direct MCQ",
        q_en="Which Schedule was added to the Indian Constitution by the 73rd Constitutional Amendment Act of 1992?",
        q_ta="1992 இன் 73வது அரசியலமைப்பு திருத்தச் சட்டத்தின் மூலம் இந்திய அரசியலமைப்பில் எந்த அட்டவணை சேர்க்கப்பட்டது?",
        opts_en=[
            "10th Schedule",
            "11th Schedule",
            "12th Schedule",
            "9th Schedule"
        ],
        opts_ta=[
            "10வது அட்டவணை",
            "11வது அட்டவணை",
            "12வது அட்டவணை",
            "9வது அட்டவணை"
        ],
        correct_ans="B",
        exp_en="Historical Context: Constitutional status for Panchayati Raj added a new functional schedule.\nReason: 73rd Amendment Act 1992 added the 11th Schedule containing 29 functional subjects for Panchayats.\nConstitutional Impact: Devolved administrative power to rural local bodies.\nExam Trap: 11th Schedule = Panchayats (29 subjects, 73rd Amendment); 12th Schedule = Municipalities (18 subjects, 74th Amendment).\nMemory Trick: 11th Sched = Panchayats; 12th Sched = Municipalities.",
        exp_ta="வரலாற்றுப் பின்னணி: பஞ்சாயத்து ராஜிற்கான அரசியலமைப்பு அந்தஸ்து ஒரு புதிய செயல்பாட்டு அட்டவணையைச் சேர்த்தது.\nகாரணம்: 73வது திருத்தச் சட்டம் 1992 பஞ்சாயத்துகளுக்கான 29 செயல்பாட்டுப் பொருட்களைக் கொண்ட 11வது அட்டவணையைச் சேர்த்தது.\nஅரசியலமைப்பு தாக்கம்: கிராமப்புற உள்ளாட்சி அமைப்புகளுக்கு நிர்வாக அதிகாரத்தைப் பகிர்ந்தளித்தது.\nதேர்வுப் பொறி: 11வது அட்டவணை = பஞ்சாயத்துகள் (29 பொருட்கள், 73வது திருத்தம்); 12வது அட்டவணை = நகராட்சிகள் (18 பொருட்கள், 74வது திருத்தம்).\nநினைவுச் சூத்திரம்: 11வது அட்டவணை = பஞ்சாயத்துகள்; 12வது அட்டவணை = நகராட்சிகள்.",
        wno_dict={
            "A": {"en": "Incorrect. 10th Schedule deals with Anti-Defection Law (added by 52nd Amendment 1985).", "ta": "தவறு. 10வது அட்டவணை கட்சித் தாவல் எதிர்ப்புச் சட்டம் பற்றியது (52வது திருத்தம் 1985 மூலம் சேர்க்கப்பட்டது)."},
            "B": {"en": "Correct. 11th Schedule added by 73rd Amendment 1992 for Panchayats (29 subjects).", "ta": "சரி. பஞ்சாயத்துகளுக்காக 73வது திருத்தம் 1992 மூலம் 11வது அட்டவணை சேர்க்கப்பட்டது (29 பொருட்கள்)."},
            "C": {"en": "Incorrect. 12th Schedule added by 74th Amendment 1992 for Municipalities (18 subjects).", "ta": "தவறு. 12வது அட்டவணை நகராட்சிகளுக்காக 74வது திருத்தம் 1992 மூலம் சேர்க்கப்பட்டது (18 பொருட்கள்)."},
            "D": {"en": "Incorrect. 9th Schedule added by 1st Amendment 1951 for land reform laws.", "ta": "தவறு. 9வது அட்டவணை நிலச் சீர்திருத்தச் சட்டங்களுக்காக 1வது திருத்தம் 1951 மூலம் சேர்க்கப்பட்டது."}
        },
        tip_en="TNPSC Tip: 11th Schedule = 73rd Amendment (Panchayats, 29 subjects). 12th Schedule = 74th Amendment (Municipalities, 18 subjects).",
        tip_ta="TNPSC குறிப்பு: 11வது அட்டவணை = 73வது திருத்தம் (பஞ்சாயத்துகள், 29 பொருட்கள்). 12வது அட்டவணை = 74வது திருத்தம் (நகராட்சிகள், 18 பொருட்கள்).",
        rev_en="11th Schedule: 73rd Amendment 1992, Panchayati Raj, 29 functional items.",
        rev_ta="11வது அட்டவணை: 73வது திருத்தம் 1992, பஞ்சாயத்து ராஜ், 29 செயல்பாட்டுப் பொருட்கள்.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Remember", est_sec=30, pyq_sim="High", tags=["11th Schedule", "73rd Amendment", "Panchayati Raj"]
    ))

    # Q65 - Conceptual - Medium - Ans A
    qs.append(make_q(
        q_id="SF_GT_065", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="Conceptual",
        q_en="What does the ideal of 'Social Justice' as declared in the Preamble and Directive Principles primarily mandate?",
        q_ta="முகவுரை மற்றும் நெறிமுறைக் கோட்பாடுகளில் அறிவிக்கப்பட்டுள்ளபடி 'சமூக நீதி' (Social Justice) என்ற லட்சியம் முதன்மையாக எதனை ஆணையிடுகிறது?",
        opts_en=[
            "Equal treatment of all citizens without any social distinction based on caste, color, race, religion, or sex, and elimination of social privileges.",
            "Distribution of free land to all voters in the country.",
            "Equal salary for all employees across private and public sectors regardless of qualification.",
            "Reserving 100% of all public posts exclusively for agrarian workers."
        ],
        opts_ta=[
            "சாதி, நிறம், இனக்குழு, மதம் அல்லது பாலினத்தின் அடிப்படையில் எந்தவொரு சமூகப் பாகுபாடுமின்றி அனைத்துக் குடிமக்களையும் சமமாக நடத்துதல் மற்றும் சமூகச் சலுகைகளை ஒழித்தல்.",
            "நாட்டில் உள்ள அனைத்து வாக்காளர்களுக்கும் இலவச நிலப் பகிர்வு.",
            "தகுதி பாராமல் தனியார் மற்றும் பொதுத்துறை நிறுவனங்களில் உள்ள அனைத்து ஊழியர்களுக்கும் சமமான சம்பளம்.",
            "அனைத்து பொதுப் பதவிகளிலும் 100% விவசாயத் தொழிலாளர்களுக்கு மட்டுமே இடஒதுக்கீடு."
        ],
        correct_ans="A",
        exp_en="Historical Context: Enshrined in Preamble (Justice - social, economic, and political) and operationalized via DPSPs (Art 38, 39, 46).\nReason: Social justice means equal treatment of all individuals without social distinctions based on caste, religion, sex, etc., along with improvement in the condition of backward classes (SCs, STs, OBCs) and women.\nConstitutional Impact: Forms the foundation of affirmative action and welfare measures in India.\nExam Trap: Social Justice is distinct from Economic Justice (wealth distribution) and Political Justice (equal voting rights).",
        exp_ta="வரலாற்றுப் பின்னணி: முகவுரையில் (நீதி - சமூக, பொருளாதார, அரசியல்) பொதிந்து DPSP-கள் மூலம் செயல்படுத்தப்படுகிறது (உறுப்புகள் 38, 39, 46).\nகாரணம்: சமூக நீதி என்பது சாதி, மதம், பாலினம் ஆகியவற்றின் அடிப்படையில் சமூகப் பாகுபாடுமின்றி அனைத்து நபர்களையும் சமமாக நடத்துவதையும், பிற்படுத்தப்பட்ட வகுப்பினரின் (SC, ST, OBC) மற்றும் பெண்களின் நிலையை மேம்படுத்துவதையும் குறிக்கிறது.\nஅரசியலமைப்பு தாக்கம்: இந்தியாவில் நேர்மறையான நடவடிக்கை மற்றும் நலன்புரி நடவடிக்கைகளின் அடித்தளத்தை அமைக்கிறது.\nதேர்வுப் பொறி: சமூக நீதி என்பது பொருளாதார நீதி (செல்வப் பகிர்வு) மற்றும் அரசியல் நீதி (சம வாக்களிப்பு உரிமைகள்) ஆகியவற்றிலிருந்து வேறுபட்டது.",
        wno_dict={
            "A": {"en": "Correct. Equal treatment without social distinction based on caste/religion/sex + elimination of privileges.", "ta": "சரி. சாதி/மதம்/பாலினத்தின் அடிப்படையில் சமூகப் பாகுபாடு இன்றி சமமாக நடத்துதல் + சலுகைகளை ஒழித்தல்."},
            "B": {"en": "Incorrect. Land redistribution is an economic measure, not the core definition of Social Justice.", "ta": "தவறு. நிலப் பகிர்வு ஒரு பொருளாதார நடவடிக்கை, சமூக நீதியின் மைய வரையறை அல்ல."},
            "C": {"en": "Incorrect. Equal salary for all irrespective of qualification is unrealistic and not Social Justice.", "ta": "தவறு. தகுதி பாராமல் சம சம்பளம் என்பது சமூக நீதி அல்ல."},
            "D": {"en": "Incorrect. 100% reservation for agrarian workers is constitutionally invalid.", "ta": "தவறு. விவசாயிகளுக்கு 100% இடஒதுக்கீடு அரசியலமைப்பு ரீதியாக செல்லாதது."}
        },
        tip_en="TNPSC Tip: Social Justice = Equal treatment without social distinction (caste, sex, religion) + uplifting backward classes.",
        tip_ta="TNPSC குறிப்பு: சமூக நீதி = சமூகப் பாகுபாடற்ற சமமான சிகிச்சை (சாதி, பாலினம், மதம்) + பிற்படுத்தப்பட்ட வகுப்பினரை உயர்த்துதல்.",
        rev_en="Social Justice: Non-discrimination based on caste/sex/religion + uplifting disadvantaged groups.",
        rev_ta="சமூக நீதி: சாதி/பாலினம்/மதத்தின் அடிப்படையிலான பாகுபாடின்மை + பிற்படுத்தப்பட்ட குழுக்களை உயர்த்துதல்.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Understand", est_sec=45, pyq_sim="High", tags=["Social Justice", "Preamble", "DPSP", "Welfare State"]
    ))

    # Q66 - PYQ Pattern - Hard - Ans D
    qs.append(make_q(
        q_id="SF_GT_066", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Hard", question_type="PYQ Pattern",
        q_en="Under Article 368, which of the following provisions requires ratification by the legislatures of NOT LESS THAN HALF of the States before being presented to the President for assent?",
        q_ta="உறுப்பு 368 இன் கீழ், பின்வரும் விதிகளில் எது ஒப்புதலுக்காகக் குடியரசுத் தலைவரிடம் சமர்ப்பிக்கப்படுவதற்கு முன்பு பாவாதிக்குக் குறையாத (NOT LESS THAN HALF) மாநிலங்களின் சட்டமன்றங்களால் அங்கீகரிக்கப்பட வேண்டும்?",
        opts_en=[
            "Abolition or creation of legislative councils in States (Article 169)",
            "Use of official language in Parliament",
            "Citizenship - acquisition and termination",
            "Election of the President and its manner (Articles 54 & 55) or Representation of States in Parliament"
        ],
        opts_ta=[
            "மாநிலங்களில் மேலவைகளை ஒழித்தல் அல்லது உருவாக்குதல் (உறுப்பு 169)",
            "நாடாளுமன்றத்தில் அதிகாரப்பூர்வ மொழியின் பயன்பாடு",
            "குடியுரிமை - பெறுதல் மற்றும் முடிவுக்கு வருதல்",
            "குடியரசுத் தலைவர் தேர்தல் மற்றும் அதன் முறை (உறுப்புகள் 54 & 55) அல்லது நாடாளுமன்றத்தில் மாநிலங்களின் பிரதிநிதித்துவம்"
        ],
        correct_ans="D",
        exp_en="Historical Context: Federal provisions under Article 368 require state consent to preserve federal balance.\nReason: Provisions affecting federal structure (Election of President Arts 54/55, Executive power of Union/States Arts 73/162, Supreme Court & High Courts, Distribution of legislative powers 7th Sched, Representation of States in Parliament, Art 368 itself) require Special Majority + Ratification by >= 50% State Legislatures by simple majority.\nConstitutional Impact: Protects state interests against unilateral federal changes.\nExam Trap: Options A, B, C can be amended by Simple Majority outside Art 368.",
        exp_ta="வரலாற்றுப் பின்னணி: உறுப்பு 368 இன் கீழ் உள்ள கூட்டாட்சி விதிகள் கூட்டாட்சி சமநிலையைப் பேண மாநில ஒப்புதலைக் கோருகின்றன.\nகாரணம்: கூட்டாட்சி அமைப்பைப் பாதிக்கும் விதிகள் (குடியரசுத் தலைவர் தேர்தல் உறுப்புகள் 54/55, மத்திய/மாநில நிர்வாக அதிகாரம் உறுப்புகள் 73/162, உச்ச நீதிமன்றம் & உயர் நீதிமன்றங்கள், 7வது அட்டவணை அதிகாரப் பகிர்வு, நாடாளுமன்றத்தில் மாநிலங்களின் பிரதிநிதித்துவம், உறுப்பு 368) சிறப்பு பெரும்பான்மை + >= 50% மாநில சட்டமன்றங்களின் சாதாரண பெரும்பான்மை ஒப்புதல் தேவை.\nஅரசியலமைப்பு தாக்கம்: ஒருதலைப்பட்ச மத்திய மாற்றங்களுக்கு எதிராக மாநில நலன்களைப் பாதுகாக்கிறது.\nதேர்வுப் பொறி: விருப்பங்கள் A, B, C ஆகியவற்றை உறுப்பு 368 க்கு வெளியே சாதாரண பெரும்பான்மையால் திருத்தலாம்.",
        wno_dict={
            "A": {"en": "Incorrect. Article 169 requires Simple Majority outside Art 368.", "ta": "தவறு. உறுப்பு 169 உறுப்பு 368 க்கு வெளியே சாதாரண பெரும்பான்மை கோருகிறது."},
            "B": {"en": "Incorrect. Official language use in Parliament requires Simple Majority.", "ta": "தவறு. நாடாளுமன்றத்தில் அதிகாரப்பூர்வ மொழி பயன்பாட்டிற்கு சாதாரண பெரும்பான்மை தேவை."},
            "C": {"en": "Incorrect. Citizenship rules require Simple Majority of Parliament.", "ta": "தவறு. குடியுரிமை விதிகளுக்கு நாடாளுமன்றத்தின் சாதாரண பெரும்பான்மை தேவை."},
            "D": {"en": "Correct. Presidential election (Arts 54/55) & State representation in Parliament require Special Majority + >= 50% State Ratification.", "ta": "சரி. குடியரசுத் தலைவர் தேர்தல் (உறுப்புகள் 54/55) & நாடாளுமன்றத்தில் மாநிலப் பிரதிநிதித்துவத்திற்கு சிறப்பு பெரும்பான்மை + >= 50% மாநில ஒப்புதல் தேவை."}
        },
        tip_en="TNPSC Tip: Federal structure amendments under Art 368 require Special Majority + 50% State Ratification (Presidential Election, 7th Sched, SC/HC, Art 368).",
        tip_ta="TNPSC குறிப்பு: உறுப்பு 368 இன் கீழ் கூட்டாட்சி கட்டமைப்பு திருத்தங்களுக்கு சிறப்பு பெரும்பான்மை + 50% மாநில ஒப்புதல் தேவை (குடியரசுத் தலைவர் தேர்தல், 7வது அட்டவணை, SC/HC, உறுப்பு 368).",
        rev_en="Article 368 Amendment type 2: Special Majority + 50% State Legislature Ratification for Federal provisions.",
        rev_ta="உறுப்பு 368 திருத்த வகை 2: கூட்டாட்சி விதிகளுக்கு சிறப்பு பெரும்பான்மை + 50% மாநில சட்டமன்ற ஒப்புதல்.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Analyze", est_sec=75, pyq_sim="High", tags=["Article 368", "Federal Structure", "State Ratification", "TNPSC Trap"]
    ))

    # Q67 - Statement-Based - Medium - Ans B
    qs.append(make_q(
        q_id="SF_GT_067", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="Statement-Based",
        q_en="Consider the following statements regarding the Election Commission of India (Article 324):\n1. The Chief Election Commissioner can be removed from office only in the like manner and on like grounds as a Judge of the Supreme Court.\n2. The service conditions of the Chief Election Commissioner cannot be varied to his disadvantage after his appointment.\n3. Other Election Commissioners can be removed from office by the President at any time without any recommendation from the Chief Election Commissioner.\n\nWhich of the statements given above are CORRECT?",
        q_ta="இந்தியத் தேர்தல் ஆணையம் (உறுப்பு 324) தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. தலைமைத் தேர்தல் ஆணையர் உச்ச நீதிமன்ற நீதிபதியை நீக்கும் அதே முறை மற்றும் காரணங்களின் அடிப்படையில் மட்டுமே பதவியிலிருந்து நீக்கப்பட முடியும்.\n2. தலைமைத் தேர்தல் ஆணையரின் சேவை நிபந்தனைகள் அவரது நியமனத்திற்குப் பிறகு அவருக்குப் பாதகமாக மாற்றப்பட முடியாது.\n3. மற்ற தேர்தல் ஆணையர்களை தலைமைத் தேர்தல் ஆணையரின் எந்தப் பரிந்துரையும் இன்றி குடியரசுத் தலைவர் எப்போது வேண்டுமானாலும் பதவியிலிருந்து நீக்கலாம்.\n\nமேற்கூறிய கூற்றுகளில் எது சரியானவை?",
        opts_en=[
            "1 and 3 only",
            "1 and 2 only",
            "2 and 3 only",
            "1, 2 and 3"
        ],
        opts_ta=[
            "1 மற்றும் 3 மட்டும்",
            "1 மற்றும் 2 மட்டும்",
            "2 மற்றும் 3 மட்டும்",
            "1, 2 மற்றும் 3"
        ],
        correct_ans="B",
        exp_en="Historical Context: Constitutional safeguards ensure independent conduct of elections in India.\nReason:\nStatement 1 is correct: Security of tenure guaranteed under Art 324(5) (removed like SC judge).\nStatement 2 is correct: Service conditions cannot be varied to his disadvantage.\nStatement 3 is INCORRECT: Article 324(5) explicitly states that other Election Commissioners can be removed ONLY on the recommendation of the Chief Election Commissioner.\nConstitutional Impact: Protects election commission members from executive pressure.",
        exp_ta="வரலாற்றுப் பின்னணி: அரசியலமைப்பு பாதுகாப்புகள் இந்தியாவில் சுதந்திரமாக தேர்தலை நடத்துவதை உறுதி செய்கின்றன.\nகாரணம்:\nகூற்று 1 சரி: உறுப்பு 324(5) இன் கீழ் பதவிக் கால பாதுகாப்பு உத்தரவாதம் அளிக்கப்பட்டுள்ளது (உச்ச நீதிமன்ற நீதிபதியைப் போல நீக்கம்).\nகூற்று 2 சரி: சேவை நிபந்தனைகள் நியமனத்திற்குப் பிறகு அவருக்குப் பாதகமாக மாற்றப்பட முடியாது.\nகூற்று 3 தவறு: தலைமைத் தேர்தல் ஆணையரின் பரிந்துரையின் பேரில் மட்டுமே மற்ற தேர்தல் ஆணையர்கள் நீக்கப்பட முடியும் என்று உறுப்பு 324(5) வெளிப்படையாகக் கூறுகிறது.\nஅரசியலமைப்பு தாக்கம்: தேர்தல் ஆணைய உறுப்பினர்களை நிர்வாக அழுத்தத்திலிருந்து பாதுகாக்கிறது.",
        wno_dict={
            "A": {"en": "Incorrect. Statement 3 is false (CEC recommendation is required).", "ta": "தவறு. கூற்று 3 தவறு (CEC பரிந்துரை தேவை)."},
            "B": {"en": "Correct. Statements 1 and 2 are correct; Statement 3 is false under Article 324(5).", "ta": "சரி. கூற்றுகள் 1 மற்றும் 2 சரி; உறுப்பு 324(5) இன் கீழ் கூற்று 3 தவறு."},
            "C": {"en": "Incorrect. Statement 3 is false.", "ta": "தவறு. கூற்று 3 தவறு."},
            "D": {"en": "Incorrect. Statement 3 is false.", "ta": "தவறு. கூற்று 3 தவறு."}
        },
        tip_en="TNPSC Trap: Other Election Commissioners CANNOT be removed except on the recommendation of the Chief Election Commissioner.",
        tip_ta="TNPSC பொறி: தலைமைத் தேர்தல் ஆணையரின் பரிந்துரை தவிர மற்ற தேர்தல் ஆணையர்களை நீக்க முடியாது.",
        rev_en="Article 324: CEC removed like SC Judge; Other ECs removed ONLY on recommendation of CEC.",
        rev_ta="உறுப்பு 324: CEC உச்ச நீதிமன்ற நீதிபதியைப் போல நீக்கப்படுவார்; மற்ற ECகள் CEC பரிந்துரையின் பேரில் மட்டுமே நீக்கப்படுவர்.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Analyze", est_sec=60, pyq_sim="High", tags=["Election Commission", "Article 324", "Constitutional Bodies", "TNPSC Trap"]
    ))

    # Q68 - Conceptual - Hard - Ans A
    qs.append(make_q(
        q_id="SF_GT_068", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Hard", question_type="Conceptual",
        q_en="How does the Indian Constitution accommodate 'Linguistic and Regional Diversity' within a unified Constitutional Framework?",
        q_ta="ஒருங்கிணைந்த அரசியலமைப்பு அமைப்பிற்குள் இந்திய அரசியலமைப்பு 'மொழி மற்றும் பிராந்திய பன்முகத்தன்மையை' எவ்வாறு உள்ளடக்கியுள்ளது?",
        opts_en=[
            "By establishing the 8th Schedule for official recognition of languages and special provisions for specific states under Articles 371 to 371J.",
            "By enforcing Hindi as the sole compulsory medium of instruction across all states.",
            "By granting absolute sovereignty to state assemblies to secede if cultural rights are breached.",
            "By prohibiting states from conducting administrative business in regional languages."
        ],
        opts_ta=[
            "மொழிகளுக்கு அதிகாரப்பூர்வ அங்கீகாரம் அளிப்பதற்காக 8வது அட்டவணையை நிறுவுதல் மற்றும் உறுப்புகள் 371 முதல் 371J வரை குறிப்பிட்ட மாநிலங்களுக்கு சிறப்பு விதிகளை வழங்குதல் மூலம்.",
            "அனைத்து மாநிலங்களிலும் ஹிந்தியை ஒரே கட்டாய பயிற்று மொழியாக அமல்படுத்துவதன் மூலம்.",
            "கலாச்சார உரிமைகள் மீறப்பட்டால் மாநில சட்டமன்றங்களுக்குப் பிரியும் முழுமையான இறையாண்மையை வழங்குவதன் மூலம்.",
            "மாநிலங்கள் பிராந்திய மொழிகளில் நிர்வாக நடவடிக்கைகளை மேற்கொள்வதைத் தடுப்பதன் மூலம்."
        ],
        correct_ans="A",
        exp_en="Historical Context: Unity in Diversity is a fundamental ethos of the Indian Constitution.\nReason: The Constitution accommodates linguistic diversity through the 8th Schedule (currently 22 recognized languages) and protects regional autonomy via special provisions under Articles 371 to 371J for Maharashtra, Gujarat, Nagaland, Assam, Manipur, Andhra Pradesh, Telangana, Sikkim, Mizoram, Arunachal Pradesh, Goa, and Karnataka.\nConstitutional Impact: Fosters national integration while respecting regional aspirations.\nExam Trap: 8th Schedule originally contained 14 languages; currently contains 22 languages.",
        exp_ta="வரலாற்றுப் பின்னணி: வேற்றுமையில் ஒற்றுமை என்பது இந்திய அரசியலமைப்பின் அடிப்படை கருத்தாகும்.\nகாரணம்: அரசியலமைப்பு 8வது அட்டவணை (தற்போது 22 அங்கீகரிக்கப்பட்ட மொழிகள்) மூலம் மொழிப் பன்முகத்தன்மையை உள்ளடக்கியுள்ளது மற்றும் மகாராஷ்டிரா, குஜராத், நாகாலாந்து, அசாம், மணிப்பூர், ஆந்திரப் பிரதேசம், தெலுங்கானா, சிக்கிம், மிசோரம், அருணாச்சலப் பிரதேசம், கோவா மற்றும் கர்நாடகா ஆகிய மாநிலங்களுக்கான உறுப்புகள் 371 முதல் 371J வரையிலான சிறப்பு விதிகள் மூலம் பிராந்திய சுயாட்சியைப் பாதுகாக்கிறது.\nஅரசியலமைப்பு தாக்கம்: பிராந்திய விருப்பங்களை மதிக்கும் அதே வேளையில் தேசிய ஒருமைப்பாட்டை வளர்க்கிறது.\nதேர்வுப் பொறி: 8வது அட்டவணையில் ஆரம்பத்தில் 14 மொழிகள் இருந்தன; தற்போது 22 மொழிகள் உள்ளன.",
        wno_dict={
            "A": {"en": "Correct. 8th Schedule (22 languages) + Special provisions under Arts 371 to 371J for regional diversity.", "ta": "சரி. 8வது அட்டவணை (22 மொழிகள்) + பிராந்திய பன்முகத்தன்மைக்கான உறுப்புகள் 371 முதல் 371J வரையிலான சிறப்பு விதிகள்."},
            "B": {"en": "Incorrect. Hindi is not the sole compulsory medium enforced nationwide.", "ta": "தவறு. நாடு முழுவதும் ஹிந்தி மட்டுமே கட்டாய பயிற்று மொழியாக அமல்படுத்தப்படவில்லை."},
            "C": {"en": "Incorrect. States have no right to secede.", "ta": "தவறு. மாநிலங்களுக்குப் பிரியும் உரிமை இல்லை."},
            "D": {"en": "Incorrect. Article 345 permits states to use regional languages for official administration.", "ta": "தவறு. உறுப்பு 345 மாநிலங்கள் அதிகாரப்பூர்வ நிர்வாகத்திற்கு பிராந்திய மொழிகளைப் பயன்படுத்த அனுமதிக்கிறது."}
        },
        tip_en="TNPSC Tip: 8th Schedule = 22 recognized languages (originally 14). Articles 371 to 371J = Special provisions for 12 states.",
        tip_ta="TNPSC குறிப்பு: 8வது அட்டவணை = 22 அங்கீகரிக்கப்பட்ட மொழிகள் (ஆரம்பத்தில் 14). உறுப்புகள் 371 முதல் 371J = 12 மாநிலங்களுக்கான சிறப்பு விதிகள்.",
        rev_en="Accommodation of Diversity: 8th Schedule (22 Languages) & Articles 371-371J (Special State Provisions).",
        rev_ta="பன்முகத்தன்மையை உள்ளடக்குதல்: 8வது அட்டவணை (22 மொழிகள்) & உறுப்புகள் 371-371J (சிறப்பு மாநில விதிகள்).",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Understand", est_sec=60, pyq_sim="High", tags=["8th Schedule", "Article 371", "Unity in Diversity"]
    ))

    # Q69 - Direct MCQ - Easy - Ans B
    qs.append(make_q(
        q_id="SF_GT_069", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Easy", question_type="Direct MCQ",
        q_en="Under Article 51A(a) of the Constitution, every citizen is duty-bound to abide by the Constitution and respect its ideals and institutions, the National Flag, and the:",
        q_ta="அரசியலமைப்பின் உறுப்பு 51A(a) இன் கீழ், ஒவ்வொரு குடிமகனும் அரசியலமைப்பிற்குக் கட்டுப்பட்டு அதன் லட்சியங்கள் மற்றும் நிறுவனங்கள், தேசியக் கொடி மற்றும் எதனை மதிக்கக் கடமைப்பட்டுள்ளனர்?",
        opts_en=[
            "National Bird",
            "National Anthem",
            "National Animal",
            "National Flower"
        ],
        opts_ta=[
            "தேசியப் பறவை",
            "தேசிய கீதம்",
            "தேசிய விலங்கு",
            "தேசிய மலர்"
        ],
        correct_ans="B",
        exp_en="Historical Context: The first Fundamental Duty under Article 51A(a) specifies core national symbols.\nReason: Article 51A(a) states: 'To abide by the Constitution and respect its ideals and institutions, the National Flag and the National Anthem'.\nConstitutional Impact: Instills civic reverence for sovereign national symbols.\nExam Trap: Article 51A(a) mentions National Flag and National Anthem, but does NOT explicitly mention National Song (Vande Mataram).\nMemory Trick: Art 51A(a) = Constitution + Flag + Anthem.",
        exp_ta="வரலாற்றுப் பின்னணி: உறுப்பு 51A(a) இன் கீழ் உள்ள முதல் அடிப்படை கடமை முக்கிய தேசிய சின்னங்களைக் குறிப்பிடுகிறது.\nகாரணம்: உறுப்பு 51A(a) கூறுகிறது: 'அரசியலமைப்பிற்குக் கட்டுப்பட்டு நடக்க வேண்டும், அதன் லட்சியங்கள் மற்றும் நிறுவனங்கள், தேசியக் கொடி மற்றும் தேசிய கீதத்தை மதிக்க வேண்டும்'.\nஅரசியலமைப்பு தாக்கம்: இறையாண்மை கொண்ட தேசிய சின்னங்கள் மீது குடிமை மரியாதையை ஏற்படுத்துகிறது.\nதேர்வுப் பொறி: உறுப்பு 51A(a) தேசியக் கொடி மற்றும் தேசிய கீதத்தைக் குறிப்பிடுகிறது, ஆனால் தேசியப் பாடலை (வந்தே மாதரம்) வெளிப்படையாகக் குறிப்பிடவில்லை.\nநினைவுச் சூத்திரம்: உறுப்பு 51A(a) = அரசியலமைப்பு + கொடி + கீதம்.",
        wno_dict={
            "A": {"en": "Incorrect. National Bird is not mentioned in Art 51A(a).", "ta": "தவறு. தேசியப் பறவை உறுப்பு 51A(a) இல் குறிப்பிடப்படவில்லை."},
            "B": {"en": "Correct. Article 51A(a) specifies National Flag and National Anthem.", "ta": "சரி. உறுப்பு 51A(a) தேசியக் கொடி மற்றும் தேசிய கீதத்தைக் குறிப்பிடுகிறது."},
            "C": {"en": "Incorrect. National Animal is protected under Art 51A(g) generally as wildlife.", "ta": "தவறு. தேசிய விலங்கு பொதுவாக 51A(g) இன் கீழ் வனவிலங்காகப் பாதுகாக்கப்படுகிறது."},
            "D": {"en": "Incorrect. National Flower is not mentioned in Art 51A(a).", "ta": "தவறு. தேசிய மலர் உறுப்பு 51A(a) இல் குறிப்பிடப்படவில்லை."}
        },
        tip_en="TNPSC Trap: Art 51A(a) mentions National Anthem, NOT National Song (Vande Mataram).",
        tip_ta="TNPSC பொறி: உறுப்பு 51A(a) தேசிய கீதத்தைக் குறிப்பிடுகிறது, தேசியப் பாடலை (வந்தே மாதரம்) அல்ல.",
        rev_en="Article 51A(a): Abide by Constitution, respect National Flag and National Anthem.",
        rev_ta="உறுப்பு 51A(a): அரசியலமைப்பிற்குக் கட்டுப்படுதல், தேசியக் கொடி மற்றும் தேசிய கீதத்தை மதித்தல்.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Remember", est_sec=30, pyq_sim="High", tags=["Fundamental Duties", "Article 51A", "National Anthem", "TNPSC Trap"]
    ))

    # Q70 - Statement-Based - Hard - Ans C
    qs.append(make_q(
        q_id="SF_GT_070", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Hard", question_type="Statement-Based",
        q_en="Consider the following statements regarding the Attorney General of India (Article 76):\n1. The Attorney General is appointed by the President of India and must be qualified to be appointed a Judge of the Supreme Court.\n2. The Attorney General has the right of audience in all courts in the territory of India.\n3. The Attorney General has the right to speak and take part in the proceedings of both Houses of Parliament, including the right to vote.\n\nWhich of the statements given above are CORRECT?",
        q_ta="இந்திய தலைமை வழக்குரைஞர் (Attorney General - உறுப்பு 76) தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இந்திய தலைமை வழக்குரைஞர் இந்தியக் குடியரசுத் தலைவரால் நியமிக்கப்படுகிறார் மற்றும் உச்ச நீதிமன்ற நீதிபதியாக நியமிக்கப்படத் தகுதியுடையவராக இருக்க வேண்டும்.\n2. இந்திய தலைமை வழக்குரைஞருக்கு இந்திய எல்லைக்குள் உள்ள அனைத்து நீதிமன்றங்களிலும் வழக்குகளை விசாரிக்கும் உரிமை உண்டு.\n3. இந்திய தலைமை வழக்குரைஞருக்கு நாடாளுமன்றத்தின் இரு அவைகளின் நடவடிக்கைகளிலும் பேசவும் பங்கேற்கவும் உரிமை உண்டு, வாக்களிக்கும் உரிமை உட்பட.\n\nமேற்கூறிய கூற்றுகளில் எது சரியானவை?",
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
        exp_en="Historical Context: Attorney General is the highest law officer in the country under Article 76.\nReason:\nStatement 1 is correct: Appointed by President, must be qualified to be SC judge (Art 76(1)).\nStatement 2 is correct: Right of audience in all courts in India (Art 76(3)).\nStatement 3 is INCORRECT: Article 88 gives AG the right to speak and take part in parliamentary proceedings, but explicitly WITHOUT the right to vote.\nConstitutional Impact: Ensures legal advice to Union Government in legislative and judicial forums.\nExam Trap: AG can speak in Parliament, but CANNOT vote.",
        exp_ta="வரலாற்றுப் பின்னணி: தலைமை வழக்குரைஞர் உறுப்பு 76 இன் கீழ் நாட்டின் மிக உயர்ந்த சட்ட அதிகாரி ஆவார்.\nகாரணம்:\nகூற்று 1 சரி: குடியரசுத் தலைவரால் நியமிக்கப்படுகிறார், உச்ச நீதிமன்ற நீதிபதியாகத் தகுதி பெற வேண்டும் (உறுப்பு 76(1)).\nகூற்று 2 சரி: இந்தியாவில் உள்ள அனைத்து நீதிமன்றங்களிலும் பார்வையாளராக இருக்கும் உரிமை உண்டு (உறுப்பு 76(3)).\nகூற்று 3 தவறு: உறுப்பு 88 AG-க்கு நாடாளுமன்ற நடவடிக்கைகளில் பேசவும் பங்கேற்கவும் உரிமை அளிக்கிறது, ஆனால் வாக்களிக்கும் உரிமை இன்றி வெளிப்படையாகத் தடுக்கிறது.\nஅரசியலமைப்பு தாக்கம்: சட்டமன்ற மற்றும் நீதித்துறை மன்றங்களில் மத்திய அரசுக்கு சட்ட ஆலோசனையை உறுதி செய்கிறது.\nதேர்வுப் பொறி: AG நாடாளுமன்றத்தில் பேசலாம், ஆனால் வாக்களிக்க முடியாது.",
        wno_dict={
            "A": {"en": "Incorrect. Statement 3 is false under Article 88 (AG has no voting right).", "ta": "தவறு. உறுப்பு 88 இன் கீழ் கூற்று 3 தவறு (AG-க்கு வாக்களிக்கும் உரிமை இல்லை)."},
            "B": {"en": "Incorrect. Statement 3 is false.", "ta": "தவறு. கூற்று 3 தவறு."},
            "C": {"en": "Correct. Statements 1 and 2 are correct; Statement 3 is false.", "ta": "சரி. கூற்றுகள் 1 மற்றும் 2 சரி; கூற்று 3 தவறு."},
            "D": {"en": "Incorrect. Statement 3 is false.", "ta": "தவறு. கூற்று 3 தவறு."}
        },
        tip_en="TNPSC Trap: Article 88: Attorney General has right to speak in Parliament, but WITHOUT the right to vote.",
        tip_ta="TNPSC குறிப்பு: உறுப்பு 88: தலைமை வழக்குரைஞருக்கு நாடாளுமன்றத்தில் பேச உரிமை உண்டு, ஆனால் வாக்களிக்கும் உரிமை இல்லை.",
        rev_en="Attorney General (Art 76): Highest law officer; right to speak in Parliament (Art 88) but NO voting right.",
        rev_ta="தலைமை வழக்குரைஞர் (உறுப்பு 76): மிக உயர்ந்த சட்ட அதிகாரி; நாடாளுமன்றத்தில் பேச உரிமை (உறுப்பு 88) ஆனால் வாக்களிக்கும் உரிமை இல்லை.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Analyze", est_sec=60, pyq_sim="High", tags=["Attorney General", "Article 76", "Article 88", "TNPSC Trap"]
    ))

    # Q71 - Match the Following - Medium - Ans D
    qs.append(make_q(
        q_id="SF_GT_071", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="Match the Following",
        q_en="Match List-I (Prerogative Writ) with List-II (Literal Meaning) and select the correct answer:\n\nList-I:\n(a) Habeas Corpus\n(b) Mandamus\n(c) Quo-Warranto\n(d) Certiorari\n\nList-II:\n1. By what authority or warrant?\n2. To be certified or informed\n3. You may have the body of\n4. We command",
        q_ta="பட்டியல்-I (பேராணை) பட்டியல்-II (நேரடிப் பொருள்) உடன் பொருத்தி சரியான பதிலதைத் தேர்ந்தெடுக்கவும்:\n\nபட்டியல்-I:\n(a) ஆட்கொணர் பேராணை (Habeas Corpus)\n(b) கட்டளையுறுத்தும் பேராணை (Mandamus)\n(c) தகுதி வினவு பேராணை (Quo-Warranto)\n(d) ஆவணக் கேட்பு பேராணை (Certiorari)\n\nபட்டியல்-II:\n1. எந்த அதிகாரத்தின் கீழ் அல்லது ஆணை மூலம்?\n2. சான்றளிக்கப்பட வேண்டும் அல்லது தெரிவிக்கப்பட வேண்டும்\n3. உடலைக் கொண்டு வரலாம்\n4. நாம் ஆணையிடுகிறோம்",
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
        exp_en="Historical Context: Borrowed from English Law where writs were known as 'Prerogative Writs' issued under Articles 32 (SC) and 226 (HC).\nReason:\n(a) Habeas Corpus = To have the body of (3)\n(b) Mandamus = We command (4)\n(c) Quo-Warranto = By what authority or warrant? (1)\n(d) Certiorari = To be certified or to be informed (2)\nMatching: (a)-3, (b)-4, (c)-1, (d)-2.",
        exp_ta="வரலாற்றுப் பின்னணி: ஆங்கிலச் சட்டத்திலிருந்து பெறப்பட்டது, அங்கு பேராணைகள் 'பிரத்யேக பேராணைகள்' என வழங்கப்பட்டு உறுப்புகள் 32 (உச்ச நீதிமன்றம்) மற்றும் 226 (உயர் நீதிமன்றம்) இன் கீழ் வெளியிடப்படுகின்றன.\nகாரணம்:\n(a) ஆட்கொணர் பேராணை = உடலைக் கொண்டு வரலாம் (3)\n(b) கட்டளையுறுத்தும் பேராணை = நாம் ஆணையிடுகிறோம் (4)\n(c) தகுதி வினவு பேராணை = எந்த அதிகாரத்தின் கீழ்? (1)\n(d) ஆவணக் கேட்பு பேராணை = சான்றளிக்கப்பட வேண்டும் அல்லது தெரிவிக்கப்பட வேண்டும் (2)\nபொருத்துதல்: (a)-3, (b)-4, (c)-1, (d)-2.",
        wno_dict={
            "A": {"en": "Incorrect. Mandamus means 'We command' (4), not 'By what authority' (1).", "ta": "தவறு. Mandamus என்றால் 'நாம் ஆணையிடுகிறோம்' (4), 'எந்த அதிகாரத்தின் கீழ்' (1) அல்ல."},
            "B": {"en": "Incorrect. Habeas Corpus means 'You may have the body of' (3), not 'We command' (4).", "ta": "தவறு. Habeas Corpus என்றால் 'உடலைக் கொண்டு வரலாம்' (3), 'நாம் ஆணையிடுகிறோம்' (4) அல்ல."},
            "C": {"en": "Incorrect. Quo-Warranto is 1, Certiorari is 2.", "ta": "தவறு. Quo-Warranto என்பது 1, Certiorari என்பது 2."},
            "D": {"en": "Correct. All four writs matched with their exact Latin literal meanings.", "ta": "சரி. நான்கு பேராணைகளும் அவற்றின் துல்லியமான இலத்தீன் நேரடிப் பொருள்களுடன் பொருந்தியுள்ளன."}
        },
        tip_en="TNPSC Tip: Writs literal meanings: Habeas Corpus (To have body of), Mandamus (We command), Prohibition (To forbid), Certiorari (To be certified), Quo-Warranto (By what authority).",
        tip_ta="TNPSC குறிப்பு: பேராணைகளின் நேரடிப் பொருள்கள்: Habeas Corpus (உடலைக் கொண்டு வருதல்), Mandamus (ஆணையிடுதல்), Prohibition (தடுத்தல்), Certiorari (சான்றளித்தல்), Quo-Warranto (எந்த அதிகாரத்தின் கீழ்).",
        rev_en="Prerogative Writs (Articles 32 & 226): Borrowed from UK Law.",
        rev_ta="பிரத்யேக பேராணைகள் (உறுப்புகள் 32 & 226): இங்கிலாந்து சட்டத்திலிருந்து பெறப்பட்டவை.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Remember", est_sec=45, pyq_sim="High", tags=["Writs", "Article 32", "Article 226", "Match the Following"]
    ))

    # Q72 - PYQ Pattern - Easy - Ans A
    qs.append(make_q(
        q_id="SF_GT_072", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Easy", question_type="PYQ Pattern",
        q_en="Which Schedule of the Indian Constitution contains the Division of Powers between the Union and the States into three lists (Union List, State List, and Concurrent List)?",
        q_ta="இந்திய அரசியலமைப்பின் எந்த அட்டவணை மத்திய அரசுக்கும் மாநிலங்களுக்கும் இடையே அதிகாரப் பகிர்வை மூன்று பட்டியல்களாக (மத்தியப் பட்டியல், மாநிலப் பட்டியல், பொதுப் பட்டியல்) கொண்டுள்ளது?",
        opts_en=[
            "Seventh Schedule",
            "Eighth Schedule",
            "Sixth Schedule",
            "Fifth Schedule"
        ],
        opts_ta=[
            "ஏழாவது அட்டவணை",
            "எட்டாவது அட்டவணை",
            "ஆறாவது அட்டவணை",
            "ஐந்தாவது அட்டவணை"
        ],
        correct_ans="A",
        exp_en="Historical Context: Legislative division of powers under Article 246 is organized in the Seventh Schedule.\nReason: Seventh Schedule specifies List I (Union List - 100 subjects), List II (State List - 61 subjects), and List III (Concurrent List - 52 subjects).\nConstitutional Impact: Core mechanism for federal legislative division of powers.\nExam Trap: Originally: Union List (97), State List (66), Concurrent List (47). Present: Union List (100), State List (61), Concurrent List (52).\nMemory Trick: 7th Schedule = 7 Days in Week = 3 Lists Division.",
        exp_ta="வரலாற்றுப் பின்னணி: உறுப்பு 246 இன் கீழ் சட்ட அதிகாரப் பகிர்வு ஏழாவது அட்டவணையில் ஒழுங்கமைக்கப்பட்டுள்ளது.\nகாரணம்: ஏழாவது அட்டவணை பட்டியல் I (மத்தியப் பட்டியல் - 100 பொருட்கள்), பட்டியல் II (மாநிலப் பட்டியல் - 61 பொருட்கள்) மற்றும் பட்டியல் III (பொதுப் பட்டியல் - 52 பொருட்கள்) ஆகியவற்றைக் குறிப்பிடுகிறது.\nஅரசியலமைப்பு தாக்கம்: கூட்டாட்சி சட்ட அதிகாரப் பகிர்விற்கான முக்கிய பொறிமுறை.\nதேர்வுப் பொறி: ஆரம்பத்தில்: மத்தியப் பட்டியல் (97), மாநிலப் பட்டியல் (66), பொதுப் பட்டியல் (47). தற்போது: மத்தியப் பட்டியல் (100), மாநிலப் பட்டியல் (61), பொதுப் பட்டியல் (52).\nநினைவுச் சூத்திரம்: 7வது அட்டவணை = 3 பட்டியல்கள் பகிர்வு.",
        wno_dict={
            "A": {"en": "Correct. Seventh Schedule contains Union, State, and Concurrent Lists under Article 246.", "ta": "சரி. ஏழாவது அட்டவணை உறுப்பு 246 இன் கீழ் மத்திய, மாநில மற்றும் பொதுப் பட்டியல்களைக் கொண்டுள்ளது."},
            "B": {"en": "Incorrect. Eighth Schedule deals with recognized Languages.", "ta": "தவறு. எட்டாவது அட்டவணை அங்கீகரிக்கப்பட்ட மொழிகள் பற்றியது."},
            "C": {"en": "Incorrect. Sixth Schedule deals with Tribal Areas in Assam, Meghalaya, Tripura, Mizoram.", "ta": "தவறு. ஆறாவது அட்டவணை அசாம், மேகலாயா, திரிபுரா, மிசோரமில் உள்ள பழங்குடியின பகுதிகள் பற்றியது."},
            "D": {"en": "Incorrect. Fifth Schedule deals with Scheduled Areas and Scheduled Tribes.", "ta": "தவறு. ஐந்தாவது அட்டவணை பட்டியல் பகுதிகள் மற்றும் பட்டியல் பழங்குடியினர் பற்றியது."}
        },
        tip_en="TNPSC Tip: 7th Schedule = Legislative Lists (Union, State, Concurrent). Originally 97/66/47; Presently 100/61/52 subjects.",
        tip_ta="TNPSC குறிப்பு: 7வது அட்டவணை = சட்டப் பட்டியல்கள் (மத்திய, மாநில, பொது). ஆரம்பத்தில் 97/66/47; தற்போது 100/61/52 பொருட்கள்.",
        rev_en="Seventh Schedule: Article 246 (Union List, State List, Concurrent List).",
        rev_ta="ஏழாவது அட்டவணை: உறுப்பு 246 (மத்தியப் பட்டியல், மாநிலப் பட்டியல், பொதுப் பட்டியல்).",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Remember", est_sec=30, pyq_sim="Direct PYQ", tags=["Seventh Schedule", "Division of Powers", "Article 246"]
    ))

    # Q73 - Conceptual - Medium - Ans B
    qs.append(make_q(
        q_id="SF_GT_073", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="Conceptual",
        q_en="Why are Residuary Powers of legislation vested in the Union Parliament rather than the States in India?",
        q_ta="இந்தியாவில் சட்டமியற்றும் எஞ்சிய அதிகாரங்கள் (Residuary Powers) மாநிலங்களுக்குப் பதிலாக ஏன் மத்திய நாடாளுமன்றத்திற்கு வழங்கப்பட்டுள்ளன?",
        opts_en=[
            "To imitate the Swiss canton system of local governance.",
            "To maintain a strong Centre and ensure national unity, borrowed from the Canadian Constitution.",
            "Because the Supreme Court recommended it in the Shankari Prasad case.",
            "To comply with requirements of the League of Nations."
        ],
        opts_ta=[
            "சுவிஸ் கான்டன் உள்ளாட்சி அமைப்பைப் பின்பற்றுவதற்கு.",
            "கனடா அரசியலமைப்பிலிருந்து பெறப்பட்டு, வலுவான மையத்தைப் பேணவும் தேசிய ஒருமைப்பாட்டை உறுதிப்படுத்தவும்.",
            "சங்கரி பிரசாத் வழக்கில் உச்ச நீதிமன்றம் அதனைப் பரிந்துரைத்ததால்.",
            "சர்வதேச சங்கத்தின் தேவைகளுக்குக் கீழ்ப்படிவதற்கு."
        ],
        correct_ans="B",
        exp_en="Historical Context: Framing of Indian federalism prioritized central unity over regional fragmentation.\nReason: Article 248 vests Residuary Powers (subjects not listed in Seventh Schedule) in Parliament. This feature was borrowed from Canada (unlike US/Australia where residuary powers lie with states) to strengthen central authority.\nConstitutional Impact: Ensures Centre can legislate on unexpected future matters (e.g., Cyber Law, Space Law).\nExam Trap: USA/Australia = Residuary powers with States; Canada/India = Residuary powers with Centre.",
        exp_ta="வரலாற்றுப் பின்னணி: இந்தியக் கூட்டாட்சியை உருவாக்குவது பிராந்தியப் பிரிவினையை விட மத்திய ஒருமைப்பாட்டிற்கு முன்னுரிமை அளித்தது.\nகாரணம்: உறுப்பு 248 எஞ்சிய அதிகாரங்களை (7வது அட்டவணையில் பட்டியலிடப்படாத பொருட்கள்) நாடாளுமன்றத்திற்கு வழங்குகிறது. இந்த அம்சம் கனடாவிலிருந்து பெறப்பட்டது (அமெரிக்கா/ஆஸ்திரேலியாவைப் போலல்லாமல் இங்கு எஞ்சிய அதிகாரங்கள் மாநிலங்களிடம் உள்ளன) மத்திய அதிகாரத்தை வலுப்படுத்த பெறப்பட்டது.\nஅரசியலமைப்பு தாக்கம்: எதிர்பாராத எதிர்கால விஷயங்களில் (எ.கா., சைபர் சட்டம், விண்வெளி சட்டம்) மத்திய அரசு சட்டமியற்ற முடியும் என்பதை உறுதி செய்கிறது.\nதேர்வுப் பொறி: அமெரிக்கா/ஆஸ்திரேலியா = எஞ்சிய அதிகாரங்கள் மாநிலங்களிடம் உள்ளன; கனடா/இந்தியா = எஞ்சிய அதிகாரங்கள் மத்திய அரசிடம் உள்ளன.",
        wno_dict={
            "A": {"en": "Incorrect. Swiss system was not followed.", "ta": "தவறு. சுவிஸ் முறை பின்பற்றப்படவில்லை."},
            "B": {"en": "Correct. Borrowed from Canadian model to establish a strong Centre (Article 248).", "ta": "சரி. வலுவான மையத்தை நிறுவ கனடா மாதிரியிலிருந்து பெறப்பட்டது (உறுப்பு 248)."},
            "C": {"en": "Incorrect. Shankari Prasad case dealt with Article 368 vs Article 13.", "ta": "தவறு. சங்கரி பிரசாத் வழக்கு உறுப்பு 368 vs உறுப்பு 13 பற்றியது."},
            "D": {"en": "Incorrect. League of Nations is irrelevant.", "ta": "தவறு. சர்வதேச சங்கம் தொடர்பற்றது."}
        },
        tip_en="TNPSC Tip: Article 248: Residuary Powers vested in Centre (Parliament) - Borrowed from Canada.",
        tip_ta="TNPSC குறிப்பு: உறுப்பு 248: எஞ்சிய அதிகாரங்கள் மத்திய அரசிடம் (நாடாளுமன்றம்) உள்ளன - கனடாவிலிருந்து பெறப்பட்டது.",
        rev_en="Residuary Powers (Art 248): Vested in Parliament (Canadian Feature).",
        rev_ta="எஞ்சிய அதிகாரங்கள் (உறுப்பு 248): நாடாளுமன்றத்திற்கு வழங்கப்பட்டுள்ளன (கனடா அம்சம்).",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Understand", est_sec=45, pyq_sim="High", tags=["Residuary Powers", "Article 248", "Canadian Constitution"]
    ))

    # Q74 - Statement-Based - Medium - Ans C
    qs.append(make_q(
        q_id="SF_GT_074", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="Statement-Based",
        q_en="Consider the following statements regarding the 44th Constitutional Amendment Act, 1978:\n1. It replaced the phrase 'internal disturbance' with 'armed rebellion' in Article 352 for declaring National Emergency.\n2. It deleted the Right to Property from the list of Fundamental Rights in Part III.\n3. It made the advice tendered by the Council of Ministers binding on the President without any option for reconsideration.\n\nWhich of the statements given above are CORRECT?",
        q_ta="1978 இன் 44வது அரசியலமைப்பு திருத்தச் சட்டம் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது தேசிய அவசரநிலையை அறிவிப்பதற்காக உறுப்பு 352 இல் 'உள்நாட்டு அமைதியின்மை' என்ற சொற்றொடருக்குப் பதிலாக 'ஆயுதமேந்திய கிளர்ச்சி' என்பதை மாற்றியது.\n2. இது பகுதி III இல் உள்ள அடிப்படை உரிமைகளின் பட்டியலிலிருந்து சொத்து உரிமையை നീக்கியது.\n3. இது அமைச்சரவை வழங்கும் ஆலோசனையை மறுபரிசீலனை செய்வதற்கான எந்த விருப்பமும் இன்றி குடியரசுத் தலைவரைக் கட்டுப்படுத்துவதாக மாற்றியது.\n\nமேற்கூறிய கூற்றுகளில் எது சரியானவை?",
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
        exp_en="Historical Context: 44th Amendment Act 1978 enacted by Janata Party government to rectify distortions introduced during emergency.\nReason:\nStatement 1 is correct: Replaced 'internal disturbance' with 'armed rebellion' in Art 352.\nStatement 2 is correct: Deleted Right to Property from Part III (made Art 300A legal right).\nStatement 3 is INCORRECT: 44th Amendment empowered President to return advice of CoM ONCE for reconsideration (though reconsidered advice is binding).\nConstitutional Impact: Restored constitutional checks and balances.",
        exp_ta="வரலாற்றுப் பின்னணி: அவசரநிலையின் போது செய்யப்பட்ட மாற்றங்களைச் சரிசெய்ய ஜனதா கட்சி அரசாங்கத்தால் 1978 இல் 44வது திருத்தச் சட்டம் இயற்றப்பட்டது.\nகாரணம்:\nகூற்று 1 சரி: உறுப்பு 352 இல் 'உள்நாட்டு அமைதியின்மை' என்பதற்குப் பதிலாக 'ஆயுதமேந்திய கிளர்ச்சி' என்று மாற்றப்பட்டது.\nகூற்று 2 சரி: பகுதி III லிருந்து சொத்து உரிமையை நீக்கியது (உறுப்பு 300A சட்ட உரிமையாக்கியது).\nகூற்று 3 தவறு: 44வது திருத்தம் அமைச்சரவையின் ஆலோசனையை ஒரு முறை மறுபரிசீலனைக்குத் திருப்பி அனுப்ப குடியரசுத் தலைவருக்கு அதிகாரம் அளித்தது (மறுபரிசீலனை செய்யப்பட்ட ஆலோசனை கட்டுப்படுத்தும் என்றாலும்).\nஅரசியலமைப்பு தாக்கம்: அரசியலமைப்பு சமநிலையை மீட்டெடுத்தது.",
        wno_dict={
            "A": {"en": "Incorrect. Statement 3 is false (President CAN send advice back once for reconsideration under 44th Amendment).", "ta": "தவறு. 44வது திருத்தத்தின் கீழ் குடியரசுத் தலைவர் ஆலோசனையை ஒரு முறை மறுபரிசீலனைக்கு திருப்பி அனுப்ப முடியும் என்பதால் கூற்று 3 தவறு."},
            "B": {"en": "Incorrect. Statement 3 is false.", "ta": "தவறு. கூற்று 3 தவறு."},
            "C": {"en": "Correct. Statements 1 and 2 are correct; Statement 3 is false.", "ta": "சரி. கூற்றுகள் 1 மற்றும் 2 சரி; கூற்று 3 தவறு."},
            "D": {"en": "Incorrect. Statement 3 is false.", "ta": "தவறு. கூற்று 3 தவறு."}
        },
        tip_en="TNPSC Trap: 44th Amendment (1978): Armed rebellion replaced internal disturbance (Art 352); President CAN send CoM advice back ONCE.",
        tip_ta="TNPSC பொறி: 44வது திருத்தம் (1978): உள்நாட்டு அமைதியின்மைக்குப் பதிலாக ஆயுதமேந்திய கிளர்ச்சி (உறுப்பு 352); குடியரசுத் தலைவர் அமைச்சரவை ஆலோசனையை ஒருமுறை திருப்பி அனுப்பலாம்.",
        rev_en="44th Amendment 1978: Armed rebellion, Property to Art 300A, President 1-time reconsideration option.",
        rev_ta="44வது திருத்தம் 1978: ஆயுதமேந்திய கிளர்ச்சி, சொத்து 300A, குடியரசுத் தலைவருக்கு 1-முறை மறுபரிசீலனை விருப்பம்.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Analyze", est_sec=60, pyq_sim="High", tags=["44th Amendment", "Emergency Provisions", "Right to Property", "TNPSC Trap"]
    ))

    # Q75 - TNPSC Trap - Hard - Ans D
    qs.append(make_q(
        q_id="SF_GT_075", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Hard", question_type="TNPSC Trap",
        q_en="Which of the following statements regarding the amendment of the Indian Constitution under Article 368 is INCORRECT?",
        q_ta="உறுப்பு 368 இன் கீழ் இந்திய அரசியலமைப்பைத் திருத்துவது தொடர்பான பின்வரும் கூற்றுகளில் எது தவறானது (INCORRECT)?",
        opts_en=[
            "An Amendment Bill can be introduced in either House of Parliament.",
            "An Amendment Bill does not require prior permission of the President for introduction.",
            "If there is a disagreement between the two Houses on a Constitutional Amendment Bill, a joint sitting is summoned under Article 108.",
            "The President must give assent to a Constitutional Amendment Bill passed by both Houses (24th Amendment 1971)."
        ],
        opts_ta=[
            "நாடாளுமன்றத்தின் எந்த அவையிலும் திருத்த மசோதாவை அறிமுகப்படுத்தலாம்.",
            "திருத்த மசோதாவை அறிமுகப்படுத்த குடியரசுத் தலைவரின் முன் அனுமதி தேவையில்லை.",
            "அரசியலமைப்பு திருத்த மசோதாவில் இரு அவைகளுக்கும் இடையே கருத்து வேறுபாடு ஏற்பட்டால், உறுப்பு 108 இன் கீழ் கூட்டு அமர்வு கூட்டப்படும்.",
            "இரு அவைகளாலும் நிறைவேற்றப்பட்ட அரசியலமைப்பு திருத்த மசோதாவிற்கு குடியரசுத் தலைவர் கட்டாயம் ஒப்புதல் அளிக்க வேண்டும் (24வது திருத்தம் 1971)."
        ],
        correct_ans="C",
        exp_en="Historical Context: Procedure for constitutional amendment under Article 368 has specific mandatory rules.\nReason: Statement C is INCORRECT because there is NO provision for holding a Joint Sitting of both Houses of Parliament in case of a dead-lock over a Constitutional Amendment Bill. Each House must pass the bill separately by Special Majority.\nConstitutional Impact: Ensures both Lok Sabha and Rajya Sabha have equal veto power over constitutional changes.\nExam Trap: Joint sitting (Art 108) applies to Ordinary Bills and Financial Bills, but NEVER to Constitutional Amendment Bills or Money Bills.",
        exp_ta="வரலாற்றுப் பின்னணி: உறுப்பு 368 இன் கீழ் அரசியலமைப்பு திருத்த நடைமுறை குறிப்பிட்ட கட்டாய விதிகளைக் கொண்டுள்ளது.\nகாரணம்: அரசியலமைப்பு திருத்த மசோதா மீதான முடக்கத்தின் போது நாடாளுமன்றத்தின் இரு அவைகளின் கூட்டு அமர்வை நடத்துவதற்கு எந்த விதியும் இல்லாததால் கூற்று C தவறானது. ஒவ்வொரு அவையும் சிறப்பு பெரும்பான்மையால் மசோதாவை தனித்தனியாக நிறைவேற்ற வேண்டும்.\nஅரசியலமைப்பு தாக்கம்: அரசியலமைப்பு மாற்றங்கள் மீது மக்களவை மற்றும் மாநிலங்களவை இரண்டும் சமமான வீட்டோ அதிகாரத்தைக் கொண்டிருப்பதை உறுதி செய்கிறது.\nதேர்வுப் பொறி: கூட்டு அமர்வு (உறுப்பு 108) சாதாரண மசோதாக்கள் மற்றும் நிதி மசோதாக்களுக்குப் பொருந்தும், ஆனால் அரசியலமைப்பு திருத்த மசோதாக்கள் அல்லது பண மசோதாக்களுக்கு ஒருபோதும் பொருந்தாது.",
        wno_dict={
            "A": {"en": "Correct statement (Can be introduced in either Lok Sabha or Rajya Sabha).", "ta": "சரியான கூற்று (மக்களவை அல்லது மாநிலங்களவை இரண்டிலும் அறிமுகப்படுத்தலாம்)."},
            "B": {"en": "Correct statement (No prior recommendation of President required).", "ta": "சரியான கூற்று (குடியரசுத் தலைவரின் முன் பரிந்துரை தேவையில்லை)."},
            "C": {"en": "INCORRECT statement (There is NO provision for joint sitting for Constitutional Amendment Bills under Art 368).", "ta": "தவறான கூற்று (உறுப்பு 368 இன் கீழ் அரசியலமைப்பு திருத்த மசோதாக்களுக்கு கூட்டு அமர்வுக்கு எந்த விதியும் இல்லை)."},
            "D": {"en": "Correct statement (24th Amendment 1971 made President's assent mandatory).", "ta": "சரியான கூற்று (24வது திருத்தம் 1971 குடியரசுத் தலைவரின் ஒப்புதலைக் கட்டாயமாக்கியது)."}
        },
        tip_en="TNPSC Trap: NO Joint Sitting for Constitutional Amendment Bills under Article 368! Each House must pass it separately.",
        tip_ta="TNPSC பொறி: உறுப்பு 368 இன் கீழ் அரசியலமைப்பு திருத்த மசோதாக்களுக்கு கூட்டு அமர்வு இல்லை! ஒவ்வொரு அவையும் தனித்தனியாக நிறைவேற்ற வேண்டும்.",
        rev_en="Article 368 rules: Introduced in either House, no prior President consent, NO Joint Sitting, President assent mandatory.",
        rev_ta="உறுப்பு 368 விதிகள்: எந்த அவையிலும் அறிமுகப்படுத்தலாம், குடியரசுத் தலைவரின் முன் அனுமதி தேவையில்லை, கூட்டு அமர்வு இல்லை, குடியரசுத் தலைவர் ஒப்புதல் கட்டாயம்.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Analyze", est_sec=75, pyq_sim="High", tags=["Article 368", "Joint Sitting", "Constitutional Amendment", "TNPSC Trap"]
    ))

    return qs

print("Part 3 defined: 25 questions.")
