import json
import sys
from pathlib import Path

# Load first 20 questions
target_path = Path(r"c:\Users\Home\Desktop\tnpsc_ai\data\questions\polity\historical_background_medium.json")
with open(target_path, "r", encoding="utf-8") as f:
    questions = json.load(f)

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
        "difficulty": "Medium",
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

# ---------------------------------------------------------
# REMAINING STATEMENT BASED QUESTIONS (HB_M_021 to HB_M_025)
# ---------------------------------------------------------

questions.append(make_q(
    "HB_M_021", "Statement Based",
    "Consider the following statements regarding the Indian Councils Act of 1909 (Morley-Minto Reforms):\n1. It retained an official majority in the Central Legislative Council but allowed Provincial Legislative Councils to have a non-official majority.\n2. It introduced separate electorates for Muslims, where Muslim members were elected only by Muslim voters.\n3. It empowered members to ask supplementary questions and move resolutions on the budget for the first time.\nWhich of the statements given above are correct?",
    "1909 ஆம் ஆண்டின் இந்தியக் கவுன்சில்கள் சட்டம் (மோர்லே-மிண்டோ சீர்திருத்தங்கள்) பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது மத்திய சட்டமன்ற கவுன்சிலில் அரசு அதிகாரிகளின் பெரும்பான்மையைத் தக்கவைத்துக் கொண்டது, ஆனால் மாகாண சட்டமன்ற கவுன்சில்களில் அரசுசாரா பெரும்பான்மையை அனுமதித்தது.\n2. இது முஸ்லிம்களுக்குத் தனித் தொகுதிகளை அறிமுகப்படுத்தியது, அங்கு முஸ்லிம் உறுப்பினர்கள் முஸ்லிம் வாக்காளர்களால் மட்டுமே தேர்ந்தெடுக்கப்பட்டனர்.\n3. உறுப்பினர்கள் முதன்முறையாகத் துணைக் கேள்விகள் கேட்கவும் வரவு செலவுத் திட்டத்தின் மீது தீர்மானங்களைக் கொண்டு வரவும் இது அதிகாரமளித்தது.\nஎது சரி?",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "D",
    "All three statements are correct. Central council retained official majority (16 to 60 expansion), provincial councils got non-official majority, separate electorates for Muslims were introduced, and supplementary questions & budget resolutions were allowed.",
    "மூன்று கூற்றுகளும் சரியானவை. மத்திய கவுன்சிலில் அரசுப் பெரும்பான்மை தக்கவைக்கப்பட்டது, மாகாண கவுன்சில்களில் அரசுசாரா பெரும்பான்மை அனுமதிக்கப்பட்டது, முஸ்லிம்களுக்குத் தனித் தொகுதி வழங்கப்பட்டது, மற்றும் துணைக் கேள்விகள்/தீர்மானங்கள் அனுமதிக்கப்பட்டன.",
    "Incorrect. Statement 3 is also correct.",
    "தவறு. கூற்று 3-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Correct. All three statements accurately describe the 1909 Act features.",
    "சரி. மூன்று கூற்றுகளும் 1909 சட்டத்தின் அம்சங்களைச் சரியாக விவரிக்கின்றன.",
    "Notice the distinction: 1909 Act allowed NON-OFFICIAL majority in Provincial Councils, but NOT elected Indian majority.",
    "வேறுபாட்டைக் கவனிக்கவும்: 1909 சட்டம் மாகாண கவுன்சில்களில் அரசுசாரா பெரும்பான்மையை அனுமதித்தது, தேர்ந்தெடுக்கப்பட்ட இந்திய பெரும்பான்மையை அல்ல.",
    "The 1909 Act expanded the Central Legislative Council size from 16 to 60 members.",
    "1909 சட்டம் மத்திய சட்டமன்ற கவுன்சிலின் அளவை 16 லிருந்து 60 உறுப்பினர்களாக உயர்த்தியது.",
    "Analyze", 75, ["Polity", "Historical Background", "Indian Councils Act 1909", "Morley-Minto"]
))

