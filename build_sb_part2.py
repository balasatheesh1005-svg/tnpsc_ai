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
# PART 2: 15 THREE STATEMENT QUESTIONS (HB_SB_016 to HB_SB_030)
# =========================================================

# HB_SB_016
questions.append(make_q(
    "HB_SB_016", "Statement Based",
    "Consider the following statements regarding the Regulating Act 1773 and Amending Act 1781:\n1. The Regulating Act 1773 established a Supreme Court at Calcutta in 1774 comprising a Chief Justice and three other judges.\n2. The Amending Act 1781 exempted the Governor-General and his Executive Council from Supreme Court jurisdiction for official acts.\n3. The Amending Act 1781 mandated that the Supreme Court administer Hindu Law to Hindus and Mohammedan Law to Muslims.\nWhich of the statements given above are correct?",
    "1773 ஒழுங்குமுறைச் சட்டம் மற்றும் 1781 திருத்தச் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 1773 ஒழுங்குமுறைச் சட்டம் 1774 இல் கொல்கத்தாவில் ஒரு தலைமை நீதிபதி மற்றும் மூன்று நீதிபதிகளைக் கொண்ட உச்ச நீதிமன்றத்தை நிறுவியது.\n2. 1781 திருத்தச் சட்டம் கவர்னர் ஜெனரல் மற்றும் அவரது நிர்வாகக் குழுவை அவர்களின் அதிகாரப்பூர்வ பணிகளுக்காக உச்ச நீதிமன்ற அதிகார வரம்பிலிருந்து விலக்கியது.\n3. 1781 திருத்தச் சட்டம் உச்ச நீதிமன்றம் இந்துக்களுக்கு இந்து சட்டத்தையும் முஸ்லிம்களுக்கு இசுலாமிய சட்டத்தையும் வழங்க வேண்டும் எனக் கட்டாயப்படுத்தியது.\nஎது சரி?",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "D",
    "All three statements are correct. 1773 Act set up SC at Calcutta (1774), 1781 Amending Act (Act of Settlement) exempted official acts from SC jurisdiction and required administration of native personal laws.",
    "மூன்று கூற்றுகளும் சரியானவை. 1774 இல் உச்ச நீதிமன்ற அமைவு, 1781 இல் அதிகாரப்பூர்வ பணிகளுக்கு விலக்கு மற்றும் சுதேசி தனிநபர் சட்டங்கள் பயன்பாடு.",
    "Incorrect. Statement 3 is also correct.",
    "தவறு. கூற்று 3-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Correct. All three statements are historically true.",
    "சரி. மூன்று கூற்றுகளும் வரலாற்று ரீதியாகச் சரியானவை.",
    "Amending Act 1781 is also known as the Act of Settlement.",
    "1781 திருத்தச் சட்டம் 'சமரசச் சட்டம்' (Act of Settlement) என்றும் அழைக்கப்படுகிறது.",
    "Sir Elijah Impey was the first Chief Justice of the Supreme Court at Calcutta.",
    "சர் எலிஜா இம்பே கொல்கத்தா உச்ச நீதிமன்றத்தின் முதல் தலைமை நீதிபதி ஆவார்.",
    "Analyze", 75, ["Polity", "Historical Background", "Regulating Act 1773", "Three Statement"]
))

# HB_SB_017
questions.append(make_q(
    "HB_SB_017", "Statement Based",
    "Consider the following statements regarding the provisions of the Charter Act of 1813:\n1. It abolished the trade monopoly of the East India Company in India except for trade in tea and trade with China.\n2. It permitted Christian missionaries to enter India for the purpose of promoting moral and religious enlightenment.\n3. It allocated a financial grant of Rupees One Lakh per year for the promotion of education among Indian subjects.\nWhich of the statements given above are correct?",
    "1813 ஆம் ஆண்டின் சாசனச் சட்டத்தின் விதிகள் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது தேயிலை வர்த்தகம் மற்றும் சீனாவுடனான வர்த்தகம் தவிர இந்தியாவில் கிழக்கிந்தியக் கம்பெனியின் வர்த்தக ஏகபோகத்தை ஒழித்தது.\n2. இது ஒழுக்க மற்றும் சமய விழிப்புணர்வை ஏற்படுத்த கிறிஸ்தவ மிஷனரிகள் இந்தியாவிற்குள் நுழைய அனுமதித்தது.\n3. இது இந்தியர்களிடையே கல்வியை மேம்படுத்துவதற்காக ஆண்டுக்கு ரூ. 1 லட்சம் நிதியை ஒதுக்கியது.\nஎது சரி?",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "D",
    "All three statements are correct. Charter Act 1813 ended EIC monopoly except Tea/China trade, allowed Christian missionaries, and provided Rs 1 Lakh annually for education.",
    "மூன்று கூற்றுகளும் சரியானவை. தேயிலை/சீனா வர்த்தகம் தவிர ஏகபோக ஒழிப்பு, மிஷனரிகள் அனுமதி, மற்றும் கல்விக்கு ரூ. 1 லட்சம் ஒதுக்கீடு.",
    "Incorrect. Statement 3 is also correct.",
    "தவறு. கூற்று 3-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Correct. All three statements accurately reflect the Charter Act 1813.",
    "சரி. மூன்று கூற்றுகளும் 1813 சாசனச் சட்டத்தைத் துல்லியமாகப் பிரதிபலிக்கின்றன.",
    "Charter Act 1813 explicitly declared Crown sovereignty over East India Company territories in India.",
    "1813 சாசனச் சட்டம் கம்பெனி நிலப்பரப்புகள் மீது பிரிட்டிஷ் முடிஅரசின் இறையாண்மையை வெளிப்படையாக அறிவித்தது.",
    "1813 Charter Act was passed during the reign of King George III.",
    "1813 சாசனச் சட்டம் மூன்றாம் ஜார்ஜ் மன்னர் ஆட்சியில் நிறைவேற்றப்பட்டது.",
    "Analyze", 75, ["Polity", "Historical Background", "Charter Act 1813", "Three Statement"]
))

