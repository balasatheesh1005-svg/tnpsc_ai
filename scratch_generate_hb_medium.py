import json
import sys
from pathlib import Path

# Target file path
target_path = Path(r"c:\Users\Home\Desktop\tnpsc_ai\data\questions\polity\historical_background_medium.json")

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

questions = []

# ---------------------------------------------------------
# 15 CONCEPTUAL QUESTIONS (HB_M_001 to HB_M_015)
# ---------------------------------------------------------

questions.append(make_q(
    "HB_M_001", "Conceptual",
    "Which of the following was the primary constitutional significance of establishing the Supreme Court of Judicature at Fort William in Calcutta under the Regulating Act of 1773?",
    "1773 ஆம் ஆண்டின் ஒழுங்குமுறைச் சட்டத்தின் கீழ் கொல்கத்தா ஃபோர்ட் வில்லியமில் உச்சநீதிமன்றம் அமைக்கப்பட்டதன் முதன்மை அரசியலமைப்பு முக்கியத்துவம் யாது?",
    "It established a supreme judicial body having jurisdiction over all native rulers in India.",
    "இது இந்தியாவில் உள்ள அனைத்து சுதேசி ஆட்சியாளர்கள் மீதும் அதிகார வரம்பு கொண்ட உச்ச நீதி அமைப்பை நிறுவியது.",
    "It created an independent judicial authority to restrain the arbitrary actions of Company officials and enforce British law.",
    "இது கம்பெனி அதிகாரிகளின் தன்னிச்சையான நடவடிக்கைகளைக் கட்டுப்படுத்தவும் பிரிட்டிஷ் சட்டத்தைச் செயல்படுத்தவும் ஒரு சுயாதீன நீதித்துறை அமைப்பை உருவாக்கியது.",
    "It replaced the Mayor's Courts in Bombay and Madras completely.",
    "இது பம்பாய் மற்றும் மதராஸில் உள்ள மேயர் நீதிமன்றங்களை முழுமையாக மாற்றீடு செய்தது.",
    "It established appellate jurisdiction over the House of Lords in London.",
    "இது லண்டனில் உள்ள பிரபுக்கள் சபையின் மேல்முறையீட்டு அதிகார வரம்பை நிறுவியது.",
    "B",
    "The Regulating Act of 1773 established a Supreme Court at Calcutta (1774) with a Chief Justice (Sir Elijah Impey) and 3 other judges to control and regulate Company officials who were engaging in private trade and corruption.",
    "1773 ஒழுங்குமுறைச் சட்டம் 1774 இல் கொல்கத்தாவில் ஒரு தலைமை நீதிபதி (சர் எலிஜா இம்பே) மற்றும் 3 நீதிபதிகளுடன் உச்ச நீதிமன்றத்தை நிறுவி, தனிப்பட்ட வர்த்தகம் மற்றும் ஊழலில் ஈடுபட்ட கம்பெனி அதிகாரிகளைக் கட்டுப்படுத்தியது.",
    "Incorrect. It had no jurisdiction over native Indian rulers outside British possessions unless by mutual agreement.",
    "தவறு. பரஸ்பர ஒப்பந்தம் இன்றி பிரிட்டிஷ் ஆட்சிக்குட்பட்ட பகுதிகளுக்கு வெளியே உள்ள சுதேசி ஆட்சியாளர்கள் மீது அதிகார வரம்பு இல்லை.",
    "Correct. The Supreme Court was created to provide a legal check over East India Company servants.",
    "சரி. கிழக்கிந்தியக் கம்பெனி ஊழியர்கள் மீது சட்டப் பூர்வக் கட்டுப்பாட்டை ஏற்படுத்த உச்ச நீதிமன்றம் உருவாக்கப்பட்டது.",
    "Incorrect. Mayor's Courts in Bombay and Madras continued until Courts of Recorder were introduced in 1797.",
    "தவறு. பம்பாய் மற்றும் மதராஸில் மேயர் நீதிமன்றங்கள் 1797 வரை தொடர்ந்தன.",
    "Incorrect. Appeals from this Supreme Court actually lay to the Privy Council in London, not House of Lords.",
    "தவறு. இந்த உச்ச நீதிமன்றத்தின் மேல்முறையீடுகள் லண்டனில் உள்ள பிரிவி கவுன்சிலுக்கு சென்றன, பிரபுக்கள் சபைக்கு அல்ல.",
    "Distinguish Supreme Court jurisdiction (1774) vs Provincial Courts. Appeals from Calcutta SC went to the Privy Council.",
    "கொல்கத்தா உச்ச நீதிமன்ற அதிகார வரம்பையும் மாகாண நீதிமன்றங்களையும் வேறுபடுத்திப் பார்க்கவும். மேல்முறையீடு பிரிவி கவுன்சிலுக்குச் சென்றது.",
    "Supreme Court at Calcutta was established in 1774 with Sir Elijah Impey as the first Chief Justice.",
    "1774 இல் கொல்கத்தா உச்ச நீதிமன்றத்தின் முதல் தலைமை நீதிபதியாக சர் எலிஜா இம்பே நியமிக்கப்பட்டார்.",
    "Understand", 60, ["Polity", "Historical Background", "Regulating Act 1773", "Supreme Court"]
))

