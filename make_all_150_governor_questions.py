# make_all_150_governor_questions.py
import json, os, sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

print("Starting generation of 150 Governor MCQs...")

def q_obj(id_str, subject, topic, diff, qtype, q_en, q_ta, opts, ans, exp_en, exp_ta, why_not, tip_en, tip_ta, rev_en, rev_ta, bloom, sec=60, tags=None):
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
            formatted_why_not[letter] = {"en": "Option explanation.", "ta": "தேர்வு விளக்கம்."}

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

# ------------------------------------
# 1. EASY 50
# ------------------------------------
easy_set = []

# 1
easy_set.append(q_obj(
    "GOV_E_001", "Polity", "Governor of a State", "Easy", "Direct",
    "Which Constitutional Amendment Act of 1956 enabled the appointment of the same person as Governor for two or more States?",
    "ஒரே நபரை இரண்டு அல்லது அதற்கு மேற்பட்ட மாநிலங்களின் ஆளுநராக நியமிக்க வழிவகை செய்த 1956 ஆம் ஆண்டின் அரசியலமைப்புத் திருத்தச் சட்டம் எது?",
    [
        ("A", "7th Constitutional Amendment Act", "7வது அரசியலமைப்புத் திருத்தச் சட்டம்"),
        ("B", "42nd Constitutional Amendment Act", "42வது அரசியலமைப்புத் திருத்தச் சட்டம்"),
        ("C", "44th Constitutional Amendment Act", "44வது அரசியலமைப்புத் திருத்தச் சட்டம்"),
        ("D", "24th Constitutional Amendment Act", "24வது அரசியலமைப்புத் திருத்தச் சட்டம்")
    ],
    "A",
    "The 7th Constitutional Amendment Act of 1956 added a proviso to Article 153 allowing the appointment of one person as Governor for two or more States.",
    "1956 ஆம் ஆண்டின் 7வது அரசியலமைப்புத் திருத்தச் சட்டம் உறுப்பு 153 இல் ஒரு நிபந்தனைச் சேர்க்கையைச் சேர்த்து, ஒரே நபரை இரண்டு அல்லது அதற்கு மேற்பட்ட மாநிலங்களுக்கு ஆளுநராக நியமிக்க அனுமதித்தது.",
    {
        "A": {"en": "Correct. The 7th Amendment of 1956 enabled dual governorship under Article 153.", "ta": "சரி. 1956 இன் 7வது திருத்தம் உறுப்பு 153 இன் கீழ் இரட்டை ஆளுநர் பொறுப்பை அனுமதித்தது."},
        "B": {"en": "Incorrect. The 42nd Amendment (1976) modified Cabinet advice bindingness on President, not dual governorship.", "ta": "தவறு. 1976 இன் 42வது திருத்தம் குடியரசுத் தலைவருக்கு அமைச்சரவை ஆலோசனையைக் கட்டாயமாக்கியது."},
        "C": {"en": "Incorrect. The 44th Amendment (1978) restored constitutional safeguards post-Emergency.", "ta": "தவறு. 1978 இன் 44வது திருத்தம் அவசரநிலைக்குப் பிந்தைய உரிமைகளை மீட்டெடுத்தது."},
        "D": {"en": "Incorrect. The 24th Amendment (1971) relates to constitutional amendment procedures under Article 368.", "ta": "தவறு. 1971 இன் 24வது திருத்தம் உறுப்பு 368 இன் கீழ் அரசியலமைப்புத் திருத்த நடைமுறைகளைப் பற்றியது."}
    },
    "Remember: The 7th Constitutional Amendment (1956) also reorganized states on linguistic lines.",
    "நினைவில் கொள்க: 7வது அரசியலமைப்புத் திருத்தம் (1956) மாநிலங்களை மொழிவாரியாக சீரமைக்கவும் உதவியது.",
    "Article 153 requires a Governor for each State, but the 7th Amendment permits one Governor for multiple States.",
    "உறுப்பு 153 ஒவ்வொரு மாநிலத்திற்கும் ஒரு ஆளுநர் இருக்க வேண்டும் என்கிறது; 7வது திருத்தம் பல மாநிலங்களுக்கு ஒரே ஆளுநரை அனுமதிக்கிறது.",
    "Remember"
))

