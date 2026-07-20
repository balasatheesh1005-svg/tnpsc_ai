import json

def get_part1_questions():
    questions = []
    
    def make_q(id_num, diff, q_type, q_en, q_ta, opt_list, ans, exp_en, exp_ta, wno, tip_en, tip_ta, rf_en, rf_ta, tags, bloom="Understand", est_time=60):
        ans_upper = ans.upper()
        ans_lower = ans.lower()
        
        opts_dict = []
        opts_en = []
        opts_ta = []
        for opt_id, o_en, o_ta in opt_list:
            opts_dict.append({"id": opt_id, "en": o_en, "ta": o_ta})
            opts_en.append(o_en)
            opts_ta.append(o_ta)
            
        return {
            "id": f"HB_GT_{id_num:03d}",
            "subject": "Polity",
            "topic": "Historical Background of the Indian Constitution",
            "difficulty": diff,
            "question_type": q_type,
            "question": {"en": q_en, "ta": q_ta},
            "options": opts_dict,
            "correct_answer": ans_upper,
            "explanation": {"en": exp_en, "ta": exp_ta},
            "why_not_others": wno,
            "tnpsc_tip": {"en": tip_en, "ta": tip_ta},
            "revision_fact": {"en": rf_en, "ta": rf_ta},
            "source_reference": [
                "M. Laxmikanth - Indian Polity",
                "NCERT Class XI/XII - Indian Constitution at Work",
                "Samacheer Kalvi - Standard 11/12 Political Science"
            ],
            "bloom_level": bloom,
            "estimated_time_sec": est_time,
            "pyq_similarity": "High",
            "tags": tags,
            "question_en": q_en,
            "question_ta": q_ta,
            "options_en": opts_en,
            "options_ta": opts_ta,
            "answer": ans_lower,
            "explanation_en": exp_en,
            "explanation_ta": exp_ta
        }

    # Q1: Direct MCQ - Easy - Regulating Act 1773
    questions.append(make_q(
        1, "Easy", "Direct MCQ",
        "Which statutory enactment designated the Governor of Bengal as the 'Governor-General of Bengal' and created an Executive Council of four members to assist him?",
        "வங்காளத்தின் ஆளுநரை 'வங்காள கவர்னர்-ஜெனரல்' என மாற்றி, அவருக்கு உதவ 4 உறுப்பினர்களைக் கொண்ட நிர்வாகக் குழுவை உருவாக்கிய சட்டப்பூர்வ சட்டம் எது?",
        [
            ("A", "Regulating Act of 1773", "1773 ஆம் ஆண்டின் ஒழுங்குமுறைச் சட்டம்"),
            ("B", "Pitt's India Act of 1784", "1784 ஆம் ஆண்டின் பிட் இந்தியச் சட்டம்"),
            ("C", "Charter Act of 1813", "1813 ஆம் ஆண்டின் சாசனச் சட்டம்"),
            ("D", "Charter Act of 1833", "1833 ஆம் ஆண்டின் சாசனச் சட்டம்")
        ],
        "A",
        "Historical Context: Passed by the British Parliament to control and regulate the affairs of the East India Company in India.\nReason: It elevated the Governor of Bengal (Warren Hastings) to Governor-General of Bengal with an Executive Council of 4 members.\nConstitutional Impact: Laid the foundation of central administration in India.\nExam Trap: Do not confuse Governor-General of Bengal (1773) with Governor-General of India (1833).\nMemory Trick: Regulating 1773 = First step of parliamentary control.",
        "வரலாற்றுப் பின்னணி: கிழக்கிந்திய கம்பெனியின் விவகாரங்களைக் கட்டுப்படுத்த பிரிட்டிஷ் நாடாளுமன்றத்தால் நிறைவேற்றப்பட்டது.\nகாரணம்: இது வங்காள ஆளுநரை (வாரன் ஹேஸ்டிங்ஸ்) 4 உறுப்பினர் கொண்ட நிர்வாகக் குழுவுடன் கவர்னர்-ஜெனரலாக உயர்த்தியது.\nஅரசியலமைப்பு தாக்கம்: இந்தியாவில் மத்திய நிர்வாகத்தின் அடித்தளத்தை அமைத்தது.\nதேர்வுப் பொறி: 1773-ன் வங்காள கவர்னர்-ஜெனரலை 1833-ன் இந்திய கவர்னர்-ஜெனரலுடன் குழப்ப வேண்டாம்.\nநினைவுச் சூத்திரம்: 1773 ஒழுங்குமுறை = நாடாளுமன்றக் கட்டுப்பாட்டின் முதல் படி.",
        {
            "A": {"en": "Correct. The 1773 Act designated the Governor of Bengal as Governor-General of Bengal.", "ta": "சரி. 1773 சட்டம் வங்காள ஆளுநரை வங்காள கவர்னர்-ஜெனரலாக மாற்றியது."},
            "B": {"en": "Incorrect. Pitt's India Act 1784 created the Board of Control.", "ta": "தவறு. 1784 பிட் இந்தியச் சட்டம் கட்டுப்பாட்டு வாரியத்தை உருவாக்கியது."},
            "C": {"en": "Incorrect. Charter Act 1813 ended EIC monopoly except tea and China trade.", "ta": "தவறு. 1813 சாசனச் சட்டம் தேயிலை, சீனா வர்த்தகம் தவிர்த்து முற்றுரிமையை ஒழித்தது."},
            "D": {"en": "Incorrect. Charter Act 1833 designated Governor-General of Bengal as Governor-General of India.", "ta": "தவறு. 1833 சாசனச் சட்டம் வங்காள கவர்னர்-ஜெனரலை இந்திய கவர்னர்-ஜெனரலாக மாற்றியது."}
        },
        "TNPSC Trap: Warren Hastings was the first Governor-General of Bengal (1773), while Lord William Bentinck was the first Governor-General of India (1833).",
        "TNPSC பொறி: வாரன் ஹேஸ்டிங்ஸ் முதல் வங்காள கவர்னர்-ஜெனரல் (1773), வில்லியம் பென்டிங்க் முதல் இந்திய கவர்னர்-ஜெனரல் (1833).",
        "Regulating Act 1773 created Governor-General of Bengal & Supreme Court at Fort William (1774).",
        "1773 ஒழுங்குமுறைச் சட்டம் வங்காள கவர்னர்-ஜெனரலையும் வில்லியம் கோட்டை உச்ச நீதிமன்றத்தையும் (1774) உருவாக்கியது.",
        ["Polity", "Historical Background", "Regulating Act 1773", "Grand Test"], "Remember", 45
    ))

    # Q2: Multi-Act Comparative - Medium - 1773 + 1784
    questions.append(make_q(
        2, "Medium", "Multi-Act Comparative",
        "Which structural administrative transformation distinguished Pitt's India Act of 1784 from the Regulating Act of 1773?",
        "1784 ஆம் ஆண்டின் பிட் இந்தியச் சட்டத்தை 1773 ஆம் ஆண்டின் ஒழுங்குமுறைச் சட்டத்திலிருந்து வேறுபடுத்திய கட்டமைப்பு நிர்வாக மாற்றம் எது?",
        [
            ("A", "Abolition of the Court of Directors and replacement by the Secretary of State", "இயக்குநர்கள் அவையைக் கலைத்துவிட்டு அரசுச் செயலரை நியமித்தல்"),
            ("B", "Establishment of a dual system of control by creating a Board of Control for political affairs while leaving commercial affairs to the Court of Directors", "அரசியல் விவகாரங்களுக்கு கட்டுப்பாட்டு வாரியத்தை உருவாக்கி, வணிக விவகாரங்களை இயக்குநர்கள் அவையிடம் விட்டு இரட்டை நிர்வாக முறையை நிறுவுதல்"),
            ("C", "Centralization of all legislative powers in the Governor-General of India", "அனைத்து சட்ட அதிகாரங்களையும் இந்திய கவர்னர்-ஜெனரலிடம் மையப்படுத்துதல்"),
            ("D", "Introduction of direct elections for non-official members", "அதிகாரப்பூர்வமற்ற உறுப்பினர்களுக்கு நேரடித் தேர்தலை அறிமுகப்படுத்துதல்")
        ],
        "B",
        "Historical Context: The 1773 Act failed to clearly separate commercial and political functions, leading to conflicts.\nReason: Pitt's India Act 1784 established the Board of Control (6 Privy Councillors) to manage political, military, and revenue affairs, creating Dual Control.\nConstitutional Impact: For the first time, EIC territories were termed 'British possessions in India'.\nExam Trap: Court of Directors was not abolished in 1784; it continued managing commercial affairs until 1858.\nMemory Trick: 1784 = Dual System (Directors + Board of Control).",
        "வரலாற்றுப் பின்னணி: 1773 சட்டம் வணிக மற்றும் அரசியல் பணிகளைத் தெளிவாகப் பிரிக்கத் தவறியது.\nகாரணம்: 1784 பிட் இந்தியச் சட்டம் அரசியல், இராணுவ மற்றும் வருவாய் விவகாரங்களை நிர்வகிக்க கட்டுப்பாட்டு வாரியத்தை உருவாக்கி இரட்டை ஆட்சியை நிறுவியது.\nஅரசியலமைப்பு தாக்கம்: கம்பெனி நிலப்பரப்புகள் முதன்முறையாக 'இந்தியாவில் உள்ள பிரிட்டிஷ் உடமைகள்' என அழைக்கப்பட்டன.\nதேர்வுப் பொறி: 1784-ல் இயக்குநர்கள் அவை கலைக்கப்படவில்லை; அது 1858 வரை வணிகத்தை நிர்வகித்தது.\nநினைவுச் சூத்திரம்: 1784 = இரட்டை நிர்வாகம் (இயக்குநர்கள் + கட்டுப்பாட்டு வாரியம்).",
        {
            "A": {"en": "Incorrect. Court of Directors was abolished in 1858, not 1784.", "ta": "தவறு. இயக்குநர்கள் அவை 1858-ல் கலைக்கப்பட்டது, 1784-ல் அல்ல."},
            "B": {"en": "Correct. 1784 Act created Board of Control for political affairs, instituting Dual Control.", "ta": "சரி. 1784 சட்டம் அரசியல் விவகாரங்களுக்கு கட்டுப்பாட்டு வாரியத்தை உருவாக்கி இரட்டை ஆட்சியை நிறுவியது."},
            "C": {"en": "Incorrect. Centralization of legislative powers was completed by 1833 Charter Act.", "ta": "தவறு. சட்ட அதிகார மையமாக்கல் 1833 சாசனச் சட்டத்தில் நிறைவடைந்தது."},
            "D": {"en": "Incorrect. Direct elections were introduced much later under the 1919 Act.", "ta": "தவறு. நேரடித் தேர்தல் 1919 சட்டத்திலேயே அறிமுகமானது."}
        },
        "TNPSC Trap: Board of Control was created in 1784, but its expenses were charged on Indian revenues starting from Charter Act 1793.",
        "TNPSC பொறி: கட்டுப்பாட்டு வாரியம் 1784-ல் உருவாக்கப்பட்டது, ஆனால் அதன் செலவுகள் 1793 சாசனச் சட்டத்திலிருந்தே இந்திய வருவாயிலிருந்து வழங்கப்பட்டன.",
        "1784 Act established Dual Control: Court of Directors (Commercial) & Board of Control (Political).",
        "1784 சட்டம் இரட்டை ஆட்சியை நிறுவியது: இயக்குநர்கள் அவை (வணிகம்) & கட்டுப்பாட்டு வாரியம் (அரசியல்).",
        ["Polity", "Historical Background", "Pitts India Act 1784", "Regulating Act 1773", "Grand Test"], "Understand", 60
    ))

    # Q3: Statement Based - Hard - Charter Act 1833
    questions.append(make_q(
        3, "Hard", "Statement Based",
        "Consider the following statements regarding the Charter Act of 1833:\n1. It transformed the Governor-General of Bengal into the Governor-General of India, vesting in him all civil and military powers.\n2. It completely deprived the Governors of Bombay and Madras of their legislative powers.\n3. It successfully established an open competitive examination system for civil service recruitment.\nWhich of the statements given above is/are correct?",
        "1833 ஆம் ஆண்டின் சாசனச் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது வங்காள கவர்னர்-ஜெனரலை அனைத்து சிவில் மற்றும் இராணுவ அதிகாரங்களையும் கொண்ட இந்திய கவர்னர்-ஜெனரலாக மாற்றியது.\n2. இது பம்பாய் மற்றும் மதராஸ் ஆளுநர்களின் சட்ட அதிகாரங்களை முற்றிலும் பறித்தது.\n3. இது சிவில் சர்வீஸ் நியமனத்திற்கான திறந்தவெளி போட்டித் தேர்வு முறையை வெற்றிகரமாக நிறுவியது.\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானவை?",
        [
            ("A", "1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
            ("B", "2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
            ("C", "1 and 3 only", "1 மற்றும் 3 மட்டுமே"),
            ("D", "1, 2 and 3", "1, 2 மற்றும் 3")
        ],
        "A",
        "Historical Context: Charter Act 1833 was the final step towards administrative centralization under Company Rule.\nReason: Statements 1 and 2 are correct. Statement 3 is incorrect because Section 87 of the 1833 Act attempted to open civil services to Indians, but the provision was negated/dropped due to severe opposition from the Court of Directors.\nConstitutional Impact: Open competition was finally introduced by the Charter Act of 1853.\nExam Trap: Attempted in 1833 (failed); introduced in 1853 (successful).\nMemory Trick: 1833 = Full Centralization + Failed Civil Services attempt.",
        "வரலாற்றுப் பின்னணி: 1833 சாசனச் சட்டம் கம்பெனி ஆட்சியில் நிர்வாக மையமாக்கலின் இறுதிப் படியாகும்.\nகாரணம்: கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் 1833 சட்டத்தின் பிரிவு 87 சிவில் சர்வீஸைத் திறக்க முயன்றாலும் இயக்குநர்கள் அவையின் எதிர்ப்பால் அது கைவிடப்பட்டது.\nஅரசியலமைப்பு தாக்கம்: திறந்தவெளி போட்டித் தேர்வு 1853 சாசனச் சட்டத்திலேயே இறுதியாக அறிமுகப்படுத்தப்பட்டது.\nதேர்வுப் பொறி: 1833-ல் முயற்சி (தோல்வி); 1853-ல் அறிமுகம் (வெற்றி).\nநினைவுச் சூத்திரம்: 1833 = முழுமையான மையமாக்கல் + தோல்வியடைந்த சிவில் சர்வீஸ் முயற்சி.",
        {
            "A": {"en": "Correct. Statements 1 and 2 are true. Statement 3 is false because open competition was negated in 1833.", "ta": "சரி. கூற்றுகள் 1 மற்றும் 2 சரி. 1833-ல் போட்டித் தேர்வு முயற்சி ரத்து செய்யப்பட்டதால் 3 தவறு."},
            "B": {"en": "Incorrect. Statement 3 is false, and Statement 1 is true.", "ta": "தவறு. கூற்று 3 தவறு, கூற்று 1 சரி."},
            "C": {"en": "Incorrect. Statement 3 is false, and Statement 2 is true.", "ta": "தவறு. கூற்று 3 தவறு, கூற்று 2 சரி."},
            "D": {"en": "Incorrect. Statement 3 is false.", "ta": "தவறு. கூற்று 3 தவறானது."}
        },
        "TNPSC Trap: Section 87 of 1833 Act declared no Indian should be barred from holding office, but implementation was blocked by Court of Directors.",
        "TNPSC பொறி: 1833 சட்டத்தின் பிரிவு 87 எந்த இந்தியரும் வேலைவாய்ப்பிலிருந்து தடுக்கப்படக் கூடாது எனக் கூறியது, ஆனால் இயக்குநர்கள் அவை அதைத் தடுத்தது.",
        "Lord William Bentinck was the first Governor-General of India created under the Charter Act of 1833.",
        "1833 சாசனச் சட்டத்தின் கீழ் உருவாக்கப்பட்ட இந்தியாவின் முதல் கவர்னர்-ஜெனரல் லார்டு வில்லியம் பென்டிங்க் ஆவார்.",
        ["Polity", "Historical Background", "Charter Act 1833", "Civil Services", "Grand Test"], "Analyze", 75
    ))

    # Q4: Assertion & Reason - Hard - Charter Act 1853
    questions.append(make_q(
        4, "Hard", "Assertion & Reason",
        "Assertion (A): The Charter Act of 1853 separated, for the first time, the legislative and executive functions of the Governor-General's Council.\nReason (R): It added six new members called legislative councillors to the Council, establishing a distinct legislative body known as the Indian (Central) Legislative Council.",
        "கூற்று (A): 1853 ஆம் ஆண்டின் சாசனச் சட்டம் முதன்முறையாக கவர்னர்-ஜெனரல் கவுன்சிலின் சட்ட மற்றும் நிர்வாகப் பணிகளைப் பிரித்தது.\nகாரணம் (R): இது கவுன்சிலில் சட்ட மேலவை உறுப்பினர்கள் எனப்படும் ஆறு புதிய உறுப்பினர்களைச் சேர்த்து, இந்திய (மத்திய) சட்ட மேலவை என்ற தனி அமைப்பை உருவாக்கியது.",
        [
            ("A", "Both (A) and (R) are true and (R) is the correct explanation of (A)", "(A) மற்றும் (R) இரண்டும் உண்மை, மேலும் (R) என்பது (A)-வின் சரியான விளக்கமாகும்"),
            ("B", "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கமல்ல"),
            ("C", "(A) is true but (R) is false", "(A) உண்மை, ஆனால் (R) தவறு"),
            ("D", "(A) is false but (R) is true", "(A) தவறு, ஆனால் (R) உண்மை")
        ],
        "A",
        "Historical Context: Charter Act 1853 was the last of the Charter Acts and instituted key parliamentary procedure mechanisms.\nReason: Both (A) and (R) are true, and (R) directly explains (A). The addition of 6 legislative councillors created a mini-parliament that adopted British parliamentary procedure.\nConstitutional Impact: Introduced local representation in the Central Legislative Council (4 of 6 members appointed by local governments of Madras, Bombay, Bengal, and Agra).\nExam Trap: Local representation started in 1853 (official legislative members), not 1861.\nMemory Trick: 1853 = Mini-Parliament + 6 Legislative Councillors.",
        "வரலாற்றுப் பின்னணி: 1853 சாசனச் சட்டம் சாசனச் சட்டங்களின் வரிசையில் கடைசியானது மற்றும் நாடாளுமன்ற நடைமுறைகளைத் தொடங்கியது.\nகாரணம்: (A) மற்றும் (R) இரண்டும் உண்மை, (R) என்பது (A)-வின் நேரடி விளக்கம். 6 புதிய சட்ட உறுப்பினர்கள் சேர்க்கப்பட்டு பிரிட்டிஷ் முறைப்படி இயங்கும் சிறிய நாடாளுமன்றம் உருவானது.\nஅரசியலமைப்பு தாக்கம்: மத்திய சட்ட மேலவையில் உள்ளூர் பிரதிநிதித்துவம் அறிமுகமானது (6-ல் 4 பேர் மதராஸ், பம்பாய், வங்காளம், ஆக்ரா உள்ளூர் அரசுகளால் நியமிக்கப்பட்டனர்).\nதேர்வுப் பொறி: உள்ளூர் பிரதிநிதித்துவம் 1853-ல் தொடங்கியது (அதிகாரப்பூர்வ உறுப்பினர்கள்), 1861-ல் அல்ல.\nநினைவுச் சூத்திரம்: 1853 = சிறிய நாடாளுமன்றம் + 6 சட்ட உறுப்பினர்கள்.",
        {
            "A": {"en": "Correct. (R) correctly explains why legislative and executive functions were separated.", "ta": "சரி. சட்ட மற்றும் நிர்வாகப் பணிகள் ஏன் பிரிக்கப்பட்டன என்பதை (R) சரியாக விளக்குகிறது."},
            "B": {"en": "Incorrect. Reason directly provides the cause for Assertion.", "ta": "தவறு. காரணம் கூற்றிற்கான நேரடிக் காரணியை அளிக்கிறது."},
            "C": {"en": "Incorrect. Reason is true.", "ta": "தவறு. காரணம் உண்மையானது."},
            "D": {"en": "Incorrect. Assertion is true.", "ta": "தவறு. கூற்று உண்மையானது."}
        },
        "TNPSC Trap: Macaulay Committee on Indian Civil Service was appointed in 1854 following the 1853 Act.",
        "TNPSC பொறி: 1853 சட்டத்தைத் தொடர்ந்து 1854-ல் இந்திய சிவில் சர்வீஸுக்கான மெக்காலே குழு நியமிக்கப்பட்டது.",
        "1853 Act was the first time local representation was introduced in the Central Legislative Council.",
        "1853 சட்டத்திலேயே முதன்முறையாக மத்திய சட்ட மேலவையில் உள்ளூர் பிரதிநிதித்துவம் அறிமுகப்படுத்தப்பட்டது.",
        ["Polity", "Historical Background", "Charter Act 1853", "Legislative Council", "Grand Test"], "Evaluate", 90
    ))

    # Q5: Match the Following - Medium - Institutions & Acts
    questions.append(make_q(
        5, "Medium", "Match the Following",
        "Match List I (Institutions / Landmark Provisions) with List II (Enacting Statutory Legislation):\n\nList I\nA. Supreme Court of Judicature at Fort William\nB. Board of Control for Political Affairs\nC. High Courts in Calcutta, Bombay, and Madras\nD. Federal Court of India\n\nList II\n1. Government of India Act, 1858\n2. Indian High Courts Act, 1861\n3. Regulating Act, 1773\n4. Pitt's India Act, 1784\n5. Government of India Act, 1935",
        "பட்டியல் I (நிறுவனங்கள் / முக்கிய விதிகளை) பட்டியல் II (இயற்றப்பட்ட சட்டங்கள்) உடன் பொருத்துக:\n\nபட்டியல் I\nA. வில்லியம் கோட்டை உச்ச நீதிமன்றம்\nB. அரசியல் விவகாரங்களுக்கான கட்டுப்பாட்டு வாரியம்\nC. கொல்கத்தா, பம்பாய், மதராஸ் உயர் நீதிமன்றங்கள்\nD. இந்தியாவின் கூட்டாட்சி நீதிமன்றம்\n\nபட்டியல் II\n1. 1858 இந்திய அரசுச் சட்டம்\n2. 1861 இந்திய உயர் நீதிமன்றங்கள் சட்டம்\n3. 1773 ஒழுங்குமுறைச் சட்டம்\n4. 1784 பிட் இந்தியச் சட்டம்\n5. 1935 இந்திய அரசுச் சட்டம்",
        [
            ("A", "A-3, B-4, C-2, D-5", "A-3, B-4, C-2, D-5"),
            ("B", "A-4, B-3, C-2, D-1", "A-4, B-3, C-2, D-1"),
            ("C", "A-3, B-1, C-4, D-5", "A-3, B-1, C-4, D-5"),
            ("D", "A-2, B-4, C-1, D-3", "A-2, B-4, C-1, D-3")
        ],
        "A",
        "Historical Context: Judicial and institutional evolution spanned multiple legislative enactments over 160 years.\nReason: Correct matches are A-3 (Fort William Supreme Court $\rightarrow$ Regulating Act 1773, set up 1774), B-4 (Board of Control $\rightarrow$ Pitt's India Act 1784), C-2 (High Courts $\rightarrow$ Indian High Courts Act 1861, set up 1862), D-5 (Federal Court $\rightarrow$ Government of India Act 1935, set up 1937).\nConstitutional Impact: Established hierarchical judicial evolution in British India.\nExam Trap: Supreme Court at Calcutta was created by 1773 Act (established 1774), Federal Court by 1935 Act (established 1937).\nMemory Trick: SC 1773 $\rightarrow$ Board 1784 $\rightarrow$ HC 1861 $\rightarrow$ Federal 1935.",
        "வரலாற்றுப் பின்னணி: நீதித்துறை மற்றும் நிறுவன வளர்ச்சி 160 ஆண்டுகால சட்டங்கள் வழியாக நிகழ்ந்தது.\nகாரணம்: சரியான பொருத்தம்: A-3 (வில்லியம் கோட்டை உச்ச நீதிமன்றம் $\rightarrow$ 1773 ஒழுங்குமுறைச் சட்டம்), B-4 (கட்டுப்பாட்டு வாரியம் $\rightarrow$ 1784 பிட் இந்தியச் சட்டம்), C-2 (உயர் நீதிமன்றங்கள் $\rightarrow$ 1861 இந்திய உயர் நீதிமன்றங்கள் சட்டம்), D-5 (கூட்டாட்சி நீதிமன்றம் $\rightarrow$ 1935 இந்திய அரசுச் சட்டம்).\nஅரசியலமைப்பு தாக்கம்: பிரிட்டிஷ் இந்தியாவில் படிநிலை நீதித்துறை வளர்ச்சியை நிறுவியது.\nதேர்வுப் பொறி: வில்லியம் கோட்டை உச்ச நீதிமன்றம் 1773 சட்டம் (அமைந்தது 1774); கூட்டாட்சி நீதிமன்றம் 1935 சட்டம் (அமைந்தது 1937).\nநினைவுச் சூத்திரம்: உச்ச 1773 $\rightarrow$ வாரியம் 1784 $\rightarrow$ உயர் 1861 $\rightarrow$ கூட்டாட்சி 1935.",
        {
            "A": {"en": "Correct match across all four judicial and executive institutions.", "ta": "சரி. நான்கு நீதி மற்றும் நிர்வாக நிறுவனங்களுக்கும் சரியான பொருத்தம்."},
            "B": {"en": "Incorrect. Supreme Court Fort William was 1773 Act (3), not 1784.", "ta": "தவறு. வில்லியம் கோட்டை உச்ச நீதிமன்றம் 1773 சட்டம் (3)."},
            "C": {"en": "Incorrect. Board of Control was created in 1784 Act (4).", "ta": "தவறு. கட்டுப்பாட்டு வாரியம் 1784 சட்டம் (4)."},
            "D": {"en": "Incorrect. Federal Court was created under 1935 Act (5).", "ta": "தவறு. கூட்டாட்சி நீதிமன்றம் 1935 சட்டம் (5)."}
        },
        "TNPSC Trap: High Courts were established in 1862 at Calcutta, Bombay, and Madras under the Indian High Courts Act of 1861.",
        "TNPSC பொறி: 1861 உயர் நீதிமன்ற சட்டத்தின் கீழ் கொல்கத்தா, பம்பாய், மதராஸ் உயர் நீதிமன்றங்கள் 1862-ல் அமைக்கப்பட்டன.",
        "Federal Court of India (1937) was converted into the Supreme Court of India in 1950.",
        "இந்தியாவின் கூட்டாட்சி நீதிமன்றம் (1937) 1950-ல் இந்திய உச்ச நீதிமன்றமாக மாற்றப்பட்டது.",
        ["Polity", "Historical Background", "Match the Following", "Judiciary Evolution", "Grand Test"], "Analyze", 75
    ))

    # Q6: Chronology - Medium - Acts Chronology
    questions.append(make_q(
        6, "Medium", "Chronology",
        "Identify the correct chronological sequence of the following landmark constitutional developments:\n1. Indian Councils Act introducing separate electorates for Muslims\n2. Charter Act abolishing East India Company's trade monopoly in India (except tea and China trade)\n3. Act for the Better Government of India transferring authority to the British Crown\n4. Introduction of Dyarchy in Indian Provinces",
        "பின்வரும் முக்கிய அரசியலமைப்பு உருவாக்கங்களின் சரியான காலவரிசையைக் கண்டறிக:\n1. முஸ்லிம்களுக்கு தனித் தொகுதிகளை அறிமுகப்படுத்திய இந்தியக் கவுன்சில்கள் சட்டம்\n2. கிழக்கிந்திய கம்பெனியின் வர்த்தக முற்றுரிமையை (தேயிலை, சீனா தவிர) ஒழித்த சாசனச் சட்டம்\n3. பிரிட்டிஷ் முடியாட்சிக்கு அதிகாரத்தை மாற்றிய இந்திய நல்வாட்சிச் சட்டம்\n4. இந்திய மாகாணங்களில் இரட்டை ஆட்சியை அறிமுகப்படுத்துதல்",
        [
            ("A", "2 -> 3 -> 1 -> 4", "2 -> 3 -> 1 -> 4"),
            ("B", "3 -> 2 -> 1 -> 4", "3 -> 2 -> 1 -> 4"),
            ("C", "2 -> 1 -> 3 -> 4", "2 -> 1 -> 3 -> 4"),
            ("D", "2 -> 3 -> 4 -> 1", "2 -> 3 -> 4 -> 1")
        ],
        "A",
        "Historical Context: Understanding statutory chronology shows the evolution from commercial company rule to responsible crown governance.\nReason: Sequence is: 2 (Charter Act 1813) $\rightarrow$ 3 (Act for Better Government of India 1858) $\rightarrow$ 1 (Indian Councils Act 1909 / Morley-Minto) $\rightarrow$ 4 (Government of India Act 1919 / Montagu-Chelmsford Dyarchy in provinces).\nConstitutional Impact: Progressive transition of constitutional power.\nExam Trap: Do not mix 1813 (partial trade monopoly end) with 1833 (total trade monopoly end).\nMemory Trick: 1813 (Trade) $\rightarrow$ 1858 (Crown) $\rightarrow$ 1909 (Separate Electorate) $\rightarrow$ 1919 (Dyarchy).",
        "வரலாற்றுப் பின்னணி: சட்டங்களின் காலவரிசையைப் புரிந்துகொள்வது வர்த்தகக் கம்பெனியிலிருந்து பிரிட்டிஷ் முடி ஆட்சி வரையிலான வளர்ச்சியைக் காட்டுகிறது.\nகாரணம்: வரிசை: 2 (1813 சாசனச் சட்டம்) $\rightarrow$ 3 (1858 இந்திய நல்வாட்சிச் சட்டம்) $\rightarrow$ 1 (1909 மோலி-மிண்டோ தனித் தொகுதி) $\rightarrow$ 4 (1919 மாண்டேகு-செம்ஸ்ஃபோர்டு மாகாண இரட்டை ஆட்சி).\nஅரசியலமைப்பு தாக்கம்: அரசியலமைப்பு அதிகாரத்தின் படிமுறை மாற்றம்.\nதேர்வுப் பொறி: 1813 (பகுதி வர்த்தக முற்றுரிமை முடிவு) மற்றும் 1833 (முழு வர்த்தக முற்றுரிமை முடிவு) ஆகியவற்றை குழப்ப வேண்டாம்.\nநினைவுச் சூத்திரம்: 1813 (வர்த்தகம்) $\rightarrow$ 1858 (முடி ஆட்சி) $\rightarrow$ 1909 (தனித் தொகுதி) $\rightarrow$ 1919 (இரட்டை ஆட்சி).",
        {
            "A": {"en": "Correct chronological order: 1813 -> 1858 -> 1909 -> 1919.", "ta": "சரி. காலவரிசை: 1813 -> 1858 -> 1909 -> 1919."},
            "B": {"en": "Incorrect. Charter Act 1813 (2) preceded the GOI Act 1858 (3).", "ta": "தவறு. 1813 சாசனச் சட்டம் 1858 சட்டத்திற்கு முந்தியது."},
            "C": {"en": "Incorrect. 1858 Act (3) preceded 1909 Morley-Minto Act (1).", "ta": "தவறு. 1858 சட்டம் 1909 சட்டத்திற்கு முந்தியது."},
            "D": {"en": "Incorrect. 1909 Act (1) came before 1919 Act (4).", "ta": "தவறு. 1909 சட்டம் 1919 சட்டத்திற்கு முந்தியது."}
        },
        "TNPSC Trap: 1813 ended monopoly except Tea & China trade; 1833 ended even Tea & China trade completely.",
        "TNPSC பொறி: 1813 தேயிலை, சீனா தவிர்த்து முற்றுரிமையை ஒழித்தது; 1833 தேயிலை, சீன வர்த்தகத்தையும் முற்றிலும் ஒழித்தது.",
        "Government of India Act 1858 was known as the 'Act for the Better Government of India'.",
        "1858 இந்திய அரசுச் சட்டம் 'இந்திய நல்வாட்சிச் சட்டம்' என அழைக்கப்பட்டது.",
        ["Polity", "Historical Background", "Chronology", "Grand Test"], "Analyze", 75
    ))

    # Q7: Multi-Act Integrated - Hard - Executive Council Evolution
    questions.append(make_q(
        7, "Hard", "Multi-Act Integrated",
        "Which inference accurately summarizes the multi-stage structural evolution of the Governor-General's / Viceroy's Executive Council across the 1773, 1833, 1861, and 1909 enactments?",
        "1773, 1833, 1861 மற்றும் 1909 சட்டங்களின் வழியாக கவர்னர்-ஜெனரல் / வைஸ்ராயின் நிர்வாகக் குழு அடைந்த கட்டமைப்பு வளர்ச்சியைத் துல்லியமாக விளக்கும் முடிவு எது?",
        [
            ("A", "4 Executive Members created (1773) -> 4th Law Member added (1833) -> 5th Finance Member added & Portfolio System recognized (1861) -> 1st Indian Member appointed (1909)", "4 நிர்வாக உறுப்பினர்கள் (1773) -> 4வது சட்ட உறுப்பினர் சேர்க்கை (1833) -> 5வது நிதி உறுப்பினர் சேர்க்கை & இலாகா முறை (1861) -> 1வது இந்திய உறுப்பினர் நியமனம் (1909)"),
            ("B", "4th Law Member added (1773) -> 4 Executive Members created (1833) -> 1st Indian Member (1861) -> 5th Member added (1909)", "4வது சட்ட உறுப்பினர் (1773) -> 4 நிர்வாக உறுப்பினர்கள் (1833) -> 1வது இந்திய உறுப்பினர் (1861) -> 5வது உறுப்பினர் (1909)"),
            ("C", "1st Indian Member (1773) -> 4 Executive Members (1833) -> 4th Law Member (1861) -> 5th Member (1909)", "1வது இந்திய உறுப்பினர் (1773) -> 4 நிர்வாக உறுப்பினர்கள் (1833) -> 4வது சட்ட உறுப்பினர் (1861) -> 5வது உறுப்பினர் (1909)"),
            ("D", "4 Executive Members (1773) -> 1st Indian Member (1833) -> 4th Law Member (1861) -> 5th Member (1909)", "4 நிர்வாக உறுப்பினர்கள் (1773) -> 1வது இந்திய உறுப்பினர் (1833) -> 4வது சட்ட உறுப்பினர் (1861) -> 5வது உறுப்பினர் (1909)")
        ],
        "A",
        "Historical Context: The Viceroy's Executive Council evolved continuously from a small governing body to a specialized cabinet.\nReason: 1773 created 4-member council $\rightarrow$ 1833 added Lord Macaulay as 4th Law Member $\rightarrow$ 1861 added 5th member (Finance - James Wilson) and statutorily recognized Lord Canning's Portfolio System $\rightarrow$ 1909 appointed Satyendra Prasad Sinha as the first Indian member (Law Member).\nConstitutional Impact: Laid the framework for Cabinet ministry system in post-independence India.\nExam Trap: Lord Macaulay was 4th Law Member (1833); S.P. Sinha was 1st Indian Law Member (1909).\nMemory Trick: 1773 (4) $\rightarrow$ 1833 (+Law) $\rightarrow$ 1861 (+Portfolio) $\rightarrow$ 1909 (+Indian).",
        "வரலாற்றுப் பின்னணி: வைஸ்ராயின் நிர்வாகக் குழு சிறிய அமைப்பிலிருந்து ஒரு சிறப்பார்ந்த அமைச்சரவையாகப் படிப்படியாக வளர்ந்தது.\nகாரணம்: 1773-ல் 4 உறுப்பினர்கள் $\rightarrow$ 1833-ல் மெக்காலே 4வது சட்ட உறுப்பினராகச் சேர்க்கப்பட்டார் $\rightarrow$ 1861-ல் 5வது உறுப்பினர் சேர்க்கப்பட்டு லார்டு கேனிங்கின் இலாகா முறை சட்டப்பூர்வமாக்கப்பட்டது $\rightarrow$ 1909-ல் சத்யேந்திர பிரசாத் சின்கா முதல் இந்திய உறுப்பினராக நியமிக்கப்பட்டார்.\nஅரசியலமைப்பு தாக்கம்: சுதந்திர இந்தியாவின் அமைச்சரவை முறைக்கு சட்டப்பூர்வ சட்டகத்தை அமைத்தது.\nதேர்வுப் பொறி: லார்டு மெக்காலே 4வது சட்ட உறுப்பினர் (1833); எஸ்.பி. சின்கா வைஸ்ராய் குழுவின் 1வது இந்திய சட்ட உறுப்பினர் (1909).\nநினைவுச் சூத்திரம்: 1773 (4) $\rightarrow$ 1833 (+சட்டம்) $\rightarrow$ 1861 (+இலாகா) $\rightarrow$ 1909 (+இந்தியர்).",
        {
            "A": {"en": "Correct sequence mapping Executive Council expansion across four major Acts.", "ta": "சரி. நான்கு சட்டங்களில் நிர்வாகக் குழு விரிவாக்கத்தின் சரியான வரிசை."},
            "B": {"en": "Incorrect. 4th Law Member was added in 1833, not 1773.", "ta": "தவறு. 4வது சட்ட உறுப்பினர் 1833-ல் சேர்க்கப்பட்டார்."},
            "C": {"en": "Incorrect. First Indian member joined in 1909, not 1773.", "ta": "தவறு. முதல் இந்திய உறுப்பினர் 1909-ல் சேர்ந்தார்."},
            "D": {"en": "Incorrect. First Indian member joined in 1909, not 1833.", "ta": "தவறு. முதல் இந்திய உறுப்பினர் 1909-ல் சேர்ந்தார்."}
        },
        "TNPSC Trap: Lord Canning introduced Portfolio system in 1859, but statutory recognition was given by Indian Councils Act 1861.",
        "TNPSC பொறி: லார்டு கேனிங் இலாகா முறையை 1859-ல் அறிமுகப்படுத்தினார், ஆனால் 1861 சட்டமே அதற்குச் சட்டப்பூர்வ அங்கீகாரம் அளித்தது.",
        "S.P. Sinha (Satyendra Prasad Sinha) was the first Indian to join the Viceroy's Executive Council as Law Member.",
        "எஸ்.பி. சின்கா வைஸ்ராயின் நிர்வாகக் குழுவில் சட்ட உறுப்பினராகச் சேர்ந்த முதல் இந்தியராவார்.",
        ["Polity", "Historical Background", "Executive Council Evolution", "Multi-Act Integration", "Grand Test"], "Evaluate", 90
    ))

    # Q8: Direct MCQ - Medium - Amending Act 1781
    questions.append(make_q(
        8, "Medium", "Direct MCQ",
        "The Amending Act of 1781 (Act of Settlement) exempted which of the following officials from the jurisdiction of the Supreme Court for acts performed in their official capacity?",
        "1781 ஆம் ஆண்டின் திருத்தச் சட்டம் (சீர்முறைச் சட்டம்) பின்வரும் எந்த அதிகாரிகளை அவர்தம் அதிகாரப்பூர்வ பணியின் காரணமாக உச்ச நீதிமன்ற அதிகார வரம்பிலிருந்து விலக்கியது?",
        [
            ("A", "Governor-General and Council members only", "கவர்னர்-ஜெனரல் மற்றும் கவுன்சில் உறுப்பினர்கள் மட்டுமே"),
            ("B", "Servants of the East India Company only", "கிழக்கிந்திய கம்பெனி ஊழியர்கள் மட்டுமே"),
            ("C", "Both Governor-General in Council and Servants of the Company for official acts", "அதிகாரப்பூர்வ பணிகளுக்காக கவர்னர்-ஜெனரல் கவுன்சில் மற்றும் கம்பெனி ஊழியர்கள் இருசாரரும்"),
            ("D", "Judges of the Supreme Court only", "உச்ச நீதிமன்ற நீதிபதிகள் மட்டுமே")
        ],
        "C",
        "Historical Context: Enacted to remedy the defects of the Regulating Act of 1773 and resolve conflicts between the Supreme Court and Governor-General in Council.\nReason: It exempted both the Governor-General in Council and Company servants from Supreme Court jurisdiction for official actions, and excluded revenue matters from Supreme Court jurisdiction.\nConstitutional Impact: Clarified executive vs judicial boundaries in early British administration.\nExam Trap: Supreme Court jurisdiction was narrowed, not abolished.\nMemory Trick: 1781 Act of Settlement = Revenue & Official Immunity.",
        "வரலாற்றுப் பின்னணி: 1773 ஒழுங்குமுறைச் சட்டத்தின் குறைபாடுகளை நிவர்த்தி செய்யவும் உச்ச நீதிமன்றம் - கவர்னர்-ஜெனரல் கவுன்சில் மோதலைத் தீர்க்கவும் இயற்றப்பட்டது.\nகாரணம்: இது கவர்னர்-ஜெனரல் கவுன்சில் மற்றும் கம்பெனி ஊழியர்களுக்கு அதிகாரப்பூர்வ பணிகளுக்காக உச்ச நீதிமன்ற வரம்பிலிருந்து விலக்களித்ததுடன் வருவாய் விவகாரங்களையும் விலக்கியது.\nஅரசியலமைப்பு தாக்கம்: ஆரம்பகால பிரிட்டிஷ் நிர்வாகத்தில் நிர்வாக-நீதித்துறை எல்லைகளைத் தெளிவுபடுத்தியது.\nதேர்வுப் பொறி: உச்ச நீதிமன்ற வரம்பு சுருக்கப்பட்டது, முற்றிலும் ஒழிக்கப்படவில்லை.\nநினைவுச் சூத்திரம்: 1781 சீர்முறைச் சட்டம் = வருவாய் & அதிகாரப்பூர்வ விலக்கு.",
        {
            "A": {"en": "Incorrect. Company servants were also exempted for official actions.", "ta": "தவறு. கம்பெனி ஊழியர்களுக்கும் அதிகாரப்பூர்வ பணிக்கு விலக்களிக்கப்பட்டது."},
            "B": {"en": "Incorrect. Governor-General and Council were also exempted.", "ta": "தவறு. கவர்னர்-ஜெனரல் மற்றும் கவுன்சிலுக்கும் விலக்களிக்கப்பட்டது."},
            "C": {"en": "Correct. Exempted both GG-in-Council and Company servants for official acts.", "ta": "சரி. அதிகாரப்பூர்வ பணிகளுக்காக இருசாரருக்கும் விலக்களித்தது."},
            "D": {"en": "Incorrect. Judges were not exempted from judicial duty.", "ta": "தவறு. நீதிபதிகளுக்கு விலக்களிக்கப்படவில்லை."}
        },
        "TNPSC Trap: 1781 Act also required Supreme Court to administer personal laws (Hindu law for Hindus, Mohammedan law for Muslims).",
        "TNPSC பொறி: 1781 சட்டம் எதிராளியின் தனிநபர் சட்டப்படி (இந்துக்களுக்கு இந்து சட்டம், முஸ்லிம்களுக்கு முகமதிய சட்டம்) தீர்ப்பு வழங்க ஆணையிட்டது.",
        "Amending Act 1781 is officially known as the 'Act of Settlement'.",
        "1781 திருத்தச் சட்டம் அதிகாரப்பூர்வமாக 'சீர்முறைச் சட்டம்' (Act of Settlement) என அழைக்கப்படுகிறது.",
        ["Polity", "Historical Background", "Act of Settlement 1781", "Grand Test"], "Understand", 60
    ))

    # Q9: Conceptual MCQ - Hard - Government of India Act 1858
    questions.append(make_q(
        9, "Hard", "Conceptual MCQ",
        "What was the exact statutory character and institutional status of the 'Council of India' established under the Government of India Act 1858?",
        "1858 இந்திய அரசுச் சட்டத்தின் கீழ் நிறுவப்பட்ட 'இந்தியக் குழுவின்' (Council of India) துல்லியமான சட்டப்பூர்வத் தன்மை மற்றும் நிறுவன அந்தஸ்து யாது?",
        [
            ("A", "A 15-member advisory body based in London, chaired by the Secretary of State for India", "இந்திய அரசுச் செயலரைத் தலைவராகக் கொண்டு லண்டனில் இயங்கிய 15 உறுப்பினர்களைக் கொண்ட ஆலோசனைக் குழு"),
            ("B", "A sovereign legislative assembly elected by provincial councils in Calcutta", "கொல்கத்தாவில் மாகாணக் குழுக்களால் தேர்ந்தெடுக்கப்பட்ட ஒரு இறையாண்மை கொண்ட சட்டமன்ற அமைப்பு"),
            ("C", "A 6-member executive cabinet operating exclusively within British India", "பிரிட்டிஷ் இந்தியாவிற்குள் மட்டும் செயல்பட்ட 6 உறுப்பினர்களைக் கொண்ட நிர்வாக அமைச்சரவை"),
            ("D", "A judicial tribunal hearing final appeals against Indian High Courts", "இந்திய உயர் நீதிமன்றங்களுக்கு எதிரான மேல்முறையீடுகளை விசாரிக்கும் இறுதி நீதித் தீர்ப்பாயம்")
        ],
        "A",
        "Historical Context: The 1858 Act ended Company Rule and established direct governance by the British Crown.\nReason: It created a 15-member Council of India in London to assist the Secretary of State for India (a British Cabinet minister). The Council was purely advisory, with the Secretary of State as its Chairman.\nConstitutional Impact: Replaced Board of Control and Court of Directors with a centralized office in London.\nExam Trap: 8 members were nominated by the Crown, and 7 were elected by the Court of Directors.\nMemory Trick: 1858 Council of India = 15 members in London chaired by SOS.",
        "வரலாற்றுப் பின்னணி: 1858 சட்டம் கம்பெனி ஆட்சியை முடிவுக்குக் கொண்டுவந்து பிரிட்டிஷ் முடியாட்சியின் நேரடி ஆட்சியை நிறுவியது.\nகாரணம்: இது லண்டனில் இந்திய அரசுச் செயலருக்கு (பிரிட்டிஷ் கேபினட் அமைச்சர்) உதவ 15 உறுப்பினர்களைக் கொண்ட இந்தியக் குழுவை உருவாக்கியது. இக்குழு ஆலோசனைக் அமைப்பாகும், அரசுச் செயலர் இதன் தலைவராவார்.\nஅரசியலமைப்பு தாக்கம்: கட்டுப்பாட்டு வாரியம் மற்றும் இயக்குநர்கள் அவையை லண்டனில் உள்ள ஒரே அலுவலகமாக மாற்றியது.\nதேர்வுப் பொறி: 15 உறுப்பினர்களில் 8 பேரை பிரிட்டிஷ் முடி ஆட்சியும் 7 பேரை இயக்குநர்கள் அவையும் தேர்வு செய்தன.\nநினைவுச் சூத்திரம்: 1858 இந்தியக் குழு = லண்டனில் 15 உறுப்பினர்கள், அரசுச் செயலர் தலைவர்.",
        {
            "A": {"en": "Correct. 15-member advisory body chaired by Secretary of State for India in London.", "ta": "சரி. லண்டனில் இயங்கிய அரசுச் செயலரைத் தலைவராகக் கொண்ட 15 உறுப்பினர் ஆலோசனைக் குழு."},
            "B": {"en": "Incorrect. It was an advisory body based in London, not an elected assembly in Calcutta.", "ta": "தவறு. இது லண்டனில் இயங்கிய ஆலோசனைக் குழு, கொல்கத்தாவில் உள்ள சட்டமன்றமல்ல."},
            "C": {"en": "Incorrect. Council of India had 15 members, based in London.", "ta": "தவறு. இந்தியக் குழு லண்டனில் 15 உறுப்பினர்களைக் கொண்டிருந்தது."},
            "D": {"en": "Incorrect. Judicial appeals went to the Privy Council.", "ta": "தவறு. நீதித்துறை மேல்முறையீடுகள் ப்ரிவி கவுன்சிலுக்குச் சென்றன."}
        },
        "TNPSC Trap: Council of India was created in 1858 and later abolished by the Government of India Act 1935.",
        "TNPSC பொறி: இந்தியக் குழு 1858-ல் உருவாக்கப்பட்டு, பின்னர் 1935 இந்திய அரசுச் சட்டத்தால் ஒழிக்கப்பட்டது.",
        "Secretary of State for India was a member of the British Cabinet and responsible to British Parliament.",
        "இந்திய அரசுச் செயலர் பிரிட்டிஷ் கேபினட் உறுப்பினராவார்; பிரிட்டிஷ் நாடாளுமன்றத்திற்குப் பொறுப்பானவராவார்.",
        ["Polity", "Historical Background", "GOI Act 1858", "Council of India", "Grand Test"], "Analyze", 75
    ))

    # Q10: Statement Based - Medium - Indian Councils Act 1861
    questions.append(make_q(
        10, "Medium", "Statement Based",
        "Consider the following statements regarding the Indian Councils Act of 1861:\n1. It initiated legislative decentralization by restoring law-making powers to Bombay and Madras Presidencies.\n2. It empowered the Viceroy to issue Ordinances during emergencies without council concurrence, valid for six months.\n3. It introduced an official majority of elected Indian members in the Central Legislative Council.\nWhich of the statements given above is/are correct?",
        "1861 ஆம் ஆண்டின் இந்தியக் கவுன்சில்கள் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது பம்பாய் மற்றும் மதராஸ் மாகாணங்களுக்கு சட்ட அதிகாரங்களை மீட்டளிப்பதன் மூலம் அதிகாரப் பரவலாக்கத்தைத் தொடங்கியது.\n2. இது அவசர காலத்தில் மேலவையின் ஒப்புதலின்றி 6 மாத ஆயுட்காலம் கொண்ட அவசரச் சட்டங்களை பிறப்பிக்க வைஸ்ராய்க்கு அதிகாரமளித்தது.\n3. இது மத்திய சட்ட மேலவையில் தேர்ந்தெடுக்கப்பட்ட இந்திய உறுப்பினர்களின் அதிகாரப்பூர்வ பெரும்பான்மையை அறிமுகப்படுத்தியது.\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானவை?",
        [
            ("A", "1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
            ("B", "2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
            ("C", "1 and 3 only", "1 மற்றும் 3 மட்டுமே"),
            ("D", "1, 2 and 3", "1, 2 மற்றும் 3")
        ],
        "A",
        "Historical Context: The 1861 Act was the first step toward associate Indian representation and legislative devolution after 1857.\nReason: Statements 1 and 2 are correct. Statement 3 is incorrect because Indians were nominated as non-official members (Raja of Benaras, Maharaja of Patiala, Sir Dinkar Rao in 1862), but the Council retained an OFFICIAL majority.\nConstitutional Impact: Reversed the centralizing trend initiated by 1773 and completed by 1833.\nExam Trap: Non-official members were nominated, not elected, in 1861.\nMemory Trick: 1861 = Decentralization + Ordinance (6 months) + Nominated Indians.",
        "வரலாற்றுப் பின்னணி: 1857 கிளர்ச்சிக்குப் பிறகு இந்தியர்களை நிர்வாகத்தில் இணைக்கவும் அதிகாரப் பரவலாக்கத்திற்கும் 1861 சட்டம் வழிவகுத்தது.\nகாரணம்: கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் இந்தியர்கள் அதிகாரப்பூர்வமற்ற உறுப்பினர்களாக நியமிக்கப்பட்டனரே தவிரத் தேர்ந்தெடுக்கப்படவில்லை, மேலும் அதிகாரப்பூர்வ பெரும்பான்மையே தொடர்ந்தது.\nஅரசியலமைப்பு தாக்கம்: 1773-ல் தொடங்கி 1833-ல் உச்சமடைந்த அதிகார மையமாக்கல் போக்கைத் தலைகீழாக மாற்றியது.\nதேர்வுப் பொறி: 1861-ல் அதிகாரப்பூர்வமற்ற உறுப்பினர்கள் நியமிக்கப்பட்டனர், தேர்ந்தெடுக்கப்படவில்லை.\nநினைவுச் சூத்திரம்: 1861 = அதிகாரப் பரவலாக்கம் + அவசரச் சட்டம் (6 மாதம்) + நியமன இந்தியர்கள்.",
        {
            "A": {"en": "Correct. Statements 1 and 2 are true; Statement 3 is false as members were nominated non-officials.", "ta": "சரி. கூற்றுகள் 1 மற்றும் 2 சரி; உறுப்பினர்கள் நியமிக்கப்பட்டதால் கூற்று 3 தவறு."},
            "B": {"en": "Incorrect. Statement 3 is false.", "ta": "தவறு. கூற்று 3 தவறானது."},
            "C": {"en": "Incorrect. Statement 3 is false.", "ta": "தவறு. கூற்று 3 தவறானது."},
            "D": {"en": "Incorrect. Statement 3 is false.", "ta": "தவறு. கூற்று 3 தவறானது."}
        },
        "TNPSC Trap: Viceroy Lord Canning nominated 3 Indians to Central Legislative Council in 1862: Raja of Benaras, Maharaja of Patiala, Sir Dinkar Rao.",
        "TNPSC பொறி: 1862-ல் வைஸ்ராய் லார்டு கேனிங் 3 இந்தியர்களை மேலவைக்கு நியமித்தார்: பெனாரஸ் ராஜா, பட்டியாலா மகாராஜா, சர் தினகர் ராவ்.",
        "Ordinance-making power of Viceroy under 1861 Act had a statutory validity of 6 months.",
        "1861 சட்டத்தின் கீழ் வைஸ்ராய் பிறப்பிக்கும் அவசரச் சட்டத்திற்கு 6 மாத சட்டப்பூர்வ ஆயுள் இருந்தது.",
        ["Polity", "Historical Background", "Indian Councils Act 1861", "Grand Test"], "Analyze", 75
    ))

    # Q11: Conceptual MCQ - Medium - Charter Act 1813 vs 1833
    questions.append(make_q(
        11, "Medium", "Multi-Act Comparative",
        "Which distinction accurately captures the change in East India Company's trade monopoly between the Charter Act of 1813 and the Charter Act of 1833?",
        "1813 சாசனச் சட்டம் மற்றும் 1833 சாசனச் சட்டத்திற்கு இடையே கிழக்கிந்திய கம்பெனியின் வர்த்தக முற்றுரிமையில் ஏற்பட்ட மாற்றத்தைத் துல்லியமாக வேறுபடுத்திக் காட்டும் கூற்று எது?",
        [
            ("A", "The 1813 Act abolished trade monopoly except for tea and trade with China, whereas the 1833 Act abolished all commercial monopolies completely.", "1813 சட்டம் தேயிலை, சீனா வர்த்தகம் தவிர்த்து முற்றுரிமையை ஒழித்தது; ஆனால் 1833 சட்டம் அனைத்து வணிக முற்றுரிமைகளையும் முற்றிலும் ஒழித்தது."),
            ("B", "The 1813 Act ended trade with China, while the 1833 Act restored the tea trade monopoly.", "1813 சட்டம் சீனாவுடனான வர்த்தகத்தை முடித்தது; ஆனால் 1833 சட்டம் தேயிலை வர்த்தக முற்றுரிமையை மீட்டெடுத்தது."),
            ("C", "The 1813 Act granted total freedom of trade to all European nations, while the 1833 Act restricted it strictly to British subjects.", "1813 சட்டம் அனைத்து ஐரோப்பிய நாடுகளுக்கும் முழு வர்த்தக சுதந்திரத்தை அளித்தது; ஆனால் 1833 சட்டம் அதை பிரிட்டிஷாருக்கு மட்டும் சுருக்கியது."),
            ("D", "The 1813 Act abolished salt monopoly, while the 1833 Act abolished opium monopoly.", "1813 சட்டம் உப்பு முற்றுரிமையை ஒழித்தது; 1833 சட்டம் அபின் முற்றுரிமையை ஒழித்தது.")
        ],
        "A",
        "Historical Context: Industrial Revolution in Britain demanded free market access to British manufacturers.\nReason: Charter Act 1813 ended EIC monopoly in India except for tea trade and trade with China. Charter Act 1833 ended even these exceptions, turning EIC into a purely administrative body.\nConstitutional Impact: Complete commercial transformation of EIC into an administrative agent of Crown.\nExam Trap: Do not reverse the two Acts (1813 = Partial end; 1833 = Total end).\nMemory Trick: 1813 = Tea & China left; 1833 = All commercial trade gone.",
        "வரலாற்றுப் பின்னணி: பிரிட்டிஷ் தொழில் புரட்சி காரணமாக பிரிட்டிஷ் உற்பத்தியாளர்களுக்கு சுதந்திர சந்தை தேவைப்பட்டது.\nகாரணம்: 1813 சாசனச் சட்டம் தேயிலை மற்றும் சீனா வர்த்தகம் தவிர கம்பெனி முற்றுரிமையை முடித்தது. 1833 சாசனச் சட்டம் அந்த விலக்குகளையும் ஒழித்து கம்பெனியை முழு நிர்வாக அமைப்பாக மாற்றியது.\nஅரசியலமைப்பு தாக்கம்: கிழக்கிந்திய கம்பெனி வணிக அமைப்பிலிருந்து முற்றிலும் பிரிட்டிஷ் முடியின் நிர்வாக முகவராக மாறியது.\nதேர்வுப் பொறி: இரண்டு சட்டங்களையும் தலைகீழாக மாற்றிவிட வேண்டாம் (1813 = பகுதி முடிவு; 1833 = முழு முடிவு).\nநினைவுச் சூத்திரம்: 1813 = தேயிலை, சீனா மிச்சம்; 1833 = அனைத்து வர்த்தகமும் காலி.",
        {
            "A": {"en": "Correct. 1813 ended monopoly except tea & China; 1833 ended all trade monopoly.", "ta": "சரி. 1813 தேயிலை, சீனா தவிர ஒழித்தது; 1833 அனைத்து வர்த்தகத்தையும் ஒழித்தது."},
            "B": {"en": "Incorrect. 1833 ended tea and China trade monopoly, did not restore it.", "ta": "தவறு. 1833 தேயிலை, சீனா வர்த்தகத்தை முடித்தது, மீட்டெடுக்கவில்லை."},
            "C": {"en": "Incorrect. Trade was opened to British merchants, not all European nations.", "ta": "தவறு. வர்த்தகம் பிரிட்டிஷ் வணிகர்களுக்கே திறக்கப்பட்டது."},
            "D": {"en": "Incorrect. Salt and opium were government revenue monopolies, not charter trade clauses.", "ta": "தவறு. உப்பும் அபினும் அரசாங்க வருவாய் விவகாரங்கள்."}
        },
        "TNPSC Trap: Charter Act 1813 allocated Rs. 1 Lakh annually for the promotion of education in India.",
        "TNPSC பொறி: 1813 சாசனச் சட்டம் இந்தியாவில் கல்வி வளர்ச்சிக்கு ஆண்டிற்கு 1 லட்சம் ரூபாய் ஒதுக்கியது.",
        "1833 Act made East India Company a purely administrative body.",
        "1833 சட்டம் கிழக்கிந்திய கம்பெனியை முற்றிலும் ஒரு நிர்வாக அமைப்பாக மாற்றியது.",
        ["Polity", "Historical Background", "Charter Act 1813", "Charter Act 1833", "Grand Test"], "Understand", 60
    ))

    # Q12: Direct MCQ - Medium - Charter Act 1793
    questions.append(make_q(
        12, "Medium", "Direct MCQ",
        "Which specific provision regarding administrative finance was mandated by the Charter Act of 1793?",
        "1793 ஆம் ஆண்டின் சாசனச் சட்டத்தால் நிர்வாக நிதி தொடர்பாக ஆணையிடப்பட்ட குறிப்பிட்ட விதி எது?",
        [
            ("A", "Salaries of the members of the Board of Control and their staff were to be paid out of Indian revenues.", "கட்டுப்பாட்டு வாரிய உறுப்பினர்கள் மற்றும் பணியாளர்களின் சம்பளம் இந்திய வருவாயிலிருந்தே வழங்கப்பட வேண்டும்."),
            ("B", "Creation of a separate Indian Treasury managed directly by the British Parliament.", "பிரிட்டிஷ் நாடாளுமன்றத்தால் நேரடியாக நிர்வகிக்கப்படும் தனி இந்திய கருவூலத்தை உருவாக்குதல்."),
            ("C", "Abolition of all internal customs duties across Bengal, Bombay, and Madras.", "வங்காளம், பம்பாய், மதராஸ் முழுவதும் அனைத்து உள்நாட்டு சுங்க வரிகளையும் ஒழித்தல்."),
            ("D", "Direct taxation powers granted to Provincial Legislative Councils.", "மாகாண சட்ட மேலவைகளுக்கு நேரடி வரி விதிக்கும் அதிகாரங்களை வழங்குதல்.")
        ],
        "A",
        "Historical Context: The 1793 Act extended the commercial charter of the EIC for another 20 years.\nReason: It stipulated that the members of the Board of Control and their staff were henceforth to be paid out of the Indian revenues. This practice continued until 1919.\nConstitutional Impact: Initiated the financial drain of Indian revenues for home administration in London.\nExam Trap: Board of Control was created in 1784, but payment from Indian revenues started in 1793.\nMemory Trick: 1793 = Board of Control paid from Indian Revenue.",
        "வரலாற்றுப் பின்னணி: 1793 சட்டம் கிழக்கிந்திய கம்பெனியின் வர்த்தக சாசனத்தை மேலும் 20 ஆண்டுகளுக்கு நீட்டித்தது.\nகாரணம்: கட்டுப்பாட்டு வாரிய உறுப்பினர்கள் மற்றும் பணியாளர்களின் சம்பளம் இனி இந்திய வருவாயிலிருந்தே வழங்கப்பட வேண்டும் என இது விதித்தது. இம்முறை 1919 வரை நீடித்தது.\nஅரசியலமைப்பு தாக்கம்: லண்டனில் உள்ள முகமைக்கான நிதிச் சுமையை இந்திய வருவாயின் மீது சுமத்தியது.\nதேர்வுப் பொறி: கட்டுப்பாட்டு வாரியம் 1784-ல் உருவாக்கப்பட்டது, ஆனால் இந்திய வருவாயிலிருந்து சம்பளம் 1793-ல் தொடங்கியது.\nநினைவுச் சூத்திரம்: 1793 = கட்டுப்பாட்டு வாரிய சம்பளம் இந்திய வருவாயில்.",
        {
            "A": {"en": "Correct. 1793 Charter Act made Board of Control salaries chargeable on Indian revenues.", "ta": "சரி. 1793 சாசனச் சட்டம் கட்டுப்பாட்டு வாரிய சம்பளத்தை இந்திய வருவாயில் சுமத்தியது."},
            "B": {"en": "Incorrect. No separate treasury managed by British Parliament was established.", "ta": "தவறு. பிரிட்டிஷ் நாடாளுமன்ற கருவூலம் எதுவும் உருவாக்கப்படவில்லை."},
            "C": {"en": "Incorrect. Customs duties were reorganized by internal administrative orders later.", "ta": "தவறு. சுங்க வரிகள் பின்னர் நிர்வாக உத்தரவுகளால் சீரமைக்கப்பட்டன."},
            "D": {"en": "Incorrect. Provincial Legislative Councils did not exist in 1793.", "ta": "தவறு. 1793-ல் மாகாண சட்ட மேலவைகள் இருக்கவில்லை."}
        },
        "TNPSC Trap: Salaries of Board of Control were charged on Indian revenue from 1793 to 1919, when the 1919 Act changed Secretary of State payment to British exchequer.",
        "TNPSC பொறி: 1793 முதல் 1919 வரை இந்திய வருவாயில் செலுத்தப்பட்ட இச்சம்பளம் 1919 சட்டத்தால் பிரிட்டிஷ் கருவூலத்திற்கு மாற்றப்பட்டது.",
        "Charter Act 1793 gave Governor-General more powers to override his council.",
        "1793 சாசனச் சட்டம் கவர்னர்-ஜெனரலுக்குத் தனது கவுன்சிலின் முடிவை நிராகரிக்கும் கூடுதல் அதிகாரங்களை அளித்தது.",
        ["Polity", "Historical Background", "Charter Act 1793", "Board of Control", "Grand Test"], "Understand", 60
    ))

    # Q13: Integrated PYQ Style - Hard - Evolution of Legislative Franchise & Budget
    questions.append(make_q(
        13, "Hard", "Integrated PYQ Style",
        "Trace the evolutionary expansion of legislative budget powers granted to Indian representatives across 1892, 1909, and 1919 Acts:",
        "1892, 1909 மற்றும் 1919 சட்டங்கள் வழியாக இந்தியப் பிரதிநிதிகளுக்கு வழங்கப்பட்ட சட்டமன்ற வரவு-செலவு (பட்ஜெட்) அதிகாரங்களின் படிமுறை வளர்ச்சியை ஆராய்க:",
        [
            ("A", "Right to discuss budget without voting (1892) -> Right to ask supplementary questions & move resolutions on budget (1909) -> Separation of Provincial Budget from Central Budget & voting on demand for grants (1919)", "பட்ஜெட்டை வாக்களிக்காமல் விவாதிக்கும் உரிமை (1892) -> துணைக்கேன்விகள் கேட்கவும் தீர்மானம் கொண்டுவரவும் உரிமை (1909) -> மாகாண பட்ஜெட்டை மத்திய பட்ஜெட்டிலிருந்து பிரித்தல் & மானியக் கோரிக்கைகளுக்கு வாக்களித்தல் (1919)"),
            ("B", "Right to vote on budget (1892) -> Right to discuss budget (1909) -> Total voting control over all budget heads (1919)", "பட்ஜெட்டிற்கு வாக்களிக்கும் உரிமை (1892) -> பட்ஜெட்டை விவாதிக்கும் உரிமை (1909) -> அனைத்து பட்ஜெட் தலைப்புகளிலும் முழு வாக்களிப்பு (1919)"),
            ("C", "Right to ask supplementary questions (1892) -> Right to discuss budget (1909) -> Direct taxation control (1919)", "துணைக்கேள்விகள் கேட்கும் உரிமை (1892) -> பட்ஜெட்டை விவாதிக்கும் உரிமை (1909) -> நேரடி வரிவிதிப்புக் கட்டுப்பாடு (1919)"),
            ("D", "Separation of budgets (1892) -> Right to vote on grants (1909) -> Complete financial autonomy (1919)", "பட்ஜெட்டுகளைப் பிரித்தல் (1892) -> மானியங்களுக்கு வாக்களிக்கும் உரிமை (1909) -> முழு நிதி தன்னாட்சி (1919)")
        ],
        "A",
        "Historical Context: Budgetary rights were expanded in phases due to nationalist demands for financial control.\nReason: 1892 Act allowed discussion of budget and asking questions (no voting, no supplementary questions) $\rightarrow$ 1909 Act allowed asking supplementary questions and moving resolutions on budget $\rightarrow$ 1919 Act separated Provincial and Central budgets and allowed provincial legislatures to enact their own budgets.\nConstitutional Impact: Foundation of fiscal federalism and parliamentary financial control.\nExam Trap: Supplementary questions allowed in 1909; budget separation occurred in 1919.\nMemory Trick: 1892 (Discuss) $\rightarrow$ 1909 (Supplementary Qs) $\rightarrow$ 1919 (Separate Budget).",
        "வரலாற்றுப் பின்னணி: தேசியவாதிகளின் கோரிக்கையால் பட்ஜெட் மீதான உரிமைகள் கட்டம் கட்டமாக வழங்கப்பட்டன.\nகாரணம்: 1892 சட்டம் பட்ஜெட் விவாதம் மற்றும் கேள்வி கேட்கும் உரிமையை அளித்தது (வாக்களிப்போ துணைக்கேள்வியோ இல்லை) $\rightarrow$ 1909 சட்டம் துணைக்கேள்விகள் கேட்கவும் தீர்மானம் கொண்டுவரவும் அனுமதித்தது $\rightarrow$ 1919 சட்டம் மாகாண மற்றும் மத்திய பட்ஜெட்டுகளைப் பிரித்து மாகாணங்கள் சொந்த பட்ஜெட்டை இயற்ற வழிவகுத்தது.\nஅரசியலமைப்பு தாக்கம்: நிதி கூட்டாட்சி மற்றும் நாடாளுமன்ற நிதிக்கட்டுப்பாட்டின் அடித்தளம்.\nதேர்வுப் பொறி: 1909-ல் துணைக்கேள்விகள்; 1919-ல் மாகாண பட்ஜெட் பிரிப்பு.\nநினைவுச் சூத்திரம்: 1892 (விவாதம்) $\rightarrow$ 1909 (துணைக்கேள்வி) $\rightarrow$ 1919 (தனி பட்ஜெட்).",
        {
            "A": {"en": "Correct sequence of budget rights expansion across 1892, 1909, and 1919.", "ta": "சரி. 1892, 1909, 1919 சட்டங்களில் பட்ஜெட் உரிமைகள் விரிவாக்கத்தின் சரியான வரிசை."},
            "B": {"en": "Incorrect. Voting on budget was not allowed in 1892.", "ta": "தவறு. 1892-ல் பட்ஜெட்டிற்கு வாக்களிக்க அனுமதி இல்லை."},
            "C": {"en": "Incorrect. Supplementary questions were allowed in 1909, not 1892.", "ta": "தவறு. 1909-லேயே துணைக்கேள்விகள் அனுமதிக்கப்பட்டன."},
            "D": {"en": "Incorrect. Budget separation happened in 1919, not 1892.", "ta": "தவறு. பட்ஜெட் பிரிப்பு 1919-ல் நடந்தது."}
        },
        "TNPSC Trap: Indian Councils Act 1892 allowed questions on budget, but supplementary questions were granted only by Indian Councils Act 1909.",
        "TNPSC பொறி: 1892 சட்டம் கேள்விகள் கேட்க அனுமதித்தது, ஆனால் துணைக்கேள்விகள் கேட்கும் உரிமை 1909 சட்டத்திலேயே கிடைத்தது.",
        "Government of India Act 1919 separated Provincial Budget from the Central Budget for the first time.",
        "1919 இந்திய அரசுச் சட்டமே முதன்முறையாக மாகாண பட்ஜெட்டை மத்திய பட்ஜெட்டிலிருந்து பிரித்தது.",
        ["Polity", "Historical Background", "Budget Evolution", "Multi-Act Integration", "Grand Test"], "Analyze", 75
    ))

    # Q14: Statement Based - Hard - Indian Councils Act 1892
    questions.append(make_q(
        14, "Hard", "Statement Based",
        "Consider the following statements regarding the Indian Councils Act of 1892:\n1. It introduced an element of indirect election for non-official seats in both central and provincial legislative councils.\n2. The word 'election' was explicitly used throughout the text of the Act.\n3. Non-official members were nominated on the recommendation of specified bodies such as district boards, municipalities, and universities.\nWhich of the statements given above is/are correct?",
        "1892 ஆம் ஆண்டின் இந்தியக் கவுன்சில்கள் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது மத்திய மற்றும் மாகாண சட்ட மேலவைகளில் அதிகாரப்பூர்வமற்ற இடங்களுக்கு மறைமுகத் தேர்தல் கூறுகளை அறிமுகப்படுத்தியது.\n2. 'தேர்தல்' என்ற சொல் இச்சட்டத்தின் உரையில் வெளிப்படையாகப் பயன்படுத்தப்பட்டது.\n3. மாவட்ட வாரியங்கள், நகராட்சிகள், பல்கலைக்கழகங்கள் போன்ற குறிப்பிட்ட அமைப்புகளின் பரிந்துரையின் பேரில் அதிகாரப்பூர்வமற்ற உறுப்பினர்கள் நியமிக்கப்பட்டனர்.\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானவை?",
        [
            ("A", "1 and 3 only", "1 மற்றும் 3 மட்டுமே"),
            ("B", "1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
            ("C", "2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
            ("D", "1, 2 and 3", "1, 2 மற்றும் 3")
        ],
        "A",
        "Historical Context: The 1892 Act was enacted in response to Indian National Congress demands for expanded legislative councils.\nReason: Statements 1 and 3 are correct. Statement 2 is incorrect because the word 'election' was carefully avoided in the text of the Act; the process was officially described as 'nomination made on recommendation'.\nConstitutional Impact: Introduced the principle of representation in British India.\nExam Trap: Election principle was implicit, but the word 'election' was NOT used in the Act.\nMemory Trick: 1892 = Recommendation system (Indirect election without using the word 'election').",
        "வரலாற்றுப் பின்னணி: இந்திய தேசிய காங்கிரஸின் கோரிக்கைகளுக்கு பதிலளிக்கும் விதமாக 1892 சட்டம் இயற்றப்பட்டது.\nகாரணம்: கூற்றுகள் 1 மற்றும் 3 சரியானவை. கூற்று 2 தவறானது, ஏனெனில் 'தேர்தல்' என்ற சொல் சட்டத்தில் பயன்படுத்தப்படவில்லை; அது 'பரிந்துரையின் பேரில் நியமனம்' என்றே குறிப்பிடப்பட்டது.\nஅரசியலமைப்பு தாக்கம்: பிரிட்டிஷ் இந்தியாவில் பிரதிநிதித்துவக் கோட்பாட்டை அறிமுகப்படுத்தியது.\nதேர்வுப் பொறி: தேர்தல் கொள்கை இருந்தது, ஆனால் 'தேர்தல்' என்ற சொல் சட்டத்தில் இடம்பெறவில்லை.\nநினைவுச் சூத்திரம்: 1892 = பரிந்துரை முறை ('தேர்தல்' என்ற சொல்லில்லாத மறைமுகத் தேர்தல்).",
        {
            "A": {"en": "Correct. Statements 1 and 3 are true. Statement 2 is false as the word 'election' was avoided.", "ta": "சரி. கூற்றுகள் 1 மற்றும் 3 சரி. 'தேர்தல்' என்ற சொல் தவிர்க்கப்பட்டதால் கூற்று 2 தவறு."},
            "B": {"en": "Incorrect. Statement 2 is false.", "ta": "தவறு. கூற்று 2 தவறானது."},
            "C": {"en": "Incorrect. Statement 2 is false.", "ta": "தவறு. கூற்று 2 தவறானது."},
            "D": {"en": "Incorrect. Statement 2 is false.", "ta": "தவறு. கூற்று 2 தவறானது."}
        },
        "TNPSC Trap: Non-officials in Central Legislative Council were nominated by Viceroy on recommendation of Bengal Chamber of Commerce and Provincial Legislative Councils.",
        "TNPSC பொறி: மத்திய மேலவை உறுப்பினர்கள் வங்காள வர்த்தக சபை மற்றும் மாகாண மேலவைகளின் பரிந்துரையில் வைஸ்ராயால் நியமிக்கப்பட்டனர்.",
        "Indian Councils Act 1892 increased the number of additional (non-official) members in central and provincial legislative councils.",
        "1892 இந்தியக் கவுன்சில்கள் சட்டம் மத்திய மற்றும் மாகாண சட்ட மேலவைகளில் கூடுதல் (அதிகாரப்பூர்வமற்ற) உறுப்பினர்களின் எண்ணிக்கையை உயர்த்தியது.",
        ["Polity", "Historical Background", "Indian Councils Act 1892", "Election Principle", "Grand Test"], "Analyze", 75
    ))

    # Q15: Conceptual MCQ - Medium - Indian Councils Act 1909 (Morley-Minto)
    questions.append(make_q(
        15, "Medium", "Conceptual MCQ",
        "Which landmark provision of the Indian Councils Act of 1909 legally institutionalized communal representation in Indian politics?",
        "1909 ஆம் ஆண்டின் இந்தியக் கவுன்சில்கள் சட்டத்தின் எந்த முக்கிய விதி இந்திய அரசியலில் வகுப்புவாத பிரதிநிதித்துவத்தை சட்டப்பூர்வமாக நிறுவனப்படுத்தியது?",
        [
            ("A", "System of separate electorates for Muslims, wherein Muslim members were to be elected only by Muslim voters", "முஸ்லிம்களுக்கு தனித் தொகுதி முறை, இதன் மூலம் முஸ்லிம் உறுப்பினர்கள் முஸ்லிம் வாக்காளர்களால் மட்டுமே தேர்ந்தெடுக்கப்பட வேண்டும்"),
            ("B", "Reservation of seats for Depressed Classes in central legislature", "மத்திய சட்டமன்றத்தில் ஒடுக்கப்பட்ட வகுப்பினருக்கு இடஒதுக்கீடு"),
            ("C", "Creation of separate legislative chambers for Hindus and Muslims", "இந்துக்கள் மற்றும் முஸ்லிம்களுக்கு தனித்தனி சட்ட மேலவைகளை உருவாக்குதல்"),
            ("D", "Weightage system granting equal representation to all religious communities regardless of population", "மக்கள் தொகையைப் பொருட்படுத்தாமல் அனைத்து மத சமூகங்களுக்கும் சம பிரதிநிதித்துவம் அளிக்கும் முறை")
        ],
        "A",
        "Historical Context: Designed to divide nationalist unity by accepting Shimla Deputation (1906) demands led by Aga Khan.\nReason: The 1909 Act introduced a system of separate electorates for Muslims, where Muslim members were elected exclusively by Muslim voters. Lord Minto came to be known as the 'Father of Communal Electorate'.\nConstitutional Impact: Sowed the seeds of communal partition in India.\nExam Trap: Separate electorates were introduced for Muslims in 1909, and extended to Sikhs, Indian Christians, Anglo-Indians, and Europeans in 1919.\nMemory Trick: 1909 Morley-Minto = Separate Electorates for Muslims (Father of Communal Electorate = Minto).",
        "வரலாற்றுப் பின்னணி: ஆகா கான் தலைமையிலான சிம்லா தூதுக்குழுவின் (1906) கோரிக்கையை ஏற்று தேசிய ஒற்றுமையைப் பிளவுபடுத்த வடிவமைக்கப்பட்டது.\nகாரணம்: 1909 சட்டம் முஸ்லிம்களுக்குத் தனித் தொகுதி முறையை அறிமுகப்படுத்தியது, அதில் முஸ்லிம் உறுப்பினர்கள் முஸ்லிம்களால் மட்டுமே தேர்ந்தெடுக்கப்பட்டனர். லார்டு மிண்டோ 'வகுப்புவாத வாக்காளர் தொகுதியின் தந்தை' என அழைக்கப்பட்டார்.\nஅரசியலமைப்பு தாக்கம்: இந்தியாவில் மதச்சார்பு பிரிவினைவாத விதைகளை விதைத்தது.\nதேர்வுப் பொறி: முஸ்லிம்களுக்கு 1909-ல் தனித் தொகுதி; சீக்கியர், கிறிஸ்தவர், ஆங்கிலோ-இந்தியர், ஐரோப்பியருக்கு 1919-ல் விரிவாக்கம்.\nநினைவுச் சூத்திரம்: 1909 மோலி-மிண்டோ = முஸ்லிம்களுக்குத் தனித் தொகுதி (வகுப்புவாத தந்தை = மிண்டோ).",
        {
            "A": {"en": "Correct. Introduced separate electorate for Muslims, legalizing communalism.", "ta": "சரி. முஸ்லிம்களுக்குத் தனித் தொகுதியை அறிமுகப்படுத்தி வகுப்புவாதத்தைச் சட்டப்பூர்வமாக்கியது."},
            "B": {"en": "Incorrect. Depressed classes reservation was proposed under 1932 Communal Award / 1935 Act.", "ta": "தவறு. ஒடுக்கப்பட்ட வகுப்பினருக்கான ஒதுக்கீடு 1932 வகுப்புவாத கொடை / 1935 சட்டத்தில் வந்தது."},
            "C": {"en": "Incorrect. No separate legislative chambers were created.", "ta": "தவறு. தனி சட்ட மேலவைகள் உருவாக்கப்படவில்லை."},
            "D": {"en": "Incorrect. Weightage was given to Muslims, but not equal representation for all.", "ta": "தவறு. முஸ்லிம்களுக்கு கூடுதல் எடைக் காரணி அளிக்கப்பட்டது, அனைவருக்கும் சமமல்ல."}
        },
        "TNPSC Trap: Lord Minto was Viceroy and Lord Morley was Secretary of State for India in 1909.",
        "TNPSC பொறி: 1909-ல் லார்டு மிண்டோ வைஸ்ராயாகவும் லார்டு மோலி இந்திய அரசுச் செயலராகவும் இருந்தனர்.",
        "1909 Act allowed non-official majority in Provincial Legislative Councils, but retained official majority in Central Legislative Council.",
        "1909 சட்டம் மாகாண சட்ட மேலவைகளில் அதிகாரப்பூர்வமற்ற பெரும்பான்மையை அனுமதித்தது, ஆனால் மத்திய மேலவையில் அதிகாரப்பூர்வ பெரும்பான்மையை நீடித்தது.",
        ["Polity", "Historical Background", "Indian Councils Act 1909", "Morley Minto Reforms", "Grand Test"], "Understand", 60
    ))

    # Q16: Multi-Act Comparative - Hard - 1909 vs 1919 Separate Electorates Extension
    questions.append(make_q(
        16, "Hard", "Multi-Act Comparative",
        "Which comparative inference correctly tracks the extension of the principle of separate electorates between the Government of India Act 1909 and the Government of India Act 1919?",
        "1909 இந்திய அரசுச் சட்டம் மற்றும் 1919 இந்திய அரசுச் சட்டத்திற்கு இடையே தனித் தொகுதி கொள்கை விரிவாக்கப்பட்டதைச் சரியாகக் காட்டும் ஒப்பீட்டு முடிவு எது?",
        [
            ("A", "1909 Act introduced separate electorates exclusively for Muslims, while 1919 Act extended separate electorates to Sikhs, Indian Christians, Anglo-Indians, and Europeans.", "1909 சட்டம் முஸ்லிம்களுக்கு மட்டும் தனித் தொகுதியை அறிமுகப்படுத்தியது; ஆனால் 1919 சட்டம் அதை சீக்கியர்கள், இந்திய கிறிஸ்தவர்கள், ஆங்கிலோ-இந்தியர்கள், ஐரோப்பியர்களுக்கும் விரிவுபடுத்தியது."),
            ("B", "1909 Act introduced separate electorates for Sikhs, while 1919 Act extended it to Muslims and Depressed Classes.", "1909 சட்டம் சீக்கியர்களுக்குத் தனித் தொகுதியை அறிமுகப்படுத்தியது; 1919 சட்டம் அதை முஸ்லிம்களுக்கும் ஒடுக்கப்பட்ட வகுப்பினருக்கும் விரிவுபடுத்தியது."),
            ("C", "1909 Act granted separate electorates to all minorities, while 1919 Act abolished separate electorates in favor of joint electorates.", "1909 சட்டம் அனைத்து சிறுபான்மையினருக்கும் தனித் தொகுதி அளித்தது; 1919 சட்டம் அதை ஒழித்து கூட்டுக் தொகுதியைக் கொண்டுவந்தது."),
            ("D", "1909 Act restricted separate electorates to provincial councils, while 1919 Act restricted them to central legislature.", "1909 சட்டம் தனித் தொகுதியை மாகாணங்களுக்கு மட்டும் சுருக்கியது; 1919 சட்டம் அதை மத்திய சட்டமன்றத்திற்கு மட்டும் சுருக்கியது.")
        ],
        "A",
        "Historical Context: Communal representation was extended systematically by the British Crown to fragment multi-religious nationalist forces.\nReason: 1909 Act introduced separate electorates for Muslims. 1919 Act (Montagu-Chelmsford Reforms) extended separate electorates to 4 additional groups: Sikhs, Indian Christians, Anglo-Indians, and Europeans. (1935 Act further extended it to Depressed Classes, Women, and Labour).\nConstitutional Impact: Deepened communal divisions across multiple administrative strata.\nExam Trap: Depressed classes were included in Communal Award 1932 / 1935 Act, NOT 1919 Act.\nMemory Trick: 1909 = Muslims; 1919 = +Sikhs, Christians, Anglo-Indians, Europeans.",
        "வரலாற்றுப் பின்னணி: தேசிய சக்திகளைப் பிரிக்க பிரிட்டிஷ் அரசு வகுப்புவாத பிரதிநிதித்துவத்தை முறையே விரிவுபடுத்தியது.\nகாரணம்: 1909 சட்டம் முஸ்லிம்களுக்குத் தனித் தொகுதியைத் தந்தது. 1919 சட்டம் (மாண்டேகு-செம்ஸ்ஃபோர்டு) அதை 4 கூடுதல் குழுக்களுக்கு (சீக்கியர், இந்திய கிறிஸ்தவர், ஆங்கிலோ-இந்தியர், ஐரோப்பியர்) விரிவுபடுத்தியது. (1935 சட்டம் ஒடுக்கப்பட்ட வகுப்பினர், பெண்கள், தொழிலாளர்களுக்கு விரிவுபடுத்தியது).\nஅரசியலமைப்பு தாக்கம்: பல மட்டங்களில் வகுப்புவாதப் பிளவுகளை ஆழப்படுத்தியது.\nதேர்வுப் பொறி: ஒடுக்கப்பட்ட வகுப்பினர் 1932 வகுப்புவாத கொடை / 1935 சட்டத்தில் இணைக்கப்பட்டனர், 1919-ல் அல்ல.\nநினைவுச் சூத்திரம்: 1909 = முஸ்லிம்கள்; 1919 = +சீக்கியர், கிறிஸ்தவர், ஆங்கிலோ-இந்தியர், ஐரோப்பியர்.",
        {
            "A": {"en": "Correct. 1909 applied to Muslims; 1919 extended to Sikhs, Christians, Anglo-Indians, Europeans.", "ta": "சரி. 1909 முஸ்லிம்களுக்கு; 1919 சீக்கியர், கிறிஸ்தவர், ஆங்கிலோ-இந்தியர், ஐரோப்பியருக்கு விரிவுபடுத்தியது."},
            "B": {"en": "Incorrect. Muslims were granted separate electorates in 1909, not 1919.", "ta": "தவறு. முஸ்லிம்களுக்கு 1909-லேயே வழங்கப்பட்டது."},
            "C": {"en": "Incorrect. Neither Act abolished separate electorates.", "ta": "தவறு. எந்தச் சட்டமும் தனித் தொகுதியை ஒழிக்கவில்லை."},
            "D": {"en": "Incorrect. Separate electorates applied to both provincial and central levels.", "ta": "தவறு. தனித் தொகுதிகள் மாகாண மற்றும் மத்திய இரண்டு மட்டங்களிலும் இயங்கின."}
        },
        "TNPSC Trap: Government of India Act 1935 extended separate electorates further to Depressed Classes (Scheduled Castes), Women, and Labour (Workers).",
        "TNPSC பொறி: 1935 இந்திய அரசுச் சட்டம் தனித் தொகுதியை மேலும் ஒடுக்கப்பட்ட வகுப்பினர், பெண்கள் மற்றும் தொழிலாளர்களுக்கு விரிவுபடுத்தியது.",
        "1919 Act is known as Montagu-Chelmsford Reforms (Montagu = Secretary of State, Chelmsford = Viceroy).",
        "1919 சட்டம் மாண்டேகு-செம்ஸ்ஃபோர்டு சீர்திருத்தங்கள் என அழைக்கப்படுகிறது (மாண்டேகு = அரசுச் செயலர், செம்ஸ்ஃபோர்டு = வைஸ்ராய்).",
        ["Polity", "Historical Background", "GOI Act 1919", "GOI Act 1909", "Separate Electorates", "Grand Test"], "Analyze", 75
    ))

    # Q17: Statement Based - Hard - Government of India Act 1919 (Dyarchy)
    questions.append(make_q(
        17, "Hard", "Statement Based",
        "Consider the following statements regarding Dyarchy introduced under the Government of India Act of 1919:\n1. Provincial executive subjects were divided into two categories: 'Reserved' and 'Transferred'.\n2. 'Reserved' subjects were administered by the Governor and his Executive Council without being responsible to the provincial legislature.\n3. 'Transferred' subjects were administered by the Governor with the advice of Ministers responsible to the provincial legislature.\n4. Dyarchy was successfully implemented at both the Central and Provincial levels under the 1919 Act.\nWhich of the statements given above are correct?",
        "1919 இந்திய அரசுச் சட்டத்தின் கீழ் அறிமுகப்படுத்தப்பட்ட இரட்டை ஆட்சி பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. மாகாண நிர்வாகத் துறைகள் 'ஒதுக்கப்பட்டவை' மற்றும் 'மாற்றப்பட்டவை' என இரு பிரிவுகளாகப் பிரிக்கப்பட்டன.\n2. 'ஒதுக்கப்பட்ட' துறைகள் மாகாண சட்டமன்றத்திற்குப் பொறுப்பில்லாத கவர்னர் மற்றும் அவரது நிர்வாகக் குழுவால் நிர்வகிக்கப்பட்டன.\n3. 'மாற்றப்பட்ட' துறைகள் மாகாண சட்டமன்றத்திற்குப் பொறுப்பான அமைச்சர்களின் ஆலோசனையுடன் கவர்னரால் நிர்வகிக்கப்பட்டன.\n4. 1919 சட்டத்தின் கீழ் மத்திய மற்றும் மாகாண இரண்டு மட்டங்களிலும் இரட்டை ஆட்சி வெற்றிகரமாக அமல்படுத்தப்பட்டது.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
        [
            ("A", "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டுமே"),
            ("B", "1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
            ("C", "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டுமே"),
            ("D", "1, 3 and 4 only", "1, 3 மற்றும் 4 மட்டுமே")
        ],
        "A",
        "Historical Context: Dyarchy (rule of two) was introduced in provinces by the 1919 Act to grant limited responsible government.\nReason: Statements 1, 2, and 3 are correct. Statement 4 is incorrect because Dyarchy was introduced ONLY in the Provinces under the 1919 Act; it was NEVER introduced at the Center (1935 Act proposed central Dyarchy, but it never came into operation).\nConstitutional Impact: First experiment with ministerial responsibility at provincial level.\nExam Trap: Dyarchy in Provinces = 1919 Act. Dyarchy proposed at Center = 1935 Act.\nMemory Trick: 1919 Dyarchy = Provinces ONLY (Reserved = Governor+Council; Transferred = Governor+Ministers).",
        "வரலாற்றுப் பின்னணி: மாகாணங்களில் வரம்பிற்குட்பட்ட பொறுப்பு ஆட்சியை வழங்க 1919 சட்டம் இரட்டை ஆட்சியை அறிமுகப்படுத்தியது.\nகாரணம்: கூற்றுகள் 1, 2 மற்றும் 3 சரியானவை. கூற்று 4 தவறானது, ஏனெனில் 1919 சட்டத்தில் இரட்டை ஆட்சி மாகாணங்களில் மட்டுமே அறிமுகமானது; மத்தியில் அறிமுகமாகவில்லை (1935 சட்டம் மத்தியில் இரட்டை ஆட்சியை முன்மொழிந்தது, ஆனால் அது நடைமுறைக்கு வரவில்லை).\nஅரசியலமைப்பு தாக்கம்: மாகாண மட்டத்தில் அமைச்சரவைப் பொறுப்பு ஆட்சியின் முதல் பரிசோதனை.\nதேர்வுப் பொறி: மாகாண இரட்டை ஆட்சி = 1919 சட்டம். மத்திய இரட்டை ஆட்சி முன்மொழிவு = 1935 சட்டம்.\nநினைவுச் சூத்திரம்: 1919 இரட்டை ஆட்சி = மாகாணங்களில் மட்டும் (ஒதுக்கப்பட்டவை = கவர்னர்+கவுன்சில்; மாற்றப்பட்டவை = கவர்னர்+அமைச்சர்கள்).",
        {
            "A": {"en": "Correct. Statements 1, 2, and 3 are true. Statement 4 is false as Dyarchy was not at the Center.", "ta": "சரி. கூற்றுகள் 1, 2, 3 சரி. மத்தியில் இரட்டை ஆட்சி இல்லாததால் கூற்று 4 தவறு."},
            "B": {"en": "Incorrect. Statement 3 is also correct.", "ta": "தவறு. கூற்று 3-ம் சரியானது."},
            "C": {"en": "Incorrect. Statement 4 is false.", "ta": "தவறு. கூற்று 4 தவறானது."},
            "D": {"en": "Incorrect. Statement 4 is false.", "ta": "தவறு. கூற்று 4 தவறானது."}
        },
        "TNPSC Trap: Law & Order, Finance, Land Revenue were 'Reserved' subjects; Education, Health, Local Self-Government were 'Transferred' subjects.",
        "TNPSC பொறி: சட்டம் & ஒழுங்கு, நிதி, நில வருவாய் ஆகியவை 'ஒதுக்கப்பட்ட' துறைகள்; கல்வி, சுகாதாரம், உள்ளாட்சி ஆகியவை 'மாற்றப்பட்ட' துறைகள்.",
        "The term 'Dyarchy' is derived from the Greek word 'di-arche', meaning double rule.",
        "'இரட்டை ஆட்சி' (Dyarchy) என்ற சொல் 'di-arche' என்ற கிரேக்க சொல்லிலிருந்து உருவானது.",
        ["Polity", "Historical Background", "GOI Act 1919", "Dyarchy", "Grand Test"], "Analyze", 75
    ))

    # Q18: Direct MCQ - Easy - Central Bicameralism 1919
    questions.append(make_q(
        18, "Easy", "Direct MCQ",
        "Which statutory enactment introduced bicameralism and direct elections at the Central Legislative level in India for the first time?",
        "இந்தியாவில் முதன்முறையாக மத்திய சட்டமன்ற மட்டத்தில் இரு அவை முறை மற்றும் நேரடித் தேர்தல்களை அறிமுகப்படுத்திய சட்டப்பூர்வ சட்டம் எது?",
        [
            ("A", "Government of India Act of 1919", "1919 ஆம் ஆண்டின் இந்திய அரசுச் சட்டம்"),
            ("B", "Indian Councils Act of 1909", "1909 ஆம் ஆண்டின் இந்தியக் கவுன்சில்கள் சட்டம்"),
            ("C", "Government of India Act of 1935", "1935 ஆம் ஆண்டின் இந்திய அரசுச் சட்டம்"),
            ("D", "Indian Councils Act of 1892", "1892 ஆம் ஆண்டின் இந்தியக் கவுன்சில்கள் சட்டம்")
        ],
        "A",
        "Historical Context: Montagu-Chelmsford Reforms replaced the Indian Legislative Council with a bicameral central legislature.\nReason: GOI Act 1919 established the Council of State (Upper House) and the Central Legislative Assembly (Lower House), with a majority of members chosen by direct election.\nConstitutional Impact: Created the prototype of modern Parliament of India (Rajya Sabha and Lok Sabha).\nExam Trap: Bicameralism at Center = 1919 Act; Bicameralism in 6 Provinces = 1935 Act.\nMemory Trick: 1919 = Central Bicameralism + Direct Elections.",
        "வரலாற்றுப் பின்னணி: மாண்டேகு-செம்ஸ்ஃபோர்டு சீர்திருத்தங்கள் மத்திய சட்ட மேலவையை இரு அவைகளைக் கொண்ட மத்திய சட்டமன்றமாக மாற்றின.\nகாரணம்: 1919 இந்திய அரசுச் சட்டம் மாநிலங்கள் குழு (மேலவை) மற்றும் மத்திய சட்ட மேலவை (கீழவை) ஆகியவற்றை நிறுவி பெரும்பான்மை உறுப்பினர்களை நேரடித் தேர்தல் மூலம் தேர்வு செய்தது.\nஅரசியலமைப்பு தாக்கம்: நவீன இந்திய நாடாளுமன்றத்தின் (மாநிலங்களவை, மக்களவை) முன்மாதிரியை உருவாக்கியது.\nதேர்வுப் பொறி: மத்திய இரு அவை முறை = 1919 சட்டம்; 6 மாகாணங்களில் இரு அவை முறை = 1935 சட்டம்.\nநினைவுச் சூத்திரம்: 1919 = மத்திய இரு அவை முறை + நேரடித் தேர்தல்.",
        {
            "A": {"en": "Correct. 1919 Act created central bicameralism (Council of State & Legislative Assembly) and direct elections.", "ta": "சரி. 1919 சட்டம் மத்திய இரு அவை முறையையும் நேரடித் தேர்தலையும் உருவாக்கியது."},
            "B": {"en": "Incorrect. 1909 Act retained unicameral central council with indirect elements.", "ta": "தவறு. 1909 சட்டம் ஓரவை கொண்டதாகவே இருந்தது."},
            "C": {"en": "Incorrect. 1935 Act introduced bicameralism in 6 out of 11 provinces.", "ta": "தவறு. 1935 சட்டம் 6 மாகாணங்களில் இரு அவை முறையைக் கொண்டுவந்தது."},
            "D": {"en": "Incorrect. 1892 Act provided indirect recommendation system.", "ta": "தவறு. 1892 சட்டம் மறைமுகப் பரிந்துரை முறையைத் தந்தது."}
        },
        "TNPSC Trap: Franchise under 1919 Act was restricted based on property, tax, or educational qualifications (only about 10% of population).",
        "TNPSC பொறி: 1919 சட்டத்தின் கீழ் வாக்குரிமை சொத்து, வரி அல்லது கல்வித் தகுதி அடிப்படையில் வரம்பிற்குட்படுத்தப்பட்டது (மக்கள் தொகையில் 10% மட்டுமே).",
        "Council of State had 60 members and Legislative Assembly had 145 members under 1919 Act.",
        "1919 சட்டத்தின் கீழ் மாநிலங்கள் குழு 60 உறுப்பினர்களையும் சட்ட மேலவை 145 உறுப்பினர்களையும் கொண்டிருந்தன.",
        ["Polity", "Historical Background", "GOI Act 1919", "Bicameralism", "Grand Test"], "Remember", 45
    ))

    # Q19: Assertion & Reason - Medium - Simon Commission (1927)
    questions.append(make_q(
        19, "Medium", "Assertion & Reason",
        "Assertion (A): The Simon Commission, appointed in November 1927, was boycotted by all major political parties in India.\nReason (R): All seven members of the Indian Statutory Commission were British, and no Indian was included in the commission.",
        "கூற்று (A): நவம்பர் 1927-ல் நியமிக்கப்பட்ட சைமன் குழுவை இந்தியாவின் அனைத்து முக்கிய அரசியல் கட்சிகளும் புறக்கணித்தன.\nகாரணம் (R): இந்திய சட்டப்பூர்வ குழுவின் ஏழு உறுப்பினர்களும் பிரிட்டிஷாராவர்; அக்குழுவில் எந்தவொரு இந்தியரும் சேர்க்கப்படவில்லை.",
        [
            ("A", "Both (A) and (R) are true and (R) is the correct explanation of (A)", "(A) மற்றும் (R) இரண்டும் உண்மை, மேலும் (R) என்பது (A)-வின் சரியான விளக்கமாகும்"),
            ("B", "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கமல்ல"),
            ("C", "(A) is true but (R) is false", "(A) உண்மை, ஆனால் (R) தவறு"),
            ("D", "(A) is false but (R) is true", "(A) தவறு, ஆனால் (R) உண்மை")
        ],
        "A",
        "Historical Context: Section 84A of 1919 Act required appointment of a statutory commission after 10 years to review governance.\nReason: Appointed two years ahead of schedule by British Prime Minister Stanley Baldwin. Because all 7 members were British, Indians felt insulted and boycotted it with slogans like 'Simon Go Back'.\nConstitutional Impact: Simon Commission report (1930) served as a key input for the Government of India Act 1935.\nExam Trap: Simon Commission was statutory commission mandated by 1919 Act; it recommended abolition of Dyarchy in provinces.\nMemory Trick: Simon Commission 1927 = All-White Commission $\rightarrow$ Total Boycott.",
        "வரலாற்றுப் பின்னணி: 1919 சட்டத்தின் பிரிவு 84A 10 ஆண்டுகளுக்குப் பிறகு ஆட்சியை மேலாய்வு செய்ய ஒரு சட்டப்பூர்வக் குழுவை நியமிக்க விதித்தது.\nகாரணம்: பிரிட்டிஷ் பிரதமர் ஸ்டான்லி பால்ட்வினால் 2 ஆண்டுகள் முன்னதாகவே நியமிக்கப்பட்டது. 7 உறுப்பினர்களும் பிரிட்டிஷார் என்பதால் இந்தியர்கள் அதை அவமானமாகக் கருதி 'சைமனே திரும்பப் போ' என்ற கோஷத்துடன் புறக்கணித்தனர்.\nஅரசியலமைப்பு தாக்கம்: சைமன் குழு அறிக்கை (1930) 1935 இந்திய அரசுச் சட்டத்திற்கு முக்கிய உள்ளீடாக அமைந்தது.\nதேர்வுப் பொறி: 1919 சட்டத்தால் விதிக்கப்பட்ட சட்டப்பூர்வ குழுவே சைமன் குழு; இது மாகாண இரட்டை ஆட்சியை ஒழிக்கப் பரிந்துரைத்தது.\nநினைவுச் சூத்திரம்: சைமன் குழு 1927 = வெள்ளை குழு $\rightarrow$ முழு புறக்கணிப்பு.",
        {
            "A": {"en": "Correct. (R) is true and directly explains why (A) occurred.", "ta": "சரி. (R) உண்மை, மேலும் (A) ஏன் நடந்தது என்பதை நேரடியாக விளக்குகிறது."},
            "B": {"en": "Incorrect. Reason directly provides the cause for Assertion.", "ta": "தவறு. காரணம் கூற்றிற்கான காரணியை நேரடியாக அளிக்கிறது."},
            "C": {"en": "Incorrect. Reason is true.", "ta": "தவறு. காரணம் உண்மையானது."},
            "D": {"en": "Incorrect. Assertion is true.", "ta": "தவறு. கூற்று உண்மையானது."}
        },
        "TNPSC Trap: Simon Commission recommended abolition of Dyarchy, establishment of provincial autonomy, and continuation of communal electorate.",
        "TNPSC பொறி: இரட்டை ஆட்சியை ஒழித்தல், மாகாண தன்னாட்சி நிறுவுதல், வகுப்புவாத தொகுதியை நீடித்தல் ஆகியவற்றை சைமன் குழு பரிந்துரைத்தது.",
        "Chairman of the Indian Statutory Commission was Sir John Simon.",
        "இந்திய சட்டப்பூர்வக் குழுவின் தலைவர் சர் ஜான் சைமன் ஆவார்.",
        ["Polity", "Historical Background", "Simon Commission 1927", "Grand Test"], "Understand", 60
    ))

    # Q20: Multi-Act Comparative - Hard - 1919 vs 1935 Provincial Governance
    questions.append(make_q(
        20, "Hard", "Multi-Act Comparative",
        "Which fundamental constitutional transition in provincial administration distinguished the Government of India Act 1935 from the Government of India Act 1919?",
        "1935 இந்திய அரசுச் சட்டத்தை 1919 இந்திய அரசுச் சட்டத்திலிருந்து வேறுபடுத்திய மாகாண நிர்வாகத்தின் அடிப்படை அரசியலமைப்பு மாற்றம் எது?",
        [
            ("A", "Abolition of Dyarchy in Provinces and introduction of Provincial Autonomy, making provincial ministers responsible to elected legislatures", "மாகாணங்களில் இரட்டை ஆட்சியை ஒழித்து மாகாண தன்னாட்சியை அறிமுகப்படுத்துதல், இதன் மூலம் மாகாண அமைச்சர்களைத் தேர்ந்தெடுக்கப்பட்ட சட்டமன்றங்களுக்குப் பொறுப்பாக்குதல்"),
            ("B", "Introduction of Dyarchy in Provinces and abolition of Governor's emergency veto powers", "மாகாணங்களில் இரட்டை ஆட்சியை அறிமுகப்படுத்துதல் மற்றும் கவர்னரின் அவசரகால தடுப்பதிகாரத்தை ஒழித்தல்"),
            ("C", "Centralization of all provincial subjects into a single Federal List controlled by the Viceroy", "அனைத்து மாகாணத் துறைகளையும் வைஸ்ராய் கட்டுப்பாட்டில் உள்ள ஒரே கூட்டாட்சிப் பட்டியலில் மையப்படுத்துதல்"),
            ("D", "Replacement of provincial governors with elected Chief Commissioners", "மாகாண கவர்னர்களுக்குப் பதிலாக தேர்ந்தெடுக்கப்பட்ட தலைமை ஆணையர்களை நியமித்தல்")
        ],
        "A",
        "Historical Context: Simon Commission and Round Table Conferences demanded replacing flawed Dyarchy with complete provincial autonomy.\nReason: GOI Act 1935 abolished Dyarchy in provinces and introduced Provincial Autonomy. Provinces derived direct authority from the Crown and acted as autonomous units of administration.\nConstitutional Impact: Provincial Autonomy came into effect in 1937, leading to Congress ministries in 8 provinces.\nExam Trap: Dyarchy was abolished in provinces by 1935 Act, but proposed (not implemented) at the Center.\nMemory Trick: 1919 = Provincial Dyarchy; 1935 = Provincial Autonomy.",
        "வரலாற்றுப் பின்னணி: சைமன் குழு மற்றும் வட்டமேஜை மாநாடுகள் குறைபாடுள்ள இரட்டை ஆட்சிக்கு பதிலாக முழு மாகாண தன்னாட்சியைக் கோரின.\nகாரணம்: 1935 இந்திய அரசுச் சட்டம் மாகாண இரட்டை ஆட்சியை ஒழித்து மாகாண தன்னாட்சியை அறிமுகப்படுத்தியது. மாகாணங்கள் பிரிட்டிஷ் முடியிலிருந்து நேரடி அதிகாரம் பெற்று தன்னாட்சி பிரிவுகளாகச் செயல்பட்டன.\nஅரசியலமைப்பு தாக்கம்: மாகாண தன்னாட்சி 1937-ல் அமலுக்கு வந்து 8 மாகாணங்களில் காங்கிரஸ் அமைச்சரவைகள் அமையக் காரணமானது.\nதேர்வுப் பொறி: 1935 சட்டத்தால் மாகாணங்களில் இரட்டை ஆட்சி ஒழிக்கப்பட்டது, ஆனால் மத்தியில் முன்மொழியப்பட்டது (அமலாகவில்லை).\nநினைவுச் சூத்திரம்: 1919 = மாகாண இரட்டை ஆட்சி; 1935 = மாகாண தன்னாட்சி.",
        {
            "A": {"en": "Correct. 1935 Act abolished Dyarchy in provinces and instituted Provincial Autonomy.", "ta": "சரி. 1935 சட்டம் மாகாண இரட்டை ஆட்சியை ஒழித்து மாகாண தன்னாட்சியை நிறுவியது."},
            "B": {"en": "Incorrect. Dyarchy in provinces was introduced in 1919, abolished in 1935.", "ta": "தவறு. மாகாண இரட்டை ஆட்சி 1919-ல் அறிமுகமாகி 1935-ல் ஒழிக்கப்பட்டது."},
            "C": {"en": "Incorrect. 1935 Act divided subjects into 3 lists (Federal, Provincial, Concurrent).", "ta": "தவறு. 1935 சட்டம் 3 பட்டியல்களாகப் பிரித்தது."},
            "D": {"en": "Incorrect. Governors continued to be appointed by the Crown.", "ta": "தவறு. கவர்னர்கள் தொடர்ந்து பிரிட்டிஷ் முடியாட்சியால் நியமிக்கப்பட்டனர்."}
        },
        "TNPSC Trap: Provincial autonomy came into operation in 1937 and was discontinued in 1939 when Congress ministries resigned.",
        "TNPSC பொறி: மாகாண தன்னாட்சி 1937-ல் அமலுக்கு வந்தது; 1939-ல் காங்கிரஸ் அமைச்சரவைகள் விலகியபோது முடங்கியது.",
        "GOI Act 1935 allowed Governors to act on advice of ministers, but retained discretionary powers ('special responsibilities').",
        "1935 சட்டம் கவர்னர்கள் அமைச்சர்களின் ஆலோசனையின்படி செயல்படக் கூறியது, ஆனால் தன்னிச்சையான 'சிறப்புப் பொறுப்புகளை' தக்கவைத்தது.",
        ["Polity", "Historical Background", "GOI Act 1935", "GOI Act 1919", "Provincial Autonomy", "Grand Test"], "Analyze", 75
    ))

    # Q21: Direct MCQ - Medium - Government of India Act 1935 Lists
    questions.append(make_q(
        21, "Medium", "Direct MCQ",
        "Under the Government of India Act of 1935, in whom were the Residuary Legislative Powers explicitly vested?",
        "1935 ஆம் ஆண்டின் இந்திய அரசுச் சட்டத்தின் கீழ், எஞ்சிய சட்ட அதிகாரங்கள் (Residuary Powers) யாருக்கு வெளிப்படையாக வழங்கப்பட்டன?",
        [
            ("A", "Governor-General of India", "இந்திய கவர்னர்-ஜெனரல்"),
            ("B", "Federal Legislature", "கூட்டாட்சி சட்டமன்றம்"),
            ("C", "Provincial Legislatures", "மாகாண சட்டமன்றங்கள்"),
            ("D", "Secretary of State for India", "இந்திய அரசுச் செயலர்")
        ],
        "A",
        "Historical Context: Distribution of powers between Center and Units under 1935 Federal Scheme.\nReason: The 1935 Act provided for 3 legislative lists: Federal List (59 items), Provincial List (54 items), and Concurrent List (36 items). The residuary powers of legislation were allocated to the Governor-General in his discretion.\nConstitutional Impact: Unlike the modern Indian Constitution (where residuary powers belong to Parliament under Article 248), under the 1935 Act residuary powers were given to the Governor-General.\nExam Trap: Modern Constitution = Parliament (Union); 1935 Act = Governor-General.\nMemory Trick: 1935 Residuary = Governor-General's Discretion.",
        "வரலாற்றுப் பின்னணி: 1935 கூட்டாட்சித் திட்டத்தில் மத்திய-மாகாண அதிகாரப் பங்கீடு.\nகாரணம்: 1935 சட்டம் 3 சட்டப் பட்டியல்களை வழங்கியது: கூட்டாட்சிப் பட்டியல் (59), மாகாணப் பட்டியல் (54), பொதுப் பட்டியல் (36). எஞ்சிய அதிகாரங்கள் கவர்னர்-ஜெனரலின் தன்னிச்சையான அதிகாரத்திற்கு வழங்கப்பட்டன.\nஅரசியலமைப்பு தாக்கம்: நவீன இந்திய அரசியலமைப்பு போலன்றி (சரத்து 248-ன் கீழ் நாடாளுமன்றத்திற்கு எஞ்சிய அதிகாரம்), 1935 சட்டத்தில் எஞ்சிய அதிகாரம் கவர்னர்-ஜெனரலிடம் இருந்தது.\nதேர்வுப் பொறி: நவீன அரசியலமைப்பு = நாடாளுமன்றம் (ஒன்றியம்); 1935 சட்டம் = கவர்னர்-ஜெனரல்.\nநினைவுச் சூத்திரம்: 1935 எஞ்சிய அதிகாரம் = கவர்னர்-ஜெனரல் விருப்பம்.",
        {
            "A": {"en": "Correct. Residuary powers were vested in the Governor-General in his discretion.", "ta": "சரி. எஞ்சிய அதிகாரங்கள் கவர்னர்-ஜெனரலின் தன்னிச்சையான அதிகாரத்திற்கு வழங்கப்பட்டன."},
            "B": {"en": "Incorrect. Federal Legislature did not hold residuary powers under 1935 Act.", "ta": "தவறு. கூட்டாட்சி சட்டமன்றத்திற்கு எஞ்சிய அதிகாரம் இல்லை."},
            "C": {"en": "Incorrect. Provincial legislatures only held powers over Provincial List items.", "ta": "தவறு. மாகாண சட்டமன்றங்களுக்கு மாகாணப் பட்டியல் அதிகாரமே இருந்தது."},
            "D": {"en": "Incorrect. Secretary of State was in London and did not hold residuary power.", "ta": "தவறு. அரசுச் செயலரிடம் எஞ்சிய அதிகாரம் இல்லை."}
        },
        "TNPSC Trap: Under Indian Constitution (Art 248), Residuary powers belong to Parliament; under US Constitution, to States; under 1935 Act, to Governor-General.",
        "TNPSC பொறி: இந்திய அரசியலமைப்பில் (சரத்து 248) எஞ்சிய அதிகாரம் நாடாளுமன்றத்திற்கு; அமெரிக்காவில் மாநிலங்களுக்கு; 1935 சட்டத்தில் கவர்னர்-ஜெனரலுக்கு.",
        "1935 Act list counts: Federal (59), Provincial (54), Concurrent (36).",
        "1935 சட்டப் பட்டியல் எண்கள்: கூட்டாட்சி (59), மாகாணம் (54), பொது (36).",
        ["Polity", "Historical Background", "GOI Act 1935", "Residuary Powers", "Grand Test"], "Understand", 60
    ))

    # Q22: Statement Based - Hard - Indian Independence Act 1947
    questions.append(make_q(
        22, "Hard", "Statement Based",
        "Consider the following statements regarding the Indian Independence Act of 1947:\n1. It declared India an independent and sovereign state from August 15, 1947.\n2. It abolished the office of Viceroy and provided for a Governor-General in each dominion appointed by the British King on the advice of the dominion cabinet.\n3. It abolished the office of Secretary of State for India and transferred his functions to the Secretary of State for Commonwealth Relations.\n4. It empowered the Constituent Assemblies of both dominions to frame and adopt any constitution and repeal any Act of British Parliament, including the Independence Act itself.\nWhich of the statements given above are correct?",
        "1947 இந்திய சுதந்திரச் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது ஆகஸ்ட் 15, 1947 முதல் இந்தியாவை சுதந்திரமான மற்றும் இறையாண்மை கொண்ட அரசாக அறிவித்தது.\n2. இது வைஸ்ராய் பதவியை ஒழித்து, டொமினியன் அமைச்சரவையின் ஆலோசனையின் பேரில் பிரிட்டிஷ் மன்னரால் நியமிக்கப்படும் கவர்னர்-ஜெனரல் பதவியை ஒவ்வொரு டொமினியனுக்கும் வழங்கியது.\n3. இது இந்திய அரசுச் செயலர் பதவியை ஒழித்து, அவரது பணிகளை காமன்வெல்த் உறவுகள் அரசுச் செயலருக்கு மாற்றியது.\n4. இது இரு டொமினியன்களின் அரசியல் நிர்ணய சபைகளுக்கும் எந்தவொரு அரசியலமைப்பையும் உருவாக்கவும், சுதந்திரச் சட்டம் உட்பட பிரிட்டிஷ் நாடாளுமன்றத்தின் எந்தவொரு சட்டத்தையும் ரத்து செய்யவும் அதிகாரமளித்தது.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
        [
            ("A", "1, 2, 3 and 4", "1, 2, 3 மற்றும் 4"),
            ("B", "1, 2 and 4 only", "1, 2 மற்றும் 4 மட்டுமே"),
            ("C", "1 and 3 only", "1 மற்றும் 3 மட்டுமே"),
            ("D", "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டுமே")
        ],
        "A",
        "Historical Context: Enacted based on Mountbatten Plan (June 3, 1947) to end British rule in India.\nReason: All four statements are correct. The 1947 Act granted complete constituent sovereignty to the Constituent Assemblies of India and Pakistan, abolished Viceroy and SOS for India offices, and allowed repealing British statutes.\nConstitutional Impact: Legal termination of British suzerainty over Princely States and Indian territories.\nExam Trap: Office of Secretary of State for India was created in 1858 and abolished in 1947.\nMemory Trick: 1947 Act = Sovereign Assemblies + No Viceroy + No SOS + Repeal British Acts.",
        "வரலாற்றுப் பின்னணி: இந்தியாவில் பிரிட்டிஷ் ஆட்சியை முடிக்க மவுண்ட்பேட்டன் திட்டத்தின் (ஜூன் 3, 1947) அடிப்படையில் இயற்றப்பட்டது.\nகாரணம்: நான்கு கூற்றுகளும் சரியானவை. 1947 சட்டம் இந்தியா மற்றும் பாகிஸ்தான் அரசியல் நிர்ணய சபைகளுக்கு முழு அரசியலமைப்பு இறையாண்மையை அளித்தது, வைஸ்ராய் மற்றும் அரசுச் செயலர் பதவிகளை ஒழித்தது, பிரிட்டிஷ் சட்டங்களை ரத்து செய்ய அதிகாரமளித்தது.\nஅரசியலமைப்பு தாக்கம்: சுதேச சமஸ்தானங்கள் மீதான பிரிட்டிஷ் மேலாதிக்கத்தின் சட்டப்பூர்வ முடிவு.\nதேர்வுப் பொறி: இந்திய அரசுச் செயலர் பதவி 1858-ல் உருவாக்கப்பட்டு 1947-ல் ஒழிக்கப்பட்டது.\nநினைவுச் சூத்திரம்: 1947 சட்டம் = இறையாண்மை சபைகள் + வைஸ்ராய் இல்லை + அரசுச் செயலர் இல்லை.",
        {
            "A": {"en": "Correct. All four statements accurately state provisions of 1947 Indian Independence Act.", "ta": "சரி. நான்கு கூற்றுகளும் 1947 இந்திய சுதந்திரச் சட்டத்தின் விதிகளைத் துல்லியமாக விவரிக்கின்றன."},
            "B": {"en": "Incorrect. Statement 3 is also correct.", "ta": "தவறு. கூற்று 3-ம் சரியானது."},
            "C": {"en": "Incorrect. Statements 2 and 4 are also correct.", "ta": "தவறு. கூற்றுகள் 2 மற்றும் 4-ம் சரியானவை."},
            "D": {"en": "Incorrect. Statement 1 is also correct.", "ta": "தவறு. கூற்று 1-ம் சரியானது."}
        },
        "TNPSC Trap: Lord Mountbatten became the first Governor-General of independent India; C. Rajagopalachari became the first and only Indian Governor-General of India.",
        "TNPSC பொறி: சுதந்திர இந்தியாவின் முதல் கவர்னர்-ஜெனரல் லார்டு மவுண்ட்பேட்டன்; முதல் மற்றும் ஒரே இந்திய கவர்னர்-ஜெனரல் சி. ராஜகோபாலாச்சாரி.",
        "Indian Independence Act was passed by British Parliament on July 18, 1947.",
        "இந்திய சுதந்திரச் சட்டம் ஜூலை 18, 1947-ல் பிரிட்டிஷ் நாடாளுமன்றத்தால் நிறைவேற்றப்பட்டது.",
        ["Polity", "Historical Background", "Indian Independence Act 1947", "Grand Test"], "Analyze", 75
    ))

    # Q23: Match the Following - Medium - Governor-Generals & Acts
    questions.append(make_q(
        23, "Medium", "Match the Following",
        "Match List I (Governor-General / Viceroy) with List II (Associated Key Constitutional Landmark):\n\nList I\nA. Warren Hastings\nB. Lord William Bentinck\nC. Lord Canning\nD. Lord Minto\n\nList II\n1. Indian Councils Act 1909 (Communal Electorates)\n2. Regulating Act 1773 (First Governor-General of Bengal)\n3. Charter Act 1833 (First Governor-General of India)\n4. Government of India Act 1858 (First Viceroy of India)",
        "பட்டியல் I (கவர்னர்-ஜெனரல் / வைஸ்ராய்) பட்டியல் II (தொடர்புடைய முக்கிய அரசியலமைப்பு மைல்கல்) பொருத்துக:\n\nபட்டியல் I\nA. வாரன் ஹேஸ்டிங்ஸ்\nB. லார்டு வில்லியம் பென்டிங்க்\nC. லார்டு கேனிங்\nD. லார்டு மிண்டோ\n\nபட்டியல் II\n1. 1809 இந்தியக் கவுன்சில்கள் சட்டம் (வகுப்புவாத தொகுதிகள்)\n2. 1773 ஒழுங்குமுறைச் சட்டம் (முதல் வங்காள கவர்னர்-ஜெனரல்)\n3. 1833 சாசனச் சட்டம் (முதல் இந்திய கவர்னர்-ஜெனரல்)\n4. 1858 இந்திய அரசுச் சட்டம் (முதல் இந்திய வைஸ்ராய்)",
        [
            ("A", "A-2, B-3, C-4, D-1", "A-2, B-3, C-4, D-1"),
            ("B", "A-3, B-2, C-4, D-1", "A-3, B-2, C-4, D-1"),
            ("C", "A-2, B-4, C-3, D-1", "A-2, B-4, C-3, D-1"),
            ("D", "A-4, B-3, C-2, D-1", "A-4, B-3, C-2, D-1")
        ],
        "A",
        "Historical Context: The evolution of executive heads mapped to statutory titles across Company and Crown Rule.\nReason: Correct matching: A-2 (Warren Hastings $\rightarrow$ 1773 1st GG of Bengal), B-3 (William Bentinck $\rightarrow$ 1833 1st GG of India), C-4 (Lord Canning $\rightarrow$ 1858 1st Viceroy), D-1 (Lord Minto $\rightarrow$ 1909 Communal Electorates).\nConstitutional Impact: Represents the transformation of executive leadership titles in British India.\nExam Trap: Warren Hastings = GG of Bengal; Bentinck = GG of India; Canning = Viceroy.\nMemory Trick: Hastings (Bengal) $\rightarrow$ Bentinck (India) $\rightarrow$ Canning (Viceroy) $\rightarrow$ Minto (Communal).",
        "வரலாற்றுப் பின்னணி: நிர்வாகத் தலைவர்களின் தலைப்புகள் சட்டங்கள் வழியாக மாறிய வளர்ச்சி.\nகாரணம்: சரியான பொருத்தம்: A-2 (வாரன் ஹேஸ்டிங்ஸ் $\rightarrow$ 1773 1வது வங்காள கவர்னர்-ஜெனரல்), B-3 (வில்லியம் பென்டிங்க் $\rightarrow$ 1833 1வது இந்திய கவர்னர்-ஜெனரல்), C-4 (லார்டு கேனிங் $\rightarrow$ 1858 1வது வைஸ்ராய்), D-1 (லார்டு மிண்டோ $\rightarrow$ 1909 வகுப்புவாத தொகுதிகள்).\nஅரசியலமைப்பு தாக்கம்: பிரிட்டிஷ் இந்தியாவின் நிர்வாக தலைமைப் பொறுப்புகளின் மாற்றத்தைக் காட்டுகிறது.\nதேர்வுப் பொறி: ஹேஸ்டிங்ஸ் = வங்காள GG; பென்டிங்க் = இந்திய GG; கேனிங் = வைஸ்ராய்.\nநினைவுச் சூத்திரம்: ஹேஸ்டிங்ஸ் (வங்காளம்) $\rightarrow$ பென்டிங்க் (இந்தியா) $\rightarrow$ கேனிங் (வைஸ்ராய்) $\rightarrow$ மிண்டோ (வகுப்புவாதம்).",
        {
            "A": {"en": "Correct match across executive heads and their respective statutory landmarks.", "ta": "சரி. நிர்வாகத் தலைவர்களுக்கும் அவர்களின் சட்டப் பணிகளுக்குமான சரியான பொருத்தம்."},
            "B": {"en": "Incorrect. Warren Hastings was Governor-General of Bengal (2), not India.", "ta": "தவறு. வாரன் ஹேஸ்டிங்ஸ் வங்காள கவர்னர்-ஜெனரல் (2)."},
            "C": {"en": "Incorrect. Bentinck was GG of India (3), Canning was Viceroy (4).", "ta": "தவறு. பென்டிங்க் இந்திய GG (3), கேனிங் வைஸ்ராய் (4)."},
            "D": {"en": "Incorrect. Hastings was not Viceroy.", "ta": "தவறு. ஹேஸ்டிங்ஸ் வைஸ்ராய் அல்ல."}
        },
        "TNPSC Trap: Lord Canning was both the last Governor-General of India under Company Rule and the first Viceroy of India under Crown Rule.",
        "TNPSC பொறி: லார்டு கேனிங் கம்பெனி ஆட்சியின் கடைசி இந்திய கவர்னர்-ஜெனரலாகவும் பிரிட்டிஷ் முடி ஆட்சியின் முதல் வைஸ்ராயாகவும் இருந்தார்.",
        "Lord Minto is known as the 'Father of Communal Electorate'.",
        "லார்டு மிண்டோ 'வகுப்புவாத வாக்காளர் தொகுதியின் தந்தை' என அழைக்கப்படுகிறார்.",
        ["Polity", "Historical Background", "Match the Following", "Governor Generals", "Grand Test"], "Analyze", 75
    ))

    # Q24: Multi-Act Integrated - Hard - Civil Services Evolution
    questions.append(make_q(
        24, "Hard", "Multi-Act Integrated",
        "Which sequence accurately details the statutory evolution of Civil Services recruitment in India from 1833 to 1935?",
        "1833 முதல் 1935 வரையிலான காலத்தில் இந்தியாவில் சிவில் சர்வீஸ் நியமனத்தின் சட்டப்பூர்வ வளர்ச்சியைத் துல்லியமாக விளக்கும் வரிசை எது?",
        [
            ("A", "Attempted open competition via Section 87 (1833) -> Open competition established via Macaulay Committee (1853/1854) -> Aitchison Committee introducing Statutory, Covenanted & Uncovenanted reforms (1886) -> Federal Public Service Commission established (1935)", "பிரிவு 87 வழி போட்டித் தேர்வு முயற்சி (1833) -> மெக்காலே குழு வழி போட்டித் தேர்வு உறுதி (1853/1854) -> ஏட்சின்சன் குழு வழி வகைப்பாடுகள் (1886) -> கூட்டாட்சி பொதுப்பணி ஆணையம் அமைப்பு (1935)"),
            ("B", "Open competition established (1833) -> Attempted open competition (1853) -> Lee Commission establishing FPSC (1886) -> Macaulay Committee (1935)", "போட்டித் தேர்வு உறுதி (1833) -> போட்டித் தேர்வு முயற்சி (1853) -> லீ குழு FPSC அமைப்பு (1886) -> மெக்காலே குழு (1935)"),
            ("C", "Aitchison Committee (1833) -> Section 87 attempt (1853) -> Macaulay Committee (1886) -> FPSC (1935)", "ஏட்சின்சன் குழு (1833) -> பிரிவு 87 முயற்சி (1853) -> மெக்காலே குழு (1886) -> FPSC (1935)"),
            ("D", "FPSC established (1833) -> Open competition (1853) -> Section 87 attempt (1886) -> Aitchison Committee (1935)", "FPSC அமைப்பு (1833) -> போட்டித் தேர்வு (1853) -> பிரிவு 87 முயற்சி (1886) -> ஏட்சின்சன் குழு (1935)")
        ],
        "A",
        "Historical Context: Civil service recruitment transitioned from EIC patronage to open merit-based competition.\nReason: 1833 Act attempted open competition (negated) $\rightarrow$ 1853 Act instituted open competition (Macaulay Committee appointed 1854) $\rightarrow$ 1886 Aitchison Committee categorized services into Imperial, Provincial, and Subordinate $\rightarrow$ 1935 GOI Act established Federal Public Service Commission (and Provincial Public Service Commissions).\nConstitutional Impact: Laid the foundation for UPSC and State PSCs in modern India (Articles 315-323).\nExam Trap: Central Public Service Commission was set up in 1926 (Lee Commission 1923); renamed Federal Public Service Commission in 1935 Act.\nMemory Trick: 1833 (Attempt) $\rightarrow$ 1853 (Macaulay Open Exam) $\rightarrow$ 1886 (Aitchison) $\rightarrow$ 1935 (FPSC).",
        "வரலாற்றுப் பின்னணி: சிவில் சர்வீஸ் நியமனம் கம்பெனி ஆதரவு முறையிலிருந்து திறந்த தகுதிப்போட்டி முறைக்கு மாறியது.\nகாரணம்: 1833 சட்டம் போட்டித் தேர்வை முயன்றது (கைவிடப்பட்டது) $\rightarrow$ 1853 சட்டம் போட்டித் தேர்வை நிறுவியது (1854 மெக்காலே குழு) $\rightarrow$ 1886 ஏட்சின்சன் குழு பணிகளை ஏகாதிபத்திய, மாகாண, சார்நிலைப் பணிகளாகப் பிரித்தது $\rightarrow$ 1935 சட்டம் கூட்டாட்சி பொதுப்பணி ஆணையத்தை நிறுவியது.\nஅரசியலமைப்பு தாக்கம்: நவீன இந்தியாவில் UPSC மற்றும் மாநில PSC-களுக்கு (சரத்துகள் 315-323) அடித்தளம் அமைத்தது.\nதேர்வுப் பொறி: மத்திய பொதுப்பணி ஆணையம் 1926-ல் அமைக்கப்பட்டது (1923 லீ குழு); 1935 சட்டத்தில் கூட்டாட்சி பொதுப்பணி ஆணையம் என பெயர் மாற்றப்பட்டது.\nநினைவுச் சூத்திரம்: 1833 (முயற்சி) $\rightarrow$ 1853 (மெக்காலே போட்டித் தேர்வு) $\rightarrow$ 1886 (ஏட்சின்சன்) $\rightarrow$ 1935 (FPSC).",
        {
            "A": {"en": "Correct sequence mapping Civil Services development from 1833 attempt to 1935 FPSC.", "ta": "சரி. 1833 முயற்சி முதல் 1935 FPSC வரையிலான சிவில் சர்வீஸ் வளர்ச்சியின் சரியான வரிசை."},
            "B": {"en": "Incorrect. 1833 attempted open competition; it was established in 1853.", "ta": "தவறு. 1833-ல் முயற்சி செய்யப்பட்டது; 1853-லேயே நிறுவப்பட்டது."},
            "C": {"en": "Incorrect. Aitchison Committee was appointed in 1886, not 1833.", "ta": "தவறு. ஏட்சின்சன் குழு 1886-ல் நியமிக்கப்பட்டது."},
            "D": {"en": "Incorrect. FPSC was established under 1935 Act, not 1833.", "ta": "தவறு. FPSC 1935 சட்டத்தில் அமைக்கப்பட்டது."}
        },
        "TNPSC Trap: Lee Commission (1923) recommended establishing Central Public Service Commission, which was set up in 1926.",
        "TNPSC பொறி: லீ குழு (1923) பரிந்துரையால் 1926-ல் மத்திய பொதுப்பணி ஆணையம் அமைக்கப்பட்டது.",
        "Macaulay Committee (Committee on Indian Civil Service) was appointed in 1854.",
        "இந்திய சிவில் சர்வீஸ் பற்றிய மெக்காலே குழு 1854-ல் நியமிக்கப்பட்டது.",
        ["Polity", "Historical Background", "Civil Services Evolution", "Multi-Act Integration", "Grand Test"], "Analyze", 75
    ))

    # Q25: Direct MCQ - Hard - Amending Act 1781 Jurisdictional Rules
    questions.append(make_q(
        25, "Hard", "Direct MCQ",
        "Regarding personal law administration under the Amending Act of 1781, what explicit statutory command was issued to the Supreme Court at Fort William?",
        "1781 ஆம் ஆண்டின் திருத்தச் சட்டத்தின் கீழ் தனிநபர் சட்ட நிர்வாகம் தொடர்பாக வில்லியம் கோட்டை உச்ச நீதிமன்றத்திற்கு வழங்கப்பட்ட வெளிப்படையான சட்டப்பூர்வ கட்டளை யாது?",
        [
            ("A", "The Supreme Court was required to administer English Common Law uniformly to all inhabitants of Calcutta regardless of religion.", "உச்ச நீதிமன்றம் மதத்தைப் பொருட்படுத்தாமல் கொல்கத்தாவின் அனைத்து குடிமக்களுக்கும் பிரிட்டிஷ் பொதுச் சட்டத்தை சீராகப் பயன்படுத்த வேண்டும்."),
            ("B", "The Supreme Court was required to administer Hindu Law for Hindu defendants and Mohammedan Law for Muslim defendants.", "உச்ச நீதிமன்றம் இந்து எதிரிகளுக்கு இந்து சட்டத்தையும் முஸ்லிம் எதிரிகளுக்கு முகமதிய சட்டத்தையும் பயன்படுத்தி தீர்ப்பு வழங்க வேண்டும்."),
            ("C", "The Supreme Court was barred completely from taking up any civil disputes between native Indians.", "உச்ச நீதிமன்றம் உள்ளூர் இந்தியர்களிடையே ஏற்படும் எந்தவொரு சிவில் வழக்குகளையும் விசாரிக்க முற்றிலும் தடை விதிக்கப்பட்டது."),
            ("D", "The Supreme Court was ordered to apply Canon Law for native Christians and Parsi Law for Parsis.", "உச்ச நீதிமன்றம் உள்ளூர் கிறிஸ்தவர்களுக்கு திருச்சபை சட்டத்தையும் பார்சிகளுக்கு பார்சி சட்டத்தையும் பயன்படுத்த உத்தரவிடப்பட்டது.")
        ],
        "B",
        "Historical Context: Conflict between English law and traditional Indian personal laws after 1773 Act.\nReason: The Amending Act of 1781 explicitly mandated that the Supreme Court was to administer personal law of the defendant—that is, cases involving Hindus were to be decided according to Hindu law, and cases involving Muslims according to Mohammedan law.\nConstitutional Impact: Early statutory recognition of religious personal laws in British Indian jurisprudence.\nExam Trap: Law of the defendant (not plaintiff) determined applicable personal law.\nMemory Trick: 1781 Personal Law = Defendant's religion determines law.",
        "வரலாற்றுப் பின்னணி: 1773 சட்டத்திற்குப் பிறகு பிரிட்டிஷ் பொதுச் சட்டத்திற்கும் இந்திய பாரம்பரிய தனிநபர் சட்டங்களுக்கும் இடையே ஏற்பட்ட மோதல்.\nகாரணம்: 1781 திருத்தச் சட்டம் எதிராளியின் தனிநபர் சட்டப்படி தீர்ப்பு வழங்க வேண்டும் என வெளிப்படையாகக் கூறியது—இந்துக்கள் தொடர்பான வழக்குகள் இந்து சட்டப்படியும், முஸ்லிம்கள் தொடர்பான வழக்குகள் முகமதிய சட்டப்படியும் தீர்மானிக்கப்பட வேண்டும்.\nஅரசியலமைப்பு தாக்கம்: பிரிட்டிஷ் இந்திய நீதித்துறையில் மத தனிநபர் சட்டங்களுக்கு வழங்கப்பட்ட ஆரம்பகால சட்டப்பூர்வ அங்கீகாரம்.\nதேர்வுப் பொறி: வாதி அல்ல, எதிராளியின் மதமே பொருந்தக்கூடிய தனிநபர் சட்டத்தைத் தீர்மானித்தது.\nநினைவுச் சூத்திரம்: 1781 தனிநபர் சட்டம் = எதிராளியின் மதமே சட்டத்தை முடிவு செய்யும்.",
        {
            "A": {"en": "Incorrect. 1781 Act mandated respect for personal religious laws, not uniform English Common Law.", "ta": "தவறு. 1781 சட்டம் தனிநபர் மதச் சட்டங்களை மதிக்கக் கூறியது."},
            "B": {"en": "Correct. Mandated Hindu law for Hindus and Mohammedan law for Muslims based on defendant's religion.", "ta": "சரி. எதிராளியின் மதத்தின் அடிப்படையில் இந்துக்களுக்கு இந்து சட்டமும் முஸ்லிம்களுக்கு முகமதிய சட்டமும் விதிக்கப்பட்டது."},
            "C": {"en": "Incorrect. Court could take up native civil disputes if both parties agreed to its jurisdiction.", "ta": "தவறு. இரு தரப்பும் ஒப்புக்கொண்டால் நீதிமன்றம் வழக்கை விசாரிக்கலாம்."},
            "D": {"en": "Incorrect. The Act specifically highlighted Hindu and Mohammedan laws.", "ta": "தவறு. சட்டம் குறிப்பாக இந்து மற்றும் முகமதிய சட்டங்களையே சுட்டிக்காட்டியது."}
        },
        "TNPSC Trap: Personal law applied based on the defendant's religion, not the plaintiff's religion under 1781 Act.",
        "TNPSC பொறி: 1781 சட்டத்தின் கீழ் தனிநபர் சட்டம் வாதியின் மதப்படியல்ல, எதிராளியின் மதப்படியே பொருந்தியது.",
        "1781 Act also provided that appeals from Provincial Courts could be taken to the Governor-General in Council, not Supreme Court.",
        "1781 சட்டம் மாகாண நீதிமன்ற மேல்முறையீடுகள் உச்ச நீதிமன்றத்திற்கு அல்லாமல் கவர்னர்-ஜெனரல் கவுன்சிலுக்கே செல்லும் என்றும் விதித்தது.",
        ["Polity", "Historical Background", "Act of Settlement 1781", "Personal Laws", "Grand Test"], "Analyze", 75
    ))

    return questions

if __name__ == "__main__":
    qs = get_part1_questions()
    print(f"Part 1 Questions Generated: {len(qs)}")