questions.append(make_q(
    "HB_M_002", "Conceptual",
    "What was the main purpose of enacting the Amending Act of 1781 (also known as the Act of Settlement)?",
    "1781 ஆம் ஆண்டின் திருத்தச் சட்டம் (சமரசச் சட்டம்) இயற்றப்பட்டதன் முதன்மை நோக்கம் யாது?",
    "To abolish the Board of Control created by the British Cabinet.",
    "பிரிட்டிஷ் அமைச்சரவையால் உருவாக்கப்பட்ட கட்டுப்பாட்டு வாரியத்தைக் கலைப்பது.",
    "To demarcate boundaries between the Supreme Court and the Governor-General in Council and exempt revenue collectors from SC jurisdiction.",
    "உச்ச நீதிமன்றத்திற்கும் கவர்னர் ஜெனரல் கவுன்சிலுக்கும் இடையிலான எல்லைகளை வரையறுத்து, வருவாய் வசூலிப்பாளர்களை உச்சநீதிமன்ற அதிகார வரம்பிலிருந்து விலக்குவது.",
    "To introduce Macaulay's penal code across Company territories.",
    "கம்பெனி பகுதிகள் முழுவதும் மெக்காலேயின் தண்டனைச் சட்டத்தை அறிமுகப்படுத்துவது.",
    "To grant financial autonomy to Madras and Bombay Presidencies.",
    "மதராஸ் மற்றும் பம்பாய் மாகாணங்களுக்கு நிதி தன்னாட்சி வழங்குவது.",
    "B",
    "The Amending Act of 1781 was passed to remedy defects of the 1773 Act by exempting the Governor-General, his council, and revenue officials from Supreme Court jurisdiction for acts performed in official capacity.",
    "1781 திருத்தச் சட்டம், 1773 சட்டத்தின் குறைபாடுகளை நீக்க இயற்றப்பட்டது. இது கவர்னர் ஜெனரல், அவரது கவுன்சில் மற்றும் வருவாய் அதிகாரிகளை அவர்களின் அதிகாரப்பூர்வ பணிகளுக்காக உச்சநீதிமன்ற அதிகார வரம்பிலிருந்து விலக்கியது.",
    "Incorrect. The Board of Control was created later by Pitt's India Act 1784.",
    "தவறு. கட்டுப்பாட்டு வாரியம் 1784 பிட் இந்தியச் சட்டத்தின் மூலமே உருவாக்கப்பட்டது.",
    "Correct. It defined revenue jurisdiction and protected official actions of Governor-General in Council.",
    "சரி. இது வருவாய் அதிகார வரம்பை வரையறுத்து கவர்னர் ஜெனரல் கவுன்சிலின் அதிகாரப்பூர்வ நடவடிக்கைகளைப் பாதுகாத்தது.",
    "Incorrect. Law Commission and Macaulay came under Charter Act of 1833.",
    "தவறு. சட்ட ஆணையமும் மெக்காலேயும் 1833 சாசனச் சட்டத்தின் கீழ் வந்தனர்.",
    "Incorrect. Financial autonomy was gradually granted much later under 1861, 1870, and 1919 developments.",
    "தவறு. நிதி தன்னாட்சி பிற்கால 1861, 1870 மற்றும் 1919 மாற்றங்களிலேயே வழங்கப்பட்டது.",
    "1781 Act is called 'Act of Settlement' because it settled disputes between Executive (GG-in-Council) and Judiciary (SC).",
    "1781 சட்டம் 'சமரசச் சட்டம்' எனப்படுகிறது, ஏனெனில் இது நிர்வாகத்திற்கும் (GG-கவுன்சில்) நீதித்துறைக்கும் (SC) இடையிலான மோதல்களைத் தீர்த்தது.",
    "1781 Act excluded revenue matters and official actions from Supreme Court jurisdiction.",
    "1781 ஆம் ஆண்டு சட்டம் வருவாய் விவகாரங்களையும் அதிகாரப்பூர்வ பணிகளையும் உச்ச நீதிமன்ற அதிகார வரம்பிலிருந்து விலக்கியது.",
    "Understand", 60, ["Polity", "Historical Background", "Amending Act 1781", "Act of Settlement"]
))

