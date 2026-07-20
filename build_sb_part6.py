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

# HB_SB_036
questions.append(make_q(
    "HB_SB_036", "Statement Based",
    "Consider the following statements regarding the Government of India Act of 1919:\n1. It introduced Dyarchy in the provinces by dividing provincial subjects into Reserved and Transferred.\n2. It introduced Bicameralism at the Centre consisting of Council of State and Central Legislative Assembly.\n3. It provided for the establishment of a Public Service Commission, which was set up in 1926.\n4. It mandated that all 6 members of the Viceroy's Executive Council must be Indian nationals.\nWhich of the statements given above are correct?",
    "1919 ஆம் ஆண்டின் இந்திய அரசுச் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது மாகாணத் துறைகளை ஒதுக்கப்பட்டவை மற்றும் மாற்றப்பட்டவை எனப் பிரித்து மாகாணங்களில் இரட்டை ஆட்சியை அறிமுகப்படுத்தியது.\n2. இது மத்தியில் மாநிலங்களவை மற்றும் மத்திய சட்டமன்றப் பேரவை கொண்ட ஈரவை முறையை அறிமுகப்படுத்தியது.\n3. இது 1926 இல் அமைக்கப்பட்ட பொதுச் சேவை ஆணையத்தை நிறுவ வழிவகை செய்தது.\n4. வைஸ்ராய் நிர்வாகக் குழுவின் 6 உறுப்பினர்களும் இந்திய குடிமக்களாக இருக்க வேண்டும் என்று இது கட்டாயப்படுத்தியது.\nஎது சரி?",
    "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டும்",
    "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டும்",
    "1, 3 and 4 only", "1, 3 மற்றும் 4 மட்டும்",
    "1, 2, 3 and 4", "1, 2, 3 மற்றும் 4",
    "A",
    "Statements 1, 2, and 3 are correct. Statement 4 is INCORRECT because the 1919 Act required 3 out of 6 members (other than Commander-in-Chief) to be Indian, NOT all members.",
    "கூற்றுகள் 1, 2, 3 சரி. கூற்று 4 தவறு, ஏனெனில் 6 இல் 3 உறுப்பினர்கள் மட்டுமே இந்தியர்களாக இருக்க வேண்டும், அனைவரும் அல்ல.",
    "Correct. Statements 1, 2, and 3 are correct; Statement 4 is false.",
    "சரி. கூற்றுகள் 1, 2, 3 சரி; கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "TNPSC Trap: Under 1919 Act, 3 out of 6 members of GG Executive Council (other than Commander-in-Chief) had to be Indian.",
    "TNPSC பொறி: 1919 சட்டப்படி GG நிர்வாகக் குழுவின் 6 உறுப்பினர்களில் 3 பேர் இந்தியர்களாக இருக்க வேண்டும்.",
    "1919 Act separated Provincial Budgets from the Central Budget for the first time.",
    "1919 சட்டம் முதன்முறையாக மாகாண வரவு செலவுத் திட்டத்தை மத்திய வரவு செலவுத் திட்டத்திலிருந்து பிரித்தது.",
    "Analyze", 75, ["Polity", "Historical Background", "Government of India Act 1919", "Four Statement"]
))

