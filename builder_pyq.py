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
        "id": f"HB_PYQ_{id_num:03d}",
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
# 15 DIRECT PYQ STYLE (Q1 - Q15)
# ----------------------------------------------------

# Q1: Direct PYQ - Easy - Regulating Act 1773
q_list.append(make_q(
    1, "Easy", "Direct MCQ",
    "Which Act of the British Parliament introduced Parliamentary control over the East India Company's administration in India for the first time?",
    "இந்தியாவில் கிழக்கிந்திய கம்பெனியின் நிர்வாகத்தின் மீது முதன்முறையாக நாடாளுமன்றக் கட்டுப்பாட்டை அறிமுகப்படுத்திய பிரிட்டிஷ் நாடாளுமன்றச் சட்டம் எது?",
    [
        ("A", "Regulating Act of 1773", "1773 ஆம் ஆண்டின் ஒழுங்குமுறைச் சட்டம்"),
        ("B", "Pitt's India Act of 1784", "1784 ஆம் ஆண்டின் பிட் இந்தியச் சட்டம்"),
        ("C", "Charter Act of 1813", "1813 ஆம் ஆண்டின் சாசனச் சட்டம்"),
        ("D", "Government of India Act of 1858", "1858 ஆம் ஆண்டின் இந்திய அரசுச் சட்டம்")
    ],
    "A",
    "The Regulating Act of 1773 was the first step taken by the British Government to control and regulate the affairs of the East India Company in India.",
    "1773 ஆம் ஆண்டின் ஒழுங்குமுறைச் சட்டம் இந்தியாவில் கிழக்கிந்திய கம்பெனியின் விவகாரங்களைக் கட்டுப்படுத்தவும் ஒழுங்குபடுத்தவும் பிரிட்டிஷ் அரசாங்கம் எடுத்த முதல் படியாகும்.",
    {
        "A": {"en": "Correct. It recognized for the first time the political and administrative functions of the EIC.", "ta": "சரி. இது முதன்முறையாக கம்பெனியின் அரசியல் மற்றும் நிர்வாகப் பணிகளை அங்கீகரித்தது."},
        "B": {"en": "Incorrect. Pitt's India Act 1784 established the dual control system (Board of Control).", "ta": "தவறு. 1784 பிட் இந்தியச் சட்டம் இரட்டை நிர்வாக முறையை (கட்டுப்பாட்டு வாரியம்) நிறுவியது."},
        "C": {"en": "Incorrect. Charter Act 1813 abolished EIC trade monopoly except for tea and trade with China.", "ta": "தவறு. 1813 சாசனச் சட்டம் தேயிலை மற்றும் சீனா வர்த்தகம் தவிர்த்து வர்த்தக முற்றுரிமையை ஒழித்தது."},
        "D": {"en": "Incorrect. 1858 Act directly transferred administration to the Crown.", "ta": "தவறு. 1858 சட்டம் நிர்வாகத்தை நேரடியாக பிரிட்டிஷ் முடி ஆட்சிக்கு மாற்றியது."}
    },
    "TNPSC Trap: 1773 Act laid the foundation of central administration in India.",
    "TNPSC பொறி: 1773 சட்டம் இந்தியாவில் மத்திய நிர்வாகத்திற்கான அடிக்கல்லை நாட்டியது.",
    "Warren Hastings became the first Governor-General of Bengal under the 1773 Regulating Act.",
    "1773 ஒழுங்குமுறைச் சட்டத்தின் கீழ் வாரன் ஹேஸ்டிங்ஸ் வங்காளத்தின் முதல் கவர்னர்-ஜெனரலானார்.",
    ["Polity", "Historical Background", "Regulating Act 1773", "PYQ Style"], "Remember", 45
))

# Q2: Direct PYQ - Easy - Pitt's India Act 1784
q_list.append(make_q(
    2, "Easy", "Direct MCQ",
    "Under which Act was the 'Board of Control' created to manage the political affairs of the East India Company?",
    "கிழக்கிந்திய கம்பெனியின் அரசியல் விவகாரங்களை நிர்வகிப்பதற்காக 'கட்டுப்பாட்டு வாரியம்' (Board of Control) எந்தச் சட்டத்தின் கீழ் உருவாக்கப்பட்டது?",
    [
        ("A", "Regulating Act of 1773", "1773 ஆம் ஆண்டின் ஒழுங்குமுறைச் சட்டம்"),
        ("B", "Pitt's India Act of 1784", "1784 ஆம் ஆண்டின் பிட் இந்தியச் சட்டம்"),
        ("C", "Charter Act of 1793", "1793 ஆம் ஆண்டின் சாசனச் சட்டம்"),
        ("D", "Charter Act of 1833", "1833 ஆம் ஆண்டின் சாசனச் சட்டம்")
    ],
    "B",
    "Pitt's India Act of 1784 established a Board of Control to manage political affairs, while Court of Directors managed commercial affairs, establishing dual control.",
    "1784 ஆம் ஆண்டின் பிட் இந்தியச் சட்டம் அரசியல் விவகாரங்களை நிர்வகிக்க கட்டுப்பாட்டு வாரியத்தை நிறுவியது, இயக்குநர்கள் அவை வணிக விவகாரங்களை நிர்வகித்தது.",
    {
        "A": {"en": "Incorrect. 1773 Act retained only Court of Directors.", "ta": "தவறு. 1773 சட்டம் இயக்குநர்கள் அவையை மட்டுமே தக்கவைத்தது."},
        "B": {"en": "Correct. Pitt's India Act 1784 created Board of Control.", "ta": "சரி. 1784 பிட் இந்தியச் சட்டம் கட்டுப்பாட்டு வாரியத்தை உருவாக்கியது."},
        "C": {"en": "Incorrect. Charter Act 1793 extended company charter by 20 years.", "ta": "தவறு. 1793 சாசனச் சட்டம் கம்பெனி சாசனத்தை 20 ஆண்டுகள் நீட்டித்தது."},
        "D": {"en": "Incorrect. Charter Act 1833 ended commercial monopoly completely.", "ta": "தவறு. 1833 சாசனச் சட்டம் வணிக முற்றுரிமையை முற்றிலும் முடிவுக்குக் கொண்டுவந்தது."}
    },
    "TNPSC Trap: Board of Control = Political affairs; Court of Directors = Commercial affairs.",
    "TNPSC பொறி: கட்டுப்பாட்டு வாரியம் = அரசியல் விவகாரங்கள்; இயக்குநர்கள் அவை = வணிக விவகாரங்கள்.",
    "The 1784 Act first called EIC territories as 'British possessions in India'.",
    "1784 சட்டம் முதன்முறையாக கம்பெனி நிலப்பரப்புகளை 'இந்தியாவில் உள்ள பிரிட்டிஷ் உடமைகள்' என அழைத்தது.",
    ["Polity", "Historical Background", "Pitts India Act 1784", "Board of Control"], "Remember", 45
))

# Q3: Direct PYQ - Easy - Charter Act 1813
q_list.append(make_q(
    3, "Easy", "Direct MCQ",
    "Which Charter Act allocated an annual sum of One Lakh rupees for the promotion of education in India?",
    "இந்தியாவில் கல்வியை மேம்படுத்துவதற்காக ஆண்டுக்கு ஒரு லட்சம் ரூபாய் நிதியை ஒதுக்கிய சாசனச் சட்டம் எது?",
    [
        ("A", "Charter Act of 1793", "1793 ஆம் ஆண்டின் சாசனச் சட்டம்"),
        ("B", "Charter Act of 1813", "1813 ஆம் ஆண்டின் சாசனச் சட்டம்"),
        ("C", "Charter Act of 1833", "1833 ஆம் ஆண்டின் சாசனச் சட்டம்"),
        ("D", "Charter Act of 1853", "1853 ஆம் ஆண்டின் சாசனச் சட்டம்")
    ],
    "B",
    "The Charter Act of 1813 directed the East India Company to spend Rs 1 Lakh annually for encouraging education and literature in India.",
    "1813 சாசனச் சட்டம் இந்தியாவில் கல்வி மற்றும் இலக்கியத்தை ஊக்குவிக்க ஆண்டுக்கு 1 லட்சம் ரூபாய் செலவிட கிழக்கிந்திய கம்பெனிக்கு உத்தரவிட்டது.",
    {
        "A": {"en": "Incorrect. 1793 Act paid Board of Control salaries from Indian revenue.", "ta": "தவறு. 1793 சட்டம் இந்திய வருவாயிலிருந்து வாரியச் சம்பளத்தை வழங்கியது."},
        "B": {"en": "Correct. Charter Act 1813 introduced the Rs 1 Lakh education grant and allowed Christian missionaries.", "ta": "சரி. 1813 சாசனச் சட்டம் ரூ.1 லட்சம் கல்வி மானியத்தை அறிமுகப்படுத்தியதுடன் கிறித்துவ மிஷனரிகளை அனுமதித்தது."},
        "C": {"en": "Incorrect. 1833 Act made Governor-General of Bengal as GG of India.", "ta": "தவறு. 1833 சட்டம் வங்காள கவர்னர்-ஜெனரலை இந்தியாவின் கவர்னர்-ஜெனரலாக மாற்றியது."},
        "D": {"en": "Incorrect. 1853 Act introduced open competitive exams for ICS.", "ta": "தவறு. 1853 சட்டம் சிவில் சர்வீஸுக்கு திறந்தவெளி போட்டித் தேர்வை அறிமுகப்படுத்தியது."}
    },
    "TNPSC Trap: 1813 Act also allowed Christian Missionaries to enter India to spread religion.",
    "TNPSC பொறி: 1813 சட்டம் கிறித்துவ மிஷனரிகள் மதத்தைப் பரப்ப இந்தியாவிற்குள் நுழையவும் அனுமதித்தது.",
    "Charter Act 1813 ended EIC's trade monopoly in India except for trade in tea and trade with China.",
    "1813 சாசனச் சட்டம் தேயிலை மற்றும் சீனா வர்த்தகம் தவிர்த்து கம்பெனியின் வர்த்தக முற்றுரிமையை முடிவுக்குக் கொண்டுவந்தது.",
    ["Polity", "Historical Background", "Charter Act 1813", "Education Grant"], "Remember", 45
))

