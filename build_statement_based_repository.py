import json
import sys
from pathlib import Path

target_path = Path(r"c:\Users\Home\Desktop\tnpsc_ai\data\questions\polity\historical_background_statement_based.json")
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
        "topic": "Historical Background",
        "difficulty": "Hard",
        "question_type": "Statement Based",
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

questions = []

# =========================================================
# PART 1: 15 TWO STATEMENT QUESTIONS (HB_SB_001 to HB_SB_015)
# =========================================================

# HB_SB_001
questions.append(make_q(
    "HB_SB_001", "Statement Based",
    "Consider the following statements regarding the Regulating Act of 1773:\n1. It designated the Governor of Bengal as the 'Governor-General of Bengal' and created an Executive Council of four members to assist him.\n2. It prohibited the servants of the East India Company from engaging in any private trade or accepting presents or bribes from the natives.\nWhich of the statements given above is/are correct?",
    "1773 ஆம் ஆண்டின் ஒழுங்குமுறைச் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது வங்காள கவர்னரை 'வங்காள கவர்னர் ஜெனரல்' என உயர்த்தியதுடன் அவருக்கு உதவ நான்கு உறுப்பினர்களைக் கொண்ட நிர்வாகக் குழுவை உருவாக்கியது.\n2. கிழக்கிந்தியக் கம்பெனி ஊழியர்கள் எந்தவொரு தனிப்பட்ட வர்த்தகத்திலும் ஈடுபடுவதையோ அல்லது சுதேசிகளிடமிருந்து பரிசுகள் அல்லது லஞ்சங்களை ஏற்றுக்கொள்வதையோ இது தடை செய்தது.\nஎது சரி?",
    "1 only", "1 மட்டும்",
    "2 only", "2 மட்டும்",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை",
    "C",
    "Both statements are correct. The 1773 Regulating Act created the office of Governor-General of Bengal (Warren Hastings) with a 4-member council and strictly prohibited private trade and gifts to eliminate corruption.",
    "இரண்டு கூற்றுகளும் சரியானவை. 1773 ஒழுங்குமுறைச் சட்டம் 4 உறுப்பினர்கள் கொண்ட நிர்வாகக் குழுவுடன் வங்காள கவர்னர் ஜெனரல் பதவியை உருவாக்கியதுடன் தனிப்பட்ட வர்த்தகம் மற்றும் பரிசுகளைத் தடை செய்தது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Correct. Both Statements 1 and 2 are historically true.",
    "சரி. கூற்றுகள் 1 மற்றும் 2 இரண்டும் உண்மை.",
    "Incorrect. Both statements are correct.",
    "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
    "The Regulating Act 1773 made the Governors of Bombay and Madras Presidencies subordinate to the Governor-General of Bengal in matters of war and peace.",
    "1773 ஒழுங்குமுறைச் சட்டம் போர் மற்றும் அமைதி விவகாரங்களில் பம்பாய், மதராஸ் கவர்னர்களை வங்காள கவர்னர் ஜெனரலுக்குக் கீழ்ப்படிந்தவர்களாக மாற்றியது.",
    "Warren Hastings was the first Governor-General of Bengal (1773-1785).",
    "வாரன் ஹேஸ்டிங்ஸ் வங்காளத்தின் முதல் கவர்னர் ஜெனரல் (1773-1785) ஆவார்.",
    "Analyze", 75, ["Polity", "Historical Background", "Regulating Act 1773", "Two Statement"]
))

# HB_SB_002
questions.append(make_q(
    "HB_SB_002", "Statement Based",
    "Consider the following statements regarding Pitt's India Act of 1784:\n1. It created a Board of Control to manage political affairs while leaving commercial operations to the Court of Directors.\n2. The Act reduced the strength of the Governor-General's Council from four to three members.\nWhich of the statements given above is/are correct?",
    "1784 ஆம் ஆண்டின் பிட் இந்தியச் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது அரசியல் விவகாரங்களை நிர்வகிக்க ஒரு கட்டுப்பாட்டு வாரியத்தை உருவாக்கியது, ஆனால் வர்த்தகப் பணிகளை இயக்குநர்கள் அவையிடம் விட்டது.\n2. இச்சட்டம் கவர்னர் ஜெனரல் கவுன்சிலின் உறுப்பினர்களின் எண்ணிக்கையை நான்கிலிருந்து மூன்றாகக் குறைத்தது.\nஎது சரி?",
    "1 only", "1 மட்டும்",
    "2 only", "2 மட்டும்",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை",
    "C",
    "Both statements are correct. Pitt's India Act 1784 established Double Government by creating Board of Control (6 Privy Councillors) for political affairs, and reduced GG Council membership from 4 to 3 (including Commander-in-Chief).",
    "இரண்டு கூற்றுகளும் சரியானவை. 1784 பிட் இந்தியச் சட்டம் அரசியல் விவகாரங்களுக்கு கட்டுப்பாட்டு வாரியத்தை அமைத்து இரட்டை ஆட்சியை நிறுவியதுடன் GG கவுன்சில் உறுப்பினர்களை 4 லிருந்து 3 ஆகக் குறைத்தது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Correct. Both Statements 1 and 2 are historically true.",
    "சரி. கூற்றுகள் 1 மற்றும் 2 இரண்டும் உண்மை.",
    "Incorrect. Both statements are correct.",
    "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
    "Pitt's India Act 1784 referred to East India Company territories in India as 'British Possessions in India' for the first time.",
    "1784 பிட் இந்தியச் சட்டம் முதன்முறையாக கம்பெனி நிலப்பரப்புகளை 'இந்தியாவில் உள்ள பிரிட்டிஷ் உடமைகள்' என குறிப்பிட்டது.",
    "The Board of Control comprised 6 Privy Councillors, including the Chancellor of the Exchequer and Secretary of State.",
    "கட்டுப்பாட்டு வாரியம் நிதிஅமைச்சர் மற்றும் அரசுச் செயலாளர் உட்பட 6 உறுப்பினர்களைக் கொண்டிருந்தது.",
    "Analyze", 75, ["Polity", "Historical Background", "Pitt's India Act 1784", "Two Statement"]
))

