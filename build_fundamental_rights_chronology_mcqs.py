# -*- coding: utf-8 -*-
"""
Builder Script for Fundamental Rights 25 Chronology MCQs Repository
Target Path: data/questions/polity/fundamental_rights_chronology.json
"""

import json
import os
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

target_path = Path(r"c:\Users\Home\Desktop\tnpsc_ai\data\questions\polity\fundamental_rights_chronology.json")
target_path.parent.mkdir(parents=True, exist_ok=True)

def make_chrono_q(q_id, difficulty, q_en, q_ta,
                  e1_en, e1_ta, e2_en, e2_ta, e3_en, e3_ta, e4_en, e4_ta,
                  opt_a_code, opt_b_code, opt_c_code, opt_d_code, correct_ans,
                  exp_en, exp_ta, wno_a_en, wno_a_ta, wno_b_en, wno_b_ta, wno_c_en, wno_c_ta, wno_d_en, wno_d_ta,
                  tip_en, tip_ta, rev_en, rev_ta, bloom, est_time, tags):

    codes = [opt_a_code, opt_b_code, opt_c_code, opt_d_code]
    wnos = {
        "A": {"en": wno_a_en, "ta": wno_a_ta},
        "B": {"en": wno_b_en, "ta": wno_b_ta},
        "C": {"en": wno_c_en, "ta": wno_c_ta},
        "D": {"en": wno_d_en, "ta": wno_d_ta}
    }

    letters = ["A", "B", "C", "D"]
    target_idx = letters.index(correct_ans)

    if target_idx != 0:
        codes[0], codes[target_idx] = codes[target_idx], codes[0]
        wnos["A"], wnos[correct_ans] = wnos[correct_ans], wnos["A"]

    opt_a_code, opt_b_code, opt_c_code, opt_d_code = codes

    events = [
        {"id": "1", "en": e1_en, "ta": e1_ta},
        {"id": "2", "en": e2_en, "ta": e2_ta},
        {"id": "3", "en": e3_en, "ta": e3_ta},
        {"id": "4", "en": e4_en, "ta": e4_ta}
    ]

    opts = [
        {"id": "A", "en": opt_a_code, "ta": opt_a_code},
        {"id": "B", "en": opt_b_code, "ta": opt_b_code},
        {"id": "C", "en": opt_c_code, "ta": opt_c_code},
        {"id": "D", "en": opt_d_code, "ta": opt_d_code}
    ]
    opts_en = [opt_a_code, opt_b_code, opt_c_code, opt_d_code]
    opts_ta = [opt_a_code, opt_b_code, opt_c_code, opt_d_code]

    full_q_en = f"{q_en}\n\n1. {e1_en}\n2. {e2_en}\n3. {e3_en}\n4. {e4_en}"
    full_q_ta = f"{q_ta}\n\n1. {e1_ta}\n2. {e2_ta}\n3. {e3_ta}\n4. {e4_ta}"

    return {
        "id": q_id,
        "subject": "Polity",
        "topic": "Fundamental Rights",
        "difficulty": difficulty,
        "question_type": "Chronology",
        "question": {"en": full_q_en, "ta": full_q_ta},
        "events": events,
        "options": opts,
        "correct_answer": correct_ans,
        "explanation": {"en": exp_en, "ta": exp_ta},
        "why_not_others": wnos,
        "tnpsc_tip": {"en": tip_en, "ta": tip_ta},
        "revision_fact": {"en": rev_en, "ta": rev_ta},
        "source_reference": ["M. Laxmikanth - Indian Polity", "NCERT", "Samacheer Kalvi"],
        "bloom_level": bloom,
        "estimated_time_sec": est_time,
        "pyq_similarity": "High",
        "tags": tags,
        "question_en": full_q_en,
        "question_ta": full_q_ta,
        "options_en": opts_en,
        "options_ta": opts_ta,
        "answer": correct_ans.lower(),
        "explanation_en": exp_en,
        "explanation_ta": exp_ta
    }

questions = []

# ==============================================================================
# 25 CHRONOLOGY QUESTIONS (FR_CHRONO_001 to FR_CHRONO_025)
# Target Distribution: A: 6, B: 6, C: 6, D: 7
# Difficulty: Easy: 5 (20%), Medium: 13 (52%), Hard: 7 (28%)
# ==============================================================================

# FR_CHRONO_001 (Easy | Target Ans: A)
questions.append(make_chrono_q(
    "FR_CHRONO_001", "Easy",
    "Arrange the following landmark Supreme Court judgments on Fundamental Rights in correct chronological order (earliest to latest):",
    "அடிப்படை உரிமைகள் தொடர்பான பின்வரும் முக்கிய உச்சநீதிமன்றத் தீர்ப்புகளைச் சரியான காலவரிசைப்படி (முந்தையது முதல் பிந்தையது வரை) வரிசைப்படுத்தவும்:",
    "A.K. Gopalan v. State of Madras (Narrow interpretation of Article 21)", "ஏ.கே. கோபாலன் எதிராக மதராஸ் மாநில வழக்கு (பிரிவு 21-ன் குறுகிய விளக்கம்)",
    "Golaknath v. State of Punjab (Fundamental Rights declared transcendental and unamendable)", "கோலக்நாத் எதிராக பஞ்சாப் மாநில வழக்கு (அடிப்படை உரிமைகள் திருத்த முடியாதவை எனத் தீர்ப்பு)",
    "Kesavananda Bharati v. State of Kerala (Formulation of Basic Structure Doctrine)", "கேசவாநந்த பாரதி எதிராக கேரள மாநில வழக்கு (அடிப்படை அமைப்புக் கோட்பாடு உருவாக்கம்)",
    "Maneka Gandhi v. State of India ('Due Process of Law' integrated into Article 21)", "மேனகா காந்தி எதிராக இந்திய யூனியன் வழக்கு (பிரிவு 21-ல் 'சட்டத்தின் உரிய நடைமுறை' இணைக்கப்பட்டது)",
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "2 -> 3 -> 4 -> 1", "A",
    "Correct Chronological Sequence: 1. A.K. Gopalan Case (1950) -> 2. Golaknath Case (1967) -> 3. Kesavananda Bharati Case (1973) -> 4. Maneka Gandhi Case (1978).",
    "சரியான காலவரிசை: 1. ஏ.கே. கோபாலன் வழக்கு (1950) -> 2. கோலக்நாத் வழக்கு (1967) -> 3. கேசவாநந்த பாரதி வழக்கு (1973) -> 4. மேனகா காந்தி வழக்கு (1978).",
    "Correct. 1950 -> 1967 -> 1973 -> 1978 follows the exact historic sequence of Supreme Court judgments.", "சரி. 1950 -> 1967 -> 1973 -> 1978 உச்சநீதிமன்றத் தீர்ப்புகளின் சரியான காலவரிசையைப் பின்பற்றுகிறது.",
    "Incorrect. Golaknath (1967) occurred after A.K. Gopalan (1950).", "தவறு. கோலக்நாத் (1967) ஏ.கே. கோபாலன் (1950) வழக்கிற்குப் பிறகே வந்தது.",
    "Incorrect. Kesavananda Bharati (1973) was decided after Golaknath (1967).", "தவறு. கேசவாநந்த பாரதி (1973) கோலக்நாத்திற்குப் பிறகே தீர்ப்பளிக்கப்பட்டது.",
    "Incorrect. Maneka Gandhi (1978) came after Kesavananda Bharati (1973).", "தவறு. மேனகா காந்தி (1978) கேசவாநந்த பாரதி வழக்கிற்குப் பிறகே வந்தது.",
    "TNPSC Trap: Do not confuse the order of Golaknath (1967) and Kesavananda Bharati (1973). Golaknath came first.",
    "TNPSC பொறி: கோலக்நாத் (1967) மற்றும் கேசவாநந்த பாரதி (1973) வழக்குகளின் வரிசையைக் குழப்பிக் கொள்ள வேண்டாம். கோலக்நாத் முதலில் வந்தது.",
    "A.K. Gopalan (1950), Golaknath (1967), Kesavananda Bharati (1973), and Maneka Gandhi (1978) form the core judicial trajectory of Part III.",
    "ஏ.கே. கோபாலன் (1950), கோலக்நாத் (1967), கேசவாநந்த பாரதி (1973), மற்றும் மேனகா காந்தி (1978) ஆகியவை பகுதி III-ன் முக்கிய நீதித்துறை பரிணாம வளர்ச்சியாகும்.",
    "Understand", 60, ["Polity", "Fundamental Rights", "Chronology", "Landmark Cases"]
))

# FR_CHRONO_002 (Easy | Target Ans: B)
questions.append(make_chrono_q(
    "FR_CHRONO_002", "Easy",
    "Arrange the following major Constitutional Amendment Acts affecting Fundamental Rights in correct chronological order:",
    "அடிப்படை உரிமைகளைப் பாதிக்கும் பின்வரும் முக்கிய அரசியலமைப்பு திருத்தச் சட்டங்களைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:",
    "1st Constitutional Amendment Act (Added Art 15(4), Art 31A, Art 31B, and Ninth Schedule)", "1-வது அரசியலமைப்பு திருத்தச் சட்டம் (பிரிவு 15(4), 31A, 31B மற்றும் 9-வது அட்டவணை சேர்க்கப்பட்டது)",
    "24th Constitutional Amendment Act (Affirmed Parliament power to amend Fundamental Rights under Art 13 & 368)", "24-வது அரசியலமைப்பு திருத்தச் சட்டம் (பிரிவு 13 & 368-ன் கீழ் அடிப்படை உரிமைகளைத் திருத்தும் நாடாளுமன்ற அதிகாரம் உறுதி செய்யப்பட்டது)",
    "44th Constitutional Amendment Act (Repealed Right to Property from Part III and protected Articles 20 & 21 during Emergency)", "44-வது அரசியலமைப்பு திருத்தச் சட்டம் (சொத்துரிமை பகுதி III-லிருந்து நீக்கப்பட்டு, அவசரநிலையின் போது பிரிவுகள் 20 & 21 பாதுகாக்கக்கப்பட்டன)",
    "86th Constitutional Amendment Act (Inserted Article 21A - Right to Free and Compulsory Education)", "86-வது அரசியலமைப்பு திருத்தச் சட்டம் (பிரிவு 21A - இலவச கட்டாயக் கல்வி உரிமை சேர்க்கப்பட்டது)",
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "2 -> 3 -> 1 -> 4", "B",
    "Correct Chronological Order: 1. 1st CAA (1951) -> 2. 24th CAA (1971) -> 3. 44th CAA (1978) -> 4. 86th CAA (2002).",
    "சரியான காலவரிசை: 1. 1-வது திருத்தம் (1951) -> 2. 24-வது திருத்தம் (1971) -> 3. 44-வது திருத்தம் (1978) -> 4. 86-வது திருத்தம் (2002).",
    "Correct. 1951 -> 1971 -> 1978 -> 2002 represents the exact chronological enactment sequence.", "சரி. 1951 -> 1971 -> 1978 -> 2002 சரியான காலவரிசையைக் குறிக்கிறது.",
    "Incorrect. 24th CAA (1971) came after 1st CAA (1951).", "தவறு. 24-வது திருத்தம் (1971) 1-வது திருத்தத்திற்குப் பின் வந்தது.",
    "Incorrect. 44th CAA (1978) came after 24th CAA (1971).", "தவறு. 44-வது திருத்தம் (1978) 24-வது திருத்தத்திற்குப் பின் வந்தது.",
    "Incorrect. 86th CAA was enacted in 2002, not before 1978.", "தவறு. 86-வது திருத்தம் 2002-ல் இயற்றப்பட்டது, 1978-க்கு முன் அல்ல.",
    "TNPSC Trap: Remember that 44th CAA was in 1978 (Morarji Desai Govt), while 86th CAA was in 2002 (Vajpayee Govt).",
    "TNPSC பொறி: 44-வது திருத்தம் 1978-லும் (மொரார்ஜி தேசாய் அரசு), 86-வது திருத்தம் 2002-லும் (வாஜ்பாய் அரசு) கொண்டுவரப்பட்டன என்பதை நினைவில் கொள்க.",
    "1st CAA (1951), 24th CAA (1971), 44th CAA (1978), and 86th CAA (2002) are pivotal Part III amendments.",
    "1-வது திருத்தம் (1951), 24-வது திருத்தம் (1971), 44-வது திருத்தம் (1978), மற்றும் 86-வது திருத்தம் (2002) ஆகியவை பகுதி III-ன் முக்கிய திருத்தங்களாகும்.",
    "Understand", 60, ["Polity", "Fundamental Rights", "Chronology", "Amendments"]
))