# Q4: Direct PYQ - Easy - Charter Act 1833
q_list.append(make_q(
    4, "Easy", "Direct MCQ",
    "Who was the first Governor-General of India designated under the Charter Act of 1833?",
    "1833 ஆம் ஆண்டின் சாசனச் சட்டத்தின் கீழ் நியமிக்கப்பட்ட இந்தியாவின் முதல் கவர்னர்-ஜெனரல் யார்?",
    [
        ("A", "Lord Warren Hastings", "லார்டு வாரன் ஹேஸ்டிங்ஸ்"),
        ("B", "Lord Cornwallis", "லார்டு கார்ன்வாலிஸ்"),
        ("C", "Lord William Bentinck", "லார்டு வில்லியம் பென்டிங்க்"),
        ("D", "Lord Canning", "லார்டு கேனிங்")
    ],
    "C",
    "Lord William Bentinck became the first Governor-General of India under the Charter Act of 1833, which re-designated Governor-General of Bengal as Governor-General of India.",
    "1833 சாசனச் சட்டத்தின் கீழ் லார்டு வில்லியம் பென்டிங்க் இந்தியாவின் முதல் கவர்னர்-ஜெனரலானார். இச்சட்டம் வங்காள கவர்னர்-ஜெனரலை இந்தியாவின் கவர்னர்-ஜெனரலாக மாற்றியது.",
    {
        "A": {"en": "Incorrect. Warren Hastings was the first Governor-General of Bengal (1773).", "ta": "தவறு. வாரன் ஹேஸ்டிங்ஸ் வங்காளத்தின் முதல் கவர்னர்-ஜெனரல் (1773)."},
        "B": {"en": "Incorrect. Lord Cornwallis was Governor-General of Bengal (1786).", "ta": "தவறு. லார்டு கார்ன்வாலிஸ் வங்காள கவர்னர்-ஜெனரலாக இருந்தார் (1786)."},
        "C": {"en": "Correct. Lord William Bentinck was the 1st Governor-General of India.", "ta": "சரி. லார்டு வில்லியம் பென்டிங்க் இந்தியாவின் 1வது கவர்னர்-ஜெனரலாவார்."},
        "D": {"en": "Incorrect. Lord Canning was the first Viceroy of India (1858).", "ta": "தவறு. லார்டு கேனிங் இந்தியாவின் முதல் வைஸ்ராய் (1858)."}
    },
    "TNPSC Trap: Distinguish between Governor-General of Bengal (1773 - Warren Hastings), Governor-General of India (1833 - William Bentinck), and Viceroy of India (1858 - Lord Canning).",
    "TNPSC பொறி: வங்காள கவர்னர்-ஜெனரல் (1773 - வாரன் ஹேஸ்டிங்ஸ்), இந்திய கவர்னர்-ஜெனரல் (1833 - வில்லியம் பென்டிங்க்), இந்திய வைஸ்ராய் (1858 - கேனிங்) ஆகியோரைத் தெளிவாக வேறுபடுத்த வேண்டும்.",
    "1833 Act completely ended EIC commercial functions, making it a purely administrative body.",
    "1833 சட்டம் கம்பெனியின் வர்த்தக நடவடிக்கைகளை முற்றிலும் முடிவுக்குக் கொண்டுவந்து அதை நிர்வாக அமைப்பாக மாற்றியது.",
    ["Polity", "Historical Background", "Charter Act 1833", "William Bentinck"], "Remember", 45
))

# Q5: Direct PYQ - Easy - Government of India Act 1858
q_list.append(make_q(
    5, "Easy", "Direct MCQ",
    "The Government of India Act of 1858 is officially known by which title?",
    "1858 ஆம் ஆண்டின் இந்திய அரசுச் சட்டம் அதிகாரப்பூர்வமாக எந்தத் தலைப்பில் அழைக்கப்படுகிறது?",
    [
        ("A", "Act of Settlement", "சீரமைப்புச் சட்டம்"),
        ("B", "Act for the Better Government of India", "இந்தியாவின் நல்லாட்சிக்கான சட்டம்"),
        ("C", "Indian Councils Act", "இந்தியக் கவுன்சில்கள் சட்டம்"),
        ("D", "Indian Independence Act", "இந்திய சுதந்திரச் சட்டம்")
    ],
    "B",
    "The Government of India Act 1858 was enacted after the 1857 Revolt and was officially titled the 'Act for the Better Government of India'.",
    "1857 பெரும் புரட்சிக்குப் பிறகு இயற்றப்பட்ட 1858 இந்திய அரசுச் சட்டம் அதிகாரப்பூர்வமாக 'இந்தியாவின் நல்லாட்சிக்கான சட்டம்' என்று அழைக்கப்பட்டது.",
    {
        "A": {"en": "Incorrect. Act of Settlement refers to the Amending Act of 1781.", "ta": "தவறு. சீரமைப்புச் சட்டம் என்பது 1781 திருத்தச் சட்டத்தைக் குறிக்கிறது."},
        "B": {"en": "Correct. Officially titled 'Act for the Better Government of India'.", "ta": "சரி. அதிகாரப்பூர்வத் தலைப்பு 'இந்தியாவின் நல்லாட்சிக்கான சட்டம்' என்பதாகும்."},
        "C": {"en": "Incorrect. Indian Councils Acts were passed in 1861, 1892, 1909.", "ta": "தவறு. இந்தியக் கவுன்சில்கள் சட்டங்கள் 1861, 1892, 1909 ஆகிய ஆண்டுகளில் இயற்றப்பட்டன."},
        "D": {"en": "Incorrect. Indian Independence Act was passed in 1947.", "ta": "தவறு. இந்திய சுதந்திரச் சட்டம் 1947-ல் இயற்றப்பட்டது."}
    },
    "TNPSC Trap: 1858 Act abolished the Board of Control and Court of Directors, vesting authority in Secretary of State.",
    "TNPSC பொறி: 1858 சட்டம் கட்டுப்பாட்டு வாரியம் மற்றும் இயக்குநர்கள் அவையை ஒழித்து அதிகாரங்களை அரசுச் செயலரிடம் ஒப்படைத்தது.",
    "Lord Canning became the first Viceroy of India under the 1858 Act.",
    "1858 சட்டத்தின் கீழ் லார்டு கேனிங் இந்தியாவின் முதல் வைஸ்ராயானார்.",
    ["Polity", "Historical Background", "GOI Act 1858", "Better Government Act"], "Remember", 45
))

# Q6: Direct PYQ - Easy - Indian Councils Act 1861
q_list.append(make_q(
    6, "Easy", "Direct MCQ",
    "Under which Act was statutory recognition given to the Portfolio System introduced by Lord Canning?",
    "லார்டு கேனிங் அறிமுகப்படுத்திய 'இலாகா முறைக்கு' (Portfolio System) எந்தச் சட்டத்தின் கீழ் சட்டப்பூர்வ அங்கீகாரம் வழங்கப்பட்டது?",
    [
        ("A", "Charter Act of 1853", "1853 ஆம் ஆண்டின் சாசனச் சட்டம்"),
        ("B", "Government of India Act of 1858", "1858 ஆம் ஆண்டின் இந்திய அரசுச் சட்டம்"),
        ("C", "Indian Councils Act of 1861", "1861 ஆம் ஆண்டின் இந்தியக் கவுன்சில்கள் சட்டம்"),
        ("D", "Indian Councils Act of 1892", "1892 ஆம் ஆண்டின் இந்தியக் கவுன்சில்கள் சட்டம்")
    ],
    "C",
    "The Indian Councils Act of 1861 gave statutory recognition to the portfolio system introduced by Lord Canning in 1859.",
    "1861 ஆம் ஆண்டின் இந்தியக் கவுன்சில்கள் சட்டம் 1859-ல் லார்டு கேனிங் அறிமுகப்படுத்திய இலாகா முறைக்குச் சட்டப்பூர்வ அங்கீகாரம் அளித்தது.",
    {
        "A": {"en": "Incorrect. 1853 Act created Central Legislative Council.", "ta": "தவறு. 1853 சட்டம் மத்திய சட்ட மேலவையை உருவாக்கியது."},
        "B": {"en": "Incorrect. 1858 Act transferred power to British Crown.", "ta": "தவறு. 1858 சட்டம் அதிகாரத்தை பிரிட்டிஷ் முடிக்கு மாற்றியது."},
        "C": {"en": "Correct. Indian Councils Act 1861 gave statutory backing to portfolio system.", "ta": "சரி. 1861 இந்தியக் கவுன்சில்கள் சட்டம் இலாகா முறைக்கு சட்டப்பூர்வ அங்கீகாரம் அளித்தது."},
        "D": {"en": "Incorrect. 1892 Act expanded budget discussion rights.", "ta": "தவறு. 1892 சட்டம் பட்ஜெட் விவாத உரிமைகளை விரிவாக்கியது."}
    },
    "TNPSC Trap: Lord Canning introduced portfolio system informally in 1859; statutory recognition came in 1861 Act.",
    "TNPSC பொறி: லார்டு கேனிங் இலாகா முறையை 1859-ல் முறைசாரா அறிமுகப்படுத்தினார்; 1861 சட்டமே அதற்குச் சட்டப்பூர்வ அங்கீகாரம் அளித்தது.",
    "The 1861 Act also restored legislative powers to Bombay and Madras Presidencies.",
    "1861 சட்டம் பம்பாய் மற்றும் மதராஸ் மாகாணங்களுக்கு சட்ட அதிகாரங்களை மீட்டளித்தது.",
    ["Polity", "Historical Background", "Indian Councils Act 1861", "Portfolio System"], "Remember", 45
))

# Q7: Direct PYQ - Easy - Indian Councils Act 1909
q_list.append(make_q(
    7, "Easy", "Direct MCQ",
    "Which Act introduced separate electorates for Muslims for the first time in British India?",
    "பிரிட்டிஷ் இந்தியாவில் முதன்முறையாக முஸ்லிம்களுக்கு தனித் தொகுதிகளை அறிமுகப்படுத்திய சட்டம் எது?",
    [
        ("A", "Indian Councils Act of 1892", "1892 ஆம் ஆண்டின் இந்தியக் கவுன்சில்கள் சட்டம்"),
        ("B", "Indian Councils Act of 1909", "1909 ஆம் ஆண்டின் இந்தியக் கவுன்சில்கள் சட்டம்"),
        ("C", "Government of India Act of 1919", "1919 ஆம் ஆண்டின் இந்திய அரசுச் சட்டம்"),
        ("D", "Government of India Act of 1935", "1935 ஆம் ஆண்டின் இந்திய அரசுச் சட்டம்")
    ],
    "B",
    "The Indian Councils Act of 1909 (Morley-Minto Reforms) introduced a system of communal representation for Muslims by accepting separate electorates.",
    "1909 இந்தியக் கவுன்சில்கள் சட்டம் (மார்லி-மிண்டோ சீர்திருத்தங்கள்) தனித் தொகுதிகளை ஏற்று முஸ்லிம்களுக்கு வகுப்புவாதப் பிரதிநிதித்துவ முறையை அறிமுகப்படுத்தியது.",
    {
        "A": {"en": "Incorrect. 1892 Act introduced indirect elections element.", "ta": "தவறு. 1892 சட்டம் மறைமுகத் தேர்தல் முறையை அறிமுகப்படுத்தியது."},
        "B": {"en": "Correct. Morley-Minto Reforms (1909) introduced separate electorates for Muslims.", "ta": "சரி. மார்லி-மிண்டோ சீர்திருத்தங்கள் (1909) முஸ்லிம்களுக்கு தனித் தொகுதிகளை அறிமுகப்படுத்தின."},
        "C": {"en": "Incorrect. 1919 Act extended separate electorates to Sikhs, Christians, Anglo-Indians.", "ta": "தவறு. 1919 சட்டம் தனித் தொகுதிகளை சீக்கியர்கள், கிறிஸ்தவர்கள், ஆங்லோ-இந்தியர்களுக்கு நீட்டித்தது."},
        "D": {"en": "Incorrect. 1935 Act extended separate electorates to depressed classes, women, labor.", "ta": "தவறு. 1935 சட்டம் தனித் தொகுதிகளை ஒடுக்கப்பட்டோர், பெண்கள், தொழிலாளர்களுக்கு நீட்டித்தது."}
    },
    "TNPSC Trap: Lord Minto was known as the 'Father of Communal Electorate'.",
    "TNPSC பொறி: லார்டு மிண்டோ 'வகுப்புவாதத் தொகுதிகளின் தந்தை' என அழைக்கப்பட்டார்.",
    "1909 Act also allowed Satyendra Prasanna Sinha to become the first Indian to join Viceroy's Executive Council.",
    "1909 சட்டம் சத்யேந்திர பிரசன்னா சின்காவை வைஸ்ராயின் நிர்வாகக் குழுவில் சேர்ந்த முதல் இந்தியராக்கியது.",
    ["Polity", "Historical Background", "Morley Minto 1909", "Separate Electorate"], "Remember", 45
))

