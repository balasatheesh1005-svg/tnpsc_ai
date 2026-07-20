import json
import os

q_list = []

def make_q(id_num, diff, q_type, q_en, q_ta, opt_list, ans, exp_en, exp_ta, wno, tip_en, tip_ta, rf_en, rf_ta, tags, bloom="Analyze"):
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
        "id": f"HB_CHRONO_{id_num:03d}",
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
        "estimated_time_sec": 75,
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

# Q1: Analytical
q_list.append(make_q(
    1, "Hard", "Chronology",
    "Arrange the following key legislative provisions during Company Rule in correct chronological order:\n1. Exemption of Governor-General and Council from Supreme Court jurisdiction for official acts\n2. Establishment of Supreme Court of Judicature at Fort William, Calcutta\n3. Extension of Governor-General's overriding powers over his council to future Governors-General\n4. Establishment of the Board of Control to supervise civil, military, and revenue affairs",
    "கம்பெனி ஆட்சியின் போது மேற்கொள்ளப்பட்ட பின்வரும் முக்கிய சட்டப்பூர்வ விதிகளை சரியான காலவரிசையில் அமைக்கவும்:\n1. அதிகாரபூர்வ நடவடிக்கைகளுக்காக உச்ச நீதிமன்ற அதிகார வரம்பிலிருந்து கவர்னர்-ஜெனரல் மற்றும் கவுன்சிலுக்கு விலக்களித்தல்\n2. கொல்கத்தா வில்லியம் கோட்டையில் உச்ச நீதிமன்றம் அமைத்தல்\n3. கவர்னர்-ஜெனரலின் நிராகரிப்பு அதிகாரத்தை எதிர்கால கவர்னர்-ஜெனரல்களுக்கு நீட்டித்தல்\n4. சிவில், ராணுவ மற்றும் வருவாய் விவகாரங்களைக் கண்காணிக்கக் கட்டுப்பாட்டு வாரியத்தை அமைத்தல்",
    [("A", "2 -> 1 -> 4 -> 3", "2 -> 1 -> 4 -> 3"), ("B", "1 -> 2 -> 3 -> 4", "1 -> 2 -> 3 -> 4"), ("C", "2 -> 4 -> 1 -> 3", "2 -> 4 -> 1 -> 3"), ("D", "4 -> 2 -> 1 -> 3", "4 -> 2 -> 1 -> 3")],
    "A",
    "Correct Sequence: 2 (1774 Supreme Court) -> 1 (1781 Exemption) -> 4 (1784 Board of Control) -> 3 (1793 Charter Act). Marks initial Parliamentary regulation of East India Company.",
    "சரியான காலவரிசை: 2 (1774 உச்ச நீதிமன்றம்) -> 1 (1781 விலக்களிப்பு) -> 4 (1784 கட்டுப்பாட்டு வாரியம்) -> 3 (1793 சாசனச் சட்டம்). கிழக்கிந்திய கம்பெனியை நாடாளுமன்றம் ஒழுங்குபடுத்தியதன் தொடக்கத்தைக் குறிக்கிறது.",
    {
        "A": {"en": "Correct. 2 (1774) -> 1 (1781) -> 4 (1784) -> 3 (1793) accurately follows historical enactment dates.", "ta": "சரி. 2 (1774) -> 1 (1781) -> 4 (1784) -> 3 (1793) வரலாற்று சட்ட இயற்றல் ஆண்டுகளைத் துல்லியமாகப் பின்பற்றுகிறது."},
        "B": {"en": "Incorrect. Supreme Court was established in 1774, before the 1781 Exemption Act.", "ta": "தவறு. உச்ச நீதிமன்றம் 1774-ல் அமைக்கப்பட்டது, இது 1781 விலக்களிப்புச் சட்டத்திற்கு முந்தியது."},
        "C": {"en": "Incorrect. Board of Control was established in 1784, after 1781.", "ta": "தவறு. கட்டுப்பாட்டு வாரியம் 1784-ல் அமைக்கப்பட்டது, இது 1781-க்கு பின்னராகும்."},
        "D": {"en": "Incorrect. Board of Control (1784) was not formed before Supreme Court (1774).", "ta": "தவறு. கட்டுப்பாட்டு வாரியம் (1784) உச்ச நீதிமன்றத்திற்கு (1774) முன் அமைக்கப்படவில்லை."}
    },
    "TNPSC Trap: Candidates confuse Supreme Court creation under 1773 Act (1774) with the Amending Act 1781.",
    "TNPSC பொறி: 1773 சட்டத்தின் கீழ் அமைக்கப்பட்ட உச்ச நீதிமன்றத்தையும் (1774), 1781 திருத்தச் சட்டத்தையும் குழப்பிக் கொள்ளக் கூடாது.",
    "The Amending Act of 1781 is also known as the Act of Settlement.",
    "1781 ஆம் ஆண்டின் திருத்தச் சட்டம் 'சீரமைப்புச் சட்டம்' (Act of Settlement) என்றும் அழைக்கப்படுகிறது.",
    ["Polity", "Historical Background", "Chronology", "Regulating Act 1773"]
))

# Q2: Analytical
q_list.append(make_q(
    2, "Hard", "Chronology",
    "Arrange the following Charter Acts and Parliamentary Acts in correct chronological sequence based on the gradual reduction of East India Company's privileges:\n1. Total abolition of EIC commercial monopoly (including tea and trade with China)\n2. Partial abolition of EIC trade monopoly in India, retaining monopoly in tea and trade with China\n3. Complete transfer of Indian administration from EIC to the British Crown\n4. Extension of EIC charter without specifying any fixed time period for the first time",
    "கிழக்கிந்திய கம்பெனியின் சலுகைகள் படிப்படியாகக் குறைக்கப்பட்டதன் அடிப்படையில் பின்வரும் சாசனச் சட்டங்கள் மற்றும் நாடாளுமன்றச் சட்டங்களை சரியான காலவரிசையில் அமைக்கவும்:\n1. தேயிலை மற்றும் சீனாவுடனான வர்த்தகம் உட்பட கம்பெனியின் வர்த்தக முற்றுரிமை முழுமையாக ஒழிக்கப்படல்\n2. தேயிலை மற்றும் சீனா வர்த்தகம் தவிர்த்து இந்தியாவில் கம்பெனியின் வர்த்தக முற்றுரிமை பகுதியளவாக ஒழிக்கப்படல்\n3. இந்திய நிர்வாகம் கிழக்கிந்திய கம்பெனியிடமிருந்து பிரிட்டிஷ் முடிக்கு முழுமையாக மாற்றப்படல்\n4. எந்தவொரு குறிப்பிட்ட காலவரையறையுமின்றி கம்பெனியின் சாசனம் முதன்முறையாக நீட்டிக்கப்படல்",
    [("A", "1 -> 2 -> 4 -> 3", "1 -> 2 -> 4 -> 3"), ("B", "2 -> 1 -> 4 -> 3", "2 -> 1 -> 4 -> 3"), ("C", "2 -> 4 -> 1 -> 3", "2 -> 4 -> 1 -> 3"), ("D", "4 -> 2 -> 1 -> 3", "4 -> 2 -> 1 -> 3")],
    "B",
    "Sequence: 2 (1813 Act) -> 1 (1833 Act) -> 4 (1853 Act) -> 3 (1858 Act). Demonstrates gradual stripping of EIC privileges.",
    "வரிசை: 2 (1813 சட்டம்) -> 1 (1833 சட்டம்) -> 4 (1853 சட்டம்) -> 3 (1858 சட்டம்). கிழக்கிந்திய கம்பெனி உரிமைகள் பறிக்கப்பட்டதை இது காட்டுகிறது.",
    {
        "A": {"en": "Incorrect. Total monopoly abolition (1833) happened after partial abolition (1813).", "ta": "தவறு. முழுமையான வர்த்தக ஒழிப்பு (1833) பகுதியளவு ஒழிப்புக்கு (1813) பிறகே நடந்தது."},
        "B": {"en": "Correct. 2 (1813) -> 1 (1833) -> 4 (1853) -> 3 (1858) follows exact legislative timeline.", "ta": "சரி. 2 (1813) -> 1 (1833) -> 4 (1853) -> 3 (1858) சரியான சட்ட காலவரிசையைப் பின்பற்றுகிறது."},
        "C": {"en": "Incorrect. Charter Act 1853 (4) came after Charter Act 1833 (1).", "ta": "தவறு. 1853 சாசனச் சட்டம் (4) 1833 சாசனச் சட்டத்திற்குப் (1) பின்னரே வந்தது."},
        "D": {"en": "Incorrect. 1853 Act (4) was the last of the four Charter Acts.", "ta": "தவறு. 1853 சட்டம் (4) சாசனச் சட்டங்களில் இறுதியானதாகும்."}
    },
    "TNPSC Trap: Earlier Charter Acts (1793, 1813, 1833) renewed charter for 20 years; 1853 Act did NOT specify a term.",
    "TNPSC பொறி: முந்தைய சாசனச் சட்டங்கள் 20 ஆண்டுகள் நீடித்தன; ஆனால் 1853 சாசனச் சட்டம் குறிப்பிட்ட ஆண்டுக் கெடுவைக் குறிப்பிடவில்லை.",
    "Charter Act of 1833 designated Governor-General of Bengal as Governor-General of India.",
    "1833 சாசனச் சட்டம் வங்காள கவர்னர்-ஜெனரலை 'இந்தியாவின் கவர்னர்-ஜெனரல்' என மாற்றியது.",
    ["Polity", "Historical Background", "Chronology", "Charter Acts"]
))

# Q3: Analytical
q_list.append(make_q(
    3, "Hard", "Chronology",
    "Arrange the following Crown Rule legislative reforms in correct chronological order:\n1. Introduction of Dyarchy in the executive government of Provinces\n2. Granting statutory recognition to Viceroy's Portfolio System and restoration of legislative powers to Presidencies\n3. Introduction of separate electorates for Muslims\n4. First use of the element of election (indirect) for non-official seats in legislative councils",
    "பிரிட்டிஷ் முடி ஆட்சியின் கீழ் கொண்டுவரப்பட்ட பின்வரும் சட்டப்பூர்வ சீர்திருத்தங்களை சரியான காலவரிசையில் அமைக்கவும்:\n1. மாகாணங்களின் நிர்வாக அரசில் இரட்டை ஆட்சி முறையை அறிமுகப்படுத்துதல்\n2. வைஸ்ராயின் இலாகா முறைக்கு சட்டப்பூர்வ அங்கீகாரம் அளித்தல் மற்றும் மாகாணங்களுக்கு சட்டமியற்றும் அதிகாரத்தை மீட்டளித்தல்\n3. முஸ்லிம்களுக்கு தனித் தொகுதிகளை அறிமுகப்படுத்துதல்\n4. சட்ட மேலவைகளில் அதிகாரப்பூர்வமற்ற இடங்களுக்கு முதன்முறையாக (மறைமுக) தேர்தல் முறையைப் பயன்படுத்துதல்",
    [("A", "2 -> 3 -> 4 -> 1", "2 -> 3 -> 4 -> 1"), ("B", "4 -> 2 -> 3 -> 1", "4 -> 2 -> 3 -> 1"), ("C", "2 -> 4 -> 3 -> 1", "2 -> 4 -> 3 -> 1"), ("D", "2 -> 4 -> 1 -> 3", "2 -> 4 -> 1 -> 3")],
    "C",
    "Sequence: 2 (1861 Act) -> 4 (1892 Act) -> 3 (1909 Act) -> 1 (1919 Act). Highlights representative progress in India.",
    "வரிசை: 2 (1861 சட்டம்) -> 4 (1892 சட்டம்) -> 3 (1909 சட்டம்) -> 1 (1919 சட்டம்). இந்தியாவில் பிரதிநிதித்துவ வளர்ச்சியை இது சுட்டிக்காட்டுகிறது.",
    {
        "A": {"en": "Incorrect. Indirect election element (1892) preceded separate electorates (1909).", "ta": "தவறு. மறைமுகத் தேர்தல் (1892) தனித் தொகுதிக்கு (1909) முந்தியது."},
        "B": {"en": "Incorrect. Portfolio system recognition (1861) came before 1892 Act.", "ta": "தவறு. இலாகா முறை அங்கீகாரம் (1861) 1892 சட்டத்திற்கு முந்தியது."},
        "C": {"en": "Correct. 2 (1861) -> 4 (1892) -> 3 (1909) -> 1 (1919) matches Crown Rule reform progression.", "ta": "சரி. 2 (1861) -> 4 (1892) -> 3 (1909) -> 1 (1919) முடி ஆட்சியின் சீர்திருத்த காலவரிசையைப் பின்பற்றுகிறது."},
        "D": {"en": "Incorrect. Dyarchy in provinces (1919) was after Separate Electorates (1909).", "ta": "தவறு. மாகாண இரட்டை ஆட்சி (1919) தனித் தொகுதிக்கு (1909) பின்னராகும்."}
    },
    "TNPSC Trap: The word 'election' was NOT explicitly used in the Act of 1892.",
    "TNPSC பொறி: 1892 சட்டத்தில் 'தேர்தல்' என்ற சொல் வெளிப்படையாகக் குறிப்பிடப்படவில்லை.",
    "Lord Minto is known as the Father of Communal Electorate in India.",
    "பிரபு மிண்டோ இந்தியாவில் 'வகுப்புவாதத் தொகுதிகளின் தந்தை' என அழைக்கப்படுகிறார்.",
    ["Polity", "Historical Background", "Chronology", "Indian Councils Act"]
))

# Q4: Analytical
q_list.append(make_q(
    4, "Hard", "Chronology",
    "Arrange the following administrative and executive milestones in chronological order of their evolution:\n1. Creation of the Office of Secretary of State for India replacing Board of Control and Court of Directors\n2. Addition of a Fourth Member (Law Member) to the Governor-General's Executive Council\n3. Introduction of open competition system for selection of Indian Civil Servants\n4. Formal dual control division into Court of Directors (commercial) and Board of Control (political)",
    "பின்வரும் நிர்வாக மற்றும் தலைமை அதிகார மைல்கற்களை அவற்றின் வளர்ச்சிக்கு ஏற்ப சரியான காலவரிசையில் அமைக்கவும்:\n1. கட்டுப்பாட்டு வாரியம் மற்றும் இயக்குநர்கள் அவைக்குப் பதிலாக இந்திய அரசுச் செயலர் அலுவலகத்தை உருவாக்குதல்\n2. கவர்னர்-ஜெனரலின் நிர்வாகக் குழுவில் நான்காவது உறுப்பினராக (சட்ட உறுப்பினர்) ஒருவரைச் சேர்த்தல்\n3. இந்திய சிவில் சர்வீஸ் தேர்வுக்கு திறந்தவெளி போட்டித் தேர்வு முறையை அறிமுகப்படுத்துதல்\n4. இயக்குநர்கள் அவை (வணிகம்) மற்றும் கட்டுப்பாட்டு வாரியம் (அரசியல்) என அதிகாரத்தை முறைப்படி இரட்டையாகப் பிரித்தல்",
    [("A", "4 -> 3 -> 2 -> 1", "4 -> 3 -> 2 -> 1"), ("B", "2 -> 4 -> 3 -> 1", "2 -> 4 -> 3 -> 1"), ("C", "4 -> 2 -> 1 -> 3", "4 -> 2 -> 1 -> 3"), ("D", "4 -> 2 -> 3 -> 1", "4 -> 2 -> 3 -> 1")],
    "D",
    "Sequence: 4 (1784 Pitt's India Act) -> 2 (1833 Charter Act) -> 3 (1853 Charter Act) -> 1 (1858 GOI Act). Shows institutional evolution.",
    "வரிசை: 4 (1784 பிட் இந்தியச் சட்டம்) -> 2 (1833 சாசனச் சட்டம்) -> 3 (1853 சாசனச் சட்டம்) -> 1 (1858 இந்திய அரசுச் சட்டம்). நிறுவன வளர்ச்சியை இது விளக்குகிறது.",
    {
        "A": {"en": "Incorrect. Law member was added in 1833 (2), before open competition in 1853 (3).", "ta": "தவறு. சட்ட உறுப்பினர் 1833-ல் சேர்க்கப்பட்டார் (2), இது 1853 போட்டித் தேர்வுக்கு (3) முந்தியது."},
        "B": {"en": "Incorrect. Dual Control was introduced in 1784 (4), before 1833 Act.", "ta": "தவறு. இரட்டைக் கட்டுப்பாடு 1784-ல் அறிமுகமானது (4), இது 1833 சட்டத்திற்கு முந்தியது."},
        "C": {"en": "Incorrect. Open competition was 1853 (3), while Secretary of State was created in 1858 (1).", "ta": "தவறு. போட்டித் தேர்வு 1853 (3), ஆனால் அரசுச் செயலர் உருவாக்கப்பட்டது 1858 (1)."},
        "D": {"en": "Correct. 4 (1784) -> 2 (1833) -> 3 (1853) -> 1 (1858) accurately reflects executive evolution.", "ta": "சரி. 4 (1784) -> 2 (1833) -> 3 (1853) -> 1 (1858) சரியான நிர்வாக மாற்றங்களை வரிசைப்படுத்துகிறது."}
    },
    "TNPSC Trap: Lord Macaulay was appointed as the 1st Law Member under 1833 Act, but initially had no executive vote.",
    "TNPSC பொறி: லார்டு மெக்காலே 1833 சட்டத்தில் 1வது சட்ட உறுப்பினராக சேர்க்கப்பட்டார், ஆனால் தொடக்கத்தில் அவருக்கு நிர்வாக வாக்களிக்கும் உரிமை இல்லை.",
    "The Secretary of State for India was assisted by a 15-member advisory body called Council of India.",
    "இந்திய அரசுச் செயலருக்கு உதவ 15 உறுப்பினர்களைக் கொண்ட 'இந்தியக் குழு' செயல்பட்டது.",
    ["Polity", "Historical Background", "Chronology", "Executive Council"]
))

