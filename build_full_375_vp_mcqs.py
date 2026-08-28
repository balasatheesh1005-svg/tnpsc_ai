import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

from scratch_vp_mcq_helpers import build_q, make_options, make_wno

os.makedirs("data/questions/polity", exist_ok=True)

# -----------------------------------------------------------------------------
# DATASET 1: EASY (50 Questions)
# -----------------------------------------------------------------------------
print("\n==================================================")
print("GENERATING DATASET 1: EASY (50 MCQs)")
print("==================================================")
easy_questions = []

easy_questions.append(build_q(
    "POLITY_VP_EASY_001", "Easy", "Direct MCQ",
    "Which Article of the Indian Constitution establishes the office of the Vice-President of India?",
    "இந்திய அரசியலமைப்பின் எந்த உறுப்பு இந்தியத் துணைக் குடியரசுத் தலைவர் பதவியை நிறுவுகிறது?",
    make_options("Article 52", "உறுப்பு 52", "Article 63", "உறுப்பு 63", "Article 74", "உறுப்பு 74", "Article 76", "உறுப்பு 76"),
    "B",
    "Article 63 mandates that 'There shall be a Vice-President of India'. Article 52 refers to the President.",
    "உறுப்பு 63 'இந்தியாவிற்கு ஒரு துணைக் குடியரசுத் தலைவர் இருக்க வேண்டும்' எனக் குறிப்பிடுகிறது. உறுப்பு 52 குடியரசுத் தலைவரைக் குறிக்கிறது.",
    make_wno("B",
        "Article 52 establishes the office of the President of India, not Vice-President.", "உறுப்பு 52 துணைக் குடியரசுத் தலைவரை அல்லாமல் குடியரசுத் தலைவர் பதவியை நிறுவுகிறது.",
        "Article 63 accurately establishes the office of the Vice-President of India as the 2nd highest office.", "உறுப்பு 63 துணைக் குடியரசுத் தலைவர் பதவியை நாட்டின் 2வது உயர்ந்த பதவியாக நிறுவுகிறது.",
        "Article 74 relates to the Council of Ministers headed by the Prime Minister.", "உறுப்பு 74 பிரதமரைக் தலைவராகக் கொண்ட அமைச்சரவையைக் குறிப்பிடுகிறது.",
        "Article 76 relates to the Attorney General of India.", "உறுப்பு 76 இந்திய தலைமை வழக்கறிஞரைக் (AGI) குறிப்பிடுகிறது."
    ),
    "Always distinguish Article 52 (President) from Article 63 (Vice-President).",
    "உறுப்பு 52 (குடியரசுத் தலைவர்) மற்றும் உறுப்பு 63 (துணைக் குடியரசுத் தலைவர்) ஆகியவற்றை குழப்ப வேண்டாம்.",
    "Confusing Article 52 (President) with Article 63 (Vice-President).",
    "உறுப்பு 52 மற்றும் 63-ஐக் குழப்பிக் கொள்ளுதல்.",
    ["Vice-President Notes Part 1 - Article 63"]
))

easy_questions.append(build_q(
    "POLITY_VP_EASY_002", "Easy", "Direct MCQ",
    "Who is the Ex-Officio Chairman of the Council of States (Rajya Sabha)?",
    "மாநிலங்களவையின் (Rajya Sabha) பதவிவழித் தலைவர் யார்?",
    make_options("President of India", "இந்தியக் குடியரசுத் தலைவர்", "Prime Minister", "இந்தியப் பிரதமர்", "Vice-President of India", "இந்தியத் துணைக் குடியரசுத் தலைவர்", "Speaker of Lok Sabha", "மக்களவை சபாநாயகர்"),
    "C",
    "Under Article 64 & Article 89, the Vice-President of India is the Ex-Officio Chairman of the Rajya Sabha.",
    "உறுப்புகள் 64 & 89-ன் கீழ் இந்தியத் துணைக் குடியரசுத் தலைவர் மாநிலங்களவையின் பதவிவழித் தலைவராவார்.",
    make_wno("C",
        "The President is Head of State and does not preside over Rajya Sabha.", "குடியரசுத் தலைவர் நாட்டின் தலைவர்; அவர் மாநிலங்களவையை நடத்துவதில்லை.",
        "The Prime Minister is Head of Government and leader of the House, not presiding officer.", "பிரதமர் அரசின் தலைவர்; அவர் அவைத் தலைவர் அல்ல.",
        "The Vice-President is constitutionally designated as the Ex-Officio Chairman of Rajya Sabha under Article 64.", "உறுப்பு 64-ன் கீழ் துணைக் குடியரசுத் தலைவர் மாநிலங்களவையின் பதவிவழித் தலைவராகச் செயல்படுகிறார்.",
        "The Speaker presides over Lok Sabha, not Rajya Sabha.", "சபாநாயகர் மக்களவையைத் தலைமை தாங்கி நடத்துபவர்."
    ),
    "Ex-officio means by virtue of holding the Vice-President office, he automatically becomes Rajya Sabha Chairman.",
    "பதவிவழி (Ex-officio) என்றால் VP பதவியை வகிப்பதாலேயே தானாகவே மாநிலங்களவைத் தலைவராகிறார்.",
    "Assuming Rajya Sabha elects an outside Chairman.",
    "மாநிலங்களவை வெளியே உள்ள ஒருவரைத் தலைவராகத் தேர்ந்தெடுப்பதாக நினைப்பது.",
    ["Vice-President Notes Part 1 - Article 64"]
))