questions.append(make_q(
    "HB_M_022", "Statement Based",
    "Consider the following statements regarding the Government of India Act 1919:\n1. It created a new office of the High Commissioner for India in London and transferred to him some of the functions performed by the Secretary of State.\n2. It extended the principle of communal representation by providing separate electorates for Sikhs, Indian Christians, Anglo-Indians, and Europeans.\n3. It provided for the appointment of a statutory commission after ten years to inquire into the working of the system.\nWhich of the statements given above are correct?",
    "1919 ஆம் ஆண்டின் இந்திய அரசுச் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது லண்டனில் இந்திய உயர் ஆணையர் என்ற புதிய அலுவலகத்தை உருவாக்கி, இந்திய அரசுச் செயலாளர் செய்து வந்த சில பணிகளை அவருக்கு மாற்றியது.\n2. இது சீக்கியர்கள், இந்தியக் கிறிஸ்தவர்கள், ஆங்கிலோ-இந்தியர்கள் மற்றும் ஐரோப்பியர்களுக்குத் தனித் தொகுதிகளை வழங்கி வகுப்புவாதப் பிரதிநிதித்துவக் கோட்பாட்டை விரிவுபடுத்தியது.\n3. இச்சமைக்கப்பட்ட அமைப்பின் செயல்பாடுகளை ஆராய பத்து ஆண்டுகளுக்குப் பிறகு ஒரு சட்டப்பூர்வ ஆணையத்தை நியமிக்க வழிவகை செய்தது.\nஎது சரி?",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "D",
    "All three statements are correct. Created High Commissioner for India in London, extended communal electorates to Sikhs, Christians, Anglo-Indians, and Europeans, and mandated a Statutory Commission (which became Simon Commission in 1927).",
    "மூன்று கூற்றுகளும் சரியானவை. லண்டனில் உயர் ஆணையர் அலுவலகத்தை உருவாக்கியது, சீக்கியர்கள், கிறிஸ்தவர்கள், ஆங்கிலோ-இந்தியர்கள், ஐரோப்பியர்களுக்குத் தனித் தொகுதி வழங்கியது, மற்றும் 10 ஆண்டிற்கு பின் சட்டப்பூர்வ ஆணையத்திற்கு (சைமன் குழு 1927) வழிவகை செய்தது.",
    "Incorrect. Statement 3 is also correct.",
    "தவறு. கூற்று 3-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Correct. All three statements are true.",
    "சரி. மூன்று கூற்றுகளும் உண்மையானவை.",
    "GOI Act 1919 provided for a Statutory Commission after 10 years, which led to the appointment of the Simon Commission in November 1927 (2 years early).",
    "1919 சட்டத்தின் 10 ஆண்டு சட்டப்பூர்வ ஆணைய விதியே 1927 நவம்பரில் சைமன் குழு நியமிக்கப்படக் காரணமானது.",
    "GOI Act 1919 introduced bicameralism at the Centre (Council of State & Legislative Assembly).",
    "1919 இந்திய அரசுச் சட்டம் மத்திய சட்டமன்றத்தில் ஈரவை முறையை (மாநிலங்கள் அவை & சட்டமன்றப் பேரவை) அறிமுகப்படுத்தியது.",
    "Analyze", 75, ["Polity", "Historical Background", "Government of India Act 1919", "Statutory Commission"]
))

questions.append(make_q(
    "HB_M_023", "Statement Based",
    "Consider the following statements regarding the Government of India Act 1935:\n1. It introduced Bicameralism in 6 out of 11 provinces: Bengal, Bombay, Madras, Bihar, Assam, and the United Provinces.\n2. It abolished Dyarchy in the provinces and introduced Provincial Autonomy in its place.\n3. It vested the residuary legislative powers directly in the Federal Legislature.\nWhich of the statements given above is/are correct?",
    "1935 ஆம் ஆண்டின் இந்திய அரசுச் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது 11 மாகாணங்களில் 6 மாகாணங்களில் (வங்காளம், பம்பாய், மதராஸ், பீகார், அசாம் மற்றும் ஐக்கிய மாகாணங்கள்) ஈரவை முறையை அறிமுகப்படுத்தியது.\n2. இது மாகாணங்களில் இரட்டை ஆட்சியை நீக்கி அதற்கு பதிலாக மாகாண தன்னாட்சியை அறிமுகப்படுத்தியது.\n3. இது எஞ்சிய சட்டமியற்றும் அதிகாரங்களை நேரடியாக கூட்டாட்சி சட்டமன்றத்திடம் ஒப்படைத்தது.\nஎது சரி?",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "A",
    "Statement 1 is correct (bicameralism in 6 provinces). Statement 2 is correct (provincial dyarchy abolished, provincial autonomy introduced). Statement 3 is INCORRECT because residuary powers were vested in the Governor-General (Viceroy), NOT in the federal legislature.",
    "கூற்று 1 சரி (6 மாகாணங்களில் ஈரவை முறை). கூற்று 2 சரி (மாகாண இரட்டை ஆட்சி நீக்கப்பட்டு தன்னாட்சி வந்தது). கூற்று 3 தவறு, ஏனெனில் எஞ்சிய அதிகாரங்கள் வைஸ்ராயிடம் (கவர்னர் ஜெனரல்) வழங்கப்பட்டன, கூட்டாட்சி சட்டமன்றத்திடம் அல்ல.",
    "Correct. Statements 1 and 2 are true; Statement 3 is false.",
    "சரி. கூற்றுகள் 1 மற்றும் 2 சரி; கூற்று 3 தவறு.",
    "Incorrect. Statement 3 is false.",
    "தவறு. கூற்று 3 தவறானது.",
    "Incorrect. Statement 3 is false.",
    "தவறு. கூற்று 3 தவறானது.",
    "Incorrect. Statement 3 is false.",
    "தவறு. கூற்று 3 தவறானது.",
    "TNPSC Trap: Under 1935 Act, Residuary Powers were NOT given to Federal or Provincial lists, but to Governor-General personally.",
    "TNPSC பொறி: 1935 சட்டத்தில் எஞ்சிய அதிகாரங்கள் கூட்டாட்சி அல்லது மாகாணப் பட்டியலுக்கு வழங்கப்படவில்லை, கவர்னர் ஜெனரலிடம் வழங்கப்பட்டன.",
    "Government of India Act 1935 extended communal representation to Scheduled Castes, Women, and Workers (Labour).",
    "1935 சட்டம் பட்டியல் சாதியினர், பெண்கள் மற்றும் தொழிலாளர்களுக்கு வகுப்புவாத பிரதிநிதித்துவத்தை விரிவுபடுத்தியது.",
    "Analyze", 75, ["Polity", "Historical Background", "Government of India Act 1935", "Residuary Powers"]
))

