import json
import os
import sys

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

# Helper to build a question with specified correct_answer position ('A', 'B', 'C', or 'D')
def create_q(
    q_id, difficulty, question_en, question_ta,
    events, seq_correct, seq_wrong_1, seq_wrong_2, seq_wrong_3,
    correct_pos,
    exp_en, exp_ta,
    wno_correct_en, wno_correct_ta,
    wno_w1_en, wno_w1_ta,
    wno_w2_en, wno_w2_ta,
    wno_w3_en, wno_w3_ta,
    tip_en, tip_ta,
    fact_en, fact_ta,
    bloom="Understand", time_sec=60, similarity="High"
):
    seqs = {
        "correct": seq_correct,
        "w1": seq_wrong_1,
        "w2": seq_wrong_2,
        "w3": seq_wrong_3
    }
    
    wnos = {
        "correct": {"en": f"Correct. {wno_correct_en}", "ta": f"சரி. {wno_correct_ta}"},
        "w1": {"en": f"Incorrect. {wno_w1_en}", "ta": f"தவறு. {wno_w1_ta}"},
        "w2": {"en": f"Incorrect. {wno_w2_en}", "ta": f"தவறு. {wno_w2_ta}"},
        "w3": {"en": f"Incorrect. {wno_w3_en}", "ta": f"தவறு. {wno_w3_ta}"}
    }
    
    # Assign positions
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
        seq_str = seqs[k]
        options.append({"id": p, "en": seq_str, "ta": seq_str})
        options_en.append(seq_str)
        options_ta.append(seq_str)
        why_not_others[p] = wnos[k]
        
    return {
        "id": q_id,
        "subject": "Polity",
        "topic": "Fundamental Duties",
        "difficulty": difficulty,
        "question_type": "Chronology",
        "question": {"en": question_en, "ta": question_ta},
        "events": events,
        "options": options,
        "correct_answer": correct_pos,
        "explanation": {"en": exp_en, "ta": exp_ta},
        "why_not_others": why_not_others,
        "tnpsc_tip": {"en": tip_en, "ta": tip_ta},
        "revision_fact": {"en": fact_en, "ta": fact_ta},
        "source_reference": ["M. Laxmikanth - Indian Polity", "NCERT", "Samacheer Kalvi"],
        "bloom_level": bloom,
        "estimated_time_sec": time_sec,
        "pyq_similarity": similarity,
        "tags": ["Polity", "Fundamental Duties", "Chronology"],
        "question_en": question_en,
        "question_ta": question_ta,
        "options_en": options_en,
        "options_ta": options_ta,
        "answer": correct_pos.lower(),
        "explanation_en": exp_en,
        "explanation_ta": exp_ta
    }

questions = []

# Target distribution: A: 6, B: 6, C: 6, D: 7
# Pattern: A, B, C, D, A, B, C, D, A, B, C, D, A, B, C, D, A, B, C, D, D, C, B, A, D

# Q1 - Easy -> A
questions.append(create_q(
    "FD_CHRONO_001", "Easy",
    "Arrange the following key milestones in the constitutional evolution of Fundamental Duties in India in correct chronological order (earliest to latest):\n\n1. Adoption of the Constitution of India without Fundamental Duties\n2. Appointment of the Swaran Singh Committee on Fundamental Duties\n3. Enactment of the 42nd Constitutional Amendment Act inserting Part IVA\n4. Enactment of the 86th Constitutional Amendment Act adding the 11th duty",
    "இந்தியாவில் அடிப்படை கடமைகளின் அரசியலமைப்பு வளர்ச்சியில் பின்வரும் முக்கிய மைல்கற்களைச் சரியான காலவரிசைப்படி (முந்தையது முதல் பிந்தையது வரை) வரிசைப்படுத்தவும்:\n\n1. அடிப்படை கடமைகள் ஏதுமின்றி இந்திய அரசியலமைப்பு ஏற்றுக்கொள்ளப்படுதல்\n2. அடிப்படை கடமைகள் தொடர்பான ஸ்வரன் சிங் குழு அமைக்கப்படுதல்\n3. பகுதி IVA-வை இணைத்து 42வது அரசியலமைப்பு திருத்தச் சட்டம் இயற்றப்படுதல்\n4. 11வது கடமையைச் சேர்த்து 86வது அரசியலமைப்பு திருத்தச் சட்டம் இயற்றப்படுதல்",
    [
        {"id": "1", "en": "Adoption of the Constitution of India without Fundamental Duties (1950)", "ta": "அடிப்படை கடமைகள் ஏதுமின்றி இந்திய அரசியலமைப்பு ஏற்றுக்கொள்ளப்படுதல் (1950)"},
        {"id": "2", "en": "Appointment of the Swaran Singh Committee on Fundamental Duties (1976)", "ta": "அடிப்படை கடமைகள் தொடர்பான ஸ்வரன் சிங் குழு அமைக்கப்படுதல் (1976)"},
        {"id": "3", "en": "Enactment of the 42nd Constitutional Amendment Act inserting Part IVA (1976)", "ta": "பகுதி IVA-வை இணைத்து 42வது அரசியலமைப்பு திருத்தச் சட்டம் இயற்றப்படுதல் (1976)"},
        {"id": "4", "en": "Enactment of the 86th Constitutional Amendment Act adding the 11th duty (2002)", "ta": "11வது கடமையைச் சேர்த்து 86வது அரசியலமைப்பு திருத்தச் சட்டம் இயற்றப்படுதல் (2002)"}
    ],
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "4 -> 3 -> 2 -> 1",
    "A",
    "Correct Chronological Sequence: 1. Adoption of Constitution (1950) -> 2. Swaran Singh Committee (1976) -> 3. 42nd CAA inserting Part IVA (1976) -> 4. 86th CAA adding 11th Duty (2002).",
    "சரியான காலவரிசை: 1. அரசியலமைப்பு ஏற்றுக்கொள்ளப்படுதல் (1950) -> 2. ஸ்வரன் சிங் குழு (1976) -> 3. 42வது திருத்தம் (1976) -> 4. 86வது திருத்தம் (2002).",
    "1950 -> 1976 (Committee) -> 1976 (42nd CAA) -> 2002 (86th CAA) represents the exact historical evolution of Part IVA.",
    "1950 -> 1976 (குழு) -> 1976 (42வது திருத்தம்) -> 2002 (86வது திருத்தம்) என்பது பகுதி IVA-ன் சரியான வரலாற்று வளர்ச்சியைக் குறிக்கிறது.",
    "The Constitution was adopted in 1950, long before the Swaran Singh Committee was set up in 1976.",
    "1976-ல் ஸ்வரன் சிங் குழு அமைப்பதற்கு நீண்ட காலத்திற்கு முன்பே 1950-ல் அரசியலமைப்பு ஏற்றுக்கொள்ளப்பட்டது.",
    "Swaran Singh Committee was appointed in early 1976 before the 42nd Amendment was enacted in late 1976.",
    "1976 பிற்பகுதியில் 42வது திருத்தம் இயற்றப்படுவதற்கு முன்பே 1976 முற்பகுதியில் ஸ்வரன் சிங் குழு அமைக்கப்பட்டது.",
    "This is the reverse chronological order.",
    "இது தலைகீழ் காலவரிசையாகும்.",
    "TNPSC Trap: Original Constitution of 1950 had NO Fundamental Duties. 10 duties were added by the 42nd CAA in 1976, and the 11th duty was added by the 86th CAA in 2002.",
    "TNPSC பொறி: 1950-ன் அசல் அரசியலமைப்பில் அடிப்படை கடமைகள் ஏதும் இல்லை. 1976-ன் 42வது திருத்தத்தால் 10 கடமைகளும், 2002-ன் 86வது திருத்தத்தால் 11வது கடமையும் சேர்க்கப்பட்டன.",
    "The idea of Fundamental Duties was borrowed from the Constitution of the erstwhile USSR.",
    "அடிப்படை கடமைகள் எனும் கருத்து முன்னாள் சோவியத் யூனியன் (USSR) அரசியலமைப்பிலிருந்து பெறப்பட்டது.",
    "Understand", 60, "High"
))

# Q2 - Medium -> B
questions.append(create_q(
    "FD_CHRONO_002", "Medium",
    "Arrange the following specific steps regarding the Swaran Singh Committee and the 42nd Amendment in correct chronological order:\n\n1. Appointment of Swaran Singh Committee by the Congress Party leadership\n2. Submission of the Swaran Singh Committee Report proposing 8 Fundamental Duties\n3. Introduction of the 42nd Constitutional Amendment Bill in Parliament\n4. Enforcement of Part IVA of the Constitution on 3rd January 1977",
    "ஸ்வரன் சிங் குழு மற்றும் 42வது திருத்தம் தொடர்பான பின்வரும் குறிப்பிட்ட படிகளைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:\n\n1. காங்கிரஸ் கட்சித் தலைமையால் ஸ்வரன் சிங் குழு நியமிக்கப்படுதல்\n2. 8 அடிப்படை கடமைகளைப் பரிந்துரைத்து ஸ்வரன் சிங் குழு அறிக்கை சமர்ப்பித்தல்\n3. நாடாளுமன்றத்தில் 42வது அரசியலமைப்பு திருத்த மசோதா அறிமுகப்படுத்தப்படுதல்\n4. 1977 ஜனவரி 3 அன்று அரசியலமைப்பின் பகுதி IVA அமலுக்கு வருதல்",
    [
        {"id": "1", "en": "Appointment of Swaran Singh Committee by the Congress Party leadership (Feb 1976)", "ta": "காங்கிரஸ் கட்சித் தலைமையால் ஸ்வரன் சிங் குழு நியமிக்கப்படுதல் (பிப்ரவரி 1976)"},
        {"id": "2", "en": "Submission of the Swaran Singh Committee Report proposing 8 Fundamental Duties (May 1976)", "ta": "8 அடிப்படை கடமைகளைப் பரிந்துரைத்து ஸ்வரன் சிங் குழு அறிக்கை சமர்ப்பித்தல் (மே 1976)"},
        {"id": "3", "en": "Introduction of the 42nd Constitutional Amendment Bill in Parliament (Sept 1976)", "ta": "நாடாளுமன்றத்தில் 42வது அரசியலமைப்பு திருத்த மசோதா அறிமுகப்படுத்தப்படுதல் (செப்டம்பர் 1976)"},
        {"id": "4", "en": "Enforcement of Part IVA of the Constitution on 3rd January 1977", "ta": "1977 ஜனவரி 3 அன்று அரசியலமைப்பின் பகுதி IVA அமலுக்கு வருதல்"}
    ],
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "3 -> 1 -> 2 -> 4",
    "B",
    "Correct Chronological Sequence: 1. Committee Appointment (Feb 1976) -> 2. Report Submission (May 1976) -> 3. Bill Introduced (Sept 1976) -> 4. Enforcement of Part IVA (3 Jan 1977).",
    "சரியான காலவரிசை: 1. குழு நியமனம் (பிப் 1976) -> 2. அறிக்கை சமர்ப்பிப்பு (மே 1976) -> 3. மசோதா அறிமுகம் (செப் 1976) -> 4. பகுதி IVA அமலாக்கம் (3 ஜனவரி 1977).",
    "Appointment (Feb 1976) -> Report (May 1976) -> Bill Introduced (Sept 1976) -> Enforced (3 Jan 1977).",
    "நியமனம் (பிப் 1976) -> அறிக்கை (மே 1976) -> மசோதா (செப் 1976) -> அமலாக்கம் (3 ஜனவரி 1977).",
    "The Swaran Singh Committee was appointed in Feb 1976 before it submitted its report in May 1976.",
    "1976 மே மாதம் அறிக்கை சமர்ப்பிப்பதற்கு முன்பே 1976 பிப்ரவரியில் ஸ்வரன் சிங் குழு நியமிக்கப்பட்டது.",
    "The committee submitted its report in May 1976 before the Amendment Bill was introduced in Parliament.",
    "நாடாளுமன்றத்தில் திருத்த மசோதா அறிமுகப்படுத்தப்படுவதற்கு முன்பே 1976 மே மாதம் குழு தனது அறிக்கையைச் சமர்ப்பித்தது.",
    "The Bill was introduced after the Swaran Singh Committee was appointed and had submitted its report.",
    "ஸ்வரன் சிங் குழு அமைக்கப்பட்டு அறிக்கை அளித்த பிறகே மசோதா அறிமுகப்படுத்தப்பட்டது.",
    "TNPSC Trap: Swaran Singh Committee recommended ONLY 8 duties, but Parliament incorporated 10 duties in the 42nd CAA, 1976.",
    "TNPSC பொறி: ஸ்வரன் சிங் குழு 8 கடமைகளை மட்டுமே பரிந்துரைத்தது, ஆனால் நாடாளுமன்றம் 1976-ன் 42வது திருத்தத்தில் 10 கடமைகளை இணைத்தது.",
    "Swaran Singh Committee recommended penalty/punishment for non-compliance with duties, but Parliament REJECTED this recommendation.",
    "கடமைகளைப் பின்பற்றாதவருக்குத் தண்டனை அல்லது அபராதம் விதிக்க ஸ்வரன் சிங் குழு பரிந்துரைத்தது, ஆனால் நாடாளுமன்றம் இப்பரிந்துரையை நிராகரித்தது.",
    "Apply", 60, "High"
))

