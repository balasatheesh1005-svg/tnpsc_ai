import json
import sys
from pathlib import Path

target_path = Path(r"c:\Users\Home\Desktop\tnpsc_ai\data\questions\polity\historical_background_hard.json")
if target_path.exists():
    with open(target_path, "r", encoding="utf-8") as f:
        questions = json.load(f)
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

# ---------------------------------------------------------
# 7 CHRONOLOGY QUESTIONS (HB_H_029 to HB_H_035)
# ---------------------------------------------------------

questions.append(make_q(
    "HB_H_029", "Chronology",
    "Arrange the creation of the following British administrative bodies in India in correct chronological sequence:\n1. Board of Control\n2. Supreme Court of Judicature at Calcutta\n3. Office of Secretary of State for India\n4. High Commissioner for India in London\nSelect the correct answer using the code given below:",
    "இந்தியாவில் பின்வரும் பிரிட்டிஷ் நிர்வாக அமைப்புகள் உருவாக்கப்பட்டதை சரியான காலவரிசையில் அமைக்கவும்:\n1. கட்டுப்பாட்டு வாரியம் (Board of Control)\n2. கொல்கத்தா உச்ச நீதிமன்றம் (Supreme Court at Calcutta)\n3. இந்திய அரசுச் செயலாளர் அலுவலகம் (Secretary of State)\n4. லண்டனில் இந்திய உயர் ஆணையர் (High Commissioner)\nசரியான வரிசையைத் தேர்ந்தெடுக்கவும்:",
    "2 - 1 - 3 - 4", "2 - 1 - 3 - 4",
    "1 - 2 - 3 - 4", "1 - 2 - 3 - 4",
    "2 - 3 - 1 - 4", "2 - 3 - 1 - 4",
    "4 - 3 - 2 - 1", "4 - 3 - 2 - 1",
    "A",
    "Chronological Order:\n- 2. Supreme Court at Calcutta: 1774 (Regulating Act 1773)\n- 1. Board of Control: 1784 (Pitt's India Act 1784)\n- 3. Secretary of State for India: 1858 (GOI Act 1858)\n- 4. High Commissioner for India: 1919 (GOI Act 1919, created 1920).",
    "சரியான காலவரிசை:\n- 2. கொல்கத்தா உச்ச நீதிமன்றம்: 1774 (1773 சட்டம்)\n- 1. கட்டுப்பாட்டு வாரியம்: 1784 (1784 சட்டம்)\n- 3. இந்திய அரசுச் செயலாளர்: 1858 (1858 சட்டம்)\n- 4. இந்திய உயர் ஆணையர்: 1919 (1919 சட்டம்).",
    "Correct. Order: 2 (1774) -> 1 (1784) -> 3 (1858) -> 4 (1919).",
    "சரி. வரிசை: 2 (1774) -> 1 (1784) -> 3 (1858) -> 4 (1919).",
    "Incorrect. Supreme Court (1774) preceded Board of Control (1784).",
    "தவறு. உச்ச நீதிமன்றம் (1774) கட்டுப்பாட்டு வாரியத்திற்கு (1784) முன்னே வந்தது.",
    "Incorrect. Board of Control came before Secretary of State.",
    "தவறு. கட்டுப்பாட்டு வாரியம் அரசுச் செயலாளருக்கு முன்னே வந்தது.",
    "Incorrect. Reverse order.",
    "தவறு. தலைகீழ் வரிசை.",
    "Key years: Supreme Court (1774) -> Board of Control (1784) -> Sec of State (1858) -> High Commissioner (1920).",
    "முக்கிய ஆண்டுகள்: உச்ச நீதிமன்றம் (1774) -> கட்டுப்பாட்டு வாரியம் (1784) -> அரசுச் செயலாளர் (1858) -> உயர் ஆணையர் (1920).",
    "The High Commissioner performed commercial duties previously handled by the Secretary of State.",
    "உயர் ஆணையர் முன்னதாக அரசுச் செயலாளர் கவனித்து வந்த வர்த்தகப் பணிகளைச் செய்தார்.",
    "Analyze", 75, ["Polity", "Historical Background", "Chronology", "Administrative Bodies"]
))

questions.append(make_q(
    "HB_H_030", "Chronology",
    "Arrange the following milestones in the evolution of Civil Services in British India in correct chronological order:\n1. Open competitive examination introduced for civil services selection\n2. Appointment of Lee Commission on Superior Civil Services\n3. Establishment of Central Public Service Commission\n4. First attempt to introduce open competition (negated by Court of Directors)\nSelect the correct answer using the code given below:",
    "பிரிட்டிஷ் இந்தியாவில் குடிமைப் பணிகளின் வளர்ச்சியில் பின்வரும் மைல்கற்களை சரியான காலவரிசையில் அமைக்கவும்:\n1. குடிமைப் பணித் தேர்வுக்கு திறந்தவெளிப் போட்டி அறிமுகப்படுத்தப்பட்டது\n2. உயர் குடிமைப் பணிகளுக்கான லீ ஆணையம் நியமனம்\n3. மத்திய பொதுச் சேவை ஆணையம் நிறுவுதல்\n4. திறந்தவெளிப் போட்டியை அறிமுகப்படுத்த முதல் முயற்சி (இயக்குநர்கள் அவையால் நிராகரிப்பு)\nசரியான வரிசையைத் தேர்ந்தெடுக்கவும்:",
    "4 - 1 - 2 - 3", "4 - 1 - 2 - 3",
    "1 - 4 - 2 - 3", "1 - 4 - 2 - 3",
    "4 - 1 - 3 - 2", "4 - 1 - 3 - 2",
    "1 - 2 - 3 - 4", "1 - 2 - 3 - 4",
    "A",
    "Chronological Order:\n- 4. First attempt: 1833 (Charter Act 1833)\n- 1. Open competition introduced: 1853 (Charter Act 1853 / Macaulay Comm 1854)\n- 2. Lee Commission appointed: 1923\n- 3. Central Public Service Commission established: 1926.",
    "சரியான காலவரிசை:\n- 4. முதல் முயற்சி: 1833 (1833 சாசனச் சட்டம்)\n- 1. போட்டித் தேர்வு அறிமுகம்: 1853 (1853 சாசனச் சட்டம் / மெக்காலே குழு 1854)\n- 2. லீ ஆணையம்: 1923\n- 3. மத்திய பொதுச் சேவை ஆணையம்: 1926.",
    "Correct. Order: 4 (1833) -> 1 (1853) -> 2 (1923) -> 3 (1926).",
    "சரி. வரிசை: 4 (1833) -> 1 (1853) -> 2 (1923) -> 3 (1926).",
    "Incorrect. First attempt (1833) preceded successful introduction (1853).",
    "தவறு. முதல் முயற்சி (1833) வெற்றி பெற்ற அறிமுகத்திற்கு (1853) முன்னே வந்தது.",
    "Incorrect. Lee Commission (1923) preceded setting up of Central PSC (1926).",
    "தவறு. லீ ஆணையம் (1923) மத்திய PSC அமைவதற்கு (1926) முன்னே வந்தது.",
    "Incorrect. Wrong order.",
    "தவறு. தவறான வரிசை.",
    "Civil Services Arc: 1833 (Attempted) -> 1853 (Open Competition) -> 1923 (Lee Comm) -> 1926 (Central PSC) -> 1935 (Federal PSC).",
    "குடிமைப் பணி வளர்ச்சி: 1833 (முயற்சி) -> 1853 (போட்டி) -> 1923 (லீ ஆணையம்) -> 1926 (மத்திய PSC) -> 1935 (கூட்டாட்சி PSC).",
    "Satyendranath Tagore became the first Indian to clear ICS exam in 1863.",
    "1863 இல் சத்யேந்திரநாத் தாகூர் ICS தேர்வில் தேர்ச்சியடைந்த முதல் இந்தியர் ஆனார்.",
    "Analyze", 75, ["Polity", "Historical Background", "Chronology", "Civil Services Arc"]
))

questions.append(make_q(
    "HB_H_031", "Chronology",
    "Arrange the following Legislative Council expansion milestones in British India in correct chronological order:\n1. Right to vote on demands for grants given to council members\n2. Right to discuss budget and address questions granted (no voting)\n3. Right to ask supplementary questions and move budget resolutions granted\n4. Creation of separate 6-member Indian (Central) Legislative Council\nSelect the correct answer using the code given below:",
    "பிரிட்டிஷ் இந்தியாவில் சட்டமன்ற கவுன்சில் அதிகார விரிவாக்க மைல்கற்களை சரியான காலவரிசையில் அமைக்கவும்:\n1. மானியக் கோரிக்கைகள் மீது வாக்களிக்கும் உரிமை உறுப்பினர்களுக்கு வழங்கப்பட்டது\n2. பட்ஜெட் விவாதம் மற்றும் கேள்விகள் கேட்கும் உரிமை வழங்கப்பட்டது (வாக்களிப்பு இன்றி)\n3. துணைக் கேள்விகள் கேட்கவும் பட்ஜெட் மீது தீர்மானம் கொண்டு வரவும் உரிமை வழங்கப்பட்டது\n4. 6 உறுப்பினர்கள் கொண்ட தனி இந்திய (மத்திய) சட்டமன்ற கவுன்சில் உருவாக்கப்பட்டது\nசரியான வரிசையைத் தேர்ந்தெடுக்கவும்:",
    "4 - 2 - 3 - 1", "4 - 2 - 3 - 1",
    "2 - 4 - 3 - 1", "2 - 4 - 3 - 1",
    "4 - 3 - 2 - 1", "4 - 3 - 2 - 1",
    "1 - 2 - 3 - 4", "1 - 2 - 3 - 4",
    "A",
    "Chronological Order:\n- 4. Separate Legislative Council created: 1853 (Charter Act 1853)\n- 2. Budget discussion & questions: 1892 (Indian Councils Act 1892)\n- 3. Supplementary questions & resolutions: 1909 (Indian Councils Act 1909)\n- 1. Voting on demands for grants: 1919 (Government of India Act 1919).",
    "சரியான காலவரிசை:\n- 4. தனி சட்டமன்ற கவுன்சில்: 1853 (1853 சாசனச் சட்டம்)\n- 2. பட்ஜெட் விவாதம் & கேள்விகள்: 1892 (1892 இந்தியக் கவுன்சில்கள் சட்டம்)\n- 3. துணைக் கேள்விகள் & தீர்மானங்கள்: 1909 (1909 இந்தியக் கவுன்சில்கள் சட்டம்)\n- 1. மானியக் கோரிக்கைகள் மீது வாக்களிப்பு: 1919 (1919 இந்திய அரசுச் சட்டம்).",
    "Correct. Order: 4 (1853) -> 2 (1892) -> 3 (1909) -> 1 (1919).",
    "சரி. வரிசை: 4 (1853) -> 2 (1892) -> 3 (1909) -> 1 (1919).",
    "Incorrect. Creation of council (1853) preceded budget discussion (1892).",
    "தவறு. கவுன்சில் உருவாக்கம் (1853) பட்ஜெட் விவாதத்திற்கு (1892) முன்னே வந்தது.",
    "Incorrect. Budget discussion (1892) preceded supplementary questions (1909).",
    "தவறு. பட்ஜெட் விவாதம் (1892) துணைக் கேள்விகளுக்கு (1909) முன்னே வந்தது.",
    "Incorrect. Reverse order.",
    "தவறு. தலைகீழ் வரிசை.",
    "Financial Powers Arc: 1853 (Council created) -> 1892 (Budget discussion) -> 1909 (Supplementary Qs) -> 1919 (Voting on demands).",
    "நிதி அதிகார வளர்ச்சி: 1853 (கவுன்சில்) -> 1892 (விவாதம்) -> 1909 (துணைக் கேள்விகள்) -> 1919 (வாக்களிப்பு).",
    "Under 1919 Act, 70% of the Central budget demands were voted on by the Legislative Assembly.",
    "1919 சட்டப்படி மத்திய பட்ஜெட் கோரிக்கைகளில் 70% சட்டமன்றப் பேரவையால் வாக்களிக்கப்பட்டது.",
    "Analyze", 75, ["Polity", "Historical Background", "Chronology", "Legislative Powers Arc"]
))

