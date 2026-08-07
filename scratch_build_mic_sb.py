import json
import sys
from pathlib import Path

target_path = Path(r"c:\Users\Home\Desktop\tnpsc_ai\data\questions\polity\making_of_indian_constitution_statement_based.json")
target_path.parent.mkdir(parents=True, exist_ok=True)

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
        "topic": "Making of Indian Constitution",
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
        "source_reference": ["M. Laxmikanth - Indian Polity", "NCERT Class 11 - Indian Constitution at Work", "Constituent Assembly Debates"],
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

questions = []

# =========================================================
# QUESTIONS 1 TO 10
# =========================================================

# MIC_SB_001
questions.append(make_q(
    "MIC_SB_001", "Statement Based",
    "With reference to the demand for a Constituent Assembly in pre-independence India, consider the following statements:\n1. M.N. Roy was the first to put forward the idea of a Constituent Assembly for India in 1934.\n2. The Indian National Congress officially demanded a Constituent Assembly for the first time in 1935.\n3. The British Government accepted the demand for a Constituent Assembly for the first time in principle in the Cripps Proposals of 1942.\nWhich of the statements given above are correct?",
    "சுதந்திரத்திற்கு முந்தைய இந்தியாவில் அரசியலமைப்பு நிர்ணய அவைகளுக்கான கோரிக்கை குறித்து பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 1934 இல் எம்.என். ராய் என்பவர்தான் முதன்முதலில் இந்தியாவிற்கான அரசியலமைப்பு நிர்ணய அவைக் கருத்தை முன்வைத்தார்.\n2. இந்திய தேசிய காங்கிரஸ் 1935 இல் முதன்முறையாக அரசியலமைப்பு நிர்ணய அவையைக் கோரி அதிகாரப்பூர்வமாக கோரிக்கை விடுத்தது.\n3. பிரிட்டிஷ் அரசாங்கம் 1942 இன் கிரிப்ஸ் தூதுக்குழு திட்டத்தில்தான் முதன்முதலில் அரசியலமைப்பு நிர்ணய அவைக் கோரிக்கையை கொள்கையளவில் ஏற்றுக்கொண்டது.\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "A",
    "Statements 1 and 2 are correct. Statement 3 is INCORRECT because the British Government accepted the demand for a Constituent Assembly for the first time IN PRINCIPLE in the 'August Offer' of 1940, not the Cripps Proposals of 1942 (the Cripps Proposals offered a concrete scheme for framing an independent constitution after WWII).",
    "கூற்றுகள் 1 மற்றும் 2 சரி. கூற்று 3 தவறு, ஏனெனில் பிரிட்டிஷ் அரசாங்கம் 1940 ஆம் ஆண்டின் 'ஆகஸ்ட் சலுகை'யில்தான் முதன்முதலில் கொள்கையளவில் அரசியலமைப்பு நிர்ணய அவைக் கோரிக்கையை ஏற்றுக்கொண்டது (1942 கிரிப்ஸ் திட்டம் அல்ல).",
    "Correct. Statements 1 and 2 are true; Statement 3 is false because August Offer 1940 accepted it in principle.", "சரி. கூற்றுகள் 1 மற்றும் 2 சரி; ஆகஸ்ட் சலுகை 1940 கொள்கையளவில் ஏற்றதால் கூற்று 3 தவறு.",
    "Incorrect. Statement 1 is true and Statement 3 is false.", "தவறு. கூற்று 1 சரி, கூற்று 3 தவறு.",
    "Incorrect. Statement 2 is true and Statement 3 is false.", "தவறு. கூற்று 2 சரி, கூற்று 3 தவறு.",
    "Incorrect. Statement 3 is incorrect.", "தவறு. கூற்று 3 தவறானது.",
    "TNPSC Trap: August Offer (1940) accepted the demand in principle; Cripps Offer (1942) proposed a concrete draft scheme; Cabinet Mission (1946) formed the actual Constituent Assembly.",
    "TNPSC பொறி: 1940 ஆகஸ்ட் சலுகை கொள்கையளவில் ஏற்றது; 1942 கிரிப்ஸ் திட்டம் வரைவுத் திட்டத்தை அளித்தது; 1946 கேபினட் தூதுக்குழு அவையை அமைத்தது.",
    "Jawaharlal Nehru declared in 1938 that the Constitution of free India must be framed without outside interference by a Constituent Assembly elected on adult franchise.",
    "1938 இல் ஜவகர்லால் நேரு வயதுவந்தோர் வாக்குரிமை அடிப்படையில் தேர்ந்தெடுக்கப்பட்ட அரசியலமைப்பு நிர்ணய அவையால் அரசியலமைப்பு உருவாக்கப்பட வேண்டும் என அறிவித்தார்.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "Demand for Constituent Assembly", "August Offer 1940"]
))

