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
    bloom="Analyze", time_sec=60, similarity="High"
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
        "source_reference": ["M. Laxmikanth - Indian Polity", "NCERT", "Samacheer Kalvi"],
        "bloom_level": bloom,
        "estimated_time_sec": time_sec,
        "pyq_similarity": similarity,
        "tags": ["Polity", "Fundamental Duties", "Reasoning"],
        "question_en": question_en,
        "question_ta": question_ta,
        "options_en": options_en,
        "options_ta": options_ta,
        "answer": correct_pos.lower(),
        "explanation_en": exp_en,
        "explanation_ta": exp_ta
    }

questions = []

# Pattern: Q1: A, Q2: B, Q3: C, Q4: D, Q5: A, Q6: B, Q7: C, Q8: D, Q9: A, Q10: B, Q11: C, Q12: D, Q13: A, Q14: B, Q15: C, Q16: D, Q17: A, Q18: B, Q19: C, Q20: D, Q21: A, Q22: B, Q23: C, Q24: D, Q25: D

# Q1 - Easy-Medium -> A
questions.append(create_q(
    "FD_R_001", "Easy-Medium", "Situation / Application",
    "SITUATION: A citizen uses the National Flag as a disposable tablecloth at a private commercial event and discards it carelessly on the street after the event.\n\nQUESTION: Which Fundamental Duty under Article 51A has been violated, and through which statutory act is this duty legally enforced?",
    "சூழல்: குடிமகன் ஒருவர் வணிக நிகழ்வு ஒன்றில் தேசியக் கொடியை ஒருமுறை மட்டுமே பயன்படுத்தும் மேஜை விரிப்பாகப் பயன்படுத்தி, நிகழ்விற்குப் பிறகு அதைத் தெருவில் கண்டுகொள்ளாமல் வீசுகிறார்.\n\nகேள்வி: உறுப்பு 51A-ன் கீழ் எந்த அடிப்படை கடமை மீறப்பட்டுள்ளது, மேலும் எந்த நாடாளுமன்றச் சட்டத்தின் மூலம் இக்கடமை சட்டப்பூர்வமாக அமல்படுத்தப்படுகிறது?",
    "", "", "", "",
    "Article 51A(a) — Prevention of Insults to National Honour Act, 1971", "உறுப்பு 51A(a) — தேசிய சின்னங்கள் அவமதிப்பு தடுப்புச் சட்டம், 1971",
    "Article 51A(b) — Representation of the People Act, 1951", "உறுப்பு 51A(b) — மக்கள் பிரதிநிதித்துவச் சட்டம், 1951",
    "Article 51A(c) — Unlawful Activities (Prevention) Act, 1967", "உறுப்பு 51A(c) — சட்டவிரோத நடவடிக்கைகள் தடுப்புச் சட்டம், 1967",
    "Article 51A(i) — Prevention of Damage to Public Property Act, 1984", "உறுப்பு 51A(i) — பொதுச் சொத்து சேதத் தடுப்புச் சட்டம், 1984",
    "A",
    "Article 51A(a) mandates respecting the National Flag and National Anthem. Disrespecting or improper use of the National Flag is an offense under the Prevention of Insults to National Honour Act, 1971.",
    "உறுப்பு 51A(a) தேசியக் கொடி மற்றும் தேசிய கீதத்தை மதிக்கக் கட்டளையிடுகிறது. தேசியக் கொடியை அவமதிப்பது 1971-ன் தேசிய சின்னங்கள் அவமதிப்பு தடுப்புச் சட்டத்தின் கீழ் குற்றமாகும்.",
    "Article 51A(a) deals with respecting the National Flag and Anthem, enforced via the 1971 Act.", "உறுப்பு 51A(a) தேசியக் கொடி மற்றும் கீதத்தை மதிப்பது பற்றியது, 1971 சட்டம் மூலம் அமல்படுத்தப்படுகிறது.",
    "Article 51A(b) deals with noble ideals of the freedom struggle, not national symbols.", "உறுப்பு 51A(b) சுதந்திரப் போராட்ட லட்சியங்களைப் பற்றியது, தேசிய சின்னங்கள் பற்றியது அல்ல.",
    "Article 51A(c) deals with sovereignty, unity, and integrity of India.", "உறுப்பு 51A(c) இறையாண்மை, ஒற்றுமை மற்றும் ஒருமைப்பாடு பற்றியது.",
    "Article 51A(i) deals with safeguarding public property.", "உறுப்பு 51A(i) பொதுச் சொத்தைப் பாதுகாப்பது பற்றியது.",
    "TNPSC Trap: Verma Committee (1999) identified the Prevention of Insults to National Honour Act, 1971 as the primary statutory enforcer of Article 51A(a).",
    "TNPSC பொறி: உறுப்பு 51A(a)-ன் முதன்மைச் சட்ட அமலாக்க அதிகாரமாக 1971-ன் தேசிய சின்னங்கள் அவமதிப்பு தடுப்புச் சட்டத்தை வர்மா குழு (1999) சுட்டிக்காட்டியது.",
    "The National Flag cannot be used as a drapery or clothing under the Flag Code of India, 2002.",
    "இந்திய தேசியக் கொடி விதித் தொகுப்பு 2002-ன் படி தேசியக் கொடியை ஆடையாகவோ அல்லது விரிப்பாகவோ பயன்படுத்தக் கூடாது.",
    "Understand", 60, "High"
))

# Q2 - Medium - Assertion & Reason -> B
questions.append(create_q(
    "FD_R_002", "Medium", "Assertion & Reason",
    "Assertion (A): Although Fundamental Duties under Article 51A are non-justiciable, courts rely on them to determine the constitutional validity of laws.\nReason (R): The Supreme Court has ruled that restrictions imposed on Fundamental Rights under Article 19 to enforce a Fundamental Duty are treated as 'reasonable restrictions'.",
    "கூற்று (A): உறுப்பு 51A-ன் கீழ் உள்ள அடிப்படை கடமைகள் நீதிமன்றத்தால் நேரடியாக அமல்படுத்தப்பட முடியாதவை என்றாலும், சட்டங்களின் அரசியலமைப்பு செல்லுபடியாகும் தன்மையை தீர்மானிக்க நீதிமன்றங்கள் அவற்றை நம்பியுள்ளன.\nகாரணம் (R): ஒரு அடிப்படை கடமையை அமல்படுத்த உறுப்பு 19-ன் கீழ் அடிப்படை உரிமைகள் மீது விதிக்கப்படும் கட்டுப்பாடுகள் 'நியாயமான கட்டுப்பாடுகளாகக்' கருதப்படும் என்று உச்சநீதிமன்றம் தீர்ப்பளித்துள்ளது.",
    "Although Fundamental Duties under Article 51A are non-justiciable, courts rely on them to determine the constitutional validity of laws.",
    "உறுப்பு 51A-ன் கீழ் உள்ள அடிப்படை கடமைகள் நீதிமன்றத்தால் அமல்படுத்தப்பட முடியாதவை என்றாலும், சட்டங்களின் அரசியலமைப்பு செல்லுபடியாகும் தன்மையை தீர்மானிக்க நீதிமன்றங்கள் அவற்றை நம்பியுள்ளன.",
    "The Supreme Court has ruled that restrictions imposed on Fundamental Rights under Article 19 to enforce a Fundamental Duty are treated as 'reasonable restrictions'.",
    "ஒரு அடிப்படை கடமையை அமல்படுத்த உறுப்பு 19-ன் கீழ் அடிப்படை உரிமைகள் மீது விதிக்கப்படும் கட்டுப்பாடுகள் 'நியாயமான கட்டுப்பாடுகளாகக்' கருதப்படும் என்று உச்சநீதிமன்றம் தீர்ப்பளித்துள்ளது.",
    "Both A and R are correct and R is the correct explanation of A", "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்.",
    "Both A and R are correct but R is NOT the correct explanation of A", "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல.",
    "A is correct but R is incorrect", "A சரி, ஆனால் R தவறு.",
    "A is incorrect but R is correct", "A தவறு, ஆனால் R சரி.",
    "B",
    "Both Assertion and Reason are true, and R explains A. Non-justiciability does not mean legal irrelevance; SC uses FD to interpret the 'reasonableness' of restrictions on Fundamental Rights under Article 19.",
    "கூற்று A மற்றும் காரணம் R இரண்டும் சரி, மேலும் R என்பது A-விற்கு சரியான விளக்கம். அமல்படுத்த முடியாதது என்பது சட்ட முக்கியத்துவம் இல்லாதது அல்ல; உறுப்பு 19-ன் கீழ் உரிமைகள் மீதான கட்டுப்பாடுகளின் நியாயத் தன்மையைச் சோதிக்க உச்சநீதிமன்றம் கடமைகளைப் பயன்படுத்துகிறது.",
    "Article 19 restrictions evaluated in light of Fundamental Duties make those restrictions constitutionally reasonable.", "அடிப்படை கடமைகளின் அடிப்படையில் உறுப்பு 19 கட்டுப்பாடுகள் மதிப்பிடப்படும் போது அவை நியாயமானவையாகக் கருதப்படுகின்றன.",
    "Reason directly explains why non-justiciable duties carry legal weight in constitutional review.", "அமல்படுத்த முடியாத கடமைகள் அரசியலமைப்பு ஆய்வில் ஏன் சட்ட முக்கியத்துவம் பெறுகின்றன என்பதை காரணம் நேரடியாக விளக்குகிறது.",
    "Reason is factually correct as per Supreme Court precedents (e.g. Mirzapur Moti Koreshi case).", "உச்சநீதிமன்ற முன்மாதிரிகளின்படி (எ.கா. மிர்சாபூர் மோதி கொரேஷி வழக்கு) காரணம் சரியானது.",
    "Assertion is factually true; duties are non-justiciable yet legally relevant.", "கூற்று சரியானது; கடமைகள் நேரடியாக அமல்படுத்த முடியாதவை ஆனால் சட்டப்பூர்வமாகத் தொடர்புடையவை.",
    "TNPSC Trap: Remember that 'non-justiciable' means a citizen cannot file a writ solely for non-performance of a duty, but Parliament can make laws enforcing duties and courts will uphold such laws.",
    "TNPSC பொறி: 'அமல்படுத்த முடியாதது' என்றால் கடமையைச் செய்யாததற்காக நேரடியாக வழக்கு தொடர முடியாது, ஆனால் நாடாளுமன்றம் கடமைகளை அமல்படுத்தச் சட்டங்களை இயற்றலாம், நீதிமன்றங்கள் அதை உறுதி செய்யும்.",
    "The SC in Javed v. State of Haryana (2003) reaffirmed that Fundamental Rights must be read along with Fundamental Duties.",
    "ஜாவேத் எதிராக ஹரியானா மாநில வழக்கிலும் (2003) அடிப்படை உரிமைகளை அடிப்படை கடமைகளுடன் இணைத்தே படிக்க வேண்டும் என்று உச்சநீதிமன்றம் மீண்டும் உறுதிப்படுத்தியது.",
    "Analyze", 60, "High"
))

# Q3 - Medium - Three-Statement -> C
questions.append(create_q(
    "FD_R_003", "Medium", "Three-Statement Reasoning",
    "Consider the following statements regarding the Education Triad under the Constitution after the 86th Amendment Act, 2002:\n\n1. Article 21A creates a Fundamental Right to education for children aged 6 to 14 years, placing primary obligation on the State.\n2. Article 45 directs the State to provide early childhood care and education for all children until they complete the age of six years.\n3. Article 51A(k) imposes a Fundamental Duty on parents/guardians to provide educational opportunities to their children aged 6 to 14 years.\n\nWhich of the statements given above are correct?",
    "2002-ன் 86வது திருத்தச் சட்டத்திற்குப் பிறகு அரசியலமைப்பின் கீழ் கல்விக் கட்டமைப்பு பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n\n1. உறுப்பு 21A 6 முதல் 14 வயது வரையிலான குழந்தைகளுக்குக் கல்வியை அடிப்படை உரிமையாக்கி, அரசின் மீது முதன்மைப் பொறுப்பைச் சுமத்துகிறது.\n2. உறுப்பு 45 ஆறு வயது வரையிலான அனைத்துக் குழந்தைகளுக்கும் ஆரம்பகால குழந்தை பராமரிப்பு மற்றும் கல்வியை வழங்க அரசை வழிகாட்டுகிறது.\n3. உறுப்பு 51A(k) 6 முதல் 14 வயது வரையிலான குழந்தைகளுக்குக் கல்விக்கான வாய்ப்புகளை வழங்கப் பெற்றோர்/பாதுகாவலர்கள் மீது அடிப்படை கடமையை விதிக்கிறது.\n\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
    "", "", "", "",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "C",
    "All three statements are correct. The 86th Amendment Act, 2002 restructured education into a tripartite constitutional system: Art 21A (FR - State duty), Art 45 (DPSP - early childhood 0-6 yrs), Art 51A(k) (FD - parent duty for 6-14 yrs).",
    "மூன்று கூற்றுகளும் சரியானவை. 2002-ன் 86வது திருத்தச் சட்டம் கல்வியை முத்தரப்பு அரசியலமைப்பு அமைப்பாக மறுசீரமைத்தது: உறுப்பு 21A (FR - அரசு கடமை), உறுப்பு 45 (DPSP - 0-6 வயது பராமரிப்பு), உறுப்பு 51A(k) (FD - 6-14 வயது வரை பெற்றோர் கடமை).",
    "All three statements (1, 2, and 3) are true.", "மூன்று கூற்றுகளும் (1, 2, மற்றும் 3) சரியானவை.",
    "Statement 1 correctly defines Article 21A (FR).", "கூற்று 1 உறுப்பு 21A-ஐச் சரியாக வரையறுக்கிறது.",
    "Statement 2 correctly defines modified Article 45 (DPSP).", "கூற்று 2 திருத்தப்பட்ட உறுப்பு 45-ஐச் சரியாக வரையறுக்கிறது.",
    "Statement 3 correctly defines Article 51A(k) (FD).", "கூற்று 3 உறுப்பு 51A(k)-ஐச் சரியாக வரையறுக்கிறது.",
    "TNPSC Trap: Do not mix age groups! Art 21A and Art 51A(k) cover 6 to 14 years, whereas modified Art 45 covers early childhood below 6 years.",
    "TNPSC பொறி: வயதுக் குழுக்களைக் குழப்பக் கூடாது! உறுப்பு 21A மற்றும் 51A(k) 6 முதல் 14 வயது வரை, திருத்தப்பட்ட உறுப்பு 45 6 வயதிற்குட்பட்ட குழந்தைப் பருவ பராமரிப்பு பற்றியது.",
    "Article 51A(k) was added as the 11th Fundamental Duty in 2002.",
    "உறுப்பு 51A(k) 2002-ல் 11வது அடிப்படை கடமையாகச் சேர்க்கப்பட்டது.",
    "Analyze", 60, "High"
))

