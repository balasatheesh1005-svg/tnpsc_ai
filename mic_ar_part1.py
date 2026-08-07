def make_ar_q(q_id, q_type, q_en, q_ta,
              correct_ans, exp_en, exp_ta,
              wno_a_en, wno_a_ta, wno_b_en, wno_b_ta, wno_c_en, wno_c_ta, wno_d_en, wno_d_ta,
              tip_en, tip_ta, rev_en, rev_ta, bloom, est_time, tags):
    opt_a_en = "Both Assertion and Reason are true and Reason is the correct explanation of Assertion."
    opt_a_ta = "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்."
    
    opt_b_en = "Both Assertion and Reason are true but Reason is NOT the correct explanation of Assertion."
    opt_b_ta = "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல."
    
    opt_c_en = "Assertion is true but Reason is false."
    opt_c_ta = "A சரி, ஆனால் R தவறு."
    
    opt_d_en = "Assertion is false but Reason is true."
    opt_d_ta = "A தவறு, ஆனால் R சரி."

    opts = [
        {"id": "A", "en": opt_a_en, "ta": opt_a_ta},
        {"id": "B", "en": opt_b_en, "ta": opt_b_ta},
        {"id": "C", "en": opt_c_en, "ta": opt_c_ta},
        {"id": "D", "en": opt_d_en, "ta": opt_d_ta}
    ]
    opts_en = [opt_a_en, opt_b_en, opt_c_en, opt_d_en]
    opts_ta = [opt_a_ta, opt_b_ta, opt_c_ta, opt_d_ta]

    return {
        "id": q_id,
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Hard",
        "question_type": "Assertion & Reason",
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
        "source_reference": ["M. Laxmikanth - Indian Polity", "NCERT Class 11 - Indian Constitution at Work", "Constituent Assembly Debates"],
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

questions = []

# MIC_AR_001
questions.append(make_ar_q(
    "MIC_AR_001", "Assertion & Reason",
    "Assertion (A): The demand for a Constituent Assembly elected on adult franchise was an essential assertion of national sovereignty against British imperial authority.\nReason (R): A constitution framed by a British-imposed committee or parliament would lack political legitimacy and popular sovereignty among the Indian people.",
    "கூற்று (A): வயதுவந்தோர் வாக்குரிமையின் அடிப்படையில் தேர்ந்தெடுக்கப்பட்ட அரசியலமைப்பு அவைக் கோரிக்கை என்பது பிரிட்டிஷ் ஏகாதிபத்திய அதிகாரத்திற்கு எதிரான தேசிய இறையாண்மையின் அத்தியாவசிய அழுத்தமான வெளிப்பாடாகும்.\nகாரணம் (R): பிரிட்டிஷ் அரசாங்கத்தால் திணிக்கப்பட்ட ஒரு குழு அல்லது நாடாளுமன்றத்தால் உருவாக்கப்படும் அரசியலமைப்பு, இந்திய மக்களிடையே அரசியல் சட்டபூர்வமான தன்மையையும் மக்கள் இறையாண்மையையும் கொண்டிருக்காது.",
    "A",
    "Both Assertion and Reason are true, and Reason correctly explains Assertion. Jawaharlal Nehru explicitly declared in 1938 that the Constitution of free India must be framed by a Constituent Assembly elected on adult franchise without outside interference, asserting that popular sovereignty belongs to Indian citizens.",
    "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும். சுதந்திர இந்தியாவின் அரசியலமைப்பு வெளிச்சக்திகளின் தலையீடின்றி வயதுவந்தோர் வாக்குரிமையால் தேர்ந்தெடுக்கப்பட்ட அவையால் உருவாக்கப்பட வேண்டும் என்று 1938 இல் நேரு அறிவித்தார்.",
    "Correct. Both A and R are true, and R correctly explains why national sovereignty mandated an Indian-elected Constituent Assembly.", "சரி. A மற்றும் R இரண்டும் சரி, R என்பது A-வின் சரியான விளக்கம்.",
    "Incorrect. R is the direct underlying reason for A.", "தவறு. R என்பது A-விற்கான நேரடி காரணம்.",
    "Incorrect. Reason (R) is true.", "தவறு. காரணம் (R) சரியானது.",
    "Incorrect. Assertion (A) is true.", "தவறு. கூற்று (A) சரியானது.",
    "TNPSC Trap: M.N. Roy first put forward the idea of a Constituent Assembly in 1934; INC demanded it officially in 1935; Nehru demanded adult franchise basis in 1938.",
    "TNPSC பொறி: எம்.என். ராய் 1934 இல் யோசனையை முன்வைத்தார்; காங்கிரஸ் 1935 இல் கோரியது; நேரு 1938 இல் வயதுவந்தோர் வாக்குரிமையைக் கோரினார்.",
    "The concept of popular sovereignty implies that political authority originates from the people.",
    "மக்கள் இறையாண்மை என்பது அரசியல் அதிகாரம் மக்களிடமிருந்தே தோன்றுகிறது என்பதைக் குறிக்கிறது.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "Demand for Constituent Assembly", "Jawaharlal Nehru"]
))

# MIC_AR_002
questions.append(make_ar_q(
    "MIC_AR_002", "Assertion & Reason",
    "Assertion (A): Both the Indian National Congress and the Muslim League initially accepted the Cabinet Mission Plan of 1946 despite holding opposing constitutional vision.\nReason (R): The Cabinet Mission Plan explicitly granted separate sovereign statehood to Pakistan while creating a loose confederation for the Indian Union.",
    "கூற்று (A): இந்திய தேசிய காங்கிரஸ் மற்றும் முஸ்லீம் லீக் ஆகிய இரண்டும் எதிரெதிர் அரசியலமைப்புப் பார்வைகளைக் கொண்டிருந்தபோதிலும் 1946 கேபினட் தூதுக்குழு திட்டத்தை தொடக்கத்தில் ஏற்றுக்கொண்டன.\nகாரணம் (R): கேபினட் தூதுக்குழு திட்டம் இந்திய ஒன்றியத்திற்கு ஒரு தளர்வான கூட்டமைப்பை உருவாக்கும் அதே வேளையில் பாகிஸ்தானுக்கு தனி இறையாண்மை கொண்ட மாநில அந்தஸ்தை வெளிப்படையாக வழங்கியது.",
    "C",
    "Assertion (A) is true because both INC and Muslim League accepted the Cabinet Mission Plan in June 1946 (before later disputes). Reason (R) is FALSE because the Cabinet Mission Plan EXPLICITLY REJECTED the demand for a sovereign Pakistan, offering instead a 3-tier grouping scheme with a weak Central Union.",
    "கூற்று (A) சரி, ஏனெனில் காங்கிரஸ் மற்றும் லீக் இரண்டும் ஜூன் 1946 இல் கேபினட் திட்டத்தை ஏற்றுக்கொண்டன. காரணம் (R) தவறு, ஏனெனில் கேபினட் தூதுக்குழு திட்டம் தனி பாகிஸ்தான் கோரிக்கையை வெளிப்படையாக நிராகரித்தது.",
    "Incorrect. Reason (R) is false because the Cabinet Mission rejected Pakistan.", "தவறு. காரணம் (R) தவறானது, ஏனெனில் கேபினட் திட்டம் பாகிஸ்தானை நிராகரித்தது.",
    "Incorrect. Reason (R) is false.", "தவறு. காரணம் (R) தவறானது.",
    "Correct. Assertion (A) is true; Reason (R) is false because Cabinet Mission rejected Pakistan.", "சரி. கூற்று (A) சரி; காரணம் (R) தவறு ஏனெனில் கேபினட் திட்டம் பாகிஸ்தானை நிராகரித்தது.",
    "Incorrect. Assertion (A) is true.", "தவறு. கூற்று (A) சரியானது.",
    "TNPSC Trap: Cabinet Mission REJECTED the demand for Pakistan on grounds of defense, communications, and minority inclusion.",
    "TNPSC பொறி: பாதுகாப்பு, தகவல் தொடர்பு மற்றும் சிறுபான்மையினர் நலன் ஆகியவற்றின் அடிப்படையில் கேபினட் தூதுக்குழு பாகிஸ்தான் கோரிக்கையை நிராகரித்தது.",
    "Cabinet Mission proposed a 3-tier structure: Union Centre, Groups of Provinces (Section A, B, C), and individual Provinces.",
    "கேபினட் தூதுக்குழு 3-அடுக்கு அமைப்பைப் பரிந்துரைத்தது: மத்திய ஒன்றியம், மாகாணக் குழுக்கள் (பிரிவு A, B, C) மற்றும் தனி மாகாணங்கள்.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "Cabinet Mission Plan", "Partition Events"]
))

# MIC_AR_003
questions.append(make_ar_q(
    "MIC_AR_003", "Assertion & Reason",
    "Assertion (A): The Constituent Assembly of India was elected indirectly by members of Provincial Legislative Assemblies rather than directly by universal adult franchise.\nReason (R): Conducting direct elections based on adult franchise in 1946 amidst widespread partition tensions, huge population, and outdated electoral rolls would have caused catastrophic delays in constitution-framing.",
    "கூற்று (A): இந்திய அரசியலமைப்பு அவை உலகளாவிய வயதுவந்தோர் வாக்குரிமையால் நேரடியாகத் தேர்ந்தெடுக்கப்படாமல் மாகாண சட்டமன்ற உறுப்பினர்களால் மறைமுகமாகத் தேர்ந்தெடுக்கப்பட்டது.\nகாரணம் (R): 1946 இல் பரவலான பிரிவினை பதற்றங்கள், பெரும் மக்கள் தொகை மற்றும் காலாவதியான வாக்காளர் பட்டியல்களுக்கு மத்தியில் வயதுவந்தோர் வாக்குரிமை அடிப்படையில் நேரடித் தேர்தல்களை நடத்துவது அரசியலமைப்பு உருவாக்கத்தில் பேரழிவுத் தாமதங்களை ஏற்படுத்தியிருக்கும்.",
    "A",
    "Both Assertion and Reason are true, and Reason is the correct explanation of Assertion. In 1946, direct elections under adult franchise were administratively impossible without delaying independence and constitution drafting by years.",
    "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும். 1946 இல் வயதுவந்தோர் வாக்குரிமையின் கீழ் நேரடித் தேர்தல் நடத்துவது சுதந்திரத்தையும் அரசியலமைப்பு உருவாக்கத்தையும் பல ஆண்டுகள் தாமதப்படுத்தாமல் நிர்வாக ரீதியாக சாத்தியமற்றதாக இருந்தது.",
    "Correct. Both A and R are true, and R correctly explains why indirect election was chosen.", "சரி. A மற்றும் R இரண்டும் சரி, R என்பது A-வின் சரியான விளக்கம்.",
    "Incorrect. R is the direct administrative rationale for A.", "தவறு. R என்பது A-விற்கான நிர்வாகக் காரணம்.",
    "Incorrect. Reason (R) is true.", "தவறு. காரணம் (R) சரியானது.",
    "Incorrect. Assertion (A) is true.", "தவறு. கூற்று (A) சரியானது.",
    "TNPSC Trap: Provincial Legislative Assemblies were elected under GoI Act 1935 with restricted franchise (only ~14% of population had voting rights).",
    "TNPSC பொறி: மாகாண சட்டமன்றங்கள் 1935 சட்டத்தின் கீழ் வரையறுக்கப்பட்ட வாக்குரிமையுடன் (மக்கள் தொகையில் ~14% மட்டுமே) தேர்ந்தெடுக்கப்பட்டவை.",
    "Despite indirect election, Granville Austin noted that the Assembly represented almost every shade of opinion in India.",
    "மறைமுகத் தேர்தல் இருந்தபோதிலும், அவை இந்தியாவின் அனைத்துக் கருத்துகளையும் பிரதிநிதித்துவப்படுத்தியதாக கிரான்வில் ஆஸ்டின் குறிப்பிட்டார்.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "Election Method", "Constituent Assembly Formation"]
))

# MIC_AR_004
questions.append(make_ar_q(
    "MIC_AR_004", "Assertion & Reason",
    "Assertion (A): Representation in the Constituent Assembly was allocated to Princely States on a population basis of roughly one seat for every one million population.\nReason (R): The Cabinet Mission Plan envisaged an integrated All-India democratic federation where representation across British Provinces and Princely States was balanced proportionately.",
    "கூற்று (A): அரசியலமைப்பு அவையில் சுதேச சமஸ்தானங்களுக்கு தோராயமாக ஒரு மில்லியன் மக்கள் தொகைக்கு ஒரு இடம் என்ற மக்கள் தொகை அடிப்படையில் இடங்கள் ஒதுக்கப்பட்டன.\nகாரணம் (R): கேபினட் தூதுக்குழு திட்டம் பிரிட்டிஷ் மாகாணங்கள் மற்றும் சுதேச சமஸ்தானங்களில் பிரதிநிதித்துவம் விகிதாசாரப்படி சீராக இருக்கும் வகையில் ஒரு ஒருங்கிணைந்த அகில இந்திய ஜனநாயகக் கூட்டமைப்பைக் கற்பனை செய்தது.",
    "A",
    "Both Assertion and Reason are true, and Reason correctly explains Assertion. Out of 389 total seats, 296 were allocated to British India and 93 to Princely States, strictly adhering to the ratio of 1 seat per 1 million people across India.",
    "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும். மொத்தமுள்ள 389 இடங்களில் 296 பிரிட்டிஷ் இந்தியாவிற்கும் 93 சமஸ்தானங்களுக்கும் 1 மில்லியன் மக்களுக்கு 1 இடம் என்ற விகிதத்தில் ஒதுக்கப்பட்டன.",
    "Correct. Both A and R are true, and R correctly explains the allocation logic.", "சரி. A மற்றும் R இரண்டும் சரி, R என்பது A-வின் சரியான விளக்கம்.",
    "Incorrect. R explains the democratic proportionality logic behind A.", "தவறு. R என்பது A-விற்கான விகிதாசாரக் காரணம்.",
    "Incorrect. Reason (R) is true.", "தவறு. காரணம் (R) சரியானது.",
    "Incorrect. Assertion (A) is true.", "தவறு. கூற்று (A) சரியானது.",
    "TNPSC Trap: Princely State representatives were initially nominated by rulers, but gradually selected in consultation with popular state people's conferences.",
    "TNPSC பொறி: சமஸ்தான பிரதிநிதிகள் தொடக்கத்தில் மன்னர்களால் பரிந்துரைக்கப்பட்டனர், பின்னர் மக்கள் அமைப்புகளுடன் கலந்தாலோசித்து தேர்ந்தெடுக்கப்பட்டனர்.",
    "Baroda was the first Princely State to send its representatives to the Constituent Assembly in April 1947.",
    "ஏப்ரல் 1947 இல் அரசியலமைப்பு அவைக்கு பிரதிநிதிகளை அனுப்பிய முதல் சுதேச சமஸ்தானம் பரோடா ஆகும்.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "Princely State Representation", "Composition"]
))

# MIC_AR_005
questions.append(make_ar_q(
    "MIC_AR_005", "Assertion & Reason",
    "Assertion (A): The Muslim League boycotted the Constituent Assembly sittings starting from December 9, 1946, demanding a separate Constituent Assembly for Pakistan.\nReason (R): The Congress interpreted provincial grouping under Cabinet Mission as voluntary, whereas the Muslim League insisted grouping was compulsory to secure Muslim-majority provincial autonomy.",
    "கூற்று (A): பாகிஸ்தானுக்கு தனி அரசியலமைப்பு அவையைக் கோரி, டிசம்பர் 9, 1946 முதல் முஸ்லீம் லீக் அரசியலமைப்பு அவைக் கூட்டங்களைப் புறக்கணித்தது.\nகாரணம் (R): கேபினட் திட்டத்தின் கீழ் மாகாணக் குழுவாக்கத்தை காங்கிரஸ் விருப்பத்திற்குரியது என விவரித்தது, ஆனால் முஸ்லீம் பெரும்பான்மை மாகாண தன்னாட்சியைப் பாதுகாக்கக் குழுவாக்கம் கட்டாயமானது என முஸ்லீம் லீக் வலியுறுத்தியது.",
    "A",
    "Both Assertion and Reason are true, and Reason correctly explains Assertion. The dispute over mandatory vs optional grouping of provinces (Section B and C) led Jawaharlal Nehru to declare in July 1946 that Congress was uncommitted to grouping, prompting the League to withdraw acceptance and boycott the Assembly.",
    "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும். கட்டாய அல்லது விருப்பக் குழுவாக்கம் பற்றிய தகராறே முஸ்லீம் லீக் அவையைப் புறக்கணிக்கக் காரணமாக அமைந்தது.",
    "Correct. Both A and R are true, and R explains the core political cause of the boycott.", "சரி. A மற்றும் R இரண்டும் சரி, R என்பது A-வின் சரியான விளக்கம்.",
    "Incorrect. R is the direct constitutional dispute explaining A.", "தவறு. R என்பது A-விற்கான நேரடி அரசியலமைப்புத் தகராறாகும்.",
    "Incorrect. Reason (R) is true.", "தவறு. காரணம் (R) சரியானது.",
    "Incorrect. Assertion (A) is true.", "தவறு. கூற்று (A) சரியானது.",
    "TNPSC Trap: Only 211 members attended the first Constituent Assembly meeting on Dec 9, 1946 due to Muslim League boycott.",
    "TNPSC பொறி: முஸ்லீம் லீக் புறக்கணிப்பு காரணமாக டிசம்பர் 9, 1946 இல் முதல் கூட்டத்தில் 211 உறுப்பினர்கள் மட்டுமே பங்கேற்றனர்.",
    "The Muslim League passed the Direct Action Day resolution on August 16, 1946.",
    "முஸ்லீம் லீக் ஆகஸ்ட் 16, 1946 இல் நேரடி நடவடிக்கை நாள் தீர்மானத்தை நிறைவேற்றியது.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "Cabinet Mission Plan", "Partition Events", "First Meeting"]
))

# MIC_AR_006
questions.append(make_chrono_q if False else make_ar_q(
    "MIC_AR_006", "Assertion & Reason",
    "Assertion (A): The Constituent Assembly of India continued constitution-framing work seamlessly after the partition of India under the Mountbatten Plan.\nReason (R): The Indian Independence Act, 1947 explicitly declared the Constituent Assembly to be a fully sovereign body with unrestricted legislative and constitutional powers.",
    "கூற்று (A): மவுண்ட்பேட்டன் திட்டத்தின் கீழ் இந்தியா பிரிக்கப்பட்ட பின்னரும் இந்திய அரசியலமைப்பு அவை அரசியலமைப்பு உருவாக்கும் பணியைத் தடையின்றித் தொடர்ந்தது.\nகாரணம் (R): 1947 இந்திய சுதந்திரச் சட்டம் அரசியலமைப்பு அவையை தடையற்ற சட்ட மற்றும் அரசியலமைப்பு அதிகாரங்களைக் கொண்ட முழுமையான இறையாண்மை கொண்ட அமைப்பாக வெளிப்படையாக அறிவித்தது.",
    "A",
    "Both Assertion and Reason are true, and Reason correctly explains Assertion. Section 8 of the Indian Independence Act 1947 removed all British parliamentary controls, making the Assembly fully sovereign to draft any Constitution and alter or repeal British statutes.",
    "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும். 1947 சுதந்திரச் சட்டத்தின் பிரிவு 8 பிரிட்டிஷ் கட்டுப்பாடுகளை நீக்கி அவைக்கு முழு இறையாண்மையை வழங்கியது.",
    "Correct. Both A and R are true, and R explains why the Assembly had legal authority to continue post-partition.", "சரி. A மற்றும் R இரண்டும் சரி, R என்பது A-வின் சரியான விளக்கம்.",
    "Incorrect. R is the exact statutory basis for A.", "தவறு. R என்பது A-விற்கான சட்டப்பூர்வ காரணம்.",
    "Incorrect. Reason (R) is true.", "தவறு. காரணம் (R) சரியானது.",
    "Incorrect. Assertion (A) is true.", "தவறு. கூற்று (A) சரியானது.",
    "TNPSC Trap: Indian Independence Act made 3 key changes to Assembly: 1. Fully sovereign body, 2. Legislative body under Mavlankar, 3. Reduced strength to 299.",
    "TNPSC பொறி: சுதந்திரச் சட்டம் அவையில் 3 மாற்றங்களைச் செய்தது: 1. இறையாண்மை அமைப்பு, 2. சட்டமன்றம் (மாவ்லங்கார்), 3. எண்ணிக்கை 299 ஆகக் குறைப்பு.",
    "Post-partition membership of Assembly was 299 (229 from Provinces + 70 from Princely States).",
    "பிரிவினைக்குப் பின் அவை உறுப்பினர் எண்ணிக்கை 299 (மாகாணங்கள் 229 + சமஸ்தானங்கள் 70).",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "Partition impact", "Reduction from 389 to 299 members"]
))