# Q3 - Medium -> C
questions.append(create_q(
    "FD_CHRONO_003", "Medium",
    "Arrange the constitutional developments regarding education from DPSP to Fundamental Duty in Article 51A(k) in correct chronological order:\n\n1. Inclusion of Article 45 in Part IV directing free and compulsory education for children up to 14 years\n2. Supreme Court ruling in Unni Krishnan Case declaring education up to 14 years a Fundamental Right\n3. Insertion of Article 21A, Article 51A(k), and modification of Article 45 via 86th CAA\n4. Enactment of the Right of Children to Free and Compulsory Education (RTE) Act",
    "DPSP-லிருந்து உறுப்பு 51A(k)-ல் உள்ள அடிப்படை கடமை வரையிலான கல்வி பற்றிய அரசியலமைப்பு வளர்ச்சிகளைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:\n\n1. 14 வயது வரையிலான குழந்தைகளுக்கு இலவசக் கல்விக்கான வழிகாட்டுதலுடன் பகுதி IV-ல் உறுப்பு 45 சேர்க்கப்படுதல்\n2. 14 வயது வரையிலான கல்வி ஒரு அடிப்படை உரிமை என உன்னிகிருஷ்ணன் வழக்கில் உச்சநீதிமன்றம் தீர்ப்பளித்தல்\n3. 86வது திருத்தம் மூலம் உறுப்பு 21A, உறுப்பு 51A(k) சேர்க்கப்பட்டு உறுப்பு 45 மாற்றியமைக்கப்படுதல்\n4. இலவச மற்றும் கட்டாயக் கல்வி உரிமைச் சட்டம் (RTE) இயற்றப்படுதல்",
    [
        {"id": "1", "en": "Inclusion of Article 45 in Part IV directing free and compulsory education for children up to 14 years (1950)", "ta": "14 வயது வரையிலான குழந்தைகளுக்கு இலவசக் கல்விக்கான வழிகாட்டுதலுடன் பகுதி IV-ல் உறுப்பு 45 சேர்க்கப்படுதல் (1950)"},
        {"id": "2", "en": "Supreme Court ruling in Unni Krishnan Case declaring education up to 14 years a Fundamental Right (1993)", "ta": "14 வயது வரையிலான கல்வி ஒரு அடிப்படை உரிமை என உன்னிகிருஷ்ணன் வழக்கில் உச்சநீதிமன்றம் தீர்ப்பளித்தல் (1993)"},
        {"id": "3", "en": "Insertion of Article 21A, Article 51A(k), and modification of Article 45 via 86th CAA (2002)", "ta": "86வது திருத்தம் மூலம் உறுப்பு 21A, உறுப்பு 51A(k) சேர்க்கப்பட்டு உறுப்பு 45 மாற்றியமைக்கப்படுதல் (2002)"},
        {"id": "4", "en": "Enactment of the Right of Children to Free and Compulsory Education (RTE) Act (2009)", "ta": "இலவச மற்றும் கட்டாயக் கல்வி உரிமைச் சட்டம் (RTE) இயற்றப்படுதல் (2009)"}
    ],
    "1 -> 2 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "2 -> 1 -> 3 -> 4", "4 -> 3 -> 2 -> 1",
    "C",
    "Correct Chronological Sequence: 1. Article 45 (1950) -> 2. Unni Krishnan Case (1993) -> 3. 86th CAA adding Art 21A & Art 51A(k) (2002) -> 4. RTE Act (2009).",
    "சரியான காலவரிசை: 1. உறுப்பு 45 (1950) -> 2. உன்னிகிருஷ்ணன் வழக்கு (1993) -> 3. 86வது திருத்தம் (2002) -> 4. RTE சட்டம் (2009).",
    "1950 (Original Art 45) -> 1993 (Unni Krishnan) -> 2002 (86th CAA) -> 2009 (RTE Act).",
    "சரி. 1950 (அசல் உறுப்பு 45) -> 1993 (உன்னிகிருஷ்ணன்) -> 2002 (86வது திருத்தம்) -> 2009 (RTE சட்டம்).",
    "Unni Krishnan case was decided in 1993, prior to the 86th Amendment Act of 2002.",
    "2002-ன் 86வது திருத்தச் சட்டத்திற்கு முன்பே 1993-ல் உன்னிகிருஷ்ணன் வழக்கு தீர்ப்பளிக்கப்பட்டது.",
    "Article 45 was part of the original 1950 Constitution, long before the Unni Krishnan case in 1993.",
    "1993-ல் உன்னிகிருஷ்ணன் வழக்குகளுக்கு நீண்ட காலத்திற்கு முன்பே 1950 அசல் அரசியலமைப்பில் உறுப்பு 45 இருந்தது.",
    "This shows reverse order.",
    "இது தலைகீழ் வரிசையைக் காட்டுகிறது.",
    "TNPSC Trap: Article 21A places duty on the STATE, Article 45 places duty on the STATE for early childhood care (0-6 yrs), and Article 51A(k) places duty on PARENTS/GUARDIANS for children aged 6-14 yrs.",
    "TNPSC பொறி: உறுப்பு 21A அரசின் கடமை, உறுப்பு 45 குழந்தைப் பருவ பராமரிப்பிற்கான (0-6 வயது) அரசின் கடமை, உறுப்பு 51A(k) பெற்றோர்/பாதுகாவலரின் கடமையாகும் (6-14 வயது).",
    "The RTE Act of 2009 came into force on 1st April 2010.",
    "2009-ன் RTE சட்டம் 2010 ஏப்ரல் 1 அன்று அமலுக்கு வந்தது.",
    "Analyze", 60, "High"
))

# Q4 - Medium -> D
questions.append(create_q(
    "FD_CHRONO_004", "Medium",
    "Arrange the environmental protection legislation and constitutional amendments in correct chronological order:\n\n1. Wildlife Protection Act\n2. Water (Prevention and Control of Pollution) Act\n3. Insertion of Article 48A (DPSP) and Article 51A(g) (FD) via 42nd Amendment Act\n4. Environment (Protection) Act",
    "சுற்றுச்சூழல் பாதுகாப்புச் சட்டங்கள் மற்றும் அரசியலமைப்பு திருத்தங்களைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:\n\n1. வனவிலங்கு பாதுகாப்புச் சட்டம்\n2. நீர் (மாசு தடுப்பு மற்றும் கட்டுப்பாடு) சட்டம்\n3. 42வது திருத்தச் சட்டம் மூலம் உறுப்பு 48A (DPSP) மற்றும் உறுப்பு 51A(g) (FD) சேர்க்கப்படுதல்\n4. சுற்றுச்சூழல் (பாதுகாப்பு) சட்டம்",
    [
        {"id": "1", "en": "Wildlife Protection Act (1972)", "ta": "வனவிலங்கு பாதுகாப்புச் சட்டம் (1972)"},
        {"id": "2", "en": "Water (Prevention and Control of Pollution) Act (1974)", "ta": "நீர் (மாசு தடுப்பு மற்றும் கட்டுப்பாடு) சட்டம் (1974)"},
        {"id": "3", "en": "Insertion of Article 48A (DPSP) and Article 51A(g) (FD) via 42nd Amendment Act (1976)", "ta": "42வது திருத்தச் சட்டம் மூலம் உறுப்பு 48A (DPSP) மற்றும் உறுப்பு 51A(g) (FD) சேர்க்கப்படுதல் (1976)"},
        {"id": "4", "en": "Environment (Protection) Act (1986)", "ta": "சுற்றுச்சூழல் (பாதுகாப்பு) சட்டம் (1986)"}
    ],
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "3 -> 1 -> 2 -> 4",
    "D",
    "Correct Chronological Sequence: 1. Wildlife Protection Act (1972) -> 2. Water Pollution Act (1974) -> 3. 42nd CAA inserting Art 48A & 51A(g) (1976) -> 4. Environment Protection Act (1986).",
    "சரியான காலவரிசை: 1. வனவிலங்கு பாதுகாப்புச் சட்டம் (1972) -> 2. நீர் மாசு தடுப்புச் சட்டம் (1974) -> 3. 42வது திருத்தம் (1976) -> 4. சுற்றுச்சூழல் பாதுகாப்புச் சட்டம் (1986).",
    "1972 -> 1974 -> 1976 -> 1986 follows exact statutory and constitutional sequence.",
    "1972 -> 1974 -> 1976 -> 1986 என்பது சரியான சட்ட மற்றும் அரசியலமைப்பு காலவரிசையைப் பின்பற்றுகிறது.",
    "Wildlife Protection Act was passed in 1972, before Water Pollution Act in 1974.",
    "1974-ல் நீர் மாசு தடுப்புச் சட்டத்திற்கு முன்பே 1972-ல் வனவிலங்கு பாதுகாப்புச் சட்டம் இயற்றப்பட்டது.",
    "Water Pollution Act (1974) preceded the 42nd Amendment Act (1976).",
    "1976-ன் 42வது திருத்தச் சட்டத்திற்கு முன்பே நீர் மாசு தடுப்புச் சட்டம் (1974) வந்தது.",
    "The 42nd Amendment (1976) came after both Wildlife (1972) and Water (1974) Acts.",
    "வனவிலங்கு (1972) மற்றும் நீர் (1974) சட்டங்கள் இரண்டிற்கும் பிறகே 42வது திருத்தம் (1976) வந்தது.",
    "TNPSC Trap: Article 48A is a DPSP (duty of the State to protect environment), while Article 51A(g) is a Fundamental Duty (duty of every citizen to protect environment and show compassion to living creatures). Both were added by the 42nd Amendment in 1976.",
    "TNPSC பொறி: உறுப்பு 48A என்பது DPSP (சுற்றுச்சூழலைப் பாதுகாக்க அரசின் கடமை), உறுப்பு 51A(g) என்பது அடிப்படை கடமை (சுற்றுச்சூழலைப் பாதுகாக்கவும் உயிரினங்களிடம் கருணை காட்டவும் குடிமகனின் கடமை). இரண்டும் 1976-ல் 42வது திருத்தத்தால் சேர்க்கப்பட்டன.",
    "Article 51A(g) specifies protection of four natural environments: forests, lakes, rivers, and wildlife.",
    "உறுப்பு 51A(g) நான்கு இயற்கை சூழல்களைப் பாதுகாப்பதைக் குறிப்பிடுகிறது: காடுகள், ஏரிகள், ஆறுகள் மற்றும் வனவிலங்குகள்.",
    "Understand", 60, "High"
))

# Q5 - Medium -> B
questions.append(create_q(
    "FD_CHRONO_005", "Medium",
    "Arrange the following parliamentary statutes identified by the Verma Committee (1999) for enforcing Fundamental Duties in correct chronological order:\n\n1. Representation of the People Act\n2. Protection of Civil Rights Act (formerly Untouchability Offences Act)\n3. Prevention of Insults to National Honour Act\n4. Forest (Conservation) Act",
    "அடிப்படை கடமைகளை அமல்படுத்துவதற்காக வர்மா குழுவால் (1999) சுட்டிக்காட்டப்பட்ட பின்வரும் நாடாளுமன்றச் சட்டங்களைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:\n\n1. மக்கள் பிரதிநிதித்துவச் சட்டம்\n2. குடிமை உரிமைகள் பாதுகாப்புச் சட்டம் (முந்தைய தீண்டாமை குற்றங்கள் சட்டம்)\n3. தேசிய சின்னங்கள்/மதிப்பை அவமதிப்பதைத் தடுக்கும் சட்டம்\n4. வன (பாதுகாப்பு) சட்டம்",
    [
        {"id": "1", "en": "Representation of the People Act (1951)", "ta": "மக்கள் பிரதிநிதித்துவச் சட்டம் (1951)"},
        {"id": "2", "en": "Protection of Civil Rights Act (1955)", "ta": "குடிமை உரிமைகள் பாதுகாப்புச் சட்டம் (1955)"},
        {"id": "3", "en": "Prevention of Insults to National Honour Act (1971)", "ta": "தேசிய சின்னங்கள்/மதிப்பை அவமதிப்பதைத் தடுக்கும் சட்டம் (1971)"},
        {"id": "4", "en": "Forest (Conservation) Act (1980)", "ta": "வன (பாதுகாப்பு) சட்டம் (1980)"}
    ],
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "4 -> 3 -> 2 -> 1",
    "B",
    "Correct Chronological Sequence: 1. Representation of People Act (1951) -> 2. Protection of Civil Rights Act (1955) -> 3. Prevention of Insults to National Honour Act (1971) -> 4. Forest Conservation Act (1980).",
    "சரியான காலவரிசை: 1. மக்கள் பிரதிநிதித்துவச் சட்டம் (1951) -> 2. குடிமை உரிமைகள் பாதுகாப்புச் சட்டம் (1955) -> 3. தேசிய சின்னங்கள் அவமதிப்பு தடுப்புச் சட்டம் (1971) -> 4. வன பாதுகாப்புச் சட்டம் (1980).",
    "1951 -> 1955 -> 1971 -> 1980 represents the correct chronological order of statutes enforcing duties.",
    "1951 -> 1955 -> 1971 -> 1980 என்பது கடமைகளை அமல்படுத்தும் சட்டங்களின் சரியான காலவரிசையாகும்.",
    "Representation of the People Act was enacted in 1951, before the Protection of Civil Rights Act in 1955.",
    "1955-ன் குடிமை உரிமைகள் பாதுகாப்புச் சட்டத்திற்கு முன்பே 1951-ல் மக்கள் பிரதிநிதித்துவச் சட்டம் இயற்றப்பட்டது.",
    "Protection of Civil Rights Act (1955) was enacted prior to the Prevention of Insults to National Honour Act (1971).",
    "1971-ன் தேசிய சின்னங்கள் அவமதிப்பு தடுப்புச் சட்டத்திற்கு முன்பே 1955-ல் குடிமை உரிமைகள் பாதுகாப்புச் சட்டம் இயற்றப்பட்டது.",
    "This shows reverse order.",
    "இது தலைகீழ் வரிசையைக் காட்டுகிறது.",
    "TNPSC Trap: Verma Committee (1999) pointed out that Fundamental Duties are enforced by statutory provisions already present in various Parliamentary Acts.",
    "TNPSC பொறி: பல்வேறு நாடாளுமன்றச் சட்டங்களில் ஏற்கனவே உள்ள சட்ட விதிகளின் மூலமே அடிப்படை கடமைகள் அமல்படுத்தப்படுகின்றன என்று வர்மா குழு (1999) சுட்டிக்காட்டியது.",
    "The Verma Committee was appointed in 1998 and submitted its report in 1999.",
    "வர்மா குழு 1998-ல் அமைக்கப்பட்டு 1999-ல் தனது அறிக்கையைச் சமர்ப்பித்தது.",
    "Understand", 60, "High"
))

# Q6 - Hard -> A
questions.append(create_q(
    "FD_CHRONO_006", "Hard",
    "Arrange the following landmark Supreme Court judgments touching upon Article 51A and Fundamental Duties in correct chronological order:\n\n1. Bijoe Emmanuel v. State of Kerala (National Anthem & Article 51A(a))\n2. M.C. Mehta v. Union of India (Directive for environmental education under Art 51A(g))\n3. AIIMS Students Union v. AIIMS (Duties held as important as Rights under Art 51A(j))\n4. Animal Welfare Board of India v. A. Nagaraja (Animal welfare rights under Art 51A(g))",
    "உறுப்பு 51A மற்றும் அடிப்படை கடமைகள் தொடர்பான பின்வரும் முக்கிய உச்சநீதிமன்றத் தீர்ப்புகளைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:\n\n1. பிஜோய் இம்மானுவேல் எதிராக கேரள மாநிலம் (தேசிய கீதம் & உறுப்பு 51A(a))\n2. எம்.சி. மேத்தா எதிராக இந்திய யூனியன் (உறுப்பு 51A(g)-ன் கீழ் சுற்றுச்சூழல் கல்விக்கான வழிகாட்டுதல்)\n3. AIIMS மாணவர் சங்கம் எதிராக AIIMS (உறுப்பு 51A(j)-ன் கீழ் உரிமைகளைப் போன்றே கடமைகளும் முக்கியம்)\n4. இந்திய விலங்கு நல வாரியம் எதிராக ஏ. நாகராஜா (உறுப்பு 51A(g)-ன் கீழ் விலங்கு நல உரிமைகள்)",
    [
        {"id": "1", "en": "Bijoe Emmanuel v. State of Kerala (1986)", "ta": "பிஜோய் இம்மானுவேல் எதிராக கேரள மாநிலம் (1986)"},
        {"id": "2", "en": "M.C. Mehta v. Union of India (Environmental Education Case) (1998)", "ta": "எம்.சி. மேத்தா எதிராக இந்திய யூனியன் (சுற்றுச்சூழல் கல்வி வழக்கு) (1998)"},
        {"id": "3", "en": "AIIMS Students Union v. AIIMS (2002)", "ta": "AIIMS மாணவர் சங்கம் எதிராக AIIMS (2002)"},
        {"id": "4", "en": "Animal Welfare Board of India v. A. Nagaraja (2014)", "ta": "இந்திய விலங்கு நல வாரியம் எதிராக ஏ. நாகராஜா (2014)"}
    ],
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "3 -> 1 -> 2 -> 4",
    "A",
    "Correct Chronological Sequence: 1. Bijoe Emmanuel (1986) -> 2. M.C. Mehta (1998) -> 3. AIIMS Students Union (2002) -> 4. Animal Welfare Board / Nagaraja (2014).",
    "சரியான காலவரிசை: 1. பிஜோய் இம்மானுவேல் (1986) -> 2. எம்.சி. மேத்தா (1998) -> 3. AIIMS மாணவர் சங்கம் (2002) -> 4. விலங்கு நல வாரியம் / நாகராஜா (2014).",
    "1986 -> 1998 -> 2002 -> 2014 is the exact chronological order of landmark FD rulings.",
    "1986 -> 1998 -> 2002 -> 2014 என்பது அடிப்படை கடமைகள் தொடர்பான முக்கிய தீர்ப்புகளின் சரியான காலவரிசையாகும்.",
    "Bijoe Emmanuel was decided in 1986, prior to M.C. Mehta Environmental Education direction in 1998.",
    "1998-ல் எம்.சி. மேத்தா சுற்றுச்சூழல் கல்வி வழிகாட்டுதலுக்கு முன்பே 1986-ல் பிஜோய் இம்மானுவேல் வழக்கு தீர்ப்பளிக்கப்பட்டது.",
    "M.C. Mehta directive was in 1998, prior to AIIMS Students Union case in 2002.",
    "2002-ல் AIIMS மாணவர் சங்க வழக்கிற்கு முன்பே 1998-ல் எம்.சி. மேத்தா வழக்கு வந்தது.",
    "AIIMS Students Union (2002) was decided long after Bijoe Emmanuel (1986).",
    "பிஜோய் இம்மானுவேல் (1986) வழக்குகளுக்கு நீண்ட காலத்திற்கு பிறகே AIIMS மாணவர் சங்கம் (2002) வழக்கு வந்தது.",
    "TNPSC Trap: In Bijoe Emmanuel (1986), SC held that standing up respectfully during National Anthem satisfies Art 51A(a); singing is not compulsory if it conflicts with genuine religious beliefs.",
    "TNPSC பொறி: பிஜோய் இம்மானுவேல் (1986) வழக்கில், தேசிய கீதத்தின் போது மரியாதையுடன் எழுந்து நின்றாலே உறுப்பு 51A(a) நிறைவேறுகிறது; உண்மையான மத நம்பிக்கைகளுக்கு முரணாக இருந்தால் பாடுவது கட்டாயமில்லை என உச்சநீதிமன்றம் கூறியது.",
    "In AIIMS Students Union case (2002), SC held that Fundamental Duties cannot be ignored and are as important as Fundamental Rights.",
    "AIIMS மாணவர் சங்க வழக்கில் (2002), அடிப்படை கடமைகளைப் புறக்கணிக்க முடியாது என்றும் அவை அடிப்படை உரிமைகளைப் போலவே முக்கியமானவை என்றும் உச்சநீதிமன்றம் கூறியது.",
    "Analyze", 60, "High"
))