# MIC_SB_002
questions.append(make_q(
    "MIC_SB_002", "Statement Based",
    "With reference to the Cabinet Mission Plan of 1946, consider the following statements:\n1. The Cabinet Mission rejected the proposal for two Constituent Assemblies and recommended a single Constituent Assembly for undivided India.\n2. The Cabinet Mission comprised Lord Pethick-Lawrence, Sir Stafford Cripps, and A.V. Alexander, with Sir Stafford Cripps serving as its Chairman.\n3. The scheme proposed by the Cabinet Mission satisfied the Muslim League's demand for a fully sovereign independent Pakistan.\nWhich of the statements given above is/are correct?",
    "1946 இன் கேபினட் தூதுக்குழு திட்டம் குறித்து பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. கேபினட் தூதுக்குழு இரண்டு அரசியலமைப்பு நிர்ணய அவைகளுக்கான முன்மொழிவை நிராகரித்து, பிரிக்கப்படாத இந்தியாவிற்கு ஒரே ஒரு அவையைப் பரிந்துரைத்தது.\n2. கேபினட் தூதுக்குழுவில் பெதிக்-லாரன்ஸ் பிரபு, சர் ஸ்டாஃபோர்ட் கிரிப்ஸ் மற்றும் ஏ.வி. அலெக்சாண்டர் ஆகியோர் இடம் பெற்றிருந்தனர், அதில் சர் ஸ்டாஃபோர்ட் கிரிப்ஸ் தலைவராகச் செயல்பட்டார்.\n3. கேபினட் தூதுக்குழு முன்மொழிந்த திட்டம் முழுமையான இறையாண்மை கொண்ட சுதந்திர பாகிஸ்தானுக்கான முஸ்லீம் லீக்கின் கோரிக்கையை திருப்திப்படுத்தியது.\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1 only", "1 மட்டும்",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "A",
    "Statement 1 is correct. Statement 2 is INCORRECT because Lord Pethick-Lawrence (the Secretary of State for India) was the Chairman of the Cabinet Mission, not Sir Stafford Cripps. Statement 3 is INCORRECT because the Cabinet Mission explicitly rejected the Muslim League demand for Pakistan, though it grouped provinces to address Muslim concerns.",
    "கூற்று 1 சரி. கூற்று 2 தவறு, ஏனெனில் இந்திய அரசுச் செயலர் பெதிக்-லாரன்ஸ் பிரபுவே கேபினட் தூதுக்குழுவின் தலைவராவார் (ஸ்டாஃபோர்ட் கிரிப்ஸ் அல்ல). கூற்று 3 தவறு, ஏனெனில் கேபினட் தூதுக்குழு பாகிஸ்தான் கோரிக்கையை நிராகரித்தது.",
    "Correct. Statement 1 is true; Statements 2 and 3 are false.", "சரி. கூற்று 1 சரி; கூற்றுகள் 2 மற்றும் 3 தவறானவை.",
    "Incorrect. Statement 2 is false as Lord Pethick-Lawrence was the Chairman.", "தவறு. பெதிக்-லாரன்ஸ் தலைவராக இருந்ததால் கூற்று 2 தவறு.",
    "Incorrect. Both Statements 2 and 3 are false.", "தவறு. கூற்றுகள் 2 மற்றும் 3 இரண்டும் தவறானவை.",
    "Incorrect. Statements 2 and 3 are false.", "தவறு. கூற்றுகள் 2 மற்றும் 3 தவறானவை.",
    "TNPSC Trap: Lord Pethick-Lawrence was the Chairman of the Cabinet Mission (not Cripps). Cabinet Mission rejected two Constituent Assemblies.",
    "TNPSC பொறி: கேபினட் தூதுக்குழுவின் தலைவர் பெதிக்-லாரன்ஸ் பிரபு (கிரிப்ஸ் அல்ல). தூதுக்குழு இரண்டு அவைகள் அமைப்பதை நிராகரித்தது.",
    "The Cabinet Mission arrived in India in March 1946 and published its plan on May 16, 1946.",
    "கேபினட் தூதுக்குழு மார்ச் 1946 இல் இந்தியா வந்து மே 16, 1946 இல் தன் திட்டத்தை வெளியிட்டது.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "Cabinet Mission Plan 1946"]
))