# Q4 - Easy-Medium - Situation -> D
questions.append(create_q(
    "FD_R_004", "Easy-Medium", "Situation / Application",
    "SITUATION: An industrialist dumps chemical waste into a public lake and argues in court that environmental preservation is exclusively the government's responsibility under Directive Principles (Article 48A), not an obligation of private citizens.\n\nQUESTION: How does constitutional reasoning evaluate this argument?",
    "சூழல்: தொழில்அதிபர் ஒருவர் இரசாயனக் கழிவுகளைப் பொது ஏரியில் கொட்டிவிட்டு, சுற்றுச்சூழல் பாதுகாப்பு என்பது அரசு நெறிமுறைக் கோட்பாடுகளின் (உறுப்பு 48A) கீழ் அரசின் பொறுப்பு மட்டுமே தவிரத் தனிப்பட்ட குடிமகனின் கடமையல்ல என்று நீதிமன்றத்தில் வாதாடுகிறார்.\n\nகேள்வி: அரசியலமைப்பு பகுப்பாய்வு இந்த வாதத்தை எவ்வாறு மதிப்பிடுகிறது?",
    "", "", "", "",
    "The argument is valid because Article 48A places environmental duty solely on the State.", "உறுப்பு 48A சுற்றுச்சூழல் கடமையை அரசு மீது மட்டுமே சுமத்துவதால் இந்த வாதம் சரியானது.",
    "The argument is valid because Fundamental Duties have no legal existence.", "அடிப்படை கடமைகளுக்குச் சட்டப்பூர்வ இருப்பு இல்லாததால் இந்த வாதம் சரியானது.",
    "The argument is invalid because Article 48A applies only to municipal corporations.", "உறுப்பு 48A நகராட்சிகளுக்கு மட்டுமே பொருந்தும் என்பதால் இந்த வாதம் தவறானது.",
    "The argument is invalid because Article 51A(g) places a Fundamental Duty on every citizen to protect and improve the natural environment, including lakes.", "உறுப்பு 51A(g) ஏரிகள் உட்பட இயற்கைச் சூழலைப் பாதுகாக்கவும் மேம்படுத்தவும் ஒவ்வொரு குடிமகனுக்கும் அடிப்படை கடமையை விதிப்பதால் இந்த வாதம் தவறானது.",
    "D",
    "The argument is invalid. While Article 48A places a duty on the State, Article 51A(g) explicitly imposes a Fundamental Duty on every citizen to protect and improve the natural environment, including forests, lakes, rivers, and wildlife.",
    "இந்த வாதம் தவறானது. உறுப்பு 48A அரசுக்குக் கடமை விதிக்கும் அதே வேளையில், உறுப்பு 51A(g) காடுகள், ஏரிகள், ஆறுகள் மற்றும் வனவிலங்குகள் உட்பட இயற்கைச் சூழலைப் பாதுகாக்கவும் மேம்படுத்தவும் ஒவ்வொரு குடிமகனுக்கும் அடிப்படை கடமையை விதிக்கிறது.",
    "Article 51A(g) directly refutes the claim that citizens have no duty towards environment.", "குடிமக்களுக்குச் சுற்றுச்சூழல் கடமை இல்லை என்ற வாதத்தை உறுப்பு 51A(g) நேரடியாக மறுக்கிறது.",
    "Article 48A applies to the State, but citizen duty is explicitly created under Article 51A(g).", "உறுப்பு 48A அரசுக்குப் பொருந்தும், ஆனால் குடிமகனின் கடமை உறுப்பு 51A(g)-ன் கீழ் தெளிவாக உருவாக்கப்பட்டுள்ளது.",
    "Fundamental Duties exist in Part IVA of the Constitution.", "அரசியலமைப்பின் பகுதி IVA-ல் அடிப்படை கடமைகள் நிலவுகின்றன.",
    "Article 48A applies to the State as a whole, including Union and State governments.", "உறுப்பு 48A ஒன்றியம் மற்றும் மாநில அரசுகள் உட்பட ஒட்டுமொத்த அரசுக்கும் பொருந்தும்.",
    "TNPSC Trap: DPSP Article 48A (State duty) and Fundamental Duty Article 51A(g) (Citizen duty) were BOTH added by the 42nd CAA, 1976.",
    "TNPSC பொறி: DPSP உறுப்பு 48A (அரசு கடமை) மற்றும் அடிப்படை கடமை உறுப்பு 51A(g) (குடிமகன் கடமை) ஆகிய இரண்டும் 1976-ன் 42வது திருத்தத்தால் சேர்க்கப்பட்டன.",
    "Article 51A(g) explicitly includes four elements: forests, lakes, rivers, and wildlife, plus compassion for living creatures.",
    "உறுப்பு 51A(g) நான்கு கூறுகளைக் குறிப்பிடுகிறது: காடுகள், ஏரிகள், ஆறுகள், வனவிலங்குகள் மற்றும் உயிரினங்களிடம் கருணை.",
    "Understand", 60, "High"
))

# Q5 - Medium - Two-Statement -> A
questions.append(create_q(
    "FD_R_005", "Medium", "Two-Statement Reasoning",
    "Consider the following statements regarding the Swaran Singh Committee recommendations vs actual 42nd Amendment provisions:\n\n1. The Swaran Singh Committee recommended that Parliament should provide for penalties or punishments for non-compliance with Fundamental Duties.\n2. The 42nd Constitutional Amendment Act, 1976 incorporated explicit penalty provisions into Article 51A for citizens who fail to perform duties.\n\nWhich of the statement(s) given above is/are correct?",
    "ஸ்வரன் சிங் குழுவின் பரிந்துரைகள் vs அசல் 42வது திருத்த விதிகள் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n\n1. அடிப்படை கடமைகளைப் பின்பற்றாதவர்களுக்கு நாடாளுமன்றம் தண்டனை அல்லது அபராதம் விதிக்க வகை செய்ய வேண்டும் என்று ஸ்வரன் சிங் குழு பரிந்துரைத்தது.\n2. 1976-ன் 42வது அரசியலமைப்பு திருத்தச் சட்டம் கடமைகளைச் செய்யத் தவறும் குடிமக்களுக்கு உறுப்பு 51A-ல் நேரடித் தண்டனை விதிகளை இணைத்தது.\n\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானவை?",
    "", "", "", "",
    "1 only", "1 மட்டும்",
    "2 only", "2 மட்டும்",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "Neither 1 nor 2", "எதுவும் இல்லை",
    "A",
    "Statement 1 is correct. The Swaran Singh Committee recommended penal provisions for non-compliance, but Parliament REJECTED this recommendation and did NOT include penalty clauses in Article 51A. Thus statement 2 is incorrect.",
    "கூற்று 1 சரி. கடமைகளைப் பின்பற்றாதவருக்குத் தண்டனை விதிக்க ஸ்வரன் சிங் குழு பரிந்துரைத்தது, ஆனால் நாடாளுமன்றம் இப்பரிந்துரையை நிராகரித்தது மற்றும் உறுப்பு 51A-ல் தண்டனை விதிகளைச் சேர்க்கவில்லை. எனவே கூற்று 2 தவறானது.",
    "Swaran Singh Committee recommended penalty provisions, which were rejected by Parliament.", "ஸ்வரன் சிங் குழு தண்டனை விதிகளைப் பரிந்துரைத்தது, ஆனால் அது நாடாளுமன்றத்தால் நிராகரிக்கப்பட்டது.",
    "Statement 2 is false because 42nd CAA did NOT incorporate penalty provisions into Article 51A.", "42வது திருத்தம் உறுப்பு 51A-ல் தண்டனை விதிகளைச் சேர்க்காததால் கூற்று 2 தவறானது.",
    "Both statements are not true because statement 2 is incorrect.", "கூற்று 2 தவறானது என்பதால் இரண்டும் சரி என்பது தவறாகும்.",
    "Statement 1 is factually true under Swaran Singh recommendations.", "ஸ்வரன் சிங் பரிந்துரைகளின் படி கூற்று 1 உண்மையானது.",
    "TNPSC Trap: Swaran Singh Committee recommended 2 key things that Parliament rejected: 1. Duty to pay taxes, 2. Penalty/punishment for non-performance of duties.",
    "TNPSC பொறி: நாடாளுமன்றம் நிராகரித்த ஸ்வரன் சிங் குழுவின் 2 முக்கிய பரிந்துரைகள்: 1. வரி செலுத்தும் கடமை, 2. கடமைகளைச் செய்யாததற்கான தண்டனை/அபராதம்.",
    "Swaran Singh Committee proposed 8 duties, but Parliament enacted 10 duties in 1976.",
    "ஸ்வரன் சிங் குழு 8 கடமைகளைப் பரிந்துரைத்தது, ஆனால் நாடாளுமன்றம் 10 கடமைகளை இயற்றியது.",
    "Understand", 60, "High"
))

# Q6 - Hard - Case Application -> B
questions.append(create_q(
    "FD_R_006", "Hard", "Case-Based Application",
    "SCENARIO: Three students belonging to Jehovah's Witnesses stand up reverently when the National Anthem is played in their school assembly, but refrain from singing because their religious faith forbids singing anthems to any entity other than God. They are expelled under Article 51A(a).\n\nQUESTION: Applying the Supreme Court ruling in Bijoe Emmanuel v. State of Kerala (1986), what is the correct constitutional verdict?",
    "சூழல்: யெகோவாவின் சாட்சிகள் பிரிவைச் சேர்ந்த மூன்று மாணவர்கள் பள்ளி வழிபாட்டுக் கூட்டத்தில் தேசிய கீதம் இசைக்கப்படும் போது மரியாதையுடன் எழுந்து நிற்கிறார்கள், ஆனால் கடவுளைத் தவிர வேறு எவருக்கும் கீதம் பாடுவதை அவர்களின் மத நம்பிக்கை தடை செய்வதால் பாட மறுக்கிறார்கள். உறுப்பு 51A(a)-ன் கீழ் அவர்கள் பள்ளியிலிருந்து நீக்கப்படுகிறார்கள்.\n\nகேள்வி: பிஜோய் இம்மானுவேல் எதிராக கேரள மாநிலம் (1986) வழக்கின் உச்சநீதிமன்றத் தீர்ப்பைப் பயன்படுத்தினால், சரியான அரசியலமைப்புத் தீர்ப்பு எது?",
    "", "", "", "",
    "The expulsion is valid because Article 51A(a) mandates both standing and vocal singing.", "உறுப்பு 51A(a) எழுந்து நிற்பது மற்றும் பாடுவது இரண்டையும் கட்டாயமாக்குவதால் பள்ளி நீக்கம் செல்லுபடியாகும்.",
    "The expulsion is invalid because standing respectfully satisfies Article 51A(a), and non-singing on genuine religious grounds is protected under Article 25.", "மரியாதையுடன் எழுந்து நின்றாலே உறுப்பு 51A(a) நிறைவேறுகிறது, மேலும் உண்மையான மத நம்பிக்கையின் அடிப்படையில் பாடாமல் இருப்பது உறுப்பு 25-ன் கீழ் பாதுகாக்கப்படுகிறது என்பதால் பள்ளி நீக்கம் செல்லாது.",
    "The expulsion is valid because Fundamental Duties override Article 25 Fundamental Rights in all educational institutions.", "அனைத்துக் கல்வி நிறுவனங்களிலும் அடிப்படை கடமைகள் உறுப்பு 25 அடிப்படை உரிமைகளை விட மேலோங்குவதால் பள்ளி நீக்கம் செல்லுபடியாகும்.",
    "The expulsion is invalid because Article 51A(a) applies only to government servants, not to school children.", "உறுப்பு 51A(a) அரசு ஊழியர்களுக்கு மட்டுமே பொருந்தும், பள்ளி குழந்தைகளுக்கு அல்ல என்பதால் பள்ளி நீக்கம் செல்லாது.",
    "B",
    "The expulsion is invalid. In Bijoe Emmanuel v. State of Kerala (1986), the Supreme Court held that standing up respectfully during the National Anthem shows proper respect under Article 51A(a). Compelling a person to sing against genuine religious conscience violates Article 25(1).",
    "பள்ளி நீக்கம் செல்லாது. பிஜோய் இம்மானுவேல் எதிராக கேரள மாநில வழக்கில் (1986), தேசிய கீதத்தின் போது மரியாதையுடன் எழுந்து நிற்பதே உறுப்பு 51A(a)-ன் கீழ் தகுந்த மரியாதையைக் காட்டுகிறது என்று உச்சநீதிமன்றம் தீர்ப்பளித்தது. மத நம்பிக்கைக்கு எதிராகப் பாடக் வற்புறுத்துவது உறுப்பு 25(1)-ஐ மீறுவதாகும்.",
    "Standing respectfully satisfies Art 51A(a) duty without violating Art 25(1) religious freedom.", "மரியாதையுடன் எழுந்து நிற்பது உறுப்பு 25(1) மத சுதந்திரத்தை மீறாமல் 51A(a) கடமையை நிறைவேற்றுகிறது.",
    "Vocal singing is not mandatory if it conflicts with genuine religious conscience under Article 25.", "உண்மையான மத நம்பிக்கைக்கு முரணாக இருந்தால் வாய்விட்டுப் பாடுவது கட்டாயமில்லை.",
    "Fundamental Duties do not automatically destroy Article 25 fundamental freedom.", "அடிப்படை கடமைகள் உறுப்பு 25 அடிப்படை சுதந்திரத்தை நேரடியாக ரத்து செய்யாது.",
    "Article 51A(a) applies to all citizens, but standing respectfully fulfills the duty.", "உறுப்பு 51A(a) அனைத்துக் குடிமக்களுக்கும் பொருந்தும், ஆனால் மரியாதையுடன் நிற்பதே கடமையை நிறைவேற்றுகிறது.",
    "TNPSC Trap: Do not confuse standing up (mandatory sign of respect) with singing (protected under Art 25 if genuine religious objection exists).",
    "TNPSC பொறி: எழுந்து நிற்பதையும் (கட்டாய மரியாதைச் சின்னம்) பாடுவதையும் (உண்மையான மத விலக்கு இருந்தால் உறுப்பு 25-ன் கீழ் பாதுகாப்பு) குழப்பக் கூடாது.",
    "Justice O. Chinnappa Reddy delivered the famous judgment in Bijoe Emmanuel (1986).",
    "பிஜோய் இம்மானுவேல் வழக்கில் (1986) புகழ்பெற்ற தீர்ப்பை நீதியரசர் ஓ. சின்னப்ப ரெட்டி வழங்கினார்.",
    "Analyze", 60, "High"
))