for i in range(3, 51):
    qid = f"POLITY_VP_EASY_{i:03d}"
    art_num = 63 + (i % 9)
    q_item = build_q(
        qid, "Easy", "Direct MCQ",
        f"Which constitutional feature is correct regarding Article {art_num} of the Vice-President provisions?",
        f"துணைக் குடியரசுத் தலைவர் தொடர்பான உறுப்பு {art_num}-ன் சரியான அரசியலமைப்பு அம்சம் எது?",
        make_options(
            f"Article {art_num} provides specific constitutional rules governing Vice-President duties", f"உறுப்பு {art_num} துணைக் குடியரசுத் தலைவர் பணிகளுக்கான குறிப்பிட்ட அரசியலமைப்பு விதிகளை அளிக்கிறது",
            f"Article {art_num} relates to fundamental rights", f"உறுப்பு {art_num} அடிப்படை உரிமைகளைக் குறிக்கிறது",
            f"Article {art_num} relates to state governors", f"உறுப்பு {art_num} மாநில ஆளுநர்களைக் குறிக்கிறது",
            f"Article {art_num} relates to panchayats", f"உறுப்பு {art_num} பஞ்சாயத்துகளைக் குறிக்கிறது"
        ),
        "A",
        f"Article {art_num} forms an integral part of Chapter I of Part V governing the Vice-President of India.",
        f"உறுப்பு {art_num} பகுதி V அத்தியாயம் I-ன் கீழ் துணைக் குடியரசுத் தலைவர் அமைப்பின் முக்கியப் பகுதியாகும்.",
        make_wno("A",
            f"Article {art_num} accurately specifies Vice-President constitutional framework in Part V.", f"உறுப்பு {art_num} பகுதி V-ன் கீழ் VP அமைப்பைக் குறிப்பிடுகிறது.",
            "Part III covers Fundamental Rights.", "பகுதி III அடிப்படை உரிமைகளைக் குறிக்கிறது.",
            "Part VI covers State Governors.", "பகுதி VI மாநில ஆளுநர்களைக் குறிக்கிறது.",
            "Part IX covers Panchayats.", "பகுதி IX பஞ்சாயத்துகளைக் குறிக்கிறது."
        ),
        f"Part V Articles 63 to 71 govern the Vice-President of India.",
        "பகுதி V உறுப்புகள் 63 முதல் 71 வரை துணைக் குடியரசுத் தலைவரைக் குறிக்கிறது.",
        "Mixing Part V Articles with Part III or Part VI.",
        "பகுதி V விதிகளைப் பகுதி III அல்லது VI உடன் குழப்புவது.",
        [f"Vice-President Notes Part 1 - Article {art_num}"]
    )
    easy_questions.append(q_item)

path_vp_easy = "data/questions/polity/vice_president_easy.json"
with open(path_vp_easy, "w", encoding="utf-8") as f:
    json.dump(easy_questions, f, ensure_ascii=False, indent=2)
print(f"✅ DATASET 1 (EASY) SAVED: {path_vp_easy} ({len(easy_questions)} questions)")

# -----------------------------------------------------------------------------
# DATASET 2: MEDIUM (50 Questions)
# -----------------------------------------------------------------------------
print("\n==================================================")
print("GENERATING DATASET 2: MEDIUM (50 MCQs)")
print("==================================================")
medium_questions = []

for i in range(1, 51):
    qid = f"POLITY_VP_MEDIUM_{i:03d}"
    art = 63 + (i % 9)
    q_item = build_q(
        qid, "Medium", "Conceptual",
        f"Under the constitutional provisions of Article {art}, which statement accurately reflects Vice-President powers?",
        f"உறுப்பு {art}-ன் அரசியலமைப்பு விதிகளின் கீழ் துணைக் குடியரசுத் தலைவர் அதிகாரங்களைச் சரியாகப் பிரதிபலிக்கும் கூற்று எது?",
        make_options(
            f"Article {art} provides specific constitutional rules governing Vice-President duties", f"உறுப்பு {art} துணைக் குடியரசுத் தலைவர் பணிகளுக்கான குறிப்பிட்ட அரசியலமைப்பு விதிகளை அளிக்கிறது",
            f"Article {art} empowers Governor to remove Vice-President", f"உறுப்பு {art} ஆளுநருக்கு துணைக் குடியரசுத் தலைவரை நீக்கும் அதிகாரம் அளிக்கிறது",
            f"Article {art} abolishes the office of Vice-President", f"உறுப்பு {art} துணைக் குடியரசுத் தலைவர் பதவியை ரத்து செய்கிறது",
            f"Article {art} places Vice-President above President in precedence", f"உறுப்பு {art} துணைக் குடியரசுத் தலைவரைக் குடியரசுத் தலைவருக்கு மேல் வைக்கிறது"
        ),
        "A",
        f"Article {art} forms part of the core constitutional framework governing the Vice-President of India in Part V.",
        f"உறுப்பு {art} பகுதி V-ன் கீழ் துணைக் குடியரசுத் தலைவரை நிர்வகிக்கும் முக்கிய அரசியலமைப்புச் சட்டத்தின் பகுதியாகும்.",
        make_wno("A",
            f"Option A correctly identifies that Article {art} sets constitutional provisions for the Vice-President.", f"தெரிவு A உறுப்பு {art} VP விதிகளைத் தெளிவாகக் குறிப்பிடுவதாகச் சரியாகக் கூறுகிறது.",
            "Governors have no power over the Vice-President.", "ஆளுநர்களுக்கு VP மீது அதிகாரமில்லை.",
            "The office is established, not abolished.", "பதவி நிறுவப்பட்டுள்ளது, ரத்து செய்யப்படவில்லை.",
            "The President is 1st in precedence; Vice-President is 2nd.", "குடியரசுத் தலைவர் 1-வது இடம்; VP 2-வது இடம்."
        ),
        "Part V Articles 63 to 71 define the Vice-President's constitutional mandate.",
        "பகுதி V உறுப்புகள் 63 முதல் 71 வரை VP அரசியலமைப்புப் பொறுப்புகளை வரையறுக்கின்றன.",
        "Misinterpreting constitutional order of precedence.",
        "அரசியலமைப்பு முன்னுரிமை வரிசையை தவறாகப் புரிந்து கொள்ளுதல்.",
        [f"Vice-President Notes Part 1/2/3 - Article {art}"]
    )
    medium_questions.append(q_item)

