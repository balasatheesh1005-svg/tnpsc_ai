import json
import sys
from pathlib import Path

target_path = Path(r"c:\Users\Home\Desktop\tnpsc_ai\data\questions\polity\historical_background_statement_based.json")
if target_path.exists():
    try:
        with open(target_path, "r", encoding="utf-8") as f:
            questions = json.load(f)
    except Exception:
        questions = []
else:
    questions = []

def make_q(q_id, q_type, q_en, q_ta, opt_a_en, opt_a_ta, opt_b_en, opt_b_ta, opt_c_en, opt_c_ta, opt_d_en, opt_d_ta,
           correct_ans, exp_en, exp_ta, wno_a_en, wno_a_ta, wno_b_en, wno_b_ta, wno_c_en, wno_c_ta, wno_d_en, wno_d_ta,
           tip_en, tip_ta, rev_en, rev_ta, bloom, est_time, tags):
    opts = [
        {"id": "A", "en": opt_a_en, "ta": opt_a_ta},
        {"id": "B", "en": opt_b_en, "ta": opt_b_ta},
        {"id": "C", "en": opt_c_en, "ta": opt_c_ta},
        {"id": "D", "en": opt_d_en, "ta": opt_d_ta}
    ]
    opts_en = [opt_a_en, opt_b_en, opt_c_en, opt_d_en]
    opts_ta = [opt_a_ta, opt_b_ta, opt_c_ta, opt_d_ta]
    
    return {
        "id": q_id,
        "subject": "Polity",
        "topic": "Historical Background",
        "difficulty": "Hard",
        "question_type": q_type,
        "question": {"en": q_en, "ta": q_ta},
        "options": opts,
        "correct_answer": correct_ans,
        "explanation": {"en": exp_en, "ta": exp_ta},
        "why_not_others": {
            "A": {"en": wno_a_en, "ta": wno_a_ta},
            "B": {"en": wno_b_en, "ta": wno_b_ta},
            "C": {"en": wno_c_en, "ta": wno_c_ta},
            "D": {"en": wno_d_en, "ta": wno_d_ta}
        },
        "tnpsc_tip": {"en": tip_en, "ta": tip_ta},
        "revision_fact": {"en": rev_en, "ta": rev_ta},
        "source_reference": ["M. Laxmikanth - Indian Polity", "NCERT", "Samacheer Kalvi"],
        "bloom_level": bloom,
        "estimated_time_sec": est_time,
        "pyq_similarity": "High",
        "tags": tags,
        "question_en": q_en,
        "question_ta": q_ta,
        "options_en": opts_en,
        "options_ta": opts_ta,
        "answer": correct_ans.lower(),
        "explanation_en": exp_en,
        "explanation_ta": exp_ta
    }

# =========================================================
# PART 4: 5 INCORRECT STATEMENT QUESTIONS (HB_SB_041 to HB_SB_045)
# =========================================================

# HB_SB_041
questions.append(make_q(
    "HB_SB_041", "Statement Based",
    "Which of the following statements regarding the Charter Act of 1833 is INCORRECT?",
    "1833 ஆம் ஆண்டின் சாசனச் சட்டம் பற்றிய பின்வரும் கூற்றுகளில் எது தவறானது?",
    "It redesignated the Governor-General of Bengal as the Governor-General of India and concentrated all civil and military powers in him.",
    "இது வங்காள கவர்னர் ஜெனரலை இந்திய கவர்னர் ஜெனரலாக மாற்றி அனைத்து சிவில் மற்றும் இராணுவ அதிகாரங்களையும் அவரிடம் குவித்தது.",
    "It added Lord Macaulay as the Law Member to the Governor-General's Executive Council.",
    "இது லார்ட் மெக்காலேயை கவர்னர் ஜெனரலின் நிர்வாகக் குழுவில் சட்ட உறுப்பினராகச் சேர்த்தது.",
    "It successfully established an open competitive examination system for civil service recruitment in India.",
    "இது இந்தியாவில் குடிமைப் பணி ஆட்சேர்ப்புக்காக ஒரு திறந்தவெளிப் போட்டித் தேர்வு முறையை வெற்றிகரமாக நிறுவியது.",
    "It provided that Company's territorial holdings were held in trust for His Majesty, His Heirs and Successors.",
    "கம்பெனியின் நிலப்பரப்பு உடமைகள் பிரிட்டிஷ் மன்னரின் நம்பிக்கைப் பொறுப்பில் (trust) வைக்கப்பட்டுள்ளதாக இது கூறியது.",
    "C",
    "Option C is INCORRECT. While the Charter Act of 1833 attempted to introduce open competition, Section 87's open competition scheme was negated due to strong opposition from the Court of Directors. Open competition was successfully introduced later by Charter Act 1853.",
    "விருப்பம் C தவறானது. 1833 சாசனச் சட்டம் திறந்தவெளிப் போட்டியை அறிமுகப்படுத்த முயன்றபோதிலும், இயக்குநர்கள் அவையின் எதிர்ப்பால் அது ரத்து செய்யப்பட்டது. திறந்தவெளிப் போட்டி 1853 சாசனச் சட்டத்தில்தான் அமலானது.",
    "Incorrect. Statement A is correct.",
    "தவறு. கூற்று A சரியானது.",
    "Incorrect. Statement B is correct.",
    "தவறு. கூற்று B சரியானது.",
    "Correct. Option C is INCORRECT (open competition succeeded in 1853, not 1833).",
    "சரி. விருப்பம் C தவறானது (திறந்தவெளிப் போட்டி 1853 இல் வெற்றி பெற்றது).",
    "Incorrect. Statement D is correct.",
    "தவறு. கூற்று D சரியானது.",
    "TNPSC Trap: 1833 Act ATTEMPTED open competition, but 1853 Act ACTUALLY IMPLEMENTED open competition for Civil Services.",
    "TNPSC பொறி: 1833 சட்டம் திறந்தவெளிப் போட்டியை முயற்சித்தது, ஆனால் 1853 சட்டமே அதைச் செயல்படுத்தியது.",
    "Lord William Bentinck was the first Governor-General of India appointed under 1833 Charter Act.",
    "1833 சாசனச் சட்டப்படி வில்லியம் பென்டிங்க் பிரபு இந்தியாவின் முதல் கவர்னர் ஜெனரலானார்.",
    "Analyze", 75, ["Polity", "Historical Background", "Charter Act 1833", "Incorrect Statement"]
))

