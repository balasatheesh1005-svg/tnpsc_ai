import json
from pathlib import Path

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
# 5 COMPARISON QUESTIONS (HB_M_031 to HB_M_035)
# ---------------------------------------------------------

questions.append(make_q(
    "HB_M_031", "Comparison",
    "In comparing the 'Double Government' system of Pitt's India Act 1784 with the administrative structure under the Government of India Act 1858, which key institutional replacement took place?",
    "1784 பிட் இந்தியச் சட்டத்தின் 'இரட்டை நிர்வாக' அமைப்பை 1858 இந்திய அரசுச் சட்டத்தின் நிர்வாகக் கட்டமைப்போடு ஒப்பிடும்போது, எந்த முக்கிய நிறுவன மாற்றீடு நிகழ்ந்தது?",
    "Board of Control and Court of Directors were replaced by the Secretary of State for India and Council of India.",
    "கட்டுப்பாட்டு வாரியமும் இயக்குநர்கள் அவையும் நீக்கப்பட்டு இந்திய அரசுச் செயலாளர் மற்றும் இந்திய கவுன்சில் ஆகியவற்றால் மாற்றீடு செய்யப்பட்டன.",
    "Governor-General of Bengal was replaced by the President of India.",
    "வங்காள கவர்னர் ஜெனரல் இந்தியக் குடியரசுத் தலைவரால் மாற்றப்பட்டார்.",
    "Supreme Court of Calcutta was replaced by the Federal Court.",
    "கொல்கத்தா உச்ச நீதிமன்றம் கூட்டாட்சி நீதிமன்றத்தால் மாற்றப்பட்டது.",
    "Privy Council was replaced by the House of Commons.",
    "பிரிவி கவுன்சில் காமன்ஸ் சபையால் மாற்றப்பட்டது.",
    "A",
    "Under 1784 Act, Double Govt consisted of Court of Directors (Commercial) and Board of Control (Political). The 1858 Act abolished BOTH and created Secretary of State for India (Cabinet Minister) assisted by a 15-member advisory Council of India.",
    "1784 இரட்டை நிர்வாகத்தில் இயக்குநர்கள் அவை மற்றும் கட்டுப்பாட்டு வாரியம் இருந்தன. 1858 சட்டம் இரண்டையும் கலைத்து இந்திய அரசுச் செயலாளர் மற்றும் 15 உறுப்பினர்கள் கொண்ட இந்திய கவுன்சிலை உருவாக்கியது.",
    "Correct. Board of Control and Court of Directors were replaced by Secretary of State and Council of India.",
    "சரி. கட்டுப்பாட்டு வாரியம் மற்றும் இயக்குநர்கள் அவை ஆகியவை அரசுச் செயலாளர் மற்றும் இந்திய கவுன்சிலால் மாற்றப்பட்டன.",
    "Incorrect. GG of Bengal became GG of India in 1833, then Viceroy in 1858.",
    "தவறு. GG of Bengal 1833 இல் GG of India ஆகி 1858 இல் வைஸ்ராய் ஆனார்.",
    "Incorrect. Federal Court was set up in 1937 under 1935 Act.",
    "தவறு. கூட்டாட்சி நீதிமன்றம் 1937 இல் அமைக்கப்பட்டது.",
    "Incorrect. Privy Council remained highest court of appeal until 1949.",
    "தவறு. பிரிவி கவுன்சில் 1949 வரை மேல்முறையீட்டு நீதிமன்றமாக இருந்தது.",
    "Comparative key: 1784 (Board of Control + Court of Directors) -> 1858 (Secretary of State + Council of India).",
    "ஒப்பீட்டுச் சாவி: 1784 (கட்டுப்பாட்டு வாரியம் + இயக்குநர்கள் அவை) -> 1858 (அரசுச் செயலாளர் + இந்திய கவுன்சில்).",
    "The 1858 Act ended Company Rule and established direct Crown Rule in India.",
    "1858 சட்டம் கம்பெனி ஆட்சியை முடித்து இந்தியாவில் பிரிட்டிஷ் மகாராணியின் நேரடி ஆட்சியை நிறுவியது.",
    "Analyze", 60, ["Polity", "Historical Background", "Comparison", "1784 vs 1858"]
))

questions.append(make_q(
    "HB_M_032", "Comparison",
    "Comparing the Charter Act of 1833 and the Charter Act of 1853, what was the major structural evolution in the composition of the Governor-General's Council?",
    "1833 ஆம் ஆண்டின் சாசனச் சட்டத்தையும் 1853 ஆம் ஆண்டின் சாசனச் சட்டத்தையும் ஒப்பிடுகையில், கவர்னர் ஜெனரல் கவுன்சிலின் கட்டமைப்பில் ஏற்பட்ட முக்கிய வளர்ச்சி யாது?",
    "The 1833 Act introduced a fourth member (Law Member) for executive purposes, while the 1853 Act created a separate 6-member Legislative Council distinguishing executive and legislative functions.",
    "1833 சட்டம் நிர்வாக நோக்கங்களுக்காக 4-வது உறுப்பினரை (சட்ட உறுப்பினர்) அறிமுகப்படுத்தியது, 1853 சட்டம் நிர்வாக மற்றும் சட்டமன்றப் பணிகளைப் பிரித்து 6 உறுப்பினர்களைக் கொண்ட தனி சட்டமன்ற கவுன்சிலை உருவாக்கியது.",
    "The 1833 Act introduced separate electorates, while the 1853 Act introduced Dyarchy.",
    "1833 சட்டம் தனித் தொகுதிகளை அறிமுகப்படுத்தியது, 1853 சட்டம் இரட்டை ஆட்சியை அறிமுகப்படுத்தியது.",
    "The 1833 Act created the Board of Control, while the 1853 Act abolished it.",
    "1833 சட்டம் கட்டுப்பாட்டு வாரியத்தை உருவாக்கியது, 1853 சட்டம் அதைக் கலைத்தது.",
    "The 1833 Act introduced provincial autonomy, while the 1853 Act centralized all powers.",
    "1833 சட்டம் மாகாண தன்னாட்சியை அறிமுகப்படுத்தியது, 1853 சட்டம் அனைத்து அதிகாரங்களையும் மையப்படுத்தியது.",
    "A",
    "In 1833, Macaulay joined executive council as 4th member (Law Member). In 1853, legislative function was separated by adding 6 new legislative members (Legislative Councillors), laying the foundation of modern Parliament.",
    "1833 இல் மெக்காலே 4-வது உறுப்பினராகச் சேர்ந்தார். 1853 இல் 6 புதிய சட்டமன்ற உறுப்பினர்கள் சேர்க்கப்பட்டு சட்டமன்றப் பணி நிர்வாகப் பணியிலிருந்து தனியாகப் பிரிக்கப்பட்டது.",
    "Correct. 1833 added Law Member to executive council; 1853 created separate Legislative Council.",
    "சரி. 1833 இல் சட்ட உறுப்பினர் சேர்க்கப்பட்டார்; 1853 இல் தனி சட்டமன்ற கவுன்சில் உருவாக்கப்பட்டது.",
    "Incorrect. Electorates and Dyarchy were 1909 and 1919 developments.",
    "தவறு. தனித் தொகுதிகளும் இரட்டை ஆட்சியும் 1909 மற்றும் 1919 மாற்றங்கள்.",
    "Incorrect. Board of Control was created in 1784 and abolished in 1858.",
    "தவறு. கட்டுப்பாட்டு வாரியம் 1784 இல் உருவாக்கப்பட்டு 1858 இல் கலைக்கப்பட்டது.",
    "Incorrect. Provincial autonomy came under 1935 Act.",
    "தவறு. மாகாண தன்னாட்சி 1935 சட்டத்தில் வந்தது.",
    "Evolution of Council: 1833 (Executive Council + Law Member) -> 1853 (Executive Council + Separate Legislative Council).",
    "கவுன்சில் வளர்ச்சி: 1833 (நிர்வாகக் குழு + சட்ட உறுப்பினர்) -> 1853 (நிர்வாகக் குழு + தனி சட்டமன்ற கவுன்சில்).",
    "Charter Act 1853 opened the Covenanted Civil Services to Indians through open competitive examination.",
    "1853 சாசனச் சட்டம் திறந்தவெளிப் போட்டித் தேர்வு மூலம் இந்தியர்களுக்கு குடிமைப் பணிகளைத் திறந்தது.",
    "Analyze", 60, ["Polity", "Historical Background", "Comparison", "1833 vs 1853"]
))

