# -*- coding: utf-8 -*-
"""
Generator for Supreme Court Medium MCQs (50 Questions)
Topic: Supreme Court of India
Difficulty: Medium
File: data/questions/polity/supreme_court_medium.json
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

def get_medium_questions():
    medium_data = [
        ("POLITY_SC_MED_001", "Medium",
         "Which landmark case established that 'consultation' with the Chief Justice of India in judicial appointments does NOT mean 'concurrence'?",
         "நீதிபதிகள் நியமனத்தில் இந்தியத் தலைமை நீதிபதியுடனான 'கலந்தாலோசனை' என்பது 'ஒப்புதல்' என்று அர்த்தமாகாது எனத் தீர்ப்பளிக்கப்பட்ட முக்கிய வழக்கு எது?",
         ("First Judges Case (SP Gupta v. Union of India, 1981)", "முதல் நீதிபதிகள் வழக்கு (எஸ்.பி. குப்தா vs இந்திய ஒன்றியம், 1981)", "Second Judges Case (1993)", "இரண்டாவது நீதிபதிகள் வழக்கு (1993)", "Third Judges Case (1998)", "மூன்றாவது நீதிபதிகள் வழக்கு (1998)", "Fourth Judges Case (2015)", "நான்காவது நீதிபதிகள் வழக்கு (2015)"),
         "A",
         "In the First Judges Case (1981), the SC held that consultation did not mean concurrence and executive primacy was maintained in judicial appointments.",
         "முதல் நீதிபதிகள் வழக்கில் (1981), கலந்தாலோசனை என்பது ஒப்புதல் அல்ல என்றும், நியமனத்தில் நிர்வாகத் துறைக்கே முதன்மை அதிகாரம் உள்ளது என்றும் உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
         ("First Judges Case (1981) gave primacy to executive.", "முதல் நீதிபதிகள் வழக்கு (1981) நிர்வாகத்துறைக்கு முதன்மை அளித்தது.", "Second Judges Case (1993) reversed this and established Collegium.", "இரண்டாவது நீதிபதிகள் வழக்கு (1993) இதை மாற்றி கொலீஜியத்தை உருவாக்கியது.", "Third Judges Case (1998) expanded Collegium to CJI + 4 seniors.", "மூன்றாவது நீதிபதிகள் வழக்கு (1998) கொலீஜியத்தை CJI + 4 மூத்த நீதிபதிகள் என விரிவாக்கியது.", "Fourth Judges Case (2015) struck down NJAC.", "நான்காவது நீதிபதிகள் வழக்கு (2015) NJAC-ஐ ரத்து செய்தது."),
         "Confusing First Judges Case 1981 (executive primacy) with Second Judges Case 1993 (Collegium origin).", "முதல் மற்றும் இரண்டாவது நீதிபதிகள் வழக்குகளின் தீர்ப்புகளைக் குழப்புவது.", "First Judges Case (1981) = Consultation != Concurrence (Executive Primacy).", "முதல் நீதிபதிகள் வழக்கு (1981) = கலந்தாலோசனை != ஒப்புதல் (நிர்வாக முதன்மை).", "1"),

        ("POLITY_SC_MED_002", "Medium",
         "In which case did the Supreme Court create the 'Collegium System' by declaring that 'consultation' actually means 'concurrence'?",
         "எந்த வழக்கில் 'கலந்தாலோசனை' என்பது 'ஒப்புதல்' எனப் பொருள் கூறி உச்ச நீதிமன்றம் 'கொலீஜியம் அமைப்பை' (Collegium System) உருவாக்கியது?",
         ("First Judges Case (1981)", "முதல் நீதிபதிகள் வழக்கு (1981)", "Second Judges Case (Supreme Court Advocates-on-Record Association, 1993)", "இரண்டாவது நீதிபதிகள் வழக்கு (1993)", "Kesavananda Bharati Case (1973)", "கேசவாநந்த பாரதி வழக்கு (1973)", "Minerva Mills Case (1980)", "மினர்வா மில்ஸ் வழக்கு (1980)"),
         "B",
         "In the Second Judges Case (1993), the SC overruled SP Gupta case, holding that 'consultation' means 'concurrence', thereby devising the Collegium System.",
         "இரண்டாவது நீதிபதிகள் வழக்கில் (1993), 'கலந்தாலோசனை' என்பது 'ஒப்புதல்' எனக் கூறி, கொலீஜியம் முறையை உச்ச நீதிமன்றம் உருவாக்கியது.",
         ("First Judges Case gave executive primacy.", "முதல் நீதிபதிகள் வழக்கு நிர்வாகத்திற்கு முதன்மை அளித்தது.", "Second Judges Case (1993) established the Collegium System.", "இரண்டாவது நீதிபதிகள் வழக்கு (1993) கொலீஜியம் முறையை உருவாக்கியது.", "Kesavananda Bharati Case established Basic Structure.", "கேசவாநந்த பாரதி வழக்கு அடிப்படை அமைப்புக் கோட்பாட்டை உருவாக்கியது.", "Minerva Mills case reinforced Judicial Review.", "மினர்வா மில்ஸ் வழக்கு நீதித்துறை சீராய்வை வலுப்படுத்தியது."),
         "Confusing First Judges Case (1981) and Second Judges Case (1993).", "முதல் மற்றும் இரண்டாவது நீதிபதிகள் வழக்குகளைக் குழப்புவது.", "Second Judges Case (1993) = Collegium System Created.", "இரண்டாவது நீதிபதிகள் வழக்கு (1993) = கொலீஜியம் அமைப்பு உருவாக்கப்பட்டது.", "1"),

        ("POLITY_SC_MED_003", "Medium",
         "According to the Third Judges Case (1998) Presidential reference, how many senior-most SC judges must the CJI consult for SC judge appointments?",
         "மூன்றாவது நீதிபதிகள் வழக்கு (1998) ஆலோசனையின் படி, உச்ச நீதிமன்ற நீதிபதிகள் நியமனத்திற்கு CJI எத்தனை மூத்த நீதிபதிகளைக் கலந்தாலோசிக்க வேண்டும்?",
         ("2 senior-most judges", "2 மூத்த நீதிபதிகள்", "3 senior-most judges", "3 மூத்த நீதிபதிகள்", "4 senior-most judges", "4 மூத்த நீதிபதிகள்", "5 senior-most judges", "5 மூத்த நீதிபதிகள்"),
         "C",
         "In the Third Judges Case (1998), the SC held that the CJI must consult a collegium of FOUR senior-most judges of the Supreme Court for SC appointments.",
         "மூன்றாவது நீதிபதிகள் வழக்கில் (1998), SC நீதிபதிகள் நியமனத்திற்கு CJI மற்றும் 4 மூத்த நீதிபதிகளைக் கொண்ட கொலீஜியம் கலந்தாலோசிக்கப்பட வேண்டும் எனத் தீர்ப்பளிக்கப்பட்டது.",
         ("2 senior judges is the collegium composition for HIGH COURT judge appointments.", "2 மூத்த நீதிபதிகள் என்பது உயர் நீதிமன்ற நீதிபதி நியமனத்துக்கான கொலீஜியம்.", "3 is incorrect.", "3 என்பது தவறானது.", "4 senior-most judges + CJI (total 5) form the SC appointment Collegium.", "4 மூத்த நீதிபதிகள் + CJI (மொத்தம் 5) உச்ச நீதிமன்ற நியமன கொலீஜியம் ஆவர்.", "5 senior judges is not the exact count of associates.", "5 மூத்த நீதிபதிகள் என்பது தவறான எண்ணிக்கையாகும்."),
         "Confusing SC judge appointment Collegium (CJI + 4 seniors) with High Court judge appointment Collegium (CJI + 2 seniors).", "உச்ச நீதிமன்ற கொலீஜியம் (CJI + 4) மற்றும் உயர் நீதிமன்ற கொலீஜியத்தைக் (CJI + 2) குழப்புவது.", "SC Judge Appointment Collegium = CJI + 4 Senior-most SC Judges.", "SC நீதிபதி நியமன கொலீஜியம் = CJI + 4 மூத்த SC நீதிபதிகள்.", "1"),

        ("POLITY_SC_MED_004", "Medium",
         "Which Constitutional Amendment Act established the National Judicial Appointments Commission (NJAC), which was later struck down by the SC?",
         "பின்னர் உச்ச நீதிமன்றத்தால் ரத்து செய்யப்பட்ட தேசிய நீதிபதிகள் நியமன ஆணையத்தை (NJAC) அமைத்த அரசியலமைப்புத் திருத்தச் சட்டம் எது?",
         ("98th Constitutional Amendment Act", "98-வது அரசியலமைப்புத் திருத்தச் சட்டம்", "99th Constitutional Amendment Act", "99-வது அரசியலமைப்புத் திருத்தச் சட்டம்", "100th Constitutional Amendment Act", "100-வது அரசியலமைப்புத் திருத்தச் சட்டம்", "101st Constitutional Amendment Act", "101-வது அரசியலமைப்புத் திருத்தச் சட்டம்"),
         "B",
         "The 99th Constitutional Amendment Act, 2014 established the NJAC. It was struck down as unconstitutional by the Supreme Court in the Fourth Judges Case (2015).",
         "99-வது அரசியலமைப்புத் திருத்தச் சட்டம் (2014) NJAC-ஐ அமைத்தது. இது 2015-ல் நான்காவது நீதிபதிகள் வழக்கில் உச்ச நீதிமன்றத்தால் செல்லாததாக்கப்பட்டது.",
         ("98th Amendment dealt with Hyderabad-Karnataka region (Art 371J).", "98-வது திருத்தம் ஹைதராபாத்-கர்நாடகா பிராந்தியம் பற்றியது.", "99th Amendment established NJAC.", "99-வது திருத்தம் NJAC-ஐ அமைத்தது.", "100th Amendment dealt with Land Boundary Agreement with Bangladesh.", "100-வது திருத்தம் வங்காளதேச எல்லை ஒப்பந்தம் பற்றியது.", "101st Amendment introduced GST.", "101-வது திருத்தம் ஜிஎஸ்டி-யை அறிமுகப்படுத்தியது."),
         "Confusing 99th Amendment (NJAC) with 100th Amendment (Land Boundary Agreement) or 101st Amendment (GST).", "99-வது (NJAC), 100-வது (எல்லை) மற்றும் 101-வது (ஜிஎஸ்டி) திருத்தங்களைக் குழப்புவது.", "99th Amendment = NJAC (Struck down in 2015 by SC).", "99-வது திருத்தம் = NJAC (2015-ல் SC-ஆல் ரத்து செய்யப்பட்டது).", "1"),

        ("POLITY_SC_MED_005", "Medium",
         "Under the Judges (Inquiry) Act 1968, when a removal motion is admitted by the Presiding Officer, how many members form the Investigation Committee?",
         "1968 நீதிபதிகள் விசாரணைச் சட்டத்தின் படி, நீக்கத் தீர்மானம் ஏற்கப்பட்ட பின் அமைக்கப்படும் விசாரணைக் குழுவில் எத்தனை உறுப்பினர்கள் இருப்பார்கள்?",
         ("2 members", "2 உறுப்பினர்கள்", "3 members", "3 உறுப்பினர்கள்", "5 members", "5 உறுப்பினர்கள்", "7 members", "7 உறுப்பினர்கள்"),
         "B",
         "When a removal motion is admitted, the Speaker/Chairman constitutes a 3-member committee to investigate the charges against the judge.",
         "நீக்கத் தீர்மானம் ஏற்கப்பட்டால், சபாநாயகர்/தலைவர் குற்றச்சாட்டுகளை விசாரிக்க 3 உறுப்பினர்கள் கொண்ட குழுவை அமைப்பார்.",
         ("2 members is insufficient.", "2 உறுப்பினர்கள் போதாது.", "3-member committee is mandated by Judges (Inquiry) Act 1968.", "3 உறுப்பினர்கள் குழு 1968 சட்டத்தால் கட்டாயமாக்கப்பட்டுள்ளது.", "5 members is not the statutory committee size.", "5 உறுப்பினர்கள் குழு அளவு அல்ல.", "7 members is incorrect.", "7 என்பது தவறு."),
         "Confusing Parliamentary inquiry committee size (3 members) with Constitution Bench size (5 judges).", "விசாரணைக் குழு (3) மற்றும் அரசியலமைப்பு அமர்வு (5) அளவுகளைக் குழப்புவது.", "Judges Removal Investigation Committee = 3 Members.", "நீதிபதிகள் நீக்க விசாரணைக் குழு = 3 உறுப்பினர்கள்.", "1"),

        ("POLITY_SC_MED_006", "Medium",
         "Which of the following is NOT one of the 3 members in the Investigation Committee constituted under the Judges (Inquiry) Act 1968?",
         "1968 நீதிபதிகள் விசாரணைச் சட்டத்தின் கீழ் அமைக்கப்படும் 3 உறுப்பினர் விசாரணைக் குழுவில் இடம்பெறாதவர் யார்?",
         ("Chief Justice or a Judge of the Supreme Court", "உச்ச நீதிமன்ற தலைமை நீதிபதி அல்லது ஒரு நீதிபதி", "Chief Justice of a High Court", "ஒரு உயர் நீதிமன்றத் தலைமை நீதிபதி", "A distinguished jurist", "ஒரு புகழ்பெற்ற சட்டம் வல்லுநர்", "Union Cabinet Law Secretary", "ஒன்றிய அமைச்சரவை சட்டச் செயலாளர்"),
         "D",
         "The 3-member committee consists of: (1) CJI or an SC Judge, (2) CJ of a High Court, and (3) a distinguished jurist. The Law Secretary is NOT a member.",
         "3 உறுப்பினர் குழுவில்: (1) CJI அல்லது SC நீதிபதி, (2) HC தலைமை நீதிபதி, (3) புகழ்பெற்ற சட்ட வல்லுநர் ஆகியோர் மட்டுமே இடம்பெறுவர். சட்டச் செயலாளர் இடம்பெற மாட்டார்.",
         ("SC CJI or Judge is Member 1.", "SC CJI அல்லது நீதிபதி உறுப்பினர் 1.", "HC Chief Justice is Member 2.", "HC தலைமை நீதிபதி உறுப்பினர் 2.", "Distinguished Jurist is Member 3.", "புகழ்பெற்ற சட்ட வல்லுநர் உறுப்பினர் 3.", "Law Secretary is EXCLUDED from the statutory committee.", "சட்டச் செயலாளர் குழுவில் இடம்பெற மாட்டார்."),
         "Assuming Law Minister/Secretary is part of the 3-member judicial inquiry committee.", "சட்டச் செயலாளரும் குழுவில் இருப்பார் என தவறாக நினைப்பது.", "Inquiry Committee Composition = SC Judge + HC CJ + Distinguished Jurist.", "விசாரணைக் குழு = SC நீதிபதி + HC தலைமை நீதிபதி + சட்ட வல்லுநர்.", "1"),

        ("POLITY_SC_MED_007", "Medium",
         "To pass a removal motion against an SC judge in Parliament, what majority is required in EACH House of Parliament under Article 124(4)?",
         "உறுப்பு 124(4)-ன் படி நாடாளுமன்றத்தின் ஒவ்வொரு அவையிலும் நீதிபதி நீக்கத் தீர்மானம் எந்த பெரும்பான்மையில் நிறைவேற்றப்பட வேண்டும்?",
         ("Simple majority of total membership", "மொத்த உறுப்பினர்களில் சாதாரண பெரும்பான்மை", "Majority of total membership AND 2/3rd majority of members present and voting", "மொத்த உறுப்பினர்களில் பெரும்பான்மை மற்றும் வருகை தந்து வாக்களிப்போரில் 2/3 பங்கு பெரும்பான்மை", "3/4th majority of members present and voting", "வருகை தந்து வாக்களிப்போரில் 3/4 பங்கு பெரும்பான்மை", "Absolute 2/3rd majority of total membership of the House", "அவையின் மொத்த உறுப்பினர்களில் 2/3 பங்கு பெரும்பான்மை"),
         "B",
         "Article 124(4) mandates a Special Majority: Majority of the total membership of that House AND a majority of not less than two-thirds of the members of that House present and voting.",
         "உறுப்பு 124(4) சிறப்புப் பெரும்பான்மையைக் கோருகிறது: அவையின் மொத்த உறுப்பினர்களில் பெரும்பான்மை மற்றும் வருகை தந்து வாக்களிப்போரில் 2/3 பங்கு பெரும்பான்மை.",
         ("Simple majority is insufficient for judge removal.", "சாதாரண பெரும்பான்மை போதாது.", "Special Majority (Total Membership Majority + 2/3rd Present & Voting) is constitutionally required.", "சிறப்புப் பெரும்பான்மை (மொத்த உறுப். பெரும்பான்மை + 2/3 வருகை & வாக்கு) தேவை.", "3/4th majority is not used in Indian Constitution.", "3/4 பெரும்பான்மை இந்தியாவில் இல்லை.", "Absolute 2/3rd of total membership is not the text of Art 124(4).", "மொத்த உறுப்பினர்களில் 2/3 பங்கு என்பது அரசியலமைப்பு வரத்து அல்ல."),
         "Confusing Special Majority under Art 124(4) (Special Majority of both houses) with simple majority.", "சிறப்புப் பெரும்பான்மை மற்றும் சாதாரண பெரும்பான்மையைக் குழப்புவது.", "Judge Removal Majority = Special Majority under Art 124(4).", "நீதிபதி நீக்கப் பெரும்பான்மை = உறுப்பு 124(4)-ன் கீழ் சிறப்புப் பெரும்பான்மை.", "1"),

        ("POLITY_SC_MED_008", "Medium",
         "Which of the following disputes is EXCLUDED from the Original Jurisdiction of the Supreme Court under the proviso to Article 131?",
         "உறுப்பு 131-ன் வரம்பின் (Proviso) கீழ் உச்ச நீதிமன்றத்தின் மூல ஆதிக்கத்திலிருந்து விலக்கப்பட்ட தகராறு எது?",
         ("Dispute arising out of any pre-Constitution treaty, agreement, or covenant", "அரசியலமைப்புக்கு முந்தைய உடன்படிக்கை அல்லது ஒப்பந்தத்திலிருந்து எழும் தகராறு", "Dispute between Centre and a State regarding tax devolution", "வரிப் பகிர்வு குறித்து ஒன்றியம் மற்றும் மாநிலத்திற்கு இடையேயான தகராறு", "Dispute between two States regarding state boundary demarcation", "மாநில எல்லை நிர்ணயம் குறித்து இரண்டு மாநிலங்களுக்கு இடையேயான தகராறு", "Dispute between Union and a State regarding property ownership", "சொத்து உரிமை குறித்து ஒன்றியம் மற்றும் மாநிலத்திற்கு இடையேயான தகராறு"),
         "A",
         "The proviso to Article 131 explicitly excludes disputes arising out of any pre-Constitution treaty, agreement, covenant, engagement, or sanad.",
         "அரசியலமைப்புக்கு முந்தைய உடன்படிக்கைகள், ஒப்பந்தங்கள் போன்றவற்றிலிருந்து எழும் தகராறுகளை உறுப்பு 131-ன் வரம்பு மூல ஆதிக்கத்திலிருந்து விலக்குகிறது.",
         ("Pre-Constitution treaties ARE EXCLUDED under Art 131 proviso.", "அரசியலமைப்புக்கு முந்தைய ஒப்பந்தங்கள் உறுப்பு 131 வரம்பில் விலக்கப்பட்டுள்ளன.", "Tax devolution between Centre-State lies in Art 131 jurisdiction.", "வரிப் பகிர்வு தகராறு உறுப்பு 131-ல் வரும்.", "State boundary dispute lies under Art 131.", "எல்லைத் தகராறு உறுப்பு 131-ல் வரும்.", "Property ownership dispute lies under Art 131.", "சொத்து உரிமைத் தகராறு உறுப்பு 131-ல் வரும்."),
         "Assuming pre-constitutional treaty disputes can be adjudicated under Article 131 Original Jurisdiction (they are strictly excluded).", "அரசியலமைப்புக்கு முந்தைய ஒப்பந்தத் தகராறுகளும் உறுப்பு 131-ல் வரும் என நினைப்பது.", "Art 131 Proviso Exclusion = Pre-Constitution treaties, covenants, agreements.", "உறுப்பு 131 விலக்கு = அரசியலமைப்புக்கு முந்தைய ஒப்பந்தங்கள் & உடன்படிக்கைகள்.", "1"),

        ("POLITY_SC_MED_009", "Medium",
         "Under Article 262 of the Constitution, which type of dispute is excluded from the Supreme Court's jurisdiction if Parliament so provides by law?",
         "நாடாளுமன்றம் சட்டத்தின் மூலம் வழிவகை செய்தால், எந்தத் தகராறு உச்ச நீதிமன்ற அதிகார வரம்பிலிருந்து விலக்கப்படும் (உறுப்பு 262)?",
         ("Inter-state trade and commerce disputes", "மாநிலங்களுக்கிடையேயான வர்த்தகத் தகராறுகள்", "Adjudication of disputes relating to waters of inter-state rivers or river valleys", "மாநிலங்களுக்கிடையேயான நதிகள் அல்லது நதிப் பள்ளத்தாக்குகளின் நீர் தொடர்பான தகராறுகள்", "Disputes relating to All-India Services cadres", "அகில இந்தியப் பணிகள் பிரிவினர் தொடர்பான தகராறுகள்", "Disputes relating to presidential election malpractices", "குடியரசுத் தலைவர் தேர்தல் முறைகேடுகள் பற்றிய தகராறுகள்"),
         "B",
         "Under Article 262(2), Parliament may by law provide that neither the Supreme Court nor any other court shall exercise jurisdiction in respect of inter-state river water disputes.",
         "உறுப்பு 262(2)-ன் படி, மாநிலங்களுக்கிடையேயான நதிநீர் தகராறுகளில் உச்ச நீதிமன்றமோ அல்லது வேறு எந்த நீதிமன்றமோ தலையிடக் கூடாது என நாடாளுமன்றம் சட்டம் இயற்றலாம்.",
         ("Trade disputes are under Art 301-307.", "வர்த்தகத் தகராறுகள் உறுப்புகள் 301-307.", "Inter-state river water disputes (Art 262) can be barred from SC jurisdiction by Parliament.", "மாநிலங்களுக்கு இடையேயான நதிநீர் தகராறுகள் (உறுப்பு 262) SC ஆதிக்கத்திலிருந்து விலக்கப்படலாம்.", "All-India Services fall under CAT / Courts.", "அகில இந்தியப் பணிகள் CAT / நீதிமன்றங்களின் கீழ் வரும்.", "Presidential election disputes are exclusively decided by SC under Art 71.", "குடியரசுத் தலைவர் தேர்தல் தகராறுகளை உறுப்பு 71-ன் படி SC மட்டுமே விசாரிக்கும்."),
         "Thinking Supreme Court has original jurisdiction over inter-state river water disputes (Art 262 excludes them if tribunal law enacted).", "மாநிலங்களுக்கு இடையேயான நதிநீர் தகராறுகளை SC நேரடியாக விசாரிக்கும் என நினைப்பது.", "Article 262 = Inter-State Water Disputes (Parliament can exclude SC jurisdiction).", "உறுப்பு 262 = மாநிலங்களுக்கிடையேயான நதிநீர் தகராறுகள் (SC அதிகார வரம்பை நாடாளுமன்றம் விலக்கலாம்).", "1"),

        ("POLITY_SC_MED_010", "Medium",
         "Which Article of the Constitution gives the Supreme Court EXCLUSIVE jurisdiction to decide disputes regarding the election of the President or Vice-President?",
         "குடியரசுத் தலைவர் அல்லது துணைக் குடியரசுத் தலைவர் தேர்தல் தொடர்பான தகராறுகளைத் தீர்க்க உச்ச நீதிமன்றத்திற்குத் தனிப்பட்ட அதிகாரத்தை வழங்கும் உறுப்பு எது?",
         ("Article 61", "உறுப்பு 61", "Article 71", "உறுப்பு 71", "Article 81", "உறுப்பு 81", "Article 131", "உறுப்பு 131"),
         "B",
         "Article 71(1) states that all doubts and disputes arising out of or in connection with the election of a President or Vice-President shall be inquired into and decided by the Supreme Court whose decision shall be final.",
         "குடியரசுத் தலைவர் அல்லது துணைக் குடியரசுத் தலைவர் தேர்தல் தொடர்பான அனைத்து சந்தேகங்கள் மற்றும் தகராறுகளை உச்ச நீதிமன்றம் மட்டுமே விசாரித்துத் தீர்க்கும் என உறுப்பு 71(1) கூறுகிறது.",
         ("Art 61 is Impeachment of President.", "உறுப்பு 61 குடியரசுத் தலைவர் பதவி நீக்கம்.", "Art 71 gives SC exclusive jurisdiction over Presidential/Vice-Presidential election disputes.", "உறுப்பு 71 குடியரசுத் தலைவர்/துணைக் குடியரசுத் தலைவர் தேர்தல் தகராறுகளில் SC-க்கு தனிப்பட்ட அதிகாரம் அளிக்கிறது.", "Art 81 is Composition of Lok Sabha.", "உறுப்பு 81 மக்களவை அமைப்பு.", "Art 131 is Federal Original Jurisdiction.", "உறுப்பு 131 கூட்டாட்சி மூல ஆதிக்கம்."),
         "Confusing Article 71 (Presidential Election Disputes) with Article 131 (Federal Disputes).", "உறுப்பு 71 மற்றும் உறுப்பு 131-ஐக் குழப்புவது.", "President/Vice-President Election Disputes = Article 71 (SC Exclusive Jurisdiction).", "குடியரசுத் தலைவர்/துணைத் தலைவர் தேர்தல் தகராறுகள் = உறுப்பு 71 (SC பிரத்யேக அதிகாரம்).", "1"),

        ("POLITY_SC_MED_011", "Medium",
         "What is the key difference between the Writ Jurisdiction of the Supreme Court (Art 32) and High Courts (Art 226)?",
         "உச்ச நீதிமன்றம் (உறுப்பு 32) மற்றும் உயர் நீதிமன்றங்களின் (உறுப்பு 226) நீதிப்பேராணை ஆதிக்கத்திற்கு இடையேயான முக்கிய வேறுபாடு என்ன?",
         ("SC can issue writs for Fundamental Rights AND legal rights, while HC can issue for Fundamental Rights only", "SC அடிப்படை உரிமைகள் மற்றும் சட்ட உரிமைகளுக்கு பேராணை பிறப்பிக்கலாம்; HC அடிப்படை உரிமைகளுக்கு மட்டுமே பிறப்பிக்கலாம்", "SC can issue writs ONLY for Fundamental Rights, while HC can issue for Fundamental Rights AND any other legal rights", "SC அடிப்படை உரிமைகளுக்கு மட்டுமே பேராணை பிறப்பிக்கலாம்; HC அடிப்படை உரிமைகள் மற்றும் இதர சட்ட உரிமைகளுக்கும் பிறப்பிக்கலாம்", "SC writ jurisdiction is narrower in territorial scope than High Court", "SC பேராணை அதிகாரம் உயர் நீதிமன்றத்தை விட ஆட்சிப்பரப்பில் குறுகியது", "SC can refuse to exercise Art 32 writ jurisdiction, while HC cannot refuse Art 226", "SC உறுப்பு 32-ஐ மறுக்கலாம்; HC உறுப்பு 226-ஐ மறுக்க முடியாது"),
         "B",
         "SC writ jurisdiction under Art 32 is restricted ONLY to Fundamental Rights enforcement. High Court writ jurisdiction under Art 226 is wider, covering Fundamental Rights and 'any other purpose' (legal rights).",
         "உறுப்பு 32-ன் கீழ் SC அடிப்படை உரிமைகளுக்கு மட்டுமே பேராணை பிறப்பிக்க முடியும். உறுப்பு 226-ன் கீழ் HC அடிப்படை உரிமைகள் மற்றும் 'இதர சட்ட உரிமைகளுக்கும்' பிறப்பிக்க முடியும் (HC அதிகாரம் பரந்தது).",
         ("SC cannot issue Art 32 writs for ordinary legal rights.", "SC சாதாரண சட்ட உரிமைகளுக்கு உறுப்பு 32-ல் பேராணை பிறப்பிக்க முடியாது.", "SC writ power = FRs only; HC writ power = FRs + ordinary legal rights.", "SC பேராணை = FR மட்டுமே; HC பேராணை = FR + சட்ட உரிமைகள்.", "SC territorial scope covers entire India, wider than HC.", "SC ஆட்சிப்பரப்பு இந்தியா முழுமைக்கும் பொருந்தும், பரந்தது.", "Art 32 is itself a Fundamental Right, so SC CANNOT refuse; whereas Art 226 is discretionary for HC.", "உறுப்பு 32 என்பதே ஒரு அடிப்படை உரிமை என்பதால் SC மறுக்க முடியாது; HC-க்கு உறுப்பு 226 தன்னிச்சையானது."),
         "Assuming Supreme Court's writ jurisdiction under Article 32 is wider than High Court's under Article 226 (High Court's writ jurisdiction is actually wider in subject-matter scope).", "உச்ச நீதிமன்றத்தின் பேராணை அதிகாரம் உயர் நீதிமன்றத்தை விடப் பரந்தது எனத் தவறாக நினைப்பது.", "Writ Jurisdiction Scope: High Court (Art 226) > Supreme Court (Art 32) in subject-matter scope.", "பேராணை வரம்பு: பொருள் வரம்பில் உயர் நீதிமன்றம் (உறுப்பு 226) > உச்ச நீதிமன்றம் (உறுப்பு 32).", "1"),

        ("POLITY_SC_MED_012", "Medium",
         "Why CANNOT the Supreme Court refuse to exercise its Writ Jurisdiction under Article 32 when a citizen approaches it?",
         "ஒரு குடிமகன் அணுகும்போது, உறுப்பு 32-ன் கீழ் தன் நீதிப்பேராணை ஆதிக்கத்தைப் பயன்படுத்த உச்ச நீதிமன்றம் ஏன் மறுக்க முடியாது?",
         ("Because Article 32 is itself a Fundamental Right guaranteed under Part III", "ஏனெனில் உறுப்பு 32 என்பதே பகுதி III-ல் உத்தரவாதம் அளிக்கப்பட்ட ஒரு அடிப்படை உரிமையாகும்", "Because Article 32 is a Directive Principle", "ஏனெனில் உறுப்பு 32 ஒரு அரசு நெறிமுறைக்கோட்பாடு", "Because the Law Minister mandates it", "ஏனெனில் சட்ட அமைச்சர் அதைக் கட்டாயப்படுத்துகிறார்", "Because High Courts have no writ jurisdiction", "ஏனெனில் உயர் நீதிமன்றங்களுக்கு பேராணை அதிகாரமில்லை"),
         "A",
         "Article 32 is described as the 'Heart and Soul of the Constitution' (Dr. Ambedkar) and is ITSELF a Fundamental Right. Hence, SC is the defender and guarantor of FRs and cannot refuse an Art 32 petition.",
         "உறுப்பு 32 என்பதே ஒரு அடிப்படை உரிமையாகும் (பகுதி III). எனவே உச்ச நீதிமன்றம் அடிப்படை உரிமைகளின் காவலனாக இருப்பதால் உறுப்பு 32 மனுவை விசாரிக்க மறுக்க முடியாது.",
         ("Art 32 is itself a Fundamental Right, making SC remedy mandatory.", "உறுப்பு 32 என்பதே அடிப்படை உரிமை என்பதால் SC மறுக்க முடியாது.", "Art 32 is not a DPSP.", "உறுப்பு 32 அரசு நெறிமுறைக்கோட்பாடு அல்ல.", "Law Minister has no say in court remedy.", "சட்ட அமைச்சருக்கு இதில் அதிகாரமில்லை.", "High Courts DO have writ jurisdiction under Art 226.", "உயர் நீதிமன்றங்களுக்கும் உறுப்பு 226-ல் அதிகாரம் உண்டு."),
         "Confusing discretionary nature of High Court Art 226 writ jurisdiction with mandatory constitutional obligation of SC under Art 32.", "உயர் நீதிமன்றத் தன்னிச்சை அதிகாரம் (226) மற்றும் உச்ச நீதிமன்றக் கட்டாயப் பொறுப்பைக் (32) குழப்புவது.", "Article 32 = Itself a Fundamental Right -> SC cannot refuse to grant remedy.", "உறுப்பு 32 = தானே ஒரு அடிப்படை உரிமை -> SC நிவாரணம் வழங்க மறுக்க முடியாது.", "1"),

        ("POLITY_SC_MED_013", "Medium",
         "Under Article 143(1), when the President refers a question of public importance to the Supreme Court, is the SC bound to give an opinion?",
         "உறுப்பு 143(1)-ன் கீழ் பொது முக்கியத்துவம் வாய்ந்த கேள்வியை குடியரசுத் தலைவர் அனுப்பும்போது, உச்ச நீதிமன்றம் கருத்து தெரிவிக்கக் கடமைப்பட்டுள்ளதா?",
         ("Yes, SC is constitutionally bound to give an opinion in all cases", "ஆம், அனைத்து வழக்குகளிலும் கருத்து தெரிவிக்க SC கடமைப்பட்டுள்ளது", "No, SC may refuse to express its opinion under Article 143(1)", "இல்லை, உறுப்பு 143(1)-ன் கீழ் SC தன் கருத்தைத் தெரிவிக்க மறுக்கலாம்", "Yes, if the reference is made by the Prime Minister", "பிரதமர் பரிந்துரைத்தால் கட்டாயம் தெரிவிக்க வேண்டும்", "No, unless Parliament passes a resolution directing SC", "நாடாளுமன்றம் ஆணையிட்டால் ஒழிய தெரிவிக்கத் தேவையில்லை"),
         "B",
         "Under Article 143(1) (general public importance questions), the SC 'may' report its opinion; it is NOT bound to give an opinion (e.g., SC refused to give opinion in Ram Janmabhoomi case, 1994).",
         "உறுப்பு 143(1)-ன் கீழ் (பொது விவகாரங்கள்), உச்ச நீதிமன்றம் கருத்து தெரிவிக்கலாம்; ஆனால் கருத்து தெரிவிக்க மறுக்கவும் உரிமை உண்டு (எ.கா. 1994 ராம் ஜென்மபூமி வழக்கில் SC கருத்து தெரிவிக்க மறுத்தது).",
         ("SC is not bound to give opinion under Art 143(1).", "உறுப்பு 143(1)-ன் கீழ் கருத்து தெரிவிக்க SC கடமைப்படவில்லை.", "SC MAY refuse to give opinion under Art 143(1).", "உறுப்பு 143(1)-ன் கீழ் கருத்து தெரிவிக்க மறுக்க SC-க்கு அதிகாரம் உண்டு.", "PM reference is not a constitutional term.", "பிரதமர் பரிந்துரை என்பது அரசியலமைப்புச் சொல் அல்ல.", "Parliament resolution is not required.", "நாடாளுமன்ற தீர்மானம் தேவையில்லை."),
         "Assuming SC MUST give an opinion under both clauses of Article 143 (Under 143(1) SC MAY refuse, under 143(2) pre-constitution disputes SC MUST opinion).", "உறுப்பு 143(1) மற்றும் 143(2) ஆகிய இரண்டிலும் SC கருத்து தெரிவிக்கக் கடமைப்பட்டுள்ளது என நினைப்பது.", "Article 143(1) = SC MAY give or refuse opinion. Article 143(2) = SC MUST give opinion.", "உறுப்பு 143(1) = SC கருத்து தெரிவிக்கலாம்/மறுக்கலாம். உறுப்பு 143(2) = SC கட்டாயம் கருத்து தெரிவிக்க வேண்டும்.", "1"),

        ("POLITY_SC_MED_014", "Medium",
         "Under Article 143(2), regarding pre-Constitution treaties/agreements, is the Supreme Court bound to tender its opinion to the President?",
         "அரசியலமைப்புக்கு முந்தைய ஒப்பந்தங்கள் பற்றிய உறுப்பு 143(2) ஆலோசனையில், உச்ச நீதிமன்றம் குடியரசுத் தலைவருக்குக் கருத்து தெரிவிக்கக் கடமைப்பட்டுள்ளதா?",
         ("No, SC can refuse under Art 143(2) as well", "இல்லை, உறுப்பு 143(2)-ன் கீழும் SC மறுக்கலாம்", "Yes, under Article 143(2) the Supreme Court 'shall' report its opinion to the President", "ஆம், உறுப்பு 143(2)-ன் கீழ் உச்ச நீதிமன்றம் குடியரசுத் தலைவருக்குக் கருத்துத் தெரிவிக்கக் 'கடமைப்பட்டுள்ளது'", "Yes, but only if approved by Law Commission", "ஆம், ஆனால் சட்ட ஆணைய ஒப்புதல் இருந்தால் மட்டுமே", "No, because pre-constitution treaties are illegal", "இல்லை, ஏனெனில் அரசியலமைப்புக்கு முந்தைய ஒப்பந்தங்கள் சட்டவிரோதமானவை"),
         "B",
         "Under Article 143(2) (disputes arising out of pre-Constitution treaties/agreements mentioned in Art 131 proviso), the Constitution uses the word 'shall', making it mandatory for SC to give its opinion.",
         "உறுப்பு 143(2)-ன் கீழ் (அரசியலமைப்புக்கு முந்தைய ஒப்பந்தங்கள்), அரசியலமைப்பு 'shall' என்ற சொல்லைப் பயன்படுத்துவதால் உச்ச நீதிமன்றம் தன் கருத்தைத் தெரிவிப்பது கட்டாயமாகும்.",
         ("Refusal is possible under 143(1), but NOT under 143(2).", "143(1)-ல் மறுக்கலாம், ஆனால் 143(2)-ல் மறுக்க முடியாது.", "SC SHALL report its opinion under Art 143(2).", "உறுப்பு 143(2)-ன் கீழ் SC கருத்துத் தெரிவிக்கக் கடமைப்பட்டுள்ளது.", "Law Commission approval is irrelevant.", "சட்ட ஆணைய ஒப்புதல் தொடர்பற்றது.", "Pre-constitution treaties are constitutionally recognized.", "அரசியலமைப்புக்கு முந்தைய ஒப்பந்தங்கள் அங்கீகரிக்கப்பட்டவை."),
         "Failing to distinguish between Article 143(1) (discretionary for SC) and Article 143(2) (mandatory for SC).", "உறுப்பு 143(1) (தன்னிச்சையானது) மற்றும் உறுப்பு 143(2) (கட்டாயமானது) ஆகியவற்றை வேறுபடுத்தத் தவறுவது.", "Art 143(1) = SC MAY give opinion. Art 143(2) = SC SHALL give opinion.", "உறுப்பு 143(1) = SC கருத்து தெரிவிக்கலாம். உறுப்பு 143(2) = SC கருத்து தெரிவிக்க வேண்டும்.", "1"),

        ("POLITY_SC_MED_015", "Medium",
         "What is the nature of the Special Leave Petition (SLP) under Article 136 of the Constitution?",
         "அரசியலமைப்பு உறுப்பு 136-ன் கீழ் வரும் சிறப்பு விடுப்பு மனுவின் (SLP) தன்மை என்ன?",
         ("It is a matter of right for every litigant", "இது ஒவ்வொரு மனுதாரருக்கும் உரிய உரிமையாகும்", "It is a discretionary power of the Supreme Court, not a right of the party", "இது உச்ச நீதிமன்றத்தின் தன்னிச்சை அதிகாரமே தவிர, மனுதாரரின் உரிமையல்ல", "It applies only to criminal cases", "இது குற்றவியல் வழக்குகளுக்கு மட்டுமே பொருந்தும்", "It requires prior permission from the High Court", "இதற்கு உயர் நீதிமன்றத்தின் முன்அனுமதி தேவை"),
         "B",
         "SLP under Article 136 is a residual, extraordinary, discretionary power of the Supreme Court. It is NOT a right of appeal given to a litigant.",
         "உறுப்பு 136-ன் கீழ் SLP என்பது உச்ச நீதிமன்றத்தின் தன்னிச்சையான (Discretionary) மற்றும் விதிவிலக்கான அதிகாரமாகும்; இது மனுதாரரின் சட்டப்பூர்வ உரிமையல்ல.",
         ("SLP is not a matter of right.", "SLP மனுதாரரின் உரிமை அல்ல.", "SLP is a DISCRETIONARY power of the SC.", "SLP உச்ச நீதிமன்றத்தின் தன்னிச்சை அதிகாரம்.", "SLP applies to civil, criminal, income tax, labor cases, etc.", "SLP சிவில், குற்றவியல், வரி, தொழிலாளர் வழக்குகள் அனைத்திற்கும் பொருந்தும்.", "No prior HC certificate/permission is required for Art 136 SLP.", "உயர் நீதிமன்ற சான்றிதழ்/அனுமதி SLP-க்குத் தேவையில்லை."),
         "Thinking SLP under Article 136 is a regular statutory right of appeal available to all citizens.", "SLP என்பது அனைவருக்கும் உரிய சாதாரண மேல்முறையீட்டு உரிமை எனக் கருதுவது.", "Article 136 SLP = Discretionary power of SC (not a right of the party).", "உறுப்பு 136 SLP = உச்ச நீதிமன்றத்தின் தன்னிச்சை அதிகாரம் (மனுதாரர் உரிமையல்ல).", "1"),

        ("POLITY_SC_MED_016", "Medium",
         "Which Article of the Constitution confers power on the Supreme Court to punish for Contempt of Court?",
         "நீதிமன்ற அவமதிப்புக்குத் தண்டிக்கும் அதிகாரத்தை உச்ச நீதிமன்றத்திற்கு வழங்கும் அரசியலமைப்பு உறுப்பு எது?",
         ("Article 129", "உறுப்பு 129", "Article 131", "உறுப்பு 131", "Article 134", "உறுப்பு 134", "Article 140", "உறுப்பு 140"),
         "A",
         "Article 129 states that the Supreme Court shall be a Court of Record and shall have all the powers of such a court including the power to punish for contempt of itself.",
         "உறுப்பு 129 உச்ச நீதிமன்றத்தைப் பதிவு நீதிமன்றமாக அறிவிப்பதுடன், நீதிமன்ற அவமதிப்புக்குத் தண்டிக்கும் அதிகாரத்தையும் வழங்குகிறது.",
         ("Art 129 confers contempt punishment power as a Court of Record.", "உறுப்பு 129 அவமதிப்புத் தண்டனை அதிகாரத்தை வழங்குகிறது.", "Art 131 is Original Jurisdiction.", "உறுப்பு 131 மூல ஆதிக்கம்.", "Art 134 is Criminal Appeals.", "உறுப்பு 134 குற்றவியல் மேல்முறையீடு.", "Art 140 is Ancillary Powers.", "உறுப்பு 140 துணை அதிகாரங்கள்."),
         "Confusing Article 129 (SC Contempt Power) with Article 215 (High Court Contempt Power).", "உச்ச நீதிமன்ற அவமதிப்பு அதிகாரம் (129) மற்றும் உயர் நீதிமன்ற அவமதிப்பு அதிகாரத்தை (215) குழப்புவது.", "Supreme Court Contempt Power = Article 129. High Court = Article 215.", "உச்ச நீதிமன்ற அவமதிப்பு அதிகாரம் = உறுப்பு 129. உயர் நீதிமன்றம் = உறுப்பு 215.", "1"),

        ("POLITY_SC_MED_017", "Medium",
         "Can the Supreme Court punish for contempt of SUBORDINATE COURTS in India under Article 129?",
         "உறுப்பு 129-ன் கீழ் கீழ்மை நீதிமன்றங்களின் (Subordinate Courts) அவமதிப்பிற்கும் உச்ச நீதிமன்றம் தண்டிக்குமா?",
         ("No, SC can punish only for contempt of itself", "இல்லை, SC தன் சொந்த அவமதிப்புக்கு மட்டுமே தண்டிக்கும்", "Yes, as a Court of Record and apex court, SC can punish for contempt of subordinate courts as well", "ஆம், உச்ச நீதிமன்றமாகவும் பதிவு நீதிமன்றமாகவும் கீழ்மை நீதிமன்ற அவமதிப்புக்கும் தண்டிக்கலாம்", "Yes, but only if the State Governor recommends", "ஆம், மாநில ஆளுநர் பரிந்துரைத்தால் மட்டுமே", "No, only High Courts have subordinate court contempt power", "இல்லை, உயர் நீதிமன்றங்களுக்கு மட்டுமே கீழ்மை நீதிமன்ற அவமதிப்பு அதிகாரம் உண்டு"),
         "B",
         "In *Delhi Judicial Service Association Case (1991)*, the SC held that under Article 129, its contempt powers extend to punishing contempt of ALL subordinate courts and tribunals in India.",
         "1991 டெல்லி நீதித்துறை சேவை சங்க வழக்கில், உறுப்பு 129-ன் கீழ் கீழ்மை நீதிமன்றங்களின் அவமதிப்புக்கும் தண்டிக்கும் அதிகாரம் உச்ச நீதிமன்றத்திற்கு உண்டு எனத் தீர்ப்பளிக்கப்பட்டது.",
         ("SC contempt power is not restricted to itself.", "SC அவமதிப்பு அதிகாரம் தன்னாட்சிக்கு மட்டும் கட்டுப்பட்டதல்ல.", "SC can punish for contempt of subordinate courts under Art 129 (Delhi Judicial Service Case 1991).", "கீழ்மை நீதிமன்ற அவமதிப்புக்கும் SC தண்டிக்கலாம் (1991 வழக்கு).", "Governor recommendation is irrelevant.", "ஆளுநர் பரிந்துரை தேவையில்லை.", "HC also has power under Art 215, but SC also possesses it under Art 129.", "HC-க்கும் அதிகாரம் உண்டு, SC-க்கும் உறுப்பு 129-ல் உண்டு."),
         "Assuming Supreme Court can ONLY punish for contempt of itself and not subordinate courts.", "உச்ச நீதிமன்றம் தன் அவமதிப்புக்கு மட்டுமே தண்டிக்க முடியும் என நினைப்பது.", "SC Contempt Power (Art 129) = Extends to Contempt of Subordinate Courts as well.", "SC அவமதிப்பு அதிகாரம் (உறுப்பு 129) = கீழ்மை நீதிமன்ற அவமதிப்புக்கும் பொருந்தும்.", "1"),

        ("POLITY_SC_MED_018", "Medium",
         "What is the doctrine of 'Stare Decisis' embedded in Article 141 of the Constitution?",
         "அரசியலமைப்பு உறுப்பு 141-ல் பொறிக்கப்பட்டுள்ள 'Stare Decisis' கோட்பாடு என்றால் என்ன?",
         ("The doctrine that lower courts must follow decisions of higher courts (binding precedent)", "கீழ்மை நீதிமன்றங்கள் உயர் நீதிமன்றங்களின் தீர்ப்புகளைப் பின்பற்ற வேண்டும் என்ற கோட்பாடு (கட்டாய முன்மாதிரி)", "The doctrine that President must approve all court judgments", "குடியரசுத் தலைவர் அனைத்து தீர்ப்புகளுக்கும் ஒப்புதல் அளிக்க வேண்டும் என்ற கோட்பாடு", "The doctrine of separation of powers between executive and legislature", "நிர்வாகம் மற்றும் சட்டமன்றப் பிரிவினை கோட்பாடு", "The doctrine that SC judgments can be overridden by State Assemblies", "மாநில சட்டமன்றங்கள் SC தீர்ப்புகளை மாற்றியமைக்கலாம் என்ற கோட்பாடு"),
         "A",
         "Stare Decisis means 'to stand by things decided'. Under Article 141, the law declared by the Supreme Court is a binding precedent for all other courts in India.",
         "Stare Decisis என்பது 'தீர்மானிக்கப்பட்ட தீர்ப்புகளுக்குக் கட்டுப்பட்டு நடப்பதாகும்'. உறுப்பு 141-ன் கீழ் உச்ச நீதிமன்றத்தின் தீர்ப்புகள் இந்தியாவில் உள்ள அனைத்து நீதிமன்றங்களுக்கும் முன்மாதிரியாகக் கட்டுப்படுத்தும்.",
         ("Stare Decisis = Binding Precedent under Article 141.", "Stare Decisis = உறுப்பு 141-ன் கீழ் கட்டாய முன்மாதிரி சட்டம்.", "President approval is not needed for judgments.", "தீர்ப்புகளுக்கு குடியரசுத் தலைவர் ஒப்புதல் தேவையில்லை.", "Separation of powers is under Art 50.", "அதிகாரப் பிரிவினை உறுப்பு 50.", "State Assemblies cannot override SC judgments on law.", "மாநில சட்டமன்றங்கள் SC தீர்ப்புகளை மாற்ற முடியாது."),
         "Confusing Stare Decisis (binding precedent) with Res Judicata (finality between parties).", "Stare Decisis (முன்மாதிரி சட்டம்) மற்றும் Res Judicata (தரப்பினரிடையே இறுதித் தன்மை) ஆகியவற்றை குழப்புவது.", "Stare Decisis = Doctrine of Binding Judicial Precedent (Article 141).", "Stare Decisis = கட்டாய நீதித்துறை முன்மாதிரிக் கோட்பாடு (உறுப்பு 141).", "1"),

        ("POLITY_SC_MED_019", "Medium",
         "Is the Supreme Court of India bound by its OWN previous decisions under Article 141?",
         "உறுப்பு 141-ன் கீழ் உச்ச நீதிமன்றம் தனது சொந்த முந்தைய தீர்ப்புகளுக்குக் கட்டுப்பட்டதா?",
         ("Yes, SC is strictly bound by its own past rulings forever", "ஆம், SC தன் முந்தைய தீர்ப்புகளுக்கு என்றென்றும் கட்டுப்பட்டது", "No, the Supreme Court is NOT bound by its own decisions and can overrule them", "இல்லை, உச்ச நீதிமன்றம் தன் சொந்தத் தீர்ப்புகளுக்குக் கட்டுப்பட்டதல்ல, அவற்றை மாற்றியமைக்கலாம்", "Yes, unless Parliament permits it to change", "ஆம், நாடாளுமன்றம் அனுமதித்தால் ஒழிய மாற்ற முடியாது", "Yes, provided the Law Minister agrees", "ஆம், சட்ட அமைச்சர் ஒப்புக்கொண்டால் மட்டுமே மாற்றலாம்"),
         "B",
         "In the *Bengal Immunity Case (1955)*, the SC held that Article 141 binds 'all courts within India', which means ALL COURTS OTHER THAN THE SUPREME COURT ITSELF. SC can overrule its past decisions.",
         "1955 பெங்கால் இம்யூனிட்டி வழக்கில், உறுப்பு 141 'இந்தியாவில் உள்ள அனைத்து நீதிமன்றங்களையும்' கட்டுப்படுத்தும் என்றால், அது உச்ச நீதிமன்றத்தைத் தவிர மற்ற நீதிமன்றங்களையே குறிக்கும்; SC தன் பழைய தீர்ப்புகளை மாற்றலாம் எனத் தீர்ப்பளிக்கப்பட்டது.",
         ("SC is not bound by its own decisions forever.", "SC தன் சொந்தத் தீர்ப்புகளுக்கு என்றென்றும் கட்டுப்பட்டதல்ல.", "SC IS NOT bound by its own decisions and can depart/overrule them (Bengal Immunity Case 1955).", "SC தன் சொந்தத் தீர்ப்புகளுக்குக் கட்டுப்பட்டதல்ல, அவற்றை மாற்றியமைக்கலாம்.", "Parliament permission is not required for SC to overrule its past judgment.", "நாடாளுமன்ற அனுமதி தேவையில்லை.", "Law Minister has no role in judicial overruling.", "சட்ட அமைச்சருக்குப் பங்கில்லை."),
         "Assuming Article 141 binds the Supreme Court itself (Art 141 binds all OTHER courts in India, not the SC itself).", "உறுப்பு 141 உச்ச நீதிமன்றத்தையும் கட்டுப்படுத்தும் எனத் தவறாக நினைப்பது.", "Article 141 = Binds all courts IN India EXCEPT the Supreme Court itself.", "உறுப்பு 141 = உச்ச நீதிமன்றத்தைத் தவிர இந்தியாவில் உள்ள அனைத்து நீதிமன்றங்களையும் கட்டுப்படுத்தும்.", "1"),

        ("POLITY_SC_MED_020", "Medium",
         "Which Article of the Constitution confers power on Parliament to enlarge the jurisdiction of the Supreme Court?",
         "உச்ச நீதிமன்றத்தின் அதிகார வரம்பை விரிவாக்கம் செய்ய நாடாளுமன்றத்திற்கு அதிகாரமளிக்கும் அரசியலமைப்பு உறுப்பு எது?",
         ("Article 138", "உறுப்பு 138", "Article 139", "உறுப்பு 139", "Article 140", "உறுப்பு 140", "Article 141", "உறுப்பு 141"),
         "A",
         "Article 138 empowers Parliament by law to enlarge the jurisdiction of the Supreme Court with respect to matters in the Union List or by special agreement with States.",
         "ஒன்றியப் பட்டியலில் உள்ள விவகாரங்கள் தொடர்பாக உச்ச நீதிமன்றத்தின் அதிகார வரம்பை சட்டத்தின் மூலம் விரிவாக்கம் செய்ய நாடாளுமன்றத்திற்கு உறுப்பு 138 அதிகாரமளிக்கிறது.",
         ("Art 138 = Enlargement of SC Jurisdiction by Parliament.", "உறுப்பு 138 = நாடாளுமன்றத்தால் SC அதிகார வரம்பு விரிவாக்கம்.", "Art 139 = Conferment of powers to issue certain writs.", "உறுப்பு 139 = குறிப்பிட்ட பேராணைகள் வழங்கும் அதிகாரம்.", "Art 140 = Ancillary powers of Supreme Court.", "உறுப்பு 140 = உச்ச நீதிமன்ற துணை அதிகாரங்கள்.", "Art 141 = Law declared by SC binding.", "உறுப்பு 141 = SC சட்டம் அனைவரையும் கட்டுப்படுத்தும்."),
         "Confusing Article 138 (Enlargement of SC Jurisdiction) with Article 139 (Conferment of additional Writ Powers).", "உறுப்பு 138 (அதிகார வரம்பு விரிவாக்கம்) மற்றும் உறுப்பு 139 (பேராணை அதிகாரம் வழங்குதல்) ஆகியவற்றை குழப்புவது.", "Enlargement of SC Jurisdiction = Article 138.", "SC அதிகார வரம்பு விரிவாக்கம் = உறுப்பு 138.", "1"),

        ("POLITY_SC_MED_021", "Medium",
         "Under Article 139, Parliament may by law confer on the Supreme Court power to issue writs for purposes OTHER than Fundamental Rights. Has Parliament exercised this power?",
         "அடிப்படை உரிமைகள் தவிர பிற காரணங்களுக்கும் பேராணை பிறப்பிக்கும் அதிகாரத்தை SC-க்கு வழங்க நாடாளுமன்றத்திற்கு உறுப்பு 139 வழிவகை செய்கிறது. நாடாளுமன்றம் இந்த அதிகாரத்தைப் பயன்படுத்தியுள்ளதா?",
         ("Yes, Parliament passed a general Writ Act in 1952", "ஆம், 1952-ல் நாடாளுமன்றம் பொது பேராணைச் சட்டத்தை இயற்றியது", "No, Parliament has NOT enacted any general law exercising Article 139 to expand SC writ powers", "இல்லை, நாடாளுமன்றம் உறுப்பு 139-ன் கீழ் SC பேராணை அதிகாரத்தை விரிவுபடுத்த பொதுச் சட்டம் எதுவும் இயற்றவில்லை", "Yes, during the 42nd Amendment", "ஆம், 42-வது திருத்தத்தின் போது இயற்றியது", "Yes, through the Contempt of Courts Act 1971", "ஆம், 1971 நீதிமன்ற அவமதிப்புச் சட்டத்தின் மூலம் இயற்றியது"),
         "B",
         "Although Article 139 allows Parliament to empower SC to issue writs for other purposes, Parliament has not enacted a general law under Article 139. Thus, Art 32 remains limited to Fundamental Rights.",
         "உறுப்பு 139 நாடாளுமன்றத்திற்கு வழிவகை செய்தாலும், நாடாளுமன்றம் இதுவரை SC-ன் பேராணை அதிகாரத்தை விரிவுபடுத்த பொதுச் சட்டம் எதுவும் இயற்றவில்லை.",
         ("No General Writ Act was passed in 1952.", "1952-ல் எந்த பேராணைச் சட்டமும் இயற்றப்படவில்லை.", "Parliament has NOT passed a general law under Article 139.", "நாடாளுமன்றம் உறுப்பு 139-ன் கீழ் பொதுச் சட்டம் இயற்றவில்லை.", "42nd Amendment did not exercise Art 139.", "42-வது திருத்தம் உறுப்பு 139-ஐப் பயன்படுத்தவில்லை.", "Contempt Act is under Art 129/215, not Art 139.", "அவமதிப்புச் சட்டம் உறுப்பு 129/215 சார்ந்தது."),
         "Assuming Parliament has already expanded SC writ jurisdiction to cover ordinary legal rights under Article 139.", "நாடாளுமன்றம் ஏற்கனவே SC பேராணை அதிகாரத்தை விரிவுபடுத்திவிட்டது எனக் கருதுவது.", "Article 139 = Enables Parliament to confer additional writ powers (not yet exercised generally).", "உறுப்பு 139 = கூடுதல் பேராணை அதிகாரம் வழங்க நாடாளுமன்றத்திற்கு வழிவகை செய்கிறது (பொதுவாகப் பயன்படுத்தப்படவில்லை).", "1"),

        ("POLITY_SC_MED_022", "Medium",
         "Which Article deals with 'Ancillary powers of Supreme Court' enabling Parliament to make provisions for supplementing SC powers?",
         "உச்ச நீதிமன்றத்தின் அதிகாரங்களை நிறைவு செய்ய நாடாளுமன்றம் துணை விவாதங்களை இயற்ற வழிவகை செய்யும் 'துணை அதிகாரங்கள்' (Ancillary Powers) பற்றிய உறுப்பு எது?",
         ("Article 139", "உறுப்பு 139", "Article 140", "உறுப்பு 140", "Article 141", "உறுப்பு 141", "Article 142", "உறுப்பு 142"),
         "B",
         "Article 140 states that Parliament may by law make provision for conferring upon the Supreme Court such supplemental/ancillary powers as may appear necessary.",
         "உச்ச நீதிமன்றம் தனது அதிகார வரம்பை பயனுள்ள வகையில் பயன்படுத்தத் தேவையான துணை அதிகாரங்களை நாடாளுமன்றம் சட்டத்தால் வழங்க உறுப்பு 140 வழிவகை செய்கிறது.",
         ("Art 139 is Writ power expansion.", "உறுப்பு 139 பேராணை அதிகாரம் விரிவாக்கம்.", "Art 140 = Ancillary Powers of Supreme Court.", "உறுப்பு 140 = உச்ச நீதிமன்ற துணை அதிகாரங்கள்.", "Art 141 = Binding law.", "உறுப்பு 141 = கட்டாயச் சட்டம்.", "Art 142 = Complete justice.", "உறுப்பு 142 = முழுமையான நீதி."),
         "Confusing Article 140 (Ancillary powers) with Article 142 (Complete justice enforcement).", "உறுப்பு 140 (துணை அதிகாரங்கள்) மற்றும் உறுப்பு 142 (முழுமையான நீதி) ஆகியவற்றை குழப்புவது.", "Ancillary Powers = Article 140.", "துணை அதிகாரங்கள் = உறுப்பு 140.", "1"),

        ("POLITY_SC_MED_023", "Medium",
         "In which case did the Supreme Court lay down guidelines for Public Interest Litigation (PIL) and entertain letters/postcards as writ petitions?",
         "எந்த வழக்கில் உச்ச நீதிமன்றம் பொது நல வழக்குகளுக்கான (PIL) வழிகாட்டுதல்களை வழங்கி, கடிதங்கள்/அஞ்சல் அட்டைகளை பேராணை மனுக்களாக ஏற்றுக்கொண்டது?",
         ("SP Gupta v. Union of India (First Judges Case, 1981)", "எஸ்.பி. குப்தா vs இந்திய ஒன்றியம் (1981)", "Hussainara Khatoon v. Home Secretary, State of Bihar (1979)", "ஹுசைனாரா கத்தூன் vs பீகார் உள்துறைச் செயலாளர் (1979)", "Kesavananda Bharati v. State of Kerala (1973)", "கேசவாநந்த பாரதி vs கேரளா மாநிலம் (1973)", "Golaknath v. State of Punjab (1967)", "கோலக்நாத் vs பஞ்சாப் மாநிலம் (1967)"),
         "B",
         "In *Hussainara Khatoon (1979)* (speedy trial for undertrials) and *SP Gupta (1981)*, Justice P. N. Bhagwati and Justice V. R. Krishna Iyer pioneered PIL in India, relaxing the rule of 'Locus Standi'.",
         "ஹுசைனாரா கத்தூன் (1979) மற்றும் எஸ்.பி. குப்தா (1981) வழக்குகளில் நீதிபதி பி.என். பகவதி மற்றும் வி.ஆர். கிருஷ்ணய்யர் எபிஸ்டோலரி ஆதிக்கத்தின் (Epistolary Jurisdiction) மூலம் PIL-ஐத் தொடங்கினர்.",
         ("SP Gupta expanded Locus Standi for public-spirited citizens.", "எஸ்.பி. குப்தா வழக்கு பொதுநல குடிமக்களுக்கான Locus Standi-ஐ விரிவுபடுத்தியது.", "Hussainara Khatoon (1979) was the FIRST recognized PIL case (speedy trial of undertrials).", "ஹுசைனாரா கத்தூன் (1979) முதல் அங்கீகரிக்கப்பட்ட PIL வழக்கு.", "Kesavananda Bharati dealt with Basic Structure.", "கேசவாநந்த பாரதி அடிப்படை அமைப்பு பற்றியது.", "Golaknath dealt with Fundamental Rights amendment restriction.", "கோலக்நாத் அடிப்படை உரிமை திருத்தக் கட்டுப்பாடு பற்றியது."),
         "Confusing the fathers of PIL (Justice P.N. Bhagwati & V.R. Krishna Iyer) and first PIL case (Hussainara Khatoon 1979).", "PIL-ன் தந்தையர்கள் மற்றும் முதல் PIL வழக்கைக் (1979) குழப்புவது.", "First PIL Case = Hussainara Khatoon (1979). Key PIL Pioneers = Justice P.N. Bhagwati & V.R. Krishna Iyer.", "முதல் PIL வழக்கு = ஹுசைனாரா கத்தூன் (1979). PIL முன்னோடிகள் = நீதிபதிகள் பி.என். பகவதி & வி.ஆர். கிருஷ்ணய்யர்.", "1"),

        ("POLITY_SC_MED_024", "Medium",
         "What traditional legal principle was relaxed by the Supreme Court to introduce Public Interest Litigation (PIL)?",
         "பொது நல வழக்கினை (PIL) அறிமுகப்படுத்த உச்ச நீதிமன்றத்தால் தளர்த்தப்பட்ட பாரம்பரிய சட்டக் கோட்பாடு எது?",
         ("Principle of Res Judicata", "Res Judicata கோட்பாடு", "Principle of Locus Standi (right to standing)", "Locus Standi கோட்பாடு (பாதிக்கப்பட்டவர் மட்டுமே வழக்கு தொடரும் உரிமை)", "Principle of Double Jeopardy", "இரட்டை ஆபத்துத் தடை கோட்பாடு", "Principle of Natural Justice", "இயற்கை நீதி கோட்பாடு"),
         "B",
         "Traditional jurisprudence mandated 'Locus Standi' (only an aggrieved person whose rights were directly violated could file a petition). SC relaxed this to allow any public-spirited citizen/organization to approach the court on behalf of oppressed persons.",
         "பாரம்பரியமாக 'Locus Standi' (பாதிக்கப்பட்டவர் மட்டுமே மனு தாக்கல் செய்ய முடியும்) என்ற விதி இருந்தது. ஒடுக்கப்பட்டோருக்காகப் பொதுநல உணர்வுள்ள எவரும் வழக்கு தொடர உச்ச நீதிமன்றம் இவ்விதியைத் தளர்த்தியது.",
         ("Res Judicata prevents re-litigation of decided disputes.", "Res Judicata மீண்டும் வழக்கு தொடர்வதைத் தடுக்கிறது.", "Locus Standi relaxation is the core foundation of PIL.", "Locus Standi தளர்வே PIL-ன் முக்கிய அடித்தளமாகும்.", "Double Jeopardy protects against multiple trials for same offence.", "இரட்டை ஆபத்துத் தடை ஒரே குற்றத்திற்கு பல விசாரணைகளைத் தடுக்கிறது.", "Natural Justice ensures fair hearing.", "இயற்கை நீதி நியாயமான விசாரணையை உறுதி செய்கிறது."),
         "Confusing Locus Standi (standing in court) with Res Judicata (final judgment bar).", "Locus Standi மற்றும் Res Judicata ஆகியவற்றைக் குழப்புவது.", "PIL Foundation = Relaxation of the Traditional Rule of LOCUS STANDI.", "PIL அடித்தளம் = Locus Standi விதியைத் தளர்த்துவது.", "1"),

        ("POLITY_SC_MED_025", "Medium",
         "Which landmark judgement of the Supreme Court introduced the concept of 'Prospective Overruling'?",
         "உச்ச நீதிமன்றத்தின் எந்த முக்கியத் தீர்ப்பு 'எதிர்காலக் கட்டுப்பாட்டுடன் கூடிய ரத்து' (Prospective Overruling) என்ற கருத்தை அறிமுகப்படுத்தியது?",
         ("Golaknath v. State of Punjab (1967)", "கோலக்நாத் vs பஞ்சாப் மாநிலம் (1967)", "Kesavananda Bharati v. State of Kerala (1973)", "கேசவாநந்த பாரதி vs கேரளா மாநிலம் (1973)", "Minerva Mills v. Union of India (1980)", "மினர்வா மில்ஸ் vs இந்திய ஒன்றியம் (1980)", "AK Gopalan v. State of Madras (1950)", "ஏ.கே. கோபாலன் vs மெட்ராஸ் மாநிலம் (1950)"),
         "A",
         "In *Golaknath Case (1967)*, Chief Justice K. Subba Rao applied the doctrine of Prospective Overruling, holding that parliament cannot amend Fundamental Rights, but this ruling would apply only prospectively (future legislation) without invalidating past constitutional amendments.",
         "1967 கோலக்நாத் வழக்கில், தலைமை நீதிபதி கே. சுப்பா ராவ் Prospective Overruling கோட்பாட்டைப் பயன்படுத்தி, இத்தீர்ப்பு எதிர்காலச் சட்டங்களுக்கு மட்டுமே பொருந்தும், கடந்தகாலத் திருத்தங்களைச் செல்லாததாக்காது எனக் கூறினார்.",
         ("Golaknath Case (1967) introduced Prospective Overruling in India.", "கோலக்நாத் வழக்கு (1967) Prospective Overruling-ஐ அறிமுகப்படுத்தியது.", "Kesavananda Bharati introduced Basic Structure.", "கேசவாநந்த பாரதி அடிப்படை அமைப்பை அறிமுகப்படுத்தியது.", "Minerva Mills reinforced balance between Part III & Part IV.", "மினர்வா மில்ஸ் பகுதி III & IV சமநிலையை வலுப்படுத்தியது.", "AK Gopalan gave narrow interpretation of Procedure Established by Law.", "ஏ.கே. கோபாலன் சட்டத்தால் அமைக்கப்பட்ட நடைமுறைக்கு குறுகிய விளக்கம் அளித்தது."),
         "Associating Prospective Overruling with Kesavananda Bharati instead of Golaknath (1967).", "Prospective Overruling கோட்பாட்டை கோலக்நாத் வழக்குக்கு (1967) பதிலாக கேசவாநந்த பாரதியுடன் இணைப்பது.", "Doctrine of Prospective Overruling = Golaknath Case (1967).", "Prospective Overruling கோட்பாடு = கோலக்நாத் வழக்கு (1967).", "1"),

        ("POLITY_SC_MED_026", "Medium",
         "In which landmark case did the Supreme Court expand the scope of 'Procedure Established by Law' in Article 21 to include 'Due Process of Law' (just, fair, and reasonable)?",
         "உறுப்பு 21-ல் உள்ள 'சட்டத்தால் அமைக்கப்பட்ட நடைமுறை' என்பதை 'நீதியான, நியாயமான மற்றும் பகுத்தறிவுள்ள நடைமுறையாக' (Due Process of Law) விரிவுபடுத்திய SC வழக்கு எது?",
         ("AK Gopalan Case (1950)", "ஏ.கே. கோபாலன் வழக்கு (1950)", "Maneka Gandhi v. Union of India (1978)", "மேனகா காந்தி vs இந்திய ஒன்றியம் (1978)", "Shankar Prasad Case (1951)", "சங்கரி பிரசாத் வழக்கு (1951)", "Sajjan Singh Case (1965)", "சஜ்ஜன் சிங் வழக்கு (1965)"),
         "B",
         "In *Maneka Gandhi Case (1978)*, the SC overruled AK Gopalan (1950) narrow interpretation and held that any procedure depriving life/personal liberty under Art 21 must not be arbitrary, but just, fair, and reasonable (incorporating American Due Process).",
         "1978 மேனகா காந்தி வழக்கில், உறுப்பு 21-ன் கீழ் தனிநபர் சுதந்திரத்தைப் பறிக்கும் நடைமுறை தன்னிச்சையானதாக இருக்கக்கூடாது; அது நீதியானதாக, நியாயமானதாக இருக்க வேண்டும் (Due Process) என SC தீர்ப்பளித்தது.",
         ("AK Gopalan 1950 took a narrow, literal view of Art 21.", "ஏ.கே. கோபாலன் வழக்கு உறுப்பு 21-க்கு குறுகிய விளக்கம் அளித்தது.", "Maneka Gandhi 1978 incorporated 'Due Process' (just, fair, and reasonable procedure).", "மேனகா காந்தி வழக்கு (1978) 'Due Process' கோட்பாட்டை உள்ளடக்கியது.", "Shankari Prasad upheld 1st Amendment.", "சங்கரி பிரசாத் 1-வது திருத்தத்தை உறுதி செய்தது.", "Sajjan Singh upheld 17th Amendment.", "சஜ்ஜன் சிங் 17-வது திருத்தத்தை உறுதி செய்தது."),
         "Confusing AK Gopalan Case 1950 (narrow view) with Maneka Gandhi Case 1978 (wide Due Process view).", "ஏ.கே. கோபாலன் (குறுகிய பார்வை) மற்றும் மேனகா காந்தி (பரந்த Due Process பார்வை) வழக்குகளைக் குழப்புவது.", "Article 21 Expanded to 'Due Process' = Maneka Gandhi Case (1978).", "உறுப்பு 21 'Due Process' ஆக விரிவுபடுத்தப்பட்டது = மேனகா காந்தி வழக்கு (1978).", "1"),

        ("POLITY_SC_MED_027", "Medium",
         "In which case did a 9-judge bench of the Supreme Court unanimously declare the Right to Privacy as a Fundamental Right under Article 21?",
         "எந்த வழக்கில் 9 நீதிபதிகள் கொண்ட உச்ச நீதிமன்ற அமர்வு 'தனிமனித இரகசிய உரிமையை' (Right to Privacy) உறுப்பு 21-ன் கீழ் அடிப்படை உரிமையாக ஒருமனதாக அறிவித்தது?",
         ("Justice K. S. Puttaswamy v. Union of India (2017)", "நீதிபதி கே. எஸ். புட்டசாமி vs இந்திய ஒன்றியம் (2017)", "Navtej Singh Johar v. Union of India (2018)", "நவ்தேஜ் சிங் ஜோஹர் vs இந்திய ஒன்றியம் (2018)", "Shayara Bano v. Union of India (2017)", "ஷாயரா பானோ vs இந்திய ஒன்றியம் (2017)", "Joseph Shine v. Union of India (2018)", "ஜோசப் ஷைன் vs இந்திய ஒன்றியம் (2018)"),
         "A",
         "In *KS Puttaswamy Case (2017)*, a 9-judge Constitution Bench overruled M.P. Sharma (1954) and Kharak Singh (1962), holding Right to Privacy as an intrinsic part of Right to Life and Personal Liberty under Article 21.",
         "2017 கே.எஸ். புட்டசாமி வழக்கில், 9 நீதிபதிகள் கொண்ட அமர்வு தனிமனித இரகசிய உரிமையை (Right to Privacy) உறுப்பு 21-ன் கீழ் ஒரு அடிப்படை உரிமையாக ஒருமனதாக அறிவித்தது.",
         ("KS Puttaswamy Case (2017) = Right to Privacy as Fundamental Right.", "கே.எஸ். புட்டசாமி வழக்கு (2017) = தனிமனித இரகசிய உரிமை அடிப்படை உரிமை.", "Navtej Johar decriminilised Sec 377 IPC.", "நவ்தேஜ் ஜோஹர் பிரிவு 377 IPC-ஐ குற்றமற்றதாக்கியது.", "Shayara Bano struck down Instant Triple Talaq.", "ஷாயரா பானோ முத்தலாக் முறையை ரத்து செய்தது.", "Joseph Shine struck down Adultery law (Sec 497 IPC).", "ஜோசப் ஷைன் சோரம்போக்குச் சட்டத்தை (பிரிவு 497) ரத்து செய்தது."),
         "Confusing landmark modern judgments: Puttaswamy (Privacy), Johar (377), Shayara Bano (Triple Talaq), Joseph Shine (Adultery).", "புட்டசாமி (இரக்கசியம்), ஜோஹர் (377), ஷாயரா பானோ (முத்தலாக்), ஜோசப் ஷைன் (சோரம்போக்கு) ஆகிய வழக்குகளைக் குழப்புவது.", "Right to Privacy = Justice K. S. Puttaswamy Case (2017) (9-Judge Bench).", "தனிமனித இரகசிய உரிமை = நீதிபதி கே. எஸ். புட்டசாமி வழக்கு (2017) (9-நீதிபதிகள் அமர்வு).", "1"),

        ("POLITY_SC_MED_028", "Medium",
         "Which Article of the Constitution gives the Supreme Court the power to grant leave to appeal against any judgment of a High Court involving a 'substantial question of law as to the interpretation of the Constitution'?",
         "அரசியலமைப்பு விளக்கமளித்தல் குறித்த முக்கிய சட்டக் கேள்வி அடங்கிய உயர் நீதிமன்ற தீர்ப்பிற்கு எதிராக மேல்முறையீடு செய்ய வழிவகை செய்யும் உறுப்பு எது?",
         ("Article 132", "உறுப்பு 132", "Article 133", "உறுப்பு 133", "Article 134", "உறுப்பு 134", "Article 135", "உறுப்பு 135"),
         "A",
         "Article 132 provides for Appellate Jurisdiction of the Supreme Court in appeals from High Courts in constitutional matters (where High Court certifies under Art 134A that a substantial question of law as to constitutional interpretation is involved).",
         "உயர் நீதிமன்றத் தீர்ப்பில் அரசியலமைப்பு விளக்கமளித்தல் குறித்த முக்கிய சட்டக் கேள்வி உள்ளது எனச் சான்றளிக்கப்பட்டால், உச்ச நீதிமன்றத்தில் மேல்முறையீடு செய்ய உறுப்பு 132 வழிவகை செய்கிறது.",
         ("Art 132 = Constitutional Appellate Jurisdiction.", "உறுப்பு 132 = அரசியலமைப்பு மேல்முறையீட்டு ஆதிக்கம்.", "Art 133 = Civil Appellate Jurisdiction.", "உறுப்பு 133 = சிவில் மேல்முறையீட்டு ஆதிக்கம்.", "Art 134 = Criminal Appellate Jurisdiction.", "உறுப்பு 134 = குற்றவியல் மேல்முறையீட்டு ஆதிக்கம்.", "Art 135 = Continuation of Federal Court powers.", "உறுப்பு 135 = கூட்டாட்சி நீதிமன்ற அதிகாரத் தொடர்ச்சி."),
         "Confusing Article 132 (Constitutional appeals) with Article 133 (Civil appeals) or Article 134 (Criminal appeals).", "உறுப்பு 132 (அரசியலமைப்பு), உறுப்பு 133 (சிவில்), உறுப்பு 134 (குற்றவியல்) ஆகியவற்றை குழப்புவது.", "Constitutional Appeals = Article 132.", "அரசியலமைப்பு மேல்முறையீடுகள் = உறுப்பு 132.", "1"),

        ("POLITY_SC_MED_029", "Medium",
         "Which Article was inserted by the 44th Amendment Act 1978 to streamline the procedure for High Courts issuing certificates of fitness for appeal to the Supreme Court?",
         "உச்ச நீதிமன்ற மேல்முறையீட்டுக்கான தகுதிச் சான்றிதழை உயர் நீதிமன்றங்கள் வழங்குவதைச் சீரமைக்க 44-வது திருத்தச் சட்டம் (1978) மூலம் சேர்க்கப்பட்ட உறுப்பு எது?",
         ("Article 134A", "உறுப்பு 134A", "Article 139A", "உறுப்பு 139A", "Article 144A", "உறுப்பு 144A", "Article 145A", "உறுப்பு 145A"),
         "A",
         "Article 134A was inserted by the 44th Constitutional Amendment Act, 1978. It allows the High Court to determine, on its own motion or oral application, whether a certificate of fitness for appeal to SC under Art 132, 133, or 134 should be granted.",
         "44-வது திருத்தச் சட்டம் (1978) மூலம் சேர்க்கப்பட்ட உறுப்பு 134A, மேல்முறையீட்டுச் சான்றிதழை உயர் நீதிமன்றம் தன்னிச்சையாகவோ அல்லது வாய்மொழி மனு பேபிலோ தீர்மானிக்க வழிவகை செய்கிறது.",
         ("Art 134A = Certificate for appeal to Supreme Court.", "உறுப்பு 134A = உச்ச நீதிமன்ற மேல்முறையீட்டுச் சான்றிதழ்.", "Art 139A = Transfer of cases.", "உறுப்பு 139A = வழக்குகள் மாற்றம்.", "Art 144A was inserted by 42nd Amendment and repealed by 43rd Amendment.", "உறுப்பு 144A 42-வது திருத்தத்தால் சேர்க்கப்பட்டு 43-வது திருத்தத்தால் நீக்கப்பட்டது.", "Art 145A is incorrect.", "உறுப்பு 145A தவறானது."),
         "Confusing Article 134A (Certificate of fitness for appeal) with Article 139A (Transfer of cases).", "உறுப்பு 134A (சான்றிதழ்) மற்றும் உறுப்பு 139A (வழக்கு மாற்றம்) ஆகியவற்றை குழப்புவது.", "Certificate for Appeal to SC = Article 134A (Added by 44th Amendment 1978).", "SC மேல்முறையீட்டுச் சான்றிதழ் = உறுப்பு 134A (44-வது திருத்தம் 1978 மூலம் சேர்க்கப்பட்டது).", "1"),

        ("POLITY_SC_MED_030", "Medium",
         "Can a private individual institute criminal contempt proceedings directly in the Supreme Court without any prior consent?",
         "ஒரு தனிநபர் எந்தவொரு முன்அனுமதியும் இன்றி நேரடியாக உச்ச நீதிமன்றத்தில் குற்றவியல் அவமதிப்பு வழக்கைத் தொடர முடியுமா?",
         ("Yes, any citizen can institute criminal contempt directly anytime", "ஆம், எந்தவொரு குடிமகனும் எப்போது வேண்டுமானாலும் நேரடியாகத் தொடரலாம்", "No, written consent of Attorney General or Solicitor General is mandatory for a private citizen", "இல்லை, தனிநபர் வழக்கு தொடர அட்டர்னி ஜெனரல் அல்லது சொலிசிட்டர் ஜெனரலின் எழுத்துப்பூர்வ ஒப்புதல் கட்டாயமாகும்", "Yes, provided the citizen deposits Rs. 50,000 security", "ஆம், ரூ. 50,000 பிணைத்தொகை செலுத்தினால் தொடரலாம்", "No, only the Union Home Minister can institute criminal contempt", "இல்லை, ஒன்றிய உள்துறை அமைச்சர் மட்டுமே தொடர முடியும்"),
         "B",
         "Under Section 15 of the Contempt of Courts Act 1971, a motion for criminal contempt brought by a private individual MUST have the written consent of the Attorney General or Solicitor General of India.",
         "1971 நீதிமன்ற அவமதிப்புச் சட்டத்தின் பிரிவு 15-ன் படி, ஒரு தனிநபர் குற்றவியல் அவமதிப்பு வழக்கு தொடர இந்திய அட்டர்னி ஜெனரல் அல்லது சொலிசிட்டர் ஜெனரலின் எழுத்துப்பூர்வ ஒப்புதல் கட்டாயமாகும்.",
         ("Direct unapproved private criminal contempt motion is barred.", "முன்அனுமதியற்ற தனிநபர் குற்றவியல் அவமதிப்பு வழக்கு தடை செய்யப்பட்டுள்ளது.", "Written consent of AG or SG is mandatory for private criminal contempt petition under Sec 15 Contempt Act.", "அட்டர்னி ஜெனரல்/சொலிசிட்டர் ஜெனரல் எழுத்துப்பூர்வ ஒப்புதல் கட்டாயமாகும்.", "Security deposit does not bypass AG consent requirement.", "பிணைத்தொகை அட்டர்னி ஜெனரல் ஒப்புதலை மாற்றாது.", "Home Minister has no statutory role under Contempt Act.", "உள்துறை அமைச்சருக்கு இதில் அதிகாரமில்லை."),
         "Assuming anyone can file criminal contempt against anyone without restriction (AG consent acts as a constitutional filter against frivolous litigation).", "யார் வேண்டுமானாலும் எவர் மீதும் அவமதிப்பு வழக்கு தொடரலாம் என நினைப்பது.", "Private Criminal Contempt Petition = Mandatory Written Consent of Attorney General or Solicitor General.", "தனிநபர் குற்றவியல் அவமதிப்பு மனு = அட்டர்னி ஜெனரல் அல்லது சொலிசிட்டர் ஜெனரலின் கட்டாய ஒப்புதல்.", "1"),

        ("POLITY_SC_MED_031", "Medium",
         "In which landmark case did the Supreme Court rule that Judicial Review is a 'Basic Feature' of the Constitution which cannot be abrogated even by Constitutional Amendment?",
         "நீதித்துறை சீராய்வு (Judicial Review) என்பது அரசியலமைப்பின் 'அடிப்படை அம்சம்' (Basic Feature) என்பதால் அரசியலமைப்பு திருத்தத்தாலும் அதை நீக்க முடியாது எனத் தீர்ப்பளிக்கப்பட்ட வழக்கு எது?",
         ("Minerva Mills v. Union of India (1980)", "மினர்வா மில்ஸ் vs இந்திய ஒன்றியம் (1980)", "Golaknath Case (1967)", "கோலக்நாத் வழக்கு (1967)", "Sankari Prasad Case (1951)", "சங்கரி பிரசாத் வழக்கு (1951)", "Champakam Dorairajan Case (1951)", "செண்பகம் துரைராஜன் வழக்கு (1951)"),
         "A",
         "In *Minerva Mills (1980)*, the SC struck down clauses (4) and (5) of Article 368 (inserted by 42nd Amendment to exclude judicial review of constitutional amendments), holding Judicial Review as part of the Basic Structure.",
         "1980 மினர்வா மில்ஸ் வழக்கில், அரசியலமைப்புத் திருத்தங்கள் மீதான நீதித்துறை சீராய்வைத் தடை செய்த 42-வது திருத்தத்தின் பிரிவுகளை ரத்து செய்து, நீதித்துறை சீராய்வு அடிப்படை அம்சம் என SC தீர்ப்பளித்தது.",
         ("Minerva Mills (1980) held Judicial Review as a Basic Feature.", "மினர்வா மில்ஸ் (1980) நீதித்துறை சீராய்வை அடிப்படை அம்சம் என அறிவித்தது.", "Golaknath held FRs non-amendable.", "கோலக்நாத் வழக்கு அடிப்படை உரிமைகளை திருத்த முடியாது என்றது.", "Sankari Prasad allowed FR amendments.", "சங்கரி பிரசாத் திருத்தங்களை அனுமதித்தது.", "Champakam Dorairajan led to 1st Amendment.", "செண்பகம் துரைராஜன் 1-வது திருத்தத்திற்கு வழிவகுத்தது."),
         "Confusing Kesavananda Bharati (origin of Basic Structure) with Minerva Mills 1980 (striking down 42nd Amendment clauses barring Judicial Review).", "கேசவாநந்த பாரதி (அடிப்படை அமைப்பு தொடக்கம்) மற்றும் மினர்வா மில்ஸ் 1980 (நீதித்துறை சீராய்வு பாதுகாப்பு) ஆகியவற்றை குழப்புவது.", "Judicial Review as Basic Feature = Minerva Mills Case (1980) & Chandra Kumar Case (1997).", "நீதித்துறை சீராய்வு அடிப்படை அம்சம் = மினர்வா மில்ஸ் வழக்கு (1980).", "1"),

        ("POLITY_SC_MED_032", "Medium",
         "In *L. Chandra Kumar v. Union of India (1997)*, what significant ruling did the Supreme Court deliver regarding Tribunals and High Court/SC Judicial Review?",
         "1997 எல். சந்திரகுமார் வழக்கில், தீர்ப்பாயங்கள் மற்றும் உயர்/உச்ச நீதிமன்றங்களின் நீதித்துறை சீராய்வு குறித்து வழங்கப்பட்ட முக்கியத் தீர்ப்பு எது?",
         ("Power of Judicial Review of High Courts under Art 226/227 is part of Basic Structure; tribunal decisions are subject to HC scrutiny", "உறுப்பு 226/227-ன் கீழ் உயர் நீதிமன்றங்களின் நீதித்துறை சீராய்வு அதிகாரம் அடிப்படை அம்சமாகும்; தீர்ப்பாய முடிவுகள் HC சீராய்வுக்கு உட்பட்டவை", "Tribunals are superior to High Courts in administrative matters", "நிர்வாக விவகாரங்களில் தீர்ப்பாயங்கள் உயர் நீதிமன்றங்களை விட மேலானவை", "High Courts have no jurisdiction over CAT or SAT", "CAT அல்லது SAT மீது உயர் நீதிமன்றங்களுக்கு அதிகார வரம்பு இல்லை", "Supreme Court alone can hear tribunal appeals, completely bypassing High Courts", "உயர் நீதிமன்றங்களை முற்றிலும் தவிர்த்து உச்ச நீதிமன்றம் மட்டுமே தீர்ப்பாய மேல்முறையீடுகளை விசாரிக்கும்"),
         "A",
         "In *L. Chandra Kumar (1997)*, a 7-judge bench declared that writ jurisdiction of HCs under Art 226/227 and SC under Art 32 is part of Basic Structure. Litigants MUST first approach the Division Bench of High Court against Tribunal decisions before coming to SC.",
         "1997 எல். சந்திரகுமார் வழக்கில், உறுப்பு 226/227 மற்றும் 32 ஆகியவற்றுக்குட்பட்ட நீதித்துறை சீராய்வு அடிப்படை அமைப்பாகும் என்றும், தீர்ப்பாய முடிவுகளுக்கு எதிராக முதலில் உயர் நீதிமன்றத்தையே அணுக வேண்டும் என்றும் 7-நீதிபதிகள் அமர்வு தீர்ப்பளித்தது.",
         ("L. Chandra Kumar (1997) affirmed HC Art 226/227 power over tribunals as Basic Structure.", "சந்திரகுமார் வழக்கு தீர்ப்பாயங்கள் மீது உயர் நீதிமன்ற சீராய்வு அதிகாரத்தை அடிப்படை அம்சம் என உறுதி செய்தது.", "Tribunals are not superior to High Courts.", "தீர்ப்பாயங்கள் உயர் நீதிமன்றங்களை விட மேலானவை அல்ல.", "High Courts DO have jurisdiction over CAT/SAT.", "உயர் நீதிமன்றங்களுக்கு CAT/SAT மீது அதிகாரம் உண்டு.", "Direct SC appeal bypassing HC was struck down in Chandra Kumar case.", "HC-ஐ தவிர்த்து நேரடியாக SC செல்லும் முறை ரத்து செய்யப்பட்டது."),
         "Thinking decisions of Administrative Tribunals (CAT) can be appealed directly to Supreme Court, bypassing High Courts (Chandra Kumar case mandated going through High Court Division Bench first).", "தீர்ப்பாய முடிவுகளை உயர் நீதிமன்றத்தைத் தவிர்த்து நேரடியாக உச்ச நீதிமன்றத்தில் மேல்முறையீடு செய்யலாம் என நினைப்பது.", "Tribunal Appeals Path = Tribunal -> High Court Division Bench -> Supreme Court (L. Chandra Kumar 1997).", "தீர்ப்பாய மேல்முறையீட்டுப் பாதை = தீர்ப்பாயம் -> உயர் நீதிமன்றப் பிரிவு அமர்வு -> உச்ச நீதிமன்றம் (1997).", "1"),

        ("POLITY_SC_MED_033", "Medium",
         "Under Article 124(2), who is constitutionally required to be consulted by the President when appointing a Judge of the Supreme Court (other than Chief Justice)?",
         "உறுப்பு 124(2)-ன் படி, உச்ச நீதிமன்ற நீதிபதியை (தலைமை நீதிபதி தவிர்த்து) நியமிக்கும்போது குடியரசுத் தலைவர் யாருடன் கலந்தாலோசிப்பது கட்டாயமாகும்?",
         ("Chief Justice of India always", "எப்போதும் இந்தியத் தலைமை நீதிபதியுடன்", "Union Law Minister only", "ஒன்றிய சட்ட அமைச்சருடன் மட்டுமே", "Prime Minister of India only", "இந்தியப் பிரதமருடன் மட்டுமே", "Speaker of Lok Sabha", "மக்களவைத் தலைவருடன்"),
         "A",
         "Under Article 124(2) proviso, in the case of appointment of a Judge other than the Chief Justice, the Chief Justice of India shall ALWAYS be consulted.",
         "உறுப்பு 124(2) வரம்பின்படி, தலைமை நீதிபதி தவிர மற்ற நீதிபதிகளை நியமிக்கும் விஷயத்தில், இந்தியத் தலைமை நீதிபதியைக் கலந்தாலோசிப்பது எப்போதுமே கட்டாயமாகும்.",
         ("CJI consultation is mandatory for appointing other SC judges under Art 124(2).", "மற்ற நீதிபதிகளை நியமிக்க CJI-யைக் கலந்தாலோசிப்பது கட்டாயமாகும்.", "Law Minister consultation is an executive process, but text specifies CJI.", "சட்ட அமைச்சர் கலந்தாலோசனை உரைச் சொல் அல்ல.", "PM is executive head, text specifies CJI.", "பிரதமர் உரைச் சொல் அல்ல.", "Speaker has no role in appointments.", "சபாநாயகருக்குப் பங்கில்லை."),
         "Confusing optional executive consultation with mandatory consultation of the Chief Justice of India under Art 124(2).", "விருப்பக் கலந்தாலோசனை மற்றும் கட்டாயத் தலைமை நீதிபதி கலந்தாலோசனையைக் குழப்புவது.", "Mandatory Consultation for SC Judge Appointment = Chief Justice of India.", "கட்டாயக் கலந்தாலோசனை = இந்தியத் தலைமை நீதிபதி.", "1"),

        ("POLITY_SC_MED_034", "Medium",
         "Which Article of the Constitution lays down the provision for 'Attendance of retired Judges at sittings of the Supreme Court'?",
         "உச்ச நீதிமன்ற அமர்வுகளில் 'ஓய்வு பெற்ற நீதிபதிகளின் வருகை' பற்றிய விதியைக் கூறும் அரசியலமைப்பு உறுப்பு எது?",
         ("Article 126", "உறுப்பு 126", "Article 127", "உறுப்பு 127", "Article 128", "உறுப்பு 128", "Article 129", "உறுப்பு 129"),
         "C",
         "Article 128 provides for the attendance of retired Supreme Court or Federal Court judges at sittings of the Supreme Court upon request by CJI with President's consent.",
         "உறுப்பு 128 குடியரசுத் தலைவர் அனுமதியுடன் CJI கோரிக்கையின் பேரில் ஓய்வு பெற்ற நீதிபதிகள் உச்ச நீதிமன்ற அமர்வுகளில் கலந்துகொள்வதைப் பற்றிக் கூறுகிறது.",
         ("Art 126 is Acting CJI.", "உறுப்பு 126 தற்காலிக CJI.", "Art 127 is Ad hoc Judges.", "உறுப்பு 127 Ad hoc நீதிபதிகள்.", "Art 128 = Attendance of Retired Judges at SC sittings.", "உறுப்பு 128 = ஓய்வு பெற்ற நீதிபதிகளின் வருகை.", "Art 129 is Court of Record.", "உறுப்பு 129 பதிவு நீதிமன்றம்."),
         "Confusing Article 127 (Ad hoc judges - sitting HC judges) with Article 128 (Retired judges).", "உறுப்பு 127 (Ad hoc - தற்போதைய HC நீதிபதி) மற்றும் உறுப்பு 128 (ஓய்வு பெற்ற நீதிபதி) ஆகியவற்றை குழப்புவது.", "Retired Judges Sitting = Article 128.", "ஓய்வு பெற்ற நீதிபதிகள் வருகை = உறுப்பு 128.", "1"),

        ("POLITY_SC_MED_035", "Medium",
         "Does a retired judge sitting and acting as an SC judge under Article 128 enjoy all the jurisdiction, powers, and privileges of a Supreme Court Judge?",
         "உறுப்பு 128-ன் கீழ் அமர்வில் கலந்துகொள்ளும் ஓய்வு பெற்ற நீதிபதி, உச்ச நீதிமன்ற நீதிபதியின் அனைத்து அதிகார வரம்புகள் மற்றும் சலுகைகளைப் பெறுவாரா?",
         ("Yes, while so sitting and acting, he has all jurisdiction, powers, and privileges of an SC judge, but is NOT deemed to be an SC judge", "ஆம், அவர் அமர்வில் இருக்கும் வரை அனைத்து அதிகாரங்களையும் சலுகைகளையும் பெறுவார், ஆனால் அவர் ஒரு புதிய SC நீதிபதியாகக் கருதப்பட மாட்டார்", "No, he acts only as an observer without voting or judgment rights", "இல்லை, அவர் எந்தத் தீர்ப்பும் வழங்க முடியாது", "Yes, and his retirement age is permanently extended to 70 years", "ஆம், அவரது ஓய்வு பெறும் வயது நிரந்தரமாக 70 ஆக உயர்த்தப்படும்", "No, he receives no allowances or salary during this period", "இல்லை, அவருக்கு எந்தப் படியோ ஊதியமோ வழங்கப்படாது"),
         "A",
         "Under Article 128 proviso, while sitting and acting, such a retired judge is entitled to allowances determined by the President and enjoys all powers/privileges of an SC judge, BUT shall NOT otherwise be deemed to be a Judge of the Supreme Court.",
         "உறுப்பு 128-ன் படி, அவர் அமர்வில் இருக்கும் வரை அனைத்து அதிகாரங்களையும் சலுகைகளையும் பெறுவார்; ஆனால் அவர் ஒரு நிரந்தர உச்ச நீதிமன்ற நீதிபதியாகக் கருதப்பட மாட்டார்.",
         ("Article 128 explicitly gives full powers/privileges while clarifying he is NOT deemed a regular judge.", "அமர்வில் இருக்கும் வரை அனைத்து அதிகாரங்களையும் அளிக்கிறது, ஆனால் நிரந்தர நீதிபதியாகக் கருதப்பட மாட்டார்.", "Observer only is incorrect.", "பார்வையாளர் மட்டுமே என்பது தவறு.", "Retirement age extension is incorrect.", "ஓய்வு வயது நீட்டிப்பு என்பது தவறு.", "Allowances are determined and paid by President order.", "குடியரசுத் தலைவர் ஆணையால் படிகள் வழங்கப்படுகின்றன."),
         "Assuming a retired judge recalled under Art 128 becomes a permanent SC judge again.", "மீண்டும் அழைக்கப்பட்ட ஓய்வு பெற்ற நீதிபதி நிரந்தர நீதிபதியாகிவிடுவார் எனக் கருதுவது.", "Article 128 Status = Enjoys all powers/privileges of SC judge, but NOT deemed a regular judge of SC.", "உறுப்பு 128 நிலை = அனைத்து அதிகாரங்களையும் அனுபவிப்பார், ஆனால் நிரந்தர நீதிபதியாகக் கருதப்பட மாட்டார்.", "1"),

        ("POLITY_SC_MED_036", "Medium",
         "What is the difference between 'Civil Contempt' and 'Criminal Contempt' under the Contempt of Courts Act 1971?",
         "1971 நீதிமன்ற அவமதிப்புச் சட்டத்தின் கீழ் 'சிவில் அவமதிப்பு' மற்றும் 'குற்றவியல் அவமதிப்பு' ஆகியவற்றிற்கு இடையேயான வேறுபாடு என்ன?",
         ("Civil contempt is willful disobedience to any judgment/order; Criminal contempt is publication or act scandalizing or lowering the authority of court", "சிவில் அவமதிப்பு என்பது தீர்ப்பு/உத்தரவை வேண்டுமென்றே மீறுதலாகும்; குற்றவியல் அவமதிப்பு என்பது நீதிமன்றத்தின் பெருமையைக் குறைக்கும் வகையில் செயல்படுதல்/வெளியிடுதலாகும்", "Civil contempt applies to High Courts; Criminal contempt applies to Supreme Court only", "சிவில் அவமதிப்பு HC-க்கும் குற்றவியல் அவமதிப்பு SC-க்கும் மட்டுமே பொருந்தும்", "Civil contempt carries death penalty; Criminal contempt carries fine only", "சிவில் அவமதிப்புக்கு மரண தண்டனையும் குற்றவியல் அவமதிப்புக்கு அபராதமும் வழங்கப்படும்", "There is no statutory distinction between Civil and Criminal Contempt in India", "இந்தியாவில் சிவில் மற்றும் குற்றவியல் அவமதிப்பு இடையே சட்டப்பூர்வ வேறுபாடு எதுவுமில்லை"),
         "A",
         "Under Sec 2 of Contempt of Courts Act 1971: Civil Contempt = Willful disobedience to court judgment/order/writ. Criminal Contempt = Publication/act which scandalizes court, prejudices judicial proceeding, or interferes with administration of justice.",
         "1971 சட்டத்தின் பிரிவு 2: சிவில் அவமதிப்பு = நீதிமன்ற உத்தரவை வேண்டுமென்றே மீறுவது. குற்றவியல் அவமதிப்பு = நீதிமன்றத்தின் பெருமையைக் குறைப்பது அல்லது நீதி நிர்வாகத்தில் தலையிடுவது.",
         ("Civil = Willful disobedience; Criminal = Scandalizing or interfering with administration of justice.", "சிவில் = உத்தரவை மீறுதல்; குற்றவியல் = பெருமையைக் குறைத்தல்/தலையிடுதல்.", "Both apply to SC and High Courts.", "இரண்டும் SC மற்றும் HC ஆகிய இரண்டிற்கும் பொருந்தும்.", "Death penalty is never awarded for contempt (max punishment is 6 months imprisonment).", "அவமதிப்புக்கு மரண தண்டனை வழங்கப்படுவதில்லை (அதிகபட்சம் 6 மாதங்கள் சிறை).", "Statutory distinction exists in 1971 Act.", "1971 சட்டத்தில் வேறுபாடு உள்ளது."),
         "Confusing Civil Contempt (willful disobedience of orders) with Criminal Contempt (scandalizing the court).", "சிவில் மற்றும் குற்றவியல் அவமதிப்பு வரைவிலக்கணங்களைக் குழப்புவது.", "Contempt Types = Civil (Willful Disobedience) vs Criminal (Scandalizing Court / Interfering with Justice).", "அவமதிப்பு வகைகள் = சிவில் (உத்தரவு மீறல்) vs குற்றவியல் (நீதிமன்ற பெருமையைக் குறைத்தல்).", "1"),

        ("POLITY_SC_MED_037", "Medium",
         "What is the MAXIMUM punishment prescribed for Contempt of Court under the Contempt of Courts Act 1971?",
         "1971 நீதிமன்ற அவமதிப்புச் சட்டத்தின் கீழ் நீதிமன்ற அவமதிப்புக்கு விதிக்கப்படும் அதிகபட்ச தண்டனை என்ன?",
         ("Simple imprisonment up to 6 months, or fine up to Rs. 2,000, or both", "6 மாதங்கள் வரை எளிய சிறைத்தண்டனை, அல்லது ரூ. 2,000 வரை அபராதம், அல்லது இரண்டும்", "Rigorous imprisonment up to 3 years", "3 ஆண்டுகள் வரை கடுங்காவல் சிறைத்தண்டனை", "Simple imprisonment up to 1 year and fine of Rs. 10,000", "1 ஆண்டு வரை எளிய சிறை மற்றும் ரூ. 10,000 அபராதம்", "Permanent disbarment from law practice only without imprisonment", "சிறைத்தண்டனையின்றி வழக்கறிஞர் தொழிலில் இருந்து நிரந்தரத் தடை மட்டுமே"),
         "A",
         "Under Section 12 of the Contempt of Courts Act 1971, contempt of court may be punished with simple imprisonment for a term which may extend to 6 months, or with fine which may extend to Rs. 2,000, or with both.",
         "1971 அவமதிப்புச் சட்டத்தின் பிரிவு 12-ன் படி, அதிகபட்ச தண்டனை 6 மாதங்கள் வரை எளிய சிறைத்தண்டனை, அல்லது ரூ. 2,000 வரை அபராதம், அல்லது இரண்டும் ஆகும்.",
         ("6 months simple imprisonment OR Rs. 2,000 fine OR both is the exact statutory maximum.", "6 மாத சிறை அல்லது ரூ. 2,000 அபராதம் அல்லது இரண்டும் சட்டப்பூர்வ அதிகபட்ச தண்டனையாகும்.", "3 years is incorrect.", "3 ஆண்டுகள் தவறு.", "1 year is incorrect.", "1 ஆண்டு தவறு.", "Disbarment is a Bar Council function, not the exclusive contempt penalty.", "தொழில் தடை மட்டுமே அவமதிப்புத் தண்டனை அல்ல."),
         "Assuming harsh multi-year prison sentences for contempt of court (maximum statutory term is 6 months).", "நீதிமன்ற அவமதிப்புக்கு பல ஆண்டுகள் சிறைத்தண்டனை விதிக்கலாம் எனத் தவறாக நினைப்பது.", "Maximum Contempt Punishment = 6 Months Simple Imprisonment OR Rs. 2,000 Fine OR Both.", "அதிகபட்ச அவமதிப்புத் தண்டனை = 6 மாத எளிய சிறை அல்லது ரூ. 2,000 அபராதம் அல்லது இரண்டும்.", "1"),

        ("POLITY_SC_MED_038", "Medium",
         "Under Article 145(5), how are decisions delivered by a Bench of the Supreme Court?",
         "உறுப்பு 145(5)-ன் படி, உச்ச நீதிமன்ற அமர்வு தன் தீர்ப்புகளை எவ்வாறு வழங்குகிறது?",
         ("By majority opinion of the judges present, with dissenting judges free to deliver separate opinions", "வருகை தந்த நீதிபதிகளின் பெரும்பான்மை கருத்து மூலம்; மாறுபட்ட நீதிபதிகள் தனித் தீர்ப்பு வழங்கலாம்", "By unanimous agreement only; no dissenting judgment is permitted", "ஒருமனதான சம்மதம் மூலம் மட்டுமே; மாறுபட்ட தீர்ப்பிற்கு அனுமதியில்லை", "By the decision of the Chief Justice of India alone regardless of other bench members", "மற்ற நீதிபதிகளைப் பொருட்படுத்தாமல் தலைமை நீதிபதியின் தனிப்பட்ட முடிவு மூலம்", "By secret ballot of all 34 Supreme Court judges", "அனைத்து 34 நீதிபதிகளின் ரகசிய வாக்கெடுப்பு மூலம்"),
         "A",
         "Article 145(5) explicitly states that no judgment shall be delivered save with the concurrence of a majority of the Judges present, but nothing prevents a dissenting Judge from delivering a dissenting judgment/opinion.",
         "உறுப்பு 145(5)-ன் படி, வருகை தந்த நீதிபதிகளின் பெரும்பான்மை சம்மதத்துடன் தீர்ப்பு வழங்கப்பட வேண்டும்; மாறுபட்ட நீதிபதி தன் மாறுபட்ட தீர்ப்பை வழங்கி பதிவிட முழு சுதந்திரம் உண்டு.",
         ("Majority concurrence decides judgment, dissenting opinions allowed under Art 145(5).", "பெரும்பான்மை முடிவு தீர்ப்பைத் தீர்மானிக்கிறது, மாறுபட்ட கருத்துக்கள் அனுமதிக்கப்படுகின்றன.", "Unanimity is NOT constitutionally required.", "ஒருமனதான சம்மதம் கட்டாயமில்லை.", "CJI cannot single-handedly override bench majority.", "தலைமை நீதிபதி தன்னிச்சையாக பெரும்பான்மையை மாற்ற முடியாது.", "Secret ballot of all 34 judges is never conducted for bench cases.", "அனைத்து நீதிபதிகளின் ரகசிய வாக்கெடுப்பு நடத்தப்படுவதில்லை."),
         "Assuming Supreme Court judgments MUST be unanimous or that dissenting judges cannot write separate opinions.", "உச்ச நீதிமன்ற தீர்ப்புகள் ஒருமனதாக இருக்க வேண்டும் என நினைப்பது.", "SC Bench Decisions = Determined by MAJORITY of judges present (Dissenting opinions permitted under Art 145(5)).", "SC அமர்வு முடிவுகள் = வருகை தந்த நீதிபதிகளின் பெரும்பான்மையால் தீர்மானிக்கப்படும் (மாறுபட்ட கருத்துக்கள் அனுமதிக்கப்படும்).", "1"),

        ("POLITY_SC_MED_039", "Medium",
         "Which Article provides that all proceedings in the Supreme Court shall be in the English language until Parliament by law otherwise provides?",
         "நாடாளுமன்றம் சட்டத்தின் மூலம் மாற்றி அமைக்கும் வரை உச்ச நீதிமன்றத்தின் அனைத்து நடைமுறைகளும் ஆங்கில மொழியிலேயே இருக்க வேண்டும் எனக் கூறும் உறுப்பு எது?",
         ("Article 343", "உறுப்பு 343", "Article 348", "உறுப்பு 348", "Article 350", "உறுப்பு 350", "Article 351", "உறுப்பு 351"),
         "B",
         "Article 348(1)(a) mandates that until Parliament by law otherwise provides, all proceedings in the Supreme Court and in every High Court shall be in the English language.",
         "அரசியலமைப்பு உறுப்பு 348(1)(a)-ன் படி, நாடாளுமன்றம் சட்டத்தால் வேறு விதமாக வழிவகை செய்யும் வரை உச்ச நீதிமன்றம் மற்றும் அனைத்து உயர் நீதிமன்றங்களின் நடைமுறைகளும் ஆங்கில மொழியிலேயே இருக்க வேண்டும்.",
         ("Art 343 is Official Language of the Union.", "உறுப்பு 343 ஒன்றியத்தின் அலுவல் மொழி.", "Art 348 = Language to be used in SC & High Courts (English).", "உறுப்பு 348 = SC மற்றும் உயர் நீதிமன்றங்களில் பயன்படுத்தப்படும் மொழி (ஆங்கிலம்).", "Art 350 is Language for redressal of grievances.", "உறுப்பு 350 குறைகேள் மனுக்களுக்கான மொழி.", "Art 351 is Directive for development of Hindi.", "உறுப்பு 351 இந்தி வளர்ச்சி வழிகாட்டுதல்."),
         "Confusing Article 343 (Official Language of Union - Hindi/English) with Article 348 (Language of Supreme Court - English).", "உறுப்பு 343 (ஒன்றிய அலுவல் மொழி) மற்றும் உறுப்பு 348 (உச்ச நீதிமன்ற மொழி) ஆகியவற்றை குழப்புவது.", "Supreme Court Proceedings Language = English under Article 348(1)(a).", "உச்ச நீதிமன்ற நடைமுறை மொழி = உறுப்பு 348(1)(a)-ன் கீழ் ஆங்கிலம்.", "1"),

        ("POLITY_SC_MED_040", "Medium",
         "Under Article 146(2), who determines the conditions of service of officers and servants of the Supreme Court?",
         "உறுப்பு 146(2)-ன் படி, உச்ச நீதிமன்றத்தின் அதிகாரிகள் மற்றும் ஊழியர்களின் பணி நிபந்தனைகளைத் தீர்மானிப்பவர் யார்?",
         ("Chief Justice of India (or judge/officer authorized by CJI), subject to President's approval for rules relating to salaries/pensions", "இந்தியத் தலைமை நீதிபதி (அல்லது அவரால அதிகாரமளிக்கப்பட்ட நீதிபதி/அதிகாரி); ஊதியம்/ஓய்வூதியம் சார்ந்த விதிகளுக்கு குடியரசுத் தலைவர் ஒப்புதல் பெற வேண்டும்", "Union Public Service Commission (UPSC)", "UPSC அமைப்பாளர்", "Union Finance Ministry independently", "ஒன்றிய நிதி அமைச்சகம் தன்னிச்சையாக", "Parliament by a 2/3rd majority act", "நாடாளுமன்றம் 2/3 பெரும்பான்மை சட்டத்தின் மூலம்"),
         "A",
         "Under Article 146(2), conditions of service of SC officers/servants are prescribed by rules made by CJI. However, rules relating to salaries, allowances, leave or pensions require approval of the President of India.",
         "உறுப்பு 146(2)-ன் படி, பணி நிபந்தனை விதிகளை CJI அமைப்பார். ஆனால் ஊதியம், படிகள், ஓய்வூதியம் தொடர்பான விதிகளுக்கு குடியரசுத் தலைவரின் ஒப்புதல் அவசியமாகும்.",
         ("CJI frames service rules; President approves financial/salary rules.", "CJI பணி விதிகளை அமைப்பார்; குடியரசுத் தலைவர் நிதி சார்ந்த விதிகளுக்கு ஒப்புதல் அளிப்பார்.", "UPSC does not frame SC staff service rules.", "UPSC ஊழியர் பணி விதிகளை அமைப்பதில்லை.", "Finance Ministry cannot unilaterally frame SC service rules.", "நிதி அமைச்சகம் தன்னிச்சையாக அமைக்க முடியாது.", "Parliament act is not required for SC administrative service rules.", "நாடாளுமன்றச் சட்டம் தேவையில்லை."),
         "Assuming Executive/Finance Ministry alone decides Supreme Court staff service rules without CJI input (CJI has primary rule-making power under Art 146).", "நிர்வாகத் துறையே SC ஊழியர்களின் பணி விதிகளை அமைக்கிறது என நினைப்பது.", "SC Staff Rules = Framed by CJI (Financial rules require President Approval) - Article 146(2).", "SC ஊழியர் விதிகள் = CJI அமைப்பார் (நிதி விதிகளுக்கு குடியரசுத் தலைவர் ஒப்புதல் தேவை).", "1"),

        ("POLITY_SC_MED_041", "Medium",
         "Which Article of the Constitution ensures the independence of the Supreme Court by barring discussion in Parliament regarding the conduct of any SC Judge?",
         "எந்தவொரு உச்ச நீதிமன்ற நீதிபதியின் நடத்தை குறித்தும் நாடாளுமன்றத்தில் விவாதிப்பதைத் தடுத்து SC சுதந்திரத்தை உறுதி செய்யும் உறுப்பு எது?",
         ("Article 121", "உறுப்பு 121", "Article 122", "உறுப்பு 122", "Article 211", "உறுப்பு 211", "Article 212", "உறுப்பு 212"),
         "A",
         "Article 121 explicitly bars any discussion in Parliament with respect to the conduct of any Judge of the Supreme Court or High Court in the discharge of his duties, EXCEPT upon a motion for presenting an address to the President for removal.",
         "உறுப்பு 121 உச்ச அல்லது உயர் நீதிமன்ற நீதிபதிகளின் பணி சார்ந்த நடத்தை குறித்து நாடாளுமன்றத்தில் விவாதிக்கத் தடை விதிக்கிறது (நீக்கத் தீர்மான விவாதத்தைத் தவிர).",
         ("Art 121 = Restriction on discussion in Parliament regarding conduct of judges.", "உறுப்பு 121 = நீதிபதிகள் நடத்தை குறித்து நாடாளுமன்றத்தில் விவாதிக்கத் தடை.", "Art 122 = Courts not to inquire into proceedings of Parliament.", "உறுப்பு 122 = நாடாளுமன்ற நடவடிக்கைகளை நீதிமன்றங்கள் விசாரிக்கக் கூடாது.", "Art 211 = Restriction on discussion in State Legislature.", "உறுப்பு 211 = மாநில சட்டமன்றத்தில் விவாதத் தடை.", "Art 212 = Courts not to inquire into State Legislature proceedings.", "உறுப்பு 212 = மாநில சட்டமன்ற நடவடிக்கைகளை நீதிமன்றங்கள் விசாரிக்கக் கூடாது."),
         "Confusing Article 121 (Bar on Parliament discussing judge conduct) with Article 122 (Bar on Courts inquiring into Parliamentary proceedings).", "உறுப்பு 121 (நாடாளுமன்றத்தில் விவாதத் தடை) மற்றும் உறுப்பு 122 (நீதிமன்றத்தில் நாடாளுமன்ற விசாரணைத் தடை) ஆகியவற்றை குழப்புவது.", "Bar on Parliament discussing Judge Conduct = Article 121. Bar on Courts inquiring Parliament = Article 122.", "நீதிபதிகள் நடத்தை விவாதத் தடை = உறுப்பு 121. நாடாளுமன்ற விசாரணைத் தடை = உறுப்பு 122.", "1"),

        ("POLITY_SC_MED_042", "Medium",
         "Which Article of the Constitution bars Courts (including Supreme Court) from inquiring into the validity of any proceedings in Parliament on grounds of alleged irregularity of procedure?",
         "நடைமுறை ஒழுங்கின்மை என்ற அடிப்படையில் நாடாளுமன்ற நடவடிக்கைகளின் செல்லுபடியாகும் தன்மையை நீதிமன்றங்கள் (உச்ச நீதிமன்றம் உட்பட) விசாரிக்கத் தடை விதிக்கும் உறுப்பு எது?",
         ("Article 120", "உறுப்பு 120", "Article 121", "உறுப்பு 121", "Article 122", "உறுப்பு 122", "Article 123", "உறுப்பு 123"),
         "C",
         "Article 122(1) mandates that the validity of any proceedings in Parliament shall not be called in question on the ground of any alleged irregularity of procedure.",
         "நடைமுறை ஒழுங்கின்மை என்ற அடிப்படையில் நாடாளுமன்றத்தின் எந்தவொரு நடவடிக்கையின் செல்லுபடியாகும் தன்மையையும் கேள்வி கேட்க முடியாது என உறுப்பு 122(1) கூறுகிறது.",
         ("Art 120 is Language used in Parliament.", "உறுப்பு 120 நாடாளுமன்றத்தில் பயன்படுத்தப்படும் மொழி.", "Art 121 is Restriction on discussion of judge conduct.", "உறுப்பு 121 நீதிபதிகள் நடத்தை விவாதத் தடை.", "Art 122 = Courts not to inquire into proceedings of Parliament.", "உறுப்பு 122 = நாடாளுமன்ற நடவடிக்கைகளை நீதிமன்றங்கள் விசாரிக்கத் தடை.", "Art 123 is Ordinance power of President.", "உறுப்பு 123 அவசரச்சட்ட அதிகாரம்."),
         "Confusing procedural irregularity (immune under Art 122) with substantive unconstitutionality/illegality (subject to Judicial Review).", "நடைமுறை ஒழுங்கின்மை (விசாரிக்க முடியாது) மற்றும் சட்டவிரோதத் தன்மையைக் (நீதித்துறை சீராய்வுக்கு உட்பட்டது) குழப்புவது.", "Courts barred from inquiring Parliamentary Procedural Irreguarity = Article 122.", "நாடாளுமன்ற நடைமுறை ஒழுங்கின்மையை நீதிமன்றங்கள் விசாரிக்கத் தடை = உறுப்பு 122.", "1"),

        ("POLITY_SC_MED_043", "Medium",
         "Which doctrine allows the Supreme Court to examine the TRUE NATURE and character of a law to determine if a legislature has transgressed its constitutional powers?",
         "ஒரு சட்டமன்றம் தன் அரசியலமைப்பு அதிகார வரம்பை மீறியுள்ளதா என்பதைத் தீர்மானிக்க, சட்டம் ஒன்றின் உண்மையான தன்மையை ஆராய உச்ச நீதிமன்றத்திற்கு உதவும் கோட்பாடு எது?",
         ("Doctrine of Severability", "பிரிக்கக்கூடிய கோட்பாடு (Severability)", "Doctrine of Pith and Substance", "சட்டத்தின் சாரம் மற்றும் உண்மைத் தன்மைக் கோட்பாடு (Pith and Substance)", "Doctrine of Eclipse", "மறைப்புக் கோட்பாடு (Eclipse)", "Doctrine of Colorable Legislation", "போலிச் சட்டக் கோட்பாடு (Colorable Legislation)"),
         "B",
         "The Doctrine of Pith and Substance is applied by SC when a law enacted by one legislature encroaches upon the domain of another list. If the 'substance' falls within its competence, the law is valid despite incidental encroachment.",
         "சட்டத்தின் சாரம் மற்றும் உண்மைத் தன்மைக் கோட்பாடு (Pith and Substance) ஒரு சட்டமன்றம் இயற்றிய சட்டம் மற்றொரு பட்டியலைத் தழுவும் போது, அதன் முதன்மை சாரத்தை ஆராயப் பயன்படுகிறது.",
         ("Severability separates valid provisions from unconstitutional provisions.", "Severability செல்லுபடியாகும் பிரிவுகளைப் பிரிக்கிறது.", "Pith and Substance examines the true nature/character of enactment to resolve list overlaps.", "Pith and Substance சட்டத்தின் உண்மையான சாரத்தை ஆராய்கிறது.", "Eclipse holds pre-constitutional laws dormant against FRs.", "Eclipse அடிப்படை உரிமைகளுக்கு எதிரான பழைய சட்டங்களை மறைத்து வைக்கிறது.", "Colorable legislation means 'what cannot be done directly cannot be done indirectly'.", "Colorable legislation என்பது 'நேரடியாக செய்ய முடியாததை மறைமுகமாக செய்ய முடியாது' என்பதாகும்."),
         "Confusing Doctrine of Pith and Substance (true nature of law) with Doctrine of Colorable Legislation (indirect transgression of power).", "Pith and Substance (உண்மைத் தன்மை) மற்றும் Colorable Legislation (மறைமுக மீறல்) ஆகிய கோட்பாடுகளைக் குழப்புவது.", "True Nature & Character of Legislation = Doctrine of Pith and Substance.", "சட்டத்தின் உண்மைத் தன்மை = Pith and Substance கோட்பாடு.", "1"),

        ("POLITY_SC_MED_044", "Medium",
         "What is the core principle behind the 'Doctrine of Colorable Legislation' frequently applied by the Supreme Court?",
         "உச்ச நீதிமன்றத்தால் அடிக்கடி பயன்படுத்தப்படும் 'போலிச் சட்டக் கோட்பாட்டின்' (Doctrine of Colorable Legislation) முதன்மைத் தத்துவம் என்ன?",
         ("What a legislature cannot do directly, it cannot do indirectly", "ஒரு சட்டமன்றம் எதை நேரடியாகச் செய்ய முடியாதோ, அதை மறைமுகமாகவும் செய்ய முடியாது", "All laws enacted before 1950 are automatically void", "1950-க்கு முன் இயற்றப்பட்ட அனைத்துச் சட்டங்களும் செல்லாதவை", "Fundamental Rights supersede Directive Principles in all circumstances", "அனைத்துச் சூழ்நிலைகளிலும் அடிப்படை உரிமைகள் அரசு நெறிமுறைகளை விட மேலானவை", "Supreme Court can legislate when Parliament is prorogued", "நாடாளுமன்றக் கூட்டம் இல்லாத போது உச்ச நீதிமன்றமே சட்டம் இயற்றலாம்"),
         "A",
         "The maxim 'Quando aliquid prohibetur ex directo, prohibetur et per obliquum' (What cannot be done directly cannot be done indirectly) forms the basis of Colorable Legislation. It checks covert constitutional overreach.",
         "நேரடியாக செய்ய முடியாத ஒரு அதிகாரத்தை மறைமுகமாக அல்லது போர்வையாக சட்டம் இயற்றி அடைவதை 'போலிச் சட்டக் கோட்பாடு' தடுக்கிறது.",
         ("What cannot be done directly cannot be done indirectly is the exact definition of Colorable Legislation.", "நேரடியாக செய்ய முடியாததை மறைமுகமாக செய்ய முடியாது என்பதே சரியான வரையறை.", "Pre-1950 laws are governed by Art 13 (Doctrine of Eclipse), not Colorable Legislation.", "1950-க்கு முந்தைய சட்டங்கள் உறுப்பு 13-ன் கீழ் வரும்.", "FR vs DPSP balance was established in Minerva Mills.", "FR vs DPSP சமநிலை மினர்வா மில்ஸ் வழக்கில் கூறப்பட்டது.", "SC cannot legislate.", "SC சட்டம் இயற்ற முடியாது."),
         "Confusing Colorable Legislation (covert power overreach) with Pith and Substance (incidental overlap of lists).", "Colorable Legislation மற்றும் Pith and Substance கோட்பாடுகளைக் குழப்புவது.", "Doctrine of Colorable Legislation = 'What cannot be done directly, cannot be done indirectly'.", "போலிச் சட்டக் கோட்பாடு = 'நேரடியாக செய்ய முடியாததை மறைமுகமாக செய்ய முடியாது'.", "1"),

        ("POLITY_SC_MED_045", "Medium",
         "Under Article 137, within how many days from the date of judgment must an application for REVIEW of a Supreme Court judgment be filed?",
         "உறுப்பு 137-ன் படி, உச்ச நீதிமன்ற தீர்ப்பு வழங்கப்பட்ட நாளிலிருந்து எத்தனை நாட்களுக்குள் சீராய்வு (Review) மனு தாக்கல் செய்யப்பட வேண்டும்?",
         ("15 days", "15 நாட்கள்", "30 days", "30 நாட்கள்", "60 days", "60 நாட்கள்", "90 days", "90 நாட்கள்"),
         "B",
         "Under Order XLVII of Supreme Court Rules 2013 (read with Art 137), a review petition must be filed within 30 days from the date of the judgment or order sought to be reviewed.",
         "உச்ச நீதிமன்ற விதிகளின்படி (உறுப்பு 137 உடன் இணைந்து), தீர்ப்பு வழங்கப்பட்ட நாளிலிருந்து 30 நாட்களுக்குள் சீராய்வு மனு தாக்கல் செய்யப்பட வேண்டும்.",
         ("15 days is too short.", "15 நாட்கள் மிகக் குறைவு.", "30 days is the exact statutory limitation period for filing a Review Petition in SC.", "30 நாட்கள் என்பது SC-ல் சீராய்வு மனு தாக்கல் செய்ய சட்டப்பூர்வக் காலக்கெடுவாகும்.", "60 days is for certain statutory civil appeals.", "60 நாட்கள் சில சிவில் மேல்முறையீடுகளுக்கு.", "90 days is standard for limitation in some appellate matters, but not SC review.", "90 நாட்கள் SC சீராய்வுக்கு உரியதல்ல."),
         "Confusing SC Review Petition limitation period (30 days) with general appellate limitation period (60 or 90 days).", "SC சீராய்வு மனு காலக்கெடுவை (30 நாட்கள்) சாதாரண மேல்முறையீட்டுக் காலக்கெடுவுடன் (60/90 நாட்கள்) குழப்புவது.", "Limitation Period for SC Review Petition = 30 Days (Supreme Court Rules).", "SC சீராய்வு மனு காலக்கெடு = 30 நாட்கள் (உச்ச நீதிமன்ற விதிகள்).", "1"),

        ("POLITY_SC_MED_046", "Medium",
         "What is a 'Curative Petition' in the Indian Supreme Court, and in which landmark case was it introduced?",
         "இந்திய உச்ச நீதிமன்றத்தில் 'குணப்படுத்தும் மனு' (Curative Petition) என்றால் என்ன, எந்த முக்கிய வழக்கில் இது அறிமுகப்படுத்தப்பட்டது?",
         ("It is the final remedy against SC review dismissal to prevent abuse of process; introduced in Rupa Ashok Hurra v. Ashok Hurra (2002)", "இது சீராய்வு மனு தள்ளுபடிக்கு பின் நீதி அநீதியைத் தடுக்க உச்சகட்ட நிவாரணமாகும்; ரூபா அசோக் ஹுர்ரா வழக்கில் (2002) அறிமுகப்படுத்தப்பட்டது", "It is a petition to cure medical illness of prisoners; introduced in Sunil Batra case (1978)", "இது கைதிகளின் மருத்துவச் சிகிச்சைக்கான மனுவாகும்; சுனில் பத்ரா வழக்கில் அறிமுகப்படுத்தப்பட்டது", "It is an administrative petition to correct spelling mistakes in court orders", "இது நீதிமன்ற உத்தரவுகளில் எழுத்துப் பிழைகளைத் திருத்தும் மனுவாகும்", "It is a petition to transfer cases from High Court to Subordinate Court", "இது வழக்குகளை உயர் நீதிமன்றத்திலிருந்து கீழ் நீதிமன்றத்திற்கு மாற்றும் மனுவாகும்"),
         "A",
         "In *Rupa Ashok Hurra v. Ashok Hurra (2002)*, a 5-judge bench of SC evolved the concept of 'Curative Petition' as a last constitutional resort after dismissal of a review petition to prevent gross abuse of process or violation of principles of natural justice.",
         "2002 ரூபா அசோக் ஹுர்ரா வழக்கில், சீராய்வு மனு தள்ளுபடி செய்யப்பட்ட பின்னரும் நீதி அநீதியைத் தடுக்க உச்சகட்ட நிவாரணமாக 'Curative Petition' முறையை 5 நீதிபதிகள் அமர்வு உருவாக்கியது.",
         ("Curative Petition was introduced in Rupa Ashok Hurra (2002) as last remedy after Review dismissal.", "ரூபா அசோக் ஹுர்ரா (2002) வழக்கில் சீராய்வுக்கு பிந்தைய கடைசி நிவாரணமாக Curative Petition அறிமுகப்படுத்தப்பட்டது.", "Sunil Batra dealt with prisoner rights & habeas corpus.", "சுனில் பத்ரா கைதிகள் உரிமைகள் பற்றியது.", "Spelling mistakes correction is governed by clerical error rules under Art 137.", "எழுத்துப் பிழைகள் திருத்தம் சாதாரண நடைமுறை.", "Case transfer is under Art 139A.", "வழக்கு மாற்றம் உறுப்பு 139A."),
         "Confusing Review Petition (Art 137 - filed within 30 days) with Curative Petition (Rupa Hurra 2002 - filed after Review Petition dismissal).", "சீராய்வு மனு (30 நாட்கள்) மற்றும் Curative Petition (சீராய்வு தள்ளுபடிக்கு பின்) ஆகியவற்றை குழப்புவது.", "Curative Petition Origin = Rupa Ashok Hurra v. Ashok Hurra (2002) (Filed after dismissal of Review Petition).", "Curative Petition தொடக்கம் = ரூபா அசோக் ஹுர்ரா வழக்கு (2002) (சீராய்வு மனு தள்ளுபடிக்குப் பின் தாக்கல் செய்யப்படுவது).", "1"),

        ("POLITY_SC_MED_047", "Medium",
         "Which Article provides for the appointment of the Officers and Servants of the Supreme Court and charging of administrative expenses upon the Consolidated Fund of India?",
         "உச்ச நீதிமன்ற அதிகாரிகள் நியமனம் மற்றும் அதன் நிர்வாகச் செலவுகளை இந்தியத் தொகுப்பு நிதியில் சுமத்துவது பற்றிக் கூறும் உறுப்பு எது?",
         ("Article 145", "உறுப்பு 145", "Article 146", "உறுப்பு 146", "Article 147", "உறுப்பு 147", "Article 148", "உறுப்பு 148"),
         "B",
         "Article 146 deals with Officers and servants and the administrative expenses of the Supreme Court.",
         "அரசியலமைப்பு உறுப்பு 146 உச்ச நீதிமன்றத்தின் அதிகாரிகள், ஊழியர்கள் மற்றும் நிர்வாகச் செலவுகளைக் கையாள்கிறது.",
         ("Art 145 = Rules of Court.", "உறுப்பு 145 = நீதிமன்ற விதிகள்.", "Art 146 = Officers, servants and administrative expenses of SC.", "உறுப்பு 146 = SC அதிகாரிகள், ஊழியர்கள் மற்றும் நிர்வாகச் செலவுகள்.", "Art 147 = Interpretation clause of Constitution.", "உறுப்பு 147 = அரசியலமைப்பு விளக்கமளித்தல் பிரிவு.", "Art 148 = CAG of India.", "உறுப்பு 148 = இந்திய தலைமைத் தணிக்கையாளர் (CAG)."),
         "Confusing Article 145 (Court rules) with Article 146 (Officers and expenses).", "உறுப்பு 145 (விதிக் குழு) மற்றும் உறுப்பு 146 (நிர்வாகச் செலவுகள்) ஆகியவற்றை குழப்புவது.", "SC Officers and Administrative Expenses = Article 146.", "SC அதிகாரிகள் மற்றும் நிர்வாகச் செலவுகள் = உறுப்பு 146.", "1"),

        ("POLITY_SC_MED_048", "Medium",
         "What is the significance of Article 147 of the Indian Constitution?",
         "இந்திய அரசியலமைப்பு உறுப்பு 147-ன் முக்கியத்துவம் என்ன?",
         ("It contains the interpretation clause clarifying references to substantial questions of law regarding Constitution/Government of India Acts", "இது அரசியலமைப்பு/இந்திய அரசுச் சட்டங்கள் பற்றிய முக்கிய சட்டக் கேள்விகள் குறித்த விளக்கமளிப்புப் பிரிவாகும்", "It provides for the impeachment of Supreme Court judges", "இது உச்ச நீதிமன்ற நீதிபதிகள் பதவி நீக்கம் பற்றிக் கூறுகிறது", "It grants advisory powers to the Prime Minister", "இது பிரதமருக்கு ஆலோசனை அதிகாரங்களை வழங்குகிறது", "It abolishes the jurisdiction of High Courts in tax matters", "இது வரி விவகாரங்களில் உயர் நீதிமன்ற அதிகார வரம்பை ரத்து செய்கிறது"),
         "A",
         "Article 147 is an 'Interpretation' clause. It clarifies that references in Chapter IV of Part V and Chapter V of Part VI to a substantial question of law as to the interpretation of the Constitution include references to Government of India Act 1935 and Indian Independence Act 1947.",
         "உறுப்பு 147 ஒரு 'விளக்கமளிப்புப்' (Interpretation) பிரிவாகும். பகுதி V மற்றும் பகுதி VI-ல் அரசியலமைப்பு விளக்கமளித்தல் என்பது 1935 இந்திய அரசுச் சட்டம் போன்றவற்றையும் உள்ளடக்கும் என இது தெளிவுபடுத்துகிறது.",
         ("Art 147 is the Interpretation Clause of Part V Chapter IV.", "உறுப்பு 147 பகுதி V அத்தியாயம் IV-ன் விளக்கமளிப்புப் பிரிவாகும்.", "Impeachment is under Art 124(4).", "நீக்கம் உறுப்பு 124(4).", "PM advisory powers do not exist under Art 147.", "பிரதமர் அதிகாரங்கள் இதில் இல்லை.", "HC tax jurisdiction is unaffected.", "HC வரி அதிகாரம் பாதிக்கப்படவில்லை."),
         "Treating Article 147 as a procedural rule rather than the constitutional Interpretation Clause for Union Judiciary.", "உறுப்பு 147-ஐ சாதாரண விதியாகக் கருதுவது.", "Article 147 = Interpretation Clause of Constitutional Provisions regarding Union Judiciary.", "உறுப்பு 147 = ஒன்றிய நீதித்துறை பற்றிய அரசியலமைப்பு விளக்கமளிப்புப் பிரிவு.", "1"),

        ("POLITY_SC_MED_049", "Medium",
         "Can Parliament REDUCE the jurisdiction and powers of the Supreme Court of India?",
         "இந்திய உச்ச நீதிமன்றத்தின் அதிகார வரம்பு மற்றும் அதிகாரங்களை நாடாளுமன்றத்தால் குறைக்க முடியுமா?",
         ("Yes, Parliament can curtail SC jurisdiction by simple majority", "ஆம், நாடாளுமன்றம் சாதாரண பெரும்பான்மை மூலம் குறைக்கலாம்", "No, Parliament can enlarge SC jurisdiction, but CANNOT curtail or reduce its constitutionally guaranteed jurisdiction", "இல்லை, நாடாளுமன்றம் SC அதிகார வரம்பை விரிவாக்கம் செய்யலாம், ஆனால் அரசியலமைப்பு வழங்கிய அதிகாரத்தைக் குறைக்க முடியாது", "Yes, during a National Emergency under Article 352", "ஆம், உறுப்பு 352 தேசிய அவசரநிலையின் போது குறைக்கலாம்", "Yes, if recommended by the Law Minister", "ஆம், சட்ட அமைச்சர் பரிந்துரைத்தால் குறைக்கலாம்"),
         "B",
         "The Constitution guarantees the jurisdiction and powers of the Supreme Court. Parliament can ENLARGE SC jurisdiction (Art 138), but CANNOT curtail or deprive the SC of its constitutionally guaranteed jurisdiction (e.g., Art 32, Art 136, Art 141, etc.).",
         "உச்ச நீதிமன்றத்தின் அதிகாரங்களை நாடாளுமன்றம் விரிவாக்கம் மட்டுமே செய்ய முடியும் (உறுப்பு 138); அரசியலமைப்பு வழங்கிய SC அதிகாரங்களைக் குறைக்கவோ ரத்து செய்யவோ நாடாளுமன்றத்திற்கு அதிகாரம் இல்லை.",
         ("Parliament cannot curtail SC constitutional jurisdiction.", "நாடாளுமன்றம் SC அதிகாரத்தைக் குறைக்க முடியாது.", "Parliament can ENLARGE SC powers (Art 138), but CANNOT curtail constitutionally assigned powers.", "நாடாளுமன்றம் விரிவாக்கம் மட்டுமே செய்ய முடியும் (உறுப்பு 138), குறைக்க முடியாது.", "Emergency does not empower Parliament to curtail SC constitutional powers.", "அவசரநிலை SC அதிகாரத்தைக் குறைக்க வழிவகுக்காது.", "Law Minister cannot reduce SC powers.", "சட்ட அமைச்சர் குறைக்க முடியாது."),
         "Assuming Parliament's power to legislate on Supreme Court extends to curtailing its core constitutional jurisdiction.", "நாடாளுமன்றம் SC அதிகாரங்களைக் குறைக்கவும் முடியும் எனத் தவறாக நினைப்பது.", "Parliament Power over SC = Can ENLARGE jurisdiction (Art 138), CANNOT CURTAIL jurisdiction.", "நாடாளுமன்ற அதிகாரம் = அதிகார வரம்பை விரிவாக்கம் செய்ய மட்டுமே முடியும், குறைக்க முடியாது.", "1"),

        ("POLITY_SC_MED_050", "Medium",
         "Who was the shortest-serving Chief Justice of India in history?",
         "இந்திய வரலாற்றில் மிகக் குறைந்த காலம் தலைமை நீதிபதியாகப் பணியாற்றியவர் யார்?",
         ("Justice K. N. Singh", "நீதிபதி கே. என். சிங்", "Justice S. Rajendra Babu", "நீதிபதி எஸ். ராஜேந்திர பாபு", "Justice J. C. Shah", "நீதிபதி ஜே. சி. ஷா", "Justice L. M. Sharma", "நீதிபதி எல். எம். சர்மா"),
         "A",
         "Justice Kamal Narain Singh (K. N. Singh) served as the 22nd Chief Justice of India for just 17 DAYS (25 November 1991 to 12 December 1991), making him the shortest-serving CJI in Indian history.",
         "நீதிபதி கமல் நரேன் சிங் (K. N. Singh) வெறும் 17 நாட்கள் மட்டுமே (25 நவம்பர் 1991 முதல் 12 டிசம்பர் 1991 வரை) 22-வது தலைமை நீதிபதியாகப் பணியாற்றினார்; இவரே மிகக் குறைந்த காலம் பணியாற்றிய CJI ஆவார்.",
         ("K. N. Singh served for ONLY 17 DAYS (shortest CJI tenure in history).", "கே. என். சிங் வெறும் 17 நாட்கள் மட்டுமே பணியாற்றினார் (வரலாற்றில் மிகக் குறைந்த காலம்).", "S. Rajendra Babu served for 29 days (2nd shortest).", "எஸ். ராஜேந்திர பாபு 29 நாட்கள் பணியாற்றினார் (2-வது மிகக் குறைந்த காலம்).", "J. C. Shah served for around 1 month 5 days.", "ஜே. சி. ஷா 1 மாதம் 5 நாட்கள் பணியாற்றினார்.", "L. M. Sharma served for around 2.5 months.", "எல். எம். சர்மா 2.5 மாதங்கள் பணியாற்றினார்."),
         "Confusing K. N. Singh (shortest CJI - 17 days) with Y. V. Chandrachud (longest CJI - 7+ years).", "மிகக் குறைந்த காலம் பணியாற்றியவர் (கே.என். சிங் - 17 நாட்கள்) மற்றும் மிக நீண்ட காலம் பணியாற்றியவரை (ஒய்.வி. சந்திரசூட் - 7+ ஆண்டுகள்) குழப்புவது.", "Shortest Serving CJI = Justice K. N. Singh (17 Days in 1991).", "மிகக் குறைந்த காலம் பணியாற்றிய CJI = நீதிபதி கே. என். சிங் (17 நாட்கள் - 1991).", "1")
    ]

    medium = []
    for idx, item in enumerate(medium_data):
        qid, diff, s_en, s_ta, opts, corr, exp_en, exp_ta, why_args, trap_en, trap_ta, tip_en, tip_ta, sp = item
        if len(opts) != 8:
            print(f"FAILED OPTS AT INDEX {idx}: QID={qid}, len(opts)={len(opts)}")
        if len(why_args) != 8:
            print(f"FAILED WHY_ARGS AT INDEX {idx}: QID={qid}, len(why_args)={len(why_args)}")
        options = make_options(*opts)
        why_not = make_why_not(corr, *why_args)
        medium.append(build_q(qid, diff, s_en, s_ta, options, corr, exp_en, exp_ta, why_not, trap_en, trap_ta, tip_en, tip_ta, sp))
    return medium

def main():
    med_qs = get_medium_questions()
    print(f"Generated Medium Questions: {len(med_qs)}")
    assert len(med_qs) == 50, f"Expected 50, got {len(med_qs)}"
    
    out_path = "data/questions/polity/supreme_court_medium.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(med_qs, f, ensure_ascii=False, indent=2)
    print(f"Saved -> {out_path}")

if __name__ == "__main__":
    main()