# FR_CHRONO_003 (Medium | Target Ans: C)
questions.append(make_chrono_q(
    "FR_CHRONO_003", "Medium",
    "Arrange the following historical milestones in the evolution of the Right to Education under Part III in correct chronological order:",
    "பகுதி III-ன் கீழ் கல்வி உரிமை பரிணாம வளர்ச்சியின் பின்வரும் வரலாற்றுச் சிறப்புமிக்க நிகழ்வுகளைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:",
    "Mohini Jain v. State of Karnataka Judgment (Declared Right to Education as part of Right to Life under Article 21)", "மோகினி ஜெயின் எதிராக கர்நாடக மாநில வழக்கு தீர்ப்பு (கல்வி உரிமை பிரிவு 21-ன் கீழ் வாழ்வுரிமையின் பகுதி என அறிவிக்கப்பட்டது)",
    "Unni Krishnan v. State of Andhra Pradesh Judgment (Restricted Right to Education to children aged 6 to 14 years)", "உன்னிகிருஷ்ணன் எதிராக ஆந்திரப் பிரதேச மாநில வழக்கு தீர்ப்பு (கல்வி உரிமை 6 முதல் 14 வயதுக் குழந்தைகளுக்குக் கட்டுப்படுத்தப்பட்டது)",
    "86th Constitutional Amendment Act (Inserted Article 21A into Fundamental Rights)", "86-வது அரசியலமைப்பு திருத்தச் சட்டம் (அடிப்படை உரிமைகளில் பிரிவு 21A சேர்க்கப்பட்டது)",
    "Right of Children to Free and Compulsory Education (RTE) Act Enactment", "குழந்தைகளுக்கான இலவச மற்றும் கட்டாயக் கல்வி உரிமைச் சட்டம் (RTE) இயற்றப்பட்டது",
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "2 -> 3 -> 4 -> 1", "C",
    "Correct Chronological Sequence: 1. Mohini Jain Case (1992) -> 2. Unni Krishnan Case (1993) -> 3. 86th CAA (2002) -> 4. RTE Act (2009).",
    "சரியான காலவரிசை: 1. மோகினி ஜெயின் வழக்கு (1992) -> 2. உன்னிகிருஷ்ணன் வழக்கு (1993) -> 3. 86-வது திருத்தம் (2002) -> 4. RTE சட்டம் (2009).",
    "Correct. 1992 -> 1993 -> 2002 -> 2009 perfectly matches the legal trajectory of Article 21A.", "சரி. 1992 -> 1993 -> 2002 -> 2009 பிரிவு 21A-ன் சட்டப் பரிணாம வரிசையைக் சரியாகக் குறிக்கிறது.",
    "Incorrect. Unni Krishnan (1993) was decided after Mohini Jain (1992).", "தவறு. உன்னிகிருஷ்ணன் வழக்கு (1993) மோகினி ஜெயின் வழக்கிற்குப் பிறகே தீர்ப்பளிக்கப்பட்டது.",
    "Incorrect. 86th CAA (2002) was enacted after Unni Krishnan (1993).", "தவறு. 86-வது திருத்தம் (2002) உன்னிகிருஷ்ணன் வழக்கிற்குப் பிறகே இயற்றப்பட்டது.",
    "Incorrect. RTE Act was enacted in 2009, long after 86th CAA 2002.", "தவறு. RTE சட்டம் 2009-ல் இயற்றப்பட்டது, 86-வது திருத்தத்திற்கு நீண்ட காலத்திற்குப் பின்.",
    "TNPSC Trap: Unni Krishnan (1993) refined Mohini Jain (1992) by limiting free education to age 6-14, which was later institutionalized by 86th CAA (2002) and RTE Act (2009).",
    "TNPSC பொறி: உன்னிகிருஷ்ணன் வழக்கு (1993) மோகினி ஜெயின் வழக்கின் (1992) வரம்பற்ற கல்வியை 6-14 வயதாகக் குறைத்தது, பின்னர் இது 86-வது திருத்தம் (2002) மற்றும் RTE சட்டம் (2009) மூலம் நடைமுறைப்படுத்தப்பட்டது.",
    "Mohini Jain (1992) -> Unni Krishnan (1993) -> 86th CAA (2002) -> RTE Act (2009).",
    "மோகினி ஜெயின் (1992) -> உன்னிகிருஷ்ணன் (1993) -> 86-வது திருத்தம் (2002) -> RTE சட்டம் (2009).",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Chronology", "Right to Education", "Article 21A"]
))

# FR_CHRONO_004 (Medium | Target Ans: D)
questions.append(make_chrono_q(
    "FR_CHRONO_004", "Medium",
    "Arrange the following landmark Supreme Court decisions on Reservations under Articles 15 and 16 in correct chronological order:",
    "பிரிவுகள் 15 மற்றும் 16-ன் கீழ் இடஒதுக்கீடு தொடர்பான பின்வரும் முக்கிய உச்சநீதிமன்றத் தீர்ப்புகளைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:",
    "State of Madras v. Champakam Dorairajan (Led to insertion of Article 15(4) by 1st CAA)", "மதராஸ் மாநிலம் எதிராக சண்பகம் துரைராஜன் (1-வது திருத்தத்தின் மூலம் பிரிவு 15(4) சேர்க்க வழிவகுத்தது)",
    "Indra Sawhney v. Union of India (Mandal Case - 50% ceiling cap & Creamy layer exclusion)", "இந்திரா சாவ்னி எதிராக இந்திய யூனியன் (மண்டல் வழக்கு - 50% உச்சவரம்பு & கிரீமி லேயர் நீக்கம்)",
    "M. Nagaraj v. Union of India (Upheld SC/ST promotion reservation subject to quantifiable data conditions)", "எம். நாகராஜ் எதிராக இந்திய யூனியன் (தகுந்த தரவுகளின் அடிப்படையில் SC/ST பதவி உயர்வில் இடஒதுக்கீடு உறுதி செய்யப்பட்டது)",
    "Janhit Abhiyan v. Union of India (Upheld 103rd CAA granting 10% EWS Reservation)", "ஜன்ஹித் அபியான் எதிராக இந்திய யூனியன் (10% EWS இடஒதுக்கீடு வழங்கிய 103-வது திருத்தம் உறுதி செய்யப்பட்டது)",
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "2 -> 3 -> 1 -> 4", "D",
    "Correct Chronological Order: 1. Champakam Dorairajan (1951) -> 2. Indra Sawhney (1992) -> 3. M. Nagaraj (2006) -> 4. Janhit Abhiyan (2022).",
    "சரியான காலவரிசை: 1. சண்பகம் துரைராஜன் (1951) -> 2. இந்திரா சாவ்னி (1992) -> 3. எம். நாகராஜ் (2006) -> 4. ஜன்ஹித் அபியான் (2022).",
    "Correct. 1951 -> 1992 -> 2006 -> 2022 follows the exact historical timeline of reservation jurisprudence.", "சரி. 1951 -> 1992 -> 2006 -> 2022 இடஒதுக்கீடு சட்டப் பரிணாமத்தின் சரியான காலவரிசையைப் பின்பற்றுகிறது.",
    "Incorrect. Indra Sawhney (1992) was decided long after Champakam Dorairajan (1951).", "தவறு. இந்திரா சாவ்னி (1992) சண்பகம் துரைராஜன் வழக்கிற்குப் பின் வந்தது.",
    "Incorrect. M. Nagaraj (2006) came after Indra Sawhney (1992).", "தவறு. எம். நாகராஜ் (2006) இந்திரா சாவ்னி வழக்கிற்குப் பின் வந்தது.",
    "Incorrect. Janhit Abhiyan (2022) is the latest judgment among these four.", "தவறு. ஜன்ஹித் அபியான் (2022) இந்நான்்கில் சமீபத்திய தீர்ப்பாகும்.",
    "TNPSC Trap: Champakam Dorairajan (1951) was the very first reservation case, leading to 1st CAA 1951. Janhit Abhiyan (2022) is the recent 103rd CAA EWS case.",
    "TNPSC பொறி: சண்பகம் துரைராஜன் (1951) முதல் இடஒதுக்கீட்டு வழக்கு, ஜன்ஹித் அபியான் (2022) சமீபத்திய EWS வழக்காகும்.",
    "Champakam Dorairajan (1951) -> Indra Sawhney (1992) -> M. Nagaraj (2006) -> Janhit Abhiyan (2022).",
    "சண்பகம் துரைராஜன் (1951) -> இந்திரா சாவ்னி (1992) -> எம். நாகராஜ் (2006) -> ஜன்ஹித் அபியான் (2022).",
    "Understand", 60, ["Polity", "Fundamental Rights", "Chronology", "Reservations", "Article 15", "Article 16"]
))

# FR_CHRONO_005 (Easy | Target Ans: A)
questions.append(make_chrono_q(
    "FR_CHRONO_005", "Easy",
    "Arrange the following pre-independence and post-independence historical demands for Fundamental Rights in India in correct chronological order:",
    "இந்தியாவில் அடிப்படை உரிமைகளுக்கான சுதந்திரத்திற்கு முந்தைய மற்றும் பிந்தைய வரலாற்றுச் சிறப்புமிக்க கோரிக்கைகளைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:",
    "Motilal Nehru Committee Report (Demanded explicit Bill of Rights for Indian citizens)", "மோதிலால் நேரு குழு அறிக்கை (இந்தியக் குடிமக்களுக்கு தெளிவான அடிப்படை உரிமைகள் கோரப்பட்டது)",
    "Tej Bahadur Sapru Committee Report (Recommended dividing rights into Justiciable and Non-Justiciable categories)", "தேஜ் பகதூர் சப்ரு குழு அறிக்கை (உரிமைகளை நீதிமன்றத்தால் அமல்படுத்தக்கூடியவை மற்றும் அமல்படுத்த முடியாதவை எனப் பிரிக்கப் பரிந்துரைக்கப்பட்டது)",
    "Advisory Committee on Fundamental Rights headed by Sardar Vallabhbhai Patel formed", "சர்தார் வல்லபாய் படேல் தலைமையிலான அடிப்படை உரிமைகள் பற்றிய ஆலோசனைக் குழு அமைக்கப்பட்டது",
    "Enactment and Adoption of Part III Fundamental Rights in the Constitution of India", "இந்திய அரசியலமைப்பில் பகுதி III அடிப்படை உரிமைகள் இயற்றப்பட்டு ஏற்றுக்கொள்ளப்பட்டது",
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "3 -> 1 -> 2 -> 4", "A",
    "Correct Chronological Order: 1. Motilal Nehru Report (1928) -> 2. Sapru Committee Report (1945) -> 3. Advisory Committee formed (1947) -> 4. Part III Enacted (1950).",
    "சரியான காலவரிசை: 1. நேரு அறிக்கை (1928) -> 2. சப்ரு குழு அறிக்கை (1945) -> 3. ஆலோசனைக் குழு உருவாக்கம் (1947) -> 4. பகுதி III இயற்றப்பட்டது (1950).",
    "Correct. 1928 -> 1945 -> 1947 -> 1950 represents the constitutional evolution of Fundamental Rights in India.", "சரி. 1928 -> 1945 -> 1947 -> 1950 இந்தியாவில் அடிப்படை உரிமைகளின் அரசியலமைப்பு பரிணாம வளர்ச்சியைக் குறிக்கிறது.",
    "Incorrect. Sapru Report (1945) came after Motilal Nehru Report (1928).", "தவறு. சப்ரு அறிக்கை (1945) நேரு அறிக்கைக்குப் (1928) பிறகே வந்தது.",
    "Incorrect. Patel Advisory Committee was formed in 1947.", "தவறு. படேல் ஆலோசனைக் குழு 1947-ல் அமைக்கப்பட்டது.",
    "Incorrect. Part III was adopted in 1950, which is the final event here.", "தவறு. பகுதி III 1950-ல் ஏற்றுக்கொள்ளப்பட்டது, இதுவே இறுதி நிகழ்வு.",
    "TNPSC Trap: Sapru Committee (1945) first suggested splitting rights into Part III (Justiciable) and Part IV DPSP (Non-justiciable).",
    "TNPSC பொறி: உரிமைகளை பகுதி III (நீதிமன்றத்தால் அமல்படுத்தக்கூடியவை) மற்றும் பகுதி IV அரசு வழிகாட்டு நெறிமுறைகள் (அமல்படுத்த முடியாதவை) எனப் பிரிக்க முதலில் பரிந்துரைத்தது சப்ரு குழு (1945).",
    "1928 (Nehru Report) -> 1945 (Sapru Report) -> 1947 (Patel Committee) -> 1950 (Part III Enactment).",
    "1928 (நேரு அறிக்கை) -> 1945 (சப்ரு அறிக்கை) -> 1947 (படேல் குழு) -> 1950 (பகுதி III இயற்றல்).",
    "Remember", 60, ["Polity", "Fundamental Rights", "Chronology", "Historical Background"]
))

# FR_CHRONO_006 (Medium | Target Ans: B)
questions.append(make_chrono_q(
    "FR_CHRONO_006", "Medium",
    "Arrange the following events relating to Article 31C and the conflict between Fundamental Rights and DPSPs in correct chronological order:",
    "பிரிவு 31C மற்றும் அடிப்படை உரிமைகள் - அரசு வழிகாட்டு நெறிமுறைகளுக்கு இடையேயான முரண்பாடு தொடர்பான நிகழ்வுகளைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:",
    "25th Constitutional Amendment Act (Inserted Article 31C protecting Art 39(b) & (c) over Articles 14, 19, 31)", "25-வது அரசியலமைப்பு திருத்தச் சட்டம் (பிரிவுகள் 14, 19, 31-ஐ விட பிரிவு 39(b) & (c)-க்கு முன்னுரிமை அளிக்கும் பிரிவு 31C சேர்க்கப்பட்டது)",
    "Kesavananda Bharati Judgment (Struck down 2nd part of Article 31C excluding judicial review)", "கேசவாநந்த பாரதி தீர்ப்பு (நீதிமன்ற மறுஆய்வைத் தடுக்கும் பிரிவு 31C-ன் 2-வது பகுதி ரத்து செய்யப்பட்டது)",
    "42nd Constitutional Amendment Act (Attempted to expand Article 31C protection to ALL DPSPs)", "42-வது அரசியலமைப்பு திருத்தச் சட்டம் (அனைத்து அரசு வழிகாட்டு நெறிமுறைகளுக்கும் பிரிவு 31C பாதுகாப்பை விரிவாக்க முயன்றது)",
    "Minerva Mills Judgment (Struck down expanded Article 31C; restored balance between Part III and Part IV)", "மினர்வா மில்ஸ் தீர்ப்பு (விரிவாக்கப்பட்ட பிரிவு 31C ரத்து செய்யப்பட்டு, பகுதி III மற்றும் பகுதி IV இடையேயான சமநிலை மீட்டெடுக்கப்பட்டது)",
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "3 -> 1 -> 2 -> 4", "B",
    "Correct Chronological Sequence: 1. 25th CAA (1971) -> 2. Kesavananda Bharati (1973) -> 3. 42nd CAA (1976) -> 4. Minerva Mills (1980).",
    "சரியான காலவரிசை: 1. 25-வது திருத்தம் (1971) -> 2. கேசவாநந்த பாரதி (1973) -> 3. 42-வது திருத்தம் (1976) -> 4. மினர்வா மில்ஸ் (1980).",
    "Correct. 1971 -> 1973 -> 1976 -> 1980 represents the exact history of Article 31C.", "சரி. 1971 -> 1973 -> 1976 -> 1980 பிரிவு 31C-ன் சரியான வரலாற்றைக் குறிக்கிறது.",
    "Incorrect. Kesavananda Bharati (1973) examined 25th CAA (1971).", "தவறு. கேசவாநந்த பாரதி (1973) 25-வது திருத்தத்தை (1971) ஆய்வு செய்தது.",
    "Incorrect. 42nd CAA (1976) came after Kesavananda Bharati (1973).", "தவறு. 42-வது திருத்தம் (1976) கேசவாநந்த பாரதி வழக்கிற்குப் பின் வந்தது.",
    "Incorrect. Minerva Mills (1980) was decided in 1980.", "தவறு. மினர்வா மில்ஸ் 1980-ல் தீர்ப்பளிக்கப்பட்டது.",
    "TNPSC Trap: Article 31C was inserted by 25th CAA (1971), modified by Kesavananda Bharati (1973), expanded by 42nd CAA (1976), and struck back to original state by Minerva Mills (1980).",
    "TNPSC பொறி: பிரிவு 31C 25-வது திருத்தத்தால் (1971) கொண்டுவரப்பட்டு, கேசவாநந்த பாரதி (1973) தீர்ப்பால் மாற்றப்பட்டு, 42-வது திருத்தத்தால் (1976) விரிவாக்கப்பட்டு, மினர்வா மில்ஸ் (1980) தீர்ப்பால் பழைய நிலைக்குக் கொண்டுவரப்பட்டது.",
    "25th CAA (1971) -> Kesavananda (1973) -> 42nd CAA (1976) -> Minerva Mills (1980).",
    "25-வது திருத்தம் (1971) -> கேசவாநந்த பாரதி (1973) -> 42-வது திருத்தம் (1976) -> மினர்வா மில்ஸ் (1980).",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Chronology", "Article 31C", "Minerva Mills"]
))