# Q7 - Medium - Conceptual -> C
questions.append(create_q(
    "FD_R_007", "Medium", "Conceptual Reasoning",
    "SCENARIO: A person holding a post-graduate degree in science publicly advocates blind faith rituals and opposes evidence-based medical treatment, claiming science and personal beliefs are separate.\n\nQUESTION: Which constitutional insight regarding Article 51A(h) is highlighted by this scenario?",
    "சூழல்: அறிவியலில் முதுகலைப் பட்டம் பெற்ற ஒருவர், அறிவியலும் தனிப்பட்ட நம்பிக்கைகளும் வெவ்வேறானவை என்று கூறி, குருட்டு மூடநம்பிக்கைச் சடங்குகளைப் பகிரங்கமாக ஆதரிக்கிறார் மற்றும் ஆதார அடிப்படையிலான மருத்துவ சிகிச்சையை எதிர்க்கிறார்.\n\nகேள்வி: இந்தச் சூழலின் மூலம் உறுப்பு 51A(h) பற்றிய எந்த அரசியலமைப்பு உண்மை சுட்டிக்காட்டப்படுகிறது?",
    "", "", "", "",
    "Acquiring formal scientific degrees automatically satisfies Article 51A(h).", "முறையான அறிவியல் பட்டங்களைப் பெறுவது தானாகவே உறுப்பு 51A(h)-ஐ நிறைவேற்றுகிறது.",
    "Article 51A(h) applies only to professional scientists in research institutes.", "உறுப்பு 51A(h) ஆராய்ச்சி நிறுவனங்களில் உள்ள தொழில்முறை விஞ்ஞானிகளுக்கு மட்டுமே பொருந்தும்.",
    "Possessing scientific knowledge or degrees does not guarantee 'scientific temper', which requires rational inquiry, evidence-based thinking, and spirit of reform.", "அறிவியல் அறிவோ அல்லது பட்டங்களோ மட்டுமே 'அறிவியல் மனப்பான்மைக்கு' உத்தரவாதம் அளிக்காது; அதற்கு பகுத்தறிவு ஆராய்ச்சி, ஆதார சிந்தனை மற்றும் சீர்திருத்த உணர்வு தேவைப்படுகிறது.",
    "Article 51A(h) empowers police to arrest anyone who follows traditional customs.", "பாரம்பரிய பழக்கவழக்கங்களைப் பின்பற்றும் எவரையும் கைது செய்ய உறுப்பு 51A(h) காவல்துறைக்கு அதிகாரமளிக்கிறது.",
    "C",
    "Possessing scientific literacy/degrees is different from cultivating 'scientific temper'. Article 51A(h) commands developing scientific temper, humanism, and the spirit of inquiry and reform as a mental attitude and civic obligation.",
    "அறிவியல் அறிவு/பட்டங்கள் வைத்திருப்பது வேறு, 'அறிவியல் மனப்பான்மையை' வளர்ப்பது வேறு. உறுப்பு 51A(h) அறிவியல் மனப்பான்மை, மனிதநேயம் மற்றும் ஆராய்ச்சி, சீர்திருத்த உணர்வை மனப்பான்மையாகவும் குடிமைப் பொறுப்பாகவும் வளர்க்கக் கட்டளையிடுகிறது.",
    "Degree alone is not scientific temper; Art 51A(h) stresses rational inquiry and reform attitude.", "பட்டம் மட்டுமே அறிவியல் மனப்பான்மை அல்ல; உறுப்பு 51A(h) பகுத்தறிவு ஆராய்ச்சி மற்றும் சீர்திருத்த மனப்பான்மையை வலியுறுத்துகிறது.",
    "Scientific knowledge is distinct from scientific temper.", "அறிவியல் அறிவு என்பது அறிவியல் மனப்பான்மையிலிருந்து வேறுபட்டது.",
    "Article 51A(h) applies to every citizen of India, not just scientists.", "உறுப்பு 51A(h) விஞ்ஞானிகளுக்கு மட்டுமல்ல, இந்தியாவின் ஒவ்வொரு குடிமகனுக்கும் பொருந்தும்.",
    "Article 51A(h) is a non-justiciable constitutional duty, not a penal arrest authorization.", "உறுப்பு 51A(h) ஒரு அரசியலமைப்பு கடமையாகும், கைது செய்யும் அதிகாரமல்ல.",
    "TNPSC Trap: Article 51A(h) contains 4 pillars: 1. Scientific temper, 2. Humanism, 3. Spirit of inquiry, 4. Spirit of reform.",
    "TNPSC பொறி: உறுப்பு 51A(h) 4 தூண்களைக் கொண்டுள்ளது: 1. அறிவியல் மனப்பான்மை, 2. மனிதநேயம், 3. ஆராய்ச்சி உணர்வு, 4. சீர்திருத்த உணர்வு.",
    "India is the first country to explicitly mandate 'scientific temper' in its Constitution.",
    "தன் அரசியலமைப்பில் 'அறிவியல் மனப்பான்மையை' வெளிப்படையாகக் கட்டாயமாக்கிய முதல் நாடு இந்தியா ஆகும்.",
    "Understand", 60, "High"
))

# Q8 - Hard - Three-Statement -> D
questions.append(create_q(
    "FD_R_008", "Hard", "Three-Statement Reasoning",
    "Consider the following statements regarding the Justice Verma Committee (1999) on Fundamental Duties:\n\n1. The Verma Committee was set up in 1998 to operationalize the strategy for teaching Fundamental Duties in educational institutions.\n2. The Verma Committee identified that non-justiciable Fundamental Duties are actually legal obligations backed by sanctions in various existing statutory Acts.\n3. The Verma Committee recommended creating a separate Writ Jurisdiction in High Courts solely to punish citizens who breach Article 51A.\n\nWhich of the statements given above are correct?",
    "அடிப்படை கடமைகள் பற்றிய நீதியரசர் வர்மா குழு (1999) பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n\n1. கல்வி நிறுவனங்களில் அடிப்படை கடமைகளைக் கற்பிப்பதற்கான உத்தியை நடைமுறைப்படுத்த 1998-ல் வர்மா குழு அமைக்கப்பட்டது.\n2. நீதிமன்றத்தால் நேரடியாக அமல்படுத்த முடியாத அடிப்படை கடமைகள் உண்மையில் பல்வேறு நாடாளுமன்றச் சட்டங்களில் உள்ள சட்ட விதிகளால் ஆதரிக்கப்படுகின்றன என்பதை வர்மா குழு சுட்டிக்காட்டியது.\n3. உறுப்பு 51A-ஐ மீறும் குடிமக்களைத் தண்டிப்பதற்காக மட்டுமே உயர்நீதிமன்றங்களில் தனி நீதிப்பேராணை அதிகார வரம்பை உருவாக்க வர்மா குழு பரிந்துரைத்தது.\n\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
    "", "", "", "",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "D",
    "Statements 1 and 2 are correct. The Verma Committee (1999) identified existing legal provisions enforcing duties (e.g. Wildlife Act, IPC, RPA). Statement 3 is incorrect as the committee did NOT recommend creating a separate criminal writ jurisdiction against citizens.",
    "கூற்றுகள் 1 மற்றும் 2 சரியானவை. வர்மா குழு (1999) கடமைகளை அமல்படுத்தும் நிலவும் சட்ட விநிகளைச் சுட்டிக்காட்டியது. குடிமக்களுக்கு எதிராகத் தனி குற்றவியல் நீதிப்பேராணை அதிகார வரம்பை உருவாக்க பரிந்துரைக்காததால் கூற்று 3 தவறானது.",
    "Statements 1 and 2 accurately capture the mandate and findings of the Justice Verma Committee.", "கூற்றுகள் 1 மற்றும் 2 வர்மா குழுவின் நோக்கம் மற்றும் கண்டுபிடிப்புகளைச் சரியாகப் படம் பிடிக்கின்றன.",
    "Statement 3 is false; no such penal writ jurisdiction was proposed.", "அத்தகைய குற்றவியல் நீதிப்பேராணை பரிந்துரைக்கப்படாததால் கூற்று 3 தவறானது.",
    "Statement 3 is incorrect.", "கூற்று 3 தவறானது.",
    "Statements 1 and 2 are true.", "கூற்றுகள் 1 மற்றும் 2 சரியானவை.",
    "TNPSC Trap: Verma Committee highlighted that duties like respecting national flag, protecting environment, and preserving civil rights are ALREADY backed by parliamentary statutes.",
    "TNPSC பொறி: தேசியக் கொடியை மதிப்பது, சுற்றுச்சூழலைப் பாதுகாப்பது போன்ற கடமைகள் ஏற்கனவே நாடாளுமன்றச் சட்டங்களால் ஆதரிக்கப்படுகின்றன என்பதை வர்மா குழு சுட்டிக்காட்டியது.",
    "Verma Committee report led to Supreme Court directions on environmental awareness in 1998.",
    "வர்மா குழு அறிக்கை 1998-ல் சுற்றுச்சூழல் விழிப்புணர்வு பற்றிய உச்சநீதிமன்ற வழிகாட்டுதல்களுக்கு வழிவகுத்தது.",
    "Analyze", 60, "High"
))

# Q9 - Easy-Medium - Situation -> A
questions.append(create_q(
    "FD_R_009", "Easy-Medium", "Situation / Application",
    "SITUATION: A local customary council orders the ostracization of women who choose to seek higher education or employment, claiming to protect traditional male authority.\n\nQUESTION: Which Fundamental Duty under Article 51A directly refutes this council's order?",
    "சூழல்: உள்ளூர் பாரம்பரிய சபை ஒன்று, உயர்கல்வி அல்லது வேலைவாய்ப்பைத் தேடும் பெண்களை ஊரை விட்டு ஒதுக்கி வைக்க உத்தரவிட்டு, பாரம்பரிய ஆண் அதிகாரத்தைப் பாதுகாப்பதாக உரிமை கோருகிறது.\n\nகேள்வி: இந்தச் சபையின் உத்தரவை உறுப்பு 51A-ன் கீழ் எந்த அடிப்படை கடமை நேரடியாக மறுக்கிறது?",
    "", "", "", "",
    "Article 51A(e) — Duty to renounce practices derogatory to the dignity of women", "உறுப்பு 51A(e) — பெண்களின் கண்ணியத்தைக் குறைக்கும் வழக்கங்களைக் கைவிடும் கடமை",
    "Article 51A(b) — Duty to follow noble ideals of freedom struggle", "உறுப்பு 51A(b) — சுதந்திரப் போராட்ட லட்சியங்களைப் பின்பற்றும் கடமை",
    "Article 51A(f) — Duty to value composite culture", "உறுப்பு 51A(f) — கூட்டுப் பண்பாட்டை மதிக்கும் கடமை",
    "Article 51A(j) — Duty to strive towards individual excellence", "உறுப்பு 51A(j) — தனிநபர் சிறப்பை நோக்கி முயலும் கடமை",
    "A",
    "Article 51A(e) explicitly commands every citizen to promote harmony and common brotherhood and to 'renounce practices derogatory to the dignity of women'. Customary practices targeting or humiliating women violate this duty.",
    "உறுப்பு 51A(e) நல்லிணக்கத்தை வளர்க்கவும் 'பெண்களின் கண்ணியத்தைக் குறைக்கும் வழக்கங்களைக் கைவிடவும்' ஒவ்வொரு குடிமகனுக்கும் கட்டாயமாக்குகிறது. பெண்களை இலக்கு வைக்கும் வழக்கங்கள் இக்கடமையை மீறுகின்றன.",
    "Article 51A(e) contains the explicit constitutional command regarding women's dignity.", "உறுப்பு 51A(e) பெண்களின் கண்ணியம் பற்றிய அரசியலமைப்பு கட்டளையைக் கொண்டுள்ளது.",
    "Article 51A(b) concerns ideals of freedom struggle.", "உறுப்பு 51A(b) சுதந்திரப் போராட்ட லட்சியங்கள் பற்றியது.",
    "Article 51A(f) concerns composite culture, which cannot be used to justify degrading women.", "உறுப்பு 51A(f) கூட்டுப் பண்பாடு பற்றியது, பெண்களைத் தாழ்த்த இதைப் பயன்படுத்த முடியாது.",
    "Article 51A(j) concerns striving towards excellence.", "உறுப்பு 51A(j) சிறப்பினை நோக்கி முயல்வது பற்றியது.",
    "TNPSC Trap: Article 51A(e) combines TWO themes: 1. Harmony & common brotherhood, 2. Renouncing practices derogatory to dignity of women.",
    "TNPSC பொறி: உறுப்பு 51A(e) 2 கருப்பொருள்களை இணைக்கிறது: 1. நல்லிணக்கம் & பொதுச் சகோதரத்துவம், 2. பெண்களின் கண்ணியத்தைக் குறைக்கும் வழக்கங்களைக் கைவிடுதல்.",
    "Section 509 of IPC and POSH Act, 2013 operationalize the protection of women's dignity in line with Article 51A(e).",
    "IPC பிரிவு 509 மற்றும் 2013-ன் POSH சட்டம் ஆகியவை உறுப்பு 51A(e)-க்கு இணங்க பெண்களின் கண்ணியத்தைப் பாதுகாக்கின்றன.",
    "Understand", 60, "High"
))

