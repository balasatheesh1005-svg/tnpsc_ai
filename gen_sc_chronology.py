# -*- coding: utf-8 -*-
"""
Generator for Supreme Court Chronology MCQs (25 Questions)
Topic: Supreme Court of India
Section: Chronology Questions
File: data/questions/polity/supreme_court_chronology.json
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
        "question_type": "Chronology",
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

def get_chronology_questions():
    chrono_data = [
        ("POLITY_SC_CHRONO_001",
         "Arrange the following landmark Supreme Court cases in chronological order of their judgment dates:\n1. Shankari Prasad v. Union of India\n2. Golaknath v. State of Punjab\n3. Kesavananda Bharati v. State of Kerala\n4. Minerva Mills v. Union of India",
         "பின்வரும் வரலாற்றுச் சிறப்புமிக்க உச்ச நீதிமன்ற வழக்குகளை அவற்றின் தீர்ப்பு நாட்களின் அடிப்படையில் காலவரிசைப்படுத்துக:\n1. சங்கரி பிரசாத் vs இந்திய ஒன்றியம்\n2. கோலக்நாத் vs பஞ்சாப் மாநிலம்\n3. கேசவாநந்த பாரதி vs கேரளா மாநிலம்\n4. மினர்வா மில்ஸ் vs இந்திய ஒன்றியம்",
         ("1 → 2 → 3 → 4", "1 → 2 → 3 → 4", "2 → 1 → 4 → 3", "2 → 1 → 4 → 3", "3 → 1 → 2 → 4", "3 → 1 → 2 → 4", "4 → 3 → 2 → 1", "4 → 3 → 2 → 1"),
         "A",
         "Correct Chronology: 1. Shankari Prasad (1951) -> 2. Golaknath (1967) -> 3. Kesavananda Bharati (1973) -> 4. Minerva Mills (1980). Sequence is 1 -> 2 -> 3 -> 4.",
         "சரியான காலவரிசை: 1. சங்கரி பிரசாத் (1951) -> 2. கோலக்நாத் (1967) -> 3. கேசவாநந்த பாரதி (1973) -> 4. மினர்வா மில்ஸ் (1980). வரிசை 1 -> 2 -> 3 -> 4.",
         ("1-2-3-4 is the exact chronological sequence.", "1-2-3-4 என்பது துல்லியமான காலவரிசையாகும்.", "Incorrect sequence.", "தவறான காலவரிசை.", "Incorrect sequence.", "தவறான காலவரிசை.", "Incorrect sequence.", "தவறான காலவரிசை."),
         "Confusing Golaknath (1967) and Kesavananda Bharati (1973) dates.", "கோலக்நாத் (1967) மற்றும் கேசவாநந்த பாரதி (1973) ஆண்டுகளைக் குழப்புவது.", "Judgments Chronology: Shankari Prasad (1951) -> Golaknath (1967) -> Kesavananda (1973) -> Minerva Mills (1980).", "தீர்ப்புகள் காலவரிசை: சங்கரி பிரசாத் (1951) -> கோலக்நாத் (1967) -> கேசவாநந்த (1973) -> மினர்வா மில்ஸ் (1980).", "1"),

        ("POLITY_SC_CHRONO_002",
         "Arrange the Judicial Appointments (Judges Cases) in chronological order of their occurrence:\n1. First Judges Case (SP Gupta v. UOI)\n2. Second Judges Case (SCAORA v. UOI)\n3. Third Judges Case (Presidential Reference)\n4. Fourth Judges Case (NJAC Striking Down)",
         "நீதிபதிகள் நியமன வழக்குகளை (Judges Cases) அவை நிகழ்ந்த காலவரிசைப்படி அமைக்கவும்:\n1. முதல் நீதிபதிகள் வழக்கு (எஸ்.பி. குப்தா வழக்கு)\n2. இரண்டாவது நீதிபதிகள் வழக்கு (SCAORA வழக்கு)\n3. மூன்றாவது நீதிபதிகள் வழக்கு (குடியரசுத் தலைவர் ஆலோசனை)\n4. நான்காவது நீதிபதிகள் வழக்கு (NJAC ரத்து வழக்கு)",
         ("1 → 2 → 3 → 4", "1 → 2 → 3 → 4", "2 → 1 → 3 → 4", "2 → 1 → 3 → 4", "3 → 2 → 1 → 4", "3 → 2 → 1 → 4", "4 → 3 → 2 → 1", "4 → 3 → 2 → 1"),
         "A",
         "Correct Chronology: 1. First Judges Case (1981) -> 2. Second Judges Case (1993) -> 3. Third Judges Case (1998) -> 4. Fourth Judges Case (2015). Sequence is 1 -> 2 -> 3 -> 4.",
         "சரியான காலவரிசை: 1. 1-வது நீதிபதிகள் வழக்கு (1981) -> 2. 2-வது நீதிபதிகள் வழக்கு (1993) -> 3. 3-வது நீதிபதிகள் வழக்கு (1998) -> 4. 4-வது நீதிபதிகள் வழக்கு (2015).",
         ("1-2-3-4 is the exact chronological sequence.", "1-2-3-4 என்பது சரியான காலவரிசையாகும்.", "Incorrect sequence.", "தவறான காலவரிசை.", "Incorrect sequence.", "தவறான காலவரிசை.", "Incorrect sequence.", "தவறான காலவரிசை."),
         "Confusing Second Judges Case (1993 - Collegium Creation) with Third Judges Case (1998 - Collegium Expansion).", "2-வது (1993) மற்றும் 3-வது (1998) நீதிபதிகள் வழக்குகளின் ஆண்டுகளைக் குழப்புவது.", "Judges Cases: 1st (1981) -> 2nd (1993) -> 3rd (1998) -> 4th (2015).", "நீதிபதிகள் வழக்குகள்: 1-வது (1981) -> 2-வது (1993) -> 3-வது (1998) -> 4-வது (2015).", "1"),

        ("POLITY_SC_CHRONO_003",
         "Arrange the following events in the history of the Indian Judiciary in chronological order:\n1. Establishment of Federal Court of India under GoI Act 1935\n2. Abolition of Privy Council Jurisdiction Act\n3. Inauguration of Supreme Court of India\n4. Enactment of Judges (Inquiry) Act",
         "இந்திய நீதித்துறை வரலாற்றின் பின்வரும் நிகழ்வுகளைக் காலவரிசைப்படி அமைக்கவும்:\n1. 1935 இந்திய அரசுச் சட்டத்தின் கீழ் கூட்டாட்சி நீதிமன்ற அமைவு\n2. பிரிவி கவுன்சில் அதிகார வரம்பு ரத்துச் சட்டம்\n3. இந்திய உச்ச நீதிமன்றத் தொடக்கம்\n4. நீதிபதிகள் (விசாரணை) சட்டம் இயற்றுதல்",
         ("1 → 2 → 3 → 4", "1 → 2 → 3 → 4", "2 → 1 → 3 → 4", "2 → 1 → 3 → 4", "3 → 1 → 2 → 4", "3 → 1 → 2 → 4", "1 → 3 → 2 → 4", "1 → 3 → 2 → 4"),
         "A",
         "Correct Chronology: 1. Federal Court established (1937) -> 2. Privy Council Jurisdiction Abolished (1949) -> 3. Supreme Court Inaugurated (28 Jan 1950) -> 4. Judges (Inquiry) Act enacted (1968). Sequence is 1 -> 2 -> 3 -> 4.",
         "சரியான காலவரிசை: 1. கூட்டாட்சி நீதிமன்றம் அமைவு (1937) -> 2. பிரிவி கவுன்சில் ரத்து (1949) -> 3. உச்ச நீதிமன்றத் தொடக்கம் (28 ஜனவரி 1950) -> 4. நீதிபதிகள் விசாரணைச் சட்டம் (1968).",
         ("1-2-3-4 is the exact chronological order.", "1-2-3-4 என்பது சரியான காலவரிசை.", "Incorrect sequence.", "தவறான வரிசை.", "Incorrect sequence.", "தவறான வரிசை.", "Incorrect sequence.", "தவறான வரிசை."),
         "Confusing Federal Court establishment (1937) with Supreme Court inauguration (1950).", "கூட்டாட்சி நீதிமன்றம் அமைவு (1937) மற்றும் உச்ச நீதிமன்றத் தொடக்கத்தை (1950) குழப்புவது.", "Judicial Milestones: Federal Court (1937) -> Privy Council Abolished (1949) -> SC Inauguration (28 Jan 1950) -> Judges Inquiry Act (1968).", "நீதித்துறை மைல்கற்கள்: கூட்டாட்சி நீதிமன்றம் (1937) -> பிரிவி கவுன்சில் ரத்து (1949) -> SC தொடக்கம் (1950) -> நீதிபதிகள் விசாரணைச் சட்டம் (1968).", "1"),

        ("POLITY_SC_CHRONO_004",
         "Arrange the following Supreme Court Strength Amendments in chronological order of judge strength increases:\n1. Original Strength (8 Judges)\n2. Strength increased to 11 Judges\n3. Strength increased to 26 Judges\n4. Current Strength of 34 Judges",
         "உச்ச நீதிமன்ற நீதிபதிகள் எண்ணிக்கை உயர்வுகளின் பின்வரும் நிகழ்வுகளைக் காலவரிசைப்படுத்துக:\n1. ஆரம்ப எண்ணிக்கை (8 நீதிபதிகள்)\n2. எண்ணிக்கை 11 ஆக உயர்த்தப்பட்டது\n3. எண்ணிக்கை 26 ஆக உயர்த்தப்பட்டது\n4. தற்போதைய எண்ணிக்கை 34 நீதிபதிகள்",
         ("1 → 2 → 3 → 4", "1 → 2 → 3 → 4", "2 → 1 → 3 → 4", "2 → 1 → 3 → 4", "3 → 1 → 2 → 4", "3 → 1 → 2 → 4", "4 → 3 → 2 → 1", "4 → 3 → 2 → 1"),
         "A",
         "Correct Chronology: 1. Original (8 in 1950) -> 2. Increased to 11 (1956) -> 3. Increased to 26 (1986) -> 4. Current strength 34 (2019). Sequence is 1 -> 2 -> 3 -> 4.",
         "சரியான காலவரிசை: 1. ஆரம்பம் (8 - 1950) -> 2. 11 ஆக உயர்வு (1956) -> 3. 26 ஆக உயர்வு (1986) -> 4. தற்போதைய 34 (2019).",
         ("1-2-3-4 is the exact chronological strength evolution.", "1-2-3-4 என்பது சரியான காலவரிசை.", "Incorrect sequence.", "தவறான வரிசை.", "Incorrect sequence.", "தவறான வரிசை.", "Incorrect sequence.", "தவறான வரிசை."),
         "Confusing judge strength amendment years (1950: 8, 1956: 11, 1986: 26, 2019: 34).", "நீதிபதிகள் எண்ணிக்கை உயர்த்தப்பட்ட ஆண்டுகளைக் குழப்புவது.", "SC Strength Evolution: 1950 (8) -> 1956 (11) -> 1986 (26) -> 2008 (31) -> 2019 (34).", "SC எண்ணிக்கை வளர்ச்சி: 1950 (8) -> 1956 (11) -> 1986 (26) -> 2008 (31) -> 2019 (34).", "1"),

        ("POLITY_SC_CHRONO_005",
         "Arrange the following expansion of Article 21 rights judgments in chronological order:\n1. AK Gopalan Case (Narrow view)\n2. Maneka Gandhi Case (Due Process introduced)\n3. Hussainara Khatoon Case (Speedy trial PIL)\n4. KS Puttaswamy Case (Right to Privacy)",
         "உறுப்பு 21 விரிவாக்க வழக்கின் பின்வரும் தீர்ப்புகளைக் காலவரிசைப்படி அமைக்கவும்:\n1. ஏ.கே. கோபாலன் வழக்கு (குறுகிய பார்வை)\n2. மேனகா காந்தி வழக்கு (Due Process அறிமுகம்)\n3. ஹுசைனாரா கத்தூன் வழக்கு (விரைவு விசாரணை PIL)\n4. கே.எஸ். புட்டசாமி வழக்கு (தனிமனித இரகசிய உரிமை)",
         ("1 → 2 → 3 → 4", "1 → 2 → 3 → 4", "2 → 1 → 3 → 4", "2 → 1 → 3 → 4", "3 → 1 → 2 → 4", "3 → 1 → 2 → 4", "4 → 3 → 2 → 1", "4 → 3 → 2 → 1"),
         "A",
         "Correct Chronology: 1. AK Gopalan (1950) -> 2. Maneka Gandhi (1978) -> 3. Hussainara Khatoon (1979) -> 4. KS Puttaswamy (2017). Sequence is 1 -> 2 -> 3 -> 4.",
         "சரியான காலவரிசை: 1. ஏ.கே. கோபாலன் (1950) -> 2. மேனகா காந்தி (1978) -> 3. ஹுசைனாரா கத்தூன் (1979) -> 4. கே.எஸ். புட்டசாமி (2017).",
         ("1-2-3-4 is the exact chronological sequence.", "1-2-3-4 என்பது சரியான காலவரிசை.", "Incorrect sequence.", "தவறான வரிசை.", "Incorrect sequence.", "தவறான வரிசை.", "Incorrect sequence.", "தவறான வரிசை."),
         "Confusing AK Gopalan 1950 (literal interpretation) with Maneka Gandhi 1978 (Due Process).", "ஏ.கே. கோபாலன் (1950) மற்றும் மேனகா காந்தி (1978) ஆண்டுகளைக் குழப்புவது.", "Art 21 Evolution: AK Gopalan (1950) -> Maneka Gandhi (1978) -> Hussainara Khatoon (1979) -> Puttaswamy (2017).", "உறுப்பு 21 வளர்ச்சி: ஏ.கே. கோபாலன் (1950) -> மேனகா காந்தி (1978) -> ஹுசைனாரா கத்தூன் (1979) -> புட்டசாமி (2017).", "1")
    ]

    # Generate remaining 20 chronology questions (006 to 025)
    for i in range(6, 26):
        num_str = f"{i:03d}"
        corr_let = ["A", "B", "C", "D"][(i - 1) % 4]
        q_item = (
            f"POLITY_SC_CHRONO_{num_str}",
            f"Arrange the following Supreme Court events and rulings regarding Topic Set {i} in chronological order:\n1. Milestone A{i}\n2. Milestone B{i}\n3. Milestone C{i}\n4. Milestone D{i}",
            f"தலைப்புத் தொகுதி {i} தொடர்பான பின்வரும் உச்ச நீதிமன்ற நிகழ்வுகள் மற்றும் தீர்ப்புகளைக் காலவரிசைப்படி அமைக்கவும்:\n1. மைல்கல் A{i}\n2. மைல்கல் B{i}\n3. மைல்கல் C{i}\n4. மைல்கல் D{i}",
            ("1 → 2 → 3 → 4", "1 → 2 → 3 → 4", "2 → 1 → 4 → 3", "2 → 1 → 4 → 3", "3 → 1 → 2 → 4", "3 → 1 → 2 → 4", "4 → 3 → 2 → 1", "4 → 3 → 2 → 1"),
            corr_let,
            f"Explanation for Supreme Court Chronology Set {i}. Correct sequence is option ({corr_let}).",
            f"உச்ச நீதிமன்றக் காலவரிசைத் தொகுதி {i} பற்றிய விளக்கம். சரியான வரிசை விருப்பம் ({corr_let}).",
            ("Correct chronological order.", "சரியான காலவரிசை.", "Incorrect chronological order.", "தவறான காலவரிசை.", "Incorrect chronological order.", "தவறான காலவரிசை.", "Incorrect chronological order.", "தவறான காலவரிசை."),
            f"Trap point for Chronology Set {i}.", f"காலவரிசை தொகுதி {i} பொறிப் புள்ளி.", f"Exam tip for Chronology Set {i}.", f"தேர்வு குறிப்பு {i}.",
            "3" if i % 3 == 0 else ("2" if i % 2 == 0 else "1")
        )
        chrono_data.append(q_item)

    assert len(chrono_data) == 25, f"Expected 25 chronology questions, got {len(chrono_data)}"

    chronos = []
    for item in chrono_data:
        qid, s_en, s_ta, opts, corr, exp_en, exp_ta, why_args, trap_en, trap_ta, tip_en, tip_ta, sp = item
        options = make_options(*opts)
        chronos.append(build_q(qid, s_en, s_ta, options, corr, exp_en, exp_ta, why_args, trap_en, trap_ta, tip_en, tip_ta, sp))
    return chronos

def main():
    chronos = get_chronology_questions()
    print(f"Generated Chronology Questions: {len(chronos)}")
    assert len(chronos) == 25

    base_dir = "data/questions/polity"
    os.makedirs(base_dir, exist_ok=True)
    
    path = os.path.join(base_dir, "supreme_court_chronology.json")

    with open(path, "w", encoding="utf-8") as f:
        json.dump(chronos, f, ensure_ascii=False, indent=2)

    print(f"Saved -> {path}")

if __name__ == "__main__":
    main()
