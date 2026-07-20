import json

def get_part3_questions():
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

    # Q51: Direct MCQ - Medium - High Commissioner for India 1919
    questions.append(make_q(
        51, "Medium", "Direct MCQ",
        "Which statutory enactment created the new office of the 'High Commissioner for India in London' and transferred to him some of the commercial functions performed by the Secretary of State?",
        "லண்டனில் 'இந்திய உயர் ஆணையர்' (High Commissioner for India) என்ற புதிய அலுவலகத்தை உருவாக்கி, இந்திய அரசுச் செயலர் செய்து வந்த சில வணிகப் பணிகளை அவருக்கு மாற்றிய சட்டப்பூர்வ சட்டம் எது?",
        [
            ("A", "Government of India Act of 1919", "1919 ஆம் ஆண்டின் இந்திய அரசுச் சட்டம்"),
            ("B", "Indian Councils Act of 1909", "1909 ஆம் ஆண்டின் இந்தியக் கவுன்சில்கள் சட்டம்"),
            ("C", "Government of India Act of 1935", "1935 ஆம் ஆண்டின் இந்திய அரசுச் சட்டம்"),
            ("D", "Indian Independence Act of 1947", "1947 ஆம் ஆண்டின் இந்திய சுதந்திரச் சட்டம்")
        ],
        "A",
        "Historical Context: Montagu-Chelmsford Reforms restructured Indian administrative machinery in London.\nReason: GOI Act 1919 created the office of High Commissioner for India in London, paid out of Indian revenues, and transferred to him commercial and agency functions previously handled by the Secretary of State for India. Sir William Stevenson Meyer was the first High Commissioner (1920).\nConstitutional Impact: Separated agency/commercial work from political oversight in London.\nExam Trap: High Commissioner created in 1919 Act; Secretary of State created in 1858 Act.\nMemory Trick: 1919 Act = Created High Commissioner for India in London.",
        "வரலாற்றுப் பின்னணி: மாண்டேகு-செம்ஸ்ஃபோர்டு சீர்திருத்தங்கள் லண்டனில் உள்ள இந்திய நிர்வாக அமைப்பை சீரமைத்தன.\nகாரணம்: 1919 இந்திய அரசுச் சட்டம் லண்டனில் இந்திய உயர் ஆணையர் அலுவலகத்தை உருவாக்கி, இந்திய அரசுச் செயலர் செய்துவந்த வணிக மற்றும் முகமைப் பணிகளை அவருக்கு மாற்றியது. சர் வில்லியம் ஸ்டீவன்சன் மேயர் முதல் உயர் ஆணையராவார் (1920).\nஅரசியலமைப்பு தாக்கம்: லண்டனில் அரசியல் மேற்பார்வையிலிருந்து வணிகப் பணிகளைப் பிரித்தது.\nதேர்வுப் பொறி: உயர் ஆணையர் உருவாக்கப்பட்டது 1919 சட்டம்; அரசுச் செயலர் உருவாக்கப்பட்டது 1858 சட்டம்.\nநினைவுச் சூத்திரம்: 1919 சட்டம் = லண்டனில் இந்திய உயர் ஆணையர் உருவாக்கப்பட்டது.",
        {
            "A": {"en": "Correct. GOI Act 1919 established the High Commissioner for India in London.", "ta": "சரி. 1919 இந்திய அரசுச் சட்டம் லண்டனில் இந்திய உயர் ஆணையரை நிறுவியது."},
            "B": {"en": "Incorrect. 1909 Act dealt with Morley-Minto council expansion.", "ta": "தவறு. 1909 சட்டம் மோலி-மிண்டோ மேலவை விரிவாக்கம் பற்றியது."},
            "C": {"en": "Incorrect. 1935 Act established Federal Court and RBI.", "ta": "தவறு. 1935 சட்டம் கூட்டாட்சி நீதிமன்றம், RBI அமைத்தது."},
            "D": {"en": "Incorrect. 1947 Act abolished Secretary of State office.", "ta": "தவறு. 1947 சட்டம் அரசுச் செயலர் பதவியை ஒழித்தது."}
        },
        "TNPSC Trap: Salary of High Commissioner for India was paid out of Indian revenues, while 1919 Act changed Secretary of State salary to British exchequer.",
        "TNPSC பொறி: உயர் ஆணையரின் சம்பளம் இந்திய வருவாயிலிருந்து வழங்கப்பட்டது, ஆனால் 1919 சட்டம் அரசுச் செயலரின் சம்பளத்தை பிரிட்டிஷ் கருவூலத்திற்கு மாற்றியது.",
        "Sir William Stevenson Meyer was appointed as the first High Commissioner for India in 1920.",
        "சர் வில்லியம் ஸ்டீவன்சன் மேயர் 1920-ல் இந்தியாவின் முதல் உயர் ஆணையராக நியமிக்கப்பட்டார்.",
        ["Polity", "Historical Background", "GOI Act 1919", "High Commissioner", "Grand Test"], "Understand", 60
    ))

    # Q52: Multi-Act Comparative - Hard - Evolution of Secretary of State Salary Payment
    questions.append(make_q(
        52, "Hard", "Multi-Act Comparative",
        "Which statutory shift in administrative funding regarding the Secretary of State for India occurred between the Charter Act 1793 / GOI Act 1858 and the Government of India Act 1919?",
        "1793 சாசனச் சட்டம் / 1858 அரசுச் சட்டம் மற்றும் 1919 இந்திய அரசுச் சட்டத்திற்கு இடையே இந்திய அரசுச் செயலரின் நிர்வாக நிதி வழங்கலில் ஏற்பட்ட சட்டப்பூர்வ மாற்றம் எது?",
        [
            ("A", "From 1793/1858 his salary was charged on Indian revenues; the 1919 Act mandated that his salary be paid out of the British Exchequer", "1793/1858 முதல் அவரது சம்பளம் இந்திய வருவாயில் சுமத்தப்பட்டது; 1919 சட்டம் அவரது சம்பளத்தை பிரிட்டிஷ் கருவூலத்திலிருந்து வழங்க ஆணையிட்டது"),
            ("B", "From 1793/1858 his salary was paid by British Exchequer; the 1919 Act shifted it to Indian revenues", "1793/1858 முதல் அவரது சம்பளம் பிரிட்டிஷ் கருவூலத்தால் வழங்கப்பட்டது; 1919 சட்டம் அதை இந்திய வருவாய்க்கு மாற்றியது"),
            ("C", "Salary was paid by East India Company share dividends until 1919 when it was completely abolished", "சம்பளம் 1919 வரை கம்பெனி பங்காதாயத்தால் வழங்கப்பட்டு பின்னர் ஒழிக்கப்பட்டது"),
            ("D", "Salary was determined and paid by Provincial Assemblies starting from 1919 Act", "1919 சட்டத்திலிருந்தே மாகாண சபைகளால் சம்பளம் தீர்மானிக்கப்பட்டு வழங்கப்பட்டது")
        ],
        "A",
        "Historical Context: Longstanding nationalist grievance regarding the 'Drain of Wealth' for London home charges.\nReason: Charter Act 1793 (and 1858 Act) mandated Board of Control / Secretary of State salaries be paid out of Indian revenues. The GOI Act 1919 ended this unfair practice by providing that the Secretary of State for India would henceforth be paid directly by the British Exchequer (British Treasury).\nConstitutional Impact: Reduced direct financial drain on Indian revenues for London cabinet office.\nExam Trap: Board of Control/SOS paid from Indian revenues (1793-1919); paid from British Treasury (1919-1947).\nMemory Trick: 1793-1919 = Paid by India; 1919-1947 = Paid by Britain.",
        "வரலாற்றுப் பின்னணி: லண்டன் முகமைச் செலவுகளுக்கான 'செல்வச் சுரண்டல்' பற்றிய தேசியவாதிகளின் நீண்டகாலக் குறைபாடு.\nகாரணம்: 1793 சாசனச் சட்டம் (மற்றும் 1858 சட்டம்) கட்டுப்பாட்டு வாரியம் / அரசுச் செயலர் சம்பளத்தை இந்திய வருவாயிலிருந்து வழங்க விதித்தது. 1919 அரசுச் சட்டம் இம்முறையை முடித்து அரசுச் செயலரின் சம்பளம் பிரிட்டிஷ் கருவூலத்திலிருந்தே வழங்கப்பட வேண்டும் என ஆணையிட்டது.\nஅரசியலமைப்பு தாக்கம்: லண்டன் அலுவலகத்திற்கான இந்திய வருவாய் நிதிச் சுரண்டலைக் குறைத்தது.\nதேர்வுப் பொறி: இந்திய வருவாயில் சம்பளம் (1793-1919); பிரிட்டிஷ் கருவூலத்தில் சம்பளம் (1919-1947).\nநினைவுச் சூத்திரம்: 1793-1919 = இந்தியா செலுத்தியது; 1919-1947 = பிரிட்டன் செலுத்தியது.",
        {
            "A": {"en": "Correct. 1919 Act changed Secretary of State payment from Indian revenue to British Exchequer.", "ta": "சரி. 1919 சட்டம் அரசுச் செயலர் சம்பளத்தை இந்திய வருவாயிலிருந்து பிரிட்டிஷ் கருவூலத்திற்கு மாற்றியது."},
            "B": {"en": "Incorrect. Reverses the actual statutory financial direction.", "ta": "தவறு. சட்டத்தின் நிதியியல் திசையை தலைகீழாக மாற்றுகிறது."},
            "C": {"en": "Incorrect. EIC dividends ended when EIC stock was liquidated in 1874.", "ta": "தவறு. கம்பெனி பங்காதாயம் 1874-ல் முடிந்தது."},
            "D": {"en": "Incorrect. Provincial assemblies had no role in Secretary of State salary.", "ta": "தவறு. மாகாண சபைகளுக்கு அரசுச் செயலர் சம்பளத்தில் தொடர்பில்லை."}
        },
        "TNPSC Trap: Lord Montagu, as Secretary of State for India, announced the August Declaration of 1917 promising responsible government.",
        "TNPSC பொறி: லார்டு மாண்டேகு இந்திய அரசுச் செயலராக இருந்தபோதே பொறுப்பு ஆட்சியை வாக்குறுதி அளித்த 1917 ஆகஸ்ட் அறிவிப்பை வெளியிட்டார்.",
        "August Declaration was made on August 20, 1917, by Montagu in the British House of Commons.",
        "ஆகஸ்ட் அறிவிப்பு 1917 ஆகஸ்ட் 20 அன்று பிரிட்டிஷ் காமன்ஸ் சபையில் மாண்டேகுவால் வெளியிடப்பட்டது.",
        ["Polity", "Historical Background", "GOI Act 1919", "Secretary of State Salary", "Multi-Act Integration", "Grand Test"], "Analyze", 75
    ))

    # Q53: Statement Based - Hard - August Declaration 1917 & GOI Act 1919 Preamble
    questions.append(make_q(
        53, "Hard", "Statement Based",
        "Consider the following statements regarding the August Declaration of 1917 and the Preamble of the Government of India Act 1919:\n1. Edwin Montagu declared that the policy of His Majesty's Government was the increasing association of Indians in every branch of administration.\n2. The Declaration explicitly promised the gradual development of self-governing institutions with a view to the progressive realization of responsible government in India as an integral part of the British Empire.\n3. The Preamble of the 1919 Act explicitly incorporated the principles of the August 1917 Declaration.\nWhich of the statements given above are correct?",
        "1917 ஆகஸ்ட் அறிவிப்பு மற்றும் 1919 இந்திய அரசுச் சட்டத்தின் முகப்புரை பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. நிர்வாகத்தின் ஒவ்வொரு கிளையிலும் இந்தியர்களின் சேர்க்கையை அதிகரிப்பதே பிரிட்டிஷ் அரசின் கொள்கை என எட்வின் மாண்டேகு அறிவித்தார்.\n2. பிரிட்டிஷ் ஏகாதிபத்தியத்தின் ஒருங்கிணைந்த பகுதியாக இந்தியாவில் பொறுப்பு ஆட்சியைப் படிப்படியாக உணர்வதற்காக சுயராஜ்ய நிறுவனங்களின் படிப்படியான வளர்ச்சியை இவ்வறிவிப்பு வெளிப்படையாக வாக்குறுதி அளித்தது.\n3. 1919 சட்டத்தின் முகப்புரை 1917 ஆகஸ்ட் அறிவிப்பின் கொள்கைகளை வெளிப்படையாகத் தன்னகத்தே கொண்டிருந்தது.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
        [
            ("A", "1, 2 and 3", "1, 2 மற்றும் 3"),
            ("B", "1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
            ("C", "2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
            ("D", "1 and 3 only", "1 மற்றும் 3 மட்டுமே")
        ],
        "A",
        "Historical Context: August Declaration (August 20, 1917) defined for the first time the objective of British rule in India.\nReason: All three statements are correct. Edwin Montagu (Secretary of State) made the declaration. Its core objective—'progressive realization of responsible government'—was enacted as the statutory Preamble to the Government of India Act 1919.\nConstitutional Impact: Made responsible government the official statutory goal of British constitutional reforms in India.\nExam Trap: Preamble of 1919 Act defined goal as 'responsible government', NOT 'Dominion Status' or 'Purna Swaraj'.\nMemory Trick: August 1917 Montagu Declaration = Responsible Government = 1919 Preamble.",
        "வரலாற்றுப் பின்னணி: 1917 ஆகஸ்ட் 20 அறிவிப்பு இந்தியாவில் பிரிட்டிஷ் ஆட்சியின் நோக்கத்தை முதன்முறையாக வரையறுத்தது.\nகாரணம்: மூன்று கூற்றுகளும் சரியானவை. எட்வின் மாண்டேகு (அரசுச் செயலர்) இவ்வறிவிப்பைச் செய்தார். இதன் முக்கிய நோக்கம்—'பொறுப்பு ஆட்சியைப் படிப்படியாக நிறுவுதல்'—1919 இந்திய அரசுச் சட்டத்தின் முகப்புரையாக இயற்றப்பட்டது.\nஅரசியலமைப்பு தாக்கம்: பொறுப்பு ஆட்சியை பிரிட்டிஷ் அரசியலமைப்பு சீர்திருத்தங்களின் அதிகாரப்பூர்வ சட்டப்பூர்வ இலக்காக மாற்றியது.\nதேர்வுப் பொறி: 1919 சட்டத்தின் முகப்புரை இலக்கை 'பொறுப்பு ஆட்சி' என வரையறுத்தது, 'டொமினியன் அந்தஸ்து' அல்லது 'பூரண சுயராஜ்யம்' அல்ல.\nநினைவுச் சூத்திரம்: ஆகஸ்ட் 1917 மாண்டேகு அறிவிப்பு = பொறுப்பு ஆட்சி = 1919 முகப்புரை.",
        {
            "A": {"en": "Correct. All three statements accurately describe the 1917 Declaration and 1919 Act Preamble.", "ta": "சரி. 1917 அறிவிப்பு மற்றும் 1919 சட்ட முகப்புரை பற்றிய மூன்று கூற்றுகளும் சரியானவை."},
            "B": {"en": "Incorrect. Statement 3 is also correct.", "ta": "தவறு. கூற்று 3-ம் சரியானது."},
            "C": {"en": "Incorrect. Statement 1 is also correct.", "ta": "தவறு. கூற்று 1-ம் சரியானது."},
            "D": {"en": "Incorrect. Statement 2 is also correct.", "ta": "தவறு. கூற்று 2-ம் சரியானது."}
        },
        "TNPSC Trap: Preamble of 1919 Act remained unchanged and was retained in the Government of India Act 1935 as its guiding spirit.",
        "TNPSC பொறி: 1919 சட்டத்தின் முகப்புரை மாற்றப்படாமல் 1935 இந்திய அரசுச் சட்டத்திலும் அதன் வழிகாட்டும் உணர்வாகத் தக்கவைக்கப்பட்டது.",
        "August Declaration was hailed by Moderate leaders like Surendranath Banerjea as the 'Magna Carta of India'.",
        "ஆகஸ்ட் அறிவிப்பு சுரேந்திரநாத் பானர்ஜி போன்ற மிதவாதிகளால் 'இந்தியாவின் மகாசாசனம்' எனப் போற்றப்பட்டது.",
        ["Polity", "Historical Background", "August Declaration 1917", "GOI Act 1919 Preamble", "Grand Test"], "Analyze", 75
    ))

    # Q54: Conceptual MCQ - Medium - 1919 Provincial Reserved vs Transferred Subjects
    questions.append(make_q(
        54, "Medium", "Conceptual MCQ",
        "Which of the following lists correctly categorizes subjects into 'Reserved' and 'Transferred' under Provincial Dyarchy of the Government of India Act 1919?",
        "1919 இந்திய அரசுச் சட்டத்தின் மாகாண இரட்டை ஆட்சியில் 'ஒதுக்கப்பட்டவை' மற்றும் 'மாற்றப்பட்டவை' துறைகளைச் சரியாக வகைப்படுத்தும் பட்டியல் எது?",
        [
            ("A", "Reserved: Land Revenue, Finance, Police, Justice; Transferred: Education, Public Health, Agriculture, Local Self-Government", "ஒதுக்கப்பட்டவை: நில வருவாய், நிதி, காவல்துறை, நீதி; மாற்றப்பட்டவை: கல்வி, பொது சுகாதாரம், வேளாண்மை, உள்ளாட்சி"),
            ("B", "Reserved: Education, Public Health; Transferred: Police, Finance, Land Revenue", "ஒதுக்கப்பட்டவை: கல்வி, பொது சுகாதாரம்; மாற்றப்பட்டவை: காவல்துறை, நிதி, நில வருவாய்"),
            ("C", "Reserved: Local Self-Government, Agriculture; Transferred: Defense, Foreign Affairs", "ஒதுக்கப்பட்டவை: உள்ளாட்சி, வேளாண்மை; மாற்றப்பட்டவை: பாதுகாப்பு, வெளியுறவு விவகாரங்கள்"),
            ("D", "Reserved: All Provincial Subjects; Transferred: All Central Subjects", "ஒதுக்கப்பட்டவை: அனைத்து மாகாணத் துறைகளும்; மாற்றப்பட்டவை: அனைத்து மத்தியத் துறைகளும்")
        ],
        "A",
        "Historical Context: Operational mechanism of Dyarchy in Indian provinces under 1919 Act.\nReason: 'Reserved' subjects (key revenue and security functions like Land Revenue, Finance, Police, Justice, Irrigation) were administered by Governor with his Executive Council. 'Transferred' subjects (nation-building services like Education, Public Health, Agriculture, Local Self-Government) were administered by Governor with elected Ministers.\nConstitutional Impact: Starved nation-building ministers of funds controlled by Reserved Finance department.\nExam Trap: Defense & Foreign Affairs were Central subjects, NOT Provincial subjects.\nMemory Trick: Reserved = Money & Power (Police/Finance); Transferred = Public Services (School/Hospital).",
        "வரலாற்றுப் பின்னணி: 1919 சட்டத்தின் கீழ் மாகாணங்களில் இரட்டை ஆட்சியின் செயல்பாட்டு முறை.\nகாரணம்: 'ஒதுக்கப்பட்ட' துறைகள் (நில வருவாய், நிதி, காவல்துறை, நீதி, பாசனம்) கவர்னர் மற்றும் அவரது நிர்வாகக் குழுவால் நிர்வகிக்கப்பட்டன. 'மாற்றப்பட்ட' துறைகள் (கல்வி, பொது சுகாதாரம், வேளாண்மை, உள்ளாட்சி) தேர்ந்தெடுக்கப்பட்ட அமைச்சர்களுடன் கவர்னரால் நிர்வகிக்கப்பட்டன.\nஅரசியலமைப்பு தாக்கம்: மாற்றப்பட்ட துறை அமைச்சர்களுக்கு நிதி கிடைக்காமல் ஒதுக்கீடு நிதித்துறை முடக்கியது.\nதேர்வுப் பொறி: பாதுகாப்பு, வெளியுறவு ஆகியவை மத்தியத் துறைகள், மாகாணத் துறைகள் அல்ல.\nநினைவுச் சூத்திரம்: ஒதுக்கப்பட்டவை = பணம் & அதிகாரம் (காவல்/நிதி); மாற்றப்பட்டவை = மக்கள் சேவை (பள்ளி/மருத்துவமனை).",
        {
            "A": {"en": "Correct classification of Reserved and Transferred provincial subjects under 1919 Act.", "ta": "சரி. 1919 சட்டத்தில் ஒதுக்கப்பட்ட மற்றும் மாற்றப்பட்ட மாகாணத் துறைகளின் சரியான வகைப்பாடு."},
            "B": {"en": "Incorrect. Reverses Reserved and Transferred categories.", "ta": "தவறு. ஒதுக்கப்பட்ட, மாற்றப்பட்ட துறைகளை தலைகீழாக மாற்றுகிறது."},
            "C": {"en": "Incorrect. Defense and Foreign Affairs were Central subjects.", "ta": "தவறு. பாதுகாப்பு, வெளியுறவு ஆகியவை மத்தியத் துறைகள்."},
            "D": {"en": "Incorrect. Both categories were sub-divisions of Provincial subjects.", "ta": "தவறு. இரண்டும் மாகாணத் துறைகளின் உள் பிரிவுகளாகும்."}
        },
        "TNPSC Trap: Finance was a Reserved subject under 1919 Act; hence Transferred ministers were financially dependent on the Reserved Executive Council member.",
        "TNPSC பொறி: 1919 சட்டத்தில் நிதி ஒதுக்கப்பட்ட துறையாக இருந்தது; எனவே மாற்றப்பட்ட துறை அமைச்சர்கள் நிதிக்காக ஒதுக்கப்பட்ட துறை உறுப்பினரைச் சார்ந்திருந்தனர்.",
        "Governor could override Transferred ministers using special veto powers.",
        "கவர்னர் தனது சிறப்புத் தடுப்பதிகாரத்தைப் பயன்படுத்தி மாற்றப்பட்ட துறை அமைச்சர்களை நிராகரிக்க முடியும்.",
        ["Polity", "Historical Background", "GOI Act 1919", "Reserved Transferred Subjects", "Grand Test"], "Understand", 60
    ))

    # Q55: Multi-Act Comparative - Hard - Evolution of Executive Responsibility
    questions.append(make_q(
        55, "Hard", "Multi-Act Comparative",
        "Which inference accurately contrasts the executive responsibility in Provinces under the 1919 Act versus the 1935 Act?",
        "1919 சட்டம் மற்றும் 1935 சட்டத்தின் கீழ் மாகாணங்களில் நிலவிய நிர்வாகப் பொறுப்புக்கூறலை துல்லியமாக வேறுபடுத்திக் காட்டும் முடிவு எது?",
        [
            ("A", "Under 1919 Act executive responsibility was dual and partial (only Transferred ministers responsible to legislature), whereas under 1935 Act full executive responsibility was established across all provincial subjects (Provincial Autonomy)", "1919 சட்டத்தில் நிர்வாகப் பொறுப்பு இரட்டையாகவும் பகுதியாகவும் இருந்தது (மாற்றப்பட்ட அமைச்சர்கள் மட்டுமே சட்டமன்றத்திற்குப் பொறுப்பு); ஆனால் 1935 சட்டத்தில் அனைத்து மாகாணத் துறைகளிலும் முழு நிர்வாகப் பொறுப்பு நிறுவப்பட்டது (மாகாண தன்னாட்சி)"),
            ("B", "Under 1919 Act ministers were fully responsible for all subjects, whereas under 1935 Act all ministers were made responsible to the Governor-General only", "1919 சட்டத்தில் அனைத்துத் துறைகளுக்கும் அமைச்சர்கள் முழுப் பொறுப்பேற்றனர்; 1935 சட்டத்தில் அனைத்து அமைச்சர்களும் கவர்னர்-ஜெனரலுக்கு மட்டுமே பொறுப்பாக்கப்பட்டனர்"),
            ("C", "Under 1919 Act Governor had no veto powers, whereas under 1935 Act Governor became an absolute dictator without ministers", "1919 சட்டத்தில் கவர்னருக்கு தடுப்பதிகாரம் இல்லை; 1935 சட்டத்தில் கவர்னர் அமைச்சர்களின்றி சர்வாதிகாரியானார்"),
            ("D", "There was no difference in executive responsibility between 1919 and 1935 Acts", "1919 மற்றும் 1935 சட்டங்களுக்கு இடையே நிர்வாகப் பொறுப்பில் எந்த வேறுபாடும் இல்லை")
        ],
        "A",
        "Historical Context: The shift from partial responsible government in provinces to complete provincial executive responsibility.\nReason: 1919 Act instituted Dyarchy (only Transferred ministers responsible to provincial legislature; Reserved executive council responsible to Crown). 1935 Act abolished Dyarchy in provinces, placing ALL provincial subjects under ministers collectively responsible to the elected provincial legislature (Provincial Autonomy).\nConstitutional Impact: Prototype for responsible cabinet government in Indian States (Article 163/164).\nExam Trap: 1919 = Partial responsibility (Dyarchy); 1935 = Full provincial responsibility (Autonomy).\nMemory Trick: 1919 = Split Responsibility; 1935 = Total Provincial Ministerial Responsibility.",
        "வரலாற்றுப் பின்னணி: மாகாணங்களில் பகுதிப் பொறுப்பு ஆட்சியிலிருந்து முழு மாகாண நிர்வாகப் பொறுப்பிற்கு மாறுதல்.\nகாரணம்: 1919 சட்டம் இரட்டை ஆட்சியை நிறுவியது (மாற்றப்பட்ட அமைச்சர்கள் மட்டுமே சட்டமன்றத்திற்குப் பொறுப்பு; ஒதுக்கப்பட்ட உறுப்பினர்கள் முடி ஆட்சிக்குப் பொறுப்பு). 1935 சட்டம் மாகாண இரட்டை ஆட்சியை ஒழித்து அனைத்துத் துறைகளையும் சட்டமன்றத்திற்குப் பொறுப்பான அமைச்சர்களின் கீழ் கொண்டுவந்தது (மாகாண தன்னாட்சி).\nஅரசியலமைப்பு தாக்கம்: இந்திய மாநிலங்களில் பொறுப்பான கேபினட் ஆட்சிக்கு (சரத்து 163/164) முன்மாதிரியானது.\nதேர்வுப் பொறி: 1919 = பகுதிப் பொறுப்பு (இரட்டை ஆட்சி); 1935 = முழு மாகாணப் பொறுப்பு (தன்னாட்சி).\nநினைவுச் சூத்திரம்: 1919 = பிளவுபட்ட பொறுப்பு; 1935 = முழு மாகாண அமைச்சரவைப் பொறுப்பு.",
        {
            "A": {"en": "Correct. 1919 had partial responsibility (Dyarchy); 1935 achieved full provincial ministerial responsibility.", "ta": "சரி. 1919 பகுதிப் பொறுப்பைக் கொண்டிருந்தது; 1935 முழு மாகாண அமைச்சரவைப் பொறுப்பைக் கொண்டுவந்தது."},
            "B": {"en": "Incorrect. Reverses the constitutional evolution.", "ta": "தவறு. அரசியலமைப்பு வளர்ச்சியை தலைகீழாக மாற்றுகிறது."},
            "C": {"en": "Incorrect. Governor had veto in both Acts, but 1935 established ministerial council.", "ta": "தவறு. இரு சட்டங்களிலும் கவர்னருக்கு தடுப்பதிகாரம் இருந்தது."},
            "D": {"en": "Incorrect. Significant structural difference existed between Dyarchy and Autonomy.", "ta": "தவறு. இரட்டை ஆட்சிக்கும் தன்னாட்சிக்கும் முக்கிய கட்டமைப்பு வேறுபாடு இருந்தது."}
        },
        "TNPSC Trap: Provincial Ministers under 1935 Act were appointed by Governor, but had to be members of provincial legislature and held collective responsibility.",
        "TNPSC பொறி: 1935 சட்டத்தில் மாகாண அமைச்சர்கள் கவர்னரால் நியமிக்கப்பட்டனர், ஆனால் அவர்கள் சட்டமன்ற உறுப்பினர்களாக இருக்க வேண்டும் மற்றும் கூட்டுப் பொறுப்பு வகித்தனர்.",
        "Collective responsibility of ministers to the legislature was established statutorily in provinces under 1935 Act.",
        "சட்டமன்றத்திற்கு அமைச்சர்களின் கூட்டுப் பொறுப்புக்கூறல் 1935 சட்டத்தின் கீழ் மாகாணங்களில் சட்டப்பூர்வமாக நிறுவப்பட்டது.",
        ["Polity", "Historical Background", "GOI Act 1919", "GOI Act 1935", "Executive Responsibility", "Multi-Act Integration", "Grand Test"], "Analyze", 75
    ))

    # Q56: Statement Based - Hard - Nehru Report 1928 & Constitutional Proposals
    questions.append(make_q(
        56, "Hard", "Statement Based",
        "Consider the following statements regarding the Nehru Report of 1928 drafted under Motilal Nehru:\n1. It was the first major attempt by Indians to draft an outline for a constitution for independent India.\n2. It recommended Dominion Status for India as the form of government.\n3. It recommended joint electorates with reservation of seats for minorities instead of separate electorates.\n4. It contained a comprehensive Bill of Rights guaranteeing nineteen fundamental rights.\nWhich of the statements given above are correct?",
        "மோதிலால் நேரு தலைமையில் வரைவு செய்யப்பட்ட 1928 நேரு அறிக்கை பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது சுதந்திர இந்தியாவின் அரசியலமைப்பு வரைவை வரைவதற்கு இந்தியர்களால் மேற்கொள்ளப்பட்ட முதல் முக்கிய முயற்சியாகும்.\n2. இது இந்தியாவிற்கு டொமினியன் அந்தஸ்தை (Dominion Status) அரசு வடிவமாகப் பரிந்துரைத்தது.\n3. இது தனித் தொகுதிகளுக்குப் பதிலாக சிறுபான்மையினருக்கு இடஒதுக்கீட்டுடன் கூடிய கூட்டுக் தொகுதிகளைப் பரிந்துரைத்தது.\n4. இது பத்தொன்பது அடிப்படை உரிமைகளுக்கு உத்தரவாதம் அளிக்கும் விரிவான உரிமைச் சாசனத்தைக் கொண்டிருந்தது.\nமேற்கொள்கிற கூற்றுகளில் எவை சரியானவை?",
        [
            ("A", "1, 2, 3 and 4", "1, 2, 3 மற்றும் 4"),
            ("B", "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டுமே"),
            ("C", "1 and 4 only", "1 மற்றும் 4 மட்டுமே"),
            ("D", "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டுமே")
        ],
        "A",
        "Historical Context: Drafted by All-Parties Conference committee in response to Lord Birkenhead's challenge that Indians could not produce an agreed constitution.\nReason: All four statements are correct. Nehru Report (1928) demanded Dominion Status (Statement 2), Joint Electorates (Statement 3), 19 Fundamental Rights (Statement 4), secular state, universal adult suffrage, and federal structure with residuary powers to Provinces.\nConstitutional Impact: Precursor to Fundamental Rights (Part III) and secular federal framework in modern Indian Constitution.\nExam Trap: Nehru Report assigned residuary powers to PROVINCES; 1935 Act assigned residuary powers to GOVERNOR-GENERAL; Modern Constitution assigns to UNION PARLIAMENT.\nMemory Trick: Nehru Report 1928 = Dominion Status + Joint Electorates + 19 Fundamental Rights.",
        "வரலாற்றுப் பின்னணி: இந்தியர்களால் ஒப்புக் கொள்ளப்பட்ட அரசியலமைப்பை உருவாக்க முடியாது என்ற லார்டு பர்க்கன்ஹெட்டின் சவாலுக்கு பதிலளிக்கும் விதமாக அனைத்துக் கட்சி மாநாட்டுக் குழுவால் வரைவு செய்யப்பட்டது.\nகாரணம்: நான்கு கூற்றுகளும் சரியானவை. நேரு அறிக்கை (1928) டொமினியன் அந்தஸ்து (கூற்று 2), கூட்டுக் தொகுதிகள் (கூற்று 3), 19 அடிப்படை உரிமைகள் (கூற்று 4), மதச்சார்பற்ற அரசு, உலகளாவிய வயதுவந்தோர் வாக்குரிமை ஆகியவற்றை வலியுறுத்தியது.\nஅரசியலமைப்பு தாக்கம்: நவீன இந்திய அரசியலமைப்பின் அடிப்படை உரிமைகள் (பகுதி III) மற்றும் மதச்சார்பற்ற கூட்டாட்சிக்கு முன்னோடியானது.\nதேர்வுப் பொறி: நேரு அறிக்கை எஞ்சிய அதிகாரங்களை மாகாணங்களுக்கு அளித்தது; 1935 சட்டம் கவர்னர்-ஜெனரலுக்கு அளித்தது; நவீன அரசியலமைப்பு ஒன்றிய நாடாளுமன்றத்திற்கு அளித்துள்ளது.\nநினைவுச் சூத்திரம்: நேரு அறிக்கை 1928 = டொமினியன் அந்தஸ்து + கூட்டுக் தொகுதி + 19 அடிப்படை உரிமைகள்.",
        {
            "A": {"en": "Correct. All four statements accurately state features of the 1928 Nehru Report.", "ta": "சரி. 1928 நேரு அறிக்கையின் நான்கு கூற்றுகளும் துல்லியமாக சரியானவை."},
            "B": {"en": "Incorrect. Statement 4 is also correct.", "ta": "தவறு. கூற்று 4-ம் சரியானது."},
            "C": {"en": "Incorrect. Statements 2 and 3 are also correct.", "ta": "தவறு. கூற்றுகள் 2 மற்றும் 3-ம் சரியானவை."},
            "D": {"en": "Incorrect. Statement 1 is also correct.", "ta": "தவறு. கூற்று 1-ம் சரியானது."}
        },
        "TNPSC Trap: Nehru Report proposed Residuary Powers to be vested in Provinces, unlike the 1935 Act (Governor-General) and modern Constitution (Center).",
        "TNPSC பொறி: நேரு அறிக்கை எஞ்சிய அதிகாரங்களை மாகாணங்களிடம் வழங்க பரிந்துரைத்தது (1935 சட்டத்திலும் நவீன அரசியலமைப்பிலும் வேறுபட்டது).",
        "Jinnah rejected Nehru Report and produced his '14 Points' in 1929 demanding separate electorates.",
        "ஜின்னா நேரு அறிக்கையை நிராகரித்து தனித் தொகுதிகளை வலியுறுத்தி 1929-ல் தனது '14 கோரிக்கைகளை' வெளியிட்டார்.",
        ["Polity", "Historical Background", "Nehru Report 1928", "Fundamental Rights Precursor", "Grand Test"], "Analyze", 75
    ))

    # Q57: Direct MCQ - Easy - Communal Award 1932 & Poona Pact
    questions.append(make_q(
        57, "Easy", "Direct MCQ",
        "The historic Poona Pact of September 1932 was signed between Mahatma Gandhi and Dr. B.R. Ambedkar to modify which British constitutional announcement?",
        "செப்டம்பர் 1932-ல் மகாத்மா காந்தி மற்றும் டாக்டர் பி.ஆர். அம்பேத்கர் இடையே கையெழுத்தான வரலாற்றுச் சிறப்புமிக்க பூனா ஒப்பந்தம் பிரிட்டிஷாரின் எந்த அரசியலமைப்பு அறிவிப்பைத் திருத்துவதற்காக மேற்கொள்ளப்பட்டது?",
        [
            ("A", "Communal Award announced by British Prime Minister Ramsay MacDonald", "பிரிட்டிஷ் பிரதமர் ராம்சே மெக்டொனால்டால் அறிவிக்கப்பட்ட வகுப்புவாத கொடை (Communal Award)"),
            ("B", "Simon Commission Recommendations", "சைமன் குழுவின் பரிந்துரைகள்"),
            ("C", "White Paper on Constitutional Reforms 1933", "1833 அரசியலமைப்பு சீர்திருத்தங்கள் பற்றிய வெள்ளை அறிக்கை"),
            ("D", "August Declaration of 1917", "1917 ஆகஸ்ட் அறிவிப்பு")
        ],
        "A",
        "Historical Context: British Prime Minister Ramsay MacDonald announced the Communal Award in August 1932 extending separate electorates to Depressed Classes.\nReason: Gandhiji undertook a fast unto death in Yerwada Jail (Pune) protesting separate electorates for Depressed Classes as a plot to divide Hindu society. Poona Pact retained joint electorates for Depressed Classes while increasing reserved seats from 71 to 147 in provincial legislatures.\nConstitutional Impact: Incorporated into Government of India Act 1935 as reserved seats under joint electorates.\nExam Trap: Communal Award = Separate electorates for Depressed Classes; Poona Pact = Reserved seats under Joint Electorates.\nMemory Trick: Communal Award 1932 (MacDonald) $\rightarrow$ Poona Pact 1932 (Gandhi & Ambedkar).",
        "வரலாற்றுப் பின்னணி: பிரிட்டிஷ் பிரதமர் ராம்சே மெக்டொனால்ட் 1932 ஆகஸ்டில் ஒடுக்கப்பட்ட வகுப்பினருக்குத் தனித் தொகுதியை விரிவுபடுத்தி வகுப்புவாத கொடையை அறிவித்தார்.\nகாரணம்: இந்து சமூகத்தைப் பிளவுபடுத்தும் இத்திட்டத்தை எதிர்த்து காந்தியடிகள் புனே எரவாடா சிறையில் சாகும் வரை உண்ணாவிரதம் இருந்தார். பூனா ஒப்பந்தம் தனித் தொகுதியைத் தவிர்த்து கூட்டுக் தொகுதியைத் தக்கவைத்து மாகாண சபைகளில் ஒதுக்கீட்டு இடங்களை 71-லிருந்து 147 ஆக உயர்த்தியது.\nஅரசியலமைப்பு தாக்கம்: 1935 இந்திய அரசுச் சட்டத்தில் கூட்டுக் தொகுதியின் கீழ் இடஒதுக்கீடாக இணைக்கப்பட்டது.\nதேர்வுப் பொறி: வகுப்புவாத கொடை = ஒடுக்கப்பட்டோருக்கு தனித் தொகுதி; பூனா ஒப்பந்தம் = கூட்டுக் தொகுதியில் இடஒதுக்கீடு.\nநினைவுச் சூத்திரம்: வகுப்புவாத கொடை 1932 (மெக்டொனால்ட்) $\rightarrow$ பூனா ஒப்பந்தம் 1932 (காந்தி & அம்பேத்கர்).",
        {
            "A": {"en": "Correct. Poona Pact modified Ramsay MacDonald's Communal Award of August 1932.", "ta": "சரி. பூனா ஒப்பந்தம் 1932 ஆகஸ்டில் ராம்சே மெக்டொனால்டின் வகுப்புவாத கொடையைத் திருத்தியது."},
            "B": {"en": "Incorrect. Simon Commission was in 1927/1930.", "ta": "தவறு. சைமன் குழு 1927/1930-ல் இயங்கியது."},
            "C": {"en": "Incorrect. White Paper came in 1933 after the Round Table Conferences.", "ta": "தவறு. வெள்ளை அறிக்கை 1933-ல் வந்தது."},
            "D": {"en": "Incorrect. August Declaration was in 1917.", "ta": "தவறு. ஆகஸ்ட் அறிவிப்பு 1917-ல் வந்தது."}
        },
        "TNPSC Trap: Poona Pact was signed by Madan Mohan Malaviya on behalf of caste Hindus and Dr. B.R. Ambedkar on behalf of Depressed Classes.",
        "TNPSC பொறி: பூனா ஒப்பந்தத்தில் சாதி இந்துக்கள் சார்பில் மதன் மோகன் மாளவியாவும் ஒடுக்கப்பட்டோர் சார்பில் டாக்டர் பி.ஆர். அம்பேத்கரும் கையெழுத்திட்டனர்.",
        "Poona Pact increased reserved seats for Depressed Classes in provincial legislatures from 71 to 147.",
        "பூனா ஒப்பந்தம் மாகாண சட்டமன்றங்களில் ஒடுக்கப்பட்டோருக்கான இடங்களை 71-லிருந்து 147 ஆக உயர்த்தியது.",
        ["Polity", "Historical Background", "Communal Award 1932", "Poona Pact", "Grand Test"], "Remember", 45
    ))

    # Q58: Conceptual MCQ - Medium - Indian Councils Act 1909 Legislative Discussions
    questions.append(make_q(
        58, "Medium", "Conceptual MCQ",
        "Under the Indian Councils Act of 1909 (Morley-Minto Reforms), which new deliberative right was granted to members of the Central and Provincial Legislative Councils?",
        "1909 ஆம் ஆண்டின் இந்தியக் கவுன்சில்கள் சட்டத்தின் (மோலி-மிண்டோ சீர்திருத்தங்கள்) கீழ் மத்திய மற்றும் மாகாண சட்ட மேலவை உறுப்பினர்களுக்கு வழங்கப்பட்ட புதிய விவாத உரிமை எது?",
        [
            ("A", "Right to ask supplementary questions and move resolutions on the budget and matters of general public interest", "துணைக்கேள்விகள் கேட்கவும், பட்ஜெட் மற்றும் பொது நலன் சார்ந்த விவகாரங்களில் தீர்மானங்களைக் கொண்டுவரவும் உரிமை"),
            ("B", "Right to vote on and reject the entire annual budget", "முழு ஆண்டறிக்கை பட்ஜெட்டிற்கும் வாக்களித்து அதை நிராகரிக்கும் உரிமை"),
            ("C", "Right to remove the Governor-General by a vote of no confidence", "நம்பிக்கையில்லாத் தீர்மானம் மூலம் கவர்னர்-ஜெனரலைப் பதவியிலிருந்து நீக்கும் உரிமை"),
            ("D", "Right to directly appoint provincial judges and civil servants", "மாகாண நீதிபதிகள் மற்றும் சிவில் அதிகாரிகளை நேரடியாக நியமிக்கும் உரிமை")
        ],
        "A",
        "Historical Context: Expanding deliberative functions of legislative councils under 1909 Act.\nReason: The 1909 Act enlarged the deliberative functions of legislative councils. Members were allowed to ask supplementary questions, move resolutions on the budget (except non-voteable heads like defense/interest), and move resolutions on matters of general public interest.\nConstitutional Impact: Advanced legislative debate standards prior to full voting powers.\nExam Trap: 1892 allowed asking questions on budget (no supplementary questions); 1909 allowed supplementary questions & resolutions.\nMemory Trick: 1892 = Ask Questions; 1909 = Ask Supplementary Questions & Move Resolutions.",
        "வரலாற்றுப் பின்னணி: 1909 சட்டத்தின் கீழ் சட்ட மேலவைகளின் விவாதப் பணிகளை விரிவுபடுத்துதல்.\nகாரணம்: 1909 சட்டம் சட்ட மேலவைகளின் விவாதப் பணிகளைப் பெரிதாக்கியது. உறுப்பினர்கள் துணைக்கேள்விகள் கேட்கவும், பட்ஜெட் மீது தீர்மானம் கொண்டுவரவும் (பாதுகாப்பு/வட்டி தவிர), பொது நலன் சார்ந்த விவகாரங்களில் தீர்மானம் கொண்டுவரவும் அனுமதிக்கப்பட்டனர்.\nஅரசியலமைப்பு தாக்கம்: வாக்களிக்கும் முழு அதிகாரத்திற்கு முன் சட்டமன்ற விவாதத் தரத்தை உயர்த்தியது.\nதேர்வுப் பொறி: 1892 பட்ஜெட்டில் கேள்விகள் கேட்க அனுமதித்தது (துணைக்கேள்விகள் இல்லை); 1909 துணைக்கேள்விகள் மற்றும் தீர்மானங்களை அனுமதித்தது.\nநினைவுச் சூத்திரம்: 1892 = கேள்விகள் கேள்; 1909 = துணைக்கேள்விகள் கேள் & தீர்மானம் கொண்டுவா.",
        {
            "A": {"en": "Correct. 1909 Act granted rights to ask supplementary questions and move budget resolutions.", "ta": "சரி. 1909 சட்டம் துணைக்கேள்விகள் கேட்கவும் பட்ஜெட் தீர்மானங்கள் கொண்டுவரவும் உரிமை அளித்தது."},
            "B": {"en": "Incorrect. Full voting on budget was not permitted in 1909.", "ta": "தவறு. பட்ஜெட்டிற்கு முழு வாக்களிப்பு 1909-ல் அனுமதிக்கப்படவில்லை."},
            "C": {"en": "Incorrect. Legislative councils had no power over Governor-General's tenure.", "ta": "தவறு. கவர்னர்-ஜெனரல் பதவிக்காலம் மீது மேலவைக்கு அதிகாரம் இல்லை."},
            "D": {"en": "Incorrect. Executive appointment powers remained with the Crown/Viceroy.", "ta": "தவறு. நியமன அதிகாரங்கள் வைஸ்ராய்/அரசரிடமே இருந்தன."}
        },
        "TNPSC Trap: Resolutions passed by Legislative Councils under 1909 Act were purely ADVISORY in nature and not binding on the executive.",
        "TNPSC பொறி: 1909 சட்டத்தின் கீழ் சட்ட மேலவைகள் நிறைவேற்றிய தீர்மானங்கள் வெறும் ஆலோசனைத் தன்மை கொண்டவை, நிர்வாகத்தைக் கட்டுப்படுத்தாது.",
        "Supplementary questions allowed members to cross-examine government members on their answers.",
        "துணைக்கேள்விகள் அரசு உறுப்பினர்களின் பதில்களை குறுக்கு விசாரணை செய்ய பிரதிநிதிகளுக்கு உதவியது.",
        ["Polity", "Historical Background", "Indian Councils Act 1909", "Supplementary Questions", "Grand Test"], "Understand", 60
    ))

    # Q59: Multi-Act Comparative - Hard - Evolution of Federal Court to Supreme Court
    questions.append(make_q(
        59, "Hard", "Multi-Act Comparative",
        "Which comparative transition accurately tracks the judicial evolution from the Federal Court of India (under 1935 Act) to the Supreme Court of India (under 1950 Constitution)?",
        "1935 சட்டத்தின் கீழ் அமைந்த கூட்டாட்சி நீதிமன்றத்திலிருந்து 1950 அரசியலமைப்பின் கீழ் அமைந்த இந்திய உச்ச நீதிமன்றத்திற்கு நிகழ்ந்த நீதித்துறை வளர்ச்சியைத் துல்லியமாக ஒப்பீடு செய்யும் கூற்று எது?",
        [
            ("A", "The Federal Court (1937) had limited jurisdiction and its decisions were subject to appeal before the Privy Council in London, whereas the Supreme Court of India (1950) replaced both Federal Court and Privy Council, becoming the apex judicial body with supreme appellate authority", "கூட்டாட்சி நீதிமன்றம் (1937) வரம்பிற்குட்பட்ட அதிகார வரம்பைக் கொண்டு லண்டன் ப்ரிவி கவுன்சிலுக்குக் கீழ்மைப்பட்டிருந்தது; ஆனால் இந்திய உச்ச நீதிமன்றம் (1950) கூட்டாட்சி நீதிமன்றம் மற்றும் ப்ரிவி கவுன்சில் இரண்டையும் பதிலீடு செய்து உச்ச மேல்முறையீட்டு அதிகார வரம்பைக் கொண்ட உயர்ந்த நீதி அமைப்பானது"),
            ("B", "The Federal Court had wider powers than modern Supreme Court because it could strike down Acts of British Parliament", "கூட்டாட்சி நீதிமன்றம் பிரிட்டிஷ் நாடாளுமன்றச் சட்டங்களை ரத்து செய்ய முடிந்ததால் நவீன உச்ச நீதிமன்றத்தை விட அதிக அதிகாரம் கொண்டிருந்தது"),
            ("C", "The Federal Court operated in London while Supreme Court operates in New Delhi", "கூட்டாட்சி நீதிமன்றம் லண்டனில் இயங்கியது; உச்ச நீதிமன்றம் புதுடெல்லியில் இயங்குகிறது"),
            ("D", "There was no institutional connection or continuity between Federal Court and Supreme Court of India", "கூட்டாட்சி நீதிமன்றத்திற்கும் இந்திய உச்ச நீதிமன்றத்திற்கும் இடையே எந்தவொரு நிறுவனத் தொடர்போ தொடர்ச்சியோ இல்லை")
        ],
        "A",
        "Historical Context: Evolution of Indian supreme judicial hierarchy from colonial subordination to independent sovereignty.\nReason: Federal Court set up under 1935 Act (inaugurated Oct 1, 1937) was not the ultimate court of appeal; appeals went to Privy Council in London. In 1949, Privy Council jurisdiction was abolished. On Jan 28, 1950, Supreme Court of India was inaugurated, succeeding both Federal Court and Privy Council appellate jurisdiction.\nConstitutional Impact: Established complete judicial sovereignty for independent India.\nExam Trap: Federal Court was established in 1937; Supreme Court of India succeeded it on Jan 28, 1950.\nMemory Trick: Federal Court (1937) + Privy Council (London) $\rightarrow$ Supreme Court of India (Jan 28, 1950).",
        "வரலாற்றுப் பின்னணி: காலனித்துவக் கீழ்மையிலிருந்து சுதந்திர இறையாண்மை வரை இந்திய உச்ச நீதித்துறை படிநிலையின் வளர்ச்சி.\nகாரணம்: 1935 சட்டத்தில் அமைந்த கூட்டாட்சி நீதிமன்றம் (1937 அக்டோபர் 1 திறப்பு) இறுதி மேல்முறையீட்டு மன்றமல்ல; மேல்முறையீடுகள் லண்டன் ப்ரிவி கவுன்சிலுக்குச் சென்றன. 1949-ல் ப்ரிவி கவுன்சில் வரம்பு ஒழிக்கப்பட்டது. 1950 ஜனவரி 28 அன்று இந்திய உச்ச நீதிமன்றம் தொடங்கப்பட்டு கூட்டாட்சி நீதிமன்றம் மற்றும் ப்ரிவி கவுன்சில் இரண்டின் அதிகாரங்களையும் பெற்றது.\nஅரசியலமைப்பு தாக்கம்: சுதந்திர இந்தியாவிற்கு முழுமையான நீதித்துறை இறையாண்மையை நிறுவியது.\nதேர்வுப் பொறி: கூட்டாட்சி நீதிமன்றம் அமைந்தது 1937; இந்திய உச்ச நீதிமன்றம் அதை பதிலீடு செய்தது ஜனவரி 28, 1950.\nநினைவுச் சூத்திரம்: கூட்டாட்சி நீதிமன்றம் (1937) + ப்ரிவி கவுன்சில் (லண்டன்) $\rightarrow$ இந்திய உச்ச நீதிமன்றம் (ஜனவரி 28, 1950).",
        {
            "A": {"en": "Correct. Supreme Court of India replaced both Federal Court of India and Judicial Committee of Privy Council.", "ta": "சரி. இந்திய உச்ச நீதிமன்றம் கூட்டாட்சி நீதிமன்றம் மற்றும் லண்டன் ப்ரிவி கவுன்சில் இரண்டையும் பதிலீடு செய்தது."},
            "B": {"en": "Incorrect. Federal Court could not strike down British Parliamentary statutes.", "ta": "தவறு. கூட்டாட்சி நீதிமன்றத்திற்கு பிரிட்டிஷ் சட்டங்களை ரத்து செய்ய அதிகாரம் இல்லை."},
            "C": {"en": "Incorrect. Federal Court operated in Delhi (Princes Chamber), not London.", "ta": "தவறு. கூட்டாட்சி நீதிமன்றம் டெல்லியில் இயங்கியது."},
            "D": {"en": "Incorrect. Supreme Court directly inherited Federal Court premises and judges.", "ta": "தவறு. உச்ச நீதிமன்றம் கூட்டாட்சி நீதிமன்றத்தின் வளாகத்தையும் நீதிபதிகளையும் நேரடியாகப் பெற்றது."}
        },
        "TNPSC Trap: Supreme Court of India was inaugurated on January 28, 1950, two days after India became a Republic.",
        "TNPSC பொறி: இந்தியா குடியரசான இரண்டு நாட்களுக்குப் பிறகு ஜனவரி 28, 1950 அன்று இந்திய உச்ச நீதிமன்றம் தொடக்கப்பட்டது.",
        "First Chief Justice of independent India's Supreme Court was Harilal J. Kania.",
        "சுதந்திர இந்தியாவின் உச்ச நீதிமன்றத்தின் முதல் தலைமை நீதிபதி ஹரிலால் ஜே. கானியா ஆவார்.",
        ["Polity", "Historical Background", "GOI Act 1935", "Federal Court", "Supreme Court Evolution", "Multi-Act Integration", "Grand Test"], "Analyze", 75
    ))

    # Q60: Statement Based - Hard - Indian Councils Act 1861 Portfolio & Legislative Features
    questions.append(make_q(
        60, "Hard", "Statement Based",
        "Consider the following statements regarding the Indian Councils Act of 1861:\n1. It empowered the Viceroy to make rules and orders for the more convenient transaction of business in the council.\n2. It gave statutory recognition to Lord Canning's Portfolio System introduced in 1859.\n3. It nominated three Indians to the Central Legislative Council in 1862: the Raja of Benaras, the Maharaja of Patiala, and Sir Dinkar Rao.\n4. It established new legislative councils for Bengal (1862), North-Western Frontier Province (1886), and Punjab (1897).\nWhich of the statements given above are correct?",
        "1861 ஆம் ஆண்டின் இந்தியக் கவுன்சில்கள் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது கவுன்சிலில் பணிகளை எளிதாக நடத்துவதற்காக விதிகள் மற்றும் உத்தரவுகளைப் பிறப்பிக்க வைஸ்ராய்க்கு அதிகாரமளித்தது.\n2. இது லார்டு கேனிங் 1859-ல் அறிமுகப்படுத்திய இலாகா முறைக்கு சட்டப்பூர்வ அங்கீகாரம் அளித்தது.\n3. இது 1862-ல் பெனாரஸ் ராஜா, பட்டியாலா மகாராஜா, சர் தினகர் ராவ் ஆகிய மூன்று இந்தியர்களை மத்திய சட்ட மேலவைக்கு நியமித்தது.\n4. இது வங்காளம் (1862), வடமேற்கு எல்லைப்புற மாகாணம் (1886), பஞ்சாப் (1897) ஆகிய மாகாணங்களுக்கு புதிய சட்ட மேலவைகளை நிறுவியது.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
        [
            ("A", "1, 2, 3 and 4", "1, 2, 3 மற்றும் 4"),
            ("B", "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டுமே"),
            ("C", "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டுமே"),
            ("D", "1 and 4 only", "1 மற்றும் 4 மட்டுமே")
        ],
        "A",
        "Historical Context: The 1861 Act laid down the institutional framework for legislative bodies in provinces across British India.\nReason: All four statements are correct. 1861 Act enabled business rules (Statement 1), legalized Portfolio system (Statement 2), saw Canning nominate 3 Indians in 1862 (Statement 3), and provided for establishing new legislative councils in Bengal (1862), NWFP (1886), and Punjab (1897) (Statement 4).\nConstitutional Impact: Created the prototype for state legislative councils in India.\nExam Trap: Bengal Council = 1862; NWFP Council = 1886; Punjab Council = 1897.\nMemory Trick: 1861 Act = Rules + Portfolio + 3 Nominated Indians + New Councils (Bengal/NWFP/Punjab).",
        "வரலாற்றுப் பின்னணி: 1861 சட்டம் பிரிட்டிஷ் இந்தியா முழுவதும் மாகாண சட்ட மன்றங்களுக்கான நிறுவனச் சட்டகத்தை அமைத்தது.\nகாரணம்: நான்கு கூற்றுகளும் சரியானவை. 1861 சட்டம் பணி விதிகளை அனுமதித்தது (கூற்று 1), இலாகா முறையை சட்டப்பூர்வமாக்கியது (கூற்று 2), 1862-ல் கேனிங் 3 இந்தியர்களை நியமித்தார் (கூற்று 3), புதிய மாகாண மேலவைகளை (வங்காளம் 1862, NWFP 1886, பஞ்சாப் 1897) உருவாக்கியது (கூற்று 4).\nஅரசியலமைப்பு தாக்கம்: இந்தியாவில் மாநில சட்ட மேலவைகளுக்கான முன்மாதிரியை உருவாக்கியது.\nதேர்வுப் பொறி: வங்காள மேலவை = 1862; NWFP மேலவை = 1886; பஞ்சாப் மேலவை = 1897.\nநினைவுச் சூத்திரம்: 1861 சட்டம் = விதிகள் + இலாகா + 3 நியமன இந்தியர்கள் + புதிய மேலவைகள் (வங்காளம்/NWFP/பஞ்சாப்).",
        {
            "A": {"en": "Correct. All four statements accurately state provisions of the Indian Councils Act 1861.", "ta": "சரி. 1861 இந்தியக் கவுன்சில்கள் சட்டத்தின் நான்கு கூற்றுகளும் துல்லியமாக சரியானவை."},
            "B": {"en": "Incorrect. Statement 4 is also correct.", "ta": "தவறு. கூற்று 4-ம் சரியானது."},
            "C": {"en": "Incorrect. Statement 1 is also correct.", "ta": "தவறு. கூற்று 1-ம் சரியானது."},
            "D": {"en": "Incorrect. Statements 2 and 3 are also correct.", "ta": "தவறு. கூற்றுகள் 2 மற்றும் 3-ம் சரியானவை."}
        },
        "TNPSC Trap: Lord Canning used the 1861 Act powers to issue the first statutory rules of executive business in India.",
        "TNPSC பொறி: லார்டு கேனிங் 1861 சட்ட அதிகாரங்களைப் பயன்படுத்தி இந்தியாவில் நிர்வாகப் பணிகளுக்கான முதல் சட்டப்பூர்வ விதிகளைப் பிறப்பித்தார்.",
        "Rules of business framed under 1861 Act are the historical predecessor to Article 77(3) of Indian Constitution.",
        "1861 சட்டத்தில் உருவான பணி விதிகள் இந்திய அரசியலமைப்பின் சரத்து 77(3)-க்கு வரலாற்று முன்னோடியாகும்.",
        ["Polity", "Historical Background", "Indian Councils Act 1861", "Portfolio System", "Grand Test"], "Analyze", 75
    ))

    # Q61: Direct MCQ - Easy - Indian Independence Act Partition Date
    questions.append(make_q(
        61, "Easy", "Direct MCQ",
        "The Indian Independence Act of 1947 fixed which exact date as the appointed day for the creation of two independent Dominions of India and Pakistan?",
        "1947 இந்திய சுதந்திரச் சட்டம் இந்தியா மற்றும் பாகிஸ்தான் என்ற இரு சுதந்திர டொமினியன்களை உருவாக்குவதற்கான குறிப்பிட்ட நியமன நாளாக எந்த தேதியை நிர்ணயித்தது?",
        [
            ("A", "August 15, 1947", "ஆகஸ்ட் 15, 1947"),
            ("B", "July 18, 1947", "ஜூலை 18, 1947"),
            ("C", "June 3, 1947", "ஜூன் 3, 1947"),
            ("D", "January 26, 1947", "ஜனவரி 26, 1947")
        ],
        "A",
        "Historical Context: Enactment of Mountbatten Plan into British statutory law.\nReason: Indian Independence Act 1947 was passed by British Parliament on July 18, 1947, and specified August 15, 1947, as the 'appointed day' when British rule ended and two independent Dominions came into existence.\nConstitutional Impact: Transfer of full sovereign power to India and Pakistan.\nExam Trap: Passed on July 18, 1947; Appointed Day = August 15, 1947.\nMemory Trick: Appointed Day = August 15, 1947.",
        "வரலாற்றுப் பின்னணி: மவுண்ட்பேட்டன் திட்டத்தை பிரிட்டிஷ் சட்டப்பூர்வ சட்டமாக இயற்றுதல்.\nகாரணம்: இந்திய சுதந்திரச் சட்டம் ஜூலை 18, 1947-ல் பிரிட்டிஷ் நாடாளுமன்றத்தால் நிறைவேற்றப்பட்டு, ஆகஸ்ட் 15, 1947-ஐ 'நியமன நாளாக' நிர்ணயித்து இரு சுதந்திர டொமினியன்களை உருவாக்கியது.\nஅரசியலமைப்பு தாக்கம்: இந்தியா மற்றும் பாகிஸ்தானுக்கு முழு இறையாண்மை அதிகாரம் மாற்றம்.\nதேர்வுப் பொறி: நிறைவேற்றப்பட்டது ஜூலை 18, 1947; நியமன நாள் = ஆகஸ்ட் 15, 1947.\nநினைவுச் சூத்திரம்: நியமன நாள் = ஆகஸ்ட் 15, 1947.",
        {
            "A": {"en": "Correct. August 15, 1947 was designated as the appointed day for two independent dominions.", "ta": "சரி. ஆகஸ்ட் 15, 1947 இரு சுதந்திர டொமினியன்களுக்கான நியமன நாளாகக் குறிக்கப்பட்டது."},
            "B": {"en": "Incorrect. July 18, 1947 was the date the Act received Royal Assent.", "ta": "தவறு. ஜூலை 18, 1947 அரசரின் ஒப்புதல் கிடைத்த நாளாகும்."},
            "C": {"en": "Incorrect. June 3, 1947 was Mountbatten Plan announcement date.", "ta": "தவறு. ஜூன் 3, 1947 மவுண்ட்பேட்டன் திட்ட அறிவிப்பு நாளாகும்."},
            "D": {"en": "Incorrect. January 26 was Declaration of Independence day (1930) and Republic day (1950).", "ta": "தவறு. ஜனவரி 26 சுதந்திரப் பிரகடன நாள் (1930) மற்றும் குடியரசு நாள் (1950)."}
        },
        "TNPSC Trap: Pakistan celebrates its independence on August 14 because Lord Mountbatten handed over power in Karachi on August 14, 1947.",
        "TNPSC பொறி: பாகிஸ்தான் ஆகஸ்ட் 14 அன்று சுதந்திர தினத்தைக் கொண்டாடுகிறது, ஏனெனில் லார்டு மவுண்ட்பேட்டன் ஆகஸ்ட் 14 அன்று கராச்சியில் அதிகாரத்தை ஒப்படைத்தார்.",
        "Indian Independence Act 1947 repealed Section 5 of Government of India Act 1935 regarding British paramountcy.",
        "1947 இந்திய சுதந்திரச் சட்டம் பிரிட்டிஷ் மேலாதிக்கம் தொடர்பான 1935 இந்திய அரசுச் சட்டத்தின் 5-வது பிரிவை ரத்து செய்தது.",
        ["Polity", "Historical Background", "Indian Independence Act 1947", "Appointed Day", "Grand Test"], "Remember", 45
    ))

    # Q62: Multi-Act Comparative - Hard - Evolution of Bicameral Central Legislature
    questions.append(make_q(
        62, "Hard", "Multi-Act Comparative",
        "Which sequence accurately details the structural composition changes of the Central Upper House from 1919 Act (Council of State) to 1935 Act (Council of State proposed)?",
        "1919 சட்டம் (மாநிலங்கள் குழு) முதல் 1935 சட்டம் (முன்மொழியப்பட்ட மாநிலங்கள் குழு) வரை மத்திய மேலவையின் அமைப்புக் மாற்றங்களை துல்லியமாக விளக்கும் வரிசை எது?",
        [
            ("A", "1919 Act: 60 members (34 elected, 26 nominated) with 5-year tenure -> 1935 Act: Proposed 260 members (156 British India elected, 104 Princely States nominated) as a permanent body with 1/3rd members retiring every 3 years", "1919 சட்டம்: 60 உறுப்பினர்கள் (34 தேர்வாகினர், 26 நியமனம்) 5 ஆண்டு ஆயுள் -> 1935 சட்டம்: முன்மொழியப்பட்ட 260 உறுப்பினர்கள் (156 பிரிட்டிஷ் இந்தியா, 104 சுதேச சமஸ்தானங்கள்) 3 ஆண்டுக்கு 1/3 பங்கு ஓய்வுபெறும் நிரந்தர அவை"),
            ("B", "1919 Act: 260 members permanent body -> 1935 Act: 60 members with 5-year tenure", "1919 சட்டம்: 260 உறுப்பினர்கள் கொண்ட நிரந்தர அவை -> 1935 சட்டம்: 60 உறுப்பினர்கள் 5 ஆண்டு ஆயுள்"),
            ("C", "1919 Act: Unicameral council -> 1935 Act: Bicameral assembly", "1919 சட்டம்: ஓரவை மன்றம் -> 1935 சட்டம்: இரு அவை பேரவை"),
            ("D", "1919 Act: 100% nominated body -> 1935 Act: 100% directly elected body", "1919 சட்டம்: 100% நியமன அவை -> 1935 சட்டம்: 100% நேரடித் தேர்தல் அவை")
        ],
        "A",
        "Historical Context: Transformation of the Central Upper House between Montagu-Chelmsford and 1935 Federal Scheme.\nReason: 1919 Council of State had 60 members (34 elected, 26 nominated) with a fixed 5-year term. 1935 Act proposed expanding Council of State to 260 members (156 British India + 104 Princely States) as a PERMANENT body not subject to dissolution, with 1/3rd members retiring every 3 years.\nConstitutional Impact: Direct model for modern Rajya Sabha (permanent body, 1/3rd retiring every 2 years under Article 83(1)).\nExam Trap: Modern Rajya Sabha 1/3rd retires every 2 years; 1935 proposed 1/3rd every 3 years.\nMemory Trick: 1919 Council of State (60 members, 5 yrs) $\rightarrow$ 1935 Council of State (260 members, Permanent, 1/3rd retire $\rightarrow$ basis for Rajya Sabha).",
        "வரலாற்றுப் பின்னணி: மாண்டேகு-செம்ஸ்ஃபோர்டு மற்றும் 1935 கூட்டாட்சித் திட்டத்திற்கு இடையே மத்திய மேலவையின் மாற்றம்.\nகாரணம்: 1919 மாநிலங்கள் குழு 60 உறுப்பினர்களைக் கொண்டிருந்தது (34 தேர்வாகினர், 26 நியமனம்) 5 ஆண்டு ஆயுளுடன். 1935 சட்டம் அதை 260 உறுப்பினர்களாக (156 பிரிட்டிஷ் இந்தியா + 104 சுதேச சமஸ்தானங்கள்) விரிவாக்கி, 3 ஆண்டுக்கு 1/3 பங்கு உறுப்பினர்கள் ஓய்வுபெறும் கலைக்கப்படாத நிரந்தர அவையாக மாற்ற முன்மொழிந்தது.\nஅரசியலமைப்பு தாக்கம்: நவீன மாநிலங்களவைக்கு (கலைக்கப்படாத நிரந்தர அவை, சரத்து 83(1)) நேரடி மாதிரியானது.\nதேர்வுப் பொறி: நவீன மாநிலங்களவை 2 ஆண்டுக்கு 1/3 ஓய்வு; 1935 சட்டம் 3 ஆண்டுக்கு 1/3 ஓய்வு என முன்மொழிந்தது.\nநினைவுச் சூத்திரம்: 1919 மேலவை (60 உறுப்பினர்கள், 5 ஆண்டு) $\rightarrow$ 1935 மேலவை (260 உறுப்பினர்கள், நிரந்தர அவை $\rightarrow$ மாநிலங்களவை அடிப்படை).",
        {
            "A": {"en": "Correct. Perfectly maps composition and tenure shift of Central Upper House between 1919 and 1935.", "ta": "சரி. 1919 மற்றும் 1935 சட்டங்களில் மத்திய மேலவையின் கட்டமைப்பு மற்றும் ஆயுட்கால மாற்றத்தின் சரியான வரிசை."},
            "B": {"en": "Incorrect. Reverses 1919 and 1935 numbers.", "ta": "தவறு. 1919 மற்றும் 1935 எண்களை தலைகீழாக மாற்றுகிறது."},
            "C": {"en": "Incorrect. 1919 was already bicameral.", "ta": "தவறு. 1919-லேயே இரு அவை முறை உருவானது."},
            "D": {"en": "Incorrect. 1919 Council of State had 34 elected members.", "ta": "தவறு. 1919 மேலவையில் 34 தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்கள் இருந்தனர்."}
        },
        "TNPSC Trap: Council of State under 1919 Act had a women restriction—women were NOT eligible to be elected or nominated to the Council of State initially.",
        "TNPSC பொறி: 1919 சட்டத்தின் கீழ் மாநிலங்கள் குழுவில் பெண்களுக்குத் தடை இருந்தது—தொடக்கத்தில் பெண்கள் மாநிலங்கள் குழுவிற்கு தேர்ந்தெடுக்கப்படவோ நியமிக்கப்படவோ தகுதியற்றவர்களாக இருந்தனர்.",
        "First President of Central Legislative Assembly (Lower House) was Sir Frederick Whyte (1921); first Indian President was Vithalbhai J. Patel (1925).",
        "மத்திய சட்ட பேரவையின் முதல் தலைவர் சர் ஃப்ரிட்ரிக் ஒய்ட் (1921); முதல் இந்தியத் தலைவர் விதேல்பாய் ஜே. படேல் (1925).",
        ["Polity", "Historical Background", "GOI Act 1919", "GOI Act 1935", "Council of State", "Rajya Sabha Prototype", "Grand Test"], "Analyze", 75
    ))

    # Q63: Statement Based - Medium - Macaulay Committee 1854 Civil Services
    questions.append(make_q(
        63, "Medium", "Statement Based",
        "Consider the following statements regarding the Committee on Indian Civil Service (Macaulay Committee) of 1854:\n1. It was appointed in 1854 following the provisions of the Charter Act of 1853.\n2. It recommended that recruitment to the Covenanted Civil Service should be made through open competitive examinations based on merit.\n3. It recommended that Haileybury College in England be expanded to accommodate all Indian candidates permanently.\nWhich of the statements given above is/are correct?",
        "1854 ஆம் ஆண்டின் இந்திய சிவில் சர்வீஸ் குழு (மெக்காலே குழு) பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது 1853 சாசனச் சட்டத்தின் விதிகளைத் தொடர்ந்து 1854-ல் நியமிக்கப்பட்டது.\n2. இது உடன்படிக்கை சிவில் சர்வீஸ் (Covenanted Civil Service) நியமனங்களை தகுதி அடிப்படையில் திறந்த போட்டித் தேர்வுகள் மூலம் செய்ய பரிந்துரைத்தது.\n3. இங்கிலாந்தில் உள்ள ஹெய்லிபரி கல்லூரியை அனைத்து இந்திய விண்ணப்பதாரர்களுக்கும் நிரந்தரமாக விரிவாக்கம் செய்ய பரிந்துரைத்தது.\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானவை?",
        [
            ("A", "1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
            ("B", "2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
            ("C", "1 and 3 only", "1 மற்றும் 3 மட்டுமே"),
            ("D", "1, 2 and 3", "1, 2 மற்றும் 3")
        ],
        "A",
        "Historical Context: Transition of Civil Service recruitment from patronage to open competition.\nReason: Statements 1 and 2 are correct. Statement 3 is incorrect because Haileybury College (where Company nominees were trained) was actually CLOSED DOWN in 1858 following the open competition reforms.\nConstitutional Impact: Established open competitive examination system for Indian Civil Services.\nExam Trap: Open competition established in 1853 Act; Macaulay Committee appointed in 1854; first open examination held in London in 1855; Haileybury closed in 1858.\nMemory Trick: 1854 Macaulay Committee = Open Civil Service Exam + Closed Haileybury College.",
        "வரலாற்றுப் பின்னணி: சிவில் சர்வீஸ் நியமனம் ஆதரவு முறையிலிருந்து திறந்த போட்டிக்கு மாறுதல்.\nகாரணம்: கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் ஹெய்லிபரி கல்லூரி (கம்பெனி நியமன உறுப்பினர்கள் பயிற்சி பெற்ற இடம்) போட்டித் தேர்வு சீர்திருத்தங்களைத் தொடர்ந்து 1858-ல் மூடப்பட்டது.\nஅரசியலமைப்பு தாக்கம்: இந்திய சிவில் சர்வீஸுக்கான திறந்த போட்டித் தேர்வு முறையை நிறுவியது.\nதேர்வுப் பொறி: 1853 சட்டத்தில் போட்டித் தேர்வு உறுதி; 1854-ல் மெக்காலே குழு நியமனம்; 1855-ல் லண்டனில் முதல் போட்டித் தேர்வு; 1858-ல் ஹெய்லிபரி மூடல்.\nநினைவுச் சூத்திரம்: 1854 மெக்காலே குழு = திறந்த சிவில் சர்வீஸ் தேர்வு + ஹெய்லிபரி கல்லூரி மூடல்.",
        {
            "A": {"en": "Correct. Statements 1 and 2 are true; Statement 3 is false as Haileybury College was closed in 1858.", "ta": "சரி. கூற்றுகள் 1 மற்றும் 2 சரி; ஹெய்லிபரி கல்லூரி 1858-ல் மூடப்பட்டதால் கூற்று 3 தவறு."},
            "B": {"en": "Incorrect. Statement 3 is false.", "ta": "தவறு. கூற்று 3 தவறானது."},
            "C": {"en": "Incorrect. Statement 3 is false.", "ta": "தவறு. கூற்று 3 தவறானது."},
            "D": {"en": "Incorrect. Statement 3 is false.", "ta": "தவறு. கூற்று 3 தவறானது."}
        },
        "TNPSC Trap: Satyendranath Tagore (brother of Rabindranath Tagore) was the first Indian to qualify for the Indian Civil Service (ICS) in 1863.",
        "TNPSC பொறி: சத்யேந்திரநாத் தாகூர் (ரவீந்திரநாத் தாகூரின் சகோதரர்) 1863-ல் இந்திய சிவில் சர்வீஸ் (ICS) தேர்வில் தேர்ச்சியடைந்த முதல் இந்தியராவார்.",
        "Age limit for ICS exam was progressively reduced from 23 to 19 by Lord Lytton in 1878 to discourage Indians.",
        "இந்தியர்கள் சேருவதைத் தடுக்க 1878-ல் லார்டு லிட்டனால் ICS தேர்வு வயது வரம்பு 23-லிருந்து 19 ஆகக் குறைக்கப்பட்டது.",
        ["Polity", "Historical Background", "Macaulay Committee 1854", "Civil Services", "Grand Test"], "Analyze", 75
    ))

    # Q64: Conceptual MCQ - Medium - Indian Councils Act 1909 Non-Official Majority
    questions.append(make_q(
        64, "Medium", "Conceptual MCQ",
        "Regarding legislative majority composition, what specific rule was established by the Indian Councils Act of 1909?",
        "சட்டமன்ற பெரும்பான்மை கட்டமைப்பு தொடர்பாக 1909 இந்தியக் கவுன்சில்கள் சட்டத்தால் நிறுவப்பட்ட குறிப்பிட்ட விதி யாது?",
        [
            ("A", "It allowed a non-official majority in Provincial Legislative Councils, while retaining an official majority in the Central Legislative Council.", "இது மாகாண சட்ட மேலவைகளில் அதிகாரப்பூர்வமற்ற பெரும்பான்மையை அனுமதித்தது, ஆனால் மத்திய சட்ட மேலவையில் அதிகாரப்பூர்வ பெரும்பான்மையை நீடித்தது."),
            ("B", "It introduced an official majority in both Central and Provincial Legislative Councils.", "இது மத்திய மற்றும் மாகாண இரண்டு சட்ட மேலவைகளிலும் அதிகாரப்பூர்வ பெரும்பான்மையை அறிமுகப்படுத்தியது."),
            ("C", "It mandated an elected Indian majority in both Central and Provincial Legislative Councils.", "இது மத்திய மற்றும் மாகாண இரண்டு மேலவைகளிலும் தேர்ந்தெடுக்கப்பட்ட இந்திய பெரும்பான்மையைக் கட்டாயமாக்கியது."),
            ("D", "It abolished all official members and filled all seats through direct elections.", "இது அனைத்து அதிகாரப்பூர்வ உறுப்பினர்களையும் ஒழித்து அனைத்து இடங்களையும் நேரடித் தேர்தல் மூலம் நிரப்பியது.")
        ],
        "A",
        "Historical Context: Asymmetric legislative representation between central and regional levels under 1909 Morley-Minto reforms.\nReason: 1909 Act expanded central council from 16 to 60 additional members and retained an OFFICIAL majority. In provincial councils, it allowed a NON-OFFICIAL majority (though nominated non-officials plus elected non-officials made up the majority, not purely elected members).\nConstitutional Impact: Step towards provincial legislative self-governance.\nExam Trap: Non-official majority in provinces (1909); Non-official majority at Center (1919).\nMemory Trick: 1909 = Official Majority at Center + Non-Official Majority in Provinces.",
        "வரலாற்றுப் பின்னணி: 1909 மோலி-மிண்டோ சீர்திருத்தங்களின் கீழ் மத்திய மற்றும் மாகாண மட்டங்களில் சீரற்ற பிரதிநிதித்துவம்.\nகாரணம்: 1909 சட்டம் மத்திய மேலவை கூடுதல் உறுப்பினர்களை 16-லிருந்து 60 ஆக உயர்த்தி அதிகாரப்பூர்வ பெரும்பான்மையை நீடித்தது. மாகாண மேலவைகளில் அதிகாரப்பூர்வமற்ற பெரும்பான்மையை அனுமதித்தது (நியமன அதிகாரப்பூர்வமற்றோர் + தேர்ந்தெடுக்கப்பட்டோர் சேர்ந்த பெரும்பான்மை).\nஅரசியலமைப்பு தாக்கம்: மாகாண சட்டமன்ற சுயராஜ்யத்தை நோக்கிய படி.\nதேர்வுப் பொறி: மாகாணங்களில் அதிகாரப்பூர்வமற்ற பெரும்பான்மை (1909); மத்தியில் அதிகாரப்பூர்வமற்ற பெரும்பான்மை (1919).\nநினைவுச் சூத்திரம்: 1909 = மத்தியில் அதிகாரப்பூர்வ பெரும்பான்மை + மாகாணங்களில் அதிகாரப்பூர்வமற்ற பெரும்பான்மை.",
        {
            "A": {"en": "Correct. 1909 Act allowed non-official majority in provinces, retained official majority at Center.", "ta": "சரி. 1909 சட்டம் மாகாணங்களில் அதிகாரப்பூர்வமற்ற பெரும்பான்மையை அனுமதித்து மத்தியில் அதிகாரப்பூர்வ பெரும்பான்மையை நீடித்தது."},
            "B": {"en": "Incorrect. Official majority was retained only at the Center.", "ta": "தவறு. அதிகாரப்பூர்வ பெரும்பான்மை மத்தியில் மட்டுமே நீடித்தது."},
            "C": {"en": "Incorrect. Elected members did not form absolute majority in 1909.", "ta": "தவறு. 1909-ல் தேர்ந்தெடுக்கப்பட்டோர் தனிப் பெரும்பான்மை பெறவில்லை."},
            "D": {"en": "Incorrect. Official members were not abolished in 1909.", "ta": "தவறு. அதிகாரப்பூர்வ உறுப்பினர்கள் ஒழிக்கப்படவில்லை."}
        },
        "TNPSC Trap: Non-official majority in 1909 provincial councils did NOT mean an elected majority, because nominated non-officials were included.",
        "TNPSC பொறி: 1909 மாகாண மேலவைகளில் அதிகாரப்பூர்வமற்ற பெரும்பான்மை என்பது தேர்ந்தெடுக்கப்பட்டோர் பெரும்பான்மை அல்ல, ஏனெனில் நியமன அதிகாரப்பூர்வமற்றோரும் அதில் அடங்குவர்.",
        "Central Legislative Council membership was increased from 16 to 60 under 1909 Act.",
        "1909 சட்டத்தின் கீழ் மத்திய சட்ட மேலவை உறுப்பினர்கள் எண்ணிக்கை 16-லிருந்து 60 ஆக உயர்த்தப்பட்டது.",
        ["Polity", "Historical Background", "Indian Councils Act 1909", "Non-Official Majority", "Grand Test"], "Understand", 60
    ))

    # Q65: Multi-Act Comparative - Hard - Indian Independence Act & Constituent Assembly Sovereignty
    questions.append(make_q(
        65, "Hard", "Multi-Act Comparative",
        "Which distinction accurately separates the status of the Constituent Assembly under the Cabinet Mission Plan (1946) from its status under the Indian Independence Act (1947)?",
        "1946 கேபினட் தூதுக்குழு திட்டத்தின் கீழ் இருந்த அரசியல் நிர்ணய சபையின் அந்தஸ்தை 1947 இந்திய சுதந்திரச் சட்டத்தின் கீழ் அதன் அந்தஸ்திலிருந்து துல்லியமாக வேறுபடுத்தும் கூற்று எது?",
        [
            ("A", "Under 1946 Cabinet Mission Plan the Constituent Assembly was a non-sovereign body subject to British Parliamentary oversight, whereas under 1947 Indian Independence Act it became a fully sovereign body capable of altering or repealing any British statute", "1946 கேபினட் திட்டத்தில் அரசியல் நிர்ணய சபை பிரிட்டிஷ் நாடாளுமன்றக் கட்டுப்பாட்டிற்குட்பட்ட இறையாண்மையற்ற அமைப்பாக இருந்தது; ஆனால் 1947 இந்திய சுதந்திரச் சட்டத்தில் அது எந்தவொரு பிரிட்டிஷ் சட்டத்தையும் மாற்றவோ ரத்து செய்யவோ தகுதியுள்ள முழு இறையாண்மை கொண்ட அமைப்பானது"),
            ("B", "Under 1946 Plan it was fully sovereign, whereas under 1947 Act it became subordinate to the British King", "1946 திட்டத்தில் அது முழு இறையாண்மை கொண்டது; ஆனால் 1947 சட்டத்தில் அது பிரிட்டிஷ் மன்னருக்குக் கீழ்மைப்பட்டது"),
            ("C", "Under 1946 Plan it was a judicial tribunal, whereas under 1947 Act it became a military council", "1946 திட்டத்தில் அது நீதி தீர்ப்பாயம்; 1947 சட்டத்தில் இராணுவக் குழுவானது"),
            ("D", "There was no legal change in the status of Constituent Assembly between 1946 and 1947", "1946 மற்றும் 1947 இடையே அரசியல் நிர்ணய சபையின் அந்தஸ்தில் எந்த சட்ட மாற்றமும் இல்லை")
        ],
        "A",
        "Historical Context: Shift from colonial constituent body to supreme sovereign constituent assembly.\nReason: Constituent Assembly set up in Nov 1946 under Cabinet Mission Plan was initially not a fully sovereign body (its parameters and limitations were set by British Government). Section 6 of Indian Independence Act 1947 conferred full constituent sovereignty on the Assembly, empowering it to frame any constitution, abrogate British suzerainty, and repeal any British Parliamentary Act (including 1947 Act itself).\nConstitutional Impact: Made the Constituent Assembly the supreme sovereign law-making body of independent India.\nExam Trap: Constituent Assembly set up in 1946 under Cabinet Mission Plan; became fully sovereign in 1947 Act.\nMemory Trick: 1946 = Non-Sovereign Assembly; 1947 Act = Fully Sovereign Assembly.",
        "வரலாற்றுப் பின்னணி: காலனித்துவ அரசியலமைப்பு அமைப்பிலிருந்து உச்ச இறையாண்மை கொண்ட அரசியல் நிர்ணய சபையாக மாறுதல்.\nகாரணம்: கேபினட் தூதுக்குழு திட்டத்தின் கீழ் 1946 நவம்பரில் அமைக்கப்பட்ட அரசியல் நிர்ணய சபை தொடக்கத்தில் முழு இறையாண்மை கொண்ட அமைப்பல்ல (அதன் வரம்புகள் பிரிட்டிஷ் அரசால் நிர்ணயிக்கப்பட்டன). 1947 இந்திய சுதந்திரச் சட்டத்தின் பிரிவு 6 சபைக்கு முழு அரசியலமைப்பு இறையாண்மையை அளித்து, எந்தவொரு அரசியலமைப்பையும் உருவாக்கவும், பிரிட்டிஷ் மேலாதிக்கத்தை ஒழிக்கவும், சுதந்திரச் சட்டம் உட்பட எந்த பிரிட்டிஷ் சட்டத்தையும் ரத்து செய்யவும் அதிகாரம் வழங்கியது.\nஅரசியலமைப்பு தாக்கம்: அரசியல் நிர்ணய சபையை சுதந்திர இந்தியாவின் உச்ச இறையாண்மை சட்ட அமைப்பாக மாற்றியது.\nதேர்வுப் பொறி: 1946-ல் அமைந்தது கேபினட் திட்டம்; முழு இறையாண்மை பெற்றது 1947 சட்டம்.\nநினைவுச் சூத்திரம்: 1946 = இறையாண்மையற்ற சபை; 1947 சட்டம் = முழு இறையாண்மை கொண்ட சபை.",
        {
            "A": {"en": "Correct. 1947 Act conferred full constituent sovereignty on the Constituent Assembly.", "ta": "சரி. 1947 சட்டம் அரசியல் நிர்ணய சபைக்கு முழு அரசியலமைப்பு இறையாண்மையை வழங்கியது."},
            "B": {"en": "Incorrect. Reverses the sovereign evolution.", "ta": "தவறு. இறையாண்மை வளர்ச்சியை தலைகீழாக மாற்றுகிறது."},
            "C": {"en": "Incorrect. Constituent Assembly was never a judicial or military body.", "ta": "தவறு. அரசியல் நிர்ணய சபை நீதி அல்லது இராணுவ அமைப்பல்ல."},
            "D": {"en": "Incorrect. Legal status shifted dramatically from non-sovereign to sovereign.", "ta": "தவறு. சட்டப்பூர்வ அந்தஸ்து இறையாண்மையற்ற நிலையிலிருந்து இறையாண்மை நிலைக்கு மாறியது."}
        },
        "TNPSC Trap: Constituent Assembly of India also functioned as the Dominion Legislature (provisional parliament) chaired by G.V. Mavalankar when meeting for legislative work.",
        "TNPSC பொறி: இந்திய அரசியல் நிர்ணய சபை சட்டப் பணிகளுக்காகக் கூடியபோது ஜி.வி. மாவிலங்கர் தலைமையில் டொமினியன் சட்டமன்றமாக (தற்காலிக நாடாளுமன்றம்) செயல்பட்டது.",
        "When Constituent Assembly met as a constituent body, it was chaired by Dr. Rajendra Prasad.",
        "அரசியலமைப்பு நிர்ணய அமைப்பாகக் கூடியபோது டாக்டர் ராஜேந்திர பிரசாத் தலைமை தாங்கினார்.",
        ["Polity", "Historical Background", "Constituent Assembly", "Indian Independence Act 1947", "Sovereignty", "Multi-Act Integration", "Grand Test"], "Analyze", 75
    ))

    # Q66: Direct MCQ - Easy - Regulating Act First Governor-General Name Trap
    questions.append(make_q(
        66, "Easy", "Direct MCQ",
        "Who among the following was appointed as the FIRST Governor-General of Bengal under the Regulating Act of 1773?",
        "1773 ஆம் ஆண்டின் ஒழுங்குமுறைச் சட்டத்தின் கீழ் வங்காளத்தின் முதல் கவர்னர்-ஜெனரலாக நியமிக்கப்பட்டவர் யார்?",
        [
            ("A", "Warren Hastings", "வாரன் ஹேஸ்டிங்ஸ்"),
            ("B", "Lord Cornwallis", "லார்டு காரன்வாலிஸ்"),
            ("C", "Lord William Bentinck", "லார்டு வில்லியம் பென்டிங்க்"),
            ("D", "Lord Clive", "லார்டு கிளைவ்")
        ],
        "A",
        "Historical Context: Regulating Act 1773 elevated Governor of Bengal to Governor-General of Bengal.\nReason: Warren Hastings, who was serving as Governor of Bengal, became the first Governor-General of Bengal under the 1773 Act.\nConstitutional Impact: Created the first unified executive head in British India.\nExam Trap: Warren Hastings = 1st GG of Bengal (1773); William Bentinck = 1st GG of India (1833); Lord Canning = 1st Viceroy (1858).\nMemory Trick: 1773 Hastings (Bengal) $\rightarrow$ 1833 Bentinck (India) $\rightarrow$ 1858 Canning (Viceroy).",
        "வரலாற்றுப் பின்னணி: 1773 ஒழுங்குமுறைச் சட்டம் வங்காள ஆளுநரை வங்காள கவர்னர்-ஜெனரலாக உயர்த்தியது.\nகாரணம்: வங்காள ஆளுநராக இருந்த வாரன் ஹேஸ்டிங்ஸ் 1773 சட்டத்தின் கீழ் வங்காளத்தின் முதல் கவர்னர்-ஜெனரலானார்.\nஅரசியலமைப்பு தாக்கம்: பிரிட்டிஷ் இந்தியாவில் முதல் ஒருங்கிணைந்த நிர்வாகத் தலைவரை உருவாக்கியது.\nதேர்வுப் பொறி: வாரன் ஹேஸ்டிங்ஸ் = 1வது வங்காள GG (1773); வில்லியம் பென்டிங்க் = 1வது இந்திய GG (1833); லார்டு கேனிங் = 1வது வைஸ்ராய் (1858).\nநினைவுச் சூத்திரம்: 1773 ஹேஸ்டிங்ஸ் (வங்காளம்) $\rightarrow$ 1833 பென்டிங்க் (இந்தியா) $\rightarrow$ 1858 கேனிங் (வைஸ்ராய்).",
        {
            "A": {"en": "Correct. Warren Hastings was the first Governor-General of Bengal (1773).", "ta": "சரி. வாரன் ஹேஸ்டிங்ஸ் முதல் வங்காள கவர்னர்-ஜெனரல் (1773)."},
            "B": {"en": "Incorrect. Lord Cornwallis became GG in 1786.", "ta": "தவறு. லார்டு காரன்வாலிஸ் 1786-ல் GG ஆனார்."},
            "C": {"en": "Incorrect. Lord William Bentinck was the first Governor-General of India (1833).", "ta": "தவறு. வில்லியம் பென்டிங்க் முதல் இந்திய கவர்னர்-ஜெனரல் (1833)."},
            "D": {"en": "Incorrect. Robert Clive was Governor of Bengal (1757-60, 1765-67), before 1773 Act.", "ta": "தவறு. ராபர்ட் கிளைவ் 1773-க்கு முன் வங்காள ஆளுநராக இருந்தார்."}
        },
        "TNPSC Trap: Warren Hastings was impeached in British Parliament upon his return to England in 1785 (acquitted in 1795).",
        "TNPSC பொறி: வாரன் ஹேஸ்டிங்ஸ் 1785-ல் இங்கிலாந்து திரும்பியதும் பிரிட்டிஷ் நாடாளுமன்றத்தில் பதவி நீக்க விசாரணைக்கு உட்படுத்தப்பட்டார் (1795-ல் விடுதலை பெறப்பட்டார்).",
        "Regulating Act 1773 created an Executive Council of 4 members to assist Warren Hastings.",
        "1773 ஒழுங்குமுறைச் சட்டம் வாரன் ஹேஸ்டிங்ஸுக்கு உதவ 4 உறுப்பினர்களைக் கொண்ட நிர்வாகக் குழுவை உருவாக்கியது.",
        ["Polity", "Historical Background", "Regulating Act 1773", "Warren Hastings", "Grand Test"], "Remember", 45
    ))

    # Q67: Statement Based - Hard - Charter Act 1853 Parliamentary Mini-Assembly Model
    questions.append(make_q(
        67, "Hard", "Statement Based",
        "Consider the following statements regarding the Central Legislative Council created under the Charter Act of 1853:\n1. It functioned as a mini-parliament, adopting the same procedure as the British Parliament.\n2. For the first time, legislation was treated as a special function of the government requiring special machinery and special process.\n3. Four out of six new legislative members were appointed by the local (provincial) governments of Madras, Bombay, Bengal, and Agra.\nWhich of the statements given above are correct?",
        "1853 சாசனச் சட்டத்தின் கீழ் உருவாக்கப்பட்ட மத்திய சட்ட மேலவை பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது பிரிட்டிஷ் நாடாளுமன்றத்தின் அதே நடைமுறைகளைப் பின்பற்றி ஒரு சிறிய நாடாளுமன்றமாகச் செயல்பட்டது.\n2. முதன்முறையாக, சட்டம் இயற்றுவது சிறப்பு இயந்திரங்கள் மற்றும் சிறப்பு நடைமுறைகள் தேவைப்படும் அரசின் சிறப்புப் பணியாகக் கருதப்பட்டது.\n3. ஆறு புதிய சட்ட உறுப்பினர்களில் நான்கு பேர் மதராஸ், பம்பாய், வங்காளம், ஆக்ரா உள்ளூர் (மாகாண) அரசுகளால் நியமிக்கப்பட்டனர்.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
        [
            ("A", "1, 2 and 3", "1, 2 மற்றும் 3"),
            ("B", "1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
            ("C", "2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
            ("D", "1 and 3 only", "1 மற்றும் 3 மட்டுமே")
        ],
        "A",
        "Historical Context: Emergence of a distinct legislative organ within the British Indian administration in 1853.\nReason: All three statements are correct. 1853 Act created a 12-member Central Legislative Council functioning as a mini-parliament (Statement 1), treated legislation as a distinct function (Statement 2), and introduced local representation with 4 members from Madras, Bombay, Bengal, and Agra (Statement 3).\nConstitutional Impact: Genesis of modern parliamentary legislative procedure in India.\nExam Trap: Local representation in central council started in 1853 (official members), not 1861.\nMemory Trick: 1853 Act = Mini-Parliament + Distinct Legislative Process + Local Representation (Madras, Bombay, Bengal, Agra).",
        "வரலாற்றுப் பின்னணி: 1853-ல் பிரிட்டிஷ் இந்திய நிர்வாகத்தில் ஒரு தனித்துவமான சட்ட அமைப்பின் எழுச்சி.\nகாரணம்: மூன்று கூற்றுகளும் சரியானவை. 1853 சட்டம் சிறிய நாடாளுமன்றமாகச் செயல்படும் 12 உறுப்பினர் மத்திய சட்ட மேலவையை உருவாக்கியது (கூற்று 1), சட்டம் இயற்றுதலைத் தனிப் பணியாகக் கருதியது (கூற்று 2), மதராஸ், பம்பாய், வங்காளம், ஆக்ராவிலிருந்து 4 உறுப்பினர்களுடன் உள்ளூர் பிரதிநிதித்துவத்தை அறிமுகப்படுத்தியது (கூற்று 3).\nஅரசியலமைப்பு தாக்கம்: இந்தியாவில் நவீன நாடாளுமன்றச் சட்ட நடைமுறையின் தொடக்கம்.\nதேர்வுப் பொறி: மத்திய மேலவையில் உள்ளூர் பிரதிநிதித்துவம் 1853-ல் தொடங்கியது (அதிகாரப்பூர்வ உறுப்பினர்கள்), 1861-ல் அல்ல.\nநினைவுச் சூத்திரம்: 1853 சட்டம் = சிறிய நாடாளுமன்றம் + தனி சட்ட நடைமுறை + உள்ளூர் பிரதிநிதித்துவம் (மதராஸ், பம்பாய், வங்காளம், ஆக்ரா).",
        {
            "A": {"en": "Correct. All three statements accurately describe the 1853 Central Legislative Council.", "ta": "சரி. 1853 மத்திய சட்ட மேலவை பற்றிய மூன்று கூற்றுகளும் துல்லியமாக சரியானவை."},
            "B": {"en": "Incorrect. Statement 3 is also correct.", "ta": "தவறு. கூற்று 3-ம் சரியானது."},
            "C": {"en": "Incorrect. Statement 1 is also correct.", "ta": "தவறு. கூற்று 1-ம் சரியானது."},
            "D": {"en": "Incorrect. Statement 2 is also correct.", "ta": "தவறு. கூற்று 2-ம் சரியானது."}
        },
        "TNPSC Trap: Chief Justice of Supreme Court at Calcutta and one puisne judge were also made ex-officio members of 1853 Legislative Council.",
        "TNPSC பொறி: கொல்கத்தா உச்ச நீதிமன்ற தலைமை நீதிபதியும் ஒரு நீதிபதியும் 1853 சட்ட மேலவையின் இணை உறுப்பினர்களாக இருந்தனர்.",
        "1853 Charter Act did not specify any time period for renewal, signaling that Company rule could be terminated by Crown anytime.",
        "1853 சாசனச் சட்டம் புதுப்பித்தலுக்கான எந்தவொரு கால வரம்பையும் குறிப்பிடவில்லை, இது கம்பெனி ஆட்சி எப்போது வேண்டுமானாலும் ஒழிக்கப்படலாம் என்பதைக் காட்டியது.",
        ["Polity", "Historical Background", "Charter Act 1853", "Mini Parliament", "Grand Test"], "Analyze", 75
    ))

    # Q68: Conceptual MCQ - Medium - Government of India Act 1935 Provincial Franchise & Women Representation
    questions.append(make_q(
        68, "Medium", "Conceptual MCQ",
        "Which progressive electoral provision regarding women representation was introduced by the Government of India Act of 1935?",
        "1935 ஆம் ஆண்டின் இந்திய அரசுச் சட்டத்தால் பெண்கள் பிரதிநிதித்துவம் தொடர்பாக அறிமுகப்படுத்தப்பட்ட முற்போக்கான தேர்தல் விதி எது?",
        [
            ("A", "Extension of separate electorates for women and reservation of seats for women in central and provincial legislatures", "பெண்களுக்குத் தனித் தொகுதிகளை விரிவுபடுத்துதல் மற்றும் மத்திய, மாகாண சட்டமன்றங்களில் பெண்களுக்கு இடஒதுக்கீடு அளித்தல்"),
            ("B", "Granting of 50% mandatory reservation for women in all cabinet ministries", "அனைத்து கேபினட் அமைச்சகங்களிலும் பெண்களுக்கு 50% கட்டாய இடஒதுக்கீடு வழங்குதல்"),
            ("C", "Granting of universal adult franchise exclusively to literate women", "எழுதப் படிக்கத் தெரிந்த பெண்களுக்கு மட்டும் உலகளாவிய வயதுவந்தோர் வாக்குரிமை வழங்குதல்"),
            ("D", "Appointment of women as Provincial Governors in all 11 provinces", "அனைத்து 11 மாகாணங்களிலும் பெண்களை மாகாண கவர்னர்களாக நியமித்தல்")
        ],
        "A",
        "Historical Context: Progressive expansion of targeted representation for marginalized sections under 1935 Act.\nReason: 1935 Act extended the principle of communal representation by providing separate electorates for Depressed Classes (Scheduled Castes), Women, and Labour (workers). Seats were reserved for women in both federal assembly and provincial assemblies.\nConstitutional Impact: Foundation for women reservation and affirmative action in Indian democracy.\nExam Trap: Separate electorates for Muslims = 1909; Sikhs/Christians/Anglo-Indians/Europeans = 1919; Women/Depressed Classes/Labour = 1935.\nMemory Trick: 1935 Electorate Expansion = Depressed Classes + Women + Labour.",
        "வரலாற்றுப் பின்னணி: 1935 சட்டத்தின் கீழ் விளிம்புநிலை பிரிவினருக்கான இலக்கு பிரதிநிதித்துவத்தின் படிமுறை விரிவாக்கம்.\nகாரணம்: 1935 சட்டம் ஒடுக்கப்பட்ட வகுப்பினர் (பட்டியல் சாதிகள்), பெண்கள் மற்றும் தொழிலாளர்களுக்குத் தனித் தொகுதிகளை வழங்கி வகுப்புவாத பிரதிநிதித்துவத்தை விரிவுபடுத்தியது. கூட்டாட்சிப் பேரவை மற்றும் மாகாணப் பேரவைகளில் பெண்களுக்கு இடங்கள் ஒதுக்கப்பட்டன.\nஅரசியலமைப்பு தாக்கம்: இந்திய ஜனநாயகத்தில் பெண் இடஒதுக்கீடு மற்றும் நேர்மறை நடவடிக்கைக்கான அடித்தளம்.\nதேர்வுப் பொறி: முஸ்லிம்கள் தனித் தொகுதி = 1909; சீக்கியர்/கிறிஸ்தவர்/ஆங்கிலோ-இந்தியர் = 1919; பெண்கள்/ஒடுக்கப்பட்டோர்/தொழிலாளர் = 1935.\nநினைவுச் சூத்திரம்: 1935 தொகுதி விரிவாக்கம் = ஒடுக்கப்பட்டோர் + பெண்கள் + தொழிலாளர்.",
        {
            "A": {"en": "Correct. 1935 Act extended separate electorates and seat reservation for women.", "ta": "சரி. 1935 சட்டம் பெண்களுக்குத் தனித் தொகுதிகளையும் இடஒதுக்கீட்டையும் விரிவுபடுத்தியது."},
            "B": {"en": "Incorrect. No 50% cabinet reservation existed.", "ta": "தவறு. 50% கேபினட் இடஒதுக்கீடு இருக்கவில்லை."},
            "C": {"en": "Incorrect. Franchise was restricted, not universal adult franchise.", "ta": "தவறு. உலகளாவிய வயதுவந்தோர் வாக்குரிமை வழங்கப்படவில்லை."},
            "D": {"en": "Incorrect. Women were not appointed as Governors under 1935 Act.", "ta": "தவறு. பெண்கள் கவர்னர்களாக நியமிக்கப்படவில்லை."}
        },
        "TNPSC Trap: Sarojini Naidu became the first female Governor of an Indian state (United Provinces) in 1947.",
        "TNPSC பொறி: சரோஜினி நாயுடு 1947-ல் இந்திய மாநிலத்தின் (ஐக்கிய மாகாணங்கள்) முதல் பெண் கவர்னரானார்.",
        "1935 Act provided 6 seats reserved for women in the Council of State and 9 seats in the Federal Assembly.",
        "1935 சட்டம் மாநிலங்கள் குழுவில் 6 இடங்களையும் கூட்டாட்சி பேரவையில் 9 இடங்களையும் பெண்களுக்கு ஒதுக்கியது.",
        ["Polity", "Historical Background", "GOI Act 1935", "Women Reservation", "Grand Test"], "Understand", 60
    ))

    # Q69: Multi-Act Comparative - Hard - Evolution of Financial Control & Audit
    questions.append(make_q(
        69, "Hard", "Multi-Act Comparative",
        "Which statutory milestone established the independent position of Auditor-General of India and statutory separation of audit from accounts?",
        "இந்திய தணிக்கை அதிகாரி (Auditor-General of India) பதவியின் சுதந்திரமான நிலையையும், தணிக்கையை கணக்கு நிர்வாகத்திலிருந்து பிரிப்பதையும் நிறுவிய சட்டப்பூர்வ மைல்கல் எது?",
        [
            ("A", "Government of India Act of 1919 (statutory status) and Government of India Act of 1935 (Federal Auditor-General appointment by Crown)", "1919 இந்திய அரசுச் சட்டம் (சட்டப்பூர்வ அந்தஸ்து) மற்றும் 1935 இந்திய அரசுச் சட்டம் (பிரிட்டிஷ் முடியால் கூட்டாட்சி தணிக்கை அதிகாரி நியமனம்)"),
            ("B", "Regulating Act of 1773 and Pitt's India Act of 1784", "1773 ஒழுங்குமுறைச் சட்டம் மற்றும் 1784 பிட் இந்தியச் சட்டம்"),
            ("C", "Charter Act of 1833 and Charter Act of 1853", "1833 சாசனச் சட்டம் மற்றும் 1853 சாசனச் சட்டம்"),
            ("D", "Indian Independence Act of 1947 only", "1947 இந்திய சுதந்திரச் சட்டம் மட்டுமே")
        ],
        "A",
        "Historical Context: Evolution of public financial accountability and audit independence in India.\nReason: Auditor-General post was created in 1858 (Lord Canning appointed Sir Edward Drummond in 1860). 1919 Act gave statutory status to Auditor-General, making him independent of executive control. 1935 Act provided for appointment of Auditor-General of India by His Majesty King and prohibited his removal except in like manner as a Federal Court judge.\nConstitutional Impact: Direct institutional precursor to Comptroller and Auditor General of India (CAG) under Article 148.\nExam Trap: Office created in 1858/1860; statutory independence granted in 1919; Crown appointment in 1935 $\rightarrow$ Article 148 CAG.\nMemory Trick: 1858 Creation $\rightarrow$ 1919 Statutory Independence $\rightarrow$ 1935 Crown Appointment $\rightarrow$ Art 148 CAG.",
        "வரலாற்றுப் பின்னணி: இந்தியாவில் பொது நிதிப் பொறுப்புக்கூறல் மற்றும் தணிக்கை சுதந்திரத்தின் வளர்ச்சி.\nகாரணம்: தணிக்கை அதிகாரி பதவி 1858-ல் உருவாக்கப்பட்டது (1860-ல் லார்டு கேனிங் சர் எட்வர்ட் டிரம்மாண்டை நியமித்தார்). 1919 சட்டம் தணிக்கை அதிகாரிகளுக்குச் சட்டப்பூர்வ அந்தஸ்தை அளித்து நிர்வாகக் கட்டுப்பாட்டிலிருந்து விலக்கியது. 1935 சட்டம் பிரிட்டிஷ் மன்னரால் கூட்டாட்சி தணிக்கை அதிகாரி நியமிக்கப்பட வேண்டும் எனவும், கூட்டாட்சி நீதிபதி போலன்றி நீக்கப்படக் கூடாது எனவும் விதித்தது.\nஅரசியலமைப்பு தாக்கம்: சரத்து 148-ன் கீழ் அமையும் இந்திய தலைமைத் தணிக்கை அதிகாரிக்கு (CAG) நேரடி முன்னோடி.\nதேர்வுப் பொறி: உருவாக்கப்பட்டது 1858/1860; சட்டப்பூர்வ சுதந்திரம் 1919; அரசரின் நியமனம் 1935 $\rightarrow$ சரத்து 148 CAG.\nநினைவுச் சூத்திரம்: 1858 உருவாக்கம் $\rightarrow$ 1919 சட்டப்பூர்வ சுதந்திரம் $\rightarrow$ 1935 அரசரின் நியமனம் $\rightarrow$ சரத்து 148 CAG.",
        {
            "A": {"en": "Correct. 1919 gave statutory status and 1935 made Auditor-General a Crown appointment independent of executive.", "ta": "சரி. 1919 சட்டப்பூர்வ அந்தஸ்தையும் 1935 அரசரின் சுதந்திர நியமனத்தையும் அளித்தன."},
            "B": {"en": "Incorrect. Auditor-General did not exist in 1773 or 1784.", "ta": "தவறு. 1773 அல்லது 1784-ல் தணிக்கை அதிகாரி இருக்கவில்லை."},
            "C": {"en": "Incorrect. Charter Acts did not institute independent Auditor-General.", "ta": "தவறு. சாசனச் சட்டங்கள் சுதந்திர தணிக்கை அதிகாரியை அமைக்கவில்லை."},
            "D": {"en": "Incorrect. Office and statutory independence predated 1947 Act.", "ta": "தவறு. பதவி மற்றும் சுதந்திரம் 1947-க்கு முந்தியது."}
        },
        "TNPSC Trap: Article 148 of Indian Constitution (CAG) is modeled on the provisions of Government of India Act 1935 regarding Auditor-General.",
        "TNPSC பொறி: இந்திய அரசியலமைப்பின் சரத்து 148 (CAG) 1935 இந்திய அரசுச் சட்டத்தின் தணிக்கை அதிகாரி விதிகளை மாதிரியாகக் கொண்டது.",
        "V. Narahari Rao was the first Comptroller and Auditor General (CAG) of independent India (1948-1954).",
        "வி. நரஹரி ராவ் சுதந்திர இந்தியாவின் முதல் தலைமை தணிக்கை அதிகாரியாவார் (1948-1954).",
        ["Polity", "Historical Background", "Auditor General Evolution", "CAG Article 148", "Multi-Act Integration", "Grand Test"], "Analyze", 75
    ))

    # Q70: Statement Based - Hard - Simon Commission Findings & Dyarchy Failure
    questions.append(make_q(
        70, "Hard", "Statement Based",
        "Consider the following statements regarding the reasons for the failure of Dyarchy as analyzed by the Simon Commission (1930):\n1. Dyarchy was inherently complex and lacked a unified executive cabinet responsibility.\n2. The division of subjects into 'Reserved' and 'Transferred' was illogical and administratively intertwined (e.g., Agriculture was Transferred but Irrigation was Reserved).\n3. Ministers in charge of Transferred subjects had no control over the Finance department, which was a Reserved subject.\n4. Governors used their overriding emergency powers frequently, undermining ministerial authority.\nWhich of the statements given above are correct?",
        "1930 சைமன் குழுவின் அறிக்கையில் ஆராயப்பட்டவாறு இரட்டை ஆட்சி தோல்வியடைந்ததற்கான காரணங்கள் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இரட்டை ஆட்சி இயல்பாகவே சிக்கலானது மற்றும் ஒருங்கிணைந்த கேபினட் பொறுப்புக்கூறல் இல்லாதது.\n2. 'ஒதுக்கப்பட்டவை' மற்றும் 'மாற்றப்பட்டவை' எனத் துறைகளைப் பிரித்தது தர்க்கமற்றதாகவும் நிர்வாக ரீதியாக பிணைக்கப்பட்டதாகவும் இருந்தது (எ.கா. வேளாண்மை மாற்றப்பட்டது, ஆனால் பாசனம் ஒதுக்கப்பட்டது).\n3. மாற்றப்பட்ட துறை அமைச்சர்களுக்கு ஒதுக்கப்பட்ட துறையான நிதித்துறையின் மீது எந்தக் கட்டுப்பாடும் இருக்கவில்லை.\n4. கவர்னர்கள் தங்களது நிராகரிக்கும் அவசரகால அதிகாரங்களை அடிக்கடி பயன்படுத்தி அமைச்சரவை அதிகாரத்தைக் குறைமதிப்பிற்கு உட்படுத்தினர்.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
        [
            ("A", "1, 2, 3 and 4", "1, 2, 3 மற்றும் 4"),
            ("B", "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டுமே"),
            ("C", "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டுமே"),
            ("D", "1 and 4 only", "1 மற்றும் 4 மட்டுமே")
        ],
        "A",
        "Historical Context: Structural analysis of Dyarchy failure leading to recommendations for Provincial Autonomy in 1935 Act.\nReason: All four statements are correct. Dyarchy failed because of executive friction (Statement 1), illogical subject split like Agriculture vs Irrigation (Statement 2), financial starvation of ministers (Statement 3), and Governor intervention (Statement 4).\nConstitutional Impact: Caused British Parliament to abandon Dyarchy in provinces and enact Provincial Autonomy under 1935 Act.\nExam Trap: Agriculture was Transferred; Irrigation was Reserved $\rightarrow$ Classic example of Dyarchy failure.\nMemory Trick: Dyarchy Failure = Illogical Split (Agri/Irri) + No Finance Control + Governor Veto.",
        "வரலாற்றுப் பின்னணி: 1935 சட்டத்தில் மாகாண தன்னாட்சிப் பரிந்துரைக்கு வழிவகுத்த இரட்டை ஆட்சி தோல்வியின் கட்டமைப்பு ஆய்வு.\nகாரணம்: நான்கு கூற்றுகளும் சரியானவை. இரட்டை ஆட்சி நிர்வாக மோதல் (கூற்று 1), வேளாண்மை-பாசனம் போன்ற தர்க்கமற்ற பிளவு (கூற்று 2), அமைச்சர்களுக்கான நிதி முடக்கம் (கூற்று 3), கவர்னர் தலையீடு (கூற்று 4) ஆகியவற்றால் தோல்வியடைந்தது.\nஅரசியலமைப்பு தாக்கம்: பிரிட்டிஷ் நாடாளுமன்றம் மாகாண இரட்டை ஆட்சையைக் கைவிட்டு 1935 சட்டத்தில் மாகாண தன்னாட்சியை இயற்றக் காரணமானது.\nதேர்வுப் பொறி: வேளாண்மை மாற்றப்பட்டது; பாசனம் ஒதுக்கப்பட்டது $\rightarrow$ இரட்டை ஆட்சி தோல்வியின் சிறந்த உதாரணம்.\nநினைவுச் சூத்திரம்: இரட்டை ஆட்சி தோல்வி = தர்க்கமற்ற பிளவு (வேளாண்மை/பாசனம்) + நிதிக்கட்டுப்பாடின்மை + கவர்னர் தடுப்பதிகாரம்.",
        {
            "A": {"en": "Correct. All four statements accurately describe the structural causes of Dyarchy failure.", "ta": "சரி. இரட்டை ஆட்சி தோல்விக்கான கட்டமைப்பு காரணங்களை நான்கு கூற்றுகளும் துல்லியமாக விவரிக்கின்றன."},
            "B": {"en": "Incorrect. Statement 4 is also correct.", "ta": "தவறு. கூற்று 4-ம் சரியானது."},
            "C": {"en": "Incorrect. Statement 1 is also correct.", "ta": "தவறு. கூற்று 1-ம் சரியானது."},
            "D": {"en": "Incorrect. Statements 2 and 3 are also correct.", "ta": "தவறு. கூற்றுகள் 2 மற்றும் 3-ம் சரியானவை."}
        },
        "TNPSC Trap: Simon Commission described Dyarchy as 'an unnatural and unstable compromise' between autocracy and democracy.",
        "TNPSC பொறி: சைமன் குழு இரட்டை ஆட்சியை தன்னாதிக்கத்திற்கும் ஜனநாயகத்திற்கும் இடையிலான 'இயற்கைக்கு மாறான மற்றும் நிலையற்ற சமரசம்' என விவரித்தது.",
        "1935 Act completely accepted Simon Commission's recommendation to abolish provincial Dyarchy.",
        "1935 சட்டம் மாகாண இரட்டை ஆட்சியை ஒழிப்பதற்கான சைமன் குழுவின் பரிந்துரையை முழுமையாக ஏற்றது.",
        ["Polity", "Historical Background", "Dyarchy Failure", "Simon Commission 1930", "Grand Test"], "Analyze", 75
    ))

    # Q71: Direct MCQ - Medium - Indian Councils Act 1892 Budget Questions Rules
    questions.append(make_q(
        71, "Medium", "Direct MCQ",
        "Under the Indian Councils Act of 1892, how many days of advance notice were required for members to ask questions on financial statements in the Legislative Council?",
        "1892 ஆம் ஆண்டின் இந்தியக் கவுன்சில்கள் சட்டத்தின் கீழ், சட்ட மேலவையில் நிதி நிலை அறிக்கைகள் (பட்ஜெட்) மீது கேள்விகள் கேட்க உறுப்பினர்களுக்கு எத்தனை நாட்கள் முன்அறிவிப்பு தேவைப்பட்டது?",
        [
            ("A", "6 Days", "6 நாட்கள்"),
            ("B", "14 Days", "14 நாட்கள்"),
            ("C", "30 Days", "30 நாட்கள்"),
            ("D", "2 Days", "2 நாட்கள்")
        ],
        "A",
        "Historical Context: Procedural statutory rules under Indian Councils Act 1892.\nReason: Under the rules framed pursuant to the 1892 Act, members were allowed to ask questions on financial matters by giving 6 days advance notice to the Government. However, no supplementary questions could be asked, and the President could disallow any question without assigning reasons.\nConstitutional Impact: Earliest procedural rules for parliamentary question hour in India.\nExam Trap: 6 days advance notice was required under 1892 Act rules; no supplementary questions were allowed.\nMemory Trick: 1892 Question Rules = 6 Days Notice + No Supplementary Qs.",
        "வரலாற்றுப் பின்னணி: 1892 இந்தியக் கவுன்சில்கள் சட்டத்தின் கீழ் நடைமுறைச் சட்ட விதிகள்.\nகாரணம்: 1892 சட்ட விதிகள் படி, உறுப்பினர்கள் அரசுக்கு 6 நாட்கள் முன்அறிவிப்பு கொடுத்து நிதி விவகாரங்களில் கேள்விகள் கேட்க அனுமதிக்கப்பட்டனர். ஆனால் துணைக்கேள்விகள் கேட்க முடியாது, தலைவர் எந்தக் கேள்வியையும் காரணமின்றி நிராகரிக்கலாம்.\nஅரசியலமைப்பு தாக்கம்: இந்தியாவில் நாடாளுமன்ற கேள்வி நேரத்திற்கான ஆரம்பகால நடைமுறை விதிகள்.\nதேர்வுப் பொறி: 1892 விதிகளின் கீழ் 6 நாட்கள் முன்அறிவிப்பு தேவை; துணைக்கேள்விகளுக்கு அனுமதி இல்லை.\nநினைவுச் சூத்திரம்: 1892 கேள்வி விதிகள் = 6 நாட்கள் முன்அறிவிப்பு + துணைக்கேள்வி இல்லை.",
        {
            "A": {"en": "Correct. 6 days advance notice was required to ask questions on budget under 1892 Act rules.", "ta": "சரி. 1892 விதிகளின் கீழ் பட்ஜெட்டில் கேள்வி கேட்க 6 நாட்கள் முன்அறிவிப்பு தேவைப்பட்டது."},
            "B": {"en": "Incorrect. 14 days notice is standard for resolutions/motions in modern Parliament.", "ta": "தவறு. 14 நாட்கள் நவீன நாடாளுமன்றத்தில் தீர்மானங்களுக்கானது."},
            "C": {"en": "Incorrect. 30 days was not required.", "ta": "தவறு. 30 நாட்கள் தேவைப்படவில்லை."},
            "D": {"en": "Incorrect. 2 days was insufficient for financial questions.", "ta": "தவறு. 2 நாட்கள் போதுமானதாக இல்லை."}
        },
        "TNPSC Trap: Supplementary questions on financial statements were introduced later by Indian Councils Act 1909.",
        "TNPSC பொறி: நிதி அறிக்கைகள் மீதான துணைக்கேள்விகள் பின்னர் 1909 இந்தியக் கவுன்சில்கள் சட்டத்தாலேயே அறிமுகப்படுத்தப்பட்டன.",
        "1892 Act allowed questions on executive policy, but prohibited questions on matters under judicial sub-judice.",
        "1892 சட்டம் நிர்வாகக் கொள்கை மீது கேள்விகளை அனுமதித்தது, ஆனால் நீதிமன்ற விசாரணையில் உள்ள வழக்குகள் மீதான கேள்விகளைத் தடை செய்தது.",
        ["Polity", "Historical Background", "Indian Councils Act 1892", "Budget Questions", "Grand Test"], "Understand", 60
    ))

    # Q72: Multi-Act Comparative - Hard - Evolution of Emergency Provisions (1919 to 1935)
    questions.append(make_q(
        72, "Hard", "Multi-Act Comparative",
        "Which comparative inference correctly maps the emergency powers framework between the 1919 Act and the 1935 Act?",
        "1919 சட்டம் மற்றும் 1935 சட்டத்திற்கு இடையே அவசரகால அதிகாரங்களின் சட்டகத்தை சரியாக வரைபடமாக்கும் ஒப்பீட்டு முடிவு எது?",
        [
            ("A", "1919 Act contained limited Governor-General emergency certification and ordinance powers, whereas 1935 Act contained comprehensive emergency powers: Section 93 (Provincial Emergency), Section 45 (Federal Emergency), and Section 102 (Proclamation of Emergency empowering central legislature to legislate on provincial subjects)", "1919 சட்டம் வரம்பிற்குட்பட்ட கவர்னர்-ஜெனரல் சான்றளிப்பு, அவசரச் சட்ட அதிகாரங்களைக் கொண்டிருந்தது; ஆனால் 1935 சட்டம் விரிவான அவசரகால அதிகாரங்களைக் கொண்டிருந்தது: பிரிவு 93 (மாகாண அவசரநிலை), பிரிவு 45 (கூட்டாட்சி அவசரநிலை), பிரிவு 102 (மத்திய சட்டமன்றம் மாகாணத் துறைகளில் சட்டமியற்ற அதிகாரமளிக்கும் அவசரநிலை பிரகடனம்)"),
            ("B", "1919 Act contained full emergency powers while 1935 Act removed all emergency powers", "1919 சட்டம் முழு அவசரகால அதிகாரங்களைக் கொண்டிருந்தது; ஆனால் 1935 சட்டம் அனைத்து அவசரகால அதிகாரங்களையும் நீக்கியது"),
            ("C", "1935 Act gave emergency powers to Provincial Ministers instead of Governors", "1935 சட்டம் கவர்னர்களுக்குப் பதிலாக மாகாண அமைச்சர்களுக்கு அவசரகால அதிகாரங்களை அளித்தது"),
            ("D", "Neither Act provided for emergency legislation", "எந்தச் சட்டமும் அவசரகால சட்டமியற்றலை வழங்கவில்லை")
        ],
        "A",
        "Historical Context: Development of emergency provisions in colonial governance that served as blueprints for Part XVIII of Indian Constitution.\nReason: 1919 Act had basic executive certification and ordinance power. 1935 Act detailed complete emergency mechanisms: Section 93 (failure of provincial constitutional machinery $\rightarrow$ Art 356), Section 45 (failure of federal machinery), and Section 102 (Proclamation of Emergency allowing center to legislate on provincial list $\rightarrow$ Art 250 / Art 352).\nConstitutional Impact: Direct statutory source for emergency provisions (Articles 352, 356, 360) in modern Constitution.\nExam Trap: Section 102 of 1935 Act = Article 250 / Article 352 of Indian Constitution.\nMemory Trick: 1935 Act Section 93 (Art 356 precursor) + Section 102 (Art 352/250 precursor).",
        "வரலாற்றுப் பின்னணி: இந்திய அரசியலமைப்பின் பகுதி XVIII-க்கு வரைபடமாக அமைந்த காலனித்துவ அவசரகால விதிகளின் வளர்ச்சி.\nகாரணம்: 1919 சட்டம் அடிப்படை சான்றளிப்பு, அவசரச் சட்ட அதிகாரத்தைக் கொண்டிருந்தது. 1935 சட்டம் முழு அவசரகால பொறிமுறைகளை விவரித்தது: பிரிவு 93 (மாகாண அரசியலமைப்பு முடக்கம் $\rightarrow$ சரத்து 356), பிரிவு 45 (கூட்டாட்சி முடக்கம்), பிரிவு 102 (மையம் மாகாணப் பட்டியலில் சட்டமியற்ற உதவும் அவசரநிலை பிரகடனம் $\rightarrow$ சரத்து 250 / சரத்து 352).\nஅரசியலமைப்பு தாக்கம்: நவீன அரசியலமைப்பின் அவசரகால விதிகளுக்கு (சரத்துகள் 352, 356, 360) நேரடி சட்ட மூலமானது.\nதேர்வுப் பொறி: 1935 சட்டத்தின் பிரிவு 102 = இந்திய அரசியலமைப்பின் சரத்து 250 / சரத்து 352.\nநினைவுச் சூத்திரம்: 1935 சட்டம் பிரிவு 93 (சரத்து 356 முன்னோடி) + பிரிவு 102 (சரத்து 352/250 முன்னோடி).",
        {
            "A": {"en": "Correct. 1935 Act detailed Sections 93, 45, and 102 emergency provisions, forming the blueprint for Part XVIII.", "ta": "சரி. 1935 சட்டம் 93, 45, 102 அவசரகால பிரிவுகளை விவரித்து பகுதி XVIII-க்கு வரைபடமானது."},
            "B": {"en": "Incorrect. Reverses emergency complexity; 1935 Act expanded emergency powers.", "ta": "தவறு. 1935 சட்டமே அவசரகால அதிகாரங்களை விரிவுபடுத்தியது."},
            "C": {"en": "Incorrect. Emergency powers remained with Governors and Governor-General.", "ta": "தவறு. அவசரகால அதிகாரம் கவர்னர்களிடமே இருந்தது."},
            "D": {"en": "Incorrect. Both Acts contained emergency legislation rules.", "ta": "தவறு. இரு சட்டங்களிலும் அவசரகால விதிகள் இருந்தன."}
        },
        "TNPSC Trap: Emergency provisions of Indian Constitution (Part XVIII) were mostly borrowed from Government of India Act 1935, while suspension of Fundamental Rights during emergency was borrowed from Weimar Constitution of Germany.",
        "TNPSC பொறி: இந்திய அரசியலமைப்பின் அவசரகால விதிகள் (பகுதி XVIII) 1935 சட்டத்திலிருந்தும்; அவசர காலத்தில் அடிப்படை உரிமைகள் இடைநீக்கம் ஜெர்மனியின் வைமர் அரசியலமைப்பிலிருந்தும் பெறப்பட்டன.",
        "Section 102 of 1935 Act allowed Federal Legislature to make laws for a province during proclaimed emergency.",
        "1935 சட்டத்தின் பிரிவு 102 பிரகடனப்படுத்தப்பட்ட அவசர காலத்தில் மாகாணத்திற்காக கூட்டாட்சி சட்டமன்றம் சட்டமியற்ற அனுமதித்தது.",
        ["Polity", "Historical Background", "GOI Act 1935", "Emergency Provisions", "Article 352 356 Precursor", "Multi-Act Integration", "Grand Test"], "Analyze", 75
    ))

    # Q73: Statement Based - Medium - Charter Act 1813 Religious & Educational Clauses
    questions.append(make_q(
        73, "Medium", "Statement Based",
        "Consider the following statements regarding the Charter Act of 1813:\n1. It allowed Christian missionaries to come to India for the purpose of enlightening the people and promoting moral upliftment.\n2. It directed the East India Company to set aside a sum of one lakh rupees annually for the revival and promotion of literature and encouragement of learned natives of India.\n3. It completely abolished the East India Company's tea trade monopoly with China.\nWhich of the statements given above is/are correct?",
        "1813 ஆம் ஆண்டின் சாசனச் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது மக்களுக்கு விழிப்புணர்வூட்டவும் நன்னெறி முன்னேற்றத்தை ஊக்குவிக்கவும் கிறிஸ்துவ மதபரப்பாளர்கள் இந்தியாவிற்கு வர அனுமதித்தது.\n2. இது இலக்கியத்தின் மறுமலர்ச்சி மற்றும் இந்திய கற்றறிந்த மனிதர்களை ஊக்குவிப்பதற்காக கிழக்கிந்திய கம்பெனியை ஆண்டிற்கு ஒரு லட்சம் ரூபாய் ஒதுக்கீடு செய்ய ஆணையிட்டது.\n3. இது சீனாவுடனான கிழக்கிந்திய கம்பெனியின் தேயிலை வர்த்தக முற்றுரிமையை முற்றிலும் ஒழித்தது.\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானவை?",
        [
            ("A", "1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
            ("B", "2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
            ("C", "1 and 3 only", "1 மற்றும் 3 மட்டுமே"),
            ("D", "1, 2 and 3", "1, 2 மற்றும் 3")
        ],
        "A",
        "Historical Context: Charter Act 1813 opened India to British missionaries and state-sponsored education.\nReason: Statements 1 and 2 are correct. Christian missionaries were licensed (Statement 1) and Rs. 1 Lakh allocated for education (Statement 2). Statement 3 is incorrect because the 1813 Act RETAINED the EIC monopoly on tea trade and trade with China (these were abolished later by Charter Act 1833).\nConstitutional Impact: First statutory state financial obligation for education in British India.\nExam Trap: 1813 Act RETAINED tea & China trade monopoly; 1833 Act ABOLISHED tea & China trade monopoly.\nMemory Trick: 1813 = Missionaries + Rs. 1 Lakh Education + Tea/China Monopoly Retained.",
        "வரலாற்றுப் பின்னணி: 1813 சாசனச் சட்டம் இந்தியாவை பிரிட்டிஷ் மதபரப்பாளர்களுக்கும் அரசு நிதியுதவி கல்விக்கும் திறந்தது.\nகாரணம்: கூற்றுகள் 1 மற்றும் 2 சரியானவை. கிறிஸ்துவ மதபரப்பாளர்கள் அனுமதிக்கப்பட்டனர் (கூற்று 1), கல்விக்கு 1 லட்சம் ரூபாய் ஒதுக்கப்பட்டது (கூற்று 2). கூற்று 3 தவறானது, ஏனெனில் 1813 சட்டம் தேயிலை மற்றும் சீனா வர்த்தக முற்றுரிமையைத் தக்கவைத்தது (இவை பின்னர் 1833 சாசனச் சட்டத்தாலேயே ஒழிக்கப்பட்டன).\nஅரசியலமைப்பு தாக்கம்: பிரிட்டிஷ் இந்தியாவில் கல்விக்கான முதல் சட்டப்பூர்வ அரசு நிதிப் பொறுப்பு.\nதேர்வுப் பொறி: 1813 சட்டம் தேயிலை, சீனா முற்றுரிமையைத் தக்கவைத்தது; 1833 சட்டம் அதை ஒழித்தது.\nநினைவுச் சூத்திரம்: 1813 = மதபரப்பாளர்கள் + 1 லட்சம் கல்வி நிதி + தேயிலை/சீனா முற்றுரிமை நீடிப்பு.",
        {
            "A": {"en": "Correct. Statements 1 and 2 are true; Statement 3 is false as 1813 retained tea & China trade monopoly.", "ta": "சரி. கூற்றுகள் 1 மற்றும் 2 சரி; 1813 தேயிலை, சீனா முற்றுரிமையைத் தக்கவைத்ததால் கூற்று 3 தவறு."},
            "B": {"en": "Incorrect. Statement 3 is false.", "ta": "தவறு. கூற்று 3 தவறானது."},
            "C": {"en": "Incorrect. Statement 3 is false.", "ta": "தவறு. கூற்று 3 தவறானது."},
            "D": {"en": "Incorrect. Statement 3 is false.", "ta": "தவறு. கூற்று 3 தவறானது."}
        },
        "TNPSC Trap: Rs 1 Lakh education grant under 1813 Act led to the Orientalist vs Anglicist controversy settled by Macaulay's Minute on Education in 1835.",
        "TNPSC பொறி: 1813 சட்டத்தின் 1 லட்சம் ரூபாய் கல்வி நிதி 1835 மெக்காலேயின் கல்வி அறிக்கையால் தீர்க்கப்பட்ட கீழ்திசைவாதிகள்-ஆங்கிலேயவாதிகள் சர்ச்சைக்கு வழிவகுத்தது.",
        "Charter Act 1813 asserted the explicit sovereignty of the British Crown over the Company's territories in India.",
        "1813 சாசனச் சட்டம் கம்பெனியின் இந்திய நிலப்பரப்புகள் மீது பிரிட்டிஷ் முடியாட்சியின் வெளிப்படையான இறையாண்மையை உறுதிப்படுத்தியது.",
        ["Polity", "Historical Background", "Charter Act 1813", "Education Grant", "Christian Missionaries", "Grand Test"], "Analyze", 75
    ))

    # Q74: Direct MCQ - Medium - Indian Councils Act 1909 Shimla Deputation Link
    questions.append(make_q(
        74, "Medium", "Direct MCQ",
        "Which historical deputation of Muslim leaders met Viceroy Lord Minto at Shimla in October 1906, directly leading to the inclusion of separate electorates in the Indian Councils Act 1909?",
        "அக்டோபர் 1906-ல் சிம்லாவில் வைஸ்ராய் லார்டு மிண்டோவைச் சந்தித்த முஸ்லிம் தலைவர்களின் எந்த வரலாற்றுத் தூதுக்குழு, 1909 இந்தியக் கவுன்சில்கள் சட்டத்தில் தனித் தொகுதிகள் நேரடியாக இணைக்கப்படக் காரணமானது?",
        [
            ("A", "Shimla Deputation led by Aga Khan", "ஆகா கான் தலைமையிலான சிம்லா தூதுக்குழு (Shimla Deputation)"),
            ("B", "Delhi Proposal led by Muhammad Ali Jinnah", "முகமது அலி ஜின்னா தலைமையிலான டெல்லி முன்மொழிவு"),
            ("C", "Khilafat Committee Deputation", "கிலாஃபத் குழு தூதுக்குழு"),
            ("D", "Aligarh Muslim Educational Conference Deputation led by Sir Syed Ahmed Khan", "சர் சையத் அகமது கான் தலைமையிலான அலிகார் முஸ்லிம் கல்வி மாநாட்டுத் தூதுக்குழு")
        ],
        "A",
        "Historical Context: Political lobbying that led directly to communal electorate provisions in 1909 Morley-Minto reforms.\nReason: On October 1, 1906, a delegation of 35 prominent Muslim leaders led by Aga Khan met Viceroy Lord Minto at Shimla (Shimla Deputation) demanding separate electorates and weightage for Muslims in representation. Lord Minto accepted these demands, which were subsequently incorporated into the Indian Councils Act of 1909.\nConstitutional Impact: Institutionalization of communal politics in British Indian statutory framework.\nExam Trap: Shimla Deputation = Aga Khan (1906); Shimla Conference = Lord Wavell (1945).\nMemory Trick: Shimla Deputation 1906 (Aga Khan & Lord Minto) $\rightarrow$ 1909 Separate Electorates.",
        "வரலாற்றுப் பின்னணி: 1909 மோலி-மிண்டோ சீர்திருத்தங்களில் வகுப்புவாத தொகுதி விதிகளுக்கு நேரடியாக வழிவகுத்த அரசியல் தூதுக் குழு.\nகாரணம்: 1906 அக்டோபர் 1 அன்று ஆகா கான் தலைமையிலான 35 முக்கிய முஸ்லிம் தலைவர்களின் தூதுக்குழு சிம்லாவில் வைஸ்ராய் லார்டு மிண்டோவைச் சந்தித்து முஸ்லிம்களுக்குத் தனித் தொகுதிகளையும் கூடுதல் பிரதிநிதித்துவத்தையும் கோரியது. லார்டு மிண்டோ இக்கோரிக்கைகளை ஏற்றார், அவை 1909 இந்தியக் கவுன்சில்கள் சட்டத்தில் இணைக்கப்பட்டன.\nஅரசியலமைப்பு தாக்கம்: பிரிட்டிஷ் இந்திய சட்டப்பூர்வ சட்டகத்தில் வகுப்புவாத அரசியலை நிறுவனப்படுத்தியது.\nதேர்வுப் பொறி: சிம்லா தூதுக்குழு = ஆகா கான் (1906); சிம்லா மாநாடு = லார்டு வேவல் (1945).\nநினைவுச் சூத்திரம்: சிம்லா தூதுக்குழு 1906 (ஆகா கான் & லார்டு மிண்டோ) $\rightarrow$ 1909 தனித் தொகுதிகள்.",
        {
            "A": {"en": "Correct. Shimla Deputation led by Aga Khan in Oct 1906 demanded separate electorates.", "ta": "சரி. அக்டோபர் 1906-ல் ஆகா கான் தலைமையிலான சிம்லா தூதுக்குழு தனித் தொகுதிகளைக் கோரியது."},
            "B": {"en": "Incorrect. Delhi Proposals were submitted in 1927.", "ta": "தவறு. டெல்லி முன்மொழிவுகள் 1927-ல் சமர்ப்பிக்கப்பட்டன."},
            "C": {"en": "Incorrect. Khilafat Movement was in 1919-1922.", "ta": "தவறு. கிலாஃபத் இயக்கம் 1919-1922-ல் இருந்தது."},
            "D": {"en": "Incorrect. Sir Syed Ahmed Khan died in 1898.", "ta": "தவறு. சர் சையத் அகமது கான் 1898-ல் மறைந்தார்."}
        },
        "TNPSC Trap: All-India Muslim League was founded shortly after the Shimla Deputation in December 1906 at Dacca (Dhaka).",
        "TNPSC பொறி: அகில இந்திய முஸ்லிம் லீக் சிம்லா தூதுக்குழுவிற்குப் பிறகு 1906 டிசம்பரில் டாக்காவில் தோற்றுவிக்கப்பட்டது.",
        "Lord Minto wrote to Morley in 1906: 'We are sowing dragon's teeth and the harvest will be bitter'.",
        "1906-ல் லார்டு மிண்டோ மோலிக்கு எழுதினார்: 'நாம் நாகப்பாம்பின் பற்களை விதைக்கிறோம், அறுவடை கசப்பானதாக இருக்கும்'.",
        ["Polity", "Historical Background", "Shimla Deputation 1906", "Indian Councils Act 1909", "Grand Test"], "Understand", 60
    ))

    # Q75: Exceptional Difficult - Hard - 1935 Act Joint Select Committee & White Paper Origins
    questions.append(make_q(
        75, "Exceptional Difficult", "Statement Based",
        "Consider the following sequence of constitutional documents that directly led to the enactment of the Government of India Act 1935:\n1. Publication of the Simon Commission Report (May 1930)\n2. Convening of the Three Round Table Conferences in London (1930–1932)\n3. Publication of the British Government's 'White Paper on Constitutional Reforms' (March 1933)\n4. Report of the Joint Select Committee of British Parliament chaired by Lord Linlithgow (1934)\nWhich option correctly states the chronological evolution of these foundational documents?",
        "1935 இந்திய அரசுச் சட்டம் இயற்றப்படுவதற்கு நேரடியாக வழிவகுத்த அரசியலமைப்பு ஆவணங்களின் பின்வரும் காலவரிசையைக் கவனியுங்கள்:\n1. சைமன் குழு அறிக்கை வெளியீடு (மே 1930)\n2. லண்டனில் மூன்று வட்டமேஜை மாநாடுகள் கூட்டுதல் (1930–1932)\n3. பிரிட்டிஷ் அரசின் 'அரசியலமைப்பு சீர்திருத்தங்கள் பற்றிய வெள்ளை அறிக்கை' வெளியீடு (மார்ச் 1933)\n4. லார்டு லின்லித்கோ தலைமையிலான பிரிட்டிஷ் நாடாளுமன்றக் கூட்டுத் தேர்வுக் குழுவின் அறிக்கை (1934)\nஇந்த அடிப்படை ஆவணங்களின் சரியான காலவரிசை வளர்ச்சியைக் குறிப்பிடும் தெரிவு எது?",
        [
            ("A", "1 -> 2 -> 3 -> 4", "1 -> 2 -> 3 -> 4"),
            ("B", "2 -> 1 -> 3 -> 4", "2 -> 1 -> 3 -> 4"),
            ("C", "3 -> 1 -> 2 -> 4", "3 -> 1 -> 2 -> 4"),
            ("D", "1 -> 3 -> 2 -> 4", "1 -> 3 -> 2 -> 4")
        ],
        "A",
        "Historical Context: Detailed statutory legislative trail resulting in the longest Act enacted by British Parliament (GOI Act 1935).\nReason: Correct sequence is: 1 (Simon Commission Report May 1930) $\rightarrow$ 2 (Three RTCs Nov 1930 - Dec 1932) $\rightarrow$ 3 (White Paper March 1933) $\rightarrow$ 4 (Joint Select Committee Report Nov 1934 chaired by Lord Linlithgow). The Bill based on the Joint Committee Report was enacted as the GOI Act 1935 in August 1935.\nConstitutional Impact: Most exhaustive constitutional enactment of British India.\nExam Trap: White Paper came AFTER the 3rd Round Table Conference (1933); Joint Select Committee was chaired by Lord Linlithgow.\nMemory Trick: Simon Report (1930) $\rightarrow$ RTCs (1930-32) $\rightarrow$ White Paper (1933) $\rightarrow$ Joint Committee (1934) $\rightarrow$ 1935 Act.",
        "வரலாற்றுப் பின்னணி: பிரிட்டிஷ் நாடாளுமன்றத்தால் இயற்றப்பட்ட மிகநீளமான சட்டத்திற்கு (1935 அரசுச் சட்டம்) வழிவகுத்த சட்டப் பாதை.\nகாரணம்: சரியான வரிசை: 1 (சைமன் குழு அறிக்கை மே 1930) $\rightarrow$ 2 (மூன்று வட்டமேஜை மாநாடுகள் நவம்பர் 1930 - டிசம்பர் 1932) $\rightarrow$ 3 (வெள்ளை அறிக்கை மார்ச் 1933) $\rightarrow$ 4 (லார்டு லின்லித்கோ தலைமையிலான கூட்டுத் தேர்வுக் குழு அறிக்கை நவம்பர் 1934). கூட்டுத் தேர்வுக் குழு அறிக்கையின் அடிப்படையில் வரைவு செய்யப்பட்ட மசோதாவே 1935 ஆகஸ்டில் 1935 இந்திய அரசுச் சட்டமாக நிறைவேறியது.\nஅரசியலமைப்பு தாக்கம்: பிரிட்டிஷ் இந்தியாவின் மிகவும் விரிவான அரசியலமைப்புச் சட்டம்.\nதேர்வுப் பொறி: வெள்ளை அறிக்கை 3வது வட்டமேஜை மாநாட்டிற்குப் பிறகே வந்தது (1933); கூட்டுத் தேர்வுக் குழுவின் தலைவர் லார்டு லின்லித்கோ.\nநினைவுச் சூத்திரம்: சைமன் அறிக்கை (1930) $\rightarrow$ வட்டமேஜை மாநாடுகள் (1930-32) $\rightarrow$ வெள்ளை அறிக்கை (1933) $\rightarrow$ கூட்டுத் தேர்வுக் குழு (1934) $\rightarrow$ 1935 சட்டம்.",
        {
            "A": {"en": "Correct sequence: Simon Report (1930) -> RTCs (1930-32) -> White Paper (1933) -> Joint Committee (1934).", "ta": "சரி. காலவரிசை: சைமன் அறிக்கை (1930) -> வட்டமேஜை மாநாடுகள் (1930-32) -> வெள்ளை அறிக்கை (1933) -> கூட்டுத் தேர்வுக் குழு (1934)."},
            "B": {"en": "Incorrect. Simon Report (1) preceded the First Round Table Conference (2).", "ta": "தவறு. சைமன் அறிக்கை 1வது வட்டமேஜை மாநாட்டிற்கு முந்தியது."},
            "C": {"en": "Incorrect. White Paper (3) came after the Round Table Conferences.", "ta": "தவறு. வெள்ளை அறிக்கை வட்டமேஜை மாநாடுகளுக்குப் பின் வந்தது."},
            "D": {"en": "Incorrect. White Paper (3) came after RTCs (2).", "ta": "தவறு. வெள்ளை அறிக்கை மாநாடுகளுக்குப் பின் வந்தது."}
        },
        "TNPSC Trap: Lord Linlithgow chaired the Joint Select Committee (1933-34) and subsequently became the Viceroy of India (1936-1943) who implemented the 1935 Act.",
        "TNPSC பொறி: லார்டு லின்லித்கோ கூட்டுத் தேர்வுக் குழுவின் தலைவராக இருந்து (1933-34), பின்னர் 1935 சட்டத்தை அமல்படுத்திய இந்தியாவின் வைஸ்ராயானார் (1936-1943).",
        "Government of India Act 1935 contained 321 Sections and 10 Schedules, making it the longest Act passed by British Parliament.",
        "1935 இந்திய அரசுச் சட்டம் 321 பிரிவுகளையும் 10 அட்டவணைகளையும் கொண்டு பிரிட்டிஷ் நாடாளுமன்றத்தின் மிகநீளமான சட்டமானது.",
        ["Polity", "Historical Background", "GOI Act 1935 Origins", "Linlithgow Joint Committee", "White Paper 1933", "Grand Test"], "Evaluate", 90
    ))

    return questions

if __name__ == "__main__":
    qs = get_part3_questions()
    print(f"Part 3 Questions Generated: {len(qs)}")