questions.append(make_q(
    "HB_H_032", "Chronology",
    "Arrange the creation of the following executive head titles in British India in chronological sequence:\n1. Governor-General of India\n2. Governor-General of Bengal\n3. Governor-General of Independent Dominion of India\n4. Viceroy and Governor-General of India\nSelect the correct code:",
    "பிரிட்டிஷ் இந்தியாவில் நிர்வாகத் தலைவர் பதவிகள் உருவானதை சரியான காலவரிசையில் அமைக்கவும்:\n1. இந்திய கவர்னர் ஜெனரல்\n2. வங்காள கவர்னர் ஜெனரல்\n3. சுதந்திர இந்திய டொமினியனின் கவர்னர் ஜெனரல்\n4. இந்திய வைஸ்ராய் மற்றும் கவர்னர் ஜெனரல்\nசரியான வரிசையைத் தேர்ந்தெடுக்கவும்:",
    "2 - 1 - 4 - 3", "2 - 1 - 4 - 3",
    "1 - 2 - 4 - 3", "1 - 2 - 4 - 3",
    "2 - 4 - 1 - 3", "2 - 4 - 1 - 3",
    "4 - 2 - 1 - 3", "4 - 2 - 1 - 3",
    "A",
    "Chronological Order:\n- 2. Governor-General of Bengal: 1773 (Regulating Act 1773 - Warren Hastings)\n- 1. Governor-General of India: 1833 (Charter Act 1833 - William Bentinck)\n- 4. Viceroy and Governor-General of India: 1858 (GOI Act 1858 - Lord Canning)\n- 3. Governor-General of Dominion of India: 1947 (Independence Act 1947 - Lord Mountbatten / C. Rajagopalachari).",
    "சரியான காலவரிசை:\n- 2. வங்காள கவர்னர் ஜெனரல்: 1773 (1773 சட்டம் - வாரன் ஹேஸ்டிங்ஸ்)\n- 1. இந்திய கவர்னர் ஜெனரல்: 1833 (1833 சாசனச் சட்டம் - வில்லியம் பென்டிங்க்)\n- 4. இந்திய வைஸ்ராய்: 1858 (1858 சட்டம் - கேனிங் பிரபு)\n- 3. சுதந்திர இந்திய கவர்னர் ஜெனரல்: 1947 (1947 சட்டம் - மவுண்ட்பேட்டன் / ராஜாஜி).",
    "Correct. Order: 2 (1773) -> 1 (1833) -> 4 (1858) -> 3 (1947).",
    "சரி. வரிசை: 2 (1773) -> 1 (1833) -> 4 (1858) -> 3 (1947).",
    "Incorrect. GG of Bengal (1773) came before GG of India (1833).",
    "தவறு. வங்காள GG 1773 இல் வந்தார், இந்திய GG 1833 இல் வந்தார்.",
    "Incorrect. GG of India (1833) came before Viceroy (1858).",
    "தவறு. இந்திய GG 1833 இல் வந்தார், வைஸ்ராய் 1858 இல் வந்தார்.",
    "Incorrect. Reverse hierarchy.",
    "தவறு. தவறான வரிசை.",
    "First incumbents: Warren Hastings (Bengal GG 1773), Lord William Bentinck (India GG 1833), Lord Canning (Viceroy 1858), C. Rajagopalachari (First Indian Dominion GG 1948).",
    "முதல் பதவி வகித்தவர்கள்: வாரன் ஹேஸ்டிங்ஸ் (1773), வில்லியம் பென்டிங்க் (1833), லார்ட் கேனிங் (1858), சி. ராஜகோபாலாச்சாரி (1948).",
    "The office of Governor-General ceased to exist on January 26, 1950 when the Constitution came into force.",
    "1950 ஜனவரி 26 இல் அரசியலமைப்பு அமலுக்கு வந்தபோது கவர்னர் ஜெனரல் பதவி முடிவுக்கு வந்தது.",
    "Analyze", 75, ["Polity", "Historical Background", "Chronology", "Executive Head Titles"]
))

questions.append(make_q(
    "HB_H_033", "Chronology",
    "Arrange the following major British Constitutional Acts in exact sequence of their passage by British Parliament:\n1. Act establishing system of Double Government\n2. Act transferring power from East India Company to British Crown\n3. Act establishing Supreme Court at Calcutta\n4. Act introducing Dyarchy in Provinces\n5. Act introducing Provincial Autonomy\nSelect the correct code:",
    "பின்வரும் பிரிட்டிஷ் அரசியலமைப்புச் சட்டங்களை அவை பிரிட்டிஷ் பாராளுமன்றத்தால் நிறைவேற்றப்பட்ட துல்லியமான வரிசையில் அமைக்கவும்:\n1. இரட்டை ஆட்சி முறையை நிறுவிய சட்டம் (Double Govt)\n2. கம்பெனியிடமிருந்து பிரிட்டிஷ் அரசிற்கு அதிகாரத்தை மாற்றிய சட்டம்\n3. கொல்கத்தா உச்ச நீதிமன்றத்தை நிறுவிய சட்டம்\n4. மாகாணங்களில் இரட்டை ஆட்சியை அறிமுகப்படுத்திய சட்டம் (Dyarchy)\n5. மாகாண தன்னாட்சியை அறிமுகப்படுத்திய சட்டம்\nசரியான வரிசையைத் தேர்ந்தெடுக்கவும்:",
    "3 - 1 - 2 - 4 - 5", "3 - 1 - 2 - 4 - 5",
    "1 - 3 - 2 - 4 - 5", "1 - 3 - 2 - 4 - 5",
    "3 - 2 - 1 - 4 - 5", "3 - 2 - 1 - 4 - 5",
    "3 - 1 - 4 - 2 - 5", "3 - 1 - 4 - 2 - 5",
    "A",
    "Chronological Sequence:\n- 3. Regulating Act 1773 (Supreme Court at Calcutta 1774)\n- 1. Pitt's India Act 1784 (Double Govt: Court of Directors vs Board of Control)\n- 2. Government of India Act 1858 (Crown takeover)\n- 4. Government of India Act 1919 (Provincial Dyarchy)\n- 5. Government of India Act 1935 (Provincial Autonomy).",
    "சரியான வரிசை:\n- 3. 1773 ஒழுங்குமுறைச் சட்டம் (கொல்கத்தா உச்ச நீதிமன்றம்)\n- 1. 1784 பிட் இந்தியச் சட்டம் (இரட்டை நிர்வாகம்)\n- 2. 1858 இந்திய அரசுச் சட்டம் (முடிஅரசு மாற்றம்)\n- 4. 1919 இந்திய அரசுச் சட்டம் (மாகாண இரட்டை ஆட்சி)\n- 5. 1935 இந்திய அரசுச் சட்டம் (மாகாண தன்னாட்சி).",
    "Correct. Order: 3 (1773) -> 1 (1784) -> 2 (1858) -> 4 (1919) -> 5 (1935).",
    "சரி. வரிசை: 3 (1773) -> 1 (1784) -> 2 (1858) -> 4 (1919) -> 5 (1935).",
    "Incorrect. Regulating Act 1773 came before Pitt's India Act 1784.",
    "தவறு. 1773 சட்டம் 1784 சட்டத்திற்கு முன்னே வந்தது.",
    "Incorrect. Pitt's Act (1784) came before Crown takeover (1858).",
    "தவறு. 1784 சட்டம் 1858 சட்டத்திற்கு முன்னே வந்தது.",
    "Incorrect. Crown takeover (1858) came before 1919 Dyarchy.",
    "தவறு. 1858 சட்டம் 1919 சட்டத்திற்கு முன்னே வந்தது.",
    "Landmark Acts timeline: 1773 -> 1784 -> 1858 -> 1919 -> 1935.",
    "முக்கிய சட்டங்கள் காலக்கோடு: 1773 -> 1784 -> 1858 -> 1919 -> 1935.",
    "Government of India Act 1935 contained 321 sections and 10 schedules.",
    "1935 இந்திய அரசுச் சட்டம் 321 பிரிவுகள் மற்றும் 10 அட்டவணைகளைக் கொண்டிருந்தது.",
    "Analyze", 75, ["Polity", "Historical Background", "Chronology", "Acts Sequence Sequence"]
))

questions.append(make_q(
    "HB_H_034", "Chronology",
    "Arrange the following political and constitutional events leading to Indian independence in correct chronological sequence:\n1. Appointment of Simon Commission\n2. Montagu's August Declaration\n3. Passage of Government of India Act 1935\n4. Cabinet Mission Plan\n5. Passage of Indian Independence Act\nSelect the correct answer using the code given below:",
    "இந்திய சுதந்திரத்திற்கு வழிவகுத்த பின்வரும் அரசியல் மற்றும் அரசியலமைப்பு நிகழ்வுகளை சரியான காலவரிசையில் அமைக்கவும்:\n1. சைமன் குழு நியமனம்\n2. மாண்டேகுவின் ஆகஸ்ட் பிரகடனம்\n3. 1935 இந்திய அரசுச் சட்டம் நிறைவேற்றம்\n4. கேபினட் மிஷன் திட்டம்\n5. இந்திய சுதந்திரச் சட்டம் நிறைவேற்றம்\nசரியான வரிசையைத் தேர்ந்தெடுக்கவும்:",
    "2 - 1 - 3 - 4 - 5", "2 - 1 - 3 - 4 - 5",
    "1 - 2 - 3 - 4 - 5", "1 - 2 - 3 - 4 - 5",
    "2 - 3 - 1 - 4 - 5", "2 - 3 - 1 - 4 - 5",
    "2 - 1 - 4 - 3 - 5", "2 - 1 - 4 - 3 - 5",
    "A",
    "Chronological Order:\n- 2. Montagu's August Declaration: August 1917\n- 1. Simon Commission appointed: November 1927\n- 3. GOI Act 1935 passed: August 1935\n- 4. Cabinet Mission Plan: March/May 1946\n- 5. Indian Independence Act passed: July 18, 1947.",
    "சரியான காலவரிசை:\n- 2. மாண்டேகு ஆகஸ்ட் பிரகடனம்: ஆகஸ்ட் 1917\n- 1. சைமன் குழு நியமனம்: நவம்பர் 1927\n- 3. 1935 அரசுச் சட்டம்: ஆகஸ்ட் 1935\n- 4. கேபினட் மிஷன் திட்டம்: மார்ச்/மே 1946\n- 5. இந்திய சுதந்திரச் சட்டம்: ஜூலை 18, 1947.",
    "Correct. Order: 2 (1917) -> 1 (1927) -> 3 (1935) -> 4 (1946) -> 5 (1947).",
    "சரி. வரிசை: 2 (1917) -> 1 (1927) -> 3 (1935) -> 4 (1946) -> 5 (1947).",
    "Incorrect. Montagu declaration (1917) came before Simon Commission (1927).",
    "தவறு. 1917 பிரகடனம் 1927 சைமன் குழுவிற்கு முன்னே வந்தது.",
    "Incorrect. Simon Commission (1927) preceded GOI Act 1935.",
    "தவறு. 1927 சைமன் குழு 1935 சட்டத்திற்கு முன்னே வந்தது.",
    "Incorrect. Cabinet Mission (1946) came after 1935 Act.",
    "தவறு. கேபினட் மிஷன் 1935 சட்டத்திற்குப் பிறகே வந்தது.",
    "Timeline check: Montagu Declaration (1917) -> Simon Comm (1927) -> GOI Act (1935) -> Cabinet Mission (1946) -> Independence Act (1947).",
    "காலக்கோடு: மாண்டேகு (1917) -> சைமன் குழு (1927) -> 1935 சட்டம் -> கேபினட் மிஷன் (1946) -> சுதந்திரச் சட்டம் (1947).",
    "Simon Commission submitted its report in 1930, leading to Round Table Conferences (1930-1932) and White Paper of 1933.",
    "சைமன் குழு 1930 இல் அறிக்கை அளித்து வட்டமேஜை மாநாடுகளுக்கும் 1933 வெள்ளை அறிக்கைக்கும் வழியமைத்தது.",
    "Analyze", 75, ["Polity", "Historical Background", "Chronology", "Constitutional Events Arc"]
))