questions.append(make_q(
    "HB_M_033", "Comparison",
    "Comparing the Indian Councils Act 1909 and the Government of India Act 1919 regarding communal representation, which of the following accurately describes their progression?",
    "வகுப்புவாதப் பிரதிநிதித்துவம் தொடர்பாக 1909 இந்தியக் கவுன்சில்கள் சட்டத்தையும் 1919 இந்திய அரசுச் சட்டத்தையும் ஒப்பிடுகையில், பின்வருவனவற்றில் எது அவற்றின் வளர்ச்சியைச் சரியாக விவரிக்கிறது?",
    "The 1909 Act introduced separate electorates for Muslims only, whereas the 1919 Act extended separate electorates to Sikhs, Indian Christians, Anglo-Indians, and Europeans.",
    "1909 சட்டம் முஸ்லிம்களுக்கு மட்டுமே தனித் தொகுதியை அறிமுகப்படுத்தியது, ஆனால் 1919 சட்டம் சீக்கியர்கள், இந்தியக் கிறிஸ்தவர்கள், ஆங்கிலோ-இந்தியர்கள் மற்றும் ஐரோப்பியர்களுக்கும் தனித் தொகுதியை விரிவுபடுத்தியது.",
    "The 1909 Act introduced separate electorates for Scheduled Castes, while the 1919 Act abolished all separate electorates.",
    "1909 சட்டம் பட்டியல் சாதியினருக்குத் தனித் தொகுதியை அறிமுகப்படுத்தியது, 1919 சட்டம் அனைத்துத் தனித் தொகுதிகளையும் கலைத்தது.",
    "The 1909 Act abolished communal electorates, while the 1919 Act re-introduced them.",
    "1909 சட்டம் வகுப்புவாதத் தொகுதிகளை ஒழித்தது, 1919 சட்டம் அவற்றை மீண்டும் அறிமுகப்படுத்தியது.",
    "Both Acts provided separate electorates exclusively for Princely State rulers.",
    "இரண்டு சட்டங்களும் சுதேச சமஸ்தான ஆட்சியாளர்களுக்கு மட்டுமே தனித் தொகுதிகளை வழங்கின.",
    "A",
    "1909 Morley-Minto Reforms introduced separate electorate for Muslims. 1919 Montagu-Chelmsford Reforms expanded communal electorates to Sikhs, Indian Christians, Anglo-Indians, and Europeans. (1935 expanded it further to Depressed Classes, Women, Labour).",
    "1909 சட்டம் முஸ்லிம்களுக்குத் தனித் தொகுதி அறிமுகப்படுத்தியது. 1919 சட்டம் சீக்கியர்கள், கிறிஸ்தவர்கள், ஆங்கிலோ-இந்தியர்கள், ஐரோப்பியர்களுக்கு விரிவுபடுத்தியது.",
    "Correct. 1909 was Muslims only; 1919 extended to Sikhs, Christians, Anglo-Indians, Europeans.",
    "சரி. 1909 முஸ்லிம்களுக்கு மட்டுமே; 1919 சீக்கியர்கள், கிறிஸ்தவர்கள், ஆங்கிலோ-இந்தியர்கள், ஐரோப்பியர்களுக்கு விரிவுபடுத்தியது.",
    "Incorrect. Depressed Classes were granted separate electorates in 1935 (Communal Award / Poona Pact context).",
    "தவறு. பட்டியல் சாதியினருக்கு 1935 இல் விரிவுபடுத்தப்பட்டது.",
    "Incorrect. Neither Act abolished communal electorates.",
    "தவறு. எந்தச் சட்டமும் வகுப்புவாதத் தொகுதிகளை ஒழிக்கவில்லை.",
    "Incorrect. Communal electorates were for voters in British India, not princely rulers.",
    "தவறு. வகுப்புவாதத் தொகுதிகள் பிரிட்டிஷ் இந்திய வாக்காளர்களுக்கானவை.",
    "Expansion of Communal Electorate: 1909 (Muslims) -> 1919 (Sikhs, Christians, Anglo-Indians, Europeans) -> 1935 (Depressed Classes, Women, Labour).",
    "வகுப்புவாதத் தொகுதி விரிவாக்கம்: 1909 (முஸ்லிம்கள்) -> 1919 (சீக்கியர்கள், கிறிஸ்தவர்கள், ஆங்கிலோ-இந்தியர்கள், ஐரோப்பியர்கள்) -> 1935 (தாழ்த்தப்பட்டோர், பெண்கள், தொழிலாளர்கள்).",
    "Lord Minto was called the 'Father of Communal Electorate' for introducing it in 1909.",
    "1909 இல் அறிமுகப்படுத்தியதால் லார்ட் மிண்டோ 'வகுப்புவாதத் தொகுதிகளின் தந்தை' எனப்பட்டார்.",
    "Analyze", 60, ["Polity", "Historical Background", "Comparison", "1909 vs 1919"]
))

questions.append(make_q(
    "HB_M_034", "Comparison",
    "What was the structural difference between Dyarchy under the Government of India Act 1919 and Dyarchy under the Government of India Act 1935?",
    "1919 இந்திய அரசுச் சட்டத்தின் கீழ் இருந்த இரட்டை ஆட்சிக்கும் 1935 இந்திய அரசுச் சட்டத்தின் கீழ் உத்தேசிக்கப்பட்ட இரட்டை ஆட்சிக்கும் இடையே உள்ள கட்டமைப்பு வேறுபாடு யாது?",
    "The 1919 Act introduced Dyarchy at the Provincial level, whereas the 1935 Act abolished provincial Dyarchy and proposed Dyarchy at the Central level.",
    "1919 சட்டம் மாகாண மட்டத்தில் இரட்டை ஆட்சியை அறிமுகப்படுத்தியது, ஆனால் 1935 சட்டம் மாகாண இரட்டை ஆட்சியை ஒழித்து மத்திய மட்டத்தில் இரட்டை ஆட்சியை உத்தேசித்தது.",
    "The 1919 Act introduced Dyarchy at the Centre, while the 1935 Act introduced Dyarchy in local village panchayats.",
    "1919 சட்டம் மத்தியில் இரட்டை ஆட்சியை அறிமுகப்படுத்தியது, 1935 சட்டம் கிராம பஞ்சாயத்துகளில் இரட்டை ஆட்சியை அறிமுகப்படுத்தியது.",
    "The 1919 Act applied Dyarchy to financial subjects only, while the 1935 Act applied it to defense only.",
    "1919 சட்டம் நிதித் துறைகளுக்கு மட்டுமே இரட்டை ஆட்சியைப் பயன்படுத்தியது, 1935 சட்டம் பாதுகாப்புத் துறைக்கு மட்டுமே பயன்படுத்தியது.",
    "There was no structural difference; Dyarchy functioned identically under both Acts.",
    "எந்தவொரு கட்டமைப்பு வேறுபாடும் இல்லை; இரண்டு சட்டங்களின் கீழும் இரட்டை ஆட்சி ஒரே மாதிரியாகச் செயல்பட்டது.",
    "A",
    "GOI Act 1919 introduced Dyarchy (Reserved & Transferred) in Provinces. GOI Act 1935 abolished Provincial Dyarchy (replacing it with Provincial Autonomy) and proposed Dyarchy at the Centre (Reserved: Defense, External Affairs, etc. vs Transferred), though Central Dyarchy was never implemented.",
    "1919 சட்டம் மாகாணங்களில் இரட்டை ஆட்சியை கொண்டுவந்தது. 1935 சட்டம் மாகாண இரட்டை ஆட்சியை ஒழித்து மாகாண தன்னாட்சியைத் தந்ததுடன், மத்தியில் இரட்டை ஆட்சியை உத்தேசித்தது (நடைமுறைக்கு வரவில்லை).",
    "Correct. 1919 = Provincial Dyarchy; 1935 = Central Dyarchy proposed (Provincial Autonomy implemented).",
    "சரி. 1919 = மாகாண இரட்டை ஆட்சி; 1935 = மத்திய இரட்டை ஆட்சி (மாகாண தன்னாட்சி அமல்).",
    "Incorrect. Dyarchy was not in village panchayats.",
    "தவறு. பஞ்சாயத்துகளில் இரட்டை ஆட்சி வரவில்லை.",
    "Incorrect. Subject division was broader than just finance or defense.",
    "தவறு. துறைப் பிரிவு நிதி அல்லது பாதுகாப்போடு மட்டும் நிற்கவில்லை.",
    "Incorrect. Shift from Provinces (1919) to Centre (1935) was a major structural difference.",
    "தவறு. மாகாணத்திலிருந்து (1919) மத்தியிற்கு (1935) மாறியது முக்கிய வேறுபாடாகும்.",
    "Dyarchy Shift: 1919 Act (Dyarchy in Provinces) -> 1935 Act (Provincial Autonomy + Dyarchy proposed at Centre).",
    "இரட்டை ஆட்சி மாற்றம்: 1919 சட்டம் (மாகாண இரட்டை ஆட்சி) -> 1935 சட்டம் (மாகாண தன்னாட்சி + மத்தியில் இரட்டை ஆட்சி).",
    "Dyarchy is derived from the Greek word 'di-arche' meaning double rule.",
    "டைஆர்க்கி என்ற சொல் 'டை-ஆர்க்கி' என்ற கிரேக்க சொல்லிலிருந்து வந்தது, இதன் பொருள் இரட்டை ஆட்சி என்பதாகும்.",
    "Analyze", 60, ["Polity", "Historical Background", "Comparison", "Dyarchy 1919 vs 1935"]
))

questions.append(make_q(
    "HB_M_035", "Comparison",
    "In comparing the executive designations of 'Governor-General of India' (Charter Act 1833) and 'Viceroy of India' (Government of India Act 1858), which statement correctly highlights their accountability shift?",
    "'இந்திய கவர்னர் ஜெனரல்' (1833 சாசனச் சட்டம்) மற்றும் 'இந்திய வைஸ்ராய்' (1858 இந்திய அரசுச் சட்டம்) ஆகிய நிர்வாகப் பதவிகளை ஒப்பிடுகையில், பின்வரும் கூற்றுகளில் எது அவர்களின் பொறுப்புக்கூறல் மாற்றத்தைச் சரியாகச் சுட்டிக்காட்டுகிறது?",
    "The Governor-General was accountable to the East India Company's Court of Directors and Board of Control, whereas the Viceroy was the direct representative of the British Crown accountable to the Secretary of State for India.",
    "கவர்னர் ஜெனரல் கிழக்கிந்தியக் கம்பெனியின் இயக்குநர்கள் அவை மற்றும் கட்டுப்பாட்டு வாரியத்திற்குப் பொறுப்புடையவராகிருந்தார், ஆனால் வைஸ்ராய் இந்திய அரசுச் செயலாளருக்குப் பொறுப்புடைய பிரிட்டிஷ் மகாராணியின் நேரடிப் பிரதிநிதியாக இருந்தார்.",
    "The Governor-General was accountable to the Indian Legislative Assembly, while the Viceroy was accountable to native rulers.",
    "கவர்னர் ஜெனரல் இந்திய சட்டமன்றப் பேரவைக்குப் பொறுப்புடையவர், வைஸ்ராய் சுதேசி மன்னர்களுக்குப் பொறுப்புடையவர்.",
    "The Governor-General was elected by the people of India, while the Viceroy was nominated by the President.",
    "கவர்னர் ஜெனரல் இந்திய மக்களால் தேர்ந்தெடுக்கப்பட்டார், வைஸ்ராய் குடியரசுத் தலைவரால் நியமிக்கப்பட்டார்.",
    "The two designations represented completely different offices operating simultaneously in Calcutta and Delhi.",
    "இரண்டு பதவிகளும் கொல்கத்தாவிலும் டெல்லியிலும் ஒரே நேரத்தில் செயல்பட்ட முற்றிலும் வேறுபட்ட அலுவலகங்களைக் குறித்தன.",
    "A",
    "Before 1858, GG was an employee/official of EIC answerable to Court of Directors/Board of Control. Under 1858 Act, the same individual held dual title: Viceroy (as direct representative of British Crown) and Governor-General (as head of administration), answerable to Secretary of State.",
    "1858க்கு முன் GG கம்பெனி அதிகாரியாக இயக்குநர்கள் அவை/கட்டுப்பாட்டு வாரியத்திற்குப் பொறுப்பளித்தார். 1858க்குப் பின் அவரே பிரிட்டிஷ் மகாராணியின் நேரடிப் பிரதிநிதியாக 'வைஸ்ராய்' எனப்பட்டார்.",
    "Correct. GG was answerable to EIC Directors/Board; Viceroy was Crown's direct representative.",
    "சரி. GG கம்பெனி இயக்குநர்களுக்குப் பொறுப்பானவர்; வைஸ்ராய் பிரிட்டிஷ் மகாராணியின் நேரடிப் பிரதிநிதி.",
    "Incorrect. Neither was accountable to Indian Assembly or native rulers.",
    "தவறு. இருவரும் இந்திய பேரவைக்கோ மன்னர்களுக்கோ பொறுப்பானவர்கள் அல்ல.",
    "Incorrect. Neither office was elected by Indian people.",
    "தவறு. மக்கள் தேர்தலின் மூலம் நியமிக்கப்படவில்லை.",
    "Incorrect. It was the same person holding the title Governor-General and Viceroy.",
    "தவறு. ஒரே நபரே கவர்னர் ஜெனரல் மற்றும் வைஸ்ராய் என்ற இரு பட்டங்களையும் வகித்தார்.",
    "Lord William Bentinck was first Governor-General of India (1833); Lord Canning was first Viceroy of India (1858).",
    "வில்லியம் பென்டிங்க் பிரபு முதல் இந்திய கவர்னர் ஜெனரல் (1833); கேனிங் பிரபு முதல் இந்திய வைஸ்ராய் (1858).",
    "The designation 'Viceroy' literally means representative of the Monarch (Crown).",
    "'வைஸ்ராய்' என்ற சொல்லின் நேரடிப் பொருள் மன்னரின் (மகாராணியின்) பிரதிநிதி என்பதாகும்.",
    "Analyze", 60, ["Polity", "Historical Background", "Comparison", "Governor-General vs Viceroy"]
))