# HB_SB_042
questions.append(make_q(
    "HB_SB_042", "Statement Based",
    "Which of the following statements regarding the Indian Councils Act of 1861 is INCORRECT?",
    "1861 ஆம் ஆண்டின் இந்தியக் கவுன்சில்கள் சட்டம் பற்றிய பின்வரும் கூற்றுகளில் எது தவறானது?",
    "It initiated the process of legislative decentralization by restoring law-making powers to Bombay and Madras Presidencies.",
    "இது பம்பாய் மற்றும் மதராஸ் மாகாணங்களுக்கு சட்ட அதிகாரங்களை மீட்டு சட்டமன்ற பரவலாக்கலைத் தொடங்கியது.",
    "It gave statutory recognition to the Portfolio System introduced by Lord Canning in 1859.",
    "இது 1859 இல் கேனிங் பிரபு அறிமுகப்படுத்திய துறை ஒதுக்கீடு முறைக்கு சட்டப்பூர்வ அங்கீகாரம் அளித்தது.",
    "It empowered the Viceroy to issue ordinances during emergencies valid for six months.",
    "இது அவசரகாலத்தில் 6 மாத காலம் செல்லுபடியாகும் அவசரச்சட்டங்களை பிறப்பிக்க வைஸ்ராய்க்கு அதிகாரமளித்தது.",
    "It granted council members the right to discuss the annual budget and vote on demands for grants.",
    "இது கவுன்சில் உறுப்பினர்களுக்கு ஆண்டு பட்ஜெட்டை விவாதிக்கவும் மானியக் கோரிக்கைகள் மீது வாக்களிக்கவும் உரிமை வழங்கியது.",
    "D",
    "Option D is INCORRECT. Budget discussion was introduced in 1892 (discussion only, no voting) and voting on demands for grants was introduced in 1919. The 1861 Act did NOT grant budget discussion or voting rights.",
    "விருப்பம் D தவறானது. பட்ஜெட் விவாதம் 1892 இலும் (விவாதம் மட்டும்) மானியக் கோரிக்கை வாக்களிப்பு 1919 இலும் வந்தன. 1861 சட்டத்தில் பட்ஜெட் உரிமைகள் வழங்கப்படவில்லை.",
    "Incorrect. Statement A is correct.",
    "தவறு. கூற்று A சரியானது.",
    "Incorrect. Statement B is correct.",
    "தவறு. கூற்று B சரியானது.",
    "Incorrect. Statement C is correct.",
    "தவறு. கூற்று C சரியானது.",
    "Correct. Option D is INCORRECT (budget powers were introduced in 1892 and 1919, not 1861).",
    "சரி. விருப்பம் D தவறானது (பட்ஜெட் அதிகாரங்கள் 1892 மற்றும் 1919 இல் வந்தன).",
    "1861 Act marked the beginning of representative institutions by nominating 3 non-official Indians in 1862.",
    "1861 சட்டம் 1862 இல் 3 இந்தியர்களை நியமித்ததன் மூலம் பிரதிநிதித்துவ அமைப்புகளுக்குத் தொடக்கமிட்டது.",
    "Lord Canning nominated Raja of Benares, Maharaja of Patiala, and Sir Dinkar Rao to the Central Legislative Council in 1862.",
    "1862 இல் கேனிங் பிரபு காசி ராஜா, பாட்டியாலா மகாராஜா, சர் தினகர் ராவ் ஆகியோரை மத்திய கவுன்சிலுக்கு நியமித்தார்.",
    "Analyze", 75, ["Polity", "Historical Background", "Indian Councils Act 1861", "Incorrect Statement"]
))