questions.append(make_q(
    "HB_H_035", "Chronology",
    "Arrange the following milestones in the expansion of Communal Electorates and Franchise in British India in correct chronological order:\n1. Separate Electorates introduced for Muslims\n2. Separate Electorates extended to Sikhs, Indian Christians, Anglo-Indians, and Europeans\n3. Separate Electorates extended to Depressed Classes (Scheduled Castes), Women, and Labour\n4. Indirect election recommendation mechanism introduced for non-official council seats\nSelect the correct answer using the code given below:",
    "பிரிட்டிஷ் இந்தியாவில் வகுப்புவாதத் தொகுதிகள் மற்றும் வாக்குரிமை விரிவாக்க மைல்கற்களை சரியான காலவரிசையில் அமைக்கவும்:\n1. முஸ்லிம்களுக்குத் தனித் தொகுதிகள் அறிமுகப்படுத்தப்பட்டன\n2. சீக்கியர்கள், இந்தியக் கிறிஸ்தவர்கள், ஆங்கிலோ-இந்தியர்கள், ஐரோப்பியர்களுக்குத் தனித் தொகுதிகள் விரிவுபடுத்தப்பட்டன\n3. தாழ்த்தப்பட்ட பிரிவினர் (பட்டியல் சாதியினர்), பெண்கள், தொழிலாளர்களுக்குத் தனித் தொகுதிகள் விரிவுபடுத்தப்பட்டன\n4. அரசுசாரா கவுன்சில் இடங்களுக்கு மறைமுகத் தேர்தல் பரிந்துரை முறை அறிமுகப்படுத்தப்பட்டது\nசரியான வரிசையைத் தேர்ந்தெடுக்கவும்:",
    "4 - 1 - 2 - 3", "4 - 1 - 2 - 3",
    "1 - 4 - 2 - 3", "1 - 4 - 2 - 3",
    "4 - 2 - 1 - 3", "4 - 2 - 1 - 3",
    "1 - 2 - 3 - 4", "1 - 2 - 3 - 4",
    "A",
    "Chronological Order:\n- 4. Indirect recommendation: 1892 (Indian Councils Act 1892)\n- 1. Muslim separate electorate: 1909 (Morley-Minto Reforms)\n- 2. Extended to Sikhs, Christians, Anglo-Indians: 1919 (Montagu-Chelmsford Reforms)\n- 3. Extended to SCs, Women, Labour: 1935 (Government of India Act 1935).",
    "சரியான காலவரிசை:\n- 4. மறைமுகப் பரிந்துரை: 1892 (1892 இந்தியக் கவுன்சில்கள் சட்டம்)\n- 1. முஸ்லிம் தனித் தொகுதி: 1909 (மோர்லே-மிண்டோ சீர்திருத்தங்கள்)\n- 2. சீக்கியர்கள், கிறிஸ்தவர்கள் விரிவாக்கம்: 1919 (மாண்டேகு-செம்ஸ்ஃபோர்டு சீர்திருத்தங்கள்)\n- 3. பட்டியல் சாதியினர், பெண்கள் விரிவாக்கம்: 1935 (1935 இந்திய அரசுச் சட்டம்).",
    "Correct. Order: 4 (1892) -> 1 (1909) -> 2 (1919) -> 3 (1935).",
    "சரி. வரிசை: 4 (1892) -> 1 (1909) -> 2 (1919) -> 3 (1935).",
    "Incorrect. Indirect recommendation (1892) came before Muslim electorate (1909).",
    "தவறு. மறைமுகப் பரிந்துரை (1892) முஸ்லிம் தனித் தொகுதிக்கு (1909) முன்னே வந்தது.",
    "Incorrect. Muslim electorate (1909) preceded Sikh extension (1919).",
    "தவறு. முஸ்லிம் தனித் தொகுதி (1909) சீக்கியர் விரிவாக்கத்திற்கு (1919) முன்னே வந்தது.",
    "Incorrect. Reverse order.",
    "தவறு. தலைகீழ் வரிசை.",
    "Electorate Expansion Timeline: 1892 (Indirect) -> 1909 (Muslims) -> 1919 (Sikhs, Christians, Europeans) -> 1935 (SCs, Women, Labour).",
    "தொகுதி விரிவாக்கம்: 1892 (மறைமுகம்) -> 1909 (முஸ்லிம்கள்) -> 1919 (சீக்கியர்கள், கிறிஸ்தவர்கள்) -> 1935 (பட்டியல் சாதியினர், பெண்கள்).",
    "Ramsay MacDonald announced the Communal Award in August 1932, leading to Poona Pact (Sept 1932) between Gandhi and Ambedkar.",
    "ராம்சே மெக்டொனால்டு 1932 ஆகஸ்டில் வகுப்புவாத கொடையை அறிவித்தார், இது காந்தி-அம்பேத்கர் இடையிலான பூனா ஒப்பந்தத்திற்கு (1932 செப்) வழியமைத்தது.",
    "Analyze", 75, ["Polity", "Historical Background", "Chronology", "Electorate Expansion Arc"]
))

# ---------------------------------------------------------
# 5 CONSTITUTIONAL EVOLUTION QUESTIONS (HB_H_036 to HB_H_040)
# ---------------------------------------------------------

questions.append(make_q(
    "HB_H_036", "Constitutional Evolution",
    "Trace the evolution of the executive's emergency Ordinance-making power in India from colonial roots to the present Indian Constitution:",
    "இந்தியாவில் நிர்வாகத்தின் அவசரச்சட்ட அதிகாரத்தின் (Ordinance) வளர்ச்சியை காலனித்துவ வேர்களிலிருந்து தற்போதைய இந்திய அரசியலமைப்பு வரை கண்டுபிடிக்கவும்:",
    "Introduced by Indian Councils Act 1861 (6 months validity for Viceroy), expanded under GOI Act 1935 (Sections 42 & 43 for Governor-General), and incorporated as Articles 123 (President) and 213 (Governor) in the 1950 Constitution.",
    "1861 இந்தியக் கவுன்சில்கள் சட்டத்தால் அறிமுகப்படுத்தப்பட்டது (வைஸ்ராய்க்கு 6 மாத காலம்), 1935 அரசுச் சட்டத்தில் விரிவாக்கப்பட்டது (பிரிவுகள் 42 & 43), மேலும் 1950 அரசியலமைப்பில் பகுதிகள் 123 (குடியரசுத் தலைவர்) மற்றும் 213 (ஆளுநர்) ஆக இணைக்கப்பட்டது.",
    "Introduced by Regulating Act 1773 and retained without change in 1950.",
    "1773 ஒழுங்குமுறைச் சட்டத்தால் அறிமுகப்படுத்தப்பட்டு 1950 இல் எந்த மாற்றமும் இன்றி தக்கவைக்கப்பட்டது.",
    "Introduced by Indian Independence Act 1947 and abolished in 1950 Constitution.",
    "1947 இந்திய சுதந்திரச் சட்டத்தால் அறிமுகப்படுத்தப்பட்டு 1950 அரசியலமைப்பில் ஒழிக்கப்பட்டது.",
    "Introduced by Charter Act 1833 for Supreme Court judges only.",
    "1833 சாசனச் சட்டத்தால் உச்ச நீதிமன்ற நீதிபதிகளுக்கு மட்டுமே அறிமுகப்படுத்தப்பட்டது.",
    "A",
    "Ordinance power was first created by Indian Councils Act 1861 (Viceroy could issue ordinances valid for 6 months during emergencies). GOI Act 1935 expanded it under Sections 42/43. Modern Articles 123 & 213 directly trace to this colonial evolutionary lineage.",
    "அவசரச்சட்ட அதிகாரம் 1861 இல் வைஸ்ராய்க்கு (6 மாதங்கள்) உருவாக்கப்பட்டது. 1935 சட்டத்தில் பிரிவுகள் 42/43 இல் விரிவாக்கப்பட்டது. தற்போதைய 123 & 213 விதிகள் இதன் தொடர்ச்சியாகும்.",
    "Correct. Traces ordinance power from 1861 Act -> 1935 Act -> Articles 123 & 213 in 1950 Constitution.",
    "சரி. அவசரச்சட்ட அதிகாரம் 1861 சட்டம் -> 1935 சட்டம் -> 1950 அரசியலமைப்பின் 123 & 213 விதிகளாக அமைந்தது.",
    "Incorrect. 1773 Act did not have ordinance provisions.",
    "தவறு. 1773 சட்டத்தில் அவசரச்சட்ட விதிகள் இல்லை.",
    "Incorrect. Ordinance power was not abolished in 1950; it is active under Articles 123 and 213.",
    "தவறு. அவசரச்சட்ட அதிகாரம் 1950 இல் ஒழிக்கப்படவில்லை.",
    "Incorrect. 1833 Act did not grant ordinance powers to SC judges.",
    "தவறு. 1833 சட்டம் நீதிபதிகளுக்கு அவசரச்சட்ட அதிகாரம் தரவில்லை.",
    "Ordinances promulgated by President (Article 123) or Governor (Article 213) must be laid before Parliament/Legislature upon reassembly.",
    "குடியரசுத் தலைவர் (பிரிவு 123) அல்லது ஆளுநர் (பிரிவு 213) பிறப்பிக்கும் அவசரச்சட்டம் பாராளுமன்றம் கூடியதும் சமர்ப்பிக்கப்பட வேண்டும்.",
    "Max life of an Ordinance without legislative approval is 6 months and 6 weeks.",
    "பாராளுமன்ற ஒப்புதலின்றி அவசரச்சட்டத்தின் அதிகபட்ச ஆயுட்காலம் 6 மாதங்கள் மற்றும் 6 வாரங்கள் ஆகும்.",
    "Analyze", 75, ["Polity", "Historical Background", "Constitutional Evolution", "Ordinance Power Arc"]
))

questions.append(make_q(
    "HB_H_037", "Constitutional Evolution",
    "Trace the evolutionary arc of judicial organization in India from Company rule to the present Supreme Court of India:",
    "கம்பெனி ஆட்சியிலிருந்து தற்போதைய இந்திய உச்ச நீதிமன்றம் வரையிலான நீதித்துறை அமைப்பின் வளர்ச்சிப் பாதையைக் கண்டறிக:",
    "1774 Supreme Court at Calcutta -> 1861 High Courts Act (replacing Supreme Courts & Sadar Adalats with High Courts at Calcutta, Bombay, Madras) -> 1937 Federal Court under 1935 Act -> 1950 Supreme Court of India under Article 124.",
    "1774 கொல்கத்தா உச்ச நீதிமன்றம் -> 1861 உயர் நீதிமன்றங்கள் சட்டம் (கொல்கத்தா, பம்பாய், மதராஸ் உயர் நீதிமன்றங்கள் அமைவு) -> 1935 சட்டத்தின் கீழ் 1937 கூட்டாட்சி நீதிமன்றம் -> 1950 அரசியலமைப்பின் பிரிவு 124 இன் கீழ் இந்திய உச்ச நீதிமன்றம்.",
    "1773 Federal Court -> 1858 High Court -> 1947 Supreme Court.",
    "1773 கூட்டாட்சி நீதிமன்றம் -> 1858 உயர் நீதிமன்றம் -> 1947 உச்ச நீதிமன்றம்.",
    "1833 Law Commission -> 1909 Privy Council -> 1950 Supreme Court.",
    "1833 சட்ட ஆணையம் -> 1909 பிரிவி கவுன்சில் -> 1950 உச்ச நீதிமன்றம்.",
    "1784 Board of Control -> 1861 Supreme Court -> 1950 High Court.",
    "1784 கட்டுப்பாட்டு வாரியம் -> 1861 உச்ச நீதிமன்றம் -> 1950 உயர் நீதிமன்றம்.",
    "A",
    "Judicial evolution: Supreme Court at Calcutta (1774) -> Indian High Courts Act 1861 merged Supreme Court and Sadar Adalats into High Courts -> GOI Act 1935 created Federal Court (1937) -> Supreme Court of India established Jan 28, 1950 (Article 124).",
    "நீதித்துறை வளர்ச்சி: 1774 கொல்கத்தா உச்ச நீதிமன்றம் -> 1861 உயர் நீதிமன்றங்கள் சட்டம் -> 1937 கூட்டாட்சி நீதிமன்றம் (1935 சட்டம்) -> 1950 ஜனவரி 28 இல் இந்திய உச்ச நீதிமன்றம் (பிரிவு 124).",
    "Correct. Traces judicial hierarchy from 1774 -> 1861 High Courts -> 1937 Federal Court -> 1950 Supreme Court.",
    "சரி. 1774 -> 1861 உயர் நீதிமன்றங்கள் -> 1937 கூட்டாட்சி நீதிமன்றம் -> 1950 உச்ச நீதிமன்றம் எனத் துல்லியமாகப் பின்பற்றுகிறது.",
    "Incorrect. Federal Court was set up in 1937, not 1773.",
    "தவறு. கூட்டாட்சி நீதிமன்றம் 1937 இல் அமைந்தது.",
    "Incorrect. Misses High Courts Act 1861 and Federal Court 1937.",
    "தவறு. 1861 உயர் நீதிமன்றங்கள் சட்டம் மற்றும் 1937 கூட்டாட்சி நீதிமன்றத்தை விடுவிக்கிறது.",
    "Incorrect. Board of Control was executive/political, not judicial.",
    "தவறு. கட்டுப்பாட்டு வாரியம் நிர்வாக அமைப்பாகும்.",
    "The Federal Court established in 1937 began functioning with Sir Maurice Gwyer as its first Chief Justice.",
    "1937 இல் தொடங்கப்பட்ட கூட்டாட்சி நீதிமன்றத்தின் முதல் தலைமை நீதிபதியாக சர் மோரிஸ் குவையர் இருந்தார்.",
    "Supreme Court of India inaugurated on January 28, 1950, succeeding both Federal Court of India and Judicial Committee of Privy Council.",
    "இந்திய உச்ச நீதிமன்றம் 1950 ஜனவரி 28 அன்று தொடங்கப்பட்டு கூட்டாட்சி நீதிமன்றம் மற்றும் பிரிவி கவுன்சில் அதிகாரம் இரண்டையும் ஏற்றது.",
    "Analyze", 75, ["Polity", "Historical Background", "Constitutional Evolution", "Judicial System Arc"]
))