questions.append(make_q(
    "HB_M_003", "Conceptual",
    "How did Pitt's India Act of 1784 establish a system of 'Double Government' in British administration of India?",
    "1784 ஆம் ஆண்டின் பிட் இந்தியச் சட்டம் பிரிட்டிஷ் இந்திய நிர்வாகத்தில் எவ்வாறு 'இரட்டை ஆட்சி' முறையை நிறுவியது?",
    "By establishing separate executive and legislative councils in Bengal.",
    "வங்காளத்தில் தனித்தனி நிர்வாக மற்றும் சட்டமன்ற கவுன்சில்களை நிறுவியதன் மூலம்.",
    "By separating commercial functions (Court of Directors) and political functions (Board of Control) of the East India Company.",
    "கிழக்கிந்தியக் கம்பெனியின் வர்த்தகப் பணிகளையும் (இயக்குநர்கள் அவை) அரசியல் பணிகளையும் (கட்டுப்பாட்டு வாரியம்) பிரித்ததன் மூலம்.",
    "By dividing powers between the British Crown and Indian Princely States.",
    "பிரிட்டிஷ் முடிஅரசு மற்றும் இந்திய சுதேச சமஸ்தானங்களுக்கு இடையே அதிகாரங்களைப் பகிர்ந்ததன் மூலம்.",
    "By introducing Dyarchy with reserved and transferred subjects in provinces.",
    "மாகாணங்களில் ஒதுக்கப்பட்ட மற்றும் மாற்றப்பட்ட துறைகளுடன் இரட்டை ஆட்சியை அறிமுகப்படுத்தியதன் மூலம்.",
    "B",
    "Pitt's India Act 1784 created a Board of Control (6 Privy Councillors) to manage political affairs while leaving commercial operations to Court of Directors, establishing System of Double Government.",
    "1784 பிட் இந்தியச் சட்டம் அரசியல் விவகாரங்களை நிர்வகிக்க கட்டுப்பாட்டு வாரியத்தை (6 உறுப்பினர்கள்) உருவாக்கியது, வர்த்தகப் பணிகளை இயக்குநர்கள் அவையிடம் விட்டது. இதுவே இரட்டை ஆட்சி முறை எனப்பட்டது.",
    "Incorrect. Executive/Legislative separation in councils happened under Charter Act 1853.",
    "தவறு. நிர்வாக மற்றும் சட்டமன்றப் பிரிவு 1853 சாசனச் சட்டத்தில்தான் நடந்தது.",
    "Correct. It separated commercial (Court of Directors) and political (Board of Control) administration.",
    "சரி. இது வர்த்தக மற்றும் அரசியல் நிர்வாகத்தைப் பிரித்தது.",
    "Incorrect. Division with princely states was part of later federal schemes (1935).",
    "தவறு. சுதேச சமஸ்தானப் பங்களிப்பு 1935 கூட்டாட்சி திட்டத்தின் பகுதி.",
    "Incorrect. Dyarchy with reserved/transferred subjects was introduced by GOI Act 1919.",
    "தவறு. ஒதுக்கப்பட்ட/மாற்றப்பட்ட துறைகளுடன் கூடிய இரட்டை ஆட்சி 1919 சட்டத்தால் வந்தது.",
    "Do not confuse Double Government of 1784 (Board of Control vs Court of Directors) with Dyarchy of 1919 (Provincial Subjects).",
    "1784 இன் இரட்டை நிர்வாகத்தையும் (Board of Control vs Court of Directors) 1919 இன் மாகாண இரட்டை ஆட்சியையும் குழப்பிக் கொள்ளக் கூடாது.",
    "Pitt's India Act 1784 used the term 'British possessions in India' for the first time.",
    "1784 பிட் இந்தியச் சட்டம் முதன்முறையாக 'இந்தியாவில் உள்ள பிரிட்டிஷ் உடமைகள்' என்ற சொல்லைப் பயன்படுத்தியது.",
    "Understand", 60, ["Polity", "Historical Background", "Pitt's India Act 1784", "Double Government"]
))

questions.append(make_q(
    "HB_M_004", "Conceptual",
    "Which Charter Act mandated that the salaries and expenses of the Board of Control and their staff should be charged upon the revenues of India?",
    "கட்டுப்பாட்டு வாரியம் மற்றும் அதன் ஊழியர்களின் ஊதியம் மற்றும் செலவுகள் இந்திய வருவாயிலிருந்தே வழங்கப்பட வேண்டும் என்று கட்டாயப்படுத்திய சாசனச் சட்டம் எது?",
    "Charter Act of 1793", "1793 ஆம் ஆண்டின் சாசனச் சட்டம்",
    "Charter Act of 1813", "1813 ஆம் ஆண்டின் சாசனச் சட்டம்",
    "Charter Act of 1833", "1833 ஆம் ஆண்டின் சாசனச் சட்டம்",
    "Charter Act of 1853", "1853 ஆம் ஆண்டின் சாசனச் சட்டம்",
    "A",
    "The Charter Act of 1793 mandated that the Board of Control members and staff were henceforth to be paid out of Indian revenues. This practice continued until the Government of India Act 1919.",
    "1793 ஆம் ஆண்டின் சாசனச் சட்டம் கட்டுப்பாட்டு வாரிய உறுப்பினர்கள் மற்றும் ஊழியர்களின் சம்பளம் இனி இந்திய வருவாயிலிருந்தே வழங்கப்பட வேண்டும் என்று கூறியது. இது 1919 வரை தொடர்ந்தது.",
    "Correct. Charter Act 1793 started paying Board of Control salaries out of Indian revenues.",
    "சரி. 1793 சாசனச் சட்டம் கட்டுப்பாட்டு வாரியத்தின் சம்பளத்தை இந்திய வருவாயிலிருந்து வழங்கத் தொடங்கியது.",
    "Incorrect. Charter Act 1813 ended Company trade monopoly except tea and trade with China.",
    "தவறு. 1813 சாசனச் சட்டம் தேயிலை மற்றும் சீனா வர்த்தகம் தவிர கம்பெனியின் வர்த்தக ஏகபோகத்தை முடிவுக்கு கொண்டு வந்தது.",
    "Incorrect. Charter Act 1833 made Governor-General of Bengal into Governor-General of India.",
    "தவறு. 1833 சாசனச் சட்டம் வங்காள கவர்னர் ஜெனரலை இந்திய கவர்னர் ஜெனரலாக மாற்றியது.",
    "Incorrect. Charter Act 1853 created the Indian Legislative Council.",
    "தவறு. 1853 சாசனச் சட்டம் இந்திய சட்டமன்ற கவுன்சிலை உருவாக்கியது.",
    "Paying British officials out of Indian revenues laid the economic root of Dadabhai Naoroji's 'Drain of Wealth' theory.",
    "இந்திய வருவாயில் பிரிட்டிஷ் அதிகாரிகளுக்கு சம்பளம் வழங்கியது தாதாபாய் நௌரோஜியின் 'செல்வச் சுரண்டல்' கோட்பாட்டிற்கு அடித்தளமிட்டது.",
    "1793 Act extended Company trade monopoly for another 20 years and required Board of Control salaries from Indian revenue.",
    "1793 சட்டம் கம்பெனியின் வர்த்தக ஏகபோகத்தை மேலும் 20 ஆண்டுகளுக்கு நீட்டித்ததுடன் இந்திய வருவாயிலிருந்து சம்பளம் வழங்க உத்தரவிட்டது.",
    "Remember", 60, ["Polity", "Historical Background", "Charter Act 1793", "Drain of Wealth"]
))

