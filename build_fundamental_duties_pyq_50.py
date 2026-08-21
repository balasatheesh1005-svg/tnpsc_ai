import json
import os
import sys

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

def create_q(
    q_id, difficulty, q_type, question_en, question_ta,
    assertion_en, assertion_ta, reason_en, reason_ta,
    seq_correct_en, seq_correct_ta,
    seq_w1_en, seq_w1_ta,
    seq_w2_en, seq_w2_ta,
    seq_w3_en, seq_w3_ta,
    correct_pos,
    exp_en, exp_ta,
    wno_correct_en, wno_correct_ta,
    wno_w1_en, wno_w1_ta,
    wno_w2_en, wno_w2_ta,
    wno_w3_en, wno_w3_ta,
    tip_en, tip_ta,
    fact_en, fact_ta,
    src_ref, pyq_sim,
    bloom="Remember", time_sec=45
):
    seqs = {
        "correct": {"en": seq_correct_en, "ta": seq_correct_ta},
        "w1": {"en": seq_w1_en, "ta": seq_w1_ta},
        "w2": {"en": seq_w2_en, "ta": seq_w2_ta},
        "w3": {"en": seq_w3_en, "ta": seq_w3_ta}
    }
    
    wnos = {
        "correct": {"en": f"Correct. {wno_correct_en}", "ta": f"சரி. {wno_correct_ta}"},
        "w1": {"en": f"Incorrect. {wno_w1_en}", "ta": f"தவறு. {wno_w1_ta}"},
        "w2": {"en": f"Incorrect. {wno_w2_en}", "ta": f"தவறு. {wno_w2_ta}"},
        "w3": {"en": f"Incorrect. {wno_w3_en}", "ta": f"தவறு. {wno_w3_ta}"}
    }
    
    positions = ["A", "B", "C", "D"]
    pos_map = {}
    pos_map[correct_pos] = "correct"
    
    remaining_pos = [p for p in positions if p != correct_pos]
    remaining_keys = ["w1", "w2", "w3"]
    
    for p, k in zip(remaining_pos, remaining_keys):
        pos_map[p] = k
        
    options = []
    options_en = []
    options_ta = []
    why_not_others = {}
    
    for p in positions:
        k = pos_map[p]
        opt_en = seqs[k]["en"]
        opt_ta = seqs[k]["ta"]
        options.append({"id": p, "en": opt_en, "ta": opt_ta})
        options_en.append(opt_en)
        options_ta.append(opt_ta)
        why_not_others[p] = wnos[k]

    assertion_obj = {"en": assertion_en, "ta": assertion_ta} if assertion_en else {}
    reason_obj = {"en": reason_en, "ta": reason_ta} if reason_en else {}

    return {
        "id": q_id,
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": difficulty,
        "question_type": q_type,
        "question": {"en": question_en, "ta": question_ta},
        "assertion": assertion_obj,
        "reason": reason_obj,
        "options": options,
        "correct_answer": correct_pos,
        "explanation": {"en": exp_en, "ta": exp_ta},
        "why_not_others": why_not_others,
        "tnpsc_tip": {"en": tip_en, "ta": tip_ta},
        "revision_fact": {"en": fact_en, "ta": fact_ta},
        "source_reference": src_ref,
        "bloom_level": bloom,
        "estimated_time_sec": time_sec,
        "pyq_similarity": pyq_sim,
        "tags": ["Polity", "Fundamental Duties", "PYQ"],
        "question_en": question_en,
        "question_ta": question_ta,
        "options_en": options_en,
        "options_ta": options_ta,
        "answer": correct_pos.lower(),
        "explanation_en": exp_en,
        "explanation_ta": exp_ta
    }

questions = []

# Exact Answer Pattern for 50 questions:
# Target: A: 12, B: 12, C: 13, D: 13
# 1-4: A, B, C, D
# 5-8: A, B, C, D
# 9-12: A, B, C, D
# 13-16: A, B, C, D
# 17-20: A, B, C, D
# 21-24: A, B, C, D
# 25-28: A, B, C, D
# 29-32: A, B, C, D
# 33-36: A, B, C, D
# 37-40: A, B, C, D
# 41-44: A, B, C, D
# 45-48: A, B, C, D
# 49-50: C, D
# Sums: A: 12, B: 12, C: 13, D: 13. Total = 50. Absolutely perfect pattern!

# Q1 - Actual PYQ -> A
questions.append(create_q(
    "FD_PYQ_001", "Easy", "Direct MCQ",
    "Under which Constitutional Amendment Act were the Fundamental Duties incorporated into the Indian Constitution?",
    "எந்த அரசியலமைப்பு திருத்தச் சட்டத்தின் கீழ் இந்திய அரசியலமைப்பில் அடிப்படை கடமைகள் சேர்க்கப்பட்டன?",
    "", "", "", "",
    "42nd Constitutional Amendment Act, 1976", "42வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
    "44th Constitutional Amendment Act, 1978", "44வது அரசியலமைப்பு திருத்தச் சட்டம், 1978",
    "86th Constitutional Amendment Act, 2002", "86வது அரசியலமைப்பு திருத்தச் சட்டம், 2002",
    "97th Constitutional Amendment Act, 2011", "97வது அரசியலமைப்பு திருத்தச் சட்டம், 2011",
    "A",
    "Fundamental Duties were added to Part IVA (Article 51A) of the Constitution by the 42nd Constitutional Amendment Act, 1976, based on Swaran Singh Committee recommendations.",
    "ஸ்வரன் சிங் குழுவின் பரிந்துரைகளின் அடிப்படையில் 1976-ன் 42வது அரசியலமைப்பு திருத்தச் சட்டம் மூலம் பகுதி IVA-ல் (உறுப்பு 51A) அடிப்படை கடமைகள் சேர்க்கப்பட்டன.",
    "42nd CAA 1976 added Part IVA (Article 51A) containing 10 Fundamental Duties.", "42வது திருத்தம் 1976 10 அடிப்படை கடமைகளைக் கொண்ட பகுதி IVA-வைச் சேர்த்தது.",
    "44th CAA 1978 retained Fundamental Duties, but did not introduce them.", "44வது திருத்தம் 1978 கடமைகளைத் தக்கவைத்தது, ஆனால் அவற்றை அறிமுகப்படுத்தவில்லை.",
    "86th CAA 2002 added the 11th Fundamental Duty [Article 51A(k)].", "86வது திருத்தம் 2002 11வது அடிப்படை கடமையைச் சேர்த்தது.",
    "97th CAA 2011 added provisions regarding Co-operative Societies.", "97வது திருத்தம் 2011 கூட்டுறவு சங்கங்கள் பற்றிய விதிகளைச் சேர்த்தது.",
    "TNPSC Trap: Remember 42nd CAA 1976 introduced Part IVA with 10 duties, while 86th CAA 2002 added the 11th duty.",
    "TNPSC பொறி: 42வது திருத்தம் 1976 10 கடமைகளுடன் பகுதி IVA-வை அறிமுகப்படுத்தியது, 86வது திருத்தம் 2002 11வது கடமையைச் சேர்த்தது.",
    "Part IVA was added during the Internal Emergency (1975-77).",
    "உள்நாட்டு அவசரநிலையின் போது (1975-77) பகுதி IVA சேர்க்கப்பட்டது.",
    ["TNPSC Group 1 2022 PYQ", "M. Laxmikanth - Indian Polity"], "Actual PYQ", "Remember", 45
))

# Q2 - Actual PYQ -> B
questions.append(create_q(
    "FD_PYQ_002", "Easy", "Direct MCQ",
    "Which Committee recommended the inclusion of Fundamental Duties in the Constitution of India?",
    "இந்திய அரசியலமைப்பில் அடிப்படை கடமைகளைச் சேர்க்க பரிந்துரைத்த குழு எது?",
    "", "", "", "",
    "Sarkaria Commission", "சர்க்காரியா ஆணையம்",
    "Swaran Singh Committee", "ஸ்வரன் சிங் குழு",
    "Kothari Commission", "கோத்தாரி ஆணையம்",
    "Balwant Rai Mehta Committee", "பல்வந்த் ராய் மேத்தா குழு",
    "B",
    "The Swaran Singh Committee, set up by the Congress Party in 1976, recommended the inclusion of a separate chapter on Fundamental Duties in the Constitution.",
    "1976-ல் காங்கிரஸ் கட்சியால் அமைக்கப்பட்ட ஸ்வரன் சிங் குழு அரசியலமைப்பில் அடிப்படை கடமைகளுக்கான தனி அத்தியாயத்தைச் சேர்க்கப் பரிந்துரைத்தது.",
    "Swaran Singh Committee recommended inclusion of Fundamental Duties in 1976.", "ஸ்வரன் சிங் குழு 1976-ல் அடிப்படை கடமைகளைச் சேர்க்கப் பரிந்துரைத்தது.",
    "Sarkaria Commission recommended Centre-State relations reforms.", "சர்க்காரியா ஆணையம் மத்திய-மாநில உறவுகள் சீர்திருத்தங்களைப் பரிந்துரைத்தது.",
    "Kothari Commission recommended national education system structure.", "கோத்தாரி ஆணையம் தேசிய கல்விக் கட்டமைப்பைப் பரிந்துரைத்தது.",
    "Balwant Rai Mehta Committee recommended 3-tier Panchayati Raj system.", "பல்வந்த் ராய் மேத்தா குழு 3-அடுக்கு பஞ்சாயத்து ராஜ் அமைப்பைப் பரிந்துரைத்தது.",
    "TNPSC Trap: Swaran Singh Committee proposed 8 duties, but Parliament enacted 10 duties in 1976.",
    "TNPSC பொறி: ஸ்வரன் சிங் குழு 8 கடமைகளைப் பரிந்துரைத்தது, ஆனால் நாடாளுமன்றம் 10 கடமைகளை இயற்றியது.",
    "Sardar Swaran Singh was then Union Cabinet Minister.",
    "சர்தார் ஸ்வரன் சிங் அப்போது மத்திய அமைச்சராக இருந்தார்.",
    ["TNPSC Group 2 2018 PYQ", "Samacheer Kalvi"], "Actual PYQ", "Remember", 45
))

# Q3 - Actual PYQ -> C
questions.append(create_q(
    "FD_PYQ_003", "Easy", "Direct MCQ",
    "The 11th Fundamental Duty (Article 51A(k)) regarding child education was added by which Constitutional Amendment Act?",
    "குழந்தைகள் கல்வி பற்றிய 11வது அடிப்படை கடமை (உறுப்பு 51A(k)) எந்த அரசியலமைப்பு திருத்தச் சட்டத்தால் சேர்க்கப்பட்டது?",
    "", "", "", "",
    "84th Constitutional Amendment Act, 2001", "84வது அரசியலமைப்பு திருத்தச் சட்டம், 2001",
    "85th Constitutional Amendment Act, 2001", "85வது அரசியலமைப்பு திருத்தச் சட்டம், 2001",
    "86th Constitutional Amendment Act, 2002", "86வது அரசியலமைப்பு திருத்தச் சட்டம், 2002",
    "91st Constitutional Amendment Act, 2003", "91வது அரசியலமைப்பு திருத்தச் சட்டம், 2003",
    "C",
    "The 86th Constitutional Amendment Act, 2002 added Article 51A(k), imposing a duty on parents/guardians to provide education opportunities to children aged 6-14 years.",
    "2002-ன் 86வது அரசியலமைப்பு திருத்தச் சட்டம் உறுப்பு 51A(k)-ஐச் சேர்த்து, 6-14 வயதுடைய குழந்தைகளுக்குக் கல்விக்கான வாய்ப்புகளை வழங்க பெற்றோர்/பாதுகாவலர்களுக்குக் கடமையாக்கியது.",
    "86th CAA 2002 added Article 51A(k) as the 11th Fundamental Duty.", "86வது திருத்தம் 2002 உறுப்பு 51A(k)-ஐ 11வது கடமையாகச் சேர்த்தது.",
    "84th CAA 2001 froze constituency delimitation till 2026.", "84வது திருத்தம் 2001 தொகுதி மறுசீரமைப்பை 2026 வரை முடக்கியது.",
    "85th CAA 2001 provided consequential seniority in SC/ST promotions.", "85வது திருத்தம் 2001 SC/ST விளம்பரங்களில் தொடர் முன்னுரிமையை அளித்தது.",
    "91st CAA 2003 limited Council of Ministers size to 15% of Lok Sabha/Assembly.", "91வது திருத்தம் 2003 அமைச்சரவை அளவை 15% ஆகக் கட்டுப்படுத்தியது.",
    "TNPSC Trap: 86th CAA 2002 amended 3 Parts: Part III (Art 21A), Part IV (Art 45), and Part IVA [Art 51A(k)].",
    "TNPSC பொறி: 86வது திருத்தம் 2002 3 பகுதிகளைத் திருத்தியது: பகுதி III (உறுப்பு 21A), பகுதி IV (உறுப்பு 45), பகுதி IVA [உறுப்பு 51A(k)].",
    "Article 51A(k) came into effect in 2002.",
    "உறுப்பு 51A(k) 2002-ல் அமலுக்கு வந்தது.",
    ["TNPSC Group 1 2019 PYQ", "NCERT"], "Actual PYQ", "Remember", 45
))

# Q4 - Actual PYQ -> D
questions.append(create_q(
    "FD_PYQ_004", "Easy", "Direct MCQ",
    "Fundamental Duties are embodied in which Part and Article of the Indian Constitution?",
    "இந்திய அரசியலமைப்பின் எந்தப் பகுதி மற்றும் உறுப்பில் அடிப்படை கடமைகள் சேர்க்கப்பட்டுள்ளன?",
    "", "", "", "",
    "Part IV, Article 51", "பகுதி IV, உறுப்பு 51",
    "Part III, Article 32", "பகுதி III, உறுப்பு 32",
    "Part V, Article 52", "பகுதி V, உறுப்பு 52",
    "Part IVA, Article 51A", "பகுதி IVA, உறுப்பு 51A",
    "D",
    "Fundamental Duties are contained in Part IVA of the Constitution, which consists of a single Article, Article 51A.",
    "அடிப்படை கடமைகள் அரசியலமைப்பின் பகுதி IVA-ல் ஒரே ஒரு உறுப்பான 51A-ல் உள்ளன.",
    "Part IVA and Article 51A contain the Fundamental Duties.", "பகுதி IVA மற்றும் உறுப்பு 51A அடிப்படை கடமைகளைக் கொண்டுள்ளன.",
    "Part IV Article 51 deals with International Peace in DPSP.", "பகுதி IV உறுப்பு 51 DPSP-ல் சர்வதேச அமைதியைக் கையாள்கிறது.",
    "Part III Article 32 deals with Constitutional Remedies.", "பகுதி III உறுப்பு 32 அரசியலமைப்பு தீர்வுகளைக் கையாள்கிறது.",
    "Part V Article 52 deals with the President of India.", "பகுதி V உறுப்பு 52 இந்தியக் குடியரசுத் தலைவரைக் கையாள்கிறது.",
    "TNPSC Trap: Do not confuse Article 51 (DPSP - International Peace) with Article 51A (Fundamental Duties).",
    "TNPSC பொறி: உறுப்பு 51 (DPSP - சர்வதேச அமைதி) மற்றும் உறுப்பு 51A (அடிப்படை கடமைகள்) ஆகிய குழப்பக் கூடாது.",
    "Part IVA contains clauses (a) to (k) under Article 51A.",
    "பகுதி IVA உறுப்பு 51A-ன் கீழ் (a) முதல் (k) வரையிலான உட்பிரிவுகளைக் கொண்டுள்ளது.",
    ["TNPSC Group 4 2016 PYQ", "Samacheer Kalvi"], "Actual PYQ", "Remember", 45
))

# Q5 - Actual PYQ -> A
questions.append(create_q(
    "FD_PYQ_005", "Easy", "Direct MCQ",
    "Fundamental Duties in the Indian Constitution were borrowed from the Constitution of which country?",
    "இந்திய அரசியலமைப்பில் உள்ள அடிப்படை கடமைகள் எந்த நாட்டின் அரசியலமைப்பிலிருந்து ஈர்க்கப்பட்டன?",
    "", "", "", "",
    "Erstwhile USSR (Soviet Union)", "முந்தைய சோவியத் யூனியன் (USSR)",
    "United States of America", "அமெரிக்க ஐக்கிய நாடுகள்",
    "United Kingdom", "ஐக்கிய இராச்சியம்",
    "Australia", "ஆஸ்திரேலியா",
    "A",
    "The Fundamental Duties in the Indian Constitution were inspired by the Constitution of the erstwhile USSR (Soviet Union). Democratic Constitutions generally do not contain citizen duties.",
    "இந்திய அரசியலமைப்பின் அடிப்படை கடமைகள் முந்தைய சோவியத் யூனியனின் (USSR) அரசியலமைப்பிலிருந்து ஈர்க்கப்பட்டவை.",
    "Erstwhile USSR Constitution was the inspirational source for Fundamental Duties.", "சோவியத் யூனியன் அரசியலமைப்பே அடிப்படை கடமைகளுக்கான உத்வேக ஆதாரமாகும்.",
    "USA Constitution contains Bill of Rights, but no explicit Fundamental Duties.", "அமெரிக்க அரசியலமைப்பில் உரிமைகள் உள்ளன, ஆனால் கடமைகள் இல்லை.",
    "UK Constitution is unwritten and has no explicit Duty chapter.", "இங்கிலாந்து அரசியலமைப்பு எழுதப்படாதது, கடமைகள் அத்தியாயம் இல்லை.",
    "Australia Constitution contains no explicit Fundamental Duties chapter.", "ஆஸ்திரேலிய அரசியலமைப்பில் கடமைகள் அத்தியாயம் இல்லை.",
    "TNPSC Trap: Among major Western democracies, only Japan's Constitution explicitly contains citizen duties.",
    "TNPSC பொறி: மேற்கத்திய ஜனநாயக நாடுகளில் ஜப்பானின் அரசியலமைப்பு மட்டுமே வெளிப்படையாகக் கடமைகளைக் கொண்டுள்ளது.",
    "The USSR Constitution of 1936 contained duties alongside rights.",
    "1936-ன் சோவியத் அரசியலமைப்பு உரிமைகளுடன் கடமைகளையும் கொண்டிருந்தது.",
    ["TNPSC Group 1 2014 PYQ", "M. Laxmikanth"], "Actual PYQ", "Remember", 45
))

# Q6 - Actual PYQ -> B
questions.append(create_q(
    "FD_PYQ_006", "Easy", "Direct MCQ",
    "How many Fundamental Duties were originally added to the Indian Constitution by the 42nd Amendment Act in 1976?",
    "1976-ன் 42வது திருத்தச் சட்டம் மூலம் அசல் இந்திய அரசியலமைப்பில் எத்தனை அடிப்படை கடமைகள் சேர்க்கப்பட்டன?",
    "", "", "", "",
    "8", "8",
    "10", "10",
    "11", "11",
    "12", "12",
    "B",
    "The 42nd Constitutional Amendment Act, 1976 added 10 Fundamental Duties to Part IVA under Article 51A.",
    "1976-ன் 42வது அரசியலமைப்பு திருத்தச் சட்டம் உறுப்பு 51A-ன் கீழ் பகுதி IVA-ல் 10 அடிப்படை கடமைகளைச் சேர்த்தது.",
    "10 duties were originally enacted by Parliament in 1976.", "1976-ல் நாடாளுமன்றத்தால் 10 கடமைகள் இயற்றப்பட்டன.",
    "8 duties were recommended by Swaran Singh Committee, but 10 were enacted.", "ஸ்வரன் சிங் குழு 8 கடமைகளைப் பரிந்துரைத்தது, ஆனால் 10 இயற்றப்பட்டன.",
    "11 is the present total count of duties after 86th CAA 2002.", "2002-ன் 86வது திருத்தத்திற்குப் பிறகு தற்போதைய மொத்த கடமைகள் 11.",
    "12 was never the duty count.", "12 கடமைகள் எண்ணிக்கை அல்ல.",
    "TNPSC Trap: Swaran Singh recommended 8; 42nd CAA added 10; 86th CAA added 11th duty.",
    "TNPSC பொறி: ஸ்வரன் சிங் பரிந்துரைத்தது 8; 42வது திருத்தம் சேர்த்தது 10; 86வது திருத்தம் 11வது கடமையைச் சேர்த்தது.",
    "The 10 duties were codified under Article 51A clauses (a) to (j).",
    "10 கடமைகளும் உறுப்பு 51A உட்பிரிவுகள் (a) முதல் (j) வரை குறியாக்கம் செய்யப்பட்டன.",
    ["TNPSC Group 2 2022 PYQ", "Samacheer Kalvi"], "Actual PYQ", "Remember", 45
))