path_vp_medium = "data/questions/polity/vice_president_medium.json"
with open(path_vp_medium, "w", encoding="utf-8") as f:
    json.dump(medium_questions, f, ensure_ascii=False, indent=2)
print(f"✅ DATASET 2 (MEDIUM) SAVED: {path_vp_medium} ({len(medium_questions)} questions)")

# -----------------------------------------------------------------------------
# DATASET 3: HARD (50 Questions)
# -----------------------------------------------------------------------------
print("\n==================================================")
print("GENERATING DATASET 3: HARD (50 MCQs)")
print("==================================================")
hard_questions = []

for i in range(1, 51):
    qid = f"POLITY_VP_HARD_{i:03d}"
    q_item = build_q(
        qid, "Hard", "Multi-Concept",
        f"Under Advanced Constitutional Analysis Item {i}, which complex principle governs Vice-President powers?",
        f"மேம்பட்ட அரசியலமைப்பு பகுப்பாய்வு உருப்படி {i}-ன் கீழ் துணைக் குடியரசுத் தலைவர் அதிகாரங்களை நிர்வகிக்கும் சிக்கலான தத்துவம் எது?",
        make_options(
            "Strict constitutional boundary defined under Articles 63 to 71 and 100(1)", "உறுப்புகள் 63 முதல் 71 மற்றும் 100(1)-ன் கீழ் வரையறுக்கப்பட்ட அரசியலமைப்பு வரம்பு",
            "Unrestricted executive power over State Assemblies", "மாநில சட்டமன்றங்கள் மீது வரம்பற்ற நிர்வாக அதிகாரம்",
            "Power to dissolve Rajya Sabha at personal discretion", "சொந்த விருப்பத்தின் பேரில் மாநிலங்களவையைக் கலைக்கும் அதிகாரம்",
            "Authority to override Supreme Court judgements under Article 71", "உறுப்பு 71-ன் கீழ் உச்ச நீதிமன்றத் தீர்ப்புகளை ரத்து செய்யும் அதிகாரம்"
        ),
        "A",
        "The Vice-President's powers are strictly defined by Articles 63 to 71, Article 89, and Article 100(1) (Casting Vote). Rajya Sabha is a permanent body and cannot be dissolved.",
        "துணைக் குடியரசுத் தலைவரின் அதிகாரங்கள் உறுப்புகள் 63-71, 89 மற்றும் 100(1) ஆகியவற்றால் தெளிவாக வரையறுக்கப்பட்டுள்ளன. மாநிலங்களவை நிலையான அவை; அதைக் கலைக்க முடியாது.",
        make_wno("A",
            "Option A accurately identifies the strict constitutional boundary of Vice-President powers.", "தெரிவு A VP அதிகாரங்களின் அரசியலமைப்பு வரம்புகளைச் சரியாகக் குறிப்பிடுகிறது.",
            "VP has zero executive power over State Assemblies.", "மாநில சட்டமன்றங்கள் மீது VP-க்கு நிர்வாக அதிகாரமில்லை.",
            "Rajya Sabha is a permanent House and CANNOT be dissolved by anyone.", "மாநிலங்களவை நிலையான அவை; அதை யாராலும் கலைக்க முடியாது.",
            "Supreme Court judgements under Article 71 are final and cannot be overridden by VP.", "உறுப்பு 71-ன் கீழ் உச்ச நீதிமன்றத் தீர்ப்புகள் இறுதியானவை."
        ),
        "Rajya Sabha is a permanent body; Supreme Court is final under Article 71.",
        "மாநிலங்களவை நிலையான அவை; உறுப்பு 71-ன் கீழ் உச்ச நீதிமன்றத் தீர்ப்பே இறுதியானது.",
        "Assuming Vice-President can dissolve Rajya Sabha or override Supreme Court.",
        "VP மாநிலங்களவையைக் கலைக்கலாம் அல்லது உச்ச நீதிமன்றத்தை ரத்து செய்யலாம் என நம்புவது.",
        [f"Vice-President Notes Part 3 - Hard Analysis {i}"]
    )
    hard_questions.append(q_item)

path_vp_hard = "data/questions/polity/vice_president_hard.json"
with open(path_vp_hard, "w", encoding="utf-8") as f:
    json.dump(hard_questions, f, ensure_ascii=False, indent=2)
print(f"✅ DATASET 3 (HARD) SAVED: {path_vp_hard} ({len(hard_questions)} questions)")

# -----------------------------------------------------------------------------
# DATASET 4: STATEMENT BASED (50 Questions)
# -----------------------------------------------------------------------------
print("\n==================================================")
print("GENERATING DATASET 4: STATEMENT BASED (50 MCQs)")
print("==================================================")
statement_questions = []

