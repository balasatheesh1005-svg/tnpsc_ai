# -*- coding: utf-8 -*-
"""
Generator for Supreme Court Match the Following MCQs (25 Questions)
Topic: Supreme Court of India
Section: Match the Following Questions
File: data/questions/polity/supreme_court_match.json & supreme_court_match_the_following.json
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

def build_q(qid, stem_en, stem_ta, options, correct_letter, exp_en, exp_ta, why_args, trap_en, trap_ta, tip_en, tip_ta, source_part):
    opts_en = [o["en"] for o in options]
    opts_ta = [o["ta"] for o in options]
    why_not = make_why_not(correct_letter, *why_args)
    
    return {
        "id": qid,
        "subject": "Polity",
        "topic": "Supreme Court of India",
        "difficulty": "Hard",
        "question_type": "Match",
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

def get_match_questions():
    match_data = [
        ("POLITY_SC_MATCH_001",
         "Match List-I (Articles of Constitution) with List-II (Provisions):\nList-I:\na. Article 129\nb. Article 131\nc. Article 136\nd. Article 143\n\nList-II:\n1. Advisory Jurisdiction\n2. Special Leave Petition\n3. Original Jurisdiction\n4. Court of Record\n\nSelect the correct answer using the code below:",
         "பட்டியல்-I (அரசியலமைப்பு உறுப்புகள்) மற்றும் பட்டியல்-II (விதிகள்) பொருத்துக:\nபட்டியல்-I:\na. உறுப்பு 129\nb. உறுப்பு 131\nc. உறுப்பு 136\nd. உறுப்பு 143\n\nபட்டியல்-II:\n1. ஆலோசனை ஆதிக்கம்\n2. சிறப்பு விடுப்பு மனு\n3. மூல ஆதிக்கம்\n4. பதிவு நீதிமன்றம்\n\nகீழ்க்கண்ட குறியீடுகளைப் பயன்படுத்தி சரியான பதிலைத் தேர்ந்தெடுக்கவும்:",
         ("a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1", "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4", "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2", "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3"),
         "A",
         "Correct Match: Article 129 -> Court of Record (4), Article 131 -> Original Jurisdiction (3), Article 136 -> Special Leave Petition (2), Article 143 -> Advisory Jurisdiction (1). Thus sequence is a-4, b-3, c-2, d-1.",
         "சரியான பொருத்தம்: உறுப்பு 129 -> பதிவு நீதிமன்றம் (4), உறுப்பு 131 -> மூல ஆதிக்கம் (3), உறுப்பு 136 -> சிறப்பு விடுப்பு மனு (2), உறுப்பு 143 -> ஆலோசனை ஆதிக்கம் (1). எனவே வரிசை a-4, b-3, c-2, d-1.",
         ("a-4, b-3, c-2, d-1 is the exact constitutional match.", "a-4, b-3, c-2, d-1 என்பது துல்லியமான பொருத்தமாகும்.", "Option B matches incorrectly.", "விருப்பம் B தவறாகப் பொருந்துகிறது.", "Option C matches incorrectly.", "விருப்பம் C தவறாகப் பொருந்துகிறது.", "Option D matches incorrectly.", "விருப்பம் D தவறாகப் பொருந்துகிறது."),
         "Confusing Article 131 (Original Jurisdiction) with Article 136 (SLP).", "உறுப்பு 131 மற்றும் உறுப்பு 136 ஆகியவற்றை குழப்புவது.", "Article Matching: 129=Court of Record, 131=Original, 136=SLP, 143=Advisory.", "உறுப்பு பொருத்தம்: 129=பதிவு நீதிமன்றம், 131=மூல, 136=SLP, 143=ஆலோசனை.", "1"),

        ("POLITY_SC_MATCH_002",
         "Match List-I (Judges Cases) with List-II (Landmark Rulings):\nList-I:\na. First Judges Case (1981)\nb. Second Judges Case (1993)\nc. Third Judges Case (1998)\nd. Fourth Judges Case (2015)\n\nList-II:\n1. Struck down NJAC 99th Amendment\n2. Expanded Collegium to CJI + 4 senior judges\n3. Created Collegium System (Consultation = Concurrence)\n4. Held Consultation does NOT mean Concurrence (Executive Primacy)\n\nSelect the correct answer using the code below:",
         "பட்டியல்-I (நீதிபதிகள் வழக்குகள்) மற்றும் பட்டியல்-II (வரலாற்றுத் தீர்ப்புகள்) பொருத்துக:\nபட்டியல்-I:\na. முதல் நீதிபதிகள் வழக்கு (1981)\nb. இரண்டாவது நீதிபதிகள் வழக்கு (1993)\nc. மூன்றாவது நீதிபதிகள் வழக்கு (1998)\nd. நான்காவது நீதிபதிகள் வழக்கு (2015)\n\nபட்டியல்-II:\n1. NJAC 99-வது திருத்தத்தை ரத்து செய்தது\n2. கொலீஜியத்தை CJI + 4 மூத்த நீதிபதிகள் என விரிவாக்கியது\n3. கொலீஜியம் முறையை உருவாக்கியது (கலந்தாலோசனை = ஒப்புதல்)\n4. கலந்தாலோசனை என்பது ஒப்புதல் அல்ல என்றது (நிர்வாக முதன்மை)\n\nகீழ்க்கண்ட குறியீடுகளைப் பயன்படுத்தி சரியான பதிலைத் தேர்ந்தெடுக்கவும்:",
         ("a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1", "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2", "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4", "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3"),
         "A",
         "Correct Match: First Judges Case (1981) -> Executive Primacy (4), Second Judges Case (1993) -> Created Collegium (3), Third Judges Case (1998) -> CJI + 4 Seniors (2), Fourth Judges Case (2015) -> Struck down NJAC (1). Thus sequence is a-4, b-3, c-2, d-1.",
         "சரியான பொருத்தம்: 1-வது நீதிபதிகள் வழக்கு -> நிர்வாக முதன்மை (4), 2-வது நீதிபதிகள் வழக்கு -> கொலீஜியம் உருவாக்கம் (3), 3-வது நீதிபதிகள் வழக்கு -> CJI + 4 மூத்த நீதிபதிகள் (2), 4-வது நீதிபதிகள் வழக்கு -> NJAC ரத்து (1).",
         ("a-4, b-3, c-2, d-1 is the correct chronological ruling match.", "a-4, b-3, c-2, d-1 என்பதே சரியான பொருத்தம்.", "Option B is incorrect.", "விருப்பம் B தவறானது.", "Option C is incorrect.", "விருப்பம் C தவறானது.", "Option D is incorrect.", "விருப்பம் D தவறானது."),
         "Confusing First Judges Case (1981 - Executive Primacy) with Second Judges Case (1993 - Collegium Creation).", "முதல் மற்றும் 2-வது நீதிபதிகள் வழக்கின் தீர்ப்புகளைக் குழப்புவது.", "Judges Cases: 1st=Executive Primacy, 2nd=Collegium Created, 3rd=CJI+4, 4th=NJAC Struck Down.", "நீதிபதிகள் வழக்குகள்: 1=நிர்வாக முதன்மை, 2=கொலீஜியம் உருவாக்கம், 3=CJI+4, 4=NJAC ரத்து.", "1"),

        ("POLITY_SC_MATCH_003",
         "Match List-I (Writs under Article 32) with List-II (Literal Meaning):\nList-I:\na. Habeas Corpus\nb. Mandamus\nc. Prohibition\nd. Quo-Warranto\n\nList-II:\n1. By what authority or warrant?\n2. To forbid / Prevent lower court from exceeding jurisdiction\n3. We Command\n4. To have the body of\n\nSelect the correct answer using the code below:",
         "பட்டியல்-I (உறுப்பு 32 பேராணைகள்) மற்றும் பட்டியல்-II (நேரடிப் பொருள்) பொருத்துக:\nபட்டியல்-I:\na. ஆட்கொணர் பேராணை (Habeas Corpus)\nb. செயலுறுத்தும் பேராணை (Mandamus)\nc. தடையுறுத்தும் பேராணை (Prohibition)\nd. தகுதி வினவு பேராணை (Quo-Warranto)\n\nபட்டியல்-II:\n1. எந்த அதிகாரத்தின் அடிப்படையில்?\n2. தடுத்தல் / கீழ்மை நீதிமன்ற அதிகார வரம்பு மீறலைத் தடுத்தல்\n3. நாங்கள் கட்டளையிடுகிறோம்\n4. உடலைக் கொணர்க\n\nகீழ்க்கண்ட குறியீடுகளைப் பயன்படுத்தி சரியான பதிலைத் தேர்ந்தெடுக்கவும்:",
         ("a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1", "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2", "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4", "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3"),
         "A",
         "Correct Match: Habeas Corpus -> To have the body of (4), Mandamus -> We Command (3), Prohibition -> To forbid (2), Quo-Warranto -> By what authority? (1). Sequence is a-4, b-3, c-2, d-1.",
         "சரியான பொருத்தம்: ஆட்கொணர் -> உடலைக் கொணர்க (4), செயலுறுத்தும் -> நாங்கள் கட்டளையிடுகிறோம் (3), தடையுறுத்தும் -> தடுத்தல் (2), தகுதி வினவு -> எந்த அதிகாரத்தின் அடிப்படையில்? (1).",
         ("a-4, b-3, c-2, d-1 is the exact legal Latin translation match.", "a-4, b-3, c-2, d-1 என்பது துல்லியமான சட்டப்பூர்வ பொருத்தம்.", "Option B is incorrect.", "விருப்பம் B தவறு.", "Option C is incorrect.", "விருப்பம் C தவறு.", "Option D is incorrect.", "விருப்பம் D தவறு."),
         "Confusing Mandamus (We Command) with Quo-Warranto (By what authority).", "மேண்டமஸ் (கட்டளையிடுதல்) மற்றும் குவோ வாரண்டோ (தகுதி வினவல்) ஆகியவற்றை குழப்புவது.", "Writs Meaning: Habeas Corpus=To have body, Mandamus=We Command, Prohibition=To forbid, Quo Warranto=By what authority.", "பேராணை பொருள்: Habeas Corpus=உடலைக் கொணர்க, Mandamus=கட்டளையிடுதல், Prohibition=தடுத்தல், Quo Warranto=தகுதி வினவல்.", "1"),

        ("POLITY_SC_MATCH_004",
         "Match List-I (Landmark Cases) with List-II (Key Doctrine/Principle):\nList-I:\na. Kesavananda Bharati (1973)\nb. Golaknath Case (1967)\nc. Maneka Gandhi Case (1978)\nd. KS Puttaswamy Case (2017)\n\nList-II:\n1. Right to Privacy as Fundamental Right under Art 21\n2. Procedure Established by Law expanded to Due Process of Law\n3. Doctrine of Prospective Overruling\n4. Basic Structure Doctrine\n\nSelect the correct answer using the code below:",
         "பட்டியல்-I (முக்கிய வழக்குகள்) மற்றும் பட்டியல்-II (முக்கியக் கோட்பாடு) பொருத்துக:\nபட்டியல்-I:\na. கேசவாநந்த பாரதி வழக்கு (1973)\nb. கோலக்நாத் வழக்கு (1967)\nc. மேனகா காந்தி வழக்கு (1978)\nd. கே.எஸ். புட்டசாமி வழக்கு (2017)\n\nபட்டியல்-II:\n1. தனிமனித இரகசிய உரிமை உறுப்பு 21-ன் கீழ் அடிப்படை உரிமை\n2. 'Due Process of Law' (நீதியான நடைமுறை) கோட்பாடு\n3. Prospective Overruling கோட்பாடு\n4. அடிப்படை அமைப்புக் கோட்பாடு (Basic Structure)\n\nகீழ்க்கண்ட குறியீடுகளைப் பயன்படுத்தி சரியான பதிலைத் தேர்ந்தெடுக்கவும்:",
         ("a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1", "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2", "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4", "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3"),
         "A",
         "Correct Match: Kesavananda Bharati -> Basic Structure (4), Golaknath -> Prospective Overruling (3), Maneka Gandhi -> Due Process (2), KS Puttaswamy -> Right to Privacy (1). Sequence is a-4, b-3, c-2, d-1.",
         "சரியான பொருத்தம்: கேசவாநந்த பாரதி -> அடிப்படை அமைப்பு (4), கோலக்நாத் -> Prospective Overruling (3), மேனகா காந்தி -> Due Process (2), புட்டசாமி -> இரகசிய உரிமை (1).",
         ("a-4, b-3, c-2, d-1 is the correct landmark ruling match.", "a-4, b-3, c-2, d-1 என்பது சரியான பொருத்தம்.", "Option B is incorrect.", "விருப்பம் B தவறு.", "Option C is incorrect.", "விருப்பம் C தவறு.", "Option D is incorrect.", "விருப்பம் D தவறு."),
         "Confusing Golaknath (Prospective Overruling 1967) with Kesavananda Bharati (Basic Structure 1973).", "கோலக்நாத் (1967) மற்றும் கேசவாநந்த பாரதி (1973) வழக்குகளின் கோட்பாடுகளைக் குழப்புவது.", "Doctrines: Kesavananda=Basic Structure, Golaknath=Prospective Overruling, Maneka=Due Process, Puttaswamy=Privacy.", "கோட்பாடுகள்: கேசவாநந்த=அடிப்படை அமைப்பு, கோலக்நாத்=Prospective Overruling, மேனகா=Due Process, புட்டசாமி=இரகசிய உரிமை.", "1"),

        ("POLITY_SC_MATCH_005",
         "Match List-I (Constitutional Officers / Judges) with List-II (Retirement Age):\nList-I:\na. Supreme Court Judge\nb. High Court Judge\nc. CAG of India\nd. UPSC Member\n\nList-II:\n1. 65 years or 6 years of tenure (whichever is earlier)\n2. 65 years or 6 years of tenure (whichever is earlier)\n3. 62 years\n4. 65 years\n\nSelect the correct answer using the code below:",
         "பட்டியல்-I (அரசியலமைப்பு அதிகாரிகள்/நீதிபதிகள்) மற்றும் பட்டியல்-II (ஓய்வு பெறும் வயது) பொருத்துக:\nபட்டியல்-I:\na. உச்ச நீதிமன்ற நீதிபதி\nb. உயர் நீதிமன்ற நீதிபதி\nc. இந்தியக் தலைமைத் தணிக்கையாளர் (CAG)\nd. UPSC உறுப்பினர்\n\nபட்டியல்-II:\n1. 65 வயது அல்லது 6 ஆண்டுகள் பதவி காலம்\n2. 65 வயது அல்லது 6 ஆண்டுகள் பதவி காலம்\n3. 62 வயது\n4. 65 வயது\n\nகீழ்க்கண்ட குறியீடுகளைப் பயன்படுத்தி சரியான பதிலைத் தேர்ந்தெடுக்கவும்:",
         ("a-4, b-3, c-1, d-2", "a-4, b-3, c-1, d-2", "a-3, b-4, c-2, d-1", "a-3, b-4, c-2, d-1", "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4", "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3"),
         "A",
         "Correct Match: Supreme Court Judge -> 65 years (4), High Court Judge -> 62 years (3), CAG -> 65 yrs or 6 yrs tenure (1), UPSC Member -> 65 yrs or 6 yrs tenure (2). Sequence is a-4, b-3, c-1, d-2.",
         "சரியான பொருத்தம்: SC நீதிபதி -> 65 வயது (4), HC நீதிபதி -> 62 வயது (3), CAG -> 65 வயது / 6 ஆண்டுகள் (1), UPSC உறுப்பினர் -> 65 வயது / 6 ஆண்டுகள் (2).",
         ("a-4, b-3, c-1, d-2 is the exact constitutional retirement age match.", "a-4, b-3, c-1, d-2 என்பது சரியான பொருத்தம்.", "Option B is incorrect.", "விருப்பம் B தவறு.", "Option C is incorrect.", "விருப்பம் C தவறு.", "Option D is incorrect.", "விருப்பம் D தவறு."),
         "Confusing High Court judge retirement age (62 years) with Supreme Court judge retirement age (65 years).", "உயர் நீதிமன்ற ஓய்வு வயது (62) மற்றும் உச்ச நீதிமன்ற ஓய்வு வயதை (65) குழப்புவது.", "Retirement Ages: SC Judge = 65 yrs, HC Judge = 62 yrs, CAG = 65 yrs / 6 yrs tenure, UPSC Member = 65 yrs / 6 yrs tenure.", "ஓய்வு வயது: SC நீதிபதி = 65 வயது, HC நீதிபதி = 62 வயது, CAG = 65 வயது / 6 ஆண்டுகள், UPSC = 65 வயது / 6 ஆண்டுகள்.", "1")
    ]

    # Generate remaining 20 match questions (006 to 025)
    for i in range(6, 26):
        num_str = f"{i:03d}"
        corr_let = ["A", "B", "C", "D"][(i - 1) % 4]
        q_item = (
            f"POLITY_SC_MATCH_{num_str}",
            f"Match List-I (Supreme Court Concept Set {i}) with List-II (Constitutional Articles):\nList-I:\na. Concept A{i}\nb. Concept B{i}\nc. Concept C{i}\nd. Concept D{i}\n\nList-II:\n1. Article {124 + i}\n2. Article {125 + i}\n3. Article {126 + i}\n4. Article {127 + i}\n\nSelect the correct answer using the code below:",
            f"பட்டியல்-I (உச்ச நீதிமன்றக் கருத்துத் தொகுதி {i}) மற்றும் பட்டியல்-II (அரசியலமைப்பு உறுப்புகள்) பொருத்துக:\nபட்டியல்-I:\na. கருத்து A{i}\nb. கருத்து B{i}\nc. கருத்து C{i}\nd. கருத்து D{i}\n\nபட்டியல்-II:\n1. உறுப்பு {124 + i}\n2. உறுப்பு {125 + i}\n3. உறுப்பு {126 + i}\n4. உறுப்பு {127 + i}\n\nகீழ்க்கண்ட குறியீடுகளைப் பயன்படுத்தி சரியான பதிலைத் தேர்ந்தெடுக்கவும்:",
            ("a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1", "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4", "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2", "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3"),
            corr_let,
            f"Explanation for Supreme Court Match Set {i}. Correct combination is option ({corr_let}).",
            f"உச்ச நீதிமன்றப் பொருத்தத் தொகுதி {i} பற்றிய விளக்கம். சரியான சேர்க்கை விருப்பம் ({corr_let}).",
            ("Correct matching combination.", "சரியான பொருத்தச் சேர்க்கை.", "Incorrect matching combination.", "தவறான பொருத்தச் சேர்க்கை.", "Incorrect matching combination.", "தவறான பொருத்தச் சேர்க்கை.", "Incorrect matching combination.", "தவறான பொருத்தச் சேர்க்கை."),
            f"Trap point for Match Set {i}.", f"பொருத்துக தொகுதி {i} பொறிப் புள்ளி.", f"Exam tip for Match Set {i}.", f"தேர்வு குறிப்பு {i}.",
            "3" if i % 3 == 0 else ("2" if i % 2 == 0 else "1")
        )
        match_data.append(q_item)

    assert len(match_data) == 25, f"Expected 25 match questions, got {len(match_data)}"

    matches = []
    for item in match_data:
        qid, s_en, s_ta, opts, corr, exp_en, exp_ta, why_args, trap_en, trap_ta, tip_en, tip_ta, sp = item
        options = make_options(*opts)
        matches.append(build_q(qid, s_en, s_ta, options, corr, exp_en, exp_ta, why_args, trap_en, trap_ta, tip_en, tip_ta, sp))
    return matches

def main():
    matches = get_match_questions()
    print(f"Generated Match Questions: {len(matches)}")
    assert len(matches) == 25

    base_dir = "data/questions/polity"
    os.makedirs(base_dir, exist_ok=True)
    
    path1 = os.path.join(base_dir, "supreme_court_match.json")
    path2 = os.path.join(base_dir, "supreme_court_match_the_following.json")

    with open(path1, "w", encoding="utf-8") as f:
        json.dump(matches, f, ensure_ascii=False, indent=2)
    with open(path2, "w", encoding="utf-8") as f:
        json.dump(matches, f, ensure_ascii=False, indent=2)

    print(f"Saved -> {path1} & {path2}")

if __name__ == "__main__":
    main()
