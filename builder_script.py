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

print(f"Generated first 10 questions. Total now: {len(q_list)}")