# Q7 - Medium -> C
questions.append(create_q(
    "FD_CHRONO_007", "Medium",
    "Arrange the following Constitutional Amendment Acts modifying or retaining Part IVA and related chapters in correct chronological order:\n\n1. 42nd Constitutional Amendment Act (Inserted Part IVA and 10 Fundamental Duties)\n2. 44th Constitutional Amendment Act (Retained Part IVA intact while repealing other Emergency provisions)\n3. 86th Constitutional Amendment Act (Added Article 51A(k) as the 11th Fundamental Duty)\n4. 97th Constitutional Amendment Act (Added Article 43B DPSP for Co-operative Societies)",
    "பகுதி IVA மற்றும் தொடர்புடைய அத்தியாயங்களை திருத்திய அல்லது தக்கவைத்த பின்வரும் அரசியலமைப்பு திருத்தச் சட்டங்களைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:\n\n1. 42வது அரசியலமைப்பு திருத்தச் சட்டம் (பகுதி IVA மற்றும் 10 அடிப்படை கடமைகளை இணைத்தது)\n2. 44வது அரசியலமைப்பு திருத்தச் சட்டம் (அவசரநிலை விதிகளை நீக்கியபோதும் பகுதி IVA-வை மாற்றாமல் தக்கவைத்தது)\n3. 86வது அரசியலமைப்பு திருத்தச் சட்டம் (11வது அடிப்படை கடமையாக உறுப்பு 51A(k)-வைச் சேர்த்தது)\n4. 97வது அரசியலமைப்பு திருத்தச் சட்டம் (கூட்டுறவு சங்கங்களுக்கான DPSP உறுப்பு 43B-ஐச் சேர்த்தது)",
    [
        {"id": "1", "en": "42nd Constitutional Amendment Act (1976)", "ta": "42வது அரசியலமைப்பு திருத்தச் சட்டம் (1976)"},
        {"id": "2", "en": "44th Constitutional Amendment Act (1978)", "ta": "44வது அரசியலமைப்பு திருத்தச் சட்டம் (1978)"},
        {"id": "3", "en": "86th Constitutional Amendment Act (2002)", "ta": "86வது அரசியலமைப்பு திருத்தச் சட்டம் (2002)"},
        {"id": "4", "en": "97th Constitutional Amendment Act (2011)", "ta": "97வது அரசியலமைப்பு திருத்தச் சட்டம் (2011)"}
    ],
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "4 -> 3 -> 2 -> 1",
    "C",
    "Correct Chronological Sequence: 1. 42nd CAA (1976) -> 2. 44th CAA (1978) -> 3. 86th CAA (2002) -> 4. 97th CAA (2011).",
    "சரியான காலவரிசை: 1. 42வது திருத்தம் (1976) -> 2. 44வது திருத்தம் (1978) -> 3. 86வது திருத்தம் (2002) -> 4. 97வது திருத்தம் (2011).",
    "1976 -> 1978 -> 2002 -> 2011 represents the exact sequence of Constitutional Amendments.",
    "சரி. 1976 -> 1978 -> 2002 -> 2011 என்பது அரசியலமைப்பு திருத்தங்களின் சரியான வரிசையாகும்.",
    "The 42nd CAA came in 1976, before the Janata government passed the 44th CAA in 1978.",
    "1978-ல் ஜனதா அரசு 44வது திருத்தத்தைக் கொண்டு வருவதற்கு முன்பே 1976-ல் 42வது திருத்தம் வந்தது.",
    "44th CAA was enacted in 1978, long before the 86th CAA in 2002.",
    "2002-ன் 86வது திருத்தத்திற்கு நீண்ட காலத்திற்கு முன்பே 1978-ல் 44வது திருத்தம் இயற்றப்பட்டது.",
    "This shows reverse chronological order.",
    "இது தலைகீழ் காலவரிசையைக் காட்டுகிறது.",
    "TNPSC Trap: Although the 44th CAA (1978) reversed many distortions of the 42nd CAA, it did NOT abolish or alter Part IVA (Fundamental Duties).",
    "TNPSC பொறி: 44வது திருத்தம் (1978) 42வது திருத்தத்தின் பல மாற்றங்களை ரத்து செய்தபோதிலும், பகுதி IVA (அடிப்படை கடமைகள்) பகுதியை நீக்கவோ மாற்றவோ இல்லை.",
    "The 97th CAA of 2011 added Article 43B (DPSP) for promotion of cooperative societies.",
    "2011-ன் 97வது திருத்தம் கூட்டுறவு சங்கங்களை ஊக்குவிப்பதற்காக உறுப்பு 43B (DPSP)-ஐச் சேர்த்தது.",
    "Understand", 60, "High"
))

# Q8 - Hard -> D
questions.append(create_q(
    "FD_CHRONO_008", "Hard",
    "Arrange the following committees, commissions, and judicial guidelines related to Fundamental Duties in correct chronological order:\n\n1. Swaran Singh Committee Report\n2. Justice Verma Committee Report on Operationalisation of Fundamental Duties\n3. National Commission to Review the Working of the Constitution (NCRWC / Venkatachaliah Commission) Report\n4. Supreme Court Guidelines in In Re Destruction of Public Property case",
    "அடிப்படை கடமைகள் தொடர்பான பின்வரும் குழுக்கள், ஆணையங்கள் மற்றும் நீதித்துறை வழிகாட்டுதல்களைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:\n\n1. ஸ்வரன் சிங் குழு அறிக்கை\n2. அடிப்படை கடமைகளை அமல்படுத்துவது பற்றிய நீதியரசர் வர்மா குழு அறிக்கை\n3. அரசியலமைப்பு செயல்பாட்டை மறுஆய்வு செய்வதற்கான தேசிய ஆணையத்தின் (NCRWC / வெங்கடாசலய்யா ஆணையம்) அறிக்கை\n4. பொதுச் சொத்து சேத வழக்கிற்கான உச்சநீதிமன்ற வழிகாட்டுதல்கள்",
    [
        {"id": "1", "en": "Swaran Singh Committee Report (1976)", "ta": "ஸ்வரன் சிங் குழு அறிக்கை (1976)"},
        {"id": "2", "en": "Justice Verma Committee Report on Operationalisation of Fundamental Duties (1999)", "ta": "அடிப்படை கடமைகளை அமல்படுத்துவது பற்றிய நீதியரசர் வர்மா குழு அறிக்கை (1999)"},
        {"id": "3", "en": "National Commission to Review the Working of the Constitution (NCRWC) Report (2002)", "ta": "அரசியலமைப்பு செயல்பாட்டை மறுஆய்வு செய்வதற்கான தேசிய ஆணையத்தின் அறிக்கை (2002)"},
        {"id": "4", "en": "Supreme Court Guidelines in In Re Destruction of Public Property case (2009)", "ta": "பொதுச் சொத்து சேத வழக்கிற்கான உச்சநீதிமன்ற வழிகாட்டுதல்கள் (2009)"}
    ],
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "4 -> 3 -> 2 -> 1",
    "D",
    "Correct Chronological Sequence: 1. Swaran Singh Committee (1976) -> 2. Verma Committee (1999) -> 3. NCRWC Report (2002) -> 4. In Re Destruction of Public Property Guidelines (2009).",
    "சரியான காலவரிசை: 1. ஸ்வரன் சிங் குழு (1976) -> 2. வர்மா குழு (1999) -> 3. NCRWC அறிக்கை (2002) -> 4. பொதுச் சொத்து சேத வழிகாட்டுதல்கள் (2009).",
    "1976 -> 1999 -> 2002 -> 2009 represents the exact historical progression.",
    "சரி. 1976 -> 1999 -> 2002 -> 2009 என்பது சரியான வரலாற்று முன்னேற்றத்தைக் குறிக்கிறது.",
    "Swaran Singh Committee was in 1976, long before the Justice Verma Committee was constituted in 1998.",
    "1998-ல் நீதியரசர் வர்மா குழு அமைப்பதற்கு நீண்ட காலத்திற்கு முன்பே 1976-ல் ஸ்வரன் சிங் குழு இருந்தது.",
    "Verma Committee submitted its report in 1999, prior to the NCRWC Report in 2002.",
    "2002-ல் NCRWC அறிக்கைக்கு முன்பே 1999-ல் வர்மா குழு தனது அறிக்கையைச் சமர்ப்பித்தது.",
    "This represents reverse order.",
    "இது தலைகீழ் வரிசையைக் காட்டுகிறது.",
    "TNPSC Trap: NCRWC (headed by M.N. Venkatachaliah) recommended adding duty to vote, duty to pay taxes, and duty to foster family values, but these were NOT added to Article 51A.",
    "TNPSC பொறி: வாக்களிக்கும் கடமை, வரி செலுத்தும் கடமை மற்றும் குடும்ப மதிப்பைப் பேணும் கடமைகளைச் சேர்க்க NCRWC பரிந்துரைத்தது, ஆனால் இவை உறுப்பு 51A-ல் சேர்க்கப்படவில்லை.",
    "In Re Destruction of Public Property (2009), Supreme Court issued guidelines enforcing Article 51A(i) (duty to safeguard public property).",
    "பொதுச் சொத்து சேத வழக்கில் (2009), உறுப்பு 51A(i) (பொதுச் சொத்தைப் பாதுகாக்கும் கடமை)-ஐ அமல்படுத்த உச்சநீதிமன்றம் வழிகாட்டுதல்களை வெளியிட்டது.",
    "Analyze", 60, "High"
))

# Q9 - Easy -> A
questions.append(create_q(
    "FD_CHRONO_009", "Easy",
    "Arrange the first four Fundamental Duties as enumerated in Article 51A of the Constitution in correct sequential order (from clause (a) to clause (d)):\n\n1. To abide by the Constitution and respect its ideals, National Flag and National Anthem\n2. To cherish and follow the noble ideals that inspired the national struggle for freedom\n3. To uphold and protect the sovereignty, unity and integrity of India\n4. To defend the country and render national service when called upon to do so",
    "அரசியலமைப்பின் உறுப்பு 51A-ல் குறிப்பிடப்பட்டுள்ள முதல் நான்கு அடிப்படை கடமைகளை உட்பிரிவு (a) முதல் (d) வரையிலான சரியான வரிசையில் வரிசைப்படுத்தவும்:\n\n1. அரசியலமைப்பிற்கு கீழ்ப்படிந்து அதன் லட்சியங்கள், தேசியக் கொடி மற்றும் தேசிய கீதத்தை மதித்தல்\n2. சுதந்திரப் போராட்டத்திற்கு ஊக்கமளித்த உயரிய லட்சியங்களைப் பேணிப் பின்பற்றுதல்\n3. இந்தியாவின் இறையாண்மை, ஒற்றுமை மற்றும் ஒருமைப்பாட்டைப் பேணிப் பாதுகாத்தல்\n4. தேசத்தைப் பாதுகாத்தல் மற்றும் தேவைப்படும்போது தேசிய சேவையாற்றுதல்",
    [
        {"id": "1", "en": "Article 51A(a): Abide by Constitution, respect Flag & Anthem", "ta": "உறுப்பு 51A(a): அரசியலமைப்பிற்கு கீழ்ப்படிதல், கொடி & கீதத்தை மதித்தல்"},
        {"id": "2", "en": "Article 51A(b): Cherish noble ideals of freedom struggle", "ta": "உறுப்பு 51A(b): சுதந்திரப் போராட்ட லட்சியங்களைப் பேணுதல்"},
        {"id": "3", "en": "Article 51A(c): Uphold sovereignty, unity and integrity", "ta": "உறுப்பு 51A(c): இறையாண்மை, ஒற்றுமை & ஒருமைப்பாட்டைப் பாதுகாத்தல்"},
        {"id": "4", "en": "Article 51A(d): Defend country and render national service", "ta": "உறுப்பு 51A(d): தேசத்தைப் பாதுகாத்தல் & தேசிய சேவையாற்றுதல்"}
    ],
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "3 -> 2 -> 1 -> 4",
    "A",
    "Correct Constitutional Sequential Order: 1. Clause (a) -> 2. Clause (b) -> 3. Clause (c) -> 4. Clause (d).",
    "சரியான அரசியலமைப்பு வரிசை: 1. உட்பிரிவு (a) -> 2. உட்பிரிவு (b) -> 3. உட்பிரிவு (c) -> 4. உட்பிரிவு (d).",
    "Clause (a), (b), (c), and (d) follow the exact alphabetical order in Article 51A.",
    "உட்பிரிவுகள் (a), (b), (c), மற்றும் (d) ஆகியவை உறுப்பு 51A-ல் உள்ளவாறே அமைத்துள்ளன.",
    "Clause (a) comes before clause (b).",
    "உட்பிரிவு (b)-க்கு முன்பே உட்பிரிவு (a) வருகிறது.",
    "Clause (b) [Freedom struggle ideals] comes before clause (c) [Sovereignty].",
    "உட்பிரிவு (c) [இறையாண்மை]-க்கு முன்பே உட்பிரிவு (b) [சுதந்திரப் போராட்ட லட்சியங்கள்] வருகிறது.",
    "Clause (c) is the third duty, not the first.",
    "உட்பிரிவு (c) என்பது மூன்றாவது கடமையாகும், முதலாவது அல்ல.",
    "TNPSC Trap: Memory Trick for 51A(a) to (d): (a)=Anthem/Flag, (b)=Background/Ideals of Freedom, (c)=Country Sovereignty/Integrity, (d)=Defense of nation.",
    "TNPSC பொறி: 51A(a) முதல் (d) வரையிலான நினைவு உத்தி: (a)=தேசிய கீதம்/கொடி, (b)=சுதந்திரப் போராட்ட லட்சியங்கள், (c)=இறையாண்மை/ஒருமைப்பாடு, (d)=தேசப் பாதுகாப்பு.",
    "Sovereignty, Unity, and Integrity in 51A(c) mirror the words added to the Preamble by the 42nd Amendment.",
    "51A(c)-ல் உள்ள இறையாண்மை, ஒற்றுமை மற்றும் ஒருமைப்பாடு ஆகியவை 42வது திருத்தத்தால் முகப்புரையில் சேர்க்கப்பட்ட சொற்களை ஒத்துள்ளன.",
    "Remember", 60, "High"
))