# Q7 - PYQ Pattern -> C
questions.append(create_q(
    "FD_PYQ_007", "Medium", "Two-Statement",
    "Consider the following statements regarding the origin of Fundamental Duties:\n\n1. Fundamental Duties were not included in the original Constitution adopted in 1949.\n2. The Swaran Singh Committee recommended 8 duties, but Parliament incorporated 10 duties in 1976.\n\nWhich of the statement(s) given above is/are correct?",
    "அடிப்படை கடமைகளின் தோற்றம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n\n1. 1949-ல் ஏற்றுக்கொள்ளப்பட்ட அசல் அரசியலமைப்பில் அடிப்படை கடமைகள் சேர்க்கப்படவில்லை.\n2. ஸ்வரன் சிங் குழு 8 கடமைகளைப் பரிந்துரைத்தது, ஆனால் 1976-ல் நாடாளுமன்றம் 10 கடமைகளை இணைத்தது.\n\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானவை?",
    "", "", "", "",
    "1 only", "1 மட்டும்",
    "2 only", "2 மட்டும்",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "Neither 1 nor 2", "எதுவும் இல்லை",
    "C",
    "Both statements are correct. Original Constitution had no Part IVA. Swaran Singh Committee recommended 8 duties, but 42nd CAA 1976 enacted 10 duties.",
    "இரண்டு கூற்றுகளும் சரியானவை. அசல் அரசியலமைப்பில் பகுதி IVA இல்லை. ஸ்வரன் சிங் குழு 8 கடமைகளைப் பரிந்துரைத்தது, ஆனால் 42வது திருத்தம் 10 கடமைகளை இயற்றியது.",
    "Statement 1 is factually true; Part IVA was missing in 1949.", "கூற்று 1 சரியானது; 1949-ல் பகுதி IVA இல்லை.",
    "Statement 2 is factually true regarding Swaran Singh proposal vs 42nd CAA enactment.", "ஸ்வரன் சிங் பரிந்துரை vs 42வது திருத்த இயற்றல் பற்றிய கூற்று 2 சரியானது.",
    "Both 1 and 2 are true.", "1 மற்றும் 2 இரண்டும் சரியானவை.",
    "Neither is false.", "எதுவும் தவறல்ல.",
    "TNPSC Trap: Swaran Singh Committee recommended tax paying duty, which Parliament omitted.",
    "TNPSC பொறி: ஸ்வரன் சிங் குழு வரி செலுத்தும் கடமையை பரிந்துரைத்தது, ஆனால் நாடாளுமன்றம் அதைத் தவிர்த்தது.",
    "Part IVA was introduced based on the 1976 committee report.",
    "1976 குழு அறிக்கையின் அடிப்படையில் பகுதி IVA அறிமுகப்படுத்தப்பட்டது.",
    ["TNPSC Group 1 Pattern", "M. Laxmikanth"], "PYQ Pattern", "Understand", 45
))

# Q8 - PYQ Pattern -> D
questions.append(create_q(
    "FD_PYQ_008", "Medium", "Match",
    "Match List I (Article 51A Clause) with List II (Duty Subject Matter):\n\nList I:\na. Article 51A(a)\nb. Article 51A(e)\nc. Article 51A(g)\nd. Article 51A(k)\n\nList II:\n1. National Flag & Anthem\n2. Dignity of women & Brotherhood\n3. Protect natural environment & compassion\n4. Education to child (6-14 years)",
    "பட்டியல் I-ஐ (உறுப்பு 51A உட்பிரிவு) பட்டியல் II உடன் (கடமையின் பொருள்) பொருத்துக:\n\nபட்டியல் I:\na. உறுப்பு 51A(a)\nb. உறுப்பு 51A(e)\nc. உறுப்பு 51A(g)\nd. உறுப்பு 51A(k)\n\nபட்டியல் II:\n1. தேசியக் கொடி & கீதம்\n2. பெண்களின் கண்ணியம் & சகோதரத்துவம்\n3. இயற்கைச் சூழல் பாதுகாப்பு & கருணை\n4. குழந்தைக்குக் கல்வி (6-14 ஆண்டுகள்)",
    "", "", "", "",
    "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
    "a-1, b-3, c-2, d-4", "a-1, b-3, c-2, d-4",
    "a-4, b-2, c-3, d-1", "a-4, b-2, c-3, d-1",
    "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
    "D",
    "Correct match: Art 51A(a) -> National Flag & Anthem (1); Art 51A(e) -> Women dignity & Brotherhood (2); Art 51A(g) -> Protect environment & compassion (3); Art 51A(k) -> Education to child (4). Sequence: 1-2-3-4.",
    "சரியான பொருத்தம்: உறுப்பு 51A(a) -> தேசியக் கொடி & கீதம் (1); உறுப்பு 51A(e) -> பெண்களின் கண்ணியம் & சகோதரத்துவம் (2); உறுப்பு 51A(g) -> இயற்கைச் சூழல் பாதுகாப்பு (3); உறுப்பு 51A(k) -> குழந்தைக்குக் கல்வி (4). வரிசை: 1-2-3-4.",
    "a-1, b-2, c-3, d-4 is the exact verified matching pair sequence.", "a-1, b-2, c-3, d-4 என்பது சரிபார்க்கப்பட்ட சரியான பொருத்த வரிசையாகும்.",
    "a-2 mismatch.", "a-2 தவறான பொருத்தம்.",
    "b-3 mismatch.", "b-3 தவறான பொருத்தம்.",
    "a-4 mismatch.", "a-4 தவறான பொருத்தம்.",
    "TNPSC Trap: Match questions require precise clause-to-subject association.",
    "TNPSC பொறி: பொருத்துக வினாக்கள் துல்லியமான உட்பிரிவு-பொருள் தொடர்பைக் கோருகின்றன.",
    "Each clause in Article 51A addresses a specific civic or moral sphere.",
    "உறுப்பு 51A-ன் ஒவ்வொரு உட்பிரிவும் ஒரு குறிப்பிட்ட குடிமை அல்லது தர்மக் களத்தைக் கையாள்கிறது.",
    ["TNPSC Group 1 Pattern", "NCERT"], "PYQ Pattern", "Analyze", 60
))

# Q9 - PYQ Pattern -> A
questions.append(create_q(
    "FD_PYQ_009", "Medium", "Assertion & Reason",
    "Assertion (A): Fundamental Duties under Part IVA of the Constitution are non-justiciable in nature.\nReason (R): There is no constitutional provision for their direct enforcement by courts upon non-performance by a citizen.",
    "கூற்று (A): அரசியலமைப்பின் பகுதி IVA-ன் கீழ் உள்ள அடிப்படை கடமைகள் இயல்பிலேயே நீதிமன்றத்தால் நேரடியாக அமல்படுத்தப்பட முடியாதவை.\nகாரணம் (R): ஒரு குடிமகன் கடமையைச் செய்யத் தவறினால் அதை நீதிமன்றங்கள் நேரடியாக அமல்படுத்துவதற்கான அரசியலமைப்பு விதி எதுவும் இல்லை.",
    "Fundamental Duties under Part IVA of the Constitution are non-justiciable in nature.",
    "அரசியலமைப்பின் பகுதி IVA-ன் கீழ் உள்ள அடிப்படை கடமைகள் இயல்பிலேயே நீதிமன்றத்தால் நேரடியாக அமல்படுத்தப்பட முடியாதவை.",
    "There is no constitutional provision for their direct enforcement by courts upon non-performance by a citizen.",
    "ஒரு குடிமகன் கடமையைச் செய்யத் தவறினால் அதை நீதிமன்றங்கள் நேரடியாக அமல்படுத்துவதற்கான அரசியலமைப்பு விதி எதுவும் இல்லை.",
    "Both A and R are correct and R is the correct explanation of A", "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்.",
    "Both A and R are correct but R is NOT the correct explanation of A", "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல.",
    "A is correct but R is incorrect", "A சரி, ஆனால் R தவறு.",
    "A is incorrect but R is correct", "A தவறு, ஆனால் R சரி.",
    "A",
    "Both A and R are true, and R explains A. Non-justiciable means citizens cannot be directly sued in court for violating Article 51A unless Parliament enacts an enforcing law.",
    "கூற்று A மற்றும் காரணம் R இரண்டும் சரி, மேலும் R என்பது A-விற்கு சரியான விளக்கம். அமல்படுத்த முடியாதது என்றால் நாடாளுமன்றம் தனியாகச் சட்டம் இயற்றாத வரை நேரடியாக வழக்கு தொடர முடியாது.",
    "Both A and R are true, and R explains why duties are non-justiciable.", "A மற்றும் R இரண்டும் சரி, மேலும் கடமைகள் ஏன் அமல்படுத்த முடியாதவை என்பதை R விளக்குகிறது.",
    "R directly explains A.", "R நேரடியாக A-வை விளக்குகிறது.",
    "R is factually true.", "R உண்மையானது.",
    "A is factually true.", "A உண்மையானது.",
    "TNPSC Trap: Non-justiciable does not mean legally useless; Parliament can enact statutory laws to enforce duties.",
    "TNPSC பொறி: அமல்படுத்த முடியாதது என்பதால் சட்டப்பயன் அற்றது எனப் பொருளல்ல; நாடாளுமன்றம் கடமைகளை அமல்படுத்தச் சட்டங்களை இயற்றலாம்.",
    "DPSPs in Part IV and Fundamental Duties in Part IVA are both non-justiciable.",
    "பகுதி IV DPSP மற்றும் பகுதி IVA அடிப்படை கடமைகள் இரண்டும் நேரடியாக அமல்படுத்த முடியாதவை.",
    ["TNPSC Group 1 Pattern", "M. Laxmikanth"], "PYQ Pattern", "Analyze", 60
))

# Q10 - Actual PYQ -> B
questions.append(create_q(
    "FD_PYQ_010", "Easy", "Direct MCQ",
    "Which one of the following is NOT a Fundamental Duty listed under Article 51A of the Indian Constitution?",
    "இந்திய அரசியலமைப்பின் உறுப்பு 51A-ன் கீழ் பட்டியலிடப்பட்டுள்ள அடிப்படை கடமைகளில் இல்லாதது எது?",
    "", "", "", "",
    "To respect the National Flag and National Anthem", "தேசியக் கொடி மற்றும் தேசிய கீதத்தை மதிக்க வேண்டும்",
    "To cast vote in general elections", "பொதுத் தேர்தல்களில் வாக்களிக்க வேண்டும்",
    "To protect and improve the natural environment", "இயற்கைச் சூழலைப் பாதுகாக்கவும் மேம்படுத்தவும் வேண்டும்",
    "To safeguard public property and abjure violence", "பொதுச் சொத்தைப் பாதுகாக்கவும் வன்முறையைக் கைவிடவும் வேண்டும்",
    "B",
    "Casting vote in general elections is NOT a Fundamental Duty in Article 51A. (NCRWC recommended it in 2002, but Parliament never enacted it).",
    "பொதுத் தேர்தல்களில் வாக்களிப்பது உறுப்பு 51A-ல் அடிப்படை கடமை அல்ல. (2002-ல் NCRWC பரிந்துரைத்தது, ஆனால் நாடாளுமன்றம் அதைச் சேர்க்கவில்லை).",
    "Casting vote is a constitutional/statutory right under Art 326/RPA 1951, NOT a Fundamental Duty.", "வாக்களிப்பது உறுப்பு 326/RPA 1951-ன் கீழ் உரிமையாகும், அடிப்படை கடமை அல்ல.",
    "Respecting Flag/Anthem is Art 51A(a).", "கொடி/கீதத்தை மதிப்பது உறுப்பு 51A(a).",
    "Protecting environment is Art 51A(g).", "சுற்றுச்சூழலைப் பாதுகாப்பது உறுப்பு 51A(g).",
    "Safeguarding public property is Art 51A(i).", "பொதுச் சொத்தைப் பாதுகாப்பது உறுப்பு 51A(i).",
    "TNPSC Trap: Duty to vote and duty to pay taxes were recommended by committees, but NEVER included in Article 51A.",
    "TNPSC பொறி: வாக்களிக்கும் கடமை மற்றும் வரி செலுத்தும் கடமை பரிந்துரைக்கப்பட்டன, ஆனால் உறுப்பு 51A-ல் சேர்க்கப்படவில்லை.",
    "Right to vote in India is a constitutional right under Article 326.",
    "இந்தியாவில் வாக்களிக்கும் உரிமை உறுப்பு 326-ன் கீழ் அரசியலமைப்பு உரிமையாகும்.",
    ["TNPSC Group 1 2017 PYQ", "Samacheer Kalvi"], "Actual PYQ", "Remember", 45
))

# Q11 - PYQ Pattern -> C
questions.append(create_q(
    "FD_PYQ_011", "Medium", "Three-Statement",
    "Consider the following statements regarding environmental preservation under Article 51A(g):\n\n1. Article 51A(g) explicitly obligates citizens to protect four natural elements: forests, lakes, rivers, and wildlife.\n2. Article 51A(g) mandates citizens to have compassion for living creatures.\n3. Article 48A in Part IV directs the State to protect and improve the environment and safeguard forests and wildlife.\n\nWhich of the statements given above are correct?",
    "உறுப்பு 51A(g)-ன் கீழ் சுற்றுச்சூழல் பாதுகாப்பு பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n\n1. உறுப்பு 51A(g) நான்கு இயற்கை கூறுகளைப் (காடுகள், ஏரிகள், ஆறுகள், வனவிலங்குகள்) பாதுகாக்கக் குடிமக்களுக்குக் கடமையாக்குகிறது.\n2. உறுப்பு 51A(g) உயிரினங்களிடம் கருணை காட்டுவதைக் குடிமக்களுக்குக் கட்டாயமாக்குகிறது.\n3. பகுதி IV-ல் உள்ள உறுப்பு 48A சுற்றுச்சூழலைப் பாதுகாக்கவும் காடுகள், வனவிலங்குகளைப் பேணவும் அரசை வழிகாட்டுகிறது.\n\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
    "", "", "", "",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "C",
    "All three statements are correct. Article 51A(g) [Citizen duty] covers forests, lakes, rivers, wildlife, and compassion. Article 48A [State DPSP duty] covers environment, forests, and wildlife.",
    "மூன்று கூற்றுகளும் சரியானவை. உறுப்பு 51A(g) [குடிமகன் கடமை] காடுகள், ஏரிகள், ஆறுகள், வனவிலங்குகள், கருணையைக் குறிக்கிறது. உறுப்பு 48A [அரசு நெறிமுறை] சுற்றுச்சூழல், காடுகள், வனவிலங்குகளைக் குறிக்கிறது.",
    "All three statements (1, 2, and 3) are true.", "மூன்று கூற்றுகளும் (1, 2, மற்றும் 3) சரியானவை.",
    "Statement 1 is correct (4 elements in 51A(g)).", "கூற்று 1 சரி (51A(g)-ல் 4 கூறுகள்).",
    "Statement 2 is correct (compassion clause).", "கூற்று 2 சரி (கருணை விதி).",
    "Statement 3 is correct (Art 48A DPSP).", "கூற்று 3 சரி (உறுப்பு 48A DPSP).",
    "TNPSC Trap: Article 51A(g) includes 'lakes and rivers', whereas Article 48A does not explicitly mention lakes and rivers.",
    "TNPSC பொறி: உறுப்பு 51A(g) 'ஏரிகள் மற்றும் ஆறுகளைக்' குறிப்பிடுகிறது, ஆனால் உறுப்பு 48A அவற்றை வெளிப்படையாகக் குறிப்பிடவில்லை.",
    "Both Art 48A and Art 51A(g) were added by the 42nd Amendment Act, 1976.",
    "உறுப்பு 48A மற்றும் 51A(g) இரண்டும் 1976-ன் 42வது திருத்தத்தால் சேர்க்கப்பட்டன.",
    ["TNPSC Group 1 Pattern", "NCERT"], "PYQ Pattern", "Analyze", 60
))

# Q12 - Actual PYQ -> D
questions.append(create_q(
    "FD_PYQ_012", "Medium", "Direct MCQ",
    "The Justice Verma Committee (1999) was appointed primarily for which purpose regarding Fundamental Duties?",
    "அடிப்படை கடமைகள் தொடர்பாக நீதியரசர் வர்மா குழு (1999) முதன்மையாக எந்த நோக்கத்திற்காக நியமிக்கப்பட்டது?",
    "", "", "", "",
    "To draft 5 new fundamental duties", "5 புதிய அடிப்படை கடமைகளை வரைவு செய்ய",
    "To make Fundamental Duties justiciable via writs", "நீதிப்பேராணைகள் மூலம் கடமைகளை அமல்படுத்தக்கூடியதாக்க",
    "To recommend deleting Part IVA", "பகுதி IVA-வை நீக்கப் பரிந்துரைக்க",
    "To operationalize strategy for teaching Fundamental Duties in educational institutions and identify existing statutory enforcers", "கல்வி நிறுவனங்களில் அடிப்படை கடமைகளைக் கற்பிப்பதற்கான உத்தியை நடைமுறைப்படுத்தவும் நிலவும் சட்ட அமலாக்கிகளை அடையவும்",
    "D",
    "The Justice Verma Committee (1999) was set up to plan strategy for teaching Fundamental Duties and identified existing Parliamentary Acts (like Wildlife Act, IPC, RPA, Insults to National Honour Act) that enforce duties.",
    "வர்மா குழு (1999) அடிப்படை கடமைகளைக் கற்பிப்பதற்கான உத்தியை வகுக்கவும், கடமைகளை அமல்படுத்தும் நிலவும் நாடாளுமன்றச் சட்டங்களை (வனவிலங்கு சட்டம், IPC, RPA, தேசிய சின்னங்கள் அவமதிப்பு சட்டம் போன்றவை) சுட்டிக்காட்டவும் அமைக்கப்பட்டது.",
    "Verma Committee planned educational teaching strategy and mapped existing statutory laws enforcing duties.", "வர்மா குழு கல்விக் கற்பித்தல் உத்தியை வகுத்து கடமைகளை அமல்படுத்தும் சட்டங்களை வரைபடமாக்கியது.",
    "No new duties were drafted by Verma Committee.", "வர்மா குழு புதிய கடமைகளை வரைவு செய்யவில்லை.",
    "Verma Committee did not recommend writ enforcement against citizens.", "குடிமக்களுக்கு எதிராக நீதிப்பேராணை அமலாக்கத்தை வர்மா குழு பரிந்துரைக்கவில்லை.",
    "Verma Committee supported retaining and teaching Part IVA.", "பகுதி IVA-வை தக்கவைத்து கற்பிப்பதை வர்மா குழு ஆதரித்தது.",
    "TNPSC Trap: Verma Committee (1999) did NOT propose amending Article 51A, but focused on operationalizing duties through law and education.",
    "TNPSC பொறி: வர்மா குழு (1999) உறுப்பு 51A-ஐ திருத்த பரிந்துரைக்கவில்லை, சட்டம் மற்றும் கல்வி மூலம் நடைமுறைப்படுத்துவதில் கவனம் செலுத்தியது.",
    "Verma Committee report was submitted in 1999.",
    "வர்மா குழு அறிக்கை 1999-ல் சமர்ப்பிக்கப்பட்டது.",
    ["TNPSC Group 2 2019 PYQ", "M. Laxmikanth"], "Actual PYQ", "Understand", 45
))

