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

# HB_SB_026
questions.append(make_q(
    "HB_SB_026", "Statement Based",
    "Consider the following statements regarding the Indian Independence Act of 1947:\n1. It declared the lapse of British paramountcy over Indian Princely States from August 15, 1947.\n2. Section 6 empowered the Constituent Assembly of each dominion to alter or repeal any Act of British Parliament applying to India.\n3. It abolished the office of Secretary of State for India and transferred his functions to the Secretary of State for Commonwealth Affairs.\nWhich of the statements given above are correct?",
    "1947 ஆம் ஆண்டின் இந்திய சுதந்திரச் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது ஆகஸ்ட் 15, 1947 முதல் இந்திய சுதேச சமஸ்தானங்கள் மீதான பிரிட்டிஷ் மேலாதிக்கம் முடிவுக்கு வந்ததாக அறிவித்தது.\n2. பிரிவு 6 ஒவ்வொரு டொமினியனின் அரசியலமைப்பு சபைக்கும் இந்தியாவில் பொருந்தும் எந்தவொரு பிரிட்டிஷ் சட்டத்தையும் மாற்ற அல்லது ரத்து செய்ய அதிகாரமளித்தது.\n3. இது இந்திய அரசுச் செயலாளர் பதவியை ஒழித்து, அவரது பொறுப்புகளை காமன்வெல்த் விவகாரச் செயலாளருக்கு மாற்றியது.\nஎது சரி?",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "D",
    "All three statements are correct. 1947 Act ended British paramountcy over Princely States, Section 6 conferred sovereign repeal powers to Assembly, and Secretary of State office was abolished.",
    "மூன்று கூற்றுகளும் சரியானவை. சுதேச சமஸ்தானங்கள் மீதான மேலாதிக்கம் முடிவு, பிரிவு 6 சட்டம் ரத்து செய்யும் அதிகாரம், மற்றும் அரசுச் செயலாளர் பதவி ஒழிப்பு.",
    "Incorrect. Statement 3 is also correct.",
    "தவறு. கூற்று 3-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Correct. All three statements accurately reflect the Indian Independence Act 1947.",
    "சரி. மூன்று கூற்றுகளும் 1947 இந்திய சுதந்திரச் சட்டத்தைத் துல்லியமாகப் பிரதிபலிக்கின்றன.",
    "Indian Independence Act 1947 was based on Mountbatten Plan (June 3 Plan, 1947).",
    "1947 இந்திய சுதந்திரச் சட்டம் மவுண்ட்பேட்டன் திட்டத்தை (ஜூன் 3 திட்டம்) அடிப்படையாகக் கொண்டது.",
    "Indian Independence Act received Royal Assent on July 18, 1947.",
    "இந்திய சுதந்திரச் சட்டம் 1947 ஜூலை 18 அன்று மன்னரின் ஒப்புதலைப் பெற்றது.",
    "Analyze", 75, ["Polity", "Historical Background", "Indian Independence Act 1947", "Three Statement"]
))

