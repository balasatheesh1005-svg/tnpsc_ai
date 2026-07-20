import json
import sys
from pathlib import Path

target_path = Path(r"c:\Users\Home\Desktop\tnpsc_ai\data\questions\polity\historical_background_hard.json")
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

# Add HB_H_016
questions.append(make_q(
    "HB_H_016", "Statement Based",
    "Consider the following statements regarding the provisions of the Indian Councils Act of 1861:\n1. It initiated the process of decentralization by restoring legislative powers to Bombay and Madras Presidencies.\n2. It gave statutory recognition to Lord Canning's 'Portfolio System' introduced in 1859.\n3. It empowered the Viceroy to issue ordinances during emergencies without the concurrence of the Legislative Council, valid for six months.\nWhich of the statements given above are correct?",
    "1861 ஆம் ஆண்டின் இந்தியக் கவுன்சில்கள் சட்டத்தின் விதிகள் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது பம்பாய் மற்றும் மதராஸ் மாகாணங்களுக்கு சட்ட அதிகாரங்களை மீட்டு பரவலாக்கல் செயல்முறையைத் தொடங்கியது.\n2. 1859 இல் லார்ட் கேனிங் அறிமுகப்படுத்திய 'துறை ஒதுக்கீடு முறைக்கு' (Portfolio System) இது சட்டப்பூர்வ அங்கீகாரம் அளித்தது.\n3. சட்டமன்ற கவுன்சிலின் ஒப்புதலின்றி அவசரகாலத்தில் 6 மாத காலத்திற்கு செல்லுபடியாகும் அவசரச்சட்டங்களை பிறப்பிக்க இது வைஸ்ராய்க்கு அதிகாரமளித்தது.\nஎது சரி?",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "D",
    "All three statements are correct. Restored legislative power to Bombay/Madras, legalized Canning's Portfolio system (1859), and gave Viceroy Ordinance power (6 months validity).",
    "மூன்று கூற்றுகளும் சரியானவை. பம்பாய்/மதராஸ் சட்ட அதிகாரத்தை மீட்டது, கேனிங்கின் துறை ஒதுக்கீடு முறையை அங்கீகரித்தது, அவசரச்சட்ட அதிகாரமளித்தது.",
    "Incorrect. Statement 3 is also correct.",
    "தவறு. கூற்று 3-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Correct. All three statements accurately reflect the Indian Councils Act 1861.",
    "சரி. மூன்று கூற்றுகளும் 1861 இந்தியக் கவுன்சில்கள் சட்டத்தை துல்லியமாகப் பிரதிபலிக்கின்றன.",
    "1861 Act marked the beginning of representative institutions by associating Indians with law-making (3 Indians nominated in 1862 by Lord Canning).",
    "1861 சட்டம் சட்டமியற்றுவதில் இந்தியர்களைச் சேர்த்ததன் மூலம் பிரதிநிதித்துவ அமைப்புகளின் தொடக்கமாக அமைந்தது.",
    "Raja of Benares, Maharaja of Patiala, and Sir Dinkar Rao were nominated to the Central Legislative Council in 1862.",
    "1862 இல் காசி ராஜா, பாட்டியாலா மகாராஜா, சர் தினகர் ராவ் ஆகியோர் மத்திய கவுன்சிலுக்கு நியமிக்கப்பட்டனர்.",
    "Analyze", 75, ["Polity", "Historical Background", "Indian Councils Act 1861", "Statement Based"]
))