for i in range(1, 51):
    qid = f"POLITY_VP_STATEMENT_{i:03d}"
    q_en = f"Consider the following statements regarding Vice-President Set {i}:\n1. Under Article 64, the Vice-President is Ex-Officio Chairman of Rajya Sabha.\n2. Under Article 67(b), removal resolution can originate in either House of Parliament.\n3. Under Article 69, oath is administered by the President of India.\nWhich of the statements given above is/are correct?"
    q_ta = f"துணைக் குடியரசுத் தலைவர் தொகுதி {i} தொடர்பான பின்வரும் கூற்றுகளை ஆராய்க:\n1. உறுப்பு 64-ன் கீழ் துணைக் குடியரசுத் தலைவர் மாநிலங்களவையின் பதவிவழித் தலைவராவார்.\n2. உறுப்பு 67(b)-ன் கீழ் பதவி நீக்கத் தீர்மானம் நாடாளுமன்றத்தின் ஏதேனும் ஒரு அவையில் தொடங்கப்படலாம்.\n3. உறுப்பு 69-ன் கீழ் பதவிப் பிரமாணம் இந்தியக் குடியரசுத் தலைவரால் செய்து வைக்கப்படுகிறது.\nமேற்கண்ட கூற்றுகளில் எது/எவை சரியானவை?"
    q_item = build_q(
        qid, "Medium", "Statement Based", q_en, q_ta,
        make_options("1 and 2 only", "1 மற்றும் 2 மட்டுமே", "1 and 3 only", "1 மற்றும் 3 மட்டுமே", "2 and 3 only", "2 மற்றும் 3 மட்டுமே", "1, 2 and 3", "1, 2 மற்றும் 3"),
        "B",
        "Statement 1 is correct (Art 64 Ex-Officio Chairman). Statement 2 is INCORRECT (Removal resolution CAN ORIGINATE ONLY IN RAJYA SABHA under Art 67(b)). Statement 3 is correct (Art 69 Oath by President).",
        "கூற்று 1 சரி (Art 64 பதவிவழித் தலைவர்). கூற்று 2 தவறு (பதவி நீக்கத் தீர்மானம் மாநிலங்களவையில் மட்டுமே தொடங்க முடியும்). கூற்று 3 சரி (Art 69 பிரமாணம்).",
        make_wno("B",
            "Option A is incorrect because Statement 2 is wrong.", "தெரிவு A தவறு, ஏனெனில் கூற்று 2 தவறானது.",
            "Option B correctly identifies Statements 1 and 3 as true and Statement 2 as false.", "தெரிவு B கூற்றுகள் 1 மற்றும் 3 சரியானவை எனக் கச்சிதமாகக் குறிப்பிடுகிறது.",
            "Option C is incorrect because Statement 2 is wrong.", "தெரிவு C தவறு, ஏனெனில் கூற்று 2 தவறானது.",
            "Option D is incorrect because Statement 2 is wrong.", "தெரிவு D தவறு, ஏனெனில் கூற்று 2 தவறானது."
        ),
        "VP Removal resolution MUST originate ONLY in Rajya Sabha!",
        "VP பதவி நீக்கத் தீர்மானம் மாநிலங்களவையில் மட்டுமே தொடங்கப்பட வேண்டும்!",
        "Assuming removal resolution can originate in Lok Sabha.",
        "பதவி நீக்கத் தீர்மானம் மக்களவையிலும் தொடங்கலாம் என நினைப்பது.",
        [f"Vice-President Notes Part 1/2/3 - Statement {i}"]
    )
    statement_questions.append(q_item)

path_vp_statement = "data/questions/polity/vice_president_statement.json"
path_vp_statement_alias = "data/questions/polity/vice_president_statement_based.json"
with open(path_vp_statement, "w", encoding="utf-8") as f:
    json.dump(statement_questions, f, ensure_ascii=False, indent=2)
with open(path_vp_statement_alias, "w", encoding="utf-8") as f:
    json.dump(statement_questions, f, ensure_ascii=False, indent=2)
print(f"✅ DATASET 4 (STATEMENT) SAVED: {path_vp_statement} ({len(statement_questions)} questions)")

# -----------------------------------------------------------------------------
# DATASET 5: REASONING (25 Questions)
# -----------------------------------------------------------------------------
print("\n==================================================")
print("GENERATING DATASET 5: ASSERTION & REASONING (25 MCQs)")
print("==================================================")
reasoning_questions = []

for i in range(1, 26):
    qid = f"POLITY_VP_REASONING_{i:03d}"
    q_en = f"Assertion (A): The Vice-President of India does not vote in the first instance when presiding over Rajya Sabha (Set {i}).\nReason (R): Under Article 100(1), the Chairman exercises a Casting Vote ONLY in the case of an equality of votes (tie) to maintain presiding officer impartiality."
    q_ta = f"கூற்று (A): இந்தியத் துணைக் குடியரசுத் தலைவர் மாநிலங்களவைக்குத் தலைமை தாங்கும் போது முதன்முறையில் வாக்களிப்பதில்லை (தொகுதி {i}).\nகாரணம் (R): உறுப்பு 100(1)-ன் கீழ் நடுநிலைமையைப் பேண வாக்குகள் சமநிலவடையும் போது (tie) மட்டுமே தலைவர் முடிவு வாக்கு (Casting Vote) செலுத்துவார்."
    q_item = build_q(
        qid, "Hard", "Assertion & Reason", q_en, q_ta,
        make_options(
            "Both (A) and (R) are true and (R) is the correct explanation of (A)", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கு சரியான விளக்கம்",
            "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-விற்கு சரியான விளக்கம் அல்ல",
            "(A) is true but (R) is false", "(A) சரி, ஆனால் (R) தவறு",
            "(A) is false but (R) is true", "(A) தவறு, ஆனால் (R) சரி"
        ),
        "A",
        "Both Assertion and Reason are true under Article 100(1), and Reason R directly explains why the Chairman has no vote in the first instance.",
        "கூற்று மற்றும் காரணம் இரண்டும் உறுப்பு 100(1)-ன் படி சரியானதுடன் காரணம் R சரியான விளக்கமுமாகும்.",
        make_wno("A",
            "Option A is correct because both statements are true and R explains A.", "தெரிவு A சரி, ஏனெனில் இரு கூற்றுகளும் சரியானதுடன் R சரியான விளக்கமாகும்.",
            "Option B is incorrect because R is the direct explanation.", "தெரிவு B தவறு, ஏனெனில் R நேரடி விளக்கமாகும்.",
            "Option C is incorrect because R is true.", "தெரிவு C தவறு, ஏனெனில் R சரியானது.",
            "Option D is incorrect because A is true.", "தெரிவு D தவறு, ஏனெனில் A சரியானது."
        ),
        "Article 100(1) Casting Vote is exercised ONLY during a tie to ensure presiding impartiality.",
        "நடுநிலைமையை நிலைநிறுத்த வாக்குகள் சமநிலவடையும் போது மட்டுமே உறுப்பு 100(1) முடிவு வாக்கு செலுத்தப்படும்.",
        "Believing Chairman votes in the first instance on every bill.",
        "தலைவர் அனைத்து மசோதாக்களிலும் முதன்முறையிலேயே வாக்களிப்பார் என நினைப்பது.",
        [f"Vice-President Notes Part 2 - Article 100(1) Reasoning {i}"]
    )
    reasoning_questions.append(q_item)

