# -*- coding: utf-8 -*-
"""
Generator for Supreme Court Hard MCQs (50 Questions)
Topic: Supreme Court of India
Difficulty: Hard
File: data/questions/polity/supreme_court_hard.json
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

def build_q(qid, difficulty, stem_en, stem_ta, options, correct_letter, exp_en, exp_ta, why_args, trap_en, trap_ta, tip_en, tip_ta, source_part):
    opts_en = [o["en"] for o in options]
    opts_ta = [o["ta"] for o in options]
    why_not = make_why_not(correct_letter, *why_args)
    
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
         ("A private individual/corporation CANNOT be a party to an Art 131 suit.", "தனிநபர்/கழகம் உறுப்பு 131 வழக்கில் தரப்பினராக இருக்க முடியாது.", "State vs Union suit IS maintainable under Art 131.", "மாநிலம் vs ஒன்றியம் வழக்கு உறுப்பு 131-ன் கீழ் செல்லும்.", "State vs State suit IS maintainable under Art 131.", "மாநிலம் vs மாநிலம் வழக்கு உறுப்பு 131-ன் கீழ் செல்லும்.", "Group of States vs Union IS maintainable under Art 131.", "மாநிலங்களின் குழு vs ஒன்றியம் வழக்கு செல்லும்."),
         "Thinking private individuals can join a suit under Article 131 Original Jurisdiction.", "தனிநபர்கள் உறுப்பு 131 மூல ஆதிக்க வழக்கில் இணையலாம் எனத் தவறாக நினைத்தல்.", "Art 131 Original Jurisdiction Parties = ONLY Units of Federation (Union & States). Private bodies/individuals strictly barred.", "உறுப்பு 131 தரப்பினர்கள் = ஒன்றியம் மற்றும் மாநிலங்கள் மட்டுமே.", "2"),

        ("POLITY_SC_HARD_002", "Hard",
         "For a legal dispute between the Union and a State to lie under the Original Jurisdiction of Article 131, what essential condition must be satisfied?",
         "அரசியலமைப்பு உறுப்பு 131-ன் கீழ் ஒன்றியம் மற்றும் மாநிலத்திற்கு இடையே வழக்கு செல்லுபடியாக என்ன அத்தியாவசிய நிபந்தனை நிறைவு செய்யப்பட வேண்டும்?",
         ("The dispute must involve a political disagreement between ruling parties", "தகராறு ஆளும் கட்சிகளுக்கிடையேயான அரசியல் கருத்து வேறுபாடாக இருக்க வேண்டும்", "The dispute must involve a question of law or fact on which the existence or extent of a LEGAL RIGHT depends", "தகராறு ஒரு சட்ட உரிமையின் இருப்பு அல்லது எல்லையைத் தீர்மானிக்கும் சட்ட அல்லது உண்மை கேள்வியைக் கொண்டிருக்க வேண்டும்", "The dispute must have been approved by the Governor of the State", "தகராறிற்கு மாநில ஆளுநர் ஒப்புதல் அளித்திருக்க வேண்டும்", "The dispute must relate exclusively to international border agreements", "தகராறு சர்வதேச எல்லை உடன்படிக்கைகள் பற்றியதாக மட்டுமே இருக்க வேண்டும்"),
         "B",
         "Article 131 explicitly mandates that the dispute must involve any question (whether of law or fact) on which the existence or extent of a LEGAL RIGHT depends (State of West Bengal v. UOI 1963). Purely political questions are excluded.",
         ("Political disagreements without legal rights are excluded.", "சட்ட உரிமை இல்லாத அரசியல் கருத்து வேறுபாடுகள் விலக்கப்படும்.", "Question of Law or Fact determining existence/extent of a LEGAL RIGHT is the mandatory constitutional condition.", "சட்ட உரிமையை தீர்மானிக்கும் சட்டக் கேள்வி என்பது கட்டாய நிபந்தனையாகும்.", "Governor approval is not required under Art 131.", "ஆளுநர் ஒப்புதல் தேவையில்லை.", "International border agreements are excluded under Art 131 proviso.", "சர்வதேச எல்லை உடன்படிக்கைகள் விலக்கப்படும்."),
         "Confusing political disputes (non-justiciable under Art 131) with disputes involving legal rights (justiciable under Art 131).", "அரசியல் தகராறுகளையும் சட்ட உரிமை தகராறுகளையும் குழப்புதல்.", "Art 131 Condition = Must involve a LEGAL RIGHT (State of WB v. UOI 1963). Political/party disputes barred.", "உறுப்பு 131 நிபந்தனை = ஒரு சட்ட உரிமை (Legal Right) சார்ந்ததாக இருக்க வேண்டும்.", "2"),

        ("POLITY_SC_HARD_003", "Hard",
         "Which of the following statements regarding the Special Leave Petition (SLP) under Article 136 of the Indian Constitution is INCORRECT?",
         "இந்திய அரசியலமைப்பு உறுப்பு 136-ன் கீழ் சிறப்பு விடுப்பு மனு (SLP) பற்றிய எந்தக் கூற்று தவறானது?",
         ("It is an extraordinary discretionary jurisdiction exercisable against final or interlocutory orders", "இது இறுதி அல்லது இடைக்கால உத்தரவுகளுக்கு எதிராகப் பயன்படுத்தக்கூடிய தன்னிச்சையான அதிகாரமாகும்", "It can be granted against decisions of any court or tribunal except Armed Forces tribunals", "இராணுவ தீர்ப்பாயங்கள் தவிர எந்தவொரு நீதிமன்றம் அல்லது தீர்ப்பாயத்தின் முடிவுகளுக்கும் வழங்கப்படலாம்", "The petitioner has an absolute constitutional right to be heard on merits once an SLP is filed", "SLP தாக்கல் செய்யப்பட்டவுடன் வழக்கின் தகுதி அடிப்படையில் விசாரணை பெற மனுதாரருக்கு முழு உரிமை உண்டு", "It covers civil, criminal, income-tax, and labor matters", "இது சிவில், குற்றவியல், வருமான வரி மற்றும் தொழிலாளர் விவகாரங்களை உள்ளடக்கியது"),
         "C",
         "Filing an SLP does not automatically give the petitioner a right to be heard on merits. The Supreme Court exercises strict discretion; it can summarily dismiss the SLP at the threshold without giving detailed reasons.",
         "SLP தாக்கல் செய்வதன் மூலம் மனுதாரருக்கு தானாகவே தகுதி அடிப்படையில் விசாரணை பெறும் உரிமை கிடைத்துவிடாது. உச்ச நீதிமன்றம் அதை ஆரம்பத்திலேயே சுருக்கமாகத் தள்ளுபடி செய்யலாம்.",
         ("SLP applies to interlocutory and final orders.", "SLP இடைக்கால மற்றும் இறுதி உத்தரவுகளுக்குப் பொருந்தும்.", "Armed Forces exception under Art 136(2) is valid.", "இராணுவத் தீர்ப்பாய விலக்கு செல்லும்.", "Petitioner does NOT have an absolute right to be heard on merits (SLP is discretionary at threshold).", "மனுதாரருக்கு தகுதி விசாரணை பெற முழு உரிமை இல்லை (SLP ஆரம்ப நிலையிலேயே தள்ளுபடி செய்யப்படலாம்).", "SLP covers all branches of law.", "SLP அனைத்து சட்டப் பிரிவுகளையும் உள்ளடக்கியது."),
         "Assuming SLP admission is a mandatory right of appeal like a statutory first appeal.", "SLP என்பது ஒரு சாதாரண சட்டப்பூர்வ மேல்முறையீட்டு உரிமை எனக் கருதுவது.", "Article 136 SLP = Discretionary at entry level. No automatic right to appeal on merits.", "உறுப்பு 136 SLP = ஆரம்ப நிலையில் தன்னிச்சையானது. தகுதி விசாரணை பெற தானியங்கி உரிமையில்லை.", "2"),

        ("POLITY_SC_HARD_004", "Hard",
         "Under Article 143, when a reference is made by the President on a question of law or fact of public importance (Art 143(1)), what is the legal nature of the Supreme Court's bench and procedure?",
         "உறுப்பு 143(1)-ன் கீழ் பொது முக்கியத்துவம் வாய்ந்த கேள்வியில் குடியரசுத் தலைவர் ஆலோசனை கோரும் போது, உச்ச நீதிமன்ற அமர்வு மற்றும் நடைமுறையின் சட்டப்பூர்வ தன்மை என்ன?",
         ("The opinion must be delivered in open court by a Constitution Bench of at least 5 judges", "குறைந்தது 5 நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வால் திறந்த நீதிமன்றத்தில் கருத்து வழங்கப்பட வேண்டும்", "The opinion can be delivered privately in writing by a single judge to the President", "ஒரு தனி நீதிபதியால் குடியரசுத் தலைவருக்கு ரகசியமாக எழுதப்பட்டு வழங்கப்படலாம்", "The opinion must be passed by a unanimous vote of all 34 judges", "அனைத்து 34 நீதிபதிகளின் ஒருமனதான வாக்களிப்பு மூலம் வழங்கப்பட வேண்டும்", "The opinion is pronounced by the Law Commission on behalf of SC", "SC சார்பாக சட்ட ஆணையம் கருத்தை அறிவிக்கும்"),
         "A",
         "Under Article 145(3) read with Art 143, any Presidential reference under Article 143 MUST be heard by a Constitution Bench of at least FIVE judges, and under Art 145(4), opinions must be delivered in open court.",
         "உறுப்பு 145(3)-ன் படி, உறுப்பு 143 குடியரசுத் தலைவர் ஆலோசனை மனு குறைந்தபட்சம் 5 நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வால் திறந்த நீதிமன்றத்தில் (Open Court) விசாரிக்கப்பட்டு கருத்து வழங்கப்பட வேண்டும்.",
         ("Art 145(3) mandates 5-judge Constitution Bench and Art 145(4) mandates open court delivery for Art 143 references.", "உறுப்பு 145(3) 5-நீதிபதிகள் அமர்வையும் உறுப்பு 145(4) திறந்த நீதிமன்றத்தையும் கட்டாயமாக்குகிறது.", "Private opinion by single judge is unconstitutional under Art 145(4).", "தனி நீதிபதியின் ரகசிய கருத்து அரசியலமைப்புக்கு எதிரானது.", "Unanimous vote of all 34 judges is not required.", "34 நீதிபதிகளின் ஒருமனதான வாக்கு தேவையில்லை.", "Law Commission has no authority to deliver SC opinions.", "சட்ட ஆணையத்திற்கு இதில் அதிகாரமில்லை."),
         "Thinking advisory opinions can be rendered informally in camera by CJI alone.", "தலைமை நீதிபதி மட்டுமே ரகசியமாக ஆலோசனை வழங்குவார் என நினைப்பது.", "Art 143 Reference Procedure = Minimum 5-Judge Constitution Bench + Delivered in OPEN COURT (Art 145(3) & 145(4)).", "உறுப்பு 143 ஆலோசனை நடைமுறை = குறைந்தபட்சம் 5-நீதிபதிகள் அரசியலமைப்பு அமர்வு + திறந்த நீதிமன்ற அறிவிப்பு.", "2"),

        ("POLITY_SC_HARD_005", "Hard",
         "What is the key distinction between Article 32 (Supreme Court) and Article 226 (High Courts) regarding the duty to grant remedy for Fundamental Rights violation?",
         "அடிப்படை உரிமை மீறலுக்கு நிவாரணம் வழங்குவதில் உறுப்பு 32 (SC) மற்றும் உறுப்பு 226 (HC) ஆகியவற்றுக்கு இடையேயான முக்கிய வேறுபாடு என்ன?",
         ("SC cannot issue Mandamus, while HC can", "SC மேண்டமஸ் பிறப்பிக்க முடியாது; HC பிறப்பிக்கலாம்", "Article 32 is a Fundamental Right making SC remedy mandatory, whereas Article 226 is discretionary for High Courts", "உறுப்பு 32 என்பதே ஒரு அடிப்படை உரிமை என்பதால் SC நிவாரணம் கட்டாயமானது; ஆனால் உயர் நீதிமன்றங்களுக்கு உறுப்பு 226 தன்னிச்சையானது", "HC writ jurisdiction is subject to Law Ministry approval", "HC பேராணை அதிகாரம் சட்ட அமைச்சக ஒப்புதலுக்கு உட்பட்டது", "Article 32 applies only during National Emergency", "உறுப்பு 32 தேசிய அவசரநிலையின் போது மட்டுமே பொருந்தும்"),
         "B",
         "Since Article 32 is itself located in Part III (Fundamental Rights), accessing SC for FR enforcement is a Fundamental Right (mandatory duty of SC). Article 226 is outside Part III, making HC writ remedy discretionary.",
         "உறுப்பு 32 பகுதி III-ல் உள்ள ஒரு அடிப்படை உரிமை என்பதால் SC நிவாரணம் வழங்குவது கட்டாயப் பொறுப்பாகும். உறுப்பு 226 பகுதி III-க்கு வெளியே உள்ளதால் HC நிவாரணம் வழங்குவது தன்னிச்சையானது (Discretionary).",
         ("SC can issue all 5 writs including Mandamus.", "SC மேண்டமஸ் உட்பட 5 பேராணைகளையும் பிறப்பிக்கும்.", "Art 32 = Guaranteed Fundamental Right (Mandatory for SC); Art 226 = Discretionary remedy for HC.", "உறுப்பு 32 = உத்தரவாதம் அளிக்கப்பட்ட அடிப்படை உரிமை (SC-க்கு கட்டாயம்); உறுப்பு 226 = HC-க்கு தன்னிச்சை நிவாரணம்.", "Law Ministry approval is not required.", "சட்ட அமைச்சக ஒப்புதல் தேவையில்லை.", "Art 32 applies in normal times and can be suspended only under Art 359 during Emergency.", "உறுப்பு 32 சாதாரண காலத்திலும் பொருந்தும்."),
         "Assuming both SC (Art 32) and HC (Art 226) have identical discretionary powers in granting writ remedies for Fundamental Rights.", "அடிப்படை உரிமைகளுக்கு இரு நீதிமன்றங்களுக்கும் ஒரே மாதிரியான தன்னிச்சை அதிகாரம் தான் உள்ளது என நினைப்பது.", "Writ Obligation = Supreme Court (Art 32) MUST grant remedy (FR itself); High Court (Art 226) HAS DISCRETION to refuse if alternative remedy exists.", "பேராணை கடமை = SC (உறுப்பு 32) கட்டாயம் நிவாரணம் வழங்க வேண்டும்; HC (உறுப்பு 226) மாற்று நிவாரணம் இருந்தால் தள்ளுபடி செய்ய தன்னிச்சை அதிகாரம் உண்டு.", "2"),

        ("POLITY_SC_HARD_006", "Hard",
         "Under Article 134, in which of the following criminal cases does an appeal lie to the Supreme Court AS OF RIGHT (without needing a High Court certificate of fitness)?",
         "உறுப்பு 134-ன் கீழ், எந்தக் குற்றவியல் வழக்கில் உயர் நீதிமன்றச் சான்றிதழ் இன்றியே தானாகவே உரிமையாக (As of Right) உச்ச நீதிமன்றத்தில் மேல்முறையீடு செய்ய முடியும்?",
         ("If High Court has on appeal reversed an order of acquittal of an accused and sentenced him to death", "கீழ் நீதிமன்றத்தின் விடுதலை உத்தரவை உயர் நீதிமன்றம் மாற்றி, குற்றவாளிக்கு மரண தண்டனை விதித்திருந்தால்", "If High Court has affirmed a trial court sentence of 3 years imprisonment", "கீழ் நீதிமன்றத்தின் 3 ஆண்டுகள் சிறைத்தண்டனையை உயர் நீதிமன்றம் உறுதி செய்திருந்தால்", "If trial court acquitted the accused and High Court confirmed acquittal", "கீழ் நீதிமன்ற விடுதலையை உயர் நீதிமன்றமும் உறுதி செய்திருந்தால்", "If High Court sentenced an accused to 6 months imprisonment for civil contempt", "சிவில் அவமதிப்புக்காக உயர் நீதிமன்றம் 6 மாத சிறை விதித்திருந்தால்"),
         "A",
         "Under Article 134(1)(a) & (b), an appeal lies to SC as of right if HC: (a) reversed acquittal and sentenced accused to death, or (b) withdrew case from subordinate court and sentenced accused to death.",
         "உறுப்பு 134(1)(a) மற்றும் (b)-ன் படி, கீழ் நீதிமன்றத்தின் விடுதலையை மாற்றி உயர் நீதிமன்றம் மரண தண்டனை விதித்திருந்தால், சான்றிதழ் இன்றியே தானாகவே SC-ல் மேல்முறையீடு செய்யலாம்.",
         ("Reversal of acquittal + Death Sentence by HC gives AUTOMATIC RIGHT OF APPEAL to SC under Art 134(1)(a).", "விடுதலை மாற்றம் + மரண தண்டனை = உறுப்பு 134(1)(a)-ன் கீழ் தானாகவே மேல்முறையீட்டு உரிமை.", "Affirming 3 years sentence requires HC certificate under Art 134(1)(c).", "3 ஆண்டுகள் தண்டனை உறுதிக்கு சான்றிதழ் தேவை.", "Confirmation of acquittal gives no automatic right of appeal.", "விடுதலை உறுதிக்கு தானியங்கி உரிமை இல்லை.", "Civil contempt appeals are under Contempt Act, not Art 134.", "சிவில் அவமதிப்பு மேல்முறையீடுகள் அவமதிப்புச் சட்டத்தின் கீழ் வரும்."),
         "Assuming ALL criminal appeals to SC require a High Court Certificate of Fitness (Art 134(1)(a) & (b) grant automatic right of appeal in death penalty cases resulting from acquittal reversal).", "அனைத்துக் குற்றவியல் மேல்முறையீடுகளுக்கும் உயர் நீதிமன்ற சான்றிதழ் கட்டாயம் எனக் கருதுவது.", "Automatic Criminal Appeal to SC (No HC Certificate needed) = HC reverses acquittal and passes DEATH SENTENCE (Art 134(1)(a)).", "தானியங்கி குற்றவியல் மேல்முறையீடு = விடுதலையை மாற்றி HC மரண தண்டனை விதித்தல் (உறுப்பு 134(1)(a)).", "2"),

        ("POLITY_SC_HARD_007", "Hard",
         "What is the legal effect of Article 142(2) regarding the investigation and enforcement powers of the Supreme Court?",
         "உச்ச நீதிமன்றத்தின் விசாரணை மற்றும் ஆணை அமலாக்க அதிகாரங்கள் குறித்த உறுப்பு 142(2)-ன் சட்டப்பூர்வ விளைவு என்ன?",
         ("SC has power to secure attendance of any person, discovery/production of documents, and investigation of contempt throughout India", "இந்தியா முழுவதும் எவரையும் நேரில் வரவழைக்கவும், ஆவணங்களைக் கண்டறியவும், அவமதிப்பை விசாரிக்கவும் SC-க்கு முழு அதிகாரம் உண்டு", "SC can issue search warrants only inside Delhi National Capital Territory", "SC டெல்லி தேசிய தலைநகரப் பகுதியில் மட்டுமே சோதனையாணை பிறப்பிக்க முடியும்", "SC order enforcement requires prior ratification by Union Cabinet", "SC ஆணை அமலாக்கத்திற்கு ஒன்றிய அமைச்சரவையின் முன்அனுமதி தேவை", "SC has no power to compel discovery of official government records", "அரசு அதிகாரப்பூர்வ ஆவணங்களை அளிக்கக் கட்டாயப்படுத்த SC-க்கு அதிகாரமில்லை"),
         "A",
         "Article 142(2) states that SC shall have all and every power to make any order for securing attendance of any person, discovery or production of documents, or investigation or punishment of any contempt of itself.",
         "உறுப்பு 142(2)-ன் படி, எவரையும் வரவழைத்தல், ஆவணங்களை உற்பத்தி செய்தல், அவமதிப்பை விசாரித்து தண்டித்தல் ஆகியவற்றுக்கு இந்தியா முழுமைக்கும் பொருந்தும் உத்தரவுகளைப் பிறப்பிக்க SC-க்கு முழு அதிகாரம் உண்டு.",
         ("Art 142(2) gives nationwide power to compel attendance, discovery of documents and investigate contempt.", "உறுப்பு 142(2) நபர்களை வரவழைக்கவும் ஆவணங்களைக் கண்டறியவும் நாடு தழுவிய அதிகாரம் அளிக்கிறது.", "Territorial limit is entire India, not Delhi only.", "ஆட்சிப்பரப்பு இந்தியா முழுமையாகும், டெல்லி மட்டுமே அல்ல.", "Cabinet ratification is unconstitutional requirement.", "அமைச்சரவை ஒப்புதல் தேவையில்லை.", "SC CAN compel production of official documents subject to privilege rules.", "அரசு ஆவணங்களை சமர்ப்பிக்க SC கட்டாயப்படுத்தலாம்."),
         "Confusing territorial limits of High Courts (state boundary) with Supreme Court orders under Art 142 (enforceable throughout the territory of India).", "உயர் நீதிமன்ற ஆட்சிப்பரப்பு எல்லை மற்றும் உச்ச நீதிமன்ற உறுப்பு 142 எல்லையைக் குழப்புவது.", "Article 142 Orders = Executable THROUGHOUT THE TERRITORY OF INDIA in such manner as prescribed by Parliament/President.", "உறுப்பு 142 ஆணைகள் = இந்தியா முழுமைக்கும் அமல்படுத்தப்படக் கூடியவை.", "2"),

        ("POLITY_SC_HARD_008", "Hard",
         "Under Article 125, how are the salaries, allowances, leave, and pensions of Supreme Court judges determined?",
         "உறுப்பு 125-ன் படி, உச்ச நீதிமன்ற நீதிபதிகளின் ஊதியம், படிகள், விடுப்பு மற்றும் ஓய்வூதியம் எவ்வாறு தீர்மானிக்கப்படுகின்றன?",
         ("By Parliament by law, and until so determined, as specified in the Second Schedule", "நாடாளுமன்ற சட்டத்தின் மூலம்; அவ்வாறு தீர்மானிக்கப்படும் வரை 2-வது அட்டவணையில் குறிப்பிட்டுள்ளபடி", "By the Chief Justice of India independently by administrative order", "இந்தியத் தலைமை நீதிபதியால் தன்னிச்சையாக நிர்வாக ஆணை மூலம்", "By the Union Finance Commission every 5 years", "5 ஆண்டுகளுக்கு ஒருமுறை ஒன்றிய நிதி ஆணையத்தால்", "By the President after consultation with UPSC", "UPSC-ஐ கலந்தாலோசித்து குடியரசுத் தலைவரால்"),
         "A",
         "Article 125(1) specifies that judges shall be paid such salaries as determined by Parliament by law and, until provision in that behalf is so made, such salaries as specified in the Second Schedule.",
         "உறுப்பு 125(1)-ன் படி, நாடாளுமன்றச் சட்டத்தால் தீர்மானிக்கப்படும் ஊதியம் நீதிபதிகளுக்கு வழங்கப்படும்; அதுவரை 2-வது அட்டவணையில் குறிப்பிடப்பட்டுள்ள ஊதியம் வழங்கப்படும்.",
         ("Parliament by law determines SC judge salaries (Second Schedule applies until parliamentary enactment).", "நாடாளுமன்ற சட்டத்தால் தீர்மானிக்கப்படும் (அதுவரை 2-வது அட்டவணை பொருந்தும்).", "CJI cannot fix judge salaries.", "CJI ஊதியத்தை நிர்ணயிக்க முடியாது.", "Finance Commission recommends tax devolution, not judge salaries.", "நிதி ஆணையம் வரிப் பகிர்வு பரிந்துரைப்பதே தவிர ஊதியம் அல்ல.", "UPSC has no role in judge salaries.", "UPSC-க்கு இதில் பங்கில்லை."),
         "Assuming SC Judge salaries are fixed by Presidential executive order or CJI notification instead of Parliamentary legislation under Art 125.", "குடியரசுத் தலைவர் ஆணையால் ஊதியம் நிர்ணயிக்கப்படுகிறது என நினைப்பது.", "SC Judge Salary Determination = PARLIAMENT BY LAW (Article 125(1) / Second Schedule).", "SC நீதிபதிகள் ஊதிய நிர்ணயம் = நாடாளுமன்றச் சட்டம் மூலம் (உறுப்பு 125(1)).", "2"),

        ("POLITY_SC_HARD_009", "Hard",
         "Which Article of the Constitution confers power on the Supreme Court to grant Special Leave to Appeal against any judgment passed by any court or tribunal in India EXCEPT Military Courts?",
         "இராணுவ நீதிமன்றங்கள் தவிர இந்தியாவில் உள்ள எந்தவொரு நீதிமன்றம்/தீர்ப்பாயத்தின் உத்தரவிற்கும் எதிராக சிறப்பு விடுப்பு வழங்க SC-க்கு அதிகாரமளிக்கும் உறுப்பு எது?",
         ("Article 136", "உறுப்பு 136", "Article 137", "உறுப்பு 137", "Article 138", "உறுப்பு 138", "Article 139", "உறுப்பு 139"),
         "A",
         "Article 136(1) empowers SC to grant special leave to appeal from any judgment, decree, determination, sentence or order in any cause or matter passed by any court or tribunal in India. Art 136(2) excludes Armed Forces courts.",
         "உறுப்பு 136(1) எந்தவொரு நீதிமன்றம்/தீர்ப்பாயத்தின் உத்தரவிற்கும் எதிராக மேல்முறையீட்டுச் சிறப்பு விடுப்பு வழங்க SC-க்கு அதிகாரமளிக்கிறது. உறுப்பு 136(2) இராணுவ நீதிமன்றங்களை விலக்குகிறது.",
         ("Art 136 = Special Leave Petition (SLP) with Armed Forces exclusion.", "உறுப்பு 136 = சிறப்பு விடுப்பு மனு (இராணுவ நீதிமன்ற விலக்குடன்).", "Art 137 = Review power.", "உறுப்பு 137 = சீராய்வு அதிகாரம்.", "Art 138 = Enlargement of jurisdiction.", "உறுப்பு 138 = அதிகார வரம்பு விரிவாக்கம்.", "Art 139 = Conferment of writ powers.", "உறுப்பு 139 = பேராணை அதிகாரம் வழங்குதல்."),
         "Confusing Article 136 (SLP) with Article 137 (Review).", "உறுப்பு 136 மற்றும் உறுப்பு 137-ஐக் குழப்புவது.", "Special Leave to Appeal = Article 136.", "சிறப்பு விடுப்பு மேல்முறையீடு = உறுப்பு 136.", "2"),

        ("POLITY_SC_HARD_010", "Hard",
         "What is the significance of the 42nd Constitutional Amendment Act 1976 regarding Article 144A and Article 131A, and what happened to them later?",
         "உறுப்பு 144A மற்றும் 131A தொடர்பாக 42-வது திருத்தச் சட்டம் (1976) செய்த மாற்றம் என்ன, பின்னர் அவற்றுக்கு என்ன நேர்ந்தது?",
         ("They restricted SC powers by requiring 7-judge bench for central law validity; they were REPEALED by the 43rd Amendment Act 1977", "அவை மத்திய சட்டங்களின் செல்லுபடியை ஆராய 7-நீதிபதிகள் அமர்வைக் கட்டாயமாக்கி SC அதிகாரத்தைக் குறைத்தன; 43-வது திருத்தச் சட்டம் (1977) மூலம் அவை ரத்து செய்யப்பட்டன", "They created the National Judicial Appointments Commission; struck down in 2015", "அவை NJAC-ஐ அமைத்தன; 2015-ல் ரத்து செய்யப்பட்டன", "They transferred High Courts under Supreme Court administrative control; repealed by 44th Amendment", "அவை உயர் நீதிமன்றங்களை SC நிர்வாகக் கட்டுப்பாட்டின் கீழ் கொண்டு வந்தன; 44-வது திருத்தத்தால் ரத்து செய்யப்பட்டன", "They abolished Advisory Jurisdiction; restored by 52nd Amendment", "அவை ஆலோசனை ஆதிக்கத்தை ரத்து செய்தன; 52-வது திருத்தத்தால் மீண்டும் கொண்டுவரப்பட்டன"),
         "A",
         "The 42nd Amendment (1976) inserted Art 131A & 144A restricting judicial review (requiring 2/3rd majority in a 7-judge bench to declare central law invalid). The 43rd Amendment Act 1977 REPEALED both Articles 131A and 144A, restoring normal SC jurisdiction.",
         "42-வது திருத்தம் (1976) உறுப்புகள் 131A மற்றும் 144A-ஐச் சேர்த்து SC அதிகாரத்தைக் குறைத்தது. 43-வது திருத்தச் சட்டம் 1977 இந்த இரண்டு உறுப்புகளையும் முற்றிலும் ரத்து செய்து பழைய நிலையை மீட்டெடுத்தது.",
         ("42nd Amendment inserted Arts 131A & 144A restricting SC; 43rd Amendment 1977 REPEALED them.", "42-வது திருத்தம் 131A & 144A-ஐச் சேர்த்தது; 43-வது திருத்தம் (1977) அவற்றை ரத்து செய்தது.", "NJAC was 99th Amendment.", "NJAC 99-வது திருத்தம்.", "HC administrative transfer was not Art 144A.", "நிர்வாக மாற்றம் 144A அல்ல.", "Advisory jurisdiction was never abolished.", "ஆலோசனை ஆதிக்கம் ரத்து செய்யப்படவில்லை."),
         "Confusing 42nd Amendment judicial restrictions (repealed by 43rd Amendment 1977) with 44th Amendment 1978 changes.", "43-வது திருத்தம் (1977) மற்றும் 44-வது திருத்தம் (1978) ஆகியவற்றின் பணிகளைக் குழப்புவது.", "Articles 131A & 144A (inserted by 42nd Amend) = REPEALED by 43rd Constitutional Amendment Act, 1977.", "உறுப்புகள் 131A & 144A = 43-வது திருத்தச் சட்டம் 1977 மூலம் ரத்து செய்யப்பட்டன.", "2"),

        ("POLITY_SC_HARD_011", "Hard",
         "Which Article of the Constitution declares that all authorities, civil and judicial, in the territory of India SHALL ACT IN AID of the Supreme Court?",
         "இந்திய எல்லைக்குள் உள்ள அனைத்து சிவில் மற்றும் நீதித்துறை அதிகாரிகளும் உச்ச நீதிமன்றத்திற்கு உதவியாகச் செயல்பட வேண்டும் எனறு உறுதியளிக்கும் உறுப்பு எது?",
         ("Article 141", "உறுப்பு 141", "Article 142", "உறுப்பு 142", "Article 144", "உறுப்பு 144", "Article 145", "உறுப்பு 145"),
         "C",
         "Article 144 mandates that 'All authorities, civil and judicial, in the territory of India shall act in aid of the Supreme Court.'",
         "அரசியலமைப்பு உறுப்பு 144 'இந்திய எல்லைக்குள் உள்ள அனைத்து சிவில் மற்றும் நீதித்துறை அதிகாரிகளும் உச்ச நீதிமன்றத்திற்கு உதவியாகச் செயல்பட வேண்டும்' எனக் கட்டாயமாக்குகிறது.",
         ("Art 141 is binding law on courts.", "உறுப்பு 141 கட்டாய முன்மாதிரி சட்டம்.", "Art 142 is complete justice enforcement.", "உறுப்பு 142 முழுமையான நீதி அமலாக்கம்.", "Art 144 = All civil and judicial authorities shall act in aid of SC.", "உறுப்பு 144 = அனைத்து சிவில் மற்றும் நீதித்துறை அதிகாரிகளும் SC-க்கு உதவியாகச் செயல்பட வேண்டும்.", "Art 145 is Court Rules.", "உறுப்பு 145 நீதிமன்ற விதிகள்."),
         "Confusing Article 144 (Civil & Judicial Authorities acting in aid of SC) with Article 141 (Law declared binding on all courts).", "உறுப்பு 144 மற்றும் உறுப்பு 141 ஆகியவற்றை குழப்புவது.", "Authorities Acting in Aid of SC = Article 144.", "SC-க்கு உதவியாகச் செயல்படும் அதிகாரிகள் = உறுப்பு 144.", "2"),

        ("POLITY_SC_HARD_012", "Hard",
         "Under Article 145(3), what is the MINIMUM bench size required for deciding any case involving a substantial question of law as to the interpretation of the Constitution OR hearing an Article 143 reference?",
         "அரசியலமைப்பு விளக்கமளித்தல் அல்லது உறுப்பு 143 குடியரசுத் தலைவர் ஆலோசனையை விசாரிக்க உறுப்பு 145(3)-ன் படி இருக்க வேண்டிய குறைந்தபட்ச அமர்வு அளவு என்ன?",
         ("3 Judges", "3 நீதிபதிகள்", "5 Judges (Constitution Bench)", "5 நீதிபதிகள் (அரசியலமைப்பு அமர்வு)", "7 Judges", "7 நீதிபதிகள்", "9 Judges", "9 நீதிபதிகள்"),
         "B",
         "Article 145(3) explicitly mandates that the minimum number of Judges who are to sit for deciding any case involving a substantial question of law as to constitutional interpretation or for hearing an Art 143 reference shall be FIVE.",
         "அரசியலமைப்பு விளக்கமளித்தல் அல்லது உறுப்பு 143 ஆலோசனையை விசாரிக்க குறைந்தபட்சம் 5 நீதிபதிகள் கொண்ட அமர்வு அமைக்கப்பட வேண்டும் என உறுப்பு 145(3) கட்டாயமாக்குகிறது.",
         ("3 judges is a Division Bench.", "3 நீதிபதிகள் பிரிவு அமர்வு.", "5 Judges is the constitutionally mandated minimum bench size under Article 145(3).", "5 நீதிபதிகள் உறுப்பு 145(3)-ன் கீழ் கட்டாயமாக்கப்பட்ட குறைந்தபட்ச அமர்வு அளவு.", "7 judges is a larger bench formed when 5-judge bench is reconsidered.", "7 நீதிபதிகள் 5-நீதிபதிகள் அமர்வை சீராய்வு செய்ய அமைக்கப்படுவது.", "9 judges is a larger bench.", "9 நீதிபதிகள் பெரிய அமர்வு."),
         "Confusing Division Bench (3 judges) with Constitution Bench minimum threshold (5 judges under Art 145(3)).", "பிரிவு அமர்வு (3) மற்றும் அரசியலமைப்பு அமர்வு (5) குறைந்தபட்ச அளவைக் குழப்புவது.", "Minimum Constitution Bench Size = 5 Judges (Article 145(3)).", "குறைந்தபட்ச அரசியலமைப்பு அமர்வு அளவு = 5 நீதிபதிகள் (உறுப்பு 145(3)).", "2"),

        ("POLITY_SC_HARD_013", "Hard",
         "In which landmark case did a 13-judge Constitution Bench of the Supreme Court rule by a 7:6 majority that Parliament CANNOT alter the 'Basic Structure' of the Constitution?",
         "எந்த வரலாற்றுச் சிறப்புமிக்க வழக்கில் 13 நீதிபதிகள் கொண்ட உச்ச நீதிமன்ற அமர்வு 7:6 என்ற பெரும்பான்மையில் நாடாளுமன்றம் அரசியலமைப்பின் 'அடிப்படை அமைப்பை' மாற்ற முடியாது எனத் தீர்ப்பளித்தது?",
         ("Golaknath v. State of Punjab (1967)", "கோலக்நாத் vs பஞ்சாப் மாநிலம் (1967)", "Kesavananda Bharati v. State of Kerala (1973)", "கேசவாநந்த பாரதி vs கேரளா மாநிலம் (1973)", "Minerva Mills v. Union of India (1980)", "மினர்வா மில்ஸ் vs இந்திய ஒன்றியம் (1980)", "Waman Rao v. Union of India (1981)", "வாமன் ராவ் vs இந்திய ஒன்றியம் (1981)"),
         "B",
         "In *Kesavananda Bharati Case (1973)*, the largest Constitution Bench in history (13 judges) overruled Golaknath, holding that while Parliament can amend any part of the Constitution under Art 368, it CANNOT alter its Basic Structure.",
         "1973 கேசவாநந்த பாரதி வழக்கில், வரலாற்றிலேயே மிகப்பெரிய 13 நீதிபதிகள் அமர்வு 7:6 பெரும்பான்மையில் அரசியலமைப்பின் 'அடிப்படை அமைப்பை' (Basic Structure) நாடாளுமன்றம் திருத்த முடியாது எனத் தீர்ப்பளித்தது.",
         ("Golaknath was an 11-judge bench (6:5 majority).", "கோலக்நாத் 11 நீதிபதிகள் அமர்வு (6:5).", "Kesavananda Bharati (1973) was a 13-judge bench (7:6 majority) establishing Basic Structure Doctrine.", "கேசவாநந்த பாரதி (1973) 13 நீதிபதிகள் அமர்வு (7:6) அடிப்படை அமைப்புக் கோட்பாட்டை நிறுவியது.", "Minerva Mills was a 5-judge bench.", "மினர்வா மில்ஸ் 5 நீதிபதிகள் அமர்வு.", "Waman Rao applied Basic Structure prospectively from 24 April 1973.", "வாமன் ராவ் 24 ஏப்ரல் 1973 முதல் அடிப்படை அமைப்பைப் பயன்படுத்தியது."),
         "Confusing bench sizes: Golaknath (11 judges), Kesavananda Bharati (13 judges - largest ever in SC history).", "அமர்வு அளவுகள்: கோலக்நாத் (11 நீதிபதிகள்), கேசவாநந்த பாரதி (13 நீதிபதிகள் - வரலாற்றிலேயே மிகப்பெரியது).", "Largest SC Bench in History = Kesavananda Bharati Case (1973) - 13 Judges (7:6 majority).", "வரலாற்றிலேயே மிகப்பெரிய SC அமர்வு = கேசவாநந்த பாரதி வழக்கு (1973) - 13 நீதிபதிகள் (7:6 பெரும்பான்மை).", "3"),

        ("POLITY_SC_HARD_014", "Hard",
         "What cutoff date was established by the Supreme Court in *Waman Rao v. Union of India (1981)* for the application of the Basic Structure Doctrine to laws placed in the Ninth Schedule?",
         "9-வது அட்டவணையில் சேர்க்கப்படும் சட்டங்களுக்கு அடிப்படை அமைப்புக் கோட்பாட்டைப் பயன்படுத்துவதற்கு 1981 வாமன் ராவ் வழக்கில் நிர்ணயிக்கப்பட்ட வரம்பு நாள் எது?",
         ("26 January 1950", "26 ஜனவரி 1950", "24 April 1973 (Date of Kesavananda Bharati Judgment)", "24 ஏப்ரல் 1973 (கேசவாநந்த பாரதி தீர்ப்பு நாள்)", "42nd Amendment enactment date (3 January 1977)", "42-வது திருத்த அமல் நாள் (3 ஜனவரி 1977)", "1 November 1956", "1 நவம்பர் 1956"),
         "B",
         "In *Waman Rao (1981)* and reiterated in *I.R. Coelho (2007)*, SC held that all constitutional amendments/laws placed in the Ninth Schedule ON OR AFTER 24 APRIL 1973 (date of Kesavananda judgment) are open to challenge on Basic Structure grounds.",
         "1981 வாமன் ராவ் மற்றும் 2007 ஐ.ஆர். கோயல்ஹோ வழக்குகளில், 24 ஏப்ரல் 1973 (கேசவாநந்த தீர்ப்பு நாள்) அல்லது அதற்குப் பிறகு 9-வது அட்டவணையில் சேர்க்கப்பட்ட சட்டங்கள் அடிப்படை அமைப்புக்கு எதிராகச் சவால் செய்யப்படலாம் எனக் கூறப்பட்டது.",
         ("26 Jan 1950 is not the Basic Structure cutoff date.", "ஜனவரி 26 அடிப்படை அமைப்பு எல்லை நாள் அல்ல.", "24 April 1973 (Kesavananda judgment date) is the EXACT constitutional cutoff date affirmed in Waman Rao (1981) & IR Coelho (2007).", "24 ஏப்ரல் 1973 (கேசவாநந்த தீர்ப்பு நாள்) என்பது வாமன் ராவ் வழக்கில் நிர்ணயிக்கப்பட்ட எல்லை நாளாகும்.", "Jan 1977 is not the cutoff date.", "ஜனவரி 1977 எல்லை நாள் அல்ல.", "Nov 1956 is Reorganisation date.", "நவம்பர் 1956 மாநில மறுசீரமைப்பு நாள்."),
         "Assuming all Ninth Schedule laws (even pre-1973) can be challenged on Basic Structure grounds (laws added prior to 24 April 1973 are immune).", "1973-க்கு முந்தைய 9-வது அட்டவணைச் சட்டங்களையும் சவால் செய்யலாம் என நினைப்பது (24 ஏப்ரல் 1973-க்கு முந்தையவை பாதுகாக்கப்பட்டவை).", "Ninth Schedule Judicial Review Cutoff Date = 24 APRIL 1973 (Waman Rao 1981 & I.R. Coelho 2007).", "9-வது அட்டவணை நீதித்துறை சீராய்வு எல்லை நாள் = 24 ஏப்ரல் 1973.", "3"),

        ("POLITY_SC_HARD_015", "Hard",
         "Under Article 124(3)(c), a person who is a 'distinguished jurist in the opinion of the President' can be appointed as a Judge of the Supreme Court. Does a similar provision exist for High Court judge appointments?",
         "உறுப்பு 124(3)(c)-ன் படி 'குடியரசுத் தலைவர் கருத்தில் புகழ்பெற்ற சட்ட வல்லுநர்' SC நீதிபதியாகலாம். உயர் நீதிமன்ற நீதிபதி நியமனத்திற்கு இதே போன்ற விதி உள்ளதா?",
         ("Yes, under Article 217(2)(c)", "ஆம், உறுப்பு 217(2)(c)-ன் கீழ் உள்ளது", "No, there is NO 'distinguished jurist' qualification category for appointment as a High Court judge", "இல்லை, உயர் நீதிமன்ற நீதிபதி நியமனத்திற்கு 'புகழ்பெற்ற சட்ட வல்லுநர்' தகுதிப் பிரிவு எதுவும் இல்லை", "Yes, but only with the consent of the Chief Minister", "ஆம், ஆனால் முதலமைச்சரின் ஒப்புதலுடன் மட்டுமே", "Yes, added by the 44th Constitutional Amendment Act", "ஆம், 44-வது திருத்தச் சட்டம் மூலம் சேர்க்கப்பட்டது"),
         "B",
         "Article 124(3)(c) allows a 'distinguished jurist' to be appointed to the Supreme Court. However, Article 217(2) prescribing qualifications for High Court judges contains NO provision for a distinguished jurist.",
         "உறுப்பு 124(3)(c) உச்ச நீதிமன்றத்திற்கு 'புகழ்பெற்ற சட்ட வல்லுநர்' தகுதியை அனுமதிக்கிறது. ஆனால் உயர் நீதிமன்ற நீதிபதி தகுதிகளைக் கூறும் உறுப்பு 217(2)-ல் 'புகழ்பெற்ற சட்ட வல்லுநர்' தகுதி இல்லை.",
         ("Art 217(2)(c) was added by 42nd Amendment but REPEALED by 44th Amendment 1978, leaving NO distinguished jurist category for HC judges.", "44-வது திருத்தம் 1978 மூலம் HC-க்கு அத்தகுதி நீக்கப்பட்டது; எனவே தற்போது HC-க்கு அத்தகுதி இல்லை.", "No distinguished jurist category currently exists for High Court judge appointments.", "உயர் நீதிமன்ற நீதிபதிகளுக்கு புகழ்பெற்ற சட்ட வல்லுநர் தகுதி தற்சமயம் இல்லை.", "CM consent is irrelevant.", "முதலமைச்சர் ஒப்புதல் தொடர்பற்றது.", "44th Amendment removed it from HC qualifications.", "44-வது திருத்தம் HC தகுதியிலிருந்து அதை நீக்கியது."),
         "Assuming the 'distinguished jurist' qualification category applies equally to both Supreme Court and High Court judge appointments.", "புகழ்பெற்ற சட்ட வல்லுநர் தகுதி SC மற்றும் HC ஆகிய இரண்டிற்கும் ஒரே மாதிரி பொருந்தும் எனக் கருதுவது.", "Distinguished Jurist Qualification = Exists ONLY for Supreme Court (Art 124(3)(c)); NOT for High Courts (Art 217(2)).", "புகழ்பெற்ற சட்ட வல்லுநர் தகுதி = உச்ச நீதிமன்றத்திற்கு மட்டுமே உண்டு (உறுப்பு 124(3)(c)); உயர் நீதிமன்றத்திற்கு இல்லை.", "3"),

        ("POLITY_SC_HARD_016", "Hard",
         "Under Article 139A(2), what power does the Supreme Court possess regarding cases pending before DIFFERENT High Courts?",
         "வெவ்வேறான உயர் நீதிமன்றங்களில் நிலுவையில் உள்ள வழக்குகள் குறித்து உறுப்பு 139A(2)-ன் கீழ் உச்ச நீதிமன்றத்திற்கு உள்ள அதிகாரம் என்ன?",
         ("SC can transfer any case pending in one High Court to another High Court", "SC ஒரு உயர் நீதிமன்றத்தில் நிலுவையில் உள்ள வழக்கை மற்றொரு உயர் நீதிமன்றத்திற்கு மாற்றலாம்", "SC can dismiss all cases pending in High Courts automatically", "SC உயர் நீதிமன்றங்களில் உள்ள அனைத்து வழக்குகளையும் தானாகவே தள்ளுபடி செய்யலாம்", "SC can merge two High Courts administratively", "SC இரண்டு உயர் நீதிமன்றங்களை நிர்வாக ரீதியாக இணைக்கலாம்", "SC can mandate that High Courts hear cases only in Hindi", "உயர் நீதிமன்றங்கள் இந்தியில் மட்டுமே வழக்குகளை விசாரிக்க வேண்டும் எனக் கட்டாயப்படுத்தலாம்"),
         "B",
         "Article 139A(2) explicitly empowers the Supreme Court to transfer any case, appeal, or other proceeding pending before one High Court to another High Court if it deems it expedient for the ends of justice.",
         "உறுப்பு 139A(2) நீதியின் நலனுக்காக ஒரு உயர் நீதிமன்றத்தில் நிலுவையில் உள்ள வழக்கு அல்லது மேல்முறையீட்டை மற்றொரு உயர் நீதிமன்றத்திற்கு மாற்ற உச்ச நீதிமன்றத்திற்கு அதிகாரமளிக்கிறது.",
         ("Art 139A(2) empowers SC to transfer cases from ONE High Court to ANOTHER High Court.", "உறுப்பு 139A(2) ஒரு உயர் நீதிமன்றத்திலிருந்து மற்றொரு உயர் நீதிமன்றத்திற்கு வழக்கை மாற்ற அதிகாரமளிக்கிறது.", "Dismissal automatically is unconstitutional.", "தானாகவே தள்ளுபடி செய்வது அரசியலமைப்புக்கு எதிரானது.", "Merging High Courts requires Parliamentary legislation under Art 214/231.", "உயர் நீதிமன்றங்கள் இணைப்பு நாடாளுமன்ற சட்டத்தால் செய்யப்பட வேண்டும்.", "Language mandate is under Art 348.", "மொழி ஆணை உறுப்பு 348-ன் கீழ் வரும்."),
         "Confusing Article 139A(1) (withdrawing case to SC itself) with Article 139A(2) (transferring case from one HC to another HC).", "உறுப்பு 139A(1) (தனக்கு மாற்றுவது) மற்றும் உறுப்பு 139A(2) (ஒரு HC-லிருந்து மற்றொரு HC-க்கு மாற்றுவது) ஆகியவற்றை குழப்புவது.", "Art 139A(1) = Transfer from HC to SC. Art 139A(2) = Transfer from HC to another HC.", "உறுப்பு 139A(1) = HC-லிருந்து SC-க்கு மாற்றுவது. உறுப்பு 139A(2) = ஒரு HC-லிருந்து மற்றொரு HC-க்கு மாற்றுவது.", "3"),

        ("POLITY_SC_HARD_017", "Hard",
         "Which Article of the Constitution empowers Parliament to confer supplemental powers on the Supreme Court to enable it more effectively to exercise its jurisdiction?",
         "உச்ச நீதிமன்றம் தன் அதிகார வரம்பை மிகவும் திறம்படப் பயன்படுத்த துணை அதிகாரங்களை வழங்குவதற்கு நாடாளுமன்றத்திற்கு அதிகாரமளிக்கும் உறுப்பு எது?",
         ("Article 139", "உறுப்பு 139", "Article 140", "உறுப்பு 140", "Article 141", "உறுப்பு 141", "Article 142", "உறுப்பு 142"),
         "B",
         "Article 140 states that Parliament may by law make provision for conferring upon the Supreme Court such supplemental powers, not inconsistent with the Constitution, as may appear necessary for enabling the court to exercise its jurisdiction effectively.",
         "உச்ச நீதிமன்றம் தனது அதிகார வரம்பைப் பயனுள்ள முறையில் செயல்படுத்தத் தேவையான துணை அதிகாரங்களை நாடாளுமன்றம் சட்டத்தால் வழங்க உறுப்பு 140 வழிவகை செய்கிறது.",
         ("Art 139 is writ power expansion.", "உறுப்பு 139 பேராணை விரிவாக்கம்.", "Art 140 = Ancillary / Supplemental Powers of Supreme Court.", "உறுப்பு 140 = உச்ச நீதிமன்றத்தின் துணை அதிகாரங்கள்.", "Art 141 is binding law.", "உறுப்பு 141 கட்டாயச் சட்டம்.", "Art 142 is complete justice enforcement.", "உறுப்பு 142 முழுமையான நீதி அமலாக்கம்."),
         "Confusing Article 140 (Supplemental/Ancillary powers) with Article 142 (Complete justice enforcement).", "உறுப்பு 140 (துணை அதிகாரங்கள்) மற்றும் உறுப்பு 142 (முழுமையான நீதி) ஆகியவற்றை குழப்புவது.", "Ancillary / Supplemental Powers = Article 140.", "துணை அதிகாரங்கள் = உறுப்பு 140.", "3"),

        ("POLITY_SC_HARD_018", "Hard",
         "Under Article 124(4), what happens AFTER both Houses of Parliament pass a removal motion against a Supreme Court Judge by a Special Majority?",
         "உறுப்பு 124(4)-ன் படி நாடாளுமன்றத்தின் இரு அவைகளும் சிறப்புப் பெரும்பான்மையில் நீக்கத் தீர்மானத்தை நிறைவேற்றிய பின் என்ன நிகழும்?",
         ("The judge is automatically removed without further action", "கூடுதல் நடவடிக்கையின்றி நீதிபதி தானாகவே பதவியிலிருந்து நீக்கப்படுவார்", "An address is presented to the President in the SAME SESSION, and the President passes an order removing the Judge", "அதே கூட்டத்தொடரில் குடியரசுத் தலைவரிடம் அறிக்கை சமர்ப்பிக்கப்பட்டு, குடியரசுத் தலைவர் நீதிபதியை நீக்கி ஆணை பிறப்பிப்பார்", "The Chief Justice of India issues the removal order", "இந்தியத் தலைமை நீதிபதி நீக்க ஆணை பிறப்பிப்பார்", "The Supreme Court Collegium must confirm the removal", "உச்ச நீதிமன்ற கொலீஜியம் நீக்கத்தை உறுதி செய்ய வேண்டும்"),
         "B",
         "Under Article 124(4), parliamentary resolution alone does not remove the judge. An address MUST be presented to the President in the SAME SESSION, and the President issues an order for removal.",
         "உறுப்பு 124(4)-ன் படி, நாடாளுமன்றத் தீர்மானம் மட்டுமே நீதிபதியை நீக்கிவிடாது. அதே கூட்டத்தொடரில் குடியரசுத் தலைவரிடம் அறிக்கை அளிக்கப்பட்டு, குடியரசுத் தலைவர் நீக்க ஆணை பிறப்பிக்க வேண்டும்.",
         ("Parliament resolution alone is not the final act.", "நாடாளுமன்றத் தீர்மானம் மட்டுமே இறுதி நடவடிக்கை அல்ல.", "Address presented to President in SAME SESSION + Presidential Order is the constitutional mandate.", "அதே கூட்டத்தொடரில் குடியரசுத் தலைவரிடம் அறிக்கை + குடியரசுத் தலைவர் ஆணை என்பதே அரசியலமைப்பு விதி.", "CJI cannot issue removal order.", "CJI நீக்க ஆணை பிறப்பிக்க முடியாது.", "Collegium confirmation is not required.", "கொலீஜியம் உறுதிப்படுத்தல் தேவையில்லை."),
         "Assuming Parliamentary impeachment vote automatically terminates the judge's tenure without a Presidential removal order.", "நாடாளுமன்ற வாக்கெடுப்பு முடிந்தவுடனேயே நீதிபதி பதவியிழப்பார் எனத் தவறாக நினைப்பது.", "Judge Removal Final Step = Address to President in SAME SESSION -> Presidential Order of Removal.", "நீதிபதி நீக்கம் இறுதிப்படி = அதே கூட்டத்தொடரில் குடியரசுத் தலைவரிடம் அறிக்கை -> குடியரசுத் தலைவரின் நீக்க ஆணை.", "3"),

        ("POLITY_SC_HARD_019", "Hard",
         "Which landmark Supreme Court judgment ruled that the Law declared by the Supreme Court under Article 141 applies RETROSPECTIVELY unless the court explicitly invokes the Doctrine of Prospective Overruling?",
         "உச்ச நீதிமன்றம் 'Prospective Overruling' கோட்பாட்டை வெளிப்படையாகப் பயன்படுத்தாத வரை, உறுப்பு 141-ன் கீழ் SC அறிவிக்கும் சட்டம் கடந்த காலத்திற்கும் (Retrospectively) பொருந்தும் எனத் தீர்ப்பளிக்கப்பட்ட வழக்கு எது?",
         ("Managing Director, ECIL v. B. Karunakar (1993)", "நிர்வாக இயக்குனர், ECIL vs பி. கருணாகரன் (1993)", "Golaknath Case (1967)", "கோலக்நாத் வழக்கு (1967)", "Bengal Immunity Co. v. State of Bihar (1955)", "பெங்கால் இம்யூனிட்டி vs பீகார் மாநிலம் (1955)", "State of West Bengal v. Committee for Protection of Democratic Rights (2010)", "மேற்கு வங்க மாநிலம் vs ஜனநாயக உரிமைகள் பாதுகாப்புக் குழு (2010)"),
         "A",
         "In *ECIL v. B. Karunakar (1993)* and *Sarwan Kumar (2005)*, the SC clarified that the law declared by SC is normally retrospective in operation, applying to all pending cases, UNLESS the court expressly restricts its application prospectively.",
         "1993 ECIL வழக்கின் படி, SC அறிவிக்கும் சட்டம் பொதுவாகக் கடந்த காலத்திற்கும் (Retrospective) நிலுவையில் உள்ள அனைத்து வழக்குகளுக்கும் பொருந்தும்; SC வெளிப்படையாக Prospective Overruling என அறிவித்தால் மட்டுமே அது எதிர்காலத்திற்குப் பொருந்தும்.",
         ("ECIL v. B. Karunakar (1993) held that SC law is retrospectively applicable unless prospective overruling is expressly invoked.", "ECIL வழக்கு SC சட்டம் பொதுவாக கடந்த காலத்திற்கும் பொருந்தும் என்றது.", "Golaknath introduced Prospective Overruling.", "கோலக்நாத் Prospective Overruling-ஐ அறிமுகப்படுத்தியது.", "Bengal Immunity held SC not bound by own past decisions.", "பெங்கால் இம்யூனிட்டி SC தன் தீர்ப்புக்கு கட்டுப்பட்டதல்ல என்றது.", "CPDR 2010 upheld CBI probe order without state consent.", "CPDR வழக்கு மாநில சம்மதமின்றி CBI விசாரணை ஆணையை உறுதி செய்தது."),
         "Assuming Supreme Court rulings apply ONLY prospectively to future cases by default (the default rule is retrospective application unless prospectivity is declared).", "SC தீர்ப்புகள் எப்போதும் எதிர்காலத்திற்கு மட்டுமே பொருந்தும் என நினைப்பது (இயல்பான விதி கடந்த காலத்திற்கும் பொருந்தும் என்பதாகும்).", "Article 141 Law Application = Retrospective by default (unless court expressly declares Prospective Overruling).", "உறுப்பு 141 சட்டப் பயன்பாடு = இயல்பாகக் கடந்த காலத்திற்கும் பொருந்தும் (Prospective என அறிவித்தால் ஒழிய).", "3"),

        ("POLITY_SC_HARD_020", "Hard",
         "What is the position regarding the appointment of a judge whose name was recommended by the Collegium and reiterated unanimously after being sent back by the Government for reconsideration?",
         "கொலீஜியம் பரிந்துரைத்து, அரசு மறுபரிசீலனைக்கு அனுப்பிய பின், கொலீஜியம் மீண்டும் ஒருமனதாக அப் பெயரை வலியுறுத்தினால் (Reiterated), அந்த நியமனத்தின் நிலை என்ன?",
         ("The Government is constitutionally bound to appoint the judge according to the Second Judges Case (1993) and Third Judges Case (1998)", "இரண்டாவது (1993) மற்றும் மூன்றாவது (1998) நீதிபதிகள் வழக்குகளின் படி, அரசு அந்த நீதிபதியை நியமிக்க அரசியலமைப்பு ரீதியாகக் கடமைப்பட்டுள்ளது", "The Government can reject the name permanently without any obligation", "அரசு எந்தக் கடமையுமின்றி அப் பெயரை நிரந்தரமாக நிராகரிக்கலாம்", "The President must refer the dispute to the Cabinet Secretary for arbitration", "குடியரசுத் தலைவர் இத்தகராறை அமைச்சரவைச் செயலாளரின் மத்தியஸ்தத்திற்கு அனுப்ப வேண்டும்", "The nomination automatically lapses after 6 months", "6 மாதங்களுக்குப் பிறகு அப்பரிந்துரை தானாகவே காலாவதியாகும்"),
         "A",
         "Under the Collegium guidelines established in Second Judges Case (1993) and Third Judges Case (1998), if the Collegium unanimously reiterates its recommendation after executive reconsideration, the appointment IS BINDING on the Government.",
         "இரண்டாவது மற்றும் மூன்றாவது நீதிபதிகள் வழக்குகளின் வழிகாட்டுதலின் படி, கொலீஜியம் தன் பரிந்துரையை மீண்டும் ஒருமனதாக வலியுறுத்தினால் (Reiterate), அரசு அந்த நியமனத்தைச் செய்வது கட்டாயமாகும் (Binding).",
         ("Reiterated Collegium recommendation IS BINDING on the Government.", "வலியுறுத்தப்பட்ட கொலீஜியம் பரிந்துரை அரசுக்குக் கட்டாயமானதாகும்.", "Government cannot permanently reject a reiterated name.", "வலியுறுத்தப்பட்ட பெயரை அரசு நிரந்தரமாக நிராகரிக்க முடியாது.", "Cabinet Secretary has no arbitration role.", "அமைச்சரவைச் செயலாளருக்கு மத்தியஸ்த அதிகாரம் இல்லை.", "No 6-month automatic lapse rule exists.", "6 மாத காலாவதி விதி எதுவுமில்லை."),
         "Assuming the Government has absolute veto power over judicial appointments even after Collegium reiteration.", "கொலீஜியம் மீண்டும் வலியுறுத்திய பிறகும் அரசுக்கு முழுமையான ரத்து அதிகாரம் (Veto) உண்டு என நினைப்பது.", "Reiterated Collegium Recommendation = BINDING on the Executive (Second & Third Judges Cases).", "மீண்டும் வலியுறுத்தப்பட்ட கொலீஜியம் பரிந்துரை = அரசுக்குக் கட்டாயமானதாகும்.", "3"),

        ("POLITY_SC_HARD_021", "Hard",
         "Under Article 130, can a High Court or State Government compel the Chief Justice of India to set up a permanent Bench of the Supreme Court in their state?",
         "உறுப்பு 130-ன் கீழ், தமது மாநிலத்தில் உச்ச நீதிமன்றத்தின் நிரந்தர அமர்வை அமைக்குமாறு உயர் நீதிமன்றமோ அல்லது மாநில அரசோ இந்தியத் தலைமை நீதிபதியைக் கட்டாயப்படுத்த முடியுமா?",
         ("Yes, if the State Assembly passes a resolution by 2/3rd majority", "ஆம், மாநில சட்டமன்றம் 2/3 பெரும்பான்மை தீர்மானம் நிறைவேற்றினால் கட்டாயப்படுத்தலாம்", "No, setting up SC benches outside Delhi under Article 130 is the EXCLUSIVE discretion of the CJI (with President's approval), and no mandamus can be issued to CJI for this", "இல்லை, உறுப்பு 130-ன் கீழ் டெல்லிக்கு வெளியே அமர்வு அமைப்பது CJI-ன் (குடியரசுத் தலைவர் ஒப்புதலுடன்) பிரத்யேக அதிகாரம்; இதற்கு CJI-க்கு மேண்டமஸ் பிறப்பிக்க முடியாது", "Yes, if recommended by the Governor", "ஆம், ஆளுநர் பரிந்துரைத்தால் கட்டாயப்படுத்தலாம்", "Yes, under Article 226 writ powers of High Court", "ஆம், உயர் நீதிமன்றத்தின் உறுப்பு 226 பேராணை அதிகாரத்தின் கீழ் கட்டாயப்படுத்தலாம்"),
         "B",
         "In *Union of India v. S.P. Anand (1998)*, the SC held that under Article 130, the CJI's power to appoint places other than Delhi as seat of SC is purely discretionary (with President's approval); no court can issue a writ of Mandamus to CJI to establish a bench.",
         "1998 எஸ்.பி. ஆனந்த் வழக்கில், உறுப்பு 130-ன் கீழ் டெல்லி தவிர பிற இடங்களில் அமர்வு அமைப்பது CJI-ன் தன்னிச்சை அதிகாரமாகும்; இதில் அமர்வு அமைக்கக் கோரி CJI-க்கு மேண்டமஸ் பிறப்பிக்க முடியாது எனக் கூறப்பட்டது.",
         ("State Assembly resolution cannot compel CJI.", "மாநில சட்டமன்றத் தீர்மானம் CJI-யைக் கட்டாயப்படுத்த முடியாது.", "Art 130 seat appointment is CJI's exclusive discretion (with President approval); no court can issue Mandamus to CJI.", "உறுப்பு 130 அமைவிடம் CJI-ன் பிரத்யேக அதிகாரம்; மேண்டமஸ் பிறப்பிக்க முடியாது.", "Governor recommendation cannot compel CJI.", "ஆளுநர் பரிந்துரை கட்டாயப்படுத்த முடியாது.", "HC cannot issue writ to CJI under Art 226 for SC bench.", "HC உறுப்பு 226-ன் கீழ் CJI-க்கு பேராணை பிறப்பிக்க முடியாது."),
         "Assuming High Courts or State Assemblies can mandate the creation of a Supreme Court bench in their region.", "மாநில சட்டமன்றங்களோ உயர் நீதிமன்றங்களோ SC அமர்வை உருவாக்க ஆணையிடலாம் என நினைப்பது.", "Article 130 Seat Allocation = Exclusive Discretion of CJI (with President's approval); Non-justiciable / No Mandamus.", "உறுப்பு 130 அமைவிடம் = CJI-ன் பிரத்யேக அதிகாரம் (குடியரசுத் தலைவர் ஒப்புதலுடன்); மேண்டமஸ் பிறப்பிக்க முடியாது.", "3"),

        ("POLITY_SC_HARD_022", "Hard",
         "Which Article of the Constitution empowers the Supreme Court to punish for contempt of itself, AND specifies that such power includes the power to punish for contempt of all courts subordinate to it?",
         "தன் அவமதிப்புக்கும் மற்றும் தன் கீழ்மை நீதிமன்றங்களின் அவமதிப்புக்கும் தண்டிக்கும் அதிகாரத்தை உச்ச நீதிமன்றத்திற்கு அளிக்கும் உறுப்பு எது?",
         ("Article 129", "உறுப்பு 129", "Article 215", "உறுப்பு 215", "Article 142", "உறுப்பு 142", "Article 144", "உறுப்பு 144"),
         "A",
         "Article 129 declares SC as a Court of Record with power to punish for contempt. In Delhi Judicial Service Association case (1991), SC held Art 129 includes power to punish for contempt of subordinate courts.",
         "உறுப்பு 129 உச்ச நீதிமன்றத்தைப் பதிவு நீதிமன்றமாக அறிவித்து அவமதிப்புத் தண்டனை அதிகாரம் அளிக்கிறது. 1991 வழக்கில் இது கீழ்மை நீதிமன்ற அவமதிப்புக்கும் பொருந்தும் என SC தீர்ப்பளித்தது.",
         ("Art 129 = Supreme Court Court of Record & Contempt power (including subordinate courts).", "உறுப்பு 129 = உச்ச நீதிமன்ற பதிவு நீதிமன்றம் & அவமதிப்பு அதிகாரம்.", "Art 215 is High Court Court of Record.", "உறுப்பு 215 உயர் நீதிமன்ற பதிவு நீதிமன்றம்.", "Art 142 is complete justice enforcement.", "உறுப்பு 142 முழுமையான நீதி.", "Art 144 is authorities acting in aid of SC.", "உறுப்பு 144 அதிகாரிகள் SC-க்கு உதவுவது."),
         "Confusing Article 129 (SC Contempt Power) with Article 215 (High Court Contempt Power).", "உறுப்பு 129 மற்றும் உறுப்பு 215 ஆகியவற்றை குழப்புவது.", "Supreme Court Court of Record = Article 129.", "உச்ச நீதிமன்ற பதிவு நீதிமன்றம் = உறுப்பு 129.", "3"),

        ("POLITY_SC_HARD_023", "Hard",
         "What is the rule regarding the suspension of Fundamental Rights and the availability of Article 32 writ remedy during a Proclamation of Emergency under Article 352?",
         "உறுப்பு 352 அவசரநிலையின் போது அடிப்படை உரிமைகள் இடைநீக்கம் மற்றும் உறுப்பு 32 பேராணை நிவாரணத்தின் நிலை என்ன?",
         ("All Fundamental Rights including Articles 20 and 21 are automatically suspended under Article 358", "உறுப்புகள் 20 மற்றும் 21 உட்பட அனைத்து அடிப்படை உரிமைகளும் உறுப்பு 358-ன் கீழ் தானாகவே இடைநீக்கம் செய்யப்படும்", "Article 32 writ remedy for enforcement of Articles 20 and 21 CANNOT be suspended even during Emergency (44th Amendment Act 1978)", "உறுப்புகள் 20 மற்றும் 21-ஐ அமல்படுத்தும் உறுப்பு 32 பேராணை நிவாரணம் அவசரநிலையிலும் இடைநீக்கம் செய்யப்பட முடியாது (44-வது திருத்தம் 1978)", "Article 32 remedy is permanently abolished during Emergency", "அவசரநிலையின் போது உறுப்பு 32 நிவாரணம் நிரந்தரமாக ரத்து செய்யப்படும்", "Only High Court writ remedy under Art 226 remains, while Art 32 is cancelled", "உறுப்பு 226 மட்டுமே இருக்கும், உறுப்பு 32 ரத்து செய்யப்படும்"),
         "B",
         "By virtue of the 44th Constitutional Amendment Act 1978, the President's order under Article 359 CANNOT suspend the right to move any court for enforcement of Articles 20 and 21. Thus, Art 32 for Arts 20 & 21 remains active.",
         "44-வது திருத்தச் சட்டம் 1978-ன் மூலம், உறுப்பு 359-ன் கீழ் குடியரசுத் தலைவரின் ஆணை உறுப்புகள் 20 மற்றும் 21-ஐ அமல்படுத்தும் உரிமையை இடைநீக்கம் செய்ய முடியாது; எனவே உறுப்பு 32 நிவாரணம் தொடரும்.",
         ("Art 20 and 21 CANNOT be suspended under Art 359 post-44th Amendment 1978.", "44-வது திருத்தத்திற்கு பின் உறுப்புகள் 20 மற்றும் 21 இடைநீக்கம் செய்யப்பட முடியாது.", "Art 32 remedy for Arts 20 and 21 CANNOT be suspended by Presidential order under Art 359.", "உறுப்புகள் 20 & 21-க்கான உறுப்பு 32 நிவாரணத்தைக் குடியரசுத் தலைவர் இடைநீக்கம் செய்ய முடியாது.", "Permanent abolition is incorrect.", "நிரந்தர ரத்து என்பது தவறு.", "Art 32 is not cancelled during emergency for Arts 20 & 21.", "உறுப்பு 32 ரத்து செய்யப்படுவதில்லை."),
         "Thinking ADM Jabalpur (1976) habeas corpus suspension rule still applies today (overruled by 44th Amendment 1978 & KS Puttaswamy 2017).", "ADM ஜபல்பூர் (1976) வழக்கு விதி இன்றும் பொருந்தும் என நினைப்பது (44-வது திருத்தம் மூலம் அது மாற்றப்பட்டது).", "Emergency FR Protection = Articles 20 & 21 CANNOT be suspended -> Article 32 writ remedy for Arts 20 & 21 remains intact.", "அவசரநிலை FR பாதுகாப்பு = உறுப்புகள் 20 & 21 இடைநீக்கம் செய்யப்பட முடியாது -> உறுப்பு 32 நிவாரணம் நீடிக்கும்.", "3"),

        ("POLITY_SC_HARD_024", "Hard",
         "Under Article 133(1), what certificate must be granted by the High Court for a civil appeal to lie to the Supreme Court?",
         "உறுப்பு 133(1)-ன் படி, சிவில் வழக்கில் உச்ச நீதிமன்ற மேல்முறையீட்டிற்கு உயர் நீதிமன்றம் எந்தச் சான்றிதழை வழங்க வேண்டும்?",
         ("That the case involves a substantial question of law of general importance AND in the opinion of the HC the said question needs to be decided by the SC", "வழக்கில் பொது முக்கியத்துவம் வாய்ந்த ஒரு முக்கிய சட்டக் கேள்வி அடங்கியுள்ளது மற்றும் அக்கேள்வி SC-ஆல் தீர்மானிக்கப்பட வேண்டும் என HC கருதுகிறது", "That the property value involved exceeds Rs. 10 Lakhs", "வழக்கின் சொத்து மதிப்பு ரூ. 10 லட்சத்திற்கு மேல் உள்ளது என சான்றளித்தல்", "That the defendant is a foreigner", "எதிராளி ஒரு வெளிநாட்டவர் என சான்றளித்தல்", "That the Law Minister has approved the appeal", "சட்ட அமைச்சர் மேல்முறையீட்டிற்கு ஒப்புதல் அளித்துள்ளார் என சான்றளித்தல்"),
         "A",
         "The 30th Constitutional Amendment Act 1972 removed the monetary valuation test (Rs. 20,000) from Article 133. Now, civil appeal lies if HC certifies under Art 134A that: (1) case involves substantial question of law of general importance, AND (2) needs to be decided by SC.",
         "30-வது திருத்தச் சட்டம் (1972) பண மதிப்பு வரம்பை (ரூ. 20,000) நீக்கியது. இப்போது (1) பொது முக்கியத்துவம் வாய்ந்த சட்டக் கேள்வி உள்ளது மற்றும் (2) அது SC-ஆல் தீர்மானிக்கப்பட வேண்டும் என சான்றளித்தால் மட்டுமே மேல்முறையீடு செல்லும்.",
         ("Monetary limit was abolished by 30th Amendment 1972. Present test is: Substantial question of law of general importance + needs SC decision.", "பண மதிப்பு வரம்பு 30-வது திருத்தத்தால் நீக்கப்பட்டது. தற்போதைய தேர்வு: பொது முக்கியத்துவம் வாய்ந்த சட்டக் கேள்வி + SC தீர்மானிக்க வேண்டிய தேவை.", "Monetary value (Rs 10 Lakhs) is no longer a criterion after 30th Amendment 1972.", "பண மதிப்பு 1972-க்குப் பின் அளவுகோல் அல்ல.", "Foreigner status is irrelevant.", "வெளிநாட்டவர் நிலை தொடர்பற்றது.", "Law Minister approval is irrelevant.", "சட்ட அமைச்சர் ஒப்புதல் தொடர்பற்றது."),
         "Assuming civil appeals to Supreme Court are still governed by monetary valuation tests (e.g., Rs 20,000 or Rs 1 Lakh).", "சிவில் மேல்முறையீடுகளுக்கு இன்னும் பண மதிப்பு வரம்பு உள்ளது என நினைப்பது (30-வது திருத்தம் 1972 மூலம் பண வரம்பு நீக்கப்பட்டது).", "Article 133 Civil Appeal Test = Substantial Question of Law of General Importance + Needs SC Decision (30th Amendment 1972).", "உறுப்பு 133 சிவில் மேல்முறையீட்டு தேர்வு = பொது முக்கியத்துவம் வாய்ந்த சட்டக் கேள்வி + SC தீர்மானிக்க வேண்டிய தேவை.", "3"),

        ("POLITY_SC_HARD_025", "Hard",
         "What is the relationship between Article 141 (Binding Law) and the decisions of High Courts within their respective territorial jurisdictions?",
         "உறுப்பு 141 (கட்டாயச் சட்டம்) மற்றும் மாநில உயர் நீதிமன்றத் தீர்ப்புகளுக்கு இடையேயான தொடர்பு என்ன?",
         ("High Court decisions are binding on all subordinate courts within its state, but NOT binding on other High Courts", "உயர் நீதிமன்றத் தீர்ப்பு அம்மாநிலத்தில் உள்ள அனைத்து கீழ்மை நீதிமன்றங்களையும் கட்டுப்படுத்தும்; ஆனால் பிற உயர் நீதிமன்றங்களைக் கட்டுப்படுத்தாது", "High Court decisions bind the Supreme Court", "உயர் நீதிமன்றத் தீர்ப்புகள் உச்ச நீதிமன்றத்தைக் கட்டுப்படுத்தும்", "High Court decisions bind all other High Courts in India equally", "உயர் நீதிமன்றத் தீர்ப்பு இந்தியாவில் உள்ள அனைத்து உயர் நீதிமன்றங்களையும் சமமாகக் கட்டுப்படுத்தும்", "High Court decisions have no binding precedent value anywhere", "உயர் நீதிமன்றத் தீர்ப்புகளுக்கு எங்கும் முன்மாதிரி சட்டம் மதிப்பு இல்லை"),
         "A",
         "Under Art 141, ONLY Supreme Court decisions bind all courts in India. A High Court decision is binding on all subordinate courts within its state territory, but has only 'persuasive value' (not binding) for other High Courts.",
         "உறுப்பு 141-ன் படி SC தீர்ப்புகள் மட்டுமே இந்தியா முழுமைக்கும் கட்டுப்படுத்தும். ஒரு HC தீர்ப்பு அம்மாநில கீழ்மை நீதிமன்றங்களை மட்டுமே கட்டுப்படுத்தும்; பிற HC-களுக்கு அது வெறும் 'வலியுறுத்தல் மதிப்பு' (Persuasive Value) மட்டுமே கொண்டது.",
         ("HC decision binds subordinate courts within its state, but has persuasive value for other HCs.", "HC தீர்ப்பு அம்மாநில கீழ்மை நீதிமன்றங்களைக் கட்டுப்படுத்தும், பிற HC-களுக்கு வலியுறுத்தல் மதிப்பு மட்டுமே.", "HC cannot bind SC.", "HC, SC-யைக் கட்டுப்படுத்த முடியாது.", "HC does not bind another HC (only persuasive).", "ஒரு HC பிற HC-யைக் கட்டுப்படுத்தாது.", "HC judgments DO have precedent value within state territory.", "HC தீர்ப்புகளுக்கு மாநில எல்லைக்குள் முன்மாதிரி மதிப்பு உண்டு."),
         "Assuming a High Court decision has binding precedent value across the entire territory of India like a Supreme Court judgment.", "உயர் நீதிமன்றத் தீர்ப்பும் உச்ச நீதிமன்றத் தீர்ப்பு போல இந்தியா முழுமைக்கும் கட்டுப்படுத்தும் எனத் தவறாக நினைப்பது.", "Precedent Value: Supreme Court (Art 141) = Binds ALL Courts in India. High Court = Binds Subordinate Courts within STATE only.", "முன்மாதிரி மதிப்பு: உச்ச நீதிமன்றம் (உறுப்பு 141) = இந்தியாவில் உள்ள அனைத்து நீதிமன்றங்களையும் கட்டுப்படுத்தும். உயர் நீதிமன்றம் = மாநில கீழ்மை நீதிமன்றங்களை மட்டுமே கட்டுப்படுத்தும்.", "3"),

        ("POLITY_SC_HARD_026", "Hard",
         "Which Constitutional Amendment inserted Article 139A empowering the Supreme Court to transfer cases involving the same question of law from High Courts to itself?",
         "ஒரே மாதிரியான சட்டக் கேள்வி கொண்ட உயர் நீதிமன்ற வழக்குகளைத் தனக்கு மாற்றிக்கொள்ள SC-க்கு அதிகாரமளிக்கும் உறுப்பு 139A-ஐச் சேர்த்த அரசியலமைப்புத் திருத்தம் எது?",
         ("42nd Constitutional Amendment Act, 1976", "42-வது அரசியலமைப்புத் திருத்தச் சட்டம், 1976", "44th Constitutional Amendment Act, 1978", "44-வது அரசியலமைப்புத் திருத்தச் சட்டம், 1978", "24th Constitutional Amendment Act, 1971", "24-வது அரசியலமைப்புத் திருத்தச் சட்டம், 1971", "52nd Constitutional Amendment Act, 1985", "52-வது அரசியலமைப்புத் திருத்தச் சட்டம், 1985"),
         "A",
         "Article 139A was inserted by the 42nd Constitutional Amendment Act 1976 and further amended by the 44th Constitutional Amendment Act 1978 to enable SC to withdraw and transfer cases.",
         "உறுப்பு 139A 42-வது அரசியலமைப்புத் திருத்தச் சட்டம் 1976 மூலம் சேர்க்கப்பட்டு, 44-வது திருத்தச் சட்டம் 1978 மூலம் மேலும் திருத்தப்பட்டது.",
         ("42nd Amendment 1976 inserted Article 139A into the Constitution.", "42-வது திருத்தம் 1976 உறுப்பு 139A-ஐச் சேர்த்தது.", "44th Amendment modified provisions of Art 139A.", "44-வது திருத்தம் உறுப்பு 139A விதியை மாற்றியமைத்தது.", "24th Amendment dealt with Art 13 & 368.", "24-வது திருத்தம் உறுப்பு 13 & 368 பற்றியது.", "52nd Amendment introduced Anti-Defection Law.", "52-வது திருத்தம் கட்சித் தாவல் தடைச் சட்டம்."),
         "Confusing 42nd Amendment 1976 (inserted Art 139A) with 44th Amendment 1978.", "42-வது திருத்தம் 1976 (உறுப்பு 139A சேர்க்கப்பட்டது) மற்றும் 44-வது திருத்தத்தைக் குழப்புவது.", "Article 139A Insertion = 42nd Constitutional Amendment Act, 1976.", "உறுப்பு 139A சேர்க்கை = 42-வது அரசியலமைப்புத் திருத்தச் சட்டம், 1976.", "1"),

        ("POLITY_SC_HARD_027", "Hard",
         "Can Parliament pass a law conferring the power of Judicial Review of Parliamentary enactments exclusively on the Supreme Court while excluding High Courts?",
         "நாடாளுமன்றச் சட்டங்களின் நீதித்துறை சீராய்வு அதிகாரத்தை உச்ச நீதிமன்றத்திற்கு மட்டுமே வழங்கி, உயர் நீதிமன்றங்களை விலக்கி நாடாளுமன்றம் சட்டம் இயற்ற முடியுமா?",
         ("No, Judicial Review powers of both High Courts (Art 226/227) and Supreme Court (Art 32/136) form part of the Basic Structure", "இல்லை, உயர் நீதிமன்றங்களின் (உறுப்பு 226/227) மற்றும் உச்ச நீதிமன்றத்தின் (உறுப்பு 32/136) நீதித்துறை சீராய்வு அதிகாரங்கள் அடிப்படை அமைப்பின் பகுதியாகும்", "Yes, Parliament has absolute power under Article 368 to exclude High Courts", "ஆம், உயர் நீதிமன்றங்களை விலக்க நாடாளுமன்றத்திற்கு உறுப்பு 368-ன் கீழ் முழு அதிகாரம் உண்டு", "Yes, if approved by a 2/3rd majority of State Legislatures", "ஆம், 2/3 பங்கு மாநில சட்டமன்றங்கள் ஒப்புதல் அளித்தால் இயற்றலாம்", "Yes, during a Financial Emergency declared under Article 360", "ஆம், உறுப்பு 360 நிதி அவசரநிலையின் போது இயற்றலாம்"),
         "A",
         "In *L. Chandra Kumar v. Union of India (1997)*, the SC held that Judicial Review under Art 226/227 (High Courts) and Art 32 (Supreme Court) is an integral part of the Basic Structure and CANNOT be excluded by any constitutional amendment or law.",
         "1997 எல். சந்திரகுமார் வழக்கில், உறுப்பு 226/227 (HC) மற்றும் உறுப்பு 32 (SC) ஆகியவற்றுக்குட்பட்ட நீதித்துறை சீராய்வு அதிகாரம் அடிப்படை அமைப்பாகும்; எந்த அரசியலமைப்பு திருத்தத்தாலும் சட்டத்தாலும் அதை நீக்க முடியாது எனத் தீர்ப்பளிக்கப்பட்டது.",
         ("Judicial review powers of BOTH SC and HC are part of Basic Structure (L. Chandra Kumar 1997).", "SC மற்றும் HC ஆகிய இரண்டின் நீதித்துறை சீராய்வு அதிகாரங்களும் அடிப்படை அமைப்பாகும்.", "Parliament CANNOT exclude High Court judicial review.", "நாடாளுமன்றம் உயர் நீதிமன்ற சீராய்வை விலக்க முடியாது.", "State Legislature approval cannot alter Basic Structure.", "மாநில சட்டமன்ற ஒப்புதல் அடிப்படை அமைப்பை மாற்ற முடியாது.", "Financial Emergency does not affect Judicial Review Basic Structure.", "நிதி அவசரநிலை அடிப்படை அமைப்பைப் பாதிக்காது."),
         "Assuming Parliament can divest High Courts of Judicial Review powers over Central Acts (L. Chandra Kumar 1997 struck down such exclusions as unconstitutional).", "மத்திய சட்டங்கள் மீதான உயர் நீதிமன்ற சீராய்வு அதிகாரத்தை நாடாளுமன்றம் பறிக்க முடியும் என நினைப்பது.", "Judicial Review of HCs (Art 226/227) & SC (Art 32/136) = Inseverable part of BASIC STRUCTURE (L. Chandra Kumar 1997).", "HC & SC நீதித்துறை சீராய்வு அதிகாரம் = அடிப்படை அமைப்பின் பிரிக்க முடியாத பகுதி.", "1"),

        ("POLITY_SC_HARD_028", "Hard",
         "Under Article 124(2), what is the MAXIMUM age up to which a Supreme Court judge can hold office, and how is any dispute regarding a judge's age determined?",
         "உறுப்பு 124(2)-ன் படி உச்ச நீதிமன்ற நீதிபதியின் அதிகபட்ச வயது என்ன, வயது பற்றிய தகராறு எவ்வாறு தீர்மானிக்கப்படுகிறது?",
         ("65 years; age dispute is determined by such authority and in such manner as Parliament may by law provide", "65 வயது; வயது தகராறு நாடாளுமன்றம் சட்டத்தால் குறிப்பிடும் அதிகாரி மற்றும் முறையில் தீர்மானிக்கப்படும்", "62 years; determined by Chief Justice of India", "62 வயது; இந்தியத் தலைமை நீதிபதியால் தீர்மானிக்கப்படும்", "65 years; determined by Union Home Ministry independently", "65 வயது; ஒன்றிய உள்துறை அமைச்சகத்தால் தன்னிச்சையாகத் தீர்மானிக்கப்படும்", "70 years; determined by UPSC Chairman", "70 வயது; UPSC தலைவரால் தீர்மானிக்கப்படும்"),
         "A",
         "Under Article 124(2A) (inserted by 15th Amendment Act 1963), the age of a Judge of the Supreme Court shall be determined by such authority and in such manner as Parliament may by law provide. Retirement age is 65 years.",
         "15-வது திருத்தச் சட்டம் 1963 மூலம் சேர்க்கப்பட்ட உறுப்பு 124(2A)-ன் படி, உச்ச நீதிமன்ற நீதிபதியின் வயது நாடாளுமன்ற சட்டத்தால் குறிப்பிடும் அதிகாரி மற்றும் முறையில் தீர்மானிக்கப்படும். ஓய்வு வயது 65.",
         ("65 years retirement + Age dispute decided by Parliamentary law authority under Art 124(2A).", "65 வயது ஓய்வு + வயது தகராறு நாடாளுமன்ற சட்ட அதிகாரி மூலம் தீர்மானிக்கப்படும்.", "62 years is for High Court judges.", "62 வயது உயர் நீதிமன்ற நீதிபதிகளுக்கு.", "Home Ministry cannot independently decide judge age.", "உள்துறை அமைச்சகம் தன்னிச்சையாகத் தீர்மானிக்க முடியாது.", "70 years / UPSC Chairman is incorrect.", "70 வயது / UPSC தலைவர் என்பது தவறு."),
         "Confusing age determination of SC Judge (Art 124(2A) - Authority prescribed by Parliament law) with HC Judge age determination (Art 217(3) - President in consultation with CJI).", "உச்ச நீதிமன்ற நீதிபதி வயது நிர்ணயம் (நாடாளுமன்றச் சட்ட அதிகாரி) மற்றும் உயர் நீதிமன்ற நீதிபதி வயது நிர்ணயத்தைக் (குடியரசுத் தலைவர் + CJI) குழப்புவது.", "SC Judge Age Dispute = Determined by Authority prescribed by PARLIAMENT BY LAW (Article 124(2A)).", "SC நீதிபதி வயது தகராறு = நாடாளுமன்ற சட்டத்தால் குறிப்பிடப்படும் அதிகாரியால் தீர்மானிக்கப்படும் (உறுப்பு 124(2A)).", "1"),

        ("POLITY_SC_HARD_029", "Hard",
         "In which landmark judgment did the Supreme Court hold that the power of Judicial Review under Article 32 and Article 226 extends even to ORDERS OF THE SPEAKER under the Tenth Schedule (Anti-Defection Law)?",
         "பத்தாவது அட்டவணையின் (கட்சித் தாவல் தடைச் சட்டம்) கீழ் சபாநாயகர் பிறப்பிக்கும் உத்தரவுகளுக்கும் உறுப்பு 32 & 226-ன் கீழ் நீதித்துறை சீராய்வு பொருந்தும் எனத் தீர்ப்பளிக்கப்பட்ட வழக்கு எது?",
         ("Kihoto Hollohan v. Zachillhu (1992)", "கிகோட்டோ ஹோல்லோஹான் vs ஜாச்சிலு (1992)", "Indira Nehru Gandhi v. Raj Narain (1975)", "இந்திரா நேரு காந்தி vs ராஜ் நரேன் (1975)", "Raja Ram Pal v. Hon'ble Speaker (2007)", "ராஜா ராம் பால் vs சபாநாயகர் (2007)", "SR Bommai v. Union of India (1994)", "எஸ்.ஆர். பொம்மை vs இந்திய ஒன்றியம் (1994)"),
         "A",
         "In *Kihoto Hollohan (1992)*, a 5-judge Constitution Bench held that the Speaker acting under the Tenth Schedule functions as a Tribunal, and his decisions are subject to Judicial Review under Art 32, 226, and 136.",
         "1992 கிகோட்டோ ஹோல்லோஹான் வழக்கில், பத்தாவது அட்டவணையின் கீழ் செயல்படும் சபாநாயகர் ஒரு தீர்ப்பாயமாகவே (Tribunal) செயல்படுகிறார்; எனவே அவரது முடிவுகள் உறுப்பு 32, 226 & 136-ன் கீழ் நீதித்துறை சீராய்வுக்கு உட்பட்டவை எனத் தீர்ப்பளிக்கப்பட்டது.",
         ("Kihoto Hollohan (1992) held Speaker decisions under Anti-Defection Law subject to Judicial Review.", "கிகோட்டோ ஹோல்லோஹான் (1992) கட்சித் தாவல் சபாநாயகர் முடிவுகள் நீதித்துறை சீராய்வுக்கு உட்பட்டவை என்றது.", "Indira Gandhi Case 1975 invalidated 39th Amendment.", "இந்திரா காந்தி வழக்கு 39-வது திருத்தத்தை ரத்து செய்தது.", "Raja Ram Pal 2007 dealt with cash-for-query MP expulsion.", "ராஜா ராம் பால் வழக்கு எம்.பி பதவி நீக்கம் பற்றியது.", "SR Bommai 1994 dealt with Art 356 President Rule judicial review.", "எஸ்.ஆர். பொம்மை வழக்கு உறுப்பு 356 பற்றியது."),
         "Assuming Speaker decisions under Tenth Schedule (Anti-Defection Law) are immune from judicial review (Paragraph 7 of Tenth Schedule excluding judicial review was struck down in Kihoto Hollohan).", "கட்சித் தாவலில் சபாநாயகர் முடிவை நீதிமன்றத்தில் சவால் செய்ய முடியாது என நினைப்பது.", "Anti-Defection Speaker Decisions = Subject to Judicial Review (Kihoto Hollohan Case 1992).", "கட்சித் தாவல் சபாநாயகர் முடிவுகள் = நீதித்துறை சீராய்வுக்கு உட்பட்டவை (கிகோட்டோ ஹோல்லோஹான் வழக்கு 1992).", "1"),

        ("POLITY_SC_HARD_030", "Hard",
         "Under Article 142, can the Supreme Court issue orders that directly CONTRADICT or IGNORE express statutory provisions passed by Parliament?",
         "உறுப்பு 142-ன் கீழ் முழுமையான நீதி வழங்க, நாடாளுமன்றம் இயற்றிய தெளிவான சட்ட விதிகளை உச்ச நீதிமன்றம் நேரடியாக மீறியோ புறக்கணித்தோ உத்தரவிட முடியுமா?",
         ("No, Article 142 powers cannot be exercised to bypass express statutory prohibition (Supreme Court Bar Association v. Union of India, 1998)", "இல்லை, நாடாளுமன்றத்தின் தெளிவான சட்டப்பூர்வத் தடையை மீறும் வகையில் உறுப்பு 142 அதிகாரத்தைப் பயன்படுத்த முடியாது (1998 வழக்கு)", "Yes, Article 142 completely overrides all statutory laws passed by Parliament", "ஆம், உறுப்பு 142 நாடாளுமன்றத்தின் அனைத்து சட்டங்களையும் முற்றிலும் மேலெழுகிறது", "Yes, provided the Prime Minister approves the order", "ஆம், பிரதமர் அவ்வுத்தரவுக்கு ஒப்புதல் அளித்தால் செய்யலாம்", "No, because Article 142 applies only to administrative staff appointments", "இல்லை, ஏனெனில் உறுப்பு 142 நிர்வாக ஊழியர்கள் நியமனத்திற்கு மட்டுமே பொருந்தும்"),
         "A",
         "In *Supreme Court Bar Association v. UOI (1998)*, a Constitution Bench held that Art 142 is a curative power, but cannot be used to ignore or supplant express statutory provisions or create a new enforceable right contrary to law.",
         "1998 Supreme Court Bar Association வழக்கில், உறுப்பு 142 என்பது நீதிக்கான அதிகாரமாகும்; ஆனால் தெளிவான சட்டப்பூர்வ தடையை மீறவோ அல்லது சட்டத்திற்கு எதிரான புதிய உரிமையை உருவாக்கவோ அதைப் பயன்படுத்த முடியாது எனத் தீர்ப்பளிக்கப்பட்டது.",
         ("Art 142 cannot supplant express statutory law (SC Bar Association Case 1998).", "உறுப்பு 142 சட்டப்பூர்வ தடையை மீற முடியாது (1998 வழக்கு).", "Art 142 does NOT give unlimited power to violate statutory laws.", "உறுப்பு 142 சட்டங்களை மீற வரம்பற்ற அதிகாரம் அளிக்காது.", "PM approval is irrelevant.", "பிரதமர் ஒப்புதல் தொடர்பற்றது.", "Art 142 is not restricted to staff appointments.", "உறுப்பு 142 ஊழியர் நியமனத்திற்கு மட்டுமே உரியதல்ல."),
         "Assuming Article 142 gives the Supreme Court absolute, unlimited power to override all parliamentary statutes (Art 142 is supplementary to law, not superior to statutory prohibitions).", "உறுப்பு 142 அனைத்து நாடாளுமன்றச் சட்டங்களையும் மீற வரம்பற்ற அதிகாரமளிக்கிறது எனத் தவறாக நினைப்பது.", "Article 142 Limitation = Cannot bypass or supplant express statutory prohibitions (SC Bar Association 1998).", "உறுப்பு 142 வரம்பு = தெளிவான சட்டப் பூர்வத் தடைகளை மீறவோ புறக்கணிக்கவோ முடியாது.", "1"),

        ("POLITY_SC_HARD_031", "Hard",
         "Which Article of the Constitution confers power on the Supreme Court to review its own judgment or order?",
         "உச்ச நீதிமன்றம் தனது சொந்தத் தீர்ப்பு அல்லது உத்தரவைச் சீராய்வு செய்யும் அதிகாரத்தை வழங்கும் உறுப்பு எது?",
         ("Article 136", "உறுப்பு 136", "Article 137", "உறுப்பு 137", "Article 138", "உறுப்பு 138", "Article 139", "உறுப்பு 139"),
         "B",
         "Article 137 grants the Supreme Court the power to review any judgment pronounced or order made by it.",
         "அரசியலமைப்பு உறுப்பு 137 உச்ச நீதிமன்றம் தன் சொந்தத் தீர்ப்பு அல்லது உத்தரவைச் சீராய்வு செய்யும் அதிகாரத்தை அளிக்கிறது.",
         ("Art 136 is Special Leave Petition.", "உறுப்பு 136 சிறப்பு விடுப்பு மனு.", "Art 137 = Review of judgments or orders by Supreme Court.", "உறுப்பு 137 = உச்ச நீதிமன்ற தீர்ப்புச் சீராய்வு.", "Art 138 is enlargement of SC jurisdiction.", "உறுப்பு 138 அதிகார வரம்பு விரிவாக்கம்.", "Art 139 is writ power enlargement.", "உறுப்பு 139 பேராணை அதிகார விரிவாக்கம்."),
         "Confusing Article 137 (Review of SC judgments) with Article 136 (Special Leave Petition).", "உறுப்பு 137 மற்றும் உறுப்பு 136 ஆகியவற்றை குழப்புவது.", "Review Power of Supreme Court = Article 137.", "உச்ச நீதிமன்ற சீராய்வு அதிகாரம் = உறுப்பு 137.", "2"),

        ("POLITY_SC_HARD_032", "Hard",
         "What is the Constitutional requirement for a judge of the Supreme Court regarding Oath or Affirmation under Third Schedule?",
         "3-வது அட்டவணையின் கீழ் உச்ச நீதிமன்ற நீதிபதிக்கான பதவிப் பிரமாணத்தின் அரசியலமைப்புத் தேவை என்ன?",
         ("To uphold the sovereignty and integrity of India and perform duties without fear or favor", "இந்தியாவின் இறையாண்மை மற்றும் ஒருமைப்பாட்டை உயர்த்திப் பிடிக்கவும், பயமும் தயவுமின்றிப் பணியாற்றவும் பிரமாணம் எடுத்தல்", "To obey all orders of the Union Cabinet Law Minister", "ஒன்றிய அமைச்சரவை சட்ட அமைச்சரின் அனைத்து உத்தரவுகளுக்கும் கீழ்ப்படிதல்", "To ensure State Governments obey Union laws exclusively", "மாநில அரசுகள் ஒன்றிய சட்டங்களுக்குக் கீழ்ப்படிவதை உறுதி செய்தல்", "To complete 10 years of service minimum", "குறைந்தது 10 ஆண்டுகள் பணியாற்றுவதை உறுதி செய்தல்"),
         "A",
         "Form IV in the Third Schedule prescribes the Oath/Affirmation for SC Judges: To bear true faith and allegiance to the Constitution, uphold sovereignty and integrity of India, and perform duties without fear or favor, affection or ill-will.",
         "3-வது அட்டவணையின் படி, SC நீதிபதிகள் அரசியலமைப்பிற்கு உண்மையாகவும், இந்தியாவின் இறையாண்மை மற்றும் ஒருமைப்பாட்டை உயர்த்திப் பிடிப்பதற்கும், அச்சமும் தயவுமின்றிப் பணியாற்றுவதற்கும் பிரமாணம் ஏற்கின்றனர்.",
         ("Form IV of Third Schedule prescribes oath to uphold sovereignty/integrity of India and act without fear or favor.", "3-வது அட்டவணை படி IV இறையாண்மையைப் பாதுகாக்கவும் அச்சமின்றிப் பணியாற்றவும் பிரமாணம் அளிக்கிறது.", "Law Minister obedience is not part of judicial oath.", "சட்ட அமைச்சருக்குக் கீழ்ப்படிதல் பிரமாணத்தில் இல்லை.", "State government monitoring is not judicial oath wording.", "மாநில அரசு கண்காணிப்பு பிரமாணத்தில் இல்லை.", "Service completion is not an oath requirement.", "பணி நிறைவு பிரமாணத்தில் இல்லை."),
         "Confusing Judicial Oath (Third Schedule Form IV - Uphold Constitution & Sovereignty/Integrity) with Executive Oath.", "நீதித்துறை பிரமாணம் மற்றும் நிர்வாகப் பிரமாணத்தைக் குழப்புவது.", "Supreme Court Judge Oath = Third Schedule Form IV (Uphold Sovereignty & Integrity of India).", "SC நீதிபதி பிரமாணம் = 3-வது அட்டவணை படி IV (இறையாண்மை மற்றும் ஒருமைப்பாட்டை உயர்த்திப்பிடித்தல்).", "1"),

        ("POLITY_SC_HARD_033", "Hard",
         "Which Article of the Constitution specifies that the Law declared by the Supreme Court shall be binding on all courts within the territory of India?",
         "உச்ச நீதிமன்றத்தால் அறிவிக்கப்படும் சட்டம் இந்தியாவில் உள்ள அனைத்து நீதிமன்றங்களையும் கட்டுப்படுத்தும் எனக் கூறும் உறுப்பு எது?",
         ("Article 140", "உறுப்பு 140", "Article 141", "உறுப்பு 141", "Article 142", "உறுப்பு 142", "Article 143", "உறுப்பு 143"),
         "B",
         "Article 141 embeds the doctrine of Stare Decisis into the Constitution, binding all courts within India to the law declared by the SC.",
         "அரசியலமைப்பு உறுப்பு 141 Stare Decisis கோட்பாட்டை பொறித்து, உச்ச நீதிமன்ற சட்டம் இந்தியாவில் உள்ள அனைத்து நீதிமன்றங்களையும் கட்டுப்படுத்தும் எனக் கூறுகிறது.",
         ("Art 140 is ancillary powers.", "உறுப்பு 140 துணை அதிகாரங்கள்.", "Art 141 = Law declared by Supreme Court binding on all courts in India.", "உறுப்பு 141 = SC சட்டம் இந்தியாவில் உள்ள அனைத்து நீதிமன்றங்களையும் கட்டுப்படுத்தும்.", "Art 142 is complete justice.", "உறுப்பு 142 முழுமையான நீதி.", "Art 143 is advisory jurisdiction.", "உறுப்பு 143 ஆலோசனை ஆதிக்கம்."),
         "Confusing Article 141 (Binding precedent) with Article 142 (Complete justice enforcement).", "உறுப்பு 141 மற்றும் உறுப்பு 142-ஐக் குழப்புவது.", "Law Declared by SC Binding = Article 141.", "SC சட்டம் அனைவரையும் கட்டுப்படுத்தும் = உறுப்பு 141.", "2"),

        ("POLITY_SC_HARD_034", "Hard",
         "What is the status of an opinion rendered by the Supreme Court under Article 143 Advisory Jurisdiction?",
         "உறுப்பு 143 ஆலோசனை ஆதிக்கத்தின் கீழ் உச்ச நீதிமன்றம் அளிக்கும் கருத்தின் நிலை என்ன?",
         ("It is advisory only, not binding on the President, and does not carry the force of a decree under Article 142", "இது வெறும் ஆலோசனையே, குடியரசுத் தலைவரைக் கட்டுப்படுத்தாது, உறுப்பு 142 ஆணையின் சக்தியைக் கொண்டிருக்காது", "It is a binding decree on all States under Article 141", "இது உறுப்பு 141-ன் கீழ் அனைத்து மாநிலங்களையும் கட்டுப்படுத்தும் ஆணையாகும்", "It automatically amends the Constitution", "இது அரசியலமைப்பைத் தானாகவே திருத்திவிடும்", "It requires 2/3rd ratification by State Assemblies to be valid", "இது செல்லுபடியாக 2/3 பங்கு மாநில சட்டமன்றங்களின் ஒப்புதல் தேவை"),
         "A",
         "An advisory opinion under Article 143 is not a decision or decree, but a non-binding opinion tendered to the President. While it carries high persuasive value, it is not binding on the President nor is it a law under Art 141.",
         "உறுப்பு 143-ன் கீழ் வழங்கப்பட்ட ஆலோசனை தீர்ப்பு அல்ல; அது குடியரசுத் தலைவருக்கு அளிக்கப்படும் கட்டாயமற்ற கருத்தாகும். அது உறுப்பு 141-ன் கீழ் கட்டாயச் சட்டமாகாது.",
         ("Advisory opinion under Art 143 is NOT binding on President and is not a judicial decree.", "உறுப்பு 143 ஆலோசனை குடியரசுத் தலைவரைக் கட்டுப்படுத்தாது, தீர்ப்பும் அல்ல.", "It is NOT a binding decree under Art 141.", "இது உறுப்பு 141-ன் கீழ் கட்டாய தீர்ப்பு அல்ல.", "It cannot amend the Constitution.", "இது அரசியலமைப்பை திருத்த முடியாது.", "State Assembly ratification is irrelevant.", "மாநில சட்டமன்ற ஒப்புதல் தொடர்பற்றது."),
         "Confusing Advisory Opinion (Art 143 - Non-binding) with Judicial Judgment (Art 141 - Binding on all courts).", "ஆலோசனை கருத்து (கட்டாயமற்றது) மற்றும் நீதிமன்றத் தீர்ப்பைக் (கட்டாயமானது) குழப்புவது.", "Article 143 Advisory Opinion = Purely Advisory, Non-binding on President, Non-executory.", "உறுப்பு 143 ஆலோசனை = வெறும் ஆலோசனையே, குடியரசுத் தலைவரைக் கட்டுப்படுத்தாது.", "1"),

        ("POLITY_SC_HARD_035", "Hard",
         "Under Article 124(6), who administers the oath of office to a newly appointed Judge of the Supreme Court?",
         "உறுப்பு 124(6)-ன் படி புதிதாக நியமிக்கப்பட்ட உச்ச நீதிமன்ற நீதிபதிக்கு பதவிப் பிரமாணம் செய்து வைப்பவர் யார்?",
         ("President of India or some person appointed in that behalf by him", "இந்தியக் குடியரசுத் தலைவர் அல்லது அவரால் நியமிக்கப்பட்ட நபர்", "Chief Justice of India independently without Presidential authorization", "குடியரசுத் தலைவர் அனுமதியின்றி தன்னிச்சையாக தலைமை நீதிபதி", "Union Law Minister", "ஒன்றிய சட்ட அமைச்சர்", "Speaker of Lok Sabha", "மக்களவைத் தலைவர்"),
         "A",
         "Article 124(6) specifies that every person appointed as a Judge of the Supreme Court shall, before he enters upon his office, make and subscribe before the President, or some person appointed in that behalf by him, an oath or affirmation.",
         "உறுப்பு 124(6)-ன் படி, உச்ச நீதிமன்ற நீதிபதியாக நியமிக்கப்படுபவர் குடியரசுத் தலைவர் அல்லது அவரால் நியமிக்கப்பட்ட நபர் முன்னிலையில் பதவிப் பிரமாணம் பெற வேண்டும்.",
         ("President or his authorized designee administers oath under Art 124(6).", "குடியரசுத் தலைவர் அல்லது அவரால் அதிகாரமளிக்கப்பட்ட நபர் பிரமாணம் செய்து வைப்பார்.", "CJI can administer ONLY IF appointed in that behalf by President.", "குடியரசுத் தலைவர் நியமித்தால் மட்டுமே CJI செய்து வைப்பார்.", "Law Minister has no constitutional role in oath.", "சட்ட அமைச்சருக்குப் பங்கில்லை.", "Speaker has no role in judicial oath.", "சபாநாயகருக்குப் பங்கில்லை."),
         "Assuming Chief Justice of India independently administers oath without Presidential authority.", "தலைமை நீதிபதியே தன்னிச்சையாகப் பிரமாணம் செய்து வைப்பார் என நினைப்பது.", "SC Judge Oath Administration = President of India OR Person appointed by him (Article 124(6)).", "SC நீதிபதி பிரமாணம் = குடியரசுத் தலைவர் அல்லது அவரால் நியமிக்கப்பட்ட நபர் (உறுப்பு 124(6)).", "1"),

        ("POLITY_SC_HARD_036", "Hard",
         "What is the effect of Article 124(7) on a retired Supreme Court judge?",
         "ஓய்வு பெற்ற உச்ச நீதிமன்ற நீதிபதி மீது உறுப்பு 124(7) விதிக்கும் விளைவு என்ன?",
         ("Complete bar from pleading or acting in ANY court or before ANY authority within the territory of India", "இந்தியாவில் உள்ள எந்தவொரு நீதிமன்றத்திலும் அல்லது அதிகார அமைப்பின் முன்னும் வழக்காடவோ பணியாற்றவோ முழுமையான தடை", "Bar from practicing only in Supreme Court, but allowed in High Courts", "உச்ச நீதிமன்றத்தில் மட்டும் தடை, உயர் நீதிமன்றங்களில் பணியாற்றலாம்", "Allowed to practice if Union Law Ministry grants permission", "சட்ட அமைச்சகம் அனுமதித்தால் பணியாற்றலாம்", "Allowed to practice only in criminal matters", "குற்றவியல் வழக்குகளில் மட்டுமே பணியாற்றலாம்"),
         "A",
         "Article 124(7) lays down a total prohibition: 'No person who has held office as a Judge of the Supreme Court shall plead or act in any court or before any authority within the territory of India.'",
         "உறுப்பு 124(7) முழுமையான தடையை விதிக்கிறது: உச்ச நீதிமன்ற நீதிபதியாகப் பணியாற்றிய ஒருவர் இந்தியாவில் உள்ள எந்தவொரு நீதிமன்றத்திலும் அல்லது அதிகார அமைப்பின் முன்னும் வழக்காடவோ பணியாற்றவோ முடியாது.",
         ("Article 124(7) imposes a COMPLETE BAR on pleading or acting in ANY court or before ANY authority in India.", "உறுப்பு 124(7) இந்தியாவில் உள்ள அனைத்து நீதிமன்றங்கள் மற்றும் அதிகார அமைப்புகளில் பணியாற்ற முழுத் தடை விதிக்கிறது.", "High Court practice is ALSO barred for retired SC judges.", "உயர் நீதிமன்றப் பணியும் தடை செய்யப்பட்டுள்ளது.", "Law Ministry permission cannot override Art 124(7).", "சட்ட அமைச்சக அனுமதி இதை மாற்ற முடியாது.", "Criminal practice is strictly barred.", "குற்றவியல் பணியும் தடை செய்யப்பட்டுள்ளது."),
         "Confusing High Court retired judges (can practice in SC & other HCs) with SC retired judges (barred from ALL courts).", "உயர் நீதிமன்ற ஓய்வு பெற்ற நீதிபதி விதிகள் மற்றும் உச்ச நீதிமன்ற நீதிபதி விதிகளைக் குழப்புவது.", "Retired SC Judge Practice = BARRED FROM ALL COURTS & AUTHORITIES IN INDIA (Article 124(7)).", "ஓய்வு பெற்ற SC நீதிபதி தொழில் = இந்தியாவில் உள்ள அனைத்து நீதிமன்றங்களிலும் பணியாற்ற முழுத் தடை.", "1"),

        ("POLITY_SC_HARD_037", "Hard",
         "Which Article of the Constitution empowers the Supreme Court to pass any decree or order necessary for doing COMPLETE JUSTICE in any cause or matter pending before it?",
         "தனக்கு முன் நிலுவையில் உள்ள எந்தவொரு வழக்கிலும் 'முழுமையான நீதி' (Complete Justice) வழங்கத் தேவையான ஆணையைப் பிறப்பிக்க SC-க்கு அதிகாரமளிக்கும் உறுப்பு எது?",
         ("Article 140", "உறுப்பு 140", "Article 141", "உறுப்பு 141", "Article 142", "உறுப்பு 142", "Article 143", "உறுப்பு 143"),
         "C",
         "Article 142(1) states that the Supreme Court in the exercise of its jurisdiction may pass such decree or make such order as is necessary for doing complete justice in any cause or matter pending before it.",
         "உறுப்பு 142(1) தனக்கு முன் நிலுவையில் உள்ள வழக்கில் 'முழுமையான நீதி' வழங்கத் தேவையான எந்தவொரு ஆணை அல்லது உத்தரவையும் பிறப்பிக்க SC-க்கு அதிகாரமளிக்கிறது.",
         ("Art 140 is ancillary powers.", "உறுப்பு 140 துணை அதிகாரங்கள்.", "Art 141 is binding precedent.", "உறுப்பு 141 கட்டாய முன்மாதிரி சட்டம்.", "Art 142 = Decree / Order for COMPLETE JUSTICE.", "உறுப்பு 142 = முழுமையான நீதிக்கான ஆணை / உத்தரவு.", "Art 143 is advisory jurisdiction.", "உறுப்பு 143 ஆலோசனை ஆதிக்கம்."),
         "Confusing Article 142 (Complete Justice) with Article 141 (Binding Precedent).", "உறுப்பு 142 மற்றும் உறுப்பு 141 ஆகியவற்றை குழப்புவது.", "Complete Justice Power = Article 142.", "முழுமையான நீதி அதிகாரம் = உறுப்பு 142.", "3"),

        ("POLITY_SC_HARD_038", "Hard",
         "Under Article 146(3), how are the administrative expenses of the Supreme Court funded?",
         "உறுப்பு 146(3)-ன் படி உச்ச நீதிமன்றத்தின் நிர்வாகச் செலவுகளுக்கு எவ்வாறு நிதி வழங்கப்படுகிறது?",
         ("Charged upon the Consolidated Fund of India", "இந்தியத் தொகுப்பு நிதியில் சுமத்தப்படுகிறது (Charged)", "Voted annually by Lok Sabha as a Demand for Grants", "மக்களவையால் ஆண்டுதோறும் மானியக் கோரிக்கையாக வாக்களிக்கப்படுகிறது", "Funded out of the Contingency Fund of India", "இந்திய அவசரகால நிதியிலிருந்து வழங்கப்படுகிறது", "Funded by State Governments proportionally", "மாநில அரசுகளால் விகிதாச்சாரப்படி நிதி வழங்கப்படுகிறது"),
         "A",
         "Article 146(3) mandates that administrative expenses of the Supreme Court, including all salaries, allowances and pensions payable to judges/staff, shall be CHARGED UPON the Consolidated Fund of India (non-votable by Parliament).",
         "உறுப்பு 146(3)-ன் படி உச்ச நீதிமன்ற நிர்வாகச் செலவுகள், நீதிபதிகள்/ஊழியர்கள் ஊதியம் மற்றும் ஓய்வூதியம் உட்பட இந்தியத் தொகுப்பு நிதியில் சுமத்தப்படுகின்றன (நாடாளுமன்ற வாக்கெடுப்புக்கு அப்பாற்பட்டது).",
         ("SC administrative expenses are CHARGED upon Consolidated Fund of India (non-votable).", "SC நிர்வாகச் செலவுகள் இந்தியத் தொகுப்பு நிதியில் சுமத்தப்படுபவை (வாக்கெடுப்பு இல்லை).", "Voted by Lok Sabha is incorrect (charged items are not voted upon).", "மக்களவையால் வாக்களிக்கப்படுவது என்பது தவறு.", "Contingency Fund is for unforeseen emergencies only.", "அவசரகால நிதி அவசரச் செலவுகளுக்கு மட்டுமே.", "State Governments do not fund SC administrative expenses.", "மாநில அரசுகள் SC-க்கு நிதி அளிப்பதில்லை."),
         "Confusing 'Charged upon Consolidated Fund' (non-votable) with 'Made from Consolidated Fund' (votable demands for grants).", "தொகுப்பு நிதியில் 'சுமத்தப்படுபவை' (வாக்கெடுப்பில்லாதவை) மற்றும் 'வாக்களிக்கப்படுபவை' ஆகியவற்றை குழப்புவது.", "SC Expenses & Salaries = CHARGED upon Consolidated Fund of India (Article 146(3)).", "SC செலவுகள் & ஊதியம் = இந்தியத் தொகுப்பு நிதியில் சுமத்தப்படுபவை (உறுப்பு 146(3)).", "1"),

        ("POLITY_SC_HARD_039", "Hard",
         "Which Article deals with the Original Jurisdiction of the Supreme Court in federal disputes between the Centre and States?",
         "ஒன்றியம் மற்றும் மாநிலங்களுக்கு இடையேயான கூட்டாட்சித் தகராறுகளில் உச்ச நீதிமன்றத்தின் மூல ஆதிக்கத்தைக் கையாளும் உறுப்பு எது?",
         ("Article 130", "உறுப்பு 130", "Article 131", "உறுப்பு 131", "Article 132", "உறுப்பு 132", "Article 133", "உறுப்பு 133"),
         "B",
         "Article 131 defines the Exclusive Original Jurisdiction of the Supreme Court in Centre-State and Inter-State disputes.",
         "உறுப்பு 131 ஒன்றியம்-மாநிலம் மற்றும் மாநிலங்களுக்கு இடையேயான தகராறுகளில் உச்ச நீதிமன்றத்தின் பிரத்யேக மூல ஆதிக்கத்தை வரையறுக்கிறது.",
         ("Art 130 is seat of SC.", "உறுப்பு 130 SC அமைவிடம்.", "Art 131 = Original Jurisdiction of Supreme Court.", "உறுப்பு 131 = உச்ச நீதிமன்றத்தின் மூல ஆதிக்கம்.", "Art 132 is constitutional appeals.", "உறுப்பு 132 அரசியலமைப்பு மேல்முறையீடு.", "Art 133 is civil appeals.", "உறுப்பு 133 சிவில் மேல்முறையீடு."),
         "Confusing Article 131 (Original Jurisdiction) with Article 132 (Appellate Jurisdiction).", "உறுப்பு 131 மற்றும் உறுப்பு 132-ஐக் குழப்புவது.", "Original Jurisdiction = Article 131.", "மூல ஆதிக்கம் = உறுப்பு 131.", "2"),

        ("POLITY_SC_HARD_040", "Hard",
         "Under Article 127, what condition must be satisfied before the Chief Justice of India appoints a High Court judge as an Ad Hoc judge of the Supreme Court?",
         "உறுப்பு 127-ன் கீழ் ஒரு HC நீதிபதியை SC Ad Hoc நீதிபதியாக நியமிக்கும் முன் CJI எந்த நிபந்தனைகளை நிறைவு செய்ய வேண்டும்?",
         ("Previous consent of the President AND consultation with the Chief Justice of the High Court concerned", "குடியரசுத் தலைவரின் முன்அனுமதி மற்றும் சம்பந்தப்பட்ட உயர் நீதிமன்றத் தலைமை நீதிபதியின் கலந்தாலோசனை", "Consent of the Union Law Minister only", "ஒன்றிய சட்ட அமைச்சரின் சம்மதம் மட்டுமே", "Approval of the Lok Sabha Speaker", "மக்களவைத் தலைவரின் ஒப்புதல்", "Consent of the State Governor only", "மாநில ஆளுநரின் சம்மதம் மட்டுமே"),
         "A",
         "Article 127(1) specifies that the CJI can appoint an ad hoc judge with the previous consent of the President and after consultation with the Chief Justice of the High Court concerned.",
         "உறுப்பு 127(1)-ன் படி, குடியரசுத் தலைவரின் முன்அனுமதி மற்றும் சம்பந்தப்பட்ட உயர் நீதிமன்றத் தலைமை நீதிபதியைக் கலந்தாலோசித்த பிறகே CJI Ad Hoc நீதிபதியை நியமிக்க முடியும்.",
         ("President's previous consent + Consultation with HC Chief Justice is mandatory under Art 127.", "குடியரசுத் தலைவர் முன்அனுமதி + HC தலைமை நீதிபதி கலந்தாலோசனை கட்டாயம்.", "Law Minister consent alone is insufficient.", "சட்ட அமைச்சர் சம்மதம் மட்டுமே போதாது.", "Speaker approval is not required.", "சபாநாயகர் ஒப்புதல் தேவையில்லை.", "Governor consent alone is insufficient.", "ஆளுநர் சம்மதம் மட்டுமே போதாது."),
         "Assuming CJI can appoint Ad hoc judges unilaterally without Presidential consent or HC Chief Justice consultation.", "CJI தன்னிச்சையாக அட்ஹாக் நீதிபதிகளை நியமிக்கலாம் என நினைப்பது.", "Ad Hoc Judge Appointment = Previous Consent of President + Consultation with HC Chief Justice (Article 127).", "Ad Hoc நீதிபதி நியமனம் = குடியரசுத் தலைவர் முன்அனுமதி + HC தலைமை நீதிபதி கலந்தாலோசனை.", "1"),

        ("POLITY_SC_HARD_041", "Hard",
         "Which Article of the Constitution lays down the provision for 'Acting Chief Justice of India'?",
         "தற்காலிக இந்தியத் தலைமை நீதிபதி (Acting CJI) நியமனம் பற்றிக் கூறும் அரசியலமைப்பு உறுப்பு எது?",
         ("Article 125", "உறுப்பு 125", "Article 126", "உறுப்பு 126", "Article 127", "உறுப்பு 127", "Article 128", "உறுப்பு 128"),
         "B",
         "Article 126 empowers the President to appoint an Acting Chief Justice of India when the office of CJI is vacant or CJI is unable to perform duties.",
         "உறுப்பு 126 தலைமை நீதிபதி பதவி காலியாக இருக்கும்போது அல்லது செயல்பட முடியாதபோது தற்காலிக CJI-யை நியமிக்க குடியரசுத் தலைவருக்கு அதிகாரமளிக்கிறது.",
         ("Art 125 is Judge Salaries.", "உறுப்பு 125 நீதிபதிகள் ஊதியம்.", "Art 126 = Appointment of Acting Chief Justice.", "உறுப்பு 126 = தற்காலிகத் தலைமை நீதிபதி நியமனம்.", "Art 127 is Ad hoc judges.", "உறுப்பு 127 Ad hoc நீதிபதிகள்.", "Art 128 is Attendance of retired judges.", "உறுப்பு 128 ஓய்வு பெற்ற நீதிபதிகள் வருகை."),
         "Confusing Article 126 (Acting CJI) with Article 127 (Ad hoc judges).", "உறுப்பு 126 மற்றும் உறுப்பு 127-ஐக் குழப்புவது.", "Acting Chief Justice = Article 126.", "தற்காலிகத் தலைமை நீதிபதி = உறுப்பு 126.", "2"),

        ("POLITY_SC_HARD_042", "Hard",
         "Under Article 128, can a retired Federal Court judge be requested to sit and act as a Judge of the Supreme Court?",
         "உறுப்பு 128-ன் கீழ் ஓய்வு பெற்ற கூட்டாட்சி நீதிமன்ற (Federal Court) நீதிபதியும் SC அமர்வில் அமர்ந்து செயல்பட கோரப்பட முடியுமா?",
         ("Yes, Article 128 explicitly includes retired judges of the Supreme Court OR of the Federal Court", "ஆம், உறுப்பு 128 ஓய்வு பெற்ற உச்ச நீதிமன்ற அல்லது கூட்டாட்சி நீதிமன்ற நீதிபதிகளை வெளிப்படையாக உள்ளடக்கிக் கூறுகிறது", "No, only retired Supreme Court judges post-1950 can be requested", "இல்லை, 1950-க்குப் பிந்தைய ஓய்வு பெற்ற SC நீதிபதிகளை மட்டுமே கோர முடியும்", "No, Federal Court judges were disqualified in 1950", "இல்லை, கூட்டாட்சி நீதிமன்ற நீதிபதிகள் 1950-ல் தகுதியிழப்பு செய்யப்பட்டனர்", "Yes, but only if approved by the Law Commission", "ஆம், ஆனால் சட்ட ஆணையம் ஒப்புதல் அளித்தால் மட்டுமே"),
         "A",
         "Article 128 text specifically states: 'the Chief Justice of India may... request any person who has held the office of a Judge of the Supreme Court or of the Federal Court... to sit and act as a Judge of the Supreme Court.'",
         "உறுப்பு 128-ன் மூல உரை தெளிவாகக் கூறுகிறது: ஓய்வு பெற்ற உச்ச நீதிமன்ற அல்லது கூட்டாட்சி நீதிமன்ற (Federal Court) நீதிபதியை அமர்வில் செயல்பட CJI கோரலாம்.",
         ("Article 128 text explicitly mentions BOTH retired SC judges and retired Federal Court judges.", "உறுப்பு 128 உரை SC மற்றும் கூட்டாட்சி நீதிமன்ற ஓய்வு பெற்ற நீதிபதிகள் இருவரையும் குறிப்பிடுகிறது.", "Exclusion of Federal Court judges is factually incorrect under Art 128 text.", "கூட்டாட்சி நீதிமன்ற நீதிபதிகளை விலக்குவது தவறானது.", "Disqualification in 1950 is factually wrong.", "1950 தகுதியிழப்பு என்பது தவறானது.", "Law Commission approval is not required.", "சட்ட ஆணைய ஒப்புதல் தேவையில்லை."),
         "Assuming Article 128 applies ONLY to post-1950 retired Supreme Court judges (the constitutional text explicitly includes retired Federal Court judges).", "உறுப்பு 128 1950-க்குப் பிந்தைய SC நீதிபதிகளுக்கு மட்டுமே பொருந்தும் என நினைப்பது.", "Article 128 Scope = Includes Retired SC Judges AND Retired Federal Court Judges.", "உறுப்பு 128 வரம்பு = ஓய்வு பெற்ற SC நீதிபதிகள் & ஓய்வு பெற்ற கூட்டாட்சி நீதிமன்ற நீதிபதிகள் இருவரையும் உள்ளடக்கியது.", "1"),

        ("POLITY_SC_HARD_043", "Hard",
         "Which Article of the Constitution confers power on the Supreme Court to grant Special Leave to Appeal?",
         "சிறப்பு விடுப்பு மேல்முறையீடு (SLP) வழங்கும் அதிகாரத்தை உச்ச நீதிமன்றத்திற்கு அளிக்கும் உறுப்பு எது?",
         ("Article 135", "உறுப்பு 135", "Article 136", "உறுப்பு 136", "Article 137", "உறுப்பு 137", "Article 138", "உறுப்பு 138"),
         "B",
         "Article 136 provides for Special Leave to Appeal by the Supreme Court.",
         "அரசியலமைப்பு உறுப்பு 136 உச்ச நீதிமன்றத்தின் சிறப்பு விடுப்பு மேல்முறையீட்டைப் பற்றிக் கூறுகிறது.",
         ("Art 135 is Federal Court jurisdiction continuance.", "உறுப்பு 135 கூட்டாட்சி நீதிமன்ற அதிகாரம் தொடர்தல்.", "Art 136 = Special Leave to Appeal (SLP).", "உறுப்பு 136 = சிறப்பு விடுப்பு மேல்முறையீடு (SLP).", "Art 137 is Review of judgments.", "உறுப்பு 137 தீர்ப்புகள் சீராய்வு.", "Art 138 is enlargement of SC jurisdiction.", "உறுப்பு 138 அதிகார வரம்பு விரிவாக்கம்."),
         "Confusing Article 136 (SLP) with Article 137 (Review).", "உறுப்பு 136 மற்றும் உறுப்பு 137-ஐக் குழப்புவது.", "Special Leave to Appeal = Article 136.", "சிறப்பு விடுப்பு மேல்முறையீடு = உறுப்பு 136.", "2"),

        ("POLITY_SC_HARD_044", "Hard",
         "Under Article 145(4), how must all judgments and advisory opinions of the Supreme Court be delivered?",
         "உறுப்பு 145(4)-ன் படி உச்ச நீதிமன்றத்தின் அனைத்துத் தீர்ப்புகளும் ஆலோசனை கருத்துக்களும் எவ்வாறு அறிவிக்கப்பட வேண்டும்?",
         ("In open court only", "திறந்த நீதிமன்றத்தில் மட்டுமே (In Open Court)", "In camera / private chambers if CJI decides", "CJI விரும்பினால் ரகசிய அறையில் அறிவிக்கலாம்", "Through press releases issued by Law Ministry", "சட்ட அமைச்சகச் செய்திக்குறிப்பு மூலம்", "By laying them on the table of Parliament", "நாடாளுமன்ற மேஜையில் சமர்ப்பிப்பதன் மூலம்"),
         "A",
         "Article 145(4) explicitly mandates: 'No judgment shall be delivered by the Supreme Court save in open court, and no report shall be made under Article 143 save in accordance with an opinion also delivered in open court.'",
         "உறுப்பு 145(4) தெளிவாகக் கட்டாயமாக்குகிறது: உச்ச நீதிமன்றத்தின் எந்தவொரு தீர்ப்பும் அல்லது உறுப்பு 143 ஆலோசனையும் திறந்த நீதிமன்றத்தில் (Open Court) மட்டுமே அறிவிக்கப்பட வேண்டும்.",
         ("Art 145(4) strictly mandates delivery in OPEN COURT.", "உறுப்பு 145(4) திறந்த நீதிமன்றத்தில் அறிவிப்பதைக் கட்டாயமாக்குகிறது.", "In camera judgment delivery is prohibited under Art 145(4).", "ரகசிய தீர்ப்பு அறிவிப்பு உறுப்பு 145(4)-க்கு எதிரானது.", "Law Ministry press release is not judicial delivery.", "சட்ட அமைச்சக செய்திக்குறிப்பு நீதித்துறை அறிவிப்பு அல்ல.", "Laying in Parliament is not judicial delivery.", "நாடாளுமன்றத்தில் சமர்ப்பிப்பது அல்ல."),
         "Assuming judgments can be delivered in private chambers without open court pronouncement.", "ரகசிய அறையில் தீர்ப்பு வழங்கப்படலாம் என நினைப்பது.", "Delivery of SC Judgments & Advisory Opinions = IN OPEN COURT ONLY (Article 145(4)).", "SC தீர்ப்புகள் & ஆலோசனை கருத்துக்கள் அறிவிப்பு = திறந்த நீதிமன்றத்தில் மட்டுமே (உறுப்பு 145(4)).", "1"),

        ("POLITY_SC_HARD_045", "Hard",
         "Which Constitutional Amendment Act added Article 134A regarding Certificate for Appeal to the Supreme Court?",
         "உச்ச நீதிமன்ற மேல்முறையீட்டுச் சான்றிதழ் பற்றிய உறுப்பு 134A-ஐச் சேர்த்த அரசியலமைப்புத் திருத்தச் சட்டம் எது?",
         ("42nd Constitutional Amendment Act 1976", "42-வது அரசியலமைப்புத் திருத்தச் சட்டம் 1976", "44th Constitutional Amendment Act 1978", "44-வது அரசியலமைப்புத் திருத்தச் சட்டம் 1978", "24th Constitutional Amendment Act 1971", "24-வது அரசியலமைப்புத் திருத்தச் சட்டம் 1971", "86th Constitutional Amendment Act 2002", "86-வது அரசியலமைப்புத் திருத்தச் சட்டம் 2002"),
         "B",
         "Article 134A was inserted by the 44th Constitutional Amendment Act 1978 to streamline the process of High Courts issuing certificates of fitness for appeal to SC.",
         "உயர் நீதிமன்றங்கள் உச்ச நீதிமன்ற மேல்முறையீட்டுச் சான்றிதழ் வழங்குவதைச் சீரமைக்க 44-வது அரசியலமைப்புத் திருத்தச் சட்டம் 1978 மூலம் உறுப்பு 134A சேர்க்கப்பட்டது.",
         ("44th Amendment Act 1978 inserted Article 134A.", "44-வது திருத்தச் சட்டம் 1978 உறுப்பு 134A-ஐச் சேர்த்தது.", "42nd Amendment inserted Art 139A, not 134A.", "42-வது திருத்தம் 139A-ஐச் சேர்த்தது.", "24th Amendment dealt with Art 13 & 368.", "24-வது திருத்தம் உறுப்பு 13 & 368.", "86th Amendment introduced Right to Education.", "86-வது திருத்தம் கல்வி உரிமை."),
         "Confusing 42nd Amendment (inserted Art 139A case transfer) with 44th Amendment (inserted Art 134A appeal certificate).", "42-வது திருத்தம் (139A) மற்றும் 44-வது திருத்தம் (134A) ஆகியவற்றை குழப்புவது.", "Article 134A Certificate for Appeal = Inserted by 44th Constitutional Amendment Act 1978.", "உறுப்பு 134A மேல்முறையீட்டுச் சான்றிதழ் = 44-வது திருத்தச் சட்டம் 1978 மூலம் சேர்க்கப்பட்டது.", "2"),

        ("POLITY_SC_HARD_046", "Hard",
         "Under Article 135, what jurisdiction does the Supreme Court exercise regarding matters not covered under Articles 133 or 134?",
         "உறுப்புகள் 133 அல்லது 134-ல் வராத விவகாரங்களில் உறுப்பு 135-ன் கீழ் உச்ச நீதிமன்றம் எந்த அதிகார வரம்பைப் பயன்படுத்துகிறது?",
         ("Jurisdiction and powers which were exercisable by the Federal Court immediately before the commencement of the Constitution under any existing law", "அரசியலமைப்பு அமலுக்கு வரும் முன் கூட்டாட்சி நீதிமன்றத்தால் (Federal Court) பயன்படுத்தப்பட்ட அதிகார வரம்பு மற்றும் அதிகாரங்கள்", "Advisory jurisdiction over foreign governments", "வெளிநாட்டு அரசுகள் மீதான ஆலோசனை ஆதிக்கம்", "Power to dissolve State Legislative Councils directly", "மாநில சட்ட மேலவைகளை நேரடியாகக் கலைக்கும் அதிகாரம்", "Power to audit Union Government defense accounts", "ஒன்றிய அரசின் பாதுகாப்பு கணக்குகளைத் தணிக்கை செய்யும் அதிகாரம்"),
         "A",
         "Article 135 provides that the Supreme Court shall also have jurisdiction and powers with respect to any matter to which the provisions of Art 133 or 134 do not apply if jurisdiction and powers in relation to that matter were exercisable by the Federal Court before the Constitution.",
         "உறுப்புகள் 133 அல்லது 134 பொருந்தாத விவகாரங்களில், அரசியலமைப்புக்கு முன் கூட்டாட்சி நீதிமன்றத்தால் (Federal Court) பயன்படுத்தப்பட்ட அதிகார வரம்பை உச்ச நீதிமன்றமும் பயன்படுத்த உறுப்பு 135 வழிவகை செய்கிறது.",
         ("Art 135 confers Federal Court powers on SC for matters outside Art 133/134.", "உறுப்பு 135 133/134-க்கு அப்பாற்பட்ட விவகாரங்களில் கூட்டாட்சி நீதிமன்ற அதிகாரங்களை SC-க்கு அளிக்கிறது.", "Foreign government advisory power is non-existent.", "வெளிநாட்டு அரசு ஆலோசனை அதிகாரம் இல்லை.", "Legislative council dissolution is not a court power.", "சட்ட மேலவைக் கலைப்பு நீதிமன்ற அதிகாரமல்ல.", "Defense accounts auditing is CAG function.", "பாதுகாப்பு கணக்குத் தணிக்கை CAG வேலை."),
         "Treating Article 135 as a defunct provision (it bridges the historical transition of jurisdiction from Federal Court to SC).", "உறுப்பு 135-ஐ ஒரு பயனற்ற விதியாகக் கருதுவது.", "Article 135 = Supreme Court exercises pre-Constitution Federal Court jurisdiction for matters outside Arts 133/134.", "உறுப்பு 135 = 133/134-க்கு அப்பாற்பட்ட விவகாரங்களில் கூட்டாட்சி நீதிமன்ற அதிகாரங்களை SC பயன்படுத்துகிறது.", "1"),

        ("POLITY_SC_HARD_047", "Hard",
         "Which Article defines the Appellate Jurisdiction of the Supreme Court in appeals from High Courts regarding CONSTITUTIONAL MATTERS?",
         "அரசியலமைப்பு விவகாரங்களில் உயர் நீதிமன்ற தீர்ப்புகளுக்கு எதிரான உச்ச நீதிமன்றத்தின் மேல்முறையீட்டு அதிகார வரம்பைக் கூறும் உறுப்பு எது?",
         ("Article 131", "உறுப்பு 131", "Article 132", "உறுப்பு 132", "Article 133", "உறுப்பு 133", "Article 134", "உறுப்பு 134"),
         "B",
         "Article 132 specifies Appellate Jurisdiction of SC in appeals from High Courts in constitutional matters.",
         "அரசியலமைப்பு விவகாரங்களில் உயர் நீதிமன்றத் தீர்ப்புகளுக்கு எதிரான மேல்முறையீட்டு அதிகாரத்தை உறுப்பு 132 அளிக்கிறது.",
         ("Art 131 is Original Jurisdiction.", "உறுப்பு 131 மூல ஆதிக்கம்.", "Art 132 = Constitutional Appellate Jurisdiction.", "உறுப்பு 132 = அரசியலமைப்பு மேல்முறையீட்டு ஆதிக்கம்.", "Art 133 is Civil Appellate Jurisdiction.", "உறுப்பு 133 சிவில் மேல்முறையீட்டு ஆதிக்கம்.", "Art 134 is Criminal Appellate Jurisdiction.", "உறுப்பு 134 குற்றவியல் மேல்முறையீட்டு ஆதிக்கம்."),
         "Confusing Article 132 (Constitutional Appeals) with Article 133 (Civil Appeals).", "உறுப்பு 132 மற்றும் உறுப்பு 133-ஐக் குழப்புவது.", "Constitutional Appellate Jurisdiction = Article 132.", "அரசியலமைப்பு மேல்முறையீட்டு ஆதிக்கம் = உறுப்பு 132.", "2"),

        ("POLITY_SC_HARD_048", "Hard",
         "Which Article defines the Appellate Jurisdiction of the Supreme Court in appeals from High Courts regarding CIVIL MATTERS?",
         "சிவில் விவகாரங்களில் உயர் நீதிமன்ற தீர்ப்புகளுக்கு எதிரான உச்ச நீதிமன்றத்தின் மேல்முறையீட்டு அதிகார வரம்பைக் கூறும் உறுப்பு எது?",
         ("Article 132", "உறுப்பு 132", "Article 133", "உறுப்பு 133", "Article 134", "உறுப்பு 134", "Article 135", "உறுப்பு 135"),
         "B",
         "Article 133 specifies Appellate Jurisdiction of SC in appeals from High Courts in civil matters.",
         "சிவில் விவகாரங்களில் உயர் நீதிமன்றத் தீர்ப்புகளுக்கு எதிரான மேல்முறையீட்டு அதிகாரத்தை உறுப்பு 133 அளிக்கிறது.",
         ("Art 132 is Constitutional appeals.", "உறுப்பு 132 அரசியலமைப்பு மேல்முறையீடு.", "Art 133 = Civil Appellate Jurisdiction.", "உறுப்பு 133 = சிவில் மேல்முறையீட்டு ஆதிக்கம்.", "Art 134 is Criminal appeals.", "உறுப்பு 134 குற்றவியல் மேல்முறையீடு.", "Art 135 is Federal court jurisdiction.", "உறுப்பு 135 கூட்டாட்சி நீதிமன்ற அதிகாரம்."),
         "Confusing Article 133 (Civil Appeals) with Article 134 (Criminal Appeals).", "உறுப்பு 133 மற்றும் உறுப்பு 134-ஐக் குழப்புவது.", "Civil Appellate Jurisdiction = Article 133.", "சிவில் மேல்முறையீட்டு ஆதிக்கம் = உறுப்பு 133.", "2"),

        ("POLITY_SC_HARD_049", "Hard",
         "Which Article defines the Appellate Jurisdiction of the Supreme Court in appeals from High Courts regarding CRIMINAL MATTERS?",
         "குற்றவியல் விவகாரங்களில் உயர் நீதிமன்ற தீர்ப்புகளுக்கு எதிரான உச்ச நீதிமன்றத்தின் மேல்முறையீட்டு அதிகார வரம்பைக் கூறும் உறுப்பு எது?",
         ("Article 132", "உறுப்பு 132", "Article 133", "உறுப்பு 133", "Article 134", "உறுப்பு 134", "Article 135", "உறுப்பு 135"),
         "C",
         "Article 134 specifies Appellate Jurisdiction of SC in appeals from High Courts in criminal matters.",
         "குற்றவியல் விவகாரங்களில் உயர் நீதிமன்றத் தீர்ப்புகளுக்கு எதிரான மேல்முறையீட்டு அதிகாரத்தை உறுப்பு 134 அளிக்கிறது.",
         ("Art 132 is Constitutional appeals.", "உறுப்பு 132 அரசியலமைப்பு மேல்முறையீடு.", "Art 133 is Civil appeals.", "உறுப்பு 133 சிவில் மேல்முறையீடு.", "Art 134 = Criminal Appellate Jurisdiction.", "உறுப்பு 134 = குற்றவியல் மேல்முறையீட்டு ஆதிக்கம்.", "Art 135 is Federal court jurisdiction.", "உறுப்பு 135 கூட்டாட்சி நீதிமன்ற அதிகாரம்."),
         "Confusing Article 134 (Criminal Appeals) with Article 133 (Civil Appeals).", "உறுப்பு 134 மற்றும் உறுப்பு 133-ஐக் குழப்புவது.", "Criminal Appellate Jurisdiction = Article 134.", "குற்றவியல் மேல்முறையீட்டு ஆதிக்கம் = உறுப்பு 134.", "3"),

        ("POLITY_SC_HARD_050", "Hard",
         "Under Article 145(1), the Supreme Court makes rules for regulating its practice and procedure WITH THE APPROVAL OF WHOM?",
         "உறுப்பு 145(1)-ன் படி உச்ச நீதிமன்றம் தன் நடைமுறை மற்றும் செயலாக்க விதிகளை யாருடைய ஒப்புதலுடன் அமைத்துக் கொள்கிறது?",
         ("President of India", "இந்தியக் குடியரசுத் தலைவர்", "Union Law Minister", "ஒன்றிய சட்ட அமைச்சர்", "Parliament of India", "இந்திய நாடாளுமன்றம்", "Chief Justice of India independently without approval", "குடியரசுத் தலைவர் ஒப்புதலின்றி தன்னிச்சையாக தலைமை நீதிபதி"),
         "A",
         "Article 145(1) states: 'Subject to the provisions of any law made by Parliament, the Supreme Court may from time to time, WITH THE APPROVAL OF THE PRESIDENT, make rules for regulating generally the practice and procedure of the Court.'",
         "உறுப்பு 145(1)-ன் படி, நாடாளுமன்றச் சட்டத்திற்கு உட்பட்டு, குடியரசுத் தலைவரின் ஒப்புதலுடன் (With the approval of the President) உச்ச நீதிமன்றம் தனது நடைமுறை விதிகளை அமைத்துக்கொள்ளலாம்.",
         ("President approval is mandated under Art 145(1) for SC rules.", "உறுப்பு 145(1)-ன் கீழ் SC விதிகளுக்கு குடியரசுத் தலைவர் ஒப்புதல் கட்டாயமாகும்.", "Law Minister approval is not the constitutional text.", "சட்ட அமைச்சர் ஒப்புதல் அரசியலமைப்பு உரைச் சொல் அல்ல.", "Parliament makes laws, but rules are framed by SC with President approval.", "நாடாளுமன்றம் சட்டங்களை இயற்றுகிறது, விதிகளை SC குடியரசுத் தலைவர் ஒப்புதலுடன் அமைக்கிறது.", "Independent framing without approval is incorrect under Art 145(1).", "ஒப்புதலின்றி தன்னிச்சையாக அமைப்பது தவறானது."),
         "Assuming SC frames its procedure rules completely independently without requiring Presidential approval (Art 145(1) explicitly requires President's approval).", "SC தன் நடைமுறை விதிகளை குடியரசுத் தலைவர் ஒப்புதலின்றி அமைக்கிறது என நினைப்பது.", "Supreme Court Rule-Making Power = Framed by SC WITH APPROVAL OF THE PRESIDENT (Article 145(1)).", "SC நடைமுறை விதிகள் = குடியரசுத் தலைவர் ஒப்புதலுடன் உச்ச நீதிமன்றம் அமைக்கும் (உறுப்பு 145(1)).", "1")
    ]

    hard = []
    for idx, item in enumerate(hard_data):
        if len(item) == 14:
            qid, diff, s_en, s_ta, opts, corr, exp_en, exp_ta, why_args, trap_en, trap_ta, tip_en, tip_ta, sp = item
        else:
            qid, diff, s_en, s_ta, opts, corr, exp_en, why_args, trap_en, trap_ta, tip_en, tip_ta, sp = item
            corr_idx = {"A": 1, "B": 3, "C": 5, "D": 7}[corr]
            exp_ta = why_args[corr_idx]
        options = make_options(*opts)
        hard.append(build_q(qid, diff, s_en, s_ta, options, corr, exp_en, exp_ta, why_args, trap_en, trap_ta, tip_en, tip_ta, sp))
    return hard

def main():
    hard_qs = get_hard_questions()
    print(f"Generated Hard Questions: {len(hard_qs)}")
    assert len(hard_qs) == 50, f"Expected 50, got {len(hard_qs)}"
    
    out_path = "data/questions/polity/supreme_court_hard.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(hard_qs, f, ensure_ascii=False, indent=2)
    print(f"Saved -> {out_path}")

if __name__ == "__main__":
    main()