# HB_SB_037
questions.append(make_q(
    "HB_SB_037", "Statement Based",
    "Consider the following statements regarding the Government of India Act of 1935:\n1. It provided for an All-India Federation consisting of Provinces and Princely States.\n2. It abolished Provincial Dyarchy and introduced Provincial Autonomy.\n3. It divided powers into Federal (59), Provincial (54), and Concurrent (36) lists.\n4. Residuary legislative powers were vested in the Federal Court.\nWhich of the statements given above are correct?",
    "1935 ஆம் ஆண்டின் இந்திய அரசுச் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது மாகாணங்கள் மற்றும் சுதேச சமஸ்தானங்களைக் கொண்ட அகில இந்திய கூட்டாட்சிக்கு வழிவகை செய்தது.\n2. இது மாகாண இரட்டை ஆட்சியை ஒழித்து மாகாண தன்னாட்சியை அறிமுகப்படுத்தியது.\n3. இது அதிகாரங்களை கூட்டாட்சி (59), மாகாண (54), மற்றும் இணைப்பு (36) பட்டியல்களாகப் பிரித்தது.\n4. எஞ்சிய சட்ட அதிகாரங்கள் கூட்டாட்சி நீதிமன்றத்திடம் ஒப்படைக்கப்பட்டன.\nஎது சரி?",
    "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டும்",
    "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டும்",
    "1, 3 and 4 only", "1, 3 மற்றும் 4 மட்டும்",
    "1, 2, 3 and 4", "1, 2, 3 மற்றும் 4",
    "A",
    "Statements 1, 2, and 3 are correct. Statement 4 is INCORRECT because Residuary legislative powers were given to the Governor-General (Viceroy), NOT to the Federal Court.",
    "கூற்றுகள் 1, 2, 3 சரி. கூற்று 4 தவறு, ஏனெனில் எஞ்சிய அதிகாரங்கள் கவர்னர் ஜெனரலிடம் (வைஸ்ராய்) ஒப்படைக்கப்பட்டன, நீதிமன்றத்திடம் அல்ல.",
    "Correct. Statements 1, 2, and 3 are correct; Statement 4 is false.",
    "சரி. கூற்றுகள் 1, 2, 3 சரி; கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "TNPSC Trap: In 1935 Act, Residuary powers belonged to Viceroy (GG). In 1950 Constitution, Residuary powers belong to Parliament (Article 248).",
    "TNPSC பொறி: 1935 சட்டத்தில் எஞ்சிய அதிகாரம் வைஸ்ராயிடம் இருந்தது. 1950 அரசியலமைப்பில் பாராளுமன்றத்திடம் உள்ளது (பிரிவு 248).",
    "1935 Act established Federal Court in 1937 and Reserve Bank of India in 1935.",
    "1935 சட்டம் 1937 இல் கூட்டாட்சி நீதிமன்றத்தையும் 1935 இல் ரிசர்வ் வங்கியையும் அமைத்தது.",
    "Analyze", 75, ["Polity", "Historical Background", "Government of India Act 1935", "Four Statement"]
))

# HB_SB_038
questions.append(make_q(
    "HB_SB_038", "Statement Based",
    "Consider the following statements regarding the Indian Independence Act of 1947:\n1. It declared India as an independent sovereign state from August 15, 1947.\n2. Section 6 empowered Constituent Assemblies to alter or repeal any British Parliamentary Act.\n3. It proclaimed the lapse of British paramountcy over Indian Princely States.\n4. It retained the office of Secretary of State for India with expanded veto powers.\nWhich of the statements given above are correct?",
    "1947 ஆம் ஆண்டின் இந்திய சுதந்திரச் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது ஆகஸ்ட் 15, 1947 முதல் இந்தியாவை ஒரு சுதந்திர இறையாண்மை நாடாக அறிவித்தது.\n2. பிரிவு 6 பிரிட்டிஷ் பாராளுமன்ற சட்டங்களை மாற்ற அல்லது ரத்து செய்ய அரசியலமைப்பு சபைகளுக்கு அதிகாரமளித்தது.\n3. இது சுதேச சமஸ்தானங்கள் மீதான பிரிட்டிஷ் மேலாதிக்கம் முடிவுக்கு வந்ததாக அறிவித்தது.\n4. இது விரிவாக்கப்பட்ட நிராகரிப்பு அதிகாரங்களுடன் இந்திய அரசுச் செயலாளர் பதவியைத் தக்கவைத்தது.\nஎது சரி?",
    "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டும்",
    "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டும்",
    "1, 3 and 4 only", "1, 3 மற்றும் 4 மட்டும்",
    "1, 2, 3 and 4", "1, 2, 3 மற்றும் 4",
    "A",
    "Statements 1, 2, and 3 are correct. Statement 4 is INCORRECT because the 1947 Act ABOLISHED the office of Secretary of State for India.",
    "கூற்றுகள் 1, 2, 3 சரி. கூற்று 4 தவறு, ஏனெனில் 1947 சுதந்திரச் சட்டம் இந்திய அரசுச் செயலாளர் பதவியை ஒழித்தது.",
    "Correct. Statements 1, 2, and 3 are correct; Statement 4 is false.",
    "சரி. கூற்றுகள் 1, 2, 3 சரி; கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "1947 Act abolished Viceroy office and appointed Governor-General as constitutional nominal head.",
    "1947 சட்டம் வைஸ்ராய் பதவியை ஒழித்து கவர்னர் ஜெனரலை பெயரளவு தலைவராக்கியது.",
    "Lord Mountbatten was the first Governor-General of independent India, and C. Rajagopalachari was the first and last Indian Governor-General.",
    "மவுண்ட்பேட்டன் பிரபு முதல் கவர்னர் ஜெனரலாகவும், ராஜாஜி முதல் மற்றும் கடைசி இந்திய கவர்னர் ஜெனரலாகவும் இருந்தனர்.",
    "Analyze", 75, ["Polity", "Historical Background", "Indian Independence Act 1947", "Four Statement"]
))