# MIC_SB_003
questions.append(make_q(
    "MIC_SB_003", "Statement Based",
    "Consider the following statements regarding the composition and election of the Constituent Assembly under the Cabinet Mission Plan:\n1. The total strength of the Constituent Assembly was fixed at 389, out of which 296 seats were allotted to British India and 93 seats to the Princely States.\n2. Seats allotted to each British Province were divided among three principal communities: Muslims, Sikhs, and General, in proportion to their population.\n3. Representatives of each community in the provincial legislative assemblies were elected by direct adult franchise across British India.\nWhich of the statements given above are correct?",
    "கேபினட் தூதுக்குழு திட்டத்தின் கீழ் அரசியலமைப்பு நிர்ணய அவையின் அமைப்பு மற்றும் தேர்தல் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. அரசியலமைப்பு நிர்ணய அவையின் மொத்த உறுப்பினர்கள் எண்ணிக்கை 389 ஆக நிர்ணயிக்கப்பட்டது, அதில் 296 இடங்கள் பிரிட்டிஷ் இந்தியாவிற்கும் 93 இடங்கள் சுதேச சமஸ்தானங்களுக்கும் ஒதுக்கப்பட்டன.\n2. ஒவ்வொரு பிரிட்டிஷ் மாகாணத்திற்கும் ஒதுக்கப்பட்ட இடங்கள் மக்கள் தொகை விகிதாச்சாரப்படி முஸ்லிம்கள், சீக்கியர்கள் மற்றும் பொதுப் பிரிவினர் ஆகிய மூன்று முக்கிய சமூகங்களிடையே பிரிக்கப்பட்டன.\n3. மாகாண சட்டமன்றங்களில் உள்ள ஒவ்வொரு சமூகத்தின் பிரதிநிதிகளும் பிரிட்டிஷ் இந்தியா முழுவதும் நேரடி வயதுவந்தோர் வாக்குரிமை மூலம் தேர்ந்தெடுக்கப்பட்டனர்.\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "A",
    "Statements 1 and 2 are correct. Statement 3 is INCORRECT because the Constituent Assembly was INDIRECTLY elected by the members of the provincial legislative assemblies (who were themselves elected on a limited franchise under the GoI Act 1935), not by direct adult franchise.",
    "கூற்றுகள் 1 மற்றும் 2 சரி. கூற்று 3 தவறு, ஏனெனில் அரசியலமைப்பு நிர்ணய அவை நேரடி வயதுவந்தோர் வாக்குரிமையால் தேர்ந்தெடுக்கப்படவில்லை; மாகாண சட்டமன்ற உறுப்பினர்களால் மறைமுகமாகத் தேர்ந்தெடுக்கப்பட்டது.",
    "Correct. Statements 1 and 2 are true; Statement 3 is false (indirect election).", "சரி. கூற்றுகள் 1 மற்றும் 2 சரி; மறைமுகத் தேர்தல் என்பதால் கூற்று 3 தவறு.",
    "Incorrect. Statement 3 is false.", "தவறு. கூற்று 3 தவறானது.",
    "Incorrect. Statement 3 is false.", "தவறு. கூற்று 3 தவறானது.",
    "Incorrect. Statement 3 is false.", "தவறு. கூற்று 3 தவறானது.",
    "TNPSC Trap: The Constituent Assembly was a PARTLY ELECTED and PARTLY NOMINATED body. British Indian members were indirectly elected; Princely State representatives were nominated.",
    "TNPSC பொறி: அரசியலமைப்பு நிர்ணய அவை பகுதி தேர்ந்தெடுக்கப்பட்ட மற்றும் பகுதி நியமிக்கப்பட்ட அமைப்பாகும். பிரிட்டிஷ் இந்திய உறுப்பினர்கள் மறைமுகமாகத் தேர்ந்தெடுக்கப்பட்டனர்; சமஸ்தான பிரதிநிதிகள் நியமிக்கப்பட்டனர்.",
    "Roughly one seat was allocated for every one million (10 lakh) population.",
    "தோராயமாக பத்து லட்சம் (1 மில்லியன்) மக்கள் தொகைக்கு ஒரு இடம் வீதம் ஒதுக்கப்பட்டது.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "Composition", "Election Method"]
))