questions.append(make_q(
    "HB_H_038", "Constitutional Evolution",
    "Trace the evolutionary steps leading to the demand, acceptance, and formation of the Constituent Assembly of India:",
    "இந்திய அரசியலமைப்பு சபையின் கோரிக்கை, ஏற்பு மற்றும் உருவாக்கத்திற்கு வழிவகுத்த வரலாற்றுப் படிகளைக் கண்டறிக:",
    "1934 M.N. Roy proposed idea -> 1935 INC official demand -> 1940 August Offer (accepted demand in principle) -> 1942 Cripps Proposals (proposed fully Indian Assembly post-WWII) -> 1946 Cabinet Mission Plan (constituted Assembly in Nov 1946).",
    "1934 எம்.என். ராய் யோசனை -> 1935 காங்கிரஸ் அதிகாரப்பூர்வ கோரிக்கை -> 1940 ஆகஸ்ட் சலுகை (கொள்கையளவில் ஏற்பு) -> 1942 கிரிப்ஸ் தூதுக்குழு (போருக்குப் பின் சபை) -> 1946 கேபினட் மிஷன் திட்டம் (நவம்பர் 1946 இல் சபை உருவாக்கம்).",
    "1919 Montagu proposal -> 1928 Nehru Report -> 1947 Independence Act.",
    "1919 மாண்டேகு திட்டம் -> 1928 நேரு அறிக்கை -> 1947 சுதந்திரச் சட்டம்.",
    "1858 Crown Proclamation -> 1909 Morley Minto -> 1946 Assembly.",
    "1858 விக்டோரியா அறிக்கை -> 1909 மோர்லே மிண்டோ -> 1946 சபை.",
    "1773 Regulating Act -> 1935 GOI Act -> 1946 Assembly.",
    "1773 ஒழுங்குமுறைச் சட்டம் -> 1935 அரசுச் சட்டம் -> 1946 சபை.",
    "A",
    "Assembly Evolution: M.N. Roy (1934) -> INC Official Demand (1935) -> August Offer 1940 (British accepted in principle) -> Cripps Mission 1942 (Draft proposal) -> Cabinet Mission Plan 1946 (Under which Constituent Assembly was actually formed in Nov 1946).",
    "சபை வளர்ச்சி: எம்.என். ராய் (1934) -> காங்கிரஸ் கோரிக்கை (1935) -> ஆகஸ்ட் சலுகை (1940) -> கிரிப்ஸ் தூதுக்குழு (1942) -> கேபினட் மிஷன் திட்டம் (1946 - சபை உருவானது).",
    "Correct. Traces sequence from M.N. Roy (1934) to Cabinet Mission Plan (1946).",
    "சரி. 1934 எம்.என். ராய் முதல் 1946 கேபினட் மிஷன் வரை சரியான வளர்ச்சிப் பாதையைத் தருகிறது.",
    "Incorrect. Omits M.N. Roy, August Offer, Cripps, Cabinet Mission.",
    "தவறு. முக்கிய மைல்கல்களை விடுவிக்கிறது.",
    "Incorrect. Wrong timeline.",
    "தவறு. தவறான காலக்கோடு.",
    "Incorrect. Wrong timeline.",
    "தவறு. தவறான காலக்கோடு.",
    "First meeting of Constituent Assembly was held on December 9, 1946; Dr. Sachchidananda Sinha was elected temporary President.",
    "அரசியலமைப்பு சபையின் முதல் கூட்டம் 1946 டிசம்பர் 9 அன்று நடந்தது; டாக்டர் சச்சிதானந்த சின்ஹா இடைக்காலத் தலைவரானார்.",
    "Objective Resolution moved by Jawaharlal Nehru on December 13, 1946; adopted unanimously on January 22, 1947.",
    "1946 டிசம்பர் 13 அன்று நேருவால் நோக்குத் தீர்மானம் முன்வைக்கப்பட்டு, 1947 ஜனவரி 22 இல் ஒருமனதாக ஏற்றுக்கொள்ளப்பட்டது.",
    "Analyze", 75, ["Polity", "Historical Background", "Constitutional Evolution", "Constituent Assembly Arc"]
))

questions.append(make_q(
    "HB_H_039", "Constitutional Evolution",
    "How did Emergency Provisions in the present Indian Constitution evolve from the Government of India Act 1935?",
    "தற்போதைய இந்திய அரசியலமைப்பில் உள்ள அவசரக்கால விதிகள் 1935 இந்திய அரசுச் சட்டத்திலிருந்து எவ்வாறு வளர்ச்சி அடைந்தன?",
    "Section 93 of GOI Act 1935 (Governor taking over provincial administration in breakdown of constitutional machinery) evolved into Article 356 (President's Rule), and Section 45 (Federal emergency) evolved into Article 352 (National Emergency).",
    "1935 சட்டத்தின் பிரிவு 93 (அரசியலமைப்பு இயந்திரம் முறிந்தால் ஆளுநர் ஆட்சி) பிரிவு 356 ஆகவும் (குடியரசுத் தலைவர் ஆட்சி), பிரிவு 45 (கூட்டாட்சி அவசரநிலை) பிரிவு 352 ஆகவும் (தேசிய அவசரநிலை) வளர்ச்சியடைந்தன.",
    "Emergency powers were completely created fresh in 1950 with no colonial precedent.",
    "அவசரகால அதிகாரங்கள் 1950 இல் எந்தவொரு காலனித்துவ முன்னுதாரணமும் இன்றி முற்றிலும் புதிதாக உருவாக்கப்பட்டன.",
    "Section 93 was derived from the Regulating Act 1773.",
    "பிரிவு 93 என்பது 1773 ஒழுங்குமுறைச் சட்டத்திலிருந்து பெறப்பட்டது.",
    "Emergency provisions were copied from the US Constitution 1787.",
    "அவசரகால விதிகள் 1787 அமெரிக்க அரசியலமைப்பிலிருந்து நகலெடுக்கப்பட்டன.",
    "A",
    "The 1935 Act empowered Provincial Governors under Section 93 to assume all executive and legislative powers if provincial government could not be carried on in accordance with the Act. This directly became Article 356 (State Emergency / President's Rule).",
    "1935 சட்டத்தின் பிரிவு 93 மாகாண அரசால் நிர்வாகத்தைச் செய்ய முடியாத போது ஆளுநரே அதிகாரங்களை ஏற்க வழிவகுத்தது. இதுவே 1950 அரசியலமைப்பின் பிரிவு 356 (ஆளுநர்/குடியரசுத் தலைவர் ஆட்சி) ஆக உருவெடுத்தது.",
    "Correct. Section 93 of 1935 Act directly evolved into Article 356 (President's Rule).",
    "சரி. 1935 சட்டத்தின் பிரிவு 93 நேரடியாக பிரிவு 356 (குடியரசுத் தலைவர் ஆட்சி) ஆக உருவானது.",
    "Incorrect. Colonial precedent existed in 1935 Act.",
    "தவறு. 1935 சட்டத்தில் முன்னுதாரணம் இருந்தது.",
    "Incorrect. 1773 Act had no emergency takeover provisions.",
    "தவறு. 1773 சட்டத்தில் அவசரகால ஆட்சி விதிகள் இல்லை.",
    "Incorrect. Suspension of Fundamental Rights during Emergency was borrowed from Weimar Constitution of Germany, while administrative blueprint came from 1935 Act.",
    "தவறு. அடிப்படை உரிமைகள் இடைநிறுத்தம் ஜெர்மனி வைமர் அரசியலமைப்பிலிருந்து பெறப்பட்டது, நிர்வாக கட்டமைப்பு 1935 சட்டத்திலிருந்து வந்தது.",
    "Part XVIII of Indian Constitution contains Emergency Provisions (Articles 352 to 360).",
    "இந்திய அரசியலமைப்பின் பகுதி XVIII அவசரகால விதிகளைக் கொண்டுள்ளது (பிரிவுகள் 352 முதல் 360 வரை).",
    "Financial Emergency (Article 360) is also inspired by Executive control provisions of the 1935 Act.",
    "நிதி அவசரநிலை (பிரிவு 360) 1935 சட்டத்தின் நிர்வாகக் கட்டுப்பாட்டு விதிகளால் ஈர்க்கப்பட்டது.",
    "Analyze", 75, ["Polity", "Historical Background", "Constitutional Evolution", "Emergency Provisions Arc"]
))

questions.append(make_q(
    "HB_H_040", "Constitutional Evolution",
    "Trace the historical progression of the conceptual bifurcation between Rights (Part III) and Directive Principles (Part IV) in the Indian Constitution:",
    "இந்திய அரசியலமைப்பில் உரிமைகள் (பகுதி III) மற்றும் வழிகாட்டுதல் கோட்பாடுகள் (பகுதி IV) இடையிலான கருத்துருப் பிரிவின் வரலாற்று வளர்ச்சியைக் கண்டறிக:",
    "1928 Nehru Report demanded fundamental rights -> 1931 Karachi Resolution drafted socio-economic rights -> 1945 Sapru Committee formally divided rights into Justiciable (enforceable by courts) and Non-Justiciable, culminating in Part III and Part IV of 1950 Constitution.",
    "1928 நேரு அறிக்கை அடிப்படை உரிமைகளைக் கோரியது -> 1931 கராச்சி தீர்மானம் சமூக-பொருளாதார உரிமைகளை வரைந்தது -> 1945 சப்ரூ குழு உரிமைகளை நீதிமன்றத்தால் அமல்படுத்தக்கூடியவை (Justiciable) மற்றும் அமல்படுத்த முடியாதவை எனப் பிரித்தது, இதுவே 1950 அரசியலமைப்பின் பகுதி III மற்றும் பகுதி IV ஆக அமைந்தது.",
    "GOI Act 1935 created Fundamental Rights and Directive Principles in 1935.",
    "1935 இந்திய அரசுச் சட்டம் 1935 இல் அடிப்படை உரிமைகள் மற்றும் வழிகாட்டுதல் கோட்பாடுகளை உருவாக்கியது.",
    "Charter Act 1853 introduced Directive Principles for British servants.",
    "1853 சாசனச் சட்டம் பிரிட்டிஷ் ஊழியர்களுக்கான வழிகாட்டுதல் கோட்பாடுகளை அறிமுகப்படுத்தியது.",
    "Indian Independence Act 1947 made all rights non-justiciable.",
    "1947 இந்திய சுதந்திரச் சட்டம் அனைத்து உரிமைகளையும் நீதிமன்றத்தால் அமல்படுத்த முடியாதவைகளாக மாற்றியது.",
    "A",
    "The division of rights into Justiciable (Fundamental Rights - Part III) and Non-justiciable (DPSP - Part IV) was recommended by Sir Tej Bahadur Sapru Committee in 1945. Earlier, 1928 Nehru Report and 1931 Karachi Resolution had articulated these rights.",
    "1945 இல் சர் தேஜ் பகதூர் சப்ரு குழு உரிமைகளை நீதிமன்றத்தால் அமல்படுத்தக்கூடியவை (அடிப்படை உரிமைகள்) மற்றும் அமல்படுத்த முடியாதவை (வழிகாட்டுதல் கோட்பாடுகள்) எனப் பிரிக்கப் பரிந்துரைத்தது.",
    "Correct. Traces evolution from Nehru Report (1928) -> Karachi Resolution (1931) -> Sapru Committee (1945) -> Parts III & IV (1950).",
    "சரி. 1928 நேரு அறிக்கை -> 1931 கராச்சி தீர்மானம் -> 1945 சப்ரூ குழு -> 1950 பகுதி III & IV எனச் சரியான பாதையைக் காட்டுகிறது.",
    "Incorrect. GOI Act 1935 did NOT include Fundamental Rights or DPSPs (Joint Parliamentary Committee rejected them).",
    "தவறு. 1935 சட்டத்தில் அடிப்படை உரிமைகள் சேர்க்கப்படவில்லை.",
    "Incorrect. 1853 Act had no provisions for rights.",
    "தவறு. 1853 சட்டத்தில் உரிமைகள் விதிகள் இல்லை.",
    "Incorrect. 1947 Act dealt with partition and transfer of power.",
    "தவறு. 1947 சட்டம் அதிகார மாற்றத்தைப் பற்றியது.",
    "TNPSC Fact: The Joint Select Committee of British Parliament rejected inclusion of Fundamental Rights in GOI Act 1935 because they were considered unenforceable declarations.",
    "TNPSC செய்தி: பிரிட்டிஷ் பாராளுமன்றக் குழு 1935 சட்டத்தில் அடிப்படை உரிமைகளைச் சேர்க்க மறுத்தது, ஏனெனில் அவை அமல்படுத்த முடியாத பிரகடனங்களாகக் கருதப்பட்டன.",
    "B.N. Rau (Constitutional Advisor) also advocated for two categories of rights based on Irish Constitution precedent.",
    "பி.என். ராவ் (அரசியலமைப்பு ஆலோசகர்) ஐரிஷ் அரசியலமைப்பு மாதிரியில் இருவகையான உரிமைகளைப் பரிந்துரைத்தார்.",
    "Analyze", 75, ["Polity", "Historical Background", "Constitutional Evolution", "Rights Bifurcation Arc"]
))

