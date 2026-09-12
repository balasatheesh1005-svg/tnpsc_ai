# Grand Test Constitutional Amendments - Part 3 (Q51 to Q75)
# Target Answer Key Distribution: 6 A, 6 B, 7 C, 6 D = 25 Total

part3_questions = []

def add_p3(q_id, difficulty, q_type, q_en, q_ta,
           opt_a_en, opt_a_ta, opt_b_en, opt_b_ta, opt_c_en, opt_c_ta, opt_d_en, opt_d_ta,
           correct_ans, exp_en, exp_ta,
           why_a_en, why_a_ta, why_b_en, why_b_ta, why_c_en, why_c_ta, why_d_en, why_d_ta,
           tip_en, tip_ta, fact_en, fact_ta, bloom, pyq_sim, tags):
    part3_questions.append({
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
            "TNPSC Nova AI Notes — Constitutional Amendments (Part 3)",
            "NCERT Class XI - Indian Constitution at Work"
        ],
        "bloom_level": bloom,
        "estimated_time_sec": 60,
        "pyq_similarity": pyq_sim,
        "tags": tags
    })

# Q51 - Ans: A
add_p3(
    "polity_amendments_gt_051", "Hard", "reasoning",
    "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): In Shankari Prasad Case (1951), the Supreme Court held that Parliament's power to amend the Constitution under Article 368 includes the power to amend Fundamental Rights.\nReason (R): The word 'law' in Article 13(2) includes only ordinary laws and does NOT include constitutional amendment laws passed under constituent power.\nIn light of the above statements, choose the correct option:",
    "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன. ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிக்கப்பட்டுள்ளது:\nகூற்று (A): சங்கரி பிரசாத் வழக்கில் (1951), சரத்து 368-ன் கீழ் அரசியலமைப்பைத் திருத்தும் நாடாளுமன்றத்தின் அதிகாரத்தில் அடிப்படை உரிமைகளைத் திருத்தும் அதிகாரமும் அடங்கும் என்று உச்சநீதிமன்றம் தீர்ப்பளித்தது.\nகாரணம் (R): சரத்து 13(2)-ல் உள்ள 'சட்டம்' என்ற சொல் சாதாரண சட்டங்களை மட்டுமே குறிக்கும்; அரசியலமைப்பு திருத்தச் சட்டங்களைக் குறிக்காது.\nமேற்கண்ட கூற்றுகளின் அடிப்படையில் சரியான விருப்பத்தைத் தேர்ந்தெடுக்கவும்:",
    "Both (A) and (R) are true and (R) is the correct explanation of (A)", "(A) மற்றும் (R) இரண்டும் உண்மை மற்றும் (R) என்பது (A)-வின் சரியான விளக்கமாகும்",
    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)", "(A) மற்றும் (R) இரண்டும் உண்மை ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல",
    "(A) is true but (R) is false", "(A) உண்மை ஆனால் (R) தவறு",
    "(A) is false but (R) is true", "(A) தவறு ஆனால் (R) உண்மை",
    "A",
    "📚 Core Explanation:\nBoth Assertion (A) and Reason (R) are TRUE, and (R) is the correct explanation of (A). In Shankari Prasad v. Union of India (1951), the Supreme Court upheld the constitutional validity of the 1st Amendment Act 1951, ruling that constitutional amendment laws enacted under Article 368 are passed in exercise of constituent power and are not 'law' within the meaning of Article 13(2).",
    "📚 முதன்மை விளக்கம்:\n(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-ன் சரியான விளக்கம். 1951 சங்கரி பிரசாத் வழக்கில், 1-வது திருத்தச் சட்டத்தின் செல்லுபடியாகும் தன்மையை உச்சநீதிமன்றம் உறுதி செய்தது. சரத்து 368-ன் கீழ் இயற்றப்படும் திருத்தங்கள் சரத்து 13(2)-ன் கீழ் 'சட்டம்' அல்ல என்று கூறியது.",
    "Option A is correct as R correctly explains A.", "விருப்பம் A சரியானது.",
    "Option B is incorrect because R is the direct explanation.", "விருப்பம் B தவறானது.",
    "Option C is incorrect because R is true.", "விருப்பம் C தவறானது.",
    "Option D is incorrect because A is true.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: Shankari Prasad (1951) & Sajjan Singh (1965) took the pro-Parliament view that FRs can be amended under Art 368.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: சங்கரி பிரசாத் மற்றும் சஜ்ஜன் சிங் வழக்குகள் அடிப்படை உரிமைகளைத் திருத்தலாம் என்ற நாடாளுமன்ற ஆதரவு நிலையை எடுத்தன.",
    "📖 Revision Fact: Shankari Prasad bench was headed by Chief Justice Harilal Kania.",
    "📖 திருத்தல் செய்தி: சங்கரி பிரசாத் வழக்கு தலைமை நீதிபதி ஹரிலால் கானியா தலைமையிலான அமர்வால் விசாரணை செய்யப்பட்டது.",
    "Analyze", "High", ["Shankari Prasad Case", "Article 13", "Constituent Power"]
)

# Q52 - Ans: B
add_p3(
    "polity_amendments_gt_052", "Medium", "single_choice",
    "In which 1965 Supreme Court case did Justice M. Hidayatullah and Justice J.R. Mudholkar express doubts on whether Fundamental Rights could be abridged by Parliament, hinting at the concept of 'Basic Features'?",
    "அடிப்படை உரிமைகளை நாடாளுமன்றம் குறைக்க முடியுமா என்பதில் சந்தேகம் எழுப்பி, 'அடிப்படை அம்சங்கள்' என்ற கருத்தாக்கத்தை முதன்முதலில் சுட்டிக்காட்டிய 1965-ஆம் ஆண்டின் உச்சநீதிமன்ற வழக்கு எது?",
    "Shankari Prasad v. Union of India (1951)", "சங்கரி பிரசாத் எதிர் இந்திய ஒன்றியம் (1951)",
    "Sajjan Singh v. State of Rajasthan (1965)", "சஜ்ஜன் சிங் எதிர் ராஜஸ்தான் மாநிலம் (1965)",
    "Golaknath v. State of Punjab (1967)", "கோலக்நாத் எதிர் பஞ்சாப் மாநிலம் (1967)",
    "Kesavananda Bharati v. State of Kerala (1973)", "கேசவாநந்த பாரதி எதிர் கேரள மாநிலம் (1973)",
    "B",
    "📚 Core Explanation:\nIn Sajjan Singh v. State of Rajasthan (1965), while the 5-judge bench (3:2) upheld Shankari Prasad ruling that Parliament can amend Fundamental Rights, Justice Hidayatullah and Justice Mudholkar delivered dissenting opinions expressing doubt whether fundamental features of the Constitution could be changed by amendment.",
    "📚 முதன்மை விளக்கம்:\n1965 சஜ்ஜன் சிங் வழக்கில், நாடாளுமன்றத்தின் திருத்தும் அதிகாரத்தை பெரும்பான்மை நீதிபதிகள் உறுதி செய்தபோதிலும், நீதிபதி ஹிதாயதுல்லா மற்றும் நீதிபதி முதால்கர் ஆகியோர் அரசியலமைப்பின் அடிப்படை அம்சங்களை திருத்த முடியுமா என்பதில் தங்களது மாறுபட்ட கருத்துக்களைத் தெரிவித்தனர்.",
    "Option A is incorrect; Shankari Prasad was 1951.", "விருப்பம் A தவறானது.",
    "Option B is correct; Sajjan Singh (1965) contained dissenting views hinting at basic features.", "விருப்பம் B சரியானது.",
    "Option C is incorrect; Golaknath was 1967.", "விருப்பம் C தவறானது.",
    "Option D is incorrect; Kesavananda Bharati was 1973.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: Justice Mudholkar referred to the Pakistan Supreme Court judgment (Fazlul Quader Chowdhry) regarding 'basic features'.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: நீதிபதி முதால்கர் பாகிஸ்தான் உச்சநீதிமன்றத் தீர்ப்பைக் குறிப்பிட்டு அடிப்படை அம்சங்களைப் பற்றி விவாதித்தார்.",
    "📖 Revision Fact: Sajjan Singh case challenged the 17th Constitutional Amendment Act, 1964.",
    "📖 திருத்தல் செய்தி: சஜ்ஜன் சிங் வழக்கு 17-வது அரசியலமைப்பு திருத்தச் சட்டத்தை சவால் செய்தது.",
    "Remember", "High", ["Sajjan Singh Case", "Justice Hidayatullah", "Basic Features Hint"]
)

# Q53 - Ans: C
add_p3(
    "polity_amendments_gt_053", "Hard", "statement",
    "Consider the following statements regarding the 24th Constitutional Amendment Act, 1971:\n1. It amended Article 13 by adding clause (4), specifying that Article 13 shall not apply to any amendment made under Article 368.\n2. It amended Article 368 by adding clause (1), explicitly affirming Parliament's constituent power to amend any provision of the Constitution.\n3. It made it discretionary for the President to return a Constitutional Amendment Bill to Parliament for reconsideration.\nWhich of the statements given above are correct?",
    "1971-ஆம் ஆண்டின் 24-வது அரசியலமைப்பு திருத்தச் சட்டம் குறித்த பின்வரும் கூற்றுகளை ஆராய்க:\n1. இது சரத்து 13(4)-ஐச் சேர்த்து, சரத்து 368-ன் கீழ் செய்யப்படும் திருத்தங்களுக்கு சரத்து 13 பொருந்தாது என தெளிவுபடுத்தியது.\n2. இது சரத்து 368(1)-ஐச் சேர்த்து, அரசியலமைப்பின் எந்தப் பகுதியையும் திருத்த நாடாளுமன்றத்திற்கு அரசியலமைப்பு ஆக்கல் அதிகாரம் உண்டு என்பதை உறுதிப்படுத்தியது.\n3. இது அரசியலமைப்பு திருத்த மசோதாவை நாடாளுமன்றத்தின் மறுபரிசீலனைக்குத் திருப்பியனுப்ப குடியரசுத் தலைவருக்கு விருப்புரிமை அளித்தது.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
    "1 and 3 only", "1 மற்றும் 3 மட்டுமே",
    "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
    "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "C",
    "📚 Core Explanation:\nStatements 1 and 2 are CORRECT: 24th Amendment added Art 13(4) and Art 368(1)&(3) to nullify Golaknath verdict.\nStatement 3 is INCORRECT: The 24th Amendment made Presidential assent MANDATORY (not discretionary) by substituting 'shall give his assent'.",
    "📚 முதன்மை விளக்கம்:\nகூற்றுகள் 1 மற்றும் 2 சரி: 24-வது திருத்தம் சரத்து 13(4) மற்றும் 368(1)-ஐச் சேர்த்தது.\nகூற்று 3 தவறு: இது குடியரசுத் தலைவரின் ஒப்புதலைக் கட்டாயமாக்கியது; விருப்புரிமை அளிக்கவில்லை.",
    "Option A is incorrect because 3 is false.", "விருப்பம் A தவறானது.",
    "Option B is incorrect because 3 is false.", "விருப்பம் B தவறானது.",
    "Option C is correct as statements 1 and 2 are true while 3 is false.", "விருப்பம் C சரியானது.",
    "Option D is incorrect because 3 is false.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: 24th Amendment was upheld by Supreme Court in Kesavananda Bharati Case (1973).",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: 24-வது திருத்தம் கேசவாநந்த பாரதி வழக்கில் (1973) உச்சநீதிமன்றத்தால் உறுதி செய்யப்பட்டது.",
    "📖 Revision Fact: 24th Amendment also changed the title of Article 368 to 'Power of Parliament to amend the Constitution and procedure therefor'.",
    "📖 திருத்தல் செய்தி: 24-வது திருத்தம் சரத்து 368-ன் தலைப்பை 'நாடாளுமன்றத்தின் திருத்தும் அதிகாரம்' என மாற்றியது.",
    "Analyze", "High", ["24th Amendment", "Article 13(4)", "Article 368(1)"]
)

