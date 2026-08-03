import json
import os

questions = [
    # Q1
    {
        "id": "MIC_M_001",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "Conceptual",
        "question": {
            "en": "Why did the Cabinet Mission Plan of 1946 reject the Muslim League's demand for a fully sovereign separate state of Pakistan with its own Constituent Assembly?",
            "ta": "1946 ஆம் ஆண்டின் கேபினட் தூதுக்குழு திட்டம், தனி அரசியலமைப்பு நிர்ணய அவையுடன் கூடிய முழு இறையாண்மை கொண்ட தனிப் பாகிஸ்தான் என்ற முஸ்லிம் லீகின் கோரிக்கையை ஏன் நிராகரித்தது?"
        },
        "options": [
            {"id": "A", "en": "It concluded that a separate Pakistan would not solve the minority problem and would create insurmountable administrative, economic, and defense complications.", "ta": "தனிப் பாகிஸ்தான் சிறுபான்மையினர் சிக்கலைத் தீர்க்காது என்றும், நிர்வாக, பொருளாதார மற்றும் பாதுகாப்பு ரீதியாக சமாளிக்க முடியாத சிக்கல்களை உருவாக்கும் என்றும் முடிவுக்கு வந்தது."},
            {"id": "B", "en": "It insisted that British India should be immediately partitioned into three independent dominion countries instead of two.", "ta": "பிரிட்டிஷ் இந்தியா இரண்டிற்குப் பதிலாக மூன்று சுயாதீன டொமினியன் நாடுகளாக உடனடியாகப் பிரிக்கப்பட வேண்டும் என்று அது வற்புறுத்தியது."},
            {"id": "C", "en": "The Indian National Congress unconditionally agreed to give full veto power to the Muslim League in a unitary government.", "ta": "ஒற்றையாட்சி அரசாங்கத்தில் முஸ்லிம் லீக்கிற்கு முழு வீட்டோ அதிகாரத்தை வழங்க இந்திய தேசிய காங்கிரஸ் நிபந்தனையின்றி ஒப்புக்கொண்டது."},
            {"id": "D", "en": "The British Parliament had already passed a statutory resolution prohibiting the partition of any British territory in Asia.", "ta": "ஆசியாவில் உள்ள எந்தவொரு பிரிட்டிஷ் பகுதியையும் பிரிப்பதைத் தடுக்கும் சட்டப்பூர்வ தீர்மானத்தை பிரிட்டிஷ் நாடாளுமன்றம் ஏற்கனவே நிறைவேற்றியிருந்தது."}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "The Cabinet Mission examined the Pakistan demand and rejected it because a separate state would still leave large non-Muslim minorities in Pakistan and Muslim minorities in India, while disrupting postal, telegraph, transportation, and defense systems.",
            "ta": "கேபினட் தூதுக்குழு பாகிஸ்தான் கோரிக்கையை ஆராய்ந்து நிராகரித்தது. ஏனெனில் தனி மாநிலம் உருவானாலும் பாகிஸ்தானில் பெரும்பான்மையற்ற முஸ்லிம் அல்லாத சிறுபான்மையினரும், இந்தியாவில் முஸ்லிம் சிறுபான்மையினரும் எஞ்சுவர்; மேலும் தபால், தந்தி, போக்குவரத்து மற்றும் பாதுகாப்பு அமைப்புகள் சீர்குலையும் என்பதால்."
        },
        "why_not_others": {
            "A": {"en": "Correct. Cabinet Mission cited geographical, administrative, defense, and minority rationale for rejecting full partition.", "ta": "சரி. கேபினட் தூதுக்குழு புவியியல், நிர்வாகம், பாதுகாப்பு மற்றும் சிறுபான்மையினர் காரணங்களைச் சுட்டிக் காட்டி முழு பிரிவினையை நிராகரித்தது."},
            "B": {"en": "Incorrect. The Mission proposed a loose three-tier grouping structure, not three separate independent countries.", "ta": "தவறு. தூதுக்குழு மூன்று அடுக்கு அமைப்புக் குழுவை முன்மொழிந்ததே தவிர மூன்று தனி நாடுகளை அல்ல."},
            "C": {"en": "Incorrect. Congress strongly opposed veto powers and unitary concessions that would weaken central unity.", "ta": "தவறு. மத்திய ஒற்றுமையைப் பலவீனப்படுத்தும் வீட்டோ அதிகாரங்களை காங்கிரஸ் கடுமையாக எதிர்த்தது."},
            "D": {"en": "Incorrect. No such statutory resolution prohibiting partition was passed by British Parliament prior to 1947.", "ta": "தவறு. 1947 க்கு முன்னர் பிரிட்டிஷ் நாடாளுமன்றத்தால் அவ்வாறான சட்டப்பூர்வ தீர்மானம் எதுவும் நிறைவேற்றப்படவில்லை."}
        },
        "tnpsc_tip": {
            "en": "Remember: Cabinet Mission proposed a 3-tier grouping system (Group A, B, C) to satisfy provincial autonomy while keeping India united.",
            "ta": "நினைவில் கொள்க: இந்தியாவை ஒன்றாக வைத்திருக்கும் அதே வேளையில் மாகாண தன்னாட்சியை திருப்திப்படுத்த கேபினட் தூதுக்குழு 3-அடுக்கு குழு அமைப்பை (Group A, B, C) முன்மொழிந்தது."
        },
        "revision_fact": {
            "en": "The Cabinet Mission presented its scheme on May 16, 1946, after negotiations at Simla failed to reach an agreement.",
            "ta": "சிம்லா பேச்சுவார்த்தையில் உடன்பாடு எட்டப்படாததைத் தொடர்ந்து, கேபினட் தூதுக்குழு மே 16, 1946 அன்று தனது திட்டத்தை முன்வைத்தது."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Understand",
        "estimated_time_sec": 60,
        "pyq_similarity": "High",
        "tags": ["Cabinet Mission Plan", "Pakistan Rejection", "3-Tier Scheme"]
    },
    # Q2
    {
        "id": "MIC_M_002",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "Process-Based",
        "question": {
            "en": "Why was indirect election by provincial legislative assemblies chosen for electing representatives to the Constituent Assembly in 1946 instead of direct election based on adult franchise?",
            "ta": "1946 ஆம் ஆண்டில் அரசியலமைப்பு நிர்ணய அவை பிரதிநிதிகளைத் தேர்ந்தெடுக்க வயதுவந்தோர் வாக்குரிமை அடிப்படையிலான நேரடித் தேர்தலுக்குப் பதிலாக மாகாண சட்டமன்றங்கள் மூலமான மறைமுகத் தேர்தல் ஏன் தேர்ந்தெடுக்கப்பட்டது?"
        },
        "options": [
            {"id": "A", "en": "Conducting direct elections on adult franchise across British India would have caused severe delay in constitution-making at a critical political juncture.", "ta": "பிரிட்டிஷ் இந்தியா முழுவதும் வயதுவந்தோர் வாக்குரிமையில் நேரடித் தேர்தலை நடத்துவது, முக்கியமான அரசியல் தருணத்தில் அரசியலமைப்பு உருவாக்கத்தில் கடுமையான தாமதத்தை ஏற்படுத்தியிருக்கும்."},
            {"id": "B", "en": "The Cabinet Mission Plan explicitly prohibited native Indian citizens from voting in any national-level constitutional election.", "ta": "கேபினட் தூதுக்குழு திட்டம், சுதேசி இந்தியக் குடிமக்கள் எந்தவொரு தேசிய அளவிலான அரசியலமைப்புத் தேர்தலிலும் வாக்களிப்பதைத் தெளிவாகத் தடைசெய்தது."},
            {"id": "C", "en": "Provincial assemblies were already elected on 100% universal adult suffrage under the Government of India Act 1935.", "ta": "1935 இந்திய அரசுச் சட்டத்தின் கீழ் மாகாண சட்டமன்றங்கள் ஏற்கனவே 100% உலகளாவிய வயதுவந்தோர் வாக்குரிமையில் தேர்ந்தெடுக்கப்பட்டிருந்தன."},
            {"id": "D", "en": "The British Crown reserved the exclusive right to choose delegates if direct voting was attempted.", "ta": "நேரடி வாக்குப்பதிவு முயலப்பட்டால் பிரதிநிதிகளைத் தேர்ந்தெடுக்கும் பிரத்யேக உரிமையை பிரிட்டிஷ் அரசு தன்வசம் வைத்திருந்தது."}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Direct election based on adult franchise would have required preparing vast electoral rolls and organizing elections across undivided India, causing immense delay when immediate constitutional transfer of power was necessary.",
            "ta": "வயதுவந்தோர் வாக்குரிமை அடிப்படையில் நேரடித் தேர்தல் நடத்துவது பரந்த வாக்காளர் பட்டியல்களைத் தயாரித்து தேர்தல் நடத்த வேண்டியிருந்திருக்கும். இது உடனடி அதிகார பரிமாற்றம் தேவைப்பட்ட நேரத்தில் பெரும் தாமதத்தை ஏற்படுத்தியிருக்கும்."
        },
        "why_not_others": {
            "A": {"en": "Correct. Time factor and urgency of political transition led to choosing existing provincial assemblies as electoral colleges.", "ta": "சரி. கால காரணியும் அவசர அரசியல் மாற்றமுமே ஏற்கனவே இருந்த மாகாண சட்டமன்றங்களை வாக்காளர் மன்றமாகத் தேர்ந்தெடுக்கக் காரணமாயின."},
            "B": {"en": "Incorrect. Cabinet Mission did not prohibit native voting; it recommended the fastest feasible mode of indirect election.", "ta": "தவறு. கேபினட் தூதுக்குழு சுதேசி வாக்களிப்பைத் தடைசெய்யவில்லை; சாத்தியமான வேகமான மறைமுகத் தேர்தலையே பரிந்துரைத்தது."},
            "C": {"en": "Incorrect. 1935 Act restricted franchise based on property, tax, and education (only ~10-14% of population had voting rights).", "ta": "தவறு. 1935 சட்டம் சொத்து, வரி, கல்வி அடிப்படையில் வாக்குரிமையைக் கட்டுப்படுத்தியது (~10-14% மக்கள் மட்டுமே வாக்களிக்க முடிந்தது)."},
            "D": {"en": "Incorrect. The British Crown had agreed to transfer power and did not demand delegate selection rights.", "ta": "தவறு. பிரிட்டிஷ் அரசு அதிகாரத்தை மாற்ற ஒப்புக்கொண்டது மற்றும் பிரதிநிதிகளைத் தேர்ந்தெடுக்கும் உரிமையைக் கோரவில்லை."}
        },
        "tnpsc_tip": {
            "en": "Note: Even though the Assembly was indirectly elected, Ambedkar noted that it represented all political, social, and cultural sections of India.",
            "ta": "குறிப்பு: நிர்ணய அவை மறைமுகமாகத் தேர்ந்தெடுக்கப்பட்ட போதிலும், அது இந்தியாவின் அனைத்து அரசியல், சமூக, பண்பாட்டுப் பிரிவுகளையும் பிரதிநிதித்துவப்படுத்தியது என்று அம்பேத்கர் குறிப்பிட்டார்."
        },
        "revision_fact": {
            "en": "The provincial legislative assemblies elected in early 1946 served as the electoral college for the Constituent Assembly.",
            "ta": "1946 இன் தொடக்கத்தில் தேர்ந்தெடுக்கப்பட்ட மாகாண சட்டமன்றங்களே அரசியலமைப்பு நிர்ணய அவைகான வாக்காளர் மன்றமாகச் செயல்பட்டன."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Understand",
        "estimated_time_sec": 60,
        "pyq_similarity": "High",
        "tags": ["Indirect Election Rationale", "1946 Elections", "Franchise Limitations"]
    },
    # Q3
    {
        "id": "MIC_M_003",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "Constitutional Understanding",
        "question": {
            "en": "What principle was adopted under the Cabinet Mission Plan to determine the number of seats allocated to each Province and Princely State in the Constituent Assembly?",
            "ta": "அரசியலமைப்பு நிர்ணய அவையில் ஒவ்வொரு மாகாணத்திற்கும் சுதேச அரசிற்கும் ஒதுக்கப்பட்ட இடங்களின் எண்ணிக்கையைத் தீர்மானிக்க கேபினட் தூதுக்குழு திட்டத்தின் கீழ் எந்தக் கோட்பாடு பின்பற்றப்பட்டது?"
        },
        "options": [
            {"id": "A", "en": "Proportional representation based on population, roughly at the ratio of one seat per one million population.", "ta": "மக்கள் தொகைக்கு ஏற்ற விகிதாசாரப் பிரதிநிதித்துவம், தோராயமாக ஒரு மில்லியன் (10 லட்சம்) மக்கள் தொகைக்கு ஒரு இடம் என்ற விகிதத்தில்."},
            {"id": "B", "en": "Equal representation to all provinces regardless of size or population, similar to the US Senate.", "ta": "அளவோ மக்கள் தொகையோ பொருட்படுத்தாமல் அனைத்து மாகாணங்களுக்கும் அமெரிக்க செனட் போல் சமமான பிரதிநிதித்துவம்."},
            {"id": "C", "en": "Allocation based strictly on revenue contribution and land area of each province.", "ta": "ஒவ்வொரு மாகாணத்தின் வருவாய் பங்களிப்பு மற்றும் நிலப்பரப்பின் அடிப்படையில் மட்டுமே இடங்கள் ஒதுக்கீடு."},
            {"id": "D", "en": "Weightage allotment favoring princely states over British Indian provinces.", "ta": "பிரிட்டிஷ் இந்திய மாகாணங்களை விட சுதேச அரசுகளுக்கு சாதகமான கூடுதல் எடை ஒதுக்கீடு (Weightage allotment)."}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Seats allocated to each province and princely state were directly proportional to their population, roughly in the ratio of one seat for every one million (10 lakh) people.",
            "ta": "ஒவ்வொரு மாகாணத்திற்கும் சுதேச அரசிற்கும் ஒதுக்கப்பட்ட இடங்கள் அவற்றின் மக்கள் தொகைக்கு நேரடி விகிதத்தில் இருந்தன, தோராயமாக ஒவ்வொரு 10 லட்சம் மக்களுக்கு ஒரு இடம் என்ற விகிதத்தில்."
        },
        "why_not_others": {
            "A": {"en": "Correct. Ratio was 1 seat per 1 million population.", "ta": "சரி. விகிதம் 10 லட்சம் மக்களுக்கு 1 இடம்."},
            "B": {"en": "Incorrect. Equal representation per unit was not adopted; population strength was the basis.", "ta": "தவறு. அலகுக்கு சம பிரதிநிதித்துவம் பின்பற்றப்படவில்லை; மக்கள் தொகை பலமே அடிப்படையாக இருந்தது."},
            "C": {"en": "Incorrect. Revenue and land area were not criteria for seat allocation.", "ta": "தவறு. வருவாய் மற்றும் நிலப்பரப்பு இட ஒதுக்கீட்டிற்கான அளவுகோல்கள் அல்ல."},
            "D": {"en": "Incorrect. No special weightage was given; uniform population ratio applied to both provinces and princely states.", "ta": "தவறு. சிறப்பு கூடுதல் எடை வழங்கப்படவில்லை; மாகாணங்கள் மற்றும் சுதேச அரசுகள் இரண்டிற்கும் சீரான மக்கள் தொகை விகிதம் பயன்படுத்தப்பட்டது."}
        },
        "tnpsc_tip": {
            "en": "Example: Madras Province had 49 seats allocated based on its ~49 million population in 1946.",
            "ta": "எடுத்துக்காட்டு: மதராஸ் மாகாணத்தின் 1946 இன் ~4.9 கோடி மக்கள் தொகைக்கு ஏற்ப 49 இடங்கள் ஒதுக்கப்பட்டன."
        },
        "revision_fact": {
            "en": "Out of 296 British Indian seats, 210 were General, 78 Muslims, and 4 Sikhs (in Punjab).",
            "ta": "296 பிரிட்டிஷ் இந்திய இடங்களில், 210 பொது, 78 முஸ்லிம்கள், மற்றும் 4 சீக்கியர்கள் (பஞ்சாபில்) ஒதுக்கப்பட்டன."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Understand",
        "estimated_time_sec": 50,
        "pyq_similarity": "High",
        "tags": ["Seat Allocation Ratio", "1 Million Population", "Proportional Representation"]
    },
    # Q4
    {
        "id": "MIC_M_004",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "TNPSC Trap Questions",
        "question": {
            "en": "Regarding the communal representation scheme in the British Indian provinces under the Cabinet Mission Plan, which three main communities were officially recognized for seat division?",
            "ta": "கேபினட் தூதுக்குழு திட்டத்தின் கீழ் பிரிட்டிஷ் இந்திய மாகாணங்களில் வகுப்புவாதப் பிரதிநிதித்துவத் திட்டத்தின் படி, இடப் பகிர்விற்காக அதிகாரப்பூர்வமாக அங்கீகரிக்கப்பட்ட மூன்று முதன்மைச் சமூகங்கள் எவை?"
        },
        "options": [
            {"id": "A", "en": "Muslims, Sikhs, and General (all except Muslims and Sikhs)", "ta": "முஸ்லிம்கள், சீக்கியர்கள் மற்றும் பொதுப் பிரிவினர் (முஸ்லிம்கள் மற்றும் சீக்கியர்கள் தவிர மற்ற அனைவரும்)"},
            {"id": "B", "en": "Hindus, Muslims, and Scheduled Castes", "ta": "இந்துக்கள், முஸ்லிம்கள் மற்றும் பட்டியல் சாதியினர்"},
            {"id": "C", "en": "Hindus, Muslims, and Christians", "ta": "இந்துக்கள், முஸ்லிம்கள் மற்றும் கிறிஸ்தவர்கள்"},
            {"id": "D", "en": "British, Muslims, and Non-Muslims", "ta": "பிரிட்டிஷார், முஸ்லிம்கள் மற்றும் முஸ்லிம் அல்லாதோர்"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Seats allocated to each British province were divided among three main communities in proportion to their population: Muslims, Sikhs, and General (which included Hindus, SCs, STs, Christians, Anglo-Indians, etc.).",
            "ta": "ஒவ்வொரு பிரிட்டிஷ் மாகாணத்திற்கும் ஒதுக்கப்பட்ட இடங்கள் அவர்களின் மக்கள் தொகைக்கு ஏற்ப மூன்று முக்கிய சமூகங்களிடையே பிரிக்கப்பட்டன: முஸ்லிம்கள், சீக்கியர்கள் மற்றும் பொதுப் பிரிவினர் (இதில் இந்துக்கள், பட்டியல் பிரிவினர், கிறிஸ்தவர்கள் போன்றோர் அடங்குவர்)."
        },
        "why_not_others": {
            "A": {"en": "Correct. The 3 recognized groups were Muslims, Sikhs, and General.", "ta": "சரி. அங்கீகரிக்கப்பட்ட 3 குழுக்கள் முஸ்லிம்கள், சீக்கியர்கள் மற்றும் பொதுப் பிரிவினர்."},
            "B": {"en": "Incorrect Trap. Hindus and Scheduled Castes were grouped under 'General', not separate electoral categories in 1946 plan.", "ta": "தவறு வலை. இந்துக்களும் பட்டியல் வகுப்பினரும் 'பொது' பிரிவின் கீழ் சேர்க்கப்பட்டனர், தனிப் பிரிவாக அல்ல."},
            "C": {"en": "Incorrect. Christians were part of General category.", "ta": "தவறு. கிறிஸ்தவர்கள் பொதுப் பிரிவின் ஒரு பகுதியாக இருந்தனர்."},
            "D": {"en": "Incorrect. British were not an electoral category in the Assembly scheme.", "ta": "தவறு. பிரிட்டிஷார் நிர்ணய அவை திட்டத்தில் வாக்காளர் பிரிவாக இல்லை."}
        },
        "tnpsc_tip": {
            "en": "Sikhs were given separate communal representation only in the province of Punjab.",
            "ta": "சீக்கியர்களுக்கு பஞ்சாப் மாகாணத்தில் மட்டுமே தனி வகுப்புவாத பிரதிநிதித்துவம் வழங்கப்பட்டது."
        },
        "revision_fact": {
            "en": "Members of each community in the provincial legislative assembly elected their own representatives using single transferable vote.",
            "ta": "மாகாண சட்டமன்றத்தில் உள்ள ஒவ்வொரு சமூகத்தின் உறுப்பினர்களும் ஒற்றை மாற்றத்தக்க வாக்கு மூலம் தங்கள் சொந்த பிரதிநிதிகளைத் தேர்ந்தெடுத்தனர்."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Understand",
        "estimated_time_sec": 55,
        "pyq_similarity": "High",
        "tags": ["Communal Representation", "Muslims Sikhs General", "Cabinet Mission"]
    },
    # Q5
    {
        "id": "MIC_M_005",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "Conceptual",
        "question": {
            "en": "Why did representatives of the Princely States stay away from the Constituent Assembly during its initial sittings in December 1946?",
            "ta": "டிசம்பர் 1946 இல் நடைபெற்ற ஆரம்ப அமர்வுகளின் போது சுதேச அரசுகளின் பிரதிநிதிகள் அரசியலமைப்பு நிர்ணய அவையிலிருந்து ஏன் விலகியிருந்தனர்?"
        },
        "options": [
            {"id": "A", "en": "They were uncertain about the future political status of their states and preferred to wait until British paramountcy officially lapsed.", "ta": "அவர்கள் தங்கள் அரசுகளின் எதிர்கால அரசியல் நிலை குறித்து உறுதியற்ற தன்மையில் இருந்தனர் மற்றும் பிரிட்டிஷ் மேலாதிக்கம் அதிகாரப்பூர்வமாக முடியும் வரை காத்திருக்க விரும்பினர்."},
            {"id": "B", "en": "The Cabinet Mission Plan explicitly barred rulers of Princely States from sending delegates until 1948.", "ta": "கேபினட் தூதுக்குழு திட்டம் 1948 வரை சுதேச அரசுகளின் ஆட்சியாளர்கள் பிரதிநிதிகளை அனுப்புவதைத் தெளிவாகத் தடைசெய்திருந்தது."},
            {"id": "C", "en": "The Constituent Assembly passed a resolution declaring all Princely States to be immediately merged into British provinces.", "ta": "அனைத்து சுதேச அரசுகளும் பிரிட்டிஷ் மாகாணங்களுடன் உடனடியாக இணைக்கப்பட வேண்டும் என்று அரசியலமைப்பு நிர்ணய அவை ஒரு தீர்மானத்தை நிறைவேற்றியது."},
            {"id": "D", "en": "The League of Nations advised the Princely States not to join any assembly formed without British military guarantees.", "ta": "பிரிட்டிஷ் ராணுவ உத்தரவாதங்கள் இன்றி உருவாக்கப்படும் எந்தவொரு அவையிலும் சேர வேண்டாம் என்று சர்வதேச சங்கம் சுதேச அரசுகளுக்கு அறிவுறுத்தியது."}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "The rulers of Princely States were hesitant about their sovereignty and integration. They waited to see the outcome of the political rift between Congress and Muslim League before deciding to send nominated members.",
            "ta": "சுதேச அரசுகளின் ஆட்சியாளர்கள் தங்கள் இறையாண்மை மற்றும் இணைப்பு குறித்து தயக்கம் காட்டினர். நியமிக்கப்பட்ட உறுப்பினர்களை அனுப்புவதை முடிவு செய்வதற்கு முன் காங்கிரஸ் மற்றும் முஸ்லிம் லீக் இடையேயான அரசியல் மோதலின் முடிவைப் பார்க்க அவர்கள் காத்திருந்தனர்."
        },
        "why_not_others": {
            "A": {"en": "Correct. Uncertainty over paramountcy and future status kept them away initially.", "ta": "சரி. மேலாதிக்கம் மற்றும் எதிர்கால நிலைமை பற்றிய உறுதியற்ற தன்மையே ஆரம்பத்தில் அவர்களை விலக்கி வைத்தது."},
            "B": {"en": "Incorrect. Cabinet Mission allocated 93 seats for princely states to join immediately.", "ta": "தவறு. கேபினட் தூதுக்குழு சுதேச அரசுகள் உடனடியாக சேர 93 இடங்களை ஒதுக்கியிருந்தது."},
            "C": {"en": "Incorrect. No such forced merger resolution was passed by the Assembly in 1946.", "ta": "தவறு. 1946 இல் அவையால் அத்தகைய கட்டாய இணைப்புத் தீர்மானம் எதுவும் நிறைவேற்றப்படவில்லை."},
            "D": {"en": "Incorrect. League of Nations had no role or advisory function in Indian constitution-making.", "ta": "தவறு. இந்திய அரசியலமைப்பு உருவாக்கத்தில் சர்வதேச சங்கத்திற்கு எந்தப்ங்கும் இல்லை."}
        },
        "tnpsc_tip": {
            "en": "On April 28, 1947, representatives of 6 Princely States (Baroda, Bikaner, Jaipur, Patiala, Rewa, Udaipur) joined the Assembly for the first time.",
            "ta": "ஏப்ரல் 28, 1947 அன்று, 6 சுதேச அரசுகளின் பிரதிநிதிகள் (பரோடா, பிகானேர், ஜெய்ப்பூர், பாட்டியாலா, ரேவா, உதய்பூர்) முதன்முறையாக அவையில் இணைந்தனர்."
        },
        "revision_fact": {
            "en": "Gradually, after Mountbatten Plan of June 3, 1947, most Princely States took their seats in the Assembly.",
            "ta": "ஜூன் 3, 1947 மவுண்ட்பேட்டன் திட்டத்திற்குப் பிறகு, பெரும்பாலான சுதேச அரசுகள் அவையில் தங்கள் இடங்களை ஏற்றுக்கொண்டன."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Understand",
        "estimated_time_sec": 55,
        "pyq_similarity": "High",
        "tags": ["Princely States Hesitation", "Paramountcy", "April 1947 Entry"]
    },
    # Q6
    {
        "id": "MIC_M_006",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "Conceptual",
        "question": {
            "en": "What was the significance of moving the historic 'Objectives Resolution' by Pandit Jawaharlal Nehru on December 13, 1946, before starting the detailed drafting of the Constitution?",
            "ta": "அரசியலமைப்பின் விரிவான வரைவைத் தொடங்குவதற்கு முன், டிசம்பர் 13, 1946 அன்று பண்டிதர் ஜவஹர்லால் நேரு வரலாற்றுச் சிறப்புமிக்க 'குறிக்கோள் தீர்மானத்தை' முன்மொழிந்ததன் முக்கியத்துவம் யாது?"
        },
        "options": [
            {"id": "A", "en": "It laid down the underlying philosophy, fundamental principles, and socio-economic vision that would guide the entire constitution-making process.", "ta": "இது முழு அரசியலமைப்பு உருவாக்க செயல்முறையையும் வழிநடத்தும் அடிப்படைத் தத்துவம், முதன்மைக் கோட்பாடுகள் மற்றும் சமூக-பொருளாதாரப் பார்வையை வகுத்துத் தந்தது."},
            {"id": "B", "en": "It served as an immediate ultimatum to the British Crown to withdraw all armed forces from India within 30 days.", "ta": "இது 30 நாட்களுக்குள் அனைத்து ஆயுதப்படைகளையும் இந்தியாவிலிருந்து திரும்பப் பெறுமாறு பிரிட்டிஷ் அரசிற்கு வழங்கப்பட்ட உடனடி இறுதி எச்சரிக்கையாகச் செயல்பட்டது."},
            {"id": "C", "en": "It established the detailed framework for the division of legislative subjects between Union and State lists.", "ta": "இது மத்திய மற்றும் மாநிலப் பட்டியல்களுக்கு இடையேயான சட்டத்துறை பாடப் பகிர்விற்கான விரிவான கட்டமைப்பை நிறுவியது."},
            {"id": "D", "en": "It automatically dissolved all provincial assemblies and declared the Constituent Assembly as the sole national tax authority.", "ta": "இது அனைத்து மாகாண சட்டமன்றங்களையும் தானாகவே கலைத்து, நிர்ணய அவையை ஒரே தேசிய வரி அதிகார அமைப்பாக அறிவித்தது."}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "The Objectives Resolution outlined the ideal of an Independent Sovereign Republic, guaranteed justice, equality, freedom, and safeguards for minorities, serving as the guiding light and philosophical cornerstone for drafting the Constitution.",
            "ta": "குறிக்கோள் தீர்மானம் ஒரு சுதந்திர இறையாண்மை கொண்ட குடியரசின் இலட்சியத்தையும், நீதி, சமத்துவம், சுதந்திரம் மற்றும் சிறுபான்மையினருக்கான பாதுகாப்புகளையும் வரைறுத்து, அரசியலமைப்பு வரைவிற்கான வழிகாட்டி ஒளியாகவும் தத்துவக் கல்லாகவும் செயல்பட்டது."
        },
        "why_not_others": {
            "A": {"en": "Correct. Objectives Resolution defined the guiding values and philosophy of the proposed Indian Republic.", "ta": "சரி. குறிக்கோள் தீர்மானம் முன்மொழியப்பட்ட இந்தியக் குடியரசின் வழிகாட்டு மதிப்புகளையும் தத்துவத்தையும் வரையறுத்தது."},
            "B": {"en": "Incorrect. It was not a military ultimatum to Britain.", "ta": "தவறு. இது பிரிட்டனுக்கான ராணுவ இறுதி எச்சரிக்கை அல்ல."},
            "C": {"en": "Incorrect. Legislative lists were drafted later by specific committees.", "ta": "தவறு. சட்டத்துறை பட்டியல்கள் பின்னர் குறிப்பிட்ட குழுக்களால் வரைவு செய்யப்பட்டன."},
            "D": {"en": "Incorrect. It did not dissolve provincial assemblies or act as a tax decree.", "ta": "தவறு. இது மாகாண சட்டமன்றங்களை கலைக்கவில்லை அல்லது வரி ஆணையாக செயல்படவில்லை."}
        },
        "tnpsc_tip": {
            "en": "Nehru described the Objectives Resolution as 'a declaration, a firm resolve, a pledge and an undertaking'.",
            "ta": "நேரு குறிக்கோள் தீர்மானத்தை 'ஒரு பிரகடனம், ஒரு உறுதியான தீர்மானம், ஒரு சூளுரை மற்றும் ஒரு பொறுப்பேற்பு' என்று விவரித்தார்."
        },
        "revision_fact": {
            "en": "The Objectives Resolution was unanimously adopted on January 22, 1947.",
            "ta": "குறிக்கோள் தீர்மானம் ஜனவரி 22, 1947 அன்று ஒருமனதாக ஏற்றுக்கொள்ளப்பட்டது."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Understand",
        "estimated_time_sec": 55,
        "pyq_similarity": "High",
        "tags": ["Objectives Resolution Significance", "Jawaharlal Nehru", "Dec 13 1946"]
    },
    # Q7
    {
        "id": "MIC_M_007",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "Constitutional Understanding",
        "question": {
            "en": "According to the Objectives Resolution introduced by Nehru, from where does all authority and power of sovereign independent India derive?",
            "ta": "நேருவால் அறிமுகப்படுத்தப்பட்ட குறிக்கோள் தீர்மானத்தின்படி, இறையாண்மை கொண்ட சுதந்திர இந்தியாவின் அனைத்து அதிகாரங்களும் பலமும் எங்கிருந்து பெறப்படுகின்றன?"
        },
        "options": [
            {"id": "A", "en": "The People of India", "ta": "இந்திய மக்கள்"},
            {"id": "B", "en": "The Constituent Assembly of India", "ta": "இந்திய அரசியலமைப்பு நிர்ணய அவை"},
            {"id": "C", "en": "The British Crown and Parliament", "ta": "பிரிட்டிஷ் அரசர் மற்றும் நாடாளுமன்றம்"},
            {"id": "D", "en": "The Supreme Court of India", "ta": "இந்திய உச்ச நீதிமன்றம்"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Paragraph 5 of the Objectives Resolution explicitly declared that 'all power and authority of the Sovereign Independent India, its constituent parts and organs of government, are derived from the people'.",
            "ta": "குறிக்கோள் தீர்மானத்தின் 5வது பத்தி, 'இறையாண்மை கொண்ட சுதந்திர இந்தியாவின் அனைத்து அதிகாரங்களும், அதன் கூறுகளும் மற்றும் அரசாங்க அமைப்புகளும் மக்களிடமிருந்தே பெறப்படுகின்றன' என்று தெளிவாகப் பிரகடனம் செய்தது."
        },
        "why_not_others": {
            "A": {"en": "Correct. Popular Sovereignty (The People) is the ultimate source of authority.", "ta": "சரி. மக்கள் இறையாண்மையே (இந்திய மக்கள்) அதிகாரத்தின் இறுதி ஆதாரமாகும்."},
            "B": {"en": "Incorrect. The Assembly derives its mandate from the people, it is not the ultimate source itself.", "ta": "தவறு. அவை தனது அதிகாரத்தை மக்களிடமிருந்தே பெறுகிறது, அதுவே மூல ஆதாரம் அல்ல."},
            "C": {"en": "Incorrect. The Resolution repudiated British imperial sovereignty.", "ta": "தவறு. இத்தீர்மானம் பிரிட்டிஷ் ஏகாதிபத்திய இறையாண்மையை நிராகரித்தது."},
            "D": {"en": "Incorrect. Judiciary is an organ under the Constitution, not the source of sovereign power.", "ta": "தவறு. நீதித்துறை அரசியலமைப்பின் ஒரு அங்கம், இறையாண்மை அதிகாரத்தின் ஆதாரம் அல்ல."}
        },
        "tnpsc_tip": {
            "en": "This concept of Popular Sovereignty is reflected in the opening words of the Preamble: 'WE, THE PEOPLE OF INDIA...'",
            "ta": "இந்த மக்கள் இறையாண்மைக் கோட்பாடு முகப்புரையின் தொடக்கச் சொற்களில் பிரதிபலிக்கிறது: 'இந்திய மக்களாகிய நாம்...'."
        },
        "revision_fact": {
            "en": "This principle established democratic republic as the non-negotiable bedrock of Indian constitutionalism.",
            "ta": "இக்கோட்பாடு ஜனநாயகக் குடியரசை இந்திய அரசியலமைப்பின் சமரசமற்ற அடித்தளமாக நிறுவியது."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Understand",
        "estimated_time_sec": 50,
        "pyq_similarity": "High",
        "tags": ["Popular Sovereignty", "Objectives Resolution", "People Source of Power"]
    },
    # Q8
    {
        "id": "MIC_M_008",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "Process-Based",
        "question": {
            "en": "How did the Indian Independence Act of 1947 alter the relationship between the Constituent Assembly and the British Parliament?",
            "ta": "1947 ஆம் ஆண்டின் இந்திய சுதந்திரச் சட்டம், அரசியலமைப்பு நிர்ணய அவைக்கும் பிரிட்டிஷ் நாடாளுமன்றத்திற்கும் இடையிலான உறவை எவ்வாறு மாற்றியமைத்தது?"
        },
        "options": [
            {"id": "A", "en": "It conferred complete sovereign authority on the Assembly, empowering it to revoke or alter any Act of the British Parliament applying to India.", "ta": "இது அவைக்கு முழு இறையாண்மை அதிகாரத்தை வழங்கியது, இந்தியாவிற்குப் பொருந்தும் பிரிட்டிஷ் நாடாளுமன்றத்தின் எந்தவொரு சட்டத்தையும் ரத்து செய்ய அல்லது மாற்றியமைக்க அவைக்கு அதிகாரம் அளித்தது."},
            {"id": "B", "en": "It required all draft constitutional provisions to receive prior royal assent from the King of Great Britain.", "ta": "அனைத்து வரைவு அரசியலமைப்பு விதிகளும் கிரேட் பிரிட்டன் அரசரின் முன் அரச ஒப்புதலைப் பெற வேண்டும் என்று அது கோரியது."},
            {"id": "C", "en": "It limited the Assembly's power to framing economic policies while keeping criminal legislation under British courts.", "ta": "குற்றவியல் சட்டங்களை பிரிட்டிஷ் நீதிமன்றங்களின் கீழ் வைத்துக்கொண்டு, பொருளாதாரக் கொள்கைகளை வரைவதோடு அவையின் அதிகாரத்தைக் கட்டுப்படுத்தியது."},
            {"id": "D", "en": "It placed the Assembly under the direct administrative supervision of the British Privy Council until 1955.", "ta": "1955 வரை பிரிட்டிஷ் பிரிவி கவுன்சிலின் நேரடி நிர்வாக மேற்பார்வையின் கீழ் அவையை வைத்தது."}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Section 8 of the Indian Independence Act 1947 declared the Assembly to be a fully sovereign body, removing all limitations imposed by the Cabinet Mission and authorizing it to repeal or amend any British statute (including the 1947 Act itself).",
            "ta": "1947 இந்திய சுதந்திரச் சட்டத்தின் 8வது பிரிவு நிர்ணய அவையை முழு இறையாண்மை கொண்ட அமைப்பாக அறிவித்தது. இது கேபினட் தூதுக்குழு விதித்த அனைத்துக் கட்டுப்பாடுகளையும் நீக்கி, எந்தவொரு பிரிட்டிஷ் சட்டத்தையும் ரத்து செய்ய அல்லது திருத்த அவைக்கு அதிகாரம் அளித்தது."
        },
        "why_not_others": {
            "A": {"en": "Correct. Assembly became a sovereign body with power to repeal any British law.", "ta": "சரி. பிரிட்டிஷ் சட்டங்களை ரத்து செய்யும் அதிகாரத்துடன் அவை இறையாண்மை அமைப்பாக மாறியது."},
            "B": {"en": "Incorrect. Royal assent requirement was abolished.", "ta": "தவறு. அரச ஒப்புதல் தேவை ஒழிக்கப்பட்டது."},
            "C": {"en": "Incorrect. Assembly obtained full plenary powers over all legal subjects.", "ta": "தவறு. அனைத்து சட்டப் பாடங்கள் மீதும் அவை முழுமையான அதிகாரத்தைப் பெற்றது."},
            "D": {"en": "Incorrect. Privy Council jurisdiction was abolished by the Constituent Assembly in 1949.", "ta": "தவறு. 1949 இல் அரசியலமைப்பு நிர்ணய அவையால் பிரிவி கவுன்சில் அதிகார வரம்பு ஒழிக்கப்பட்டது."}
        },
        "tnpsc_tip": {
            "en": "Three key changes made by 1947 Act: 1. Made Assembly Sovereign, 2. Assigned Legislative role, 3. Reduced membership to 299.",
            "ta": "1947 சட்டத்தால் செய்யப்பட்ட மூன்று முக்கிய மாற்றங்கள்: 1. அவையை இறையாண்மையுடையதாக்கியது, 2. சட்டமன்றப் பணியை வழங்கியது, 3. உறுப்பினர் எண்ணிக்கையை 299 ஆகக் குறைத்தது."
        },
        "revision_fact": {
            "en": "Abolition of Privy Council Jurisdiction Act was enacted in September 1949 by the Constituent Assembly.",
            "ta": "பிரிவி கவுன்சில் அதிகார வரம்பு ஒழிப்புச் சட்டம் செப்டம்பர் 1949 இல் நிர்ணய அவையால் இயற்றப்பட்டது."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Understand",
        "estimated_time_sec": 55,
        "pyq_similarity": "High",
        "tags": ["Indian Independence Act 1947", "Sovereign Assembly", "Repeal Powers"]
    },
    # Q9
    {
        "id": "MIC_M_009",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "Process-Based",
        "question": {
            "en": "Why did the Constituent Assembly function as a dual-role body after August 15, 1947, and how were these roles distinguished?",
            "ta": "ஆகஸ்ட் 15, 1947க்குப் பிறகு அரசியலமைப்பு நிர்ணய அவை ஏன் இரட்டைப் பணி அமைப்பாகச் செயல்பட்டது, மேலும் இந்த பாத்திரங்கள் எவ்வாறு வேறுபடுத்தப்பட்டன?"
        },
        "options": [
            {"id": "A", "en": "It functioned as a Constituent body chaired by Dr. Rajendra Prasad to draft the Constitution, and as a Legislative body chaired by G.V. Mavlankar to enact ordinary laws.", "ta": "இது அரசியலமைப்பை வரைவதற்கு டாக்டர் ராஜேந்திர பிரசாத் தலைமையில் அரசியலமைப்பு அமைப்பாகவும், சாதாரண சட்டங்களை இயற்ற ஜி.வி. மாவலங்கர் தலைமையில் சட்டமன்ற அமைப்பாகவும் செயல்பட்டது."},
            {"id": "B", "en": "It functioned as an executive cabinet chaired by Nehru and a judicial supreme court chaired by H.J. Kania.", "ta": "இது நேரு தலைமையில் ஒரு நிர்வாக அமைச்சரவையாகவும், எச்.ஜே. கானியா தலைமையில் ஒரு நீதித்துறை உச்ச நீதிமன்றமாகவும் செயல்பட்டது."},
            {"id": "C", "en": "It functioned as a federal senate chaired by Patel and a provincial assembly chaired by Ambedkar.", "ta": "இது படேல் தலைமையில் ஒரு கூட்டாட்சி மேலவையாகவும், அம்பேத்கர் தலைமையில் ஒரு மாகாண அவையாகவும் செயல்பட்டது."},
            {"id": "D", "en": "It functioned as a military defense council during daytime and a legislative drafting body at night.", "ta": "இது பகல் நேரத்தில் ராணுவப் பாதுகாப்புக் குழுவாகவும் இரவில் சட்ட வரைவுக் குழுவாகவும் செயல்பட்டது."}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "After independence, the Assembly became the Provisional Parliament of India. To separate constitution-making from day-to-day lawmaking, it met as a Constituent body under Dr. Rajendra Prasad and as a Legislative body under G.V. Mavlankar on separate days.",
            "ta": "சுதந்திரத்திற்குப் பிறகு, அவை இந்தியாவின் தற்காலிக நாடாளுமன்றமாக மாறியது. அரசியலமைப்பு உருவாக்கத்தை அன்றாட சட்டமியற்றலிலிருந்து பிரிக்க, அது டாக்டர் ராஜேந்திர பிரசாத் தலைமையில் அரசியலமைப்பு அமைப்பாகவும், ஜி.வி. மாவலங்கர் தலைமையில் சட்டமன்ற அமைப்பாகவும் வெவ்வேறு நாட்களில் கூடியது."
        },
        "why_not_others": {
            "A": {"en": "Correct. Rajendra Prasad chaired constituent sittings; G.V. Mavlankar chaired legislative sittings.", "ta": "சரி. ராஜேந்திர பிரசாத் அரசியலமைப்பு அமர்வுகளுக்குத் தலைமை தாங்கினார்; ஜி.வி. மாவலங்கர் சட்டமன்ற அமர்வுகளுக்குத் தலைமை தாங்கினார்."},
            "B": {"en": "Incorrect. Executive cabinet was headed by Prime Minister Nehru, but Assembly was not acting as supreme court.", "ta": "தவறு. நிர்வாக அமைச்சரவை பிரதமர் நேரு தலைமையில் இருந்தது, ஆனால் அவை உச்ச நீதிமன்றமாக செயல்படவில்லை."},
            "C": {"en": "Incorrect. Assembly was a unicameral body acting in dual capacities.", "ta": "தவறு. அவை இருவேறு திறன்களில் செயல்படும் ஓரவை அமைப்பாக இருந்தது."},
            "D": {"en": "Incorrect. Day/night military distinction is factually incorrect.", "ta": "தவறு. பகல்/இரவு ராணுவப் பாகுபாடு என்பது தவறானது."}
        },
        "tnpsc_tip": {
            "en": "These dual functions continued until November 26, 1949, when constitution-making was finished.",
            "ta": "அரசியலமைப்பு உருவாக்கம் முடிந்த நவம்பர் 26, 1949 வரை இந்த இரட்டைப் பணிகள் தொடர்ந்தன."
        },
        "revision_fact": {
            "en": "On November 17, 1947, G.V. Mavlankar was elected as the Speaker of the Assembly (Legislative).",
            "ta": "நவம்பர் 17, 1947 அன்று ஜி.வி. மாவலங்கர் அவையின் (சட்டமன்றம்) சபாநாயகராகத் தேர்ந்தெடுக்கப்பட்டார்."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Understand",
        "estimated_time_sec": 55,
        "pyq_similarity": "High",
        "tags": ["Dual Function Assembly", "Rajendra Prasad", "G.V. Mavlankar"]
    },
    # Q10
    {
        "id": "MIC_M_010",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "Conceptual",
        "question": {
            "en": "What was the fundamental role played by Sir B.N. Rau, the Constitutional Adviser to the Constituent Assembly?",
            "ta": "அரசியலமைப்பு நிர்ணய அவையின் அரசியலமைப்பு ஆலோசகரான சர் பி.என். ராவ் ஆற்றிய அடிப்படைப் பங்கு யாது?"
        },
        "options": [
            {"id": "A", "en": "He prepared the initial raw Draft Constitution based on reports of various committees and extensive international legal research before the Drafting Committee was formed.", "ta": "வரைவுக் குழு உருவாக்கப்படுவதற்கு முன், பல்வேறு குழுக்களின் அறிக்கைகள் மற்றும் பரந்த சர்வதேச சட்ட ஆராய்ச்சியின் அடிப்படையில் ஆரம்ப மூல வரைவு அரசியலமைப்பை அவர் தயாரித்தார்."},
            {"id": "B", "en": "He served as the elected Chairman of the Steering Committee responsible for guiding day-to-day assembly debates.", "ta": "அன்றாட அவை விவாதங்களை வழிநடத்துவதற்குப் பொறுப்பான வழிகாட்டும் குழுவின் தேர்ந்தெடுக்கப்பட்ட தலைவராக அவர் பணியாற்றினார்."},
            {"id": "C", "en": "He was the Finance Minister who audited the overall expenditure of constitution-making.", "ta": "அவர் அரசியலமைப்பு உருவாக்கத்தின் மொத்த செலவையும் தணிக்கை செய்த நிதி அமைச்சராவார்."},
            {"id": "D", "en": "He translated the entire Constitution into Tamil and Bengali official versions.", "ta": "அவர் முழு அரசியலமைப்பையும் தமிழ் மற்றும் வங்காள அதிகாரப்பூர்வ பதிப்புகளில் மொழிபெயர்த்தார்."}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Sir B.N. Rau collected constitutional materials from 60 countries, consulted foreign legal experts, and prepared the primary Draft Constitution (containing 243 Articles and 13 Schedules) in October 1947, which was then scrutinized and revised by Dr. Ambedkar's Drafting Committee.",
            "ta": "சர் பி.என். ராவ் 60 நாடுகளின் அரசியலமைப்பு ஆதாரங்களைச் சேகரித்து, வெளிநாட்டு சட்ட நிபுணர்களைக் கலந்தாலோசித்து, அக்டோபர் 1947 இல் முதன்மை வரைவு அரசியலமைப்பைத் (243 சரத்துகள் & 13 அட்டவணைகள்) தயாரித்தார். இது பின்னர் அம்பேத்கரின் வரைவுக் குழுவால் கூர்ந்தாய்வு செய்யப்பட்டு திருத்தப்பட்டது."
        },
        "why_not_others": {
            "A": {"en": "Correct. B.N. Rau drafted the initial baseline draft of the Constitution.", "ta": "சரி. பி.என். ராவ் அரசியலமைப்பின் ஆரம்ப அடிப்படை வரைவை வரைந்தார்."},
            "B": {"en": "Incorrect. Dr. Rajendra Prasad chaired Steering Committee.", "ta": "தவறு. டாக்டர் ராஜேந்திர பிரசாத் வழிகாட்டும் குழுவின் தலைவராக இருந்தார்."},
            "C": {"en": "Incorrect. Rau was a distinguished judge and legal adviser, not Finance Minister.", "ta": "தவறு. ராவ் ஒரு சிறந்த நீதிபதி மற்றும் சட்ட ஆலோசகர், நிதி அமைச்சர் அல்ல."},
            "D": {"en": "Incorrect. Rau was legal adviser; translation committees handled regional translations later.", "ta": "தவறு. ராவ் சட்ட ஆலோசகர்; மொழிபெயர்ப்புக் குழுக்கள் பின்னர் பிராந்திய மொழிபெயர்ப்புகளைக் கையாண்டன."}
        },
        "tnpsc_tip": {
            "en": "Dr. B.R. Ambedkar paid tribute to Sir B.N. Rau in the Assembly, stating that the credit for preparing the raw draft belonged to Rau.",
            "ta": "மூல வரைவைத் தயாரித்ததற்கான பெருமை பி.என். ராவையே சாரும் என்று கூறி டாக்டர் பி.ஆர். அம்பேத்கர் அவையில் அவருக்கு அஞ்சலி செலுத்தினார்."
        },
        "revision_fact": {
            "en": "Sir B.N. Rau later became a Judge of the International Court of Justice (ICJ) at The Hague.",
            "ta": "சர் பி.என். ராவ் பின்னர் தி ஹேக் நகரில் உள்ள சர்வதேச நீதிமன்றத்தின் (ICJ) நீதிபதியானார்."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Understand",
        "estimated_time_sec": 55,
        "pyq_similarity": "High",
        "tags": ["Sir B.N. Rau", "Constitutional Adviser", "Initial Draft"]
    },
    # Q11
    {
        "id": "MIC_M_011",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "Committee-Based",
        "question": {
            "en": "Why was the 7-member Drafting Committee set up on August 29, 1947, considered the most crucial of all Assembly committees?",
            "ta": "ஆகஸ்ட் 29, 1947 அன்று அமைக்கப்பட்ட 7 பேர் கொண்ட வரைவுக் குழு, அவைக் குழுக்கள் அனைத்திலும் மிகவும் முக்கியமானதாக ஏன் கருதப்பட்டது?"
        },
        "options": [
            {"id": "A", "en": "It was tasked with scrutinizing the initial draft prepared by B.N. Rau and giving concrete legal shape to the new Constitution for parliamentary consideration.", "ta": "பி.என். ராவ் தயாரித்த ஆரம்ப வரைவை கூர்ந்தாய்வு செய்து, நாடாளுமன்றப் பரிசீலனைக்காக புதிய அரசியலமைப்பிற்கு உறுதியான சட்ட வடிவத்தை வழங்கும் பணி அதற்கு அளிக்கப்பட்டிருந்தது."},
            {"id": "B", "en": "It had exclusive authority to declare war, ratify treaties, and manage international boundary demarcations.", "ta": "போர் அறிவிக்கவும், ஒப்பந்தங்களை உறுதிப்படுத்தவும், சர்வதேச எல்லைக் குறியீடுகளை நிர்வகிக்கவும் அதற்கு பிரத்யேக அதிகாரம் இருந்தது."},
            {"id": "C", "en": "It was the only committee that contained elected representatives from all 565 Princely States.", "ta": "அனைத்து 565 சுதேச அரசுகளிலிருந்தும் தேர்ந்தெடுக்கப்பட்ட பிரதிநிதிகளைக் கொண்டிருந்த ஒரே குழு இதுவே ஆகும்."},
            {"id": "D", "en": "It was appointed directly by the United Nations to oversee the democratic transition in South Asia.", "ta": "தெற்காசியாவில் ஜனநாயக மாற்றத்தை மேற்பார்வையிட ஐக்கிய நாடுகள் சபையால் இது நேரடியாக நியமிக்கப்பட்டது."}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "The Drafting Committee chaired by Dr. B.R. Ambedkar was entrusted with synthesizing committee reports, examining public suggestions, clause-by-clause drafting, and preparing the final text of the Constitution.",
            "ta": "டாக்டர் பி.ஆர். அம்பேத்கர் தலைமையிலான வரைவுக் குழுவிடம் குழு அறிக்கைகளைத் தொகுத்து, பொதுப் பரிந்துரைகளை ஆராய்ந்து, சரத்து வாரியாக வரைவு செய்து, அரசியலமைப்பின் இறுதி உரையைத் தயாரிக்கும் பணி ஒப்படைக்கப்பட்டது."
        },
        "why_not_others": {
            "A": {"en": "Correct. Drafting Committee gave statutory legal shape to constitutional proposals.", "ta": "சரி. வரைவுக் குழு அரசியலமைப்பு முன்மொழிவுகளுக்கு சட்ட வடிவம் கொடுத்தது."},
            "B": {"en": "Incorrect. Foreign affairs and war powers belonged to Cabinet/Provisional Govt, not Drafting Committee.", "ta": "தவறு. வெளியுறவு மற்றும் போர் அதிகாரங்கள் அமைச்சரவைக்கு உரியவை, வரைவுக்குழுவிற்கு அல்ல."},
            "C": {"en": "Incorrect. Drafting Committee had only 7 members.", "ta": "தவறு. வரைவுக் குழுவில் 7 உறுப்பினர்கள் மட்டுமே இருந்தனர்."},
            "D": {"en": "Incorrect. UN had no involvement in appointing Assembly committees.", "ta": "தவறு. அவைக் குழுக்களை நியமிப்பதில் ஐநாவுக்கு எந்தப்ங்கும் இல்லை."}
        },
        "tnpsc_tip": {
            "en": "Drafting Committee sat for 141 days and submitted its final draft on November 4, 1948.",
            "ta": "வரைவுக் குழு 141 நாட்கள் அமர்ந்து தனது இறுதி வரைவை நவம்பர் 4, 1948 இல் சமர்ப்பித்தது."
        },
        "revision_fact": {
            "en": "Dr. Ambedkar introduced the final draft of the Constitution in the Assembly on November 4, 1948 (First Reading).",
            "ta": "டாக்டர் அம்பேத்கர் நவம்பர் 4, 1948 அன்று அவையில் அரசியலமைப்பின் இறுதி வரைவை அறிமுகப்படுத்தினார் (முதல் வாசிப்பு)."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Understand",
        "estimated_time_sec": 55,
        "pyq_similarity": "High",
        "tags": ["Drafting Committee Purpose", "Dr. B.R. Ambedkar", "Aug 29 1947"]
    },
    # Q12
    {
        "id": "MIC_M_012",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "Process-Based",
        "question": {
            "en": "Why was the First Draft of the Constitution published in February 1948, and what process followed its publication?",
            "ta": "அரசியலமைப்பின் முதல் வரைவு பிப்ரவரி 1948 இல் ஏன் வெளியிடப்பட்டது, மேலும் அது வெளியானதைத் தொடர்ந்து என்ன செயல்முறை பின்பற்றப்பட்டது?"
        },
        "options": [
            {"id": "A", "en": "It was published to give the citizens of India 8 months to discuss the draft, suggest amendments, and offer public feedback before formal Assembly debates.", "ta": "முறைப்படியான அவை விவாதங்களுக்கு முன் வரைவைப் பற்றி விவாதிக்கவும், திருத்தங்களைப் பரிந்துரைக்கவும், பொதுக் கருத்துக்களை வழங்கவும் இந்தியக் குடிமக்களுக்கு 8 மாத அவகாசம் வழங்க வெளியிடப்பட்டது."},
            {"id": "B", "en": "It was published to conduct a referendum where every citizen had to vote YES or NO on the entire text.", "ta": "ஒவ்வொரு குடிமகனும் முழு உரையிலும் ஆம் அல்லது இல்லை என்று வாக்களிக்க வேண்டிய பொதுவாக்கெடுப்பை நடத்த இது வெளியிடப்பட்டது."},
            {"id": "C", "en": "It was published to allow British legal scholars to veto clauses that infringed on imperial trade treaties.", "ta": "ஏகாதிபத்திய வர்த்தக ஒப்பந்தங்களை மீறும் சரத்துகளை பிரிட்டிஷ் சட்ட வல்லுநர்கள் வீட்டோ செய்ய அனுமதிக்க வெளியிடப்பட்டது."},
            {"id": "D", "en": "It was published as a temporary law to govern provinces until 1960 without parliamentary debate.", "ta": "நாடாளுமன்ற விவாதம் இன்றி 1960 வரை மாகாணங்களை ஆளுவதற்கான தற்காலிகச் சட்டமாக இது வெளியிடப்பட்டது."}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "The Drafting Committee published the First Draft in Feb 1948. Over 8 months, the Indian public, press, provincial assemblies, and courts submitted comments and criticism. Taking these into account, the Drafting Committee prepared a Second Draft published in October 1948.",
            "ta": "வரைவுக் குழு முதல் வரைவை பிப்ரவரி 1948 இல் வெளியிட்டது. 8 மாதங்களுக்கும் மேலாக, இந்தியப் பொதுமக்கள், பத்திரிகைகள், மாகாணச் சபைகள் மற்றும் நீதிமன்றங்கள் கருத்துக்களையும் விமர்சனங்களையும் சமர்ப்பித்தன. இவற்றைக் கருத்தில் கொண்டு, வரைவுக் குழு அக்டோபர் 1948 இல் இரண்டாவது வரைவைத் தயாரித்து வெளியிட்டது."
        },
        "why_not_others": {
            "A": {"en": "Correct. 8 months public consultation period was provided for feedback and amendments.", "ta": "சரி. கருத்துக்கள் மற்றும் திருத்தங்களுக்காக 8 மாத பொது மக்கள் கலந்தாய்வு காலம் வழங்கப்பட்டது."},
            "B": {"en": "Incorrect. No referendum was conducted; public feedback was reviewed by Assembly.", "ta": "தவறு. பொதுவாக்கெடுப்பு எதுவும் நடத்தப்படவில்லை; பொதுக் கருத்துக்கள் அவையால் பரிசீலிக்கப்பட்டன."},
            "C": {"en": "Incorrect. British scholars had no veto power over the draft.", "ta": "தவறு. வரைவின் மீது பிரிட்டிஷ் அறிஞர்களுக்கு எந்த வீட்டோ அதிகாரமும் இல்லை."},
            "D": {"en": "Incorrect. It was a draft for debate, not an interim governing law.", "ta": "தவறு. இது விவாதத்திற்கான வரைவு, இடைக்கால ஆளும் சட்டம் அல்ல."}
        },
        "tnpsc_tip": {
            "en": "Total amendments proposed during consideration: 7,635; Total amendments actually discussed in detail: 2,473.",
            "ta": "பரிசீலனையின் போது முன்மொழியப்பட்ட மொத்த திருத்தங்கள்: 7,635; விரிவாக விவாதிக்கப்பட்ட மொத்த திருத்தங்கள்: 2,473."
        },
        "revision_fact": {
            "en": "The Second Draft was published in October 1948 after incorporating public and expert feedback.",
            "ta": "பொதுமக்கள் மற்றும் நிபுணர்களின் கருத்துக்களைக் கொண்டு அக்டோபர் 1948 இல் இரண்டாவது வரைவு வெளியிடப்பட்டது."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Understand",
        "estimated_time_sec": 55,
        "pyq_similarity": "High",
        "tags": ["First Draft Feb 1948", "Public Consultation", "Second Draft Oct 1948"]
    },
    # Q13
    {
        "id": "MIC_M_013",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "Committee-Based",
        "question": {
            "en": "Why was the Advisory Committee on Fundamental Rights, Minorities and Tribal Areas divided into five sub-committees under Sardar Vallabhbhai Patel's leadership?",
            "ta": "சர்தார் வல்லபாய் படேலின் தலைமையிலான அடிப்படை உரிமைகள், சிறுபான்மையினர் மற்றும் பழங்குடியினர் ஆலோசனைக் குழு ஏன் ஐந்து துணைக் குழுக்களாகப் பிரிக்கப்பட்டது?"
        },
        "options": [
            {"id": "A", "en": "To enable specialized, in-depth investigation into distinct complex issues like civil liberties, minority safeguards, and regional tribal governance.", "ta": "குடிமைச் சுதந்திரங்கள், சிறுபான்மையினர் பாதுகாப்புகள் மற்றும் பிராந்திய பழங்குடியினர் நிர்வாகம் போன்ற தனித்துவமான சிக்கலான பிரச்சினைகளில் தனித்துவமான, ஆழமான விசாரணையைச் சாத்தியமாக்க."},
            {"id": "B", "en": "Because Sardar Patel refused to preside over meetings that included non-Congress delegates.", "ta": "ஏனெனில் காங்கிரஸ் அல்லாத பிரதிநிதிகள் கலந்துகொண்ட கூட்டங்களுக்கு தலைமை தாங்க சர்தார் படேல் மறுத்துவிட்டார்."},
            {"id": "C", "en": "To fulfill a mandatory clause in the 1935 Act that required separate sub-committees for every religious group.", "ta": "ஒவ்வொரு மதக் குழுவிற்கும் தனித் துணைக் குழுக்களைக் கோரும் 1935 ஆம் ஆண்டின் சட்டத்தின் கட்டாயச் சரத்தைப் பூர்த்தி செய்ய."},
            {"id": "D", "en": "Because the British Governor-General insisted on retaining personal oversight over tribal administration.", "ta": "ஏனெனில் பிரிட்டிஷ் கவர்னர்-ஜெனரல் பழங்குடியினர் நிர்வாகத்தின் மீது தனிப்பட்ட மேற்பார்வையைத் தக்க வைத்துக் கொள்ள வலியுறுத்தினார்."}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "The Advisory Committee was the largest committee (54 members). Patel subdivided it into 5 sub-committees (such as FR Sub-Committee under Kripalani, Minorities Sub-Committee under H.C. Mookerjee, North-East Tribal Sub-Committee under Bardoloi) to ensure expert handling of diverse socio-political protections.",
            "ta": "ஆலோசனைக் குழு மிகப்பெரிய குழுவாகும் (54 உறுப்பினர்கள்). பல்வேறு சமூக-அரசியல் பாதுகாப்புகளை நிபுணத்துவத்துடன் கையாளுவதை உறுதி செய்ய படேல் அதை 5 துணைக் குழுக்களாகப் பிரித்தார் (கிருபளானி தலைமையிலான அடிப்படை உரிமைகள் துணைக் குழு, எச்.சி. முகர்ஜி தலைமையிலான சிறுபான்மையினர் துணைக் குழு போன்றவை)."
        },
        "why_not_others": {
            "A": {"en": "Correct. Sub-committees allowed granular analysis of fundamental rights, minority protection, and tribal administration.", "ta": "சரி. துணைக் குழுக்கள் அடிப்படை உரிமைகள், சிறுபான்மையினர் பாதுகாப்பு, பழங்குடியினர் நிர்வாகத்தின் விரிவான ஆய்வுக்கு வழிவகுத்தன."},
            "B": {"en": "Incorrect. Patel worked closely with all non-Congress members including Ambedkar and Mookerjee.", "ta": "தவறு. அம்பேத்கர், முகர்ஜி உட்பட அனைத்து காங்கிரஸ் அல்லாத உறுப்பினர்களுடனும் படேல் நெருக்கமாகப் பணியாற்றினார்."},
            "C": {"en": "Incorrect. 1935 Act had no such requirement for Assembly sub-committees.", "ta": "தவறு. 1935 சட்டத்தில் அவைத் துணைக் குழுக்களுக்கான அத்தகைய தேவை எதுவுமில்லை."},
            "D": {"en": "Incorrect. Governor-General had no role in structuring Assembly committees.", "ta": "தவறு. அவைக் குழுக்களை அமைப்பதில் கவர்னர்-ஜெனரலுக்கு எந்தப்ங்கும் இல்லை."}
        },
        "tnpsc_tip": {
            "en": "Key Sub-Committees: 1. Fundamental Rights (J.B. Kripalani), 2. Minorities (H.C. Mookerjee), 3. NE Frontier Tribal (Gopinath Bardoloi), 4. Excluded Areas (A.V. Thakkar).",
            "ta": "முக்கிய துணைக் குழுக்கள்: 1. அடிப்படை உரிமைகள் (ஜே.பி. கிருபளானி), 2. சிறுபான்மையினர் (எச்.சி. முகர்ஜி), 3. வடகிழக்கு பழங்குடியினர் (கோபிநாத் பர்தோலோய்), 4. விலக்கப்பட்ட பகுதிகள் (ஏ.வி. தாக்கர்)."
        },
        "revision_fact": {
            "en": "The recommendations of Bardoloi and Thakkar sub-committees formed the basis for Fifth and Sixth Schedules of the Constitution.",
            "ta": "பர்தோலோய் மற்றும் தாக்கர் துணைக் குழுக்களின் பரிந்துரைகளே அரசியலமைப்பின் 5 மற்றும் 6 வது அட்டவணைகளுக்கு அடிப்படையாக அமைந்தன."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Understand",
        "estimated_time_sec": 60,
        "pyq_similarity": "High",
        "tags": ["Advisory Committee Sub-committees", "Sardar Patel", "Specialized Study"]
    },
    # Q14
    {
        "id": "MIC_M_014",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "Constitutional Understanding",
        "question": {
            "en": "What was the significance of the compromise reached in the Constituent Assembly regarding Justiciable vs. Non-Justiciable Rights?",
            "ta": "நீதிமன்றத்தால் செயலாக்கப்படக்கூடிய உரிமைகள் மற்றும் செயலாக்கப்பட முடியாத உரிமைகள் குறித்து அரசியலமைப்பு நிர்ணய அவையில் எட்டப்பட்ட சமரசத்தின் முக்கியத்துவம் யாது?"
        },
        "options": [
            {"id": "A", "en": "It bifurcated rights into legally enforceable Fundamental Rights (Part III) and non-enforceable Directive Principles (Part IV) based on B.N. Rau's recommendation to balance individual freedom with economic capability.", "ta": "தனிநபர் சுதந்திரத்தை பொருளாதாரத் திறனுடன் சமநிலைப்படுத்த பி.என். ராவின் பரிந்துரையின் அடிப்படையில் உரிமைகளை சட்டப்பூர்வமாக அமல்படுத்தக்கூடிய அடிப்படை உரிமைகள் (பகுதி III) மற்றும் அமல்படுத்த முடியாத அரசு நெறிமுறைகள் (பகுதி IV) என இரண்டாகப் பிரித்தது."},
            {"id": "B", "en": "It declared that all economic and social rights would be enforceable immediately through High Courts, while political rights were deferred.", "ta": "அனைத்து பொருளாதார மற்றும் சமூக உரிமைகளும் உயர் நீதிமன்றங்கள் மூலம் உடனடியாக அமல்படுத்தப்படும் என்றும், அரசியல் உரிமைகள் தள்ளிவைக்கப்படும் என்றும் அறிவித்தது."},
            {"id": "C", "en": "It abolished the judicial review powers of the Supreme Court over Fundamental Rights.", "ta": "அடிப்படை உரிமைகள் மீதான உச்ச நீதிமன்றத்தின் நீதித்துறை மறுஆய்வு அதிகாரங்களை இது ஒழித்தது."},
            {"id": "D", "en": "It restricted justiciable rights strictly to British residents living in cantonments.", "ta": "நீதிமன்றத்தால் செயலாக்கப்படக்கூடிய உரிமைகளை ராணுவக் குடியிருப்புப் பகுதிகளில் வாழும் பிரிட்டிஷ் குடியிருப்பாளர்களுக்கு மட்டுமே தீவிரமாகக் கட்டுப்படுத்தியது."}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Sir B.N. Rau suggested classifying rights into two categories: justiciable (enforceable in courts) and non-justiciable (guidelines for state policy). The Assembly accepted this to ensure civil liberties (Part III) were protected immediately, while socio-economic goals (Part IV) were realized progressively as resources grew.",
            "ta": "சர் பி.என். ராவ் உரிமைகளை இரண்டு வகைகளாகப் பிரிக்கப் பரிந்துரைத்தார்: நீதிமன்றத்தால் செயலாக்கப்படக்கூடியவை மற்றும் செயலாக்கப்பட முடியாதவை. குடிமைச் சுதந்திரங்கள் (பகுதி III) உடனடியாகப் பாதுகாக்கப்படுவதையும், சமூக-பொருளாதார இலக்குகள் (பகுதி IV) வளங்கள் வளர வளரப் படிப்படியாக நிறைவேற்றப்படுவதையும் உறுதி செய்ய அவை இதை ஏற்றுக்கொண்டது."
        },
        "why_not_others": {
            "A": {"en": "Correct. Distinction between Part III (Justiciable) and Part IV (Non-justiciable) solved financial resource constraints.", "ta": "சரி. பகுதி III (நீதிமன்றத்தால் செயலாக்கப்படக்கூடியவை) மற்றும் பகுதி IV (செயலாக்கப்பட முடியாதவை) இடையேயான வேறுபாடு நிதி ஆதாரக் கட்டுப்பாடுகளைத் தீர்த்தது."},
            "B": {"en": "Incorrect. Political and civil rights were made enforceable; socio-economic rights were non-justiciable.", "ta": "தவறு. அரசியல் மற்றும் குடிமை உரிமைகள் அமல்படுத்தக்கூடியதாக மாற்றப்பட்டன; சமூக-பொருளாதார உரிமைகள் செயலாக்கப்பட முடியாதவையாக இருந்தன."},
            "C": {"en": "Incorrect. Judicial review over Fundamental Rights under Article 32 was created as the 'heart and soul' of the Constitution.", "ta": "தவறு. சரத்து 32 இன் கீழ் அடிப்படை உரிமைகள் மீதான நீதித்துறை மறுஆய்வு அரசியலமைப்பின் 'இதயம் மற்றும் ஆன்மா'வாக உருவாக்கப்பட்டது."},
            "D": {"en": "Incorrect. Rights applied to all citizens across India.", "ta": "தவறு. உரிமைகள் இந்தியா முழுவதிலும் உள்ள அனைத்துக் குடிமக்களுக்கும் பொருந்தும்."}
        },
        "tnpsc_tip": {
            "en": "Dr. Ambedkar called Article 32 (Right to Constitutional Remedies) 'the heart and soul of the Constitution'.",
            "ta": "டாக்டர் அம்பேத்கர் சரத்து 32 ஐ (அரசியலமைப்புப் பரிகார உரிமை) 'அரசியலமைப்பின் இதயம் மற்றும் ஆன்மா' என்று அழைத்தார்."
        },
        "revision_fact": {
            "en": "The distinction between Part III and Part IV was adopted from the Irish Constitution model.",
            "ta": "பகுதி III மற்றும் பகுதி IV இடையேயான வேறுபாடு அயர்லாந்து அரசியலமைப்பு மாதிரியிலிருந்து பெறப்பட்டது."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Understand",
        "estimated_time_sec": 60,
        "pyq_similarity": "High",
        "tags": ["Justiciable vs Non-Justiciable", "B.N. Rau Proposal", "Part III & Part IV"]
    },
    # Q15
    {
        "id": "MIC_M_015",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "Conceptual",
        "question": {
            "en": "Why did the Assembly choose to adopt the phrase 'Union of States' rather than 'Federation of States' in Article 1 of the Draft Constitution?",
            "ta": "வரைவு அரசியலமைப்பின் சரத்து 1 இல் 'மாநிலங்களின் கூட்டமைப்பு' (Federation of States) என்பதற்குப் பதிலாக 'மாநிலங்களின் ஒன்றியம்' (Union of States) என்ற சொற்றொடரை ஏற்றுக்கொள்ள அவை ஏன் தேர்வு செய்தது?"
        },
        "options": [
            {"id": "A", "en": "To emphasize that the Indian federation was not the result of an agreement among sovereign states, and no state had the right to secede from the Union.", "ta": "இந்தியக் கூட்டமைப்பு இறையாண்மை கொண்ட மாநிலங்களுக்கு இடையேயான ஒப்பந்தத்தின் விளைவு அல்ல என்பதையும், எந்த மாநிலத்திற்கும் ஒன்றியத்திலிருந்து பிரிந்து செல்லும் உரிமை இல்லை என்பதையும் வலியுறுத்த."},
            {"id": "B", "en": "Because the British Parliament explicitly forbade the use of the word 'Federation' in Asian constitutions.", "ta": "ஏனெனில் பிரிட்டிஷ் நாடாளுமன்றம் ஆசிய அரசியலமைப்புகளில் 'கூட்டமைப்பு' என்ற வார்த்தையைப் பயன்படுத்துவதைத் தெளிவாகத் தடுத்திருந்தது."},
            {"id": "C", "en": "To allow the Union Government to unilaterally convert all states into union territories without constitutional amendment.", "ta": "மத்திய அரசு அரசியலமைப்புத் திருத்தமின்றி அனைத்து மாநிலங்களையும் தன்னிச்சையாக யூனியன் பிரதேசங்களாக மாற்ற அனுமதிப்பதற்காக."},
            {"id": "D", "en": "Because 'Federation' was considered a strictly monarchy-based term in European diplomacy.", "ta": "ஏனெனில் 'கூட்டமைப்பு' என்பது ஐரோப்பிய இராஜதந்திரத்தில் முற்றிலும் முடியாட்சி சார்ந்த வார்த்தையாகக் கருதப்பட்டது."}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Dr. Ambedkar explained in the Assembly that 'Union of States' was preferred because: 1) The Indian federation is not the result of an agreement by states (unlike the US), and 2) States have no right to secede; the federation is an indestructible Union.",
            "ta": "டாக்டர் அம்பேத்கர் அவையில் விளக்கினார்: 'மாநிலங்களின் ஒன்றியம்' விரும்பப்பட்டதற்குக் காரணம்: 1) இந்தியக் கூட்டமைப்பு மாநிலங்களின் ஒப்பந்தத்தின் விளைவு அல்ல (அமெரிக்கா போல் அல்ல), மற்றும் 2) மாநிலங்களுக்குப் பிரியும் உரிமை இல்லை; ஒன்றியம் ஒரு அழிக்க முடியாத அமைப்பாகும்."
        },
        "why_not_others": {
            "A": {"en": "Correct. Indestructible Union of destructible states rationale explained by Dr. Ambedkar.", "ta": "சரி. அழிக்க முடியாத ஒன்றியம் என்ற அம்பேத்கரின் விளக்கம்."},
            "B": {"en": "Incorrect. British Parliament had used 'Federation of India' in the 1935 Act itself.", "ta": "தவறு. 1935 சட்டத்திலேயே பிரிட்டிஷ் நாடாளுமன்றம் 'இந்தியக் கூட்டமைப்பு' என்று பயன்படுத்தியிருந்தது."},
            "C": {"en": "Incorrect. Article 1 does not grant arbitrary powers to dissolve state autonomy.", "ta": "தவறு. சரத்து 1 மாநிலத் தன்னாட்சியைக் கலைக்க தன்னிச்சையான அதிகாரங்களை வழங்கவில்லை."},
            "D": {"en": "Incorrect. 'Federation' is a democratic federal term, not a monarchical term.", "ta": "தவறு. 'கூட்டமைப்பு' என்பது ஒரு ஜனநாயக கூட்டாட்சிச் சொல், முடியாட்சிச் சொல் அல்ல."}
        },
        "tnpsc_tip": {
            "en": "Ambedkar's famous quote: 'The country is one integral whole, its people a single people living under a single imperium derived from a single source.'",
            "ta": "அம்பேத்கரின் புகழ்பெற்ற கூற்று: 'நாடு ஒரு ஒருங்கிணைந்த முழுமை, அதன் மக்கள் ஒரே மூலத்திலிருந்து பெறப்பட்ட ஒரே பேரரசின் கீழ் வாழும் ஒற்றை மக்கள்.'."
        },
        "revision_fact": {
            "en": "Article 1 describes India, that is Bharat, as a 'Union of States'.",
            "ta": "சரத்து 1 இந்தியாவை, அதாவது பாரதத்தை, 'மாநிலங்களின் ஒன்றியம்' என்று விவரிக்கிறது."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Understand",
        "estimated_time_sec": 55,
        "pyq_similarity": "High",
        "tags": ["Union of States", "Article 1 Debate", "No Right to Secede"]
    },
    # Q16
    {
        "id": "MIC_M_016",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "Constitutional Understanding",
        "question": {
            "en": "Why did the Constituent Assembly adopt a Parliamentary form of government over an American Presidential Executive system for independent India?",
            "ta": "சுதந்திர இந்தியாவிற்கு அமெரிக்க அதிபர் ஆட்சிமுறை நிர்வாகத்திற்குப் பதிலாக நாடாளுமன்ற ஜனநாயக ஆட்சிமுறையை அரசியலமைப்பு நிர்ணய அவை ஏன் ஏற்றுக்கொண்டது?"
        },
        "options": [
            {"id": "A", "en": "The framers prioritized responsibility over stability and were already familiar with the working of cabinet government under British executive reforms.", "ta": "உருவாக்குநர்கள் ஸ்திரத்தன்மையை விடப் பொறுப்புக்கூறலுக்கு முன்னுரிமை அளித்தனர் மற்றும் பிரிட்டிஷ் நிர்வாகச் சீர்திருத்தங்களின் கீழ் அமைச்சரவை அரசாங்கத்தின் செயல்பாட்டை ஏற்கனவே அறிந்திருந்தனர்."},
            {"id": "B", "en": "The Presidential system was rejected because the US Constitution prohibited foreign nations from adopting its executive structure.", "ta": "அமெரிக்க அரசியலமைப்பு வெளிநாடுகள் அதன் நிர்வாகக் கட்டமைப்பை ஏற்றுக்கொள்வதைத் தடுத்ததால் அதிபர் முறை நிராகரிக்கப்பட்டது."},
            {"id": "C", "en": "The Cabinet Mission Plan made parliamentary governance a legally binding condition for transferring independence.", "ta": "கேபினட் தூதுக்குழு திட்டம் நாடாளுமன்ற ஆட்சியை சுதந்திரத்தை மாற்றுவதற்கான சட்டப்பூர்வக் கட்டாய நிபந்தனையாக ஆக்கியது."},
            {"id": "D", "en": "The Supreme Court advised that a Presidential system would violate the basic structure of ancient Indian village republics.", "ta": "அதிபர் முறை பண்டைய இந்திய கிராமக் குடியரசுகளின் அடிப்படைமைப்பை மீறும் என்று உச்ச நீதிமன்றம் அறிவுறுத்தியது."}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Dr. Ambedkar pointed out that a democratic executive must satisfy two conditions: stability and responsibility. While the American system offers more stability but less responsibility, the British Parliamentary system offers daily assessment of responsibility through questions, resolutions, and no-confidence motions, which suited India's diverse needs.",
            "ta": "ஒரு ஜனநாயக நிர்வாகம் இரண்டு நிபந்தனைகளை பூர்த்தி செய்ய வேண்டும் என்று அம்பேத்கர் சுட்டிக்காட்டினார்: ஸ்திரத்தன்மை மற்றும் பொறுப்புக்கூறல். அமெரிக்க முறை அதிக ஸ்திரத்தன்மையையும் குறைந்த பொறுப்புக்கூறலையும் வழங்கும் அதே வேளையில், பிரிட்டிஷ் நாடாளுமன்ற முறை கேள்விகள், தீர்மானங்கள் மற்றும் நம்பிக்கையில்லாத் தீர்மானங்கள் மூலம் தினசரி பொறுப்புக்கூறல் மதிப்பீட்டை வழங்குகிறது, இது இந்தியாவின் பல்வேறு தேவைகளுக்குப் பொருத்தமாக இருந்தது."
        },
        "why_not_others": {
            "A": {"en": "Correct. Preference for daily assessment of executive responsibility and long familiarity with parliamentary institutions.", "ta": "சரி. நிர்வாகப் பொறுப்புக்கூறலின் தினசரி மதிப்பீட்டிற்கான முன்னுரிமை மற்றும் நாடாளுமன்ற நிறுவனங்களின் நீண்ட காலப் பரிச்சயம்."},
            "B": {"en": "Incorrect. US Constitution has no foreign prohibition clause.", "ta": "தவறு. அமெரிக்க அரசியலமைப்பில் வெளிநாட்டுத் தடைச் சரத்து எதுவும் இல்லை."},
            "C": {"en": "Incorrect. Cabinet Mission left the form of executive entirely to the Assembly's sovereign choice.", "ta": "தவறு. கேபினட் தூதுக்குழு நிர்வாகத்தின் வடிவத்தை அவையின் இறையாண்மைத் தேர்வுக்கு முழுமையாக விட்டது."},
            "D": {"en": "Incorrect. Supreme Court did not exist yet and basic structure doctrine was developed in 1973.", "ta": "தவறு. உச்ச நீதிமன்றம் அப்போது உருவாகவில்லை மற்றும் அடிப்படை அமைப்பு கோட்பாடு 1973 இல் உருவானது."}
        },
        "tnpsc_tip": {
            "en": "K.M. Munshi observed: 'For the last thirty or forty years, some kind of responsibility has been introduced in governance; our constitutional traditions have become parliamentary.'",
            "ta": "கே.எம். முன்ஷி குறிப்பிட்டார்: 'கடந்த முப்பது அல்லது நாற்பது ஆண்டுகளாக, நிர்வாகத்தில் சில வகையான பொறுப்புக்கூறல் அறிமுகப்படுத்தப்பட்டுள்ளது; நமது அரசியலமைப்பு மரபுகள் நாடாளுமன்ற மரபுகளாக மாறியுள்ளன.'."
        },
        "revision_fact": {
            "en": "Articles 74-75 handle parliamentary system at the Center, and Articles 163-164 in the States.",
            "ta": "சரத்துகள் 74-75 மத்தியில் நாடாளுமன்ற முறையையும், சரத்துகள் 163-164 மாநிலங்களிலும் கையாள்கின்றன."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Understand",
        "estimated_time_sec": 60,
        "pyq_similarity": "High",
        "tags": ["Parliamentary System Rationale", "Responsibility vs Stability", "Executive Form"]
    },
    # Q17
    {
        "id": "MIC_M_017",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "Conceptual",
        "question": {
            "en": "Why was the proposal to incorporate Panchayati Raj as the primary unit of administration in the main body of the Constitution rejected during the debates, and placed instead under Article 40 of Directive Principles?",
            "ta": "அரசியலமைப்பின் முதன்மைப் பகுதியில் பஞ்சாயத்து ராஜை நிர்வாகத்தின் முதன்மை அலகாக இணைக்கும் முன்மொழிவு விவாதங்களின் போது ஏன் நிராகரிக்கப்பட்டு, அதற்குப் பதிலாக பகுதி IV இன் சரத்து 40 இன் கீழ் வைக்கப்பட்டது?"
        },
        "options": [
            {"id": "A", "en": "Dr. B.R. Ambedkar strongly criticized traditional Indian villages as 'dens of localism and ignorance' dominated by caste hierarchies, preferring individual-centric governance over village-centric governance.", "ta": "டாக்டர் பி.ஆர். அம்பேத்கர் பாரம்பரிய இந்தியக் கிராமங்களை சாதி படிநிலைகள் ஆதிக்கம் செலுத்தும் 'உள்ளூர்வாதம் மற்றும் அறியாமையின் குகைகள்' என்று கடுமையாக விமர்சித்தார், கிராம மைய நிர்வாகத்தை விட தனிநபர் மைய நிர்வாகத்தை விரும்பினார்."},
            {"id": "B", "en": "The British Crown declared that local councils were illegal under international law.", "ta": "சர்வதேச சட்டத்தின் கீழ் உள்ளாட்சி மன்றங்கள் சட்டவிரோதமானவை என்று பிரிட்டிஷ் அரசு அறிவித்தது."},
            {"id": "C", "en": "Mahatma Gandhi explicitly wrote to the Assembly requesting that Panchayats be kept out of constitutional law.", "ta": "பஞ்சாயத்துகளை அரசியலமைப்புச் சட்டத்திலிருந்து விலக்கி வைக்குமாறு மகாத்மா காந்தி அவைக்கு அதிகாரப்பூர்வமாக கடிதம் எழுதினார்."},
            {"id": "D", "en": "The Drafting Committee found no historic precedent for local administration anywhere in Asia.", "ta": "ஆசியாவில் எங்கும் உள்ளாட்சி நிர்வாகத்திற்கான வரலாற்று முன்மாதிரியை வரைவுக் குழு கண்டுபிடிக்கவில்லை."}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "While Gandhian members wanted a village-based constitution, Dr. Ambedkar argued that Indian villages were dominated by upper-caste oppression, communalism, and backwardness. Making the individual citizen (not the village) the fundamental unit ensured equal rights and social mobility for Dalits and marginalized groups.",
            "ta": "காந்திய உறுப்பினர்கள் கிராமத்தை அடிப்படையாகக் கொண்ட அரசியலமைப்பை விரும்பிய போதிலும், இந்தியக் கிராமங்களில் மேல்சாதி ஒடுக்குமுறை, வகுப்புவாதம் மற்றும் பிற்போக்குத்தனம் ஆதிக்கம் செலுத்துவதாக டாக்டர் அம்பேத்கர் வாதிட்டார். கிராமத்திற்குப் பதிலாக தனிநபர் குடிமகனை அடிப்படை அலகாக ஆக்கியது ஒடுக்கப்பட்ட பிரிவினருக்கு சம உரிமையையும் சமூக முன்னேற்றத்தையும் உறுதி செய்தது."
        },
        "why_not_others": {
            "A": {"en": "Correct. Ambedkar's strong opposition to village unit due to caste oppression led to compromise under DPSP Article 40.", "ta": "சரி. சாதி ஒடுக்குமுறை காரணமாக கிராம அலகிற்கு அம்பேத்கரின் பலமான எதிர்ப்பு DPSP சரத்து 40 இன் கீழ் சமரசத்திற்கு வழிவகுத்தது."},
            "B": {"en": "Incorrect. British Crown had no say in Assembly debates on local government.", "ta": "தவறு. உள்ளாட்சி குறித்த அவை விவாதங்களில் பிரிட்டிஷ் அரசிற்கு எந்தப்ங்கும் இல்லை."},
            "C": {"en": "Incorrect. Gandhi was a passionate champion of Panchayati Raj (Gram Swaraj).", "ta": "தவறு. காந்தி கிராம பஞ்சாயத்து ராஜின் (கிராம சுயராஜ்யம்) தீவிர ஆதரவாளராக இருந்தார்."},
            "D": {"en": "Incorrect. Chola village assemblies (Kudavolai) and ancient sabhas were well-known precedents.", "ta": "தவறு. சோழர் கிராம சபைகள் (குடவோலை) மற்றும் பண்டைய சபைகள் நன்கு அறியப்பட்ட முன்மாதிரிகள்."}
        },
        "tnpsc_tip": {
            "en": "K. Santhanam moved the amendment to include village panchayats in Directive Principles, which became Article 40.",
            "ta": "கிராம பஞ்சாயத்துகளை அரசு நெறிமுறைகளில் சேர்க்க கே. சந்தானம் திருத்தத்தைக் கொண்டு வந்தார், அதுவே சரத்து 40 ஆக மாறியது."
        },
        "revision_fact": {
            "en": "Panchayati Raj finally gained constitutional status in 1992 through the 73rd Constitutional Amendment Act.",
            "ta": "பஞ்சாயத்து ராஜ் இறுதியாக 1992 இல் 73 வது அரசியலமைப்புத் திருத்தச் சட்டத்தின் மூலம் அரசியலமைப்பு அந்தஸ்தைப் பெற்றது."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Understand",
        "estimated_time_sec": 60,
        "pyq_similarity": "High",
        "tags": ["Panchayati Raj Debate", "Dr. Ambedkar View", "Article 40 DPSP"]
    },
    # Q18
    {
        "id": "MIC_M_018",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "Process-Based",
        "question": {
            "en": "What was the significance of the debate surrounding the Emergency Provisions (Articles 352-360) in the Constituent Assembly?",
            "ta": "அரசியலமைப்பு நிர்ணய அவையில் அவசரநிலைப் பிரகடன விதிகள் (சரத்துகள் 352-360) சுற்றியுள்ள விவாதத்தின் முக்கியத்துவம் யாது?"
        },
        "options": [
            {"id": "A", "en": "Critics like H.V. Kamath and K.T. Shah feared the provisions could transform the federal republic into an autocratic dictatorship, but Ambedkar defended them as 'necessary safety valves' for national security.", "ta": "எச்.வி. காமத் மற்றும் கே.டி. ஷா போன்ற விமர்சகர்கள் இவ்விதிகள் கூட்டாட்சிக் குடியரசை தன்னிச்சையான சர்வாதிகாரமாக மாற்றக்கூடும் என்று அஞ்சினர், ஆனால் அம்பேத்கர் தேசிய பாதுகாப்பிற்கான 'அவசியமான பாதுகாப்பு நெறிமுறைகள்' என அவற்றை நியாயப்படுத்தினார்."},
            {"id": "B", "en": "The provisions were adopted unanimously in a single day without any opposition or parliamentary discussion.", "ta": "எந்தவொரு எதிர்ப்பும் அல்லது நாடாளுமன்ற விவாதமும் இன்றி ஒரே நாளில் இவ்விதிகள் ஒருமனதாக ஏற்றுக்கொள்ளப்பட்டன."},
            {"id": "C", "en": "Emergency powers were restricted strictly to municipal corporations during natural disasters.", "ta": "அவசரநிலை அதிகாரங்கள் இயற்கை சீற்றங்களின் போது மாநகராட்சிகளுக்கு மட்டுமே தீவிரமாகக் கட்டுப்படுத்தப்பட்டன."},
            {"id": "D", "en": "The provisions mandated that the British Governor-General must approve any emergency declaration.", "ta": "எந்தவொரு அவசரநிலைப் பிரகடனத்தையும் பிரிட்டிஷ் கவர்னர்-ஜெனரல் அங்கீகரிக்க வேண்டும் என்று இவ்விதிகள் கட்டாயப்படுத்தின."}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Emergency Provisions sparked intense debates. Members expressed fear of totalitarian abuse. Dr. Ambedkar famously remarked that he hoped these articles 'would remain a dead letter' and would be invoked only as a last resort to safeguard the existence of the Union.",
            "ta": "அவசரநிலை விதிகள் தீவிர விவாதங்களைத் தூண்டின. உறுப்பினர்கள் சர்வாதிகார துஷ்பிரயோகம் குறித்த பயத்தை வெளிப்படுத்தினர். இந்த சரத்துகள் 'பயன்படுத்தப்படாத எழுத்தாகவே இருக்கும்' என்றும், ஒன்றியத்தின் இருப்பைப் பாதுகாக்க கடைசி முயற்சியாக மட்டுமே பயன்படுத்தப்படும் என்றும் அம்பேத்கர் புகழ்பெற்ற முறையில் குறிப்பிட்டார்."
        },
        "why_not_others": {
            "A": {"en": "Correct. Debate highlighted tension between civil liberty vs national security; Ambedkar called it a 'dead letter' hope.", "ta": "சரி. விவாதம் குடிமை சுதந்திரத்திற்கும் தேசிய பாதுகாப்பிற்கும் இடையிலான பதற்றத்தை எடுத்துக்காட்டியது; அம்பேத்கர் அதை ஒரு 'பயன்படாத எழுத்து' என்று நம்பினார்."},
            "B": {"en": "Incorrect. Emergency provisions were among the most hotly debated subjects in the Assembly.", "ta": "தவறு. அவசரநிலை விதிகள் அவையில் மிகவும் சூடாக விவாதிக்கப்பட்ட பாடங்களில் ஒன்றாகும்."},
            "C": {"en": "Incorrect. Emergency powers dealt with national sovereignty, financial breakdown, and constitutional failure in states.", "ta": "தவறு. அவசரநிலை அதிகாரங்கள் தேசிய இறையாண்மை, நிதிச் சீர்குலைவு மற்றும் மாநிலங்களில் அரசியலமைப்பு முடக்கம் ஆகியவற்றைக் கையாண்டன."},
            "D": {"en": "Incorrect. Emergency powers were vested in the elected President acting on Cabinet advice.", "ta": "தவறு. அவசரநிலை அதிகாரங்கள் அமைச்சரவை ஆலோசனையின்படி செயல்படும் தேர்ந்தெடுக்கப்பட்ட குடியரசுத் தலைவரிடம் வழங்கப்பட்டன."}
        },
        "tnpsc_tip": {
            "en": "H.V. Kamath remarked during the debate: 'This is a day of sorrow and shame. God save the Indian people from this Constitution.'",
            "ta": "விவாதத்தின் போது எச்.வி. காமத் குறிப்பிட்டார்: 'இது துக்கமும் வெட்கமும் நிறைந்த நாள். இந்த அரசியலமைப்பிலிருந்து கடவுள் இந்திய மக்களைக் காப்பாற்றுவாராக.'."
        },
        "revision_fact": {
            "en": "Articles 352 (National), 356 (State/President's Rule), and 360 (Financial) constitute Part XVIII of the Constitution.",
            "ta": "சரத்துகள் 352 (தேசியம்), 356 (மாநிலம்/குடியரசுத் தலைவர் ஆட்சி), 360 (நிதி) ஆகியவை அரசியலமைப்பின் பகுதி XVIII ஐ உருவாக்குகின்றன."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Understand",
        "estimated_time_sec": 60,
        "pyq_similarity": "High",
        "tags": ["Emergency Provisions Debate", "Ambedkar Dead Letter", "H.V. Kamath Criticism"]
    },
    # Q19
    {
        "id": "MIC_M_019",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "Conceptual",
        "question": {
            "en": "Why was the Uniform Civil Code (UCC) placed under Article 44 of Directive Principles of State Policy rather than made an immediately enforceable Fundamental Right?",
            "ta": "பொதுச் சிவில் சட்டம் (UCC) ஏன் உடனடியாக அமல்படுத்தப்படக்கூடிய அடிப்படை உரிமையாக மாற்றப்படாமல், அரசு நெறிமுறைகளின் சரத்து 44 இன் கீழ் வைக்கப்பட்டது?"
        },
        "options": [
            {"id": "A", "en": "To prevent communal disharmony during the fragile post-partition period and allow national consensus to evolve naturally among diverse religious groups.", "ta": "பலவீனமான பிரிவினைக்குப் பிந்தைய காலத்தில் வகுப்புவாத சீர்குலைவைத் தடுக்கவும், பல்வேறு மதக் குழுக்களிடையே தேசிய ஒருமித்த கருத்து இயல்பாக உருவாக அனுமதிக்கவும்."},
            {"id": "B", "en": "Because the Drafting Committee believed that family personal laws were beyond the legislative competence of any sovereign parliament.", "ta": "ஏனெனில் குடும்பத் தனிநபர் சட்டங்கள் எந்தவொரு இறையாண்மை கொண்ட நாடாளுமன்றத்தின் சட்டத்துறை அதிகார வரம்பிற்கு அப்பாற்பட்டவை என்று வரைவுக் குழு நம்பியதால்."},
            {"id": "C", "en": "The Cabinet Mission Plan contained a permanent clause prohibiting India from reforming personal laws.", "ta": "தனிநபர் சட்டங்களை இந்தியா சீர்திருத்துவதைத் தடுக்கும் நிரந்தரச் சரத்து கேபினட் தூதுக்குழு திட்டத்தில் இருந்ததால்."},
            {"id": "D", "en": "Because the League of Nations issued a directive mandating separate personal laws in all Asian republics.", "ta": "ஏனெனில் அனைத்து ஆசியக் குடியரசுகளிலும் தனித்தனி தனிநபர் சட்டங்களைக் கட்டாயப்படுத்தும் வழிகாட்டுதலை சர்வதேச சங்கம் வெளியிட்டதால்."}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Muslim members (like Poker Sahib, Naziruddin Ahmad) expressed anxiety that a mandatory UCC would infringe on religious freedom. Dr. Ambedkar reassured the Assembly that Article 44 was purely directional and that no future Parliament would enforce a UCC in a manner that created communal friction.",
            "ta": "கட்டாய பொதுச் சிவில் சட்டம் மத சுதந்திரத்தை மீறும் என்று முஸ்லிம் உறுப்பினர்கள் கவலை தெரிவித்தனர். சரத்து 44 முற்றிலும் வழிகாட்டுதல் மட்டுமே என்றும், வகுப்புவாத உராய்வை உருவாக்கும் வகையில் எதிர்கால நாடாளுமன்றம் பொதுச் சிவில் சட்டத்தை அமல்படுத்தாது என்றும் டாக்டர் அம்பேத்கர் அவைக்கு உறுதியளித்தார்."
        },
        "why_not_others": {
            "A": {"en": "Correct. Desire for national integration without forcing instant reform on sensitive minority personal laws.", "ta": "சரி. உணர்திறன் மிக்க சிறுபான்மையினரின் தனிநபர் சட்டங்கள் மீது உடனடி சீர்திருத்தத்தைக் திணிக்காமல் தேசிய ஒருங்கிணைப்பை விரும்பியது."},
            "B": {"en": "Incorrect. Parliament has full legislative competence under Concurrent List Item 5 over marriage, divorce, and succession.", "ta": "தவறு. திருமணம், விவாகரத்து, வாரிசுரிமை மீது பொதுப்பட்டியல் உருப்படி 5 இன் கீழ் நாடாளுமன்றத்திற்கு முழு சட்ட அதிகார வரம்பு உள்ளது."},
            "C": {"en": "Incorrect. Cabinet Mission Plan had no such prohibition clause.", "ta": "தவறு. கேபினட் தூதுக்குழு திட்டத்தில் அத்தகைய தடைச் சரத்து எதுவும் இல்லை."},
            "D": {"en": "Incorrect. League of Nations had no directive on civil codes.", "ta": "தவறு. சிவில் சட்டங்கள் குறித்து சர்வதேச சங்கத்திற்கு எந்த வழிகாட்டுதலும் இல்லை."}
        },
        "tnpsc_tip": {
            "en": "K.M. Munshi argued in favor of UCC: 'Personal laws should be separated from religion so that gender equality and national unity can be achieved.'",
            "ta": "கே.எம். முன்ஷி UCC க்கு ஆதரவாக வாதிட்டார்: 'பாலின சமத்துவத்தையும் தேசிய ஒற்றுமையையும் அடையும் வகையில் தனிநபர் சட்டங்கள் மதத்திலிருந்து பிரிக்கப்பட வேண்டும்.'."
        },
        "revision_fact": {
            "en": "Article 44 states that the State shall endeavor to secure for the citizens a Uniform Civil Code throughout the territory of India.",
            "ta": "சரத்து 44, இந்தியா முழுவதிலும் உள்ள குடிமக்களுக்கு ஒரு பொதுவான சிவில் சட்டத்தைப் பெற அரசு முயல வேண்டும் என்று கூறுகிறது."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Understand",
        "estimated_time_sec": 60,
        "pyq_similarity": "High",
        "tags": ["Uniform Civil Code Debate", "Article 44 DPSP", "Minority Personal Laws"]
    },
    # Q20
    {
        "id": "MIC_M_020",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "Process-Based",
        "question": {
            "en": "How was the highly contentious issue of the 'Official Language of the Union' resolved by the Constituent Assembly under the famous Munshi-Ayyangar Formula?",
            "ta": "புகழ்பெற்ற முன்ஷி-அய்யங்கார் சூத்திரத்தின் கீழ் அரசியலமைப்பு நிர்ணய அவையால் 'ஒன்றியத்தின் அதிகாரப்பூர்வ மொழி' என்ற மிகவும் சர்ச்சைக்கிரிய பிரச்சினை எவ்வாறு தீர்க்கப்பட்டது?"
        },
        "options": [
            {"id": "A", "en": "Hindi in Devanagari script was declared the Official Language of the Union, while English was retained for all official purposes for an initial transition period of 15 years.", "ta": "தேவநாகரி வரிவடிவத்தில் உள்ள இந்தி ஒன்றியத்தின் அதிகாரப்பூர்வ மொழியாக அறிவிக்கப்பட்டது, அதே வேளையில் ஆங்கிலம் 15 ஆண்டுகால ஆரம்ப மாற்றக் காலத்திற்கு அனைத்து அதிகாரப்பூர்வ நோக்கங்களுக்கும் தக்கவைக்கப்பட்டது."},
            {"id": "B", "en": "Sanskrit was declared the sole National Language, banning English and Hindi from government records immediately.", "ta": "சமஸ்கிருதம் ஒரே தேசிய மொழியாக அறிவிக்கப்பட்டது, அரசாங்கப் பதிவேடுகளிலிருந்து ஆங்கிலம் மற்றும் இந்தி உடனடியாகத் தடைசெய்யப்பட்டது."},
            {"id": "C", "en": "Tamil and Hindi were declared dual co-equal official national languages for all central administration.", "ta": "மத்திய நிர்வாகம் அனைத்திற்கும் தமிழும் இந்தியும் சமமான இரு அதிகாரப்பூர்வ தேசிய மொழிகளாக அறிவிக்கப்பட்டன."},
            {"id": "D", "en": "The language decision was deferred permanently, leaving regional languages to operate without any Union official language.", "ta": "மொழி முடிவு நிரந்தரமாகத் தள்ளிவைக்கப்பட்டது, எந்தவொரு ஒன்றிய அதிகாரப்பூர்வ மொழியும் இன்றி பிராந்திய மொழிகள் செயல்பட வழிவகுத்தது."}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "The Language debate threatened to split the Assembly between Hindi proponents (like Purushottam Das Tandon) and non-Hindi delegates (from South India and Bengal). K.M. Munshi and N. Gopalaswami Ayyangar drafted a compromise formula: Hindi in Devanagari script is the Official Language, international form of Indian numerals is used, and English continues for 15 years (Article 343).",
            "ta": "மொழி விவாதம் இந்தி ஆதரவாளர்களுக்கும் (புருஷோத்தம் தாஸ் டாண்டன் போன்றோர்) இந்தி அல்லாத பிரதிநிதிகளுக்கும் (தென்னிந்தியா மற்றும் வங்காளம்) இடையே அவையைப் பிளவுபடுத்தும் அச்சுறுத்தலை ஏற்படுத்தியது. கே.எம். முன்ஷி மற்றும் என். கோபாலசுவாமி அய்யங்கார் ஒரு சமரச சூத்திரத்தை வரைந்தனர்: தேவநாகரி வடிவ இந்தி அதிகாரப்பூர்வ மொழி, இந்திய எண்களின் சர்வதேச வடிவம் பயன்படுத்தப்படும், மேலும் 15 ஆண்டுகளுக்கு ஆங்கிலம் தொடரும் (சரத்து 343)."
        },
        "why_not_others": {
            "A": {"en": "Correct. Munshi-Ayyangar formula balanced Hindi official language status with 15-year English transition period.", "ta": "சரி. முன்ஷி-அய்யங்கார் சூத்திரம் இந்தி அதிகாரப்பூர்வ மொழி அந்தஸ்தை 15 ஆண்டுகால ஆங்கில மாற்றக் காலத்துடன் சமநிலைப்படுத்தியது."},
            "B": {"en": "Incorrect. Sanskrit was not made the sole national language.", "ta": "தவறு. சமஸ்கிருதம் ஒரே தேசிய மொழியாக மாற்றப்படவில்லை."},
            "C": {"en": "Incorrect. Tamil was included in the Eighth Schedule, but not made central co-official language in 1949.", "ta": "தவறு. தமிழ் எட்டாவது அட்டவணையில் சேர்க்கப்பட்டது, ஆனால் 1949 இல் மத்திய இணை அதிகாரப்பூர்வ மொழியாக மாற்றப்படவில்லை."},
            "D": {"en": "Incorrect. Article 343 explicitly laid down the official language framework.", "ta": "தவறு. சரத்து 343 அதிகாரப்பூர்வ மொழிக் கட்டமைப்பைத் தெளிவாக வகுத்தது."}
        },
        "tnpsc_tip": {
            "en": "Note: The Constitution uses the term 'Official Language' (அதிகாரப்பூர்வ மொழி) under Part XVII, and NOT 'National Language' (தேசிய மொழி).",
            "ta": "குறிப்பு: அரசியலமைப்பு பகுதி XVII இன் கீழ் 'அதிகாரப்பூர்வ மொழி' என்ற சொல்லைப் பயன்படுத்துகிறது, 'தேசிய மொழி' என்ற சொல்லை அல்ல."
        },
        "revision_fact": {
            "en": "Official Languages Act of 1963 extended the use of English indefinitely beyond the initial 15-year period (1965).",
            "ta": "1963 ஆம் ஆண்டின் அதிகாரப்பூர்வ மொழிகள் சட்டம் ஆரம்ப 15 ஆண்டுகாலத்திற்கு (1965) அப்பாலும் ஆங்கிலத்தின் பயன்பாட்டை காலவரையின்றி நீடித்தது."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Understand",
        "estimated_time_sec": 60,
        "pyq_similarity": "High",
        "tags": ["Language Debate", "Munshi-Ayyangar Formula", "Article 343"]
    },
    # Q21
    {
        "id": "MIC_M_021",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "Process-Based",
        "question": {
            "en": "Why did the Constituent Assembly adopt the National Flag on July 22, 1947, several weeks prior to formal Independence on August 15, 1947?",
            "ta": "ஆகஸ்ட் 15, 1947 இல் முறைப்படியான சுதந்திரத்திற்கு பல வாரங்களுக்கு முன், ஜூலை 22, 1947 அன்று தேசியக் கொடியை அரசியலமைப்பு நிர்ணய அவை ஏன் ஏற்றுக்கொண்டது?"
        },
        "options": [
            {"id": "A", "en": "To ensure that a sovereign national emblem was officially ready to be hoisted during the midnight independence ceremony and flown on official government buildings.", "ta": "நள்ளிரவு சுதந்திர விழாவின் போது அதிகாரப்பூர்வமாக ஏற்றுவதற்கும் அரசு கட்டிடங்களில் பறக்கவிடுவதற்கும் ஒரு இறையாண்மை கொண்ட தேசிய சின்னம் தயாராக இருப்பதை உறுதி செய்ய."},
            {"id": "B", "en": "Because the British Parliament insisted that the flag design must be submitted for royal approval 30 days before independence.", "ta": "ஏனெனில் சுதந்திரத்திற்கு 30 நாட்களுக்கு முன் கொடி வடிவமைப்பு அரச ஒப்புதலுக்கு சமர்ப்பிக்கப்பட வேண்டும் என்று பிரிட்டிஷ் நாடாளுமன்றம் வலியுறுத்தியதால்."},
            {"id": "C", "en": "To comply with a mandatory requirement of the United Nations Security Council for recognizing new sovereign nations.", "ta": "புதிய இறையாண்மை கொண்ட நாடுகளை அங்கீகரிப்பதற்காக ஐக்கிய நாடுகள் பாதுகாப்பு சபையின் கட்டாயத் தேவையைப் பூர்த்தி செய்ய."},
            {"id": "D", "en": "Because the Charkha (spinning wheel) was legally protected under international patent law.", "ta": "ஏனெனில் இராட்டை (சர்க்கா) சர்வதேச காப்புரிமைச் சட்டத்தின் கீழ் சட்டப்பூர்வமாக பாதுகாக்கப்பட்டிருந்ததால்."}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Jawaharlal Nehru presented the resolution for adopting the Tricolor (Saffron, White, Green with Ashoka's Dharma Chakra in navy blue replacing the charkha) on July 22, 1947. This allowed state departments, diplomatic missions, and citizens to prepare for hoisting the sovereign flag on August 15.",
            "ta": "ஜூலை 22, 1947 அன்று ஜவஹர்லால் நேரு மூவர்ணக் கொடியை (இராட்டைக்கு பதிலாக கடற்படை நீல நிற அசோக தர்ம சக்கரத்துடன் காவி, வெள்ளை, பச்சை) ஏற்றுக்கொள்வதற்கான தீர்மானத்தை முன்வைத்தார். இது ஆகஸ்ட் 15 அன்று இறையாண்மை கொடியை ஏற்றுவதற்கு அரசுத் துறைகள், இராஜதந்திர தூதரகங்கள் மற்றும் குடிமக்கள் ஆயத்தமாக வழிவகுத்தது."
        },
        "why_not_others": {
            "A": {"en": "Correct. National Flag adoption on July 22, 1947 prepared the nation for Independence Day ceremonial hoisting.", "ta": "சரி. ஜூலை 22, 1947 அன்று தேசியக் கொடி ஏர்ப்பு சுதந்திர தின விழா ஏற்றத்திற்கு தேசத்தை ஆயத்தப்படுத்தியது."},
            "B": {"en": "Incorrect. Flag design required no British royal approval.", "ta": "தவறு. கொடி வடிவமைப்புக்கு பிரிட்டிஷ் அரச ஒப்புதல் எதுவும் தேவையில்லை."},
            "C": {"en": "Incorrect. UNSC did not mandate flag submission timing.", "ta": "தவறு. ஐநா பாதுகாப்பு சபை கொடி சமர்ப்பிக்கும் நேரத்தைக் கட்டாயப்படுத்தவில்லை."},
            "D": {"en": "Incorrect. Patent law had no connection to replacing charkha with Ashoka Chakra.", "ta": "தவறு. இராட்டையை அசோக சக்கரமாக மாற்றியதற்கு காப்புரிமை சட்டத்துடன் எந்த தொடர்பும் இல்லை."}
        },
        "tnpsc_tip": {
            "en": "Nehru described the Flag as 'a flag of freedom and a flag that will bring freedom not only to ourselves, but a message of freedom to all people who see it'.",
            "ta": "நேரு கொடியை 'ஒரு சுதந்திரத்தின் கொடி மற்றும் நமக்கு மட்டுமல்லாமல் அதைப்பார்க்கும் அனைத்து மக்களுக்கும் சுதந்திரத்தின் செய்தியைக் கொண்டுவரும் கொடி' என்று விவரித்தார்."
        },
        "revision_fact": {
            "en": "The Flag was designed by Pingali Venkayya and modified by the Assembly committee.",
            "ta": "தேசியக் கொடி பிங்கலி வெங்கையாவால் வடிவமைக்கப்பட்டு அவைக் குழுவால் மாற்றியமைக்கப்பட்டது."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Understand",
        "estimated_time_sec": 50,
        "pyq_similarity": "High",
        "tags": ["National Flag Adoption", "July 22 1947", "Pingali Venkayya"]
    },
    # Q22
    {
        "id": "MIC_M_022",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "Process-Based",
        "question": {
            "en": "Why did India's decision to maintain membership in the Commonwealth of Nations in May 1949 spark debate, and how was it justified by Nehru?",
            "ta": "மே 1949 இல் காமன்வெல்த் அமைப்பில் உறுப்பினர் உரிமையைத் தக்கவைத்துக்கொள்ளும் இந்தியாவின் முடிவு ஏன் விவாதத்தைத் தூண்டியது, மேலும் அது நேருவால் எவ்வாறு நியாயப்படுத்தப்பட்டது?"
        },
        "options": [
            {"id": "A", "en": "Critics argued it compromised Republican sovereignty, but Nehru clarified that it was a voluntary association without allegiance to the British Crown or restriction on India's foreign policy.", "ta": "இது குடியரசு இறையாண்மையை சமரசம் செய்வதாக விமர்சகர்கள் வாதிட்டனர், ஆனால் இது பிரிட்டிஷ் அரசிற்கு விசுவாசம் இல்லாத அல்லது இந்தியாவின் வெளியுறவுக் கொள்கைக்கு எந்தக் கட்டுப்பாடும் இல்லாத தன்னார்வச் சங்கம் என்று நேரு தெளிவுபடுத்தினார்."},
            {"id": "B", "en": "It was approved only after Britain agreed to pay India £100 million annually as constitutional royalty.", "ta": "பிரிட்டன் இந்தியாவிற்கு ஆண்டுதோறும் £100 மில்லியனை அரசியலமைப்பு ராயல்டியாக வழங்க ஒப்புக்கொண்ட பிறகே இது அங்கீகரிக்கப்பட்டது."},
            {"id": "C", "en": "It automatically made the British monarch the ex-officio Commander-in-Chief of Indian armed forces.", "ta": "இது தானாகவே பிரிட்டிஷ் பேரரசரை இந்திய ஆயுதப்படைகளின் முன்னாள் தலைவர் பதவி வகிக்கும் தளபதியாக ஆக்கியது."},
            {"id": "D", "en": "The Assembly rejected Commonwealth membership permanently by a 90% margin.", "ta": "அவை காமன்வெல்த் உறுப்பினர் உரிமையை 90% வாக்கு வித்தியாசத்தில் நிரந்தரமாக நிராகரித்தது."}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "When India declared itself a Sovereign Democratic Republic, remaining in the Commonwealth seemed contradictory to some members. Nehru explained at the London Declaration (April 1949) that King George VI was recognized only as 'the symbol of the free association of independent member nations', without any constitutional authority over India.",
            "ta": "இந்தியா தன்னை ஒரு இறையாண்மை கொண்ட ஜனநாயகக் குடியரசாக அறிவித்த போது, காமன்வெல்த்தில் நீடிப்பது சில உறுப்பினர்களுக்கு முரண்பாடாகத் தோன்றியது. லண்டன் பிரகடனத்தில் (ஏப்ரல் 1949) ஆறாம் ஜார்ஜ் மன்னர் 'சுதந்திர உறுப்பினர் நாடுகளின் இலவசச் சங்கத்தின் அடையாளமாக' மட்டுமே அங்கீகரிக்கப்பட்டார், இந்தியாவின் மீது எந்த அரசியலமைப்பு அதிகாரமும் இல்லை என்று நேரு விளக்கினார்."
        },
        "why_not_others": {
            "A": {"en": "Correct. Commonwealth membership was an extra-constitutional voluntary international association.", "ta": "சரி. காமன்வெல்த் உறுப்பினருரிமை என்பது அரசியலமைப்பிற்கு அப்பாற்பட்ட தன்னார்வ சர்வதேச சங்கமாகும்."},
            "B": {"en": "Incorrect. No monetary royalty payment was involved.", "ta": "தவறு. இதில் எந்த பண ராயல்டி செலுத்துதலும் ஈடுபடவில்லை."},
            "C": {"en": "Incorrect. President of India is the Supreme Commander of Indian Armed Forces under Article 53.", "ta": "தவறு. சரத்து 53 இன் கீழ் இந்தியக் குடியரசுத் தலைவரே இந்திய ஆயுதப்படைகளின் தலைமைத் தளபதியாவார்."},
            "D": {"en": "Incorrect. Assembly ratified the membership resolution in May 1949.", "ta": "தவறு. அவை மே 1949 இல் உறுப்பினர் தீர்மானத்தை உறுதி செய்தது."}
        },
        "tnpsc_tip": {
            "en": "Nehru famously stated: 'We have touched the agreement with Britain with a touch of magic, leaving both completely free and friendly.'",
            "ta": "நேரு புகழ்பெற்ற முறையில் கூறினார்: 'நாங்கள் பிரிட்டனுடனான ஒப்பந்தத்தை ஒரு மாயத் தொடுதலுடன் தொட்டுள்ளோம், அது இருவரையும் முற்றிலும் சுதந்திரமாகவும் நட்பாகவும் விட்டுச்செல்கிறது.'."
        },
        "revision_fact": {
            "en": "India was the first republic to be admitted into the Commonwealth without swearing allegiance to the British Crown.",
            "ta": "பிரிட்டிஷ் அரசிற்கு விசுவாசப் பிரமாணம் செய்யாமல் காமன்வெல்த்தில் சேர்க்கப்பட்ட முதல் குடியரசு இந்தியா ஆகும்."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Understand",
        "estimated_time_sec": 60,
        "pyq_similarity": "High",
        "tags": ["Commonwealth Ratification", "May 1949", "Republican Sovereignty"]
    },
    # Q23
    {
        "id": "MIC_M_023",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "Process-Based",
        "question": {
            "en": "Why did the Constituent Assembly elect Dr. Rajendra Prasad as the first President of India on January 24, 1950, rather than holding immediate nationwide presidential elections?",
            "ta": "உடனடி நாடு தழுவிய குடியரசுத் தலைவர் தேர்தலை நடத்துவதற்குப் பதிலாக, ஜனவரி 24, 1950 அன்று டாக்டர் ராஜேந்திர பிரசாத்தை இந்தியாவின் முதல் குடியரசுத் தலைவராக அரசியலமைப்பு நிர்ணய அவை ஏன் தேர்ந்தெடுத்தது?"
        },
        "options": [
            {"id": "A", "en": "Because general elections based on the new adult franchise electorate could only be organized after preparing complete electoral rolls, requiring a provisional President in the interim.", "ta": "ஏனெனில் புதிய வயதுவந்தோர் வாக்குரிமையின் அடிப்படையிலான பொதுத் தேர்தல்களை முழுமையான வாக்காளர் பட்டியல்களைத் தயாரித்த பிறகே நடத்த முடியும் என்பதால், இடைக்காலத்தில் ஒரு தற்காலிகக் குடியரசுத் தலைவர் தேவைப்பட்டார்."},
            {"id": "B", "en": "Because the British Independence Act prohibited any direct presidential voting until 1960.", "ta": "ஏனெனில் பிரிட்டிஷ் சுதந்திரச் சட்டம் 1960 வரை எந்தவொரு நேரடி குடியரசுத் தலைவர் வாக்குப்பதிவையும் தடுத்திருந்ததால்."},
            {"id": "C", "en": "Because Dr. Rajendra Prasad was appointed for life by a special decree of the Privy Council.", "ta": "ஏனெனில் டாக்டர் ராஜேந்திர பிரசாத் பிரிவி கவுன்சிலின் சிறப்பு ஆணையால் ஆயுள் காலம் வரை நியமிக்கப்பட்டிருந்தார்."},
            {"id": "D", "en": "Because the Supreme Court ruled that parliamentary democracy did not require a President after 1950.", "ta": "ஏனெனில் 1950க்குப் பிறகு நாடாளுமன்ற ஜனநாயகத்திற்கு குடியரசுத் தலைவர் தேவைப்படவில்லை என்று உச்ச நீதிமன்றம் தீர்ப்பளித்ததால்."}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Under Article 380 (transitional provision), until a President was elected by an electoral college under Article 54 following general elections, the person elected by the Constituent Assembly would serve as provisional President of India. Dr. Rajendra Prasad took office on Jan 26, 1950 and served until elected regularly in 1952.",
            "ta": "சரத்து 380 இன் கீழ் (இடைக்கால விதி), பொதுத் தேர்தல்களைத் தொடர்ந்து சரத்து 54 இன் கீழ் வாக்காளர் மன்றத்தால் ஒரு குடியரசுத் தலைவர் தேர்ந்தெடுக்கப்படும் வரை, அரசியலமைப்பு நிர்ணய அவையால் தேர்ந்தெடுக்கப்பட்ட நபர் இந்தியாவின் தற்காலிகக் குடியரசுத் தலைவராகச் செயல்படுவார். டாக்டர் ராஜேந்திர பிரசாத் ஜனவரி 26, 1950 இல் பதவியேற்று 1952 இல் வழக்கமாகத் தேர்ந்தெடுக்கப்படும் வரை பணியாற்றினார்."
        },
        "why_not_others": {
            "A": {"en": "Correct. Constitutional transitional provision (Article 380) enabled seamless executive transition to a Republic.", "ta": "சரி. அரசியலமைப்பு இடைக்கால விதி (சரத்து 380) ஒரு குடியரசிற்கு தடையற்ற நிர்வாக மாற்றத்தை சாத்தியமாக்கியது."},
            "B": {"en": "Incorrect. 1947 Act had no restriction on presidential elections.", "ta": "தவறு. 1947 சட்டத்தில் குடியரசுத் தலைவர் தேர்தல்களுக்கு எந்தக் கட்டுப்பாடும் இல்லை."},
            "C": {"en": "Incorrect. He was elected democratically by the Assembly, not appointed for life by Privy Council.", "ta": "தவறு. அவர் அவையால் ஜனநாயக முறைப்படி தேர்ந்தெடுக்கப்பட்டார், பிரிவி கவுன்சிலால் ஆயுள் காலம் வரை நியமிக்கப்படவில்லை."},
            "D": {"en": "Incorrect. A President is mandatory head of state under Article 52.", "ta": "தவறு. சரத்து 52 இன் கீழ் குடியரசுத் தலைவர் கட்டாயமான அரசுத் தலைவராவார்."}
        },
        "tnpsc_tip": {
            "en": "Dr. Rajendra Prasad is the only Indian President to have served two full terms (1952-1957 and 1957-1962).",
            "ta": "டாக்டர் ராஜேந்திர பிரசாத் இரண்டு முழு பதவிக்காலங்கள் (1952-1957 மற்றும் 1957-1962) பணியாற்றிய ஒரே இந்தியக் குடியரசுத் தலைவர் ஆவார்."
        },
        "revision_fact": {
            "en": "The first general elections in Independent India were held between October 1951 and February 1952.",
            "ta": "சுதந்திர இந்தியாவின் முதல் பொதுத் தேர்தல்கள் அக்டோபர் 1951 மற்றும் பிப்ரவரி 1952 இடையே நடைபெற்றன."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Understand",
        "estimated_time_sec": 55,
        "pyq_similarity": "High",
        "tags": ["First President Election", "Dr. Rajendra Prasad", "Provisional President"]
    },
    # Q24
    {
        "id": "MIC_M_024",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "Constitutional Understanding",
        "question": {
            "en": "Why did specific provisions of the Constitution relating to Citizenship (Articles 5-9), Elections (Article 324), and Provisional Parliament come into force immediately on November 26, 1949, ahead of January 26, 1950?",
            "ta": "குடியுரிமை (சரத்துகள் 5-9), தேர்தல்கள் (சரத்து 324) மற்றும் தற்காலிக நாடாளுமன்றம் தொடர்பான அரசியலமைப்பின் குறிப்பிட்ட விதிகள் ஜனவரி 26, 1950க்கு முன் நவம்பர் 26, 1949 அன்றே ஏன் உடனடியாக நடைமுறைக்கு வந்தன?"
        },
        "options": [
            {"id": "A", "en": "To immediately establish legal citizenship criteria for post-partition refugees and enable administrative machinery to prepare for governance and upcoming national elections.", "ta": "பிரிவினைக்குப் பிந்தைய அகதிகளுக்கான சட்டப்பூர்வ குடியுரிமை அளவுகோல்களை உடனடியாக நிறுவவும், நிர்வாக இயந்திரம் ஆட்சிக்கும் வரவிருக்கும் தேசியத் தேர்தல்களுக்கும் ஆயத்தமாக அனுமதிக்கவும்."},
            {"id": "B", "en": "Because the British Parliament threatened to revoke independence if those specific articles were delayed.", "ta": "ஏனெனில் அந்த குறிப்பிட்ட சரத்துகள் தாமதமானால் சுதந்திரத்தை ரத்து செய்வதாக பிரிட்டிஷ் நாடாளுமன்றம் அச்சுறுத்தியதால்."},
            {"id": "C", "en": "Because the Supreme Court ruled that Article 324 must precede all fundamental rights.", "ta": "ஏனெனில் சரத்து 324 அனைத்து அடிப்படை உரிமைகளுக்கும் முந்த வேண்டும் என்று உச்ச நீதிமன்றம் தீர்ப்பளித்ததால்."},
            {"id": "D", "en": "Because the Drafting Committee lost the original manuscript for the remaining articles until January 1950.", "ta": "ஏனெனில் ஜனவரி 1950 வரை எஞ்சிய சரத்துகளுக்கான மூலப் பிரதியை வரைவுக் குழு இழந்திருந்ததால்."}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Article 394 specified that Articles 5, 6, 7, 8, 9 (citizenship), 60 (President's oath), 324 (Election Commission), 366, 367, 379, 380, 388, 391, 392, 393 came into force at once on Nov 26, 1949. This was legally necessary to define who was an Indian citizen after partition trauma and empower the provisional government.",
            "ta": "சரத்து 394, சரத்துகள் 5, 6, 7, 8, 9 (குடியுரிமை), 60 (குடியரசுத் தலைவர் உறுதிமொழி), 324 (தேர்தல் ஆணையம்) போன்றவை நவம்பர் 26, 1949 அன்று உடனடியாக நடைமுறைக்கு வந்ததாகக் குறிப்பிட்டது. பிரிவினை துயரத்திற்குப் பிறகு யார் இந்தியக் குடிமகன் என்பதை வரையறுக்கவும், தற்காலிக அரசாங்கத்திற்கு அதிகாரம் அளிக்கவும் இது சட்டப்பூர்வமாகத் தேவைப்பட்டது."
        },
        "why_not_others": {
            "A": {"en": "Correct. Article 394 governed immediate commencement of essential citizenship, oath, and electoral machinery provisions.", "ta": "சரி. சரத்து 394 அவசியமான குடியுரிமை, உறுதிமொழி மற்றும் தேர்தல் இயந்திர விதிகளின் உடனடித் தொடக்கத்தை நிர்வகித்தது."},
            "B": {"en": "Incorrect. British Parliament had no veto over implementation timing.", "ta": "தவறு. அமலாக்க நேரத்தில் பிரிட்டிஷ் நாடாளுமன்றத்திற்கு எந்த வீட்டோவும் இல்லை."},
            "C": {"en": "Incorrect. Supreme Court did not issue such a ruling.", "ta": "தவறு. உச்ச நீதிமன்றம் அத்தகைய தீர்ப்பை வழங்கவில்லை."},
            "D": {"en": "Incorrect. The manuscript was safe and complete; delay to Jan 26 was purely historic.", "ta": "தவறு. கையெழுத்துப் பிரதி பாதுகாப்பாகவும் முழுமையாகவும் இருந்தது; ஜனவரி 26க்கான தாமதம் முற்றிலும் வரலாற்று சிறப்புமிக்கது."}
        },
        "tnpsc_tip": {
            "en": "Remember: Article 394 is the 'commencement clause' that specifies which articles came into force on Nov 26, 1949 and which on Jan 26, 1950.",
            "ta": "நினைவில் கொள்க: சரத்து 394 என்பது நவம்பர் 26, 1949 இல் எந்தச் சரத்துகள் நடைமுறைக்கு வந்தன, ஜனவரி 26, 1950 இல் எந்தச் சரத்துகள் நடைமுறைக்கு வந்தன என்பதைக் குறிப்பிடும் 'தொடக்கச் சரத்து' ஆகும்."
        },
        "revision_fact": {
            "en": "The remaining major portion of the Constitution came into force on January 26, 1950 (Date of Commencement).",
            "ta": "அரசியலமைப்பின் எஞ்சிய முக்கிய பகுதி ஜனவரி 26, 1950 (நடைமுறைக்கு வந்த நாள்) அன்று நடைமுறைக்கு வந்தது."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Understand",
        "estimated_time_sec": 60,
        "pyq_similarity": "High",
        "tags": ["Article 394", "Immediate Commencement", "Nov 26 1949 Provisions"]
    },
    # Q25
    {
        "id": "MIC_M_025",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "Conceptual",
        "question": {
            "en": "What was the legal effect of Article 395 of the Constitution upon its full commencement on January 26, 1950?",
            "ta": "ஜனவரி 26, 1950 இல் முழுமையாக நடைமுறைக்கு வந்தவுடன் அரசியலமைப்பின் சரத்து 395 இன் சட்டப்பூர்வ விளைவு யாது?"
        },
        "options": [
            {"id": "A", "en": "It officially repealed the Indian Independence Act of 1947 and the Government of India Act of 1935, together with all enactments amending or supplementing them.", "ta": "இது 1947 ஆம் ஆண்டின் இந்திய சுதந்திரச் சட்டம் மற்றும் 1935 ஆம் ஆண்டின் இந்திய அரசுச் சட்டம் ஆகியவற்றை, அவற்றைத் திருத்தும் அல்லது சேர்க்கும் அனைத்து சட்டங்களுடன் அதிகாரப்பூர்வமாக ரத்து செய்தது."},
            {"id": "B", "en": "It declared that all existing British High Courts in India were abolished immediately.", "ta": "இந்தியாவில் உள்ள அனைத்து பிரிட்டிஷ் உயர் நீதிமன்றங்களும் உடனடியாக ஒழிக்கப்பட்டதாக இது அறிவித்தது."},
            {"id": "C", "en": "It merged all princely state territories directly under the Ministry of Defense.", "ta": "இது அனைத்து சுதேச அரசுப் பகுதிகளையும் பாதுகாப்பு அமைச்சகத்தின் கீழ் நேரடியாக இணைத்தது."},
            {"id": "D", "en": "It mandated that the Constitution could never be amended by any future Parliament.", "ta": "எதிர்கால நாடாளுமன்றத்தால் அரசியலமைப்பை ஒருபோதும் திருத்த முடியாது என்று இது கட்டாயப்படுத்தியது."}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Article 395 explicitly repealed the Indian Independence Act 1947 and the Government of India Act 1935 (except the Abolition of Privy Council Jurisdiction Act 1949), ensuring that India's constitutional law was completely indigenous and no longer derived from British statutes.",
            "ta": "சரத்து 395 1947 இந்திய சுதந்திரச் சட்டம் மற்றும் 1935 இந்திய அரசுச் சட்டத்தை (பிரிவி கவுன்சில் அதிகார வரம்பு ஒழிப்புச் சட்டம் 1949 தவிர) அதிகாரப்பூர்வமாக ரத்து செய்தது. இது இந்தியாவின் அரசியலமைப்புச் சட்டம் முற்றிலும் சுதேசியமானது என்பதையும் இனி பிரிட்டிஷ் சட்டங்களிலிருந்து பெறப்படவில்லை என்பதையும் உறுதி செய்தது."
        },
        "why_not_others": {
            "A": {"en": "Correct. Article 395 severed remaining statutory ties with British constitutional acts.", "ta": "சரி. சரத்து 395 பிரிட்டிஷ் அரசியலமைப்புச் சட்டங்களுடனான எஞ்சிய சட்டப்பூர்வத் தொடர்புகளைத் துண்டித்தது."},
            "B": {"en": "Incorrect. Existing High Courts were continued under Article 225, not abolished.", "ta": "தவறு. ஏற்கனவே இருந்த உயர் நீதிமன்றங்கள் சரத்து 225 இன் கீழ் தொடரப்பட்டன, ஒழிக்கப்படவில்லை."},
            "C": {"en": "Incorrect. Princely state integration was governed by Accession Instruments and Part B state structures.", "ta": "தவறு. சுதேச அரசு இணைப்பு சம்மதப் பத்திரங்கள் மற்றும் பகுதி B மாநிலக் கட்டமைப்புகளால் நிர்வகிக்கப்பட்டது."},
            "D": {"en": "Incorrect. Article 368 provided detailed amendment procedures.", "ta": "தவறு. சரத்து 368 விரிவான திருத்தச் செயல்முறைகளை வழங்கியது."}
        },
        "tnpsc_tip": {
            "en": "Article 395 is the final article of the original Constitution of India.",
            "ta": "சரத்து 395 என்பது மூல இந்திய அரசியலமைப்பின் இறுதிச் சரத்தாகும்."
        },
        "revision_fact": {
            "en": "The Abolition of Privy Council Jurisdiction Act (1949) was specifically exempted from repeal under Article 395.",
            "ta": "பிரிவி கவுன்சில் அதிகார வரம்பு ஒழிப்புச் சட்டம் (1949) சரத்து 395 இன் கீழ் ரத்து செய்யப்படுவதிலிருந்து குறிப்பாக விலக்கு அளிக்கப்பட்டது."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Understand",
        "estimated_time_sec": 55,
        "pyq_similarity": "High",
        "tags": ["Article 395 Repeal", "Colonial Laws Abolition", "1935 & 1947 Acts"]
    },
    # Q26
    {
        "id": "MIC_M_026",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "TNPSC Trap Questions",
        "question": {
            "en": "Which of the following pairs of Committee of the Constituent Assembly and its Chairman is INCORRECTLY matched?",
            "ta": "அரசியலமைப்பு நிர்ணய அவையின் குழு மற்றும் அதன் தலைவர் ஆகிய பின்வரும் இணைகளில் எது தவறாகப் பொருந்தியுள்ளது?"
        },
        "options": [
            {"id": "A", "en": "States Committee (Committee for Negotiating with States) — Sardar Vallabhbhai Patel", "ta": "மாநிலங்கள் குழு (மாநிலங்களுடன் பேச்சுவார்த்தை நடத்தும் குழு) — சர்தார் வல்லபாய் படேல்"},
            {"id": "B", "en": "Drafting Committee — Dr. B.R. Ambedkar", "ta": "வரைவுக் குழு — டாக்டர் பி.ஆர். அம்பேத்கர்"},
            {"id": "C", "en": "Rules of Procedure Committee — Dr. Rajendra Prasad", "ta": "நடைமுறை விதிகளுக்கான குழு — டாக்டர் ராஜேந்திர பிரசாத்"},
            {"id": "D", "en": "Union Constitution Committee — Jawaharlal Nehru", "ta": "மத்திய அரசியலமைப்புச் சாசனக் குழு — ஜவஹர்லால் நேரு"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "TRAP QUESTION! The States Committee (Committee for Negotiating with States) was chaired by Jawaharlal Nehru, NOT Sardar Patel. Patel chaired the Provincial Constitution Committee and the Advisory Committee on Fundamental Rights, Minorities and Tribal Areas.",
            "ta": "வலைக் கேள்வி! மாநிலங்கள் குழுவிற்கு (மாநிலங்களுடன் பேச்சுவார்த்தை நடத்தும் குழு) ஜவஹர்லால் நேரு தலைமை தாங்கினார், சர்தார் படேல் அல்ல. படேல் மாகாண அரசியலமைப்புச் சாசனக் குழு மற்றும் ஆலோசனைக் குழுவிற்கு தலைமை தாங்கினார்."
        },
        "why_not_others": {
            "A": {"en": "Correct (Incorrectly Matched). States Committee Chairman was Jawaharlal Nehru. People wrongly assume Patel because he integrated princely states.", "ta": "சரி (தவறாகப் பொருந்தியுள்ளது). மாநிலங்கள் குழுவின் தலைவர் ஜவஹர்லால் நேரு. படேல் சுதேச அரசுகளை இணைத்ததால் மக்கள் தவறாக அவரை ஊகிப்பார்கள்."},
            "B": {"en": "Incorrect (Correctly Matched). Ambedkar chaired Drafting Committee.", "ta": "தவறு (சரியாகப் பொருந்தியுள்ளது). அம்பேத்கர் வரைவுக்குழுத் தலைவர்."},
            "C": {"en": "Incorrect (Correctly Matched). Rajendra Prasad chaired Rules of Procedure Committee.", "ta": "தவறு (சரியாகப் பொருந்தியுள்ளது). ராஜேந்திர பிரசாத் நடைமுறை விதிகள் குழுத் தலைவர்."},
            "D": {"en": "Incorrect (Correctly Matched). Nehru chaired Union Constitution Committee.", "ta": "தவறு (சரியாகப் பொருந்தியுள்ளது). நேரு மத்திய அரசியலமைப்புச் சாசனக் குழுத் தலைவர்."}
        },
        "tnpsc_tip": {
            "en": "Major Trap: States Committee -> Nehru; Provincial Constitution Committee -> Patel.",
            "ta": "முக்கிய வலை: மாநிலங்கள் குழு -> நேரு; மாகாண அரசியலமைப்புச் சாசனக் குழு -> படேல்."
        },
        "revision_fact": {
            "en": "Jawaharlal Nehru chaired three major committees: 1. Union Powers, 2. Union Constitution, 3. States Committee.",
            "ta": "ஜவஹர்லால் நேரு மூன்று முக்கிய குழுக்களுக்கு தலைமை தாங்கினார்: 1. மத்திய அதிகாரங்கள், 2. மத்திய அரசியலமைப்புச் சாசனம், 3. மாநிலங்கள் குழு."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Understand",
        "estimated_time_sec": 50,
        "pyq_similarity": "High",
        "tags": ["States Committee Trap", "Jawaharlal Nehru", "Patel Distinction"]
    },
    # Q27
    {
        "id": "MIC_M_027",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "Basic Statement Model",
        "question": {
            "en": "Consider the following statements regarding the Drafting Committee of the Constituent Assembly:\n1. It was set up on August 29, 1947, with Dr. B.R. Ambedkar as Chairman.\n2. N. Madhava Rau replaced B.L. Mitter who resigned due to ill-health.\n3. T.T. Krishnamachari replaced D.P. Khaitan who died in 1948.\n\nWhich of the statements given above is/are correct?",
            "ta": "அரசியலமைப்பு வரைவுக் குழு பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. இது ஆகஸ்ட் 29, 1947 இல் டாக்டர் பி.ஆர். அம்பேத்கரைத் தலைவராகக் கொண்டு அமைக்கப்பட்டது.\n2. உடல்நலக் குறைவால் ராஜினாமா செய்த பி.எல். மிட்டருக்கு பதிலாக என். மாதவ ராவ் நியமிக்கப்பட்டார்.\n3. 1948 இல் மறைந்த டி.பி. கைத்தானுக்கு பதிலாக டி.டி. கிருஷ்ணமாச்சாரி நியமிக்கப்பட்டார்.\n\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 and 2 only", "ta": "1 மற்றும் 2 மட்டுமே"},
            {"id": "B", "en": "2 and 3 only", "ta": "2 மற்றும் 3 மட்டுமே"},
            {"id": "C", "en": "1 and 3 only", "ta": "1 மற்றும் 3 மட்டுமே"},
            {"id": "D", "en": "1, 2, and 3", "ta": "1, 2 மற்றும் 3"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "All three statements are factually and conceptually correct. The 7 members were Ambedkar (Chair), Gopalaswami Ayyangar, Alladi Krishnaswami Ayyar, K.M. Munshi, Saadullah, N. Madhava Rau (replaced Mitter), and T.T. Krishnamachari (replaced Khaitan).",
            "ta": "மூன்று கூற்றுகளும் தகவமைப்பு மற்றும் கோட்பாட்டு ரீதியாக சரியானவை. 7 உறுப்பினர்கள்: அம்பேத்கர் (தலைவர்), கோபாலசுவாமி அய்யங்கார், அல்லாடி கிருஷ்ணசுவாமி அய்யர், கே.எம். முன்ஷி, சாதுல்லா, என். மாதவ ராவ் (மிட்டருக்கு பதில்), மற்றும் டி.டி. கிருஷ்ணமாச்சாரி (கைத்தானுக்கு பதில்)."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Statement 3 is also correct.", "ta": "தவறு. கூற்று 3 உம் சரியானது."},
            "B": {"en": "Incorrect. Statement 1 is also correct.", "ta": "தவறு. கூற்று 1 உம் சரியானது."},
            "C": {"en": "Incorrect. Statement 2 is also correct.", "ta": "தவறு. கூற்று 2 உம் சரியானது."},
            "D": {"en": "Correct. All 1, 2, and 3 are true.", "ta": "சரி. 1, 2 மற்றும் 3 ஆகிய அனைத்தும் சரியானவை."}
        },
        "tnpsc_tip": {
            "en": "Remember the two replacements in the Drafting Committee: Mitter -> Madhava Rau; Khaitan -> Krishnamachari.",
            "ta": "வரைவுக் குழுவின் இரண்டு மாற்றங்களை நினைவில் கொள்க: மிட்டர் -> மாதவ ராவ்; கைத்தான் -> கிருஷ்ணமாச்சாரி."
        },
        "revision_fact": {
            "en": "The Drafting Committee sat for 141 days and prepared the draft within 6 months.",
            "ta": "வரைவுக் குழு 141 நாட்கள் அமர்ந்து 6 மாதங்களுக்குள் வரைவைத் தயாரித்தது."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Understand",
        "estimated_time_sec": 55,
        "pyq_similarity": "High",
        "tags": ["Drafting Committee Statement", "Replacements", "7 Members"]
    },
    # Q28
    {
        "id": "MIC_M_028",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "Basic Statement Model",
        "question": {
            "en": "Consider the following statements regarding the Objectives Resolution:\n1. It was moved by Jawaharlal Nehru on December 13, 1946.\n2. It was unanimously adopted by the Assembly on January 22, 1947.\n3. Its modified version forms the Preamble of the present Constitution.\n\nWhich of the statements given above are correct?",
            "ta": "குறிக்கோள் தீர்மானம் பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. இது டிசம்பர் 13, 1946 இல் ஜவஹர்லால் நேருவால் முன்மொழியப்பட்டது.\n2. இது ஜனவரி 22, 1947 அன்று அவையால் ஒருமனதாக ஏற்றுக்கொள்ளப்பட்டது.\n3. இதன் திருத்தப்பட்ட வடிவமே தற்போதைய அரசியலமைப்பின் முகப்புரையாக உள்ளது.\n\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 and 2 only", "ta": "1 மற்றும் 2 மட்டுமே"},
            {"id": "B", "en": "2 and 3 only", "ta": "2 மற்றும் 3 மட்டுமே"},
            {"id": "C", "en": "1 and 3 only", "ta": "1 மற்றும் 3 மட்டுமே"},
            {"id": "D", "en": "1, 2, and 3", "ta": "1, 2 மற்றும் 3"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "All three statements are true. Nehru moved it on Dec 13, 1946; Assembly adopted it on Jan 22, 1947; and it was adapted into the Preamble of the Indian Constitution.",
            "ta": "மூன்று கூற்றுகளும் உண்மையானவை. நேரு டிசம்பர் 13, 1946 இல் முன்மொழிந்தார்; அவை ஜனவரி 22, 1947 இல் ஏற்றுக்கொண்டது; மேலும் இது இந்திய அரசியலமைப்பின் முகப்புரையாக மாற்றியமைக்கப்பட்டது."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Statement 3 is also correct.", "ta": "தவறு. கூற்று 3 உம் சரியானது."},
            "B": {"en": "Incorrect. Statement 1 is also correct.", "ta": "தவறு. கூற்று 1 உம் சரியானது."},
            "C": {"en": "Incorrect. Statement 2 is also correct.", "ta": "தவறு. கூற்று 2 உம் சரியானது."},
            "D": {"en": "Correct. Statements 1, 2, and 3 are all correct.", "ta": "சரி. கூற்றுகள் 1, 2 மற்றும் 3 அனைத்தும் சரியானவை."}
        },
        "tnpsc_tip": {
            "en": "Common TNPSC question combination! Note the timeline sequence: Dec 13, 1946 (Moved) -> Jan 22, 1947 (Adopted) -> Nov 26, 1949 (Preamble enacted).",
            "ta": "பொதுவான டிஎன்பிஎஸ்சி கேள்வி சேர்க்கை! காலவரிசையைக் கவனிக்கவும்: டிசம்பர் 13, 1946 (முன்மொழிவு) -> ஜனவரி 22, 1947 (ஏற்பு) -> நவம்பர் 26, 1949 (முகப்புரை இயற்றம்)."
        },
        "revision_fact": {
            "en": "The Objectives Resolution contained 8 main paragraphs outlining democratic republic ideals.",
            "ta": "குறிக்கோள் தீர்மானம் ஜனநாயகக் குடியரசு இலட்சியங்களை விவரிக்கும் 8 முக்கிய பத்திகளைக் கொண்டிருந்தது."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Understand",
        "estimated_time_sec": 50,
        "pyq_similarity": "High",
        "tags": ["Objectives Resolution Statement", "Preamble Origin", "Timeline"]
    },
    # Q29
    {
        "id": "MIC_M_029",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "TNPSC Trap Questions",
        "question": {
            "en": "Which of the following prominent national leaders was NOT a member of the Constituent Assembly of India?",
            "ta": "பின்வரும் முக்கிய தேசியத் தலைவர்களில் யார் இந்திய அரசியலமைப்பு நிர்ணய அவையில் உறுப்பினராக இருக்கவில்லை?"
        },
        "options": [
            {"id": "A", "en": "Mahatma Gandhi and Muhammad Ali Jinnah", "ta": "மகாத்மா காந்தி மற்றும் முகமது அலி ஜின்னா"},
            {"id": "B", "en": "Dr. Rajendra Prasad and Sardar Patel", "ta": "டாக்டர் ராஜேந்திர பிரசாத் மற்றும் சர்தார் படேல்"},
            {"id": "C", "en": "Jawaharlal Nehru and C. Rajagopalachari", "ta": "ஜவஹர்லால் நேரு மற்றும் சி. ராஜகோபாலாச்சாரி"},
            {"id": "D", "en": "Dr. B.R. Ambedkar and K.M. Munshi", "ta": "டாக்டர் பி.ஆர். அம்பேத்கர் மற்றும் கே.எம். முன்ஷி"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "TRAP QUESTION! With the exception of Mahatma Gandhi and Muhammad Ali Jinnah, the Constituent Assembly included almost all important personalities of India at that time.",
            "ta": "வலைக் கேள்வி! மகாத்மா காந்தி மற்றும் முகமது அலி ஜின்னா ஆகிய இருவரைத் தவிர, அக்காலகட்டத்தின் இந்தியாவின் அனைத்து முக்கிய ஆளுமைகளும் அரசியலமைப்பு நிர்ணய அவையில் இடம் பெற்றிருந்தனர்."
        },
        "why_not_others": {
            "A": {"en": "Correct. Both Mahatma Gandhi and M.A. Jinnah stayed out of the Constituent Assembly.", "ta": "சரி. மகாத்மா காந்தி மற்றும் எம்.ஏ. ஜின்னா ஆகிய இருவரும் அரசியலமைப்பு நிர்ணய அவையிலிருந்து விலகியிருந்தனர்."},
            "B": {"en": "Incorrect. Both Rajendra Prasad and Sardar Patel were prominent members.", "ta": "தவறு. ராஜேந்திர பிரசாத் மற்றும் சர்தார் படேல் ஆகிய இருவரும் முக்கிய உறுப்பினர்கள்."},
            "C": {"en": "Incorrect. Nehru and Rajaji were prominent members.", "ta": "தவறு. நேரு மற்றும் ராஜாஜி முக்கிய உறுப்பினர்கள்."},
            "D": {"en": "Incorrect. Ambedkar and Munshi were key Drafting Committee members.", "ta": "தவறு. அம்பேத்கர் மற்றும் முன்ஷி முக்கிய வரைவுக்குழு உறுப்பினர்கள்."}
        },
        "tnpsc_tip": {
            "en": "Always remember this classic exception: Gandhi and Jinnah were NEVER members of the Constituent Assembly.",
            "ta": "இந்த உன்னதமான விலக்கை எப்போதும் நினைவில் கொள்க: காந்தி மற்றும் ஜின்னா நிர்ணய அவையில் ஒருபோதும் உறுப்பினர்களாக இல்லை."
        },
        "revision_fact": {
            "en": "Although Gandhi was not a member, his philosophy heavily influenced the Directive Principles (Article 40, 43, 47, 48).",
            "ta": "காந்தி உறுப்பினராக இல்லாவிட்டாலும், அவரது தத்துவம் அரசு நெறிமுறைகளில் பெரும் தாக்கத்தை ஏற்படுத்தியது (சரத்துகள் 40, 43, 47, 48)."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Remember",
        "estimated_time_sec": 45,
        "pyq_similarity": "High",
        "tags": ["Gandhi Jinnah Exclusion", "Assembly Membership", "TNPSC Trap"]
    },
    # Q30
    {
        "id": "MIC_M_030",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "Conceptual",
        "question": {
            "en": "How did the partition of India under the Mountbatten Plan affect the territorial representation and composition of the Constituent Assembly?",
            "ta": "மவுண்ட்பேட்டன் திட்டத்தின் கீழ் இந்தியாவின் பிரிவினை அரசியலமைப்பு நிர்ணய அவையின் பிராந்தியப் பிரதிநிதித்துவம் மற்றும் அமைப்பை எவ்வாறு பாதித்தது?"
        },
        "options": [
            {"id": "A", "en": "Members from areas included in Pakistan (East Bengal, West Punjab, Sindh, NWFP, Baluchistan, Sylhet) ceased to be members, reducing Assembly strength from 389 to 299.", "ta": "பாகிஸ்தானில் சேர்க்கப்பட்ட பகுதிகளின் உறுப்பினர்கள் (கிழக்கு வங்காளம், மேற்கு பஞ்சாப், சிந்து, வடமேற்கு எல்லைப்புற மாகாணம், பலுசிஸ்தான், சில்ஹெட்) உறுப்பினர்களாக இருப்பது முடிவுக்கு வந்தது, அவையின் பலம் 389-லிருந்து 299 ஆகக் குறைந்தது."},
            {"id": "B", "en": "The Assembly was completely dissolved and a fresh election was ordered by Lord Mountbatten.", "ta": "அவை முற்றிலும் கலைக்கப்பட்டு புதிய தேர்தலுக்கு மவுண்ட்பேட்டன் பிரபு உத்தரவிட்டார்."},
            {"id": "C", "en": "The strength of Princely States increased from 93 to 150 to compensate for lost provincial seats.", "ta": "இழந்த மாகாண இடங்களை ஈடுசெய்ய சுதேச அரசுகளின் பலம் 93-லிருந்து 150 ஆக அதிகரித்தது."},
            {"id": "D", "en": "The Assembly membership remained exactly 389, but Pakistani delegates were given non-voting observer status.", "ta": "அவையின் உறுப்பினர்கள் எண்ணிக்கை சரியாக 389 ஆக இருந்தது, ஆனால் பாகிஸ்தான் பிரதிநிதிகளுக்கு வாக்களிக்கும் உரிமையற்ற பார்வையாளர் அந்தஸ்து வழங்கப்பட்டது."}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "With partition, members representing areas that went to Pakistan withdrew. The total strength was reduced to 299 (229 for Indian provinces and 70 for princely states), and the Assembly became a fully sovereign body for the Dominion of India.",
            "ta": "பிரிவினையுடன், பாகிஸ்தானுக்குச் சென்ற பகுதிகளின் உறுப்பினர்கள் விலகினர். மொத்த பலம் 299 ஆகக் குறைக்கப்பட்டது (இந்திய மாகாணங்களுக்கு 229 மற்றும் சுதேச அரசுகளுக்கு 70), மேலும் அவை இந்திய டொமினியனுக்கான முழு இறையாண்மை அமைப்பாக மாறியது."
        },
        "why_not_others": {
            "A": {"en": "Correct. Pakistan territory representatives ceased membership, dropping Assembly count to 299.", "ta": "சரி. பாகிஸ்தான் பகுதி பிரதிநிதிகள் உறுப்பினர் பதவியை இழந்தனர், எண்ணிக்கை 299 ஆகக் குறைந்தது."},
            "B": {"en": "Incorrect. Assembly was not dissolved; it was reconstituted for India.", "ta": "தவறு. அவை கலைக்கப்படவில்லை; இந்தியாவுக்காக மாற்றிமைக்கப்பட்டது."},
            "C": {"en": "Incorrect. Princely state quota also decreased from 93 to 70.", "ta": "தவறு. சுதேச அரசு ஒதுக்கீடும் 93-லிருந்து 70 ஆகக் குறைந்தது."},
            "D": {"en": "Incorrect. Pakistani delegates withdrew completely to form Pakistan's Constituent Assembly.", "ta": "தவறு. பாகிஸ்தான் பிரதிநிதிகள் பாகிஸ்தானின் நிர்ணய அவையை அமைக்க முற்றிலும் விலகினர்."}
        },
        "tnpsc_tip": {
            "en": "Breakdown to remember: Pre-partition: 389 (296 + 93); Post-partition: 299 (229 + 70).",
            "ta": "நினைவில் கொள்ள வேண்டிய பகுப்பு: பிரிவினைக்கு முன்: 389 (296 + 93); பிரிவினைக்குப் பின்: 299 (229 + 70)."
        },
        "revision_fact": {
            "en": "The revised figures were published on October 31, 1947.",
            "ta": "மாற்றிமைக்கப்பட்ட புள்ளிவிவரங்கள் அக்டோபர் 31, 1947 அன்று வெளியிடப்பட்டன."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Understand",
        "estimated_time_sec": 55,
        "pyq_similarity": "High",
        "tags": ["Partition Impact", "299 Members Breakdown", "Mountbatten Plan"]
    },
    # Q31
    {
        "id": "MIC_M_031",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "Process-Based",
        "question": {
            "en": "Why did the Constituent Assembly take nearly three years (2 years, 11 months, 18 days) to complete the framing of the Constitution?",
            "ta": "அரசியலமைப்பை உருவாக்கும் பணியை முடிக்க அரசியலமைப்பு நிர்ணய அவை ஏன் கிட்டத்தட்ட மூன்று ஆண்டுகள் (2 ஆண்டுகள், 11 மாதங்கள், 18 நாட்கள்) எடுத்துக்கொண்டது?"
        },
        "options": [
            {"id": "A", "en": "The framers conducted clause-by-clause scrutiny, debated 2,473 amendments, accommodated vast regional/communal diversity, and reconciled federalism with unity in a newly independent nation.", "ta": "உருவாக்குநர்கள் சரத்து வாரியாக கூர்ந்தாய்வு செய்தனர், 2,473 திருத்தங்களை விவாதித்தனர், பரந்த பிராந்திய/வகுப்புவாத பன்முகத்தன்மையை உள்ளடக்கி, ஒரு புதிய சுதந்திர நாட்டில் கூட்டாட்சியை ஒற்றுமையுடன் சமரசம் செய்தனர்."},
            {"id": "B", "en": "The Assembly was suspended for two years due to international sanctions imposed by the United Nations.", "ta": "ஐக்கிய நாடுகள் சபையால் விதிக்கப்பட்ட சர்வதேச தடைகள் காரணமாக அவை இரண்டு ஆண்டுகள் இடைநீக்கம் செய்யப்பட்டது."},
            {"id": "C", "en": "The Drafting Committee spent most of its time translating the text into 22 scheduled languages before presenting it to the Assembly.", "ta": "வரைவுக் குழு உரை அவையில் சமர்ப்பிப்பதற்கு முன் 22 அட்டவணை மொழிகளில் மொழிபெயர்ப்பதில் பெரும்பகுதியைச் செலவிட்டது."},
            {"id": "D", "en": "The British Governor-General vetoed three consecutive draft versions, forcing complete rewrites.", "ta": "பிரிட்டிஷ் கவர்னர்-ஜெனரல் தொடர்ச்சியாக மூன்று வரைவுப் பதிப்புகளை வீட்டோ செய்தார், இதனால் முழுமையாக மீண்டும் எழுத வேண்டிய கட்டாயம் ஏற்பட்டது."}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Unlike shorter constitutions, the Indian Constitution had to address complex problems: integrating 565 princely states, protecting minorities, balancing central-state relations, incorporating fundamental rights and DPSP, and tackling partition trauma through consensus-building.",
            "ta": "குறுகிய அரசியலமைப்புகளைப் போலல்லாமல், இந்திய அரசியலமைப்பு சிக்கலான பிரச்சினைகளுக்குத் தீர்வு காண வேண்டியிருந்தது: 565 சுதேச அரசுகளை இணைத்தல், சிறுபான்மையினரைப் பாதுகாத்தல், மத்திய-மாநில உறவுகளைச் சமநிலைப்படுத்துதல், அடிப்படை உரிமைகள் மற்றும் DPSP ஐ உள்ளடக்குதல், மற்றும் கருத்து ஒருமித்த கருத்து உருவாக்கம் மூலம் பிரிவினை வடுவைக் கையாளுதல்."
        },
        "why_not_others": {
            "A": {"en": "Correct. Consensus-seeking methodology, detailed debates on 2,473 amendments, and extraordinary diversity required extensive deliberations.", "ta": "சரி. கருத்து ஒருமித்த கருத்து நாடும் முறை, 2,473 திருத்தங்கள் பற்றிய விரிவான விவாதங்கள் மற்றும் அபரிமிதமான பன்முகத்தன்மை ஆகியவை பரந்த விவாதங்களைக் கோரின."},
            "B": {"en": "Incorrect. Assembly was never suspended by UN.", "ta": "தவறு. அவை ஐநாவால் ஒருபோதும் இடைநீக்கம் செய்யப்படவில்லை."},
            "C": {"en": "Incorrect. Draft was prepared in English initially; official translations were done alongside.", "ta": "தவறு. வரைவு ஆரம்பத்தில் ஆங்கிலத்தில் தயாரிக்கப்பட்டது; அதிகாரப்பூர்வ மொழிபெயர்ப்புகள் இணையாகச் செய்யப்பட்டன."},
            "D": {"en": "Incorrect. Governor-General had no veto power over Assembly drafts post-August 1947.", "ta": "தவறு. ஆகஸ்ட் 1947க்குப் பிறகு அவை வரைவுகள் மீது கவர்னர்-ஜெனரலுக்கு வீட்டோ அதிகாரம் இல்லை."}
        },
        "tnpsc_tip": {
            "en": "Method of decision-making: The Assembly preferred 'Consensus' and 'Accommodation' over simple majority voting whenever possible.",
            "ta": "முடிவெடுக்கும் முறை: எப்போதெல்லாம் சாத்தியமோ அப்போதெல்லாம் எளிய பெரும்பான்மை வாக்களிப்பை விட 'கருத்து ஒருமித்த கருத்து' மற்றும் 'சமரசம்' ஆகியவற்றை அவை விரும்பியது."
        },
        "revision_fact": {
            "en": "Granville Austin called the Indian constitution-making process an example of 'Consensus and Accommodation'.",
            "ta": "கான்வில் ஆஸ்டின் இந்திய அரசியலமைப்பு உருவாக்க செயல்முறையை 'கருத்து ஒருமித்த கருத்து மற்றும் சமரசம்' என்பதற்கு ஒரு சான்றாக அழைத்தார்."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Understand",
        "estimated_time_sec": 60,
        "pyq_similarity": "High",
        "tags": ["Duration Rationale", "Consensus & Accommodation", "Granville Austin"]
    },
    # Q32
    {
        "id": "MIC_M_032",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "Process-Based",
        "question": {
            "en": "Why was the adoption of 'Vande Mataram' as the National Song given equal status with 'Jana Gana Mana' as the National Anthem on January 24, 1950?",
            "ta": "ஜனவரி 24, 1950 அன்று 'வந்தே மாதரம்' தேசியப் பாடலாக ஏற்றுக்கொள்ளப்பட்டது 'ஜன கண மன' தேசிய கீதத்திற்கு இணையான அந்தஸ்திற்கு ஏன் உயர்த்தப்பட்டது?"
        },
        "options": [
            {"id": "A", "en": "To honor its historic role as the inspiring anthem of the Indian National Movement since 1896, while selecting 'Jana Gana Mana' for its orchestral adaptability as the official Anthem.", "ta": "1896 முதல் இந்திய தேசிய இயக்கத்தின் எழுச்சிமிக்க பாடலாக அதன் வரலாற்றுப் பங்கை மதிக்கும் வகையில், அதே வேளையில் இசைக்குழு தழுவலுக்காக 'ஜன கண மன' அதிகாரப்பூர்வ கீதமாகத் தேர்ந்தெடுக்கப்பட்டது."},
            {"id": "B", "en": "Because Vande Mataram was written in Hindi whereas Jana Gana Mana was written in Sanskrit.", "ta": "ஏனெனில் வந்தே மாதரம் இந்தியில் எழுதப்பட்டது, அதே சமயம் ஜன கண மன சமஸ்கிருதத்தில் எழுதப்பட்டது."},
            {"id": "C", "en": "Because the League of Nations mandated that all developing nations must have two distinct anthems.", "ta": "ஏனெனில் அனைத்து வளர்ந்து வரும் நாடுகளும் இரண்டு தனித்தனி கீதங்களைக் கொண்டிருக்க வேண்டும் என்று சர்வதேச சங்கம் கட்டாயப்படுத்தியதால்."},
            {"id": "D", "en": "To fulfill a statutory order issued by the British Privy Council in 1948.", "ta": "1948 இல் பிரிட்டிஷ் பிரிவி கவுன்சில் வெளியிட்ட சட்டப்பூர்வ உத்தரவைப் பூர்த்தி செய்ய."}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Dr. Rajendra Prasad announced in the Assembly on Jan 24, 1950 that 'Jana Gana Mana' is the National Anthem, and 'Vande Mataram', which played a historic part in the struggle for Indian freedom, shall be honored equally and have equal status with it.",
            "ta": "ஜனவரி 24, 1950 அன்று டாக்டர் ராஜேந்திர பிரசாத் அவையில் அறிவித்தார்: 'ஜன கண மன' தேசிய கீதமாகும், மேலும் இந்திய சுதந்திரப் போராட்டத்தில் வரலாற்றுச் சிறப்புமிக்க பங்காற்றிய 'வந்தே மாதரம்' சமமாக சம அந்தஸ்துடன் கௌரவிக்கப்படும்."
        },
        "why_not_others": {
            "A": {"en": "Correct. Historic emotional connection of Vande Mataram to freedom movement granted it equal status.", "ta": "சரி. சுதந்திர இயக்கத்துடன் வந்தே மாதரத்தின் வரலாற்று உணர்ச்சிப்பூர்வமான தொடர்பு அதற்கு சம அந்தஸ்தை வழங்கியது."},
            "B": {"en": "Incorrect. Vande Mataram is in Sanskritized Bengali; Jana Gana Mana in Bengali.", "ta": "தவறு. வந்தே மாதரம் சமஸ்கிருதமயமாக்கப்பட்ட வங்காள மொழியில் உள்ளது; ஜன கண மன வங்காள மொழியில் உள்ளது."},
            "C": {"en": "Incorrect. League of Nations had no anthem guidelines.", "ta": "தவறு. சர்வதேச சங்கத்திற்கு கீத வழிகாட்டுதல்கள் எதுவும் இல்லை."},
            "D": {"en": "Incorrect. Privy Council had no authority over national symbols.", "ta": "தவறு. தேசிய சின்னங்கள் மீது பிரிவி கவுன்சிலுக்கு அதிகாரம் இல்லை."}
        },
        "tnpsc_tip": {
            "en": "President Dr. Rajendra Prasad made a statement in the Assembly regarding Anthem and Song without taking a formal vote.",
            "ta": "குடியரசுத் தலைவர் டாக்டர் ராஜேந்திர பிரசாத் முறைப்படியான வாக்கெடுப்பு நடத்தாமல் கீதம் மற்றும் பாடல் குறித்து அவையில் ஒரு அறிக்கையை வெளியிட்டார்."
        },
        "revision_fact": {
            "en": "Vande Mataram was first sung at the 1896 INC session by Rabindranath Tagore.",
            "ta": "வந்தே மாதரம் முதன்முதலில் 1896 ஐஎன்சி மாநாட்டில் ரவீந்திரநாத் தாகூரால் பாடப்பட்டது."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Understand",
        "estimated_time_sec": 55,
        "pyq_similarity": "High",
        "tags": ["Vande Mataram Status", "Jana Gana Mana", "Jan 24 1950"]
    },
    # Q33
    {
        "id": "MIC_M_033",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "Process-Based",
        "question": {
            "en": "What was the significance of Prem Behari Narain Raizada's role in the physical creation of the original Indian Constitution?",
            "ta": "மூல இந்திய அரசியலமைப்பின் பௌதிக உருவாக்கத்தில் பிரேம் பிஹாரி நரேன் ரைசாதாவின் பங்கின் முக்கியத்துவம் யாது?"
        },
        "options": [
            {"id": "A", "en": "He spent six months handwriting the complete original manuscript of the Constitution in elegant italic calligraphy without taking any remuneration.", "ta": "எந்தவொரு சன்மானமும் பெறாமல், நேர்த்தியான சாய்ந்த கையெழுத்துக் கலையில் முழு மூல அரசியலமைப்பு கையெழுத்துப் பிரதியையும் கைப்பட எழுத அவர் ஆறு மாதங்களைச் செலவிட்டார்."},
            {"id": "B", "en": "He engineered the special helium-filled glass cases used to preserve the manuscript in Parliament Library.", "ta": "நாடாளுமன்ற நூலகத்தில் கையெழுத்துப் பிரதியைப் பாதுகாக்கப் பயன்படும் சிறப்பு ஹீலியம் நிரப்பப்பட்ட கண்ணாடிப் பெட்டிகளை அவர் வடிவமைத்தார்."},
            {"id": "C", "en": "He translated the draft text into Hindi and Urdu versions.", "ta": "வரைவு உரையை இந்தி மற்றும் உருது பதிப்புகளில் அவர் மொழிபெயர்த்தார்."},
            {"id": "D", "en": "He was the chief printer who operated the Government of India Press in Shimla.", "ta": "சிம்லாவில் உள்ள இந்திய அரசு அச்சகத்தை இயக்கிய முதன்மை அச்சுப்பொறியாளர் ஆவார்."}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Prem Behari Narain Raizada was a master calligrapher. When Nehru asked him to write the Constitution, he refused payment, asking only to sign his name on every page and his grandfather's name on the last page. He used 303 pen nibs and parchment paper to write 251 pages.",
            "ta": "பிரேம் பிஹாரி நரேன் ரைசாதா ஒரு மாஸ்டர் கையெழுத்துக் கலைஞர். நேரு அவரை அரசியலமைப்பை எழுதக் கேட்ட போது, அவர் சன்மானம் பெற மறுத்து, ஒவ்வொரு பக்கத்திலும் தனது பெயரையும், கடைசி பக்கத்தில் தனது தாத்தாவின் பெயரையும் எழுத மட்டுமே அனுமதி கோரினார். அவர் 251 பக்கங்களை எழுத 303 பேனா முனைகளையும் தோல்பட்டையையும் பயன்படுத்தினார்."
        },
        "why_not_others": {
            "A": {"en": "Correct. Raizada handwritten the English manuscript in flowing italic style freely.", "ta": "சரி. ரைசாதா ஆங்கிலக் கையெழுத்துப் பிரதியை அழகிய சாய்ந்த பாணியில் இலவசமாக கைப்பட எழுதினார்."},
            "B": {"en": "Incorrect. Preservation helium cases were developed later by National Physical Laboratory.", "ta": "தவறு. பாதுகாப்பு ஹீலியம் பெட்டிகள் பின்னர் தேசிய இயற்பியல் ஆய்வகத்தால் உருவாக்கப்பட்டன."},
            "C": {"en": "Incorrect. Vasant Krishnan Vaidya calligraphed the Hindi version.", "ta": "தவறு. வசந்த் கிரிஷ்ணன் வைத்யா இந்திப் பதிப்பை கையெழுத்தில் எழுதினார்."},
            "D": {"en": "Incorrect. The original manuscript was not commercially printed or typeset.", "ta": "தவறு. மூல கையெழுத்துப் பிரதி வணிக ரீதியாக அச்சிடப்படவில்லை."}
        },
        "tnpsc_tip": {
            "en": "Calligrapher of English Version = Prem Behari Narain Raizada; Calligrapher of Hindi Version = Vasant Krishnan Vaidya.",
            "ta": "ஆங்கிலப் பதிப்பின் கையெழுத்துக் கலைஞர் = பிரேம் பிஹாரி நரேன் ரைசாதா; இந்திப் பதிப்பின் கையெழுத்துக் கலைஞர் = வசந்த் கிரிஷ்ணன் வைத்யா."
        },
        "revision_fact": {
            "en": "Nandalal Bose and Beohar Rammanohar Sinha decorated and illuminated the pages handwritten by Raizada.",
            "ta": "ரைசாதாவால் கைப்பட எழுதப்பட்ட பக்கங்களை நந்தலால் போஸ் மற்றும் பியோஹர் ராம்மனோஹர் சின்ஹா ஆகியோர் சித்திரங்களால் அலங்கரித்தனர்."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Understand",
        "estimated_time_sec": 50,
        "pyq_similarity": "High",
        "tags": ["Calligrapher Prem Behari", "Handwritten Constitution", "Italic Calligraphy"]
    },
    # Q34
    {
        "id": "MIC_M_034",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "Process-Based",
        "question": {
            "en": "What role did Nandalal Bose and artists from Shantiniketan play in the final physical presentation of the Indian Constitution?",
            "ta": "இந்திய அரசியலமைப்பின் இறுதி பௌதிக வெளிப்பாட்டில் நந்தலால் போஸ் மற்றும் சாந்திநிகேதன் கலைஞர்கள் ஆற்றிய பங்கு யாது?"
        },
        "options": [
            {"id": "A", "en": "They decorated and illuminated every page and chapter heading with historic artwork depicting India's heritage from Mohenjo-daro to the Freedom Movement.", "ta": "அவர்கள் மொகஞ்சதாரோ முதல் சுதந்திர இயக்கம் വരையான இந்தியாவின் பாரம்பரியத்தை சித்தரிக்கும் வரலாற்று கலைப்படைப்புகளுடன் ஒவ்வொரு பக்கத்தையும் அத்தியாயத் தலைப்பையும் அலங்கரித்து ஒளிரச்செய்தனர்."},
            {"id": "B", "en": "They sculpted the bronze statue of Ambedkar placed outside Parliament House.", "ta": "நாடாளுமன்ற இல்லத்திற்கு வெளியே வைக்கப்பட்டுள்ள அம்பேத்கரின் வெண்கலச் சிலையை அவர்கள் செதுக்கினர்."},
            {"id": "C", "en": "They designed the ballot papers used in the 1952 general election.", "ta": "1952 பொதுத் தேர்தலில் பயன்படுத்தப்பட்ட வாக்குச் சீட்டுகளை அவர்கள் வடிவமைத்தனர்."},
            {"id": "D", "en": "They built the Constitution Hall where the Assembly held its sessions.", "ta": "அவை தனது அமர்வுகளை நடத்திய அரசியலமைப்பு அரங்கைக் கட்டினார்கள்."}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Nandalal Bose led a team of artists from Kala Bhavana, Shantiniketan (including Beohar Rammanohar Sinha, Kripal Singh Shekhawat). They decorated the margins of all 22 parts of the Constitution with miniature paintings representing Harappan civilization, Vedic era, Ashoka, Gupta age, Cholas, Mughals, and Freedom Struggle.",
            "ta": "சாந்திநிகேதன் கலா பவனத்தைச் சேர்ந்த கலைஞர் குழுவிற்கு நந்தலால் போஸ் தலைமை தாங்கினார் (பியோஹர் ராம்மனோஹர் சின்ஹா உட்பட). சிந்துசமவெளி நாகரிகம், வேத காலம், அசோகர், குப்தர் காலம், சோழர்கள், முகலாயர்கள் மற்றும் சுதந்திரப் போராட்டத்தைப் பிரதிநிதித்துவப்படுத்தும் சித்திர ஓவியங்களால் அரசியலமைப்பின் 22 பாகங்களின் ஓரங்களையும் அவர்கள் அலங்கரித்தனர்."
        },
        "why_not_others": {
            "A": {"en": "Correct. Shantiniketan team under Nandalal Bose created the iconic historic artwork on all 22 parts.", "ta": "சரி. நந்தலால் போஸ் தலைமையிலான சாந்திநிகேதன் குழு 22 பாகங்களிலும் சின்னமான வரலாற்று கலைப்படைப்புகளை உருவாக்கியது."},
            "B": {"en": "Incorrect. Parliament statues were sculpted by other artists decades later.", "ta": "தவறு. நாடாளுமன்றச் சிலைகள் பல தசாப்தங்களுக்குப் பிறகு பிற கலைஞர்களால் செதுக்கப்பட்டன."},
            "C": {"en": "Incorrect. Ballot papers were designed by Election Commission staff.", "ta": "தவறு. வாக்குச் சீட்டுகள் தேர்தல் ஆணைய ஊழியர்களால் வடிவமைக்கப்பட்டன."},
            "D": {"en": "Incorrect. Constitution Hall was built during British rule as part of Parliament House.", "ta": "தவறு. அரசியலமைப்பு அரங்கம் பிரிட்டிஷ் ஆட்சியின் போது நாடாளுமன்றத்தின் ஒரு பகுதியாகக் கட்டப்பட்டது."}
        },
        "tnpsc_tip": {
            "en": "Beohar Rammanohar Sinha specifically illustrated and signed the Preamble page.",
            "ta": "பியோஹர் ராம்மனோஹர் சின்ஹா குறிப்பாக முகப்புரைப் பக்கத்தைச் சித்திரங்களால் அலங்கரித்து கையொப்பமிட்டார்."
        },
        "revision_fact": {
            "en": "The artwork depicts 4000 years of Indian history across the 22 parts of the Constitution.",
            "ta": "ஓவியங்கள் அரசியலமைப்பின் 22 பாகங்களில் 4000 ஆண்டுகால இந்திய வரலாற்றைச் சித்தரிக்கின்றன."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Understand",
        "estimated_time_sec": 55,
        "pyq_similarity": "High",
        "tags": ["Nandalal Bose Artwork", "Shantiniketan Artists", "Manuscript Illumination"]
    },
    # Q35
    {
        "id": "MIC_M_035",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "Conceptual",
        "question": {
            "en": "Why was the Elephant chosen as the official seal and emblem of the Constituent Assembly of India?",
            "ta": "இந்திய அரசியலமைப்பு நிர்ணய அவையின் அதிகாரப்பூர்வ முத்திரையாகவும் சின்னமாகவும் யானை ஏன் தேர்ந்தெடுக்கப்பட்டது?"
        },
        "options": [
            {"id": "A", "en": "It symbolized vastness, strength, wisdom, and the grand diversity of the Indian subcontinent embraced by the Assembly.", "ta": "இது அவையால் தழுவப்பட்ட இந்திய துணைக் கண்டத்தின் பரந்த தன்மை, பலம், ஞானம் மற்றும் பிரமாண்டமான பன்முகத்தன்மையைக் குறியீடாகக் கொண்டிருந்தது."},
            {"id": "B", "en": "Because it was the personal crest of Dr. B.R. Ambedkar's ancestral family.", "ta": "ஏனெனில் இது டாக்டர் பி.ஆர். அம்பேத்கரின் முன்னோர்களின் குடும்ப தனிப்பட்ட சின்னமாகும்."},
            {"id": "C", "en": "Because the British East India Company had used the Elephant on its gold coins since 1600.", "ta": "ஏனெனில் கிழக்கிந்தியக் கம்பெனி 1600 முதல் தனது தங்க நாணயங்களில் யானையைப் பயன்படுத்தியிருந்தது."},
            {"id": "D", "en": "It was mandated by the United Nations as a compulsory symbol for South Asian assemblies.", "ta": "தெற்காசிய அவைகளுக்கான கட்டாயச் சின்னமாக ஐக்கிய நாடுகள் சபையால் இது கட்டாயப்படுத்தப்பட்டது."}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "The Constituent Assembly adopted the Elephant as its official seal. Critics like H.V. Kamath jokingly remarked that the Constitution turned out to be 'elephantine' in size like its seal, but the symbol reflected wisdom, strength, and the massive scale of Indian democracy.",
            "ta": "அரசியலமைப்பு நிர்ணய அவை யானையை தனது அதிகாரப்பூர்வ முத்திரையாக ஏற்றுக்கொண்டது. எச்.வி. காமத் போன்ற விமர்சகர்கள் அரசியலமைப்பு அதன் முத்திரையைப் போலவே அளவிலும் 'யானை அளவு' ஆகிவிட்டது என்று வேடிக்கையாகக் குறிப்பிட்டனர், ஆனால் இச்சின்னம் ஞானம், பலம் மற்றும் இந்திய ஜனநாயகத்தின் பிரமாண்ட அளவைப் பிரதிபலித்தது."
        },
        "why_not_others": {
            "A": {"en": "Correct. Elephant seal reflected strength, wisdom, and subcontinent-wide representation.", "ta": "சரி. யானை முத்திரை பலம், ஞானம் மற்றும் துணைக்கண்டம் தழுவிய பிரதிநிதித்துவத்தைப் பிரதிபலித்தது."},
            "B": {"en": "Incorrect. It was not Ambedkar's family crest.", "ta": "தவறு. இது அம்பேத்கரின் குடும்பச் சின்னம் அல்ல."},
            "C": {"en": "Incorrect. East India Company seal featured lions and a coat of arms.", "ta": "தவறு. கிழக்கிந்தியக் கம்பெனி முத்திரையில் சிங்கங்கள் இருந்தன."},
            "D": {"en": "Incorrect. UN had no involvement in choosing Assembly symbols.", "ta": "தவறு. அவைச் சின்னங்களைத் தேர்ந்தெடுப்பதில் ஐநாவுக்கு எந்தப்ங்கும் இல்லை."}
        },
        "tnpsc_tip": {
            "en": "H.V. Kamath famously commented: 'The emblem and seal that we have chosen for our Assembly is an elephant. It is perhaps fitting that our Constitution, too, is the bulkiest in the world!'",
            "ta": "எச்.வி. காமத் புகழ்பெற்ற முறையில் கருத்துத் தெரிவித்தார்: 'நமது அவைக்கு நாம் தேர்ந்தெடுத்துள்ள சின்னம் மற்றும் முத்திரை ஒரு யானை. நமது அரசியலமைப்பும் உலகில் மிகச் பெரியதாக இருப்பது பொருத்தமானதே!'."
        },
        "revision_fact": {
            "en": "The elephant symbol was used on official documents, letterheads, and publications of the Constituent Assembly.",
            "ta": "யானைச் சின்னம் நிர்ணய அவையின் அதிகாரப்பூர்வ ஆவணங்கள், கடிதத் தலைப்புகள் மற்றும் வெளியீடுகளில் பயன்படுத்தப்பட்டது."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Understand",
        "estimated_time_sec": 50,
        "pyq_similarity": "High",
        "tags": ["Elephant Seal", "Assembly Emblem", "Bulkiest Constitution"]
    },
    # Q36
    {
        "id": "MIC_M_036",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "TNPSC Trap Questions",
        "question": {
            "en": "Which of the following women members of the Constituent Assembly was the ONLY Muslim female member in the Assembly?",
            "ta": "அரசியலமைப்பு நிர்ணய அவையின் பெண் உறுப்பினர்களில் ஒரே ஒரு முஸ்லிம் பெண் உறுப்பினராக இருந்தவர் யார்?"
        },
        "options": [
            {"id": "A", "en": "Begum Aizaz Rasul", "ta": "பேகம் ஐசாஸ் ரசூல்"},
            {"id": "B", "en": "Dakshayani Velayudhan", "ta": "தாக்ஷாயணி வேலாயுதன்"},
            {"id": "C", "en": "Ammu Swaminathan", "ta": "அம்மு சுவாமிநாதன்"},
            {"id": "D", "en": "Renuka Ray", "ta": "ரேணுகா ராய்"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "TRAP QUESTION! Begum Aizaz Rasul was the only Muslim woman member in the Constituent Assembly of India. She played an active role in opposing separate electorates for minorities, arguing that reservation harms minority integration.",
            "ta": "வலைக் கேள்வி! பேகம் ஐசாஸ் ரசூல் இந்திய அரசியலமைப்பு நிர்ணய அவையில் இருந்த ஒரே முஸ்லிம் பெண் உறுப்பினர் ஆவர். சிறுபான்மையினருக்கான தனித் தொகுதிகளை எதிர்ப்பதில் அவர் தீவிர பங்காற்றினார்."
        },
        "why_not_others": {
            "A": {"en": "Correct. Begum Aizaz Rasul was the sole Muslim female member among the 15 women members.", "ta": "சரி. 15 பெண் உறுப்பினர்களில் பேகம் ஐசாஸ் ரசூல் மட்டுமே ஒரே முஸ்லிம் பெண் உறுப்பினர்."},
            "B": {"en": "Incorrect. Dakshayani Velayudhan was the first and only Dalit woman member in the Assembly.", "ta": "தவறு. தாக்ஷாயணி வேலாயுதன் அவையில் இருந்த முதல் மற்றும் ஒரே தலித் பெண் உறுப்பினர்."},
            "C": {"en": "Incorrect. Ammu Swaminathan was a prominent Hindu woman member from Madras.", "ta": "தவறு. அம்மு சுவாமிநாதன் மதராஸைச் சேர்ந்த ஒரு முக்கிய இந்து பெண் உறுப்பினர்."},
            "D": {"en": "Incorrect. Renuka Ray was a prominent woman delegate from West Bengal.", "ta": "தவறு. ரேணுகா ராய் மேற்கு வங்கத்தைச் சேர்ந்த ஒரு முக்கிய பெண் பிரதிநிதி."}
        },
        "tnpsc_tip": {
            "en": "Two Unique Women Members to Remember: Begum Aizaz Rasul (Only Muslim Woman) and Dakshayani Velayudhan (Only Dalit Woman).",
            "ta": "நினைவில் கொள்ள வேண்டிய இரண்டு தனித்துவமான பெண் உறுப்பினர்கள்: பேகம் ஐசாஸ் ரசூல் (ஒரே முஸ்லிம் பெண்) மற்றும் தாக்ஷாயணி வேலாயுதன் (ஒரே தலித் பெண்)."
        },
        "revision_fact": {
            "en": "There were 15 female members in total in the Constituent Assembly of India.",
            "ta": "இந்திய அரசியலமைப்பு நிர்ணய அவையில் மொத்தம் 15 பெண் உறுப்பினர்கள் இருந்தனர்."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Remember",
        "estimated_time_sec": 45,
        "pyq_similarity": "High",
        "tags": ["Begum Aizaz Rasul", "Sole Muslim Female Member", "15 Women Members"]
    },
    # Q37
    {
        "id": "MIC_M_037",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "TNPSC Trap Questions",
        "question": {
            "en": "Which member of the Constituent Assembly holds the distinction of being the FIRST and ONLY Dalit woman elected to the Assembly?",
            "ta": "அரசியலமைப்பு நிர்ணய அவைக்குத் தேர்ந்தெடுக்கப்பட்ட முதல் மற்றும் ஒரே தலித் பெண் உறுப்பினர் என்ற பெருமையைப் பெற்றவர் யார்?"
        },
        "options": [
            {"id": "A", "en": "Dakshayani Velayudhan", "ta": "தாக்ஷாயணி வேலாயுதன்"},
            {"id": "B", "en": "Sucheta Kripalani", "ta": "சுசேதா கிருபளானி"},
            {"id": "C", "en": "Sarojini Naidu", "ta": "சரோஜினி நாயுடு"},
            {"id": "D", "en": "Hansa Mehta", "ta": "ஹன்சா மேத்தா"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Dakshayani Velayudhan (from Madras/Kerala) was the first and only Dalit woman elected to the Constituent Assembly at the age of 34. She spoke strongly against untouchability and forced labor during the debates on Fundamental Rights.",
            "ta": "தாக்ஷாயணி வேலாயுதன் (மதராஸ்/கேரளா) தனது 34 வது வயதில் அரசியலமைப்பு நிர்ணய அவைக்குத் தேர்ந்தெடுக்கப்பட்ட முதல் மற்றும் ஒரே தலித் பெண் உறுப்பினர் ஆவார். அடிப்படை உரிமைகள் மீதான விவாதங்களின் போது தீண்டாமை மற்றும் கொத்தடிமை முறைக்கு எதிராக அவர் கடுமையாகப் பேசினார்."
        },
        "why_not_others": {
            "A": {"en": "Correct. Dakshayani Velayudhan was the sole Dalit female member.", "ta": "சரி. தாக்ஷாயணி வேலாயுதன் மட்டுமே ஒரே தலித் பெண் உறுப்பினர்."},
            "B": {"en": "Incorrect. Sucheta Kripalani was later India's first woman Chief Minister (UP).", "ta": "தவறு. சுசேதா கிருபளானி பின்னர் இந்தியாவின் முதல் பெண் முதலமைச்சரானார் (உபி)."},
            "C": {"en": "Incorrect. Sarojini Naidu was the Nightingale of India and Governor of UP.", "ta": "தவறு. சரோஜினி நாயுடு இந்தியாவின் கானக்குயில் மற்றும் உபி ஆளுநர்."},
            "D": {"en": "Incorrect. Hansa Mehta represented India at the UN Human Rights Commission.", "ta": "தவறு. ஹன்சா மேத்தா ஐநா மனித உரிமைகள் ஆணைக்குழுவில் இந்தியாவைப் பிரதிநிதித்துவப்படுத்தினார்."}
        },
        "tnpsc_tip": {
            "en": "Dakshayani Velayudhan famously declared in the Assembly that the Constitution should not merely abolish untouchability on paper, but provide moral and social remedies.",
            "ta": "அரசியலமைப்பு தீண்டாமையை காகிதத்தில் மட்டும் ஒழிக்காமல், தத்துவார்த்த மற்றும் சமூகப் பரிகாரங்களை வழங்க வேண்டும் என்று தாக்ஷாயணி வேலாயுதன் அவையில் புகழ்பெற்ற முறையில் பிரகடனம் செய்தார்."
        },
        "revision_fact": {
            "en": "Dakshayani Velayudhan was also the youngest female member in the Constituent Assembly.",
            "ta": "தாக்ஷாயணி வேலாயுதன் அரசியலமைப்பு நிர்ணய அவையின் மிக இளைய பெண் உறுப்பினராகவும் இருந்தார்."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Remember",
        "estimated_time_sec": 45,
        "pyq_similarity": "High",
        "tags": ["Dakshayani Velayudhan", "Sole Dalit Female Member", "Untouchability Debate"]
    },
    # Q38
    {
        "id": "MIC_M_038",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "Conceptual",
        "question": {
            "en": "Why was the Constituent Assembly criticized by some political scholars as being 'a one-party body in a one-party country'?",
            "ta": "அரசியலமைப்பு நிர்ணய அவை சில அரசியல் அறிஞர்களால் 'ஒரு கட்சி நாட்டில் ஒரு கட்சி அமைப்பு' என்று ஏன் விமர்சிக்கப்பட்டது?"
        },
        "options": [
            {"id": "A", "en": "Granville Austin noted that the Congress Party dominated the Assembly with over 82% seats after partition, though it accommodated wide internal ideological diversity.", "ta": "பிரிவினைக்குப் பிறகு காங்கிரஸ் கட்சி 82% க்கும் அதிகமான இடங்களுடன் அவையில் ஆதிக்கம் செலுத்தியதாக கான்வில் ஆஸ்டின் குறிப்பிட்டார், இருப்பினும் அது பரந்த உள் தத்துவார்த்த பன்முகத்தன்மையை உள்ளடக்கியிருந்தது."},
            {"id": "B", "en": "Because the British Parliament passed a decree outlawing all political parties except the Indian National Congress in 1946.", "ta": "ஏனெனில் 1946 இல் இந்திய தேசிய காங்கிரஸைத் தவிர அனைத்து அரசியல் கட்சிகளையும் பிரிட்டிஷ் நாடாளுமன்றம் சட்டவிரோதமாக்கியதால்."},
            {"id": "C", "en": "Because Dr. B.R. Ambedkar was the General Secretary of the Congress Party.", "ta": "ஏனெனில் டாக்டர் பி.ஆர். அம்பேத்கர் காங்கிரஸ் கட்சியின் பொதுச் செயலாளராக இருந்ததால்."},
            {"id": "D", "en": "Because non-Congress delegates were physically prevented from entering the Constitution Hall.", "ta": "ஏனெனில் காங்கிரஸ் அல்லாத பிரதிநிதிகள் அரசியலமைப்பு அரங்கிற்குள் நுழைவது பௌதிகமாகத் தடுக்கப்பட்டதால்."}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "British constitutional expert Granville Austin commented: 'The Constituent Assembly was a one-party body in an essentially one-party country. The Assembly was the Congress and the Congress was India.' However, he added that Congress contained diverse factions (Rightists, Leftists, Socialists, Conservatives).",
            "ta": "பிரிட்டிஷ் அரசியலமைப்பு நிபுணர் கான்வில் ஆஸ்டின் குறிப்பிட்டார்: 'நிர்ணய அவை அடிப்படையில் ஒரு கட்சி நாட்டில் ஒரு கட்சி அமைப்பாக இருந்தது. அவை காங்கிரஸாக இருந்தது, காங்கிரஸ் இந்தியாவாக இருந்தது.' இருப்பினும், காங்கிரஸில் பலதரப்பட்ட பிரிவுகள் இருந்தன என்று அவர் மேலும் கூறினார்."
        },
        "why_not_others": {
            "A": {"en": "Correct. Granville Austin's famous observation on Congress dominance post-partition.", "ta": "சரி. பிரிவினைக்குப் பிந்தைய காங்கிரஸ் ஆதிக்கம் குறித்த கான்வில் ஆஸ்டினின் புகழ்பெற்ற கருத்து."},
            "B": {"en": "Incorrect. Other parties existed and contested elections.", "ta": "தவறு. பிற கட்சிகள் இருந்தன மற்றும் தேர்தலில் போட்டியிட்டன."},
            "C": {"en": "Incorrect. Ambedkar belonged to Scheduled Castes Federation, not Congress.", "ta": "தவறு. அம்பேத்கர் பட்டியல் சாதிகள் கூட்டமைப்பைச் சேர்ந்தவர், காங்கிரஸைச் சேர்ந்தவர் அல்ல."},
            "D": {"en": "Incorrect. Non-Congress leaders like Ambedkar, Mookerjee, and Kunzru played leading roles.", "ta": "தவறு. அம்பேத்கர், முகர்ஜி, குன்ஸ்ரு போன்ற காங்கிரஸ் அல்லாத தலைவர்கள் முன்னணிப் பங்காற்றினர்."}
        },
        "tnpsc_tip": {
            "en": "Criticisms of Assembly to remember: 1. Not a representative body, 2. Not a sovereign body (initially), 3. Time-consuming, 4. Congress-dominated, 5. Lawyer-Politician dominated, 6. Hindu-dominated.",
            "ta": "நினைவில் கொள்ள வேண்டிய அவையின் விமர்சனங்கள்: 1. பிரதிநிதித்துவ அமைப்பல்ல, 2. இறையாண்மை அமைப்பல்ல (ஆரம்பத்தில்), 3. அதிக நேரம் எடுத்தது, 4. காங்கிரஸ் ஆதிக்கம், 5. வழக்கறிஞர்-அரசியல்வாதி ஆதிக்கம், 6. இந்து ஆதிக்கம்."
        },
        "revision_fact": {
            "en": "Winston Churchill criticized the Assembly as representing 'only one major community in India'.",
            "ta": "வின்ஸ்டன் சர்ச்சில் அவையை 'இந்தியாவில் உள்ள ஒரு முக்கிய சமூகத்தை மட்டுமே பிரதிநிதித்துவப்படுத்துகிறது' என்று விமர்சித்தார்."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Understand",
        "estimated_time_sec": 60,
        "pyq_similarity": "High",
        "tags": ["Granville Austin Quote", "One Party Criticism", "Assembly Criticism"]
    },
    # Q39
    {
        "id": "MIC_M_039",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "Conceptual",
        "question": {
            "en": "Why was the Constituent Assembly criticized for being a 'Lawyer-Politician Dominated' body, and what was its impact on the Constitution?",
            "ta": "அரசியலமைப்பு நிர்ணய அவை 'வழக்கறிஞர்-அரசியல்வாதி ஆதிக்கம் செலுத்தும்' அமைப்பாக இருந்தது என்று ஏன் விமர்சிக்கப்பட்டது, மேலும் அது அரசியலமைப்பில் என்ன தாக்கத்தை ஏற்படுத்தியது?"
        },
        "options": [
            {"id": "A", "en": "Legal luminaries (like Ambedkar, Alladi, Munshi, Rau) dominated discussions, resulting in an exceptionally detailed, bulky document written in complex legal language.", "ta": "சட்டப் புகழ்பெற்ற ஆளுமைகள் (அம்பேத்கர், அல்லாடி, முன்ஷி, ராவ் போன்றோர்) விவாதங்களில் ஆதிக்கம் செலுத்தினர், இதன் விளைவாக சிக்கலான சட்ட மொழியில் எழுதப்பட்ட விதிவிலக்கான விரிவான, பருமனான ஆவணம் உருவானது."},
            {"id": "B", "en": "Because only practicing advocates holding a Master of Laws degree were permitted to vote in the Assembly.", "ta": "ஏனெனில் சட்ட முதுகலை பட்டம் பெற்ற வழக்கறிஞர்களுக்கு மட்டுமே அவையில் வாக்களிக்க அனுமதி அளிக்கப்பட்டதால்."},
            {"id": "C", "en": "Because the British Bar Council appointed all 299 delegates directly.", "ta": "ஏனெனில் பிரிட்டிஷ் பார் கவுன்சில் அனைத்து 299 பிரதிநிதிகளையும் நேரடியாக நியமித்ததால்."},
            {"id": "D", "en": "It resulted in abolishing the Supreme Court in favor of local arbitration tribunals.", "ta": "இது உள்ளூர் மத்தியஸ்த தீர்ப்பாயங்களுக்கு ஆதரவாக உச்ச நீதிமன்றத்தை ஒழிப்பதற்கு வழிவகுத்தது."}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Critics pointed out that other sections of society (like farmers, workers, industrialists) were insufficiently represented. The dominance of legal experts made the Constitution overly elaborate, rigid, and phrased in complicated 'lawyer's paradise' legal language.",
            "ta": "சமூகத்தின் பிற பிரிவினர் (விவசாயிகள், தொழிலாளர்கள், தொழிலதிபர்கள் போன்றோர்) போதுமான அளவு பிரதிநிதித்துவப்படுத்தப்படவில்லை என்று விமர்சகர்கள் சுட்டிக்காட்டினர். சட்ட நிபுணர்களின் ஆதிக்கம் அரசியலமைப்பை மிகவும் விரிவானதாகவும், விறைப்பானதாகவும், சிக்கலான 'வழக்கறிஞர்களின் சொர்க்கம்' என்ற சட்ட மொழியில் வடிவமைக்கப்பட்டதாகவும் ஆக்கியது."
        },
        "why_not_others": {
            "A": {"en": "Correct. Dominance of legal scholars led to comprehensive detail and legalistic complexity ('Lawyer's Paradise').", "ta": "சரி. சட்ட அறிஞர்களின் ஆதிக்கம் விரிவான விளக்கம் மற்றும் சட்டச் சிக்கலுக்கு வழிவகுத்தது ('வழக்கறிஞர்களின் சொர்க்கம்')."},
            "B": {"en": "Incorrect. No law degree restriction existed for membership.", "ta": "தவறு. உறுப்பினர் பதவிக்கு சட்டப் பட்டக் கட்டுப்பாடு எதுவும் இல்லை."},
            "C": {"en": "Incorrect. British Bar Council had no nomination role.", "ta": "தவறு. பிரிட்டிஷ் பார் கவுன்சிலுக்கு எந்த நியமனப்ங்கும் இல்லை."},
            "D": {"en": "Incorrect. Legal experts actually strengthened the independent Judiciary and Supreme Court.", "ta": "தவறு. சட்ட நிபுணர்கள் உண்மையில் சுயாதீன நீதித்துறை மற்றும் உச்ச நீதிமன்றத்தைப் பலப்படுத்தினர்."}
        },
        "tnpsc_tip": {
            "en": "Sir Ivor Jennings called the Indian Constitution a 'Lawyer's Paradise' due to its legalistic complexity.",
            "ta": "சர் ஐவர் ஜென்னிங்ஸ் இந்திய அரசியலமைப்பை அதன் சட்டச் சிக்கல் காரணமாக 'வழக்கறிஞர்களின் சொர்க்கம்' என்று அழைத்தார்."
        },
        "revision_fact": {
            "en": "Sir Ivor Jennings also described the Indian Constitution as the longest and most detailed constitution in the world.",
            "ta": "சர் ஐவர் ஜென்னிங்ஸ் இந்திய அரசியலமைப்பை உலகின் மிக நீண்ட மற்றும் விரிவான அரசியலமைப்பு என்றும் விவரித்தார்."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Understand",
        "estimated_time_sec": 55,
        "pyq_similarity": "High",
        "tags": ["Lawyers Paradise", "Ivor Jennings Quote", "Legalistic Complexity"]
    },
    # Q40
    {
        "id": "MIC_M_040",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "Process-Based",
        "question": {
            "en": "What was the significance of the debate over whether to include the word 'God' in the Preamble of the Indian Constitution?",
            "ta": "இந்திய அரசியலமைப்பின் முகப்புரையில் 'கடவுள்' என்ற வார்த்தையைச் சேர்க்க வேண்டுமா என்பது குறித்த விவாதத்தின் முக்கியத்துவம் யாது?"
        },
        "options": [
            {"id": "A", "en": "An amendment to introduce 'In the name of God' was defeated by a vote in the Assembly to preserve the secular, inclusive character of the sovereign Republic.", "ta": "இறையாண்மை கொண்ட குடியரசின் மதச்சார்பற்ற, அனைவரையும் உள்ளடக்கிய தன்மையைப் பாதுகாக்க 'கடவுளின் பெயரால்' என்ற திருத்தம் அவையில் வாக்கெடுப்பு மூலம் தோற்கடிக்கப்பட்டது."},
            {"id": "B", "en": "The proposal was accepted unanimously and added to the first line of the Preamble.", "ta": "இமுன்மொழிவு ஒருமனதாக ஏற்றுக்கொள்ளப்பட்டு முகப்புரையின் முதல் வரியில் சேர்க்கப்பட்டது."},
            {"id": "C", "en": "The Assembly decided to replace 'We the People' with 'We the Religious Believers'.", "ta": "'இந்திய மக்களாகிய நாம்' என்பதற்குப் பதிலாக 'மத நம்பிக்கையாளர்களாகிய நாம்' என்று மாற்ற அவை முடிவெடுத்தது."},
            {"id": "D", "en": "The British Crown vetoed any preamble that did not mention the Church of England.", "ta": "இங்கிலாந்து திருச்சபையைக் குறிப்பிடாத எந்தவொரு முகப்புரையையும் பிரிட்டிஷ் அரசு வீட்டோ செய்தது."}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Member H.V. Kamath moved an amendment to insert 'In the name of God' at the beginning of the Preamble. Other members (like Hriday Nath Kunzru) argued that invoking God would be unfair to non-believers and atheists in a secular nation. The amendment was put to vote and defeated (68 against, 41 in favor).",
            "ta": "உறுப்பினர் எச்.வி. காமத் முகப்புரையின் தொடக்கத்தில் 'கடவுளின் பெயரால்' என்பதைச் சேர்க்க திருத்தத்தைக் கொண்டு வந்தார். மற்ற உறுப்பினர்கள் (ஹ்ரிதய நாத் குன்ஸ்ரு போன்றோர்) கடவுளைக் குறிப்பிடுவது மதச்சார்பற்ற நாட்டில் நம்பிக்கையற்றவர்களுக்கும் நாத்திகர்களுக்கும் அநீதியானது என்று வாதிட்டனர். இத்திருத்தம் வாக்கெடுப்பிற்கு விடப்பட்டு தோற்கடிக்கப்பட்டது (எதிராக 68, ஆதரவாக 41)."
        },
        "why_not_others": {
            "A": {"en": "Correct. Voting down the inclusion of 'God' preserved neutrality for believers and non-believers alike.", "ta": "சரி. 'கடவுள்' என்பதைச் சேர்ப்பதை வாக்களித்துத் தோற்கடித்தது நம்பிக்கையாளர்கள் மற்றும் நம்பிக்கையற்றவர்கள் இருவருக்கும் நடுநிலைமையைப் பாதுகாத்தது."},
            "B": {"en": "Incorrect. It was put to vote and defeated.", "ta": "தவறு. இது வாக்கெடுப்பிற்கு விடப்பட்டு தோற்கடிக்கப்பட்டது."},
            "C": {"en": "Incorrect. 'We the People' was retained as the opening phrase.", "ta": "தவறு. 'இந்திய மக்களாகிய நாம்' என்பது தொடக்கச் சொற்றொடராகத் தக்கவைக்கப்பட்டது."},
            "D": {"en": "Incorrect. British Crown had no veto over the Preamble.", "ta": "தவறு. முகப்புரை மீது பிரிட்டிஷ் அரசிற்கு எந்த வீட்டோவும் இல்லை."}
        },
        "tnpsc_tip": {
            "en": "H.N. Kunzru observed: 'We should not bring in the name of God in a matter which relies on collective human sovereign will.'",
            "ta": "எச்.என். குன்ஸ்ரு குறிப்பிட்டார்: 'கூட்டு மனித இறையாண்மை விருப்பத்தைச் சார்ந்திருக்கும் ஒரு விஷயத்தில் கடவுளின் பெயரைக் கொண்டுவரக்கூடாது.'."
        },
        "revision_fact": {
            "en": "The Preamble begins with the solemn words: 'WE, THE PEOPLE OF INDIA...'.",
            "ta": "முகப்புரை 'இந்திய மக்களாகிய நாம்...' என்ற கம்பீரமான சொற்களுடன் தொடங்குகிறது."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Understand",
        "estimated_time_sec": 55,
        "pyq_similarity": "High",
        "tags": ["God in Preamble Debate", "Secular Principle", "Kamath Amendment Defeated"]
    },
    # Q41
    {
        "id": "MIC_M_041",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "Basic Statement Model",
        "question": {
            "en": "Consider the following statements regarding the role of S.N. Mukherjee in the Constituent Assembly:\n1. He served as the Chief Draftsman of the Constitution in the Assembly.\n2. Dr. B.R. Ambedkar praised his ability to put complex legal propositions in the simplest legal form.\n3. He was elected as the permanent Legal Adviser to the Assembly after B.N. Rau's resignation.\n\nWhich of the statements given above is/are correct?",
            "ta": "அரசியலமைப்பு நிர்ணய அவையில் எஸ்.என். முகர்ஜியின் பங்கு பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. அவர் அவையில் அரசியலமைப்பின் முதன்மை வரைவாளராகச் (Chief Draftsman) பணியாற்றினார்.\n2. சிக்கலான சட்ட முன்மொழிவுகளை எளிய சட்ட வடிவத்தில் வைக்கும் அவரது திறனை டாக்டர் பி.ஆர். அம்பேத்கர் பாராட்டினார்.\n3. பி.என். ராவின் ராஜினாமாவுக்குப் பிறகு அவையின் நிரந்தர சட்ட ஆலோசகராக அவர் தேர்ந்தெடுக்கப்பட்டார்.\n\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 and 2 only", "ta": "1 மற்றும் 2 மட்டுமே"},
            {"id": "B", "en": "2 and 3 only", "ta": "2 மற்றும் 3 மட்டுமே"},
            {"id": "C", "en": "1 and 3 only", "ta": "1 மற்றும் 3 மட்டுமே"},
            {"id": "D", "en": "1, 2, and 3", "ta": "1, 2 மற்றும் 3"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Statements 1 and 2 are correct. S.N. Mukherjee was the Chief Draftsman. Dr. Ambedkar paid high tribute to Mukherjee's drafting skill in his closing speech on Nov 25, 1949. Statement 3 is incorrect because B.N. Rau never resigned, and Rau was Constitutional Adviser while Mukherjee was Chief Draftsman.",
            "ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. எஸ்.என். முகர்ஜி முதன்மை வரைவாளராக இருந்தார். நவம்பர் 25, 1949 இல் தனது நிறைவு உரையில் முகர்ஜியின் வரைவுத் திறனுக்கு அம்பேத்கர் உயர் அஞ்சலி செலுத்தினார். பி.என். ராவ் ஒருபோதும் ராஜினாமா செய்யவில்லை என்பதால் கூற்று 3 தவறானது."
        },
        "why_not_others": {
            "A": {"en": "Correct. Statements 1 and 2 are true; 3 is false.", "ta": "சரி. கூற்றுகள் 1 மற்றும் 2 உண்மையானவை; 3 தவறானது."},
            "B": {"en": "Incorrect. Statement 3 is false.", "ta": "தவறு. கூற்று 3 தவறானது."},
            "C": {"en": "Incorrect. Statement 3 is false.", "ta": "தவறு. கூற்று 3 தவறானது."},
            "D": {"en": "Incorrect. Statement 3 is false.", "ta": "தவறு. கூற்று 3 தவறானது."}
        },
        "tnpsc_tip": {
            "en": "Ambedkar's quote on Mukherjee: 'Without his help, drafting would have taken far longer than it did.'",
            "ta": "முகர்ஜி பற்றிய அம்பேத்கரின் கூற்று: 'அவரது உதவியின்றி, வரைவுப் பணி நடந்ததை விட அதிக நேரம் எடுத்திருக்கும்.'."
        },
        "revision_fact": {
            "en": "H.V.R. Iengar was the Secretary to the Constituent Assembly.",
            "ta": "எச்.வி.ஆர். ஐயங்கார் அரசியலமைப்பு நிர்ணய அவையின் செயலாளராக இருந்தார்."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Understand",
        "estimated_time_sec": 55,
        "pyq_similarity": "High",
        "tags": ["S.N. Mukherjee", "Chief Draftsman", "Ambedkar Tribute"]
    },
    # Q42
    {
        "id": "MIC_M_042",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "Process-Based",
        "question": {
            "en": "What was the significance of Dr. B.R. Ambedkar's famous final speech in the Constituent Assembly on November 25, 1949?",
            "ta": "நவம்பர் 25, 1949 அன்று அரசியலமைப்பு நிர்ணய அவையில் டாக்டர் பி.ஆர். அம்பேத்கர் ஆற்றிய புகழ்பெற்ற நிறைவு உரையின் முக்கியத்துவம் யாது?"
        },
        "options": [
            {"id": "A", "en": "He warned against 'Grammar of Anarchy' (unconstitutional street protests), hero-worship (bhakti) in politics, and emphasized the need to achieve social and economic democracy alongside political equality.", "ta": "அவர் 'அராஜகத்தின் இலக்கணம்' (அரசியலமைப்பிற்கு எதிரான தெருப் போராட்டங்கள்), அரசியலில் தனிநபர் வழிபாடு (பக்தி) ஆகியவற்றுக்கு எதிராக எச்சரித்தார், மேலும் அரசியல் சமத்துவத்துடன் சமூக மற்றும் பொருளாதார ஜனநாயகத்தை அடைய வேண்டியதன் அவசியத்தை வலியுறுத்தினார்."},
            {"id": "B", "en": "He proposed dissolving the Union of States and returning all power to the British Crown.", "ta": "அவர் மாநிலங்களின் ஒன்றியத்தைக் கலைத்து அனைத்து அதிகாரங்களையும் பிரிட்டிஷ் அரசிற்குத் திரும்ப வழங்க முன்மொழிந்தார்."},
            {"id": "C", "en": "He announced that the Constitution would be scrapped and rewritten every 10 years.", "ta": "அரசியலமைப்பு ஒவ்வொரு 10 ஆண்டுகளுக்கும் ரத்து செய்யப்பட்டு மீண்டும் எழுதப்படும் என்று அவர் அறிவித்தார்."},
            {"id": "D", "en": "He resigned from his post as Law Minister in protest against the adoption of the Preamble.", "ta": "முகப்புரையை ஏற்றுக்கொண்டதற்கு எதிர்ப்பு தெரிவித்து சட்ட அமைச்சர் பதவியை அவர் ராஜினாமா செய்தார்."}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "In his historic closing address, Ambedkar highlighted three warnings for preserving democracy: 1) Abandon unconstitutional methods (Grammar of Anarchy), 2) Beware of Bhakti/Hero-worship in politics (which leads to dictatorship), 3) Remove social and economic inequality ('We are going to enter a life of contradictions').",
            "ta": "தனது வரலாற்றுச் சிறப்புமிக்க நிறைவு உரையில், ஜனநாயகத்தைப் பாதுகாப்பதற்கான மூன்று எச்சரிக்கைகளை அம்பேத்கர் சுட்டிக்காட்டினார்: 1) அரசியலமைப்பிற்கு அப்பாற்பட்ட முறைகளைக் கைவிடுங்கள் (அராஜகத்தின் இலக்கணம்), 2) அரசியலில் பக்தி/தனிநபர் வழிபாட்டில் எச்சரிக்கையாக இருங்கள் (இது சர்வாதிகாரத்திற்கு வழிவகுக்கும்), 3) சமூக மற்றும் பொருளாதார சமத்துவமின்மையை நீக்குங்கள் ('நாம் முரண்பாடுகள் நிறைந்த வாழ்க்கையில் நுழையப் போகிறோம்')."
        },
        "why_not_others": {
            "A": {"en": "Correct. Ambedkar's warnings on Grammar of Anarchy, Bhakti in politics, and contradiction between political vs social equality.", "ta": "சரி. அராஜகத்தின் இலக்கணம், அரசியலில் பக்தி, அரசியல் மற்றும் சமூக சமத்துவத்திற்கு இடையிலான முரண்பாடு குறித்த அம்பேத்கரின் எச்சரிக்கைகள்."},
            "B": {"en": "Incorrect. Ambedkar was a passionate champion of Indian sovereignty.", "ta": "தவறு. அம்பேத்கர் இந்திய இறையாண்மையின் தீவிர ஆதரவாளராக இருந்தார்."},
            "C": {"en": "Incorrect. He laid down Article 368 for orderly constitutional amendment.", "ta": "தவறு. ஒழுங்கான அரசியலமைப்புத் திருத்தத்திற்கு அவர் சரத்து 368 ஐ வகுத்தார்."},
            "D": {"en": "Incorrect. Ambedkar resigned later in 1951 over the Hindu Code Bill, not Preamble adoption.", "ta": "தவறு. அம்பேத்கர் பின்னர் 1951 இல் இந்து குறியீட்டு மசோதா தொடர்பாக ராஜினாமா செய்தார், முகப்புரை ஏற்பின் போது அல்ல."}
        },
        "tnpsc_tip": {
            "en": "Famous Quote: 'On 26th January 1950, we are going to enter into a life of contradictions. In politics we will have equality and in social and economic life we will have inequality.'",
            "ta": "புகழ்பெற்ற கூற்று: 'ஜனவரி 26, 1950 அன்று, நாம் முரண்பாடுகள் நிறைந்த வாழ்க்கையில் நுழையப் போகிறோம். அரசியலில் நமக்கு சமத்துவம் இருக்கும், சமூக மற்றும் பொருளாதார வாழ்க்கையில் சமத்துவமின்மை இருக்கும்.'."
        },
        "revision_fact": {
            "en": "This speech delivered on Nov 25, 1949 is widely considered one of the greatest constitutional speeches in world history.",
            "ta": "நவம்பர் 25, 1949 இல் ஆற்றப்பட்ட இந்த உரை உலக வரலாற்றிலேயே மிகச்சிறந்த அரசியலமைப்பு உரைகளில் ஒன்றாக பரவலாகக் கருதப்படுகிறது."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Understand",
        "estimated_time_sec": 60,
        "pyq_similarity": "High",
        "tags": ["Ambedkar Final Speech", "Grammar of Anarchy", "Bhakti in Politics"]
    },
    # Q43
    {
        "id": "MIC_M_043",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "TNPSC Trap Questions",
        "question": {
            "en": "Which of the following constitutional provisions was adopted by the Constituent Assembly WITHOUT any debate or disagreement among members?",
            "ta": "பின்வரும் அரசியலமைப்பு விதிகளில் எது உறுப்பினர்களிடையே எந்தவொரு விவாதமும் அல்லது கருத்து வேறுபாடும் இன்றி அரசியலமைப்பு நிர்ணய அவையால் ஏற்றுக்கொள்ளப்பட்டது?"
        },
        "options": [
            {"id": "A", "en": "Introduction of Universal Adult Suffrage (granting right to vote to all adult citizens)", "ta": "உலகளாவிய வயதுவந்தோர் வாக்குரிமையை அறிமுகப்படுத்துதல் (அனைத்து வயதுவந்த குடிமக்களுக்கும் வாக்களிக்கும் உரிமை வழங்குதல்)"},
            {"id": "B", "en": "Directive Principles of State Policy under Part IV", "ta": "பகுதி IV இன் கீழ் உள்ள அரசு வழிகாட்டு நெறிமுறைகள்"},
            {"id": "C", "en": "Emergency Provisions under Articles 352-360", "ta": "சரத்துகள் 352-360 இன் கீழ் உள்ள அவசரநிலை விதிகள்"},
            {"id": "D", "en": "Official Language of the Union under Part XVII", "ta": "பகுதி XVII இன் கீழ் உள்ள ஒன்றியத்தின் அதிகாரப்பூர்வ மொழி"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "TRAP QUESTION! Almost every provision was hotly debated, EXCEPT Universal Adult Suffrage. The grant of voting rights to every citizen above 21 years (later reduced to 18) regardless of gender, caste, education, or wealth was adopted with complete unanimity and enthusiasm.",
            "ta": "வலைக் கேள்வி! உலகளாவிய வயதுவந்தோர் வாக்குரிமையைத் தவிர மற்ற அனைத்து விதிகளும் சூடாக விவாதிக்கப்பட்டன. பாலினம், சாதி, கல்வி அல்லது செல்வம் பொருட்படுத்தாமல் 21 வயதிற்கு மேற்பட்ட அனைத்து குடிமக்களுக்கும் (பின்னர் 18 ஆகக் குறைக்கப்பட்டது) வாக்களிக்கும் உரிமை வழங்குவது முழு ஒருமனதான ஆதரவுடனும் உற்சாகத்துடனும் ஏற்றுக்கொள்ளப்பட்டது."
        },
        "why_not_others": {
            "A": {"en": "Correct (Unanimously adopted without debate). Universal Adult Suffrage was accepted without a single dissenting voice.", "ta": "சரி (விவாதமின்றி ஒருமனதாக ஏற்கப்பட்டது). உலகளாவிய வயதுவந்தோர் வாக்குரிமை ஒரு எதிர்ப்புக் குரலும் இன்றி ஏற்றுக்கொள்ளப்பட்டது."},
            "B": {"en": "Incorrect. DPSP was fiercely debated (justiciable vs non-justiciable).", "ta": "தவறு. DPSP கடுமையாக விவாதிக்கப்பட்டது (செயலாக்கப்படக்கூடியவை vs செயலாக்கப்பட முடியாதவை)."},
            "C": {"en": "Incorrect. Emergency provisions sparked passionate debate.", "ta": "தவறு. அவசரநிலை விதிகள் உணர்ச்சிப்பூர்வமான விவாதத்தைத் தூண்டின."},
            "D": {"en": "Incorrect. Language debate almost split the Assembly.", "ta": "தவறு. மொழி விவாதம் அவையை ஏறக்குறைய பிளவுபடுத்தியது."}
        },
        "tnpsc_tip": {
            "en": "Alladi Krishnaswamy Ayyar remarked: 'The Assembly adopted adult franchise with an abundant faith in the common man and the ultimate success of democratic rule.'",
            "ta": "அல்லாடி கிருஷ்ணசுவாமி அய்யர் குறிப்பிட்டார்: 'சாதாரண மனிதன் மீதும் ஜனநாயக ஆட்சியின் இறுதி வெற்றியின் மீதும் மிகுந்த நம்பிக்கையுடன் அவை வயதுவந்தோர் வாக்குரிமையை ஏற்றுக்கொண்டது.'."
        },
        "revision_fact": {
            "en": "Voting age was reduced from 21 to 18 years by the 61st Constitutional Amendment Act of 1988.",
            "ta": "வாக்களிக்கும் வயது 1988 ஆம் ஆண்டின் 61 வது அரசியலமைப்புத் திருத்தச் சட்டத்தின் மூலம் 21 லிருந்து 18 ஆகக் குறைக்கப்பட்டது."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Understand",
        "estimated_time_sec": 50,
        "pyq_similarity": "High",
        "tags": ["Universal Adult Suffrage", "No Debate Provision", "TNPSC Trap"]
    },
    # Q44
    {
        "id": "MIC_M_044",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "Basic Statement Model",
        "question": {
            "en": "Consider the following statements regarding the adoption and signing of the Constitution:\n1. The Constitution was adopted on November 26, 1949.\n2. On November 26, 1949, exactly 284 members out of 299 were present and signed the official copy.\n3. The Preamble was adopted BEFORE all other parts of the Constitution were passed.\n\nWhich of the statements given above are correct?",
            "ta": "அரசியலமைப்பு ஏற்பு மற்றும் கையொப்பமிடுதல் பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. அரசியலமைப்பு நவம்பர் 26, 1949 அன்று ஏற்றுக்கொள்ளப்பட்டது.\n2. நவம்பர் 26, 1949 அன்று, 299 உறுப்பினர்களில் சரியாக 284 உறுப்பினர்கள் நேரில் கலந்து கொண்டு அதிகாரப்பூர்வ பிரதியில் கையொப்பமிட்டனர்.\n3. அரசியலமைப்பின் பிற அனைத்து பகுதிகளும் நிறைவேறுவதற்கு முன்பே முகப்புரை ஏற்றுக்கொள்ளப்பட்டது.\n\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 and 2 only", "ta": "1 மற்றும் 2 மட்டுமே"},
            {"id": "B", "en": "2 and 3 only", "ta": "2 மற்றும் 3 மட்டுமே"},
            {"id": "C", "en": "1 and 3 only", "ta": "1 மற்றும் 3 மட்டுமே"},
            {"id": "D", "en": "1, 2, and 3", "ta": "1, 2 மற்றும் 3"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Statements 1 and 2 are correct. Statement 3 is INCORRECT because the Preamble was enacted AFTER the entire Constitution was already passed, to ensure that it was in full conformity with the rest of the Constitution.",
            "ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. முழு அரசியலமைப்பும் ஏற்கனவே நிறைவேற்றப்பட்ட பிறகே முகப்புரை இயற்றப்பட்டது என்பதால் கூற்று 3 தவறானது. இது அரசியலமைப்பின் எஞ்சிய பகுதியுடன் முழுமையாக இணங்குவதை உறுதி செய்யவே இவ்வாறு செய்யப்பட்டது."
        },
        "why_not_others": {
            "A": {"en": "Correct. Statements 1 and 2 are true; 3 is false.", "ta": "சரி. கூற்றுகள் 1 மற்றும் 2 உண்மையானவை; 3 தவறானது."},
            "B": {"en": "Incorrect. Statement 3 is false.", "ta": "தவறு. கூற்று 3 தவறானது."},
            "C": {"en": "Incorrect. Statement 3 is false.", "ta": "தவறு. கூற்று 3 தவறானது."},
            "D": {"en": "Incorrect. Statement 3 is false.", "ta": "தவறு. கூற்று 3 தவறானது."}
        },
        "tnpsc_tip": {
            "en": "Classic Procedural Trap: The Preamble was voted upon and enacted LAST in the Assembly order of business.",
            "ta": "உன்னதமான வழிமுறை வலை: அவையின் வர்த்தக வரிசையில் முகப்புரை இறுதியாக வாக்கெடுப்பிற்கு விடப்பட்டு இயற்றப்பட்டது."
        },
        "revision_fact": {
            "en": "The motion on the Draft Constitution was passed on November 26, 1949.",
            "ta": "வரைவு அரசியலமைப்பு மீதான தீர்மானம் நவம்பர் 26, 1949 அன்று நிறைவேற்றப்பட்டது."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Understand",
        "estimated_time_sec": 55,
        "pyq_similarity": "High",
        "tags": ["Preamble Enactment Order", "284 Members Signing", "Nov 26 1949"]
    },
    # Q45
    {
        "id": "MIC_M_045",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "Conceptual",
        "question": {
            "en": "Why did Naziruddin Ahmad, a member of the Constituent Assembly, mockingly call the Drafting Committee a 'Drifting Committee'?",
            "ta": "அரசியலமைப்பு நிர்ணய அவையின் உறுப்பினரான நசிருதீன் அகமது வரைவுக் குழுவை 'மிதக்கும் குழு' (Drifting Committee) என்று ஏன் கேலியாக அழைத்தார்?"
        },
        "options": [
            {"id": "A", "en": "He was criticizing the prolonged time taken by the Drafting Committee and frequent postponements of draft discussions.", "ta": "வரைவுக் குழு எடுத்துக்கொண்ட நீண்ட காலம் மற்றும் வரைவு விவாதங்களின் அடிக்கடி தள்ளிவைப்புகளை அவர் விமர்சித்தார்."},
            {"id": "B", "en": "Because the Drafting Committee held its meetings on a moving river ship on the Ganges.", "ta": "ஏனெனில் வரைவுக் குழு தனது கூட்டங்களை கங்கையில் இயங்கும் நகரும் நதிக் கப்பலில் நடத்தியதால்."},
            {"id": "C", "en": "Because all seven members of the Drafting Committee resigned simultaneously in 1948.", "ta": "ஏனெனில் வரைவுக் குழுவின் ஏழு உறுப்பினர்களும் 1948 இல் ஒரே நேரத்தில் ராஜினாமா செய்ததால்."},
            {"id": "D", "en": "Because the committee failed to draft any provisions regarding maritime boundary rights.", "ta": "ஏனெனில் கடல் எல்லை உரிமைகள் தொடர்பான எந்தவொரு விதிகளையும் வரைவதில் குழு தோல்வியடைந்ததால்."}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Naziruddin Ahmad coined the term 'Drifting Committee' to accuse Ambedkar's committee of delaying the process. In response, Dr. Ambedkar defended the timeframe by comparing India's detailed constitution-making with the US (which took 4 months for a short text) and Australia (which took 9 years).",
            "ta": "செயல்முறையைத் தாமதப்படுத்துவதாக அம்பேத்கரின் குழு மீது குற்றம் சாட்ட நசிருதீன் அகமது 'மிதக்கும் குழு' என்ற சொல்லை உருவாக்கினார். பதிலுக்கு, அமெரிக்கா (குறுகிய உரைக்கு 4 மாதங்கள் எடுத்தது) மற்றும் ஆஸ்திரேலியாவுடன் (9 ஆண்டுகள் எடுத்தது) இந்தியாவின் விரிவான அரசியலமைப்பு உருவாக்கத்தை ஒப்பிட்டு அம்பேத்கர் நேரத்தைக் கட்டுப்படுத்தியதை நியாயப்படுத்தினார்."
        },
        "why_not_others": {
            "A": {"en": "Correct. Criticism of delay led to Naziruddin Ahmad's 'Drifting Committee' coinage.", "ta": "சரி. தாமதம் பற்றிய விமர்சனம் நசிருதீன் அகமதுவின் 'மிதக்கும் குழு' நாணயத்திற்கு வழிவகுத்தது."},
            "B": {"en": "Incorrect. Meetings were held in Constitution Hall, New Delhi.", "ta": "தவறு. கூட்டங்கள் புதுடெல்லியிலுள்ள அரசியலமைப்பு அரங்கில் நடைபெற்றன."},
            "C": {"en": "Incorrect. Members did not resign simultaneously.", "ta": "தவறு. உறுப்பினர்கள் ஒரே நேரத்தில் ராஜினாமா செய்யவில்லை."},
            "D": {"en": "Incorrect. Maritime provisions were duly included in List I.", "ta": "தவறு. கடல்சார் விதிகள் பட்டியல் I இல் முறையாக சேர்க்கப்பட்டன."}
        },
        "tnpsc_tip": {
            "en": "Ambedkar pointed out that the American Constitution contained only 7 articles and took 4 months, whereas India's Constitution contained 395 articles dealing with a vast country.",
            "ta": "அமெரிக்க அரசியலமைப்பு 7 சரத்துகளை மட்டுமே கொண்டு 4 மாதங்கள் எடுத்தது, அதே சமயம் இந்தியாவின் அரசியலமைப்பு ஒரு பரந்த நாட்டைக் கையாளும் 395 சரத்துகளைக் கொண்டிருந்தது என்று அம்பேத்கர் சுட்டிக்காட்டினார்."
        },
        "revision_fact": {
            "en": "The Drafting Committee actually spent only 141 days in sittings out of the total duration.",
            "ta": "வரைவுக் குழு மொத்த காலத்தில் 141 நாட்கள் மட்டுமே அமர்வுகளில் செலவிட்டது."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Understand",
        "estimated_time_sec": 55,
        "pyq_similarity": "High",
        "tags": ["Drifting Committee Criticism", "Naziruddin Ahmad", "Ambedkar Defense"]
    },
    # Q46
    {
        "id": "MIC_M_046",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "TNPSC Trap Questions",
        "question": {
            "en": "Who among the following was the Chairman of the Order of Business Committee of the Constituent Assembly?",
            "ta": "அரசியலமைப்பு நிர்ணய அவையின் வர்த்தக ஒழுங்குமுறைக் குழுவின் (Order of Business Committee) தலைவராக இருந்தவர் யார்?"
        },
        "options": [
            {"id": "A", "en": "Dr. K.M. Munshi", "ta": "டாக்டர் கே.எம். முன்ஷி"},
            {"id": "B", "en": "Dr. B.R. Ambedkar", "ta": "டாக்டர் பி.ஆர். அம்பேத்கர்"},
            {"id": "C", "en": "Jawaharlal Nehru", "ta": "ஜவஹர்லால் நேரு"},
            {"id": "D", "en": "G.V. Mavlankar", "ta": "ஜி.வி. மாவலங்கர்"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "TRAP QUESTION! Dr. K.M. Munshi was the Chairman of the Order of Business Committee. People often confuse him with G.V. Mavlankar (who chaired Committee on Functions of Constituent Assembly) or Rajendra Prasad (Steering Committee).",
            "ta": "வலைக் கேள்வி! டாக்டர் கே.எம். முன்ஷி வர்த்தக ஒழுங்குமுறைக் குழுவின் தலைவராக இருந்தார். மக்கள் பெரும்பாலும் அவரை ஜி.வி. மாவலங்கர் (செயல்பாடுகள் குழுத் தலைவர்) அல்லது ராஜேந்திர பிரசாத் (வழிகாட்டும் குழு) ஆகியோருடன் குழப்பிக் கொள்கிறார்கள்."
        },
        "why_not_others": {
            "A": {"en": "Correct. K.M. Munshi chaired Order of Business Committee.", "ta": "சரி. கே.எம். முன்ஷி வர்த்தக ஒழுங்குமுறைக் குழுவின் தலைவர்."},
            "B": {"en": "Incorrect. Ambedkar chaired Drafting Committee.", "ta": "தவறு. அம்பேத்கர் வரைவுக் குழுவின் தலைவர்."},
            "C": {"en": "Incorrect. Nehru chaired Union Powers & Union Constitution Committees.", "ta": "தவறு. நேரு மத்திய அதிகாரங்கள் & மத்திய அரசியலமைப்புச் சாசனக் குழுக்களின் தலைவர்."},
            "D": {"en": "Incorrect. G.V. Mavlankar chaired Committee on Functions of Constituent Assembly.", "ta": "தவறு. ஜி.வி. மாவலங்கர் நிர்ணய அவையின் செயல்பாடுகள் குழுவின் தலைவர்."}
        },
        "tnpsc_tip": {
            "en": "Distinguish: Order of Business Committee -> K.M. Munshi; Steering Committee -> Dr. Rajendra Prasad; Functions of Assembly Committee -> G.V. Mavlankar.",
            "ta": "வேறுபடுத்துக: வர்த்தக ஒழுங்குமுறைக் குழு -> கே.எம். முன்ஷி; வழிகாட்டும் குழு -> டாக்டர் ராஜேந்திர பிரசாத்; அவையின் செயல்பாடுகள் குழு -> ஜி.வி. மாவலங்கர்."
        },
        "revision_fact": {
            "en": "K.M. Munshi was also a key member of the Drafting Committee.",
            "ta": "கே.எம். முன்ஷி வரைவுக் குழுவின் முக்கிய உறுப்பினராகவும் இருந்தார்."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Remember",
        "estimated_time_sec": 45,
        "pyq_similarity": "High",
        "tags": ["Order of Business Committee", "K.M. Munshi", "Committee Trap"]
    },
    # Q47
    {
        "id": "MIC_M_047",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "TNPSC Trap Questions",
        "question": {
            "en": "Who chaired the Ad hoc Committee on the National Flag set up by the Constituent Assembly on June 23, 1947?",
            "ta": "ஜூன் 23, 1947 அன்று அரசியலமைப்பு நிர்ணய அவையால் அமைக்கப்பட்ட தேசியக் கொடிக்கான தற்காலிகக் குழுவிற்கு (Ad hoc Committee on National Flag) தலைமை தாங்கியவர் யார்?"
        },
        "options": [
            {"id": "A", "en": "Dr. Rajendra Prasad", "ta": "டாக்டர் ராஜேந்திர பிரசாத்"},
            {"id": "B", "en": "J.B. Kripalani", "ta": "ஜே.பி. கிருபளானி"},
            {"id": "C", "en": "Jawaharlal Nehru", "ta": "ஜவஹர்லால் நேரு"},
            {"id": "D", "en": "C. Rajagopalachari", "ta": "சி. ராஜகோபாலாச்சாரி"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "MAJOR TRAP QUESTION! The official Ad hoc Committee on National Flag was chaired by Dr. Rajendra Prasad. Many guidebooks incorrectly list J.B. Kripalani, but official Assembly records confirm Dr. Rajendra Prasad as Chairman.",
            "ta": "முக்கிய வலைக் கேள்வி! தேசியக் கொடிக்கான அதிகாரப்பூர்வ தற்காலிகக் குழுவிற்கு டாக்டர் ராஜேந்திர பிரசாத் தலைமை தாங்கினார். பல வழிகாட்டி புத்தகங்கள் தவறாக ஜே.பி. கிருபளானியைக் குறிப்பிடுகின்றன, ஆனால் அதிகாரப்பூர்வ அவை பதிவுகள் டாக்டர் ராஜேந்திர பிரசாத்தையே தலைவராக உறுதிப்படுத்துகின்றன."
        },
        "why_not_others": {
            "A": {"en": "Correct. Dr. Rajendra Prasad chaired the Ad hoc Committee on National Flag.", "ta": "சரி. டாக்டர் ராஜேந்திர பிரசாத் தேசியக் கொடிக்கான தற்காலிகக் குழுவின் தலைவர்."},
            "B": {"en": "Incorrect Common Distractor. J.B. Kripalani was a member, not the Chairman of the Flag Committee.", "ta": "தவறு பொதுவான குழப்பம். ஜே.பி. கிருபளானி ஒரு உறுப்பினர், கொடிக் குழுவின் தலைவர் அல்ல."},
            "C": {"en": "Incorrect. Nehru moved the resolution on Flag adoption in July 1947, but was not Chair of this Ad hoc committee.", "ta": "தவறு. நேரு ஜூலை 1947 இல் கொடி ஏற்புத் தீர்மானத்தை முன்மொழிந்தார், ஆனால் இத்தற்காலிகக் குழுவின் தலைவர் அல்ல."},
            "D": {"en": "Incorrect. Rajaji was a member of the committee.", "ta": "தவறு. ராஜாஜி இக்குழுவின் உறுப்பினராக இருந்தார்."}
        },
        "tnpsc_tip": {
            "en": "Members of Flag Ad hoc Committee: Rajendra Prasad (Chair), Ambedkar, Maulana Azad, Sarojini Naidu, Rajaji, Kripalani, KM Munshi, BR Ambedkar.",
            "ta": "கொடிக் தற்காலிகக் குழு உறுப்பினர்கள்: ராஜேந்திர பிரசாத் (தலைவர்), அம்பேத்கர், மௌலானா ஆசாத், சரோஜினி நாயுடு, ராஜாஜி, கிருபளானி, கே.எம். முன்ஷி."
        },
        "revision_fact": {
            "en": "The committee recommended adopting the Tricolor with Ashoka Chakra as the National Flag.",
            "ta": "அசோக சக்கரத்துடன் கூடிய மூவர்ணக் கொடியை தேசியக் கொடியாக ஏற்றுக்கொள்ள இக்குழு பரிந்துரைத்தது."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Remember",
        "estimated_time_sec": 50,
        "pyq_similarity": "High",
        "tags": ["Ad hoc Flag Committee", "Dr. Rajendra Prasad", "Kripalani Trap"]
    },
    # Q48
    {
        "id": "MIC_M_048",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "Basic Statement Model",
        "question": {
            "en": "Consider the following statements regarding the sessions of the Constituent Assembly:\n1. The Constituent Assembly held a total of 11 formal sessions for constitution-making.\n2. The 11th session was held between November 14 and November 26, 1949.\n3. The Assembly met for a special 12th session on January 24, 1950 to sign the Constitution.\n\nWhich of the statements given above are correct?",
            "ta": "அரசியலமைப்பு நிர்ணய அவையின் அமர்வுகள் பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. அரசியலமைப்பு உருவாக்கத்திற்காக அரசியலமைப்பு நிர்ணய அவை மொத்தம் 11 முறைப்படியான அமர்வுகளை நடத்தியது.\n2. 11 வது அமர்வு நவம்பர் 14 முதல் நவம்பர் 26, 1949 வரை நடைபெற்றது.\n3. அரசியலமைப்பில் கையொப்பமிட ஜனவரி 24, 1950 அன்று அவை சிறப்பு 12 வது அமர்வாகக் கூடியது.\n\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?"
        },
        "options": [
            {"id": "A", "en": "1 and 2 only", "ta": "1 மற்றும் 2 மட்டுமே"},
            {"id": "B", "en": "2 and 3 only", "ta": "2 மற்றும் 3 மட்டுமே"},
            {"id": "C", "en": "1 and 3 only", "ta": "1 மற்றும் 3 மட்டுமே"},
            {"id": "D", "en": "1, 2, and 3", "ta": "1, 2 மற்றும் 3"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "All three statements are true. There were 11 formal sessions dedicated to constitution-making (11th session ending on Nov 26, 1949), and the Assembly assembled one final time on Jan 24, 1950 for signing the official text.",
            "ta": "மூன்று கூற்றுகளும் உண்மையானவை. அரசியலமைப்பு உருவாக்கத்திற்காக 11 முறைப்படியான அமர்வுகள் அர்ப்பணிக்கப்பட்டன (11 வது அமர்வு நவம்பர் 26, 1949 இல் முடிவடைந்தது), மேலும் அதிகாரப்பூர்வ உரையில் கையொப்பமிட ஜனவரி 24, 1950 அன்று அவை இறுதி முறையாகக் கூடியது."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Statement 3 is also correct.", "ta": "தவறு. கூற்று 3 உம் சரியானது."},
            "B": {"en": "Incorrect. Statement 1 is also correct.", "ta": "தவறு. கூற்று 1 உம் சரியானது."},
            "C": {"en": "Incorrect. Statement 2 is also correct.", "ta": "தவறு. கூற்று 2 உம் சரியானது."},
            "D": {"en": "Correct. Statements 1, 2, and 3 are all correct.", "ta": "சரி. கூற்றுகள் 1, 2 மற்றும் 3 அனைத்தும் சரியானவை."}
        },
        "tnpsc_tip": {
            "en": "Total constitution-making sessions = 11; Final signing session = Jan 24, 1950.",
            "ta": "மொத்த அரசியலமைப்பு உருவாக்க அமர்வுகள் = 11; இறுதி கையொப்ப அமர்வு = ஜனவரி 24, 1950."
        },
        "revision_fact": {
            "en": "First session was held from December 9 to December 23, 1946.",
            "ta": "முதல் அமர்வு டிசம்பர் 9 முதல் டிசம்பர் 23, 1946 வரை நடைபெற்றது."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Understand",
        "estimated_time_sec": 55,
        "pyq_similarity": "High",
        "tags": ["Assembly Sessions Count", "11 Sessions", "Jan 24 Final Sitting"]
    },
    # Q49
    {
        "id": "MIC_M_049",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "Process-Based",
        "question": {
            "en": "What was the significance of the role played by Sir Alladi Krishnaswamy Ayyar in the Drafting Committee and Assembly debates?",
            "ta": "வரைவுக் குழுவிலும் அவை விவாதங்களிலும் சர் அல்லாடி கிருஷ்ணசுவாமி அய்யர் ஆற்றிய பங்கின் முக்கியத்துவம் யாது?"
        },
        "options": [
            {"id": "A", "en": "As a former Advocate-General of Madras, his profound expertise in constitutional law shaped provisions on judicial review, fundamental rights, and executive powers.", "ta": "மதராஸின் முன்னாள் அட்வகேட் ஜெனரலாக, அரசியலமைப்புச் சட்டத்தில் அவரது ஆழமான நிபுணத்துவம் நீதித்துறை மறுஆய்வு, அடிப்படை உரிமைகள் மற்றும் நிர்வாக அதிகாரங்கள் பற்றிய விதிகளை வடிவமைத்தது."},
            {"id": "B", "en": "He was the chief financial consultant who introduced the First Five-Year Plan in the Assembly.", "ta": "அவர் அவையில் முதல் ஐந்தாண்டுத் திட்டத்தை அறிமுகப்படுத்திய முதன்மை நிதி ஆலோசகராவார்."},
            {"id": "C", "en": "He led the socialist opposition group that voted against the Preamble.", "ta": "முகப்புரைக்கு எதிராக வாக்களித்த சோசலிச எதிர்ப்புக் குழுவிற்கு அவர் தலைமை தாங்கினார்."},
            {"id": "D", "en": "He translated the Constitution into Tamil and Telugu.", "ta": "அவர் அரசியலமைப்பை தமிழ் மற்றும் தெலுங்கில் மொழிபெயர்த்தார்."}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Sir Alladi Krishnaswamy Ayyar was one of India's most eminent legal minds. Dr. Ambedkar paid high tribute to Alladi's legal scholarship in the Assembly, noting that Alladi's mastery of case law and foreign constitutions was invaluable to the Drafting Committee.",
            "ta": "சர் அல்லாடி கிருஷ்ணசுவாமி அய்யர் இந்தியாவின் மிகச்சிறந்த சட்ட அறிஞர்களில் ஒருவராவார். அவையில் அல்லாடியின் சட்டப் புலமைக்கு அம்பேத்கர் உயர் அஞ்சலி செலுத்தினார், வழக்குச் சட்டம் மற்றும் வெளிநாட்டு அரசியலமைப்புகளில் அல்லாடியின் தேர்ச்சி வரைவுக் குழுவிற்கு மிகவும் மதிப்பற்றது என்று குறிப்பிட்டார்."
        },
        "why_not_others": {
            "A": {"en": "Correct. Alladi Krishnaswamy Ayyar's legal genius played a central role in framing rights and judicial powers.", "ta": "சரி. அல்லாடி கிருஷ்ணசுவாமி அய்யரின் சட்டப் மேதைமை உரிமைகள் மற்றும் நீதித்துறை அதிகாரங்களை வரைவதில் மத்திய பங்காற்றியது."},
            "B": {"en": "Incorrect. Five-Year Plans were developed under Planning Commission in 1950s.", "ta": "தவறு. ஐந்தாண்டுத் திட்டங்கள் 1950களில் திட்டக் குழுவின் கீழ் உருவாக்கப்பட்டன."},
            "C": {"en": "Incorrect. Alladi supported the Preamble and Constitution whole-heartedly.", "ta": "தவறு. அல்லாடி முகப்புரை மற்றும் அரசியலமைப்பை முழுமனதுடன் ஆதரித்தார்."},
            "D": {"en": "Incorrect. He was a legal draftsman, not a regional translator.", "ta": "தவறு. அவர் ஒரு சட்ட வரைவாளர், பிராந்திய மொழிபெயர்ப்பாளர் அல்ல."}
        },
        "tnpsc_tip": {
            "en": "Alladi famously described the Preamble as expressing 'what we had thought or dreamed so long'.",
            "ta": "அல்லாடி முகப்புரையை 'நாம் இவ்வளவு காலம் சிந்தித்ததை அல்லது கற்பனை செய்ததை வெளிப்படுத்துவது' என்று புகழ்பெற்ற முறையில் விவரித்தார்."
        },
        "revision_fact": {
            "en": "Sir Alladi Krishnaswamy Ayyar served as Advocate-General of Madras Presidency for 15 years (1929-1944).",
            "ta": "சர் அல்லாடி கிருஷ்ணசுவாமி அய்யர் மதராஸ் மாகாணத்தின் அட்வகேட் ஜெனரலாக 15 ஆண்டுகள் (1929-1944) பணியாற்றினார்."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Understand",
        "estimated_time_sec": 55,
        "pyq_similarity": "High",
        "tags": ["Sir Alladi Krishnaswamy Ayyar", "Drafting Committee Member", "Legal Genius"]
    },
    # Q50
    {
        "id": "MIC_M_050",
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Medium",
        "question_type": "Conceptual",
        "question": {
            "en": "Which of the following features highlights the unique achievement of the Indian Constituent Assembly compared to constitutional assemblies in many other post-colonial nations?",
            "ta": "மற்ற பல காலனித்துவத்திற்கு பிந்தைய நாடுகளின் அரசியலமைப்பு அவைகளுடன் ஒப்பிடும் போது, இந்திய அரசியலமைப்பு நிர்ணய அவையின் தனித்துவமான சாதனையை விளக்கும் அம்சம் எது?"
        },
        "options": [
            {"id": "A", "en": "It successfully created a durable democratic constitutional framework that has endured without military overthrows, civil wars, or constitutional abrogation for over seven decades.", "ta": "இது ராணுவ கவிழ்ப்புகள், உள்நாட்டுப் போர்கள் அல்லது அரசியலமைப்பு ரத்துக்கள் இன்றி ஏழு தசாப்தங்களுக்கும் மேலாக நீடித்த ஒரு உறுதியான ஜனநாயக அரசியலமைப்புக் கட்டமைப்பை வெற்றிகரமாக உருவாக்கியது."},
            {"id": "B", "en": "It was the only assembly in world history that drafted a constitution without holding a single vote on any clause.", "ta": "எந்தவொரு சரத்தின் மீதும் ஒரு வாக்கெடுப்பும் நடத்தாமல் அரசியலமைப்பை வரைந்த உலக வரலாற்றிலேயே ஒரே அவை இதுவே ஆகும்."},
            {"id": "C", "en": "It succeeded in abolishing all regional languages and establishing a single religion across India.", "ta": "இது அனைத்து பிராந்திய மொழிகளையும் ஒழித்து இந்தியா முழுவதும் ஒரே மதத்தை நிறுவுவதில் வெற்றி பெற்றது."},
            {"id": "D", "en": "It was the only assembly that retained British governors in all states permanently.", "ta": "அனைத்து மாநிலங்களிலும் பிரிட்டிஷ் ஆளுநர்களை நிரந்தரமாகத் தக்க வைத்துக் கொண்ட ஒரே அவை இதுவே ஆகும்."}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "While constitutional frameworks in many post-colonial Asian and African nations collapsed into military dictatorships or were repeatedly rewritten, India's Constituent Assembly constructed an enduring, flexible, democratic foundation that preserved national unity while protecting liberty and diversity.",
            "ta": "பல காலனித்துவத்திற்கு பிந்தைய ஆசிய மற்றும் ஆப்பிரிக்க நாடுகளின் அரசியலமைப்பு சட்டக் கட்டமைப்புகள் ராணுவ சர்வாதிகாரங்களில் சரிந்தன அல்லது மீண்டும் மீண்டும் எழுதப்பட்ட போதிலும், இந்தியாவின் அரசியலமைப்பு நிர்ணய அவை சுதந்திரம் மற்றும் பன்முகத்தப்பைப் பாதுகாக்கும் அதே வேளையில் தேசிய ஒற்றுமையைப் பேணும் ஒரு நீடித்த, நெகிழ்வான, ஜனநாயக அடித்தளத்தை உருவாக்கியது."
        },
        "why_not_others": {
            "A": {"en": "Correct. Extraordinary durability and stability of Indian constitutional democracy post-1950.", "ta": "சரி. 1950 க்குப் பிந்தைய இந்திய அரசியலமைப்பு ஜனநாயகத்தின் அபரிமிதமான நீடிப்புத்தன்மை மற்றும் ஸ்திரத்தன்மை."},
            "B": {"en": "Incorrect. Votes were held on contentious amendments.", "ta": "தவறு. சர்ச்சைக்குரிய திருத்தங்கள் மீது வாக்குப்பதிவுகள் நடத்தப்பட்டன."},
            "C": {"en": "Incorrect. India is a secular nation with 22 official languages in Eighth Schedule.", "ta": "தவறு. எட்டாவது அட்டவணையில் 22 அதிகாரப்பூர்வ மொழிகளைக் கொண்ட ஒரு மதச்சார்பற்ற நாடு இந்தியா."},
            "D": {"en": "Incorrect. British governors were replaced by elected/appointed Indian Governors."}
        },
        "tnpsc_tip": {
            "en": "Granville Austin called the Indian Constitution 'first and foremost a social document' dedicated to national renaissance.",
            "ta": "கான்வில் ஆஸ்டின் இந்திய அரசியலமைப்பை தேசிய மறுமலர்ச்சிக்கு அர்ப்பணிக்கப்பட்ட 'முதன்மையாகவும் முதன்மையாகவும் ஒரு சமூக ஆவணம்' என்று அழைத்தார்."
        },
        "revision_fact": {
            "en": "The Constitution of India is the longest written constitution of any sovereign country in the world.",
            "ta": "இந்திய அரசியலமைப்பு உலகின் எந்தவொரு இறையாண்மை கொண்ட நாட்டின் மிக நீண்ட எழுதப்பட்ட அரசியலமைப்பாகும்."
        },
        "source_reference": ["M. Laxmikanth", "NCERT", "Samacheer Kalvi"],
        "bloom_level": "Understand",
        "estimated_time_sec": 60,
        "pyq_similarity": "High",
        "tags": ["Unique Achievement", "Durable Constitution", "Granville Austin"]
    }
]

# Add legacy backward compatibility flat fields
for q in questions:
    q["question_en"] = q["question"]["en"]
    q["question_ta"] = q["question"]["ta"]
    q["options_en"] = [opt["en"] for opt in q["options"]]
    q["options_ta"] = [opt["ta"] for opt in q["options"]]
    q["answer"] = q["correct_answer"].lower()
    q["explanation_en"] = q["explanation"]["en"]
    q["explanation_ta"] = q["explanation"]["ta"]

target_file = r"c:\Users\Home\Desktop\tnpsc_ai\data\questions\polity\making_of_indian_constitution_medium.json"
os.makedirs(os.path.dirname(target_file), exist_ok=True)

with open(target_file, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {len(questions)} high-quality Medium MCQs into {target_file}")
