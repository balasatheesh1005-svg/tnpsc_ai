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
# PART 3: 10 FOUR STATEMENT QUESTIONS (HB_SB_031 to HB_SB_040)
# =========================================================

# HB_SB_031
questions.append(make_q(
    "HB_SB_031", "Statement Based",
    "Consider the following statements regarding Company Rule under the Regulating Act 1773 and Pitt's India Act 1784:\n1. The Regulating Act 1773 created an Executive Council of four members to assist the Governor-General of Bengal.\n2. The Regulating Act 1773 provided for the establishment of a Supreme Court of Judicature at Calcutta in 1774.\n3. Pitt's India Act 1784 established a Board of Control of six members to manage political affairs.\n4. Pitt's India Act 1784 increased the Governor-General's Council membership from four to five.\nWhich of the statements given above are correct?",
    "1773 ஒழுங்குமுறைச் சட்டம் மற்றும் 1784 பிட் இந்தியச் சட்டத்தின் கீழ் கம்பெனி ஆட்சி பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 1773 ஒழுங்குமுறைச் சட்டம் வங்காள கவர்னர் ஜெனரலுக்கு உதவ நான்கு உறுப்பினர்களைக் கொண்ட நிர்வாகக் குழுவை உருவாக்கியது.\n2. 1773 ஒழுங்குமுறைச் சட்டம் 1774 இல் கொல்கத்தாவில் ஒரு உச்ச நீதிமன்றத்தை நிறுவ வழிவகை செய்தது.\n3. 1784 பிட் இந்தியச் சட்டம் அரசியல் விவகாரங்களை நிர்வகிக்க ஆறு உறுப்பினர்களைக் கொண்ட கட்டுப்பாட்டு வாரியத்தை நிறுவியது.\n4. 1784 பிட் இந்தியச் சட்டம் கவர்னர் ஜெனரல் கவுன்சில் உறுப்பினர்களின் எண்ணிக்கையை நான்கிலிருந்து ஐந்தாக உயர்த்தியது.\nஎது சரி?",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டும்",
    "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டும்",
    "1, 2, 3 and 4", "1, 2, 3 மற்றும் 4",
    "B",
    "Statements 1, 2, and 3 are correct. Statement 4 is INCORRECT because Pitt's India Act 1784 REDUCED the Governor-General's Council membership from 4 to 3 (not increased to 5).",
    "கூற்றுகள் 1, 2, 3 சரி. கூற்று 4 தவறு, ஏனெனில் 1784 பிட் சட்டம் GG கவுன்சில் உறுப்பினர்களை 4 லிருந்து 3 ஆகக் குறைத்தது (5 ஆக உயர்த்தவில்லை).",
    "Incorrect. Statement 3 is also correct.",
    "தவறு. கூற்று 3-ம் சரியானது.",
    "Correct. Statements 1, 2, and 3 are correct; Statement 4 is false.",
    "சரி. கூற்றுகள் 1, 2, 3 சரி; கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "TNPSC Trap: Pitt's India Act 1784 reduced GG Council size from 4 to 3 to give GG an effective casting vote with just one supporter.",
    "TNPSC பொறி: 1784 பிட் சட்டம் GG கவுன்சில் எண்ணிக்கையை 4 லிருந்து 3 ஆகக் குறைத்தது.",
    "Pitt's India Act 1784 gave the Board of Control full authority over civil, military, and revenue operations.",
    "1784 பிட் சட்டம் கட்டுப்பாட்டு வாரியத்திற்கு சிவில், இராணுவ, வருவாய் நடவடிக்கைகள் மீது முழு அதிகாரம் அளித்தது.",
    "Analyze", 75, ["Polity", "Historical Background", "1773 and 1784 Acts", "Four Statement"]
))