questions.append(make_q(
    "HB_M_024", "Statement Based",
    "Consider the following statements regarding the Indian Independence Act of 1947:\n1. It proclaimed the lapse of British paramountcy over the Indian Princely States and treaty relations with tribal areas from August 15, 1947.\n2. It granted freedom to Indian Princely States either to join the Dominion of India or Dominion of Pakistan or to remain independent.\n3. It designated the Governor-General of India and provincial governors as constitutional (nominal) heads of the states.\nWhich of the statements given above are correct?",
    "1947 ஆம் ஆண்டின் இந்திய சுதந்திரச் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது ஆகஸ்ட் 15, 1947 முதல் இந்திய சுதேச சமஸ்தானங்கள் மீதான பிரிட்டிஷ் மேலாதிக்கம் மற்றும் பழங்குடி பகுதிகளுடனான ஒப்பந்த உறவுகள் முடிவுக்கு வந்ததாக அறிவித்தது.\n2. இது இந்திய சுதேச சமஸ்தானங்களுக்கு இந்திய டொமினியன் அல்லது பாகிஸ்தான் டொமினியனில் இணையவோ அல்லது சுதந்திரமாக இருக்கவோ சுதந்திரம் அளித்தது.\n3. இது இந்திய கவர்னர் ஜெனரல் மற்றும் மாகாண கவர்னர்களை அரசியலமைப்பு ரீதியான (பெயரளவு) தலைவர்களாக நியமித்தது.\nஎது சரி?",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "D",
    "All three statements are correct. Lapse of paramountcy took place, Princely States were given 3 choices (India, Pakistan, or Independent), and GG and provincial governors became nominal constitutional heads bound by council of ministers.",
    "மூன்று கூற்றுகளும் சரியானவை. மேலாதிக்கம் முடிந்தது, சுதேச சமஸ்தானங்களுக்கு 3 தேர்வுகள் அளிக்கப்பட்டன, மற்றும் கவர்னர் ஜெனரல்/மாகாண கவர்னர்கள் பெயரளவு தலைவர்களாயினர்.",
    "Incorrect. Statement 3 is also correct.",
    "தவறு. கூற்று 3-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Correct. All three statements accurately reflect the Indian Independence Act 1947 provisions.",
    "சரி. மூன்று கூற்றுகளும் 1947 சுதந்திரச் சட்ட விதிகளைச் சரியாகப் பிரதிபலிக்கின்றன.",
    "Lord Mountbatten became the first Governor-General of independent India; C. Rajagopalachari became the first and last Indian Governor-General of free India.",
    "சுதந்திர இந்தியாவின் முதல் கவர்னர் ஜெனரலாக மவுண்ட்பேட்டன் பிரபுவும், முதல் மற்றும் கடைசி இந்திய கவர்னர் ஜெனரலாக சி. ராஜகோபாலாச்சாரியும் இருந்தனர்.",
    "Indian Independence Act 1947 was passed by British Parliament on July 18, 1947.",
    "1947 இந்திய சுதந்திரச் சட்டம் ஜூலை 18, 1947 இல் பிரிட்டிஷ் பாராளுமன்றத்தால் நிறைவேற்றப்பட்டது.",
    "Analyze", 75, ["Polity", "Historical Background", "Indian Independence Act 1947", "Lapse of Paramountcy"]
))

