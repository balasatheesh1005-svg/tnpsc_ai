import json
import sys
from pathlib import Path

target_path = Path(r"c:\Users\Home\Desktop\tnpsc_ai\data\questions\polity\historical_background_statement_based.json")
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

# HB_SB_006
questions.append(make_q(
    "HB_SB_006", "Statement Based",
    "Consider the following statements regarding the Charter Act of 1853:\n1. It separated for the first time the legislative and executive functions of the Governor-General's Council.\n2. It introduced an open competition system for the selection and recruitment of civil servants.\nWhich of the statements given above is/are correct?",
    "1853 ஆம் ஆண்டின் சாசனச் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது முதன்முறையாக கவர்னர் ஜெனரல் கவுன்சிலின் சட்டமன்ற மற்றும் நிர்வாகப் பணிகளைப் பிரித்தது.\n2. இது குடிமைப் பணியாளர்களைத் தேர்ந்தெடுப்பதற்கும் சேர்ப்பதற்கும் திறந்தவெளிப் போட்டி முறையை அறிமுகப்படுத்தியது.\nஎது சரி?",
    "1 only", "1 மட்டும்",
    "2 only", "2 மட்டும்",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை",
    "C",
    "Both statements are correct. Charter Act 1853 separated legislative/executive functions (created Indian Legislative Council) and opened civil service recruitment to open competition.",
    "இரண்டு கூற்றுகளும் சரியானவை. 1853 சாசனச் சட்டம் சட்டமன்ற/நிர்வாகப் பணிகளைப் பிரித்ததுடன் குடிமைப் பணிகளைத் திறந்தவெளிப் போட்டிக்குக் கொண்டு வந்தது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Correct. Both Statements 1 and 2 are historically true.",
    "சரி. கூற்றுகள் 1 மற்றும் 2 இரண்டும் உண்மை.",
    "Incorrect. Both statements are correct.",
    "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
    "The 1853 Act introduced local representation in Central Legislative Council for the first time (4 members from Madras, Bombay, Bengal, Agra).",
    "1853 சட்டம் மத்திய சட்டமன்ற கவுன்சிலில் உள்ளூர் பிரதிநிதித்துவத்தை (மதராஸ், பம்பாய், வங்காளம், ஆக்ரா) அறிமுகப்படுத்தியது.",
    "Macaulay Committee on Indian Civil Service was appointed in 1854 pursuant to 1853 Act.",
    "1853 சட்டத்தைத் தொடர்ந்து 1854 இல் இந்திய குடிமைப் பணிக்கான மெக்காலே குழு அமைக்கப்பட்டது.",
    "Analyze", 75, ["Polity", "Historical Background", "Charter Act 1853", "Two Statement"]
))

# HB_SB_007
questions.append(make_q(
    "HB_SB_007", "Statement Based",
    "Consider the following statements regarding the Government of India Act 1858:\n1. It abolished the East India Company's Court of Directors and Board of Control.\n2. It created a 15-member Council of India to assist the Secretary of State for India.\nWhich of the statements given above is/are correct?",
    "1858 ஆம் ஆண்டின் இந்திய அரசுச் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது கிழக்கிந்தியக் கம்பெனியின் இயக்குநர்கள் அவை மற்றும் கட்டுப்பாட்டு வாரியத்தைக் கலைத்தது.\n2. இது இந்திய அரசுச் செயலாளருக்கு உதவ 15 உறுப்பினர்களைக் கொண்ட இந்திய கவுன்சிலை உருவாக்கியது.\nஎது சரி?",
    "1 only", "1 மட்டும்",
    "2 only", "2 மட்டும்",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை",
    "C",
    "Both statements are correct. GOI Act 1858 ended Double Government (abolished Board of Control & Directors) and created Secretary of State for India assisted by a 15-member Council of India.",
    "இரண்டு கூற்றுகளும் சரியானவை. 1858 அரசுச் சட்டம் இரட்டை நிர்வாகத்தைக் கலைத்ததுடன் 15 உறுப்பினர்கள் கொண்ட இந்திய கவுன்சிலுடன் கூடிய அரசுச் செயலாளரை உருவாக்கியது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Correct. Both Statements 1 and 2 are historically true.",
    "சரி. கூற்றுகள் 1 மற்றும் 2 இரண்டும் உண்மை.",
    "Incorrect. Both statements are correct.",
    "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
    "GOI Act 1858 changed designation of Governor-General of India to Viceroy of India (Lord Canning became first Viceroy).",
    "1858 சட்டம் இந்திய கவர்னர் ஜெனரல் பதவியை இந்திய வைஸ்ராய் என மாற்றியது (கேனிங் பிரபு முதல் வைஸ்ராயானார்).",
    "The 15-member Council of India was an advisory body chaired by the Secretary of State.",
    "15 உறுப்பினர்கள் கொண்ட இந்திய கவுன்சில் என்பது அரசுச் செயலாளர் தலைமையிலான ஓர் ஆலோசனைக் குழுவாகும்.",
    "Analyze", 75, ["Polity", "Historical Background", "Government of India Act 1858", "Two Statement"]
))