# Q13 - PYQ Pattern -> A
questions.append(create_q(
    "FD_PYQ_013", "Medium", "Chronology",
    "Arrange the following historical milestones of Fundamental Duties in chronological order:\n\n1. Appointment of Swaran Singh Committee\n2. Enactment of 42nd Amendment Act\n3. Appointment of Justice Verma Committee\n4. Enactment of 86th Amendment Act",
    "அடிப்படை கடமைகளின் பின்வரும் வரலாற்று மைல்கற்களை காலவரிசைப்படி வரிசைப்படுத்துக:\n\n1. ஸ்வரன் சிங் குழு நியமனம்\n2. 42வது திருத்தச் சட்டம் இயற்றப்படுதல்\n3. நீதியரசர் வர்மா குழு நியமனம்\n4. 86வது திருத்தச் சட்டம் இயற்றப்படுதல்",
    "", "", "", "",
    "1 - 2 - 3 - 4", "1 - 2 - 3 - 4",
    "2 - 1 - 4 - 3", "2 - 1 - 4 - 3",
    "1 - 3 - 2 - 4", "1 - 3 - 2 - 4",
    "3 - 1 - 2 - 4", "3 - 1 - 2 - 4",
    "A",
    "Chronological sequence: 1. Swaran Singh Committee (1976) -> 2. 42nd CAA (1976) -> 3. Justice Verma Committee (1998-1999) -> 4. 86th CAA (2002). Sequence: 1 - 2 - 3 - 4.",
    "காலவரிசை: 1. ஸ்வரன் சிங் குழு (1976) -> 2. 42வது திருத்தம் (1976) -> 3. வர்மா குழு (1998-1999) -> 4. 86வது திருத்தம் (2002). வரிசை: 1 - 2 - 3 - 4.",
    "1 - 2 - 3 - 4 is the exact chronological sequence.", "1 - 2 - 3 - 4 என்பது சரியான காலவரிசையாகும்.",
    "2 - 1 is reverse (42nd CAA came after committee).", "2 - 1 தலைகீழ் (குழுவிற்குப் பிறகே 42வது திருத்தம் வந்தது).",
    "3 is 1998, which is after 1976.", "3 என்பது 1998, அது 1976-க்கு பிறகானது.",
    "3 - 1 is incorrect.", "3 - 1 தவறானது.",
    "TNPSC Trap: Swaran Singh Committee was set up in 1976; 42nd CAA passed in 1976; Verma Committee set up in 1998; 86th CAA passed in 2002.",
    "TNPSC பொறி: ஸ்வரன் சிங் குழு 1976; 42வது திருத்தம் 1976; வர்மா குழு 1998; 86வது திருத்தம் 2002.",
    "The sequence spans 1976 to 2002.",
    "இவ்வரிசை 1976 முதல் 2002 வரை நீடிக்கிறது.",
    ["TNPSC Group 1 Pattern", "Samacheer Kalvi"], "PYQ Pattern", "Analyze", 60
))

# Q14 - PYQ Pattern -> B
questions.append(create_q(
    "FD_PYQ_014", "Hard", "Case Application",
    "Which landmark Supreme Court decision held that standing up respectfully during the National Anthem satisfies Article 51A(a), and non-singing on genuine religious grounds is protected under Article 25?",
    "தேசிய கீதத்தின் போது மரியாதையுடன் எழுந்து நிற்பதே உறுப்பு 51A(a)-ஐ நிறைவேற்றுகிறது, மேலும் உண்மையான மத நம்பிக்கையின் அடிப்படையில் பாடாமல் இருப்பது உறுப்பு 25-ன் கீழ் பாதுகாக்கப்படுகிறது என்று தீர்ப்பளித்த முக்கிய உச்சநீதிமன்ற வழக்கு எது?",
    "", "", "", "",
    "Minerva Mills v. Union of India (1980)", "மினர்வா மில்ஸ் எதிராக இந்திய யூனியன் (1980)",
    "Bijoe Emmanuel v. State of Kerala (1986)", "பிஜோய் இம்மானுவேல் எதிராக கேரள மாநிலம் (1986)",
    "Kesavananda Bharati v. State of Kerala (1973)", "கேசவாநந்த பாரதி எதிராக கேரள மாநிலம் (1973)",
    "Maneka Gandhi v. Union of India (1978)", "மேனகா காந்தி எதிராக இந்திய யூனியன் (1978)",
    "B",
    "In Bijoe Emmanuel v. State of Kerala (1986), the Supreme Court ruled that Jehovah's Witness students standing respectfully during the anthem fulfilled Article 51A(a), and compelling them to sing violated Article 25.",
    "பிஜோய் இம்மானுவேல் வழக்கில் (1986), தேசிய கீதத்தின் போது மரியாதையுடன் எழுந்து நிற்பதே உறுப்பு 51A(a)-ஐ நிறைவேற்றுகிறது என்றும், பாடக் வற்புறுத்துவது உறுப்பு 25-ஐ மீறுகிறது என்றும் உச்சநீதிமன்றம் தீர்ப்பளித்தது.",
    "Bijoe Emmanuel (1986) is the landmark precedent on Art 51A(a) National Anthem vs Art 25 religious freedom.", "பிஜோய் இம்மானுவேல் (1986) தேசிய கீதம் உறுப்பு 51A(a) vs உறுப்பு 25 மத சுதந்திரம் பற்றிய முக்கிய வழக்கு முன்மாதிரியாகும்.",
    "Minerva Mills (1980) dealt with Basic Structure and FR-DPSP balance.", "மினர்வா மில்ஸ் (1980) அடிப்படை அமைப்பு மற்றும் FR-DPSP சமநிலை பற்றியது.",
    "Kesavananda Bharati (1973) established Basic Structure Doctrine.", "கேசவாநந்த பாரதி (1973) அடிப்படை அமைப்புக் கோட்பாட்டை உருவாக்கியது.",
    "Maneka Gandhi (1978) expanded Article 21 personal liberty.", "மேனகா காந்தி (1978) உறுப்பு 21 தனிநபர் சுதந்திரத்தை விரிவுபடுத்தியது.",
    "TNPSC Trap: Standing up shows proper respect under 51A(a); vocal singing cannot be compelled against genuine religious conscience.",
    "TNPSC பொறி: எழுந்து நிற்பதே 51A(a)-ன் கீழ் மரியாதையைக் காட்டுகிறது; மத நம்பிக்கைக்கு எதிராகப் பாட வற்புறுத்த முடியாது.",
    "Judgment delivered by Justice O. Chinnappa Reddy.",
    "தீர்ப்பை நீதியரசர் ஓ. சின்னப்ப ரெட்டி வழங்கினார்.",
    ["TNPSC Group 1 Pattern", "M. Laxmikanth"], "PYQ Pattern", "Analyze", 60
))

# Q15 - Actual PYQ -> C
questions.append(create_q(
    "FD_PYQ_015", "Easy", "Direct MCQ",
    "Which recommendation of the Swaran Singh Committee was REJECTED by Parliament while enacting the 42nd Amendment Act in 1976?",
    "1976-ல் 42வது திருத்தச் சட்டத்தை இயற்றும் போது நாடாளுமன்றத்தால் நிராகரிக்கப்பட்ட ஸ்வரன் சிங் குழுவின் பரிந்துரை எது?",
    "", "", "", "",
    "Duty to respect the Constitution", "அரசியலமைப்பை மதிக்கும் கடமை",
    "Duty to safeguard public property", "பொதுச் சொத்தைப் பாதுகாக்கும் கடமை",
    "Duty to pay taxes", "வரி செலுத்தும் கடமை",
    "Duty to defend the country", "தேசத்தைப் பாதுகாக்கும் கடமை",
    "C",
    "The Swaran Singh Committee recommended that 'duty to pay taxes' should be a Fundamental Duty, but Parliament REJECTED this recommendation and omitted it from Article 51A.",
    "ஸ்வரன் சிங் குழு 'வரி செலுத்தும் கடமையை' அடிப்படை கடமையாக்கப் பரிந்துரைத்தது, ஆனால் நாடாளுமன்றம் இப்பரிந்துரையை நிராகரித்து உறுப்பு 51A-லிருந்து தவிர்த்தது.",
    "Duty to pay taxes was recommended by Swaran Singh Committee but rejected by Parliament.", "வரி செலுத்தும் கடமை ஸ்வரன் சிங் குழுவால் பரிந்துரைக்கப்பட்டது ஆனால் நாடாளுமன்றத்தால் நிராகரிக்கப்பட்டது.",
    "Respecting Constitution was enacted under Art 51A(a).", "அரசியலமைப்பை மதிப்பது உறுப்பு 51A(a)-ன் கீழ் இயற்றப்பட்டது.",
    "Safeguarding public property was enacted under Art 51A(i).", "பொதுச் சொத்தைப் பாதுகாப்பது உறுப்பு 51A(i)-ன் கீழ் இயற்றப்பட்டது.",
    "Defending country was enacted under Art 51A(d).", "தேசத்தைப் பாதுகாப்பது உறுப்பு 51A(d)-ன் கீழ் இயற்றப்பட்டது.",
    "TNPSC Trap: Parliament also rejected Swaran Singh's proposal to empower Parliament to impose penalties/imprisonment for non-performance of duties.",
    "TNPSC பொறி: கடமைகளைச் செய்யாதவருக்குத் தண்டனை விதிக்கும் நாடாளுமன்ற அதிகாரப் பரிந்துரையையும் நாடாளுமன்றம் நிராகரித்தது.",
    "Paying taxes remains a statutory obligation under Income Tax Act 1961, but not a constitutional Fundamental Duty.",
    "வரி செலுத்துவது வருமான வரிச் சட்டம் 1961-ன் கீழ் சட்டக் கடமையாகும், ஆனால் அரசியலமைப்பு அடிப்படை கடமையல்ல.",
    ["TNPSC Group 1 2021 PYQ", "Samacheer Kalvi"], "Actual PYQ", "Remember", 45
))

# Q16 - PYQ Pattern -> D
questions.append(create_q(
    "FD_PYQ_016", "Medium", "Two-Statement",
    "Consider the following statements regarding Article 51A(h) ('Scientific Temper'):\n\n1. Article 51A(h) obligates every citizen to develop scientific temper, humanism, and the spirit of inquiry and reform.\n2. India's Constitution is the first in the world to explicitly include 'scientific temper' as a constitutional duty.\n\nWhich of the statement(s) given above is/are correct?",
    "உறுப்பு 51A(h) ('அறிவியல் மனப்பான்மை') பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n\n1. உறுப்பு 51A(h) அறிவியல் மனப்பான்மை, மனிதநேயம் மற்றும் ஆராய்ச்சி, சீர்திருத்த உணர்வை வளர்க்க ஒவ்வொரு குடிமகனுக்கும் கடமையாக்குகிறது.\n2. தன் அரசியலமைப்பில் 'அறிவியல் மனப்பான்மையை' ஒரு கடமையாக வெளிப்படையாகச் சேர்த்த உலகின் முதல் நாடு இந்தியா ஆகும்.\n\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானவை?",
    "", "", "", "",
    "1 only", "1 மட்டும்",
    "2 only", "2 மட்டும்",
    "Neither 1 nor 2", "எதுவும் இல்லை",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "D",
    "Both statements are correct. Article 51A(h) contains scientific temper, humanism, inquiry, and reform. India was the first country to constitutionally mandate scientific temper.",
    "இரண்டு கூற்றுகளும் சரியானவை. உறுப்பு 51A(h) அறிவியல் மனப்பான்மை, மனிதநேயம், ஆராய்ச்சி, சீர்திருத்தத்தைக் கொண்டுள்ளது. அறிவியல் மனப்பான்மையை அரசியலமைப்பில் கட்டாயமாக்கிய முதல் நாடு இந்தியா ஆகும்.",
    "Both 1 and 2 are true.", "1 மற்றும் 2 இரண்டும் சரியானவை.",
    "Statement 1 accurately lists the 4 pillars of Art 51A(h).", "கூற்று 1 உறுப்பு 51A(h)-ன் 4 தூண்களைச் சரியாகப் பட்டியலிடுகிறது.",
    "Statement 2 is historically accurate regarding global constitutions.", "உலகளாவிய அரசியலமைப்புகளில் கூற்று 2 வரலாற்று ரீதியாக சரியானது.",
    "Neither statement is false.", "எக்கூற்றும் தவறல்ல.",
    "TNPSC Trap: Scientific temper means evidence-based rational thinking, distinct from mere possession of a science degree.",
    "TNPSC பொறி: அறிவியல் மனப்பான்மை என்பது ஆதார அடிப்படையிலான பகுத்தறிவு சிந்தனையாகும், வெறும் அறிவியல் பட்டம் வைத்திருப்பதிலிருந்து வேறுபட்டது.",
    "Jawaharlal Nehru coined the term 'scientific temper' in 1946.",
    "ஜவஹர்லால் நேரு 1946-ல் 'அறிவியல் மனப்பான்மை' என்ற சொல்லை உருவாக்கினார்.",
    ["TNPSC Group 1 Pattern", "NCERT"], "PYQ Pattern", "Understand", 45
))

# Q17 - PYQ Pattern -> A
questions.append(create_q(
    "FD_PYQ_017", "Easy", "Direct MCQ",
    "Which clause of Article 51A explicitly commands citizens to 'renounce practices derogatory to the dignity of women'?",
    "உறுப்பு 51A-ன் எந்த உட்பிரிவு 'பெண்களின் கண்ணியத்தைக் குறைக்கும் வழக்கங்களைக் கைவிடக்' குடிமக்களுக்கு வெளிப்படையாகக் கட்டளையிடுகிறது?",
    "", "", "", "",
    "Article 51A(e)", "உறுப்பு 51A(e)",
    "Article 51A(b)", "உறுப்பு 51A(b)",
    "Article 51A(f)", "உறுப்பு 51A(f)",
    "Article 51A(i)", "உறுப்பு 51A(i)",
    "A",
    "Article 51A(e) contains two directives: 1. Promote harmony and common brotherhood transcending diversities, 2. Renounce practices derogatory to the dignity of women.",
    "உறுப்பு 51A(e) இரண்டு கட்டளைகளைக் கொண்டுள்ளது: 1. நல்லிணக்கம் & சகோதரத்துவத்தை வளர்த்தல், 2. பெண்களின் கண்ணியத்தைக் குறைக்கும் வழக்கங்களைக் கைவிடுதல்.",
    "Article 51A(e) explicitly contains the women dignity clause.", "உறுப்பு 51A(e) பெண்களின் கண்ணிய விதியை வெளிப்படையாகக் கொண்டுள்ளது.",
    "Article 51A(b) concerns freedom struggle noble ideals.", "உறுப்பு 51A(b) சுதந்திரப் போராட்ட உயரிய லட்சியங்கள் பற்றியது.",
    "Article 51A(f) concerns composite culture.", "உறுப்பு 51A(f) கூட்டுப் பண்பாடு பற்றியது.",
    "Article 51A(i) concerns safeguarding public property.", "உறுப்பு 51A(i) பொதுச் சொத்தைப் பாதுகாப்பது பற்றியது.",
    "TNPSC Trap: IPC Section 509 and POSH Act 2013 enforce the constitutional intent of Article 51A(e).",
    "TNPSC பொறி: IPC பிரிவு 509 மற்றும் POSH சட்டம் 2013 ஆகியவை உறுப்பு 51A(e)-ன் அரசியலமைப்பு நோக்கத்தை அமல்படுத்துகின்றன.",
    "Dignity of women is a core constitutional value in Part III, IV, and IVA.",
    "பெண்களின் கண்ணியம் பகுதிகள் III, IV, IVA-ல் முக்கிய அரசியலமைப்பு மதிப்பாகும்.",
    ["TNPSC Group 1 Pattern", "Samacheer Kalvi"], "PYQ Pattern", "Remember", 45
))

# Q18 - PYQ Pattern -> B
questions.append(create_q(
    "FD_PYQ_018", "Medium", "Three-Statement",
    "Consider the following statements regarding the applicability of Fundamental Duties:\n\n1. Fundamental Duties apply exclusively to citizens of India and do not extend to foreigners.\n2. Fundamental Duties contain both moral duties and civic duties.\n3. Fundamental Duties can be enforced directly by courts without any parliamentary enabling law.\n\nWhich of the statements given above are correct?",
    "அடிப்படை கடமைகளின் பயன்பாடு பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n\n1. அடிப்படை கடமைகள் இந்தியக் குடிமக்களுக்கு மட்டுமே பொருந்தும், வெளிநாட்டவருக்குப் பொருந்தாது.\n2. அடிப்படை கடமைகள் தர்மக் கடமைகள் மற்றும் குடிமைக் கடமைகள் இரண்டையும் கொண்டுள்ளன.\n3. நாடாளுமன்றச் சட்டம் எதுவுமின்றி நீதிமன்றங்களால் நேரடியாக அடிப்படை கடமைகளை அமல்படுத்த முடியும்.\n\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
    "", "", "", "",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "B",
    "Statements 1 and 2 are correct. Duties apply ONLY to citizens (statement 1) and include moral/civic duties (statement 2). Statement 3 is false because non-justiciable duties CANNOT be directly enforced without statutory enabling laws.",
    "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கடமைகள் குடிமக்களுக்கு மட்டுமே பொருந்தும் (கூற்று 1) மற்றும் தர்ம/குடிமைக் கடமைகளைக் கொண்டுள்ளன (கூற்று 2). சட்டங்களின்றி நேரடியாக அமல்படுத்த முடியாது என்பதால் கூற்று 3 தவறானது.",
    "Statements 1 and 2 are factually true.", "கூற்றுகள் 1 மற்றும் 2 சரியானவை.",
    "Statement 3 is false because duties are non-justiciable.", "கடமைகள் அமல்படுத்த முடியாதவை என்பதால் கூற்று 3 தவறானது.",
    "Statement 3 is incorrect.", "கூற்று 3 தவறானது.",
    "Statement 3 is false.", "கூற்று 3 தவறானது.",
    "TNPSC Trap: Certain Fundamental Rights apply to all persons (citizens + foreigners), but ALL Fundamental Duties apply ONLY to citizens.",
    "TNPSC பொறி: சில அடிப்படை உரிமைகள் அனைவருக்கும் பொருந்தும், ஆனால் அனைத்து அடிப்படை கடமைகளும் குடிமக்களுக்கு மட்டுமே பொருந்தும்.",
    "Article 51A opens with 'It shall be the duty of every citizen of India'.",
    "உறுப்பு 51A 'இது இந்தியாவின் ஒவ்வொரு குடிமகனின் கடமையாகும்' என்றே தொடங்குகிறது.",
    ["TNPSC Group 1 Pattern", "M. Laxmikanth"], "PYQ Pattern", "Analyze", 60
))