# HB_SB_043
questions.append(make_q(
    "HB_SB_043", "Statement Based",
    "Which of the following statements regarding the Government of India Act of 1919 is INCORRECT?",
    "1919 ஆம் ஆண்டின் இந்திய அரசுச் சட்டம் பற்றிய பின்வரும் கூற்றுகளில் எது தவறானது?",
    "It introduced Dyarchy in eight provinces by classifying provincial subjects into Reserved and Transferred.",
    "இது மாகாணத் துறைகளை ஒதுக்கப்பட்டவை மற்றும் மாற்றப்பட்டவை என வகைப்படுத்தி 8 மாகாணங்களில் இரட்டை ஆட்சியை அறிமுகப்படுத்தியது.",
    "It established a bicameral central legislature consisting of Council of State and Legislative Assembly.",
    "இது மாநிலங்களவை மற்றும் சட்டமன்றப் பேரவை கொண்ட ஈரவை மத்திய சட்டமன்றத்தை நிறுவியது.",
    "It placed Finance and Law & Order under the control of elected Indian Transferred Ministers.",
    "இது நிதி மற்றும் சட்டம்-ஒழுங்கை தேர்ந்தெடுக்கப்பட்ட இந்திய மாற்றப்பட்ட துறை அமைச்சர்களின் கட்டுப்பாட்டில் வைத்தது.",
    "It provided for the creation of Central Public Service Commission which was established in 1926.",
    "இது 1926 இல் அமைக்கப்பட்ட மத்திய பொதுச் சேவை ஆணையத்தை உருவாக்க வழிவகை செய்தது.",
    "C",
    "Option C is INCORRECT. Finance, Law & Order, and Land Revenue were classified as RESERVED subjects administered directly by the Governor and his Executive Council (not under Transferred ministers). Transferred subjects included Education, Health, and Local Self-Govt.",
    "விருப்பம் C தவறானது. நிதி, சட்டம்-ஒழுங்கு ஆகியவை கவர்னரின் ஒதுக்கப்பட்ட பட்டியலில் இருந்தன (மாற்றப்பட்ட துறை அமைச்சர்களிடம் இல்லை). மாற்றப்பட்ட துறைகளில் கல்வி, சுகாதாரம் ஆகியவை இருந்தன.",
    "Incorrect. Statement A is correct.",
    "தவறு. கூற்று A சரியானது.",
    "Incorrect. Statement B is correct.",
    "தவறு. கூற்று B சரியானது.",
    "Correct. Option C is INCORRECT (Finance was a Reserved subject under Governor, not Transferred).",
    "சரி. விருப்பம் C தவறானது (நிதி ஒதுக்கப்பட்ட பட்டியலில் கவர்னரிடம் இருந்தது).",
    "Incorrect. Statement D is correct.",
    "தவறு. கூற்று D சரியானது.",
    "Dyarchy failed in practice because Indian Ministers in Transferred subjects lacked funds controlled by Reserved Finance.",
    "நிதி ஒதுக்கப்பட்ட பட்டியலில் இருந்ததால் மாற்றப்பட்ட துறை அமைச்சர்களால் செயல்பட முடியாமல் இரட்டை ஆட்சி தோற்றது.",
    "1919 Act introduced direct elections in India for the first time.",
    "1919 சட்டம் இந்தியாவில் முதன்முறையாக நேரடித் தேர்தலை அறிமுகப்படுத்தியது.",
    "Analyze", 75, ["Polity", "Historical Background", "Government of India Act 1919", "Incorrect Statement"]
))