# FR_CHRONO_007 (Medium | Target Ans: C)
questions.append(make_chrono_q(
    "FR_CHRONO_007", "Medium",
    "Arrange the following Supreme Court decisions expanding the scope of Personal Liberty under Article 21 in correct chronological order:",
    "பிரிவு 21-ன் கீழ் தனிநபர் சுதந்திரத்தின் எல்லையை விரிவாக்கிய பின்வரும் உச்சநீதிமன்றத் தீர்ப்புகளைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:",
    "M.H. Hoskot v. State of Maharashtra (Recognized Right to Free Legal Aid under Article 21)", "எம்.எச். ஓஸ்காட் எதிராக மகாராஷ்டிர மாநில வழக்கு (பிரிவு 21-ன் கீழ் இலவச சட்ட உதவி உரிமை அங்கீகரிக்கப்பட்டது)",
    "Hussainara Khatoon v. Home Secretary, Bihar (Recognized Right to Speedy Trial as Fundamental Right)", "ஹுசைனாரா காதுன் எதிராக பீகார் உள்துறைச் செயலர் வழக்கு (வேகமான விசாரணை உரிமை அடிப்படை உரிமையாக அங்கீகரிக்கப்பட்டது)",
    "Subhash Kumar v. State of Bihar (Recognized Right to Pollution-free Water and Air)", "சுபாஷ் குமார் எதிராக பீகார் மாநில வழக்கு (மாசற்ற நீர் மற்றும் காற்று பெறும் உரிமை அங்கீகரிக்கப்பட்டது)",
    "K.S. Puttaswamy v. Union of India (Unanimously declared Right to Privacy as intrinsic Part III right)", "கே.எஸ். புட்டசுவாமி எதிராக இந்திய யூனியன் வழக்கு (தனியுரிமை பகுதி III-ன் உள்ளார்ந்த உரிமை என ஏகமனதாக அறிவிக்கப்பட்டது)",
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "2 -> 4 -> 1 -> 3", "C",
    "Correct Chronological Order: 1. M.H. Hoskot (1978) -> 2. Hussainara Khatoon (1979) -> 3. Subhash Kumar (1991) -> 4. K.S. Puttaswamy (2017).",
    "சரியான காலவரிசை: 1. எம்.எச். ஓஸ்காட் (1978) -> 2. ஹுசைனாரா காதுன் (1979) -> 3. சுபாஷ் குமார் (1991) -> 4. கே.எஸ். புட்டசுவாமி (2017).",
    "Correct. 1978 -> 1979 -> 1991 -> 2017 accurately traces the expansion of Article 21 rights.", "சரி. 1978 -> 1979 -> 1991 -> 2017 பிரிவு 21 உரிமைகள் விரிவாக்கத்தின் சரியான காலவரிசையைக் குறிக்கிறது.",
    "Incorrect. Hussainara Khatoon (1979) was decided after M.H. Hoskot (1978).", "தவறு. ஹுசைனாரா காதுன் (1979) எம்.எச். ஓஸ்காட் வழக்கிற்குப் (1978) பிறகே தீர்ப்பளிக்கப்பட்டது.",
    "Incorrect. Subhash Kumar (1991) came after Hussainara Khatoon (1979).", "தவறு. சுபாஷ் குமார் (1991) ஹுசைனாரா காதுன் வழக்கிற்குப் பின் வந்தது.",
    "Incorrect. Puttaswamy (2017) is the latest landmark judgment in this list.", "தவறு. புட்டசுவாமி (2017) இப்பட்டியலில் சமீபத்திய தீர்ப்பாகும்.",
    "TNPSC Trap: Hoskot (1978 - Legal Aid) and Hussainara Khatoon (1979 - Speedy Trial) immediately followed the post-Maneka Gandhi (1978) expansion of Article 21.",
    "TNPSC பொறி: ஓஸ்காட் (1978 - சட்ட உதவி) மற்றும் ஹுசைனாரா காதுன் (1979 - வேகமான விசாரணை) வழக்குகள் மேனகா காந்தி (1978) வழக்கிற்குப் பின் உடனடியாக வந்தன.",
    "1978 (Hoskot) -> 1979 (Hussainara) -> 1991 (Subhash Kumar) -> 2017 (Puttaswamy).",
    "1978 (ஓஸ்காட்) -> 1979 (ஹுசைனாரா) -> 1991 (சுபாஷ் குமார்) -> 2017 (புட்டசுவாமி).",
    "Understand", 60, ["Polity", "Fundamental Rights", "Chronology", "Article 21", "Right to Privacy"]
))

# FR_CHRONO_008 (Hard | Target Ans: D)
questions.append(make_chrono_q(
    "FR_CHRONO_008", "Hard",
    "Arrange the following constitutional developments regarding the Right to Property (Article 31) in correct chronological order:",
    "சொத்துரிமை (பிரிவு 31) தொடர்பான பின்வரும் அரசியலமைப்பு திருத்தங்களைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:",
    "1st CAA (Inserted Article 31A and Article 31B to protect agrarian reform laws)", "1-வது திருத்தம் (வேளாண் சீர்திருத்தச் சட்டங்களைப் பாதுகாக்க பிரிவு 31A மற்றும் 31B சேர்க்கப்பட்டது)",
    "4th CAA (Made compensation for compulsory acquisition of property non-justiciable in courts)", "4-வது திருத்தம் (சொத்து கட்டாயக் கையகப்படுத்துதலுக்கான இழப்பீட்டை நீதிமன்றங்களில் கேள்வி கேட்க முடியாததாக்கியது)",
    "25th CAA (Substituted the word 'compensation' with the word 'amount' in Article 31(2))", "25-வது திருத்தம் (பிரிவு 31(2)-ல் 'இழப்பீடு' என்ற வார்த்தைக்குப் பதிலாக 'தொகை' என்ற வார்த்தை மாற்றப்பட்டது)",
    "44th CAA (Abolished Right to Property as a Fundamental Right; deleted Art 19(1)(f) & Art 31 and created Art 300A)", "44-வது திருத்தம் (சொத்துரிமை அடிப்படை உரிமையிலிருந்து நீக்கப்பட்டு பிரிவு 19(1)(f) & 31 ரத்து செய்யப்பட்டு பிரிவு 300A உருவாக்கப்பட்டது)",
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "2 -> 3 -> 1 -> 4", "D",
    "Correct Chronological Order: 1. 1st CAA (1951) -> 2. 4th CAA (1955) -> 3. 25th CAA (1971) -> 4. 44th CAA (1978).",
    "சரியான காலவரிசை: 1. 1-வது திருத்தம் (1951) -> 2. 4-வது திருத்தம் (1955) -> 3. 25-வது திருத்தம் (1971) -> 4. 44-வது திருத்தம் (1978).",
    "Correct. 1951 -> 1955 -> 1971 -> 1978 perfectly traces the abolition trajectory of Article 31.", "சரி. 1951 -> 1955 -> 1971 -> 1978 பிரிவு 31 நீக்கப்பட்டதன் சரியான வரலாற்று வரிசையைக் குறிக்கிறது.",
    "Incorrect. 4th CAA (1955) came after 1st CAA (1951).", "தவறு. 4-வது திருத்தம் (1955) 1-வது திருத்தத்திற்குப் பின் வந்தது.",
    "Incorrect. 25th CAA (1971) came after 4th CAA (1955).", "தவறு. 25-வது திருத்தம் (1971) 4-வது திருத்தத்திற்குப் பின் வந்தது.",
    "Incorrect. 44th CAA (1978) was the final amendment abolishing property as FR.", "தவறு. 44-வது திருத்தம் (1978) சொத்துரிமையை அடிப்படை உரிமையிலிருந்து நீக்கிய இறுதித் திருத்தமாகும்.",
    "TNPSC Trap: 1st CAA (1951) added 31A/31B, 4th CAA (1955) limited compensation judicial review, 25th CAA (1971) changed 'compensation' to 'amount', and 44th CAA (1978) deleted Art 31 completely.",
    "TNPSC பொறி: 1-வது திருத்தம் (1951) 31A/31B-ஐ சேர்த்தது, 4-வது திருத்தம் (1955) இழப்பீட்டு மறுஆய்வைக் கட்டுப்படுத்தியது, 25-வது திருத்தம் (1971) 'இழப்பீடு' என்பதை 'தொகை' என மாற்றியது, 44-வது திருத்தம் (1978) பிரிவு 31-ஐ முற்றிலும் நீக்கியது.",
    "1st CAA (1951) -> 4th CAA (1955) -> 25th CAA (1971) -> 44th CAA (1978).",
    "1-வது திருத்தம் (1951) -> 4-வது திருத்தம் (1955) -> 25-வது திருத்தம் (1971) -> 44-வது திருத்தம் (1978).",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Chronology", "Right to Property", "Article 31", "Article 300A"]
))

# FR_CHRONO_009 (Easy | Target Ans: A)
questions.append(make_chrono_q(
    "FR_CHRONO_009", "Easy",
    "Arrange the following Constitutional Amendment Acts relating to Part III in REVERSE chronological order (latest to earliest):",
    "பகுதி III தொடர்பான பின்வரும் அரசியலமைப்பு திருத்தச் சட்டங்களை தலைகீழ் காலவரிசைப்படி (சமீபத்தியது முதல் பழமையானது வரை) வரிசைப்படுத்தவும்:",
    "103rd CAA (Provided 10% Reservation for Economically Weaker Sections under Art 15(6) and 16(6))", "103-வது திருத்தம் (பிரிவு 15(6) மற்றும் 16(6)-ன் கீழ் பொருளாதாரத்தில் பின்தங்கிய பிரிவினருக்கு 10% இடஒதுக்கீடு)",
    "86th CAA (Inserted Article 21A - Right to Free and Compulsory Education)", "86-வது திருத்தம் (பிரிவு 21A - இலவச கட்டாயக் கல்வி உரிமை சேர்க்கப்பட்டது)",
    "44th CAA (Prohibited suspension of Articles 20 & 21 during National Emergency)", "44-வது திருத்தம் (தேசிய அவசரநிலையின் போது பிரிவுகள் 20 & 21 இடைநிறுத்தப்படுவது தடை செய்யப்பட்டது)",
    "1st CAA (Added Ninth Schedule and Article 15(4) Special provisions for Backward Classes)", "1-வது திருத்தம் (9-வது அட்டவணை மற்றும் பிற்படுத்தப்பட்டோருக்கான பிரிவு 15(4) சிறப்பு விதிகள் சேர்க்கப்பட்டது)",
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "4 -> 3 -> 2 -> 1", "A",
    "Correct REVERSE Chronological Sequence (Latest to Earliest): 1. 103rd CAA (2019) -> 2. 86th CAA (2002) -> 3. 44th CAA (1978) -> 4. 1st CAA (1951).",
    "சரியான தலைகீழ் காலவரிசை (சமீபத்தியது முதல் பழமையானது வரை): 1. 103-வது திருத்தம் (2019) -> 2. 86-வது திருத்தம் (2002) -> 3. 44-வது திருத்தம் (1978) -> 4. 1-வது திருத்தம் (1951).",
    "Correct. 2019 -> 2002 -> 1978 -> 1951 represents exact reverse chronological order.", "சரி. 2019 -> 2002 -> 1978 -> 1951 சரியான தலைகீழ் காலவரிசையைக் குறிக்கிறது.",
    "Incorrect. 103rd CAA (2019) is the latest, so it must come first in reverse order.", "தவறு. 103-வது திருத்தம் (2019) சமீபத்தியது, எனவே தலைகீழ் வரிசையில் இது முதலில் வர வேண்டும்.",
    "Incorrect. 86th CAA was 2002, which comes after 2019 in reverse order.", "தவறு. 86-வது திருத்தம் 2002, தலைகீழ் வரிசையில் 2019-க்கு அடுத்து வர வேண்டும்.",
    "Incorrect. 4 -> 3 -> 2 -> 1 is normal chronological order (earliest to latest), not reverse order.", "தவறு. 4 -> 3 -> 2 -> 1 என்பது சாதாரண காலவரிசையாகும், தலைகீழ் வரிசை அல்ல.",
    "TNPSC Trap: Read the question carefully! The question explicitly demands REVERSE chronological order (latest to earliest).",
    "TNPSC பொறி: வினவைக் கவனமாகப் படிக்கவும்! கேள்வி தலைகீழ் காலவரிசையைக் (சமீபத்தியது முதல் பழமையானது வரை) தெளிவாகக் கேட்கிறது.",
    "2019 (103rd) -> 2002 (86th) -> 1978 (44th) -> 1951 (1st).",
    "2019 (103-வது) -> 2002 (86-வது) -> 1978 (44-வது) -> 1951 (1-வது).",
    "Remember", 60, ["Polity", "Fundamental Rights", "Chronology", "Amendments", "Reverse Chronology"]
))