# HB_SB_008
questions.append(make_q(
    "HB_SB_008", "Statement Based",
    "Consider the following statements regarding the Indian Councils Act of 1861:\n1. It initiated legislative decentralization by restoring law-making powers to Bombay and Madras Presidencies.\n2. It empowered the Viceroy to issue ordinances during emergencies with a validity period of one year.\nWhich of the statements given above is/are correct?",
    "1861 ஆம் ஆண்டின் இந்தியக் கவுன்சில்கள் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது பம்பாய் மற்றும் மதராஸ் மாகாணங்களுக்கு சட்ட அதிகாரங்களை மீட்டு சட்டமன்ற பரவலாக்கலைத் தொடங்கியது.\n2. இது அவசரகாலத்தில் ஒரு வருடம் செல்லுபடியாகும் அவசரச்சட்டங்களை பிறப்பிக்க வைஸ்ராய்க்கு அதிகாரமளித்தது.\nஎது சரி?",
    "1 only", "1 மட்டும்",
    "2 only", "2 மட்டும்",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை",
    "A",
    "Statement 1 is correct (restored legislative powers to Bombay/Madras). Statement 2 is INCORRECT because Viceroy's Ordinance validity was SIX MONTHS, not one year.",
    "கூற்று 1 சரி (பம்பாய்/மதராஸ் சட்ட அதிகாரங்கள் மீட்பு). கூற்று 2 தவறு, ஏனெனில் வைஸ்ராய் அவசரச்சட்டத்தின் செல்லுபடி காலம் 6 மாதங்கள் மட்டுமே, ஒரு வருடம் அல்ல.",
    "Correct. Statement 1 is true; Statement 2 is false.",
    "சரி. கூற்று 1 சரி; கூற்று 2 தவறானது.",
    "Incorrect. Statement 2 is false.",
    "தவறு. கூற்று 2 தவறானது.",
    "Incorrect. Statement 2 is false.",
    "தவறு. கூற்று 2 தவறானது.",
    "Incorrect. Statement 1 is correct.",
    "தவறு. கூற்று 1 சரியானது.",
    "TNPSC Trap: Ordinance validity under Indian Councils Act 1861 was 6 MONTHS (not 1 year).",
    "TNPSC பொறி: 1861 சட்டப்படி வைஸ்ராய் அவசரச்சட்டத்தின் செல்லுபடியாகும் காலம் 6 மாதங்கள் (1 வருடம் அல்ல).",
    "1861 Act legalized Lord Canning's Portfolio System introduced in 1859.",
    "1861 சட்டம் 1859 இல் லார்ட் கேனிங் கொண்டு வந்த துறை ஒதுக்கீடு முறையை சட்டப்பூர்வமாக்கியது.",
    "Analyze", 75, ["Polity", "Historical Background", "Indian Councils Act 1861", "Two Statement"]
))

# HB_SB_009
questions.append(make_q(
    "HB_SB_009", "Statement Based",
    "Consider the following statements regarding the Indian Councils Act of 1892:\n1. It increased the number of additional non-official members in Central and Provincial Legislative Councils.\n2. It gave members the right to ask supplementary questions and vote on the budget.\nWhich of the statements given above is/are correct?",
    "1892 ஆம் ஆண்டின் இந்தியக் கவுன்சில்கள் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது மத்திய மற்றும் மாகாண சட்டமன்ற கவுன்சில்களில் கூடுதல் அரசுசாரா உறுப்பினர்களின் எண்ணிக்கையை உயர்த்தியது.\n2. இது உறுப்பினர்களுக்கு துணைக் கேள்விகள் கேட்கவும் பட்ஜெட் மீது வாக்களிக்கவும் உரிமை வழங்கியது.\nஎது சரி?",
    "1 only", "1 மட்டும்",
    "2 only", "2 மட்டும்",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை",
    "A",
    "Statement 1 is correct (increased non-official members). Statement 2 is INCORRECT because 1892 Act allowed ONLY budget discussion and asking questions with 6 days notice; it did NOT permit supplementary questions or voting on the budget.",
    "கூற்று 1 சரி (அரசுசாரா உறுப்பினர்கள் அதிகரிப்பு). கூற்று 2 தவறு, ஏனெனில் 1892 சட்டம் பட்ஜெட் விவாதம் & கேள்விகளை மட்டுமே அனுமதித்தது; துணைக் கேள்விகள்/வாக்களிப்பு அனுமதி இல்லை.",
    "Correct. Statement 1 is true; Statement 2 is false.",
    "சரி. கூற்று 1 சரி; கூற்று 2 தவறானது.",
    "Incorrect. Statement 2 is false.",
    "தவறு. கூற்று 2 தவறானது.",
    "Incorrect. Statement 2 is false.",
    "தவறு. கூற்று 2 தவறானது.",
    "Incorrect. Statement 1 is correct.",
    "தவறு. கூற்று 1 சரியானது.",
    "1892 Act introduced an element of indirect election via recommendation, but avoided the word 'election' in the statute text.",
    "1892 சட்டம் பரிந்துரை மூலமான மறைமுகத் தேர்தல் கூறைக் கொண்டு வந்தது, ஆனால் 'தேர்தல்' என்ற சொல்லைத் தவிர்த்தது.",
    "Budget discussion was permitted for the first time in India under Indian Councils Act 1892.",
    "இந்தியாவில் முதன்முறையாக பட்ஜெட் விவாதம் 1892 இந்தியக் கவுன்சில்கள் சட்டத்தின் கீழ் அனுமதிக்கப்பட்டது.",
    "Analyze", 75, ["Polity", "Historical Background", "Indian Councils Act 1892", "Two Statement"]
))