# Q5: Analytical
q_list.append(make_q(
    5, "Hard", "Chronology",
    "Arrange the following legislative council financial and structural privileges in order of their constitutional grant:\n1. Grant of Provincial Autonomy and establishment of a tri-partite legislative distribution (Federal, Provincial, Concurrent lists)\n2. Right of legislative members to discuss the budget without power to vote or move resolutions\n3. Establishment of a bicameral legislature at the Centre with Council of State and Legislative Assembly\n4. Right of legislative members to ask supplementary questions and move resolutions on the budget",
    "சட்ட மேலவைகளின் நிதி மற்றும் கட்டமைப்பு சலுகைகள் வழங்கப்பட்டதன் அடிப்படையில் அவற்றை சரியான காலவரிசையில் அமைக்கவும்:\n1. மாகாண தன்னாட்சி வழங்குதல் மற்றும் மூன்று அடுக்கு சட்டப் பட்டியல்கள் (கூட்டாட்சி, மாகாண, பொதுப் பட்டியல்கள்) உருவாக்குதல்\n2. வாக்களிக்கும் அல்லது தீர்மானம் கொண்டுவரும் அதிகாரமின்றி வரவு செலவுத் திட்டத்தை (பட்ஜெட்) விவாதிக்க உறுப்பினர்களுக்கு உரிமை அளித்தல்\n3. மத்திய சட்டமன்றத்தில் மாநிலங்கள் அவை மற்றும் சட்டப் பேரவை கொண்ட இரு அவை முறையை உருவாக்குதல்\n4. பட்ஜெட் மீது துணைக் கேள்விகள் கேட்கவும் தீர்மானங்கள் கொண்டுவரவும் உறுப்பினர்களுக்கு உரிமை அளித்தல்",
    [("A", "2 -> 4 -> 3 -> 1", "2 -> 4 -> 3 -> 1"), ("B", "4 -> 2 -> 3 -> 1", "4 -> 2 -> 3 -> 1"), ("C", "2 -> 3 -> 4 -> 1", "2 -> 3 -> 4 -> 1"), ("D", "2 -> 4 -> 1 -> 3", "2 -> 4 -> 1 -> 3")],
    "A",
    "Sequence: 2 (1892 Act) -> 4 (1909 Act) -> 3 (1919 Act) -> 1 (1935 Act). Demonstrates legislative empowerment.",
    "வரிசை: 2 (1892 சட்டம்) -> 4 (1909 சட்டம்) -> 3 (1919 சட்டம்) -> 1 (1935 சட்டம்). சட்டமன்ற அதிகாரங்களின் வளர்ச்சியை இது காட்டுகிறது.",
    {
        "A": {"en": "Correct. 2 (1892) -> 4 (1909) -> 3 (1919) -> 1 (1935) follows exact legislative privilege growth.", "ta": "சரி. 2 (1892) -> 4 (1909) -> 3 (1919) -> 1 (1935) சட்டமன்ற உரிமைகளின் வளர்ச்சியைத் துல்லியமாகப் பின்பற்றுகிறது."},
        "B": {"en": "Incorrect. Budget discussion (1892) preceded supplementary questions (1909).", "ta": "தவறு. பட்ஜெட் விவாதம் (1892) துணைக் கேள்விகளுக்கு (1909) முந்தியது."},
        "C": {"en": "Incorrect. Central bicameralism (1919) was after supplementary questions (1909).", "ta": "தவறு. மத்திய இரு அவை முறை (1919) துணைக் கேள்விகளுக்குப் (1909) பின்னரே வந்தது."},
        "D": {"en": "Incorrect. Provincial Autonomy (1935) came after 1919 central bicameralism.", "ta": "தவறு. மாகாண தன்னாட்சி (1935) 1919 மத்திய இரு அவை முறைக்குப் பின்னரே வந்தது."}
    },
    "TNPSC Trap: Supplementary questions were allowed in 1909, whereas initial budget discussion was in 1892.",
    "TNPSC பொறி: துணைக் கேள்விகள் 1909-ல் அனுமதிக்கப்பட்டன; ஆனால் ஆரம்ப பட்ஜெட் விவாதம் 1892-ல் அனுமதிக்கப்பட்டது.",
    "GOI Act 1919 separated provincial budgets from central budget for the first time.",
    "1919 இந்திய அரசுச் சட்டம் முதன்முறையாக மாகாண வரவு செலவுத் திட்டத்தை மத்திய வரவு செலவுத் திட்டத்திலிருந்து பிரித்தது.",
    ["Polity", "Historical Background", "Chronology", "Budget Powers"]
))

# Q6: Analytical
q_list.append(make_q(
    6, "Hard", "Chronology",
    "Arrange the establishment of the following judicial bodies in British India and Independent India in correct chronological order:\n1. Inauguration of the Supreme Court of India under the Constitution of India\n2. Establishment of the Federal Court of India at Delhi\n3. Establishment of High Courts at Calcutta, Bombay, and Madras\n4. Establishment of the Supreme Court of Judicature at Fort William, Calcutta",
    "பிரிட்டிஷ் இந்தியா மற்றும் சுதந்திர இந்தியாவில் பின்வரும் நீதித்துறை அமைப்புகள் நிறுவப்பட்டதை சரியான காலவரிசையில் அமைக்கவும்:\n1. இந்திய அரசியலமைப்பின் கீழ் இந்திய உச்ச நீதிமன்றத்தை முறைப்படி தொடங்குதல்\n2. டெல்லியில் இந்தியாவின் கூட்டாட்சி நீதிமன்றத்தை (Federal Court) அமைத்தல்\n3. கொல்கத்தா, பம்பாய் மற்றும் மதராஸில் உயர் நீதிமன்றங்களை அமைத்தல்\n4. கொல்கத்தா வில்லியம் கோட்டையில் உச்ச நீதிமன்றத்தை அமைத்தல்",
    [("A", "4 -> 2 -> 3 -> 1", "4 -> 2 -> 3 -> 1"), ("B", "4 -> 3 -> 2 -> 1", "4 -> 3 -> 2 -> 1"), ("C", "3 -> 4 -> 2 -> 1", "3 -> 4 -> 2 -> 1"), ("D", "4 -> 3 -> 1 -> 2", "4 -> 3 -> 1 -> 2")],
    "B",
    "Sequence: 4 (1774 Fort William SC) -> 3 (1862 High Courts) -> 2 (1937 Federal Court) -> 1 (1950 Supreme Court of India). Shows judicial integration trajectory.",
    "வரிசை: 4 (1774 வில்லியம் கோட்டை உச்ச நீதிமன்றம்) -> 3 (1862 உயர் நீதிமன்றங்கள்) -> 2 (1937 கூட்டாட்சி நீதிமன்றம்) -> 1 (1950 இந்திய உச்ச நீதிமன்றம்). நீதித்துறை ஒருங்கிணைப்பை இது விளக்குகிறது.",
    {
        "A": {"en": "Incorrect. High Courts (1862) were established before Federal Court (1937).", "ta": "தவறு. உயர் நீதிமன்றங்கள் (1862) கூட்டாட்சி நீதிமன்றத்திற்கு (1937) முன்பே அமைக்கப்பட்டன."},
        "B": {"en": "Correct. 4 (1774) -> 3 (1862) -> 2 (1937) -> 1 (1950) perfectly matches judicial history.", "ta": "சரி. 4 (1774) -> 3 (1862) -> 2 (1937) -> 1 (1950) நீதித்துறை வரலாற்றைத் துல்லியமாகப் பிரதிபலிக்கிறது."},
        "C": {"en": "Incorrect. Fort William Supreme Court (1774) was long before High Courts (1862).", "ta": "தவறு. வில்லியம் கோட்டை உச்ச நீதிமன்றம் (1774) உயர் நீதிமன்றங்களுக்கு (1862) முந்தியது."},
        "D": {"en": "Incorrect. Supreme Court of India (1950) was after Federal Court (1937).", "ta": "தவறு. இந்திய உச்ச நீதிமன்றம் (1950) கூட்டாட்சி நீதிமன்றத்திற்குப் (1937) பின்னரே தொடங்கப்பட்டது."}
    },
    "TNPSC Trap: High Courts of Calcutta, Bombay, and Madras were established in 1862 under the Indian High Courts Act 1861.",
    "TNPSC பொறி: கொல்கத்தா, பம்பாய் மற்றும் மதராஸ் உயர் நீதிமன்றங்கள் 1861 சட்டத்தின் கீழ் 1862-ல் அமைக்கப்பட்டன.",
    "The Federal Court established in 1937 functioned until the Supreme Court of India was inaugurated on Jan 28, 1950.",
    "1937-ல் அமைக்கப்பட்ட கூட்டாட்சி நீதிமன்றம் ஜனவரி 28, 1950-ல் இந்திய உச்ச நீதிமன்றம் தொடங்கப்படும் வரை செயல்பட்டது.",
    ["Polity", "Historical Background", "Chronology", "Judiciary"]
))

# Q7: Analytical
q_list.append(make_q(
    7, "Hard", "Chronology",
    "Arrange the following Civil Services Commissions and Reform Committees in British India in correct chronological sequence:\n1. Royal Commission on Superior Civil Services in India (Lee Commission)\n2. Committee on the Indian Civil Service (Macaulay Committee)\n3. Royal Commission on Public Services in India (Islington Commission)\n4. Public Service Commission under Sir Charles Aitchison (Aitchison Commission)",
    "பிரிட்டிஷ் இந்தியாவில் சிவில் சர்வீசஸ் கமிஷன்கள் மற்றும் சீர்திருத்தக் குழுக்கள் அமைக்கப்பட்டதை சரியான காலவரிசையில் அமைக்கவும்:\n1. இந்தியாவில் மேலதிக சிவில் சர்வீசஸ்க்கான அரச ஆணையம் (லீ ஆணையம்)\n2. இந்திய சிவில் சர்வீஸ் குழு (மெக்காலே குழு)\n3. இந்தியாவில் பொதுச் சேவைகளுக்கான அரச ஆணையம் (இஸ்லிங்டன் ஆணையம்)\n4. சர் சார்லஸ் அட்சிகன் தலைமையிலான பொதுச் சேவை ஆணையம் (அட்சிகன் ஆணையம்)",
    [("A", "2 -> 1 -> 4 -> 3", "2 -> 1 -> 4 -> 3"), ("B", "4 -> 2 -> 3 -> 1", "4 -> 2 -> 3 -> 1"), ("C", "2 -> 4 -> 3 -> 1", "2 -> 4 -> 3 -> 1"), ("D", "2 -> 4 -> 1 -> 3", "2 -> 4 -> 1 -> 3")],
    "C",
    "Sequence: 2 (1854 Macaulay) -> 4 (1886 Aitchison) -> 3 (1912 Islington) -> 1 (1923 Lee). Demonstrates bureaucratic reform evolution.",
    "வரிசை: 2 (1854 மெக்காலே) -> 4 (1886 அட்சிகன்) -> 3 (1912 இஸ்லிங்டன்) -> 1 (1923 லீ). நிர்வாகச் சீர்திருத்த வளர்ச்சியை இது விளக்குகிறது.",
    {
        "A": {"en": "Incorrect. Lee Commission (1923) was appointed after Aitchison Commission (1886).", "ta": "தவறு. லீ ஆணையம் (1923) அட்சிகன் ஆணையத்திற்குப் (1886) பின்னரே நியமிக்கப்பட்டது."},
        "B": {"en": "Incorrect. Macaulay Committee (1854) was the earliest among civil service committees.", "ta": "தவறு. சிவில் சர்வீஸ் குழுக்களில் மெக்காலே குழுவே (1854) மிகவும் பழமையானது."},
        "C": {"en": "Correct. 2 (1854) -> 4 (1886) -> 3 (1912) -> 1 (1923) follows exact civil service history.", "ta": "சரி. 2 (1854) -> 4 (1886) -> 3 (1912) -> 1 (1923) சிவில் சர்வீஸ் வரலாற்றைத் துல்லியமாகப் பின்பற்றுகிறது."},
        "D": {"en": "Incorrect. Islington Commission (1912) preceded Lee Commission (1923).", "ta": "தவறு. இஸ்லிங்டன் ஆணையம் (1912) லீ ஆணையத்திற்கு (1923) முந்தியது."}
    },
    "TNPSC Trap: Aitchison Commission (1886) classified civil services into Imperial, Provincial, and Subordinate services.",
    "TNPSC பொறி: அட்சிகன் ஆணையம் (1886) சிவில் சர்வீசஸ்களை இம்பீரியல், மாகாண மற்றும் கீழ்நிலை சேவைகள் எனப் பிரித்தது.",
    "Lee Commission (1923) led directly to setting up Central Public Service Commission in 1926.",
    "லீ ஆணையத்தின் (1923) பரிந்துரையால் 1926-ல் மத்திய பொதுச் சேவை ஆணையம் அமைக்கப்பட்டது.",
    ["Polity", "Historical Background", "Chronology", "Civil Services"]
))

# Q8: Analytical
q_list.append(make_q(
    8, "Hard", "Chronology",
    "Arrange the following administrative decentralization and local self-government milestones in chronological order:\n1. Transfer of Local Self-Government to the administrative control of elected Indian Ministers (Transferred Subject)\n2. Lord Ripon's Resolution on Local Self-Government (Magna Carta of Local Self-Government)\n3. Appointment of the Royal Commission on Decentralization (Hobhouse Commission)\n4. Lord Mayo's Resolution on Financial Decentralization granting fixed grants to provinces",
    "பின்வரும் நிர்வாகப் பரவலாக்கம் மற்றும் உள்ளாட்சி சுயஅரசு மைல்கற்களை காலவரிசையில் அமைக்கவும்:\n1. உள்ளாட்சி சுயஅரசை தேர்ந்தெடுக்கப்பட்ட இந்திய அமைச்சர்களின் நிர்வாகக் கட்டுப்பாட்டிற்கு மாற்றுதல் (மாற்றப்பட்ட துறை)\n2. லார்டு ரிப்பனின் உள்ளாட்சி சுயஅரசு தீர்மானம் (உள்ளாட்சி சுயஅரசின் மகாசாசனம்)\n3. பரவலாக்கத்திற்கான அரச ஆணையம் அமைத்தல் (ஹாப்ஹவுஸ் ஆணையம்)\n4. மாகாணங்களுக்கு நிலையான மானியங்களை வழங்கி நிதிப் பரவலாக்கம் செய்த லார்டு மேயோவின் தீர்மானம்",
    [("A", "4 -> 3 -> 2 -> 1", "4 -> 3 -> 2 -> 1"), ("B", "2 -> 4 -> 3 -> 1", "2 -> 4 -> 3 -> 1"), ("C", "4 -> 2 -> 1 -> 3", "4 -> 2 -> 1 -> 3"), ("D", "4 -> 2 -> 3 -> 1", "4 -> 2 -> 3 -> 1")],
    "D",
    "Sequence: 4 (1870 Mayo Resolution) -> 2 (1882 Ripon Resolution) -> 3 (1907 Hobhouse Commission) -> 1 (1919 Dyarchy Transfer). Local government evolution.",
    "வரிசை: 4 (1870 மேயோ தீர்மானம்) -> 2 (1882 ரிப்பன் தீர்மானம்) -> 3 (1907 ஹாப்ஹவுஸ் ஆணையம்) -> 1 (1919 இரட்டை ஆட்சி மாற்றம்). உள்ளாட்சி வளர்ச்சி.",
    {
        "A": {"en": "Incorrect. Ripon Resolution (1882) was before Hobhouse Commission (1907).", "ta": "தவறு. ரிப்பன் தீர்மானம் (1882) ஹாப்ஹவுஸ் ஆணையத்திற்கு (1907) முந்தியது."},
        "B": {"en": "Incorrect. Mayo Resolution (1870) was before Ripon Resolution (1882).", "ta": "தவறு. மேயோ தீர்மானம் (1870) ரிப்பன் தீர்மானத்திற்கு (1882) முந்தியது."},
        "C": {"en": "Incorrect. Hobhouse Commission (1907) came before GOI Act 1919.", "ta": "தவறு. ஹாப்ஹவுஸ் ஆணையம் (1907) 1919 சட்டத்திற்கு முன்பே வந்தது."},
        "D": {"en": "Correct. 4 (1870) -> 2 (1882) -> 3 (1907) -> 1 (1919) matches local self-government progress.", "ta": "சரி. 4 (1870) -> 2 (1882) -> 3 (1907) -> 1 (1919) உள்ளாட்சி வளர்ச்சியைக் காட்டுகிறது."}
    },
    "TNPSC Trap: Lord Ripon is Father of Local Self-Government; Lord Mayo introduced financial decentralization.",
    "TNPSC பொறி: லார்டு ரிப்பன் 'உள்ளாட்சி அமைப்புகளின் தந்தை'; லார்டு மேயோ நிதிப் பரவலாக்கத்தை அறிமுகப்படுத்தினார்.",
    "Local Self-Government became a Transferred Subject under Dyarchy in GOI Act 1919.",
    "1919 இந்திய அரசுச் சட்டத்தின் கீழ் உள்ளாட்சி சுயஅரசு மாற்றப்பட்ட துறையாக ஆக்கப்பட்டது.",
    ["Polity", "Historical Background", "Chronology", "Local Self Government"]
))