# HB_SB_039
questions.append(make_q(
    "HB_SB_039", "Statement Based",
    "Consider the following statements regarding the Constituent Assembly of India:\n1. It was formed in November 1946 under the Cabinet Mission Plan.\n2. The total strength of the Assembly was 389 members prior to partition.\n3. The first meeting of the Constituent Assembly was held on December 9, 1946.\n4. All 389 members were directly elected by universal adult franchise.\nWhich of the statements given above are correct?",
    "இந்திய அரசியலமைப்பு சபை பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது கேபினட் மிஷன் திட்டத்தின் கீழ் நவம்பர் 1946 இல் உருவாக்கப்பட்டது.\n2. பிரிவினைக்கு முன் சபையின் மொத்த உறுப்பினர்களின் எண்ணிக்கை 389 ஆகும்.\n3. அரசியலமைப்பு சபையின் முதல் கூட்டம் டிசம்பர் 9, 1946 அன்று நடைபெற்றது.\n4. 389 உறுப்பினர்களும் உலகளாவிய வயதுவந்தோர் வாக்குரிமை மூலம் நேரடியாகத் தேர்ந்தெடுக்கப்பட்டனர்.\nஎது சரி?",
    "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டும்",
    "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டும்",
    "1, 3 and 4 only", "1, 3 மற்றும் 4 மட்டும்",
    "1, 2, 3 and 4", "1, 2, 3 மற்றும் 4",
    "A",
    "Statements 1, 2, and 3 are correct. Statement 4 is INCORRECT because Assembly members were NOT directly elected by adult franchise (British Indian seats were indirectly elected by provincial assemblies, and Princely State seats were nominated).",
    "கூற்றுகள் 1, 2, 3 சரி. கூற்று 4 தவறு, ஏனெனில் உறுப்பினர்கள் நேரடி வாக்குரிமையால் தேர்ந்தெடுக்கப்படவில்லை (மறைமுகத் தேர்தல் & நியமனம்).",
    "Correct. Statements 1, 2, and 3 are correct; Statement 4 is false.",
    "சரி. கூற்றுகள் 1, 2, 3 சரி; கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "Dr. Sachchidananda Sinha was elected as temporary President of the Assembly in its first meeting on Dec 9, 1946.",
    "1946 டிசம்பர் 9 முதல் கூட்டத்தில் டாக்டர் சச்சிதானந்த சின்ஹா இடைக்காலத் தலைவராகத் தேர்ந்தெடுக்கப்பட்டார்.",
    "Dr. Rajendra Prasad was elected permanent President of the Assembly on December 11, 1946.",
    "1946 டிசம்பர் 11 அன்று டாக்டர் ராஜேந்திர பிரசாத் நிரந்தரத் தலைவராகத் தேர்ந்தெடுக்கப்பட்டார்.",
    "Analyze", 75, ["Polity", "Historical Background", "Constituent Assembly Formation", "Four Statement"]
))