# Q19 - Actual PYQ -> C
questions.append(create_q(
    "FD_PYQ_019", "Easy", "Direct MCQ",
    "'To value and preserve the rich heritage of our composite culture' is a Fundamental Duty enshrined in which clause of Article 51A?",
    "'நமது கூட்டுப் பண்பாட்டின் வளமான பாரம்பரியத்தைப் போற்றிப் பேணுதல்' என்பது உறுப்பு 51A-ன் எந்த உட்பிரிவில் உள்ள அடிப்படை கடமையாகும்?",
    "", "", "", "",
    "Article 51A(c)", "உறுப்பு 51A(c)",
    "Article 51A(e)", "உறுப்பு 51A(e)",
    "Article 51A(f)", "உறுப்பு 51A(f)",
    "Article 51A(h)", "உறுப்பு 51A(h)",
    "C",
    "Article 51A(f) mandates every citizen 'to value and preserve the rich heritage of our composite culture'.",
    "உறுப்பு 51A(f) 'நமது கூட்டுப் பண்பாட்டின் வளமான பாரம்பரியத்தைப் போற்றிப் பேண' ஒவ்வொரு குடிமகனுக்கும் கடமையாக்குகிறது.",
    "Article 51A(f) explicitly contains the composite culture clause.", "உறுப்பு 51A(f) கூட்டுப் பண்பாட்டு விதியை வெளிப்படையாகக் கொண்டுள்ளது.",
    "Article 51A(c) concerns sovereignty, unity, and integrity.", "உறுப்பு 51A(c) இறையாண்மை, ஒற்றுமை, ஒருமைப்பாடு பற்றியது.",
    "Article 51A(e) concerns brotherhood and women dignity.", "உறுப்பு 51A(e) சகோதரத்துவம் மற்றும் பெண்களின் கண்ணியம் பற்றியது.",
    "Article 51A(h) concerns scientific temper.", "உறுப்பு 51A(h) அறிவியல் மனப்பான்மை பற்றியது.",
    "TNPSC Trap: 'Composite culture' refers to the syncretic pluralistic heritage of India.",
    "TNPSC பொறி: 'கூட்டுப் பண்பாடு' என்பது இந்தியாவின் பன்முகக் கூட்டுப் பாரம்பரியத்தைக் குறிக்கிறது.",
    "The phrase 'composite culture' also appears in Article 351.",
    "'கூட்டுப் பண்பாடு' என்ற சொல் உறுப்பு 351-லும் காணப்படுகிறது.",
    ["TNPSC Group 4 2018 PYQ", "Samacheer Kalvi"], "Actual PYQ", "Remember", 45
))

# Q20 - PYQ Pattern -> D
questions.append(create_q(
    "FD_PYQ_020", "Hard", "Assertion & Reason",
    "Assertion (A): In State of Gujarat v. Mirzapur Moti Koreshi (2005), the Supreme Court upheld a total ban on cow slaughter.\nReason (R): Restrictions imposed on Fundamental Rights under Article 19 to give effect to DPSP (Art 48) and Fundamental Duty (Art 51A(g)) are constitutionally reasonable restrictions.",
    "கூற்று (A): குஜராத் மாநிலம் எதிராக மிர்சாபூர் மோதி கொரேஷி (2005) வழக்கில் பசு வதைத் தடையை உச்சநீதிமன்றம் உறுதி செய்தது.\nகாரணம் (R): DPSP (உறுப்பு 48) மற்றும் அடிப்படை கடமைக்கு (உறுப்பு 51A(g)) பலனளிக்க உறுப்பு 19-ன் கீழ் அடிப்படை உரிமைகள் மீது விதிக்கப்படும் கட்டுப்பாடுகள் நியாயமான கட்டுப்பாடுகளாகும்.",
    "In State of Gujarat v. Mirzapur Moti Koreshi (2005), the Supreme Court upheld a total ban on cow slaughter.",
    "குஜராத் மாநிலம் எதிராக மிர்சாபூர் மோதி கொரேஷி (2005) வழக்கில் பசு வதைத் தடையை உச்சநீதிமன்றம் உறுதி செய்தது.",
    "Restrictions imposed on Fundamental Rights under Article 19 to give effect to DPSP (Art 48) and Fundamental Duty (Art 51A(g)) are constitutionally reasonable restrictions.",
    "DPSP (உறுப்பு 48) மற்றும் அடிப்படை கடமைக்கு (உறுப்பு 51A(g)) பலனளிக்க உறுப்பு 19-ன் கீழ் அடிப்படை உரிமைகள் மீது விதிக்கப்படும் கட்டுப்பாடுகள் நியாயமான கட்டுப்பாடுகளாகும்.",
    "Both A and R are correct but R is NOT the correct explanation of A", "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல.",
    "A is correct but R is incorrect", "A சரி, ஆனால் R தவறு.",
    "A is incorrect but R is correct", "A தவறு, ஆனால் R சரி.",
    "Both A and R are correct and R is the correct explanation of A", "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்.",
    "D",
    "Both Assertion and Reason are true, and R explains A. In Mirzapur (2005), 7-judge Bench used Art 51A(g) to uphold restrictions on Art 19(1)(g) right to trade.",
    "கூற்று A மற்றும் காரணம் R இரண்டும் சரி, மேலும் R என்பது A-விற்கு சரியான விளக்கம். மிர்சாபூர் வழக்கில் (2005) 7 நீதிபதிகள் அமர்வு உறுப்பு 19(1)(g) தொழிலும் உரிமை மீதான கட்டுப்பாடுகளை உறுதிப்படுத்த உறுப்பு 51A(g)-ஐப் பயன்படுத்தியது.",
    "Both A and R are true, and R correctly explains the constitutional justification.", "A மற்றும் R இரண்டும் சரி, மேலும் R அரசியலமைப்பு நியாயத்தை விளக்குகிறது.",
    "Reason explains Assertion directly.", "காரணம் கூற்றை நேரடியாக விளக்குகிறது.",
    "Reason is factually correct.", "காரணம் சரியானது.",
    "Assertion is factually true.", "கூற்று சரியானது.",
    "TNPSC Trap: Mirzapur (2005) overruled Quareshi (1958) because Part IVA did not exist in 1958.",
    "TNPSC பொறி: 1958-ல் பகுதி IVA இல்லாததால், 2005-ன் மிர்சாபூர் வழக்கு 1958-ன் குரேஷி தீர்ப்பை ரத்து செய்தது.",
    "7-judge Constitution Bench was headed by CJI R.C. Lahoti.",
    "7 நீதிபதிகள் அமர்விற்கு தலைமை நீதிபதி ஆர்.சி. லஹோட்டி தலைமை தாங்கினார்.",
    ["TNPSC Group 1 Pattern", "M. Laxmikanth"], "PYQ Pattern", "Analyze", 60
))

# Q21 - PYQ Pattern -> A
questions.append(create_q(
    "FD_PYQ_021", "Medium", "Direct MCQ",
    "Which Parliamentary Act serves as the statutory enforcer of the Fundamental Duty to safeguard public property and abjure violence under Article 51A(i)?",
    "உறுப்பு 51A(i)-ன் கீழ் பொதுச் சொத்தைப் பாதுகாக்கவும் வன்முறையைக் கைவிடவும் உள்ள அடிப்படை கடமையின் சட்ட அமலாக்கச் சட்டமாக விளங்கும் நாடாளுமன்றச் சட்டம் எது?",
    "", "", "", "",
    "Prevention of Damage to Public Property Act, 1984", "பொதுச் சொத்து சேதத் தடுப்புச் சட்டம், 1984",
    "Arms Act, 1959", "ஆயுதச் சட்டம், 1959",
    "National Security Act, 1980", "தேசிய பாதுகாப்புச் சட்டம், 1980",
    "Unlawful Activities (Prevention) Act, 1967", "சட்டவிரோத நடவடிக்கைகள் தடுப்புச் சட்டம், 1967",
    "A",
    "The Prevention of Damage to Public Property Act, 1984 enforces Article 51A(i) by penalizing destruction of public property during violent protests.",
    "1984-ன் பொதுச் சொத்து சேதத் தடுப்புச் சட்டம் வன்முறைப் போராட்டங்களின் போது பொதுச் சொத்தை சேதப்படுத்துவதைத் தண்டிப்பதன் மூலம் உறுப்பு 51A(i)-ஐ அமல்படுத்துகிறது.",
    "1984 Act directly enforces Article 51A(i).", "1984 சட்டம் நேரடியாக உறுப்பு 51A(i)-ஐ அமல்படுத்துகிறது.",
    "Arms Act 1959 regulates firearms possession.", "ஆயுதச் சட்டம் 1959 துப்பாக்கிகள் வைப்பச் சீர்படுத்துகிறது.",
    "NSA 1980 provides for preventive detention.", "NSA 1980 முன்னெச்சரிக்கை தடுப்புக் காவலை அளிக்கிறது.",
    "UAPA 1967 deals with unlawful activities and terrorism.", "UAPA 1967 சட்டவிரோத நடவடிக்கைகள் மற்றும் பயங்கரவாதத்தைக் கையாள்கிறது.",
    "TNPSC Trap: SC in 2009 issued guidelines making protest organizers financially liable for public property damage under Article 51A(i).",
    "TNPSC பொறி: 2009-ல் உச்சநீதிமன்றம் 51A(i)-ன் கீழ் பொதுச் சொத்து சேதத்திற்குப் போராட்ட அமைப்பாளர்களுக்கு நிதிப் பொறுப்பு விதித்தது.",
    "Article 51A(i) combines safeguarding public property AND abjuring violence.",
    "உறுப்பு 51A(i) பொதுச் சொத்தைப் பாதுகாத்தல் மற்றும் வன்முறையைக் கைவிடுதல் இரண்டையும் இணைக்கிறது.",
    ["TNPSC Group 1 Pattern", "NCERT"], "PYQ Pattern", "Understand", 45
))

# Q22 - Actual PYQ -> B
questions.append(create_q(
    "FD_PYQ_022", "Easy", "Direct MCQ",
    "The National Commission to Review the Working of the Constitution (NCRWC, 2002) was headed by whom?",
    "2002-ன் அரசியலமைப்பு செயல்பாட்டை மறுஆய்வு செய்வதற்கான தேசிய ஆணையத்திற்கு (NCRWC) தலைமை தாங்கியவர் யார்?",
    "", "", "", "",
    "Justice J.S. Verma", "நீதியரசர் ஜே.எஸ். வர்மா",
    "Justice M.N. Venkatachaliah", "நீதியரசர் எம்.என். வெங்கடாசலய்யா",
    "Justice R.S. Sarkaria", "நீதியரசர் ஆர்.எஸ். சர்க்காரியா",
    "Justice K.T. Thomas", "நீதியரசர் கே.டி. தாமஸ்",
    "B",
    "The NCRWC (2002) was headed by former Chief Justice of India M.N. Venkatachaliah, which reviewed Part IVA and suggested adding new duties.",
    "அரசியலமைப்பு மறுஆய்வு ஆணையத்திற்கு (2002) முன்னாள் தலைமை நீதிபதி எம்.என். வெங்கடாசலய்யா தலைமை தாங்கினார்.",
    "Justice M.N. Venkatachaliah headed the NCRWC in 2002.", "நீதியரசர் எம்.என். வெங்கடாசலய்யா 2002-ல் NCRWC-க்கு தலைமை தாங்கினார்.",
    "Justice J.S. Verma headed the Fundamental Duties Committee in 1999.", "நீதியரசர் ஜே.எஸ். வர்மா 1999 கடமைகள் குழுவிற்கு தலைமை தாங்கினார்.",
    "Justice R.S. Sarkaria headed Centre-State Relations Commission in 1983.", "நீதியரசர் ஆர்.எஸ். சர்க்காரியா 1983 மத்திய-மாநில ஆணையத்திற்கு தலைமை தாங்கினார்.",
    "Justice K.T. Thomas was a committee member.", "நீதியரசர் கே.டி. தாமஸ் குழு உறுப்பினராக இருந்தார்.",
    "TNPSC Trap: NCRWC recommended adding duty to vote and pay taxes, but Parliament did NOT enact them.",
    "TNPSC பொறி: NCRWC வாக்களிக்கும் மற்றும் வரி செலுத்தும் கடமைகளைப் பரிந்துரைத்தது, ஆனால் நாடாளுமன்றம் அவற்றை இயற்றவில்லை.",
    "NCRWC submitted its report in March 2002.",
    "NCRWC தனது அறிக்கையை மார்ச் 2002-ல் சமர்ப்பித்தது.",
    ["TNPSC Group 2 2015 PYQ", "M. Laxmikanth"], "Actual PYQ", "Remember", 45
))

# Q23 - PYQ Pattern -> C
questions.append(create_q(
    "FD_PYQ_023", "Medium", "Match",
    "Match List I (Fundamental Duty Clause) with List II (Key Statutory Enforcer):\n\nList I:\na. Article 51A(a)\nb. Article 51A(c)\nc. Article 51A(g)\nd. Article 51A(i)\n\nList II:\n1. Prevention of Insults to National Honour Act 1971\n2. IPC Section 153B\n3. Wildlife Protection Act 1972\n4. Prevention of Damage to Public Property Act 1984",
    "பட்டியல் I-ஐ (அடிப்படை கடமை உட்பிரிவு) பட்டியல் II உடன் (சட்ட அமலாக்கி) பொருத்துக:\n\nபட்டியல் I:\na. உறுப்பு 51A(a)\nb. உறுப்பு 51A(c)\nc. உறுப்பு 51A(g)\nd. உறுப்பு 51A(i)\n\nபட்டியல் II:\n1. தேசிய சின்னங்கள் அவமதிப்பு தடுப்புச் சட்டம் 1971\n2. IPC பிரிவு 153B\n3. வனவிலங்கு பாதுகாப்புச் சட்டம் 1972\n4. பொதுச் சொத்து சேதத் தடுப்புச் சட்டம் 1984",
    "", "", "", "",
    "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
    "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2",
    "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
    "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1",
    "C",
    "Correct match: Art 51A(a) -> Insults to National Honour Act (1); Art 51A(c) -> IPC Sec 153B (2); Art 51A(g) -> Wildlife Protection Act (3); Art 51A(i) -> Damage to Public Property Act (4). Sequence: 1-2-3-4.",
    "சரியான பொருத்தம்: 51A(a) -> 1971 சட்டம் (1); 51A(c) -> IPC 153B (2); 51A(g) -> 1972 சட்டம் (3); 51A(i) -> 1984 சட்டம் (4). வரிசை: 1-2-3-4.",
    "a-1, b-2, c-3, d-4 is the exact verified match sequence.", "a-1, b-2, c-3, d-4 என்பது சரிபார்க்கப்பட்ட சரியான பொருத்த வரிசையாகும்.",
    "a-2 mismatch.", "a-2 தவறான பொருத்தம்.",
    "a-3 mismatch.", "a-3 தவறான பொருத்தம்.",
    "a-4 mismatch.", "a-4 தவறான பொருத்தம்.",
    "TNPSC Trap: Justice Verma Committee (1999) mapped these exact statutory enforcers to Fundamental Duties.",
    "TNPSC பொறி: நீதியரசர் வர்மா குழு (1999) இந்தச் சட்ட அமலாக்கிகளை அடிப்படை கடமைகளுடன் சரியாக வரைபடமாக்கியது.",
    "IPC 153B penalizes assertions prejudicial to national integration.",
    "IPC 153B தேசிய ஒருமைப்பாட்டிற்கு எதிரான கருத்துகளைத் தண்டிக்கிறது.",
    ["TNPSC Group 1 Pattern", "Samacheer Kalvi"], "PYQ Pattern", "Analyze", 60
))

# Q24 - PYQ Pattern -> D
questions.append(create_q(
    "FD_PYQ_024", "Medium", "Two-Statement",
    "Consider the following statements regarding national defense service:\n\n1. Article 51A(d) obligates citizens to defend the country and render national service when called upon to do so.\n2. Article 23(2) permits the State to impose compulsory service for public purposes without violating the prohibition against forced labor.\n\nWhich of the statement(s) given above is/are correct?",
    "தேசப் பாதுகாப்பு சேவை பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n\n1. உறுப்பு 51A(d) தேசத்தைப் பாதுகாக்கவும் தேவைப்படும் போது தேசிய சேவையாற்றவும் குடிமக்களுக்குக் கடமையாக்குகிறது.\n2. உறுப்பு 23(2) பொது நோக்கங்களுக்காகக் கட்டாய சேவையை விதிக்க அரசை அனுமதிப்பதால் அது கட்டாய வேலைத் தடையை மீறாது.\n\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானவை?",
    "", "", "", "",
    "1 only", "1 மட்டும்",
    "2 only", "2 மட்டும்",
    "Neither 1 nor 2", "எதுவும் இல்லை",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "D",
    "Both statements are correct. Article 51A(d) commands national defense service, while Article 23(2) provides the constitutional exception permitting compulsory public service.",
    "இரண்டு கூற்றுகளும் சரியானவை. உறுப்பு 51A(d) தேசப் பாதுகாப்பு சேவையைக் கட்டாயமாக்குகிறது, அதே வேளையில் உறுப்பு 23(2) கட்டாயப் பொது சேவைக்கான அரசியலமைப்பு விலக்கை அளிக்கிறது.",
    "Both 1 and 2 are true.", "1 மற்றும் 2 இரண்டும் சரியானவை.",
    "Statement 1 is factually true under Art 51A(d).", "கூற்று 1 உறுப்பு 51A(d)-ன் படி சரியானது.",
    "Statement 2 is factually true under Art 23(2).", "கூற்று 2 உறுப்பு 23(2)-ன் படி சரியானது.",
    "Neither is false.", "எதுவும் தவறல்ல.",
    "TNPSC Trap: Article 23(2) prohibits discrimination based ON RELIGION, RACE, CASTE OR CLASS when imposing compulsory service.",
    "TNPSC பொறி: கட்டாய சேவை விதிக்கும் போது மதம், இனம், சாதி அல்லது வகுப்பு அடிப்படையில் பாகுபாடு காட்டுவதை உறுப்பு 23(2) தடை செய்கிறது.",
    "Article 51A(d) applies whenever Parliament enacts a national service law.",
    "நாடாளுமன்றம் தேசிய சேவைச் சட்டத்தை இயற்றும் போதெல்லாம் உறுப்பு 51A(d) பொருந்தும்.",
    ["TNPSC Group 1 Pattern", "M. Laxmikanth"], "PYQ Pattern", "Understand", 45
))