# Q9: Analytical
q_list.append(make_q(
    9, "Hard", "Chronology",
    "Arrange the following phases of legislative centralization and decentralization in India in correct chronological sequence:\n1. Total centralized legislative authority vested in Governor-General of India, depriving Bombay and Madras of legislative powers\n2. Reversal of centralization policy by restoring legislative powers to Bombay and Madras Presidencies\n3. Initial subordination of Bombay and Madras Presidencies to Governor-General of Bengal in matters of war and peace\n4. Complete grant of Provincial Autonomy with full executive responsibility to provincial ministers",
    "இந்தியாவில் சட்டமியற்றும் அதிகார மையமாக்கல் மற்றும் அதிகாரப் பரவலாக்கத்தின் பின்வரும் கட்டங்களை சரியான காலவரிசையில் அமைக்கவும்:\n1. பம்பாய் மற்றும் மதராஸின் சட்ட அதிகாரங்களைப் பறித்து, இந்தியாவின் கவர்னர்-ஜெனரலிடம் சட்ட அதிகாரத்தை முழுமையாக மையப்படுத்துதல்\n2. பம்பாய் மற்றும் மதராஸ் மாகாணங்களுக்கு சட்ட அதிகாரங்களை மீட்டளித்து அதிகார மையமாக்கலைத் திரும்பப் பெறுதல்\n3. போர் மற்றும் அமைதி விவகாரங்களில் பம்பாய் மற்றும் மதராஸ் மாகாணங்களை வங்காள கவர்னர்-ஜெனரலுக்குத் தொடக்கத்தில் கீழ்ப்படுத்துதல்\n4. மாகாண அமைச்சர்களுக்கு முழு நிர்வாகப் பொறுப்புடன் கூடிய முழுமையான மாகாண தன்னாட்சி வழங்குதல்",
    [("A", "3 -> 1 -> 2 -> 4", "3 -> 1 -> 2 -> 4"), ("B", "1 -> 3 -> 2 -> 4", "1 -> 3 -> 2 -> 4"), ("C", "3 -> 2 -> 1 -> 4", "3 -> 2 -> 1 -> 4"), ("D", "3 -> 1 -> 4 -> 2", "3 -> 1 -> 4 -> 2")],
    "A",
    "Sequence: 3 (1773 Regulating Act) -> 1 (1833 Charter Act) -> 2 (1861 Indian Councils Act) -> 4 (1935 GOI Act). Centralization to decentralization pendulum.",
    "வரிசை: 3 (1773 ஒழுங்குமுறைச் சட்டம்) -> 1 (1833 சாசனச் சட்டம்) -> 2 (1861 இந்தியக் கவுன்சில்கள் சட்டம்) -> 4 (1935 இந்திய அரசுச் சட்டம்).",
    {
        "A": {"en": "Correct. 3 (1773) -> 1 (1833) -> 2 (1861) -> 4 (1935) tracks central vs provincial power shifts.", "ta": "சரி. 3 (1773) -> 1 (1833) -> 2 (1861) -> 4 (1935) மத்திய-மாகாண அதிகார மாற்றங்களைத் துல்லியமாகக் காட்டுகிறது."},
        "B": {"en": "Incorrect. Subordination of presidencies (1773) was prior to 1833 Act.", "ta": "தவறு. மாகாணங்கள் கீழ்ப்படுத்தப்படுதல் (1773) 1833 சட்டத்திற்கு முந்தியது."},
        "C": {"en": "Incorrect. Restoration of powers (1861) was after total centralization in 1833.", "ta": "தவறு. அதிகார மீட்பு (1861) 1833 முழு மையமாக்கலுக்குப் பின்னராகும்."},
        "D": {"en": "Incorrect. Restoration of powers (1861) preceded Provincial Autonomy (1935).", "ta": "தவறு. அதிகார மீட்பு (1861) 1935 மாகாண தன்னாட்சிக்கு முந்தியது."}
    },
    "TNPSC Trap: 1833 Act was the climax of centralization; 1861 Act marked the start of decentralization.",
    "TNPSC பொறி: 1833 சட்டம் மையமாக்கலின் உச்சம்; 1861 சட்டம் அதிகாரப் பரவலாக்கத்தின் தொடக்கம்.",
    "Provincial Autonomy introduced by GOI Act 1935 came into force in 1937.",
    "1935 இந்திய அரசுச் சட்டம் அறிமுகப்படுத்திய மாகாண தன்னாட்சி 1937-ல் அமலுக்கு வந்தது.",
    ["Polity", "Historical Background", "Chronology", "Decentralization"]
))

# Q10: Analytical
q_list.append(make_q(
    10, "Hard", "Chronology",
    "Arrange the following major political events and committee recommendations leading to the Government of India Act 1935 in correct chronological order:\n1. Publication of the Nehru Report proposing a Dominion Status Constitution for India\n2. Submission of the Simon Commission Report recommending abolition of Dyarchy\n3. Publication of the British Government's 'White Paper on Constitutional Reforms'\n4. Convening of the First Round Table Conference in London",
    "1935 இந்திய அரசுச் சட்டத்திற்கு வழிகோலிய பின்வரும் முக்கிய அரசியல் நிகழ்வுகள் மற்றும் குழு பரிந்துரைகளை சரியான காலவரிசையில் அமைக்கவும்:\n1. இந்தியாவுக்கு டொமினியன் அந்தஸ்து அரசியலமைப்பை முன்மொழிந்த நேரு அறிக்கை வெளியிடப்படல்\n2. இரட்டை ஆட்சியை நீக்கப் பரிந்துரைத்து சைமன் குழு அறிக்கை சமர்ப்பிக்கப்படல்\n3. பிரிட்டிஷ் அரசாங்கத்தின் 'அரசியலமைப்பு சீர்திருத்தங்கள் பற்றிய வெள்ளை அறிக்கை' வெளியிடப்படல்\n4. லண்டனில் முதலாவது வட்டமேஜை மாநாடு கூட்டப்படல்",
    [("A", "1 -> 4 -> 2 -> 3", "1 -> 4 -> 2 -> 3"), ("B", "1 -> 2 -> 4 -> 3", "1 -> 2 -> 4 -> 3"), ("C", "2 -> 1 -> 4 -> 3", "2 -> 1 -> 4 -> 3"), ("D", "1 -> 2 -> 3 -> 4", "1 -> 2 -> 3 -> 4")],
    "B",
    "Sequence: 1 (Nehru Report Aug 1928) -> 2 (Simon Report May 1930) -> 4 (1st RTC Nov 1930) -> 3 (White Paper Mar 1933). Road to 1935 Act.",
    "வரிசை: 1 (நேரு அறிக்கை ஆக 1928) -> 2 (சைமன் அறிக்கை மே 1930) -> 4 (1வது RTC நவ 1930) -> 3 (வெள்ளை அறிக்கை மார்ச் 1933).",
    {
        "A": {"en": "Incorrect. Simon Commission Report (May 1930) was submitted before 1st RTC (Nov 1930).", "ta": "தவறு. சைமன் குழு அறிக்கை (மே 1930) 1வது வட்டமேஜை மாநாட்டிற்கு (நவ 1930) முந்தியது."},
        "B": {"en": "Correct. 1 (Aug 1928) -> 2 (May 1930) -> 4 (Nov 1930) -> 3 (Mar 1933) accurately matches history.", "ta": "சரி. 1 (ஆக 1928) -> 2 (மே 1930) -> 4 (நவ 1930) -> 3 (மார்ச் 1933) வரலாற்று நாட்காட்டியைப் பின்பற்றுகிறது."},
        "C": {"en": "Incorrect. Nehru Report was published in 1928, before Simon Report in 1930.", "ta": "தவறு. நேரு அறிக்கை 1928-ல் வெளியிடப்பட்டது, இது சைமன் அறிக்கைக்கு (1930) முந்தியது."},
        "D": {"en": "Incorrect. White Paper (1933) was published after Round Table Conferences.", "ta": "தவறு. வெள்ளை அறிக்கை (1933) வட்டமேஜை மாநாடுகளுக்குப் பிறகே வந்தது."}
    },
    "TNPSC Trap: Nehru Report was drafted in 1928 as a response to Birkenhead's challenge.",
    "TNPSC பொறி: லார்டு பர்க்கன்ஹெட்டின் சவாலை ஏற்று 1928-ல் நேரு அறிக்கை தயாரிக்கப்பட்டது.",
    "The White Paper of 1933 led to Joint Select Committee recommendations forming the GOI Act 1935.",
    "1933 வெள்ளை அறிக்கை நாடாளுமன்றக் கூட்டுத் தேர்வுக் குழுவின் ஆலோசனைகள் வழியாக 1935 சட்டமாக உருவானது.",
    ["Polity", "Historical Background", "Chronology", "1935 Act Background"]
))

# Q11: Conceptual
q_list.append(make_q(
    11, "Hard", "Chronology",
    "Arrange the following events and committees related to Dyarchy and constitutional review in correct chronological sequence:\n1. Appointment of the Reforms Enquiry Committee (Muddiman Committee) to examine Dyarchy\n2. Announcement of the Montagu-Chelmsford Report proposing Dyarchy in provinces\n3. Appointment of the Statutory Commission (Simon Commission) under Sir John Simon\n4. Enactment of the Government of India Act 1919 establishing Dyarchy",
    "இரட்டை ஆட்சி மற்றும் அரசியலமைப்பு மறுஆய்வு தொடர்பான பின்வரும் நிகழ்வுகள் மற்றும் குழுக்களை சரியான காலவரிசையில் அமைக்கவும்:\n1. இரட்டை ஆட்சியை ஆராய சீர்திருத்தங்கள் விசாரணை குழு (முடிமேன் குழு) அமைத்தல்\n2. மாகாணங்களில் இரட்டை ஆட்சியை முன்மொழிந்த மாண்டேகு-செம்ஸ்ஃபோர்டு அறிக்கை அறிவிப்பு\n3. சர் ஜான் சைமன் தலைமையில் சட்டப்பூர்வ ஆணையம் (சைமன் குழு) அமைத்தல்\n4. இரட்டை ஆட்சியை நிறுவிய 1919 இந்திய அரசுச் சட்டம் இயற்றப்படல்",
    [("A", "2 -> 1 -> 4 -> 3", "2 -> 1 -> 4 -> 3"), ("B", "4 -> 2 -> 1 -> 3", "4 -> 2 -> 1 -> 3"), ("C", "2 -> 4 -> 1 -> 3", "2 -> 4 -> 1 -> 3"), ("D", "2 -> 4 -> 3 -> 1", "2 -> 4 -> 3 -> 1")],
    "C",
    "Sequence: 2 (Montagu-Chelmsford Report 1918) -> 4 (GOI Act 1919) -> 1 (Muddiman Committee 1924) -> 3 (Simon Commission 1927). Traces review mechanisms.",
    "வரிசை: 2 (மாண்டேகு அறிக்கை 1918) -> 4 (1919 சட்டம்) -> 1 (முடிமேன் குழு 1924) -> 3 (சைமன் குழு 1927).",
    {
        "A": {"en": "Incorrect. Muddiman Committee (1924) was formed after the GOI Act 1919 (1919).", "ta": "தவறு. முடிமேன் குழு (1924) 1919 இந்திய அரசுச் சட்டத்திற்குப் பிறகே அமைந்தது."},
        "B": {"en": "Incorrect. Montagu-Chelmsford Report (1918) came before the enactment of 1919 Act.", "ta": "தவறு. மாண்டேகு-செம்ஸ்ஃபோர்டு அறிக்கை (1918) 1919 சட்டம் இயற்றப்படுவதற்கு முந்தியது."},
        "C": {"en": "Correct. 2 (1918) -> 4 (1919) -> 1 (1924) -> 3 (1927) perfectly follows Dyarchy evaluation history.", "ta": "சரி. 2 (1918) -> 4 (1919) -> 1 (1924) -> 3 (1927) இரட்டை ஆட்சி மதிப்பீட்டு வரலாற்றைப் பின்பற்றுகிறது."},
        "D": {"en": "Incorrect. Simon Commission (1927) was appointed after Muddiman Committee (1924).", "ta": "தவறு. சைமன் குழு (1927) முடிமேன் குழுவிற்கு (1924) பின்னரே அமைந்தது."}
    },
    "TNPSC Trap: Muddiman Committee was appointed in 1924 due to Swarajist pressure inside the assembly.",
    "TNPSC பொறி: சட்டமன்றத்திற்குள் சுயராஜ்யக் கட்சியினரின் நெருக்கடியால் 1924-ல் முடிமேன் குழு அமைக்கப்பட்டது.",
    "The 1919 Act provided for a statutory commission to be appointed 10 years after its enactment, but Simon Commission was appointed 2 years early (1927).",
    "10 ஆண்டுகளுக்குப் பின் சட்ட ஆணையம் அமைக்க 1919 சட்டம் வழிவகை செய்தது, ஆனால் சைமன் குழு 2 ஆண்டுகளுக்கு முன்பே (1927) அமைந்தது.",
    ["Polity", "Historical Background", "Chronology", "Simon Commission", "Dyarchy"]
))