# MIC_SB_004
questions.append(make_q(
    "MIC_SB_004", "Statement Based",
    "Consider the following statements regarding the representation of Princely States in the Constituent Assembly:\n1. The 93 seats allotted to Princely States were to be filled by representatives nominated by the rulers of the Princely States.\n2. The representatives of all 93 Princely States joined the Constituent Assembly during its very first meeting on December 9, 1946.\n3. The Princely States gradually joined the Assembly, starting with representatives of six states taking their seats in April 1947.\nWhich of the statements given above is/are correct?",
    "அரசியலமைப்பு நிர்ணய அவையில் சுதேச சமஸ்தானங்களின் பிரதிநிதித்துவம் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. சுதேச சமஸ்தானங்களுக்கு ஒதுக்கப்பட்ட 93 இடங்கள் சமஸ்தான ஆட்சியாளர்களால் நியமிக்கப்பட்ட பிரதிநிதிகள் மூலம் நிரப்பப்பட வேண்டும்.\n2. அனைத்து 93 சுதேச சமஸ்தானங்களின் பிரதிநிதிகளும் டிசம்பர் 9, 1946 அன்று நடந்த முதல் கூட்டத்திலேயே அவையில் இணைந்தனர்.\n3. சுதேச சமஸ்தானங்கள் படிப்படியாக அவையில் இணைந்தன; ஏப்ரல் 1947 இல் ஆறு சமஸ்தானங்களின் பிரதிநிதிகள் முதன்முதலில் தங்கள் இடங்களை எடுத்துக்கொண்டனர்.\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1 only", "1 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "B",
    "Statements 1 and 3 are correct. Statement 2 is INCORRECT because the Princely States initially decided to stay away from the Constituent Assembly and did not attend the first meeting on Dec 9, 1946. They joined gradually; on April 28, 1947, representatives of 6 states (Baroda, Bikaner, Jaipur, Patiala, Rewa, Udaipur) joined.",
    "கூற்றுகள் 1 மற்றும் 3 சரி. கூற்று 2 தவறு, ஏனெனில் ஆரம்பத்தில் சுதேச சமஸ்தானங்கள் அவையிலிருந்து விலகியிருக்க முடிவு செய்து டிசம்பர் 9, 1946 கூட்டத்தில் பங்கேற்கவில்லை. ஏப்ரல் 28, 1947 இல் 6 சமஸ்தான பிரதிநிதிகள் முதன்முதலில் சேர்ந்தனர்.",
    "Incorrect. Statement 3 is also correct.", "தவறு. கூற்று 3 உம் சரியானது.",
    "Correct. Statements 1 and 3 are true; Statement 2 is false (they boycotted first meeting).", "சரி. கூற்றுகள் 1 மற்றும் 3 சரி; முதல் கூட்டத்தை புறக்கணித்ததால் கூற்று 2 தவறு.",
    "Incorrect. Statement 2 is false.", "தவறு. கூற்று 2 தவறானது.",
    "Incorrect. Statement 2 is false.", "தவறு. கூற்று 2 தவறானது.",
    "TNPSC Trap: Princely States stayed away initially. 6 states joined on April 28, 1947. After the Mountbatten Plan of June 3, 1947, most other states took their seats.",
    "TNPSC பொறி: சமஸ்தானங்கள் ஆரம்பத்தில் விலகி இருந்தன. ஏப்ரல் 28, 1947 இல் 6 சமஸ்தானங்கள் சேர்ந்தன. ஜூன் 3, 1947 மவுண்ட்பேட்டன் திட்டத்திற்குப் பின் பெரும்பாலானவை இணைந்தன.",
    "The 6 states that joined first on April 28, 1947 were Baroda, Bikaner, Jaipur, Patiala, Rewa, and Udaipur.",
    "ஏப்ரல் 28, 1947 இல் முதன்முதலில் இணைந்த 6 சமஸ்தானங்கள்: பரோடா, பிகானேர், ஜெய்ப்பூர், பட்டியாலா, ரேவா மற்றும் உதய்பூர்.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "Princely State Representation"]
))

