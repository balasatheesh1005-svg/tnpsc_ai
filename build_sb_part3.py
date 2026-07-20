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

# HB_SB_021
questions.append(make_q(
    "HB_SB_021", "Statement Based",
    "Consider the following statements regarding the Indian Councils Act of 1861:\n1. It gave statutory recognition to Lord Canning's Portfolio System introduced in 1859.\n2. It empowered the Governor-General to issue ordinances during emergency without council consent, valid for six months.\n3. Lord Canning nominated three Indians—the Raja of Benares, the Maharaja of Patiala, and Sir Dinkar Rao—to the Central Legislative Council in 1862.\nWhich of the statements given above are correct?",
    "1861 ஆம் ஆண்டின் இந்தியக் கவுன்சில்கள் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது 1859 இல் லார்ட் கேனிங் அறிமுகப்படுத்திய 'துறை ஒதுக்கீடு முறைக்கு' (Portfolio System) சட்டப்பூர்வ அங்கீகாரம் அளித்தது.\n2. கவுன்சில் ஒப்புதலின்றி அவசரகாலத்தில் 6 மாத காலம் செல்லுபடியாகும் அவசரச்சட்டங்களை பிறப்பிக்க இது கவர்னர் ஜெனரலுக்கு அதிகாரமளித்தது.\n3. கேனிங் பிரபு 1862 இல் காசி ராஜா, பாட்டியாலா மகாராஜா, மற்றும் சர் தினகர் ராவ் ஆகிய மூன்று இந்தியர்களை மத்திய கவுன்சிலுக்கு நியமித்தார்.\nஎது சரி?",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "D",
    "All three statements are correct. 1861 Act recognized Portfolio system, authorized 6-month Ordinance power, and Canning nominated 3 Indian non-official members in 1862.",
    "மூன்று கூற்றுகளும் சரியானவை. துறை ஒதுக்கீடு முறை அங்கீகாரம், 6 மாத அவசரச்சட்ட அதிகாரம், மற்றும் 3 இந்திய உறுப்பினர்கள் நியமனம்.",
    "Incorrect. Statement 3 is also correct.",
    "தவறு. கூற்று 3-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Correct. All three statements accurately reflect the Indian Councils Act 1861.",
    "சரி. மூன்று கூற்றுகளும் 1861 இந்தியக் கவுன்சில்கள் சட்டத்தைத் துல்லியமாகப் பிரதிபலிக்கின்றன.",
    "1861 Act established legislative councils for Bengal (1862), NWFP (1886), and Punjab (1897).",
    "1861 சட்டம் வங்காளம் (1862), வடமேற்கு எல்லைப்புற மாகாணம் (1886), பஞ்சாப் (1897) ஆகியவற்றிற்கு கவுன்சில்களை அமைத்தது.",
    "The Portfolio System allowed a member of the executive council to be in charge of one or more government departments.",
    "துறை ஒதுக்கீடு முறை நிர்வாகக் குழு உறுப்பினர் ஒருவரே ஒன்று அல்லது அதற்கு மேற்பட்ட துறைகளுக்குப் பொறுப்பேற்க அனுமதித்தது.",
    "Analyze", 75, ["Polity", "Historical Background", "Indian Councils Act 1861", "Three Statement"]
))

# HB_SB_022
questions.append(make_q(
    "HB_SB_022", "Statement Based",
    "Consider the following statements regarding the Indian Councils Act of 1892:\n1. It introduced an indirect element of election for non-official seats based on recommendations of local bodies.\n2. It permitted legislative council members to discuss the budget and address questions to the executive with six days prior notice.\n3. It allowed members to ask supplementary questions and vote on individual budget items.\nWhich of the statements given above is/are correct?",
    "1892 ஆம் ஆண்டின் இந்தியக் கவுன்சில்கள் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது உள்ளாட்சி அமைப்புகளின் பரிந்துரைகளின் அடிப்படையில் அரசுசாரா இடங்களுக்கு மறைமுகத் தேர்தல் கூறைக் கொண்டு வந்தது.\n2. இது ஆறு நாட்கள் முன்னறிவிப்புடன் பட்ஜெட்டை விவாதிக்கவும் நிர்வாகத்திற்கு கேள்விகள் கேட்கவும் உறுப்பினர்களை அனுமதித்தது.\n3. இது உறுப்பினர்களுக்கு துணைக் கேள்விகள் கேட்கவும் தனிப்பட்ட பட்ஜெட் உருப்படிகள் மீது வாக்களிக்கவும் அனுமதித்தது.\nஎது சரி?",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "A",
    "Statements 1 and 2 are correct. Statement 3 is INCORRECT because supplementary questions and voting on budget were NOT allowed under 1892 Act (they were introduced under 1909 and 1919 Acts).",
    "கூற்றுகள் 1 மற்றும் 2 சரி. கூற்று 3 தவறு, ஏனெனில் 1892 சட்டத்தில் துணைக் கேள்விகளோ அல்லது பட்ஜெட் வாக்களிப்போ அனுமதிக்கப்படவில்லை.",
    "Correct. Statements 1 and 2 are correct; Statement 3 is false.",
    "சரி. கூற்றுகள் 1 மற்றும் 2 சரி; கூற்று 3 தவறானது.",
    "Incorrect. Statement 3 is false.",
    "தவறு. கூற்று 3 தவறானது.",
    "Incorrect. Statement 3 is false.",
    "தவறு. கூற்று 3 தவறானது.",
    "Incorrect. Statement 3 is false.",
    "தவறு. கூற்று 3 தவறானது.",
    "TNPSC Trap: Supplementary questions were introduced in 1909 Morley-Minto reforms, NOT in 1892.",
    "TNPSC பொறி: துணைக் கேள்விகள் கேட்கும் உரிமை 1909 சீர்திருத்தங்களில்தான் அறிமுகப்படுத்தப்பட்டது, 1892 இல் அல்ல.",
    "The word 'election' was deliberately avoided in the text of the 1892 Act.",
    "1892 சட்டத்தின் உரையில் 'தேர்தல்' என்ற சொல் வேண்டுமென்றே தவிர்க்கப்பட்டது.",
    "Analyze", 75, ["Polity", "Historical Background", "Indian Councils Act 1892", "Three Statement"]
))

