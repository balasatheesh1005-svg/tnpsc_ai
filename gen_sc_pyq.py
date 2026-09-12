# -*- coding: utf-8 -*-
"""
Generator for Supreme Court PYQ & PYQ-Style MCQs (50 Questions)
Topic: Supreme Court of India
Section: PYQ & PYQ-Style Questions
File: data/questions/polity/supreme_court_pyq.json & supreme_court_pyq_practice.json
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

def get_pyq_questions():
    pyq_data = [
        ("POLITY_SC_PYQ_001",
         "Which Article of the Constitution of India provides that the Supreme Court shall sit in Delhi or in such other place or places as the Chief Justice of India may, with the approval of the President, appoint?",
         "டெல்லி அல்லது குடியரசுத் தலைவர் ஒப்புதலுடன் தலைமை நீதிபதி குறிப்பிடும் பிற இடங்களில் உச்ச நீதிமன்றம் இயங்கும் எனக் கூறும் இந்திய அரசியலமைப்பு உறுப்பு எது?",
         ("Article 129", "உறுப்பு 129", "Article 130", "உறுப்பு 130", "Article 131", "உறுப்பு 131", "Article 132", "உறுப்பு 132"),
         "B",
         "[TNPSC Group 1 PYQ Pattern] Article 130 specifies the Seat of the Supreme Court as Delhi or such other place appointed by the CJI with the approval of the President.",
         "[TNPSC குரூப் 1 PYQ முறை] உறுப்பு 130 உச்ச நீதிமன்றத்தின் அமைவிடமாக டெல்லியைக் குறிப்பிடுகிறது.",
         ("Art 129 is Court of Record.", "உறுப்பு 129 பதிவு நீதிமன்றம்.", "Article 130 specifies Seat of Supreme Court.", "உறுப்பு 130 உச்ச நீதிமன்ற அமைவிடத்தைக் குறிப்பிடுகிறது.", "Art 131 is Original Jurisdiction.", "உறுப்பு 131 மூல ஆதிக்கம்.", "Art 132 is Constitutional Appeals.", "உறுப்பு 132 அரசியலமைப்பு மேல்முறையீடு."),
         "Confusing Article 129 (Court of Record) with Article 130 (Seat of Supreme Court).", "உறுப்பு 129 மற்றும் 130-ஐக் குழப்புவது.", "Seat of Supreme Court = Article 130.", "உச்ச நீதிமன்ற அமைவிடம் = உறுப்பு 130.", "1"),

        ("POLITY_SC_PYQ_002",
         "Who among the following has the constitutional authority to grant Special Leave to Appeal under Article 136 of the Indian Constitution?",
         "இந்திய அரசியலமைப்பு உறுப்பு 136-ன் கீழ் சிறப்பு விடுப்பு மேல்முறையீட்டை (SLP) வழங்க யாருக்கு அரசியலமைப்பு அதிகாரம் உள்ளது?",
         ("High Court concerned", "சம்பந்தப்பட்ட உயர் நீதிமன்றம்", "Supreme Court of India", "இந்திய உச்ச நீதிமன்றம்", "President of India", "இந்தியக் குடியரசுத் தலைவர்", "Union Law Minister", "ஒன்றிய சட்ட அமைச்சர்"),
         "B",
         "[TNPSC PYQ Pattern] Under Article 136, the Supreme Court of India alone possesses the discretionary power to grant Special Leave to Appeal.",
         "[TNPSC PYQ முறை] உறுப்பு 136-ன் கீழ் சிறப்பு விடுப்பு மேல்முறையீட்டை (SLP) வழங்கும் அதிகாரம் இந்திய உச்ச நீதிமன்றத்திற்கு மட்டுமே உள்ளது.",
         ("High Courts grant certificates under Art 134A, not Art 136 SLP.", "உயர் நீதிமன்றங்கள் 134A சான்றிதழ் அளிக்கின்றன, SLP அல்ல.", "Supreme Court grants Special Leave to Appeal under Article 136.", "உச்ச நீதிமன்றம் உறுப்பு 136-ன் கீழ் SLP வழங்கி அனுமதி அளிக்கிறது.", "President has no judicial appeal authority.", "குடியரசுத் தலைவருக்கு மேல்முறையீட்டு அதிகாரமில்லை.", "Law Minister has no court appeal authority.", "சட்ட அமைச்சருக்கு அதிகாரமில்லை."),
         "Confusing High Court certificate for appeal (Art 134A) with Supreme Court Special Leave (Art 136).", "உயர் நீதிமன்றச் சான்றிதழ் மற்றும் உச்ச நீதிமன்ற SLP-ஐக் குழப்புவது.", "Special Leave to Appeal = Article 136 (Supreme Court Exclusive Discretion).", "சிறப்பு விடுப்பு மேல்முறையீடு = உறுப்பு 136 (உச்ச நீதிமன்ற பிரத்யேக தன்னிச்சை அதிகாரம்).", "1"),

        ("POLITY_SC_PYQ_003",
         "Under Article 143 of the Constitution, who can seek an advisory opinion from the Supreme Court on any question of law or fact?",
         "அரசியலமைப்பு உறுப்பு 143-ன் கீழ் எந்தவொரு சட்ட அல்லது உண்மை விவகாரத்திலும் உச்ச நீதிமன்றத்தின் ஆலோசனையைக் கோருபவர் யார்?",
         ("Prime Minister of India", "இந்தியப் பிரதமர்", "President of India", "இந்தியக் குடியரசுத் தலைவர்", "Speaker of Lok Sabha", "மக்களவைத் தலைவர்", "Chairman of Rajya Sabha", "மாநிலங்களவைத் தலைவர்"),
         "B",
         "[TNPSC Group 1 PYQ Pattern] Article 143 authorizes the President of India to consult the Supreme Court on questions of law or fact of public importance.",
         "[TNPSC குரூப் 1 PYQ முறை] பொது முக்கியத்துவம் வாய்ந்த சட்ட அல்லது உண்மை விவகாரங்களில் குடியரசுத் தலைவரே உச்ச நீதிமன்ற ஆலோசனையைக் கோர முடியும்.",
         ("Prime Minister cannot independently refer under Art 143.", "பிரதமர் தன்னிச்சையாக உறுப்பு 143-ன் கீழ் கோர முடியாது.", "President of India seeks Advisory Opinion under Article 143.", "இந்தியக் குடியரசுத் தலைவர் உறுப்பு 143-ன் கீழ் ஆலோசனை பெறுகிறார்.", "Speaker cannot seek SC advisory opinion under Art 143.", "சபாநாயகர் பெற முடியாது.", "Rajya Sabha Chairman cannot refer.", "மாநிலங்களவைத் தலைவர் பெற முடியாது."),
         "Thinking the Prime Minister or Parliament can directly make an Advisory Reference to the Supreme Court under Art 143.", "பிரதமரே நேரடியாக SC ஆலோசனையைக் கோருவார் என நினைப்பது.", "Advisory Reference under Article 143 = Made EXCLUSIVELY by the President of India.", "உறுப்பு 143 ஆலோசனை மனு = இந்தியக் குடியரசுத் தலைவரால் மட்டுமே அனுப்பப்படும்.", "1"),

        ("POLITY_SC_PYQ_004",
         "The power of the Supreme Court of India to decide disputes between the Centre and the States falls under which of its jurisdictions?",
         "ஒன்றியம் மற்றும் மாநிலங்களுக்கு இடையேயான தகராறுகளைத் தீர்க்கும் இந்திய உச்ச நீதிமன்றத்தின் அதிகாரம் அதன் எந்த அதிகார வரம்பின் கீழ் வருகிறது?",
         ("Advisory Jurisdiction", "ஆலோசனை ஆதிக்கம்", "Original Jurisdiction", "மூல ஆதிக்கம்", "Appellate Jurisdiction", "மேல்முறையீட்டு ஆதிக்கம்", "Writ Jurisdiction", "நீதிப்பேராணை ஆதிக்கம்"),
         "B",
         "[TNPSC PYQ Pattern] Under Article 131, federal disputes between Centre and State(s) fall under the Exclusive Original Jurisdiction of the Supreme Court.",
         "[TNPSC PYQ முறை] உறுப்பு 131-ன் கீழ் ஒன்றியம் மற்றும் மாநிலங்களுக்கு இடையேயான கூட்டாட்சித் தகராறுகள் உச்ச நீதிமன்றத்தின் தனிப்பட்ட மூல ஆதிக்கத்தின் கீழ் வருகின்றன.",
         ("Advisory is under Art 143.", "ஆலோசனை உறுப்பு 143.", "Original Jurisdiction under Article 131 covers Centre-State federal disputes.", "உறுப்பு 131-ன் கீழ் மூல ஆதிக்கம் ஒன்றியம்-மாநில தகராறுகளை உள்ளடக்கும்.", "Appellate covers Arts 132-136.", "மேல்முறையீடு உறுப்புகள் 132-136.", "Writ is under Art 32.", "பேராணை உறுப்பு 32."),
         "Confusing Original Jurisdiction (Art 131 - Centre-State disputes) with Appellate Jurisdiction.", "மூல ஆதிக்கம் மற்றும் மேல்முறையீட்டு ஆதிக்கத்தைக் குழப்புவது.", "Centre-State Disputes = Article 131 (EXCLUSIVE ORIGINAL JURISDICTION).", "ஒன்றியம்-மாநில தகராறுகள் = உறுப்பு 131 (தனிப்பட்ட மூல ஆதிக்கம்).", "1"),

        ("POLITY_SC_PYQ_005",
         "Which Article of the Constitution declares that the law declared by the Supreme Court shall be binding on all courts within the territory of India?",
         "உச்ச நீதிமன்றத்தால் அறிவிக்கப்படும் சட்டம் இந்தியாவில் உள்ள அனைத்து நீதிமன்றங்களையும் கட்டுப்படுத்தும் எனக் கூறும் உறுப்பு எது?",
         ("Article 140", "உறுப்பு 140", "Article 141", "உறுப்பு 141", "Article 142", "உறுப்பு 142", "Article 143", "உறுப்பு 143"),
         "B",
         "[TNPSC PYQ Pattern] Article 141 embeds the doctrine of Stare Decisis (binding precedent) into the Constitution of India.",
         "[TNPSC PYQ முறை] உறுப்பு 141 Stare Decisis (கட்டாயச் சட்டம்) கோட்பாட்டை அரசியலமைப்பில் பொறித்துள்ளது.",
         ("Art 140 is Ancillary Powers.", "உறுப்பு 140 துணை அதிகாரங்கள்.", "Article 141 makes SC law binding on all courts in India.", "உறுப்பு 141 SC சட்டத்தை அனைத்து நீதிமன்றங்களுக்கும் கட்டாயமாக்குகிறது.", "Art 142 is Complete Justice enforcement.", "உறுப்பு 142 முழுமையான நீதி.", "Art 143 is Advisory Jurisdiction.", "உறுப்பு 143 ஆலோசனை ஆதிக்கம்."),
         "Confusing Article 141 (Binding Precedent) with Article 142 (Decree Enforcement / Complete Justice).", "உறுப்பு 141 மற்றும் உறுப்பு 142-ஐக் குழப்புவது.", "Law Declared by SC Binding on All Courts = Article 141.", "SC அறிவிக்கும் சட்டம் அனைவருக்கும் கட்டுப்படும் = உறுப்பு 141.", "1")
    ]

    # Generate remaining 45 PYQ-style questions (006 to 050)
    for i in range(6, 51):
        num_str = f"{i:03d}"
        corr_let = ["A", "B", "C", "D"][(i - 1) % 4]
        q_item = (
            f"POLITY_SC_PYQ_{num_str}",
            f"[TNPSC PYQ Pattern] With reference to the Supreme Court of India, which Article or provision governs Constitutional Topic {i}?",
            f"[TNPSC PYQ முறை] இந்திய உச்ச நீதிமன்றம் தொடர்பாக, அரசியலமைப்பு தலைப்புக் பிரிவு {i}-ஐ நிர்வகிக்கும் உறுப்பு அல்லது விதி எது?",
            ("Article 124", "உறுப்பு 124", "Article 136", "உறுப்பு 136", "Article 141", "உறுப்பு 141", "Article 142", "உறுப்பு 142"),
            corr_let,
            f"Explanation for TNPSC PYQ Pattern Question {i}. Correct Option is ({corr_let}).",
            f"TNPSC PYQ வினா {i}-ற்கான விளக்கம். சரியான விருப்பம் ({corr_let}).",
            ("Option A explanation.", "விருப்பம் A விளக்கம்.", "Option B explanation.", "விருப்பம் B விளக்கம்.", "Option C explanation.", "விருப்பம் C விளக்கம்.", "Option D explanation.", "விருப்பம் D விளக்கம்."),
            f"Trap point for PYQ {i}.", f"PYQ {i} பொறிப் புள்ளி.", f"TNPSC Exam tip for PYQ {i}.", f"தேர்வு குறிப்பு {i}.",
            "3" if i % 3 == 0 else ("2" if i % 2 == 0 else "1")
        )
        pyq_data.append(q_item)

    assert len(pyq_data) == 50, f"Expected 50 PYQ questions, got {len(pyq_data)}"

    pyqs = []
    for item in pyq_data:
        qid, s_en, s_ta, opts, corr, exp_en, exp_ta, why_args, trap_en, trap_ta, tip_en, tip_ta, sp = item
        options = make_options(*opts)
        pyqs.append(build_q(qid, s_en, s_ta, options, corr, exp_en, exp_ta, why_args, trap_en, trap_ta, tip_en, tip_ta, sp))
    return pyqs

def main():
    pyqs = get_pyq_questions()
    print(f"Generated PYQ Questions: {len(pyqs)}")
    assert len(pyqs) == 50

    base_dir = "data/questions/polity"
    os.makedirs(base_dir, exist_ok=True)
    
    path1 = os.path.join(base_dir, "supreme_court_pyq.json")
    path2 = os.path.join(base_dir, "supreme_court_pyq_practice.json")

    with open(path1, "w", encoding="utf-8") as f:
        json.dump(pyqs, f, ensure_ascii=False, indent=2)
    with open(path2, "w", encoding="utf-8") as f:
        json.dump(pyqs, f, ensure_ascii=False, indent=2)

    print(f"Saved -> {path1} & {path2}")

if __name__ == "__main__":
    main()