# MIC_SB_005
questions.append(make_q(
    "MIC_SB_005", "Statement Based",
    "With reference to the elections held for the Constituent Assembly in July–August 1946, consider the following statements:\n1. The Indian National Congress won 208 seats out of the 296 seats allotted to British Indian provinces.\n2. The Muslim League won 73 seats, while small groups and independents secured the remaining 15 seats.\n3. Although the Constituent Assembly was not directly elected by the adult population, it included representatives of all sections of Indian society except Mahatma Gandhi and M.A. Jinnah.\nWhich of the statements given above are correct?",
    "ஜூலை-ஆகஸ்ட் 1946 இல் அரசியலமைப்பு நிர்ணய அவைக்கு நடந்த தேர்தல்கள் குறித்து பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. பிரிட்டிஷ் இந்திய மாகாணங்களுக்கு ஒதுக்கப்பட்ட 296 இடங்களில் இந்திய தேசிய காங்கிரஸ் 208 இடங்களை வென்றது.\n2. முஸ்லீம் லீக் 73 இடங்களை வென்றது, சிறிய குழுக்களும் சுயேச்சைகளும் மீதமுள்ள 15 இடங்களைக் கைப்பற்றினர்.\n3. அரசியலமைப்பு நிர்ணய அவை மக்களால் நேரடியாக தேர்ந்தெடுக்கப்படவில்லை என்றாலும், மகாத்மா காந்தி மற்றும் எம்.ஏ. ஜின்னா தவிர இந்திய சமூகத்தின் அனைத்துப் பிரிவுகளின் பிரதிநிதிகளும் இதில் இடம் பெற்றிருந்தனர்.\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "D",
    "All three statements are correct. Congress won 208 seats, Muslim League won 73, independents won 15 out of 296 British India seats. The Assembly included leaders of Hindus, Muslims, Sikhs, Parsis, Anglo-Indians, Indian Christians, SCs, STs, and women. Mahatma Gandhi and M.A. Jinnah were notable exceptions who were NOT members of the Assembly.",
    "மூன்று கூற்றுகளும் சரி. 296 இடங்களில் காங்கிரஸ் 208, முஸ்லிம் லீக் 73, சுயேச்சைகள் 15 இடங்களை வென்றன. காந்தி மற்றும் ஜின்னா தவிர அனைத்து முக்கியத் தலைவர்களும் அவையில் உறுப்பினர்களாக இருந்தனர்.",
    "Incorrect. Statement 3 is also correct.", "தவறு. கூற்று 3 உம் சரியானது.",
    "Incorrect. Statement 1 is also correct.", "தவறு. கூற்று 1 உம் சரியானது.",
    "Incorrect. Statement 2 is also correct.", "தவறு. கூற்று 2 உம் சரியானது.",
    "Correct. All statements 1, 2, and 3 are accurate.", "சரி. கூற்றுகள் 1, 2 மற்றும் 3 அனைத்தும் சரியானவை.",
    "TNPSC Trap: Mahatma Gandhi was NEVER a member of the Constituent Assembly. Neither was M.A. Jinnah.",
    "TNPSC பொறி: மகாத்மா காந்தி அரசியலமைப்பு நிர்ணய அவையின் உறுப்பினராக ஒருபோதும் இருக்கவில்லை. எம்.ஏ. ஜின்னாவும் இருக்கவில்லை.",
    "Out of 296 British India seats, 292 were from 11 governor's provinces and 4 were from chief commissioners' provinces (Delhi, Ajmer-Merwara, Coorg, British Baluchistan).",
    "296 இடங்களில் 292 கவர்னர் மாகாணங்களிலிருந்தும், 4 தலைமை ஆணையர் மாகாணங்களிலிருந்தும் (டெல்லி, அஜ்மீர்-மேர்வாரா, கூர்க், பலுசிஸ்தான்) வந்தன.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "British India Representation", "Important Personalities"]
))

# MIC_SB_006
questions.append(make_q(
    "MIC_SB_006", "Statement Based",
    "Consider the following statements regarding Women's Representation in the Constituent Assembly of India:\n1. A total of 15 women were members of the Constituent Assembly of India.\n2. Begum Aizaz Rasul was the only Muslim woman member in the Constituent Assembly.\n3. Sarojini Naidu, Hansa Mehta, and Rajkumari Amrit Kaur were among the prominent women members of the Assembly.\nWhich of the statements given above are correct?",
    "இந்திய அரசியலமைப்பு நிர்ணய அவையில் பெண்களின் பிரதிநிதித்துவம் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இந்திய அரசியலமைப்பு நிர்ணய அவையில் மொத்தம் 15 பெண் உறுப்பினர்கள் இருந்தனர்.\n2. பேகம் ஐசாஸ் ரசூல் அரசியலமைப்பு நிர்ணய அவையில் இருந்த ஒரே முஸ்லிம் பெண் உறுப்பினர் ஆவார்.\n3. சரோஜினி நாயுடு, ஹன்சா மேத்தா மற்றும் ராஜ்குமாரி அம்ரித் கவுர் ஆகியோர் அவையின் முக்கிய பெண் உறுப்பினர்களில் அடங்குவர்.\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "D",
    "All three statements are correct. There were 15 women members in the Constituent Assembly. Begum Aizaz Rasul was the sole Muslim woman member. Prominent women included Sarojini Naidu, Hansa Mehta, Rajkumari Amrit Kaur, Sucheta Kripalani, Durgabai Deshmukh, Ammu Swaminathan, Renuka Ray, Dakshayani Velayudhan, Malati Choudhury, Leela Ray, Kamla Chaudhry, Purnima Banerjee, Vijayalakshmi Pandit, and Annie Mascarene.",
    "மூன்று கூற்றுகளும் சரி. அவையில் மொத்தம் 15 பெண் உறுப்பினர்கள் இருந்தனர். பேகம் ஐசாஸ் ரசூல் மட்டுமே ஒரே முஸ்லிம் பெண் உறுப்பினர். சரோஜினி நாயுடு, ஹன்சா மேத்தா, ராஜ்குமாரி அம்ரித் கவுர் உள்ளிட்டோர் முக்கியப் பங்கு வகித்தனர்.",
    "Incorrect. Statement 3 is also true.", "தவறு. கூற்று 3 உம் சரி.",
    "Incorrect. Statement 1 is also true.", "தவறு. கூற்று 1 உம் சரி.",
    "Incorrect. Statement 2 is also true.", "தவறு. கூற்று 2 உம் சரி.",
    "Correct. All 3 statements are true.", "சரி. 3 கூற்றுகளும் சரியானவை.",
    "TNPSC Trap: Begum Aizaz Rasul opposed separate electorates for minorities in the Constituent Assembly.",
    "TNPSC பொறி: பேகம் ஐசாஸ் ரசூல் அவையில் சிறுபான்மையினருக்கான தனித் தொகுதிகளை எதிர்த்தார்.",
    "Hansa Mehta served on the Advisory Committee and Fundamental Rights Sub-Committee.",
    "ஹன்சா மேத்தா ஆலோசனைக் குழு மற்றும் அடிப்படை உரிமைகள் துணைக் குழுவில் பணியாற்றினார்.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "Women's Representation"]
))