# Add HB_H_017
questions.append(make_q(
    "HB_H_017", "Statement Based",
    "Consider the following statements regarding the Indian Councils Act of 1892:\n1. It introduced the word 'election' explicitly for the first time in the British Indian statutory framework.\n2. It expanded the functions of legislative councils, allowing members to discuss the budget and address questions to the executive.\n3. It permitted council members to ask supplementary questions and vote on budget demands.\nWhich of the statements given above is/are correct?",
    "1892 ஆம் ஆண்டின் இந்தியக் கவுன்சில்கள் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது பிரிட்டிஷ் இந்திய சட்டக் கட்டமைப்பில் 'தேர்தல்' என்ற சொல்லை முதன்முறையாக வெளிப்படையாகப் பயன்படுத்தியது.\n2. இது சட்டமன்ற கவுன்சில்களின் பணிகளை விரிவுபடுத்தி, உறுப்பினர்கள் பட்ஜெட்டை விவாதிக்கவும் நிர்வாகத்திற்கு கேள்விகள் கேட்கவும் அனுமதித்தது.\n3. இது கவுன்சில் உறுப்பினர்களுக்கு துணைக் கேள்விகள் கேட்கவும் பட்ஜெட் மீது வாக்களிக்கவும் அனுமதித்தது.\nஎது சரி?",
    "2 only", "2 மட்டும்",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "A",
    "Statement 1 is INCORRECT (the word 'election' was NOT used in the Act; the process was described as nomination on recommendation). Statement 2 is correct (allowed budget discussion and addressing questions with 6 days notice). Statement 3 is INCORRECT (supplementary questions and budget voting were NOT allowed in 1892; came in 1909/1919).",
    "கூற்று 1 தவறு ('தேர்தல்' என்ற சொல் சட்டத்தில் பயன்படுத்தப்படவில்லை, பரிந்துரை அடிப்படையிலான நியமனம் என்றே விவரிக்கப்பட்டது). கூற்று 2 சரி (பட்ஜெட் விவாதம் & கேள்விகள் அனுமதி). கூற்று 3 தவறு (துணைக் கேள்விகள்/வாக்களிப்பு அனுமதி இல்லை).",
    "Correct. Only Statement 2 is correct.",
    "சரி. கூற்று 2 மட்டுமே சரியானது.",
    "Incorrect. Statement 1 is false because the word 'election' was avoided in the Act text.",
    "தவறு. 'தேர்தல்' என்ற சொல் தவிர்க்கப்பட்டதால் கூற்று 1 தவறானது.",
    "Incorrect. Statement 3 is false.",
    "தவறு. கூற்று 3 தவறானது.",
    "Incorrect. Statements 1 and 3 are false.",
    "தவறு. கூற்றுகள் 1 மற்றும் 3 தவறானவை.",
    "TNPSC Trap: The 1892 Act introduced an indirect element of election via recommendation, but the word 'ELECTION' was carefully avoided in the text.",
    "TNPSC பொறி: 1892 சட்டம் மறைமுகத் தேர்தல் கூறைக் கொண்டு வந்தாலும் 'தேர்தல்' என்ற சொல் சட்டத்தில் தவிர்க்கப்பட்டது.",
    "1892 Act required 6 days prior notice to ask questions on public interest.",
    "1892 சட்டத்தில் பொதுநலக் கேள்விகள் கேட்க 6 நாட்கள் முன்னறிவிப்பு தேவைப்பட்டது.",
    "Analyze", 75, ["Polity", "Historical Background", "Indian Councils Act 1892", "Budget Discussion"]
))