# ---------------------------------------------------------
# 5 CHRONOLOGY QUESTIONS (HB_M_036 to HB_M_040)
# ---------------------------------------------------------

questions.append(make_q(
    "HB_M_036", "Chronology",
    "Arrange the creation of the following British Administrative Institutions in India in correct chronological order:\n1. Board of Control\n2. Supreme Court of Judicature at Calcutta\n3. Office of Secretary of State for India\n4. High Commissioner for India in London\nSelect the correct answer using the code given below:",
    "இந்தியாவில் பின்வரும் பிரிட்டிஷ் நிர்வாக நிறுவனங்கள் உருவாக்கப்பட்டதை சரியான காலவரிசையில் அமைக்கவும்:\n1. கட்டுப்பாட்டு வாரியம் (Board of Control)\n2. கொல்கத்தா உச்ச நீதிமன்றம் (Supreme Court at Calcutta)\n3. இந்திய அரசுச் செயலாளர் அலுவலகம் (Secretary of State)\n4. லண்டனில் இந்திய உயர் ஆணையர் (High Commissioner)\nசரியான வரிசையைத் தேர்ந்தெடுக்கவும்:",
    "2 - 1 - 3 - 4", "2 - 1 - 3 - 4",
    "1 - 2 - 3 - 4", "1 - 2 - 3 - 4",
    "2 - 3 - 1 - 4", "2 - 3 - 1 - 4",
    "4 - 3 - 2 - 1", "4 - 3 - 2 - 1",
    "A",
    "Chronological order:\n- Supreme Court at Calcutta: 1774 (under Regulating Act 1773)\n- Board of Control: 1784 (under Pitt's India Act 1784)\n- Office of Secretary of State for India: 1858 (under GOI Act 1858)\n- High Commissioner for India in London: 1919 (under GOI Act 1919, created 1920).",
    "சரியான காலவரிசை:\n- கொல்கத்தா உச்ச நீதிமன்றம்: 1774 (1773 சட்டம்)\n- கட்டுப்பாட்டு வாரியம்: 1784 (1784 சட்டம்)\n- இந்திய அரசுச் செயலாளர்: 1858 (1858 சட்டம்)\n- இந்திய உயர் ஆணையர்: 1919 (1919 சட்டம், உருவானது 1920).",
    "Correct. 2 (1774) -> 1 (1784) -> 3 (1858) -> 4 (1919).",
    "சரி. 2 (1774) -> 1 (1784) -> 3 (1858) -> 4 (1919).",
    "Incorrect. Supreme Court (1774) came before Board of Control (1784).",
    "தவறு. உச்ச நீதிமன்றம் (1774) கட்டுப்பாட்டு வாரியத்திற்கு (1784) முன்னே வந்தது.",
    "Incorrect. Board of Control was set up in 1784, before Secretary of State (1858).",
    "தவறு. கட்டுப்பாட்டு வாரியம் 1784 இல் அமைக்கப்பட்டது.",
    "Incorrect. Reverse order.",
    "தவறு. தலைகீழ் வரிசை.",
    "Chronology mnemonic: Supreme Court (1774) -> Board of Control (1784) -> Sec of State (1858) -> High Comm (1920).",
    "காலவரிசை நினைவுக் குறிப்பு: உச்ச நீதிமன்றம் (1774) -> கட்டுப்பாட்டு வாரியம் (1784) -> அரசுச் செயலாளர் (1858) -> உயர் ஆணையர் (1920).",
    "The High Commissioner for India performed trade and commercial duties previously handled by the Secretary of State.",
    "இந்திய உயர் ஆணையர் முன்னதாக அரசுச் செயலாளர் கவனித்து வந்த வணிக மற்றும் வர்த்தகப் பணிகளைச் செய்தார்.",
    "Analyze", 75, ["Polity", "Historical Background", "Chronology", "Administrative Evolution"]
))

questions.append(make_q(
    "HB_M_037", "Chronology",
    "Arrange the following Legislative Council milestones in British India in correct chronological order:\n1. Introduction of indirect election recommendation element in councils\n2. Creation of separate 6-member Indian (Central) Legislative Council\n3. Introduction of separate electorates for Muslims\n4. Introduction of Bicameralism at the Centre\nSelect the correct answer using the code given below:",
    "பிரிட்டிஷ் இந்தியாவில் சட்டமன்ற கவுன்சில் மைல்கற்களை சரியான காலவரிசையில் அமைக்கவும்:\n1. கவுன்சில்களில் மறைமுகத் தேர்தல் பரிந்துரைக் கூறை அறிமுகப்படுத்தியது\n2. 6 உறுப்பினர்கள் கொண்ட மத்திய சட்டமன்ற கவுன்சிலை உருவாக்கியது\n3. முஸ்லிம்களுக்குத் தனித் தொகுதிகளை அறிமுகப்படுத்தியது\n4. மத்திய சட்டமன்றத்தில் ஈரவை முறையை அறிமுகப்படுத்தியது\nசரியான வரிசையைத் தேர்ந்தெடுக்கவும்:",
    "2 - 1 - 3 - 4", "2 - 1 - 3 - 4",
    "1 - 2 - 3 - 4", "1 - 2 - 3 - 4",
    "2 - 3 - 1 - 4", "2 - 3 - 1 - 4",
    "3 - 2 - 1 - 4", "3 - 2 - 1 - 4",
    "A",
    "Chronological order:\n- Creation of separate Legislative Council: 1853 (Charter Act 1853)\n- Indirect election element: 1892 (Indian Councils Act 1892)\n- Separate electorate for Muslims: 1909 (Indian Councils Act 1909)\n- Bicameralism at Centre: 1919 (Government of India Act 1919).",
    "சரியான காலவரிசை:\n- தனி சட்டமன்ற கவுன்சில்: 1853 (1853 சாசனச் சட்டம்)\n- மறைமுகத் தேர்தல் கூறு: 1892 (1892 இந்தியக் கவுன்சில்கள் சட்டம்)\n- முஸ்லிம்களுக்குத் தனித் தொகுதி: 1909 (1909 இந்தியக் கவுன்சில்கள் சட்டம்)\n- மத்திய ஈரவை முறை: 1919 (1919 இந்திய அரசுச் சட்டம்).",
    "Correct. 2 (1853) -> 1 (1892) -> 3 (1909) -> 4 (1919).",
    "சரி. 2 (1853) -> 1 (1892) -> 3 (1909) -> 4 (1919).",
    "Incorrect. Legislative Council creation (1853) preceded indirect election (1892).",
    "தவறு. 1853 சட்டம் 1892 சட்டத்திற்கு முன்னே வந்தது.",
    "Incorrect. Indirect election (1892) came before separate electorates (1909).",
    "தவறு. 1892 சட்டம் 1909 சட்டத்திற்கு முன்னே வந்தது.",
    "Incorrect. Wrong chronology.",
    "தவறு. தவறான காலவரிசை.",
    "Key years: 1853 (Legislative Council) -> 1892 (Indirect recommendation) -> 1909 (Communal Electorate) -> 1919 (Bicameralism).",
    "முக்கிய ஆண்டுகள்: 1853 (சட்டமன்ற கவுன்சில்) -> 1892 (மறைமுகத் தேர்தல்) -> 1909 (வகுப்புவாதத் தொகுதி) -> 1919 (ஈரவை முறை).",
    "The 1919 Act created the Council of State (Upper House) and Central Legislative Assembly (Lower House).",
    "1919 சட்டம் மாநிலங்கள் அவை (மேலவை) மற்றும் மத்திய சட்டமன்றப் பேரவை (கீழவை) ஆகியவற்றை உருவாக்கியது.",
    "Analyze", 75, ["Polity", "Historical Background", "Chronology", "Legislative Evolution"]
))

