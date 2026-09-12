# scratch/make_easy_questions.py
import json

def get_easy_questions():
    q = []

    # 1 to 10
    q.append({
        "id": "GOV_E_001",
        "subject": "Polity",
        "topic": "Governor of a State",
        "difficulty": "Easy",
        "question_type": "Direct",
        "question": {
            "en": "Which Constitutional Amendment Act of 1956 enabled the appointment of the same person as Governor for two or more States?",
            "ta": "ஒரே நபரை இரண்டு அல்லது அதற்கு மேற்பட்ட மாநிலங்களின் ஆளுநராக நியமிக்க வழிவகை செய்த 1956 ஆம் ஆண்டின் அரசியலமைப்புத் திருத்தச் சட்டம் எது?"
        },
        "options": [
            {"id": "A", "en": "7th Constitutional Amendment Act", "ta": "7வது அரசியலமைப்புத் திருத்தச் சட்டம்"},
            {"id": "B", "en": "42nd Constitutional Amendment Act", "ta": "42வது அரசியலமைப்புத் திருத்தச் சட்டம்"},
            {"id": "C", "en": "44th Constitutional Amendment Act", "ta": "44வது அரசியலமைப்புத் திருத்தச் சட்டம்"},
            {"id": "D", "en": "24th Constitutional Amendment Act", "ta": "24வது அரசியலமைப்புத் திருத்தச் சட்டம்"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "The 7th Constitutional Amendment Act of 1956 added a proviso to Article 153 allowing the appointment of one person as Governor for two or more States.",
            "ta": "1956 ஆம் ஆண்டின் 7வது அரசியலமைப்புத் திருத்தச் சட்டம் உறுப்பு 153 இல் ஒரு நிபந்தனைச் சேர்க்கையைச் சேர்த்து, ஒரே நபரை இரண்டு அல்லது அதற்கு மேற்பட்ட மாநிலங்களுக்கு ஆளுநராக நியமிக்க அனுமதித்தது."
        },
        "why_not_others": {
            "A": {"en": "Correct. The 7th Amendment of 1956 enabled dual governorship under Article 153.", "ta": "சரி. 1956 இன் 7வது திருத்தம் உறுப்பு 153 இன் கீழ் இரட்டை ஆளுநர் பொறுப்பை அனுமதித்தது."},
            "B": {"en": "Incorrect. The 42nd Amendment of 1976 modified Cabinet advice bindingness on President, not dual governorship.", "ta": "தவறு. 1976 இன் 42வது திருத்தம் குடியரசுத் தலைவருக்கு அமைச்சரவை ஆலோசனையைக் கட்டாயமாக்கியது."},
            "C": {"en": "Incorrect. The 44th Amendment of 1978 restored constitutional safeguards post-Emergency.", "ta": "தவறு. 1978 இன் 44வது திருத்தம் அவசரநிலைக்குப் பிந்தைய உரிமைகளை மீட்டெடுத்தது."},
            "D": {"en": "Incorrect. The 24th Amendment of 1971 relates to constitutional amendment procedures under Article 368.", "ta": "தவறு. 1971 இன் 24வது திருத்தம் உறுப்பு 368 இன் கீழ் அரசியலமைப்புத் திருத்த நடைமுறைகளைப் பற்றியது."}
        },
        "tnpsc_tip": {
            "en": "Remember: The 7th Constitutional Amendment (1956) also reorganized states on linguistic lines.",
            "ta": "நினைவில் கொள்க: 7வது அரசியலமைப்புத் திருத்தம் (1956) மாநிலங்களை மொழிவாரியாக சீரமைக்கவும் உதவியது."
        },
        "revision_fact": {
            "en": "Article 153 requires a Governor for each State, but the 7th Amendment permits one Governor for multiple States.",
            "ta": "உறுப்பு 153 ஒவ்வொரு மாநிலத்திற்கும் ஒரு ஆளுநர் இருக்க வேண்டும் என்கிறது; 7வது திருத்தம் பல மாநிலங்களுக்கு ஒரே ஆளுநரை அனுமதிக்கிறது."
        },
        "source_reference": ["M. Laxmikanth – Indian Polity"],
        "bloom_level": "Remember",
        "estimated_time_sec": 45,
        "pyq_similarity": "Standard",
        "tags": ["Governor", "Article 153", "7th Amendment"]
    })

    q.append({
        "id": "GOV_E_002",
        "subject": "Polity",
        "topic": "Governor of a State",
        "difficulty": "Easy",
        "question_type": "Direct",
        "question": {
            "en": "Under Article 154 of the Indian Constitution, the executive power of the State is vested in which constitutional authority?",
            "ta": "இந்திய அரசியலமைப்பின் உறுப்பு 154-ன் படி, மாநிலத்தின் நிர்வாக அதிகாரம் எந்த அரசியலமைப்பு அதிகாரியிடம் ஒப்படைக்கப்பட்டுள்ளது?"
        },
        "options": [
            {"id": "A", "en": "Chief Minister of the State", "ta": "மாநில முதலமைச்சர்"},
            {"id": "B", "en": "Governor of the State", "ta": "மாநில ஆளுநர்"},
            {"id": "C", "en": "Speaker of the Legislative Assembly", "ta": "சட்டமன்றப் பேரவைத் தலைவர்"},
            {"id": "D", "en": "Chief Justice of the High Court", "ta": "உயர்நீதிமன்றத் தலைமை நீதிபதி"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "Article 154(1) lays down that the executive power of the State shall be vested in the Governor and exercised by him either directly or through officers subordinate to him.",
            "ta": "உறுப்பு 154(1) மாநிலத்தின் நிர்வாக அதிகாரம் ஆளுநரிடம் ஒப்படைக்கப்பட்டு, அவரால் நேரடியாகவோ அல்லது தமக்குக் கீழ் உள்ள அலுவலர்கள் மூலமாகவோ செயல்படுத்தப்படும் எனக் கூறுகிறது."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. The Chief Minister is the real executive head (de facto), but constitutional executive power resides in the Governor (de jure).", "ta": "தவறு. முதலமைச்சர் உண்மையான நிர்வாகத் தலைவர், ஆனால் அரசியலமைப்பு நிர்வாக அதிகாரம் ஆளுநரிடமே உள்ளது."},
            "B": {"en": "Correct. Article 154 explicitly vests executive power of the state in the Governor.", "ta": "சரி. உறுப்பு 154 மாநில நிர்வாக அதிகாரத்தை ஆளுநரிடம் ஒப்படைக்கிறது."},
            "C": {"en": "Incorrect. The Speaker presides over the Assembly and holds legislative administration authority.", "ta": "தவறு. சபாநாயகர் சட்டமன்றத்தை தலைமை தாங்கி நடத்துபவர்."},
            "D": {"en": "Incorrect. The High Court Chief Justice heads the judicial branch of the state.", "ta": "தவறு. உயர்நீதிமன்ற தலைமை நீதிபதி மாநில நீதித்துறையின் தலைவராவார்."}
        },
        "tnpsc_tip": {
            "en": "De jure head = Governor (Article 154); De facto head = Chief Minister (Article 164).",
            "ta": "பெயரளவு நிர்வாகத் தலைவர் = ஆளுநர் (உறுப்பு 154); உண்மையான நிர்வாகத் தலைவர் = முதலமைச்சர் (உறுப்பு 164)."
        },
        "revision_fact": {
            "en": "Article 154 specifies that all executive action of a State Government is constitutionally vested in the Governor.",
            "ta": "உறுப்பு 154 மாநில அரசின் அனைத்து நிர்வாக நடவடிக்கைகளும் அரசியலமைப்புப்படி ஆளுநரிடம் ஒப்படைக்கப்பட்டுள்ளன என்பதைக் குறிப்பிடுகிறது."
        },
        "source_reference": ["M. Laxmikanth – Indian Polity"],
        "bloom_level": "Understand",
        "estimated_time_sec": 45,
        "pyq_similarity": "Standard",
        "tags": ["Governor", "Article 154", "Executive Power"]
    })

    q.append({
        "id": "GOV_E_003",
        "subject": "Polity",
        "topic": "Governor of a State",
        "difficulty": "Easy",
        "question_type": "Direct",
        "question": {
            "en": "Which constitutional authority appoints the Governor of a State under Article 155?",
            "ta": "உறுப்பு 155-ன் படி மாநில ஆளுநரை நியமிக்கும் அரசியலமைப்பு அதிகாரம் எது?"
        },
        "options": [
            {"id": "A", "en": "Chief Justice of India", "ta": "இந்தியத் தலைமை நீதிபதி"},
            {"id": "B", "en": "Chief Minister of the State", "ta": "மாநில முதலமைச்சர்"},
            {"id": "C", "en": "President of India", "ta": "இந்தியக் குடியரசுத் தலைவர்"},
            {"id": "D", "en": "Prime Minister of India", "ta": "இந்தியப் பிரதமர்"}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "Article 155 provides that the Governor of a State shall be appointed by the President by warrant under his hand and seal.",
            "ta": "உறுப்பு 155 மாநில ஆளுநர் குடியரசுத் தலைவரால் அவரது கையொப்பம் மற்றும் முத்திரையுடன் கூடிய சாசனம் மூலம் நியமிக்கப்படுவார் எனக் கூறுகிறது."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. The Chief Justice of India administers the oath to the President, not appoints the Governor.", "ta": "தவறு. இந்திய தலைமை நீதிபதி குடியரசுத் தலைவருக்குப் பதவிப்பிரமாணம் செய்து வைப்பவர்."},
            "B": {"en": "Incorrect. The Chief Minister has no constitutional role in appointing the Governor.", "ta": "தவறு. ஆளுநரை நியமிப்பதில் முதலமைச்சருக்கு அரசியலமைப்புப் பங்கு எதுவுமில்லை."},
            "C": {"en": "Correct. Article 155 mandates appointment by the President of India.", "ta": "சரி. உறுப்பு 155 குடியரசுத் தலைவரால் நியமிக்கப்படுவதை ஆணையிடுகிறது."},
            "D": {"en": "Incorrect. The Prime Minister heads the Cabinet advising the President, but appointment is made by the President.", "ta": "தவறு. பிரதமர் அமைச்சரவையின் தலைவராக ஆலோசனையளிக்கிறார், ஆனால் நியமனம் குடியரசுத் தலைவரால் செய்யப்படுகிறது."}
        },
        "tnpsc_tip": {
            "en": "Warrant under his hand and seal = Formal executive instrument used by the President for appointing constitutional dignitaries like Governor, SC Judges, CAG.",
            "ta": "கையொப்பம் மற்றும் முத்திரையுடன் கூடிய சாசனம் = ஆளுநர், உச்சநீதிமன்ற நீதிபதிகள், சி.ஏ.ஜி போன்ற உயரிய பதவி நியமனங்களுக்குக் குடியரசுத் தலைவரால் பயன்படுத்தப்படும் சாசனம்."
        },
        "revision_fact": {
            "en": "Governor is an appointee of the President and holds office during the pleasure of the President (Article 156).",
            "ta": "ஆளுநர் குடியரசுத் தலைவரால் நியமிக்கப்படுபவர் ஆவார், மேலும் குடியரசுத் தலைவரின் விருப்பம் உள்ளவரை பதவியில் நீடிப்பார் (உறுப்பு 156)."
        },
        "source_reference": ["M. Laxmikanth – Indian Polity"],
        "bloom_level": "Remember",
        "estimated_time_sec": 45,
        "pyq_similarity": "Standard",
        "tags": ["Governor", "Article 155", "Appointment"]
    })

    q.append({
        "id": "GOV_E_004",
        "subject": "Polity",
        "topic": "Governor of a State",
        "difficulty": "Easy",
        "question_type": "Direct",
        "question": {
            "en": "What is the normal term of office for a Governor under Article 156 of the Indian Constitution?",
            "ta": "இந்திய அரசியலமைப்பின் உறுப்பு 156-ன் கீழ் ஆளுநரின் சாதாரண பதவிக் காலம் என்ன?"
        },
        "options": [
            {"id": "A", "en": "4 years", "ta": "4 ஆண்டுகள்"},
            {"id": "B", "en": "5 years", "ta": "5 ஆண்டுகள்"},
            {"id": "C", "en": "6 years", "ta": "6 ஆண்டுகள்"},
            {"id": "D", "en": "Life tenure", "ta": "ஆயுட்காலம்"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "Article 156(3) states that subject to the pleasure of the President, a Governor holds office for a term of 5 years from the date on which he enters upon his office.",
            "ta": "உறுப்பு 156(3) குடியரசுத் தலைவரின் விருப்பத்திற்கு உட்பட்டு, ஆளுநர் தாம் பதவியேற்ற நாளிலிருந்து 5 ஆண்டுகள் பதவிக் காலம் வகிப்பார் எனக் கூறுகிறது."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. 4 years is the US Presidential term, not the Governor's term in India.", "ta": "தவறு. 4 ஆண்டுகள் என்பது அமெரிக்க அதிபரின் பதவிக்காலம், இந்திய ஆளுநரின் பதவிக்காலம் அன்று."},
            "B": {"en": "Correct. 5 years is the normal constitutional term under Article 156(3).", "ta": "சரி. உறுப்பு 156(3) இன் படி 5 ஆண்டுகள் சாதாரண அரசியலமைப்பு பதவிக்காலமாகும்."},
            "C": {"en": "Incorrect. 6 years is the term of Rajya Sabha and State Legislative Council members.", "ta": "தவறு. 6 ஆண்டுகள் என்பது மாநிலங்களவை மற்றும் சட்டமேலவை உறுப்பினர்களின் பதவிக்காலம்."},
            "D": {"en": "Incorrect. There is no life tenure for any constitutional office in India.", "ta": "தவறு. இந்தியாவில் எந்தவொரு அரசியலமைப்புப் பதவிக்கும் ஆயுட்காலப் பதவி கிடையாது."}
        },
        "tnpsc_tip": {
            "en": "Key Distinction: Although 5 years is specified, the Governor holds office during the 'pleasure of the President' and can be removed at any time.",
            "ta": "முக்கிய வேறுபாடு: 5 ஆண்டுகள் எனக் குறிப்பிடப்பட்டிருந்தாலும், ஆளுநர் 'குடியரசுத் தலைவரின் விருப்பம் உள்ளவரை' பதவியில் நீடிப்பார்."
        },
        "revision_fact": {
            "en": "Governor holds office for 5 years subject to Presidential pleasure and continues until his successor enters office.",
            "ta": "ஆளுநர் குடியரசுத் தலைவரின் விருப்பத்திற்கு உட்பட்டு 5 ஆண்டுகள் பதவிக் காலம் வகிப்பார் மற்றும் அவருக்குப் பின் வருபவர் பதவியேற்கும் வரை நீடிப்பார்."
        },
        "source_reference": ["M. Laxmikanth – Indian Polity"],
        "bloom_level": "Remember",
        "estimated_time_sec": 45,
        "pyq_similarity": "Standard",
        "tags": ["Governor", "Article 156", "Tenure"]
    })

    q.append({
        "id": "GOV_E_005",
        "subject": "Polity",
        "topic": "Governor of a State",
        "difficulty": "Easy",
        "question_type": "Direct",
        "question": {
            "en": "What is the minimum age qualification required for appointment as a Governor under Article 157?",
            "ta": "உறுப்பு 157-ன் படி ஆளுநராக நியமிக்கப்படுவதற்குத் தேவையான குறைந்தபட்ச வயதுத் தகுதி என்ன?"
        },
        "options": [
            {"id": "A", "en": "25 years", "ta": "25 ஆண்டுகள்"},
            {"id": "B", "en": "30 years", "ta": "30 ஆண்டுகள்"},
            {"id": "C", "en": "35 years", "ta": "35 ஆண்டுகள்"},
            {"id": "D", "en": "40 years", "ta": "40 ஆண்டுகள்"}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "Article 157 specifies two qualifications for Governor: (1) He must be a citizen of India, and (2) He must have completed the age of 35 years.",
            "ta": "உறுப்பு 157 ஆளுநருக்கான இரண்டு தகுதிகளைக் குறிப்பிடுகிறது: (1) அவர் இந்தியக் குடிமகனாக இருக்க வேண்டும், (2) 35 வயதைப் பூர்த்தி செய்திருக்க வேண்டும்."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. 25 years is the minimum age for Lok Sabha and Legislative Assembly membership.", "ta": "தவறு. 25 வயது என்பது மக்களவை மற்றும் சட்டப்பேரவை உறுப்பினருக்கான குறைந்தபட்ச வயது."},
            "B": {"en": "Incorrect. 30 years is the minimum age for Rajya Sabha and Legislative Council membership.", "ta": "தவறு. 30 வயது என்பது மாநிலங்களவை மற்றும் சட்டமேலவை உறுப்பினருக்கான குறைந்தபட்ச வயது."},
            "C": {"en": "Correct. 35 years is the constitutionally prescribed minimum age for Governor (and President/Vice-President).", "ta": "சரி. 35 வயது என்பது ஆளுநருக்கு (மற்றும் குடியரசுத் தலைவர்/துணைத் தலைவருக்கு) அரசியலமைப்பால் நிர்ணயிக்கப்பட்ட குறைந்தபட்ச வயது."},
            "D": {"en": "Incorrect. 40 years is not a prescribed minimum age for any constitutional office in India.", "ta": "தவறு. 40 வயது எந்தவொரு அரசியலமைப்புப் பதவிக்கும் நிர்ணயிக்கப்பட்ட குறைந்தபட்ச வயது அன்று."}
        },
        "tnpsc_tip": {
            "en": "Age Qualifications Cheat Sheet: 25 yrs = Lok Sabha/MLA; 30 yrs = Rajya Sabha/MLC; 35 yrs = President, Vice-President, Governor.",
            "ta": "வயது தகுதிகள்: 25 வயது = மக்களவை/எம்.எல்.ஏ; 30 வயது = மாநிலங்களவை/எம்.எல்.சி; 35 வயது = குடியரசுத் தலைவர், துணைத் தலைவர், ஆளுநர்."
        },
        "revision_fact": {
            "en": "Article 157 lays down only two qualification criteria: Indian citizenship and completion of 35 years of age.",
            "ta": "உறுப்பு 157 இரண்டு தகுதிகளை மட்டுமே விதிக்கிறது: இந்தியக் குடியுரிமை மற்றும் 35 வயது பூர்த்தி அடைந்திருத்தல்."
        },
        "source_reference": ["M. Laxmikanth – Indian Polity"],
        "bloom_level": "Remember",
        "estimated_time_sec": 45,
        "pyq_similarity": "Standard",
        "tags": ["Governor", "Article 157", "Qualifications"]
    })

    q.append({
        "id": "GOV_E_006",
        "subject": "Polity",
        "topic": "Governor of a State",
        "difficulty": "Easy",
        "question_type": "Direct",
        "question": {
            "en": "Who administers the oath of office to a newly appointed Governor under Article 159?",
            "ta": "உறுப்பு 159-ன் கீழ் புதிதாக நியமிக்கப்பட்ட ஆளுநருக்குப் பதவிப் பிரமாணம் செய்து வைப்பவர் யார்?"
        },
        "options": [
            {"id": "A", "en": "President of India", "ta": "இந்தியக் குடியரசுத் தலைவர்"},
            {"id": "B", "en": "Chief Justice of the concerned High Court", "ta": "சம்பந்தப்பட்ட உயர்நீதிமன்றத் தலைமை நீதிபதி"},
            {"id": "C", "en": "Chief Minister of the State", "ta": "மாநில முதலமைச்சர்"},
            {"id": "D", "en": "Speaker of the Legislative Assembly", "ta": "சட்டமன்றப் பேரவைத் தலைவர்"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "Article 159 provides that every Governor shall, before entering upon his office, make and subscribe an oath or affirmation in the presence of the Chief Justice of the High Court exercising jurisdiction in relation to the State (or senior-most Judge available).",
            "ta": "உறுப்பு 159 ஒவ்வொரு ஆளுநரும் பதவியேற்பதற்கு முன், அந்த மாநில உயர்நீதிமன்றத் தலைமை நீதிபதி (அல்லது மூத்த நீதிபதி) முன்னிலையில் பதவிப் பிரமாணம் எடுத்துக் கொள்ள வேண்டும் என வழங்குகிறது."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. The President appoints the Governor, but does not administer the oath.", "ta": "தவறு. குடியரசுத் தலைவர் ஆளுநரை நியமிக்கிறார், ஆனால் பதவிப் பிரமாணம் செய்து வைப்பதில்லை."},
            "B": {"en": "Correct. Article 159 specifies the High Court Chief Justice (or senior-most judge) as oath-administering authority.", "ta": "சரி. உறுப்பு 159 உயர்நீதிமன்றத் தலைமை நீதிபதியை பதவிப் பிரமாணம் செய்து வைக்கும் அதிகாரியாகக் குறிப்பிடுகிறது."},
            "C": {"en": "Incorrect. The Chief Minister takes oath before the Governor, not vice versa.", "ta": "தவறு. முதலமைச்சரே ஆளுநர் முன் பதவிப் பிரமாணம் எடுக்கிறார்."},
            "D": {"en": "Incorrect. Speaker presides over Legislative Assembly and plays no role in Governor's oath.", "ta": "தவறு. சபாநாயகர் சட்டமன்றப் பேரவையை நடத்துபவர், ஆளுநர் பிரமாணத்தில் தொடர்பில்லை."}
        },
        "tnpsc_tip": {
            "en": "Trap Alert: President appoints Governor (Article 155), but High Court Chief Justice administers the oath (Article 159).",
            "ta": "எச்சரிக்கை: குடியரசுத் தலைவர் ஆளுநரை நியமிக்கிறார் (உறுப்பு 155), ஆனால் உயர்நீதிமன்றத் தலைமை நீதிபதி பதவிப் பிரமாணம் செய்து வைக்கிறார் (உறுப்பு 159)."
        },
        "revision_fact": {
            "en": "Article 159 specifies that the Governor's oath is administered by the Chief Justice of the High Court or the senior-most judge available.",
            "ta": "உறுப்பு 159 ஆளுநரின் பதவிப் பிரமாணம் உயர்நீதிமன்றத் தலைமை நீதிபதியால் அல்லது உள்ள மூத்த நீதிபதியால் செய்து வைக்கப்படும் எனக் குறிப்பிடுகிறது."
        },
        "source_reference": ["M. Laxmikanth – Indian Polity"],
        "bloom_level": "Remember",
        "estimated_time_sec": 45,
        "pyq_similarity": "Standard",
        "tags": ["Governor", "Article 159", "Oath"]
    })

    q.append({
        "id": "GOV_E_007",
        "subject": "Polity",
        "topic": "Governor of a State",
        "difficulty": "Easy",
        "question_type": "Direct",
        "question": {
            "en": "To whom does the Governor submit his written resignation under Article 156(2)?",
            "ta": "உறுப்பு 156(2)-ன் கீழ் ஆளுநர் தனது எழுத்துப்பூர்வமான ராஜினாமாக் கடிதத்தை யாரிடம் சமர்ப்பிக்கிறார்?"
        },
        "options": [
            {"id": "A", "en": "Chief Minister of the State", "ta": "மாநில முதலமைச்சர்"},
            {"id": "B", "en": "Chief Justice of the High Court", "ta": "உயர்நீதிமன்றத் தலைமை நீதிபதி"},
            {"id": "C", "en": "President of India", "ta": "இந்தியக் குடியரசுத் தலைவர்"},
            {"id": "D", "en": "Speaker of the Legislative Assembly", "ta": "சட்டமன்றப் பேரவைத் தலைவர்"}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "Article 156(2) provides that the Governor may, by writing under his hand addressed to the President, resign his office.",
            "ta": "உறுப்பு 156(2) ஆளுநர் தமது கையொப்பமிட்ட எழுத்துப்பூர்வக் கடிதத்தைக் குடியரசுத் தலைவருக்கு முகவரியிட்டுத் தமது பதவியை ராஜினாமா செய்யலாம் என வழங்குகிறது."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. The Chief Minister is subordinate in executive protocol and does not receive Governor's resignation.", "ta": "தவறு. முதலமைச்சர் நிர்வாக நெறிமுறையில் ஆளுநருக்கு ராஜினாமாக் கடிதம் வழங்கும் நபரல்ல."},
            "B": {"en": "Incorrect. High Court Chief Justice administers the oath, but resignation is sent to President.", "ta": "தவறு. உயர்நீதிமன்ற தலைமை நீதிபதி பதவிப் பிரமாணம் செய்து வைக்கிறார், ஆனால் ராஜினாமா குடியரசுத் தலைவரிடமே வழங்கப்படுகிறது."},
            "C": {"en": "Correct. Article 156(2) explicitly mandates resignation addressed to the President.", "ta": "சரி. உறுப்பு 156(2) குடியரசுத் தலைவரிடம் ராஜினாமா கடிதம் அளிப்பதை தெளிவாக விதிக்கிறது."},
            "D": {"en": "Incorrect. Speaker receives resignation of Assembly members, not the Governor.", "ta": "தவறு. சபாநாயகர் சட்டமன்ற உறுப்பினர்களின் ராஜினாமாவைப் பெறுபவர்."}
        },
        "tnpsc_tip": {
            "en": "Appointing authority = Resignation receiving authority. Since President appoints Governor (Art 155), resignation goes to President (Art 156(2)).",
            "ta": "நியமன அதிகாரி = ராஜினாமா பெறும் அதிகாரி. குடியரசுத் தலைவர் ஆளுநரை நியமிப்பதால் (உறுப்பு 155), ராஜினாமா குடியரசுத் தலைவருக்கே செல்ல வேண்டும் (உறுப்பு 156(2))."
        },
        "revision_fact": {
            "en": "Article 156(2) mandates that Governor's resignation must be in writing and addressed to the President.",
            "ta": "உறுப்பு 156(2) ஆளுநரின் ராஜினாமா எழுத்துப்பூர்வமாக குடியரசுத் தலைவருக்கு முகவரியிடப்பட வேண்டும் என விதிக்கிறது."
        },
        "source_reference": ["M. Laxmikanth – Indian Polity"],
        "bloom_level": "Remember",
        "estimated_time_sec": 45,
        "pyq_similarity": "Standard",
        "tags": ["Governor", "Article 156", "Resignation"]
    })

    q.append({
        "id": "GOV_E_008",
        "subject": "Polity",
        "topic": "Governor of a State",
        "difficulty": "Easy",
        "question_type": "Direct",
        "question": {
            "en": "Which Article of the Indian Constitution empowers the Governor to grant pardons, reprieves, respites or remissions of punishment?",
            "ta": "மன்னிப்பு அளிக்கவும், தண்டனையைக் குறைக்கவும், தற்காலிகமாக நிறுத்தவும் ஆளுநருக்கு அதிகாரமளிக்கும் இந்திய அரசியலமைப்பின் உறுப்பு எது?"
        },
        "options": [
            {"id": "A", "en": "Article 72", "ta": "உறுப்பு 72"},
            {"id": "B", "en": "Article 161", "ta": "உறுப்பு 161"},
            {"id": "C", "en": "Article 123", "ta": "உறுப்பு 123"},
            {"id": "D", "en": "Article 213", "ta": "உறுப்பு 213"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "Article 161 deals with the pardoning power of the Governor for offenses against any law relating to a matter to which the executive power of the State extends.",
            "ta": "உறுப்பு 161 மாநிலத்தின் நிர்வாக அதிகாரம் நீட்டிக்கப்படும் விஷயங்கள் தொடர்பான சட்டங்களுக்கு எதிரான குற்றங்களுக்கான ஆளுநரின் மன்னிப்பு அதிகாரத்தைப் பற்றியது."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Article 72 empowers the President of India to grant pardons.", "ta": "தவறு. உறுப்பு 72 குடியரசுத் தலைவரின் மன்னிப்பு அதிகாரத்தைப் பற்றியது."},
            "B": {"en": "Correct. Article 161 governs the Governor's pardoning power.", "ta": "சரி. உறுப்பு 161 ஆளுநரின் மன்னிப்பு அதிகாரத்தை நிர்வகிக்கிறது."},
            "C": {"en": "Incorrect. Article 123 relates to Ordinance-making power of the President.", "ta": "தவறு. உறுப்பு 123 குடியரசுத் தலைவரின் அவசரச் சட்ட அதிகாரத்தைப் பற்றியது."},
            "D": {"en": "Incorrect. Article 213 relates to Ordinance-making power of the Governor.", "ta": "தவறு. உறுப்பு 213 ஆளுநரின் அவசரச் சட்ட அதிகாரத்தைப் பற்றியது."}
        },
        "tnpsc_tip": {
            "en": "Pardoning Power Pair: President = Article 72; Governor = Article 161.",
            "ta": "மன்னிப்பு அதிகார இணை: குடியரசுத் தலைவர் = உறுப்பு 72; ஆளுநர் = உறுப்பு 161."
        },
        "revision_fact": {
            "en": "Article 161 grants judicial mercy powers to the Governor over matters within state executive jurisdiction.",
            "ta": "உறுப்பு 161 மாநில நிர்வாக எல்லைக்குட்பட்ட விஷயங்களில் ஆளுநருக்குக் கருணை அதிகாரங்களை வழங்குகிறது."
        },
        "source_reference": ["M. Laxmikanth – Indian Polity"],
        "bloom_level": "Remember",
        "estimated_time_sec": 45,
        "pyq_similarity": "Standard",
        "tags": ["Governor", "Article 161", "Pardoning Power"]
    })

    q.append({
        "id": "GOV_E_009",
        "subject": "Polity",
        "topic": "Governor of a State",
        "difficulty": "Easy",
        "question_type": "Direct",
        "question": {
            "en": "Which Article of the Indian Constitution empowers the Governor to promulgate Ordinances during the recess of the State Legislature?",
            "ta": "மாநில சட்டமன்றக் கூட்டத்தொடர் இல்லாத போது அவசரச் சட்டங்களை பிறப்பிக்க ஆளுநருக்கு அதிகாரமளிக்கும் இந்திய அரசியலமைப்பின் உறுப்பு எது?"
        },
        "options": [
            {"id": "A", "en": "Article 213", "ta": "உறுப்பு 213"},
            {"id": "B", "en": "Article 123", "ta": "உறுப்பு 123"},
            {"id": "C", "en": "Article 200", "ta": "உறுப்பு 200"},
            {"id": "D", "en": "Article 356", "ta": "உறுப்பு 356"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Article 213 empowers the Governor to promulgate Ordinances when the State Legislature (or either House in bicameral legislature) is not in session.",
            "ta": "உறுப்பு 213 மாநில சட்டமன்றம் (அல்லது இரு அவைகளில் ஒன்று) கூட்டத்தொடரில் இல்லாத போது அவசரச் சட்டங்களை பிறப்பிக்க ஆளுநருக்கு அதிகாரமளிக்கிறது."
        },
        "why_not_others": {
            "A": {"en": "Correct. Article 213 specifies the Governor's Ordinance-making power.", "ta": "சரி. உறுப்பு 213 ஆளுநரின் அவசரச் சட்ட அதிகாரத்தைக் குறிப்பிடுகிறது."},
            "B": {"en": "Incorrect. Article 123 empowers the President to promulgate Ordinances during recess of Parliament.", "ta": "தவறு. உறுப்பு 123 நாடாளுமன்றக் கூட்டத்தொடர் இல்லாத போது குடியரசுத் தலைவரின் அவசரச் சட்ட அதிகாரத்தைப் பற்றியது."},
            "C": {"en": "Incorrect. Article 200 deals with Governor's assent to Bills passed by State Legislature.", "ta": "தவறு. உறுப்பு 200 சட்டமன்றத்தால் நிறைவேற்றப்பட்ட மசோதாக்களுக்கு ஆளுநர் ஒப்புதல் அளிப்பதைப் பற்றியது."},
            "D": {"en": "Incorrect. Article 356 deals with President's Rule in a State.", "ta": "தவறு. உறுப்பு 356 மாநிலத்தில் குடியரசுத் தலைவர் ஆட்சியைப் பற்றியது."}
        },
        "tnpsc_tip": {
            "en": "Ordinance Power Pair: President = Article 123; Governor = Article 213 (Notice digits 1-2-3 vs 2-1-3!).",
            "ta": "அவசரச் சட்ட இணை: குடியரசுத் தலைவர் = உறுப்பு 123; ஆளுநர் = உறுப்பு 213 (எண்களைக் கவனியுங்கள் 1-2-3 மற்றும் 2-1-3!)."
        },
        "revision_fact": {
            "en": "Article 213 grants legislative power to the Governor to enact temporary laws via Ordinances when legislature is in recess.",
            "ta": "உறுப்பு 213 சட்டமன்றக் கூட்டத்தொடர் இல்லாத போது அவசரச் சட்டங்கள் மூலம் தற்காலிகச் சட்டங்களை இயற்ற ஆளுநருக்கு சட்டமியற்றும் அதிகாரத்தை அளிக்கிறது."
        },
        "source_reference": ["M. Laxmikanth – Indian Polity"],
        "bloom_level": "Remember",
        "estimated_time_sec": 45,
        "pyq_similarity": "Standard",
        "tags": ["Governor", "Article 213", "Ordinance"]
    })

    q.append({
        "id": "GOV_E_010",
        "subject": "Polity",
        "topic": "Governor of a State",
        "difficulty": "Easy",
        "question_type": "Direct",
        "question": {
            "en": "Who appoints the Advocate General for the State under Article 165 of the Indian Constitution?",
            "ta": "இந்திய அரசியலமைப்பின் உறுப்பு 165-ன் கீழ் மாநிலத்தின் தலைமை வழக்கறிஞரை (Advocate General) நியமிப்பவர் யார்?"
        },
        "options": [
            {"id": "A", "en": "Chief Justice of the High Court", "ta": "உயர்நீதிமன்றத் தலைமை நீதிபதி"},
            {"id": "B", "en": "Governor of the State", "ta": "மாநில ஆளுநர்"},
            {"id": "C", "en": "Chief Minister of the State", "ta": "மாநில முதலமைச்சர்"},
            {"id": "D", "en": "President of India", "ta": "இந்தியக் குடியரசுத் தலைவர்"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "Article 165(1) mandates that the Governor of each State shall appoint a person who is qualified to be appointed a Judge of a High Court to be Advocate General for the State.",
            "ta": "உறுப்பு 165(1) உயர்நீதிமன்ற நீதிபதியாக நியமிக்கப்பட தகுதியுடைய ஒருவரை மாநிலத்தின் தலைமை வழக்கறிஞராக (Advocate General) மாநில ஆளுநர் நியமிக்க வேண்டும் என ஆணையிடுகிறது."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. High Court Chief Justice does not appoint constitutional law officers.", "ta": "தவறு. உயர்நீதிமன்ற தலைமை நீதிபதி அரசியலமைப்பு சட்ட அதிகாரிகளை நியமிப்பதில்லை."},
            "B": {"en": "Correct. Article 165 explicitly vests the appointment of Advocate General in the Governor.", "ta": "சரி. உறுப்பு 165 தலைமை வழக்கறிஞர் நியமனத்தை ஆளுநரிடம் தெளிவாக ஒப்படைக்கிறது."},
            "C": {"en": "Incorrect. CM leads the Cabinet that advises the Governor, but the formal appointing authority is the Governor.", "ta": "தவறு. முதலமைச்சர் ஆலோசனையளிக்கும் அமைச்சரவைக்கு தலைமை தாங்குகிறார், ஆனால் நியமன அதிகாரி ஆளுநராவார்."},
            "D": {"en": "Incorrect. The President appoints Attorney General for India (Article 76), while Governor appoints Advocate General for State (Article 165).", "ta": "தவறு. குடியரசுத் தலைவர் மத்திய அரசுக்கான அட்டர்னி ஜெனரலை நியமிக்கிறார் (உறுப்பு 76), ஆளுநர் மாநிலத்துக்கான அட்வகேட் ஜெனரலை நியமிக்கிறார்."}
        },
        "tnpsc_tip": {
            "en": "Law Officer Pair: Union Attorney General (Art 76) appointed by President; State Advocate General (Art 165) appointed by Governor.",
            "ta": "சட்ட அதிகாரி இணை: மத்திய அட்டர்னி ஜெனரல் (உறுப்பு 76) குடியரசுத் தலைவரால்; மாநில அட்வகேட் ஜெனரல் (உறுப்பு 165) ஆளுநரால்."
        },
        "revision_fact": {
            "en": "Article 165 provides for Advocate General for the State, appointed by Governor and holding office during Governor's pleasure.",
            "ta": "உறுப்பு 165 ஆளுநரால் நியமிக்கப்பட்டு ஆளுநரின் விருப்பம் உள்ளவரை பதவியில் இருக்கும் மாநில அட்வகேட் ஜெனரல் பதவியை வழங்குகிறது."
        },
        "source_reference": ["M. Laxmikanth – Indian Polity"],
        "bloom_level": "Remember",
        "estimated_time_sec": 45,
        "pyq_similarity": "Standard",
        "tags": ["Governor", "Article 165", "Advocate General"]
    })

    return q

