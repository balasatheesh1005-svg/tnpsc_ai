import json
import os

q_list = []

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

# ----------------------------------------------------
# 100 GRAND TEST QUESTIONS - MIXED QUESTION TYPES & DIFFICULTIES
# ----------------------------------------------------

# Q1: Direct MCQ - Easy - Regulating Act 1773
q_list.append(make_q(
    1, "Easy", "Direct MCQ",
    "Which Act of the British Parliament designated the Governor of Bengal as the 'Governor-General of Bengal' for the first time?",
    "பிரிட்டிஷ் நாடாளுமன்றத்தின் எந்தச் சட்டம் முதன்முறையாக வங்காள ஆளுநரை 'வங்காள கவர்னர்-ஜெனரல்' என மாற்றியமைத்தது?",
    [
        ("A", "Regulating Act of 1773", "1773 ஆம் ஆண்டின் ஒழுங்குமுறைச் சட்டம்"),
        ("B", "Pitt's India Act of 1784", "1784 ஆம் ஆண்டின் பிட் இந்தியச் சட்டம்"),
        ("C", "Charter Act of 1813", "1813 ஆம் ஆண்டின் சாசனச் சட்டம்"),
        ("D", "Charter Act of 1833", "1833 ஆம் ஆண்டின் சாசனச் சட்டம்")
    ],
    "A",
    "The Regulating Act of 1773 designated the Governor of Bengal as the 'Governor-General of Bengal' and created an Executive Council of four members to assist him. Warren Hastings was the first such Governor-General.",
    "1773 ஆம் ஆண்டின் ஒழுங்குமுறைச் சட்டம் வங்காள ஆளுநரை 'வங்காள கவர்னர்-ஜெனரல்' என மாற்றி, அவருக்கு உதவ 4 உறுப்பினர்களைக் கொண்ட நிர்வாகக் குழுவை உருவாக்கியது. வாரன் ஹேஸ்டிங்ஸ் முதல் கவர்னர்-ஜெனரலாவார்.",
    {
        "A": {"en": "Correct. 1773 Act created Governor-General of Bengal.", "ta": "சரி. 1773 சட்டம் வங்காள கவர்னர்-ஜெனரலை உருவாக்கியது."},
        "B": {"en": "Incorrect. 1784 Act created Board of Control.", "ta": "தவறு. 1784 சட்டம் கட்டுப்பாட்டு வாரியத்தை உருவாக்கியது."},
        "C": {"en": "Incorrect. 1813 Act ended EIC trade monopoly except tea and China.", "ta": "தவறு. 1813 சட்டம் தேயிலை, சீனா தவிர்த்து வர்த்தக முற்றுரிமையை ஒழித்தது."},
        "D": {"en": "Incorrect. 1833 Act created Governor-General of India.", "ta": "தவறு. 1833 சட்டம் இந்தியாவின் கவர்னர்-ஜெனரலை உருவாக்கியது."}
    },
    "TNPSC Trap: 1773 Act = Governor-General of Bengal; 1833 Act = Governor-General of India.",
    "TNPSC பொறி: 1773 சட்டம் = வங்காள கவர்னர்-ஜெனரல்; 1833 சட்டம் = இந்திய கவர்னர்-ஜெனரல்.",
    "Warren Hastings became the first Governor-General of Bengal in 1773.",
    "1773-ல் வாரன் ஹேஸ்டிங்ஸ் வங்காளத்தின் முதல் கவர்னர்-ஜெனரலானார்.",
    ["Polity", "Historical Background", "Regulating Act 1773", "Grand Test"], "Remember", 45
))