questions.append(make_q(
    "HB_M_005", "Conceptual",
    "What was a landmark feature introduced by the Charter Act of 1813 regarding social and educational evolution in British India?",
    "பிரிட்டிஷ் இந்தியாவின் சமூக மற்றும் கல்வி வளர்ச்சியில் 1813 ஆம் ஆண்டின் சாசனச் சட்டம் அறிமுகப்படுத்திய ஒரு மைல்கல் அம்சம் யாது?",
    "It established compulsory primary education across all presidencies.",
    "இது அனைத்து மாகாணங்களிலும் கட்டாயத் தொடக்கக் கல்வியை நிறுவியது.",
    "It set aside a sum of Rupees One Lakh annually for promotion of literature, learning, and science among Indians, and permitted Christian missionaries to operate.",
    "இந்தியர்களிடையே இலக்கியம், கல்வி மற்றும் அறிவியலை மேம்படுத்த ஆண்டிற்கு ரூ. 1 லட்சம் ஒதுக்கியதுடன், கிறிஸ்தவ மிஷனரிகள் செயல்பட அனுமதித்தது.",
    "It created the first Indian University in Calcutta.",
    "இது கொல்கத்தாவில் முதல் இந்தியப் பல்கலைக்கழகத்தை உருவாக்கியது.",
    "It abolished English as the official language of courts.",
    "இது நீதிமன்றங்களின் அதிகாரப்பூர்வ மொழியாக ஆங்கிலத்தை நீக்கியது.",
    "B",
    "Charter Act 1813 ended EIC's trade monopoly in India (except tea and China trade), asserted Crown sovereignty over Company territories, allocated Rs 1 Lakh for education, and allowed Christian missionaries to preach.",
    "1813 சாசனச் சட்டம் கம்பெனியின் வர்த்தக ஏகபோகத்தை (தேயிலை மற்றும் சீனா வர்த்தகம் தவிர) ரத்து செய்தது, கல்விக்காக ரூ. 1 லட்சம் ஒதுக்கியது, மற்றும் கிறிஸ்தவ மிஷனரிகளுக்கு அனுமதி அளித்தது.",
    "Incorrect. Primary education was not made compulsory by this Act.",
    "தவறு. இந்த சட்டத்தின் மூலம் தொடக்கக் கல்வி கட்டாயமாக்கப்படவில்லை.",
    "Correct. Allocated Rs 1 Lakh for education and allowed Christian missionaries.",
    "சரி. கல்விக்கு ரூ. 1 லட்சம் ஒதுக்கியதுடன் மிஷனரிகளையும் அனுமதித்தது.",
    "Incorrect. Universities of Calcutta, Bombay, Madras were set up in 1857 following Wood's Despatch (1854).",
    "தவறு. கொல்கத்தா, பம்பாய், மதராஸ் பல்கலைக்கழகங்கள் 1857 இல் அமைக்கப்பட்டன.",
    "Incorrect. English became official language of higher courts later in 1835/1837.",
    "தவறு. ஆங்கிலம் நீதிமன்ற மொழியானது 1835/1837 காலக்கட்டத்திலாகும்.",
    "1813 Act stripped commercial monopoly EXCEPT Tea trade and Trade with China (which were abolished in 1833).",
    "1813 சட்டம் தேயிலை மற்றும் சீனா வர்த்தகம் தவிர மற்ற ஏகபோகத்தை முடித்தது (அவை 1833 இல் முடிந்தன).",
    "Charter Act 1813 allocated Rs 1 Lakh annually for education in India.",
    "1813 சாசனச் சட்டம் இந்தியாவில் கல்விக்காக ஆண்டிற்கு ரூ. 1 லட்சம் ஒதுக்கியது.",
    "Understand", 60, ["Polity", "Historical Background", "Charter Act 1813", "Education"]
))