# Q10 - Hard - Assertion & Reason -> B
questions.append(create_q(
    "FD_R_010", "Hard", "Assertion & Reason",
    "Assertion (A): In Animal Welfare Board of India v. A. Nagaraja (2014), the Supreme Court held that bulls cannot be subjected to unnecessary pain and suffering during Jallikattu.\nReason (R): Article 51A(g) enjoins a Fundamental Duty on every citizen to have compassion for living creatures, elevating animal welfare into a constitutional concern.",
    "கூற்று (A): இந்திய விலங்கு நல வாரியம் எதிராக ஏ. நாகராஜா (2014) வழக்கில், ஜல்லிக்கட்டின் போது காளைகளைத் தேவையில்லாத வலி மற்றும் துன்பத்திற்கு ஆளாக்க முடியாது என உச்சநீதிமன்றம் தீர்ப்பளித்தது.\nகாரணம் (R): உறுப்பு 51A(g) உயிரினங்களிடம் கருணை காட்டுவதை ஒவ்வொரு குடிமகனின் அடிப்படை கடமையாக விதித்து, விலங்கு நலனை அரசியலமைப்பு கவலையாக உயர்த்துகிறது.",
    "In Animal Welfare Board of India v. A. Nagaraja (2014), the Supreme Court held that bulls cannot be subjected to unnecessary pain and suffering during Jallikattu.",
    "இந்திய விலங்கு நல வாரியம் எதிராக ஏ. நாகராஜா (2014) வழக்கில், ஜல்லிக்கட்டின் போது காளைகளைத் தேவையில்லாத வலிக்கு ஆளாக்க முடியாது என உச்சநீதிமன்றம் தீர்ப்பளித்தது.",
    "Article 51A(g) enjoins a Fundamental Duty on every citizen to have compassion for living creatures, elevating animal welfare into a constitutional concern.",
    "உறுப்பு 51A(g) உயிரினங்களிடம் கருணை காட்டுவதை ஒவ்வொரு குடிமகனின் அடிப்படை கடமையாக விதித்து, விலங்கு நலனை அரசியலமைப்பு கவலையாக உயர்த்துகிறது.",
    "Both A and R are correct but R is NOT the correct explanation of A", "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல.",
    "Both A and R are correct and R is the correct explanation of A", "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்.",
    "A is correct but R is incorrect", "A சரி, ஆனால் R தவறு.",
    "A is incorrect but R is correct", "A தவறு, ஆனால் R சரி.",
    "B",
    "Both Assertion and Reason are true, and R explains A. In Nagaraja (2014), SC relied heavily on Article 51A(g) ('compassion for living creatures') to read animal rights into PCA Act 1960.",
    "கூற்று A மற்றும் காரணம் R இரண்டும் சரி, மேலும் R என்பது A-விற்கு சரியான விளக்கம். நாகராஜா வழக்கில் (2014) உறுப்பு 51A(g)-ன் 'உயிரினங்களிடம் கருணை' என்ற விதியையே உச்சநீதிமன்றம் முதன்மையாக நம்பியது.",
    "Article 51A(g) compassion clause is the exact constitutional foundation of Nagaraja (2014) ruling.", "உறுப்பு 51A(g) கருணை விதியே நாகராஜா (2014) தீர்ப்பின் அரசியலமைப்பு அடித்தளமாகும்.",
    "Reason directly explains the constitutional basis of Assertion.", "காரணம் கூற்றின் அரசியலமைப்பு அடிப்படையை நேரடியாக விளக்குகிறது.",
    "Reason is factually correct as per Article 51A(g).", "காரணம் உறுப்பு 51A(g)-ன் படி சரியானது.",
    "Assertion is factually true as per 2014 SC judgment.", "கூற்று 2014 உச்சநீதிமன்ற தீர்ப்பின் படி சரியானது.",
    "TNPSC Trap: Article 51A(g) protects 4 natural elements (forests, lakes, rivers, wildlife) AND mandates 'compassion for living creatures'.",
    "TNPSC பொறி: உறுப்பு 51A(g) 4 இயற்கை கூறுகளைப் பாதுகாப்பதுடன் 'உயிரினங்களிடம் கருணை காட்டுவதையும்' கட்டாயமாக்குகிறது.",
    "The Tamil Nadu Assembly later passed the Prevention of Cruelty to Animals (Tamil Nadu Amendment) Act, 2017 to permit regulated Jallikattu.",
    "சீர்படுத்தப்பட்ட ஜல்லிக்கட்டை அனுமதிக்கத் தமிழ்நாடு சட்டமன்றம் 2017-ல் திருத்தச் சட்டத்தை இயற்றியது.",
    "Analyze", 60, "High"
))

# Q11 - Medium - Two-Statement -> C
questions.append(create_q(
    "FD_R_011", "Medium", "Two-Statement Reasoning",
    "Consider the following statements regarding Article 51A(c) ('Sovereignty, Unity and Integrity of India'):\n\n1. Article 51A(c) places an affirmative duty on citizens to uphold and protect sovereignty, unity, and integrity of India.\n2. Upholding sovereignty is primarily a legal-constitutional duty, while protecting unity and integrity is a social, territorial, and psychological commitment.\n\nWhich of the statement(s) given above is/are correct?",
    "உறுப்பு 51A(c) ('இந்தியாவின் இறையாண்மை, ஒற்றுமை மற்றும் ஒருமைப்பாடு') பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n\n1. உறுப்பு 51A(c) இந்தியாவின் இறையாண்மை, ஒற்றுமை மற்றும் ஒருமைப்பாட்டைப் பேணிப் பாதுகாக்கும் கடமையைச் சுமத்துகிறது.\n2. இறையாண்மையைப் பேணுவது முதன்மையாகச் சட்ட-அரசியலமைப்பு கடமையாகும், அதே வேளையில் ஒற்றுமை மற்றும் ஒருமைப்பாட்டைப் பாதுகாப்பது சமூக, பிராந்திய மற்றும் உளவியல் கடமையாகும்.\n\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானவை?",
    "", "", "", "",
    "1 only", "1 மட்டும்",
    "2 only", "2 மட்டும்",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "Neither 1 nor 2", "எதுவும் இல்லை",
    "C",
    "Both statements are correct. Article 51A(c) is unique in combining political sovereignty with territorial and emotional integrity of the nation.",
    "இரண்டு கூற்றுகளும் சரியானவை. உறுப்பு 51A(c) அரசியல் இறையாண்மையை நாட்டின் பிராந்திய மற்றும் உணர்வுப்பூர்வ ஒருமைப்பாட்டுடன் இணைப்பதில் தனித்துவமானது.",
    "Statement 1 is factually correct as per Article 51A(c).", "கூற்று 1 உறுப்பு 51A(c)-ன் படி சரியானது.",
    "Statement 2 accurately distinguishes constitutional sovereignty from social/territorial integrity.", "கூற்று 2 அரசியலமைப்பு இறையாண்மையைச் சமூக/பிராந்திய ஒருமைப்பாட்டிலிருந்து சரியாக வேறுபடுத்துகிறது.",
    "Both 1 and 2 are true.", "1 மற்றும் 2 இரண்டும் சரியானவை.",
    "Neither is false.", "எதுவும் தவறல்ல.",
    "TNPSC Trap: Sovereignty, Unity, and Integrity are also mentioned in the Preamble (as amended by 42nd CAA, 1976).",
    "TNPSC பொறி: இறையாண்மை, ஒற்றுமை மற்றும் ஒருமைப்பாடு ஆகியவை முகப்புரையிலும் (42வது திருத்தம் 1976-ன் படி) குறிப்பிடப்பட்டுள்ளன.",
    "Section 153B of IPC enforces Article 51A(c) by penalizing assertions prejudicial to national integration.",
    "தேசிய ஒருமைப்பாட்டிற்கு எதிரான கருத்துகளைத் தண்டிப்பதன் மூலம் IPC பிரிவு 153B உறுப்பு 51A(c)-ஐ அமல்படுத்துகிறது.",
    "Understand", 60, "High"
))

# Q12 - Medium - Situation -> D
questions.append(create_q(
    "FD_R_012", "Medium", "Situation / Application",
    "SITUATION: During a political bandh, protestors burn public transport buses and destroy railway station property to register their grievance against government policies.\n\nQUESTION: Applying constitutional reasoning and Supreme Court guidelines (In Re Destruction of Public Property, 2009), which Fundamental Duty is breached and what is the legal liability?",
    "சூழல்: அரசியல் பந்த் போராட்டத்தின் போது, அரசு கொள்கைகளுக்கு எதிர்ப்பு தெரிவிக்கப் போராட்டக்காரர்கள் பொதுப் பேருந்துகளைக் கொளுத்தி, ரயில் நிலையச் சொத்துக்களைச் சேதப்படுத்துகிறார்கள்.\n\nகேள்வி: அரசியலமைப்பு பகுப்பாய்வு மற்றும் உச்சநீதிமன்ற வழிகாட்டுதல்களின்படி (பொதுச் சொத்து சேத வழக்கு, 2009), எந்த அடிப்படை கடமை மீறப்படுகிறது மற்றும் சட்டப்பூர்வ பொறுப்பு என்ன?",
    "", "", "", "",
    "Article 51A(d) is breached; protesters must be forcibly drafted into mandatory military service.", "உறுப்பு 51A(d) மீறப்படுகிறது; போராட்டக்காரர்கள் கட்டாய ராணுவ சேவையில் சேர்க்கப்பட வேண்டும்.",
    "Article 51A(h) is breached; protesters lose their right to vote permanently.", "உறுப்பு 51A(h) மீறப்படுகிறது; போராட்டக்காரர்கள் தங்கள் வாக்களிக்கும் உரிமையை நிரந்தரமாக இழக்கிறார்கள்.",
    "Article 51A(a) is breached; public buses are national symbols under the Constitution.", "உறுப்பு 51A(a) மீறப்படுகிறது; பொதுப் பேருந்துகள் தேசிய சின்னங்களாகும்.",
    "Article 51A(i) is breached; citizens violate duty to safeguard public property and abjure violence, making organizers liable for financial compensation.", "உறுப்பு 51A(i) மீறப்படுகிறது; பொதுச் சொத்தைப் பாதுகாக்கவும் வன்முறையைக் கைவிடவும் உள்ள கடமை மீறப்படுவதால், அமைப்பாளர்கள் நிதி இழப்பீடு வழங்கப் பொறுப்பாவார்கள்.",
    "D",
    "Article 51A(i) commands citizens 'to safeguard public property and to abjure violence'. In 2009, SC framed guidelines making organizers of violent protests financially liable for public property damage.",
    "உறுப்பு 51A(i) 'பொதுச் சொத்தைப் பாதுகாக்கவும் வன்முறையைக் கைவிடவும்' கட்டளையிடுகிறது. 2009-ல் வன்முறைப் போராட்ட அமைப்பாளர்கள் பொதுச் சொத்து சேதத்திற்கு நிதி இழப்பீடு வழங்கப் பொறுப்பாவார்கள் என உச்சநீதிமன்றம் வழிகாட்டுதல்களை உருவாக்கியது.",
    "Article 51A(i) covers safeguarding public property and abjuring violence.", "உறுப்பு 51A(i) பொதுச் சொத்தைப் பாதுகாத்தல் மற்றும் வன்முறையைக் கைவிடுதலை உள்ளடக்கியது.",
    "Article 51A(d) deals with national defense, not internal protest riots.", "உறுப்பு 51A(d) தேசப் பாதுகாப்பு பற்றியது, உள்நாட்டுப் போராட்டக் கலவரங்கள் பற்றியது அல்ல.",
    "Article 51A(h) deals with scientific temper, not property destruction.", "உறுப்பு 51A(h) அறிவியல் மனப்பான்மை பற்றியது.",
    "Public buses are public property under 51A(i), not national symbols under 51A(a).", "பொதுப் பேருந்துகள் 51A(i)-ன் கீழ் பொதுச் சொத்துக்கள், 51A(a)-ன் கீழ் தேசிய சின்னங்கள் அல்ல.",
    "TNPSC Trap: Article 51A(i) contains two complementary mandates: 1. Safeguard public property, 2. Abjure (renounce) violence.",
    "TNPSC பொறி: உறுப்பு 51A(i) இரண்டு நிரப்பு கட்டளைகளைக் கொண்டுள்ளது: 1. பொதுச் சொத்தைப் பாதுகாத்தல், 2. வன்முறையைக் கைவிடுதல்.",
    "Prevention of Damage to Public Property Act, 1984 acts as the statutory enforcer of Article 51A(i).",
    "1984-ன் பொதுச் சொத்து சேதத் தடுப்புச் சட்டம் உறுப்பு 51A(i)-ன் சட்டப்பூர்வ அமலாக்க அதிகாரியாகச் செயல்படுகிறது.",
    "Understand", 60, "High"
))

# Q13 - Medium - Three-Statement -> A
questions.append(create_q(
    "FD_R_013", "Medium", "Three-Statement Reasoning",
    "Consider the following statements regarding Article 51A(f) ('Composite Culture'):\n\n1. Article 51A(f) obligates citizens to value and preserve the rich heritage of India's 'composite culture'.\n2. 'Composite culture' refers exclusively to ancient Vedic literature, excluding medieval and modern syncretic traditions.\n3. Article 51A(f) complements minority cultural rights under Articles 29 and 30 by encouraging national cross-cultural respect.\n\nWhich of the statements given above are correct?",
    "உறுப்பு 51A(f) ('கூட்டுப் பண்பாடு') பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n\n1. உறுப்பு 51A(f) இந்தியாவின் 'கூட்டுப் பண்பாட்டின்' வளமான பாரம்பரியத்தைப் போற்றிப் பேணக் குடிமக்களுக்குக் கடமையாக்குகிறது.\n2. 'கூட்டுப் பண்பாடு' என்பது இடைக்கால மற்றும் நவீன கூட்டுப் பாரம்பரியங்களைத் தவிர்த்து, பண்டைய வைதீக இலக்கியங்களை மட்டுமே குறிக்கிறது.\n3. உறுப்பு 51A(f) கலாச்சார மரியாதையை ஊக்குவிப்பதன் மூலம் உறுப்புகள் 29 மற்றும் 30-ன் கீழ் உள்ள சிறுபான்மையினர் பண்பாட்டு உரிமைகளுக்கு நிரப்பியாக அமைகிறது.\n\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
    "", "", "", "",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "A",
    "Statements 1 and 3 are correct. 'Composite culture' (Ganga-Jamuni tehzeeb) reflects the synthesis of diverse regional, linguistic, and religious streams. Restricting it exclusively to ancient Vedic literature (statement 2) is incorrect.",
    "கூற்றுகள் 1 மற்றும் 3 சரியானவை. 'கூட்டுப் பண்பாடு' என்பது பல்வேறு பிராந்திய, மொழி மற்றும் மதச் சேர்க்கையின் கலவையாகும். அதை வைதீக இலக்கியங்களுக்கு மட்டுமே எல்லைப்படுத்துவது (கூற்று 2) தவறானது.",
    "Statements 1 and 3 correctly describe composite culture and its constitutional link with Art 29/30.", "கூற்றுகள் 1 மற்றும் 3 கூட்டுப் பண்பாட்டையும் உறுப்புகள் 29/30 உடனான அதன் தொடர்பையும் சரியாக விவரிக்கின்றன.",
    "Statement 2 is false because composite culture includes all historical streams (Buddhist, Jain, Islamic, Bhakti, Sufi, Western, etc.).", "கூட்டுப் பண்பாடு அனைத்து வரலாற்று நீரோட்டங்களையும் உள்ளடக்கியது என்பதால் கூற்று 2 தவறானது.",
    "Statement 2 is incorrect.", "கூற்று 2 தவறானது.",
    "Statement 2 is false.", "கூற்று 2 தவறானது.",
    "TNPSC Trap: 'Composite culture' in 51A(f) mirrors the term 'composite culture' used in Article 351 (development of Hindi language).",
    "TNPSC பொறி: 51A(f)-ல் உள்ள 'கூட்டுப் பண்பாடு' எனும் சொல் உறுப்பு 351-ல் (ஹிந்தி மொழி வளர்ச்சி) பயன்படுத்தப்பட்ட சொல்லோடு ஒத்துள்ளது.",
    "Article 51A(f) reinforces constitutional secularism and pluralism.",
    "உறுப்பு 51A(f) அரசியலமைப்பு மதச்சார்பின்மை மற்றும் பன்முகத்தன்மையை வலுப்படுத்துகிறது.",
    "Analyze", 60, "High"
))

