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

# =========================================================
# 20 FOUR STATEMENT QUESTIONS (HB_SB_031 to HB_SB_050)
# =========================================================

# HB_SB_031
questions.append(make_q(
    "HB_SB_031", "Statement Based",
    "Consider the following statements interlinking Company Rule enactments (1773 to 1813):\n1. The Regulating Act 1773 established a Supreme Court of Judicature at Calcutta in 1774.\n2. Pitt's India Act 1784 established Double Government by creating a Board of Control of 6 members.\n3. The Charter Act 1793 mandated that salaries of Board of Control staff be charged on Indian revenues.\n4. The Charter Act 1813 completely ended ALL commercial trade monopoly of the East India Company without exception.\nWhich of the statements given above are correct?",
    "1773 முதல் 1813 வரையிலான கம்பெனி ஆட்சிச் சட்டங்களை இணைக்கும் பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 1773 ஒழுங்குமுறைச் சட்டம் 1774 இல் கொல்கத்தாவில் ஒரு உச்ச நீதிமன்றத்தை நிறுவியது.\n2. 1784 பிட் இந்தியச் சட்டம் 6 உறுப்பினர்கள் கொண்ட கட்டுப்பாட்டு வாரியத்தை அமைத்து இரட்டை ஆட்சியை நிறுவியது.\n3. 1793 சாசனச் சட்டம் கட்டுப்பாட்டு வாரிய ஊழியர்களின் சம்பளத்தை இந்திய வருவாயிலிருந்து வழங்க உத்தரவிட்டது.\n4. 1813 சாசனச் சட்டம் எந்தவிலக்கும் இன்றி கிழக்கிந்தியக் கம்பெனியின் அனைத்து வர்த்தக ஏகபோகத்தையும் முழுமையாக ஒழித்தது.\nஎது சரி?",
    "1, 2 and 4 only", "1, 2 மற்றும் 4 மட்டும்",
    "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டும்",
    "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டும்",
    "1, 2, 3 and 4", "1, 2, 3 மற்றும் 4",
    "B",
    "Statements 1, 2, and 3 are correct. Statement 4 is INCORRECT because the Charter Act 1813 retained the Company's trade monopoly in Tea and Trade with China (all trade monopoly ended only under Charter Act 1833).",
    "கூற்றுகள் 1, 2, 3 சரி. கூற்று 4 தவறு, ஏனெனில் 1813 சட்டம் தேயிலை மற்றும் சீனா வர்த்தக ஏகபோகத்தைத் தக்கவைத்தது (அனைத்து வர்த்தகமும் 1833 இலேயே முடிந்தது).",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "Correct. Statements 1, 2, and 3 are correct; Statement 4 is false.",
    "சரி. கூற்றுகள் 1, 2, 3 சரி; கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "TNPSC Trap: 1813 Act retained Tea & China trade monopoly; 1833 Act ended ALL commercial monopoly.",
    "TNPSC பொறி: 1813 சட்டம் தேயிலை, சீனா வர்த்தகத்தைத் தக்கவைத்தது; 1833 சட்டம் அனைத்தையும் ஒழித்தது.",
    "Paying Board of Control salaries from Indian revenues laid the early foundation for Dadabhai Naoroji's Drain of Wealth theory.",
    "இந்திய வருவாயில் கட்டுப்பாட்டு வாரியத்திற்கு சம்பளம் வழங்கியது செல்வச் சுரண்டல் கோட்பாட்டிற்கு அடித்தளமானது.",
    "Analyze", 75, ["Polity", "Historical Background", "Company Rule Enactments", "Four Statement"]
))

# HB_SB_032
questions.append(make_q(
    "HB_SB_032", "Statement Based",
    "Consider the following statements interlinking major constitutional shifts from 1833 to 1861:\n1. Charter Act 1833 redesignated the Governor-General of Bengal as Governor-General of India.\n2. Charter Act 1853 created a separate 6-member Indian Legislative Council, introducing parliamentary debate procedure.\n3. Government of India Act 1858 abolished the Board of Control and Court of Directors, ending Double Government.\n4. Indian Councils Act 1861 empowered the Viceroy to issue Ordinances valid for one full year during emergencies.\nWhich of the statements given above are correct?",
    "1833 முதல் 1861 வரையிலான முக்கிய அரசியலமைப்பு மாற்றங்களை இணைக்கும் பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 1833 சாசனச் சட்டம் வங்காள கவர்னர் ஜெனரலை இந்திய கவர்னர் ஜெனரலாக மாற்றியது.\n2. 1853 சாசனச் சட்டம் 6 உறுப்பினர்கள் கொண்ட தனி இந்திய சட்டமன்ற கவுன்சிலை உருவாக்கி நாடாளுமன்ற விவாத நடைமுறையை அறிமுகப்படுத்தியது.\n3. 1858 இந்திய அரசுச் சட்டம் கட்டுப்பாட்டு வாரியம் மற்றும் இயக்குநர்கள் அவையைக் கலைத்து இரட்டை ஆட்சியை முடிவுக்குக் கொண்டு வந்தது.\n4. 1861 இந்தியக் கவுன்சில்கள் சட்டம் அவசரகாலத்தில் ஒரு முழு வருடம் செல்லுபடியாகும் அவசரச்சட்டங்களை பிறப்பிக்க வைஸ்ராய்க்கு அதிகாரமளித்தது.\nஎது சரி?",
    "1, 2 and 4 only", "1, 2 மற்றும் 4 மட்டும்",
    "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டும்",
    "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டும்",
    "1, 2, 3 and 4", "1, 2, 3 மற்றும் 4",
    "B",
    "Statements 1, 2, and 3 are correct. Statement 4 is INCORRECT because Viceroy Ordinance validity under 1861 Act was SIX MONTHS, not one year.",
    "கூற்றுகள் 1, 2, 3 சரி. கூற்று 4 தவறு, ஏனெனில் 1861 சட்டப்படி வைஸ்ராய் அவசரச்சட்டம் 6 மாதங்கள் மட்டுமே செல்லுபடியாகும் (1 வருடம் அல்ல).",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "Correct. Statements 1, 2, and 3 are correct; Statement 4 is false.",
    "சரி. கூற்றுகள் 1, 2, 3 சரி; கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "TNPSC Trap: Ordinance validity under 1861 Act was 6 MONTHS (not 1 year).",
    "TNPSC பொறி: 1861 சட்டப்படி வைஸ்ராய் அவசரச்சட்டத்தின் செல்லுபடியாகும் காலம் 6 மாதங்கள் (1 வருடம் அல்ல).",
    "Lord William Bentinck was the first Governor-General of India (1833), and Lord Canning was the first Viceroy (1858).",
    "வில்லியம் பென்டிங்க் பிரபு முதல் இந்திய கவர்னர் ஜெனரலாகவும் (1833), கேனிங் பிரபு முதல் வைஸ்ராயாகவும் (1858) இருந்தனர்.",
    "Analyze", 75, ["Polity", "Historical Background", "Constitutional Shifts 1833 to 1861", "Four Statement"]
))