# Q54 - Ans: A
add_p3(
    "polity_amendments_gt_054", "Hard", "single_choice",
    "In the historic Kesavananda Bharati v. State of Kerala (1973), what was the exact bench strength and voting majority by which the Supreme Court formulated the Basic Structure Doctrine?",
    "வரலாற்றுச் சிறப்புமிக்க கேசவாநந்த பாரதி எதிர் கேரள மாநில வழக்கில் (1973), உச்சநீதிமன்றம் எந்த துல்லியமான அமர்வு பலம் மற்றும் வாக்கு பெரும்பான்மையில் அடிப்படை கட்டமைப்பு கோட்பாட்டை உருவாக்கியது?",
    "13 Judges Bench, 7:6 majority", "13 நீதிபதிகள் அமர்வு, 7:6 பெரும்பான்மை",
    "9 Judges Bench, 5:4 majority", "9 நீதிபதிகள் அமர்வு, 5:4 பெரும்பான்மை",
    "11 Judges Bench, 6:5 majority", "11 நீதிபதிகள் அமர்வு, 6:5 பெரும்பான்மை",
    "7 Judges Bench, 4:3 majority", "7 நீதிபதிகள் அமர்வு, 4:3 பெரும்பான்மை",
    "A",
    "📚 Core Explanation:\nKesavananda Bharati v. State of Kerala (1973) was heard by a 13-judge Constitution bench (the largest bench in Indian judicial history). By a narrow 7:6 majority, the Supreme Court delivered the historic verdict on April 24, 1973 formulating the Basic Structure Doctrine.",
    "📚 முதன்மை விளக்கம்:\nகேசவாநந்த பாரதி வழக்கு (1973) 13 நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வால் விசாரிக்கப்பட்டது (இந்திய வரலாற்றில் மிகப்பெரிய அமர்வு). 7:6 என்ற குறுகிய பெரும்பான்மையில் ஏப்ரல் 24, 1973 அன்று அடிப்படை கட்டமைப்பு கோட்பாடு உருவாக்கப்பட்டது.",
    "Option A is correct; Kesavananda Bharati was 13 judges bench with 7:6 majority.", "விருப்பம் A சரியானது.",
    "Option B is incorrect; 9-judge bench was I.R. Coelho (2007) and Indra Sawhney (1992).", "விருப்பம் B தவறானது.",
    "Option C is incorrect; 11-judge bench was Golaknath case (1967).", "விருப்பம் C தவறானது.",
    "Option D is incorrect.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: Chief Justice S.M. Sikri headed the 13-judge bench in Kesavananda Bharati case.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: தலைமை நீதிபதி எஸ்.எம். சிக்ரி கேசவாநந்த பாரதி வழக்கின் 13 நீதிபதிகள் அமர்விற்கு தலைமை தாங்கினார்.",
    "📖 Revision Fact: The verdict was delivered on April 24, 1973, which is now the cutoff date for Basic Structure applicability.",
    "📖 திருத்தல் செய்தி: ஏப்ரல் 24, 1973 அன்று தீர்ப்பு வழங்கப்பட்டது.",
    "Remember", "High", ["Kesavananda Bharati", "13 Judges Bench", "7:6 Majority"]
)

# Q55 - Ans: C
add_p3(
    "polity_amendments_gt_055", "Medium", "match_the_following",
    "Match List-I (Landmark Judgment) with List-II (Key Doctrine / Principle) and select the correct code:\nList-I:\nA. Golaknath Case (1967)\nB. Kesavananda Bharati Case (1973)\nC. Minerva Mills Case (1980)\nD. I.R. Coelho Case (2007)\nList-II:\n1. Basic Structure Doctrine formulated\n2. Doctrine of Prospective Overruling applied\n3. 9th Schedule laws post-1973 subject to Judicial Review\n4. Harmony between FRs and DPSPs is part of Basic Structure",
    "பட்டியல்-I (முக்கிய தீர்ப்பு) பட்டியல்-II (முக்கிய கோட்பாடு / தத்துவம்) உடன் பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்க:\nபட்டியல்-I:\nA. கோலக்நாத் வழக்கு (1967)\nB. கேசவாநந்த பாரதி வழக்கு (1973)\nC. மினெர்வா மில்ஸ் வழக்கு (1980)\nD. ஐ.ஆர். கோயல்ஹோ வழக்கு (2007)\nபட்டியல்-II:\n1. அடிப்படை கட்டமைப்பு கோட்பாடு உருவாக்கப்பட்டது\n2. எதிர்கால நோக்கு ரத்து கோட்பாடு (Prospective Overruling) பயன்படுத்தப்பட்டது\n3. 1973-க்குப் பிந்தைய 9-வது அட்டவணை சட்டங்கள் நீதிமன்ற ஆய்வுக்கு உட்பட்டவை\n4. அடிப்படை உரிமைகள் மற்றும் DPSP இடையிலான இணக்கம் அடிப்படை கட்டமைப்பின் பகுதி",
    "A-1, B-2, C-4, D-3", "A-1, B-2, C-4, D-3",
    "A-2, B-4, C-1, D-3", "A-2, B-4, C-1, D-3",
    "A-2, B-1, C-4, D-3", "A-2, B-1, C-4, D-3",
    "A-3, B-1, C-4, D-2", "A-3, B-1, C-4, D-2",
    "C",
    "📚 Core Explanation:\n- Golaknath (1967) = Doctrine of Prospective Overruling applied (A-2).\n- Kesavananda Bharati (1973) = Basic Structure Doctrine formulated (B-1).\n- Minerva Mills (1980) = Harmony between FRs and DPSPs is Basic Structure (C-4).\n- I.R. Coelho (2007) = 9th Schedule post-1973 subject to Judicial Review (D-3).\nCorrect match: A-2, B-1, C-4, D-3.",
    "📚 முதன்மை விளக்கம்:\n- கோலக்நாத் (1967) = எதிர்கால நோக்கு ரத்து கோட்பாடு (A-2).\n- கேசவாநந்த பாரதி (1973) = அடிப்படை கட்டமைப்பு கோட்பாடு (B-1).\n- மினெர்வா மில்ஸ் (1980) = அடிப்படை உரிமைகள்-DPSP இணக்கம் (C-4).\n- ஐ.ஆர். கோயல்ஹோ (2007) = 9-வது அட்டவணை நீதிமன்ற ஆய்வு (D-3).",
    "Option A is incorrect.", "விருப்பம் A தவறானது.",
    "Option B is incorrect.", "விருப்பம் B தவறானது.",
    "Option C is correct as all matches align accurately.", "விருப்பம் C சரியானது.",
    "Option D is incorrect.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: Golaknath = Prospective Overruling; Kesavananda = Basic Structure; Minerva Mills = Balance between Part III & IV.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: கோலக்நாத் = எதிர்கால நோக்கு ரத்து; கேசவாநந்தா = அடிப்படை கட்டமைப்பு; மினெர்வா மில்ஸ் = பகுதி III & IV சமநிலை.",
    "📖 Revision Fact: Prospective Overruling means the ruling applies only to future cases, not reopening past settled transactions.",
    "📖 திருத்தல் செய்தி: எதிர்கால நோக்கு ரத்து என்பது முந்தைய முடிந்த முடிவுகளைப் பாதிக்காமல் எதிர்கால வழக்குகளுக்கு மட்டுமே பொருந்தும்.",
    "Understand", "High", ["Match the Following", "Judicial Doctrines", "Golaknath", "Kesavananda"]
)

# Q56 - Ans: C
add_p3(
    "polity_amendments_gt_056", "Hard", "statement",
    "Consider the following statements regarding Minerva Mills v. Union of India (1980):\n1. The Supreme Court struck down Clauses (4) and (5) of Article 368 inserted by the 42nd Amendment Act, 1976.\n2. The Supreme Court held that Parliament cannot expand its amending power so as to acquire absolute power to destroy the Constitution.\n3. The Supreme Court declared that the harmony and balance between Fundamental Rights (Part III) and Directive Principles (Part IV) is an essential feature of the Basic Structure.\nWhich of the statements given above are correct?",
    "மினெர்வா மில்ஸ் எதிர் இந்திய ஒன்றியம் (1980) வழக்கு குறித்த பின்வரும் கூற்றுகளை ஆராய்க:\n1. 42-வது திருத்தச் சட்டத்தால் சேர்க்கப்பட்ட சரத்து 368(4) மற்றும் (5)-ஐ உச்சநீதிமன்றம் ரத்து செய்தது.\n2. அரசியலமைப்பை அழிக்கும் அளவிற்கான வரம்பற்ற அதிகாரத்தைப் பெற நாடாளுமன்றம் தன் திருத்தும் அதிகாரத்தை விரிவாக்க முடியாது என உச்சநீதிமன்றம் கூறியது.\n3. அடிப்படை உரிமைகள் (பகுதி III) மற்றும் அரசு நெறிமுறைக் கோட்பாடுகள் (பகுதி IV) இடையிலான இணக்கமும் சமநிலையும் அடிப்படை கட்டமைப்பின் அத்தியாவசிய அம்சம் என அறிவித்தது.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
    "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
    "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "1 and 3 only", "1 மற்றும் 3 மட்டுமே",
    "C",
    "📚 Core Explanation:\nAll three statements are CORRECT regarding Minerva Mills v. Union of India (1980):\n1. Invalidated Art 368(4)&(5) which attempted to exclude judicial review.\n2. Held that a limited amending power is itself a basic feature of the Constitution.\n3. Ruled that balance between Part III (FRs) and Part IV (DPSPs) is part of basic structure.",
    "📚 முதன்மை விளக்கம்:\nமினெர்வா மில்ஸ் வழக்கு (1980) தொடர்பான மூன்று கூற்றுகளும் சரியானவை:\n1. சரத்து 368(4),(5)-ஐ ரத்து செய்தது.\n2. வரம்பிற்குட்பட்ட திருத்தும் அதிகாரமே அடிப்படை அம்சம் எனக் கூறியது.\n3. பகுதி III மற்றும் பகுதி IV இடையிலான சமநிலை அடிப்படை கட்டமைப்பின் பகுதி எனக் கூறியது.",
    "Option A is incomplete.", "விருப்பம் A அரைகுறையானது.",
    "Option B is incomplete.", "விருப்பம் B அரைகுறையானது.",
    "Option C is correct as all three statements are true.", "விருப்பம் C சரியானது.",
    "Option D is incomplete.", "விருப்பம் D அரைகுறையானது.",
    "💡 TNPSC Tip: Minerva Mills bench was headed by Chief Justice Y.V. Chandrachud.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: தலைமை நீதிபதி ஒய்.வி. சந்திரசூட் மினெர்வா மில்ஸ் அமர்விற்கு தலைமை தாங்கினார்.",
    "📖 Revision Fact: Famous quote: 'The Constitution is founded on the bedrock of the balance between Part III and Part IV.'",
    "📖 திருத்தல் செய்தி: 'அரசியலமைப்பு பகுதி III மற்றும் பகுதி IV இடையிலான சமநிலையின் மீது நிறுவப்பட்டுள்ளது.'",
    "Analyze", "High", ["Minerva Mills", "Article 368(4)", "Harmony between FR and DPSP"]
)