# HB_SB_044
questions.append(make_q(
    "HB_SB_044", "Statement Based",
    "Which of the following statements regarding the Government of India Act of 1935 is INCORRECT?",
    "1935 ஆம் ஆண்டின் இந்திய அரசுச் சட்டம் பற்றிய பின்வரும் கூற்றுகளில் எது தவறானது?",
    "It provided for an All-India Federation consisting of British Indian Provinces and Princely States.",
    "இது பிரிட்டிஷ் இந்திய மாகாணங்கள் மற்றும் சுதேச சமஸ்தானங்களைக் கொண்ட அகில இந்திய கூட்டாட்சிக்கு வழிவகை செய்தது.",
    "It abolished Dyarchy in provinces and introduced Provincial Autonomy in 1937.",
    "இது மாகாண இரட்டை ஆட்சியை ஒழித்து 1937 இல் மாகாண தன்னாட்சியை அறிமுகப்படுத்தியது.",
    "It divided legislative subjects into Federal, Provincial, and Concurrent lists.",
    "இது சட்ட அதிகாரங்களை கூட்டாட்சி, மாகாண, மற்றும் இணைப்புப் பட்டியல்களாகப் பிரித்தது.",
    "It assigned Residuary legislative powers exclusively to the Federal Parliament.",
    "இது எஞ்சிய சட்ட அதிகாரங்களை கூட்டாட்சி பாராளுமன்றத்திற்கு மட்டுமே ஒப்படைத்தது.",
    "D",
    "Option D is INCORRECT. Under the Government of India Act 1935, Residuary legislative powers were given to the Governor-General (Viceroy) to allocate at his discretion, NOT to the Federal Parliament. Residuary powers belong to Parliament only under Article 248 of the 1950 Constitution.",
    "விருப்பம் D தவறானது. 1935 சட்டத்தின் கீழ் எஞ்சிய அதிகாரங்கள் கவர்னர் ஜெனரலிடம் (வைஸ்ராய்) கொடுக்கப்பட்டன, பாராளுமன்றத்திடம் அல்ல. 1950 அரசியலமைப்பின் 248 விதியில்தான் அவை பாராளுமன்றத்திடம் உள்ளன.",
    "Incorrect. Statement A is correct.",
    "தவறு. கூற்று A சரியானது.",
    "Incorrect. Statement B is correct.",
    "தவறு. கூற்று B சரியானது.",
    "Incorrect. Statement C is correct.",
    "தவறு. கூற்று C சரியானது.",
    "Correct. Option D is INCORRECT (Residuary powers were with Viceroy, not Federal Parliament).",
    "சரி. விருப்பம் D தவறானது (எஞ்சிய அதிகாரங்கள் வைஸ்ராயிடம் இருந்தன).",
    "TNPSC Comparison: Residuary Powers in 1935 Act = Viceroy (GG); Residuary Powers in 1950 Constitution = Parliament (Article 248).",
    "TNPSC ஒப்பீடு: 1935 சட்டத்தில் எஞ்சிய அதிகாரங்கள் = வைஸ்ராய்; 1950 அரசியலமைப்பில் எஞ்சிய அதிகாரங்கள் = பாராளுமன்றம் (பிரிவு 248).",
    "1935 Act introduced bicameralism in 6 out of 11 provinces.",
    "1935 சட்டம் 11 இல் 6 மாகாணங்களில் ஈரவை முறையை அறிமுகப்படுத்தியது.",
    "Analyze", 75, ["Polity", "Historical Background", "Government of India Act 1935", "Incorrect Statement"]
))

# HB_SB_045
questions.append(make_q(
    "HB_SB_045", "Statement Based",
    "Which of the following statements regarding the Indian Independence Act of 1947 is INCORRECT?",
    "1947 ஆம் ஆண்டின் இந்திய சுதந்திரச் சட்டம் பற்றிய பின்வரும் கூற்றுகளில் எது தவறானது?",
    "It declared India and Pakistan as independent dominions from August 15, 1947.",
    "இது ஆகஸ்ட் 15, 1947 முதல் இந்தியா மற்றும் பாகிஸ்தானை சுதந்திர டொமினியன்களாக அறிவித்தது.",
    "Section 6 empowered the Constituent Assembly to alter or repeal any Act of British Parliament applying to India.",
    "பிரிவு 6 இந்தியாவில் பொருந்தும் எந்தவொரு பிரிட்டிஷ் பாராளுமன்ற சட்டத்தையும் மாற்ற அல்லது ரத்து செய்ய அரசியலமைப்பு சபைக்கு அதிகாரமளித்தது.",
    "It proclaimed the lapse of British paramountcy over Indian Princely States.",
    "இது சுதேச சமஸ்தானங்கள் மீதான பிரிட்டிஷ் மேலாதிக்கம் முடிவுக்கு வந்ததாக அறிவித்தது.",
    "It mandated that all laws enacted by the Constituent Assembly must receive Royal Assent from the British Monarch.",
    "அரசியலமைப்பு சபை நிறைவேற்றும் அனைத்து சட்டங்களும் பிரிட்டிஷ் மன்னரின் அரச ஒப்புதலைப் பெற வேண்டும் என்று இது கட்டாயப்படுத்தியது.",
    "D",
    "Option D is INCORRECT. The Indian Independence Act 1947 explicitly abolished the requirement of Royal Assent by the British Crown for laws passed by the Constituent Assembly of either Dominion. The Governor-General had full power to assent to laws in the name of His Majesty.",
    "விருப்பம் D தவறானது. 1947 சுதந்திரச் சட்டம் அரசியலமைப்பு சபை இயற்றும் சட்டங்களுக்கு பிரிட்டிஷ் மன்னரின் அரச ஒப்புதல் தேவையை வெளிப்படையாக ரத்து செய்தது. கவர்னர் ஜெனரலே ஒப்புதல் அளிக்கும் அதிகாரம் பெற்றார்.",
    "Incorrect. Statement A is correct.",
    "தவறு. கூற்று A சரியானது.",
    "Incorrect. Statement B is correct.",
    "தவறு. கூற்று B சரியானது.",
    "Incorrect. Statement C is correct.",
    "தவறு. கூற்று C சரியானது.",
    "Correct. Option D is INCORRECT (Royal Assent requirement was explicitly abolished).",
    "சரி. விருப்பம் D தவறானது (அரச ஒப்புதல் தேவை ரத்து செய்யப்பட்டது).",
    "1947 Act abolished the title 'Emperor of India' from the royal style and titles of the King of England.",
    "1947 சட்டம் இங்கிலாந்து மன்னரின் பட்டங்களிலிருந்து 'இந்தியப் பேரரசர்' என்ற பட்டத்தை நீக்கியது.",
    "Indian Independence Act 1947 received Royal Assent on July 18, 1947.",
    "இந்திய சுதந்திரச் சட்டம் 1947 ஜூலை 18 அன்று மன்னரின் ஒப்புதலைப் பெற்றது.",
    "Analyze", 75, ["Polity", "Historical Background", "Indian Independence Act 1947", "Incorrect Statement"]
))