# HB_SB_018
questions.append(make_q(
    "HB_SB_018", "Statement Based",
    "Consider the following statements regarding the Charter Act of 1833:\n1. It ended all commercial trading activities of the East India Company, converting it into a purely administrative body.\n2. Section 87 of the Act provided that no Indian subject should be disabled from holding any place, office, or employment under the Company by reason of religion, place of birth, descent, or colour.\n3. It introduced Lord Macaulay as the Fourth (Law) Member in the Governor-General's Council.\nWhich of the statements given above are correct?",
    "1833 ஆம் ஆண்டின் சாசனச் சட்டத்தின் விதிகள் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது கிழக்கிந்தியக் கம்பெனியின் அனைத்து வர்த்தக நடவடிக்கைகளையும் முடிவுக்குக் கொண்டுவந்து, அதை ஒரு தூய நிர்வாக அமைப்பாக மாற்றியது.\n2. இச்சட்டத்தின் பிரிவு 87 மதம், பிறந்த இடம், இனம் அல்லது நிறம் அடிப்படையில் எந்தவொரு இந்தியருக்கும் வேலைவாய்ப்பு மறுக்கப்படக் கூடாது எனக் கூறியது.\n3. இது கவர்னர் ஜெனரல் கவுன்சிலில் லார்ட் மெக்காலேயை நான்காவது (சட்ட) உறுப்பினராக அறிமுகப்படுத்தியது.\nஎது சரி?",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "D",
    "All three statements are correct. Charter Act 1833 ended all EIC commercial operations, enacted Section 87 (first anti-discrimination provision), and added Lord Macaulay as Law Member.",
    "மூன்று கூற்றுகளும் சரியானவை. கம்பெனியின் வர்த்தகப் பணிகள் முற்றிலும் ரத்து, பிரிவு 87 பாகுபாடற்ற விதி, மற்றும் மெக்காலே சட்ட உறுப்பினராகச் சேர்க்கை.",
    "Incorrect. Statement 3 is also correct.",
    "தவறு. கூற்று 3-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Correct. All three statements accurately describe the landmark 1833 Charter Act.",
    "சரி. மூன்று கூற்றுகளும் 1833 சாசனச் சட்டத்தை துல்லியமாக விவரிக்கின்றன.",
    "Section 87 of Charter Act 1833 is regarded as the precursor to Article 15 and 16 of the modern Indian Constitution.",
    "1833 சாசனச் சட்டத்தின் பிரிவு 87 தற்போதைய 15 மற்றும் 16 விதிகளுக்கு முன்னோடியாகக் கருதப்படுகிறது.",
    "Lord Macaulay chaired the First Law Commission constituted under the 1833 Charter Act.",
    "1833 சாசனச் சட்டத்தின்கீழ் அமைக்கப்பட்ட முதல் சட்ட ஆணையத்திற்கு மெக்காலே பிரபு தலைமை தாங்கினார்.",
    "Analyze", 75, ["Polity", "Historical Background", "Charter Act 1833", "Three Statement"]
))