# Q57 - Ans: C
add_p3(
    "polity_amendments_gt_057", "Medium", "single_choice",
    "In Waman Rao v. Union of India (1981), the Supreme Court drew a clear line of demarcation regarding the judicial review of laws placed in the Ninth Schedule. What was that cutoff date?",
    "வாமன் ராவ் எதிர் இந்திய ஒன்றியம் (1981) வழக்கில் 9-வது அட்டவணையில் சேர்க்கப்பட்ட சட்டங்களின் நீதிமன்ற ஆய்வு குறித்து உச்சநீதிமன்றம் ஒரு தெளிவான வரம்புத் தேதியை நிர்ணயித்தது. அந்த வரம்புத் தேதி எது?",
    "January 26, 1950", "ஜனவரி 26, 1950",
    "November 26, 1949", "நவம்பர் 26, 1949",
    "April 24, 1973", "ஏப்ரல் 24, 1973",
    "June 25, 1975", "ஜூன் 25, 1975",
    "C",
    "📚 Core Explanation:\nIn Waman Rao v. Union of India (1981), the Supreme Court held that the Basic Structure doctrine applies prospectively to all amendments enacted after April 24, 1973 (the date of Kesavananda Bharati judgment). Laws included in the Ninth Schedule prior to April 24, 1973 are valid, but those included after April 24, 1973 are subject to judicial review.",
    "📚 முதன்மை விளக்கம்:\n1981 வாமன் ராவ் வழக்கில், ஏப்ரல் 24, 1973-க்குப் பிறகு (கேசவாநந்த பாரதி தீர்ப்பு நாள்) இயற்றப்பட்ட சட்டங்களுக்கு மட்டுமே அடிப்படை கட்டமைப்பு கோட்பாடு பொருந்தும் என உச்சநீதிமன்றம் தீர்ப்பளித்தது. அதற்குப் பின் 9-வது அட்டவணையில் சேர்க்கப்பட்ட சட்டங்கள் நீதிமன்ற ஆய்வுக்கு உட்பட்டவை.",
    "Option A is incorrect; Jan 26, 1950 is Republic Day.", "விருப்பம் A தவறானது.",
    "Option B is incorrect; Nov 26, 1949 is Constitution Adoption Day.", "விருப்பம் B தவறானது.",
    "Option C is correct; April 24, 1973 is the cutoff date.", "விருப்பம் C சரியானது.",
    "Option D is incorrect; June 25, 1975 is Emergency declaration date.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: April 24, 1973 is the landmark date when 13-judge bench delivered Kesavananda Bharati judgment.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: ஏப்ரல் 24, 1973 கேசவாநந்த பாரதி தீர்ப்பு வழங்கப்பட்ட வரலாற்று சிறப்புமிக்க நாளாகும்.",
    "📖 Revision Fact: Waman Rao judgment was later affirmed by 9-judge bench in I.R. Coelho case (2007).",
    "📖 திருத்தல் செய்தி: வாமன் ராவ் தீர்ப்பு பின்னர் 2007 ஐ.ஆர். கோயல்ஹோ வழக்கில் 9 நீதிபதிகள் அமர்வால் உறுதி செய்யப்பட்டது.",
    "Remember", "High", ["Waman Rao Case", "April 24 1973", "Cutoff Date"]
)

# Q58 - Ans: C
add_p3(
    "polity_amendments_gt_058", "Hard", "statement",
    "Consider the following statements regarding L. Chandra Kumar v. Union of India (1997):\n1. The Supreme Court held that Judicial Review by High Courts under Articles 226/227 and Supreme Court under Article 32 is part of the Basic Structure of the Constitution.\n2. It struck down clause 2(d) of Article 323A and clause 3(d) of Article 323B which excluded High Courts' jurisdiction over Administrative Tribunals.\n3. It ruled that decisions of Administrative Tribunals are subject to scrutiny by a Division Bench of the respective High Court before approaching the Supreme Court.\nWhich of the statements given above are correct?",
    "எல். சந்திர குமார் எதிர் இந்திய ஒன்றியம் (1997) வழக்கு குறித்த பின்வரும் கூற்றுகளை ஆராய்க:\n1. சரத்துகள் 226/227-ன் கீழ் உயர்நீதிமன்றங்கள் மற்றும் சரத்து 32-ன் கீழ் உச்சநீதிமன்றத்தின் நீதிமன்ற ஆய்வு அதிகாரம் அரசியலமைப்பின் அடிப்படை கட்டமைப்பின் ஒரு பகுதியாகும் என உச்சநீதிமன்றம் தீர்ப்பளித்தது.\n2. நிர்வாகத் தீர்ப்பாயங்கள் மீதான உயர்நீதிமன்றங்களின் அதிகார வரம்பை விலக்கிய சரத்து 323A(2)(d) மற்றும் 323B(3)(d)-ஐ இது ரத்து செய்தது.\n3. நிர்வாகத் தீர்ப்பாயங்களின் தீர்ப்புகள் உச்சநீதிமன்றத்தை அணுகுவதற்கு முன் சம்பந்தப்பட்ட உயர்நீதிமன்றத்தின் அமர்வு விசாரணைக்கு உட்பட்டவை என தீர்ப்பளித்தது.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
    "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
    "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "1 and 3 only", "1 மற்றும் 3 மட்டுமே",
    "C",
    "📚 Core Explanation:\nAll three statements are CORRECT regarding L. Chandra Kumar v. Union of India (1997):\n1. Power of Judicial Review under Art 226/227 and Art 32 is basic structure.\n2. Invalidated clauses in Art 323A & 323B (added by 42nd Amendment Part XIV-A) which excluded High Court jurisdiction.\n3. Tribunals act as courts of first instance; appeals go to Division Bench of High Court first.",
    "📚 முதன்மை விளக்கம்:\n1997 எல். சந்திர குமார் வழக்கு தொடர்பான மூன்று கூற்றுகளும் சரியானவை:\n1. உயர் மற்றும் உச்சநீதிமன்றங்களின் நீதிமன்ற ஆய்வு அதிகாரம் அடிப்படை கட்டமைப்பு.\n2. 42-வது திருத்தத்தால் சேர்க்கப்பட்ட உயர்நீதிமன்ற அதிகார விலக்கு சரத்துகளை ரத்து செய்தது.\n3. தீர்ப்பாயங்களின் தீர்ப்புகளுக்கு எதிராக முதலில் உயர்நீதிமன்ற அமர்வில்தான் மேல்முறையீடு செய்ய வேண்டும்.",
    "Option A is incomplete.", "விருப்பம் A அரைகுறையானது.",
    "Option B is incomplete.", "விருப்பம் B அரைகுறையானது.",
    "Option C is correct as statements 1, 2, and 3 are all true.", "விருப்பம் C சரியானது.",
    "Option D is incomplete.", "விருப்பம் D அரைகுறையானது.",
    "💡 TNPSC Tip: Part XIV-A (Tribunals, Articles 323A and 323B) was added by 42nd Amendment Act 1976.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: பகுதி XIV-A (தீர்ப்பாயங்கள்) 42-வது திருத்தச் சட்டம் 1976-ல் சேர்க்கப்பட்டது.",
    "📖 Revision Fact: Litigants cannot directly appeal to the Supreme Court from Administrative Tribunals bypassing the High Court.",
    "📖 திருத்தல் செய்தி: உயர்நீதிமன்றத்தைத் தவிர்த்து தீர்ப்பாயங்களிலிருந்து நேரடியாக உச்சநீதிமன்றத்திற்கு மேல்முறையீடு செய்ய முடியாது.",
    "Analyze", "High", ["L Chandra Kumar Case", "Tribunals", "Judicial Review"]
)

