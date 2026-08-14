# sf_q_part4.py - Questions 76 to 100 for Salient Features Grand Test
from scratch_sf_helper import make_q

def get_part4_questions():
    qs = []

    # Q76 - Direct MCQ - Easy - Ans A
    qs.append(make_q(
        q_id="SF_GT_076", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Easy", question_type="Direct MCQ",
        q_en="Which feature of the Indian Constitution ensures that all public offices are open to every citizen without any discrimination?",
        q_ta="இந்திய அரசியலமைப்பின் எந்த அம்சம் அனைத்து பொதுப் பதவிகளும் எந்தவொரு பாகுபாடுமின்றி ஒவ்வொரு குடிமகனுக்கும் திறந்திருப்பதை உறுதி செய்கிறது?",
        opts_en=[
            "Republican Character",
            "Federal System",
            "Bicameralism",
            "Emergency Provisions"
        ],
        opts_ta=[
            "குடியரசுத் தன்மை",
            "கூட்டாட்சி முறை",
            "ஈரவை முறை",
            "அவசரக்கால விதிகள்"
        ],
        correct_ans="A",
        exp_en="Historical Context: The term 'Republic' in the Preamble signifies two things: elected head of state and absence of privileged class.\nReason: In a Republic, political sovereignty is vested in the people and all public offices are open to every citizen without any discrimination.\nConstitutional Impact: Guarantees equal opportunity under Article 16 in public employment.\nExam Trap: Monarchy has privileged hereditary offices; Republic has open public offices for all citizens.\nMemory Trick: Republic = Open Public offices for all.",
        exp_ta="வரலாற்றுப் பின்னணி: முகவுரையில் உள்ள 'குடியரசு' என்ற சொல் இரண்டு விஷயங்களைக் குறிக்கிறது: தேர்ந்தெடுக்கப்பட்ட நாட்டின் தலைவர் மற்றும் சலுகை பெற்ற வகுப்பு இல்லாதது.\nகாரணம்: ஒரு குடியரசில், அரசியல் இறையாண்மை மக்களிடம் உள்ளது மற்றும் அனைத்து பொதுப் பதவிகளும் எந்தவொரு பாகுபாடுமின்றி ஒவ்வொரு குடிமகனுக்கும் திறந்திருக்கும்.\nஅரசியலமைப்பு தாக்கம்: பொது வேலைவாய்ப்பில் உறுப்பு 16 இன் கீழ் சம வாய்ப்பை உத்தரவாதம் செய்கிறது.\nதேர்வுப் பொறி: முடியாட்சி சலுகை பெற்ற பரம்பரை பதவிகளைக் கொண்டுள்ளது; குடியரசு அனைத்து குடிமக்களுக்கும் திறந்த பொதுப் பதவிகளைக் கொண்டுள்ளது.\nநினைவுச் சூத்திரம்: குடியரசு = அனைவருக்கும் திறந்த பொதுப் பதவிகள்.",
        wno_dict={
            "A": {"en": "Correct. Republican character ensures public offices are open to all citizens.", "ta": "சரி. குடியரசுத் தன்மை பொதுப் பதவிகள் அனைத்து குடிமக்களுக்கும் திறந்திருப்பதை உறுதி செய்கிறது."},
            "B": {"en": "Incorrect. Federal system deals with division of power between Centre and States.", "ta": "தவறு. கூட்டாட்சி முறை மத்திய அரசுக்கும் மாநிலங்களுக்கும் இடையிலான அதிகாரப் பகிர்வைக் கையாள்கிறது."},
            "C": {"en": "Incorrect. Bicameralism means having two houses of legislature.", "ta": "தவறு. ஈரவை முறை என்பது இரண்டு சட்டமன்ற அவைகளைக் கொண்டிருப்பதாகும்."},
            "D": {"en": "Incorrect. Emergency provisions deal with national crises.", "ta": "தவறு. அவசரக்கால விதிகள் தேசிய நெருக்கடிகளைக் கையாள்கின்றன."}
        },
        tip_en="TNPSC Tip: Republic = Elected Head of State + Absence of privileged class + All public offices open to all citizens.",
        tip_ta="TNPSC குறிப்பு: குடியரசு = தேர்ந்தெடுக்கப்பட்ட நாட்டின் தலைவர் + சலுகை பெற்ற வகுப்பு இல்லாமை + அனைத்து பொதுப் பதவிகளும் அனைவருக்கும் திறந்திருக்கும்.",
        rev_en="Republic: Elected head of state + all public offices open without discrimination.",
        rev_ta="குடியரசு: தேர்ந்தெடுக்கப்பட்ட நாட்டின் தலைவர் + பாகுபாடின்றி அனைவருக்கும் திறந்த பொதுப் பதவிகள்.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Remember", est_sec=30, pyq_sim="High", tags=["Republic", "Public Offices", "Equality of Opportunity"]
    ))

    # Q77 - Conceptual - Medium - Ans B
    qs.append(make_q(
        q_id="SF_GT_077", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="Conceptual",
        q_en="Which of the following constitutional provisions contains specific safeguards for the educational and economic interests of Scheduled Castes, Scheduled Tribes, and other Weaker Sections?",
        q_ta="பின்வரும் அரசியலமைப்பு விதிகளில் எது பட்டியல் சாதியினர், பட்டியல் பழங்குடியினர் மற்றும் பிற பலவீனமான பிரிவினரின் கல்வி மற்றும் பொருளாதார நலன்களுக்கான குறிப்பிட்ட பாதுகாப்புகளைக் கொண்டுள்ளது?",
        opts_en=[
            "Article 40 in DPSP",
            "Article 46 in DPSP",
            "Article 51 in DPSP",
            "Article 43 in DPSP"
        ],
        opts_ta=[
            "DPSP இல் உள்ள உறுப்பு 40",
            "DPSP இல் உள்ள உறுப்பு 46",
            "DPSP இல் உள்ள உறுப்பு 51",
            "DPSP இல் உள்ள உறுப்பு 43"
        ],
        correct_ans="B",
        exp_en="Historical Context: Article 46 is a key Directive Principle under Part IV aimed at social justice and uplifting disadvantaged sections.\nReason: Article 46 directs the State to promote with special care the educational and economic interests of the weaker sections of the people, and in particular, of the Scheduled Castes and the Scheduled Tribes, and protect them from social injustice and all forms of exploitation.\nConstitutional Impact: Forms the constitutional bedrock for affirmative welfare policies and reservation provisions.\nExam Trap: Art 46 = SC/ST educational/economic welfare; Art 40 = Village Panchayats; Art 43 = Living wage for workers.",
        exp_ta="வரலாற்றுப் பின்னணி: உறுப்பு 46 என்பது பகுதி IV இன் கீழ் சமூக நீதி மற்றும் பிற்படுத்தப்பட்ட பிரிவினரை உயர்த்துவதை நோக்கமாகக் கொண்ட ஒரு முக்கிய நெறிமுறைக் கோட்பாடாகும்.\nகாரணம்: மக்களின் பலவீனமான பிரிவினர், குறிப்பாக பட்டியல் சாதியினர் மற்றும் பட்டியல் பழங்குடியினரின் கல்வி மற்றும் பொருளாதார நலன்களை சிறப்பு கவனத்துடன் மேம்படுத்தவும், சமூக அநீதி மற்றும் அனைத்து வகையான சுரண்டல்களிலிருந்தும் அவர்களைப் பாதுகாக்கவும் உறுப்பு 46 அரசுக்கு வழிகாட்டுகிறது.\nஅரசியலமைப்பு தாக்கம்: நேர்மறையான நலன்புரி கொள்கைகள் மற்றும் இடஒதுக்கீடு விதிகளுக்கான அரசியலமைப்பு அடித்தளத்தை அமைக்கிறது.\nதேர்வுப் பொறி: உறுப்பு 46 = SC/ST கல்வி/பொருளாதார நலன்; உறுப்பு 40 = கிராம பஞ்சாயத்துகள்; உறுப்பு 43 = தொழிலாளர்களுக்கு வாழ்வாதார ஊதியம்.",
        wno_dict={
            "A": {"en": "Incorrect. Article 40 deals with Organization of Village Panchayats.", "ta": "தவறு. உறுப்பு 40 கிராம பஞ்சாயத்துகள் அமைப்பு பற்றியது."},
            "B": {"en": "Correct. Article 46 protects educational and economic interests of SCs, STs, and weaker sections.", "ta": "சரி. உறுப்பு 46 SC, ST மற்றும் பலவீனமான பிரிவினரின் கல்வி மற்றும் பொருளாதார நலன்களைப் பாதுகாக்கிறது."},
            "C": {"en": "Incorrect. Article 51 deals with Promotion of International Peace and Security.", "ta": "தவறு. உறுப்பு 51 சர்வதேச அமைதி மற்றும் பாதுகாப்பை ஊக்குவிப்பது பற்றியது."},
            "D": {"en": "Incorrect. Article 43 deals with Living wage for workers.", "ta": "தவறு. உறுப்பு 43 தொழிலாளர்களுக்கு வாழ்வாதார ஊதியம் பற்றியது."}
        },
        tip_en="TNPSC Tip: Article 46 (DPSP) = Educational & Economic interests of SCs, STs & Weaker Sections.",
        tip_ta="TNPSC குறிப்பு: உறுப்பு 46 (DPSP) = SC, ST & பலவீனமான பிரிவினரின் கல்வி & பொருளாதார நலன்கள்.",
        rev_en="Article 46 DPSP: State shall promote educational and economic interests of SCs, STs, and weaker sections.",
        rev_ta="உறுப்பு 46 DPSP: SC, ST மற்றும் பலவீனமான பிரிவினரின் கல்வி மற்றும் பொருளாதார நலன்களை அரசு மேம்படுத்த வேண்டும்.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Remember", est_sec=45, pyq_sim="High", tags=["Article 46", "DPSP", "SC ST Safeguards", "Social Justice"]
    ))

    # Q78 - Statement-Based - Medium - Ans C
    qs.append(make_q(
        q_id="SF_GT_078", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="Statement-Based",
        q_en="Consider the following statements regarding the 'Basic Structure' of the Indian Constitution:\n1. The term 'Basic Structure' is explicitly defined under Article 368 of the Constitution.\n2. In Minerva Mills Case (1980), judicial review was held to be a basic feature of the Constitution.\n3. Parliament cannot use its amending power under Article 368 to destroy its own limited amending power.\n\nWhich of the statements given above are CORRECT?",
        q_ta="இந்திய அரசியலமைப்பின் 'அடிப்படை கட்டமைப்பு' (Basic Structure) தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 'அடிப்படை கட்டமைப்பு' என்ற சொல் அரசியலமைப்பின் உறுப்பு 368 இன் கீழ் வெளிப்படையாக வரையறுக்கப்பட்டுள்ளது.\n2. மினர்வா மில்ஸ் வழக்கில் (1980), நீதித்துறை மறுஆய்வு அரசியலமைப்பின் அடிப்படை அம்சமாக நிலைநிறுத்தப்பட்டது.\n3. நாடாளுமன்றம் உறுப்பு 368 இன் கீழ் தனக்குள்ள திருத்தும் அதிகாரத்தைப் பயன்படுத்தித் தனது சொந்த வரம்பிற்குட்பட்ட திருத்தும் அதிகாரத்தை அழிக்க முடியாது.\n\nமேற்கூறிய கூற்றுகளில் எது சரியானவை?",
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
        correct_ans="C",
        exp_en="Historical Context: Basic Structure doctrine was propounded in Kesavananda Bharati (1973) and reaffirmed in Minerva Mills (1980).\nReason:\nStatement 1 is INCORRECT: The phrase 'Basic Structure' is NOWHERE mentioned or defined in the Constitution text; it is a judicial invention.\nStatement 2 is correct: Judicial Review was affirmed as Basic Structure in Minerva Mills (1980).\nStatement 3 is correct: SC held that limited amending power itself is a basic feature; Parliament cannot expand it to unlimited power under Art 368.\nConstitutional Impact: Preserves constitutional identity against legislative overreach.\nExam Trap: 'Basic Structure' phrase is NOT defined in the Constitution.",
        exp_ta="வரலாற்றுப் பின்னணி: அடிப்படை கட்டமைப்பு கோட்பாடு கேசவாநந்த பாரதி (1973) வழக்கில் முன்வைக்கப்பட்டு மினர்வா மில்ஸ் (1980) வழக்கில் மீண்டும் உறுதிப்படுத்தப்பட்டது.\nகாரணம்:\nகூற்று 1 தவறு: 'அடிப்படை கட்டமைப்பு' என்ற சொல் அரசியலமைப்பு உரையில் எங்கும் குறிப்பிடப்படவோ வரையறுக்கப்படவோ இல்லை; இது ஒரு நீதித்துறை கண்டுபிடிப்பு.\nகூற்று 2 சரி: மினர்வா மில்ஸ் (1980) வழக்கில் நீதித்துறை மறுஆய்வு அடிப்படை அமைப்பாக உறுதி செய்யப்பட்டது.\nகூற்று 3 சரி: வரம்பிற்குட்பட்ட திருத்தும் அதிகாரமே ஒரு அடிப்படை அம்சம் என்று உச்ச நீதிமன்றம் கூறியது; உறுப்பு 368 இன் கீழ் நாடாளுமன்றம் அதை வரம்பற்ற அதிகாரமாக விரிவுபடுத்த முடியாது.\nஅரசியலமைப்பு தாக்கம்: சட்டமன்ற மீறலுக்கு எதிராக அரசியலமைப்பு அடையாளத்தைப் பாதுகாக்கிறது.\nதேர்வுப் பொறி: 'அடிப்படை கட்டமைப்பு' என்ற சொல் அரசியலமைப்பில் வரையறுக்கப்படவில்லை.",
        wno_dict={
            "A": {"en": "Incorrect. Statement 1 is false (Basic Structure is not defined in Constitution).", "ta": "தவறு. கூற்று 1 தவறு (அடிப்படை கட்டமைப்பு அரசியலமைப்பில் வரையறுக்கப்படவில்லை)."},
            "B": {"en": "Incorrect. Statement 1 is false.", "ta": "தவறு. கூற்று 1 தவறு."},
            "C": {"en": "Correct. Statements 2 and 3 are correct; Statement 1 is false.", "ta": "சரி. கூற்றுகள் 2 மற்றும் 3 சரி; கூற்று 1 தவறு."},
            "D": {"en": "Incorrect. Statement 1 is false.", "ta": "தவறு. கூற்று 1 தவறு."}
        },
        tip_en="TNPSC Trap: 'Basic Structure' is a judicial creation and is NOT defined anywhere in the text of the Constitution.",
        tip_ta="TNPSC பொறி: 'அடிப்படை கட்டமைப்பு' என்பது ஒரு நீதித்துறை உருவாக்கம் மற்றும் அரசியலமைப்பின் உரையில் எங்கும் வரையறுக்கப்படவில்லை.",
        rev_en="Basic Structure Doctrine: Judicial creation (1973), not defined in Constitution text.",
        rev_ta="அடிப்படை கட்டமைப்பு கோட்பாடு: நீதித்துறை உருவாக்கம் (1973), அரசியலமைப்பு உரையில் வரையறுக்கப்படவில்லை.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Analyze", est_sec=60, pyq_sim="High", tags=["Basic Structure", "Minerva Mills Case", "Article 368", "TNPSC Trap"]
    ))

    # Q79 - Assertion & Reason - Medium - Ans D
    qs.append(make_q(
        q_id="SF_GT_079", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="Assertion & Reason",
        q_en="Given below are two statements, one labeled as Assertion (A) and the other labeled as Reason (R):\n\nAssertion (A): Fundamental Rights protected under Part III of the Constitution are absolute and unconditional.\nReason (R): Parliament can impose reasonable restrictions on Fundamental Rights on grounds such as sovereignty, security of the state, public order, and morality under Article 19.",
        q_ta="கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிக்கப்பட்டுள்ளது:\n\nகூற்று (A): அரசியலமைப்பின் பகுதி III இன் கீழ் பாதுகாக்கப்பட்ட அடிப்படை உரிமைகள் முழுமையானவை (absolute) மற்றும் நிபந்தனையற்றவை.\nகாரணம் (R): உறுப்பு 19 இன் கீழ் நாட்டின் இறையாண்மை, அரசின் பாதுகாப்பு, பொது ஒழுங்கு மற்றும் ஒழுக்கம் போன்ற காரணங்களின் அடிப்படையில் அடிப்படை உரிமைகள் மீது நாடாளுமன்றம் ஏதுவான வரம்புகளைச் (reasonable restrictions) சுமத்த முடியும்.",
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
        correct_ans="D",
        exp_en="Historical Context: Framing of Part III balanced individual liberty with social interest.\nReason: Assertion (A) is FALSE: Fundamental Rights are NOT absolute; they are qualified. State can impose reasonable restrictions. Reason (R) is TRUE: Article 19 explicitly permits reasonable restrictions on rights (speech, assembly, association, movement, residence, profession) for public interest and state security.\nConstitutional Impact: Strikes a balance between individual freedom and public interest.\nExam Trap: Fundamental Rights are QUALIFIED, not absolute.",
        exp_ta="வரலாற்றுப் பின்னணி: பகுதி III ஐ உருவாக்குவது தனிநபர் சுதந்திரத்தைச் சமூக நலனுடன் சமநிலைப்படுத்தியது.\nகாரணம்: கூற்று (A) தவறு: அடிப்படை உரிமைகள் முழுமையானவை அல்ல; அவை வரம்பிற்குட்பட்டவை (qualified). அரசு ஏதுவான வரம்புகளைச் சுமத்தலாம். காரணம் (R) சரி: உறுப்பு 19 பொது நலன் மற்றும் அரசு பாதுகாப்பிற்காக உரிமைகள் (பேச்சு, கூட்டம், சங்கம், இயக்கம், வசிப்பிடம், தொழில்) மீது ஏதுவான வரம்புகளை வெளிப்படையாக அனுமதிக்கிறது.\nஅரசியலமைப்பு தாக்கம்: தனிநபர் சுதந்திரத்திற்கும் பொது நலனுக்கும் இடையே ஒரு சமநிலையை ஏற்படுத்துகிறது.\nதேர்வுப் பொறி: அடிப்படை உரிமைகள் வரம்பிற்குட்பட்டவை (QUALIFIED), முழுமையானவை (absolute) அல்ல.",
        wno_dict={
            "A": {"en": "Incorrect. (A) is false because FRs are not absolute.", "ta": "தவறு. (A) தவறு ஏனெனில் அடிப்படை உரிமைகள் முழுமையானவை அல்ல."},
            "B": {"en": "Incorrect. (A) is false.", "ta": "தவறு. (A) தவறு."},
            "C": {"en": "Incorrect. (A) is false.", "ta": "தவறு. (A) தவறு."},
            "D": {"en": "Correct. (A) is false (FRs are qualified, not absolute) and (R) is true (reasonable restrictions apply).", "ta": "சரி. (A) தவறு (FRகள் வரம்பிற்குட்பட்டவை, முழுமையானவை அல்ல) மற்றும் (R) சரி (ஏதுவான வரம்புகள் பொருந்தும்)."}
        },
        tip_en="TNPSC Trap: Fundamental Rights are NOT absolute, but QUALIFIED (subject to reasonable restrictions under Art 19).",
        tip_ta="TNPSC பொறி: அடிப்படை உரிமைகள் முழுமையானவை அல்ல, வரம்பிற்குட்பட்டவை (உறுப்பு 19 இன் கீழ் ஏதுவான வரம்புகளுக்கு உட்பட்டவை).",
        rev_en="Fundamental Rights = Qualified, not Absolute (Subject to Reasonable Restrictions).",
        rev_ta="அடிப்படை உரிமைகள் = வரம்பிற்குட்பட்டவை, முழுமையானவை அல்ல (ஏதுவான வரம்புகளுக்கு உட்பட்டவை).",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Evaluate", est_sec=60, pyq_sim="High", tags=["Fundamental Rights", "Article 19", "Reasonable Restrictions", "TNPSC Trap"]
    ))

    # Q80 - Match the Following - Medium - Ans B
    qs.append(make_q(
        q_id="SF_GT_080", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="Match the Following",
        q_en="Match List-I (Constitutional Amendment) with List-II (Core Provision Added/Modified) and select the correct option:\n\nList-I:\n(a) 42nd Amendment Act (1976)\n(b) 44th Amendment Act (1978)\n(c) 61st Amendment Act (1988)\n(d) 86th Amendment Act (2002)\n\nList-II:\n1. Reduction of voting age from 21 to 18 years\n2. Insertion of Article 21A (Right to Education)\n3. Addition of Part IVA (Fundamental Duties)\n4. Creation of Article 300A (Right to Property as Legal Right)",
        q_ta="பட்டியல்-I (அரசியலமைப்பு திருத்தம்) பட்டியல்-II (சேர்க்கப்பட்ட/மாற்றப்பட்ட முக்கிய விதி) உடன் பொருத்தி சரியான விருப்பத்தைத் தேர்ந்தெடுக்கவும்:\n\nபட்டியல்-I:\n(a) 42வது திருத்தச் சட்டம் (1976)\n(b) 44வது திருத்தச் சட்டம் (1978)\n(c) 61வது திருத்தச் சட்டம் (1988)\n(d) 86வது திருத்தச் சட்டம் (2002)\n\nபட்டியல்-II:\n1. வாக்களிக்கும் வயதை 21 இலிருந்து 18 ஆகக் குறைத்தல்\n2. உறுப்பு 21A சேர்ப்பு (கல்வி உரிமை)\n3. பகுதி IVA சேர்ப்பு (அடிப்படை கடமைகள்)\n4. உறுப்பு 300A உருவாக்கம் (சொத்து உரிமை சட்ட உரிமையாக)\n\nவிருப்பங்கள்:",
        opts_en=[
            "(a)-3, (b)-1, (c)-4, (d)-2",
            "(a)-3, (b)-4, (c)-1, (d)-2",
            "(a)-4, (b)-3, (c)-1, (d)-2",
            "(a)-3, (b)-4, (c)-2, (d)-1"
        ],
        opts_ta=[
            "(a)-3, (b)-1, (c)-4, (d)-2",
            "(a)-3, (b)-4, (c)-1, (d)-2",
            "(a)-4, (b)-3, (c)-1, (d)-2",
            "(a)-3, (b)-4, (c)-2, (d)-1"
        ],
        correct_ans="B",
        exp_en="Historical Context: Key constitutional amendments defined modern rights and democratic participation.\nReason:\n(a) 42nd Amendment (1976) = Part IVA Fundamental Duties (3)\n(b) 44th Amendment (1978) = Article 300A Right to Property (4)\n(c) 61st Amendment (1988) = Voting age reduced to 18 (1)\n(d) 86th Amendment (2002) = Article 21A Right to Education (2)\nMatching: (a)-3, (b)-4, (c)-1, (d)-2.",
        exp_ta="வரலாற்றுப் பின்னணி: முக்கிய அரசியலமைப்பு திருத்தங்கள் நவீன உரிமைகள் மற்றும் ஜனநாயக பங்கேற்பை வரையறுத்தன.\nகாரணம்:\n(a) 42வது திருத்தம் (1976) = பகுதி IVA அடிப்படை கடமைகள் (3)\n(b) 44வது திருத்தம் (1978) = உறுப்பு 300A சொத்து உரிமை (4)\n(c) 61வது திருத்தம் (1988) = வாக்கு வயது 18 ஆகக் குறைக்கப்பட்டது (1)\n(d) 86வது திருத்தம் (2002) = உறுப்பு 21A கல்வி உரிமை (2)\nபொருத்துதல்: (a)-3, (b)-4, (c)-1, (d)-2.",
        wno_dict={
            "A": {"en": "Incorrect. 44th Amendment is Art 300A (4), not Voting age (1).", "ta": "தவறு. 44வது திருத்தம் உறுப்பு 300A (4), வாக்கு வயது (1) அல்ல."},
            "B": {"en": "Correct. All four amendments matched accurately: (a)-3, (b)-4, (c)-1, (d)-2.", "ta": "சரி. நான்கு திருத்தங்களும் துல்லியமாகப் பொருந்துகின்றன: (a)-3, (b)-4, (c)-1, (d)-2."},
            "C": {"en": "Incorrect. 42nd Amendment is FDs (3), not Art 300A (4).", "ta": "தவறு. 42வது திருத்தம் FDகள் (3), உறுப்பு 300A (4) அல்ல."},
            "D": {"en": "Incorrect. 61st Amendment is Voting age (1), not Art 21A (2).", "ta": "தவறு. 61வது திருத்தம் வாக்கு வயது (1), உறுப்பு 21A (2) அல்ல."}
        },
        tip_en="TNPSC Tip: Core Amendment matches: 42nd (FDs), 44th (Prop 300A), 61st (Voting 18), 86th (RTE 21A).",
        tip_ta="TNPSC குறிப்பு: முக்கிய திருத்தப் பொருத்தங்கள்: 42வது (FDகள்), 44வது (சொத்து 300A), 61வது (வாக்கு 18), 86வது (RTE 21A).",
        rev_en="42nd (FDs), 44th (Art 300A), 61st (Voting 18), 86th (Art 21A).",
        rev_ta="42வது (FDகள்), 44வது (உறுப்பு 300A), 61வது (வாக்கு 18), 86வது (உறுப்பு 21A).",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Remember", est_sec=60, pyq_sim="High", tags=["Amendments", "42nd Amendment", "44th Amendment", "61st Amendment", "86th Amendment", "Match the Following"]
    ))

    # Q81 - Chronology - Medium - Ans D
    qs.append(make_q(
        q_id="SF_GT_081", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="Chronology",
        q_en="Arrange the following official judicial decisions defining the scope of Article 368 and Fundamental Rights in chronological order:\n1. Shankari Prasad Case\n2. Sajjan Singh Case\n3. Golaknath Case\n4. Kesavananda Bharati Case",
        q_ta="உறுப்பு 368 மற்றும் அடிப்படை உரிமைகளின் வரம்பை வரையறுக்கும் பின்வரும் அதிகாரப்பூர்வ நீதித்துறை முடிவுகளை காலவரிசைப்படி வரிசைப்படுத்தவும்:\n1. சங்கரி பிரசாத் வழக்கு\n2. சஜ்ஜன் சிங் வழக்கு\n3. கோலக்நாத் வழக்கு\n4. கேசவாநந்த பாரதி வழக்கு",
        opts_en=[
            "1 - 3 - 2 - 4",
            "2 - 1 - 3 - 4",
            "1 - 2 - 4 - 3",
            "1 - 2 - 3 - 4"
        ],
        opts_ta=[
            "1 - 3 - 2 - 4",
            "2 - 1 - 3 - 4",
            "1 - 2 - 4 - 3",
            "1 - 2 - 3 - 4"
        ],
        correct_ans="D",
        exp_en="Historical Context: Evolution of judicial stance on Article 368 amending power vs Fundamental Rights.\nReason:\n1. Shankari Prasad Case: 1951 (Parliament can amend FRs).\n2. Sajjan Singh Case: 1965 (Reaffirmed Shankari Prasad decision).\n3. Golaknath Case: 1967 (FRs are transcendental and cannot be amended).\n4. Kesavananda Bharati Case: 1973 (Basic Structure Doctrine).\nSequence: 1 (1951) -> 2 (1965) -> 3 (1967) -> 4 (1973).",
        exp_ta="வரலாற்றுப் பின்னணி: உறுப்பு 368 திருத்தும் அதிகாரம் vs அடிப்படை உரிமைகள் மீதான நீதித்துறை நிலப்பாட்டின் வளர்ச்சி.\nகாரணம்:\n1. சங்கரி பிரசாத் வழக்கு: 1951 (நாடாளுமன்றம் FRகளை திருத்தலாம்).\n2. சஜ்ஜன் சிங் வழக்கு: 1965 (சங்கரி பிரசாத் முடிவை மீண்டும் உறுதிப்படுத்தியது).\n3. கோலக்நாத் வழக்கு: 1967 (FRகள் புனிதமானவை, திருத்த முடியாது).\n4. கேசவாநந்த பாரதி வழக்கு: 1973 (அடிப்படை கட்டமைப்பு கோட்பாடு).\nவரிசை: 1 (1951) -> 2 (1965) -> 3 (1967) -> 4 (1973).",
        wno_dict={
            "A": {"en": "Incorrect. Sajjan Singh (1965) came BEFORE Golaknath (1967).", "ta": "தவறு. சஜ்ஜன் சிங் (1965) கோலக்நாத்திற்கு (1967) முன்பே வந்தது."},
            "B": {"en": "Incorrect. Shankari Prasad (1951) came BEFORE Sajjan Singh (1965).", "ta": "தவறு. சங்கரி பிரசாத் (1951) சஜ்ஜன் சிங்கிற்கு (1965) முன்பே வந்தது."},
            "C": {"en": "Incorrect. Golaknath (1967) came BEFORE Kesavananda (1973).", "ta": "தவறு. கோலக்நாத் (1967) கேசவாநந்தாவிற்கு (1973) முன்பே வந்தது."},
            "D": {"en": "Correct. 1 (1951) -> 2 (1965) -> 3 (1967) -> 4 (1973).", "ta": "சரி. 1 (1951) -> 2 (1965) -> 3 (1967) -> 4 (1973)."}
        },
        tip_en="TNPSC Tip: Article 368 Jurisprudence Sequence: Shankari Prasad (1951) -> Sajjan Singh (1965) -> Golaknath (1967) -> Kesavananda (1973).",
        tip_ta="TNPSC குறிப்பு: உறுப்பு 368 வழக்கு வரிசை: சங்கரி பிரசாத் (1951) -> சஜ்ஜன் சிங் (1965) -> கோலக்நாத் (1967) -> கேசவாநந்தா (1973).",
        rev_en="Amending Power Timeline: Shankari Prasad (1951) -> Sajjan Singh (1965) -> Golaknath (1967) -> Kesavananda (1973).",
        rev_ta="திருத்தும் அதிகார காலவரிசை: சங்கரி பிரசாத் (1951) -> சஜ்ஜன் சிங் (1965) -> கோலக்நாத் (1967) -> கேசவாநந்தா (1973).",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Analyze", est_sec=60, pyq_sim="High", tags=["Chronology", "Article 368", "Landmark Cases", "Shankari Prasad", "Golaknath"]
    ))

    # Q82 - Direct MCQ - Easy - Ans B
    qs.append(make_q(
        q_id="SF_GT_082", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Easy", question_type="Direct MCQ",
        q_en="Under Article 352, on which of the following grounds can a National Emergency NOT be declared?",
        q_ta="உறுப்பு 352 இன் கீழ், பின்வரும் எந்தக் காரணத்தின் அடிப்படையில் தேசிய அவசரநிலையை அறிவிக்க முடியாது?",
        opts_en=[
            "War",
            "Internal Disturbance",
            "External Aggression",
            "Armed Rebellion"
        ],
        opts_ta=[
            "போர்",
            "உள்நாட்டு அமைதியின்மை",
            "வெளியார் ஆக்கிரமிப்பு",
            "ஆயுதமேந்திய கிளர்ச்சி"
        ],
        correct_ans="B",
        exp_en="Historical Context: The phrase 'internal disturbance' was exploited during the 1975 emergency.\nReason: The 44th Constitutional Amendment Act, 1978 substituted 'armed rebellion' for 'internal disturbance'. Hence, 'internal disturbance' is NO LONGER a valid ground for declaring National Emergency under Article 352.\nConstitutional Impact: Restricts executive discretion in proclaiming emergency.\nExam Trap: Valid grounds today are: War, External Aggression, Armed Rebellion. 'Internal disturbance' was removed in 1978.\nMemory Trick: Internal disturbance = Deleted in 1978.",
        exp_ta="வரலாற்றுப் பின்னணி: 'உள்நாட்டு அமைதியின்மை' என்ற சொல் 1975 அவசரநிலையின் போது தவறாகப் பயன்படுத்தப்பட்டது.\nகாரணம்: 44வது அரசியலமைப்பு திருத்தச் சட்டம், 1978 'உள்நாட்டு அமைதியின்மை' என்பதற்குப் பதிலாக 'ஆயுதமேந்திய கிளர்ச்சி' என்பதை மாற்றியது. எனவே, 'உள்நாட்டு அமைதியின்மை' என்பது உறுப்பு 352 இன் கீழ் தேசிய அவசரநிலையை அறிவிப்பதற்கான செல்லுபடியாகும் காரணம் அல்ல.\nஅரசியலமைப்பு தாக்கம்: அவசரநிலையை அறிவிப்பதில் நிர்வாக விருப்பத்தினைக் கட்டுப்படுத்துகிறது.\nதேர்வுப் பொறி: இன்று செல்லுபடியாகும் காரணங்கள்: போர், வெளியார் ஆக்கிரமிப்பு, ஆயுதமேந்திய கிளர்ச்சி. 'உள்நாட்டு அமைதியின்மை' 1978 இல் நீக்கப்பட்டது.\nநினைவுச் சூத்திரம்: உள்நாட்டு அமைதியின்மை = 1978 இல் நீக்கப்பட்டது.",
        wno_dict={
            "A": {"en": "Incorrect. 'War' is a valid ground under Art 352.", "ta": "தவறு. 'போர்' உறுப்பு 352 இன் கீழ் செல்லுபடியாகும் காரணம்."},
            "B": {"en": "Correct. 'Internal Disturbance' was deleted by 44th Amendment 1978 and is NO LONGER a ground.", "ta": "சரி. 'உள்நாட்டு அமைதியின்மை' 44வது திருத்தம் 1978 மூலம் நீக்கப்பட்டது மற்றும் இப்போது ஒரு காரணம் அல்ல."},
            "C": {"en": "Incorrect. 'External Aggression' is a valid ground under Art 352.", "ta": "தவறு. 'வெளியார் ஆக்கிரமிப்பு' உறுப்பு 352 இன் கீழ் செல்லுபடியாகும் காரணம்."},
            "D": {"en": "Incorrect. 'Armed Rebellion' is a valid ground under Art 352.", "ta": "தவறு. 'ஆயுதமேந்திய கிளர்ச்சி' உறுப்பு 352 இன் கீழ் செல்லுபடியாகும் காரணம்."}
        },
        tip_en="TNPSC Tip: Valid grounds for Art 352 National Emergency: War, External Aggression, Armed Rebellion. ('Internal Disturbance' was deleted in 1978).",
        tip_ta="TNPSC குறிப்பு: உறுப்பு 352 தேசிய அவசரநிலைக்கான காரணங்கள்: போர், வெளியார் ஆக்கிரமிப்பு, ஆயுதமேந்திய கிளர்ச்சி. ('உள்நாட்டு அமைதியின்மை' 1978 இல் நீக்கப்பட்டது).",
        rev_en="Article 352 grounds: War, External Aggression, Armed Rebellion (NOT Internal Disturbance).",
        rev_ta="உறுப்பு 352 காரணங்கள்: போர், வெளியார் ஆக்கிரமிப்பு, ஆயுதமேந்திய கிளர்ச்சி (உள்நாட்டு அமைதியின்மை அல்ல).",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Remember", est_sec=30, pyq_sim="High", tags=["National Emergency", "Article 352", "44th Amendment", "TNPSC Trap"]
    ))

    # Q83 - Conceptual - Medium - Ans D
    qs.append(make_q(
        q_id="SF_GT_083", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="Conceptual",
        q_en="What is the key difference between 'Judicial Review' and 'Judicial Activism'?",
        q_ta="'நீதித்துறை மறுஆய்வு' (Judicial Review) மற்றும் 'நீதித்துறை செயல்பாட்டுத்தன்மை' (Judicial Activism) ஆகியவற்றிற்கு இடையே உள்ள முக்கிய வேறுபாடு என்ன?",
        opts_en=[
            "Judicial Review is unconstitutional, whereas Judicial Activism is explicitly authorized by Article 368.",
            "Judicial Review applies to executive orders only, while Judicial Activism applies to state budgets only.",
            "Judicial Review is exercised only by High Courts, whereas Judicial Activism is exercised only by Subordinate Courts.",
            "Judicial Review is the constitutional power of courts to examine the validity of laws, whereas Judicial Activism is the proactive role played by judiciary to protect public interest and enforce rights beyond traditional boundaries."
        ],
        opts_ta=[
            "நீதித்துறை மறுஆய்வு அரசியலமைப்பிற்கு எதிரானது, அதே நேரத்தில் நீதித்துறை செயல்பாட்டுத்தன்மை உறுப்பு 368 ஆல் வெளிப்படையாக அங்கீகரிக்கப்பட்டுள்ளது.",
            "நீதித்துறை மறுஆய்வு நிர்வாக உத்தரவுகளுக்கு மட்டுமே பொருந்தும், அதே நேரத்தில் நீதித்துறை செயல்பாட்டுத்தன்மை மாநில வரவுசெலவுத் திட்டங்களுக்கு மட்டுமே பொருந்தும்.",
            "நீதித்துறை மறுஆய்வு உயர் நீதிமன்றங்களால் மட்டுமே பயன்படுத்தப்படுகிறது, அதே நேரத்தில் நீதித்துறை செயல்பாட்டுத்தன்மை சார்பு நீதிமன்றங்களால் மட்டுமே பயன்படுத்தப்படுகிறது.",
            "நீதித்துறை மறுஆய்வு என்பது சட்டங்களின் செல்லுபடியாகும் தன்மையை ஆய்வு செய்யும் நீதிமன்றங்களின் அரசியலமைப்பு அதிகாரமாகும், அதே நேரத்தில் நீதித்துறை செயல்பாட்டுத்தன்மை என்பது பொது நலனைப் பாதுகாக்கவும் பாரம்பரிய எல்லைகளைத் தாண்டி உரிமைகளை அமல்படுத்தவும் நீதித்துறை வகிக்கும் முனைப்பான பங்காகும்."
        ],
        correct_ans="D",
        exp_en="Historical Context: Growth of PIL (Public Interest Litigation) in the 1980s led to judicial activism in India.\nReason: Judicial Review is the core constitutional function of scrutinizing legislative/executive actions against constitutional parameters. Judicial Activism goes beyond mere review to actively formulate policy directives, issue guidelines (e.g., Vishaka guidelines), and protect rights where executive/legislature fails to act.\nConstitutional Impact: Enhances access to justice for marginalized sections.\nExam Trap: Judicial activism must not cross into 'Judicial Overreach' (usurping legislative/executive functions).",
        exp_ta="வரலாற்றுப் பின்னணி: 1980 களில் பொது நல வழக்கின் (PIL) வளர்ச்சி இந்தியாவில் நீதித்துறை செயல்பாட்டுத்தன்மைக்கு வழிவகுத்தது.\nகாரணம்: நீதித்துறை மறுஆய்வு என்பது அரசியலமைப்பு அளவுகோல்களுக்கு எதிராக சட்டமன்ற/நிர்வாக நடவடிக்கைகளை ஆராயும் முக்கிய அரசியலமைப்பு செயல்பாடாகும். நீதித்துறை செயல்பாட்டுத்தன்மை வெறும் மறுஆய்வைத் தாண்டி கொள்கை வழிகாட்டுதல்களை உருவாக்கவும், வழிகாட்டுதல்களை வெளியிடவும் (எ.கா., விசாகா வழிகாட்டுதல்கள்), நிர்வாகம்/சட்டமன்றம் செயல்படத் தவறும்போது உரிமைகளைப் பாதுகாக்கவும் முனைப்புடன் செயல்படுகிறது.\nஅரசியலமைப்பு தாக்கம்: விளிம்புநிலை பிரிவினருக்கு நீதி கிடைப்பதை அதிகரிக்கிறது.\nதேர்வுப் பொறி: நீதித்துறை செயல்பாட்டுத்தன்மை 'நீதித்துறை மீறலாக' (சட்டமன்ற/நிர்வாக செயல்பாடுகளை ஆக்கிரமித்தல்) மாறக்கூடாது.",
        wno_dict={
            "A": {"en": "Incorrect. Judicial Review is a Basic Structure feature.", "ta": "தவறு. நீதித்துறை மறுஆய்வு ஒரு அடிப்படை அமைப்பின் அம்சமாகும்."},
            "B": {"en": "Incorrect. Neither concept is restricted to budgets.", "ta": "தவறு. எந்தவொரு கருத்தும் வரவுசெலவுத் திட்டங்களுக்கு வரம்பிற்குட்பட்டது அல்ல."},
            "C": {"en": "Incorrect. Both SC and HCs exercise Judicial Review and Judicial Activism.", "ta": "தவறு. உச்ச நீதிமன்றம் மற்றும் உயர் நீதிமன்றங்கள் இரண்டும் நீதித்துறை மறுஆய்வு மற்றும் செயல்பாட்டுத்தன்மையைப் பயன்படுத்துகின்றன."},
            "D": {"en": "Correct. Judicial Review = Examining law validity; Judicial Activism = Proactive role protecting public interest and rights.", "ta": "சரி. நீதித்துறை மறுஆய்வு = சட்டத்தின் செல்லுபடியை ஆய்வு செய்தல்; நீதித்துறை செயல்பாட்டுத்தன்மை = பொது நலன் மற்றும் உரிமைகளைப் பாதுகாக்கும் முனைப்பான பங்கு."}
        },
        tip_en="TNPSC Tip: Judicial Review = Checking law validity against Constitution; Judicial Activism = Proactive judicial intervention (PIL) for public welfare.",
        tip_ta="TNPSC குறிப்பு: நீதித்துறை மறுஆய்வு = அரசியலமைப்பிற்கு எதிராக சட்ட செல்லுபடியைச் சரிபார்த்தல்; நீதித்துறை செயல்பாட்டுத்தன்மை = பொது நலனுக்கான முனைப்பான நீதித்துறை தலையீடு (PIL).",
        rev_en="Judicial Review (Law examination) vs Judicial Activism (Proactive intervention/PIL).",
        rev_ta="நீதித்துறை மறுஆய்வு (சட்ட ஆய்வு) vs நீதித்துறை செயல்பாட்டுத்தன்மை (முனைப்பான தலையீடு/PIL).",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Understand", est_sec=60, pyq_sim="High", tags=["Judicial Review", "Judicial Activism", "PIL"]
    ))

    # Q84 - Statement-Based - Medium - Ans B
    qs.append(make_q(
        q_id="SF_GT_084", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="Statement-Based",
        q_en="Consider the following statements regarding the Supremacy of the Constitution in India:\n1. The Constitution is the Supreme Law of the Land (Lex Loci) from which all organs of the state derive authority.\n2. Any law passed by Parliament or State Legislature that violates the Constitution can be declared void by the judiciary.\n3. The Preamble is the sole supreme provision of the Constitution that overrides all other Articles.\n\nWhich of the statements given above are CORRECT?",
        q_ta="இந்தியாவில் அரசியலமைப்பின் மேலாதிக்கம் (Supremacy of the Constitution) தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. அரசியலமைப்பு என்பது நாட்டின் மிக உயர்ந்த சட்டமாகும் (Lex Loci), இதிலிருந்தே அரசின் அனைத்து அங்கங்களும் அதிகாரத்தைப் பெறுகின்றன.\n2. அரசியலமைப்பை மீறும் வகையில் நாடாளுமன்றம் அல்லது மாநில சட்டமன்றத்தால் நிறைவேற்றப்படும் எந்தவொரு சட்டமும் நீதித்துறையால் செல்லாதது என அறிவிக்கப்படலாம்.\n3. முகவுரை என்பது மற்ற அனைத்து உறுப்புகளையும் மிஞ்சும் அரசியலமைப்பின் ஒரே உயரிய விதியாகும்.\n\nமேற்கூறிய கூற்றுகளில் எது சரியானவை?",
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
        exp_en="Historical Context: Constitutional Supremacy is a cornerstone of Indian democracy and a part of the Basic Structure.\nReason:\nStatement 1 is correct: Constitution is supreme law; Legislature, Executive, Judiciary operate within its limits.\nStatement 2 is correct: Under Article 13 & judicial review, unconstitutional laws are declared void.\nStatement 3 is INCORRECT: Preamble is an introduction/key to the Constitution, but it does NOT override specific substantive Articles.\nConstitutional Impact: Ensures legal sovereignty rests in the Constitution.\nExam Trap: Preamble is part of Constitution, but does NOT override clear statutory/article text.",
        exp_ta="வரலாற்றுப் பின்னணி: அரசியலமைப்பு மேலாதிக்கம் இந்திய ஜனநாயகத்தின் ஒரு முக்கிய தூண் மற்றும் அடிப்படை அமைப்பின் ஒரு பகுதியாகும்.\nகாரணம்:\nகூற்று 1 சரி: அரசியலமைப்பு உயரிய சட்டம்; சட்டமன்றம், நிர்வாகத் துறை, நீதித்துறை ஆகியவை அதன் எல்லைக்குள் செயல்படுகின்றன.\nகூற்று 2 சரி: உறுப்பு 13 & நீதித்துறை மறுஆய்வின் கீழ், அரசியலமைப்பிற்கு எதிரான சட்டங்கள் செல்லாதவை என அறிவிக்கப்படுகின்றன.\nகூற்று 3 தவறு: முகவுரை என்பது அரசியலமைப்பிற்கான ஒரு அறிமுகம்/சாவி, ஆனால் அது குறிப்பிட்ட உறுப்புகளை மிஞ்சாது.\nஅரசியலமைப்பு தாக்கம்: சட்டப்பூர்வ இறையாண்மை அரசியலமைப்பில் உள்ளதை உறுதி செய்கிறது.\nதேர்வுப் பொறி: முகவுரை அரசியலமைப்பின் ஒரு பகுதி, ஆனால் அது உறுப்பு உரையை மிஞ்சாது.",
        wno_dict={
            "A": {"en": "Incorrect. Statement 3 is false (Preamble does not override substantive Articles).", "ta": "தவறு. கூற்று 3 தவறு (முகவுரை குறிப்பிட்ட உறுப்புகளை மிஞ்சாது)."},
            "B": {"en": "Correct. Statements 1 and 2 are correct; Statement 3 is false.", "ta": "சரி. கூற்றுகள் 1 மற்றும் 2 சரி; கூற்று 3 தவறு."},
            "C": {"en": "Incorrect. Statement 3 is false.", "ta": "தவறு. கூற்று 3 தவறு."},
            "D": {"en": "Incorrect. Statement 3 is false.", "ta": "தவறு. கூற்று 3 தவறு."}
        },
        tip_en="TNPSC Tip: Constitutional Supremacy = Constitution is the Supreme Law; Legislature & Executive derive power from it and are bound by it.",
        tip_ta="TNPSC குறிப்பு: அரசியலமைப்பு மேலாதிக்கம் = அரசியலமைப்பு உயரிய சட்டம்; சட்டமன்றமும் நிர்வாகத் துறையும் அதிலிருந்தே அதிகாரத்தைப் பெறுகின்றன.",
        rev_en="Constitutional Supremacy: Lex Loci (Supreme Law of the Land), Basic Structure feature.",
        rev_ta="அரசியலமைப்பு மேலாதிக்கம்: நாட்டின் உயரிய சட்டம், அடிப்படை அமைப்பின் அம்சம்.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Analyze", est_sec=60, pyq_sim="High", tags=["Constitutional Supremacy", "Basic Structure", "Lex Loci"]
    ))

    # Q85 - Hard / Analytical - Hard - Ans D
    qs.append(make_q(
        q_id="SF_GT_085", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Hard", question_type="Hard / Analytical",
        q_en="Which of the following constitutional provisions underscores the concept of 'Political Justice' guaranteed in the Preamble?",
        q_ta="முகவுரையில் உத்தரவாதம் அளிக்கப்பட்ட 'அரசியல் நீதி' (Political Justice) என்ற கருத்தை பின்வரும் அரசியலமைப்பு விதிகளில் எது அடிக்கோடிட்டுக் காட்டுகிறது?",
        opts_en=[
            "Equal pay for equal work under Article 39(d)",
            "Free legal aid under Article 39A",
            "Promotion of educational interests of SCs/STs under Article 46",
            "Universal Adult Franchise under Article 326 and non-discrimination in voter registration under Article 325"
        ],
        opts_ta=[
            "உறுப்பு 39(d) இன் கீழ் சம வேலைக்கு சம ஊதியம்",
            "உறுப்பு 39A இன் கீழ் இலவச சட்ட உதவி",
            "உறுப்பு 46 இன் கீழ் SC/ST கல்வியின் மேம்பாடு",
            "உறுப்பு 326 இன் கீழ் உலகளாவிய வயதுவந்தோர் வாக்குரிமை மற்றும் உறுப்பு 325 இன் கீழ் வாக்காளர் பதிவில் பாகுபாடின்மை"
        ],
        correct_ans="D",
        exp_en="Historical Context: Preamble promises Justice - Social, Economic, and Political.\nReason: Political Justice means all citizens should have equal political rights, equal access to all political offices, and equal voice in the government. Article 326 (Universal Adult Franchise) and Article 325 (No exclusion from electoral rolls on grounds of religion, race, caste, or sex) directly embody Political Justice.\nConstitutional Impact: Ensures democratic equality regardless of wealth or status.\nExam Trap: Art 39(d) = Economic/Social Justice; Art 39A = Social/Legal Justice; Arts 325 & 326 = Political Justice.",
        exp_ta="வரலாற்றுப் பின்னணி: முகவுரை நீதி - சமூக, பொருளாதார, அரசியல் என உறுதியளிக்கிறது.\nகாரணம்: அரசியல் நீதி என்பது அனைத்து குடிமக்களுக்கும் சமமான அரசியல் உரிமைகள், அனைத்து அரசியல் பதவிகளுக்கும் சமமான அணுகல் மற்றும் அரசாங்கத்தில் சமமான குரல் இருக்க வேண்டும் என்பதாகும். உறுப்பு 326 (உலகளாவிய வயதுவந்தோர் வாக்குரிமை) மற்றும் உறுப்பு 325 (மதம், இனம், சாதி அல்லது பாலினத்தின் அடிப்படையில் வாக்காளர் பட்டியலிலிருந்து விலக்கப்படாமை) நேரடியாக அரசியல் நீதியைப் பிரதிபலிக்கின்றன.\nஅரசியலமைப்பு தாக்கம்: செல்வம் அல்லது அந்தஸ்து பாராமல் ஜனநாயக சமத்துவத்தை உறுதி செய்கிறது.\nதேர்வுப் பொறி: உறுப்பு 39(d) = பொருளாதார/சமூக நீதி; உறுப்பு 39A = சமூக/சட்ட நீதி; உறுப்புகள் 325 & 326 = அரசியல் நீதி.",
        wno_dict={
            "A": {"en": "Incorrect. Article 39(d) represents Economic/Social Justice.", "ta": "தவறு. உறுப்பு 39(d) பொருளாதார/சமூக நீதியைக் குறிக்கிறது."},
            "B": {"en": "Incorrect. Article 39A represents Legal/Social Justice.", "ta": "தவறு. உறுப்பு 39A சட்ட/சமூக நீதியைக் குறிக்கிறது."},
            "C": {"en": "Incorrect. Article 46 represents Social Justice.", "ta": "தவறு. உறுப்பு 46 சமூக நீதியைக் குறிக்கிறது."},
            "D": {"en": "Correct. Articles 325 and 326 ensure equal political rights, access, and voting power (Political Justice).", "ta": "சரி. உறுப்புகள் 325 மற்றும் 326 சமமான அரசியல் உரிமைகள், அணுகல் மற்றும் வாக்கு அதிகாரத்தை உறுதி செய்கின்றன (அரசியல் நீதி)."}
        },
        tip_en="TNPSC Tip: Political Justice = Equal access to political offices and voting power (Arts 325 & 326).",
        tip_ta="TNPSC குறிப்பு: அரசியல் நீதி = அரசியல் பதவிகள் மற்றும் வாக்கு அதிகாரத்திற்கான சமமான அணுகல் (உறுப்புகள் 325 & 326).",
        rev_en="Political Justice = Articles 325 & 326 (Universal Adult Franchise & Equal Electoral Access).",
        rev_ta="அரசியல் நீதி = உறுப்புகள் 325 & 326 (உலகளாவிய வயதுவந்தோர் வாக்குரிமை & சமமான வாக்காளர் அணுகல்).",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Analyze", est_sec=60, pyq_sim="High", tags=["Political Justice", "Article 325", "Article 326", "Preamble"]
    ))

    # Q86 - Direct MCQ - Easy - Ans B
    qs.append(make_q(
        q_id="SF_GT_086", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Easy", question_type="Direct MCQ",
        q_en="Under Article 356, what is the maximum permissible period for which President's Rule can be extended in a State with parliamentary approval every six months?",
        q_ta="உறுப்பு 356 இன் கீழ், ஒவ்வொரு ஆறு மாதங்களுக்கும் நாடாளுமன்ற ஒப்புதலுடன் ஒரு மாநிலத்தில் குடியரசுத் தலைவர் ஆட்சியை நீட்டிக்கக்கூடிய அதிகபட்ச அனுமதிக்கப்பட்ட காலம் என்ன?",
        opts_en=[
            "One year",
            "Three years",
            "Five years",
            "Indefinite period"
        ],
        opts_ta=[
            "ஒரு ஆண்டு",
            "மூன்று ஆண்டுகள்",
            "ஐந்து ஆண்டுகள்",
            "வரம்பற்ற காலம்"
        ],
        correct_ans="B",
        exp_en="Historical Context: 44th Amendment 1978 introduced restrictions to prevent long-term President's Rule.\nReason: President's Rule under Art 356 can be extended for 6 months at a time up to a MAXIMUM of 3 years. Beyond 1 year, extension requires two conditions: (1) National Emergency in operation; (2) EC certifies election cannot be held.\nConstitutional Impact: Protects state democratic governance from prolonged central suspension.\nExam Trap: National Emergency (352) = Indefinite extension; President's Rule (356) = Maximum 3 years limit.\nMemory Trick: Art 356 = Max 3 Years Limit.",
        exp_ta="வரலாற்றுப் பின்னணி: 44வது திருத்தம் 1978 நீண்ட கால குடியரசுத் தலைவர் ஆட்சியைத் தடுக்கக் கட்டுப்பாடுகளை அறிமுகப்படுத்தியது.\nகாரணம்: உறுப்பு 356 இன் கீழ் குடியரசுத் தலைவர் ஆட்சி ஒரு நேரத்தில் 6 மாதங்களுக்கு அதிகபட்சமாக 3 ஆண்டுகள் வரை நீட்டிக்கப்படலாம். 1 ஆண்டுக்கு மேல் நீட்டிக்க இரண்டு நிபந்தனைகள் தேவை: (1) தேசிய அவசரநிலை அமலில் இருப்பது; (2) தேர்தல் நடத்த முடியாது என EC சான்றளிப்பது.\nஅரசியலமைப்பு தாக்கம்: நீண்டகால மத்திய நிறுத்தத்திலிருந்து மாநில ஜனநாயக ஆட்சியைப் பாதுகாக்கிறது.\nதேர்வுப் பொறி: தேசிய அவசரநிலை (352) = வரம்பற்ற நீட்டிப்பு; குடியரசுத் தலைவர் ஆட்சி (356) = அதிகபட்சம் 3 ஆண்டுகள் வரம்பு.\nநினைவுச் சூத்திரம்: உறுப்பு 356 = அதிகபட்சம் 3 ஆண்டுகள் வரம்பு.",
        wno_dict={
            "A": {"en": "Incorrect. One year is the limit beyond which special conditions apply, not the absolute maximum.", "ta": "தவறு. ஒரு ஆண்டு என்பது சிறப்பு நிபந்தனைகள் பொருந்தும் வரம்பு, அதிகபட்ச வரம்பு அல்ல."},
            "B": {"en": "Correct. Maximum period of President's Rule under Article 356 is 3 years.", "ta": "சரி. உறுப்பு 356 இன் கீழ் குடியரசுத் தலைவர் ஆட்சியின் அதிகபட்ச காலம் 3 ஆண்டுகள்."},
            "C": {"en": "Incorrect. Five years is wrong.", "ta": "தவறு. ஐந்து ஆண்டுகள் என்பது தவறு."},
            "D": {"en": "Incorrect. Indefinite period applies to National Emergency (Art 352), not Art 356.", "ta": "தவறு. வரம்பற்ற காலம் தேசிய அவசரநிலைக்குப் (உறுப்பு 352) பொருந்தும், உறுப்பு 356 க்கு அல்ல."}
        },
        tip_en="TNPSC Trap: Art 352 (National Emergency) = Indefinite max limit. Art 356 (President's Rule) = Max 3 Years limit.",
        tip_ta="TNPSC பொறி: உறுப்பு 352 (தேசிய அவசரநிலை) = வரம்பற்ற அதிகபட்ச வரம்பு. உறுப்பு 356 (குடியரசுத் தலைவர் ஆட்சி) = அதிகபட்சம் 3 ஆண்டுகள் வரம்பு.",
        rev_en="President's Rule (Art 356): Maximum limit = 3 Years (with parliamentary approval every 6 months).",
        rev_ta="குடியரசுத் தலைவர் ஆட்சி (உறுப்பு 356): அதிகபட்ச வரம்பு = 3 ஆண்டுகள் (ஒவ்வொரு 6 மாதங்களுக்கும் நாடாளுமன்ற ஒப்புதலுடன்).",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Remember", est_sec=30, pyq_sim="High", tags=["President's Rule", "Article 356", "Emergency Limits"]
    ))

    # Q87 - Conceptual - Medium - Ans C
    qs.append(make_q(
        q_id="SF_GT_087", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="Conceptual",
        q_en="What is the fundamental objective behind incorporating the 'Directive Principles of State Policy' in Part IV of the Indian Constitution?",
        q_ta="இந்திய அரசியலமைப்பின் பகுதி IV இல் 'அரசு நெறிமுறைப்படுத்தும் கோட்பாடுகளை' உள்ளடக்கியதன் அடிப்படை நோக்கம் என்ன?",
        opts_en=[
            "To establish a Police State focused exclusively on revenue collection.",
            "To grant absolute autocratic powers to the Prime Minister during economic crises.",
            "To establish social and economic democracy and create a Welfare State.",
            "To override Fundamental Rights whenever executive ordinances are issued."
        ],
        opts_ta=[
            "வருவாய் வசூலில் மட்டுமே கவனம் செலுத்தும் போலீஸ் அரசை நிறுவுவதற்கு.",
            "பொருளாதார நெருக்கடிகளின் போது பிரதமருக்கு முழுமையான தன்னிச்சையான அதிகாரங்களை வழங்குவதற்கு.",
            "சமூக மற்றும் பொருளாதார ஜனநாயகத்தை நிறுவி ஒரு நலன்புரி அரசை (Welfare State) உருவாக்குவதற்கு.",
            "நிர்வாக அவசரச் சட்டங்கள் பிறப்பிக்கப்படும் போதெல்லாம் அடிப்படை உரிமைகளை மீறுவதற்கு."
        ],
        correct_ans="C",
        exp_en="Historical Context: Fundamental Rights guarantee Political Democracy; DPSPs guarantee Social and Economic Democracy.\nReason: As Dr. B.R. Ambedkar noted, political democracy without social and economic democracy is meaningless. Part IV aims to secure social and economic justice, reducing inequality and establishing a Welfare State.\nConstitutional Impact: Directs government policy toward socio-economic welfare.\nExam Trap: Fundamental Rights = Political Democracy; DPSPs = Social & Economic Democracy.\nMemory Trick: FRs = Political Democracy; DPSPs = Socio-Economic Democracy.",
        exp_ta="வரலாற்றுப் பின்னணி: அடிப்படை உரிமைகள் அரசியல் ஜனநாயகத்திற்கு உத்தரவாதம் அளிக்கின்றன; DPSP-கள் சமூக மற்றும் பொருளாதார ஜனநாயகத்திற்கு உத்தரவாதம் அளிக்கின்றன.\nகாரணம்: டாக்டர் பி.ஆர். அம்பேத்கர் குறிப்பிட்டது போல, சமூக மற்றும் பொருளாதார ஜனநாயகம் இல்லாத அரசியல் ஜனநாயகம் அர்த்தமற்றது. பகுதி IV சமூக மற்றும் பொருளாதார நீதியைப் பாதுகாப்பதை நோக்கமாகக் கொண்டுள்ளது, ஏற்றத்தாழ்வைக் குறைத்து ஒரு நலன்புரி அரசை உருவாக்குகிறது.\nஅரசியலமைப்பு தாக்கம்: சமூக-பொருளாதார நலனை நோக்கிய அரசு கொள்கையை இயக்குகிறது.\nதேர்வுப் பொறி: அடிப்படை உரிமைகள் = அரசியல் ஜனநாயகம்; DPSP-கள் = சமூக & பொருளாதார ஜனநாயகம்.\nநினைவுச் சூத்திரம்: FR = அரசியல் ஜனநாயகம்; DPSP = சமூக-பொருளாதார ஜனநாயகம்.",
        wno_dict={
            "A": {"en": "Incorrect. DPSPs establish a Welfare State, not a Police State.", "ta": "தவறு. DPSP-கள் நலன்புரி அரசை நிறுவுகின்றன, போலீஸ் அரசை அல்ல."},
            "B": {"en": "Incorrect. DPSPs do not grant autocratic powers to PM.", "ta": "தவறு. DPSP-கள் பிரதமருக்கு தன்னிச்சையான அதிகாரங்களை வழங்குவதில்லை."},
            "C": {"en": "Correct. Fundamental objective of DPSPs is to establish social & economic democracy and a Welfare State.", "ta": "சரி. DPSP-களின் அடிப்படை நோக்கம் சமூக & பொருளாதார ஜனநாயகத்தை நிறுவி ஒரு நலன்புரி அரசை உருவாக்குவதாகும்."},
            "D": {"en": "Incorrect. DPSPs do not override FRs automatically.", "ta": "தவறு. DPSP-கள் தானாகவே FR-களை மீறுவதில்லை."}
        },
        tip_en="TNPSC Tip: Fundamental Rights = Political Democracy; DPSP = Social & Economic Democracy (Welfare State).",
        tip_ta="TNPSC குறிப்பு: அடிப்படை உரிமைகள் = அரசியல் ஜனநாயகம்; DPSP = சமூக & பொருளாதார ஜனநாயகம் (நலன்புரி அரசு).",
        rev_en="DPSP objective: Social and Economic Democracy -> Welfare State.",
        rev_ta="DPSP நோக்கம்: சமூக மற்றும் பொருளாதார ஜனநாயகம் -> நலன்புரி அரசு.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Understand", est_sec=45, pyq_sim="High", tags=["DPSP", "Welfare State", "Social and Economic Democracy"]
    ))

    # Q88 - Statement-Based - Medium - Ans A
    qs.append(make_q(
        q_id="SF_GT_088", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="Statement-Based",
        q_en="Consider the following statements regarding the Finance Commission of India (Article 280):\n1. It is a Quasi-Judicial body constituted by the President of India every fifth year.\n2. Its recommendations regarding distribution of taxes and grants-in-aid are advisory in nature and not legally binding on the Government.\n3. The Chairman of the Finance Commission must be a retired Chief Justice of India.\n\nWhich of the statements given above are CORRECT?",
        q_ta="இந்திய நிதி ஆணையம் (உறுப்பு 280) தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது இந்தியக் குடியரசுத் தலைவரால் ஒவ்வொரு ஐந்தாம் ஆண்டிலும் அமைக்கப்படும் ஒரு அரை-நீதிமன்ற (Quasi-Judicial) அமைப்பாகும்.\n2. வரிகள் பகிர்வு மற்றும் மானியங்கள் குறித்த அதன் பரிந்துரைகள் ஆலோசனைக் இயல்புடையவை மற்றும் அரசாங்கத்தைச் சட்டப்பூர்வமாகக் கட்டுப்படுத்தாது.\n3. நிதி ஆணையத்தின் தலைவர் ஓய்வு பெற்ற இந்தியத் தலைமை நீதிபதியாக இருக்க வேண்டும்.\n\nமேற்கூறிய கூற்றுகளில் எது சரியானவை?",
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
        correct_ans="A",
        exp_en="Historical Context: Finance Commission balances central-state fiscal relations as a constitutional quasi-judicial body.\nReason:\nStatement 1 is correct: Quasi-judicial body constituted every 5 years under Art 280.\nStatement 2 is correct: Recommendations are advisory in nature; Constitution does not make them binding.\nStatement 3 is INCORRECT: The Chairman must be a person having experience in public affairs (not necessarily a retired CJI). The 4 members come from judicial, financial, economic backgrounds.\nConstitutional Impact: Ensures equitable fiscal devolution.\nExam Trap: FC recommendations are ADVISORY, not binding.",
        exp_ta="வரலாற்றுப் பின்னணி: நிதி ஆணையம் ஒரு அரசியலமைப்பு அரை-நீதிமன்ற அமைப்பாக மத்திய-மாநில நிதி உறவுகளை சமநிலைப்படுத்துகிறது.\nகாரணம்:\nகூற்று 1 சரி: உறுப்பு 280 இன் கீழ் ஒவ்வொரு 5 ஆண்டிற்கும் அமைக்கப்படும் அரை-நீதிமன்ற அமைப்பு.\nகூற்று 2 சரி: பரிந்துரைகள் ஆலோசனைக் இயல்புடையவை; அரசியலமைப்பு அவற்றை கட்டுப்படுத்துவதாக மாற்றவில்லை.\nகூற்று 3 தவறு: தலைவர் பொது விவகாரங்களில் அனுபவம் வாய்ந்த ஒரு நபராக இருக்க வேண்டும் (ஓய்வு பெற்ற CJI ஆக இருக்க வேண்டிய அவசியமில்லை). 4 உறுப்பினர்கள் நீதித்துறை, நிதி, பொருளாதாரப் பின்னணியில் இருந்து வருகிறார்கள்.\nஅரசியலமைப்பு தாக்கம்: நியாயமான நிதிப் பகிர்வை உறுதி செய்கிறது.\nதேர்வுப் பொறி: FC பரிந்துரைகள் ஆலோசனையானவை, கட்டுப்படுத்துபவை அல்ல.",
        wno_dict={
            "A": {"en": "Correct. Statements 1 and 2 are correct; Statement 3 is false (Chairman needs experience in public affairs, not CJI).", "ta": "சரி. கூற்றுகள் 1 மற்றும் 2 சரி; கூற்று 3 தவறு (தலைவருக்கு பொது விவகாரங்களில் அனுபவம் தேவை, CJI அல்ல)."},
            "B": {"en": "Incorrect. Statement 3 is false.", "ta": "தவறு. கூற்று 3 தவறு."},
            "C": {"en": "Incorrect. Statement 3 is false.", "ta": "தவறு. கூற்று 3 தவறு."},
            "D": {"en": "Incorrect. Statement 3 is false.", "ta": "தவறு. கூற்று 3 தவறு."}
        },
        tip_en="TNPSC Tip: Finance Commission (Art 280) = Quasi-judicial body, advisory recommendations, Chairman = experience in public affairs.",
        tip_ta="TNPSC குறிப்பு: நிதி ஆணையம் (உறுப்பு 280) = அரை-நீதிமன்ற அமைப்பு, ஆலோசனைக் பரிந்துரைகள், தலைவர் = பொது விவகாரங்களில் அனுபவம்.",
        rev_en="Finance Commission: Quasi-judicial, advisory role, constituted every 5 years by President.",
        rev_ta="நிதி ஆணையம்: அரை-நீதிமன்றம், ஆலோசனைக் பங்கு, குடியரசுத் தலைவரால் ஒவ்வொரு 5 ஆண்டிற்கும் அமைக்கப்படுகிறது.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Analyze", est_sec=60, pyq_sim="High", tags=["Finance Commission", "Article 280", "Constitutional Bodies"]
    ))

    # Q89 - Direct MCQ - Easy - Ans D
    qs.append(make_q(
        q_id="SF_GT_089", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Easy", question_type="Direct MCQ",
        q_en="Under Article 356, a proclamation of President's Rule in a State must be approved by both Houses of Parliament within:",
        q_ta="உறுப்பு 356 இன் கீழ், ஒரு மாநிலத்தில் குடியரசுத் தலைவர் ஆட்சி அறிவிப்பு நாடாளுமன்றத்தின் இரு அவைகளாலும் எந்தக் காலத்திற்குள் அங்கீகரிக்கப்பட வேண்டும்?",
        opts_en=[
            "One month from the date of issue",
            "Six weeks from the date of issue",
            "Six months from the date of issue",
            "Two months from the date of issue"
        ],
        opts_ta=[
            "வெளியிடப்பட்ட தேதியிலிருந்து ஒரு மாதம்",
            "வெளியிடப்பட்ட தேதியிலிருந்து ஆறு வாரங்கள்",
            "வெளியிடப்பட்ட தேதியிலிருந்து ஆறு மாதங்கள்",
            "வெளியிடப்பட்ட தேதியிலிருந்து இரண்டு மாதங்கள்"
        ],
        correct_ans="D",
        exp_en="Historical Context: Approval timelines ensure legislative check on executive emergency powers.\nReason: Under Article 356(3), a proclamation of President's Rule must be approved by both Houses of Parliament within TWO MONTHS from the date of issue by a Simple Majority.\nConstitutional Impact: Prevents prolonged executive takeover of state administration without parliamentary assent.\nExam Trap: Art 352 (National Emergency) = 1 Month (Special Majority); Art 356 (President's Rule) = 2 Months (Simple Majority).\nMemory Trick: Art 352 = 1 mo; Art 356 = 2 mo.",
        exp_ta="வரலாற்றுப் பின்னணி: ஒப்புதல் காலக்கெடுகள் நிர்வாக அவசரக்கால அதிகாரங்கள் மீது நாடாளுமன்றத் தடையை உறுதி செய்கின்றன.\nகாரணம்: உறுப்பு 356(3) இன் கீழ், குடியரசுத் தலைவர் ஆட்சி அறிவிப்பு வெளியிடப்பட்ட தேதியிலிருந்து இரண்டு மாதங்களுக்குள் நாடாளுமன்றத்தின் இரு அவைகளாலும் சாதாரண பெரும்பான்மையால் அங்கீகரிக்கப்பட வேண்டும்.\nஅரசியலமைப்பு தாக்கம்: நாடாளுமன்ற ஒப்புதலின்றி மாநில நிர்வாகத்தை நீண்டகாலம் நிர்வாகம் எடுத்துக்கொள்வதைத் தடுக்கிறது.\nதேர்வுப் பொறி: உறுப்பு 352 (தேசிய அவசரநிலை) = 1 மாதம் (சிறப்பு பெரும்பான்மை); உறுப்பு 356 (குடியரசுத் தலைவர் ஆட்சி) = 2 மாதங்கள் (சாதாரண பெரும்பான்மை).\nநினைவுச் சூத்திரம்: உறுப்பு 352 = 1 மாதம்; உறுப்பு 356 = 2 மாதங்கள்.",
        wno_dict={
            "A": {"en": "Incorrect. One month applies to National Emergency under Article 352.", "ta": "தவறு. ஒரு மாதம் உறுப்பு 352 இன் கீழ் தேசிய அவசரநிலைக்குப் பொருந்தும்."},
            "B": {"en": "Incorrect. Six weeks applies to Ordinance approval after reassembly of Parliament.", "ta": "தவறு. ஆறு வாரங்கள் நாடாளுமன்றம் மீண்டும் கூடிய பிறகு அவசரச் சட்ட ஒப்புதலுக்குப் பொருந்தும்."},
            "C": {"en": "Incorrect. Six months is the period for which emergency continues once approved.", "ta": "தவறு. ஆறு மாதங்கள் என்பது ஒருமுறை அங்கீகரிக்கப்பட்ட அவசரநிலை தொடரும் காலமாகும்."},
            "D": {"en": "Correct. President's Rule proclamation must be approved within 2 months by Simple Majority.", "ta": "சரி. குடியரசுத் தலைவர் ஆட்சி அறிவிப்பு 2 மாதங்களுக்குள் சாதாரண பெரும்பான்மையால் அங்கீகரிக்கப்பட வேண்டும்."}
        },
        tip_en="TNPSC Trap: Approval limits: National Emergency (Art 352) = 1 Month; President's Rule (Art 356) = 2 Months.",
        tip_ta="TNPSC பொறி: ஒப்புதல் வரம்புகள்: தேசிய அவசரநிலை (உறுப்பு 352) = 1 மாதம்; குடியரசுத் தலைவர் ஆட்சி (உறுப்பு 356) = 2 மாதங்கள்.",
        rev_en="President's Rule approval: 2 Months, Simple Majority.",
        rev_ta="குடியரசுத் தலைவர் ஆட்சி ஒப்புதல்: 2 மாதங்கள், சாதாரண பெரும்பான்மை.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Remember", est_sec=30, pyq_sim="High", tags=["President's Rule", "Article 356", "Emergency Approval"]
    ))

    # Q90 - PYQ Pattern - Hard - Ans B
    qs.append(make_q(
        q_id="SF_GT_090", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Hard", question_type="PYQ Pattern",
        q_en="Which Article of the Indian Constitution guarantees the 'Right to Freedom of Speech and Expression' subject to reasonable restrictions under clause (2)?",
        q_ta="இந்திய அரசியலமைப்பின் எந்த உறுப்பு உட்கூறு (2) இன் கீழ் ஏதுவான வரம்புகளுக்கு உட்பட்டு 'பேச்சு மற்றும் வெளிப்பாட்டு சுதந்திரத்திற்கான உரிமையை' உத்தரவாதம் செய்கிறது?",
        opts_en=[
            "Article 14",
            "Article 19(1)(a)",
            "Article 21",
            "Article 25"
        ],
        opts_ta=[
            "உறுப்பு 14",
            "உறுப்பு 19(1)(a)",
            "உறுப்பு 21",
            "உறுப்பு 25"
        ],
        correct_ans="B",
        exp_en="Historical Context: Freedom of speech and expression is the cornerstone of democratic governance.\nReason: Article 19(1)(a) guarantees to all citizens the right to freedom of speech and expression. Article 19(2) allows reasonable restrictions on 8 grounds: Sovereignty & Integrity of India, Security of State, Friendly relations with foreign states, Public order, Decency/Morality, Contempt of court, Defamation, Incitement to offence.\nConstitutional Impact: Protects free press and democratic debate.\nExam Trap: Right to Speech is in 19(1)(a), restrictions are in 19(2).",
        exp_ta="வரலாற்றுப் பின்னணி: பேச்சு மற்றும் வெளிப்பாட்டு சுதந்திரம் ஜனநாயக ஆட்சியின் மூலைக்கல்லாகும்.\nகாரணம்: உறுப்பு 19(1)(a) அனைத்து குடிமக்களுக்கும் பேச்சு மற்றும் வெளிப்பாட்டு சுதந்திரத்திற்கான உரிமையை உத்தரவாதம் செய்கிறது. உறுப்பு 19(2) 8 காரணங்களின் கீழ் ஏதுவான வரம்புகளை அனுமதிக்கிறது: இந்தியாவின் இறையாண்மை & ஒருமைப்பாடு, அரசின் பாதுகாப்பு, வெளிநாடுகளுடனான நட்புறவு, பொது ஒழுங்கு, கண்ணியம்/ஒழுக்கம், நீதிமன்ற அவமதிப்பு, அவதூறு, குற்றத்திற்குத் தூண்டுதல்.\nஅரசியலமைப்பு தாக்கம்: சுதந்திரமான பத்திரிகை மற்றும் ஜனநாயக விவாதத்தைப் பாதுகாக்கிறது.\nதேர்வுப் பொறி: பேச்சு உரிமை 19(1)(a) இல் உள்ளது, வரம்புகள் 19(2) இல் உள்ளன.",
        wno_dict={
            "A": {"en": "Incorrect. Article 14 guarantees Equality before Law.", "ta": "தவறு. உறுப்பு 14 சட்டத்தின் முன் சமத்துவத்தை உத்தரவாதம் செய்கிறது."},
            "B": {"en": "Correct. Article 19(1)(a) guarantees Right to Freedom of Speech and Expression.", "ta": "சரி. உறுப்பு 19(1)(a) பேச்சு மற்றும் வெளிப்பாட்டு சுதந்திரத்திற்கான உரிமையை உத்தரவாதம் செய்கிறது."},
            "C": {"en": "Incorrect. Article 21 guarantees Protection of Life and Personal Liberty.", "ta": "தவறு. உறுப்பு 21 வாழ்வு மற்றும் தனிநபர் சுதந்திர பாதுகாப்பை உத்தரவாதம் செய்கிறது."},
            "D": {"en": "Incorrect. Article 25 guarantees Freedom of Conscience and Religion.", "ta": "தவறு. உறுப்பு 25 மனசாட்சி மற்றும் சமய சுதந்திரத்தை உத்தரவாதம் செய்கிறது."}
        },
        tip_en="TNPSC Tip: Article 19(1)(a) = Speech & Expression; Article 19(2) = 8 grounds of Reasonable Restrictions.",
        tip_ta="TNPSC குறிப்பு: உறுப்பு 19(1)(a) = பேச்சு & வெளிப்பாடு; உறுப்பு 19(2) = 8 ஏதுவான வரம்புகளின் காரணங்கள்.",
        rev_en="Article 19(1)(a): Freedom of Speech and Expression (subject to Art 19(2) reasonable restrictions).",
        rev_ta="உறுப்பு 19(1)(a): பேச்சு மற்றும் வெளிப்பாட்டு சுதந்திரம் (உறுப்பு 19(2) ஏதுவான வரம்புகளுக்கு உட்பட்டது).",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Remember", est_sec=30, pyq_sim="Direct PYQ", tags=["Article 19", "Freedom of Speech", "Fundamental Rights"]
    ))

    # Q91 - Conceptual - Medium - Ans D
    qs.append(make_q(
        q_id="SF_GT_091", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="Conceptual",
        q_en="Why is the Indian Parliament described as a 'Non-Sovereign Lawmaking Body' unlike the British Parliament?",
        q_ta="பிரிட்டிஷ் நாடாளுமன்றத்தைப் போலல்லாமல் இந்திய நாடாளுமன்றம் ஏன் ஒரு 'இறையாண்மையற்ற சட்டமியற்றும் அமைப்பு' (Non-Sovereign Lawmaking Body) என்று விவரிக்கப்படுகிறது?",
        opts_en=[
            "Because Indian Parliament cannot make laws on defense or foreign affairs.",
            "Because the Prime Minister can veto any law passed by Parliament without explanation.",
            "Because state governors must sign every central bill before it becomes law.",
            "Because Indian Parliament operates within the boundaries of a written Constitution, federal division of powers, fundamental rights, and judicial review."
        ],
        opts_ta=[
            "ஏனெனில் இந்திய நாடாளுமன்றம் பாதுகாப்பு அல்லது வெளியுறவு விவகாரங்களில் சட்டங்களை இயற்ற முடியாது.",
            "ஏனெனில் நாடாளுமன்றம் நிறைவேற்றும் எந்தவொரு சட்டத்தையும் பிரதமர் எவ்வித விளக்கமுமின்றி வீட்டோ செய்ய முடியும்.",
            "ஏனெனில் ஒவ்வொரு மத்திய மசோதாவும் சட்டமாவதற்கு முன் மாநில ஆளுநர்கள் கையொப்பமிட வேண்டும்.",
            "ஏனெனில் இந்திய நாடாளுமன்றம் எழுதப்பட்ட அரசியலமைப்பு, கூட்டாட்சி அதிகாரப் பகிர்வு, அடிப்படை உரிமைகள் மற்றும் நீதித்துறை மறுஆய்வு ஆகியவற்றின் எல்லைகளுக்குள் செயல்படுகிறது."
        ],
        correct_ans="D",
        exp_en="Historical Context: Synthesis of Parliamentary Sovereignty (UK) and Judicial Supremacy (USA).\nReason: British Parliament is sovereign (can make or unmake any law; no court can declare its laws invalid). Indian Parliament is NOT sovereign because: (1) India has a Written Constitution; (2) Federal distribution of powers; (3) Fundamental Rights limit legislative authority; (4) Supreme Court exercises Judicial Review.\nConstitutional Impact: Establishes Constitutional Supremacy over Parliamentary Supremacy.\nExam Trap: Parliament is NOT sovereign in India; the CONSTITUTION is supreme.",
        exp_ta="வரலாற்றுப் பின்னணி: நாடாளுமன்ற இறையாண்மை (இங்கிலாந்து) மற்றும் நீதித்துறை மேலாதிக்கம் (அமெரிக்கா) ஆகியவற்றின் இணைப்பு.\nகாரணம்: பிரிட்டிஷ் நாடாளுமன்றம் இறையாண்மை கொண்டது (எந்தச் சட்டத்தையும் உருவாக்கலாம் அல்லது ரத்து செய்யலாம்; எந்த நீதிமன்றமும் அதன் சட்டங்களைச் செல்லாததாக்க முடியாது). இந்திய நாடாளுமன்றம் இறையாண்மை கொண்டது அல்ல ஏனெனில்: (1) இந்தியா எழுதப்பட்ட அரசியலமைப்பைக் கொண்டுள்ளது; (2) கூட்டாட்சி அதிகாரப் பகிர்வு; (3) அடிப்படை உரிமைகள் சட்டமன்ற அதிகாரத்தைக் கட்டுப்படுத்துகின்றன; (4) உச்ச நீதிமன்றம் நீதித்துறை மறுஆய்வைப் பயன்படுத்துகிறது.\nஅரசியலமைப்பு தாக்கம்: நாடாளுமன்ற மேலாதிக்கத்திற்கு பதிலாக அரசியலமைப்பு மேலாதிக்கத்தை நிறுவுகிறது.\nதேர்வுப் பொறி: இந்தியாவில் நாடாளுமன்றம் இறையாண்மை கொண்டது அல்ல; அரசியலமைப்பே உயரியது.",
        wno_dict={
            "A": {"en": "Incorrect. Parliament CAN legislate on defense and foreign affairs (Union List).", "ta": "தவறு. நாடாளுமன்றம் பாதுகாப்பு மற்றும் வெளியுறவு விவகாரங்களில் சட்டங்களை இயற்ற முடியும் (மத்தியப் பட்டியல்)."},
            "B": {"en": "Incorrect. PM does not have individual veto power over bills.", "ta": "தவறு. மசோதாக்கள் மீது பிரதமருக்கு தனிநபர் வீட்டோ அதிகாரம் இல்லை."},
            "C": {"en": "Incorrect. Governors do not sign central bills.", "ta": "தவறு. ஆளுநர்கள் மத்திய மசோதாக்களில் கையொப்பமிடுவதில்லை."},
            "D": {"en": "Correct. Written Constitution, Federalism, FRs, and Judicial Review limit Indian Parliament's authority.", "ta": "சரி. எழுதப்பட்ட அரசியலமைப்பு, கூட்டாட்சி, அடிப்படை உரிமைகள் மற்றும் நீதித்துறை மறுஆய்வு ஆகியவை இந்திய நாடாளுமன்றத்தின் அதிகாரத்தைக் கட்டுப்படுத்துகின்றன."}
        },
        tip_en="TNPSC Tip: Indian Parliament is NOT sovereign due to: Written Constitution, Federal Division of Powers, Fundamental Rights, Judicial Review.",
        tip_ta="TNPSC குறிப்பு: இதன்காரணமாக இந்திய நாடாளுமன்றம் இறையாண்மை கொண்டது அல்ல: எழுதப்பட்ட அரசியலமைப்பு, கூட்டாட்சி அதிகாரப் பகிர்வு, அடிப்படை உரிமைகள், நீதித்துறை மறுஆய்வு.",
        rev_en="Non-sovereign Parliament: Bound by written Constitution, Fundamental Rights, Judicial Review.",
        rev_ta="இறையாண்மையற்ற நாடாளுமன்றம்: எழுதப்பட்ட அரசியலமைப்பு, அடிப்படை உரிமைகள், நீதித்துறை மறுஆய்வுக்கு கட்டுப்பட்டது.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Understand", est_sec=45, pyq_sim="High", tags=["Parliamentary Sovereignty", "Constitutional Supremacy", "Non-Sovereign Parliament"]
    ))

    # Q92 - Statement-Based - Medium - Ans C
    qs.append(make_q(
        q_id="SF_GT_092", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="Statement-Based",
        q_en="Consider the following statements regarding the 'Preamble' as a salient feature of the Constitution:\n1. The Preamble is based on the 'Objectives Resolution' drafted and moved by Pandit Jawaharlal Nehru in 1946.\n2. The Preamble has been amended only once so far, by the 42nd Constitutional Amendment Act of 1976.\n3. The Preamble is a source of power to the legislature and is justiciable in courts of law.\n\nWhich of the statements given above are CORRECT?",
        q_ta="அரசியலமைப்பின் முக்கிய அம்சமாக 'முகவுரை' (Preamble) தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. முகவுரை 1946 இல் பண்டித ஜவஹர்லால் நேருவால் வரைவு செய்யப்பட்டு கொண்டுவரப்பட்ட 'குறிக்கோள்கள் தீர்மானத்தை' அடிப்படையாகக் கொண்டது.\n2. 1976 இன் 42வது அரசியலமைப்பு திருத்தச் சட்டத்தின் மூலம் முகவுரை இதுவரை ஒரே ஒரு முறை மட்டுமே திருத்தப்பட்டுள்ளது.\n3. முகவுரை என்பது சட்டமன்றத்திற்கு ஒரு அதிகார மூலமாகும் மற்றும் நீதிமன்றங்களில் நிலைநிறுத்தப்படக்கூடியது (justiciable).\n\nமேற்கூறிய கூற்றுகளில் எது சரியானவை?",
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
        exp_en="Historical Context: Preamble embodies the fundamental values and philosophy of the Constitution.\nReason:\nStatement 1 is correct: Based on Nehru's Objectives Resolution (moved Dec 13, 1946, adopted Jan 22, 1947).\nStatement 2 is correct: Amended ONCE by 42nd Amendment 1976 (added Socialist, Secular, Integrity).\nStatement 3 is INCORRECT: Preamble is NEITHER a source of power to legislature NOR a prohibition upon powers, and it is NON-JUSTICIABLE in courts.\nConstitutional Impact: Guides interpretation of ambiguous constitutional articles.\nExam Trap: Preamble is non-justiciable and NOT a source of legislative power.",
        exp_ta="வரலாற்றுப் பின்னணி: முகவுரை அரசியலமைப்பின் அடிப்படை மதிப்புகள் மற்றும் தத்துவத்தை பொதிந்துள்ளது.\nகாரணம்:\nகூற்று 1 சரி: நேருவின் குறிக்கோள்கள் தீர்மானத்தை அடிப்படையாகக் கொண்டது (டிசம்பர் 13, 1946 இல் கொண்டுவரப்பட்டது, ஜனவரி 22, 1947 இல் ஏற்றுக்கொள்ளப்பட்டது).\nகூற்று 2 சரி: 42வது திருத்தம் 1976 மூலம் ஒரே ஒரு முறை திருத்தப்பட்டது (சமதர்ம, மதச்சார்பற்ற, ஒருமைப்பாடு சேர்க்கப்பட்டது).\nகூற்று 3 தவறு: முகவுரை சட்டமன்றத்திற்கு அதிகார மூலமும் அல்ல, அதிகாரத் தடையும் அல்ல, மேலும் இது நீதிமன்றங்களில் நிலைநிறுத்த முடியாதது (non-justiciable).\nஅரசியலமைப்பு தாக்கம்: தெளிவற்ற அரசியலமைப்பு உறுப்புகளை விளக்குவதற்கு வழிகாட்டுகிறது.\nதேர்வுப் பொறி: முகவுரை நீதிமன்றத்தால் நிலைநிறுத்த முடியாதது மற்றும் சட்டமன்ற அதிகார மூலம் அல்ல.",
        wno_dict={
            "A": {"en": "Incorrect. Statement 3 is false (Preamble is non-justiciable and not a source of power).", "ta": "தவறு. கூற்று 3 தவறு (முகவுரை நிலைநிறுத்த முடியாதது மற்றும் அதிகார மூலம் அல்ல)."},
            "B": {"en": "Incorrect. Statement 3 is false.", "ta": "தவறு. கூற்று 3 தவறு."},
            "C": {"en": "Correct. Statements 1 and 2 are correct; Statement 3 is false.", "ta": "சரி. கூற்றுகள் 1 மற்றும் 2 சரி; கூற்று 3 தவறு."},
            "D": {"en": "Incorrect. Statement 3 is false.", "ta": "தவறு. கூற்று 3 தவறு."}
        },
        tip_en="TNPSC Tip: Preamble: Objectives Resolution (Nehru), Amended ONCE (42nd Amendment 1976: Socialist, Secular, Integrity), Non-Justiciable.",
        tip_ta="TNPSC குறிப்பு: முகவுரை: குறிக்கோள்கள் தீர்மானம் (நேரு), ஒரே ஒரு முறை திருத்தப்பட்டது (42வது திருத்தம் 1976: சமதர்ம, மதச்சார்பற்ற, ஒருமைப்பாடு), நிலைநிறுத்த முடியாதது.",
        rev_en="Preamble: Nehru's Objectives Resolution, amended ONCE (1976), Non-justiciable.",
        rev_ta="முகவுரை: நேருவின் குறிக்கோள்கள் தீர்மானம், ஒரே ஒரு முறை திருத்தப்பட்டது (1976), நிலைநிறுத்த முடியாதது.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Analyze", est_sec=60, pyq_sim="High", tags=["Preamble", "Objectives Resolution", "42nd Amendment", "TNPSC Trap"]
    ))

    # Q93 - Assertion & Reason - Medium - Ans A
    qs.append(make_q(
        q_id="SF_GT_093", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="Assertion & Reason",
        q_en="Given below are two statements, one labeled as Assertion (A) and the other labeled as Reason (R):\n\nAssertion (A): The Indian Constitution is the lengthiest written constitution in the world.\nReason (R): It incorporates detailed provisions for both the Union and States, historical baggage of the 1935 Act, geographical diversity, and dominance of legal luminaries in the Constituent Assembly.",
        q_ta="கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிக்கப்பட்டுள்ளது:\n\nகூற்று (A): இந்திய அரசியலமைப்பு உலகிலேயே மிக நீளமான எழுதப்பட்ட அரசியலமைப்பாகும்.\nகாரணம் (R): இது மத்திய அரசு மற்றும் மாநிலங்கள் இரண்டிற்குமான விரிவான விதிகள், 1935 சட்டத்தின் வரலாற்றுத் தாக்கம், புவியியல் பன்முகத்தன்மை மற்றும் அரசியலமைப்பு நிர்ணய சபையில் சட்ட வல்லுநர்களின் ஆதிக்கம் ஆகியவற்றை உள்ளடக்கியுள்ளது.",
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
        exp_en="Historical Context: Originally contained 395 Articles, 8 Schedules, and 22 Parts in 1949.\nReason: Four factors contributed to its vast size: (1) Geographical factors (vastness and diversity); (2) Historical factors (GOI Act 1935 influence); (3) Single constitution for both Centre and States; (4) Dominance of legal luminaries in CA.\nConstitutional Impact: Provides comprehensive legal clarity and minimizes administrative ambiguities.\nExam Trap: Single Constitution for both Centre and States (except J&K historically, now unified) is a key reason for length.",
        exp_ta="வரலாற்றுப் பின்னணி: 1949 இல் ஆரம்பத்தில் 395 உறுப்புகள், 8 அட்டவணைகள் மற்றும் 22 பகுதிகளைக் கொண்டிருந்தது.\nகாரணம்: இதன் மிகப்பெரிய அளவிற்கு நான்கு காரணிகள் பங்களித்தன: (1) புவியியல் காரணிகள் (பறந்த பரப்பு மற்றும் பன்முகத்தன்மை); (2) வரலாற்று காரணிகள் (1935 அரசுச் சட்டத்தின் தாக்கம்); (3) மத்திய அரசு மற்றும் மாநிலங்கள் இரண்டிற்கும் ஒரே அரசியலமைப்பு; (4) அரசியலமைப்பு நிர்ணய சபையில் சட்ட வல்லுநர்களின் ஆதிக்கம்.\nஅரசியலமைப்பு தாக்கம்: விரிவான சட்டத் தெளிவை வழங்குகிறது மற்றும் நிர்வாக தெளிவின்மைகளைக் குறைக்கிறது.\nதேர்வுப் பொறி: மத்திய அரசு மற்றும் மாநிலங்கள் இரண்டிற்கும் ஒரே அரசியலமைப்பு என்பது நீளத்திற்கான ஒரு முக்கிய காரணமாகும்.",
        wno_dict={
            "A": {"en": "Correct. Both statements are true and (R) accurately explains why the Constitution is the lengthiest.", "ta": "சரி. இரு கூற்றுகளும் சரி, மற்றும் (R) ஏன் அரசியலமைப்பு மிக நீளமானது என்பதைத் துல்லியமாக விளக்குகிறது."},
            "B": {"en": "Incorrect. (R) is the direct justification for (A).", "ta": "தவறு. (R) என்பது (A)-க்கான நேரடி விளக்கமாகும்."},
            "C": {"en": "Incorrect. (R) is true.", "ta": "தவறு. (R) உண்மை."},
            "D": {"en": "Incorrect. (A) is true.", "ta": "தவறு. (A) உண்மை."}
        },
        tip_en="TNPSC Tip: 4 Reasons for Lengthiest Constitution: Geographical vastness, Historical 1935 Act, Single Constitution for Centre & States, Legal Luminaries.",
        tip_ta="TNPSC குறிப்பு: மிக நீளமான அரசியலமைப்பிற்கான 4 காரணங்கள்: புவியியல் பரப்பு, வரலாற்று 1935 சட்டம், மத்திய-மாநிலங்களுக்கு ஒரே அரசியலமைப்பு, சட்ட வல்லுநர்கள்.",
        rev_en="Lengthiest Constitution: 4 factors (Geography, History/1935 Act, Single Constitution, Legal Experts).",
        rev_ta="மிக நீளமான அரசியலமைப்பு: 4 காரணிகள் (புவியியல், வரலாறு/1935 சட்டம், ஒற்றை அரசியலமைப்பு, சட்ட நிபுணர்கள்).",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Evaluate", est_sec=60, pyq_sim="High", tags=["Lengthiest Constitution", "Salient Features", "Assertion Reason"]
    ))

    # Q94 - Direct MCQ - Easy - Ans C
    qs.append(make_q(
        q_id="SF_GT_094", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Easy", question_type="Direct MCQ",
        q_en="Which feature of the Indian Judiciary ensures that judges cannot be removed from office arbitrarily by the Executive?",
        q_ta="இந்திய நீதித்துறையின் எந்த அம்சம் நீதிபதிகளை நிர்வாகத் துறையால் தன்னிச்சையாக பதவியிலிருந்து நீக்க முடியாது என்பதை உறுதி செய்கிறது?",
        opts_en=[
            "Advisory Jurisdiction",
            "Public Interest Litigation",
            "Security of Tenure",
            "Universal Adult Franchise"
        ],
        opts_ta=[
            "ஆலோசனைக் அதிகார வரம்பு",
            "பொது நல வழக்கு",
            "பதவிக்கால பாதுகாப்பு (Security of Tenure)",
            "உலகளாவிய வயதுவந்தோர் வாக்குரிமை"
        ],
        correct_ans="C",
        exp_en="Historical Context: Independent judiciary requires financial, security, and procedural safeguards from political interference.\nReason: Security of Tenure ensures SC and HC judges can be removed ONLY by the President based on an address passed by Parliament with Special Majority on grounds of proved misbehaviour or incapacity (Article 124(4)).\nConstitutional Impact: Enables judges to deliver impartial justice without fear of executive backlash.\nExam Trap: Judges do NOT hold office during the pleasure of the President.\nMemory Trick: Independent Judiciary = Security of Tenure.",
        exp_ta="வரலாற்றுப் பின்னணி: சுதந்திரமான நீதித்துறைக்கு அரசியல் தலையீட்டிலிருந்து நிதி, பாதுகாப்பு மற்றும் நடைமுறை பாதுகாப்புகள் தேவை.\nகாரணம்: பதவிக்கால பாதுகாப்பு உச்ச நீதிமன்ற மற்றும் உயர் நீதிமன்ற நீதிபதிகள் நிரூபிக்கப்பட்ட தவறான நடத்தை அல்லது இயலாமை காரணமாக சிறப்பு பெரும்பான்மையுடன் நாடாளுமன்றத்தால் நிறைவேற்றப்பட்ட உரையின் அடிப்படையில் மட்டுமே குடியரசுத் தலைவரால் நீக்கப்பட முடியும் என்பதை உறுதி செய்கிறது (உறுப்பு 124(4)).\nஅரசியலமைப்பு தாக்கம்: நிர்வாகப் பழிவாங்கலுக்குப் பயப்படாமல் நீதிபதிகள் நடுநிலையான நீதியை வழங்க உதவுகிறது.\nதேர்வுப் பொறி: நீதிபதிகள் குடியரசுத் தலைவரின் விருப்பம் வரை பதவியில் இருக்க மாட்டார்கள்.\nநினைவுச் சூத்திரம்: சுதந்திரமான நீதித்துறை = பதவிக்கால பாதுகாப்பு.",
        wno_dict={
            "A": {"en": "Incorrect. Advisory jurisdiction is SC consultation under Art 143.", "ta": "தவறு. ஆலோசனைக் அதிகார வரம்பு என்பது உறுப்பு 143 இன் கீழ் உச்ச நீதிமன்ற ஆலோசனையாகும்."},
            "B": {"en": "Incorrect. PIL is a mechanism to access justice.", "ta": "தவறு. PIL என்பது நீதியை அணுகுவதற்கான ஒரு வழிமுறையாகும்."},
            "C": {"en": "Correct. Security of tenure guarantees judges cannot be removed arbitrarily by executive.", "ta": "சரி. பதவிக்கால பாதுகாப்பு நீதிபதிகளை நிர்வாகத் துறையால் தன்னிச்சையாக நீக்க முடியாது என்பதை உத்தரவாதம் செய்கிறது."},
            "D": {"en": "Incorrect. Adult franchise deals with voting rights.", "ta": "தவறு. வயதுவந்தோர் வாக்குரிமை வாக்களிக்கும் உரிமைகளைக் கையாள்கிறது."}
        },
        tip_en="TNPSC Tip: Independent Judiciary features: Security of Tenure, Fixed Service Conditions, Expenses charged on Consolidated Fund, Power to punish for Contempt.",
        tip_ta="TNPSC குறிப்பு: சுதந்திரமான நீதித்துறை அம்சங்கள்: பதவிக்கால பாதுகாப்பு, நிலையான சேவை நிபந்தனைகள், தொகுப்பு நிதியிலிருந்து செலவுகள், அவமதிப்பிற்குத் தண்டிக்கும் அதிகாரம்.",
        rev_en="Judicial Independence: Security of Tenure (Removal only by Parliament Special Majority).",
        rev_ta="நீதித்துறை சுதந்திரம்: பதவிக்கால பாதுகாப்பு (நாடாளுமன்ற சிறப்பு பெரும்பான்மை மூலம் மட்டுமே நீக்கம்).",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Remember", est_sec=30, pyq_sim="High", tags=["Independent Judiciary", "Security of Tenure", "Judicial Safeguards"]
    ))

    # Q95 - TNPSC Trap - Medium - Ans B
    qs.append(make_q(
        q_id="SF_GT_095", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="TNPSC Trap",
        q_en="Which of the following bodies is NOT established directly under a specific Article of the Indian Constitution?",
        q_ta="பின்வரும் அமைப்புகளில் எது இந்திய அரசியலமைப்பின் குறிப்பிட்ட உறுப்பின் கீழ் நேரடியாக நிறுவப்படவில்லை?",
        opts_en=[
            "Finance Commission",
            "State Human Rights Commission",
            "Union Public Service Commission",
            "Comptroller and Auditor General of India"
        ],
        opts_ta=[
            "நிதி ஆணையம்",
            "மாநில மனித உரிமைகள் ஆணையம்",
            "மத்திய அரசுப் பணியாளர் தேர்வாணையம்",
            "இந்திய தலைமை தணிக்கை அதிகாரி"
        ],
        correct_ans="B",
        exp_en="Historical Context: Distinction between Constitutional Bodies and Statutory Bodies is frequently tested by TNPSC.\nReason: State Human Rights Commission (SHRC) is a STATUTORY body created by the Protection of Human Rights Act, 1993, NOT a constitutional body. Finance Commission (Art 280), UPSC (Art 315), CAG (Art 148) are CONSTITUTIONAL bodies.\nConstitutional Impact: Statutory bodies derive power from Parliamentary/State Acts, not Constitution text directly.\nExam Trap: SHRC, NHRC, CVC, Central Information Commission are Statutory; FC, UPSC, CAG, EC are Constitutional.",
        exp_ta="வரலாற்றுப் பின்னணி: அரசியலமைப்பு அமைப்புகளுக்கும் சட்டப்பூர்வ அமைப்புகளுக்கும் இடையிலான வேறுபாடு TNPSC ஆல் அடிக்கடி சோதிக்கப்படுகிறது.\nகாரணம்: மாநில மனித உரிமைகள் ஆணையம் (SHRC) என்பது மனித உரிமைகள் பாதுகாப்புச் சட்டம், 1993 மூலம் உருவாக்கப்பட்ட ஒரு சட்டப்பூர்வ (STATUTORY) அமைப்பாகும், அரசியலமைப்பு அமைப்பு அல்ல. நிதி ஆணையம் (உறுப்பு 280), UPSC (உறுப்பு 315), CAG (உறுப்பு 148) ஆகியவை அரசியலமைப்பு அமைப்புகளாகும்.\nஅரசியலமைப்பு தாக்கம்: சட்டப்பூர்வ அமைப்புகள் நாடாளுமன்ற/மாநிலச் சட்டங்களிலிருந்து அதிகாரத்தைப் பெறுகின்றன, நேரடியாக அரசியலமைப்பு உரையிலிருந்து அல்ல.\nதேர்வுப் பொறி: SHRC, NHRC, CVC, CIC ஆகியவை சட்டப்பூர்வமானவை; நிதி ஆணையம், UPSC, CAG, தேர்தல் ஆணையம் ஆகியவை அரசியலமைப்பு சார்ந்தவை.",
        wno_dict={
            "A": {"en": "Incorrect. Finance Commission is a Constitutional body under Article 280.", "ta": "தவறு. நிதி ஆணையம் உறுப்பு 280 இன் கீழ் ஒரு அரசியலமைப்பு அமைப்பாகும்."},
            "B": {"en": "Correct. State Human Rights Commission is a Statutory body (Human Rights Act 1993), NOT constitutional.", "ta": "சரி. மாநில மனித உரிமைகள் ஆணையம் ஒரு சட்டப்பூர்வ அமைப்பாகும் (மனித உரிமைகள் சட்டம் 1993), அரசியலமைப்பு அமைப்பு அல்ல."},
            "C": {"en": "Incorrect. UPSC is a Constitutional body under Article 315.", "ta": "தவறு. UPSC உறுப்பு 315 இன் கீழ் ஒரு அரசியலமைப்பு அமைப்பாகும்."},
            "D": {"en": "Incorrect. CAG is a Constitutional body under Article 148.", "ta": "தவறு. CAG உறுப்பு 148 இன் கீழ் ஒரு அரசியலமைப்பு அமைப்பாகும்."}
        },
        tip_en="TNPSC Trap: SHRC/NHRC = Statutory Bodies (1993 Act). FC (280), UPSC (315), CAG (148) = Constitutional Bodies.",
        tip_ta="TNPSC பொறி: SHRC/NHRC = சட்டப்பூர்வ அமைப்புகள் (1993 சட்டம்). FC (280), UPSC (315), CAG (148) = அரசியலமைப்பு அமைப்புகள்.",
        rev_en="Statutory vs Constitutional Bodies: SHRC (Statutory 1993 Act); FC, UPSC, CAG (Constitutional).",
        rev_ta="சட்டப்பூர்வ vs அரசியலமைப்பு அமைப்புகள்: SHRC (சட்டப்பூர்வ 1993 சட்டம்); FC, UPSC, CAG (அரசியலமைப்பு).",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Understand", est_sec=45, pyq_sim="High", tags=["Statutory Bodies", "Constitutional Bodies", "SHRC", "TNPSC Trap"]
    ))

    # Q96 - Direct MCQ - Easy - Ans A
    qs.append(make_q(
        q_id="SF_GT_096", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Easy", question_type="Direct MCQ",
        q_en="Under Article 51A(k) added by the 86th Amendment Act of 2002, providing opportunities for education to one's child between the age of 6 and 14 years is the duty of:",
        q_ta="2002 இன் 86வது திருத்தச் சட்டத்தின் மூலம் சேர்க்கப்பட்ட உறுப்பு 51A(k) இன் கீழ், 6 முதல் 14 வயது வரையிலான தனது குழந்தைக்குக் கல்விக்கான வாய்ப்புகளை வழங்குவது யாருடைய கடமையாகும்?",
        opts_en=[
            "Every parent or guardian",
            "The District Collector only",
            "The State School Education Department only",
            "The Union HRD Minister only"
        ],
        opts_ta=[
            "ஒவ்வொரு பெற்றோர் அல்லது பாதுகாவலர்",
            "மாவட்ட ஆட்சியர் மட்டுமே",
            "மாநிலப் பள்ளி கல்வித் துறை மட்டுமே",
            "மத்திய மனிதவள மேம்பாட்டுத் துறை அமைச்சர் மட்டுமே"
        ],
        correct_ans="A",
        exp_en="Historical Context: Added as the 11th Fundamental Duty by the 86th Constitutional Amendment Act, 2002.\nReason: Article 51A(k) states that it is the duty of a citizen of India who is a parent or guardian to provide opportunities for education to his child or ward between the age of 6 and 14 years.\nConstitutional Impact: Complements Article 21A (State duty for free & compulsory education).\nExam Trap: Art 21A = State's duty to provide education; Art 51A(k) = Parent/Guardian's duty to provide educational opportunity.\nMemory Trick: Art 51A(k) = 11th Duty for Parents.",
        exp_ta="வரலாற்றுப் பின்னணி: 2002 இன் 86வது அரசியலமைப்பு திருத்தச் சட்டத்தின் மூலம் 11வது அடிப்படை கடமையாகச் சேர்க்கப்பட்டது.\nகாரணம்: பெற்றோர் அல்லது பாதுகாவலராக இருக்கும் இந்தியக் குடிமகன் 6 முதல் 14 வயது வரையிலான தனது குழந்தைக்குக் கல்விக்கான வாய்ப்புகளை வழங்குவது அவரது கடமையாகும் என்று உறுப்பு 51A(k) கூறுகிறது.\nஅரசியலமைப்பு தாக்கம்: உறுப்பு 21A ஐ (இலவச & கட்டாயக் கல்விக்கான அரசின் கடமை) நிரப்புகிறது.\nதேர்வுப் பொறி: உறுப்பு 21A = கல்வியை வழங்குவதற்கான அரசின் கடமை; உறுப்பு 51A(k) = கல்வி வாய்ப்பை வழங்குவதற்கான பெற்றோர்/பாதுகாவலரின் கடமை.\nநினைவுச் சூத்திரம்: உறுப்பு 51A(k) = பெற்றோர்களுக்கான 11வது கடமை.",
        wno_dict={
            "A": {"en": "Correct. Article 51A(k) places duty on every parent or guardian.", "ta": "சரி. உறுப்பு 51A(k) ஒவ்வொரு பெற்றோர் அல்லது பாதுகாவலர் மீது கடமையைச் சுமத்துகிறது."},
            "B": {"en": "Incorrect. District Collector is an executive official.", "ta": "தவறு. மாவட்ட ஆட்சியர் ஒரு நிர்வாக அதிகாரி."},
            "C": {"en": "Incorrect. School Education Department handles state implementation under Art 21A.", "ta": "தவறு. பள்ளி கல்வித் துறை உறுப்பு 21A இன் கீழ் மாநில அமலாக்கத்தைக் கையாள்கிறது."},
            "D": {"en": "Incorrect. HRD Minister is a cabinet minister.", "ta": "தவறு. மனிதவள மேம்பாட்டு அமைச்சர் ஒரு அமைச்சரவை அமைச்சர்."}
        },
        tip_en="TNPSC Tip: Art 21A (FR) = State obligation for 6-14 education; Art 51A(k) (FD) = Parent/Guardian obligation for 6-14 education.",
        tip_ta="TNPSC குறிப்பு: உறுப்பு 21A (FR) = 6-14 கல்விக்கான அரசின் கடமை; உறுப்பு 51A(k) (FD) = 6-14 கல்விக்கான பெற்றோர்/பாதுகாவலர் கடமை.",
        rev_en="Article 51A(k): 11th Duty added by 86th Amendment 2002 for parents/guardians.",
        rev_ta="உறுப்பு 51A(k): பெற்றோர்கள்/பாதுகாவலர்களுக்காக 86வது திருத்தம் 2002 மூலம் சேர்க்கப்பட்ட 11வது கடமை.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Remember", est_sec=30, pyq_sim="High", tags=["Fundamental Duties", "86th Amendment", "Article 51A"]
    ))

    # Q97 - Conceptual - Medium - Ans C
    qs.append(make_q(
        q_id="SF_GT_097", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="Conceptual",
        q_en="Why is the Indian Constitution described as 'Quasi-Federal' by constitutional jurist K.C. Wheare?",
        q_ta="அரசியலமைப்புச் சட்ட வல்லுநர் கே.சி. வேரால் இந்திய அரசியலமைப்பு ஏன் 'அரை-கூட்டாட்சி' (Quasi-Federal) என்று விவரிக்கப்படுகிறது?",
        opts_en=[
            "Because India has no written Constitution and relies entirely on unwritten conventions.",
            "Because states have more legislative powers than the Union Parliament.",
            "Because it establishes a unitary state with subsidiary federal features rather than a federal state with subsidiary unitary features.",
            "Because all state governors are elected directly by the people."
        ],
        opts_ta=[
            "ஏனெனில் இந்தியாவிடம் எழுதப்பட்ட அரசியலமைப்பு இல்லை மற்றும் முழுமையாக எழுதப்படாத மரபுகளை மட்டுமே நம்பியுள்ளது.",
            "ஏனெனில் மத்திய நாடாளுமன்றத்தை விட மாநிலங்களுக்கு அதிக சட்ட அதிகாரங்கள் உள்ளன.",
            "ஏனெனில் அது துணைக் கூட்டாட்சி அம்சங்களைக் கொண்ட ஒற்றையாட்சி அரசை நிறுவுகிறதே தவிர, துணை ஒற்றையாட்சி அம்சங்களைக் கொண்ட கூட்டாட்சி அரசை அல்ல.",
            "ஏனெனில் அனைத்து மாநில ஆளுநர்களும் மக்களால் நேரடியாகத் தேர்ந்தெடுக்கப்படுகிறார்கள்."
        ],
        correct_ans="C",
        exp_en="Historical Context: K.C. Wheare analyzed Indian federalism in comparison with standard classical federations (USA, Australia).\nReason: Wheare concluded that India is 'Quasi-Federal' (unitary state with subsidiary federal features) because the Centre holds overwhelming power during emergencies, appoints Governors, alters state boundaries (Art 3), and controls key administrative services.\nConstitutional Impact: Highlights the strong centralizing tilt designed by the Constitution framers.\nExam Trap: K.C. Wheare = Quasi-Federal; Granville Austin = Cooperative Federalism.",
        exp_ta="வரலாற்றுப் பின்னணி: கே.சி. வேர் திட்டவட்டமான பாரம்பரியக் கூட்டாட்சிகளுடன் (அமெரிக்கா, ஆஸ்திரேலியா) ஒப்பிட்டு இந்தியக் கூட்டாட்சியை பகுப்பாய்வு செய்தார்.\nகாரணம்: அவசரநிலைகளின் போது மத்திய அரசு அசைக்க முடியாத அதிகாரத்தைக் கொண்டிருப்பதாலும், ஆளுநர்களை நியமிப்பதாலும், மாநில எல்லைகளை மாற்றுவதாலும் (உறுப்பு 3), முக்கிய நிர்வாகப் பணிகளைக் கட்டுப்படுத்துவதாலும் இந்தியா 'அரை-கூட்டாட்சி' (துணைக் கூட்டாட்சி அம்சங்களைக் கொண்ட ஒற்றையாட்சி அரசு) என்று வேர் முடிவுக்கு வந்தார்.\nஅரசியலமைப்பு தாக்கம்: அரசியலமைப்பு உருவாக்கிகளால் வடிவமைக்கப்பட்ட வலுவான மையப்படுத்தும் சாய்வைச் சுட்டிக்காட்டுகிறது.\nதேர்வுப் பொறி: கே.சி. வேர் = அரை-கூட்டாட்சி; கிரான்வில் ஆஸ்டின் = கூட்டுறவு கூட்டாட்சி.",
        wno_dict={
            "A": {"en": "Incorrect. India has the lengthiest written constitution in the world.", "ta": "தவறு. இந்தியா உலகிலேயே மிக நீளமான எழுதப்பட்ட அரசியலமைப்பைக் கொண்டுள்ளது."},
            "B": {"en": "Incorrect. Centre has more legislative powers (Union list has 100 subjects).", "ta": "தவறு. மத்திய அரசு அதிக சட்ட அதிகாரங்களைக் கொண்டுள்ளது (மத்தியப் பட்டியலில் 100 பொருட்கள் உள்ளன)."},
            "C": {"en": "Correct. Unitary state with subsidiary federal features (K.C. Wheare's definition of Quasi-Federal).", "ta": "சரி. துணைக் கூட்டாட்சி அம்சங்களைக் கொண்ட ஒற்றையாட்சி அரசு (கே.சி. வேரின் அரை-கூட்டாட்சி வரையறை)."},
            "D": {"en": "Incorrect. Governors are appointed by President, not elected.", "ta": "தவறு. ஆளுநர்கள் குடியரசுத் தலைவரால் நியமிக்கப்படுகிறார்கள், தேர்ந்தெடுக்கப்படுவதில்லை."}
        },
        tip_en="TNPSC Tip: K.C. Wheare quote: 'Quasi-Federal' = Unitary state with subsidiary federal features.",
        tip_ta="TNPSC குறிப்பு: கே.சி. வேர் மேற்கோள்: 'அரை-கூட்டாட்சி' = துணைக் கூட்டாட்சி அம்சங்களைக் கொண்ட ஒற்றையாட்சி அரசு.",
        rev_en="Quasi-Federal (K.C. Wheare): Unitary bias in Indian federal framework.",
        rev_ta="அரை-கூட்டாட்சி (கே.சி. வேர்): இந்தியக் கூட்டாட்சி அமைப்பில் ஒற்றையாட்சி சாய்வு.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Understand", est_sec=45, pyq_sim="High", tags=["K.C. Wheare", "Quasi-Federal", "Federalism"]
    ))

    # Q98 - Statement-Based - Medium - Ans B
    qs.append(make_q(
        q_id="SF_GT_098", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Medium", question_type="Statement-Based",
        q_en="Consider the following statements regarding the 'Rule of Law' as embodied in Article 14:\n1. 'Equality before Law' is a negative concept of British origin signifying absence of any special privilege in favor of any individual.\n2. 'Equal Protection of the Laws' is a positive concept of American origin signifying equal treatment under equal circumstances.\n3. The rule of equality before law is absolute in India without any constitutional exceptions for the President or State Governors.\n\nWhich of the statements given above are CORRECT?",
        q_ta="உறுப்பு 14 இல் பொதிந்துள்ள 'சட்டத்தின் ஆட்சி' (Rule of Law) தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 'சட்டத்தின் முன் சமத்துவம்' என்பது எந்தவொரு நபருக்கும் சாதகமான சிறப்புச் சலுகை இல்லாமையைக் குறிக்கும் பிரிட்டிஷ் மூலத்தின் எதிர்மறைக் கருத்தாகும்.\n2. 'சட்டங்களின் சமமான பாதுகாப்பு' என்பது சமமான சூழ்நிலைகளில் சமமான சிகிச்சையைக் குறிக்கும் அமெரிக்க மூலத்தின் நேர்மறைக் கருத்தாகும்.\n3. சட்டத்தின் முன் சமத்துவ விதி இந்தியாவில் குடியரசுத் தலைவர் அல்லது மாநில ஆளுநர்களுக்கு எந்தவொரு அரசியலமைப்பு விதிவிலக்குகளும் இன்றி முழுமையானது.\n\nமேற்கூறிய கூற்றுகளில் எது சரியானவை?",
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
        exp_en="Historical Context: Article 14 combines British 'Equality before Law' and American 'Equal Protection of Laws'.\nReason:\nStatement 1 is correct: Equality before Law (UK origin) = Negative concept (no special privilege).\nStatement 2 is correct: Equal Protection of Laws (US origin) = Positive concept (like should be treated alike).\nStatement 3 is INCORRECT: Article 14 is NOT absolute; Article 361 provides constitutional immunity to the President and Governors from criminal proceedings during their term of office.\nConstitutional Impact: Synthesizes formal legal equality with practical equity.\nExam Trap: President and Governors enjoy immunity under Article 361 as exceptions to Article 14.",
        exp_ta="வரலாற்றுப் பின்னணி: உறுப்பு 14 பிரிட்டிஷ் 'சட்டத்தின் முன் சமத்துவம்' மற்றும் அமெரிக்க 'சட்டங்களின் சமமான பாதுகாப்பு' ஆகியவற்றை இணைக்கிறது.\nகாரணம்:\nகூற்று 1 சரி: சட்டத்தின் முன் சமத்துவம் (இங்கிலாந்து மூலம்) = எதிர்மறைக் கருத்து (சிறப்புச் சலுகை இல்லை).\nகூற்று 2 சரி: சட்டங்களின் சமமான பாதுகாப்பு (அமெரிக்க மூலம்) = நேர்மறைக் கருத்து (சமமானவை சமமாக நடத்தப்பட வேண்டும்).\nகூற்று 3 தவறு: உறுப்பு 14 முழுமையானது அல்ல; உறுப்பு 361 குடியரசுத் தலைவர் மற்றும் ஆளுநர்களுக்கு அவர்களின் பதவிக் காலத்தில் குற்றவியல் நடவடிக்கைகளிலிருந்து அரசியலமைப்பு விலக்கு அளிக்கிறது.\nஅரசியலமைப்பு தாக்கம்: முறைப்படியான சட்ட சமத்துவத்தை நடைமுறை நேர்மையுடன் இணைக்கிறது.\nதேர்வுப் பொறி: உறுப்பு 14 க்கு விதிவிலக்காக உறுப்பு 361 இன் கீழ் குடியரசுத் தலைவர் மற்றும் ஆளுநர்கள் விலக்கு பெறுகிறார்கள்.",
        wno_dict={
            "A": {"en": "Incorrect. Statement 3 is false (Article 361 provides exceptions for President/Governors).", "ta": "தவறு. உறுப்பு 361 குடியரசுத் தலைவர்/ஆளுநர்களுக்கு விதிவிலக்குகளை வழங்குவதால் கூற்று 3 தவறு."},
            "B": {"en": "Correct. Statements 1 and 2 are correct; Statement 3 is false.", "ta": "சரி. கூற்றுகள் 1 மற்றும் 2 சரி; கூற்று 3 தவறு."},
            "C": {"en": "Incorrect. Statement 3 is false.", "ta": "தவறு. கூற்று 3 தவறு."},
            "D": {"en": "Incorrect. Statement 3 is false.", "ta": "தவறு. கூற்று 3 தவறு."}
        },
        tip_en="TNPSC Trap: Article 14 has exceptions: Article 361 (President & Governor immunity), Article 31C (DPSP 39b/c primacy), Foreign Ambassadors.",
        tip_ta="TNPSC குறிப்பு: உறுப்பு 14 க்கு விதிவிலக்குகள் உள்ளன: உறுப்பு 361 (குடியரசுத் தலைவர் & ஆளுநர் விலக்கு), உறுப்பு 31C (DPSP 39b/c முதன்மை), வெளிநாட்டு தூதர்கள்.",
        rev_en="Article 14: Equality before Law (UK - negative) + Equal Protection of Laws (USA - positive). Exceptions = Art 361.",
        rev_ta="உறுப்பு 14: சட்டத்தின் முன் சமத்துவம் (இங்கிலாந்து - எதிர்மறை) + சட்டங்களின் சமமான பாதுகாப்பு (அமெரிக்கா - நேர்மறை). விதிவிலக்குகள் = உறுப்பு 361.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Analyze", est_sec=60, pyq_sim="High", tags=["Article 14", "Rule of Law", "Article 361", "TNPSC Trap"]
    ))

    # Q99 - Hard / Analytical - Hard - Ans A
    qs.append(make_q(
        q_id="SF_GT_099", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Hard", question_type="Hard / Analytical",
        q_en="Which of the following landmark judgments established that the 'Harmony and Balance between Fundamental Rights and Directive Principles' is an essential feature of the Basic Structure of the Constitution?",
        q_ta="பின்வரும் எந்த வரலாற்றுச் சிறப்புமிக்க தீர்ப்பு 'அடிப்படை உரிமைகளுக்கும் நெறிமுறைக் கோட்பாடுகளுக்கும் இடையிலான இணக்கமும் சமநிலையும்' அரசியலமைப்பின் அடிப்படை அமைப்பின் ஒரு முக்கிய அம்சம் என நிறுவியது?",
        opts_en=[
            "Minerva Mills v. Union of India (1980)",
            "Kesavananda Bharati v. State of Kerala (1973)",
            "Golaknath v. State of Punjab (1967)",
            "Maneka Gandhi v. Union of India (1978)"
        ],
        opts_ta=[
            "மினர்வா மில்ஸ் எதிர் இந்திய யூனியன் (1980)",
            "கேசவாநந்த பாரதி எதிர் கேரள மாநிலம் (1973)",
            "கோலக்நாத் எதிர் பஞ்சாப் மாநிலம் (1967)",
            "மேனகா காந்தி எதிர் இந்திய யூனியன் (1978)"
        ],
        correct_ans="A",
        exp_en="Historical Context: Minerva Mills (1980) invalidated Section 4 & 55 of 42nd Amendment 1976.\nReason: Supreme Court held that Part III (FRs) and Part IV (DPSPs) are like two wheels of a chariot. Giving absolute precedence to DPSPs over FRs destroys the harmony between them, which is a Basic Feature of the Constitution.\nConstitutional Impact: Restored judicial balance between individual liberties and social welfare.\nExam Trap: Kesavananda Bharati (1973) created Basic Structure Doctrine; Minerva Mills (1980) specified HARMONY between FR & DPSP as Basic Structure.",
        exp_ta="வரலாற்றுப் பின்னணி: மினர்வா மில்ஸ் (1980) 42வது திருத்தம் 1976 இன் பிரிவு 4 & 55 ஐ செல்லாததாக்கியது.\nகாரணம்: பகுதி III (FR) மற்றும் பகுதி IV (DPSP) ஆகியவை ஒரு தேரின் இரண்டு சக்கரங்களைப் போன்றவை என்று உச்ச நீதிமன்றம் கூறியது. FRகளை விட DPSPகளுக்கு முழுமையான முன்னுரிமை அளிப்பது அவற்றுக்கிடையேயான இணக்கத்தை அழிக்கிறது, இது அரசியலமைப்பின் ஒரு அடிப்படை அம்சமாகும்.\nஅரசியலமைப்பு தாக்கம்: தனிநபர் சுதந்திரத்திற்கும் சமூக நலனுக்கும் இடையே நீதித்துறை சமநிலையை மீட்டெடுத்தது.\nதேர்வுப் பொறி: கேசவாநந்த பாரதி (1973) அடிப்படை கட்டமைப்பு கோட்பாட்டை உருவாக்கியது; மினர்வா மில்ஸ் (1980) FR & DPSP இடையேயான இணக்கத்தை அடிப்படை அமைப்பாகக் குறிப்பிட்டது.",
        wno_dict={
            "A": {"en": "Correct. Minerva Mills Case (1980) established harmony between FRs and DPSPs as Basic Structure.", "ta": "சரி. மினர்வா மில்ஸ் வழக்கு (1980) FR மற்றும் DPSP இடையேயான இணக்கத்தை அடிப்படை அமைப்பாக நிறுவியது."},
            "B": {"en": "Incorrect. Kesavananda Bharati (1973) introduced Basic Structure doctrine generally.", "ta": "தவறு. கேசவாநந்த பாரதி (1973) பொதுவான அடிப்படை கட்டமைப்பு கோட்பாட்டை அறிமுகப்படுத்தியது."},
            "C": {"en": "Incorrect. Golaknath (1967) held FRs cannot be amended.", "ta": "தவறு. கோலக்நாத் (1967) FRகளை திருத்த முடியாது என்றது."},
            "D": {"en": "Incorrect. Maneka Gandhi (1978) expanded Article 21.", "ta": "தவறு. மேனகா காந்தி (1978) உறுப்பு 21 ஐ விரிவுபடுத்தியது."}
        },
        tip_en="TNPSC Tip: Minerva Mills Case 1980 = Harmony and balance between Part III (FRs) and Part IV (DPSPs) is Basic Structure.",
        tip_ta="TNPSC குறிப்பு: மினர்வா மில்ஸ் வழக்கு 1980 = பகுதி III (FR) மற்றும் பகுதி IV (DPSP) இடையேயான இணக்கமும் சமநிலையும் அடிப்படை அமைப்பு.",
        rev_en="Minerva Mills Case (1980): Harmony between FRs & DPSPs = Basic Feature.",
        rev_ta="மினர்வா மில்ஸ் வழக்கு (1980): FR & DPSP இடையேயான இணக்கம் = அடிப்படை அம்சம்.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Analyze", est_sec=60, pyq_sim="High", tags=["Minerva Mills Case", "Basic Structure", "FR vs DPSP"]
    ))

    # Q100 - Conceptual - Hard - Ans D
    qs.append(make_q(
        q_id="SF_GT_100", subject="Polity", topic="Salient Features of the Indian Constitution",
        difficulty="Hard", question_type="Conceptual",
        q_en="How does the Indian Constitution synthesize 'Parliamentary Sovereignty' (British Model) with 'Judicial Supremacy' (American Model)?",
        q_ta="பிரிட்டிஷ் மாதிரியான 'நாடாளுமன்ற இறையாண்மை' மற்றும் அமெரிக்க மாதிரியான 'நீதித்துறை மேலாதிக்கம்' ஆகியவற்றை இந்திய அரசியலமைப்பு எவ்வாறு இணைக்கிறது?",
        opts_en=[
            "By granting the Supreme Court power to abolish Parliament during economic emergencies.",
            "By making the Prime Minister the ultimate judicial authority above all courts.",
            "By allowing Parliament to amend any constitutional provision without judicial review.",
            "By empowering the Judiciary to declare parliamentary laws unconstitutional via Judicial Review, while empowering Parliament to amend major portions of the Constitution under Article 368 within Basic Structure limits."
        ],
        opts_ta=[
            "பொருளாதார அவசரநிலைகளின் போது நாடாளுமன்றத்தை ஒழிக்கும் அதிகாரத்தை உச்ச நீதிமன்றத்திற்கு வழங்குவதன் மூலம்.",
            "அனைத்து நீதிமன்றங்களுக்கும் மேலாக பிரதமரை இறுதியான நீதித்துறை அதிகாரமாக ஆக்குவதன் மூலம்.",
            "நீதித்துறை மறுஆய்வின்றி எந்தவொரு அரசியலமைப்பு விதியையும் திருத்த நாடாளுமன்றத்தை அனுமதிப்பதன் மூலம்.",
            "நீதித்துறை மறுஆய்வு மூலம் நாடாளுமன்றச் சட்டங்களை அரசியலமைப்பிற்கு எதிரானது என அறிவிக்க நீதித்துறைக்கு அதிகாரம் அளிக்கும் அதே வேளையில், அடிப்படை கட்டமைப்பு வரம்புகளுக்குள் உறுப்பு 368 இன் கீழ் அரசியலமைப்பின் பெரும்பகுதிகளைத் திருத்த நாடாளுமன்றத்திற்கு அதிகாரம் அளிப்பதன் மூலம்."
        ],
        correct_ans="D",
        exp_en="Historical Context: The Constitution framers consciously avoided the extremes of British Parliamentary Sovereignty and American Judicial Supremacy.\nReason: Supreme Court can declare parliamentary laws unconstitutional through Judicial Review (checking legislative overreach like in USA). On the other hand, Parliament can amend major parts of the Constitution under Article 368 (checking judicial rigidity like in UK). This synthesis creates a balanced constitutional system.\nConstitutional Impact: Ensures no single organ of state holds unbridled, absolute authority.\nExam Trap: India has Constitutional Supremacy, NOT Parliamentary Sovereignty or Judicial Tyranny.\nMemory Trick: Synthesis = SC Judicial Review + Parliamentary Amending Power (Art 368).",
        exp_ta="வரலாற்றுப் பின்னணி: அரசியலமைப்பு உருவாக்குநர்கள் பிரிட்டிஷ் நாடாளுமன்ற இறையாண்மை மற்றும் அமெரிக்க நீதித்துறை மேலாதிக்கத்தின் தீவிரங்களைத் தையிரியமாகத் தவிர்த்தனர்.\nகாரணம்: நீதித்துறை மறுஆய்வு மூலம் நாடாளுமன்றச் சட்டங்களை அரசியலமைப்பிற்கு எதிரானது என உச்ச நீதிமன்றம் அறிவிக்க முடியும் (அமெரிக்காவைப் போல சட்டமன்ற மீறலைச் சரிபார்க்கிறது). மறுபுறம், நாடாளுமன்றம் உறுப்பு 368 இன் கீழ் அரசியலமைப்பின் பெரும்பகுதிகளைத் திருத்த முடியும் (இங்கிலாந்தைப் போல நீதித்துறை நெகிழ்வின்மையைச் சரிபார்க்கிறது). இந்த இணைப்பு ஒரு சமநிலையான அரசியலமைப்பு அமைப்பை உருவாக்குகிறது.\nஅரசியலமைப்பு தாக்கம்: அரசின் எந்தவொரு ஒற்றை அங்கமும் தடையற்ற, முழுமையான அதிகாரத்தைக் கொண்டிருக்கவில்லை என்பதை உறுதி செய்கிறது.\nதேர்வுப் பொறி: இந்தியாவில் அரசியலமைப்பு மேலாதிக்கம் உள்ளது, நாடாளுமன்ற இறையாண்மையோ அல்லது நீதித்துறை கொடுங்கோன்மையோ இல்லை.\nநினைவுச் சூத்திரம்: இணைப்பு = உச்ச நீதிமன்ற நீதித்துறை மறுஆய்வு + நாடாளுமன்றத் திருத்தும் அதிகாரம் (உறுப்பு 368).",
        wno_dict={
            "A": {"en": "Incorrect. SC cannot abolish Parliament.", "ta": "தவறு. உச்ச நீதிமன்றம் நாடாளுமன்றத்தை ஒழிக்க முடியாது."},
            "B": {"en": "Incorrect. PM is executive head, not judicial authority.", "ta": "தவறு. பிரதமர் நிர்வாகத் தலைவர், நீதித்துறை அதிகாரி அல்ல."},
            "C": {"en": "Incorrect. Judicial review limits parliamentary amending power.", "ta": "தவறு. நீதித்துறை மறுஆய்வு நாடாளுமன்ற திருத்தும் அதிகாரத்தைக் கட்டுப்படுத்துகிறது."},
            "D": {"en": "Correct. Perfect synthesis: Judicial Review balances Parliamentary Amending Power under Article 368 within Basic Structure limits.", "ta": "சரி. சரியான இணைப்பு: நீதித்துறை மறுஆய்வு அடிப்படை கட்டமைப்பு வரம்புகளுக்குள் உறுப்பு 368 இன் கீழ் நாடாளுமன்ற திருத்தும் அதிகாரத்தைச் சமநிலைப்படுத்துகிறது."}
        },
        tip_en="TNPSC Tip: Indian Polity = Synthesis of Parliamentary Sovereignty (UK) and Judicial Supremacy (USA) under Constitutional Supremacy.",
        tip_ta="TNPSC குறிப்பு: இந்திய அரசியல் = அரசியலமைப்பு மேலாதிக்கத்தின் கீழ் நாடாளுமன்ற இறையாண்மை (இங்கிலாந்து) மற்றும் நீதித்துறை மேலாதிக்கம் (அமெரிக்கா) ஆகியவற்றின் இணைப்பு.",
        rev_en="Synthesis: Judicial Review (US feature) + Parliamentary Amending Power Art 368 (UK feature) = Constitutional Supremacy.",
        rev_ta="இணைப்பு: நீதித்துறை மறுஆய்வு (அமெரிக்க அம்சம்) + நாடாளுமன்ற திருத்தும் அதிகாரம் உறுப்பு 368 (இங்கிலாந்து அம்சம்) = அரசியலமைப்பு மேலாதிக்கம்.",
        sources=["M. Laxmikanth - Indian Polity"],
        bloom="Evaluate", est_sec=60, pyq_sim="High", tags=["Parliamentary Sovereignty", "Judicial Supremacy", "Constitutional Supremacy", "Synthesis"]
    ))

    return qs

print("Part 4 defined: 25 questions.")