# HB_SB_033
questions.append(make_q(
    "HB_SB_033", "Statement Based",
    "Consider the following statements interlinking legislative progress from 1892 to 1935:\n1. Indian Councils Act 1892 permitted legislative members to discuss the budget for the first time.\n2. Indian Councils Act 1909 introduced Separate Electorates exclusively for Muslims.\n3. Government of India Act 1919 introduced Dyarchy in 8 British Indian Provinces.\n4. Government of India Act 1935 assigned Residuary legislative powers exclusively to the Federal Parliament.\nWhich of the statements given above are correct?",
    "1892 முதல் 1935 வரையிலான சட்டமன்ற வளர்ச்சியை இணைக்கும் பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 1892 இந்தியக் கவுன்சில்கள் சட்டம் முதன்முறையாக உறுப்பினர்கள் பட்ஜெட்டை விவாதிக்க அனுமதித்தது.\n2. 1909 இந்தியக் கவுன்சில்கள் சட்டம் முஸ்லிம்களுக்கு மட்டுமே பிரத்யேகத் தனித் தொகுதியை அறிமுகப்படுத்தியது.\n3. 1919 இந்திய அரசுச் சட்டம் 8 பிரிட்டிஷ் இந்திய மாகாணங்களில் இரட்டை ஆட்சியை அறிமுகப்படுத்தியது.\n4. 1935 இந்திய அரசுச் சட்டம் எஞ்சிய சட்ட அதிகாரங்களை கூட்டாட்சி பாராளுமன்றத்திற்கு மட்டுமே ஒப்படைத்தது.\nஎது சரி?",
    "1, 2 and 4 only", "1, 2 மற்றும் 4 மட்டும்",
    "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டும்",
    "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டும்",
    "1, 2, 3 and 4", "1, 2, 3 மற்றும் 4",
    "B",
    "Statements 1, 2, and 3 are correct. Statement 4 is INCORRECT because Residuary legislative powers under 1935 Act were assigned to the Governor-General (Viceroy), NOT to the Federal Parliament.",
    "கூற்றுகள் 1, 2, 3 சரி. கூற்று 4 தவறு, ஏனெனில் 1935 சட்டத்தில் எஞ்சிய அதிகாரங்கள் வைஸ்ராயிடம் இருந்தன (கூட்டாட்சி பாராளுமன்றத்திடம் அல்ல).",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "Correct. Statements 1, 2, and 3 are correct; Statement 4 is false.",
    "சரி. கூற்றுகள் 1, 2, 3 சரி; கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "TNPSC Trap: In 1935 Act, Residuary powers = Governor-General. In 1950 Constitution, Residuary powers = Parliament (Article 248).",
    "TNPSC பொறி: 1935 சட்டத்தில் எஞ்சிய அதிகாரங்கள் = கவர்னர் ஜெனரல். 1950 அரசியலமைப்பில் எஞ்சிய அதிகாரங்கள் = பாராளுமன்றம் (பிரிவு 248).",
    "1892 Act allowed budget discussion but prohibited asking supplementary questions.",
    "1892 சட்டம் பட்ஜெட் விவாதத்தை அனுமதித்தது ஆனால் துணைக் கேள்விகளைத் தடுத்தது.",
    "Analyze", 75, ["Polity", "Historical Background", "Legislative Progress 1892 to 1935", "Four Statement"]
))

# HB_SB_034
questions.append(make_q(
    "HB_SB_034", "Statement Based",
    "Consider the following statements regarding representative milestones in British India:\n1. Indian Councils Act 1861 gave statutory recognition to Lord Canning's Portfolio System.\n2. Indian Councils Act 1892 explicitly introduced the word 'ELECTION' for non-official council seats.\n3. Indian Councils Act 1909 granted council members the right to ask supplementary questions and move budget resolutions.\n4. Government of India Act 1919 granted council members the right to vote on demands for grants.\nWhich of the statements given above are correct?",
    "பிரிட்டிஷ் இந்தியாவில் பிரதிநிதித்துவ மைல்கற்கள் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 1861 இந்தியக் கவுன்சில்கள் சட்டம் கேனிங் பிரபுவின் துறை ஒதுக்கீடு முறைக்கு சட்டப்பூர்வ அங்கீகாரம் அளித்தது.\n2. 1892 இந்தியக் கவுன்சில்கள் சட்டம் அரசுசாரா கவுன்சில் இடங்களுக்கு 'தேர்தல்' என்ற சொல்லை வெளிப்படையாக அறிமுகப்படுத்தியது.\n3. 1909 இந்தியக் கவுன்சில்கள் சட்டம் உறுப்பினர்களுக்கு துணைக் கேள்விகள் கேட்கவும் பட்ஜெட் தீர்மானங்கள் கொண்டு வரவும் உரிமை அளித்தது.\n4. 1919 இந்திய அரசுச் சட்டம் உறுப்பினர்களுக்கு மானியக் கோரிக்கைகள் மீது வாக்களிக்கும் உரிமையை வழங்கியது.\nஎது சரி?",
    "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டும்",
    "1, 2 and 4 only", "1, 2 மற்றும் 4 மட்டும்",
    "1, 3 and 4 only", "1, 3 மற்றும் 4 மட்டும்",
    "1, 2, 3 and 4", "1, 2, 3 மற்றும் 4",
    "C",
    "Statements 1, 3, and 4 are correct. Statement 2 is INCORRECT because the word 'election' was carefully avoided in the text of the 1892 Act (described as recommendation).",
    "கூற்றுகள் 1, 3, 4 சரி. கூற்று 2 தவறு, ஏனெனில் 1892 சட்ட உரையில் 'தேர்தல்' என்ற சொல் தவிர்க்கப்பட்டது.",
    "Incorrect. Statement 2 is false.",
    "தவறு. கூற்று 2 தவறானது.",
    "Incorrect. Statement 2 is false.",
    "தவறு. கூற்று 2 தவறானது.",
    "Correct. Statements 1, 3, and 4 are correct; Statement 2 is false.",
    "சரி. கூற்றுகள் 1, 3, 4 சரி; கூற்று 2 தவறானது.",
    "Incorrect. Statement 2 is false.",
    "தவறு. கூற்று 2 தவறானது.",
    "TNPSC Trap: 1892 Act used recommendation for non-official seats, avoiding the word 'ELECTION'.",
    "TNPSC பொறி: 1892 சட்டம் பரிந்துரை முறையைப் பயன்படுத்தியது, ஆனால் 'தேர்தல்' என்ற சொல்லைத் தவிர்த்தது.",
    "1919 Act introduced direct elections in India for the first time.",
    "1919 சட்டம் இந்தியாவில் முதன்முறையாக நேரடித் தேர்தலை அறிமுகப்படுத்தியது.",
    "Analyze", 75, ["Polity", "Historical Background", "Representative Milestones Arc", "Four Statement"]
))

# HB_SB_035
questions.append(make_q(
    "HB_SB_035", "Statement Based",
    "Consider the following statements regarding the progression of Indian executive representation:\n1. The Indian Councils Act 1861 nominated 3 non-official Indians to the Legislative Council in 1862.\n2. The Indian Councils Act 1909 appointed Satyendra Prasad Sinha as the first Indian Law Member in the Viceroy's Executive Council.\n3. The Government of India Act 1919 mandated that 3 out of 6 members of the Viceroy's Executive Council be Indian.\n4. An All-Indian Interim Cabinet headed by Jawaharlal Nehru was formed in September 1946.\nWhich of the statements given above are correct?",
    "நிர்வாகத்தில் இந்தியர் சேர்க்கை வளர்ச்சி பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 1861 கவுன்சில்கள் சட்டம் 1862 இல் 3 அரசுசாரா இந்தியர்களை சட்டமன்ற கவுன்சிலுக்கு நியமித்தது.\n2. 1909 கவுன்சில்கள் சட்டம் சத்யேந்திர பிரசாத் சின்ஹாவை வைஸ்ராய் நிர்வாகக் குழுவின் முதல் இந்திய சட்ட உறுப்பினராக நியமித்தது.\n3. 1919 அரசுச் சட்டம் வைஸ்ராய் நிர்வாகக் குழுவின் 6 உறுப்பினர்களில் 3 பேர் இந்தியர்களாக இருக்க வேண்டும் எனப் பணித்தது.\n4. ஜவஹர்லால் நேரு தலைமையில் செப்டம்பர் 1946 இல் அனைத்து இந்தியர்கள் கொண்ட இடைக்கால அமைச்சரவை அமைக்கப்பட்டது.\nஎது சரி?",
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
    "Lord Canning nominated Raja of Benares, Maharaja of Patiala, and Sir Dinkar Rao in 1862.",
    "1862 இல் கேனிங் பிரபு காசி ராஜா, பாட்டியாலா மகாராஜா, சர் தினகர் ராவ் ஆகியோரை நியமித்தார்.",
    "In 1946 Interim Government, Jawaharlal Nehru held Vice-President of Executive Council & External Affairs portfolio.",
    "1946 இடைக்கால அரசில் ஜவஹர்லால் நேரு நிர்வாகக் குழுவின் துணைத் தலைவராகவும் வெளியுறவுத்துறை அமைச்சராகவும் இருந்தார்.",
    "Analyze", 75, ["Polity", "Historical Background", "Executive Indianization Progression Arc", "Four Statement"]
))