# Q8: Direct PYQ - Easy - Government of India Act 1919
q_list.append(make_q(
    8, "Easy", "Direct MCQ",
    "The system of Dyarchy in provincial governments was introduced by which Act?",
    "மாகாண அரசுகளில் இரட்டை ஆட்சி முறை (Dyarchy) எந்தச் சட்டத்தின் மூலம் அறிமுகப்படுத்தப்பட்டது?",
    [
        ("A", "Indian Councils Act of 1909", "1909 ஆம் ஆண்டின் இந்தியக் கவுன்சில்கள் சட்டம்"),
        ("B", "Government of India Act of 1919", "1919 ஆம் ஆண்டின் இந்திய அரசுச் சட்டம்"),
        ("C", "Government of India Act of 1935", "1935 ஆம் ஆண்டின் இந்திய அரசுச் சட்டம்"),
        ("D", "Indian Independence Act of 1947", "1947 ஆம் ஆண்டின் இந்திய சுதந்திரச் சட்டம்")
    ],
    "B",
    "The Government of India Act of 1919 (Montagu-Chelmsford Reforms) introduced Dyarchy in provinces by dividing provincial subjects into Reserved and Transferred.",
    "1919 இந்திய அரசுச் சட்டம் (மாண்டேகு-செம்ஸ்ஃபோர்டு சீர்திருத்தங்கள்) மாகாணத் துறைகளை ஒதுக்கப்பட்டவை மற்றும் மாற்றப்பட்டவை எனப் பிரித்து இரட்டை ஆட்சியை அறிமுகப்படுத்தியது.",
    {
        "A": {"en": "Incorrect. 1909 Act introduced separate electorates for Muslims.", "ta": "தவறு. 1909 சட்டம் முஸ்லிம்களுக்கு தனித் தொகுதிகளை அறிமுகப்படுத்தியது."},
        "B": {"en": "Correct. GOI Act 1919 introduced Dyarchy in provinces.", "ta": "சரி. 1919 இந்திய அரசுச் சட்டம் மாகாணங்களில் இரட்டை ஆட்சியை அறிமுகப்படுத்தியது."},
        "C": {"en": "Incorrect. 1935 Act abolished provincial dyarchy and introduced Provincial Autonomy.", "ta": "தவறு. 1935 சட்டம் மாகாண இரட்டை ஆட்சியை நீக்கி மாகாண தன்னாட்சியை அறிமுகப்படுத்தியது."},
        "D": {"en": "Incorrect. 1947 Act granted independence to India.", "ta": "தவறு. 1947 சட்டம் இந்தியாவுக்கு சுதந்திரம் வழங்கியது."}
    },
    "TNPSC Trap: Dyarchy was introduced in Provinces by 1919 Act and abolished in Provinces by 1935 Act.",
    "TNPSC பொறி: இரட்டை ஆட்சி 1919 சட்டத்தால் மாகாணங்களில் கொண்டுவரப்பட்டு, 1935 சட்டத்தால் மாகாணங்களில் ஒழிக்கப்பட்டது.",
    "The word 'Dyarchy' is derived from the Greek word 'di-arche' meaning double rule.",
    "'டையார்கி' என்ற சொல் 'டை-ஆர்க்கி' என்ற கிரேக்கச் சொல்லிலிருந்து உருவானது, இதன் பொருள் இரட்டை ஆட்சி என்பதாகும்.",
    ["Polity", "Historical Background", "GOI Act 1919", "Dyarchy"], "Remember", 45
))

# Q9: Direct PYQ - Easy - Government of India Act 1935
q_list.append(make_q(
    9, "Easy", "Direct MCQ",
    "Which Act provided for the establishment of an All-India Federation comprising British Indian provinces and Princely States?",
    "பிரிட்டிஷ் இந்திய மாகாணங்கள் மற்றும் சுதேச சமஸ்தானங்களை உள்ளடக்கிய அகில இந்திய கூட்டாட்சியை நிறுவ வழிவகை செய்த சட்டம் எது?",
    [
        ("A", "Government of India Act of 1919", "1919 ஆம் ஆண்டின் இந்திய அரசுச் சட்டம்"),
        ("B", "Government of India Act of 1935", "1935 ஆம் ஆண்டின் இந்திய அரசுச் சட்டம்"),
        ("C", "Indian Independence Act of 1947", "1947 ஆம் ஆண்டின் இந்திய சுதந்திரச் சட்டம்"),
        ("D", "Regulating Act of 1773", "1773 ஆம் ஆண்டின் ஒழுங்குமுறைச் சட்டம்")
    ],
    "B",
    "The Government of India Act of 1935 provided for the establishment of an All-India Federation consisting of provinces and princely states as units.",
    "1935 ஆம் ஆண்டின் இந்திய அரசுச் சட்டம் மாகாணங்கள் மற்றும் சுதேச சமஸ்தானங்களை அலகுகளாகக் கொண்டு அகில இந்திய கூட்டாட்சியை நிறுவ வழிவகை செய்தது.",
    {
        "A": {"en": "Incorrect. 1919 Act introduced central bicameralism and provincial dyarchy.", "ta": "தவறு. 1919 சட்டம் மத்திய இரு அவை முறையையும் மாகாண இரட்டை ஆட்சியையும் அறிமுகப்படுத்தியது."},
        "B": {"en": "Correct. GOI Act 1935 proposed All-India Federation (though it never came into operation).", "ta": "சரி. 1935 இந்திய அரசுச் சட்டம் அகில இந்திய கூட்டாட்சியை முன்மொழிந்தது (ஆனால் நடைமுறைக்கு வரவில்லை)."},
        "C": {"en": "Incorrect. 1947 Act created two separate dominions (India & Pakistan).", "ta": "தவறு. 1947 சட்டம் இரண்டு தனி டொமினியன்களை உருவாக்கியது."},
        "D": {"en": "Incorrect. 1773 Act regulated EIC administration.", "ta": "தவறு. 1773 சட்டம் கம்பெனி நிர்வாகத்தை ஒழுங்குபடுத்தியது."}
    },
    "TNPSC Trap: The All-India Federation proposed in 1935 never came into being because princely states did not join.",
    "TNPSC பொறி: சுதேச சமஸ்தானங்கள் இணையாததால் 1935-ல் முன்மொழியப்பட்ட அகில இந்திய கூட்டாட்சி ஒருபோதும் நடைமுறைக்கு வரவில்லை.",
    "GOI Act 1935 divided powers into 3 lists: Federal List (59 items), Provincial List (54 items), Concurrent List (36 items).",
    "1935 சட்டம் அதிகாரங்களை 3 பட்டியல்களாகப் பிரித்தது: கூட்டாட்சி (59), மாகாண (54), பொதுப் பட்டியல் (36).",
    ["Polity", "Historical Background", "GOI Act 1935", "All India Federation"], "Remember", 45
))

# Q10: Direct PYQ - Easy - Indian Independence Act 1947
q_list.append(make_q(
    10, "Easy", "Direct MCQ",
    "Under the Indian Independence Act of 1947, who was appointed as the first Governor-General of independent India?",
    "1947 இந்திய சுதந்திரச் சட்டத்தின் கீழ், சுதந்திர இந்தியாவின் முதல் கவர்னர்-ஜெனரலாக நியமிக்கப்பட்டவர் யார்?",
    [
        ("A", "C. Rajagopalachari", "சி. ராஜகோபாலாச்சாரி"),
        ("B", "Lord Mountbatten", "லார்டு மவுண்ட்பேட்டன்"),
        ("C", "Dr. Rajendra Prasad", "டாக்டர் ராஜேந்திர பிரசாத்"),
        ("D", "Jawaharlal Nehru", "ஜவாஹர்லால் நேரு")
    ],
    "B",
    "Lord Mountbatten became the first Governor-General of independent India, while Jawaharlal Nehru became the first Prime Minister.",
    "லார்டு மவுண்ட்பேட்டன் சுதந்திர இந்தியாவின் முதல் கவர்னர்-ஜெனரலானார்; ஜவாஹர்லால் நேரு முதல் பிரதமரானார்.",
    {
        "A": {"en": "Incorrect. C. Rajagopalachari was the first Indian Governor-General (1948-1950).", "ta": "தவறு. சி. ராஜகோபாலாச்சாரி முதல் இந்திய கவர்னர்-ஜெனரலாவார் (1948-1950)."},
        "B": {"en": "Correct. Lord Mountbatten served as 1st Governor-General of independent India.", "ta": "சரி. லார்டு மவுண்ட்பேட்டன் சுதந்திர இந்தியாவின் 1வது கவர்னர்-ஜெனரலாகப் பணியாற்றினார்."},
        "C": {"en": "Incorrect. Dr. Rajendra Prasad was the first President of India (1950).", "ta": "தவறு. டாக்டர் ராஜேந்திர பிரசாத் இந்தியாவின் முதல் குடியரசுத் தலைவராவார் (1950)."},
        "D": {"en": "Incorrect. Jawaharlal Nehru was the first Prime Minister.", "ta": "தவறு. ஜவாஹர்லால் நேரு முதல் பிரதமராவார்."}
    },
    "TNPSC Trap: Lord Mountbatten was 1st Governor-General of Independent India; C. Rajagopalachari was 1st Indian Governor-General.",
    "TNPSC பொறி: லார்டு மவுண்ட்பேட்டன் சுதந்திர இந்தியாவின் 1வது கவர்னர்-ஜெனரல்; சி. ராஜகோபாலாச்சாரி 1வது இந்திய கவர்னர்-ஜெனரல்.",
    "Indian Independence Act received Royal Assent on July 18, 1947 and came into force on August 15, 1947.",
    "இந்திய சுதந்திரச் சட்டம் 1947 ஜூலை 18 அன்று மன்னரின் ஒப்புதலைப் பெற்று ஆகஸ்ட் 15, 1947 அன்று அமலுக்கு வந்தது.",
    ["Polity", "Historical Background", "Independence Act 1947", "Mountbatten"], "Remember", 45
))