# HB_SB_027
questions.append(make_q(
    "HB_SB_027", "Statement Based",
    "Consider the following statements regarding the evolution of Civil Services in British India:\n1. Charter Act 1833 made the first attempt to introduce an open competition system, but it was negated due to opposition from the Court of Directors.\n2. Charter Act 1853 successfully introduced open competition for civil services, leading to the appointment of Macaulay Committee in 1854.\n3. The Lee Commission (1923) recommended the immediate establishment of a Public Service Commission, leading to Central PSC in 1926.\nWhich of the statements given above are correct?",
    "பிரிட்டிஷ் இந்தியாவில் குடிமைப் பணிகளின் வளர்ச்சி பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 1833 சாசனச் சட்டம் திறந்தவெளிப் போட்டி முறையை அறிமுகப்படுத்த முதல் முயற்சியை மேற்கொண்டது, ஆனால் இயக்குநர்கள் அவையின் எதிர்ப்பால் அது நிராகரிக்கப்பட்டது.\n2. 1853 சாசனச் சட்டம் குடிமைப் பணிகளுக்கு திறந்தவெளிப் போட்டியை வெற்றிகரமாக அறிமுகப்படுத்தி 1854 இல் மெக்காலே குழு அமையக் காரணமானது.\n3. லீ ஆணையம் (1923) உடனடியாக பொதுச் சேவை ஆணையத்தை நிறுவப் பரிந்துரைத்து 1926 இல் மத்திய PSC அமையக் காரணமானது.\nஎது சரி?",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "D",
    "All three statements are correct. 1833 attempted open competition, 1853 successfully enacted it (Macaulay Comm 1854), and 1923 Lee Commission led to Central PSC in 1926.",
    "மூன்று கூற்றுகளும் சரியானவை. 1833 முதல் முயற்சி, 1853 வெற்றிபெற்ற சட்டம் (1854 மெக்காலே குழு), மற்றும் 1923 லீ ஆணையத்தால் 1926 இல் மத்திய PSC.",
    "Incorrect. Statement 3 is also correct.",
    "தவறு. கூற்று 3-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Correct. All three statements accurately trace Civil Services history.",
    "சரி. மூன்று கூற்றுகளும் குடிமைப் பணி வரலாற்றைத் துல்லியமாகக் காட்டுகின்றன.",
    "Satyendranath Tagore (elder brother of Rabindranath Tagore) was the first Indian to clear Indian Civil Services exam in 1863.",
    "1863 இல் இந்திய குடிமைப் பணித் தேர்வில் தேர்ச்சி பெற்ற முதல் இந்தியர் சத்யேந்திரநாத் தாகூர் ஆவார்.",
    "Federal Public Service Commission created under 1935 Act became Union Public Service Commission (UPSC) under 1950 Constitution.",
    "1935 சட்டத்தின் கூட்டாட்சி PSC 1950 அரசியலமைப்பில் UPSC என உருவானது.",
    "Analyze", 75, ["Polity", "Historical Background", "Civil Services Arc", "Three Statement"]
))

# HB_SB_028
questions.append(make_q(
    "HB_SB_028", "Statement Based",
    "Consider the following statements regarding the financial legislative progression in British India:\n1. The Indian Councils Act 1892 allowed legislative members to discuss the budget for the first time.\n2. The Indian Councils Act 1909 allowed members to ask supplementary questions and move budget resolutions.\n3. The Government of India Act 1919 granted council members the right to vote on demands for grants and separated Provincial Budgets from the Central Budget.\nWhich of the statements given above are correct?",
    "பிரிட்டிஷ் இந்தியாவில் நிதி தொடர்பான சட்ட வளர்ச்சி பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 1892 இந்தியக் கவுன்சில்கள் சட்டம் முதன்முறையாக உறுப்பினர்கள் பட்ஜெட்டை விவாதிக்க அனுமதித்தது.\n2. 1909 இந்தியக் கவுன்சில்கள் சட்டம் உறுப்பினர்களுக்கு துணைக் கேள்விகள் கேட்கவும் பட்ஜெட் தீர்மானங்களைக் கொண்டு வரவும் அனுமதித்தது.\n3. 1919 இந்திய அரசுச் சட்டம் உறுப்பினர்களுக்கு மானியக் கோரிக்கைகள் மீது வாக்களிக்கும் உரிமையை வழங்கியதுடன் மாகாண பட்ஜெட்டை மத்திய பட்ஜெட்டிலிருந்து பிரித்தது.\nஎது சரி?",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "D",
    "All three statements are correct. 1892 budget discussion allowed -> 1909 supplementary questions/resolutions -> 1919 voting on demands & provincial budget separation.",
    "மூன்று கூற்றுகளும் சரியானவை. 1892 பட்ஜெட் விவாதம் -> 1909 துணைக் கேள்விகள் -> 1919 மானியக் கோரிக்கை வாக்களிப்பு & மாகாண பட்ஜெட் பிரிப்பு.",
    "Incorrect. Statement 3 is also correct.",
    "தவறு. கூற்று 3-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Correct. All three statements accurately trace Financial Control evolution.",
    "சரி. மூன்று கூற்றுகளும் நிதி கட்டுப்பாட்டு வளர்ச்சியைத் துல்லியமாகக் காட்டுகின்றன.",
    "Separation of Railway Budget from General Budget occurred in 1924 based on Acworth Committee recommendations.",
    "அக்வொர்த் குழுப் பரிந்துரைப்படி 1924 இல் இரயில்வே பட்ஜெட் பொது பட்ஜெட்டிலிருந்து பிரிக்கப்பட்டது.",
    "Under 1919 Act, about 70% of the Central budget demands were subject to voting.",
    "1919 சட்டப்படி மத்திய பட்ஜெட் கோரிக்கைகளில் சுமார் 70% வாக்களிப்பிற்கு உட்பட்டது.",
    "Analyze", 75, ["Polity", "Historical Background", "Financial Control Arc", "Three Statement"]
))