# HB_SB_036
questions.append(make_q(
    "HB_SB_036", "Statement Based",
    "Consider the following statements regarding Civil Services evolution in British India:\n1. Charter Act 1833 attempted to introduce open competition, but it was negated due to opposition from Court of Directors.\n2. Charter Act 1853 successfully introduced open competition for covenanted civil service recruitment.\n3. The Macaulay Committee on Indian Civil Service was appointed in 1854 pursuant to the 1853 Act.\n4. The Lee Commission (1923) recommended establishing a Public Service Commission, leading to Central PSC in 1926.\nWhich of the statements given above are correct?",
    "பிரிட்டிஷ் இந்தியாவில் குடிமைப் பணிகள் வளர்ச்சி பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 1833 சாசனச் சட்டம் திறந்தவெளிப் போட்டியை அறிமுகப்படுத்த முயன்றது, ஆனால் இயக்குநர்கள் அவையின் எதிர்ப்பால் அது நிராகரிக்கப்பட்டது.\n2. 1853 சாசனச் சட்டம் ஒப்பந்த குடிமைப் பணி ஆட்சேர்ப்புக்கு திறந்தவெளிப் போட்டியை வெற்றிகரமாக அறிமுகப்படுத்தியது.\n3. 1853 சட்டத்தைத் தொடர்ந்து 1854 இல் இந்திய குடிமைப் பணிக்கான மெக்காலே குழு அமைக்கப்பட்டது.\n4. லீ ஆணையம் (1923) பொதுச் சேவை ஆணையத்தை நிறுவப் பரிந்துரைத்து 1926 இல் மத்திய PSC அமையக் காரணமானது.\nஎது சரி?",
    "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டும்",
    "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டும்",
    "1, 3 and 4 only", "1, 3 மற்றும் 4 மட்டும்",
    "1, 2, 3 and 4", "1, 2, 3 மற்றும் 4",
    "D",
    "All four statements are correct. 1833 attempt negated -> 1853 open competition introduced -> 1854 Macaulay Comm -> 1923 Lee Comm -> 1926 Central PSC.",
    "நான்கு கூற்றுகளும் சரியானவை. 1833 முயற்சி ரத்து -> 1853 போட்டித் தேர்வு அமல் -> 1854 மெக்காலே குழு -> 1923 லீ ஆணையம் -> 1926 மத்திய PSC.",
    "Incorrect. Statement 4 is also correct.",
    "தவறு. கூற்று 4-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Correct. All four statements accurately describe Civil Services evolution.",
    "சரி. நான்கு கூற்றுகளும் குடிமைப் பணி வளர்ச்சியைத் துல்லியமாக விவரிக்கின்றன.",
    "Satyendranath Tagore was the first Indian to clear ICS exam in 1863.",
    "1863 இல் சத்யேந்திரநாத் தாகூர் ICS தேர்வில் தேர்ச்சியடைந்த முதல் இந்தியர் ஆனார்.",
    "Federal Public Service Commission under 1935 Act became UPSC under 1950 Constitution.",
    "1935 சட்டத்தின் கூட்டாட்சி PSC 1950 அரசியலமைப்பில் UPSC என உருவானது.",
    "Analyze", 75, ["Polity", "Historical Background", "Civil Services Arc", "Four Statement"]
))

# HB_SB_037
questions.append(make_q(
    "HB_SB_037", "Statement Based",
    "Consider the following statements regarding Financial Control progression in British India:\n1. Indian Councils Act 1861 prohibited legislative council members from discussing the annual budget.\n2. Indian Councils Act 1892 permitted budget discussion for the first time with six days prior notice.\n3. Indian Councils Act 1909 permitted members to ask supplementary questions and move budget resolutions.\n4. Government of India Act 1919 introduced voting on demands for grants and separated Provincial Budgets from Central Budget.\nWhich of the statements given above are correct?",
    "பிரிட்டிஷ் இந்தியாவில் நிதி கட்டுப்பாட்டு வளர்ச்சி பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 1861 இந்தியக் கவுன்சில்கள் சட்டம் உறுப்பினர்கள் ஆண்டு பட்ஜெட்டை விவாதிப்பதைத் தடுத்தது.\n2. 1892 இந்தியக் கவுன்சில்கள் சட்டம் முதன்முறையாக ஆறு நாட்கள் முன்னறிவிப்புடன் பட்ஜெட்டை விவாதிக்க அனுமதித்தது.\n3. 1909 இந்தியக் கவுன்சில்கள் சட்டம் உறுப்பினர்களுக்கு துணைக் கேள்விகள் கேட்கவும் பட்ஜெட் தீர்மானங்கள் கொண்டு வரவும் அனுமதித்தது.\n4. 1919 இந்திய அரசுச் சட்டம் மானியக் கோரிக்கை வாக்களிப்பை அறிமுகப்படுத்தி மாகாண பட்ஜெட்டை மத்திய பட்ஜெட்டிலிருந்து பிரித்தது.\nஎது சரி?",
    "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டும்",
    "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டும்",
    "1, 3 and 4 only", "1, 3 மற்றும் 4 மட்டும்",
    "1, 2, 3 and 4", "1, 2, 3 மற்றும் 4",
    "D",
    "All four statements are correct. Financial Control Arc: 1861 (No budget discussion) -> 1892 (Discussion allowed, no voting) -> 1909 (Supplementary Qs & resolutions) -> 1919 (Voting on demands for grants & provincial budget separation).",
    "நான்கு கூற்றுகளும் சரியானவை. நிதி கட்டுப்பாட்டு வளர்ச்சி: 1861 (விவாதம் இல்லை) -> 1892 (விவாதம் மட்டும்) -> 1909 (துணைக் கேள்விகள் & தீர்மானங்கள்) -> 1919 (வாக்களிப்பு & மாகாண பட்ஜெட் பிரிப்பு).",
    "Incorrect. Statement 4 is also correct.",
    "தவறு. கூற்று 4-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Correct. All four statements accurately describe Financial Control progression.",
    "சரி. நான்கு கூற்றுகளும் நிதி கட்டுப்பாட்டு வளர்ச்சியைத் துல்லியமாக விவரிக்கின்றன.",
    "First Indian Budget was presented on February 18, 1860 by James Wilson.",
    "1860 பிப்ரவரி 18 அன்று ஜேம்ஸ் வில்சனால் முதல் இந்திய பட்ஜெட் தாக்கல் செய்யப்பட்டது.",
    "Railway Budget was separated from General Budget in 1924 based on Acworth Committee recommendations.",
    "அக்வொர்த் குழுப் பரிந்துரைப்படி 1924 இல் இரயில்வே பட்ஜெட் பொது பட்ஜெட்டிலிருந்து பிரிக்கப்பட்டது.",
    "Analyze", 75, ["Polity", "Historical Background", "Financial Control Progression Arc", "Four Statement"]
))

# HB_SB_038
questions.append(make_q(
    "HB_SB_038", "Statement Based",
    "Consider the following statements regarding the Judicial System lineage in India:\n1. 1774: Supreme Court of Judicature established at Calcutta under Regulating Act 1773 with Sir Elijah Impey as Chief Justice.\n2. 1861: Indian High Courts Act established High Courts at Calcutta, Bombay, and Madras by merging Supreme Courts and Sadar Adalats.\n3. 1937: Federal Court of India established under Government of India Act 1935 with Sir Maurice Gwyer as Chief Justice.\n4. Jan 28, 1950: Supreme Court of India inaugurated under Article 124, replacing both Federal Court and Privy Council appellate jurisdiction.\nWhich of the statements given above are correct?",
    "இந்தியாவில் நீதித்துறை அமைப்பின் வளர்ச்சி குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 1774: 1773 ஒழுங்குமுறைச் சட்டத்தின் கீழ் சர் எலிஜா இம்பேயைத் தலைமை நீதிபதியாகக் கொண்டு கொல்கத்தா உச்ச நீதிமன்றம் அமைவு.\n2. 1861: உயர் நீதிமன்றங்கள் சட்டம் பழைய நீதிமன்றங்களைக் கலைத்து கொல்கத்தா, பம்பாய், மதராஸ் உயர் நீதிமன்றங்களை உருவாக்கியது.\n3. 1937: 1935 இந்திய அரசுச் சட்டத்தின் கீழ் சர் மோரிஸ் குவையரைத் தலைமை நீதிபதியாகக் கொண்டு இந்திய கூட்டாட்சி நீதிமன்றம் அமைவு.\n4. ஜனவரி 28, 1950: பிரிவு 124 இன் கீழ் இந்திய உச்ச நீதிமன்றம் தொடங்கப்பட்டு கூட்டாட்சி நீதிமன்றம் மற்றும் பிரிவி கவுன்சில் அதிகாரம் இரண்டையும் ஏற்றது.\nஎது சரி?",
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
    "Correct. All four statements accurately describe Judicial System evolution.",
    "சரி. நான்கு கூற்றுகளும் நீதித்துறை அமைப்பின் வளர்ச்சியைத் துல்லியமாக விவரிக்கின்றன.",
    "Abolition of Privy Council Jurisdiction Act was passed in 1949 to transfer all appellate jurisdiction to Federal Court before SC inauguration.",
    "1949 இல் பிரிவி கவுன்சில் அதிகார வரம்பு ஒழிப்புச் சட்டம் நிறைவேற்றப்பட்டு கூட்டாட்சி நீதிமன்றத்திற்கு மேல்முறையீடுகள் மாற்றப்பட்டன.",
    "H.J. Kania was the first Chief Justice of independent India's Supreme Court in 1950.",
    "எச்.ஜே. கானியா 1950 இல் சுதந்திர இந்தியாவின் உச்ச நீதிமன்றத்தின் முதல் தலைமை நீதிபதியாக இருந்தார்.",
    "Analyze", 75, ["Polity", "Historical Background", "Judicial System Lineage Arc", "Four Statement"]
))