# Q11: Direct PYQ - Medium - Amending Act 1781
q_list.append(make_q(
    11, "Medium", "Direct MCQ",
    "The Amending Act of 1781 was passed by the British Parliament to remedy the defects of which of the following Acts?",
    "1781 ஆம் ஆண்டின் திருத்தச் சட்டம் பின்வரும் எந்தச் சட்டத்தின் குறைபாடுகளை நிவர்த்தி செய்வதற்காக பிரிட்டிஷ் நாடாளுமன்றத்தால் இயற்றப்பட்டது?",
    [
        ("A", "Regulating Act of 1773", "1773 ஆம் ஆண்டின் ஒழுங்குமுறைச் சட்டம்"),
        ("B", "Pitt's India Act of 1784", "1784 ஆம் ஆண்டின் பிட் இந்தியச் சட்டம்"),
        ("C", "Charter Act of 1793", "1793 ஆம் ஆண்டின் சாசனச் சட்டம்"),
        ("D", "Charter Act of 1813", "1813 ஆம் ஆண்டின் சாசனச் சட்டம்")
    ],
    "A",
    "The Amending Act of 1781 (also known as the Act of Settlement) was passed to rectify jurisdictional defects and conflicts caused by the Regulating Act of 1773.",
    "1781 ஆம் ஆண்டின் திருத்தச் சட்டம் (சீர்திருத்தச் சட்டம்) 1773 ஒழுங்குமுறைச் சட்டத்தால் ஏற்பட்ட அதிகார வரம்பு குறைபாடுகளை சரிசெய்ய இயற்றப்பட்டது.",
    {
        "A": {"en": "Correct. It exempted Governor-General and revenue matters from Supreme Court jurisdiction.", "ta": "சரி. இது கவர்னர்-ஜெனரல் மற்றும் வருவாய் விவகாரங்களை உச்ச நீதிமன்ற அதிகார வரம்பிலிருந்து விலக்கியது."},
        "B": {"en": "Incorrect. Pitt's India Act was passed in 1784, after 1781.", "ta": "தவறு. பிட் இந்தியச் சட்டம் 1781-க்கு பின் 1784-ல் இயற்றப்பட்டது."},
        "C": {"en": "Incorrect. Charter Act of 1793 was passed 12 years later.", "ta": "தவறு. 1793 சாசனச் சட்டம் 12 ஆண்டுகளுக்குப் பின் இயற்றப்பட்டது."},
        "D": {"en": "Incorrect. Charter Act of 1813 ended commercial trade monopoly.", "ta": "தவறு. 1813 சாசனச் சட்டம் வணிக முற்றுரிமையை ஒழித்தது."}
    },
    "TNPSC Trap: Amending Act 1781 is officially known as 'Act of Settlement'.",
    "TNPSC பொறி: 1781 திருத்தச் சட்டம் அதிகாரப்பூர்வமாக 'சீரமைப்புச் சட்டம்' (Act of Settlement) என அழைக்கப்படுகிறது.",
    "1781 Act exempted official actions of servants of the Company from Supreme Court jurisdiction.",
    "1781 சட்டம் கம்பெனி ஊழியர்களின் அதிகாரப்பூர்வ நடவடிக்கைகளை உச்ச நீதிமன்ற வரம்பிலிருந்து விலக்கியது.",
    ["Polity", "Historical Background", "Act of Settlement 1781", "Regulating Act"], "Understand", 60
))

# Q12: Direct PYQ - Medium - Charter Act 1853
q_list.append(make_q(
    12, "Medium", "Direct MCQ",
    "Which Committee was appointed in 1854 to implement the open competition system for the Indian Civil Service under the Charter Act of 1853?",
    "1853 ஆம் ஆண்டின் சாசனச் சட்டத்தின் கீழ் இந்திய சிவில் சர்வீஸுக்கான திறந்தவெளி போட்டித் தேர்வு முறையை அமல்படுத்துவதற்காக 1854-ல் நியமிக்கப்பட்ட குழு எது?",
    [
        ("A", "Hunter Committee", "ஹண்டர் குழு"),
        ("B", "Macaulay Committee", "மெக்காலே குழு"),
        ("C", "Aitchison Commission", "அட்சிகன் ஆணையம்"),
        ("D", "Islington Commission", "இஸ்லிங்டன் ஆணையம்")
    ],
    "B",
    "The Macaulay Committee (the Committee on the Indian Civil Service) was appointed in 1854 pursuant to the Charter Act of 1853 to frame open competition rules for ICS.",
    "1853 சாசனச் சட்டத்தைத் தொடர்ந்து, இந்திய சிவில் சர்வீஸுக்கான திறந்தவெளி போட்டித் தேர்வு விதிகளை உருவாக்க 1854-ல் மெக்காலே குழு நியமிக்கப்பட்டது.",
    {
        "A": {"en": "Incorrect. Hunter Committee investigated the Jallianwala Bagh massacre (1919) or education (1882).", "ta": "தவறு. ஹண்டர் குழு ஜாலியன்வாலா பாக் படுகொலை (1919) அல்லது கல்வியை (1882) ஆராய்ந்தது."},
        "B": {"en": "Correct. Macaulay Committee (1854) framed rules for open ICS examination.", "ta": "சரி. மெக்காலே குழு (1854) திறந்தவெளி சிவில் சர்வீஸ் தேர்வுகளுக்கான விதிகளைத் தயாரித்தது."},
        "C": {"en": "Incorrect. Aitchison Commission was appointed in 1886.", "ta": "தவறு. அட்சிகன் ஆணையம் 1886-ல் நியமிக்கப்பட்டது."},
        "D": {"en": "Incorrect. Islington Commission was appointed in 1912.", "ta": "தவறு. இஸ்லிங்டன் ஆணையம் 1912-ல் நியமிக்கப்பட்டது."}
    },
    "TNPSC Trap: Charter Act 1853 threw open Civil Services to Indians for the first time via open competition.",
    "TNPSC பொறி: 1853 சாசனச் சட்டம் திறந்தவெளி போட்டித் தேர்வு மூலம் முதன்முறையாக இந்தியர்களுக்கு சிவில் சர்வீஸ் கதவுகளைத் திறந்தது.",
    "Charter Act 1853 separated executive and legislative functions of the Governor-General's Council.",
    "1853 சாசனச் சட்டம் கவர்னர்-ஜெனரல் கவுன்சிலின் நிர்வாக மற்றும் சட்டப் பணிகளைப் பிரித்தது.",
    ["Polity", "Historical Background", "Macaulay Committee", "Civil Services"], "Understand", 60
))

# Q13: Direct PYQ - Medium - Indian Councils Act 1892
q_list.append(make_q(
    13, "Medium", "Direct MCQ",
    "Which of the following functions was conferred upon Legislative Councils by the Indian Councils Act of 1892?",
    "1892 ஆம் ஆண்டின் இந்தியக் கவுன்சில்கள் சட்டத்தின் மூலம் சட்ட மேலவைகளுக்கு வழங்கப்பட்ட அதிகாரம் எது?",
    [
        ("A", "Power to vote on demands for grants", "மானியக் கோரிக்கைகள் மீது வாக்களிக்கும் அதிகாரம்"),
        ("B", "Power to discuss the budget and address questions to the executive", "பட்ஜெட்டை விவாதிக்கவும் நிர்வாகத்திடம் கேள்விகள் கேட்கவும் அதிகாரம்"),
        ("C", "Power to ask supplementary questions on budget", "பட்ஜெட் மீது துணைக் கேள்விகள் கேட்கும் அதிகாரம்"),
        ("D", "Power to move resolutions on the budget", "பட்ஜெட் மீது தீர்மானங்கள் கொண்டுவரும் அதிகாரம்")
    ],
    "B",
    "The Indian Councils Act of 1892 gave legislative council members the right to discuss the budget and address questions to the executive (with 6 days prior notice).",
    "1892 இந்தியக் கவுன்சில்கள் சட்டம் உறுப்பினர்களுக்கு பட்ஜெட்டை விவாதிக்கவும் நிர்வாகத்திடம் கேள்விகள் கேட்கவும் உரிமை அளித்தது.",
    {
        "A": {"en": "Incorrect. Voting on budget demands was not allowed in 1892.", "ta": "தவறு. 1892-ல் பட்ஜெட் மானியங்கள் மீது வாக்களிக்க அனுமதி இல்லை."},
        "B": {"en": "Correct. Members got the right to discuss budget and ask questions.", "ta": "சரி. உறுப்பினர்கள் பட்ஜெட்டை விவாதிக்கவும் கேள்விகள் கேட்கவும் உரிமை பெற்றனர்."},
        "C": {"en": "Incorrect. Supplementary questions were introduced later in 1909.", "ta": "தவறு. துணைக் கேள்விகள் 1909-ல் தான் அறிமுகப்படுத்தப்பட்டன."},
        "D": {"en": "Incorrect. Resolutions on budget were allowed in 1909.", "ta": "தவறு. பட்ஜெட் மீதான தீர்மானங்கள் 1909-ல் அனுமதிக்கப்பட்டன."}
    },
    "TNPSC Trap: 1892 Act allowed discussion of budget, but NO voting and NO supplementary questions.",
    "TNPSC பொறி: 1892 சட்டம் பட்ஜெட் விவாதத்தை மட்டுமே அனுமதித்தது; வாக்களிப்பு மற்றும் துணைக் கேள்விகளுக்கு அனுமதி இல்லை.",
    "1892 Act also introduced indirect nomination based on recommendations of local bodies.",
    "1892 சட்டம் உள்ளாட்சி அமைப்புகளின் பரிந்துரையின் பேரில் மறைமுக நியமனத்தையும் அறிமுகப்படுத்தியது.",
    ["Polity", "Historical Background", "Indian Councils Act 1892", "Budget Discussion"], "Understand", 60
))

# Q14: Direct PYQ - Medium - Simon Commission
q_list.append(make_q(
    14, "Medium", "Direct MCQ",
    "Why was the Indian National Congress opposed to the Statutory Commission (Simon Commission) appointed in November 1927?",
    "நவம்பர் 1927-ல் நியமிக்கப்பட்ட சட்டப்பூர்வ ஆணையத்தை (சைமன் குழு) இந்திய தேசிய காங்கிரஸ் ஏன் எதிர்த்தது?",
    [
        ("A", "It recommended the immediate partition of India", "இது இந்தியாவின் உடனடிப் பிரிவினையை முன்மொழிந்தது"),
        ("B", "All seven members of the commission were British, excluding Indians", "ஆணையத்தின் ஏழு உறுப்பினர்களும் பிரிட்டிஷாராக இருந்தனர், இந்தியர்கள் சேர்க்கப்படவில்லை"),
        ("C", "It rejected the concept of Provincial Autonomy", "இது மாகாண தன்னாட்சி கருத்தை நிராகரித்தது"),
        ("D", "It abolished separate electorates for Muslims", "இது முஸ்லிம்களுக்கான தனித் தொகுதிகளை ஒழித்தது")
    ],
    "B",
    "The Simon Commission was boycotted by all parties, including INC, because all its 7 members were Englishmen and no Indian was included.",
    "சைமன் குழுவின் 7 உறுப்பினர்களும் ஆங்கிலேயர்களாக இருந்ததாலும், இந்தியர்கள் எவரும் சேர்க்கப்படாததாலும் அனைத்துக் கட்சிகளாலும் அக்குழு புறக்கணிக்கப்பட்டது.",
    {
        "A": {"en": "Incorrect. Simon Commission did not recommend immediate partition.", "ta": "தவறு. சைமன் குழு உடனடிப் பிரிவினையை முன்மொழியவில்லை."},
        "B": {"en": "Correct. All-white composition sparked nationwide boycott.", "ta": "சரி. அனைத்து உறுப்பினர்களும் வெள்ளையர்களாக இருந்தது நாடு தழுவிய எதிர்ப்பை உருவாக்கியது."},
        "C": {"en": "Incorrect. Simon Commission actually recommended abolition of dyarchy and grant of provincial autonomy.", "ta": "தவறு. சைமன் குழு இரட்டை ஆட்சியை நீக்கி மாகாண தன்னாட்சியைப் பரிந்துரைத்தது."},
        "D": {"en": "Incorrect. It recommended continuation of communal electorates.", "ta": "தவறு. இது வகுப்புவாதத் தொகுதிகள் தொடரப் பரிந்துரைத்தது."}
    },
    "TNPSC Trap: Simon Commission was appointed 2 years ahead of schedule (1927 instead of 10 years after 1919 Act).",
    "TNPSC பொறி: 1919 சட்டத்திற்கு 10 ஆண்டுகளுக்குப் பின் அமைய வேண்டிய சைமன் குழு 2 ஆண்டுகளுக்கு முன்பே (1927) அமைக்கப்பட்டது.",
    "The Simon Commission submitted its report in May 1930.",
    "சைமன் குழு தனது அறிக்கையை மே 1930-ல் சமர்ப்பித்தது.",
    ["Polity", "Historical Background", "Simon Commission", "1927 Commission"], "Understand", 60
))