questions.append(make_q(
    "HB_M_025", "Statement Based",
    "Consider the following statements regarding the evolutionary trajectory of centralization and decentralization in British Indian administration:\n1. The process of administrative centralization reached its climax under the Charter Act of 1833.\n2. The Indian Councils Act of 1861 marked the beginning of legislative decentralization by returning legislative powers to Madras and Bombay.\n3. The Government of India Act 1935 completed the provincial autonomy scheme by introducing responsible provincial governments.\nWhich of the statements given above are correct?",
    "பிரிட்டிஷ் இந்திய நிர்வாகத்தில் மத்தியமயமாக்கல் மற்றும் பரவலாக்கலின் வரலாற்றுப் பாதை பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. நிர்வாக மத்தியமயமாக்கல் செயல்முறை 1833 ஆம் ஆண்டின் சாசனச் சட்டத்தின் கீழ் அதன் உச்சத்தை அடைந்தது.\n2. 1861 ஆம் ஆண்டின் இந்தியக் கவுன்சில்கள் சட்டம் மதராஸ் மற்றும் பம்பாய்க்கு சட்ட அதிகாரங்களை மீண்டும் வழங்கி சட்டமன்ற பரவலாக்கலைத் தொடங்கியது.\n3. 1935 ஆம் ஆண்டின் இந்திய அரசுச் சட்டம் பொறுப்புள்ள மாகாண அரசாங்கங்களை அறிமுகப்படுத்தியதன் மூலம் மாகாண தன்னாட்சித் திட்டத்தை முழுமைப்படுத்தியது.\nஎது சரி?",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "D",
    "All three statements are correct. 1833 was peak centralization; 1861 initiated decentralization; 1935 established full Provincial Autonomy.",
    "மூன்று கூற்றுகளும் சரியானவை. 1833 உச்சகட்ட மத்தியமயமாக்கல்; 1861 பரவலாக்கலின் தொடக்கம்; 1935 முழு மாகாண தன்னாட்சி.",
    "Incorrect. Statement 3 is also correct.",
    "தவறு. கூற்று 3-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Correct. All statements trace the administrative pendulum from centralization to decentralization accurately.",
    "சரி. அனைத்துக் கூற்றுகளும் மத்தியமயமாக்கலிலிருந்து பரவலாக்கலுக்கான கட்டமைப்பு மாற்றத்தைச் சரியாக விவரிக்கின்றன.",
    "Remember the trajectory: 1773 (start of centralization) -> 1833 (peak centralization) -> 1861 (turning point to decentralization) -> 1935 (full provincial autonomy).",
    "வளர்ச்சிப் பாதையை நினைவில் கொள்க: 1773 (தொடக்கம்) -> 1833 (உச்சம்) -> 1861 (பரவலாக்கல் தொடக்கம்) -> 1935 (முழு மாகாண தன்னாட்சி).",
    "Provincial autonomy under 1935 Act came into force in 1937 and was discontinued in 1939 when Congress ministers resigned.",
    "1935 சட்டத்தின் மாகாண தன்னாட்சி 1937 இல் அமலுக்கு வந்தது, 1939 இல் காங்கிரஸ் அமைச்சர்கள் ராஜினாமா செய்தபோது நிறுத்தப்பட்டது.",
    "Analyze", 75, ["Polity", "Historical Background", "Administrative Evolution", "Decentralization"]
))

# ---------------------------------------------------------
# 5 CAUSE & EFFECT QUESTIONS (HB_M_026 to HB_M_030)
# ---------------------------------------------------------