# Q12: Conceptual
q_list.append(make_q(
    12, "Hard", "Chronology",
    "Arrange the following wartime constitutional proposals and missions in correct chronological order:\n1. Lord Linlithgow's August Offer offering Constituent Assembly after war\n2. Cripps Mission proposals headed by Sir Stafford Cripps\n3. Cabinet Mission Plan proposing Union of India and Constituent Assembly\n4. Wavell Plan presented at the Shimla Conference",
    "இரண்டாம் உலகப் போர்க் காலத்தில் கொண்டுவரப்பட்ட பின்வரும் அரசியலமைப்பு முன்மொழிவுகள் மற்றும் தூதுக்குழுக்களை சரியான காலவரிசையில் அமைக்கவும்:\n1. போருக்குப் பின் அரசியலமைப்பு நிர்ணய சபை அமைப்பதாக உறுதியளித்த லார்டு லின்லித்கோவின் ஆகஸ்ட் கொடை\n2. சர் ஸ்டாஃபோர்டு கிரிப்ஸ் தலைமையிலான கிரிப்ஸ் தூதுக்குழு முன்மொழிவுகள்\n3. இந்திய ஒன்றியம் மற்றும் அரசியலமைப்பு நிர்ணய சபையை முன்மொழிந்த கேபினட் தூதுக்குழு திட்டம்\n4. சிம்லா மாநாட்டில் முன்வைக்கப்பட்ட வேவல் திட்டம்",
    [("A", "1 -> 2 -> 3 -> 4", "1 -> 2 -> 3 -> 4"), ("B", "2 -> 1 -> 4 -> 3", "2 -> 1 -> 4 -> 3"), ("C", "1 -> 4 -> 2 -> 3", "1 -> 4 -> 2 -> 3"), ("D", "1 -> 2 -> 4 -> 3", "1 -> 2 -> 4 -> 3")],
    "D",
    "Sequence: 1 (August Offer Aug 1940) -> 2 (Cripps Mission Mar 1942) -> 4 (Wavell Plan/Shimla Conf June 1945) -> 3 (Cabinet Mission Mar 1946).",
    "வரிசை: 1 (ஆகஸ்ட் கொடை ஆக 1940) -> 2 (கிரிப்ஸ் தூதுக்குழு மார்ச் 1942) -> 4 (வேவல் திட்டம் ஜூன் 1945) -> 3 (கேபினட் தூதுக்குழு மார்ச் 1946).",
    {
        "A": {"en": "Incorrect. Wavell Plan (1945) came before Cabinet Mission Plan (1946).", "ta": "தவறு. வேவல் திட்டம் (1945) கேபினட் தூதுக்குழு திட்டத்திற்கு (1946) முந்தியது."},
        "B": {"en": "Incorrect. August Offer (1940) preceded Cripps Mission (1942).", "ta": "தவறு. ஆகஸ்ட் கொடை (1940) கிரிப்ஸ் தூதுக்குழுவிற்கு (1942) முந்தியது."},
        "C": {"en": "Incorrect. Cripps Mission (1942) was before Wavell Plan (1945).", "ta": "தவறு. கிரிப்ஸ் தூதுக்குழு (1942) வேவல் திட்டத்திற்கு (1945) முந்தியது."},
        "D": {"en": "Correct. 1 (1940) -> 2 (1942) -> 4 (1945) -> 3 (1946) accurately tracks wartime negotiations.", "ta": "சரி. 1 (1940) -> 2 (1942) -> 4 (1945) -> 3 (1946) போர் கால பேச்சுவார்த்தைகளைத் துல்லியமாகக் காட்டுகிறது."}
    },
    "TNPSC Trap: August Offer (1940) was the first official document recognizing Indians' right to frame their own constitution.",
    "TNPSC பொறி: இந்தியர்கள் தமக்கான அரசியலமைப்பை வகுக்கும் உரிமையை முதன்முதலில் அங்கீகரித்தது 1940 ஆகஸ்ட் கொடை ஆகும்.",
    "Cabinet Mission Plan rejected the demand for a full-fledged Pakistan and proposed a 3-tier grouping system.",
    "கேபினட் தூதுக்குழு தனி பாகிஸ்தான் கோரிக்கையை நிராகரித்து 3 அடுக்குக் குழு முறையை முன்மொழிந்தது.",
    ["Polity", "Historical Background", "Chronology", "Cabinet Mission", "Cripps Mission"]
))

# Q13: Conceptual
q_list.append(make_q(
    13, "Hard", "Chronology",
    "Arrange the creation/designation of the following top executive heads in India in chronological order:\n1. First Governor-General of Bengal under Regulating Act (Warren Hastings)\n2. First Governor-General of India under Charter Act (Lord William Bentinck)\n3. First Viceroy of India under Government of India Act (Lord Canning)\n4. First Governor-General of Independent India (Lord Mountbatten)",
    "இந்தியாவின் உயர்மட்ட நிர்வாகப் பொறுப்புகள் மற்றும் பதவிகள் உருவாக்கப்பட்டதை சரியான காலவரிசையில் அமைக்கவும்:\n1. ஒழுங்குமுறைச் சட்டத்தின் கீழ் வங்காளத்தின் முதல் கவர்னர்-ஜெனரல் (வாரன் ஹேஸ்டிங்ஸ்)\n2. சாசனச் சட்டத்தின் கீழ் இந்தியாவின் முதல் கவர்னர்-ஜெனரல் (லார்டு வில்லியம் பென்டிங்க்)\n3. இந்திய அரசுச் சட்டத்தின் கீழ் இந்தியாவின் முதல் வைஸ்ராய் (லார்டு கேனிங்)\n4. சுதந்திர இந்தியாவின் முதல் கவர்னர்-ஜெனரல் (லார்டு மவுண்ட்பேட்டன்)",
    [("A", "1 -> 2 -> 3 -> 4", "1 -> 2 -> 3 -> 4"), ("B", "2 -> 1 -> 3 -> 4", "2 -> 1 -> 3 -> 4"), ("C", "1 -> 3 -> 2 -> 4", "1 -> 3 -> 2 -> 4"), ("D", "1 -> 2 -> 4 -> 3", "1 -> 2 -> 4 -> 3")],
    "A",
    "Sequence: 1 (1773 GG of Bengal) -> 2 (1833 GG of India) -> 3 (1858 Viceroy of India) -> 4 (1947 GG of Independent India). Executive designation evolution.",
    "வரிசை: 1 (1773 வங்காள கவர்னர்-ஜெனரல்) -> 2 (1833 இந்திய கவர்னர்-ஜெனரல்) -> 3 (1858 இந்திய வைஸ்ராய்) -> 4 (1947 சுதந்திர இந்திய கவர்னர்-ஜெனரல்).",
    {
        "A": {"en": "Correct. 1 (1773) -> 2 (1833) -> 3 (1858) -> 4 (1947) perfectly matches top executive office transitions.", "ta": "சரி. 1 (1773) -> 2 (1833) -> 3 (1858) -> 4 (1947) உயர்மட்ட நிர்வாகப் பதவி மாற்றங்களைத் துல்லியமாகப் பின்பற்றுகிறது."},
        "B": {"en": "Incorrect. Governor-General of Bengal (1773) was created before Governor-General of India (1833).", "ta": "தவறு. வங்காள கவர்னர்-ஜெனரல் (1773) இந்திய கவர்னர்-ஜெனரலுக்கு (1833) முந்தியவர்."},
        "C": {"en": "Incorrect. Governor-General of India designation (1833) preceded Viceroy designation (1858).", "ta": "தவறு. இந்திய கவர்னர்-ஜெனரல் பதவி (1833) வைஸ்ராய் பதவிக்கு (1858) முந்தியது."},
        "D": {"en": "Incorrect. Viceroy designation (1858) was long before 1947 independence.", "ta": "தவறு. வைஸ்ராய் பதவி (1858) 1947 சுதந்திரத்திற்குப் பல ஆண்டுகள் முந்தியது."}
    },
    "TNPSC Trap: Lord Canning was both the last Governor-General of Company Rule and first Viceroy of Crown Rule.",
    "TNPSC பொறி: லார்டு கேனிங் கம்பெனி ஆட்சியின் கடைசி கவர்னர்-ஜெனரலாகவும் பிரிட்டிஷ் ஆட்சியின் முதல் வைஸ்ராயாகவும் இருந்தார்.",
    "C. Rajagopalachari was the first and last Indian Governor-General of Independent India (1948-1950).",
    "சி. ராஜகோபாலாச்சாரி சுதந்திர இந்தியாவின் முதல் மற்றும் கடைசி இந்திய கவர்னர்-ஜெனரலாக (1948-1950) இருந்தார்.",
    ["Polity", "Historical Background", "Chronology", "Governor General", "Viceroy"]
))

# Q14: Conceptual
q_list.append(make_q(
    14, "Hard", "Chronology",
    "Arrange the following executive council reform provisions associated with Viceroys/Governors-General in chronological order:\n1. Empowering Lord Cornwallis with overriding powers over Council in special cases\n2. Informal introduction of Portfolio System by Lord Dalhousie\n3. Grant of statutory recognition to Portfolio System under Lord Canning\n4. Association of Satyendra Prasanna Sinha with Viceroy's Executive Council as Law Member under Lord Minto",
    "கவர்னர்-ஜெனரல்கள் / வைஸ்ராய்களுடன் தொடர்புடைய பின்வரும் நிர்வாகக் குழு சீர்திருத்த விதிகளை காலவரிசையில் அமைக்கவும்:\n1. சிறப்பு நிகழ்வுகளில் கவுன்சிலின் முடிவை நிராகரிக்கும் அதிகாரத்தை லார்டு கார்ன்வாலிஸுக்கு வழங்குதல்\n2. லார்டு டல்ஹௌசியால் இலாகா முறை முறைசாரா முறையில் அறிமுகப்படுத்தப்படல்\n3. லார்டு கேனிங்கின் கீழ் இலாகா முறைக்கு சட்டப்பூர்வ அங்கீகாரம் வழங்கப்படல்\n4. லார்டு மிண்டோவின் கீழ் சத்யேந்திர பிரசன்னா சின்கா வைஸ்ராயின் நிர்வாகக் குழுவில் சட்ட உறுப்பினராகச் சேர்க்கப்படல்",
    [("A", "1 -> 3 -> 2 -> 4", "1 -> 3 -> 2 -> 4"), ("B", "1 -> 2 -> 3 -> 4", "1 -> 2 -> 3 -> 4"), ("C", "2 -> 1 -> 3 -> 4", "2 -> 1 -> 3 -> 4"), ("D", "1 -> 2 -> 4 -> 3", "1 -> 2 -> 4 -> 3")],
    "B",
    "Sequence: 1 (1786 Act for Cornwallis) -> 2 (1859 Dalhousie informal portfolio) -> 3 (1861 Canning statutory portfolio) -> 4 (1909 S.P. Sinha appointed).",
    "வரிசை: 1 (1786 கார்ன்வாலிஸ் சட்டம்) -> 2 (1859 டல்ஹௌசி முறைசாரா இலாகா) -> 3 (1861 கேனிங் சட்டப்பூர்வ இலாகா) -> 4 (1909 எஸ்.பி. சின்கா நியமனம்).",
    {
        "A": {"en": "Incorrect. Dalhousie's informal introduction (1859) came before Canning's statutory Act (1861).", "ta": "தவறு. டல்ஹௌசியின் முறைசாரா அறிமுகம் (1859) கேனிங்கின் சட்டத்திற்கு (1861) முந்தியது."},
        "B": {"en": "Correct. 1 (1786) -> 2 (1859) -> 3 (1861) -> 4 (1909) matches executive portfolio evolution.", "ta": "சரி. 1 (1786) -> 2 (1859) -> 3 (1861) -> 4 (1909) நிர்வாக இலாகா முறையின் வளர்ச்சியைப் பின்பற்றுகிறது."},
        "C": {"en": "Incorrect. Cornwallis overriding powers Act (1786) preceded Dalhousie (1859).", "ta": "தவறு. கார்ன்வாலிஸ் நிராகரிப்பு அதிகாரச் சட்டம் (1786) டல்ஹௌசிக்கு (1859) முந்தியது."},
        "D": {"en": "Incorrect. S.P. Sinha was appointed in 1909 (4), after 1861 statutory portfolio recognition (3).", "ta": "தவறு. எஸ்.பி. சின்கா 1909-ல் நியமிக்கப்பட்டார் (4), இது 1861 சட்டத்திற்குப் பின்னராகும்."}
    },
    "TNPSC Trap: Portfolio system was introduced informally by Lord Dalhousie in 1859 but got statutory status under Indian Councils Act 1861.",
    "TNPSC பொறி: இலாகா முறை 1859-ல் டல்ஹௌசியால் முறைசாரா அறிமுகமானது; 1861 சட்டத்தில் தான் சட்டப்பூர்வ அந்தஸ்து பெற்றது.",
    "S.P. Sinha was the first Indian to join the Viceroy's Executive Council.",
    "சத்யேந்திர பிரசன்னா சின்கா வைஸ்ராயின் நிர்வாகக் குழுவில் இணைந்த முதல் இந்தியராவார்.",
    ["Polity", "Historical Background", "Chronology", "Portfolio System", "Viceroy Council"]
))

# Q15: Conceptual
q_list.append(make_q(
    15, "Hard", "Chronology",
    "Arrange the progressive Indianization of imperial executive governance in correct chronological sequence:\n1. Appointment of K.G. Gupta and Syed Hussain Bilgrami to the Council of Secretary of State in London\n2. Appointment of Satyendra Prasanna Sinha as first Indian member in Viceroy's Executive Council\n3. Statutory provision for 3 out of 6 members in Viceroy's Executive Council to be Indians\n4. Swearing-in of the Interim Government composed entirely of Indian members (except Viceroy)",
    "அரசு தலைமை நிர்வாக அமைப்பில் இந்தியர்கள் சேர்க்கப்பட்டதை (இந்தியமயமாக்கல்) சரியான காலவரிசையில் அமைக்கவும்:\n1. லண்டனில் உள்ள இந்திய அரசுச் செயலர் குழுவிற்கு கே.ஜி. குப்தா மற்றும் சையத் உசேன் பில்கிராமி நியமிக்கப்படல்\n2. வைஸ்ராயின் நிர்வாகக் குழுவின் முதல் இந்திய உறுப்பினராக சத்யேந்திர பிரசன்னா சின்கா நியமிக்கப்படல்\n3. வைஸ்ராயின் நிர்வாகக் குழுவில் 6 உறுப்பினர்களில் 3 பேர் இந்தியர்களாக இருக்க வேண்டும் என்ற சட்டப்பூர்வ விதி\n4. வைஸ்ராய் தவிர அனைத்து இந்திய உறுப்பினர்களையும் கொண்ட இடைக்கால அரசு பதவியேற்றல்",
    [("A", "2 -> 1 -> 3 -> 4", "2 -> 1 -> 3 -> 4"), ("B", "1 -> 2 -> 4 -> 3", "1 -> 2 -> 4 -> 3"), ("C", "1 -> 2 -> 3 -> 4", "1 -> 2 -> 3 -> 4"), ("D", "2 -> 3 -> 1 -> 4", "2 -> 3 -> 1 -> 4")],
    "C",
    "Sequence: 1 (1907 London appointments) -> 2 (1909 Viceroy Council Sinha) -> 3 (1919 GOI Act 3/6 Indians) -> 4 (Sept 1946 Interim Govt).",
    "வரிசை: 1 (1907 லண்டன் நியமனங்கள்) -> 2 (1909 வைஸ்ராய் குழு சின்கா) -> 3 (1919 சட்டம் 3/6 இந்தியர்கள்) -> 4 (செப் 1946 இடைக்கால அரசு).",
    {
        "A": {"en": "Incorrect. London Council appointments (1907) preceded Sinha's appointment in India (1909).", "ta": "தவறு. லண்டன் குழு நியமனங்கள் (1907) சின்காவின் இந்திய நியமனத்திற்கு (1909) முந்தியவை."},
        "B": {"en": "Incorrect. Provision for 3/6 Indians (1919) was before Interim Government (1946).", "ta": "தவறு. 3/6 இந்தியர்கள் விதி (1919) இடைக்கால அரசுக்கு (1946) முந்தியது."},
        "C": {"en": "Correct. 1 (1907) -> 2 (1909) -> 3 (1919) -> 4 (1946) tracks step-by-step executive Indianization.", "ta": "சரி. 1 (1907) -> 2 (1909) -> 3 (1919) -> 4 (1946) இந்தியமயமாக்கலின் படிகளைத் துல்லியமாகக் காட்டுகிறது."},
        "D": {"en": "Incorrect. Sinha (1909) was after London council appointments (1907).", "ta": "தவறு. சின்கா (1909) லண்டன் குழு நியமனங்களுக்குப் (1907) பின்னரே வந்தவர்."}
    },
    "TNPSC Trap: 1907 saw Indians in Council of Secretary of State in London; 1909 saw Indian in Viceroy's Executive Council in India.",
    "TNPSC பொறி: 1907-ல் லண்டன் அரசுச் செயலர் குழுவிலும், 1909-ல் இந்திய வைஸ்ராய் குழுவிலும் இந்தியர்கள் சேர்க்கப்பட்டனர்.",
    "The 3 Indian members under 1919 Act excluded Commander-in-Chief.",
    "1919 சட்டத்தின் கீழ் இருந்த 3 இந்திய உறுப்பினர்களில் தளபதி (Commander-in-Chief) சேர்க்கப்படவில்லை.",
    ["Polity", "Historical Background", "Chronology", "Indianization", "Interim Government"]
))