# Q15: Direct PYQ - Medium - GOI Act 1935 RBI
q_list.append(make_q(
    15, "Medium", "Direct MCQ",
    "Which institution was established under the provisions of the Government of India Act 1935 to control the currency and credit of India?",
    "இந்தியாவின் நாணயம் மற்றும் கடனைக் கட்டுப்படுத்துவதற்காக 1935 இந்திய அரசுச் சட்டத்தின் விதிகளின் கீழ் நிறுவப்பட்ட அமைப்பு எது?",
    [
        ("A", "Imperial Bank of India", "இந்திய இம்பீரியல் வங்கி"),
        ("B", "Reserve Bank of India", "இந்திய ரிசர்வ் வங்கி"),
        ("C", "Federal Bank of India", "இந்திய ஃபெடரல் வங்கி"),
        ("D", "State Bank of India", "பாரத ஸ்டேட் வங்கி")
    ],
    "B",
    "The Government of India Act of 1935 provided for the establishment of the Reserve Bank of India to regulate currency and credit in the country.",
    "1935 ஆம் ஆண்டின் இந்திய அரசுச் சட்டம் நாட்டில் நாணயம் மற்றும் கடனைக் கட்டுப்படுத்துவதற்காக இந்திய ரிசர்வ் வங்கியை நிறுவ வழிவகை செய்தது.",
    {
        "A": {"en": "Incorrect. Imperial Bank was created in 1921 by merging Presidency Banks.", "ta": "தவறு. இம்பீரியல் வங்கி 1921-ல் மாகாண வங்கிகளை இணைத்து உருவாக்கப்பட்டது."},
        "B": {"en": "Correct. RBI was established pursuant to the 1935 Act provisions (and RBI Act 1934).", "ta": "சரி. இந்திய ரிசர்வ் வங்கி 1935 சட்ட விதிகளின்படி அமைக்கப்பட்டது."},
        "C": {"en": "Incorrect. Federal Bank is a private commercial bank.", "ta": "தவறு. ஃபெடரல் வங்கி ஒரு தனியார் வணிக வங்கியாகும்."},
        "D": {"en": "Incorrect. SBI was created in 1955 by nationalizing Imperial Bank.", "ta": "தவறு. SBI 1955-ல் இம்பீரியல் வங்கியை தேசியமயமாக்கி உருவாக்கப்பட்டது."}
    },
    "TNPSC Trap: GOI Act 1935 provided for RBI, Federal Court (1937), and Provincial Public Service Commissions.",
    "TNPSC பொறி: 1935 சட்டம் ஆர்பிஐ, கூட்டாட்சி நீதிமன்றம் (1937), மாகாண பொதுச் சேவை ஆணையங்களை வழங்கியது.",
    "The Reserve Bank of India commenced operations on April 1, 1935.",
    "இந்திய ரிசர்வ் வங்கி ஏப்ரல் 1, 1935 அன்று தனது பணிகளைத் தொடங்கியது.",
    ["Polity", "Historical Background", "GOI Act 1935", "Reserve Bank of India"], "Understand", 60
))

# ----------------------------------------------------
# 10 CONCEPTUAL PYQ STYLE (Q16 - Q25)
# ----------------------------------------------------

# Q16: Conceptual - Medium - Regulating Act 1773 Executive Council
q_list.append(make_q(
    16, "Medium", "Advanced Conceptual",
    "How did the Regulating Act of 1773 modify the executive structure of the Bengal Presidency?",
    "1773 ஆம் ஆண்டின் ஒழுங்குமுறைச் சட்டம் வங்காள மாகாணத்தின் நிர்வாகக் கட்டமைப்பை எவ்வாறு மாற்றியமைத்தது?",
    [
        ("A", "It created a Viceroy assisted by a 15-member advisory Council of India", "இது 15 உறுப்பினர்களைக் கொண்ட இந்தியக் குழுவின் உதவியுடன் ஒரு வைஸ்ராயை உருவாக்கியது"),
        ("B", "It designated Governor of Bengal as Governor-General of Bengal and created an Executive Council of 4 members to assist him", "இது வங்காள ஆளுநரை வங்காள கவர்னர்-ஜெனரலாக மாற்றி, அவருக்கு உதவ 4 உறுப்பினர்களைக் கொண்ட நிர்வாகக் குழுவை உருவாக்கியது"),
        ("C", "It added a Fourth Member as Law Member to the Governor's Executive Council", "இது ஆளுநரின் நிர்வாகக் குழுவில் நான்காவது உறுப்பினராகச் சட்ட உறுப்பினரைச் சேர்த்தது"),
        ("D", "It introduced the Portfolio System allocating separate departments to executive members", "இது நிர்வாக உறுப்பினர்களுக்குத் தனித்தனித் துறைகளை ஒதுக்கும் இலாகா முறையை அறிமுகப்படுத்தியது")
    ],
    "B",
    "The 1773 Act designated the Governor of Bengal as 'Governor-General of Bengal' and created an Executive Council of four members to assist him, acting by majority vote.",
    "1773 சட்டம் வங்காள ஆளுநரை 'வங்காள கவர்னர்-ஜெனரல்' என மாற்றி, அவருக்கு உதவ பெரும்பான்மை வாக்களிக்கும் 4 உறுப்பினர்களைக் கொண்ட நிர்வாகக் குழுவை உருவாக்கியது.",
    {
        "A": {"en": "Incorrect. Viceroy and 15-member Council were established in 1858 Act.", "ta": "தவறு. வைஸ்ராய் மற்றும் 15 உறுப்பினர் குழு 1858 சட்டத்தில் அமைக்கப்பட்டன."},
        "B": {"en": "Correct. Created Governor-General of Bengal with Executive Council of 4 members.", "ta": "சரி. 4 உறுப்பினர்களைக் கொண்ட நிர்வாகக் குழுவுடன் வங்காள கவர்னர்-ஜெனரலை உருவாக்கியது."},
        "C": {"en": "Incorrect. Law Member was added in 1833 Act.", "ta": "தவறு. சட்ட உறுப்பினர் 1833 சட்டத்தில் சேர்க்கப்பட்டார்."},
        "D": {"en": "Incorrect. Portfolio system was recognized in 1861 Act.", "ta": "தவறு. இலாகா முறை 1861 சட்டத்தில் அங்கீகரிக்கப்பட்டது."}
    },
    "TNPSC Trap: Decisions in the 1773 Executive Council were taken by majority vote; Governor-General had only a casting vote in case of a tie.",
    "TNPSC பொறி: 1773 நிர்வாகக் குழுவில் முடிவுகள் பெரும்பான்மை வாக்களிப்பால் எடுக்கப்பட்டன; கவர்னர்-ஜெனரலுக்கு சமநிலை ஏற்படும் போது மட்டுமே வாக்களிக்கும் உரிமை இருந்தது.",
    "The 4 executive council members under 1773 Act were Clavering, Monson, Barwell, and Philip Francis.",
    "1773 சட்டத்தின் கீழ் 4 நிர்வாகக் குழு உறுப்பினர்கள் கிளாவரிங், மான்சன், பார்வெல் மற்றும் பிலிப் பிரான்சிஸ் ஆவார்.",
    ["Polity", "Historical Background", "Regulating Act 1773", "Executive Council"], "Analyze", 75
))

# Q17: Conceptual - Medium - Charter Act 1833 Centralization
q_list.append(make_q(
    17, "Medium", "Advanced Conceptual",
    "Why is the Charter Act of 1833 regarded as the final step towards legislative centralization in British India?",
    "1833 ஆம் ஆண்டின் சாசனச் சட்டம் ஏன் பிரிட்டிஷ் இந்தியாவில் சட்டமியற்றும் அதிகார மையமாக்கலின் இறுதிப் படியாகக் கருதப்படுகிறது?",
    [
        ("A", "It abolished the Supreme Court at Calcutta and centralized judicial authority", "இது கொல்கத்தா உச்ச நீதிமன்றத்தை ஒழித்து நீதித்துறை அதிகாரத்தை மையப்படுத்தியது"),
        ("B", "It deprived the Governors of Bombay and Madras of their legislative powers and vested exclusive legislative authority in Governor-General of India", "இது பம்பாய் மற்றும் மதராஸ் ஆளுநர்களின் சட்ட அதிகாரங்களைப் பறித்து, இந்தியாவின் கவர்னர்-ஜெனரலிடம் பிரத்யேக சட்ட அதிகாரத்தை ஒப்படைத்தது"),
        ("C", "It centralized all revenue collections directly under the British Parliament in London", "இது அனைத்து வருவாய் வசூலையும் நேரடியாக லண்டனில் உள்ள பிரிட்டிஷ் நாடாளுமன்றத்தின் கீழ் மையப்படுத்தியது"),
        ("D", "It merged the Princely States into British Presidencies under a single administration", "இது சுதேச சமஸ்தானங்களை ஒரே நிர்வாகத்தின் கீழ் பிரிட்டிஷ் மாகாணங்களுடன் இணைத்தது")
    ],
    "B",
    "The Charter Act of 1833 deprived the Governors of Bombay and Madras of their legislative powers. The Governor-General of India was given exclusive legislative powers for the whole of British India.",
    "1833 சாசனச் சட்டம் பம்பாய், மதராஸ் ஆளுநர்களின் சட்ட அதிகாரங்களைப் பறித்தது. இந்தியாவின் கவர்னர்-ஜெனரலுக்கு பிரிட்டிஷ் இந்தியா முழுமைக்கும் பிரத்யேக சட்ட அதிகாரம் வழங்கப்பட்டது.",
    {
        "A": {"en": "Incorrect. Supreme Court at Calcutta was not abolished in 1833 (it was merged into High Court in 1862).", "ta": "தவறு. கொல்கத்தா உச்ச நீதிமன்றம் 1833-ல் ஒழிக்கப்படவில்லை (1862-ல் உயர் நீதிமன்றத்துடன் இணைக்கப்பட்டது)."},
        "B": {"en": "Correct. Complete centralization of law-making power under Governor-General of India.", "ta": "சரி. இந்தியாவின் கவர்னர்-ஜெனரலின் கீழ் சட்டமியற்றும் அதிகாரம் முழுமையாக மையப்படுத்தப்பட்டது."},
        "C": {"en": "Incorrect. Revenue administration remained with Governor-General in Council.", "ta": "தவறு. வருவாய் நிர்வாகம் கவர்னர்-ஜெனரல் குழுவிடமே இருந்தது."},
        "D": {"en": "Incorrect. Princely states were not merged into British presidencies in 1833.", "ta": "தவறு. சுதேச சமஸ்தானங்கள் 1833-ல் பிரிட்டிஷ் மாகாணங்களுடன் இணைக்கப்படவில்லை."}
    },
    "TNPSC Trap: Laws made under earlier Acts were called 'Regulations'; laws made under Charter Act 1833 were called 'Acts'.",
    "TNPSC பொறி: முந்தைய சட்டங்களின் கீழ் செய்யப்பட்ட சட்டங்கள் 'ஒழுங்குமுறைகள்' (Regulations) எனப்பட்டன; 1833 சட்டத்தின் கீழ் இயற்றப்பட்டவை 'சட்டங்கள்' (Acts) எனப்பட்டன.",
    "Charter Act 1833 added Lord Macaulay as the 4th Law Member (non-voting) to the Executive Council.",
    "1833 சாசனச் சட்டம் லார்டு மெக்காலேவை 4வது சட்ட உறுப்பினராக (வாக்களிக்கும் உரிமையற்றவர்) சேர்த்தது.",
    ["Polity", "Historical Background", "Charter Act 1833", "Centralization"], "Analyze", 75
))