questions.append(make_q(
    "HB_M_026", "Cause & Effect",
    "Cause: The Great Bengal Famine of 1770 and rampant corruption among East India Company servants led to severe financial distress, forcing the Company to apply for a loan of £1 million from the British Government.\nWhat was the immediate Constitutional Effect of this crisis?",
    "காரணம்: 1770 ஆம் ஆண்டின் பெரும் வங்காளப் பஞ்சமும் கிழக்கிந்தியக் கம்பெனி ஊழியர்களின் ஊழலும் கடுமையான நிதி நெருக்கடியை ஏற்படுத்தி, பிரிட்டிஷ் அரசிடம் 1 மில்லியன் பவுண்ட் கடன் கேட்க நிர்பந்தித்தன.\nஇந்த நெருக்கடியின் உடனடி அரசியலமைப்பு விளைவு யாது?",
    "Enactment of the Regulating Act of 1773 to control and regulate the affairs of the East India Company.",
    "கிழக்கிந்தியக் கம்பெனியின் விவகாரங்களைக் கட்டுப்படுத்தவும் முறைப்படுத்தவும் 1773 ஆம் ஆண்டின் ஒழுங்குமுறைச் சட்டம் இயற்றப்பட்டமை.",
    "Immediate abolition of the East India Company and transfer of power to the Crown.",
    "கிழக்கிந்தியக் கம்பெனியை உடனடியாகக் கலைத்து பிரிட்டிஷ் அரசிற்கு அதிகாரத்தை மாற்றியமை.",
    "Establishment of the Reserve Bank of India to manage Company currency.",
    "கம்பெனி பணத்தை நிர்வகிக்க இந்திய ரிசர்வ் வங்கியை நிறுவியமை.",
    "Appointment of the Lee Commission to restructure civil services.",
    "குடிமைப் பணிகளை சீரமைக்க லீ ஆணையத்தை நியமித்தமை.",
    "A",
    "The financial bankruptcy of EIC and corruption of servants forced the British Parliament to pass the Regulating Act of 1773, marking the first step towards parliamentary control over the Company in India.",
    "EIC இன் நிதி நெருக்கடியும் ஊழியர்களின் ஊழலும் பிரிட்டிஷ் பாராளுமன்றத்தை 1773 ஒழுங்குமுறைச் சட்டத்தை இயற்ற வைத்து கம்பெனி மீதான முதல் பாராளுமன்றக் கட்டுப்பாட்டை ஏற்படுத்தின.",
    "Correct. Regulating Act of 1773 was the direct outcome of EIC financial crisis and corruption.",
    "சரி. 1773 ஒழுங்குமுறைச் சட்டம் EIC நிதி நெருக்கடி மற்றும் ஊழலின் நேரடி விளைவாகும்.",
    "Incorrect. Transfer of power to Crown happened after 1857 revolt (1858 Act).",
    "தவறு. பிரிட்டிஷ் அரசிற்கு அதிகார மாற்றம் 1857 கிளர்ச்சிக்குப் பிறகே (1858 சட்டம்) நடந்தது.",
    "Incorrect. Reserve Bank of India was set up in 1935.",
    "தவறு. ரிசர்வ் வங்கி 1935 இல் அமைக்கப்பட்டது.",
    "Incorrect. Lee Commission was appointed in 1923.",
    "தவறு. லீ ஆணையம் 1923 இல் நியமிக்கப்பட்டது.",
    "Connect historical events: 1770 Famine & Financial collapse -> 1773 Regulating Act (First parliamentary intervention).",
    "வரலாற்று நிகழ்வுகளை இணைக்கவும்: 1770 பஞ்சமும் நிதிச் சரிவும் -> 1773 ஒழுங்குமுறைச் சட்டம்.",
    "Regulating Act 1773 recognized for the first time the political and administrative functions of the Company.",
    "1773 ஒழுங்குமுறைச் சட்டம் முதன்முறையாக கம்பெனியின் அரசியல் மற்றும் நிர்வாகப் பணிகளை அங்கீகரித்தது.",
    "Apply", 60, ["Polity", "Historical Background", "Regulating Act 1773", "Cause and Effect"]
))

questions.append(make_q(
    "HB_M_027", "Cause & Effect",
    "Cause: Severe jurisdictional conflicts and deadlock arose between the Supreme Court of Judicature at Calcutta and the Governor-General in Council over executive revenue actions.\nWhat was the direct Constitutional Effect of this conflict?",
    "காரணம்: கொல்கத்தா உச்ச நீதிமன்றத்திற்கும் கவர்னர் ஜெனரல் கவுன்சிலுக்கும் இடையே நிர்வாக வருவாய் நடவடிக்கைகள் தொடர்பாக கடுமையான அதிகார வரம்பு மோதல்களும் முட்டுக்கட்டையும் எழுந்தன.\nஇந்த மோதலின் நேரடி அரசியலமைப்பு விளைவு யாது?",
    "Passing of the Amending Act of 1781 (Act of Settlement) to exempt the Governor-General, council, and revenue collectors from Supreme Court jurisdiction.",
    "கவர்னர் ஜெனரல், கவுன்சில் மற்றும் வருவாய் வசூலிப்பாளர்களை உச்ச நீதிமன்ற அதிகார வரம்பிலிருந்து விலக்க 1781 ஆம் ஆண்டின் திருத்தச் சட்டம் (சமரசச் சட்டம்) நிறைவேற்றப்பட்டமை.",
    "Abolition of the Supreme Court at Calcutta and creation of High Courts.",
    "கொல்கத்தா உச்ச நீதிமன்றத்தைக் கலைத்து உயர் நீதிமன்றங்களை உருவாக்கியமை.",
    "Resignation of Warren Hastings as Governor-General.",
    "வாரன் ஹேஸ்டிங்ஸ் கவர்னர் ஜெனரல் பதவியை ராஜினாமா செய்தமை.",
    "Enactment of Charter Act of 1813 to remove judicial powers.",
    "நீதித்துறை அதிகாரங்களை நீக்க 1813 சாசனச் சட்டத்தை இயற்றியமை.",
    "A",
    "To resolve the tussle between Supreme Court (headed by Impey) and Governor-General in Council (Hastings), Parliament passed Amending Act 1781, excluding revenue matters and official executive acts from Supreme Court jurisdiction.",
    "உச்ச நீதிமன்றத்திற்கும் கவர்னர் ஜெனரல் கவுன்சிலுக்கும் இடையிலான மோதலைத் தீர்க்க 1781 திருத்தச் சட்டம் இயற்றப்பட்டு வருவாய் மற்றும் அதிகாரப்பூர்வப் பணிகள் நீதிமன்ற அதிகார வரம்பிலிருந்து நீக்கப்பட்டன.",
    "Correct. Amending Act 1781 (Act of Settlement) directly resolved this conflict.",
    "சரி. 1781 திருத்தச் சட்டம் (சமரசச் சட்டம்) இந்த மோதலை நேரடியாகத் தீர்த்தது.",
    "Incorrect. Supreme Court was not abolished; High Courts were created much later in 1861.",
    "தவறு. உச்ச நீதிமன்றம் கலைக்கப்படவில்லை; உயர் நீதிமன்றங்கள் 1861 இல் உருவாக்கப்பட்டன.",
    "Incorrect. Warren Hastings did not resign due to this 1781 Act.",
    "தவறு. வாரன் ஹேஸ்டிங்ஸ் 1781 சட்டத்தினால் ராஜினாமா செய்யவில்லை.",
    "Incorrect. Charter Act 1813 was passed for trade monopoly reasons.",
    "தவறு. 1813 சாசனச் சட்டம் வர்த்தக ஏகபோகப் காரணங்களுக்காக இயற்றப்பட்டது.",
    "1781 Act is explicitly titled 'Act of Settlement' because it settled the conflict between Executive and Supreme Court.",
    "1781 சட்டம் 'சமரசச் சட்டம்' எனப்படுகிறது, ஏனெனில் இது நிர்வாகத்திற்கும் நீதிமன்றத்திற்கும் இடையிலான மோதலைத் தீர்த்தது.",
    "The 1781 Act also declared that Mohammedan law apply to Muslims and Hindu law apply to Hindus in personal matters before SC.",
    "1781 சட்டம் தனிநபர் விவகாரங்களில் முஸ்லிம்களுக்கு இசுலாமிய சட்டமும் இந்துக்களுக்கு இந்து சட்டமும் பொருந்தும் எனத் தெளிவுபடுத்தியது.",
    "Apply", 60, ["Polity", "Historical Background", "Amending Act 1781", "Cause and Effect"]
))