# MIC_AR_007
questions.append(make_ar_q(
    "MIC_AR_007", "Assertion & Reason",
    "Assertion (A): The Constituent Assembly set up a 7-member Drafting Committee on August 29, 1947, chaired by Dr. B.R. Ambedkar.\nReason (R): A compact expert committee of jurists was necessary to process, scrutinize, and synthesize reports of various subject committees into a coherent legal draft.",
    "கூற்று (A): ஆகஸ்ட் 29, 1947 இல் டாக்டர் பி.ஆர். அம்பேத்கர் தலைமையில் 7 உறுப்பினர்களைக் கொண்ட வரைவுக் குழுவை அரசியலமைப்பு அவை அமைத்தது.\nகாரணம் (R): பல்வேறு பாடக் குழுக்களின் அறிக்கைகளை செயலாக்கவும், ஆராயவும், ஒருமுகப்படுத்தவும் சட்ட நிபுணர்களின் சிறிய குழு அவசியமாக இருந்தது.",
    "A",
    "Both Assertion and Reason are true, and Reason correctly explains Assertion. While broad constitutional principles were decided by major committees, the detailed legal formulation required a small committee of legal experts led by Ambedkar.",
    "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும். பரந்த கொள்கைகள் முக்கியக் குழுக்களால் தீர்மானிக்கப்பட்ட நிலையில், துல்லியமான சட்ட வரைவு தயாரிப்பிற்கு அம்பேத்கரின் வரைவுக் குழு தேவைப்பட்டது.",
    "Correct. Both A and R are true, and R correctly explains the necessity of forming the Drafting Committee.", "சரி. A மற்றும் R இரண்டும் சரி, R என்பது A-வின் சரியான விளக்கம்.",
    "Incorrect. R provides the institutional rationale for A.", "தவறு. R என்பது A-விற்கான அமைப்புக் காரணமாகும்.",
    "Incorrect. Reason (R) is true.", "தவறு. காரணம் (R) சரியானது.",
    "Incorrect. Assertion (A) is true.", "தவறு. கூற்று (A) சரியானது.",
    "TNPSC Trap: Drafting Committee was set up AFTER Independence (Aug 29, 1947), NOT before.",
    "TNPSC பொறி: வரைவுக் குழு சுதந்திரத்திற்குப் பின் (ஆகஸ்ட் 29, 1947) அமைக்கப்பட்டது, அதற்கு முன் அல்ல.",
    "The Drafting Committee took less than six months to prepare its first draft published in Feb 1948.",
    "வரைவுக் குழு தனது முதல் வரைவைத் தயாரிக்க 6 மாதங்களுக்கும் குறைவான காலத்தையே எடுத்துக்கொண்டது.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "Drafting Committee", "Ambedkar"]
))

