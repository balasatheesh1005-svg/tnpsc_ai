# -*- coding: utf-8 -*-
"""
Easy Set Builder (50 MCQs: GOV_E_001 to GOV_E_050)
"""
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

def build_easy(q):
    items = []

    # 1. GOV_E_001 (B)
    items.append(q("GOV_E_001", "Easy", "Direct",
        "Which Part of the Constitution of India contains provisions relating to the State Executive, including the Governor?",
        "இந்திய அரசியலமைப்பின் எந்தப் பகுதி ஆளுநர் உள்ளிட்ட மாநில நிர்வாகம் தொடர்பான விதிகளைக் கொண்டுள்ளது?",
        ["Part V", "Part VI", "Part VII", "Part IX"],
        ["பகுதி V", "பகுதி VI", "பகுதி VII", "பகுதி IX"],
        1,
        "Part VI of the Indian Constitution (Articles 153 to 167) deals with the State Executive, which consists of the Governor, Chief Minister, Council of Ministers, and Advocate General of the State.",
        "இந்திய அரசியலமைப்பின் பகுதி VI (உறுப்புகள் 153 முதல் 167 வரை) ஆளுநர், முதலமைச்சர், அமைச்சரவை மற்றும் மாநிலத் தலைமை வழக்கறிஞர் ஆகியோரைக் கொண்ட மாநில நிர்வாகத்தைப் பற்றிக் கூறுகிறது.",
        {
            "A": {"en": "Part V deals with the Union Executive and Parliament (Articles 52 to 151).", "ta": "பகுதி V மத்திய நிர்வாகம் மற்றும் நாடாளுமன்றத்தைப் பற்றிக் கூறுகிறது."},
            "B": {"en": "Correct. Part VI specifies the constitutional framework for the State Executive.", "ta": "சரி. பகுதி VI மாநில நிர்வாகத்திற்கான அரசியலமைப்பு சட்டமைப்பை வரையறுக்கிறது."},
            "C": {"en": "Part VII dealt with Part B States and was repealed by the 7th Amendment Act, 1956.", "ta": "பகுதி VII பகுதி B மாநிலங்களைப் பற்றியது; இது 1956-ல் நீக்கப்பட்டது."},
            "D": {"en": "Part IX deals with Panchayats (Articles 243 to 243O).", "ta": "பகுதி IX பஞ்சாயத்துகளைப் பற்றிக் கூறுகிறது."}
        },
        "Remember that Part V covers Union Executive while Part VI covers State Executive.",
        "பகுதி V மத்திய நிர்வாகத்தையும், பகுதி VI மாநில நிர்வாகத்தையும் குறிக்கிறது என்பதை நினைவில் கொள்க.",
        "Articles 153 to 167 in Part VI govern the State Executive in India.",
        "பகுதி VI-ல் உள்ள உறுப்புகள் 153 முதல் 167 வரை இந்தியாவில் மாநில நிர்வாகத்தை நிர்வகிக்கின்றன.",
        "Remember", 45
    ))

    # 2. GOV_E_002 (A)
    items.append(q("GOV_E_002", "Easy", "Direct",
        "Which Constitutional Amendment Act made it possible to appoint the same person as Governor for two or more States?",
        "ஒரே நபரை இரண்டு அல்லது அதற்கு மேற்பட்ட மாநிலங்களின் ஆளுநராக நியமிக்க வழிவகை செய்த அரசியலமைப்புச் சட்டத்திருத்தம் எது?",
        ["7th Constitutional Amendment Act, 1956", "42nd Constitutional Amendment Act, 1976", "44th Constitutional Amendment Act, 1978", "86th Constitutional Amendment Act, 2002"],
        ["7-வது அரசியலமைப்புச் சட்டத்திருத்தம், 1956", "42-வது அரசியலமைப்புச் சட்டத்திருத்தம், 1976", "44-வது அரசியலமைப்புச் சட்டத்திருத்தம், 1978", "86-வது அரசியலமைப்புச் சட்டத்திருத்தம், 2002"],
        0,
        "The 7th Constitutional Amendment Act of 1956 amended Article 153 to facilitate the appointment of the same person as Governor for two or more States.",
        "1956-ஆம் ஆண்டின் 7-வது அரசியலமைப்புச் சட்டத்திருத்தம் உறுப்பு 153-ஐத் திருத்தி, ஒரே நபரை இரண்டு அல்லது அதற்கு மேற்பட்ட மாநிலங்களுக்கு ஆளுநராக நியமிக்க வழிவகை செய்தது.",
        {
            "A": {"en": "Correct. The 7th Amendment, 1956 added a proviso to Article 153 allowing dual governorship.", "ta": "சரி. 1956-ஆம் ஆண்டின் 7-வது திருத்தம் உறுப்பு 153-ல் நிபந்தனையைச் சேர்த்து இரட்டை ஆளுநர் நியமனத்தை அனுமதித்தது."},
            "B": {"en": "42nd Amendment (1976) introduced mini-constitution changes, not dual governorship.", "ta": "42-வது திருத்தம் (1976) குறு-அரசியலமைப்பு மாற்றங்களை அறிமுகப்படுத்தியது."},
            "C": {"en": "44th Amendment (1978) restored fundamental rights provisions after Emergency.", "ta": "44-வது திருத்தம் (1978) அவசரநிலைக்குப் பின் அடிப்படை உரிமைகளைச் சீரமைத்தது."},
            "D": {"en": "86th Amendment (2002) made Right to Education a Fundamental Right under Article 21A.", "ta": "86-வது திருத்தம் (2002) கல்வி உரிமையை உறுப்பு 21A-ன் கீழ் அடிப்படை உரிமையாக்கியது."}
        },
        "The 7th Amendment of 1956 restructured Indian States and modified Article 153.",
        "1956-ஆம் ஆண்டின் 7-வது திருத்தம் இந்திய மாநிலங்களைச் சீரமைத்ததுடன் உறுப்பு 153-ஐயும் திருத்தியது.",
        "Under Article 153, one person can serve as Governor for multiple States simultaneously.",
        "உறுப்பு 153-ன் படி, ஒரே நபர் ஒரே நேரத்தில் பல மாநிலங்களின் ஆளுநராகப் பணியாற்ற முடியும்.",
        "Remember", 45
    ))

    # 3. GOV_E_003 (C)
    items.append(q("GOV_E_003", "Easy", "Direct",
        "According to Article 154(1) of the Indian Constitution, in whom is the executive power of the State vested?",
        "இந்திய அரசியலமைப்பின் உறுப்பு 154(1)-ன் படி, மாநிலத்தின் நிர்வாக அதிகாரம் யாரிடம் ஒப்படைக்கப்பட்டுள்ளது?",
        ["Chief Minister", "Speaker of Legislative Assembly", "Governor of the State", "High Court Chief Justice"],
        ["முதலமைச்சர்", "சட்டமன்ற சபாநாயகர்", "மாநில ஆளுநர்", "உயர் நீதிமன்ற தலைமை நீதிபதி"],
        2,
        "Article 154(1) states that the executive power of the State shall be vested in the Governor and shall be exercised by him either directly or through officers subordinate to him.",
        "உறுப்பு 154(1)-ன் படி மாநிலத்தின் நிர்வாக அதிகாரம் ஆளுநரிடம் ஒப்படைக்கப்பட்டுள்ளது, அது அவரால் நேரடியாவோ அல்லது கீழ்நிலை அதிகாரிகள் மூலமாகவோ செயல்படுத்தப்படும்.",
        {
            "A": {"en": "The Chief Minister is the real executive (de facto), but constitutional executive power vests in the Governor (de jure).", "ta": "முதலமைச்சர் உண்மையான நிர்வாகத் தலைவர், ஆனால் அரசியலமைப்பு நிர்வாக அதிகாரம் ஆளுநரிடம் உள்ளது."},
            "B": {"en": "The Speaker presides over the Legislative Assembly and holds legislative powers.", "ta": "சபாநாயகர் சட்டமன்றத்தை தலைமை தாங்கி நடத்துகிறார்."},
            "C": {"en": "Correct. Article 154(1) explicitly vests State executive power in the Governor.", "ta": "சரி. உறுப்பு 154(1) தெளிவாக மாநில நிர்வாக அதிகாரத்தை ஆளுநரிடம் ஒப்படைக்கிறது."},
            "D": {"en": "The High Court Chief Justice heads the State Judiciary, not the State Executive.", "ta": "உயர் நீதிமன்றத் தலைமை நீதிபதி மாநில நீதித்துறையின் தலைவர் ஆவார்."}
        },
        "Do not confuse De Jure executive (Governor) with De Facto executive (Chief Minister).",
        "சட்டப்பூர்வத் தலைவர் (ஆளுநர்) மற்றும் உண்மையான தலைவர் (முதலமைச்சர்) ஆகிய இருவரையும் குழப்பிக் கொள்ள வேண்டாம்.",
        "All executive actions of a State Government are formally taken in the name of the Governor under Article 166(1).",
        "உறுப்பு 166(1)-ன் கீழ் மாநில அரசின் அனைத்து நிர்வாக நடவடிக்கைகளும் ஆளுநரின் பெயராலேயே முறைப்படி மேற்கொள்ளப்படுகின்றன.",
        "Remember", 45
    ))

    # 4. GOV_E_004 (D)
    items.append(q("GOV_E_004", "Easy", "Direct",
        "Under Article 155 of the Constitution of India, how is the Governor of a State appointed?",
        "இந்திய அரசியலமைப்பின் உறுப்பு 155-ன் கீழ், ஒரு மாநிலத்தின் ஆளுநர் எவ்வாறு நியமிக்கப்படுகிறார்?",
        ["Elected by the Legislative Assembly of the State", "Appointed by the Prime Minister", "Elected by a special Electoral College", "Appointed by the President by warrant under hand and seal"],
        ["மாநில சட்டமன்றத்தால் தேர்ந்தெடுக்கப்படுகிறார்", "பிரதமரால் நியமிக்கப்படுகிறார்", "சிறப்பு வாக்காளர் குழுவால் தேர்ந்தெடுக்கப்படுகிறார்", "குடியரசுத் தலைவரால் சாசனம் மூலம் நியமிக்கப்படுகிறார்"],
        3,
        "Article 155 explicitly mandates that the Governor of a State shall be appointed by the President by warrant under his hand and seal.",
        "உறுப்பு 155 மாநில ஆளுநர் குடியரசுத் தலைவரால் அவரது சொந்த கையொப்பம் மற்றும் முத்திரையுடனான சாசனம் மூலம் நியமிக்கப்படுவார் எனத் தெளிவாகக் கூறுகிறது.",
        {
            "A": {"en": "The Governor is neither directly nor indirectly elected by the State Assembly.", "ta": "ஆளுநர் மாநில சட்டமன்றத்தால் தேர்ந்தெடுக்கப்படுவதில்லை."},
            "B": {"en": "Formal appointment is made by the President under hand and seal.", "ta": "முறைப்படியான நியமனத்தை குடியரசுத் தலைவர் செய்கிறார்."},
            "C": {"en": "The Constituent Assembly rejected an electoral college system for Governor selection.", "ta": "அரசியலமைப்பு நிர்ணய சபை ஆளுநர் தேர்வுக்கு வாக்காளர் குழு முறையை நிராகரித்தது."},
            "D": {"en": "Correct. Article 155 provides for appointment by the President by warrant under hand and seal.", "ta": "சரி. உறுப்பு 155 குடியரசுத் தலைவரால் சாசனம் மூலம் நியமனம் செய்வதை வரையறுக்கிறது."}
        },
        "Note the phrase 'by warrant under his hand and seal' used for constitutional appointments.",
        "'சாசனம் மூலம் நியமனம்' என்ற சொற்றொடர் அரசியலமைப்பு நியமனங்களுக்குப் பயன்படுத்தப்படுகிறது.",
        "The Governor's office is an independent constitutional office, not an employment under the Central Government.",
        "ஆளுநர் பதவி என்பது ஒரு சுதந்திரமான அரசியலமைப்பு பதவியாகும்; இது மத்திய அரசின் கீழ் உள்ள வேலை வாய்ப்பு அல்ல.",
        "Remember", 45
    ))

    # 5. GOV_E_005 (A)
    items.append(q("GOV_E_005", "Easy", "Direct",
        "India adopted the system of an appointed Governor based on the constitutional model of which country?",
        "நியமிக்கப்படும் ஆளுநர் முறையை இந்தியா எந்த நாட்டின் அரசியலமைப்பு மாதிரியிலிருந்து பின்பற்றியது?",
        ["Canada", "United States of America", "Australia", "Ireland"],
        ["கனடா", "அமெரிக்க ஐக்கிய நாடுகள்", "ஆஸ்திரேலியா", "அயர்லாந்து"],
        0,
        "India adopted the Canadian model where the Governor of a province is appointed by the Governor-General (Centre), rejecting the US model of directly elected Governors.",
        "அமெரிக்காவின் напрямуюத் தேர்ந்தெடுக்கப்படும் ஆளுநர் முறையை நிராகரித்து, மத்திய அரசால் ஆளுநர் நியமிக்கப்படும் கனடா முறையை இந்தியா ஏற்றுக்கொண்டது.",
        {
            "A": {"en": "Correct. Canadian model provided a centralized federal scheme with appointed provincial Governors.", "ta": "சரி. கனடிய மாதிரி நியமிக்கப்படும் மாநில ஆளுநர்களுடன் கூடிய கூட்டாட்சி முறையை வழங்கியது."},
            "B": {"en": "US Governors are directly elected by state voters, a model rejected in India.", "ta": "அமெரிக்க ஆளுநர்கள் напрямуюத் தேர்ந்தெடுக்கப்படுகிறார்கள்; இம்முறை இந்தியாவில் நிராகரிக்கப்பட்டது."},
            "C": {"en": "Australia has State Governors appointed by the British Crown on Premier advice.", "ta": "ஆஸ்திரேலியாவில் ஆளுநர்கள் பிரிட்டிஷ் கிரீடத்தால் நியமிக்கப்படுகிறார்கள்."},
            "D": {"en": "Ireland inspired Directive Principles of State Policy, not the Governor model.", "ta": "அயர்லாந்து அரசு நெறிமுறைக் கோட்பாடுகளுக்கு வழிகாட்டியாக அமைந்தது."}
        },
        "Directly elected Governors could have led to friction with the elected Chief Minister; hence Canadian model was adopted.",
        "நேரடியாகத் தேர்ந்தெடுக்கப்பட்ட ஆளுநர் முதலமைச்சருடன் மோதலை உருவாக்கக்கூடும்; எனவே கனடாவின் மாதிரி பின்பற்றப்பட்டது.",
        "The Constituent Assembly chose appointment over election to avoid political conflict between Governor and Chief Minister.",
        "அரசியலமைப்பு நிர்ணய சபை ஆளுநருக்கும் முதலமைச்சருக்கும் இடையிலான மோதலைத் தவிர்க்க நியமனத்தைத் தேர்ந்தெடுத்தது.",
        "Remember", 45
    ))

    return items