questions.append(make_q(
    "HB_M_006", "Conceptual",
    "The Charter Act of 1833 is considered the climax of administrative centralization in British India. Which of the following structural changes directly brought about this centralization?",
    "1833 ஆம் ஆண்டின் சாசனச் சட்டம் பிரிட்டிஷ் இந்தியாவில் நிர்வாக மத்தியமயமாக்கலின் உச்சகட்டமாகக் கருதப்படுகிறது. பின்வரும் எந்த கட்டமைப்பு மாற்றம் இந்த மத்தியமயமாக்கலை நேரடியாகக் கொண்டு வந்தது?",
    "It designated the Governor-General of Bengal as the Governor-General of India and deprived Governors of Bombay and Madras of their legislative powers.",
    "இது வங்காள கவர்னர் ஜெனரலை இந்திய கவர்னர் ஜெனரலாக மாற்றி, பம்பாய் மற்றும் மதராஸ் கவர்னர்களின் சட்டமியற்றும் அதிகாரங்களைப் பறித்தது.",
    "It created separate Provincial Legislative Assemblies for Bombay, Madras, and Bengal.",
    "இது பம்பாய், மதராஸ் மற்றும் வங்காளத்திற்கு தனித்தனியாக மாகாண சட்டமன்றங்களை உருவாக்கியது.",
    "It created a Supreme Court in every presidency capital.",
    "இது ஒவ்வொரு மாகாணத் தலைநகரிலும் ஒரு உச்ச நீதிமன்றத்தை உருவாக்கியது.",
    "It transferred the administration of India directly to the British Parliament.",
    "இது இந்தியாவின் நிர்வாகத்தை நேரடியாக பிரிட்டிஷ் பாராளுமன்றத்திற்கு மாற்றியது.",
    "A",
    "The Charter Act of 1833 redesignated the Governor-General of Bengal as Governor-General of India (Lord William Bentinck was first) and vested all civil and military powers in him, centralizing lawmaking exclusively at the Centre.",
    "1833 சாசனச் சட்டம் வங்காள கவர்னர் ஜெனரலை இந்திய கவர்னர் ஜெனரலாக (முதல் நபர்: வில்லியம் பென்டிங்க் பிரபு) மாற்றியதுடன், அனைத்து சிவில் மற்றும் இராணுவ அதிகாரங்களையும் அவரிடம் வழங்கி, சட்டமியற்றும் அதிகாரத்தை மையப்படுத்தியது.",
    "Correct. Made GG of Bengal as GG of India and concentrated all legislative powers in his council.",
    "சரி. வங்காள GG-ஐ இந்திய GG-ஆக மாற்றி சட்டமியற்றும் அதிகாரத்தை மையத்தில் குவித்து பம்பாய்/மதராஸ் அதிகாரத்தைப் பறித்தது.",
    "Incorrect. Provincial legislative powers were deprived by this Act, not created.",
    "தவறு. மாகாண சட்டமியற்றும் அதிகாரங்கள் இந்த சட்டத்தால் பறிக்கப்பட்டன.",
    "Incorrect. Supreme Courts were not created in every presidency capital by 1833.",
    "தவறு. 1833 இல் அனைத்து மாகாணத் தலைநகரங்களிலும் உச்ச நீதிமன்றங்கள் உருவாக்கப்படவில்லை.",
    "Incorrect. Direct transfer to British Crown/Parliament took place under Government of India Act 1858.",
    "தவறு. பிரிட்டிஷ் முடிஅரசுக்கு நேரடி நிர்வாக மாற்றம் 1858 ஆம் ஆண்டு சட்டத்தில் நடந்தது.",
    "1833 Act created 'Governor-General of India' and laws made under it were called 'Acts' (earlier called 'Regulations').",
    "1833 சட்டத்திற்கு முன் இயற்றப்பட்ட விதிகள் 'ஒழுங்குமுறைகள்' (Regulations) எனப்பட்டன, இதன் பின் இயற்றப்பட்டவை 'சட்டங்கள்' (Acts) எனப்பட்டன.",
    "Lord William Bentinck became the first Governor-General of India under Charter Act 1833.",
    "1833 சாசனச் சட்டத்தின் கீழ் வில்லியம் பென்டிங்க் பிரபு இந்தியாவின் முதல் கவர்னர் ஜெனரலானார்.",
    "Understand", 60, ["Polity", "Historical Background", "Charter Act 1833", "Centralization"]
))