# HB_SB_029
questions.append(make_q(
    "HB_SB_029", "Statement Based",
    "Consider the following statements regarding the progression of Electorates and Franchise in British India:\n1. The Indian Councils Act 1909 introduced Separate Electorates exclusively for Muslims.\n2. The Government of India Act 1919 extended Separate Electorates to Sikhs, Indian Christians, Anglo-Indians, and Europeans.\n3. The Government of India Act 1935 extended Separate Electorates to Depressed Classes (Scheduled Castes), Women, and Labour.\nWhich of the statements given above are correct?",
    "பிரிட்டிஷ் இந்தியாவில் தொகுதிகள் மற்றும் வாக்குரிமை விரிவாக்கம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 1909 இந்தியக் கவுன்சில்கள் சட்டம் முஸ்லிம்களுக்கு மட்டுமே பிரத்யேகத் தனித் தொகுதியை அறிமுகப்படுத்தியது.\n2. 1919 இந்திய அரசுச் சட்டம் சீக்கியர்கள், இந்தியக் கிறிஸ்தவர்கள், ஆங்கிலோ-இந்தியர்கள், ஐரோப்பியர்களுக்குத் தனித் தொகுதிகளை விரிவுபடுத்தியது.\n3. 1935 இந்திய அரசுச் சட்டம் தாழ்த்தப்பட்ட பிரிவினர் (பட்டியல் சாதியினர்), பெண்கள், தொழிலாளர்களுக்குத் தனித் தொகுதிகளை விரிவுபடுத்தியது.\nஎது சரி?",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "D",
    "All three statements are correct. Electorates expanded in 3 stages: 1909 (Muslims) -> 1919 (Sikhs, Christians, Europeans, Anglo-Indians) -> 1935 (Depressed classes, Women, Labour).",
    "மூன்று கூற்றுகளும் சரியானவை. தொகுதி விரிவாக்கம் 3 கட்டங்கள்: 1909 (முஸ்லிம்கள்) -> 1919 (சீக்கியர்கள், கிறிஸ்தவர்கள்) -> 1935 (பட்டியல் சாதியினர், பெண்கள்).",
    "Incorrect. Statement 3 is also correct.",
    "தவறு. கூற்று 3-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Correct. All three statements accurately trace Communal Electorates expansion.",
    "சரி. மூன்று கூற்றுகளும் வகுப்புவாத தொகுதி விரிவாக்கத்தைத் துல்லியமாகக் காட்டுகின்றன.",
    "The Communal Award was announced by British Prime Minister Ramsay MacDonald in August 1932.",
    "ராம்சே மெக்டொனால்டு 1932 ஆகஸ்டில் வகுப்புவாத கொடையை அறிவித்தார்.",
    "Poona Pact (1932) retained joint electorate for Depressed Classes with reserved seats.",
    "பூனா ஒப்பந்தம் (1932) தாழ்த்தப்பட்ட பிரிவினருக்கு இடஒதுக்கீட்டுடன் கூடிய கூட்டுத் தொகுதியைத் தக்கவைத்தது.",
    "Analyze", 75, ["Polity", "Historical Background", "Communal Electorates Arc", "Three Statement"]
))