# =========================================================
# PART 5: 5 INTEGRATED STATEMENT QUESTIONS (HB_SB_046 to HB_SB_050)
# =========================================================

# HB_SB_046
questions.append(make_q(
    "HB_SB_046", "Statement Based",
    "Consider the following integrated statements regarding the pendulum shift from Centralization to Decentralization in British India:\n1. The Regulating Act 1773 initiated centralizing control by making Bombay and Madras subordinate to Bengal in war and peace.\n2. The Charter Act 1833 represented the climax of centralization by depriving Bombay and Madras Governors of all legislative powers.\n3. The Indian Councils Act 1861 initiated legislative decentralization by restoring law-making powers to Bombay and Madras.\n4. The Government of India Act 1935 completed decentralization by establishing full Provincial Autonomy.\nWhich of the statements given above are correct?",
    "பிரிட்டிஷ் இந்தியாவில் மத்தியமயமாக்கலிலிருந்து பரவலாக்கலுக்கு ஏற்பட்ட கட்டமைப்பு மாற்றங்கள் பற்றிய பின்வரும் ஒருங்கிணைந்த கூற்றுகளைக் கவனியுங்கள்:\n1. 1773 ஒழுங்குமுறைச் சட்டம் போர் மற்றும் அமைதியில் பம்பாய், மதராஸை வங்காளத்திற்குக் கீழ்ப்படிந்ததாக்கி மத்தியமயமாக்கலைத் தொடங்கியது.\n2. 1833 சாசனச் சட்டம் பம்பாய், மதராஸ் கவர்னர்களின் சட்ட அதிகாரங்களைப் பறித்து மத்தியமயமாக்கலின் உச்சத்தை அடைந்தது.\n3. 1861 இந்தியக் கவுன்சில்கள் சட்டம் பம்பாய், மதராஸுக்கு சட்ட அதிகாரங்களை மீட்டு சட்டமன்ற பரவலாக்கலைத் தொடங்கியது.\n4. 1935 இந்திய அரசுச் சட்டம் முழு மாகாண தன்னாட்சியை நிறுவி பரவலாக்கலை நிறைவு செய்தது.\nஎது சரி?",
    "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டும்",
    "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டும்",
    "1, 3 and 4 only", "1, 3 மற்றும் 4 மட்டும்",
    "1, 2, 3 and 4", "1, 2, 3 மற்றும் 4",
    "D",
    "All four statements are correct. Centralization trajectory: 1773 (Initiation) -> 1833 (Climax) -> 1861 (Reversal / Decentralization onset) -> 1935 (Provincial Autonomy completion).",
    "நான்கு கூற்றுகளும் சரியானவை. மத்தியமயமாக்கல் பாதை: 1773 (தொடக்கம்) -> 1833 (உச்சம்) -> 1861 (திருப்பம்/பரவலாக்கல்) -> 1935 (மாகாண தன்னாட்சி).",
    "Incorrect. Statement 4 is also correct.",
    "தவறு. கூற்று 4-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Correct. All four statements accurately trace the centralization-decentralization trajectory.",
    "சரி. நான்கு கூற்றுகளும் மத்தியமயமாக்கல்-பரவலாக்கல் பாதையைத் துல்லியமாகக் காட்டுகின்றன.",
    "Provincial Autonomy came into force in April 1937 under GOI Act 1935.",
    "மாகாண தன்னாட்சி 1935 அரசுச் சட்டப்படி 1937 ஏப்ரலில் அமலுக்கு வந்தது.",
    "1833 Charter Act created Governor-General of India, concentrating all legislative powers in the Centre.",
    "1833 சாசனச் சட்டம் அனைத்து சட்ட அதிகாரங்களையும் மையத்தில் குவித்து இந்திய கவர்னர் ஜெனரலை உருவாக்கியது.",
    "Analyze", 75, ["Polity", "Historical Background", "Centralization to Autonomy Arc", "Integrated Statement"]
))