# Add HB_H_018
questions.append(make_q(
    "HB_H_018", "Statement Based",
    "Consider the following statements regarding the Indian Councils Act of 1909:\n1. It retained an official majority in the Central Legislative Council, but allowed non-official majorities in Provincial Legislative Councils.\n2. It empowered members to ask supplementary questions and move resolutions on the budget and matters of general public interest.\n3. Satyendra Prasad Sinha became the first Indian to join the Governor-General's Executive Council as the Law Member.\nWhich of the statements given above are correct?",
    "1909 ஆம் ஆண்டின் இந்தியக் கவுன்சில்கள் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது மத்திய சட்டமன்ற கவுன்சிலில் அதிகாரபூர்வ பெரும்பான்மையைத் தக்கவைத்தது, ஆனால் மாகாண கவுன்சில்களில் அரசுசாரா பெரும்பான்மையை அனுமதித்தது.\n2. இது உறுப்பினர்களுக்கு துணைக் கேள்விகள் கேட்கவும் பட்ஜெட் மற்றும் பொதுநல விவகாரங்கள் மீது தீர்மானங்களை நகர்த்தவும் அதிகாரம் அளித்தது.\n3. சத்யேந்திர பிரசாத் சின்ஹா கவர்னர் ஜெனரலின் நிர்வாகக் குழுவில் சட்ட உறுப்பினராக இணைந்த முதல் இந்தியரானார்.\nஎது சரி?",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "D",
    "All three statements are correct. Official majority retained at Centre, non-official majority allowed in Provinces, supplementary questions/resolutions enabled, and S.P. Sinha appointed as first Indian Law Member in Viceroy Executive Council.",
    "மூன்று கூற்றுகளும் சரியானவை. மத்திய கவுன்சிலில் அதிகாரபூர்வ பெரும்பான்மை, மாகாணங்களில் அரசுசாரா பெரும்பான்மை, துணைக் கேள்விகள்/தீர்மானங்கள் அனுமதி, மற்றும் எஸ்.பி. சின்ஹா சேர்க்கை.",
    "Incorrect. Statement 3 is also correct.",
    "தவறு. கூற்று 3-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Correct. All three statements accurately describe the 1909 Morley-Minto reforms.",
    "சரி. மூன்று கூற்றுகளும் 1909 மோர்லே-மிண்டோ சீர்திருத்தங்களைச் சரியாக விவரிக்கின்றன.",
    "1909 Act increased Central Legislative Council members from 16 to 60.",
    "1909 சட்டம் மத்திய கவுன்சில் உறுப்பினர்களை 16 லிருந்து 60 ஆக உயர்த்தியது.",
    "Lord Minto appointed S.P. Sinha into the Executive Council following 1909 Act.",
    "1909 சட்டத்தைத் தொடர்ந்து லார்ட் மிண்டோ எஸ்.பி. சின்ஹாவை நிர்வாகக் குழுவில் நியமித்தார்.",
    "Analyze", 75, ["Polity", "Historical Background", "Indian Councils Act 1909", "Statement Based"]
))

# Add HB_H_019
questions.append(make_q(
    "HB_H_019", "Statement Based",
    "Consider the following statements regarding the Government of India Act of 1919:\n1. It introduced for the first time Bicameralism and Direct Elections in the Central Legislature of British India.\n2. It provided for the establishment of a Public Service Commission, leading to the setting up of the Central Public Service Commission in 1926.\n3. It mandated that all members of the Governor-General's Executive Council must be Indian nationals.\nWhich of the statements given above is/are correct?",
    "1919 ஆம் ஆண்டின் இந்திய அரசுச் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது பிரிட்டிஷ் இந்தியாவின் மத்திய சட்டமன்றத்தில் முதன்முறையாக ஈரவை முறை மற்றும் நேரடித் தேர்தல்களை அறிமுகப்படுத்தியது.\n2. இது ஒரு பொதுச் சேவை ஆணையத்தை நிறுவ வழிவகை செய்து, 1926 இல் மத்திய பொதுச் சேவை ஆணையம் அமையக் காரணமானது.\n3. கவர்னர் ஜெனரலின் நிர்வாகக் குழுவின் அனைத்து உறுப்பினர்களும் இந்திய குடிமக்களாக இருக்க வேண்டும் என்று இது கட்டாயப்படுத்தியது.\nஎது சரி?",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "A",
    "Statement 1 is correct (introduced Bicameralism - Council of State & Legislative Assembly - and direct elections). Statement 2 is correct (provided for Public Service Commission, set up in 1926 under Lee Commission). Statement 3 is INCORRECT (required 3 out of 6 members to be Indian, NOT all members).",
    "கூற்று 1 சரி (ஈரவை முறை & நேரடித் தேர்தல்). கூற்று 2 சரி (1926 இல் மத்திய PSC அமைப்பு). கூற்று 3 தவறு (6 இல் 3 உறுப்பினர்கள் மட்டுமே இந்தியர்கள், அனைவரும் அல்ல).",
    "Correct. Statements 1 and 2 are correct; Statement 3 is false.",
    "சரி. கூற்றுகள் 1 மற்றும் 2 சரி; கூற்று 3 தவறானது.",
    "Incorrect. Statement 3 is false.",
    "தவறு. கூற்று 3 தவறானது.",
    "Incorrect. Statement 3 is false.",
    "தவறு. கூற்று 3 தவறானது.",
    "Incorrect. Statement 3 is false.",
    "தவறு. கூற்று 3 தவறானது.",
    "TNPSC Trap: 1919 Act required 3 of 6 members of GG Executive Council (other than Commander-in-Chief) to be Indian.",
    "TNPSC பொறி: 1919 சட்டம் GG நிர்வாகக் குழுவின் 6 உறுப்பினர்களில் 3 பேர் இந்தியர்களாக இருக்க உத்தரவிட்டது.",
    "1919 Act created the office of High Commissioner for India in London.",
    "1919 சட்டம் லண்டனில் இந்திய உயர் ஆணையர் அலுவலகத்தை உருவாக்கியது.",
    "Analyze", 75, ["Polity", "Historical Background", "Government of India Act 1919", "Bicameralism"]
))