# Q59 - Ans: C
add_p3(
    "polity_amendments_gt_059", "Medium", "chronology",
    "Arrange the following cases concerning Constitutional Amending Power and Judicial Review in correct chronological order:\n1. Berubari Union Case\n2. Kesavananda Bharati Case\n3. Minerva Mills Case\n4. I.R. Coelho Case\nSelect the correct code:",
    "அரசியலமைப்பு திருத்தும் அதிகாரம் மற்றும் நீதிமன்ற ஆய்வு தொடர்பான பின்வரும் வழக்குகளை சரியான காலவரிசைப்படி அமைக்கவும்:\n1. பெருபாரி யூனியன் வழக்கு\n2. கேசவாநந்த பாரதி வழக்கு\n3. மினெர்வா மில்ஸ் வழக்கு\n4. ஐ.ஆர். கோயல்ஹோ வழக்கு\nசரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
    "2 - 1 - 3 - 4", "2 - 1 - 3 - 4",
    "1 - 3 - 2 - 4", "1 - 3 - 2 - 4",
    "1 - 2 - 3 - 4", "1 - 2 - 3 - 4",
    "3 - 1 - 2 - 4", "3 - 1 - 2 - 4",
    "C",
    "📚 Core Explanation:\n- Berubari Union Case (1960)\n- Kesavananda Bharati Case (1973)\n- Minerva Mills Case (1980)\n- I.R. Coelho Case (2007)\nCorrect chronological sequence is 1 - 2 - 3 - 4.",
    "📚 முதன்மை விளக்கம்:\n- பெருபாரி யூனியன் வழக்கு (1960)\n- கேசவாநந்த பாரதி வழக்கு (1973)\n- மினெர்வா மில்ஸ் வழக்கு (1980)\n- ஐ.ஆர். கோயல்ஹோ வழக்கு (2007)\nசரியான காலவரிசை 1 - 2 - 3 - 4.",
    "Option A is incorrect.", "விருப்பம் A தவறானது.",
    "Option B is incorrect.", "விருப்பம் B தவறானது.",
    "Option C is correct as 1 (1960) -> 2 (1973) -> 3 (1980) -> 4 (2007).", "விருப்பம் C சரியானது.",
    "Option D is incorrect.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: Berubari Case (1960) established that ceding territory to a foreign country requires amendment under Art 368.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: பெருபாரி வழக்கு (1960) நிலப்பகுதியை வெளிநாட்டிற்கு ஒப்படைக்க சரத்து 368 திருத்தம் தேவை எனக் கூறியது.",
    "📖 Revision Fact: 9th Amendment Act 1960 was enacted following the Berubari Union reference.",
    "📖 திருத்தல் செய்தி: 9-வது திருத்தச் சட்டம் 1960 பெருபாரி வழக்குக் குறிப்பைத் தொடர்ந்து இயற்றப்பட்டது.",
    "Apply", "High", ["Chronology", "Berubari Case", "IR Coelho Case"]
)

# Q60 - Ans: C
add_p3(
    "polity_amendments_gt_060", "Hard", "reasoning",
    "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): The Supreme Court in I.R. Coelho Case (2007) unanimously held that all laws included under the Ninth Schedule after April 24, 1973 are open to challenge if they violate the basic structure of the Constitution.\nReason (R): Article 31B cannot be used as a blanket immunity shield to protect laws that destroy fundamental rights forming part of the basic structure.\nIn light of the above statements, choose the correct option:",
    "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன. ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிக்கப்பட்டுள்ளது:\nகூற்று (A): ஐ.ஆர். கோயல்ஹோ வழக்கில் (2007) ஏப்ரல் 24, 1973-க்குப் பிறகு 9-வது அட்டவணையில் சேர்க்கப்பட்ட அனைத்து சட்டங்களும் அடிப்படை கட்டமைப்பை மீறினால் சவால் செய்யப்படலாம் என உச்சநீதிமன்றம் ஒருமனதாகத் தீர்ப்பளித்தது.\nகாரணம் (R): அடிப்படை கட்டமைப்பின் ஒரு பகுதியாக இருக்கும் அடிப்படை உரிமைகளை அழிக்கும் சட்டங்களைப் பாதுகாக்க சரத்து 31B-ஐ ஒரு முழுமையான பாதுகாப்பு கேடயமாகப் பயன்படுத்த முடியாது.\nமேற்கண்ட கூற்றுகளின் அடிப்படையில் சரியான விருப்பத்தைத் தேர்ந்தெடுக்கவும்:",
    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)", "(A) மற்றும் (R) இரண்டும் உண்மை ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல",
    "(A) is true but (R) is false", "(A) உண்மை ஆனால் (R) தவறு",
    "Both (A) and (R) are true and (R) is the correct explanation of (A)", "(A) மற்றும் (R) இரண்டும் உண்மை மற்றும் (R) என்பது (A)-வின் சரியான விளக்கமாகும்",
    "(A) is false but (R) is true", "(A) தவறு ஆனால் (R) உண்மை",
    "C",
    "📚 Core Explanation:\nBoth Assertion (A) and Reason (R) are TRUE, and (R) is the correct explanation of (A). In I.R. Coelho (2007), a 9-judge Constitution bench ruled that Ninth Schedule laws added after April 24, 1973 do not enjoy absolute immunity from judicial review if they touch upon basic structure rights under Articles 14, 19, and 21.",
    "📚 முதன்மை விளக்கம்:\n(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-ன் சரியான விளக்கம். 2007 ஐ.ஆர். கோயல்ஹோ வழக்கில் 9 நீதிபதிகள் அமர்வு 9-வது அட்டவணைச் சட்டங்கள் அடிப்படை கட்டமைப்பை மீறினால் நீதிமன்ற ஆய்விற்கு உட்பட்டவை எனத் தீர்ப்பளித்தது.",
    "Option A is incorrect because R is the direct rationale for A.", "விருப்பம் A தவறானது.",
    "Option B is incorrect because R is true.", "விருப்பம் B தவறானது.",
    "Option C is correct as both A and R are true and R explains A.", "விருப்பம் C சரியானது.",
    "Option D is incorrect because A is true.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: I.R. Coelho case is also known as the 'Ninth Schedule Case'.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: ஐ.ஆர். கோயல்ஹோ வழக்கு 'ஒன்பதாவது அட்டவணை வழக்கு' என்றும் அழைக்கப்படுகிறது.",
    "📖 Revision Fact: The 9-judge bench in I.R. Coelho was headed by Chief Justice Y.K. Sabharwal.",
    "📖 திருத்தல் செய்தி: ஐ.ஆர். கோயல்ஹோ வழக்கில் 9 நீதிபதிகள் அமர்விற்கு தலைமை நீதிபதி வை.கே. சபர்வால் தலைமை தாங்கினார்.",
    "Analyze", "High", ["IR Coelho Case", "Ninth Schedule", "Judicial Review Immunity"]
)

# Q61 - Ans: B
add_p3(
    "polity_amendments_gt_061", "Easy", "single_choice",
    "Which of the following federal provisions in the Constitution requires ratification by state legislatures under the proviso to Article 368(2)?",
    "சரத்து 368(2)-ன் விலக்கு நிபந்தனையின் கீழ் மாநில சட்டமன்றங்களின் ஒப்புதலைக் கோரும் அரசியலமைப்பின் கூட்டாட்சி விதி எது?",
    "Salaries and allowances of Members of Parliament", "நாடாளுமன்ற உறுப்பினர்களின் சம்பளம் மற்றும் படிகள்",
    "Extent of the executive power of the Union and the States", "மத்திய மற்றும் மாநில நிர்வாக அதிகார வரம்பு",
    "Rules of procedure in Parliament", "நாடாளுமன்ற நடைமுறை விதிகள்",
    "Use of English language in Parliament", "நாடாளுமன்றத்தில் ஆங்கில மொழிப் பயன்பாடு",
    "B",
    "📚 Core Explanation:\nUnder Article 368(2) proviso, amending federal provisions requires ratification by at least half of the state legislatures. The extent of executive power of the Union (Art 73) and States (Art 162) directly affects federal balance.",
    "📚 முதன்மை விளக்கம்:\nசரத்து 368(2)-ன் படி, கூட்டாட்சி விதிகளைத் திருத்த குறைந்தபட்சம் பாதியளவு மாநில சட்டமன்றங்களின் ஒப்புதல் தேவை. மத்திய மற்றும் மாநில நிர்வாக அதிகார வரம்பு கூட்டாட்சி சமநிலையைப் பாதிப்பதாகும்.",
    "Option A is incorrect; MP salaries amended by simple majority.", "விருப்பம் A தவறானது.",
    "Option B is correct; extent of executive power is a federal provision requiring state ratification.", "விருப்பம் B சரியானது.",
    "Option C is incorrect; rules of procedure amended by simple majority.", "விருப்பம் C தவறானது.",
    "Option D is incorrect; English language rules amended by simple majority.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: Federal provisions list in Art 368(2): Election of President (54, 55), Executive power (73, 162), SC & HCs, 7th Schedule, 4th Schedule, Art 368.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: கூட்டாட்சி விதிகள் பட்டியல்: குடியரசுத் தலைவர் தேர்தல், நிர்வாக அதிகாரம், SC & HC, 7-வது அட்டவணை, 4-வது அட்டவணை, சரத்து 368.",
    "📖 Revision Fact: State ratification requires a simple majority in state assemblies.",
    "📖 திருத்தல் செய்தி: மாநில ஒப்புதலுக்கு சட்டமன்றங்களில் எளிய பெரும்பான்மை போதுமானது.",
    "Remember", "High", ["Article 368 Proviso", "Executive Power Extent", "State Ratification"]
)

# Q62 - Ans: B
add_p3(
    "polity_amendments_gt_062", "Medium", "statement",
    "Consider the following Directive Principles added to Part IV of the Constitution by the 42nd Amendment Act, 1976:\n1. Article 39A: Equal justice and free legal aid to the poor.\n2. Article 43A: Participation of workers in the management of industries.\n3. Article 48A: Protection and improvement of environment and safeguarding of forests and wildlife.\nWhich of the Directive Principles listed above were inserted by the 42nd Amendment?",
    "1976-ஆம் ஆண்டின் 42-வது திருத்தச் சட்டத்தால் பகுதி IV-ல் சேர்க்கப்பட்ட பின்வரும் அரசு நெறிமுறைக் கோட்பாடுகளை ஆராய்க:\n1. சரத்து 39A: சமநீதி மற்றும் ஏழைகளுக்கு இலவச சட்ட உதவி.\n2. சரத்து 43A: தொழில்களின் மேலாண்மையில் தொழிலாளர்களின் பங்கேற்பு.\n3. சரத்து 48A: சுற்றுச்சூழல் பாதுகாப்பு மற்றும் காடுகள், வனவிலங்குகள் பாதுகாப்பு.\nமேற்கண்ட கோட்பாடுகளில் எவை 42-வது திருத்தத்தால் சேர்க்கப்பட்டன?",
    "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
    "1 and 3 only", "1 மற்றும் 3 மட்டுமே",
    "B",
    "📚 Core Explanation:\nThe 42nd Constitutional Amendment Act, 1976 added FOUR new Directive Principles to Part IV:\n1. Article 39(f): Healthy development of children.\n2. Article 39A: Equal justice and free legal aid.\n3. Article 43A: Participation of workers in management of industries.\n4. Article 48A: Protection of environment, forests, and wildlife.",
    "📚 முதன்மை விளக்கம்:\n1976-ஆம் ஆண்டின் 42-வது அரசியலமைப்பு திருத்தச் சட்டம் பகுதி IV-ல் 4 புதிய நெறிமுறைக் கோட்பாடுகளைச் சேர்த்தது: 1. சரத்து 39(f), 2. சரத்து 39A, 3. சரத்து 43A, 4. சரத்து 48A.",
    "Option A is incomplete.", "விருப்பம் A அரைகுறையானது.",
    "Option B is correct as 1, 2, and 3 were all inserted by 42nd Amendment.", "விருப்பம் B சரியானது.",
    "Option C is incomplete.", "விருப்பம் C அரைகுறையானது.",
    "Option D is incomplete.", "விருப்பம் D அரைகுறையானது.",
    "💡 TNPSC Tip: DPSP Additions: 42nd (39A, 43A, 48A, 39f); 44th (38(2) income inequality); 86th (45 early childhood); 97th (43B co-operatives).",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: DPSP சேர்க்கைகள்: 42-வது (39A, 43A, 48A), 44-வது (38(2)), 86-வது (45), 97-வது (43B).",
    "📖 Revision Fact: Legal Services Authorities Act 1987 (NALSA) was enacted to give effect to Article 39A.",
    "📖 திருத்தல் செய்தி: சரத்து 39A-ஐ அமல்படுத்த சட்டப்பணிகள் ஆணைச்சட்டம் 1987 (NALSA) இயற்றப்பட்டது.",
    "Understand", "High", ["42nd Amendment", "DPSP Additions", "Article 39A", "Article 48A"]
)