# HB_SB_003
questions.append(make_q(
    "HB_SB_003", "Statement Based",
    "Consider the following statements regarding the Charter Act of 1793:\n1. It extended the trade monopoly of the East India Company in India for a further period of twenty years.\n2. It mandated that the Commander-in-Chief was automatically an ex-officio member of the Governor-General's Council in all circumstances.\nWhich of the statements given above is/are correct?",
    "1793 ஆம் ஆண்டின் சாசனச் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது இந்தியாவில் கிழக்கிந்தியக் கம்பெனியின் வர்த்தக ஏகபோகத்தை மேலும் இருபது ஆண்டுகளுக்கு நீட்டித்தது.\n2. இது அனைத்து சூழ்நிலைகளிலும் தளபதியை (Commander-in-Chief) கவர்னர் ஜெனரல் கவுன்சிலின் இயல்பான உறுப்பினராகத் தானாகவே கட்டாயப்படுத்தியது.\nஎது சரி?",
    "1 only", "1 மட்டும்",
    "2 only", "2 மட்டும்",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை",
    "A",
    "Statement 1 is correct (extended trade monopoly for 20 years). Statement 2 is INCORRECT because the 1793 Act specifically provided that the Commander-in-Chief was NOT to be a member of the Governor-General's Council unless specifically appointed by the Court of Directors.",
    "கூற்று 1 சரி (வர்த்தக ஏகபோகம் 20 ஆண்டுகள் நீட்டிப்பு). கூற்று 2 தவறு, ஏனெனில் 1793 சட்டம் இயக்குநர்கள் அவையால் சிறப்பாக நியமிக்கப்பட்டால் ஒழிய தளபதி தானாக கவுன்சில் உறுப்பினராக முடியாது எனத் தெளிவுபடுத்தியது.",
    "Correct. Statement 1 is true; Statement 2 is false.",
    "சரி. கூற்று 1 சரி; கூற்று 2 தவறானது.",
    "Incorrect. Statement 2 is false.",
    "தவறு. கூற்று 2 தவறானது.",
    "Incorrect. Statement 2 is false.",
    "தவறு. கூற்று 2 தவறானது.",
    "Incorrect. Statement 1 is correct.",
    "தவறு. கூற்று 1 சரியானது.",
    "TNPSC Trap: 1793 Act laid down that Commander-in-Chief was NOT an ex-officio member of GG Council unless explicitly appointed.",
    "TNPSC பொறி: 1793 சட்டம் தளபதி தானாகவே கவுன்சில் உறுப்பினராக இருக்க முடியாது எனத் தெளிவுபடுத்தியது.",
    "1793 Act required salaries of Board of Control staff to be charged on Indian revenues.",
    "1793 சட்டம் கட்டுப்பாட்டு வாரிய ஊழியர்களின் சம்பளத்தை இந்திய வருவாயிலிருந்து வழங்க உத்தரவிட்டது.",
    "Analyze", 75, ["Polity", "Historical Background", "Charter Act 1793", "Two Statement"]
))