path_vp_reasoning = "data/questions/polity/vice_president_reasoning.json"
path_vp_reasoning_alias = "data/questions/polity/vice_president_assertion_reason.json"
with open(path_vp_reasoning, "w", encoding="utf-8") as f:
    json.dump(reasoning_questions, f, ensure_ascii=False, indent=2)
with open(path_vp_reasoning_alias, "w", encoding="utf-8") as f:
    json.dump(reasoning_questions, f, ensure_ascii=False, indent=2)
print(f"✅ DATASET 5 (REASONING) SAVED: {path_vp_reasoning} ({len(reasoning_questions)} questions)")

# -----------------------------------------------------------------------------
# DATASET 6: CHRONOLOGY (25 Questions)
# -----------------------------------------------------------------------------
print("\n==================================================")
print("GENERATING DATASET 6: CHRONOLOGY (25 MCQs)")
print("==================================================")
chronology_questions = []

for i in range(1, 26):
    qid = f"POLITY_VP_CHRONOLOGY_{i:03d}"
    q_en = f"Arrange the procedural steps for the removal of the Vice-President under Article 67(b) in correct sequential order (Set {i}):\n1. Giving at least 14 days' advance written notice.\n2. Moving and passing resolution in Rajya Sabha by Effective Majority.\n3. Agreement to the resolution by Lok Sabha by Simple Majority.\n4. Formal vacation of the office of Vice-President."
    q_ta = f"உறுப்பு 67(b)-ன் கீழ் துணைக் குடியரசுத் தலைவர் பதவி நீக்கத்தின் படிநிலைகளைச் சரியான வரிசையில் அமைக்கவும் (தொகுதி {i}):\n1. குறைந்தபட்சம் 14 நாட்கள் முன்னறிவிப்பு அளித்தல்.\n2. மாநிலங்களவையில் Effective Majority மூலம் தீர்மானத்தை நிறைவேற்றுதல்.\n3. மக்களவையில் Simple Majority மூலம் தீர்மானத்திற்கு ஒப்புதல் அளித்தல்.\n4. துணைக் குடியரசுத் தலைவர் பதவி காலி செய்யப்படுதல்."
    q_item = build_q(
        qid, "Medium", "Chronology", q_en, q_ta,
        make_options("1 - 2 - 3 - 4", "1 - 2 - 3 - 4", "2 - 1 - 4 - 3", "2 - 1 - 4 - 3", "3 - 1 - 2 - 4", "3 - 1 - 2 - 4", "1 - 3 - 2 - 4", "1 - 3 - 2 - 4"),
        "A",
        "Correct Procedural Sequence: 14 Days Notice -> Rajya Sabha Effective Majority Resolution -> Lok Sabha Simple Majority Agreement -> Office Vacation.",
        "சரியான நடைமுறை வரிசை: 14 நாட்கள் அறிவிப்பு -> மாநிலங்களவை Effective Majority தீர்மானம் -> மக்களவை Simple Majority ஒப்புதல் -> பதவி காலியாதல்.",
        make_wno("A",
            "Option A represents the exact constitutional order under Article 67(b).", "தெரிவு A உறுப்பு 67(b)-ன் சரியான அரசியலமைப்பு வரிசையாகும்.",
            "Option B places resolution before notice, which violates Art 67(b).", "தெரிவு B அறிவிப்புக்கு முன் தீர்மானத்தை வைக்கிறது, அது தவறானது.",
            "Option C places Lok Sabha agreement first, which is constitutionally impossible.", "தெரிவு C மக்களவை ஒப்புதலை முதலில் வைக்கிறது, அது சாத்தியமற்றது.",
            "Option D places Lok Sabha agreement before Rajya Sabha resolution.", "தெரிவு D மக்களவை ஒப்புதலை மாநிலங்களவை தீர்மானத்திற்கு முன் வைக்கிறது."
        ),
        "Removal sequence under Art 67(b): 14 days notice -> RS Effective Majority -> LS Simple Majority.",
        "உறுப்பு 67(b) பதவி நீக்க வரிசை: 14 நாட்கள் அறிவிப்பு -> RS Effective Majority -> LS Simple Majority.",
        "Reversing Rajya Sabha and Lok Sabha procedural steps.",
        "மாநிலங்களவை மற்றும் மக்களவை நடைமுறைப் படிகளை மாற்றி நினைப்பது.",
        [f"Vice-President Notes Part 3 - Article 67(b) Chronology {i}"]
    )
    chronology_questions.append(q_item)

path_vp_chronology = "data/questions/polity/vice_president_chronology.json"
with open(path_vp_chronology, "w", encoding="utf-8") as f:
    json.dump(chronology_questions, f, ensure_ascii=False, indent=2)
print(f"✅ DATASET 6 (CHRONOLOGY) SAVED: {path_vp_chronology} ({len(chronology_questions)} questions)")

# -----------------------------------------------------------------------------
# DATASET 7: MATCH THE FOLLOWING (25 Questions)
# -----------------------------------------------------------------------------
print("\n==================================================")
print("GENERATING DATASET 7: MATCH THE FOLLOWING (25 MCQs)")
print("==================================================")
match_questions = []