# ---------------------------------------------------------
# 5 MULTI-ACT COMPARISON QUESTIONS (HB_H_041 to HB_H_045)
# ---------------------------------------------------------

questions.append(make_q(
    "HB_H_041", "Multi-Act Comparison",
    "Comparing Pitt's India Act of 1784 and the Government of India Act 1858, what was the core structural shift in supreme administrative oversight over India?",
    "1784 பிட் இந்தியச் சட்டத்தையும் 1858 இந்திய அரசுச் சட்டத்தையும் ஒப்பிடுகையில், இந்திய நிர்வாகத்தின் உச்சகட்ட மேற்பார்வையில் ஏற்பட்ட மையக் கட்டமைப்பு மாற்றம் யாது?",
    "Pitt's India Act 1784 established Double Government (Court of Directors for commerce, Board of Control for political affairs), whereas GOI Act 1858 abolished BOTH bodies and vested supreme authority in the Secretary of State for India assisted by a 15-member Council of India.",
    "1784 பிட் சட்டம் இரட்டை நிர்வாகத்தை (வர்த்தகத்திற்கு இயக்குநர்கள் அவை, அரசியலுக்கு கட்டுப்பாட்டு வாரியம்) நிறுவியது, ஆனால் 1858 அரசுச் சட்டம் இரண்டையும் ஒழித்து 15 உறுப்பினர்கள் கொண்ட இந்திய கவுன்சிலுடன் கூடிய இந்திய அரசுச் செயலாளரிடம் உச்ச அதிகாரத்தை ஒப்படைத்தது.",
    "Pitt's India Act created the Viceroy, while the 1858 Act created the Governor-General.",
    "பிட் இந்தியச் சட்டம் வைஸ்ராயை உருவாக்கியது, 1858 சட்டம் கவர்னர் ஜெனரலை உருவாக்கியது.",
    "Pitt's India Act introduced Dyarchy in provinces, while the 1858 Act introduced Provincial Autonomy.",
    "பிட் இந்தியச் சட்டம் மாகாண இரட்டை ஆட்சியை அறிமுகப்படுத்தியது, 1858 சட்டம் மாகாண தன்னாட்சியை அறிமுகப்படுத்தியது.",
    "Both Acts maintained identical administrative structures without any modification.",
    "இரண்டு சட்டங்களும் எந்த மாற்றமும் இன்றி ஒரே மாதிரியான நிர்வாகக் கட்டமைப்பைப் பராமரித்தன.",
    "A",
    "1784 Act created Dual Control (Court of Directors + Board of Control). 1858 Act abolished this Dual Control and replaced it with a single Cabinet minister (Secretary of State) assisted by Council of India, transitioning from Company to Crown rule.",
    "1784 சட்டம் இரட்டைக் கட்டுப்பாட்டை உருவாக்கியது. 1858 சட்டம் அவ்விரண்டையும் கலைத்து அரசுச் செயலாளர் மற்றும் இந்திய கவுன்சிலைக் கொண்டு கம்பெனி ஆட்சியை முடிஆட்சியாக்கியது.",
    "Correct. 1784 (Board of Control + Court of Directors) -> 1858 (Secretary of State + Council of India).",
    "சரி. 1784 (இரட்டை நிர்வாகம்) -> 1858 (அரசுச் செயலாளர் + இந்திய கவுன்சில்).",
    "Incorrect. Viceroy designation came in 1858, not 1784.",
    "தவறு. வைஸ்ராய் பட்டம் 1858 இல் வந்தது.",
    "Incorrect. Dyarchy came in 1919 and Autonomy in 1935.",
    "தவறு. இரட்டை ஆட்சி 1919 இலும் தன்னாட்சி 1935 இலும் வந்தன.",
    "Incorrect. Major structural overhaul occurred in 1858.",
    "தவறு. 1858 இல் பெரும் கட்டமைப்பு மாற்றம் நடந்தது.",
    "Secretary of State for India was a member of the British Cabinet and answerable to British Parliament.",
    "இந்திய அரசுச் செயலாளர் பிரிட்டிஷ் அமைச்சரவை உறுப்பினராகவும் பாராளுமன்றத்திற்குப் பொறுப்பானவராகவும் இருந்தார்.",
    "Expenses of Secretary of State and Council of India were charged on Indian revenues until 1919.",
    "அரசுச் செயலாளர் மற்றும் கவுன்சில் செலவுகள் 1919 வரை இந்திய வருவாயிலிருந்தே வழங்கப்பட்டன.",
    "Analyze", 75, ["Polity", "Historical Background", "Multi-Act Comparison", "1784 vs 1858 Oversights"]
))

questions.append(make_q(
    "HB_H_042", "Multi-Act Comparison",
    "Comparing the Governor-General's Council under the Charter Act of 1833 and the Charter Act of 1853, which option correctly contrasts their composition and functional specialization?",
    "1833 சாசனச் சட்டம் மற்றும் 1853 சாசனச் சட்டத்தின் கீழ் கவர்னர் ஜெனரல் கவுன்சிலை ஒப்பிடுகையில், அவற்றின் கட்டமைப்பு மற்றும் பணிச் சிறப்புத் தன்மையை சரியாக வேறுபடுத்தும் விருப்பம் எது?",
    "The 1833 Act added a Law Member (Macaulay) for executive law drafting without full voting rights initially, whereas the 1853 Act created a separate 6-member Legislative Council distinguishing legislative work from executive governance.",
    "1833 சட்டம் சட்ட வரைவுக்காக வாக்களிக்கும் உரிமையற்ற ஒரு சட்ட உறுப்பினரைத் (மெக்காலே) சேர்த்தது, ஆனால் 1853 சட்டம் நிர்வாக நிர்வாகத்திலிருந்து சட்டமன்றப் பணியைப் பிரித்து 6 உறுப்பினர்களைக் கொண்ட தனி சட்டமன்ற கவுன்சிலை உருவாக்கியது.",
    "The 1833 Act created a 60-member council, while the 1853 Act reduced it to 4 members.",
    "1833 சட்டம் 60 உறுப்பினர்கள் கொண்ட கவுன்சிலை உருவாக்கியது, 1853 சட்டம் அதை 4 உறுப்பினர்களாகக் குறைத்தது.",
    "The 1833 Act introduced elected Indian members, while the 1853 Act removed all Indians.",
    "1833 சட்டம் தேர்ந்தெடுக்கப்பட்ட இந்திய உறுப்பினர்களை அறிமுகப்படுத்தியது, 1853 சட்டம் அனைத்து இந்தியர்களையும் நீக்கியது.",
    "Both Acts maintained identical executive council structures without legislative separation.",
    "இரண்டு சட்டங்களும் சட்டமன்றப் பிரிவின்றி ஒரே மாதிரியான நிர்வாகக் குழு கட்டமைப்பைப் பராமரித்தன.",
    "A",
    "1833 Charter Act introduced Macaulay as 4th Law Member in Executive Council. 1853 Charter Act separated legislative and executive functions by adding 6 new legislative members (Legislative Councillors), forming the Indian Legislative Council.",
    "1833 சாசனச் சட்டம் மெக்காலேயை 4வது சட்ட உறுப்பினராகச் சேர்த்தது. 1853 சாசனச் சட்டம் 6 புதிய சட்டமன்ற உறுப்பினர்களைச் சேர்த்து சட்டமன்ற மற்றும் நிர்வாகப் பணிகளைப் பிரித்தது.",
    "Correct. 1833 introduced Law Member into Executive Council; 1853 created separate Legislative Council.",
    "சரி. 1833 இல் சட்ட உறுப்பினர் சேர்க்கப்பட்டார்; 1853 இல் தனி சட்டமன்ற கவுன்சில் உருவாக்கப்பட்டது.",
    "Incorrect. Council size expansion to 60 happened in 1909.",
    "தவறு. 60 உறுப்பினர்களாக உயர்த்தப்பட்டது 1909 இல்.",
    "Incorrect. Neither Act had elected Indian members.",
    "தவறு. எந்தச் சட்டத்திலும் தேர்ந்தெடுக்கப்பட்ட இந்திய உறுப்பினர்கள் இல்லை.",
    "Incorrect. 1853 Act explicitly separated legislative and executive functions.",
    "தவறு. 1853 சட்டம் சட்டமன்ற/நிர்வாகப் பணிகளைப் பிரித்தது.",
    "1853 Act introduced local representation in Central Legislative Council (4 of 6 members from Madras, Bombay, Bengal, Agra local governments).",
    "1853 சட்டம் மத்திய சட்டமன்ற கவுன்சிலில் உள்ளூர் பிரதிநிதித்துவத்தை (மதராஸ், பம்பாய், வங்காளம், ஆக்ரா) அறிமுகப்படுத்தியது.",
    "Macaulay Committee (1854) gave India its first open competitive civil service exam framework.",
    "மெக்காலே குழு (1854) இந்தியாவிற்கு முதல் திறந்தவெளிப் போட்டித் தேர்வு கட்டமைப்பை வழங்கியது.",
    "Analyze", 75, ["Polity", "Historical Background", "Multi-Act Comparison", "1833 vs 1853 Councils"]
))

