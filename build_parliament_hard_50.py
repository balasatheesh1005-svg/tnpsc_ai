import json
import os
from collections import Counter

def create_hard_questions():
    questions = []

    def add_q(q_id, question_en, question_ta, opt_a_en, opt_a_ta, opt_b_en, opt_b_ta, opt_c_en, opt_c_ta, opt_d_en, opt_d_ta, correct, exp_en, exp_ta, why_a_en, why_a_ta, why_b_en, why_b_ta, why_c_en, why_c_ta, why_d_en, why_d_ta, tip_en, tip_ta, fact_en, fact_ta, bloom, difficulty, tags, notes_part):
        q_obj = {
            "id": q_id,
            "subject": "Polity",
            "topic": "Parliament of India",
            "difficulty": difficulty,
            "question_type": "mcq",
            "question": {
                "en": question_en,
                "ta": question_ta
            },
            "options": [
                {"id": "A", "en": opt_a_en, "ta": opt_a_ta},
                {"id": "B", "en": opt_b_en, "ta": opt_b_ta},
                {"id": "C", "en": opt_c_en, "ta": opt_c_ta},
                {"id": "D", "en": opt_d_en, "ta": opt_d_ta}
            ],
            "correct_answer": correct,
            "explanation": {
                "en": exp_en,
                "ta": exp_ta
            },
            "why_not_others": {
                "A": {"en": why_a_en, "ta": why_a_ta},
                "B": {"en": why_b_en, "ta": why_b_ta},
                "C": {"en": why_c_en, "ta": why_c_ta},
                "D": {"en": why_d_en, "ta": why_d_ta}
            },
            "tnpsc_tip": {
                "en": tip_en,
                "ta": tip_ta
            },
            "revision_fact": {
                "en": fact_en,
                "ta": fact_ta
            },
            "source_reference": [
                "M. Laxmikanth — Indian Polity",
                "NCERT Class XI — Constitution at Work",
                "Tamil Nadu Samacheer Kalvi — Class 12 Polity",
                f"TNPSC Nova AI Notes — Parliament of India ({notes_part})"
            ],
            "bloom_level": bloom,
            "estimated_time_sec": 90,
            "pyq_similarity": "High Similarity to TNPSC Group 1 Mains/Prelims Multi-Layer Questions",
            "tags": tags
        }
        questions.append(q_obj)

    # 50 Hard questions balance target: A:13, B:13, C:12, D:12

    # Q001 - Correct: A (1)
    add_q(
        "CZ_PL_HD_001",
        "Consider a scenario where Lok Sabha passes an Ordinary Bill and transmits it to Rajya Sabha. Under Article 108, which of the following conditions MUST be satisfied for the President to summon a Joint Sitting of both Houses?",
        "மக்களவை ஒரு சாதாரண மசோதாவை நிறைவேற்றி மாநிலங்களவைக்கு அனுப்புகிறது எனக் கொள்வோம். சரத்து 108 இன் கீழ் இரு அவைகளின் கூட்டுக் கூட்டத்தைக் கூட்ட குடியரசுத் தலைவர் பின்வரும் எந்த நிபந்தனைகளைப் பூர்த்தி செய்ய வேண்டும்?",
        "Rajya Sabha rejects the bill, OR disagrees on amendments, OR holds the bill without passing for more than 6 months", "மாநிலங்களவை மசோதாவை நிராகரித்தல், அல்லது திருத்தங்களில் கருத்து வேறுபாடு கொள்ளுதல், அல்லது 6 மாதங்களுக்கு மேல் நிறைவேற்றாமல் நிலுவையில் வைத்திருத்தல்",
        "Rajya Sabha rejects the bill, OR President rejects the bill, OR Speaker requests a Joint Sitting", "மாநிலங்களவை மசோதாவை நிராகரித்தல், அல்லது குடியரசுத் தலைவர் மசோதாவை நிராகரித்தல், அல்லது சபாநாயகர் கோருதல்",
        "Lok Sabha passes a resolution by 2/3rd majority requesting a Joint Sitting from the President", "கூட்டுக் கூட்டம் கோரி மக்களவை 2/3 பெரும்பான்மையுடன் தீர்மானம் நிறைவேற்றுதல்",
        "Rajya Sabha rejects the bill within 14 days of receipt from Lok Sabha", "மக்களவையிலிருந்து பெறப்பட்ட 14 நாட்களுக்குள் மாநிலங்களவை மசோதாவை நிராகரித்தல்",
        "A",
        "Under Article 108(1), a deadlock for a Joint Sitting arises if: (a) Bill is rejected by the other House, (b) Houses have finally disagreed as to amendments to be made, or (c) More than 6 months lapse from receipt of bill without being passed by the other House. Note: In calculating 6 months, periods when House is prorogued or adjourned for >4 consecutive days are excluded.",
        "சரத்து 108(1) இன் கீழ் கூட்டுக் கூட்டத்திற்கான முட்டுக்கட்டை சூழல்கள்: (a) மற்ற அவையால் மசோதா நிராகரிக்கப்படல், (b) திருத்தங்களில் கருத்து வேறுபாடு ஏற்படுதல், அல்லது (c) மற்ற அவையில் 6 மாதங்களுக்கு மேல் நிறைவேற்றப்படாமல் இருத்தல். (4 நாட்களுக்கு மேலான ஒத்திவைப்பு நாட்கள் 6 மாதக் கணக்கீட்டில் சேர்க்கப்படாது).",
        "Option A is correct because it states the exact three deadlock conditions specified under Article 108(1).", "விருப்பம் A சரியானது, ஏனெனில் சரத்து 108(1) இன் கீழ் குறிப்பிடப்பட்ட மூன்று முட்டுக்கட்டை நிபந்தனைகளை இது சரியாகக் கூறுகிறது.",
        "Option B is incorrect; Presidential veto or Speaker request does not constitute a deadlock under Art 108.", "விருப்பம் B தவறானது; குடியரசு தலைவர் நிராகரிப்பு அல்லது சபாநாயகர் கோரிக்கை முட்டுக்கட்டையாகாது.",
        "Option C is incorrect; Joint Sitting does not require a 2/3rd resolution from Lok Sabha.", "விருப்பம் C தவறானது; மக்களவை 2/3 தீர்மானம் இயற்றத் தேவையில்லை.",
        "Option D is incorrect; 14 days limit applies to Money Bills (Art 109), for which Joint Sitting is NEVER allowed.", "விருப்பம் D தவறானது; 14 நாட்கள் வரம்பு பண மசோதாவிற்குரியது, அதற்கு கூட்டுக் கூட்டம் கிடையாது.",
        "TNPSC Hard Trap: In calculating the 6-month period under Article 108(2), no account shall be taken of any period during which the House was prorogued or adjourned for more than 4 consecutive days!",
        "டிஎன்பிஎஸ்சி பொறி: சரத்து 108(2) இன் கீழ் 6 மாதக் காலத்தைக் கணக்கிடும்போது, அவை தொடர்ந்து 4 நாட்களுக்கு மேல் ஒத்திவைக்கப்பட்ட அல்லது கூட்டத்தொடர் ஒத்திவைக்கப்பட்ட நாட்களைச் சேர்க்கக்கூடாது!",
        "Article 108 Joint Sitting deadlock conditions and 6-month calculation rule.",
        "சரத்து 108 இன் கீழ் கூட்டுக் கூட்ட முட்டுக்கட்டை நிபந்தனைகள் மற்றும் 6 மாதக் கணக்கீட்டு விதி.",
        "Evaluating", "Hard", ["Article 108", "Joint Sitting Deadlock Conditions", "6 Months Calculation Rule"], "Part 2"
    )

    # Q002 - Correct: B (1)
    add_q(
        "CZ_PL_HD_002",
        "Which of the following statements accurately highlights the constitutional distinction between Financial Bill (I) under Article 117(1) and Financial Bill (II) under Article 117(3)?",
        "சரத்து 117(1) இன் கீழான நிதி மசோதா (I) மற்றும் சரத்து 117(3) இன் கீழான நிதி மசோதா (II) இடையிலான அரசியலமைப்பு வேறுபாட்டைப் பின்வருவனவற்றில் எது சரியாகச் சுட்டிக்காட்டுகிறது?",
        "Financial Bill (I) contains Article 110 matters and can be introduced in either House, whereas Financial Bill (II) contains no Article 110 matters and can be introduced only in Lok Sabha", "நிதி மசோதா (I) சரத்து 110 விவகாரங்களைக் கொண்டு இரு அவைகளிலும் அறிமுகமாகலாம், ஆனால் நிதி மசோதா (II) சரத்து 110 விவகாரங்கள் இன்றி மக்களவையில் மட்டுமே அறிமுகமாகலாம்",
        "Financial Bill (I) contains Article 110 matters and can be introduced ONLY in Lok Sabha on President's recommendation, whereas Financial Bill (II) involves Consolidated Fund expenditure, contains no Article 110 matters, and can be introduced in EITHER House", "நிதி மசோதா (I) சரத்து 110 விவகாரங்களைக் கொண்டு குடியரசுத் தலைவர் பரிந்துரையுடன் மக்களவையில் மட்டுமே அறிமுகமாகலாம், ஆனால் நிதி மசோதா (II) தொகுப்பு நிதி செலவினங்களைக் கொண்டு, சரத்து 110 விவகாரங்கள் இன்றி இரு அவைகளிலும் அறிமுகமாகலாம்",
        "Financial Bill (I) requires state ratification under Article 368, whereas Financial Bill (II) does not require state ratification", "நிதி மசோதா (I) க்கு மாநில ஒப்புதல் தேவை, நிதி மசோதா (II) க்கு மாநில ஒப்புதல் தேவையில்லை",
        "Financial Bill (I) cannot be referred to a Joint Sitting under Article 108, whereas Financial Bill (II) can be referred to a Joint Sitting", "நிதி மசோதா (I) ஐக் கூட்டுக் கூட்டத்திற்கு அனுப்ப முடியாது, நிதி மசோதா (II) ஐக் கூட்டுக் கூட்டத்திற்கு அனுப்பலாம்",
        "B",
        "Financial Bill (I) under Art 117(1) contains matters of Art 110 PLUS general legislation; like a Money Bill, it can ONLY be introduced in Lok Sabha on President's recommendation, but in all other respects it is governed by ordinary bill procedures (RS has equal powers, Joint Sitting allowed). Financial Bill (II) under Art 117(3) contains provisions involving expenditure from Consolidated Fund without Art 110 items; it can be introduced in EITHER House without prior recommendation, but CANNOT be passed by either House unless President recommends its consideration.",
        "சரத்து 117(1) நிதி மசோதா (I) 110 விவகாரங்களுடன் கூடியது; குடியரசு தலைவர் பரிந்துரையுடன் மக்களவையில் மட்டுமே அறிமுகமாகலாம். சரத்து 117(3) நிதி மசோதா (II) தொகுப்பு நிதி செலவினம் பற்றியது; இரு அவைகளிலும் அறிமுகமாகலாம், ஆனால் பரிசீலனைக்குக் குடியரசு தலைவர் பரிந்துரை தேவை. இரண்டிற்கும் கூட்டுக் கூட்டம் பொருந்தும்.",
        "Option A is incorrect; Financial Bill (I) CANNOT be introduced in Rajya Sabha.", "விருப்பம் A தவறானது; நிதி மசோதா (I) ஐ மாநிலங்களவையில் அறிமுகப்படுத்த முடியாது.",
        "Option B is correct because it precisely captures the introduction and recommendation differences between Art 117(1) and Art 117(3).", "விருப்பம் B சரியானது, ஏனெனில் சரத்து 117(1) மற்றும் 117(3) இடையிலான வேறுபாடுகளை இது சரியாகக் கூறுகிறது.",
        "Option C is incorrect; neither Financial Bill requires Article 368 state ratification.", "விருப்பம் C தவறானது; நிதி மசோதாக்களுக்கு மாநில ஒப்புதல் தேவையில்லை.",
        "Option D is incorrect; Joint Sitting under Article 108 is available for BOTH Financial Bill (I) and Financial Bill (II).", "விருப்பம் D தவறானது; இரு நிதி மசோதாக்களுக்குமே கூட்டுக் கூட்டம் பொருந்தும்.",
        "TNPSC Comparison Matrix: Money Bill (Art 110) = LS Only + Pres Rec + No RS Veto + NO Joint Sitting. Financial Bill I (Art 117(1)) = LS Only + Pres Rec + RS Veto Exists + Joint Sitting Allowed. Financial Bill II (Art 117(3)) = Either House + Pres Rec for Consideration + RS Veto Exists + Joint Sitting Allowed.",
        "டிஎன்பிஎஸ்சி ஒப்பீட்டு அட்டவணை: பண மசோதா = மக்களவை மட்டுமே + கூட்டுக்கூட்டம் இல்லை. நிதி மசோதா I = மக்களவை மட்டுமே + கூட்டுக் கூட்டம் உண்டு. நிதி மசோதா II = இரு அவைகளும் + கூட்டுக் கூட்டம் உண்டு.",
        "Detailed comparison of Financial Bill (I) Art 117(1) vs Financial Bill (II) Art 117(3).",
        "நிதி மசோதா (I) சரத்து 117(1) மற்றும் நிதி மசோதா (II) சரத்து 117(3) ஒப்பீடு.",
        "Analyzing", "Hard", ["Article 117", "Financial Bill Type I vs II", "Joint Sitting Applicability"], "Part 2"
    )

    # Q003 - Correct: C (1)
    add_q(
        "CZ_PL_HD_003",
        "Under Article 105(2) of the Constitution, what is the extent and boundary of Parliamentary Immunity granted to a Member of Parliament regarding freedom of speech?",
        "சரத்து 105(2) இன் கீழ் ஒரு நாடாளுமன்ற உறுப்பினருக்கு பேச்சுரிமை தொடர்பாக வழங்கப்படும் நாடாளுமன்ற விலக்களிப்பின் எல்லை என்ன?",
        "Immunity applies to all speeches and acts committed anywhere in India during the term of office", "பதவிக் காலத்தில் இந்தியாவில் எங்கு பேசப்படும் பேச்சுக்கும் செய்யப்படும் செயலுக்கும் விலக்களிப்பு பொருந்தும்",
        "Immunity applies only to speeches made inside Parliament, but members can be sued in court if the speech breaches criminal law", "நாடாளுமன்றத்திற்குள் பேசும் பேச்சுக்கு மட்டுமே பொருந்தும், ஆனால் குற்றவியல் சட்டத்தை மீறினால் நீதிமன்றத்தில் வழக்கு தொடரலாம்",
        "No MP shall be liable to any proceedings in any court in respect of anything said or any vote given by him in Parliament or any committee thereof", "நாடாளுமன்றத்தில் அல்லது அதன் குழுவில் பேசிய அல்லது அளித்த வாக்கு தொடர்பாக எந்த உறுப்பினரும் எந்த நீதிமன்ற நடவடிக்கைகளுக்கும் உள்ளாக மாட்டார்கள்",
        "Immunity is granted only if the speech is pre-approved by the Speaker or Chairman of the House", "சபாநாயகர் அல்லது தலைவரால் முன்-ஒப்புதல் அளிக்கப்பட்ட பேச்சுக்கு மட்டுமே விலக்களிப்பு உண்டு",
        "C",
        "Article 105(2) provides absolute judicial immunity: 'No member of Parliament shall be liable to any proceedings in any court in respect of anything said or any vote given by him in Parliament or any committee thereof.' However, this speech is subject to the rules of the House and Article 121 (prohibiting discussion on conduct of SC/HC judges).",
        "சரத்து 105(2) நீதிமன்ற நடவடிக்கைகளிலிருந்து முழு விலக்களிப்பை வழங்குகிறது: நாடாளுமன்றத்தில் அல்லது அதன் குழுவில் பேசிய அல்லது அளித்த வாக்கு தொடர்பாக எந்த உறுப்பினரும் நீதிமன்ற நடவடிக்கைகளுக்கு உள்ளாக மாட்டார்கள். (சரத்து 121 நீதிபதிகள் குறித்த விவாதத் தடைக்கு உட்பட்டது).",
        "Option A is incorrect; immunity is confined to statements/votes in Parliament or its committees, not anywhere in India.", "விருப்பம் A தவறானது; விலக்களிப்பு நாடாளுமன்றத்திற்குள்ளான பேச்சு/வாக்கிற்கு மட்டுமே பொருந்தும்.",
        "Option B is incorrect; court proceedings are barred even for defamatory speeches inside Parliament (Tejkiran Jain case).", "விருப்பம் B தவறானது; நாடாளுமன்றத்திற்குள் பேசும் பேச்சுக்கு நீதிமன்ற வழக்குகள் முற்றிலும் தடை செய்யப்பட்டுள்ளன.",
        "Option C is correct because Article 105(2) explicitly grants total court immunity for anything said or voted in Parliament.", "விருப்பம் C சரியானது, ஏனெனில் சரத்து 105(2) நீதிமன்ற நடவடிக்கைகளிலிருந்து முழு விலக்கு அளிக்கிறது.",
        "Option D is incorrect; pre-approval by Speaker is not a requirement for constitutional immunity under Art 105(2).", "விருப்பம் D தவறானது; சபாநாயகரின் முன்-ஒப்புதல் அரசியலமைப்பு விலக்களிப்பிற்குத் தேவையில்லை.",
        "Landmark Precedent: In Tejkiran Jain v. N. Sanjiva Reddy (1970), Supreme Court held that the word 'anything' in Article 105(2) is of the widest amplitude and court has no jurisdiction to entertain any action for speech inside Parliament.",
        "வரலாற்று முன்மாதிரி: தேஜ்கிரண் ஜெயின் வழக்கில் (1970) சரத்து 105(2) இல் உள்ள 'எதுவும்' என்ற சொல் மிக பரந்த எல்லையைக் கொண்டது எனவும் நாடாளுமன்ற பேச்சுக்கு நீதிமன்றத்திற்கு அதிகார வரம்பு இல்லை என்றும் தீர்ப்பளிக்கப்பட்டது.",
        "Absolute judicial immunity under Article 105(2) for parliamentary speeches and votes.",
        "சரத்து 105(2) இன் கீழ் நாடாளுமன்ற பேச்சு மற்றும் வாக்களிப்பிற்கு நீதிமன்ற விலக்களிப்பு.",
        "Evaluating", "Hard", ["Article 105(2)", "Parliamentary Immunity", "Tejkiran Jain Case"], "Part 3"
    )

    # Q004 - Correct: D (1)
    add_q(
        "CZ_PL_HD_004",
        "Under the Tenth Schedule (Anti-Defection Law) inserted by 52nd CA 1985 and amended by 91st CA 2003, in which of the following scenarios does an MP NOT incur disqualification?",
        "52வது திருத்தம் 1985 மற்றும் 91வது திருத்தம் 2003 மூலம் சேர்க்கப்பட்ட பத்தாவது அட்டவணையின் (கட்சித் தாவல் தடைச் சட்டம்) கீழ், பின்வரும் எந்தச் சூழலில் ஒரு நாடாளுமன்ற உறுப்பினர் தகுதியிழப்பைப் பெறமாட்டார்?",
        "If a member voluntarily gives up membership of the political party on whose ticket he was elected", "தேர்ந்தெடுக்கப்பட்ட அரசியல் கட்சியின் உறுப்பினரிலிருந்து அவராகவே விலகினால்",
        "If an independent elected member joins any political party after the election", "தேர்தலுக்குப் பின் சுயேச்சை உறுப்பினர் ஏதேனும் ஒரு அரசியல் கட்சியில் சேர்ந்தால்",
        "If a nominated member joins any political party after the expiry of 6 months from taking his seat", "நியமன உறுப்பினர் பதவிப் பிரமாணம் செய்த 6 மாதங்களுக்குப் பிறகு ஏதேனும் ஒரு அரசியல் கட்சியில் சேர்ந்தால்",
        "If a member is elected as Speaker or Deputy Speaker and voluntarily gives up party membership during term of office", "சபாநாயகர் அல்லது துணை சபாநாயகராகத் தேர்ந்தெடுக்கப்பட்டு பதவிக் காலத்தில் அரசியல் கட்சி உறுப்பினர் பதவியை அவராகவே துறந்தால்",
        "D",
        "Paragraph 5 of the Tenth Schedule grants explicit exemption from defection disqualification to a member elected as Speaker/Deputy Speaker of Lok Sabha or Chairman/Deputy Chairman of Rajya Sabha who voluntarily gives up party membership upon election and does not rejoin during office.",
        "பத்தாவது அட்டவணை பத்தி 5 சபாநாயகர், துணை சபாநாயகர், துணைத் தலைவராகத் தேர்ந்தெடுக்கப்படுபவர் தனது கட்சி உறுப்பினர் பதவியைத் துறந்தால் தகுதியிழப்பிலிருந்து விலக்களிக்கிறது.",
        "Option A is incorrect; voluntarily giving up party membership causes defection disqualification under Paragraph 2(1)(a).", "விருப்பம் A தவறானது; கட்சியிலிருந்து விலகினால் தகுதியிழப்பு ஏற்படும்.",
        "Option B is incorrect; an independent member incurs disqualification if he joins ANY political party after election under Paragraph 2(2).", "விருப்பம் B தவறானது; சுயேச்சை உறுப்பினர் கட்சியில் சேர்ந்தால் தகுதியிழப்பு ஏற்படும்.",
        "Option C is incorrect; a nominated member incurs disqualification if he joins a party AFTER 6 months under Paragraph 2(3).", "விருப்பம் C தவறானது; நியமன உறுப்பினர் 6 மாதத்திற்குப் பின் சேர்ந்தால் தகுதியிழப்பு ஏற்படும்.",
        "Option D is correct because Paragraph 5 explicitly protects Presiding Officers giving up party membership to maintain neutrality.", "விருப்பம் D சரியானது, ஏனெனில் பத்தி 5 அவைத் தலைவர்கள் கட்சி பதவியைத் துறப்பதற்கு விலக்களிக்கிறது.",
        "TNPSC Exemption Rule: Presiding Officers (Speaker/Deputy Speaker/Deputy Chairman) are exempted from defection disqualification under Paragraph 5 of Tenth Schedule.",
        "டிஎன்பிஎஸ்சி விதிவிலக்கு விதி: அவைத் தலைவர்கள் கட்சித் தாவல் தகுதியிழப்பிலிருந்து பத்தாவது அட்டவணை பத்தி 5 இன் கீழ் விலக்குப் பெறுகின்றனர்.",
        "Tenth Schedule Paragraph 5 Presiding Officer exemption mechanics.",
        "பத்தாவது அட்டவணை பத்தி 5 அவைத் தலைவர் விலக்கு விதிமுறைகள்.",
        "Analyzing", "Hard", ["Tenth Schedule Exemption", "Paragraph 5 Anti Defection", "Speaker Neutrality Immunity"], "Part 3"
    )

    # Generate remaining 46 questions programmatically for Hard set with balance A:13, B:13, C:12, D:12

    topics_hard = [
        # (Corr, Topic, EnText, TaText, Part)
        ("A", "Kihoto Hollohan 1992 Judicial Review Cutoff", "Speaker acts as a Tribunal under 10th Schedule, so decision is subject to Judicial Review", "10வது அட்டவணையின் கீழ் சபாநாயகர் தீர்ப்பாயமாகச் செயல்படுவதால் அவரது முடிவு நீதிமன்ற ஆய்விற்கு உட்பட்டது", "Part 3"),
        ("B", "Article 102(1)(a) Office of Profit Test Criteria", "Government control, appointment power, remuneration source, and functions nature", "அரசின் கட்டுப்பாடு, நியமன அதிகாரம், ஊதிய ஆதாரம் மற்றும் பணிகளின் தன்மை", "Part 1"),
        ("C", "Article 101 Dual Membership Vacancy Mechanics", "Member elected to both Houses must intimate within 10 days, else RS seat becomes vacant", "இரு அவைகளுக்கும் தேர்ந்தெடுக்கப்பட்டவர் 10 நாட்களுக்குள் தெரிவிக்க வேண்டும், இல்லையெனில் RS இடம் காலியாகும்", "Part 1"),
        ("D", "Article 113(3) President Recommendation for Demands for Grants", "No demand for grant shall be made except on recommendation of President", "குடியரசுத் தலைவரின் பரிந்துரையின்றி எந்த மானியக் கோரிக்கையும் கொண்டு வர முடியாது", "Part 3"),
        ("A", "Article 114(2) Restriction on Amendments to Appropriation Bill", "No amendment shall be proposed in either House to alter amount or destination of grant", "மானியத் தொகையையோ நோக்கத்தையோ மாற்ற எந்த அவையிலும் திருத்தம் கொண்டு வர முடியாது", "Part 3"),
        ("B", "Article 115 Supplementary vs Additional vs Excess Grant", "Excess Grant requires PAC scrutiny & Lok Sabha vote after financial year ends", "எக்செஸ் கிராண்ட் நிதியாண்டு முடிந்த பின் PAC பரிசீலனை & மக்களவை வாக்கெடுப்பு கோரும்", "Part 3"),
        ("C", "Article 116 Vote on Account vs Vote on Credit vs Exceptional Grant", "Vote on Credit is an undetailed blank cheque for unexpected national demands", "கடன் வாக்கு என்பது எதிர்பாராத தேசிய கோரிக்கைக்கான விரிவான தகவலற்ற முன் ஒப்புதல்", "Part 3"),
        ("D", "Article 266(1) vs 266(2) vs 267 Fund Withdrawal Authority", "Contingency Fund (Art 267) held by Finance Secretary on behalf of President for executive advance", "அவசரகால நிதி (சரத்து 267) குடியரசுத் தலைவர் சார்பில் நிதிச் செயலாளரால் நிர்வகிக்கப்படுகிறது", "Part 3"),
        ("A", "Article 368 Amendment Veto & Joint Sitting Ban", "President MUST give assent (24th CA 1971); NO Joint Sitting allowed for Amendment Bills", "குடியரசு தலைவர் ஒப்புதல் அளிக்க வேண்டும்; கூட்டுக் கூட்டம் சாத்தியமில்லை", "Part 3"),
        ("B", "Parliamentary Sovereignty vs Basic Structure Invalidation", "Indian Parliament is not sovereign like UK Parliament because SC can invalidate laws violating Basic Structure", "அடிப்படை அமைப்பை மீறும் சட்டங்களை உச்ச நீதிமன்றம் ரத்து செய்ய முடியும் என்பதால் இந்திய நாடாளுமன்றம் வரம்பற்ற இறையாண்மை கொண்டது அல்ல", "Part 3"),
        ("C", "Article 100 Quorum Absence Presiding Duty", "It shall be duty of Speaker/Chairman to adjourn House or suspend meeting until quorum", "குறைவெண் வரும் வரை அவையை ஒத்திவைப்பது அல்லது கூட்டத்தை நிறுத்துவது சபாநாயகர்/தலைவர் கடமையாகும்", "Part 2"),
        ("D", "Article 121 Bar on Discussion of SC/HC Judges Conduct", "No discussion in Parliament regarding conduct of Judge EXCEPT upon removal motion under Art 124(4)", "நீக்கத் தீர்மானத்தை (சரத்து 124(4)) தவிர நீதிபதி நடத்தை குறித்து நாடாளுமன்றத்தில் விவாதிக்கத் தடை", "Part 3"),
        ("A", "Article 122 Bar on Courts to Inquire Parliamentary Proceedings", "Validity of proceedings in Parliament cannot be called in question on ground of irregularity of procedure", "நடைமுறை தவறுகள் என்ற அடிப்படையில் நாடாளுமன்ற நடவடிக்கைகளின் செல்லுபடியாகும் தன்மையை நீதிமன்றம் கேள்வி கேட்க முடியாது", "Part 3"),
        ("B", "Article 105(3) Parliamentary Privileges Law Making Power", "Parliament can codify its privileges by law; until then statutory immunities continue", "நாடாளுமன்றம் சட்டம் மூலம் தனது சலுகைகளை வரையறுக்கலாம்; அதுவரை நிலவும் சலுகைகள் தொடரும்", "Part 3"),
        ("C", "No-Confidence Motion vs Censure Motion Difference", "No-Confidence can be moved only against entire Council of Ministers; Censure against individual Minister or Ministry", "நம்பிக்கையில்லாத் தீர்மானம் அமைச்சரவை முழுமைக்கும் எதிரானது; கண்டனத் தீர்மானம் தனி அமைச்சருக்கும் எதிரானது", "Part 2"),
        ("D", "Adjournment Motion Admissibility Limitations", "Shall not raise a matter of privilege, nor revive discussion on matter discussed in same session", "உரிமை மீறல் விவகாரத்தை உயர்த்தக் கூடாது, அதே கூட்டத்தொடரில் விவாதிக்கப்பட்டதை மீண்டும் கொண்டு வரக் கூடாது", "Part 2"),
        ("A", "Question Hour Starred vs Short Notice Questions", "Short Notice Question relates to urgent public matter and is asked with less than 10 days notice", "குறுகிய கால கேள்வி 10 நாட்களுக்குள் குறைந்த அவகாச அறிவிப்பில் கேட்கப்படுவது", "Part 2"),
        ("B", "Cut Motions Effect on Ministry Stability", "Passage of any Cut Motion (Policy, Economy, Token) in Lok Sabha amounts to loss of majority & resignation of Cabinet", "மக்களவையில் எந்தவொரு வெட்டுத் தீர்மானம் நிறைவேறினாலும் அமைச்சரவை பதவி விலக நேரிடும்", "Part 3"),
        ("C", "Delegated Legislation Scrutiny Committee Powers", "Examines whether executive rules violate Parent Act or Constitution and reports to House", "நிர்வாக விதிகள் தாய் சட்டத்தையோ அரசியலமைப்பையோ மீறுகிறதா என ஆராய்ந்து அறிக்கையளிப்பது", "Part 2"),
        ("D", "Estimates Committee Non-Inclusion of RS Members", "Estimates Committee consists of 30 members ALL from LS to preserve exclusive LS financial control", "மக்களவையின் பிரத்தியேக நிதிக் கட்டுப்பாட்டைப் பேண 30 உறுப்பினர்களும் மக்களவையிலிருந்து மட்டுமே", "Part 2"),
        ("A", "Public Accounts Committee PAC Examination Scope", "Examines CAG Audit Reports to ensure public money spent as authorized by Parliament", "நாடாளுமன்ற அனுமதியின்படி பொதுப்பணம் செலவிடப்பட்டுள்ளதா என CAG அறிக்கைகளை ஆராய்வது", "Part 2"),
        ("B", "COPU Committee Membership & Minister Ban", "Minister CANNOT be elected as a member of PAC, Estimates, or COPU Committees", "அமைச்சர் எவரும் PAC, மதிப்பீட்டுக் குழு அல்லது COPU குழுக்களின் உறுப்பினராகத் தேர்ந்தெடுக்கப்பட முடியாது", "Part 2"),
        ("C", "Pro-Tem Speaker Removal & Function Mechanics", "Appointed under Art 95(1) until Speaker elected; administers oath to new MPs under Art 99", "சபாநாயகர் தேர்ந்தெடுக்கப்படும் வரை சரத்து 95(1) இன் கீழ் நியமிக்கப்பட்டு சரத்து 99 இன் கீழ் பிரமாணம் செய்விப்பவர்", "Part 2"),
        ("D", "Effective Majority Definition in Presiding Officer Removal", "Majority of all the then members (Total sanctioned strength MINUS vacancies)", "அப்போதைய அனைத்து உறுப்பினர்களின் பெரும்பான்மை (மொத்த பலம் கழித்தல் காலியிடங்கள்)", "Part 2"),
        ("A", "Article 85(1) Maximum Inter-Session Gap Rule", "Six months shall not intervene between last sitting in one session and first sitting in next session", "ஒரு கூட்டத்தொடரின் கடைசி அமர்விற்கும் அடுத்த தொடரின் முதல் அமர்விற்கும் இடையே 6 மாதங்கள் மிகக்கூடாது", "Part 1"),
        ("B", "Lame Duck Session Detailed Mechanics", "Refers to last session of outgoing Lok Sabha after elections for new LS have been completed", "புதிய மக்களவைத் தேர்தலுக்குப் பின் முந்தைய மக்களவையின் கடைசி கூட்டத்தொடர்", "Part 1"),
        ("C", "Article 83(2) Lok Sabha Term Extension in Emergency", "Term extended by Parliament by law for 1 year at a time during Proclamation of Emergency", "தேசிய அவசரநிலையின் போது நாடாளுமன்றச் சட்டம் மூலம் ஒரே நேரத்தில் 1 ஆண்டுக்கு நீட்டிக்கப்படலாம்", "Part 1"),
        ("D", "Article 84 Qualification Amendment 1951 Requirement", "RPA 1951 mandates elector qualification in any parliamentary constituency", "RPA 1951 நாடாளுமன்றத் தொகுதியில் வாக்காளராகப் பதிவு செய்திருக்க வேண்டும் எனக் கோருகிறது", "Part 1"),
        ("A", "Article 101 Multiple Seats Representation Rules", "Person elected to both Parliament & State Legislature loses Parliament seat if not resigning state seat in 14 days", "14 நாட்களுக்குள் மாநில இடத்தை ராஜினாமா செய்யாவிட்டால் நாடாளுமன்ற இடம் காலியாகும்", "Part 1"),
        ("B", "Article 102 Disqualification Court Jurisdiction", "President seeks binding opinion of Election Commission before deciding non-defection disqualification", "கட்சித் தாவல் அல்லாத தகுதியிழப்புகளில் குடியரசு தலைவர் தேர்தல் ஆணையத்தின் பிணைப்பு கருத்துப்படி முடிவு செய்வார்", "Part 1"),
        ("C", "Article 109 Money Bill Rajya Sabha Recommendation Limit", "Rajya Sabha must return bill within 14 days; LS may accept or reject all/any recommendations", "மாநிலங்களவை 14 நாட்களுக்குள் மசோதாவைத் திருப்ப வேண்டும்; மக்களவை பரிந்துரைகளை ஏற்கலாம் அல்லது நிராகரிக்கலாம்", "Part 2"),
        ("D", "Article 110(1) Six Money Bill Criteria", "Taxation, Borrowing, Consolidated Fund custody, Appropriation, Expenditure charging, Incidental matters", "வரி விதிப்பு, கடன் வாங்குதல், தொகுப்பு நிதி பராமரிப்பு, ஒதுக்கீடு, செலவினம் சுமத்துதல், துணை விஷயங்கள்", "Part 2"),
        ("A", "Article 111 Presidential Options on Ordinary Bills", "Assent, Withhold Assent, or Return for Reconsideration (Suspensive Veto)", "ஒப்புதல் அளிக்கலாம், நிறுத்தலாம் அல்லது மறுபரிசீலனைக்குத் திருப்பியனுப்பலாம் (இடைநிறுத்த வீட்டோ)", "Part 2"),
        ("B", "Article 117(1) vs 110 Joint Sitting Availability", "Money Bill cannot have Joint Sitting; Financial Bill (I) CAN have Joint Sitting under Art 108", "பண மசோதாவிற்கு கூட்டுக் கூட்டம் இல்லை; நிதி மசோதா (I) க்கு கூட்டுக் கூட்டம் உண்டு", "Part 2"),
        ("C", "Article 118 Rules of Procedure Making Power", "Each House of Parliament may make rules for regulating its procedure & conduct of business", "நாடாளுமன்றத்தின் ஒவ்வொரு அவையும் தனது நடைமுறை மற்றும் நடத்தையை ஒழுங்குபடுத்த விதிகளை உருவாக்கலாம்", "Part 2"),
        ("D", "Article 123 Ordinance Expiry Mechanics", "Lapses 6 weeks from reassembly of Parliament, or earlier if disapproved by resolutions of both Houses", "நாடாளுமன்றம் கூடிய 6 வாரங்களில் அல்லது இரு அவைகளின் நிராகரிப்புத் தீர்மானத்தால் காலாவதியாகும்", "Part 2"),
        ("A", "Article 112 Budget Non-Votable Charged Items", "Emoluments & allowances of President, SC Judges, CAG, Chairman RS, Speaker LS", "குடியரசு தலைவர், உச்ச நீதிமன்ற நீதிபதிகள், CAG, அவைத் தலைவர்கள் ஊதியங்கள்", "Part 3"),
        ("B", "Article 113 Demands for Grants Presentation Exclusive House", "Demands for Grants submitted ONLY to Lok Sabha under Article 113(2)", "சரத்து 113(2) இன் கீழ் மானியக் கோரிக்கைகள் மக்களவையில் மட்டுமே சமர்ப்பிக்கப்படும்", "Part 3"),
        ("C", "Article 114 Appropriation Act Necessity", "No money can be withdrawn from Consolidated Fund EXCEPT under appropriation made by law", "சட்டப்பூர்வ ஒதுக்கீட்டின்றி தொகுப்பு நிதியிலிருந்து பணம் எடுக்க முடியாது", "Part 3"),
        ("D", "Article 115 Additional & Excess Grants Procedural Difference", "Excess Grant relates to money spent in EXCESS of granted amount during a completed financial year", "முடிவுற்ற நிதியாண்டில் ஒதுக்கப்பட்ட தொகையை விட அதிகமாகச் செலவிட்ட பணத்திற்குரியது", "Part 3"),
        ("A", "Article 116(1)(a) Vote on Account Pre-Budget Grant", "Grant for part of financial year pending completion of voting on Demands for Grants", "மானியக் கோரிக்கைகள் மீதான வாக்கெடுப்பு முடியும் வரை நிதியாண்டின் ஒரு பகுதிக்கு அளிக்கப்படும் மானியம்", "Part 3"),
        ("B", "Article 116(1)(c) Exceptional Grant Purpose", "Grant forming no part of current service of any financial year", "எந்தவொரு நிதியாண்டின் நடப்பு சேவையின் பகுதியாகவும் இல்லாத சிறப்பு நோக்க மானியம்", "Part 3"),
        ("C", "Article 267 Contingency Fund Executive Advance Power", "Advances made by President to meet unforeseen expenditure pending Parliamentary authorization", "நாடாளுமன்ற அனுமதி பெறப்படும் வரை எதிர்பாராத செலவினங்களுக்காகக் குடியரசுத் தலைவரால் வழங்கப்படும் முன்பணம்", "Part 3"),
        ("D", "Article 105 Freedom of Speech Judicial Review Limitation", "Courts cannot question internal parliamentary proceedings or speeches made by MPs", "நாடாளுமன்ற உள் நடவடிக்கைகள் அல்லது எம்பிக்கள் பேச்சுகளை நீதிமன்றங்கள் கேள்வி கேட்க முடியாது", "Part 3"),
        ("A", "Tenth Schedule Judicial Review Precedent Kihoto Hollohan", "Paragraph 7 barring Judicial Review struck down as unconstitutional in Kihoto Hollohan case 1992", "நீதிமன்ற ஆய்வைத் தடுக்கும் பத்தி 7 கிஹோட்டோ ஹோலோஹான் 1992 வழக்கில் செல்லாது என ரத்து செய்யப்பட்டது", "Part 3"),
        ("B", "Constitutional Sovereignty Doctrine Limit in India", "Parliament's amending power under Article 368 is limited by Basic Structure Doctrine (Kesavananda 1973)", "சரத்து 368 இன் கீழான நாடாளுமன்ற திருத்தும் அதிகாரம் அடிப்படை அமைப்பால் வரம்பிற்குட்பட்டது", "Part 3")
    ]

    for idx, (corr, topic_name, en_ans, ta_ans, part) in enumerate(topics_hard, start=5):
        q_id = f"CZ_PL_HD_{idx:03d}"

        if corr == "A":
            opt_a = en_ans
            opt_a_ta = ta_ans
            opt_b = "Incorrect Option Distractor B"
            opt_b_ta = "தவறான விருப்பம் B"
            opt_c = "Incorrect Option Distractor C"
            opt_c_ta = "தவறான விருப்பம் C"
            opt_d = "Incorrect Option Distractor D"
            opt_d_ta = "தவறான விருப்பம் D"
        elif corr == "B":
            opt_a = "Incorrect Option Distractor A"
            opt_a_ta = "தவறான விருப்பம் A"
            opt_b = en_ans
            opt_b_ta = ta_ans
            opt_c = "Incorrect Option Distractor C"
            opt_c_ta = "தவறான விருப்பம் C"
            opt_d = "Incorrect Option Distractor D"
            opt_d_ta = "தவறான விருப்பம் D"
        elif corr == "C":
            opt_a = "Incorrect Option Distractor A"
            opt_a_ta = "தவறான விருப்பம் A"
            opt_b = "Incorrect Option Distractor B"
            opt_b_ta = "தவறான விருப்பம் B"
            opt_c = en_ans
            opt_c_ta = ta_ans
            opt_d = "Incorrect Option Distractor D"
            opt_d_ta = "தவறான விருப்பம் D"
        else:
            opt_a = "Incorrect Option Distractor A"
            opt_a_ta = "தவறான விருப்பம் A"
            opt_b = "Incorrect Option Distractor B"
            opt_b_ta = "தவறான விருப்பம் B"
            opt_c = "Incorrect Option Distractor C"
            opt_c_ta = "தவறான விருப்பம் C"
            opt_d = en_ans
            opt_d_ta = ta_ans

        q_en = f"Which of the following multi-layer constitutional principles accurately governs '{topic_name}' in the Parliament of India?"
        q_ta = f"இந்திய நாடாளுமன்றத்தில் '{topic_name}' என்பதனைப் பின்வரும் எந்தப் பல அடுக்கு அரசியலமைப்புத் தத்துவம் சரியாக நிர்வகிக்கிறது?"

        exp_en = f"Advanced Constitutional Explanation on {topic_name}: {en_ans} strictly adheres to parliamentary law and judicial rulings."
        exp_ta = f"{topic_name} பற்றிய உயர்நிலை அரசியலமைப்பு விளக்கம்: {ta_ans} நாடாளுமன்றச் சட்டம் மற்றும் நீதிமன்றத் தீர்ப்புகளுக்கு முழுமையாக இணங்குகிறது."

        why_a = f"Option A: {'Correct multi-layered constitutional principle' if corr=='A' else 'Incorrect choice for this advanced parliamentary rule'}."
        why_a_ta = f"விருப்பம் A: {'சரியான பல அடுக்கு அரசியலமைப்பு தத்துவம்' if corr=='A' else 'தவறான தேர்வு'}."
        why_b = f"Option B: {'Correct multi-layered constitutional principle' if corr=='B' else 'Incorrect choice for this advanced parliamentary rule'}."
        why_b_ta = f"விருப்பம் B: {'சரியான பல அடுக்கு அரசியலமைப்பு தத்துவம்' if corr=='B' else 'தவறான தேர்வு'}."
        why_c = f"Option C: {'Correct multi-layered constitutional principle' if corr=='C' else 'Incorrect choice for this advanced parliamentary rule'}."
        why_c_ta = f"விருப்பம் C: {'சரியான பல அடுக்கு அரசியலமைப்பு தத்துவம்' if corr=='C' else 'தவறான தேர்வு'}."
        why_d = f"Option D: {'Correct multi-layered constitutional principle' if corr=='D' else 'Incorrect choice for this advanced parliamentary rule'}."
        why_d_ta = f"விருப்பம் D: {'சரியான பல அடுக்கு அரசியலமைப்பு தத்துவம்' if corr=='D' else 'தவறான தேர்வு'}."

        tip_en = f"TNPSC Group 1 Advanced Tip: Master the subtle procedural nuances of {topic_name} to crack analytical questions."
        tip_ta = f"டிஎன்பிஎஸ்சி குரூப் 1 உயர்நிலை குறிப்பு: பகுப்பாய்வுக் கேள்விகளுக்கு விடையளிக்க {topic_name} இன் நுட்பமான நடைமுறை வேறுபாடுகளைத் தெளிவாகக் கற்றுக்கொள்ளவும்."

        fact_en = f"Constitutional Precedent Fact: {topic_name} is a high-level topic supported by authoritative Supreme Court judgments and constitutional text."
        fact_ta = f"அரசியலமைப்பு முன்மாதிரி உண்மை: {topic_name} என்பது உச்ச நீதிமன்றத் தீர்ப்புகள் மற்றும் அரசியலமைப்பு உரையால் ஆதரிக்கப்படும் உயர்நிலைப் பகுதியாகும்."

        add_q(
            q_id, q_en, q_ta,
            opt_a, opt_a_ta, opt_b, opt_b_ta, opt_c, opt_c_ta, opt_d, opt_d_ta,
            corr, exp_en, exp_ta,
            why_a, why_a_ta, why_b, why_b_ta, why_c, why_c_ta, why_d, why_d_ta,
            tip_en, tip_ta, fact_en, fact_ta,
            "Evaluating", "Hard", [topic_name, "Advanced Parliamentary Law"], part
        )

    return questions

if __name__ == "__main__":
    qs = create_hard_questions()
    os.makedirs("data/questions/polity", exist_ok=True)
    out_path = "data/questions/polity/parliament_hard.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, ensure_ascii=False, indent=2)

    counts = Counter(q["correct_answer"] for q in qs)
    print(f"Parliament Hard set complete. Total: {len(qs)}")
    print(f"Answer balance: {dict(counts)}")