# MIC_SB_007
questions.append(make_q(
    "MIC_SB_007", "Statement Based",
    "With reference to the first meeting of the Constituent Assembly on December 9, 1946, consider the following statements:\n1. The first meeting was attended by all 389 members of the Constituent Assembly.\n2. Dr. Sachchidananda Sinha was elected as the temporary President of the Assembly, following the French practice of selecting the oldest member.\n3. The Muslim League boycotted the first meeting and insisted on a separate Constituent Assembly for Pakistan.\nWhich of the statements given above is/are correct?",
    "டிசம்பர் 9, 1946 அன்று நடந்த அரசியலமைப்பு நிர்ணய அவையின் முதல் கூட்டம் குறித்து பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. முதல் கூட்டத்தில் அரசியலமைப்பு நிர்ணய அவையின் அனைத்து 389 உறுப்பினர்களும் கலந்துகொண்டனர்.\n2. மூத்த உறுப்பினரைத் தேர்ந்தெடுக்கும் ஃபிரெஞ்சுக் வழக்கத்தைப் பின்பற்றி, டாக்டர் சச்சிதானந்த சின்ஹா அவையின் தற்காலிகத் தலைவராகத் தேர்ந்தெடுக்கப்பட்டார்.\n3. முஸ்லீம் லீக் முதல் கூட்டத்தைப் புறக்கணித்து பாகிஸ்தானுக்குத் தனி அரசியலமைப்பு நிர்ணய அவையைக் கோரியது.\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "2 only", "2 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "B",
    "Statements 2 and 3 are correct. Statement 1 is INCORRECT because only 211 members attended the first meeting on Dec 9, 1946. The Muslim League boycotted it and princely states stayed away.",
    "கூற்றுகள் 2 மற்றும் 3 சரி. கூற்று 1 தவறு, ஏனெனில் டிசம்பர் 9, 1946 முதல் கூட்டத்தில் 211 உறுப்பினர்கள் மட்டுமே கலந்து கொண்டனர் (389 உறுப்பினர்களும் அல்ல).",
    "Incorrect. Statement 3 is also correct.", "தவறு. கூற்று 3 உம் சரியானது.",
    "Correct. Statements 2 and 3 are true; Statement 1 is false (only 211 members attended).", "சரி. கூற்றுகள் 2 மற்றும் 3 சரி; 211 உறுப்பினர்கள் மட்டுமே பங்கேற்றதால் கூற்று 1 தவறு.",
    "Incorrect. Statement 1 is false.", "தவறு. கூற்று 1 தவறானது.",
    "Incorrect. Statement 1 is false.", "தவறு. கூற்று 1 தவறானது.",
    "TNPSC Trap: Only 211 members attended the 1st meeting on Dec 9, 1946. Winston Churchill commented that the Assembly meeting looked like 'a marriage without the bride'.",
    "TNPSC பொறி: முதல் கூட்டத்தில் 211 பேர் மட்டுமே பங்கேற்றனர். சர்ச்சில் இக்கூட்டத்தை 'மணப்பெண் இல்லாத திருமணம்' என விமர்சித்தார்.",
    "Dr. Sachchidananda Sinha was recommended as temporary President by J.B. Kripalani.",
    "ஜெ.பி. கிருபளானியால் டாக்டர் சச்சிதானந்த சின்ஹா தற்காலிகத் தலைவராக முன்மொழியப்பட்டார்.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "Temporary President", "Constituent Assembly Formation"]
))

