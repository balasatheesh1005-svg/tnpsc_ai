# -*- coding: utf-8 -*-
"""
Complete Builder for 50 Easy MCQs for Governor Part 1 (GOV_E_001 to GOV_E_050)
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

OUT_PATH = r"data/questions/polity/governor_easy.json"

def q(qid, q_en, q_ta, opts_en, opts_ta, corr_idx, exp_en, exp_ta, wno, tip_en, tip_ta, fact_en, fact_ta, bloom="Remember", time_sec=45):
    corr_letter = ["A", "B", "C", "D"][corr_idx]
    corr_lower = ["a", "b", "c", "d"][corr_idx]
    
    return {
        "id": qid,
        "subject": "Polity",
        "topic": "Governor of a State",
        "difficulty": "Easy",
        "question_type": "Direct",
        "question": {"en": q_en, "ta": q_ta},
        "question_en": q_en,
        "question_ta": q_ta,
        "options": [
            {"id": "A", "en": opts_en[0], "ta": opts_ta[0]},
            {"id": "B", "en": opts_en[1], "ta": opts_ta[1]},
            {"id": "C", "en": opts_en[2], "ta": opts_ta[2]},
            {"id": "D", "en": opts_en[3], "ta": opts_ta[3]}
        ],
        "options_en": opts_en,
        "options_ta": opts_ta,
        "correct_answer": corr_letter,
        "answer": corr_lower,
        "explanation": {"en": exp_en, "ta": exp_ta},
        "explanation_en": exp_en,
        "explanation_ta": exp_ta,
        "why_not_others": {
            "A": {"en": wno["A"]["en"], "ta": wno["A"]["ta"]},
            "B": {"en": wno["B"]["en"], "ta": wno["B"]["ta"]},
            "C": {"en": wno["C"]["en"], "ta": wno["C"]["ta"]},
            "D": {"en": wno["D"]["en"], "ta": wno["D"]["ta"]}
        },
        "distractor_analysis": {
            k: {
                "status": "Correct" if k == corr_letter else "Incorrect",
                "explanation_english": wno[k]["en"],
                "explanation_tamil": wno[k]["ta"]
            } for k in ["A", "B", "C", "D"]
        },
        "tnpsc_tip": {"en": tip_en, "ta": tip_ta},
        "tnpsc_expert_tip": f"{tip_en} / {tip_ta}",
        "revision_fact": {"en": fact_en, "ta": fact_ta},
        "high_yield_fact": f"{fact_en} / {fact_ta}",
        "source_reference": ["M. Laxmikanth – Indian Polity", "Samacheer Kalvi Class 12 Political Science"],
        "bloom_level": bloom,
        "estimated_time_sec": time_sec,
        "pyq_similarity": "Standard",
        "tags": ["Governor", "Polity", "State Executive", "Part VI"]
    }

easy_qs = []

# Target distribution for 50 items: A=13, B=12, C=13, D=12

# 1-10
easy_qs.append(q("GOV_E_001",
    "Which Part of the Constitution of India contains provisions relating to the State Executive, including the Governor?",
    "இந்திய அரசியலமைப்பின் எந்தப் பகுதி ஆளுநர் உள்ளிட்ட மாநில நிர்வாகம் தொடர்பான விதிகளைக் கொண்டுள்ளது?",
    ["Part V", "Part VI", "Part VII", "Part IX"],
    ["பகுதி V", "பகுதி VI", "பகுதி VII", "பகுதி IX"],
    1, # B
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
    "பகுதி VI-ல் உள்ள உறுப்புகள் 153 முதல் 167 வரை இந்தியாவில் மாநில நிர்வாகத்தை நிர்வகிக்கின்றன."
))

easy_qs.append(q("GOV_E_002",
    "Which Constitutional Amendment Act made it possible to appoint the same person as Governor for two or more States?",
    "ஒரே நபரை இரண்டு அல்லது அதற்கு மேற்பட்ட மாநிலங்களின் ஆளுநராக நியமிக்க வழிவகை செய்த அரசியலமைப்புச் சட்டத்திருத்தம் எது?",
    ["7th Constitutional Amendment Act, 1956", "42nd Constitutional Amendment Act, 1976", "44th Constitutional Amendment Act, 1978", "86th Constitutional Amendment Act, 2002"],
    ["7-வது அரசியலமைப்புச் சட்டத்திருத்தம், 1956", "42-வது அரசியலமைப்புச் சட்டத்திருத்தம், 1976", "44-வது அரசியலமைப்புச் சட்டத்திருத்தம், 1978", "86-வது அரசியலமைப்புச் சட்டத்திருத்தம், 2002"],
    0, # A
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
    "உறுப்பு 153-ன் படி, ஒரே நபர் ஒரே நேரத்தில் பல மாநிலங்களின் ஆளுநராகப் பணியாற்ற முடியும்."
))

easy_qs.append(q("GOV_E_003",
    "According to Article 154(1) of the Indian Constitution, in whom is the executive power of the State vested?",
    "இந்திய அரசியலமைப்பின் உறுப்பு 154(1)-ன் படி, மாநிலத்தின் நிர்வாக அதிகாரம் யாரிடம் ஒப்படைக்கப்பட்டுள்ளது?",
    ["Chief Minister", "Speaker of Legislative Assembly", "Governor of the State", "High Court Chief Justice"],
    ["முதலமைச்சர்", "சட்டமன்ற சபாநாயகர்", "மாநில ஆளுநர்", "உயர் நீதிமன்ற தலைமை நீதிபதி"],
    2, # C
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
    "உறுப்பு 166(1)-ன் கீழ் மாநில அரசின் அனைத்து நிர்வாக நடவடிக்கைகளும் ஆளுநரின் பெயராலேயே முறைப்படி மேற்கொள்ளப்படுகின்றன."
))

easy_qs.append(q("GOV_E_004",
    "Under Article 155 of the Constitution of India, how is the Governor of a State appointed?",
    "இந்திய அரசியலமைப்பின் உறுப்பு 155-ன் கீழ், ஒரு மாநிலத்தின் ஆளுநர் எவ்வாறு நியமிக்கப்படுகிறார்?",
    ["Elected by the Legislative Assembly of the State", "Appointed by the Prime Minister", "Elected by a special Electoral College", "Appointed by the President by warrant under hand and seal"],
    ["மாநில சட்டமன்றத்தால் தேர்ந்தெடுக்கப்படுகிறார்", "பிரதமரால் நியமிக்கப்படுகிறார்", "சிறப்பு வாக்காளர் குழுவால் தேர்ந்தெடுக்கப்படுகிறார்", "குடியரசுத் தலைவரால் சாசனம் மூலம் நியமிக்கப்படுகிறார்"],
    3, # D
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
    "ஆளுநர் பதவி என்பது ஒரு சுதந்திரமான அரசியலமைப்பு பதவியாகும்; இது மத்திய அரசின் கீழ் உள்ள வேலை வாய்ப்பு அல்ல."
))

easy_qs.append(q("GOV_E_005",
    "India adopted the system of an appointed Governor based on the constitutional model of which country?",
    "நியமிக்கப்படும் ஆளுநர் முறையை இந்தியா எந்த நாட்டின் அரசியலமைப்பு மாதிரியிலிருந்து பின்பற்றியது?",
    ["Canada", "United States of America", "Australia", "Ireland"],
    ["கனடா", "அமெரிக்க ஐக்கிய நாடுகள்", "ஆஸ்திரேலியா", "அயர்லாந்து"],
    0, # A
    "India adopted the Canadian model where the Governor of a province is appointed by the Governor-General (Centre), rejecting the US model of directly elected Governors.",
    "அமெரிக்காவின் напрямуюத் தேர்ந்தெடுக்கப்படும் ஆளுநர் முறையை நிராகரித்து, மத்திய அரசால் ஆளுநர் நியமிக்கப்படும் கனடா முறையை இந்தியா ஏற்றுக்கொண்டது.",
    {
        "A": {"en": "Correct. Canadian model provided a centralized federal scheme with appointed provincial Governors.", "ta": "சரி. கனடிய மாதிரி நியமிக்கப்படும் மாநில ஆளுநர்களுடன் கூடிய கூட்டாட்சி முறையை வழங்கியது."},
        "B": {"en": "US Governors are directly elected by state voters, a model rejected in India.", "ta": "அமெரிக்க ஆளுநர்கள் நேரடியாகத் தேர்ந்தெடுக்கப்படுகிறார்கள்; இம்முறை இந்தியாவில் நிராகரிக்கப்பட்டது."},
        "C": {"en": "Australia has State Governors appointed by the British Crown on Premier advice.", "ta": "ஆஸ்திரேலியாவில் ஆளுநர்கள் பிரிட்டிஷ் கிரீடத்தால் நியமிக்கப்படுகிறார்கள்."},
        "D": {"en": "Ireland inspired Directive Principles of State Policy, not the Governor model.", "ta": "அயர்லாந்து அரசு நெறிமுறைக் கோட்பாடுகளுக்கு வழிகாட்டியாக அமைந்தது."}
    },
    "Directly elected Governors could have led to friction with the elected Chief Minister; hence Canadian model was adopted.",
    "நேரடியாகத் தேர்ந்தெடுக்கப்பட்ட ஆளுநர் முதலமைச்சருடன் மோதலை உருவாக்கக்கூடும்; எனவே கனடாவின் மாதிரி பின்பற்றப்பட்டது.",
    "The Constituent Assembly chose appointment over election to avoid political conflict between Governor and Chief Minister.",
    "அரசியலமைப்பு நிர்ணய சபை ஆளுநருக்கும் முதலமைச்சருக்கும் இடையிலான மோதலைத் தவிர்க்க நியமனத்தைத் தேர்ந்தெடுத்தது."
))

easy_qs.append(q("GOV_E_006",
    "Under Article 157 of the Constitution of India, what is the minimum age required for appointment as a Governor?",
    "இந்திய அரசியலமைப்பின் உறுப்பு 157-ன் படி, ஆளுநராக நியமிக்கப்படுவதற்குத் தேவையான குறைந்தபட்ச வயது என்ன?",
    ["25 years", "35 years", "30 years", "40 years"],
    ["25 ஆண்டுகள்", "35 ஆண்டுகள்", "30 ஆண்டுகள்", "40 ஆண்டுகள்"],
    1, # B
    "Article 157 lays down two qualifications for appointment as Governor: he must be a citizen of India and must have completed the age of 35 years.",
    "உறுப்பு 157 ஆளுநர் நியமனத்திற்கான இரு தகுதிகளை வரையறுக்கிறது: அவர் இந்தியக் குடிமகனாக இருக்க வேண்டும் மற்றும் 35 வயதைப் பூர்த்தி செய்திருக்க வேண்டும்.",
    {
        "A": {"en": "25 years is the minimum age required for Lok Sabha and State Assembly membership.", "ta": "25 வயது என்பது மக்களவை மற்றும் சட்டப்பேரவை உறுப்பினருக்கான குறைந்தபட்ச வயதாகும்."},
        "B": {"en": "Correct. Article 157 mandates minimum 35 years of age for Governor appointment.", "ta": "சரி. உறுப்பு 157 ஆளுநர் நியமனத்திற்கு குறைந்தபட்சம் 35 வயது இருக்க வேண்டும் எனக் கூறுகிறது."},
        "C": {"en": "30 years is the minimum age for Rajya Sabha and Legislative Council membership.", "ta": "30 வயது என்பது மாநிலங்களவை மற்றும் சட்ட மேலவை உறுப்பினருக்கான குறைந்தபட்ச வயதாகும்."},
        "D": {"en": "40 years is not a prescribed minimum age qualification for any constitutional executive office.", "ta": "40 வயது என்பது எந்தவொரு அரசியலமைப்பு பதவிக்கும் குறைந்தபட்ச வயதாக நிர்ணயிக்கப்படவில்லை."}
    },
    "Remember age qualifications: President/VP/Governor = 35 years; RS/MLC = 30 years; LS/MLA = 25 years.",
    "வயதுத் தகுதிகள்: குடியரசுத் தலைவர்/துணைக் குடியரசுத் தலைவர்/ஆளுநர் = 35; மாநிலங்களவை/மேலவை = 30; மக்களவை/சட்டப்பேரவை = 25.",
    "Only two qualifications are explicitly mentioned in Article 157: Indian citizenship and 35 years of age.",
    "உறுப்பு 157-ல் இரண்டு தகுதிகள் மட்டுமே கூறப்பட்டுள்ளன: இந்தியக் குடியுரிமை மற்றும் 35 வயது நிறைவு."
))

easy_qs.append(q("GOV_E_007",
    "Which of the following is an explicit qualification laid down under Article 157 for a person to be appointed as Governor?",
    "ஆளுநராக நியமிக்கப்படுவதற்கு உறுப்பு 157-ன் கீழ் தெளிவாக வரையறுக்கப்பட்டுள்ள தகுதி எது?",
    ["Must be a member of Parliament", "Must have served as a High Court Judge", "Must be a citizen of India", "Must be a resident of the State concerned"],
    ["நாடாளுமன்ற உறுப்பினராக இருக்க வேண்டும்", "உயர் நீதிமன்ற நீதிபதியாகப் பணியாற்றியிருக்க வேண்டும்", "இந்தியக் குடிமகனாக இருக்க வேண்டும்", "சம்பந்தப்பட்ட மாநிலத்தின் வசிப்பிடத்தைக் கொண்டிருக்க வேண்டும்"],
    2, # C
    "Article 157 specifies only two qualifications: 1. He must be a citizen of India; 2. He must have completed 35 years of age.",
    "உறுப்பு 157 இரண்டு தகுதிகளை மட்டுமே குறிப்பிடுகிறது: 1. அவர் இந்தியக் குடிமகனாக இருக்க வேண்டும்; 2. 35 வயதைப் பூர்த்தி செய்திருக்க வேண்டும்.",
    {
        "A": {"en": "Article 158(1) explicitly debars a Governor from being an MP or MLA.", "ta": "உறுப்பு 158(1) ஆளுநர் எம்.பி அல்லது எம்.எல்.ஏ-வாக இருப்பதைத் தடுத்து நிறுத்துகிறது."},
        "B": {"en": "High Court judge service is a qualification for Advocate General or Judge, not Governor.", "ta": "உயர் நீதிமன்ற நீதிபதி பணி என்பது வழக்கறிஞர் அல்லது நீதிபதி பதவிகளுக்கானது."},
        "C": {"en": "Correct. Indian citizenship is a mandatory constitutional qualification under Article 157.", "ta": "சரி. இந்தியக் குடியுரிமை உறுப்பு 157-ன் கீழ் கட்டாய அரசியலமைப்புத் தகுதியாகும்."},
        "D": {"en": "Being an outsider is a constitutional convention, not an Article 157 explicit requirement.", "ta": "வெளிமாநிலத்தவராக இருப்பது ஒரு அரசியலமைப்பு மரபு, உறுப்பு 157-ன் நேரடி நிபந்தனை அல்ல."}
    },
    "Distinguish between express constitutional qualifications (Art 157) and constitutional conventions (Outsider, CM consultation).",
    "தெளிவான அரசியலமைப்புத் தகுதிகள் (விதி 157) மற்றும் அரசியலமைப்பு மரபுகள் ஆகியவற்றுக்கு இடையேயான வேறுபாட்டைப் புரிந்துகொள்ளவும்.",
    "Citizenship by birth or naturalization both qualify a person for Governor office in India.",
    "பிறப்பால் அல்லது இயல்புரிமையால் குடியுரிமை பெற்ற இருவரும் இந்தியாவில் ஆளுநர் பதவிக்குத் தகுதியானவர்கள்."
))

easy_qs.append(q("GOV_E_008",
    "Under Article 158(1) of the Constitution, what happens if a Member of Parliament is appointed as Governor of a State?",
    "அரசியலமைப்பு உறுப்பு 158(1)-ன் படி, ஒரு நாடாளுமன்ற உறுப்பினர் மாநில ஆளுநராக நியமிக்கப்பட்டால் என்ன நிகழும்?",
    ["He retains his seat in Parliament for 6 months", "He must resign from Parliament within 30 days", "He can hold both offices simultaneously with President permission", "He is deemed to have vacated his seat in Parliament on the date he enters upon his office as Governor"],
    ["அவர் 6 மாதங்களுக்கு நாடாளுமன்ற இடத்தைத் தக்கவைத்துக்கொள்வார்", "அவர் 30 நாட்களுக்குள் நாடாளுமன்றப் பதவியை ராஜினாமா செய்ய வேண்டும்", "குடியரசுத் தலைவர் அனுமதியுடன் இரு பதவிகளையும் வகிக்கலாம்", "ஆளுநராகப் பதவியேற்கும் நாளில் நாடாளுமன்றத்தில் அவரது இடம் காலியானதாகக் கருதப்படும்"],
    3, # D
    "Article 158(1) states that the Governor shall not be a member of either House of Parliament or State Legislature; if appointed, he is deemed to have vacated his seat in that House on the date he enters upon his office.",
    "உறுப்பு 158(1)-ன் படி ஆளுநர் நாடாளுமன்றத்தின் அல்லது மாநில சட்டமன்றத்தின் எந்தவொரு அவையிலும் உறுப்பினராக இருக்கக்கூடாது; நியமிக்கப்பட்டால், அவர் ஆளுநராகப் பதவியேற்கும் நாளில் அந்த அவையிலுள்ள அவரது இடம் காலியானதாகக் கருதப்படும்.",
    {
        "A": {"en": "There is no 6-month retention period for legislative seats upon entering Governor office.", "ta": "ஆளுநர் பதவியேற்ற பின் சட்டமன்ற இடத்தைத் தக்கவைக்க 6 மாத அவகாசம் இல்லை."},
        "B": {"en": "No formal resignation letter is needed; vacation of seat is automatic by operation of law.", "ta": "முறையான ராஜினாமா தேவையில்லை; சட்டப்படி தானாகவே பதவி காலியாகும்."},
        "C": {"en": "Dual membership of Legislature and Governor office is strictly prohibited under Article 158.", "ta": "சட்டமன்ற உறுப்பினர் மற்றும் ஆளுநர் பதவி ஆகிய இரண்டையும் ஒரே நேரத்தில் வகிக்கத் தடையுள்ளது."},
        "D": {"en": "Correct. Deemed vacation occurs automatically on the date of entering Governor office.", "ta": "சரி. ஆளுநர் பதவியேற்கும் நாளில் நாடாளுமன்ற இடம் தானாகவே காலியாகிவிடும்."}
    },
    "Automatic vacation of legislative seat on entering office applies to both President and Governor.",
    "பதவியேற்கும் நாளில் நாடாளுமன்ற இடம் தானாக காலியாவது குடியரசுத் தலைவர் மற்றும் ஆளுநர் இருவருக்குமே பொருந்தும்.",
    "Article 158 also debars the Governor from holding any other Office of Profit.",
    "உறுப்பு 158 ஆளுநர் ஆதாயம் தரும் வேறு எந்தப் பதவியையும் வகிக்கத் தடை விதிக்கிறது."
))

easy_qs.append(q("GOV_E_009",
    "When the same person is appointed as Governor of two or more States under Article 158(3A), who determines the allocation of emoluments among the States?",
    "உறுப்பு 158(3A)-ன் கீழ் ஒரே நபர் இரண்டு அல்லது அதற்கு மேற்பட்ட மாநிலங்களின் ஆளுநராக நியமிக்கப்படும் போது, மாநிலங்களுக்கு இடையேயான ஊதியப் பங்கீட்டை தீர்மானிப்பவர் யார்?",
    ["President of India", "Parliament of India", "Chief Justices of the concerned High Courts", "Inter-State Council"],
    ["இந்தியக் குடியரசுத் தலைவர்", "இந்திய நாடாளுமன்றம்", "சம்பந்தப்பட்ட உயர் நீதிமன்றத் தலைமை நீதிபதிகள்", "மாநிலங்களுக்கு இடையேயான குழு"],
    0, # A
    "Article 158(3A) specifies that where the same person is appointed as Governor of two or more States, the emoluments and allowances payable to the Governor shall be allocated among those States in such proportion as the President may by order determine.",
    "உறுப்பு 158(3A)-ன் படி ஒரே நபர் இரண்டு அல்லது அதற்கு மேற்பட்ட மாநிலங்களுக்கு ஆளுநராக நியமிக்கப்படும் போது, அவருக்கு வழங்கப்படும் ஊதியம் மற்றும் படிகள் குடியரசுத் தலைவரின் ஆணையால் தீர்மானிக்கப்படும் விகிதத்தில் அந்த மாநிலங்களால் பகிர்ந்தளிக்கப்படும்.",
    {
        "A": {"en": "Correct. The President determines the proportion in which participating States share the Governor's salary.", "ta": "சரி. குடியரசுத் தலைவர் தனது ஆணை மூலம் ஆளுநரின் ஊதியப் பகிர்வு விகிதத்தைத் தீர்மானிக்கிறார்."},
        "B": {"en": "Parliament fixes normal Governor salary by law under Art 158(3), but President allocates for dual states under Art 158(3A).", "ta": "நாடாளுமன்றம் பொதுவான ஊதியத்தைச் சட்டத்தால் நிர்ணயிக்கிறது, ஆனால் இரட்டை மாநிலப் பகிர்வை குடியரசுத் தலைவர் தீர்மானிக்கிறார்."},
        "C": {"en": "High Court Chief Justices have no role in executive salary allocations.", "ta": "உயர் நீதிமன்றத் தலைமை நீதிபதிகளுக்கு நிர்வாக ஊதியப் பகிர்வில் பங்கில்லை."},
        "D": {"en": "Inter-State Council deals with Centre-State coordination under Art 263, not Governor salaries.", "ta": "மாநிலங்களுக்கு இடையேயான குழு மையம்-மாநில ஒருங்கிணைப்பை மேற்கொள்ளும் அமைப்பாகும்."}
    },
    "Remember: Parliament fixes Governor's salary by law (Second Schedule), but President allocates salary sharing between states for dual governorship.",
    "நினைவில் கொள்க: நாடாளுமன்றம் ஆளுநரின் ஊதியத்தை நிர்ணயிக்கிறது, ஆனால் இரட்டை ஆளுநர் ஊதியப் பங்கீட்டை குடியரசுத் தலைவர் தீர்மானிக்கிறார்.",
    "The salary of the Governor is charged on the Consolidated Fund of the concerned State(s).",
    "ஆளுநரின் ஊதியம் சம்பந்தப்பட்ட மாநிலத்தின் திரண்ட நிதியிலிருந்து (Consolidated Fund) வழங்கப்படுகிறது."
))

easy_qs.append(q("GOV_E_010",
    "Under Article 158(4) of the Constitution of India, what is the rule regarding the emoluments and allowances of a Governor during his term of office?",
    "இந்திய அரசியலமைப்பின் உறுப்பு 158(4)-ன் படி, ஆளுநரின் பதவிக்காலத்தில் அவரது ஊதியம் மற்றும் படிகள் தொடர்பான விதி என்ன?",
    ["They can be reduced during financial emergency only", "They shall not be diminished during his term of office", "They can be varied by the State Legislature at any time", "They are subject to annual review by Parliament"],
    ["நிதி அவசரநிலையின் போது மட்டுமே குறைக்கப்படலாம்", "அவரது பதவிக்காலத்தில் குறைக்கப்படக் கூடாது", "மாநில சட்டமன்றத்தால் எப்போது வேண்டுமானாலும் மாற்றப்படலாம்", "நாடாளுமன்றத்தின் ஆண்டு ஆய்வுக்கு உட்பட்டவை"],
    1, # B
    "Article 158(4) explicitly provides that the emoluments and allowances of the Governor shall not be diminished during his term of office.",
    "உறுப்பு 158(4) ஆளுநரின் ஊதியம் மற்றும் படிகள் அவரது பதவிக்காலத்தில் குறைக்கப்படக் கூடாது எனத் தெளிவாகக் கூறுகிறது.",
    {
        "A": {"en": "Unlike judges or executive staff under Art 360, Art 158(4) gives an absolute guarantee that Governor salary cannot be diminished.", "ta": "உறுப்பு 158(4) ஆளுநர் ஊதியம் அவரது பதவிக் காலத்தில் குறைக்கப்படக் கூடாது என்ற முழுமையான உத்தரவாதத்தை அளிக்கிறது."},
        "B": {"en": "Correct. Emoluments and allowances shall not be diminished during his term of office.", "ta": "சரி. பதவிக்காலத்தில் ஊதியம் மற்றும் படிகள் குறைக்கப்படக் கூடாது."},
        "C": {"en": "State Legislature has no power to fix or vary the Governor's emoluments.", "ta": "மாநில சட்டமன்றத்திற்கு ஆளுநரின் ஊதியத்தை மாற்றியமைக்கும் அதிகாரம் இல்லை."},
        "D": {"en": "Governor emoluments are charged expenditure, not subject to annual voting or review.", "ta": "ஆளுநர் ஊதியம் திரண்ட நிதியில் சுமத்தப்பட்ட செலவினமாகும்."}
    },
    "Guaranteed non-diminution of salary ensures the constitutional independence of the Governor's office.",
    "ஊதியம் குறைக்கப்படக் கூடாது என்ற உத்தரவாதம் ஆளுநர் பதவியின் சுதந்திரத்தைப் பாதுகாக்கிறது.",
    "Governor's salary and allowances are specified in the Second Schedule to the Constitution.",
    "ஆளுநரின் ஊதியம் மற்றும் படிகள் அரசியலமைப்பின் இரண்டாவது அட்டவணையில் குறிப்பிடப்பட்டுள்ளன."
))

# Save first 10 questions to ensure generation works
with open(OUT_PATH, "w", encoding="utf-8") as f:
    json.dump(easy_qs, f, ensure_ascii=False, indent=2)

print(f"Generated {len(easy_qs)} easy questions.")