# Q18: Conceptual - Medium - GOI Act 1919 Dyarchy Logic
q_list.append(make_q(
    18, "Medium", "Advanced Conceptual",
    "Under the Government of India Act 1919, how were provincial administration subjects classified under the system of Dyarchy?",
    "1919 இந்திய அரசுச் சட்டத்தின் கீழ், இரட்டை ஆட்சி முறையின் போது மாகாண நிர்வாகத் துறைகள் எவ்வாறு வகைப்படுத்தப்பட்டன?",
    [
        ("A", "Federal subjects and Provincial subjects", "கூட்டாட்சித் துறைகள் மற்றும் மாகாணத் துறைகள்"),
        ("B", "Reserved subjects administered by Governor with Executive Council and Transferred subjects administered by Governor with elected Ministers", "நிர்வாகக் குழுவுடன் கவர்னரால் நிர்வகிக்கப்படும் ஒதுக்கப்பட்ட துறைகள் மற்றும் தேர்ந்தெடுக்கப்பட்ட அமைச்சர்களுடன் கவர்னரால் நிர்வகிக்கப்படும் மாற்றப்பட்ட துறைகள்"),
        ("C", "Union subjects, State subjects, and Concurrent subjects", "ஒன்றியத் துறைகள், மாநிலத் துறைகள் மற்றும் பொதுத் துறைகள்"),
        ("D", "Imperial subjects and Local subjects", "இம்பீரியல் துறைகள் மற்றும் உள்ளூர் துறைகள்")
    ],
    "B",
    "Under Dyarchy (GOI Act 1919), provincial subjects were divided into Reserved (law & order, finance, land revenue) administered by Governor & Executive Council without legislative accountability, and Transferred (education, health, local self-govt) administered by Governor with elected Ministers accountable to legislature.",
    "1919 சட்ட இரட்டை ஆட்சியில் மாகாணத் துறைகள் 'ஒதுக்கப்பட்டவை' (சட்டம்-ஒழுங்கு, நிதி - சட்டமன்ற பொறுப்பின்றி கவர்னர் & குழுவால் நிர்வகிக்கப்பட்டவை) மற்றும் 'மாற்றப்பட்டவை' (கல்வி, சுகாதாரம் - சட்டமன்றத்திற்குப் பொறுப்பான அமைச்சர்களுடன் கவர்னரால் நிர்வகிக்கப்பட்டவை) எனப் பிரிக்கப்பட்டன.",
    {
        "A": {"en": "Incorrect. Central and Provincial classification was the top-level list division under 1919 Act.", "ta": "தவறு. மத்திய மற்றும் மாகாணப் பகுப்பு 1919 சட்டத்தின் மேலடுக்கு பட்டியல் பிரிப்பாகும்."},
        "B": {"en": "Correct. Dyarchy divided provincial subjects into Reserved and Transferred subjects.", "ta": "சரி. இரட்டை ஆட்சி மாகாணத் துறைகளை ஒதுக்கப்பட்டவை மற்றும் மாற்றப்பட்டவை எனப் பிரித்தது."},
        "C": {"en": "Incorrect. 3-list division (Federal, Provincial, Concurrent) was introduced in 1935 Act.", "ta": "தவறு. 3-பட்டியல் பிரிப்பு (கூட்டாட்சி, மாகாண, பொது) 1935 சட்டத்தில் அறிமுகமானது."},
        "D": {"en": "Incorrect. Imperial and Local was not the statutory classification of Dyarchy.", "ta": "தவறு. இம்பீரியல் மற்றும் உள்ளூர் என்பது இரட்டை ஆட்சியின் சட்டப்பூர்வ வகைப்பாடு அல்ல."}
    },
    "TNPSC Trap: Reserved subjects were NOT responsible to the provincial legislature; Transferred subjects WERE responsible to the legislature.",
    "TNPSC பொறி: ஒதுக்கப்பட்ட துறைகள் மாகாண சட்டமன்றத்திற்குப் பொறுப்பானவை அல்ல; மாற்றப்பட்ட துறைகள் சட்டமன்றத்திற்குப் பொறுப்பானவை.",
    "1919 Act introduced bicameralism and direct elections at the Centre for the first time.",
    "1919 சட்டம் முதன்முறையாக மத்தியில் இரு அவை முறையையும் நேரடித் தேர்தலையும் அறிமுகப்படுத்தியது.",
    ["Polity", "Historical Background", "GOI Act 1919", "Reserved Transferred"], "Analyze", 75
))

# Q19: Conceptual - Medium - GOI Act 1935 Provincial Autonomy
q_list.append(make_q(
    19, "Medium", "Advanced Conceptual",
    "What was the core feature of 'Provincial Autonomy' introduced by the Government of India Act of 1935?",
    "1935 ஆம் ஆண்டின் இந்திய அரசுச் சட்டம் அறிமுகப்படுத்திய 'மாகாண தன்னாட்சியின்' (Provincial Autonomy) முதன்மை அம்சம் யாது?",
    [
        ("A", "Provinces were allowed to secede from the All-India Federation at will", "மாகாணங்கள் அகில இந்திய கூட்டாட்சியிலிருந்து விரும்பியவாறு பிரிய அனுமதிக்கப்பட்டன"),
        ("B", "Abolition of Dyarchy in provinces and establishment of responsible government with Governor acting on advice of Ministers accountable to legislature", "மாகாணங்களில் இரட்டை ஆட்சியை ஒழித்து, சட்டமன்றத்திற்குப் பொறுப்பான அமைச்சர்களின் ஆலோசனைப்படி கவர்னர் செயல்படும் பொறுப்பு ஆட்சியை நிறுவுதல்"),
        ("C", "Total financial independence of provinces without any central audit control", "மத்திய தணிக்கைக் கட்டுப்பாடின்றி மாகாணங்களின் முழுமையான நிதி சுதந்திரம்"),
        ("D", "Replacement of British Governors with elected Indian Governors in all provinces", "அனைத்து மாகாணங்களிலும் பிரிட்டிஷ் கவர்னர்களுக்குப் பதிலாக தேர்ந்தெடுக்கப்பட்ட இந்திய கவர்னர்களை நியமித்தல்")
    ],
    "B",
    "Provincial Autonomy under GOI Act 1935 meant provinces derived executive authority directly from the Crown, dyarchy was abolished, and Governor was required to act on the advice of elected ministers responsible to provincial legislature.",
    "1935 சட்டத்தின் கீழ் மாகாண தன்னாட்சி என்பது இரட்டை ஆட்சியை ஒழித்து, மாகாண சட்டமன்றத்திற்குப் பொறுப்பான தேர்ந்தெடுக்கப்பட்ட அமைச்சர்களின் ஆலோசனைப்படி கவர்னர் செயல்படும் பொறுப்பு ஆட்சியை நிறுவுவதைக் குறித்தது.",
    {
        "A": {"en": "Incorrect. Provinces had no right of secession from the proposed federation.", "ta": "தவறு. மாகாணங்களுக்கு கூட்டாட்சியிலிருந்து பிரியும் உரிமை வழங்கப்படவில்லை."},
        "B": {"en": "Correct. Abolished provincial dyarchy and established responsible government in provinces.", "ta": "சரி. மாகாண இரட்டை ஆட்சியை ஒழித்து மாகாணங்களில் பொறுப்பு ஆட்சியை நிறுவியது."},
        "C": {"en": "Incorrect. Federal Court and Auditor-General maintained central oversight.", "ta": "தவறு. கூட்டாட்சி நீதிமன்றம் மற்றும் தலைமைத் தணிக்கையாளர் மத்திய கண்காணிப்பைக் கொண்டிருந்தனர்."},
        "D": {"en": "Incorrect. Governors continued to be appointed by the Crown.", "ta": "தவறு. கவர்னர்கள் பிரிட்டிஷ் முடியாட்சியால் தொடர்ந்து நியமிக்கப்பட்டனர்."}
    },
    "TNPSC Trap: GOI Act 1935 abolished Dyarchy in Provinces but PROPOSED Dyarchy at the Centre.",
    "TNPSC பொறி: 1935 சட்டம் மாகாணங்களில் இரட்டை ஆட்சியை ஒழித்தது; ஆனால் மத்தியில் இரட்டை ஆட்சியை முன்மொழிந்தது.",
    "Provincial Autonomy came into operation in 1937 and was suspended in 1939 due to WWII resignations of Congress ministries.",
    "மாகாண தன்னாட்சி 1937-ல் அமலுக்கு வந்து, 1939-ல் காங்கிரஸ் அமைச்சரவைகளின் ராஜினாமாவால் நிறுத்தி வைக்கப்பட்டது.",
    ["Polity", "Historical Background", "GOI Act 1935", "Provincial Autonomy"], "Analyze", 75
))