# HB_SB_039
questions.append(make_q(
    "HB_SB_039", "Statement Based",
    "Consider the following statements regarding the Government of India Act of 1935:\n1. Section 93 empowered the Provincial Governor to assume full provincial powers during breakdown of constitutional machinery.\n2. Sections 42 and 43 empowered the Governor-General to issue Ordinances during legislative recess and emergencies.\n3. It divided legislative subjects into Federal List (59), Provincial List (54), and Concurrent List (36).\n4. Joining the All-India Federation proposed under the Act was mandatory for all Indian Princely States.\nWhich of the statements given above are correct?",
    "1935 இந்திய அரசுச் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. பிரிவு 93 அரசியலமைப்பு இயந்திரம் முறிந்தால் மாகாண கவர்னரே முழு மாகாண அதிகாரங்களையும் ஏற்க வழிவகை செய்தது.\n2. பிரிவுகள் 42 மற்றும் 43 கவர்னர் ஜெனரலுக்கு அவசரச்சட்டம் பிறப்பிக்கும் அதிகாரத்தை வழங்கின.\n3. இது சட்டத் துறைகளை கூட்டாட்சி (59), மாகாண (54), மற்றும் இணைப்பு (36) பட்டியல்களாகப் பிரித்தது.\n4. இச்சட்டத்தின் கீழ் உத்தேசிக்கப்பட்ட அகில இந்திய கூட்டாட்சியில் இணைவது அனைத்து சுதேச சமஸ்தானங்களுக்கும் கட்டாயமாக்கப்பட்டது.\nஎது சரி?",
    "1, 2 and 4 only", "1, 2 மற்றும் 4 மட்டும்",
    "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டும்",
    "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டும்",
    "1, 2, 3 and 4", "1, 2, 3 மற்றும் 4",
    "B",
    "Statements 1, 2, and 3 are correct. Statement 4 is INCORRECT because joining the proposed All-India Federation was OPTIONAL for Princely States (mandatory only for British Indian Provinces).",
    "கூற்றுகள் 1, 2, 3 சரி. கூற்று 4 தவறு, ஏனெனில் சுதேச சமஸ்தானங்கள் கூட்டாட்சியில் இணைவது விருப்பத்தின் பேரில் அமைந்தது (கட்டாயம் அல்ல).",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "Correct. Statements 1, 2, and 3 are correct; Statement 4 is false.",
    "சரி. கூற்றுகள் 1, 2, 3 சரி; கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "TNPSC Trap: Joining 1935 Federation was OPTIONAL for Princely States, which is why it never materialized.",
    "TNPSC பொறி: 1935 கூட்டாட்சியில் இணைவது சுதேச சமஸ்தானங்களுக்கு விருப்பத்தின் பேரில் அமைந்ததால் அது அமையவே இல்லை.",
    "Section 93 of 1935 Act directly evolved into Article 356 (President's Rule) in the 1950 Constitution.",
    "1935 சட்டத்தின் பிரிவு 93 நேரடியாக 1950 அரசியலமைப்பின் பிரிவு 356 (குடியரசுத் தலைவர் ஆட்சி) ஆக உருவானது.",
    "Analyze", 75, ["Polity", "Historical Background", "Government of India Act 1935 Provisions", "Four Statement"]
))

# HB_SB_040
questions.append(make_q(
    "HB_SB_040", "Statement Based",
    "Consider the following statements regarding the Indian Independence Act of 1947:\n1. It declared India and Pakistan as independent dominions from August 15, 1947.\n2. Section 6 empowered Constituent Assemblies to alter or repeal any Act of British Parliament applying to India.\n3. It proclaimed the lapse of British paramountcy over Indian Princely States and treaty relations with Tribal areas.\n4. It retained the absolute right of the British Governor-General to veto bills passed by Dominion Assemblies without Cabinet advice.\nWhich of the statements given above are correct?",
    "1947 இந்திய சுதந்திரச் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது ஆகஸ்ட் 15, 1947 முதல் இந்தியா மற்றும் பாகிஸ்தானை சுதந்திர டொமினியன்களாக அறிவித்தது.\n2. பிரிவு 6 பிரிட்டிஷ் பாராளுமன்ற சட்டங்களை மாற்ற அல்லது ரத்து செய்ய அரசியலமைப்பு சபைகளுக்கு அதிகாரமளித்தது.\n3. இது சுதேச சமஸ்தானங்கள் மீதான பிரிட்டிஷ் மேலாதிக்கம் மற்றும் பழங்குடி பகுதிகள் மீதான ஒப்பந்த உறவுகள் முடிவுக்கு வந்ததாக அறிவித்தது.\n4. இது அமைச்சரவை ஆலோசனையின்றி மசோதாக்களை நிராகரிக்கும் (veto) பிரிட்டிஷ் கவர்னர் ஜெனரலின் முழுமையான உரிமையைத் தக்கவைத்தது.\nஎது சரி?",
    "1, 2 and 4 only", "1, 2 மற்றும் 4 மட்டும்",
    "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டும்",
    "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டும்",
    "1, 2, 3 and 4", "1, 2, 3 மற்றும் 4",
    "B",
    "Statements 1, 2, and 3 are correct. Statement 4 is INCORRECT because the 1947 Act STRIPPED the Governor-General of arbitrary veto powers, converting him into a constitutional nominal head bound by Dominion cabinet advice.",
    "கூற்றுகள் 1, 2, 3 சரி. கூற்று 4 தவறு, ஏனெனில் 1947 சுதந்திரச் சட்டம் கவர்னர் ஜெனரலின் தன்னிச்சையான நிராகரிப்பு அதிகாரங்களை நீக்கி அவரை அமைச்சரவைக்குக் கட்டுப்பட்ட பெயரளவு தலைவராக்கியது.",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "Correct. Statements 1, 2, and 3 are correct; Statement 4 is false.",
    "சரி. கூற்றுகள் 1, 2, 3 சரி; கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "TNPSC Trap: 1947 Act stripped Governor-General's discretionary veto powers and made him bound by Dominion Council of Ministers.",
    "TNPSC பொறி: 1947 சட்டம் கவர்னர் ஜெனரலின் தன்னிச்சை அதிகாரங்களை நீக்கி அவரை அமைச்சரவைக்குக் கட்டுப்பட்டவராக்கியது.",
    "Indian Independence Act received Royal Assent on July 18, 1947.",
    "இந்திய சுதந்திரச் சட்டம் 1947 ஜூலை 18 அன்று மன்னரின் ஒப்புதலைப் பெற்றது.",
    "Analyze", 75, ["Polity", "Historical Background", "Indian Independence Act 1947 Provisions", "Four Statement"]
))