# Q10 - Medium -> B
questions.append(create_q(
    "FD_CHRONO_010", "Medium",
    "Arrange the following events relating to Fundamental Duties in REVERSE chronological order (LATEST to EARLIEST):\n\n1. Coming into force of the Right to Education (RTE) Act\n2. Enactment of the 86th Constitutional Amendment Act\n3. Insertion of Part IVA into the Constitution by 42nd CAA\n4. Swaran Singh Committee constituted by Congress Party",
    "அடிப்படை கடமைகள் தொடர்பான பின்வரும் நிகழ்வுகளைத் தலைகீழ் காலவரிசைப்படி (பிந்தையது முதல் முந்தையது வரை) வரிசைப்படுத்தவும்:\n\n1. இலவசக் கல்வி உரிமைச் சட்டம் (RTE) அமலுக்கு வருதல்\n2. 86வது அரசியலமைப்பு திருத்தச் சட்டம் இயற்றப்படுதல்\n3. 42வது திருத்தம் மூலம் அரசியலமைப்பில் பகுதி IVA சேர்க்கப்படுதல்\n4. காங்கிரஸ் கட்சியால் ஸ்வரன் சிங் குழு அமைக்கப்படுதல்",
    [
        {"id": "1", "en": "Coming into force of the Right to Education (RTE) Act (2010)", "ta": "இலவசக் கல்வி உரிமைச் சட்டம் (RTE) அமலுக்கு வருதல் (2010)"},
        {"id": "2", "en": "Enactment of the 86th Constitutional Amendment Act (2002)", "ta": "86வது அரசியலமைப்பு திருத்தச் சட்டம் இயற்றப்படுதல் (2002)"},
        {"id": "3", "en": "Insertion of Part IVA into the Constitution by 42nd CAA (1976)", "ta": "42வது திருத்தம் மூலம் அரசியலமைப்பில் பகுதி IVA சேர்க்கப்படுதல் (1976)"},
        {"id": "4", "en": "Swaran Singh Committee constituted by Congress Party (Feb 1976)", "ta": "காங்கிரஸ் கட்சியால் ஸ்வரன் சிங் குழு அமைக்கப்படுதல் (பிப்ரவரி 1976)"}
    ],
    "1 -> 2 -> 3 -> 4", "4 -> 3 -> 2 -> 1", "1 -> 3 -> 2 -> 4", "2 -> 1 -> 4 -> 3",
    "B",
    "Correct Reverse Chronological Sequence (Latest to Earliest): 1. RTE Act in force (2010) -> 2. 86th CAA (2002) -> 3. 42nd CAA (Late 1976) -> 4. Swaran Singh Committee (Feb 1976).",
    "சரியான தலைகீழ் காலவரிசை (பிந்தையது முதல் முந்தையது வரை): 1. RTE சட்டம் அமலாக்கம் (2010) -> 2. 86வது திருத்தம் (2002) -> 3. 42வது திருத்தம் (1976 பிற்பகுதி) -> 4. ஸ்வரன் சிங் குழு (1976 பிப்ரவரி).",
    "2010 -> 2002 -> 1976 (42nd CAA) -> 1976 (Swaran Singh) represents the exact latest-to-earliest sequence.",
    "சரி. 2010 -> 2002 -> 1976 (42வது திருத்தம்) -> 1976 (ஸ்வரன் சிங்) என்பது சரியான பிந்தையது முதல் முந்தையது வரையிலான வரிசையாகும்.",
    "This is the forward chronological order (earliest to latest).",
    "தவறு. இது சாதாரண காலவரிசையாகும் (முந்தையது முதல் பிந்தையது வரை).",
    "42nd CAA (1976) came before 86th CAA (2002), so in reverse order 2002 must precede 1976.",
    "தவறு. தலைகீழ் வரிசையில் 1976-க்கு முன்னே 2002 வர வேண்டும்.",
    "RTE Act coming into force in 2010 is the latest event, so it must be first in reverse order.",
    "தவறு. 2010-ல் RTE சட்டம் அமலுக்கு வந்தது மிகச் சமீபத்திய நிகழ்வு என்பதால் அதுவே முதலில் வர வேண்டும்.",
    "TNPSC Trap: Pay close attention to question instructions! When asked for REVERSE chronological order, arrange from latest year to earliest year.",
    "TNPSC பொறி: வினாவின் வழிமுறைகளைக் கவனமாகப் படிக்கவும்! தலைகீழ் காலவரிசை என்று கேட்கப்பட்டால், சமீபத்திய ஆண்டிலிருந்து முந்தைய ஆண்டு வரை வரிசைப்படுத்தவும்.",
    "RTE Act was enacted by Parliament in August 2009 and came into effect on April 1, 2010.",
    "RTE சட்டம் நாடாளுமன்றத்தால் 2009 ஆகஸ்டில் இயற்றப்பட்டு 2010 ஏப்ரல் 1 அன்று அமலுக்கு வந்தது.",
    "Analyze", 60, "High"
))

# Q11 - Hard -> C
questions.append(create_q(
    "FD_CHRONO_011", "Hard",
    "Arrange the following environmental jurisprudence milestones connecting Fundamental Rights, DPSPs, and Fundamental Duties in correct chronological order:\n\n1. UN Conference on the Human Environment at Stockholm\n2. Constitutional insertion of Article 48A and Article 51A(g) via 42nd CAA\n3. Supreme Court ruling in M.C. Mehta v. Union of India (Ganga Pollution Case)\n4. Supreme Court ruling in Vellore Citizens Welfare Forum v. Union of India (Precautionary Principle)",
    "அடிப்படை உரிமைகள், DPSP மற்றும் அடிப்படை கடமைகளை இணைக்கும் சுற்றுச்சூழல் சட்டவியல் மைல்கற்களைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:\n\n1. ஸ்டாக்ஹோமில் நடைபெற்ற மனித சுற்றுச்சூழல் பற்றிய ஐ.நா மாநாடு\n2. 42வது திருத்தம் மூலம் உறுப்பு 48A மற்றும் உறுப்பு 51A(g) அரசியலமைப்பில் சேர்க்கப்படுதல்\n3. எம்.சி. மேத்தா எதிராக இந்திய யூனியன் (கங்கை மாசு வழக்கு) உச்சநீதிமன்றத் தீர்ப்பு\n4. வேலூர் குடிமக்கள் நல மன்றம் எதிராக இந்திய யூனியன் (முன்னெச்சரிக்கைக் கோட்பாடு) உச்சநீதிமன்றத் தீர்ப்பு",
    [
        {"id": "1", "en": "UN Conference on the Human Environment at Stockholm (1972)", "ta": "ஸ்டாக்ஹோமில் நடைபெற்ற மனித சுற்றுச்சூழல் பற்றிய ஐ.நா மாநாடு (1972)"},
        {"id": "2", "en": "Constitutional insertion of Article 48A and Article 51A(g) via 42nd CAA (1976)", "ta": "42வது திருத்தம் மூலம் உறுப்பு 48A மற்றும் உறுப்பு 51A(g) அரசியலமைப்பில் சேர்க்கப்படுதல் (1976)"},
        {"id": "3", "en": "Supreme Court ruling in M.C. Mehta v. Union of India (Ganga Pollution Case) (1987)", "ta": "எம்.சி. மேத்தா எதிராக இந்திய யூனியன் (கங்கை மாசு வழக்கு) உச்சநீதிமன்றத் தீர்ப்பு (1987)"},
        {"id": "4", "en": "Supreme Court ruling in Vellore Citizens Welfare Forum v. Union of India (1996)", "ta": "வேலூர் குடிமக்கள் நல மன்றம் எதிராக இந்திய யூனியன் உச்சநீதிமன்றத் தீர்ப்பு (1996)"}
    ],
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "3 -> 1 -> 2 -> 4",
    "C",
    "Correct Chronological Sequence: 1. Stockholm Conference (1972) -> 2. 42nd CAA (1976) -> 3. M.C. Mehta Ganga Case (1987) -> 4. Vellore Citizens Case (1996).",
    "சரியான காலவரிசை: 1. ஸ்டாக்ஹோம் மாநாடு (1972) -> 2. 42வது திருத்தம் (1976) -> 3. எம்.சி. மேத்தா கங்கை வழக்கு (1987) -> 4. வேலூர் குடிமக்கள் வழக்கு (1996).",
    "1972 (Stockholm) -> 1976 (42nd CAA) -> 1987 (M.C. Mehta) -> 1996 (Vellore Citizens) is the accurate timeline.",
    "சரி. 1972 (ஸ்டாக்ஹோம்) -> 1976 (42வது திருத்தம்) -> 1987 (எம்.சி. மேத்தா) -> 1996 (வேலூர் குடிமக்கள்) என்பது சரியான காலவரிசையாகும்.",
    "Stockholm Conference took place in June 1972, prior to the 42nd Amendment of 1976.",
    "1976-ன் 42வது திருத்தத்திற்கு முன்பே 1972 ஜூன் மாதத்தில் ஸ்டாக்ஹோம் மாநாடு நடைபெற்றது.",
    "42nd Amendment adding Art 51A(g) occurred in 1976, before the 1987 Ganga pollution judgment.",
    "1987 கங்கை மாசுத் தீர்ப்பிற்கு முன்பே 1976-ல் 51A(g) சேர்ந்த 42வது திருத்தம் நடந்தது.",
    "M.C. Mehta case (1987) was decided long after Stockholm Declaration (1972).",
    "ஸ்டாக்ஹோம் பிரகடனத்திற்கு (1972) நீண்ட காலத்திற்கு பிறகே எம்.சி. மேத்தா வழக்கு (1987) வந்தது.",
    "TNPSC Trap: The 1972 Stockholm Declaration inspired India to enact the 42nd CAA in 1976 incorporating Article 48A (DPSP) and Article 51A(g) (FD).",
    "TNPSC பொறி: 1972 ஸ்டாக்ஹோம் பிரகடனத்தின் தூண்டுதலால் தான் 1976-ல் 42வது திருத்தத்தின் மூலம் உறுப்பு 48A (DPSP) மற்றும் உறுப்பு 51A(g) (FD) இணைக்கப்பட்டன.",
    "In Vellore Citizens Welfare Forum (1996), Supreme Court integrated Precautionary Principle and Polluter Pays Principle into Indian environmental jurisprudence under Article 21 and Article 51A(g).",
    "வேலூர் குடிமக்கள் நல மன்ற வழக்கின் போது (1996), முன்னெச்சரிக்கைக் கோட்பாடு மற்றும் மாசுபடுத்துபவரே செலுத்தும் கோட்பாடு ஆகியவற்றை உறுப்பு 21 மற்றும் 51A(g)-ன் கீழ் நீதிமன்றம் இணைத்தது.",
    "Analyze", 60, "High"
))

# Q12 - Hard -> D
questions.append(create_q(
    "FD_CHRONO_012", "Hard",
    "Arrange the enactments and judicial precedents concerning National Symbols and National Honour (Article 51A(a)) in correct chronological order:\n\n1. Emblems and Names (Prevention of Improper Use) Act\n2. Prevention of Insults to National Honour Act\n3. Promulgation of the Flag Code of India, 2002\n4. Supreme Court ruling in Union of India v. Naveen Jindal",
    "தேசிய சின்னங்கள் மற்றும் தேசிய மரியாதை (உறுப்பு 51A(a)) பற்றிய சட்டங்கள் மற்றும் நீதித்துறை முன்மாதிரிகளைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:\n\n1. முத்திரைகள் மற்றும் பெயர்கள் (தவறான பயன்பாடு தடுப்பு) சட்டம்\n2. தேசிய சின்னங்கள்/மதிப்பை அவமதிப்பதைத் தடுக்கும் சட்டம்\n3. இந்திய தேசியக் கொடி விதித் தொகுப்பு, 2002 வெளியிடப்படுதல்\n4. இந்திய யூனியன் எதிராக நவீன் ஜிந்தால் வழக்கில் உச்சநீதிமன்றத் தீர்ப்பு",
    [
        {"id": "1", "en": "Emblems and Names (Prevention of Improper Use) Act (1950)", "ta": "முத்திரைகள் மற்றும் பெயர்கள் (தவறான பயன்பாடு தடுப்பு) சட்டம் (1950)"},
        {"id": "2", "en": "Prevention of Insults to National Honour Act (1971)", "ta": "தேசிய சின்னங்கள்/மதிப்பை அவமதிப்பதைத் தடுக்கும் சட்டம் (1971)"},
        {"id": "3", "en": "Promulgation of the Flag Code of India (2002)", "ta": "இந்திய தேசியக் கொடி விதித் தொகுப்பு வெளியிடப்படுதல் (2002)"},
        {"id": "4", "en": "Supreme Court ruling in Union of India v. Naveen Jindal (2004)", "ta": "இந்திய யூனியன் எதிராக நவீன் ஜிந்தால் வழக்கில் உச்சநீதிமன்றத் தீர்ப்பு (2004)"}
    ],
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "4 -> 3 -> 2 -> 1",
    "D",
    "Correct Chronological Sequence: 1. Emblems and Names Act (1950) -> 2. Prevention of Insults Act (1971) -> 3. Flag Code of India (2002) -> 4. Naveen Jindal Judgment (2004).",
    "சரியான காலவரிசை: 1. முத்திரைகள் மற்றும் பெயர்கள் சட்டம் (1950) -> 2. தேசிய சின்னங்கள் அவமதிப்பு தடுப்புச் சட்டம் (1971) -> 3. தேசியக் கொடி விதித் தொகுப்பு (2002) -> 4. நவீன் ஜிந்தால் தீர்ப்பு (2004).",
    "1950 -> 1971 -> 2002 -> 2004 is the exact chronological timeline of statutes and case law.",
    "சரி. 1950 -> 1971 -> 2002 -> 2004 என்பது சட்டங்கள் மற்றும் வழக்கின் சரியான காலவரிசையாகும்.",
    "Emblems and Names Act was passed in 1950, long before the 1971 Prevention of Insults to National Honour Act.",
    "1971-ன் தேசிய சின்னங்கள் அவமதிப்பு தடுப்புச் சட்டத்திற்கு நீண்ட காலத்திற்கு முன்பே 1950-ல் முத்திரைகள் சட்டம் வந்தது.",
    "1971 Act preceded the Flag Code of India (2002).",
    "2002-ன் தேசியக் கொடி விதித் தொகுப்பிற்கு முன்பே 1971 சட்டம் இயற்றப்பட்டது.",
    "This represents reverse order.",
    "இது தலைகீழ் வரிசையைக் காட்டுகிறது.",
    "TNPSC Trap: In Naveen Jindal case (2004), SC held that flying the National Flag respectfully is a Fundamental Right under Art 19(1)(a), but bounded by the duty under Art 51A(a).",
    "TNPSC பொறி: நவீன் ஜிந்தால் வழக்கில் (2004), தேசியக் கொடியை மரியாதையுடன் ஏற்றுவது உறுப்பு 19(1)(a)-ன் கீழ் அடிப்படை உரிமை என்றும், அது உறுப்பு 51A(a) கடமைக்கு உட்பட்டது என்றும் உச்சநீதிமன்றம் தீர்ப்பளித்தது.",
    "Flag Code of India was modified with effect from 26th January 2002.",
    "இந்திய தேசியக் கொடி விதித் தொகுப்பு 2002 ஜனவரி 26 முதல் திருத்தப்பட்டு அமலுக்கு வந்தது.",
    "Understand", 60, "High"
))