# Q25 - Actual PYQ -> A
questions.append(create_q(
    "FD_PYQ_025", "Easy", "Direct MCQ",
    "Which Article of the Indian Constitution prescribes the Fundamental Duty of every citizen to strive towards excellence in all spheres of individual and collective activity?",
    "தனிநபர் மற்றும் கூட்டுச் செயல்பாடுகளின் அனைத்துத் துறைகளிலும் சிறப்பினை நோக்கி முயலும் அடிப்படை கடமையை இந்திய அரசியலமைப்பின் எந்த உறுப்பு விதிக்கிறது?",
    "", "", "", "",
    "Article 51A(j)", "உறுப்பு 51A(j)",
    "Article 51A(g)", "உறுப்பு 51A(g)",
    "Article 51A(h)", "உறுப்பு 51A(h)",
    "Article 51A(i)", "உறுப்பு 51A(i)",
    "A",
    "Article 51A(j) mandates every citizen 'to strive towards excellence in all spheres of individual and collective activity so that the nation constantly rises to higher levels of endeavour and achievement'.",
    "உறுப்பு 51A(j) 'நாடு தொடர்ந்து உயர்ந்த முயற்சிகள் மற்றும் சாதனைகளின் நிலைகளுக்கு உயர்வதற்காகத் தனிநபர் மற்றும் கூட்டுச் செயல்பாடுகளின் அனைத்துத் துறைகளிலும் சிறப்பினை நோக்கி முயல' ஒவ்வொரு குடிமகனுக்கும் கடமையாக்குகிறது.",
    "Article 51A(j) explicitly contains the excellence clause.", "உறுப்பு 51A(j) சிறப்பினை நோக்கிய விதியை வெளிப்படையாகக் கொண்டுள்ளது.",
    "Article 51A(g) concerns natural environment.", "உறுப்பு 51A(g) இயற்கைச் சூழல் பற்றியது.",
    "Article 51A(h) concerns scientific temper.", "உறுப்பு 51A(h) அறிவியல் மனப்பான்மை பற்றியது.",
    "Article 51A(i) concerns safeguarding public property.", "உறுப்பு 51A(i) பொதுச் சொத்தைப் பாதுகாப்பது பற்றியது.",
    "TNPSC Trap: Article 51A(j) covers BOTH individual activity AND collective activity.",
    "TNPSC பொறி: உறுப்பு 51A(j) தனிநபர் செயல்பாடு மற்றும் கூட்டுச் செயல்பாடு இரண்டையும் உள்ளடக்கியது.",
    "AIIMS Students Union case (2002) applied Article 51A(j) to academic excellence.",
    "AIIMS மாணவர் சங்க வழக்கு (2002) உறுப்பு 51A(j)-ஐக் கல்விச் சிறப்பிற்குப் பயன்படுத்தியது.",
    ["TNPSC Group 1 2015 PYQ", "Samacheer Kalvi"], "Actual PYQ", "Remember", 45
))

# Q26 - PYQ Pattern -> B
questions.append(create_q(
    "FD_PYQ_026", "Easy", "Direct MCQ",
    "Which of the following is NOT among the 11 Fundamental Duties listed under Article 51A?",
    "உறுப்பு 51A-ன் கீழ் பட்டியலிடப்பட்டுள்ள 11 அடிப்படை கடமைகளில் இல்லாதது எது?",
    "", "", "", "",
    "To cherish and follow noble ideals of freedom struggle", "சுதந்திரப் போராட்ட உயரிய லட்சியங்களைப் பேணிப் பின்பற்றல்",
    "To promote international peace and security", "சர்வதேச அமைதி மற்றும் பாதுகாப்பை ஊக்குவித்தல்",
    "To uphold and protect sovereignty, unity and integrity of India", "இந்தியாவின் இறையாண்மை, ஒற்றுமை, ஒருமைப்பாட்டைப் பேணிப் பாதுகாத்தல்",
    "To develop scientific temper, humanism and spirit of inquiry", "அறிவியல் மனப்பான்மை, மனிதநேயம், ஆராய்ச்சி உணர்வை வளர்த்தல்",
    "B",
    "Promoting international peace and security is a Directive Principle under Article 51 in Part IV, NOT a Fundamental Duty in Article 51A.",
    "சர்வதேச அமைதி மற்றும் பாதுகாப்பை ஊக்குவிப்பது பகுதி IV உறுப்பு 51-ன் கீழ் அரசு நெறிமுறைக் கோட்பாடாகும், உறுப்பு 51A-ல் அடிப்படை கடமையல்ல.",
    "Promoting international peace is Article 51 (DPSP), not Article 51A duty.", "சர்வதேச அமைதியை ஊக்குவிப்பது உறுப்பு 51 (DPSP), உறுப்பு 51A கடமையல்ல.",
    "Freedom ideals is Art 51A(b).", "சுதந்திர லட்சியங்கள் உறுப்பு 51A(b).",
    "Sovereignty & unity is Art 51A(c).", "இறையாண்மை & ஒற்றுமை உறுப்பு 51A(c).",
    "Scientific temper is Art 51A(h).", "அறிவியல் மனப்பான்மை உறுப்பு 51A(h).",
    "TNPSC Trap: Do not confuse Article 51 (State duty for International Peace) with Article 51A (Citizen Fundamental Duties).",
    "TNPSC பொறி: உறுப்பு 51 (சர்வதேச அமைதிக்கான அரசு கடமை) மற்றும் உறுப்பு 51A (குடிமகன் அடிப்படை கடமைகள்) ஆகிய குழப்பக் கூடாது.",
    "Article 51 is the final article of Part IV DPSP.", "உறுப்பு 51 பகுதி IV DPSP-ன் இறுதி உறுப்பாகும்.",
    ["TNPSC Group 1 Pattern", "NCERT"], "PYQ Pattern", "Remember", 45
))

# Q27 - PYQ Pattern -> C
questions.append(create_q(
    "FD_PYQ_027", "Medium", "Three-Statement",
    "Consider the following statements regarding committee proposals on Fundamental Duties:\n\n1. Swaran Singh Committee recommended penal provisions for non-compliance, which Parliament rejected.\n2. Swaran Singh Committee proposed 8 duties, but 42nd CAA incorporated 10 duties.\n3. 86th Constitutional Amendment Act, 2002 added the duty to pay income tax.\n\nWhich of the statements given above are correct?",
    "அடிப்படை கடமைகள் பற்றிய குழுப் பரிந்துரைகள் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n\n1. கடமைகளைப் பின்பற்றாதவருக்குத் தண்டனை விதிக்க ஸ்வரன் சிங் குழு பரிந்துரைத்தது, அதை நாடாளுமன்றம் நிராகரித்தது.\n2. ஸ்வரன் சிங் குழு 8 கடமைகளைப் பரிந்துரைத்தது, ஆனால் 42வது திருத்தம் 10 கடமைகளை இணைத்தது.\n3. 2002-ன் 86வது திருத்தச் சட்டம் வருமான வரி செலுத்தும் கடமையைச் சேர்த்தது.\n\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
    "", "", "", "",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "C",
    "Statements 1 and 2 are correct. Swaran Singh's penal proposal was rejected (statement 1). Swaran Singh proposed 8 duties, but 10 were enacted (statement 2). Statement 3 is false because 86th CAA added Art 51A(k) [education], NOT tax paying duty.",
    "கூற்றுகள் 1 மற்றும் 2 சரியானவை. ஸ்வரன் சிங்கின் தண்டனைப் பரிந்துரை நிராகரிக்கப்பட்டது (கூற்று 1). 8 கடமைகளைப் பரிந்துரைத்தார், 10 இயற்றப்பட்டன (கூற்று 2). 86வது திருத்தம் கல்வியைச் சேர்த்ததே தவிர வரியைச் சேர்க்காததால் கூற்று 3 தவறானது.",
    "Statements 1 and 2 are factually true.", "கூற்றுகள் 1 மற்றும் 2 சரியானவை.",
    "Statement 3 is false because 86th CAA added Art 51A(k) education duty.", "86வது திருத்தம் 51A(k) கல்விக் கடமையைச் சேர்த்ததால் கூற்று 3 தவறானது.",
    "Statement 3 is incorrect.", "கூற்று 3 தவறானது.",
    "Statement 3 is false.", "கூற்று 3 தவறானது.",
    "TNPSC Trap: Income tax duty was recommended by Swaran Singh (1976) and NCRWC (2002), but NEVER enacted into Article 51A.",
    "TNPSC பொறி: வருமான வரி செலுத்தும் கடமை ஸ்வரன் சிங் மற்றும் NCRWC-யால் பரிந்துரைக்கப்பட்டது, ஆனால் உறுப்பு 51A-ல் இதுவரை சேர்க்கப்படவில்லை.",
    "86th CAA added Article 51A(k) on education.", "86வது திருத்தம் கல்வி பற்றிய உறுப்பு 51A(k)-ஐச் சேர்த்தது.",
    ["TNPSC Group 1 Pattern", "M. Laxmikanth"], "PYQ Pattern", "Analyze", 60
))

# Q28 - Actual PYQ -> D
questions.append(create_q(
    "FD_PYQ_028", "Easy", "Direct MCQ",
    "In which year were Fundamental Duties incorporated into the Constitution of India?",
    "இந்திய அரசியலமைப்பில் எந்த ஆண்டில் அடிப்படை கடமைகள் சேர்க்கப்பட்டன?",
    "", "", "", "",
    "1950", "1950",
    "1978", "1978",
    "2002", "2002",
    "1976", "1976",
    "D",
    "Fundamental Duties were added by the 42nd Constitutional Amendment Act enacted in 1976 during the Internal Emergency.",
    "உள்நாட்டு அவசரநிலையின் போது 1976-ல் இயற்றப்பட்ட 42வது அரசியலமைப்பு திருத்தச் சட்டம் மூலம் அடிப்படை கடமைகள் சேர்க்கப்பட்டன.",
    "1976 is the exact enactment year of 42nd CAA adding Part IVA.", "1976 என்பது பகுதி IVA-வைச் சேர்த்த 42வது திருத்தம் இயற்றப்பட்ட ஆண்டாகும்.",
    "1950 is commencement year of original Constitution (no FD).", "1950 அசல் அரசியலமைப்பு அமல்படுத்தப்பட்ட ஆண்டு (கடமைகள் இல்லை).",
    "1978 is year of 44th CAA.", "1978 என்பது 44வது திருத்த ஆண்டு.",
    "2002 is year of 86th CAA adding 11th duty.", "2002 என்பது 11வது கடமையைச் சேர்த்த 86வது திருத்த ஆண்டு.",
    "TNPSC Trap: 42nd CAA was enacted in 1976 and came into force on 3rd January 1977.",
    "TNPSC பொறி: 42வது திருத்தம் 1976-ல் இயற்றப்பட்டு ஜனவரி 3, 1977-ல் அமலுக்கு வந்தது.",
    "3rd January is observed as National Fundamental Duties Day.", "ஜனவரி 3 தேசிய அடிப்படை கடமைகள் தினமாகக் கடைப்பிடிக்கப்படுகிறது.",
    ["TNPSC Group 2 2013 PYQ", "Samacheer Kalvi"], "Actual PYQ", "Remember", 45
))

# Q29 - PYQ Pattern -> A
questions.append(create_q(
    "FD_PYQ_029", "Hard", "Case Application",
    "In AIIMS Students Union v. AIIMS (2002), the Supreme Court relied on which Fundamental Duty clause to hold that academic merit and institutional excellence in super-speciality admissions cannot be completely sacrificed?",
    "AIIMS மாணவர் சங்கம் எதிராக AIIMS (2002) வழக்கில், மேல்-சிறப்பு சேர்க்கைகளில் கல்வித் தகுதி மற்றும் நிறுவனச் சிறப்பை முழுமையாகத் தியாகம் செய்ய முடியாது எனக் கூற உச்சநீதிமன்றம் எந்த அடிப்படை கடமை உட்பிரிவை நம்பியது?",
    "", "", "", "",
    "Article 51A(j)", "உறுப்பு 51A(j)",
    "Article 51A(a)", "உறுப்பு 51A(a)",
    "Article 51A(e)", "உறுப்பு 51A(e)",
    "Article 51A(k)", "உறுப்பு 51A(k)",
    "A",
    "In AIIMS Students Union (2002), SC held that Article 51A(j) ('strive towards excellence') requires preserving merit standards in medical super-specialities.",
    "AIIMS மாணவர் சங்க வழக்கில் (2002), உறுப்பு 51A(j) ('சிறப்பினை நோக்கி முயலுதல்') மருத்துவ மேல்-சிறப்புப் படிப்புகளில் தகுதி நிலைகளைப் பேணுவதைக் கோருகிறது என்று உச்சநீதிமன்றம் கூறியது.",
    "Article 51A(j) excellence clause was the foundation of AIIMS judgment.", "உறுப்பு 51A(j) சிறப்பினை நோக்கிய விதியே AIIMS தீர்ப்பின் அடித்தளமாகும்.",
    "Article 51A(a) concerns National Flag/Anthem.", "உறுப்பு 51A(a) தேசியக் கொடி/கீதம் பற்றியது.",
    "Article 51A(e) concerns brotherhood and women dignity.", "உறுப்பு 51A(e) சகோதரத்துவம் மற்றும் பெண்களின் கண்ணியம் பற்றியது.",
    "Article 51A(k) concerns child education duty.", "உறுப்பு 51A(k) குழந்தைகள் கல்விக் கடமை பற்றியது.",
    "TNPSC Trap: SC declared that Fundamental Duties are equal in weight to Fundamental Rights when interpreting constitutional validity.",
    "TNPSC பொறி: அரசியலமைப்புச் செல்லுபடியை விளக்கும் போது அடிப்படை கடமைகள் அடிப்படை உரிமைகளுக்கு இணையான எடை கொண்டவை என உச்சநீதிமன்றம் அறிவித்தது.",
    "Judgment observed that duties are foundation of constitutionalism.", "கடமைகளே அரசியலமைப்பின் அடித்தளம் என அத்தீர்ப்பு சுட்டிக்காட்டியது.",
    ["TNPSC Group 1 Pattern", "M. Laxmikanth"], "PYQ Pattern", "Analyze", 60
))

# Q30 - PYQ Pattern -> B
questions.append(create_q(
    "FD_PYQ_030", "Medium", "Assertion & Reason",
    "Assertion (A): The 44th Constitutional Amendment Act, 1978 retained Part IVA (Fundamental Duties) completely intact despite repealing many 42nd Amendment provisions.\nReason (R): The Janata Party government recognized that civic duties promoting national unity and constitutional discipline are non-partisan national values.",
    "கூற்று (A): 44வது அரசியலமைப்பு திருத்தச் சட்டம் (1978) 42வது திருத்தத்தின் பல விதிகளையும் ரத்து செய்தபோதிலும் பகுதி IVA-வை (அடிப்படை கடமைகள்) முழுமையாகத் தக்கவைத்துக் கொண்டது.\nகாரணம் (R): தேசிய ஒருமைப்பாடு மற்றும் அரசியலமைப்பு ஒழுங்கை ஊக்குவிக்கும் குடிமைப் பொறுப்புகள் கட்சி அரசியல் கடந்த தேசிய மதிப்புகள் என்பதை ஜனதா கட்சி அரசு அங்கீகரித்தது.",
    "The 44th Constitutional Amendment Act, 1978 retained Part IVA (Fundamental Duties) completely intact despite repealing many 42nd Amendment provisions.",
    "44வது அரசியலமைப்பு திருத்தச் சட்டம் (1978) 42வது திருத்தத்தின் பல விதிகளையும் ரத்து செய்தபோதிலும் பகுதி IVA-வை முழுமையாகத் தக்கவைத்துக் கொண்டது.",
    "The Janata Party government recognized that civic duties promoting national unity and constitutional discipline are non-partisan national values.",
    "தேசிய ஒருமைப்பாடு மற்றும் அரசியலமைப்பு ஒழுங்கை ஊக்குவிக்கும் குடிமைப் பொறுப்புகள் கட்சி அரசியல் கடந்த தேசிய மதிப்புகள் என்பதை ஜனதா கட்சி அரசு அங்கீகரித்தது.",
    "Both A and R are correct and R is the correct explanation of A", "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்.",
    "Both A and R are correct but R is NOT the correct explanation of A", "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல.",
    "A is correct but R is incorrect", "A சரி, ஆனால் R தவறு.",
    "A is incorrect but R is correct", "A தவறு, ஆனால் R சரி.",
    "B",
    "Both A and R are true, and R explains A. 44th CAA 1978 reversed Emergency changes but retained Part IVA because civic duties were acknowledged as bipartisan national values.",
    "கூற்று A மற்றும் காரணம் R இரண்டும் சரி, மேலும் R என்பது A-விற்கு சரியான விளக்கம். 44வது திருத்தம் அவசரநிலை மாற்றங்களை ரத்து செய்தபோதிலும், குடிமைப் பொறுப்புகள் கட்சி கடந்த மதிப்புகளாக ஏற்றுக்கொள்ளப்பட்டதால் பகுதி IVA தக்கவைக்கப்பட்டது.",
    "Both A and R are true, and R correctly explains the non-partisan retention.", "A மற்றும் R இரண்டும் சரி, மேலும் R கட்சி கடந்த தக்கவைப்பைச் சரியாக விளக்குகிறது.",
    "Reason explains Assertion directly.", "காரணம் கூற்றை நேரடியாக விளக்குகிறது.",
    "Reason is factually accurate.", "காரணம் சரியானது.",
    "Assertion is factually true.", "கூற்று சரியானது.",
    "TNPSC Trap: 44th CAA modified DPSP Article 38(2), but left Part IVA untouched.",
    "TNPSC பொறி: 44வது திருத்தம் DPSP உறுப்பு 38(2)-ஐத் திருத்தியது, ஆனால் பகுதி IVA-வைத் தொடவில்லை.",
    "Retaining Part IVA gave Fundamental Duties permanent bipartisan legitimacy.",
    "பகுதி IVA-வை தக்கவைத்தது அடிப்படை கடமைகளுக்கு நிரந்தரக் கட்சி கடந்த செல்லுபடியை அளித்தது.",
    ["TNPSC Group 1 Pattern", "M. Laxmikanth"], "PYQ Pattern", "Analyze", 60
))

# Q31 - Actual PYQ -> C
questions.append(create_q(
    "FD_PYQ_031", "Easy", "Direct MCQ",
    "The duty to provide educational opportunities to one's child aged 6 to 14 years under Article 51A(k) is placed primarily upon whom?",
    "உறுப்பு 51A(k)-ன் கீழ் 6 முதல் 14 வயதுடைய தனது குழந்தைக்குக் கல்விக்கான வாய்ப்புகளை வழங்கும் கடமை முதன்மையாக யாருக்கு விதிக்கப்பட்டுள்ளது?",
    "", "", "", "",
    "The State Government", "மாநில அரசு",
    "The Central Government", "மத்திய அரசு",
    "Every parent or guardian", "ஒவ்வொரு பெற்றோர் அல்லது பாதுகாவலர்",
    "School Headmasters", "பள்ளித் தலைமை ஆசிரியர்கள்",
    "C",
    "Article 51A(k) explicitly states that it shall be the duty of 'who is a parent or guardian to provide opportunities for education to his child or ward between the age of six and fourteen years'.",
    "உறுப்பு 51A(k) 'பெற்றோராக அல்லது பாதுகாவலராக இருப்பவர் ஆறு முதல் பதினான்கு வயது வரையிலான தனது குழந்தைக்குக் கல்விக்கான வாய்ப்புகளை வழங்குவது' கடமையாகும் எனத் தெளிவாகக் குறிப்பிடுகிறது.",
    "Every parent or guardian is the explicit duty-bearer under Article 51A(k).", "ஒவ்வொரு பெற்றோர் அல்லது பாதுகாவலரே உறுப்பு 51A(k)-ன் கீழ் வெளிப்படையான கடமைப் பொறுப்பாளர் ஆவார்.",
    "State Government obligation is under Article 21A (FR) and Article 45 (DPSP).", "மாநில அரசின் பொறுப்பு உறுப்பு 21A (FR) மற்றும் உறுப்பு 45 (DPSP)-ன் கீழ் உள்ளது.",
    "Central Government provides legislation like RTE Act 2009.", "மத்திய அரசு RTE சட்டம் 2009 போன்ற சட்டங்களை வழங்குகிறது.",
    "Headmasters execute school administration.", "தலைமை ஆசிரியர்கள் பள்ளி நிர்வாகத்தைச் செயல்படுத்துகிறார்கள்.",
    "TNPSC Trap: Distinguish Duty Bearers: Art 21A = State Duty (FR); Art 51A(k) = Parent/Guardian Duty (FD).",
    "TNPSC பொறி: கடமைப் பொறுப்பாளர்களை வேறுபடுத்துங்கள்: உறுப்பு 21A = அரசு கடமை (FR); உறுப்பு 51A(k) = பெற்றோர்/பாதுகாவலர் கடமை (FD).",
    "Added by 86th Amendment Act in 2002.", "2002-ன் 86வது திருத்தச் சட்டத்தால் சேர்க்கப்பட்டது.",
    ["TNPSC Group 1 2020 PYQ", "NCERT"], "Actual PYQ", "Remember", 45
))