# Q14 - Hard - Assertion & Reason -> B
questions.append(create_q(
    "FD_R_014", "Hard", "Assertion & Reason",
    "Assertion (A): The 44th Constitutional Amendment Act, 1978 retained Part IVA (Fundamental Duties) completely intact despite repealing many 42nd Amendment changes.\nReason (R): The Janata Party government recognized that civic duties promoting national unity and constitutional discipline are non-partisan national values.",
    "கூற்று (A): 44வது அரசியலமைப்பு திருத்தச் சட்டம் (1978) 42வது திருத்தத்தின் பல மாற்றங்களை ரத்து செய்தபோதிலும் பகுதி IVA-வை (அடிப்படை கடமைகள்) முழுமையாகத் தக்கவைத்துக் கொண்டது.\nகாரணம் (R): தேசிய ஒருமைப்பாடு மற்றும் அரசியலமைப்பு ஒழுங்கை ஊக்குவிக்கும் குடிமைப் பொறுப்புகள் கட்சி அரசியல் கடந்த தேசிய மதிப்புகள் என்பதை ஜனதா கட்சி அரசு அங்கீகரித்தது.",
    "The 44th Constitutional Amendment Act, 1978 retained Part IVA (Fundamental Duties) completely intact despite repealing many 42nd Amendment changes.",
    "44வது அரசியலமைப்பு திருத்தச் சட்டம் (1978) 42வது திருத்தத்தின் பல மாற்றங்களை ரத்து செய்தபோதிலும் பகுதி IVA-வை முழுமையாகத் தக்கவைத்துக் கொண்டது.",
    "The Janata Party government recognized that civic duties promoting national unity and constitutional discipline are non-partisan national values.",
    "தேசிய ஒருமைப்பாடு மற்றும் அரசியலமைப்பு ஒழுங்கை ஊக்குவிக்கும் குடிமைப் பொறுப்புகள் கட்சி அரசியல் கடந்த தேசிய மதிப்புகள் என்பதை ஜனதா கட்சி அரசு அங்கீகரித்தது.",
    "Both A and R are correct but R is NOT the correct explanation of A", "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல.",
    "Both A and R are correct and R is the correct explanation of A", "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்.",
    "A is correct but R is incorrect", "A சரி, ஆனால் R தவறு.",
    "A is incorrect but R is correct", "A தவறு, ஆனால் R சரி.",
    "B",
    "Both Assertion and Reason are true, and R explains A. While the 44th CAA reversed Emergency era anti-democratic changes, it retained Part IVA because Fundamental Duties were universally acknowledged as vital civic responsibilities.",
    "கூற்று A மற்றும் காரணம் R இரண்டும் சரி, மேலும் R என்பது A-விற்கு சரியான விளக்கம். 44வது திருத்தம் அவசரநிலை கால மாற்றங்களை ரத்து செய்தபோதிலும், அடிப்படை கடமைகள் முக்கியமான குடிமைப் பொறுப்புகளாக ஏற்றுக்கொள்ளப்பட்டதால் பகுதி IVA தக்கவைக்கப்பட்டது.",
    "44th CAA retained Part IVA intact, and R correctly explains the bipartisan acceptance of civic duties.", "44வது திருத்தம் பகுதி IVA-வை தக்கவைத்தது, மேலும் R குடிமைப் பொறுப்புகளின் ஏற்பை சரியாக விளக்குகிறது.",
    "Reason directly explains why Part IVA survived the political change of 1977-78.", "1977-78 அரசியல் மாற்றத்திலும் பகுதி IVA ஏன் தப்பித்தது என்பதை காரணம் நேரடியாக விளக்குகிறது.",
    "Reason is historically accurate.", "காரணம் வரலாற்று ரீதியாக சரியானது.",
    "Assertion is factually true under 44th CAA 1978.", "44வது திருத்தம் 1978-ன் படி கூற்று சரியானது.",
    "TNPSC Trap: 44th CAA modified DPSP Article 38 by adding clause (2) (reducing inequalities), but did NOT touch Part IVA.",
    "TNPSC பொறி: 44வது திருத்தம் DPSP உறுப்பு 38(2)-ஐச் சேர்த்தது, ஆனால் பகுதி IVA-வை தொடவில்லை.",
    "This shows that Fundamental Duties enjoy unanimous cross-party constitutional legitimacy.",
    "இது அடிப்படை கடமைகள் அனைத்துக் கட்சிகளாலும் ஏற்றுக்கொள்ளப்பட்ட அரசியலமைப்புச் செல்லுபடியைப் பெற்றுள்ளன என்பதைக் காட்டுகிறது.",
    "Analyze", 60, "High"
))

# Q15 - Hard - Situation -> C
questions.append(create_q(
    "FD_R_015", "Hard", "Situation / Application",
    "SITUATION: A student association challenges academic excellence standards and entrance cut-offs in super-speciality medical education, arguing that merit criteria conflict with social welfare principles.\n\nQUESTION: Applying the Supreme Court ruling in AIIMS Students Union v. AIIMS (2002), how does Article 51A(j) govern this issue?",
    "சூழல்: மருத்துவ மேல்-சிறப்பு படிப்புகளில் கல்வித் தகுதி நிலைகள் மற்றும் நுழைவு மதிப்பெண்களை மாணவர் சங்கம் ஒன்று எதிர்த்து, தகுதி நிலைகள் சமூக நலக் கோட்பாடுகளுக்கு முரணானவை என்று வாதாடுகிறது.\n\nகேள்வி: AIIMS மாணவர் சங்கம் எதிராக AIIMS (2002) வழக்கின் உச்சநீதிமன்றத் தீர்ப்பைப் பயன்படுத்தினால், உறுப்பு 51A(j) இச்சிக்கலை எவ்வாறு நிர்வகிக்கிறது?",
    "", "", "", "",
    "Article 51A(j) commands the State to abolish entrance examinations in higher education.", "உறுப்பு 51A(j) உயர்கல்வியில் நுழைவுத் தேர்வுகளை ரத்து செய்ய அரசைப் பணிக்கிறது.",
    "Article 51A(j) applies exclusively to international sports events, not academic admissions.", "உறுப்பு 51A(j) சர்வதேச விளையாட்டு நிகழ்வுகளுக்கு மட்டுமே பொருந்தும், கல்விச் சேர்க்கைகளுக்கு அல்ல.",
    "Article 51A(j) obligates citizens and State to strive towards excellence in all spheres, meaning institutional merit and super-speciality excellence cannot be completely sacrificed.", "உறுப்பு 51A(j) அனைத்துத் துறைகளிலும் சிறப்பினை நோக்கி முயலக் குடிமக்களுக்கும் அரசுக்கும் கடமையாக்குகிறது, எனவே நிறுவனத் தகுதி மற்றும் மேல்-சிறப்பு தகுதியை முழுமையாகத் தியாகம் செய்ய முடியாது.",
    "Article 51A(j) grants courts power to automatically cancel university degrees of low-performing students.", "உறுப்பு 51A(j) குறைந்த செயல்திறன் கொண்ட மாணவர்களின் பல்கலைக்கழகப் பட்டங்களை ரத்து செய்ய நீதிமன்றங்களுக்கு அதிகாரமளிக்கிறது.",
    "C",
    "In AIIMS Students Union (2002), Supreme Court held that Fundamental Duties under Article 51A(j) ('strive towards excellence') are as important as Fundamental Rights; excellence in super-specialities cannot be completely overlooked.",
    "AIIMS மாணவர் சங்க வழக்கில் (2002), உறுப்பு 51A(j)-ன் கீழ் உள்ள அடிப்படை கடமை ('சிறப்பினை நோக்கி முயலுதல்') அடிப்படை உரிமைகளைப் போலவே முக்கியமானது என்றும் மேல்-சிறப்பு படிப்புகளில் தகுதியைப் புறக்கணிக்க முடியாது என்றும் உச்சநீதிமன்றம் கூறியது.",
    "Art 51A(j) excellence clause mandates preserving standards in super-specialities.", "உறுப்பு 51A(j) சிறப்பினை நோக்கிய விதி மேல்-சிறப்பு படிப்புகளில் தரத்தைப் பேணுவதைக் கட்டாயமாக்குகிறது.",
    "Art 51A(j) promotes excellence, not abolition of standards.", "உறுப்பு 51A(j) சிறப்பினை ஊக்குவிக்கிறது, தகுதியை ரத்து செய்யாது.",
    "Art 51A(j) applies to ALL spheres of individual and collective activity.", "உறுப்பு 51A(j) தனிநபர் மற்றும் கூட்டுச் செயல்பாடுகளின் அனைத்துத் துறைகளுக்கும் பொருந்தும்.",
    "Art 51A(j) is a constitutional duty, not an administrative degree cancellation authorization.", "உறுப்பு 51A(j) அரசியலமைப்பு கடமையாகும், பட்டங்களை ரத்து செய்யும் அதிகாரமல்ல.",
    "TNPSC Trap: Article 51A(j) covers BOTH individual activity AND collective activity.",
    "TNPSC பொறி: உறுப்பு 51A(j) தனிநபர் செயல்பாடு மற்றும் கூட்டுச் செயல்பாடு இரண்டையும் உள்ளடக்கியது.",
    "AIIMS Students Union case affirmed that Fundamental Duties are equal in weight to Fundamental Rights.",
    "AIIMS மாணவர் சங்க வழக்கு அடிப்படை கடமைகள் அடிப்படை உரிமைகளுக்கு இணையான எடை கொண்டவை என்பதை உறுதிப்படுத்தியது.",
    "Analyze", 60, "High"
))

# Q16 - Easy-Medium - Two-Statement -> D
questions.append(create_q(
    "FD_R_016", "Easy-Medium", "Two-Statement Reasoning",
    "Consider the following statements regarding Article 51A(b) ('Cherish noble ideals of freedom struggle'):\n\n1. Article 51A(b) requires citizens to cherish and follow the noble ideals that inspired the national struggle for freedom (such as non-violence, secularism, democracy, and equality).\n2. Article 51A(b) mandates that every citizen must become an active registered member of a political party.\n\nWhich of the statement(s) given above is/are correct?",
    "உறுப்பு 51A(b) ('சுதந்திரப் போராட்ட லட்சியங்களைப் பேணுதல்') பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n\n1. உறுப்பு 51A(b) நமது தேசிய சுதந்திரப் போராட்டத்திற்கு ஊக்கமளித்த உயரிய லட்சியங்களை (அகிம்சை, மதச்சார்பின்மை, ஜனநாயகம், சமத்துவம் போன்றவை) பேணிப் பின்பற்றுரக் குடிமக்களைக் கேட்கிறது.\n2. உறுப்பு 51A(b) ஒவ்வொரு குடிமகனும் ஒரு அரசியல் கட்சியின் பதிவுசெய்த உறுப்பினராக மாற வேண்டும் என்று கட்டாயமாக்குகிறது.\n\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானவை?",
    "", "", "", "",
    "2 only", "2 மட்டும்",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "Neither 1 nor 2", "எதுவும் இல்லை",
    "1 only", "1 மட்டும்",
    "D",
    "Statement 1 is correct. Article 51A(b) inspires moral adherence to freedom struggle values. Statement 2 is false; there is no constitutional mandate requiring political party membership.",
    "கூற்று 1 சரி. உறுப்பு 51A(b) சுதந்திரப் போராட்ட மதிப்புகளைப் பின்பற்ற ஊக்கமளிக்கிறது. அரசியல் கட்சி உறுப்பினராவதை அரசியலமைப்பு கட்டாயமாக்காததால் கூற்று 2 தவறானது.",
    "Statement 1 correctly describes the moral scope of Article 51A(b).", "கூற்று 1 உறுப்பு 51A(b)-ன் தத்துவார்த்த எல்லையைச் சரியாக விவரிக்கிறது.",
    "Statement 2 is absurd and constitutionally false.", "அரசியல் கட்சி உறுப்பினர் கட்டாயமில்லை என்பதால் கூற்று 2 தவறானது.",
    "Both statements are not true because statement 2 is false.", "கூற்று 2 தவறானது என்பதால் இரண்டும் சரி என்பது தவறாகும்.",
    "Statement 1 is true.", "கூற்று 1 சரியானது.",
    "TNPSC Trap: Article 51A(b) is classified as a 'moral duty', whereas Article 51A(a) (respecting flag/anthem) is a 'civic duty'.",
    "TNPSC பொறி: உறுப்பு 51A(b) 'தர்மக் கடமையாக' (moral duty) வகைப்படுத்தப்படுகிறது, ஆனால் 51A(a) (கொடி/கீதம் மதிப்பீடு) 'குடிமைக் கடமையாகும்' (civic duty).",
    "Nobel ideals of freedom struggle form the inspirational foundation of Part III, IV, and IVA.",
    "சுதந்திரப் போராட்ட லட்சியங்களே பகுதிகள் III, IV மற்றும் IVA-ன் உத்வேக அடித்தளமாகும்.",
    "Understand", 60, "High"
))