# HB_SB_004
questions.append(make_q(
    "HB_SB_004", "Statement Based",
    "Consider the following statements regarding the Charter Act of 1813:\n1. It completely abolished all commercial trade activities of the East India Company in India without exception.\n2. It explicitly asserted the sovereignty of the British Crown over the Company's territories in India.\nWhich of the statements given above is/are correct?",
    "1813 ஆம் ஆண்டின் சாசனச் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது எந்தவிலக்கும் இன்றி இந்தியாவில் கிழக்கிந்தியக் கம்பெனியின் அனைத்து வர்த்தக நடவடிக்கைகளையும் முழுமையாக ஒழித்தது.\n2. இது கம்பெனியின் இந்திய நிலப்பரப்புகள் மீது பிரிட்டிஷ் முடிஅரசின் இறையாண்மையை வெளிப்படையாக அறிவித்தது.\nஎது சரி?",
    "1 only", "1 மட்டும்",
    "2 only", "2 மட்டும்",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை",
    "B",
    "Statement 1 is INCORRECT because 1813 Act retained Company's trade monopoly in Tea and Trade with China (these were abolished in 1833). Statement 2 is correct (asserted Crown sovereignty).",
    "கூற்று 1 தவறு, ஏனெனில் 1813 சட்டம் தேயிலை மற்றும் சீனா வர்த்தக ஏகபோகத்தைத் தக்கவைத்தது (அவை 1833 இல் ஒழிக்கப்பட்டன). கூற்று 2 சரி (முடிஅரசு இறையாண்மை அறிவிப்பு).",
    "Incorrect. Statement 1 is false.",
    "தவறு. கூற்று 1 தவறானது.",
    "Correct. Statement 2 is true; Statement 1 is false.",
    "சரி. கூற்று 2 சரி; கூற்று 1 தவறானது.",
    "Incorrect. Statement 1 is false.",
    "தவறு. கூற்று 1 தவறானது.",
    "Incorrect. Statement 2 is correct.",
    "தவறு. கூற்று 2 சரியானது.",
    "1813 Act allowed Christian Missionaries to come to India and allocated Rs 1 Lakh annually for education.",
    "1813 சட்டம் கிறிஸ்தவ மிஷனரிகளை அனுமதித்ததுடன் கல்விக்காக ஆண்டிற்கு ரூ. 1 லட்சம் ஒதுக்கியது.",
    "Charter Act 1813 was passed during the Governor-Generalship of Lord Minto I / Lord Hastings.",
    "1813 சாசனச் சட்டம் முதலாம் மிண்டோ / ஹேஸ்டிங்ஸ் பிரபு கால கட்டத்தில் நிறைவேற்றப்பட்டது.",
    "Analyze", 75, ["Polity", "Historical Background", "Charter Act 1813", "Two Statement"]
))

# HB_SB_005
questions.append(make_q(
    "HB_SB_005", "Statement Based",
    "Consider the following statements regarding the Charter Act of 1833:\n1. It redesignated the Governor-General of Bengal as the 'Governor-General of India' and vested in him all civil and military powers.\n2. Lord William Bentinck was appointed the first Governor-General of India under this Act.\nWhich of the statements given above is/are correct?",
    "1833 ஆம் ஆண்டின் சாசனச் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது வங்காள கவர்னர் ஜெனரலை 'இந்திய கவர்னர் ஜெனரல்' என மாற்றி அவருக்கு அனைத்து சிவில் மற்றும் இராணுவ அதிகாரங்களையும் வழங்கியது.\n2. இச்சட்டத்தின் கீழ் வில்லியம் பென்டிங்க் பிரபு இந்தியாவின் முதல் கவர்னர் ஜெனரலாக நியமிக்கப்பட்டார்.\nஎது சரி?",
    "1 only", "1 மட்டும்",
    "2 only", "2 மட்டும்",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை",
    "C",
    "Both statements are correct. Charter Act 1833 created Governor-General of India with full civil & military control, making Lord William Bentinck the first Governor-General of India.",
    "இரண்டு கூற்றுகளும் சரியானவை. 1833 சாசனச் சட்டம் அனைத்து சிவில், இராணுவ அதிகாரங்களுடன் இந்திய கவர்னர் ஜெனரல் பதவியை உருவாக்கி வில்லியம் பென்டிங்க் பிரபுவை முதல் கவர்னர் ஜெனரலாக்கியது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Correct. Both Statements 1 and 2 are historically accurate.",
    "சரி. கூற்றுகள் 1 மற்றும் 2 இரண்டும் உண்மை.",
    "Incorrect. Both statements are correct.",
    "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
    "1833 Act created a government having authority over the entire territorial area possessed by the British in India.",
    "1833 சட்டம் பிரிட்டிஷாரால் ஆளப்பட்ட முழு இந்திய நிலப்பரப்பின் மீதும் அதிகாரம் கொண்ட அரசாங்கத்தை உருவாக்கியது.",
    "Charter Act 1833 added Lord Macaulay as the 4th Law Member (without full voting rights initially).",
    "1833 சாசனச் சட்டம் மெக்காலே பிரபுவை 4வது சட்ட உறுப்பினராகச் சேர்த்தது.",
    "Analyze", 75, ["Polity", "Historical Background", "Charter Act 1833", "Two Statement"]
))

# Save checkpoint
with open(target_path, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"Added {len(questions)} Two-Statement questions.")