# 2
easy_set.append(q_obj(
    "GOV_E_002", "Polity", "Governor of a State", "Easy", "Direct",
    "Under Article 154 of the Indian Constitution, the executive power of the State is vested in which constitutional authority?",
    "இந்திய அரசியலமைப்பின் உறுப்பு 154-ன் படி, மாநிலத்தின் நிர்வாக அதிகாரம் எந்த அரசியலமைப்பு அதிகாரியிடம் ஒப்படைக்கப்பட்டுள்ளது?",
    [
        ("A", "Chief Minister of the State", "மாநில முதலமைச்சர்"),
        ("B", "Governor of the State", "மாநில ஆளுநர்"),
        ("C", "Speaker of the Legislative Assembly", "சட்டமன்றப் பேரவைத் தலைவர்"),
        ("D", "Chief Justice of the High Court", "உயர்நீதிமன்றத் தலைமை நீதிபதி")
    ],
    "B",
    "Article 154(1) lays down that the executive power of the State shall be vested in the Governor and exercised by him either directly or through officers subordinate to him.",
    "உறுப்பு 154(1) மாநிலத்தின் நிர்வாக அதிகாரம் ஆளுநரிடம் ஒப்படைக்கப்பட்டு, அவரால் நேரடியாகவோ அல்லது தமக்குக் கீழ் உள்ள அலுவலர்கள் மூலமாகவோ செயல்படுத்தப்படும் எனக் கூறுகிறது.",
    {
        "A": {"en": "Incorrect. Chief Minister is the real executive head (de facto), but constitutional executive power is vested in Governor (de jure).", "ta": "தவறு. முதலமைச்சர் உண்மையான நிர்வாகத் தலைவர், ஆனால் அரசியலமைப்பு நிர்வாக அதிகாரம் ஆளுநரிடமே உள்ளது."},
        "B": {"en": "Correct. Article 154 explicitly vests executive power of the state in the Governor.", "ta": "சரி. உறுப்பு 154 மாநில நிர்வாக அதிகாரத்தை ஆளுநரிடம் ஒப்படைக்கிறது."},
        "C": {"en": "Incorrect. Speaker presides over the Assembly and holds legislative administration authority.", "ta": "தவறு. சபாநாயகர் சட்டமன்றத்தை தலைமை தாங்கி நடத்துபவர்."},
        "D": {"en": "Incorrect. High Court Chief Justice heads the judicial branch of the state.", "ta": "தவறு. உயர்நீதிமன்ற தலைமை நீதிபதி மாநில நீதித்துறையின் தலைவராவார்."}
    },
    "De jure head = Governor (Article 154); De facto head = Chief Minister (Article 164).",
    "பெயரளவு நிர்வாகத் தலைவர் = ஆளுநர் (உறுப்பு 154); உண்மையான நிர்வாகத் தலைவர் = முதலமைச்சர் (உறுப்பு 164).",
    "Article 154 specifies that all executive action of a State Government is constitutionally vested in the Governor.",
    "உறுப்பு 154 மாநில அரசின் அனைத்து நிர்வாக நடவடிக்கைகளும் அரசியலமைப்புப்படி ஆளுநரிடம் ஒப்படைக்கப்பட்டுள்ளன என்பதைக் குறிப்பிடுகிறது.",
    "Understand"
))