# Q17 - Hard - Situation -> A
questions.append(create_q(
    "FD_R_017", "Hard", "Situation / Application",
    "SITUATION: During a national crisis or armed conflict, Parliament passes a law requiring civilian doctors and engineers to render compulsory temporary service for national defense. A doctor refuses, claiming forced labor is prohibited under Article 23(1).\n\nQUESTION: How does the Constitution resolve this conflict under Article 51A(d) and Article 23(2)?",
    "சூழல்: தேசிய நெருக்கடி அல்லது ஆயுதமேந்திய மோதலின் போது, தேசப் பாதுகாப்பிற்காகத் தற்காலிக சேவை செய்யக் குடிமக்களான மருத்துவர்கள் மற்றும் பொறியாளர்களைக் கட்டாயப்படுத்தும் சட்டத்தை நாடாளுமன்றம் இயற்றுகிறது. மருத்துவர் ஒருவர் உறுப்பு 23(1)-ன் கீழ் கட்டாய வேலை தடை செய்யப்பட்டுள்ளது எனக் கூறி மறுக்கிறார்.\n\nகேள்வி: உறுப்பு 51A(d) மற்றும் உறுப்பு 23(2)-ன் கீழ் அரசியலமைப்பு இச்சிடுக்கை எவ்வாறு தீர்க்கிறது?",
    "", "", "", "",
    "The refusal is invalid because Article 51A(d) commands citizens to render national service when called upon, and Article 23(2) explicitly permits the State to impose compulsory service for public purposes.", "உறுப்பு 51A(d) தேச சேவை செய்யக் கட்டளையிடுகிறது, மேலும் உறுப்பு 23(2) பொது நோக்கங்களுக்காகக் கட்டாய சேவையை விதிக்க அரசை வெளிப்படையாக அனுமதிப்பதால் மறுப்பு செல்லாது.",
    "The refusal is valid because compulsory service is strictly prohibited as forced labor under Article 23(1) without any exception.", "எந்தவொரு விதிவிலக்கும் இன்றி உறுப்பு 23(1)-ன் கீழ் கட்டாய வேலை தடை செய்யப்பட்டுள்ளதால் மறுப்பு செல்லுபடியாகும்.",
    "The refusal is valid because Fundamental Duties apply only during Internal Emergency proclaimed under Article 352.", "உறுப்பு 352-ன் கீழ் அவசரநிலை அறிவிக்கப்படும் போது மட்டுமே அடிப்படை கடமைகள் பொருந்தும் என்பதால் மறுப்பு செல்லுபடியாகும்.",
    "The refusal is invalid because Article 51A(d) grants military officers power to execute non-compliant citizens.", "உறுப்பு 51A(d) ராணுவத்திற்கு மரண தண்டனை அதிகாரமளிப்பதால் மறுப்பு செல்லாது.",
    "A",
    "The refusal is invalid. Article 51A(d) commands citizens 'to defend the country and render national service when called upon to do so'. Furthermore, Article 23(2) specifically exempts the State from Article 23(1) when imposing compulsory service for public purposes (without discrimination on grounds of religion, race, caste, or class).",
    "மறுப்பு செல்லாது. உறுப்பு 51A(d) 'தேசத்தைப் பாதுகாக்கவும் தேவைப்படும் போது தேசிய சேவையாற்றவும்' குடிமக்களுக்குக் கட்டளையிடுகிறது. மேலும், பொது நோக்கங்களுக்காகக் கட்டாய சேவை விதிக்கும் போது உறுப்பு 23(2) அரசை உறுப்பு 23(1) தடையிலிருந்து வெளிப்படையாக விலக்குகிறது.",
    "Art 51A(d) duty read with Art 23(2) exception constitutionalizes compulsory national service.", "உறுப்பு 51A(d) கடமை மற்றும் 23(2) விதிவிலக்கு ஆகியவை கட்டாயத் தேசிய சேவையை அரசியலமைப்பு ரீதியாக அனுமதிக்கின்றன.",
    "Article 23(2) provides an explicit constitutional exception to compulsory public service.", "உறுப்பு 23(2) கட்டாயப் பொது சேவைக்கு வெளிப்படையான அரசியலமைப்பு விதிவிலக்கை அளிக்கிறது.",
    "Article 51A(d) applies whenever called upon by law, not only in Article 352 emergencies.", "சட்டத்தால் அழைக்கப்படும் போதெல்லாம் உறுப்பு 51A(d) பொருந்தும், 352 அவசரநிலையில் மட்டுமே அல்ல.",
    "Article 51A(d) does not grant extra-judicial execution powers.", "உறுப்பு 51A(d) சட்டத்திற்குப் புறம்பான தண்டனை அதிகாரங்களை அளிக்காது.",
    "TNPSC Trap: Article 23(2) permits compulsory service for public purposes, but prohibits discrimination based ON RELIGION, RACE, CASTE OR CLASS (or any of them).",
    "TNPSC பொறி: உறுப்பு 23(2) பொது நோக்கத்திற்கான கட்டாய சேவையை அனுமதிக்கிறது, ஆனால் மதம், இனம், சாதி அல்லது வகுப்பு அடிப்படையில் பாகுபாடு காட்டுவதைத் தடை செய்கிறது.",
    "Article 51A(d) embodies the principle of civic participation in national defense.", "உறுப்பு 51A(d) தேசப் பாதுகாப்பில் குடிமக்களின் பங்களிப்புக் கோட்பாட்டை வெளிப்படுத்துகிறது.",
    "Analyze", 60, "High"
))

# Q18 - Medium - Three-Statement -> B
questions.append(create_q(
    "FD_R_018", "Medium", "Three-Statement Reasoning",
    "Consider the following statements regarding the National Commission to Review the Working of the Constitution (NCRWC / Venkatachaliah Commission, 2002) recommendations on Fundamental Duties:\n\n1. NCRWC recommended adding a duty to vote in elections and actively participate in democratic process.\n2. NCRWC recommended adding a duty to pay taxes honestly and promptly.\n3. All recommendations of NCRWC regarding new Fundamental Duties were enacted by Parliament in the 86th Amendment Act, 2002.\n\nWhich of the statements given above are correct?",
    "அடிப்படை கடமைகள் பற்றிய அரசியலமைப்பு செயல்பாட்டை மறுஆய்வு செய்வதற்கான தேசிய ஆணையத்தின் (NCRWC / வெங்கடாசலய்யா ஆணையம், 2002) பரிந்துரைகள் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n\n1. தேர்தலில் வாக்களிக்கவும் ஜனநாயகச் செயல்பாட்டில் பங்கேற்கவும் ஒரு புதிய கடமையைச் சேர்க்க NCRWC பரிந்துரைத்தது.\n2. நேர்மையாகவும் உடனுக்குடனும் வரி செலுத்தும் கடமையைச் சேர்க்க NCRWC பரிந்துரைத்தது.\n3. புதிய அடிப்படை கடமைகள் பற்றிய NCRWC-ன் அனைத்துப் பரிந்துரைகளும் 2002-ன் 86வது திருத்தச் சட்டம் மூலம் நாடாளுமன்றத்தால் இயற்றப்பட்டன.\n\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
    "", "", "", "",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "B",
    "Statements 1 and 2 are correct. NCRWC (2002) recommended adding duty to vote, pay taxes, and foster family values. However, statement 3 is false because Parliament did NOT enact NCRWC's recommended new duties; 86th CAA added ONLY the 11th duty [Art 51A(k)] regarding education.",
    "கூற்றுகள் 1 மற்றும் 2 சரியானவை. வாக்களிக்கும் கடமை, வரி செலுத்தும் கடமை ஆகியவற்றைச் சேர்க்க NCRWC பரிந்துரைத்தது. ஆனால் 86வது திருத்தம் கல்வியைப் பற்றிய 11வது கடமையை [51A(k)] மட்டுமே சேர்த்தது, NCRWC பரிந்துரைகளைச் சேர்க்கவில்லை என்பதால் கூற்று 3 தவறானது.",
    "Statements 1 and 2 accurately state NCRWC proposals.", "கூற்றுகள் 1 மற்றும் 2 NCRWC பரிந்துரைகளைச் சரியாகக் குறிப்பிடுகின்றன.",
    "Statement 3 is false; NCRWC proposals were NOT added to Article 51A.", "NCRWC பரிந்துரைகள் உறுப்பு 51A-ல் சேர்க்கப்படாததால் கூற்று 3 தவறானது.",
    "Statement 3 is incorrect.", "கூற்று 3 தவறானது.",
    "Statements 1 and 2 are true.", "கூற்றுகள் 1 மற்றும் 2 சரியானவை.",
    "TNPSC Trap: Both Swaran Singh Committee (1976) AND NCRWC (2002) recommended adding the 'duty to pay taxes', but it has NEVER been added to Article 51A.",
    "TNPSC பொறி: ஸ்வரன் சிங் குழு (1976) மற்றும் NCRWC (2002) ஆகிய இரண்டும் 'வரி செலுத்தும் கடமையை' பரிந்துரைத்தன, ஆனால் அது உறுப்பு 51A-ல் இதுவரை சேர்க்கப்படவில்லை.",
    "NCRWC was headed by former Chief Justice M.N. Venkatachaliah.",
    "NCRWC ஆணையத்திற்கு முன்னாள் தலைமை நீதிபதி எம்.என். வெங்கடாசலய்யா தலைமை தாங்கினார்.",
    "Analyze", 60, "High"
))

# Q19 - Hard - Assertion & Reason -> C
questions.append(create_q(
    "FD_R_019", "Hard", "Assertion & Reason",
    "Assertion (A): In Aruna Roy v. Union of India (2002), the Supreme Court upheld value-based education in school curricula based on comparative religion.\nReason (R): The Court held that imparting knowledge of universal moral values derived from religions fosters common brotherhood under Article 51A(e) and cultural harmony under Article 51A(f) without violating Article 28 secularism.",
    "கூற்று (A): அருணா ராய் எதிராக இந்திய யூனியன் (2002) வழக்கில், ஒப்பிட்டு மதக் கல்வி சார்ந்த பள்ளிப் பாடத்திட்டத்தின் மதிப்புக் கல்வியை உச்சநீதிமன்றம் உறுதி செய்தது.\nகாரணம் (R): மதங்களிலிருந்து பெறப்பட்ட உலகளாவிய தர்ம மதிப்புகளைக் கற்பிப்பது உறுப்பு 28 மதச்சார்பின்மையை மீறாமல், உறுப்பு 51A(e)-ன் கீழ் சகோதரத்துவத்தையும் உறுப்பு 51A(f)-ன் கீழ் பண்பாட்டு நல்லிணக்கத்தையும் வளர்க்கிறது என நீதிமன்றம் கூறியது.",
    "In Aruna Roy v. Union of India (2002), the Supreme Court upheld value-based education in school curricula based on comparative religion.",
    "அருணா ராய் எதிராக இந்திய யூனியன் (2002) வழக்கில், ஒப்பிட்டு மதக் கல்வி சார்ந்த பள்ளிப் பாடத்திட்டத்தின் மதிப்புக் கல்வியை உச்சநீதிமன்றம் உறுதி செய்தது.",
    "The Court held that imparting knowledge of universal moral values derived from religions fosters common brotherhood under Article 51A(e) and cultural harmony under Article 51A(f) without violating Article 28 secularism.",
    "மதங்களிலிருந்து பெறப்பட்ட உலகளாவிய தர்ம மதிப்புகளைக் கற்பிப்பது உறுப்பு 28 மதச்சார்பின்மையை மீறாமல், உறுப்பு 51A(e)-ன் கீழ் சகோதரத்துவத்தையும் உறுப்பு 51A(f)-ன் கீழ் பண்பாட்டு நல்லிணக்கத்தையும் வளர்க்கிறது என நீதிமன்றம் கூறியது.",
    "Both A and R are correct but R is NOT the correct explanation of A", "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல.",
    "A is correct but R is incorrect", "A சரி, ஆனால் R தவறு.",
    "Both A and R are correct and R is the correct explanation of A", "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்.",
    "A is incorrect but R is correct", "A தவறு, ஆனால் R சரி.",
    "C",
    "Both Assertion and Reason are true, and R explains A. In Aruna Roy (2002), SC held that 'value education' based on comparative philosophy is distinct from 'religious instruction' prohibited under Article 28(1), and fulfills Article 51A(e) and (f).",
    "கூற்று A மற்றும் காரணம் R இரண்டும் சரி, மேலும் R என்பது A-விற்கு சரியான விளக்கம். அருணா ராய் வழக்கில் (2002), ஒப்பிட்டு மதங்களின் அடிப்படையிலான 'மதிப்புக் கல்வி' என்பது உறுப்பு 28(1)-ல் தடைசெய்யப்பட்ட 'மதப் போதனையிலிருந்து' வேறுபட்டது என்றும், அது உறுப்புகள் 51A(e) மற்றும் (f)-ஐ நிறைவேற்றுகிறது என்றும் கூறப்பட்டது.",
    "Aruna Roy ruling explicitly linked value education to Article 51A(e) and (f).", "அருணா ராய் தீர்ப்பு மதிப்புக் கல்வியை உறுப்புகள் 51A(e) மற்றும் (f) உடன் நேரடியாக இணைத்தது.",
    "Reason explains why value education does not violate secularism.", "காரணம் மதிப்புக் கல்வி ஏன் மதச்சார்பின்மையை மீறவில்லை என்பதை விளக்குகிறது.",
    "Reason is factually correct.", "காரணம் சரியானது.",
    "Assertion is factually true.", "கூற்று சரியானது.",
    "TNPSC Trap: Article 28(1) prohibits 'religious instruction' in wholly state-funded schools, but does NOT prohibit teaching about religions or value education.",
    "TNPSC பொறி: உறுப்பு 28(1) அரசு நிதியுதவி பெறும் பள்ளிகளில் 'மதப் போதனையைத்' தடை செய்கிறது, ஆனால் மதங்களைப் பற்றிய கல்வியையோ மதிப்புக் கல்வியையோ தடை செய்யவில்லை.",
    "Justice M.B. Shah delivered the lead judgment in Aruna Roy (2002).",
    "அருணா ராய் வழக்கில் (2002) முதன்மைத் தீர்ப்பை நீதியரசர் எம்.பி. ஷா வழங்கினார்.",
    "Analyze", 60, "High"
))