# Q16: Conceptual
q_list.append(make_q(
    16, "Hard", "Chronology",
    "Arrange the establishment of the following central administrative and legal bodies in chronological sequence:\n1. Establishment of the Supreme Court at Fort William, Calcutta\n2. Appointment of the First Law Commission under Lord Macaulay\n3. Creation of the Indian (Central) Legislative Council (mini-Parliament)\n4. Establishment of Presidency High Courts under Indian High Courts Act",
    "பின்வரும் மத்திய நிர்வாக மற்றும் சட்ட அமைப்புகள் நிறுவப்பட்டதை சரியான காலவரிசையில் அமைக்கவும்:\n1. கொல்கத்தா வில்லியம் கோட்டையில் உச்ச நீதிமன்றம் அமைத்தல்\n2. லார்டு மெக்காலே தலைமையில் முதல் சட்ட ஆணையம் அமைத்தல்\n3. இந்திய (மத்திய) சட்ட மேலவையை (சிறிய நாடாளுமன்றம்) உருவாக்குதல்\n4. இந்திய உயர் நீதிமன்றங்கள் சட்டத்தின் கீழ் மாகாண உயர் நீதிமன்றங்களை அமைத்தல்",
    [("A", "1 -> 3 -> 2 -> 4", "1 -> 3 -> 2 -> 4"), ("B", "2 -> 1 -> 3 -> 4", "2 -> 1 -> 3 -> 4"), ("C", "1 -> 2 -> 4 -> 3", "1 -> 2 -> 4 -> 3"), ("D", "1 -> 2 -> 3 -> 4", "1 -> 2 -> 3 -> 4")],
    "D",
    "Sequence: 1 (1774 Supreme Court) -> 2 (1835 1st Law Commission under 1833 Act) -> 3 (1853 Central Legislative Council) -> 4 (1862 High Courts).",
    "வரிசை: 1 (1774 உச்ச நீதிமன்றம்) -> 2 (1835 முதல் சட்ட ஆணையம்) -> 3 (1853 மத்திய சட்ட மேலவை) -> 4 (1862 உயர் நீதிமன்றங்கள்).",
    {
        "A": {"en": "Incorrect. First Law Commission (1835) was appointed before Central Legislative Council (1853).", "ta": "தவறு. முதல் சட்ட ஆணையம் (1835) மத்திய சட்ட மேலவைக்கு (1853) முன்பே அமைந்தது."},
        "B": {"en": "Incorrect. Fort William Supreme Court (1774) was before First Law Commission (1835).", "ta": "தவறு. வில்லியம் கோட்டை உச்ச நீதிமன்றம் (1774) முதல் சட்ட ஆணையத்திற்கு (1835) முந்தியது."},
        "C": {"en": "Incorrect. Central Legislative Council (1853) came before Presidency High Courts (1862).", "ta": "தவறு. மத்திய சட்ட மேலவை (1853) உயர் நீதிமன்றங்களுக்கு (1862) முந்தியது."},
        "D": {"en": "Correct. 1 (1774) -> 2 (1835) -> 3 (1853) -> 4 (1862) matches institutional creation chronology.", "ta": "சரி. 1 (1774) -> 2 (1835) -> 3 (1853) -> 4 (1862) நிறுவன உருவாக்க காலவரிசையைத் துல்லியமாகப் பின்பற்றுகிறது."}
    },
    "TNPSC Trap: Charter Act of 1853 created the 6-member Indian (Central) Legislative Council, often called mini-Parliament.",
    "TNPSC பொறி: 1853 சாசனச் சட்டம் 6 உறுப்பினர்களைக் கொண்ட மத்திய சட்ட மேலவையை ('சிறிய நாடாளுமன்றம்') உருவாக்கியது.",
    "First Law Commission under Macaulay drafted the Indian Penal Code (IPC).",
    "மெக்காலே தலைமையிலான முதல் சட்ட ஆணையம் இந்திய தண்டனைச் சட்டத்தை (IPC) தயாரித்தது.",
    ["Polity", "Historical Background", "Chronology", "Law Commission", "Legislative Council"]
))

# Q17: Conceptual
q_list.append(make_q(
    17, "Hard", "Chronology",
    "Arrange the establishment of the following constitutional and statutory institutions in 20th Century British India in correct chronological order:\n1. Amalgamation of Presidency Banks into Imperial Bank of India\n2. Establishment of Central Public Service Commission\n3. Establishment of Reserve Bank of India\n4. Inauguration of the Federal Court of India",
    "20 ஆம் நூற்றாண்டு பிரிட்டிஷ் இந்தியாவில் பின்வரும் அரசியலமைப்பு மற்றும் சட்டப்பூர்வ அமைப்புகள் தொடங்கப்பட்டதை காலவரிசையில் அமைக்கவும்:\n1. மாகாண வங்கிகளை இணைத்து இந்தியாவின் இம்பீரியல் வங்கியை உருவாக்குதல்\n2. மத்திய பொதுச் சேவை ஆணையம் அமைத்தல்\n3. இந்திய ரிசர்வ் வங்கி அமைத்தல்\n4. இந்தியாவின் கூட்டாட்சி நீதிமன்றத்தைத் தொடங்குதல்",
    [("A", "1 -> 2 -> 3 -> 4", "1 -> 2 -> 3 -> 4"), ("B", "2 -> 1 -> 3 -> 4", "2 -> 1 -> 3 -> 4"), ("C", "1 -> 3 -> 2 -> 4", "1 -> 3 -> 2 -> 4"), ("D", "1 -> 2 -> 4 -> 3", "1 -> 2 -> 4 -> 3")],
    "A",
    "Sequence: 1 (Imperial Bank 1921) -> 2 (CPSC Oct 1926) -> 3 (RBI April 1935 under 1934 Act) -> 4 (Federal Court Oct 1937 under 1935 Act).",
    "வரிசை: 1 (இம்பீரியல் வங்கி 1921) -> 2 (மத்திய பொதுச் சேவை ஆணையம் அக் 1926) -> 3 (ரிசர்வ் வங்கி ஏப் 1935) -> 4 (கூட்டாட்சி நீதிமன்றம் அக் 1937).",
    {
        "A": {"en": "Correct. 1 (1921) -> 2 (1926) -> 3 (1935) -> 4 (1937) follows exact institutional creation timeline.", "ta": "சரி. 1 (1921) -> 2 (1926) -> 3 (1935) -> 4 (1937) நிறுவன உருவாக்க ஆண்டைத் துல்லியமாகப் பின்பற்றுகிறது."},
        "B": {"en": "Incorrect. Imperial Bank (1921) was established before CPSC (1926).", "ta": "தவறு. இம்பீரியல் வங்கி (1921) மத்திய பொதுச் சேவை ஆணையத்திற்கு (1926) முன்பே அமைந்தது."},
        "C": {"en": "Incorrect. CPSC (1926) was established before RBI (1935).", "ta": "தவறு. மத்திய பொதுச் சேவை ஆணையம் (1926) ரிசர்வ் வங்கிக்கு (1935) முந்தியது."},
        "D": {"en": "Incorrect. RBI (April 1935) was established before Federal Court (Oct 1937).", "ta": "தவறு. ரிசர்வ் வங்கி (ஏப்ரல் 1935) கூட்டாட்சி நீதிமன்றத்திற்கு (அக்டோபர் 1937) முந்தியது."}
    },
    "TNPSC Trap: RBI was established in 1935 under Reserve Bank of India Act 1934; Federal Court was established in 1937 under GOI Act 1935.",
    "TNPSC பொறி: ரிசர்வ் வங்கி 1934 சட்டத்தின்படி 1935-ல் அமைந்தது; கூட்டாட்சி நீதிமன்றம் 1935 சட்டத்தின்படி 1937-ல் அமைந்தது.",
    "Imperial Bank of India later became State Bank of India (SBI) in 1955.",
    "இந்திய இம்பீரியல் வங்கி பின்னர் 1955-ல் பாரத ஸ்டேட் வங்கி (SBI) என மாறியது.",
    ["Polity", "Historical Background", "Chronology", "RBI", "Federal Court"]
))

# Q18: Conceptual
q_list.append(make_q(
    18, "Hard", "Chronology",
    "Arrange the creation of the following supervisory offices in Great Britain for Indian administration in chronological order:\n1. Creation of the Office of Governor-General of Bengal with a Council of Four\n2. Creation of the Office of Board of Control consisting of six Privy Councillors\n3. Creation of the Office of Secretary of State for India assisted by Council of India\n4. Creation of the Office of High Commissioner for India in London",
    "இந்திய நிர்வாகத்திற்காக பிரித்தானியாவில் உருவாக்கப்பட்ட பின்வரும் கண்காணிப்பு அலுவலகங்களை காலவரிசையில் அமைக்கவும்:\n1. நான்கு உறுப்பினர்களைக் கொண்ட கவுன்சிலுடன் வங்காள கவர்னர்-ஜெனரல் அலுவலகத்தை உருவாக்குதல்\n2. ஆறு ப்ரிவி கவுன்சிலர்களைக் கொண்ட கட்டுப்பாட்டு வாரிய அலுவலகத்தை உருவாக்குதல்\n3. இந்தியக் குழுவின் உதவியுடன் இந்திய அரசுச் செயலர் அலுவலகத்தை உருவாக்குதல்\n4. லண்டனில் இந்திய உயர் ஆணையர் (High Commissioner) அலுவலகத்தை உருவாக்குதல்",
    [("A", "1 -> 3 -> 2 -> 4", "1 -> 3 -> 2 -> 4"), ("B", "1 -> 2 -> 3 -> 4", "1 -> 2 -> 3 -> 4"), ("C", "2 -> 1 -> 3 -> 4", "2 -> 1 -> 3 -> 4"), ("D", "1 -> 2 -> 4 -> 3", "1 -> 2 -> 4 -> 3")],
    "B",
    "Sequence: 1 (1773 Regulating Act) -> 2 (1784 Pitt's India Act) -> 3 (1858 GOI Act) -> 4 (1919 GOI Act). London institutional mechanisms.",
    "வரிசை: 1 (1773 ஒழுங்குமுறைச் சட்டம்) -> 2 (1784 பிட் இந்தியச் சட்டம்) -> 3 (1858 இந்திய அரசுச் சட்டம்) -> 4 (1919 இந்திய அரசுச் சட்டம்).",
    {
        "A": {"en": "Incorrect. Board of Control (1784) was created before Secretary of State (1858).", "ta": "தவறு. கட்டுப்பாட்டு வாரியம் (1784) அரசுச் செயலருக்கு (1858) முந்தியது."},
        "B": {"en": "Correct. 1 (1773) -> 2 (1784) -> 3 (1858) -> 4 (1919) matches imperial oversight office timeline.", "ta": "சரி. 1 (1773) -> 2 (1784) -> 3 (1858) -> 4 (1919) கண்காணிப்பு அலுவலக உருவாக்க ஆண்டைப் பின்பற்றுகிறது."},
        "C": {"en": "Incorrect. Governor-General of Bengal (1773) was created before Board of Control (1784).", "ta": "தவறு. வங்காள கவர்னர்-ஜெனரல் (1773) கட்டுப்பாட்டு வாரியத்திற்கு (1784) முந்தியவர்."},
        "D": {"en": "Incorrect. High Commissioner for India in London was created by GOI Act 1919 (4).", "ta": "தவறு. லண்டன் இந்திய உயர் ஆணையர் பதவி 1919 இந்திய அரசுச் சட்டத்தால் உருவாக்கப்பட்டது (4)." }
    },
    "TNPSC Trap: GOI Act 1919 created High Commissioner for India in London and transferred some functions from Secretary of State.",
    "TNPSC பொறி: 1919 இந்திய அரசுச் சட்டம் லண்டனில் இந்திய உயர் ஆணையர் பதவியை உருவாக்கி அரசுச் செயலரின் சில அதிகாரங்களை மாற்றியது.",
    "Board of Control and Court of Directors were abolished together by the Government of India Act 1858.",
    "கட்டுப்பாட்டு வாரியம் மற்றும் இயக்குநர்கள் அவை இரண்டும் 1858 இந்திய அரசுச் சட்டத்தால் ஒன்றாக ஒழிக்கப்பட்டன.",
    ["Polity", "Historical Background", "Chronology", "High Commissioner", "Secretary of State"]
))

# Q19: Conceptual
q_list.append(make_q(
    19, "Hard", "Chronology",
    "Arrange the following constitutional milestones in the evolution of Indian legislative representation in correct chronological order:\n1. First statutory distinction made between legislative and executive functions of Governor-General's Council\n2. Inclusion of non-official Indians (Raja of Benaras, Maharaja of Patiala, Sir Dinkar Rao) as nominated members\n3. Introduction of direct elections for the central and provincial legislative bodies\n4. Establishment of complete provincial executive accountability to an elected legislature",
    "இந்தியச் சட்ட பிரதிநிதித்துவ வளர்ச்சியின் பின்வரும் அரசியலமைப்பு மைல்கற்களை சரியான காலவரிசையில் அமைக்கவும்:\n1. கவர்னர்-ஜெனரல் கவுன்சிலின் சட்ட மற்றும் நிர்வாகப் பணிகளுக்கு இடையே முதன்முறையாக சட்டப்பூர்வ வேறுபாடு ஏற்படுத்தப்படல்\n2. பரிந்துரைக்கப்பட்ட உறுப்பினர்களாக அதிகாரப்பூர்வமற்ற இந்தியர்கள் (பெனாரஸ் ராஜா, பட்டியாலா மகாராஜா, சர் தினகர் ராவ்) சேர்க்கப்படல்\n3. மத்திய மற்றும் மாகாண சட்டமன்றங்களுக்கு நேரடித் தேர்தல் முறையை அறிமுகப்படுத்துதல்\n4. தேர்ந்தெடுக்கப்பட்ட சட்டமன்றத்திற்கு மாகாண நிர்வாகத்தின் முழுமையான பொறுப்புடைமையை நிறுவுதல்",
    [("A", "1 -> 3 -> 2 -> 4", "1 -> 3 -> 2 -> 4"), ("B", "2 -> 1 -> 3 -> 4", "2 -> 1 -> 3 -> 4"), ("C", "1 -> 2 -> 3 -> 4", "1 -> 2 -> 3 -> 4"), ("D", "1 -> 2 -> 4 -> 3", "1 -> 2 -> 4 -> 3")],
    "C",
    "Sequence: 1 (1853 Charter Act) -> 2 (1861 Indian Councils Act) -> 3 (1919 GOI Act) -> 4 (1935 GOI Act). Legislative representation trajectory.",
    "வரிசை: 1 (1853 சாசனச் சட்டம்) -> 2 (1861 இந்தியக் கவுன்சில்கள் சட்டம்) -> 3 (1919 இந்திய அரசுச் சட்டம்) -> 4 (1935 இந்திய அரசுச் சட்டம்).",
    {
        "A": {"en": "Incorrect. Nominated Indians inclusion (1861) was before direct elections (1919).", "ta": "தவறு. இந்தியர்கள் நியமனம் (1861) நேரடித் தேர்தலுக்கு (1919) முந்தியது."},
        "B": {"en": "Incorrect. Separation of functions (1853) came before nomination of Indians (1861).", "ta": "தவறு. பணிகளின் வேறுபாடு (1853) இந்தியர்கள் நியமனத்திற்கு (1861) முந்தியது."},
        "C": {"en": "Correct. 1 (1853) -> 2 (1861) -> 3 (1919) -> 4 (1935) accurately tracks representative evolution.", "ta": "சரி. 1 (1853) -> 2 (1861) -> 3 (1919) -> 4 (1935) பிரதிநிதித்துவ வளர்ச்சியைத் துல்லியமாகக் காட்டுகிறது."},
        "D": {"en": "Incorrect. Direct elections (1919) preceded provincial responsible government (1935).", "ta": "தவறு. நேரடித் தேர்தல் (1919) மாகாணப் பொறுப்பு ஆட்சிக்கு (1935) முந்தியது."}
    },
    "TNPSC Trap: Lord Canning nominated Raja of Benaras, Maharaja of Patiala, and Sir Dinkar Rao to Legislative Council in 1862.",
    "TNPSC பொறி: 1862-ல் லார்டு கேனிங் பெனாரஸ் ராஜா, பட்டியாலா மகாராஜா, சர் தினகர் ராவ் ஆகியோரைச் சட்ட மேலவைக்கு நியமித்தார்.",
    "Direct elections were introduced in India for the first time by the Government of India Act 1919.",
    "1919 இந்திய அரசுச் சட்டம் மூலமாகவே இந்தியாவில் முதன்முறையாக நேரடித் தேர்தல் முறை அறிமுகமானது.",
    ["Polity", "Historical Background", "Chronology", "Legislative Evolution", "Direct Elections"]
))