# Q2: Conceptual MCQ - Medium - Pitt's India Act 1784
q_list.append(make_q(
    2, "Medium", "Conceptual MCQ",
    "What was the dual system of control introduced by Pitt's India Act of 1784?",
    "1784 ஆம் ஆண்டின் பிட் இந்தியச் சட்டத்தால் அறிமுகப்படுத்தப்பட்ட இரட்டை நிர்வாக முறை யாது?",
    [
        ("A", "Division of subjects into Reserved and Transferred", "துறைகளை ஒதுக்கப்பட்டவை மற்றும் மாற்றப்பட்டவை எனப் பிரித்தல்"),
        ("B", "Court of Directors managing commercial affairs and Board of Control managing political affairs", "இயக்குநர்கள் அவை வணிக விவகாரங்களையும், கட்டுப்பாட்டு வாரியம் அரசியல் விவகாரங்களையும் நிர்வகித்தல்"),
        ("C", "Division of powers between Federal and Provincial governments", "கூட்டாட்சி மற்றும் மாகாண அரசுகளுக்கு இடையே அதிகாரங்களைப் பிரித்தல்"),
        ("D", "Bicameral central legislature with Upper and Lower houses", "மேலவை மற்றும் கீழவை கொண்ட இரு அவை மத்திய சட்டமன்றம்")
    ],
    "B",
    "Pitt's India Act 1784 established dual control: Court of Directors managed commercial affairs, while a new 6-member Board of Control was established to manage civil, military, and revenue political affairs.",
    "1784 பிட் இந்தியச் சட்டம் இரட்டை ஆட்சியை நிறுவியது: இயக்குநர்கள் அவை வணிக விவகாரங்களையும், புதிய 6 உறுப்பினர் கட்டுப்பாட்டு வாரியம் அரசியல் விவகாரங்களையும் நிர்வகித்தன.",
    {
        "A": {"en": "Incorrect. Reserved and Transferred division was Dyarchy under 1919 Act.", "ta": "தவறு. ஒதுக்கப்பட்ட மற்றும் மாற்றப்பட்ட துறைகள் 1919 சட்ட இரட்டை ஆட்சியாகும்."},
        "B": {"en": "Correct. Court of Directors (Commercial) and Board of Control (Political).", "ta": "சரி. இயக்குநர்கள் அவை (வணிகம்) மற்றும் கட்டுப்பாட்டு வாரியம் (அரசியல்)."},
        "C": {"en": "Incorrect. Federal and Provincial division was introduced in 1935 Act.", "ta": "தவறு. கூட்டாட்சி-மாகாணப் பிரிப்பு 1935 சட்டத்தில் அறிமுகமானது."},
        "D": {"en": "Incorrect. Bicameralism was introduced in 1919 Act.", "ta": "தவறு. இரு அவை முறை 1919 சட்டத்தில் அறிமுகமானது."}
    },
    "TNPSC Trap: Board of Control members were appointed by the British Crown and paid out of Indian revenues (from 1793).",
    "TNPSC பொறி: கட்டுப்பாட்டு வாரிய உறுப்பினர்கள் பிரிட்டிஷ் முடியால் நியமிக்கப்பட்டனர்; அவர்தம் சம்பளம் இந்திய வருவாயிலிருந்து வழங்கப்பட்டது.",
    "1784 Act for the first time called EIC territories as 'British possessions in India'.",
    "1784 சட்டம் முதன்முறையாக கம்பெனி நிலப்பரப்புகளை 'இந்தியாவில் உள்ள பிரிட்டிஷ் உடமைகள்' எனக் குறிப்பிட்டது.",
    ["Polity", "Historical Background", "Pitts India Act 1784", "Grand Test"], "Understand", 60
))