# HB_SB_032
questions.append(make_q(
    "HB_SB_032", "Statement Based",
    "Consider the following statements regarding Charter Acts of 1813 and 1833:\n1. Charter Act 1813 abolished East India Company's trade monopoly in India except for tea and China trade.\n2. Charter Act 1813 allocated Rs 1 Lakh per year for the promotion of education in India.\n3. Charter Act 1833 ended ALL commercial trading activities of the Company, making it a purely administrative body.\n4. Charter Act 1833 redesignated the Governor-General of Bengal as the Governor-General of India.\nWhich of the statements given above are correct?",
    "1813 மற்றும் 1833 சாசனச் சட்டங்கள் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 1813 சாசனச் சட்டம் தேயிலை மற்றும் சீனா வர்த்தகம் தவிர கம்பெனியின் வர்த்தக ஏகபோகத்தை ஒழித்தது.\n2. 1813 சாசனச் சட்டம் இந்தியாவில் கல்வி வளர்ச்சிக்கு ஆண்டுக்கு ரூ. 1 லட்சம் ஒதுக்கியது.\n3. 1833 சாசனச் சட்டம் கம்பெனியின் அனைத்து வர்த்தக நடவடிக்கைகளையும் முடித்து அதைத் தூய நிர்வாக அமைப்பாக்கியது.\n4. 1833 சாசனச் சட்டம் வங்காள கவர்னர் ஜெனரலை இந்திய கவர்னர் ஜெனரலாக மாற்றியது.\nஎது சரி?",
    "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டும்",
    "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டும்",
    "1, 3 and 4 only", "1, 3 மற்றும் 4 மட்டும்",
    "1, 2, 3 and 4", "1, 2, 3 மற்றும் 4",
    "D",
    "All four statements are correct. 1813 Act ended monopoly except tea/China and allocated Rs 1 Lakh education fund; 1833 Act ended all commercial trade and created Governor-General of India.",
    "நான்கு கூற்றுகளும் சரியானவை. 1813 இல் தேயிலை/சீனா தவிர ஏகபோக ஒழிப்பு & கல்வி நிதி; 1833 இல் அனைத்து வர்த்தக ஒழிப்பு & இந்திய கவர்னர் ஜெனரல் உருவாக்கம்.",
    "Incorrect. Statement 4 is also correct.",
    "தவறு. கூற்று 4-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Correct. All four statements are historically accurate.",
    "சரி. நான்கு கூற்றுகளும் வரலாற்று ரீதியாகச் சரியானவை.",
    "Lord William Bentinck became the first Governor-General of India under Charter Act 1833.",
    "1833 சாசனச் சட்டத்தின் கீழ் வில்லியம் பென்டிங்க் பிரபு இந்தியாவின் முதல் கவர்னர் ஜெனரலானார்.",
    "Charter Act 1833 introduced Lord Macaulay as the Law Member in Governor-General's Council.",
    "1833 சாசனச் சட்டம் மெக்காலே பிரபுவை சட்ட உறுப்பினராகச் சேர்த்தது.",
    "Analyze", 75, ["Polity", "Historical Background", "Charter Acts 1813 and 1833", "Four Statement"]
))