# Q20: Conceptual
q_list.append(make_q(
    20, "Hard", "Chronology",
    "Arrange the following developments concerning communal electorates and seat reservations in chronological sequence:\n1. Introduction of separate electorates exclusively for Muslims\n2. Extension of separate electorates to Sikhs, Indian Christians, Anglo-Indians, and Europeans\n3. Announcement of Communal Award by Ramsay MacDonald extending separate electorates to Depressed Classes\n4. Signing of Poona Pact retaining joint electorate for Depressed Classes with reserved seats",
    "வகுப்புவாதத் தொகுதிகள் மற்றும் இடஒதுக்கீடு தொடர்பான பின்வரும் நிகழ்வுகளை காலவரிசையில் அமைக்கவும்:\n1. முஸ்லிம்களுக்கு மட்டும் பிரத்யேகமாக தனித் தொகுதிகளை அறிமுகப்படுத்துதல்\n2. சீக்கியர்கள், இந்தியக் கிறிஸ்தவர்கள், ஆங்லோ-இந்தியர்கள் மற்றும் ஐரோப்பியர்களுக்கும் தனித் தொகுதிகளை நீட்டித்தல்\n3. ஒடுக்கப்பட்ட வகுப்பினருக்கும் தனித் தொகுதிகளை நீட்டித்து ராம்சே மெக்டொனால்டு வகுப்புவாத அறிக்கையை அறிவித்தல்\n4. ஒடுக்கப்பட்ட வகுப்பினருக்கு இடஒதுக்கீட்டுடன் கூட்டுத் தொகுதியை உறுதிசெய்து பூனா ஒப்பந்தம் கையெழுத்தாதல்",
    [("A", "1 -> 3 -> 2 -> 4", "1 -> 3 -> 2 -> 4"), ("B", "2 -> 1 -> 3 -> 4", "2 -> 1 -> 3 -> 4"), ("C", "1 -> 2 -> 4 -> 3", "1 -> 2 -> 4 -> 3"), ("D", "1 -> 2 -> 3 -> 4", "1 -> 2 -> 3 -> 4")],
    "D",
    "Sequence: 1 (1909 Morley-Minto) -> 2 (1919 Montagu-Chelmsford) -> 3 (Aug 1932 Communal Award) -> 4 (Sept 1932 Poona Pact).",
    "வரிசை: 1 (1909 மார்லி-மிண்டோ) -> 2 (1919 மாண்டேகு-செம்ஸ்ஃபோர்டு) -> 3 (ஆக 1932 வகுப்புவாத அறிக்கை) -> 4 (செப் 1932 பூனா ஒப்பந்தம்).",
    {
        "A": {"en": "Incorrect. Extension to Sikhs/Christians (1919) was before Communal Award (1932).", "ta": "தவறு. சீக்கியர்கள்/கிறிஸ்தவர்கள் நீட்டிப்பு (1919) வகுப்புவாத அறிக்கைக்கு (1932) முந்தியது."},
        "B": {"en": "Incorrect. Muslim separate electorate (1909) preceded 1919 extensions.", "ta": "தவறு. முஸ்லிம் தனித் தொகுதி (1909) 1919 நீட்டிப்புகளுக்கு முந்தியது."},
        "C": {"en": "Incorrect. Poona Pact (Sept 1932) was signed after Communal Award (Aug 1932).", "ta": "தவறு. பூனா ஒப்பந்தம் (செப் 1932) வகுப்புவாத அறிக்கைக்கு (ஆக 1932) பிறகே கையெழுத்தானது."},
        "D": {"en": "Correct. 1 (1909) -> 2 (1919) -> 3 (Aug 1932) -> 4 (Sept 1932) accurately follows communal electoral history.", "ta": "சரி. 1 (1909) -> 2 (1919) -> 3 (ஆக 1932) -> 4 (செப் 1932) வகுப்புவாத தேர்தல் வரலாற்றைத் துல்லியமாகப் பின்பற்றுகிறது."}
    },
    "TNPSC Trap: Poona Pact modified the Communal Award by replacing separate electorates for Depressed Classes with reserved seats in joint electorates.",
    "TNPSC பொறி: பூனா ஒப்பந்தம் ஒடுக்கப்பட்ட வகுப்பினருக்கான தனித் தொகுதியை நீக்கி கூட்டுத் தொகுதியில் இடஒதுக்கீட்டை வழங்கியது.",
    "Poona Pact was signed between B.R. Ambedkar and M.K. Gandhi (represented by Madan Mohan Malaviya) in Yerwada Central Jail.",
    "பூனா ஒப்பந்தம் எரவாடா சிறையில் பி.ஆர். அம்பேத்கர் மற்றும் எம்.கே. காந்தி (மதன் மோகன் மாளவியா மூலம்) இடையே கையெழுத்தானது.",
    ["Polity", "Historical Background", "Chronology", "Communal Award", "Poona Pact"]
))

# Q21: Comparative
q_list.append(make_q(
    21, "Hard", "Chronology",
    "Arrange the following legislative control stages over financial budgets in British India in chronological order:\n1. Non-official members allowed to discuss budget without power to vote or move resolutions\n2. Right to ask supplementary questions and move resolutions on specific budget items granted\n3. Separation of Central and Provincial budgets with independent provincial tax-raising authority\n4. Enactment of statutory federal, provincial, and concurrent legislative heads controlling budget items",
    "பிரிட்டிஷ் இந்தியாவில் நிதி வரவு செலவுத் திட்டத்தின் மீதான சட்டமன்றக் கட்டுப்பாட்டு கட்டங்களை காலவரிசையில் அமைக்கவும்:\n1. வாக்களிக்கும் அல்லது தீர்மானம் கொண்டுவரும் அதிகாரமின்றி பட்ஜெட்டை விவாதிக்க உறுப்பினர்களுக்கு அனுமதித்தல்\n2. பட்ஜெட் தலைப்புகளில் துணைக் கேள்விகள் கேட்கவும் தீர்மானங்கள் கொண்டுவரவும் உரிமை வழங்கப்படல்\n3. மத்திய மற்றும் மாகாண வரவு செலவுத் திட்டங்களை தனியாகப் பிரித்து மாகாணங்களுக்கு வரி விதிக்கும் அதிகாரம் அளித்தல்\n4. கூட்டாட்சி, மாகாண மற்றும் பொதுப் பட்டியல்களின் மூலம் பட்ஜெட் செலவினங்களைச் சட்டப்பூர்வமாகப் பிரித்தல்",
    [("A", "1 -> 2 -> 3 -> 4", "1 -> 2 -> 3 -> 4"), ("B", "2 -> 1 -> 3 -> 4", "2 -> 1 -> 3 -> 4"), ("C", "1 -> 3 -> 2 -> 4", "1 -> 3 -> 2 -> 4"), ("D", "1 -> 2 -> 4 -> 3", "1 -> 2 -> 4 -> 3")],
    "A",
    "Sequence: 1 (1892 Indian Councils Act) -> 2 (1909 Indian Councils Act) -> 3 (1919 GOI Act) -> 4 (1935 GOI Act). Budget control evolution.",
    "வரிசை: 1 (1892 இந்தியக் கவுன்சில்கள் சட்டம்) -> 2 (1909 இந்தியக் கவுன்சில்கள் சட்டம்) -> 3 (1919 இந்திய அரசுச் சட்டம்) -> 4 (1935 இந்திய அரசுச் சட்டம்).",
    {
        "A": {"en": "Correct. 1 (1892) -> 2 (1909) -> 3 (1919) -> 4 (1935) tracks progressively expanding budget powers.", "ta": "சரி. 1 (1892) -> 2 (1909) -> 3 (1919) -> 4 (1935) பட்ஜெட் அதிகாரங்களின் வளர்ச்சியைத் துல்லியமாகக் காட்டுகிறது."},
        "B": {"en": "Incorrect. Discussion of budget (1892) was allowed before supplementary questions (1909).", "ta": "தவறு. பட்ஜெட் விவாதம் (1892) துணைக் கேள்விகளுக்கு (1909) முந்தியது."},
        "C": {"en": "Incorrect. Supplementary questions (1909) came before budget separation (1919).", "ta": "தவறு. துணைக் கேள்விகள் (1909) பட்ஜெட் பிரிப்பிற்கு (1919) முந்தியது."},
        "D": {"en": "Incorrect. 3-tier list division (1935) was enacted after 1919 budget separation.", "ta": "தவறு. 3 அடுக்கு பட்டியல் பிரிப்பு (1935) 1919 பட்ஜெட் பிரிப்பிற்குப் பின்னரே இயற்றப்பட்டது."}
    },
    "TNPSC Trap: Indian Councils Act 1892 allowed budget discussion, but voting on budget was NOT allowed until later.",
    "TNPSC பொறி: 1892 இந்தியக் கவுன்சில்கள் சட்டம் பட்ஜெட் விவாதத்தை மட்டுமே அனுமதித்தது; வாக்களிக்கும் உரிமை வழங்கப்படவில்லை.",
    "The 1919 Act separated provincial budgets, authorizing provincial legislatures to enact their own budgets.",
    "1919 சட்டம் மாகாண வரவு செலவுத் திட்டத்தைப் பிரித்து, மாகாண சட்டமன்றங்கள் சொந்த பட்ஜெட்டை இயற்ற அதிகாரமளித்தது.",
    ["Polity", "Historical Background", "Chronology", "Budget Powers", "Financial Devolution"]
))

# Q22: Comparative
q_list.append(make_q(
    22, "Hard", "Chronology",
    "Arrange the following provisions strengthening Governor-General's extraordinary legislative powers in chronological order:\n1. Governor-General in Council empowered to make rules, regulations, and ordinances for Bengal presidency\n2. Governor-General vested with exclusive law-making authority for all British territories in India\n3. Power to issue Ordinances during emergencies without concurrence of Legislative Council granted\n4. Power of Certification and absolute Veto over Central Legislative bills enacted",
    "கவர்னர்-ஜெனரலின் அவசரகால மற்றும் பிரத்யேக சட்ட அதிகாரங்கள் வலுப்படுத்தப்பட்டதை காலவரிசையில் அமைக்கவும்:\n1. வங்காள மாகாணத்திற்கு விதிகள், ஒழுங்குமுறைகள் மற்றும் அவசரச் சட்டங்களை பிறப்பிக்க கவர்னர்-ஜெனரலுக்கு அதிகாரம் அளித்தல்\n2. பிரிட்டிஷ் இந்தியாவின் அனைத்துப் பகுதிகளுக்கும் பிரத்யேக சட்டமியற்றும் அதிகாரத்தை கவர்னர்-ஜெனரலிடம் ஒப்படைத்தல்\n3. அவசர காலத்தில் சட்ட மேலவையின் ஒப்புதலின்றி அவசரச் சட்டங்களை (Ordinances) பிறப்பிக்கும் அதிகாரம் அளித்தல்\n4. மத்திய சட்டமன்ற மசோதாக்கள் மீது நிராகரிப்பு (Veto) மற்றும் சான்றளிப்பு (Certification) அதிகாரங்களை வழங்குதல்",
    [("A", "2 -> 1 -> 3 -> 4", "2 -> 1 -> 3 -> 4"), ("B", "1 -> 2 -> 3 -> 4", "1 -> 2 -> 3 -> 4"), ("C", "1 -> 3 -> 2 -> 4", "1 -> 3 -> 2 -> 4"), ("D", "1 -> 2 -> 4 -> 3", "1 -> 2 -> 4 -> 3")],
    "B",
    "Sequence: 1 (1773 Regulating Act) -> 2 (1833 Charter Act) -> 3 (1861 Indian Councils Act) -> 4 (1919 GOI Act). Evolution of executive ordinance & veto powers.",
    "வரிசை: 1 (1773 ஒழுங்குமுறைச் சட்டம்) -> 2 (1833 சாசனச் சட்டம்) -> 3 (1861 இந்தியக் கவுன்சில்கள் சட்டம்) -> 4 (1919 இந்திய அரசுச் சட்டம்).",
    {
        "A": {"en": "Incorrect. 1773 Bengal regulation power (1) preceded 1833 all-India power (2).", "ta": "தவறு. 1773 வங்காள ஒழுங்குமுறை அதிகாரம் (1) 1833 அகில இந்திய அதிகாரத்திற்கு (2) முந்தியது."},
        "B": {"en": "Correct. 1 (1773) -> 2 (1833) -> 3 (1861) -> 4 (1919) accurately traces Governor-General's ordinance & veto powers.", "ta": "சரி. 1 (1773) -> 2 (1833) -> 3 (1861) -> 4 (1919) கவர்னர்-ஜெனரலின் அவசரச் சட்ட அதிகாரங்களின் வளர்ச்சியைத் துல்லியமாகக் காட்டுகிறது."},
        "C": {"en": "Incorrect. Ordinance power (1861) came after exclusive law-making authority (1833).", "ta": "தவறு. அவசரச் சட்ட அதிகாரம் (1861) பிரத்யேக சட்டமியற்றும் அதிகாரத்திற்குப் (1833) பின்னரே வந்தது."},
        "D": {"en": "Incorrect. Certification power (1919) was enacted after Ordinance power of 1861.", "ta": "தவறு. சான்றளிப்பு அதிகாரம் (1919) 1861 அவசரச் சட்ட அதிகாரத்திற்குப் பின்னரே வந்தது."}
    },
    "TNPSC Trap: Statutory Ordinance-making power of Viceroy was introduced by Indian Councils Act of 1861 (valid for 6 months).",
    "TNPSC பொறி: வைஸ்ராயின் அவசரச் சட்டம் பிறப்பிக்கும் அதிகாரம் (6 மாத காலம் செல்லுபடியாகும்) 1861 சட்டத்தில் அறிமுகப்படுத்தப்பட்டது.",
    "The 1919 Act gave Governor-General certification power to enact any bill rejected by the legislature.",
    "சட்டமன்றத்தால் நிராகரிக்கப்பட்ட மசோதாவையும் நிறைவேற்ற கவர்னர்-ஜெனரலுக்கு சான்றளிப்பு அதிகாரத்தை 1919 சட்டம் வழங்கியது.",
    ["Polity", "Historical Background", "Chronology", "Ordinance Power", "Veto Power"]
))

# Q23: Comparative
q_list.append(make_q(
    23, "Hard", "Chronology",
    "Arrange the following constitutional milestones altering the status of East India Company in chronological order:\n1. Extension of EIC charter for 20 years with commercial monopoly intact\n2. Termination of EIC trade monopoly in India except for tea trade and trade with China\n3. Complete termination of EIC commercial activities, converting it into a purely administrative body\n4. Extension of EIC charter on trust for the Crown without specifying any fixed time period",
    "கிழக்கிந்திய கம்பெனியின் அந்தஸ்தை மாற்றிய பின்வரும் அரசியலமைப்பு மைல்கற்களை காலவரிசையில் அமைக்கவும்:\n1. வர்த்தக முற்றுரிமையுடன் கம்பெனி சாசனத்தை 20 ஆண்டுகளுக்கு நீட்டித்தல்\n2. தேயிலை மற்றும் சீனா வர்த்தகம் தவிர்த்து கம்பெனியின் வர்த்தக முற்றுரிமையை முடிவுக்குக் கொண்டுவருதல்\n3. கம்பெனியின் வணிக நடவடிக்கைகளை முழுமையாக முடிவுக்குக் கொண்டுவந்து அதை நிர்வாக அமைப்பாக மட்டும் மாற்றுதல்\n4. எந்தவொரு குறிப்பிட்ட காலவரையறையுமின்றி பிரிட்டிஷ் முடி ஆட்சிக்காக கம்பெனி சாசனத்தை நீட்டித்தல்",
    [("A", "1 -> 3 -> 2 -> 4", "1 -> 3 -> 2 -> 4"), ("B", "2 -> 1 -> 3 -> 4", "2 -> 1 -> 3 -> 4"), ("C", "1 -> 2 -> 3 -> 4", "1 -> 2 -> 3 -> 4"), ("D", "1 -> 2 -> 4 -> 3", "1 -> 2 -> 4 -> 3")],
    "C",
    "Sequence: 1 (1793 Charter Act) -> 2 (1813 Charter Act) -> 3 (1833 Charter Act) -> 4 (1853 Charter Act). Gradual dismantling of EIC.",
    "வரிசை: 1 (1793 சாசனச் சட்டம்) -> 2 (1813 சாசனச் சட்டம்) -> 3 (1833 சாசனச் சட்டம்) -> 4 (1853 சாசனச் சட்டம்).",
    {
        "A": {"en": "Incorrect. Partial abolition of monopoly (1813) came before complete commercial termination (1833).", "ta": "தவறு. பகுதியளவு வர்த்தக ஒழிப்பு (1813) முழு வணிக ஒழிப்புக்கு (1833) முந்தியது."},
        "B": {"en": "Incorrect. Charter extension in 1793 (1) was before 1813 Act (2).", "ta": "தவறு. 1793 சாசன நீட்டிப்பு (1) 1813 சட்டத்திற்கு (2) முந்தியது."},
        "C": {"en": "Correct. 1 (1793) -> 2 (1813) -> 3 (1833) -> 4 (1853) perfectly matches the 4 sequential Charter Acts.", "ta": "சரி. 1 (1793) -> 2 (1813) -> 3 (1833) -> 4 (1853) நான்கு சாசனச் சட்டங்களையும் வரிசையாகப் பின்பற்றுகிறது."},
        "D": {"en": "Incorrect. Charter Act 1853 (4) was after Charter Act 1833 (3).", "ta": "தவறு. 1853 சாசனச் சட்டம் (4) 1833 சாசனச் சட்டத்திற்குப் (3) பின்னரே வந்தது."}
    },
    "TNPSC Trap: 1833 Act ended ALL commercial activities; EIC became purely an administrative body for British territories in India.",
    "TNPSC பொறி: 1833 சட்டம் கம்பெனியின் அனைத்து வர்த்தக நடவடிக்கைகளையும் முடிவுக்குக் கொண்டுவந்து அதை முற்றிலும் நிர்வாக அமைப்பாக மாற்றியது.",
    "Charter Act of 1793 laid down that salaries of Board of Control members were to be paid out of Indian revenues.",
    "1793 சாசனச் சட்டம் கட்டுப்பாட்டு வாரிய உறுப்பினர்களின் சம்பளம் இந்திய வருவாயிலிருந்தே வழங்கப்பட வேண்டும் என விதித்தது.",
    ["Polity", "Historical Background", "Chronology", "Charter Acts", "East India Company"]
))