questions.append(make_q(
    "HB_M_028", "Cause & Effect",
    "Cause: The Industrial Revolution in Britain generated powerful British merchant lobbies demanding laissez-faire economic policies and access to Indian markets.\nWhat was the direct Legislative Effect on East India Company's monopoly in India?",
    "காரணம்: பிரிட்டனில் ஏற்பட்ட தொழிற்புரட்சி, தாராளமய பொருளாதாரக் கொள்கைகளையும் இந்திய சந்தைகளில் அணுகலையும் கோரும் சக்திவாய்ந்த பிரிட்டிஷ் வர்த்தகக் குழுக்களை உருவாக்கியது.\nஇந்தியாவில் கிழக்கிந்தியக் கம்பெனியின் ஏகபோகத்தின் மீதான நேரடி சட்ட விளைவு யாது?",
    "Enactment of the Charter Act of 1813, which abolished the Company's trade monopoly in India except for trade in Tea and trade with China.",
    "தேயிலை வர்த்தகம் மற்றும் சீனாவுடனான வர்த்தகம் தவிர இந்தியாவில் கம்பெனியின் வர்த்தக ஏகபோகத்தை ரத்து செய்த 1813 ஆம் ஆண்டின் சாசனச் சட்டத்தை இயற்றியமை.",
    "Complete abolition of all British trade in Asia.",
    "ஆசியாவில் அனைத்து பிரிட்டிஷ் வர்த்தகத்தையும் முழுமையாக ரத்து செய்தமை.",
    "Enactment of Pitt's India Act of 1784 granting monopoly forever.",
    "ஏகபோகத்தை என்றென்றும் வழங்கும் 1784 பிட் இந்தியச் சட்டத்தை இயற்றியமை.",
    "Transfer of trade monopoly directly to French merchants.",
    "வர்த்தக ஏகபோகத்தை நேரடியாக பிரெஞ்சு வர்த்தகர்களுக்கு மாற்றியமை.",
    "A",
    "Industrial Revolution produced surplus manufactured goods in Britain. British merchants demanded end to EIC monopoly. Charter Act 1813 abolished EIC trade monopoly in India except Tea and China trade (which were abolished in 1833).",
    "தொழிற்புரட்சியால் பிரிட்டன் வணிகர்கள் கம்பெனி ஏகபோகத்தை எதிர்க்கத் தொடங்கினர். 1813 சாசனச் சட்டம் தேயிலை மற்றும் சீனா வர்த்தகம் தவிர கம்பெனியின் ஏகபோகத்தை முடிவுக்குக் கொண்டு வந்தது.",
    "Correct. Charter Act 1813 ended Indian trade monopoly except Tea and China trade.",
    "சரி. 1813 சாசனச் சட்டம் தேயிலை மற்றும் சீனா வர்த்தகம் தவிர ஏகபோகத்தை ரத்து செய்தது.",
    "Incorrect. British trade expanded, not abolished.",
    "தவறு. பிரிட்டிஷ் வர்த்தகம் விரிவடைந்தது, ரத்து செய்யப்படவில்லை.",
    "Incorrect. Pitt's Act 1784 did not address trade monopoly.",
    "தவறு. 1784 பிட் சட்டம் வர்த்தக ஏகபோகத்தைப் பற்றியது அல்ல.",
    "Incorrect. Trade was opened to all British merchants, not French.",
    "தவறு. வர்த்தகம் அனைத்து பிரிட்டிஷ் வணிகர்களுக்கும் திறக்கப்பட்டது.",
    "Sequence of Monopoly abolition: 1813 Act (Partial abolition: except Tea & China) -> 1833 Act (Total abolition).",
    "ஏகபோக ஒழிப்பு வரிசை: 1813 சட்டம் (பகுதி ஒழிப்பு: தேயிலை & சீனா தவிர) -> 1833 சட்டம் (முழுமையான ஒழிப்பு).",
    "Charter Act 1813 explicitly asserted the sovereignty of the British Crown over Company territories in India.",
    "1813 சாசனச் சட்டம் கம்பெனியின் இந்தியப் பகுதிகள் மீது பிரிட்டிஷ் முடிஅரசின் இறையாண்மையை வெளிப்படையாக அறிவித்தது.",
    "Apply", 60, ["Polity", "Historical Background", "Charter Act 1813", "Cause and Effect"]
))

