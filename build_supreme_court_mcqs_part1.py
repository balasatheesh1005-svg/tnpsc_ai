# -*- coding: utf-8 -*-
"""
Full Dataset Generator for Supreme Court of India Part 1 MCQs (150 Questions)
Easy = 50, Medium = 50, Hard = 50
Generates:
- data/questions/polity/supreme_court_easy.json
- data/questions/polity/supreme_court_medium.json
- data/questions/polity/supreme_court_hard.json
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


def get_hard_questions():
    hard_data = [
        ("POLITY_SC_HARD_001", "Hard",
         "A suit under Article 131 (Original Jurisdiction of the Supreme Court) CANNOT be entertained if it is filed by which of the following parties?",
         "அரசியலமைப்பு உறுப்பு 131-ன் கீழ் (மூல ஆதிக்கம்) தாக்கல் செய்யப்படும் வழக்கினை, எந்தத் தரப்பினர் தாக்கல் செய்தால் உச்ச நீதிமன்றம் விசாரிக்க முடியாது?",
         ("A private individual or a statutory corporation against the Government of India", "ஒரு தனிநபர் அல்லது சட்டப்பூர்வக் கழகம் இந்திய அரசிற்கு எதிராகத் தாக்கல் செய்தால்", "The State of West Bengal against the Union of India", "மேற்கு வங்க மாநிலம் இந்திய ஒன்றியத்திற்கு எதிராகத் தாக்கல் செய்தால்", "The State of Tamil Nadu against the State of Karnataka", "தமிழ்நாடு மாநிலம் கர்நாடக மாநிலத்திற்கு எதிராகத் தாக்கல் செய்தால்", "A group of States against the Union Government", "மாநிலங்களின் குழு ஒன்றிய அரசிற்கு எதிராகத் தாக்கல் செய்தால்"),
         "A",
         "Under Article 131, Original Jurisdiction applies EXCLUSIVELY to federal disputes between units of the federation (Centre vs State, State vs State). A private individual or corporation cannot file a suit against the Union/State under Art 131.",
         "உறுப்பு 131-ன் கீழ் மூல ஆதிக்கம் கூட்டாட்சி அமைப்புகளுக்கு (ஒன்றியம் vs மாநிலம், மாநிலம் vs மாநிலம்) இடையேயான தகராறுகளுக்கு மட்டுமே பொருந்தும். ஒரு தனிநபரோ அல்லது கழகமோ உறுப்பு 131-ன் கீழ் வழக்கு தாக்கல் செய்ய முடியாது.",
         ("A private individual/corporation CANNOT be a party to an Art 131 suit.", "தனிநபர்/கழகம் உறுப்பு 131 வழக்கில் தரப்பினராக இருக்க முடியாது.", "State vs Union suit IS maintainable under Art 131.", "மாநிலம் vs ஒன்றியம் வழக்கு உறுப்பு 131-ன் கீழ் செல்லும்.", "State vs State suit IS maintainable under Art 131.", "மாநிலம் vs மாநிலம் வழக்கு உறுப்பு 131-ன் கீழ் செல்லும்.", "Group of States vs Union IS maintainable under Art 131.", "மாநிலங்களின் குழு vs ஒன்றியம் வழக்கு செல்லும்."),
         "Thinking private individuals can join a suit under Article 131 Original Jurisdiction.", "தனிநபர்கள் உறுப்பு 131 மூல ஆதிக்க வழக்கில் இணையலாம் எனத் தவறாக நினைத்தல்.", "Art 131 Original Jurisdiction Parties = ONLY Units of Federation (Union & States). Private bodies/individuals strictly barred.", "உறுப்பு 131 தரப்பினர்கள் = ஒன்றியம் மற்றும் மாநிலங்கள் மட்டுமே.", "2"),

        ("POLITY_SC_HARD_002", "Hard",
         "For a legal dispute between the Union and a State to lie under the Original Jurisdiction of Article 131, what essential condition must be satisfied?",
         "அரசியலமைப்பு உறுப்பு 131-ன் கீழ் ஒன்றியம் மற்றும் மாநிலத்திற்கு இடையே வழக்கு செல்லுபடியாக என்ன அத்தியாவசிய நிபந்தனை நிறைவு செய்யப்பட வேண்டும்?",
         ("The dispute must involve a political disagreement between ruling parties", "தகராறு ஆளும் கட்சிகளுக்கிடையேயான அரசியல் கருத்து வேறுபாடாக இருக்க வேண்டும்", "The dispute must involve a question of law or fact on which the existence or extent of a LEGAL RIGHT depends", "தகராறு ஒரு சட்ட உரிமையின் இருப்பு அல்லது எல்லையைத் தீர்மானிக்கும் சட்ட அல்லது உண்மை கேள்வியைக் கொண்டிருக்க வேண்டும்", "The dispute must have been approved by the Governor of the State", "தகராறிற்கு மாநில ஆளுநர் ஒப்புதல் அளித்திருக்க வேண்டும்", "The dispute must relate exclusively to international border agreements", "தகராறு சர்வதேச எல்லை உடன்படிக்கைகள் பற்றியதாக மட்டுமே இருக்க வேண்டும்"),
         "B",
         "Article 131 explicitly mandates that the dispute must involve any question (whether of law or fact) on which the existence or extent of a LEGAL RIGHT depends (State of West Bengal v. UOI 1963). Purely political questions are excluded.",
         "அரசியலமைப்பு உறுப்பு 131, தகராறானது ஒரு சட்ட உரிமையின் (Legal Right) இருப்பு அல்லது எல்லையைத் தீர்மானிக்கும் சட்ட அல்லது உண்மை கேள்வியைக் கொண்டிருக்க வேண்டும் எனக் கட்டாயமாக்குகிறது.",
         ("Political disagreements without legal rights are excluded.", "சட்ட உரிமை இல்லாத அரசியல் கருத்து வேறுபாடுகள் விலக்கப்படும்.", "Question of Law or Fact determining existence/extent of a LEGAL RIGHT is the mandatory constitutional condition.", "சட்ட உரிமையை தீர்மானிக்கும் சட்டக் கேள்வி என்பது கட்டாய நிபந்தனையாகும்.", "Governor approval is not required under Art 131.", "ஆளுநர் ஒப்புதல் தேவையில்லை.", "International border agreements are excluded under Art 131 proviso.", "சர்வதேச எல்லை உடன்படிக்கைகள் விலக்கப்படும்."),
         "Confusing political disputes (non-justiciable under Art 131) with disputes involving legal rights (justiciable under Art 131).", "அரசியல் தகராறுகளையும் சட்ட உரிமை தகராறுகளையும் குழப்புதல்.", "Art 131 Condition = Must involve a LEGAL RIGHT (State of WB v. UOI 1963). Political/party disputes barred.", "உறுப்பு 131 நிபந்தனை = ஒரு சட்ட உரிமை (Legal Right) சார்ந்ததாக இருக்க வேண்டும்.", "2"),

        ("POLITY_SC_HARD_003", "Hard",
         "Which of the following statements regarding the Special Leave Petition (SLP) under Article 136 of the Indian Constitution is INCORRECT?",
         "இந்திய அரசியலமைப்பு உறுப்பு 136-ன் கீழ் சிறப்பு விடுப்பு மனு (SLP) பற்றிய எந்தக் கூற்று தவறானது?",
         ("SLP is a discretionary power of the Supreme Court, not a statutory right of appeal of the party", "SLP என்பது உச்ச நீதிமன்றத்தின் விருப்பவுரிமை அதிகாரம், மனுதாரரின் சட்டப்பூர்வ உரிமை அல்ல", "SLP can be granted against final as well as interlocutory orders of any court or tribunal", "எந்தவொரு நீதிமன்றம் அல்லது தீர்ப்பாயத்தின் இறுதி மற்றும் இடைக்கால உத்தரவுகளுக்கு எதிராகவும் SLP வழங்கப்படலாம்", "SLP is a regular third appeal available automatically in all civil and criminal cases", "SLP என்பது அனைத்து சிவில் மற்றும் குற்றவியல் வழக்குகளிலும் தானாகக் கிடைக்கும் வழக்கமான 3-வது மேல்முறையீடு ஆகும்", "SLP does not apply to Armed Forces Courts Martial decisions", "இராணுவ நீதிமன்றத் தீர்ப்புகளுக்கு SLP பொருந்தாது"),
         "C",
         "Article 136 confers an extraordinary, discretionary appellate power on the Supreme Court. It is NOT a regular or statutory right of appeal available automatically to litigants.",
         "அரசியலமைப்பு உறுப்பு 136 உச்ச நீதிமன்றத்திற்கு ஒரு விதிவிலக்கான விருப்பவுரிமை மேல்முறையீட்டு அதிகாரத்தை வழங்குகிறது. இது வழக்குதாரர்களுக்கு தானாகக் கிடைக்கும் வழக்கமான மேல்முறையீட்டு உரிமை அல்ல.",
         ("SLP is indeed discretionary, not a right of appeal.", "SLP என்பது விருப்பவுரிமை அதிகாரம், சட்ட உரிமை அல்ல.", "SLP applies to final and interlocutory orders.", "SLP இறுதி மற்றும் இடைக்கால உத்தரவுகளுக்குப் பொருந்தும்.", "SLP is NOT a regular third appeal available automatically (Hence C is incorrect).", "SLP வழக்கமான 3-வது மேல்முறையீடு அல்ல (எனவே C தவறான கூற்றாகும்).", "Armed Forces Courts Martial are explicitly excluded under Art 136(2).", "இராணுவ நீதிமன்றங்கள் விலக்கப்பட்டுள்ளன."),
         "Treating Special Leave Petition under Article 136 as an ordinary or regular right of appeal.", "உறுப்பு 136 SLP-ஐ வழக்கமான மேல்முறையீட்டு உரிமையாகக் கருதுதல்.", "Art 136 SLP = Plenary Discretionary Power of Supreme Court (Not a right of appeal).", "உறுப்பு 136 SLP = உச்ச நீதிமன்றத்தின் முழுமையான விருப்பவுரிமை அதிகாரம் (மேல்முறையீட்டு உரிமை அல்ல).", "2"),

        ("POLITY_SC_HARD_004", "Hard",
         "What distinguishes an appeal under Articles 132, 133, and 134 from a Special Leave Petition under Article 136?",
         "அரசியலமைப்பு உறுப்புகள் 132, 133, 134-ன் கீழ் வரும் மேல்முறையீட்டை உறுப்பு 136-ன் கீழ் வரும் சிறப்பு விடுப்பு மனுவிலிருந்து (SLP) வேறுபடுத்துவது எது?",
         ("Appeals under Articles 132-134 require a High Court Certificate under Art 134A, whereas Article 136 enables the Supreme Court to grant leave directly without a High Court Certificate", "உறுப்புகள் 132-134 மேல்முறையீட்டிற்கு உயர் நீதிமன்ற சான்றிதழ் தேவை, ஆனால் உறுப்பு 136 சான்றிதழ் இன்றியே நேரடியாக SC அனுமதி வழங்க வழிசெய்கிறது", "Articles 132-134 apply only to criminal cases, while Article 136 applies only to civil cases", "உறுப்புகள் 132-134 குற்றவியல் வழக்குகளுக்கும், உறுப்பு 136 சிவில் வழக்குகளுக்கும் மட்டுமே பொருந்தும்", "Article 136 requires Parliamentary approval for each petition", "உறுப்பு 136-க்கு ஒவ்வொரு மனுவிற்கும் நாடாளுமன்ற ஒப்புதல் தேவை", "Articles 132-134 apply only to Union Territories", "உறுப்புகள் 132-134 ஒன்றிய பிரதேசங்களுக்கு மட்டுமே பொருந்தும்"),
         "D",
         "Appeals under Arts 132-134 follow statutory conditions and generally require a High Court Certificate under Art 134A. In contrast, Art 136 bypasses the High Court certificate requirement and allows SC to grant leave directly at its discretion.",
         "உறுப்புகள் 132-134 கீழ் வரும் மேல்முறையீடுகளுக்கு 134A சான்றிதழ் தேவை. மாறாக, உறுப்பு 136 உயர் நீதிமன்ற சான்றிதழ் தேவையின்றி நேரடியாக உச்ச நீதிமன்றம் தன் விருப்பப்படி அனுமதி வழங்க வழிவகை செய்கிறது.",
         ("Articles 132-134 require HC certificate under Art 134A, while Art 136 grants leave directly without HC certificate.", "உறுப்புகள் 132-134-க்கு சான்றிதழ் தேவை, உறுப்பு 136-க்கு சான்றிதழ் தேவையின்றி SC நேரடியாக அனுமதி அளிக்கும்.", "Arts 132-134 cover constitutional, civil and criminal cases.", "உறுப்புகள் 132-134 அரசியலமைப்பு, சிவில் மற்றும் குற்றவியல் மூன்றுக்கும் பொருந்தும்.", "Parliamentary approval is not needed for Art 136.", "நாடாளுமன்ற ஒப்புதல் தேவையில்லை.", "Arts 132-134 apply nationwide, not just UTs.", "நாடு முழுமைக்கும் பொருந்தும்."),
         "Thinking that every appeal to the Supreme Court requires a High Court certificate.", "உச்ச நீதிமன்றத்திற்கான அனைத்து மேல்முறையீடுகளுக்கும் உயர் நீதிமன்ற சான்றிதழ் கட்டாயம் என நினைத்தல்.", "Art 132-134 Appeals -> Require High Court Certificate (Art 134A); Art 136 SLP -> Overrides requirement of High Court Certificate.", "உறுப்பு 132-134 = HC சான்றிதழ் தேவை; உறுப்பு 136 SLP = HC சான்றிதழ் தேவையில்லை.", "2"),

        ("POLITY_SC_HARD_005", "Hard",
         "Under Article 134(1) of the Constitution, an appeal in a criminal proceeding lies as of right to the Supreme Court WITHOUT a High Court certificate in which of the following specific instances?",
         "அரசியலமைப்பு உறுப்பு 134(1)-ன் கீழ், உயர் நீதிமன்ற சான்றிதழ் இன்றியே ஒரு குற்றவியல் வழக்கில் உச்ச நீதிமன்றத்திற்கு சட்டப்பூர்வ உரிமையாக மேல்முறையீடு எப்போது செல்லும்?",
         ("If the High Court has on appeal reversed an order of acquittal of an accused and sentenced him to death", "உயர் நீதிமன்றம் மேல்முறையீட்டில் எதிரியின் விடுதலை உத்தரவை மாற்றி அவருக்கு மரண தண்டனை விதித்திருந்தால்", "If the High Court has withdrawn a case from a subordinate court and convicted the accused sentencing him to death", "உயர் நீதிமன்றம் கீழமை நீதிமன்ற வழக்கைத் தனக்கு மாற்றி எதிரிக்கு மரண தண்டனை விதித்திருந்தால்", "Both A and B instances", "கூற்றுகள் A மற்றும் B ஆகிய இரண்டு நிகழ்வுகளிலும்", "If the accused pays a security deposit of Rs. 1 Lakh in Supreme Court", "எதிரி 1 லட்சம் ரூபாய் பிணைத்தொகை செலுத்தினால்"),
         "C",
         "Article 134(1)(a) & (b) grant a constitutional right of criminal appeal without HC certificate if High Court: (a) reversed acquittal and sentenced to death, or (b) withdrew case from subordinate court, convicted and sentenced to death.",
         "அரசியலமைப்பு உறுப்பு 134(1)(a) & (b), உயர் நீதிமன்ற சான்றிதழ் இன்றியே குற்றவியல் மேல்முறையீட்டு உரிமையை வழங்குகிறது: (a) விடுதலையை மாற்றி மரண தண்டனை விதித்தால், அல்லது (b) வழக்கைத் தனக்கு மாற்றி மரண தண்டனை விதித்தால்.",
         ("Reversal of acquittal to death sentence is Art 134(1)(a) instance.", "விடுதலையை மாற்றி மரண தண்டனை உறுப்பு 134(1)(a) நிகழ்வு.", "Withdrawal of case and death sentence is Art 134(1)(b) instance.", "வழக்கை மாற்றி மரண தண்டனை உறுப்பு 134(1)(b) நிகழ்வு.", "Both A and B are the exact constitutional instances under Art 134(1) where criminal appeal lies as of right without certificate.", "கூற்றுகள் A மற்றும் B ஆகிய இரண்டும் சான்றிதழ் இன்றி மேல்முறையீடு செல்லும் நிகழ்வுகளாகும்.", "Security deposit is irrelevant to constitutional jurisdiction.", "பிணைத்தொகை தொடர்பில்லாதது."),
         "Thinking that a criminal appeal to SC without HC certificate lies in all murder conviction cases.", "அனைத்துக் கொலை வழக்குகளிலும் HC சான்றிதழ் இன்றி SC-க்கு மேல்முறையீடு செல்லலாம் என நினைத்தல்.", "Art 134(1)(a)&(b) Appeals as of Right -> ONLY when High Court imposes DEATH SENTENCE (by reversing acquittal or withdrawing case).", "உறுப்பு 134(1) சட்டப்பூர்வ மேல்முறையீடு -> உயர் நீதிமன்றம் மரண தண்டனை விதித்தால் மட்டுமே சான்றிதழ் இன்றி செல்லும்.", "2"),

        ("POLITY_SC_HARD_006", "Hard",
         "The Supreme Court (Enlargement of Criminal Appellate Jurisdiction) Act 1970 extended the right of criminal appeal to the Supreme Court without certificate to cases where a High Court imposes what sentence?",
         "1970 உச்ச நீதிமன்ற (குற்றவியல் மேல்முறையீட்டு ஆதிக்க விரிவாக்க) சட்டம், எந்தத் தண்டனையை உயர் நீதிமன்றம் விதிக்கும் வழக்குகளுக்கும் சான்றிதழ் இன்றி மேல்முறையீட்டு உரிமையை விரிவாக்கியது?",
         ("Fines exceeding Rs. 50,000", "50,000 ரூபாய்க்கு மிகையான அபராதம்", "Imprisonment for life or imprisonment for a period of not less than 10 years", "ஆயுள் தண்டனை அல்லது 10 ஆண்டுகளுக்குக் குறையாத சிறைத்தண்டனை", "Simple imprisonment for 3 years", "3 ஆண்டுகள் சாதாரண சிறைத்தண்டனை", "Forfeiture of private property", "தனியார் சொத்துக்களைப் பறிமுதல் செய்தல்"),
         "B",
         "Parliament enacted the SC (Enlargement of Criminal Appellate Jurisdiction) Act 1970 under Art 134(2), extending criminal appeal rights without HC certificate to cases where HC on appeal reversed acquittal and sentenced accused to life imprisonment or 10+ years imprisonment.",
         "உறுப்பு 134(2)-ன் கீழ் நாடாளுமன்றம் 1970 சட்டத்தை இயற்றி, உயர் நீதிமன்றம் விடுதலையை மாற்றி ஆயுள் தண்டனை அல்லது 10+ ஆண்டுகள் சிறைத்தண்டனை விதிக்கும் வழக்குகளுக்கும் மேல்முறையீட்டு உரிமையை விரிவாக்கியது.",
         ("Fine amount is not the criterion.", "அபராதத் தொகை காரணியல்ல.", "Life imprisonment or 10+ years imprisonment is the exact statutory threshold under the 1970 Act.", "ஆயுள் தண்டனை அல்லது 10+ ஆண்டுகள் சிறைத்தண்டனை என்பது 1970 சட்டத்தின் துல்லியமான வரம்பாகும்.", "3 years imprisonment is not covered.", "3 ஆண்டுகள் சிறை இதில் வராது.", "Forfeiture of property is not the criterion.", "சொத்து பறிமுதல் காரணியல்ல."),
         "Confusing constitutional death sentence threshold (Art 134(1)) with statutory enlarged threshold under 1970 Act (Life or 10+ yrs imprisonment).", "அரசியலமைப்பு மரண தண்டனை வரம்பையும் (உறுப்பு 134(1)) 1970 சட்டத்தின் ஆயுள்/10+ ஆண்டு தண்டனை வரம்பையும் குழப்புதல்.", "Criminal Appeal as of Right: Art 134(1) = Death Sentence; 1970 Act = Life Imprisonment or 10+ years imprisonment.", "குற்றவியல் மேல்முறையீடு: உறுப்பு 134(1) = மரண தண்டனை; 1970 சட்டம் = ஆயுள் அல்லது 10+ ஆண்டுகள் சிறை.", "2"),

        ("POLITY_SC_HARD_007", "Hard",
         "Under Article 134A, when can a High Court determine whether to grant a Certificate of Appeal to the Supreme Court?",
         "அரசியலமைப்பு உறுப்பு 134A-ன் கீழ், உச்ச நீதிமன்ற மேல்முறையீட்டு சான்றிதழ் வழங்குவதைப் பற்றி உயர் நீதிமன்றம் எப்போது தீர்மானிக்க முடியும்?",
         ("Only if the Supreme Court issues a show-cause notice", "உச்ச நீதிமன்றம் நோட்டீஸ் அனுப்பினால் மட்டுமே", "Only after 1 year from the date of judgment", "தீர்ப்பு நாளிலிருந்து 1 ஆண்டு கழித்து மட்டுமே", "On its own motion (suo motu) OR on an oral application made by aggrieved party immediately after passing judgment", "தானாக முன்வந்து (suo motu) அல்லது தீர்ப்பு வழங்கப்பட்ட உடனே பாதிக்கப்பட்ட தரப்பு அளிக்கும் வாய்மொழி மனுவின் அடிப்படையில்", "Only if approved by the State Advocate General", "மாநில அட்வகேட் ஜெனரல் ஒப்புதல் அளித்தால் மட்டுமே"),
         "C",
         "Article 134A mandates that every High Court passing a judgment shall determine the question of granting a certificate (a) on its own motion, or (b) on an oral application by or on behalf of aggrieved party made immediately after judgment.",
         "அரசியலமைப்பு உறுப்பு 134A, உயர் நீதிமன்றம் தீர்ப்பு வழங்கிய உடனே (a) தானாக முன்வந்தோ அல்லது (b) பாதிக்கப்பட்ட தரப்பின் வாய்மொழி மனு அடிப்படையிலோ சான்றிதழ் அளிப்பதைத் தீர்மானிக்க வேண்டும் எனக் கூறுகிறது.",
         ("Show-cause notice is not required.", "நோட்டீஸ் தேவையில்லை.", "1 year delay invalidates immediate determination.", "1 ஆண்டு தாமதம் முறையல்ல.", "Suo motu OR on oral application immediately after passing judgment is the exact constitutional procedure under Art 134A.", "தானாக முன்வந்து அல்லது தீர்ப்பு வழங்கப்பட்ட உடனே வாய்மொழி மனு என்பது உறுப்பு 134A-ன் துல்லியமான நடைமுறையாகும்.", "Advocate General approval is not required.", "அட்வகேட் ஜெனரல் ஒப்புதல் தேவையில்லை."),
         "Thinking a formal written petition filed after several months is required for Art 134A certificate instead of oral application immediately after judgment.", "தீர்ப்பு வழங்கப்பட்ட உடனே வாய்மொழி மனுவிற்குப் பதிலாக பல மாதங்கள் கழித்து எழுத்துப்பூர்வ மனு தேவை என நினைத்தல்.", "Art 134A Procedure = HC determines certificate issue (1) Suo Motu OR (2) On Oral Application made IMMEDIATELY after judgment.", "உறுப்பு 134A நடைமுறை = தீர்ப்பு வழங்கப்பட்ட உடனே தானாக முன்வந்து அல்லது வாய்மொழி மனு அடிப்படையில் சான்றிதழ் தீர்மானிக்கப்படும்.", "2"),

        ("POLITY_SC_HARD_008", "Hard",
         "What is the fundamental difference between Presidential References under Article 143(1) and Article 143(2)?",
         "அரசியலமைப்பு உறுப்பு 143(1) மற்றும் உறுப்பு 143(2)-ன் கீழ் வரப்பெறும் குடியரசுத் தலைவர் குறிப்புகளுக்கு இடையேயான அடிப்படை வேறுபாடு என்ன?",
         ("Under 143(1) SC 'may' report opinion (discretionary), whereas under 143(2) regarding pre-Constitution treaties SC 'shall' report opinion (mandatory)", "143(1)-ன் கீழ் SC கருத்து தெரிவிக்கலாம் (விருப்பவுரிமை), ஆனால் 143(2)-ன் கீழ் 1950-க்கு முந்தைய உடன்படிக்கைகளில் SC கருத்து தெரிவிப்பது கட்டாயமாகும் (shall)", "Under 143(1) opinion is binding, whereas under 143(2) opinion is non-binding", "143(1)-ன் கீழ் கருத்து கட்டுப்படுத்தும், 143(2)-ன் கீழ் கட்டுப்படுத்தாது", "Article 143(1) applies to High Courts, whereas 143(2) applies to Supreme Court", "143(1) உயர் நீதிமன்றங்களுக்கும் 143(2) உச்ச நீதிமன்றத்திற்கும் பொருந்தும்", "Article 143(2) was repealed by the 44th Amendment", "உறுப்பு 143(2) 44-வது திருத்தத்தால் நீக்கப்பட்டது"),
         "D",
         "Under Art 143(1) (public importance), SC 'may' report opinion (discretionary to refuse). Under Art 143(2) (pre-Constitution treaties/disputes under Art 131 proviso), SC 'shall' report opinion (constitutionally mandatory to give opinion).",
         "உறுப்பு 143(1)-ன் கீழ் (பொது முக்கியத்துவம்) SC கருத்து தெரிவிக்கலாம் (மறுக்கவும் அதிகாரம் உண்டு). உறுப்பு 143(2)-ன் கீழ் (1950-க்கு முந்தைய உடன்படிக்கைகள்) SC கருத்து தெரிவிப்பது அரசியலமைப்பு ரீதியாகக் கட்டாயமாகும் (shall).",
         ("Under 143(1) SC 'may' report opinion; under 143(2) SC 'shall' report opinion.", "143(1)-ன் கீழ் SC கருத்து தெரிவிக்கலாம்; 143(2)-ன் கீழ் கட்டாயம் கருத்து தெரிவிக்க வேண்டும்.", "Both opinions under Art 143 are advisory and NON-BINDING.", "உறுப்பு 143-ன் கீழ் உள்ள இரு ஆலோசனைகளும் கட்டாயமற்றவை.", "Both 143(1) and 143(2) apply exclusively to Supreme Court.", "இரண்டுமே உச்ச நீதிமன்றத்திற்கு மட்டுமே பொருந்தும்.", "Art 143(2) is active and intact.", "உறுப்பு 143(2) அமலில் உள்ளது."),
         "Thinking Supreme Court can refuse to answer a reference under Article 143(2) just like it can under Article 143(1).", "உறுப்பு 143(1) போல உறுப்பு 143(2) குறிப்பிற்கும் உச்ச நீதிமன்றம் பதிலளிக்க மறுக்கலாம் என நினைத்தல்.", "Art 143(1) (Public Importance) = SC MAY give opinion (e.g. Refused in Ayodhya 1993); Art 143(2) (Pre-Constitution Treaties) = SC SHALL give opinion (Mandatory obligation).", "உறுப்பு 143(1) = கருத்து தெரிவிக்கலாம் (விருப்பவுரிமை); உறுப்பு 143(2) = கட்டாயம் தெரிவிக்க வேண்டும் (கடமை).", "2"),

        ("POLITY_SC_HARD_009", "Hard",
         "In which Presidential Reference under Article 143(1) did the Supreme Court explicitly decline to answer the question referred by the President?",
         "அரசியலமைப்பு உறுப்பு 143(1)-ன் கீழ் வரப்பெற்ற எந்தக் குடியரசுத் தலைவர் குறிப்பில் உச்ச நீதிமன்றம் தனது கருத்தைத் தெரிவிக்கத் திட்டவட்டமாக மறுத்தது?",
         ("Ayodhya Reference (Ismail Faruqui Case, 1993)", "அயோத்தி குறிப்பு (இஸ்மாயில் ஃபரூக்கி வழக்கு, 1993)", "Berubari Union Reference (1960)", "பெருபாரி யூனியன் குறிப்பு (1960)", "Sea Customs Act Reference (1963)", "கடல் சுங்கச் சட்டக் குறிப்பு (1963)", "Special Courts Bill Reference (1978)", "சிறப்பு நீதிமன்றங்கள் மசோதா குறிப்பு (1978)"),
         "A",
         "In the Ayodhya Reference (1993) under Art 143(1) ('whether a Hindu temple existed before Ram Janmabhoomi Babri Masjid structure'), the SC declined to answer, holding the reference unnecessary and favoured resolution via regular suits.",
         "1993 அயோத்தி குறிப்பில் (உறுப்பு 143(1)), உச்ச நீதிமன்றம் தனக்கு அளிக்கப்பட்ட வினாவுக்குக் கருத்து தெரிவிக்க மறுத்து, வழக்கமான உரிமையியல் வழக்குகள் மூலமே தீர்வுகாண வேண்டும் எனக் கூறியது.",
         ("Ayodhya Reference (1993) is the famous instance where SC declined to answer Art 143(1) reference.", "அயோத்தி குறிப்பு (1993) உச்ச நீதிமன்றம் உறுப்பு 143(1) வினாவுக்கு பதிலளிக்க மறுத்த புகழ்பெற்ற நிகழ்வாகும்.", "Berubari Union 1960 SC gave opinion on ceding territory.", "பெருபாரி யூனியன் 1960-ல் SC கருத்து தெரிவித்தது.", "Sea Customs Act 1963 SC gave opinion.", "கடல் சுங்கச் சட்டத்தில் SC கருத்து தெரிவித்தது.", "Special Courts Bill 1978 SC gave opinion.", "சிறப்பு நீதிமன்றங்கள் மசோதாவில் SC கருத்து தெரிவித்தது."),
         "Believing that the Supreme Court has answered every Article 143 reference made by the President.", "குடியரசுத் தலைவர் கேட்ட அனைத்து உறுப்பு 143 குறிப்புகளுக்கும் உச்ச நீதிமன்றம் பதிலளித்துள்ளது என நினைத்தல்.", "Landmark Art 143(1) Refusal = Ayodhya Reference (1993) -> SC exercised discretion under Art 143(1) 'may report' to decline answering.", "உறுப்பு 143(1) மறுப்பு வழக்கு = அயோத்தி குறிப்பு (1993).", "2"),

        ("POLITY_SC_HARD_010", "Hard",
         "What is the constitutional status of the Supreme Court's power to punish for contempt of itself under Article 129 vis-à-vis Parliamentary statutes?",
         "அரசியலமைப்பு உறுப்பு 129-ன் கீழ் உச்ச நீதிமன்றத்தின் அவமதிப்புக்குத் தண்டிக்கும் அதிகாரம் நாடாளுமன்றச் சட்டங்களுக்கு முன் எவ்வகை அந்தஸ்தைப் பெறுகிறது?",
         ("It is subject to approval by the Union Law Minister", "இது ஒன்றிய சட்ட அமைச்சரின் ஒப்புதலுக்கு உட்பட்டது", "It is an inherent constitutional power that CANNOT be abrogated or stultified even by Parliamentary legislation", "இது ஒரு இயல்பான அரசியலமைப்பு அதிகாரம்; நாடாளுமன்றச் சட்டத்தால் கூட இதைக் குறைக்கவோ ரத்து செய்யவோ முடியாது", "It can be exercised only if Parliament passes a special resolution", "நாடாளுமன்றம் சிறப்புத் தீர்மானம் நிறைவேற்றினால் மட்டுமே இதைப் பயன்படுத்த முடியும்", "It applies only to printed publications and not oral statements", "இது அச்சிடப்பட்ட வெளியீடுகளுக்கு மட்டுமே பொருந்தும், வாய்மொழி கூற்றுகளுக்கு அல்ல"),
         "B",
         "In *In re Vinay Chandra Mishra (1995)* and *SCBA v. UOI (1998)*, the SC held that the power to punish for contempt under Art 129 is a constitutional power derived directly from the Constitution and cannot be limited or taken away by any statute including the Contempt of Courts Act 1971.",
         "வினய் சந்திர மிஸ்ரா (1995) மற்றும் SCBA (1998) வழக்குகளில், உறுப்பு 129 அவமதிப்பு அதிகாரம் அரசியலமைப்பிலிருந்து நேரடியாகப் பெறப்படும் அதிகாரம் என்றும், நாடாளுமன்றச் சட்டத்தால் கூட இதைக் குறைக்க முடியாது என்றும் உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
         ("Law Minister approval is not required.", "சட்ட அமைச்சர் ஒப்புதல் தேவையில்லை.", "Inherent constitutional power under Art 129 cannot be limited by Parliamentary legislation.", "உறுப்பு 129 இயல்பான அதிகாரம் நாடாளுமன்றச் சட்டத்தால் குறைக்கப்பட முடியாது.", "Parliamentary resolution is not needed.", "நாடாளுமன்றத் தீர்மானம் தேவையில்லை.", "Applies to both oral and written statements.", "வாய்மொழி மற்றும் எழுத்து இரண்டிற்கும் பொருந்தும்."),
         "Thinking the Contempt of Courts Act 1971 can restrict or curtail the Supreme Court's constitutional contempt power under Article 129.", "1971 அவமதிப்புச் சட்டம் உச்ச நீதிமன்றத்தின் உறுப்பு 129 அரசியலமைப்பு அதிகாரத்தைக் கட்டுப்படுத்தும் என நினைத்தல்.", "Article 129 Contempt Power = Inherent Constitutional Power. Contempt of Courts Act 1971 regulates procedure, but CANNOT limit SC's constitutional power under Art 129.", "உறுப்பு 129 அவமதிப்பு அதிகாரம் = இயல்பான அரசியலமைப்பு அதிகாரம். சட்டம் நடைமுறையை மட்டுமே ஒழுங்குபடுத்தும்.", "2"),

        ("POLITY_SC_HARD_011", "Hard",
         "In Supreme Court Bar Association v. Union of India (1998), why did the Supreme Court hold that it CANNOT suspend an advocate's license to practice while exercising contempt jurisdiction under Article 129?",
         "உச்ச நீதிமன்ற வழக்கறிஞர் சங்கம் எதிர் இந்திய ஒன்றியம் (1998) வழக்கில், உறுப்பு 129 அவமதிப்பு அதிகாரத்தைப் பயன்படுத்தும் போது ஒரு வழக்கறிஞரின் வழக்கறிஞர் உரிமத்தை இடைநீக்கம் செய்ய முடியாது என உச்ச நீதிமன்றம் ஏன் தீர்ப்பளித்தது?",
         ("Because advocates are immune from contempt proceedings", "ஏனெனில் வழக்கறிஞர்களுக்கு அவமதிப்பு நடவடிக்கையிலிருந்து விலக்கு உண்டு", "Because the Advocate General must consent first", "ஏனெனில் அட்வகேட் ஜெனரல் முதலில் ஒப்புதல் அளிக்க வேண்டும்", "Because the power to punish for professional misconduct belongs exclusively to the State Bar Council and Bar Council of India under the Advocates Act 1961", "ஏனெனில் தொழிலும் சார்ந்த நடத்தைக் குறைபாட்டிற்குத் தண்டிக்கும் அதிகாரம் 1961 வழக்கறிஞர்கள் சட்டத்தின் கீழ் பார் கவுன்சிலுக்கு மட்டுமே உரியது", "Because suspension requires a 2/3rd majority vote in Parliament", "ஏனெனில் இடைநீக்கம் செய்ய நாடாளுமன்றத்தில் 2/3 பங்கு வாக்கு தேவை"),
         "C",
         "In SCBA v. UOI (1998), a 5-judge bench overruled Vinay Chandra Mishra (1995) and held that while SC can punish for contempt under Art 129, it cannot usurp the statutory disciplinary jurisdiction of the Bar Council under Advocates Act 1961 to suspend an advocate's license.",
         "1998 SCBA வழக்கில், 5 நீதிபதிகள் அமர்வு வினய் சந்திர மிஸ்ரா தீர்ப்பை மாற்றி, உறுப்பு 129 அவமதிப்பு தண்டனையாக 1961 சட்டத்தின் கீழ் பார் கவுன்சிலுக்கு உரிய வழக்கறிஞர் உரிம இடைநீக்கத் தண்டனையை SC வழங்க முடியாது எனத் தீர்ப்பளித்தது.",
         ("Advocates are NOT immune from contempt.", "வழக்கறிஞர்களுக்கு அவமதிப்பிலிருந்து விலக்கில்லை.", "Advocate General consent is for criminal contempt filing, not punishment scope.", "அட்வகேட் ஜெனரல் ஒப்புதல் மனு தாக்கல் செய்யவே.", "Professional misconduct disciplinary power belongs exclusively to Bar Councils under Advocates Act 1961.", "தொழில்முறை ஒழுங்கு நடவடிக்கை அதிகாரம் 1961 சட்டத்தின் கீழ் பார் கவுன்சிலுக்கு மட்டுமே உரியது.", "Parliament vote is not required for advocate suspension.", "நாடாளுமன்ற வாக்கு தேவையில்லை."),
         "Confusing Supreme Court's contempt power under Art 129 with Bar Council's statutory disciplinary power under Advocates Act 1961.", "உறுப்பு 129 அவமதிப்பு அதிகாரத்தையும் 1961 வழக்கறிஞர்கள் சட்டத்தின் கீழ் பார் கவுன்சில் அதிகாரத்தையும் குழப்புதல்.", "SCBA v. UOI (1998) = SC under Art 129 CANNOT suspend an Advocate's license to practice as punishment for contempt (Bar Council's exclusive statutory domain under Advocates Act 1961).", "SCBA வழக்கு (1998) = உறுப்பு 129 அவமதிப்பு தண்டனையாக வழக்கறிஞர் உரிமத்தை இடைநீக்கம் செய்ய முடியாது.", "2"),

        ("POLITY_SC_HARD_012", "Hard",
         "In Golaknath v. State of Punjab (1967), what major constitutional doctrine was introduced for the first time in Indian jurisprudence by Chief Justice K. Subba Rao?",
         "கோலக்நாத் எதிர் பஞ்சாப் மாநிலம் (1967) வழக்கில், தலைமை நீதிபதி கே. சுப்பா ராவால் இந்திய சட்டத்துறையில் முதன்முதலில் அறிமுகப்படுத்தப்பட்ட முக்கிய கோட்பாடு எது?",
         ("Basic Structure Doctrine", "அடிப்படை கட்டமைப்புக் கோட்பாடு", "Doctrine of Pith and Substance", "சாராம்சக் கோட்பாடு (Pith and Substance)", "Doctrine of Colorable Legislation", "வண்ணப் போலிச் சட்டக் கோட்பாடு", "Doctrine of Prospective Overruling", "எதிர்கால நோக்குடைய ரத்துக் கோட்பாடு (Prospective Overruling)"),
         "D",
         "In Golaknath (1967), CJI K. Subba Rao invoked the American 'Doctrine of Prospective Overruling', declaring that the ruling (that Parliament cannot amend FRs) would apply ONLY to future legislation and would not invalidate past constitutional amendments.",
         "கோலக்நாத் வழக்கில் (1967), தலைமை நீதிபதி கே. சுப்பா ராவ் அமெரிக்க 'எதிர்கால நோக்குடைய ரத்துக் கோட்பாட்டை' (Prospective Overruling) அறிமுகப்படுத்தி, தீர்ப்பு எதிர்கால சட்டங்களுக்கு மட்டுமே பொருந்தும் என்றும் கடந்தகால திருத்தங்களை செல்லாததாக்காது என்றும் கூறினார்.",
         ("Basic Structure Doctrine came later in Kesavananda Bharati (1973).", "அடிப்படை கட்டமைப்புக் கோட்பாடு கேசவாநந்த பாரதியில் (1973) வந்தது.", "Pith and Substance is legislative list interpretation doctrine.", "சாராம்சக் கோட்பாடு சட்டமன்றப் பட்டியல் பற்றியது.", "Colorable Legislation is legislative competence doctrine.", "வண்ணப் போலிச் சட்டக் கோட்பாடு சட்டமன்ற அதிகாரம் பற்றியது.", "Doctrine of Prospective Overruling was introduced for the first time in Golaknath (1967).", "எதிர்கால நோக்குடைய ரத்துக் கோட்பாடு கோலக்நாத்தில் (1967) முதன்முதலில் அறிமுகப்படுத்தப்பட்டது."),
         "Confusing Golaknath (1967 - introduced Prospective Overruling & declared FRs unamendable) with Kesavananda Bharati (1973 - introduced Basic Structure Doctrine).", "கோலக்நாத் (1967 - Prospective Overruling) மற்றும் கேசவாநந்த பாரதி (1973 - Basic Structure) ஆகியவற்றை குழப்புதல்.", "Golaknath Case (1967) = First time 'Doctrine of Prospective Overruling' invoked in India. Held Parliament has NO power to amend Fundamental Rights.", "கோலக்நாத் வழக்கு (1967) = இந்தியாவில் முதன்முதலில் 'Prospective Overruling' கோட்பாடு அறிமுகப்படுத்தப்பட்டது.", "3"),

        ("POLITY_SC_HARD_013", "Hard",
         "In Kesavananda Bharati (1973), while upholding the 24th Amendment, which specific clause of Article 31C added by the 25th Amendment Act 1971 was declared UNCONSTITUTIONAL?",
         "கேசவாநந்த பாரதி வழக்கில் (1973), 24-வது திருத்தத்தை உறுதி செய்த அதே வேளையில், 25-வது திருத்தச் சட்டம் 1971 மூலம் சேர்க்கப்பட்ட உறுப்பு 31C-ன் எந்த குறிப்பிட்ட பகுதி அரசியலமைப்பிற்கு முரணானது என அறிவிக்கப்பட்டது?",
         ("The second part of Article 31C which barred judicial review ('no law containing a declaration shall be questioned in any court')", "நீதித்துறை ஆய்வை விலக்கிய உறுப்பு 31C-ன் இரண்டாம் பகுதி ('அறிவிப்பைக் கொண்ட எந்தச் சட்டமும் நீதிமன்றத்தில் கேள்வி கேட்கப்படக் கூடாது')", "The first part giving precedence to DPSPs under Art 39(b) and (c) over Articles 14 and 19", "உறுப்பு 39(b) மற்றும் (c) நெறிமுறைகளுக்கு 14 மற்றும் 19-ஐ விட முன்னுரிமை அளித்த முதல் பகுதி", "The whole of Article 31C", "உறுப்பு 31C முழுவதும்", "The 24th Amendment in its entirety", "24-வது திருத்தம் முழுவதும்"),
         "A",
         "In Kesavananda Bharati (1973), SC upheld the 1st part of Art 31C (giving primacy to Art 39(b)&(c) DPSPs over Arts 14, 19, 31), BUT struck down the 2nd part of Art 31C which stated 'no law containing a declaration shall be called in question in any court' because it destroyed Judicial Review.",
         "கேசவாநந்த பாரதி வழக்கில் (1973), உறுப்பு 31C-ன் முதல் பகுதி செல்லுபடியாகும் எனக் கூறிய உச்ச நீதிமன்றம், நீதித்துறை ஆய்வைத் தடுத்த அதன் 2-வது பகுதியை ('நீதிமன்றத்தில் கேள்வி கேட்கக் கூடாது') அரசியலமைப்பிற்கு முரணானது என ரத்து செய்தது.",
         ("The second part of Art 31C barring judicial review was declared UNCONSTITUTIONAL.", "நீதித்துறை ஆய்வை விலக்கிய உறுப்பு 31C-ன் 2-வது பகுதி அரசியலமைப்பிற்கு முரணானது என அறிவிக்கப்பட்டது.", "First part of Art 31C was UPHELD in Kesavananda Bharati.", "உறுப்பு 31C-ன் முதல் பகுதி உறுதி செய்யப்பட்டது.", "Whole of Art 31C was not struck down.", "உறுப்பு 31C முழுவதும் ரத்து செய்யப்படவில்லை.", "24th Amendment was fully UPHELD.", "24-வது திருத்தம் முழுமையாக உறுதி செய்யப்பட்டது."),
         "Thinking the entire Article 31C was struck down in Kesavananda Bharati.", "கேசவாநந்த பாரதியில் உறுப்பு 31C முழுவதுமாக ரத்து செய்யப்பட்டது எனத் தவறாக நினைத்தல்.", "Kesavananda Bharati (1973) Art 31C Ruling = 1st part UPHELD; 2nd part (barring Judicial Review) STRUCK DOWN as it damaged Basic Structure.", "கேசவாநந்த பாரதி (1973) உறுப்பு 31C தீர்ப்பு = முதல் பகுதி உறுதி; 2-வது பகுதி (நீதித்துறை ஆய்வுத் தடை) ரத்து.", "3"),

        ("POLITY_SC_HARD_014", "Hard",
         "Which of the following features has NOT been declared by the Supreme Court as part of the Basic Structure of the Constitution?",
         "எது உச்ச நீதிமன்றத்தால் அரசியலமைப்பின் 'அடிப்படை கட்டமைப்பு' (Basic Structure) பகுதியாக அறிவிக்கப்படவில்லை?",
         ("Supremacy of the Constitution and Secularism", "அரசியலமைப்பின் மேலாதிக்கம் மற்றும் மதச்சார்பின்மை", "Unbridled and Unlimited Amending Power of Parliament under Article 368", "உறுப்பு 368-ன் கீழ் நாடாளுமன்றத்தின் கட்டுப்பாடற்ற மற்றும் வரம்பற்ற திருத்த அதிகாரம்", "Judicial Review and Independence of the Judiciary", "நீதித்துறை ஆய்வு மற்றும் நீதித்துறையின் சுதந்திரம்", "Rule of Law and Free & Fair Elections", "சட்டத்தின் ஆட்சி மற்றும் சுதந்திரமான, நேர்மையான தேர்தல்கள்"),
         "B",
         "Unbridled amending power of Parliament is NOT a basic feature. In Minerva Mills (1980), SC held that limited amending power itself is a basic feature, and Parliament cannot use Art 368 to grant itself unlimited amending power.",
         "நாடாளுமன்றத்தின் கட்டுப்பாடற்ற திருத்த அதிகாரம் அடிப்படை அம்சம் அல்ல. மினெர்வா மில்ஸ் (1980) வழக்கில், 'வரம்பிற்குட்பட்ட திருத்த அதிகாரமே' அடிப்படை அம்சம் என்றும், நாடாளுமன்றம் தனக்கு வரம்பற்ற அதிகாரத்தை வழங்க முடியாது என்றும் SC தீர்ப்பளித்தது.",
         ("Supremacy of Constitution and Secularism ARE Basic Features.", "அரசியலமைப்பு மேலாதிக்கம் மற்றும் மதச்சார்பின்மை அடிப்படை அம்சங்கள்.", "Unbridled Amending Power is NOT a basic feature (In fact, LIMITED amending power IS the basic feature).", "கட்டுப்பாடற்ற திருத்த அதிகாரம் அடிப்படை அம்சம் அல்ல (வரம்பிற்குட்பட்ட திருத்த அதிகாரமே அடிப்படை அம்சம்).", "Judicial Review and Independence of Judiciary ARE Basic Features.", "நீதித்துறை ஆய்வு மற்றும் சுதந்திரம் அடிப்படை அம்சங்கள்.", "Rule of Law and Free & Fair Elections ARE Basic Features.", "சட்டத்தின் ஆட்சி மற்றும் நேர்மையான தேர்தல் அடிப்படை அம்சங்கள்."),
         "Confusing Parliamentary amending power (which is LIMITED under Basic Structure) with actual Basic Features.", "நாடாளுமன்றத் திருத்த அதிகாரத்தைக் அடிப்படை அம்சங்களோடு குழப்புதல்.", "Basic Structure Core Principle = Parliament has LIMITED amending power under Art 368. Limited amending power ITSELF is a Basic Feature (Minerva Mills 1980).", "அடிப்படை கட்டமைப்பு கொள்கை = வரம்பிற்குட்பட்ட திருத்த அதிகாரமே ஒரு அடிப்படை அம்சமாகும் (மினெர்வா மில்ஸ் 1980).", "3"),

        ("POLITY_SC_HARD_015", "Hard",
         "In AIIMS Students Union v. AIIMS (2002), how did the Supreme Court define the legal relationship between Fundamental Rights (Part III) and Fundamental Duties (Part IVA)?",
         "AIIMS மாணவர்கள் சங்கம் எதிர் AIIMS (2002) வழக்கில், அடிப்படை உரிமைகள் (பகுதி III) மற்றும் அடிப்படை கடமைகள் (பகுதி IVA) ஆகியவற்றுக்கு இடையேயான சட்டப்பூர்வ தொடர்பை உச்ச நீதிமன்றம் எவ்வாறு வரையறுத்தது?",
         ("Fundamental Duties are superior to Fundamental Rights", "அடிப்படை கடமைகள் அடிப்படை உரிமைகளை விட மேலானவை", "Fundamental Duties are completely non-existent in constitutional interpretation", "அரசியலமைப்பு விளக்கத்தில் அடிப்படை கடமைகள் முற்றிலும் இல்லாதவை", "Fundamental Duties are equally important as Fundamental Rights and serve as a tool for interpreting constitutional statutes and basic structure", "அடிப்படை கடமைகளும் அடிப்படை உரிமைகளைப் போலவே முக்கியத்துவம் வாய்ந்தவை மற்றும் அரசியலமைப்புச் சட்டங்கள் மற்றும் அடிப்படை கட்டமைப்பை விளக்க உதவும் கருவியாகும்", "Fundamental Duties apply only to civil servants", "அடிப்படை கடமைகள் அரசு ஊழியர்களுக்கு மட்டுமே பொருந்தும்"),
         "C",
         "In AIIMS Students Union (2002), SC held that Fundamental Duties under Art 51A, though non-justiciable directly, are as important as Fundamental Rights and serve as a vital tool for constitutional interpretation and basic structure balance.",
         "2002 AIIMS வழக்கில், உறுப்பு 51A அடிப்படை கடமைகள் நேரடியாக நீதிமன்றத்தால் அமல்படுத்தப்படாவிட்டாலும், அடிப்படை உரிமைகளைப் போலவே முக்கியமானவை மற்றும் அரசியலமைப்பு விளக்கத்திற்கு உதவும் கருவியாகும் என உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
         ("Duties superior to Rights was rejected.", "கடமைகள் உரிமைகளை விட மேலானவை என்பது நிராகரிக்கப்பட்டது.", "Non-existent argument was rejected.", "இல்லாதவை என்பது நிராகரிக்கப்பட்டது.", "Fundamental Duties are equally important as FRs and act as a tool for interpreting statutes and basic structure.", "அடிப்படை கடமைகளும் அடிப்படை உரிமைகளைப் போலவே முக்கியம் மற்றும் அரசியலமைப்பு விளக்கத்திற்கு உதவும் கருவியாகும்.", "Applies to all citizens, not just civil servants.", "அனைத்துக் குடிமக்களுக்கும் பொருந்தும்."),
         "Treating Fundamental Duties as entirely useless in judicial interpretation because they are non-justiciable.", "அடிப்படை கடமைகள் நீதிமன்றத்தால் நேரடியாக அமல்படுத்தப்படாததால் நீதித்துறை விளக்கத்திற்குப் பயன்படாது என நினைத்தல்.", "Fundamental Duties (Part IVA) = Non-justiciable directly, BUT used by Courts as an interpretive tool for determining constitutional validity & Basic Structure (AIIMS Case 2002).", "அடிப்படை கடமைகள் = நேரடியாக அமல்படுத்தப்படாவிட்டாலும் அரசியலமைப்பு செல்லுபடி தன்மையை விளக்கும் கருவியாக நீதிமன்றங்களால் பயன்படுத்தப்படுகிறது.", "3"),

        ("POLITY_SC_HARD_016", "Hard",
         "Under Article 262(2) of the Constitution, how does Parliament exclude the jurisdiction of the Supreme Court over inter-state river water disputes?",
         "அரசியலமைப்பு உறுப்பு 262(2)-ன் கீழ், மாநிலங்களுக்கு இடையேயான நதிநீர் தகராறுகளில் உச்ச நீதிமன்றத்தின் அதிகார வரம்பை நாடாளுமன்றம் எவ்வாறு விலக்குகிறது?",
         ("By issuing an executive order through the Ministry of Jal Shakti", "ஜல் சக்தி அமைச்சகம் மூலம் நிர்வாக ஆணை பிறப்பிப்பதன் மூலம்", "By enacting a Parliamentary law providing that neither Supreme Court nor any other court shall exercise jurisdiction over such dispute referred to a Tribunal", "தீர்ப்பாயத்திற்கு அனுப்பப்பட்ட தகராறில் உச்ச நீதிமன்றமோ வேறு எந்த நீதிமன்றமோ அதிகாரம் செலுத்தக்கூடாது என சட்டம் இயற்றுவதன் மூலம்", "By amending Article 32 by 2/3rd majority", "உறுப்பு 32-ஐ 2/3 பங்கு பெரும்பான்மையுடன் திருத்துவதன் மூலம்", "By transferring water subject to the State List permanently", "நீர் விஷயத்தை மாநில பட்டியலுக்கு நிரந்தரமாக மாற்றுவதன் மூலம்"),
         "D",
         "Article 262(2) states that Parliament may by law provide that neither the Supreme Court nor any other court shall exercise jurisdiction in respect of any such dispute or complaint referred to an Inter-State River Water Disputes Tribunal.",
         "அரசியலமைப்பு உறுப்பு 262(2), நதிநீர் தீர்ப்பாயத்திற்கு அனுப்பப்படும் தகராறுகளில் உச்ச நீதிமன்றமோ அல்லது பிற நீதிமன்றமோ அதிகாரம் செலுத்தக்கூடாது என நாடாளுமன்றம் சட்டத்தின் மூலம் வழிவகை செய்யலாம் எனக் கூறுகிறது.",
         ("Executive order cannot exclude court jurisdiction.", "நிர்வாக ஆணை நீதிமன்ற அதிகாரத்தை விலக்க முடியாது.", "Parliamentary law enacted under Art 262(2) (Inter-State River Water Disputes Act 1956) is the exact constitutional mechanism.", "உறுப்பு 262(2)-ன் கீழ் இயற்றப்படும் நாடாளுமன்றச் சட்டமே (1956 நதிநீர் தகராறுகள் சட்டம்) துல்லியமான அரசியலமைப்பு வழிமுறையாகும்.", "Art 32 amendment is not required.", "உறுப்பு 32 திருத்தம் தேவையில்லை.", "State List transfer is irrelevant.", "மாநிலப் பட்டியல் மாற்றம் தொடர்பில்லாதது."),
         "Confusing general Original Jurisdiction under Art 131 with special Parliamentary bar under Art 262(2) regarding river water disputes.", "உறுப்பு 131 பொது மூல ஆதிக்கத்தையும் உறுப்பு 262(2) நதிநீர் தகராறுகள் சிறப்புத் தடையையும் குழப்புதல்.", "Inter-State River Water Disputes -> Art 262(2) empowers Parliament by law to bar Supreme Court & all court jurisdiction. Enacted via Inter-State Water Disputes Act 1956.", "மாநிலங்களுக்கு இடையேயான நதிநீர் தகராறுகள் -> உறுப்பு 262(2) நாடாளுமன்றச் சட்டம் மூலம் நீதிமன்ற அதிகாரத்தைத் தடுக்கிறது.", "2"),

        ("POLITY_SC_HARD_017", "Hard",
         "In the Cauvery Water Disputes Tribunal appeals, how did the Supreme Court reconcile the bar under Article 262 with its own jurisdiction?",
         "காாவிரி நதிநீர் தீர்ப்பாய மேல்முறையீட்டு வழக்குகளில், உறுப்பு 262 தடையை உச்ச நீதிமன்றம் தனது சொந்த அதிகார வரம்போடு எவ்வாறு சமரசம் செய்தது?",
         ("SC held that while original adjudication of water sharing is barred, appeals against Tribunal awards on legal/constitutional errors lie under Article 136 and 142", "நதிநீர் பங்கீடு மூல விசாரணை தடைசெய்யப்பட்டாலும், தீர்ப்பாய உத்தரவுகளின் சட்டப் பிழைகளுக்கு எதிரான மேல்முறையீடுகள் உறுப்பு 136 மற்றும் 142-ன் கீழ் செல்லும் என SC தீர்ப்பளித்தது", "SC struck down Article 262 as unconstitutional", "SC உறுப்பு 262-ஐ அரசியலமைப்பிற்கு முரணானது என ரத்து செய்தது", "SC held that water disputes belong exclusively to High Courts", "நதிநீர் தகராறுகள் உயர் நீதிமன்றங்களுக்கு மட்டுமே உரியவை என SC தீர்ப்பளித்தது", "SC declared that Parliamentary laws under Art 262 are subject to Governor's veto", "உறுப்பு 262 சட்டங்கள் ஆளுநரின் வீட்டோ அதிகாரத்திற்கு உட்பட்டவை என SC கூறியது"),
         "A",
         "In the Cauvery Water Tribunal appeals, SC clarified that Article 262 bars original suits on water disputes under Art 131, BUT does NOT oust SC's extraordinary appellate jurisdiction under Art 136 or plenary power under Art 142 to correct legal errors or enforce fundamental rights.",
         "காவிரி நதிநீர் தீர்ப்பாய மேல்முறையீட்டு வழக்கில், உறுப்பு 262 உறுப்பு 131 மூல வழக்குகளை மட்டுமே தடுக்கிறது என்றும், உறுப்பு 136 மேல்முறையீடு மற்றும் உறுப்பு 142 முழுமையான நீதி அதிகாரத்தைத் தடுக்காது என்றும் SC தெளிவுபடுத்தியது.",
         ("SC held Art 136 & 142 appeals against Tribunal awards are permissible on legal/constitutional grounds despite Art 262 bar.", "தீர்ப்பாய உத்தரவுகளுக்கு எதிரான உறுப்பு 136 & 142 மேல்முறையீடுகள் சட்ட அடிப்படையில் செல்லும் என SC தீர்ப்பளித்தது.", "SC did NOT strike down Art 262.", "SC உறுப்பு 262-ஐ ரத்து செய்யவில்லை.", "High Courts do not have exclusive water dispute jurisdiction.", "உயர் நீதிமன்றங்களுக்கு தனி அதிகாரம் இல்லை.", "Governor veto is irrelevant.", "ஆளுநர் வீட்டோ தொடர்பில்லாதது."),
         "Thinking Article 262 completely bars Supreme Court under ALL Articles including Special Leave Petition under Article 136.", "உறுப்பு 262 உறுப்பு 136 SLP உட்பட அனைத்து விதிகளின் கீழும் உச்ச நீதிமன்றத்தை முற்றிலும் தடுக்கிறது என நினைத்தல்.", "Cauvery Appeals Jurisprudence = Art 262 bars Art 131 Original Suits, BUT does NOT bar Art 136 Special Leave Appeals or Art 142 Complete Justice powers against Tribunal orders.", "காவிரி வழக்குத் தீர்ப்பு = உறுப்பு 262 உறுப்பு 131 மூல வழக்குகளை மட்டுமே தடுக்கிறது, உறுப்பு 136/142 மேல்முறையீடுகளைத் தடுக்காது.", "2"),

        ("POLITY_SC_HARD_018", "Hard",
         "In the Fourth Judges Case (2015), Article 124A inserted by the 99th Constitutional Amendment Act was declared void primarily because of what institutional defect?",
         "4-வது நீதிபதிகள் வழக்கில் (2015), 99-வது திருத்தத்தால் சேர்க்கப்பட்ட உறுப்பு 124A எந்த அமைப்பியல் குறைபாட்டின் காரணமாக செல்லாததாக்கப்பட்டது?",
         ("Inclusion of the Union Law Minister and 2 eminent persons with veto power, which compromised Judicial Independence", "ஒன்றிய சட்ட அமைச்சர் மற்றும் வீட்டோ அதிகாரம் கொண்ட 2 பிரபல நபர்களின் சேர்க்கை நீதித்துறை சுதந்திரத்தைப் பாதித்தது", "Exclusion of the Prime Minister from the appointment process", "நியமன நடைமுறையிலிருந்து பிரதமரை விலக்கியது", "Failure to get ratification from at least 10 State Assemblies", "குறைந்தபட்சம் 10 மாநில சட்டமன்றங்களின் ஒப்புதலைப் பெறத் தவறியது", "Allowing High Court Judges to be appointed without written exams", "எழுத்துத் தேர்வின்றி உயர் நீதிமன்ற நீதிபதிகளை நியமிக்க அனுமதித்தது"),
         "B",
         "In Fourth Judges Case (2015), SC struck down Art 124A (NJAC) because giving executive members (Law Minister & 2 eminent persons) veto power over judicial appointments impinged upon 'Independence of Judiciary' (Basic Structure).",
         "4-வது நீதிபதிகள் வழக்கில் (2015), NJAC-ல் சட்ட அமைச்சர் மற்றும் 2 பிரபல நபர்களுக்கு வீட்டோ அதிகாரம் வழங்கியது அடிப்படை அம்சமான 'நீதித்துறை சுதந்திரத்தைப்' பாதித்ததால் உறுப்பு 124A ரத்து செய்யப்பட்டது.",
         ("Inclusion of Law Minister and 2 eminent persons with veto power compromised Judicial Independence.", "சட்ட அமைச்சர் மற்றும் 2 நபர்களுக்கு வீட்டோ அதிகாரம் வழங்கியது நீதித்துறை சுதந்திரத்தைப் பாதித்தது.", "Exclusion of PM was not the defect.", "பிரதமர் விலக்கம் குறைபாடல்ல.", "State ratification WAS obtained (16 states ratified), so procedural defect argument failed.", "மாநில ஒப்புதல் பெறப்பட்டது (16 மாநிலங்கள்).", "Written exams was not an issue.", "எழுத்துத் தேர்வு பிரச்சனையில்லை."),
         "Thinking NJAC was struck down due to procedural lack of State ratification (procedural defect) rather than substantive Basic Structure violation (Judicial Independence).", "NJAC மாநில ஒப்புதல் பெறாததால் ரத்து செய்யப்பட்டது எனத் தவறாக நினைத்தல்.", "Fourth Judges Case (2015) Ground = Inclusion of Executive (Law Minister + 2 Eminent Persons with Veto) in NJAC (Art 124A) violated Basic Structure ('Independence of Judiciary').", "4-வது நீதிபதிகள் வழக்கு (2015) காரணம் = NJAC-ல் நிர்வாகத்தின் பங்கேற்பு 'நீதித்துறை சுதந்திரம்' என்ற அடிப்படை அம்சத்தை மீறியது.", "3"),

        ("POLITY_SC_HARD_019", "Hard",
         "What is the 'Restatement of Values of Judicial Life' adopted by the Supreme Court of India in 1999?",
         "1999-ல் இந்திய உச்ச நீதிமன்றத்தால் ஏற்றுக்கொள்ளப்பட்ட 'நீதிமன்ற வாழ்க்கையின் விழுமியங்களின் மறுஅறிக்கை' (Restatement of Values of Judicial Life) என்றால் என்ன?",
         ("A Parliamentary code of conduct for removing judges", "நீதிபதிகளை நீக்குவதற்கான நாடாளுமன்ற நடத்தை விதிகள்", "A set of 16 ethical principles adopted for self-regulation of judicial conduct and maintaining judicial integrity", "நீதிபதிகளின் சுயகட்டுப்பாடு மற்றும் நேர்மையைப் பேண ஏற்றுக்கொள்ளப்பட்ட 16 அறநெறிக் கோட்பாடுகள்", "A statutory scheme for increasing judges' pensions", "நீதிபதிகளின் ஓய்வூதியத்தை உயர்த்தும் சட்டப்பூர்வ திட்டம்", "A set of rules for fast-tracking PIL cases", "PIL வழக்குகளை விரைவுபடுத்தும் விதிகளின் தொகுப்பு"),
         "C",
         "Formulated by Justice J.S. Verma Committee and adopted in 1999, the 'Restatement of Values of Judicial Life' comprises 16 ethical principles serving as a code of conduct for self-regulation by SC and HC judges.",
         "நீதிபதி ஜே.எஸ். வர்மா குழுவால் உருவாக்கப்பட்டு 1999-ல் ஏற்றுக்கொள்ளப்பட்ட 'நீதிமன்ற வாழ்க்கையின் விழுமியங்களின் மறுஅறிக்கை' என்பது நீதிபதிகளின் சுயகட்டுப்பாட்டிற்கான 16 அறநெறிக் கோட்பாடுகளாகும்.",
         ("Parliamentary code is incorrect.", "நாடாளுமன்ற விதிகள் என்பது தவறு.", "16 ethical principles adopted by Judiciary for self-regulation is the exact definition.", "நீதித்துறையால் சுயகட்டுப்பாட்டிற்காக ஏற்றுக்கொள்ளப்பட்ட 16 அறநெறிக் கோட்பாடுகள் என்பதே சரியாகும்.", "Pension scheme is incorrect.", "ஓய்வூதியத் திட்டம் தவறு.", "PIL fast-tracking is incorrect.", "PIL விரைவுபடுத்தல் தவறு."),
         "Confusing internal judicial self-regulation code (Restatement of Values 1999) with external Parliamentary legislation.", "உள்நீதித்துறை சுயகட்டுப்பாட்டு விதியை நாடாளுமன்ற சட்டத்தோடு குழப்புதல்.", "Restatement of Values of Judicial Life (1999) = 16 Ethical Principles adopted by Full Court of Supreme Court for self-regulation of judicial conduct.", "நீதிமன்ற வாழ்க்கையின் விழுமியங்களின் மறுஅறிக்கை (1999) = நீதிபதிகளின் சுயகட்டுப்பாட்டிற்கான 16 அறநெறிக் கோட்பாடுகள்.", "3"),

        ("POLITY_SC_HARD_020", "Hard",
         "Article 124(7) prohibits a retired Supreme Court Judge from pleading or acting in any court or authority in India, BUT does NOT prohibit which of the following activities?",
         "அரசியலமைப்பு உறுப்பு 124(7) ஓய்வு பெற்ற உச்ச நீதிமன்ற நீதிபதி நீதிமன்றங்களில் வழக்காடுவதைத் தடை செய்கிறது, ஆனால் எந்த நடவடிக்கையைத் தடை செய்யவில்லை?",
         ("Accepting post-retirement appointments such as Governor, NHRC Chairperson, or Law Commission Chairman", "ஆளுநர், தேசிய மனித உரிமைகள் ஆணையத் தலைவர் அல்லது சட்ட ஆணையத் தலைவர் போன்ற ஓய்வுக்குப் பிந்தைய பதவிகளை ஏற்பது", "Pleading as an advocate before the Delhi High Court", "டெல்லி உயர் நீதிமன்றத்தில் வழக்கறிஞராக வாதிடுவது", "Acting as an attorney before the Income Tax Appellate Tribunal", "வருமான வரி மேல்முறையீட்டு தீர்ப்பாயத்தில் வழக்கறிஞராகப் பணியாற்றுவது", "Pleading before any Subordinate District Court", "மாவட்டக் கீழமை நீதிமன்றத்தில் வாதிடுவது"),
         "D",
         "Article 124(7) bars pleading or acting in any COURT or AUTHORITY. However, it does NOT constitutionally bar taking up post-retirement executive or statutory appointments (e.g. NHRC Chairman, Law Commission, Governor, Rajya Sabha nomination).",
         "அரசியலமைப்பு உறுப்பு 124(7) நீதிமன்றங்கள் அல்லது அதிகார அமைப்புகளில் வழக்கறிஞராகப் பணியாற்றுவதை மட்டுமே தடை செய்கிறது. ஓய்வுக்குப் பிந்தைய நிர்வாக அல்லது சட்டப்பூர்வ பதவிகளை (ஆளுநர், NHRC தலைவர்) ஏற்பதைத் தடை செய்யவில்லை.",
         ("Accepting post-retirement executive/statutory appointments IS NOT barred by Art 124(7) text.", "ஓய்வுக்குப் பிந்தைய பதவிகளை ஏற்பது உறுப்பு 124(7) உரையால் தடை செய்யப்படவில்லை.", "Pleading in Delhi HC IS strictly barred.", "டெல்லி HC-ல் வாதிடுவது தடை செய்யப்பட்டுள்ளது.", "Acting in Income Tax Tribunal IS strictly barred.", "வருமான வரித் தீர்ப்பாயத்தில் பணியாற்றுவது தடை செய்யப்பட்டுள்ளது.", "Pleading in District Court IS strictly barred.", "மாவட்ட நீதிமன்றத்தில் வாதிடுவது தடை செய்யப்பட்டுள்ளது."),
         "Thinking Article 124(7) prohibits retired Supreme Court judges from holding statutory/executive positions like NHRC Chairman or Governor.", "உறுப்பு 124(7) ஓய்வு பெற்ற நீதிபதிகள் NHRC தலைவர் அல்லது ஆளுநர் போன்ற பதவிகளை வகிப்பதைத் தடை செய்கிறது எனத் தவறாக நினைத்தல்.", "Art 124(7) Bar = Bars PLEADING or ACTING as an Advocate in any Court/Authority. DOES NOT bar post-retirement tribunal/commission chairmanships or political appointments like Governor.", "உறுப்பு 124(7) தடை = வழக்கறிஞராகப் பணியாற்றுவதற்கு மட்டுமே தடை. ஆணையத் தலைவர்/ஆளுநர் பதவிகளுக்குத் தடையல்ல.", "1"),

        ("POLITY_SC_HARD_021", "Hard",
         "In the Second Judges Case (1993), what specific constitutional convention regarding the Chief Justice of India was converted into a mandatory binding rule?",
         "2-வது நீதிபதிகள் வழக்கில் (1993), இந்தியத் தலைமை நீதிபதி தொடர்பான எந்த குறிப்பிட்ட அரசியலமைப்பு மரபு கட்டாயக் கட்டுப்படுத்தும் விதியாக மாற்றப்பட்டது?",
         ("The senior-most judge of the Supreme Court MUST be appointed as the Chief Justice of India", "உச்ச நீதிமன்றத்தின் மூத்த நீதிபதியே இந்தியத் தலைமை நீதிபதியாகக் கட்டாயம் நியமிக்கப்பட வேண்டும்", "The Chief Justice of India must be appointed by the Speaker of Lok Sabha", "தலைமை நீதிபதியை மக்களவை சபாநாயகர் நியமிக்க வேண்டும்", "The Chief Justice of India must be a former High Court Chief Justice for 10 years", "தலைமை நீதிபதி 10 ஆண்டுகள் உயர் நீதிமன்ற தலைமை நீதிபதியாக இருந்திருக்க வேண்டும்", "The Chief Justice of India must resign upon reaching 60 years of age", "தலைமை நீதிபதி 60 வயதை அடைந்தவுடன் ராஜினாமா செய்ய வேண்டும்"),
         "A",
         "In the Second Judges Case (1993), the SC ruled that the appointment to the office of CJI shall be of the SENIOR-MOST judge of the Supreme Court considered fit to hold the office, removing executive discretion completely.",
         "2-வது நீதிபதிகள் வழக்கில் (1993), உச்ச நீதிமன்றத்தின் மூத்த நீதிபதியே (Senior-most Judge) இந்தியத் தலைமை நீதிபதியாக நியமிக்கப்பட வேண்டும் என்ற மரபு கட்டாய விதியாக மாற்றப்பட்டது.",
         ("Senior-most judge appointment as CJI was made mandatory in 2nd Judges Case 1993.", "மூத்த நீதிபதியை CJI ஆக நியமிப்பது 2-வது வழக்கின் மூலம் கட்டாயமாக்கப்பட்டது.", "Speaker appointment is incorrect.", "சபாநாயகர் நியமனம் தவறு.", "10 years HC CJ is not required.", "10 ஆண்டுகள் HC CJ தேவையில்லை.", "Retirement age remains 65, not 60.", "ஓய்வு வயது 65."),
         "Thinking executive retains discretion to select CJI from among top 3 SC judges.", "முதல் 3 நீதிபதிகளில் ஒருவரை தேர்வு செய்ய நிர்வாகத்திற்கு விருப்பவுரிமை உண்டு என நினைத்தல்.", "CJI Appointment Rule (post-1993 2nd Judges Case) = Senior-most SC Judge MUST be appointed as CJI. Executive discretion is ZERO.", "CJI நியமன விதி (1993 2-வது வழக்கு) = உச்ச நீதிமன்றத்தின் மூத்த நீதிபதியே கட்டாயம் CJI ஆக நியமிக்கப்பட வேண்டும்.", "1"),

        ("POLITY_SC_HARD_022", "Hard",
         "In Indira Nehru Gandhi (1975) and Minerva Mills (1980), 'Rule of Law' under Article 14 was declared to be an essential component of which constitutional principle?",
         "இந்திரா நேரு காந்தி (1975) மற்றும் மினெர்வா மில்ஸ் (1980) வழக்குகளில், உறுப்பு 14-ன் கீழ் உள்ள 'சட்டத்தின் ஆட்சி' (Rule of Law) எந்த அரசியலமைப்புக் கோட்பாட்டின் அத்தியாவசியக் கூறாக அறிவிக்கப்பட்டது?",
         ("Directive Principles of State Policy", "அரசு வழிகாட்டு நெறிமுறைகள்", "Basic Structure of the Constitution", "அரசியலமைப்பின் அடிப்படை கட்டமைப்பு (Basic Structure)", "Parliamentary Sovereignty", "நாடாளுமன்ற இறையாண்மை", "Federal Division of Powers", "கூட்டாட்சி அதிகாரப் பகிர்வு"),
         "B",
         "In Indira Gandhi (1975) and Minerva Mills (1980), the Supreme Court explicitly held that the 'Rule of Law' embodied under Article 14 is an inviolable part of the Basic Structure of the Constitution.",
         "இந்திரா காந்தி (1975) மற்றும் மினெர்வா மில்ஸ் (1980) வழக்குகளில், உறுப்பு 14-ல் உள்ள 'சட்டத்தின் ஆட்சி' அரசியலமைப்பின் அடிப்படை கட்டமைப்பின் மீற முடியாத பகுதி என உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
         ("DPSP is Part IV, whereas Rule of Law under Art 14 is a Basic Feature.", "DPSP பகுதி IV, சட்டத்தின் ஆட்சி அடிப்படை அம்சமாகும்.", "Rule of Law under Article 14 was declared a core element of the Basic Structure of the Constitution.", "உறுப்பு 14-ன் கீழ் சட்டத்தின் ஆட்சி அடிப்படை கட்டமைப்பின் முதன்மை கூறாக அறிவிக்கப்பட்டது.", "Parliamentary Sovereignty is limited by Basic Structure.", "நாடாளுமன்ற இறையாண்மை அடிப்படை அமைப்பால் வரம்பிற்குட்பட்டது.", "Federal Division is a separate feature.", "கூட்டாட்சி பகிர்வு தனி அம்சமாகும்."),
         "Thinking Rule of Law is merely an ordinary Fundamental Right under Article 14 and not part of Basic Structure.", "சட்டத்தின் ஆட்சி என்பது உறுப்பு 14-ன் கீழ் ஒரு சாதாரண அடிப்படை உரிமை மட்டுமே, அடிப்படை கட்டமைப்பு அல்ல என நினைத்தல்.", "Rule of Law (Art 14) = Declared part of Basic Structure in Indira Gandhi (1975) & Minerva Mills (1980). Cannot be destroyed by constitutional amendment.", "சட்டத்தின் ஆட்சி (உறுப்பு 14) = இந்திரா காந்தி மற்றும் மினெர்வா மில்ஸ் வழக்குகளில் அடிப்படை கட்டமைப்பின் பகுதியாக அறிவிக்கப்பட்டது.", "2"),

        ("POLITY_SC_HARD_023", "Hard",
         "Which condition is constitutionally MANDATORY for the Supreme Court to issue a Writ of Quo Warranto against an incumbent holding a public office?",
         "ஒரு பொதுப் பதவியை வகிப்பவருக்கு எதிராக உச்ச நீதிமன்றம் Quo Warranto பேராணையைப் பிறப்பிக்க எந்த நிபந்தனை அரசியலமைப்பு ரீதியாகக் கட்டாயமாகும்?",
         ("The public office must be of a permanent nature created by statute or Constitution", "பொதுப் பதவி ஒரு சட்டத்தாலோ அல்லது அரசியலமைப்பாலோ உருவாக்கப்பட்ட நிரந்தரத் தன்மை கொண்டதாக இருக்க வேண்டும்", "The petitioner must have suffered direct monetary loss", "மனுதாரர் நேரடியாக நிதி இழப்பைச் சந்தித்திருக்க வேண்டும்", "The Union Law Ministry must approve the petition", "ஒன்றிய சட்ட அமைச்சகம் மனுவிற்கு ஒப்புதல் அளிக்க வேண்டும்", "The office holder must be a Member of Parliament", "பதவி வகிப்பவர் நாடாளுமன்ற உறுப்பினராக இருக்க வேண்டும்"),
         "C",
         "Quo Warranto lies only if: (1) Public office is created by statute or Constitution, (2) Office is of a public nature and permanent, (3) Incumbent is holding office without legal qualification. It does NOT lie for private or contractual offices.",
         "Quo Warranto பொருந்தக்கூடிய நிபந்தனைகள்: (1) பொதுப் பதவி சட்டத்தால்/அரசியலமைப்பால் உருவாக்கப்பட்டிருக்க வேண்டும், (2) பதவி நிரந்தரத் தன்மை கொண்டதாக இருக்க வேண்டும், (3) வகிப்பவர் சட்டப்பூர்வ தகுதியின்றி இருக்க வேண்டும்.",
         ("Public office created by statute/Constitution of permanent nature is the mandatory condition.", "சட்டத்தால்/அரசியலமைப்பால் உருவாக்கப்பட்ட நிரந்தர பொதுப் பதவி என்பதே கட்டாய நிபந்தனையாகும்.", "Direct monetary loss is NOT required (Locus standi is relaxed).", "நேரடி நிதி இழப்பு தேவையில்லை.", "Law Ministry approval is irrelevant.", "சட்ட அமைச்சக ஒப்புதல் தேவையில்லை.", "Holder need not be an MP (applies to any statutory post).", "நாடாளுமன்ற உறுப்பினராக இருக்க வேண்டியதில்லை."),
         "Thinking Quo Warranto can be issued to challenge appointments in private companies or temporary contractual posts.", "தனியார் நிறுவனங்கள் அல்லது தற்காலிக ஒப்பந்தப் பதவிகளுக்கு எதிராக Quo Warranto பிறப்பிக்கலாம் என நினைத்தல்.", "Quo Warranto Conditions -> (1) Statutory/Constitutional Public Office, (2) Permanent Nature, (3) Illegal Usurpation/Lack of Qualification. NOT applicable to private bodies.", "Quo Warranto நிபந்தனைகள் -> (1) சட்டப்பூர்வ/அரசியலமைப்பு பொதுப் பதவி, (2) நிரந்தரத் தன்மை, (3) சட்டவிரோத ஆக்கிரமிப்பு.", "1"),

        ("POLITY_SC_HARD_024", "Hard",
         "Why can the Constitutional Writ of Mandamus NOT be issued by the Supreme Court to enforce departmental guidelines or administrative circulars?",
         "துறை சார்ந்த வழிகாட்டுதல்கள் அல்லது நிர்வாகச் சுற்றறிக்கைகளை அமல்படுத்த உச்ச நீதிமன்றத்தால் செயல்உறுத்தும் பேராணையை (Mandamus) ஏன் பிறப்பிக்க முடியாது?",
         ("Because administrative circulars lack statutory force of law", "ஏனெனில் நிர்வாகச் சுற்றறிக்கைகளுக்குச் சட்டப்பூர்வ சட்டம் என்ற அதிகாரம் இல்லை என்பதால்", "Because Mandamus is issued only against judges", "ஏனெனில் Mandamus நீதிபதிகளுக்கு எதிராக மட்டுமே பிறப்பிக்கப்படும் என்பதால்", "Because circulars are framed by the President", "ஏனெனில் சுற்றறிக்கைகள் குடியரசுத் தலைவரால் உருவாக்கப்படுகின்றன என்பதால்", "Because Mandamus was abolished by the 44th Amendment", "ஏனெனில் Mandamus 44-வது திருத்தத்தால் நீக்கப்பட்டது என்பதால்"),
         "D",
         "Mandamus is issued ONLY to enforce a mandatory STATUTORY duty or fundamental right. Executive instructions, departmental circulars, or administrative guidelines that lack statutory force do not create an enforceable legal duty for Mandamus.",
         "Mandamus ஒரு கட்டாயச் சட்டப்பூர்வக் கடமையை (Statutory Duty) அமல்படுத்த மட்டுமே பிறப்பிக்கப்படும். சட்டப்பூர்வ அதிகாரம் இல்லாத நிர்வாகச் சுற்றறிக்கைகள் Mandamus மூலம் அமல்படுத்தப்பட முடியாது.",
         ("Lack of statutory force in circulars prevents Mandamus enforcement.", "சுற்றறிக்கைகளுக்கு சட்டப்பூர்வ அதிகாரம் இல்லாததால் Mandamus அமல்படுத்தப்பட முடியாது.", "Mandamus is issued to public officers, not just judges.", "Mandamus பொது அதிகாரிகளுக்கு பிறப்பிக்கப்படும்.", "Circulars are framed by departments, not President.", "சுற்றறிக்கைகள் துறைகளால் உருவாக்கப்படுகின்றன.", "Mandamus was never abolished.", "Mandamus நீக்கப்படவில்லை."),
         "Thinking Mandamus can be used to enforce any internal office memo or departmental guideline.", "எந்தவொரு உள்அலுவலகக் குறிப்பையும் சுற்றறிக்கையையும் Mandamus மூலம் அமல்படுத்தலாம் என நினைத்தல்.", "Mandamus Requirement = Must enforce a STATUTORY Duty or Fundamental Right. Non-statutory administrative instructions CANNOT be enforced by Mandamus.", "Mandamus நிபந்தனை = ஒரு சட்டப்பூர்வக் கடமை (Statutory Duty) அல்லது அடிப்படை உரிமையை அமல்படுத்த மட்டுமே பிறப்பிக்கப்படும்.", "1"),

        ("POLITY_SC_HARD_025", "Hard",
         "On which of the following combined grounds can a Writ of Certiorari be issued by the Supreme Court to quash a decision of a judicial or quasi-judicial body?",
         "எந்தக் கூட்டுக் காரணங்களின் அடிப்படையில் ஒரு நீதித்துறை அல்லது பகுதி-நீதித்துறை அமைப்பின் முடிவை ரத்து செய்ய உச்ச நீதிமன்றத்தால் Certiorari பேராணை பிறப்பிக்கப்படலாம்?",
         ("Excess of jurisdiction, Lack of jurisdiction, Violation of Natural Justice, or Error of Law apparent on the face of the record", "அதிகார வரம்பு மீறல், அதிகார வரம்பின்மை, இயற்கை நீதி மீறல் அல்லது பதிவேட்டின் முகப்பில் தெளிவாகத் தெரியும் சட்டப் பிழை", "Political disagreement with government policy", "அரசு கொள்கையுடனான அரசியல் கருத்து வேறுபாடு", "Simple error of fact that requires re-appreciation of evidence", "ஆதாரங்களை மீண்டும் பரிசீலிக்கத் தேவையான சாதாரண உண்மைப் பிழை", "Non-payment of court fee by the tribunal", "தீர்ப்பாயத்தால் நீதிமன்றக் கட்டணம் செலுத்தப்படாமை"),
         "A",
         "Certiorari is issued on four established grounds: (1) Want/Lack of jurisdiction, (2) Excess of jurisdiction, (3) Violation of principles of Natural Justice, and (4) Error of Law apparent on the face of the record.",
         "Certiorari 4 காரணங்களுக்காகப் பிறப்பிக்கப்படுகிறது: (1) அதிகார வரம்பின்மை, (2) அதிகார வரம்பு மீறல், (3) இயற்கை நீதி கோட்பாடுகள் மீறல், (4) பதிவேட்டின் முகப்பில் தெளிவாகத் தெரியும் சட்டப் பிழை.",
         ("Excess/Lack of jurisdiction, Natural Justice violation, and Error of Law apparent on record are the exact 4 grounds for Certiorari.", "அதிகார வரம்பு மீறல், அதிகார வரம்பின்மை, இயற்கை நீதி மீறல், சட்டப் பிழை ஆகிய 4 காரணங்களே Certiorari-க்குரியவையாகும்.", "Political disagreement is non-justiciable.", "அரசியல் கருத்து வேறுபாடு இதில் வராது.", "Simple error of fact is NOT a ground for Certiorari (SC does not re-appreciate evidence as appellate court of fact in Certiorari).", "சாதாரண உண்மைப் பிழை Certiorari-க்கு காரணமல்ல.", "Court fee non-payment is irrelevant.", "நீதிமன்றக் கட்டணம் தொடர்பில்லாதது."),
         "Confusing Error of Law apparent on the face of the record (ground for Certiorari) with simple error of fact (NOT a ground for Certiorari).", "தெளிவான சட்டப் பிழைக்கும் (Certiorari காரணம்) சாதாரண உண்மைப் பிழைக்கும் (Certiorari காரணம் அல்ல) வித்தியாசம் தெரியாமல் குழம்புவது.", "Certiorari Grounds = (1) Lack of Jurisdiction, (2) Excess of Jurisdiction, (3) Natural Justice Violation, (4) Error of Law apparent on face of record. Note: Simple error of fact is NOT a ground.", "Certiorari காரணங்கள் = (1) அதிகார வரம்பின்மை, (2) எல்லை மீறல், (3) இயற்கை நீதி மீறல், (4) தெளிவான சட்டப் பிழை.", "2"),

        ("POLITY_SC_HARD_026", "Hard",
         "Under Article 13(1) of the Constitution, how does the 'Doctrine of Eclipse' operate on pre-constitutional laws that are inconsistent with Fundamental Rights?",
         "அரசியலமைப்பு உறுப்பு 13(1)-ன் கீழ், அடிப்படை உரிமைகளுக்கு முரணான 1950-க்கு முந்தைய சட்டங்கள் மீது 'மறைப்புக் கோட்பாடு' (Doctrine of Eclipse) எவ்வாறு செயல்படுகிறது?",
         ("The pre-constitutional law becomes void ab initio and is permanently erased from statute book", "1950-க்கு முந்தைய சட்டம் தொடக்கத்திலிருந்தே செல்லாததாகி முழுமையாக அழிக்கப்படுகிறது", "The pre-constitutional law does not die completely, but remains dormant/shadowed under the eclipse of Fundamental Rights, and becomes active again if FR is amended", "1950-க்கு முந்தைய சட்டம் முற்றிலும் அழிந்துவிடாது; அடிப்படை உரிமையின் நிழலில் மறைந்து கிடக்கும்; அடிப்படை உரிமை திருத்தப்பட்டால் மீண்டும் உயிர்பெறும்", "The pre-constitutional law automatically overrides Fundamental Rights", "1950-க்கு முந்தைய சட்டம் தானாகவே அடிப்படை உரிமைகளை மேலோங்கும்", "The law applies only to non-citizens permanently", "அச்சட்டம் வெளிநாட்டினருக்கு மட்டுமே நிரந்தரமாகப் பொருந்தும்"),
         "B",
         "In Bhikaji Narain v. State of MP (1955), SC held that under Art 13(1), pre-constitutional laws inconsistent with FRs are not void ab initio, but shadowed/eclipsed by FRs. If the FR is amended to remove inconsistency, the shadow is lifted and the law becomes enforceable again.",
         "பிகாஜி நரேன் வழக்கில் (1955), உறுப்பு 13(1)-ன் கீழ் 1950-க்கு முந்தைய சட்டங்கள் தொடக்கத்திலிருந்தே செல்லாதவை அல்ல, அடிப்படை உரிமையால் மறைக்கப்படுகின்றன. முரண்பாடு நீக்கப்பட்டால் மறைப்பு நீங்கி சட்டம் மீண்டும் உயிர்பெறும் என SC தீர்ப்பளித்தது.",
         ("Void ab initio applies to post-constitutional laws under Art 13(2), NOT pre-constitutional laws under Art 13(1).", "தொடக்கம் முதலே செல்லாதது என்பது உறுப்பு 13(2) 1950-க்கு பிந்தைய சட்டங்களுக்குப் பொருந்தும்.", "Dormant/shadowed status lifting upon FR amendment is the exact working of Doctrine of Eclipse (Bhikaji Narain Case 1955).", "மறைந்து கிடந்து அடிப்படை உரிமை திருத்தப்பட்டவுடன் மீண்டும் உயிர்பெறுவது மறைப்புக் கோட்பாடாகும் (பிகாஜி நரேன் வழக்கு 1955).", "Pre-constitutional laws do NOT override FRs.", "முந்தைய சட்டங்கள் FR-ஐ மேலோங்க முடியாது.", "Non-citizens statement is incomplete explanation.", "வெளிநாட்டினர் கூற்று முழுமையற்ற விளக்கம்."),
         "Applying Doctrine of Eclipse to post-constitutional laws (which are void ab initio under Art 13(2)) instead of pre-constitutional laws under Art 13(1).", "மறைப்புக் கோட்பாட்டை 1950-க்கு பிந்தைய சட்டங்களுக்குப் பயன்படுத்துதல் (அவை தொடக்கம் முதலே செல்லாதவை).", "Doctrine of Eclipse (Bhikaji Narain 1955) = Applies primarily to Pre-Constitutional Laws (Art 13(1)). Law is shadowed, not dead. Becomes active if constitutional shadow removed.", "மறைப்புக் கோட்பாடு (பிகாஜி நரேன் 1955) = 1950-க்கு முந்தைய சட்டங்களுக்குப் பொருந்தும் (உறுப்பு 13(1)). சட்டம் மறைந்து கிடக்கும், இறக்காது.", "2"),

        ("POLITY_SC_HARD_027", "Hard",
         "How does the 'Doctrine of Severability' under Article 13 protect a statute containing both valid and invalid provisions?",
         "அரசியலமைப்பு உறுப்பு 13-ன் கீழ் உள்ள 'பிரித்தறியும் கோட்பாடு' (Doctrine of Severability) செல்லுபடியாகும் மற்றும் செல்லாத பகுதிகளைக் கொண்ட ஒரு சட்டத்தை எவ்வாறு பாதுகாக்கிறது?",
         ("The entire statute is automatically declared unconstitutional if one word is invalid", "ஒரு சொல் செல்லாவிட்டாலும் சட்டம் முழுவதும் அரசியலமைப்பிற்கு முரணானதாக அறிவிக்கப்படும்", "If the invalid portion can be separated from the valid portion, ONLY the invalid portion is struck down, leaving the valid portion intact", "செல்லாத பகுதியை செல்லுபடியாகும் பகுதியிலிருந்து பிரிக்க முடியும் என்றால், செல்லாத பகுதி மட்டுமே ரத்து செய்யப்படும், செல்லுபடியாகும் பகுதி நீடிக்கும்", "The Supreme Court rewrites the invalid portion itself", "உச்ச நீதிமன்றமே செல்லாத பகுதியை மீண்டும் திருத்தி எழுதும்", "The statute is referred to a referendum", "சட்டம் மக்கள் வாக்கெடுப்பிற்கு அனுப்பப்படும்"),
         "C",
         "In R.M.D. Chamarbaugwalla v. UOI (1957), SC laid down rules for Doctrine of Severability under Art 13: if valid and invalid provisions are severable, only the invalid part is struck down; if inseparable, whole act falls.",
         "ஆர்.எம்.டி. சாமர்பாகவாலா வழக்கில் (1957), உறுப்பு 13-ன் கீழ் பிரித்தறியும் கோட்பாட்டு விதிகளை SC வகுத்தது: செல்லாத பகுதியை பிரிக்க முடிந்தால் அதுமட்டுமே ரத்து செய்யப்படும்; பிரிக்க முடியாவிட்டால் சட்டம் முழுவதும் ரத்தாகும்.",
         ("Entire statute declaration is done ONLY if valid and invalid parts are inextricably mixed.", "பிரிக்க முடியாதவாறு கலந்திருந்தால் மட்டுமே சட்டம் முழுவதும் ரத்தாகும்.", "Striking down ONLY the invalid portion when severable is the exact Doctrine of Severability (RMD Chamarbaugwalla Case 1957).", "செல்லாத பகுதி பிரிக்கக்கூடியதாக இருந்தால் அதை மட்டுமே ரத்து செய்வது பிரித்தறியும் கோட்பாடாகும் (சாமர்பாகவாலா வழக்கு 1957).", "SC does not rewrite legislation.", "SC சட்டத்தை திருத்தி எழுதுவதில்லை.", "Referendum is not a judicial procedure.", "மக்கள் வாக்கெடுப்பு நீதிமுறை அல்ல."),
         "Thinking that any unconstitutional clause in an Act automatically destroys the entire enactment.", "ஒரு சட்டத்தில் ஒரு பிரிவு செல்லாது என்றால் சட்டம் முழுவதுமே தானாகவே அழிந்துவிடும் என நினைத்தல்.", "Doctrine of Severability (Art 13) = 'Inconsistent to the extent of such inconsistency'. Valid part saved if severable from invalid part (RMD Chamarbaugwalla 1957).", "பிரித்தறியும் கோட்பாடு (உறுப்பு 13) = முரண்படும் எல்லை வரை மட்டுமே செல்லாது. பிரிக்க முடிந்தால் செல்லுபடியாகும் பகுதி பாதுகாக்கப்படும்.", "2"),

        ("POLITY_SC_HARD_028", "Hard",
         "What is the practical legal effect of the 'Doctrine of Prospective Overruling' first applied by the Supreme Court in Golaknath (1967)?",
         "கோலக்நாத் (1967) வழக்கில் உச்ச நீதிமன்றத்தால் முதன்முதலில் பயன்படுத்தப்பட்ட 'எதிர்கால நோக்குடைய ரத்துக் கோட்பாட்டின்' (Prospective Overruling) நடைமுறை சட்ட விளைவு என்ன?",
         ("All past actions taken under the old interpretation are invalidated retrospectively", "பழைய விளக்கத்தின் கீழ் எடுக்கப்பட்ட அனைத்து கடந்தகால நடவடிக்கைகளும் பின்னோக்கி செல்லாததாக்கப்படும்", "The new judicial interpretation applies ONLY to future transactions and cases, leaving past actions and validated amendments undisturbed", "புதிய நீதித்துறை விளக்கம் எதிர்கால வழக்குகளுக்கு மட்டுமே பொருந்தும்; கடந்தகால நடவடிக்கைகள் மற்றும் திருத்தங்கள் பாதிக்கப்படாது", "The Supreme Court judgment comes into effect only after Parliamentary ratification", "உச்ச நீதிமன்ற தீர்ப்பு நாடாளுமன்ற ஒப்புதலுக்குப் பிறகே அமலுக்கு வரும்", "The Constitution ceases to operate for 6 months", "அரசியலமைப்பு 6 மாதங்களுக்குச் செயல்படாது"),
         "D",
         "Under Prospective Overruling (Golaknath 1967), the new ruling applies ONLY to future cases. Actions taken and constitutional amendments passed under the old interpretation remain valid and undisturbed.",
         "எதிர்கால நோக்குடைய ரத்துக் கோட்பாட்டின் படி (கோலக்நாத் 1967), புதிய தீர்ப்பு எதிர்கால வழக்குகளுக்கு மட்டுமே பொருந்தும். பழைய விளக்கத்தின் கீழ் எடுக்கப்பட்ட கடந்தகால நடவடிக்கைகள் செல்லுபடியாகும்.",
         ("Retrospective invalidation is the traditional doctrine, NOT prospective overruling.", "பின்னோக்கி செல்லாததாக்குவது பாரம்பரிய கோட்பாடு, Prospective Overruling அல்ல.", "New interpretation applying ONLY to future cases leaving past actions undisturbed is the exact definition of Prospective Overruling.", "புதிய விளக்கம் எதிர்கால வழக்குகளுக்கு மட்டுமே பொருந்தும், கடந்தகால நடவடிக்கைகள் பாதிக்கப்படாது என்பதே Prospective Overruling பொருளாகும்.", "Parliamentary ratification is not required.", "நாடாளுமன்ற ஒப்புதல் தேவையில்லை.", "Constitution operation is not suspended.", "அரசியலமைப்பு செயல்படுவது நிறுத்தி வைக்கப்படுவதில்லை."),
         "Confusing Prospective Overruling (applies ONLY to future cases) with Retrospective Overruling (invalidates past actions).", "Prospective Overruling (எதிர்காலத்திற்கு மட்டுமே) மற்றும் Retrospective Overruling (கடந்தகாலத்தையும் பாதிப்பது) ஆகியவற்றை குழப்புதல்.", "Prospective Overruling (Golaknath 1967) = New legal interpretation applies strictly FUTURE-ONWARDS. Past transactions/amendments under old rule remain valid.", "எதிர்கால நோக்குடைய ரத்துக் கோட்பாடு (கோலக்நாத் 1967) = புதிய தீர்ப்பு எதிர்காலத்திற்கு மட்டுமே பொருந்தும்; கடந்தகால நடவடிக்கைகள் செல்லும்.", "2"),

        ("POLITY_SC_HARD_029", "Hard",
         "Through judicial interpretation of Article 21, in which landmark 9-judge Constitution Bench case was the 'Right to Privacy' unanimously declared a Fundamental Right in 2017?",
         "உறுப்பு 21-ன் நீதித்துறை விளக்கம் மூலம், எந்த வரலாற்றுச் சிறப்புமிக்க 9 நீதிபதிகள் கொண்ட அரசியல் சாசன அமர்வு வழக்கில் 'தனிநபர் தனியுரிமை' (Right to Privacy) ஒரு அடிப்படை உரிமையாக 2017-ல் ஒருமனதாக அறிவிக்கப்பட்டது?",
         ("Justice K.S. Puttaswamy v. Union of India (2017)", "நீதிபதி கே.எஸ். புட்டசுவாமி எதிர் இந்திய ஒன்றியம் (2017)", "Maneka Gandhi v. Union of India (1978)", "மேனகா காந்தி எதிர் இந்திய ஒன்றியம் (1978)", "Olga Tellis v. Bombay Municipal Corporation (1985)", "ஒல்கா டெல்லிஸ் எதிர் பம்பாய் மாநகராட்சி (1985)", "Unni Krishnan v. State of Andhra Pradesh (1993)", "உன்னிகிருஷ்ணன் எதிர் ஆந்திரப் பிரதேச மாநிலம் (1993)"),
         "A",
         "In Justice K.S. Puttaswamy v. UOI (2017), a unanimous 9-judge bench overruled M.P. Sharma (1954) & Kharak Singh (1962), declaring Right to Privacy an intrinsic part of Right to Life and Personal Liberty under Art 21.",
         "நீதிபதி கே.எஸ். புட்டசுவாமி வழக்கில் (2017), 9 நீதிபதிகள் அமர்வு ஒருமனதாக எம்.பி. சர்மா (1954) மற்றும் கரக் சிங் (1962) தீர்ப்புகளை மாற்றி, தனியுரிமை உறுப்பு 21-ன் கீழ் அடிப்படை உரிமை எனத் தீர்ப்பளித்தது.",
         ("Justice K.S. Puttaswamy (2017) is the landmark 9-judge bench ruling declaring Right to Privacy a Fundamental Right.", "கே.எஸ். புட்டசுவாமி (2017) என்பது தனியுரிமையை அடிப்படை உரிமையாக அறிவித்த வரலாற்றுச் சிறப்புமிக்க 9 நீதிபதிகள் அமர்வு வழக்காகும்.", "Maneka Gandhi (1978) established due process under Art 21.", "மேனகா காந்தி உறுப்பு 21 நியாயமான நடைமுறை பற்றியது.", "Olga Tellis (1985) declared Right to Livelihood under Art 21.", "ஒல்கா டெல்லிஸ் வாழ்வாதார உரிமை பற்றியது.", "Unni Krishnan (1993) declared Right to Education under Art 21.", "உன்னிகிருஷ்ணன் கல்வி உரிமை பற்றியது."),
         "Confusing earlier Article 21 expansion cases (Olga Tellis, Unni Krishnan) with K.S. Puttaswamy 2017 (Right to Privacy).", "உறுப்பு 21 விரிவாக்க வழக்குகளான ஒல்கா டெல்லிஸ், உன்னிகிருஷ்ணன் ஆகியவற்றை புட்டசுவாமி (2017) வழக்கோடு குழப்புதல்.", "Landmark Privacy Ruling = Justice K.S. Puttaswamy v. UOI (2017) [Unanimous 9-Judge Bench -> Right to Privacy is a Fundamental Right under Art 21].", "தனியுரிமை வரலாற்றுத் தீர்ப்பு = நீதிபதி கே.எஸ். புட்டசுவாமி வழக்கு (2017) [9 நீதிபதிகள் அமர்வு ஒருமனதான தீர்ப்பு].", "3"),

        ("POLITY_SC_HARD_030", "Hard",
         "In Vishaka v. State of Rajasthan (1997), how did the Supreme Court exercise its constitutional powers under Article 32/141 in the absence of enacted legislation?",
         "விசாகா எதிர் ராஜஸ்தான் மாநிலம் (1997) வழக்கில், நாடாளுமன்றச் சட்டம் இல்லாத நிலையில் உச்ச நீதிமன்றம் தனது உறுப்பு 32/141 அதிகாரங்களை எவ்வாறு பயன்படுத்தியது?",
         ("It refused to hear the petition citing lack of legislation", "சட்டம் இல்லை எனக் கூறி மனுவை விசாரிக்க மறுத்தது", "It laid down legally binding guidelines against sexual harassment of women at workplace to operate as law until Parliament enacted legislation", "நாடாளுமன்றம் சட்டம் இயற்றும் வரை சட்டமாகச் செயல்படும் வகையில் பணியிடத்தில் பெண்களுக்கு எதிரான பாலியல் துன்புறுத்தலுக்கு எதிரான கட்டாய வழிகாட்டுதல்களை வகுத்தது", "It referred the case to the International Court of Justice", "வழக்கை சர்வதேச நீதிமன்றத்திற்கு அனுப்பியது", "It ordered the immediate dissolution of the Rajasthan Assembly", "ராஜஸ்தான் சட்டமன்றத்தை உடனடியாகக் கலைக்க உத்தரவிட்டது"),
         "B",
         "In Vishaka (1997), SC invoked Art 32 & Art 141 read with CEDAW International Convention to frame comprehensive guidelines against workplace sexual harassment, which operated as binding law until POSH Act 2013 was enacted.",
         "விசாகா வழக்கில் (1997), SC உறுப்பு 32 & 141-ஐப் பயன்படுத்தி, சர்வதேச மாநாட்டின் அடிப்படையில் 2013 POSH சட்டம் வரும் வரை சட்டமாகக் கட்டுப்படுத்தும் விசாகா வழிகாட்டுதல்களை வகுத்தது.",
         ("SC did NOT refuse to hear the petition.", "மனுவை விசாரிக்க SC மறுக்கவில்லை.", "Framing binding guidelines to fill legislative vacuum until Parliament enacts law is classic judicial activism in Vishaka case (1997).", "நாடாளுமன்றம் சட்டம் இயற்றும் வரை சட்டமாகக் கட்டுப்படுத்தும் வழிகாட்டுதல்களை வகுத்தது விசாகா வழக்கின் சாதனையாகும்.", "ICJ reference is invalid.", "சர்வதேச நீதிமன்றத்திற்கு அனுப்பப்படவில்லை.", "Assembly dissolution is irrelevant.", "சட்டமன்றக் கலைப்பு தொடர்பில்லாதது."),
         "Thinking Supreme Court cannot lay down binding guidelines when Parliament has not enacted a law.", "நாடாளுமன்றம் சட்டம் இயற்றாத போது உச்ச நீதிமன்றம் கட்டாய வழிகாட்டுதல்களை வகுக்க முடியாது என நினைத்தல்.", "Vishaka Guidelines (1997) = Classic example of Judicial Law-making/Activism under Art 32 & 141 to fill legislative void until POSH Act 2013.", "விசாகா வழிகாட்டுதல்கள் (1997) = சட்டம் இல்லாத நிலையில் உறுப்பு 32 & 141-ன் கீழ் கட்டாய வழிகாட்டுதல்களை வகுத்த நீதித்துறை செயலாக்கம்.", "3"),

        ("POLITY_SC_HARD_031", "Hard",
         "In State of Uttaranchal v. Balwant Singh Chaufal (2010), what comprehensive directions did the Supreme Court issue to curb the menace of frivolous PILs?",
         "உத்தராஞ்சல் மாநிலம் எதிர் பல்வந்த் சிங் சௌபால் (2010) வழக்கில், போலியான PIL மனுக்களைத் தடுக்க உச்ச நீதிமன்றம் என்ன விரிவான வழிகாட்டுதல்களை வெளியிட்டது?",
         ("It completely abolished Public Interest Litigation in India", "இந்தியாவில் பொது நல வழக்குகளை முற்றிலுமாக ரத்து செய்தது", "It mandated that every PIL petitioner must pay Rs. 10 Lakhs upfront", "ஒவ்வொரு PIL மனுதாரரும் ரூ. 10 லட்சம் முன் பணம் செலுத்த வேண்டும் எனக் கட்டாயமாக்கியது", "It issued an 8-point guideline mandating High Courts to verify credentials of petitioners, check genuine public interest, and impose exemplary costs on frivolous petitions", "மனுதாரர்களின் தகுதியைச் சரிபார்க்கவும், உண்மையான பொது நலனைச் சரிபார்க்கவும், போலியான மனுக்களுக்கு அபராதம் விதிக்கவும் 8 அம்ச வழிகாட்டுதல்களை வெளியிட்டது", "It transferred all PIL cases to the Law Ministry", "அனைத்து PIL வழக்குகளையும் சட்ட அமைச்சகத்திற்கு மாற்றியது"),
         "C",
         "In Balwant Singh Chaufal (2010), SC framed 8-point guidelines to preserve PIL purity: verifying petitioner credentials, ensuring genuine public interest, prioritizing urgent matters, and penalizing personal/political motivated PILs with exemplary costs.",
         "பல்வந்த் சிங் சௌபால் வழக்கில் (2010), PIL தூய்மையைப் பாதுகாக்க 8 அம்ச வழிகாட்டுதல்களை SC வகுத்தது: மனுதாரர் தகுதியைச் சரிபார்த்தல், தனிநபர்/அரசியல் நோக்கமுள்ள மனுக்களுக்குக் கடுமையான அபராதம் விதித்தல்.",
         ("PIL was NOT abolished.", "PIL ரத்து செய்யப்படவில்லை.", "Upfront 10 Lakhs payment is incorrect.", "ரூ. 10 லட்சம் முன் பணம் தவறு.", "8-point guidelines to verify credentials and impose exemplary costs on frivolous/motivated petitions was laid down in Balwant Singh (2010).", "மனுதாரர்களின் தகுதியைச் சரிபார்க்கவும், போலியான மனுக்களுக்கு அபராதம் விதிக்கவும் 8 அம்ச வழிகாட்டுதல்கள் வெளியிடப்பட்டன.", "Transfer to Law Ministry is invalid.", "சட்ட அமைச்சகத்திற்கு மாற்றுவது தவறானது."),
         "Thinking PIL cannot be penalized or checked by courts even if filed for private malice or political vendetta.", "தனிநபர் பகை அல்லது அரசியல் நோக்கத்திற்காக தாக்கல் गरப்படும் PIL மனுக்களை நீதிமன்றங்களால் தண்டிக்க முடியாது என நினைத்தல்.", "Balwant Singh Chaufal (2010) = 8-Point SC Guidelines to curb abuse of PIL. Courts will check credentials and impose exemplary costs on busybodies.", "பல்வந்த் சிங் சௌபால் (2010) = PIL துஷ்பிரயோகத்தைத் தடுக்க 8 அம்ச வழிகாட்டுதல்கள்.", "3"),

        ("POLITY_SC_HARD_032", "Hard",
         "Under Article 141 binding precedent rules, if a 3-judge Bench of the Supreme Court disagrees with a ruling of an earlier 3-judge Bench, what is the mandatory judicial procedure to be followed?",
         "உறுப்பு 141 முன்மாதிரி சட்ட விதிகளின் கீழ், 3 நீதிபதிகள் கொண்ட உச்ச நீதிமன்ற அமர்வு முந்தைய 3 நீதிபதிகள் அமர்வின் தீர்ப்போடு வேறுபட்டால், பின்பற்றப்பட வேண்டிய கட்டாய நடைமுறை என்ன?",
         ("The later 3-judge Bench can simply overrule the earlier 3-judge Bench on its own", "பிந்தைய 3 நீதிபதிகள் அமர்வு முந்தைய அமர்வின் தீர்ப்பைத் தானே ரத்து செய்துவிடலாம்", "The later Bench MUST refer the matter to the Chief Justice of India for constituting a LARGER Bench (e.g. 5-judge Bench)", "பிந்தைய அமர்வு அக் கோப்பை பெரிய அமர்வு (எ.கா. 5 நீதிபதிகள் அமர்வு) அமைக்க இந்தியத் தலைமை நீதிபதிக்கு கட்டாயம் அனுப்ப வேண்டும்", "The earlier ruling automatically stands affirmed", "முந்தைய தீர்ப்பு தானாகவே உறுதி செய்யப்படும்", "The dispute must be sent to Parliament for arbitration", "தகராறு நாடாளுமன்ற நடுவர் மன்றத்திற்கு அனுப்பப்பட வேண்டும்"),
         "D",
         "In *Central Board of Dawoodi Bohra Community (2005)*, SC affirmed that a Bench of equal strength CANNOT overrule a co-ordinate Bench. If it disagrees, it MUST refer the question to CJI to constitute a larger Bench.",
         "தாவூதி போஹ்ரா சமுதாய வழக்கில் (2005), சம எண்ணிக்கையுள்ள அமர்வு மற்றொரு அமர்வின் தீர்ப்பை ரத்து செய்ய முடியாது என்றும், வேறுபட்டால் பெரிய அமர்வு அமைக்க CJI-க்கு பரிந்துரைக்க வேண்டும் என்றும் SC உறுதி செய்தது.",
         ("Co-ordinate Bench CANNOT overrule another Bench of equal strength.", "சம எண்ணிக்கையுள்ள அமர்வு மற்றொரு அமர்வை ரத்து செய்ய முடியாது.", "Referring the matter to CJI for constituting a LARGER Bench is the mandatory precedent rule under Art 141.", "பெரிய அமர்வு அமைக்க CJI-க்கு பரிந்துரைப்பதே உறுப்பு 141-ன் கீழ் கட்டாய நடைமுறையாகும்.", "Earlier ruling does not automatically stand without reference.", "தானாக உறுதி செய்யப்படாது.", "Parliament arbitration is irrelevant.", "நாடாளுமன்ற நடுவர் தொடர்பில்லாதது."),
         "Thinking a 3-judge bench of Supreme Court can overrule an earlier 3-judge bench decision.", "உச்ச நீதிமன்ற 3 நீதிபதிகள் அமர்வு முந்தைய 3 நீதிபதிகள் அமர்வின் தீர்ப்பை தானே ரத்து செய்யலாம் என நினைத்தல்.", "Rule of Precedent (Art 141) = Bench of equal strength CANNOT overrule co-ordinate Bench. Must refer to CJI for Larger Bench (Dawoodi Bohra Case 2005).", "முன்மாதிரி சட்ட விதி (உறுப்பு 141) = சம அமர்வு மற்றொரு சம அமர்வை ரத்து செய்ய முடியாது; பெரிய அமர்வுக்கு அனுப்ப வேண்டும்.", "3"),

        ("POLITY_SC_HARD_033", "Hard",
         "In Supreme Court Bar Association v. Union of India (1998), what limitation did the Supreme Court recognize regarding its own plenary powers under Article 142?",
         "உச்ச நீதிமன்ற வழக்கறிஞர் சங்கம் வழக்கில் (1998), உறுப்பு 142-ன் கீழ் உள்ள தனது இயல்பான அதிகாரங்கள் குறித்து உச்ச நீதிமன்றம் எந்த வரம்பை அங்கீகரித்தது?",
         ("Article 142 powers are absolute and can override explicit constitutional prohibitions", "உறுப்பு 142 அதிகாரங்கள் வரம்பற்றவை, அரசியலமைப்புத் தடைகளையும் மேலோங்கும்", "Article 142 powers are supplementary and CANNOT be used to supplant express statutory provisions or constitutional mandates", "உறுப்பு 142 அதிகாரங்கள் துணைக் கூறுகளே; வெளிப்படையான சட்ட விதிகளையோ அரசியலமைப்பு கட்டளைகளையோ மாற்றி அமைக்க அவற்றைப் பயன்படுத்த முடியாது", "Article 142 can be exercised only with prior Law Cabinet approval", "உறுப்பு 142-ஐ சட்ட அமைச்சரவை ஒப்புதலுடன் மட்டுமே பயன்படுத்த முடியும்", "Article 142 applies only to administrative staff matters", "உறுப்பு 142 நிர்வாக ஊழியர்கள் விவகாரங்களுக்கு மட்டுமே பொருந்தும்"),
         "A",
         "In SCBA v. UOI (1998), SC held that Art 142 'complete justice' power is supplementary in nature. It cannot be used to ignore or supplant express statutory provisions or constitutional prohibitions.",
         "1998 SCBA வழக்கில், உறுப்பு 142 'முழுமையான நீதி' அதிகாரம் ஒரு துணை அதிகாரமே தவிர, வெளிப்படையான சட்ட விதிகளையோ அரசியலமைப்புத் தடைகளையோ புறக்கணிக்கவோ மாற்றி அமைக்கவோ பயன்படாது என SC தீர்ப்பளித்தது.",
         ("Absolute power argument was expressly REJECTED in SCBA 1998.", "வரம்பற்ற அதிகாரம் என்பது 1998 SCBA வழக்கில் நிராகரிக்கப்பட்டது.", "Article 142 is supplementary and CANNOT supplant express statutory provisions or constitutional mandates.", "உறுப்பு 142 துணைக் கூறே தவிர வெளிப்படையான சட்ட விதிகளையோ அரசியலமைப்பு கட்டளைகளையோ மாற்ற முடியாது.", "Cabinet approval is not required.", "அமைச்சரவை ஒப்புதல் தேவையில்லை.", "Not restricted to staff matters.", "ஊழியர் விவகாரங்களுக்கு மட்டுமே என்பது தவறு."),
         "Believing Article 142 gives unlimited power to Supreme Court to ignore any statute or constitutional provision.", "உறுப்பு 142 எந்தவொரு சட்டத்தையும் அரசியலமைப்பு விதியையும் புறக்கணிக்க உச்ச நீதிமன்றத்திற்கு வரம்பற்ற அதிகாரம் அளிக்கிறது என நினைத்தல்.", "Article 142 Limitation (SCBA Case 1998) = Art 142 is a built-in constitutional power to do complete justice, BUT cannot override express statutory provisions or constitutional prohibitions.", "உறுப்பு 142 வரம்பு (SCBA வழக்கு 1998) = முழுமையான நீதி அதிகாரமாக இருந்தாலும், வெளிப்படையான சட்ட விதிகளையும் அரசியலமைப்புத் தடைகளையும் மேலோங்க முடியாது.", "1"),

        ("POLITY_SC_HARD_034", "Hard",
         "Under Article 124(4) and the Judges Inquiry Act 1968, what happens after the 3-member inquiry committee finds a Supreme Court Judge GUILTY of proved misbehaviour or incapacity?",
         "அரசியலமைப்பு உறுப்பு 124(4) மற்றும் 1968 சட்டத்தின் கீழ், 3 உறுப்பினர்கள் கொண்ட விசாரணைக் குழு நீதிபதி குற்றவாளி எனக் கண்டறிந்தால் அடுத்து என்ன நடக்கும்?",
         ("The President immediately issues a dismissal order without Parliamentary vote", "குடியரசுத் தலைவர் நாடாளுமன்ற வாக்கெடுப்பின்றி உடனடியாக பணிநீக்க ஆணை பிறப்பிப்பார்", "The House of Parliament where motion is pending considers the report and votes on the address for removal by Special Majority", "தீர்மானம் நிலுவையிலுள்ள நாடாளுமன்ற அவை அறிக்கையைப் பரிசீலித்து சிறப்பு பெரும்பான்மையுடன் நீக்கத் தீர்மானத்தின் மீது வாக்களிக்கும்", "The judge is automatically sent to prison for 5 years", "நீதிபதி தானாகவே 5 ஆண்டுகள் சிறைக்கு அனுப்பப்படுவார்", "The Chief Justice of India suspends the judge permanently", "இந்தியத் தலைமை நீதிபதி நீதிபதியை நிரந்தரமாக இடைநீக்கம் செய்வார்"),
         "B",
         "Under Section 6(2) of Judges Inquiry Act 1968 & Art 124(4), if the committee finds the judge guilty, the motion together with the report is taken up for consideration by the House and voted upon by Special Majority.",
         "1968 சட்டப் பிரிவு 6(2) & உறுப்பு 124(4)-ன் கீழ், குழு குற்றவாளி என அறிக்கை அளித்தால், அந்த அறிக்கை அவையின் பரிசீலனைக்கு எடுத்துக்கொள்ளப்பட்டு சிறப்பு பெரும்பான்மையுடன் வாக்களிக்கப்படும்.",
         ("President cannot order dismissal without Parliamentary Special Majority address.", "நாடாளுமன்ற சிறப்பு பெரும்பான்மை தீர்மானம் இன்றி குடியரசுத் தலைவர் பணிநீக்கம் செய்ய முடியாது.", "House considers the report and votes on the address by Special Majority in EACH House.", "அவை அறிக்கையைப் பரிசீலித்து ஒவ்வொரு அவையிலும் சிறப்பு பெரும்பான்மையுடன் வாக்களிக்கும்.", "Judges Inquiry Act removal procedure is constitutional removal, not criminal imprisonment.", "இது அரசியலமைப்பு நீக்க நடைமுறையே தவிர சிறைத்தண்டனை அல்ல.", "CJI cannot permanently suspend an SC Judge.", "CJI நிரந்தரமாக இடைநீக்கம் செய்ய முடியாது."),
         "Thinking that the inquiry committee report automatically removes the judge without Parliamentary voting.", "விசாரணைக் குழு அறிக்கை நாடாளுமன்ற வாக்களிப்பின்றி தானாகவே நீதிபதியை நீக்கிவிடும் என நினைத்தல்.", "Removal Sequence: Signature (100 LS / 50 RS) -> Speaker Admits -> 3-Member Judicial Committee -> Guilt Report -> Special Majority Vote in BOTH Houses -> Presidential Order.", "நீக்க நடைமுறை: கையொப்பம் -> சபாநாயகர் ஏற்பு -> 3 நபர் குழு -> குற்ற அறிக்கை -> இரு அவைகளிலும் சிறப்பு பெரும்பான்மை வாக்கு -> குடியரசுத் தலைவர் ஆணை.", "2"),

        ("POLITY_SC_HARD_035", "Hard",
         "Who was the first Supreme Court judge against whom a removal motion was admitted and voted upon in the Lok Sabha in May 1993?",
         "மே 1993-ல் மக்களவையில் நீக்கத் தீர்மானம் ஏற்கப்பட்டு வாக்களிப்பிற்கு உட்படுத்தப்பட்ட முதல் உச்ச நீதிமன்ற நீதிபதி யார்?",
         ("Justice Soumitra Sen", "நீதிபதி சௌமித்ரா சென்", "Justice P.D. Dinakaran", "நீதிபதி பி.டி. தினகரன்", "Justice V. Ramaswami", "நீதிபதி வி. ராமசுவாமி", "Justice Dipak Misra", "நீதிபதி தீபக் மிஸ்ரா"),
         "C",
         "Justice V. Ramaswami (1993) was the first Supreme Court judge against whom removal proceedings were initiated and voted upon in Lok Sabha (the motion failed due to Congress abstention).",
         "நீதிபதி வி. ராமசுவாமி (1993) மக்களவையில் நீக்கத் தீர்மானம் கொண்டுவரப்பட்டு வாக்களிக்கப்பட்ட முதல் உச்ச நீதிமன்ற நீதிபதியாவார் (காங்கிரஸ் விலகலால் தீர்மானம் தோல்வியடைந்தது).",
         ("Justice Soumitra Sen was a Calcutta HIGH COURT judge (2011), not SC judge.", "நீதிபதி சௌமித்ரா சென் கல்கத்தா உயர் நீதிமன்ற நீதிபதி (2011).", "Justice P.D. Dinakaran was Sikkim HC Chief Justice (2011), resigned before vote.", "நீதிபதி பி.டி. தினகரன் சிக்கிம் HC தலைமை நீதிபதி.", "Justice V. Ramaswami was the 1st SUPREME COURT judge facing removal motion in Lok Sabha in 1993.", "நீதிபதி வி. ராமசுவாமி 1993-ல் மக்களவையில் நீக்கத் தீர்மானத்தைச் சந்தித்த முதல் உச்ச நீதிமன்ற நீதிபதியாவார்.", "Justice Dipak Misra was CJI in 2018 (motion rejected by RS Chairman).", "நீதிபதி தீபக் மிஸ்ரா 2018-ல் RS தலைவரால் நிராகரிக்கப்பட்டவர்."),
         "Confusing Justice V. Ramaswami (First SC Judge facing removal vote in 1993) with Justice Soumitra Sen (Calcutta HC Judge facing RS vote in 2011).", "நீதிபதி வி. ராமசுவாமியையும் (1993 முதல் SC நீதிபதி) நீதிபதி சௌமித்ரா சென்னையும் (2011 HC நீதிபதி) குழப்புதல்.", "First SC Judge Impeachment Motion = Justice V. Ramaswami (1993). Inquiry committee found him guilty, but motion failed in Lok Sabha due to lack of 2/3rd voting majority.", "முதல் SC நீதிபதி நீக்கத் தீர்மானம் = நீதிபதி வி. ராமசுவாமி (1993). குழு குற்றவாளி என்றாலும் மக்களவையில் 2/3 பங்கு வாக்கு பெறாமல் தோல்வியடைந்தது.", "3"),

        ("POLITY_SC_HARD_036", "Hard",
         "Why did the removal motion against Justice V. Ramaswami fail in the Lok Sabha in May 1993, despite the 3-member inquiry committee finding him guilty of misbehaviour?",
         "3 உறுப்பினர்கள் கொண்ட விசாரணைக் குழு தவறான நடத்தைக்காகக் குற்றவாளி என அறிவித்த போதிலும், மே 1993-ல் நீதிபதி வி. ராமசுவாமிக்கு எதிரான நீக்கத் தீர்மானம் மக்களவையில் ஏன் தோல்வியடைந்தது?",
         ("Because the Supreme Court issued a stay order on the voting", "உச்ச நீதிமன்றம் வாக்கெடுப்பிற்கு இடைக்காலத் தடை விதித்ததால்", "Because the President vetoed the resolution", "குடியரசுத் தலைவர் தீர்மானத்தை வீட்டோ செய்ததால்", "Because the Speaker cancelled the motion at the last minute", "சபாநாயகர் கடைசி நிமிடத்தில் தீர்மானத்தை ரத்து செய்ததால்", "Because the ruling Congress party abstained from voting, failing to secure the mandatory 2/3rd majority of members present and voting", "ஆளும் காங்கிரஸ் கட்சி வாக்களிப்பில் பங்கேற்காமல் விலகியதால், வந்து வாக்களிப்போரின் கட்டாய 2/3 பங்கு பெரும்பான்மை கிடைக்காமல் போனதால்"),
         "D",
         "In May 1993, the motion against Justice V. Ramaswami received 108 votes in favour and 0 against, BUT 205 Congress members abstained from voting. Thus, it failed to secure the mandatory 2/3rd majority of members present and voting under Art 124(4).",
         "மே 1993-ல், தீர்மானத்திற்கு ஆதரவாக 108 வாக்குகளும் எதிராக 0 வாக்குகளும் பதிவாகின, ஆனால் 205 காங்கிரஸ் உறுப்பினர்கள் வாக்களிக்காமல் விலகியதால், உறுப்பு 124(4)-ன் கீழ் தேவையான 2/3 பங்கு பெரும்பான்மை கிடைக்காமல் தீர்மானம் விழுந்தது.",
         ("Supreme Court cannot stay Parliamentary voting on removal address.", "நாடாளுமன்ற வாக்கெடுப்பிற்கு உச்ச நீதிமன்றம் தடை விதிக்க முடியாது.", "President cannot veto before address is passed and presented.", "நிறைவேற்றப்படும் முன் குடியரசுத் தலைவர் வீட்டோ செய்ய முடியாது.", "Speaker did not cancel the motion.", "சபாநாயகர் ரத்து செய்யவில்லை.", "Abstention by 205 Congress members led to failure of securing 2/3rd present and voting majority under Art 124(4).", "205 காங்கிரஸ் உறுப்பினர்கள் விலகியதால் 2/3 பங்கு பெரும்பான்மை கிடைக்காமல் தீர்மானம் தோல்வியடைந்தது."),
         "Thinking that no judge has ever faced a voting motion in Parliament or that the motion failed due to court intervention.", "நாடாளுமன்றத்தில் எந்த நீதிபதிக்கும் வாக்கெடுப்பு நடக்கவில்லை என்றோ நீதிமன்றத் தலையீட்டால் தோல்வியடைந்தது என்றோ நினைத்தல்.", "Justice V. Ramaswami Impeachment (1993) -> Failed because 205 Congress MPs abstained, so 2/3rd majority of present and voting was not achieved. Note: No judge has been successfully removed by Parliament till date.", "வி. ராமசுவாமி நீக்கத் தீர்மானம் (1993) -> 205 எம்.பி-க்கள் விலகியதால் 2/3 பங்கு பெரும்பான்மை கிடைக்காமல் தோல்வியடைந்தது. குறிப்பு: இதுவரை எந்த நீதிபதியும் நாடாளுமன்றத்தால் நீக்கப்படவில்லை.", "4"),

        ("POLITY_SC_HARD_037", "Hard",
         "While attending the sittings of the Supreme Court under Article 127, what jurisdiction, powers, and privileges does an Ad Hoc Judge exercise?",
         "அரசியலமைப்பு உறுப்பு 127-ன் கீழ் உச்ச நீதிமன்ற அமர்வுகளில் பங்கேற்கும் போது, ஒரு Ad Hoc நீதிபதி எவ்வகை ஆதிக்கம், அதிகாரங்கள் மற்றும் சலுகைகளை அனுபவிக்கிறார்?",
         ("He has ALL the jurisdiction, powers, and privileges of a regular Judge of the Supreme Court", "அவர் ஒரு வழக்கமான உச்ச நீதிமன்ற நீதிபதியின் அனைத்து ஆதிக்கம், அதிகாரங்கள் மற்றும் சலுகைகளையும் அனுபவிக்கிறார்", "He can vote only on administrative decisions, not judicial judgments", "அவர் நிர்வாக முடிவுகளில் மட்டுமே வாக்களிக்கலாம், நீதித்துறை தீர்ப்புகளில் அல்ல", "He receives only half the powers of an SC Judge", "அவர் SC நீதிபதியின் பாதி அதிகாரங்களை மட்டுமே பெறுகிறார்", "He can sit only on single-judge benches", "அவர் தனி நீதிபதி அமர்வில் மட்டுமே அமர முடியும்"),
         "A",
         "Article 127(2) specifies that it shall be the duty of the judge so designated to attend sittings of the Supreme Court, and while so attending, he 'shall have all the jurisdiction, powers and privileges, and shall discharge the duties, of a Judge of the Supreme Court'.",
         "அரசியலமைப்பு உறுப்பு 127(2), Ad Hoc நீதிபதியாக நியமிக்கப்படுபவர் உச்ச நீதிமன்றத்தில் பங்கேற்கும் காலத்தில் 'உச்ச நீதிமன்ற நீதிபதியின் அனைத்து ஆதிக்கம், அதிகாரங்கள் மற்றும் சலுகைகளைக் கொண்டிருப்பார்' எனக் கூறுகிறது.",
         ("Ad Hoc judge has ALL jurisdiction, powers and privileges of a regular SC Judge under Art 127(2).", "Ad Hoc நீதிபதி உறுப்பு 127(2)-ன் கீழ் உச்ச நீதிமன்ற நீதிபதியின் அனைத்து அதிகாரங்களையும் சலுகைகளையும் பெறுகிறார்.", "He hears judicial cases with full powers.", "அவர் முழு அதிகாரத்துடன் வழக்குகளை விசாரிக்கிறார்.", "Half powers is incorrect.", "பாதி அதிகாரம் தவறு.", "Bench size is determined by CJI, no single-judge restriction in Art 127.", "தனி நீதிபதி வரம்பு இல்லை."),
         "Thinking Ad Hoc Judges have limited or inferior judicial powers compared to regular Supreme Court judges.", "Ad Hoc நீதிபதிகளுக்கு வழக்கமான நீதிபதிகளை விட குறைவான அல்லது வரம்பிற்குட்பட்ட அதிகாரங்களே உண்டு என நினைத்தல்.", "Ad Hoc Judge (Art 127) Powers = Full & Equal Jurisdiction, Powers and Privileges of a regular Supreme Court Judge while attending sittings.", "Ad Hoc நீதிபதி அதிகாரங்கள் (உறுப்பு 127) = அமர்வில் பங்கேற்கும் காலத்தில் வழக்கமான உச்ச நீதிமன்ற நீதிபதிக்கு இணையான முழு அதிகாரங்கள்.", "1"),

        ("POLITY_SC_HARD_038", "Hard",
         "Who constitutionally determines the allowances payable to a retired Judge invited to sit and act in the Supreme Court under Article 128?",
         "அரசியலமைப்பு உறுப்பு 128-ன் கீழ் உச்ச நீதிமன்றத்தில் அமர்ந்து செயல்பட அழைக்கப்படும் ஓய்வு பெற்ற நீதிபதிக்கு வழங்கப்படும் படிகளை அரசியலமைப்பு ரீதியாகத் தீர்மானிப்பவர் யார்?",
         ("The Parliament of India by law", "நாடாளுமன்றச் சட்டம் மூலம்", "The President of India by order", "குடியரசுத் தலைவர் ஆணை மூலம் (President by order)", "The Chief Justice of India independently", "இந்தியத் தலைமை நீதிபதி தன்னிச்சையாக", "The Union Finance Ministry", "ஒன்றிய நிதி அமைச்சகம்"),
         "B",
         "Article 128 specifies that a retired judge sitting and acting in the Supreme Court 'shall be entitled to such allowances as the President may by order determine'.",
         "அரசியலமைப்பு உறுப்பு 128, உச்ச நீதிமன்றத்தில் அமர்ந்து செயல்படும் ஓய்வு பெற்ற நீதிபதி 'குடியரசுத் தலைவர் ஆணையால் தீர்மானிக்கும் படிகளைப் பெற உரிமையுடையவர்' எனக் கூறுகிறது.",
         ("Parliament laws govern regular judges' salaries under Art 125, not retired judge allowances under Art 128.", "நாடாளுமன்றச் சட்டம் உறுப்பு 125 வழக்கமான நீதிபதிகள் சம்பளம் பற்றியது.", "President by order is the exact authority specified in Article 128 for determining allowances.", "குடியரசுத் தலைவர் ஆணை மூலம் என்பது உறுப்பு 128-ல் குறிப்பிடப்பட்டுள்ள துல்லியமான அதிகாரமாகும்.", "CJI requests attendance with President's consent, but President determines allowances.", "CJI அழைக்கிறார், ஆனால் படிகளைக் குடியரசுத் தலைவர் தீர்மானிக்கிறார்.", "Finance Ministry executes administrative disbursement.", "நிதி அமைச்சகம் வழங்குதலைச் செய்கிறது."),
         "Confusing regular SC Judges' salaries (determined by Parliament by law under Art 125) with retired SC Judges' allowances under Art 128 (determined by President by order).", "வழக்கமான நீதிபதிகள் சம்பளத்தையும் (நாடாளுமன்றச் சட்டம்) ஓய்வு பெற்ற நீதிபதிகள் படிகளையும் (குடியரசுத் தலைவர் ஆணை) குழப்புதல்.", "Art 125 Regular SC Judge Salary -> Determined by Parliament by Law; Art 128 Retired SC Judge Allowances -> Determined by President by Order.", "உறுப்பு 125 வழக்கமான நீதிபதி சம்பளம் -> நாடாளுமன்றச் சட்டம்; உறுப்பு 128 ஓய்வு பெற்ற நீதிபதி படிகள் -> குடியரசுத் தலைவர் ஆணை.", "1"),

        ("POLITY_SC_HARD_039", "Hard",
         "Under Article 146(2), rules framed by the Chief Justice of India regarding salaries, allowances, leave, or pensions of Supreme Court officers and servants require whose approval?",
         "அரசியலமைப்பு உறுப்பு 146(2)-ன் கீழ், உச்ச நீதிமன்ற அதிகாரிகள் மற்றும் ஊழியர்களின் சம்பளங்கள், படிகள், விடுமுறை அல்லது ஓய்வூதியம் தொடர்பாக CJI இயற்றும் விதிகளுக்கு யாருடைய ஒப்புதல் தேவை?",
         ("The Parliament of India", "இந்திய நாடாளுமன்றம்", "The Union Public Service Commission", "ஒன்றிய அரசுப் பணியாளர் தேர்வாணையம்", "The President of India", "இந்தியக் குடியரசுத் தலைவர் (President of India)", "The Comptroller and Auditor General of India", "இந்தியத் தலைமைத் தணிக்கைக் கட்டுப்பாட்டு அதிகாரி"),
         "C",
         "Article 146(2) proviso mandates that rules made by the CJI relating to salaries, allowances, leave or pensions of SC officers and servants SHALL REQUIRE THE APPROVAL OF THE PRESIDENT.",
         "அரசியலமைப்பு உறுப்பு 146(2) விதிவிலக்கு, உச்ச நீதிமன்ற அதிகாரிகள் மற்றும் ஊழியர்களின் சம்பளம், படிகள், விடுமுறை, ஓய்வூதியம் தொடர்பாக CJI இயற்றும் விதிகளுக்குக் குடியரசுத் தலைவரின் ஒப்புதல் கட்டாயம் தேவை எனக் கூறுகிறது.",
         ("Parliament does not approve internal staff rules framed by CJI.", "நாடாளுமன்றம் ஊழியர் விதிகளுக்கு ஒப்புதல் அளிப்பதில்லை.", "UPSC consultation is barred for SC staff appointments under Art 146(1).", "UPSC கலந்தாய்வு உறுப்பு 146(1)-ன் கீழ் விலக்கப்பட்டுள்ளது.", "The President of India approval is explicitly mandatory under Article 146(2) proviso.", "இந்தியக் குடியரசுத் தலைவரின் ஒப்புதல் உறுப்பு 146(2) விதிவிலக்கின் கீழ் கட்டாயமாகும்.", "CAG audits accounts, does not approve rules.", "CAG தணிக்கை செய்கிறார், விதிகளுக்கு ஒப்புதல் அளிப்பதில்லை."),
         "Thinking that CJI has absolute power to fix SC staff salaries without any executive approval, missing the President's approval requirement under Article 146(2) proviso.", "CJI எவ்வித நிர்வாக ஒப்புதலுமின்றி ஊழியர் சம்பளத்தை நிர்ணயிக்கலாம் என நினைத்து குடியரசுத் தலைவர் ஒப்புதல் தேவையை விடுத்தல்.", "Art 146 Staff Rules: CJI appoints officers & frames rules. BUT rules relating to Salaries/Allowances/Pensions REQUIRE APPROVAL OF THE PRESIDENT (Art 146(2) Proviso).", "உறுப்பு 146 ஊழியர் விதிகள்: CJI விதிகளை இயற்றுகிறார். ஆனால் சம்பளம்/படிகள் தொடர்பான விதிகளுக்குக் குடியரசுத் தலைவர் ஒப்புதல் கட்டாயம்.", "1"),

        ("POLITY_SC_HARD_040", "Hard",
         "Under Article 146(3), why are all administrative expenses of the Supreme Court (including salaries and pensions of officers and servants) CHARGED upon the Consolidated Fund of India?",
         "அரசியலமைப்பு உறுப்பு 146(3)-ன் கீழ், உச்ச நீதிமன்றத்தின் அனைத்து நிர்வாகச் செலவுகளும் (ஊழியர்களின் சம்பளம் மற்றும் ஓய்வூதியம் உட்பட) ஏன் இந்தியத் தொகுப்பு நிதியில் சுமத்தப்பட்ட செலவாக வைக்கப்பட்டுள்ளன?",
         ("To reduce administrative burden on the Law Ministry", "சட்ட அமைச்சகத்தின் நிர்வாக பாரத்தைக் குறைக்க", "To allow Parliament to vote on judicial salaries annually", "நாடாளுமன்றம் ஆண்டுதோறும் நீதித்துறை சம்பளத்திற்கு வாக்களிக்க அனுமதிக்க", "To bypass auditing by the Comptroller and Auditor General", "CAG தணிக்கையைத் தவிர்க்க", "To secure the financial independence of the Supreme Court from executive and parliamentary control", "நிர்வாக மற்றும் நாடாளுமன்றக் கட்டுப்பாட்டிலிருந்து உச்ச நீதிமன்றத்தின் நிதிச் சுதந்திரத்தைப் பாதுகாக்க"),
         "D",
         "Article 146(3) makes administrative expenses of SC CHARGED upon the Consolidated Fund of India (non-votable by Parliament) to insulate the Supreme Court from parliamentary political control and secure Financial Independence.",
         "அரசியலமைப்பு உறுப்பு 146(3) உச்ச நீதிமன்ற நிர்வாகச் செலவுகளை இந்தியத் தொகுப்பு நிதியில் சுமத்தப்பட்ட செலவாக (நாடாளுமன்ற வாக்களிப்பிற்கு உட்பட்டதல்ல) மாற்றி, நீதித்துறையின் நிதிச் சுதந்திரத்தைப் பாதுகாக்கிறது.",
         ("Law Ministry burden reduction is not the constitutional rationale.", "சட்ட அமைச்சக பாரம் குறைப்பு காரணமல்ல.", "Charged expenditure means NON-VOTABLE by Parliament, opposite of annual voting.", "சுமத்தப்பட்ட செலவு என்றால் நாடாளுமன்ற வாக்களிப்பிற்கு உட்பட்டதல்ல.", "CAG still audits judicial accounts.", "CAG தணிக்கை தொடர்கிறது.", "Securing Financial Independence from executive/parliamentary interference is the core constitutional objective of Article 146(3).", "நிர்வாக மற்றும் நாடாளுமன்றத் தலையீடற்ற நிதிச் சுதந்திரத்தைப் பாதுகாப்பதே உறுப்பு 146(3)-ன் முதன்மை அரசியலமைப்பு நோக்கமாகும்."),
         "Confusing 'charged expenditure' (non-votable, safeguards independence) with 'made from' expenditure (subject to annual parliamentary vote).", "சுமத்தப்பட்ட செலவு (வாக்களிப்பிற்கு உட்பட்டதல்ல, சுதந்திரப் பாதுகாப்பு) மற்றும் சாதாரண வாக்களிக்கப்படும் செலவு ஆகியவற்றை குழப்புதல்.", "Art 146(3) Charged Expenditure = Administrative Expenses of SC non-votable by Parliament -> Safeguards Financial Independence of Supreme Court.", "உறுப்பு 146(3) சுமத்தப்பட்ட செலவு = நாடாளுமன்ற வாக்களிப்பிற்கு உட்பட்டதல்ல -> உச்ச நீதிமன்ற நிதிச் சுதந்திரத்தைப் பாதுகாக்கிறது.", "1"),

        ("POLITY_SC_HARD_041", "Hard",
         "How does the Original Jurisdiction of the Indian Supreme Court under Article 131 differ structurally from the Original Jurisdiction of the US Supreme Court?",
         "அரசியலமைப்பு உறுப்பு 131-ன் கீழ் இந்திய உச்ச நீதிமன்றத்தின் மூல ஆதிக்கம் அமெரிக்க உச்ச நீதிமன்றத்தின் மூல ஆதிக்கத்திலிருந்து அமைப்பியல் ரீதியாக எவ்வாறு வேறுபடுகிறது?",
         ("US Supreme Court original jurisdiction is specified in the US Constitution and cannot be altered or expanded by Congress, whereas Indian SC Original Jurisdiction under Art 131 is strictly federal, while Writ Original Jurisdiction under Art 32 is concurrent with High Courts under Art 226", "அமெரிக்க SC மூல ஆதிக்கம் அரசியலமைப்பில் குறிப்பிடப்பட்டு காங்கிரஸால் மாற்ற முடியாது, ஆனால் இந்திய SC உறுப்பு 131 மூல ஆதிக்கம் கூட்டாட்சி சார்ந்தது, உறுப்பு 32 பேராணை ஆதிக்கம் HC-உடன் இணைந்ததாகும்", "US Supreme Court has no original jurisdiction at all", "அமெரிக்க உச்ச நீதிமன்றத்திற்கு மூல ஆதிக்கமே இல்லை", "Indian Supreme Court original jurisdiction applies to all criminal trials directly", "இந்திய உச்ச நீதிமன்ற மூல ஆதிக்கம் அனைத்து குற்றவியல் வழக்குகளுக்கும் நேரடியாகப் பொருந்தும்", "Indian Supreme Court cannot entertain disputes between States", "இந்திய உச்ச நீதிமன்றம் மாநிலங்களுக்கு இடையேயான தகராறுகளை விசாரிக்க முடியாது"),
         "A",
         "In the US, SC original jurisdiction covers cases affecting ambassadors and where a State is a party (fixed by US Constitution Marbury v. Madison). In India, Art 131 covers federal disputes exclusively, while Art 32 writ original jurisdiction is concurrent with HCs (Art 226).",
         "அமெரிக்காவில் SC மூல ஆதிக்கம் தூதர்கள் மற்றும் மாநிலங்கள் தொடர்பான வழக்குகளை உள்ளடக்கியது (காங்கிரஸால் மாற்ற முடியாது). இந்தியாவில் உறுப்பு 131 கூட்டாட்சி தகராறுகளையும், உறுப்பு 32 பேராணை மூல ஆதிக்கம் HC-உடன் இணைந்தும் செயல்படுகிறது.",
         ("US SC original jurisdiction is fixed by US Constitution; Indian SC Art 131 is exclusive federal original jurisdiction, while Art 32 writ jurisdiction is concurrent with HCs under Art 226.", "அமெரிக்க SC மூல ஆதிக்கம் அரசியலமைப்பால் நிர்ணயிக்கப்பட்டது; இந்திய SC உறுப்பு 131 கூட்டாட்சி சார்ந்தது, உறுப்பு 32 இணைந்த ஆதிக்கமாகும்.", "US SC DOES have original jurisdiction under Article III.", "அமெரிக்க SC-க்கு மூல ஆதிக்கம் உண்டு.", "Indian SC does NOT conduct original criminal trials.", "இந்திய SC நேரடி குற்றவியல் விசாரணை நடத்துவதில்லை.", "Indian SC DOES entertain inter-state disputes under Art 131.", "இந்திய SC மாநில தகராறுகளை விசாரிக்கும்."),
         "Assuming US Supreme Court and Indian Supreme Court have identical Original Jurisdiction scopes.", "அமெரிக்க மற்றும் இந்திய உச்ச நீதிமன்றங்களின் மூல ஆதிக்கம் முற்றிலும் ஒன்று என நினைத்தல்.", "Original Jurisdiction Comparison = US SC Original Jurisdiction (Ambassadors + States) is fixed by US Constitution Article III; Indian SC has Exclusive Federal Original Jurisdiction (Art 131) and Concurrent Writ Original Jurisdiction (Art 32).", "மூல ஆதிக்கம் ஒப்பீடு = அமெரிக்க SC மூல ஆதிக்கம் தூதர்கள் & மாநிலங்கள் பற்றியது; இந்திய SC உறுப்பு 131 கூட்டாட்சி சார்ந்தது, உறுப்பு 32 பேராணை சார்ந்தது.", "2"),

        ("POLITY_SC_HARD_042", "Hard",
         "How does the constitutional basis of Judicial Review in India differ from that in the United States?",
         "இந்தியாவில் நீதித்துறை ஆய்வின் (Judicial Review) அரசியலமைப்பு அடிப்படை அமெரிக்காவிலிருந்து எவ்வாறு வேறுபடுகிறது?",
         ("Judicial Review in US is derived from judicial precedent (Marbury v. Madison 1803) without explicit constitutional mention, whereas in India it is EXPLICITLY embodied in Articles 13, 32, 131-136, 143, 226, 246", "அமெரிக்காவில் நீதித்துறை ஆய்வு அரசியலமைப்பில் குறிப்பிடப்படாமல் தீர்ப்பு முன்மாதிரி (Marbury v. Madison 1803) மூலம் வந்தது, ஆனால் இந்தியாவில் உறுப்புகள் 13, 32, 131-136, 226, 246 ஆகியவற்றில் தெளிவாகக் குறிப்பிடப்பட்டுள்ளது", "Judicial Review in India is derived only from unwritten conventions", "இந்தியாவில் நீதித்துறை ஆய்வு எழுதப்படாத மரபுகளில் இருந்து மட்டுமே வந்தது", "US Constitution explicitly mentions Judicial Review in 50 Articles", "அமெரிக்க அரசியலமைப்பு 50 உறுப்புகளில் நீதித்துறை ஆய்வைக் தெளிவாகக் குறிப்பிடுகிறது", "India does not have Judicial Review", "இந்தியாவில் நீதித்துறை ஆய்வே இல்லை"),
         "B",
         "In the US, Judicial Review was formulated by Chief Justice John Marshall in *Marbury v. Madison (1803)* as an implied power. In India, Judicial Review is EXPLICITLY written into the text of the Constitution (Arts 13, 32, 226, 246, etc.).",
         "அமெரிக்காவில் நீதித்துறை ஆய்வு தலைமை நீதிபதி ஜான் மார்ஷலால் *Marbury v. Madison (1803)* வழக்கில் மறைமுக அதிகாரமாக உருவாக்கப்பட்டது. இந்தியாவில் நீதித்துறை ஆய்வு அரசியலமைப்பு உரையில் (உறுப்புகள் 13, 32, 226, 246) தெளிவாக எழுதப்பட்டுள்ளது.",
         ("Judicial Review in US is derived from Marbury v. Madison 1803; in India it is EXPLICITLY provided in constitutional text.", "அமெரிக்காவில் Marbury v. Madison 1803 வழக்கில் இருந்து வந்தது; இந்தியாவில் அரசியலமைப்பு உரையில் தெளிவாக உள்ளது.", "India's Judicial Review is WRITTEN into constitutional text.", "இந்தியாவின் நீதித்துறை ஆய்வு அரசியலமைப்பில் எழுதப்பட்டுள்ளது.", "US Constitution does NOT explicitly mention Judicial Review in its text.", "அமெரிக்க அரசியலமைப்பு உரையில் நீதித்துறை ஆய்வு குறிப்பிடப்படவில்லை.", "India DOES have robust Judicial Review.", "இந்தியாவில் வலிமையான நீதித்துறை ஆய்வு உண்டு."),
         "Thinking Judicial Review in India is an unwritten doctrine inferred only from court cases like in the US.", "இந்தியாவிலும் அமெரிக்கா போல நீதித்துறை ஆய்வு வழக்கிலிருந்து மட்டுமே பெறப்பட்ட எழுதப்படாத கோட்பாடு என நினைத்தல்.", "Judicial Review Origin = US: Implied Power derived from Marbury v. Madison (1803); India: EXPLICITLY written in Articles 13, 32, 131-136, 226, 246.", "நீதித்துறை ஆய்வு தோற்றம் = அமெரிக்கா: Marbury v. Madison (1803) வழக்கு மூலம்; இந்தியா: உறுப்புகள் 13, 32, 226 போன்றவற்றில் தெளிவாக எழுதப்பட்டது.", "2"),

        ("POLITY_SC_HARD_043", "Hard",
         "How did the interpretation of Article 21 evolve from A.K. Gopalan (1950) to Maneka Gandhi (1978) regarding 'Due Process of Law'?",
         "உறுப்பு 21-ன் கீழ் 'Due Process of Law' தொடர்பாக ஏ.கே. கோபாலன் (1950) வழக்கிலிருந்து மேனகா காந்தி (1978) வழக்கு வரை உச்ச நீதிமன்ற விளக்கம் எவ்வாறு பரிணாமம் அடைந்தது?",
         ("A.K. Gopalan adopted strict Japanese 'Procedure Established by Law' (procedural check only), whereas Maneka Gandhi expanded it to American Substantive 'Due Process of Law' (just, fair and reasonable check)", "ஏ.கே. கோபாலன் ஜப்பானிய 'சட்டத்தால் அமைக்கப்பட்ட நடைமுறை' என்பதை ஏற்றுக்கொண்டார்; மேனகா காந்தி அதை அமெரிக்க 'Due Process of Law' (நீதியான, நியாயமான நடைமுறை) என விரிவுபடுத்தினார்", "A.K. Gopalan adopted American Due Process while Maneka Gandhi restricted it to Procedure Established by Law", "ஏ.கே. கோபாலன் அமெரிக்க Due Process-ஐ ஏற்றுக்கொண்டார், மேனகா காந்தி அதை சுருக்கினார்", "Both cases rejected Article 21 applicability to executive actions", "இரண்டு வழக்குகளும் உறுப்பு 21 நிர்வாக நடவடிக்கைகளுக்குப் பொருந்தாது என நிராகரித்தன", "Neither case discussed Article 21", "எந்த வழக்கிலும் உறுப்பு 21 விவாதிக்கப்படவில்லை"),
         "A",
         "In A.K. Gopalan (1950), SC took a narrow view: Art 21 only protects against arbitrary EXECUTIVE action if a enacted procedure exists. In Maneka Gandhi (1978), SC expanded Art 21 to protect against arbitrary LEGISLATIVE action as well, requiring procedure to be 'just, fair and reasonable' (Substantive Due Process).",
         "ஏ.கே. கோபாலன் வழக்கில் (1950), சட்டம் இருந்தால் போதும் என குறுகிய விளக்கம் அளிக்கப்பட்டது. மேனகா காந்தி வழக்கில் (1978), சட்டம் மற்றும் நடைமுறை 'நீதியானதாக, நியாயமானதாக' இருக்க வேண்டும் எனக் கூறி அமெரிக்க Substantive Due Process கோட்பாடு கொண்டுவரப்பட்டது.",
         ("A.K. Gopalan (1950) = Procedural check only ('Procedure Established by Law'); Maneka Gandhi (1978) = Substantive check ('Due Process' - Just, Fair & Reasonable).", "ஏ.கே. கோபாலன் (1950) = நடைமுறை ஆய்வு மட்டுமே; மேனகா காந்தி (1978) = நீதியான, நியாயமான ஆய்வு (Due Process).", "Statement is reversed.", "கூற்று தலைகீழானது.", "Both cases applied Art 21 to executive actions.", "இரண்டும் நிர்வாக நடவடிக்கைகளுக்குப் பொருந்தும் என்றன.", "Both cases extensively discussed Art 21.", "இரண்டும் உறுப்பு 21-ஐ விரிவாக விவாதித்தன."),
         "Swapping the rulings of A.K. Gopalan (1950) and Maneka Gandhi (1978).", "ஏ.கே. கோபாலன் (1950) மற்றும் மேனகா காந்தி (1978) தீர்ப்புகளை மாற்றிப் புரிந்து கொள்ளுதல்.", "Art 21 Evolution: Gopalan (1950) -> Procedure Established by Law (Procedural Check ONLY against Executive); Maneka Gandhi (1978) -> Substantive Due Process (Just, Fair & Reasonable Check against BOTH Executive & Legislature).", "உறுப்பு 21 பரிணாமம்: கோபாலன் (1950) -> சட்டத்தால் அமைக்கப்பட்ட நடைமுறை; மேனகா காந்தி (1978) -> நீதியான, நியாயமான நடைமுறை (Due Process).", "2"),

        ("POLITY_SC_HARD_044", "Hard",
         "How does the Advisory Jurisdiction of the Indian Supreme Court under Article 143 compare with that of the US Supreme Court?",
         "அரசியலமைப்பு உறுப்பு 143-ன் கீழ் இந்திய உச்ச நீதிமன்றத்தின் ஆலோசனை ஆதிக்கம் அமெரிக்க உச்ச நீதிமன்றத்தோடு எவ்வாறு ஒப்பிடப்படுகிறது?",
         ("US Supreme Court has no advisory jurisdiction and refuses to give advisory opinions, whereas Indian SC possesses explicit Advisory Jurisdiction under Article 143", "அமெரிக்க உச்ச நீதிமன்றத்திற்கு ஆலோசனை ஆதிக்கமே இல்லை மற்றும் ஆலோசனை வழங்க மறுக்கிறது; ஆனால் இந்திய SC உறுப்பு 143-ன் கீழ் ஆலோசனை ஆதிக்கத்தைக் கொண்டுள்ளது", "US Supreme Court gives advisory opinions to Congress daily", "அமெரிக்க SC நாள்தோறும் காங்கிரஸுக்கு ஆலோசனை வழங்குகிறது", "Indian Supreme Court advisory opinions are legally binding on all High Courts", "இந்திய SC ஆலோசனைகள் அனைத்து உயர் நீதிமன்றங்களையும் சட்டப்பூர்வமாகக் கட்டுப்படுத்தும்", "Both Supreme Courts have identical advisory jurisdiction", "இரண்டு உச்ச நீதிமன்றங்களுக்கும் ஒரே மாதிரியான ஆலோசனை ஆதிக்கம் உண்டு"),
         "B",
         "The US Supreme Court strictly refuses to issue advisory opinions (holds that Article III limits judicial power to actual 'Cases and Controversies'). In contrast, Article 143 explicitly empowers the President of India to seek advisory opinions from the Indian Supreme Court.",
         "அமெரிக்க உச்ச நீதிமன்றம் ஆலோசனை வழங்க மறுக்கிறது (வழக்குகள் மற்றும் தகராறுகளை மட்டுமே விசாரிக்கும்). மாறாக, இந்திய அரசியலமைப்பு உறுப்பு 143 குடியரசுத் தலைவர் உச்ச நீதிமன்றத்திடம் ஆலோசனை கோர வழிவகை செய்கிறது.",
         ("US SC has NO advisory jurisdiction under Art III US Constitution; Indian SC HAS explicit Advisory Jurisdiction under Art 143.", "அமெரிக்க SC-க்கு ஆலோசனை ஆதிக்கம் இல்லை; இந்திய SC-க்கு உறுப்பு 143-ன் கீழ் ஆலோசனை ஆதிக்கம் உண்டு.", "US SC strictly refuses advisory opinions since 1793 (Jay Treaty reference refusal).", "அமெரிக்க SC 1793 முதல் ஆலோசனை வழங்க மறுக்கிறது.", "Indian SC advisory opinions under Art 143 are NOT legally binding precedent under Art 141.", "இந்திய SC உறுப்பு 143 ஆலோசனை உறுப்பு 141 முன்மாதிரி சட்டம் அல்ல.", "Advisory jurisdiction is NOT identical."),
         "Thinking the US Supreme Court also gives advisory opinions to the US President just like the Indian Supreme Court under Article 143.", "அமெரிக்க உச்ச நீதிமன்றமும் இந்திய உச்ச நீதிமன்றத்தைப் போல குடியரசுத் தலைவருக்கு ஆலோசனை வழங்குகிறது என நினைத்தல்.", "Advisory Jurisdiction Comparison = India: Explicitly provided under Art 143 (President consults SC); US: Absolutely NO advisory jurisdiction (US SC refuses non-justiciable advisory references).", "ஆலோசனை ஆதிக்கம் ஒப்பீடு = இந்தியா: உறுப்பு 143-ன் கீழ் உண்டு; அமெரிக்கா: முற்றிலும் இல்லை (ஆலோசனை வழங்க மறுக்கிறது).", "2"),

        ("POLITY_SC_HARD_045", "Hard",
         "What structural feature distinguishes the Indian judicial system from the dual judicial system of the United States?",
         "இந்திய நீதித்துறையை அமெரிக்காவின் இரட்டை நீதித்துறை அமைப்பிலிருந்து (Dual Judicial System) வேறுபடுத்தும் அமைப்பியல் அம்சம் எது?",
         ("India has a Single Integrated Judicial System enforcing both Central and State laws, whereas US has a Dual Judiciary (Federal Courts for Federal Laws, State Courts for State Laws)", "இந்தியா மையம் மற்றும் மாநிலச் சட்டங்கள் இரண்டையும் அமல்படுத்தும் ஒற்றை ஒருங்கிணைந்த நீதித்துறை அமைப்பைக் கொண்டுள்ளது; அமெரிக்கா இரட்டை நீதித்துறையைக் கொண்டுள்ளது", "US has a single integrated judiciary while India has a dual judiciary", "அமெரிக்கா ஒற்றை அமைப்பையும் இந்தியா இரட்டை அமைப்பையும் கொண்டுள்ளது", "India has separate federal and state Supreme Courts", "இந்தியாவில் தனித்தனி ஒன்றிய மற்றும் மாநில உச்ச நீதிமன்றங்கள் உள்ளன", "US Supreme Court has no appellate jurisdiction over State Supreme Courts", "அமெரிக்க உச்ச நீதிமன்றத்திற்கு மாநில உச்ச நீதிமன்றங்கள் மீது மேல்முறையீட்டு ஆதிக்கம் இல்லை"),
         "A",
         "The Indian Constitution establishes a Single Integrated Judiciary with Supreme Court at the apex, High Courts below it, and Subordinate Courts below High Courts, enforcing BOTH Central and State laws. US has a dual system (Federal Judiciary enforcing Federal Laws, State Judiciary enforcing State Laws).",
         "இந்திய அரசியலமைப்பு உச்ச நீதிமன்றத்தை உச்சியில் கொண்டு மையம் மற்றும் மாநிலச் சட்டங்கள் இரண்டையும் அமல்படுத்தும் 'ஒற்றை ஒருங்கிணைந்த நீதித்துறை அமைப்பை' (Single Integrated Judiciary) நிறுவுகிறது. அமெரிக்காவில் இரட்டை நீதித்துறை அமைப்பு உள்ளது.",
         ("India has Single Integrated Judiciary enforcing Central + State laws; US has Dual Judiciary (Federal vs State).", "இந்தியா ஒற்றை ஒருங்கிணைந்த நீதித்துறை அமைப்பைக் கொண்டுள்ளது; அமெரிக்கா இரட்டை நீதித்துறையைக் கொண்டுள்ளது.", "Statement is reversed.", "கூற்று தலைகீழானது.", "India does NOT have separate federal and state Supreme Courts.", "இந்தியாவில் தனித்தனி உச்ச நீதிமன்றங்கள் இல்லை.", "US SC has federal appellate jurisdiction under Art III."),
         "Confusing Indian Federalism in Legislature/Executive (Dual Structure) with Indian Judiciary (Single Integrated Structure).", "இந்திய சட்டமன்ற/நிர்வாக கூட்டாட்சியை (இரட்டை அமைப்பு) நீதித்துறை அமைப்போடு (ஒற்றை ஒருங்கிணைந்த அமைப்பு) குழப்புதல்.", "Indian Judicial Hierarchy = Single Integrated Hierarchy (Apex: SC -> HC -> Subordinate Courts). Enforces both Union and State laws.", "இந்திய நீதித்துறை வரிசை = ஒற்றை ஒருங்கிணைந்த அமைப்பு (SC -> HC -> கீழமை நீதிமன்றங்கள்). மையம் & மாநில சட்டங்கள் இரண்டையும் அமல்படுத்தும்.", "1"),

        ("POLITY_SC_HARD_046", "Hard",
         "Under Article 130 of the Constitution, what condition MUST be satisfied for the Chief Justice of India to hold sittings of the Supreme Court at a place OTHER than Delhi?",
         "அரசியலமைப்பு உறுப்பு 130-ன் கீழ் டெல்லி தவிர பிற இடத்தில் உச்ச நீதிமன்ற அமர்வை நடத்த தலைமை நீதிபதி என்ன நிபந்தனையை கட்டாயம் நிறைவு செய்ய வேண்டும்?",
         ("Prior approval of the President of India", "இந்தியக் குடியரசுத் தலைவரின் முன்ஒப்புதல் (Approval of the President)", "A 2/3rd majority resolution of the Rajya Sabha", "மாநிலங்களவையின் 2/3 பங்கு பெரும்பான்மைத் தீர்மானம்", "Concurrence of the Union Law Minister and Attorney General", "ஒன்றிய சட்ட அமைச்சர் மற்றும் அட்டர்னி ஜெனரல் ஒப்புதல்", "Approval of the Bar Council of India", "இந்திய பார் கவுன்சிலின் ஒப்புதல்"),
         "B",
         "Article 130 specifies: 'The Supreme Court shall sit in Delhi or in such other place or places as the Chief Justice of India may, WITH THE APPROVAL OF THE PRESIDENT, from time to time, appoint.'",
         "அரசியலமைப்பு உறுப்பு 130: 'உச்ச நீதிமன்றம் டெல்லியில் அல்லது குடியரசுத் தலைவரின் ஒப்புதலுடன் CJI அவ்வப்போது நியமிக்கும் பிற இடத்தில் அமரும்.'",
         ("Rajya Sabha resolution is not required under Art 130.", "மாநிலங்களவைத் தீர்மானம் தேவையில்லை.", "Approval of the President is the explicit constitutional requirement under Article 130.", "குடியரசுத் தலைவரின் ஒப்புதல் என்பது உறுப்பு 130-ன் கீழ் உள்ள துல்லியமான அரசியலமைப்பு நிபந்தனையாகும்.", "Law Minister/AG concurrence is not mentioned in text.", "சட்ட அமைச்சர்/AG ஒப்புதல் உரையில் இல்லை.", "Bar Council approval is irrelevant.", "பார் கவுன்சில் ஒப்புதல் தொடர்பில்லாதது."),
         "Thinking CJI can establish Circuit Benches of Supreme Court outside Delhi unilaterally without Presidential approval.", "குடியரசுத் தலைவர் ஒப்புதலின்றி CJI தன்னிச்சையாக டெல்லிக்கு வெளியே சுழற்சி அமர்வுகளை (Circuit Benches) அமைக்கலாம் என நினைத்தல்.", "Seat of SC (Art 130) = Delhi. To hold sittings elsewhere -> CJI appoints + Approval of the President MANDATORY.", "உச்ச நீதிமன்ற அமர்வு (உறுப்பு 130) = டெல்லி. வேறு இடத்தில் அமர்வு நடத்த -> CJI நியமனம் + குடியரசுத் தலைவர் ஒப்புதல் கட்டாயம்.", "1"),

        ("POLITY_SC_HARD_047", "Hard",
         "According to Article 348(1)(a) of the Constitution of India, in which language MUST all proceedings in the Supreme Court of India be conducted until Parliament by law otherwise provides?",
         "இந்திய அரசியலமைப்பு உறுப்பு 348(1)(a)-ன் படி, நாடாளுமன்றம் சட்டத்தின் மூலம் வேறு விதமாக வழிவகை செய்யும் வரை, உச்ச நீதிமன்றத்தின் அனைத்து நடவடிக்கைகளும் எந்த மொழியில் நடத்தப்பட வேண்டும்?",
         ("Hindi in Devanagari script", "தேவநாகரி எழுத்துவடிவில் இந்தி", "English language only", "ஆங்கில மொழி மட்டுமே (English language only)", "Hindi or English at the option of the litigant", "வழக்குதாரரின் விருப்பப்படி இந்தி அல்லது ஆங்கிலம்", "Any official language listed in the Eighth Schedule", "எட்டாவது அட்டவணையில் உள்ள எந்தவொரு அலுவல் மொழியும்"),
         "C",
         "Article 348(1)(a) explicitly mandates that until Parliament by law otherwise provides, ALL PROCEEDINGS in the Supreme Court and in every High Court shall be in the ENGLISH LANGUAGE.",
         "அரசியலமைப்பு உறுப்பு 348(1)(a), நாடாளுமன்றம் சட்டம் இயற்றும் வரை, உச்ச நீதிமன்றம் மற்றும் அனைத்து உயர் நீதிமன்றங்களின் அனைத்து நடவடிக்கைகளும் ஆங்கில மொழியிலேயே இருக்க வேண்டும் எனக் கட்டாயமாக்குகிறது.",
         ("Hindi is not the mandatory language of Supreme Court proceedings under Art 348(1)(a).", "இந்தி உச்ச நீதிமன்ற நடவடிக்கைகளின் கட்டாய மொழி அல்ல.", "English language ONLY is the explicit mandate of Article 348(1)(a) for Supreme Court proceedings.", "ஆங்கில மொழி மட்டுமே என்பது உறுப்பு 348(1)(a)-ன் கீழ் உச்ச நீதிமன்ற நடவடிக்கைகளுக்கான கட்டாய விதியாகும்.", "Litigant option does not apply to SC proceedings under Art 348(1)(a).", "வழக்குதாரர் விருப்பம் SC நடவடிக்கைகளுக்குப் பொருந்தாது.", "Eighth Schedule languages do not automatically apply to SC proceedings.", "8-வது அட்டவணை மொழிகள் தானாகப் பொருந்தாது."),
         "Confusing High Court language provisions (where Governor with President's consent can authorize Hindi/regional language under Art 348(2)) with Supreme Court language (strictly English under Art 348(1)(a)).", "உயர் நீதிமன்ற மொழி விதியையும் (ஆளுநர் குடியரசுத் தலைவர் ஒப்புதலுடன் இந்தி/பிராந்திய மொழியை அனுமதிக்கலாம்) உச்ச நீதிமன்ற மொழி விதியையும் (ஆங்கிலம் மட்டுமே) குழப்புதல்.", "Language of Supreme Court (Art 348(1)(a)) = English Language ONLY. (Note: Governor with President's consent can authorize Hindi/State Official Language in HIGH COURT under Art 348(2), but NOT in Supreme Court).", "உச்ச நீதிமன்ற மொழி (உறுப்பு 348(1)(a)) = ஆங்கில மொழி மட்டுமே.", "3"),

        ("POLITY_SC_HARD_048", "Hard",
         "What is the fundamental procedural difference between a 'Review of Judgment' under Article 137 and a 'Recall of Judgment' under the inherent powers of the Supreme Court?",
         "அரசியலமைப்பு உறுப்பு 137-ன் கீழ் வரும் 'சீராய்வு' (Review) மற்றும் உச்ச நீதிமன்றத்தின் இயல்பான அதிகாரங்களின் கீழ் வரும் 'திரும்பப் பெறுதல்' (Recall) ஆகியவற்றிற்கு இடையேயான அடிப்படை நடைமுறை வேறுபாடு என்ன?",
         ("Review re-examines a judgment for errors apparent on the face of the record, whereas Recall voids a judgment passed without jurisdiction or in violation of natural justice (audi alteram partem)", "Review என்பது தீர்ப்பின் முகப்பிலுள்ள பிழைகளை மறுபரிசீலனை செய்கிறது; Recall என்பது அதிகார வரம்பின்றியோ அல்லது இயற்கை நீதி மீறப்பட்டோ வழங்கப்பட்ட தீர்ப்பை செல்லாததாக்குகிறது", "Review applies only to criminal cases while Recall applies only to civil cases", "Review குற்றவியல் வழக்குகளுக்கும் Recall சிவில் வழக்குகளுக்கும் மட்டுமே பொருந்தும்", "Review requires Presidential sanction while Recall requires Law Cabinet sanction", "Review-க்கு குடியரசுத் தலைவர் ஒப்புதலும் Recall-க்கு சட்ட அமைச்சரவை ஒப்புதலும் தேவை", "There is no legal difference between Review and Recall", "Review மற்றும் Recall இடையே எந்த சட்ட வேறுபாடும் இல்லை"),
         "D",
         "In *Asim Kumar Sen v. State of WB*, SC clarified that Review (Art 137) re-examines merits for error apparent on record, whereas Recall (inherent power under Art 142) invalidates a decree passed per incuriam, without jurisdiction, or violating audi alteram partem (natural justice).",
         "அசீம் குமார் சென் வழக்கில், SC தெளிவுபடுத்தியது: Review (உறுப்பு 137) தீர்ப்பின் முகப்பிலுள்ள பிழைகளை மறுபரிசீலனை செய்கிறது. Recall (உறுப்பு 142) அதிகார வரம்பின்றியோ அல்லது இயற்கை நீதியை மீறியோ வழங்கப்பட்ட உத்தரவை முற்றிலும் செல்லாததாக்குகிறது.",
         ("Review re-examines judgment for errors apparent on record, whereas Recall voids judgment passed without jurisdiction or violating natural justice.", "Review என்பது தீர்ப்பின் முகப்பிலுள்ள பிழைகளை மறுபரிசீலனை செய்கிறது; Recall என்பது இயற்கை நீதி மீறப்பட்ட தீர்ப்பை செல்லாததாக்குகிறது.", "Not divided by civil/criminal distinction.", "சிவில்/குற்றவியல் எனப் பிரிக்கப்படுவதில்லை.", "Presidential/Cabinet sanction is not required for either.", "அமைச்சரவை ஒப்புதல் தேவையில்லை.", "Distinct legal concepts in procedure.", "வெவ்வேறான சட்டக் கருத்துக்கள்."),
         "Confusing Review of Judgment (Article 137 - error on face of record) with Recall of Order (Article 142 - violation of natural justice / lack of jurisdiction).", "சீராய்வு (Review) மற்றும் திரும்பப் பெறுதல் (Recall) ஆகியவற்றின் வேறுபாட்டை அறியாமல் குழம்புவது.", "Review (Art 137) = Corrects error apparent on face of record (30 days limit); Recall (Art 142) = Voids order passed without jurisdiction or violating Natural Justice (Audi alteram partem).", "Review (உறுப்பு 137) = தீர்ப்பின் முகப்பிலுள்ள பிழையைத் திருத்துவது; Recall (உறுப்பு 142) = இயற்கை நீதி மீறப்பட்ட உத்தரவைச் செல்லாததாக்குவது.", "1"),

        ("POLITY_SC_HARD_049", "Hard",
         "Why is the Indian Judiciary constitutionally described as a 'Single Integrated Judicial System' despite India having a federal polity?",
         "இந்தியா கூட்டாட்சி அமைப்பைக் கொண்டிருந்த போதிலும், இந்திய நீதித்துறை ஏன் அரசியலமைப்பு ரீதியாக 'ஒற்றை ஒருங்கிணைந்த நீதித்துறை அமைப்பு' என விவரிக்கப்படுகிறது?",
         ("Because the Supreme Court appoints all sub-magistrates directly", "ஏனெனில் உச்ச நீதிமன்றம் அனைத்து நடுவர்களையும் நேரடியாக நியமிக்கிறது", "Because a single hierarchy of courts (Supreme Court at apex, High Courts, Subordinate Courts) enforces BOTH Union (Central) and State laws", "ஏனெனில் உச்சத்தில் உச்ச நீதிமன்றம் கொண்ட ஒற்றை நீதித்துறை வரிசை ஒன்றியம் மற்றும் மாநிலச் சட்டங்கள் இரண்டையும் அமல்படுத்துகிறது", "Because State Governors have no authority over state courts", "ஏனெனில் மாநில ஆளுநர்களுக்கு நீதிமன்றங்கள் மீது அதிகாரமில்லை", "Because all High Court judgments are written in Hindi", "ஏனெனில் அனைத்து உயர் நீதிமன்ற தீர்ப்புகளும் இந்தியில் எழுதப்படுகின்றன"),
         "A",
         "Unlike US Dual Judiciary (where Federal Courts enforce Federal Laws and State Courts enforce State Laws), India has a Single Integrated Judiciary: a unified pyramid of courts with SC at the apex that enforces BOTH Central and State laws.",
         "அமெரிக்க இரட்டை நீதித்துறை போலல்லாமல், இந்தியாவில் உச்சத்தில் உச்ச நீதிமன்றத்தைக் கொண்ட ஒருங்கிணைந்த பிரமிட் போன்ற நீதித்துறை அமைப்பு ஒன்றியம் மற்றும் மாநிலச் சட்டங்கள் இரண்டையும் அமல்படுத்துகிறது.",
         ("Direct appointment by SC is incorrect (HC appoints subordinate judges under Art 233-235).", "SC நேரடியாக நியமிப்பதாகக் கூறுவது தவறு.", "Single hierarchy enforcing BOTH Union and State laws is the exact definition of Single Integrated Judicial System.", "ஒன்றியம் மற்றும் மாநிலச் சட்டங்கள் இரண்டையும் அமல்படுத்துவதே ஒற்றை ஒருங்கிணைந்த அமைப்பின் துல்லியமான வரையறையாகும்.", "Governor authority is administrative under Art 233.", "ஆளுநர் அதிகாரம் நிர்வாகச் சார்ந்ததே.", "Language is English/regional, not Hindi only.", "மொழி இந்தி மட்டுமே அல்ல."),
         "Assuming India has separate Federal Courts for Union Laws and State Courts for State Laws like the USA.", "அமெரிக்கா போல இந்தியாவிலும் ஒன்றிய சட்டங்களுக்குத் தனி நீதிமன்றங்களும் மாநில சட்டங்களுக்குத் தனி நீதிமன்றங்களும் உள்ளன என நினைத்தல்.", "Single Integrated Judiciary = Unified pyramid (SC -> HC -> Subordinate Courts) enforcing BOTH Central and State laws. Core unifying feature of Indian Constitution.", "ஒற்றை ஒருங்கிணைந்த நீதித்துறை = உச்ச நீதிமன்றம் முதல் கீழமை நீதிமன்றங்கள் வரை ஒன்றியம் மற்றும் மாநிலச் சட்டங்கள் இரண்டையும் அமல்படுத்தும் ஒரே அமைப்பு.", "2"),

        ("POLITY_SC_HARD_050", "Hard",
         "What is the ultimate constitutional significance of Article 141 declaring that the law declared by the Supreme Court shall be binding on all courts within India?",
         "உச்ச நீதிமன்றத்தால் அறிவிக்கப்படும் சட்டம் இந்தியாவில் உள்ள அனைத்து நீதிமன்றங்களையும் கட்டுப்படுத்தும் என்று உறுப்பு 141 அறிவிப்பதன் இறுதி அரசியலமைப்பு முக்கியத்துவம் என்ன?",
         ("It establishes a system of binding judicial precedent (Stare Decisis), creating uniform constitutional and legal jurisprudence throughout India", "இது கட்டாய நீதித்துறை முன்மாதிரி சட்ட முறையை (Stare Decisis) நிறுவி, நாடு முழுவதும் சீரான அரசியலமைப்பு மற்றும் சட்டக் கோட்பாட்டை உருவாக்குகிறது", "It abolishes the law-making power of State Legislatures", "இது மாநில சட்டமன்றங்களின் சட்டம் இயற்றும் அதிகாரத்தை ரத்து செய்கிறது", "It makes Supreme Court decisions subject to review by the Law Commission", "இது உச்ச நீதிமன்ற முடிவுகளை சட்ட ஆணையத்தின் சீராய்வுக்கு உட்படுத்துகிறது", "It forces High Courts to seek prior approval from SC before delivering any judgment", "உயர் நீதிமன்றங்கள் எந்த தீர்ப்பையும் வழங்கும் முன் SC-ன் முன்ஒப்புதலைப் பெறக் கட்டாயப்படுத்துகிறது"),
         "B",
         "Article 141 embeds the doctrine of Stare Decisis (binding judicial precedent) into the Constitution, ensuring that Supreme Court interpretations of law create a uniform, cohesive legal system across all States and Union Territories of India.",
         "உறுப்பு 141 Stare Decisis (கட்டாய முன்மாதிரி சட்டம்) கோட்பாட்டை அரசியலமைப்பில் பொறித்து, உச்ச நீதிமன்ற தீர்ப்புகள் இந்தியா முழுமைக்கும் சீரான சட்ட அமைப்பை உருவாக்குவதை உறுதி செய்கிறது.",
         ("Stare Decisis & uniform legal jurisprudence creation throughout India is the ultimate significance of Art 141.", "நாடு முழுவதும் சீரான சட்டக் கோட்பாட்டை உருவாக்குவதே உறுப்பு 141-ன் இறுதி முக்கியத்துவமாகும்.", "State Legislature law-making power is preserved under Art 246.", "மாநில சட்டமன்ற அதிகாரம் பாதுகாக்கப்படுகிறது.", "Law Commission review is invalid.", "சட்ட ஆணைய சீராய்வு தவறு.", "Prior approval for HC judgments is invalid.", "முன்ஒப்புதல் தவறு."),
         "Treating Article 141 as merely a procedural rule rather than the bedrock of judicial precedent and uniform legal system in India.", "உறுப்பு 141-ஐ ஒரு சாதாரண நடைமுறை விதியாக மட்டும் கருதுவது.", "Article 141 Significance = Establishes Doctrine of Stare Decisis (Binding Precedent). Ensures UNIFORMITY of Law across all Courts in India.", "உறுப்பு 141 முக்கியத்துவம் = Stare Decisis (முன்மாதிரி சட்டம்) கோட்பாட்டை நிறுவி, இந்தியா முழுவதும் சட்டத்தின் சீரான தன்மையை உறுதி செய்கிறது.", "1")
    ]

    hard = []
    for item in hard_data:
        qid, diff, s_en, s_ta, opts, corr, exp_en, exp_ta, why_args, trap_en, trap_ta, tip_en, tip_ta, sp = item
        options = make_options(*opts)
        why_not = make_why_not(corr, *why_args)
        hard.append(build_q(qid, diff, s_en, s_ta, options, corr, exp_en, exp_ta, why_not, trap_en, trap_ta, tip_en, tip_ta, sp))
    return hard

def main():
    print("==================================================")
    print("GENERATING SUPREME COURT PART 1 MCQS (150 QUESTIONS)")
    print("==================================================")

    easy_qs = get_easy_questions()
    medium_qs = get_medium_questions()
    hard_qs = get_hard_questions()

    print(f"✅ Generated Easy Questions: {len(easy_qs)}")
    print(f"✅ Generated Medium Questions: {len(medium_qs)}")
    print(f"✅ Generated Hard Questions: {len(hard_qs)}")

    assert len(easy_qs) == 50, f"Expected 50 Easy questions, got {len(easy_qs)}"
    assert len(medium_qs) == 50, f"Expected 50 Medium questions, got {len(medium_qs)}"
    assert len(hard_qs) == 50, f"Expected 50 Hard questions, got {len(hard_qs)}"

    all_qs = easy_qs + medium_qs + hard_qs
    print(f"Total Part 1 MCQs: {len(all_qs)}")

    # Validation Engine
    all_ids = set()
    all_stems = set()
    ans_counts = {"A": 0, "B": 0, "C": 0, "D": 0}

    for idx, q in enumerate(all_qs):
        # 1. ID uniqueness
        qid = q["id"]
        if qid in all_ids:
            raise ValueError(f"Duplicate ID found: {qid}")
        all_ids.add(qid)

        # 2. Text uniqueness
        stem = q["question"]["en"].strip().lower()
        if stem in all_stems:
            raise ValueError(f"Duplicate question text found at index {idx}: {q['question']['en']}")
        all_stems.add(stem)

        # 3. Options count
        opts = q.get("options", [])
        if len(opts) != 4:
            raise ValueError(f"Question {qid} does not have exactly 4 options!")
        
        # 4. Correct answer validity & match
        corr = q.get("correct_answer")
        if corr not in ["A", "B", "C", "D"]:
            raise ValueError(f"Question {qid} has invalid correct_answer: {corr}")
        ans_counts[corr] += 1

        opt_ids = [o["id"] for o in opts]
        if opt_ids != ["A", "B", "C", "D"]:
            raise ValueError(f"Question {qid} options IDs are {opt_ids}")

        # 5. Bilingual text presence
        if not q["question"]["en"] or not q["question"]["ta"]:
            raise ValueError(f"Question {qid} missing bilingual stem!")
        if not q["explanation"]["en"] or not q["explanation"]["ta"]:
            raise ValueError(f"Question {qid} missing bilingual explanation!")
        for o in opts:
            if not o["en"] or not o["ta"]:
                raise ValueError(f"Question {qid} option {o['id']} missing bilingual text!")

    print("\n--- Answer Key Distribution ---")
    for letter, count in ans_counts.items():
        print(f"Option {letter}: {count}")

    # Output directory
    out_dir = "data/questions/polity"
    os.makedirs(out_dir, exist_ok=True)

    easy_path = os.path.join(out_dir, "supreme_court_easy.json")
    medium_path = os.path.join(out_dir, "supreme_court_medium.json")
    hard_path = os.path.join(out_dir, "supreme_court_hard.json")

    with open(easy_path, "w", encoding="utf-8") as f:
        json.dump(easy_qs, f, ensure_ascii=False, indent=2)
    print(f"✅ Saved Easy Dataset -> {easy_path}")

    with open(medium_path, "w", encoding="utf-8") as f:
        json.dump(medium_qs, f, ensure_ascii=False, indent=2)
    print(f"✅ Saved Medium Dataset -> {medium_path}")

    with open(hard_path, "w", encoding="utf-8") as f:
        json.dump(hard_qs, f, ensure_ascii=False, indent=2)
    print(f"✅ Saved Hard Dataset -> {hard_path}")

    print("\n==================================================")
    print("PART 1 MCQ GENERATION COMPLETED SUCCESSFULLY!")
    print("==================================================")

if __name__ == "__main__":
    main()