questions.append(make_q(
    "HB_M_038", "Chronology",
    "Arrange the following British Parliamentary Acts in chronological sequence of their enactment:\n1. Charter Act removing Company's trade monopoly in India except Tea and China\n2. Act establishing Supreme Court at Calcutta\n3. Act transferring Indian governance from Company to Crown\n4. Act introducing Dyarchy in Provinces\n5. Act introducing Provincial Autonomy\nSelect the correct order:",
    "பின்வரும் பிரிட்டிஷ் பாராளுமன்றச் சட்டங்களை அவை இயற்றப்பட்ட காலவரிசையில் அமைக்கவும்:\n1. தேயிலை & சீனா தவிர கம்பெனியின் வர்த்தக ஏகபோகத்தை நீக்கிய சாசனச் சட்டம்\n2. கொல்கத்தா உச்ச நீதிமன்றத்தை நிறுவிய சட்டம்\n3. கம்பெனியிடமிருந்து பிரிட்டிஷ் அரசிற்கு அதிகாரத்தை மாற்றிய சட்டம்\n4. மாகாணங்களில் இரட்டை ஆட்சியை அறிமுகப்படுத்திய சட்டம்\n5. மாகாண தன்னாட்சியை அறிமுகப்படுத்திய சட்டம்\nசரியான வரிசையைத் தேர்ந்தெடுக்கவும்:",
    "2 - 1 - 3 - 4 - 5", "2 - 1 - 3 - 4 - 5",
    "1 - 2 - 3 - 4 - 5", "1 - 2 - 3 - 4 - 5",
    "2 - 3 - 1 - 4 - 5", "2 - 3 - 1 - 4 - 5",
    "2 - 1 - 4 - 3 - 5", "2 - 1 - 4 - 3 - 5",
    "A",
    "Chronological Order:\n2. Regulating Act 1773 (Supreme Court at Calcutta)\n1. Charter Act 1813 (Trade monopoly end except Tea/China)\n3. Government of India Act 1858 (Crown transfer)\n4. Government of India Act 1919 (Provincial Dyarchy)\n5. Government of India Act 1935 (Provincial Autonomy).",
    "சரியான காலவரிசை:\n2. 1773 ஒழுங்குமுறைச் சட்டம் (கொல்கத்தா உச்ச நீதிமன்றம்)\n1. 1813 சாசனச் சட்டம் (தேயிலை/சீனா தவிர ஏகபோக ஒழிப்பு)\n3. 1858 இந்திய அரசுச் சட்டம் (முடிஅரசு மாற்றம்)\n4. 1919 இந்திய அரசுச் சட்டம் (மாகாண இரட்டை ஆட்சி)\n5. 1935 இந்திய அரசுச் சட்டம் (மாகாண தன்னாட்சி).",
    "Correct. Sequence is 1773 -> 1813 -> 1858 -> 1919 -> 1935.",
    "சரி. காலவரிசை: 1773 -> 1813 -> 1858 -> 1919 -> 1935.",
    "Incorrect. Regulating Act (1773) came before Charter Act 1813.",
    "தவறு. 1773 சட்டம் 1813 சட்டத்திற்கு முன்னே வந்தது.",
    "Incorrect. Charter Act 1813 came before GOI Act 1858.",
    "தவறு. 1813 சட்டம் 1858 சட்டத்திற்கு முன்னே வந்தது.",
    "Incorrect. GOI Act 1858 came before GOI Act 1919.",
    "தவறு. 1858 சட்டம் 1919 சட்டத்திற்கு முன்னே வந்தது.",
    "Major landmark years: 1773 -> 1813 -> 1858 -> 1919 -> 1935.",
    "முக்கிய மைல்கல் ஆண்டுகள்: 1773 -> 1813 -> 1858 -> 1919 -> 1935.",
    "The 1935 Act was the longest Act passed by British Parliament until then, containing 321 sections and 10 schedules.",
    "1935 சட்டம் பிரிட்டிஷ் பாராளுமன்றத்தால் நிறைவேற்றப்பட்ட மிக நீண்ட சட்டமாகும் (321 பிரிவுகள், 10 அட்டவணைகள்).",
    "Analyze", 75, ["Polity", "Historical Background", "Chronology", "Acts Sequence"]
))

questions.append(make_q(
    "HB_M_039", "Chronology",
    "Arrange the following key political and constitutional events leading to Indian Independence in correct chronological order:\n1. Appointment of the Simon Commission\n2. Montagu's August Declaration\n3. Cabinet Mission Plan\n4. Enactment of the Government of India Act 1935\n5. Enactment of the Indian Independence Act\nSelect the correct answer using the code given below:",
    "இந்திய சுதந்திரத்திற்கு வழிவகுத்த பின்வரும் முக்கிய அரசியல் மற்றும் அரசியலமைப்பு நிகழ்வுகளைச் சரியான காலவரிசையில் அமைக்கவும்:\n1. சைமன் குழு நியமனம்\n2. மாண்டேகுவின் ஆகஸ்ட் பிரகடனம்\n3. கேபினட் மிஷன் திட்டம்\n4. 1935 இந்திய அரசுச் சட்டம் நிறைவேற்றம்\n5. இந்திய சுதந்திரச் சட்டம் நிறைவேற்றம்\nசரியான வரிசையைத் தேர்ந்தெடுக்கவும்:",
    "2 - 1 - 4 - 3 - 5", "2 - 1 - 4 - 3 - 5",
    "1 - 2 - 4 - 3 - 5", "1 - 2 - 4 - 3 - 5",
    "2 - 4 - 1 - 3 - 5", "2 - 4 - 1 - 3 - 5",
    "2 - 1 - 3 - 4 - 5", "2 - 1 - 3 - 4 - 5",
    "A",
    "Chronological Order:\n2. Montagu's August Declaration (August 1917)\n1. Appointment of Simon Commission (November 1927)\n4. Government of India Act 1935 (August 1935)\n3. Cabinet Mission Plan (March/May 1946)\n5. Indian Independence Act (July 1947).",
    "சரியான காலவரிசை:\n2. மாண்டேகு ஆகஸ்ட் பிரகடனம் (ஆகஸ்ட் 1917)\n1. சைமன் குழு நியமனம் (நவம்பர் 1927)\n4. 1935 இந்திய அரசுச் சட்டம் (ஆகஸ்ட் 1935)\n3. கேபினட் மிஷன் திட்டம் (மார்ச்/மே 1946)\n5. இந்திய சுதந்திரச் சட்டம் (ஜூலை 1947).",
    "Correct. Order: 2 (1917) -> 1 (1927) -> 4 (1935) -> 3 (1946) -> 5 (1947).",
    "சரி. வரிசை: 2 (1917) -> 1 (1927) -> 4 (1935) -> 3 (1946) -> 5 (1947).",
    "Incorrect. Montagu declaration (1917) preceded Simon Commission (1927).",
    "தவறு. 1917 பிரகடனம் 1927 சைமன் குழுவிற்கு முன்னே வந்தது.",
    "Incorrect. Simon Commission (1927) was appointed before 1935 Act was enacted.",
    "தவறு. 1927 சைமன் குழு 1935 சட்டத்திற்கு முன்னரே நியமிக்கப்பட்டது.",
    "Incorrect. Cabinet Mission (1946) came after 1935 Act.",
    "தவறு. கேபினட் மிஷன் (1946) 1935 சட்டத்திற்குப் பிறகே வந்தது.",
    "Timeline check: Montagu (1917) -> Simon Comm (1927) -> GOI Act (1935) -> Cabinet Mission (1946) -> Independence Act (1947).",
    "காலக்கோடு: மாண்டேகு (1917) -> சைமன் குழு (1927) -> 1935 சட்டம் -> கேபினட் மிஷன் (1946) -> சுதந்திரச் சட்டம் (1947).",
    "Simon Commission submitted its report in 1930, which was discussed in three Round Table Conferences (1930-32).",
    "சைமன் குழு 1930 இல் தனது அறிக்கையைச் சமர்ப்பித்தது, அது மூன்று வட்டமேஜை மாநாடுகளில் (1930-32) விவாதிக்கப்பட்டது.",
    "Analyze", 75, ["Polity", "Historical Background", "Chronology", "Constitutional Milestones"]
))

questions.append(make_q(
    "HB_M_040", "Chronology",
    "Arrange the evolution of executive designation titles in British India in chronological order:\n1. Governor-General of India\n2. Governor-General of Bengal\n3. Viceroy and Governor-General of India\n4. Governor-General of Independent Dominion of India\nSelect the correct code:",
    "பிரிட்டிஷ் இந்தியாவில் நிர்வாகத் தலைவர் பதவிகளின் மாற்றத்தை காலவரிசையில் அமைக்கவும்:\n1. இந்திய கவர்னர் ஜெனரல்\n2. வங்காள கவர்னர் ஜெனரல்\n3. இந்திய வைஸ்ராய் மற்றும் கவர்னர் ஜெனரல்\n4. சுதந்திர இந்திய டொமினியனின் கவர்னர் ஜெனரல்\nசரியான வரிசையைத் தேர்ந்தெடுக்கவும்:",
    "2 - 1 - 3 - 4", "2 - 1 - 3 - 4",
    "1 - 2 - 3 - 4", "1 - 2 - 3 - 4",
    "2 - 3 - 1 - 4", "2 - 3 - 1 - 4",
    "3 - 2 - 1 - 4", "3 - 2 - 1 - 4",
    "A",
    "Chronological Order:\n2. Governor-General of Bengal (1773 Regulating Act - Warren Hastings)\n1. Governor-General of India (1833 Charter Act - William Bentinck)\n3. Viceroy and Governor-General of India (1858 GOI Act - Lord Canning)\n4. Governor-General of Dominion of India (1947 Independence Act - Lord Mountbatten / C. Rajagopalachari).",
    "சரியான காலவரிசை:\n2. வங்காள கவர்னர் ஜெனரல் (1773 சட்டம் - வாரன் ஹேஸ்டிங்ஸ்)\n1. இந்திய கவர்னர் ஜெனரல் (1833 சாசனச் சட்டம் - வில்லியம் பென்டிங்க்)\n3. இந்திய வைஸ்ராய் (1858 சட்டம் - கேனிங் பிரபு)\n4. சுதந்திர இந்திய கவர்னர் ஜெனரல் (1947 சட்டம் - மவுண்ட்பேட்டன் / ராஜாஜி).",
    "Correct. Order: 2 (1773) -> 1 (1833) -> 3 (1858) -> 4 (1947).",
    "சரி. வரிசை: 2 (1773) -> 1 (1833) -> 3 (1858) -> 4 (1947).",
    "Incorrect. GG of Bengal came before GG of India.",
    "தவறு. வங்காள GG 1773 இல் வந்தார், இந்திய GG 1833 இல் வந்தார்.",
    "Incorrect. GG of India (1833) preceded Viceroy (1858).",
    "தவறு. இந்திய GG 1833 இல் வந்தார், வைஸ்ராய் 1858 இல் வந்தார்.",
    "Incorrect. Reverse hierarchy.",
    "தவறு. தவறான வரிசை.",
    "Remember first office-holders: Warren Hastings (GG of Bengal 1773), Lord William Bentinck (GG of India 1833), Lord Canning (Viceroy 1858), Lord Mountbatten (Dominion GG 1947).",
    "முதல் பதவி வகித்தவர்களை நினைவில் கொள்க: வாரன் ஹேஸ்டிங்ஸ் (1773), வில்லியம் பென்டிங்க் (1833), லார்ட் கேனிங் (1858), லார்ட் மவுண்ட்பேட்டன் (1947).",
    "The office of Governor-General of India ceased to exist on January 26, 1950 when Dr. Rajendra Prasad was sworn in as President.",
    "1950 ஜனவரி 26 அன்று டாக்டர் ராஜேந்திர பிரசாத் குடியரசுத் தலைவராகப் பொறுப்பேற்ற போது கவர்னர் ஜெனரல் பதவி முடிவுக்கு வந்தது.",
    "Analyze", 75, ["Polity", "Historical Background", "Chronology", "Viceroy Designation"]
))

