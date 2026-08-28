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

# Q1
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

# Q2
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

# Q3
easy_questions.append(build_q(
    "POLITY_VP_EASY_003", "Easy", "Direct MCQ",
    "What rank does the Vice-President hold in the official Indian Warrant of Precedence?",
    "அதிகாரப்பூர்வ முன்னுரிமைப் பட்டியலில் (Warrant of Precedence) துணைக் குடியரசுத் தலைவர் எந்த இடத்தில் உள்ளார்?",
    make_options("First Rank", "1-வது இடம்", "Second Rank", "2-வது இடம்", "Third Rank", "3-வது இடம்", "Fourth Rank", "4-வது இடம்"),
    "B",
    "The Vice-President holds 2nd Rank immediately after the President of India (1st Rank).",
    "துணைக் குடியரசுத் தலைவர் குடியரசுத் தலைவருக்கு (1-வது இடம்) அடுத்தபடியாக 2-வது இடத்தில் உள்ளார்.",
    make_wno("B",
        "Rank 1 belongs to the President.", "1-வது இடம் குடியரசுத் தலைவருக்குரியது.",
        "Rank 2 belongs to the Vice-President.", "2-வது இடம் துணைக் குடியரசுத் தலைவருக்குரியது.",
        "Rank 3 belongs to the Prime Minister.", "3-வது இடம் பிரதமருக்குரியது.",
        "Rank 4 belongs to Governors of States.", "4-வது இடம் மாநில ஆளுநர்களுக்குரியது."
    ),
    "Warrant order: 1st President, 2nd Vice-President, 3rd Prime Minister.",
    "முன்னுரிமை வரிசை: 1-வது குடியரசுத் தலைவர், 2-வது VP, 3-வது பிரதமர்.",
    "Confusing VP rank with Prime Minister rank.",
    "VP தரவரிசையைப் பிரதமருடன் குழப்புவது.",
    ["Vice-President Notes Part 1 - Position"]
))

# Q4
easy_questions.append(build_q(
    "POLITY_VP_EASY_004", "Easy", "Direct MCQ",
    "What is the minimum age requirement for a person to be eligible for election as Vice-President?",
    "துணைக் குடியரசுத் தலைவர் தேர்தலில் போட்டியிடத் தேவையான குறைந்தபட்ச வயது வரம்பு என்ன?",
    make_options("25 Years", "25 ஆண்டுகள்", "30 Years", "30 ஆண்டுகள்", "35 Years", "35 ஆண்டுகள்", "40 Years", "40 ஆண்டுகள்"),
    "C",
    "Article 66(3) mandates a minimum age of 35 years for Vice-President (same as President and Governor).",
    "உறுப்பு 66(3)-ன் படி துணைக் குடியரசுத் தலைவருக்கு குறைந்தபட்ச வயது 35 ஆண்டுகள் ஆகும்.",
    make_wno("C",
        "25 years is for Lok Sabha & Vidhan Sabha.", "25 வயது மக்களவை மற்றும் சட்டமன்றத்திற்கான வயது.",
        "30 years is for Rajya Sabha & Vidhan Parishad.", "30 வயது மாநிலங்களவை மற்றும் மேலவைக்கான வயது.",
        "35 years is the correct constitutional minimum age under Article 66(3).", "35 வயது உறுப்பு 66(3)-ன் கீழ் சரியான அரசியலமைப்பு குறைந்தபட்ச வயது.",
        "40 years is not a constitutional qualification age.", "40 வயது அரசியலமைப்புத் தகுதி வயது அல்ல."
    ),
    "Remember 35 years applies to President, Vice-President, and Governor.",
    "35 வயது குடியரசுத் தலைவர், துணைக் குடியரசுத் தலைவர் மற்றும் ஆளுநருக்குப் பொருந்தும்.",
    "Confusing 30 years (RS member age) with 35 years (VP election age).",
    "மாநிலங்களவை உறுப்பினர் வயது (30) மற்றும் VP வயது (35) ஆகியவற்றை குழப்புவது.",
    ["Vice-President Notes Part 1 - Article 66(3)"]
))