# MIC_SB_008
questions.append(make_q(
    "MIC_SB_008", "Statement Based",
    "Consider the following statements regarding the officers of the Constituent Assembly elected on December 11, 1946:\n1. Dr. Rajendra Prasad was elected as the permanent President of the Constituent Assembly.\n2. H.C. Mookherjee was elected as the sole Vice-President of the Constituent Assembly throughout its existence.\n3. Sir B.N. Rau was appointed as the Constitutional Adviser (Legal Advisor) to the Assembly.\nWhich of the statements given above is/are correct?",
    "டிசம்பர் 11, 1946 இல் தேர்ந்தெடுக்கப்பட்ட அரசியலமைப்பு நிர்ணய அவையின் நிர்வாகிகள் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. டாக்டர் ராஜேந்திர பிரசாத் அரசியலமைப்பு நிர்ணய அவையின் நிரந்தரத் தலைவராகத் தேர்ந்தெடுக்கப்பட்டார்.\n2. எச்.சி. முகர்ஜி மட்டுமே அவையின் ஒரே துணைத் தலைவராக அதன் காலம் முழுவதும் செயல்பட்டார்.\n3. சர் பி.என். ராவ் அவையின் அரசியலமைப்பு ஆலோசகராக (சட்ட ஆலோசகர்) நியமிக்கப்பட்டார்.\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "A",
    "Statements 1 and 3 are correct. Statement 2 is INCORRECT because the Constituent Assembly had TWO Vice-Presidents: H.C. Mookherjee AND V.T. Krishnamachari.",
    "கூற்றுகள் 1 மற்றும் 3 சரி. கூற்று 2 தவறு, ஏனெனில் அரசியலமைப்பு நிர்ணய அவைக்கு இரண்டு துணைத் தலைவர்கள் இருந்தனர்: எச்.சி. முகர்ஜி மற்றும் வி.டி. கிருஷ்ணமாச்சாரி.",
    "Correct. Statements 1 and 3 are true; Statement 2 is false (there were TWO Vice-Presidents).", "சரி. கூற்றுகள் 1 மற்றும் 3 சரி; இரண்டு துணைத் தலைவர்கள் இருந்ததால் கூற்று 2 தவறு.",
    "Incorrect. Statement 2 is false.", "தவறு. கூற்று 2 தவறானது.",
    "Incorrect. Statement 2 is false.", "தவறு. கூற்று 2 தவறானது.",
    "Incorrect. Statement 2 is false.", "தவறு. கூற்று 2 தவறானது.",
    "TNPSC Trap: Constituent Assembly had TWO Vice-Presidents: H.C. Mookherjee (representing Christian minority/provinces) and V.T. Krishnamachari (representing princely states).",
    "TNPSC பொறி: அரசியலமைப்பு நிர்ணய அவைக்கு இரண்டு துணைத் தலைவர்கள் இருந்தனர்: எச்.சி. முகர்ஜி மற்றும் வி.டி. கிருஷ்ணமாச்சாரி.",
    "Sir B.N. Rau was a distinguished jurist who prepared the initial draft of the Indian Constitution.",
    "சர் பி.என். ராவ் இந்திய அரசியலமைப்பின் ஆரம்ப வரைவைத் தயாரித்த ஒரு சிறந்த சட்ட வல்லுநர் ஆவார்.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "Permanent President", "B. N. Rau"]
))

# MIC_SB_009
questions.append(make_q(
    "MIC_SB_009", "Statement Based",
    "With reference to the Objectives Resolution moved in the Constituent Assembly, consider the following statements:\n1. It was moved by Pandit Jawaharlal Nehru on December 13, 1946.\n2. It laid down the fundamentals and philosophy of the constitutional structure and was adopted by the Assembly on the very day it was introduced.\n3. The modified version of the Objectives Resolution forms the Preamble of the present Constitution.\nWhich of the statements given above is/are correct?",
    "அரசியலமைப்பு நிர்ணய அவையில் முன்மொழியப்பட்ட குறிக்கோள்கள் தீர்மானம் குறித்து பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது பண்டித ஜவகர்லால் நேருவால் டிசம்பர் 13, 1946 அன்று முன்மொழியப்பட்டது.\n2. இது அரசியலமைப்பு அமைப்பின் அடிப்படைகள் மற்றும் தத்துவத்தை வகுத்தது, மேலும் இது அறிமுகப்படுத்தப்பட்ட நாளிலேயே அவையால் ஏற்றுக்கொள்ளப்பட்டது.\n3. குறிக்கோள்கள் தீர்மானத்தின் திருத்தப்பட்ட வடிவமே தற்போதைய அரசியலமைப்பின் முகப்புரையாக உள்ளது.\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "A",
    "Statements 1 and 3 are correct. Statement 2 is INCORRECT because the Objectives Resolution was NOT adopted on the day of introduction (Dec 13, 1946). Its adoption was postponed to allow Muslim League and Princely State representatives to join, and it was unanimously adopted on January 22, 1947.",
    "கூற்றுகள் 1 மற்றும் 3 சரி. கூற்று 2 தவறு, ஏனெனில் குறிக்கோள்கள் தீர்மானம் அறிமுகப்படுத்தப்பட்ட நாளிலேயே ஏற்றுக்கொள்ளப்படவில்லை; ஜனவரி 22, 1947 அன்றே ஒருமனதாக ஏற்றுக்கொள்ளப்பட்டது.",
    "Correct. Statements 1 and 3 are true; Statement 2 is false (adopted Jan 22, 1947).", "சரி. கூற்றுகள் 1 மற்றும் 3 சரி; ஜனவரி 22, 1947 இல் ஏற்கப்பட்டதால் கூற்று 2 தவறு.",
    "Incorrect. Statement 2 is false.", "தவறு. கூற்று 2 தவறானது.",
    "Incorrect. Statement 2 is false.", "தவறு. கூற்று 2 தவறானது.",
    "Incorrect. Statement 2 is false.", "தவறு. கூற்று 2 தவறானது.",
    "TNPSC Trap: Objectives Resolution introduced: Dec 13, 1946. Adopted: Jan 22, 1947 (NOT same day).",
    "TNPSC பொறி: குறிக்கோள்கள் தீர்மானம் அறிமுகம்: டிசம்பர் 13, 1946. ஏற்றுக்கொள்ளப்பட்டது: ஜனவரி 22, 1947 (ஒரே நாளில் அல்ல).",
    "M.R. Jayakar opposed immediate passage on Dec 13, 1946, urging the Assembly to wait for Muslim League and Princely States.",
    "எம்.ஆர். ஜெயக்கர் டிசம்பர் 13 அன்றே உடனடியாக நிறைவேற்றுவதை எதிர்த்து லீக் மற்றும் சமஸ்தானங்களுக்காக காத்திருக்கக் கோரினார்.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "Objectives Resolution"]
))