# ---------------------------------------------------------
# 5 ASSERTION & REASON QUESTIONS (HB_M_041 to HB_M_045)
# ---------------------------------------------------------

questions.append(make_q(
    "HB_M_041", "Assertion & Reason",
    "Assertion (A): The Charter Act of 1833 represents the climax of administrative centralization in British India.\nReason (R): It deprived the Governors of Bombay and Madras of their legislative powers and concentrated all law-making authority exclusively in the Governor-General of India in Council.",
    "கூற்று (A): 1833 ஆம் ஆண்டின் சாசனச் சட்டம் பிரிட்டிஷ் இந்தியாவில் நிர்வாக மத்தியமயமாக்கலின் உச்சகட்டத்தைக் குறிக்கிறது.\nகாரணம் (R): இது பம்பாய் மற்றும் மதராஸ் கவர்னர்களின் சட்டமியற்றும் அதிகாரங்களைப் பறித்து, அனைத்து சட்டமியற்றும் அதிகாரத்தையும் இந்திய கவர்னர் ஜெனரல் கவுன்சிலிடம் மட்டுமே குவித்தது.",
    "Both A and R are true, and R is the correct explanation of A.",
    "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்.",
    "Both A and R are true, but R is NOT the correct explanation of A.",
    "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல.",
    "A is true, but R is false.",
    "A சரி, ஆனால் R தவறு.",
    "A is false, but R is true.",
    "A தவறு, ஆனால் R சரி.",
    "A",
    "Both Assertion and Reason are true and R correctly explains A. The 1833 Act centralized all legislative power by stripping Bombay & Madras of law-making authority and vesting exclusive legislative authority in Governor-General of India (Lord William Bentinck).",
    "கூற்றும் காரணமும் சரி, மேலும் காரணம் கூற்றைச் சரியாக விளக்குகிறது. பம்பாய், மதராஸின் சட்ட அதிகாரங்கள் பறிக்கப்பட்டு இந்திய கவர்னர் ஜெனரலிடம் குவிக்கப்பட்டதால் இது மத்தியமயமாக்கலின் உச்சமானது.",
    "Correct. Centralization reached its climax (A) precisely because legislative power was taken away from provinces and given exclusively to the Centre (R).",
    "சரி. மாகாண சட்ட அதிகாரம் பறிக்கப்பட்டு மையத்தில் குவிக்கப்பட்டதே மத்தியமயமாக்கலின் உச்சத்திற்குக் காரணமாகும்.",
    "Incorrect. R directly explains why A is considered the climax of centralization.",
    "தவறு. R நேரடியாக A-விற்கான விளக்கமாகும்.",
    "Incorrect. Both statements are true.",
    "தவறு. இரண்டு கூற்றுகளும் உண்மையானவை.",
    "Incorrect. A is true.",
    "தவறு. கூற்று A சரியானது.",
    "Check cause-effect link: Strip of provincial legislative power = Peak central lawmaking = Climax of Centralization.",
    "காரண-விளைவுத் தொடர்பைப் பார்க்கவும்: மாகாண சட்ட அதிகாரம் பறிப்பு = மத்திய சட்ட அதிகாரம் = மத்தியமயமாக்கலின் உச்சம்.",
    "Laws enacted under Charter Act 1833 were officially called 'Acts', whereas previous regulations were called 'Regulations'.",
    "1833 சாசனச் சட்டத்தின் கீழ் இயற்றப்பட்ட சட்டங்கள் 'சட்டங்கள்' (Acts) எனப்பட்டன, இதற்கு முந்தையவை 'ஒழுங்குமுறைகள்' எனப்பட்டன.",
    "Analyze", 75, ["Polity", "Historical Background", "Assertion and Reason", "1833 Centralization"]
))

questions.append(make_q(
    "HB_M_042", "Assertion & Reason",
    "Assertion (A): The Indian Councils Act of 1909 (Morley-Minto Reforms) is often criticized by historians for sowing the seeds of partition of India.\nReason (R): It legalized communalism in Indian politics by introducing separate electorates for Muslims.",
    "கூற்று (A): 1909 ஆம் ஆண்டின் இந்தியக் கவுன்சில்கள் சட்டம் (மோர்லே-மிண்டோ சீர்திருத்தங்கள்) இந்தியப் பிரிவினைக்கு வித்திட்டதாக வரலாற்று ஆசிரியர்களால் பெரும்பாலும் விமர்சிக்கப்படுகிறது.\nகாரணம் (R): இது முஸ்லிம்களுக்குத் தனித் தொகுதிகளை அறிமுகப்படுத்தியதன் மூலம் இந்திய அரசியலில் வகுப்புவாதத்தைச் சட்டப்பூர்வமாக்கியது.",
    "Both A and R are true, and R is the correct explanation of A.",
    "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்.",
    "Both A and R are true, but R is NOT the correct explanation of A.",
    "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல.",
    "A is true, but R is false.",
    "A சரி, ஆனால் R தவறு.",
    "A is false, but R is true.",
    "A தவறு, ஆனால் R சரி.",
    "A",
    "Both A and R are true and R explains A. Morley-Minto reforms introduced separate electorates for Muslims, creating institutional communal divisions between Hindus and Muslims, which eventually led to the demand for Pakistan and partition in 1947.",
    "கூற்றும் காரணமும் சரி. 1909 சட்டம் முஸ்லிம்களுக்குத் தனித் தொகுதி வழங்கி வகுப்புவாதத்தை சட்டப்பூர்வமாக்கியதால், அது இந்து-முஸ்லிம் பிரிவினையை உண்டாக்கி 1947 பிரிவினைக்கு அடித்தளமிட்டது.",
    "Correct. Legitimizing separate electorates (R) was the direct mechanism that sowed the seeds of partition (A).",
    "சரி. தனித் தொகுதிகளைச் சட்டப்பூர்வமாக்கியதே (R) பிரிவினைக்கு வித்திட்டதன் (A) நேரடி நுட்பமாகும்.",
    "Incorrect. R is the precise historical cause for A.",
    "தவறு. R என்பது A விற்கான துல்லியமான வரலாற்றுக் காரணமாகும்.",
    "Incorrect. R is true.",
    "தவறு. R சரியானது.",
    "Incorrect. A is true.",
    "தவறு. A சரியானது.",
    "Lord Morley remarked to Minto: 'We are sowing dragon's teeth, and the harvest will be bitter.'",
    "லார்ட் மோர்லே மிண்டோவிடம் கூறினார்: 'நாம் விஷ வித்துக்களை விதைக்கிறோம், இதன் அறுவடை கசப்பானதாக இருக்கும்.'",
    "Lord Minto was designated as the 'Father of Communal Electorate'.",
    "லார்ட் மிண்டோ 'வகுப்புவாதத் தொகுதிகளின் தந்தை' என அழைக்கப்பட்டார்.",
    "Analyze", 75, ["Polity", "Historical Background", "Assertion and Reason", "1909 Partition Seeds"]
))

questions.append(make_q(
    "HB_M_043", "Assertion & Reason",
    "Assertion (A): The system of Dyarchy introduced in the provinces under the Government of India Act 1919 broke down in practice and failed to establish true responsible government.\nReason (R): Essential subjects such as Finance, Law & Order, and Land Revenue were retained in the Reserved list under an executive council answerable to the Governor, leaving Indian ministers with Transferred subjects deprived of financial resources.",
    "கூற்று (A): 1919 ஆம் ஆண்டின் இந்திய அரசுச் சட்டத்தின் கீழ் மாகாணங்களில் அறிமுகப்படுத்தப்பட்ட இரட்டை ஆட்சி முறை நடைமுறையில் முறிந்து உண்மையான பொறுப்புள்ள அரசாங்கத்தை நிறுவத் தவறியது.\nகாரணம் (R): நிதி, சட்டம்-ஒழுங்கு, நில வருவாய் போன்ற அத்தியாவசியத் துறைகள் கவர்னருக்குப் பொறுப்பான நிர்வாகக் குழுவின் கீழ் ஒதுக்கப்பட்ட பட்டியலில் தக்கவைக்கப்பட்டன, இதனால் இந்திய அமைச்சர்கள் நிதி ஆதாரங்கள் இல்லாத மாற்றப்பட்ட துறைகளுடன் விடப்பட்டனர்.",
    "Both A and R are true, and R is the correct explanation of A.",
    "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்.",
    "Both A and R are true, but R is NOT the correct explanation of A.",
    "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல.",
    "A is true, but R is false.",
    "A சரி, ஆனால் R தவறு.",
    "A is false, but R is true.",
    "A தவறு, ஆனால் R சரி.",
    "A",
    "Both A and R are true and R explains A. Dyarchy failed because Indian ministers held departments like Education and Health (Transferred), but lacked finance (Reserved under Governor's executive council), creating friction and making executive responsibility impossible.",
    "கூற்றும் காரணமும் சரி. கல்வி, சுகாதாரம் போன்ற துறைகள் இந்திய அமைச்சர்களிடம் இருந்தபோதிலும், அதற்குத் தேவையான நிதி ஒதுக்கீடு கவர்னரின் ஒதுக்கப்பட்ட கவுன்சிலிடம் இருந்ததால் இரட்டை ஆட்சி தோற்றது.",
    "Correct. Retaining Finance in Reserved subjects without ministerial control (R) caused the failure of Dyarchy (A).",
    "சரி. நிதியை அமைச்சர்களின் கட்டுப்பாடின்றி ஒதுக்கப்பட்ட பட்டியலில் வைத்திருந்ததே (R) இரட்டை ஆட்சித் தோல்விக்குக் (A) காரணமாகும்.",
    "Incorrect. R directly explains why Dyarchy failed.",
    "தவறு. R நேரடியாக இரட்டை ஆட்சி ஏன் தோற்றது என்பதை விளக்குகிறது.",
    "Incorrect. Both statements are true.",
    "தவறு. இரண்டு கூற்றுகளும் உண்மையானவை.",
    "Incorrect. A is true.",
    "தவறு. கூற்று A சரியானது.",
    "Understand the core flaw of 1919 Dyarchy: 'Ministers without purses, and Executive Councillors with purses but without administrative responsibility.'",
    "1919 இரட்டை ஆட்சியின் முக்கியக் குறைபாடு: 'பணப்பை இல்லாத அமைச்சர்கள், நிர்வாகப் பொறுப்பில்லாத பணப்பை கொண்ட கவுன்சிலர்கள்.'",
    "Dyarchy in provinces was abolished by the Government of India Act 1935.",
    "மாகாண இரட்டை ஆட்சி 1935 இந்திய அரசுச் சட்டத்தால் ஒழிக்கப்பட்டது.",
    "Analyze", 75, ["Polity", "Historical Background", "Assertion and Reason", "Dyarchy Failure"]
))