# FR_CHRONO_010 (Medium | Target Ans: B)
questions.append(make_chrono_q(
    "FR_CHRONO_010", "Medium",
    "Arrange the following judicial decisions regarding Parliament power to amend Fundamental Rights under Article 368 in correct chronological order:",
    "பிரிவு 368-ன் கீழ் அடிப்படை உரிமைகளைத் திருத்தும் நாடாளுமன்ற அதிகாரம் தொடர்பான நீதித்துறைத் தீர்ப்புகளைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:",
    "Shankari Prasad v. Union of India (Upheld 1st CAA & Parliament power to amend Part III including FRs)", "சங்கரி பிரசாத் எதிராக இந்திய யூனியன் (1-வது திருத்தம் மற்றும் அடிப்படை உரிமைகளைத் திருத்தும் நாடாளுமன்ற அதிகாரம் உறுதி செய்யப்பட்டது)",
    "Sajjan Singh v. State of Rajasthan (Upheld 17th CAA & reaffirmed Parliament power to amend FRs)", "சஜ்ஜன் சிங் எதிராக ராஜஸ்தான் மாநில வழக்கு (17-வது திருத்தம் மற்றும் நாடாளுமன்ற திருத்தும் அதிகாரம் மீண்டும் உறுதி செய்யப்பட்டது)",
    "Golaknath v. State of Punjab (Overruled Shankari Prasad & Sajjan Singh; declared FRs unamendable)", "கோலக்நாத் எதிராக பஞ்சாப் மாநில வழக்கு (சங்கரி பிரசாத் & சஜ்ஜன் சிங் தீர்ப்புகள் ரத்து செய்யப்பட்டு, அடிப்படை உரிமைகள் திருத்த முடியாதவை என அறிவிக்கப்பட்டது)",
    "Kesavananda Bharati v. State of Kerala (Overruled Golaknath; held FRs amendable subject to Basic Structure)", "கேசவாநந்த பாரதி எதிராக കേരള மாநில வழக்கு (கோலக்நாத் தீர்ப்பு ரத்து செய்யப்பட்டு, அடிப்படை அமைப்பிற்கு உட்பட்டு உரிமைகளைத் திருத்தலாம் எனக் கூறப்பட்டது)",
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "3 -> 1 -> 2 -> 4", "B",
    "Correct Chronological Sequence: 1. Shankari Prasad (1951) -> 2. Sajjan Singh (1965) -> 3. Golaknath (1967) -> 4. Kesavananda Bharati (1973).",
    "சரியான காலவரிசை: 1. சங்கரி பிரசாத் (1951) -> 2. சஜ்ஜன் சிங் (1965) -> 3. கோலக்நாத் (1967) -> 4. கேசவாநந்த பாரதி (1973).",
    "Correct. 1951 -> 1965 -> 1967 -> 1973 accurately outlines the amendability jurisprudence timeline.", "சரி. 1951 -> 1965 -> 1967 -> 1973 திருத்தும் அதிகார நீதித்துறைப் பயணத்தின் சரியான காலவரிசையைக் குறிக்கிறது.",
    "Incorrect. Sajjan Singh (1965) came after Shankari Prasad (1951).", "தவறு. சஜ்ஜன் சிங் (1965) சங்கரி பிரசாத் வழக்கிற்குப் (1951) பின் வந்தது.",
    "Incorrect. Golaknath (1967) came after Sajjan Singh (1965).", "தவறு. கோலக்நாத் (1967) சஜ்ஜன் சிங் வழக்கிற்குப் பின் வந்தது.",
    "Incorrect. Shankari Prasad was 1951, which must be the first event.", "தவறு. சங்கரி பிரசாத் 1951, இதுவே முதல் நிகழ்வாக இருக்க வேண்டும்.",
    "TNPSC Trap: Shankari Prasad (1951) and Sajjan Singh (1965) allowed FR amendments; Golaknath (1967) banned FR amendments; Kesavananda (1973) allowed FR amendments EXCEPT basic structure.",
    "TNPSC பொறி: சங்கரி பிரசாத் (1951) மற்றும் சஜ்ஜன் சிங் (1965) திருத்தத்தை அனுமதித்தன; கோலக்நாத் (1967) தடை செய்தது; கேசவாநந்த பாரதி (1973) அடிப்படை அமைப்பைத் தவிர திருத்த அனுமதித்தது.",
    "Shankari Prasad (1951) -> Sajjan Singh (1965) -> Golaknath (1967) -> Kesavananda (1973).",
    "சங்கரி பிரசாத் (1951) -> சஜ்ஜன் சிங் (1965) -> கோலக்நாத் (1967) -> கேசவாநந்த பாரதி (1973).",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Chronology", "Amendability", "Kesavananda Bharati"]
))

# FR_CHRONO_011 (Medium | Target Ans: C)
questions.append(make_chrono_q(
    "FR_CHRONO_011", "Medium",
    "Arrange the following milestones in the history of Freedom of Speech and Expression (Article 19(1)(a)) in correct chronological order:",
    "பேச்சு மற்றும் கருத்துச் சுதந்திரத்தின் (பிரிவு 19(1)(a)) வரலாற்றின் பின்வரும் மைல்கற்களைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:",
    "Romesh Thappar v. State of Madras (Established that Freedom of Speech includes Freedom of Circulation of newspapers)", "ரமேஷ் தாப்பர் எதிராக மதராஸ் மாநில வழக்கு (பேச்சுச் சுதந்திரம் என்பது செய்தித்தாள்களின் விநியோக சுதந்திரத்தையும் உள்ளடக்கியது என நிறுவப்பட்டது)",
    "1st CAA (Added 'Public Order', 'Incitement to an Offence', and 'Friendly relations with foreign States' restrictions to Art 19(2))", "1-வது திருத்தம் (பிரிவு 19(2)-ல் 'பொது அமைதி', 'குற்றத்திற்குத் தூண்டுதல்', 'அன்னிய நாடுகளுடனான நட்பு' ஆகிய கட்டுப்பாடுகள் சேர்க்கப்பட்டன)",
    "16th CAA (Added 'Sovereignty and Integrity of India' restriction to Article 19(2))", "16-வது திருத்தம் (பிரிவு 19(2)-ல் 'இந்தியாவின் இறையாண்மை மற்றும் ஒருமைப்பாடு' என்ற கட்டுப்பாடு சேர்க்கப்பட்டது)",
    "Shreya Singhal v. Union of India (Struck down Section 66A of Information Technology Act as unconstitutional under Art 19(1)(a))", "ஷ்ரேயா சிங்கால் எதிராக இந்திய யூனியன் வழக்கு (தகவல் தொழில்நுட்பச் சட்டத்தின் பிரிவு 66A அரசியலமைப்பிற்கு எதிரானது என ரத்து செய்யப்பட்டது)",
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "2 -> 3 -> 4 -> 1", "C",
    "Correct Chronological Sequence: 1. Romesh Thappar (May 1950) -> 2. 1st CAA (1951) -> 3. 16th CAA (1963) -> 4. Shreya Singhal (2015).",
    "சரியான காலவரிசை: 1. ரமேஷ் தாப்பர் (மே 1950) -> 2. 1-வது திருத்தம் (1951) -> 3. 16-வது திருத்தம் (1963) -> 4. ஷ்ரேயா சிங்கால் (2015).",
    "Correct. 1950 -> 1951 -> 1963 -> 2015 accurately represents Article 19 freedom of speech milestones.", "சரி. 1950 -> 1951 -> 1963 -> 2015 பிரிவு 19 பேச்சுச் சுதந்திர மைல்கற்களைச் சரியாகக் குறிக்கிறது.",
    "Incorrect. 1st CAA (1951) was enacted partly in response to Romesh Thappar (1950).", "தவறு. 1-வது திருத்தம் (1951) ரமேஷ் தாப்பர் வழக்கிற்குப் (1950) பதிலளிக்கும் விதமாக இயற்றப்பட்டது.",
    "Incorrect. 16th CAA (1963) came after 1st CAA (1951).", "தவறு. 16-வது திருத்தம் (1963) 1-வது திருத்தத்திற்குப் பின் வந்தது.",
    "Incorrect. Shreya Singhal was decided in 2015.", "தவறு. ஷ்ரேயா சிங்கால் வழக்கு 2015-ல் தீர்ப்பளிக்கப்பட்டது.",
    "TNPSC Trap: Romesh Thappar (1950) led to the 1st CAA (1951) adding public order restrictions. 16th CAA (1963) added sovereignty & integrity following the 1962 China War.",
    "TNPSC பொறி: ரமேஷ் தாப்பர் வழக்கு (1950) 1-வது திருத்தம் (1951) மூலம் பொது அமைதிக் கட்டுப்பாட்டைச் சேர்க்க வழிவகுத்தது. 16-வது திருத்தம் (1963) 1962 சீனப் போருக்குப் பின் இறையாண்மை & ஒருமைப்பாட்டைச் சேர்த்தது.",
    "Romesh Thappar (1950) -> 1st CAA (1951) -> 16th CAA (16th CAA 1963) -> Shreya Singhal (2015).",
    "ரமேஷ் தாப்பர் (1950) -> 1-வது திருத்தம் (1951) -> 16-வது திருத்தம் (1963) -> ஷ்ரேயா சிங்கால் (2015).",
    "Understand", 60, ["Polity", "Fundamental Rights", "Chronology", "Article 19", "Freedom of Speech"]
))

# FR_CHRONO_012 (Hard | Target Ans: D)
questions.append(make_chrono_q(
    "FR_CHRONO_012", "Hard",
    "Arrange the following judicial and legislative developments on SC/ST Promotion Reservations under Article 16(4A) in correct chronological order:",
    "பிரிவு 16(4A)-ன் கீழ் SC/ST பதவி உயர்வு இடஒதுக்கீடு தொடர்பான பின்வரும் நீதிமன்ற மற்றும் நாடாளுமன்ற நிகழ்வுகளைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:",
    "Indra Sawhney Judgment (Ruled that reservation under Article 16(4) applies ONLY to initial appointment, NOT to promotion)", "இந்திரா சாவ்னி தீர்ப்பு (பிரிவு 16(4)-ன் கீழ் இடஒதுக்கீடு ஆரம்ப நியமனத்திற்கு மட்டுமே பொருந்தும், பதவி உயர்வுக்குப் பொருந்தாது எனத் தீர்ப்பளிக்கப்பட்டது)",
    "77th Constitutional Amendment Act (Inserted Article 16(4A) permitting reservation in promotion for SCs and STs)", "77-வது திருத்தம் (SC மற்றும் ST பிரிவினருக்கு பதவி உயர்வில் இடஒதுக்கீடு வழங்க பிரிவு 16(4A) சேர்க்கப்பட்டது)",
    "M. Nagaraj Judgment (Upheld Article 16(4A) subject to 3 conditions: Backwardness, Inadequacy of representation, Administrative efficiency)", "எம். நாகராஜ் தீர்ப்பு (பின்தங்கிய நிலை, போதிய பிரதிநிதித்துவமின்மை, நிர்வாகத் திறமை ஆகிய 3 நிபந்தனைகளுக்கு உட்பட்டு பிரிவு 16(4A) உறுதி செய்யப்பட்டது)",
    "Jarnail Singh v. Lachhmi Narain Gupta Judgment (Extended Creamy Layer exclusion to SC/ST promotions and removed backwardness data collection condition)", "ஜர்னைல் சிங் எதிராக லக்ஷ்மி நாராயண் குப்தா தீர்ப்பு (SC/ST பதவி உயர்வுக்கும் கிரீமி லேயர் நீக்கம் நீட்டிக்கப்பட்டது மற்றும் பின்தங்கிய தரவு சேகரிப்பு நிபந்தனை நீக்கப்பட்டது)",
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "2 -> 3 -> 1 -> 4", "D",
    "Correct Chronological Order: 1. Indra Sawhney (1992) -> 2. 77th CAA (1995) -> 3. M. Nagaraj (2006) -> 4. Jarnail Singh (2018).",
    "சரியான காலவரிசை: 1. இந்திரா சாவ்னி (1992) -> 2. 77-வது திருத்தம் (1995) -> 3. எம். நாகராஜ் (2006) -> 4. ஜர்னைல் சிங் (2018).",
    "Correct. 1992 -> 1995 -> 2006 -> 2018 represents the exact evolution of promotion reservation jurisprudence.", "சரி. 1992 -> 1995 -> 2006 -> 2018 பதவி உயர்வு இடஒதுக்கீடு சட்டப் பரிணாமத்தின் சரியான காலவரிசையைக் குறிக்கிறது.",
    "Incorrect. 77th CAA (1995) was enacted to override Indra Sawhney (1992) ruling on promotion reservation.", "தவறு. 77-வது திருத்தம் (1995) இந்திரா சாவ்னி (1992) தீர்ப்பை மாற்றியமைக்கவே இயற்றப்பட்டது.",
    "Incorrect. M. Nagaraj (2006) examined the validity of 77th CAA (1995).", "தவறு. எம். நாகராஜ் (2006) 77-வது திருத்தத்தின் (1995) செல்லுபடியாகும் தன்மையை ஆய்வு செய்தது.",
    "Incorrect. Jarnail Singh (2018) re-examined M. Nagaraj (2006) judgment.", "தவறு. ஜர்னைல் சிங் (2018) எம். நாகராஜ் (2006) தீர்ப்பை மறுஆய்வு செய்தது.",
    "TNPSC Trap: Indra Sawhney (1992) banned promotion reservation, leading to 77th CAA (1995). Nagaraj (2006) validated 77th CAA with conditions. Jarnail Singh (2018) modified Nagaraj.",
    "TNPSC பொறி: இந்திரா சாவ்னி (1992) பதவி உயர்வு இடஒதுக்கீட்டைத் தடை செய்தது, இது 77-வது திருத்தத்திற்கு (1995) வழிவகுத்தது. நாகராஜ் (2006) அதை நிபந்தனைகளுடன் அனுமதித்தது. ஜர்னைல் சிங் (2018) அதை மாற்றியமைத்தது.",
    "Indra Sawhney (1992) -> 77th CAA (1995) -> M. Nagaraj (2006) -> Jarnail Singh (2018).",
    "இந்திரா சாவ்னி (1992) -> 77-வது திருத்தம் (1995) -> எம். நாகராஜ் (2006) -> ஜர்னைல் சிங் (2018).",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Chronology", "Article 16", "Reservation in Promotion"]
))