# HB_SB_023
questions.append(make_q(
    "HB_SB_023", "Statement Based",
    "Consider the following statements regarding the Indian Councils Act of 1909:\n1. It retained an official majority in the Central Legislative Council, but allowed non-official majorities in Provincial Legislative Councils.\n2. It granted members the right to ask supplementary questions and move budget resolutions.\n3. It introduced separate electorates for Muslims, earning Lord Minto the title 'Father of Communal Electorate'.\nWhich of the statements given above are correct?",
    "1909 ஆம் ஆண்டின் இந்தியக் கவுன்சில்கள் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது மத்திய கவுன்சிலில் அதிகாரபூர்வ பெரும்பான்மையைத் தக்கவைத்தது, ஆனால் மாகாண கவுன்சில்களில் அரசுசாரா பெரும்பான்மையை அனுமதித்தது.\n2. இது உறுப்பினர்களுக்கு துணைக் கேள்விகள் கேட்கவும் பட்ஜெட் தீர்மானங்களைக் கொண்டு வரவும் உரிமை அளித்தது.\n3. இது முஸ்லிம்களுக்குத் தனித் தொகுதிகளை அறிமுகப்படுத்தி, லார்ட் மிண்டோவுக்கு 'வகுப்புவாதத் தொகுதிகளின் தந்தை' என்ற பட்டத்தைப் பெற்றுத் தந்தது.\nஎது சரி?",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "D",
    "All three statements are correct. 1909 Act allowed provincial non-official majorities, permitted supplementary questions/resolutions, and established Muslim separate electorates.",
    "மூன்று கூற்றுகளும் சரியானவை. மாகாண அரசுசாரா பெரும்பான்மை, துணைக் கேள்விகள்/தீர்மானங்கள் உரிமை, மற்றும் முஸ்லிம் தனித் தொகுதி.",
    "Incorrect. Statement 3 is also correct.",
    "தவறு. கூற்று 3-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Correct. All three statements accurately represent the 1909 Act.",
    "சரி. மூன்று கூற்றுகளும் 1909 சட்டத்தைச் சரியாகப் பிரதிபலிக்கின்றன.",
    "Satyendra Prasad Sinha was the first Indian appointed to the Viceroy's Executive Council (as Law Member) under 1909 Act.",
    "1909 சட்டப்படி சத்யேந்திர பிரசாத் சின்ஹா வைஸ்ராய் நிர்வாகக் குழுவின் முதல் இந்திய சட்ட உறுப்பினராக நியமிக்கப்பட்டார்.",
    "1909 Act expanded Central Legislative Council membership from 16 to 60.",
    "1909 சட்டம் மத்திய கவுன்சில் உறுப்பினர்களின் எண்ணிக்கையை 16 லிருந்து 60 ஆக உயர்த்தியது.",
    "Analyze", 75, ["Polity", "Historical Background", "Indian Councils Act 1909", "Three Statement"]
))