# HB_SB_041
questions.append(make_q(
    "HB_SB_041", "Statement Based",
    "Consider the following statements regarding the 1773 Regulating Act and 1781 Amending Act:\n1. The Regulating Act 1773 established an Executive Council of 4 members to assist GG of Bengal, with decisions taken by majority vote.\n2. The Supreme Court at Calcutta (1774) possessed jurisdiction over all native Indian inhabitants across Bengal, Bihar, and Orissa in personal law matters.\n3. The Amending Act 1781 exempted the Governor-General and his council from Supreme Court jurisdiction for official acts done by them.\n4. The Amending Act 1781 required the Supreme Court to administer Hindu Law to Hindus and Mohammedan Law to Muslims.\nWhich of the statements given above are correct?",
    "1773 ஒழுங்குமுறைச் சட்டம் மற்றும் 1781 திருத்தச் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 1773 ஒழுங்குமுறைச் சட்டம் வங்காள கவர்னர் ஜெனரலுக்கு உதவ 4 உறுப்பினர்கள் கொண்ட நிர்வாகக் குழுவை அமைத்தது, முடிவுகள் பெரும்பான்மை வாக்களிப்பால் எடுக்கப்பட்டன.\n2. 1774 கொல்கத்தா உச்ச நீதிமன்றம் தனிநபர் சட்ட விவகாரங்களில் வங்காளம், பீகார், ஒரிசா முழுவதும் உள்ள அனைத்து சுதேசி இந்தியர்கள் மீதும் அதிகார வரம்பைக் கொண்டிருந்தது.\n3. 1781 திருத்தச் சட்டம் கவர்னர் ஜெனரல் மற்றும் அவரது கவுன்சிலை அவர்களின் அதிகாரப்பூர்வ பணிகளுக்காக உச்ச நீதிமன்ற அதிகார வரம்பிலிருந்து விலக்கியது.\n4. 1781 திருத்தச் சட்டம் உச்ச நீதிமன்றம் இந்துக்களுக்கு இந்து சட்டத்தையும் முஸ்லிம்களுக்கு இசுலாமிய சட்டத்தையும் வழங்க வேண்டும் எனக் கட்டாயப்படுத்தியது.\nஎது சரி?",
    "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டும்",
    "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டும்",
    "1, 3 and 4 only", "1, 3 மற்றும் 4 மட்டும்",
    "1, 2, 3 and 4", "1, 2, 3 மற்றும் 4",
    "C",
    "Statements 1, 3, and 4 are correct. Statement 2 is INCORRECT because Supreme Court jurisdiction over native Indians was restricted to Calcutta inhabitants (or EIC employees), NOT all natives across Bengal, Bihar, Orissa.",
    "கூற்றுகள் 1, 3, 4 சரி. கூற்று 2 தவறு, ஏனெனில் உச்ச நீதிமன்ற அதிகார வரம்பு கொல்கத்தா வாசிகளுக்கு மட்டுமே இருந்தது (முழு வங்காள சுதேசிகளுக்கும் அல்ல).",
    "Incorrect. Statement 2 is false.",
    "தவறு. கூற்று 2 தவறானது.",
    "Incorrect. Statement 2 is false.",
    "தவறு. கூற்று 2 தவறானது.",
    "Correct. Statements 1, 3, and 4 are correct; Statement 2 is false.",
    "சரி. கூற்றுகள் 1, 3, 4 சரி; கூற்று 2 தவறானது.",
    "Incorrect. Statement 2 is false.",
    "தவறு. கூற்று 2 தவறானது.",
    "TNPSC Trap: Supreme Court (1774) had jurisdiction over Calcutta inhabitants, NOT all native Indians across Bengal, Bihar, Orissa.",
    "TNPSC பொறி: 1774 உச்ச நீதிமன்ற அதிகார வரம்பு கொல்கத்தா வாசிகளுக்கு மட்டுமே இருந்தது, முழு வங்காள இந்தியர்களுக்கும் அல்ல.",
    "Sir Elijah Impey was the first Chief Justice of Calcutta Supreme Court.",
    "கொல்கத்தா உச்ச நீதிமன்றத்தின் முதல் தலைமை நீதிபதி சர் எலிஜா இம்பே ஆவார்.",
    "Analyze", 75, ["Polity", "Historical Background", "1773 and 1781 Acts Deep Analysis", "Four Statement"]
))

# HB_SB_042
questions.append(make_q(
    "HB_SB_042", "Statement Based",
    "Consider the following statements regarding Pitt's India Act 1784 and Charter Act 1793:\n1. Pitt's India Act 1784 created a Board of Control of 6 members to superintend political and civil affairs.\n2. Pitt's India Act 1784 reduced Governor-General's Council membership from four to three members.\n3. Charter Act 1793 extended East India Company's trade monopoly in India for a further period of 20 years.\n4. Charter Act 1793 mandated that the Commander-in-Chief was automatically an ex-officio member of GG Council in all circumstances.\nWhich of the statements given above are correct?",
    "1784 பிட் இந்தியச் சட்டம் மற்றும் 1793 சாசனச் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 1784 பிட் சட்டம் அரசியல், சிவில் விவகாரங்களைக் கண்காணிக்க 6 உறுப்பினர்கள் கொண்ட கட்டுப்பாட்டு வாரியத்தை உருவாக்கியது.\n2. 1784 பிட் சட்டம் கவர்னர் ஜெனரல் கவுன்சில் உறுப்பினர்களின் எண்ணிக்கையை 4 லிருந்து 3 ஆகக் குறைத்தது.\n3. 1793 சாசனச் சட்டம் கிழக்கிந்தியக் கம்பெனியின் வர்த்தக ஏகபோகத்தை மேலும் 20 ஆண்டுகளுக்கு நீட்டித்தது.\n4. 1793 சாசனச் சட்டம் அனைத்து சூழ்நிலைகளிலும் தளபதியை (Commander-in-Chief) கவர்னர் ஜெனரல் கவுன்சிலின் இயல்பான உறுப்பினராகத் தானாகவே கட்டாயப்படுத்தியது.\nஎது சரி?",
    "1, 2 and 4 only", "1, 2 மற்றும் 4 மட்டும்",
    "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டும்",
    "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டும்",
    "1, 2, 3 and 4", "1, 2, 3 மற்றும் 4",
    "B",
    "Statements 1, 2, and 3 are correct. Statement 4 is INCORRECT because Charter Act 1793 explicitly provided that the Commander-in-Chief was NOT to be an ex-officio member of GG Council unless specifically appointed by Court of Directors.",
    "கூற்றுகள் 1, 2, 3 சரி. கூற்று 4 தவறு, ஏனெனில் 1793 சட்டம் இயக்குநர்கள் அவையால் சிறப்பாக நியமிக்கப்பட்டால் ஒழிய தளபதி தானாக கவுன்சில் உறுப்பினராக முடியாது எனக் கூறியது.",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "Correct. Statements 1, 2, and 3 are correct; Statement 4 is false.",
    "சரி. கூற்றுகள் 1, 2, 3 சரி; கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "TNPSC Trap: 1793 Act explicitly barred Commander-in-Chief from being ex-officio member of GG Council unless specifically nominated.",
    "TNPSC பொறி: 1793 சட்டம் தளபதி தானாகவே கவுன்சில் உறுப்பினராக இருப்பதைத் தடுத்தது.",
    "Pitt's India Act 1784 used the term 'British possessions in India' for the first time.",
    "1784 பிட் இந்தியச் சட்டம் முதன்முறையாக 'இந்தியாவில் உள்ள பிரிட்டிஷ் உடமைகள்' என்ற சொல்லைப் பயன்படுத்தியது.",
    "Analyze", 75, ["Polity", "Historical Background", "1784 and 1793 Acts Deep Analysis", "Four Statement"]
))

# HB_SB_043
questions.append(make_q(
    "HB_SB_043", "Statement Based",
    "Consider the following statements regarding Charter Act 1813 and Charter Act 1833:\n1. Charter Act 1813 allocated Rs 1 Lakh per year for the promotion of literature and education in India.\n2. Charter Act 1813 permitted Christian missionaries to enter India to promote moral and religious enlightenment.\n3. Charter Act 1833 ended all commercial trading activities of the East India Company, converting it into an administrative body.\n4. Section 87 of Charter Act 1833 mandated 100% reservation for native Indians in all senior civil posts.\nWhich of the statements given above are correct?",
    "1813 மற்றும் 1833 சாசனச் சட்டங்கள் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 1813 சாசனச் சட்டம் இந்தியாவில் கல்வி மற்றும் இலக்கிய மேம்பாட்டிற்காக ஆண்டுக்கு ரூ. 1 லட்சம் ஒதுக்கியது.\n2. 1813 சாசனச் சட்டம் கிறிஸ்தவ மிஷனரிகள் இந்தியாவிற்குள் நுழைய அனுமதித்தது.\n3. 1833 சாசனச் சட்டம் கம்பெனியின் அனைத்து வர்த்தக நடவடிக்கைகளையும் முடித்து அதைத் தூய நிர்வாக அமைப்பாக்கியது.\n4. 1833 சாசனச் சட்டத்தின் பிரிவு 87 அனைத்து உயர் சிவில் பதவிகளிலும் இந்தியர்களுக்கு 100% இடஒதுக்கீட்டை கட்டாயப்படுத்தியது.\nஎது சரி?",
    "1, 2 and 4 only", "1, 2 மற்றும் 4 மட்டும்",
    "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டும்",
    "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டும்",
    "1, 2, 3 and 4", "1, 2, 3 மற்றும் 4",
    "B",
    "Statements 1, 2, and 3 are correct. Statement 4 is INCORRECT because Section 87 was a NON-DISCRIMINATION provision (no Indian disabled on ground of religion, birth, descent, colour), NOT a 100% reservation mandate.",
    "கூற்றுகள் 1, 2, 3 சரி. கூற்று 4 தவறு, ஏனெனில் பிரிவு 87 என்பது பாகுபாடற்ற விதியாகும் (100% இடஒதுக்கீடு விதி அல்ல).",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "Correct. Statements 1, 2, and 3 are correct; Statement 4 is false.",
    "சரி. கூற்றுகள் 1, 2, 3 சரி; கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "TNPSC Trap: Section 87 of 1833 Act was a non-discrimination clause (precursor to Article 15/16), NOT reservation.",
    "TNPSC பொறி: 1833 சட்டத்தின் பிரிவு 87 என்பது பாகுபாடற்ற விதியாகும் (இடஒதுக்கீடு அல்ல).",
    "Lord William Bentinck was appointed first Governor-General of India under Charter Act 1833.",
    "1833 சாசனச் சட்டப்படி வில்லியம் பென்டிங்க் பிரபு இந்தியாவின் முதல் கவர்னர் ஜெனரலானார்.",
    "Analyze", 75, ["Polity", "Historical Background", "1813 and 1833 Acts Deep Analysis", "Four Statement"]
))