# HB_SB_047
questions.append(make_q(
    "HB_SB_047", "Statement Based",
    "Consider the following integrated statements regarding the evolution of Executive Ordinance-making powers in India:\n1. Ordinance-making power was first introduced by the Indian Councils Act of 1861, empowering the Viceroy to issue ordinances valid for 6 months.\n2. Sections 42 and 43 of the Government of India Act 1935 expanded Ordinance powers of the Governor-General during legislative recess and emergencies.\n3. The 1950 Constitution incorporated executive ordinance powers under Article 123 (President) and Article 213 (Governor).\nWhich of the statements given above are correct?",
    "இந்தியாவில் நிர்வாகத்தின் அவசரச்சட்ட அதிகாரத்தின் (Ordinance) வளர்ச்சி பற்றிய பின்வரும் ஒருங்கிணைந்த கூற்றுகளைக் கவனியுங்கள்:\n1. அவசரச்சட்ட அதிகாரம் 1861 இந்தியக் கவுன்சில்கள் சட்டத்தால் முதன்முறையாக அறிமுகப்படுத்தப்பட்டு வைஸ்ராய்க்கு 6 மாத அவசரச்சட்ட அதிகாரம் அளித்தது.\n2. 1935 இந்திய அரசுச் சட்டத்தின் பிரிவுகள் 42 மற்றும் 43 கவர்னர் ஜெனரலின் அவசரச்சட்ட அதிகாரங்களை சட்டமன்ற இடைவேளை மற்றும் அவசரகாலங்களில் விரிவுபடுத்தின.\n3. 1950 அரசியலமைப்பு நிர்வாக அவசரச்சட்ட அதிகாரங்களை பிரிவு 123 (குடியரசுத் தலைவர்) மற்றும் பிரிவு 213 (ஆளுநர்) ஆகியவற்றின் கீழ் இணைத்தது.\nஎது சரி?",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "D",
    "All three statements are correct. Traces Ordinance power from 1861 Act (6 months) -> 1935 Act (Sections 42/43) -> 1950 Constitution (Articles 123 & 213).",
    "மூன்று கூற்றுகளும் சரியானவை. அவசரச்சட்ட அதிகாரம் 1861 சட்டம் (6 மாதங்கள்) -> 1935 சட்டம் (பிரிவுகள் 42/43) -> 1950 அரசியலமைப்பு (பிரிவுகள் 123 & 213).",
    "Incorrect. Statement 3 is also correct.",
    "தவறு. கூற்று 3-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Correct. All three statements accurately synthesize Ordinance power evolution.",
    "சரி. மூன்று கூற்றுகளும் அவசரச்சட்ட அதிகார வளர்ச்சியைத் துல்லியமாக ஒருங்கிணைக்கின்றன.",
    "Ordinances promulgated under Articles 123 or 213 have the same force and effect as an Act of Parliament/Legislature.",
    "பிரிவு 123 அல்லது 213 இன் கீழ் பிறப்பிக்கப்படும் அவசரச்சட்டம் பாராளுமன்ற சட்டத்திற்கு இணையான அதிகாரம் கொண்டது.",
    "Max life of an Ordinance without legislative approval is 6 months and 6 weeks.",
    "சட்டமன்ற ஒப்புதலின்றி அவசரச்சட்டத்தின் அதிகபட்ச ஆயுட்காலம் 6 மாதங்கள் மற்றும் 6 வாரங்கள் ஆகும்.",
    "Analyze", 75, ["Polity", "Historical Background", "Ordinance Power Evolution Arc", "Integrated Statement"]
))