questions.append(make_q(
    "HB_M_044", "Assertion & Reason",
    "Assertion (A): The proposed All-India Federation under the Government of India Act 1935 never materialized.\nReason (R): The joining of Princely States was optional, and the required number of princely rulers refused to sign the Instrument of Accession.",
    "கூற்று (A): 1935 ஆம் ஆண்டின் இந்திய அரசுச் சட்டத்தின் கீழ் உத்தேசிக்கப்பட்ட அகில இந்திய கூட்டாட்சி ஒருபோதும் நடைமுறைக்கு வரவில்லை.\nகாரணம் (R): சுதேச சமஸ்தானங்கள் இணைவது அவர்களின் விருப்பத்தைப் பொறுத்ததாக இருந்தது, மேலும் தேவையான எண்ணிக்கையிலான சுதேச மன்னர்கள் இணைப்புக் சாசனத்தில் கையெழுத்திட மறுத்துவிட்டனர்.",
    "Both A and R are true, and R is the correct explanation of A.",
    "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்.",
    "Both A and R are true, but R is NOT the correct explanation of A.",
    "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல.",
    "A is true, but R is false.",
    "A சரி, ஆனால் R தவறு.",
    "A is false, but R is true.",
    "A தவறு, ஆனால் R சரி.",
    "A",
    "Both A and R are true and R explains A. The 1935 Federation required princely states representing at least half the total princely population to accede. Since rulers refused to surrender their sovereign privileges, the federation never came into force.",
    "கூற்றும் காரணமும் சரி. சுதேச மன்னர்கள் தங்கள் அதிகாரத்தை இழக்க விரும்பாமல் இணைப்புக் சாசனத்தில் கையெழுத்திட மறுத்ததால் அகில இந்திய கூட்டாட்சி திட்டம் ஒருபோதும் நடைமுறைக்கு வரவில்லை.",
    "Correct. Non-accession by Princely States (R) directly prevented the All-India Federation from coming into force (A).",
    "சரி. சுதேச மன்னர்கள் இணைய மறுத்ததே (R) அகில இந்திய கூட்டாட்சி நடைமுறைக்கு வராததற்கான (A) நேரடிக் காரணமாகும்.",
    "Incorrect. R is the exact reason why the federation failed to start.",
    "தவறு. R என்பது கூட்டாட்சி தொடங்காததற்கான சரியான காரணமாகும்.",
    "Incorrect. Both statements are true.",
    "தவறு. இரண்டு கூற்றுகளும் உண்மையானவை.",
    "Incorrect. A is true.",
    "தவறு. A சரியானது.",
    "Notice that British Indian Provinces were MANDATORILY part of 1935 Federation, but Princely States were OPTIONAL.",
    "பிரிட்டிஷ் இந்திய மாகாணங்களுக்குக் கூட்டாட்சி கட்டாயமாக இருந்தது, சுதேச மாநிலங்களுக்கு விருப்பத்தின் அடிப்படையில் இருந்தது.",
    "Though the Federation did not materialise, the Provincial part of 1935 Act came into operation in 1937.",
    "கூட்டாட்சி வராதபோதிலும், 1935 சட்டத்தின் மாகாணப் பகுதி 1937 இல் செயல்பாட்டுக்கு வந்தது.",
    "Analyze", 75, ["Polity", "Historical Background", "Assertion and Reason", "1935 Federation Non-Start"]
))

questions.append(make_q(
    "HB_M_045", "Assertion & Reason",
    "Assertion (A): The Constituent Assembly of India became a fully sovereign body only after the passage of the Indian Independence Act of 1947.\nReason (R): The Indian Independence Act 1947 explicitly abolished British parliamentary authority over India and empowered the Assembly to alter or repeal any Act of British Parliament applying to India.",
    "கூற்று (A): 1947 ஆம் ஆண்டின் இந்திய சுதந்திரச் சட்டம் நிறைவேற்றப்பட்ட பின்னரே இந்திய அரசியலமைப்பு சபை ஒரு முழுமையான சுயாட்சி (இறையாண்மை) அமைப்பாக மாறியது.\nகாரணம் (R): 1947 இந்திய சுதந்திரச் சட்டம் பிரிட்டிஷ் பாராளுமன்றத்திற்கு இந்தியா மீதான அதிகாரத்தை வெளிப்படையாக ஒழித்ததுடன், இந்தியாவில் பொருந்தும் எந்தவொரு பிரிட்டிஷ் சட்டத்தையும் மாற்றுவதற்கோ அல்லது ரத்து செய்வதற்கோ சபைக்கு அதிகாரமளித்தது.",
    "Both A and R are true, and R is the correct explanation of A.",
    "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்.",
    "Both A and R are true, but R is NOT the correct explanation of A.",
    "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல.",
    "A is true, but R is false.",
    "A சரி, ஆனால் R தவறு.",
    "A is false, but R is true.",
    "A தவறு, ஆனால் R சரி.",
    "A",
    "Both A and R are true and R explains A. When formed in Nov 1946 under Cabinet Mission Plan, Constituent Assembly was created by British executive order. Only section 6 of Indian Independence Act 1947 conferred full legislative sovereignty and power to repeal British Acts.",
    "கூற்றும் காரணமும் சரி. 1946 இல் அமைக்கப்பட்டபோது சபை பிரிட்டிஷ் திட்டத்தின் கீழ் இருந்தது. 1947 சுதந்திரச் சட்டத்தின் பிரிவு 6 மட்டுமே சபைக்கு முழு இறையாண்மையையும் பிரிட்டிஷ் சட்டங்களை ரத்து செய்யும் அதிகாரத்தையும் வழங்கியது.",
    "Correct. Section 6 of 1947 Act (R) legally conferred complete sovereignty on the Assembly (A).",
    "சரி. 1947 சட்டத்தின் பிரிவு 6 (R) அரசியலமைப்பு சபைக்கு சட்டப்பூர்வ முழு இறையாண்மையை (A) அளித்தது.",
    "Incorrect. R directly explains how and why Assembly attained sovereignty.",
    "தவறு. R நேரடியாக சபை எவ்வாறு இறையாண்மை பெற்றது என்பதை விளக்குகிறது.",
    "Incorrect. Both statements are true.",
    "தவறு. இரண்டு கூற்றுகளும் உண்மையானவை.",
    "Incorrect. A is true.",
    "தவறு. A சரியானது.",
    "Assembly status transformation: Nov 1946 (Created under Cabinet Mission Plan) -> Aug 15, 1947 (Sovereign body under Independence Act).",
    "சபையின் அந்தஸ்து மாற்றம்: நவம்பர் 1946 (கேபினட் மிஷன் கீழான சபை) -> ஆகஸ்ட் 15, 1947 (சுதந்திரச் சட்டத்தின் கீழான இறையாண்மை சபை).",
    "The Indian Independence Act 1947 repealed the Government of India Act 1935's control mechanisms, while keeping its administrative provisions as interim framework.",
    "1947 சுதந்திரச் சட்டம் 1935 சட்டத்தின் கட்டுப்பாடுகளை ரத்து செய்து, அதன் நிர்வாக விதிகளை இடைக்காலக் கட்டமைப்பாக வைத்தது.",
    "Analyze", 75, ["Polity", "Historical Background", "Assertion and Reason", "Assembly Sovereignty"]
))

# ---------------------------------------------------------
# 5 MULTI-CONCEPT INTEGRATION QUESTIONS (HB_M_046 to HB_M_050)
# ---------------------------------------------------------