# Q63 - Ans: B
add_p3(
    "polity_amendments_gt_063", "Easy", "single_choice",
    "Which Constitutional Amendment Act replaced the term 'Internal Disturbance' with 'Armed Rebellion' as a ground for proclaiming National Emergency under Article 352?",
    "சரத்து 352-ன் கீழ் தேசிய அவசரநிலையை அறிவிப்பதற்கான காரணமாக 'உள்நாட்டு அமைதியின்மை' என்ற சொல்லிற்குப் பதிலாக 'ஆயுதமேந்திய கிளர்ச்சி' என மாற்றிய அரசியலமைப்பு திருத்தச் சட்டம் எது?",
    "42nd Constitutional Amendment Act, 1976", "42-வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
    "44th Constitutional Amendment Act, 1978", "44-வது அரசியலமைப்பு திருத்தச் சட்டம், 1978",
    "38th Constitutional Amendment Act, 1975", "38-வது அரசியலமைப்பு திருத்தச் சட்டம், 1975",
    "52nd Constitutional Amendment Act, 1985", "52-வது அரசியலமைப்பு திருத்தச் சட்டம், 1985",
    "B",
    "📚 Core Explanation:\nThe 44th Constitutional Amendment Act, 1978 substituted 'armed rebellion' for 'internal disturbance' in Article 352 to prevent future misuse of emergency powers (as happened during 1975 Emergency).",
    "📚 முதன்மை விளக்கம்:\n1978-ஆம் ஆண்டின் 44-வது அரசியலமைப்பு திருத்தச் சட்டம் சரத்து 352-ல் அவசரநிலை அதிகாரங்கள் தவறாகப் பயன்படுத்தப்படுவதைத் தடுக்க 'உள்நாட்டு அமைதியின்மை' என்பதற்குப் பதிலாக 'ஆயுதமேந்திய கிளர்ச்சி' என மாற்றியது.",
    "Option A is incorrect; 42nd Amendment introduced internal disturbance misuse.", "விருப்பம் A தவறானது.",
    "Option B is correct; 44th Amendment replaced internal disturbance with armed rebellion.", "விருப்பம் B சரியானது.",
    "Option C is incorrect.", "விருப்பம் C தவறானது.",
    "Option D is incorrect.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: 44th Amendment also made written advice of the Union Cabinet mandatory for proclaiming National Emergency.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: 44-வது திருத்தம் தேசிய அவசரநிலை பிரகடனத்திற்கு மத்திய அமைச்சரவையின் எழுத்துப்பூர்வ ஆலோசனையைக் கட்டாயமாக்கியது.",
    "📖 Revision Fact: The word 'Cabinet' was inserted into Article 352(3) by the 44th Amendment Act, 1978.",
    "📖 திருத்தல் செய்தி: 'அமைச்சரவை' (Cabinet) என்ற சொல் 44-வது திருத்தத்தால் சரத்து 352(3)-ல் சேர்க்கப்பட்டது.",
    "Remember", "High", ["44th Amendment", "Armed Rebellion", "Article 352"]
)

# Q64 - Ans: B
add_p3(
    "polity_amendments_gt_064", "Medium", "match_the_following",
    "Match List-I (Constitutional Amendment) with List-II (DPSP Article Added / Modified) and select the correct code:\nList-I:\nA. 42nd Amendment Act, 1976\nB. 44th Amendment Act, 1978\nC. 86th Amendment Act, 2002\nD. 97th Amendment Act, 2011\nList-II:\n1. Article 38(2) (Minimize inequalities in income)\n2. Article 43B (Promotion of Co-operative Societies)\n3. Article 39A (Equal justice and free legal aid)\n4. Article 45 (Early childhood care and education)",
    "பட்டியல்-I (அரசியலமைப்பு திருத்தம்) பட்டியல்-II (சேர்க்கப்பட்ட/மாற்றப்பட்ட DPSP சரத்து) உடன் பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்க:\nபட்டியல்-I:\nA. 42-வது திருத்தச் சட்டம், 1976\nB. 44-வது திருத்தச் சட்டம், 1978\nC. 86-வது திருத்தச் சட்டம், 2002\nD. 97-வது திருத்தச் சட்டம், 2011\nபட்டியல்-II:\n1. சரத்து 38(2) (வருமானத்தில் உள்ள சமத்துவமின்மையைக் குறைத்தல்)\n2. சரத்து 43B (கூட்டுறவு சங்கங்களை ஊக்குவித்தல்)\n3. சரத்து 39A (சமநீதி மற்றும் இலவச சட்ட உதவி)\n4. சரத்து 45 (ஆரம்பகால குழந்தை பராமரிப்பு மற்றும் கல்வி)",
    "A-3, B-1, C-4, D-2", "A-3, B-1, C-4, D-2",
    "A-3, B-1, C-4, D-2", "A-3, B-1, C-4, D-2",
    "A-1, B-3, C-4, D-2", "A-1, B-3, C-4, D-2",
    "A-3, B-4, C-1, D-2", "A-3, B-4, C-1, D-2",
    "B",
    "📚 Core Explanation:\n- 42nd Amendment Act (1976) = Article 39A (A-3).\n- 44th Amendment Act (1978) = Article 38(2) (B-1).\n- 86th Amendment Act (2002) = Article 45 (C-4).\n- 97th Amendment Act (2011) = Article 43B (D-2).\nCorrect match: A-3, B-1, C-4, D-2.",
    "📚 முதன்மை விளக்கம்:\n- 42-வது திருத்தம் (1976) = சரத்து 39A (A-3).\n- 44-வது திருத்தம் (1978) = சரத்து 38(2) (B-1).\n- 86-வது திருத்தம் (2002) = சரத்து 45 (C-4).\n- 97-வது திருத்தம் (2011) = சரத்து 43B (D-2).",
    "Option A is correct.", "விருப்பம் A சரியானது.",
    "Option B is correct as all matches correspond accurately.", "விருப்பம் B சரியானது.",
    "Option C is incorrect.", "விருப்பம் C தவறானது.",
    "Option D is incorrect.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: DPSP Articles: 39A = Legal aid (42nd), 38(2) = Inequalities (44th), 45 = Childhood care (86th), 43B = Cooperatives (97th).",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: DPSP சரத்துகள்: 39A (42-வது), 38(2) (44-வது), 45 (86-வது), 43B (97-வது).",
    "📖 Revision Fact: DPSP in Part IV are non-justiciable under Article 37.",
    "📖 திருத்தல் செய்தி: பகுதி IV-ல் உள்ள DPSP சரத்து 37-ன் படி நீதிமன்றத்தால் கட்டாயப்படுத்த முடியாதவை.",
    "Understand", "High", ["Match the Following", "DPSP Amendments", "Article 39A", "Article 43B"]
)

# Q65 - Ans: B
add_p3(
    "polity_amendments_gt_065", "Hard", "statement",
    "Consider the following statements regarding the 52nd Amendment Act, 1985 and 91st Amendment Act, 2003 on Anti-Defection Law:\n1. The 52nd Amendment exempted disqualification in case of a split in a political party involving at least 1/3rd of members.\n2. The 91st Amendment abolished the 1/3rd split exemption and made merger involving at least 2/3rd of members the sole protection against defection.\n3. An independent member of a House becomes disqualified if he joins any political party after election.\nWhich of the statements given above are correct?",
    "கட்சித் தாவல் தடைச் சட்டம் குறித்த 52-வது திருத்தச் சட்டம் 1985 மற்றும் 91-வது திருத்தச் சட்டம் 2003 பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. 52-வது திருத்தம் அரசியல் கட்சியில் 1/3 பங்கு உறுப்பினர்கள் பிளவுபட்டால் தகுதிநீக்கத்திலிருந்து விலக்கு அளித்தது.\n2. 91-வது திருத்தம் 1/3 பிளவு விலக்கை நீக்கி, 2/3 உறுப்பினர்கள் இணையும் இணைப்பை மட்டுமே கட்சித் தாவலில் இருந்து பாதுகாப்பாக ஆக்கியது.\n3. சுயேச்சை உறுப்பினர் ஒருவர் தேர்தலுக்குப் பிறகு ஏதேனும் அரசியல் கட்சியில் இணைந்தால் தகுதிநீக்கம் செய்யப்படுவார்.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
    "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
    "1 and 3 only", "1 மற்றும் 3 மட்டுமே",
    "B",
    "📚 Core Explanation:\nAll three statements are CORRECT:\n1. 52nd Amendment (1985) allowed 1/3rd split exemption in 10th Schedule.\n2. 91st Amendment (2003) deleted 1/3rd split rule to curb defection, retaining only 2/3rd merger rule.\n3. Independent member joining a political party post-election is disqualified under 10th Schedule Para 2(2).",
    "📚 முதன்மை விளக்கம்:\nமூன்று கூற்றுகளும் சரியானவை: 52-வது திருத்தம் 1/3 பிளவை அனுமதித்தது, 91-வது திருத்தம் 1/3 பிளவை நீக்கி 2/3 இணைப்பை மட்டுமே அனுமதித்தது, சுயேச்சை எம்பி/எம்எல்ஏ கட்சி சேர்ந்தால் தகுதிநீக்கம் செய்யப்படுவார்.",
    "Option A is incomplete.", "விருப்பம் A அரைகுறையானது.",
    "Option B is correct as statements 1, 2, and 3 are all true.", "விருப்பம் B சரியானது.",
    "Option C is incomplete.", "விருப்பம் C அரைகுறையானது.",
    "Option D is incomplete.", "விருப்பம் D அரைகுறையானது.",
    "💡 TNPSC Tip: Nominated members get 6 months to join any political party; if they join AFTER 6 months, they stand disqualified.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: நியமன உறுப்பினர்கள் 6 மாதத்திற்குள் கட்சி சேரலாம்; 6 மாதத்திற்குப் பின் சேர்ந்தால் தகுதிநீக்கம் செய்யப்படுவர்.",
    "📖 Revision Fact: Decision on disqualification under 10th Schedule is made by Speaker/Chairman (subject to judicial review as per Kihoto Hollohan 1992 case).",
    "📖 திருத்தல் செய்தி: 10-வது அட்டவணை தகுதிநீக்க முடிவை சபாநாயகர் எடுக்கிறார் (நீதிமன்ற ஆய்வுக்கு உட்பட்டது).",
    "Analyze", "High", ["Anti Defection Law", "52nd Amendment", "91st Amendment", "10th Schedule"]
)

