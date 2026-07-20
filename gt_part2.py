import json

def get_part2_questions():
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

    # Q26: Multi-Act Comparative - Hard - Company Rule to Crown Rule Legal Transfer
    questions.append(make_q(
        26, "Hard", "Multi-Act Comparative",
        "Which legal and institutional transformation marked the formal shift of sovereignty from Company Rule to Crown Rule under the Government of India Act 1858?",
        "1858 இந்திய அரசுச் சட்டத்தின் கீழ் கிழக்கிந்திய கம்பெனி ஆட்சியிலிருந்து பிரிட்டிஷ் முடி ஆட்சிக்கு அதிகாரப்பூர்வமாக இறையாண்மை மாறியதை சுட்டிக்காட்டும் சட்டப்பூர்வ மற்றும் நிறுவன மாற்றம் எது?",
        [
            ("A", "Liquidation of East India Company's rule, abolition of Court of Directors and Board of Control, and creation of Secretary of State for India in Council", "கிழக்கிந்திய கம்பெனியின் ஆட்சியை முடித்து, இயக்குநர்கள் அவை மற்றும் கட்டுப்பாட்டு வாரியத்தைக் கலைத்து, இந்திய அரசுச் செயலர் பதவியை உருவாக்குதல்"),
            ("B", "Transfer of military command to the Governor-General while leaving civil administration with the Court of Directors", "சிவில் நிர்வாகத்தை இயக்குநர்கள் அவையிடம் விட்டு இராணுவக் கட்டுப்பாட்டை மட்டும் கவர்னர்-ஜெனரலிடம் மாற்றுதல்"),
            ("C", "Establishment of a sovereign Federal Parliament in Calcutta with supreme legislative authority", "கொல்கத்தாவில் உச்ச சட்ட அதிகாரம் கொண்ட இறையாண்மை கூட்டாட்சி நாடாளுமன்றத்தை அமைத்தல்"),
            ("D", "Replacement of British Indian laws with the English Bill of Rights 1689", "பிரிட்டிஷ் இந்தியச் சட்டங்களுக்குப் பதிலாக 1689 இங்கிலாந்து உரிமைச் சாசனத்தைப் பயன்படுத்துதல்")
        ],
        "A",
        "Historical Context: Passed in the aftermath of the Revolt of 1857 (Sepoy Mutiny).\nReason: GOI Act 1858 abolished the dual system of control created by Pitt's India Act 1784 by dissolving the Court of Directors and Board of Control. It transferred governance to Her Majesty Queen Victoria and created the Secretary of State for India assisted by a 15-member Council of India.\nConstitutional Impact: Direct responsibility of British Cabinet for Indian administration.\nExam Trap: 1858 Act changed the administrative machinery in London, but did not alter the system of governance inside India significantly.\nMemory Trick: 1858 Act = No EIC + No Board of Control + Yes Secretary of State.",
        "வரலாற்றுப் பின்னணி: 1857 பெரும் புரட்சியின் (சிப்பாய் கலகம்) விளைவாக நிறைவேற்றப்பட்டது.\nகாரணம்: 1858 இந்திய அரசுச் சட்டம் 1784 பிட் இந்தியச் சட்டத்தால் உருவாக்கப்பட்ட இரட்டை ஆட்சியை (இயக்குநர்கள் அவை & கட்டுப்பாட்டு வாரியம்) கலைத்து ஒழித்தது. ஆட்சி அதிகாரம் விக்டோரியா மகாராணிக்கு மாற்றப்பட்டு 15 உறுப்பினர் குழுவுடன் இந்திய அரசுச் செயலர் உருவாக்கப்பட்டார்.\nஅரசியலமைப்பு தாக்கம்: இந்திய நிர்வாகத்திற்கு பிரிட்டிஷ் அமைச்சரவையின் நேரடிப் பொறுப்புக்கூறல்.\nதேர்வுப் பொறி: 1858 சட்டம் லண்டனில் உள்ள நிர்வாக அமைப்பை மாற்றியதே தவிர இந்தியாவில் உள்ள உள்நாட்டு ஆட்சி முறையை பெரிய அளவில் மாற்றவில்லை.\nநினைவுச் சூத்திரம்: 1858 சட்டம் = கம்பெனி இல்லை + கட்டுப்பாட்டு வாரியம் இல்லை + அரசுச் செயலர் உண்டு.",
        {
            "A": {"en": "Correct. Abolished EIC rule, Court of Directors, Board of Control, and created SOS for India.", "ta": "சரி. கம்பெனி ஆட்சி, இயக்குநர்கள் அவை, கட்டுப்பாட்டு வாரியம் ஒழிக்கப்பட்டு அரசுச் செயலர் உருவாக்கப்பட்டார்."},
            "B": {"en": "Incorrect. Both civil and military powers were transferred to the Crown.", "ta": "தவறு. சிவில், இராணுவம் இரண்டும் முடி ஆட்சிக்கு மாறின."},
            "C": {"en": "Incorrect. Supreme legislative authority remained with British Parliament in London.", "ta": "தவறு. உச்ச அதிகார நாடாளுமன்றம் கொல்கத்தாவில் அமைக்கப்படவில்லை."},
            "D": {"en": "Incorrect. Bill of Rights 1689 was not extended to India.", "ta": "தவறு. 1689 உரிமைச் சாசனம் இந்தியாவிற்கு நீட்டிக்கப்படவில்லை."}
        },
        "TNPSC Trap: Lord Canning announced Queen Victoria's Proclamation at the Allahabad Durbar on November 1, 1858.",
        "TNPSC பொறி: லார்டு கேனிங் 1858 நவம்பர் 1 அன்று அலகாபாத் தர்பாரில் விக்டோரியா மகாராணியின் பேரறிக்கையை வாசித்தார்.",
        "Queen Victoria's Proclamation (1858) was hailed as the 'Magnacarta of the People of India'.",
        "விக்டோரியா மகாராணியின் பேரறிக்கை (1858) 'இந்திய மக்களின் மகாசாசனம்' எனப் போற்றப்பட்டது.",
        ["Polity", "Historical Background", "GOI Act 1858", "Crown Rule", "Grand Test"], "Analyze", 75
    ))

    # Q27: Statement Based - Medium - Evolution of Law Commissions
    questions.append(make_q(
        27, "Medium", "Statement Based",
        "Consider the following statements regarding the historical establishment of Law Commissions in British India:\n1. The First Law Commission of India was established in 1834 under the Charter Act of 1833.\n2. Lord Macaulay was appointed as the Chairman of the First Law Commission.\n3. The Indian Penal Code (IPC) of 1860 was drafted based on the recommendations of the First Law Commission.\nWhich of the statements given above are correct?",
        "பிரிட்டிஷ் இந்தியாவில் சட்ட ஆணையங்கள் (Law Commissions) வரலாற்று ரீதியாக அமைக்கப்பட்டமை பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இந்தியாவின் முதல் சட்ட ஆணையம் 1833 சாசனச் சட்டத்தின் கீழ் 1834-ல் அமைக்கப்பட்டது.\n2. லார்டு மெக்காலே முதல் சட்ட ஆணையத்தின் தலைவராக நியமிக்கப்பட்டார்.\n3. 1860 ஆம் ஆண்டின் இந்திய தண்டனைச் சட்டம் (IPC) முதல் சட்ட ஆணையத்தின் பரிந்துரைகளின் அடிப்படையில் வரைவு செய்யப்பட்டது.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
        [
            ("A", "1, 2 and 3", "1, 2 மற்றும் 3"),
            ("B", "1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
            ("C", "2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
            ("D", "1 and 3 only", "1 மற்றும் 3 மட்டுமே")
        ],
        "A",
        "Historical Context: Codification of Indian laws was initiated under the Charter Act of 1833 to codify diverse legal systems.\nReason: All three statements are correct. 1st Law Commission (1834) was chaired by Macaulay. Its draft formed the basis of IPC 1860, CrPC 1861, and Civil Procedure Code 1859.\nConstitutional Impact: Created codified statutory criminal and civil jurisprudence across British India.\nExam Trap: 1st Law Commission was 1834 (under 1833 Act), while 2nd, 3rd, and 4th Law Commissions were appointed in 1853, 1861, and 1879.\nMemory Trick: 1834 1st Law Commission = Macaulay + Codified IPC 1860.",
        "வரலாற்றுப் பின்னணி: பல்வேறு சட்ட முறைகளை முறைப்படுத்த 1833 சாசனச் சட்டத்தின் கீழ் சட்டங்களின் குறியீடாக்கம் தொடங்கப்பட்டது.\nகாரணம்: மூன்று கூற்றுகளும் சரியானவை. 1834 முதல் சட்ட ஆணையத்திற்கு மெக்காலே தலைமை தாங்கினார். அதன் வரைவே 1860 IPC, 1861 CrPC, 1859 CPC ஆகியவற்றுக்கு அடிப்படையாக அமைந்தது.\nஅரசியலமைப்பு தாக்கம்: பிரிட்டிஷ் இந்தியா முழுவதும் சீரான சட்டத் தொகுப்புகளை உருவாக்கியது.\nதேர்வுப் பொறி: 1வது சட்ட ஆணையம் 1834 (1833 சட்டத்தின்கீழ்); 2வது, 3வது, 4வது ஆணையங்கள் 1853, 1861, 1879-ல் நியமிக்கப்பட்டன.\nநினைவுச் சூத்திரம்: 1834 1வது சட்ட ஆணையம் = மெக்காலே + 1860 IPC வரைவு.",
        {
            "A": {"en": "Correct. All three statements regarding the First Law Commission are historically true.", "ta": "சரி. முதல் சட்ட ஆணையம் தொடர்பான மூன்று கூற்றுகளும் வரலாற்று ரீதியாக சரியானவை."},
            "B": {"en": "Incorrect. Statement 3 is also correct.", "ta": "தவறு. கூற்று 3-ம் சரியானது."},
            "C": {"en": "Incorrect. Statement 1 is also correct.", "ta": "தவறு. கூற்று 1-ம் சரியானது."},
            "D": {"en": "Incorrect. Statement 2 is also correct.", "ta": "தவறு. கூற்று 2-ம் சரியானது."}
        },
        "TNPSC Trap: Lord Macaulay was appointed to Governor-General's Council as 4th Law Member under Charter Act 1833 and subsequently chaired 1834 Law Commission.",
        "TNPSC பொறி: லார்டு மெக்காலே 1833 சட்டத்தின் கீழ் 4வது சட்ட உறுப்பினராகச் சேர்க்கப்பட்டு, 1834 சட்ட ஆணையத்தின் தலைவரானார்.",
        "Indian Penal Code drafted in 1837 by Macaulay Commission came into force in 1860.",
        "1837-ல் மெக்காலே குழுவால் வரைவு செய்யப்பட்ட தண்டனைச் சட்டம் 1860-ல் அமலுக்கு வந்தது.",
        ["Polity", "Historical Background", "Law Commission", "Macaulay", "Grand Test"], "Understand", 60
    ))

    # Q28: Direct MCQ - Medium - Portfolio System 1861
    questions.append(make_q(
        28, "Medium", "Direct MCQ",
        "Which Governor-General / Viceroy introduced the 'Portfolio System' in 1859, which subsequently received statutory recognition under the Indian Councils Act of 1861?",
        "1859-ல் 'இலாகா முறையை' (Portfolio System) அறிமுகப்படுத்தி, பின்னர் 1861 இந்தியக் கவுன்சில்கள் சட்டத்தின் கீழ் அதற்குச் சட்டப்பூர்வ அங்கீகாரம் பெற்ற தந்த வைஸ்ராய் யார்?",
        [
            ("A", "Lord Canning", "லார்டு கேனிங்"),
            ("B", "Lord Dalhousie", "லார்டு டல்ஹவுசி"),
            ("C", "Lord Mayo", "லார்டு மாயோ"),
            ("D", "Lord Curzon", "லார்டு கர்சன்")
        ],
        "A",
        "Historical Context: Need for administrative efficiency in executive decision-making.\nReason: Lord Canning introduced the portfolio system in 1859. Under this system, a member of the Viceroy's Executive Council was made in-charge of one or more departments and authorized to issue final orders on behalf of the Council. Indian Councils Act 1861 gave statutory recognition to this system.\nConstitutional Impact: Created modern Cabinet system of portfolio division.\nExam Trap: System introduced in 1859 by Canning; statutory approval given in 1861 Act.\nMemory Trick: Portfolio = Canning (1859 intro $\rightarrow$ 1861 Act).",
        "வரலாற்றுப் பின்னணி: நிர்வாக முடிவெடுத்தலில் திறமையைக் கொண்டுவருவதற்கான தேவை.\nகாரணம்: லார்டு கேனிங் 1859-ல் இலாகா முறையை அறிமுகப்படுத்தினார். இம்முறையின் கீழ் வைஸ்ராய் குழுவின் உறுப்பினர் ஒருவர் ஒன்று அல்லது அதற்கு மேற்பட்ட துறைகளுக்குப் பொறுப்பாக்கப்பட்டு கவுன்சில் சார்பில் இறுதி உத்தரவிட அதிகாரம் பெற்றார். 1861 சட்டம் இதற்குச் சட்டப்பூர்வ அங்கீகாரம் அளித்தது.\nஅரசியலமைப்பு தாக்கம்: நவீன கேபினட் அமைச்சரவை முறைக்கு வழிவகுத்தது.\nதேர்வுப் பொறி: 1859-ல் கேனிங் அறிமுகம்; 1861 சட்டத்தில் சட்டப்பூர்வ அங்கீகாரம்.\nநினைவுச் சூத்திரம்: இலாகா முறை = கேனிங் (1859 அறிமுகம் $\rightarrow$ 1861 சட்டம்).",
        {
            "A": {"en": "Correct. Lord Canning introduced Portfolio System in 1859, recognized statutorily in 1861.", "ta": "சரி. லார்டு கேனிங் 1859-ல் இலாகா முறையை அறிமுகப்படுத்தினார், 1861-ல் சட்டப்பூர்வ அங்கீகாரம் பெற்றது."},
            "B": {"en": "Incorrect. Lord Dalhousie introduced telegraph and railway reforms, not Portfolio system.", "ta": "தவறு. லார்டு டல்ஹவுசி தந்தி, ரயில்வே சீர்திருத்தங்களைக் கொண்டுவந்தார்."},
            "C": {"en": "Incorrect. Lord Mayo initiated financial decentralization in 1870.", "ta": "தவறு. லார்டு மாயோ 1870-ல் நிதி பரவலாக்கத்தைத் தொடங்கினார்."},
            "D": {"en": "Incorrect. Lord Curzon was Viceroy during Bengal Partition 1905.", "ta": "தவறு. லார்டு கர்சன் 1905 வங்கப் பிரிவினையின் போது வைஸ்ராயாக இருந்தார்."}
        },
        "TNPSC Trap: Lord Canning was also the Viceroy who introduced Income Tax in India (1860) with Finance Member James Wilson.",
        "TNPSC பொறி: லார்டு கேனிங் நிதி உறுப்பினர் ஜேம்ஸ் வில்சனுடன் இணைந்து 1860-ல் இந்தியாவில் வருமான வரியை அறிமுகப்படுத்திய வைஸ்ராயாவார்.",
        "Portfolio system transformed the Executive Council from a collective board into a Cabinet of departmental ministers.",
        "இலாகா முறை நிர்வாகக் குழுவை ஒரு கூட்டு வாரியத்திலிருந்து துறைசார் அமைச்சர்களின் கேபினட்டாக மாற்றியது.",
        ["Polity", "Historical Background", "Portfolio System", "Lord Canning", "Grand Test"], "Remember", 45
    ))

    # Q29: Multi-Act Comparative - Hard - Legislative Power Centralization & Decentralization
    questions.append(make_q(
        29, "Hard", "Multi-Act Comparative",
        "Which pair of statutory enactments correctly represents the APEX of legislative centralization and the START of legislative decentralization in British India?",
        "பிரிட்டிஷ் இந்தியாவில் சட்ட அதிகாரங்களின் மையமாக்கலின் 'உச்சம்' மற்றும் அதிகாரப் பரவலாக்கலின் 'தொடக்கம்' ஆகியவற்றைச் சரியாகக் குறிப்பிடும் சட்டங்களின் இணை எது?",
        [
            ("A", "Charter Act of 1833 (Apex of Centralization) and Indian Councils Act of 1861 (Start of Decentralization)", "1833 சாசனச் சட்டம் (மையமாக்கலின் உச்சம்) மற்றும் 1861 இந்தியக் கவுன்சில்கள் சட்டம் (பரவலாக்கலின் தொடக்கம்)"),
            ("B", "Regulating Act of 1773 (Apex of Centralization) and Pitt's India Act of 1784 (Start of Decentralization)", "1773 ஒழுங்குமுறைச் சட்டம் (மையமாக்கலின் உச்சம்) மற்றும் 1784 பிட் இந்தியச் சட்டம் (பரவலாக்கலின் தொடக்கம்)"),
            ("C", "Government of India Act 1858 (Apex of Centralization) and Indian Councils Act 1892 (Start of Decentralization)", "1858 இந்திய அரசுச் சட்டம் (மையமாக்கலின் உச்சம்) மற்றும் 1892 இந்தியக் கவுன்சில்கள் சட்டம் (பரவலாக்கலின் தொடக்கம்)"),
            ("D", "Charter Act of 1853 (Apex of Centralization) and Government of India Act 1919 (Start of Decentralization)", "1853 சாசனச் சட்டம் (மையமாக்கலின் உச்சம்) மற்றும் 1919 இந்திய அரசுச் சட்டம் (பரவலாக்கலின் தொடக்கம்)")
        ],
        "A",
        "Historical Context: Legislative power swung from centralization under Company rule to decentralization under Crown rule.\nReason: Charter Act 1833 reached the APEX of legislative centralization by depriving Bombay and Madras Presidencies of all law-making powers and concentrating legislative authority exclusively in the Governor-General of India. Indian Councils Act 1861 STARTED legislative decentralization by restoring law-making powers to Bombay and Madras Presidencies.\nConstitutional Impact: Set off the chain of devolution leading to complete Provincial Autonomy under the 1935 Act.\nExam Trap: Centralization started in 1773, reached apex in 1833. Decentralization started in 1861, culminated in 1935.\nMemory Trick: Apex Centralization = 1833; Start Decentralization = 1861.",
        "வரலாற்றுப் பின்னணி: சட்ட அதிகாரம் கம்பெனி ஆட்சியில் மையமாக்கலை நோக்கியும் முடி ஆட்சியில் பரவலாக்கலை நோக்கியும் இயங்கியது.\nகாரணம்: 1833 சாசனச் சட்டம் பம்பாய், மதராஸ் மாகாணங்களின் அனைத்து சட்ட அதிகாரங்களையும் பறித்து இந்திய கவர்னர்-ஜெனரலிடம் மட்டுமே குவித்ததன் மூலம் மையமாக்கலின் உச்சத்தை அடைந்தது. 1861 இந்தியக் கவுன்சில்கள் சட்டம் அப்பாவகங்களின் சட்ட அதிகாரங்களை மீட்டளித்து அதிகாரப் பரவலாக்கத்தைத் தொடங்கியது.\nஅரசியலமைப்பு தாக்கம்: 1935 சட்டத்தின் முழு மாகாண தன்னாட்சிக்கு வழிவகுத்த அதிகாரப் பரவலாக்கல் தொடக்கம்.\nதேர்வுப் பொறி: மையமாக்கல் 1773-ல் தொடங்கி 1833-ல் உச்சமடைந்தது. பரவலாக்கல் 1861-ல் தொடங்கி 1935-ல் உச்சமடைந்தது.\nநினைவுச் சூத்திரம்: மையமாக்கல் உச்சம் = 1833; பரவலாக்கல் தொடக்கம் = 1861.",
        {
            "A": {"en": "Correct. 1833 was apex of centralization; 1861 started legislative decentralization.", "ta": "சரி. 1833 மையமாக்கலின் உச்சம்; 1861 அதிகாரப் பரவலாக்கத்தின் தொடக்கம்."},
            "B": {"en": "Incorrect. 1773 started centralization, but apex was 1833.", "ta": "தவறு. 1773 மையமாக்கலை மட்டுமே தொடங்கியது."},
            "C": {"en": "Incorrect. 1858 transferred executive power to Crown, 1861 started legislative decentralization.", "ta": "தவறு. 1858 நிர்வாக மாற்றத்தைக் குறித்தது."},
            "D": {"en": "Incorrect. 1853 separated legislative function, did not start decentralization.", "ta": "தவறு. 1853 சட்டப் பணியைப் பிரித்தது."}
        },
        "TNPSC Trap: Decentralization process started by 1861 Act culminated in complete Provincial Autonomy under Government of India Act 1935.",
        "TNPSC பொறி: 1861 சட்டத்தால் தொடங்கப்பட்ட அதிகாரப் பரவலாக்கல் 1935 இந்திய அரசுச் சட்டத்தில் முழு மாகாண தன்னாட்சியாக நிறைவடைந்தது.",
        "1833 Charter Act deprived Madras and Bombay Governors of legislative powers completely.",
        "1833 சாசனச் சட்டம் மதராஸ், பம்பாய் ஆளுநர்களின் சட்ட அதிகாரங்களை முற்றிலும் பறித்தது.",
        ["Polity", "Historical Background", "Centralization vs Decentralization", "Multi-Act Integration", "Grand Test"], "Analyze", 75
    ))

    # Q30: Assertion & Reason - Hard - Indian High Courts Act 1861
    questions.append(make_q(
        30, "Hard", "Assertion & Reason",
        "Assertion (A): The Indian High Courts Act of 1861 led to the merger and abolition of the Supreme Courts of Judicature and the Sadar Adalats in Presidency towns.\nReason (R): It authorized the British Crown to issue Letters Patent establishing High Courts at Calcutta, Bombay, and Madras by unifying dual judicial systems.",
        "கூற்று (A): 1861 ஆம் ஆண்டின் இந்திய உயர் நீதிமன்றங்கள் சட்டம் மாகாண நகரங்களில் இருந்த உச்ச நீதிமன்றங்கள் மற்றும் சதர் அதாலத்துகளை இணைத்து ஒழிப்பதற்கு வழிவகுத்தது.\nகாரணம் (R): இது இரட்டை நீதித்துறை அமைப்புகளை ஒருங்கிணைத்து கொல்கத்தா, பம்பாய், மதராஸ் நகரங்களில் உயர் நீதிமன்றங்களை நிறுவ பிரிட்டிஷ் முடியாட்சிக்கு காப்புரிமைப் பட்டயம் வழங்க அதிகாரமளித்தது.",
        [
            ("A", "Both (A) and (R) are true and (R) is the correct explanation of (A)", "(A) மற்றும் (R) இரண்டும் உண்மை, மேலும் (R) என்பது (A)-வின் சரியான விளக்கமாகும்"),
            ("B", "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கமல்ல"),
            ("C", "(A) is true but (R) is false", "(A) உண்மை, ஆனால் (R) தவறு"),
            ("D", "(A) is false but (R) is true", "(A) தவறு, ஆனால் (R) உண்மை")
        ],
        "A",
        "Historical Context: Before 1861, dual courts existed—Crown Courts (Supreme Courts) in presidency towns and Company Courts (Sadar Diwani & Sadar Nizamat Adalat) in mofussil areas.\nReason: Indian High Courts Act 1861 abolished the Supreme Courts and Sadar Adalats, merging them into unified High Courts established at Calcutta, Bombay, and Madras in 1862. (R) correctly explains (A).\nConstitutional Impact: Created an integrated judicial structure under Crown Rule.\nExam Trap: High Courts Act was passed in 1861; High Courts were actually established in 1862 (Calcutta 1st, then Bombay & Madras).\nMemory Trick: 1861 High Courts Act = Merged Supreme Court + Sadar Adalat into High Court (1862).",
        "வரலாற்றுப் பின்னணி: 1861-க்கு முன் இரட்டை நீதிமன்றங்கள் இருந்தன—மாகாண நகரங்களில் முடி நீதிமன்றங்கள் (உச்ச நீதிமன்றங்கள்) மற்றும் கிராமப்புறங்களில் கம்பெனி நீதிமன்றங்கள் (சதர் திவானி & சதர் நிசாமத் அதாலத்).\nகாரணம்: 1861 உயர் நீதிமன்றங்கள் சட்டம் உச்ச நீதிமன்றங்கள் மற்றும் சதர் அதாலத்துகளை ஒழித்து, அவற்றை 1862-ல் கொல்கத்தா, பம்பாய், மதராஸ் நகரங்களில் ஒருங்கிணைந்த உயர் நீதிமன்றங்களாக அமைத்தது. (R) என்பது (A)-வின் சரியான விளக்கம்.\nஅரசியலமைப்பு தாக்கம்: முடி ஆட்சியின் கீழ் ஒருங்கிணைக்கப்பட்ட நீதித்துறை அமைப்பை உருவாக்கியது.\nதேர்வுப் பொறி: உயர் நீதிமன்றச் சட்டம் நிறைவேற்றப்பட்டது 1861; உயர் நீதிமன்றங்கள் உண்மையில் அமைந்தது 1862 (1வது கொல்கத்தா, பிறகு பம்பாய் & மதராஸ்).\nநினைவுச் சூத்திரம்: 1861 உயர் நீதிமன்ற சட்டம் = உச்ச நீதிமன்றம் + சதர் அதாலத் = உயர் நீதிமன்றம் (1862).",
        {
            "A": {"en": "Correct. (R) correctly explains why Supreme Courts and Sadar Adalats were abolished.", "ta": "சரி. உச்ச நீதிமன்றங்களும் சதர் அதாலத்துகளும் ஏன் ஒழிக்கப்பட்டன என்பதை (R) சரியாக விளக்குகிறது."},
            "B": {"en": "Incorrect. Reason directly explains the Assertion.", "ta": "தவறு. காரணம் கூற்றை நேரடியாக விளக்குகிறது."},
            "C": {"en": "Incorrect. Reason is true.", "ta": "தவறு. காரணம் உண்மையானது."},
            "D": {"en": "Incorrect. Assertion is true.", "ta": "தவறு. கூற்று உண்மையானது."}
        },
        "TNPSC Trap: Calcutta High Court was established first on July 2, 1862; Bombay on August 14, 1862; Madras on August 15, 1862.",
        "TNPSC பொறி: கொல்கத்தா உயர் நீதிமன்றம் முதலில் ஜூலை 2, 1862-லும்; பம்பாய் ஆகஸ்ட் 14, 1862-லும்; மதராஸ் ஆகஸ்ட் 15, 1862-லும் அமைக்கப்பட்டன.",
        "Allahabad High Court was established fourth in 1866 (originally at Agra).",
        "அலகாபாத் உயர் நீதிமன்றம் நான்காவதாக 1866-ல் அமைக்கப்பட்டது (முதலில் ஆக்ராவில்).",
        ["Polity", "Historical Background", "Indian High Courts Act 1861", "Judiciary", "Grand Test"], "Evaluate", 90
    ))

    # Q31: Conceptual MCQ - Medium - Government of India Act 1935 Bicameralism
    questions.append(make_q(
        31, "Medium", "Conceptual MCQ",
        "Under the Government of India Act of 1935, bicameral legislatures were introduced in how many out of the eleven Indian Provinces?",
        "1935 ஆம் ஆண்டின் இந்திய அரசுச் சட்டத்தின் கீழ், பதினொரு இந்திய மாகாணங்களில் எத்தனை மாகாணங்களில் இரு அவை சட்டமன்றங்கள் அறிமுகப்படுத்தப்பட்டன?",
        [
            ("A", "Six Provinces (Bengal, Bombay, Madras, Bihar, Assam, and United Provinces)", "ஆறு மாகாணங்கள் (வங்காளம், பம்பாய், மதராஸ், பீகார், அசாம் மற்றும் ஐக்கிய மாகாணங்கள்)"),
            ("B", "All Eleven Provinces", "அனைத்து 11 மாகாணங்கள்"),
            ("C", "Three Presidencies only (Bengal, Bombay, and Madras)", "மூன்று மாகாண நகரங்கள் மட்டுமே (வங்காளம், பம்பாய் மற்றும் மதராஸ்)"),
            ("D", "Five Provinces (Punjab, Sindh, NWFP, CP & Berar, and Orissa)", "ஐந்து மாகாணங்கள் (பஞ்சாப், சிந்து, வடமேற்கு எல்லைப்புற மாகாணம், சி.பி & பேரார், ஒரிசா)")
        ],
        "A",
        "Historical Context: Expanding legislative structural complexity in major provinces under 1935 Act.\nReason: The 1935 Act introduced bicameralism (Legislative Assembly and Legislative Council) in 6 out of 11 provinces: Bengal, Bombay, Madras, Bihar, Assam, and United Provinces. The remaining 5 provinces remained unicameral.\nConstitutional Impact: Structural foundation for bicameral state legislatures in modern India (Article 169).\nExam Trap: Central bicameralism = 1919 Act; Provincial bicameralism in 6 provinces = 1935 Act.\nMemory Trick: 1935 Provincial Bicameralism = 6/11 (3 Presidencies + Bihar, Assam, UP).",
        "வரலாற்றுப் பின்னணி: 1935 சட்டத்தின் கீழ் முக்கிய மாகாணங்களில் சட்டமன்றக் கட்டமைப்பை விரிவாக்குதல்.\nகாரணம்: 1935 சட்டம் 11-ல் 6 மாகாணங்களில் இரு அவை முறையை (சட்டமன்ற மேலவை & சட்டமன்ற பேரவை) அறிமுகப்படுத்தியது: வங்காளம், பம்பாய், மதராஸ், பீகார், அசாம், ஐக்கிய மாகாணங்கள். மீதமுள்ள 5 மாகாணங்கள் ஓரவையாகவே தொடர்ந்தன.\nஅரசியலமைப்பு தாக்கம்: நவீன இந்தியாவில் மாநில இரு அவை சட்டமன்றங்களுக்கு (சரத்து 169) கட்டமைப்பு அடித்தளம்.\nதேர்வுப் பொறி: மத்திய இரு அவை முறை = 1919 சட்டம்; 6 மாகாணங்களில் இரு அவை முறை = 1935 சட்டம்.\nநினைவுச் சூத்திரம்: 1935 மாகாண இரு அவை முறை = 6/11 (3 மாகாணங்கள் + பீகார், அசாம், UP).",
        {
            "A": {"en": "Correct. Introduced bicameralism in 6 out of 11 provinces: Bengal, Bombay, Madras, Bihar, Assam, UP.", "ta": "சரி. 11-ல் 6 மாகாணங்களில் இரு அவை முறையைக் கொண்டுவந்தது: வங்காளம், பம்பாய், மதராஸ், பீகார், அசாம், UP."},
            "B": {"en": "Incorrect. Only 6 provinces were bicameral, 5 were unicameral.", "ta": "தவறு. 6 மாகாணங்கள் மட்டுமே இரு அவை முறையைக் கொண்டிருந்தன."},
            "C": {"en": "Incorrect. Bihar, Assam, and UP were also bicameral, making total 6.", "ta": "தவறு. பீகார், அசாம், UP ஆகியவையும் சேர்த்து மொத்தம் 6."},
            "D": {"en": "Incorrect. Punjab, Sindh, NWFP, CP, Orissa were unicameral.", "ta": "தவறு. பஞ்சாப், சிந்து, வடமேற்கு மாகாணம் போன்றவை ஓரவை அமைப்புகள்."}
        },
        "TNPSC Trap: Punjab and Central Provinces (CP & Berar) remained UNICAMERAL under 1935 Act.",
        "TNPSC பொறி: 1935 சட்டத்தின் கீழ் பஞ்சாப் மற்றும் மத்திய மாகாணங்கள் (CP & Berar) ஓரவை அமைப்பாகவே தொடர்ந்தன.",
        "1935 Act created Federal Legislature consisting of Council of States and Federal Assembly.",
        "1935 சட்டம் மாநிலங்கள் குழு மற்றும் கூட்டாட்சி பேரவை கொண்ட கூட்டாட்சி சட்டமன்றத்தை உருவாக்கியது.",
        ["Polity", "Historical Background", "GOI Act 1935", "Provincial Bicameralism", "Grand Test"], "Understand", 60
    ))

    # Q32: Direct MCQ - Medium - Simon Commission Recommendations
    questions.append(make_q(
        32, "Medium", "Direct MCQ",
        "Which of the following was NOT recommended by the Simon Commission in its 1930 Report?",
        "1930 ஆம் ஆண்டின் தனது அறிக்கையில் சைமன் குழுவால் பரிந்துரைக்கப்படாதது எது?",
        [
            ("A", "Establishment of a Dyarchical system at the Central level", "மத்திய மட்டத்தில் இரட்டை ஆட்சி முறையை நிறுவுதல்"),
            ("B", "Abolition of Dyarchy in Indian Provinces and establishment of Provincial Autonomy", "இந்திய மாகாணங்களில் இரட்டை ஆட்சியை ஒழித்து மாகாண தன்னாட்சியை நிறுவுதல்"),
            ("C", "Continuation of Communal Electorates for religious minorities", "மத சிறுபான்மையினருக்கான வகுப்புவாத தொகுதிகளைத் தொடர்ந்து நீடித்தல்"),
            ("D", "Establishment of a Federation of British India and Princely States", "பிரிட்டிஷ் இந்தியா மற்றும் சுதேச சமஸ்தானங்களின் கூட்டாட்சியை நிறுவுதல்")
        ],
        "A",
        "Historical Context: Simon Commission report (1930) made major recommendations for future constitutional reforms.\nReason: Simon Commission recommended: (1) Abolition of provincial Dyarchy, (2) Establishment of provincial autonomy, (3) Continuation of communal electorate, (4) Federation of British India and Princely States. It did NOT recommend Dyarchy at the Center.\nConstitutional Impact: Rejection of central Dyarchy; central Dyarchy was later proposed independently by GOI Act 1935.\nExam Trap: Simon Commission opposed Dyarchy everywhere, including at the Center.\nMemory Trick: Simon Commission = NO Dyarchy (Abolish Provincial Dyarchy, No Central Dyarchy).",
        "வரலாற்றுப் பின்னணி: சைமன் குழு அறிக்கை (1930) எதிர்கால அரசியலமைப்பு சீர்திருத்தங்களுக்கு முக்கிய பரிந்துரைகளை அளித்தது.\nகாரணம்: சைமன் குழு பரிந்துரைத்தவை: (1) மாகாண இரட்டை ஆட்சி ஒழிப்பு, (2) மாகாண தன்னாட்சி அமைப்பு, (3) வகுப்புவாத தொகுதி நீடிப்பு, (4) பிரிட்டிஷ் இந்தியா-சுதேச சமஸ்தானங்களின் கூட்டாட்சி. இது மத்திய இரட்டை ஆட்சியைப் பரிந்துரைக்கவில்லை.\nஅரசியலமைப்பு தாக்கம்: மத்திய இரட்டை ஆட்சியை நிராகரித்தல்; மத்திய இரட்டை ஆட்சி பின்னர் 1935 சட்டத்தால் சுதந்திரமாக முன்மொழியப்பட்டது.\nதேர்வுப் பொறி: சைமன் குழு இரட்டை ஆட்சியை அனைத்து மட்டங்களிலும் எதிர்த்தது.\nநினைவுச் சூத்திரம்: சைமன் குழு = இரட்டை ஆட்சி இல்லை (மாகாண இரட்டை ஆட்சி ஒழிப்பு, மத்திய இரட்டை ஆட்சி நிராகரிப்பு).",
        {
            "A": {"en": "Correct option (NOT recommended). Simon Commission did not recommend Dyarchy at Center.", "ta": "சரி (பரிந்துரைக்கப்படாதது). சைமன் குழு மத்தியில் இரட்டை ஆட்சியைப் பரிந்துரைக்கவில்லை."},
            "B": {"en": "Incorrect. Abolition of provincial Dyarchy was recommended by Simon Commission.", "ta": "தவறு. மாகாண இரட்டை ஆட்சி ஒழிப்பு பரிந்துரைக்கப்பட்டது."},
            "C": {"en": "Incorrect. Continuation of communal electorate was recommended.", "ta": "தவறு. வகுப்புவாத தொகுதி நீடிப்பு பரிந்துரைக்கப்பட்டது."},
            "D": {"en": "Incorrect. Federation of British India and Princely States was recommended.", "ta": "தவறு. கூட்டாட்சி அமைப்பு பரிந்துரைக்கப்பட்டது."}
        },
        "TNPSC Trap: Simon Commission report (1930) led to 3 Round Table Conferences (1930-32) and the White Paper on Constitutional Reforms (1933).",
        "TNPSC பொறி: சைமன் குழு அறிக்கை (1930) 3 வட்டமேஜை மாநாடுகள் (1930-32) மற்றும் 1933 வெள்ளை அறிக்கைக்கு வழிவகுத்தது.",
        "Simon Commission comprised 7 members from British Parliament, chaired by Sir John Simon.",
        "சைமன் குழு சர் ஜான் சைமன் தலைமையில் பிரிட்டிஷ் நாடாளுமன்றத்தின் 7 உறுப்பினர்களைக் கொண்டிருந்தது.",
        ["Polity", "Historical Background", "Simon Commission 1927", "Grand Test"], "Understand", 60
    ))

    # Q33: Statement Based - Hard - Government of India Act 1935 Federal Court & Institutions
    questions.append(make_q(
        33, "Hard", "Statement Based",
        "Consider the following statements regarding institutions established under the Government of India Act of 1935:\n1. It provided for the establishment of a Federal Court, which was set up in 1937 in Delhi with one Chief Justice and not more than six puisne judges.\n2. The Federal Court had exclusive original jurisdiction in disputes between the Federation and its constituent units.\n3. Appeals from the Federal Court could be taken to the Judicial Committee of the Privy Council in London in specified circumstances.\n4. It established the Reserve Bank of India to control the currency and credit of the country.\nWhich of the statements given above are correct?",
        "1935 இந்திய அரசுச் சட்டத்தின் கீழ் நிறுவப்பட்ட நிறுவனங்கள் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது ஒரு கூட்டாட்சி நீதிமன்றத்தை அமைக்க வழிவகுத்தது, அது 1937-ல் டெல்லியில் ஒரு தலைமை நீதிபதி மற்றும் ஆறுக்கு மிகாத நீதிபதிகளுடன் அமைந்தது.\n2. கூட்டாட்சி மற்றும் அதன் உறுப்பு அலகுகளுக்கிடையேயான தகராறுகளில் கூட்டாட்சி நீதிமன்றம் தனித்துவமான முதன்மை அதிகார வரம்பைக் கொண்டிருந்தது.\n3. கூட்டாட்சி நீதிமன்றத் தீர்ப்புகளுக்கு எதிராக லண்டனில் உள்ள ப்ரிவி கவுன்சிலின் நீதித்துறை குழுவிற்கு மேல்முறையீடு செய்ய வழி இருந்தது.\n4. நாட்டின் நாணயம் மற்றும் கடனைக் கட்டுப்படுத்த இது இந்திய ரிசர்வ் வங்கியை நிறுவியது.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
        [
            ("A", "1, 2, 3 and 4", "1, 2, 3 மற்றும் 4"),
            ("B", "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டுமே"),
            ("C", "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டுமே"),
            ("D", "1 and 4 only", "1 மற்றும் 4 மட்டுமே")
        ],
        "A",
        "Historical Context: The 1858-1935 evolution introduced institutional machinery essential for a federal nation-state.\nReason: All four statements are correct. Federal Court set up in 1937 (1 Chief Justice Sir Maurice Gwyer + max 6 judges), had original federal jurisdiction, appeals went to Privy Council. RBI was set up under RBI Act 1934 following 1935 framework recommendations.\nConstitutional Impact: Federal Court served as precursor to Supreme Court of India (1950).\nExam Trap: Federal Court was NOT the highest court of appeal; Privy Council in London remained supreme appellate authority until 1949.\nMemory Trick: 1935 Institutions = Federal Court (1937) + RBI (1935) + FPSC + PPSC.",
        "வரலாற்றுப் பின்னணி: 1858-1935 வளர்ச்சி ஒரு கூட்டாட்சி நாட்டின் அமைப்பிற்கான நிறுவனங்களை நிறுவியது.\nகாரணம்: நான்கு கூற்றுகளும் சரியானவை. 1937-ல் கூட்டாட்சி நீதிமன்றம் அமைக்கப்பட்டது (1 தலைமை நீதிபதி சர் மோரிஸ் குவையர் + அதிகபட்சம் 6 நீதிபதிகள்), இது முதன்மை அதிகார வரம்பைக் கொண்டிருந்தது, மேல்முறையீடு ப்ரிவி கவுன்சிலுக்குச் சென்றது. ரிசர்வ் வங்கியும் இச்சட்டத்தின் சட்டகத்தால் அமைக்கப்பட்டது.\nஅரசியலமைப்பு தாக்கம்: கூட்டாட்சி நீதிமன்றமே 1950-ல் அமைந்த இந்திய உச்ச நீதிமன்றத்திற்கு முன்னோடியாகும்.\nதேர்வுப் பொறி: கூட்டாட்சி நீதிமன்றம் மிக உயர்ந்த மேல்முறையீட்டு நீதிமன்றமல்ல; லண்டன் ப்ரிவி கவுன்சிலே 1949 வரை உச்ச மேல்முறையீட்டு அதிகாரத்தைக் கொண்டிருந்தது.\nநினைவுச் சூத்திரம்: 1935 நிறுவனங்கள் = கூட்டாட்சி நீதிமன்றம் (1937) + RBI (1935) + FPSC.",
        {
            "A": {"en": "Correct. All four statements accurately state statutory institution provisions of 1935 Act.", "ta": "சரி. நான்கு கூற்றுகளும் 1935 சட்டத்தின் நிறுவன விதிகளைத் துல்லியமாக விவரிக்கின்றன."},
            "B": {"en": "Incorrect. Statement 4 is also correct.", "ta": "தவறு. கூற்று 4-ம் சரியானது."},
            "C": {"en": "Incorrect. Statement 1 is also correct.", "ta": "தவறு. கூற்று 1-ம் சரியானது."},
            "D": {"en": "Incorrect. Statements 2 and 3 are also correct.", "ta": "தவறு. கூற்றுகள் 2 மற்றும் 3-ம் சரியானவை."}
        },
        "TNPSC Trap: Sir Maurice Gwyer was the first Chief Justice of the Federal Court of India (1937).",
        "TNPSC பொறி: சர் மோரிஸ் குவையர் இந்தியாவின் கூட்டாட்சி நீதிமன்றத்தின் முதல் தலைமை நீதிபதியாவார் (1937).",
        "Abolition of Privy Council Jurisdiction Act was passed in India in 1949, making Supreme Court the ultimate appellate court in 1950.",
        "1949-ல் ப்ரிவி கவுன்சில் அதிகார வரம்பு ஒழிப்புச் சட்டம் நிறைவேற்றப்பட்டு 1950-ல் இந்திய உச்ச நீதிமன்றம் இறுதி மேல்முறையீட்டு மன்றமானது.",
        ["Polity", "Historical Background", "GOI Act 1935", "Federal Court", "RBI", "Grand Test"], "Analyze", 75
    ))

    # Q34: Multi-Act Comparative - Hard - Evolution of Bicameralism
    questions.append(make_q(
        34, "Hard", "Multi-Act Comparative",
        "Which distinction accurately separates the introduction of Central Bicameralism under the 1919 Act from Provincial Bicameralism under the 1935 Act?",
        "1919 சட்டத்தின் கீழ் மத்திய இரு அவை முறை அறிமுகமானதையும் 1935 சட்டத்தின் கீழ் மாகாண இரு அவை முறை அறிமுகமானதையும் துல்லியமாக வேறுபடுத்தும் கூற்று எது?",
        [
            ("A", "The 1919 Act introduced bicameralism at the Central level (Council of State & Central Legislative Assembly), whereas the 1935 Act introduced bicameralism in 6 out of 11 Provinces.", "1919 சட்டம் மத்திய மட்டத்தில் இரு அவை முறையை (மாநிலங்கள் குழு & மத்திய சட்டமன்றம்) அறிமுகப்படுத்தியது; ஆனால் 1935 சட்டம் 11-ல் 6 மாகாணங்களில் இரு அவை முறையை அறிமுகப்படுத்தியது."),
            ("B", "The 1919 Act introduced bicameralism in Provinces, whereas the 1935 Act introduced bicameralism at the Center.", "1919 சட்டம் மாகாணங்களில் இரு அவை முறையை அறிமுகப்படுத்தியது; ஆனால் 1935 சட்டம் மத்தியில் இரு அவை முறையை அறிமுகப்படுத்தியது."),
            ("C", "The 1919 Act created a three-chamber central parliament, while the 1935 Act abolished upper houses in all provinces.", "1919 சட்டம் மூன்று அவைகளைக் கொண்ட மத்திய நாடாளுமன்றத்தை உருவாக்கியது; 1935 சட்டம் அனைத்து மாகாண மேலவைகளையும் ஒழித்தது."),
            ("D", "The 1919 Act made all provincial chambers bicameral, while the 1935 Act merged them into unicameral bodies.", "1919 சட்டம் அனைத்து மாகாண அவைகளையும் இரு அவைகளாக்கியது; 1935 சட்டம் அவற்றை ஓரவை அமைப்புகளாக மாற்றியது.")
        ],
        "A",
        "Historical Context: Gradual introduction of dual-chamber parliamentary structures at central and regional levels.\nReason: 1919 Act established Central Bicameralism (Council of State & Central Legislative Assembly). 1935 Act extended bicameralism to the provinces, establishing Upper & Lower houses in 6 provinces (Bengal, Bombay, Madras, Bihar, Assam, UP).\nConstitutional Impact: Created modern bicameral parliament and state legislatures in India.\nExam Trap: Do not mix 1919 Central Bicameralism with 1935 Provincial Bicameralism.\nMemory Trick: 1919 = Center Bicameral; 1935 = 6 Provinces Bicameral.",
        "வரலாற்றுப் பின்னணி: மத்திய மற்றும் மாகாண மட்டங்களில் இரு அவை நாடாளுமன்ற அமைப்புகளைப் படிப்படியாக அறிமுகப்படுத்துதல்.\nகாரணம்: 1919 சட்டம் மத்திய இரு அவை முறையை நிறுவியது (மாநிலங்கள் குழு & மத்திய சட்ட பேரவை). 1935 சட்டம் இரு அவை முறையை மாகாணங்களுக்கு விரிவுபடுத்தி 6 மாகாணங்களில் மேலவை, கீழவைகளை அமைத்தது.\nஅரசியலமைப்பு தாக்கம்: நவீன இந்தியாவில் இரு அவை நாடாளுமன்றம் மற்றும் மாநில சட்டப்பேரவைகளை உருவாக்கியது.\nதேர்வுப் பொறி: 1919 மத்திய இரு அவை முறையை 1935 மாகாண இரு அவை முறையுடன் குழப்பக் கூடாது.\nநினைவுச் சூத்திரம்: 1919 = மத்திய இரு அவை; 1935 = 6 மாகாணங்களில் இரு அவை.",
        {
            "A": {"en": "Correct. 1919 introduced Central bicameralism; 1935 introduced Provincial bicameralism in 6 provinces.", "ta": "சரி. 1919 மத்திய இரு அவை முறையையும்; 1935 6 மாகாணங்களில் இரு அவை முறையையும் கொண்டுவந்தன."},
            "B": {"en": "Incorrect. Reverses the two Acts.", "ta": "தவறு. இரண்டு சட்டங்களையும் தலைகீழாக மாற்றுகிறது."},
            "C": {"en": "Incorrect. Neither Act created a three-chamber parliament.", "ta": "தவறு. எந்தச் சட்டமும் மூன்று அவைகளை உருவாக்கவில்லை."},
            "D": {"en": "Incorrect. 1919 did not make provincial chambers bicameral.", "ta": "தவறு. 1919 மாகாண அவைகளை இரு அவைகளாக்கவில்லை."}
        },
        "TNPSC Trap: Indian Legislative Council created in 1853 was unicameral; Central Legislature became bicameral in 1919 Act.",
        "TNPSC பொறி: 1853-ல் உருவான மத்திய சட்ட மேலவை ஓரவை அமைப்பாக இருந்தது; 1919 சட்டத்திலேயே அது இரு அவை அமைப்பானது.",
        "Council of State under 1919 Act had a 5-year tenure, while Legislative Assembly had a 3-year tenure.",
        "1919 சட்டத்தின் கீழ் மாநிலங்கள் குழு 5 ஆண்டு ஆயுளையும், சட்ட பேரவை 3 ஆண்டு ஆயுளையும் கொண்டிருந்தன.",
        ["Polity", "Historical Background", "Bicameralism Evolution", "Multi-Act Integration", "Grand Test"], "Analyze", 75
    ))

    # Q35: Direct MCQ - Easy - Regulating Act Supreme Court Year Trap
    questions.append(make_q(
        35, "Easy", "Direct MCQ",
        "The Supreme Court of Judicature at Fort William in Calcutta was provided for by the Regulating Act of 1773. In which exact year was it actually established?",
        "1773 ஆம் ஆண்டின் ஒழுங்குமுறைச் சட்டத்தின் கீழ் கொல்கத்தா வில்லியம் கோட்டையில் உச்ச நீதிமன்றம் அமைக்க வழிவகை செய்யப்பட்டது. அது எந்த ஆண்டில் அதிகாரப்பூர்வமாக அமைக்கப்பட்டது?",
        [
            ("A", "1774", "1774"),
            ("B", "1773", "1773"),
            ("C", "1781", "1781"),
            ("D", "1784", "1784")
        ],
        "A",
        "Historical Context: Passage of enactment vs actual date of institutional creation.\nReason: Regulating Act was passed in 1773; Supreme Court at Fort William was actually constituted and opened in 1774 with Sir Elijah Impey as its first Chief Justice.\nConstitutional Impact: First independent judicial body in British India.\nExam Trap: Act year = 1773; Establishment year = 1774.\nMemory Trick: Regulating Act 1773 $\rightarrow$ Supreme Court 1774.",
        "வரலாற்றுப் பின்னணி: சட்டம் இயற்றப்பட்ட ஆண்டும் நிறுவனம் அமைக்கப்பட்ட ஆண்டும் வேறானவை.\nகாரணம்: ஒழுங்குமுறைச் சட்டம் 1773-ல் நிறைவேற்றப்பட்டது; வில்லியம் கோட்டை உச்ச நீதிமன்றம் உண்மையில் 1774-ல் சர் எலிஜா இம்பே முதல் தலைமை நீதிபதியாகக் கொண்டு அமைக்கப்பட்டது.\nஅரசியலமைப்பு தாக்கம்: பிரிட்டிஷ் இந்தியாவின் முதல் சுதந்திரமான நீதித்துறை அமைப்பு.\nதேர்வுப் பொறி: சட்டம் = 1773; அமைக்கப்பட்ட ஆண்டு = 1774.\nநினைவுச் சூத்திரம்: 1773 ஒழுங்குமுறை சட்டம் $\rightarrow$ 1774 உச்ச நீதிமன்றம்.",
        {
            "A": {"en": "Correct. Supreme Court Fort William was established in 1774 under 1773 Act.", "ta": "சரி. வில்லியம் கோட்டை உச்ச நீதிமன்றம் 1773 சட்டத்தின்கீழ் 1774-ல் அமைக்கப்பட்டது."},
            "B": {"en": "Incorrect. 1773 was the year the Act was passed in British Parliament.", "ta": "தவறு. 1773 சட்டம் நிறைவேற்றப்பட்ட ஆண்டாகும்."},
            "C": {"en": "Incorrect. 1781 was the Amending Act (Act of Settlement).", "ta": "தவறு. 1781 திருத்தச் சட்டம் இயற்றப்பட்ட ஆண்டாகும்."},
            "D": {"en": "Incorrect. 1784 was Pitt's India Act.", "ta": "தவறு. 1784 பிட் இந்தியச் சட்டம்."}
        },
        "TNPSC Trap: Sir Elijah Impey was the first Chief Justice of the Supreme Court at Calcutta established in 1774.",
        "TNPSC பொறி: 1774-ல் அமைக்கப்பட்ட கொல்கத்தா உச்ச நீதிமன்றத்தின் முதல் தலைமை நீதிபதி சர் எலிஜா இம்பே ஆவார்.",
        "Supreme Court at Calcutta comprised 1 Chief Justice and 3 other judges in 1774.",
        "1774-ல் கொல்கத்தா உச்ச நீதிமன்றம் 1 தலைமை நீதிபதி மற்றும் 3 நீதிபதிகளைக் கொண்டிருந்தது.",
        ["Polity", "Historical Background", "Regulating Act 1773", "Supreme Court 1774", "Grand Test"], "Remember", 45
    ))

    # Q36: Chronology - Medium - Sequence of Franchise Extensions
    questions.append(make_q(
        36, "Medium", "Chronology",
        "Arrange the following electoral franchise and representation extensions in correct chronological order:\n1. Introduction of indirect recommendation for non-officials in legislative councils\n2. Granting of separate electorates for Depressed Classes, Women, and Labour\n3. Granting of separate electorates for Muslims\n4. Introduction of direct elections for voting based on property, tax, and education",
        "பின்வரும் தேர்தல் வாக்குரிமை மற்றும் பிரதிநிதித்துவ விரிவாக்கங்களை சரியான காலவரிசையில் அமைக்கவும்:\n1. சட்ட மேலவைகளில் அதிகாரப்பூர்வமற்ற உறுப்பினர்களுக்கு மறைமுகப் பரிந்துரை முறையை அறிமுகப்படுத்துதல்\n2. ஒடுக்கப்பட்ட வகுப்பினர், பெண்கள் மற்றும் தொழிலாளர்களுக்குத் தனித் தொகுதிகளை வழங்குதல்\n3. முஸ்லிம்களுக்குத் தனித் தொகுதிகளை வழங்குதல்\n4. சொத்து, வரி, கல்வி அடிப்படையில் வாக்களிக்க நேரடித் தேர்தலை அறிமுகப்படுத்துதல்",
        [
            ("A", "1 -> 3 -> 4 -> 2", "1 -> 3 -> 4 -> 2"),
            ("B", "3 -> 1 -> 4 -> 2", "3 -> 1 -> 4 -> 2"),
            ("C", "1 -> 4 -> 3 -> 2", "1 -> 4 -> 3 -> 2"),
            ("D", "1 -> 3 -> 2 -> 4", "1 -> 3 -> 2 -> 4")
        ],
        "A",
        "Historical Context: Progressive expansion of franchise from indirect recommendation to direct limited vote and communal reservation.\nReason: Correct sequence: 1 (1892 Indirect recommendation) $\rightarrow$ 3 (1909 Separate electorates for Muslims) $\rightarrow$ 4 (1919 Direct elections with restricted franchise) $\rightarrow$ 2 (1935 Extended separate electorates to Depressed Classes, Women, Labour).\nConstitutional Impact: Democratic franchise expanded step-by-step under Crown rule.\nExam Trap: Indirect recommendation = 1892; Muslim electorate = 1909; Direct vote = 1919; Depressed classes = 1935.\nMemory Trick: 1892 (Indirect) $\rightarrow$ 1909 (Muslim Electorate) $\rightarrow$ 1919 (Direct Vote) $\rightarrow$ 1935 (Depressed/Women).",
        "வரலாற்றுப் பின்னணி: மறைமுகப் பரிந்துரையிலிருந்து நேரடி வரம்பிற்குட்பட்ட வாக்குரிமை மற்றும் வகுப்புவாத ஒதுக்கீடு வரை வாக்குரிமை விரிவாக்கம்.\nகாரணம்: சரியான வரிசை: 1 (1892 மறைமுகப் பரிந்துரை) $\rightarrow$ 3 (1909 முஸ்லிம்களுக்குத் தனித் தொகுதி) $\rightarrow$ 4 (1919 நேரடித் தேர்தல்) $\rightarrow$ 2 (1935 ஒடுக்கப்பட்டோர், பெண்கள், தொழிலாளர் தனித் தொகுதி).\nஅரசியலமைப்பு தாக்கம்: முடி ஆட்சியில் ஜனநாயக வாக்குரிமை படிப்படியாக விரிவடைந்தது.\nதேர்வுப் பொறி: மறைமுகப் பரிந்துரை = 1892; முஸ்லிம் தொகுதி = 1909; நேரடி வாக்கு = 1919; ஒடுக்கப்பட்டோர் = 1935.\nநினைவுச் சூத்திரம்: 1892 (மறைமுகம்) $\rightarrow$ 1909 (முஸ்லிம் தொகுதி) $\rightarrow$ 1919 (நேரடி வாக்கு) $\rightarrow$ 1935 (ஒடுக்கப்பட்டோர்/பெண்கள்).",
        {
            "A": {"en": "Correct sequence matching enactment dates: 1892 -> 1909 -> 1919 -> 1935.", "ta": "சரி. சட்ட ஆண்டுகள்: 1892 -> 1909 -> 1919 -> 1935."},
            "B": {"en": "Incorrect. 1892 recommendation (1) came before 1909 Muslim electorate (3).", "ta": "தவறு. 1892 பரிந்துரை (1) 1909-க்கு முந்தியது."},
            "C": {"en": "Incorrect. 1909 Muslim electorate (3) came before 1919 direct vote (4).", "ta": "தவறு. 1909 (3) 1919-க்கு (4) முந்தியது."},
            "D": {"en": "Incorrect. 1935 extension (2) came after 1919 direct vote (4).", "ta": "தவறு. 1935 விரிவாக்கம் (2) 1919-க்கு பிந்தியது."}
        },
        "TNPSC Trap: Government of India Act 1935 extended voting rights to about 14% of the total population of British India.",
        "TNPSC பொறி: 1935 இந்திய அரசுச் சட்டம் பிரிட்டிஷ் இந்தியாவின் மொத்த மக்கள் தொகையில் சுமார் 14% பேருக்கு வாக்குரிமை அளித்தது.",
        "Communal Award of 1932 by Ramsay MacDonald was incorporated into the Government of India Act 1935 with Poona Pact modifications.",
        "1932 ராம்சே மெக்டொனால்டின் வகுப்புவாத கொடை பூனா ஒப்பந்த திருத்தங்களுடன் 1935 சட்டத்தில் இணைக்கப்பட்டது.",
        ["Polity", "Historical Background", "Franchise Expansion", "Chronology", "Grand Test"], "Analyze", 75
    ))

    # Q37: Statement Based - Hard - Government of India Act 1919 Central Executive & Legislature
    questions.append(make_q(
        37, "Hard", "Statement Based",
        "Consider the following statements regarding the Central Government under the Government of India Act of 1919:\n1. The Governor-General retained full executive authority and was not made responsible to the Central Legislature.\n2. Three of the six members of the Viceroy's Executive Council (other than the Commander-in-Chief) were to be Indian.\n3. The Central Legislature was given full power to vote on all financial demands without any Governor-General restore authority.\nWhich of the statements given above is/are correct?",
        "1919 இந்திய அரசுச் சட்டத்தின் கீழ் மத்திய அரசு பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. கவர்னர்-ஜெனரல் முழு நிர்வாக அதிகாரத்தையும் தக்கவைத்துக்கொண்டார், மேலும் மத்திய சட்டமன்றத்திற்குப் பொறுப்பாக்கப்படவில்லை.\n2. வைஸ்ராயின் நிர்வாகக் குழுவின் ஆறு உறுப்பினர்களில் மூவர் (கமாண்டர்-இன்-சீஃப் தவிர) இந்தியர்களாக இருக்க வேண்டும்.\n3. கவர்னர்-ஜெனரலின் மீட்டெடுக்கும் அதிகாரமின்றி அனைத்து நிதி மானியக் கோரிக்கைகளுக்கும் வாக்களிக்கும் முழு அதிகாரமும் மத்திய சட்டமன்றத்திற்கு வழங்கப்பட்டது.\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானவை?",
        [
            ("A", "1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
            ("B", "2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
            ("C", "1 and 3 only", "1 மற்றும் 3 மட்டுமே"),
            ("D", "1, 2 and 3", "1, 2 மற்றும் 3")
        ],
        "A",
        "Historical Context: Montagu-Chelmsford Reforms maintained central autocracy while granting limited responsiveness.\nReason: Statements 1 and 2 are correct. 3 of 6 executive council members were Indian (e.g., Sir Tej Bahadur Sapru). Statement 3 is incorrect because the Governor-General retained veto power and the power of 'certification' to restore any grant rejected by the Central Legislature.\nConstitutional Impact: Retained central executive autocracy despite legislative expansion.\nExam Trap: Executive council had 3 Indian members out of 6, but Commander-in-Chief was distinct.\nMemory Trick: 1919 Central Executive = 3/6 Indians + GG Veto/Certification power.",
        "வரலாற்றுப் பின்னணி: மாண்டேகு-செம்ஸ்ஃபோர்டு சீர்திருத்தங்கள் சட்டமன்றத்தை விரிவுபடுத்தினாலும் மத்திய தன்னாதிக்கத்தைத் தக்கவைத்தன.\nகாரணம்: கூற்றுகள் 1 மற்றும் 2 சரியானவை. 6 நிர்வாகக் குழு உறுப்பினர்களில் 3 பேர் இந்தியர்களாவர் (எ.கா. சர் தேஜ் பகதூர் சப்ரு). கூற்று 3 தவறானது, ஏனெனில் மத்திய சட்டமன்றத்தால் நிராகரிக்கப்பட்ட எந்தவொரு மானியத்தையும் மீட்டெடுக்கும் 'சான்றளிப்பு' அதிகாரம் மற்றும் தடுப்பதிகாரம் கவர்னர்-ஜெனரலிடம் இருந்தது.\nஅரசியலமைப்பு தாக்கம்: சட்டமன்ற விரிவாக்கம் இருந்தபோதிலும் மத்திய நிர்வாக தன்னாதிக்கத்தைத் தக்கவைத்தது.\nதேர்வுப் பொறி: 6-ல் 3 இந்திய உறுப்பினர்கள் இருந்தனர், ஆனால் கமாண்டர்-இன்-சீஃப் தனிநபராவார்.\nநினைவுச் சூத்திரம்: 1919 மத்திய நிர்வாகம் = 3/6 இந்தியர்கள் + GG சான்றளிப்பு அதிகாரம்.",
        {
            "A": {"en": "Correct. Statements 1 and 2 are true; Statement 3 is false as Governor-General held certification powers.", "ta": "சரி. கூற்றுகள் 1 மற்றும் 2 சரி; சான்றளிப்பு அதிகாரம் இருந்ததால் கூற்று 3 தவறு."},
            "B": {"en": "Incorrect. Statement 3 is false.", "ta": "தவறு. கூற்று 3 தவறானது."},
            "C": {"en": "Incorrect. Statement 3 is false.", "ta": "தவறு. கூற்று 3 தவறானது."},
            "D": {"en": "Incorrect. Statement 3 is false.", "ta": "தவறு. கூற்று 3 தவறானது."}
        },
        "TNPSC Trap: Under 1919 Act, 3 out of 6 executive council members were Indians, but key portfolios like Home and Finance were held by British members.",
        "TNPSC பொறி: 1919 சட்டத்தில் 6-ல் 3 பேர் இந்தியர்களாக இருந்தபோதிலும் உள்துறை, நிதி போன்ற முக்கியத் துறைகள் பிரிட்டிஷாரிடமே இருந்தன.",
        "Governor-General under 1919 Act could issue ordinances valid for 6 months.",
        "1919 சட்டத்தின் கீழ் கவர்னர்-ஜெனரல் 6 மாத ஆயுள் கொண்ட அவசரச் சட்டங்களை பிறப்பிக்க முடியும்.",
        ["Polity", "Historical Background", "GOI Act 1919", "Central Government", "Grand Test"], "Analyze", 75
    ))

    # Q38: Conceptual MCQ - Medium - Indian Councils Act 1892 Indirect Election Mechanism
    questions.append(make_q(
        38, "Medium", "Conceptual MCQ",
        "Which bodies recommended non-official members to the Provincial Legislative Councils under the Indian Councils Act of 1892?",
        "1892 ஆம் ஆண்டின் இந்தியக் கவுன்சில்கள் சட்டத்தின் கீழ் மாகாண சட்ட மேலவைகளுக்கு அதிகாரப்பூர்வமற்ற உறுப்பினர்களைப் பரிந்துரைத்த அமைப்புகள் எவை?",
        [
            ("A", "District Boards, Municipalities, Universities, Trade Associations, and Zamindars", "மாவட்ட வாரியங்கள், நகராட்சிகள், பல்கலைக்கழகங்கள், வர்த்தக சங்கங்கள் மற்றும் ஜமீன்தார்கள்"),
            ("B", "Gram Panchayats, Co-operative Societies, and Farmer Unions", "கிராம பஞ்சாயத்துகள், கூட்டுறவு சங்கங்கள் மற்றும் விவசாயிகள் சங்கங்கள்"),
            ("C", "High Court Judges, Military Officers, and Religious Trusts", "உயர் நீதிமன்ற நீதிபதிகள், இராணுவ அதிகாரிகள் மற்றும் மத அறக்கட்டளைகள்"),
            ("D", "British House of Commons and Colonial Governors", "பிரிட்டிஷ் காமன்ஸ் சபை மற்றும் காலனித்துவ ஆளுநர்கள்")
        ],
        "A",
        "Historical Context: Recommendation principle introduced to select Indian non-officials without using the term 'election'.\nReason: Under 1892 Act, non-official members of Provincial Legislative Councils were nominated by Governors on the recommendation of District Boards, Municipalities, Universities, Trade Associations, Zamindars, and Chambers of Commerce.\nConstitutional Impact: Earliest institutional nexus between local bodies and provincial legislation.\nExam Trap: Central Council non-officials were recommended by Bengal Chamber of Commerce & Provincial Councils; Provincial Council non-officials by District Boards, Municipalities, Universities.\nMemory Trick: 1892 Provincial Recommendations = Local Bodies + Universities + Trade.",
        "வரலாற்றுப் பின்னணி: 'தேர்தல்' என்ற சொல்லைப் பயன்படுத்தாமல் அதிகாரப்பூர்வமற்ற இந்தியர்களைத் தேர்ந்தெடுக்க அறிமுகப்படுத்தப்பட்ட பரிந்துரைக் கோட்பாடு.\nகாரணம்: 1892 சட்டத்தில் மாகாண மேலவை உறுப்பினர்கள் மாவட்ட வாரியங்கள், நகராட்சிகள், பல்கலைக்கழகங்கள், வர்த்தக சங்கங்கள், ஜமீன்தார்கள் பரிந்துரையின் பேரில் ஆளுநர்களால் நியமிக்கப்பட்டனர்.\nஅரசியலமைப்பு தாக்கம்: உள்ளாட்சி அமைப்புகளுக்கும் மாகாண சட்ட உருவாக்கத்திற்கும் இடையிலான ஆரம்பகால தொடர்பு.\nதேர்வுப் பொறி: மத்திய மேலவைக்கு வங்காள வர்த்தக சபை; மாகாண மேலவைக்கு மாவட்ட வாரியங்கள், நகராட்சிகள், பல்கலைக்கழகங்கள்.\nநினைவுச் சூத்திரம்: 1892 மாகாண பரிந்துரை = உள்ளாட்சி அமைப்புகள் + பல்கலைக்கழகங்கள் + வர்த்தகம்.",
        {
            "A": {"en": "Correct. District boards, municipalities, universities, zamindars recommended provincial non-officials.", "ta": "சரி. மாவட்ட வாரியங்கள், நகராட்சிகள், பல்கலைக்கழகங்கள், ஜமீன்தார்கள் மாகாண உறுப்பினர்களைப் பரிந்துரைத்தனர்."},
            "B": {"en": "Incorrect. Gram panchayats were not statutory electoral recommenders in 1892.", "ta": "தவறு. கிராம பஞ்சாயத்துகள் 1892-ல் பரிந்துரை அமைப்புகளாக இல்லை."},
            "C": {"en": "Incorrect. High court judges and military officers did not make council recommendations.", "ta": "தவறு. நீதிபதிகளும் இராணுவ அதிகாரிகளும் பரிந்துரைக்கவில்லை."},
            "D": {"en": "Incorrect. House of Commons did not recommend provincial members.", "ta": "தவறு. காமன்ஸ் சபை பரிந்துரைக்கவில்லை."}
        },
        "TNPSC Trap: Central Legislative Council non-officials were nominated on recommendation of Bengal Chamber of Commerce and non-official members of Provincial Councils.",
        "TNPSC பொறி: மத்திய மேலவை உறுப்பினர்கள் வங்காள வர்த்தக சபை மற்றும் மாகாண மேலவை உறுப்பினர்களின் பரிந்துரையில் நியமிக்கப்பட்டனர்.",
        "1892 Act was the first step toward representative government in India.",
        "1892 சட்டம் இந்தியாவில் பிரதிநிதித்துவ அரசாங்கத்திற்கான முதல் படியாகும்.",
        ["Polity", "Historical Background", "Indian Councils Act 1892", "Local Bodies", "Grand Test"], "Understand", 60
    ))

    # Q39: Integrated PYQ Style - Hard - Evolution of Executive Veto & Ordinance Powers
    questions.append(make_q(
        39, "Hard", "Integrated PYQ Style",
        "Trace the statutory development of Ordinance-Making Power of the Governor-General / Viceroy across 1861, 1919, and 1935 Acts:",
        "1861, 1919 மற்றும் 1935 சட்டங்கள் வழியாக கவர்னர்-ஜெனரல் / வைஸ்ராயின் அவசரச் சட்டம் (Ordinance) பிறப்பிக்கும் அதிகாரத்தின் சட்டப்பூர்வ வளர்ச்சியை ஆராய்க:",
        [
            ("A", "Introduced in 1861 valid for 6 months without Council concurrence -> Retained in 1919 with emergency overriding powers -> Retained in 1935 with dual powers: during legislative recess & discretionary emergency ordinances", "1861-ல் கவுன்சில் ஒப்புதலின்றி 6 மாத ஆயுளுடன் அறிமுகம் -> 1919-ல் அவசரகால அதிகாரங்களுடன் நீடிப்பு -> 1935-ல் இருவகை அதிகாரங்கள்: மேலவை கூட்டத்தொடர் இல்லாதபோது & தன்னிச்சையான அவசரச் சட்டங்கள்"),
            ("B", "Introduced in 1773 -> Abolished in 1861 -> Restored in 1935", "1773-ல் அறிமுகம் -> 1861-ல் ஒழிப்பு -> 1935-ல் மீட்பு"),
            ("C", "Introduced in 1892 for 1 year -> Reduced to 6 months in 1919 -> Transferred to High Court Judges in 1935", "1892-ல் 1 ஆண்டிற்கு அறிமுகம் -> 1919-ல் 6 மாதங்களாகக் குறைப்பு -> 1935-ல் உயர் நீதிமன்ற நீதிபதிகளுக்கு மாற்றம்"),
            ("D", "Introduced in 1919 valid for 3 months -> Expanded to 1 year in 1935", "1919-ல் 3 மாத ஆயுளுடன் அறிமுகம் -> 1935-ல் 1 ஆண்டாக விரிவாக்கம்")
        ],
        "A",
        "Historical Context: Ordinance-making power provided executive autocracy alongside legislative expansion.\nReason: 1861 Act introduced Ordinance-making power (valid for 6 months in emergency) $\rightarrow$ 1919 Act retained it $\rightarrow$ 1935 Act expanded it (Section 42: Ordinances during recess of legislature on advice of ministers; Section 43: Emergency ordinances in Governor-General's sole discretion).\nConstitutional Impact: Provided model for Article 123 (President's Ordinance power) and Article 213 (Governor's Ordinance power) in modern Constitution.\nExam Trap: 1861 Act introduced ordinances; 1935 Act created two distinct types of ordinances.\nMemory Trick: 1861 (6 Months Intro) $\rightarrow$ 1919 (Retained) $\rightarrow$ 1935 (Recess + Discretionary Ordinances $\rightarrow$ Basis for Art 123).",
        "வரலாற்றுப் பின்னணி: அவசரச் சட்ட அதிகாரம் சட்டமன்ற விரிவாக்கத்துடன் இணைந்து நிர்வாக தன்னாதிக்கத்தை அளித்தது.\nகாரணம்: 1861 சட்டம் அவசரச் சட்ட அதிகாரத்தை அறிமுகப்படுத்தியது (அவசர காலத்தில் 6 மாத ஆயுள்) $\rightarrow$ 1919 சட்டம் அதை நீடித்தது $\rightarrow$ 1935 சட்டம் அதை விரிவாக்கியது (பிரிவு 42: அமைச்சர்கள் ஆலோசனையுடன் கூட்டத்தொடர் இல்லாதபோது; பிரிவு 43: கவர்னர்-ஜெனரலின் தன்னிச்சையான அவசரச் சட்டம்).\nஅரசியலமைப்பு தாக்கம்: நவீன அரசியலமைப்பின் சரத்து 123 (குடியரசுத் தலைவர் அவசரச் சட்டம்) மற்றும் சரத்து 213 (கவர்னர் அவசரச் சட்டம்) ஆகியவற்றுக்கு முன்மாதிரியானது.\nதேர்வுப் பொறி: 1861 சட்டம் அவசரச் சட்டத்தை அறிமுகப்படுத்தியது; 1935 சட்டம் இரண்டு தனிப்பட்ட அவசரச் சட்ட வகைகளை உருவாக்கியது.\nநினைவுச் சூத்திரம்: 1861 (6 மாத அறிமுகம்) $\rightarrow$ 1919 (நீடிப்பு) $\rightarrow$ 1935 (கூட்டத்தொடர் இல்லாதபோது + தன்னிச்சை $\rightarrow$ சரத்து 123 அடிப்படை).",
        {
            "A": {"en": "Correct sequence mapping Ordinance-making power from 1861 to 1935.", "ta": "சரி. 1861 முதல் 1935 வரை அவசரச் சட்ட அதிகார வளர்ச்சியின் சரியான வரிசை."},
            "B": {"en": "Incorrect. Ordinances were not introduced in 1773.", "ta": "தவறு. 1773-ல் அவசரச் சட்டம் அறிமுகமாகவில்லை."},
            "C": {"en": "Incorrect. Ordinances were introduced in 1861 with 6-month validity.", "ta": "தவறு. 1861-லேயே 6 மாத ஆயுளுடன் அறிமுகமானது."},
            "D": {"en": "Incorrect. Ordinance power originated in 1861, not 1919.", "ta": "தவறு. 1861-லேயே அவசரச் சட்ட அதிகாரம் உருவானது."}
        },
        "TNPSC Trap: Article 123 of modern Indian Constitution (President's Ordinance Power) is modeled on Section 42/43 of Government of India Act 1935.",
        "TNPSC பொறி: நவீன இந்திய அரசியலமைப்பின் சரத்து 123 (குடியரசுத் தலைவர் அவசரச் சட்ட அதிகாரம்) 1935 இந்திய அரசுச் சட்டத்தின் பிரிவு 42/43-ன் மாதிரி உருவமாகும்.",
        "Ordinances issued by Viceroy under 1861 Act had the same force of law as an Act passed by the Legislative Council.",
        "1861 சட்டத்தில் வைஸ்ராய் பிறப்பித்த அவசரச் சட்டத்திற்கு சட்ட மேலவை நிறைவேற்றிய சட்டத்திற்கு இணையான அதிகாரம் இருந்தது.",
        ["Polity", "Historical Background", "Ordinance Power Evolution", "Multi-Act Integration", "Grand Test"], "Analyze", 75
    ))

    # Q40: Statement Based - Medium - Government of India Act 1935 Federal Scheme Failure
    questions.append(make_q(
        40, "Medium", "Statement Based",
        "Consider the following statements regarding the All-India Federation proposed under the Government of India Act of 1935:\n1. It aimed to unite British Indian Provinces and Princely States into a single federal union.\n2. Joining the Federation was compulsory for British Indian Provinces, but voluntary for Princely States through an Instrument of Accession.\n3. The proposed All-India Federation came into operation immediately in 1937.\nWhich of the statements given above is/are correct?",
        "1935 இந்திய அரசுச் சட்டத்தின் கீழ் முன்மொழியப்பட்ட அகில இந்திய கூட்டாட்சி பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது பிரிட்டிஷ் இந்திய மாகாணங்களையும் சுதேச சமஸ்தானங்களையும் ஒரே கூட்டாட்சி ஒன்றியமாக இணைக்க இலக்குக் கொண்டது.\n2. கூட்டாட்சியில் சேர்வது பிரிட்டிஷ் இந்திய மாகாணங்களுக்குக் கட்டாயமாகவும், சுதேச சமஸ்தானங்களுக்கு இணையுறுதி ஆவணம் (Instrument of Accession) மூலம் விருப்பத்தின் அடிப்படையிலும் இருந்தது.\n3. முன்மொழியப்பட்ட அகில இந்திய கூட்டாட்சி 1937-ல் உடனடியாக நடைமுறைக்கு வந்தது.\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானவை?",
        [
            ("A", "1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
            ("B", "2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
            ("C", "1 and 3 only", "1 மற்றும் 3 மட்டுமே"),
            ("D", "1, 2 and 3", "1, 2 மற்றும் 3")
        ],
        "A",
        "Historical Context: The 1935 Act contemplated an All-India Federation comprising British Provinces and Princely States.\nReason: Statements 1 and 2 are correct. Statement 3 is incorrect because the proposed All-India Federation NEVER came into operation because the Princely States did not join it (required minimum quota of states refused to sign Instrument of Accession).\nConstitutional Impact: Provincial autonomy part of 1935 Act came into operation in 1937, but the federal part never materialized.\nExam Trap: Provincial Autonomy came into effect in 1937; Federal Scheme NEVER came into effect.\nMemory Trick: 1935 Federal Scheme = Proposed (Never came into effect because Princely States refused).",
        "வரலாற்றுப் பின்னணி: 1858-1935 சட்டங்களில் 1935 சட்டம் பிரிட்டிஷ் மாகாணங்கள் மற்றும் சுதேச சமஸ்தானங்களை உள்ளடக்கிய அகில இந்திய கூட்டாட்சியைத் திட்டமிட்டது.\nகாரணம்: கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் சுதேச சமஸ்தானங்கள் இணைய மறுத்ததால் (தேவையான குறைந்தபட்ச சமஸ்தானங்கள் இணையுறுதி ஆவணத்தில் கையெழுத்திடவில்லை) முன்மொழியப்பட்ட அகில இந்திய கூட்டாட்சி ஒருபோதும் நடைமுறைக்கு வரவில்லை.\nஅரசியலமைப்பு தாக்கம்: 1935 சட்டத்தின் மாகாண தன்னாட்சிப் பகுதி 1937-ல் அமலுக்கு வந்தது, ஆனால் கூட்டாட்சிப் பகுதி அமலாகவே இல்லை.\nதேர்வுப் பொறி: மாகாண தன்னாட்சி 1937-ல் அமலானது; கூட்டாட்சித் திட்டம் ஒருபோதும் அமலாகவில்லை.\nநினைவுச் சூத்திரம்: 1935 கூட்டாட்சித் திட்டம் = முன்மொழியப்பட்டது (சமஸ்தானங்கள் சேராததால் அமலாகவில்லை).",
        {
            "A": {"en": "Correct. Statements 1 and 2 are true; Statement 3 is false as Federal Scheme never materialized.", "ta": "சரி. கூற்றுகள் 1 மற்றும் 2 சரி; கூட்டாட்சி அமலாகாததால் கூற்று 3 தவறு."},
            "B": {"en": "Incorrect. Statement 3 is false.", "ta": "தவறு. கூற்று 3 தவறானது."},
            "C": {"en": "Incorrect. Statement 3 is false.", "ta": "தவறு. கூற்று 3 தவறானது."},
            "D": {"en": "Incorrect. Statement 3 is false.", "ta": "தவறு. கூற்று 3 தவறானது."}
        },
        "TNPSC Trap: Princely States were to get 125 out of 375 seats in Federal Assembly, nominated directly by rulers.",
        "TNPSC பொறி: கூட்டாட்சி பேரவையில் உள்ள 375 இடங்களில் 125 இடங்கள் ஆட்சியாளர்களால் நேரடியாக நியமிக்கப்படும் சுதேச சமஸ்தானங்களுக்கு ஒதுக்கப்பட்டன.",
        "Instrument of Accession was the legal document executed by rulers of Princely States to join the Federation.",
        "இணையுறுதி ஆவணம் (Instrument of Accession) என்பது கூட்டாட்சியில் சேர சுதேச ஆட்சியாளர்களால் கையெழுத்திடப்பட்ட சட்டப்பூர்வ ஆவணமாகும்.",
        ["Polity", "Historical Background", "GOI Act 1935", "Federal Scheme", "Grand Test"], "Analyze", 75
    ))

    # Q41: Direct MCQ - Easy - Secretary of State Office Creation
    questions.append(make_q(
        41, "Easy", "Direct MCQ",
        "The office of the 'Secretary of State for India' was created by which constitutional enactment?",
        "'இந்திய அரசுச் செயலர்' (Secretary of State for India) என்ற பதவி எந்த அரசியலமைப்பு சட்டத்தால் உருவாக்கப்பட்டது?",
        [
            ("A", "Government of India Act of 1858", "1858 ஆம் ஆண்டின் இந்திய அரசுச் சட்டம்"),
            ("B", "Regulating Act of 1773", "1773 ஆம் ஆண்டின் ஒழுங்குமுறைச் சட்டம்"),
            ("C", "Pitt's India Act of 1784", "1784 ஆம் ஆண்டின் பிட் இந்தியச் சட்டம்"),
            ("D", "Indian Councils Act of 1861", "1861 ஆம் ஆண்டின் இந்தியக் கவுன்சில்கள் சட்டம்")
        ],
        "A",
        "Historical Context: Transfer of power from EIC to British Crown under GOI Act 1858.\nReason: GOI Act 1858 created the office of Secretary of State for India, a member of the British Cabinet, complete with absolute authority and control over Indian administration.\nConstitutional Impact: Centralized political control over India in London.\nExam Trap: Created in 1858 Act; abolished by Indian Independence Act 1947.\nMemory Trick: Secretary of State = 1858 Crown Takeover.",
        "வரலாற்றுப் பின்னணி: 1858 இந்திய அரசுச் சட்டத்தில் கம்பெனியிடமிருந்து பிரிட்டிஷ் முடிக்கு அதிகாரம் மாற்றம்.\nகாரணம்: 1858 இந்திய அரசுச் சட்டம் பிரிட்டிஷ் கேபினட் அமைச்சரான இந்திய அரசுச் செயலர் பதவியை உருவாக்கி இந்திய நிர்வாகத்தின் முழு அதிகாரத்தையும் வழங்கியது.\nஅரசியலமைப்பு தாக்கம்: இந்திய மீதான அரசியல் கட்டுப்பாட்டை லண்டனில் மையப்படுத்தியது.\nதேர்வுப் பொறி: உருவாக்கப்பட்டது 1858 சட்டம்; ஒழிக்கப்பட்டது 1947 இந்திய சுதந்திரச் சட்டம்.\nநினைவுச் சூத்திரம்: அரசுச் செயலர் = 1858 முடி ஆட்சி தொடக்கம்.",
        {
            "A": {"en": "Correct. GOI Act 1858 created the Secretary of State for India office.", "ta": "சரி. 1858 இந்திய அரசுச் சட்டம் இந்திய அரசுச் செயலர் பதவியை உருவாக்கியது."},
            "B": {"en": "Incorrect. 1773 Act created Governor-General of Bengal.", "ta": "தவறு. 1773 சட்டம் வங்காள கவர்னர்-ஜெனரலை உருவாக்கியது."},
            "C": {"en": "Incorrect. 1784 Act created Board of Control.", "ta": "தவறு. 1784 சட்டம் கட்டுப்பாட்டு வாரியத்தை உருவாக்கியது."},
            "D": {"en": "Incorrect. 1861 Act expanded Legislative Councils.", "ta": "தவறு. 1861 சட்டம் மேலவைகளை விரிவுபடுத்தியது."}
        },
        "TNPSC Trap: Lord Stanley was the first Secretary of State for India in 1858.",
        "TNPSC பொறி: லார்டு ஸ்டான்லி 1858-ல் இந்தியாவின் முதல் அரசுச் செயலராவார்.",
        "Secretary of State for India was assisted by a 15-member Council of India.",
        "இந்திய அரசுச் செயலருக்கு 15 உறுப்பினர்களைக் கொண்ட இந்தியக் குழு உதவியது.",
        ["Polity", "Historical Background", "GOI Act 1858", "Secretary of State", "Grand Test"], "Remember", 45
    ))

    # Q42: Multi-Act Comparative - Hard - Evolution of Bicameralism & Franchise
    questions.append(make_q(
        42, "Hard", "Multi-Act Comparative",
        "Which inference accurately connects the progressive expansion of legislative membership across the 1861, 1892, 1909, 1919, and 1935 enactments?",
        "1861, 1892, 1909, 1919 மற்றும் 1935 சட்டங்களின் வழியாக சட்டமன்ற உறுப்பினர்களின் படிமுறை விரிவாக்கத்தை துல்லியமாக இணைக்கும் முடிவு எது?",
        [
            ("A", "Nomination of non-officials (1861) -> Indirect election recommendation (1892) -> Non-official majority in provinces & separate electorates (1909) -> Direct election & central bicameralism (1919) -> Provincial autonomy & bicameralism in 6 provinces (1935)", "அதிகாரப்பூர்வமற்றோர் நியமனம் (1861) -> மறைமுகத் தேர்தல் பரிந்துரை (1892) -> மாகாணங்களில் அதிகாரப்பூர்வமற்ற பெரும்பான்மை & தனித் தொகுதி (1909) -> நேரடித் தேர்தல் & மத்திய இரு அவை முறை (1919) -> மாகாண தன்னாட்சி & 6 மாகாணங்களில் இரு அவை முறை (1935)"),
            ("B", "Direct election (1861) -> Indirect election (1892) -> Provincial autonomy (1909) -> Central Dyarchy (1919) -> Abolition of all councils (1935)", "நேரடித் தேர்தல் (1861) -> மறைமுகத் தேர்தல் (1892) -> மாகாண தன்னாட்சி (1909) -> மத்திய இரட்டை ஆட்சி (1919) -> அனைத்து கவுன்சில்கள் ஒழிப்பு (1935)"),
            ("C", "Bicameralism (1861) -> Nominated majority (1892) -> Direct election (1909) -> Separate electorates (1919) -> Dyarchy (1935)", "இரு அவை முறை (1861) -> நியமனப் பெரும்பான்மை (1892) -> நேரடித் தேர்தல் (1909) -> தனித் தொகுதி (1919) -> இரட்டை ஆட்சி (1935)"),
            ("D", "Official majority everywhere (1861 to 1935 without any expansion)", "1861 முதல் 1935 வரை எந்த விரிவாக்கமும் இன்றி அனைத்து இடங்களிலும் அதிகாரப்பூர்வ பெரும்பான்மை")
        ],
        "A",
        "Historical Context: The continuous evolution of legislative representation in British India over 75 years.\nReason: 1861 (Nominated non-officials) $\rightarrow$ 1892 (Indirect recommendation system) $\rightarrow$ 1909 (Non-official majority in provinces + Muslim electorate) $\rightarrow$ 1919 (Direct elections + Central bicameralism) $\rightarrow$ 1935 (Provincial autonomy + 6 provincial bicameral legislatures).\nConstitutional Impact: Incremental movement toward representative and responsible parliamentary governance in India.\nExam Trap: Non-official majority in Center was granted ONLY in 1919, not 1909.\nMemory Trick: Nominated (1861) $\rightarrow$ Recommended (1892) $\rightarrow$ Non-official Prov (1909) $\rightarrow$ Direct Vote (1919) $\rightarrow$ Autonomy (1935).",
        "வரலாற்றுப் பின்னணி: 75 ஆண்டுகளில் பிரிட்டிஷ் இந்தியாவில் சட்டமன்ற பிரதிநிதித்துவத்தின் தொடர்ச்சியான வளர்ச்சி.\nகாரணம்: 1861 (நியமன உறுப்பினர்கள்) $\rightarrow$ 1892 (மறைமுகப் பரிந்துரை முறை) $\rightarrow$ 1909 (மாகாணங்களில் அதிகாரப்பூர்வமற்ற பெரும்பான்மை + முஸ்லிம் தொகுதி) $\rightarrow$ 1919 (நேரடித் தேர்தல் + மத்திய இரு அவை முறை) $\rightarrow$ 1935 (மாகாண தன்னாட்சி + 6 மாகாண இரு அவை மன்றங்கள்).\nஅரசியலமைப்பு தாக்கம்: இந்தியாவில் பிரதிநிதித்துவ நாடாளுமன்ற ஆட்சிக்கான படிமுறை இயக்கம்.\nதேர்வுப் பொறி: மத்திய மேலவையில் அதிகாரப்பூர்வமற்ற பெரும்பான்மை 1919-லேயே அளிக்கப்பட்டது, 1909-ல் அல்ல.\nநினைவுச் சூத்திரம்: நியமனம் (1861) $\rightarrow$ பரிந்துரை (1892) $\rightarrow$ மாகாண பெரும்பான்மை (1909) $\rightarrow$ நேரடி வாக்கு (1919) $\rightarrow$ தன்னாட்சி (1935).",
        {
            "A": {"en": "Correct. Perfectly maps legislative evolution across all five major Acts.", "ta": "சரி. ஐந்து முக்கிய சட்டங்களிலும் சட்டமன்ற வளர்ச்சியின் துல்லியமான வரிசை."},
            "B": {"en": "Incorrect. Direct election was not introduced in 1861.", "ta": "தவறு. 1861-ல் நேரடித் தேர்தல் வரவில்லை."},
            "C": {"en": "Incorrect. Bicameralism was introduced in 1919, not 1861.", "ta": "தவறு. இரு அவை முறை 1919-ல் வந்தது."},
            "D": {"en": "Incorrect. Legislative expansion occurred steadily across all Acts.", "ta": "தவறு. சட்டமன்ற விரிவாக்கம் தொடர்ச்சியாக நடந்தது."}
        },
        "TNPSC Trap: Non-official majority in Provincial Councils came in 1909; Non-official majority in Central Council came in 1919.",
        "TNPSC பொறி: மாகாண மேலவைகளில் அதிகாரப்பூர்வமற்ற பெரும்பான்மை 1909-ல்; மத்திய மேலவையில் அதிகாரப்பூர்வமற்ற பெரும்பான்மை 1919-ல் வந்தது.",
        "1909 Act retained official majority in Central Legislative Council while allowing non-official majority in Provincial Councils.",
        "1909 சட்டம் மத்திய மேலவையில் அதிகாரப்பூர்வ பெரும்பான்மையை நீடித்தது, மாகாணங்களில் அதிகாரப்பூர்வமற்ற பெரும்பான்மையை அனுமதித்தது.",
        ["Polity", "Historical Background", "Legislative Evolution", "Multi-Act Integration", "Grand Test"], "Evaluate", 90
    ))

    # Q43: Assertion & Reason - Medium - Act of Settlement 1781 Revenue Jurisdiction
    questions.append(make_q(
        43, "Medium", "Assertion & Reason",
        "Assertion (A): The Amending Act of 1781 excluded revenue matters and matters arising in the collection of revenue from the jurisdiction of the Supreme Court at Fort William.\nReason (R): Conflicts between the Supreme Court and Company revenue collectors had severely hampered revenue collection in Bengal.",
        "கூற்று (A): 1781 ஆம் ஆண்டின் திருத்தச் சட்டம் வருவாய் விவகாரங்களையும் வருவாய் வசூலில் எழும் விவகாரங்களையும் வில்லியம் கோட்டை உச்ச நீதிமன்ற அதிகார வரம்பிலிருந்து விலக்கியது.\nகாரணம் (R): உச்ச நீதிமன்றத்திற்கும் கம்பெனி வருவாய் வசூலிப்பாளர்களுக்கும் இடையிலான மோதல்கள் வங்காளத்தில் வருவாய் வசூலை கடுமையாகப் பாதித்தன.",
        [
            ("A", "Both (A) and (R) are true and (R) is the correct explanation of (A)", "(A) மற்றும் (R) இரண்டும் உண்மை, மேலும் (R) என்பது (A)-வின் சரியான விளக்கமாகும்"),
            ("B", "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கமல்ல"),
            ("C", "(A) is true but (R) is false", "(A) உண்மை, ஆனால் (R) தவறு"),
            ("D", "(A) is false but (R) is true", "(A) தவறு, ஆனால் (R) உண்மை")
        ],
        "A",
        "Historical Context: The Supreme Court set up in 1774 issued writs against revenue collectors, creating administrative paralysis.\nReason: Both (A) and (R) are true, and (R) directly explains why the British Parliament passed the 1781 Amending Act to explicitly exclude revenue administration from judicial interference.\nConstitutional Impact: Separated revenue executive function from judicial review.\nExam Trap: Supreme Court lost revenue jurisdiction in 1781, not 1773.\nMemory Trick: 1781 Act of Settlement = Revenue Protection for Company.",
        "வரலாற்றுப் பின்னணி: 1774-ல் அமைக்கப்பட்ட உச்ச நீதிமன்றம் வருவாய் வசூலிப்பாளர்கள் மீது பேராணைகளைப் பிறப்பித்து நிர்வாக முடக்கத்தை ஏற்படுத்தியது.\nகாரணம்: (A) மற்றும் (R) இரண்டும் உண்மை, மேலும் நீதித்துறைத் தலையீட்டிலிருந்து வருவாய் நிர்வாகத்தை விலக்க ஏன் 1781 சட்டம் நிறைவேற்றப்பட்டது என்பதை (R) நேரடியாக விளக்குகிறது.\nஅரசியலமைப்பு தாக்கம்: வருவாய் நிர்வாகப் பணியை நீதித்துறை மேலாய்விலிருந்து பிரித்தது.\nதேர்வுப் பொறி: உச்ச நீதிமன்றம் வருவாய் வரம்பை 1781-ல் இழந்தது, 1773-ல் அல்ல.\nநினைவுச் சூத்திரம்: 1781 சீர்முறைச் சட்டம் = கம்பெனியின் வருவாய் பாதுகாப்பு.",
        {
            "A": {"en": "Correct. (R) directly explains why revenue jurisdiction was removed in 1781.", "ta": "சரி. 1781-ல் வருவாய் வரம்பு ஏன் நீக்கப்பட்டது என்பதை (R) நேரடியாக விளக்குகிறது."},
            "B": {"en": "Incorrect. Reason directly provides the cause for Assertion.", "ta": "தவறு. காரணம் கூற்றிற்கான காரணியை நேரடியாக அளிக்கிறது."},
            "C": {"en": "Incorrect. Reason is true.", "ta": "தவறு. காரணம் உண்மையானது."},
            "D": {"en": "Incorrect. Assertion is true.", "ta": "தவறு. கூற்று உண்மையானது."}
        },
        "TNPSC Trap: 1781 Act also recognized the jurisdiction of Provincial Courts (Sadar Adalats) and empowered GG-in-Council to frame regulations for them.",
        "TNPSC பொறி: 1781 சட்டம் மாகாண நீதிமன்றங்களின் (சதர் அதாலத்துகள்) அதிகார வரம்பை அங்கீகரித்து அவற்றுக்கான விதிகளை உருவாக்க கவர்னர்-ஜெனரல் கவுன்சிலுக்கு அதிகாரமளித்தது.",
        "Regulations framed by Governor-General in Council under 1781 Act did not require registration in Supreme Court.",
        "1781 சட்டத்தின் கீழ் கவர்னர்-ஜெனரல் கவுன்சில் உருவாக்கிய விதிகளை உச்ச நீதிமன்றத்தில் பதிவு செய்யத் தேவையில்லை.",
        ["Polity", "Historical Background", "Act of Settlement 1781", "Revenue Jurisdiction", "Grand Test"], "Understand", 60
    ))

    # Q44: Match the Following - Medium - Statutory Committees & Commissions
    questions.append(make_q(
        44, "Medium", "Match the Following",
        "Match List I (Historic Committee / Commission) with List II (Associated Year & Reform Purpose):\n\nList I\nA. Macaulay Committee\nB. Aitchison Committee\nC. Lee Commission\nD. Simon Commission\n\nList II\n1. 1923 (Establishment of Central Public Service Commission)\n2. 1927 (Review of GOI Act 1919 working)\n3. 1854 (Committee on Indian Civil Service - Open Competition)\n4. 1886 (Public Service Commission dividing services into Statutory/Imperial/Provincial)",
        "பட்டியல் I (வரலாற்று குழு / ஆணையம்) பட்டியல் II (தொடர்புடைய ஆண்டு & சீர்திருத்த நோக்கம்) பொருத்துக:\n\nபட்டியல் I\nA. மெக்காலே குழு\nB. ஏட்சின்சன் குழு\nC. லீ குழு\nD. சைமன் குழு\n\nபட்டியல் II\n1. 1923 (மத்திய பொதுப்பணி ஆணைய அமைப்பு)\n2. 1927 (1919 சட்ட செயல்பாட்டை மேலாய்வு செய்தல்)\n3. 1854 (இந்திய சிவில் சர்வீஸ் குழு - திறந்த போட்டித் தேர்வு)\n4. 1886 (பொதுப்பணி ஆணையம் - பணிகளை ஏகாதிபத்திய/மாகாணப் பிரிவுகளாகப் பிரித்தல்)",
        [
            ("A", "A-3, B-4, C-1, D-2", "A-3, B-4, C-1, D-2"),
            ("B", "A-4, B-3, C-1, D-2", "A-4, B-3, C-1, D-2"),
            ("C", "A-3, B-1, C-4, D-2", "A-3, B-1, C-4, D-2"),
            ("D", "A-2, B-4, C-1, D-3", "A-2, B-4, C-1, D-3")
        ],
        "A",
        "Historical Context: Committees and Commissions shaped statutory reforms in civil services and governance.\nReason: Correct matches are A-3 (Macaulay Committee 1854 $\rightarrow$ Civil Service Open Competition), B-4 (Aitchison Committee 1886 $\rightarrow$ Public Service classification), C-1 (Lee Commission 1923 $\rightarrow$ Central Public Service Commission 1926), D-2 (Simon Commission 1927 $\rightarrow$ Review of 1919 Act).\nConstitutional Impact: Evolution of bureaucratic administration and constitutional review.\nExam Trap: Macaulay Committee = 1854; Aitchison = 1886; Lee Commission = 1923; Simon = 1927.\nMemory Trick: Macaulay (1854) $\rightarrow$ Aitchison (1886) $\rightarrow$ Lee (1923) $\rightarrow$ Simon (1927).",
        "வரலாற்றுப் பின்னணி: குழுக்களும் ஆணையங்களும் சிவில் சர்வீஸ் மற்றும் ஆட்சியில் சட்டப்பூர்வ சீர்திருத்தங்களை உருவாக்கின.\nகாரணம்: சரியான பொருத்தம்: A-3 (மெக்காலே குழு 1854 $\rightarrow$ சிவில் சர்வீஸ் போட்டித் தேர்வு), B-4 (ஏட்சின்சன் குழு 1886 $\rightarrow$ பொதுப்பணி வகைப்பாடு), C-1 (லீ குழு 1923 $\rightarrow$ மத்திய பொதுப்பணி ஆணையம் 1926), D-2 (சைமன் குழு 1927 $\rightarrow$ 1919 சட்ட மேலாய்வு).\nஅரசியலமைப்பு தாக்கம்: அதிகாரித்துவ நிர்வாகம் மற்றும் அரசியலமைப்பு மேலாய்வின் வளர்ச்சி.\nதேர்வுப் பொறி: மெக்காலே = 1854; ஏட்சின்சன் = 1886; லீ குழு = 1923; சைமன் = 1927.\nநினைவுச் சூத்திரம்: மெக்காலே (1854) $\rightarrow$ ஏட்சின்சன் (1886) $\rightarrow$ லீ (1923) $\rightarrow$ சைமன் (1927).",
        {
            "A": {"en": "Correct match across historic civil service and statutory commissions.", "ta": "சரி. வரலாற்றுச் சிறப்புமிக்க சிவில் சர்வீஸ் மற்றும் சட்டக் குழுக்களுக்கு சரியான பொருத்தம்."},
            "B": {"en": "Incorrect. Macaulay Committee was 1854 (3).", "ta": "தவறு. மெக்காலே குழு 1854 (3)."},
            "C": {"en": "Incorrect. Aitchison Committee was 1886 (4).", "ta": "தவறு. ஏட்சின்சன் குழு 1886 (4)."},
            "D": {"en": "Incorrect. Simon Commission was appointed in 1927 (2).", "ta": "தவறு. சைமன் குழு 1927-ல் நியமிக்கப்பட்டது (2)."}
        },
        "TNPSC Trap: Central Public Service Commission recommended by Lee Commission was set up on October 1, 1926, with Sir Ross Barker as 1st Chairman.",
        "TNPSC பொறி: லீ குழு பரிந்துரைத்த மத்திய பொதுப்பணி ஆணையம் 1926 அக்டோபர் 1 அன்று சர் ரோஸ் பார்கர் தலைவராக அமைக்கப்பட்டது.",
        "Aitchison Commission recommended abolishing the Statutory Civil Service created in 1879.",
        "ஏட்சின்சன் ஆணையம் 1879-ல் உருவாக்கப்பட்ட சட்டப்பூர்வ சிவில் சர்வீஸை ஒழிக்கப் பரிந்துரைத்தது.",
        ["Polity", "Historical Background", "Match the Following", "Committees & Commissions", "Grand Test"], "Analyze", 75
    ))

    # Q45: Direct MCQ - Medium - Indian Independence Act 1947 Boundary Commissions
    questions.append(make_q(
        45, "Medium", "Direct MCQ",
        "Who was appointed as the Chairman of the Boundary Commissions created under the Indian Independence Act of 1947 to demarcate the borders of Bengal and Punjab?",
        "1947 இந்திய சுதந்திரச் சட்டத்தின் கீழ் வங்காளம் மற்றும் பஞ்சாப் எல்லைகளை வரையறுக்க உருவாக்கப்பட்ட எல்லைக் குழுக்களின் தலைவராக நியமிக்கப்பட்டவர் யார்?",
        [
            ("A", "Sir Cyril Radcliffe", "சர் சிரில் ராட்க்ளிஃப்"),
            ("B", "Lord Mountbatten", "லார்டு மவுண்ட்பேட்டன்"),
            ("C", "Sir Stafford Cripps", "சர் ஸ்டாஃபோர்டு கிரிப்ஸ்"),
            ("D", "Pethick-Lawrence", "பெதிக்-லாரன்ஸ்")
        ],
        "A",
        "Historical Context: Partition of India required rapid statutory border demarcation in Bengal and Punjab.\nReason: Sir Cyril Radcliffe was appointed as Chairman of two Boundary Commissions (one for Bengal, one for Punjab) under the Indian Independence Act 1947 to draw the international borders (Radcliffe Line).\nConstitutional Impact: Created international boundaries of India and Pakistan.\nExam Trap: Durand Line = India/Afghansitan (1893); McMahon Line = India/China (1914); Radcliffe Line = India/Pakistan (1947).\nMemory Trick: 1947 Partition Border = Cyril Radcliffe.",
        "வரலாற்றுப் பின்னணி: இந்தியப் பிரிவினை வங்காளம் மற்றும் பஞ்சாபில் விரைவான சட்டப்பூர்வ எல்லை நிர்ணயத்தைக் கோரியது.\nகாரணம்: 1947 இந்திய சுதந்திரச் சட்டத்தின் கீழ் சர்வதேச எல்லைகளை (ராட்க்ளிஃப் கோடு) வரையறுக்க இரு எல்லைக் குழுக்களின் தலைவராக சர் சிரில் ராட்க்ளிஃப் நியமிக்கப்பட்டார்.\nஅரசியலமைப்பு தாக்கம்: இந்தியா மற்றும் பாகிஸ்தானின் சர்வதேச எல்லைகளை உருவாக்கியது.\nதேர்வுப் பொறி: துரந்த் கோடு = இந்தியா/ஆப்கானிஸ்தான் (1893); மெக்மகன் கோடு = இந்தியா/சீனா (1914); ராட்க்ளிஃப் கோடு = இந்தியா/பாகிஸ்தான் (1947).\nநினைவுச் சூத்திரம்: 1947 பிரிவினை எல்லை = சிரில் ராட்க்ளிஃப்.",
        {
            "A": {"en": "Correct. Sir Cyril Radcliffe chaired the Punjab and Bengal Boundary Commissions in 1947.", "ta": "சரி. சர் சிரில் ராட்க்ளிஃப் 1947-ல் பஞ்சாப் மற்றும் வங்காள எல்லைக் குழுக்களுக்கு தலைமை தாங்கினார்."},
            "B": {"en": "Incorrect. Lord Mountbatten was the Viceroy who proposed Mountbatten Plan.", "ta": "தவறு. லார்டு மவுண்ட்பேட்டன் திட்டத்தை முன்மொழிந்த வைஸ்ராயாவார்."},
            "C": {"en": "Incorrect. Sir Stafford Cripps led the Cripps Mission in 1942.", "ta": "தவறு. சர் ஸ்டாஃபோர்டு கிரிப்ஸ் 1942 கிரிப்ஸ் தூதுக்குழுவை வழிநடத்தினார்."},
            "D": {"en": "Incorrect. Pethick-Lawrence led the Cabinet Mission in 1946.", "ta": "தவறு. பெதிக்-லாரன்ஸ் 1946 கேபினட் தூதுக்குழுவை வழிநடத்தினார்."}
        },
        "TNPSC Trap: Radcliffe Line award was officially published on August 17, 1947, two days after independence.",
        "TNPSC பொறி: ராட்க்ளிஃப் எல்லை விருது சுதந்திரத்திற்கு இரண்டு நாட்களுக்குப் பிறகு ஆகஸ்ட் 17, 1947 அன்று அதிகாரப்பூர்வமாக வெளியானது.",
        "Boundary Commissions had 4 judge members each from Congress and Muslim League chaired by Radcliffe.",
        "எல்லைக் குழுக்கள் காங்கிரஸ் மற்றும் முஸ்லிம் லீக்கிலிருந்து தலா 4 நீதிபதி உறுப்பினர்களைக் கொண்டிருந்தன.",
        ["Polity", "Historical Background", "Indian Independence Act 1947", "Radcliffe Line", "Grand Test"], "Understand", 60
    ))

    # Q46: Statement Based - Hard - Regulating Act 1773 Features
    questions.append(make_q(
        46, "Hard", "Statement Based",
        "Consider the following statements regarding the Regulating Act of 1773:\n1. It was the first step taken by the British Government to control and regulate the affairs of the East India Company in India.\n2. It prohibited the servants of the Company from engaging in any private trade or accepting presents or bribes from the natives.\n3. It strengthened the control of the British Government over the Company by requiring the Court of Directors to report on its revenue, civil, and military affairs in India.\nWhich of the statements given above are correct?",
        "1773 ஆம் ஆண்டின் ஒழுங்குமுறைச் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது இந்தியாவில் கிழக்கிந்திய கம்பெனியின் விவகாரங்களைக் கட்டுப்படுத்தவும் சீரமைக்கவும் பிரிட்டிஷ் அரசு எடுத்த முதல் படியாகும்.\n2. இது கம்பெனி ஊழியர்கள் எந்தவொரு தனியார் வர்த்தகத்திலும் ஈடுபடுவதையோ அல்லது உள்ளூர்வாசிகளிடமிருந்து பரிசுகள் அல்லது லஞ்சங்களை வாங்குவதையோ தடை செய்தது.\n3. இது இந்தியாவில் தனது வருவாய், சிவில் மற்றும் இராணுவ விவகாரங்கள் பற்றி புகாரளிக்க இயக்குநர்கள் அவையைக் கட்டாயப்படுத்தியதன் மூலம் கம்பெனி மீதான பிரிட்டிஷ் அரசின் கட்டுப்பாட்டை வலுப்படுத்தியது.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
        [
            ("A", "1, 2 and 3", "1, 2 மற்றும் 3"),
            ("B", "1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
            ("C", "2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
            ("D", "1 and 3 only", "1 மற்றும் 3 மட்டுமே")
        ],
        "A",
        "Historical Context: Passed by Lord North's government to fix EIC financial crisis and corruption in Bengal.\nReason: All three statements are correct. The 1773 Act established parliamentary oversight (Statement 1), banned private trade & bribes for EIC servants (Statement 2), and mandated Court of Directors reporting to British Treasury (Statement 3).\nConstitutional Impact: Recognized for the first time the political and administrative functions of the Company.\nExam Trap: Private trade was banned in 1773, while Board of Control was created in 1784.\nMemory Trick: 1773 Act = First Parliamentary Control + No Private Trade + Reporting to Crown.",
        "வரலாற்றுப் பின்னணி: வங்காளத்தில் கம்பெனியின் நிதி நெருக்கடி மற்றும் ஊழலைச் சரிசெய்ய லார்டு நார்த் அரசால் நிறைவேற்றப்பட்டது.\nகாரணம்: மூன்று கூற்றுகளும் சரியானவை. 1773 சட்டம் நாடாளுமன்றக் மேற்பார்வையை நிறுவியது (கூற்று 1), கம்பெனி ஊழியர்களின் தனியார் வர்த்தகம் மற்றும் லஞ்சத்தைத் தடை செய்தது (கூற்று 2), இயக்குநர்கள் அவை பிரிட்டிஷ் கருவூலத்திற்கு புகாரளிப்பதைக் கட்டாயமாக்கியது (கூற்று 3).\nஅரசியலமைப்பு தாக்கம்: கம்பெனியின் அரசியல் மற்றும் நிர்வாகப் பணிகளை முதன்முறையாக அங்கீகரித்தது.\nதேர்வுப் பொறி: தனியார் வர்த்தகத் தடை 1773-ல்; கட்டுப்பாட்டு வாரியம் 1784-ல்.\nநினைவுச் சூத்திரம்: 1773 சட்டம் = முதல் நாடாளுமன்றக் கட்டுப்பாடு + தனியார் வர்த்தகத் தடை + அரசிற்கு அறிக்கை.",
        {
            "A": {"en": "Correct. All three statements accurately state provisions of Regulating Act 1773.", "ta": "சரி. 1773 ஒழுங்குமுறைச் சட்டத்தின் மூன்று கூற்றுகளும் துல்லியமாக சரியானவை."},
            "B": {"en": "Incorrect. Statement 3 is also correct.", "ta": "தவறு. கூற்று 3-ம் சரியானது."},
            "C": {"en": "Incorrect. Statement 1 is also correct.", "ta": "தவறு. கூற்று 1-ம் சரியானது."},
            "D": {"en": "Incorrect. Statement 2 is also correct.", "ta": "தவறு. கூற்று 2-ம் சரியானது."}
        },
        "TNPSC Trap: Lord North's Secret Committee recommended the passage of the Regulating Act of 1773.",
        "TNPSC பொறி: லார்டு நார்த்தின் இரகசியக் குழுவின் பரிந்துரையின் பேரில் 1773 ஒழுங்குமுறைச் சட்டம் நிறைவேற்றப்பட்டது.",
        "Regulating Act 1773 made Governors of Bombay and Madras subordinate to Governor-General of Bengal.",
        "1773 ஒழுங்குமுறைச் சட்டம் பம்பாய், மதராஸ் ஆளுநர்களை வங்காள கவர்னர்-ஜெனரலுக்குக் கீழ்மைப்படுத்தியது.",
        ["Polity", "Historical Background", "Regulating Act 1773", "Grand Test"], "Analyze", 75
    ))

    # Q47: Conceptual MCQ - Medium - Government of India Act 1858 Title & Sovereign Status
    questions.append(make_q(
        47, "Medium", "Conceptual MCQ",
        "What official statutory title was given to the Government of India Act of 1858 when it was enacted by the British Parliament?",
        "1858 இந்திய அரசுச் சட்டம் பிரிட்டிஷ் நாடாளுமன்றத்தால் இயற்றப்பட்டபோது அதற்கு வழங்கப்பட்ட அதிகாரப்பூர்வ சட்டப்பூர்வ தலைப்பு யாது?",
        [
            ("A", "An Act for the Better Government of India", "இந்திய நல்வாட்சிப் பெற இயற்றப்பட்ட சட்டம் (An Act for the Better Government of India)"),
            ("B", "The Indian Independence and Sovereignty Act", "இந்திய சுதந்திரம் மற்றும் இறையாண்மைச் சட்டம்"),
            ("C", "The Charter Renewal and Crown Takeover Act", "சாசனப் புதுப்பித்தல் மற்றும் முடி ஆட்சி மீட்புச் சட்டம்"),
            ("D", "The British Empire Indian Dominions Act", "பிரிட்டிஷ் ஏகாதிபத்திய இந்திய டொமினியன் சட்டம்")
        ],
        "A",
        "Historical Context: Enacted after 1857 Revolt to reassure British public and Indian subjects of orderly governance.\nReason: The Government of India Act 1858 was officially titled 'An Act for the Better Government of India'. It transferred governance from EIC to Queen Victoria.\nConstitutional Impact: Established direct Crown executive control.\nExam Trap: Official title was 'Act for the Better Government of India', not 'Crown Rule Act'.\nMemory Trick: 1858 = Better Government of India Act.",
        "வரலாற்றுப் பின்னணி: 1857 கிளர்ச்சிக்குப் பிறகு பிரிட்டிஷ் பொதுமக்களுக்கும் இந்திய மக்களுக்கும் ஒழுங்கான ஆட்சியை உறுதிப்படுத்த இயற்றப்பட்டது.\nகாரணம்: 1858 இந்திய அரசுச் சட்டம் அதிகாரப்பூர்வமாக 'இந்திய நல்வாட்சிப் பெற இயற்றப்பட்ட சட்டம்' என தலைப்பிடப்பட்டது. இது ஆட்சியை கம்பெனியிடமிருந்து விக்டோரியா மகாராணிக்கு மாற்றியது.\nஅரசியலமைப்பு தாக்கம்: பிரிட்டிஷ் முடியின் நேரடி நிர்வாகக் கட்டுப்பாட்டை நிறுவியது.\nதேர்வுப் பொறி: அதிகாரப்பூர்வ தலைப்பு 'இந்திய நல்வாட்சிச் சட்டம்', 'முடி ஆட்சிச் சட்டம்' அல்ல.\nநினைவுச் சூத்திரம்: 1858 = இந்திய நல்வாட்சிச் சட்டம்.",
        {
            "A": {"en": "Correct. Official title of 1858 Act was 'An Act for the Better Government of India'.", "ta": "சரி. 1858 சட்டத்தின் அதிகாரப்பூர்வ தலைப்பு 'இந்திய நல்வாட்சிச் சட்டம்'."},
            "B": {"en": "Incorrect. Independence Act was enacted in 1947.", "ta": "தவறு. சுதந்திரச் சட்டம் 1947-ல் இயற்றப்பட்டது."},
            "C": {"en": "Incorrect. Not the official statutory title.", "ta": "தவறு. அதிகாரப்பூர்வ சட்டப்பூர்வ தலைப்பல்ல."},
            "D": {"en": "Incorrect. Not the official statutory title.", "ta": "தவறு. அதிகாரப்பூர்வ சட்டப்பூர்வ தலைப்பல்ல."}
        },
        "TNPSC Trap: Under 1858 Act, the Governor-General was given the additional title of 'Viceroy' (meaning representative of the Crown).",
        "TNPSC பொறி: 1858 சட்டத்தின் கீழ் கவர்னர்-ஜெனரலுக்கு 'வைஸ்ராய்' (அரசரின் பிரதிநிதி) என்ற கூடுதல் தலைப்பு வழங்கப்பட்டது.",
        "Lord Canning was the last Governor-General of India and first Viceroy of India under 1858 Act.",
        "லார்டு கேனிங் 1858 சட்டத்தின் கீழ் இந்தியாவின் கடைசி கவர்னர்-ஜெனரலாகவும் முதல் வைஸ்ராயாகவும் இருந்தார்.",
        ["Polity", "Historical Background", "GOI Act 1858", "Viceroy", "Grand Test"], "Understand", 60
    ))

    # Q48: Multi-Act Comparative - Hard - Evolution of Executive Power Override
    questions.append(make_q(
        48, "Hard", "Multi-Act Comparative",
        "Which statutory enactment for the first time granted the Governor-General specific discretionary authority to override the decisions of his Executive Council in extraordinary situations?",
        "எந்த சட்டப்பூர்வ சட்டம் முதன்முறையாக கவர்னர்-ஜெனரலுக்கு அசாதாரண சூழ்நிலைகளில் தனது நிர்வாகக் குழுவின் முடிவுகளை நிராகரிக்க குறிப்பிட்ட தன்னிச்சையான அதிகாரத்தை வழங்கியது?",
        [
            ("A", "Act of 1786 (enacted specifically for Lord Cornwallis)", "1786 ஆம் ஆண்டின் சட்டம் (லார்டு காரன்வாலிஸுக்காக இயற்றப்பட்டது)"),
            ("B", "Regulating Act of 1773", "1773 ஆம் ஆண்டின் ஒழுங்குமுறைச் சட்டம்"),
            ("C", "Pitt's India Act of 1784", "1784 ஆம் ஆண்டின் பிட் இந்தியச் சட்டம்"),
            ("D", "Charter Act of 1813", "1813 ஆம் ஆண்டின் சாசனச் சட்டம்")
        ],
        "A",
        "Historical Context: Lord Cornwallis demanded overriding powers over his council as a precondition to accept Governor-Generalship.\nReason: In 1786, British Parliament passed the Act of 1786 giving Lord Cornwallis power to override his council in extraordinary cases involving safety, peace, or interest of British possessions. This power was later extended to all future Governor-Generals by the Charter Act of 1793.\nConstitutional Impact: Created supreme executive discretion vested in the Governor-General.\nExam Trap: Overriding power enacted in 1786 for Cornwallis; extended to all future GGs in 1793 Charter Act.\nMemory Trick: 1786 Act = Cornwallis Override Power.",
        "வரலாற்றுப் பின்னணி: லார்டு காரன்வாலிஸ் கவர்னர்-ஜெனரல் பதவியை ஏற்கத் தனது கவுன்சிலை நிராகரிக்கும் அதிகாரத்தைக் நிபந்தனையாகக் கோரினார்.\nகாரணம்: 1786-ல் பிரிட்டிஷ் நாடாளுமன்றம் 1786 சட்டத்தை நிறைவேற்றி பாதுகாப்பு, அமைதி தொடர்பாக அசாதாரண சூழலில் கவுன்சிலை நிராகரிக்க காரன்வாலிஸுக்கு அதிகாரமளித்தது. இவதிகாரம் 1793 சாசனச் சட்டத்தில் அனைத்து வருங்கால GG-களுக்கும் நீட்டிக்கப்பட்டது.\nஅரசியலமைப்பு தாக்கம்: கவர்னர்-ஜெனரலிடம் உச்ச தன்னிச்சை அதிகாரத்தை உருவாக்கியது.\nதேர்வுப் பொறி: 1786-ல் காரன்வாலிஸுக்கு நிராகரிப்பு அதிகாரம்; 1793-ல் அனைவருக்கும் நீட்டிப்பு.\nநினைவுச் சூத்திரம்: 1786 சட்டம் = காரன்வாலிஸ் நிராகரிப்பு அதிகாரம்.",
        {
            "A": {"en": "Correct. Act of 1786 granted Lord Cornwallis overriding power over his council.", "ta": "சரி. 1786 சட்டம் லார்டு காரன்வாலிஸுக்கு கவுன்சிலை நிராகரிக்கும் அதிகாரத்தை அளித்தது."},
            "B": {"en": "Incorrect. 1773 Act bound the Governor-General to majority vote of his 4-member council.", "ta": "தவறு. 1773 சட்டம் கவர்னர்-ஜெனரலை கவுன்சில் பெரும்பான்மை வாக்கிற்கு கட்டுப்படுத்தியது."},
            "C": {"en": "Incorrect. 1784 Act reduced council to 3 members, but did not grant overriding veto.", "ta": "தவறு. 1784 சட்டம் உறுப்பினர்களை 3 ஆகக் குறைத்தது, நிராகரிப்பு அதிகாரம் அளிக்கவில்லை."},
            "D": {"en": "Incorrect. 1813 Act dealt with trade monopoly and education.", "ta": "தவறு. 1813 சட்டம் வர்த்தகம் மற்றும் கல்வியைக் கையாண்டது."}
        },
        "TNPSC Trap: Lord Cornwallis was also appointed as Commander-in-Chief alongside Governor-General under the Act of 1786.",
        "TNPSC பொறி: லார்டு காரன்வாலிஸ் 1786 சட்டத்தின் கீழ் கவர்னர்-ஜெனரலுடன் கமாண்டர்-இன்-சீஃப் ஆகவும் நியமிக்கப்பட்டார்.",
        "Charter Act of 1793 extended the council overriding power to all future Governor-Generals and Governors of Presidencies.",
        "1793 சாசனச் சட்டம் கவுன்சில் நிராகரிப்பு அதிகாரத்தை அனைத்து எதிர்கால கவர்னர்-ஜெனரல்கள் மற்றும் ஆளுநர்களுக்கும் நீட்டித்தது.",
        ["Polity", "Historical Background", "Act of 1786", "Lord Cornwallis", "Overriding Power", "Grand Test"], "Analyze", 75
    ))

    # Q49: Direct MCQ - Medium - Indian Councils Act 1909 Legislative Powers
    questions.append(make_q(
        49, "Medium", "Direct MCQ",
        "Under the Indian Councils Act of 1909, which member was appointed as the first Indian to join the Viceroy's Executive Council?",
        "1909 ஆம் ஆண்டின் இந்தியக் கவுன்சில்கள் சட்டத்தின் கீழ், வைஸ்ராயின் நிர்வாகக் குழுவில் சேர்ந்த முதல் இந்திய உறுப்பினர் யார்?",
        [
            ("A", "Satyendra Prasad Sinha", "சத்யேந்திர பிரசாத் சின்கா"),
            ("B", "Tej Bahadur Sapru", "தேஜ் பகதூர் சப்ரு"),
            ("C", "Dadabhai Naoroji", "தாதாபாய் நௌரோஜி"),
            ("D", "Gopal Krishna Gokhale", "கோபால கிருஷ்ண கோகலே")
        ],
        "A",
        "Historical Context: Morley-Minto reforms provided for the association of Indians with executive councils.\nReason: Satyendra Prasad Sinha (S.P. Sinha) became the first Indian to join the Viceroy's Executive Council. He was appointed as the Law Member.\nConstitutional Impact: Historical breakthrough breaking racial bar in supreme executive council.\nExam Trap: S.P. Sinha = 1st Indian in Viceroy's Executive Council (1909); Tej Bahadur Sapru served later under 1919 Act.\nMemory Trick: 1909 S.P. Sinha = First Indian Law Member in Viceroy Council.",
        "வரலாற்றுப் பின்னணி: மோலி-மிண்டோ சீர்திருத்தங்கள் இந்தியர்களை நிர்வாகக் குழுக்களில் இணைக்க வழிவகுத்தன.\nகாரணம்: சத்யேந்திர பிரசாத் சின்கா (எஸ்.பி. சின்கா) வைஸ்ராயின் நிர்வாகக் குழுவில் சேர்ந்த முதல் இந்தியராவார். அவர் சட்ட உறுப்பினராக நியமிக்கப்பட்டார்.\nஅரசியலமைப்பு தாக்கம்: உச்ச நிர்வாகக் குழுவில் இனப் பாகுபாட்டை உடைத்த வரலாற்றுத் திருப்புமுனை.\nதேர்வுப் பொறி: எஸ்.பி. சின்கா = வைஸ்ராய் குழுவில் 1வது இந்தியர் (1909); தேஜ் பகதூர் சப்ரு 1919 சட்டத்தின்கீழ் பின்னர் பணியாற்றினார்.\nநினைவுச் சூத்திரம்: 1909 எஸ்.பி. சின்கா = வைஸ்ராய் குழுவின் முதல் இந்திய சட்ட உறுப்பினர்.",
        {
            "A": {"en": "Correct. S.P. Sinha was appointed as Law Member in Viceroy's Executive Council in 1909.", "ta": "சரி. எஸ்.பி. சின்கா 1909-ல் வைஸ்ராய் குழுவின் சட்ட உறுப்பினராக நியமிக்கப்பட்டார்."},
            "B": {"en": "Incorrect. Tej Bahadur Sapru joined the Viceroy's Executive Council in 1920 under 1919 Act.", "ta": "தவறு. தேஜ் பகதூர் சப்ரு 1920-ல் சேர்ந்தார்."},
            "C": {"en": "Incorrect. Dadabhai Naoroji was the first Indian member of British House of Commons (1892).", "ta": "தவறு. தாதாபாய் நௌரோஜி பிரிட்டிஷ் காமன்ஸ் சபையின் முதல் இந்திய உறுப்பினராவார்."},
            "D": {"en": "Incorrect. Gopal Krishna Gokhale was a member of Imperial Legislative Council, not Executive Council.", "ta": "தவறு. கோகலே மத்திய சட்ட மேலவை உறுப்பினராவார்."}
        },
        "TNPSC Trap: S.P. Sinha was later made Lord Sinha (Baron Sinha of Raipur) and appointed Governor of Bihar and Orissa in 1920.",
        "TNPSC பொறி: எஸ்.பி. சின்கா பின்னர் லார்டு சின்காவாக்கப்பட்டு 1920-ல் பீகார்-ஒரிசாவின் கவர்னராக நியமிக்கப்பட்டார்.",
        "1909 Act also allowed two Indians (K.G. Gupta and Syed Husain Bilgrami) to be appointed to the Council of India in London.",
        "1909 சட்டம் லண்டனில் உள்ள இந்தியக் குழுவிலும் இரு இந்தியர்களை (கே.ஜி. குப்தா, சையத் உசேன் பில்கிராமி) நியமிக்க வழிவகுத்தது.",
        ["Polity", "Historical Background", "Indian Councils Act 1909", "S.P. Sinha", "Grand Test"], "Understand", 60
    ))

    # Q50: Exceptional Difficult - Hard - 1935 Act Provincial Autonomy Safeguards Trap
    questions.append(make_q(
        50, "Exceptional Difficult", "Statement Based",
        "Consider the following statements regarding the special discretionary powers ('special responsibilities') of Provincial Governors under the Government of India Act of 1935:\n1. Governors could override their provincial ministers when exercising their 'special responsibilities' (e.g., prevention of grave menace to peace, protection of minorities, and rights of civil servants).\n2. When acting in discretion, Governors were subject to the control of the Governor-General and through him the Secretary of State for India.\n3. Section 93 empowered the Governor to suspend the constitutional machinery and assume all powers of the provincial government.\nWhich of the statements given above are correct?",
        "1935 இந்திய அரசுச் சட்டத்தின் கீழ் மாகாண கவர்னர்களின் சிறப்பான தன்னிச்சையான அதிகாரங்கள் ('சிறப்புப் பொறுப்புகள்') பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. அமைதிக்கான அச்சுறுத்தலைத் தடுத்தல், சிறுபான்மையினர் பாதுகாப்பு, அரசு ஊழியர்களின் உரிமைகள் போன்ற 'சிறப்புப் பொறுப்புகளை' செயல்படுத்தும்போது கவர்னர்கள் தங்களது மாகாண அமைச்சர்களை நிராகரிக்க முடியும்.\n2. தன்னிச்சையாகச் செயல்படும்போது, கவர்னர்கள் கவர்னர்-ஜெனரல் மற்றும் அவர் மூலம் இந்திய அரசுச் செயலரின் கட்டுப்பாட்டிற்கு உட்பட்டவர்கள்.\n3. பிரிவு 93 கவர்னருக்கு அரசியலமைப்பு பொறிமுறையை முடக்கி மாகாண அரசின் அனைத்து அதிகாரங்களையும் தானே ஏற்றுக்கொள்ள அதிகாரமளித்தது.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
        [
            ("A", "1, 2 and 3", "1, 2 மற்றும் 3"),
            ("B", "1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
            ("C", "2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
            ("D", "1 and 3 only", "1 மற்றும் 3 மட்டுமே")
        ],
        "A",
        "Historical Context: Section 93 of 1935 Act provided emergency powers that limited genuine provincial autonomy.\nReason: All three statements are correct. Governor's 'special responsibilities' overrode ministers (Statement 1), Governor was responsible to GG and SOS when acting in individual judgment/discretion (Statement 2), and Section 93 allowed Governor rule in emergency (Statement 3).\nConstitutional Impact: Section 93 of 1935 Act became the direct prototype for Article 356 (President's Rule) in Article 356 of modern Constitution.\nExam Trap: Section 93 of 1935 Act = Article 356 of Indian Constitution.\nMemory Trick: Section 93 of 1935 Act = Governor's Emergency Rule $\rightarrow$ Precursor to Art 356.",
        "வரலாற்றுப் பின்னணி: 1935 சட்டத்தின் பிரிவு 93 மாகாண தன்னாட்சியைக் கட்டுப்படுத்திய அவசரகால அதிகாரங்களை வழங்கியது.\nகாரணம்: மூன்று கூற்றுகளும் சரியானவை. கவர்னரின் 'சிறப்புப் பொறுப்புகள்' அமைச்சர்களை நிராகரித்தன (கூற்று 1), தன்னிச்சையாகச் செயல்படும்போது கவர்னர் GG மற்றும் அரசுச் செயலருக்குப் பொறுப்பானவர் (கூற்று 2), பிரிவு 93 அவசர காலத்தில் கவர்னர் ஆட்சியை அனுமதித்தது (கூற்று 3).\nஅரசியலமைப்பு தாக்கம்: 1935 சட்டத்தின் பிரிவு 93 நவீன அரசியலமைப்பின் சரத்து 356 (குடியரசுத் தலைவர் ஆட்சி)க்கான நேரடி மாதிரியாக அமைந்தது.\nதேர்வுப் பொறி: 1935 சட்டத்தின் பிரிவு 93 = இந்திய அரசியலமைப்பின் சரத்து 356.\nநினைவுச் சூத்திரம்: 1935 பிரிவு 93 = கவர்னரின் அவசரகால ஆட்சி $\rightarrow$ சரத்து 356 முன்னோடி.",
        {
            "A": {"en": "Correct. All three statements regarding Section 93 and Governor's discretionary powers under 1935 Act are true.", "ta": "சரி. 1935 சட்டத்தின் பிரிவு 93 மற்றும் கவர்னரின் தன்னிச்சை அதிகாரங்கள் தொடர்பான மூன்று கூற்றுகளும் சரியானவை."},
            "B": {"en": "Incorrect. Statement 3 is also correct.", "ta": "தவறு. கூற்று 3-ம் சரியானது."},
            "C": {"en": "Incorrect. Statement 1 is also correct.", "ta": "தவறு. கூற்று 1-ம் சரியானது."},
            "D": {"en": "Incorrect. Statement 2 is also correct.", "ta": "தவறு. கூற்று 2-ம் சரியானது."}
        },
        "TNPSC Trap: Section 93 of 1935 Act was invoked in late 1939 when Congress ministries in 8 provinces resigned protesting India's drag into WWII without consent.",
        "TNPSC பொறி: 1939 பிற்பகுதியில் இரண்டாம் உலகப்போரில் இந்தியாவைக் கலந்தாலோசிக்காமல் ஈடுபடுத்தியதை எதிர்த்து 8 மாகாண காங்கிரஸ் அமைச்சரவைகள் விலகியபோது பிரிவு 93 அமலானது.",
        "Section 93 empowered Governors to take over provincial administration for up to 3 years.",
        "பிரிவு 93 கவர்னர்கள் 3 ஆண்டுகள் வரை மாகாண நிர்வாகத்தைக் கைப்பற்ற அதிகாரமளித்தது.",
        ["Polity", "Historical Background", "GOI Act 1935", "Section 93", "Article 356 Precursor", "Grand Test"], "Evaluate", 90
    ))

    return questions

if __name__ == "__main__":
    qs = get_part2_questions()
    print(f"Part 2 Questions Generated: {len(qs)}")