# Q3: Statement Based - Hard - Charter Act 1833
q_list.append(make_q(
    3, "Hard", "Statement Based",
    "Consider the following statements regarding the Charter Act of 1833:\n1. It made the Governor-General of Bengal as the Governor-General of India.\n2. It ended the commercial activities of the East India Company, making it a purely administrative body.\n3. It successfully introduced an open competition system for the selection of civil servants.\nWhich of the statements given above is/are correct?",
    "1833 ஆம் ஆண்டின் சாசனச் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது வங்காள கவர்னர்-ஜெனரலை இந்தியாவின் கவர்னர்-ஜெனரலாக மாற்றியது.\n2. இது கிழக்கிந்திய கம்பெனியின் வணிக நடவடிக்கைகளை முடிவுக்குக் கொண்டுவந்து, அதை முற்றிலும் நிர்வாக அமைப்பாக மாற்றியது.\n3. இது சிவில் சர்வீஸ் தேர்வுக்கு திறந்தவெளி போட்டித் தேர்வு முறையை வெற்றிகரமாக அறிமுகப்படுத்தியது.\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானவை?",
    [
        ("A", "1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
        ("B", "2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
        ("C", "1 and 3 only", "1 மற்றும் 3 மட்டுமே"),
        ("D", "1, 2 and 3", "1, 2 மற்றும் 3")
    ],
    "A",
    "Statements 1 and 2 are correct. Statement 3 is incorrect because, although Section 87 of the 1833 Act attempted an open competition system, it was negated due to strong opposition from the Court of Directors. Open competition was actually introduced later by the Charter Act of 1853.",
    "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் 1833 சட்டம் போட்டித் தேர்வை முயற்சியுற்றாலும் இயக்குநர்கள் அவையின் எதிர்ப்பால் அது கைவிடப்பட்டது. 1853 சட்டத்திலேயே போட்டித் தேர்வு நடைமுறைக்கு வந்தது.",
    {
        "A": {"en": "Correct. Statements 1 and 2 are correct; 3 is false as 1833 open competition attempt failed.", "ta": "சரி. கூற்றுகள் 1 மற்றும் 2 சரி; 1833 முயற்சி தோல்வியடைந்ததால் 3 தவறு."},
        "B": {"en": "Incorrect. Statement 3 is false.", "ta": "தவறு. கூற்று 3 தவறானது."},
        "C": {"en": "Incorrect. Statement 3 is false.", "ta": "தவறு. கூற்று 3 தவறானது."},
        "D": {"en": "Incorrect. Statement 3 is false.", "ta": "தவறு. கூற்று 3 தவறானது."}
    },
    "TNPSC Trap: Open competition attempted in 1833 (failed); successfully introduced in 1853 Charter Act.",
    "TNPSC பொறி: திறந்தவெளி போட்டித் தேர்வு 1833-ல் முயற்சி செய்யப்பட்டது (தோல்வி); 1853 சாசனச் சட்டத்தில் வெற்றிகரமாக அறிமுகமானது.",
    "Lord William Bentinck was the first Governor-General of India under 1833 Act.",
    "1833 சட்டத்தின் கீழ் லார்டு வில்லியம் பென்டிங்க் இந்தியாவின் முதல் கவர்னர்-ஜெனரலானார்.",
    ["Polity", "Historical Background", "Charter Act 1833", "Grand Test"], "Analyze", 75
))

# Q4: Assertion & Reason - Hard - Charter Act 1853
q_list.append(make_q(
    4, "Hard", "Assertion & Reason",
    "Assertion (A): The Charter Act of 1853 separated, for the first time, the legislative and executive functions of the Governor-General's Council.\nReason (R): It added six new members called legislative councillors to the Governor-General's Executive Council.",
    "கூற்று (A): 1853 ஆம் ஆண்டின் சாசனச் சட்டம் முதன்முறையாக கவர்னர்-ஜெனரல் கவுன்சிலின் சட்ட மற்றும் நிர்வாகப் பணிகளைப் பிரித்தது.\nகாரணம் (R): இது கவர்னர்-ஜெனரலின் நிர்வாகக் குழுவில் சட்ட மேலவை உறுப்பினர்கள் எனப்படும் ஆறு புதிய உறுப்பினர்களைச் சேர்த்தது.",
    [
        ("A", "Both (A) and (R) are true and (R) is the correct explanation of (A)", "(A) மற்றும் (R) இரண்டும் உண்மை, மேலும் (R) என்பது (A)-வின் சரியான விளக்கமாகும்"),
        ("B", "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கமல்ல"),
        ("C", "(A) is true but (R) is false", "(A) உண்மை, ஆனால் (R) தவறு"),
        ("D", "(A) is false but (R) is true", "(A) தவறு, ஆனால் (R) உண்மை")
    ],
    "A",
    "Both (A) and (R) are true, and (R) is the correct explanation of (A). Adding 6 legislative councillors created a distinct legislative wing known as the Indian (Central) Legislative Council, separating legislative work from executive council work.",
    "(A) மற்றும் (R) இரண்டும் உண்மை, மேலும் (R) என்பது (A)-வின் சரியான விளக்கம். 6 புதிய சட்ட உறுப்பினர்களைச் சேர்த்ததன் மூலம் சட்டப் பணிகள் நிர்வாகப் பணிகளிலிருந்து பிரிக்கப்பட்டன.",
    {
        "A": {"en": "Correct. Addition of 6 legislative members established the legislative branch.", "ta": "சரி. 6 புதிய சட்ட உறுப்பினர்கள் சேர்க்கப்பட்டதே சட்டப்பிரிவு உருவாகக் காரணமானது."},
        "B": {"en": "Incorrect. Reason directly explains the Assertion.", "ta": "தவறு. காரணம் கூற்றை நேரடியாக விளக்குகிறது."},
        "C": {"en": "Incorrect. Reason is true.", "ta": "தவறு. காரணம் உண்மையானது."},
        "D": {"en": "Incorrect. Assertion is true.", "ta": "தவறு. கூற்று உண்மையானது."}
    },
    "TNPSC Trap: 4 out of 6 legislative members were appointed by local governments of Madras, Bombay, Bengal, and Agra.",
    "TNPSC பொறி: 6 சட்ட உறுப்பினர்களில் 4 பேர் மதராஸ், பம்பாய், வங்காளம், ஆக்ரா உள்ளூர் அரசுகளால் நியமிக்கப்பட்டனர்.",
    "Charter Act 1853 created Central Legislative Council which functioned as a mini-parliament.",
    "1853 சாசனச் சட்டம் சிறிய நாடாளுமன்றமாகச் செயல்பட்ட மத்திய சட்ட மேலவையை உருவாக்கியது.",
    ["Polity", "Historical Background", "Charter Act 1853", "Grand Test"], "Evaluate", 90
))

# Q5: Match the Following - Medium - Institutions & Acts
q_list.append(make_q(
    5, "Medium", "Match the Following",
    "Match List I (Institutions/Offices) with List II (Enacting Legislation):\n\nList I\nA. Supreme Court at Fort William\nB. Board of Control\nC. Secretary of State for India\nD. Federal Court of India\n\nList II\n1. Government of India Act, 1858\n2. Government of India Act, 1935\n3. Regulating Act, 1773\n4. Pitt's India Act, 1784",
    "பட்டியல் I (நிறுவனங்கள்/அலுவலகங்கள்) உடன் பட்டியல் II (இயற்றப்பட்ட சட்டம்) பொருத்துக:\n\nபட்டியல் I\nA. வில்லியம் கோட்டை உச்ச நீதிமன்றம்\nB. கட்டுப்பாட்டு வாரியம்\nC. இந்திய அரசுச் செயலர்\nD. இந்தியாவின் கூட்டாட்சி நீதிமன்றம்\n\nபட்டியல் II\n1. 1858 இந்திய அரசுச் சட்டம்\n2. 1935 இந்திய அரசுச் சட்டம்\n3. 1773 ஒழுங்குமுறைச் சட்டம்\n4. 1784 பிட் இந்தியச் சட்டம்",
    [
        ("A", "A-3, B-4, C-1, D-2", "A-3, B-4, C-1, D-2"),
        ("B", "A-4, B-3, C-1, D-2", "A-4, B-3, C-1, D-2"),
        ("C", "A-3, B-1, C-4, D-2", "A-3, B-1, C-4, D-2"),
        ("D", "A-2, B-4, C-1, D-3", "A-2, B-4, C-1, D-3")
    ],
    "A",
    "Correct match: A-3 (Fort William SC -> 1773 Act), B-4 (Board of Control -> 1784 Act), C-1 (Secretary of State -> 1858 Act), D-2 (Federal Court -> 1935 Act).",
    "சரியான பொருத்தம்: A-3 (உச்ச நீதிமன்றம் -> 1773 சட்டம்), B-4 (கட்டுப்பாட்டு வாரியம் -> 1784 சட்டம்), C-1 (அரசுச் செயலர் -> 1858 சட்டம்), D-2 (கூட்டாட்சி நீதிமன்றம் -> 1935 சட்டம்).",
    {
        "A": {"en": "Correct match across all four foundational institutions.", "ta": "சரி. நான்கு முக்கிய நிறுவனங்களுக்கும் சரியான பொருத்தம்."},
        "B": {"en": "Incorrect. Fort William SC was 1773 Act (3).", "ta": "தவறு. வில்லியம் கோட்டை உச்ச நீதிமன்றம் 1773 சட்டம் (3)."},
        "C": {"en": "Incorrect. Board of Control was 1784 Act (4).", "ta": "தவறு. கட்டுப்பாட்டு வாரியம் 1784 சட்டம் (4)."},
        "D": {"en": "Incorrect. Fort William SC was not 1935 Act.", "ta": "தவறு. வில்லியம் கோட்டை உச்ச நீதிமன்றம் 1935 சட்டமல்ல."}
    },
    "TNPSC Trap: Supreme Court Fort William set up in 1774; Federal Court set up in 1937.",
    "TNPSC பொறி: வில்லியம் கோட்டை உச்ச நீதிமன்றம் 1774-ல் அமைக்கப்பட்டது; கூட்டாட்சி நீதிமன்றம் 1937-ல் அமைக்கப்பட்டது.",
    "Secretary of State replaced the President of Board of Control in 1858.",
    "1858-ல் இந்திய அரசுச் செயலர் கட்டுப்பாட்டு வாரியத் தலைவருக்குப் பதிலாக வந்தார்.",
    ["Polity", "Historical Background", "Match the Following", "Grand Test"], "Analyze", 75
))

# Q6: Chronology - Medium - Acts Chronology
q_list.append(make_q(
    6, "Medium", "Chronology",
    "Arrange the following Acts in correct chronological sequence:\n1. Indian Councils Act of 1892\n2. Charter Act of 1853\n3. Indian Councils Act of 1861\n4. Indian Councils Act of 1909",
    "பின்வரும் சட்டங்களை சரியான காலவரிசையில் அமைக்கவும்:\n1. 1892 ஆம் ஆண்டின் இந்தியக் கவுன்சில்கள் சட்டம்\n2. 1853 ஆம் ஆண்டின் சாசனச் சட்டம்\n3. 1861 ஆம் ஆண்டின் இந்தியக் கவுன்சில்கள் சட்டம்\n4. 1909 ஆம் ஆண்டின் இந்தியக் கவுன்சில்கள் சட்டம்",
    [
        ("A", "2 -> 3 -> 1 -> 4", "2 -> 3 -> 1 -> 4"),
        ("B", "3 -> 2 -> 1 -> 4", "3 -> 2 -> 1 -> 4"),
        ("C", "2 -> 1 -> 3 -> 4", "2 -> 1 -> 3 -> 4"),
        ("D", "2 -> 3 -> 4 -> 1", "2 -> 3 -> 4 -> 1")
    ],
    "A",
    "Correct Chronological Sequence: 2 (Charter Act 1853) -> 3 (Indian Councils Act 1861) -> 1 (Indian Councils Act 1892) -> 4 (Indian Councils Act 1909).",
    "சரியான காலவரிசை: 2 (1853 சாசனச் சட்டம்) -> 3 (1861 இந்தியக் கவுன்சில்கள் சட்டம்) -> 1 (1892 இந்தியக் கவுன்சில்கள் சட்டம்) -> 4 (1909 இந்தியக் கவுன்சில்கள் சட்டம்).",
    {
        "A": {"en": "Correct sequence matching enactment dates: 1853 -> 1861 -> 1892 -> 1909.", "ta": "சரி. சட்ட இயற்றப்பட்ட ஆண்டுகள்: 1853 -> 1861 -> 1892 -> 1909."},
        "B": {"en": "Incorrect. Charter Act 1853 (2) was before Indian Councils Act 1861 (3).", "ta": "தவறு. 1853 சாசனச் சட்டம் (2) 1861 சட்டத்திற்கு (3) முந்தியது."},
        "C": {"en": "Incorrect. 1861 Act (3) came before 1892 Act (1).", "ta": "தவறு. 1861 சட்டம் (3) 1892 சட்டத்திற்கு (1) முந்தியது."},
        "D": {"en": "Incorrect. 1892 Act (1) came before 1909 Act (4).", "ta": "தவறு. 1892 சட்டம் (1) 1909 சட்டத்திற்கு (4) முந்தியது."}
    },
    "TNPSC Trap: Charter Act 1853 was under Company Rule; Indian Councils Acts 1861, 1892, 1909 were under Crown Rule.",
    "TNPSC பொறி: 1853 சாசனச் சட்டம் கம்பெனி ஆட்சியில்; 1861, 1892, 1909 கவுன்சில்கள் சட்டங்கள் பிரிட்டிஷ் முடி ஆட்சியில்.",
    "1853 Act was the last Charter Act; 1861 Act started the Councils Acts series.",
    "1853 சட்டம் கடைசி சாசனச் சட்டம்; 1861 சட்டம் கவுன்சில்கள் சட்ட வரிசையைத் தொடங்கியது.",
    ["Polity", "Historical Background", "Chronology", "Grand Test"], "Analyze", 75
))

# Q7: Integrated PYQ Style - Hard - Evolution of Executive Council
q_list.append(make_q(
    7, "Hard", "Integrated Evolution",
    "Trace the structural expansion of the Governor-General's / Viceroy's Executive Council from 1773 to 1909:\n1. Regulating Act 1773\n2. Charter Act 1833\n3. Indian Councils Act 1861\n4. Indian Councils Act 1909\nWhich option correctly describes the addition of members to the Council at each stage?",
    "1773 முதல் 1909 வரையிலான கவர்னர்-ஜெனரல் / வைஸ்ராயின் நிர்வாகக் குழுவின் அமைப்புக் விரிவாக்கத்தை ஆராய்க:\n1. 1773 ஒழுங்குமுறைச் சட்டம்\n2. 1833 சாசனச் சட்டம்\n3. 1861 இந்தியக் கவுன்சில்கள் சட்டம்\n4. 1909 இந்தியக் கவுன்சில்கள் சட்டம்\nஒவ்வொரு கட்டத்திலும் குழுவில் உறுப்பினர்கள் சேர்க்கப்பட்டதைச் சரியாக விவரிக்கும் தெரிவு எது?",
    [
        ("A", "4 Executive members created (1773) -> 4th Law Member added (1833) -> 5th Member added & Portfolio System recognized (1861) -> First Indian Member appointed (1909)", "4 நிர்வாக உறுப்பினர்கள் (1773) -> 4வது சட்ட உறுப்பினர் சேர்க்கை (1833) -> 5வது உறுப்பினர் சேர்க்கை & இலாகா முறை (1861) -> முதல் இந்திய உறுப்பினர் நியமனம் (1909)"),
        ("B", "4th Law Member added (1773) -> 4 Executive members created (1833) -> First Indian Member (1861) -> 5th Member added (1909)", "4வது சட்ட உறுப்பினர் (1773) -> 4 நிர்வாக உறுப்பினர்கள் (1833) -> முதல் இந்திய உறுப்பினர் (1861) -> 5வது உறுப்பினர் (1909)"),
        ("C", "First Indian Member (1773) -> 4 Executive members (1833) -> 4th Law Member (1861) -> 5th Member (1909)", "முதல் இந்திய உறுப்பினர் (1773) -> 4 நிர்வாக உறுப்பினர்கள் (1833) -> 4வது சட்ட உறுப்பினர் (1861) -> 5வது உறுப்பினர் (1909)"),
        ("D", "4 Executive members (1773) -> First Indian Member (1833) -> 4th Law Member (1861) -> 5th Member (1909)", "4 நிர்வாக உறுப்பினர்கள் (1773) -> முதல் இந்திய உறுப்பினர் (1833) -> 4வது சட்ட உறுப்பினர் (1861) -> 5வது உறுப்பினர் (1909)")
    ],
    "A",
    "Option A correctly maps executive council changes: 1773 created Council of 4; 1833 added 4th Law Member (Macaulay); 1861 added 5th member and recognized Portfolio System; 1909 appointed S.P. Sinha as 1st Indian member.",
    "தெரிவு A சரியான நிர்வாகக் குழு மாற்றங்களைக் காட்டுகிறது: 1773 (4 உறுப்பினர்கள்) -> 1833 (4வது சட்ட உறுப்பினர்) -> 1861 (5வது உறுப்பினர் & இலாகா முறை) -> 1909 (எஸ்.பி. சின்கா முதல் இந்திய உறுப்பினர்).",
    {
        "A": {"en": "Correct. Perfectly describes executive council member expansion steps.", "ta": "சரி. நிர்வாகக் குழு உறுப்பினர்கள் விரிவடைந்த நிலைகளைத் துல்லியமாக விவரிக்கிறது."},
        "B": {"en": "Incorrect. 4th Law Member was added in 1833, not 1773.", "ta": "தவறு. 4வது சட்ட உறுப்பினர் 1833-ல் சேர்க்கப்பட்டார்."},
        "C": {"en": "Incorrect. First Indian member joined in 1909, not 1773.", "ta": "தவறு. முதல் இந்திய உறுப்பினர் 1909-ல் சேர்ந்தார்."},
        "D": {"en": "Incorrect. First Indian member joined in 1909, not 1833.", "ta": "தவறு. முதல் இந்திய உறுப்பினர் 1909-ல் சேர்ந்தார்."}
    },
    "TNPSC Trap: Lord Macaulay was 4th Law Member (1833); S.P. Sinha was 1st Indian Law Member in Viceroy Council (1909).",
    "TNPSC பொறி: லார்டு மெக்காலே 4வது சட்ட உறுப்பினர் (1833); எஸ்.பி. சின்கா வைஸ்ராய் குழுவின் 1வது இந்திய சட்ட உறுப்பினர் (1909).",
    "5th member added in 1861 was a Finance member (James Wilson drafted 1st Indian budget).",
    "1861-ல் சேர்க்கப்பட்ட 5வது உறுப்பினர் நிதி உறுப்பினராவார் (ஜேம்ஸ் வில்சன் 1வது இந்திய பட்ஜெட்டைத் தயாரித்தார்).",
    ["Polity", "Historical Background", "Integrated Evolution", "Executive Council"], "Evaluate", 90
))

# Q8: Direct MCQ - Medium - Amending Act 1781
q_list.append(make_q(
    8, "Medium", "Direct MCQ",
    "The Amending Act of 1781 exempted which of the following officials from the jurisdiction of the Supreme Court for their official actions?",
    "1781 ஆம் ஆண்டின் திருத்தச் சட்டம் பின்வரும் எந்த அதிகாரிகளை அவர்களின் அதிகாரப்பூர்வ நடவடிக்கைகளுக்காக உச்ச நீதிமன்ற அதிகார வரம்பிலிருந்து விலக்கியது?",
    [
        ("A", "Governor-General and Council only", "கவர்னர்-ஜெனரல் மற்றும் கவுன்சில் மட்டுமே"),
        ("B", "Servants of the Company only", "கம்பெனி ஊழியர்கள் மட்டுமே"),
        ("C", "Both Governor-General in Council and Servants of the Company for their official acts", "அதிகாரப்பூர்வ பணிகளுக்காக கவர்னர்-ஜெனரல் கவுன்சில் மற்றும் கம்பெனி ஊழியர்கள் இருசாரரும்"),
        ("D", "Judges of the Supreme Court only", "உச்ச நீதிமன்ற நீதிபதிகள் மட்டுமே")
    ],
    "C",
    "The Amending Act of 1781 exempted the Governor-General and Council, as well as the servants of the Company, from the jurisdiction of the Supreme Court for acts done by them in their official capacity.",
    "1781 திருத்தச் சட்டம் கவர்னர்-ஜெனரல், கவுன்சில் மற்றும் கம்பெனி ஊழியர்களை அவர்தம் அதிகாரப்பூர்வ பணிகளுக்காக உச்ச நீதிமன்ற வரம்பிலிருந்து விலக்கியது.",
    {
        "A": {"en": "Incorrect. Servants of the Company were also exempted for official acts.", "ta": "தவறு. கம்பெனி ஊழியர்களுக்கும் விலக்களிக்கப்பட்டது."},
        "B": {"en": "Incorrect. Governor-General and Council were also exempted.", "ta": "தவறு. கவர்னர்-ஜெனரல் மற்றும் கவுன்சிலுக்கும் விலக்களிக்கப்பட்டது."},
        "C": {"en": "Correct. Exempted both GG-in-Council and Company servants for official acts.", "ta": "சரி. அதிகாரப்பூர்வ பணிகளுக்காக இருசாரருக்கும் விலக்களித்தது."},
        "D": {"en": "Incorrect. Judges were not exempted from judicial accountability.", "ta": "தவறு. நீதிபதிகளுக்கு விலக்களிக்கப்படவில்லை."}
    },
    "TNPSC Trap: 1781 Act also exempted revenue matters and revenue collection from Supreme Court jurisdiction.",
    "TNPSC பொறி: 1781 சட்டம் வருவாய் விவகாரங்களையும் வருவாய் வசூலையும் உச்ச நீதிமன்ற வரம்பிலிருந்து விலக்கியது.",
    "1781 Act declared that Supreme Court should administer personal law of the defendant (Hindu law for Hindus, Mohammedan law for Muslims).",
    "1781 சட்டம் எதிராளியின் தனிநபர் சட்டப்படி (இந்துக்களுக்கு இந்து சட்டம், முஸ்லிம்களுக்கு முகமதிய சட்டம்) நீதிமன்றம் தீர்ப்பு வழங்க வேண்டும் எனக் கூறியது.",
    ["Polity", "Historical Background", "Act of Settlement 1781", "Grand Test"], "Understand", 60
))

# Q9: Conceptual MCQ - Hard - Government of India Act 1858
q_list.append(make_q(
    9, "Hard", "Conceptual MCQ",
    "What was the nature and status of the Council of India established under the Government of India Act 1858?",
    "1858 இந்திய அரசுச் சட்டத்தின் கீழ் நிறுவப்பட்ட 'இந்தியக் குழுவின்' (Council of India) தன்மை மற்றும் அந்தஸ்து யாது?",
    [
        ("A", "A 15-member advisory body chaired by the Secretary of State for India", "இந்திய அரசுச் செயலரைத் தலைவராகக் கொண்ட 15 உறுப்பினர்களைக் கொண்ட ஆலோசனைக் குழு"),
        ("B", "A sovereign legislative assembly elected by provincial councils", "மாகாணக் குழுக்களால் தேர்ந்தெடுக்கப்பட்ட ஒரு இறையாண்மை கொண்ட சட்டமன்ற அமைப்பு"),
        ("C", "A 6-member executive cabinet based in Calcutta", "கொல்கத்தாவை தளமாகக் கொண்ட 6 உறுப்பினர்களைக் கொண்ட நிர்வாக அமைச்சரவை"),
        ("D", "A judicial tribunal hearing appeals against Indian High Courts", "இந்திய உயர் நீதிமன்றங்களுக்கு எதிரான மேல்முறையீடுகளை விசாரிக்கும் நீதிமன்ற தீர்ப்பாயம்")
    ],
    "A",
    "The 1858 Act created a 15-member Council of India to assist the Secretary of State for India. The Council was an advisory body, and the Secretary of State was made its Chairman.",
    "1858 சட்டம் இந்திய அரசுச் செயலருக்கு உதவ 15 உறுப்பினர்களைக் கொண்ட இந்தியக் குழுவை உருவாக்கியது. இக்குழு ஒரு ஆலோசனைக் அமைப்பாகும், அரசுச் செயலர் இதன் தலைவராவார்.",
    {
        "A": {"en": "Correct. 15-member advisory body based in London, chaired by Secretary of State.", "ta": "சரி. லண்டனில் இயங்கிய அரசுச் செயலரைத் தலைவராகக் கொண்ட 15 உறுப்பினர் ஆலோசனைக் குழு."},
        "B": {"en": "Incorrect. It was an advisory council, not an elected legislature.", "ta": "தவறு. இது ஆலோசனைக் குழுவாகும், தேர்ந்தெடுக்கப்பட்ட சட்டமன்றமல்ல."},
        "C": {"en": "Incorrect. It was based in London, not Calcutta.", "ta": "தவறு. இது லண்டனில் இயங்கியது, கொல்கத்தாவில் அல்ல."},
        "D": {"en": "Incorrect. Privy Council was the judicial appellate body.", "ta": "தவறு. ப்ரிவி கவுன்சிலே நீதித்துறை மேல்முறையீட்டு அமைப்பாகும்."}
    },
    "TNPSC Trap: 8 members of Council of India were appointed by the Crown, and 7 were selected by Court of Directors.",
    "TNPSC பொறி: 15 உறுப்பினர்களில் 8 பேரை பிரிட்டிஷ் முடியாட்சியும், 7 பேரை இயக்குநர்கள் அவையும் தேர்வு செய்தன.",
    "The Council of India was a corporate body capable of suing and being sued in England and India.",
    "இந்தியக் குழு இங்கிலாந்து மற்றும் இந்தியாவில் வழக்குத் தொடரவும் வழக்கை எதிர்கொள்ளவும் தகுதியுள்ள ஒரு சட்டப்பூர்வ அமைப்பாகும்.",
    ["Polity", "Historical Background", "GOI Act 1858", "Council of India"], "Analyze", 75
))

# Q10: Statement Based - Medium - Indian Councils Act 1861
q_list.append(make_q(
    10, "Medium", "Statement Based",
    "Consider the following statements regarding the Indian Councils Act of 1861:\n1. It initiated the process of decentralization by restoring legislative powers to Bombay and Madras Presidencies.\n2. It empowered the Viceroy to issue Ordinances during emergencies without the concurrence of the legislative council.\n3. It introduced an official majority of elected Indian members in the Central Legislative Council.\nWhich of the statements given above is/are correct?",
    "1861 ஆம் ஆண்டின் இந்தியக் கவுன்சில்கள் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது பம்பாய் மற்றும் மதராஸ் மாகாணங்களுக்கு சட்ட அதிகாரங்களை மீட்டளிப்பதன் மூலம் அதிகாரப் பரவலாக்கத்தைத் தொடங்கியது.\n2. இது அவசர காலத்தில் சட்ட மேலவையின் ஒப்புதலின்றி அவசரச் சட்டங்களை பிறப்பிக்க வைஸ்ராய்க்கு அதிகாரமளித்தது.\n3. இது மத்திய சட்ட மேலவையில் தேர்ந்தெடுக்கப்பட்ட இந்திய உறுப்பினர்களின் அதிகாரப்பூர்வ பெரும்பான்மையை அறிமுகப்படுத்தியது.\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானவை?",
    [
        ("A", "1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
        ("B", "2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
        ("C", "1 and 3 only", "1 மற்றும் 3 மட்டுமே"),
        ("D", "1, 2 and 3", "1, 2 மற்றும் 3")
    ],
    "A",
    "Statements 1 and 2 are correct. Statement 3 is incorrect because the 1861 Act nominated non-official Indian members (Raja of Benaras, Maharaja of Patiala, Sir Dinkar Rao), but maintained an OFFICIAL majority in the Central Legislative Council.",
    "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் 1861 சட்டம் இந்தியர்களை நியமித்ததே தவிரத் தேர்ந்தெடுக்கவில்லை, மேலும் அதிகாரப்பூர்வ பெரும்பான்மையையே தக்கவைத்தது.",
    {
        "A": {"en": "Correct. Statements 1 and 2 are true; 3 is false as members were nominated, not elected.", "ta": "சரி. கூற்றுகள் 1 மற்றும் 2 சரி; உறுப்பினர்கள் நியமிக்கப்பட்டதால் 3 தவறு."},
        "B": {"en": "Incorrect. Statement 3 is false.", "ta": "தவறு. கூற்று 3 தவறானது."},
        "C": {"en": "Incorrect. Statement 3 is false.", "ta": "தவறு. கூற்று 3 தவறானது."},
        "D": {"en": "Incorrect. Statement 3 is false.", "ta": "தவறு. கூற்று 3 தவறானது."}
    },
    "TNPSC Trap: Ordinances issued by Viceroy under 1861 Act had a life of 6 months.",
    "TNPSC பொறி: 1861 சட்டத்தின் கீழ் வைஸ்ராய் பிறப்பித்த அவசரச் சட்டத்தின் ஆயுட்காலம் 6 மாதங்கள் ஆகும்.",
    "Lord Canning nominated Raja of Benaras, Maharaja of Patiala, and Sir Dinkar Rao to Central Legislative Council in 1862.",
    "1862-ல் லார்டு கேனிங் பெனாரஸ் ராஜா, பட்டியாலா மகாராஜா, சர் தினகர் ராவ் ஆகியோரை மேலவைக்கு நியமித்தார்.",
    ["Polity", "Historical Background", "Indian Councils Act 1861", "Grand Test"], "Analyze", 75
))

print(f"Generated first 10 GT questions. Total: {len(q_list)}")