questions.append(make_q(
    "HB_M_007", "Conceptual",
    "Which Charter Act introduced for the first time a distinction between executive and legislative functions of the Governor-General's Council and created a 6-member Indian (Central) Legislative Council?",
    "கவர்னர் ஜெனரல் கவுன்சிலின் நிர்வாக மற்றும் சட்டமன்றப் பணிகளுக்கு இடையே முதன்முறையாக வேறுபாட்டை அறிமுகப்படுத்தி 6 உறுப்பினர்களைக் கொண்ட இந்திய (மத்திய) சட்டமன்ற கவுன்சிலை உருவாக்கிய சாசனச் சட்டம் எது?",
    "Charter Act of 1813", "1813 ஆம் ஆண்டின் சாசனச் சட்டம்",
    "Charter Act of 1833", "1833 ஆம் ஆண்டின் சாசனச் சட்டம்",
    "Charter Act of 1853", "1853 ஆம் ஆண்டின் சாசனச் சட்டம்",
    "Government of India Act 1858", "1858 ஆம் ஆண்டின் இந்திய அரசுச் சட்டம்",
    "C",
    "Charter Act of 1853 added 6 new legislative members (called Legislative Councillors) to the Governor-General's Council, functioning as a 'Mini-Parliament' adopting British parliamentary procedure, and introduced open competition for Civil Services (Macaulay Committee 1854).",
    "1853 சாசனச் சட்டம் கவர்னர் ஜெனரல் கவுன்சிலில் 6 புதிய சட்டமன்ற உறுப்பினர்களைச் சேர்த்தது ('மினி பாராளுமன்றம்'). மேலும் இது குடிமைப் பணிகளுக்கான திறந்தவெளிப் போட்டித் தேர்வை அறிமுகப்படுத்தியது (மெக்காலே குழு 1854).",
    "Incorrect. Charter Act 1813 dealt with trade monopoly and education.",
    "தவறு. 1813 சாசனச் சட்டம் வர்த்தக ஏகபோகம் மற்றும் கல்வியைப் பற்றியது.",
    "Incorrect. Charter Act 1833 added Law Member (Macaulay) to executive council without separate legislative body.",
    "தவறு. 1833 சாசனச் சட்டம் சட்ட உறுப்பினரை (மெக்காலே) சேர்த்தது ஆனால் தனி சட்டமன்ற உடலை உருவாக்கவில்லை.",
    "Correct. Charter Act 1853 created Central Legislative Council and separated legislative/executive functions.",
    "சரி. 1853 சாசனச் சட்டம் மத்திய சட்டமன்ற கவுன்சிலை உருவாக்கி சட்டமன்ற/நிர்வாகப் பணிகளைப் பிரித்தது.",
    "Incorrect. GOI Act 1858 transferred power to Crown.",
    "தவறு. 1858 இந்திய அரசுச் சட்டம் அதிகாரத்தை பிரிட்டிஷ் அரசிற்கு மாற்றியது.",
    "Charter Act 1853 introduced local representation in Central Legislative Council: 4 out of 6 new members were appointed by local governments of Madras, Bombay, Bengal, and Agra.",
    "1853 சாசனச் சட்டம் மத்திய சட்டமன்ற கவுன்சிலில் உள்ளூர் பிரதிநிதித்துவத்தை அறிமுகப்படுத்தியது (மதராஸ், பம்பாய், வங்காளம், ஆக்ரா).",
    "Charter Act 1853 was the last of the series of Charter Acts passed between 1793 and 1853.",
    "1793 மற்றும் 1853 க்கு இடையில் இயற்றப்பட்ட சாசனச் சட்டங்களின் வரிசையில் 1853 சாசனச் சட்டமே கடைசியானதாகும்.",
    "Understand", 60, ["Polity", "Historical Background", "Charter Act 1853", "Legislative Council"]
))

questions.append(make_q(
    "HB_M_008", "Conceptual",
    "The Government of India Act 1858 (Act for the Good Government of India) substituted Company rule with Crown rule. Which of the following offices was created by this Act to exercise direct control over Indian administration from London?",
    "1858 ஆம் ஆண்டின் இந்திய அரசுச் சட்டம் கம்பெனி ஆட்சியை முடிஆட்சிக்கு மாற்றியது. லண்டனிலிருந்து இந்திய நிர்வாகத்தின் மீது நேரடி அதிகாரத்தைச் செலுத்த இந்தச் சட்டத்தால் உருவாக்கப்பட்ட அலுவலகம் எது?",
    "High Commissioner for India", "இந்திய உயர் ஆணையர்",
    "Secretary of State for India", "இந்திய அரசுச் செயலாளர் (செயலர்)",
    "Viceroy and Governor-General of India", "இந்திய வைஸ்ராய் மற்றும் கவர்னர் ஜெனரல்",
    "President of the Board of Control", "கட்டுப்பாட்டு வாரியத்தின் தலைவர்",
    "B",
    "The GOI Act 1858 created the office of 'Secretary of State for India', a cabinet minister of British Parliament, assisted by a 15-member advisory Council of India. Lord Stanley was the first Secretary of State for India.",
    "1858 இந்திய அரசுச் சட்டம் பிரிட்டிஷ் அமைச்சரவை உறுப்பினரான 'இந்திய அரசுச் செயலாளர்' அலுவலகத்தை உருவாக்கியது. இவருக்கு உதவ 15 உறுப்பினர்களைக் கொண்ட 'இந்திய கவுன்சில்' அமைக்கப்பட்டது.",
    "Incorrect. High Commissioner for India was created later under Government of India Act 1919.",
    "தவறு. இந்திய உயர் ஆணையர் பதவி பிற்காலத்தில் 1919 ஆம் ஆண்டு சட்டத்தின் கீழ் உருவாக்கப்பட்டது.",
    "Correct. Created Secretary of State for India residing in London with ultimate control.",
    "சரி. லண்டனில் தங்கி முழு நிர்வாகக் கட்டுப்பாட்டைக் கொண்ட இந்திய அரசுச் செயலாளர் பதவி உருவாக்கப்பட்டது.",
    "Incorrect. Viceroy was the direct representative of the Crown in India, but Secretary of State exercised ultimate authority from London.",
    "தவறு. வைஸ்ராய் இந்தியாவில் பிரிட்டிஷ் அரசியின் பிரதிநிதி, ஆனால் லண்டனிலிருந்து முழு அதிகாரம் செலுத்தியவர் அரசுச் செயலாளரே.",
    "Incorrect. Board of Control was abolished by the 1858 Act.",
    "தவறு. கட்டுப்பாட்டு வாரியம் 1858 சட்டத்தின் மூலம் கலைக்கப்பட்டது.",
    "Distinguish roles: Secretary of State was based in London (Cabinet Minister); Viceroy was based in Calcutta/Delhi as Crown representative.",
    "வேறுபாட்டை உணர்க: அரசுச் செயலாளர் லண்டனில் இருந்தார்; வைஸ்ராய் இந்தியாவில் பிரிட்டிஷ் மகாராணியின் பிரதிநிதியாக இருந்தார்.",
    "Lord Canning became the first Viceroy of India under GOI Act 1858.",
    "1858 ஆம் ஆண்டு சட்டத்தின் கீழ் லார்ட் கேனிங் இந்தியாவின் முதல் வைஸ்ராயானார்.",
    "Understand", 60, ["Polity", "Historical Background", "Government of India Act 1858", "Secretary of State"]
))

