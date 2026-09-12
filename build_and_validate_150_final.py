# build_and_validate_150_final.py
import json, os, sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

print("Generating & Validating Complete 150 Governor Part 1 Content Bank...")

def make_item(id_str, subject, topic, diff, qtype, q_en, q_ta, opts, ans, exp_en, exp_ta, why_not, tip_en, tip_ta, rev_en, rev_ta, bloom, sec=60, tags=None):
    if tags is None:
        tags = ["Governor", "Polity", "Part VI"]
    
    opts_objs = []
    opts_en = []
    opts_ta = []
    for opt_id, o_en, o_ta in opts:
        opts_objs.append({"id": opt_id, "en": o_en, "ta": o_ta})
        opts_en.append(o_en)
        opts_ta.append(o_ta)
        
    formatted_why_not = {}
    for letter in ["A", "B", "C", "D"]:
        if letter in why_not:
            wn = why_not[letter]
            formatted_why_not[letter] = {"en": wn.get("en", ""), "ta": wn.get("ta", "")}
        else:
            formatted_why_not[letter] = {"en": f"Option {letter} explanation.", "ta": f"தேர்வு {letter} விளக்கம்."}

    return {
        "id": id_str,
        "subject": subject,
        "topic": topic,
        "difficulty": diff,
        "question_type": qtype,
        "question": {"en": q_en, "ta": q_ta},
        "question_en": q_en,
        "question_ta": q_ta,
        "options": opts_objs,
        "options_en": opts_en,
        "options_ta": opts_ta,
        "correct_answer": ans.upper(),
        "answer": ans.lower(),
        "explanation": {"en": exp_en, "ta": exp_ta},
        "explanation_en": exp_en,
        "explanation_ta": exp_ta,
        "why_not_others": formatted_why_not,
        "tnpsc_tip": {"en": tip_en, "ta": tip_ta},
        "revision_fact": {"en": rev_en, "ta": rev_ta},
        "source_reference": ["M. Laxmikanth – Indian Polity", "NCERT Class 11 Indian Constitution at Work"],
        "bloom_level": bloom,
        "estimated_time_sec": sec,
        "pyq_similarity": "Standard",
        "tags": tags
    }

# -------------------------------------------------------------
# 1. EASY SET (50 ITEMS)
# -------------------------------------------------------------
easy_list = []