questions.append(make_q(
    "HB_M_046", "Multi-Concept Integration",
    "Trace the multi-stage evolution of Civil Services in British India by matching the relevant Act/Commission (Column I) with its Constitutional/Administrative Contribution (Column II):\n\nColumn I:\n1. Charter Act 1833\n2. Charter Act 1853\n3. Lee Commission (1923)\n4. Government of India Act 1935\n\nColumn II:\na. Open competition introduced; Macaulay Committee appointed (1854)\nb. First attempted open competition (negated by Court of Directors)\nc. Established Federal Public Service Commission and Provincial PSCs\nd. Recommended setting up of Central Public Service Commission (established 1926)\n\nSelect the correct matching code:",
    "பிரிட்டிஷ் இந்தியாவில் குடிமைப் பணிகளின் பலகட்ட வளர்ச்சியைப் பொருத்தமான சட்டம்/ஆணையம் (பத்தி I) மற்றும் அதன் அரசியலமைப்பு/நிர்வாகப் பங்களிப்புடன் (பத்தி II) பொருத்துக:\n\nபத்தி I:\n1. 1833 சாசனச் சட்டம்\n2. 1853 சாசனச் சட்டம்\n3. லீ ஆணையம் (1923)\n4. 1935 இந்திய அரசுச் சட்டம்\n\nபத்தி II:\na. திறந்தவெளிப் போட்டி அறிமுகம்; மெக்காலே குழு நியமனம் (1854)\nb. திறந்தவெளிப் போட்டிக்கு முதல் முயற்சி (இயக்குநர்கள் அவையால் நிராகரிப்பு)\nc. கூட்டாட்சி பொதுச் சேவை ஆணையம் & மாகாண PSC நிறுவுதல்\nd. மத்திய பொதுச் சேவை ஆணையத்தை அமைக்க பரிந்துரை (1926 இல் அமைவு)\n\nசரியான பொருத்தக் குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
    "1-b, 2-a, 3-d, 4-c", "1-b, 2-a, 3-d, 4-c",
    "1-a, 2-b, 3-c, 4-d", "1-a, 2-b, 3-c, 4-d",
    "1-b, 2-d, 3-a, 4-c", "1-b, 2-d, 3-a, 4-c",
    "1-d, 2-a, 3-b, 4-c", "1-d, 2-a, 3-b, 4-c",
    "A",
    "Matching breakdown:\n- Charter Act 1833 -> b. First attempted open competition (negated by Directors)\n- Charter Act 1853 -> a. Open competition introduced & Macaulay Committee 1854\n- Lee Commission (1923) -> d. Recommended Central PSC (established 1926)\n- GOI Act 1935 -> c. Federal PSC, Provincial PSCs, Joint PSC.",
    "பொருத்தம்:\n- 1833 சாசனச் சட்டம் -> b. முதல் முயற்சி (நிராகரிப்பு)\n- 1853 சாசனச் சட்டம் -> a. திறந்தவெளிப் போட்டி அறிமுகம் & மெக்காலே குழு\n- லீ ஆணையம் (1923) -> d. மத்திய PSC பரிந்துரை (1926 அமைவு)\n- 1935 அரசுச் சட்டம் -> c. கூட்டாட்சி PSC, மாகாண PSCகள்.",
    "Correct. Matches 1-b, 2-a, 3-d, 4-c accurately.",
    "சரி. 1-b, 2-a, 3-d, 4-c சரியாகப் பொருந்துகிறது.",
    "Incorrect. 1833 attempted, 1853 introduced.",
    "தவறு. 1833 முயற்சி செய்தது, 1853 அறிமுகப்படுத்தியது.",
    "Incorrect. Lee Commission recommended Central PSC.",
    "தவறு. லீ ஆணையம் மத்திய PSC-ஐ பரிந்துரைத்தது.",
    "Incorrect. Wrong mapping.",
    "தவறு. தவறான பொருத்தம்.",
    "Civil Services evolution timeline: 1833 (Attempted) -> 1853 (Open Competition) -> 1926 (Central PSC under Lee Comm) -> 1935 (Federal & Provincial PSCs).",
    "குடிமைப் பணி வளர்ச்சி: 1833 (முயற்சி) -> 1853 (போட்டி அறிமுகம்) -> 1926 (மத்திய PSC) -> 1935 (கூட்டாட்சி & மாகாண PSCகள்).",
    "Satyendranath Tagore (brother of Rabindranath Tagore) was the first Indian to qualify for the Indian Civil Service (ICS) in 1863.",
    "1863 இல் இந்திய குடிமைப் பணிக்குத் (ICS) தேர்ச்சியடைந்த முதல் இந்தியர் சத்யேந்திரநாத் தாகூர் ஆவார்.",
    "Analyze", 75, ["Polity", "Historical Background", "Multi-Concept", "Civil Services Evolution"]
))

questions.append(make_q(
    "HB_M_047", "Multi-Concept Integration",
    "Integrate the constitutional growth of Financial and Budgetary powers of Indian Legislative Councils from 1861 to 1919 by arranging the progressive rights granted to members:\n1. Right to vote on demands for grants and creation of separate Provincial Budgets\n2. No power to discuss budget or ask questions\n3. Right to discuss budget and address questions to executive (with 6 days notice, no voting)\n4. Right to move resolutions on the budget and ask supplementary questions\nSelect the correct evolution sequence from earliest to latest:",
    "1861 முதல் 1919 வரை இந்திய சட்டமன்ற கவுன்சில்களின் நிதி மற்றும் வரவு செலவுத் திட்ட அதிகாரங்களின் வளர்ச்சியை ஆரம்பம் முதல் இறுதி வரை வரிசைப்படுத்துக:\n1. மானியக் கோரிக்கைகள் மீது வாக்களிக்கும் உரிமை & தனி மாகாண வரவு செலவுத் திட்டம் உருவாக்கம்\n2. வரவு செலவுத் திட்டத்தை விவாதிக்கவோ கேள்விகள் கேட்கவோ அதிகாரம் இல்லை\n3. வரவு செலவுத் திட்டத்தை விவாதிக்கவும் கேள்விகள் கேட்கவும் உரிமை (வாக்களிப்பு இன்றி)\n4. வரவு செலவுத் திட்டத்தின் மீது தீர்மானங்கள் கொண்டு வரவும் துணைக் கேள்விகள் கேட்கவும் உரிமை\nமுந்தையதிலிருந்து பிந்தையதிற்கான சரியான வளர்ச்சியைத் தேர்ந்தெடுக்கவும்:",
    "2 - 3 - 4 - 1", "2 - 3 - 4 - 1",
    "3 - 2 - 4 - 1", "3 - 2 - 4 - 1",
    "2 - 4 - 3 - 1", "2 - 4 - 3 - 1",
    "1 - 2 - 3 - 4", "1 - 2 - 3 - 4",
    "A",
    "Financial Power Growth Timeline:\n- 2. 1861 Act: No right to discuss budget at all.\n- 3. 1892 Act: Allowed budget discussion & asking questions (no voting/supplementary).\n- 4. 1909 Act: Allowed supplementary questions & resolutions on budget.\n- 1. 1919 Act: Allowed voting on demands for grants (70% budget) & separated provincial budgets.",
    "நிதி அதிகார வளர்ச்சி காலவரிசை:\n- 2. 1861 சட்டம்: பட்ஜெட் விவாத உரிமை இல்லை.\n- 3. 1892 சட்டம்: பட்ஜெட் விவாதம் & கேள்விகள் கேட்க அனுமதி.\n- 4. 1909 சட்டம்: துணைக் கேள்விகள் & தீர்மானங்கள் கொண்டு வர அனுமதி.\n- 1. 1919 சட்டம்: மானியக் கோரிக்கைகள் மீது வாக்களிப்பு & தனி மாகாண பட்ஜெட்.",
    "Correct. Progression: 2 (1861) -> 3 (1892) -> 4 (1909) -> 1 (1919).",
    "சரி. வளர்ச்சி வரிசை: 2 (1861) -> 3 (1892) -> 4 (1909) -> 1 (1919).",
    "Incorrect. 1861 had no budget discussion.",
    "தவறு. 1861 இல் விவாத உரிமை இல்லை.",
    "Incorrect. Budget discussion (1892) preceded supplementary questions (1909).",
    "தவறு. 1892 சட்டம் 1909 சட்டத்திற்கு முன்னே வந்தது.",
    "Incorrect. Reverse sequence.",
    "தவறு. தலைகீழ் வரிசை.",
    "Financial Evolution Summary: 1861 (No discussion) -> 1892 (Discussion only) -> 1909 (Resolutions & Supplementary Qs) -> 1919 (Voting on demands & Provincial budget separation).",
    "நிதி வளர்ச்சி சுருக்கம்: 1861 (விவாதம் இல்லை) -> 1892 (விவாதம் மட்டும்) -> 1909 (தீர்மானங்கள் & துணைக் கேள்விகள்) -> 1919 (வாக்களிப்பு & மாகாண பட்ஜெட் பிரிப்பு).",
    "James Wilson introduced the first Indian Budget on February 18, 1860 under Lord Canning's administration.",
    "ஜேம்ஸ் வில்சன் 1860 பிப்ரவரி 18 அன்று லார்ட் கேனிங் நிர்வாகத்தில் முதல் இந்திய பட்ஜெட்டைத் தாக்கல் செய்தார்.",
    "Analyze", 75, ["Polity", "Historical Background", "Multi-Concept", "Financial Powers Evolution"]
))

questions.append(make_q(
    "HB_M_048", "Multi-Concept Integration",
    "Integrate the multi-act evolution of federal division of legislative powers in British India. Match the Act (Column I) with its specific Division of Powers scheme (Column II):\n\nColumn I:\n1. Charter Act 1833\n2. Indian Councils Act 1861\n3. Government of India Act 1919\n4. Government of India Act 1935\n\nColumn II:\na. Categorized subjects into Central and Provincial subjects\nb. Divided powers into Federal List (59), Provincial List (54), and Concurrent List (36)\nc. Concentrated all legislative power exclusively at the Centre\nd. Re-initiated legislative decentralization to Presidencies\n\nSelect the correct matching code:",
    "பிரிட்டிஷ் இந்தியாவில் சட்டமன்ற அதிகாரங்களின் கூட்டாட்சிப் பகிர்வின் பலகட்ட வளர்ச்சியை ஒருங்கிணைக்குக. சட்டம் (பத்தி I) மற்றும் அதன் அதிகாரப் பகிர்வுத் திட்டத்தை (பத்தி II) பொருத்துக:\n\nபத்தி I:\n1. 1833 சாசனச் சட்டம்\n2. 1861 இந்தியக் கவுன்சில்கள் சட்டம்\n3. 1919 இந்திய அரசுச் சட்டம்\n4. 1935 இந்திய அரசுச் சட்டம்\n\nபத்தி II:\a. அதிகாரங்களை மத்திய மற்றும் மாகாணத் துறைகளாக வகைப்படுத்தியது\nb. அதிகாரங்களை கூட்டாட்சிப் பட்டியல் (59), மாகாணப் பட்டியல் (54), இணைப்புப் பட்டியல் (36) எனப் பிரித்தது\nc. அனைத்து சட்ட அதிகாரங்களையும் மையத்தில் மட்டுமே குவித்தது\nd. மாகாணங்களுக்குச் சட்ட அதிகாரங்களை வழங்கி பரவலாக்கலைத் தொடங்கியது\n\nசரியான பொருத்தக் குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
    "1-c, 2-d, 3-a, 4-b", "1-c, 2-d, 3-a, 4-b",
    "1-a, 2-b, 3-c, 4-d", "1-a, 2-b, 3-c, 4-d",
    "1-c, 2-a, 3-d, 4-b", "1-c, 2-a, 3-d, 4-b",
    "1-d, 2-c, 3-a, 4-b", "1-d, 2-c, 3-a, 4-b",
    "A",
    "Matching breakdown:\n- Charter Act 1833 -> c. Concentrated all legislative power at Centre\n- Indian Councils Act 1861 -> d. Re-initiated legislative decentralization\n- GOI Act 1919 -> a. Categorized Central and Provincial subjects\n- GOI Act 1935 -> b. Divided powers into 3 Lists (Federal 59, Provincial 54, Concurrent 36).",
    "பொருத்தம்:\n- 1833 சாசனச் சட்டம் -> c. மையத்தில் சட்ட அதிகாரம் குவிப்பு\n- 1861 இந்தியக் கவுன்சில்கள் சட்டம் -> d. பரவலாக்கல் தொடக்கம்\n- 1919 அரசுச் சட்டம் -> a. மத்திய & மாகாணத் துறைகள் வகைப்பாடு\n- 1935 அரசுச் சட்டம் -> b. 3 பட்டியல்கள் (கூட்டாட்சி 59, மாகாணம் 54, இணைப்பு 36).",
    "Correct. Matches 1-c, 2-d, 3-a, 4-b accurately.",
    "சரி. 1-c, 2-d, 3-a, 4-b சரியாகப் பொருந்துகிறது.",
    "Incorrect. 1833 centralized powers.",
    "தவறு. 1833 அதிகாரங்களை மையப்படுத்தியது.",
    "Incorrect. 1861 initiated decentralization.",
    "தவறு. 1861 பரவலாக்கலைத் தொடங்கியது.",
    "Incorrect. Wrong order.",
    "தவறு. தவறான வரிசை.",
    "Division of Powers Arc: 1833 (Total Central Monopoly) -> 1861 (Decentralization onset) -> 1919 (2-List Subject division) -> 1935 (3-List Federal Scheme).",
    "அதிகாரப் பகிர்வு வளர்ச்சி: 1833 (மையக் குவிப்பு) -> 1861 (பரவலாக்கல் தொடக்கம்) -> 1919 (2-துறைப் பிரிவு) -> 1935 (3 பட்டியல்கள் கொண்ட கூட்டாட்சி).",
    "Our current Constitution's 7th Schedule (Union, State, Concurrent Lists) is directly modeled on the 1935 Act structure.",
    "நமது அரசியலமைப்பின் 7வது அட்டவணை (மத்திய, மாநில, பொதுப் பட்டியல்கள்) 1935 சட்டத்தின் மாதிரியிலேயே அமைக்கப்பட்டது.",
    "Analyze", 75, ["Polity", "Historical Background", "Multi-Concept", "Division of Powers"]
))

