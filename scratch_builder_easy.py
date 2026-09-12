# build_governor_easy_final.py
import json

def get_easy_questions():
    items = []
    
    # 1
    items.append({
        "id": "GOV_E_001",
        "subject": "Polity",
        "topic": "Governor of a State",
        "difficulty": "Easy",
        "question_type": "Direct",
        "question": {
            "en": "Which Constitutional Amendment Act of 1956 facilitated the appointment of the same person as Governor for two or more States?",
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
            "en": "The 7th Constitutional Amendment Act of 1956 amended Article 153 to permit the appointment of the same person as Governor for two or more States.",
            "ta": "1956 ஆம் ஆண்டின் 7வது அரசியலமைப்புத் திருத்தச் சட்டம் உறுப்பு 153-ஐ திருத்தி, ஒரே நபரை இரண்டு அல்லது அதற்கு மேற்பட்ட மாநிலங்களுக்கு ஆளுநராக நியமிக்க வழிவகை செய்தது."
        },
        "why_not_others": {
            "A": {"en": "Correct. The 7th Amendment Act of 1956 made this key provision in Article 153.", "ta": "சரி. 1956 இன் 7வது சட்டத்திருத்தம் உறுப்பு 153 இல் இந்த முக்கிய மாற்றத்தைக் கொண்டுவந்தது."},
            "B": {"en": "Incorrect. The 42nd Amendment (1976) introduced major constitutional changes like Mini-Constitution but not dual governorship.", "ta": "தவறு. 42வது திருத்தம் (1976) சிறு அரசியலமைப்பு என அழைக்கப்படுகிறது, இது இரட்டை ஆளுநர் பற்றியது அன்று."},
            "C": {"en": "Incorrect. The 44th Amendment (1978) restored fundamental rights provisions after Emergency.", "ta": "தவறு. 44வது திருத்தம் (1978) அவசரநிலைக்குப் பிந்தைய உரிமைகளை மீட்டெடுத்தது."},
            "D": {"en": "Incorrect. The 24th Amendment (1971) affirmed Parliament's power to amend Fundamental Rights.", "ta": "தவறு. 24வது திருத்தம் (1971) அடிப்படை உரிமைகளைத் திருத்தும் நாடாளுமன்ற அதிகாரத்தைப் பற்றியது."}
        },
        "tnpsc_tip": {
            "en": "Remember: Originally, Article 153 required a separate Governor for each state. The 7th Amendment (1956) changed this requirement.",
            "ta": "நினைவில் கொள்க: தொடக்கத்தில் ஒவ்வொரு மாநிலத்திற்கும் தனி ஆளுநர் தேவைப்பட்டார். 7வது திருத்தம் (1956) இதை மாற்றியது."
        },
        "revision_fact": {
            "en": "Article 153 states there shall be a Governor for each State, with the 7th Amendment allowing dual charge.",
            "ta": "உறுப்பு 153 ஒவ்வொரு மாநிலத்திற்கும் ஒரு ஆளுநர் இருக்க வேண்டும் எனக் கூறுகிறது; 7வது திருத்தம் இரட்டைப் பொறுப்பை அனுமதிக்கிறது."
        },
        "source_reference": ["M. Laxmikanth – Indian Polity", "NCERT Class 11 Indian Constitution at Work"],
        "bloom_level": "Remember",
        "estimated_time_sec": 45,
        "pyq_similarity": "Standard",
        "tags": ["Governor", "Article 153", "7th Amendment"]
    })

    # 2
    items.append({
        "id": "GOV_E_002",
        "subject": "Polity",
        "topic": "Governor of a State",
        "difficulty": "Easy",
        "question_type": "Direct",
        "question": {
            "en": "According to Article 154 of the Indian Constitution, in whom is the executive power of the State vested?",
            "ta": "இந்திய அரசியலமைப்பின் உறுப்பு 154-ன் படி, மாநிலத்தின் நிர்வாக அதிகாரம் யாரிடம் ஒப்படைக்கப்பட்டுள்ளது?"
        },
        "options": [
            {"id": "A", "en": "Chief Minister", "ta": "முதலமைச்சர்"},
            {"id": "B", "en": "Governor", "ta": "ஆளுநர்"},
            {"id": "C", "en": "State Legislative Assembly", "ta": "மாநில சட்டமன்றப் பேரவை"},
            {"id": "D", "en": "High Court Chief Justice", "ta": "உயர்நீதிமன்ற தலைமை நீதிபதி"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "Article 154 explicitly states that the executive power of the State shall be vested in the Governor and shall be exercised by him either directly or through officers subordinate to him.",
            "ta": "உறுப்பு 154 மாநிலத்தின் நிர்வாக அதிகாரம் ஆளுநரிடம் ஒப்படைக்கப்படும் என்றும், அவர் அதை நேரடியாகவோ அல்லது தமக்குக் கீழ் உள்ள அலுவலர்கள் மூலமாகவோ செயல்படுத்துவார் என்றும் വ്യക്തமாகக் கூறுகிறது."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. The Chief Minister is the real executive head (de facto), but constitutional executive power is vested in the Governor (de jure).", "ta": "தவறு. முதலமைச்சர் உண்மையான நிர்வாகத் தலைவர் (de facto), ஆனால் அரசியலமைப்பு நிர்வாக அதிகாரம் ஆளுநரிடமே (de jure) உள்ளது."},
            "B": {"en": "Correct. Article 154 vests the executive power of the state in the Governor.", "ta": "சரி. உறுப்பு 154 மாநிலத்தின் நிர்வாக அதிகாரத்தை ஆளுநரிடம் ஒப்படைக்கிறது."},
            "C": {"en": "Incorrect. The State Legislative Assembly exercises legislative power, not executive power.", "ta": "தவறு. மாநில சட்டமன்றம் சட்டமியற்றும் அதிகாரத்தைப் பெற்றுள்ளது, நிர்வாக அதிகாரம் அன்று."},
            "D": {"en": "Incorrect. The High Court Chief Justice heads the state judiciary.", "ta": "தவறு. உயர்நீதிமன்ற தலைமை நீதிபதி மாநில நீதித்துறையின் தலைவராவார்."}
        },
        "tnpsc_tip": {
            "en": "De jure head of state executive = Governor (Article 154). De facto head of state executive = Chief Minister.",
            "ta": "மாநில நிர்வாகத்தின் பெயரளவுத் தலைவர் = ஆளுநர் (உறுப்பு 154). உண்மையானத் தலைவர் = முதலமைச்சர்."
        },
        "revision_fact": {
            "en": "Article 154 vests state executive authority in the Governor, to be exercised directly or through subordinate officers.",
            "ta": "உறுப்பு 154 மாநில நிர்வாக அதிகாரத்தை ஆளுநரிடம் வழங்கி, அதை நேரடியாகவோ அல்லது கீழதிகாரிகள் மூலமாகவோ செயல்படுத்த வகை செய்கிறது."
        },
        "source_reference": ["M. Laxmikanth – Indian Polity"],
        "bloom_level": "Understand",
        "estimated_time_sec": 45,
        "pyq_similarity": "Standard",
        "tags": ["Governor", "Article 154", "Executive Power"]
    })

    # 3
    items.append({
        "id": "GOV_E_003",
        "subject": "Polity",
        "topic": "Governor of a State",
        "difficulty": "Easy",
        "question_type": "Direct",
        "question": {
            "en": "Under Article 155 of the Indian Constitution, how is the Governor of a State appointed?",
            "ta": "இந்திய அரசியலமைப்பின் உறுப்பு 155-ன் கீழ், ஒரு மாநிலத்தின் ஆளுநர் எவ்வாறு நியமிக்கப்படுகிறார்?"
        },
        "options": [
            {"id": "A", "en": "Elected by the State Legislative Assembly", "ta": "மாநில சட்டமன்றத்தால் தேர்ந்தெடுக்கப்படுகிறார்"},
            {"id": "B", "en": "Appointed by the President by warrant under his hand and seal", "ta": "குடியரசுத் தலைவரால் அவரது கையொப்பம் மற்றும் முத்திரையுடன் கூடிய சாசனம் மூலம் நியமிக்கப்படுகிறார்"},
            {"id": "C", "en": "Appointed by the Prime Minister of India", "ta": "இந்தியப் பிரதமரால் நியமிக்கப்படுகிறார்"},
            {"id": "D", "en": "Elected directly by the people of the State", "ta": "மாநில மக்களால் நேரடியாகத் தேர்ந்தெடுக்கப்படுகிறார்"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "Article 155 provides that the Governor of a State shall be appointed by the President by warrant under his hand and seal. The Governor is neither directly nor indirectly elected.",
            "ta": "உறுப்பு 155 ஒரு மாநிலத்தின் ஆளுநர் குடியரசுத் தலைவரால் அவரது கையொப்பம் மற்றும் முத்திரையுடன் கூடிய சாசனம் மூலம் நியமிக்கப்படுவார் என வழங்குகிறது. ஆளுநர் நேரடியாகவோ மறைமுகமாகவோ தேர்ந்தெடுக்கப்படுவதில்லை."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. The State Legislative Assembly has no role in the appointment of the Governor.", "ta": "தவறு. ஆளுநர் நியமனத்தில் மாநில சட்டமன்றத்திற்கு எவ்விதப்ங்கும் இல்லை."},
            "B": {"en": "Correct. Article 155 mandates appointment by the President by warrant under his hand and seal.", "ta": "சரி. உறுப்பு 155 குடியரசுத் தலைவரால் கையொப்பம் மற்றும் முத்திரையுடன் சாசனம் மூலம் நியமனத்தை ஆணையிடுகிறது."},
            "C": {"en": "Incorrect. Constitutionally, the President appoints the Governor, though acting on the advice of the Union Cabinet headed by the PM.", "ta": "தவறு. அரசியலமைப்புப்படி குடியரசுத் தலைவரே நியமிக்கிறார் (பிரதமர் தலைமையிலான மத்திய அமைச்சரவையின் ஆலோசனையின்படி)."},
            "D": {"en": "Incorrect. Direct election model was explicitly rejected by the Constituent Assembly to prevent conflict with the CM.", "ta": "தவறு. முதலமைச்சருடன் மோதலைத் தவிர்க்க நேரடித் தேர்தல் முறையை அரசியலமைப்பு நிர்ணய சபை நிராகரித்தது."}
        },
        "tnpsc_tip": {
            "en": "India adopted the Canadian model of Governor appointment (appointment by Centre) rather than the American model (elected Governor).",
            "ta": "இந்தியா ஆளுநர் நியமனத்தில் அமெரிக்க மாதிரியை (தேர்ந்தெடுக்கப்பட்ட ஆளுநர்) தவிர்க்க கனடா மாதிரியை (மத்திய அரசால் நியமனம்) ஏற்றுக்கொண்டது."
        },
        "revision_fact": {
            "en": "Article 155 specifies that the Governor is appointed by the President of India under his hand and seal.",
            "ta": "உறுப்பு 155 ஆளுநர் இந்தியக் குடியரசுத் தலைவரால் நியமிக்கப்படுகிறார் என்பதைக் குறிப்பிடுகிறது."
        },
        "source_reference": ["M. Laxmikanth – Indian Polity"],
        "bloom_level": "Remember",
        "estimated_time_sec": 45,
        "pyq_similarity": "Standard",
        "tags": ["Governor", "Article 155", "Appointment"]
    })

    # Add 47 more Easy items up to GOV_E_050
    # Let's populate all 50 items systematically!
    return items