# Q13 - Easy -> A
questions.append(create_q(
    "FD_CHRONO_013", "Easy",
    "Arrange the second group of Fundamental Duties as listed in Article 51A in correct sequential order (from clause (e) to clause (h)):\n\n1. To promote harmony and the spirit of common brotherhood and renounce practices derogatory to the dignity of women\n2. To value and preserve the rich heritage of our composite culture\n3. To protect and improve the natural environment including forests, lakes, rivers and wildlife\n4. To develop the scientific temper, humanism and the spirit of inquiry and reform",
    "உறுப்பு 51A-ல் குறிப்பிடப்பட்டுள்ள இரண்டாவது தொகுதி அடிப்படை கடமைகளை உட்பிரிவு (e) முதல் (h) வரையிலான சரியான வரிசையில் வரிசைப்படுத்தவும்:\n\n1. நல்லிணக்கம் மற்றும் பொதுச் சகோதரத்துவத்தை வளர்த்தல், பெண்களின் கண்ணியத்தைக் குறைக்கும் வழக்கங்களைக் கைவிடுதல்\n2. நமது கூட்டுப் பண்பாட்டின் வளமான பாரம்பரியத்தைப் போற்றிப் பேணுதல்\n3. காடுகள், ஏரிகள், ஆறுகள் மற்றும் வனவிலங்குகள் உள்ளிட்ட இயற்கைச் சூழலைப் பாதுகாத்து மேம்படுத்துதல்\n4. அறிவியல் மனப்பான்மை, மனிதநேயம் மற்றும் ஆராய்ச்சி, சீர்திருத்த உணர்வை வளர்த்தல்",
    [
        {"id": "1", "en": "Article 51A(e): Harmony, brotherhood, dignity of women", "ta": "உறுப்பு 51A(e): நல்லிணக்கம், சகோதரத்துவம், பெண்கள் கண்ணியம்"},
        {"id": "2", "en": "Article 51A(f): Preserve rich heritage of composite culture", "ta": "உறுப்பு 51A(f): கூட்டுப் பண்பாட்டின் பாரம்பரியத்தைப் பேணுதல்"},
        {"id": "3", "en": "Article 51A(g): Protect natural environment & compassion for living creatures", "ta": "உறுப்பு 51A(g): இயற்கைச் சூழல் பாதுகாப்பு & உயிரினங்களிடம் கருணை"},
        {"id": "4", "en": "Article 51A(h): Scientific temper, humanism, inquiry and reform", "ta": "உறுப்பு 51A(h): அறிவியல் மனப்பான்மை, மனிதநேயம், ஆராய்ச்சி & சீர்திருத்தம்"}
    ],
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "3 -> 2 -> 1 -> 4",
    "A",
    "Correct Constitutional Sequential Order: 1. Clause (e) -> 2. Clause (f) -> 3. Clause (g) -> 4. Clause (h).",
    "சரியான அரசியலமைப்பு வரிசை: 1. உட்பிரிவு (e) -> 2. உட்பிரிவு (f) -> 3. உட்பிரிவு (g) -> 4. உட்பிரிவு (h).",
    "Clause (e), (f), (g), (h) follow alphabetical sub-clause order in Article 51A.",
    "உட்பிரிவுகள் (e), (f), (g), (h) ஆகியவை உறுப்பு 51A-ன் அகரவரிசையைப் பின்பற்றுகின்றன.",
    "Clause (e) [Brotherhood & Women's dignity] comes before clause (f) [Composite culture].",
    "உட்பிரிவு (f) [கூட்டுப் பண்பாடு]-க்கு முன்பே உட்பிரிவு (e) [சகோதரத்துவம் & பெண்கள் கண்ணியம்] வருகிறது.",
    "Clause (f) [Culture] comes before clause (g) [Environment].",
    "உட்பிரிவு (g) [சுற்றுச்சூழல்]-க்கு முன்பே உட்பிரிவு (f) [பண்பாடு] வருகிறது.",
    "Clause (g) is the 7th duty, not the 5th.",
    "உட்பிரிவு (g) என்பது 7வது கடமையாகும், 5வது அல்ல.",
    "TNPSC Trap: Clause (e) contains TWO parts: 1. Promoting harmony & common brotherhood, 2. Renouncing practices derogatory to the dignity of women.",
    "TNPSC பொறி: உட்பிரிவு (e) இரண்டு பகுதிகளைக் கொண்டுள்ளது: 1. நல்லிணக்கம் மற்றும் பொதுச் சகோதரத்துவத்தை வளர்த்தல், 2. பெண்களின் கண்ணியத்தைக் குறைக்கும் வழக்கங்களைக் கைவிடுதல்.",
    "Article 51A(h) is unique in mentioning 'scientific temper, humanism and the spirit of inquiry and reform' as a constitutional duty.",
    "அறிவியல் மனப்பான்மை, மனிதநேயம் மற்றும் ஆராய்ச்சி, சீர்திருத்த உணர்வை ஒரு அரசியலமைப்பு கடமையாக உறுப்பு 51A(h) தனித்துவமாகக் குறிப்பிடுகிறது.",
    "Remember", 60, "High"
))

# Q14 - Hard -> B
questions.append(create_q(
    "FD_CHRONO_014", "Hard",
    "Arrange the judicial expansion of the Right to Education leading up to the 86th Constitutional Amendment Act in correct chronological order:\n\n1. Original DPSP Article 45 enacted directing state to provide free and compulsory education within 10 years\n2. Mohini Jain v. State of Karnataka (Capitation Fee Case linking education to Right to Life under Art 21)\n3. Unni Krishnan v. State of Andhra Pradesh (Restricting Right to Free Education up to 14 years of age)\n4. Enactment of 86th CAA introducing Article 21A, Article 51A(k) and modifying Article 45",
    "86வது அரசியலமைப்பு திருத்தச் சட்டத்திற்கு வழிவகுத்த கல்வி உரிமையின் நீதித்துறை விரிவாக்கங்களைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:\n\n1. 10 ஆண்டுகளுக்குள் அரசு இலவசக் கல்வி அளிக்க வேண்டும் என வழிகாட்டும் அசல் DPSP உறுப்பு 45 இயற்றப்படுதல்\n2. மோகினி ஜெயின் எதிராக கர்நாடக மாநில வழக்கு (உறுப்பு 21-ன் வாழ்வுரிமையுடன் கல்வியை இணைக்கும் தலைக்கட்டு கட்டண வழக்கு)\n3. உன்னிகிருஷ்ணன் எதிராக ஆந்திரப் பிரதேச மாநில வழக்கு (இலவசக் கல்வி உரிமையை 14 வயது வரை மட்டுமே எல்லைப்படுத்துதல்)\n4. 86வது திருத்தம் மூலம் உறுப்பு 21A, உறுப்பு 51A(k) சேர்க்கப்பட்டு உறுப்பு 45 திருத்தப்படுதல்",
    [
        {"id": "1", "en": "Original Article 45 enacted (1950)", "ta": "அசல் உறுப்பு 45 இயற்றப்படுதல் (1950)"},
        {"id": "2", "en": "Mohini Jain v. State of Karnataka (Capitation Fee Case) (1992)", "ta": "மோகினி ஜெயின் எதிராக கர்நாடக மாநில வழக்கு (1992)"},
        {"id": "3", "en": "Unni Krishnan v. State of Andhra Pradesh (1993)", "ta": "உன்னிகிருஷ்ணன் எதிராக ஆந்திரப் பிரதேச மாநில வழக்கு (1993)"},
        {"id": "4", "en": "86th Constitutional Amendment Act enacted (2002)", "ta": "86வது அரசியலமைப்பு திருத்தச் சட்டம் இயற்றப்படுதல் (2002)"}
    ],
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "4 -> 3 -> 2 -> 1",
    "B",
    "Correct Chronological Sequence: 1. Article 45 (1950) -> 2. Mohini Jain Case (1992) -> 3. Unni Krishnan Case (1993) -> 4. 86th CAA (2002).",
    "சரியான காலவரிசை: 1. உறுப்பு 45 (1950) -> 2. மோகினி ஜெயின் வழக்கு (1992) -> 3. உன்னிகிருஷ்ணன் வழக்கு (1993) -> 4. 86வது திருத்தம் (2002).",
    "1950 -> 1992 -> 1993 -> 2002 represents the exact legal progression of education jurisprudence.",
    "சரி. 1950 -> 1992 -> 1993 -> 2002 என்பது கல்விச் சட்டவியலின் சரியான வளர்ச்சிப் பாதையாகும்.",
    "Article 45 was in the 1950 Constitution, long before Mohini Jain in 1992.",
    "தவறு. 1992 மோகினி ஜெயின் வழக்கிற்கு நீண்ட காலத்திற்கு முன்பே 1950 அரசியலமைப்பில் உறுப்பு 45 இருந்தது.",
    "Mohini Jain (1992) preceded Unni Krishnan (1993).",
    "தவறு. உன்னிகிருஷ்ணன் (1993) வழக்கிற்கு முன்பே மோகினி ஜெயின் (1992) வழக்கு வந்தது.",
    "This displays reverse chronological sequence.",
    "தவறு. இது தலைகீழ் காலவரிசையைக் காட்டுகிறது.",
    "TNPSC Trap: Mohini Jain (1992) declared right to education at all levels as a FR under Art 21; Unni Krishnan (1993) limited this FR to children up to 14 years. This was later formalized by the 86th CAA in 2002.",
    "TNPSC பொறி: மோகினி ஜெயின் (1992) அனைத்து நிலைக் கல்வியையும் உறுப்பு 21-ன் கீழ் அடிப்படை உரிமை என்றது; உன்னிகிருஷ்ணன் (1993) இதை 14 வயது வரை என வரைமுறைப்படுத்தியது. இதுவே 2002-ன் 86வது திருத்தமாக உருவெடுத்தது.",
    "The 86th CAA created a tripartite synthesis: Art 21A (FR - State obligation), Art 45 (DPSP - 0 to 6 yrs care), Art 51A(k) (FD - Parent duty for 6 to 14 yrs).",
    "86வது திருத்தம் முத்தரப்புத் தொகுப்பை உருவாக்கியது: உறுப்பு 21A (FR - அரசின் கடமை), உறுப்பு 45 (DPSP - 0-6 வயது பராமரிப்பு), உறுப்பு 51A(k) (FD - 6-14 வயது வரை பெற்றோரின் கடமை).",
    "Analyze", 60, "High"
))

# Q15 - Medium -> C
questions.append(create_q(
    "FD_CHRONO_015", "Medium",
    "Arrange the following timeline of Constitutional Amendments that impacted Parts III, IV, and IVA of the Indian Constitution in correct chronological order:\n\n1. 42nd CAA (Added Part IVA Fundamental Duties)\n2. 44th CAA (Added Article 38(2) DPSP and modified Article 31)\n3. 86th CAA (Added Article 21A FR, Article 51A(k) FD, amended Article 45 DPSP)\n4. 97th CAA (Added Article 19(1)(c) Right to form Co-operatives, Article 43B DPSP)",
    "இந்திய அரசியலமைப்பின் பகுதிகள் III, IV மற்றும் IVA ஆகியவற்றை பாதித்த அரசியலமைப்பு திருத்தங்களின் காலவரிசையைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:\n\n1. 42வது திருத்தம் (பகுதி IVA அடிப்படை கடமைகளைச் சேர்த்தது)\n2. 44வது திருத்தம் (உறுப்பு 38(2) DPSP-ஐச் சேர்த்து உறுப்பு 31-ஐ திருத்தியது)\n3. 86வது திருத்தம் (உறுப்பு 21A FR, உறுப்பு 51A(k) FD சேர்த்து, உறுப்பு 45 DPSP-ஐத் திருத்தியது)\n4. 97வது திருத்தம் (உறுப்பு 19(1)(c) கூட்டுறவு அமைக்கும் உரிமை, உறுப்பு 43B DPSP-ஐச் சேர்த்தது)",
    [
        {"id": "1", "en": "42nd Constitutional Amendment Act (1976)", "ta": "42வது அரசியலமைப்பு திருத்தச் சட்டம் (1976)"},
        {"id": "2", "en": "44th Constitutional Amendment Act (1978)", "ta": "44வது அரசியலமைப்பு திருத்தச் சட்டம் (1978)"},
        {"id": "3", "en": "86th Constitutional Amendment Act (2002)", "ta": "86வது அரசியலமைப்பு திருத்தச் சட்டம் (2002)"},
        {"id": "4", "en": "97th Constitutional Amendment Act (2011)", "ta": "97வது அரசியலமைப்பு திருத்தச் சட்டம் (2011)"}
    ],
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "3 -> 2 -> 1 -> 4",
    "C",
    "Correct Chronological Sequence: 1. 42nd CAA (1976) -> 2. 44th CAA (1978) -> 3. 86th CAA (2002) -> 4. 97th CAA (2011).",
    "சரியான காலவரிசை: 1. 42வது திருத்தம் (1976) -> 2. 44வது திருத்தம் (1978) -> 3. 86வது திருத்தம் (2002) -> 4. 97வது திருத்தம் (2011).",
    "1976 -> 1978 -> 2002 -> 2011 represents the exact chronological sequence.",
    "சரி. 1976 -> 1978 -> 2002 -> 2011 என்பது சரியான அரசியலமைப்பு திருத்தங்களின் வரிசையாகும்.",
    "42nd CAA was enacted in 1976, prior to 44th CAA in 1978.",
    "தவறு. 1978-ன் 44வது திருத்தத்திற்கு முன்பே 1976-ல் 42வது திருத்தம் இயற்றப்பட்டது.",
    "44th CAA was passed in 1978, long before 86th CAA in 2002.",
    "தவறு. 2002-ன் 86வது திருத்தத்திற்கு நீண்ட காலத்திற்கு முன்பே 1978-ல் 44வது திருத்தம் வந்தது.",
    "86th CAA (2002) was enacted after both 42nd (1976) and 44th (1978) amendments.",
    "தவறு. 42 (1976) மற்றும் 44 (1978) ஆகிய இரு திருத்தங்களுக்கும் பிறகே 86வது திருத்தம் (2002) வந்தது.",
    "TNPSC Trap: Remember that 42nd CAA (1976) added Part IVA (10 duties), while 86th CAA (2002) added the 11th duty [Art 51A(k)].",
    "TNPSC பொறி: 42வது திருத்தம் (1976) பகுதி IVA-ஐ (10 கடமைகள்) சேர்த்தது, 86வது திருத்தம் (2002) 11வது கடமையைச் [உறுப்பு 51A(k)] சேர்த்தது என்பதை நினைவில் கொள்க.",
    "The 97th CAA of 2011 added Part IXB for Co-operative Societies.",
    "2011-ன் 97வது திருத்தம் கூட்டுறவு சங்கங்களுக்காக பகுதி IXB-ஐச் சேர்த்தது.",
    "Understand", 60, "High"
))