# Q20 - Easy-Medium - Situation -> D
questions.append(create_q(
    "FD_R_020", "Easy-Medium", "Situation / Application",
    "SITUATION: A group attacks migrant workers from neighboring states and vandalizes commercial signboards in minority languages, claiming to defend local regional pride.\n\nQUESTION: Which Fundamental Duty under Article 51A is directly violated by this conduct?",
    "சூழல்: குழு ஒன்று அண்டை மாநிலங்களிலிருந்து வந்த புலம்பெயர்ந்த தொழிலாளர்களைத் தாக்கி, சிறுபான்மை மொழிகளில் உள்ள வணிகப் பெயர் பலகைகளைச் சேதப்படுத்தி, உள்ளூர் பிராந்தியப் பெருமையைப் பாதுகாப்பதாக உரிமை கோருகிறது.\n\nகேள்வி: இந்த நடவடிக்கையால் உறுப்பு 51A-ன் கீழ் எந்த அடிப்படை கடமை நேரடியாக மீறப்படுகிறது?",
    "", "", "", "",
    "Article 51A(h) — Duty to develop scientific temper", "உறுப்பு 51A(h) — அறிவியல் மனப்பான்மையை வளர்க்கும் கடமை",
    "Article 51A(k) — Duty to provide education opportunities", "உறுப்பு 51A(k) — கல்விக்கான வாய்ப்புகளை வழங்கும் கடமை",
    "Article 51A(b) — Duty to follow freedom struggle ideals", "உறுப்பு 51A(b) — சுதந்திரப் போராட்ட லட்சியங்களைப் பின்பற்றும் கடமை",
    "Article 51A(e) — Duty to promote harmony and common brotherhood transcending religious, linguistic, regional or sectional diversities", "உறுப்பு 51A(e) — மத, மொழி, பிராந்திய அல்லது பிரிவு வேறுபாடுகளைக் கடந்து நல்லிணக்கம் மற்றும் பொதுச் சகோதரத்துவத்தை வளர்க்கும் கடமை",
    "D",
    "Article 51A(e) explicitly mandates promoting harmony and common brotherhood among all people of India 'transcending religious, linguistic and regional or sectional diversities'. Attacking migrants or linguistic minorities violates this fundamental duty.",
    "உறுப்பு 51A(e) 'மத, மொழி, பிராந்திய அல்லது பிரிவு வேறுபாடுகளைக் கடந்து' நல்லிணக்கம் மற்றும் பொதுச் சகோதரத்துவத்தை வளர்க்கக் கட்டளையிடுகிறது. புலம்பெயர்ந்தோரையும் மொழிச் சிறுபான்மையினரையும் தாக்குவது இக்கடமையை மீறுகிறது.",
    "Article 51A(e) specifically targets linguistic and regional diversity harmony.", "உறுப்பு 51A(e) மொழி மற்றும் பிராந்திய நல்லிணக்கத்தைக் குறிப்பாக இலக்கு வைக்கிறது.",
    "Article 51A(h) deals with scientific temper.", "உறுப்பு 51A(h) அறிவியல் மனப்பான்மை பற்றியது.",
    "Article 51A(k) deals with child education.", "உறுப்பு 51A(k) குழந்தைகள் கல்வி பற்றியது.",
    "Article 51A(b) deals with freedom struggle ideals.", "உறுப்பு 51A(b) சுதந்திரப் போராட்ட லட்சியங்கள் பற்றியது.",
    "TNPSC Trap: Article 51A(e) lists 4 specific types of diversities to transcend: Religious, Linguistic, Regional, and Sectional.",
    "TNPSC பொறி: உறுப்பு 51A(e) கடக்க வேண்டிய 4 குறிப்பிட்ட வேறுபாடுகளைப் பட்டியலிடுகிறது: மத, மொழி, பிராந்திய மற்றும் பிரிவு வேறுபாடுகள்.",
    "IPC Section 153A penalizes promoting enmity between different groups on grounds of religion, race, place of birth, or language.",
    "IPC பிரிவு 153A மதம், இனம், பிறந்த இடம் அல்லது மொழியின் அடிப்படையில் குழுக்களிடையே பகைமையை வளர்ப்பதைத் தண்டிக்கிறது.",
    "Understand", 60, "High"
))

# Q21 - Medium - Two-Statement -> A
questions.append(create_q(
    "FD_R_021", "Medium", "Two-Statement Reasoning",
    "Consider the following statements regarding comparative constitutional law on Fundamental Duties:\n\n1. India is one of the few democratic Constitutions (along with Japan) that explicitly contains a comprehensive chapter on Fundamental Duties of citizens.\n2. Major Western democratic Constitutions such as the USA, Canada, France, and Australia included elaborate explicit chapters on Fundamental Duties in their original texts.\n\nWhich of the statement(s) given above is/are correct?",
    "அடிப்படை கடமைகள் பற்றிய ஒப்பீட்டு அரசியலமைப்புச் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n\n1. ஜப்பானுடன் சேர்த்து குடிமக்களின் அடிப்படை கடமைகள் பற்றிய விரிவான அத்தியாயத்தை வெளிப்படையாகக் கொண்டுள்ள சில ஜனநாயக அரசியலமைப்புகளில் இந்தியாவும் ஒன்றாகும்.\n2. அமெரிக்கா, கனடா, பிரான்ஸ் மற்றும் ஆஸ்திரேலியா போன்ற முக்கிய மேற்கத்திய ஜனநாயக அரசியலமைப்புகள் தங்கள் அசல் உரையில் அடிப்படை கடமைகள் பற்றிய விரிவான அத்தியாயங்களைச் சேர்த்திருந்தன.\n\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானவை?",
    "", "", "", "",
    "1 only", "1 மட்டும்",
    "2 only", "2 மட்டும்",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "Neither 1 nor 2", "எதுவும் இல்லை",
    "A",
    "Statement 1 is correct. Modern democratic Constitutions generally do not specify duties (except Japan). Major Western democracies (USA, France, Canada, Australia) do NOT contain constitutional chapters on duties. Duties are traditionally featured in socialist Constitutions (like erstwhile USSR).",
    "கூற்று 1 சரி. நவீன ஜனநாயக அரசியலமைப்புகள் பொதுவாகக் கடமைகளைக் குறிப்பிடுவதில்லை (ஜப்பான் தவிர). அமெரிக்கா, பிரான்ஸ், கனடா போன்ற மேற்கத்திய அரசியலமைப்புகளில் கடமைகள் பற்றிய அத்தியாயங்கள் இல்லை என்பதால் கூற்று 2 தவறானது.",
    "Statement 1 is factually accurate regarding India and Japan.", "இந்தியா மற்றும் ஜப்பான் பற்றிய கூற்று 1 வரலாற்று ரீதியாக சரியானது.",
    "Statement 2 is false because Western democracies rely on common law/statutes rather than constitutional duty chapters.", "மேற்கத்திய நாடுகளில் அரசியலமைப்பு கடமைகள் அத்தியாயம் இல்லாததால் கூற்று 2 தவறானது.",
    "Statement 2 is false.", "கூற்று 2 தவறானது.",
    "Statement 1 is true.", "கூற்று 1 சரியானது.",
    "TNPSC Trap: Fundamental Duties in Part IVA were primarily inspired by the Socialist Constitution of USSR, not Western democracies.",
    "TNPSC பொறி: பகுதி IVA-ல் உள்ள அடிப்படை கடமைகள் மேற்கத்திய நாடுகளிலிருந்து அல்லாமல், சோவியத் யூனியனின் (USSR) சோசலிச அரசியலமைப்பிலிருந்து பெறப்பட்டன.",
    "Japan's Constitution (1947) is one of the rare democratic Constitutions containing citizen duties.",
    "ஜப்பானின் அரசியலமைப்பு (1947) குடிமக்களின் கடமைகளைக் கொண்டுள்ள அரிய ஜனநாயக அரசியலமைப்புகளில் ஒன்றாகும்.",
    "Understand", 60, "High"
))

# Q22 - Hard - Case Situation -> B
questions.append(create_q(
    "FD_R_022", "Hard", "Case-Based Situation",
    "SCENARIO: A state legislature passes a law banning the slaughter of cows and draft cattle to promote agriculture and animal welfare. Cattle traders challenge the ban as an infringement on their fundamental right to trade under Article 19(1)(g).\n\nQUESTION: How did the 7-judge Constitution Bench of the Supreme Court rule in State of Gujarat v. Mirzapur Moti Koreshi Kassab Jamat (2005)?",
    "சூழல்: வேளாண்மை மற்றும் விலங்கு நலனை ஊக்குவிக்க மாநில சட்டமன்றம் பசுக்கள் மற்றும் காளைகளை வதை செய்வதைத் தடை செய்யும் சட்டத்தை இயற்றுகிறது. கால்நடை வியாபாரிகள் இத்தடையை உறுப்பு 19(1)(g)-ன் கீழ் தங்களின் தொழில் சுதந்திரத்தை மீறுவதாக எதிர்த்து வழக்கு தொடர்கின்றனர்.\n\nகேள்வி: குஜராத் மாநிலம் எதிராக மிர்சாபூர் மோதி கொரேஷி கசாப் ஜமாத் (2005) வழக்கில் உச்சநீதிமன்றத்தின் 7 நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வு எவ்வாறு தீர்ப்பளித்தது?",
    "", "", "", "",
    "The Court struck down the ban because Fundamental Rights completely override non-justiciable DPSP and Fundamental Duties.", "அடிப்படை உரிமைகள் அமல்படுத்த முடியாத DPSP மற்றும் கடமைகளை விட மேலோங்குவதால் நீதிமன்றம் தடையை ரத்து செய்தது.",
    "The Court upheld the ban, holding that restrictions placed on Fundamental Rights to give effect to DPSP (Art 48) and Fundamental Duty (Art 51A(g)) are 'reasonable restrictions' under Article 19.", "DPSP (உறுப்பு 48) மற்றும் அடிப்படை கடமையை (உறுப்பு 51A(g)) நிறைவேற்ற அடிப்படை உரிமைகள் மீது விதிக்கப்படும் கட்டுப்பாடுகள் உறுப்பு 19-ன் கீழ் 'நியாயமான கட்டுப்பாடுகள்' எனக் கூறி நீதிமன்றம் தடையை உறுதி செய்தது.",
    "The Court held that Article 51A(g) applies only to national parks and wildlife sanctuaries, not to agricultural animals.", "உறுப்பு 51A(g) தேசிய பூங்காக்களுக்கு மட்டுமே பொருந்தும் எனக் கூறி நீதிமன்றம் தடையை ரத்து செய்தது.",
    "The Court held that Fundamental Duties apply only during Emergency.", "அவசரநிலையில் மட்டுமே அடிப்படை கடமைகள் பொருந்தும் என நீதிமன்றம் தீர்ப்பளித்தது.",
    "B",
    "In Mirzapur Moti Koreshi (2005), a 7-judge Bench of SC upheld the total ban on cow slaughter, ruling that restrictions on Article 19(1)(g) to enforce DPSP (Art 48) and Fundamental Duty under Article 51A(g) are constitutionally reasonable restrictions.",
    "மிர்சாபூர் மோதி கொரேஷி வழக்கில் (2005), DPSP (உறுப்பு 48) மற்றும் உறுப்பு 51A(g) கடமையை நிறைவேற்ற உறுப்பு 19(1)(g) மீது விதிக்கப்படும் கட்டுப்பாடுகள் அரசியலமைப்பு ரீதியாக நியாயமானவை எனக் கூறி 7 நீதிபதிகள் அமர்வு பசு வதைத் தடையை உறுதி செய்தது.",
    "Mirzapur Moti Koreshi judgment is a landmark precedent using Art 51A(g) to validate restrictions on Art 19(1)(g).", "மிர்சாபூர் மோதி கொரேஷி தீர்ப்பு உறுப்பு 19(1)(g) மீதான கட்டுப்பாடுகளை உறுதிப்படுத்த உறுப்பு 51A(g)-ஐப் பயன்படுத்திய முக்கிய முன்மாதிரியாகும்.",
    "The Court upheld the ban instead of striking it down.", "நீதிமன்றம் தடையை ரத்து செய்யாமல் உறுதி செய்தது.",
    "Art 51A(g) includes domestic animals and living creatures, not just wildlife sanctuaries.", "உறுப்பு 51A(g) வனவிலங்கு சரணாலயங்களை மட்டுமல்லாமல் வளர்ப்பு விலங்குகளையும் உள்ளடக்கியது.",
    "Fundamental Duties apply at all times, not just during Emergency.", "அடிப்படை கடமைகள் அவசரநிலை காலத்தில் மட்டுமல்லாமல் அனைத்து நேரங்களிலும் பொருந்தும்.",
    "TNPSC Trap: Mirzapur Moti Koreshi (2005) explicitly overruled the earlier Quareshi (1958) judgment by relying on the added Part IVA (Art 51A(g)) and 42nd Amendment.",
    "TNPSC பொறி: பகுதி IVA (உறுப்பு 51A(g)) மற்றும் 42வது திருத்தத்தை நம்பி, 1958-ன் குரேஷி தீர்ப்பை 2005-ன் மிர்சாபூர் வழக்கு வெளிப்படையாக ரத்து செய்தது.",
    "Former Chief Justice R.C. Lahoti headed the 7-judge Constitution Bench in 2005.",
    "2005-ல் 7 நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வுக்கு முன்னாள் தலைமை நீதிபதி ஆர்.சி. லஹோட்டி தலைமை தாங்கினார்.",
    "Analyze", 60, "High"
))