# HB_SB_030
questions.append(make_q(
    "HB_SB_030", "Statement Based",
    "Consider the following statements regarding the Constituent Assembly under the Cabinet Mission Plan (1946):\n1. The total strength of the Constituent Assembly was fixed at 389 members (296 for British India and 93 for Princely States).\n2. Members from British Indian provinces were indirectly elected by the members of provincial legislative assemblies using single transferable vote.\n3. Members from Princely States were directly elected by universal adult franchise.\nWhich of the statements given above is/are correct?",
    "கேபினட் மிஷன் திட்டத்தின்கீழ் (1946) அமைக்கப்பட்ட அரசியலமைப்பு சபை பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. அரசியலமைப்பு சபையின் மொத்த உறுப்பினர்களின் எண்ணிக்கை 389 என நிர்ணயிக்கப்பட்டது (பிரிட்டிஷ் இந்தியா 296, சுதேச சமஸ்தானங்கள் 93).\n2. பிரிட்டிஷ் இந்திய மாகாண உறுப்பினர்கள் மாகாண சட்டமன்ற உறுப்பினர்களால் ஒற்றை மாற்றத்தக்க வாக்கு மூலம் மறைமுகமாகத் தேர்ந்தெடுக்கப்பட்டனர்.\n3. சுதேச சமஸ்தான உறுப்பினர்கள் உலகளாவிய வயதுவந்தோர் வாக்குரிமை மூலம் நேரடியாகத் தேர்ந்தெடுக்கப்பட்டனர்.\nஎது சரி?",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "A",
    "Statements 1 and 2 are correct. Statement 3 is INCORRECT because members from Princely States were NOT elected; they were nominated by the heads of the Princely States.",
    "கூற்றுகள் 1 மற்றும் 2 சரி. கூற்று 3 தவறு, ஏனெனில் சுதேச சமஸ்தான உறுப்பினர்கள் தேர்ந்தெடுக்கப்படவில்லை; அவர்கள் மன்னர்களால் நியமிக்கப்பட்டனர்.",
    "Correct. Statements 1 and 2 are correct; Statement 3 is false.",
    "சரி. கூற்றுகள் 1 மற்றும் 2 சரி; கூற்று 3 தவறானது.",
    "Incorrect. Statement 3 is false.",
    "தவறு. கூற்று 3 தவறானது.",
    "Incorrect. Statement 3 is false.",
    "தவறு. கூற்று 3 தவறானது.",
    "Incorrect. Statement 3 is false.",
    "தவறு. கூற்று 3 தவறானது.",
    "TNPSC Trap: Constituent Assembly was a partly elected and partly nominated body.",
    "TNPSC பொறி: அரசியலமைப்பு சபை பகுதி அளவு தேர்ந்தெடுக்கப்பட்ட மற்றும் பகுதி அளவு நியமிக்கப்பட்ட அமைப்பாகும்.",
    "Constituent Assembly elections were held in July-August 1946 for 296 seats.",
    "296 இடங்களுக்கு 1946 ஜூலை-ஆகஸ்டில் தேர்தல்கள் நடந்தன.",
    "Analyze", 75, ["Polity", "Historical Background", "Constituent Assembly Scheme", "Three Statement"]
))

# Save checkpoint
questions.sort(key=lambda x: x["id"])
with open(target_path, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"Part 4 complete: {len(questions)} questions saved.")