# Q16 - Hard -> D
questions.append(create_q(
    "FD_CHRONO_016", "Hard",
    "Arrange the following judicial decisions where courts used Article 51A to interpret reasonableness of restrictions on Fundamental Rights under Article 19 in correct chronological order:\n\n1. Bijoe Emmanuel v. State of Kerala (Freedom of speech & Article 51A(a))\n2. Aruna Roy v. Union of India (Value education & Article 51A(e)/(f))\n3. State of Gujarat v. Mirzapur Moti Koreshi Kassab Jamat (Cow slaughter ban justified under Art 51A(g))\n4. In Re Destruction of Public Property (Guidelines under Art 51A(i))",
    "உறுப்பு 19-ன் கீழ் அடிப்படை உரிமைகள் மீதான கட்டுப்பாடுகளின் நியாயத் தன்மையை விளக்குவதற்கு நீதிமன்றங்கள் உறுப்பு 51A-ஐப் பயன்படுத்திய பின்வரும் தீர்ப்புகளைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:\n\n1. பிஜோய் இம்மானுவேல் எதிராக கேரள மாநிலம் (பேச்சுரிமை & உறுப்பு 51A(a))\n2. அருணா ராய் எதிராக இந்திய யூனியன் (மதிப்புக் கல்வி & உறுப்பு 51A(e)/(f))\n3. குஜராத் மாநிலம் எதிராக மிர்சாபூர் மோதி கொரேஷி கசாப் ஜமாத் (உறுப்பு 51A(g)-ன் கீழ் பசு வதைத் தடை நியாயப்படுத்தப்பட்டது)\n4. பொதுச் சொத்து சேத வழக்கு (உறுப்பு 51A(i)-ன் கீழ் வழிகாட்டுதல்கள்)",
    [
        {"id": "1", "en": "Bijoe Emmanuel v. State of Kerala (1986)", "ta": "பிஜோய் இம்மானுவேல் எதிராக கேரள மாநிலம் (1986)"},
        {"id": "2", "en": "Aruna Roy v. Union of India (2002)", "ta": "அருணா ராய் எதிராக இந்திய யூனியன் (2002)"},
        {"id": "3", "en": "State of Gujarat v. Mirzapur Moti Koreshi Kassab Jamat (2005)", "ta": "குஜராத் மாநிலம் எதிராக மிர்சாபூர் மோதி கொரேஷி கசாப் ஜமாத் (2005)"},
        {"id": "4", "en": "In Re Destruction of Public Property (2009)", "ta": "பொதுச் சொத்து சேத வழக்கு (2009)"}
    ],
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "3 -> 1 -> 2 -> 4",
    "D",
    "Correct Chronological Sequence: 1. Bijoe Emmanuel (1986) -> 2. Aruna Roy (2002) -> 3. Mirzapur Moti Koreshi (2005) -> 4. In Re Destruction of Public Property (2009).",
    "சரியான காலவரிசை: 1. பிஜோய் இம்மானுவேல் (1986) -> 2. அருணா ராய் (2002) -> 3. மிர்சாபூர் மோதி கொரேஷி (2005) -> 4. பொதுச் சொத்து சேத வழக்கு (2009).",
    "1986 -> 2002 -> 2005 -> 2009 is the exact chronological sequence of judicial precedents.",
    "சரி. 1986 -> 2002 -> 2005 -> 2009 என்பது நீதிமன்ற முன்மாதிரிகளின் சரியான காலவரிசையாகும்.",
    "Bijoe Emmanuel judgment was delivered in 1986, prior to Aruna Roy in 2002.",
    "தவறு. 2002-ன் அருணா ராய் வழக்கிற்கு முன்பே 1986-ல் பிஜோய் இம்மானுவேல் தீர்ப்பு அளிக்கப்பட்டது.",
    "Aruna Roy (2002) preceded the Mirzapur Moti Koreshi judgment in 2005.",
    "தவறு. 2005-ன் மிர்சாபூர் மோதி கொரேஷி தீர்ப்பிற்கு முன்பே அருணா ராய் (2002) வழக்கு வந்தது.",
    "Mirzapur Moti Koreshi (2005) was decided long after Bijoe Emmanuel (1986).",
    "தவறு. பிஜோய் இம்மானுவேல் (1986) வழக்கிற்கு நீண்ட காலத்திற்கு பிறகே மிர்சாபூர் மோதி கொரேஷி (2005) வழக்கு வந்தது.",
    "TNPSC Trap: In Mirzapur Moti Koreshi (2005), a 7-judge Constitution Bench held that restrictions placed on FRs to give effect to FD under Art 51A(g) are reasonable under Art 19.",
    "TNPSC பொறி: மிர்சாபூர் மோதி கொரேஷி (2005) வழக்கில், உறுப்பு 51A(g) கடமையை நிறைவேற்ற அடிப்படை உரிமைகள் மீது விதிக்கப்படும் கட்டுப்பாடுகள் உறுப்பு 19-ன் கீழ் நியாயமானவை என 7 நீதிபதிகள் கொண்ட அமர்வு தீர்ப்பளித்தது.",
    "In Aruna Roy case (2002), SC upheld value education based on all religions citing Art 51A(e).",
    "அருணா ராய் வழக்கில் (2002), உறுப்பு 51A(e)-ஐ மேற்கோள் காட்டி அனைத்து மதங்கள் சார்ந்த மதிப்புக் கல்வியை உச்சநீதிமன்றம் உறுதி செய்தது.",
    "Analyze", 60, "High"
))

# Q17 - Easy -> A
questions.append(create_q(
    "FD_CHRONO_017", "Easy",
    "Arrange the final group of Fundamental Duties as listed in Article 51A in correct sequential order (from clause (h) to clause (k)):\n\n1. To develop scientific temper, humanism and the spirit of inquiry and reform\n2. To safeguard public property and to abjure violence\n3. To strive towards excellence in all spheres of individual and collective activity\n4. To provide opportunities for education to child/ward between 6 and 14 years by parent/guardian",
    "உறுப்பு 51A-ல் குறிப்பிடப்பட்டுள்ள இறுதித் தொகுதி அடிப்படை கடமைகளை உட்பிரிவு (h) முதல் (k) வரையிலான சரியான வரிசையில் வரிசைப்படுத்தவும்:\n\n1. அறிவியல் மனப்பான்மை, மனிதநேயம் மற்றும் ஆராய்ச்சி, சீர்திருத்த உணர்வை வளர்த்தல்\n2. பொதுச் சொத்தைப் பாதுகாத்தல் மற்றும் வன்முறையைக் கைவிடுதல்\n3. தனிநபர் மற்றும் கூட்டுச் செயல்பாடுகளின் அனைத்துத் துறைகளிலும் சிறப்பினை நோக்கி முயலுதல்\n4. 6 முதல் 14 வயது வரையிலான குழந்தைகள்/வார்டுகளுக்குக் கல்விக்கான வாய்ப்புகளைப் பெற்றோர்/பாதுகாவலர் வழங்குதல்",
    [
        {"id": "1", "en": "Article 51A(h): Scientific temper, humanism, inquiry and reform", "ta": "உறுப்பு 51A(h): அறிவியல் மனப்பான்மை, மனிதநேயம், ஆராய்ச்சி & சீர்திருத்தம்"},
        {"id": "2", "en": "Article 51A(i): Safeguard public property and abjure violence", "ta": "உறுப்பு 51A(i): பொதுச் சொத்தைப் பாதுகாத்தல் & வன்முறையைக் கைவிடுதல்"},
        {"id": "3", "en": "Article 51A(j): Strive towards excellence in individual and collective activity", "ta": "உறுப்பு 51A(j): தனிநபர் & கூட்டுச் செயல்பாடுகளில் சிறப்பினை நோக்கி முயலுதல்"},
        {"id": "4", "en": "Article 51A(k): Provide education opportunities (added by 86th CAA)", "ta": "உறுப்பு 51A(k): கல்விக் வாய்ப்புகளை வழங்குதல் (86வது திருத்தத்தால் சேர்க்கப்பட்டது)"}
    ],
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "4 -> 3 -> 2 -> 1",
    "A",
    "Correct Constitutional Sequential Order: 1. Clause (h) -> 2. Clause (i) -> 3. Clause (j) -> 4. Clause (k).",
    "சரியான அரசியலமைப்பு வரிசை: 1. உட்பிரிவு (h) -> 2. உட்பிரிவு (i) -> 3. உட்பிரிவு (j) -> 4. உட்பிரிவு (k).",
    "Clauses (h), (i), (j), and (k) follow the exact alphabetical order in Article 51A.",
    "உட்பிரிவுகள் (h), (i), (j), மற்றும் (k) ஆகியவை உறுப்பு 51A-ல் உள்ளவாறே அமைத்துள்ளன.",
    "Clause (h) comes before clause (i).",
    "உட்பிரிவு (i)-க்கு முன்பே உட்பிரிவு (h) வருகிறது.",
    "Clause (i) [Public property] comes before clause (j) [Excellence].",
    "உட்பிரிவு (j) [சிறப்பினை நோக்கிய முயற்சி]-க்கு முன்பே உட்பிரிவு (i) [பொதுச் சொத்து] வருகிறது.",
    "This shows reverse order starting from the 11th duty.",
    "இது 11வது கடமையிலிருந்து தொடங்கும் தலைகீழ் வரிசையாகும்.",
    "TNPSC Trap: Article 51A(k) is the ONLY duty that was NOT added in 1976; it was inserted by the 86th CAA in 2002.",
    "TNPSC பொறி: உறுப்பு 51A(k) மட்டுமே 1976-ல் சேர்க்கப்படாத ஒரே கடமை; இது 2002-ன் 86வது திருத்தத்தால் சேர்க்கப்பட்டது.",
    "Article 51A(i) commands citizens to safeguard PUBLIC property and abjure violence.",
    "உறுப்பு 51A(i) குடிமக்களைப் பொதுச் சொத்தைப் பாதுகாக்கவும் வன்முறையைக் கைவிடவும் கட்டாயமாக்குகிறது.",
    "Remember", 60, "High"
))

# Q18 - Hard -> B
questions.append(create_q(
    "FD_CHRONO_018", "Hard",
    "Arrange the key procedural steps in the enactment and operationalization of the 86th Constitutional Amendment Act (Article 51A(k)) in correct chronological order:\n\n1. Submission of the 165th Law Commission Report recommending free compulsory education\n2. Passage of the 86th Constitutional Amendment Bill by both Houses of Parliament\n3. Presidential assent given to the 86th Constitutional Amendment Act\n4. Enforcement of the Right of Children to Free and Compulsory Education (RTE) Act",
    "86வது அரசியலமைப்பு திருத்தச் சட்டம் (உறுப்பு 51A(k)) இயற்றப்பட்டு அமல்படுத்தப்பட்டதன் முக்கிய நடைமுறைப் படிகளைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:\n\n1. இலவசக் கட்டாயக் கல்வியைப் பரிந்துரைத்து 165வது சட்ட ஆணைய அறிக்கை சமர்ப்பிக்கப்படுதல்\n2. நாடாளுமன்றத்தின் இரு அவைகளிலும் 86வது அரசியலமைப்பு திருத்த மசோதா நிறைவேற்றப்படுதல்\n3. 86வது அரசியலமைப்பு திருத்தச் சட்டத்திற்கு குடியரசுத் தலைவர் ஒப்புதல் அளித்தல்\n4. இலவச மற்றும் கட்டாயக் கல்வி உரிமைச் சட்டம் (RTE) அமலுக்கு வருதல்",
    [
        {"id": "1", "en": "165th Law Commission Report on Free and Compulsory Education (1998)", "ta": "இலவச மற்றும் கட்டாயக் கல்வி பற்றிய 165வது சட்ட ஆணைய அறிக்கை (1998)"},
        {"id": "2", "en": "Passage of 86th Constitutional Amendment Bill by Parliament (Dec 2002)", "ta": "நாடாளுமன்றத்தால் 86வது திருத்த மசோதா நிறைவேற்றப்படுதல் (டிசம்பர் 2002)"},
        {"id": "3", "en": "Presidential Assent to the 86th CAA (12th Dec 2002)", "ta": "86வது திருத்தச் சட்டத்திற்கு குடியரசுத் தலைவர் ஒப்புதல் அளித்தல் (12 டிசம்பர் 2002)"},
        {"id": "4", "en": "Enforcement of RTE Act on 1st April 2010", "ta": "2010 ஏப்ரல் 1 அன்று RTE சட்டம் அமலுக்கு வருதல்"}
    ],
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "3 -> 2 -> 1 -> 4",
    "B",
    "Correct Chronological Sequence: 1. Law Commission Report (1998) -> 2. Parliamentary Passage (Dec 2002) -> 3. Presidential Assent (Dec 2002) -> 4. RTE Act Enforcement (April 2010).",
    "சரியான காலவரிசை: 1. சட்ட ஆணைய அறிக்கை (1998) -> 2. நாடாளுமன்ற ஒப்புதல் (டிச 2002) -> 3. குடியரசுத் தலைவர் ஒப்புதல் (டிச 2002) -> 4. RTE சட்டம் அமலாக்கம் (ஏப்ரல் 2010).",
    "1998 (Law Commission) -> Dec 2002 (Parliament) -> Dec 2002 (Assent) -> April 2010 (RTE Enforcement) is the precise timeline.",
    "சரி. 1998 (சட்ட ஆணையம்) -> டிச 2002 (நாடாளுமன்றம்) -> டிச 2002 (ஒப்புதல்) -> ஏப்ரல் 2010 (RTE அமலாக்கம்) என்பது சரியான காலவரிசையாகும்.",
    "Law Commission 165th Report came out in 1998, prior to Parliamentary passage of the 86th Amendment Bill in Dec 2002.",
    "தவறு. 2002 டிசம்பரில் 86வது திருத்த மசோதா நிறைவேற்றப்படுவதற்கு முன்பே 1998-ல் 165வது சட்ட ஆணைய அறிக்கை வந்தது.",
    "Parliament passes a bill before the President gives assent.",
    "தவறு. குடியரசுத் தலைவர் ஒப்புதல் அளிப்பதற்கு முன்பே நாடாளுமன்றம் மசோதாவை நிறைவேற்றுகிறது.",
    "Presidential assent comes after passage by Parliament, not before.",
    "தவறு. குடியரசுத் தலைவர் ஒப்புதல் நாடாளுமன்ற நிறைவேற்றத்திற்குப் பிறகே வரும், முன்பல்ல.",
    "TNPSC Trap: 86th CAA was enacted in 2002, but its operational statutory enabling act (RTE Act) came into force on 1st April 2010.",
    "TNPSC பொறி: 86வது திருத்தம் 2002-ல் இயற்றப்பட்டது, ஆனால் அதை அமல்படுத்தும் சட்டப்பூர்வ சட்டம் (RTE சட்டம்) 2010 ஏப்ரல் 1 அன்றே அமலுக்கு வந்தது.",
    "165th Law Commission Report was titled 'Free and Compulsory Education for Children' (1998).",
    "165வது சட்ட ஆணைய அறிக்கை 'குழந்தைகளுக்கான இலவச மற்றும் கட்டாயக் கல்வி' (1998) என்ற தலைப்பைக் கொண்டிருந்தது.",
    "Analyze", 60, "High"
))