# Q32 - PYQ Pattern -> D
questions.append(create_q(
    "FD_PYQ_032", "Medium", "Match",
    "Match List I (Constitutional Feature) with List II (Constitutional Part):\n\nList I:\na. Fundamental Rights\nb. Directive Principles of State Policy\nc. Fundamental Duties\nd. Union Executive\n\nList II:\n1. Part III\n2. Part IV\n3. Part IVA\n4. Part V",
    "பட்டியல் I-ஐ (அரசியலமைப்பு அம்சம்) பட்டியல் II உடன் (அரசியலமைப்பு பகுதி) பொருத்துக:\n\nபட்டியல் I:\na. அடிப்படை உரிமைகள்\nb. அரசு நெறிமுறைப்படுத்தும் கோட்பாடுகள்\nc. அடிப்படை கடமைகள்\nd. மத்திய நிர்வாகம்\n\nபட்டியல் II:\n1. பகுதி III\n2. பகுதி IV\n3. பகுதி IVA\n4. பகுதி V",
    "", "", "", "",
    "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
    "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2",
    "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1",
    "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
    "D",
    "Correct match: Fundamental Rights -> Part III (1); DPSP -> Part IV (2); Fundamental Duties -> Part IVA (3); Union Executive -> Part V (4). Sequence: 1-2-3-4.",
    "சரியான பொருத்தம்: அடிப்படை உரிமைகள் -> பகுதி III (1); DPSP -> பகுதி IV (2); அடிப்படை கடமைகள் -> பகுதி IVA (3); மத்திய நிர்வாகம் -> பகுதி V (4). வரிசை: 1-2-3-4.",
    "a-1, b-2, c-3, d-4 is the exact verified match sequence.", "a-1, b-2, c-3, d-4 என்பது சரிபார்க்கப்பட்ட சரியான பொருத்த வரிசையாகும்.",
    "a-2 mismatch.", "a-2 தவறான பொருத்தம்.",
    "a-3 mismatch.", "a-3 தவறான பொருத்தம்.",
    "a-4 mismatch.", "a-4 தவறான பொருத்தம்.",
    "TNPSC Trap: Part IV = DPSP (Articles 36-51); Part IVA = Fundamental Duties (Article 51A).",
    "TNPSC பொறி: பகுதி IV = DPSP (பிரிவுகள் 36-51); பகுதி IVA = அடிப்படை கடமைகள் (பிரிவு 51A).",
    "Part IVA consists of a single article (Article 51A).", "பகுதி IVA ஒரே ஒரு உறுப்பைக் (உறுப்பு 51A) கொண்டுள்ளது.",
    ["TNPSC Group 1 Pattern", "Samacheer Kalvi"], "PYQ Pattern", "Analyze", 60
))

# Q33 - PYQ Pattern -> A
questions.append(create_q(
    "FD_PYQ_033", "Medium", "Two-Statement",
    "Consider the following statements regarding Article 51A(b) ('Freedom Struggle Ideals'):\n\n1. Article 51A(b) requires citizens to cherish and follow the noble ideals that inspired our national struggle for freedom.\n2. Article 51A(b) is classified as a 'moral duty', whereas Article 51A(a) is classified as a 'civic duty'.\n\nWhich of the statement(s) given above is/are correct?",
    "உறுப்பு 51A(b) ('சுதந்திரப் போராட்ட லட்சியங்கள்') பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n\n1. உறுப்பு 51A(b) நமது தேசிய சுதந்திரப் போராட்டத்திற்கு ஊக்கமளித்த உயரிய லட்சியங்களைப் பேணிப் பின்பற்றக் குடிமக்களைக் கேட்கிறது.\n2. உறுப்பு 51A(b) 'தர்மக் கடமை' எனவும், உறுப்பு 51A(a) 'குடிமைக் கடமை' எனவும் வகைப்படுத்தப்படுகின்றன.\n\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானவை?",
    "", "", "", "",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "1 only", "1 மட்டும்",
    "2 only", "2 மட்டும்",
    "Neither 1 nor 2", "எதுவும் இல்லை",
    "A",
    "Both statements are correct. Article 51A(b) commands cherishing freedom ideals. Cherishing ideals is a moral duty, while respecting Flag/Anthem (51A(a)) is a civic duty.",
    "இரண்டு கூற்றுகளும் சரியானவை. உறுப்பு 51A(b) சுதந்திர லட்சியங்களைப் பேணக் கட்டளையிடுகிறது. லட்சியங்களைப் பேணுவது தர்மக் கடமையாகும், கொடி/கீதத்தை மதிப்பது (51A(a)) குடிமைக் கடமையாகும்.",
    "Both 1 and 2 are true.", "1 மற்றும் 2 இரண்டும் சரியானவை.",
    "Statement 1 correctly describes Article 51A(b).", "கூற்று 1 உறுப்பு 51A(b)-ஐச் சரியாக விவரிக்கிறது.",
    "Statement 2 accurately distinguishes moral vs civic duty classification.", "கூற்று 2 தர்ம vs குடிமைக் கடமை வகைப்பாட்டைச் சரியாக வேறுபடுத்துகிறது.",
    "Neither is false.", "எதுவும் தவறல்ல.",
    "TNPSC Trap: Moral duties guide inner conscience, while civic duties govern public conduct.",
    "TNPSC பொறி: தர்மக் கடமைகள் மனசாட்சியை வழிகாட்டுகின்றன, குடிமைக் கடமைகள் பொது நடத்தையை நிர்வகிக்கின்றன.",
    "Fundamental Duties contain a harmonious blend of moral and civic duties.",
    "அடிப்படை கடமைகள் தர்ம மற்றும் குடிமைக் கடமைகளின் இணக்கமான கலவையைக் கொண்டுள்ளன.",
    ["TNPSC Group 1 Pattern", "M. Laxmikanth"], "PYQ Pattern", "Understand", 45
))

# Q34 - Actual PYQ -> B
questions.append(create_q(
    "FD_PYQ_034", "Easy", "Direct MCQ",
    "Which of the following major democratic countries has a Constitution that explicitly includes a comprehensive chapter on Fundamental Duties of citizens?",
    "பின்வரும் முக்கிய ஜனநாயக நாடுகளில் குடிமக்களின் அடிப்படை கடமைகள் பற்றிய விரிவான அத்தியாயத்தை வெளிப்படையாகக் கொண்டுள்ள அரசியலமைப்பைக் கொண்ட நாடு எது?",
    "", "", "", "",
    "United States of America", "அமெரிக்க ஐக்கிய நாடுகள்",
    "Japan", "ஜப்பான்",
    "United Kingdom", "ஐக்கிய இராச்சியம்",
    "Canada", "கனடா",
    "B",
    "Japan is one of the rare democratic Constitutions (post-WWII Constitution 1947) that explicitly contains a chapter on citizen duties alongside rights.",
    "ஜப்பான் தனது அரசியலமைப்பில் (1947) உரிமைகளுடன் கடமைகள் பற்றிய அத்தியாயத்தையும் வெளிப்படையாகக் கொண்டுள்ள அரிய ஜனநாயக நாடுகளில் ஒன்றாகும்.",
    "Japan's Constitution explicitly contains citizen duties.", "ஜப்பானின் அரசியலமைப்பு வெளிப்படையாகக் குடிமக்களின் கடமைகளைக் கொண்டுள்ளது.",
    "USA Constitution has no explicit Duty chapter.", "அமெரிக்க அரசியலமைப்பில் கடமைகள் அத்தியாயம் இல்லை.",
    "UK has no written constitution.", "இங்கிலாந்திற்கு எழுதப்பட்ட அரசியலமைப்பு இல்லை.",
    "Canada Constitution has no explicit Duty chapter.", "கனடா அரசியலமைப்பில் கடமைகள் அத்தியாயம் இல்லை.",
    "TNPSC Trap: Socialist Constitutions (like USSR) traditionally contained duties, whereas democratic Constitutions (except Japan & India) did not.",
    "TNPSC பொறி: சோசலிச அரசியலமைப்புகள் பாரம்பரியமாகக் கடமைகளைக் கொண்டிருந்தன, ஆனால் ஜனநாயக நாடுகள் (ஜப்பான் & இந்தியா தவிர) கொண்டிருக்கவில்லை.",
    "Japan's Post-war Constitution was enacted in 1947.",
    "ஜப்பானின் போருக்குப் பிந்தைய அரசியலமைப்பு 1947-ல் இயற்றப்பட்டது.",
    ["TNPSC Group 4 2019 PYQ", "Samacheer Kalvi"], "Actual PYQ", "Remember", 45
))

# Q35 - PYQ Pattern -> C
questions.append(create_q(
    "FD_PYQ_035", "Easy", "Direct MCQ",
    "What is the primary legal distinction between Fundamental Rights under Part III and Fundamental Duties under Part IVA?",
    "பகுதி III-ன் கீழ் உள்ள அடிப்படை உரிமைகளுக்கும் பகுதி IVA-ன் கீழ் உள்ள அடிப்படை கடமைகளுக்கும் இடையிலான முதன்மைச் சட்ட வேறுபாடு என்ன?",
    "", "", "", "",
    "Fundamental Rights are non-justiciable, while Fundamental Duties are justiciable", "அடிப்படை உரிமைகள் அமல்படுத்த முடியாதவை, அடிப்படை கடமைகள் அமல்படுத்தக் கூடியவை",
    "Both are directly justiciable through Supreme Court writ petitions", "இரண்டும் உச்சநீதிமன்ற நீதிப்பேராணைகள் மூலம் நேரடியாக அமல்படுத்தப்படக் கூடியவை",
    "Fundamental Rights are justiciable in court, while Fundamental Duties are non-justiciable", "அடிப்படை உரிமைகள் நீதிமன்றத்தால் அமல்படுத்தப்படக் கூடியவை, அடிப்படை கடமைகள் அமல்படுத்தப்பட முடியாதவை",
    "Both apply only during Internal Emergency proclaimed under Article 352", "இரண்டும் உறுப்பு 352 அவசரநிலையின் போது மட்டுமே பொருந்தும்",
    "C",
    "Fundamental Rights (Part III) are directly justiciable (enforceable via writs under Art 32/226), whereas Fundamental Duties (Part IVA) are non-justiciable by themselves.",
    "அடிப்படை உரிமைகள் (பகுதி III) நேரடியாக நீதிமன்றத்தால் அமல்படுத்தப்படக் கூடியவை (உறுப்பு 32/226), ஆனால் அடிப்படை கடமைகள் (பகுதி IVA) நேரடியாக அமல்படுத்தப்பட முடியாதவை.",
    "Fundamental Rights are justiciable; Fundamental Duties are non-justiciable.", "அடிப்படை உரிமைகள் அமல்படுத்தக் கூடியவை; அடிப்படை கடமைகள் அமல்படுத்த முடியாதவை.",
    "Reversed statement is false.", "தலைகீழ் கூற்று தவறானது.",
    "Fundamental Duties are not directly writ-enforceable.", "அடிப்படை கடமைகள் நேரடியாக நீதிப்பேராணை மூலம் அமல்படுத்தக் கூடியவை அல்ல.",
    "Fundamental Rights apply at all times subject to reasonable restrictions.", "அடிப்படை உரிமைகள் அனைத்து நேரங்களிலும் பொருந்தும்.",
    "TNPSC Trap: Parliament CAN pass statutory laws enforcing Fundamental Duties, making specific violations punishable under those Acts.",
    "TNPSC பொறி: நாடாளுமன்றம் அடிப்படை கடமைகளை அமல்படுத்தச் சட்டங்களை இயற்றலாம், குறிப்பிட்ட மீறல்களை அச்சத்துக்கள் மூலம் தண்டிக்கலாம்.",
    "Part III is justiciable under Article 32.", "பகுதி III உறுப்பு 32-ன் கீழ் அமல்படுத்தக் கூடியது.",
    ["TNPSC Group 1 Pattern", "M. Laxmikanth"], "PYQ Pattern", "Understand", 45
))

# Q36 - PYQ Pattern -> D
questions.append(create_q(
    "FD_PYQ_036", "Medium", "Three-Statement",
    "Consider the following statements regarding the 86th Constitutional Amendment Act, 2002:\n\n1. It inserted Article 21A making free and compulsory education a Fundamental Right for children aged 6-14 years.\n2. It substituted Article 45 directing early childhood care and education for children below 6 years.\n3. It added Article 51A(k) placing a Fundamental Duty on parents/guardians to provide education opportunities to children aged 6-14 years.\n\nWhich of the statements given above are correct?",
    "2002-ன் 86வது அரசியலமைப்பு திருத்தச் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n\n1. இது 6-14 வயதுடைய குழந்தைகளுக்கு இலவச மற்றும் கட்டாயக் கல்வியை அடிப்படை உரிமையாக்கும் உறுப்பு 21A-ஐ இணைத்தது.\n2. இது 6 வயதிற்குட்பட்ட குழந்தைகளுக்கு ஆரம்பகால குழந்தை பராமரிப்பு மற்றும் கல்வியை வழிகாட்டும் உறுப்பு 45-ஐ மாற்றியமைத்தது.\n3. இது 6-14 வயதுடைய குழந்தைகளுக்குக் கல்விக்கான வாய்ப்புகளை வழங்க பெற்றோர்/பாதுகாவலர்களுக்கு கடமையாக்கும் உறுப்பு 51A(k)-ஐச் சேர்த்தது.\n\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
    "", "", "", "",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "D",
    "All three statements are correct. The 86th CAA 2002 amended Part III (Art 21A), Part IV (Art 45), and Part IVA [Art 51A(k)] to create a unified education triad.",
    "மூன்று கூற்றுகளும் சரியானவை. 86வது திருத்தம் 2002 பகுதி III (உறுப்பு 21A), பகுதி IV (உறுப்பு 45), பகுதி IVA [உறுப்பு 51A(k)] ஆகியவற்றைத் திருத்தியது.",
    "All three statements (1, 2, and 3) are true.", "மூன்று கூற்றுகளும் (1, 2, மற்றும் 3) சரியானவை.",
    "Statement 1 is correct (Art 21A FR).", "கூற்று 1 சரி (உறுப்பு 21A FR).",
    "Statement 2 is correct (Art 45 DPSP).", "கூற்று 2 சரி (உறுப்பு 45 DPSP).",
    "Statement 3 is correct (Art 51A(k) FD).", "கூற்று 3 சரி (உறுப்பு 51A(k) FD).",
    "TNPSC Trap: Age breakdown: 6-14 years for Art 21A & 51A(k); below 6 years for Art 45.",
    "TNPSC பொறி: வயது வகைப்பாடு: 21A & 51A(k)-க்கு 6-14 ஆண்டுகள்; 45-க்கு 6 வயதிற்குட்பட்டது.",
    "RTE Act 2009 operationalized Article 21A.", "RTE சட்டம் 2009 உறுப்பு 21A-ஐ நடைமுறைப்படுத்தியது.",
    ["TNPSC Group 1 Pattern", "NCERT"], "PYQ Pattern", "Analyze", 60
))

# Q37 - Actual PYQ -> A
questions.append(create_q(
    "FD_PYQ_037", "Easy", "Direct MCQ",
    "Protection of wildlife, forests, lakes, and rivers is mentioned in which combination of Constitutional Parts?",
    "வனவிலங்குகள், காடுகள், ஏரிகள் மற்றும் ஆறுகளைப் பாதுகாத்தல் அரசியலமைப்பின் எந்தப் பகுதிகளின் சேர்க்கையில் குறிப்பிடப்பட்டுள்ளது?",
    "", "", "", "",
    "Part IV (DPSP) and Part IVA (FD)", "பகுதி IV (DPSP) மற்றும் பகுதி IVA (FD)",
    "Part III (FR) and Part IV (DPSP)", "பகுதி III (FR) மற்றும் பகுதி IV (DPSP)",
    "Part III (FR) and Part IVA (FD)", "பகுதி III (FR) மற்றும் பகுதி IVA (FD)",
    "Part I and Part II", "பகுதி I மற்றும் பகுதி II",
    "A",
    "Environmental and wildlife protection is mentioned in Part IV under DPSP Article 48A (State duty) AND Part IVA under Fundamental Duty Article 51A(g) (Citizen duty).",
    "சுற்றுச்சூழல் மற்றும் வனவிலங்கு பாதுகாப்பு பகுதி IV-ல் DPSP உறுப்பு 48A (அரசு கடமை) மற்றும் பகுதி IVA-ல் அடிப்படை கடமை உறுப்பு 51A(g) (குடிமகன் கடமை) ஆகியவற்றில் குறிப்பிடப்பட்டுள்ளது.",
    "Part IV (Art 48A) and Part IVA (Art 51A(g)) together cover environmental protection.", "பகுதி IV (உறுப்பு 48A) மற்றும் பகுதி IVA (உறுப்பு 51A(g)) இணைந்து சுற்றுச்சூழல் பாதுகாப்பைக் கவர் செய்கின்றன.",
    "Part III has no explicit environmental clause.", "பகுதி III-ல் வெளிப்படையான சுற்றுச்சூழல் விதி இல்லை.",
    "Part III does not contain environment clause explicitly.", "பகுதி III-ல் வெளிப்படையாக இல்லை.",
    "Part I/II deal with Territory and Citizenship.", "பகுதி I/II நிலப்பரப்பு மற்றும் குடியுரிமையைக் கையாள்கின்றன.",
    "TNPSC Trap: Judicial decisions under Article 21 (Right to Life) also include right to clean environment.",
    "TNPSC பொறி: உறுப்பு 21 (வாழும் உரிமை) நீதிமன்றத் தீர்ப்புகளும் தூய்மையான சுற்றுச்சூழல் உரிமையை உள்ளடக்கியுள்ளன.",
    "Both Art 48A and 51A(g) were introduced by 42nd CAA 1976.",
    "உறுப்பு 48A மற்றும் 51A(g) இரண்டும் 42வது திருத்தம் 1976 மூலம் அறிமுகப்படுத்தப்பட்டன.",
    ["TNPSC Group 1 2018 PYQ", "Samacheer Kalvi"], "Actual PYQ", "Remember", 45
))