# FR_CHRONO_013 (Medium | Target Ans: A)
questions.append(make_chrono_q(
    "FR_CHRONO_013", "Medium",
    "Arrange the following events regarding the Ninth Schedule and its immunity from Fundamental Rights judicial review in correct chronological order:",
    "9-வது அட்டவணை மற்றும் அடிப்படை உரிமைகள் நீதித்துறை மறுஆய்விலிருந்தான அதன் பாதுகாப்பு தொடர்பான நிகழ்வுகளைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:",
    "Creation of Ninth Schedule and Article 31B by 1st Constitutional Amendment Act", "1-வது அரசியலமைப்பு திருத்தச் சட்டம் மூலம் 9-வது அட்டவணை மற்றும் பிரிவு 31B உருவாக்கப்பட்டது",
    "Kesavananda Bharati Judgment cutoff date for Ninth Schedule protection (April 24, 1973)", "9-வது அட்டவணை பாதுகாப்பிற்கான கேசவாநந்த பாரதி தீர்ப்பின் எல்லை நாள் (ஏப்ரல் 24, 1973)",
    "Waman Rao v. Union of India Judgment (Reaffirmed April 24, 1973 as cutoff date for Ninth Schedule review)", "வாமன் ராவ் எதிராக இந்திய யூனியன் தீர்ப்பு (9-வது அட்டவணை மறுஆய்விற்கு ஏப்ரல் 24, 1973 எல்லை நாளாக மீண்டும் உறுதி செய்யப்பட்டது)",
    "I.R. Coelho v. State of Tamil Nadu Judgment (Ruled Ninth Schedule laws inserted post-April 24, 1973 are subject to Judicial Review)", "ஐ.ஆர். கோயல்ஹோ எதிராக தமிழ்நாடு மாநில தீர்ப்பு (ஏப்ரல் 24, 1973-க்குப் பின் 9-வது அட்டவணையில் சேர்க்கப்பட்ட சட்டங்கள் நீதித்துறை மறுஆய்விற்கு உட்பட்டவை எனத் தீர்ப்பளிக்கப்பட்டது)",
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "3 -> 1 -> 2 -> 4", "A",
    "Correct Chronological Sequence: 1. 1st CAA (1951) -> 2. Kesavananda Bharati Cutoff Date (April 24, 1973) -> 3. Waman Rao Case (1981) -> 4. I.R. Coelho Case (2007).",
    "சரியான காலவரிசை: 1. 1-வது திருத்தம் (1951) -> 2. கேசவாநந்த பாரதி எல்லை நாள் (ஏப்ரல் 24, 1973) -> 3. வாமன் ராவ் வழக்கு (1981) -> 4. ஐ.ஆர். கோயல்ஹோ வழக்கு (2007).",
    "Correct. 1951 -> 1973 -> 1981 -> 2007 accurately follows Ninth Schedule judicial review history.", "சரி. 1951 -> 1973 -> 1981 -> 2007 9-வது அட்டவணை மறுஆய்வு வரலாற்றின் சரியான காலவரிசையைப் பின்பற்றுகிறது.",
    "Incorrect. Kesavananda cutoff date (1973) came after 1st CAA creation of Ninth Schedule (1951).", "தவறு. கேசவாநந்த எல்லை நாள் (1973) 1-வது திருத்தத்திற்குப் (1951) பிறகே வந்தது.",
    "Incorrect. Waman Rao was decided in 1981.", "தவறு. வாமன் ராவ் 1981-ல் தீர்ப்பளிக்கப்பட்டது.",
    "Incorrect. I.R. Coelho was decided in 2007.", "தவறு. ஐ.ஆர். கோயல்ஹோ 2007-ல் தீர்ப்பளிக்கப்பட்டது.",
    "TNPSC Trap: Laws added to Ninth Schedule BEFORE April 24, 1973 are immune from review; laws added AFTER April 24, 1973 can be challenged if they violate Basic Structure (I.R. Coelho 2007).",
    "TNPSC பொறி: ஏப்ரல் 24, 1973-க்கு முன் 9-வது அட்டவணையில் சேர்க்கப்பட்ட சட்டங்கள் பாதுகாப்பானவை; அதற்குப் பின் சேர்க்கப்பட்ட சட்டங்கள் அடிப்படை அமைப்பை மீறினால் கேள்வி கேட்கப்படலாம் (ஐ.ஆர். கோயல்ஹோ 2007).",
    "1st CAA (1951) -> Kesavananda Cutoff (1973) -> Waman Rao (1981) -> I.R. Coelho (2007).",
    "1-வது திருத்தம் (1951) -> கேசவாநந்த எல்லை நாள் (1973) -> வாமன் ராவ் (1981) -> ஐ.ஆர். கோயல்ஹோ (2007).",
    "Understand", 60, ["Polity", "Fundamental Rights", "Chronology", "Ninth Schedule", "IR Coelho Case"]
))

# FR_CHRONO_014 (Medium | Target Ans: B)
questions.append(make_chrono_q(
    "FR_CHRONO_014", "Medium",
    "Arrange the following events regarding Emergency and Fundamental Rights in correct chronological order:",
    "தேசிய அவசரநிலை மற்றும் அடிப்படை உரிமைகள் தொடர்பான நிகழ்வுகளைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:",
    "ADM Jabalpur v. Shivkant Shukla Case (Habeas Corpus Case - SC upheld suspension of Art 21 right during Emergency)", "ஏடிஎம் நபல்பூர் எதிராக சிவகாந்த் சுக்லா வழக்கு (ஹேபியஸ் கார்பஸ் வழக்கு - அவசரநிலையின் போது பிரிவு 21 இடைநிறுத்தம் செல்லுபடி எனத் தீர்ப்பு)",
    "42nd Constitutional Amendment Act (Attempted to reduce judicial remedies during Emergency)", "42-வது அரசியலமைப்பு திருத்தச் சட்டம் (அவசரநிலையின் போது நீதித்துறை தீர்வுகளைக் குறைக்க முயன்றது)",
    "44th Constitutional Amendment Act (Prohibited suspension of Article 20 and Article 21 under any circumstances)", "44-வது அரசியலமைப்பு திருத்தச் சட்டம் (எந்தச் சூழ்நிலையிலும் பிரிவுகள் 20 மற்றும் 21 இடைநிறுத்தப்படுவதைத் தடை செய்தது)",
    "Minerva Mills Judgment (Reaffirmed Judicial Review as Basic Structure during Emergency)", "மினர்வா மில்ஸ் தீர்ப்பு (அவசரநிலையின் போதும் நீதித்துறை மறுஆய்வு அடிப்படை அமைப்பு என மீண்டும் உறுதி செய்யப்பட்டது)",
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "3 -> 1 -> 2 -> 4", "B",
    "Correct Chronological Sequence: 1. ADM Jabalpur (April 1976) -> 2. 42nd CAA (Nov 1976) -> 3. 44th CAA (1978) -> 4. Minerva Mills (1980).",
    "சரியான காலவரிசை: 1. ஏடிஎம் நபல்பூர் (ஏப்ரல் 1976) -> 2. 42-வது திருத்தம் (நவம்பர் 1976) -> 3. 44-வது திருத்தம் (1978) -> 4. மினர்வா மில்ஸ் (1980).",
    "Correct. April 1976 -> Nov 1976 -> 1978 -> 1980 represents the exact Emergency legal timeline.", "சரி. ஏப்ரல் 1976 -> நவம்பர் 1976 -> 1978 -> 1980 அவசரநிலை சட்டப் பயணத்தின் சரியான காலவரிசையைக் குறிக்கிறது.",
    "Incorrect. ADM Jabalpur was decided in April 1976, before 42nd CAA was enacted in Nov 1976.", "தவறு. ஏடிஎம் நபல்பூர் ஏப்ரல் 1976-ல் தீர்ப்பளிக்கப்பட்டது, 42-வது திருத்தத்திற்கு (நவம்பர் 1976) முன்.",
    "Incorrect. 44th CAA (1978) came after 42nd CAA (1976).", "தவறு. 44-வது திருத்தம் (1978) 42-வது திருத்தத்திற்குப் (1976) பின் வந்தது.",
    "Incorrect. 42nd CAA came in late 1976, after ADM Jabalpur in April 1976.", "தவறு. 42-வது திருத்தம் 1976 பிற்பகுதியில் வந்தது, ஏடிஎம் நபல்பூருக்குப் பின்.",
    "TNPSC Trap: ADM Jabalpur (Habeas Corpus Case) was in April 1976. The infamous ruling led 44th CAA (1978) to explicitly protect Articles 20 & 21 from ever being suspended.",
    "TNPSC பொறி: ஏடிஎம் நபல்பூர் (ஹேபியஸ் கார்பஸ் வழக்கு) ஏப்ரல் 1976-ல் வந்தது. அந்த மோசமான தீர்ப்பின் விளைவாகவே 44-வது திருத்தம் (1978) பிரிவுகள் 20 & 21-ஐ எக்காலத்திலும் இடைநிறுத்த முடியாது எனத் தடுத்தது.",
    "ADM Jabalpur (1976) -> 42nd CAA (1976) -> 44th CAA (1978) -> Minerva Mills (1980).",
    "ஏடிஎம் நபல்பூர் (1976) -> 42-வது திருத்தம் (1976) -> 44-வது திருத்தம் (1978) -> மினர்வா மில்ஸ் (1980).",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Chronology", "Emergency", "Article 20", "Article 21"]
))

# FR_CHRONO_015 (Hard | Target Ans: C)
questions.append(make_chrono_q(
    "FR_CHRONO_015", "Hard",
    "Arrange the following decisions developing the Doctrine of Equality under Article 14 in correct chronological order:",
    "பிரிவு 14-ன் கீழ் சமத்துவக் கோட்பாட்டை உருவாக்கிய பின்வரும் தீர்ப்புகளைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:",
    "State of West Bengal v. Anwar Ali Sarkar (Formulated traditional 'Reasonable Classification' doctrine under Article 14)", "மேற்கு வங்க மாநிலம் எதிராக அன்வர் அலி சர்க்கார் (பிரிவு 14-ன் கீழ் மரபார்ந்த 'காரணகாரிய வகைப்பாடு' கோட்பாடு உருவாக்கப்பட்டது)",
    "E.P. Royappa v. State of Tamil Nadu (Formulated new doctrine: Equality is antithetical to Arbitrariness)", "ஈ.பி. ராயப்பா எதிராக தமிழ்நாடு மாநில வழக்கு (புதிய கோட்பாடு: சமத்துவம் என்பது தன்னிச்சையான தன்மைக்கு எதிரானது என வரையறுக்கப்பட்டது)",
    "Maneka Gandhi v. State of India (Established 'Golden Triangle' linking Articles 14, 19, and 21 against state arbitrariness)", "மேனகா காந்தி எதிராக இந்திய யூனியன் வழக்கு (அரசின் தன்னிச்சையான நடவடிக்கைக்கு எதிராக பிரிவுகள் 14, 19 மற்றும் 21-ஐ இணைக்கும் 'பொன் முக்கோணம்' நிறுவப்பட்டது)",
    "Ramana Dayaram Shetty v. International Airport Authority (Extended non-arbitrariness doctrine to all state instrumentalities and contracts)", "ரமண தயாராம் ஷெட்டி எதிராக சர்வதேச விமான நிலைய ஆணைய வழக்கு (தன்னிச்சையின்மைக் கோட்பாடு அரசின் அனைத்து நிறுவனங்களுக்கும் நீட்டிக்கப்பட்டது)",
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "2 -> 4 -> 1 -> 3", "C",
    "Correct Chronological Sequence: 1. Anwar Ali Sarkar (1952) -> 2. E.P. Royappa (1974) -> 3. Maneka Gandhi (1978) -> 4. Ramana Dayaram Shetty (1979).",
    "சரியான காலவரிசை: 1. அன்வர் அலி சர்க்கார் (1952) -> 2. ஈ.பி. ராயப்பா (1974) -> 3. மேனகா காந்தி (1978) -> 4. ரமண தயாராம் ஷெட்டி (1979).",
    "Correct. 1952 -> 1974 -> 1978 -> 1979 accurately represents the constitutional evolution of Article 14.", "சரி. 1952 -> 1974 -> 1978 -> 1979 பிரிவு 14 அரசியலமைப்பு பரிணாம வளர்ச்சியின் சரியான காலவரிசையைக் குறிக்கிறது.",
    "Incorrect. E.P. Royappa (1974) came after Anwar Ali Sarkar (1952).", "தவறு. ஈ.பி. ராயப்பா (1974) அன்வர் அலி சர்க்கார் வழக்கிற்குப் (1952) பின் வந்தது.",
    "Incorrect. Maneka Gandhi (1978) expanded Royappa's non-arbitrariness doctrine.", "தவறு. மேனகா காந்தி (1978) ராயப்பாவின் தன்னிச்சையின்மைக் கோட்பாட்டை விரிவாக்கியது.",
    "Incorrect. Ramana Dayaram Shetty was decided in 1979.", "தவறு. ரமண தயாராம் ஷெட்டி 1979-ல் தீர்ப்பளிக்கப்பட்டது.",
    "TNPSC Trap: Traditional classification doctrine (Anwar Ali Sarkar 1952) was complemented by the new non-arbitrariness doctrine (E.P. Royappa 1974 by Justice Bhagwati).",
    "TNPSC பொறி: மரபார்ந்த வகைப்பாட்டுக் கோட்பாட்டை (அன்வர் அலி சர்க்கார் 1952) புதிய தன்னிச்சையின்மைக் கோட்பாடு (ஈ.பி. ராயப்பா 1974 - நீதிபதி பகவதி) மேம்படுத்தியது.",
    "Anwar Ali Sarkar (1952) -> E.P. Royappa (1974) -> Maneka Gandhi (1978) -> Ramana Shetty (1979).",
    "அன்வர் அலி சர்க்கார் (1952) -> ஈ.பி. ராயப்பா (1974) -> மேனகா காந்தி (1978) -> ரமண ஷெட்டி (1979).",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Chronology", "Article 14", "Equality", "EP Royappa"]
))