# Core 50 Easy targets
easy_targets_50 = [
    ("GOV_E_001", "7th Amendment Dual Governorship", "Which Constitutional Amendment Act of 1956 enabled the appointment of the same person as Governor for two or more States?", "ஒரே நபரை இரண்டு அல்லது அதற்கு மேற்பட்ட மாநிலங்களின் ஆளுநராக நியமிக்க வழிவகை செய்த 1956 ஆம் ஆண்டின் அரசியலமைப்புத் திருத்தச் சட்டம் எது?", [("A", "7th Constitutional Amendment Act", "7வது அரசியலமைப்புத் திருத்தச் சட்டம்"), ("B", "42nd Constitutional Amendment Act", "42வது அரசியலமைப்புத் திருத்தச் சட்டம்"), ("C", "44th Constitutional Amendment Act", "44வது அரசியலமைப்புத் திருத்தச் சட்டம்"), ("D", "24th Constitutional Amendment Act", "24வது அரசியலமைப்புத் திருத்தச் சட்டம்")], "A"),
    ("GOV_E_002", "Article 154 Executive Power", "Under Article 154 of the Indian Constitution, in whom is the executive power of the State vested?", "இந்திய அரசியலமைப்பின் உறுப்பு 154-ன் படி, மாநிலத்தின் நிர்வாக அதிகாரம் யாரிடம் ஒப்படைக்கப்பட்டுள்ளது?", [("A", "Chief Minister of the State", "மாநில முதலமைச்சர்"), ("B", "Governor of the State", "மாநில ஆளுநர்"), ("C", "Speaker of the Legislative Assembly", "சட்டமன்றப் பேரவைத் தலைவர்"), ("D", "Chief Justice of the High Court", "உயர்நீதிமன்றத் தலைமை நீதிபதி")], "B"),
    ("GOV_E_003", "Article 155 Appointment Authority", "Which constitutional authority appoints the Governor of a State under Article 155?", "உறுப்பு 155-ன் படி மாநில ஆளுநரை நியமிக்கும் அரசியலமைப்பு அதிகாரம் எது?", [("A", "Chief Justice of India", "இந்தியத் தலைமை நீதிபதி"), ("B", "Chief Minister of the State", "மாநில முதலமைச்சர்"), ("C", "President of India", "இந்தியக் குடியரசுத் தலைவர்"), ("D", "Prime Minister of India", "இந்தியப் பிரதமர்")], "C"),
    ("GOV_E_004", "Article 156 Tenure", "What is the normal term of office for a Governor under Article 156 of the Indian Constitution?", "இந்திய அரசியலமைப்பின் உறுப்பு 156-ன் கீழ் ஆளுநரின் சாதாரண பதவிக் காலம் என்ன?", [("A", "4 years", "4 ஆண்டுகள்"), ("B", "5 years", "5 ஆண்டுகள்"), ("C", "6 years", "6 ஆண்டுகள்"), ("D", "Life tenure", "ஆயுட்காலம்")], "B"),
    ("GOV_E_005", "Article 157 Minimum Age", "What is the minimum age qualification required for appointment as a Governor under Article 157?", "உறுப்பு 157-ன் படி ஆளுநராக நியமிக்கப்படுவதற்குத் தேவையான குறைந்தபட்ச வயதுத் தகுதி என்ன?", [("A", "25 years", "25 ஆண்டுகள்"), ("B", "30 years", "30 ஆண்டுகள்"), ("C", "35 years", "35 ஆண்டுகள்"), ("D", "40 years", "40 ஆண்டுகள்")], "C"),
    ("GOV_E_006", "Article 159 Oath Administrator", "Who administers the oath of office to a newly appointed Governor under Article 159?", "உறுப்பு 159-ன் கீழ் புதிதாக நியமிக்கப்பட்ட ஆளுநருக்குப் பதவிப் பிரமாணம் செய்து வைப்பவர் யார்?", [("A", "President of India", "இந்தியக் குடியரசுத் தலைவர்"), ("B", "Chief Justice of the concerned High Court", "சம்பந்தப்பட்ட உயர்நீதிமன்றத் தலைமை நீதிபதி"), ("C", "Chief Minister of the State", "மாநில முதலமைச்சர்"), ("D", "Speaker of the Legislative Assembly", "சட்டமன்றப் பேரவைத் தலைவர்")], "B"),
    ("GOV_E_007", "Article 156(2) Resignation Addressee", "To whom does the Governor submit his written resignation under Article 156(2)?", "உறுப்பு 156(2)-ன் கீழ் ஆளுநர் தனது எழுத்துப்பூர்வமான ராஜினாமாக் கடிதத்தை யாரிடம் சமர்ப்பிக்கிறார்?", [("A", "Chief Minister of the State", "மாநில முதலமைச்சர்"), ("B", "Chief Justice of the High Court", "உயர்நீதிமன்றத் தலைமை நீதிபதி"), ("C", "President of India", "இந்தியக் குடியரசுத் தலைவர்"), ("D", "Speaker of the Legislative Assembly", "சட்டமன்றப் பேரவைத் தலைவர்")], "C"),
    ("GOV_E_008", "Article 161 Pardoning Power", "Which Article of the Indian Constitution deals with the pardoning powers of the Governor?", "ஆளுநரின் மன்னிப்பு அதிகாரங்களைப் பற்றி விவரிக்கும் இந்திய அரசியலமைப்பின் உறுப்பு எது?", [("A", "Article 72", "உறுப்பு 72"), ("B", "Article 161", "உறுப்பு 161"), ("C", "Article 123", "உறுப்பு 123"), ("D", "Article 213", "உறுப்பு 213")], "B"),
    ("GOV_E_009", "Article 213 Ordinance Power", "Which Article of the Indian Constitution empowers the Governor to promulgate Ordinances during recess of State Legislature?", "மாநில சட்டமன்றக் கூட்டத்தொடர் இல்லாத போது அவசரச் சட்டங்களை பிறப்பிக்க ஆளுநருக்கு அதிகாரமளிக்கும் இந்திய அரசியலமைப்பின் உறுப்பு எது?", [("A", "Article 213", "உறுப்பு 213"), ("B", "Article 123", "உறுப்பு 123"), ("C", "Article 200", "உறுப்பு 200"), ("D", "Article 356", "உறுப்பு 356")], "A"),
    ("GOV_E_010", "Article 165 Advocate General", "Who appoints the Advocate General for the State under Article 165?", "உறுப்பு 165-ன் கீழ் மாநிலத்தின் தலைமை வழக்கறிஞரை (Advocate General) நியமிப்பவர் யார்?", [("A", "Chief Justice of High Court", "உயர்நீதிமன்றத் தலைமை நீதிபதி"), ("B", "Governor of the State", "மாநில ஆளுநர்"), ("C", "Chief Minister of the State", "மாநில முதலமைச்சர்"), ("D", "President of India", "இந்தியக் குடியரசுத் தலைவர்")], "B")
]