# Q19 - Medium -> C
questions.append(create_q(
    "FD_CHRONO_019", "Medium",
    "Arrange the steps from the origin of Swaran Singh Committee to 42nd CAA in REVERSE chronological order (LATEST to EARLIEST):\n\n1. Coming into force of Part IVA (3rd January 1977)\n2. Presidential Assent to the 42nd Amendment Act (18th December 1976)\n3. Submission of Swaran Singh Committee Report (May 1976)\n4. Formation of Swaran Singh Committee (February 1976)",
    "ஸ்வரன் சிங் குழுவின் தொடக்கம் முதல் 42வது திருத்தம் வரையிலான படிகளைத் தலைகீழ் காலவரிசைப்படி (பிந்தையது முதல் முந்தையது வரை) வரிசைப்படுத்தவும்:\n\n1. பகுதி IVA அமலுக்கு வருதல் (3 ஜனவரி 1977)\n2. 42வது திருத்தச் சட்டத்திற்கு குடியரசுத் தலைவர் ஒப்புதல் அளித்தல் (18 டிசம்பர் 1976)\n3. ஸ்வரன் சிங் குழு அறிக்கை சமர்ப்பித்தல் (மே 1976)\n4. ஸ்வரன் சிங் குழு உருவாக்கப்படுதல் (பிப்ரவரி 1976)",
    [
        {"id": "1", "en": "Coming into force of Part IVA (3rd January 1977)", "ta": "பகுதி IVA அமலுக்கு வருதல் (3 ஜனவரி 1977)"},
        {"id": "2", "en": "Presidential Assent to 42nd CAA (18th December 1976)", "ta": "42வது திருத்தச் சட்டத்திற்கு குடியரசுத் தலைவர் ஒப்புதல் அளித்தல் (18 டிசம்பர் 1976)"},
        {"id": "3", "en": "Submission of Swaran Singh Committee Report (May 1976)", "ta": "ஸ்வரன் சிங் குழு அறிக்கை சமர்ப்பித்தல் (மே 1976)"},
        {"id": "4", "en": "Formation of Swaran Singh Committee (February 1976)", "ta": "ஸ்வரன் சிங் குழு உருவாக்கப்படுதல் (பிப்ரவரி 1976)"}
    ],
    "1 -> 2 -> 3 -> 4", "4 -> 3 -> 2 -> 1", "1 -> 3 -> 2 -> 4", "2 -> 1 -> 4 -> 3",
    "C",
    "Correct Reverse Chronological Sequence: 1. Enforced (3 Jan 1977) -> 2. Presidential Assent (18 Dec 1976) -> 3. Report Submitted (May 1976) -> 4. Committee Formed (Feb 1976).",
    "சரியான தலைகீழ் காலவரிசை: 1. அமலாக்கம் (3 ஜனவரி 1977) -> 2. குடியரசுத் தலைவர் ஒப்புதல் (18 டிசம்பர் 1976) -> 3. அறிக்கை சமர்ப்பிப்பு (மே 1976) -> 4. குழு உருவாக்கம் (பிப்ரவரி 1976).",
    "Jan 1977 -> Dec 1976 -> May 1976 -> Feb 1976 represents the exact reverse sequence.",
    "சரி. ஜனவரி 1977 -> டிசம்பர் 1976 -> மே 1976 -> பிப்ரவரி 1976 என்பது சரியான தலைகீழ் வரிசையாகும்.",
    "This represents forward chronological order (earliest to latest).",
    "தவறு. இது சாதாரண காலவரிசையாகும் (முந்தையது முதல் பிந்தையது வரை).",
    "Presidential Assent (18 Dec 1976) came after Report Submission (May 1976), so in reverse order Assent must precede Report.",
    "தவறு. தலைகீழ் வரிசையில் 1976 மே அறிக்கைக்கு முன்பே 1976 டிசம்பர் ஒப்புதல் வர வேண்டும்.",
    "Coming into force on 3rd Jan 1977 is the latest event, so it must be first in reverse order.",
    "தவறு. 1977 ஜனவரி 3-ல் அமலுக்கு வந்தது மிகச் சமீபத்திய நிகழ்வு என்பதால் அதுவே முதலில் வர வேண்டும்.",
    "TNPSC Trap: January 3 is celebrated as 'Fundamental Duties Day' in India because Part IVA came into effect on 3rd January 1977.",
    "TNPSC பொறி: 1977 ஜனவரி 3 அன்று பகுதி IVA அமலுக்கு வந்ததால், இந்தியாவில் ஜனவரி 3 ஆம் தேதி 'அடிப்படை கடமைகள் நாளாகக்' கொண்டாடப்படுகிறது.",
    "The 42nd Amendment Act of 1976 is also known as the 'Mini-Constitution' due to its comprehensive changes.",
    "1976-ன் 42வது திருத்தச் சட்டம் அதன் விரிவான மாற்றங்கள் காரணமாக 'குறு அரசியலமைப்பு' என்றும் அழைக்கப்படுகிறது.",
    "Apply", 60, "High"
))

# Q20 - Medium -> D
questions.append(create_q(
    "FD_CHRONO_020", "Medium",
    "Arrange the following criminal and civil enactments related to national harmony and communal balance in correct chronological order:\n\n1. Indian Penal Code provisions penalizing offences against national integration (Section 153B)\n2. Representation of the People Act penalizing communal election appeals\n3. Protection of Civil Rights Act penalizing untouchability\n4. Unlawful Activities (Prevention) Act (UAPA)",
    "தேசிய நல்லிணக்கம் மற்றும் சமூகச் சமநிலை தொடர்பான பின்வரும் குற்றவியல் மற்றும் குடிமையியல் சட்டங்களைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:\n\n1. தேசிய ஒருமைப்பாட்டிற்கு எதிரான குற்றங்களைத் தண்டிக்கும் இந்திய தண்டனைச் சட்ட விதிகள் (பிரிவு 153B)\n2. வகுப்புவாத தேர்தல் பரப்புரைகளைத் தண்டிக்கும் மக்கள் பிரதிநிதித்துவச் சட்டம்\n3. தீண்டாமையைத் தண்டிக்கும் குடிமை உரிமைகள் பாதுகாப்புச் சட்டம்\n4. சட்டவிரோத நடவடிக்கைகள் தடுப்புச் சட்டம் (UAPA)",
    [
        {"id": "1", "en": "Indian Penal Code (1860)", "ta": "இந்திய தண்டனைச் சட்டம் (1860)"},
        {"id": "2", "en": "Representation of the People Act (1951)", "ta": "மக்கள் பிரதிநிதித்துவச் சட்டம் (1951)"},
        {"id": "3", "en": "Protection of Civil Rights Act (1955)", "ta": "குடிமை உரிமைகள் பாதுகாப்புச் சட்டம் (1955)"},
        {"id": "4", "en": "Unlawful Activities (Prevention) Act (1967)", "ta": "சட்டவிரோத நடவடிக்கைகள் தடுப்புச் சட்டம் (1967)"}
    ],
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "4 -> 3 -> 2 -> 1",
    "D",
    "Correct Chronological Sequence: 1. Indian Penal Code (1860) -> 2. Representation of the People Act (1951) -> 3. Protection of Civil Rights Act (1955) -> 4. UAPA (1967).",
    "சரியான காலவரிசை: 1. இந்திய தண்டனைச் சட்டம் (1860) -> 2. மக்கள் பிரதிநிதித்துவச் சட்டம் (1951) -> 3. குடிமை உரிமைகள் பாதுகாப்புச் சட்டம் (1955) -> 4. UAPA (1967).",
    "1860 -> 1951 -> 1955 -> 1967 represents the exact statutory sequence enforcing aspects of Art 51A(c) & (e).",
    "சரி. 1860 -> 1951 -> 1955 -> 1967 என்பது உறுப்புகள் 51A(c) & (e)-ஐ அமல்படுத்தும் சட்டங்களின் சரியான காலவரிசையாகும்.",
    "IPC was enacted in 1860 during British rule, long before RPA in 1951.",
    "தவறு. 1951-ன் மக்கள் பிரதிநிதித்துவச் சட்டத்திற்கு நீண்ட காலத்திற்கு முன்பே பிரிட்டிஷ் ஆட்சியில் 1860-ல் IPC இயற்றப்பட்டது.",
    "RPA (1951) was enacted before the Untouchability Offences / Civil Rights Act (1955).",
    "தவறு. 1955-ன் தீண்டாமை குற்றங்கள் / குடிமை உரிமைகள் சட்டத்திற்கு முன்பே மக்கள் பிரதிநிதித்துவச் சட்டம் (1951) வந்தது.",
    "This shows reverse chronological order.",
    "இது தலைகீழ் காலவரிசையைக் காட்டுகிறது.",
    "TNPSC Trap: IPC Sec 153B penalizes imputations prejudicial to national integration, directly enforcing Article 51A(c) (sovereignty, unity, integrity).",
    "TNPSC பொறி: IPC பிரிவு 153B தேசிய ஒருமைப்பாட்டிற்கு எதிரான குற்றங்களைத் தண்டிக்கிறது, இது உறுப்பு 51A(c) (இறையாண்மை, ஒற்றுமை, ஒருமைப்பாடு)-ஐ நேரடியாக அமல்படுத்துகிறது.",
    "The Untouchability Offences Act of 1955 was amended and renamed as the Protection of Civil Rights Act in 1976.",
    "1955-ன் தீண்டாமை குற்றங்கள் சட்டம் 1976-ல் திருத்தப்பட்டு குடிமை உரிமைகள் பாதுகாப்புச் சட்டம் எனப் பெயர் மாற்றப்பட்டது.",
    "Understand", 60, "High"
))

# Q21 - Easy -> D
questions.append(create_q(
    "FD_CHRONO_021", "Easy",
    "Arrange the growth of total number of Fundamental Duties in India from 0 to 11 in correct chronological sequence:\n\n1. Commencement of the Constitution with 0 Fundamental Duties\n2. Swaran Singh Committee recommendation to add 8 Fundamental Duties\n3. Enactment of 42nd Amendment Act introducing 10 Fundamental Duties\n4. Enactment of 86th Amendment Act adding the 11th Fundamental Duty",
    "இந்தியாவில் அடிப்படை கடமைகளின் மொத்த எண்ணிக்கை 0-லிருந்து 11 ஆகக் கூடிய வளர்ச்சியைக் காலவரிசைப்படி வரிசைப்படுத்தவும்:\n\n1. 0 அடிப்படை கடமைகளுடன் அரசியலமைப்பு அமலுக்கு வருதல்\n2. 8 அடிப்படை கடமைகளைச் சேர்க்க ஸ்வரன் சிங் குழு பரிந்துரைத்தல்\n3. 10 அடிப்படை கடமைகளை அறிமுகப்படுத்தி 42வது திருத்தச் சட்டம் இயற்றப்படுதல்\n4. 11வது அடிப்படை கடமையைச் சேர்த்து 86வது திருத்தச் சட்டம் இயற்றப்படுதல்",
    [
        {"id": "1", "en": "Commencement of Constitution with 0 Duties (26th Jan 1950)", "ta": "0 கடமைகளுடன் அரசியலமைப்பு அமலுக்கு வருதல் (26 ஜனவரி 1950)"},
        {"id": "2", "en": "Swaran Singh Committee recommending 8 Duties (May 1976)", "ta": "8 கடமைகளை ஸ்வரன் சிங் குழு பரிந்துரைத்தல் (மே 1976)"},
        {"id": "3", "en": "42nd CAA introducing 10 Duties (1976)", "ta": "42வது திருத்தம் 10 கடமைகளை அறிமுகப்படுத்துதல் (1976)"},
        {"id": "4", "en": "86th CAA adding 11th Duty (2002)", "ta": "86வது திருத்தம் 11வது கடமையைச் சேர்த்தல் (2002)"}
    ],
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "4 -> 3 -> 2 -> 1",
    "D",
    "Correct Chronological Sequence: 1. 0 Duties (1950) -> 2. 8 Duties proposed (May 1976) -> 3. 10 Duties enacted (Late 1976) -> 4. 11 Duties total (2002).",
    "சரியான காலவரிசை: 1. 0 கடமைகள் (1950) -> 2. 8 கடமைகள் பரிந்துரை (மே 1976) -> 3. 10 கடமைகள் சேர்க்கை (1976 பிற்பகுதி) -> 4. மொத்தம் 11 கடமைகள் (2002).",
    "1950 (0 duties) -> May 1976 (8 recommended) -> Late 1976 (10 enacted) -> 2002 (11th duty) is the exact numerical progression.",
    "சரி. 1950 (0 கடமைகள்) -> மே 1976 (8 பரிந்துரை) -> 1976 பிற்பகுதி (10 சேர்க்கை) -> 2002 (11வது கடமை) என்பது சரியான எண்ணிக்கைப் பாதையாகும்.",
    "The Constitution commenced in 1950 with 0 duties, before the Swaran Singh Committee was set up in 1976.",
    "தவறு. 1976-ல் ஸ்வரன் சிங் குழு அமைப்பதற்கு முன்பே 1950-ல் 0 கடமைகளுடன் அரசியலமைப்பு அமலுக்கு வந்தது.",
    "Swaran Singh Committee submitted its report in May 1976 before the 42nd Amendment was passed in late 1976.",
    "தவறு. 1976 பிற்பகுதியில் 42வது திருத்தம் நிறைவேற்றப்படுவதற்கு முன்பே 1976 மே மாதம் ஸ்வரன் சிங் குழு அறிக்கை அளித்தது.",
    "This represents reverse order.",
    "தவறு. இது தலைகீழ் வரிசையைக் காட்டுகிறது.",
    "TNPSC Trap: Swaran Singh recommended 8 duties, 42nd CAA enacted 10 duties, and 86th CAA added 1 duty to make the present total 11 duties.",
    "TNPSC பொறி: ஸ்வரன் சிங் 8 கடமைகளைப் பரிந்துரைத்தார், 42வது திருத்தம் 10 கடமைகளை இயற்றியது, 86வது திருத்தம் 1 கடமையைச் சேர்த்து தற்போது மொத்தம் 11 கடமைகள் உள்ளன.",
    "All 11 Fundamental Duties are listed in a single Article, Article 51A, in Part IVA.",
    "அனைத்து 11 அடிப்படை கடமைகளும் பகுதி IVA-ல் உள்ள ஒரே உறுப்பான உறுப்பு 51A-ல் பட்டியலிடப்பட்டுள்ளன.",
    "Understand", 60, "High"
))

# Q22 - Hard -> C
questions.append(create_q(
    "FD_CHRONO_022", "Hard",
    "Arrange the following environmental protection case precedents directly citing Article 51A(g) in correct chronological order:\n\n1. Sachidanand Pandey v. State of West Bengal (Duty of Court and Citizen to protect ecology)\n2. M.C. Mehta v. Union of India (Kanpur Tanneries Ganga Pollution Case)\n3. T.N. Godavarman Thirumulpad v. Union of India (Forest Conservation Case)\n4. Animal Welfare Board of India v. A. Nagaraja (Jallikattu & Animal Rights Case)",
    "உறுப்பு 51A(g)-ஐ நேரடியாக மேற்கோள் காட்டிய பின்வரும் சுற்றுச்சூழல் பாதுகாப்பு வழக்கு முன்மாதிரிகளைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:\n\n1. சச்சிதானந்த் பாண்டே எதிராக மேற்கு வங்க மாநிலம் (சுற்றுச்சூழலைப் பாதுகாப்பதில் நீதிமன்றம் மற்றும் குடிமகனின் கடமை)\n2. எம்.சி. மேத்தா எதிராக இந்திய யூனியன் (கான்பூர் தோல் பதனிடும் ஆலை கங்கை மாசு வழக்கு)\n3. டி.என். கோதாவர்மன் திருமுல்பாட் எதிராக இந்திய யூனியன் (வன பாதுகாப்பு வழக்கு)\n4. இந்திய விலங்கு நல வாரியம் எதிராக ஏ. நாகராஜா (ஜல்லிக்கட்டு & விலங்கு உரிமைகள் வழக்கு)",
    [
        {"id": "1", "en": "Sachidanand Pandey v. State of West Bengal (1987)", "ta": "சச்சிதானந்த் பாண்டே எதிராக மேற்கு வங்க மாநிலம் (1987)"},
        {"id": "2", "en": "M.C. Mehta v. Union of India (Kanpur Tanneries Case) (1987)", "ta": "எம்.சி. மேத்தா எதிராக இந்திய யூனியன் (கான்பூர் ஆலைகள் வழக்கு) (1987)"},
        {"id": "3", "en": "T.N. Godavarman Thirumulpad v. Union of India (1996)", "ta": "டி.என். கோதாவர்மன் திருமுல்பாட் எதிராக இந்திய யூனியன் (1996)"},
        {"id": "4", "en": "Animal Welfare Board of India v. A. Nagaraja (2014)", "ta": "இந்திய விலங்கு நல வாரியம் எதிராக ஏ. நாகராஜா (2014)"}
    ],
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "4 -> 3 -> 2 -> 1",
    "C",
    "Correct Chronological Sequence: 1. Sachidanand Pandey (Feb 1987) -> 2. M.C. Mehta Kanpur Tanneries (Sept 1987) -> 3. Godavarman Forest Case (1996) -> 4. Animal Welfare Board / Nagaraja (2014).",
    "சரியான காலவரிசை: 1. சச்சிதானந்த் பாண்டே (பிப் 1987) -> 2. எம்.சி. மேத்தா கான்பூர் வழக்கு (செப் 1987) -> 3. கோதாவர்மன் வன வழக்கு (1996) -> 4. விலங்கு நல வாரியம் / நாகராஜா (2014).",
    "Feb 1987 -> Sept 1987 -> 1996 -> 2014 is the accurate timeline of environmental rulings citing Art 51A(g).",
    "சரி. பிப் 1987 -> செப் 1987 -> 1996 -> 2014 என்பது உறுப்பு 51A(g)-ஐ மேற்கோள் காட்டிய தீர்ப்புகளின் சரியான வரிசையாகும்.",
    "Sachidanand Pandey was decided in Feb 1987, prior to Kanpur Tanneries judgment in Sept 1987.",
    "தவறு. 1987 செப்டம்பரில் கான்பூர் தோல் ஆலைத் தீர்ப்பிற்கு முன்பே 1987 பிப்ரவரியில் சச்சிதானந்த் பாண்டே தீர்ப்பு வந்தது.",
    "M.C. Mehta Kanpur Tanneries case (1987) was decided long before Godavarman (1996).",
    "தவறு. 1996-ல் கோதாவர்மன் வழக்கிற்கு நீண்ட காலத்திற்கு முன்பே எம்.சி. மேத்தா கான்பூர் வழக்கு (1987) வந்தது.",
    "This displays reverse chronological sequence.",
    "தவறு. இது தலைகீழ் காலவரிசையைக் காட்டுகிறது.",
    "TNPSC Trap: In Sachidanand Pandey (1987), Supreme Court stated that whenever ecology is disturbed, Court is bound to keep Art 48A and Art 51A(g) in mind.",
    "TNPSC பொறி: சச்சிதானந்த் பாண்டே (1987) வழக்கில், சுற்றுச்சூழல் பாதிக்கப்படும் போதெல்லாம் நீதிமன்றம் உறுப்பு 48A மற்றும் உறுப்பு 51A(g)-ஐ மனதில் கொள்ளக் கடமைப்பட்டுள்ளது எனக் கூறியது.",
    "In Nagaraja case (2014), Supreme Court held that animal welfare is protected under Article 51A(g) ('compassion for living creatures').",
    "நாகராஜா வழக்கில் (2014), உறுப்பு 51A(g)-ன் கீழ் ('உயிரினங்களிடம் கருணை') விலங்கு நலன் பாதுகாக்கப்படுகிறது என உச்சநீதிமன்றம் கூறியது.",
    "Analyze", 60, "High"
))

