# preamble_easy_q26_50.py
from scratch_preamble_easy_helper import make_q

def get_q26_50():
    qs = []

    # Q26 - Conceptual - Ans B
    qs.append(make_q(
        q_id="PRE_E_026", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="Conceptual",
        q_en="Is the Preamble of the Indian Constitution justiciable in courts of law?",
        q_ta="இந்திய அரசியலமைப்பின் முகவுரை நீதிமன்றங்களில் நிலைநிறுத்தக்கூடியதா (justiciable)?",
        opts_en=[
            "Yes, it can be enforced directly under Article 32.",
            "No, it is non-justiciable and its provisions are not directly enforceable in courts.",
            "Yes, but only during Financial Emergency.",
            "Yes, but only in High Courts under Article 226."
        ],
        opts_ta=[
            "ஆம், இதை உறுப்பு 32 இன் கீழ் நேரடியாக அமல்படுத்தலாம்.",
            "இல்லை, இது நீதிமன்றத்தால் நிலைநிறுத்த முடியாதது (non-justiciable) மற்றும் இதன் விதிகளை நீதிமன்றங்களில் நேரடியாக அமல்படுத்த முடியாது.",
            "ஆம், ஆனால் நிதி அவசரநிலையின் போது மட்டுமே.",
            "ஆம், ஆனால் உறுப்பு 226 இன் கீழ் உயர் நீதிமன்றங்களில் மட்டுமே."
        ],
        correct_ans="B",
        exp_en="The Preamble is NON-JUSTICIABLE. Its provisions are not enforceable in courts of law directly. A writ cannot be filed solely for Preamble violation.",
        exp_ta="முகவுரை நீதிமன்றத்தால் நிலைநிறுத்த முடியாதது. இதன் விதிகளை நீதிமன்றங்களில் நேரடியாக அமல்படுத்த முடியாது. முகவுரை மீறலுக்காக மட்டும் பேராணை மனு தாக்கல் செய்ய முடியாது.",
        wno_dict={
            "A": {"en": "Incorrect. Fundamental Rights are justiciable under Art 32, not Preamble alone.", "ta": "தவறு. அடிப்படை உரிமைகளே நிலைநிறுத்தக்கூடியவை."},
            "B": {"en": "Correct. Preamble is non-justiciable.", "ta": "சரி. முகவுரை நீதிமன்றத்தால் நிலைநிறுத்த முடியாதது."},
            "C": {"en": "Incorrect. Emergency does not make Preamble justiciable.", "ta": "தவறு. அவசரநிலை இதை மாற்றாது."},
            "D": {"en": "Incorrect. Not justiciable in High Courts either.", "ta": "தவறு. உயர் நீதிமன்றங்களிலும் முடியாது."}
        },
        tip_en="TNPSC Trap: Preamble is NON-JUSTICIABLE (just like DPSPs and Fundamental Duties).",
        tip_ta="TNPSC பொறி: முகவுரை நீதிமன்றத்தால் நிலைநிறுத்த முடியாதது (DPSP மற்றும் அடிப்படை கடமைகள் போல).",
        rev_en="Preamble = Non-justiciable in courts.",
        rev_ta="முகவுரை = நீதிமன்றத்தால் நிலைநிறுத்த முடியாதது.",
        sources=["Preamble Notes Part 2"],
        bloom="Understand", est_sec=30, pyq_sim="High", tags=["Justiciability", "Non-justiciable"]
    ))

    # Q27 - Conceptual - Ans C
    qs.append(make_q(
        q_id="PRE_E_027", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="Conceptual",
        q_en="Which of the following correctly describes the legal role of the Preamble regarding legislative power?",
        q_ta="சட்டமன்ற அதிகாரம் தொடர்பாக முகவுரையின் சட்டப்பூர்வ பணியை பின்வருவனவற்றில் எது சரியாக விவரிக்கிறது?",
        opts_en=[
            "Preamble is an independent source of legislative power for Parliament.",
            "Preamble is an absolute prohibition on legislative powers.",
            "Preamble is NEITHER a source of power NOR a restriction upon the powers of the legislature.",
            "Preamble overrides clear provisions of Parliament acts."
        ],
        opts_ta=[
            "முகவுரை நாடாளுமன்றத்திற்கான ஒரு சுதந்திரமான சட்டமன்ற அதிகார மூலம் ஆகும்.",
            "முகவுரை சட்டமன்ற அதிகாரங்கள் மீதான ஒரு பூரண தடையாகும்.",
            "முகவுரை சட்டமன்றத்திற்கான அதிகார மூலமும் அல்ல, சட்டமன்ற அதிகாரங்கள் மீதான தடையும் அல்ல.",
            "நாடாளுமன்ற சட்டங்களின் தெளிவான விதிகளை முகவுரை மேலெழுதுகிறது."
        ],
        correct_ans="C",
        exp_en="The Supreme Court held that the Preamble is NEITHER a source of power to the legislature NOR a prohibition upon the powers of the legislature.",
        exp_ta="உச்ச நீதிமன்றம் முகவுரை சட்டமன்றத்திற்கான அதிகார மூலமும் அல்ல, சட்டமன்ற அதிகாரங்கள் மீதான தடையும் அல்ல என்று தீர்ப்பளித்தது.",
        wno_dict={
            "A": {"en": "Incorrect. Preamble confers no power.", "ta": "தவறு. முகவுரை எந்த அதிகாரத்தையும் வழங்காது."},
            "B": {"en": "Incorrect. Preamble is not a restriction.", "ta": "தவறு. முகவுரை கட்டுப்பாடு அல்ல."},
            "C": {"en": "Correct. Neither a source of power nor a restriction on power.", "ta": "சரி. அதிகார மூலமும் அல்ல, அதிகாரத் தடையும் அல்ல."},
            "D": {"en": "Incorrect. Operative provisions prevail when clear.", "ta": "தவறு. தெளிவான விதிகள் மட்டுமே வெல்லும்."}
        },
        tip_en="Preamble = NEITHER a source of power NOR a restriction on power.",
        tip_ta="முகவுரை = அதிகார மூலமும் அல்ல, அதிகாரத் தடையும் அல்ல.",
        rev_en="Preamble confers no power and imposes no prohibition.",
        rev_ta="முகவுரை அதிகாரமும் தராது, தடையும் விதிக்காது.",
        sources=["Preamble Notes Part 2"],
        bloom="Understand", est_sec=30, pyq_sim="High", tags=["Source of Power", "Legislative Power"]
    ))

    # Q28 - Term / Meaning - Ans D
    qs.append(make_q(
        q_id="PRE_E_028", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="Term / Meaning",
        q_en="When can courts refer to the Preamble as an 'Interpretive Guide'?",
        q_ta="நீதிமன்றங்கள் எப்போது முகவுரையை ஒரு 'விளக்கமளிக்கும் வழிகாட்டி'யாகப் பயன்படுத்தலாம்?",
        opts_en=[
            "In every criminal trial automatically.",
            "To invalidate clear and unambiguous constitutional articles.",
            "To create new Fundamental Rights without constitutional amendments.",
            "When the language of a constitutional article is ambiguous or capable of two interpretations."
        ],
        opts_ta=[
            "ஒவ்வொரு குற்றவியல் வழக்கிலும் தானாகவே.",
            "தெளிவான அரசியலமைப்புச் சரத்துகளைச் செல்லாததாக்க.",
            "அரசியலமைப்பு திருத்தம் இன்றி புதிய அடிப்படை உரிமைகளை உருவாக்க.",
            "ஒரு அரசியலமைப்புச் சரத்தின் மொழி தெளிவற்றதாக அல்லது இரண்டு விளக்கங்களுக்கு இடமளிப்பதாக இருக்கும் போது."
        ],
        correct_ans="D",
        exp_en="Courts use the Preamble as an Interpretive Aid ONLY when the wording of a constitutional provision is ambiguous or obscure.",
        exp_ta="நீதிமன்றங்கள் ஒரு அரசியலமைப்பு விதியின் சொற்கள் தெளிவற்றதாக அல்லது சந்தேகத்திற்குரியதாக இருக்கும் போது மட்டுமே முகவுரையை விளக்கமளிக்கும் உதவியாகப் பயன்படுத்துகின்றன.",
        wno_dict={
            "A": {"en": "Incorrect. Not automatic in criminal cases.", "ta": "தவறு. குற்றவியல் வழக்குகளில் தானாக வராது."},
            "B": {"en": "Incorrect. Cannot override clear text.", "ta": "தவறு. தெளிவான உரையை மேலெழுத முடியாது."},
            "C": {"en": "Incorrect. Cannot create FRs directly.", "ta": "தவறு. உரிமைகளை நேரடியாக உருவாக்க முடியாது."},
            "D": {"en": "Correct. Used during text ambiguity or obscurity.", "ta": "சரி. உரை தெளிவற்றதாக இருக்கும்போது பயன்படுத்தப்படுகிறது."}
        },
        tip_en="Preamble acts as Interpretive Aid ONLY during textual ambiguity.",
        tip_ta="உரை தெளிவற்றதாக இருக்கும்போது மட்டுமே முகவுரை வழிகாட்டியாக செயல்படும்.",
        rev_en="Interpretive Aid = Used during ambiguity in articles.",
        rev_ta="விளக்கமளிக்கும் வழிகாட்டி = தெளிவற்ற நிலைகளில் பயன்படுத்தப்படுகிறது.",
        sources=["Preamble Notes Part 2"],
        bloom="Understand", est_sec=30, pyq_sim="High", tags=["Interpretive Guide", "Ambiguity"]
    ))

    # Q29 - Direct - Ans A
    qs.append(make_q(
        q_id="PRE_E_029", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="Direct",
        q_en="Which word was added to the Fraternity section ('Unity and _____ of the Nation') by the 42nd Amendment Act 1976?",
        q_ta="42வது திருத்தச் சட்டம் 1976 மூலம் சகோதரத்துவப் பகுதியில் ('தேசத்தின் ஒற்றுமையும் _____') சேர்க்கப்பட்ட சொல் எது?",
        opts_en=["Integrity", "Sovereignty", "Secularism", "Dignity"],
        opts_ta=["ஒருமைப்பாடு (Integrity)", "இறையாண்மை (Sovereignty)", "மதச்சார்பின்மை (Secularism)", "கண்ணியம் (Dignity)"],
        correct_ans="A",
        exp_en="The 42nd Amendment Act 1976 added the word 'Integrity' to the Fraternity section, changing 'unity of the Nation' to 'unity and integrity of the Nation'.",
        exp_ta="42வது திருத்தச் சட்டம் 1976 சகோதரத்துவப் பகுதியில் 'ஒருமைப்பாடு' என்ற சொல்லைச் சேர்த்தது, 'தேசத்தின் ஒற்றுமை' என்பதை 'தேசத்தின் ஒற்றுமையும் ஒருமைப்பாடும்' என மாற்றியது.",
        wno_dict={
            "A": {"en": "Correct. Integrity was added in 1976.", "ta": "சரி. ஒருமைப்பாடு 1976 இல் சேர்க்கப்பட்டது."},
            "B": {"en": "Incorrect. Sovereignty was in original Preamble.", "ta": "தவறு. இறையாண்மை அசல் முகவுரையில் இருந்தது."},
            "C": {"en": "Incorrect. Secular was added in Nature of State section.", "ta": "தவறு. மதச்சார்பற்ற என்பது அரசின் தன்மையில் சேர்க்கப்பட்டது."},
            "D": {"en": "Incorrect. Dignity was in original Preamble.", "ta": "தவறு. கண்ணியம் அசல் முகவுரையில் இருந்தது."}
        },
        tip_en="TNPSC Trap: 'Integrity' was added to Fraternity section ('Unity and Integrity of the Nation').",
        tip_ta="TNPSC பொறி: 'ஒருமைப்பாடு' என்ற சொல் சகோதரத்துவப் பகுதியில் சேர்க்கப்பட்டது.",
        rev_en="Integrity added to 'Unity and Integrity of Nation' in 1976.",
        rev_ta="ஒருமைப்பாடு 1976 இல் 'தேசத்தின் ஒற்றுமையும் ஒருமைப்பாடும்' எனச் சேர்க்கப்பட்டது.",
        sources=["Preamble Notes Part 1 & 2"],
        bloom="Remember", est_sec=30, pyq_sim="High", tags=["Integrity", "42nd Amendment", "Fraternity"]
    ))

    # Q30 - Direct - Ans B
    qs.append(make_q(
        q_id="PRE_E_030", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="Direct",
        q_en="On which exact date did the 42nd Constitutional Amendment Act of 1976 come into force?",
        q_ta="1976 இன் 42வது அரசியலமைப்பு திருத்தச் சட்டம் எந்தத் துல்லியமான நாளில் நடைமுறைக்கு வந்தது?",
        opts_en=["26th November 1976", "3rd January 1977", "26th January 1977", "15th August 1976"],
        opts_ta=["26 நவம்பர் 1976", "3 ஜனவரி 1977", "26 ஜனவரி 1977", "15 ஆகஸ்ட் 1976"],
        correct_ans="B",
        exp_en="The 42nd Constitutional Amendment Act of 1976 came into force on 3rd January 1977.",
        exp_ta="1976 இன் 42வது அரசியலமைப்பு திருத்தச் சட்டம் 3 ஜனவரி 1977 அன்று நடைமுறைக்கு வந்தது.",
        wno_dict={
            "A": {"en": "Incorrect. 26 Nov is Constitution day.", "ta": "தவறு. 26 நவம்பர் அரசியலமைப்பு தினம்."},
            "B": {"en": "Correct. Enforced on 3rd January 1977.", "ta": "சரி. 3 ஜனவரி 1977 இல் அமலானது."},
            "C": {"en": "Incorrect. Incorrect date.", "ta": "தவறு. தவறான நாள்."},
            "D": {"en": "Incorrect. Incorrect date.", "ta": "தவறு. தவறான நாள்."}
        },
        tip_en="42nd Amendment 1976 Enforcement Date = 3rd January 1977.",
        tip_ta="42வது திருத்தம் 1976 நடைமுறைக்கு வந்த நாள் = 3 ஜனவரி 1977.",
        rev_en="42nd Amendment enforcement = 3rd January 1977.",
        rev_ta="42வது திருத்தம் அமலான நாள் = 3 ஜனவரி 1977.",
        sources=["Preamble Notes Part 2"],
        bloom="Remember", est_sec=30, pyq_sim="High", tags=["42nd Amendment", "Enforcement Date"]
    ))

    # Q31 - Conceptual - Ans C
    qs.append(make_q(
        q_id="PRE_E_031", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="Conceptual",
        q_en="In which landmark case did the Supreme Court hold that Secularism is part of the Basic Structure of the Constitution?",
        q_ta="எந்த வரலாற்றுச் சிறப்புமிக்க வழக்கில் மதச்சார்பின்மை என்பது அரசியலமைப்பின் அடிப்படை அமைப்பின் ஒரு பகுதி என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது?",
        opts_en=["Berubari Case (1960)", "Golaknath Case (1967)", "S.R. Bommai Case (1994)", "AK Gopalan Case (1950)"],
        opts_ta=["பெருபாரி வழக்கு (1960)", "கோலக்நாத் வழக்கு (1967)", "எஸ்.ஆர். பொம்மை வழக்கு (1994)", "ஏ.கே. கோபாலன் வழக்கு (1950)"],
        correct_ans="C",
        exp_en="In S.R. Bommai vs Union of India (1994), the Supreme Court held that Secularism is part of the Basic Structure of the Constitution.",
        exp_ta="எஸ்.ஆர். பொம்மை vs யூனியன் ஆஃப் இந்தியா (1994) வழக்கில் உச்ச நீதிமன்றம் மதச்சார்பின்மை அரசியலமைப்பின் அடிப்படை அமைப்பின் ஒரு பகுதி என்று தீர்ப்பளித்தது.",
        wno_dict={
            "A": {"en": "Incorrect. Berubari 1960 was about enclave transfer.", "ta": "தவறு. பெருபாரி வழக்கு நிலப்பரப்பு பரிமாற்றம் பற்றியது."},
            "B": {"en": "Incorrect. Golaknath was 1967.", "ta": "தவறு. கோலக்நாத் 1967."},
            "C": {"en": "Correct. S.R. Bommai Case 1994 declared Secularism as Basic Structure.", "ta": "சரி. எஸ்.ஆர். பொம்மை வழக்கு 1994 மதச்சார்பின்மையை அடிப்படை அமைப்பாக அறிவித்தது."},
            "D": {"en": "Incorrect. AK Gopalan was 1950.", "ta": "தவறு. ஏகே கோபாலன் 1950."}
        },
        tip_en="S.R. Bommai Case (1994) = Secularism & Federalism are Basic Structure.",
        tip_ta="எஸ்.ஆர். பொம்மை வழக்கு (1994) = மதச்சார்பின்மை & கூட்டாட்சி ஆகியவை அடிப்படை அமைப்பாகும்.",
        rev_en="SR Bommai Case 1994 = Secularism is Basic Structure.",
        rev_ta="எஸ்.ஆர். பொம்மை வழக்கு 1994 = மதச்சார்பின்மை அடிப்படை அமைப்பாகும்.",
        sources=["Preamble Notes Part 1 & 2"],
        bloom="Remember", est_sec=30, pyq_sim="High", tags=["SR Bommai Case", "Secularism", "Basic Structure"]
    ))

    # Q32 - Term / Meaning - Ans D
    qs.append(make_q(
        q_id="PRE_E_032", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="Term / Meaning",
        q_en="What does 'Political Justice' in the Preamble ensure to Indian citizens?",
        q_ta="முகவுரையில் உள்ள 'அரசியல் நீதி' (Political Justice) இந்தியக் குடிமக்களுக்கு எதனை உறுதி செய்கிறது?",
        opts_en=[
            "Free employment in government sector without qualifications.",
            "Exemption from all taxes.",
            "Ownership of all private banks by public.",
            "Equal political rights, equal access to political offices, and equal voice in government."
        ],
        opts_ta=[
            "தகுதியின்றி அரசுத் துறையில் இலவச வேலைவாய்ப்பு.",
            "அனைத்து வரிகளிலிருந்தும் விலக்கு.",
            "அனைத்து தனியார் வங்கிகளையும் பொதுமக்கள் உடைமையாக்குவது.",
            "சமமான அரசியல் உரிமைகள், அரசியல் பதவிகளுக்கு சமமான அணுகல் மற்றும் அரசாங்கத்தில் சமமான குரல்."
        ],
        correct_ans="D",
        exp_en="Political Justice ensures that all citizens have equal political rights, equal access to all political offices, and equal voice in the governance of the nation.",
        exp_ta="அரசியல் நீதி என்பது அனைத்து குடிமக்களுக்கும் சமமான அரசியல் உரிமைகள், அனைத்து அரசியல் பதவிகளுக்கும் சமமான அணுகல் மற்றும் நாட்டின் ஆட்சியில் சமமான குரல் இருப்பதை உறுதி செய்கிறது.",
        wno_dict={
            "A": {"en": "Incorrect. Qualifications are required.", "ta": "தவறு. தகுதிகள் தேவை."},
            "B": {"en": "Incorrect. Taxes are statutory.", "ta": "தவறு. வரிகள் சட்டப்பூர்வமானவை."},
            "C": {"en": "Incorrect. Economic policy aspect.", "ta": "தவறு. பொருளாதாரக் கொள்கை அம்சம்."},
            "D": {"en": "Correct. Equal political rights and access to public office.", "ta": "சரி. சமமான அரசியல் உரிமைகள் மற்றும் பொதுப் பதவிகளுக்கான அணுகல்."}
        },
        tip_en="Political Justice = Equal voting rights & equal access to political offices.",
        tip_ta="அரசியல் நீதி = சம வாக்குரிமை & அரசியல் பதவிகளுக்கான சம அணுகல்.",
        rev_en="Political Justice = Equal political rights & access to offices.",
        rev_ta="அரசியல் நீதி = சம அரசியல் உரிமைகள் & பதவிகளுக்கான அணுகல்.",
        sources=["Preamble Notes Part 1"],
        bloom="Understand", est_sec=30, pyq_sim="High", tags=["Political Justice", "Meaning"]
    ))

    # Q33 - Conceptual - Ans A
    qs.append(make_q(
        q_id="PRE_E_033", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="Conceptual",
        q_en="How does the Indian Constitution promote the ideal of 'Fraternity' mentioned in the Preamble?",
        q_ta="முகவுரையில் குறிப்பிடப்பட்டுள்ள 'சகோதரத்துவம்' என்ற தத்துவத்தை இந்திய அரசியலமைப்பு எவ்வாறு ஊக்குவிக்கிறது?",
        opts_en=[
            "By establishing Single Citizenship for the entire country (Part II).",
            "By establishing Dual Citizenship for Centre and States.",
            "By granting special titles to hereditary rulers.",
            "By restricting inter-state trade."
        ],
        opts_ta=[
            "முழு நாட்டிற்கும் ஒற்றைக் குடியுரிமையை (பகுதி II) நிறுவுவதன் மூலம்.",
            "மத்திய மற்றும் மாநிலங்களுக்கு இரட்டை குடியுரிமையை நிறுவுவதன் மூலம்.",
            "பரம்பரை ஆட்சியாளர்களுக்கு சிறப்புப் பட்டங்களை வழங்குவதன் மூலம்.",
            "மாநிலங்களுக்கு இடையேயான வர்த்தகத்தைக் கட்டுப்படுத்துவதன் மூலம்."
        ],
        correct_ans="A",
        exp_en="The Constitution promotes Fraternity through Single Citizenship (Part II) and Fundamental Duties (Article 51A(e)), instilling a feeling of common brotherhood.",
        exp_ta="அரசியலமைப்பு ஒற்றைக் குடியுரிமை (பகுதி II) மற்றும் அடிப்படை கடமைகள் (உறுப்பு 51A(e)) மூலம் பொதுவான சகோதரத்துவ உணர்வை வளர்த்து சகோதரத்துவத்தை ஊக்குவிக்கிறது.",
        wno_dict={
            "A": {"en": "Correct. Single Citizenship promotes common brotherhood.", "ta": "சரி. ஒற்றைக் குடியுரிமை பொதுவான சகோதரத்துவத்தை ஊக்குவிக்கிறது."},
            "B": {"en": "Incorrect. India has single citizenship, not dual.", "ta": "தவறு. இந்தியாவில் ஒற்றைக் குடியுரிமை மட்டுமே உள்ளது."},
            "C": {"en": "Incorrect. Article 18 abolished titles.", "ta": "தவறு. உறுப்பு 18 பட்டங்களை ஒழித்தது."},
            "D": {"en": "Incorrect. Article 301 guarantees free trade.", "ta": "தவறு. உறுப்பு 301 சுதந்திர வர்த்தகத்தை உத்தரவாதம் செய்கிறது."}
        },
        tip_en="Fraternity is promoted by Single Citizenship (Part II) and Fundamental Duties (Art 51A).",
        tip_ta="சகோதரத்துவம் ஒற்றைக் குடியுரிமை (பகுதி II) மற்றும் அடிப்படை கடமைகள் (உறுப்பு 51A) மூலம் ஊக்குவிக்கப்படுகிறது.",
        rev_en="Fraternity promoted via Single Citizenship.",
        rev_ta="சகோதரத்துவம் ஒற்றைக் குடியுரிமை மூலம் ஊக்குவிக்கப்படுகிறது.",
        sources=["Preamble Notes Part 1"],
        bloom="Understand", est_sec=30, pyq_sim="High", tags=["Fraternity", "Single Citizenship"]
    ))

    # Q34 - TNPSC Trap - Ans B
    qs.append(make_q(
        q_id="PRE_E_034", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="TNPSC Trap",
        q_en="Which of the following is NOT a Fundamental Right in Part III, but exists as a Legal Right under Article 300A in Part XII?",
        q_ta="பின்வருவனவற்றில் எது பகுதி III இல் அடிப்படை உரிமை அல்ல, ஆனால் பகுதி XII இல் உறுப்பு 300A இன் கீழ் ஒரு சட்ட உரிமையாக உள்ளது?",
        opts_en=["Right to Equality", "Right to Property", "Right to Freedom of Religion", "Right to Constitutional Remedies"],
        opts_ta=["சமத்துவ உரிமை", "சொத்து உரிமை", "சமய சுதந்திர உரிமை", "அரசியலமைப்பு தீர்வுகளுக்கான உரிமை"],
        correct_ans="B",
        exp_en="Right to Property was deleted from Fundamental Rights (Part III) by 44th Amendment 1978 and made a Legal Right under Article 300A in Part XII.",
        exp_ta="சொத்து உரிமை 44வது திருத்தம் 1978 மூலம் அடிப்படை உரிமையிலிருந்து (பகுதி III) நீக்கப்பட்டு பகுதி XII இல் உறுப்பு 300A இன் கீழ் சட்ட உரிமையாக மாற்றப்பட்டது.",
        wno_dict={
            "A": {"en": "Incorrect. Articles 14-18 is FR.", "ta": "தவறு. உறுப்புகள் 14-18 அடிப்படை உரிமை."},
            "B": {"en": "Correct. Right to Property is now a Legal Right under Art 300A.", "ta": "சரி. சொத்து உரிமை இப்போது உறுப்பு 300A இன் கீழ் சட்ட உரிமை."},
            "C": {"en": "Incorrect. Articles 25-28 is FR.", "ta": "தவறு. உறுப்புகள் 25-28 அடிப்படை உரிமை."},
            "D": {"en": "Incorrect. Article 32 is FR.", "ta": "தவறு. உறுப்பு 32 அடிப்படை உரிமை."}
        },
        tip_en="TNPSC Trap: Right to Property is a Legal Right under Art 300A (44th Amendment 1978).",
        tip_ta="TNPSC பொறி: சொத்து உரிமை என்பது உறுப்பு 300A இன் கீழ் உள்ள ஒரு சட்ட உரிமை (44வது திருத்தம் 1978).",
        rev_en="Right to Property = Legal Right under Art 300A (Part XII).",
        rev_ta="சொத்து உரிமை = உறுப்பு 300A இன் கீழ் சட்ட உரிமை.",
        sources=["Preamble Notes Part 1"],
        bloom="Understand", est_sec=30, pyq_sim="Direct PYQ", tags=["Right to Property", "Article 300A", "TNPSC Trap"]
    ))

    # Q35 - Direct - Ans C
    qs.append(make_q(
        q_id="PRE_E_035", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="Direct",
        q_en="By which Constitutional Amendment Act was the voting age reduced from 21 years to 18 years?",
        q_ta="எந்த அரசியலமைப்பு திருத்தச் சட்டத்தின் மூலம் வாக்களிக்கும் வயது 21 லிருந்து 18 ஆகக் குறைக்கப்பட்டது?",
        opts_en=["42nd Amendment Act, 1976", "44th Amendment Act, 1978", "61st Amendment Act, 1988", "86th Amendment Act, 2002"],
        opts_ta=["42வது திருத்தச் சட்டம், 1976", "44வது திருத்தச் சட்டம், 1978", "61வது திருத்தச் சட்டம், 1988", "86வது திருத்தச் சட்டம், 2002"],
        correct_ans="C",
        exp_en="The 61st Constitutional Amendment Act, 1988 (enforced in 1989) amended Article 326 to reduce the voting age from 21 to 18 years.",
        exp_ta="61வது அரசியலமைப்பு திருத்தச் சட்டம், 1988 (1989 இல் அமல்) வாக்களிக்கும் வயதை 21 லிருந்து 18 ஆகக் குறைக்க உறுப்பு 326 ஐத் திருத்தியது.",
        wno_dict={
            "A": {"en": "Incorrect. 42nd Amendment added Socialist, Secular, Integrity.", "ta": "தவறு. 42வது திருத்தம் சமதர்ம, மதச்சார்பற்ற, ஒருமைப்பாட்டைச் சேர்த்தது."},
            "B": {"en": "Incorrect. 44th Amendment removed property right from FR.", "ta": "தவறு. 44வது திருத்தம் சொத்து உரிமையை நீக்கியது."},
            "C": {"en": "Correct. 61st Amendment 1988 reduced voting age to 18.", "ta": "சரி. 61வது திருத்தம் 1988 வாக்கு வயதை 18 ஆகக் குறைத்தது."},
            "D": {"en": "Incorrect. 86th Amendment added Right to Education.", "ta": "தவறு. 86வது திருத்தம் கல்வி உரிமையைச் சேர்த்தது."}
        },
        tip_en="61st Amendment 1988 = Voting age 21 -> 18 years (Article 326).",
        tip_ta="61வது திருத்தம் 1988 = வாக்கு வயது 21 -> 18 ஆண்டுகள் (உறுப்பு 326).",
        rev_en="61st Amendment 1988 = Voting age reduced to 18.",
        rev_ta="61வது திருத்தம் 1988 = வாக்கு வயது 18 ஆகக் குறைப்பு.",
        sources=["Preamble Notes Part 1"],
        bloom="Remember", est_sec=30, pyq_sim="Direct PYQ", tags=["61st Amendment", "Voting Age", "Article 326"]
    ))

    # Q36 - Term / Meaning - Ans D
    qs.append(make_q(
        q_id="PRE_E_036", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="Term / Meaning",
        q_en="What does 'Social Justice' in the Preamble primarily aim to eliminate?",
        q_ta="முகவுரையில் உள்ள 'சமூக நீதி' (Social Justice) முதன்மையாக எதனை ஒழிப்பதை நோக்கமாகக் கொண்டுள்ளது?",
        opts_en=[
            "Private property ownership.",
            "Foreign trade relations.",
            "Judicial review by courts.",
            "Social discrimination based on caste, religion, race, or sex."
        ],
        opts_ta=[
            "தனியார் சொத்து உரிமையை.",
            "வெளிநாட்டு வர்த்தக உறவுகளை.",
            "நீதிமன்றங்களின் நீதிப் புனராய்வை.",
            "சாதி, மதம், இனம் அல்லது பாலினம் அடிப்படையிலான சமூகப் பாகுபாடுகளை."
        ],
        correct_ans="D",
        exp_en="Social Justice means equal treatment of all citizens without any social discrimination based on caste, color, race, religion, or sex.",
        exp_ta="சமூக நீதி என்பது சாதி, நிறம், இனம், மதம் அல்லது பாலினத்தின் அடிப்படையில் எந்தவொரு சமூகப் பாகுபாடும் இன்றி அனைத்து குடிமக்களையும் சமமாக நடத்துவதைக் குறிக்கிறது.",
        wno_dict={
            "A": {"en": "Incorrect. Property ownership is permitted.", "ta": "தவறு. சொத்து உரிமை அனுமதிக்கப்பட்டது."},
            "B": {"en": "Incorrect. Trade is encouraged.", "ta": "தவறு. வர்த்தகம் ஊக்குவிக்கப்படுகிறது."},
            "C": {"en": "Incorrect. Judicial review is basic structure.", "ta": "தவறு. நீதிப் புனராய்வு அடிப்படை அமைப்பு."},
            "D": {"en": "Correct. Eliminates social discrimination.", "ta": "சரி. சமூகப் பாகுபாடுகளை ஒழிக்கிறது."}
        },
        tip_en="Social Justice = Equal treatment without discrimination (Articles 15, 17).",
        tip_ta="சமூக நீதி = பாகுபாடின்றி சமமான நடத்தை (உறுப்புகள் 15, 17).",
        rev_en="Social Justice = Eliminates social discrimination.",
        rev_ta="சமூக நீதி = சமூகப் பாகுபாடுகளை ஒழிக்கிறது.",
        sources=["Preamble Notes Part 1"],
        bloom="Understand", est_sec=30, pyq_sim="High", tags=["Social Justice", "Meaning"]
    ))

    # Q37 - Direct - Ans A
    qs.append(make_q(
        q_id="PRE_E_037", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="Direct",
        q_en="Which part of the Indian Constitution is described as the 'Magna Carta of India'?",
        q_ta="இந்திய அரசியலமைப்பின் எந்தப் பகுதி 'இந்தியாவின் மகா சாசனம்' (Magna Carta of India) என்று விவரிக்கப்படுகிறது?",
        opts_en=["Part III (Fundamental Rights)", "Part IV (DPSP)", "Part IVA (Fundamental Duties)", "Part I (Union and its Territory)"],
        opts_ta=["பகுதி III (அடிப்படை உரிமைகள்)", "பகுதி IV (DPSP)", "பகுதி IVA (அடிப்படை கடமைகள்)", "பகுதி I (ஒன்றியமும் அதன் நிலப்பரப்பும்)"],
        correct_ans="A",
        exp_en="Part III of the Constitution containing Fundamental Rights (Articles 12-35) is described as the 'Magna Carta of India'.",
        exp_ta="அடிப்படை உரிமைகளைக் கொண்டுள்ள (உறுப்புகள் 12-35) அரசியலமைப்பின் பகுதி III 'இந்தியாவின் மகா சாசனம்' என்று விவரிக்கப்படுகிறது.",
        wno_dict={
            "A": {"en": "Correct. Part III = Magna Carta of India.", "ta": "சரி. பகுதி III = இந்தியாவின் மகா சாசனம்."},
            "B": {"en": "Incorrect. Part IV is DPSP.", "ta": "தவறு. பகுதி IV DPSP."},
            "C": {"en": "Incorrect. Part IVA is Fundamental Duties.", "ta": "தவறு. பகுதி IVA அடிப்படை கடமைகள்."},
            "D": {"en": "Incorrect. Part I is Union & Territory.", "ta": "தவறு. பகுதி I ஒன்றியமும் நிலப்பரப்பும்."}
        },
        tip_en="Magna Carta of India = Part III (Fundamental Rights).",
        tip_ta="இந்தியாவின் மகா சாசனம் = பகுதி III (அடிப்படை உரிமைகள்).",
        rev_en="Part III = Magna Carta of India.",
        rev_ta="பகுதி III = இந்தியாவின் மகா சாசனம்.",
        sources=["Preamble Notes Part 1"],
        bloom="Remember", est_sec=30, pyq_sim="Direct PYQ", tags=["Part III", "Magna Carta", "Fundamental Rights"]
    ))

    # Q38 - Conceptual - Ans B
    qs.append(make_q(
        q_id="PRE_E_038", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="Conceptual",
        q_en="What relationship exists between the Preamble and the Directive Principles of State Policy (DPSP) in Part IV?",
        q_ta="முகவுரைக்கும் பகுதி IV இல் உள்ள அரசு நெறிமுறைப்படுத்தும் கோட்பாடுகளுக்கும் (DPSP) இடையே என்ன தொடர்பு உள்ளது?",
        opts_en=[
            "Preamble contradicts DPSPs in all economic matters.",
            "DPSPs translate the noble economic and social goals of the Preamble into concrete state policy directives.",
            "DPSPs can override Fundamental Rights if Preamble is violated.",
            "There is no conceptual connection between Preamble and DPSPs."
        ],
        opts_ta=[
            "முகவுரை அனைத்து பொருளாதார விஷயங்களிலும் DPSP உடன் முரண்படுகிறது.",
            "DPSP முகவுரையின் உன்னதமான பொருளாதார மற்றும் சமூக இலக்குகளை உறுதியான அரசு கொள்கை வழிகாட்டுதல்களாக மாற்றுகிறது.",
            "முகவுரை மீறப்பட்டால் DPSP அடிப்படை உரிமைகளை மேலெழுதலாம்.",
            "முகவுரைக்கும் DPSP க்கும் இடையே எந்தவொரு கருத்துத் தொடர்பும் இல்லை."
        ],
        correct_ans="B",
        exp_en="DPSPs in Part IV translate the grand socio-economic vision of the Preamble (Social Justice, Economic Justice, Welfare State) into operational state policy directives.",
        exp_ta="பகுதி IV இல் உள்ள DPSP முகவுரையின் பிரம்மாண்டமான சமூக-பொருளாதார தொலைநோக்கை (சமூக நீதி, பொருளாதார நீதி, நலன்புரி அரசு) செயல்படும் அரசு கொள்கை வழிகாட்டுதல்களாக மாற்றுகிறது.",
        wno_dict={
            "A": {"en": "Incorrect. They are completely harmonized.", "ta": "தவறு. அவை முற்றிலும் நல்லிணக்கம் கொண்டவை."},
            "B": {"en": "Correct. DPSPs operationalize Preamble's socio-economic goals.", "ta": "சரி. DPSP முகவுரையின் சமூக-பொருளாதார இலக்குகளை செயல்படுத்துகிறது."},
            "C": {"en": "Incorrect. Preamble is non-justiciable.", "ta": "தவறு. முகவுரை நிலைநிறுத்த முடியாதது."},
            "D": {"en": "Incorrect. Strong conceptual linkage exists.", "ta": "தவறு. வலுவான தொடர்பு உள்ளது."}
        },
        tip_en="Preamble = Vision/Goals; DPSP = Operational Policy Directives for Welfare State.",
        tip_ta="முகவுரை = தொலைநோக்கு/இலக்குகள்; DPSP = நலன்புரி அரசுக்கான செயல்பாட்டுக் கொள்கை வழிகாட்டுதல்கள்.",
        rev_en="DPSP operationalizes Preamble's social and economic justice goals.",
        rev_ta="DPSP முகவுரையின் சமூக மற்றும் பொருளாதார நீதி இலக்குகளை செயல்படுத்துகிறது.",
        sources=["Preamble Notes Part 2"],
        bloom="Understand", est_sec=30, pyq_sim="High", tags=["DPSP", "Preamble Relationship"]
    ))

    # Q39 - Direct - Ans C
    qs.append(make_q(
        q_id="PRE_E_039", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="Direct",
        q_en="Under which Part and Article were Fundamental Duties incorporated into the Indian Constitution?",
        q_ta="இந்திய அரசியலமைப்பின் எந்தப் பகுதி மற்றும் உறுப்பின் கீழ் அடிப்படை கடமைகள் சேர்க்கப்பட்டன?",
        opts_en=["Part IV, Article 51", "Part III, Article 32", "Part IVA, Article 51A", "Part V, Article 75"],
        opts_ta=["பகுதி IV, உறுப்பு 51", "பகுதி III, உறுப்பு 32", "பகுதி IVA, உறுப்பு 51A", "பகுதி V, உறுப்பு 75"],
        correct_ans="C",
        exp_en="Fundamental Duties were incorporated into Part IVA under Article 51A by the 42nd Constitutional Amendment Act of 1976 on Swaran Singh Committee recommendation.",
        exp_ta="ஸ்வரன் சிங் குழுவின் பரிந்துரையின் பேரில் 1976 இன் 42வது திருத்தச் சட்டம் மூலம் பகுதி IVA இல் உறுப்பு 51A இன் கீழ் அடிப்படை கடமைகள் சேர்க்கப்பட்டன.",
        wno_dict={
            "A": {"en": "Incorrect. Article 51 is international peace in DPSP.", "ta": "தவறு. உறுப்பு 51 சர்வதேச அமைதி பற்றியது."},
            "B": {"en": "Incorrect. Article 32 is constitutional remedies.", "ta": "தவறு. உறுப்பு 32 அரசியலமைப்பு தீர்வு பற்றியது."},
            "C": {"en": "Correct. Part IVA, Article 51A contains Fundamental Duties.", "ta": "சரி. பகுதி IVA, உறுப்பு 51A அடிப்படை கடமைகளைக் கொண்டுள்ளது."},
            "D": {"en": "Incorrect. Article 75 deals with Ministers.", "ta": "தவறு. உறுப்பு 75 அமைச்சர்கள் பற்றியது."}
        },
        tip_en="Part IVA, Article 51A = Fundamental Duties (42nd Amendment 1976).",
        tip_ta="பகுதி IVA, உறுப்பு 51A = அடிப்படை கடமைகள் (42வது திருத்தம் 1976).",
        rev_en="Fundamental Duties = Part IVA, Article 51A.",
        rev_ta="அடிப்படை கடமைகள் = பகுதி IVA, உறுப்பு 51A.",
        sources=["Preamble Notes Part 1 & 2"],
        bloom="Remember", est_sec=30, pyq_sim="Direct PYQ", tags=["Fundamental Duties", "Part IVA", "Article 51A"]
    ))

    # Q40 - TNPSC Trap - Ans D
    qs.append(make_q(
        q_id="PRE_E_040", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="TNPSC Trap",
        q_en="Which of the following statements regarding the Preamble is INCORRECT?",
        q_ta="முகவுரை தொடர்பான பின்வரும் கூற்றுகளில் எது தவறானது?",
        opts_en=[
            "Preamble is based on Nehru's Objectives Resolution.",
            "Preamble was declared as a part of the Constitution in Kesavananda Bharati Case (1973).",
            "Preamble has been amended only once by the 42nd Amendment Act 1976.",
            "Preamble is an independent source of substantive power for the Union Parliament."
        ],
        opts_ta=[
            "முகவுரை நேருவின் குறிக்கோள் தீர்மானத்தின் அடிப்படையில் அமைந்தது.",
            "கேசவாநந்த பாரதி வழக்கில் (1973) முகவுரை அரசியலமைப்பின் ஒரு பகுதி என அறிவிக்கப்பட்டது.",
            "42வது திருத்தச் சட்டம் 1976 மூலம் முகவுரை ஒரே ஒரு முறை மட்டுமே திருத்தப்பட்டுள்ளது.",
            "முகவுரை மத்திய நாடாளுமன்றத்திற்கான ஒரு சுதந்திரமான உரிமையியல் அதிகார மூலம் ஆகும்."
        ],
        correct_ans="D",
        exp_en="Statement D is INCORRECT because the Supreme Court explicitly held that the Preamble is NEITHER a source of power to the legislature NOR a prohibition upon powers.",
        exp_ta="கூற்று D தவறானது, ஏனெனில் உச்ச நீதிமன்றம் முகவுரை சட்டமன்றத்திற்கான அதிகார மூலமும் அல்ல, அதிகாரத் தடையும் அல்ல என்று வெளிப்படையாகத் தீர்ப்பளித்துள்ளது.",
        wno_dict={
            "A": {"en": "Incorrect statement choice. Statement A is TRUE.", "ta": "தவறு. கூற்று A சரி."},
            "B": {"en": "Incorrect statement choice. Statement B is TRUE.", "ta": "தவறு. கூற்று B சரி."},
            "C": {"en": "Incorrect statement choice. Statement C is TRUE.", "ta": "தவறு. கூற்று C சரி."},
            "D": {"en": "Correct statement choice (this statement is FALSE). Preamble is NOT a source of power.", "ta": "சரி (இந்தக் கூற்று தவறானது). முகவுரை அதிகார மூலம் அல்ல."}
        },
        tip_en="TNPSC Trap: Preamble is NOT a source of power nor a restriction on power.",
        tip_ta="TNPSC பொறி: முகவுரை அதிகார மூலமும் அல்ல, அதிகாரத் தடையும் அல்ல.",
        rev_en="Preamble confers no independent legislative power.",
        rev_ta="முகவுரை எந்தவொரு சுதந்திரமான சட்டமன்ற அதிகாரத்தையும் வழங்காது.",
        sources=["Preamble Notes Part 2"],
        bloom="Understand", est_sec=45, pyq_sim="High", tags=["Preamble", "Source of Power", "TNPSC Trap"]
    ))

    # Q41 - Direct - Ans A
    qs.append(make_q(
        q_id="PRE_E_041", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="Direct",
        q_en="Who described the Preamble as the 'Horoscope of our Sovereign Democratic Republic'?",
        q_ta="முகவுரையை 'நமது இறையாண்மை ஜனநாயகக் குடியரசின் ஜாதகம்' என்று விவரித்தவர் யார்?",
        opts_en=["K.M. Munshi", "Dr. B.R. Ambedkar", "Jawaharlal Nehru", "Dr. Rajendra Prasad"],
        opts_ta=["கே.எம். முன்ஷி", "டாக்டர் பி.ஆர். அம்பேத்கர்", "ஜவஹர்லால் நேரு", "டாக்டர் ராஜேந்திர பிரசாத்"],
        correct_ans="A",
        exp_en="K.M. Munshi, a member of the Drafting Committee, described the Preamble as the 'Horoscope of our Sovereign Democratic Republic'.",
        exp_ta="வரைவுக் குழுவின் உறுப்பினரான கே.எம். முன்ஷி முகவுரையை 'நமது இறையாண்மை ஜனநாயகக் குடியரசின் ஜாதகம்' என்று விவரித்தார்.",
        wno_dict={
            "A": {"en": "Correct. K.M. Munshi called it Horoscope of Sovereign Democratic Republic.", "ta": "சரி. கே.எம். முன்ஷி அதை ஜாதகம் என்றார்."},
            "B": {"en": "Incorrect. Ambedkar called Art 32 Heart & Soul.", "ta": "தவறு. அம்பேத்கர் உறுப்பு 32 ஐ இதயம் & ஆன்மா என்றார்."},
            "C": {"en": "Incorrect. Nehru moved Objectives Resolution.", "ta": "தவறு. நேரு குறிக்கோள் தீர்மானத்தை முன்மொழிந்தார்."},
            "D": {"en": "Incorrect. Rajendra Prasad was Assembly President.", "ta": "தவறு. ராஜேந்திர பிரசாத் சபாத்தலைவர்."}
        },
        tip_en="Horoscope of Republic = K.M. Munshi.",
        tip_ta="குடியரசின் ஜாதகம் = கே.எம். முன்ஷி.",
        rev_en="K.M. Munshi = Horoscope of Sovereign Democratic Republic.",
        rev_ta="கே.எம். முன்ஷி = இறையாண்மை ஜனநாயகக் குடியரசின் ஜாதகம்.",
        sources=["Preamble Notes Part 1"],
        bloom="Remember", est_sec=30, pyq_sim="High", tags=["KM Munshi", "Horoscope", "Preamble Quotes"]
    ))

    # Q42 - Direct - Ans B
    qs.append(make_q(
        q_id="PRE_E_042", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="Direct",
        q_en="Who described the Preamble as the 'soul of the Constitution, a key to the Constitution, and a jewel set in the Constitution'?",
        q_ta="முகவுரையை 'அரசியலமைப்பின் ஆன்மா, அரசியலமைப்பின் சாவி மற்றும் அரசியலமைப்பில் பதிக்கப்பட்ட மாணிக்கம்' என்று விவரித்தவர் யார்?",
        opts_en=["Sir Ivor Jennings", "Pandit Thakur Das Bhargava", "Granville Austin", "K.C. Wheare"],
        opts_ta=["சர் ஐவர் ஜென்னிங்ஸ்", "பண்டிட் தாக்கூர் தாஸ் பார்கவா", "கிரான்வில் ஆஸ்டின்", "கே.சி. வியர்"],
        correct_ans="B",
        exp_en="Pandit Thakur Das Bhargava stated: 'The Preamble is the most precious part of the Constitution. It is the soul of the Constitution. It is a key to the Constitution. It is a jewel set in the Constitution.'",
        exp_ta="பண்டிட் தாக்கூர் தாஸ் பார்கவா கூறினார்: 'முகவுரை அரசியலமைப்பின் மிக விலையுயர்ந்த பகுதியாகும். இது அரசியலமைப்பின் ஆன்மா. இது அரசியலமைப்பின் சாவி. இது அரசியலமைப்பில் பதிக்கப்பட்ட மாணிக்கம்.'",
        wno_dict={
            "A": {"en": "Incorrect. Jennings commented on federation centralizing tendency.", "ta": "தவறு. ஜென்னிங்ஸ் மையப்போக்கு கூட்டாட்சி என்றார்."},
            "B": {"en": "Correct. Pandit Thakur Das Bhargava described it as Soul, Key, and Jewel.", "ta": "சரி. பண்டிட் தாக்கூர் தாஸ் பார்கவா அதை ஆன்மா, சாவி, மாணிக்கம் என்றார்."},
            "C": {"en": "Incorrect. Austin called federalism cooperative.", "ta": "தவறு. ஆஸ்டின் கூட்டுறவு கூட்டாட்சி என்றார்."},
            "D": {"en": "Incorrect. Wheare called it quasi-federal.", "ta": "தவறு. வியர் பகுதி-கூட்டாட்சி என்றார்."}
        },
        tip_en="Soul, Key, Jewel set in Constitution = Pandit Thakur Das Bhargava.",
        tip_ta="அரசியலமைப்பின் ஆன்மா, சாவி, மாணிக்கம் = பண்டிட் தாக்கூர் தாஸ் பார்கவா.",
        rev_en="Thakur Das Bhargava = Soul, Key, and Jewel of Constitution.",
        rev_ta="தாக்கூர் தாஸ் பார்கவா = அரசியலமைப்பின் ஆன்மா, சாவி, மாணிக்கம்.",
        sources=["Preamble Notes Part 1"],
        bloom="Remember", est_sec=30, pyq_sim="High", tags=["Thakur Das Bhargava", "Soul of Constitution"]
    ))

    # Q43 - Conceptual - Ans C
    qs.append(make_q(
        q_id="PRE_E_043", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="Conceptual",
        q_en="What is the significance of the Basic Structure Doctrine regarding the amendment of the Preamble?",
        q_ta="முகவுரையைத் திருத்துவது தொடர்பாக அடிப்படை கட்டமைப்பு கோட்பாட்டின் முக்கியத்துவம் என்ன?",
        opts_en=[
            "Parliament can repeal the Preamble entirely.",
            "Preamble can never be amended by Parliament.",
            "Parliament can amend the Preamble, but cannot alter or destroy its basic elements (like Secularism or Democracy).",
            "President can alter the Preamble by executive decree."
        ],
        opts_ta=[
            "நாடாளுமன்றம் முகவுரையை முற்றிலும் ரத்து செய்யலாம்.",
            "முகவுரையை நாடாளுமன்றத்தால் ஒருபோதும் திருத்த முடியாது.",
            "நாடாளுமன்றம் முகவுரையைத் திருத்தலாம், ஆனால் அதில் உள்ள அடிப்படை கூறுகளை (மதச்சார்பின்மை அல்லது ஜனநாயகம் போன்றவை) மாற்றவோ அழிக்கவோ முடியாது.",
            "குடியரசுத் தலைவர் நிர்வாக ஆணை மூலம் முகவுரையை மாற்றலாம்."
        ],
        correct_ans="C",
        exp_en="Under the Basic Structure Doctrine (Kesavananda Bharati 1973), Parliament can amend the Preamble under Art 368, but CANNOT alter or destroy its basic features (like Democracy, Secularism, Republic).",
        exp_ta="அடிப்படை கட்டமைப்பு கோட்பாட்டின் கீழ் (கேசவாநந்த பாரதி 1973), நாடாளுமன்றம் உறுப்பு 368 இன் கீழ் முகவுரையைத் திருத்தலாம், ஆனால் அதன் அடிப்படை அம்சங்களை (ஜனநாயகம், மதச்சார்பின்மை, குடியரசு போன்றவை) மாற்றவோ அழிக்கவோ முடியாது.",
        wno_dict={
            "A": {"en": "Incorrect. Parliament cannot destroy basic structure.", "ta": "தவறு. நாடாளுமன்றம் அடிப்படை அமைப்பை அழிக்க முடியாது."},
            "B": {"en": "Incorrect. Preamble WAS amended in 1976.", "ta": "தவறு. முகவுரை 1976 இல் திருத்தப்பட்டது."},
            "C": {"en": "Correct. Can amend subject to Basic Structure limitation.", "ta": "சரி. அடிப்படை கட்டமைப்பு வரம்பிற்கு உட்பட்டு திருத்தலாம்."},
            "D": {"en": "Incorrect. Executive decrees cannot amend Constitution.", "ta": "தவறு. நிர்வாக ஆணைகளால் அரசியலமைப்பைத் திருத்த முடியாது."}
        },
        tip_en="Basic Structure Doctrine limits Parliament's amendment power under Article 368.",
        tip_ta="அடிப்படை கட்டமைப்பு கோட்பாடு உறுப்பு 368 இன் கீழ் நாடாளுமன்றத்தின் திருத்த அதிகாரத்தைக் கட்டுப்படுத்துகிறது.",
        rev_en="Preamble Amendable bounded by Basic Structure Doctrine.",
        rev_ta="அடிப்படை கட்டமைப்புக்கு உட்பட்டு முகவுரை திருத்தப்படலாம்.",
        sources=["Preamble Notes Part 2"],
        bloom="Understand", est_sec=30, pyq_sim="High", tags=["Basic Structure", "Amendability"]
    ))

    # Q44 - Direct - Ans D
    qs.append(make_q(
        q_id="PRE_E_044", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="Direct",
        q_en="On which date was the Objectives Resolution unanimously adopted by the Constituent Assembly?",
        q_ta="அரசியலமைப்புச் சபையால் குறிக்கோள் தீர்மானம் ஏகமனதாக ஏற்றுக்கொள்ளப்பட்ட நாள் எது?",
        opts_en=["13th December 1946", "26th November 1949", "26th January 1950", "22nd January 1947"],
        opts_ta=["13 டிசம்பர் 1946", "26 நவம்பர் 1949", "26 ஜனவரி 1950", "22 ஜனவரி 1947"],
        correct_ans="D",
        exp_en="The Objectives Resolution was moved by Nehru on Dec 13, 1946 and unanimously adopted by the Constituent Assembly on 22nd January 1947.",
        exp_ta="குறிக்கோள் தீர்மானம் நேருவால் 13 டிசம்பர் 1946 அன்று முன்மொழியப்பட்டு 22 ஜனவரி 1947 அன்று அரசியலமைப்புச் சபையால் ஏகமனதாக ஏற்றுக்கொள்ளப்பட்டது.",
        wno_dict={
            "A": {"en": "Incorrect. 13th Dec 1946 was the date it was MOVED.", "ta": "தவறு. 13 டிசம்பர் 1946 முன்மொழியப்பட்ட நாள்."},
            "B": {"en": "Incorrect. 26th Nov 1949 was Constitution Adoption date.", "ta": "தவறு. 26 நவம்பர் 1949 அரசியலமைப்பு ஏற்றுக்கொள்ளப்பட்ட நாள்."},
            "C": {"en": "Incorrect. 26th Jan 1950 was Republic Day.", "ta": "தவறு. 26 ஜனவரி 1950 குடியரசு தினம்."},
            "D": {"en": "Correct. 22nd January 1947 is the Date of Adoption of Objectives Resolution.", "ta": "சரி. 22 ஜனவரி 1947 குறிக்கோள் தீர்மானம் ஏற்றுக்கொள்ளப்பட்ட நாள்."}
        },
        tip_en="TNPSC Trap: Moved = Dec 13, 1946; Adopted = Jan 22, 1947.",
        tip_ta="TNPSC பொறி: முன்மொழியப்பட்டது = டிசம்பர் 13, 1946; ஏற்றுக்கொள்ளப்பட்டது = ஜனவரி 22, 1947.",
        rev_en="Objectives Resolution Adopted = 22nd January 1947.",
        rev_ta="குறிக்கோள் தீர்மானம் ஏற்றுக்கொள்ளப்பட்ட நாள் = 22 ஜனவரி 1947.",
        sources=["Preamble Notes Part 1"],
        bloom="Remember", est_sec=30, pyq_sim="Direct PYQ", tags=["Objectives Resolution", "22 January 1947"]
    ))

    # Q45 - Conceptual - Ans A
    qs.append(make_q(
        q_id="PRE_E_045", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="Conceptual",
        q_en="Why was the Preamble voted upon and passed by the Constituent Assembly AFTER the rest of the Constitution was already adopted?",
        q_ta="அரசியலமைப்பின் இதர பகுதிகள் ஏற்கனவே ஏற்றுக்கொள்ளப்பட்ட பின்னரே முகவுரையின் மீது வாக்களிக்கப்பட்டு அரசியலமைப்புச் சபையால் நிறைவேற்றப்பட்டது ஏன்?",
        opts_en=[
            "To ensure that the Preamble was in complete conformity with the text of the Constitution as enacted.",
            "Because framers forgot to draft the Preamble earlier.",
            "Because the British Parliament insisted on passing it last.",
            "Because Article 368 mandated passing Preamble at the end."
        ],
        opts_ta=[
            "நிறைவேற்றப்பட்ட அரசியலமைப்பின் உரையுடன் முகவுரை முற்றிலும் ஒத்துப்போவதை உறுதி செய்வதற்காக.",
            "வரைவாளர்கள் முகவுரையை முன்பே உருவாக்க மறந்துவிட்டதால்.",
            "பிரிட்டிஷ் நாடாளுமன்றம் அதை கடைசியாக நிறைவேற்ற வற்புறுத்தியதால்.",
            "உறுப்பு 368 முகவுரையை இறுதியில் நிறைவேற்ற கட்டாயப்படுத்தியதால்."
        ],
        correct_ans="A",
        exp_en="The Preamble was enacted last by the Assembly specifically to ensure that its wording aligned in complete harmony and conformity with the body of the Constitution.",
        exp_ta="அரசியலமைப்புச் சபையால் முகவுரை இறுதியில் இயற்றப்பட்டது, ஏனெனில் அதன் சொற்கள் அரசியலமைப்பின் உடற்பகுதியுடன் முழுமையான நல்லிணக்கத்துடனும் ஒத்துப்போவதையும் உறுதி செய்வதற்காக ஆகும்.",
        wno_dict={
            "A": {"en": "Correct. Enacted last to ensure conformity with main Constitution text.", "ta": "சரி. முதன்மை அரசியலமைப்பு உரையுடன் ஒத்துப்போவதை உறுதி செய்ய இறுதியில் இயற்றப்பட்டது."},
            "B": {"en": "Incorrect. Objectives resolution was moved first in 1946.", "ta": "தவறு. குறிக்கோள் தீர்மானம் 1946 லேயே முன்மொழியப்பட்டது."},
            "C": {"en": "Incorrect. British parliament had no role in Constituent Assembly voting.", "ta": "தவறு. பிரிட்டிஷ் நாடாளுமன்றத்திற்கு இதில் பங்கில்லை."},
            "D": {"en": "Incorrect. Art 368 does not specify assembly voting order.", "ta": "தவறு. உறுப்பு 368 இதை குறிப்பிடவில்லை."}
        },
        tip_en="Preamble was enacted LAST to ensure conformity with the Constitution.",
        tip_ta="அரசியலமைப்புடன் ஒத்துப்போவதை உறுதி செய்ய முகவுரை இறுதியில் இயற்றப்பட்டது.",
        rev_en="Preamble passed last by Assembly to match Constitution text.",
        rev_ta="அரசியலமைப்பு உரையுடன் பொருந்த முகவுரை இறுதியில் நிறைவேற்றப்பட்டது.",
        sources=["Preamble Notes Part 2"],
        bloom="Understand", est_sec=30, pyq_sim="High", tags=["Enactment Order", "Constituent Assembly"]
    ))

    # Q46 - Direct - Ans B
    qs.append(make_q(
        q_id="PRE_E_046", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="Direct",
        q_en="Which of the following was the original phrase declaring the Nature of State in the Preamble before the 1976 Amendment?",
        q_ta="1976 திருத்தத்திற்கு முன் முகவுரையில் அரசின் தன்மையை விவரித்த அசல் தொடர் எது?",
        opts_en=[
            "Sovereign Socialist Secular Democratic Republic",
            "Sovereign Democratic Republic",
            "Sovereign Republic",
            "Democratic Republic"
        ],
        opts_ta=[
            "இறையாண்மை சமதர்ம மதச்சார்பற்ற ஜனநாயக குடியரசு",
            "இறையாண்மை ஜனநாயக குடியரசு (Sovereign Democratic Republic)",
            "இறையாண்மை குடியரசு",
            "ஜனநாயக குடியரசு"
        ],
        correct_ans="B",
        exp_en="Before the 42nd Amendment Act 1976, the original Preamble described India as a 'Sovereign Democratic Republic'. Socialist and Secular were inserted in 1976.",
        exp_ta="1976 இன் 42வது திருத்தச் சட்டத்திற்கு முன், அசல் முகவுரை இந்தியாவை 'இறையாண்மை ஜனநாயகக் குடியரசு' என்று விவரித்தது. சமதர்ம மற்றும் மதச்சார்பற்ற சொற்கள் 1976 இல் சேர்க்கப்பட்டன.",
        wno_dict={
            "A": {"en": "Incorrect. This is the present amended phrase (after 1976).", "ta": "தவறு. இது தற்போதைய திருத்தப்பட்ட தொடர் (1976க்கு பின்)."},
            "B": {"en": "Correct. Original phrase was 'Sovereign Democratic Republic'.", "ta": "சரி. அசல் தொடர் 'இறையாண்மை ஜனநாயகக் குடியரசு'."},
            "C": {"en": "Incorrect. Democratic was present originally.", "ta": "தவறு. ஜனநாயகம் அசலில் இருந்தது."},
            "D": {"en": "Incorrect. Sovereign was present originally.", "ta": "தவறு. இறையாண்மை அசலில் இருந்தது."}
        },
        tip_en="Original Preamble (1950) = Sovereign Democratic Republic.",
        tip_ta="அசல் முகவுரை (1950) = இறையாண்மை ஜனநாயகக் குடியரசு.",
        rev_en="Original Nature phrase = Sovereign Democratic Republic.",
        rev_ta="அசல் அரசின் தன்மையின் தொடர் = இறையாண்மை ஜனநாயகக் குடியரசு.",
        sources=["Preamble Notes Part 1 & 2"],
        bloom="Remember", est_sec=30, pyq_sim="High", tags=["Original Preamble", "42nd Amendment"]
    ))

    # Q47 - Direct - Ans C
    qs.append(make_q(
        q_id="PRE_E_047", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="Direct",
        q_en="Under whose Prime Ministership was the 42nd Constitutional Amendment Act 1976 passed?",
        q_ta="எந்தப் பிரதமரின் ஆட்சிக் காலத்தில் 42வது அரசியலமைப்பு திருத்தச் சட்டம் 1976 நிறைவேற்றப்பட்டது?",
        opts_en=["Jawaharlal Nehru", "Lal Bahadur Shastri", "Mrs. Indira Gandhi", "Morarji Desai"],
        opts_ta=["ஜவஹர்லால் நேரு", "லால் பகதூர் சாஸ்திரி", "திருமதி இந்திரா காந்தி", "மொரார்ஜி தேசாய்"],
        correct_ans="C",
        exp_en="The 42nd Constitutional Amendment Act 1976 was passed during the Prime Ministership of Mrs. Indira Gandhi on the recommendations of the Swaran Singh Committee.",
        exp_ta="42வது அரசியலமைப்பு திருத்தச் சட்டம் 1976 ஸ்வரன் சிங் குழுவின் பரிந்துரைகளின் பேரில் திருமதி இந்திரா காந்தி பிரதமராக இருந்தபோது நிறைவேற்றப்பட்டது.",
        wno_dict={
            "A": {"en": "Incorrect. Nehru passed away in 1964.", "ta": "தவறு. நேரு 1964 இல் மறைந்தார்."},
            "B": {"en": "Incorrect. Shastri passed away in 1966.", "ta": "தவறு. சாஸ்திரி 1966 இல் மறைந்தார்."},
            "C": {"en": "Correct. Mrs. Indira Gandhi was PM in 1976.", "ta": "சரி. திருமதி இந்திரா காந்தி 1976 இல் பிரதமராக இருந்தார்."},
            "D": {"en": "Incorrect. Morarji Desai passed 44th Amendment in 1978.", "ta": "தவறு. மொரார்ஜி தேசாய் 1978 இல் 44வது திருத்தத்தைக் கொண்டுவந்தார்."}
        },
        tip_en="42nd Amendment 1976 PM = Mrs. Indira Gandhi (Swaran Singh Committee).",
        tip_ta="42வது திருத்தம் 1976 பிரதமர் = திருமதி இந்திரா காந்தி (ஸ்வரன் சிங் குழு).",
        rev_en="42nd Amendment PM = Indira Gandhi.",
        rev_ta="42வது திருத்தத்தின் பிரதமர் = இந்திரா காந்தி.",
        sources=["Preamble Notes Part 2"],
        bloom="Remember", est_sec=30, pyq_sim="High", tags=["Indira Gandhi", "42nd Amendment"]
    ))

    # Q48 - TNPSC Trap - Ans D
    qs.append(make_q(
        q_id="PRE_E_048", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="TNPSC Trap",
        q_en="Were the principles of Secularism and Socialism completely absent from the Indian Constitution before the 42nd Amendment Act 1976?",
        q_ta="1976 இன் 42வது திருத்தச் சட்டத்திற்கு முன்னர் மதச்சார்பின்மை மற்றும் சமதர்மக் கோட்பாடுகள் இந்திய அரசியலமைப்பில் முற்றிலும் இல்லையா?",
        opts_en=[
            "Yes, they were completely absent before 1976.",
            "Yes, they were added by British Parliament in 1976.",
            "No, only Socialism was present in Part III.",
            "NO, secularism was already present in Articles 25-28 and socialism was in Part IV DPSPs."
        ],
        opts_ta=[
            "ஆம், 1976க்கு முன்னர் அவை முற்றிலும் இல்லை.",
            "ஆம், அவை 1976 இல் பிரிட்டிஷ் நாடாளுமன்றத்தால் சேர்க்கப்பட்டன.",
            "இல்லை, பகுதி III இல் சமதர்மம் மட்டுமே இருந்தது.",
            "இல்லை, மதச்சார்பின்மை ஏற்கனவே உறுப்புகள் 25-28 இலும், சமதர்மம் பகுதி IV DPSP இலும் பொதிந்திருந்தன."
        ],
        correct_ans="D",
        exp_en="NO. Even before 1976, secular principles were enshrined in Fundamental Rights (Articles 25-28) and socialist goals were in DPSPs (Articles 38 & 39). The 1976 Amendment merely made them explicit in the Preamble.",
        exp_ta="இல்லை. 1976க்கு முன்பே, மதச்சார்பற்ற கோட்பாடுகள் அடிப்படை உரிமைகளிலும் (உறுப்புகள் 25-28) சமதர்ம இலக்குகள் DPSP இலும் (உறுப்புகள் 38 & 39) பொதிந்திருந்தன. 1976 திருத்தம் முகவுரையில் அவற்றை வெளிப்படையாக ஆக்கியது.",
        wno_dict={
            "A": {"en": "Incorrect. They existed implicitly in Articles 25-28 and DPSP.", "ta": "தவறு. அவை மறைமுகமாக உறுப்புகள் 25-28 மற்றும் DPSP இல் இருந்தன."},
            "B": {"en": "Incorrect. British parliament had no role.", "ta": "தவறு. பிரிட்டிஷ் நாடாளுமன்றத்திற்கு இதில் பங்கில்லை."},
            "C": {"en": "Incorrect. Socialism was in Part IV DPSP.", "ta": "தவறு. சமதர்மம் பகுதி IV DPSP இல் இருந்தது."},
            "D": {"en": "Correct. They existed implicitly before being made explicit in 1976.", "ta": "சரி. 1976 இல் வெளிப்படையாக்கப்படுவதற்கு முன்பே அவை இருந்தன."}
        },
        tip_en="TNPSC Trap: Secularism (Arts 25-28) & Socialism (Part IV DPSPs) existed implicitly before 1976.",
        tip_ta="TNPSC பொறி: மதச்சார்பின்மை (உறுப்புகள் 25-28) & சமதர்மம் (பகுதி IV DPSP) 1976க்கு முன்பே இருந்தன.",
        rev_en="Pre-1976: Secularism in Arts 25-28; Socialism in DPSP.",
        rev_ta="1976க்கு முன்: உறுப்புகள் 25-28 இல் மதச்சார்பின்மை; DPSP இல் சமதர்மம்.",
        sources=["Preamble Notes Part 1 & 2"],
        bloom="Understand", est_sec=45, pyq_sim="High", tags=["Pre-1976 Status", "TNPSC Trap"]
    ))

    # Q49 - Direct - Ans A
    qs.append(make_q(
        q_id="PRE_E_049", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="Direct",
        q_en="Which Committee recommended the inclusion of Fundamental Duties in Part IVA of the Constitution in 1976?",
        q_ta="1976 இல் அரசியலமைப்பின் பகுதி IVA இல் அடிப்படை கடமைகளை சேர்க்கப் பரிந்துரைத்த குழு எது?",
        opts_en=["Swaran Singh Committee", "Sarkaria Commission", "Balwant Rai Mehta Committee", "Verma Committee"],
        opts_ta=["ஸ்வரன் சிங் குழு (Swaran Singh Committee)", "சர்க்காரியா ஆணையம்", "பல்வந்த் ராய் மேத்தா குழு", "வர்மா குழு"],
        correct_ans="A",
        exp_en="The Swaran Singh Committee (1976) recommended the inclusion of Fundamental Duties, which led to the 42nd Amendment Act 1976 adding Part IVA (Article 51A).",
        exp_ta="ஸ்வரன் சிங் குழு (1976) அடிப்படை கடமைகளைச் சேர்க்கப் பரிந்துரைத்தது, இது 42வது திருத்தச் சட்டம் 1976 பகுதி IVA (உறுப்பு 51A) ஐச் சேர்க்க வழிவகுத்தது.",
        wno_dict={
            "A": {"en": "Correct. Swaran Singh Committee recommended Fundamental Duties.", "ta": "சரி. ஸ்வரன் சிங் குழு அடிப்படை கடமைகளைப் பரிந்துரைத்தது."},
            "B": {"en": "Incorrect. Sarkaria Commission was Centre-State relations 1983.", "ta": "தவறு. சர்க்காரியா ஆணையம் மத்திய-மாநில உறவுகள் 1983."},
            "C": {"en": "Incorrect. Balwant Rai Mehta was Panchayati Raj 1957.", "ta": "தவறு. பல்வந்த் ராய் மேத்தா பஞ்சாயத்து ராஜ் 1957."},
            "D": {"en": "Incorrect. Verma Committee was 1999 review on FDs.", "ta": "தவறு. வர்மா குழு 1999 இல் வந்தது."}
        },
        tip_en="Swaran Singh Committee 1976 = Recommended Fundamental Duties (Part IVA, Art 51A).",
        tip_ta="ஸ்வரன் சிங் குழு 1976 = அடிப்படை கடமைகளைப் பரிந்துரைத்தது (பகுதி IVA, உறுப்பு 51A).",
        rev_en="Swaran Singh Committee = Recommended Fundamental Duties.",
        rev_ta="ஸ்வரன் சிங் குழு = அடிப்படை கடமைகளைப் பரிந்துரைத்தது.",
        sources=["Preamble Notes Part 1 & 2"],
        bloom="Remember", est_sec=30, pyq_sim="Direct PYQ", tags=["Swaran Singh Committee", "Fundamental Duties"]
    ))

    # Q50 - Conceptual - Ans B
    qs.append(make_q(
        q_id="PRE_E_050", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="Conceptual",
        q_en="What is the ultimate constitutional significance of the Preamble in the Indian Republic?",
        q_ta="இந்தியக் குடியரசில் முகவுரையின் இறுதி அரசியலமைப்பு முக்கியத்துவம் என்ன?",
        opts_en=[
            "It serves as a penal code to punish criminal offences.",
            "It embodies the grand vision, moral values, and foundational philosophy of the Constitution.",
            "It empowers Parliament to dissolve State Legislatures at will.",
            "It replaces the Fundamental Rights during National Emergency."
        ],
        opts_ta=[
            "இது குற்றவியல் குற்றங்களைத் தண்டிக்கும் தண்டனைச் சட்டமாக செயல்படுகிறது.",
            "இது அரசியலமைப்பின் பிரம்மாண்டமான தொலைநோக்கு, நெறிமுறை மதிப்புகள் மற்றும் அடிப்படை தத்துவத்தை வெளிப்படுத்துகிறது.",
            "இது மாநில சட்டமன்றங்களை விருப்பம்போல கலைக்க நாடாளுமன்றத்திற்கு அதிகாரம் அளிக்கிறது.",
            "தேசிய அவசரநிலையின் போது இது அடிப்படை உரிமைகளுக்குப் பதிலாக செயல்படுகிறது."
        ],
        correct_ans="B",
        exp_en="The ultimate constitutional significance of the Preamble is that it embodies the noble vision, moral values, and fundamental philosophical foundation on which the Indian Democratic Republic is built.",
        exp_ta="முகவுரையின் இறுதி அரசியலமைப்பு முக்கியத்துவம் என்னவெனில், இந்திய ஜனநாயகக் குடியரசு கட்டமைக்கப்பட்டுள்ள உன்னதமான தொலைநோக்கு, நெறிமுறை மதிப்புகள் மற்றும் அடிப்படை தத்துவப் அடித்தளத்தை இது வெளிப்படுத்துவதாகும்.",
        wno_dict={
            "A": {"en": "Incorrect. IPC is penal code, not Preamble.", "ta": "தவறு. IPC தான் தண்டனைச் சட்டம்."},
            "B": {"en": "Correct. Embodies foundational philosophy and grand vision of Constitution.", "ta": "சரி. அரசியலமைப்பின் அடிப்படை தத்துவம் மற்றும் உன்னத தொலைநோக்கை வெளிப்படுத்துகிறது."},
            "C": {"en": "Incorrect. Article 356 governs state dissolution.", "ta": "தவறு. உறுப்பு 356 மாநிலக் கலைப்பைக் ஆள்கிறது."},
            "D": {"en": "Incorrect. Articles 358 & 359 govern emergency suspension.", "ta": "தவறு. உறுப்புகள் 358 & 359 அவசரநிலையைக் கையாள்கின்றன."}
        },
        tip_en="Preamble = Soul, Identity Card, and Philosophical Blueprint of the Constitution.",
        tip_ta="முகவுரை = அரசியலமைப்பின் ஆன்மா, அடையாள அட்டை மற்றும் தத்துவ நீலவரைபடம்.",
        rev_en="Preamble = Moral values & philosophical foundation of Indian Republic.",
        rev_ta="முகவுரை = இந்தியக் குடியரசின் நெறிமுறை மதிப்புகள் & தத்துவ அடித்தளம்.",
        sources=["Preamble Notes Part 1 & 2"],
        bloom="Understand", est_sec=30, pyq_sim="High", tags=["Significance", "Preamble Philosophy"]
    ))

    return qs