# MIC_SB_010
questions.append(make_q(
    "MIC_SB_010", "Statement Based",
    "Consider the following statements regarding the Major Committees of the Constituent Assembly and their Chairmen:\n1. Jawaharlal Nehru chaired the Union Powers Committee, Union Constitution Committee, and States Committee.\n2. Sardar Vallabhbhai Patel chaired the Provincial Constitution Committee and the Advisory Committee on Fundamental Rights, Minorities and Tribal and Excluded Areas.\n3. Dr. B.R. Ambedkar chaired both the Drafting Committee and the Steering Committee.\nWhich of the statements given above are correct?",
    "அரசியலமைப்பு நிர்ணய அவையின் முக்கியக் குழுக்கள் மற்றும் அவற்றின் தலைவர்கள் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. ஜவகர்லால் நேரு மத்திய அதிகாரக் குழு, மத்திய அரசியலமைப்புக்குழு மற்றும் மாநிலங்கள் குழு ஆகியவற்றிற்குத் தலைமை தாங்கினார்.\n2. சர்தார் வல்லபாய் படேல் மாகாண அரசியலமைப்புக்குழு மற்றும் அடிப்படை உரிமைகள், சிறுபான்மையினர் மற்றும் பழங்குடியினர் ஆலோசகக் குழுவிற்குத் தலைமை தாங்கினார்.\n3. டாக்டர் பி.ஆர். அம்பேத்கர் வரைவுக் குழு மற்றும் வழிநடத்தல் குழு ஆகிய இரண்டிற்கும் தலைமை தாங்கினார்.\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "A",
    "Statements 1 and 2 are correct. Statement 3 is INCORRECT because Dr. Rajendra Prasad chaired the Steering Committee (and Rules of Procedure Committee), NOT Dr. B.R. Ambedkar. Dr. Ambedkar chaired the Drafting Committee.",
    "கூற்றுகள் 1 மற்றும் 2 சரி. கூற்று 3 தவறு, ஏனெனில் வழிகாட்டுதல் குழுவிற்கு (Steering Committee) டாக்டர் ராஜேந்திர பிரசாத் தலைமை தாங்கினார் (அம்பேத்கர் அல்ல).",
    "Correct. Statements 1 and 2 are true; Statement 3 is false (Rajendra Prasad chaired Steering Committee).", "சரி. கூற்றுகள் 1 மற்றும் 2 சரி; ராஜேந்திர பிரசாத் வழிகாட்டுதல் குழுத் தலைவர் என்பதால் கூற்று 3 தவறு.",
    "Incorrect. Statement 3 is false.", "தவறு. கூற்று 3 தவறானது.",
    "Incorrect. Statement 3 is false.", "தவறு. கூற்று 3 தவறானது.",
    "Incorrect. Statement 3 is false.", "தவறு. கூற்று 3 தவறானது.",
    "TNPSC Trap: Steering Committee Chair = Dr. Rajendra Prasad. Drafting Committee Chair = Dr. B.R. Ambedkar.",
    "TNPSC பொறி: வழிநடத்தல் குழுத் தலைவர் = டாக்டர் ராஜேந்திர பிரசாத். வரைவுக் குழுத் தலைவர் = டாக்டர் பி.ஆர். அம்பேத்கர்.",
    "States Committee (Committee for Negotiating with States) was chaired by Jawaharlal Nehru.",
    "மாநிலங்கள் குழு (மாநில பேச்சுவார்த்தைக் குழு) ஜவகர்லால் நேரு தலைமையிலானது.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "Committees of Constituent Assembly", "Steering Committee"]
))

print("Q1-10 loaded.")