# HB_SB_048
questions.append(make_q(
    "HB_SB_048", "Statement Based",
    "Consider the following integrated statements regarding the evolution of Division of Powers between Centre and States:\n1. Charter Act 1833 established a central legislative monopoly with zero division of powers.\n2. GOI Act 1919 classified legislative subjects into Central and Provincial lists for the first time.\n3. GOI Act 1935 created a 3-tier distribution of powers: Federal (59), Provincial (54), Concurrent (36) with Residuary powers to Viceroy.\n4. The 1950 Constitution adapted the 3-tier distribution into the 7th Schedule (Union, State, Concurrent Lists) and assigned Residuary powers to Parliament under Article 248.\nWhich of the statements given above are correct?",
    "மத்திய மற்றும் மாநிலங்களுக்கு இடையிலான அதிகாரப் பகிர்வின் வளர்ச்சி பற்றிய பின்வரும் ஒருங்கிணைந்த கூற்றுகளைக் கவனியுங்கள்:\n1. 1833 சாசனச் சட்டம் அதிகாரப் பகிர்வின்றி மத்திய சட்ட ஏகபோகத்தை நிறுவியது.\n2. 1919 அரசுச் சட்டம் முதன்முறையாக சட்டத் துறைகளை மத்திய மற்றும் மாகாணப் பட்டியல்களாக வகைப்படுத்தியது.\n3. 1935 அரசுச் சட்டம் அதிகாரங்களை 3 பட்டியல்களாகப் (கூட்டாட்சி 59, மாகாணம் 54, இணைப்பு 36) பிரித்து எஞ்சிய அதிகாரங்களை வைஸ்ராய்க்கு அளித்தது.\n4. 1950 அரசியலமைப்பு 3-அடுக்கு பட்டியலை 7வது அட்டவணையாக ஏற்று எஞ்சிய அதிகாரங்களை பிரிவு 248 இல் பாராளுமன்றத்திற்கு வழங்கியது.\nஎது சரி?",
    "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டும்",
    "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டும்",
    "1, 3 and 4 only", "1, 3 மற்றும் 4 மட்டும்",
    "1, 2, 3 and 4", "1, 2, 3 மற்றும் 4",
    "D",
    "All four statements are correct. Traces power division from 1833 central monopoly -> 1919 classification -> 1935 3 lists -> 7th Schedule in 1950 Constitution.",
    "நான்கு கூற்றுகளும் சரியானவை. 1833 மத்திய ஏகபோகம் -> 1919 துறைப் பிரிவு -> 1935 3 பட்டியல்கள் -> 1950 அரசியலமைப்பின் 7வது அட்டவணை.",
    "Incorrect. Statement 4 is also correct.",
    "தவறு. கூற்று 4-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Correct. All four statements accurately synthesize the 7th Schedule evolution.",
    "சரி. நான்கு கூற்றுகளும் 7வது அட்டவணை வளர்ச்சியைத் துல்லியமாக ஒருங்கிணைக்கின்றன.",
    "Residuary powers were shifted from Viceroy (1935 Act) to Union Parliament (Article 248, 1950 Constitution).",
    "எஞ்சிய அதிகாரங்கள் வைஸ்ராயிடமிருந்து (1935 சட்டம்) மத்திய பாராளுமன்றத்திற்கு (பிரிவு 248, 1950) மாற்றப்பட்டன.",
    "Canadian Constitution inspired assigning Residuary powers to the Union Parliament.",
    "எஞ்சிய அதிகாரங்களை மத்திய பாராளுமன்றத்திற்கு வழங்குவது கனடா அரசியலமைப்பால் ஈர்க்கப்பட்டது.",
    "Analyze", 75, ["Polity", "Historical Background", "7th Schedule Division Arc", "Integrated Statement"]
))

# HB_SB_049
questions.append(make_q(
    "HB_SB_049", "Statement Based",
    "Consider the following integrated statements regarding the evolution of Supreme Court and Judicial structure in India:\n1. 1774: Supreme Court of Judicature established at Calcutta under Regulating Act 1773.\n2. 1861: Indian High Courts Act abolished Supreme Courts & Sadar Adalats and created High Courts at Calcutta, Bombay, and Madras.\n3. 1937: Federal Court of India established under Government of India Act 1935.\n4. Jan 28, 1950: Supreme Court of India inaugurated under Article 124, replacing both Federal Court and Privy Council appellate jurisdiction.\nWhich of the statements given above are correct?",
    "இந்தியாவில் உச்ச நீதிமன்றம் மற்றும் நீதித்துறை அமைப்பின் வளர்ச்சி பற்றிய பின்வரும் ஒருங்கிணைந்த கூற்றுகளைக் கவனியுங்கள்:\n1. 1774: 1773 ஒழுங்குமுறைச் சட்டத்தின் கீழ் கொல்கத்தாவில் உச்ச நீதிமன்றம் அமைவு.\n2. 1861: உயர் நீதிமன்றங்கள் சட்டம் பழைய நீதிமன்றங்களைக் கலைத்து கொல்கத்தா, பம்பாய், மதராஸ் உயர் நீதிமன்றங்களை உருவாக்கியது.\n3. 1937: 1935 இந்திய அரசுச் சட்டத்தின் கீழ் இந்திய கூட்டாட்சி நீதிமன்றம் அமைவு.\n4. ஜனவரி 28, 1950: பிரிவு 124 இன் கீழ் இந்திய உச்ச நீதிமன்றம் தொடங்கப்பட்டு கூட்டாட்சி நீதிமன்றம் மற்றும் பிரிவி கவுன்சில் மேல்முறையீட்டு அதிகாரங்களை ஏற்றது.\nஎது சரி?",
    "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டும்",
    "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டும்",
    "1, 3 and 4 only", "1, 3 மற்றும் 4 மட்டும்",
    "1, 2, 3 and 4", "1, 2, 3 மற்றும் 4",
    "D",
    "All four statements are correct. Traces judicial evolution: 1774 Calcutta SC -> 1861 High Courts -> 1937 Federal Court -> Jan 28, 1950 Supreme Court of India.",
    "நான்கு கூற்றுகளும் சரியானவை. நீதித்துறை பாதை: 1774 கொல்கத்தா SC -> 1861 உயர் நீதிமன்றங்கள் -> 1937 கூட்டாட்சி நீதிமன்றம் -> 1950 ஜனவரி 28 உச்ச நீதிமன்றம்.",
    "Incorrect. Statement 4 is also correct.",
    "தவறு. கூற்று 4-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Correct. All four statements accurately describe the judicial evolutionary lineage.",
    "சரி. நான்கு கூற்றுகளும் நீதித்துறை வரலாற்றுப் பாதையைத் துல்லியமாக விவரிக்கின்றன.",
    "Abolition of Privy Council Jurisdiction Act was passed in 1949 to transfer all appellate jurisdiction to Federal Court before SC inauguration.",
    "1949 இல் பிரிவி கவுன்சில் அதிகார வரம்பு ஒழிப்புச் சட்டம் நிறைவேற்றப்பட்டு கூட்டாட்சி நீதிமன்றத்திற்கு மேல்முறையீடுகள் மாற்றப்பட்டன.",
    "Sir Maurice Gwyer was the first Chief Justice of Federal Court (1937); H.J. Kania was the first Chief Justice of independent India's Supreme Court (1950).",
    "சர் மோரிஸ் குவையர் கூட்டாட்சி நீதிமன்றத்தின் முதல் தலைமை நீதிபதி (1937); எச்.ஜே. கானியா இந்திய உச்ச நீதிமன்றத்தின் முதல் தலைமை நீதிபதி (1950).",
    "Analyze", 75, ["Polity", "Historical Background", "Judicial Hierarchy Arc", "Integrated Statement"]
))