# HB_SB_044
questions.append(make_q(
    "HB_SB_044", "Statement Based",
    "Consider the following statements regarding Charter Act 1853 and Government of India Act 1858:\n1. Charter Act 1853 separated legislative and executive functions of GG Council by creating 6-member Legislative Council.\n2. Charter Act 1853 introduced local representation in Central Legislative Council with 4 members from Madras, Bombay, Bengal, Agra.\n3. GOI Act 1858 abolished Board of Control and Court of Directors, placing India directly under British Crown.\n4. GOI Act 1858 provided that all 15 members of the Council of India be directly elected by native Indian voters.\nWhich of the statements given above are correct?",
    "1853 சாசனச் சட்டம் மற்றும் 1858 இந்திய அரசுச் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 1853 சாசனச் சட்டம் 6 உறுப்பினர்கள் கொண்ட சட்டமன்ற கவுன்சிலை உருவாக்கி சட்டமன்ற/நிர்வாகப் பணிகளைப் பிரித்தது.\n2. 1853 சாசனச் சட்டம் மதராஸ், பம்பாய், வங்காளம், ஆக்ரா உள்ளூர் அரசுகளால் நியமிக்கப்பட்ட 4 உறுப்பினர்களுடன் உள்ளூர் பிரதிநிதித்துவத்தை அறிமுகப்படுத்தியது.\n3. 1858 அரசுச் சட்டம் கட்டுப்பாட்டு வாரியம் மற்றும் இயக்குநர்கள் அவையைக் கலைத்து இந்தியாவை நேரடியாக முடிஅரசின் கீழ் கொண்டு வந்தது.\n4. 1858 அரசுச் சட்டம் 15 உறுப்பினர்கள் கொண்ட இந்திய கவுன்சில் உறுப்பினர்கள் அனைவரும் இந்திய வாக்காளர்களால் நேரடியாகத் தேர்ந்தெடுக்கப்பட வேண்டும் எனப் பணித்தது.\nஎது சரி?",
    "1, 2 and 4 only", "1, 2 மற்றும் 4 மட்டும்",
    "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டும்",
    "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டும்",
    "1, 2, 3 and 4", "1, 2, 3 மற்றும் 4",
    "B",
    "Statements 1, 2, and 3 are correct. Statement 4 is INCORRECT because Council of India members were APPOINTED in London (7 by Crown, 8 by Court of Directors), NOT elected by Indian voters.",
    "கூற்றுகள் 1, 2, 3 சரி. கூற்று 4 தவறு, ஏனெனில் 15 உறுப்பினர்கள் கொண்ட இந்திய கவுன்சில் லண்டனில் நியமிக்கப்பட்டது (இந்திய வாக்காளர்களால் தேர்ந்தெடுக்கப்படவில்லை).",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "Correct. Statements 1, 2, and 3 are correct; Statement 4 is false.",
    "சரி. கூற்றுகள் 1, 2, 3 சரி; கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "TNPSC Trap: Council of India (1858) was an advisory body appointed in London, NOT elected by Indians.",
    "TNPSC பொறி: இந்திய கவுன்சில் (1858) என்பது லண்டனில் நியமிக்கப்பட்ட ஆலோசனைக் குழுவாகும் (தேர்ந்தெடுக்கப்படவில்லை).",
    "Macaulay Committee on Indian Civil Service was appointed in 1854 pursuant to Charter Act 1853.",
    "1853 சாசனச் சட்டத்தைத் தொடர்ந்து 1854 இல் மெக்காலே குழு அமைக்கப்பட்டது.",
    "Analyze", 75, ["Polity", "Historical Background", "1853 and 1858 Acts Deep Analysis", "Four Statement"]
))

# HB_SB_045
questions.append(make_q(
    "HB_SB_045", "Statement Based",
    "Consider the following statements regarding Indian Councils Acts 1861 and 1892:\n1. Indian Councils Act 1861 restored law-making powers to Bombay and Madras Presidencies.\n2. Indian Councils Act 1861 empowered Viceroy to issue Ordinances during emergencies valid for 6 months.\n3. Indian Councils Act 1892 permitted budget discussion for the first time with six days prior notice.\n4. Indian Councils Act 1892 granted council members full rights to vote on demands for grants.\nWhich of the statements given above are correct?",
    "1861 மற்றும் 1892 இந்தியக் கவுன்சில்கள் சட்டங்கள் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 1861 கவுன்சில்கள் சட்டம் பம்பாய், மதராஸ் மாகாணங்களுக்கு சட்ட அதிகாரங்களை மீட்டு வழங்கியது.\n2. 1861 கவுன்சில்கள் சட்டம் அவசரகாலத்தில் 6 மாதங்கள் செல்லுபடியாகும் அவசரச்சட்டங்களை பிறப்பிக்க வைஸ்ராய்க்கு அதிகாரமளித்தது.\n3. 1892 கவுன்சில்கள் சட்டம் முதன்முறையாக ஆறு நாட்கள் முன்னறிவிப்புடன் பட்ஜெட்டை விவாதிக்க அனுமதித்தது.\n4. 1892 கவுன்சில்கள் சட்டம் உறுப்பினர்களுக்கு மானியக் கோரிக்கைகள் மீது முழுமையாக வாக்களிக்கும் உரிமையை வழங்கியது.\nஎது சரி?",
    "1, 2 and 4 only", "1, 2 மற்றும் 4 மட்டும்",
    "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டும்",
    "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டும்",
    "1, 2, 3 and 4", "1, 2, 3 மற்றும் 4",
    "B",
    "Statements 1, 2, and 3 are correct. Statement 4 is INCORRECT because voting on demands for grants was NOT permitted under 1892 Act (introduced under Government of India Act 1919).",
    "கூற்றுகள் 1, 2, 3 சரி. கூற்று 4 தவறு, ஏனெனில் மானியக் கோரிக்கைகள் மீது வாக்களிக்கும் உரிமை 1892 சட்டத்தில் இல்லை (1919 சட்டத்தில்தான் வந்தது).",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "Correct. Statements 1, 2, and 3 are correct; Statement 4 is false.",
    "சரி. கூற்றுகள் 1, 2, 3 சரி; கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "TNPSC Trap: 1892 Act allowed budget DISCUSSION only; 1919 Act introduced VOTING on demands for grants.",
    "TNPSC பொறி: 1892 சட்டம் பட்ஜெட் விவாதத்தை மட்டுமே அனுமதித்தது; 1919 சட்டமே மானியக் கோரிக்கை வாக்களிப்பைக் கொண்டு வந்தது.",
    "1861 Act legalized Lord Canning's Portfolio system introduced in 1859.",
    "1861 சட்டம் 1859 இல் கேனிங் பிரபு கொண்டு வந்த துறை ஒதுக்கீடு முறையை சட்டப்பூர்வமாக்கியது.",
    "Analyze", 75, ["Polity", "Historical Background", "1861 and 1892 Acts Deep Analysis", "Four Statement"]
))

