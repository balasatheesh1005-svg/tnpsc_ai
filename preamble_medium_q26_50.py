# preamble_medium_q26_50.py
from scratch_preamble_medium_helper import make_medium_q

def get_medium_q26_50():
    qs = []

    # Q26 - Conceptual Distinction - Ans B
    qs.append(make_medium_q(
        q_id="PRE_M_026", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="Conceptual Distinction",
        q_en="Which statement accurately explains why the Preamble is called the 'Key to open the mind of the makers'?",
        q_ta="முகவுரை ஏன் 'அரசியலமைப்புச் சிற்பிகளின் சிந்தனையைத் திறக்கும் சாவி' என்று அழைக்கப்படுகிறது என்பதைச் சரியாக விவரிக்கும் கூற்று எது?",
        opts_en=[
            "Because it contains secret codes to unlock executive emergency powers.",
            "Because it encapsulates the general intentions, core values, and overall philosophy of the Constituent Assembly members when drafting the Constitution.",
            "Because it grants judges the power to overrule parliamentary elections at will.",
            "Because it was written by British constitutional lawyers prior to 1947."
        ],
        opts_ta=[
            "நிர்வாக அவசரகால அதிகாரங்களைத் திறப்பதற்கான ரகசியக் குறியீடுகளைக் கொண்டுள்ளதால்.",
            "அரசியலமைப்பை வரைந்த போது அரசியலமைப்புச் சபை உறுப்பினர்களின் பொதுவான நோக்கங்கள், முக்கிய மதிப்புகள் மற்றும் ஒட்டுமொத்த தத்துவத்தை இது சுருக்கமாகக் கொண்டுள்ளதால்.",
            "நீதிபதிகளுக்கு நாடாளுமன்றத் தேர்தல்களை விருப்பம்போல ரத்து செய்யும் அதிகாரத்தை வழங்குவதால்.",
            "1947க்கு முன் பிரிட்டிஷ் அரசியலமைப்பு வழக்கறிஞர்களால் எழுதப்பட்டதால்."
        ],
        correct_ans="B",
        exp_en="The SC in Berubari (1960) and Kesavananda (1973) observed that Preamble contains the key to framers' mind because it expresses the grand goals and values that guided the Assembly.",
        exp_ta="பெருபாரி (1960) மற்றும் கேசவாநந்தா (1973) வழக்குகளில் உச்ச நீதிமன்றம் முகவுரை வரைவாளர்களின் மனதைத் திறக்கும் சாவியைக் கொண்டுள்ளது என்று குறிப்பிட்டது, ஏனெனில் இது சபையை வழிநடத்திய உன்னதமான இலக்குகளையும் மதிப்புகளையும் வெளிப்படுத்துகிறது.",
        wno_dict={
            "A": {"en": "Incorrect. Irrelevant claim.", "ta": "தவறு. தொடர்பற்ற கூற்று."},
            "B": {"en": "Correct. Encapsulates framers' core intentions and philosophy.", "ta": "சரி. வரைவாளர்களின் முக்கிய நோக்கங்களையும் தத்துவத்தையும் சுருக்கமாகக் கொண்டுள்ளது."},
            "C": {"en": "Incorrect. Preamble does not confer judicial power to overrule elections.", "ta": "தவறு. தேர்தல்களை ரத்து செய்ய அதிகாரம் தராது."},
            "D": {"en": "Incorrect. Drafted by Indian Constituent Assembly.", "ta": "தவறு. இந்திய அரசியலமைப்புச் சபையால் வரைடப்பட்டது."}
        },
        tip_en="Preamble = Key to Framers' Mind (used when provisions are ambiguous).",
        tip_ta="முகவுரை = வரைவாளர்களின் மனதைத் திறக்கும் சாவி (சரத்துகள் தெளிவற்ற நிலையில் பயன்படுத்தப்படும்).",
        rev_en="Key to framers' mind = Encapsulates Assembly's core philosophy.",
        rev_ta="வரைவாளர்களின் மனதைத் திறக்கும் சாவி = சபையின் தத்துவத்தைக் கொண்டுள்ளது.",
        sources=["Preamble Notes Part 1 & 2"],
        bloom="Understand", est_sec=45, pyq_sim="High", tags=["Key to Mind", "Preamble Significance"]
    ))

    # Q27 - Constitutional Relationship - Ans C
    qs.append(make_medium_q(
        q_id="PRE_M_027", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="Constitutional Relationship",
        q_en="How does Article 39(b) and 39(c) in Part IV (DPSPs) directly serve the Preamble's commitment to 'Socialist' and 'Economic Justice' goals?",
        q_ta="பகுதி IV இல் உள்ள (DPSP) உறுப்பு 39(b) மற்றும் 39(c) முகவுரையின் 'சமதர்ம' மற்றும் 'பொருளாதார நீதி' இலக்குகளுக்கான அர்ப்பணிப்பிற்கு எவ்வாறு நேரடியாகச் சேவையாற்றுகிறது?",
        opts_en=[
            "By establishing military dictatorship over all private factories.",
            "By completely eliminating foreign exchange transactions.",
            "By directing the State to distribute material resources of the community for common good [Art 39(b)] and prevent concentration of wealth to common detriment [Art 39(c)].",
            "By granting tax exemptions to multinational monopolies."
        ],
        opts_ta=[
            "அனைத்து தனியார் தொழிற்சாலைகள் மீதும் இராணுவ சர்வாதிகாரத்தை நிறுவுவதன் மூலம்.",
            "அந்நிய செலாவணி பரிவர்த்தனைகளை முற்றிலும் ஒழிப்பதன் மூலம்.",
            "சமுதாயத்தின் பொருள் வளங்களைப் பொது நலனுக்காக விநியோகிக்கவும் [உறுப்பு 39(b)] மற்றும் பொதுக் கேட்டிற்கு வழிவகுக்கும் வகையில் செல்வம் குவிவதைத் தடுக்கவும் [உறுப்பு 39(c)] அரசை வழிநடத்துவதன் மூலம்.",
            "பன்னாட்டு ஏகபோக நிறுவனங்களுக்கு வரி விலக்குகள் வழங்குவதன் மூலம்."
        ],
        correct_ans="C",
        exp_en="Articles 39(b) and 39(c) embody the economic core of Democratic Socialism, requiring the State to ensure material resources serve the common good and prevent concentration of wealth.",
        exp_ta="உறுப்புகள் 39(b) மற்றும் 39(c) ஜனநாயக சமதர்மத்தின் பொருளாதார மையத்தைக் கொண்டுள்ளன, சமுதாயப் பொருள் வளங்கள் பொது நலனுக்காகச் சேவையாற்றுவதையும் செல்வம் குவிவது தடுக்கப்படுவதையும் அரசு உறுதி செய்ய ஆணையிடுகிறது.",
        wno_dict={
            "A": {"en": "Incorrect. India is a democracy.", "ta": "தவறு. இந்தியா ஒரு ஜனநாயகம்."},
            "B": {"en": "Incorrect. Foreign exchange is regulated, not eliminated.", "ta": "தவறு. அந்நிய செலாவணி ஒழுங்குபடுத்தப்படுகிறது."},
            "C": {"en": "Correct. Art 39(b) & (c) mandate equitable resource distribution & prevent wealth concentration.", "ta": "சரி. உறுப்பு 39(b) & (c) சமமான வள விநியோகத்தையும் செல்வம் குவிவதைத் தடுப்பதையும் ஆணையிடுகிறது."},
            "D": {"en": "Incorrect. Prevents monopolies, doesn't grant tax exemptions to them.", "ta": "தவறு. ஏகபோகங்களைத் தடுக்கிறது."}
        },
        tip_en="Articles 39(b) & 39(c) = Core DPSP articles implementing Preamble's Socialist and Economic Justice goals.",
        tip_ta="உறுப்புகள் 39(b) & 39(c) = முகவுரையின் சமதர்ம மற்றும் பொருளாதார நீதி இலக்குகளை அமல்படுத்தும் முக்கிய DPSP உறுப்புகள்.",
        rev_en="Art 39(b)&(c) = Implements Socialist & Economic Justice goals.",
        rev_ta="உறுப்பு 39(b)&(c) = சமதர்ம & பொருளாதார நீதி இலக்குகளை அமல்படுத்துகிறது.",
        sources=["Preamble Notes Part 1 & 2"],
        bloom="Analyze", est_sec=45, pyq_sim="High", tags=["Article 39b", "Article 39c", "Socialist", "DPSP"]
    ))

    # Q28 - Case-law - Ans D
    qs.append(make_medium_q(
        q_id="PRE_M_028", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="Case-law Based",
        q_en="What was the core difference between the Supreme Court's approach to the Preamble in Berubari (1960) versus Kesavananda Bharati (1973)?",
        q_ta="1960 பெருபாரி மற்றும் 1973 கேசவாநந்த பாரதி வழக்கிலும் முகவுரையை அணுகிய உச்ச நீதிமன்றத்தின் அணுகுமுறையில் உள்ள முக்கிய வேறுபாடு என்ன?",
        opts_en=[
            "Berubari held Preamble was justiciable, whereas Kesavananda held it non-justiciable.",
            "Berubari held Preamble was amended in 1976, whereas Kesavananda held it was amended in 1950.",
            "Berubari held Preamble was written by Nehru, whereas Kesavananda held it was written by Ambedkar.",
            "Berubari held Preamble was NOT a part of the Constitution, whereas Kesavananda OVERRULED Berubari and declared Preamble IS a part of the Constitution."
        ],
        opts_ta=[
            "பெருபாரி முகவுரை நிலைநிறுத்தக்கூடியது என்றது; ஆனால் கேசவாநந்தா நிலைநிறுத்த முடியாதது என்றது.",
            "பெருபாரி முகவுரை 1976 இல் திருத்தப்பட்டது என்றது; ஆனால் கேசவாநந்தா 1950 இல் திருத்தப்பட்டது என்றது.",
            "பெருபாரி முகவுரை நேருவால் எழுதப்பட்டது என்றது; ஆனால் கேசவாநந்தா அம்பேத்கரால் எழுதப்பட்டது என்றது.",
            "பெருபாரி முகவுரை அரசியலமைப்பின் ஒரு பகுதி அல்ல என்றது; ஆனால் கேசவாநந்தா பெருபாரியை ரத்து செய்து முகவுரை அரசியலமைப்பின் ஒரு பகுதி தான் என அறிவித்தது."
        ],
        correct_ans="D",
        exp_en="The fundamental shift in jurisprudence: Berubari (1960) excluded Preamble from the Constitution text; Kesavananda Bharati (1973) explicitly overruled Berubari and recognized Preamble as part of the Constitution.",
        exp_ta="வழக்கியலின் அடிப்படை மாற்றம்: பெருபாரி (1960) முகவுரையை அரசியலமைப்பு உரையிலிருந்து விலக்கியது; கேசவாநந்த பாரதி (1973) பெருபாரியை ரத்து செய்து முகவுரையை அரசியலமைப்பின் ஒரு பகுதியாக அங்கீகரித்தது.",
        wno_dict={
            "A": {"en": "Incorrect. Both agreed Preamble is non-justiciable.", "ta": "தவறு. இரண்டும் முகவுரை நிலைநிறுத்த முடியாதது என்பதை ஏற்றன."},
            "B": {"en": "Incorrect. Chronologically impossible.", "ta": "தவறு. காலவரிசைப்படி சாத்தியமற்றது."},
            "C": {"en": "Incorrect. Irrelevant claim.", "ta": "தவறு. தொடர்பற்ற கூற்று."},
            "D": {"en": "Correct. Berubari = NOT part; Kesavananda = Overruled Berubari & declared IS part.", "ta": "சரி. பெருபாரி = பகுதி அல்ல; கேசவாநந்தா = ரத்து செய்து பகுதி தான் என்றது."}
        },
        tip_en="Remember key shift: Berubari (1960) = NOT part -> Kesavananda (1973) = IS part.",
        tip_ta="முக்கிய மாற்றத்தை நினைவில் கொள்க: பெருபாரி (1960) = பகுதி அல்ல -> கேசவாநந்தா (1973) = பகுதி தான்.",
        rev_en="Berubari (1960): NOT part vs Kesavananda (1973): IS part.",
        rev_ta="பெருபாரி (1960): பகுதி அல்ல vs கேசவாநந்தா (1973): பகுதி தான்.",
        sources=["Preamble Notes Part 2"],
        bloom="Understand", est_sec=45, pyq_sim="High", tags=["Berubari", "Kesavananda", "Judicial Evolution"]
    ))

    # Q29 - Amendment / Status - Ans A
    qs.append(make_medium_q(
        q_id="PRE_M_029", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="Amendment / Status",
        q_en="Why was the addition of the word 'Integrity' in 1976 considered constitutionally significant for national unity?",
        q_ta="1976 இல் 'ஒருமைப்பாடு' (Integrity) என்ற சொல் சேர்க்கப்பட்டது தேசிய ஒற்றுமைக்கு அரசியலமைப்பு ரீதியாக ஏன் முக்கியத்துவம் வாய்ந்ததாகக் கருதப்படுகிறது?",
        opts_en=[
            "It strengthened the territorial and psychological dimension of national integration, countering secessionist tendencies.",
            "It allowed Parliament to abolish State Legislative Assemblies at will.",
            "It mandated a single national language across all states.",
            "It made fundamental duties punishable by death penalty."
        ],
        opts_ta=[
            "இது பிரிவினைவாதப் போக்குகளை எதிர்த்து தேசிய ஒருமைப்பாட்டின் நிலப்பரப்பு மற்றும் உளவியல் பரிமாணத்தை வலுப்படுத்தியது.",
            "இது நாடாளுமன்றத்திற்கு மாநில சட்டமன்றங்களை விருப்பம்போல ஒழிக்க அனுமதித்தது.",
            "இது அனைத்து மாநிலங்களிலும் ஒரே தேசிய மொழியைக் கட்டாயமாக்கியது.",
            "இது அடிப்படை கடமைகளை மரண தண்டனைக்குரியதாக ஆக்கியது."
        ],
        correct_ans="A",
        exp_en="The word 'Integrity' aims at preventing regional secessionism, reinforcing that India is an indestructible Union of destructible states with a psychological bond of common nationhood.",
        exp_ta="'ஒருமைப்பாடு' என்ற சொல் பிராந்திய பிரிவினைவாதத்தைத் தடுப்பதை நோக்கமாகக் கொண்டுள்ளது, இந்தியா என்பது அழியக்கூடிய மாநிலங்களின் அழியாத ஒன்றியம் என்பதை உளவியல் ரீதியாக வலுப்படுத்துகிறது.",
        wno_dict={
            "A": {"en": "Correct. Integrity counters secessionism and emphasizes national unity.", "ta": "சரி. ஒருமைப்பாடு பிரிவினைவாதத்தை எதிர்த்து தேசிய ஒற்றுமையை வலியுறுத்துகிறது."},
            "B": {"en": "Incorrect. Article 356 governs state suspension under strict judicial review.", "ta": "தவறு. உறுப்பு 356 மாநில இடைநிறுத்தத்தை ஆள்கிறது."},
            "C": {"en": "Incorrect. Article 343 & 8th Schedule protect linguistic diversity.", "ta": "தவறு. உறுப்பு 343 & 8வது அட்டவணை மொழிப் பன்முகத்தன்மையைப் பாதுகாக்கிறது."},
            "D": {"en": "Incorrect. FDs are non-penal in constitutional text.", "ta": "தவறு. கடமைகள் தண்டனைக்குரியவை அல்ல."}
        },
        tip_en="Integrity (added by 42nd Amend 1976) = Counters Secessionism & strengthens Territorial Integration.",
        tip_ta="ஒருமைப்பாடு (42வது திருத்தம் 1976 இல் சேர்க்கப்பட்டது) = பிரிவினைவாதத்தை எதிர்த்து நிலப்பரப்பு ஒருமைப்பாட்டை வலுப்படுத்துகிறது.",
        rev_en="Integrity added in 1976 counters secessionist tendencies.",
        rev_ta="1976 இல் சேர்க்கப்பட்ட ஒருமைப்பாடு பிரிவினைவாதப் போக்குகளை எதிர்க்கிறது.",
        sources=["Preamble Notes Part 1 & 2"],
        bloom="Understand", est_sec=45, pyq_sim="High", tags=["Integrity", "National Unity", "Secessionism"]
    ))

    # Q30 - Conceptual Distinction - Ans B
    qs.append(make_medium_q(
        q_id="PRE_M_030", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="Conceptual Distinction",
        q_en="Which statement correctly distinguishes 'Social Justice' from 'Economic Justice' in the Preamble?",
        q_ta="முகவுரையில் உள்ள 'சமூக நீதியை' 'பொருளாதார நீதியி'லிருந்து சரியாக வேறுபடுத்தும் கூற்று எது?",
        opts_en=[
            "Social Justice applies to foreign citizens, whereas Economic Justice applies to Indian citizens.",
            "Social Justice aims at equal treatment by eliminating social discrimination based on caste, race, or sex; whereas Economic Justice aims at eliminating non-discrimination based on economic factors like wealth and income disparities.",
            "Social Justice is part of Preamble, whereas Economic Justice is not mentioned in Preamble.",
            "Social Justice was added in 1976, whereas Economic Justice was present in 1950."
        ],
        opts_ta=[
            "சமூக நீதி வெளிநாட்டு குடிமக்களுக்குப் பொருந்தும்; ஆனால் பொருளாதார நீதி இந்திய குடிமக்களுக்குப் பொருந்தும்.",
            "சமூக நீதி சாதி, இனம் அல்லது பாலினம் அடிப்படையிலான சமூகப் பாகுபாடுகளை ஒழித்து சமமான நடத்தையை நோக்கமாகக் கொண்டுள்ளது; ஆனால் பொருளாதார நீதி செல்வம் மற்றும் வருமான ஏற்றத்தாழ்வுகள் போன்ற பொருளாதாரக் காரணிகளின் அடிப்படையிலான பாகுபாடுகளை ஒழிப்பதை நோக்கமாகக் கொண்டுள்ளது.",
            "சமூக நீதி முகவுரையின் பகுதி; ஆனால் பொருளாதார நீதி முகவுரையில் குறிப்பிடப்படவில்லை.",
            "சமூக நீதி 1976 இல் சேர்க்கப்பட்டது; ஆனால் பொருளாதார நீதி 1950 இல் இருந்தது."
        ],
        correct_ans="B",
        exp_en="Social Justice = Elimination of social status discrimination (caste, religion, sex). Economic Justice = Elimination of economic inequality (wealth, income, property disparities). Combined = Distributive Justice.",
        exp_ta="சமூக நீதி = சமூக அந்தஸ்து பாகுபாடு ஒழிப்பு (சாதி, மதம், பாலினம்). பொருளாதார நீதி = பொருளாதார சமத்துவமின்மை ஒழிப்பு (செல்வம், வருமானம், சொத்து ஏற்றத்தாழ்வுகள்). இரண்டும் சேர்ந்தது = விநியோக நீதி.",
        wno_dict={
            "A": {"en": "Incorrect. Both apply to Indian society.", "ta": "தவறு. இரண்டும் இந்திய சமுதாயத்திற்குப் பொருந்தும்."},
            "B": {"en": "Correct. Accurately distinguishes social status equality from wealth/income equality.", "ta": "சரி. சமூக அந்தஸ்து சமத்துவத்தை செல்வம்/வருமான சமத்துவத்திலிருந்து துல்லியமாக வேறுபடுத்துகிறது."},
            "C": {"en": "Incorrect. Both are explicitly in Preamble.", "ta": "தவறு. இரண்டும் முகவுரையில் வெளிப்படையாக உள்ளன."},
            "D": {"en": "Incorrect. Both were present in original 1950 Preamble.", "ta": "தவறு. இரண்டும் 1950 அசல் முகவுரையில் இருந்தன."}
        },
        tip_en="Social Justice + Economic Justice = Distributive Justice.",
        tip_ta="சமூக நீதி + பொருளாதார நீதி = விநியோக நீதி.",
        rev_en="Social Justice (caste/sex equality) + Economic Justice (income/wealth equality).",
        rev_ta="சமூக நீதி (சாதி/பாலின சமத்துவம்) + பொருளாதார நீதி (வருமான/செல்வ சமத்துவம்).",
        sources=["Preamble Notes Part 1"],
        bloom="Understand", est_sec=45, pyq_sim="High", tags=["Social Justice", "Economic Justice", "Distributive Justice"]
    ))

    # Q31 - Application / Inference - Ans C
    qs.append(make_medium_q(
        q_id="PRE_M_031", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="Application / Inference",
        q_en="Suppose a High Court judge is interpreting an ambiguous provision of a state tenancy law. Which constitutional principle guides the judge to choose an interpretation that favors vulnerable tenants over land monopolies?",
        q_ta="ஒரு உயர் நீதிமன்ற நீதிபதி ஒரு மாநில வாடகைச் சட்டத்தின் தெளிவற்ற விதியை விவரிப்பதாகக் கொள்வோம். நில ஏகபோகங்களை விடப் பாதிக்கப்படக்கூடிய வாடகைதாரர்களுக்குச் சாதகமான விளக்கத்தைத் தேர்ந்தெடுக்க நீதிபதிக்கு எந்த அரசியலமைப்புக் கோட்பாடு வழிகாட்டுகிறது?",
        opts_en=[
            "The principle of Judicial Supremacy over Parliament.",
            "The principle of Absolute Free Market Capitalism.",
            "The Preamble's commitment to 'Socialist' welfare state goals and 'Social & Economic Justice'.",
            "The doctrine of Parliamentary Privilege."
        ],
        opts_ta=[
            "பாராளுமன்றத்திற்கு மேலான நீதித்துறை மேலாதிக்கக் கோட்பாடு.",
            "பூரண சுதந்திர சந்தை முதலாளித்துவக் கோட்பாடு.",
            "சமதர்ம' நலன்புரி அரசு இலக்குகள் மற்றும் 'சமூக & பொருளாதார நீதிக்கு' முகவுரையின் அர்ப்பணிப்பு.",
            "பாராளுமன்றச் சலுகைக் கோட்பாடு."
        ],
        correct_ans="C",
        exp_en="Judges use Preamble's 'Socialist' and 'Social & Economic Justice' goals as an Interpretive Compass when statutory wording is ambiguous, leaning towards welfare and protection of vulnerable groups.",
        exp_ta="சட்டத்தின் சொற்கள் தெளிவற்றதாக இருக்கும் போது நீதிபதிகள் நலன்புரி மற்றும் பாதிக்கப்பட்ட குழுக்களின் பாதுகாப்பை நோக்கிச் சாய முகவுரையின் 'சமதர்ம' மற்றும் 'சமூக & பொருளாதார நீதி' இலக்குகளை ஒரு விளக்கமளிக்கும் திசைகாட்டியாகப் பயன்படுத்துகின்றனர்.",
        wno_dict={
            "A": {"en": "Incorrect. India has Constitutional Supremacy, not Judicial Supremacy.", "ta": "தவறு. இந்தியாவில் அரசியலமைப்பு மேலாதிக்கம் உள்ளது."},
            "B": {"en": "Incorrect. Indian socialism rejects absolute unrestricted capitalism.", "ta": "தவறு. இந்திய சமதர்மம் கட்டுப்பாடற்ற முதலாளித்துவத்தை நிராகரிக்கிறது."},
            "C": {"en": "Correct. Preamble's Socialist & Distributive Justice ideals guide interpretation favoring welfare.", "ta": "சரி. முகவுரையின் சமதர்ம & விநியோக நீதி தத்துவங்கள் நலன்புரி விளக்கத்திற்கு வழிகாட்டுகின்றன."},
            "D": {"en": "Incorrect. Irrelevant to statutory interpretation of tenancy rights.", "ta": "தவறு. வாடகை உரிமை சட்ட விளக்கத்திற்கு தொடர்பற்றது."}
        },
        tip_en="Preamble is used as an Interpretive Compass to promote Welfare State goals in statutory ambiguity.",
        tip_ta="சட்டத் தெளிவற்ற நிலையில் நலன்புரி அரசு இலக்குகளை ஊக்குவிக்க முகவுரை விளக்கமளிக்கும் திசைகாட்டியாகப் பயன்படுகிறது.",
        rev_en="Preamble Socialist & Justice goals guide welfare-oriented statutory interpretation.",
        rev_ta="முகவுரை சமதர்ம & நீதி இலக்குகள் நலன்புரி சார்ந்த சட்ட விளக்கத்திற்கு வழிகாட்டுகின்றன.",
        sources=["Preamble Notes Part 1 & 2"],
        bloom="Apply", est_sec=45, pyq_sim="High", tags=["Socialist", "Welfare State", "Judicial Interpretation"]
    ))

    # Q32 - Constitutional Relationship - Ans D
    qs.append(make_medium_q(
        q_id="PRE_M_032", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="Constitutional Relationship",
        q_en="What is the functional relationship between the Preamble, Fundamental Rights (Part III), DPSP (Part IV), and Fundamental Duties (Part IVA)?",
        q_ta="முகவுரை, அடிப்படை உரிமைகள் (பகுதி III), DPSP (பகுதி IV) மற்றும் அடிப்படை கடமைகள் (பகுதி IVA) ஆகியவற்றுக்கு இடையே உள்ள செயல்பாட்டுத் தொடர்பு என்ன?",
        opts_en=[
            "Preamble is justiciable, FRs are policies, DPSPs are duties, and FDs are invalid.",
            "FRs override Preamble, DPSPs override FRs, and FDs override everything.",
            "All four are completely unrelated components added by different foreign powers.",
            "Preamble states the grand Blueprint/Vision, Part III guarantees Civil & Political Rights, Part IV directs Socio-Economic Welfare Policies, and Part IVA imposes Civic Responsibilities on citizens."
        ],
        opts_ta=[
            "முகவுரை நிலைநிறுத்தக்கூடியது, FR கொள்கைகள், DPSP கடமைகள், மற்றும் FD செல்லாதவை.",
            "FR முகவுரையை மேலெழுதுகிறது, DPSP FR ஐ மேலெழுதுகிறது, மற்றும் FD அனைத்தையும் மேலெழுதுகிறது.",
            "நான்கும் வெவ்வேறு வெளிநாட்டு அதிகாரங்களால் சேர்க்கப்பட்ட முற்றிலும் தொடர்பற்ற கூறுகள்.",
            "முகவுரை பெரும் நீலவரைபடம்/தொலைநோக்கைக் கூறுகிறது, பகுதி III குடிமை & அரசியல் உரிமைகளை உத்தரவாதம் செய்கிறது, பகுதி IV சமூக-பொருளாதார நலன்புரிக் கொள்கைகளை வழிகாட்டுகிறது, பகுதி IVA குடிமக்கள் மீது குடிமைப் பொறுப்புகளைச் சுமத்துகிறது."
        ],
        correct_ans="D",
        exp_en="This forms the organic triad of the Constitution: Preamble = Grand Blueprint; Part III = Civil/Political Rights; Part IV = Socio-Economic Directives; Part IVA = Citizen Duties.",
        exp_ta="இது அரசியலமைப்பின் முக்கோண அமைப்பை உருவாக்குகிறது: முகவுரை = பெரும் நீலவரைபடம்; பகுதி III = குடிமை/அரசியல் உரிமைகள்; பகுதி IV = சமூக-பொருளாதார வழிகாட்டுதல்கள்; பகுதி IVA = குடிமகன் கடமைகள்.",
        wno_dict={
            "A": {"en": "Incorrect. Misidentifies all four elements.", "ta": "தவறு. நான்கு கூறுகளையும் தவறாக அடையாளம் காண்கிறது."},
            "B": {"en": "Incorrect. No automatic overriding hierarchy exists.", "ta": "தவறு. தானியங்கி மேலெழுதும் படிநிலை இல்லை."},
            "C": {"en": "Incorrect. Drafted by Indian Constituent Assembly.", "ta": "தவறு. இந்திய அரசியலமைப்புச் சபையால் வரைடப்பட்டது."},
            "D": {"en": "Correct. Accurately captures the integrated constitutional architecture.", "ta": "சரி. ஒருங்கிணைந்த அரசியலமைப்பு கட்டமைப்பைத் துல்லியமாகப் படம்பிடிக்கிறது."}
        },
        tip_en="Integrated Architecture: Preamble (Blueprint) -> Part III (Rights) -> Part IV (Welfare Policies) -> Part IVA (Duties).",
        tip_ta="ஒருங்கிணைந்த கட்டமைப்பு: முகவுரை (நீலவரைபடம்) -> பகுதி III (உரிமைகள்) -> பகுதி IV (நலன்கொள்கைகள்) -> பகுதி IVA (கடமைகள்).",
        rev_en="Preamble = Blueprint; Part III = Rights; Part IV = Welfare; Part IVA = Duties.",
        rev_ta="முகவுரை = நீலவரைபடம்; பகுதி III = உரிமைகள்; பகுதி IV = நலன்; பகுதி IVA = கடமைகள்.",
        sources=["Preamble Notes Part 1 & 2"],
        bloom="Analyze", est_sec=45, pyq_sim="High", tags=["Constitutional Triad", "FR DPSP FD Preamble"]
    ))

    # Q33 - TNPSC Trap - Ans A
    qs.append(make_medium_q(
        q_id="PRE_M_033", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="TNPSC Trap",
        q_en="Which of the following is a CORRECT statement regarding the Supreme Court's declaration of Basic Structure elements derived from the Preamble?",
        q_ta="முகவுரையிலிருந்து பெறப்பட்ட அடிப்படை கட்டமைப்பு கூறுகளை உச்ச நீதிமன்றம் அறிவிப்பது தொடர்பான பின்வரும் கூற்றுகளில் எது சரியானது?",
        opts_en=[
            "Not every single word in the Preamble is automatically a separate Basic Structure element; the SC identifies specific core features (e.g. Secularism, Democracy, Federalism) on a case-by-case basis.",
            "Every single word in the Preamble, including 'and' and 'the', is an independent Basic Structure element that can never be amended.",
            "Basic Structure elements can be repealed by a two-thirds majority in Rajya Sabha alone.",
            "Basic Structure doctrine applies only to State Executive orders, not Constitutional Amendments."
        ],
        opts_ta=[
            "முகவுரையில் உள்ள ஒவ்வொரு தனிச் சொல்லும் தானாகவே தனி அடிப்படை கட்டமைப்பு கூறு அல்ல; உச்ச நீதிமன்றம் வழக்குக்கு வழக்கு குறிப்பிட்ட முக்கிய அம்சங்களை (எ.கா. மதச்சார்பின்மை, ஜனநாயகம், கூட்டாட்சி) அடையாளம் காண்கிறது.",
            "முகவுரையில் உள்ள 'மற்றும்' உட்பட ஒவ்வொரு தனிச் சொல்லும் திருத்தப்பட முடியாத ஒரு சுதந்திரமான அடிப்படை கட்டமைப்பு கூறு ஆகும்.",
            "மாநிலங்களவையில் மட்டும் மூன்றில் இரண்டு பங்கு பெரும்பான்மையால் அடிப்படை கட்டமைப்பு கூறுகளை ரத்து செய்ய முடியும்.",
            "அடிப்படை கட்டமைப்பு கோட்பாடு மாநில நிர்வாக ஆணைகளுக்கு மட்டுமே பொருந்தும், அரசியலமைப்பு திருத்தங்களுக்கு அல்ல."
        ],
        correct_ans="A",
        exp_en="The Supreme Court determines Basic Structure features on a case-by-case basis using Preamble philosophy. Not every single word automatically constitutes an untouchable basic feature.",
        exp_ta="முகவுரை தத்துவத்தைப் பயன்படுத்தி உச்ச நீதிமன்றம் வழக்குக்கு வழக்கு அடிப்படை கட்டமைப்பு அம்சங்களைத் தீர்மானிக்கிறது. ஒவ்வொரு தனிச் சொல்லும் தானாகவே தொட முடியாத அடிப்படை அம்சமாக அமையாது.",
        wno_dict={
            "A": {"en": "Correct. SC identifies core features (Secularism, Democracy, Sovereignty) case-by-case.", "ta": "சரி. உச்ச நீதிமன்றம் முக்கிய அம்சங்களை வழக்குக்கு வழக்கு அடையாளம் காண்கிறது."},
            "B": {"en": "Incorrect. Extreme assertion that every single word is basic structure.", "ta": "தவறு. ஒவ்வொரு தனிச் சொல்லும் அடிப்படை அமைப்பு என்ற தீவிரக் கூற்று."},
            "C": {"en": "Incorrect. Basic structure CANNOT be destroyed by any parliamentary majority.", "ta": "தவறு. அடிப்படை அமைப்பை எந்த நாடாளுமன்ற பெரும்பான்மையாலும் அழிக்க முடியாது."},
            "D": {"en": "Incorrect. Basic structure specifically limits Constitutional Amendments under Art 368.", "ta": "தவறு. அடிப்படை அமைப்பு உறுப்பு 368 இன் கீழ் திருத்தங்களை வரம்பிற்குட்படுத்துகிறது."}
        },
        tip_en="TNPSC Trap: Basic Structure is identified CASE-BY-CASE by Supreme Court (not every word is automatically a basic feature).",
        tip_ta="TNPSC பொறி: அடிப்படை கட்டமைப்பு உச்ச நீதிமன்றத்தால் வழக்குக்கு வழக்கு அடையாளம் காணப்படுகிறது.",
        rev_en="Basic Structure elements identified case-by-case by Supreme Court.",
        rev_ta="அடிப்படை கட்டமைப்பு கூறுகள் உச்ச நீதிமன்றத்தால் வழக்குக்கு வழக்கு அடையாளம் காணப்படுகின்றன.",
        sources=["Preamble Notes Part 2"],
        bloom="Understand", est_sec=45, pyq_sim="High", tags=["Basic Structure", "Case by Case", "TNPSC Trap"]
    ))

    # Q34 - Direct - Ans B
    qs.append(make_medium_q(
        q_id="PRE_M_034", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="Direct",
        q_en="Which member of the Constituent Assembly famously observed that the Preamble expresses 'what we had thought or dreamed so long'?",
        q_ta="முகவுரை 'நாம் இவ்வளவு காலம் சிந்தித்ததை அல்லது கனவு கண்டதை' வெளிப்படுத்துகிறது என்று கூறிய அரசியலமைப்புச் சபை உறுப்பினர் யார்?",
        opts_en=["Dr. B.R. Ambedkar", "Sir Alladi Krishnaswami Ayyar", "K.M. Munshi", "Pandit Jawaharlal Nehru"],
        opts_ta=["டாக்டர் பி.ஆர். அம்பேத்கர்", "சர் அல்லாடி கிருஷ்ணசாமி ஐயர்", "கே.எம். முன்ஷி", "பண்டிட் ஜவஹர்லால் நேரு"],
        correct_ans="B",
        exp_en="Sir Alladi Krishnaswami Ayyar, a member of the Drafting Committee, remarked: 'The Preamble to our Constitution expresses what we had thought or dreamed so long.'",
        exp_ta="வரைவுக் குழுவின் உறுப்பினரான சர் அல்லாடி கிருஷ்ணசாமி ஐயர் குறிப்பிட்டார்: 'நமது அரசியலமைப்பின் முகவுரை நாம் இவ்வளவு காலம் சிந்தித்ததை அல்லது கனவு கண்டதை வெளிப்படுத்துகிறது.'",
        wno_dict={
            "A": {"en": "Incorrect. Ambedkar called Art 32 Heart & Soul.", "ta": "தவறு. அம்பேத்கர் உறுப்பு 32 ஐ இதயம் & ஆன்மா என்றார்."},
            "B": {"en": "Correct. Sir Alladi Krishnaswami Ayyar coined this statement.", "ta": "சரி. சர் அல்லாடி கிருஷ்ணசாமி ஐயர் இந்த அறிக்கையைக் கூறினார்."},
            "C": {"en": "Incorrect. K.M. Munshi called it Horoscope of Sovereign Democratic Republic.", "ta": "தவறு. கே.எம். முன்ஷி அதை ஜாதகம் என்றார்."},
            "D": {"en": "Incorrect. Nehru moved Objectives Resolution.", "ta": "தவறு. நேரு குறிக்கோள் தீர்மானத்தை முன்மொழிந்தார்."}
        },
        tip_en="Alladi Krishnaswami Ayyar = 'Preamble expresses what we had thought or dreamed so long'.",
        tip_ta="அல்லாடி கிருஷ்ணசாமி ஐயர் = 'நாம் இவ்வளவு காலம் சிந்தித்ததை அல்லது கனவு கண்டதை முகவுரை வெளிப்படுத்துகிறது'.",
        rev_en="Alladi Krishnaswami Ayyar = Expresses what we dreamed so long.",
        rev_ta="அல்லாடி கிருஷ்ணசாமி ஐயர் = நாம் கனவு கண்டதை வெளிப்படுத்துகிறது.",
        sources=["Preamble Notes Part 1"],
        bloom="Remember", est_sec=30, pyq_sim="High", tags=["Alladi Krishnaswami Ayyar", "Preamble Quotes"]
    ))

    # Q35 - Conceptual Distinction - Ans C
    qs.append(make_medium_q(
        q_id="PRE_M_035", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="Conceptual Distinction",
        q_en="Which statement correctly distinguishes between 'Formal Equality' and 'Substantive Equality' in Indian constitutional law?",
        q_ta="இந்திய அரசியலமைப்புச் சட்டத்தில் 'முறையான சமத்துவம்' மற்றும் 'பொருள்சார்ந்த சமத்துவம்' ஆகியவற்றைச் சரியாக வேறுபடுத்தும் கூற்று எது?",
        opts_en=[
            "Formal Equality is in Part IV DPSP, whereas Substantive Equality is in Preamble.",
            "Formal Equality applies only to corporations, whereas Substantive Equality applies to individuals.",
            "Formal Equality treats everyone identically regardless of background (equal law for all), whereas Substantive Equality recognizes real socio-economic inequalities and allows protective discrimination / affirmative action to bring disadvantaged groups to an equal starting line.",
            "Formal Equality was added in 1976, whereas Substantive Equality was deleted in 1978."
        ],
        opts_ta=[
            "முறையான சமத்துவம் பகுதி IV DPSP இல் உள்ளது; ஆனால் பொருள்சார்ந்த சமத்துவம் முகவுரையில் உள்ளது.",
            "முறையான சமத்துவம் நிறுவனங்களுக்கு மட்டுமே பொருந்தும்; ஆனால் பொருள்சார்ந்த சமத்துவம் தனிநபர்களுக்குப் பொருந்தும்.",
            "முறையான சமத்துவம் பின்னணியைப் பொருட்படுத்தாமல் அனைவரையும் ஒரே மாதிரியாக நடத்துகிறது (அனைவருக்கும் சமமான சட்டம்); ஆனால் பொருள்சார்ந்த சமத்துவம் உண்மையான சமூக-பொருளாதார சமத்துவமின்மைகளை அங்கீகரித்து, பாதிக்கப்பட்ட குழுக்களை சமமான தொடக்கக் கோட்டிற்கு கொண்டு வரப் பாதுகாப்பு பாகுபாடு / சாதகமான நடவடிக்கையை அனுமதிக்கிறது.",
            "முறையான சமத்துவம் 1976 இல் சேர்க்கப்பட்டது; ஆனால் பொருள்சார்ந்த சமத்துவம் 1978 இல் நீக்கப்பட்டது."
        ],
        correct_ans="C",
        exp_en="Indian Constitutional Equality is Substantive: Article 14 permits reasonable classification among equals and unequals cannot be treated equally. Affirmative action (Arts 15(4), 16(4)) achieves substantive equality.",
        exp_ta="இந்திய அரசியலமைப்பு சமத்துவம் பொருள்சார்ந்தது: உறுப்பு 14 சமமானவர்களிடையே நியாயமான வகைப்பாட்டை அனுமதிக்கிறது மற்றும் சமமற்றவர்களை சமமாக நடத்த முடியாது. சாதகமான நடவடிக்கை பொருள்சார்ந்த சமத்துவத்தை அடைகிறது.",
        wno_dict={
            "A": {"en": "Incorrect. Both concepts pervade Part III Articles 14-18.", "ta": "தவறு. இரு கருத்துக்களும் பகுதி III இல் ஊடுருவியுள்ளன."},
            "B": {"en": "Incorrect. Article 14 applies to persons (including corporations).", "ta": "தவறு. உறுப்பு 14 நபர்களுக்குப் பொருந்தும்."},
            "C": {"en": "Correct. Formal = identical treatment; Substantive = affirmative action to equalize starting line.", "ta": "சரி. முறையான = ஒரே மாதிரி நடத்துதல்; பொருள்சார்ந்தது = தொடக்கக் கோட்டை சமமாக்க சாதகமான நடவடிக்கை."},
            "D": {"en": "Incorrect. Neither was added or deleted by these amendments.", "ta": "தவறு. இந்த திருத்தங்களால் இரண்டும் சேர்க்கப்படவோ நீக்கப்படவோ இல்லை."}
        },
        tip_en="Substantive Equality in India = Permits Affirmative Action / Reservation (Articles 15(4) & 16(4)).",
        tip_ta="இந்தியாவில் பொருள்சார்ந்த சமத்துவம் = சாதகமான நடவடிக்கை / இடஒதுக்கீட்டை అనుమதிக்கிறது (உறுப்புகள் 15(4) & 16(4)).",
        rev_en="Substantive Equality allows affirmative action for disadvantaged groups.",
        rev_ta="பொருள்சார்ந்த சமத்துவம் பாதிக்கப்பட்ட குழுக்களுக்கு சாதகமான நடவடிக்கையை அனுமதிக்கிறது.",
        sources=["Preamble Notes Part 1"],
        bloom="Understand", est_sec=45, pyq_sim="High", tags=["Substantive Equality", "Formal Equality", "Affirmative Action"]
    ))

    # Q36 - Application / Inference - Ans B
    qs.append(make_medium_q(
        q_id="PRE_M_036", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="Application / Inference",
        q_en="In a case involving an executive order prohibiting religious assemblies of a minority community, how does the Supreme Court evaluate the order against the Preamble's declaration of 'Secularism' and 'Liberty of Faith & Worship'?",
        q_ta="ஒரு சிறுபான்மை சமூகத்தின் மதக் கூட்டங்களைத் தடை செய்யும் ஒரு நிர்வாக ஆணையை உள்ளடக்கிய வழக்கில், முகவுரையின் 'மதச்சார்பின்மை' மற்றும் 'நம்பிக்கை & வழிபாட்டுச் சுதந்திரம்' பிரகடனத்திற்கு எதிராக உச்ச நீதிமன்றம் அந்த ஆணையை எவ்வாறு மதிப்பிடுகிறது?",
        opts_en=[
            "The SC automatically upholds the executive order because executive discretion is supreme.",
            "The SC strikes down the order if it violates the fundamental right under Article 25, using the Preamble's ideals of Secularism and Liberty of Worship to interpret Article 25's protection.",
            "The SC refers the matter to foreign religious bodies.",
            "The SC converts the minority community into a political party."
        ],
        opts_ta=[
            "நிர்வாக விருப்ப அதிகாரம் மேலானது என்பதால் உச்ச நீதிமன்றம் நிர்வாக ஆணையை தானாகவே உறுதி செய்கிறது.",
            "நிர்வாக ஆணை உறுப்பு 25 இன் கீழ் உள்ள அடிப்படை உரிமையை மீறினால், உறுப்பு 25 இன் பாதுகாப்பை விளக்க முகவுரையின் மதச்சார்பின்மை மற்றும் வழிபாட்டுச் சுதந்திர தத்துவங்களைப் பயன்படுத்தி நீதிமன்றம் அந்த ஆணையை ரத்து செய்கிறது.",
            "உச்ச நீதிமன்றம் இந்த விஷயத்தை வெளிநாட்டு மத அமைப்புகளுக்கு அனுப்புகிறது.",
            "உச்ச நீதிமன்றம் சிறுபான்மை சமூகத்தை ஒரு அரசியல் கட்சியாக மாற்றுகிறது."
        ],
        correct_ans="B",
        exp_en="The Supreme Court will evaluate the order against Article 25 (Right to Freedom of Religion), using the Preamble's ideals of Secularism and Liberty of Worship to interpret and protect religious freedom.",
        exp_ta="உச்ச நீதிமன்றம் அந்த ஆணையை உறுப்பு 25க்கு (மத சுதந்திர உரிமை) எதிராக மதிப்பிடும், மேலும் மத சுதந்திரத்தைப் பாதுகாக்கவும் விளக்கமளிக்கவும் முகவுரையின் மதச்சார்பின்மை மற்றும் வழிபாட்டுச் சுதந்திர தத்துவங்களைப் பயன்படுத்தும்.",
        wno_dict={
            "A": {"en": "Incorrect. Executive orders are subject to judicial review under Part III.", "ta": "தவறு. நிர்வாக ஆணைகள் பகுதி III இன் கீழ் நீதிப் புனராய்விற்கு உட்பட்டவை."},
            "B": {"en": "Correct. Strikes down unsecular order violating Art 25 using Preamble ideals as interpretive aid.", "ta": "சரி. முகவுரை தத்துவங்களை விளக்க உதவியாகப் பயன்படுத்தி உறுப்பு 25 ஐ மீறும் மதச்சார்பற்ற ஆணையை ரத்து செய்கிறது."},
            "C": {"en": "Incorrect. Foreign bodies have no constitutional jurisdiction.", "ta": "தவறு. வெளிநாட்டு அமைப்புகளுக்கு அரசியலமைப்பு அதிகார வரம்பு இல்லை."},
            "D": {"en": "Incorrect. Irrelevant claim.", "ta": "தவறு. தொடர்பற்ற கூற்று."}
        },
        tip_en="Preamble Secularism and Liberty of Worship guide the enforcement of Fundamental Rights under Article 25.",
        tip_ta="முகவுரையின் மதச்சார்பின்மை மற்றும் வழிபாட்டுச் சுதந்திரம் உறுப்பு 25 இன் கீழ் அடிப்படை உரிமைகள் அமலாக்கத்திற்கு வழிகாட்டுகின்றன.",
        rev_en="Preamble Secularism & Liberty ideals interpret Article 25 protections.",
        rev_ta="முகவுரையின் மதச்சார்பின்மை & சுதந்திர தத்துவங்கள் உறுப்பு 25 பாதுகாப்புகளுக்கு விளக்கமளிக்கின்றன.",
        sources=["Preamble Notes Part 1 & 2"],
        bloom="Apply", est_sec=45, pyq_sim="High", tags=["Secularism", "Liberty of Worship", "Article 25"]
    ))


    # Q37 - Direct - Ans A
    qs.append(make_medium_q(
        q_id="PRE_M_037", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="Direct",
        q_en="Which constitutional committee officially recommended the addition of Fundamental Duties, which reinforced the Preamble's goals of Fraternity and National Integrity in 1976?",
        q_ta="1976 இல் முகவுரையின் சகோதரத்துவம் மற்றும் தேசிய ஒருமைப்பாடு இலக்குகளை வலுப்படுத்திய அடிப்படை கடமைகளைச் சேர்க்க எந்த அரசியலமைப்புக் குழு அதிகாரப்பூர்வமாகப் பரிந்துரைத்தது?",
        opts_en=[
            "Swaran Singh Committee",
            "Sarkaria Commission",
            "M.N. Venkatachaliah Commission",
            "Kothari Commission"
        ],
        opts_ta=[
            "ஸ்வரன் சிங் குழு (Swaran Singh Committee)",
            "சர்க்காரியா ஆணையம்",
            "எம்.என். வெங்கடாசலையா ஆணையம்",
            "கொத்தாரி ஆணையம்"
        ],
        correct_ans="A",
        exp_en="The Swaran Singh Committee set up in 1976 recommended the inclusion of Fundamental Duties (Part IVA, Article 51A) to instill civic responsibility and national integrity.",
        exp_ta="1976 இல் அமைக்கப்பட்ட ஸ்வரன் சிங் குழு குடிமைப் பொறுப்பையும் தேசிய ஒருமைப்பாட்டையும் வளர்க்க அடிப்படை கடமைகளைச் (பகுதி IVA, உறுப்பு 51A) சேர்க்கப் பரிந்துரைத்தது.",
        wno_dict={
            "A": {"en": "Correct. Swaran Singh Committee recommended Fundamental Duties.", "ta": "சரி. ஸ்வரன் சிங் குழு அடிப்படை கடமைகளைப் பரிந்துரைத்தது."},
            "B": {"en": "Incorrect. Sarkaria Commission was Centre-State relations (1983).", "ta": "தவறு. சர்க்காரியா ஆணையம் மத்திய-மாநில உறவுகள் (1983)."},
            "C": {"en": "Incorrect. NCRWC was 2000.", "ta": "தவறு. வெங்கடாசலையா ஆணையம் 2000."},
            "D": {"en": "Incorrect. Kothari Commission was Education (1964).", "ta": "தவறு. கொத்தாரி ஆணையம் கல்வி (1964)."}
        },
        tip_en="Swaran Singh Committee (1976) = Recommended Fundamental Duties in Part IVA.",
        tip_ta="ஸ்வரன் சிங் குழு (1976) = பகுதி IVA இல் அடிப்படை கடமைகளைப் பரிந்துரைத்தது.",
        rev_en="Swaran Singh Committee 1976 = Recommended Fundamental Duties.",
        rev_ta="ஸ்வரன் சிங் குழு 1976 = அடிப்படை கடமைகளைப் பரிந்துரைத்தது.",
        sources=["Preamble Notes Part 1 & 2"],
        bloom="Remember", est_sec=30, pyq_sim="Direct PYQ", tags=["Swaran Singh Committee", "Fundamental Duties"]
    ))

    # Q38 - Conceptual Distinction - Ans B
    qs.append(make_medium_q(
        q_id="PRE_M_038", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="Conceptual Distinction",
        q_en="Which statement correctly distinguishes 'Liberty of Thought and Expression' in the Preamble from Fundamental Rights under Article 19(1)(a)?",
        q_ta="முகவுரையில் உள்ள 'சிந்தனை மற்றும் வெளிப்பாட்டுச் சுதந்திரத்தை' உறுப்பு 19(1)(a) இன் கீழ் உள்ள அடிப்படை உரிமையிலிருந்து சரியாக வேறுபடுத்தும் கூற்று எது?",
        opts_en=[
            "Preamble Liberty is justiciable under Article 32, whereas Article 19(1)(a) is non-justiciable.",
            "Preamble states the overarching philosophical objective of Liberty, whereas Article 19(1)(a) provides the specific, enforceable legal right subject to reasonable restrictions under Article 19(2).",
            "Preamble Liberty applies only during war, whereas Article 19(1)(a) applies during peace.",
            "Article 19(1)(a) was added by 42nd Amendment, whereas Preamble Liberty was present in 1950."
        ],
        opts_ta=[
            "முகவுரை சுதந்திரம் உறுப்பு 32 இன் கீழ் நிலைநிறுத்தக்கூடியது; ஆனால் உறுப்பு 19(1)(a) நிலைநிறுத்த முடியாதது.",
            "முகவுரை சுதந்திரத்தின் ஒட்டுமொத்த தத்துவ இலக்கைக் கூறுகிறது; ஆனால் உறுப்பு 19(1)(a) உறுப்பு 19(2) இன் கீழ் நியாயமான கட்டுப்பாடுகளுக்கு உட்பட்ட নির্দিষ্ট, அமல்படுத்தத்தக்க சட்ட உரிமையை வழங்குகிறது.",
            "முகவுரை சுதந்திரம் போர்க்காலத்தில் மட்டுமே பொருந்தும்; ஆனால் உறுப்பு 19(1)(a) அமைதிக்காலத்தில் பொருந்தும்.",
            "உறுப்பு 19(1)(a) 42வது திருத்தத்தால் சேர்க்கப்பட்டது; ஆனால் முகவுரை சுதந்திரம் 1950 இல் இருந்தது."
        ],
        correct_ans="B",
        exp_en="Preamble expresses the grand philosophical ideal of Liberty. Article 19(1)(a) translates that ideal into an enforceable, justiciable Fundamental Right bounded by reasonable restrictions in Art 19(2).",
        exp_ta="முகவுரை சுதந்திரத்தின் பெரும் தத்துவ லட்சியத்தை வெளிப்படுத்துகிறது. உறுப்பு 19(1)(a) அந்த லட்சியத்தை உறுப்பு 19(2) இல் நியாயமான கட்டுப்பாடுகளுக்கு உட்பட்ட அமல்படுத்தத்தக்க அடிப்படை உரிமையாக மாற்றுகிறது.",
        wno_dict={
            "A": {"en": "Incorrect. Reverses justiciability attributes.", "ta": "தவறு. நிலைநிறுத்தும் பண்புகளை தலைகீழாக மாற்றுகிறது."},
            "B": {"en": "Correct. Preamble = Philosophical goal; Article 19(1)(a) = Enforceable legal right with Art 19(2) restrictions.", "ta": "சரி. முகவுரை = தத்துவ இலக்கு; உறுப்பு 19(1)(a) = உறுப்பு 19(2) கட்டுப்பாடுகளுடன் அமல்படுத்தத்தக்க சட்ட உரிமை."},
            "C": {"en": "Incorrect. Both apply during peacetime.", "ta": "தவறு. இரண்டும் அமைதிக்காலத்தில் பொருந்தும்."},
            "D": {"en": "Incorrect. Article 19(1)(a) was present in original 1950 Constitution.", "ta": "தவறு. உறுப்பு 19(1)(a) 1950 அசல் அரசியலமைப்பில் இருந்தது."}
        },
        tip_en="Preamble Liberty = Grand Ideal; Article 19(1)(a) = Enforceable Right bounded by Article 19(2) restrictions.",
        tip_ta="முகவுரை சுதந்திரம் = பெரும் லட்சியம்; உறுப்பு 19(1)(a) = உறுப்பு 19(2) கட்டுப்பாடுகளுடன் அமல்படுத்தத்தக்க உரிமை.",
        rev_en="Preamble Liberty (Ideal) vs Article 19(1)(a) (Enforceable Right).",
        rev_ta="முகவுரை சுதந்திரம் (லட்சியம்) vs உறுப்பு 19(1)(a) (அமல்படுத்தத்தக்க உரிமை).",
        sources=["Preamble Notes Part 1"],
        bloom="Understand", est_sec=45, pyq_sim="High", tags=["Liberty of Thought", "Article 19", "Reasonable Restrictions"]
    ))

    # Q39 - Constitutional Relationship - Ans C
    qs.append(make_medium_q(
        q_id="PRE_M_039", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="Constitutional Relationship",
        q_en="How does the abolition of Untouchability under Article 17 serve the Preamble's twin goals of 'Equality of Status' and 'Fraternity assuring the Dignity of the Individual'?",
        q_ta="உறுப்பு 17 இன் கீழ் தீண்டாமை ஒழிப்பு முகவுரையின் 'தகுதி சமத்துவம்' மற்றும் 'தனிமனித கண்ணியத்தை உறுதி செய்யும் சகோதரத்துவம்' ஆகிய இரட்டை இலக்குகளுக்கு எவ்வாறு சேவையாற்றுகிறது?",
        opts_en=[
            "Article 17 grants financial subsidies to high-caste landowners.",
            "Article 17 creates separate electoral rolls for scheduled castes.",
            "Article 17 abolishes an ancient social stigma, restoring human dignity to historically marginalized citizens and establishing equal social status necessary for true brotherhood.",
            "Article 17 restricts lower-caste citizens from entering civil service."
        ],
        opts_ta=[
            "உறுப்பு 17 உயர் சாதி நில உரிமையாளர்களுக்கு நிதி மானியங்களை வழங்குகிறது.",
            "உறுப்பு 17 பட்டியல் சாதிகளுக்கு தனி வாக்காளர் பட்டியலை உருவாக்குகிறது.",
            "உறுப்பு 17 ஒரு பழங்கால சமூகக் கறையை ஒழித்து, வரலாற்று ரீதியாக ஓரங்கட்டப்பட்ட குடிமக்களுக்கு மனித கண்ணியத்தை மீட்டுத் தருகிறது மற்றும் உண்மையான சகோதரத்துவத்திற்குத் தேவையான சமமான சமூக அந்தஸ்தை நிறுவுகிறது.",
            "உறுப்பு 17 தாழ்த்தப்பட்ட குடிமக்கள் சிவில் சர்வீசில் சேருவதைத் தடுக்கிறது."
        ],
        correct_ans="C",
        exp_en="Article 17 (Abolition of Untouchability) is a vital constitutional tool enforcing Social Equality (Preamble) and establishing Dignity of Individual and Fraternity by eradicating a humiliating social practice.",
        exp_ta="உறுப்பு 17 (தீண்டாமை ஒழிப்பு) ஒரு அவமானகரமான சமூக நடைமுறையை ஒழிப்பதன் மூலம் சமூக சமத்துவத்தையும் (முகவுரை) தனிமனித கண்ணியத்தையும் சகோதரத்துவத்தையும் நிறுவும் ஒரு முக்கிய அரசியலமைப்பு கருவியாகும்.",
        wno_dict={
            "A": {"en": "Incorrect. Article 17 abolishes untouchability, not grant subsidies.", "ta": "தவறு. உறுப்பு 17 தீண்டாமையை ஒழிக்கிறது."},
            "B": {"en": "Incorrect. Joint electorate was retained.", "ta": "தவறு. கூட்டு வாக்காளர் முறை தக்கவைக்கப்பட்டது."},
            "C": {"en": "Correct. Eradicates social stigma, restoring human dignity and equality of status.", "ta": "சரி. சமூகக் கறையை ஒழித்து, மனித கண்ணியத்தையும் தகுதி சமத்துவத்தையும் மீட்கிறது."},
            "D": {"en": "Incorrect. Article 16 guarantees equal opportunity in public employment.", "ta": "தவறு. உறுப்பு 16 பொது வேலைவாய்ப்பில் சம வாய்ப்பை உத்தரவாதம் செய்கிறது."}
        },
        tip_en="Article 17 (Abolition of Untouchability) directly operationalizes Preamble's Social Justice, Equality of Status, and Dignity of Individual.",
        tip_ta="உறுப்பு 17 (தீண்டாமை ஒழிப்பு) முகவுரையின் சமூக நீதி, தகுதி சமத்துவம் மற்றும் தனிமனித கண்ணியத்தை நேரடியாக நடைமுறைப்படுத்துகிறது.",
        rev_en="Article 17 enforces Social Justice, Equality of Status, and Dignity of Individual.",
        rev_ta="உறுப்பு 17 சமூக நீதி, தகுதி சமத்துவம் மற்றும் தனிமனித கண்ணியத்தை அமல்படுத்துகிறது.",
        sources=["Preamble Notes Part 1"],
        bloom="Analyze", est_sec=45, pyq_sim="High", tags=["Article 17", "Untouchability", "Dignity of Individual"]
    ))

    # Q40 - Direct - Ans D
    qs.append(make_medium_q(
        q_id="PRE_M_040", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="Direct",
        q_en="Which of the following constitutional provisions abolished hereditary titles (except military and academic distinctions), directly fulfilling the Preamble's ideal of 'Equality of Status'?",
        q_ta="முகவுரையின் 'தகுதி சமத்துவம்' லட்சியத்தை நேரடியாக நிறைவேற்றும் வகையில் பின்வரும் அரசியலமைப்பு விதிகளில் எது பரம்பரைப் பட்டங்களை (இராணுவ மற்றும் கல்விச் சிறப்புப் பட்டங்கள் தவிர) ஒழித்தது?",
        opts_en=["Article 14", "Article 15", "Article 17", "Article 18"],
        opts_ta=["உறுப்பு 14", "உறுப்பு 15", "உறுப்பு 17", "உறுப்பு 18"],
        correct_ans="D",
        exp_en="Article 18 abolishes titles (like Maharaja, Rai Bahadur, Knight) to ensure no privileged class exists, directly establishing Equality of Status as declared in the Preamble.",
        exp_ta="உறுப்பு 18 பட்டங்களை (மகாராஜா, ராய் பகதூர் போன்றவை) ஒழித்து எந்தவொரு சலுகை பெற்ற வகுப்பும் இல்லை என்பதை உறுதி செய்கிறது, முகவுரையில் பிரகடனப்படுத்தப்பட்ட தகுதி சமத்துவத்தை நேரடியாக நிறுவுகிறது.",
        wno_dict={
            "A": {"en": "Incorrect. Article 14 is Equality before Law.", "ta": "தவறு. உறுப்பு 14 சட்டத்தின் முன் சமத்துவம்."},
            "B": {"en": "Incorrect. Article 15 is Prohibition of Discrimination.", "ta": "தவறு. உறுப்பு 15 பாகுபாடின்மை."},
            "C": {"en": "Incorrect. Article 17 is Abolition of Untouchability.", "ta": "தவறு. உறுப்பு 17 தீண்டாமை ஒழிப்பு."},
            "D": {"en": "Correct. Article 18 abolishes titles to maintain equality of status.", "ta": "சரி. உறுப்பு 18 தகுதி சமத்துவத்தைப் பராமரிக்க பட்டங்களை ஒழிக்கிறது."}
        },
        tip_en="Article 18 = Abolition of Titles (ensures Equality of Status in Preamble).",
        tip_ta="உறுப்பு 18 = பட்டங்கள் ஒழிப்பு (முகவுரையில் தகுதி சமத்துவத்தை உறுதி செய்கிறது).",
        rev_en="Article 18 = Abolition of Titles (Status Equality).",
        rev_ta="உறுப்பு 18 = பட்டங்கள் ஒழிப்பு (தகுதி சமத்துவம்).",
        sources=["Preamble Notes Part 1"],
        bloom="Remember", est_sec=30, pyq_sim="Direct PYQ", tags=["Article 18", "Abolition of Titles", "Equality of Status"]
    ))

    # Q41 - Conceptual Distinction - Ans A
    qs.append(make_medium_q(
        q_id="PRE_M_041", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="Conceptual Distinction",
        q_en="Which statement correctly contrasts the 'Source of Authority' in the Preamble with the 'Source of Authority' in pre-independence Government of India Acts (1919/1935)?",
        q_ta="முகவுரையில் உள்ள 'அதிகார மூலம்' என்பதை சுதந்திரத்திற்கு முந்தைய இந்திய அரசுச் சட்டங்களில் (1919/1935) உள்ள 'அதிகார மூலத்துடன்' சரியாக வேறுபடுத்தும் கூற்று எது?",
        opts_en=[
            "Preamble derives authority from 'WE, THE PEOPLE OF INDIA' (Popular Sovereignty), whereas GOI Acts 1919/1935 derived authority from the British Crown and Parliament.",
            "Preamble derives authority from the British Privy Council, whereas GOI Acts derived authority from local Panchayats.",
            "Preamble derives authority from United Nations, whereas GOI Acts derived authority from US Congress.",
            "Preamble derives authority from Supreme Court, whereas GOI Acts derived authority from Viceroy alone."
        ],
        opts_ta=[
            "முகவுரை 'இந்திய மக்களாகிய நாம்' என்பவரிடமிருந்து அதிகாரத்தைப் பெறுகிறது (மக்களின் இறையாண்மை); ஆனால் 1919/1935 இந்திய அரசுச் சட்டங்கள் பிரிட்டிஷ் முடிசூட்டு அதிகாரம் மற்றும் நாடாளுமன்றத்திலிருந்து அதிகாரத்தைப் பெற்றன.",
            "முகவுரை பிரிட்டிஷ் பிரிவி கவுன்சிலிடமிருந்து அதிகாரத்தைப் பெறுகிறது; ஆனால் இந்திய அரசுச் சட்டங்கள் உள்ளூர் பஞ்சாயத்துகளிலிருந்து அதிகாரத்தைப் பெற்றன.",
            "முகவுரை ஐக்கிய நாடுகளிடமிருந்து அதிகாரத்தைப் பெறுகிறது; ஆனால் இந்திய அரசுச் சட்டங்கள் அமெரிக்க காங்கிரஸிடமிருந்து அதிகாரத்தைப் பெற்றன.",
            "முகவுரை உச்ச நீதிமன்றத்திலிருந்து அதிகாரத்தைப் பெறுகிறது; ஆனால் இந்திய அரசுச் சட்டங்கள் வைஸ்ராயிடமிருந்து மட்டுமே அதிகாரத்தைப் பெற்றன."
        ],
        correct_ans="A",
        exp_en="GOI Acts 1919 and 1935 were enactments of the Imperial British Parliament deriving authority from the King-in-Parliament. The 1950 Preamble marks an indigenous break, deriving authority from the sovereign Indian People.",
        exp_ta="1919 மற்றும் 1935 இந்திய அரசுச் சட்டங்கள் பிரிட்டிஷ் பாராளுமன்றத்தின் சட்டங்களாகும், அவை அரசரிடமிருந்து அதிகாரத்தைப் பெற்றன. 1950 முகவுரை ஒரு உள்நாட்டுத் திருப்புமுனையாகும், இது இறையாண்மை கொண்ட இந்திய மக்களிடமிருந்து அதிகாரத்தைப் பெறுகிறது.",
        wno_dict={
            "A": {"en": "Correct. Preamble = People of India (Popular Sovereignty); GOI Acts = British Crown/Parliament.", "ta": "சரி. முகவுரை = இந்திய மக்கள்; இந்திய அரசுச் சட்டங்கள் = பிரிட்டிஷ் ஆட்சி/பாராளுமன்றம்."},
            "B": {"en": "Incorrect. Reverses historical origins.", "ta": "தவறு. வரலாற்று மூலங்களைத் தலைகீழாக மாற்றுகிறது."},
            "C": {"en": "Incorrect. Absurd international bodies claim.", "ta": "தவறு. பொருத்தமற்ற சர்வதேச அமைப்புகள் கூற்று."},
            "D": {"en": "Incorrect. Supreme Court did not exist in 1935 in present form.", "ta": "தவறு. உச்ச நீதிமன்றம் 1935 இல் தற்போதைய வடிவில் இல்லை."}
        },
        tip_en="Source of Authority: GOI Acts 1919/1935 = British Parliament; Indian Constitution 1950 = WE, THE PEOPLE OF INDIA.",
        tip_ta="அதிகார மூலம்: இந்திய அரசுச் சட்டங்கள் 1919/1935 = பிரிட்டிஷ் பாராளுமன்றம்; இந்திய அரசியலமைப்பு 1950 = இந்திய மக்களாகிய நாம்.",
        rev_en="Authority source shifted from British Crown to Indian People.",
        rev_ta="அதிகார மூலம் பிரிட்டிஷ் ஆட்சியிலிருந்து இந்திய மக்களுக்கு மாறியது.",
        sources=["Preamble Notes Part 1"],
        bloom="Understand", est_sec=45, pyq_sim="High", tags=["Source of Authority", "Popular Sovereignty", "GOI Acts"]
    ))

    # Q42 - Application / Inference - Ans B
    qs.append(make_medium_q(
        q_id="PRE_M_042", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="Application / Inference",
        q_en="Suppose a state government enacts a law banning citizens from speaking any language other than the state official language in public spaces. Which Preamble principles and Fundamental Rights are violated by this law?",
        q_ta="ஒரு மாநில அரசு பொது இடங்களில் மாநில அதிகாரப்பூர்வ மொழியைத் தவிர வேறு எந்த மொழியையும் குடிமக்கள் பேசுவதைத் தடை செய்யும் ஒரு சட்டத்தை இயற்றுகிறது எனக் கொள்வோம். இந்தச் சட்டத்தால் எந்த முகவுரைக் கோட்பாடுகள் மற்றும் அடிப்படை உரிமைகள் மீறப்படுகின்றன?",
        opts_en=[
            "Violates only Article 368 amendment procedures.",
            "Violates Preamble's 'Liberty of Thought & Expression' and 'Fraternity assuring Dignity of Individual', alongside Article 19(1)(a) (Freedom of Speech) and Article 29 (Linguistic Rights).",
            "Violates only President's Emergency powers under Article 352.",
            "Violates no constitutional principle because states have absolute sovereignty over language."
        ],
        opts_ta=[
            "உறுப்பு 368 திருத்த நடைமுறைகளை மட்டுமே மீறுகிறது.",
            "முகவுரையின் 'சிந்தனை & வெளிப்பாட்டுச் சுதந்திரம்' மற்றும் 'தனிமனித கண்ணியத்தை உறுதி செய்யும் சகோதரத்துவம்', அத்துடன் உறுப்பு 19(1)(a) (பேச்சு சுதந்திரம்) மற்றும் உறுப்பு 29 (மொழி உரிமைகள்) ஆகியவற்றை மீறுகிறது.",
            "உறுப்பு 352 இன் கீழ் குடியரசுத் தலைவரின் அவசரகால அதிகாரங்களை மட்டுமே மீறுகிறது.",
            "மாநிலங்களுக்கு மொழி மீது பூரண இறையாண்மை இருப்பதால் எந்த அரசியலமைப்புக் கோட்பாட்டையும் மீறவில்லை."
        ],
        correct_ans="B",
        exp_en="Banning minority language speech violates Preamble's Liberty of Thought & Expression and Fraternity/Dignity, while directly breaching justiciable FRs under Art 19(1)(a) and Art 29.",
        exp_ta="சிறுபான்மை மொழிப் பேச்சைத் தடை செய்வது முகவுரையின் சிந்தனை & வெளிப்பாட்டுச் சுதந்திரத்தையும் சகோதரத்துவம்/கண்ணியத்தையும் மீறுகிறது, அதே நேரத்தில் உறுப்பு 19(1)(a) மற்றும் உறுப்பு 29 இன் கீழ் உள்ள நிலைநிறுத்தக்கூடிய அடிப்படை உரிமைகளை நேரடியாக மீறுகிறது.",
        wno_dict={
            "A": {"en": "Incorrect. Article 368 is parliamentary amendment procedure.", "ta": "தவறு. உறுப்பு 368 நாடாளுமன்ற திருத்த நடைமுறை."},
            "B": {"en": "Correct. Violates Preamble Liberty/Fraternity + FR Arts 19(1)(a) and 29.", "ta": "சரி. முகவுரை சுதந்திரம்/சகோதரத்துவம் + FR உறுப்புகள் 19(1)(a) மற்றும் 29 ஐ மீறுகிறது."},
            "C": {"en": "Incorrect. Emergency provisions irrelevant to language ban.", "ta": "தவறு. அவசரகால விதிகள் மொழித் தடைக்கு தொடர்பற்றவை."},
            "D": {"en": "Incorrect. States do not possess absolute sovereignty; bound by FRs.", "ta": "தவறு. மாநிலங்களுக்கு பூரண இறையாண்மை இல்லை."}
        },
        tip_en="Preamble Liberty of Expression & Fraternity guide the enforcement of Article 19(1)(a) and Article 29.",
        tip_ta="முகவுரையின் வெளிப்பாட்டுச் சுதந்திரம் & சகோதரத்துவம் உறுப்புகள் 19(1)(a) மற்றும் 29 அமலாக்கத்திற்கு வழிகாட்டுகின்றன.",
        rev_en="Preamble Liberty & Fraternity support Art 19(1)(a) & Art 29 protections.",
        rev_ta="முகவுரை சுதந்திரம் & சகோதரத்துவம் உறுப்புகள் 19(1)(a) & 29 பாதுகாப்புகளுக்கு ஆதரவளிக்கின்றன.",
        sources=["Preamble Notes Part 1"],
        bloom="Apply", est_sec=45, pyq_sim="High", tags=["Liberty of Expression", "Article 19", "Article 29"]
    ))

    # Q43 - Case-law - Ans C
    qs.append(make_medium_q(
        q_id="PRE_M_043", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="Case-law Based",
        q_en="What primary takeaway did the Supreme Court establish in the A.K. Gopalan Case (1950) regarding the Preamble, which was later modified in the Maneka Gandhi Case (1978)?",
        q_ta="ஏ.கே. கோபாலன் வழக்கில் (1950) முகவுரை தொடர்பாக உச்ச நீதிமன்றம் நிறுவிய முதன்மை செய்தி என்ன, அது பின்னர் மேனகா காந்தி வழக்கில் (1978) மாற்றியமைக்கப்பட்டது?",
        opts_en=[
            "In 1950, the SC held that Preamble could amend Fundamental Rights directly.",
            "In 1950, the SC held that Preamble was justiciable under Article 32.",
            "In 1950, the SC took a literal view holding that Preamble ideals cannot be used to expand the clear, literal text of Article 21 ('procedure established by law'); which was later broadened in 1978.",
            "In 1950, the SC declared Preamble unconstitutional."
        ],
        opts_ta=[
            "1950 இல், முகவுரை அடிப்படை உரிமைகளை நேரடியாகத் திருத்த முடியும் என உச்ச நீதிமன்றம் கூறியது.",
            "1950 இல், முகவுரை உறுப்பு 32 இன் கீழ் நிலைநிறுத்தக்கூடியது என உச்ச நீதிமன்றம் கூறியது.",
            "1950 இல், உறுப்பு 21 இன் ('சட்டத்தால் நிறுவப்பட்ட நடைமுறை') தெளிவான, நேரடி உரையை விரிவாக்க முகவுரை லட்சியங்களைப் பயன்படுத்த முடியாது என்ற எழுத்துவழிப் பார்வையை உச்ச நீதிமன்றம் எடுத்தது; அது பின்னர் 1978 இல் அகலப்படுத்தப்பட்டது.",
            "1950 இல், முகவுரை அரசியலமைப்பிற்கு முரணானது என உச்ச நீதிமன்றம் அறிவித்தது."
        ],
        correct_ans="C",
        exp_en="In AK Gopalan (1950), SC took a strict literalist view refusing to read Preamble's 'Liberty' into Art 21. In Maneka Gandhi (1978), SC reversed this narrow view, using Preamble ideals to infuse 'Due Process' into Art 21.",
        exp_ta="ஏகே கோபாலன் (1950) வழக்கில், உச்ச நீதிமன்றம் உறுப்பு 21 இல் முகவுரையின் 'சுதந்திரத்தை' ஓத மறுத்து ஒரு கடுமையான எழுத்துவழிப் பார்வையை எடுத்தது. மேனகா காந்தி (1978) வழக்கில், உச்ச நீதிமன்றம் இந்த குறுகிய பார்வையை மாற்றி, உறுப்பு 21 இல் 'சட்டத்தின் உரிய நடைமுறையை' இணைக்க முகவுரை தத்துவங்களைப் பயன்படுத்தியது.",
        wno_dict={
            "A": {"en": "Incorrect. Preamble cannot amend FRs.", "ta": "தவறு. முகவுரை FR ஐ திருத்த முடியாது."},
            "B": {"en": "Incorrect. Preamble was not held justiciable.", "ta": "தவறு. முகவுரை நிலைநிறுத்தக்கூடியதாகக் கொள்ளப்படவில்லை."},
            "C": {"en": "Correct. AK Gopalan (1950) literalist view -> Maneka Gandhi (1978) holistic view using Preamble.", "ta": "சரி. ஏகே கோபாலன் (1950) எழுத்துவழி பார்வை -> மேனகா காந்தி (1978) முகவுரையைப் பயன்படுத்திய ஒட்டுமொத்த பார்வை."},
            "D": {"en": "Incorrect. Absurd claim.", "ta": "தவறு. பொருத்தமற்ற கூற்று."}
        },
        tip_en="Evolution: AK Gopalan (1950) narrow literal interpretation -> Maneka Gandhi (1978) wide Preamble-guided interpretation.",
        tip_ta="வளர்ச்சி: ஏகே கோபாலன் (1950) குறுகிய எழுத்துவழி விளக்கம் -> மேனகா காந்தி (1978) முகவுரை வழிகாட்டப்பட்ட அகன்ற விளக்கம்.",
        rev_en="AK Gopalan (1950) narrow view vs Maneka Gandhi (1978) broad view using Preamble.",
        rev_ta="ஏகே கோபாலன் (1950) குறுகிய பார்வை vs மேனகா காந்தி (1978) முகவுரை வழிகாட்டப்பட்ட அகன்ற பார்வை.",
        sources=["Preamble Notes Part 2"],
        bloom="Understand", est_sec=45, pyq_sim="High", tags=["AK Gopalan Case", "Maneka Gandhi Case", "Article 21 Evolution"]
    ))

    # Q44 - Direct - Ans D
    qs.append(make_medium_q(
        q_id="PRE_M_044", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="Direct",
        q_en="Which of the following describes the correct status of the Preamble in comparison with Constitutional Provisions in terms of legal force?",
        q_ta="சட்டப்பூர்வ ஆற்றலின் அடிப்படையில் அரசியலமைப்பு விதிகளுடன் ஒப்பிடும்போது முகவுரையின் சரியான அந்தஸ்தை விவரிப்பது எது?",
        opts_en=[
            "Preamble overrides Constitutional Provisions during judicial conflict.",
            "Preamble is justiciable, whereas Constitutional Provisions are non-justiciable.",
            "Preamble provides independent legislative authority to the President.",
            "Preamble expresses grand philosophy and serves as an interpretive aid, whereas Operative Constitutional Provisions contain enforceable legal rules and establish governmental powers."
        ],
        opts_ta=[
            "நீதிமன்ற மோதலின் போது முகவுரை அரசியலமைப்பு விதிகளை மேலெழுதுகிறது.",
            "முகவுரை நிலைநிறுத்தக்கூடியது; ஆனால் அரசியலமைப்பு விதிகள் நிலைநிறுத்த முடியாதவை.",
            "முகவுரை குடியரசுத் தலைவருக்கு சுதந்திரமான சட்டமன்ற அதிகாரத்தை வழங்குகிறது.",
            "முகவுரை பெரும் தத்துவத்தை வெளிப்படுத்தி ஒரு விளக்கமளிக்கும் உதவியாகச் செயல்படுகிறது; ஆனால் செயல்படும் அரசியலமைப்பு விதிகள் அமல்படுத்தத்தக்க சட்ட விதிகளைக் கொண்டுள்ளன மற்றும் அரசு அதிகாரங்களை நிறுவுகின்றன."
        ],
        correct_ans="D",
        exp_en="Comparison Table Rule: Preamble = Introductory philosophy & interpretive guide; Operative Provisions (Parts III-XXII) = Enforceable legal rules, powers, and institutional mechanisms.",
        exp_ta="ஒப்பீட்டு அட்டவணை விதி: முகவுரை = அறிமுகத் தத்துவம் & விளக்கமளிக்கும் வழிகாட்டி; செயல்படும் விதிகள் (பகுதிகள் III-XXII) = அமல்படுத்தத்தக்க சட்ட விதிகள், அதிகாரங்கள் மற்றும் நிறுவன அமைப்புகள்.",
        wno_dict={
            "A": {"en": "Incorrect. Operative provisions prevail when clear.", "ta": "தவறு. தெளிவான செயல்படும் விதிகளே வெல்லும்."},
            "B": {"en": "Incorrect. Reverses justiciability.", "ta": "தவறு. நிலைநிறுத்தும் தன்மையைத் தலைகீழாக மாற்றுகிறது."},
            "C": {"en": "Incorrect. Preamble confers no legislative power.", "ta": "தவறு. முகவுரை எந்த சட்டமன்ற அதிகாரத்தையும் தராது."},
            "D": {"en": "Correct. Accurately contrasts Preamble philosophy with operative legal provisions.", "ta": "சரி. முகவுரை தத்துவத்தை செயல்படும் சட்ட விதிகளுடன் துல்லியமாக வேறுபடுத்துகிறது."}
        },
        tip_en="Preamble = Philosophy & Interpretive Aid; Operative Provisions = Legal Rules & Governmental Powers.",
        tip_ta="முகவுரை = தத்துவம் & விளக்கமளிக்கும் உதவி; செயல்படும் விதிகள் = சட்ட விதிகள் & அரசு அதிகாரங்கள்.",
        rev_en="Preamble (Philosophy) vs Operative Provisions (Legal rules & powers).",
        rev_ta="முகவுரை (தத்துவம்) vs செயல்படும் விதிகள் (சட்ட விதிகள் & அதிகாரங்கள்).",
        sources=["Preamble Notes Part 2"],
        bloom="Remember", est_sec=30, pyq_sim="High", tags=["Preamble vs Operative Provisions", "Legal Force"]
    ))

    # Q45 - Conceptual Distinction - Ans A
    qs.append(make_medium_q(
        q_id="PRE_M_045", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="Conceptual Distinction",
        q_en="Which statement correctly distinguishes between 'Unity of the Nation' and 'Integrity of the Nation'?",
        q_ta="தேசத்தின் ஒற்றுமை' (Unity) மற்றும் 'தேசத்தின் ஒருமைப்பாடு' (Integrity) ஆகியவற்றைச் சரியாக வேறுபடுத்தும் கூற்று எது?",
        opts_en=[
            "Unity reflects the psychological and emotional integration of diverse citizens into one nation, whereas Integrity reflects the physical and territorial indivisibility of the Indian State.",
            "Unity applies only to states, whereas Integrity applies only to Union Territories.",
            "Unity was added in 1976, whereas Integrity was present in 1950.",
            "Unity is justiciable, whereas Integrity is non-justiciable."
        ],
        opts_ta=[
            "ஒற்றுமை என்பது வெவ்வேறு குடிமக்களின் உளவியல் மற்றும் உணர்வுப்பூர்வமான ஒருமைப்பாட்டை வெளிப்படுத்துகிறது; ஆனால் ஒருமைப்பாடு என்பது இந்திய அரசின் பௌதிக மற்றும் நிலப்பரப்பு பிரிக்க முடியாத தன்மையைப் பிரதிபலிக்கிறது.",
            "ஒற்றுமை மாநிலங்களுக்கு மட்டுமே பொருந்தும்; ஆனால் ஒருமைப்பாடு ஒன்றிய பிரதேசங்களுக்கு மட்டுமே பொருந்தும்.",
            "ஒற்றுமை 1976 இல் சேர்க்கப்பட்டது; ஆனால் ஒருமைப்பாடு 1950 இல் இருந்தது.",
            "ஒற்றுமை நிலைநிறுத்தக்கூடியது; ஆனால் ஒருமைப்பாடு நிலைநிறுத்த முடியாதது."
        ],
        correct_ans="A",
        exp_en="Unity is a socio-psychological concept (feeling of common nationhood among people). Integrity is a territorial/geographical concept (indivisibility of the national territory countering secession).",
        exp_ta="ஒற்றுமை என்பது ஒரு சமூக-உளவியல் கருத்தாகும் (மக்களிடையே பொதுவான தேசிய உணர்வு). ஒருமைப்பாடு என்பது நிலப்பரப்பு/புவியியல் கருத்தாகும் (பிரிவினைவாதத்தை எதிர்க்கும் தேசிய நிலப்பரப்பின் பிரிக்க முடியாத தன்மை).",
        wno_dict={
            "A": {"en": "Correct. Unity = Emotional/Psychological bond; Integrity = Territorial indivisibility.", "ta": "சரி. ஒற்றுமை = உணர்வுப்பூர்வ/உளவியல் பிணைப்பு; ஒருமைப்பாடு = நிலப்பரப்பு பிரிக்க முடியாத தன்மை."},
            "B": {"en": "Incorrect. Both apply to the entire Republic.", "ta": "தவறு. இரண்டும் முழு குடியரசுக்கும் பொருந்தும்."},
            "C": {"en": "Incorrect. 'Unity' was in original Preamble; 'Integrity' was added in 1976.", "ta": "தவறு. 'ஒற்றுமை' அசல் முகவுரையில் இருந்தது; 'ஒருமைப்பாடு' 1976 இல் சேர்க்கப்பட்டது."},
            "D": {"en": "Incorrect. Both are non-justiciable Preamble goals.", "ta": "தவறு. இரண்டும் நிலைநிறுத்த முடியாத முகவுரை இலக்குகள்."}
        },
        tip_en="Unity = Psychological Integration; Integrity (added 1976) = Territorial Indivisibility.",
        tip_ta="ஒற்றுமை = உளவியல் ஒருமைப்பாடு; ஒருமைப்பாடு (1976 இல் சேர்க்கப்பட்டது) = நிலப்பரப்பு பிரிக்க முடியாத தன்மை.",
        rev_en="Unity (Psychological bond) vs Integrity (Territorial indivisibility).",
        rev_ta="ஒற்றுமை (உளவியல் பிணைப்பு) vs ஒருமைப்பாடு (நிலப்பரப்பு பிரிக்க முடியாத தன்மை).",
        sources=["Preamble Notes Part 1 & 2"],
        bloom="Understand", est_sec=45, pyq_sim="High", tags=["Unity vs Integrity", "Conceptual Distinction"]
    ))

    # Q46 - Application / Inference - Ans B
    qs.append(make_medium_q(
        q_id="PRE_M_046", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="Application / Inference",
        q_en="In a situation where Parliament passes a Constitutional Amendment under Article 368 attempting to convert India into a hereditary Monarchy, what will be the ruling of the Supreme Court?",
        q_ta="இந்தியாவை ஒரு பரம்பரை முடியாட்சியாக மாற்ற முயற்சிக்கும் ஒரு அரசியலமைப்பு திருத்தத்தை உறுப்பு 368 இன் கீழ் நாடாளுமன்றம் நிறைவேற்றும் ஒரு சூழலில், உச்ச நீதிமன்றத்தின் தீர்ப்பு என்னவாக இருக்கும்?",
        opts_en=[
            "The Court will uphold the amendment because Parliament has unlimited power under Article 368.",
            "The Court will strike down the amendment as unconstitutional for violating the 'Republic' principle which forms part of the unamendable Basic Structure of the Constitution.",
            "The Court will ask the President to decide independently without judicial intervention.",
            "The Court will refer the amendment to the British Parliament for approval."
        ],
        opts_ta=[
            "உறுப்பு 368 இன் கீழ் நாடாளுமன்றத்திற்கு வரம்பற்ற அதிகாரம் இருப்பதால் நீதிமன்றம் திருத்தத்தை உறுதி செய்யும்.",
            "அரசியலமைப்பின் திருத்த முடியாத அடிப்படை அமைப்பின் ஒரு பகுதியாக விளங்கும் 'குடியரசு' கோட்பாட்டை மீறியதற்காக நீதிமன்றம் அத்திருத்தத்தை அரசியலமைப்பிற்கு முரணானது என ரத்து செய்யும்.",
            "நீதிமன்றத் தலையீடின்றி குடியரசுத் தலைவரைச் சுதந்திரமாகத் தீர்மானிக்க நீதிமன்றம் கேட்கும்.",
            "நீதிமன்றம் திருத்தத்தை ஒப்புதலுக்காக பிரிட்டிஷ் பாராளுமன்றத்திற்கு அனுப்பும்."
        ],
        correct_ans="B",
        exp_en="Under Basic Structure Doctrine (Kesavananda 1973), 'Republican nature of Indian polity' is an essential basic feature. Parliament cannot delete or alter Republican form to Monarchy.",
        exp_ta="அடிப்படை கட்டமைப்பு கோட்பாட்டின் கீழ் (கேசவாநந்தா 1973), 'இந்திய அரசின் குடியரசுத் தன்மை' ஒரு இன்றியமையாத அடிப்படை அம்சமாகும். நாடாளுமன்றம் குடியரசு வடிவத்தை நீக்கவோ முடியாட்சியாக மாற்றவோ முடியாது.",
        wno_dict={
            "A": {"en": "Incorrect. Parliament's power under Art 368 is limited by Basic Structure.", "ta": "தவறு. நாடாளுமன்ற அதிகாரம் அடிப்படை அமைப்பால் வரம்பிற்குட்பட்டது."},
            "B": {"en": "Correct. Republic is part of Basic Structure; any amendment destroying it is void.", "ta": "சரி. குடியரசு அடிப்படை அமைப்பின் பகுதி; அதை அழிக்கும் எந்தத் திருத்தமும் செல்லாது."},
            "C": {"en": "Incorrect. Judiciary has supreme power of judicial review.", "ta": "தவறு. நீதித்துறைக்கு உச்சபட்ச நீதிப் புனராய்வு அதிகாரம் உள்ளது."},
            "D": {"en": "Incorrect. Absurd foreign reference.", "ta": "தவறு. பொருத்தமற்ற வெளிநாட்டுப் பரிந்துரை."}
        },
        tip_en="Republican nature of Indian Polity = Unamendable Basic Structure feature.",
        tip_ta="இந்திய அரசின் குடியரசுத் தன்மை = திருத்த முடியாத அடிப்படை கட்டமைப்பு அம்சம்.",
        rev_en="Republic nature is part of untouchable Basic Structure.",
        rev_ta="குடியரசுத் தன்மை தொட முடியாத அடிப்படை அமைப்பின் பகுதியாகும்.",
        sources=["Preamble Notes Part 1 & 2"],
        bloom="Apply", est_sec=45, pyq_sim="High", tags=["Republic", "Basic Structure", "Article 368 Limitation"]
    ))

    # Q47 - Direct - Ans C
    qs.append(make_medium_q(
        q_id="PRE_M_047", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="Direct",
        q_en="Which Constituent Assembly President's ruling officially settled that the motion 'The Preamble stands part of the Constitution' was adopted by the Assembly?",
        q_ta="முகவுரை அரசியலமைப்பின் ஒரு பகுதியாக அமைகிறது' என்ற தீர்மானம் சபையால் ஏற்றுக்கொள்ளப்பட்டது என்பதை அதிகாரப்பூர்வமாகத் தீர்த்த அரசியலமைப்புச் சபைத் தலைவர் யார்?",
        opts_en=["Dr. B.R. Ambedkar", "Pandit Jawaharlal Nehru", "Dr. Rajendra Prasad", "K.M. Munshi"],
        opts_ta=["டாக்டர் பி.ஆர். அம்பேத்கர்", "பண்டிட் ஜவஹர்லால் நேரு", "டாக்டர் ராஜேந்திர பிரசாத்", "கே.எம். முன்ஷி"],
        correct_ans="C",
        exp_en="Dr. Rajendra Prasad, President of the Constituent Assembly, put the motion to vote: 'The question is that the Preamble stands part of the Constitution.' The motion was adopted.",
        exp_ta="அரசியலமைப்புச் சபையின் தலைவரான டாக்டர் ராஜேந்திர பிரசாத் தீர்மானத்தை வாக்களிப்பிற்கு விட்டார்: 'கேள்வி என்னவென்றால், முகவுரை அரசியலமைப்பின் ஒரு பகுதியாக அமைகிறது என்பதாகும்.' இத்தீர்மானம் ஏற்றுக்கொள்ளப்பட்டது.",
        wno_dict={
            "A": {"en": "Incorrect. Dr. Ambedkar was Chairman of Drafting Committee.", "ta": "தவறு. அம்பேத்கர் வரைவுக் குழுத் தலைவர்."},
            "B": {"en": "Incorrect. Nehru moved Objectives Resolution.", "ta": "தவறு. நேரு குறிக்கோள் தீர்மானத்தை முன்மொழிந்தார்."},
            "C": {"en": "Correct. Dr. Rajendra Prasad was Assembly President who put the motion to vote.", "ta": "சரி. டாக்டர் ராஜேந்திர பிரசாத் சபாத்தலைவராக தீர்மானத்தை வாக்களிப்பிற்கு விட்டார்."},
            "D": {"en": "Incorrect. K.M. Munshi was a member of Drafting Committee.", "ta": "தவறு. கே.எம். முன்ஷி வரைவுக் குழு உறுப்பினர்."}
        },
        tip_en="Dr. Rajendra Prasad put the motion: 'The Preamble stands part of the Constitution' which was adopted by the Assembly.",
        tip_ta="டாக்டர் ராஜேந்திர பிரசாத் 'முகவுரை அரசியலமைப்பின் ஒரு பகுதியாக அமைகிறது' என்ற தீர்மானத்தை வாக்களிப்பிற்கு விட்டு நிறைவேற்றினார்.",
        rev_en="Dr. Rajendra Prasad put Preamble adoption motion to Constituent Assembly vote.",
        rev_ta="டாக்டர் ராஜேந்திர பிரசாத் முகவுரை ஏற்புத் தீர்மானத்தை சபை வாக்களிப்பிற்கு விட்டார்.",
        sources=["Preamble Notes Part 1 & 2"],
        bloom="Remember", est_sec=30, pyq_sim="High", tags=["Dr Rajendra Prasad", "Assembly Voting", "Preamble Adoption"]
    ))

    # Q48 - TNPSC Trap - Ans D
    qs.append(make_medium_q(
        q_id="PRE_M_048", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="TNPSC Trap",
        q_en="Which of the following is a FALSE statement regarding the legal nature of the Preamble?",
        q_ta="முகவுரையின் சட்டப்பூர்வத் தன்மை தொடர்பான பின்வரும் கூற்றுகளில் எது தவறான கூற்று?",
        opts_en=[
            "Preamble is part of the Constitution according to Kesavananda Bharati Case (1973).",
            "Preamble can be amended under Article 368 subject to Basic Structure limits.",
            "Preamble is an interpretive aid when constitutional articles are ambiguous.",
            "Preamble acts as an independent prohibition preventing Parliament from levying new taxes."
        ],
        opts_ta=[
            "கேசவாநந்த பாரதி வழக்கின்படி (1973) முகவுரை அரசியலமைப்பின் ஒரு பகுதியாகும்.",
            "அடிப்படை கட்டமைப்பு வரம்புகளுக்கு உட்பட்டு உறுப்பு 368 இன் கீழ் முகவுரையைத் திருத்த முடியும்.",
            "அரசியலமைப்புச் சரத்துகள் தெளிவற்றதாக இருக்கும் போது முகவுரை ஒரு விளக்கமளிக்கும் உதவியாக அமைகிறது.",
            "நாடாளுமன்றம் புதிய வரிகளை விதிப்பதைத் தடுக்கும் ஒரு சுதந்திரமான தடையாக முகவுரை செயல்படுகிறது."
        ],
        correct_ans="D",
        exp_en="Statement D is FALSE because the Supreme Court explicitly held that the Preamble is NEITHER a source of power NOR a prohibition/limitation upon legislative powers (including tax powers).",
        exp_ta="கூற்று D தவறானது, ஏனெனில் உச்ச நீதிமன்றம் முகவுரை சட்டமன்ற அதிகாரங்கள் மீதான (வரி அதிகாரங்கள் உட்பட) அதிகார மூலமும் அல்ல, தடையும் அல்ல என்று வெளிப்படையாகத் தீர்ப்பளித்துள்ளது.",
        wno_dict={
            "A": {"en": "Incorrect statement choice. Statement A is TRUE.", "ta": "தவறு. கூற்று A சரி."},
            "B": {"en": "Incorrect statement choice. Statement B is TRUE.", "ta": "தவறு. கூற்று B சரி."},
            "C": {"en": "Incorrect statement choice. Statement C is TRUE.", "ta": "தவறு. கூற்று C சரி."},
            "D": {"en": "Correct statement choice (this statement is FALSE). Preamble is NOT a prohibition on legislative tax power.", "ta": "சரி (இந்தக் கூற்று தவறானது). முகவுரை சட்டமன்ற வரி அதிகாரம் மீதான தடை அல்ல."}
        },
        tip_en="TNPSC Trap: Preamble imposes NO prohibition/limitation on legislative powers.",
        tip_ta="TNPSC பொறி: முகவுரை சட்டமன்ற அதிகாரங்கள் மீது எந்தவொரு தடையையும்/வரம்பையும் விதிக்காது.",
        rev_en="Preamble is not a source of power or restriction on legislature.",
        rev_ta="முகவுரை அதிகார மூலமும் அல்ல, சட்டமன்றத்தின் மீதான தடையும் அல்ல.",
        sources=["Preamble Notes Part 2"],
        bloom="Understand", est_sec=45, pyq_sim="High", tags=["Prohibition on Power", "Legal Nature", "TNPSC Trap"]
    ))

    # Q49 - Conceptual Distinction - Ans A
    qs.append(make_medium_q(
        q_id="PRE_M_049", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="Conceptual Distinction",
        q_en="Which statement correctly contrasts the 'Source of Authority' in the Preamble with the 'Objectives' in the Preamble?",
        q_ta="முகவுரையில் உள்ள 'அதிகார மூலம்' என்பதை முகவுரையில் உள்ள 'இலக்குகளுடன்' சரியாக வேறுபடுத்தும் கூற்று எது?",
        opts_en=[
            "Source of Authority declares WHERE power comes from ('WE, THE PEOPLE OF INDIA'), whereas Objectives declare WHAT goals the Constitution seeks to achieve (Justice, Liberty, Equality, Fraternity).",
            "Source of Authority declares the date of adoption, whereas Objectives declare the name of the Prime Minister.",
            "Source of Authority is justiciable, whereas Objectives are non-justiciable.",
            "Source of Authority was added in 1976, whereas Objectives were adopted in 1950."
        ],
        opts_ta=[
            "அதிகார மூலம் அதிகாரம் எங்கிருந்து வருகிறது என்பதைப் பிரகடனம் செய்கிறது ('இந்திய மக்களாகிய நாம்'); ஆனால் இலக்குகள் அரசியலமைப்பு அடைய விரும்பும் இலக்குகளைப் பிரகடனம் செய்கின்றன (நீதி, சுதந்திரம், சமத்துவம், சகோதரத்துவம்).",
            "அதிகார மூலம் ஏற்றுக்கொள்ளப்பட்ட தேதியை அறிவிக்கிறது; ஆனால் இலக்குகள் பிரதமரின் பெயரை அறிவிக்கின்றன.",
            "அதிகார மூலம் நிலைநிறுத்தக்கூடியது; ஆனால் இலக்குகள் நிலைநிறுத்த முடியாதவை.",
            "அதிகார மூலம் 1976 இல் சேர்க்கப்பட்டது; ஆனால் இலக்குகள் 1950 இல் ஏற்றுக்கொள்ளப்பட்டன."
        ],
        correct_ans="A",
        exp_en="Preamble components: 1. Source of Authority = People of India. 2. Nature of State = Sovereign Socialist Secular Democratic Republic. 3. Objectives = Justice, Liberty, Equality, Fraternity. 4. Date = 26 Nov 1949.",
        exp_ta="முகவுரை கூறுகள்: 1. அதிகார மூலம் = இந்திய மக்கள். 2. அரசின் தன்மை = இறையாண்மை சமதர்ம மதச்சார்பற்ற ஜனநாயக குடியரசு. 3. இலக்குகள் = நீதி, சுதந்திரம், சமத்துவம், சகோதரத்துவம். 4. நாள் = 26 நவம்பர் 1949.",
        wno_dict={
            "A": {"en": "Correct. Source = Where power originates ('We the People'); Objectives = Goals to achieve (J-L-E-F).", "ta": "சரி. மூலம் = அதிகாரம் உருவாகுமிடம்; இலக்குகள் = அடைய விரும்பும் கோள்கள்."},
            "B": {"en": "Incorrect. PM name is not in Preamble.", "ta": "தவறு. பிரதமர் பெயர் முகவுரையில் இல்லை."},
            "C": {"en": "Incorrect. Both are parts of the non-justiciable Preamble.", "ta": "தவறு. இரண்டும் நிலைநிறுத்த முடியாத முகவுரையின் பகுதிகள்."},
            "D": {"en": "Incorrect. Both were present in original 1950 text.", "ta": "தவறு. இரண்டும் 1950 அசல் உரையில் இருந்தன."}
        },
        tip_en="4 Components of Preamble: Source of Authority, Nature of State, Statement of Objectives, Date of Adoption.",
        tip_ta="முகவுரையின் 4 கூறுகள்: அதிகார மூலம், அரசின் தன்மை, இலக்குகளின் அறிக்கை, ஏற்றுக்கொள்ளப்பட்ட நாள்.",
        rev_en="Source = We the People vs Objectives = Justice, Liberty, Equality, Fraternity.",
        rev_ta="மூலம் = மக்களாகிய நாம் vs இலக்குகள் = நீதி, சுதந்திரம், சமத்துவம், சகோதரத்துவம்.",
        sources=["Preamble Notes Part 1"],
        bloom="Understand", est_sec=45, pyq_sim="High", tags=["Source of Authority", "Objectives", "Preamble Components"]
    ))

    # Q50 - Conceptual Distinction - Ans B
    qs.append(make_medium_q(
        q_id="PRE_M_050", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="Conceptual Distinction",
        q_en="What is the ultimate synthesis of the Preamble's grand vision as described by Dr. B.R. Ambedkar in the Constituent Assembly?",
        q_ta="அரசியலமைப்புச் சபையில் டாக்டர் பி.ஆர். அம்பேத்கர் விவரித்தவாறு முகவுரையின் பெரும் தொலைநோக்கின் இறுதித் தொகுப்பு எது?",
        opts_en=[
            "Political democracy is completely independent of social democracy.",
            "Political democracy cannot last unless there lies at the base of it Social Democracy, which recognizes Liberty, Equality, and Fraternity as a union of trinity.",
            "Economic growth must precede political democracy by fifty years.",
            "Fraternity can be enforced by police powers alone."
        ],
        opts_ta=[
            "அரசியல் ஜனநாயகம் சமூக ஜனநாயகத்திலிருந்து முற்றிலும் சுதந்திரமானது.",
            "சுதந்திரம், சமத்துவம் மற்றும் சகோதரத்துவத்தை ஒரு முக்கூட்டு ஒன்றியமாக அங்கீகரிக்கும் சமூக ஜனநாயகம் அதன் அடித்தளமாக இல்லாவிட்டால் அரசியல் ஜனநாயகம் நீடிக்க முடியாது.",
            "பொருளாதார வளர்ச்சி அரசியல் ஜனநாயகத்திற்கு ஐம்பது ஆண்டுகள் முன்பே வர வேண்டும்.",
            "சகோதரத்துவத்தைக் காவல் அதிகாரங்களால் மட்டுமே அமல்படுத்த முடியும்."
        ],
        correct_ans="B",
        exp_en="Dr. B.R. Ambedkar stressed: 'Political democracy cannot last unless there lies at the base of it social democracy... Liberty, Equality, Fraternity form a union of trinity in the sense that to divorce one from the other is to defeat the very purpose of democracy.'",
        exp_ta="டாக்டர் பி.ஆர். அம்பேத்கர் வலியுறுத்தினார்: 'அதன் அடித்தளத்தில் சமூக ஜனநாயகம் இல்லாவிட்டால் அரசியல் ஜனநாயகம் நீடிக்க முடியாது... சுதந்திரம், சமத்துவம், சகோதரத்துவம் ஆகியவை ஒரு முக்கூட்டு ஒன்றியத்தை உருவாக்குகின்றன, ஒன்றிலிருந்து மற்றொன்றைப் பிரிப்பது ஜனநாயகத்தின் நோக்கத்தையே தோற்கடிப்பதாகும்.'",
        wno_dict={
            "A": {"en": "Incorrect. Ambedkar insisted they are inseparable.", "ta": "தவறு. அவை பிரிக்க முடியாதவை என்று அம்பேத்கர் வலியுறுத்தினார்."},
            "B": {"en": "Correct. Political democracy rests on Social Democracy; Liberty, Equality, Fraternity form a Trinity.", "ta": "சரி. அரசியல் ஜனநாயகம் சமூக ஜனநாயகத்தில் உள்ளது; சுதந்திரம், சமத்துவம், சகோதரத்துவம் முக்கூட்டு ஒன்றியம்."},
            "C": {"en": "Incorrect. Irrelevant quote.", "ta": "தவறு. தொடர்பற்ற மேற்கோள்."},
            "D": {"en": "Incorrect. Fraternity is a moral and constitutional bond.", "ta": "தவறு. சகோதரத்துவம் ஒரு நெறிமுறைப் பிணைப்பு."}
        },
        tip_en="Ambedkar's Trinity: Liberty, Equality, Fraternity are inseparable components of Social Democracy.",
        tip_ta="அம்பேத்கரின் முக்கூட்டு: சுதந்திரம், சமத்துவம், சகோதரத்துவம் ஆகியவை சமூக ஜனநாயகத்தின் பிரிக்க முடியாத கூறுகள்.",
        rev_en="Ambedkar: Political Democracy rests on Social Democracy (Liberty, Equality, Fraternity Trinity).",
        rev_ta="அம்பேத்கர்: அரசியல் ஜனநாயகம் சமூக ஜனநாயகத்தில் இயங்குகிறது (சுதந்திரம், சமத்துவம், சகோதரத்துவ முக்கூட்டு).",
        sources=["Preamble Notes Part 1"],
        bloom="Understand", est_sec=45, pyq_sim="High", tags=["Ambedkar", "Social Democracy", "Trinity of Liberty Equality Fraternity"]
    ))

    return qs