# HB_SB_050
questions.append(make_q(
    "HB_SB_050", "Statement Based",
    "Consider the following integrated statements regarding direct borrowings of the 1950 Indian Constitution from colonial British Acts:\n1. Nearly 250 articles of the 1950 Constitution were directly adapted or modified from the Government of India Act 1935.\n2. The institutional framework of Bicameralism and Legislative Election procedures was adapted from the Government of India Act 1919.\n3. The Ordinance-making power of President/Governor and Portfolio System model were adapted from the Indian Councils Act 1861.\nWhich of the statements given above are correct?",
    "காலனித்துவ பிரிட்டிஷ் சட்டங்களிலிருந்து 1950 இந்திய அரசியலமைப்பு நேரடியாக எடுத்தாண்ட அம்சங்கள் பற்றிய பின்வரும் ஒருங்கிணைந்த கூற்றுகளைக் கவனியுங்கள்:\n1. 1950 அரசியலமைப்பின் சுமார் 250 விதிகள் 1935 இந்திய அரசுச் சட்டத்திலிருந்து நேரடியாகவோ அல்லது மாற்றங்களுடனோ எடுத்தாளப்பட்டன.\n2. ஈரவை முறை மற்றும் சட்டமன்ற தேர்தல் நடைமுறைகளின் நிறுவனக் கட்டமைப்பு 1919 இந்திய அரசுச் சட்டத்திலிருந்து பெறப்பட்டன.\n3. குடியரசுத் தலைவர்/ஆளுநரின் அவசரச்சட்ட அதிகாரம் மற்றும் துறை ஒதுக்கீடு மாதிரி ஆகியவை 1861 இந்தியக் கவுன்சில்கள் சட்டத்திலிருந்து பெறப்பட்டன.\nஎது சரி?",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "D",
    "All three statements are correct. 1950 Constitution borrowed ~250 articles from 1935 Act, bicameralism/election structures from 1919 Act, and portfolio/ordinance models from 1861 Act.",
    "மூன்று கூற்றுகளும் சரியானவை. 1950 அரசியலமைப்பு 1935 சட்டத்திலிருந்து ~250 விதிகள், 1919 சட்டத்திலிருந்து ஈரவை/தேர்தல், மற்றும் 1861 சட்டத்திலிருந்து போர்ட்ஃபோலியோ/அவசரச்சட்டம் ஆகியவற்றை எடுத்தாண்டது.",
    "Incorrect. Statement 3 is also correct.",
    "தவறு. கூற்று 3-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Correct. All three statements accurately synthesize the constitutional borrowings.",
    "சரி. மூன்று கூற்றுகளும் அரசியலமைப்புப் பெறல்களைத் துல்லியமாக ஒருங்கிணைக்கின்றன.",
    "Dr. B.R. Ambedkar famously remarked that the Drafting Committee made no apology for borrowing administrative details from the 1935 Act.",
    "1935 சட்டத்தின் நிர்வாக விவரங்களை எடுத்தாண்டதற்கு வரைவுக் குழு மன்னிப்பு கேட்காது என அம்பேத்கர் கூறினார்.",
    "Government of India Act 1935 formed the single largest source of the Indian Constitution.",
    "1935 இந்திய அரசுச் சட்டமே இந்திய அரசியலமைப்பின் மிகப்பெரிய ஒற்றை மூல ஆதாரமாகும்.",
    "Analyze", 75, ["Polity", "Historical Background", "Constitutional Borrowings Arc", "Integrated Statement"]
))

# Sort all 50 questions by ID
questions.sort(key=lambda x: x["id"])

# Save complete repository
with open(target_path, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"Total Questions in Repository: {len(questions)}")

# Validate with validators.py
sys.path.insert(0, r"c:\Users\Home\Desktop\tnpsc_ai")
from core.question_engine.validators import validate_questions
val_res = validate_questions(questions)
print(f"Validation Result: Valid={val_res.valid}")
if val_res.errors:
    print("Validation Errors:", val_res.errors)
if val_res.warnings:
    print("Validation Warnings:", val_res.warnings)