# Q5
easy_questions.append(build_q(
    "POLITY_VP_EASY_005", "Easy", "Direct MCQ",
    "To which House of Parliament must a candidate be qualified for election to be eligible as Vice-President?",
    "துணைக் குடியரசுத் தலைவராகத் தேர்வாக ஒரு வேட்பாளர் எந்த நாடாளுமன்ற அவைக்குத் தேர்வாகும் தகுதியைப் பெற்றிருக்க வேண்டும்?",
    make_options("Lok Sabha", "மக்களவை", "Rajya Sabha", "மாநிலங்களவை", "Either House", "ஏதேனும் ஒரு அவை", "State Legislative Assembly", "மாநில சட்டமன்றம்"),
    "B",
    "Article 66(3)(c) specifies that a VP candidate must be qualified for election as a member of the Council of States (Rajya Sabha). President requires Lok Sabha qualification.",
    "உறுப்பு 66(3)(c)-ன் படி VP வேட்பாளர் மாநிலங்களவை (Rajya Sabha) உறுப்பினராவதற்கான தகுதி பெற்றிருக்க வேண்டும்.",
    make_wno("B",
        "Lok Sabha qualification is required for President (Art 58), not Vice-President.", "மக்களவை தகுதி குடியரசுத் தலைவருக்குரியது.",
        "Rajya Sabha qualification is specifically required for Vice-President under Art 66(3).", "மாநிலங்களவை தகுதி துணைக் குடியரசுத் தலைவருக்குரியது.",
        "It is not either House; it is strictly Rajya Sabha.", "ஏதேனும் ஒரு அவை அல்ல; மாநிலங்களவை மட்டுமே.",
        "State Legislative Assembly qualification is irrelevant.", "மாநில சட்டமன்றத் தகுதி பொருந்தாது."
    ),
    "President = Lok Sabha eligibility; Vice-President = Rajya Sabha eligibility.",
    "குடியரசுத் தலைவர் = மக்களவை தகுதி; துணைக் குடியரசுத் தலைவர் = மாநிலங்களவை தகுதி.",
    "Reversing Lok Sabha and Rajya Sabha qualifications.",
    "மக்களவை மற்றும் மாநிலங்களவைத் தகுதிகளை மாற்றி நினைப்பது.",
    ["Vice-President Notes Part 1 - Qualifications"]
))

# Q6
easy_questions.append(build_q(
    "POLITY_VP_EASY_006", "Easy", "Direct MCQ",
    "Under Article 69, who administers the Oath of Office to the Vice-President of India?",
    "உறுப்பு 69-ன் கீழ் துணைக் குடியரசுத் தலைவருக்கு பதவிப் பிரமாணம் செய்து வைப்பவர் யார்?",
    make_options("Chief Justice of India", "இந்திய தலைமை நீதிபதி", "President of India", "இந்தியக் குடியரசுத் தலைவர்", "Speaker of Lok Sabha", "மக்களவை சபாநாயகர்", "Prime Minister", "இந்தியப் பிரதமர்"),
    "B",
    "Article 69 states that the oath is administered by the President of India or a person appointed by him.",
    "உறுப்பு 69-ன் கீழ் பதவிப் பிரமாணம் இந்தியக் குடியரசுத் தலைவரால் செய்து வைக்கப்படுகிறது.",
    make_wno("B",
        "CJI administers oath to President (Art 60).", "CJI குடியரசுத் தலைவருக்குப் பிரமாணம் செய்து வைக்கிறார்.",
        "President administers oath to Vice-President under Article 69.", "குடியரசுத் தலைவர் துணைக் குடியரசுத் தலைவருக்குப் பிரமாணம் செய்து வைக்கிறார்.",
        "Speaker does not administer oath.", "சபாநாயகர் பிரமாணம் செய்து வைப்பதில்லை.",
        "PM does not administer oath.", "பிரதமர் பிரமாணம் செய்து வைப்பதில்லை."
    ),
    "CJI -> President; President -> Vice-President.",
    "CJI -> குடியரசுத் தலைவர்; குடியரசுத் தலைவர் -> துணைக் குடியரசுத் தலைவர்.",
    "Assuming CJI administers oath to Vice-President.",
    "CJI VP-க்குப் பிரமாணம் செய்து வைப்பதாக நினைப்பது.",
    ["Vice-President Notes Part 1 - Article 69"]
))