# Q38 - PYQ Pattern -> B
questions.append(create_q(
    "FD_PYQ_038", "Medium", "Chronology",
    "Arrange the following Constitutional Amendment Acts in chronological order:\n\n1. 42nd Constitutional Amendment Act\n2. 44th Constitutional Amendment Act\n3. 86th Constitutional Amendment Act\n4. 97th Constitutional Amendment Act",
    "பின்வரும் அரசியலமைப்பு திருத்தச் சட்டங்களை காலவரிசைப்படி வரிசைப்படுத்துக:\n\n1. 42வது அரசியலமைப்பு திருத்தச் சட்டம்\n2. 44வது அரசியலமைப்பு திருத்தச் சட்டம்\n3. 86வது அரசியலமைப்பு திருத்தச் சட்டம்\n4. 97வது அரசியலமைப்பு திருத்தச் சட்டம்",
    "", "", "", "",
    "2 - 1 - 4 - 3", "2 - 1 - 4 - 3",
    "1 - 2 - 3 - 4", "1 - 2 - 3 - 4",
    "1 - 3 - 2 - 4", "1 - 3 - 2 - 4",
    "4 - 3 - 2 - 1", "4 - 3 - 2 - 1",
    "B",
    "Chronological order: 1. 42nd CAA (1976) -> 2. 44th CAA (1978) -> 3. 86th CAA (2002) -> 4. 97th CAA (2011). Sequence: 1 - 2 - 3 - 4.",
    "காலவரிசை: 1. 42வது திருத்தம் (1976) -> 2. 44வது திருத்தம் (1978) -> 3. 86வது திருத்தம் (2002) -> 4. 97வது திருத்தம் (2011). வரிசை: 1 - 2 - 3 - 4.",
    "1 - 2 - 3 - 4 is the exact chronological sequence.", "1 - 2 - 3 - 4 என்பது சரியான காலவரிசையாகும்.",
    "2 - 1 is reverse (44th came after 42nd).", "2 - 1 தலைகீழ் (42வதுக்குப் பிறகே 44வது வந்தது).",
    "3 is 2002, which is after 1978.", "3 என்பது 2002, அது 1978-க்கு பிறகானது.",
    "4 - 3 - 2 - 1 is reverse order.", "4 - 3 - 2 - 1 என்பது தலைகீழ் வரிசை.",
    "TNPSC Trap: 42nd CAA added 10 duties in 1976; 44th CAA retained duties in 1978; 86th CAA added 11th duty in 2002.",
    "TNPSC பொறி: 42வது திருத்தம் 10 கடமைகளைச் சேர்த்தது (1976); 44வது திருத்தம் கடமைகளைத் தக்கவைத்தது (1978); 86வது திருத்தம் 11வது கடமையைச் சேர்த்தது (2002).",
    "Sequence spans 1976 to 2011.",
    "இவ்வரிசை 1976 முதல் 2011 வரை நீடிக்கிறது.",
    ["TNPSC Group 1 Pattern", "M. Laxmikanth"], "PYQ Pattern", "Analyze", 60
))

# Q39 - PYQ Pattern -> C
questions.append(create_q(
    "FD_PYQ_039", "Hard", "Case Application",
    "In Aruna Roy v. Union of India (2002), the Supreme Court held that value-based education derived from comparative religious philosophy promotes which Fundamental Duty clause(s)?",
    "அருணா ராய் எதிராக இந்திய யூனியன் (2002) வழக்கில், ஒப்பிட்டு மதக் கல்வி சார்ந்த மதிப்புக் கல்வி எந்த அடிப்படை கடமை உட்பிரிவை ஊக்குவிக்கிறது என உச்சநீதிமன்றம் கூறியது?",
    "", "", "", "",
    "Article 51A(a)", "உறுப்பு 51A(a)",
    "Article 51A(i)", "உறுப்பு 51A(i)",
    "Article 51A(e) & (f)", "உறுப்பு 51A(e) & (f)",
    "Article 51A(k)", "உறுப்பு 51A(k)",
    "C",
    "In Aruna Roy (2002), SC held that teaching universal moral values promotes common brotherhood under Article 51A(e) and cultural harmony under Article 51A(f) without violating Article 28 secularism.",
    "அருணா ராய் வழக்கில் (2002), உலகளாவிய தர்ம மதிப்புகளைக் கற்பிப்பது உறுப்பு 51A(e)-ன் கீழ் சகோதரத்துவத்தையும் 51A(f)-ன் கீழ் பண்பாட்டு நல்லிணக்கத்தையும் ஊக்குவிக்கிறது என உச்சநீதிமன்றம் கூறியது.",
    "Article 51A(e) and (f) were explicitly linked to value-based education in Aruna Roy judgment.", "அருணா ராய் தீர்ப்பில் உறுப்புகள் 51A(e) மற்றும் (f) மதிப்புக் கல்வியுடன் நேரடியாக இணைக்கப்பட்டன.",
    "Article 51A(a) concerns Flag/Anthem.", "உறுப்பு 51A(a) கொடி/கீதம் பற்றியது.",
    "Article 51A(i) concerns public property.", "உறுப்பு 51A(i) பொதுச் சொத்து பற்றியது.",
    "Article 51A(k) concerns child school admission duty.", "உறுப்பு 51A(k) குழந்தைகள் பள்ளிச் சேர்க்கைக் கடமை பற்றியது.",
    "TNPSC Trap: Article 28(1) prohibits 'religious instruction' in state schools, but permits 'value-based education' and comparative study of religions.",
    "TNPSC பொறி: உறுப்பு 28(1) 'மதப் போதனையைத்' தடை செய்கிறது, ஆனால் 'மதிப்புக் கல்வியையும்' மதங்களின் ஒப்பீட்டு ஆய்வையும் அனுமதிக்கிறது.",
    "Judgment delivered by 3-judge Bench.", "3 நீதிபதிகள் அமர்வு தீர்ப்பு வழங்கியது.",
    ["TNPSC Group 1 Pattern", "M. Laxmikanth"], "PYQ Pattern", "Analyze", 60
))

# Q40 - PYQ Pattern -> D
questions.append(create_q(
    "FD_PYQ_040", "Medium", "Assertion & Reason",
    "Assertion (A): Parliament can enact statutory laws to penalize non-compliance with any Fundamental Duty under Article 51A.\nReason (R): Courts will uphold the constitutional validity of parliamentary laws that impose reasonable restrictions on rights to enforce Fundamental Duties.",
    "கூற்று (A): உறுப்பு 51A-ன் கீழ் உள்ள எந்தவொரு அடிப்படை கடமையையும் பின்பற்றாத தண்டிக்க நாடாளுமன்றம் சட்டங்களை இயற்ற முடியும்.\nகாரணம் (R): அடிப்படை கடமைகளை அமல்படுத்த உரிமைகள் மீது நியாயமான கட்டுப்பாடுகளை விதிக்கும் நாடாளுமன்றச் சட்டங்களின் அரசியலமைப்பு செல்லுபடியாகும் தன்மையை நீதிமன்றங்கள் உறுதி செய்யும்.",
    "Parliament can enact statutory laws to penalize non-compliance with any Fundamental Duty under Article 51A.",
    "உறுப்பு 51A-ன் கீழ் உள்ள எந்தவொரு அடிப்படை கடமையையும் பின்பற்றாத தண்டிக்க நாடாளுமன்றம் சட்டங்களை இயற்ற முடியும்.",
    "Courts will uphold the constitutional validity of parliamentary laws that impose reasonable restrictions on rights to enforce Fundamental Duties.",
    "அடிப்படை கடமைகளை அமல்படுத்த உரிமைகள் மீது நியாயமான கட்டுப்பாடுகளை விதிக்கும் நாடாளுமன்றச் சட்டங்களின் அரசியலமைப்பு செல்லுபடியாகும் தன்மையை நீதிமன்றங்கள் உறுதி செய்யும்.",
    "Both A and R are correct but R is NOT the correct explanation of A", "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல.",
    "A is correct but R is incorrect", "A சரி, ஆனால் R தவறு.",
    "A is incorrect but R is correct", "A தவறு, ஆனால் R சரி.",
    "Both A and R are correct and R is the correct explanation of A", "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்.",
    "D",
    "Both A and R are true, and R explains A. Non-justiciability means duties cannot be directly writ-enforced by themselves, but Parliament has full power to legislate enforcers which courts will validate.",
    "கூற்று A மற்றும் காரணம் R இரண்டும் சரி, மேலும் R என்பது A-விற்கு சரியான விளக்கம். கடமைகளைத் நேரடியாக அமல்படுத்த முடியாது என்றாலும் நாடாளுமன்றத்திற்குச் சட்டமியற்றும் முழு அதிகாரம் உண்டு, நீதிமன்றங்கள் அதை உறுதி செய்யும்.",
    "Both A and R are true, and R explains why parliamentary enabling laws are valid.", "A மற்றும் R இரண்டும் சரி, மேலும் நாடாளுமன்றச் சட்டங்கள் ஏன் செல்லுபடியாகும் என்பதை R விளக்குகிறது.",
    "Reason explains Assertion directly.", "காரணம் கூற்றை நேரடியாக விளக்குகிறது.",
    "Reason is factually correct.", "காரணம் சரியானது.",
    "Assertion is factually true.", "கூற்று சரியானது.",
    "TNPSC Trap: Prevention of Insults to National Honour Act 1971 and Wildlife Act 1972 are exact examples of parliamentary statutory enforcers.",
    "TNPSC பொறி: 1971-ன் தேசிய சின்னங்கள் அவமதிப்பு சட்டம் மற்றும் 1972-ன் வனவிலங்கு சட்டம் ஆகியவை நாடாளுமன்றச் சட்ட அமலாக்கிகளுக்குச் சரியான உதராணங்களாகும்.",
    "Verma Committee listed 7 major Parliamentary Acts enforcing duties.", "வர்மா குழு கடமைகளை அமல்படுத்தும் 7 முக்கிய நாடாளுமன்றச் சட்டங்களைப் பட்டியலிட்டது.",
    ["TNPSC Group 1 Pattern", "M. Laxmikanth"], "PYQ Pattern", "Analyze", 60
))

# Q41 - Actual PYQ -> A
questions.append(create_q(
    "FD_PYQ_041", "Easy", "Direct MCQ",
    "Under Article 51A(c), citizens are required to uphold and protect what three core concepts of India?",
    "உறுப்பு 51A(c)-ன் கீழ் குடிமக்கள் இந்தியாவின் எந்த மூன்று முக்கியக் கோட்பாடுகளைப் பேணிப் பாதுகாக்க வேண்டும்?",
    "", "", "", "",
    "Sovereignty, Unity and Integrity", "இறையாண்மை, ஒற்றுமை மற்றும் ஒருமைப்பாடு",
    "Liberty, Equality and Fraternity", "சுதந்திரம், சமத்துவம் மற்றும் சகோதரத்துவம்",
    "Justice, Social and Economic", "நீதி, சமூகம் மற்றும் பொருளாதாரம்",
    "Democracy, Secularism and Socialism", "ஜனநாயகம், மதச்சார்பின்மை மற்றும் சோசலிசம்",
    "A",
    "Article 51A(c) states that it shall be the duty of every citizen of India 'to uphold and protect the sovereignty, unity and integrity of India'.",
    "உறுப்பு 51A(c) 'இந்தியாவின் இறையாண்மை, ஒற்றுமை மற்றும் ஒருமைப்பாட்டைப் பேணிப் பாதுகாப்பது' ஒவ்வொரு குடிமகனின் கடமையாகும் எனக் குறிப்பிடுகிறது.",
    "Article 51A(c) explicitly contains Sovereignty, Unity and Integrity.", "உறுப்பு 51A(c) இறையாண்மை, ஒற்றுமை மற்றும் ஒருமைப்பாட்டை வெளிப்படையாகக் கொண்டுள்ளது.",
    "Liberty, Equality, Fraternity is from Preamble / French Revolution.", "சுதந்திரம், சமத்துவம், சகோதரத்துவம் முகப்புரை / பிரெஞ்சு புரட்சியிலிருந்து வந்தது.",
    "Justice Social Economic is from Preamble / Russian Revolution.", "நீதி சமூக பொருளாதாரம் முகப்புரை / ரஷ்ய புரட்சியிலிருந்து வந்தது.",
    "Democracy Secularism is Preamble objective.", "ஜனநாயகம் மதச்சார்பின்மை முகப்புரை இலக்காகும்.",
    "TNPSC Trap: Sovereignty, Unity and Integrity are mentioned in BOTH Preamble AND Article 51A(c).",
    "TNPSC பொறி: இறையாண்மை, ஒற்றுமை மற்றும் ஒருமைப்பாடு ஆகியவை முகப்புரை மற்றும் உறுப்பு 51A(c) இரண்டிலும் குறிப்பிடப்பட்டுள்ளன.",
    "Section 153B of IPC penalizes actions against national integration.", "IPC பிரிவு 153B தேசிய ஒருமைப்பாட்டிற்கு எதிரான நடவடிக்கைகளைத் தண்டிக்கிறது.",
    ["TNPSC Group 2 2014 PYQ", "Samacheer Kalvi"], "Actual PYQ", "Remember", 45
))

# Q42 - PYQ Pattern -> B
questions.append(create_q(
    "FD_PYQ_042", "Medium", "Two-Statement",
    "Consider the following statements regarding Article 51A(e) ('Brotherhood'):\n\n1. Article 51A(e) requires citizens to promote harmony transcending religious, linguistic, regional, or sectional diversities.\n2. Section 153A of the IPC penalizes promoting enmity between different groups on grounds of religion, race, place of birth, or language, enforcing Article 51A(e).\n\nWhich of the statement(s) given above is/are correct?",
    "உறுப்பு 51A(e) ('சகோதரத்துவம்') பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n\n1. உறுப்பு 51A(e) மத, மொழி, பிராந்திய அல்லது பிரிவு வேறுபாடுகளைக் கடந்து நல்லிணக்கத்தை வளர்க்கக் குடிமக்களுக்குக் கடமையாக்குகிறது.\n2. IPC பிரிவு 153A மதம், இனம், பிறந்த இடம் அல்லது மொழியின் அடிப்படையில் குழுக்களிடையே பகைமையை வளர்ப்பதைத் தண்டித்து, உறுப்பு 51A(e)-ஐ அமல்படுத்துகிறது.\n\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானவை?",
    "", "", "", "",
    "1 only", "1 மட்டும்",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "2 only", "2 மட்டும்",
    "Neither 1 nor 2", "எதுவும் இல்லை",
    "B",
    "Both statements are correct. Article 51A(e) commands harmony transcending diversities, and IPC Section 153A acts as its statutory penal enforcer.",
    "இரண்டு கூற்றுகளும் சரியானவை. உறுப்பு 51A(e) வேறுபாடுகளைக் கடந்த நல்லிணக்கத்தைக் கட்டாயமாக்குகிறது, மேலும் IPC பிரிவு 153A அதன் சட்டத் தண்டனை அமலாக்கியாகச் செயல்படுகிறது.",
    "Both 1 and 2 are true.", "1 மற்றும் 2 இரண்டும் சரியானவை.",
    "Statement 1 is factually true under Art 51A(e).", "கூற்று 1 உறுப்பு 51A(e)-ன் படி சரியானது.",
    "Statement 2 is factually true regarding IPC Sec 153A.", "IPC பிரிவு 153A பற்றிய கூற்று 2 சரியானது.",
    "Neither is false.", "எதுவும் தவறல்ல.",
    "TNPSC Trap: Article 51A(e) lists 4 specific diversities: Religious, Linguistic, Regional, Sectional.",
    "TNPSC பொறி: உறுப்பு 51A(e) 4 குறிப்பிட்ட வேறுபாடுகளைப் பட்டியலிடுகிறது: மத, மொழி, பிராந்திய, பிரிவு வேறுபாடுகள்.",
    "Verma Committee identified IPC 153A as a key duty enforcer.", "வர்மா குழு IPC 153A-வை முக்கிய கடமை அமலாக்கியாகச் சுட்டிக்காட்டியது.",
    ["TNPSC Group 1 Pattern", "NCERT"], "PYQ Pattern", "Understand", 45
))

# Q43 - PYQ Pattern -> C
questions.append(create_q(
    "FD_PYQ_043", "Easy", "Direct MCQ",
    "Which of the following commissions or committees was NOT associated with reviewing, recommending, or mapping provisions regarding Fundamental Duties?",
    "அடிப்படை கடமைகள் பற்றிய வினைகளை மறுஆய்வு செய்வதிலோ, பரிந்துரைப்பதிலோ அல்லது வரைபடமாக்குவதிலோ தொடர்பில்லாத ஆணையம் அல்லது குழு எது?",
    "", "", "", "",
    "Swaran Singh Committee (1976)", "ஸ்வரன் சிங் குழு (1976)",
    "Justice Verma Committee (1999)", "நீதியரசர் வர்மா குழு (1999)",
    "Kothari Education Commission (1964-66)", "கோத்தாரி கல்விக் குழு (1964-66)",
    "NCRWC / Venkatachaliah Commission (2002)", "NCRWC / வெங்கடாசலய்யா ஆணையம் (2002)",
    "C",
    "Kothari Education Commission (1964-66) was appointed for national education policy prior to the introduction of Fundamental Duties in 1976. Swaran Singh, Verma, and NCRWC were directly associated with Fundamental Duties.",
    "கோத்தாரி கல்விக் குழு (1964-66) 1976-ல் அடிப்படை கடமைகள் அறிமுகப்படுத்தப்படுவதற்கு முன்பே தேசிய கல்விக் கொள்கைக்காக நியமிக்கப்பட்டது.",
    "Kothari Commission (1964) predates Fundamental Duties (1976).", "கோத்தாரி குழு (1964) அடிப்படை கடமைகளுக்கு (1976) முந்தையது.",
    "Swaran Singh proposed Part IVA in 1976.", "ஸ்வரன் சிங் 1976-ல் பகுதி IVA-வை முன்மொழிந்தார்.",
    "Verma Committee mapped statutory enforcers in 1999.", "வர்மா குழு 1999-ல் சட்ட அமலாக்கிகளை வரைபடமாக்கியது.",
    "NCRWC reviewed Part IVA in 2002.", "NCRWC 2002-ல் பகுதி IVA-வை மறுஆய்வு செய்தது.",
    "TNPSC Trap: Kothari Commission recommended 10+2+3 education structure, not Fundamental Duties.",
    "TNPSC பொறி: கோத்தாரி குழு 10+2+3 கல்விக் கட்டமைப்பைப் பரிந்துரைத்தது, அடிப்படை கடமைகளை அல்ல.",
    "Kothari Commission was headed by Daulat Singh Kothari.", "கோத்தாரி குழுவிற்கு தௌலத் சிங் கோத்தாரி தலைமை தாங்கினார்.",
    ["TNPSC Group 1 Pattern", "Samacheer Kalvi"], "PYQ Pattern", "Remember", 45
))

# Q44 - Actual PYQ -> D
questions.append(create_q(
    "FD_PYQ_044", "Easy", "Direct MCQ",
    "The duty to safeguard public property and abjure violence is enshrined in which clause of Article 51A?",
    "பொதுச் சொத்தைப் பாதுகாக்கவும் வன்முறையைக் கைவிடவும் உள்ள கடமை உறுப்பு 51A-ன் எந்த உட்பிரிவில் பொறிக்கப்பட்டுள்ளது?",
    "", "", "", "",
    "Article 51A(f)", "உறுப்பு 51A(f)",
    "Article 51A(g)", "உறுப்பு 51A(g)",
    "Article 51A(h)", "உறுப்பு 51A(h)",
    "Article 51A(i)", "உறுப்பு 51A(i)",
    "D",
    "Article 51A(i) mandates every citizen of India 'to safeguard public property and to abjure violence'.",
    "உறுப்பு 51A(i) 'பொதுச் சொத்தைப் பாதுகாக்கவும் வன்முறையைக் கைவிடவும்' ஒவ்வொரு இந்தியக் குடிமகனுக்கும் கடமையாக்குகிறது.",
    "Article 51A(i) explicitly contains the public property safeguarding clause.", "உறுப்பு 51A(i) பொதுச் சொத்தைப் பாதுகாக்கும் விதியை வெளிப்படையாகக் கொண்டுள்ளது.",
    "Article 51A(f) concerns composite culture.", "உறுப்பு 51A(f) கூட்டுப் பண்பாடு பற்றியது.",
    "Article 51A(g) concerns natural environment.", "உறுப்பு 51A(g) இயற்கைச் சூழல் பற்றியது.",
    "Article 51A(h) concerns scientific temper.", "உறுப்பு 51A(h) அறிவியல் மனப்பான்மை பற்றியது.",
    "TNPSC Trap: Prevention of Damage to Public Property Act 1984 acts as the statutory enforcer of Article 51A(i).",
    "TNPSC பொறி: 1984-ன் பொதுச் சொத்து சேதத் தடுப்புச் சட்டம் உறுப்பு 51A(i)-ன் சட்ட அமலாக்கியாகச் செயல்படுகிறது.",
    "Added as part of the original 10 duties in 1976.", "1976-ல் அசல் 10 கடமைகளின் பகுதியாகச் சேர்க்கப்பட்டது.",
    ["TNPSC Group 1 2013 PYQ", "Samacheer Kalvi"], "Actual PYQ", "Remember", 45
))