# Q66 - Ans: A
add_p3(
    "polity_amendments_gt_066", "Easy", "single_choice",
    "Which Constitutional Amendment Act added Part IX (Articles 243 to 243O) and the 11th Schedule containing 29 functional items to constitutionalize Panchayati Raj?",
    "பஞ்சாயத்து ராஜிற்கு அரசியலமைப்பு அந்தஸ்து வழங்க பகுதி IX (சரத்துகள் 243 முதல் 243O வரை) மற்றும் 29 செயல்பாட்டுத் தலைப்புகளைக் கொண்ட 11-வது அட்டவணையைச் சேர்த்த திருத்தச் சட்டம் எது?",
    "73rd Constitutional Amendment Act, 1992", "73-வது அரசியலமைப்பு திருத்தச் சட்டம், 1992",
    "74th Constitutional Amendment Act, 1992", "74-வது அரசியலமைப்பு திருத்தச் சட்டம், 1992",
    "64th Constitutional Amendment Bill", "64-வது அரசியலமைப்பு திருத்த மசோதா",
    "97th Constitutional Amendment Act, 2011", "97-வது அரசியலமைப்பு திருத்தச் சட்டம், 2011",
    "A",
    "📚 Core Explanation:\nThe 73rd Constitutional Amendment Act, 1992 added Part IX and 11th Schedule (29 functional subjects) to give constitutional status to Panchayati Raj Institutions in India.",
    "📚 முதன்மை விளக்கம்:\n1992-ஆம் ஆண்டின் 73-வது அரசியலமைப்பு திருத்தச் சட்டம் பகுதி IX மற்றும் 11-வது அட்டவணையைச் (29 செயல்பாட்டுத் தலைப்புகள்) சேர்த்து பஞ்சாயத்து ராஜ் அமைப்புகளுக்கு அரசியலமைப்பு அந்தஸ்து வழங்கியது.",
    "Option A is correct; 73rd Amendment constitutionalized Panchayati Raj.", "விருப்பம் A சரியானது.",
    "Option B is incorrect; 74th Amendment related to Municipalities.", "விருப்பம் B தவறானது.",
    "Option C is incorrect; 64th Bill lapsed in Rajya Sabha in 1989.", "விருப்பம் C தவறானது.",
    "Option D is incorrect; 97th Amendment related to Co-operatives.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: 73rd Amendment mandated a 3-tier Panchayati Raj system (Gram Panchayat, Panchayat Samiti, Zilla Parishad) for states with population above 20 lakhs.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: 20 லட்சத்திற்கு மேல் மக்கள் தொகை கொண்ட மாநிலங்களுக்கு 3-அடுக்கு பஞ்சாயத்து முறை கட்டாயமாக்கப்பட்டது.",
    "📖 Revision Fact: 73rd Amendment enacted under P.V. Narasimha Rao government came into force on April 24, 1993.",
    "📖 திருத்தல் செய்தி: நரசிம்ம ராவ் ஆட்சியில் இயற்றப்பட்டு ஏப்ரல் 24, 1993 அன்று அமலுக்கு வந்தது.",
    "Remember", "High", ["73rd Amendment", "Panchayati Raj", "11th Schedule"]
)

# Q67 - Ans: A
add_p3(
    "polity_amendments_gt_067", "Easy", "single_choice",
    "Which Constitutional Amendment Act introduced 1/3rd (33%) mandatory reservation for women in Panchayats and Municipalities under Articles 243D(3) and 243T(3)?",
    "சரத்துகள் 243D(3) மற்றும் 243T(3)-ன் கீழ் பஞ்சாயத்துகள் மற்றும் நகராட்சிகளில் மகளிருக்கு 1/3 பங்கு (33%) கட்டாய இடஒதுக்கீட்டை அறிமுகப்படுத்திய அரசியலமைப்பு திருத்தச் சட்டங்கள் எவை?",
    "73rd and 74th Constitutional Amendment Acts, 1992", "73 மற்றும் 74-வது அரசியலமைப்பு திருத்தச் சட்டங்கள், 1992",
    "42nd and 44th Constitutional Amendment Acts", "42 மற்றும் 44-வது அரசியலமைப்பு திருத்தச் சட்டங்கள்",
    "86th and 91st Constitutional Amendment Acts", "86 மற்றும் 91-வது அரசியலமைப்பு திருத்தச் சட்டங்கள்",
    "103rd and 104th Constitutional Amendment Acts", "103 மற்றும் 104-வது அரசியலமைப்பு திருத்தச் சட்டங்கள்",
    "A",
    "📚 Core Explanation:\nThe 73rd and 74th Constitutional Amendment Acts, 1992 introduced mandatory 33% (one-third) reservation for women in all local self-government bodies (Panchayats & Municipalities), including the office of Chairpersons.",
    "📚 முதன்மை விளக்கம்:\n1992-ஆம் ஆண்டின் 73 மற்றும் 74-வது அரசியலமைப்பு திருத்தச் சட்டங்கள் பஞ்சாயத்துகள் மற்றும் நகராட்சிகளில் தலைவர் பதவிகள் உட்பட மகளிருக்கு 33% கட்டாய இடஒதுக்கீட்டை அறிமுகப்படுத்தின.",
    "Option A is correct; 73rd & 74th Amendments introduced women's reservation in local bodies.", "விருப்பம் A சரியானது.",
    "Option B is incorrect.", "விருப்பம் B தவறானது.",
    "Option C is incorrect.", "விருப்பம் C தவறானது.",
    "Option D is incorrect.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: Tamil Nadu increased women's reservation in local bodies from 33% to 50% in 2016.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: தமிழ்நாடு உள்ளாட்சி அமைப்புகளில் மகளிர் இடஒதுக்கீட்டை 2016-ல் 33%-லிருந்து 50% ஆக உயர்த்தியது.",
    "📖 Revision Fact: Articles 243D (Panchayats) and 243T (Municipalities) provide for reservation of seats for SCs, STs, and Women.",
    "📖 திருத்தல் செய்தி: சரத்து 243D மற்றும் 243T உள்ளாட்சிகளில் SC, ST, மகளிருக்கு இடஒதுக்கீடு வழங்குகிறது.",
    "Remember", "High", ["73rd Amendment", "74th Amendment", "Women Reservation Local Bodies"]
)

# Q68 - Ans: A
add_p3(
    "polity_amendments_gt_068", "Medium", "statement",
    "Consider the following statements regarding the 86th Constitutional Amendment Act, 2002:\n1. It added Article 21A in Part III making free and compulsory education for 6-14 year children a Fundamental Right.\n2. It substituted Article 45 in Part IV directing the State to provide early childhood care and education for all children until they complete 6 years.\n3. It added clause (k) to Article 51A making it a duty of parent/guardian to provide education opportunities to their child aged 6-14 years.\nWhich of the statements given above are correct?",
    "2002-ஆம் ஆண்டின் 86-வது அரசியலமைப்பு திருத்தச் சட்டம் குறித்த பின்வரும் கூற்றுகளை ஆராய்க:\n1. இது பகுதி III-ல் சரத்து 21A-ஐச் சேர்த்து 6-14 வயதுக் குழந்தைகளுக்கு இலவச கட்டாயக் கல்வியை அடிப்படை உரிமையாக்கியது.\n2. இது பகுதி IV-ல் உள்ள சரத்து 45-ஐ மாற்றி 6 வயது முடியும் வரை குழந்தைப் பருவ பராமரிப்பு மற்றும் கல்வியை வழங்க அரசுக்கு வழிகாட்டியது.\n3. இது சரத்து 51A-ல் (k) பிரிவைச் சேர்த்து 6-14 வயதுக் குழந்தைகளுக்கு கல்வி வாய்ப்புகளை வழங்குவதை பெற்றோரின் கடமையாக்கியது.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
    "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
    "1 and 3 only", "1 மற்றும் 3 மட்டுமே",
    "A",
    "📚 Core Explanation:\nAll three statements are CORRECT. The 86th Amendment Act 2002 made a threefold modification in the Constitution concerning education: Part III (Art 21A), Part IV (Art 45), and Part IV-A (Art 51A(k)).",
    "📚 முதன்மை விளக்கம்:\nமூன்று கூற்றுகளும் சரியானவை: 86-வது திருத்தச் சட்டம் 2002 கல்வி தொடர்பாக பகுதி III (21A), பகுதி IV (45), பகுதி IV-A (51A(k)) ஆகிய மூன்று இடங்களில் மாற்றங்களைச் செய்தது.",
    "Option A is correct as statements 1, 2, and 3 are all true.", "விருப்பம் A சரியானது.",
    "Option B is incomplete.", "விருப்பம் B அரைகுறையானது.",
    "Option C is incomplete.", "விருப்பம் C அரைகுறையானது.",
    "Option D is incomplete.", "விருப்பம் D அரைகுறையானது.",
    "💡 TNPSC Tip: Remember: 86th Amendment touched FR, DPSP, AND Fundamental Duty simultaneously.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: 86-வது திருத்தம் அடிப்படை உரிமை, DPSP, அடிப்படை கடமை ஆகிய மூன்றையும் ஒரே நேரத்தில் தொட்டது.",
    "📖 Revision Fact: Right of Children to Free and Compulsory Education (RTE) Act was passed in 2009.",
    "📖 திருத்தல் செய்தி: இலவச கட்டாயக் கல்வி உரிமைச் சட்டம் 2009-ல் இயற்றப்பட்டது.",
    "Analyze", "High", ["86th Amendment", "Article 21A", "Article 45", "Article 51A(k)"]
)