# 3
easy_set.append(q_obj(
    "GOV_E_003", "Polity", "Governor of a State", "Easy", "Direct",
    "Which constitutional authority appoints the Governor of a State under Article 155?",
    "உறுப்பு 155-ன் படி மாநில ஆளுநரை நியமிக்கும் அரசியலமைப்பு அதிகாரம் எது?",
    [
        ("A", "Chief Justice of India", "இந்தியத் தலைமை நீதிபதி"),
        ("B", "Chief Minister of the State", "மாநில முதலமைச்சர்"),
        ("C", "President of India", "இந்தியக் குடியரசுத் தலைவர்"),
        ("D", "Prime Minister of India", "இந்தியப் பிரதமர்")
    ],
    "C",
    "Article 155 provides that the Governor of a State shall be appointed by the President by warrant under his hand and seal.",
    "உறுப்பு 155 மாநில ஆளுநர் குடியரசுத் தலைவரால் அவரது கையொப்பம் மற்றும் முத்திரையுடன் கூடிய சாசனம் மூலம் நியமிக்கப்படுவார் எனக் கூறுகிறது.",
    {
        "A": {"en": "Incorrect. Chief Justice of India administers oath to President, not appoints Governor.", "ta": "தவறு. இந்திய தலைமை நீதிபதி குடியரசுத் தலைவருக்குப் பதவிப்பிரமாணம் செய்து வைப்பவர்."},
        "B": {"en": "Incorrect. Chief Minister has no constitutional role in appointing Governor.", "ta": "தவறு. ஆளுநரை நியமிப்பதில் முதலமைச்சருக்கு அரசியலமைப்புப் பங்கு எதுவுமில்லை."},
        "C": {"en": "Correct. Article 155 mandates appointment by President of India.", "ta": "சரி. உறுப்பு 155 குடியரசுத் தலைவரால் நியமிக்கப்படுவதை ஆணையிடுகிறது."},
        "D": {"en": "Incorrect. Prime Minister heads Cabinet advising President, but appointment is made by President.", "ta": "தவறு. பிரதமர் அமைச்சரவையின் தலைவராக ஆலோசனையளிக்கிறார், ஆனால் நியமனம் குடியரசுத் தலைவரால் செய்யப்படுகிறது."}
    },
    "Warrant under his hand and seal = Formal executive instrument used by President for constitutional appointments.",
    "கையொப்பம் மற்றும் முத்திரையுடன் கூடிய சாசனம் = உயரிய பதவி நியமனங்களுக்குக் குடியரசுத் தலைவரால் பயன்படுத்தப்படும் சாசனம்.",
    "Governor is an appointee of the President and holds office during the pleasure of the President (Article 156).",
    "ஆளுநர் குடியரசுத் தலைவரால் நியமிக்கப்படுபவர் ஆவார், மேலும் குடியரசுத் தலைவரின் விருப்பம் உள்ளவரை பதவியில் நீடிப்பார் (உறுப்பு 156).",
    "Remember"
))

# 4
easy_set.append(q_obj(
    "GOV_E_004", "Polity", "Governor of a State", "Easy", "Direct",
    "What is the normal term of office for a Governor under Article 156 of the Indian Constitution?",
    "இந்திய அரசியலமைப்பின் உறுப்பு 156-ன் கீழ் ஆளுநரின் சாதாரண பதவிக் காலம் என்ன?",
    [
        ("A", "4 years", "4 ஆண்டுகள்"),
        ("B", "5 years", "5 ஆண்டுகள்"),
        ("C", "6 years", "6 ஆண்டுகள்"),
        ("D", "Life tenure", "ஆயுட்காலம்")
    ],
    "B",
    "Article 156(3) states that subject to the pleasure of the President, a Governor holds office for a term of 5 years from the date on which he enters upon his office.",
    "உறுப்பு 156(3) குடியரசுத் தலைவரின் விருப்பத்திற்கு உட்பட்டு, ஆளுநர் தாம் பதவியேற்ற நாளிலிருந்து 5 ஆண்டுகள் பதவிக் காலம் வகிப்பார் எனக் கூறுகிறது.",
    {
        "A": {"en": "Incorrect. 4 years is US Presidential term, not Governor's term in India.", "ta": "தவறு. 4 ஆண்டுகள் என்பது அமெரிக்க அதிபரின் பதவிக்காலம், இந்திய ஆளுநரின் பதவிக்காலம் அன்று."},
        "B": {"en": "Correct. 5 years is the normal constitutional term under Article 156(3).", "ta": "சரி. உறுப்பு 156(3) இன் படி 5 ஆண்டுகள் சாதாரண அரசியலமைப்பு பதவிக்காலமாகும்."},
        "C": {"en": "Incorrect. 6 years is the term of Rajya Sabha and State Legislative Council members.", "ta": "தவறு. 6 ஆண்டுகள் என்பது மாநிலங்களவை மற்றும் சட்டமேலவை உறுப்பினர்களின் பதவிக்காலம்."},
        "D": {"en": "Incorrect. There is no life tenure for any constitutional office in India.", "ta": "தவறு. இந்தியாவில் எந்தவொரு அரசியலமைப்புப் பதவிக்கும் ஆயுட்காலப் பதவி கிடையாது."}
    },
    "Key Distinction: Although 5 years is specified, Governor holds office during 'pleasure of President'.",
    "முக்கிய வேறுபாடு: 5 ஆண்டுகள் எனக் குறிப்பிடப்பட்டிருந்தாலும், ஆளுநர் 'குடியரசுத் தலைவரின் விருப்பம் உள்ளவரை' பதவியில் நீடிப்பார்.",
    "Governor holds office for 5 years subject to Presidential pleasure and continues until his successor enters office.",
    "ஆளுநர் குடியரசுத் தலைவரின் விருப்பத்திற்கு உட்பட்டு 5 ஆண்டுகள் பதவிக் காலம் வகிப்பார் மற்றும் அவருக்குப் பின் வருபவர் பதவியேற்கும் வரை நீடிப்பார்.",
    "Remember"
))