# Q20: Conceptual - Hard - Indian Independence Act 1947 Sovereignty
q_list.append(make_q(
    20, "Hard", "Advanced Conceptual",
    "What was the legal consequence of the 'Lapse of Paramountcy' under Section 7 of the Indian Independence Act 1947?",
    "1947 இந்திய சுதந்திரச் சட்டத்தின் பிரிவு 7-ன் கீழ் 'மேலாதிக்கம் ரத்தாதலின்' (Lapse of Paramountcy) சட்டப்பூர்வ விளைவு யாது?",
    [
        ("A", "All Princely States automatically became part of the Union of India", "அனைத்து சுதேச சமஸ்தானங்களும் தானாகவே இந்திய ஒன்றியத்தின் அங்கமாயின"),
        ("B", "British suzerainty over Indian Princely States terminated, restoring their independent status to join India, Pakistan, or remain independent", "இந்திய சுதேச சமஸ்தானங்கள் மீதான பிரிட்டிஷ் மேலாதிக்கம் முடிவுக்கு வந்தது, இந்தியா அல்லது பாகிஸ்தானில் இணையவோ அல்லது சுதந்திரமாக இருக்கவோ அவற்றிற்கு உரிமை மீட்கப்பட்டது"),
        ("C", "The Crown transferred sovereignty over Princely States exclusively to Pakistan", "சுதேச சமஸ்தானங்கள் மீதான இறையாண்மையை பிரிட்டிஷ் முடி பாகிஸ்தானுக்கு மட்டுமே மாற்றியது"),
        ("D", "Princely States were brought under direct administration of the United Nations", "சுதேச சமஸ்தானங்கள் ஐக்கிய நாடுகள் சபையின் நேரடி நிர்வாகத்தின் கீழ் கொண்டுவரப்பட்டன")
    ],
    "B",
    "Section 7 of the Indian Independence Act 1947 declared the lapse of British paramountcy/suzerainty over Indian Princely States and tribal areas, returning them to their pre-treaty status with freedom to accede to India or Pakistan or remain independent.",
    "1947 இந்திய சுதந்திரச் சட்டத்தின் பிரிவு 7 சுதேச சமஸ்தானங்கள் மீதான பிரிட்டிஷ் மேலாதிக்கம் ரத்தானதாக அறிவித்தது, இதனால் அவை இந்தியா அல்லது பாகிஸ்தானுடன் இணையவோ அல்லது சுதந்திரமாக இருக்கவோ சுதந்திரம் பெற்றன.",
    {
        "A": {"en": "Incorrect. Princely states did not automatically join India; they had options.", "ta": "தவறு. சுதேச சமஸ்தானங்கள் தானாகவே இந்தியாவில் இணையவில்லை; அவற்றுக்கு விருப்ப உரிமைகள் இருந்தன."},
        "B": {"en": "Correct. Terminated suzerainty and lapsed treaty obligations over Princely States.", "ta": "சரி. சுதேச சமஸ்தானங்கள் மீதான பிரிட்டிஷ் மேலாதிக்கத்தை முடிவுக்குக் கொண்டுவந்தது."},
        "C": {"en": "Incorrect. Sovereignty was not transferred to Pakistan exclusively.", "ta": "தவறு. இறையாண்மை பாகிஸ்தானுக்கு மட்டும் மாற்றப்படவில்லை."},
        "D": {"en": "Incorrect. UN had no role under the 1947 Act.", "ta": "தவறு. 1947 சட்டத்தின் கீழ் ஐநாவுக்கு எந்தப் பங்கும் இல்லை."}
    },
    "TNPSC Trap: Sardar Vallabhbhai Patel, along with V.P. Menon, integrated 560+ princely states into India using Instruments of Accession.",
    "TNPSC பொறி: சர்தார் வல்லபாய் படேல், வி.பி. மேனனுடன் இணைந்து 560-க்கும் மேற்பட்ட சுதேச சமஸ்தானங்களை இணைப்பு ஆவணங்கள் மூலம் இந்தியாவில் இணைத்தார்.",
    "The 1947 Act designated the Constituent Assembly of each dominion as a fully sovereign legislature.",
    "1947 சட்டம் ஒவ்வொரு டொமினியனின் அரசியலமைப்பு நிர்ணய சபையையும் முழு இறையாண்மை கொண்ட சட்டமன்றமாக மாற்றியது.",
    ["Polity", "Historical Background", "Independence Act 1947", "Paramountcy"], "Analyze", 75
))

# Q21: Conceptual - Hard - Company Rule vs Crown Rule Transition
q_list.append(make_q(
    21, "Hard", "Advanced Conceptual",
    "Which structural change best marks the transition from Company Rule to Crown Rule in Indian constitutional history?",
    "இந்திய அரசியலமைப்பு வரலாற்றில் கம்பெனி ஆட்சியிலிருந்து பிரிட்டிஷ் முடி ஆட்சிக்கு மாறியதை எந்தக் கட்டமைப்பு மாற்றம் சிறந்த முறையில் குறிக்கிறது?",
    [
        ("A", "Substitution of Board of Control and Court of Directors by Secretary of State for India advised by Council of India", "கட்டுப்பாட்டு வாரியம் மற்றும் இயக்குநர்கள் அவைக்குப் பதிலாக இந்தியக் குழுவின் ஆலோசனையுடன் கூடிய இந்திய அரசுச் செயலர் நியமிக்கப்பட்டமை"),
        ("B", "Introduction of universal adult suffrage in provincial council elections", "மாகாண மேலவைத் தேர்தல்களில் அனைத்துலக வயதுவந்தோர் வாக்குரிமை அறிமுகப்படுத்தப்பட்டமை"),
        ("C", "Creation of a Supreme Court of Judicature replacing all native courts", "அனைத்து சுதேச நீதிமன்றங்களுக்கும் பதிலாக உச்ச நீதிமன்றம் உருவாக்கப்பட்மை"),
        ("D", "Complete devolution of legislative tax powers to district municipal boards", "மாவட்ட நகராட்சி வாரியங்களுக்கு வரி விதிக்கும் சட்ட அதிகாரங்கள் முழுமையாகப் பகிர்ந்தளிக்கப்பட்டமை")
    ],
    "A",
    "The Government of India Act 1858 abolished the dual government structure of Company Rule (Court of Directors & Board of Control) and created the office of Secretary of State for India, a Cabinet minister assisted by a 15-member advisory Council of India.",
    "1858 இந்திய அரசுச் சட்டம் கம்பெனி ஆட்சியின் இரட்டை அரசு முறையை (இயக்குநர்கள் அவை & கட்டுப்பாட்டு வாரியம்) ஒழித்து, 15 உறுப்பினர்களைக் கொண்ட இந்தியக் குழுவின் உதவியுடன் பிரிட்டிஷ் அமைச்சரவை உறுப்பினரான இந்திய அரசுச் செயலர் அலுவலகத்தை உருவாக்கியது.",
    {
        "A": {"en": "Correct. It replaced Company supervision with direct British Cabinet responsibility.", "ta": "சரி. இது கம்பெனி கண்காணிப்புக்கு பதிலாக பிரிட்டிஷ் அமைச்சரவை நேரடிப் பொறுப்பைக் கொண்டுவந்தது."},
        "B": {"en": "Incorrect. Universal adult franchise was only introduced in 1950 Constitution.", "ta": "தவறு. அனைத்துலக வயதுவந்தோர் வாக்குரிமை 1950 அரசியலமைப்பில் மட்டுமே வந்தது."},
        "C": {"en": "Incorrect. Native courts were not replaced by Supreme Court in 1858.", "ta": "தவறு. சுதேச நீதிமன்றங்கள் 1858-ல் உச்ச நீதிமன்றத்தால் மாற்றப்படவில்லை."},
        "D": {"en": "Incorrect. Tax devolution to municipal boards occurred later (Ripon 1882).", "ta": "தவறு. நகராட்சி வாரியங்களுக்கான வரிப் பகிர்வு பின்னர் (ரிப்பன் 1882) நடந்தது."}
    },
    "TNPSC Trap: Secretary of State was a member of the British Cabinet and directly responsible to the British Parliament.",
    "TNPSC பொறி: இந்திய அரசுச் செயலர் பிரிட்டிஷ் அமைச்சரவையின் உறுப்பினராவார், அவர் பிரிட்டிஷ் நாடாளுமன்றத்திற்கு நேரடியாகப் பொறுப்பானவர்.",
    "The 15-member Council of India was purely an advisory body chaired by the Secretary of State.",
    "15 உறுப்பினர்களைக் கொண்ட இந்தியக் குழு அரசுச் செயலரைத் தலைவராகக் கொண்ட வெறும் ஆலோசனைக் குழுவாகும்.",
    ["Polity", "Historical Background", "Company to Crown", "Secretary of State"], "Analyze", 75
))

# Q22: Conceptual - Medium - Charter Act 1853 Mini Parliament
q_list.append(make_q(
    22, "Medium", "Advanced Conceptual",
    "The Charter Act of 1853 established a 6-member Indian (Central) Legislative Council. Why was this body referred to as a 'Mini-Parliament'?",
    "1853 சாசனச் சட்டம் 6 உறுப்பினர்களைக் கொண்ட இந்திய (மத்திய) சட்ட மேலவையை உருவாக்கியது. அமைப்பானது ஏன் 'சிறிய நாடாளுமன்றம்' என அழைக்கப்பட்டது?",
    [
        ("A", "It was elected directly by citizens of all presidencies", "இது அனைத்து மாகாணக் குடிமக்களாலும் நேரடியாகத் தேர்ந்தெடுக்கப்பட்டது"),
        ("B", "It adopted the same parliamentary procedure and legislative machinery as the British Parliament", "இது பிரிட்டிஷ் நாடாளுமன்றத்தைப் போன்றே நாடாளுமன்ற நடைமுறைகள் மற்றும் சட்ட இயற்றும் முறைகளைப் பின்பற்றியது"),
        ("C", "It had the power to override decisions of the British House of Commons", "இது பிரிட்டிஷ் காமன்ஸ் அவையின் முடிவுகளை நிராகரிக்கும் அதிகாரத்தைக் கொண்டிருந்தது"),
        ("D", "It included elected representatives from all Indian Princely States", "இது அனைத்து இந்திய சுதேச சமஸ்தானங்களின் தேர்ந்தெடுக்கப்பட்ட பிரதிநிதிகளைக் கொண்டிருந்தது")
    ],
    "B",
    "The Charter Act of 1853 added 6 new legislative members to GG's executive council, establishing the Indian (Central) Legislative Council. It functioned for the first time as a mini-parliament, adopting procedures of British Parliament.",
    "1853 சாசனச் சட்டம் கவர்னர்-ஜெனரல் குழுவில் 6 புதிய சட்ட உறுப்பினர்களைச் சேர்த்து மத்திய சட்ட மேலவையை உருவாக்கியது. இது பிரிட்டிஷ் நாடாளுமன்ற நடைமுறைகளைப் பின்பற்றி சிறிய நாடாளுமன்றமாகச் செயல்பட்டது.",
    {
        "A": {"en": "Incorrect. Legislative council members were nominated, not directly elected.", "ta": "தவறு. சட்ட மேலவை உறுப்பினர்கள் நியமிக்கப்பட்டவர்களே, தேர்ந்தெடுக்கப்பட்டவர்கள் அல்ல."},
        "B": {"en": "Correct. Adopted special legislative procedure akin to British Parliament.", "ta": "சரி. பிரிட்டிஷ் நாடாளுமன்றம் போன்ற சிறப்பு சட்ட நடைமுறைகளைப் பின்பற்றியது."},
        "C": {"en": "Incorrect. It was completely subordinate to British Parliament.", "ta": "தவறு. இது பிரிட்டிஷ் நாடாளுமன்றத்திற்கு முற்றிலும் கீழ்ப்படிந்த அமைப்பாகும்."},
        "D": {"en": "Incorrect. Princely state representatives were not included in 1853.", "ta": "தவறு. சுதேச சமஸ்தான பிரதிநிதிகள் 1853-ல் சேர்க்கப்படவில்லை."}
    },
    "TNPSC Trap: Charter Act 1853 introduced local representation in Central Legislative Council for 1st time (4 members from Madras, Bombay, Bengal, Agra).",
    "TNPSC பொறி: 1853 சாசனச் சட்டம் முதன்முறையாக மத்திய சட்ட மேலவையில் உள்ளூர் பிரதிநிதித்துவத்தை (மதராஸ், பம்பாய், வங்காளம், ஆக்ரா ஆளுநர்களால் நியமிக்கப்பட்ட 4 உறுப்பினர்கள்) அறிமுகப்படுத்தியது.",
    "Charter Act 1853 was the last of the four Charter Acts (1793, 1813, 1833, 1853).",
    "1853 சாசனச் சட்டம் நான்கு சாசனச் சட்டங்களில் (1793, 1813, 1833, 1853) இறுதியானதாகும்.",
    ["Polity", "Historical Background", "Charter Act 1853", "Mini Parliament"], "Analyze", 75
))