# Q24: Comparative
q_list.append(make_q(
    24, "Hard", "Chronology",
    "Arrange the structural transformation of Indian legislative bodies in correct chronological order:\n1. Maintenance of official majority in Central Legislative Council while allowing non-official majority in Provincial Councils\n2. Creation of a Bicameral Central Legislature comprising Council of State and Central Legislative Assembly\n3. Extension of Bicameralism to 6 out of 11 British Indian provinces\n4. Complete termination of British Parliament's legislative authority over India and Bengal",
    "இந்திய சட்டமன்ற அமைப்புகளின் கட்டமைப்பு மாற்றங்களை சரியான காலவரிசையில் அமைக்கவும்:\n1. மத்திய சட்ட மேலவையில் அதிகாரப்பூர்வ பெரும்பான்மையைத் தக்கவைத்து மாகாண மேலவைகளில் அதிகாரப்பூர்வமற்ற பெரும்பான்மையை அனுமதித்தல்\n2. மாநிலங்கள் அவை மற்றும் மத்திய சட்டப் பேரவையைக் கொண்ட இரு அவை மத்திய சட்டமன்றத்தை உருவாக்குதல்\n3. 11 பிரிட்டிஷ் இந்திய மாகாணங்களில் 6 மாகாணங்களுக்கு இரு அவை முறையை நீட்டித்தல்\n4. இந்தியா மற்றும் வங்காளத்தின் மீதான பிரிட்டிஷ் நாடாளுமன்றத்தின் சட்ட அதிகாரத்தை முழுமையாக முடிவுக்குக் கொண்டுவருதல்",
    [("A", "1 -> 3 -> 2 -> 4", "1 -> 3 -> 2 -> 4"), ("B", "2 -> 1 -> 3 -> 4", "2 -> 1 -> 3 -> 4"), ("C", "1 -> 2 -> 4 -> 3", "1 -> 2 -> 4 -> 3"), ("D", "1 -> 2 -> 3 -> 4", "1 -> 2 -> 3 -> 4")],
    "D",
    "Sequence: 1 (1909 Indian Councils Act) -> 2 (1919 GOI Act) -> 3 (1935 GOI Act) -> 4 (1947 Indian Independence Act). Parliamentary architecture trajectory.",
    "வரிசை: 1 (1909 இந்தியக் கவுன்சில்கள் சட்டம்) -> 2 (1919 இந்திய அரசுச் சட்டம்) -> 3 (1935 இந்திய அரசுச் சட்டம்) -> 4 (1947 இந்திய சுதந்திரச் சட்டம்).",
    {
        "A": {"en": "Incorrect. Central bicameralism (1919) was created before provincial bicameralism in 6 provinces (1935).", "ta": "தவறு. மத்திய இரு அவை முறை (1919) 6 மாகாண இரு அவை முறைக்கு (1935) முன்பே உருவாக்கப்பட்டது."},
        "B": {"en": "Incorrect. 1909 majority rule (1) preceded 1919 Central Bicameralism (2).", "ta": "தவறு. 1909 பெரும்பான்மை விதி (1) 1919 மத்திய இரு அவை முறைக்கு (2) முந்தியது."},
        "C": {"en": "Incorrect. Termination of British authority (1947) was the final step.", "ta": "தவறு. பிரிட்டிஷ் அதிகார முடிவு (1947) இறுதிப் படியாகும்."},
        "D": {"en": "Correct. 1 (1909) -> 2 (1919) -> 3 (1935) -> 4 (1947) accurately traces legislative body transformation.", "ta": "சரி. 1 (1909) -> 2 (1919) -> 3 (1935) -> 4 (1947) சட்டமன்றக் கட்டமைப்பு மாற்றத்தை துல்லியமாகக் காட்டுகிறது."}
    },
    "TNPSC Trap: GOI Act 1935 introduced bicameralism in 6 provinces: Bengal, Bombay, Madras, Bihar, Assam, and United Provinces.",
    "TNPSC பொறி: 1935 இந்திய அரசுச் சட்டம் 6 மாகாணங்களில் (வங்காளம், பம்பாய், மதராஸ், பீகார், அசாம், ஐக்கிய மாகாணம்) இரு அவை முறையை அறிமுகப்படுத்தியது.",
    "Indian Independence Act 1947 declared that no Act of British Parliament passed after August 15, 1947 would extend to new Dominions.",
    "1947 ஆகஸ்ட் 15-க்கு பின் இயற்றப்படும் பிரிட்டிஷ் நாடாளுமன்றச் சட்டங்கள் புதிய டொமினியன்களுக்குப் பொருந்தாது என 1947 சுதந்திரச் சட்டம் கூறியது.",
    ["Polity", "Historical Background", "Chronology", "Bicameralism", "Independence Act"]
))

# Q25: Comparative
q_list.append(make_q(
    25, "Hard", "Chronology",
    "Arrange the following shifts in provincial legislative independence in chronological order:\n1. Subordination of Governors of Bombay and Madras to Governor-General of Bengal in making laws\n2. Complete deprivation of legislative powers of Bombay and Madras Presidencies\n3. Restoration of legislative powers to Bombay and Madras Presidencies initiating decentralization\n4. Bifurcation of provincial executive into Reserved and Transferred subjects under Dyarchy",
    "மாகாண சட்ட சுதந்திரத்தில் ஏற்பட்ட பின்வரும் மாற்றங்களை காலவரிசையில் அமைக்கவும்:\n1. சட்டங்கள் இயற்றுவதில் பம்பாய் மற்றும் மதராஸ் கவர்னர்களை வங்காள கவர்னர்-ஜெனரலுக்குக் கீழ்ப்படுத்துதல்\n2. பம்பாய் மற்றும் மதராஸ் மாகாணங்களின் சட்ட அதிகாரங்களை முழுமையாகப் பறித்தல்\n3. பம்பாய் மற்றும் மதராஸ் மாகாணங்களுக்கு சட்ட அதிகாரங்களை மீட்டளித்து அதிகாரப் பரவலாக்கத்தைத் தொடங்குதல்\n4. இரட்டை ஆட்சியின் கீழ் மாகாண நிர்வாகத்தை ஒதுக்கப்பட்ட மற்றும் மாற்றப்பட்ட துறைகளாகப் பிரித்தல்",
    [("A", "1 -> 2 -> 3 -> 4", "1 -> 2 -> 3 -> 4"), ("B", "2 -> 1 -> 3 -> 4", "2 -> 1 -> 3 -> 4"), ("C", "1 -> 3 -> 2 -> 4", "1 -> 3 -> 2 -> 4"), ("D", "1 -> 2 -> 4 -> 3", "1 -> 2 -> 4 -> 3")],
    "A",
    "Sequence: 1 (1773 Regulating Act) -> 2 (1833 Charter Act) -> 3 (1861 Indian Councils Act) -> 4 (1919 GOI Act). Provincial status evolution.",
    "வரிசை: 1 (1773 ஒழுங்குமுறைச் சட்டம்) -> 2 (1833 சாசனச் சட்டம்) -> 3 (1861 இந்தியக் கவுன்சில்கள் சட்டம்) -> 4 (1919 இந்திய அரசுச் சட்டம்).",
    {
        "A": {"en": "Correct. 1 (1773) -> 2 (1833) -> 3 (1861) -> 4 (1919) tracks provincial legislative powers shift.", "ta": "சரி. 1 (1773) -> 2 (1833) -> 3 (1861) -> 4 (1919) மாகாண சட்ட அதிகார மாற்றங்களைத் துல்லியமாகக் காட்டுகிறது."},
        "B": {"en": "Incorrect. Subordination of Presidencies (1773) occurred before total legislative deprivation (1833).", "ta": "தவறு. மாகாணங்கள் கீழ்ப்படுத்தப்படுதல் (1773) முழு அதிகாரப் பறிப்புக்கு (1833) முந்தியது."},
        "C": {"en": "Incorrect. Restoration of legislative powers (1861) was after 1833 Act.", "ta": "தவறு. சட்ட அதிகார மீட்பு (1861) 1833 சட்டத்திற்குப் பின்னராகும்."},
        "D": {"en": "Incorrect. Dyarchy in provinces (1919) came after legislative restoration of 1861.", "ta": "தவறு. மாகாண இரட்டை ஆட்சி (1919) 1861 அதிகார மீட்புக்குப் பின்னரே வந்தது."}
    },
    "TNPSC Trap: 1833 Act deprived Bombay and Madras of legislative powers; 1861 Act restored them.",
    "TNPSC பொறி: 1833 சட்டம் பம்பாய், மதராஸின் சட்ட அதிகாரங்களைப் பறித்தது; 1861 சட்டம் அவற்றை மீட்டளித்தது.",
    "Under Dyarchy (1919 Act), Reserved subjects were administered by Governor with Executive Council, and Transferred subjects with Ministers.",
    "1919 இரட்டை ஆட்சியில் ஒதுக்கப்பட்ட துறைகள் கவர்னரின் நிர்வாகக் குழுவாலும், மாற்றப்பட்ட துறைகள் அமைச்சர்களாலும் நிர்வகிக்கப்பட்டன.",
    ["Polity", "Historical Background", "Chronology", "Provincial Devolution", "Dyarchy"]
))

# Q26: Constitutional Evolution
q_list.append(make_q(
    26, "Hard", "Chronology",
    "Arrange the following statutory steps in provincial constitutional autonomy in correct chronological order:\n1. Devolution Rules framed under Act of 1919 separating Central and Provincial subjects\n2. Appointment of Simon Commission to report on working of provincial executive dyarchy\n3. Abolition of provincial Dyarchy and introduction of full Provincial Autonomy\n4. Enactment of Indian Independence Act providing for partition of Bengal and Punjab provincial assemblies",
    "மாகாண அரசியலமைப்பு தன்னாட்சியின் பின்வரும் சட்டப்பூர்வ படிகளை சரியான காலவரிசையில் அமைக்கவும்:\n1. மத்திய மற்றும் மாகாணத் துறைகளைப் பிரித்து 1919 சட்டத்தின் கீழ் தயாரித்த அதிகாரப் பகிர்வு விதிகள் (Devolution Rules)\n2. மாகாண இரட்டை ஆட்சியின் செயல்பாட்டை ஆராய சைமன் குழு அமைத்தல்\n3. மாகாண இரட்டை ஆட்சியை ஒழித்து முழுமையான மாகாண தன்னாட்சியை அறிமுகப்படுத்துதல்\n4. வங்காளம் மற்றும் பஞ்சாப் மாகாண சட்டப் பேரவைகளைப் பிரிக்க வழிவகுத்த இந்திய சுதந்திரச் சட்டம் இயற்றப்படல்",
    [("A", "1 -> 3 -> 2 -> 4", "1 -> 3 -> 2 -> 4"), ("B", "1 -> 2 -> 3 -> 4", "1 -> 2 -> 3 -> 4"), ("C", "2 -> 1 -> 3 -> 4", "2 -> 1 -> 3 -> 4"), ("D", "1 -> 2 -> 4 -> 3", "1 -> 2 -> 4 -> 3")],
    "B",
    "Sequence: 1 (1919 Devolution Rules) -> 2 (1927 Simon Commission) -> 3 (1935 Provincial Autonomy) -> 4 (1947 Partition of Provincial assemblies).",
    "வரிசை: 1 (1919 பகிர்வு விதிகள்) -> 2 (1927 சைமன் குழு) -> 3 (1935 மாகாண தன்னாட்சி) -> 4 (1947 மாகாணங்கள் பிரிவினை).",
    {
        "A": {"en": "Incorrect. Simon Commission (1927) was appointed before Provincial Autonomy was introduced (1935).", "ta": "தவறு. சைமன் குழு (1927) மாகாண தன்னாட்சி அறிமுகத்திற்கு (1935) முன்பே அமைந்தது."},
        "B": {"en": "Correct. 1 (1919) -> 2 (1927) -> 3 (1935) -> 4 (1947) tracks constitutional progression of provinces.", "ta": "சரி. 1 (1919) -> 2 (1927) -> 3 (1935) -> 4 (1947) மாகாண அரசியலமைப்பு வளர்ச்சியைத் துல்லியமாகக் காட்டுகிறது."},
        "C": {"en": "Incorrect. Devolution Rules (1919) came before Simon Commission (1927).", "ta": "தவறு. அதிகாரப் பகிர்வு விதிகள் (1919) சைமன் குழுவிற்கு (1927) முந்தியவை."},
        "D": {"en": "Incorrect. Partition of provincial assemblies (1947) was after 1935 Provincial Autonomy.", "ta": "தவறு. மாகாணங்கள் பிரிவினை (1947) 1935 மாகாண தன்னாட்சிக்குப் பின்னரே நடந்தது."}
    },
    "TNPSC Trap: Dyarchy was abolished in Provinces by GOI Act 1935 and replaced by Provincial Autonomy, but Dyarchy was proposed at the Centre.",
    "TNPSC பொறி: 1935 சட்டம் மாகாணங்களில் இரட்டை ஆட்சியை நீக்கி தன்னாட்சியைக் கொண்டுவந்தது; ஆனால் மத்திய அளவில் இரட்டை ஆட்சியை முன்மொழிந்தது.",
    "Provincial autonomy meant governor was required to act on advice of ministers responsible to provincial legislature.",
    "மாகாண தன்னாட்சி என்பது கவர்னர் மாகாண சட்டமன்றத்திற்குப் பொறுப்பான அமைச்சர்களின் ஆலோசனைப்படி செயல்படுவதைக் குறித்தது.",
    ["Polity", "Historical Background", "Chronology", "Provincial Autonomy", "Devolution Rules"]
))