# Add HB_H_020
questions.append(make_q(
    "HB_H_020", "Statement Based",
    "Consider the following statements regarding the institutional innovations under the Government of India Act of 1935:\n1. It introduced Bicameralism in six out of eleven provinces: Bengal, Bombay, Madras, Bihar, Assam, and United Provinces.\n2. It established a Federal Court which began functioning in 1937 with Sir Maurice Gwyer as its Chief Justice.\n3. It provided for the establishment of the Reserve Bank of India to control the currency and credit of the country.\nWhich of the statements given above are correct?",
    "1935 ஆம் ஆண்டின் இந்திய அரசுச் சட்டத்தின் கீழ் ஏற்பட்ட நிறுவன மாற்றங்கள் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது 11 மாகாணங்களில் 6 மாகாணங்களில் (வங்காளம், பம்பாய், மதராஸ், பீகார், அசாம், ஐக்கிய மாகாணங்கள்) ஈரவை முறையை அறிமுகப்படுத்தியது.\n2. இது சர் மோரிஸ் குவையரை தலைமை நீதிபதியாகக் கொண்டு 1937 இல் செயல்படத் தொடங்கிய கூட்டாட்சி நீதிமன்றத்தை நிறுவியது.\n3. நாட்டின் நாணயம் மற்றும் கடனைக் கட்டுப்படுத்த இந்திய ரிசர்வ் வங்கியை நிறுவ இது வழிவகை செய்தது.\nஎது சரி?",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "D",
    "All three statements are correct. Bicameralism in 6 provinces (Bengal, Bombay, Madras, Bihar, Assam, UP), Federal Court in 1937 with Sir Maurice Gwyer, and establishment of RBI in April 1935.",
    "மூன்று கூற்றுகளும் சரியானவை. 6 மாகாணங்களில் ஈரவை முறை, 1937 இல் மோரிஸ் குவையருடன் கூட்டாட்சி நீதிமன்றம், மற்றும் 1935 இல் ரிசர்வ் வங்கி அமைவு.",
    "Incorrect. Statement 3 is also correct.",
    "தவறு. கூற்று 3-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Correct. All three statements are historically accurate.",
    "சரி. மூன்று கூற்றுகளும் வரலாற்று ரீதியாகச் சரியானவை.",
    "1935 Act also provided for Federal Public Service Commission, Provincial Public Service Commission, and Joint Public Service Commission.",
    "1935 சட்டம் கூட்டாட்சி, மாகாண மற்றும் கூட்டு பொதுச் சேவை ஆணையங்களை நிறுவ வழிவகுத்தது.",
    "Residuary legislative powers under 1935 Act were assigned to the Governor-General.",
    "1935 சட்டத்தின் கீழ் எஞ்சிய சட்ட அதிகாரங்கள் கவர்னர் ஜெனரலிடம் வழங்கப்பட்டன.",
    "Analyze", 75, ["Polity", "Historical Background", "Government of India Act 1935", "Institutions Arc"]
))

# Sort all 50 questions by ID
questions.sort(key=lambda x: x["id"])

# Save to file
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