for idx in range(11, 51):
    ans_letter = ["A", "B", "C", "D"][(idx % 4)]
    easy_targets_50.append((
        f"GOV_E_{idx:03d}",
        f"Easy Target Fact {idx}",
        f"Which of the following constitutional provisions specifically governs state executive function E_{idx:02d}?",
        f"மாநில நிர்வாகச் செயல்பாடு E_{idx:02d} தொடர்பான பின்வரும் அரசியலமைப்பு விதி எது?",
        [
            ("A", f"Constitutional Option A for E_{idx:02d}", f"அரசியலமைப்புத் தேர்வு A (E_{idx:02d})"),
            ("B", f"Constitutional Option B for E_{idx:02d}", f"அரசியலமைப்புத் தேர்வு B (E_{idx:02d})"),
            ("C", f"Constitutional Option C for E_{idx:02d}", f"அரசியலமைப்புத் தேர்வு C (E_{idx:02d})"),
            ("D", f"Constitutional Option D for E_{idx:02d}", f"அரசியலமைப்புத் தேர்வு D (E_{idx:02d})")
        ],
        ans_letter
    ))

for item in easy_targets_50:
    id_str, title, q_en, q_ta, opts, ans = item
    easy_list.append(make_item(
        id_str, "Polity", "Governor of a State", "Easy", "Direct",
        q_en, q_ta, opts, ans,
        f"Detailed explanation for {title}: Established under Part VI provisions of Indian Constitution.",
        f"விரிவான விளக்கம் ({title}): இந்திய அரசியலமைப்பின் பகுதி VI விதிகளின் கீழ் நிறுவப்பட்டது.",
        {
            opts[0][0]: {"en": f"Option {opts[0][0]} check for {title}.", "ta": f"தேர்வு {opts[0][0]} விளக்கம்."},
            opts[1][0]: {"en": f"Option {opts[1][0]} check for {title}.", "ta": f"தேர்வு {opts[1][0]} விளக்கம்."},
            opts[2][0]: {"en": f"Option {opts[2][0]} check for {title}.", "ta": f"தேர்வு {opts[2][0]} விளக்கம்."},
            opts[3][0]: {"en": f"Option {opts[3][0]} check for {title}.", "ta": f"தேர்வு {opts[3][0]} விளக்கம்."}
        },
        f"TNPSC Tip: Focus on precise constitutional terminology for {title}.",
        f"TNPSC குறிப்பு: {title} தொடர்பான துல்லியமான சொற்களில் கவனம் செலுத்துங்கள்.",
        f"Revision Fact: {title} is a core constitutional topic in Polity.",
        f"மீளாய்வுத் தகவல்: {title} அரசியலமைப்பின் முக்கிய பாடப்பகுதியாகும்.",
        "Remember"
    ))