# Q27: Constitutional Evolution
q_list.append(make_q(
    27, "Hard", "Chronology",
    "Arrange the creation and territorial restructuring of the following provinces in British India in chronological order:\n1. Creation of Bengal Presidency under Governor-General of Bengal\n2. Establishment of North-Western Provinces under a Lieutenant Governor\n3. Creation of Chief Commissionership of Assam carved out of Bengal\n4. Separation of Sind from Bombay and creation of Orissa as separate provinces",
    "பிரிட்டிஷ் இந்தியாவில் பின்வரும் மாகாணங்கள் உருவாக்கப்பட்டது மற்றும் நிலப்பரப்பு மறுசீரமைக்கப்பட்டதை காலவரிசையில் அமைக்கவும்:\n1. வங்காள கவர்னர்-ஜெனரலின் கீழ் வங்காள மாகாணத்தை உருவாக்குதல்\n2. துணைநிலை ஆளுநரின் கீழ் வடமேற்கு மாகாணங்களை உருவாக்குதல்\n3. வங்காளத்திலிருந்து பிரிக்கப்பட்டு அசாம் தலைமை ஆணையர் (Chief Commissioner) மாகாணம் உருவாக்கப்படல்\n4. பம்பாயிலிருந்து சிந்து பிரிக்கப்பட்டு, ஒரிசா தனி மாகாணமாக உருவாக்கப்படல்",
    [("A", "1 -> 3 -> 2 -> 4", "1 -> 3 -> 2 -> 4"), ("B", "2 -> 1 -> 3 -> 4", "2 -> 1 -> 3 -> 4"), ("C", "1 -> 2 -> 3 -> 4", "1 -> 2 -> 3 -> 4"), ("D", "1 -> 2 -> 4 -> 3", "1 -> 2 -> 4 -> 3")],
    "C",
    "Sequence: 1 (1773 Bengal Presidency) -> 2 (1836 North-Western Provinces under 1833 Act) -> 3 (1874 Assam Chief Commissionership) -> 4 (1935 GOI Act creating Sind & Orissa).",
    "வரிசை: 1 (1773 வங்காள மாகாணம்) -> 2 (1836 வடமேற்கு மாகாணங்கள்) -> 3 (1874 அசாம் மாகாணம்) -> 4 (1935 சிந்து & ஒரிசா உருவாக்கம்).",
    {
        "A": {"en": "Incorrect. North-Western Provinces (1836) was created before Assam Chief Commissionership (1874).", "ta": "தவறு. வடமேற்கு மாகாணங்கள் (1836) அசாம் தலைமை ஆணையர் மாகாணத்திற்கு (1874) முந்தியவை."},
        "B": {"en": "Incorrect. Bengal Presidency (1773) was created before NWP (1836).", "ta": "தவறு. வங்காள மாகாணம் (1773) வடமேற்கு மாகாணங்களுக்கு (1836) முந்தியது."},
        "C": {"en": "Correct. 1 (1773) -> 2 (1836) -> 3 (1874) -> 4 (1935) accurately follows provincial territorial creation.", "ta": "சரி. 1 (1773) -> 2 (1836) -> 3 (1874) -> 4 (1935) மாகாணங்களின் உருவாக்க ஆண்டைத் துல்லியமாகப் பின்பற்றுகிறது."},
        "D": {"en": "Incorrect. Sind and Orissa creation (1935) was after 1874 Assam creation.", "ta": "தவறு. சிந்து மற்றும் ஒரிசா உருவாக்கம் (1935) 1874 அசாம் உருவாக்கத்திற்குப் பின்னராகும்."}
    },
    "TNPSC Trap: GOI Act 1935 separated Sind from Bombay Presidency and created Orissa as a new province (effective April 1936).",
    "TNPSC பொறி: 1935 இந்திய அரசுச் சட்டம் பம்பாயிலிருந்து சிந்தை பிரித்ததுடன் ஒரிசாவை புதிய மாகாணமாக உருவாக்கியது (ஏப்ரல் 1936 அமல்).",
    "Assam was separated from Bengal in 1874 and placed under a Chief Commissioner.",
    "அசாம் 1874-ல் வங்காளத்திலிருந்து பிரிக்கப்பட்டு தலைமை ஆணையரின் கீழ் கொண்டுவரப்பட்டது.",
    ["Polity", "Historical Background", "Chronology", "Provincial Boundaries", "Sind and Orissa"]
))

# Q28: Constitutional Evolution
q_list.append(make_q(
    28, "Hard", "Chronology",
    "Arrange the following macro-constitutional transition milestones in India in correct chronological order:\n1. Regulating Act initiating British Parliamentary supervision over East India Company governance\n2. Government of India Act 1858 ending Company Rule and establishing direct Crown Rule\n3. Government of India Act 1935 proposing an All-India Federation and abolishing provincial dyarchy\n4. Indian Independence Act 1947 terminating British Suzerainty and creating two independent Dominions",
    "இந்தியாவின் பேரின அரசியலமைப்பு மாற்றங்களின் பின்வரும் மைல்கற்களை சரியான காலவரிசையில் அமைக்கவும்:\n1. கிழக்கிந்திய கம்பெனியின் நிர்வாகத்தின் மீது பிரிட்டிஷ் நாடாளுமன்ற கண்காணிப்பைத் தொடங்கிய ஒழுங்குமுறைச் சட்டம்\n2. கம்பெனி ஆட்சியை முடிவுக்குக் கொண்டுவந்து பிரிட்டிஷ் முடி ஆட்சியை நிறுவிய 1858 இந்திய அரசுச் சட்டம்\n3. அகில இந்திய கூட்டாட்சியை முன்மொழிந்து மாகாண இரட்டை ஆட்சியை நீக்கிய 1935 இந்திய அரசுச் சட்டம்\n4. பிரிட்டிஷ் மேலாதிக்கத்தை முடிவுக்குக் கொண்டுவந்து இரண்டு சுதந்திர டொமினியன்களை உருவாக்கிய 1947 இந்திய சுதந்திரச் சட்டம்",
    [("A", "1 -> 3 -> 2 -> 4", "1 -> 3 -> 2 -> 4"), ("B", "2 -> 1 -> 3 -> 4", "2 -> 1 -> 3 -> 4"), ("C", "1 -> 2 -> 4 -> 3", "1 -> 2 -> 4 -> 3"), ("D", "1 -> 2 -> 3 -> 4", "1 -> 2 -> 3 -> 4")],
    "D",
    "Sequence: 1 (1773 Parliamentary supervision) -> 2 (1858 Crown takeover) -> 3 (1935 Federal Scheme) -> 4 (1947 Dominion Status & Independence). Sovereign transition timeline.",
    "வரிசை: 1 (1773 நாடாளுமன்றக் கண்காணிப்பு) -> 2 (1858 முடி ஆட்சி) -> 3 (1935 கூட்டாட்சி திட்டம்) -> 4 (1947 சுதந்திரம்).",
    {
        "A": {"en": "Incorrect. Crown Rule establishment (1858) was before 1935 Act.", "ta": "தவறு. முடி ஆட்சி உருவாக்கம் (1858) 1935 சட்டத்திற்கு முந்தியது."},
        "B": {"en": "Incorrect. Regulating Act 1773 (1) preceded Government of India Act 1858 (2).", "ta": "தவறு. 1773 ஒழுங்குமுறைச் சட்டம் (1) 1858 இந்திய அரசுச் சட்டத்திற்கு (2) முந்தியது."},
        "C": {"en": "Incorrect. 1935 Act (3) came before 1947 Independence Act (4).", "ta": "தவறு. 1935 சட்டம் (3) 1947 சுதந்திரச் சட்டத்திற்கு (4) முந்தியது."},
        "D": {"en": "Correct. 1 (1773) -> 2 (1858) -> 3 (1935) -> 4 (1947) forms the master timeline of constitutional history.", "ta": "சரி. 1 (1773) -> 2 (1858) -> 3 (1935) -> 4 (1947) அரசியலமைப்பு வரலாற்றின் முதன்மை காலவரிசையாகும்."}
    },
    "TNPSC Trap: Indian Independence Act 1947 resulted in the lapse of British Paramountcy over Indian Princely States.",
    "TNPSC பொறி: 1947 இந்திய சுதந்திரச் சட்டம் சுதேச சமஸ்தானங்களின் மீதான பிரிட்டிஷ் மேலாதிக்கம் (Paramountcy) ரத்தாக வழிகோலியது.",
    "The 1935 Act proposal for All-India Federation never came into operation as princely states did not join.",
    "சுதேச சமஸ்தானங்கள் இணையாததால் 1935 சட்டத்தின் அகில இந்திய கூட்டாட்சி திட்டம் நடைமுறைக்கு வரவில்லை.",
    ["Polity", "Historical Background", "Chronology", "Company to Crown", "Indian Independence"]
))

# Q29: Constitutional Evolution
q_list.append(make_q(
    29, "Hard", "Chronology",
    "Arrange the following British Parliamentary intervention acts in Indian constitutional evolution in chronological sequence:\n1. Amending Act of 1781 (Act of Settlement) removing executive actions from Supreme Court's oversight\n2. Pitt's India Act of 1784 establishing the dual system of control via Board of Control\n3. Indian Councils Act of 1892 introducing recommendations for non-official seats\n4. Government of India Act of 1919 introducing Dyarchy in provinces and central bicameralism",
    "இந்திய அரசியலமைப்பு வளர்ச்சியில் பிரிட்டிஷ் நாடாளுமன்றத்தின் பின்வரும் தலையீட்டுச் சட்டங்களை காலவரிசையில் அமைக்கவும்:\n1. உச்ச நீதிமன்றக் கண்காணிப்பிலிருந்து நிர்வாக நடவடிக்கைகளை விலக்கிய 1781 திருத்தச் சட்டம் (சீரமைப்புச் சட்டம்)\n2. கட்டுப்பாட்டு வாரியம் மூலம் இரட்டை நிர்வாக முறையை நிறுவிய 1784 பிட் இந்தியச் சட்டம்\n3. அதிகாரப்பூர்வமற்ற இடங்களுக்குப் பரிந்துரைகளை அறிமுகப்படுத்திய 1892 இந்தியக் கவுன்சில்கள் சட்டம்\n4. மாகாணங்களில் இரட்டை ஆட்சியையும் மத்தியில் இரு அவை முறையையும் கொண்டுவந்த 1919 இந்திய அரசுச் சட்டம்",
    [("A", "1 -> 2 -> 3 -> 4", "1 -> 2 -> 3 -> 4"), ("B", "2 -> 1 -> 3 -> 4", "2 -> 1 -> 3 -> 4"), ("C", "1 -> 3 -> 2 -> 4", "1 -> 3 -> 2 -> 4"), ("D", "1 -> 2 -> 4 -> 3", "1 -> 2 -> 4 -> 3")],
    "A",
    "Sequence: 1 (1781 Act of Settlement) -> 2 (1784 Pitt's India Act) -> 3 (1892 Indian Councils Act) -> 4 (1919 GOI Act). Intervention timeline.",
    "வரிசை: 1 (1781 சீரமைப்புச் சட்டம்) -> 2 (1784 பிட் இந்தியச் சட்டம்) -> 3 (1892 இந்தியக் கவுன்சில்கள் சட்டம்) -> 4 (1919 இந்திய அரசுச் சட்டம்).",
    {
        "A": {"en": "Correct. 1 (1781) -> 2 (1784) -> 3 (1892) -> 4 (1919) accurately follows chronological order of enactments.", "ta": "சரி. 1 (1781) -> 2 (1784) -> 3 (1892) -> 4 (1919) சட்ட இயற்றல்களின் காலவரிசையைத் துல்லியமாகப் பின்பற்றுகிறது."},
        "B": {"en": "Incorrect. Act of Settlement (1781) was passed before Pitt's India Act (1784).", "ta": "தவறு. சீரமைப்புச் சட்டம் (1781) பிட் இந்தியச் சட்டத்திற்கு (1784) முன்பே இயற்றப்பட்டது."},
        "C": {"en": "Incorrect. Pitt's India Act (1784) was enacted long before Indian Councils Act 1892 (3).", "ta": "தவறு. பிட் இந்தியச் சட்டம் (1784) 1892 இந்தியக் கவுன்சில்கள் சட்டத்திற்கு பல ஆண்டுகள் முந்தியது."},
        "D": {"en": "Incorrect. 1919 Act (4) was enacted after 1892 Act (3).", "ta": "தவறு. 1919 சட்டம் (4) 1892 சட்டத்திற்குப் (3) பின்னரே இயற்றப்பட்டது."}
    },
    "TNPSC Trap: Pitt's India Act 1784 declared Company's territories in India as 'British possessions in India' for the first time.",
    "TNPSC பொறி: 1784 பிட் இந்தியச் சட்டம் முதன்முறையாக இந்தியாவில் கம்பெனியின் நிலப்பரப்புகளை 'இந்தியாவில் உள்ள பிரிட்டிஷ் உடமைகள்' என அறிவித்தது.",
    "Act of Settlement 1781 exempted revenue matters and collection of revenues from Supreme Court jurisdiction.",
    "1781 சீரமைப்புச் சட்டம் வருவாய் விவகாரங்களையும் வசூலையும் உச்ச நீதிமன்ற அதிகார வரம்பிலிருந்து விலக்கியது.",
    ["Polity", "Historical Background", "Chronology", "Act of Settlement", "Pitts India Act"]
))

# Q30: Constitutional Evolution
q_list.append(make_q(
    30, "Hard", "Chronology",
    "Arrange the following key structural changes transitioning India from Company dual governance to a Federal structure:\n1. Establishment of Board of Control introducing Dual System of Control\n2. Open Competitive Examination for Indian Civil Services established by Charter Act\n3. Amalgamation of Supreme Court and Sadar Diwani Adalat under Indian High Courts Act\n4. Establishment of the Federal Court of India and Reserve Bank of India",
    "இந்தியாவை கம்பெனி இரட்டை நிர்வாகத்திலிருந்து கூட்டாட்சி அமைப்பிற்கு மாற்றிய பின்வரும் கட்டமைப்பு மாற்றங்களை காலவரிசையில் அமைக்கவும்:\n1. இரட்டை நிர்வாக முறையை அறிமுகப்படுத்தி கட்டுப்பாட்டு வாரியம் அமைத்தல்\n2. சாசனச் சட்டத்தின் மூலம் இந்திய சிவில் சர்வீஸ்க்கான திறந்தவெளி போட்டித் தேர்வு அமைக்கப்படல்\n3. இந்திய உயர் நீதிமன்றங்கள் சட்டத்தின் கீழ் உச்ச நீதிமன்றம் மற்றும் சதர் திவானி அதாலத் இணைப்பு\n4. இந்தியாவின் கூட்டாட்சி நீதிமன்றம் மற்றும் இந்திய ரிசர்வ் வங்கி அமைத்தல்",
    [("A", "1 -> 3 -> 2 -> 4", "1 -> 3 -> 2 -> 4"), ("B", "1 -> 2 -> 3 -> 4", "1 -> 2 -> 3 -> 4"), ("C", "2 -> 1 -> 3 -> 4", "2 -> 1 -> 3 -> 4"), ("D", "1 -> 2 -> 4 -> 3", "1 -> 2 -> 4 -> 3")],
    "B",
    "Sequence: 1 (1784 Board of Control) -> 2 (1853 ICS Open Competition) -> 3 (1861 High Courts Act amalgamating SC & Sadar Adalats) -> 4 (1935 Federal Court & RBI).",
    "வரிசை: 1 (1784 கட்டுப்பாட்டு வாரியம்) -> 2 (1853 போட்டித் தேர்வு) -> 3 (1861 உயர் நீதிமன்றங்கள் சட்டம்) -> 4 (1935 கூட்டாட்சி நீதிமன்றம் & ரிசர்வ் வங்கி).",
    {
        "A": {"en": "Incorrect. ICS Open Competition (1853) was established before High Courts Act (1861).", "ta": "தவறு. சிவில் சர்வீஸ் போட்டித் தேர்வு (1853) உயர் நீதிமன்றங்கள் சட்டத்திற்கு (1861) முந்தியது."},
        "B": {"en": "Correct. 1 (1784) -> 2 (1853) -> 3 (1861) -> 4 (1935) tracks master structural transition of state institutions.", "ta": "சரி. 1 (1784) -> 2 (1853) -> 3 (1861) -> 4 (1935) அரசின் முதன்மைக் கட்டமைப்பு மாற்றங்களை வரிசைப்படுத்துகிறது."},
        "C": {"en": "Incorrect. Board of Control (1784) was formed long before Charter Act 1853 (2).", "ta": "தவறு. கட்டுப்பாட்டு வாரியம் (1784) 1853 சாசனச் சட்டத்திற்குப் பல ஆண்டுகள் முந்தியது."},
        "D": {"en": "Incorrect. Federal Court & RBI (1935) came after 1861 High Courts Act (3).", "ta": "தவறு. கூட்டாட்சி நீதிமன்றம் & ரிசர்வ் வங்கி (1935) 1861 உயர் நீதிமன்றங்கள் சட்டத்திற்குப் பின்னரே வந்தன."}
    },
    "TNPSC Trap: Indian High Courts Act 1861 abolished Supreme Court of Calcutta and Sadar Adalats, amalgamating them into High Courts.",
    "TNPSC பொறி: 1861 இந்திய உயர் நீதிமன்றங்கள் சட்டம் கொல்கத்தா உச்ச நீதிமன்றத்தையும் சதர் அதாலத்துகளையும் ஒழித்து உயர் நீதிமன்றங்களாக இணைத்தது.",
    "The Federal Court established under GOI Act 1935 began functioning on October 1, 1937 with Sir Maurice Gwyer as Chief Justice.",
    "1935 சட்டத்தின் கீழ் அமைக்கப்பட்ட கூட்டாட்சி நீதிமன்றம் அக் 1, 1937-ல் சர் மொரிஸ் குவையர் தலைமை நீதிபதியாகக் கொண்டு செயல்படத் தொடங்கியது.",
    ["Polity", "Historical Background", "Chronology", "Federal System", "Structural Changes"]
))

output_dir = r"c:\Users\Home\Desktop\tnpsc_ai\data\questions\polity"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "historical_background_chronology.json")

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(q_list, f, ensure_ascii=False, indent=2)

print(f"SUCCESSFULLY GENERATED REPOSITORY AT: {output_path}")
print(f"TOTAL QUESTIONS: {len(q_list)}")