# HB_SB_040
questions.append(make_q(
    "HB_SB_040", "Statement Based",
    "Consider the following statements regarding the progression of Indian representation in executive administration:\n1. The Indian Councils Act 1861 initiated Indian association with law-making by nominating 3 non-official Indians.\n2. The Indian Councils Act 1909 appointed Satyendra Prasad Sinha as the first Indian Law Member in Viceroy's Executive Council.\n3. The Government of India Act 1919 mandated that 3 out of 6 members of the Viceroy's Executive Council be Indian.\n4. An All-Indian Interim Government was formed in September 1946 headed by Jawaharlal Nehru.\nWhich of the statements given above are correct?",
    "நிர்வாகத்தில் இந்தியப் பிரதிநிதித்துவ வளர்ச்சி பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 1861 கவுன்சில்கள் சட்டம் 3 அரசுசாரா இந்தியர்களை நியமித்து சட்டமியற்றலில் இந்தியர்களை இணைக்கத் தொடங்கியது.\n2. 1909 கவுன்சில்கள் சட்டம் சத்யேந்திர பிரசாத் சின்ஹாவை வைஸ்ராய் நிர்வாகக் குழுவின் முதல் இந்திய சட்ட உறுப்பினராக நியமித்தது.\n3. 1919 அரசுச் சட்டம் வைஸ்ராய் நிர்வாகக் குழுவின் 6 உறுப்பினர்களில் 3 பேர் இந்தியர்களாக இருக்க வேண்டும் எனப் பணித்தது.\n4. ஜவஹர்லால் நேரு தலைமையில் செப்டம்பர் 1946 இல் அனைத்து இந்தியர்கள் கொண்ட இடைக்கால அரசு அமைக்கப்பட்டது.\nஎது சரி?",
    "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டும்",
    "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டும்",
    "1, 3 and 4 only", "1, 3 மற்றும் 4 மட்டும்",
    "1, 2, 3 and 4", "1, 2, 3 மற்றும் 4",
    "D",
    "All four statements are correct. Traces executive Indianization: 1861 nomination -> 1909 S.P. Sinha -> 1919 3 of 6 members -> Sept 1946 All-Indian Interim Cabinet.",
    "நான்கு கூற்றுகளும் சரியானவை. 1861 நியமனம் -> 1909 எஸ்.பி. சின்ஹா -> 1919 6 இல் 3 பேர் -> செப் 1946 இடைக்கால அமைச்சரவை.",
    "Incorrect. Statement 4 is also correct.",
    "தவறு. கூற்று 4-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Correct. All four statements are historically true.",
    "சரி. நான்கு கூற்றுகளும் வரலாற்று ரீதியாகச் சரியானவை.",
    "In the 1946 Interim Government, Jawaharlal Nehru served as Vice-President of Executive Council & Minister of External Affairs.",
    "1946 இடைக்கால அரசில் ஜவஹர்லால் நேரு நிர்வாகக் குழுவின் துணைத் தலைவராகவும் வெளியுறவுத்துறை அமைச்சராகவும் இருந்தார்.",
    "Satyendra Prasad Sinha was later raised to the peerage as Lord Sinha of Raipur.",
    "சத்யேந்திர பிரசாத் சின்ஹா பின்னர் ராய்பூரின் லார்ட் சின்ஹா எனப் பிரபுக்கள் அவைக்கு உயர்த்தப்பட்டார்.",
    "Analyze", 75, ["Polity", "Historical Background", "Executive Indianization Arc", "Four Statement"]
))

# Save checkpoint
questions.sort(key=lambda x: x["id"])
with open(target_path, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"Part 6 complete: {len(questions)} questions saved.")