questions.append(make_q(
    "HB_M_029", "Cause & Effect",
    "Cause: The Revolt of 1857 (First War of Indian Independence) exposed severe systemic failures, corruption, and instability of East India Company rule.\nWhat was the immediate Constitutional Effect enacted by the British Parliament?",
    "காரணம்: 1857 ஆம் ஆண்டின் பெரும் புரட்சி (முதல் இந்திய சுதந்திரப் போர்) கிழக்கிந்தியக் கம்பெனி ஆட்சியின் அமைப்புரீதியான குறைபாடுகளையும் நிலையற்ற தன்மையையும் வெளிப்படுத்தியது.\nபிரிட்டிஷ் பாராளுமன்றத்தால் இயற்றப்பட்ட உடனடி அரசியலமைப்பு விளைவு யாது?",
    "Passing of the Government of India Act 1858, liquidating the East India Company and transferring Indian governance directly to the British Crown.",
    "கிழக்கிந்தியக் கம்பெனியைக் கலைத்து இந்திய நிர்வாகத்தை நேரடியாக பிரிட்டிஷ் அரசிற்கு மாற்றிய 1858 ஆம் ஆண்டின் இந்திய அரசுச் சட்டத்தை நிறைவேற்றியமை.",
    "Signing of the Treaty of Allahabad with Princely States.",
    "சுதேச சமஸ்தானங்களுடன் அலகாபாத் ஒப்பந்தத்தில் கையெழுத்திட்டமை.",
    "Enactment of Indian Councils Act 1909 to grant independence.",
    "சுதந்திரம் வழங்க 1909 இந்தியக் கவுன்சில்கள் சட்டத்தை இயற்றியமை.",
    "Creation of the Indian National Congress to handle complaints.",
    "புகார்களைக் கையாள இந்திய தேசிய காங்கிரஸை உருவாக்கியமை.",
    "A",
    "The 1857 Revolt led directly to the enactment of GOI Act 1858 ('Act for Good Government of India'), abolishing EIC rule, terminating Board of Control & Court of Directors, and establishing direct Crown Rule via Secretary of State & Viceroy.",
    "1857 புரட்சியின் நேரடி விளைவாக 1858 இந்திய அரசுச் சட்டம் இயற்றப்பட்டு கம்பெனி ஆட்சி கலைக்கப்பட்டு பிரிட்டிஷ் மகாராணியின் நேரடி ஆட்சித் தொடங்கியது.",
    "Correct. GOI Act 1858 transferred government directly to British Crown.",
    "சரி. 1858 இந்திய அரசுச் சட்டம் அதிகாரத்தை பிரிட்டிஷ் அரசிற்கு நேரடியாக மாற்றியது.",
    "Incorrect. Treaty of Allahabad was signed much earlier in 1765.",
    "தவறு. அலகாபாத் ஒப்பந்தம் 1765 இல் கையெழுத்தானது.",
    "Incorrect. 1909 Act came much later.",
    "தவறு. 1909 சட்டம் பிற்காலத்தில் வந்தது.",
    "Incorrect. INC was formed in 1885 by A.O. Hume.",
    "தவறு. காங்கிரஸ் 1885 இல் ஏ.ஓ. ஹியூமால் தொடங்கப்பட்டது.",
    "Queen Victoria's Proclamation was read out by Lord Canning at Allahabad Durbar on November 1, 1858, announcing the Crown takeover.",
    "விக்டோரியா மகாராணியின் அறிக்கை 1858 நவம்பர் 1 அன்று அலகாபாத் தர்பாரில் லார்ட் கேனிங்கால் படிக்கப்பட்டது.",
    "Lord Canning was the Governor-General during 1857 Revolt and became the first Viceroy under 1858 Act.",
    "1857 கிளர்ச்சியின் போது கவர்னர் ஜெனரலாக இருந்த கேனிங் பிரபு 1858 சட்டத்தின் கீழ் முதல் வைஸ்ராயானார்.",
    "Apply", 60, ["Polity", "Historical Background", "Government of India Act 1858", "Cause and Effect"]
))