questions.append(make_q(
    "HB_M_009", "Conceptual",
    "The Indian Councils Act of 1861 initiated the process of associating Indians with the law-making process. Which Indians were nominated by Lord Canning to the expansion of his Central Legislative Council in 1862?",
    "1861 ஆம் ஆண்டின் இந்தியக் கவுன்சில்கள் சட்டம் இந்தியர்களைச் சட்டமியற்றும் பணியில் இணைக்கும் செயல்முறையைத் தொடங்கியது. 1862 இல் லார்ட் கேனிங்கால் மத்திய சட்டமன்ற கவுன்சிலில் நியமிக்கப்பட்ட இந்தியர்கள் யாவர்?",
    "Raja of Benares, Maharaja of Patiala, and Sir Dinkar Rao",
    "காசி (பனாரஸ்) ராஜா, பாட்டியாலா மகாராஜா, மற்றும் சர் தினகர் ராவ்",
    "Dadabhai Naoroji, Gopal Krishna Gokhale, and Pherozeshah Mehta",
    "தாதாபாய் நௌரோஜி, கோபால கிருஷ்ண கோகலே, மற்றும் பிரோஸ்ஷா மேத்தா",
    "Satyendra Prasad Sinha, Motilal Nehru, and Tej Bahadur Sapru",
    "சத்யேந்திர பிரசாத் சின்ஹா, மோதிலால் நேரு, மற்றும் தேஜ் பகதூர் சப்ரு",
    "Swami Vivekananda, Bal Gangadhar Tilak, and Lala Lajpat Rai",
    "சுவாமி விவேகானந்தர், பால கங்காதர திலகர், மற்றும் லாலா லஜபதி ராய்",
    "A",
    "In 1862, Lord Canning nominated three non-official Indian members to his expanded legislative council under Indian Councils Act 1861: Raja of Benares, Maharaja of Patiala, and Sir Dinkar Rao.",
    "1861 இந்தியக் கவுன்சில்கள் சட்டத்தின் கீழ் 1862 இல் லார்ட் கேனிங் மூன்று இந்திய உறுப்பினர்களைத் தனது விரிவாக்கப்பட்ட சட்டமன்றக் குழுவில் நியமித்தார்: காசி ராஜா, பாட்டியாலா மகாராஜா, மற்றும் சர் தினகர் ராவ்.",
    "Correct. Raja of Benares, Maharaja of Patiala, and Sir Dinkar Rao were nominated in 1862.",
    "சரி. காசி ராஜா, பாட்டியாலா மகாராஜா மற்றும் சர் தினகர் ராவ் ஆகிய 3 நபர்கள் 1862 இல் நியமிக்கப்பட்டனர்.",
    "Incorrect. Moderates like Naoroji and Gokhale came much later into legislative prominence.",
    "தவறு. நௌரோஜி, கோகலே போன்றோர் பிற்கால அரசியல் தலைவர்கள்.",
    "Incorrect. S.P. Sinha was the first Indian appointed to Viceroy's Executive Council under 1909 Act.",
    "தவறு. எஸ்.பி. சின்ஹா 1909 சட்டத்தின் கீழ் வைஸ்ராயின் நிர்வாக கவுன்சிலில் சேர்ந்த முதல் இந்தியர்.",
    "Incorrect. Extremist leaders like Tilak were not nominated to Viceroy's council.",
    "தவறு. திலகர் போன்ற தீவிர தேசிய தலைவர்கள் வைஸ்ராய் கவுன்சிலுக்கு நியமிக்கப்படவில்லை.",
    "Indian Councils Act 1861 also legalized the Portfolio System (introduced by Canning in 1859) and restored legislative powers to Bombay and Madras.",
    "1861 சட்டம் போர்ட்ஃபோலியோ (துறை ஒதுக்கீடு) முறையை அங்கீகரித்ததுடன் பம்பாய், மதராஸின் சட்ட அதிகாரங்களை மீண்டும் வழங்கியது.",
    "Indian Councils Act 1861 empowered the Viceroy to issue Ordinances during emergencies with a validity of 6 months.",
    "1861 சட்டம் வைஸ்ராய்க்கு 6 மாத கால அவகாசம் கொண்ட அவசரச் சட்டங்களை (Ordinances) பிறப்பிக்கும் அதிகாரத்தை வழங்கியது.",
    "Remember", 60, ["Polity", "Historical Background", "Indian Councils Act 1861", "Nominations"]
))