# HB_SB_046
questions.append(make_q(
    "HB_SB_046", "Statement Based",
    "Consider the following statements regarding Indian Councils Act 1909 and Government of India Act 1919:\n1. Indian Councils Act 1909 introduced Separate Electorates exclusively for Muslims.\n2. Indian Councils Act 1909 increased Central Legislative Council members from 16 to 60.\n3. Government of India Act 1919 introduced Bicameralism at the Centre consisting of Council of State and Legislative Assembly.\n4. Government of India Act 1919 introduced Dyarchy at the Central level, dividing central subjects into Reserved and Transferred.\nWhich of the statements given above are correct?",
    "1909 இந்தியக் கவுன்சில்கள் சட்டம் மற்றும் 1919 இந்திய அரசுச் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 1909 கவுன்சில்கள் சட்டம் முஸ்லிம்களுக்கு மட்டுமே பிரத்யேகத் தனித் தொகுதியை அறிமுகப்படுத்தியது.\n2. 1909 கவுன்சில்கள் சட்டம் மத்திய கவுன்சில் உறுப்பினர்களின் எண்ணிக்கையை 16 லிருந்து 60 ஆக உயர்த்தியது.\n3. 1919 அரசுச் சட்டம் மத்தியில் மாநிலங்களவை மற்றும் சட்டமன்றப் பேரவை கொண்ட ஈரவை முறையை அறிமுகப்படுத்தியது.\n4. 1919 அரசுச் சட்டம் மத்திய மட்டத்தில் இரட்டை ஆட்சியை அறிமுகப்படுத்தி மத்தியத் துறைகளை ஒதுக்கப்பட்டவை, மாற்றப்பட்டவை எனப் பிரித்தது.\nஎது சரி?",
    "1, 2 and 4 only", "1, 2 மற்றும் 4 மட்டும்",
    "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டும்",
    "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டும்",
    "1, 2, 3 and 4", "1, 2, 3 மற்றும் 4",
    "B",
    "Statements 1, 2, and 3 are correct. Statement 4 is INCORRECT because GOI Act 1919 introduced Dyarchy in PROVINCES (not Centre). Central Dyarchy was proposed later by 1935 Act.",
    "கூற்றுகள் 1, 2, 3 சரி. கூற்று 4 தவறு, ஏனெனில் 1919 சட்டம் மாகாணங்களில்தான் இரட்டை ஆட்சியை கொண்டு வந்தது (மத்தியில் அல்ல).",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "Correct. Statements 1, 2, and 3 are correct; Statement 4 is false.",
    "சரி. கூற்றுகள் 1, 2, 3 சரி; கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "TNPSC Trap: 1919 Act = Dyarchy in PROVINCES; Central Dyarchy was proposed by 1935 Act.",
    "TNPSC பொறி: 1919 சட்டம் = மாகாணங்களில் இரட்டை ஆட்சி; 1935 சட்டம் = மத்தியில் இரட்டை ஆட்சி உத்தேசம்.",
    "Satyendra Prasad Sinha was appointed as Law Member in Viceroy's Executive Council under 1909 Act.",
    "1909 சட்டப்படி சத்யேந்திர பிரசாத் சின்ஹா வைஸ்ராய் நிர்வாகக் குழுவின் முதல் இந்திய சட்ட உறுப்பினரானார்.",
    "Analyze", 75, ["Polity", "Historical Background", "1909 and 1919 Acts Deep Analysis", "Four Statement"]
))

# HB_SB_047
questions.append(make_q(
    "HB_SB_047", "Statement Based",
    "Consider the following statements regarding Government of India Act 1919 and Government of India Act 1935:\n1. GOI Act 1919 introduced Dyarchy in 8 provinces with Reserved and Transferred subjects.\n2. GOI Act 1919 created the office of High Commissioner for India in London.\n3. GOI Act 1935 abolished Provincial Dyarchy and established full Provincial Autonomy in 1937.\n4. GOI Act 1935 successfully operated Dyarchy at the Central level throughout World War II.\nWhich of the statements given above are correct?",
    "1919 இந்திய அரசுச் சட்டம் மற்றும் 1935 இந்திய அரசுச் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 1919 அரசுச் சட்டம் 8 மாகாணங்களில் ஒதுக்கப்பட்ட மற்றும் மாற்றப்பட்ட துறைகளுடன் இரட்டை ஆட்சியை அறிமுகப்படுத்தியது.\n2. 1919 அரசுச் சட்டம் லண்டனில் இந்திய உயர் ஆணையர் அலுவலகத்தை உருவாக்கியது.\n3. 1935 அரசுச் சட்டம் மாகாண இரட்டை ஆட்சியை ஒழித்து 1937 இல் முழு மாகாண தன்னாட்சியை நிறுவியது.\n4. 1935 அரசுச் சட்டம் இரண்டாம் உலகப் போர் முழுவதும் மத்திய மட்டத்தில் இரட்டை ஆட்சியை வெற்றிகரமாக இயக்கியது.\nஎது சரி?",
    "1, 2 and 4 only", "1, 2 மற்றும் 4 மட்டும்",
    "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டும்",
    "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டும்",
    "1, 2, 3 and 4", "1, 2, 3 மற்றும் 4",
    "B",
    "Statements 1, 2, and 3 are correct. Statement 4 is INCORRECT because Dyarchy at the Centre proposed under 1935 Act NEVER came into operation at all.",
    "கூற்றுகள் 1, 2, 3 சரி. கூற்று 4 தவறு, ஏனெனில் 1935 சட்டத்தில் உத்தேசிக்கப்பட்ட மத்திய இரட்டை ஆட்சி ஒருபோதும் நடைமுறைக்கு வரவே இல்லை.",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "Correct. Statements 1, 2, and 3 are correct; Statement 4 is false.",
    "சரி. கூற்றுகள் 1, 2, 3 சரி; கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "TNPSC Trap: Central Dyarchy proposed under 1935 Act was NEVER brought into force.",
    "TNPSC பொறி: 1935 சட்டத்தின் மத்திய இரட்டை ஆட்சி ஒருபோதும் அமலுக்கு வரவில்லை.",
    "Central Public Service Commission was established in 1926 under 1919 Act (Lee Comm 1923).",
    "1919 சட்டப்படி 1923 லீ ஆணையப் பரிந்துரையால் 1926 இல் மத்திய பொதுச் சேவை ஆணையம் அமைந்தது.",
    "Analyze", 75, ["Polity", "Historical Background", "1919 and 1935 Acts Deep Analysis", "Four Statement"]
))

# HB_SB_048
questions.append(make_q(
    "HB_SB_048", "Statement Based",
    "Consider the following statements regarding the genesis of the Constituent Assembly of India:\n1. 1934: M.N. Roy proposed the idea of a Constituent Assembly for India for the first time.\n2. 1935: Indian National Congress officially demanded a Constituent Assembly to frame the Indian Constitution.\n3. 1940: British Government accepted the demand for a Constituent Assembly in principle in the August Offer.\n4. November 1946: Constituent Assembly of India was constituted under the Cabinet Mission Plan.\nWhich of the statements given above are correct?",
    "இந்திய அரசியலமைப்பு சபையின் தோற்றம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 1934: எம்.என். ராய் முதன்முறையாக இந்தியாவிற்கான அரசியலமைப்பு சபை யோசனையை முன்வைத்தார்.\n2. 1935: இந்திய தேசிய காங்கிரஸ் இந்திய அரசியலமைப்பை உருவாக்க அரசியலமைப்பு சபையை அதிகாரப்பூர்வமாகக் கோரியது.\n3. 1940: பிரிட்டிஷ் அரசு ஆகஸ்ட் சலுகையில் அரசியலமைப்பு சபைக் கோரிக்கையைக் கொள்கையளவில் ஏற்றுக்கொண்டது.\n4. நவம்பர் 1946: கேபினட் மிஷன் திட்டத்தின் கீழ் இந்திய அரசியலமைப்பு சபை அமைக்கப்பட்டது.\nஎது சரி?",
    "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டும்",
    "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டும்",
    "1, 3 and 4 only", "1, 3 மற்றும் 4 மட்டும்",
    "1, 2, 3 and 4", "1, 2, 3 மற்றும் 4",
    "D",
    "All four statements are correct. Traces Assembly genesis: 1934 M.N. Roy proposal -> 1935 INC demand -> 1940 August Offer acceptance in principle -> Nov 1946 Cabinet Mission formation.",
    "நான்கு கூற்றுகளும் சரியானவை. சபை தோற்றப் பாதை: 1934 எம்.என். ராய் யோசனை -> 1935 காங்கிரஸ் கோரிக்கை -> 1940 ஆகஸ்ட் சலுகை ஏற்பு -> நவம்பர் 1946 கேபினட் மிஷன் சபை அமைப்பு.",
    "Incorrect. Statement 4 is also correct.",
    "தவறு. கூற்று 4-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Correct. All four statements accurately describe Constituent Assembly genesis.",
    "சரி. நான்கு கூற்றுகளும் அரசியலமைப்பு சபையின் தோற்றத்தை துல்லியமாக விவரிக்கின்றன.",
    "Cripps Mission of 1942 proposed a fully Indian Constituent Assembly after World War II.",
    "1942 கிரிப்ஸ் தூதுக்குழு போருக்குப் பின் முழுமையான இந்திய அரசியலமைப்பு சபையை உத்தேசித்தது.",
    "Objective Resolution was moved by Jawaharlal Nehru on December 13, 1946.",
    "1946 டிசம்பர் 13 அன்று ஜவஹர்லால் நேரு நோக்குத் தீர்மானத்தை முன்வைத்தார்.",
    "Analyze", 75, ["Polity", "Historical Background", "Constituent Assembly Genesis Arc", "Four Statement"]
))