# Q45 - PYQ Pattern -> A
questions.append(create_q(
    "FD_PYQ_045", "Medium", "Three-Statement",
    "Consider the following statements regarding the 86th Constitutional Amendment Act, 2002:\n\n1. It added Article 51A(k) as the 11th Fundamental Duty.\n2. It added Article 21A as a Fundamental Right.\n3. It amended Article 45 in Directive Principles of State Policy.\n\nWhich of the statements given above are correct?",
    "2002-ன் 86வது அரசியலமைப்பு திருத்தச் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n\n1. இது 11வது அடிப்படை கடமையாக உறுப்பு 51A(k)-ஐச் சேர்த்தது.\n2. இது ஒரு அடிப்படை உரிமையாக உறுப்பு 21A-ஐச் சேர்த்தது.\n3. இது அரசு நெறிமுறைப் பிரிவுகளில் உறுப்பு 45-ஐ திருத்தியது.\n\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
    "", "", "", "",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "A",
    "All three statements are correct. The 86th Amendment Act, 2002 simultaneously modified three Parts of the Constitution: Part III (Art 21A), Part IV (Art 45), and Part IVA [Art 51A(k)].",
    "மூன்று கூற்றுகளும் சரியானவை. 2002-ன் 86வது திருத்தச் சட்டம் ஒரே நேரத்தில் அரசியலமைப்பின் மூன்று பகுதிகளைத் திருத்தியது: பகுதி III (உறுப்பு 21A), பகுதி IV (உறுப்பு 45), பகுதி IVA [உறுப்பு 51A(k)].",
    "All three statements (1, 2, and 3) are true.", "மூன்று கூற்றுகளும் (1, 2, மற்றும் 3) சரியானவை.",
    "Statement 1 is correct (Art 51A(k) FD).", "கூற்று 1 சரி (உறுப்பு 51A(k) FD).",
    "Statement 2 is correct (Art 21A FR).", "கூற்று 2 சரி (உறுப்பு 21A FR).",
    "Statement 3 is correct (Art 45 DPSP).", "கூற்று 3 சரி (உறுப்பு 45 DPSP).",
    "TNPSC Trap: 86th CAA 2002 is unique in modifying Part III, Part IV, and Part IVA simultaneously.",
    "TNPSC பொறி: 86வது திருத்தம் 2002 ஒரே நேரத்தில் பகுதி III, பகுதி IV, பகுதி IVA ஆகிய மூன்றையும் திருத்தியதில் தனித்துவமானது.",
    "The 11th duty was added 26 years after the first 10 duties.", "முதல் 10 கடமைகளுக்கு 26 ஆண்டுகளுக்குப் பிறகே 11வது கடமை சேர்க்கப்பட்டது.",
    ["TNPSC Group 1 Pattern", "NCERT"], "PYQ Pattern", "Analyze", 60
))

# Q46 - PYQ Pattern -> B
questions.append(create_q(
    "FD_PYQ_046", "Medium", "Match",
    "Match List I (Key Constitutional Concept) with List II (Article 51A Clause):\n\nList I:\na. Freedom struggle noble ideals\nb. Scientific temper & humanism\nc. Excellence in all spheres\nd. Parent duty for child education\n\nList II:\n1. Article 51A(b)\n2. Article 51A(h)\n3. Article 51A(j)\n4. Article 51A(k)",
    "பட்டியல் I-ஐ (முக்கிய அரசியலமைப்புக் கருத்து) பட்டியல் II உடன் (உறுப்பு 51A உட்பிரிவு) பொருத்துக:\n\nபட்டியல் I:\na. சுதந்திரப் போராட்ட உயரிய லட்சியங்கள்\nb. அறிவியல் மனப்பான்மை & மனிதநேயம்\nc. அனைத்துத் துறைகளிலும் சிறப்பு\nd. குழந்தை கல்விக்கான பெற்றோர் கடமை\n\nபட்டியல் II:\n1. உறுப்பு 51A(b)\n2. உறுப்பு 51A(h)\n3. உறுப்பு 51A(j)\n4. உறுப்பு 51A(k)",
    "", "", "", "",
    "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
    "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
    "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2",
    "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1",
    "B",
    "Correct match: Freedom ideals -> Art 51A(b) (1); Scientific temper -> Art 51A(h) (2); Excellence -> Art 51A(j) (3); Education -> Art 51A(k) (4). Sequence: 1-2-3-4.",
    "சரியான பொருத்தம்: சுதந்திர லட்சியங்கள் -> 51A(b) (1); அறிவியல் மனப்பான்மை -> 51A(h) (2); சிறப்பு -> 51A(j) (3); கல்வி -> 51A(k) (4). வரிசை: 1-2-3-4.",
    "a-1, b-2, c-3, d-4 is the exact verified match sequence.", "a-1, b-2, c-3, d-4 என்பது சரிபார்க்கப்பட்ட சரியான பொருத்த வரிசையாகும்.",
    "a-2 mismatch.", "a-2 தவறான பொருத்தம்.",
    "a-3 mismatch.", "a-3 தவறான பொருத்தம்.",
    "a-4 mismatch.", "a-4 தவறான பொருத்தம்.",
    "TNPSC Trap: Ensure precise clause assignment: (b) = freedom ideals, (h) = scientific temper, (j) = excellence, (k) = child education.",
    "TNPSC பொறி: துல்லியமான உட்பிரிவு ஒதுக்கீட்டை உறுதி செய்க: (b) = சுதந்திர லட்சியங்கள், (h) = அறிவியல் மனப்பான்மை, (j) = சிறப்பு, (k) = குழந்தை கல்வி.",
    "Clause (k) is the only duty added in 2002.", "உட்பிரிவு (k) 2002-ல் சேர்க்கப்பட்ட ஒரே கடமையாகும்.",
    ["TNPSC Group 1 Pattern", "Samacheer Kalvi"], "PYQ Pattern", "Analyze", 60
))

# Q47 - PYQ Pattern -> C
questions.append(create_q(
    "FD_PYQ_047", "Easy", "Direct MCQ",
    "In which year did the 86th Constitutional Amendment Act come into force, incorporating free education right and the 11th Fundamental Duty?",
    "இலவசக் கல்வி உரிமையையும் 11வது அடிப்படை கடமையையும் இணைத்த 86வது அரசியலமைப்பு திருத்தச் சட்டம் எந்த ஆண்டில் அமலுக்கு வந்தது?",
    "", "", "", "",
    "2000", "2000",
    "2009", "2009",
    "2002", "2002",
    "2010", "2010",
    "C",
    "The 86th Constitutional Amendment Act was enacted in 2002, adding Article 51A(k) as the 11th Fundamental Duty.",
    "2002-ல் 86வது அரசியலமைப்பு திருத்தச் சட்டம் இயற்றப்பட்டு, உறுப்பு 51A(k)-ஐ 11வது அடிப்படை கடமையாகச் சேர்த்தது.",
    "2002 is the exact enactment year of 86th CAA.", "2002 என்பது 86வது திருத்தம் இயற்றப்பட்ட ஆண்டாகும்.",
    "2000 was Sarva Shiksha Abhiyan launch year.", "2000 என்பது சர்வ சிக்சா அபியான் தொடங்கப்பட்ட ஆண்டு.",
    "2009 was RTE Act enactment year.", "2009 என்பது RTE சட்டம் இயற்றப்பட்ட ஆண்டு.",
    "2010 was RTE Act commencement year (April 1, 2010).", "2010 என்பது RTE சட்டம் அமலுக்கு வந்த ஆண்டு (ஏப்ரல் 1, 2010).",
    "TNPSC Trap: 86th CAA was passed in 2002, while the Right to Education (RTE) Act was passed in 2009 and came into force on April 1, 2010.",
    "TNPSC பொறி: 86வது திருத்தம் 2002-ல் நிறைவேறியது, ஆனால் கல்வி உரிமை (RTE) சட்டம் 2009-ல் நிறைவேறி ஏப்ரல் 1, 2010-ல் அமலுக்கு வந்தது.",
    "RTE Act operationalized Article 21A.", "RTE சட்டம் உறுப்பு 21A-ஐ நடைமுறைப்படுத்தியது.",
    ["TNPSC Group 1 Pattern", "NCERT"], "PYQ Pattern", "Remember", 45
))

# Q48 - Actual PYQ -> D
questions.append(create_q(
    "FD_PYQ_048", "Easy", "Direct MCQ",
    "Fundamental Duties were incorporated into the Indian Constitution during the tenure of which Prime Minister?",
    "எந்தப் பிரதம மந்திரியின் பதவிக் காலத்தில் இந்திய அரசியலமைப்பில் அடிப்படை கடமைகள் சேர்க்கப்பட்டன?",
    "", "", "", "",
    "Jawaharlal Nehru", "ஜவஹர்லால் நேரு",
    "Morarji Desai", "மொரார்ஜி தேசாய்",
    "Rajiv Gandhi", "ராஜீவ் காந்தி",
    "Indira Gandhi", "இந்திரா காந்தி",
    "D",
    "Fundamental Duties were introduced by the 42nd Constitutional Amendment Act, 1976 during the Prime Ministership of Indira Gandhi during the Internal Emergency.",
    "உள்நாட்டு அவசரநிலையின் போது இந்திரா காந்தி பிரதமராக இருந்த போது 1976-ன் 42வது அரசியலமைப்பு திருத்தச் சட்டம் மூலம் அடிப்படை கடமைகள் அறிமுகப்படுத்தப்பட்டன.",
    "Indira Gandhi was Prime Minister in 1976 when 42nd CAA was enacted.", "42வது திருத்தம் இயற்றப்பட்ட 1976-ல் இந்திரா காந்தி பிரதமராக இருந்தார்.",
    "Jawaharlal Nehru was PM from 1947 to 1964.", "ஜவஹர்லால் நேரு 1947 முதல் 1964 வரை பிரதமராக இருந்தார்.",
    "Morarji Desai was PM during 44th CAA (1977-79).", "44வது திருத்தத்தின் போது (1977-79) மொரார்ஜி தேசாய் பிரதமராக இருந்தார்.",
    "Rajiv Gandhi was PM from 1984 to 1989.", "ராஜீவ் காந்தி 1984 முதல் 1989 வரை பிரதமராக இருந்தார்.",
    "TNPSC Trap: Morarji Desai's Janata government enacted the 44th CAA in 1978, which retained Indira Gandhi's Part IVA intact.",
    "TNPSC பொறி: மொரார்ஜி தேசாயின் ஜனதா அரசு 1978-ல் 44வது திருத்தத்தை இயற்றியது, அது இந்திரா காந்தியின் பகுதி IVA-வை மாற்றாமல் தக்கவைத்தது.",
    "Sardar Swaran Singh submitted his report to Congress President D.K. Barooah in 1976.",
    "சர்தார் ஸ்வரன் சிங் 1976-ல் காங்கிரஸ் தலைவர் டி.கே. பரூவாவிடம் அறிக்கையைச் சமர்ப்பித்தார்.",
    ["TNPSC Group 2 2011 PYQ", "Samacheer Kalvi"], "Actual PYQ", "Remember", 45
))

# Q49 - PYQ Pattern -> C
questions.append(create_q(
    "FD_PYQ_049", "Medium", "Two-Statement",
    "Consider the following statements regarding the Supreme Court's interpretation of Fundamental Duties:\n\n1. Article 51A applies to every citizen of India.\n2. The Supreme Court in Javed v. State of Haryana (2003) reaffirmed that Fundamental Rights must be read along with Fundamental Duties and Directive Principles.\n\nWhich of the statement(s) given above is/are correct?",
    "அடிப்படை கடமைகள் பற்றிய உச்சநீதிமன்றத்தின் விளக்கம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n\n1. உறுப்பு 51A இந்தியாவின் ஒவ்வொரு குடிமகனுக்கும் பொருந்தும்.\n2. ஜாவேத் எதிராக ஹரியானா மாநில வழக்கிலும் (2003) அடிப்படை உரிமைகளை அடிப்படை கடமைகள் மற்றும் அரசு நெறிமுறைகளுடன் இணைத்தே படிக்க வேண்டும் என்று உச்சநீதிமன்றம் மீண்டும் உறுதிப்படுத்தியது.\n\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானவை?",
    "", "", "", "",
    "1 only", "1 மட்டும்",
    "2 only", "2 மட்டும்",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "Neither 1 nor 2", "எதுவும் இல்லை",
    "C",
    "Both statements are correct. Article 51A applies to citizens, and SC in Javed (2003) held that FRs cannot be read in isolation from FDs and DPSPs.",
    "இரண்டு கூற்றுகளும் சரியானவை. உறுப்பு 51A குடிமக்களுக்குப் பொருந்தும், மேலும் ஜாவேத் வழக்கில் (2003) அடிப்படை உரிமைகளை கடமைகள் மற்றும் நெறிமுறைகளிலிருந்து தனித்து படிக்க முடியாது என்று உச்சநீதிமன்றம் கூறியது.",
    "Both 1 and 2 are true.", "1 மற்றும் 2 இரண்டும் சரியானவை.",
    "Statement 1 is factually true under Art 51A.", "கூற்று 1 உறுப்பு 51A-ன் படி சரியானது.",
    "Statement 2 is factually true regarding Javed (2003) precedent.", "ஜாவேத் (2003) முன்மாதிரி பற்றிய கூற்று 2 சரியானது.",
    "Neither is false.", "எதுவும் தவறல்ல.",
    "TNPSC Trap: Javed (2003) upheld two-child norm for panchayat elections by reading Art 19/21 alongside Art 51A(j) and DPSP Art 47.",
    "TNPSC பொறி: ஜாவேத் (2003) வழக்கு பஞ்சாயத்துத் தேர்தல்களுக்கான இரண்டு குழந்தை விதியை உறுப்பு 51A(j) மற்றும் DPSP உறுப்பு 47 உடன் இணைத்து படித்து உறுதி செய்தது.",
    "Fundamental Rights and Duties are complementary and supplementary.", "அடிப்படை உரிமைகளும் கடமைகளும் ஒன்றுக்கொன்று நிரப்பியானவை.",
    ["TNPSC Group 1 Pattern", "M. Laxmikanth"], "PYQ Pattern", "Understand", 45
))

# Q50 - PYQ Pattern -> D
questions.append(create_q(
    "FD_PYQ_050", "Medium", "Assertion & Reason",
    "Assertion (A): Part III (Fundamental Rights), Part IV (Directive Principles), and Part IVA (Fundamental Duties) form an integrated triad of Indian constitutional philosophy.\nReason (R): Part III guarantees individual liberties, Part IV outlines State social welfare goals, and Part IVA reminds citizens of their responsibility to sustain both liberty and welfare.",
    "கூற்று (A): பகுதி III (அடிப்படை உரிமைகள்), பகுதி IV (DPSP) மற்றும் பகுதி IVA (அடிப்படை கடமைகள்) ஆகியவை இந்திய அரசியலமைப்புத் தத்துவத்தின் ஒருங்கிணைந்த முக்கோணத்தை உருவாக்குகின்றன.\nகாரணம் (R): பகுதி III தனிநபர் சுதந்திரத்திற்கு உத்தரவாதம் அளிக்கிறது, பகுதி IV அரசின் சமூக நல இலக்குகளை கோடிட்டுக் காட்டுகிறது, பகுதி IVA சுதந்திரம் மற்றும் நலன் இரண்டையும் பேணுவதற்கான பொறுப்பைக் குடிமக்களுக்கு நினைவூட்டுகிறது.",
    "Part III (Fundamental Rights), Part IV (Directive Principles), and Part IVA (Fundamental Duties) form an integrated triad of Indian constitutional philosophy.",
    "பகுதி III (அடிப்படை உரிமைகள்), பகுதி IV (DPSP) மற்றும் பகுதி IVA (அடிப்படை கடமைகள்) ஆகியவை இந்திய அரசியலமைப்புத் தத்துவத்தின் ஒருங்கிணைந்த முக்கோணத்தை உருவாக்குகின்றன.",
    "Part III guarantees individual liberties, Part IV outlines State social welfare goals, and Part IVA reminds citizens of their responsibility to sustain both liberty and welfare.",
    "பகுதி III தனிநபர் சுதந்திரத்திற்கு உத்தரவாதம் அளிக்கிறது, பகுதி IV அரசின் சமூக நல இலக்குகளை கோடிட்டுக் காட்டுகிறது, பகுதி IVA சுதந்திரம் மற்றும் நலன் இரண்டையும் பேணுவதற்கான பொறுப்பைக் குடிமக்களுக்கு நினைவூட்டுகிறது.",
    "Both A and R are correct but R is NOT the correct explanation of A", "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல.",
    "A is correct but R is incorrect", "A சரி, ஆனால் R தவறு.",
    "A is incorrect but R is correct", "A தவறு, ஆனால் R சரி.",
    "Both A and R are correct and R is the correct explanation of A", "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்.",
    "D",
    "Both A and R are true, and R explains A. The three Parts represent Rights (Part III), State Duties (Part IV), and Citizen Duties (Part IVA).",
    "கூற்று A மற்றும் காரணம் R இரண்டும் சரி, மேலும் R என்பது A-விற்கு சரியான விளக்கம். மூன்று பகுதிகளும் உரிமைகள் (பகுதி III), அரசு கடமைகள் (பகுதி IV), குடிமகன் கடமைகள் (பகுதி IVA) ஆகியவற்றைப் பிரதிநிதித்துவப்படுத்துகின்றன.",
    "Both A and R are true, and R explains the constitutional philosophy.", "A மற்றும் R இரண்டும் சரி, மேலும் R அரசியலமைப்புத் தத்துவத்தை விளக்குகிறது.",
    "Reason explains Assertion directly.", "காரணம் கூற்றை நேரடியாக விளக்குகிறது.",
    "Reason is factually correct.", "காரணம் சரியானது.",
    "Assertion is factually true.", "கூற்று சரியானது.",
    "TNPSC Trap: Remember Part III is justiciable, whereas Part IV and Part IVA are non-justiciable.",
    "TNPSC பொறி: பகுதி III நீதிமன்றத்தால் அமல்படுத்தக் கூடியது, ஆனால் பகுதி IV மற்றும் பகுதி IVA அமல்படுத்தப்பட முடியாதவை என்பதை நினைவில் கொள்க.",
    "Triad concept reaffirmed by Supreme Court in several constitutional bench judgments.",
    "முக்கோணக் கோட்பாடு பல அரசியலமைப்பு அமர்வு தீர்ப்புகளில் உச்சநீதிமன்றத்தால் மீண்டும் உறுதிப்படுத்தப்பட்டது.",
    ["TNPSC Group 1 Pattern", "M. Laxmikanth"], "PYQ Pattern", "Analyze", 60
))

# Save to BOTH file paths to support all loader signatures
files = [
    "data/questions/polity/fundamental_duties_pyq.json",
    "data/questions/polity/fundamental_duties_pyq_practice.json"
]

for file_path in files:
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print(f"Successfully written {len(questions)} questions to {file_path}")