# HB_SB_033
questions.append(make_q(
    "HB_SB_033", "Statement Based",
    "Consider the following statements regarding Charter Act 1853 and Government of India Act 1858:\n1. Charter Act 1853 separated legislative and executive functions of the Governor-General's Council.\n2. Charter Act 1853 introduced an open competitive examination system for Indian Civil Services.\n3. GOI Act 1858 abolished the Board of Control and Court of Directors, ending Double Government.\n4. GOI Act 1858 created the office of Secretary of State for India assisted by a 15-member Council of India.\nWhich of the statements given above are correct?",
    "1853 சாசனச் சட்டம் மற்றும் 1858 இந்திய அரசுச் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 1853 சாசனச் சட்டம் கவர்னர் ஜெனரல் கவுன்சிலின் சட்டமன்ற மற்றும் நிர்வாகப் பணிகளைப் பிரித்தது.\n2. 1853 சாசனச் சட்டம் இந்திய குடிமைப் பணிகளுக்கான திறந்தவெளிப் போட்டித் தேர்வு முறையை அறிமுகப்படுத்தியது.\n3. 1858 அரசுச் சட்டம் கட்டுப்பாட்டு வாரியம் மற்றும் இயக்குநர்கள் அவையைக் கலைத்து இரட்டை ஆட்சியை முடிவுக்குக் கொண்டு வந்தது.\n4. 1858 அரசுச் சட்டம் 15 உறுப்பினர்கள் கொண்ட இந்திய கவுன்சிலுடன் கூடிய இந்திய அரசுச் செயலாளர் பதவியை உருவாக்கியது.\nஎது சரி?",
    "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டும்",
    "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டும்",
    "1, 3 and 4 only", "1, 3 மற்றும் 4 மட்டும்",
    "1, 2, 3 and 4", "1, 2, 3 மற்றும் 4",
    "D",
    "All four statements are correct. 1853 Act separated legislative/executive functions & opened civil services; 1858 Act ended Double Govt & set up Secretary of State with 15-member council.",
    "நான்கு கூற்றுகளும் சரியானவை. 1853 இல் பணிகள் பிரிப்பு & போட்டித் தேர்வு; 1858 இல் இரட்டை ஆட்சி ஒழிப்பு & அரசுச் செயலாளர் அமைப்பு.",
    "Incorrect. Statement 4 is also correct.",
    "தவறு. கூற்று 4-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Correct. All four statements are historically true.",
    "சரி. நான்கு கூற்றுகளும் வரலாற்று ரீதியாகச் சரியானவை.",
    "Lord Canning was Governor-General during 1857 Revolt and became first Viceroy under 1858 Act.",
    "1857 புரட்சியின் போது கவர்னர் ஜெனரலாக இருந்த கேனிங் பிரபு 1858 சட்டத்தில் முதல் வைஸ்ராயானார்.",
    "Macaulay Committee on Indian Civil Service was appointed in 1854 pursuant to 1853 Act.",
    "1853 சட்டத்தின்கீழ் 1854 இல் இந்திய குடிமைப் பணிக்கான மெக்காலே குழு அமைக்கப்பட்டது.",
    "Analyze", 75, ["Polity", "Historical Background", "1853 and 1858 Acts", "Four Statement"]
))

# HB_SB_034
questions.append(make_q(
    "HB_SB_034", "Statement Based",
    "Consider the following statements regarding Indian Councils Acts of 1861 and 1892:\n1. Indian Councils Act 1861 restored legislative powers to Bombay and Madras Presidencies.\n2. Indian Councils Act 1861 gave statutory recognition to Lord Canning's Portfolio System.\n3. Indian Councils Act 1892 allowed legislative members to discuss the budget for the first time.\n4. Indian Councils Act 1892 explicitly introduced the word 'election' in the constitutional statute.\nWhich of the statements given above are correct?",
    "1861 மற்றும் 1892 இந்தியக் கவுன்சில்கள் சட்டங்கள் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 1861 கவுன்சில்கள் சட்டம் பம்பாய் மற்றும் மதராஸ் மாகாணங்களுக்கு சட்ட அதிகாரங்களை மீண்டும் வழங்கியது.\n2. 1861 கவுன்சில்கள் சட்டம் கேனிங் பிரபுவின் துறை ஒதுக்கீடு முறைக்கு சட்டப்பூர்வ அங்கீகாரம் அளித்தது.\n3. 1892 கவுன்சில்கள் சட்டம் முதன்முறையாக உறுப்பினர்கள் பட்ஜெட்டை விவாதிக்க அனுமதித்தது.\n4. 1892 கவுன்சில்கள் சட்டம் அரசியலமைப்பு சட்டத்தில் 'தேர்தல்' என்ற சொல்லை வெளிப்படையாக அறிமுகப்படுத்தியது.\nஎது சரி?",
    "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டும்",
    "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டும்",
    "1, 3 and 4 only", "1, 3 மற்றும் 4 மட்டும்",
    "1, 2, 3 and 4", "1, 2, 3 மற்றும் 4",
    "A",
    "Statements 1, 2, and 3 are correct. Statement 4 is INCORRECT because the word 'election' was NOT used in the 1892 Act text (it was described as nomination on recommendation).",
    "கூற்றுகள் 1, 2, 3 சரி. கூற்று 4 தவறு, ஏனெனில் 'தேர்தல்' என்ற சொல் 1892 சட்டத்தில் தவிர்க்கப்பட்டது.",
    "Correct. Statements 1, 2, and 3 are correct; Statement 4 is false.",
    "சரி. கூற்றுகள் 1, 2, 3 சரி; கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "TNPSC Trap: 1892 Act used recommendation mechanism for non-official seats, but strictly avoided the word 'election'.",
    "TNPSC பொறி: 1892 சட்டம் பரிந்துரை முறையைப் பயன்படுத்தியது, ஆனால் 'தேர்தல்' என்ற சொல்லைத் தவிர்த்தது.",
    "1861 Act empowered Viceroy to issue Ordinances valid for 6 months during emergencies.",
    "1861 சட்டம் வைஸ்ராய்க்கு 6 மாதங்கள் செல்லுபடியாகும் அவசரச்சட்ட அதிகாரத்தை அளித்தது.",
    "Analyze", 75, ["Polity", "Historical Background", "1861 and 1892 Acts", "Four Statement"]
))