# MIC_AR_008
questions.append(make_ar_q(
    "MIC_AR_008", "Assertion & Reason",
    "Assertion (A): Sir B.N. Rau was appointed as the Constitutional Adviser to the Constituent Assembly despite not being an elected political member of the Assembly.\nReason (R): Sir B.N. Rau was an eminent jurist who possessed vast expertise in comparative constitutional law and drafted the preliminary 243-Article blueprint of the Constitution.",
    "கூற்று (A): அவையின் தேர்ந்தெடுக்கப்பட்ட அரசியல் உறுப்பினராக இல்லாதபோதிலும் சர் பி.என். ராவ் அரசியலமைப்பு அவையின் அரசியலமைப்பு ஆலோசகராக நியமிக்கப்பட்டார்.\nகாரணம் (R): சர் பி.என். ராவ் ஒப்பீட்டு அரசியலமைப்புச் சட்டத்தில் பெரும் நிபுணத்துவம் பெற்ற புகழ்பெற்ற சட்ட மேதையாக இருந்தார் மற்றும் 243 சரத்துகளைக் கொண்ட தொடக்க வரைவை எழுதினார்.",
    "A",
    "Both Assertion and Reason are true, and Reason correctly explains Assertion. Sir B.N. Rau was selected strictly for his non-partisan legal erudition and civil service experience to advise the Assembly and prepare the initial draft.",
    "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும். பி.என். ராவ் அவரது நடுநிலையான சட்டப் புலமைக்காகவே ஆலோசகராக நியமிக்கப்பட்டார்.",
    "Correct. Both A and R are true, and R explains why Rau was appointed as Adviser.", "சரி. A மற்றும் R இரண்டும் சரி, R என்பது A-வின் சரியான விளக்கம்.",
    "Incorrect. R explains the meritocratic reasoning behind A.", "தவறு. R என்பது A-விற்கான தகுதி அடிப்படையிலான காரணமாகும்.",
    "Incorrect. Reason (R) is true.", "தவறு. காரணம் (R) சரியானது.",
    "Incorrect. Assertion (A) is true.", "தவறு. கூற்று (A) சரியானது.",
    "TNPSC Trap: Sir B.N. Rau prepared the FIRST draft containing 243 Articles and 13 Schedules in October 1947.",
    "TNPSC பொறி: சர் பி.என். ராவ் அக்டோபர் 1947 இல் 243 சரத்துகள் மற்றும் 13 அட்டவணைகளைக் கொண்ட முதல் வரைவைத் தயாரித்தார்.",
    "Sir B.N. Rau later represented India at the UN Security Council and served as Judge of the ICJ at The Hague.",
    "பி.என். ராவ் பின்னர் சர்வதேச நீதிமன்ற (ICJ) நீதிபதியாகப் பணியாற்றினார்.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "B. N. Rau", "Constitutional Adviser"]
))