questions.append(make_q(
    "HB_H_043", "Multi-Act Comparison",
    "Comparing the Indian Councils Act 1909 (Morley-Minto) and the Government of India Act 1919 (Montagu-Chelmsford), which statement accurately contrasts their provisions regarding communal electorates and budgetary powers?",
    "1909 இந்தியக் கவுன்சில்கள் சட்டத்தையும் 1919 இந்திய அரசுச் சட்டத்தையும் ஒப்பிடுகையில், வகுப்புவாதத் தொகுதிகள் மற்றும் வரவு செலவுத் திட்ட அதிகாரங்கள் குறித்த அவற்றின் விதிகளைச் சரியாக வேறுபடுத்தும் கூற்று எது?",
    "The 1909 Act introduced separate electorates for Muslims only and allowed members to ask supplementary questions and move budget resolutions without voting, whereas the 1919 Act extended separate electorates to Sikhs, Christians, Anglo-Indians, and Europeans, and granted the right to vote on demands for grants.",
    "1909 சட்டம் முஸ்லிம்களுக்கு மட்டுமே தனித் தொகுதியை அறிமுகப்படுத்தியதுடன் வாக்களிப்பன்றி துணைக் கேள்விகள் கேட்கவும் பட்ஜெட் தீர்மானங்கள் கொண்டு வரவும் அனுமதித்தது, ஆனால் 1919 சட்டம் சீக்கியர்கள், கிறிஸ்தவர்கள், ஆங்கிலோ-இந்தியர்கள், ஐரோப்பியர்களுக்குத் தனித் தொகுதியை விரிவுபடுத்தியதுடன் மானியக் கோரிக்கைகள் மீது வாக்களிக்கும் உரிமையையும் வழங்கியது.",
    "The 1909 Act granted full voting rights on the budget, while the 1919 Act withdrew budget discussion completely.",
    "1909 சட்டம் பட்ஜெட் மீது முழு வாக்களிக்கும் உரிமையை வழங்கியது, 1919 சட்டம் பட்ஜெட் விவாதத்தையே முற்றிலும் திரும்பப் பெற்றது.",
    "The 1909 Act extended communal electorates to all minorities, while the 1919 Act restricted it to Muslims.",
    "1909 சட்டம் அனைத்து சிறுபான்மையினருக்கும் வகுப்புவாதத் தொகுதியை விரிவுபடுத்தியது, 1919 சட்டம் அதை முஸ்லிம்களுக்கு மட்டுமே கட்டுப்படுத்தியது.",
    "Both Acts provided identical budgetary voting powers and communal representation rules.",
    "இரண்டு சட்டங்களும் ஒரே மாதிரியான பட்ஜெட் வாக்களிக்கும் அதிகாரங்களையும் வகுப்புவாத பிரதிநிதித்துவ விதிகளையும் வழங்கின.",
    "A",
    "1909 Act: Separate electorate for Muslims only; budget discussion, supplementary questions & resolutions allowed (no voting on grants). 1919 Act: Extended separate electorates to Sikhs, Indian Christians, Anglo-Indians, Europeans; members granted right to vote on demands for grants (70% of budget).",
    "1909 சட்டம்: முஸ்லிம்களுக்கு மட்டும் தனித் தொகுதி; துணைக் கேள்விகள்/தீர்மானங்கள் (வாக்களிப்பு இல்லை). 1919 சட்டம்: சீக்கியர்கள், கிறிஸ்தவர்கள், ஆங்கிலோ-இந்தியர்கள், ஐரோப்பியர்களுக்கு விரிவு; மானியக் கோரிக்கைகள் மீது வாக்களிப்பு உரிமை.",
    "Correct. 1909 (Muslim electorate only + non-voting budget resolutions) vs 1919 (Extended electorates + Voting on demands for grants).",
    "சரி. 1909 (முஸ்லிம் தனித் தொகுதி + வாக்களிப்பற்ற பட்ஜெட் தீர்மானம்) vs 1919 (விரிவாக்கப்பட்ட தொகுதிகள் + மானியக் கோரிக்கை வாக்களிப்பு).",
    "Incorrect. Voting on budget demands was introduced in 1919, not 1909.",
    "தவறு. பட்ஜெட் வாக்களிப்பு 1919 இல் வந்தது, 1909 இல் அல்ல.",
    "Incorrect. 1909 was Muslims only; 1919 expanded to Sikhs/Christians/etc.",
    "தவறு. 1909 முஸ்லிம்களுக்கு மட்டுமே; 1919 விரிவாக்கப்பட்டது.",
    "Incorrect. Significant expansion occurred in 1919.",
    "தவறு. 1919 இல் குறிப்பிடத்தக்க விரிவாக்கம் நடந்தது.",
    "1919 Act also separated Provincial Budgets from Central Budget for the first time.",
    "1919 சட்டம் முதன்முறையாக மாகாண வரவு செலவுத் திட்டத்தை மத்திய வரவு செலவுத் திட்டத்திலிருந்து பிரித்தது.",
    "1919 Act introduced Bicameralism at the Centre (Council of State and Legislative Assembly).",
    "1919 சட்டம் மத்திய சட்டமன்றத்தில் ஈரவை முறையை அறிமுகப்படுத்தியது.",
    "Analyze", 75, ["Polity", "Historical Background", "Multi-Act Comparison", "1909 vs 1919 Progression"]
))

questions.append(make_q(
    "HB_H_044", "Multi-Act Comparison",
    "Contrasting the mechanism of Dyarchy as introduced under the Government of India Act 1919 with its proposed structure under the Government of India Act 1935, which statement is historically accurate?",
    "1919 இந்திய அரசுச் சட்டத்தின் கீழ் அறிமுகப்படுத்தப்பட்ட இரட்டை ஆட்சியின் நுட்பத்தையும் 1935 இந்திய அரசுச் சட்டத்தின் கீழ் உத்தேசிக்கப்பட்ட அதன் கட்டமைப்பையும் ஒப்பிடுகையில், வரலாற்று ரீதியாக துல்லியமான கூற்று எது?",
    "The 1919 Act introduced Dyarchy in Provinces (Reserved vs Transferred subjects), which was abolished by the 1935 Act and replaced with Provincial Autonomy, while the 1935 Act proposed Dyarchy at the Centre (Reserved: Defense, External Affairs, Ecclesiastical vs Transferred), though Central Dyarchy never came into operation.",
    "1919 சட்டம் மாகாணங்களில் இரட்டை ஆட்சியை (ஒதுக்கப்பட்டவை vs மாற்றப்பட்டவை) கொண்டுவந்தது, இது 1935 சட்டத்தால் ஒழிக்கப்பட்டு மாகாண தன்னாட்சி வந்தது, அதே வேளையில் 1935 சட்டம் மத்தியில் இரட்டை ஆட்சியை உத்தேசித்தது (ஒதுக்கப்பட்டவை: பாதுகாப்பு, வெளியுறவு vs மாற்றப்பட்டவை), ஆனால் மத்திய இரட்டை ஆட்சி நடைமுறைக்கு வரவில்லை.",
    "The 1919 Act introduced Dyarchy at the Centre, while the 1935 Act introduced Dyarchy in the Supreme Court.",
    "1919 சட்டம் மத்தியில் இரட்டை ஆட்சியை அறிமுகப்படுத்தியது, 1935 சட்டம் உச்ச நீதிமன்றத்தில் இரட்டை ஆட்சியை அறிமுகப்படுத்தியது.",
    "The 1919 Act abolished Dyarchy in all territories, while the 1935 Act re-introduced it in Madras only.",
    "1919 சட்டம் அனைத்து பகுதிகளிலும் இரட்டை ஆட்சியை ஒழித்தது, 1935 சட்டம் மதராஸில் மட்டுமே அதை மீண்டும் கொண்டுவந்தது.",
    "Both Acts successfully operated Dyarchy at both Central and Provincial levels simultaneously.",
    "இரண்டு சட்டங்களும் ஒரே நேரத்தில் மத்திய மற்றும் மாகாண மட்டங்களில் இரட்டை ஆட்சியை வெற்றிகரமாக இயக்கின.",
    "A",
    "1919 GOI Act: Dyarchy implemented in 8 Provinces. 1935 GOI Act: Abolished Provincial Dyarchy (established Provincial Autonomy) and proposed Dyarchy at Centre (Reserved: Defense, External Affairs, Ecclesiastical, Tribal vs Transferred). Central Dyarchy was never brought into force.",
    "1919 சட்டம்: 8 மாகாணங்களில் இரட்டை ஆட்சி. 1935 சட்டம்: மாகாண இரட்டை ஆட்சி ஒழிப்பு (மாகாண தன்னாட்சி அமல்) மற்றும் மத்தியில் இரட்டை ஆட்சி உத்தேசம் (பாதுகாப்பு, வெளியுறவு ஒதுக்கப்பட்டவை). மத்திய இரட்டை ஆட்சி அமலாகவில்லை.",
    "Correct. 1919 = Provincial Dyarchy implemented; 1935 = Provincial Autonomy implemented + Central Dyarchy proposed (never operated).",
    "சரி. 1919 = மாகாண இரட்டை ஆட்சி அமல்; 1935 = மாகாண தன்னாட்சி அமல் + மத்தியில் இரட்டை ஆட்சி உத்தேசம்.",
    "Incorrect. Dyarchy in 1919 was in Provinces, not Centre.",
    "தவறு. 1919 இல் இரட்டை ஆட்சி மாகாணங்களில் இருந்தது.",
    "Incorrect. Dyarchy was created in 1919, not abolished.",
    "தவறு. 1919 இல் இரட்டை ஆட்சி உருவாக்கப்பட்டது.",
    "Incorrect. Central Dyarchy under 1935 Act never came into operation.",
    "தவறு. 1935 சட்டத்தின் மத்திய இரட்டை ஆட்சி அமலுக்கு வரவில்லை.",
    "Under 1935 Act, Provincial Autonomy came into force in 1937 and was suspended in 1939 due to Congress resignations.",
    "1935 சட்டத்தில் மாகாண தன்னாட்சி 1937 இல் அமலுக்கு வந்தது, 1939 இல் காங்கிரஸ் ராஜினாமாவால் நிறுத்தப்பட்டது.",
    "Dyarchy is derived from Greek word 'di-arche' meaning double rule.",
    "டைஆர்க்கி என்ற சொல் கிரேக்க சொல்லிலிருந்து வந்தது, இதன் பொருள் இரட்டை ஆட்சி.",
    "Analyze", 75, ["Polity", "Historical Background", "Multi-Act Comparison", "Dyarchy 1919 vs 1935 Shifts"]
))

questions.append(make_q(
    "HB_H_045", "Multi-Act Comparison",
    "Comparing the executive powers of the Governor-General of India under the Government of India Act 1919, Government of India Act 1935, and Indian Independence Act 1947, which option correctly outlines his functional transformation?",
    "1919 இந்திய அரசுச் சட்டம், 1935 இந்திய அரசுச் சட்டம் மற்றும் 1947 இந்திய சுதந்திரச் சட்டத்தின் கீழ் இந்திய கவர்னர் ஜெனரலின் நிர்வாக அதிகாரங்களை ஒப்பிடுகையில், அவரது பணி மாற்றத்தை சரியாக விவரிக்கும் விருப்பம் எது?",
    "Under 1919 and 1935 Acts, the Governor-General exercised autocratic veto, ordinance, and certification powers answerable to Secretary of State, whereas under the 1947 Act, he became a purely constitutional nominal head acting on advice of Indian Ministers.",
    "1919 மற்றும் 1935 சட்டங்களின் கீழ் கவர்னர் ஜெனரல் அரசுச் செயலாளருக்குப் பொறுப்பான தன்னிச்சையான நிராகரிப்பு (veto), அவசரச்சட்டம் மற்றும் சான்றளிக்கும் அதிகாரங்களைப் பயன்படுத்தினார், ஆனால் 1947 சட்டத்தின் கீழ் இந்திய அமைச்சர்களின் ஆலோசனையின்படி செயல்படும் தூய அரசியலமைப்பு பெயரளவு தலைவரானார்.",
    "Under 1919 Act he was a nominal head, but under 1947 Act he became an absolute dictator.",
    "1919 சட்டத்தில் அவர் பெயரளவு தலைவராக இருந்தார், ஆனால் 1947 சட்டத்தில் அவர் ஒரு முழுமையான சர்வாதிகாரியானார்.",
    "Under 1935 Act he lost all ordinance powers, which were restored in 1947.",
    "1935 சட்டத்தில் அவர் அனைத்து அவசரச்சட்ட அதிகாரங்களையும் இழந்தார், அவை 1947 இல் மீட்கப்பட்டன.",
    "His executive powers remained completely unchanged across all three Acts.",
    "மூன்று சட்டங்களிலும் அவரது நிர்வாக அதிகாரங்கள் எந்த மாற்றமும் இன்றி அப்படியே இருந்தன.",
    "A",
    "Under 1919 and 1935 Acts, Governor-General (Viceroy) retained discretion, individual judgment, veto powers, and certification over legislation. The 1947 Independence Act stripped these discretionary powers, converting GG into a constitutional nominal head bound by Council of Ministers.",
    "1919 மற்றும் 1935 சட்டங்களில் கவர்னர் ஜெனரல் (வைஸ்ராய்) தன்னிச்சையான நிராகரிப்பு மற்றும் சான்றளிக்கும் அதிகாரங்களைக் கொண்டிருந்தார். 1947 சுதந்திரச் சட்டம் இத்தன்னிச்சை அதிகாரங்களை நீக்கி அவரை அமைச்சரவைக்குக் கட்டுப்பட்ட பெயரளவு தலைவராக்கியது.",
    "Correct. Autocratic executive head under 1919/1935 -> Nominal constitutional head under 1947 Act.",
    "சரி. 1919/1935 இல் தன்னிச்சை நிர்வாகத் தலைவர் -> 1947 இல் பெயரளவு அரசியலமைப்புத் தலைவர்.",
    "Incorrect. 1947 Act made him constitutional head, not dictator.",
    "தவறு. 1947 சட்டம் அவரை பெயரளவு தலைவராக்கியது.",
    "Incorrect. Ordinance power was available in 1935 Act.",
    "தவறு. 1935 சட்டத்தில் அவசரச்சட்ட அதிகாரம் இருந்தது.",
    "Incorrect. Transformation from real executive to nominal head was complete in 1947.",
    "தவறு. 1947 இல் உண்மையான தலைவரிலிருந்து பெயரளவு தலைவராக மாறினார்.",
    "Indian Independence Act 1947 abolished the British Cabinet office of Secretary of State for India.",
    "1947 இந்திய சுதந்திரச் சட்டம் பிரிட்டிஷ் அமைச்சரவையின் இந்திய அரசுச் செயலாளர் பதவியை ரத்து செய்தது.",
    "Lord Mountbatten served as the first Governor-General of independent India (Aug 1947 - June 1948).",
    "சுதந்திர இந்தியாவின் முதல் கவர்னர் ஜெனரலாக மவுண்ட்பேட்டன் பிரபு (1947 ஆகஸ்ட் - 1948 ஜூன்) இருந்தார்.",
    "Analyze", 75, ["Polity", "Historical Background", "Multi-Act Comparison", "Governor-General Powers Transformation"]
))