# HB_SB_024
questions.append(make_q(
    "HB_SB_024", "Statement Based",
    "Consider the following statements regarding the Government of India Act of 1919:\n1. It introduced Dyarchy in eight provinces by dividing subjects into Reserved (administered by Governor & Executive Council) and Transferred (administered by Governor & Ministers).\n2. It created the office of High Commissioner for India in London and transferred some functions of the Secretary of State to him.\n3. It established a Central Public Service Commission in 1926 based on recommendations of the Lee Commission (1923).\nWhich of the statements given above are correct?",
    "1919 ஆம் ஆண்டின் இந்திய அரசுச் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது துறைகளை ஒதுக்கப்பட்டவை (கவர்னர் & கவுன்சில்) மற்றும் மாற்றப்பட்டவை (கவர்னர் & அமைச்சர்கள்) எனப் பிரித்து 8 மாகாணங்களில் இரட்டை ஆட்சியை அறிமுகப்படுத்தியது.\n2. இது லண்டனில் இந்திய உயர் ஆணையர் அலுவலகத்தை உருவாக்கி, அரசுச் செயலாளரின் சில பொறுப்புகளை அவருக்கு மாற்றியது.\n3. இது 1923 லீ ஆணையப் பரிந்துரைப்படி 1926 இல் மத்திய பொதுச் சேவை ஆணையத்தை நிறுவியது.\nஎது சரி?",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "D",
    "All three statements are correct. 1919 Act introduced provincial Dyarchy, created High Commissioner for India in London, and set up Central PSC in 1926 (Lee Comm).",
    "மூன்று கூற்றுகளும் சரியானவை. மாகாண இரட்டை ஆட்சி, லண்டனில் உயர் ஆணையர் பதவி, மற்றும் 1926 இல் மத்திய PSC அமைப்பு.",
    "Incorrect. Statement 3 is also correct.",
    "தவறு. கூற்று 3-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Correct. All three statements accurately reflect the GOI Act 1919.",
    "சரி. மூன்று கூற்றுகளும் 1919 அரசுச் சட்டத்தைத் துல்லியமாகப் பிரதிபலிக்கின்றன.",
    "1919 Act provided for a statutory commission to inquire into its working after 10 years (leading to Simon Commission in 1927).",
    "1919 சட்டம் 10 ஆண்டுகளுக்குப் பின் சட்டப்படி விசாரணை நடத்த ஒரு குழுவை அமைக்க உத்தரவிட்டது (1927 சைமன் குழு).",
    "1919 Act extended separate electorates to Sikhs, Indian Christians, Anglo-Indians, and Europeans.",
    "1919 சட்டம் சீக்கியர்கள், இந்தியக் கிறிஸ்தவர்கள், ஆங்கிலோ-இந்தியர்கள், ஐரோப்பியர்களுக்குத் தனித் தொகுதிகளை விரிவுபடுத்தியது.",
    "Analyze", 75, ["Polity", "Historical Background", "Government of India Act 1919", "Three Statement"]
))

# HB_SB_025
questions.append(make_q(
    "HB_SB_025", "Statement Based",
    "Consider the following statements regarding the Government of India Act of 1935:\n1. It divided legislative powers into Federal List (59 items), Provincial List (54 items), and Concurrent List (36 items), with Residuary powers given to the Viceroy.\n2. It introduced Bicameralism in six out of eleven provinces (Bengal, Bombay, Madras, Bihar, Assam, United Provinces).\n3. It provided for the establishment of a Federal Court (set up in 1937) and Reserve Bank of India (established in 1935).\nWhich of the statements given above are correct?",
    "1935 ஆம் ஆண்டின் இந்திய அரசுச் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது சட்ட அதிகாரங்களை கூட்டாட்சி (59), மாகாண (54), மற்றும் இணைப்பு (36) பட்டியல்களாகப் பிரித்து எஞ்சிய அதிகாரங்களை வைஸ்ராய்க்கு அளித்தது.\n2. இது 11 மாகாணங்களில் 6 மாகாணங்களில் (வங்காளம், பம்பாய், மதராஸ், பீகார், அசாம், ஐக்கிய மாகாணங்கள்) ஈரவை முறையை அறிமுகப்படுத்தியது.\n3. இது கூட்டாட்சி நீதிமன்றம் (1937) மற்றும் இந்திய ரிசர்வ் வங்கி (1935) அமைப்பிற்கு வழிவகை செய்தது.\nஎது சரி?",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "D",
    "All three statements are correct. 3-List scheme with Residuary powers to Viceroy, Bicameralism in 6 provinces, Federal Court (1937) and RBI (1935) provisions.",
    "மூன்று கூற்றுகளும் சரியானவை. 3 பட்டியல்கள் திட்டம், 6 மாகாணங்களில் ஈரவை முறை, மற்றும் கூட்டாட்சி நீதிமன்றம் (1937) & ரிசர்வ் வங்கி (1935).",
    "Incorrect. Statement 3 is also correct.",
    "தவறு. கூற்று 3-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Correct. All three statements accurately reflect the GOI Act 1935.",
    "சரி. மூன்று கூற்றுகளும் 1935 அரசுச் சட்டத்தைத் துல்லியமாகப் பிரதிபலிக்கின்றன.",
    "The 1935 Act abolished provincial dyarchy and established full Provincial Autonomy.",
    "1935 சட்டம் மாகாண இரட்டை ஆட்சியை ஒழித்து முழு மாகாண தன்னாட்சியை நிறுவியது.",
    "The 1935 Act extended separate electorates to Depressed Classes (Scheduled Castes), Women, and Labour.",
    "1935 சட்டம் தாழ்த்தப்பட்ட பிரிவினர், பெண்கள், தொழிலாளர்களுக்குத் தனித் தொகுதிகளை விரிவுபடுத்தியது.",
    "Analyze", 75, ["Polity", "Historical Background", "Government of India Act 1935", "Three Statement"]
))

# Save checkpoint
questions.sort(key=lambda x: x["id"])
with open(target_path, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"Part 3 complete: {len(questions)} questions saved.")