# HB_SB_010
questions.append(make_q(
    "HB_SB_010", "Statement Based",
    "Consider the following statements regarding the Indian Councils Act of 1909 (Morley-Minto Reforms):\n1. It introduced a system of communal representation for Muslims by accepting the concept of separate electorate.\n2. Satyendra Prasad Sinha became the first Indian to join the Governor-General's Executive Council.\nWhich of the statements given above is/are correct?",
    "1909 ஆம் ஆண்டின் இந்தியக் கவுன்சில்கள் சட்டம் (மோர்லே-மிண்டோ சீர்திருத்தங்கள்) பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது தனித் தொகுதி முறையை ஏற்றுக்கொண்டு முஸ்லிம்களுக்கு வகுப்புவாத பிரதிநிதித்துவ முறையை அறிமுகப்படுத்தியது.\n2. சத்யேந்திர பிரசாத் சின்ஹா கவர்னர் ஜெனரலின் நிர்வாகக் குழுவில் இணைந்த முதல் இந்தியரானார்.\nஎது சரி?",
    "1 only", "1 மட்டும்",
    "2 only", "2 மட்டும்",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை",
    "C",
    "Both statements are correct. Morley-Minto Reforms 1909 introduced Separate Electorates for Muslims (Lord Minto = Father of Communal Electorate) and appointed Satyendra Prasad Sinha as Law Member in Viceroy's Executive Council.",
    "இரண்டு கூற்றுகளும் சரியானவை. 1909 சட்டம் முஸ்லிம்களுக்குத் தனித் தொகுதியை கொண்டு வந்ததுடன் எஸ்.பி. சின்ஹாவை வைஸ்ராய் நிர்வாகக் குழுவின் சட்ட உறுப்பினராக நியமித்தது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Correct. Both Statements 1 and 2 are historically true.",
    "சரி. கூற்றுகள் 1 மற்றும் 2 இரண்டும் உண்மை.",
    "Incorrect. Both statements are correct.",
    "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
    "Lord Minto came to be known as the 'Father of Communal Electorate' due to the 1909 reforms.",
    "1909 சீர்திருத்தங்களால் லார்ட் மிண்டோ 'வகுப்புவாதத் தொகுதிகளின் தந்தை' என அழைக்கப்பட்டார்.",
    "1909 Act retained official majority in Central Legislative Council, but allowed non-official majority in Provincial Legislative Councils.",
    "1909 சட்டம் மத்திய கவுன்சிலில் அதிகாரபூர்வ பெரும்பான்மையையும் மாகாண கவுன்சில்களில் அரசுசாரா பெரும்பான்மையையும் அனுமதித்தது.",
    "Analyze", 75, ["Polity", "Historical Background", "Indian Councils Act 1909", "Two Statement"]
))

# Deduplicate by ID
seen = set()
uniq = []
for q in questions:
    if q["id"] not in seen:
        seen.add(q["id"])
        uniq.append(q)

uniq.sort(key=lambda x: x["id"])

print(f"Total Questions: {len(uniq)}")

# Save to target file
with open(target_path, "w", encoding="utf-8") as f:
    json.dump(uniq, f, ensure_ascii=False, indent=2)

# Run validation
sys.path.insert(0, r"c:\Users\Home\Desktop\tnpsc_ai")
from core.question_engine.validators import validate_questions
val_res = validate_questions(uniq)
print(f"Validation Result: Valid={val_res.valid}")
if val_res.errors:
    print("Validation Errors:", val_res.errors)
if val_res.warnings:
    print("Validation Warnings:", val_res.warnings)