# ---------------------------------------------------------
# 5 INTEGRATED ANALYTICAL QUESTIONS (HB_H_046 to HB_H_050)
# ---------------------------------------------------------

questions.append(make_q(
    "HB_H_046", "Integrated Analytical",
    "Analyze the integrated historical trajectory of Financial Autonomy and Budgetary Control in British India from 1861 to 1935. Which option correctly synthesizes this legislative progression?",
    "1861 முதல் 1935 வரை பிரிட்டிஷ் இந்தியாவில் நிதி தன்னாட்சி மற்றும் வரவு செலவுத் திட்டக் கட்டுப்பாட்டின் ஒருங்கிணைந்த வரலாற்றுப் பாதையை பகுப்பாய்வு செய்க. இந்தச் சட்ட வளர்ச்சியைச் சரியாக ஒருங்கிணைக்கும் விருப்பம் எது?",
    "1861 Act prohibited budget discussion -> 1892 Act allowed budget discussion without voting -> 1909 Act allowed supplementary questions and budget resolutions -> 1919 Act introduced voting on grant demands and separated Provincial Budgets -> 1935 Act established full provincial financial autonomy.",
    "1861 சட்டம் பட்ஜெட் விவாதத்தைத் தடுத்தது -> 1892 சட்டம் வாக்களிப்பின்றி பட்ஜெட் விவாதத்தை அனுமதித்தது -> 1909 சட்டம் துணைக் கேள்விகள் & பட்ஜெட் தீர்மானங்களை அனுமதித்தது -> 1919 சட்டம் மானியக் கோரிக்கை வாக்களிப்பை அறிமுகப்படுத்தி மாகாண பட்ஜெட்டைப் பிரித்தது -> 1935 சட்டம் முழு மாகாண நிதி தன்னாட்சியை நிறுவியது.",
    "1861 Act granted full voting on budget -> 1935 Act abolished all budget discussions.",
    "1861 சட்டம் பட்ஜெட் மீது முழு வாக்களிப்பை வழங்கியது -> 1935 சட்டம் அனைத்து பட்ஜெட் விவாதங்களையும் ஒழித்தது.",
    "1892 Act separated Central and Provincial budgets -> 1919 Act merged them back.",
    "1892 சட்டம் மத்திய மற்றும் மாகாண பட்ஜெட்களைப் பிரித்தது -> 1919 சட்டம் அவற்றை மீண்டும் இணைத்தது.",
    "Financial powers remained completely unevolved throughout British rule.",
    "பிரிட்டிஷ் ஆட்சி முழுவதும் நிதி அதிகாரங்கள் எந்த வளர்ச்சியும் அடையாமல் இருந்தன.",
    "A",
    "Financial Control Arc: 1861 (No budget discussion) -> 1892 (Discussion allowed, no voting) -> 1909 (Supplementary Qs & resolutions) -> 1919 (Voting on demands for grants & provincial budget separation) -> 1935 (Full Provincial Financial Autonomy).",
    "நிதி கட்டுப்பாட்டு வளர்ச்சி: 1861 (விவாதம் இல்லை) -> 1892 (விவாதம் மட்டும்) -> 1909 (துணைக் கேள்விகள் & தீர்மானங்கள்) -> 1919 (வாக்களிப்பு & மாகாண பட்ஜெட் பிரிப்பு) -> 1935 (முழு மாகாண நிதி தன்னாட்சி).",
    "Correct. Synthesizes the 5-stage evolutionary trajectory of financial control accurately.",
    "சரி. நிதி கட்டுப்பாட்டின் 5-கட்ட வரலாற்றுப் பாதையைத் துல்லியமாக ஒருங்கிணைக்கிறது.",
    "Incorrect. 1861 had no voting on budget.",
    "தவறு. 1861 இல் வாக்களிப்பு இல்லை.",
    "Incorrect. Provincial budget separation happened in 1919, not 1892.",
    "தவறு. மாகாண பட்ஜெட் பிரிப்பு 1919 இல் நடந்தது.",
    "Incorrect. Financial powers underwent steady progressive expansion.",
    "தவறு. நிதி அதிகாரங்கள் படிப்படியாக விரிவடைந்தன.",
    "First Indian Budget was presented on February 18, 1860 by James Wilson under Lord Canning's administration.",
    "1860 பிப்ரவரி 18 அன்று ஜேம்ஸ் வில்சனால் முதல் இந்திய பட்ஜெட் தாக்கல் செய்யப்பட்டது.",
    "Separation of Railway Budget from General Budget occurred in 1924 based on Acworth Committee recommendations (1920-21).",
    "1924 இல் அக்வொர்த் குழுப் பரிந்துரைப்படி இரயில்வே பட்ஜெட் பொது பட்ஜெட்டிலிருந்து பிரிக்கப்பட்டது.",
    "Analyze", 75, ["Polity", "Historical Background", "Integrated Analytical", "Financial Autonomy Arc"]
))

questions.append(make_q(
    "HB_H_047", "Integrated Analytical",
    "Analyze the structural pendulum of Administrative Centralization versus Decentralization in British India from 1773 to 1935:",
    "1773 முதல் 1935 வரை பிரிட்டிஷ் இந்தியாவில் நிர்வாக மத்தியமயமாக்கல் மற்றும் பரவலாக்கலின் கட்டமைப்பு மாற்றத்தைப் பகுப்பாய்வு செய்க:",
    "1773 Regulating Act initiated centralization -> 1833 Charter Act reached peak centralization (central monopoly) -> 1861 Indian Councils Act initiated legislative decentralization -> 1919 GOI Act classified central/provincial subjects -> 1935 GOI Act established full Provincial Autonomy.",
    "1773 ஒழுங்குமுறைச் சட்டம் மத்தியமயமாக்கலைத் தொடங்கியது -> 1833 சாசனச் சட்டம் உச்சக்கட்ட மத்தியமயமாக்கலை அடைந்தது -> 1861 இந்தியக் கவுன்சில்கள் சட்டம் சட்டமன்ற பரவலாக்கலைத் தொடங்கியது -> 1919 அரசுச் சட்டம் மத்திய/மாகாணத் துறைகளைப் பிரித்தது -> 1935 அரசுச் சட்டம் முழு மாகாண தன்னாட்சியை நிறுவியது.",
    "1773 Act gave full autonomy -> 1935 Act created total centralization.",
    "1773 சட்டம் முழு தன்னாட்சியை அளித்தது -> 1935 சட்டம் முழுமையான மத்தியமயமாக்கலை உருவாக்கியது.",
    "1833 Act created Provincial Autonomy -> 1861 Act abolished all provinces.",
    "1833 சட்டம் மாகாண தன்னாட்சியை உருவாக்கியது -> 1861 சட்டம் அனைத்து மாகாணங்களையும் கலைத்தது.",
    "Administrative structure remained static without any centralizing or decentralizing shifts.",
    "நிர்வாகக் கட்டமைப்பு மத்தியமயமாக்கல் அல்லது பரவலாக்கல் மாற்றங்களின்றி நிலையாக இருந்தது.",
    "A",
    "Centralization/Decentralization Arc: 1773 (Start of centralization) -> 1833 (Peak centralization: GG of India deprived Madras/Bombay of legislative powers) -> 1861 (Reversal: legislative powers restored to Bombay/Madras) -> 1919 (Subject classification) -> 1935 (Provincial Autonomy).",
    "மத்தியமயமாக்கல்/பரவலாக்கல் பாதை: 1773 (தொடக்கம்) -> 1833 (உச்சம்: பம்பாய்/மதராஸ் சட்ட அதிகாரம் பறிப்பு) -> 1861 (திருப்பம்: சட்ட அதிகாரம் மீட்பு) -> 1919 (துறைப் பிரிவு) -> 1935 (மாகாண தன்னாட்சி).",
    "Correct. Accurately synthesizes the structural evolution from 1773 centralization to 1935 provincial autonomy.",
    "சரி. 1773 மத்தியமயமாக்கலிலிருந்து 1935 மாகாண தன்னாட்சி வரையிலான கட்டமைப்பு மாற்றத்தைச் சரியாக ஒருங்கிணைக்கிறது.",
    "Incorrect. Reverse logic.",
    "தவறு. தலைகீழ் தர்க்கம்.",
    "Incorrect. 1833 was peak centralization, not autonomy.",
    "தவறு. 1833 உச்சகட்ட மத்தியமயமாக்கல் ஆகும்.",
    "Incorrect. Structural shifts were dynamic and progressive.",
    "தவறு. கட்டமைப்பு மாற்றங்கள் தீவிரமாக நடந்தன.",
    "Under 1935 Act, provinces acted as autonomous units of administration in their defined sphere.",
    "1935 சட்டத்தில் மாகாணங்கள் தங்கள் வரையறுக்கப்பட்ட துறையில் தன்னாட்சி நிர்வாக அலகுகளாகச் செயல்பட்டன.",
    "Provincial Autonomy came into effect in 1937 and saw Congress governments in 8 out of 11 provinces.",
    "மாகாண தன்னாட்சி 1937 இல் அமலுக்கு வந்து 11 இல் 8 மாகாணங்களில் காங்கிரஸ் ஆட்சியை அமைத்தது.",
    "Analyze", 75, ["Polity", "Historical Background", "Integrated Analytical", "Centralization Decentralization Pendulum"]
))

questions.append(make_q(
    "HB_H_048", "Integrated Analytical",
    "Analyze the multi-stage historical progression of Indianization of Executive and Legislative bodies in British India from 1861 to 1946:",
    "1861 முதல் 1946 வரை பிரிட்டிஷ் இந்தியாவில் நிர்வாக மற்றும் சட்டமன்ற அமைப்புகளில் இந்தியர்கள் சேர்க்கப்பட்டதன் பலகட்ட வரலாற்று வளர்ச்சியைப் பகுப்பாய்வு செய்க:",
    "1861 Act (3 non-official Indians nominated to Legislative Council) -> 1892 Act (Indirect election element for non-official seats) -> 1909 Act (First Indian S.P. Sinha in Viceroy's Executive Council) -> 1919 Act (3 out of 6 executive council members Indians) -> Sept 1946 (All-Indian Interim Government formed under Jawaharlal Nehru).",
    "1861 சட்டம் (சட்டமன்ற கவுன்சிலுக்கு 3 இந்தியர்கள் நியமனம்) -> 1892 சட்டம் (அரசுசாரா இடங்களுக்கு மறைமுகத் தேர்தல் கூறு) -> 1909 சட்டம் (வைஸ்ராய் நிர்வாகக் குழுவில் முதல் இந்தியர் எஸ்.பி. சின்ஹா) -> 1919 சட்டம் (நிர்வாகக் குழுவின் 6 இல் 3 பேர் இந்தியர்கள்) -> செப் 1946 (ஜவஹர்லால் நேரு தலைமையில் அனைத்து இந்தியர்கள் கொண்ட இடைக்கால அரசு).",
    "1861 Act (All members Indians) -> 1946 Act (All members British).",
    "1861 சட்டம் (அனைத்து உறுப்பினர்களும் இந்தியர்கள்) -> 1946 சட்டம் (அனைத்து உறுப்பினர்களும் பிரிட்டிஷார்).",
    "1909 Act (First Indian Prime Minister) -> 1946 Act (Abolished all Indian seats).",
    "1909 சட்டம் (முதல் இந்தியப் பிரதமர்) -> 1946 சட்டம் (அனைத்து இந்திய இடங்களும் ரத்து).",
    "Indianization occurred in a single step in 1947 without prior legislative milestones.",
    "முந்தைய சட்ட மைல்கற்களின்றி 1947 இல் ஒரே படியில் இந்தியர் சேர்க்கை நடந்தது.",
    "A",
    "Indianization Progression Arc: 1861 (First non-official Indian nominations by Canning: Raja of Benares, Maharaja of Patiala, Sir Dinkar Rao) -> 1892 (Indirect election recommendation) -> 1909 (S.P. Sinha in Executive Council) -> 1919 (3 of 6 Executive Council members Indians) -> Sept 1946 (Interim Cabinet formed).",
    "இந்தியர் சேர்க்கை பாதை: 1861 (முதல் நியமனங்கள்: காசி ராஜா, பாட்டியாலா மகாராஜா, சர் தினகர் ராவ்) -> 1892 (மறைமுகத் தேர்தல்) -> 1909 (நிர்வாகக் குழுவில் எஸ்.பி. சின்ஹா) -> 1919 (6 இல் 3 உறுப்பினர்கள்) -> செப் 1946 (இடைக்கால அமைச்சரவை).",
    "Correct. Accurately synthesizes the 5-stage Indianization trajectory from 1861 to 1946.",
    "சரி. 1861 முதல் 1946 வரையிலான 5-கட்ட இந்தியர் சேர்க்கைப் பாதையைத் துல்லியமாக ஒருங்கிணைக்கிறது.",
    "Incorrect. Reverse logic.",
    "தவறு. தலைகீழ் தர்க்கம்.",
    "Incorrect. No Indian Prime Minister in 1909.",
    "தவறு. 1909 இல் இந்தியப் பிரதமர் பதவி இல்லை.",
    "Incorrect. Indianization was a gradual multi-stage process over 85 years.",
    "தவறு. இந்தியர் சேர்க்கை 85 ஆண்டு காலப் படிப்படியான செயல்முறையாகும்.",
    "In 1946 Interim Government, Jawaharlal Nehru held Vice-President of Executive Council & External Affairs portfolio.",
    "1946 இடைக்கால அரசில் ஜவஹர்லால் நேரு நிர்வாகக் குழுவின் துணைத் தலைவராகவும் வெளியுறவுத்துறை அமைச்சராகவும் இருந்தார்.",
    "In 1919 Act, 3 out of 6 members of Viceroy's Executive Council (other than Commander-in-Chief) had to be Indian.",
    "1919 சட்டப்படி வைஸ்ராய் நிர்வாகக் குழுவின் 6 உறுப்பினர்களில் 3 பேர் (தளபதி தவிர) இந்தியர்களாக இருக்க வேண்டும்.",
    "Analyze", 75, ["Polity", "Historical Background", "Integrated Analytical", "Indianization Trajectory Arc"]
))