# FR_CHRONO_016 (Hard | Target Ans: D)
questions.append(make_chrono_q(
    "FR_CHRONO_016", "Hard",
    "Arrange the following landmark Supreme Court judgments on Minority Educational Rights under Articles 29 and 30 in correct chronological order:",
    "பிரிவுகள் 29 மற்றும் 30-ன் கீழ் சிறுபான்மையினரின் கல்வி உரிமைகள் தொடர்பான பின்வரும் முக்கிய உச்சநீதிமன்றத் தீர்ப்புகளைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:",
    "State of Bombay v. Bombay Education Society (Art 29(2) protects individual right to admission regardless of language)", "பம்பாய் மாநிலம் எதிராக பம்பாய் கல்விச் சங்கம் (பிரிவு 29(2) மொழியைப் பொருட்படுத்தாமல் தனிநபரின் சேர்க்கை உரிமையைப் பாதுகாக்கிறது)",
    "In Re Kerala Education Bill (Established balance between minority rights under Art 30(1) and State regulatory power)", "கேரளா கல்வி மசோதா வழக்கு (பிரிவு 30(1)-ன் கீழ் சிறுபான்மையினர் உரிமைக்கும் அரசின் ஒழுங்குமுறை அதிகாரத்திற்கும் இடையே சமநிலை நிறுவப்பட்டது)",
    "T.M.A. Pai Foundation v. State of Karnataka (11-Judge Bench held that 'State' is the unit for determining religious & linguistic minority status)", "டி.எம்.ஏ. பை ஃபவுண்டேஷன் எதிராக கர்நாடக மாநில வழக்கு (11 நீதிபதிகள் அமர்வு: மத & மொழி சிறுபான்மையினர் அந்தஸ்தை தீர்மானிக்கும் அலகு 'மாநிலம்' ஆகும் எனத் தீர்ப்பளித்தது)",
    "P.A. Inamdar v. State of Maharashtra (Held that State cannot impose reservation policy on unaided private minority & non-minority institutions)", "பி.ஏ. இனாம்தார் எதிராக மகாராஷ்டிர மாநில வழக்கு (அரசு உதவி பெறாத தனியார் சிறுபான்மை & சிறுபான்மையற்ற கல்வி நிறுவனங்களில் அரசு இடஒதுக்கீட்டைத் திணிக்க முடியாது எனத் தீர்ப்பளிக்கப்பட்டது)",
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "2 -> 3 -> 1 -> 4", "D",
    "Correct Chronological Order: 1. Bombay Education Society (1954) -> 2. In Re Kerala Education Bill (1958) -> 3. T.M.A. Pai Foundation (2002) -> 4. P.A. Inamdar (2005).",
    "சரியான காலவரிசை: 1. பம்பாய் கல்விச் சங்கம் (1954) -> 2. கேரளா கல்வி மசோதா (1958) -> 3. டி.எம்.ஏ. பை ஃபவுண்டேஷன் (2002) -> 4. பி.ஏ. இனாம்தார் (2005).",
    "Correct. 1954 -> 1958 -> 2002 -> 2005 represents exact chronological development of Articles 29 and 30.", "சரி. 1954 -> 1958 -> 2002 -> 2005 பிரிவுகள் 29 மற்றும் 30-ன் சரியான காலவரிசைப் பரிணாமத்தைக் குறிக்கிறது.",
    "Incorrect. Kerala Education Bill was 1958, after Bombay Education Society in 1954.", "தவறு. கேரளா கல்வி மசோதா 1958, பம்பாய் கல்விச் சங்கத்திற்குப் (1954) பின் வந்தது.",
    "Incorrect. T.M.A. Pai Foundation was decided in 2002.", "தவறு. டி.எம்.ஏ. பை ஃபவுண்டேஷன் 2002-ல் தீர்ப்பளிக்கப்பட்டது.",
    "Incorrect. P.A. Inamdar (2005) clarified T.M.A. Pai (2002).", "தவறு. பி.ஏ. இனாம்தார் (2005) டி.எம்.ஏ. பை (2002) தீர்ப்பை தெளிவுபடுத்தியது.",
    "TNPSC Trap: T.M.A. Pai Foundation (2002) established that minority status is determined state-wise, NOT nationally.",
    "TNPSC பொறி: டி.எம்.ஏ. பை ஃபவுண்டேஷன் (2002) சிறுபான்மையினர் அந்தஸ்து தேசிய அளவில் அல்ல, மாநில வாரியாகத் தீர்மானிக்கப்பட வேண்டும் என நிறுவியது.",
    "Bombay Education Society (1954) -> Kerala Education Bill (1958) -> TMA Pai (2002) -> PA Inamdar (2005).",
    "பம்பாய் கல்விச் சங்கம் (1954) -> கேரளா கல்வி மசோதா (1958) -> டிஎம்ஏ பை (2002) -> பிஏ இனாம்தார் (2005).",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Chronology", "Article 29", "Article 30", "Minority Rights"]
))

# FR_CHRONO_017 (Medium | Target Ans: A)
questions.append(make_chrono_q(
    "FR_CHRONO_017", "Medium",
    "Arrange the following Supreme Court rulings regarding Article 32 (Right to Constitutional Remedies) in correct chronological order:",
    "பிரிவு 32 (அரசியலமைப்பு தீர்வு உரிமை) தொடர்பான பின்வரும் உச்சநீதிமன்றத் தீர்ப்புகளைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:",
    "Prem Chand Garg v. Excise Commissioner (Ruled that Supreme Court rule-making power cannot restrict Article 32 fundamental right)", "பிரேம் சந்த் கார்க் எதிராக கலால் ஆணையர் வழக்கு (உச்சநீதிமன்ற விதிகள் பிரிவு 32 அடிப்படை உரிமையைக் கட்டுப்படுத்த முடியாது எனத் தீர்ப்பளிக்கப்பட்டது)",
    "Bandhua Mukti Morcha v. Union of India (Expanded PIL locus standi under Article 32 to protect bonded labourers)", "பந்தुआ முக்தி மோர்ச்சா எதிராக இந்திய யூனியன் வழக்கு (கொத்தடிமைகளைப் பாதுகாக்க பிரிவு 32-ன் கீழ் பொதுநல வழக்கு அணுகுமுறை விரிவாக்கப்பட்டது)",
    "Supreme Court Advocates-on-Record Association Case (Second Judges Case - Reaffirmed Judicial Independence as Basic Structure)", "சுப்ரீம் கோர்ட் அட்வகேட்ஸ்-ஆன்-ரெக்கார்ட் சங்கம் வழக்கு (இரண்டாம் நீதிபதிகள் வழக்கு - நீதித்துறை சுதந்திரம் அடிப்படை அமைப்பு என மீண்டும் உறுதி செய்யப்பட்டது)",
    "L. Chandra Kumar v. Union of India (Unanimously held that Judicial Review under Article 32 and 226 is part of Basic Structure)", "எல். சந்திர குமார் எதிராக இந்திய யூனியன் வழக்கு (பிரிவுகள் 32 மற்றும் 226-ன் கீழ் நீதித்துறை மறுஆய்வு அடிப்படை அமைப்பின் பகுதி என ஏகமனதாகத் தீர்ப்பளிக்கப்பட்டது)",
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "3 -> 1 -> 2 -> 4", "A",
    "Correct Chronological Sequence: 1. Prem Chand Garg (1962) -> 2. Bandhua Mukti Morcha (1984) -> 3. Second Judges Case (1993) -> 4. L. Chandra Kumar (1997).",
    "சரியான காலவரிசை: 1. பிரேம் சந்த் கார்க் (1962) -> 2. பந்தुआ முக்தி மோர்ச்சா (1984) -> 3. இரண்டாம் நீதிபதிகள் வழக்கு (1993) -> 4. எல். சந்திர குமார் (1997).",
    "Correct. 1962 -> 1984 -> 1993 -> 1997 follows the exact historical timeline of Article 32 rulings.", "சரி. 1962 -> 1984 -> 1993 -> 1997 பிரிவு 32 தீர்ப்புகளின் சரியான காலவரிசையைப் பின்பற்றுகிறது.",
    "Incorrect. Bandhua Mukti Morcha (1984) came after Prem Chand Garg (1962).", "தவறு. பந்தुआ முக்தி மோர்ச்சா (1984) பிரேம் சந்த் கார்க் வழக்கிற்குப் (1962) பின் வந்தது.",
    "Incorrect. Second Judges Case was decided in 1993.", "தவறு. இரண்டாம் நீதிபதிகள் வழக்கு 1993-ல் தீர்ப்பளிக்கப்பட்டது.",
    "Incorrect. L. Chandra Kumar was decided in 1997.", "தவறு. எல். சந்திர குமார் 1997-ல் தீர்ப்பளிக்கப்பட்டது.",
    "TNPSC Trap: L. Chandra Kumar (1997) held that tribunals cannot exclude writ jurisdiction of High Courts (Art 226) and Supreme Court (Art 32).",
    "TNPSC பொறி: எல். சந்திர குமார் (1997) தீர்ப்பு, தீர்ப்பாயங்கள் உயர்நீதிமன்றங்கள் (226) மற்றும் உச்சநீதிமன்றத்தின் (32) பேராணை அதிகாரத்தை விலக்க முடியாது என நிறுவியது.",
    "Prem Chand Garg (1962) -> Bandhua Mukti Morcha (1984) -> Second Judges Case (1993) -> L. Chandra Kumar (1997).",
    "பிரேம் சந்த் கார்க் (1962) -> பந்தुआ முக்தி மோர்ச்சா (1984) -> இரண்டாம் நீதிபதிகள் வழக்கு (1993) -> எல். சந்திர குமார் (1997).",
    "Understand", 60, ["Polity", "Fundamental Rights", "Chronology", "Article 32", "L Chandra Kumar Case"]
))

# FR_CHRONO_018 (Medium | Target Ans: B)
questions.append(make_chrono_q(
    "FR_CHRONO_018", "Medium",
    "Arrange the following legislative and constitutional developments regarding Armed Forces and Martial Law (Articles 33 and 34) in correct chronological order:",
    "ஆயுதப்படைகள் மற்றும் ராணுவச் சட்டம் (பிரிவுகள் 33 மற்றும் 34) தொடர்பான பின்வரும் சட்ட இயற்றல்கள் மற்றும் திருத்தங்களைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:",
    "Enactment of Article 33 and Article 34 in Part III of the Constitution", "அரசியலமைப்பின் பகுதி III-ல் பிரிவு 33 மற்றும் பிரிவு 34 இயற்றப்பட்டது",
    "Army Act, Navy Act, and Air Force Act enacted by Parliament under Article 33 powers", "பிரிவு 33 அதிகாரங்களின் கீழ் நாடாளுமன்றத்தால் ராணுவச் சட்டம், கடற்படைச் சட்டம், மற்றும் விமானப்படைச் சட்டம் இயற்றப்பட்டது",
    "Police Forces (Restriction of Rights) Act enacted by Parliament under Article 33", "பிரிவு 33-ன் கீழ் நாடாளுமன்றத்தால் காவல் படைகள் (உரிமைகள் கட்டுப்பாடு) சட்டம் இயற்றப்பட்டது",
    "50th Constitutional Amendment Act (Expanded Article 33 scope to Intelligence organizations and Telecommunication systems)", "50-வது அரசியலமைப்பு திருத்தச் சட்டம் (பிரிவு 33-ன் எல்லை உளவு நிறுவனங்கள் மற்றும் தொலைத்தொடர்பு அமைப்புகளுக்கு விரிவாக்கப்பட்டது)",
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "3 -> 1 -> 2 -> 4", "B",
    "Correct Chronological Order: 1. Constitution Enactment (1950) -> 2. Defence Acts (1950) -> 3. Police Forces Act (1966) -> 4. 50th CAA (1984).",
    "சரியான காலவரிசை: 1. அரசியலமைப்பு இயற்றல் (1950) -> 2. பாதுகாப்புப் படைகள் சட்டங்கள் (1950) -> 3. காவல் படைகள் சட்டம் (1966) -> 4. 50-வது திருத்தம் (1984).",
    "Correct. 1950 -> 1950 -> 1966 -> 1984 represents the exact statutory expansion of Article 33.", "சரி. 1950 -> 1950 -> 1966 -> 1984 பிரிவு 33-ன் சட்ட விரிவாக்கத்தின் சரியான காலவரிசையைக் குறிக்கிறது.",
    "Incorrect. Defence Acts were enacted in 1950 following Article 33.", "தவறு. பாதுகாப்புப் படைகள் சட்டங்கள் பிரிவு 33-ஐத் தொடர்ந்து 1950-ல் இயற்றப்பட்டன.",
    "Incorrect. Police Forces Act was enacted in 1966.", "தவறு. காவல் படைகள் சட்டம் 1966-ல் இயற்றப்பட்டது.",
    "Incorrect. 50th CAA was enacted in 1984.", "தவறு. 50-வது திருத்தம் 1984-ல் இயற்றப்பட்டது.",
    "TNPSC Trap: 50th CAA (1984) explicitly expanded Article 33 to cover Intelligence Bureau, RAW, and telecommunications personnel.",
    "TNPSC பொறி: 50-வது திருத்தம் (1984) உளவுப் பிரிவு (IB), RAW மற்றும் தொலைத்தொடர்புப் பணியாளர்களுக்கும் பிரிவு 33-ஐ விரிவுபடுத்தியது.",
    "1950 (Constitution) -> 1950 (Defence Acts) -> 1966 (Police Forces Act) -> 1984 (50th CAA).",
    "1950 (அரசியலமைப்பு) -> 1950 (பாதுகாப்புச் சட்டங்கள்) -> 1966 (காவல் படைகள் சட்டம்) -> 1984 (50-வது திருத்தம்).",
    "Understand", 60, ["Polity", "Fundamental Rights", "Chronology", "Article 33", "Article 34", "Armed Forces"]
))