# Q23: Conceptual - Medium - Indian Councils Act 1861 Decentralization
q_list.append(make_q(
    23, "Medium", "Advanced Conceptual",
    "How did the Indian Councils Act of 1861 initiate the process of legislative decentralization in British India?",
    "1861 ஆம் ஆண்டின் இந்தியக் கவுன்சில்கள் சட்டம் பிரிட்டிஷ் இந்தியாவில் சட்ட அதிகாரப் பரவலாக்கல் நடவடிக்கையை எவ்வாறு தொடங்கியது?",
    [
        ("A", "By transferring central taxation powers to village panchayats", "மத்திய வரி விதிப்பு அதிகாரங்களை கிராம பஞ்சாயத்துகளுக்கு மாற்றுவதன் மூலம்"),
        ("B", "By restoring legislative powers to the Presidencies of Bombay and Madras", "பம்பாய் மற்றும் மதராஸ் மாகாணங்களுக்குச் சட்ட அதிகாரங்களை மீட்டளிப்பதன் மூலம்"),
        ("C", "By creating independent state assemblies in all native princely states", "அனைத்து சுதேச சமஸ்தானங்களிலும் தன்னாட்சி பெற்ற மாநிலப் பேரவைகளை உருவாக்குவதன் மூலம்"),
        ("D", "By abolishing the legislative council at the Centre", "மத்தியில் உள்ள சட்ட மேலவையை ஒழிப்பதன் மூலம்")
    ],
    "B",
    "The Indian Councils Act of 1861 reversed the centralizing trend that started in 1773 and climaxed in 1833, by restoring legislative powers to Bombay and Madras Presidencies, thereby initiating legislative decentralization.",
    "1861 இந்தியக் கவுன்சில்கள் சட்டம் பம்பாய், மதராஸ் மாகாணங்களுக்கு சட்ட அதிகாரங்களை மீட்டளித்து 1773-ல் தொடங்கி 1833-ல் உச்சமடைந்த அதிகார மையமாக்கலைத் திரும்பப் பெற்று, பரவலாக்கத்தைத் தொடங்கியது.",
    {
        "A": {"en": "Incorrect. Panchayats had no statutory taxation powers under 1861 Act.", "ta": "தவறு. 1861 சட்டத்தில் பஞ்சாயத்துகளுக்கு வரி அதிகாரங்கள் இல்லை."},
        "B": {"en": "Correct. Restored legislative powers to Bombay and Madras Presidencies.", "ta": "சரி. பம்பாய் மற்றும் மதராஸ் மாகாணங்களுக்குச் சட்ட அதிகாரங்களை மீட்டளித்தது."},
        "C": {"en": "Incorrect. Native princely states were not given legislative assemblies by 1861 Act.", "ta": "தவறு. சுதேச சமஸ்தானங்களுக்கு 1861 சட்டம் சட்டப் பேரவைகளை வழங்கவில்லை."},
        "D": {"en": "Incorrect. Central Legislative Council was retained and expanded.", "ta": "தவறு. மத்திய சட்ட மேலவை தக்கவைக்கப்பட்டு விரிவாக்கப்பட்டது."}
    },
    "TNPSC Trap: Legislative decentralization started in 1861 Act and culminated in full Provincial Autonomy under 1935 Act.",
    "TNPSC பொறி: சட்ட அதிகாரப் பரவலாக்கம் 1861 சட்டத்தில் தொடங்கி 1935 சட்டத்தின் கீழ் முழு மாகாண தன்னாட்சியாக நிறைவுற்றது.",
    "The 1861 Act empowered Viceroy to issue Ordinances during emergencies without council concurrence.",
    "1861 சட்டம் அவசர காலத்தில் கவுன்சிலின் ஒப்புதலின்றி அவசரச் சட்டங்களை பிறப்பிக்க வைஸ்ராய்க்கு அதிகாரமளித்தது.",
    ["Polity", "Historical Background", "Indian Councils Act 1861", "Decentralization"], "Analyze", 75
))

# Q24: Conceptual - Hard - GOI Act 1919 Central Bicameralism
q_list.append(make_q(
    24, "Hard", "Advanced Conceptual",
    "The Government of India Act of 1919 introduced bicameralism at the Centre. What were the two houses created?",
    "1919 ஆம் ஆண்டின் இந்திய அரசுச் சட்டம் மத்தியில் இரு அவை முறையை அறிமுகப்படுத்தியது. உருவாக்கப்பட்ட அந்த இரண்டு அவைகள் யாவை?",
    [
        ("A", "House of Commons and House of Lords", "காமன்ஸ் அவை மற்றும் பிரபுக்கள் அவை"),
        ("B", "Council of State (Upper House) and Central Legislative Assembly (Lower House)", "மாநிலங்கள் அவை (மேலவை) மற்றும் மத்திய சட்டப் பேரவை (கீழவை)"),
        ("C", "Federal Assembly and Council of Princes", "கூட்டணிப் பேரவை மற்றும் இளவரசர்கள் அவை"),
        ("D", "Legislative Council and Legislative Assembly of Provinces", "மாகாண சட்ட மேலவை மற்றும் சட்டப் பேரவை")
    ],
    "B",
    "The 1919 Act replaced the Indian Legislative Council with a bicameral legislature at the Centre consisting of Council of State (Upper House - 60 members) and Central Legislative Assembly (Lower House - 140 members), with majority of members directly elected.",
    "1919 சட்டம் மத்திய சட்ட மேலவையை மாற்றி, மாநிலங்கள் அவை (மேலவை - 60 உறுப்பினர்கள்) மற்றும் மத்திய சட்டப் பேரவை (கீழவை - 140 உறுப்பினர்கள்) கொண்ட இரு அவைகளை மத்தியில் நிறுவியது.",
    {
        "A": {"en": "Incorrect. House of Commons and Lords are chambers of British Parliament in London.", "ta": "தவறு. காமன்ஸ் அவை மற்றும் பிரபுக்கள் அவை லண்டனில் உள்ள பிரிட்டிஷ் நாடாளுமன்ற அவைகளாகும்."},
        "B": {"en": "Correct. Council of State and Central Legislative Assembly were created in 1919.", "ta": "சரி. மாநிலங்கள் அவை மற்றும் மத்திய சட்டப் பேரவை 1919-ல் உருவாக்கப்பட்டன."},
        "C": {"en": "Incorrect. Chamber of Princes (Narendra Mandal) was established in 1921, not a chamber of Central Legislature.", "ta": "தவறு. இளவரசர்கள் அவை (நரேந்திர மண்டல்) 1921-ல் அமைந்தது, அது மத்திய சட்டமன்றத்தின் அவையல்ல."},
        "D": {"en": "Incorrect. Provincial bicameralism was introduced later in 1935 Act for 6 provinces.", "ta": "தவறு. மாகாண இரு அவை முறை பின்னர் 1935 சட்டத்தில் 6 மாகாணங்களுக்கு அறிமுகமானது."}
    },
    "TNPSC Trap: Direct elections were introduced at the Centre for the majority of members in both houses by 1919 Act.",
    "TNPSC பொறி: 1919 சட்டம் இரு அவைகளின் பெரும்பாலான உறுப்பினர்களுக்கு மத்தியில் முதன்முறையாக நேரடித் தேர்தலை அறிமுகப்படுத்தியது.",
    "The term of Council of State was 5 years, and Central Legislative Assembly was 3 years under 1919 Act.",
    "1919 சட்டத்தின் கீழ் மாநிலங்கள் அவையின் காலம் 5 ஆண்டுகள், மத்திய சட்டப் பேரவையின் காலம் 3 ஆண்டுகள் ஆகும்.",
    ["Polity", "Historical Background", "GOI Act 1919", "Bicameralism"], "Analyze", 75
))

# Q25: Conceptual - Hard - GOI Act 1935 Federal List System
q_list.append(make_q(
    25, "Hard", "Advanced Conceptual",
    "Where were the 'Residuary Powers' of legislation vested under the Government of India Act of 1935?",
    "1935 ஆம் ஆண்டின் இந்திய அரசுச் சட்டத்தின் கீழ் சட்டமியற்றும் 'எஞ்சிய அதிகாரங்கள்' (Residuary Powers) யாரிடம் ஒப்படைக்கப்பட்டன?",
    [
        ("A", "Federal Legislature", "கூட்டாட்சி சட்டமன்றம்"),
        ("B", "Provincial Legislatures", "மாகாண சட்டமன்றங்கள்"),
        ("C", "Governor-General of India", "இந்தியாவின் கவர்னர்-ஜெனரல்"),
        ("D", "Secretary of State for India in London", "லண்டனில் உள்ள இந்திய அரசுச் செயலர்")
    ],
    "C",
    "Unlike the modern Indian Constitution where residuary powers rest with Union Parliament (Article 248), under the GOI Act 1935, residuary legislative powers were vested in the discretion of the Governor-General of India.",
    "தற்போதைய இந்திய அரசியலமைப்பில் எஞ்சிய அதிகாரங்கள் நாடாளுமன்றத்திடம் (சரத்து 248) உள்ளதைப் போலன்றி, 1935 இந்திய அரசுச் சட்டத்தின் கீழ் எஞ்சிய அதிகாரங்கள் கவர்னர்-ஜெனரலின் தனிப்பட்ட விருப்புரிமையிடம் ஒப்படைக்கப்பட்டன.",
    {
        "A": {"en": "Incorrect. Federal Legislature had exclusive power over Federal List (59 items).", "ta": "தவறு. கூட்டாட்சி சட்டமன்றம் கூட்டாட்சிப் பட்டியல் (59) மீது மட்டுமே அதிகாரம் கொண்டிருந்தது."},
        "B": {"en": "Incorrect. Provincial Legislatures had power over Provincial List (54 items).", "ta": "தவறு. மாகாண சட்டமன்றங்கள் மாகாணப் பட்டியல் (54) மீது அதிகாரம் கொண்டிருந்தன."},
        "C": {"en": "Correct. Residuary powers were allocated at discretion to Governor-General of India.", "ta": "சரி. எஞ்சிய அதிகாரங்கள் கவர்னர்-ஜெனரலின் விருப்புரிமைக்கு ஒதுக்கப்பட்டன."},
        "D": {"en": "Incorrect. Secretary of State was the imperial supervisory authority, not residuary legislative holder.", "ta": "தவறு. அரசுச் செயலர் மேலாய்வு அதிகாரியாவார், எஞ்சிய அதிகாரம் அவரிடம் இல்லை."}
    },
    "TNPSC Trap: Modern India -> Residuary power with Parliament (Union); 1935 Act -> Residuary power with Governor-General.",
    "TNPSC பொறி: தற்போதைய இந்தியா -> எஞ்சிய அதிகாரம் நாடாளுமன்றத்திடம்; 1935 சட்டம் -> எஞ்சிய அதிகாரம் கவர்னர்-ஜெனரலிடம்.",
    "GOI Act 1935 allocated 59 items to Federal List, 54 to Provincial List, and 36 to Concurrent List.",
    "1935 சட்டம் கூட்டாட்சிப் பட்டியலுக்கு 59, மாகாணப் பட்டியலுக்கு 54, பொதுப் பட்டியலுக்கு 36 துறைகளை ஒதுக்கியது.",
    ["Polity", "Historical Background", "GOI Act 1935", "Residuary Powers"], "Analyze", 75
))

print(f"Generated first 25 questions. Total now: {len(q_list)}")