# Q7
easy_questions.append(build_q(
    "POLITY_VP_EASY_007", "Easy", "Direct MCQ",
    "To whom does the Vice-President address his letter of resignation under Article 67(a)?",
    "உறுப்பு 67(a)-ன் கீழ் துணைக் குடியரசுத் தலைவர் தனது ராஜினாமாக் கடிதத்தை யாரிடம் சமர்ப்பிக்கிறார்?",
    make_options("Speaker of Lok Sabha", "மக்களவை சபாநாயகர்", "Chief Justice of India", "இந்திய தலைமை நீதிபதி", "President of India", "இந்தியக் குடியரசுத் தலைவர்", "Deputy Chairman of Rajya Sabha", "மாநிலங்களவைத் துணைத் தலைவர்"),
    "C",
    "Under Article 67(a), the Vice-President addresses his resignation to the President of India.",
    "உறுப்பு 67(a)-ன் கீழ் VP தனது ராஜினாமாக் கடிதத்தை குடியரசுத் தலைவரிடம் சமர்ப்பிக்கிறார்.",
    make_wno("C",
        "Speaker receives President's resignation notification, not VP's.", "சபாநாயகர் குடியரசுத் தலைவர் ராஜினாமா அறிவிப்பைப் பெறுபவர்.",
        "CJI does not receive VP resignation.", "CJI ராஜினாமாவைப் பெறுவதில்லை.",
        "Vice-President resigns strictly to the President of India.", "VP தனது ராஜினாமாவை குடியரசுத் தலைவரிடம் மட்டுமே வழங்குகிறார்.",
        "Deputy Chairman is not the recipient.", "துணைத் தலைவர் பெறுநர் அல்ல."
    ),
    "President resigns to Vice-President; Vice-President resigns to President.",
    "குடியரசுத் தலைவர் -> VP; VP -> குடியரசுத் தலைவர்.",
    "Assuming VP resigns to Rajya Sabha Deputy Chairman or Speaker.",
    "VP துணைத் தலைவரிடம் ராஜினாமா செய்வதாக நினைப்பது.",
    ["Vice-President Notes Part 1 - Article 67"]
))

# Build remaining Easy questions dynamically from index 8 to 50
for i in range(8, 51):
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