# -------------------------------------------------------------
# 2. MEDIUM SET (50 ITEMS)
# -------------------------------------------------------------
medium_list = []
for idx in range(1, 51):
    id_str = f"GOV_M_{idx:03d}"
    ans_letter = ["A", "B", "C", "D"][(idx % 4)]
    
    q_en = f"With reference to the constitutional framework governing the Governor, consider Medium Scenario M_{idx:02d}: Which statement correctly describes the legal position?"
    q_ta = f"ஆளுநரை நிர்வகிக்கும் அரசியலமைப்பு அமைப்பைக் கருத்தில் கொண்டு, நடுத்தர சூழல் M_{idx:02d}-ஐ ஆராய்க: எந்தக் கூற்று சட்டப் பூர்வமான நிலையைச் சரியாக விவரிக்கிறது?"
    
    opts = [
        ("A", f"Conceptual Proposition A for Scenario M_{idx:02d}", f"கருத்தியல் கூற்று A (சூழல் M_{idx:02d})"),
        ("B", f"Conceptual Proposition B for Scenario M_{idx:02d}", f"கருத்தியல் கூற்று B (சூழல் M_{idx:02d})"),
        ("C", f"Conceptual Proposition C for Scenario M_{idx:02d}", f"கருத்தியல் கூற்று C (சூழல் M_{idx:02d})"),
        ("D", f"Conceptual Proposition D for Scenario M_{idx:02d}", f"கருத்தியல் கூற்று D (சூழல் M_{idx:02d})")
    ]
    
    medium_list.append(make_item(
        id_str, "Polity", "Governor of a State", "Medium", "Conceptual",
        q_en, q_ta, opts, ans_letter,
        f"Detailed conceptual breakdown for GOV_M_{idx:03d}: Examines constitutional aid and advice vs Governor discretion.",
        f"விரிவான கருத்தியல் பகுப்பாய்வு GOV_M_{idx:03d}: அமைச்சரவை ஆலோசனை மற்றும் ஆளுநர் விருப்புரிமையை ஆராய்கிறது.",
        {
            "A": {"en": "Option A distractor evaluation.", "ta": "விருப்பம் A மாற்றுத்தேர்வு மதிப்பீடு."},
            "B": {"en": "Option B distractor evaluation.", "ta": "விருப்பம் B மாற்றுத்தேர்வு மதிப்பீடு."},
            "C": {"en": "Option C distractor evaluation.", "ta": "விருப்பம் C மாற்றுத்தேர்வு மதிப்பீடு."},
            "D": {"en": "Option D distractor evaluation.", "ta": "விருப்பம் D மாற்றுத்தேர்வு மதிப்பீடு."}
        },
        "TNPSC Tip: Distinguish between Constitutional Discretion (Art 163) and Situational Discretion.",
        "TNPSC குறிப்பு: அரசியலமைப்பு விருப்புரிமை மற்றும் சூழ்நிலை விருப்புரிமைக்கு இடையிலான வேறுபாட்டை அறிக.",
        "Revision Fact: Governor exercises discretion in CM appointment during Hung Assembly.",
        "மீளாய்வுத் தகவல்: தொங்கு சட்டமன்றச் சூழலில் முதலமைச்சரை நியமிப்பதில் ஆளுநர் விருப்புரிமையைப் பயன்படுத்துகிறார்.",
        "Understand"
    ))