# Q69 - Ans: A
add_p3(
    "polity_amendments_gt_069", "Medium", "single_choice",
    "Which Article of the Constitution was inserted by the 89th Amendment Act, 2003 to establish a separate National Commission for Scheduled Tribes (NCST)?",
    "தனி தேசிய பட்டியல் பழங்குடியினர் ஆணையத்தை (NCST) நிறுவ 89-வது திருத்தச் சட்டம் 2003-ஆல் அரசியலமைப்பில் சேர்க்கப்பட்ட சரத்து எது?",
    "Article 338A", "சரத்து 338A",
    "Article 338B", "சரத்து 338B",
    "Article 338", "சரத்து 338",
    "Article 340", "சரத்து 340",
    "A",
    "📚 Core Explanation:\nThe 89th Constitutional Amendment Act, 2003 inserted Article 338A to create a separate National Commission for Scheduled Tribes (NCST), while Article 338 remained for National Commission for Scheduled Castes (NCSC).",
    "📚 முதன்மை விளக்கம்:\n2003-ஆம் ஆண்டின் 89-வது அரசியலமைப்பு திருத்தச் சட்டம் சரத்து 338A-ஐச் சேர்த்து தனி தேசிய பழங்குடியினர் ஆணையத்தை (NCST) உருவாக்கியது. சரத்து 338 NCSC-க்காக நீடித்தது.",
    "Option A is correct; Article 338A created NCST.", "விருப்பம் A சரியானது.",
    "Option B is incorrect; Article 338B created NCBC (102nd Amendment 2018).", "விருப்பம் B தவறானது.",
    "Option C is incorrect; Article 338 is NCSC.", "விருப்பம் C தவறானது.",
    "Option D is incorrect; Article 340 relates to Backward Classes Commission appointment.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: Article 338 = NCSC, Article 338A = NCST, Article 338B = NCBC.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: சரத்து 338 = NCSC, 338A = NCST, 338B = NCBC.",
    "📖 Revision Fact: NCST consists of a Chairperson, a Vice-Chairperson, and 3 other members appointed by President.",
    "📖 திருத்தல் செய்தி: NCST தலைவர், துணைத் தலைவர் மற்றும் 3 உறுப்பினர்களைக் கொண்டது.",
    "Remember", "High", ["89th Amendment", "Article 338A", "NCST"]
)

# Q70 - Ans: D
add_p3(
    "polity_amendments_gt_070", "Medium", "chronology",
    "Arrange the following amendments adding languages to the Eighth Schedule of the Constitution in correct chronological order:\n1. 21st Amendment Act (Sindhi)\n2. 71st Amendment Act (Konkani, Manipuri, Nepali)\n3. 92nd Amendment Act (Bodo, Dogri, Maithili, Santhali)\n4. 96th Amendment Act (Renaming Oriya to Odia)\nSelect the correct code:",
    "அரசியலமைப்பின் எட்டாவது அட்டவணையில் மொழிகளைச் சேர்த்த பின்வரும் திருத்தங்களை சரியான காலவரிசைப்படி அமைக்கவும்:\n1. 21-வது திருத்தச் சட்டம் (சிந்தி)\n2. 71-வது திருத்தச் சட்டம் (கொங்கணி, மணிப்பூரி, நேபாளி)\n3. 92-வது திருத்தச் சட்டம் (போடோ, டோக்ரி, மைதிலி, சந்தாலி)\n4. 96-வது திருத்தச் சட்டம் (ஒரியா என்பதை ஒடியா என மாற்றம்)\nசரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
    "1 - 3 - 2 - 4", "1 - 3 - 2 - 4",
    "2 - 1 - 3 - 4", "2 - 1 - 3 - 4",
    "1 - 2 - 4 - 3", "1 - 2 - 4 - 3",
    "1 - 2 - 3 - 4", "1 - 2 - 3 - 4",
    "D",
    "📚 Core Explanation:\n- 21st Amendment Act (1967): Sindhi (15th language).\n- 71st Amendment Act (1992): Konkani, Manipuri, Nepali (16-18th languages).\n- 92nd Amendment Act (2003): Bodo, Dogri, Maithili, Santhali (19-22nd languages).\n- 96th Amendment Act (2011): Renamed Oriya to Odia.\nHence, correct chronological sequence is 1 - 2 - 3 - 4.",
    "📚 முதன்மை விளக்கம்:\n- 21-வது திருத்தச் சட்டம் (1967): சிந்தி.\n- 71-வது திருத்தச் சட்டம் (1992): கொங்கணி, மணிப்பூரி, நேபாளி.\n- 92-வது திருத்தச் சட்டம் (2003): போடோ, டோக்ரி, மைதிலி, சந்தாலி.\n- 96-வது திருத்தச் சட்டம் (2011): ஒரியா -> ஒடியா பெயர் மாற்றம்.\nசரியான வரிசை 1 - 2 - 3 - 4.",
    "Option A is incorrect.", "விருப்பம் A தவறானது.",
    "Option B is incorrect.", "விருப்பம் B தவறானது.",
    "Option C is incorrect.", "விருப்பம் C தவறானது.",
    "Option D is correct as 1 (1967) -> 2 (1992) -> 3 (2003) -> 4 (2011).", "விருப்பம் D சரியானது.",
    "💡 TNPSC Tip: 8th Schedule expanded: Original 14 -> 15 (21st) -> 18 (71st) -> 22 (92nd).",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: எட்டாவது அட்டவணை வளர்ச்சி: 14 -> 15 (21-வது) -> 18 (71-வது) -> 22 (92-வது).",
    "📖 Revision Fact: English, Rajasthani, and Bhojpuri are NOT included in Eighth Schedule.",
    "📖 திருத்தல் செய்தி: ஆங்கிலம், ராஜஸ்தானி, போஜ்புரி ஆகியவை எட்டாவது அட்டவணையில் இல்லை.",
    "Apply", "High", ["Chronology", "Eighth Schedule", "Language Amendments"]
)

# Q71 - Ans: D
add_p3(
    "polity_amendments_gt_071", "Hard", "reasoning",
    "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): The Supreme Court in the Fourth Judges Case (2015) struck down the 99th Constitutional Amendment Act and the NJAC Act in its entirety.\nReason (R): Independence of the Judiciary is an essential element of the Basic Structure, and inclusion of the Union Law Minister and two eminent persons in the NJAC compromised judicial independence.\nIn light of the above statements, choose the correct option:",
    "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன. ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிக்கப்பட்டுள்ளது:\n<ctrl42>கூற்று (A): நான்காவது நீதிபதிகள் வழக்கில் (2015) 99-வது அரசியலமைப்பு திருத்தச் சட்டம் மற்றும் NJAC சட்டத்தை உச்சநீதிமன்றம் முழுமையாக ரத்து செய்தது.\nகாரணம் (R): நீதித்துறையின் சுதந்திரம் அடிப்படை கட்டமைப்பின் அத்தியாவசிய அங்கமாகும். NJAC-ல் மத்திய சட்ட அமைச்சர் மற்றும் இரு முக்கிய நபர்களைச் சேர்த்தது நீதித்துறை சுதந்திரத்தைப் பாதித்தது.\nமேற்கண்ட கூற்றுகளின் அடிப்படையில் சரியான விருப்பத்தைத் தேர்ந்தெடுக்கவும்:",
    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)", "(A) மற்றும் (R) இரண்டும் உண்மை ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல",
    "(A) is true but (R) is false", "(A) உண்மை ஆனால் (R) தவறு",
    "(A) is false but (R) is true", "(A) தவறு ஆனால் (R) உண்மை",
    "Both (A) and (R) are true and (R) is the correct explanation of (A)", "(A) மற்றும் (R) இரண்டும் உண்மை மற்றும் (R) என்பது (A)-வின் சரியான விளக்கமாகும்",
    "D",
    "📚 Core Explanation:\nBoth Assertion (A) and Reason (R) are TRUE, and (R) is the correct explanation of (A). In 2015, SC struck down 99th Amendment & NJAC Act because giving executive veto power over judicial appointments violated independence of judiciary.",
    "📚 முதன்மை விளக்கம்:\n(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-ன் சரியான விளக்கம். 2015-ல் உச்சநீதிமன்றம் 99-வது திருத்தத்தை ரத்து செய்தது, ஏனெனில் நிர்வாகத்திற்கு நீதிபதிகள் நியமனத்தில் வீட்டோ அதிகாரம் அளிப்பது நீதித்துறை சுதந்திரத்தைப் பாதிக்கும் எனக் கருதியது.",
    "Option A is incorrect because R explains A.", "விருப்பம் A தவறானது.",
    "Option B is incorrect because R is true.", "விருப்பம் B தவறானது.",
    "Option C is incorrect because A is true.", "விருப்பம் C தவறானது.",
    "Option D is correct as both A and R are true and R explains A.", "விருப்பம் D சரியானது.",
    "💡 TNPSC Tip: 99th Amendment is the ONLY amendment completely struck down by Supreme Court.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: உச்சநீதிமன்றத்தால் முழுமையாக ரத்து செய்யப்பட்ட ஒரே திருத்தம் 99-வது திருத்தம்.",
    "📖 Revision Fact: Collegium system was originally established in Second Judges Case (1993).",
    "📖 திருத்தல் செய்தி: கொலீஜியம் முறை இரண்டாவது நீதிபதிகள் வழக்கில் (1993) உருவாக்கப்பட்டது.",
    "Analyze", "High", ["99th Amendment", "NJAC", "Independence of Judiciary"]
)

# Q72 - Ans: D
add_p3(
    "polity_amendments_gt_072", "Medium", "statement",
    "Consider the following statements regarding the 101st Constitutional Amendment Act, 2016:\n1. It inserted Article 246A conferring concurrent tax power on Parliament and State Legislatures with respect to Goods and Services Tax (GST).\n2. It inserted Article 269A providing that Integrated GST (IGST) on inter-state supply shall be levied and collected by the Government of India.\n3. It inserted Article 279A constituting the GST Council as a constitutional body chaired by the Union Finance Minister.\nWhich of the statements given above are correct?",
    "2016-ஆம் ஆண்டின் 101-வது அரசியலமைப்பு திருத்தச் சட்டம் குறித்த பின்வரும் கூற்றுகளை ஆராய்க:\n1. இது சரத்து 246A-ஐச் சேர்த்து ஜிஎஸ்டி (GST) மீது நாடாளுமன்றம் மற்றும் மாநில சட்டமன்றங்களுக்கு ஒரே நேரத்தில் வரி விதிக்கும் அதிகாரத்தை வழங்கியது.\n2. இது சரத்து 269A-ஐச் சேர்த்து மாநிலங்களுக்கிடையேயான ஒருங்கிணைந்த ஜிஎஸ்டி (IGST) மத்திய அரசால் விதிக்கப்பட்டு வசூலிக்கப்படும் என வகைசெய்தது.\n3. இது சரத்து 279A-ஐச் சேர்த்து மத்திய நிதி அமைச்சர் தலைமையில் ஜிஎஸ்டி கவுன்சிலை அரசியலமைப்பு அமைப்பாக உருவாக்கியது.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
    "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
    "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
    "1 and 3 only", "1 மற்றும் 3 மட்டுமே",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "D",
    "📚 Core Explanation:\nAll three statements are CORRECT regarding 101st Amendment Act, 2016:\n- Art 246A: Special provision for GST (concurrent power).\n- Art 269A: IGST levy & collection by Centre, distributed between Centre & States.\n- Art 279A: GST Council (constitutional body headed by Union FM).",
    "📚 முதன்மை விளக்கம்:\n101-வது திருத்தச் சட்டம் 2016 தொடர்பான மூன்று கூற்றுகளும் சரியானவை: சரத்து 246A (ஜிஎஸ்டி அதிகாரம்), சரத்து 269A (IGST வசூல்), சரத்து 279A (ஜிஎஸ்டி கவுன்சில்).",
    "Option A is incomplete.", "விருப்பம் A அரைகுறையானது.",
    "Option B is incomplete.", "விருப்பம் B அரைகுறையானது.",
    "Option C is incomplete.", "விருப்பம் C அரைகுறையானது.",
    "Option D is correct as all three statements are true.", "விருப்பம் D சரியானது.",
    "💡 TNPSC Tip: Voting power in GST Council: Centre has 1/3rd weightage, all States together have 2/3rd weightage; decision requires 3/4th majority.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: ஜிஎஸ்டி கவுன்சில் வாக்கு உரிமை: மத்திய அரசு 1/3 பங்கு, மாநிலங்கள் 2/3 பங்கு; முடிவு எடுக்க 3/4 பங்கு பெரும்பான்மை தேவை.",
    "📖 Revision Fact: Assam was the FIRST state to ratify the 101st GST Amendment Bill.",
    "📖 திருத்தல் செய்தி: 101-வது ஜிஎஸ்டி திருத்த மசோதாவிற்கு ஒப்புதல் அளித்த முதல் மாநிலம் அசாம் ஆகும்.",
    "Analyze", "High", ["101st Amendment", "GST Council", "Article 246A", "Article 279A"]
)