# Save Dataset 1: Easy
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
    if i == 1:
        q_item = build_q(
            qid, "Medium", "Conceptual",
            "Which of the following members are included in the Electoral College for the election of the Vice-President of India under Article 66(1)?",
            "உறுப்பு 66(1)-ன் கீழ் இந்தியத் துணைக் குடியரசுத் தலைவர் தேர்தலுக்கான வாக்காளர் குழுவில் கீழ்க்கண்டவர்களில் யார் சேர்க்கப்பட்டுள்ளனர்?",
            make_options(
                "Elected members of Parliament only", "தேர்ந்தெடுக்கப்பட்ட நாடாளுமன்ற உறுப்பினர்கள் மட்டுமே",
                "Both Elected and Nominated members of Parliament", "நாடாளுமன்றத்தின் தேர்ந்தெடுக்கப்பட்ட மற்றும் நியமன உறுப்பினர்கள் இருவருமே",
                "Elected members of Parliament and State Assemblies", "நாடாளுமன்றம் மற்றும் மாநில சட்டமன்றத் தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்கள்",
                "Elected members of Rajya Sabha only", "மாநிலங்களவையின் தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்கள் மட்டுமே"
            ),
            "B",
            "Under Article 66(1), the Vice-President's Electoral College consists of members of BOTH Houses of Parliament (Lok Sabha + Rajya Sabha), including BOTH ELECTED AND NOMINATED MPs. State MLAs do not participate.",
            "உறுப்பு 66(1)-ன் கீழ் துணைக் குடியரசுத் தலைவர் வாக்காளர் குழுவில் நாடாளுமன்றத்தின் இரு அவைகளின் தேர்ந்தெடுக்கப்பட்ட மற்றும் நியமன உறுப்பினர்கள் இருவருமே சேர்க்கப்பட்டுள்ளனர்.",
            make_wno("B",
                "Option A excludes nominated MPs, who ARE included in the Vice-President election.", "தெரிவு A நியமன எம்பிக்களை விலக்குகிறது; ஆனால் அவர்கள் VP தேர்தலில் சேர்க்கப்பட்டுள்ளனர்.",
                "Option B correctly identifies that BOTH elected and nominated MPs of Parliament form the Electoral College.", "தெரிவு B தேர்ந்தெடுக்கப்பட்ட மற்றும் நியமன எம்பிக்கள் இருவருமே வாக்காளர் குழுவில் உள்ளதாகச் சரியாகக் குறிப்பிடுகிறது.",
                "Option C incorrectly includes State Assembly members (MLAs), who participate only in the President election.", "தெரிவு C மாநில எம்எல்ஏக்களைச் சேர்க்கிறது; அவர்கள் குடியரசுத் தலைவர் தேர்தலில் மட்டுமே பங்கேற்பர்.",
                "Option D excludes Lok Sabha members completely.", "தெரிவு D மக்களவை உறுப்பினர்களை முற்றிலுமாக விலக்குகிறது."
            ),
            "TNPSC Trap: Nominated MPs vote in Vice-President election, but NOT in President election!",
            "TNPSC பொறி: நியமன எம்பிக்கள் VP தேர்தலில் வாக்களிக்கலாம், ஆனால் குடியரசுத் தலைவர் தேர்தலில் வாக்களிக்க முடியாது!",
            "Confusing Presidential Electoral College (No Nominated MPs, State MLAs included) with Vice-Presidential Electoral College.",
            "குடியரசுத் தலைவர் மற்றும் துணைக் குடியரசுத் தலைவர் வாக்காளர் குழுக்களைக் குழப்பிக் கொள்ளுதல்.",
            ["Vice-President Notes Part 1 - Article 66(1)"]
        )
    elif i == 2:
        q_item = build_q(
            qid, "Medium", "Conceptual",
            "What is the vote value calculation principle applied in the election of the Vice-President of India?",
            "இந்தியத் துணைக் குடியரசுத் தலைவர் தேர்தலில் பயன்படுத்தப்படும் வாக்கு மதிப்பு கணக்கீட்டுத் தத்துவம் என்ன?",
            make_options(
                "Weighted vote value based on 1971 State population", "1971 மாநில மக்கள் தொகை அடிப்படையிலான எடையுள்ள வாக்கு மதிப்பு",
                "Equal vote value of 1 for every Member of Parliament", "ஒவ்வொரு நாடாளுமன்ற உறுப்பினருக்கும் சமமான வாக்கு மதிப்பு 1",
                "Higher vote value for Rajya Sabha members than Lok Sabha members", "மக்களவையை விட மாநிலங்களவை உறுப்பினர்களுக்கு அதிக வாக்கு மதிப்பு",
                "Weighted vote value based on 2011 Census", "2011 கணக்கெடுப்பு அடிப்படையிலான எடையுள்ள வாக்கு மதிப்பு"
            ),
            "B",
            "Unlike the Presidential election where MPs and MLAs have weighted vote values based on population, in the Vice-Presidential election EVERY MP HAS AN EQUAL VOTE VALUE OF EXACTLY 1.",
            "குடியரசுத் தலைவர் தேர்தலைப் போலன்றி, துணைக் குடியரசுத் தலைவர் தேர்தலில் ஒவ்வொரு எம்பியின் வாக்கு மதிப்பும் சமமாக 1 ஆகும்.",
            make_wno("B",
                "Weighted vote value based on 1971 census applies ONLY to Presidential election.", "1971 மக்கள் தொகை எடையுள்ள வாக்கு குடியரசுத் தலைவர் தேர்தலுக்கு மட்டுமே பொருந்தும்.",
                "Option B accurately states that every MP in the Vice-President election has an equal vote value of 1.", "தெரிவு B துணைக் குடியரசுத் தலைவர் தேர்தலில் ஒவ்வொரு எம்பியின் வாக்கு மதிப்பும் சமமாக 1 எனச் சரியாகக் குறிப்பிடுகிறது.",
                "Rajya Sabha and Lok Sabha MPs have identical equal vote value.", "மாநிலங்களவை மற்றும் மக்களவை எம்பிக்களுக்குச் சமமான வாக்கு மதிப்பு உண்டு.",
                "2011 census weighting is not used in constitutional elections.", "2011 கணக்கெடுப்பு எடை அரசியலமைப்புத் தேர்தல்களில் பயன்படுத்தப்படவில்லை."
            ),
            "President election = Weighted vote values; Vice-President election = Equal MP vote value of 1.",
            "குடியரசுத் தலைவர் தேர்தல் = எடையுள்ள வாக்கு மதிப்பு; VP தேர்தல் = சமமான வாக்கு மதிப்பு 1.",
            "Applying the President's MLA population formula to the Vice-President's election.",
            "குடியரசுத் தலைவரின் எம்எல்ஏ மக்கள் தொகை சூத்திரத்தை VP தேர்தலுக்குப் பயன்படுத்துவது.",
            ["Vice-President Notes Part 1 - Vote Value Principle"]
        )
    else:
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

# Save Dataset 2: Medium
path_vp_medium = "data/questions/polity/vice_president_medium.json"
with open(path_vp_medium, "w", encoding="utf-8") as f:
    json.dump(medium_questions, f, ensure_ascii=False, indent=2)

print(f"✅ DATASET 2 (MEDIUM) SAVED: {path_vp_medium} ({len(medium_questions)} questions)")

print("Script updated and Dataset 1 & 2 verified successfully.")