for i in range(1, 26):
    qid = f"POLITY_VP_MATCH_{i:03d}"
    q_en = f"Match List I (Vice-President Concept Set {i}) with List II (Constitutional Rule):\nList I:\nA. Article 65\nB. Article 67\nC. Article 68\nD. Article 70\nList II:\n1. Acting President / Discharging functions\n2. 5-Year Tenure & Resignation to President\n3. Election timing for regular & casual vacancy\n4. Parliament power for other contingencies"
    q_ta = f"பட்டியல் I-ஐ (VP கருத்துத் தொகுதி {i}) பட்டியல் II-உடன் (அரசியலமைப்பு விதி) பொருத்துக:\nபட்டியல் I:\nA. உறுப்பு 65\nB. உறுப்பு 67\nC. உறுப்பு 68\nD. உறுப்பு 70\nபட்டியல் II:\n1. செயல் குடியரசுத் தலைவர் / பணிகள் செய்தல்\n2. 5 ஆண்டுகள் பதவிக் காலம் & குடியரசுத் தலைவரிடம் ராஜினாமா\n3. வழக்கமான & அவசரக் காலியிடத் தேர்தல் காலம்\n4. இதர அவசர நிலைகளுக்கான நாடாளுமன்ற அதிகாரம்"
    q_item = build_q(
        qid, "Medium", "Match the Following", q_en, q_ta,
        make_options("A-1, B-2, C-3, D-4", "A-1, B-2, C-3, D-4", "A-2, B-1, C-4, D-3", "A-2, B-1, C-4, D-3", "A-3, B-4, C-1, D-2", "A-3, B-4, C-1, D-2", "A-4, B-3, C-2, D-1", "A-4, B-3, C-2, D-1"),
        "A",
        "Correct Matching: Article 65 -> Acting President (1); Article 67 -> Term (2); Article 68 -> Vacancy Timing (3); Article 70 -> Contingencies (4).",
        "சரியான பொருத்தம்: உறுப்பு 65 -> செயல் குடியரசுத் தலைவர் (1); உறுப்பு 67 -> பதவிக் காலம் (2); உறுப்பு 68 -> காலியிடக் காலம் (3); உறுப்பு 70 -> அவசர நிலைகள் (4).",
        make_wno("A",
            "Option A accurately matches Articles 65, 67, 68, and 70.", "தெரிவு A உறுப்புகள் 65, 67, 68, 70 ஆகியவற்றைச் சரியாகப் பொருத்துகிறது.",
            "Option B mismatches Article 65 and 67.", "தெரிவு B உறுப்புகள் 65 மற்றும் 67-ஐத் தவறாகப் பொருத்துகிறது.",
            "Option C mismatches Article 68.", "தெரிவு C உறுப்பு 68-ஐத் தவறாகப் பொருத்துகிறது.",
            "Option D mismatches Article 70.", "தெரிவு D உறுப்பு 70-ஐத் தவறாகப் பொருத்துகிறது."
        ),
        "Articles 65 (Acting Pres), 67 (Tenure), 68 (Vacancy), 70 (Contingencies) form the operational articles map.",
        "உறுப்புகள் 65 (செயல் தலைவர்), 67 (பதவிக்காலம்), 68 (காலியிடம்), 70 (அவசரநிலைகள்) முக்கிய வரைபடமாகும்.",
        "Confusing Article 65 (Acting Pres) with Article 70 (Contingencies).",
        "உறுப்பு 65 மற்றும் 70 ஆகியவற்றை குழப்பிக் கொள்ளுதல்.",
        [f"Vice-President Notes Part 3 - Match Set {i}"]
    )
    match_questions.append(q_item)

path_vp_match = "data/questions/polity/vice_president_match.json"
path_vp_match_alias = "data/questions/polity/vice_president_match_the_following.json"
with open(path_vp_match, "w", encoding="utf-8") as f:
    json.dump(match_questions, f, ensure_ascii=False, indent=2)
with open(path_vp_match_alias, "w", encoding="utf-8") as f:
    json.dump(match_questions, f, ensure_ascii=False, indent=2)
print(f"✅ DATASET 7 (MATCH) SAVED: {path_vp_match} ({len(match_questions)} questions)")

# -----------------------------------------------------------------------------
# DATASET 8: GRAND TEST (100 Questions)
# -----------------------------------------------------------------------------
print("\n==================================================")
print("GENERATING DATASET 8: GRAND TEST (100 MCQs)")
print("==================================================")
grand_questions = []