questions.append(make_q(
    "HB_M_049", "Multi-Concept Integration",
    "Integrate the progressive Indianization of executive and legislative bodies by connecting the historical act with the specific milestone achieved:\n1. First Indian Law Member in Viceroy's Executive Council -> Satyendra Prasad Sinha (1909 Act)\n2. First 3 nominated Indian members in Central Legislative Council -> Raja of Benares, Maharaja of Patiala, Sir Dinkar Rao (1861 Act)\n3. Requirement that 3 out of 6 members of Viceroy's Executive Council (other than Commander-in-Chief) must be Indian -> Government of India Act 1919\n4. Interim Government of India formed with all-Indian Executive Council members -> September 1946\nWhich of the above linkages are correct?",
    "நிர்வாக மற்றும் சட்டமன்ற அமைப்புகளில் இந்தியர்களின் இணைப்பை வரலாற்றுச் சட்டத்துடன் பொருத்தியுள்ள பின்வரும் இணைப்புகளை ஒருங்கிணைத்து எவை சரி எனத் தேர்ந்தெடுக்கவும்:\n1. வைஸ்ராய் நிர்வாகக் குழுவில் முதல் இந்தியச் சட்ட உறுப்பினர் -> சத்யேந்திர பிரசாத் சின்ஹா (1909 சட்டம்)\n2. மத்திய சட்டமன்ற கவுன்சிலில் முதல் 3 அரசுசாரா இந்திய உறுப்பினர்கள் -> காசி ராஜா, பாட்டியாலா மகாராஜா, சர் தினகர் ராவ் (1861 சட்டம்)\n3. வைஸ்ராய் நிர்வாகக் குழுவின் 6 உறுப்பினர்களில் (இராணுவத் தளபதி தவிர) 3 பேர் இந்தியர்களாக இருக்க வேண்டும் என்ற விதி -> 1919 இந்திய அரசுச் சட்டம்\n4. அனைத்து இந்திய உறுப்பினர்களையும் கொண்ட இடைக்கால அரசாங்கம் அமைவு -> செப்டம்பர் 1946\nஎது சரி?",
    "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டும்",
    "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டும்",
    "1, 3 and 4 only", "1, 3 மற்றும் 4 மட்டும்",
    "1, 2, 3 and 4", "1, 2, 3 மற்றும் 4",
    "D",
    "All four linkages are historically accurate. 1861 Act (3 non-official Indians in legislative council), 1909 Act (S.P. Sinha in executive council), 1919 Act (3 of 6 executive members Indians), Sep 1946 (Interim Govt under Nehru).",
    "நான்கு இணைப்புகளும் வரலாற்று ரீதியாகச் சரியானவை. 1861 சட்டம் (3 இந்தியர்கள்), 1909 சட்டம் (எஸ்.பி. சின்ஹா), 1919 சட்டம் (6 இல் 3 இந்தியர்கள்), செப் 1946 (நேரு தலைமையில் இடைக்கால அரசு).",
    "Incorrect. Linkage 4 is also correct.",
    "தவறு. இணைப்பு 4-ம் சரியானது.",
    "Incorrect. Linkage 1 is also correct.",
    "தவறு. இணைப்பு 1-ம் சரியானது.",
    "Incorrect. Linkage 2 is also correct.",
    "தவறு. இணைப்பு 2-ம் சரியானது.",
    "Correct. All 4 historical linkages are 100% accurate.",
    "சரி. 4 வரலாற்று இணைப்புகளும் 100% சரியானவை.",
    "Indianization Milestones: 1861 (Legislative Council nomination) -> 1909 (First Executive Council Indian) -> 1919 (3 out of 6 Executive members) -> 1946 (Interim Cabinet).",
    "இந்தியர் சேர்க்கை மைல்கற்கள்: 1861 (சட்டமன்ற நியமனம்) -> 1909 (நிர்வாகக் குழுவில் முதல் இந்தியர்) -> 1919 (6 இல் 3 உறுப்பினர்கள்) -> 1946 (இடைக்கால அமைச்சரவை).",
    "In the 1946 Interim Government, Jawahar Lal Nehru held Vice-President of Executive Council & External Affairs portfolio.",
    "1946 இடைக்கால அரசில் ஜவஹர்லால் நேரு நிர்வாகக் குழுவின் துணைத் தலைவராகவும் வெளியுறவுத்துறை அமைச்சராகவும் இருந்தார்.",
    "Analyze", 75, ["Polity", "Historical Background", "Multi-Concept", "Indianization of Administration"]
))

questions.append(make_q(
    "HB_M_050", "Multi-Concept Integration",
    "Which of the following constitutional provisions of the present Indian Constitution of 1950 are directly borrowed/derived from the Government of India Act 1935?\n1. Federal Scheme and Division of Powers into three lists\n2. Office of Governor and emergency powers\n3. Structure of Judiciary (Federal Court model for Supreme Court)\n4. Public Service Commissions (UPSC and State PSCs)\nSelect the correct answer using the code given below:",
    "1950 ஆம் ஆண்டின் தற்போதைய இந்திய அரசியலமைப்பின் பின்வரும் எந்த அரசியலமைப்பு விதிகள் 1935 ஆம் ஆண்டின் இந்திய அரசுச் சட்டத்திலிருந்து நேரடியாகப் பெறப்பட்டன?\n1. கூட்டாட்சித் திட்டம் மற்றும் அதிகாரங்களை மூன்று பட்டியல்களாகப் பிரித்தல்\n2. ஆளுநர் அலுவலகம் மற்றும் அவசரக்கால அதிகாரங்கள்\n3. நீதித்துறை கட்டமைப்பு (உச்ச நீதிமன்றத்திற்கான கூட்டாட்சி நீதிமன்ற மாதிரி)\n4. பொது சேவை ஆணையங்கள் (UPSC மற்றும் மாநில PSCகள்)\nசரியான விடையைத் தேர்ந்தெடுக்கவும்:",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டும்",
    "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டும்",
    "1, 2, 3 and 4", "1, 2, 3 மற்றும் 4",
    "D",
    "The Government of India Act 1935 served as the main structural blueprint for the 1950 Constitution of India (about 250 provisions borrowed). Federal scheme, Office of Governor, Judiciary, Public Service Commissions, Emergency provisions, and Administrative details were taken from 1935 Act.",
    "1935 இந்திய அரசுச் சட்டம் 1950 இந்திய அரசியலமைப்பின் முதன்மை வரைபடமாகச் செயல்பட்டது (சுமார் 250 விதிகள் எடுத்தாளப்பட்டன). கூட்டாட்சி, ஆளுநர் அலுவலகம், நீதித்துறை, பொது சேவை ஆணையங்கள், அவசரக்கால விதிகள் ஆகியவை 1935 சட்டத்திலிருந்து எடுக்கப்பட்டன.",
    "Incorrect. Statements 3 and 4 are also correct.",
    "தவறு. கூற்றுகள் 3 மற்றும் 4-ம் சரியானவை.",
    "Incorrect. Statement 4 is also correct.",
    "தவறு. கூற்று 4-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Correct. All 4 features are directly derived from the GOI Act 1935.",
    "சரி. 4 அம்சங்களும் 1935 இந்திய அரசுச் சட்டத்திலிருந்து நேரடியாகப் பெறப்பட்டவை.",
    "Remember: About 250 articles of 1950 Constitution were adapted directly or with slight modifications from GOI Act 1935.",
    "நினைவில் கொள்க: 1950 அரசியலமைப்பின் சுமார் 250 விதிகள் 1935 சட்டத்திலிருந்து நேரடியாக எடுத்தாளப்பட்டன.",
    "Dr. B.R. Ambedkar acknowledged that the draft Constitution had borrowed extensively from the Government of India Act 1935.",
    "டாக்டர் பி.ஆர். அம்பேத்கர் வரைவு அரசியலமைப்பு 1935 சட்டத்திலிருந்து அதிகளவில் எடுத்தாளப்பட்டதை அங்கீகரித்தார்.",
    "Analyze", 75, ["Polity", "Historical Background", "Multi-Concept", "Constitutional Borrowings 1935"]
))

# Save all 50 questions to target file
with open(target_path, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"Successfully generated and saved ALL {len(questions)} questions to {target_path}")

# Run schema validation using core/question_engine/validators.py
try:
    sys.path.insert(0, r"c:\Users\Home\Desktop\tnpsc_ai")
    from core.question_engine.validators import validate_questions
    val_res = validate_questions(questions)
    print(f"Validation Result: Valid={val_res.valid}")
    if val_res.errors:
        print("Validation Errors:", val_res.errors)
    if val_res.warnings:
        print("Validation Warnings:", val_res.warnings)
except Exception as e:
    print("Validation check failed with exception:", e)