# Q73 - Ans: D
add_p3(
    "polity_amendments_gt_073", "Medium", "single_choice",
    "Which Constitutional Amendment Act inserted Article 338B to confer constitutional status on the National Commission for Backward Classes (NCBC)?",
    "தேசிய பிற்படுத்தப்பட்டோர் ஆணையத்திற்கு (NCBC) அரசியலமைப்பு அந்தஸ்து வழங்க சரத்து 338B-ஐச் சேர்த்த திருத்தச் சட்டம் எது?",
    "100th Constitutional Amendment Act, 2015", "100-வது அரசியலமைப்பு திருத்தச் சட்டம், 2015",
    "101st Constitutional Amendment Act, 2016", "101-வது அரசியலமைப்பு திருத்தச் சட்டம், 2016",
    "103rd Constitutional Amendment Act, 2019", "103-வது அரசியலமைப்பு திருத்தச் சட்டம், 2019",
    "102nd Constitutional Amendment Act, 2018", "102-வது அரசியலமைப்பு திருத்தச் சட்டம், 2018",
    "D",
    "📚 Core Explanation:\nThe 102nd Constitutional Amendment Act, 2018 inserted Article 338B granting constitutional status to NCBC. It also inserted Article 342A.",
    "📚 முதன்மை விளக்கம்:\n2018-ஆம் ஆண்டின் 102-வது அரசியலமைப்பு திருத்தச் சட்டம் சரத்து 338B-ஐச் சேர்த்து NCBC-க்கு அரசியலமைப்பு அந்தஸ்து வழங்கியது.",
    "Option A is incorrect.", "விருப்பம் A தவறானது.",
    "Option B is incorrect.", "விருப்பம் B தவறானது.",
    "Option C is incorrect.", "விருப்பம் C தவறானது.",
    "Option D is correct; 102nd Amendment inserted Article 338B.", "விருப்பம் D சரியானது.",
    "💡 TNPSC Tip: NCBC consists of a Chairperson, Vice-Chairperson, and 3 other members appointed by President.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: NCBC தலைவர், துணைத் தலைவர், 3 உறுப்பினர்களைக் கொண்டது.",
    "📖 Revision Fact: 105th Amendment 2021 clarified Article 342A to maintain state OBC lists.",
    "📖 திருத்தல் செய்தி: 105-வது திருத்தம் 2021 மாநிலங்களின் OBC பட்டியலைப் பராமரிக்கும் அதிகாரத்தை மீட்டெடுத்தது.",
    "Remember", "High", ["102nd Amendment", "NCBC", "Article 338B"]
)

# Q74 - Ans: D
add_p3(
    "polity_amendments_gt_074", "Hard", "statement",
    "Consider the following statements regarding the 103rd Constitutional Amendment Act, 2019:\n1. It inserted Article 15(6) to enable the State to make special provisions for advancement of Economically Weaker Sections (EWS) in educational admissions.\n2. It inserted Article 16(6) to enable the State to make provisions for reservation in appointments for EWS up to a maximum of 10%.\n3. The Supreme Court in Janhit Abhiyan Case (2022) upheld the 103rd Amendment by a 3:2 majority.\nWhich of the statements given above are correct?",
    "2019-ஆம் ஆண்டின் 103-வது அரசியலமைப்பு திருத்தச் சட்டம் குறித்த பின்வரும் கூற்றுகளை ஆராய்க:\n1. இது EWS பிரிவினருக்கு கல்வி நிறுவன சேர்க்கையில் சிறப்பு விதிகளை உருவாக்க சரத்து 15(6)-ஐச் சேர்த்தது.\n2. இது EWS பிரிவினருக்கு வேலைவாய்ப்பில் அதிகபட்சமாக 10% வரை இடஒதுக்கீடு வழங்க சரத்து 16(6)-ஐச் சேர்த்தது.\n3. ஜன்ஹித் அபியான் வழக்கில் (2022) உச்சநீதிமன்றம் 3:2 பெரும்பான்மையில் 103-வது திருத்தத்தை உறுதி செய்தது.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
    "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
    "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
    "1 and 3 only", "1 மற்றும் 3 மட்டுமே",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "D",
    "📚 Core Explanation:\nAll three statements are CORRECT regarding 103rd Amendment Act 2019 and Janhit Abhiyan (2022) verdict upholding 10% EWS reservation.",
    "📚 முதன்மை விளக்கம்:\nமூன்று கூற்றுகளும் சரியானவை: 103-வது திருத்தம் சரத்து 15(6), 16(6)-ஐச் சேர்த்தது; ஜன்ஹித் அபியான் வழக்கில் (2022) 3:2 பெரும்பான்மையில் உச்சநீதிமன்றம் உறுதி செய்தது.",
    "Option A is incomplete.", "விருப்பம் A அரைகுறையானது.",
    "Option B is incomplete.", "விருப்பம் B அரைகுறையானது.",
    "Option C is incomplete.", "விருப்பம் C அரைகுறையானது.",
    "Option D is correct as all three statements are true.", "விருப்பம் D சரியானது.",
    "💡 TNPSC Tip: EWS quota excludes SCs, STs, and OBCs who are covered under Articles 15(4), 15(5), 16(4).",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: EWS இடஒதுக்கீடு SC, ST, OBC பிரிவினரைத் தவிர்த்து பொதுப் பிரிவில் நலிவடைந்தவர்களுக்கு மட்டுமே.",
    "📖 Revision Fact: Maximum EWS reservation threshold is 10%.",
    "📖 திருத்தல் செய்தி: EWS இடஒதுக்கீட்டின் அதிகபட்ச வரம்பு 10% ஆகும்.",
    "Analyze", "High", ["103rd Amendment", "EWS Reservation", "Janhit Abhiyan Case"]
)

# Q75 - Ans: D
add_p3(
    "polity_amendments_gt_075", "Medium", "single_choice",
    "Which Constitutional Amendment Act extended the reservation of seats for Scheduled Castes (SCs) and Scheduled Tribes (STs) in Lok Sabha and State Assemblies until 2030, while discontinuing the nomination of Anglo-Indian members?",
    "மக்களவை மற்றும் மாநில சட்டமன்றங்களில் SC மற்றும் ST பிரிவினருக்கான இடஒதுக்கீட்டை 2030 வரை நீட்டித்து, ஆங்கிலோ-இந்திய உறுப்பினர்களின் நியமனத்தை நிறுத்திய திருத்தச் சட்டம் எது?",
    "95th Constitutional Amendment Act, 2009", "95-வது அரசியலமைப்பு திருத்தச் சட்டம், 2009",
    "102nd Constitutional Amendment Act, 2018", "102-வது அரசியலமைப்பு திருத்தச் சட்டம், 2018",
    "103rd Constitutional Amendment Act, 2019", "103-வது அரசியலமைப்பு திருத்தச் சட்டம், 2019",
    "104th Constitutional Amendment Act, 2020", "104-வது அரசியலமைப்பு திருத்தச் சட்டம், 2020",
    "D",
    "📚 Core Explanation:\nThe 104th Constitutional Amendment Act, 2020 amended Article 334 to extend SC/ST seat reservation in Lok Sabha and Assemblies by 10 years (from 70 to 80 years, i.e., till 25 January 2030), while ceasing the nomination of Anglo-Indians.",
    "📚 முதன்மை விளக்கம்:\n2020-ஆம் ஆண்டின் 104-வது அரசியலமைப்பு திருத்தச் சட்டம் சரத்து 334-ஐத் திருத்தி மக்களவை மற்றும் சட்டமன்றங்களில் SC/ST இடஒதுக்கீட்டை 2030 வரை நீட்டித்தது; ஆங்கிலோ-இந்தியர் நியமனத்தை நிறுத்தியது.",
    "Option A is incorrect; 95th Amendment extended reservation till 2020.", "விருப்பம் A தவறானது.",
    "Option B is incorrect; 102nd Amendment constitutionalized NCBC.", "விருப்பம் B தவறானது.",
    "Option C is incorrect; 103rd Amendment introduced EWS reservation.", "விருப்பம் C தவறானது.",
    "Option D is correct; 104th Amendment extended SC/ST reservation till 2030 and discontinued Anglo-Indian nomination.", "விருப்பம் D சரியானது.",
    "💡 TNPSC Tip: Previously, President nominated up to 2 Anglo-Indians to Lok Sabha (Art 331) and Governor nominated 1 to State Assembly (Art 333).",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: முன்பு குடியரசுத் தலைவர் 2 ஆங்கிலோ-இந்தியர்களை மக்களவைக்கும் (சரத்து 331), ஆளுநர் 1 நபரை சட்டமன்றத்திற்கும் (சரத்து 333) நியமித்தனர்.",
    "📖 Revision Fact: 104th Amendment came into effect on 25 January 2020.",
    "📖 திருத்தல் செய்தி: 104-வது திருத்தம் ஜனவரி 25, 2020 அன்று அமலுக்கு வந்தது.",
    "Remember", "High", ["104th Amendment", "SC ST Reservation Extension", "Anglo Indian Nomination Ceased"]
)

print("Part 3 questions Q51 to Q75 loaded completely.")