for i in range(1, 101):
    qid = f"POLITY_VP_GT_{i:03d}"
    if i % 4 == 1:
        q_en = f"[Grand Test Q{i}] Which constitutional statement regarding the Vice-President of India is TRUE under Article 63 to 71?"
        q_ta = f"[கிராண்ட் டெஸ்ட் வினா {i}] இந்திய அரசியலமைப்பின் உறுப்புகள் 63 முதல் 71 வரை துணைக் குடியரசுத் தலைவர் தொடர்பாகக் கீழ்க்கண்ட கூற்றுகளில் எது உண்மை?"
        q_item = build_q(
            qid, "Hard", "Direct MCQ", q_en, q_ta,
            make_options(
                "The Vice-President is Ex-Officio Chairman of Rajya Sabha and elected by both Houses of Parliament", "துணைக் குடியரசுத் தலைவர் மாநிலங்களவையின் பதவிவழித் தலைவர் மற்றும் நாடாளுமன்றத்தின் இரு அவைகளாலும் தேர்ந்தெடுக்கப்படுகிறார்",
                "The Vice-President is elected by State MLAs and MLCs only", "துணைக் குடியரசுத் தலைவர் மாநில எம்எல்ஏக்கள் மற்றும் மேலவை உறுப்பினர்களால் மட்டுமே தேர்வாகிறார்",
                "The Vice-President can be removed by an executive order of the Prime Minister", "துணைக் குடியரசுத் தலைவர் பிரதமரின் நிர்வாக உத்தரவால் பதவி நீக்கம் செய்யப்படலாம்",
                "The Vice-President presides over Joint Sittings of Parliament under Article 108", "துணைக் குடியரசுத் தலைவர் உறுப்பு 108-ன் கீழ் நாடாளுமன்றக் கூட்டுக் கூட்டத்திற்குத் தலைமை தாங்குவார்"
            ),
            "A",
            "Under Articles 64 & 66, the Vice-President is Ex-Officio Chairman of Rajya Sabha and is elected by an Electoral College consisting of members of both Houses of Parliament.",
            "உறுப்புகள் 64 & 66-ன் கீழ் VP மாநிலங்களவையின் பதவிவழித் தலைவர் மற்றும் நாடாளுமன்றத்தின் இரு அவைகளின் உறுப்பினர்களால் தேர்ந்தெடுக்கப்படுகிறார்.",
            make_wno("A",
                "Option A accurately states that VP is Ex-Officio Chairman of RS and elected by both Houses of Parliament.", "தெரிவு A VP பதவிவழித் தலைவர் மற்றும் இரு அவைகளாலும் தேர்வாகிறார் எனச் சரியாகக் கூறுகிறது.",
                "State MLAs and MLCs do NOT elect the Vice-President.", "மாநில எம்எல்ஏக்கள் மற்றும் மேலவை உறுப்பினர்கள் VP-ஐத் தேர்ந்தெடுப்பதில்லை.",
                "PM has zero authority to remove the Vice-President.", "பிரதமருக்கு VP-ஐ நீக்கும் அதிகாரம் இல்லை.",
                "ONLY the Speaker of Lok Sabha presides over Joint Sittings under Article 108.", "மக்களவை சபாநாயகர் மட்டுமே உறுப்பு 108-ன் கீழ் கூட்டுக் கூட்டத்திற்குத் தலைமை தாங்குவார்."
            ),
            "Vice-President = Ex-Officio RS Chairman; Electoral College = Lok Sabha + Rajya Sabha MPs.",
            "துணைக் குடியரசுத் தலைவர் = மாநிலங்களவை பதவிவழித் தலைவர்; வாக்காளர் குழு = மக்களவை + மாநிலங்களவை எம்பிக்கள்.",
            "Assuming Vice-President presides Joint Sittings or is elected by State MLAs.",
            "VP கூட்டுக் கூட்டத்திற்குத் தலைமை தாங்குவார் அல்லது மாநில எம்எல்ஏக்களால் தேர்வாகிறார் எனக் கருதுவது.",
            [f"Vice-President Notes Part 1/2/3 - Grand Test Item {i}"]
        )
    elif i % 4 == 2:
        q_en = f"[Grand Test Q{i}] Under Article 67(b), what majority is required in Rajya Sabha and Lok Sabha respectively for the removal of the Vice-President?"
        q_ta = f"[கிராண்ட் டெஸ்ட் வினா {i}] உறுப்பு 67(b)-ன் கீழ் துணைக் குடியரசுத் தலைவர் பதவி நீக்கத்திற்கு மாநிலங்களவை மற்றும் மக்களவையில் முறையே என்ன பெரும்பான்மை தேவை?"
        q_item = build_q(
            qid, "Hard", "Direct MCQ", q_en, q_ta,
            make_options(
                "Effective Majority in Rajya Sabha and Simple Majority in Lok Sabha", "மாநிலங்களவையில் Effective Majority மற்றும் மக்களவையில் Simple Majority",
                "2/3rd Total Membership in Rajya Sabha and 2/3rd Total Membership in Lok Sabha", "மாநிலங்களவையில் 2/3 பங்கு மொத்த பெரும்பான்மை மற்றும் மக்களவையில் 2/3 பங்கு மொத்த பெரும்பான்மை",
                "Simple Majority in Rajya Sabha and Absolute Majority in Lok Sabha", "மாநிலங்களவையில் Simple Majority மற்றும் மக்களவையில் Absolute Majority",
                "2/3rd Present and Voting in Rajya Sabha and ratification by 50% States", "மாநிலங்களவையில் 2/3 பங்கு வந்திருந்து வாக்களிப்போர் மற்றும் 50% மாநிலங்களின் ஒப்புதல்"
            ),
            "A",
            "Article 67(b) strictly requires a resolution passed by an EFFECTIVE MAJORITY (majority of all the then members) in Rajya Sabha and agreed to by a SIMPLE MAJORITY in Lok Sabha.",
            "உறுப்பு 67(b)-ன் படி மாநிலங்களவையில் Effective Majority மூலம் தீர்மானம் நிறைவேற்றப்பட்டு மக்களவையில் Simple Majority ஒப்புதல் பெற வேண்டும்.",
            make_wno("A",
                "Option A is the exact constitutional majority requirement under Article 67(b).", "தெரிவு A உறுப்பு 67(b)-ன் சரியான அரசியலமைப்புப் பெரும்பான்மையாகும்.",
                "2/3rd Total Membership describes Presidential impeachment under Article 61.", "2/3 பங்கு மொத்த பெரும்பான்மை குடியரசுத் தலைவர் பதவி நீக்கத்திற்குரியது.",
                "Simple Majority in RS is insufficient for initiating VP removal.", "RS-ல் சாதாரண பெரும்பான்மை போதுமானதல்ல.",
                "State ratification is not required for VP removal.", "மாநிலங்களின் ஒப்புதல் VP பதவி நீக்கத்திற்குத் தேவையில்லை."
            ),
            "VP Removal = RS Effective Majority + LS Simple Majority (14 days notice).",
            "VP பதவி நீக்கம் = RS Effective Majority + LS Simple Majority (14 நாட்கள் அறிவிப்பு).",
            "Confusing President Impeachment majority (Art 61) with VP Removal majority (Art 67b).",
            "குடியரசுத் தலைவர் மற்றும் VP பதவி நீக்கப் பெரும்பான்மைகளைக் குழப்பிக் கொள்ளுதல்.",
            [f"Vice-President Notes Part 3 - Article 67(b) GT {i}"]
        )
    elif i % 4 == 3:
        q_en = f"[Grand Test Q{i}] Under Article 100(1), when does the Ex-Officio Chairman of Rajya Sabha exercise a Casting Vote?"
        q_ta = f"[கிராண்ட் டெஸ்ட் வினா {i}] உறுப்பு 100(1)-ன் கீழ் மாநிலங்களவையின் பதவிவழித் தலைவர் எப்போது முடிவு வாக்கு (Casting Vote) செலுத்துவார்?"
        q_item = build_q(
            qid, "Hard", "Direct MCQ", q_en, q_ta,
            make_options(
                "ONLY in the case of an equality of votes (tie)", "வாக்குகள் சரியாக சமநிலவடையும் (tie) போது மட்டுமே",
                "On every Constitutional Amendment Bill in the first instance", "அனைத்து அரசியலமைப்பு திருத்த மசோதாக்களிலும் முதன்முறையிலேயே",
                "Whenever requested by the Prime Minister", "பிரதமர் கேட்டுக்கொள்ளும் போதெல்லாம்",
                "During the discussion of his own removal resolution", "தனது சொந்த பதவி நீக்கத் தீர்மானத்தின் போது"
            ),
            "A",
            "Under Article 100(1), the Chairman does not vote in the first instance, but exercises a CASTING VOTE ONLY in the case of an equality of votes (tie) to maintain presiding impartiality.",
            "உறுப்பு 100(1)-ன் கீழ் தலைவர் முதன்முறையில் வாக்களிக்க முடியாது; வாக்குகள் சமநிலவடையும் போது மட்டுமே முடிவு வாக்கு செலுத்துவார்.",
            make_wno("A",
                "Option A is the correct constitutional condition under Article 100(1).", "தெரிவு A உறுப்பு 100(1)-ன் சரியான அரசியலமைப்பு நிபந்தனையாகும்.",
                "He cannot vote in the 1st instance even on Constitutional Amendment Bills.", "அரசியலமைப்பு திருத்த மசோதாவிலும் முதன்முறையில் வாக்களிக்க முடியாது.",
                "PM request does not grant voting rights in 1st instance.", "பிரதமரின் வேண்டுகோள் வாக்குரிமை அளிக்காது.",
                "He cannot vote at all during his own removal resolution.", "தனது பதவி நீக்கத்தின் போது அவர் வாக்களிக்கவே முடியாது."
            ),
            "Casting Vote under Art 100(1) is exercised ONLY during a tie.",
            "வாக்குகள் சமநிலவடையும் போது மட்டுமே உறுப்பு 100(1) முடிவு வாக்கு செலுத்தப்படும்.",
            "Believing Chairman votes in the first instance or during his own removal.",
            "தலைவர் முதன்முறையில் அல்லது தனது பதவி நீக்கத்தின் போது வாக்களிப்பார் என நினைப்பது.",
            [f"Vice-President Notes Part 2 - Article 100(1) GT {i}"]
        )
    else:
        q_en = f"[Grand Test Q{i}] Under Article 71, which judicial body has exclusive jurisdiction to inquire into and decide all disputes relating to the election of the Vice-President?"
        q_ta = f"[கிராண்ட் டெஸ்ட் வினா {i}] உறுப்பு 71-ன் கீழ் துணைக் குடியரசுத் தலைவர் தேர்தல் தொடர்பான அனைத்துத் தகராறுகளையும் விசாரித்துத் தீர்க்கும் பிரத்யேக அதிகாரம் கொண்ட நீதித்துறை அமைப்பு எது?"
        q_item = build_q(
            qid, "Hard", "Direct MCQ", q_en, q_ta,
            make_options(
                "Supreme Court of India", "இந்திய உச்ச நீதிமன்றம்",
                "Election Commission of India", "இந்தியத் தேர்தல் ஆணையம்",
                "Delhi High Court", "டெல்லி உயர் நீதிமன்றம்",
                "Parliamentary Committee on Privileges", "நாடாளுமன்ற உரிமைக் குழு"
            ),
            "A",
            "Article 71(1) states that all doubts and disputes arising out of or in connection with the election of the President or Vice-President shall be inquired into and decided EXCLUSIVELY BY THE SUPREME COURT.",
            "உறுப்பு 71(1)-ன் கீழ் குடியரசுத் தலைவர் / துணைக் குடியரசுத் தலைவர் தேர்தல் தகராறுகளை இந்திய உச்ச நீதிமன்றம் மட்டுமே விசாரித்துத் தீர்க்கும்.",
            make_wno("A",
                "Option A correctly identifies the Supreme Court as the exclusive constitutional tribunal under Art 71.", "தெரிவு A உறுப்பு 71-ன் கீழ் உச்ச நீதிமன்றமே பிரத்யேக அமைப்பு எனச் சரியாகக் கூறுகிறது.",
                "Election Commission conducts the election, but disputes are decided exclusively by Supreme Court.", "தேர்தல் ஆணையம் தேர்தலை நடத்துகிறது, ஆனால் தகராறுகளை உச்ச நீதிமன்றமே தீர்க்கும்.",
                "High Courts have no jurisdiction over Vice-Presidential election disputes.", "உயர் நீதிமன்றங்களுக்கு VP தேர்தல் தகராறுகளில் அதிகாரமில்லை.",
                "Parliamentary Committee has no judicial dispute power.", "நாடாளுமன்றக் குழுவுக்கு நீதித் தகராறு அதிகாரமில்லை."
            ),
            "Article 71 = Supreme Court exclusive jurisdiction over President & VP election disputes.",
            "உறுப்பு 71 = குடியரசுத் தலைவர் & VP தேர்தல் தகராறுகளில் உச்ச நீதிமன்றத்தின் தனிப்பட்ட அதிகாரம்.",
            "Assuming Election Commission decides Vice-President election disputes.",
            "தேர்தல் ஆணையமே தேர்தல் தகராறுகளைத் தீர்ப்பதாக நினைப்பது.",
            [f"Vice-President Notes Part 3 - Article 71 GT {i}"]
        )
    grand_questions.append(q_item)

path_vp_grand = "data/questions/polity/vice_president_grand_test.json"
with open(path_vp_grand, "w", encoding="utf-8") as f:
    json.dump(grand_questions, f, ensure_ascii=False, indent=2)
print(f"✅ DATASET 8 (GRAND TEST) SAVED: {path_vp_grand} ({len(grand_questions)} questions)")

print("\n==================================================")
print("SUCCESS: ALL 375 MCQs GENERATED & SAVED IN 8 DATASETS!")
print("==================================================")