questions.append(make_q(
    "HB_M_010", "Conceptual",
    "What was the significant advance made by the Indian Councils Act of 1892 regarding the financial powers of the Legislative Councils?",
    "சட்டமன்ற கவுன்சில்களின் நிதி அதிகாரங்கள் தொடர்பாக 1892 ஆம் ஆண்டின் இந்திய கவுன்சில்கள் சட்டம் செய்த குறிப்பிடத்தக்க முன்னேற்றம் யாது?",
    "Members were granted the power to vote on demands for grants and veto the budget.",
    "உறுப்பினர்களுக்கு மானியக் கோரிக்கைகள் மீது வாக்களிக்கும் மற்றும் வரவு செலவுத் திட்டத்தை நிராகரிக்கும் அதிகாரம் வழங்கப்பட்டது.",
    "Members were given the power of discussing the annual financial statement (budget) and addressing questions to the executive.",
    "உறுப்பினர்களுக்கு வருடாந்திர நிதிநிலை அறிக்கையை (பட்ஜெட்) விவாதிக்கவும், நிர்வாகத்திடம் கேள்விகள் கேட்கவும் அதிகாரம் வழங்கப்பட்டது.",
    "Members were allowed to move resolutions on the budget and ask supplementary questions.",
    "உறுப்பினர்களுக்கு பட்ஜெட் மீது தீர்மானம் கொண்டு வரவும் கூடுதல் கேள்விகள் (துணைக் கேள்விகள்) கேட்கவும் அனுமதிக்கப்பட்டது.",
    "Financial powers were completely transferred to elected Indian provincial representatives.",
    "நிதி அதிகாரங்கள் தேர்ந்தெடுக்கப்பட்ட இந்திய மாகாணப் பிரதிநிதிகளுக்கு முழுமையாக மாற்றப்பட்டன.",
    "B",
    "The 1892 Act allowed council members to discuss the budget and address questions to the executive (with 6 days prior notice). However, members could NOT vote on the budget or ask supplementary questions (that came in 1909).",
    "1892 ஆம் ஆண்டு சட்டம் கவுன்சில் உறுப்பினர்களுக்கு பட்ஜெட் பற்றி விவாதிக்கவும், கேள்விகள் கேட்கவும் உரிமை அளித்தது (6 நாட்கள் முன் அறிவிப்புடன்). ஆனால் வாக்களிக்கும் உரிமையோ துணைக் கேள்விகள் கேட்கும் உரிமையோ வழங்கப்படவில்லை (அவை 1909 இல் வந்தன).",
    "Incorrect. Voting on demands for grants was introduced later by GOI Act 1919.",
    "தவறு. மானியக் கோரிக்கைகள் மீது வாக்களிக்கும் அதிகாரம் 1919 சட்டத்தில்தான் வந்தது.",
    "Correct. Allowed discussion of budget and asking questions to executive without voting or supplementary questions.",
    "சரி. பட்ஜெட் விவாதம் மற்றும் கேள்விகள் கேட்க அனுமதித்தது; வாக்களிக்கவோ துணைக் கேள்விகள் கேட்கவோ அனுமதியில்லை.",
    "Incorrect. Moving resolutions on budget and supplementary questions were allowed by Morley-Minto Reforms 1909.",
    "தவறு. தீர்மானங்கள் கொண்டுவருவதும் துணைக் கேள்விகள் கேட்பதும் 1909 மோர்லே-மிண்டோ சீர்திருத்தங்களால் அனுமதிக்கப்பட்டன.",
    "Incorrect. Financial powers were not transferred to elected Indians in 1892.",
    "தவறு. 1892 இல் நிதி அதிகாரங்கள் இந்தியர்களுக்கு மாற்றப்படவில்லை.",
    "1892 Act introduced an element of 'indirect election' through recommendations by local bodies, though the word 'election' was not explicitly used in the Act.",
    "1892 சட்டம் உள்ளாட்சி அமைப்புகளின் பரிந்துரைகள் மூலம் 'மறைமுக தேர்தல்' என்ற கூறைக் கொண்டு வந்தது ('தேர்தல்' என்ற சொல் பயன்படுத்தப்படவில்லை).",
    "Indian Councils Act 1892 increased non-official members in both Central and Provincial Legislative Councils.",
    "1892 சட்டம் மத்திய மற்றும் மாகாண சட்டமன்ற கவுன்சில்களில் அரசுசாரா உறுப்பினர்களின் எண்ணிக்கையை உயர்த்தியது.",
    "Understand", 60, ["Polity", "Historical Background", "Indian Councils Act 1892", "Budget Discussion"]
))

# Write early checkpoint
with open(target_path, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"Added {len(questions)} questions.")
