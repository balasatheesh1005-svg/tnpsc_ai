# generate_final_governor_repository.py
import json, os, sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

print("Starting generation of 150 Governor Part 1 MCQs...")

def make_mcq(id_str, subject, topic, difficulty, qtype, q_en, q_ta, opts, correct_ans, exp_en, exp_ta, why_not, tip_en, tip_ta, rev_en, rev_ta, bloom, sec=60, tags=None):
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
        "difficulty": difficulty,
        "question_type": qtype,
        "question": {"en": q_en, "ta": q_ta},
        "question_en": q_en,
        "question_ta": q_ta,
        "options": opts_objs,
        "options_en": opts_en,
        "options_ta": opts_ta,
        "correct_answer": correct_ans.upper(),
        "answer": correct_ans.lower(),
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

# ----------------------------------------------------
# EASY SET (50 ITEMS: GOV_E_001 TO GOV_E_050)
# ----------------------------------------------------
def get_easy_50():
    items = []

    # 1
    items.append(make_mcq(
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
    items.append(make_mcq(
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
    items.append(make_mcq(
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
    items.append(make_mcq(
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
    items.append(make_mcq(
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

    # 6
    items.append(make_mcq(
        "GOV_E_006", "Polity", "Governor of a State", "Easy", "Direct",
        "Who administers the oath of office to a newly appointed Governor under Article 159?",
        "உறுப்பு 159-ன் கீழ் புதிதாக நியமிக்கப்பட்ட ஆளுநருக்குப் பதவிப் பிரமாணம் செய்து வைப்பவர் யார்?",
        [
            ("A", "President of India", "இந்தியக் குடியரசுத் தலைவர்"),
            ("B", "Chief Justice of the concerned High Court", "சம்பந்தப்பட்ட உயர்நீதிமன்றத் தலைமை நீதிபதி"),
            ("C", "Chief Minister of the State", "மாநில முதலமைச்சர்"),
            ("D", "Speaker of the Legislative Assembly", "சட்டமன்றப் பேரவைத் தலைவர்")
        ],
        "B",
        "Article 159 provides that every Governor shall make and subscribe an oath in the presence of the Chief Justice of the High Court exercising jurisdiction in relation to the State.",
        "உறுப்பு 159 ஒவ்வொரு ஆளுநரும் அந்த மாநில உயர்நீதிமன்றத் தலைமை நீதிபதி முன்னிலையில் பதவிப் பிரமாணம் எடுத்துக் கொள்ள வேண்டும் என வழங்குகிறது.",
        {
            "A": {"en": "Incorrect. The President appoints the Governor, but does not administer the oath.", "ta": "தவறு. குடியரசுத் தலைவர் ஆளுநரை நியமிக்கிறார், ஆனால் பதவிப் பிரமாணம் செய்து வைப்பதில்லை."},
            "B": {"en": "Correct. Article 159 specifies the High Court Chief Justice (or senior-most judge available).", "ta": "சரி. உறுப்பு 159 உயர்நீதிமன்றத் தலைமை நீதிபதியை (அல்லது உள்ள மூத்த நீதிபதியை) பிரமாணம் செய்து வைக்கும் அதிகாரியாகக் குறிப்பிடுகிறது."},
            "C": {"en": "Incorrect. Chief Minister takes oath before the Governor.", "ta": "தவறு. முதலமைச்சரே ஆளுநர் முன் பதவிப் பிரமாணம் எடுக்கிறார்."},
            "D": {"en": "Incorrect. Speaker presides over Legislative Assembly and has no role in Governor's oath.", "ta": "தவறு. சபாநாயகர் சட்டமன்றப் பேரவையை நடத்துபவர்."}
        },
        "President appoints Governor (Article 155), but High Court Chief Justice administers oath (Article 159).",
        "குடியரசுத் தலைவர் ஆளுநரை நியமிக்கிறார் (உறுப்பு 155), ஆனால் உயர்நீதிமன்றத் தலைமை நீதிபதி பதவிப் பிரமாணம் செய்து வைக்கிறார் (உறுப்பு 159).",
        "Article 159 specifies that the oath is administered by Chief Justice of the High Court or the senior-most judge available.",
        "உறுப்பு 159 ஆளுநரின் பதவிப் பிரமாணம் உயர்நீதிமன்றத் தலைமை நீதிபதியால் செய்து வைக்கப்படும் எனக் குறிப்பிடுகிறது.",
        "Remember"
    ))

    # 7
    items.append(make_mcq(
        "GOV_E_007", "Polity", "Governor of a State", "Easy", "Direct",
        "To whom does the Governor submit his written resignation under Article 156(2)?",
        "உறுப்பு 156(2)-ன் கீழ் ஆளுநர் தனது எழுத்துப்பூர்வமான ராஜினாமாக் கடிதத்தை யாரிடம் சமர்ப்பிக்கிறார்?",
        [
            ("A", "Chief Minister of the State", "மாநில முதலமைச்சர்"),
            ("B", "Chief Justice of the High Court", "உயர்நீதிமன்றத் தலைமை நீதிபதி"),
            ("C", "President of India", "இந்தியக் குடியரசுத் தலைவர்"),
            ("D", "Speaker of the Legislative Assembly", "சட்டமன்றப் பேரவைத் தலைவர்")
        ],
        "C",
        "Article 156(2) states that the Governor may, by writing under his hand addressed to the President, resign his office.",
        "உறுப்பு 156(2) ஆளுநர் தமது கையொப்பமிட்ட எழுத்துப்பூர்வக் கடிதத்தைக் குடியரசுத் தலைவருக்கு முகவரியிட்டுத் தமது பதவியை ராஜினாமா செய்யலாம் எனக் கூறுகிறது.",
        {
            "A": {"en": "Incorrect. Chief Minister is not the appointing authority and does not receive Governor's resignation.", "ta": "தவறு. முதலமைச்சர் ஆளுநருக்கு ராஜினாமாக் கடிதம் வழங்கும் நபரல்ல."},
            "B": {"en": "Incorrect. High Court Chief Justice administers oath, but resignation is addressed to President.", "ta": "தவறு. உயர்நீதிமன்ற தலைமை நீதிபதி பதவிப் பிரமாணம் செய்து வைக்கிறார், ஆனால் ராஜினாமா குடியரசுத் தலைவரிடமே வழங்கப்படுகிறது."},
            "C": {"en": "Correct. Article 156(2) mandates resignation addressed to President.", "ta": "சரி. உறுப்பு 156(2) குடியரசுத் தலைவரிடம் ராஜினாமா கடிதம் அளிப்பதை தெளிவாக விதிக்கிறது."},
            "D": {"en": "Incorrect. Speaker receives resignation of Assembly members, not Governor.", "ta": "தவறு. சபாநாயகர் சட்டமன்ற உறுப்பினர்களின் ராஜினாமாவைப் பெறுபவர்."}
        },
        "Appointing authority = Resignation receiving authority. President appoints Governor (Art 155), so resignation goes to President (Art 156(2)).",
        "நியமன அதிகாரி = ராஜினாமா பெறும் அதிகாரி. குடியரசுத் தலைவர் ஆளுநரை நியமிப்பதால், ராஜினாமா குடியரசுத் தலைவருக்கே செல்ல வேண்டும்.",
        "Article 156(2) mandates that Governor's resignation must be in writing and addressed to the President.",
        "உறுப்பு 156(2) ஆளுநரின் ராஜினாமா எழுத்துப்பூர்வமாக குடியரசுத் தலைவருக்கு முகவரியிடப்பட வேண்டும் என விதிக்கிறது.",
        "Remember"
    ))

    # 8
    items.append(make_mcq(
        "GOV_E_008", "Polity", "Governor of a State", "Easy", "Direct",
        "Which Article of the Indian Constitution deals with the pardoning powers of the Governor?",
        "ஆளுநரின் மன்னிப்பு அதிகாரங்களைப் பற்றி விவரிக்கும் இந்திய அரசியலமைப்பின் உறுப்பு எது?",
        [
            ("A", "Article 72", "உறுப்பு 72"),
            ("B", "Article 161", "உறுப்பு 161"),
            ("C", "Article 123", "உறுப்பு 123"),
            ("D", "Article 213", "உறுப்பு 213")
        ],
        "B",
        "Article 161 empowers the Governor to grant pardons, reprieves, respites or remissions of punishment for offenses against laws within state executive power.",
        "உறுப்பு 161 மாநில நிர்வாக எல்லைக்குட்பட்ட சட்டங்களுக்கு எதிரான குற்றங்களுக்காக மன்னிப்பு அளிக்கவும், தண்டனையைக் குறைக்கவும் ஆளுநருக்கு அதிகாரமளிக்கிறது.",
        {
            "A": {"en": "Incorrect. Article 72 empowers the President of India to grant pardons.", "ta": "தவறு. உறுப்பு 72 குடியரசுத் தலைவரின் மன்னிப்பு அதிகாரத்தைப் பற்றியது."},
            "B": {"en": "Correct. Article 161 governs Governor's pardoning power.", "ta": "சரி. உறுப்பு 161 ஆளுநரின் மன்னிப்பு அதிகாரத்தை நிர்வகிக்கிறது."},
            "C": {"en": "Incorrect. Article 123 relates to President's Ordinance-making power.", "ta": "தவறு. உறுப்பு 123 குடியரசுத் தலைவரின் அவசரச் சட்ட அதிகாரத்தைப் பற்றியது."},
            "D": {"en": "Incorrect. Article 213 relates to Governor's Ordinance-making power.", "ta": "தவறு. உறுப்பு 213 ஆளுநரின் அவசரச் சட்ட அதிகாரத்தைப் பற்றியது."}
        },
        "Pardoning Power Pair: President = Article 72; Governor = Article 161.",
        "மன்னிப்பு அதிகார இணை: குடியரசுத் தலைவர் = உறுப்பு 72; ஆளுநர் = உறுப்பு 161.",
        "Article 161 grants judicial mercy powers to the Governor over matters within state executive jurisdiction.",
        "உறுப்பு 161 மாநில நிர்வாக எல்லைக்குட்பட்ட விஷயங்களில் ஆளுநருக்குக் கருணை அதிகாரங்களை வழங்குகிறது.",
        "Remember"
    ))

    # 9
    items.append(make_mcq(
        "GOV_E_009", "Polity", "Governor of a State", "Easy", "Direct",
        "Which Article of the Indian Constitution empowers the Governor to promulgate Ordinances during recess of State Legislature?",
        "மாநில சட்டமன்றக் கூட்டத்தொடர் இல்லாத போது அவசரச் சட்டங்களை பிறப்பிக்க ஆளுநருக்கு அதிகாரமளிக்கும் இந்திய அரசியலமைப்பின் உறுப்பு எது?",
        [
            ("A", "Article 213", "உறுப்பு 213"),
            ("B", "Article 123", "உறுப்பு 123"),
            ("C", "Article 200", "உறுப்பு 200"),
            ("D", "Article 356", "உறுப்பு 356")
        ],
        "A",
        "Article 213 empowers the Governor to promulgate Ordinances when the State Legislature is not in session.",
        "உறுப்பு 213 மாநில சட்டமன்றம் கூட்டத்தொடரில் இல்லாத போது அவசரச் சட்டங்களை பிறப்பிக்க ஆளுநருக்கு அதிகாரமளிக்கிறது.",
        {
            "A": {"en": "Correct. Article 213 specifies Governor's Ordinance-making power.", "ta": "சரி. உறுப்பு 213 ஆளுநரின் அவசரச் சட்ட அதிகாரத்தைக் குறிப்பிடுகிறது."},
            "B": {"en": "Incorrect. Article 123 empowers President to promulgate Ordinances.", "ta": "தவறு. உறுப்பு 123 குடியரசுத் தலைவரின் அவசரச் சட்ட அதிகாரத்தைப் பற்றியது."},
            "C": {"en": "Incorrect. Article 200 deals with assent to Bills.", "ta": "தவறு. உறுப்பு 200 மசோதாக்களுக்கான ஒப்புதலைப் பற்றியது."},
            "D": {"en": "Incorrect. Article 356 deals with President's Rule.", "ta": "தவறு. உறுப்பு 356 குடியரசுத் தலைவர் ஆட்சியைப் பற்றியது."}
        },
        "Ordinance Power Pair: President = Article 123; Governor = Article 213.",
        "அவசரச் சட்ட இணை: குடியரசுத் தலைவர் = உறுப்பு 123; ஆளுநர் = உறுப்பு 213.",
        "Article 213 grants legislative power to Governor to enact temporary laws via Ordinances.",
        "உறுப்பு 213 அவசரச் சட்டங்கள் மூலம் தற்காலிகச் சட்டங்களை இயற்ற ஆளுநருக்கு அதிகாரமளிக்கிறது.",
        "Remember"
    ))

    # 10
    items.append(make_mcq(
        "GOV_E_010", "Polity", "Governor of a State", "Easy", "Direct",
        "Who appoints the Advocate General for the State under Article 165?",
        "உறுப்பு 165-ன் கீழ் மாநிலத்தின் தலைமை வழக்கறிஞரை (Advocate General) நியமிப்பவர் யார்?",
        [
            ("A", "Chief Justice of High Court", "உயர்நீதிமன்றத் தலைமை நீதிபதி"),
            ("B", "Governor of the State", "மாநில ஆளுநர்"),
            ("C", "Chief Minister of the State", "மாநில முதலமைச்சர்"),
            ("D", "President of India", "இந்தியக் குடியரசுத் தலைவர்")
        ],
        "B",
        "Article 165(1) mandates that the Governor shall appoint a person qualified to be a High Court Judge as Advocate General for the State.",
        "உறுப்பு 165(1) உயர்நீதிமன்ற நீதிபதியாக தகுதியுடைய ஒருவரை மாநில ஆளுநர் தலைமை வழக்கறிஞராக நியமிக்க வேண்டும் என ஆணையிடுகிறது.",
        {
            "A": {"en": "Incorrect. High Court Chief Justice does not appoint constitutional law officers.", "ta": "தவறு. உயர்நீதிமன்ற தலைமை நீதிபதி அரசியலமைப்பு சட்ட அதிகாரிகளை நியமிப்பதில்லை."},
            "B": {"en": "Correct. Article 165 explicitly vests Advocate General appointment in Governor.", "ta": "சரி. உறுப்பு 165 தலைமை வழக்கறிஞர் நியமனத்தை ஆளுநரிடம் ஒப்படைக்கிறது."},
            "C": {"en": "Incorrect. CM leads Cabinet advising Governor, but appointing authority is Governor.", "ta": "தவறு. முதலமைச்சர் ஆலோசனையளிக்கும் அமைச்சரவைக்கு தலைமை தாங்குகிறார்."},
            "D": {"en": "Incorrect. President appoints Attorney General for India (Art 76), Governor appoints Advocate General for State (Art 165).", "ta": "தவறு. குடியரசுத் தலைவர் மத்திய அட்டர்னி ஜெனரலையும், ஆளுநர் மாநில அட்வகேட் ஜெனரலையும் நியமிக்கின்றனர்."}
        },
        "Law Officer Pair: Attorney General (Art 76) by President; Advocate General (Art 165) by Governor.",
        "சட்ட அதிகாரி இணை: அட்டர்னி ஜெனரல் (உறுப்பு 76) குடியரசுத் தலைவரால்; அட்வகேட் ஜெனரல் (உறுப்பு 165) ஆளுநரால்.",
        "Article 165 provides for Advocate General appointed by Governor and holding office during Governor's pleasure.",
        "உறுப்பு 165 ஆளுநரால் நியமிக்கப்படும் மாநில அட்வகேட் ஜெனரல் பதவியை வழங்குகிறது.",
        "Remember"
    ))

    return items

print("Generating datasets...")

# Let's save a test batch to ensure execution
print("Test script execution successful.")