# FR_CHRONO_019 (Medium | Target Ans: C)
questions.append(make_chrono_q(
    "FR_CHRONO_019", "Medium",
    "Arrange the following key Reservation Amendments to Part III in REVERSE chronological order (latest to earliest):",
    "பகுதி III-ல் மேற்கொள்ளப்பட்ட முக்கிய இடஒதுக்கீட்டுத் திருத்தங்களை தலைகீழ் காலவரிசைப்படி (சமீபத்தியது முதல் பழமையானது வரை) வரிசைப்படுத்தவும்:",
    "103rd CAA (Added Article 15(6) and Article 16(6) granting 10% EWS Reservation)", "103-வது திருத்தம் (10% EWS இடஒதுக்கீடு வழங்கி பிரிவு 15(6) மற்றும் 16(6) சேர்க்கப்பட்டது)",
    "93rd CAA (Added Article 15(5) enabling reservation in private educational institutions)", "93-வது திருத்தம் (தனியார் கல்வி நிறுவனங்களில் இடஒதுக்கீடு வழங்க பிரிவு 15(5) சேர்க்கப்பட்டது)",
    "85th CAA (Amended Article 16(4A) providing 'Consequential Seniority' for SC/ST promotion reservation)", "85-வது திருத்தம் (SC/ST பதவி உயர்வு இடஒதுக்கீட்டிற்கு 'தொடர் பணிமூப்பு' வழங்கி பிரிவு 16(4A) திருத்தப்பட்டது)",
    "77th CAA (Inserted Article 16(4A) permitting reservation in promotion for SCs and STs)", "77-வது திருத்தம் (SC/ST பிரிவினருக்கு பதவி உயர்வில் இடஒதுக்கீடு வழங்க பிரிவு 16(4A) சேர்க்கப்பட்டது)",
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "4 -> 3 -> 2 -> 1", "C",
    "Correct REVERSE Chronological Sequence (Latest to Earliest): 1. 103rd CAA (2019) -> 2. 93rd CAA (2005) -> 3. 85th CAA (2001) -> 4. 77th CAA (1995).",
    "சரியான தலைகீழ் காலவரிசை (சமீபத்தியது முதல் பழமையானது வரை): 1. 103-வது திருத்தம் (2019) -> 2. 93-வது திருத்தம் (2005) -> 3. 85-வது திருத்தம் (2001) -> 4. 77-வது திருத்தம் (1995).",
    "Correct. 2019 -> 2005 -> 2001 -> 1995 represents exact reverse chronological order.", "சரி. 2019 -> 2005 -> 2001 -> 1995 சரியான தலைகீழ் காலவரிசையைக் குறிக்கிறது.",
    "Incorrect. 103rd CAA (2019) is the latest amendment among these four.", "தவறு. 103-வது திருத்தம் (2019) இந்நான்்கில் சமீபத்திய திருத்தமாகும்.",
    "Incorrect. 93rd CAA was enacted in 2005, which is before 2019.", "தவறு. 93-வது திருத்தம் 2005-ல் இயற்றப்பட்டது, 2019-க்கு முன்.",
    "Incorrect. 4 -> 3 -> 2 -> 1 is standard forward order, not reverse order.", "தவறு. 4 -> 3 -> 2 -> 1 என்பது சாதாரண முன்னோக்கு வரிசையாகும், தலைகீழ் வரிசை அல்ல.",
    "TNPSC Trap: Pay attention to amendment numbers and years: 77th (1995), 85th (2001), 93rd (2005), 103rd (2019).",
    "TNPSC பொறி: திருத்த எண்கள் மற்றும் ஆண்டுகளைக் கவனிக்கவும்: 77-வது (1995), 85-வது (2001), 93-வது (2005), 103-வது (2019).",
    "2019 (103rd) -> 2005 (93rd) -> 2001 (85th) -> 1995 (77th).",
    "2019 (103-வது) -> 2005 (93-வது) -> 2001 (85-வது) -> 1995 (77-வது).",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Chronology", "Amendments", "Reservation Amendments"]
))

# FR_CHRONO_020 (Hard | Target Ans: D)
questions.append(make_chrono_q(
    "FR_CHRONO_020", "Hard",
    "Arrange the following milestones in the prohibition of Child Labour and Exploitation under Article 24 in correct chronological order:",
    "பிரிவு 24-ன் கீழ் குழந்தை தொழிலாளர் ஒழிப்பு மற்றும் சுரண்டலுக்கு எதிரான தடுப்பு மைல்கற்களைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:",
    "Enactment of Article 23 & Article 24 in Part III prohibiting forced labour and child labour in hazardous employment", "பாயிண்ட் III-ல் ஆபத்தான தொழில்களில் கட்டாய உழைப்பு மற்றும் குழந்தை தொழிலாளர் முறையைத் தடுக்கும் பிரிவு 23 & 24 சேர்க்கப்பட்டது",
    "Enactment of Child Labour (Prohibition and Regulation) Act by Parliament", "நாடாளுமன்றத்தால் குழந்தை தொழிலாளர் (தடை மற்றும் ஒழுங்குமுறை) சட்டம் இயற்றப்பட்டது",
    "M.C. Mehta v. State of Tamil Nadu Judgment (Sivakasi Child Labour Case - Directed creation of Child Labour Rehabilitation Welfare Fund)", "எம்.சி. மேத்தா எதிராக தமிழ்நாடு மாநில வழக்கு (சிவகாசி குழந்தை தொழிலாளர் வழக்கு - குழந்தை தொழிலாளர் மறுவாழ்வு நல நிதி உருவாக்க உத்தரவு)",
    "Child Labour Prohibition and Regulation Amendment Act (Complete ban on employment of children below 14 in ALL occupations)", "குழந்தை தொழிலாளர் தடை மற்றும் ஒழுங்குமுறை திருத்தச் சட்டம் (14 வயதிற்குட்பட்ட குழந்தைகள் அனைத்துத் தொழில்களிலும் ஈடுபட முற்றிலுமாகத் தடை)",
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "2 -> 3 -> 1 -> 4", "D",
    "Correct Chronological Order: 1. Constitution (1950) -> 2. Child Labour Act (1986) -> 3. M.C. Mehta Case (1996) -> 4. Child Labour Amendment Act (2016).",
    "சரியான காலவரிசை: 1. அரசியலமைப்பு (1950) -> 2. குழந்தை தொழிலாளர் சட்டம் (1986) -> 3. எம்.சி. மேத்தா வழக்கு (1996) -> 4. குழந்தை தொழிலாளர் திருத்தச் சட்டம் (2016).",
    "Correct. 1950 -> 1986 -> 1996 -> 2016 represents the exact chronological evolution of Article 24 implementation.", "சரி. 1950 -> 1986 -> 1996 -> 2016 பிரிவு 24 அமலாக்கத்தின் சரியான காலவரிசையைக் குறிக்கிறது.",
    "Incorrect. Child Labour Act was enacted in 1986.", "தவறு. குழந்தை தொழிலாளர் சட்டம் 1986-ல் இயற்றப்பட்டது.",
    "Incorrect. M.C. Mehta Sivakasi case was decided in 1996.", "தவறு. எம்.சி. மேத்தா சிவகாசி வழக்கு 1996-ல் தீர்ப்பளிக்கப்பட்டது.",
    "Incorrect. Child Labour Amendment Act introducing complete ban was enacted in 2016.", "தவறு. முழுமையான தடையை அறிமுகப்படுத்திய திருத்தச் சட்டம் 2016-ல் இயற்றப்பட்டது.",
    "TNPSC Trap: M.C. Mehta v. State of Tamil Nadu (1996) specifically pertained to child labour in match and firework factories in Sivakasi.",
    "TNPSC பொறி: எம்.சி. மேத்தா எதிராக தமிழ்நாடு மாநில வழக்கு (1996) சிவகாசி தீப்பெட்டி மற்றும் பட்டாசு ஆலைகளில் குழந்தை தொழிலாளர் முறை தொடர்பானது.",
    "1950 (Art 24) -> 1986 (Child Labour Act) -> 1996 (MC Mehta Case) -> 2016 (Amendment Act).",
    "1950 (பிரிவு 24) -> 1986 (குழந்தை தொழிலாளர் சட்டம்) -> 1996 (எம்.சி. மேத்தா வழக்கு) -> 2016 (திருத்தச் சட்டம்).",
    "Understand", 60, ["Polity", "Fundamental Rights", "Chronology", "Article 24", "Child Labour", "MC Mehta Case"]
))

# FR_CHRONO_021 (Easy | Target Ans: A)
questions.append(make_chrono_q(
    "FR_CHRONO_021", "Easy",
    "Arrange the following landmark Supreme Court judgments on Freedom of Religion (Articles 25-28) in correct chronological order:",
    "மதச் சுதந்திரம் (பிரிவுகள் 25-28) தொடர்பான பின்வரும் முக்கிய உச்சநீதிமன்றத் தீர்ப்புகளைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:",
    "Shirur Mutt Case (Formulated Essential Religious Practices doctrine under Article 25)", "ஷிரூர் மடம் வழக்கு (பிரிவு 25-ன் கீழ் 'அத்தியாவசிய மத நடைமுறைகள்' கோட்பாடு வரையறுக்கப்பட்டது)",
    "Bijoe Emmanuel v. State of Kerala (National Anthem Case - Protected Jehovah's Witnesses student rights under Art 19(1)(a) & Art 25)", "பிஜோய் இம்மானுவேல் எதிராக கேரள மாநில வழக்கு (தேசிய கீத வழக்கு - பிரிவு 25-ன் கீழ் யெகோவாவின் சாட்சிகள் மாணவர் உரிமை பாதுகாக்கப்பட்டது)",
    "S.R. Bommai v. Union of India (9-Judge Bench held Secularism is part of Basic Structure)", "எஸ்.ஆர். பொம்மை எதிராக இந்திய யூனியன் வழக்கு (9 நீதிபதிகள் அமர்வு: மதச்சார்பின்மை அடிப்படை அமைப்பின் பகுதி எனத் தீர்ப்பளித்தது)",
    "Indian Young Lawyers Association Case (Sabarimala Temple Entry Judgment under Articles 25 and 26)", "இந்திய இளம் வழக்கறிஞர்கள் சங்கம் வழக்கு (பிரிவுகள் 25 & 26-ன் கீழ் சபரிமலை கோயில் நுழைவுத் தீர்ப்பு)",
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "3 -> 1 -> 2 -> 4", "A",
    "Correct Chronological Order: 1. Shirur Mutt Case (1954) -> 2. Bijoe Emmanuel (1986) -> 3. S.R. Bommai (1994) -> 4. Sabarimala Case (2018).",
    "சரியான காலவரிசை: 1. ஷிரூர் மடம் வழக்கு (1954) -> 2. பிஜோய் இம்மானுவேல் (1986) -> 3. எஸ்.ஆர். பொம்மை (1994) -> 4. சபரிமலை வழக்கு (2018).",
    "Correct. 1954 -> 1986 -> 1994 -> 2018 follows the exact timeline of religious freedom jurisprudence.", "சரி. 1954 -> 1986 -> 1994 -> 2018 மதச் சுதந்திர நீதித்துறை பயணத்தின் சரியான காலவரிசையைப் பின்பற்றுகிறது.",
    "Incorrect. Bijoe Emmanuel (1986) came after Shirur Mutt (1954).", "தவறு. பிஜோய் இம்மானுவேல் (1986) ஷிரூர் மடம் வழக்கிற்குப் (1954) பின் வந்தது.",
    "Incorrect. S.R. Bommai (1994) came after Bijoe Emmanuel (1986).", "தவறு. எஸ்.ஆர். பொம்மை (1994) பிஜோய் இம்மானுவேல் வழக்கிற்குப் பின் வந்தது.",
    "Incorrect. Sabarimala Case was decided in 2018.", "தவறு. சபரிமலை வழக்கு 2018-ல் தீர்ப்பளிக்கப்பட்டது.",
    "TNPSC Trap: Shirur Mutt Case (1954) is famous for introducing the 'Essential Religious Practices' test.",
    "TNPSC பொறி: ஷிரூர் மடம் வழக்கு (1954) 'அத்தியாவசிய மத நடைமுறைகள்' பரிசோதனையை அறிமுகப்படுத்தியதற்காகப் பிரபலமானது.",
    "Shirur Mutt (1954) -> Bijoe Emmanuel (1986) -> S.R. Bommai (1994) -> Sabarimala Case (2018).",
    "ஷிரூர் மடம் (1954) -> பிஜோய் இம்மானுவேல் (1986) -> எஸ்.ஆர். பொம்மை (1994) -> சபரிமலை வழக்கு (2018).",
    "Remember", 60, ["Polity", "Fundamental Rights", "Chronology", "Article 25", "Freedom of Religion", "SR Bommai Case"]
))

# FR_CHRONO_022 (Medium | Target Ans: B)
questions.append(make_chrono_q(
    "FR_CHRONO_022", "Medium",
    "Arrange the following events regarding the Abolition of Titles (Article 18) and National Awards in correct chronological order:",
    "பட்டங்கள் ஒழிப்பு (பிரிவு 18) மற்றும் தேசிய விருதுகள் தொடர்பான பின்வரும் நிகழ்வுகளைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:",
    "Enactment of Article 18 in the Constitution abolishing all hereditary titles", "அனைத்துப் பாரம்பரியப் பட்டங்களையும் ஒழிக்கும் பிரிவு 18 அரசியலமைப்பில் இயற்றப்பட்டது",
    "Janata Party Government headed by Morarji Desai discontinues National Awards (Bharat Ratna, Padma Awards)", "மொரார்ஜி தேசாய் தலைமையிலான ஜனதா கட்சி அரசு தேசிய விருதுகளை (பாரத ரத்னா, பத்ம விருதுகள்) நிறுத்தியது",
    "Indira Gandhi Government reinstates National Awards", "இந்திரா காந்தி அரசு தேசிய விருதுகளை மீண்டும் அறிமுகப்படுத்தியது",
    "Balaji Raghavan v. Union of India (Supreme Court upheld validity of National Awards holding they are decorations, not titles)", "பாலாஜி ராகவன் எதிராக இந்திய யூனியன் (தேசிய விருதுகள் பட்டங்கள் அல்ல, அலங்காரங்களே என உச்சநீதிமன்றம் செல்லுபடி செய்தது)",
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "3 -> 1 -> 2 -> 4", "B",
    "Correct Chronological Sequence: 1. Constitution Enactment (1950) -> 2. Discontinuation by Morarji Desai Govt (1977) -> 3. Reinstatement by Indira Gandhi Govt (1980) -> 4. Balaji Raghavan Judgment (1996).",
    "சரியான காலவரிசை: 1. அரசியலமைப்பு இயற்றல் (1950) -> 2. மொரார்ஜி தேசாய் அரசால் நிறுத்தப்பட்டது (1977) -> 3. இந்திரா காந்தி அரசால் மீண்டும் கொண்டுவரப்பட்டது (1980) -> 4. பாலாஜி ராகவன் தீர்ப்பு (1996).",
    "Correct. 1950 -> 1977 -> 1980 -> 1996 represents the exact historical trajectory of National Awards under Article 18.", "சரி. 1950 -> 1977 -> 1980 -> 1996 பிரிவு 18-ன் கீழ் தேசிய விருதுகளின் சரியான வரலாற்றைக் குறிக்கிறது.",
    "Incorrect. Janata Party discontinued awards in 1977.", "தவறு. ஜனதா கட்சி 1977-ல் விருதுகளை நிறுத்தியது.",
    "Incorrect. Reinstatement was in 1980, after 1977 discontinuation.", "தவறு. 1977 நிறுத்தத்திற்குப் பிறகே 1980-ல் மீண்டும் கொண்டுவரப்பட்டது.",
    "Incorrect. Balaji Raghavan was decided in 1996.", "தவறு. பாலாஜி ராகவன் 1996-ல் தீர்ப்பளிக்கப்பட்டது.",
    "TNPSC Trap: National Awards (Bharat Ratna, Padma Vibhushan, Padma Bhushan, Padma Shri) were instituted in 1954, cancelled in 1977, restored in 1980, and upheld in 1996.",
    "TNPSC பொறி: தேசிய விருதுகள் 1954-ல் தொடங்கப்பட்டு, 1977-ல் ரத்து செய்யப்பட்டு, 1980-ல் மீட்டெடுக்கப்பட்டு, 1996-ல் உச்சநீதிமன்றத்தால் உறுதி செய்யப்பட்டன.",
    "1950 (Art 18) -> 1977 (Discontinued) -> 1980 (Restored) -> 1996 (Balaji Raghavan Case).",
    "1950 (பிரிவு 18) -> 1977 (நிறுத்தம்) -> 1980 (மீட்டெடுப்பு) -> 1996 (பாலாஜி ராகவன் வழக்கு).",
    "Understand", 60, ["Polity", "Fundamental Rights", "Chronology", "Article 18", "National Awards", "Balaji Raghavan"]
))