questions.append(make_q(
    "HB_M_030", "Cause & Effect",
    "Cause: The August Declaration of 1917 by Secretary of State Edwin Montagu stated that the objective of British policy was 'gradual development of self-governing institutions with a view to progressive realization of responsible government in India'.\nWhat was the direct Legislative Effect resulting from this declaration?",
    "காரணம்: 1817 ஆகஸ்ட் பிரகடனத்தில் அரசுச் செயலாளர் எட்வின் மாண்டேகு 'இந்தியாவில் பொறுப்புள்ள அரசாங்கத்தை படிப்படியாக நிறுவுவதே பிரிட்டிஷ் கொள்கையின் நோக்கம்' எனக் கூறினார்.\nஇந்த அறிவிப்பால் ஏற்பட்ட நேரடி சட்ட விளைவு யாது?",
    "Enactment of the Government of India Act 1919, which introduced Responsible Government in provincial transferred subjects via Dyarchy.",
    "மாகாண மாற்றப்பட்ட துறைகளில் இரட்டை ஆட்சி மூலம் பொறுப்புள்ள அரசாங்கத்தை அறிமுகப்படுத்திய 1919 ஆம் ஆண்டின் இந்திய அரசுச் சட்டத்தை இயற்றியமை.",
    "Granting of immediate Dominion Status to India in 1919.",
    "1919 இல் இந்தியாவிற்கு உடனடியாக டொமினியன் அந்தஸ்து வழங்கியமை.",
    "Enactment of the Indian Independence Act 1947.",
    "1947 இந்திய சுதந்திரச் சட்டத்தை இயற்றியமை.",
    "Abolition of all Provincial Governors' offices.",
    "அனைத்து மாகாண கவர்னர்களின் அலுவலகங்களையும் கலைத்தமை.",
    "A",
    "Montagu's August Declaration (Aug 20, 1917) promised 'responsible government'. This led to Montagu-Chelmsford Report (1918) and the GOI Act 1919, which introduced partial responsible government in provinces through Dyarchy.",
    "மாண்டேகுவின் ஆகஸ்ட் பிரகடனம் (1917) 'பொறுப்புள்ள அரசாங்கத்தை' வாக்குறுதி அளித்தது. இதன் விளைவாக 1919 இந்திய அரசுச் சட்டம் மாகாணங்களில் இரட்டை ஆட்சி மூலம் பகுதி பொறுப்புள்ள அரசாங்கத்தை அமைத்தது.",
    "Correct. GOI Act 1919 was enacted to fulfill Montagu's 1917 declaration.",
    "சரி. மாண்டேகுவின் 1917 பிரகடனத்தை நிறைவேற்றவே 1919 இந்திய அரசுச் சட்டம் இயற்றப்பட்டது.",
    "Incorrect. Dominion status was not granted in 1919.",
    "தவறு. 1919 இல் டொமினியன் அந்தஸ்து வழங்கப்படவில்லை.",
    "Incorrect. 1947 Act came 30 years later.",
    "தவறு. 1947 சட்டம் 30 ஆண்டுகளுக்குப் பின்னரே வந்தது.",
    "Incorrect. Provincial Governors were retained.",
    "தவறு. மாகாண கவர்னர்கள் தக்கவைக்கப்பட்டனர்.",
    "Montagu Declaration of 1917 is called the 'August Declaration' (do not confuse with 'August Offer' of 1940 by Linlithgow).",
    "1917 மாண்டேகு பிரகடனம் 'ஆகஸ்ட் பிரகடனம்' எனப்படுகிறது (1940 லின்லித்கோவின் 'ஆகஸ்ட் சலுகை'யுடன் குழப்பக் கூடாது).",
    "Government of India Act 1919 came into force in 1921.",
    "1919 இந்திய அரசுச் சட்டம் 1921 இல் அமலுக்கு வந்தது.",
    "Apply", 60, ["Polity", "Historical Background", "Government of India Act 1919", "Cause and Effect"]
))

# Save checkpoint
with open(target_path, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"Added {len(questions)} questions.")