# HB_SB_019
questions.append(make_q(
    "HB_SB_019", "Statement Based",
    "Consider the following statements regarding the Charter Act of 1853:\n1. It created a separate Indian (Central) Legislative Council of six new members.\n2. It introduced local representation in the Central Legislative Council, with four members appointed by local governments of Madras, Bombay, Bengal, and Agra.\n3. It was the last of the series of Charter Acts passed by British Parliament between 1793 and 1853.\nWhich of the statements given above are correct?",
    "1853 ஆம் ஆண்டின் சாசனச் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது ஆறு புதிய உறுப்பினர்களைக் கொண்ட ஒரு தனி இந்திய (மத்திய) சட்டமன்ற கவுன்சிலை உருவாக்கியது.\n2. மதராஸ், பம்பாய், வங்காளம் மற்றும் ஆக்ரா உள்ளூர் அரசுகளால் நியமிக்கப்பட்ட நான்கு உறுப்பினர்களுடன் இது மத்திய சட்டமன்ற கவுன்சிலில் உள்ளூர் பிரதிநிதித்துவத்தை அறிமுகப்படுத்தியது.\n3. 1793 முதல் 1853 வரை பிரிட்டிஷ் பாராளுமன்றத்தால் நிறைவேற்றப்பட்ட சாசனச் சட்ட வரிசையில் இதுவே கடைசியானதாகும்.\nஎது சரி?",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "D",
    "All three statements are correct. Charter Act 1853 set up 6-member Legislative Council (Mini-Parliament), introduced local representation from 4 provinces, and was the final Charter Act.",
    "மூன்று கூற்றுகளும் சரியானவை. 6 உறுப்பினர்கள் சட்டமன்ற கவுன்சில் அமைப்பு, 4 மாகாண உள்ளூர் பிரதிநிதித்துவம், மற்றும் கடைசி சாசனச் சட்டம்.",
    "Incorrect. Statement 3 is also correct.",
    "தவறு. கூற்று 3-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Correct. All three statements are historically true.",
    "சரி. மூன்று கூற்றுகளும் வரலாற்று ரீதியாகச் சரியானவை.",
    "The 1853 Act did not specify any fixed time limit for Company rule (unlike earlier 20-year renewals), indicating Company rule could be terminated anytime by Parliament.",
    "1853 சட்டம் கம்பெனி ஆட்சிக்கு காலக்கெடு எதையும் குறிப்பிடவில்லை, இதனால் பாராளுமன்றம் விரும்பியபோது ஆட்சியைக் கலைக்க வழிவகுத்தது.",
    "Macaulay Committee on Indian Civil Service was appointed in 1854 following the 1853 Act.",
    "1853 சட்டத்தைத் தொடர்ந்து 1854 இல் இந்திய குடிமைப் பணிக்கான மெக்காலே குழு அமைக்கப்பட்டது.",
    "Analyze", 75, ["Polity", "Historical Background", "Charter Act 1853", "Three Statement"]
))

# HB_SB_020
questions.append(make_q(
    "HB_SB_020", "Statement Based",
    "Consider the following statements regarding the Government of India Act 1858:\n1. It was styled as the 'Act for the Good Government of India'.\n2. It created a new office, Secretary of State for India, who was a member of the British Cabinet and answerable to the British Parliament.\n3. Lord Canning became the first Viceroy of India under this Act.\nWhich of the statements given above are correct?",
    "1858 ஆம் ஆண்டின் இந்திய அரசுச் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது 'இந்தியாவின் நல்லாட்சிக்கான சட்டம்' என அழைக்கப்பட்டது.\n2. இது பிரிட்டிஷ் அமைச்சரவை உறுப்பினராகவும் பாராளுமன்றத்திற்குப் பொறுப்பானவராகவும் விளங்கிய இந்திய அரசுச் செயலாளர் என்ற புதிய பதவியை உருவாக்கியது.\n3. கேனிங் பிரபு இச்சட்டத்தின் கீழ் இந்தியாவின் முதல் வைஸ்ராயானார்.\nஎது சரி?",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "D",
    "All three statements are correct. GOI Act 1858 ('Good Government Act') created Secretary of State for India and made Lord Canning the first Viceroy.",
    "மூன்று கூற்றுகளும் சரியானவை. 'நல்லாட்சிச் சட்டம்' எனப்பட்டது, அரசுச் செயலாளர் பதவியை உருவாக்கியது, மற்றும் கேனிங் பிரபு முதல் வைஸ்ராயானார்.",
    "Incorrect. Statement 3 is also correct.",
    "தவறு. கூற்று 3-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Correct. All three statements accurately represent the 1858 Act.",
    "சரி. மூன்று கூற்றுகளும் 1858 அரசுச் சட்டத்தைச் சரியாகப் பிரதிபலிக்கின்றன.",
    "The 1858 Act constituted the Secretary of State in Council as a corporate body capable of suing and being sued in India and England.",
    "1858 சட்டம் அரசுச் செயலாளர் கவுன்சிலை வழக்காடத் தகுதியான ஒரு கார்ப்பரேட் அமைப்பாக ஆக்கியது.",
    "Queen Victoria's Proclamation of November 1, 1858 was read out by Lord Canning at Allahabad Durbar.",
    "1858 நவம்பர் 1 அன்று விக்டோரியா மகாராணியின் பிரகடனம் அலகாபாத் தர்பாரில் கேனிங் பிரபுவால் வாசிக்கப்பட்டது.",
    "Analyze", 75, ["Polity", "Historical Background", "Government of India Act 1858", "Three Statement"]
))

# Save checkpoint
questions.sort(key=lambda x: x["id"])
with open(target_path, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"Part 2 complete: {len(questions)} questions saved.")
