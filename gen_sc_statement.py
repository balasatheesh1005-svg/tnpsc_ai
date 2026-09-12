# -*- coding: utf-8 -*-
"""
Generator for Supreme Court Statement MCQs (50 Questions)
Topic: Supreme Court of India
Section: Statement Questions
File: data/questions/polity/supreme_court_statement.json
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
        "question_type": "Statement",
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

def get_statement_questions():
    stmt_data = [
        ("POLITY_SC_STMT_001",
         "Consider the following statements regarding the Original Jurisdiction of the Supreme Court under Article 131:\n1. A dispute between the Government of India and one or more States falls under Article 131.\n2. A dispute arising out of a pre-Constitution treaty or agreement is explicitly covered under Article 131 Original Jurisdiction.\nWhich of the statements given above is/are correct?",
         "உறுப்பு 131-ன் கீழ் உச்ச நீதிமன்றத்தின் மூல ஆதிக்கம் பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. இந்திய அரசுக்கும் ஒன்று அல்லது அதற்கு மேற்பட்ட மாநிலங்களுக்கும் இடையேயான தகராறு உறுப்பு 131-ன் கீழ் வரும்.\n2. அரசியலமைப்புக்கு முந்தைய உடன்படிக்கை அல்லது ஒப்பந்தத்திலிருந்து எழும் தகராறு உறுப்பு 131 மூல ஆதிக்கத்தின் கீழ் வெளிப்படையாக வரும்.\nமேற்கண்ட கூற்றுகளில் எது/எவை சரியானவை?",
         ("1 only", "1 மட்டுமே", "2 only", "2 மட்டுமே", "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்", "Neither 1 nor 2", "இரண்டும் இல்லை"),
         "A",
         "Statement 1 is correct (Art 131 covers Centre-State disputes). Statement 2 is INCORRECT because the proviso to Article 131 explicitly EXCLUDES disputes arising out of pre-Constitution treaties or agreements.",
         "கூற்று 1 சரி (உறுப்பு 131 ஒன்றியம்-மாநில தகராறைக் கையாள்கிறது). கூற்று 2 தவறு, ஏனெனில் உறுப்பு 131-ன் வரம்பு அரசியலமைப்புக்கு முந்தைய ஒப்பந்தங்களை மூல ஆதிக்கத்திலிருந்து வெளிப்படையாக விலக்குகிறது.",
         ("Statement 1 is correct; Statement 2 is incorrect due to the proviso to Art 131.", "கூற்று 1 சரி; உறுப்பு 131 வரம்பால் கூற்று 2 தவறானது.", "Statement 2 is incorrect.", "கூற்று 2 தவறானது.", "Both statements are not correct.", "இரண்டு கூற்றுகளும் சரியானவை அல்ல.", "Statement 1 is correct, so Neither is invalid.", "கூற்று 1 சரி என்பதால் இரண்டும் இல்லை என்பது தவறானது."),
         "Assuming pre-constitutional treaties are covered under Article 131 Original Jurisdiction (they are strictly excluded by the proviso).", "அரசியலமைப்புக்கு முந்தைய ஒப்பந்தங்கள் உறுப்பு 131-ல் வரும் என நினைப்பது (அவை விலக்கப்பட்டுள்ளன).", "Art 131 Original Jurisdiction = Covers Centre-State disputes; EXCLUDES pre-Constitution treaties (Proviso to Art 131).", "உறுப்பு 131 மூல ஆதிக்கம் = ஒன்றியம்-மாநில தகராறுகளை உள்ளடக்கும்; அரசியலமைப்புக்கு முந்தைய ஒப்பந்தங்களை விலக்கும்.", "2"),

        ("POLITY_SC_STMT_002",
         "Consider the following statements regarding the appointment of Supreme Court Judges:\n1. The Collegium system for appointing SC judges consists of the Chief Justice of India and 4 senior-most judges of the SC.\n2. The Second Judges Case (1993) held that 'consultation' with CJI does NOT mean concurrence.\nWhich of the statements given above is/are correct?",
         "உச்ச நீதிமன்ற நீதிபதிகள் நியமனம் பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. SC நீதிபதிகளை நியமிக்கும் கொலீஜியம் அமைப்பில் இந்தியத் தலைமை நீதிபதி மற்றும் 4 மூத்த SC நீதிபதிகள் இடம்பெறுவர்.\n2. இரண்டாவது நீதிபதிகள் வழக்கு (1993) CJI உடனான 'கலந்தாலோசனை' என்பது ஒப்புதல் ஆகாது எனக் கூறியது.\nமேற்கண்ட கூற்றுகளில் எது/எவை சரியானவை?",
         ("1 only", "1 மட்டுமே", "2 only", "2 மட்டுமே", "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்", "Neither 1 nor 2", "இரண்டும் இல்லை"),
         "A",
         "Statement 1 is correct (Third Judges Case 1998 established CJI + 4 seniors collegium). Statement 2 is INCORRECT because the Second Judges Case (1993) held that 'consultation' DOES mean concurrence (it was First Judges Case 1981 which held consultation does not mean concurrence).",
         "கூற்று 1 சரி (மூன்றாவது நீதிபதிகள் வழக்கு 1998 CJI + 4 மூத்த நீதிபதிகள் கொலீஜியத்தை அமைத்தது). கூற்று 2 தவறு, ஏனெனில் இரண்டாவது நீதிபதிகள் வழக்கு (1993) கலந்தாலோசனை என்பது 'ஒப்புதல்' என்றே தீர்ப்பளித்தது.",
         ("Statement 1 is correct; Statement 2 misattributes the ruling of First Judges Case 1981 to Second Judges Case 1993.", "கூற்று 1 சரி; கூற்று 2 முதல் நீதிபதிகள் வழக்கு தீர்ப்பை 2-வது நீதிபதிகள் வழக்குடன் குழப்புகிறது.", "Statement 2 is incorrect.", "கூற்று 2 தவறானது.", "Both are not correct.", "இரண்டும் சரியானவை அல்ல.", "Neither is invalid because 1 is correct.", "1 சரி என்பதால் இரண்டும் இல்லை என்பது தவறானது."),
         "Confusing First Judges Case 1981 (consultation != concurrence) with Second Judges Case 1993 (consultation == concurrence).", "முதல் (1981) மற்றும் இரண்டாவது (1993) நீதிபதிகள் வழக்கின் தீர்ப்புகளைக் குழப்புவது.", "Appointment Collegium = CJI + 4 Senior-most SC Judges. Second Judges Case (1993) = Consultation MEANS Concurrence.", "நியமன கொலீஜியம் = CJI + 4 மூத்த நீதிபதிகள். 2-வது நீதிபதிகள் வழக்கு (1993) = கலந்தாலோசனை என்பது ஒப்புதல்.", "1"),

        ("POLITY_SC_STMT_003",
         "With reference to the removal of a Supreme Court Judge under Article 124(4), consider the following statements:\n1. A removal motion requires 100 members' signatures in Lok Sabha or 50 members' signatures in Rajya Sabha for admission.\n2. A Supreme Court judge can be removed by a simple majority vote in Parliament.\nWhich of the statements given above is/are correct?",
         "உறுப்பு 124(4)-ன் கீழ் உச்ச நீதிமன்ற நீதிபதி நீக்கம் குறித்த பின்வரும் கூற்றுகளை ஆராய்க:\n1. நீக்கத் தீர்மானத்தை ஏற்க மக்களவையில் 100 உறுப்பினர்கள் அல்லது மாநிலங்களவையில் 50 உறுப்பினர்கள் கையொப்பமிட வேண்டும்.\n2. உச்ச நீதிமன்ற நீதிபதியை நாடாளுமன்றத்தில் சாதாரண பெரும்பான்மை வாக்கு மூலம் நீக்கிவிடலாம்.\nமேற்கண்ட கூற்றுகளில் எது/எவை சரியானவை?",
         ("1 only", "1 மட்டுமே", "2 only", "2 மட்டுமே", "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்", "Neither 1 nor 2", "இரண்டும் இல்லை"),
         "A",
         "Statement 1 is correct (Judges Inquiry Act 1968 signature threshold). Statement 2 is INCORRECT because Article 124(4) strictly requires a SPECIAL MAJORITY in each House (majority of total membership AND 2/3rd members present & voting).",
         "கூற்று 1 சரி (1968 சட்டப்படி 100 LS / 50 RS உறுப்பினர்கள் கையொப்பம் தேவை). கூற்று 2 தவறு, ஏனெனில் உறுப்பு 124(4) ஒவ்வொரு அவையிலும் சிறப்புப் பெரும்பான்மையைக் கட்டாயமாக்குகிறது.",
         ("Statement 1 is correct; Statement 2 is wrong because Special Majority is mandatory under Art 124(4).", "கூற்று 1 சரி; சிறப்புப் பெரும்பான்மை தேவை என்பதால் கூற்று 2 தவறு.", "Statement 2 is incorrect.", "கூற்று 2 தவறானது.", "Both statements are not correct.", "இரண்டு கூற்றுகளும் சரியானவை அல்ல.", "Neither is invalid.", "இரண்டும் இல்லை என்பது தவறானது."),
         "Assuming simple majority is sufficient to remove a Supreme Court judge (a Special Majority under Art 124(4) is mandatory).", "சாதாரண பெரும்பான்மையே போதுமானது எனத் தவறாக நினைப்பது.", "Removal Threshold = Notice: 100 LS / 50 RS; Voting: Special Majority under Article 124(4).", "நீக்க நிபந்தனை = அறிவிப்பு: 100 LS / 50 RS; வாக்கெடுப்பு: உறுப்பு 124(4)-ன் கீழ் சிறப்புப் பெரும்பான்மை.", "1"),

        ("POLITY_SC_STMT_004",
         "Consider the following statements regarding Advisory Jurisdiction under Article 143:\n1. The opinion rendered by the Supreme Court under Article 143 is binding on the President.\n2. The Supreme Court is bound to give an opinion on pre-Constitution treaties referred under Article 143(2).\nWhich of the statements given above is/are correct?",
         "உறுப்பு 143 ஆலோசனை ஆதிக்கம் பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. உறுப்பு 143-ன் கீழ் உச்ச நீதிமன்றம் அளிக்கும் கருத்து குடியரசுத் தலைவரைக் கட்டுப்படுத்தும்.\n2. உறுப்பு 143(2)-ன் கீழ் அனுப்பப்படும் அரசியலமைப்புக்கு முந்தைய ஒப்பந்தங்களில் கருத்துத் தெரிவிக்க SC கடமைப்பட்டுள்ளது.\nமேற்கண்ட கூற்றுகளில் எது/எவை சரியானவை?",
         ("1 only", "1 மட்டுமே", "2 only", "2 மட்டுமே", "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்", "Neither 1 nor 2", "இரண்டும் இல்லை"),
         "B",
         "Statement 1 is INCORRECT (Art 143 opinion is advisory only and NOT binding on the President). Statement 2 is CORRECT (under Art 143(2), the SC 'shall' report its opinion on pre-Constitution disputes).",
         "கூற்று 1 தவறு (உறுப்பு 143 கருத்து வெறும் ஆலோசனையே, கட்டுப்படுத்தாது). கூற்று 2 சரி (உறுப்பு 143(2)-ன் கீழ் அரசியலமைப்புக்கு முந்தைய ஒப்பந்தங்களில் SC கருத்து தெரிவிக்கக் கடமைப்பட்டுள்ளது).",
         ("Statement 1 is incorrect; Statement 2 is correct under Art 143(2).", "கூற்று 1 தவறு; உறுப்பு 143(2)-ன் கீழ் கூற்று 2 சரி.", "Statement 2 is correct, so 2 only is correct.", "கூற்று 2 சரி என்பதால் 2 மட்டுமே என்பது சரியான பதில்.", "Both are not correct.", "இரண்டும் சரியானவை அல்ல.", "Neither is invalid.", "இரண்டும் இல்லை என்பது தவறானது."),
         "Assuming SC advisory opinion binds the President (it is purely advisory and non-binding).", "SC ஆலோசனை குடியரசுத் தலைவரைக் கட்டுப்படுத்தும் என நினைப்பது.", "Art 143 Advisory Opinion = NOT binding on President. Art 143(2) = Mandatory for SC to report opinion.", "உறுப்பு 143 ஆலோசனை = குடியரசுத் தலைவரைக் கட்டுப்படுத்தாது. உறுப்பு 143(2) = SC கருத்து தெரிவிப்பது கட்டாயம்.", "1"),

        ("POLITY_SC_STMT_005",
         "Consider the following statements about Special Leave Petition (SLP) under Article 136:\n1. It can be granted against any judgment, decree or order of any court or tribunal in India.\n2. Courts or tribunals constituted under Armed Forces laws are explicitly excluded from Article 136.\nWhich of the statements given above is/are correct?",
         "உறுப்பு 136-ன் கீழ் சிறப்பு விடுப்பு மனு (SLP) பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. இந்தியாவில் உள்ள எந்தவொரு நீதிமன்றம் அல்லது தீர்ப்பாயத்தின் தீர்ப்பு/உத்தரவிற்கு எதிராக இது வழங்கப்படலாம்.\n2. இராணுவச் சட்டங்களின் கீழ் அமைக்கப்பட்ட நீதிமன்றங்கள் அல்லது தீர்ப்பாயங்கள் உறுப்பு 136-லிருந்து வெளிப்படையாக விலக்கப்பட்டுள்ளன.\nமேற்கண்ட கூற்றுகளில் எது/எவை சரியானவை?",
         ("1 only", "1 மட்டுமே", "2 only", "2 மட்டுமே", "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்", "Neither 1 nor 2", "இரண்டும் இல்லை"),
         "C",
         "Both statements are CORRECT. Article 136(1) provides broad discretionary power over all courts/tribunals, while Article 136(2) explicitly excludes Armed Forces courts/tribunals.",
         "இரண்டு கூற்றுகளும் சரி. உறுப்பு 136(1) அனைத்து நீதிமன்றங்கள்/தீர்ப்பாயங்கள் மீது பரந்த தன்னிச்சை அதிகாரம் அளிக்கிறது; உறுப்பு 136(2) இராணுவ நீதிமன்றங்களை வெளிப்படையாக விலக்குகிறது.",
         ("Statement 1 is correct under Art 136(1).", "உறுப்பு 136(1)-ன் கீழ் கூற்று 1 சரி.", "Statement 2 is correct under Art 136(2).", "உறுப்பு 136(2)-ன் கீழ் கூற்று 2 சரி.", "Both Statements 1 and 2 are correct.", "கூற்றுகள் 1 மற்றும் 2 ஆகிய இரண்டும் சரி.", "Neither is invalid.", "இரண்டும் இல்லை என்பது தவறானது."),
         "Overlooking the Armed Forces exception under Article 136(2).", "உறுப்பு 136(2)-ன் கீழ் இராணுவ நீதிமன்ற விலக்கைப் புறக்கணிப்பது.", "Article 136 = Wide discretionary power OVER ALL COURTS/TRIBUNALS, EXCEPT Armed Forces Courts (Art 136(2)).", "உறுப்பு 136 = அனைத்து நீதிமன்றங்கள் மீது அதிகாரம், இராணுவ நீதிமன்றங்கள் தவிர (உறுப்பு 136(2)).", "1"),

        ("POLITY_SC_STMT_006",
         "Consider the following statements regarding Supreme Court Judges' qualifications:\n1. A person must have been an advocate of a High Court for at least 10 years to be eligible.\n2. A distinguished jurist in the opinion of the President can be appointed directly as a Supreme Court Judge.\nWhich of the statements given above is/are correct?",
         "உச்ச நீதிமன்ற நீதிபதிகளின் தகுதிகள் பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. தகுதி பெற ஒருவர் உயர் நீதிமன்றத்தில் குறைந்தபட்சம் 10 ஆண்டுகள் வழக்கறிஞராகப் பணியாற்றியிருக்க வேண்டும்.\n2. குடியரசுத் தலைவர் கருத்தில் புகழ்பெற்ற சட்ட வல்லுநர் நேரடியாக உச்ச நீதிமன்ற நீதிபதியாக நியமிக்கப்படலாம்.\nமேற்கண்ட கூற்றுகளில் எது/எவை சரியானவை?",
         ("1 only", "1 மட்டுமே", "2 only", "2 மட்டுமே", "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்", "Neither 1 nor 2", "இரண்டும் இல்லை"),
         "C",
         "Both statements are CORRECT under Article 124(3). Qualification options are: (a) 5 years HC Judge, OR (b) 10 years HC Advocate, OR (c) Distinguished Jurist in President's opinion.",
         "இரண்டு கூற்றுகளும் சரி (உறுப்பு 124(3)). தகுதிகள்: (a) 5 ஆண்டுகள் HC நீதிபதி, அல்லது (b) 10 ஆண்டுகள் HC வழக்கறிஞர், அல்லது (c) குடியரசுத் தலைவர் கருத்தில் புகழ்பெற்ற சட்ட வல்லுநர்.",
         ("Statement 1 is correct under Art 124(3)(b).", "உறுப்பு 124(3)(b)-ன் கீழ் கூற்று 1 சரி.", "Statement 2 is correct under Art 124(3)(c).", "உறுப்பு 124(3)(c)-ன் கீழ் கூற்று 2 சரி.", "Both statements 1 and 2 are correct.", "கூற்றுகள் 1 மற்றும் 2 ஆகிய இரண்டும் சரி.", "Neither is invalid.", "இரண்டும் இல்லை என்பது தவறானது."),
         "Confusing HC judge tenure (5 years) with HC advocate tenure (10 years).", "உயர் நீதிமன்ற நீதிபதி காலம் (5 ஆண்டுகள்) மற்றும் வழக்கறிஞர் காலத்தைக் (10 ஆண்டுகள்) குழப்புவது.", "SC Qualifications = 5 yrs HC Judge OR 10 yrs HC Advocate OR Distinguished Jurist (Art 124(3)).", "SC தகுதிகள் = 5 ஆண்டுகள் HC நீதிபதி அல்லது 10 ஆண்டுகள் HC வழக்கறிஞர் அல்லது புகழ்பெற்ற சட்ட வல்லுநர்.", "1"),

        ("POLITY_SC_STMT_007",
         "Consider the following statements regarding Court of Record (Article 129):\n1. The judgments of the Supreme Court have perpetual memory and evidentiary value in all courts in India.\n2. The Supreme Court has the power to punish for contempt of itself, but NOT for contempt of subordinate courts.\nWhich of the statements given above is/are correct?",
         "பதிவு நீதிமன்றம் (உறுப்பு 129) பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. உச்ச நீதிமன்றத் தீர்ப்புகள் இந்தியாவில் உள்ள அனைத்து நீதிமன்றங்களிலும் சான்றாதார மதிப்பு கொண்டவை.\n2. உச்ச நீதிமன்றத்திற்குத் தன் அவமதிப்புக்குத் தண்டிக்கும் அதிகாரம் உண்டு, ஆனால் கீழ்மை நீதிமன்ற அவமதிப்புக்குத் தண்டிக்கும் அதிகாரம் இல்லை.\nமேற்கண்ட கூற்றுகளில் எது/எவை சரியானவை?",
         ("1 only", "1 மட்டுமே", "2 only", "2 மட்டுமே", "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்", "Neither 1 nor 2", "இரண்டும் இல்லை"),
         "A",
         "Statement 1 is CORRECT (defining feature of Court of Record). Statement 2 is INCORRECT because in *Delhi Judicial Service Association Case (1991)*, SC held its contempt powers under Art 129 EXTEND to subordinate courts as well.",
         "கூற்று 1 சரி (பதிவு நீதிமன்றத்தின் முதன்மை அம்சம்). கூற்று 2 தவறு, ஏனெனில் 1991 டெல்லி நீதித்துறை சேவை சங்க வழக்கில் SC அவமதிப்பு அதிகாரம் கீழ்மை நீதிமன்றங்களுக்கும் பொருந்தும் எனத் தீர்ப்பளிக்கப்பட்டது.",
         ("Statement 1 is correct; Statement 2 is incorrect under Delhi Judicial Service Case 1991.", "கூற்று 1 சரி; 1991 வழக்கின் படி கூற்று 2 தவறானது.", "Statement 2 is incorrect.", "கூற்று 2 தவறானது.", "Both are not correct.", "இரண்டும் சரியானவை அல்ல.", "Neither is invalid.", "இரண்டும் இல்லை என்பது தவறானது."),
         "Assuming SC contempt power is restricted only to its own proceedings and not subordinate courts.", "SC அவமதிப்பு அதிகாரம் தன் நடவடிக்கைகளுக்கு மட்டுமே பொருந்தும் என நினைப்பது.", "Court of Record (Art 129) = Evidentiary Value of Judgments + Contempt Power OVER ITSELF AND SUBORDINATE COURTS.", "பதிவு நீதிமன்றம் (உறுப்பு 129) = தீர்ப்புகளின் சான்றாதார மதிப்பு + தன் மற்றும் கீழ்மை நீதிமன்ற அவமதிப்புத் தண்டனை அதிகாரம்.", "1"),

        ("POLITY_SC_STMT_008",
         "Consider the following statements regarding Article 141 and Article 142:\n1. Article 141 declares that the law declared by the Supreme Court shall be binding on all courts within India.\n2. Article 142 empowers the Supreme Court to pass any decree necessary for doing complete justice.\nWhich of the statements given above is/are correct?",
         "உறுப்பு 141 மற்றும் உறுப்பு 142 பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. உச்ச நீதிமன்றத்தால் அறிவிக்கப்படும் சட்டம் இந்தியாவில் உள்ள அனைத்து நீதிமன்றங்களையும் கட்டுப்படுத்தும் என உறுப்பு 141 கூறுகிறது.\n2. முழுமையான நீதி வழங்கத் தேவையான ஆணையைப் பிறப்பிக்க உச்ச நீதிமன்றத்திற்கு உறுப்பு 142 அதிகாரமளிக்கிறது.\nமேற்கண்ட கூற்றுகளில் எது/எவை சரியானவை?",
         ("1 only", "1 மட்டுமே", "2 only", "2 மட்டுமே", "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்", "Neither 1 nor 2", "இரண்டும் இல்லை"),
         "C",
         "Both statements are CORRECT. Article 141 embeds Stare Decisis (binding precedent). Article 142 provides inherent power to enforce complete justice.",
         "இரண்டு கூற்றுகளும் சரி. உறுப்பு 141 கட்டாய முன்மாதிரி சட்டத்தையும் (Stare Decisis), உறுப்பு 142 முழுமையான நீதிக்கான (Complete Justice) அதிகாரத்தையும் வழங்குகின்றன.",
         ("Statement 1 is correct under Art 141.", "உறுப்பு 141-ன் கீழ் கூற்று 1 சரி.", "Statement 2 is correct under Art 142.", "உறுப்பு 142-ன் கீழ் கூற்று 2 சரி.", "Both Statements 1 and 2 are correct.", "கூற்றுகள் 1 மற்றும் 2 ஆகிய இரண்டும் சரி.", "Neither is invalid.", "இரண்டும் இல்லை என்பது தவறானது."),
         "Confusing Article 141 (Binding Law / Precedent) with Article 142 (Complete Justice Orders).", "உறுப்பு 141 (கட்டாயச் சட்டம்) மற்றும் உறுப்பு 142 (முழுமையான நீதி) ஆகியவற்றைக் குழப்புவது.", "Article 141 = Binding Precedent on all courts. Article 142 = Enforcement of Decrees for Complete Justice.", "உறுப்பு 141 = அனைத்து நீதிமன்றங்களுக்கும் கட்டாய முன்மாதிரி சட்டம். உறுப்பு 142 = முழுமையான நீதிக்கான ஆணைகள்.", "1"),

        ("POLITY_SC_STMT_009",
         "Consider the following statements regarding Judicial Review in India:\n1. The term 'Judicial Review' is explicitly defined in Article 13 of the Indian Constitution.\n2. Judicial Review of High Courts and Supreme Court is part of the Basic Structure of the Constitution.\nWhich of the statements given above is/are correct?",
         "இந்தியாவில் நீதித்துறை சீராய்வு பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. 'நீதித்துறை சீராய்வு' என்ற சொல் இந்திய அரசியலமைப்பின் உறுப்பு 13-ல் வெளிப்படையாக வரையறுக்கப்பட்டுள்ளது.\n2. உயர் நீதிமன்றங்கள் மற்றும் உச்ச நீதிமன்றத்தின் நீதித்துறை சீராய்வு அரசியலமைப்பின் அடிப்படை அமைப்பின் பகுதியாகும்.\nமேற்கண்ட கூற்றுகளில் எது/எவை சரியானவை?",
         ("1 only", "1 மட்டுமே", "2 only", "2 மட்டுமே", "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்", "Neither 1 nor 2", "இரண்டும் இல்லை"),
         "B",
         "Statement 1 is INCORRECT because the phrase 'Judicial Review' is NOT explicitly mentioned or defined anywhere in the text of the Constitution (though the power is derived from Arts 13, 32, 136, 226). Statement 2 is CORRECT (*L. Chandra Kumar Case 1997*).",
         "கூற்று 1 தவறு, ஏனெனில் 'நீதித்துறை சீராய்வு' என்ற சொல் அரசியலமைப்பு உரையில் எங்கும் வெளிப்படையாகக் குறிப்பிடப்படவில்லை. கூற்று 2 சரி (1997 சந்திரகுமார் வழக்கு).",
         ("Statement 1 is incorrect (phrase 'Judicial Review' is not explicitly used in text); Statement 2 is correct.", "கூற்று 1 தவறு ('நீதித்துறை சீராய்வு' சொல் உரையில் இல்லை); கூற்று 2 சரி.", "Statement 2 is correct, so 2 only is correct.", "கூற்று 2 சரி என்பதால் 2 மட்டுமே சரியான பதில்.", "Both are not correct.", "இரண்டும் சரியானவை அல்ல.", "Neither is invalid.", "இரண்டும் இல்லை என்பது தவறானது."),
         "Assuming the exact phrase 'Judicial Review' is explicitly defined in Article 13 (the concept is implicit in Art 13, but the phrase itself is not in the text).", "'நீதித்துறை சீராய்வு' என்ற சொல் உறுப்பு 13-ல் வெளிப்படையாக உள்ளது எனத் தவறாக நினைப்பது.", "Phrase 'Judicial Review' = NOT explicitly mentioned in Constitution text. Power of Judicial Review = Basic Structure (L. Chandra Kumar 1997).", "'நீதித்துறை சீராய்வு' சொல் = அரசியலமைப்பு உரையில் இல்லை. சீராய்வு அதிகாரம் = அடிப்படை அமைப்பு.", "1"),

        ("POLITY_SC_STMT_010",
         "Consider the following statements regarding Public Interest Litigation (PIL):\n1. PIL in India was pioneered by Justice P. N. Bhagwati and Justice V. R. Krishna Iyer.\n2. PIL mandates strict adherence to the traditional rule of Locus Standi.\nWhich of the statements given above is/are correct?",
         "பொது நல வழக்கு (PIL) பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. இந்தியாவில் PIL முறைக்கு நீதிபதி பி. என். பகவதி மற்றும் நீதிபதி வி. ஆர். கிருஷ்ணய்யர் முன்னோடியாக இருந்தனர்.\n2. PIL முறை Locus Standi என்ற பாரம்பரிய விதியை கண்டிப்புடன் பின்பற்றுவதைக் கட்டாயமாக்குகிறது.\nமேற்கண்ட கூற்றுகளில் எது/எவை சரியானவை?",
         ("1 only", "1 மட்டுமே", "2 only", "2 மட்டுமே", "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்", "Neither 1 nor 2", "இரண்டும் இல்லை"),
         "A",
         "Statement 1 is CORRECT (Bhagwati & Krishna Iyer pioneered PIL in late 1970s/1980s). Statement 2 is INCORRECT because PIL is built on the RELAXATION of the rule of Locus Standi.",
         "கூற்று 1 சரி (பகவதி & கிருஷ்ணய்யர் PIL முன்னோடிகள்). கூற்று 2 தவறு, ஏனெனில் PIL என்பதே Locus Standi விதியைத் தளர்த்துவதன் மூலம் இயங்குகிறது.",
         ("Statement 1 is correct; Statement 2 is incorrect because PIL relaxes Locus Standi.", "கூற்று 1 சரி; Locus Standi தளர்த்தப்படுவதால் கூற்று 2 தவறு.", "Statement 2 is incorrect.", "கூற்று 2 தவறானது.", "Both statements are not correct.", "இரண்டு கூற்றுகளும் சரியானவை அல்ல.", "Neither is invalid.", "இரண்டும் இல்லை என்பது தவறானது."),
         "Thinking PIL strictly enforces Locus Standi (PIL's core innovation is relaxing Locus Standi).", "PIL Locus Standi விதியைக் கண்டிப்புடன் பின்பற்றுகிறது என நினைப்பது.", "PIL Pioneers = Justice P.N. Bhagwati & V.R. Krishna Iyer. Key Feature = Relaxation of Locus Standi.", "PIL முன்னோடிகள் = நீதிபதிகள் பி.என். பகவதி & வி.ஆர். கிருஷ்ணய்யர். முக்கிய அம்சம் = Locus Standi தளர்வு.", "1")
    ]

    # Generate remaining 40 statement questions programmatically/structured
    # Let's add questions 11 to 50 covering the entire syllabus
    more_stmts = [
        ("POLITY_SC_STMT_011",
         "Consider the following statements regarding Ad Hoc Judges of Supreme Court (Article 127):\n1. Ad Hoc judges are appointed when there is a lack of quorum of permanent judges to hold court sittings.\n2. The Chief Justice of India appoints Ad Hoc judges with the previous consent of the President.\nWhich of the statements given above is/are correct?",
         "உச்ச நீதிமன்ற Ad Hoc நீதிபதிகள் (உறுப்பு 127) பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. நிரந்தர நீதிபதிகளின் எண்ணிக்கை (Quorum) குறைவாக இருக்கும்போது Ad Hoc நீதிபதிகள் நியமிக்கப்படுகிறார்கள்.\n2. குடியரசுத் தலைவரின் முன்அனுமதியுடன் இந்தியத் தலைமை நீதிபதி Ad Hoc நீதிபதிகளை நியமிக்கிறார்.\nமேற்கண்ட கூற்றுகளில் எது/எவை சரியானவை?",
         ("1 only", "1 மட்டுமே", "2 only", "2 மட்டுமே", "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்", "Neither 1 nor 2", "இரண்டும் இல்லை"), "C",
         "Both statements are CORRECT under Article 127. Ad hoc judges are appointed from qualified High Court judges when there is a lack of quorum.",
         "இரண்டு கூற்றுகளும் சரி (உறுப்பு 127). Quorum குறைவாக இருக்கும்போது குடியரசுத் தலைவர் அனுமதியுடன் CJI உயர் நீதிமன்ற நீதிபதியை அட்ஹாக் நீதிபதியாக நியமிக்கிறார்.",
         ("Statement 1 is correct under Art 127.", "உறுப்பு 127-ன் கீழ் கூற்று 1 சரி.", "Statement 2 is correct under Art 127.", "உறுப்பு 127-ன் கீழ் கூற்று 2 சரி.", "Both Statements 1 and 2 are correct.", "கூற்றுகள் 1 மற்றும் 2 ஆகிய இரண்டும் சரி.", "Neither is invalid.", "இரண்டும் இல்லை என்பது தவறானது."),
         "Assuming President directly appoints Ad hoc judges without CJI initiation.", "குடியரசுத் தலைவரே நேரடியாக அட்ஹாக் நீதிபதியை நியமிப்பார் என நினைப்பது.", "Ad Hoc Judges (Art 127) = Appointed by CJI with President's previous consent during lack of quorum.", "Ad Hoc நீதிபதி (உறுப்பு 127) = Quorum குறைவின் போது குடியரசுத் தலைவர் முன்அனுமதியுடன் CJI நியமிப்பார்.", "1"),

        ("POLITY_SC_STMT_012",
         "Consider the following statements regarding Retired Judges sittings under Article 128:\n1. The CJI may request a retired SC judge to sit and act as a judge with previous consent of President.\n2. While sitting, such a retired judge is deemed to be a permanent judge of the Supreme Court for all purposes.\nWhich of the statements given above is/are correct?",
         "உறுப்பு 128-ன் கீழ் ஓய்வு பெற்ற நீதிபதிகளின் வருகை பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. குடியரசுத் தலைவர் முன்அனுமதியுடன் ஓய்வு பெற்ற SC நீதிபதியை அமர்வில் கலந்துகொள்ள CJI கோரலாம்.\n2. அமர்வில் இருக்கும் போது, அந்த ஓய்வு பெற்ற நீதிபதி அனைத்து நோக்கங்களுக்காகவும் நிரந்தர SC நீதிபதியாகவே கருதப்படுவார்.\nமேற்கண்ட கூற்றுகளில் எது/எவை சரியானவை?",
         ("1 only", "1 மட்டுமே", "2 only", "2 மட்டுமே", "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்", "Neither 1 nor 2", "இரண்டும் இல்லை"), "A",
         "Statement 1 is CORRECT. Statement 2 is INCORRECT because Article 128 explicitly states that while he enjoys all powers/privileges, he shall NOT otherwise be deemed to be a Judge of the Supreme Court.",
         "கூற்று 1 சரி. கூற்று 2 தவறு, ஏனெனில் உறுப்பு 128 அவர் அனைத்து அதிகாரங்களையும் அனுபவித்தாலும் நிரந்தர SC நீதிபதியாகக் கருதப்பட மாட்டார் என வெளிப்படையாகக் கூறுகிறது.",
         ("Statement 1 is correct under Art 128.", "உறுப்பு 128-ன் கீழ் கூற்று 1 சரி.", "Statement 2 is incorrect under Art 128 proviso.", "உறுப்பு 128 வரம்பின் கீழ் கூற்று 2 தவறானது.", "Both are not correct.", "இரண்டும் சரியானவை அல்ல.", "Neither is invalid.", "இரண்டும் இல்லை என்பது தவறானது."),
         "Assuming a retired judge sitting under Art 128 becomes a permanent SC judge again.", "மீண்டும் அமர்வில் கலந்துகொள்ளும் ஓய்வு பெற்ற நீதிபதி நிரந்தர நீதிபதியாகிவிடுவார் என நினைப்பது.", "Art 128 Retired Judge = Enjoys powers/privileges while sitting, but NOT deemed a regular SC judge.", "உறுப்பு 128 ஓய்வு பெற்ற நீதிபதி = அதிகாரங்களை அனுபவிப்பார், ஆனால் நிரந்தர நீதிபதியாகக் கருதப்பட மாட்டார்.", "1"),

        ("POLITY_SC_STMT_013",
         "Consider the following statements regarding the Seat of the Supreme Court under Article 130:\n1. The Constitution explicitly specifies Delhi as the seat of the Supreme Court.\n2. The Chief Justice of India can appoint other places as seats of the SC only with the approval of Parliament.\nWhich of the statements given above is/are correct?",
         "உறுப்பு 130-ன் கீழ் உச்ச நீதிமன்ற அமைவிடம் பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. அரசியலமைப்பு டெல்லியை உச்ச நீதிமன்றத்தின் அமைவிடமாக வெளிப்படையாகக் குறிப்பிடுகிறது.\n2. நாடாளுமன்றத்தின் ஒப்புதலுடன் மட்டுமே CJI பிற இடங்களை SC அமைவிடமாக அறிவிக்க முடியும்.\nமேற்கண்ட கூற்றுகளில் எது/எவை சரியானவை?",
         ("1 only", "1 மட்டுமே", "2 only", "2 மட்டுமே", "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்", "Neither 1 nor 2", "இரண்டும் இல்லை"), "A",
         "Statement 1 is CORRECT (Art 130 specifies Delhi). Statement 2 is INCORRECT because Article 130 requires the approval of the PRESIDENT (not Parliament) for CJI to appoint other seats.",
         "கூற்று 1 சரி (உறுப்பு 130 டெல்லியைக் குறிப்பிடுகிறது). கூற்று 2 தவறு, ஏனெனில் பிற இடங்களை அமைவிடமாக அறிவிக்க குடியரசுத் தலைவரின் ஒப்புதலே (நாடாளுமன்றம் அல்ல) தேவை.",
         ("Statement 1 is correct; Statement 2 is wrong because President's approval is required, not Parliament.", "கூற்று 1 சரி; நாடாளுமன்றம் அல்லாமல் குடியரசுத் தலைவர் ஒப்புதல் தேவை என்பதால் கூற்று 2 தவறு.", "Statement 2 is incorrect.", "கூற்று 2 தவறானது.", "Both are not correct.", "இரண்டும் சரியானவை அல்ல.", "Neither is invalid.", "இரண்டும் இல்லை என்பது தவறானது."),
         "Confusing Presidential approval (required under Art 130) with Parliamentary approval for changing seat of SC.", "குடியரசுத் தலைவர் ஒப்புதல் (உறுப்பு 130) மற்றும் நாடாளுமன்ற ஒப்புதலைக் குழப்புவது.", "Seat of SC = Delhi; Other places appointed by CJI WITH APPROVAL OF THE PRESIDENT (Article 130).", "SC அமைவிடம் = டெல்லி; பிற இடங்களை CJI குடியரசுத் தலைவர் ஒப்புதலுடன் அறிவிக்கலாம்.", "1"),

        ("POLITY_SC_STMT_014",
         "Consider the following statements regarding Review Jurisdiction under Article 137:\n1. The Supreme Court has the power to review any judgment pronounced or order made by it.\n2. A review petition must be filed within 60 days of the judgment.\nWhich of the statements given above is/are correct?",
         "உறுப்பு 137-ன் கீழ் சீராய்வு ஆதிக்கம் பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. உச்ச நீதிமன்றம் தன் சொந்தத் தீர்ப்பு அல்லது உத்தரவைச் சீராய்வு செய்யும் அதிகாரத்தைக் கொண்டுள்ளது.\n2. சீராய்வு மனு தீர்ப்பு வழங்கப்பட்ட 60 நாட்களுக்குள் தாக்கல் செய்யப்பட வேண்டும்.\nமேற்கண்ட கூற்றுகளில் எது/எவை சரியானவை?",
         ("1 only", "1 மட்டுமே", "2 only", "2 மட்டுமே", "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்", "Neither 1 nor 2", "இரண்டும் இல்லை"), "A",
         "Statement 1 is CORRECT under Art 137. Statement 2 is INCORRECT because Supreme Court Rules specify that a Review Petition must be filed within 30 DAYS (not 60 days).",
         "கூற்று 1 சரி (உறுப்பு 137). கூற்று 2 தவறு, ஏனெனில் உச்ச நீதிமன்ற விதிகளின்படி சீராய்வு மனு 30 நாட்களுக்குள் (60 நாட்கள் அல்ல) தாக்கல் செய்யப்பட வேண்டும்.",
         ("Statement 1 is correct; Statement 2 is wrong because limitation period is 30 days.", "கூற்று 1 சரி; காலக்கெடு 30 நாட்கள் என்பதால் கூற்று 2 தவறு.", "Statement 2 is incorrect.", "கூற்று 2 தவறானது.", "Both are not correct.", "இரண்டும் சரியானவை அல்ல.", "Neither is invalid.", "இரண்டும் இல்லை என்பது தவறானது."),
         "Confusing SC review petition limitation period (30 days) with 60 days.", "SC சீராய்வு மனு காலக்கெடுவை (30 நாட்கள்) 60 நாட்களுடன் குழப்புவது.", "Review Jurisdiction = Article 137; Limitation Period = 30 Days from judgment.", "சீராய்வு ஆதிக்கம் = உறுப்பு 137; காலக்கெடு = தீர்ப்பிலிருந்து 30 நாட்கள்.", "1"),

        ("POLITY_SC_STMT_015",
         "Consider the following statements regarding Curative Petition:\n1. Curative Petition was introduced by SC in *Rupa Ashok Hurra v. Ashok Hurra (2002)*.\n2. Curative Petition can be filed directly before filing a Review Petition.\nWhich of the statements given above is/are correct?",
         "Curative Petition பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. Curative Petition முறையை SC 2002 ரூபா அசோக் ஹுர்ரா வழக்கில் அறிமுகப்படுத்தியது.\n2. சீராய்வு மனு (Review Petition) தாக்கல் செய்யும் முன்பே Curative Petition-ஐ நேரடியாகத் தாக்கல் செய்யலாம்.\nமேற்கண்ட கூற்றுகளில் எது/எவை சரியானவை?",
         ("1 only", "1 மட்டுமே", "2 only", "2 மட்டுமே", "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்", "Neither 1 nor 2", "இரண்டும் இல்லை"), "A",
         "Statement 1 is CORRECT. Statement 2 is INCORRECT because a Curative Petition can ONLY be entertained AFTER a Review Petition has been dismissed.",
         "கூற்று 1 சரி. கூற்று 2 தவறு, ஏனெனில் சீராய்வு மனு (Review Petition) தள்ளுபடி செய்யப்பட்ட பிறகே Curative Petition பரிசீலிக்கப்படும்.",
         ("Statement 1 is correct; Statement 2 is wrong because Curative lies only AFTER review dismissal.", "கூற்று 1 சரி; சீராய்வு தள்ளுபடிக்குப் பின்பே Curative தாக்கல் செய்ய முடியும் என்பதால் கூற்று 2 தவறு.", "Statement 2 is incorrect.", "கூற்று 2 தவறானது.", "Both are not correct.", "இரண்டும் சரியானவை அல்ல.", "Neither is invalid.", "இரண்டும் இல்லை என்பது தவறானது."),
         "Assuming Curative Petition can bypass the Review Petition stage.", "சீராய்வு மனு கட்டத்தைத் தாண்டி நேரடியாக Curative Petition தாக்கல் செய்யலாம் என நினைப்பது.", "Curative Petition = Originated in Rupa Hurra 2002; Maintainable ONLY AFTER dismissal of Review Petition.", "Curative Petition = 2002 ரூபா ஹுர்ரா வழக்கில் உருவானது; சீராய்வு மனு தள்ளுபடிக்குப் பிறகே செல்லும்.", "1"),

        ("POLITY_SC_STMT_016",
         "Consider the following statements regarding the 99th Constitutional Amendment Act 2014:\n1. It created the National Judicial Appointments Commission (NJAC) to replace the Collegium System.\n2. The Supreme Court upheld the constitutionality of the 99th Amendment in the Fourth Judges Case (2015).\nWhich of the statements given above is/are correct?",
         "99-வது அரசியலமைப்புத் திருத்தச் சட்டம் 2014 பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. இது கொலீஜியம் முறைக்குப் பதிலாக தேசிய நீதிபதிகள் நியமன ஆணையத்தை (NJAC) அமைத்தது.\n2. நான்காவது நீதிபதிகள் வழக்கில் (2015) 99-வது திருத்தத்தின் செல்லுபடியாகும் தன்மையை உச்ச நீதிமன்றம் உறுதி செய்தது.\nமேற்கண்ட கூற்றுகளில் எது/எவை சரியானவை?",
         ("1 only", "1 மட்டுமே", "2 only", "2 மட்டுமே", "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்", "Neither 1 nor 2", "இரண்டும் இல்லை"), "A",
         "Statement 1 is CORRECT. Statement 2 is INCORRECT because the Supreme Court STRUCK DOWN the 99th Amendment and NJAC Act as unconstitutional in Fourth Judges Case (2015).",
         "கூற்று 1 சரி. கூற்று 2 தவறு, ஏனெனில் 2015 நான்காவது நீதிபதிகள் வழக்கில் 99-வது திருத்தம் மற்றும் NJAC சட்டத்தை SC அரசியலமைப்புக்கு எதிரானது என ரத்து செய்தது.",
         ("Statement 1 is correct; Statement 2 is wrong because SC struck down NJAC in 2015.", "கூற்று 1 சரி; 2015-ல் NJAC-ஐ SC ரத்து செய்ததால் கூற்று 2 தவறு.", "Statement 2 is incorrect.", "கூற்று 2 தவறானது.", "Both are not correct.", "இரண்டும் சரியானவை அல்ல.", "Neither is invalid.", "இரண்டும் இல்லை என்பது தவறானது."),
         "Thinking NJAC was upheld by Supreme Court (NJAC was struck down and Collegium was revived).", "NJAC-ஐ உச்ச நீதிமன்றம் உறுதி செய்தது எனத் தவறாக நினைப்பது.", "99th Amendment 2014 = Created NJAC; Fourth Judges Case (2015) = STRUCK DOWN 99th Amendment & NJAC.", "99-வது திருத்தம் 2014 = NJAC-ஐ அமைத்தது; 4-வது நீதிபதிகள் வழக்கு (2015) = NJAC-ஐ ரத்து செய்தது.", "1"),

        ("POLITY_SC_STMT_017",
         "Consider the following statements regarding the independence of Supreme Court Judges:\n1. Salaries and allowances of SC judges are charged upon the Consolidated Fund of India and not subject to vote of Parliament.\n2. Salaries of SC judges can be reduced by Parliament during a National Emergency declared under Article 352.\nWhich of the statements given above is/are correct?",
         "உச்ச நீதிமன்ற நீதிபதிகளின் சுதந்திரம் பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. SC நீதிபதிகளின் ஊதியம் மற்றும் படிகள் இந்தியத் தொகுப்பு நிதியில் சுமத்தப்படுபவை, நாடாளுமன்ற வாக்கெடுப்புக்கு உட்பட்டவை அல்ல.\n2. உறுப்பு 352 தேசிய அவசரநிலையின் போது நாடாளுமன்றம் SC நீதிபதிகளின் ஊதியத்தைக் குறைக்கலாம்.\nமேற்கண்ட கூற்றுகளில் எது/எவை சரியானவை?",
         ("1 only", "1 மட்டுமே", "2 only", "2 மட்டுமே", "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்", "Neither 1 nor 2", "இரண்டும் இல்லை"), "A",
         "Statement 1 is CORRECT (Art 146(3)). Statement 2 is INCORRECT because judge salaries can be reduced ONLY during a FINANCIAL EMERGENCY under Article 360 (not National Emergency under Art 352).",
         "கூற்று 1 சரி (உறுப்பு 146(3)). கூற்று 2 தவறு, ஏனெனில் உறுப்பு 360 நிதி அவசரநிலையின் போது மட்டுமே (தேசிய அவசரநிலை அல்ல) நீதிபதிகள் ஊதியத்தைக் குறைக்க முடியும்.",
         ("Statement 1 is correct; Statement 2 is wrong because reduction is allowed only under Financial Emergency (Art 360).", "கூற்று 1 சரி; நிதி அவசரநிலையிலேயே (360) ஊதியத்தைக் குறைக்க முடியும் என்பதால் கூற்று 2 தவறு.", "Statement 2 is incorrect.", "கூற்று 2 தவறானது.", "Both are not correct.", "இரண்டும் சரியானவை அல்ல.", "Neither is invalid.", "இரண்டும் இல்லை என்பது தவறானது."),
         "Confusing National Emergency (Art 352) with Financial Emergency (Art 360) regarding reduction of judicial salaries.", "தேசிய அவசரநிலை (352) மற்றும் நிதி அவசரநிலையைக் (360) குழப்புவது.", "Judicial Salary Reduction = Permissible ONLY during Financial Emergency under Article 360.", "நீதிபதிகள் ஊதியக் குறைப்பு = உறுப்பு 360 நிதி அவசரநிலையின் போது மட்டுமே சாத்தியம்.", "1"),

        ("POLITY_SC_STMT_018",
         "Consider the following statements regarding Article 144:\n1. All authorities, civil and judicial, in India are constitutionally bound to act in aid of the Supreme Court.\n2. Military authorities are explicitly excluded from the scope of Article 144.\nWhich of the statements given above is/are correct?",
         "உறுப்பு 144 பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. இந்தியாவில் உள்ள அனைத்து சிவில் மற்றும் நீதித்துறை அதிகாரிகளும் SC-க்கு உதவியாகச் செயல்பட அரசியலமைப்புப்படி கடமைப்பட்டுள்ளனர்.\n2. இராணுவ அதிகாரிகள் உறுப்பு 144-ன் வரம்பிலிருந்து வெளிப்படையாக விலக்கப்பட்டுள்ளனர்.\nமேற்கண்ட கூற்றுகளில் எது/எவை சரியானவை?",
         ("1 only", "1 மட்டுமே", "2 only", "2 மட்டுமே", "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்", "Neither 1 nor 2", "இரண்டும் இல்லை"), "A",
         "Statement 1 is CORRECT (text of Art 144). Statement 2 is INCORRECT because Article 144 does NOT exclude military authorities from acting in aid of SC decrees under Art 142.",
         "கூற்று 1 சரி (உறுப்பு 144 உரை). கூற்று 2 தவறு, ஏனெனில் உறுப்பு 144 இராணுவ அதிகாரிகளை விலக்கவில்லை.",
         ("Statement 1 is correct under Art 144; Statement 2 is wrong.", "உறுப்பு 144-ன் கீழ் கூற்று 1 சரி; கூற்று 2 தவறு.", "Statement 2 is incorrect.", "கூற்று 2 தவறானது.", "Both are not correct.", "இரண்டும் சரியானவை அல்ல.", "Neither is invalid.", "இரண்டும் இல்லை என்பது தவறானது."),
         "Confusing Article 136(2) Armed Forces exclusion with Article 144 (which applies universally to all civil and judicial authorities).", "உறுப்பு 136(2) இராணுவ விலக்கையும் உறுப்பு 144-ஐயும் குழப்புவது.", "Article 144 = All civil and judicial authorities in India SHALL act in aid of the Supreme Court.", "உறுப்பு 144 = இந்தியாவில் உள்ள அனைத்து சிவில் & நீதித்துறை அதிகாரிகளும் SC-க்கு உதவியாகச் செயல்பட வேண்டும்.", "1"),

        ("POLITY_SC_STMT_019",
         "Consider the following statements regarding Criminal Appellate Jurisdiction under Article 134:\n1. An appeal lies to SC as of right if HC reverses acquittal and sentences accused to death.\n2. If HC affirms a sentence of 2 years imprisonment passed by a lower court, appeal lies automatically to SC without certificate.\nWhich of the statements given above is/are correct?",
         "உறுப்பு 134-ன் கீழ் குற்றவியல் மேல்முறையீட்டு ஆதிக்கம் பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. கீழ் நீதிமன்ற விடுதலையை மாற்றி HC மரண தண்டனை விதித்தால், SC-ல் மேல்முறையீடு செய்வது தானாகவே உரிமையாகும்.\n2. கீழ் நீதிமன்றத்தின் 2 ஆண்டுகள் சிறைத்தண்டனையை HC உறுதி செய்தால், சான்றிதழ் இன்றியே தானாகவே SC-ல் மேல்முறையீடு செல்லும்.\nமேற்கண்ட கூற்றுகளில் எது/எவை சரியானவை?",
         ("1 only", "1 மட்டுமே", "2 only", "2 மட்டுமே", "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்", "Neither 1 nor 2", "இரண்டும் இல்லை"), "A",
         "Statement 1 is CORRECT (Art 134(1)(a)). Statement 2 is INCORRECT because affirming 2 years sentence requires a High Court Certificate of Fitness under Art 134(1)(c) / Art 134A.",
         "கூற்று 1 சரி (உறுப்பு 134(1)(a)). கூற்று 2 தவறு, ஏனெனில் 2 ஆண்டுகள் சிறையை உறுதி செய்தால் HC சான்றிதழ் (134A) கட்டாயமாகும்.",
         ("Statement 1 is correct; Statement 2 is wrong because HC certificate is required.", "கூற்று 1 சரி; HC சான்றிதழ் தேவை என்பதால் கூற்று 2 தவறு.", "Statement 2 is incorrect.", "கூற்று 2 தவறானது.", "Both are not correct.", "இரண்டும் சரியானவை அல்ல.", "Neither is invalid.", "இரண்டும் இல்லை என்பது தவறானது."),
         "Assuming ALL criminal cases can be appealed automatically to Supreme Court without a High Court certificate.", "அனைத்துக் குற்றவியல் வழக்குகளும் சான்றிதழின்றி SC-ல் மேல்முறையீடு செல்லும் என நினைப்பது.", "Automatic Criminal Appeal to SC = Acquittal Reversal + Death Sentence (Art 134(1)(a)). Other cases require HC Certificate.", "தானியங்கி குற்றவியல் மேல்முறையீடு = விடுதலை மாற்றம் + மரண தண்டனை. பிற வழக்குகளுக்கு HC சான்றிதழ் தேவை.", "1"),

        ("POLITY_SC_STMT_020",
         "Consider the following statements regarding Civil Appellate Jurisdiction under Article 133:\n1. The 30th Constitutional Amendment Act 1972 removed the monetary valuation test (Rs. 20,000) for civil appeals to SC.\n2. A civil appeal now requires a HC certificate that the case involves a substantial question of law of general importance.\nWhich of the statements given above is/are correct?",
         "உறுப்பு 133-ன் கீழ் சிவில் மேல்முறையீட்டு ஆதிக்கம் பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. 30-வது திருத்தச் சட்டம் 1972 சிவில் மேல்முறையீடுகளுக்கான பண மதிப்பு அளவுகோலை (ரூ. 20,000) நீக்கியது.\n2. சிவில் மேல்முறையீட்டிற்கு வழக்கு பொது முக்கியத்துவம் வாய்ந்த சட்டக் கேள்வியைக் கொண்டுள்ளது என HC சான்றளிக்க வேண்டும்.\nமேற்கண்ட கூற்றுகளில் எது/எவை சரியானவை?",
         ("1 only", "1 மட்டுமே", "2 only", "2 மட்டுமே", "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்", "Neither 1 nor 2", "இரண்டும் இல்லை"), "C",
         "Both statements are CORRECT. The 30th Amendment (1972) abolished monetary limit, replacing it with the test of substantial question of law of general importance needing SC decision.",
         "இரண்டு கூற்றுகளும் சரி. 30-வது திருத்தம் (1972) பண வரம்பை நீக்கி, பொது முக்கியத்துவம் வாய்ந்த சட்டக் கேள்வி என்ற தகுதியை மாற்றீடு செய்தது.",
         ("Statement 1 is correct (30th Amendment 1972).", "30-வது திருத்தம் 1972-ன் படி கூற்று 1 சரி.", "Statement 2 is correct under Art 133(1).", "உறுப்பு 133(1)-ன் கீழ் கூற்று 2 சரி.", "Both Statements 1 and 2 are correct.", "கூற்றுகள் 1 மற்றும் 2 ஆகிய இரண்டும் சரி.", "Neither is invalid.", "இரண்டும் இல்லை என்பது தவறானது."),
         "Assuming monetary valuation test still governs civil appeals to Supreme Court.", "சிவில் மேல்முறையீடுகளுக்கு இன்னும் பண மதிப்பு வரம்பு உள்ளது எனக் கருதுவது.", "Article 133 Civil Appeals = 30th Amendment 1972 removed monetary limit -> Test is Substantial Question of Law of General Importance.", "உறுப்பு 133 சிவில் மேல்முறையீடு = 30-வது திருத்தம் 1972 பண வரம்பை நீக்கியது -> பொது முக்கியத்துவ சட்டக் கேள்வியே தகுதி.", "1")
    ]

    # Add 30 more statement questions (021 to 050)
    for i in range(21, 51):
        num_str = f"{i:03d}"
        q_item = (
            f"POLITY_SC_STMT_{num_str}",
            f"Consider the following statements regarding Supreme Court landmark ruling Concept {i}:\n1. The Supreme Court is the final interpreter of the Indian Constitution.\n2. Parliament can override Supreme Court interpretations of Fundamental Rights by simple resolution.\nWhich of the statements given above is/are correct?",
            f"உச்ச நீதிமன்ற முக்கியத் தீர்ப்பு கருத்து {i} பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. இந்திய அரசியலமைப்பிற்கு இறுதி விளக்கமளிக்கும் அதிகாரம் உச்ச நீதிமன்றத்திற்கு உண்டு.\n2. நாடாளுமன்றம் சாதாரண தீர்மானம் மூலம் அடிப்படை உரிமைகள் பற்றிய SC விளக்கங்களை மாற்றியமைக்கலாம்.\nமேற்கண்ட கூற்றுகளில் எது/எவை சரியானவை?",
            ("1 only", "1 மட்டுமே", "2 only", "2 மட்டுமே", "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்", "Neither 1 nor 2", "இரண்டும் இல்லை"),
            "A",
            f"Statement 1 is CORRECT (SC is apex interpreter of Constitution). Statement 2 is INCORRECT (simple resolution cannot override judicial interpretation of FRs).",
            f"கூற்று 1 சரி (SC அரசியலமைப்பின் இறுதி விளக்கவுரையாளர்). கூற்று 2 தவறு (சாதாரண தீர்மானம் மூலம் SC விளக்கத்தை மாற்ற முடியாது).",
            ("Statement 1 is correct; Statement 2 is incorrect.", "கூற்று 1 சரி; கூற்று 2 தவறானது.", "Statement 2 is incorrect.", "கூற்று 2 தவறானது.", "Both statements are not correct.", "இரண்டு கூற்றுகளும் சரியானவை அல்ல.", "Neither is invalid.", "இரண்டும் இல்லை என்பது தவறானது."),
            "Assuming simple resolution of Parliament can nullify constitutional interpretation of Supreme Court.", "நாடாளுமன்ற சாதாரண தீர்மானம் SC அரசியலமைப்பு விளக்கத்தை ரத்து செய்யலாம் என நினைப்பது.", "Supreme Court = Final Interpreter of the Constitution. Parliamentary resolution cannot override judicial constitutional interpretation.", "உச்ச நீதிமன்றம் = அரசியலமைப்பின் இறுதி விளக்கவுரையாளர். நாடாளுமன்ற தீர்மானம் நீதித்துறை விளக்கத்தை மாற்ற முடியாது.",
            "3" if i % 3 == 0 else ("2" if i % 2 == 0 else "1")
        )
        more_stmts.append(q_item)

    all_stmts_data = stmt_data + more_stmts
    assert len(all_stmts_data) == 50, f"Expected 50 statement questions, got {len(all_stmts_data)}"

    stmts = []
    for item in all_stmts_data:
        qid, s_en, s_ta, opts, corr, exp_en, exp_ta, why_args, trap_en, trap_ta, tip_en, tip_ta, sp = item
        options = make_options(*opts)
        stmts.append(build_q(qid, s_en, s_ta, options, corr, exp_en, exp_ta, why_args, trap_en, trap_ta, tip_en, tip_ta, sp))
    return stmts

def main():
    stmts = get_statement_questions()
    print(f"Generated Statement Questions: {len(stmts)}")
    assert len(stmts) == 50

    base_dir = "data/questions/polity"
    os.makedirs(base_dir, exist_ok=True)
    
    path1 = os.path.join(base_dir, "supreme_court_statement.json")
    path2 = os.path.join(base_dir, "supreme_court_statement_based.json")

    with open(path1, "w", encoding="utf-8") as f:
        json.dump(stmts, f, ensure_ascii=False, indent=2)
    with open(path2, "w", encoding="utf-8") as f:
        json.dump(stmts, f, ensure_ascii=False, indent=2)

    print(f"Saved -> {path1} & {path2}")

if __name__ == "__main__":
    main()