# Q23 - Medium -> B
questions.append(create_q(
    "FD_CHRONO_023", "Medium",
    "Arrange the timeline of the Justice Verma Committee on Fundamental Duties in correct chronological order:\n\n1. Enactment of 42nd CAA inserting Part IVA into the Constitution\n2. Appointment of Justice Verma Committee by the Union Government\n3. Submission of Justice Verma Committee Report identifying legal provisions for duties\n4. Presentation of the NCRWC Report endorsing Verma Committee recommendations",
    "அடிப்படை கடமைகள் பற்றிய நீதியரசர் வர்மா குழுவின் காலவரிசையைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:\n\n1. 42வது திருத்தம் மூலம் அரசியலமைப்பில் பகுதி IVA சேர்க்கப்படுதல்\n2. ஒன்றிய அரசாங்கத்தால் நீதியரசர் வர்மா குழு நியமிக்கப்படுதல்\n3. கடமைகளுக்கான சட்ட விதிகளைச் சுட்டிக்காட்டி நீதியரசர் வர்மா குழு அறிக்கை சமர்ப்பித்தல்\n4. வர்மா குழுவின் பரிந்துரைகளை ஆதரித்து NCRWC அறிக்கை சமர்ப்பிக்கப்படுதல்",
    [
        {"id": "1", "en": "42nd CAA inserting Part IVA (1976)", "ta": "பகுதி IVA-ஐச் சேர்த்த 42வது திருத்தம் (1976)"},
        {"id": "2", "en": "Appointment of Justice Verma Committee (1998)", "ta": "நீதியரசர் வர்மா குழு நியமனம் (1998)"},
        {"id": "3", "en": "Submission of Justice Verma Committee Report (1999)", "ta": "நீதியரசர் வர்மா குழு அறிக்கை சமர்ப்பிப்பு (1999)"},
        {"id": "4", "en": "Presentation of NCRWC Report (2002)", "ta": "NCRWC அறிக்கை சமர்ப்பிப்பு (2002)"}
    ],
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "4 -> 3 -> 2 -> 1",
    "B",
    "Correct Chronological Sequence: 1. 42nd CAA (1976) -> 2. Verma Committee Appointed (1998) -> 3. Verma Report Submitted (1999) -> 4. NCRWC Report (2002).",
    "சரியான காலவரிசை: 1. 42வது திருத்தம் (1976) -> 2. வர்மா குழு நியமனம் (1998) -> 3. வர்மா அறிக்கை சமர்ப்பிப்பு (1999) -> 4. NCRWC அறிக்கை (2002).",
    "1976 -> 1998 -> 1999 -> 2002 represents the exact historical sequence.",
    "சரி. 1976 -> 1998 -> 1999 -> 2002 என்பது சரியான வரலாற்று வரிசையாகும்.",
    "Part IVA was inserted by the 42nd Amendment in 1976, long before the Verma Committee was set up in 1998.",
    "தவறு. 1998-ல் வர்மா குழு அமைப்பதற்கு நீண்ட காலத்திற்கு முன்பே 1976-ல் 42வது திருத்தத்தால் பகுதி IVA சேர்க்கப்பட்டது.",
    "Verma Committee was appointed in 1998, before submitting its report in 1999.",
    "தவறு. 1999-ல் அறிக்கை சமர்ப்பிப்பதற்கு முன்பே 1998-ல் வர்மா குழு நியமிக்கப்பட்டது.",
    "This represents reverse order.",
    "தவறு. இது தலைகீழ் வரிசையைக் காட்டுகிறது.",
    "TNPSC Trap: Justice Verma Committee was appointed in 1998 specifically to teach and operationalize Fundamental Duties in educational institutions.",
    "TNPSC பொறி: கல்வி நிறுவனங்களில் அடிப்படை கடமைகளைக் கற்பிக்கவும் செயல்படுத்தவும் 1998-ல் நீதியரசர் வர்மா குழு அமைக்கப்பட்டதை நினைவில் கொள்க.",
    "Verma Committee identified 8 statutory Acts that enforce non-justiciable Fundamental Duties in India.",
    "இந்தியாவில் அமல்படுத்த முடியாத அடிப்படை கடமைகளை அமல்படுத்தும் 8 நாடாளுமன்றச் சட்டங்களை வர்மா குழு சுட்டிக்காட்டியது.",
    "Understand", 60, "High"
))

# Q24 - Medium -> A
questions.append(create_q(
    "FD_CHRONO_024", "Medium",
    "Arrange the following landmark Constitutional Amendments inserting NEW PARTS into the Constitution of India in correct chronological order:\n\n1. 42nd CAA (Inserted Part IVA - Fundamental Duties and Part XIVA - Tribunals)\n2. 73rd CAA (Inserted Part IX - The Panchayats)\n3. 74th CAA (Inserted Part IXA - The Municipalities)\n4. 97th CAA (Inserted Part IXB - The Co-operative Societies)",
    "இந்திய அரசியலமைப்பில் புதிய பகுதிகளை இணைத்த பின்வரும் முக்கிய அரசியலமைப்பு திருத்தங்களைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:\n\n1. 42வது திருத்தம் (பகுதி IVA - அடிப்படை கடமைகள் & பகுதி XIVA - தீர்ப்பாயங்கள் சேர்த்தது)\n2. 73வது திருத்தம் (பகுதி IX - ஊராட்சிகள் சேர்த்தது)\n3. 74வது திருத்தம் (பகுதி IXA - நகராட்சிகள் சேர்த்தது)\n4. 97வது திருத்தம் (பகுதி IXB - கூட்டுறவு சங்கங்கள் சேர்த்தது)",
    [
        {"id": "1", "en": "42nd Constitutional Amendment Act (1976)", "ta": "42வது அரசியலமைப்பு திருத்தச் சட்டம் (1976)"},
        {"id": "2", "en": "73rd Constitutional Amendment Act (1992)", "ta": "73வது அரசியலமைப்பு திருத்தச் சட்டம் (1992)"},
        {"id": "3", "en": "74th Constitutional Amendment Act (1992)", "ta": "74வது அரசியலமைப்பு திருத்தச் சட்டம் (1992)"},
        {"id": "4", "en": "97th Constitutional Amendment Act (2011)", "ta": "97வது அரசியலமைப்பு திருத்தச் சட்டம் (2011)"}
    ],
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "4 -> 3 -> 2 -> 1",
    "A",
    "Correct Chronological Sequence: 1. 42nd CAA Part IVA (1976) -> 2. 73rd CAA Part IX (1992) -> 3. 74th CAA Part IXA (1992) -> 4. 97th CAA Part IXB (2011).",
    "சரியான காலவரிசை: 1. 42வது திருத்தம் பகுதி IVA (1976) -> 2. 73வது திருத்தம் பகுதி IX (1992) -> 3. 74வது திருத்தம் பகுதி IXA (1992) -> 4. 97வது திருத்தம் பகுதி IXB (2011).",
    "1976 -> 1992 (73rd) -> 1992 (74th) -> 2011 (97th) represents the exact chronological order of amendments adding new Parts.",
    "சரி. 1976 -> 1992 (73வது) -> 1992 (74வது) -> 2011 (97வது) என்பது புதிய பகுதிகளைச் சேர்த்த திருத்தங்களின் சரியான வரிசையாகும்.",
    "Part IVA was added by 42nd CAA in 1976, long before 73rd CAA in 1992.",
    "தவறு. 1992-ன் 73வது திருத்தத்திற்கு நீண்ட காலத்திற்கு முன்பே 1976-ல் 42வது திருத்தத்தால் பகுதி IVA சேர்க்கப்பட்டது.",
    "73rd CAA (Panchayats) was enacted prior to 74th CAA (Municipalities).",
    "தவறு. 74வது திருத்தத்திற்கு (நகராட்சிகள்) முன்பே 73வது திருத்தம் (ஊராட்சிகள்) இயற்றப்பட்டது.",
    "This shows reverse chronological order.",
    "தவறு. இது தலைகீழ் காலவரிசையைக் காட்டுகிறது.",
    "TNPSC Trap: Part IVA (Fundamental Duties) and Part XIVA (Tribunals) were both added to the Constitution by the 42nd CAA in 1976.",
    "TNPSC பொறி: பகுதி IVA (அடிப்படை கடமைகள்) மற்றும் பகுதி XIVA (தீர்ப்பாயங்கள்) ஆகிய இரண்டும் 1976-ன் 42வது திருத்தத்தால் அரசியலமைப்பில் சேர்க்கப்பட்டன.",
    "Part IVA currently consists of a single Article, Article 51A.",
    "பகுதி IVA தற்போது உறுப்பு 51A என்ற ஒரே ஒரு உறுப்பைக் கொண்டுள்ளது.",
    "Understand", 60, "High"
))

# Q25 - Medium -> D
questions.append(create_q(
    "FD_CHRONO_025", "Medium",
    "Arrange the following developments regarding national symbols, composite culture, and values under Article 51A in correct chronological order:\n\n1. Prevention of Insults to National Honour Act enacted\n2. Bijoe Emmanuel judgment regarding standing for National Anthem\n3. Aruna Roy judgment upholding value education in schools\n4. Supreme Court interim order mandating playing National Anthem in cinema halls",
    "உறுப்பு 51A-ன் கீழ் தேசிய சின்னங்கள், கூட்டுப் பண்பாடு மற்றும் மதிப்புகள் தொடர்பான பின்வரும் வளர்ச்சிகளைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:\n\n1. தேசிய சின்னங்கள்/மதிப்பை அவமதிப்பதைத் தடுக்கும் சட்டம் இயற்றப்படுதல்\n2. தேசிய கீதத்திற்காக எழுந்து நிற்பது பற்றிய பிஜோய் இம்மானுவேல் தீர்ப்பு\n3. பள்ளிகளில் மதிப்புகளுக்கான கல்வியை உறுதி செய்த அருணா ராய் தீர்ப்பு\n4. திரையரங்குகளில் தேசிய கீதம் இசைப்பதை கட்டாயமாக்கிய உச்சநீதிமன்ற இடைக்கால உத்தரவு",
    [
        {"id": "1", "en": "Prevention of Insults to National Honour Act (1971)", "ta": "தேசிய சின்னங்கள் அவமதிப்பு தடுப்புச் சட்டம் (1971)"},
        {"id": "2", "en": "Bijoe Emmanuel v. State of Kerala (1986)", "ta": "பிஜோய் இம்மானுவேல் எதிராக கேரள மாநிலம் (1986)"},
        {"id": "3", "en": "Aruna Roy v. Union of India (2002)", "ta": "அருணா ராய் எதிராக இந்திய யூனியன் (2002)"},
        {"id": "4", "en": "SC interim order on National Anthem in Cinema Halls (2016)", "ta": "திரையரங்குகளில் தேசிய கீதம் பற்றிய உச்சநீதிமன்ற உத்தரவு (2016)"}
    ],
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "4 -> 3 -> 2 -> 1",
    "D",
    "Correct Chronological Sequence: 1. Prevention of Insults Act (1971) -> 2. Bijoe Emmanuel (1986) -> 3. Aruna Roy (2002) -> 4. Cinema Halls Order (2016).",
    "சரியான காலவரிசை: 1. தேசிய சின்னங்கள் அவமதிப்பு தடுப்புச் சட்டம் (1971) -> 2. பிஜோய் இம்மானுவேல் (1986) -> 3. அருணா ராய் (2002) -> 4. திரையரங்க உத்தரவு (2016).",
    "1971 -> 1986 -> 2002 -> 2016 represents the exact chronological progression.",
    "சரி. 1971 -> 1986 -> 2002 -> 2016 என்பது சரியான காலவரிசையாகும்.",
    "Prevention of Insults to National Honour Act was passed in 1971, prior to Bijoe Emmanuel in 1986.",
    "தவறு. 1986-ன் பிஜோய் இம்மானுவேல் வழக்கிற்கு முன்பே 1971-ல் தேசிய சின்னங்கள் அவமதிப்பு தடுப்புச் சட்டம் இயற்றப்பட்டது.",
    "Bijoe Emmanuel judgment (1986) preceded Aruna Roy judgment (2002).",
    "தவறு. அருணா ராய் தீர்ப்பிற்கு (2002) முன்பே பிஜோய் இம்மானுவேல் தீர்ப்பு (1986) வந்தது.",
    "This shows reverse chronological order.",
    "தவறு. இது தலைகீழ் காலவரிசையைக் காட்டுகிறது.",
    "TNPSC Trap: In Shyam Narayan Chouksey case (2016), SC issued interim directions to play National Anthem in cinema halls, which were later modified in 2018 making it optional.",
    "TNPSC பொறி: ஷியாம் நாராயண் சௌக்சே வழக்கில் (2016), திரையரங்குகளில் தேசிய கீதம் இசைக்க இடைக்கால உத்தரவிடப்பட்டு, 2018-ல் அது விருப்பத்தின் பேரில் மாற்றியமைக்கப்பட்டது.",
    "Respecting National Flag and National Anthem is the first Fundamental Duty under Article 51A(a).",
    "தேசியக் கொடி மற்றும் தேசிய கீதத்தை மதிப்பது உறுப்பு 51A(a)-ன் கீழ் உள்ள முதல் அடிப்படை கடமையாகும்.",
    "Understand", 60, "High"
))

# Save to target JSON file
target_file = "data/questions/polity/fundamental_duties_chronology.json"
os.makedirs(os.path.dirname(target_file), exist_ok=True)
with open(target_file, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"Successfully updated {len(questions)} questions in {target_file}")
