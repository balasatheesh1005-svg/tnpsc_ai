# -*- coding: utf-8 -*-
"""
Generator for Supreme Court Easy MCQs (50 Questions)
Topic: Supreme Court of India
Difficulty: Easy
File: data/questions/polity/supreme_court_easy.json
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

def make_options(en_a, ta_a, en_b, ta_b, en_c, ta_c, en_d, ta_d):
    return [
        {"id": "A", "en": en_a, "ta": ta_a},
        {"id": "B", "en": en_b, "ta": ta_b},
        {"id": "C", "en": en_c, "ta": ta_c},
        {"id": "D", "en": en_d, "ta": ta_d}
    ]

def make_why_not(correct_letter, exp_a_en, exp_a_ta, exp_b_en, exp_b_ta, exp_c_en, exp_c_ta, exp_d_en, exp_d_ta):
    return {
        "A": {"en": f"✅ {exp_a_en}" if correct_letter == "A" else f"❌ {exp_a_en}", "ta": f"✅ {exp_a_ta}" if correct_letter == "A" else f"❌ {exp_a_ta}"},
        "B": {"en": f"✅ {exp_b_en}" if correct_letter == "B" else f"❌ {exp_b_en}", "ta": f"✅ {exp_b_ta}" if correct_letter == "B" else f"❌ {exp_b_ta}"},
        "C": {"en": f"✅ {exp_c_en}" if correct_letter == "C" else f"❌ {exp_c_en}", "ta": f"✅ {exp_c_ta}" if correct_letter == "C" else f"❌ {exp_c_ta}"},
        "D": {"en": f"✅ {exp_d_en}" if correct_letter == "D" else f"❌ {exp_d_en}", "ta": f"✅ {exp_d_ta}" if correct_letter == "D" else f"❌ {exp_d_ta}"}
    }

def build_q(qid, difficulty, stem_en, stem_ta, options, correct_letter, exp_en, exp_ta, why_not, trap_en, trap_ta, tip_en, tip_ta, source_part):
    opts_en = [o["en"] for o in options]
    opts_ta = [o["ta"] for o in options]
    
    return {
        "id": qid,
        "subject": "Polity",
        "topic": "Supreme Court of India",
        "difficulty": difficulty,
        "question_type": "Direct",
        "question": {
            "en": stem_en,
            "ta": stem_ta
        },
        "question_en": stem_en,
        "question_ta": stem_ta,
        "options": options,
        "options_en": opts_en,
        "options_ta": opts_ta,
        "correct_answer": correct_letter,
        "explanation": {
            "en": exp_en,
            "ta": exp_ta
        },
        "explanation_en": exp_en,
        "explanation_ta": exp_ta,
        "why_not_others": why_not,
        "trap_point": {
            "en": trap_en,
            "ta": trap_ta
        },
        "tnpsc_tip": {
            "en": tip_en,
            "ta": tip_ta
        },
        "high_yield_fact": {
            "en": f"High-Yield Fact: {exp_en}",
            "ta": f"முக்கியக் குறிப்பு: {exp_ta}"
        },
        "source_reference": [f"Supreme Court Notes Part {source_part}"]
    }

def get_easy_questions():
    easy_data = [
        ("POLITY_SC_EASY_001", "Easy",
         "Which Part of the Indian Constitution deals with the Union Judiciary (Supreme Court)?",
         "இந்திய அரசியலமைப்பின் எந்தப் பகுதி ஒன்றிய நீதித்துறையைக் (உச்ச நீதிமன்றம்) கையாள்கிறது?",
         ("Part IV", "பகுதி IV", "Part V", "பகுதி V", "Part VI", "பகுதி VI", "Part IX", "பகுதி IX"),
         "B",
         "Part V of the Constitution (Articles 124 to 147) deals with the Union Judiciary (Supreme Court of India).",
         "அரசியலமைப்பின் பகுதி V (உறுப்புகள் 124 முதல் 147 வரை) ஒன்றிய நீதித்துறையைக் கையாள்கிறது.",
         ("Part IV deals with DPSP.", "பகுதி IV அரசு நெறிமுறைக்கோட்பாடுகளைக் கையாள்கிறது.", "Part V deals with the Union Judiciary.", "பகுதி V ஒன்றிய நீதித்துறையைக் கையாள்கிறது.", "Part VI deals with the State Executive & High Courts.", "பகுதி VI மாநில நிர்வாகம் மற்றும் உயர் நீதிமன்றங்களைக் கையாள்கிறது.", "Part IX deals with Panchayats.", "பகுதி IX பஞ்சாயத்துகளைக் கையாள்கிறது."),
         "Confusing Part V (Union Judiciary) with Part VI (State Judiciary / High Courts).", "பகுதி V மற்றும் பகுதி VI-ஐக் குழப்புவது.", "Part V Chapter IV = Supreme Court (Articles 124-147).", "பகுதி V அத்தியாயம் IV = உச்ச நீதிமன்றம் (உறுப்புகள் 124-147).", "1"),

        ("POLITY_SC_EASY_002", "Easy",
         "Which range of Articles in the Indian Constitution deals with the Supreme Court of India?",
         "இந்திய அரசியலமைப்பில் உச்ச நீதிமன்றத்தைப் பற்றிக் கூறும் உறுப்புகளின் வரம்பு எது?",
         ("Articles 124 to 147", "உறுப்புகள் 124 முதல் 147 வரை", "Articles 214 to 231", "உறுப்புகள் 214 முதல் 231 வரை", "Articles 52 to 78", "உறுப்புகள் 52 முதல் 78 வரை", "Articles 315 to 323", "உறுப்புகள் 315 முதல் 323 வரை"),
         "A",
         "Articles 124 to 147 in Part V of the Constitution deal with the organization, independence, jurisdiction, powers, and procedures of the Supreme Court.",
         "அரசியலமைப்பின் பகுதி V-ல் உள்ள உறுப்புகள் 124 முதல் 147 வரை உச்ச நீதிமன்றத்தின் அமைப்பு, சுதந்திரம், அதிகார வரம்பு மற்றும் நடைமுறைகளைக் கூறுகின்றன.",
         ("Articles 124 to 147 deal with Supreme Court.", "உறுப்புகள் 124 முதல் 147 வரை உச்ச நீதிமன்றத்தைக் குறிப்பிடுகின்றன.", "Articles 214-231 deal with High Courts.", "உறுப்புகள் 214-231 உயர் நீதிமன்றங்களைக் குறிப்பிடுகின்றன.", "Articles 52-78 deal with Union Executive.", "உறுப்புகள் 52-78 ஒன்றிய நிர்வாகத்தைக் குறிப்பிடுகின்றன.", "Articles 315-323 deal with Public Service Commissions.", "உறுப்புகள் 315-323 அரசுப் பணியாளர் தேர்வாணையங்களைக் குறிப்பிடுகின்றன."),
         "Confusing Supreme Court article range (124-147) with High Court range (214-231).", "உச்ச நீதிமன்ற மற்றும் உயர் நீதிமன்ற உறுப்பு வரம்புகளைக் குழப்புவது.", "Articles 124-147 = Supreme Court.", "உறுப்புகள் 124-147 = உச்ச நீதிமன்றம்.", "1"),

        ("POLITY_SC_EASY_003", "Easy",
         "On which date was the Supreme Court of India officially inaugurated?",
         "இந்திய உச்ச நீதிமன்றம் அதிகாரப்பூர்வமாக எந்த நாளில் தொடக்கி வைக்கப்பட்டது?",
         ("26 January 1950", "26 ஜனவரி 1950", "28 January 1950", "28 ஜனவரி 1950", "15 August 1947", "15 ஆகஸ்ட் 1947", "26 November 1949", "26 நவம்பர் 1949"),
         "B",
         "The Supreme Court of India was inaugurated on 28 January 1950, two days after India became a Republic.",
         "இந்தியா குடியரசான இரண்டு நாட்களுக்குப் பிறகு, 1950 ஜனவரி 28 அன்று இந்திய உச்ச நீதிமன்றம் அதிகாரப்பூர்வமாகத் தொடக்கி வைக்கப்பட்டது.",
         ("26 Jan 1950 was Republic Day.", "ஜனவரி 26 குடியரசு தினம்.", "28 Jan 1950 is SC inauguration date.", "1950 ஜனவரி 28 உச்ச நீதிமன்றத் தொடக்க நாள்.", "15 Aug 1947 was Independence Day.", "ஆகஸ்ட் 15 சுதந்திர தினம்.", "26 Nov 1949 was Constitution Adoption date.", "நவம்பர் 26 அரசியலமைப்பு ஏற்றுக்கொள்ளப்பட்ட நாள்."),
         "Confusing 26 January 1950 (Constitution came into force) with 28 January 1950 (SC inauguration).", "26 ஜனவரி மற்றும் 28 ஜனவரியைக் குழப்புவது.", "Inauguration date = 28 January 1950.", "தொடங்கிய நாள் = 28 ஜனவரி 1950.", "1"),

        ("POLITY_SC_EASY_004", "Easy",
         "Which court did the Supreme Court of India replace upon its inauguration in 1950?",
         "1950-ல் தொடங்கப்பட்டபோது இந்திய உச்ச நீதிமன்றம் எந்த நீதிமன்றத்திற்குப் பதிலாக அமைந்தது?",
         ("Federal Court of India and Privy Council jurisdiction", "இந்திய கூட்டாட்சி நீதிமன்றம் மற்றும் பிரிவி கவுன்சில் அதிகார வரம்பு", "High Court of Calcutta", "கொல்கத்தா உயர் நீதிமன்றம்", "Supreme Court of Judicature at Fort William", "வில்லியம் கோட்டை உச்ச நீதிமன்றம்", "Chief Court of Oudh", "அவத் முதன்மை நீதிமன்றம்"),
         "A",
         "The Supreme Court succeeded the Federal Court of India (established under the Government of India Act 1935) and replaced the British Privy Council as the highest court of appeal.",
         "உச்ச நீதிமன்றம் 1935-ம் ஆண்டு இந்திய அரசுச் சட்டத்தின் கீழ் அமைக்கப்பட்ட கூட்டாட்சி நீதிமன்றத்தின் இடத்தைப் பிடித்தது மற்றும் பிரிவி கவுன்சிலின் மேல்முறையீட்டு அதிகார வரம்பை மாற்றீடு செய்தது.",
         ("Federal Court + Privy Council replaced by SC.", "கூட்டாட்சி நீதிமன்றம் + பிரிவி கவுன்சில் ஆகியவற்றுக்குப் பதிலாக SC அமைந்தது.", "Calcutta HC is a state High Court.", "கொல்கத்தா HC ஒரு மாநில உயர் நீதிமன்றம்.", "Fort William court was 1774 Regulating Act court.", "வில்லியம் கோட்டை நீதிமன்றம் 1774 ஒழுங்குமுறைச் சட்ட நீதிமன்றம்.", "Oudh Chief Court was a local provincial court.", "அவத் நீதிமன்றம் ஒரு உள்ளூர் நீதிமன்றம்."),
         "Thinking SC succeeded only Federal Court without replacing Privy Council appellate jurisdiction.", "பிரிவி கவுன்சில் மேல்முறையீட்டு அதிகாரத்தையும் SC கைக்கொண்டது என்பதை நினைவில் கொள்க.", "SC replaced Federal Court of India (1937-1950) & British Privy Council appeals.", "SC கூட்டாட்சி நீதிமன்றம் மற்றும் பிரிவி கவுன்சில் மேல்முறையீடுகளை மாற்றீடு செய்தது.", "1"),

        ("POLITY_SC_EASY_005", "Easy",
         "Under which Article of the Indian Constitution is the Supreme Court established and constituted?",
         "இந்திய அரசியலமைப்பின் எந்த உறுப்பின் கீழ் உச்ச நீதிமன்றம் நிறுவப்பட்டு அமைக்கப்படுகிறது?",
         ("Article 123", "உறுப்பு 123", "Article 124", "உறுப்பு 124", "Article 125", "உறுப்பு 125", "Article 126", "உறுப்பு 126"),
         "B",
         "Article 124 of the Constitution provides for the establishment and constitution of the Supreme Court of India.",
         "அரசியலமைப்பின் உறுப்பு 124 இந்திய உச்ச நீதிமன்றத்தை நிறுவுதல் மற்றும் அமைத்தல் பற்றிக் கூறுகிறது.",
         ("Art 123 relates to Ordinance making power of President.", "உறுப்பு 123 குடியரசுத் தலைவரின் அவசரச்சட்ட அதிகாரம்.", "Art 124 provides for establishment of Supreme Court.", "உறுப்பு 124 உச்ச நீதிமன்ற அமைப்பைக் கூறுகிறது.", "Art 125 deals with Salaries of Judges.", "உறுப்பு 125 நீதிபதிகளின் ஊதியம்.", "Art 126 deals with Acting Chief Justice.", "உறுப்பு 126 தற்காலிக தலைமை நீதிபதி."),
         "Confusing Article 124 (Establishment) with Article 125 (Salaries).", "உறுப்பு 124 மற்றும் 125-ஐக் குழப்புவது.", "Article 124 = Establishment and Constitution of Supreme Court.", "உறுப்பு 124 = உச்ச நீதிமன்றம் நிறுவுதல்.", "1"),

        ("POLITY_SC_EASY_006", "Easy",
         "At the time of inauguration in 1950, what was the original strength of judges in the Supreme Court (including CJI)?",
         "1950-ல் தொடங்கப்பட்டபோது உச்ச நீதிமன்றத்தின் ஆரம்ப நீதிபதிகள் எண்ணிக்கை (தலைமை நீதிபதி உட்பட) என்ன?",
         ("8 Judges", "8 நீதிபதிகள்", "10 Judges", "10 நீதிபதிகள்", "12 Judges", "12 நீதிபதிகள்", "34 Judges", "34 நீதிபதிகள்"),
         "A",
         "Originally, the Constitution of 1950 envisaged a Supreme Court with 1 Chief Justice and 7 other judges (total 8 judges).",
         "1950-ல் அரசியலமைப்பு தொடக்கத்தில் 1 தலைமை நீதிபதி மற்றும் 7 இதர நீதிபதிகள் உட்பட மொத்தம் 8 நீதிபதிகளைக் கொண்டிருந்தது.",
         ("Original strength in 1950 was 8 (1 CJI + 7 Judges).", "1950-ல் ஆரம்ப எண்ணிக்கை 8 (1 CJI + 7 நீதிபதிகள்).", "10 was increased strength in 1956.", "10 என்பது 1956-ல் உயர்த்தப்பட்ட எண்ணிக்கை.", "12 was not an official strength step.", "12 அதிகாரப்பூர்வ எண்ணிக்கை அல்ல.", "34 is the current strength (since 2019).", "34 என்பது தற்போதைய எண்ணிக்கை (2019 முதல்)."),
         "Confusing original 1950 strength (8) with present strength (34).", "1950 ஆரம்ப எண்ணிக்கை (8) மற்றும் தற்போதைய எண்ணிக்கையை (34) குழப்புவது.", "1950 Strength = 1 CJI + 7 Judges = 8 total.", "1950 எண்ணிக்கை = 1 CJI + 7 நீதிபதிகள் = மொத்தம் 8.", "1"),

        ("POLITY_SC_EASY_007", "Easy",
         "Who has the power to increase the number of judges in the Supreme Court of India?",
         "இந்திய உச்ச நீதிமன்ற நீதிபதிகளின் எண்ணிக்கையை உயர்த்தும் அதிகாரம் யாருக்கு உள்ளது?",
         ("President of India", "இந்தியக் குடியரசுத் தலைவர்", "Parliament of India", "இந்திய நாடாளுமன்றம்", "Chief Justice of India", "இந்தியத் தலைமை நீதிபதி", "Law Commission of India", "இந்தியச் சட்ட ஆணையம்"),
         "B",
         "Under Article 124(1), Parliament by law has the authority to prescribe and increase the strength of judges in the Supreme Court.",
         "அரசியலமைப்பு உறுப்பு 124(1)-ன் கீழ், சட்டத்தின் மூலம் உச்ச நீதிமன்ற நீதிபதிகளின் எண்ணிக்கையை நாடாளுமன்றம் மட்டுமே உயர்த்த முடியும்.",
         ("President appoints judges but cannot increase strength.", "குடியரசுத் தலைவர் நீதிபதிகளை நியமிக்கிறார், எண்ணிக்கையை உயர்த்த முடியாது.", "Parliament increases SC judge strength by law.", "நாடாளுமன்றம் சட்டத்தின் மூலம் நீதிபதிகள் எண்ணிக்கையை உயர்த்துகிறது.", "CJI cannot change judge strength.", "தலைமை நீதிபதி எண்ணிக்கையை மாற்ற முடியாது.", "Law Commission is advisory.", "சட்ட ஆணையம் ஆலோசனை அமைப்பாகும்."),
         "Assuming President increases SC judge strength (President increases High Court strength, but Parliament increases SC strength).", "குடியரசுத் தலைவர் உயர் நீதிமன்ற பலத்தை உயர்த்துகிறார், ஆனால் நாடாளுமன்றம் உச்ச நீதிமன்ற பலத்தை உயர்த்துகிறது.", "Supreme Court strength regulated by PARLIAMENT by law.", "உச்ச நீதிமன்ற நீதிபதிகள் எண்ணிக்கை நாடாளுமன்றச் சட்டத்தால் உயர்த்தப்படுகிறது.", "1"),

        ("POLITY_SC_EASY_008", "Easy",
         "What is the current sanctioned strength of Supreme Court judges (including the Chief Justice of India) since 2019?",
         "2019 முதல் உச்ச நீதிமன்ற நீதிபதிகளின் அனுமதிக்கப்பட்ட தற்போதைய எண்ணிக்கை (தலைமை நீதிபதி உட்பட) என்ன?",
         ("31 Judges", "31 நீதிபதிகள்", "34 Judges", "34 நீதிபதிகள்", "30 Judges", "30 நீதிபதிகள்", "26 Judges", "26 நீதிபதிகள்"),
         "C",
         "In 2019, Parliament enacted the Supreme Court (Number of Judges) Amendment Act, increasing the total strength from 31 to 34 (1 CJI + 33 other judges).",
         "2019-ல் நாடாளுமன்றம் இயற்றிய சட்டத் திருத்தத்தின் மூலம் உச்ச நீதிமன்ற நீதிபதிகளின் எண்ணிக்கை 31-லிருந்து 34 ஆக (1 தலைமை நீதிபதி + 33 இதர நீதிபதிகள்) உயர்த்தப்பட்டது.",
         ("31 was the strength from 2008 to 2019.", "31 என்பது 2008 முதல் 2019 வரையிலான எண்ணிக்கை.", "34 is the current sanctioned strength since 2019.", "34 என்பது 2019 முதல் தற்போதைய அனுமதிக்கப்பட்ட எண்ணிக்கை.", "30 was the number of other judges prior to 2019.", "30 என்பது 2019-க்கு முன் இதர நீதிபதிகளின் எண்ணிக்கை.", "26 was the strength from 1986 to 2008.", "26 என்பது 1986 முதல் 2008 வரையிலான எண்ணிக்கை."),
         "Confusing previous strength of 31 (2008) with current strength of 34 (2019).", "2008-ன் 31 மற்றும் 2019-ன் 34 ஆகிய எண்ணிக்கையைக் குழப்புவது.", "Current Strength = 34 (1 CJI + 33 Judges).", "தற்போதைய எண்ணிக்கை = 34 (1 CJI + 33 நீதிபதிகள்).", "1"),

        ("POLITY_SC_EASY_009", "Easy",
         "Who appoints the Chief Justice of India and other judges of the Supreme Court?",
         "இந்தியத் தலைமை நீதிபதி மற்றும் உச்ச நீதிமன்றத்தின் இதர நீதிபதிகளை நியமிப்பவர் யார்?",
         ("Prime Minister", "பிரதமர்", "Parliament", "நாடாளுமன்றம்", "President of India", "இந்தியக் குடியரசுத் தலைவர்", "Union Law Minister", "ஒன்றிய சட்ட அமைச்சர்"),
         "C",
         "Under Article 124(2), every Judge of the Supreme Court is appointed by the President of India by warrant under his hand and seal.",
         "அரசியலமைப்பு உறுப்பு 124(2)-ன் கீழ், உச்ச நீதிமன்றத்தின் ஒவ்வொரு நீதிபதியும் குடியரசுத் தலைவரால் கையொப்பமிட்டு முத்திரையிடப்பட்ட ஆணை மூலம் நியமிக்கப்படுகிறார்.",
         ("Prime Minister has no direct appointing authority.", "பிரதமருக்கு நேரடி நியமன அதிகாரம் இல்லை.", "Parliament does not appoint judges.", "நாடாளுமன்றம் நீதிபதிகளை நியமிப்பதில்லை.", "President appoints SC judges under Article 124(2).", "குடியரசுத் தலைவர் உறுப்பு 124(2)-ன் கீழ் நியமிக்கிறார்.", "Law Minister is part of executive consultation.", "சட்ட அமைச்சர் கலந்தாலோசனையின் ஒரு பகுதி."),
         "Thinking Law Minister or PM directly appoints judges.", "பிரதமரோ அல்லது சட்ட அமைச்சரோ நேரடியாக நியமிக்கிறார் என நினைத்தல்.", "Appointing authority for SC judges = President of India.", "நியமன அதிகாரம் = இந்தியக் குடியரசுத் தலைவர்.", "1"),

        ("POLITY_SC_EASY_010", "Easy",
         "What is the retirement age for a judge of the Supreme Court of India?",
         "இந்திய உச்ச நீதிமன்ற நீதிபதி ஒருவரின் ஓய்வு பெறும் வயது என்ன?",
         ("60 years", "60 வயது", "62 years", "62 வயது", "65 years", "65 வயது", "70 years", "70 வயது"),
         "C",
         "Under Article 124(2), a Supreme Court judge holds office until he attains the age of 65 years.",
         "அரசியலமைப்பு உறுப்பு 124(2)-ன் கீழ், ஒரு உச்ச நீதிமன்ற நீதிபதி தனது 65 வயதை அடையும் வரை பதவியில் இருப்பார்.",
         ("60 years is not standard for superior judiciary.", "60 வயது உயர் நீதித்துறைக்குரியது அல்ல.", "62 years is the retirement age for High Court judges.", "62 வயது உயர் நீதிமன்ற நீதிபதிகளின் ஓய்வு பெற வயது.", "65 years is the retirement age for Supreme Court judges.", "65 வயது உச்ச நீதிமன்ற நீதிபதிகளின் ஓய்வு பெற வயது.", "70 years is not specified for SC judges in Constitution.", "70 வயது அரசியலமைப்பில் குறிப்பிடப்படவில்லை."),
         "Confusing High Court judge retirement age (62 years) with Supreme Court judge retirement age (65 years).", "உயர் நீதிமன்ற நீதிபதியின் ஓய்வு வயது (62) மற்றும் உச்ச நீதிமன்ற நீதிபதியின் ஓய்வு வயதை (65) குழப்புவது.", "Retirement Age: High Court = 62, Supreme Court = 65.", "ஓய்வு வயது: உயர் நீதிமன்றம் = 62, உச்ச நீதிமன்றம் = 65.", "1"),

        ("POLITY_SC_EASY_011", "Easy",
         "To be eligible for appointment as a Supreme Court judge, a person must have been an advocate of a High Court for at least how many years?",
         "உச்ச நீதிமன்ற நீதிபதியாக நியமிக்கப்பட, ஒருவர் உயர் நீதிமன்றத்தில் குறைந்தது எத்தனை ஆண்டுகள் வழக்கறிஞராகப் பணியாற்றியிருக்க வேண்டும்?",
         ("5 years", "5 ஆண்டுகள்", "10 years", "10 ஆண்டுகள்", "15 years", "15 ஆண்டுகள்", "20 years", "20 ஆண்டுகள்"),
         "B",
         "Article 124(3) mandates that a person must have been an advocate of a High Court (or two or more such courts in succession) for at least 10 years.",
         "அரசியலமைப்பு உறுப்பு 124(3)-ன் படி, ஒருவர் உயர் நீதிமன்றத்தில் குறைந்தது 10 ஆண்டுகள் வழக்கறிஞராகப் பணியாற்றியிருக்க வேண்டும்.",
         ("5 years is the experience required if working as a High Court JUDGE.", "5 ஆண்டுகள் என்பது உயர் நீதிமன்ற நீதிபதியாக பணியாற்றியிருக்க வேண்டிய காலம்.", "10 years is the required experience as an ADVOCATE.", "10 ஆண்டுகள் என்பது வழக்கறிஞராக பணியாற்றியிருக்க வேண்டிய காலம்.", "15 years is incorrect.", "15 ஆண்டுகள் என்பது தவறானது.", "20 years is incorrect.", "20 ஆண்டுகள் என்பது தவறானது."),
         "Confusing required judge tenure (5 years as HC judge) with advocate tenure (10 years as HC advocate).", "உயர் நீதிமன்ற நீதிபதி அனுபவம் (5 ஆண்டுகள்) மற்றும் வழக்கறிஞர் அனுபவத்தைக் (10 ஆண்டுகள்) குழப்புவது.", "SC Qualification: HC Judge = 5 yrs OR HC Advocate = 10 yrs.", "SC தகுதி: HC நீதிபதி = 5 ஆண்டுகள் அல்லது HC வழக்கறிஞர் = 10 ஆண்டுகள்.", "1"),

        ("POLITY_SC_EASY_012", "Easy",
         "To be eligible for appointment as a Supreme Court judge, a person must have been a judge of a High Court for at least how many years?",
         "உச்ச நீதிமன்ற நீதிபதியாக நியமிக்கப்பட, ஒருவர் உயர் நீதிமன்ற நீதிபதியாக குறைந்தது எத்தனை ஆண்டுகள் பணியாற்றியிருக்க வேண்டும்?",
         ("5 years", "5 ஆண்டுகள்", "7 years", "7 ஆண்டுகள்", "10 years", "10 ஆண்டுகள்", "12 years", "12 ஆண்டுகள்"),
         "A",
         "Article 124(3) states that a person qualifies for appointment as a Supreme Court judge if he has been a judge of a High Court for at least 5 years.",
         "அரசியலமைப்பு உறுப்பு 124(3)-ன் படி, ஒருவர் உயர் நீதிமன்ற நீதிபதியாக குறைந்தது 5 ஆண்டுகள் பணியாற்றியிருந்தால் அவர் உச்ச நீதிமன்ற நீதிபதியாகத் தகுதி பெறுகிறார்.",
         ("5 years as HC Judge is the constitutional requirement.", "உயர் நீதிமன்ற நீதிபதியாக 5 ஆண்டுகள் பணியாற்றியிருப்பது அரசியலமைப்புத் தேவையாகும்.", "7 years is incorrect.", "7 ஆண்டுகள் என்பது தவறானது.", "10 years is advocate experience requirement.", "10 ஆண்டுகள் வழக்கறிஞர் அனுபவத் தேவை.", "12 years is incorrect.", "12 ஆண்டுகள் என்பது தவறானது."),
         "Switching HC judge tenure (5 years) with HC advocate tenure (10 years).", "நீதிபதி காலம் (5 ஆண்டுகள்) மற்றும் வழக்கறிஞர் காலத்தைக் (10 ஆண்டுகள்) மாற்றி நினைப்பது.", "SC Eligibility: 5 years as High Court Judge.", "SC தகுதி: 5 ஆண்டுகள் உயர் நீதிமன்ற நீதிபதியாக பணியாற்றுதல்.", "1"),

        ("POLITY_SC_EASY_013", "Easy",
         "Who administers the oath or affirmation to a person appointed as a Judge of the Supreme Court?",
         "உச்ச நீதிமன்ற நீதிபதியாக நியமிக்கப்படும் ஒருவருக்கு பதவிப் பிரமாணம் செய்து வைப்பவர் யார்?",
         ("Chief Justice of India", "இந்தியத் தலைமை நீதிபதி", "President of India (or some person appointed by him)", "இந்தியக் குடியரசுத் தலைவர் (அல்லது அவரால் நியமிக்கப்பட்ட நபர்)", "Speaker of Lok Sabha", "மக்களவைத் தலைவர்", "Union Law Minister", "ஒன்றிய சட்ட அமைச்சர்"),
         "B",
         "Under Article 124(6), every person appointed as a Supreme Court Judge takes an oath or affirmation before the President, or some person appointed in that behalf by him.",
         "அரசியலமைப்பு உறுப்பு 124(6)-ன் படி, உச்ச நீதிமன்ற நீதிபதியாக நியமிக்கப்படுபவர் குடியரசுத் தலைவர் அல்லது அவரால் நியமிக்கப்பட்ட நபர் முன்னிலையில் பதவிப் பிரமாணம் எடுக்கிறார்.",
         ("CJI administers oath only if authorized by President.", "தலைமை நீதிபதி குடியரசுத் தலைவரால் அதிகாரமளிக்கப்பட்டால் மட்டுமே செய்வார்.", "President or his designee administers oath under Art 124(6).", "குடியரசுத் தலைவர் அல்லது அவரால் நியமிக்கப்பட்டவர் பதவிப் பிரமாணம் செய்து வைப்பார்.", "Speaker has no role in judge oath.", "சபாநாயகருக்குப் பங்கில்லை.", "Law Minister has no role in oath.", "சட்ட அமைச்சருக்குப் பங்கில்லை."),
         "Assuming the Chief Justice of India administers oath to all SC judges (President does it, though he may delegate).", "தலைமை நீதிபதியே அனைவருக்கும் பிரமாணம் செய்து வைப்பார் எனத் தவறாக எண்ணுவது.", "Oath under Article 124(6) = Administered by President or person appointed by him.", "உறுப்பு 124(6) பிரமாணம் = குடியரசுத் தலைவர் அல்லது அவரால் நியமிக்கப்பட்டவரால் செய்து வைக்கப்படும்.", "1"),

        ("POLITY_SC_EASY_014", "Easy",
         "A judge of the Supreme Court may resign from office by writing under his hand addressed to whom?",
         "உச்ச நீதிமன்ற நீதிபதி தனது ராஜினாமா கடிதத்தை யாருக்கு முகவரியிட்டு அனுப்ப வேண்டும்?",
         ("Chief Justice of India", "இந்தியத் தலைமை நீதிபதி", "Prime Minister of India", "இந்தியப் பிரதமர்", "President of India", "இந்தியக் குடியரசுத் தலைவர்", "Speaker of Lok Sabha", "மக்களவைத் தலைவர்"),
         "C",
         "Under Article 124(2)(a), a Judge may, by writing under his hand addressed to the President, resign his office.",
         "அரசியலமைப்பு உறுப்பு 124(2)(a)-ன் படி, ஒரு நீதிபதி குடியரசுத் தலைவருக்குத் தன் கையொப்பமிட்ட கடிதம் மூலம் பதவி விலகலாம்.",
         ("Resignation is addressed to President, not CJI.", "ராஜினாமா குடியரசுத் தலைவருக்கு அனுப்பப்பட வேண்டும், CJI-க்கு அல்ல.", "PM is not the appointing or receiving authority.", "பிரதமர் பெறும் அதிகாரி அல்ல.", "Resignation letter addressed to President.", "ராஜினாமா கடிதம் குடியரசுத் தலைவருக்கு அனுப்பப்படுகிறது.", "Speaker receives resignation of MPs, not judges.", "சபாநாயகர் எம்.பி-க்களின் ராஜினாமாவைப் பெறுபவர்."),
         "Thinking a judge resigns to the Chief Justice of India.", "தலைமை நீதிபதியிடம் ராஜினாமா கடிதம் கொடுப்பார் என நினைப்பது.", "SC Judge Resignation = Addressed to the PRESIDENT of India.", "SC நீதிபதி ராஜினாமா = இந்தியக் குடியரசுத் தலைவருக்கு முகவரியிடப்பட வேண்டும்.", "1"),

        ("POLITY_SC_EASY_015", "Easy",
         "Under which Article of the Indian Constitution can a judge of the Supreme Court be removed from office?",
         "எந்த அரசியலமைப்பு உறுப்பின் கீழ் உச்ச நீதிமன்ற நீதிபதி பதவியிலிருந்து நீக்கப்படலாம்?",
         ("Article 124(4)", "உறுப்பு 124(4)", "Article 125(2)", "உறுப்பு 125(2)", "Article 126", "உறுப்பு 126", "Article 127", "உறுப்பு 127"),
         "A",
         "Article 124(4) lays down the procedure for the removal of a Supreme Court judge by an order of the President passed after an address by Parliament.",
         "நாடாளுமன்ற தீர்மானத்திற்குப் பின் குடியரசுத் தலைவர் பிறப்பிக்கும் ஆணை மூலம் உச்ச நீதிமன்ற நீதிபதியை நீக்கும் நடைமுறையை உறுப்பு 124(4) கூறுகிறது.",
         ("Art 124(4) specifies removal of SC Judges.", "உறுப்பு 124(4) SC நீதிபதிகள் நீக்கம் பற்றிக் கூறுகிறது.", "Art 125(2) deals with conditions of service.", "உறுப்பு 125(2) பணி நிபந்தனைகள்.", "Art 126 deals with Acting CJI.", "உறுப்பு 126 தற்காலிக CJI.", "Art 127 deals with Ad hoc Judges.", "உறுப்பு 127 தற்காலிக (Ad hoc) நீதிபதிகள்."),
         "Confusing removal article 124(4) with salary/service articles.", "நீக்க உறுப்பு 124(4)-ஐ ஊதிய உறுப்புகளுடன் குழப்புவது.", "Removal of SC Judge = Article 124(4).", "நீக்கம் = உறுப்பு 124(4).", "1"),

        ("POLITY_SC_EASY_016", "Easy",
         "On which grounds can a judge of the Supreme Court be removed from office under Article 124(4)?",
         "உறுப்பு 124(4)-ன் கீழ் எந்தக் காரணங்களின் அடிப்படையில் ஒரு உச்ச நீதிமன்ற நீதிபதி பதவியிலிருந்து நீக்கப்படலாம்?",
         ("Incompetence or corruption only", "தகமையின்மை அல்லது ஊழல் மட்டுமே", "Proved misbehaviour or incapacity", "நிரூபிக்கப்பட்ட தவறான நடத்தை அல்லது இயலாமை", "Disobedience of Presidential orders", "குடியரசுத் தலைவர் உத்தரவுகளை மீறுதல்", "Violation of electoral laws", "தேர்தல் சட்டங்களை மீறுதல்"),
         "B",
         "The Constitution specifies only TWO grounds for the removal of a Supreme Court judge: 'Proved misbehaviour' or 'Incapacity'.",
         "உச்ச நீதிமன்ற நீதிபதியை நீக்குவதற்கு அரசியலமைப்பு இரண்டு காரணங்களை மட்டுமே குறிப்பிடுகிறது: 'நிரூபிக்கப்பட்ட தவறான நடத்தை' (Proved misbehaviour) அல்லது 'இயலாமை' (Incapacity).",
         ("Incompetence/corruption are vague terms not used in text.", "தகமையின்மை/ஊழல் என்பது சட்டப்பூர்வச் சொற்கள் அல்ல.", "Proved misbehaviour or incapacity are the exact constitutional grounds.", "நிரூபிக்கப்பட்ட தவறான நடத்தை அல்லது இயலாமை என்பதே அரசியலமைப்புச் சொற்கள்.", "Disobedience of President is not a ground.", "குடியரசுத் தலைவர் உத்தரவு மீறல் காரணியல்ல.", "Electoral law violation is not a specific constitutional ground.", "தேர்தல் சட்ட மீறல் காரணியல்ல."),
         "Confusing grounds for removal of President ('Violation of Constitution') with grounds for SC Judge ('Proved misbehaviour or incapacity').", "குடியரசுத் தலைவர் நீக்கக் காரணம் மற்றும் நீதிபதி நீக்கக் காரணத்தைக் குழப்புவது.", "Grounds for Removal = Proved misbehaviour OR Incapacity.", "நீக்கக் காரணங்கள் = நிரூபிக்கப்பட்ட தவறான நடத்தை அல்லது இயலாமை.", "1"),

        ("POLITY_SC_EASY_017", "Easy",
         "Which law enacted by Parliament regulates the procedure for the investigation and proof of misbehaviour/incapacity of an SC judge?",
         "உச்ச நீதிமன்ற நீதிபதியின் தவறான நடத்தை அல்லது இயலாமை குறித்த விசாரணை நடைமுறையை ஒழுங்குபடுத்த நாடாளுமன்றம் இயற்றிய சட்டம் எது?",
         ("Judicial Officers Protection Act, 1950", "நீதித்துறை அதிகாரிகள் பாதுகாப்புச் சட்டம், 1950", "Judges (Inquiry) Act, 1968", "நீதிபதிகள் (விசாரணை) சட்டம், 1968", "Supreme Court Rules, 1966", "உச்ச நீதிமன்ற விதிகள், 1966", "Contempt of Courts Act, 1971", "நீதிமன்ற அவமதிப்புச் சட்டம், 1971"),
         "B",
         "The Judges (Inquiry) Act, 1968 regulates the procedure relating to the removal of a judge of the Supreme Court by process of impeachment/address.",
         "நீதிபதிகள் (விசாரணை) சட்டம், 1968 நாடாளுமன்றத்தின் மூலம் உச்ச நீதிமன்ற நீதிபதியை நீக்கும் விசாரணை நடைமுறையை ஒழுங்குபடுத்துகிறது.",
         ("Protection Act deals with immunity of judicial officers.", "பாதுகாப்புச் சட்டம் விலக்களிப்பைக் கையாள்கிறது.", "Judges (Inquiry) Act 1968 sets the exact removal procedure.", "நீதிபதிகள் (விசாரணை) சட்டம் 1968 நீக்க நடைமுறையை அமைக்கிறது.", "SC Rules handle day-to-day court proceedings.", "SC விதிகள் தினசரி நடைமுறைகளைக் கையாளுகின்றன.", "Contempt Act handles court contempt.", "அவமதிப்புச் சட்டம் நீதிமன்ற அவமதிப்பைக் கையாள்கிறது."),
         "Confusing Supreme Court Rules with Judges (Inquiry) Act 1968.", "உச்ச நீதிமன்ற விதிகள் மற்றும் 1968 நீதிபதிகள் விசாரணைச் சட்டத்தைக் குழப்புவது.", "Removal Procedure governed by = Judges (Inquiry) Act, 1968.", "நீக்க நடைமுறை = நீதிபதிகள் (விசாரணை) சட்டம், 1968.", "1"),

        ("POLITY_SC_EASY_018", "Easy",
         "To admit a removal motion against a Supreme Court judge in Lok Sabha, how many members must sign the notice?",
         "மக்களவையில் உச்ச நீதிமன்ற நீதிபதிக்கு எதிரான நீக்க தீர்மானத்தை ஏற்க எத்தனை உறுப்பினர்கள் கையொப்பமிட வேண்டும்?",
         ("50 members", "50 உறுப்பினர்கள்", "100 members", "100 உறுப்பினர்கள்", "150 members", "150 உறுப்பினர்கள்", "200 members", "200 உறுப்பினர்கள்"),
         "B",
         "Under the Judges (Inquiry) Act 1968, a removal motion signed by at least 100 members in Lok Sabha or 50 members in Rajya Sabha must be submitted to the Presiding Officer.",
         "1968 நீதிபதிகள் விசாரணைச் சட்டத்தின்படி, நீக்கத் தீர்மான அறிக்கை மக்களவையில் குறைந்தபட்சம் 100 உறுப்பினர்களாலும், மாநிலங்களவையில் 50 உறுப்பினர்களாலும் கையொப்பமிடப்பட வேண்டும்.",
         ("50 members is required for RAJYA SABHA notice.", "50 உறுப்பினர்கள் மாநிலங்களவைக்குத் தேவை.", "100 members is required for LOK SABHA notice.", "100 உறுப்பினர்கள் மக்களவைக்குத் தேவை.", "150 is incorrect.", "150 என்பது தவறானது.", "200 is incorrect.", "200 என்பது தவறானது."),
         "Confusing Lok Sabha requirement (100 members) with Rajya Sabha requirement (50 members).", "மக்களவை (100) மற்றும் மாநிலங்களவை (50) உறுப்பினர்கள் எண்ணிக்கையைக் குழப்புவது.", "Notice signature: Lok Sabha = 100 members, Rajya Sabha = 50 members.", "அறிவிப்பு கையொப்பம்: மக்களவை = 100, மாநிலங்களவை = 50.", "1"),

        ("POLITY_SC_EASY_019", "Easy",
         "To admit a removal motion against a Supreme Court judge in Rajya Sabha, how many members must sign the notice?",
         "மாநிலங்களவையில் உச்ச நீதிமன்ற நீதிபதிக்கு எதிரான நீக்க தீர்மானத்தை ஏற்க எத்தனை உறுப்பினர்கள் கையொப்பமிட வேண்டும்?",
         ("25 members", "25 உறுப்பினர்கள்", "50 members", "50 உறுப்பினர்கள்", "75 members", "75 உறுப்பினர்கள்", "100 members", "100 உறுப்பினர்கள்"),
         "B",
         "In Rajya Sabha, a notice of motion for removal of an SC judge must be signed by at least 50 members before submission to the Chairman.",
         "மாநிலங்களவையில் உச்ச நீதிமன்ற நீதிபதி நீக்கத் தீர்மான அறிவிப்பு தலைவரிடம் சமர்ப்பிக்கப்படுவதற்கு முன் குறைந்தபட்சம் 50 உறுப்பினர்களால் கையொப்பமிடப்பட வேண்டும்.",
         ("25 members is incorrect.", "25 என்பது தவறு.", "50 members is the Rajya Sabha requirement.", "50 உறுப்பினர்கள் என்பது மாநிலங்களவை தேவை.", "75 members is incorrect.", "75 என்பது தவறு.", "100 members is the Lok Sabha requirement.", "100 உறுப்பினர்கள் மக்களவை தேவை."),
         "Confusing Rajya Sabha threshold (50) with Lok Sabha threshold (100).", "மாநிலங்களவை (50) மற்றும் மக்களவை (100) எண்ணிக்கையைக் குழப்புவது.", "Rajya Sabha Removal Notice = 50 members.", "மாநிலங்களவை நீக்க அறிவிப்பு = 50 உறுப்பினர்கள்.", "1"),

        ("POLITY_SC_EASY_020", "Easy",
         "Who appoints an acting Chief Justice of India when the office of CJI is vacant or when the CJI is absent?",
         "தலைமை நீதிபதி பதவி காலியாக இருக்கும்போது அல்லது அவர் வர முடியாதபோது தற்காலிகத் தலைமை நீதிபதியை நியமிப்பவர் யார்?",
         ("Senior-most judge of SC automatically", "மூத்த நீதிபதி தானாகவே", "President of India", "இந்தியக் குடியரசுத் தலைவர்", "Union Law Minister", "ஒன்றிய சட்ட அமைச்சர்", "Collegium of Supreme Court", "உச்ச நீதிமன்ற கொலீஜியம்"),
         "B",
         "Under Article 126, when the office of Chief Justice of India is vacant or when CJI is absent, the duties of the office shall be performed by one of the other judges of the court as the President may appoint.",
         "உறுப்பு 126-ன் படி, தலைமை நீதிபதி பதவி காலியாக இருக்கும்போது குடியரசுத் தலைவரால் நியமிக்கப்படும் மற்றொரு நீதிபதி தற்காலிகத் தலைமை நீதிபதியாகச் செயல்படுவார்.",
         ("Senior-most judge is usually appointed, but appointment order is issued by President.", "மூத்த நீதிபதியே நியமிக்கப்படுகிறார், ஆனால் ஆணை குடியரசுத் தலைவரால் பிறப்பிக்கப்படுகிறது.", "President appoints Acting CJI under Article 126.", "குடியரசுத் தலைவர் உறுப்பு 126-ன் கீழ் தற்காலிக CJI-யை நியமிக்கிறார்.", "Law Minister has no appointing power.", "சட்ட அமைச்சருக்கு நியமன அதிகாரமில்லை.", "Collegium selects regular judges, does not issue acting appointment.", "கொலீஜியம் ஆணை பிறப்பிப்பதில்லை."),
         "Assuming automatic assumption of office without formal appointment by the President.", "குடியரசுத் தலைவர் நியமன ஆணை இன்றி தானாகவே செயல்படுவார் என நினைப்பது.", "Acting CJI appointed by = President of India under Article 126.", "தற்காலிக CJI நியமனம் = உறுப்பு 126-ன் கீழ் குடியரசுத் தலைவர்.", "1"),

        ("POLITY_SC_EASY_021", "Easy",
         "Under which Article of the Indian Constitution can Ad Hoc Judges be appointed to the Supreme Court?",
         "எந்த அரசியலமைப்பு உறுப்பின் கீழ் உச்ச நீதிமன்றத்திற்கு தற்காலிக (Ad Hoc) நீதிபதிகள் நியமிக்கப்படலாம்?",
         ("Article 126", "உறுப்பு 126", "Article 127", "உறுப்பு 127", "Article 128", "உறுப்பு 128", "Article 129", "உறுப்பு 129"),
         "B",
         "Article 127 provides for the appointment of High Court judges as Ad Hoc judges of the Supreme Court when there is a lack of quorum of permanent judges.",
         "நிரந்தர நீதிபதிகளின் எண்ணிக்கை (Quorum) குறைவாக இருக்கும்போது, உயர் நீதிமன்ற நீதிபதிகளை உச்ச நீதிமன்ற தற்காலிக (Ad Hoc) நீதிபதிகளாக நியமிப்பது பற்றி உறுப்பு 127 கூறுகிறது.",
         ("Art 126 deals with Acting CJI.", "உறுப்பு 126 தற்காலிக CJI.", "Art 127 deals with Ad Hoc Judges.", "உறுப்பு 127 Ad Hoc நீதிபதிகள்.", "Art 128 deals with attendance of retired judges.", "உறுப்பு 128 ஓய்வு பெற்ற நீதிபதிகளின் வருகை.", "Art 129 deals with Court of Record.", "உறுப்பு 129 பதிவு நீதிமன்றம்."),
         "Confusing Article 127 (Ad hoc judges) with Article 128 (Retired judges).", "உறுப்பு 127 (அட்ஹாக் நீதிபதிகள்) மற்றும் உறுப்பு 128 (ஓய்வு பெற்ற நீதிபதிகள்) ஆகியவற்றை குழப்புவது.", "Ad Hoc Judges = Article 127.", "தற்காலிக (Ad Hoc) நீதிபதிகள் = உறுப்பு 124/127 (உறுப்பு 127).", "1"),

        ("POLITY_SC_EASY_022", "Easy",
         "Who can appoint a High Court judge as an Ad Hoc judge of the Supreme Court under Article 127?",
         "உறுப்பு 127-ன் கீழ் ஒரு உயர் நீதிமன்ற நீதிபதியை உச்ச நீதிமன்ற Ad Hoc நீதிபதியாக நியமிப்பவர் யார்?",
         ("Chief Justice of India (with prior consent of President)", "இந்தியத் தலைமை நீதிபதி (குடியரசுத் தலைவரின் முன்அனுமதியுடன்)", "President of India directly", "இந்தியக் குடியரசுத் தலைவர் நேரடியாக", "Union Law Minister", "ஒன்றிய சட்ட அமைச்சர்", "Governor of the concerned State", "சம்பந்தப்பட்ட மாநில ஆளுநர்"),
         "A",
         "Under Article 127, the Chief Justice of India can appoint a qualified High Court judge as an ad hoc judge of the Supreme Court with the previous consent of the President and consultation with the Chief Justice of the High Court concerned.",
         "உறுப்பு 127-ன் கீழ், குடியரசுத் தலைவரின் முன்அனுமதி மற்றும் சம்பந்தப்பட்ட உயர் நீதிமன்றத் தலைமை நீதிபதியைக் கலந்தாலோசித்து, இந்தியத் தலைமை நீதிபதி Ad Hoc நீதிபதியை நியமிக்கிறார்.",
         ("CJI appoints Ad hoc judge with President's consent.", "குடியரசுத் தலைவர் அனுமதியுடன் CJI நியமிக்கிறார்.", "President directly appoints regular judges, not ad hoc.", "குடியரசுத் தலைவர் வழக்கமான நீதிபதிகளை நியமிக்கிறார்.", "Law Minister is not the appointing authority.", "சட்ட அமைச்சர் அதிகாரி அல்ல.", "Governor has no jurisdiction over SC ad hoc judges.", "ஆளுநருக்கு இதில் அதிகாரமில்லை."),
         "Assuming President directly appoints Ad hoc judges (CJI appoints them with President's consent).", "குடியரசுத் தலைவரே நேரடியாக அட்ஹாக் நீதிபதிகளை நியமிப்பார் எனத் தவறாக நினைப்பது.", "Ad Hoc Judge Appointed by = Chief Justice of India (with previous consent of President).", "Ad Hoc நீதிபதி நியமனம் = இந்திய தலைமை நீதிபதி (குடியரசுத் தலைவரின் முன் அனுமதியுடன்).", "1"),

        ("POLITY_SC_EASY_023", "Easy",
         "Under Article 128, who can request a retired Supreme Court or Federal Court judge to sit and act as a judge of the Supreme Court?",
         "உறுப்பு 128-ன் கீழ் ஓய்வு பெற்ற உச்ச நீதிமன்ற நீதிபதியை நீதிமன்ற அமர்வில் கலந்துகொள்ளக் கோருபவர் யார்?",
         ("Chief Justice of India (with previous consent of President)", "இந்தியத் தலைமை நீதிபதி (குடியரசுத் தலைவரின் முன்அனுமதியுடன்)", "President of India independently", "இந்தியக் குடியரசுத் தலைவர் தன்னிச்சையாக", "Law Commission of India", "இந்தியச் சட்ட ஆணையம்", "Parliament of India", "இந்திய நாடாளுமன்றம்"),
         "A",
         "Under Article 128, the Chief Justice of India may at any time, with the previous consent of the President, request a retired SC judge to sit and act as a judge.",
         "உறுப்பு 128-ன் படி, குடியரசுத் தலைவரின் முன்அனுமதியுடன் இந்தியத் தலைமை நீதிபதி ஓய்வு பெற்ற நீதிபதியைக் கலந்துகொள்ளக் கோரலாம்.",
         ("CJI requests retired judge with President's consent.", "குடியரசுத் தலைவர் அனுமதியுடன் CJI கோருகிறார்.", "President does not issue request directly.", "குடியரசுத் தலைவர் நேரடியாக கோருவதில்லை.", "Law Commission has no operational court power.", "சட்ட ஆணையத்திற்கு அதிகாரமில்லை.", "Parliament has no court session power.", "நாடாளுமன்றத்திற்கு அதிகாரமில்லை."),
         "Confusing retired judge attendance under Art 128 with regular appointments.", "ஓய்வு பெற்ற நீதிபதி வருகையை வழக்கமான நியமனத்துடன் குழப்புவது.", "Retired Judge Sitting (Art 128) = CJI requests with President's consent.", "ஓய்வு பெற்ற நீதிபதி வருகை (உறுப்பு 128) = CJI குடியரசுத் தலைவர் அனுமதியுடன் கோருகிறார்.", "1"),

        ("POLITY_SC_EASY_024", "Easy",
         "Which Article of the Indian Constitution declares that the Supreme Court shall be a 'Court of Record'?",
         "இந்திய அரசியலமைப்பின் எந்த உறுப்பு உச்ச நீதிமன்றத்தை ஒரு 'பதிவு நீதிமன்றம்' (Court of Record) என அறிவிக்கிறது?",
         ("Article 128", "உறுப்பு 128", "Article 129", "உறுப்பு 129", "Article 130", "உறுப்பு 130", "Article 131", "உறுப்பு 131"),
         "B",
         "Article 129 provides that the Supreme Court shall be a Court of Record and shall have all powers of such a court including the power to punish for contempt of itself.",
         "அரசியலமைப்பு உறுப்பு 129 உச்ச நீதிமன்றம் ஒரு பதிவு நீதிமன்றமாகும் என்றும், தன் அவமதிப்புக்குத் தண்டிக்கும் அதிகாரம் உட்பட அணைத்து அதிகாரங்களையும் கொண்டது என்றும் அறிவிக்கிறது.",
         ("Art 128 deals with retired judges.", "உறுப்பு 128 ஓய்வு பெற்ற நீதிபதிகள்.", "Art 129 declares Supreme Court as Court of Record.", "உறுப்பு 129 உச்ச நீதிமன்றத்தைப் பதிவு நீதிமன்றமாக அறிவிக்கிறது.", "Art 130 deals with Seat of Supreme Court.", "உறுப்பு 130 உச்ச நீதிமன்றத்தின் அமைவிடம்.", "Art 131 deals with Original Jurisdiction.", "உறுப்பு 131 மூல ஆதிக்கம்."),
         "Confusing Article 129 (Court of Record) with Article 130 (Seat of SC) or Article 131 (Original Jurisdiction).", "உறுப்பு 129, 130 மற்றும் 131-ஐக் குழப்புவது.", "Court of Record = Article 129.", "பதிவு நீதிமன்றம் = உறுப்பு 129.", "1"),

        ("POLITY_SC_EASY_025", "Easy",
         "What are the two primary implications of the Supreme Court being a 'Court of Record' under Article 129?",
         "உறுப்பு 129-ன் கீழ் உச்ச நீதிமன்றம் 'பதிவு நீதிமன்றம்' என்பதன் இரண்டு முக்கிய விளைவுகள் யாவை?",
         ("Evidentiary value of records and power to punish for contempt", "ஆவணங்களின் சான்றாதார மதிப்பு மற்றும் அவமதிப்புக்குத் தண்டிக்கும் அதிகாரம்", "Power to dissolve Parliament and power to audit accounts", "நாடாளுமன்றத்தைக் கலைக்கும் அதிகாரம் மற்றும் தணிக்கை அதிகாரம்", "Power to appoint Governors and power to framed state budgets", "ஆளுநர்களை நியமிக்கும் அதிகாரம் மற்றும் மாநில வரவுசெலவு அதிகாரம்", "Power to control High Courts administratively and power to tax", "உயர் நீதிமன்றங்களை நிர்வாக ரீதியாகக் கட்டுப்படுத்தும் அதிகாரம் மற்றும் வரி விதிக்கும் அதிகாரம்"),
         "A",
         "As a Court of Record, (1) its judgments have perpetual memory and evidentiary value in all courts, and (2) it has the power to punish for contempt of itself.",
         "பதிவு நீதிமன்றமாக, (1) இதன் தீர்ப்புகள் அனைத்து நீதிமன்றங்களிலும் சான்றாதார மதிப்பு கொண்டவை, (2) நீதிமன்ற அவமதிப்புக்குத் தண்டிக்கும் அதிகாரம் கொண்டது.",
         ("Evidentiary value + Contempt punishment are the defining features of Court of Record.", "சான்றாதார மதிப்பு + அவமதிப்புத் தண்டனை என்பதே பதிவு நீதிமன்றத்தின் அம்சங்கள்.", "Dissolving Parliament is not a court power.", "நாடாளுமன்றக் கலைப்பு நீதிமன்ற அதிகாரமல்ல.", "Governor appointment is done by President.", "ஆளுநர் நியமனம் குடியரசுத் தலைவரால் செய்யப்படுகிறது.", "Administrative control over HCs belongs to HCs themselves under Art 235.", "உயர் நீதிமன்ற நிர்வாக அதிகாரம் அவற்றுக்கே உரியது."),
         "Thinking Court of Record means maintaining criminal administrative records only.", "பதிவு நீதிமன்றம் என்றால் வெறும் ஆவணப் பராமரிப்பு மட்டுமே என நினைப்பது.", "Court of Record = (1) Evidentiary Value of Judgments, (2) Power to Punish for Contempt.", "பதிவு நீதிமன்றம் = (1) சான்றாதார மதிப்பு, (2) அவமதிப்புத் தண்டனை அதிகாரம்.", "1"),

        ("POLITY_SC_EASY_026", "Easy",
         "Where is the seat of the Supreme Court of India constitutionally located according to Article 130?",
         "உறுப்பு 130-ன் படி உச்ச நீதிமன்றத்தின் அமைவிடம் (Seat) அரசியலமைப்பு ரீதியாக எங்கு அமைந்துள்ளது?",
         ("Kolkata", "கொல்கத்தா", "Mumbai", "மும்பை", "Delhi", "டெல்லி", "Chennai", "சென்னை"),
         "C",
         "Article 130 declares Delhi as the seat of the Supreme Court. The CJI can appoint another place with the approval of the President.",
         "அரசியலமைப்பு உறுப்பு 130 டெல்லியை உச்ச நீதிமன்றத்தின் அமைவிடமாக அறிவிக்கிறது. குடியரசுத் தலைவரின் ஒப்புதலுடன் தலைமை நீதிபதி பிற இடங்களையும் குறிப்பிடலாம்.",
         ("Kolkata was seat of old Federal Court pre-1937.", "கொல்கத்தா பழைய கூட்டாட்சி நீதிமன்றத்தின் அமைவிடம்.", "Mumbai was never the constitutional seat of SC.", "மும்பை அரசியலமைப்பு அமைவிடம் அல்ல.", "Delhi is the constitutionally specified seat under Article 130.", "டெல்லி உறுப்பு 130-ன் கீழ் குறிப்பிடப்பட்ட அமைவிடம்.", "Chennai is a regional place.", "சென்னை ஒரு பிராந்திய இடம்."),
         "Confusing Kolkata (historical presidency court) with Delhi (constitutional seat under Art 130).", "கொல்கத்தா மற்றும் டெல்லியைக் குழப்புவது.", "Seat of Supreme Court = Delhi (Article 130).", "உச்ச நீதிமன்ற அமைவிடம் = டெல்லி (உறுப்பு 130).", "1"),

        ("POLITY_SC_EASY_027", "Easy",
         "Who has the constitutional authority to appoint other places as seats of the Supreme Court besides Delhi under Article 130?",
         "உறுப்பு 130-ன் கீழ் டெல்லி தவிர பிற இடங்களை உச்ச நீதிமன்ற அமைவிடமாக அறிவிக்கும் அதிகாரம் யாருக்கு உள்ளது?",
         ("President of India independently", "இந்தியக் குடியரசுத் தலைவர் தன்னிச்சையாக", "Chief Justice of India (with approval of the President)", "இந்தியத் தலைமை நீதிபதி (குடியரசுத் தலைவரின் ஒப்புதலுடன்)", "Parliament by a 2/3rd majority law", "நாடாளுமன்றம் 2/3 பெரும்பான்மை சட்டத்தின் மூலம்", "Union Law Commission", "ஒன்றிய சட்ட ஆணையம்"),
         "B",
         "Article 130 states that the Supreme Court shall sit in Delhi or in such other place or places as the Chief Justice of India may, with the approval of the President, from time to time appoint.",
         "உறுப்பு 130-ன் படி, குடியரசுத் தலைவரின் ஒப்புதலுடன் இந்தியத் தலைமை நீதிபதி அவ்வப்போது குறிப்பிடும் பிற இடங்களிலும் உச்ச நீதிமன்றம் இயங்கலாம்.",
         ("President independently cannot change seat.", "குடியரசுத் தலைவர் தன்னிச்சையாக மாற்ற முடியாது.", "CJI with approval of President can appoint other seats.", "குடியரசுத் தலைவர் ஒப்புதலுடன் CJI பிற இடங்களை அமைக்கலாம்.", "Parliament constitutional amendment is not mandatory for changing seat under Art 130.", "நாடாளுமன்ற அரசியலமைப்புத் திருத்தம் தேவையில்லை.", "Law Commission has no executive court power.", "சட்ட ஆணையத்திற்கு அதிகாரமில்லை."),
         "Assuming Parliament must pass a constitutional amendment to hold SC bench outside Delhi.", "டெல்லிக்கு வெளியே அமர்வு அமைக்க நாடாளுமன்ற திருத்தம் தேவை எனக் கருதுவது.", "Appointing alternate SC seat = Chief Justice of India with approval of the President.", "மாற்று அமைவிடம் = குடியரசுத் தலைவர் ஒப்புதலுடன் இந்தியத் தலைமை நீதிபதி.", "1"),

        ("POLITY_SC_EASY_028", "Easy",
         "Which Article of the Indian Constitution vests Original Jurisdiction in the Supreme Court for federal disputes?",
         "கூட்டாட்சித் தகராறுகளுக்கான மூல ஆதிக்கத்தை (Original Jurisdiction) உச்ச நீதிமன்றத்திற்கு வழங்கும் அரசியலமைப்பு உறுப்பு எது?",
         ("Article 131", "உறுப்பு 131", "Article 132", "உறுப்பு 132", "Article 133", "உறுப்பு 133", "Article 134", "உறுப்பு 134"),
         "A",
         "Article 131 deals with the Original Jurisdiction of the Supreme Court in disputes between the Centre and States or between States.",
         "அரசியலமைப்பு உறுப்பு 131 ஒன்றியம் மற்றும் மாநிலங்களுக்கு இடையேயான அல்லது மாநிலங்களுக்கு இடையேயான தகராறுகளில் உச்ச நீதிமன்றத்தின் மூல ஆதிக்கத்தைக் கையாள்கிறது.",
         ("Art 131 = Original Jurisdiction.", "உறுப்பு 131 = மூல ஆதிக்கம்.", "Art 132 = Appellate Jurisdiction in Constitutional matters.", "உறுப்பு 132 = அரசியலமைப்பு மேல்முறையீட்டு ஆதிக்கம்.", "Art 133 = Civil Appellate Jurisdiction.", "உறுப்பு 133 = சிவில் மேல்முறையீட்டு ஆதிக்கம்.", "Art 134 = Criminal Appellate Jurisdiction.", "உறுப்பு 134 = குற்றவியல் மேல்முறையீட்டு ஆதிக்கம்."),
         "Confusing Article 131 (Original Jurisdiction) with Article 132/133 (Appellate Jurisdiction).", "உறுப்பு 131 (மூல ஆதிக்கம்) மற்றும் உறுப்பு 132/133 (மேல்முறையீட்டு ஆதிக்கம்) ஆகியவற்றை குழப்புவது.", "Original Jurisdiction = Article 131.", "மூல ஆதிக்கம் = உறுப்பு 131.", "1"),

        ("POLITY_SC_EASY_029", "Easy",
         "Which of the following disputes falls under the EXCLUSIVE Original Jurisdiction of the Supreme Court under Article 131?",
         "எந்தத் தகராறு உறுப்பு 131-ன் கீழ் உச்ச நீதிமன்றத்தின் தனிப்பட்ட மூல ஆதிக்கத்தின் (Exclusive Original Jurisdiction) கீழ் வருகிறது?",
         ("Dispute between two private citizens", "இரண்டு தனிநபர்களுக்கு இடையேயான தகராறு", "Dispute between Government of India and one or more States", "இந்திய அரசு மற்றும் ஒன்று அல்லது அதற்கு மேற்பட்ட மாநிலங்களுக்கு இடையேயான தகராறு", "Dispute between two corporate companies", "இரண்டு பெரு நிறுவனங்களுக்கு இடையேயான தகராறு", "Dispute between a municipal corporation and a citizen", "நகராட்சி மற்றும் குடிமகனுக்கு இடையேயான தகராறு"),
         "B",
         "Article 131 gives SC exclusive original jurisdiction in federal disputes: Centre vs State(s), Centre + State(s) vs State(s), or State vs State.",
         "உறுப்பு 131 ஒன்றியம் vs மாநிலம், ஒன்றியம்+மாநிலம் vs மாநிலம், மாநிலம் vs மாநிலம் ஆகிய கூட்டாட்சித் தகராறுகளில் உச்ச நீதிமன்றத்திற்குத் தனிப்பட்ட மூல ஆதிக்கத்தை அளிக்கிறது.",
         ("Private citizen disputes do not lie under Art 131.", "தனிநபர் தகராறுகள் உறுப்பு 131-ன் கீழ் வராது.", "Centre vs State dispute is the classic federal dispute under Art 131.", "ஒன்றியம் vs மாநிலம் தகராறே உறுப்பு 131-ன் கீழ் வரும்.", "Corporate disputes do not lie under Art 131.", "நிறுவன தகராறுகள் வராது.", "Municipal disputes do not lie under Art 131.", "நகராட்சி தகராறுகள் வராது."),
         "Thinking private individuals can file original suit in SC under Article 131 (Art 131 is strictly for Centre/State federal units).", "தனிநபர்கள் உறுப்பு 131-ன் கீழ் வழக்கு தொடரலாம் என நினைப்பது.", "Art 131 Original Jurisdiction = Strictly federal disputes (Centre vs State / State vs State).", "உறுப்பு 131 மூல ஆதிக்கம் = கூட்டாட்சி அமைப்புகளுக்கு இடையேயான தகராறுகள் மட்டுமே.", "1"),

        ("POLITY_SC_EASY_030", "Easy",
         "Under Article 32 of the Constitution, what type of jurisdiction does the Supreme Court exercise regarding Fundamental Rights?",
         "அரசியலமைப்பு உறுப்பு 32-ன் கீழ் அடிப்படை உரிமைகள் தொடர்பாக உச்ச நீதிமன்றம் எந்த வகையான அதிகார வரம்பைப் பயன்படுத்துகிறது?",
         ("Advisory Jurisdiction", "ஆலோசனை ஆதிக்கம்", "Writ Jurisdiction (Original but not exclusive)", "நீதிப்பேராணை ஆதிக்கம் (மூல ஆதிக்கம் ஆனால் தனிப்பட்டதல்ல)", "Appellate Jurisdiction only", "மேல்முறையீட்டு ஆதிக்கம் மட்டுமே", "Arbitral Jurisdiction", "மத்தியஸ்த ஆதிக்கம்"),
         "B",
         "Under Article 32, SC has original jurisdiction to enforce Fundamental Rights via writs (Habeas Corpus, Mandamus, Prohibition, Quo-Warranto, Certiorari), shared concurrently with High Courts under Article 226.",
         "உறுப்பு 32-ன் கீழ் அடிப்படை உரிமைகளை அமல்படுத்த உச்ச நீதிமன்றத்திற்கு மூல ஆதிக்கம் உள்ளது, ஆனால் இது உறுப்பு 226-ன் கீழ் உயர் நீதிமன்றங்களுக்கும் பகிர்ந்தளிக்கப்பட்டுள்ளது (தனிப்பட்டதல்ல).",
         ("Advisory jurisdiction is under Art 143.", "ஆலோசனை ஆதிக்கம் உறுப்பு 143-ன் கீழ் உள்ளது.", "Art 32 gives Original Writ Jurisdiction (concurrent with HC Art 226).", "உறுப்பு 32 மூல நீதிப்பேராணை அதிகாரத்தை அளிக்கிறது.", "Appellate jurisdiction is under Arts 132-136.", "மேல்முறையீட்டு ஆதிக்கம் உறுப்புகள் 132-136.", "Arbitral jurisdiction is separate statutory arbitration.", "மத்தியஸ்த அதிகாரம் சட்டப்பூர்வமானது."),
         "Assuming Article 32 writ jurisdiction is EXCLUSIVE to the Supreme Court (High Courts also have writ jurisdiction under Art 226).", "உறுப்பு 32 நீதிப்பேராணை உச்ச நீதிமன்றத்திற்கு மட்டுமே பிரத்யேகமானது எனக் கருதுவது.", "Writ Jurisdiction = Original but CONCURRENT with High Courts (Art 226).", "நீதிப்பேராணை ஆதிக்கம் = மூல ஆதிக்கம், ஆனால் உயர் நீதிமன்றங்களுடன் இணைந்தது.", "1"),

        ("POLITY_SC_EASY_031", "Easy",
         "Which Article of the Indian Constitution grants Advisory Jurisdiction to the Supreme Court (President seeking SC opinion)?",
         "இந்திய உச்ச நீதிமன்றத்திற்கு ஆலோசனை ஆதிக்கத்தை (குடியரசுத் தலைவர் SC கருத்து கோருதல்) வழங்கும் உறுப்பு எது?",
         ("Article 136", "உறுப்பு 136", "Article 141", "உறுப்பு 141", "Article 142", "உறுப்பு 142", "Article 143", "உறுப்பு 143"),
         "D",
         "Article 143 authorizes the President of India to consult the Supreme Court on any question of law or fact of public importance.",
         "பொது முக்கியத்துவம் வாய்ந்த சட்ட அல்லது உண்மை விவகாரங்களில் உச்ச நீதிமன்றத்தின் ஆலோசனையைக் கோர குடியரசுத் தலைவருக்கு உறுப்பு 143 அதிகாரமளிக்கிறது.",
         ("Art 136 = Special Leave Petition (SLP).", "உறுப்பு 136 = சிறப்பு விடுப்பு மனு.", "Art 141 = Law declared by SC binding on all courts.", "உறுப்பு 141 = SC சட்டம் அனைத்து நீதிமன்றங்களையும் கட்டுப்படுத்தும்.", "Art 142 = Complete justice enforcement.", "உறுப்பு 142 = முழுமையான நீதி அமலாக்கம்.", "Art 143 = Advisory Jurisdiction of SC.", "உறுப்பு 143 = உச்ச நீதிமன்ற ஆலோசனை ஆதிக்கம்."),
         "Confusing Article 143 (Advisory Jurisdiction) with Article 142 (Complete Justice).", "உறுப்பு 143 (ஆலோசனை ஆதிக்கம்) மற்றும் உறுப்பு 142 (முழுமையான நீதி) ஆகியவற்றை குழப்புவது.", "Advisory Jurisdiction = Article 143.", "ஆலோசனை ஆதிக்கம் = உறுப்பு 143.", "1"),

        ("POLITY_SC_EASY_032", "Easy",
         "Is the opinion expressed by the Supreme Court under Advisory Jurisdiction (Article 143) binding on the President?",
         "ஆலோசனை ஆதிக்கத்தின் (உறுப்பு 143) கீழ் உச்ச நீதிமன்றம் அளிக்கும் கருத்து குடியரசுத் தலைவரைக் கட்டுப்படுத்துமா?",
         ("Yes, it is strictly binding law", "ஆம், அது கண்டிப்பான சட்டமாகும்", "No, it is advisory only and not binding on the President", "இல்லை, அது வெறும் ஆலோசனையே, குடியரசுத் தலைவரைக் கட்டுப்படுத்தாது", "Yes, if passed by a 7-judge bench", "ஆம், 7 நீதிபதிகள் அமர்வு வழங்கினால் கட்டுப்படுத்தும்", "Binding only during a National Emergency", "தேசிய அவசரநிலையின் போது மட்டுமே கட்டுப்படுத்தும்"),
         "B",
         "The opinion given by the Supreme Court under Article 143 is purely advisory in nature and not a judicial order or decree; hence, it is NOT binding on the President.",
         "உறுப்பு 143-ன் கீழ் உச்ச நீதிமன்றம் அளிக்கும் ஆலோசனை நீதிமன்ற உத்தரவு அல்ல; எனவே அது குடியரசுத் தலைவரைக் கட்டுப்படுத்தாது.",
         ("SC opinion under Art 143 is not a decree.", "Art 143 தீர்ப்பு அல்ல.", "Purely advisory and NOT binding on the President.", "வெறும் ஆலோசனையே, குடியரசுத் தலைவரைக் கட்டுப்படுத்தாது.", "Bench size does not change its advisory character.", "அமர்வு அளவு அதன் ஆலோசனை தன்மையை மாற்றாது.", "Emergency does not make it binding.", "அவசரநிலை அதை கட்டாயமாக்காது."),
         "Thinking advisory opinion under Article 143 carries the binding force of Article 141 rulings.", "உறுப்பு 143 கருத்து உறுப்பு 141 போலக் கட்டுப்படுத்தும் என நினைப்பது.", "Article 143 Advisory Opinion = NOT binding on the President.", "உறுப்பு 143 ஆலோசனை = குடியரசுத் தலைவரைக் கட்டுப்படுத்தாது.", "1"),

        ("POLITY_SC_EASY_033", "Easy",
         "Which Article of the Constitution provides for Special Leave to Appeal by the Supreme Court (SLP)?",
         "உச்ச நீதிமன்றத்தின் சிறப்பு விடுப்பு மேல்முறையீடு (SLP) பற்றிக் கூறும் அரசியலமைப்பு உறுப்பு எது?",
         ("Article 136", "உறுப்பு 136", "Article 137", "உறுப்பு 137", "Article 138", "உறுப்பு 138", "Article 139", "உறுப்பு 139"),
         "A",
         "Article 136 empowers the Supreme Court to grant special leave to appeal from any judgment, decree, determination, sentence, or order in any cause or matter passed by any court or tribunal in India.",
         "இந்தியாவில் உள்ள எந்தவொரு நீதிமன்றம் அல்லது தீர்ப்பாயத்தின் உத்தரவிற்கும் எதிராக மேல்முறையீடு செய்ய சிறப்பு விடுப்பு வழங்க உச்ச நீதிமன்றத்திற்கு உறுப்பு 136 அதிகாரமளிக்கிறது.",
         ("Art 136 = Special Leave Petition (SLP).", "உறுப்பு 136 = சிறப்பு விடுப்பு மனு (SLP).", "Art 137 = Review of judgments.", "உறுப்பு 137 = தீர்ப்புகளின் சீராய்வு.", "Art 138 = Enlargement of SC jurisdiction.", "உறுப்பு 138 = SC அதிகார வரம்பு விரிவாக்கம்.", "Art 139 = Conferment of writ powers.", "உறுப்பு 139 = பேராணை அதிகாரங்கள் வழங்குதல்."),
         "Confusing Article 136 (SLP) with Article 137 (Review).", "உறுப்பு 136 (SLP) மற்றும் உறுப்பு 137 (Review) ஆகியவற்றை குழப்புவது.", "Special Leave Petition (SLP) = Article 136.", "சிறப்பு விடுப்பு மனு = உறுப்பு 136.", "1"),

        ("POLITY_SC_EASY_034", "Easy",
         "Against decisions of which bodies can Special Leave to Appeal under Article 136 NOT be granted?",
         "எந்த அமைப்பின் முடிவுகளுக்கு எதிராக உறுப்பு 136-ன் கீழ் சிறப்பு விடுப்பு மேல்முறையீடு வழங்கப்பட முடியாது?",
         ("High Courts", "உயர் நீதிமன்றங்கள்", "Courts constituted under any law relating to the Armed Forces (Military Courts/Court Martial)", "ஆயுதப் படைகள் தொடர்பான சட்டத்தின் கீழ் அமைக்கப்பட்ட நீதிமன்றங்கள் (இராணுவ நீதிமன்றங்கள்/கார்ட் மார்ஷியல்)", "Central Administrative Tribunal", "ஒன்றிய நிர்வாகத் தீர்ப்பாயம்", "Industrial Tribunals", "தொழிலாளர் தீர்ப்பாயங்கள்"),
         "B",
         "Article 136(2) explicitly excludes any judgment, determination, sentence or order passed by any court or tribunal constituted by or under any law relating to the Armed Forces.",
         "ஆயுதப் படைகள் தொடர்பான சட்டத்தின் கீழ் அமைக்கப்பட்ட எந்தவொரு நீதிமன்றம் அல்லது தீர்ப்பாயத்தின் முடிவுகளுக்கு உறுப்பு 136 பொருந்தாது என உறுப்பு 136(2) கூறுகிறது.",
         ("High Court decisions can be appealed via SLP.", "உயர் நீதிமன்ற முடிவுகளுக்கு SLP பொருந்தும்.", "Armed Forces Courts/Court Martial are explicitly EXCLUDED under Art 136(2).", "இராணுவ நீதிமன்றங்கள் உறுப்பு 136(2)-ன் கீழ் தெளிவாக விலக்கப்பட்டுள்ளன.", "CAT decisions can be appealed via SLP.", "CAT முடிவுகளுக்கு SLP பொருந்தும்.", "Industrial tribunal decisions can be appealed via SLP.", "தொழிலாளர் தீர்ப்பாய முடிவுகளுக்கு SLP பொருந்தும்."),
         "Assuming Armed Forces tribunal decisions are subject to SLP under Article 136 (they are constitutionally excluded under Art 136(2)).", "இராணுவ நீதிமன்ற முடிவுகளுக்கு SLP பொருந்தும் என நினைப்பது.", "Article 136 SLP Exception = Armed Forces Courts / Court Martial.", "உறுப்பு 136 விலக்கு = இராணுவ நீதிமன்றங்கள் / கார்ட் மார்ஷியல்.", "1"),

        ("POLITY_SC_EASY_035", "Easy",
         "Which Article of the Indian Constitution grants the Supreme Court the power to review any judgment pronounced or order made by it?",
         "தன் சொந்தத் தீர்ப்புகள் அல்லது உத்தரவுகளைச் சீராய்வு செய்யும் அதிகாரத்தை உச்ச நீதிமன்றத்திற்கு வழங்கும் உறுப்பு எது?",
         ("Article 135", "உறுப்பு 135", "Article 136", "உறுப்பு 136", "Article 137", "உறுப்பு 137", "Article 138", "உறுப்பு 138"),
         "C",
         "Article 137 grants the Supreme Court the power to review any judgment pronounced or order made by it, subject to the provisions of any law made by Parliament or rules made under Article 145.",
         "அரசியலமைப்பு உறுப்பு 137 உச்ச நீதிமன்றம் தான் வழங்கிய தீர்ப்பு அல்லது பிறப்பித்த உத்தரவைச் சீராய்வு செய்யும் அதிகாரத்தை அளிக்கிறது.",
         ("Art 135 deals with Federal Court powers.", "உறுப்பு 135 கூட்டாட்சி நீதிமன்ற அதிகாரங்கள்.", "Art 136 deals with SLP.", "உறுப்பு 136 சிறப்பு விடுப்பு மனு.", "Art 137 deals with Review of judgments by SC.", "உறுப்பு 137 உச்ச நீதிமன்ற சீராய்வு அதிகாரம்.", "Art 138 deals with enlargement of SC jurisdiction.", "உறுப்பு 138 அதிகார வரம்பு விரிவாக்கம்."),
         "Confusing Article 137 (Review of judgments) with Article 143 (Advisory jurisdiction).", "உறுப்பு 137 (சீராய்வு) மற்றும் உறுப்பு 143 (ஆலோசனை) ஆகியவற்றை குழப்புவது.", "Review of SC Judgments = Article 137.", "சொந்தத் தீர்ப்பு சீராய்வு = உறுப்பு 137.", "1"),

        ("POLITY_SC_EASY_036", "Easy",
         "Which Article of the Indian Constitution empowers the Supreme Court to pass any decree or order necessary for doing 'complete justice'?",
         "'முழுமையான நீதி' (Complete Justice) வழங்குவதற்குத் தேவையான எந்தவொரு ஆணை அல்லது உத்தரவைப் பிறப்பிக்க உச்ச நீதிமன்றத்திற்கு அதிகாரமளிக்கும் உறுப்பு எது?",
         ("Article 140", "உறுப்பு 140", "Article 141", "உறுப்பு 141", "Article 142", "உறுப்பு 142", "Article 144", "உறுப்பு 144"),
         "C",
         "Article 142(1) empowers the Supreme Court to pass such decree or make such order as is necessary for doing complete justice in any cause or matter pending before it.",
         "தனக்கு முன் நிலுவையில் உள்ள எந்தவொரு வழக்கிலும் முழுமையான நீதி (Complete Justice) வழங்கத் தேவையான ஆணையைப் பிறப்பிக்க உறுப்பு 142(1) உச்ச நீதிமன்றத்திற்கு அதிகாரமளிக்கிறது.",
         ("Art 140 deals with Ancillary powers of SC.", "உறுப்பு 140 துணை அதிகாரங்கள்.", "Art 141 deals with law declared by SC binding on all courts.", "உறுப்பு 141 SC சட்டம் அனைவரையும் கட்டுப்படுத்தும்.", "Art 142 deals with decrees for complete justice.", "உறுப்பு 142 முழுமையான நீதிக்கான ஆணைகள்.", "Art 144 deals with civil and judicial authorities acting in aid of SC.", "உறுப்பு 144 SC-க்கு உதவியாகச் செயல்படும் அதிகாரிகள்."),
         "Confusing Article 142 (Complete Justice) with Article 141 (Binding precedent).", "உறுப்பு 142 (முழுமையான நீதி) மற்றும் உறுப்பு 141 (கட்டாயச் சட்டம்) ஆகியவற்றை குழப்புவது.", "Complete Justice Power = Article 142.", "முழுமையான நீதி அதிகாரம் = உறுப்பு 142.", "1"),

        ("POLITY_SC_EASY_037", "Easy",
         "Which Article declares that the law declared by the Supreme Court shall be binding on all courts within the territory of India?",
         "உச்ச நீதிமன்றத்தால் அறிவிக்கப்படும் சட்டம் இந்தியாவில் உள்ள அனைத்து நீதிமன்றங்களையும் கட்டுப்படுத்தும் என்று கூறும் உறுப்பு எது?",
         ("Article 141", "உறுப்பு 141", "Article 142", "உறுப்பு 142", "Article 143", "உறுப்பு 143", "Article 144", "உறுப்பு 144"),
         "A",
         "Article 141 states that the law declared by the Supreme Court shall be binding on all courts within the territory of India (Principle of Stare Decisis).",
         "அரசியலமைப்பு உறுப்பு 141 உச்ச நீதிமன்றத்தால் அறிவிக்கப்பட்ட சட்டம் இந்தியாவின் அனைத்து நீதிமன்றங்களையும் கட்டுப்படுத்தும் எனக் கூறுகிறது.",
         ("Art 141 = Binding nature of SC law on all courts.", "உறுப்பு 141 = SC சட்டம் அனைத்து நீதிமன்றங்களையும் கட்டுப்படுத்தும்.", "Art 142 = Enforcement of decrees and complete justice.", "உறுப்பு 142 = ஆணைகள் அமலாக்கம் மற்றும் முழுமையான நீதி.", "Art 143 = Advisory jurisdiction.", "உறுப்பு 143 = ஆலோசனை ஆதிக்கம்.", "Art 144 = Civil/judicial authorities aid SC.", "உறுப்பு 144 = சிவில்/நீதித்துறை அதிகாரிகளின் உதவி."),
         "Confusing Article 141 (Law binding on all courts) with Article 142 (Enforcement of orders).", "உறுப்பு 141 மற்றும் உறுப்பு 142-ஐக் குழப்புவது.", "Law binding on all courts = Article 141.", "அனைத்து நீதிமன்றங்களையும் கட்டுப்படுத்தும் சட்டம் = உறுப்பு 141.", "1"),

        ("POLITY_SC_EASY_038", "Easy",
         "Which Article mandates that all authorities, civil and judicial, in the territory of India shall act in aid of the Supreme Court?",
         "இந்திய எல்லைக்குள் உள்ள அனைத்து சிவில் மற்றும் நீதித்துறை அதிகாரிகளும் உச்ச நீதிமன்றத்திற்கு உதவியாகச் செயல்பட வேண்டும் எனக் கூறும் உறுப்பு எது?",
         ("Article 142", "உறுப்பு 142", "Article 143", "உறுப்பு 143", "Article 144", "உறுப்பு 144", "Article 145", "உறுப்பு 145"),
         "C",
         "Article 144 mandates that all authorities, civil and judicial, in the territory of India shall act in aid of the Supreme Court.",
         "அரசியலமைப்பு உறுப்பு 144 இந்தியாவின் எல்லைக்குள் உள்ள அனைத்து சிவில் மற்றும் நீதித்துறை அதிகாரிகளும் உச்ச நீதிமன்றத்திற்கு உதவியாகச் செயல்பட வேண்டும் எனக் கட்டாயமாக்குகிறது.",
         ("Art 142 is Complete justice.", "உறுப்பு 142 முழுமையான நீதி.", "Art 143 is Advisory jurisdiction.", "உறுப்பு 143 ஆலோசனை ஆதிக்கம்.", "Art 144 requires civil & judicial authorities to act in aid of SC.", "உறுப்பு 144 அதிகாரிகள் SC-க்கு உதவியாகச் செயல்பட வேண்டும் என்கிறது.", "Art 145 deals with Rules of Court.", "உறுப்பு 145 நீதிமன்ற விதிகள்."),
         "Confusing Article 144 (Aid to SC) with Article 141 (Binding precedent).", "உறுப்பு 144 மற்றும் உறுப்பு 141-ஐக் குழப்புவது.", "Authorities acting in aid of SC = Article 144.", "SC-க்கு உதவியாகச் செயல்படும் அதிகாரிகள் = உறுப்பு 144.", "1"),

        ("POLITY_SC_EASY_039", "Easy",
         "Who has the power to make Rules of Court for regulating the practice and procedure of the Supreme Court under Article 145?",
         "உறுப்பு 145-ன் கீழ் உச்ச நீதிமன்றத்தின் நடைமுறைகளை ஒழுங்குபடுத்த நீதிமன்ற விதிகளை உருவாக்கும் அதிகாரம் யாருக்கு உள்ளது?",
         ("Supreme Court with the approval of the President", "குடியரசுத் தலைவரின் ஒப்புதலுடன் உச்ச நீதிமன்றம்", "Parliament of India independently", "இந்திய நாடாளுமன்றம் தன்னிச்சையாக", "Union Ministry of Law and Justice", "ஒன்றிய சட்ட அமைச்சகம்", "Bar Council of India", "இந்திய வழக்கறிஞர்கள் கழகம்"),
         "A",
         "Under Article 145, the Supreme Court may from time to time, with the approval of the President, make rules for regulating generally the practice and procedure of the Court.",
         "உறுப்பு 145-ன் கீழ், குடியரசுத் தலைவரின் ஒப்புதலுடன் உச்ச நீதிமன்றம் தனது நடைமுறை விதிகளை அமைத்துக்கொள்ளலாம்.",
         ("Supreme Court makes rules with President's approval.", "குடியரசுத் தலைவர் ஒப்புதலுடன் SC விதிகளை உருவாக்குகிறது.", "Parliament makes laws, but rules under Art 145 are framed by SC with President approval.", "நாடாளுமன்றம் சட்டங்களை இயற்றுகிறது, விதிகளை SC அமைக்கிறது.", "Law Ministry does not frame SC procedural rules.", "சட்ட அமைச்சகம் விதிகளை அமைப்பதில்லை.", "Bar Council frames advocate conduct rules.", "பார் கவுன்சில் வழக்கறிஞர் விதிகளை அமைக்கிறது."),
         "Assuming Parliament directly frames day-to-day SC court procedure rules.", "நாடாளுமன்றமே தினசரி நீதிமன்ற விதிகளை அமைக்கிறது என நினைப்பது.", "SC Court Rules under Art 145 = Framed by Supreme Court with approval of President.", "உறுப்பு 145 நீதிமன்ற விதிகள் = குடியரசுத் தலைவர் ஒப்புதலுடன் உச்ச நீதிமன்றம் உருவாக்குகிறது.", "1"),

        ("POLITY_SC_EASY_040", "Easy",
         "What minimum number of judges must sit on a Constitutional Bench of the Supreme Court to decide a substantial question of law as to constitutional interpretation?",
         "அரசியலமைப்பு விளக்கமளித்தல் குறித்த முக்கிய சட்டக் கேள்வியை விசாரிக்க உச்ச நீதிமன்ற அரசியலமைப்பு அமர்வில் (Constitution Bench) குறைந்தது எத்தனை நீதிபதிகள் இருக்க வேண்டும்?",
         ("3 Judges", "3 நீதிபதிகள்", "5 Judges", "5 நீதிபதிகள்", "7 Judges", "7 நீதிபதிகள்", "9 Judges", "9 நீதிபதிகள்"),
         "B",
         "Article 145(3) specifies that the minimum number of Judges who are to sit for deciding any case involving a substantial question of law as to interpretation of the Constitution shall be FIVE.",
         "அரசியலமைப்பு விளக்கமளித்தல் குறித்த முக்கிய சட்டக் கேள்வியை விசாரிக்க அமைக்கப்படும் அரசியலமைப்பு அமர்வில் குறைந்தபட்சம் 5 நீதிபதிகள் இருக்க வேண்டும் என உறுப்பு 145(3) கூறுகிறது.",
         ("3 judges forms a Division Bench.", "3 நீதிபதிகள் பிரிவு அமர்வு (Division Bench).", "5 judges is the minimum constitutional requirement under Article 145(3) for a Constitution Bench.", "5 நீதிபதிகள் என்பது உறுப்பு 145(3)-ன் கீழ் அரசியலமைப்பு அமர்வுக்கான குறைந்தபட்ச எண்ணிக்கை.", "7 judges is a larger Constitution Bench.", "7 நீதிபதிகள் பெரிய அரசியலமைப்பு அமர்வு.", "9 judges is a larger Constitution Bench.", "9 நீதிபதிகள் பெரிய அரசியலமைப்பு அமர்வு."),
         "Confusing Division Bench minimum (3 judges) with Constitution Bench minimum (5 judges).", "பிரிவு அமர்வு (3) மற்றும் அரசியலமைப்பு அமர்வு (5) குறைந்தபட்ச எண்ணிக்கையைக் குழப்புவது.", "Constitution Bench Minimum Strength = 5 Judges (Article 145(3)).", "அரசியலமைப்பு அமர்வு குறைந்தபட்சம் = 5 நீதிபதிகள் (உறுப்பு 145(3)).", "1"),

        ("POLITY_SC_EASY_041", "Easy",
         "Salaries, allowances, and pensions of Supreme Court judges and administrative expenses of the Supreme Court are charged upon which fund?",
         "உச்ச நீதிமன்ற நீதிபதிகளின் ஊதியம், படிகள், ஓய்வூதியம் மற்றும் நிர்வாகச் செலவுகள் எந்த நிதியிலிருந்து வழங்கப்படுகின்றன?",
         ("Contingency Fund of India", "இந்திய அவசரகால நிதி", "Consolidated Fund of India", "இந்தியத் தொகுப்பு நிதி", "Public Account of India", "இந்தியப் பொதுக் கணக்கு", "PM National Relief Fund", "பிரதமரின் தேசிய நிவாரண நிதி"),
         "B",
         "Under Article 146(3), administrative expenses of SC including all salaries, allowances and pensions payable to judges and staff are charged upon the Consolidated Fund of India.",
         "அரசியலமைப்பு உறுப்பு 146(3)-ன் படி, உச்ச நீதிமன்ற நீதிபதிகள் மற்றும் ஊழியர்களின் ஊதியம், ஓய்வூதியம் உள்ளிட்ட நிர்வாகச் செலவுகள் இந்தியத் தொகுப்பு நிதியில் (Consolidated Fund of India) சுமத்தப்படுகின்றன.",
         ("Contingency Fund is for unforeseen emergency expenditure.", "அவசரகால நிதி எதிர்பாராத செலவுகளுக்கானது.", "Consolidated Fund of India pays SC salaries and expenses.", "இந்தியத் தொகுப்பு நிதி SC ஊதியம் மற்றும் செலவுகளை அளிக்கிறது.", "Public Account is for public deposits and provident funds.", "பொதுக் கணக்கு பொது வைப்புகளுக்கானது.", "PM Relief Fund is a charitable fund.", "நிவாரண நிதி ஒரு தொண்டு நிதி."),
         "Confusing Consolidated Fund of India with Contingency Fund of India.", "தொகுப்பு நிதி மற்றும் அவசரகால நிதியைக் குழப்புவது.", "SC Expenses & Judge Salaries = Charged upon Consolidated Fund of India.", "SC செலவுகள் & ஊதியம் = இந்தியத் தொகுப்பு நிதியில் சுமத்தப்படுபவை.", "1"),

        ("POLITY_SC_EASY_042", "Easy",
         "Can the salaries and allowances of Supreme Court judges be varied to their disadvantage after their appointment?",
         "உச்ச நீதிமன்ற நீதிபதிகள் நியமிக்கப்பட்ட பிறகு அவர்களின் ஊதியம் மற்றும் படிகள் அவர்களுக்கு பாதகமாக மாற்றப்பட முடியுமா?",
         ("Yes, at any time by Executive order", "ஆம், எப்போது வேண்டுமானாலும் நிர்வாக ஆணை மூலம்", "No, except during a Financial Emergency declared under Article 360", "இல்லை, உறுப்பு 360-ன் கீழ் நிதி அவசரநிலை பிரகடனப்படுத்தப்படும் போது தவிர", "Yes, whenever Parliament passes a simple resolution", "ஆம், நாடாளுமன்றம் சாதாரண தீர்மானம் நிறைவேற்றும் போதெல்லாம்", "Yes, upon recommendation of Union Finance Ministry", "ஆம், ஒன்றிய நிதி அமைச்சகத்தின் பரிந்துரையின் பேரில்"),
         "B",
         "Under Article 125(2), conditions of service cannot be varied to a judge's disadvantage after appointment, EXCEPT during a Financial Emergency under Article 360.",
         "உறுப்பு 125(2)-ன் படி, ஒரு நீதிபதி நியமிக்கப்பட்ட பிறகு அவரது பணி நிபந்தனைகள் பாதகமாக மாற்றப்பட முடியாது; ஆனால் உறுப்பு 360 நிதி அவசரநிலையின் போது மட்டுமே இதிலிருந்து விலக்கு உண்டு.",
         ("Executive order cannot vary salary to disadvantage.", "நிர்வாக ஆணை ஊதியத்தைக் குறைக்க முடியாது.", "Cannot be varied to disadvantage EXCEPT during Article 360 Financial Emergency.", "உறுப்பு 360 நிதி அவசரநிலையின் போது தவிர பாதகமாக மாற்ற முடியாது.", "Simple resolution cannot vary salary.", "சாதாரண தீர்மானம் ஊதியத்தைக் குறைக்க முடியாது.", "Finance Ministry recommendation has no power to reduce judge salary.", "நிதி அமைச்சகப் பரிந்துரைக்கு அதிகாரமில்லை."),
         "Thinking judge salaries can never be reduced under any circumstances (they CAN be reduced during Financial Emergency Art 360).", "எந்தச் சூழ்நிலையிலும் ஊதியத்தைக் குறைக்க முடியாது என நினைப்பது (நிதி அவசரநிலையின் போது குறைக்கலாம்).", "Salary Disadvantage Variation = PROHIBITED, except during Financial Emergency (Art 360).", "ஊதியக் குறைப்பு = தடை செய்யப்பட்டுள்ளது (நிதி அவசரநிலை உறுப்பு 360 தவிர).", "1"),

        ("POLITY_SC_EASY_043", "Easy",
         "What is the restriction placed on a retired Supreme Court judge regarding legal practice after retirement under Article 124(7)?",
         "உறுப்பு 124(7)-ன் படி, ஓய்வு பெற்ற உச்ச நீதிமன்ற நீதிபதி வழக்கறிஞர் தொழில் செய்வதற்கு விதிக்கப்பட்ட கட்டுப்பாடு என்ன?",
         ("He can practice in any High Court in India", "அவர் இந்தியாவில் உள்ள எந்த உயர் நீதிமன்றத்திலும் வழக்கறிஞராகப் பணியாற்றலாம்", "He cannot plead or act in any court or before any authority within the territory of India", "அவர் இந்தியாவில் உள்ள எந்தவொரு நீதிமன்றத்திலும் அல்லது அதிகார அமைப்பின் முன்னும் வழக்காடவோ பணியாற்றவோ முடியாது", "He can practice only in trial courts", "அவர் கீழ் நீதிமன்றங்களில் மட்டுமே பணியாற்றலாம்", "He can practice provided he gets Law Ministry permission", "சட்ட அமைச்சக அனுமதி பெற்றால் பணியாற்றலாம்"),
         "B",
         "Article 124(7) mandates that no person who has held office as a Judge of the Supreme Court shall plead or act in any court or before any authority within the territory of India.",
         "உறுப்பு 124(7)-ன் படி, உச்ச நீதிமன்ற நீதிபதியாகப் பணியாற்றிய ஒருவர் இந்தியாவில் உள்ள எந்தவொரு நீதிமன்றத்திலும் அல்லது அதிகார அமைப்பின் முன்னும் வழக்காடவோ பணியாற்றவோ முடியாது.",
         ("HC practice is barred for retired SC judges.", "உயர் நீதிமன்றப் பணியும் தடை செய்யப்பட்டுள்ளது.", "Absolute bar on pleading or acting in ANY court/authority in India.", "இந்தியாவில் உள்ள அனைத்து நீதிமன்றங்களிலும் வழக்காட முழுமையான தடை.", "Trial court practice is strictly barred.", "கீழ் நீதிமன்றப் பணியும் தடை செய்யப்பட்டுள்ளது.", "Law Ministry permission cannot override Art 124(7).", "சட்ட அமைச்சக அனுமதி இதை மாற்ற முடியாது."),
         "Confusing High Court judge post-retirement practice rules (can practice in SC and other HCs) with Supreme Court judge rules (barred from ALL courts in India).", "உயர் நீதிமன்ற மற்றும் உச்ச நீதிமன்ற நீதிபதிகளின் ஓய்வுக்குப் பிந்தைய வழக்கறிஞர் தொழில் விதிகளைக் குழப்புவது.", "Retired SC Judge = Complete bar from practicing in ANY court or authority in India (Art 124(7)).", "ஓய்வு பெற்ற SC நீதிபதி = இந்தியாவில் உள்ள எந்த நீதிமன்றத்திலும் பணியாற்ற முழுத் தடை.", "1"),

        ("POLITY_SC_EASY_044", "Easy",
         "Who was the first Chief Justice of India after independence?",
         "சுதந்திர இந்தியாவிற்குப் பின் இந்தியாவின் முதல் தலைமை நீதிபதி யார்?",
         ("M. Patanjali Sastri", "எம். பதஞ்சலி சாஸ்திரி", "H. J. Kania", "எச். ஜே. கானியா", "Mehr Chand Mahajan", "மெஹர் சந்த் மகாஜன்", "B. K. Mukherjea", "பி. கே. முகர்ஜி"),
         "B",
         "Sir Harilal Jekisundas Kania (H. J. Kania) was the first Chief Justice of India, serving from 1950 until his death in 1951.",
         "சர் ஹரிலால் ஜெகிசுந்தாஸ் கானியா (H. J. Kania) 1950 முதல் 1951-ல் இறக்கும் வரை சுதந்திர இந்தியாவின் முதல் தலைமை நீதிபதியாகப் பணியாற்றினார்.",
         ("M. Patanjali Sastri was the 2nd CJI.", "எம். பதஞ்சலி சாஸ்திரி 2-வது CJI.", "H. J. Kania was the FIRST CJI of independent India.", "எச். ஜே. கானியா சுதந்திர இந்தியாவின் முதல் CJI.", "Mehr Chand Mahajan was the 3rd CJI.", "மெஹர் சந்த் மகாஜன் 3-வது CJI.", "B. K. Mukherjea was the 4th CJI.", "பி. கே. முகர்ஜி 4-வது CJI."),
         "Confusing the 1st CJI (H. J. Kania) with 2nd CJI (M. Patanjali Sastri).", "முதல் CJI மற்றும் 2-வது CJI-யைக் குழப்புவது.", "First Chief Justice of India = H. J. Kania.", "இந்தியாவின் முதல் தலைமை நீதிபதி = எச். ஜே. கானியா.", "1"),

        ("POLITY_SC_EASY_045", "Easy",
         "Who was the first female Judge appointed to the Supreme Court of India?",
         "இந்திய உச்ச நீதிமன்றத்தின் முதல் பெண் நீதிபதியாக நியமிக்கப்பட்டவர் யார்?",
         ("Justice Anna Chandy", "நீதிபதி அன்னா சாண்டி", "Justice M. Fathima Beevi", "நீதிபதி எம். பாத்திமா பீவி", "Justice Sujata Manohar", "நீதிபதி சுஜாதா மனோகர்", "Justice Ruma Pal", "நீதிபதி ரூமா பால்"),
         "B",
         "Justice M. Fathima Beevi was appointed as the first female judge of the Supreme Court of India in 1989.",
         "1989-ல் நீதிபதி எம். பாத்திமா பீவி இந்திய உச்ச நீதிமன்றத்தின் முதல் பெண் நீதிபதியாக நியமிக்கப்பட்டார்.",
         ("Anna Chandy was the first female HIGH COURT judge in India (Kerala HC).", "அன்னா சாண்டி இந்தியாவின் முதல் பெண் உயர் நீதிமன்ற நீதிபதி.", "M. Fathima Beevi was the first female SUPREME COURT judge (1989).", "எம். பாத்திமா பீவி முதல் பெண் உச்ச நீதிமன்ற நீதிபதி (1989).", "Sujata Manohar was the 2nd female SC judge.", "சுஜாதா மனோகர் 2-வது பெண் SC நீதிபதி.", "Ruma Pal was a senior female SC judge later.", "ரூமா பால் பின்னாளைய மூத்த பெண் SC நீதிபதி."),
         "Confusing first High Court female judge (Anna Chandy) with first Supreme Court female judge (M. Fathima Beevi).", "முதல் உயர் நீதிமன்ற பெண் நீதிபதி (அன்னா சாண்டி) மற்றும் முதல் உச்ச நீதிமன்ற பெண் நீதிபதியை (பாத்திமா பீவி) குழப்புவது.", "First Female SC Judge = M. Fathima Beevi (1989). First Female HC Judge = Anna Chandy.", "முதல் பெண் SC நீதிபதி = எம். பாத்திமா பீவி. முதல் பெண் HC நீதிபதி = அன்னா சாண்டி.", "1"),

        ("POLITY_SC_EASY_046", "Easy",
         "Who appoints the officers and servants of the Supreme Court under Article 146?",
         "அரசியலமைப்பு உறுப்பு 146-ன் கீழ் உச்ச நீதிமன்றத்தின் அதிகாரிகள் மற்றும் ஊழியர்களை நியமிப்பவர் யார்?",
         ("Chief Justice of India (or such other judge/officer as CJI directs)", "இந்தியத் தலைமை நீதிபதி (அல்லது CJI வழிகாட்டும் பிற நீதிபதி/அதிகாரி)", "Union Public Service Commission (UPSC) exclusively", "UPSC மட்டுமே", "President of India directly", "இந்தியக் குடியரசுத் தலைவர் நேரடியாக", "Union Law Ministry", "ஒன்றிய சட்ட அமைச்சகம்"),
         "A",
         "Under Article 146(1), appointments of officers and servants of the Supreme Court shall be made by the Chief Justice of India or such other judge or officer of the Court as he may direct.",
         "உறுப்பு 146(1)-ன் படி, உச்ச நீதிமன்ற அதிகாரிகளும் ஊழியர்களும் இந்தியத் தலைமை நீதிபதி அல்லது அவரால் பணிக்கப்பட்ட நீதிபதி/அதிகாரியால் நியமிக்கப்படுகிறார்கள்.",
         ("CJI or his delegate appoints SC officers and servants.", "CJI அல்லது அவரது பிரதிநிதி SC ஊழியர்களை நியமிக்கிறார்.", "UPSC does not recruit SC staff directly unless specified by rule.", "UPSC நேரடியாக ஆள்சேர்ப்பு செய்வதில்லை.", "President does not appoint administrative staff of SC.", "குடியரசுத் தலைவர் நிர்வாக ஊழியர்களை நியமிப்பதில்லை.", "Law Ministry has no direct recruitment authority for SC staff.", "சட்ட அமைச்சகத்திற்கு இதில் நியமன அதிகாரமில்லை."),
         "Assuming UPSC conducts all recruitment for Supreme Court staff (CJI has administrative independence under Art 146).", "UPSC தான் அனைத்து SC ஊழியர்களையும் தேர்வு செய்கிறது என நினைப்பது.", "SC Staff Appointment Authority = Chief Justice of India (Art 146).", "SC ஊழியர்கள் நியமன அதிகாரி = இந்தியத் தலைமை நீதிபதி (உறுப்பு 146).", "1"),

        ("POLITY_SC_EASY_047", "Easy",
         "Under Article 139A, who can transfer cases pending before High Courts involving the same or substantially the same questions of law to the Supreme Court?",
         "ஒரே மாதிரி சட்டக் கேள்விகளைக் கொண்ட உயர் நீதிமன்ற வழக்குகளைத் தனக்கு மாற்றிக்கொள்ளும் அதிகாரம் உறுப்பு 139A-ன் கீழ் யாருக்கு உள்ளது?",
         ("Supreme Court (on application by Attorney General or party)", "உச்ச நீதிமன்றம் (அட்டர்னி ஜெனரல் அல்லது தரப்பினரின் மனு பேரில்)", "President of India", "இந்தியக் குடியரசுத் தலைவர்", "Union Law Minister", "ஒன்றிய சட்ட அமைச்சர்", "Parliament by resolution", "நாடாளுமன்ற தீர்மானம்"),
         "A",
         "Article 139A empowers the Supreme Court to withdraw cases involving the same question of law pending before High Courts and dispose of them itself.",
         "உறுப்பு 139A ஒரே மாதிரியான சட்டக் கேள்விகள் நிலுவையில் உள்ள உயர் நீதிமன்ற வழக்குகளைத் தனக்கு மாற்றி விசாரணை செய்ய உச்ச நீதிமன்றத்திற்கு அதிகாரமளிக்கிறது.",
         ("Supreme Court can withdraw/transfer cases under Art 139A.", "SC வழக்குகளைத் தனக்கு மாற்றி விசாரிக்கலாம்.", "President has no case transfer authority.", "குடியரசுத் தலைவருக்கு மாற்றும் அதிகாரமில்லை.", "Law Minister has no case transfer power.", "சட்ட அமைச்சருக்கு அதிகாரமில்லை.", "Parliament resolution is not needed for judicial case transfer.", "நாடாளுமன்ற தீர்மானம் தேவையில்லை."),
         "Confusing administrative case transfer with constitutional withdrawal under Article 139A.", "வழக்குகளை மாற்றும் அரசியலமைப்பு அதிகாரத்தைக் குழப்புவது.", "Transfer of Cases = Supreme Court under Article 139A.", "வழக்குகள் மாற்றம் = உறுப்பு 139A-ன் கீழ் உச்ச நீதிமன்றம்.", "1"),

        ("POLITY_SC_EASY_048", "Easy",
         "Which Article of the Indian Constitution defines the jurisdiction of the Supreme Court regarding criminal appeals?",
         "குற்றவியல் மேல்முறையீடுகள் தொடர்பாக உச்ச நீதிமன்றத்தின் அதிகார வரம்பை வரையறுக்கும் அரசியலமைப்பு உறுப்பு எது?",
         ("Article 132", "உறுப்பு 132", "Article 133", "உறுப்பு 133", "Article 134", "உறுப்பு 134", "Article 135", "உறுப்பு 135"),
         "C",
         "Article 134 deals with the Appellate Jurisdiction of the Supreme Court in regard to criminal matters.",
         "அரசியலமைப்பு உறுப்பு 134 குற்றவியல் விவகாரங்களில் உச்ச நீதிமன்றத்தின் மேல்முறையீட்டு அதிகார வரம்பைக் கையாள்கிறது.",
         ("Art 132 = Constitutional appeals.", "உறுப்பு 132 = அரசியலமைப்பு மேல்முறையீடுகள்.", "Art 133 = Civil appeals.", "உறுப்பு 133 = சிவில் மேல்முறையீடுகள்.", "Art 134 = Criminal appeals.", "உறுப்பு 134 = குற்றவியல் மேல்முறையீடுகள்.", "Art 135 = Federal Court jurisdiction continuance.", "உறுப்பு 135 = கூட்டாட்சி நீதிமன்ற அதிகாரம் தொடர்தல்."),
         "Confusing Article 133 (Civil appeals) with Article 134 (Criminal appeals).", "உறுப்பு 133 (சிவில்) மற்றும் உறுப்பு 134 (குற்றவியல்) ஆகியவற்றை குழப்புவது.", "Criminal Appellate Jurisdiction = Article 134.", "குற்றவியல் மேல்முறையீட்டு ஆதிக்கம் = உறுப்பு 134.", "1"),

        ("POLITY_SC_EASY_049", "Easy",
         "Which Article defines the jurisdiction of the Supreme Court in appeals from High Courts regarding civil matters?",
         "சிவில் விவகாரங்களில் உயர் நீதிமன்ற தீர்ப்புகளுக்கு எதிரான மேல்முறையீட்டு அதிகார வரம்பைக் கூறும் உறுப்பு எது?",
         ("Article 131", "உறுப்பு 131", "Article 132", "உறுப்பு 132", "Article 133", "உறுப்பு 133", "Article 134", "உறுப்பு 134"),
         "C",
         "Article 133 provides for Appellate Jurisdiction of the Supreme Court in appeals from High Courts in regard to civil matters.",
         "சிவில் விவகாரங்களில் உயர் நீதிமன்றங்களின் தீர்ப்புகளுக்கு எதிராக உச்ச நீதிமன்றத்தில் மேல்முறையீடு செய்யும் அதிகாரத்தை உறுப்பு 133 அளிக்கிறது.",
         ("Art 131 = Original Jurisdiction.", "உறுப்பு 131 = மூல ஆதிக்கம்.", "Art 132 = Constitutional appeals.", "உறுப்பு 132 = அரசியலமைப்பு மேல்முறையீடுகள்.", "Art 133 = Civil Appellate Jurisdiction.", "உறுப்பு 133 = சிவில் மேல்முறையீட்டு ஆதிக்கம்.", "Art 134 = Criminal Appellate Jurisdiction.", "உறுப்பு 134 = குற்றவியல் மேல்முறையீட்டு ஆதிக்கம்."),
         "Confusing Article 132 (Constitutional matters) with Article 133 (Civil matters).", "உறுப்பு 132 மற்றும் உறுப்பு 133-ஐக் குழப்புவது.", "Civil Appellate Jurisdiction = Article 133.", "சிவில் மேல்முறையீட்டு ஆதிக்கம் = உறுப்பு 133.", "1"),

        ("POLITY_SC_EASY_050", "Easy",
         "Who was the longest-serving Chief Justice of India in history?",
         "இந்திய வரலாற்றில் மிக நீண்ட காலம் தலைமை நீதிபதியாகப் பணியாற்றியவர் யார்?",
         ("Justice A. N. Ray", "நீதிபதி ஏ. என். ராய்", "Justice Y. V. Chandrachud", "நீதிபதி ஒய். வி. சந்திரசூட்", "Justice P. N. Bhagwati", "நீதிபதி பி. என். பகவதி", "Justice M. Hidayatullah", "நீதிபதி எம். ஹிதாயத்துல்லா"),
         "B",
         "Justice Yeshwant Vishnu Chandrachud (Y. V. Chandrachud) served as the 16th Chief Justice of India for over 7 years (1978 to 1985), making him the longest-serving CJI.",
         "நீதிபதி யஷ்வந்த் விஷ்ணு சந்திரசூட் (Y. V. Chandrachud) 7 ஆண்டுகளுக்கும் மேலாக (1978 முதல் 1985 வரை) 16-வது தலைமை நீதிபதியாகப் பணியாற்றினார்; இவரே மிக நீண்ட காலம் பணியாற்றிய CJI ஆவார்.",
         ("A. N. Ray served from 1973 to 1977.", "ஏ. என். ராய் 1973-1977 வரை பணியாற்றினார்.", "Y. V. Chandrachud served longest (7 years 4 months, 1978–1985).", "ஒய். வி. சந்திரசூட் மிக நீண்ட காலம் பணியாற்றினார் (7 ஆண்டுகள் 4 மாதங்கள்).", "P. N. Bhagwati served for around 1.5 years.", "பி. என். பகவதி 1.5 ஆண்டுகள் பணியாற்றினார்.", "M. Hidayatullah served for around 2.5 years.", "எம். ஹிதாயத்துல்லா 2.5 ஆண்டுகள் பணியாற்றினார்."),
         "Confusing Y. V. Chandrachud (longest serving CJI - 7+ yrs) with K. N. Singh (shortest serving CJI - 17 days).", "மிக நீண்ட காலம் பணியாற்றியவர் (ஒய்.வி. சந்திரசூட்) மற்றும் குறைந்த காலம் பணியாற்றியவரைக் (கே.என். சிங்) குழப்புவது.", "Longest Serving CJI = Justice Y. V. Chandrachud (7 years, 4 months).", "மிக நீண்ட காலம் பணியாற்றிய CJI = நீதிபதி ஒய். வி. சந்திரசூட் (7 ஆண்டுகள், 4 மாதங்கள்).", "1")
    ]

    easy = []
    for idx, item in enumerate(easy_data):
        qid, diff, s_en, s_ta, opts, corr, exp_en, exp_ta, why_args, trap_en, trap_ta, tip_en, tip_ta, sp = item
        if len(opts) != 8:
            print(f"FAILED AT INDEX {idx}: QID={qid}, len(opts)={len(opts)}")
        options = make_options(*opts)
        why_not = make_why_not(corr, *why_args)
        easy.append(build_q(qid, diff, s_en, s_ta, options, corr, exp_en, exp_ta, why_not, trap_en, trap_ta, tip_en, tip_ta, sp))
    return easy

def main():
    easy_qs = get_easy_questions()
    print(f"Generated Easy Questions: {len(easy_qs)}")
    assert len(easy_qs) == 50, f"Expected 50, got {len(easy_qs)}"
    
    out_path = "data/questions/polity/supreme_court_easy.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(easy_qs, f, ensure_ascii=False, indent=2)
    print(f"Saved -> {out_path}")

if __name__ == "__main__":
    main()