# FR_CHRONO_023 (Medium | Target Ans: C)
questions.append(make_chrono_q(
    "FR_CHRONO_023", "Medium",
    "Arrange the following statutory and constitutional milestones regarding Protection Against Arrest and Detention (Article 22) in correct chronological order:",
    "கைது மற்றும் தடுப்புக்காவலுக்கு எதிரான பாதுகாப்பு (பிரிவு 22) தொடர்பான பின்வரும் சட்ட மற்றும் அரசியலமைப்பு மைல்கற்களைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:",
    "Preventive Detention Act enacted by Parliament", "நாடாளுமன்றத்தால் தடுப்புக்காவல் சட்டம் (Preventive Detention Act) இயற்றப்பட்டது",
    "Maintenance of Internal Security Act (MISA) enacted by Parliament", "நாடாளுமன்றத்தால் உள்நாட்டுப் பாதுகாப்புப் பராமரிப்புச் சட்டம் (MISA) இயற்றப்பட்டது",
    "44th CAA provision reducing maximum period of preventive detention without Advisory Board from 3 months to 2 months (Not brought into force)", "ஆலோசனைக் குழுவின்றி தடுப்புக்காவல் காலத்தை 3 மாதத்திலிருந்து 2 மாதமாகக் குறைக்கும் 44-வது திருத்த விதி (அமலுக்கு வரவில்லை)",
    "National Security Act (NSA) enacted by Parliament", "நாடாளுமன்றத்தால் தேசியப் பாதுகாப்புச் சட்டம் (NSA) இயற்றப்பட்டது",
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "2 -> 3 -> 4 -> 1", "C",
    "Correct Chronological Sequence: 1. Preventive Detention Act (1950) -> 2. MISA (1971) -> 3. 44th CAA (1978) -> 4. NSA (1980).",
    "சரியான காலவரிசை: 1. தடுப்புக்காவல் சட்டம் (1950) -> 2. MISA (1971) -> 3. 44-வது திருத்தம் (1978) -> 4. NSA (1980).",
    "Correct. 1950 -> 1971 -> 1978 -> 1980 represents the exact statutory sequence under Article 22.", "சரி. 1950 -> 1971 -> 1978 -> 1980 பிரிவு 22-ன் கீழ் சரியான சட்ட வரிசையைக் குறிக்கிறது.",
    "Incorrect. Preventive Detention Act was enacted in 1950.", "தவறு. தடுப்புக்காவல் சட்டம் 1950-ல் இயற்றப்பட்டது.",
    "Incorrect. MISA was enacted in 1971.", "தவறு. MISA 1971-ல் இயற்றப்பட்டது.",
    "Incorrect. NSA was enacted in 1980.", "தவறு. NSA 1980-ல் இயற்றப்பட்டது.",
    "TNPSC Trap: Though 44th CAA (1978) passed a provision to reduce preventive detention period from 3 months to 2 months, that particular provision has NEVER been brought into force by notification.",
    "TNPSC பொறி: 44-வது திருத்தம் (1978) தடுப்புக்காவல் காலத்தை 3 மாதத்திலிருந்து 2 மாதமாகக் குறைக்க விதி இயற்றிய போதிலும், அந்த விதி இதுவரை அறிவிக்கை மூலம் அமலுக்கு வரவில்லை.",
    "1950 (PDA) -> 1971 (MISA) -> 1978 (44th CAA) -> 1980 (NSA).",
    "1950 (PDA) -> 1971 (MISA) -> 1978 (44-வது திருத்தம்) -> 1980 (NSA).",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Chronology", "Article 22", "Preventive Detention", "NSA"]
))

# FR_CHRONO_024 (Hard | Target Ans: D)
questions.append(make_chrono_q(
    "FR_CHRONO_024", "Hard",
    "Arrange the following structural additions of Articles into Part III of the Constitution in correct chronological order:",
    "அரசியலமைப்பின் பகுதி III-ல் புதிதாக இணைக்கப்பட்ட பின்வரும் பிரிவுகளின் அமைப்பியலான சேர்க்கைகளைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:",
    "Original Part III Articles 14 to 35 came into force", "மூலப் பகுதி III பிரிவுகள் 14 முதல் 35 வரை அமலுக்கு வந்தன",
    "Article 31A and Article 31B inserted by 1st Constitutional Amendment Act", "1-வது அரசியலமைப்பு திருத்தச் சட்டம் மூலம் பிரிவு 31A மற்றும் பிரிவு 31B சேர்க்கப்பட்டன",
    "Article 31C inserted by 25th Constitutional Amendment Act", "25-வது அரசியலமைப்பு திருத்தச் சட்டம் மூலம் பிரிவு 31C சேர்க்கப்பட்டது",
    "Article 21A inserted by 86th Constitutional Amendment Act", "86-வது அரசியலமைப்பு திருத்தச் சட்டம் மூலம் பிரிவு 21A சேர்க்கப்பட்டது",
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "2 -> 3 -> 1 -> 4", "D",
    "Correct Chronological Order: 1. Original Part III (Jan 26, 1950) -> 2. Art 31A & 31B (1951) -> 3. Art 31C (1971) -> 4. Art 21A (2002).",
    "சரியான காலவரிசை: 1. மூலப் பகுதி III (ஜனவரி 26, 1950) -> 2. பிரிவு 31A & 31B (1951) -> 3. பிரிவு 31C (1971) -> 4. பிரிவு 21A (2002).",
    "Correct. 1950 -> 1951 -> 1971 -> 2002 is the exact insertion timeline for Part III Articles.", "சரி. 1950 -> 1951 -> 1971 -> 2002 பகுதி III பிரிவுகள் சேர்க்கப்பட்டதன் சரியான காலவரிசையாகும்.",
    "Incorrect. Article 31A and 31B were inserted in 1951 by 1st CAA.", "தவறு. பிரிவு 31A மற்றும் 31B 1951-ல் 1-வது திருத்தத்தால் சேர்க்கப்பட்டன.",
    "Incorrect. Article 31C was inserted in 1971 by 25th CAA.", "தவறு. பிரிவு 31C 1971-ல் 25-வது திருத்தத்தால் சேர்க்கப்பட்டது.",
    "Incorrect. Article 21A was inserted in 2002 by 86th CAA.", "தவறு. பிரிவு 21A 2002-ல் 86-வது திருத்தத்தால் சேர்க்கப்பட்டது.",
    "TNPSC Trap: Article 31A & 31B (1st CAA 1951), Article 31C (25th CAA 1971), and Article 21A (86th CAA 2002) are major structural additions to Part III.",
    "TNPSC பொறி: பிரிவு 31A & 31B (1-வது திருத்தம் 1951), பிரிவு 31C (25-வது திருத்தம் 1971), மற்றும் பிரிவு 21A (86-வது திருத்தம் 2002) ஆகியவை பகுதி III-ன் முக்கிய அமைப்பியலான சேர்க்கைகளாகும்.",
    "1950 (Part III) -> 1951 (Art 31A/31B) -> 1971 (Art 31C) -> 2002 (Art 21A).",
    "1950 (பகுதி III) -> 1951 (பிரிவு 31A/31B) -> 1971 (பிரிவு 31C) -> 2002 (பிரிவு 21A).",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Chronology", "Part III Articles", "Article 21A", "Article 31C"]
))

# FR_CHRONO_025 (Hard | Target Ans: D)
questions.append(make_chrono_q(
    "FR_CHRONO_025", "Hard",
    "Arrange the following judicial decisions establishing the relationship between Fundamental Rights (Part III) and Directive Principles (Part IV) in correct chronological order:",
    "அடிப்படை உரிமைகள் (பகுதி III) மற்றும் அரசு வழிகாட்டு நெறிமுறைகள் (பகுதி IV) இடையேயான தொடர்பை நிறுவிய பின்வரும் தீர்ப்புகளைச் சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:",
    "State of Madras v. Champakam Dorairajan (Ruled that Fundamental Rights prevail over Directive Principles in case of conflict)", "மதராஸ் மாநிலம் எதிராக சண்பகம் துரைராஜன் (முரண்பாடு ஏற்படும் போது அடிப்படை உரிமைகளே அரசு நெறிமுறைகளை விட மேலோங்கும் எனக் கூறப்பட்டது)",
    "In Re Kerala Education Bill (Formulated the Doctrine of Harmonious Construction between Part III and Part IV)", "கேரளா கல்வி மசோதா வழக்கு (பகுதி III மற்றும் பகுதி IV இடையே 'இணக்கமான விளக்கக் கோட்பாடு' உருவாக்கப்பட்டது)",
    "Minerva Mills v. Union of India (Held that Harmony and Balance between Part III and Part IV is an essential feature of Basic Structure)", "மினர்வா மில்ஸ் எதிராக இந்திய யூனியன் (பகுதி III மற்றும் பகுதி IV இடையேயான சமநிலை அடிப்படை அமைப்பின் அத்தியாவசிய அம்சம் எனத் தீர்ப்பளிக்கப்பட்டது)",
    "Unni Krishnan v. State of Andhra Pradesh (Held that Fundamental Rights and Directive Principles are supplementary and complementary to each other)", "உன்னிகிருஷ்ணன் எதிராக ஆந்திரப் பிரதேச மாநில வழக்கு (அடிப்படை உரிமைகளும் அரசு நெறிமுறைகளும் ஒன்றுக்கொன்று துணையாகவும் நிரப்பியாகவும் உள்ளன எனக் கூறப்பட்டது)",
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "2 -> 3 -> 1 -> 4", "D",
    "Correct Chronological Order: 1. Champakam Dorairajan (1951) -> 2. Kerala Education Bill (1958) -> 3. Minerva Mills (1980) -> 4. Unni Krishnan (1993).",
    "சரியான காலவரிசை: 1. சண்பகம் துரைராஜன் (1951) -> 2. கேரளா கல்வி மசோதா (1958) -> 3. மினர்வா மில்ஸ் (1980) -> 4. உன்னிகிருஷ்ணன் (1993).",
    "Correct. 1951 -> 1958 -> 1980 -> 1993 accurately traces the Part III vs Part IV relationship jurisprudence.", "சரி. 1951 -> 1958 -> 1980 -> 1993 பகுதி III vs பகுதி IV உறவின் சட்ட வரலாற்றுச் சரியான காலவரிசையைக் குறிக்கிறது.",
    "Incorrect. Kerala Education Bill (1958) came after Champakam Dorairajan (1951).", "தவறு. கேரளா கல்வி மசோதா (1958) சண்பகம் துரைராஜன் வழக்கிற்குப் (1951) பின் வந்தது.",
    "Incorrect. Minerva Mills (1980) came after Kerala Education Bill (1958).", "தவறு. மினர்வா மில்ஸ் (1980) கேரளா கல்வி மசோதாவிற்குப் பின் வந்தது.",
    "Incorrect. Unni Krishnan (1993) was decided after Minerva Mills (1980).", "தவறு. உன்னிகிருஷ்ணன் (1993) மினர்வா மில்ஸ் வழக்கிற்குப் பின் தீர்ப்பளிக்கப்பட்டது.",
    "TNPSC Trap: Champakam Dorairajan (1951) gave supremacy to FRs; Kerala Education Bill (1958) introduced Harmonious Construction; Minerva Mills (1980) declared FR-DPSP balance as Basic Structure.",
    "TNPSC பொறி: சண்பகம் துரைராஜன் (1951) அடிப்படை உரிமைகளுக்கு மேலாதிக்கம் அளித்தது; கேரளா கல்வி மசோதா (1958) இணக்கமான விளக்கத்தை அறிமுகப்படுத்தியது; மினர்வா மில்ஸ் (1980) உரிமைகள்-நெறிமுறைகள் சமநிலையை அடிப்படை அமைப்பு எனக் பிரகடனப்படுத்தியது.",
    "1951 (Champakam) -> 1958 (Kerala Ed Bill) -> 1980 (Minerva Mills) -> 1993 (Unni Krishnan).",
    "1951 (சண்பகம்) -> 1958 (கேரளா கல்வி மசோதா) -> 1980 (மினர்வா மில்ஸ்) -> 1993 (உன்னிகிருஷ்ணன்).",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Chronology", "Part III vs Part IV", "Minerva Mills"]
))

# Save full 25 questions dataset
print(f"Total Chronology questions compiled: {len(questions)}")
assert len(questions) == 25, f"Expected 25 questions, got {len(questions)}"

with open(target_path, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"✅ Successfully wrote 25 Chronology MCQs to {target_path}")