# HB_SB_049
questions.append(make_q(
    "HB_SB_049", "Statement Based",
    "Consider the following statements regarding direct structural borrowings in the 1950 Indian Constitution from colonial Acts:\n1. Government of India Act 1935 provided the administrative blueprint and nearly 250 Articles for the 1950 Constitution.\n2. Government of India Act 1919 provided the institutional framework for Bicameralism and Direct Elections.\n3. Indian Councils Act 1861 provided the model for Executive Ordinance powers (Art 123/213) and Portfolio System.\n4. Regulating Act 1773 provided the foundational blueprint for Part III Fundamental Rights of the Indian Constitution.\nWhich of the statements given above are correct?",
    "காலனித்துவ சட்டங்களிலிருந்து 1950 இந்திய அரசியலமைப்பு நேரடியாக எடுத்தாண்ட கட்டமைப்பு அம்சங்கள் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 1935 இந்திய அரசுச் சட்டம் 1950 அரசியலமைப்பிற்கு நிர்வாக வரைபடத்தையும் சுமார் 250 விதிகளையும் வழங்கியது.\n2. 1919 இந்திய அரசுச் சட்டம் ஈரவை முறை மற்றும் நேரடித் தேர்தல்களின் நிறுவன கட்டமைப்பை வழங்கியது.\n3. 1861 இந்தியக் கவுன்சில்கள் சட்டம் அவசரச்சட்ட அதிகாரங்கள் (பிரிவு 123/213) மற்றும் துறை ஒதுக்கீடு மாதிரிக்கு அடித்தளமானது.\n4. 1773 ஒழுங்குமுறைச் சட்டம் இந்திய அரசியலமைப்பின் பகுதி III அடிப்படை உரிமைகளுக்கு அடிப்படை வரைபடத்தை வழங்கியது.\nஎது சரி?",
    "1, 2 and 4 only", "1, 2 மற்றும் 4 மட்டும்",
    "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டும்",
    "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டும்",
    "1, 2, 3 and 4", "1, 2, 3 மற்றும் 4",
    "B",
    "Statements 1, 2, and 3 are correct. Statement 4 is INCORRECT because Fundamental Rights (Part III) were borrowed from the US Bill of Rights (US Constitution), NOT from the 1773 Regulating Act.",
    "கூற்றுகள் 1, 2, 3 சரி. கூற்று 4 தவறு, ஏனெனில் அடிப்படை உரிமைகள் (பகுதி III) அமெரிக்க அரசியலமைப்பிலிருந்து பெறப்பட்டன (1773 சட்டத்திலிருந்து அல்ல).",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "Correct. Statements 1, 2, and 3 are correct; Statement 4 is false.",
    "சரி. கூற்றுகள் 1, 2, 3 சரி; கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "TNPSC Borrowings Fact: GOI Act 1935 = Administrative blueprint (~250 articles); US Constitution = Fundamental Rights (Part III).",
    "TNPSC பெறல் செய்தி: 1935 அரசுச் சட்டம் = நிர்வாக வரைபடம் (~250 விதிகள்); அமெரிக்க அரசியலமைப்பு = அடிப்படை உரிமைகள் (பகுதி III).",
    "Dr. B.R. Ambedkar acknowledged that the administrative details of 1935 Act were retained to ensure stability during transition.",
    "அதிகார மாற்றத்தின் போது ஸ்திரத்தன்மையை உறுதி செய்ய 1935 சட்டத்தின் நிர்வாக விவரங்கள் தக்கவைக்கப்பட்டதாக அம்பேத்கர் கூறினார்.",
    "Analyze", 75, ["Polity", "Historical Background", "Constitutional Borrowings Analysis", "Four Statement"]
))

# HB_SB_050
questions.append(make_q(
    "HB_SB_050", "Statement Based",
    "Consider the following statements regarding the lineage of Emergency Provisions in the Indian Constitution:\n1. Section 93 of the Government of India Act 1935 directly evolved into Article 356 (President's Rule / State Emergency).\n2. Section 45 of the Government of India Act 1935 evolved into Article 352 (National Emergency).\n3. Financial Emergency provisions under Article 360 were inspired by executive financial control provisions under the 1935 Act.\n4. The 1773 Regulating Act was the first colonial statute to contain explicit provisions for Financial Emergency.\nWhich of the statements given above are correct?",
    "இந்திய அரசியலமைப்பின் அவசரகால விதிகளின் பரம்பரை வளர்ச்சி பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 1935 இந்திய அரசுச் சட்டத்தின் பிரிவு 93 நேரடியாக பிரிவு 356 (குடியரசுத் தலைவர் ஆட்சி / மாநில அவசரநிலை) ஆக உருவானது.\n2. 1935 இந்திய அரசுச் சட்டத்தின் பிரிவு 45 பிரிவு 352 (தேசிய அவசரநிலை) ஆக உருவானது.\n3. பிரிவு 360 இன் கீழ் நிதி அவசரநிலை விதிகள் 1935 சட்டத்தின் நிர்வாக நிதிக் கட்டுப்பாட்டு விதிகளால் ஈர்க்கப்பட்டன.\n4. 1773 ஒழுங்குமுறைச் சட்டம் நிதி அவசரநிலைக்கான வெளிப்படையான விதிகளைக் கொண்டிருந்த முதல் காலனித்துவ சட்டமாகும்.\nஎது சரி?",
    "1, 2 and 4 only", "1, 2 மற்றும் 4 மட்டும்",
    "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டும்",
    "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டும்",
    "1, 2, 3 and 4", "1, 2, 3 மற்றும் 4",
    "B",
    "Statements 1, 2, and 3 are correct. Statement 4 is INCORRECT because the 1773 Regulating Act contained NO emergency provisions at all; emergency powers evolved under 1935 Act Sections 93 and 45.",
    "கூற்றுகள் 1, 2, 3 சரி. கூற்று 4 தவறு, ஏனெனில் 1773 ஒழுங்குமுறைச் சட்டத்தில் அவசரகால விதிகள் எதுவும் இல்லை.",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "Correct. Statements 1, 2, and 3 are correct; Statement 4 is false.",
    "சரி. கூற்றுகள் 1, 2, 3 சரி; கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.",
    "தவறு. கூற்று 4 தவறானது.",
    "TNPSC Emergency Lineage: Section 93 of 1935 Act = Article 356 (President's Rule).",
    "TNPSC அவசரகால மரபு: 1935 சட்டத்தின் பிரிவு 93 = பிரிவு 356 (குடியரசுத் தலைவர் ஆட்சி).",
    "Part XVIII of the Indian Constitution contains Emergency Provisions (Articles 352 to 360).",
    "இந்திய அரசியலமைப்பின் பகுதி XVIII அவசரகால விதிகளைக் கொண்டுள்ளது (பிரிவுகள் 352 முதல் 360 வரை).",
    "Analyze", 75, ["Polity", "Historical Background", "Emergency Provisions Lineage", "Four Statement"]
))

# Deduplicate by ID
seen = set()
uniq = []
for q in questions:
    if q["id"] not in seen:
        seen.add(q["id"])
        uniq.append(q)

uniq.sort(key=lambda x: x["id"])

print(f"Total Questions in Refined Repository: {len(uniq)}")

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