questions.append(make_q(
    "HB_H_049", "Integrated Analytical",
    "Analyze the structural evolution of Federal Division of Legislative Powers from colonial rule to the 7th Schedule of the 1950 Indian Constitution:",
    "காலனித்துவ ஆட்சியிலிருந்து 1950 இந்திய அரசியலமைப்பின் 7வது அட்டவணை வரையிலான சட்ட அதிகாரங்களின் கூட்டாட்சிப் பகிர்வின் கட்டமைப்பு வளர்ச்சியைப் பகுப்பாய்வு செய்க:",
    "1833 Charter Act (Total Central Legislative Monopoly) -> 1861 Indian Councils Act (Decentralization onset) -> 1919 GOI Act (Classification into Central and Provincial Subjects) -> 1935 GOI Act (3-List Scheme: Federal 59, Provincial 54, Concurrent 36; Residuary to Viceroy) -> 1950 Constitution (7th Schedule: Union, State, Concurrent Lists; Residuary to Parliament under Article 248).",
    "1833 சாசனச் சட்டம் (முழு மத்திய சட்ட ஏகபோகம்) -> 1861 இந்தியக் கவுன்சில்கள் சட்டம் (பரவலாக்கல் தொடக்கம்) -> 1919 அரசுச் சட்டம் (மத்திய/மாகாணத் துறைகள் வகைப்பாடு) -> 1935 அரசுச் சட்டம் (3 பட்டியல்கள்: கூட்டாட்சி 59, மாகாணம் 54, இணைப்பு 36; எஞ்சிய அதிகாரம் வைஸ்ராயிடம்) -> 1950 அரசியலமைப்பு (7வது அட்டவணை: மத்திய, மாநில, பொதுப் பட்டியல்கள்; எஞ்சிய அதிகாரம் பிரிவு 248 இல் பாராளுமன்றத்திடம்).",
    "1833 Act created 7th Schedule -> 1950 Constitution abolished all lists.",
    "1833 சட்டம் 7வது அட்டவணையை உருவாக்கியது -> 1950 அரசியலமைப்பு அனைத்துப் பட்டியல்களையும் ஒழித்தது.",
    "1919 Act gave Residuary powers to Supreme Court -> 1935 Act gave it to Municipalities.",
    "1919 சட்டம் எஞ்சிய அதிகாரங்களை உச்ச நீதிமன்றத்திற்கு அளித்தது -> 1935 சட்டம் அதை நகராட்சிகளுக்கு அளித்தது.",
    "Division of powers remained unchanged from 1773 Regulating Act to present day.",
    "அதிகாரப் பகிர்வு 1773 ஒழுங்குமுறைச் சட்டத்திலிருந்து இன்று வரை மாற்றமின்றி உள்ளது.",
    "A",
    "Division of Powers Arc: 1833 (Central monopoly) -> 1861 (Decentralization onset) -> 1919 (Central/Provincial Subject classification) -> 1935 (3 Lists with Residuary to Viceroy) -> 1950 (7th Schedule Union/State/Concurrent lists with Residuary to Parliament).",
    "அதிகாரப் பகிர்வு வளர்ச்சி: 1833 (மத்திய ஏகபோகம்) -> 1861 (பரவலாக்கல் தொடக்கம்) -> 1919 (மத்திய/மாகாணத் துறைப் பிரிவு) -> 1935 (3 பட்டியல்கள், எஞ்சிய அதிகாரம் வைஸ்ராயிடம்) -> 1950 (7வது அட்டவணை, எஞ்சிய அதிகாரம் பாராளுமன்றத்திடம்).",
    "Correct. Accurately synthesizes the evolution of Federal Division of Powers leading to 7th Schedule.",
    "சரி. 7வது அட்டவணைக்கு வழிவகுத்த கூட்டாட்சி அதிகாரப் பகிர்வின் வளர்ச்சியைத் துல்லியமாக ஒருங்கிணைக்கிறது.",
    "Incorrect. 7th Schedule came in 1950, not 1833.",
    "தவறு. 7வது அட்டவணை 1950 இல் வந்தது.",
    "Incorrect. Residuary powers were with Viceroy in 1935 and Parliament in 1950.",
    "தவறு. எஞ்சிய அதிகாரம் 1935 இல் வைஸ்ராயிடமும் 1950 இல் பாராளுமன்றத்திடமும் இருந்தது.",
    "Incorrect. Division of powers underwent major constitutional evolutions.",
    "தவறு. அதிகாரப் பகிர்வு பெரும் அரசியலமைப்பு மாற்றங்களைச் சந்தித்தது.",
    "Key difference: In 1935 Act, Residuary powers were given to Viceroy (GG). In 1950 Constitution, Residuary powers belong to Union Parliament (Article 248).",
    "முக்கிய வேறுபாடு: 1935 சட்டத்தில் எஞ்சிய அதிகாரம் வைஸ்ராயிடம் இருந்தது. 1950 அரசியலமைப்பில் எஞ்சிய அதிகாரம் மத்திய பாராளுமன்றத்திடம் உள்ளது (பிரிவு 248).",
    "The 1935 Act list count: Federal List (59), Provincial List (54), Concurrent List (36).",
    "1935 சட்டப் பட்டியல் அளவுகள்: கூட்டாட்சி (59), மாகாணம் (54), இணைப்பு (36).",
    "Analyze", 75, ["Polity", "Historical Background", "Integrated Analytical", "7th Schedule Division of Powers Arc"]
))

questions.append(make_q(
    "HB_H_050", "Integrated Analytical",
    "Synthesize the direct structural borrowings of the 1950 Constitution of India from British-era Acts and landmark colonial institutional frameworks:",
    "பிரிட்டிஷ் காலச் சட்டங்கள் மற்றும் மைல்கல் நிறுவனக் கட்டமைப்புகளிலிருந்து 1950 இந்திய அரசியலமைப்பு நேரடியாக எடுத்தாண்ட கட்டமைப்பு அம்சங்களை ஒருங்கிணைக்குக:",
    "GOI Act 1935 (Federal Scheme, Office of Governor, Judiciary, PSCs, Emergency provisions, ~250 Articles) + GOI Act 1919 (Bicameralism & Direct Elections foundation) + Indian Councils Act 1861 (Portfolio System & Ordinance powers model).",
    "1935 அரசுச் சட்டம் (கூட்டாட்சி, ஆளுநர் பதவி, நீதித்துறை, PSCகள், அவசரக்கால விதிகள், ~250 விதிகள்) + 1919 அரசுச் சட்டம் (ஈரவை முறை & நேரடித் தேர்தல் அடிப்படை) + 1861 கவுன்சில்கள் சட்டம் (போர்ட்ஃபோலியோ முறை & அவசரச்சட்ட மாதிரி).",
    "1950 Constitution borrowed 100% features from the US Constitution with zero British era borrowings.",
    "1950 அரசியலமைப்பு 100% அம்சங்களை அமெரிக்க அரசியலமைப்பிலிருந்து எடுத்தாண்டது, பிரிட்டிஷ் காலப் பயன்பாடு ஏதுமில்லை.",
    "1858 Act provided the Preamble, while 1773 Act provided Fundamental Rights.",
    "1858 சட்டம் முகப்புரையையும், 1773 சட்டம் அடிப்படை உரிமைகளையும் வழங்கின.",
    "All colonial era features were explicitly repudiated and none were adapted into the 1950 Constitution.",
    "அனைத்து காலனித்துவ அம்சங்களும் வெளிப்படையாக நிராகரிக்கப்பட்டு எதுவும் 1950 அரசியலமைப்பில் ஏற்கப்படவில்லை.",
    "A",
    "The 1950 Indian Constitution is a synthesis of colonial administrative blueprints and modern democratic principles. GOI Act 1935 formed the principal structural blueprint (~250 articles), 1919 Act provided bicameralism & elections framework, and 1861 Act provided portfolio & ordinance models.",
    "1950 இந்திய அரசியலமைப்பு காலனித்துவ நிர்வாக வரைபடங்கள் மற்றும் ஜனநாயகக் கோட்பாடுகளின் சேர்க்கையாகும். 1935 சட்டம் முதன்மை வரைபடமானது (~250 விதிகள்), 1919 சட்டம் ஈரவை முறையையும், 1861 சட்டம் போர்ட்ஃபோலியோ/அவசரச்சட்ட மாதிரிகளையும் அளித்தன.",
    "Correct. Accurately synthesizes structural borrowings from 1935, 1919, and 1861 Acts into the 1950 Constitution.",
    "சரி. 1935, 1919 மற்றும் 1861 சட்டங்களிலிருந்து 1950 அரசியலமைப்பிற்கு பெறப்பட்ட அம்சங்களைத் துல்லியமாக ஒருங்கிணைக்கிறது.",
    "Incorrect. Structural administrative blueprint was heavily drawn from 1935 Act.",
    "தவறு. நிர்வாகக் கட்டமைப்பு 1935 சட்டத்திலிருந்து பெறப்பட்டது.",
    "Incorrect. Preamble was inspired by Objective Resolution; FRs from US Constitution.",
    "தவறு. முகப்புரை நோக்குத் தீர்மானத்திலிருந்தும், அடிப்படை உரிமைகள் அமெரிக்காவிலிருந்தும் பெறப்பட்டன.",
    "Incorrect. About 250 articles were adapted from 1935 Act.",
    "தவறு. 1935 சட்டத்திலிருந்து சுமார் 250 விதிகள் எடுத்தாளப்பட்டன.",
    "Dr. B.R. Ambedkar acknowledged that the administrative details of the 1935 Act were retained to ensure stability during transition.",
    "அதிகார மாற்றத்தின் போது ஸ்திரத்தன்மையை உறுதி செய்ய 1935 சட்டத்தின் நிர்வாக விவரங்கள் தக்கவைக்கப்பட்டதாக டாக்டர் பி.ஆர். அம்பேத்கர் கூறினார்.",
    "The 1950 Constitution came into force on January 26, 1950, giving India the status of a Sovereign Democratic Republic.",
    "1950 ஜனவரி 26 அன்று இந்திய அரசியலமைப்பு அமலுக்கு வந்து இந்தியாவை இறையாண்மைமிக்க ஜனநாயகக் குடியரசாக்கியது.",
    "Analyze", 75, ["Polity", "Historical Background", "Integrated Analytical", "Constitutional Borrowings Synthesis"]
))

# Save all 50 questions to target JSON file
with open(target_path, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"Successfully generated and saved ALL {len(questions)} questions to {target_path}")

# Run schema validation using core/question_engine/validators.py
sys.path.insert(0, r"c:\Users\Home\Desktop\tnpsc_ai")
from core.question_engine.validators import validate_questions
val_res = validate_questions(questions)
print(f"Validation Result: Valid={val_res.valid}")
if val_res.errors:
    print("Validation Errors:", val_res.errors)
if val_res.warnings:
    print("Validation Warnings:", val_res.warnings)