# Q23 - Medium - Three-Statement -> C
questions.append(create_q(
    "FD_R_023", "Medium", "Three-Statement Reasoning",
    "Consider the following statements regarding the scope and applicability of Fundamental Duties under Article 51A:\n\n1. Fundamental Duties contain both moral duties (such as cherishing freedom struggle ideals) and civic duties (such as respecting the Constitution, Flag, and Anthem).\n2. Fundamental Duties apply exclusively to citizens of India and do not extend to foreign nationals residing in India.\n3. Unlike Fundamental Rights (some of which apply to all persons including foreigners), Article 51A explicitly begins with 'It shall be the duty of every citizen of India'.\n\nWhich of the statements given above are correct?",
    "உறுப்பு 51A-ன் கீழ் உள்ள அடிப்படை கடமைகளின் எல்லை மற்றும் பயன்பாடு பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n\n1. அடிப்படை கடமைகள் தர்மக் கடமைகள் (சுதந்திரப் போராட்ட லட்சியங்களைப் பேணுதல் போன்றவை) மற்றும் குடிமைக் கடமைகள் (அரசியலமைப்பு, கொடி, கீதத்தை மதித்தல் போன்றவை) இரண்டையும் கொண்டுள்ளன.\n2. அடிப்படை கடமைகள் இந்தியக் குடிமக்களுக்கு மட்டுமே பொருந்தும், இந்தியாவில் வாழும் வெளிநாட்டு குடிமக்களுக்குப் பொருந்தாது.\n3. அடிப்படை உரிமைகளைப் போலன்றி (அவற்றில் சில வெளிநாட்டவர் உட்பட அனைவருக்கும் பொருந்தும்), உறுப்பு 51A வெளிப்படையாக 'இது இந்தியாவின் ஒவ்வொரு குடிமகனின் கடமையாகும்' என்றே தொடங்குகிறது.\n\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
    "", "", "", "",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "C",
    "All three statements are correct. Fundamental Duties distinguish moral vs civic duties, and are strictly confined to CITIZENS of India (unlike certain FRs under Art 14, 21, etc., which apply to all persons).",
    "மூன்று கூற்றுகளும் சரியானவை. அடிப்படை கடமைகள் தர்ம மற்றும் குடிமைக் கடமைகளை வேறுபடுத்துகின்றன, மேலும் அவை இந்தியக் குடிமக்களுக்கு மட்டுமே பொருந்தும் (அனைவருக்கும் பொருந்தும் உறுப்புகள் 14, 21 போன்ற சில அடிப்படை உரிமைகளைப் போலன்றி).",
    "Statement 1 is correct (moral vs civic classification).", "கூற்று 1 சரி (தர்ம vs குடிமைக் கடமை வகைப்பாடு).",
    "Statement 2 is correct (applicable only to citizens).", "கூற்று 2 சரி (குடிமக்களுக்கு மட்டுமே பொருந்தும்).",
    "Statement 3 is correct (textual phrasing of Art 51A).", "கூற்று 3 சரி (உறுப்பு 51A-ன் உரையாக்கம்).",
    "All three statements (1, 2, and 3) are true.", "மூன்று கூற்றுகளும் (1, 2, மற்றும் 3) சரியானவை.",
    "TNPSC Trap: Fundamental Rights under Articles 15, 16, 19, 29, 30 AND all Fundamental Duties under Article 51A apply ONLY to Indian citizens.",
    "TNPSC பொறி: உறுப்புகள் 15, 16, 19, 29, 30-ன் கீழ் உள்ள அடிப்படை உரிமைகள் மற்றும் உறுப்பு 51A-ன் கீழ் உள்ள அனைத்து அடிப்படை கடமைகளும் இந்தியக் குடிமக்களுக்கு மட்டுமே பொருந்தும்.",
    "Foreigners residing in India are bound by statutory laws of India, but constitutional Fundamental Duties under Part IVA apply only to citizens.",
    "இந்தியாவில் வாழும் வெளிநாட்டினர் இந்தியச் சட்டங்களுக்குக் கட்டுப்பட்டவர்கள், ஆனால் பகுதி IVA-ன் கீழ் உள்ள அரசியலமைப்பு கடமைகள் குடிமக்களுக்கு மட்டுமே பொருந்தும்.",
    "Understand", 60, "High"
))

# Q24 - Medium - Situation -> D
questions.append(create_q(
    "FD_R_024", "Medium", "Situation / Application",
    "SITUATION: A factory owner employs 10-year-old children in hazardous manufacturing and claims he is fulfilling Article 51A(k) by giving them practical vocational experience.\n\nQUESTION: Which constitutional analysis correctly invalidates the factory owner's defense?",
    "சூழல்: தொழிற்சாலை உரிமையாளர் ஒருவர் 10 வயதுக் குழந்தைகளை ஆபத்தான உற்பத்தியில் ஈடுபடுத்தி, அவர்களுக்கு நடைமுறைத் தொழிற்கல்வி அனுபவத்தை வழங்குவதன் மூலம் தான் உறுப்பு 51A(k)-ஐ நிறைவேற்றுவதாக வாதிடுகிறார்.\n\nகேள்வி: எந்த அரசியலமைப்பு பகுப்பாய்வு தொழிற்சாலை உரிமையாளரின் வாதத்தைச் சரியாக நிராகரிக்கிறது?",
    "", "", "", "",
    "Article 51A(k) applies to factory owners, but requires theoretical classroom teaching.", "உறுப்பு 51A(k) தொழிற்சாலை உரிமையாளர்களுக்குப் பொருந்தும், ஆனால் தத்துவார்த்த வகுப்பறைக் கல்வியைக் கோருகிறது.",
    "Article 51A(k) applies only to State government officers, not to private individuals.", "உறுப்பு 51A(k) அரசு அதிகாரிகளுக்கு மட்டுமே பொருந்தும், தனிநபர்களுக்கு அல்ல.",
    "Article 51A(k) permits child labor if the child is paid full adult minimum wages.", "குழந்தைக்கு முழு குறைந்தபட்ச ஊதியம் வழங்கப்பட்டால் உறுப்பு 51A(k) குழந்தை தொழிலாளரை அனுமதிக்கிறது.",
    "Article 51A(k) imposes a duty specifically on PARENTS or GUARDIANS for education (6-14 yrs), while Article 24 strictly prohibits child labor in factories; a factory owner cannot exploit children under the guise of duty.", "உறுப்பு 51A(k) பெற்றோர் அல்லது பாதுகாவலர்கள் மீது மட்டுமே கல்விக் கடமையை (6-14 வயது) விதிக்கிறது, அதே வேளையில் உறுப்பு 24 தொழிற்சாலைகளில் குழந்தைகள் தொழிலாளரைத் தடை செய்கிறது; உரிமையாளர் கடமையின் போர்வையில் குழந்தைகளைச் சுரண்ட முடியாது.",
    "D",
    "Article 51A(k) explicitly places the duty on the 'parent or guardian' to provide educational opportunities to their child aged 6-14 years. A factory owner cannot misappropriate this duty. Furthermore, Article 24 (FR) prohibits employment of children below 14 in factories/hazardous work.",
    "உறுப்பு 51A(k) 6-14 வயதுடைய குழந்தைகளுக்குக் கல்விக்கான வாய்ப்புகளை வழங்கக் 'பெற்றோர் அல்லது பாதுகாவலர்' மீது மட்டுமே கடமையை விதிக்கிறது. தொழிற்சாலை உரிமையாளர் இக்கடமையைத் தவறாகப் பயன்படுத்த முடியாது. மேலும் உறுப்பு 24 (FR) 14 வயதிற்குட்பட்ட குழந்தைகளைத் தொழிற்சாலைகளில் வேலைக்கு அமர்த்துவதைத் தடை செய்கிறது.",
    "Article 51A(k) specifies parents/guardians, while Article 24 prohibits factory child labor.", "உறுப்பு 51A(k) பெற்றோர்/பாதுகாவலர்களைக் குறிப்பிடுகிறது, உறுப்பு 24 குழந்தை தொழிலாளரைத் தடை செய்கிறது.",
    "Article 51A(k) does not apply to employers.", "உறுப்பு 51A(k) முதலாளிகளுக்குப் பொருந்தாது.",
    "Article 51A(k) applies to citizens who are parents/guardians.", "உறுப்பு 51A(k) பெற்றோராக இருக்கும் குடிமக்களுக்குப் பொருந்தும்.",
    "Child labor in hazardous work is strictly unconstitutional under Article 24 regardless of wages.", "ஊதியம் பொருட்படுத்தாமல் ஆபத்தான வேலையில் குழந்தை தொழிலாளர் உறுப்பு 24-ன் கீழ் அரசியலமைப்புக்கு முரணானது.",
    "TNPSC Trap: Distinguish Duty-Bearers! Article 21A = State Duty; Article 51A(k) = Parent/Guardian Duty.",
    "TNPSC பொறி: கடமைப் பொறுப்பாளர்களை வேறுபடுத்துங்கள்! உறுப்பு 21A = அரசின் கடமை; உறுப்பு 51A(k) = பெற்றோர்/பாதுகாவலரின் கடமை.",
    "Child Labour (Prohibition and Regulation) Act, 1986 operationalizes Article 24.",
    "1986-ன் குழந்தை தொழிலாளர் (தடை மற்றும் சீரமைப்பு) சட்டம் உறுப்பு 24-ஐ அமல்படுத்துகிறது.",
    "Analyze", 60, "High"
))

# Q25 - Medium - Assertion & Reason -> D
questions.append(create_q(
    "FD_R_025", "Medium", "Assertion & Reason",
    "Assertion (A): Part III (Fundamental Rights), Part IV (Directive Principles), and Part IVA (Fundamental Duties) form an organic constitutional triad for holistic nation-building.\nReason (R): Fundamental Rights guarantee individual liberties against State encroachment, Directive Principles guide the State toward welfare goals, and Fundamental Duties remind citizens of their responsibility to sustain both liberty and welfare.",
    "கூற்று (A): பகுதி III (அடிப்படை உரிமைகள்), பகுதி IV (DPSP) மற்றும் பகுதி IVA (அடிப்படை கடமைகள்) ஆகியவை ஒட்டுமொத்த தேசக் கட்டமைப்பிற்கான ஒருங்கிணைந்த அரசியலமைப்பு முக்கோணத்தை உருவாக்குகின்றன.\nகாரணம் (R): அடிப்படை உரிமைகள் அரசு ஆக்கிரமிப்பிற்கு எதிராகத் தனிநபர் சுதந்திரத்திற்கு உத்தரவாதம் அளிக்கின்றன, அரசு நெறிமுறைகள் அரசை நலன்புரி இலக்குகளை நோக்கி வழிகாட்டுகின்றன, மேலும் அடிப்படை கடமைகள் சுதந்திரம் மற்றும் நலன் இரண்டையும் பேணுவதற்கான தங்கள் பொறுப்பைக் குடிமக்களுக்கு நினைவூட்டுகின்றன.",
    "Part III (Fundamental Rights), Part IV (Directive Principles), and Part IVA (Fundamental Duties) form an organic constitutional triad for holistic nation-building.",
    "பகுதி III (அடிப்படை உரிமைகள்), பகுதி IV (DPSP) மற்றும் பகுதி IVA (அடிப்படை கடமைகள்) ஆகியவை ஒட்டுமொத்த தேசக் கட்டமைப்பிற்கான ஒருங்கிணைந்த அரசியலமைப்பு முக்கோணத்தை உருவாக்குகின்றன.",
    "Fundamental Rights guarantee individual liberties against State encroachment, Directive Principles guide the State toward welfare goals, and Fundamental Duties remind citizens of their responsibility to sustain both liberty and welfare.",
    "அடிப்படை உரிமைகள் அரசு ஆக்கிரமிப்பிற்கு எதிராகத் தனிநபர் சுதந்திரத்திற்கு உத்தரவாதம் அளிக்கின்றன, அரசு நெறிமுறைகள் அரசை நலன்புரி இலக்குகளை நோக்கி வழிகாட்டுகின்றன, மேலும் அடிப்படை கடமைகள் சுதந்திரம் மற்றும் நலன் இரண்டையும் பேணுவதற்கான தங்கள் பொறுப்பைக் குடிமக்களுக்கு நினைவூட்டுகின்றன.",
    "Both A and R are correct but R is NOT the correct explanation of A", "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல.",
    "A is correct but R is incorrect", "A சரி, ஆனால் R தவறு.",
    "A is incorrect but R is correct", "A தவறு, ஆனால் R சரி.",
    "Both A and R are correct and R is the correct explanation of A", "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்.",
    "D",
    "Both Assertion and Reason are true, and R explains A. Part III (FR), Part IV (DPSP), and Part IVA (FD) represent the three pillars of Indian constitutionalism: Individual Rights, State Obligations, and Citizen Responsibilities.",
    "கூற்று A மற்றும் காரணம் R இரண்டும் சரி, மேலும் R என்பது A-விற்கு சரியான விளக்கம். பகுதி III (FR), பகுதி IV (DPSP) மற்றும் பகுதி IVA (FD) ஆகியவை இந்திய அரசியலமைப்பின் மூன்று தூண்களாகும்: தனிநபர் உரிமைகள், அரசின் கடமைகள் மற்றும் குடிமக்களின் பொறுப்புகள்.",
    "Part III, IV, and IVA form the fundamental triad of Indian constitutional philosophy.", "பகுதிகள் III, IV மற்றும் IVA ஆகியவை இந்திய அரசியலமைப்புத் தத்துவத்தின் அடிப்படை முக்கோணத்தை உருவாக்குகின்றன.",
    "Reason directly explains the distinct roles of FR, DPSP, and FD in this triad.", "இந்த முக்கோணத்தில் FR, DPSP மற்றும் FD ஆகியவற்றின் குறிப்பிட்ட பங்குகளை காரணம் நேரடியாக விளக்குகிறது.",
    "Reason is factually and conceptually accurate.", "காரணம் தத்துவார்த்த ரீதியாக சரியானது.",
    "Assertion is factually true.", "கூற்று சரியானது.",
    "TNPSC Trap: Remember that Part III is Justiciable, while Part IV and Part IVA are Non-Justiciable by themselves.",
    "TNPSC பொறி: பகுதி III நீதிமன்றத்தால் அமல்படுத்தக் கூடியது, ஆனால் பகுதி IV மற்றும் பகுதி IVA ஆகியவை நேரடியாக அமல்படுத்தப்பட முடியாதவை என்பதை நினைவில் கொள்க.",
    "The Supreme Court in Minerva Mills (1980) emphasized harmony between Part III and Part IV as part of Basic Structure.",
    "மினர்வா மில்ஸ் வழக்கில் (1980) பகுதி III மற்றும் பகுதி IV இடையேயான சமநிலை அடிப்படை அமைப்பின் பகுதி என உச்சநீதிமன்றம் வலியுறுத்தியது.",
    "Analyze", 60, "High"
))

# Save to BOTH file paths to support all loader signatures
files = [
    "data/questions/polity/fundamental_duties_reasoning.json",
    "data/questions/polity/fundamental_duties_assertion_reason.json"
]

for file_path in files:
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print(f"Successfully written {len(questions)} questions to {file_path}")