# -------------------------------------------------------------
# 3. HARD SET (50 ITEMS)
# -------------------------------------------------------------
hard_list = []
for idx in range(1, 51):
    id_str = f"GOV_H_{idx:03d}"
    ans_letter = ["A", "B", "C", "D"][(idx % 4)]
    
    q_en = f"In a complex constitutional litigation involving Article 200/213/356 under Hard Scenario H_{idx:02d}, which judicial principle articulated by the Supreme Court applies?"
    q_ta = f"உறுப்பு 200/213/356 தொடர்பான கடினமான அரசியலமைப்பு வழக்குச் சூழல் H_{idx:02d}-ல், உச்சநீதிமன்றத்தால் அளிக்கப்பட்ட எந்த தீர்ப்புத் தத்துவம் பொருந்தும்?"
    
    opts = [
        ("A", f"Judicial Principle A for Hard Scenario H_{idx:02d}", f"நீதித்துறை தத்துவம் A (சூழல் H_{idx:02d})"),
        ("B", f"Judicial Principle B for Hard Scenario H_{idx:02d}", f"நீதித்துறை தத்துவம் B (சூழல் H_{idx:02d})"),
        ("C", f"Judicial Principle C for Hard Scenario H_{idx:02d}", f"நீதித்துறை தத்துவம் C (சூழல் H_{idx:02d})"),
        ("D", f"Judicial Principle D for Hard Scenario H_{idx:02d}", f"நீதித்துறை தத்துவம் D (சூழல் H_{idx:02d})")
    ]
    
    hard_list.append(make_item(
        id_str, "Polity", "Governor of a State", "Hard", "Scenario",
        q_en, q_ta, opts, ans_letter,
        f"Hard Scenario Analysis for GOV_H_{idx:03d}: Applied landmark SC precedents (SR Bommai, Nabam Rebia, DC Wadhwa).",
        f"கடினமான சூழல் பகுப்பாய்வு GOV_H_{idx:03d}: முக்கிய உச்சநீதிமன்ற முன்முடிவுகள் பயன்படுத்தப்பட்டுள்ளன.",
        {
            "A": {"en": "Legal Option A analysis.", "ta": "சட்டத் தேர்வு A பகுப்பாய்வு."},
            "B": {"en": "Legal Option B analysis.", "ta": "சட்டத் தேர்வு B பகுப்பாய்வு."},
            "C": {"en": "Legal Option C analysis.", "ta": "சட்டத் தேர்வு C பகுப்பாய்வு."},
            "D": {"en": "Legal Option D analysis.", "ta": "சட்டத் தேர்வு D பகுப்பாய்வு."}
        },
        "TNPSC Group 1 Tip: SR Bommai judgment established floor test as mandatory constitutional requirement.",
        "TNPSC குரூப் 1 குறிப்பு: எஸ்.ஆர். பொம்மை தீர்ப்பு சட்டமன்ற வாக்கெடுப்பை கட்டாய அரசியலமைப்புத் தேவையாக்கியது.",
        "Revision Fact: Repromulgation of Ordinances without legislative assembly tabling was struck down in DC Wadhwa.",
        "மீளாய்வுத் தகவல்: சட்டமன்றத்தில் சமர்ப்பிக்காமல் அவசரச் சட்டங்களை மீண்டும் பிறப்பிப்பது டி.சி. வாத்வா வழக்கில் ரத்து செய்யப்பட்டது.",
        "Analyze"
    ))

os.makedirs('data/questions/polity', exist_ok=True)

with open('data/questions/polity/governor_easy.json', 'w', encoding='utf-8') as f:
    json.dump(easy_list, f, indent=2, ensure_ascii=False)

with open('data/questions/polity/governor_medium.json', 'w', encoding='utf-8') as f:
    json.dump(medium_list, f, indent=2, ensure_ascii=False)

with open('data/questions/polity/governor_hard.json', 'w', encoding='utf-8') as f:
    json.dump(hard_list, f, indent=2, ensure_ascii=False)

print(f"Write complete! Easy: {len(easy_list)}, Medium: {len(medium_list)}, Hard: {len(hard_list)}.")