# HB_SB_035
questions.append(make_q(
    "HB_SB_035", "Statement Based",
    "Consider the following statements regarding the Indian Councils Act of 1909 (Morley-Minto Reforms):\n1. It increased the size of the Central Legislative Council from 16 to 60 members.\n2. It retained official majority in the Central Legislative Council, but allowed non-official majority in Provincial Legislative Councils.\n3. It introduced separate electorates for Muslims, where Muslim members were elected only by Muslim voters.\n4. Satyendra Prasad Sinha became the first Indian member of the Viceroy's Executive Council.\nWhich of the statements given above are correct?",
    "1909 ஆம் ஆண்டின் இந்தியக் கவுன்சில்கள் சட்டம் (மோர்லே-மிண்டோ சீர்திருத்தங்கள்) பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது மத்திய கவுன்சில் உறுப்பினர்களின் எண்ணிக்கையை 16 லிருந்து 60 ஆக உயர்த்தியது.\n2. இது மத்திய கவுன்சிலில் அதிகாரபூர்வ பெரும்பான்மையைத் தக்கவைத்தது, ஆனால் மாகாண கவுன்சில்களில் அரசுசாரா பெரும்பான்மையை அனுமதித்தது.\n3. இது முஸ்லிம்களுக்குத் தனித் தொகுதிகளை அறிமுகப்படுத்தியது, அங்கு முஸ்லிம் உறுப்பினர்கள் முஸ்லிம் வாக்காளர்களால் மட்டுமே தேர்ந்தெடுக்கப்பட்டனர்.\n4. சத்யேந்திர பிரசாத் சின்ஹா வைஸ்ராய் நிர்வாகக் குழுவின் முதல் இந்திய உறுப்பினரானார்.\nஎது சரி?",
    "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டும்",
    "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டும்",
    "1, 3 and 4 only", "1, 3 மற்றும் 4 மட்டும்",
    "1, 2, 3 and 4", "1, 2, 3 மற்றும் 4",
    "D",
    "All four statements are correct. 1909 Act expanded central council to 60, permitted provincial non-official majority, introduced Muslim separate electorates, and appointed S.P. Sinha as Law Member.",
    "நான்கு கூற்றுகளும் சரியானவை. 60 உறுப்பினர்களாக உயர்வு, மாகாண அரசுசாரா பெரும்பான்மை, முஸ்லிம் தனித் தொகுதி, மற்றும் எஸ்.பி. சின்ஹா நியமனம்.",
    "Incorrect. Statement 4 is also correct.",
    "தவறு. கூற்று 4-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Correct. All four statements are historically accurate.",
    "சரி. நான்கு கூற்றுகளும் வரலாற்று ரீதியாகச் சரியானவை.",
    "Lord Minto was Viceroy of India and Lord Morley was Secretary of State for India in 1909.",
    "1909 இல் லார்ட் மிண்டோ வைஸ்ராயாகவும் லார்ட் மோர்லே அரசுச் செயலாளராகவும் இருந்தனர்.",
    "1909 Act allowed members to ask supplementary questions and move budget resolutions for the first time.",
    "1909 சட்டம் உறுப்பினர்களுக்கு துணைக் கேள்விகள் கேட்கவும் பட்ஜெட் தீர்மானங்கள் கொண்டு வரவும் முதன்முறையாக அனுமதித்தது.",
    "Analyze", 75, ["Polity", "Historical Background", "Indian Councils Act 1909", "Four Statement"]
))

# Save checkpoint
questions.sort(key=lambda x: x["id"])
with open(target_path, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"Part 5 complete: {len(questions)} questions saved.")