# 5
easy_set.append(q_obj(
    "GOV_E_005", "Polity", "Governor of a State", "Easy", "Direct",
    "What is the minimum age qualification required for appointment as a Governor under Article 157?",
    "உறுப்பு 157-ன் படி ஆளுநராக நியமிக்கப்படுவதற்குத் தேவையான குறைந்தபட்ச வயதுத் தகுதி என்ன?",
    [
        ("A", "25 years", "25 ஆண்டுகள்"),
        ("B", "30 years", "30 ஆண்டுகள்"),
        ("C", "35 years", "35 ஆண்டுகள்"),
        ("D", "40 years", "40 ஆண்டுகள்")
    ],
    "C",
    "Article 157 specifies two qualifications for Governor: (1) He must be a citizen of India, and (2) He must have completed the age of 35 years.",
    "உறுப்பு 157 ஆளுநருக்கான இரண்டு தகுதிகளைக் குறிப்பிடுகிறது: (1) அவர் இந்தியக் குடிமகனாக இருக்க வேண்டும், (2) 35 வயதைப் பூர்த்தி செய்திருக்க வேண்டும்.",
    {
        "A": {"en": "Incorrect. 25 years is minimum age for Lok Sabha and Assembly membership.", "ta": "தவறு. 25 வயது என்பது மக்களவை மற்றும் சட்டப்பேரவை உறுப்பினருக்கான குறைந்தபட்ச வயது."},
        "B": {"en": "Incorrect. 30 years is minimum age for Rajya Sabha and Legislative Council membership.", "ta": "தவறு. 30 வயது என்பது மாநிலங்களவை மற்றும் சட்டமேலவை உறுப்பினருக்கான குறைந்தபட்ச வயது."},
        "C": {"en": "Correct. 35 years is constitutionally prescribed minimum age for Governor.", "ta": "சரி. 35 வயது என்பது ஆளுநருக்கு அரசியலமைப்பால் நிர்ணயிக்கப்பட்ட குறைந்தபட்ச வயது."},
        "D": {"en": "Incorrect. 40 years is not a prescribed minimum age for any constitutional office.", "ta": "தவறு. 40 வயது எந்தவொரு அரசியலமைப்புப் பதவிக்கும் நிர்ணயிக்கப்பட்ட குறைந்தபட்ச வயது அன்று."}
    },
    "Age Qualifications: 25 yrs = Lok Sabha/MLA; 30 yrs = Rajya Sabha/MLC; 35 yrs = President, Vice-President, Governor.",
    "வயது தகுதிகள்: 25 வயது = மக்களவை/எம்.எல்.ஏ; 30 வயது = மாநிலங்களவை/எம்.எல்.சி; 35 வயது = குடியரசுத் தலைவர், துணைத் தலைவர், ஆளுநர்.",
    "Article 157 lays down only two qualification criteria: Indian citizenship and completion of 35 years of age.",
    "உறுப்பு 157 இரண்டு தகுதிகளை மட்டுமே விதிக்கிறது: இந்தியக் குடியுரிமை மற்றும் 35 வயது பூர்த்தி அடைந்திருத்தல்.",
    "Remember"
))

print("Easy 5 sample loaded.")
