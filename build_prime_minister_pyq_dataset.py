# -*- coding: utf-8 -*-
"""
Dedicated PYQ Practice Dataset Builder for Indian Polity - Prime Minister of India
Target: Exactly 50 Questions (5 Actual Verified PYQs + 45 PYQ_PATTERN Questions)
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

def make_opt(letter, en_text, ta_text):
    return {"id": letter, "en": en_text, "ta": ta_text}

def make_distractor_pair(correct_letter, exp_a_en, exp_a_ta, exp_b_en, exp_b_ta, exp_c_en, exp_c_ta, exp_d_en, exp_d_ta):
    why_not = {
        "A": {"en": exp_a_en, "ta": exp_a_ta},
        "B": {"en": exp_b_en, "ta": exp_b_ta},
        "C": {"en": exp_c_en, "ta": exp_c_ta},
        "D": {"en": exp_d_en, "ta": exp_d_ta}
    }
    
    da = {
        "A": {
            "status": "CORRECT" if correct_letter == "A" else "INCORRECT",
            "explanation_english": exp_a_en,
            "explanation_tamil": exp_a_ta,
            "trap": "Correct constitutional answer" if correct_letter == "A" else "Common distractor / misconception"
        },
        "B": {
            "status": "CORRECT" if correct_letter == "B" else "INCORRECT",
            "explanation_english": exp_b_en,
            "explanation_tamil": exp_b_ta,
            "trap": "Correct constitutional answer" if correct_letter == "B" else "Common distractor / misconception"
        },
        "C": {
            "status": "CORRECT" if correct_letter == "C" else "INCORRECT",
            "explanation_english": exp_c_en,
            "explanation_tamil": exp_c_ta,
            "trap": "Correct constitutional answer" if correct_letter == "C" else "Common distractor / misconception"
        },
        "D": {
            "status": "CORRECT" if correct_letter == "D" else "INCORRECT",
            "explanation_english": exp_d_en,
            "explanation_tamil": exp_d_ta,
            "trap": "Correct constitutional answer" if correct_letter == "D" else "Common distractor / misconception"
        }
    }
    return why_not, da

def build_pyq_item(
    idx, difficulty, qtype,
    q_en, q_ta,
    options_list, correct_ans,
    exp_en, exp_ta,
    exp_a_en, exp_a_ta,
    exp_b_en, exp_b_ta,
    exp_c_en, exp_c_ta,
    exp_d_en, exp_d_ta,
    tip_en, tip_ta,
    hy_en, hy_ta,
    trap_en, trap_ta,
    source_type="PYQ_PATTERN",
    exam=None, year=None, group=None, question_number=None, verified_answer=None,
    pattern_basis=None, pyq_insight_en=None, pyq_insight_ta=None,
    sources=None
):
    qid = f"POLITY_PM_PYQ_{idx:03d}"
    
    why_not, da = make_distractor_pair(
        correct_ans,
        exp_a_en, exp_a_ta,
        exp_b_en, exp_b_ta,
        exp_c_en, exp_c_ta,
        exp_d_en, exp_d_ta
    )

    item = {
        "id": qid,
        "subject": "Indian Polity",
        "topic": "Prime Minister of India",
        "difficulty": difficulty,
        "question_type": qtype,
        "question_en": q_en,
        "question_ta": q_ta,
        "question": {"en": q_en, "ta": q_ta},
        "options": options_list,
        "correct_answer": correct_ans,
        "explanation_en": exp_en,
        "explanation_ta": exp_ta,
        "explanation": {"en": exp_en, "ta": exp_ta},
        "why_not_others": why_not,
        "distractor_analysis": da,
        "tnpsc_tip": {"en": tip_en, "ta": tip_ta},
        "tnpsc_expert_tip": {"en": tip_en, "ta": tip_ta},
        "revision_fact": {"en": hy_en, "ta": hy_ta},
        "high_yield_revision_fact": {"en": hy_en, "ta": hy_ta},
        "trap_point": {"en": trap_en, "ta": trap_ta},
        "source_type": source_type,
        "source_reference": sources or ["Prime Minister Notes Part 1, 2 & 3"]
    }

    if source_type == "ACTUAL_PYQ":
        item["exam"] = exam
        item["year"] = year
        if group:
            item["group"] = group
        if question_number:
            item["question_number"] = question_number
        item["verified_answer"] = verified_answer or correct_ans
    else:
        item["pattern_basis"] = pattern_basis or "Based on TNPSC constitutional executive examination patterns."
        if pyq_insight_en and pyq_insight_ta:
            item["pyq_insight"] = {"en": pyq_insight_en, "ta": pyq_insight_ta}

    return item

print("Building 50 Prime Minister PYQ Practice Questions...")
questions = []

# ==============================================================================
# Q1 - Q5: ACTUAL VERIFIED TNPSC PYQs
# ==============================================================================

# Q1: ACTUAL PYQ (Group-I 2021 Q152)
q1_opts = [
    make_opt("A", "Articles 74, 75 and 78", "விதிகள் 74, 75 மற்றும் 78"),
    make_opt("B", "Articles 51, 74 and 75", "விதிகள் 51, 74 மற்றும் 75"),
    make_opt("C", "Articles 85, 74 and 75", "விதிகள் 85, 74 மற்றும் 75"),
    make_opt("D", "Articles 74, 75 and 79", "விதிகள் 74, 75 மற்றும் 79")
]
questions.append(build_pyq_item(
    1, "Medium", "Direct MCQ",
    "Which of the following articles broadly Govern the relationship between the Prime Minister and the President?",
    "பின்வரும் விதிகளில் எது பிரதமர் மற்றும் குடியரசுத் தலைவருக்கு இடையிலான உறவை விவரிக்கிறது?",
    q1_opts, "A",
    "Articles 74, 75, and 78 form the constitutional core governing PM-President relations. Art 74 provides for a Council of Ministers headed by PM to advise President; Art 75 deals with PM appointment, tenure, and responsibility; Art 78 outlines PM duties to furnish information to the President.",
    "விதிகள் 74, 75 மற்றும் 78 ஆகியவை பிரதமர்-குடியரசுத் தலைவர் இடையிலான அரசியலமைப்பு உறவை வரையறுக்கின்றன. விதி 74 அமைச்சரவையின் ஆலோசனையைக் குறிப்பிடுகிறது; விதி 75 பிரதமரின் நியமனம் மற்றும் பொறுப்புகளைக் குறிப்பிடுகிறது; விதி 78 பிரதமரின் தகவளிக்கும் கடமைகளைக் குறிப்பிடுகிறது.",
    "Correct. Articles 74 (aid & advice), 75 (appointment & responsibility), and 78 (PM duties to President) comprehensively regulate PM-President relations.",
    "சரி. விதிகள் 74, 75 மற்றும் 78 ஆகியவை பிரதமர் மற்றும் குடியரசுத் தலைவருக்கு இடையிலான உறவை முழுமையாக விவரிக்கின்றன.",
    "Incorrect. Article 51 belongs to Directive Principles (International Peace) and has no relation to executive relations.",
    "தவறு. விதி 51 அரசு நெறிமுறைக் கோட்பாடுகளில் (சர்வதேச அமைதி) உள்ளது, நிர்வாக உறவுகளுடன் தொடர்பில்லை.",
    "Incorrect. Article 85 deals with sessions, prorogation, and dissolution of Parliament, not executive PM-President relations.",
    "தவறு. விதி 85 நாடாளுமன்றக் கூட்டத்தொடர் தொடர்பானது.",
    "Incorrect. Article 79 deals with the Constitution of Parliament (President + Rajya Sabha + Lok Sabha).",
    "தவறு. விதி 79 நாடாளுமன்ற அமைப்பைக் குறிப்பிடுகிறது.",
    "TNPSC Tip: Remember the triad 74-75-78 for PM-President executive relations. Art 74 = Advice; Art 75 = Appointment; Art 78 = Communication.",
    "தேர்வு உதவி: 74-75-78 என்ற முக்கோண விதியை நினைவில் கொள்க: 74 = ஆலோசனை; 75 = நியமனம்; 78 = தகவல் அளித்தல்.",
    "Article 78 explicitly creates a constitutional bridge between the Prime Minister and the President.",
    "விதி 78 பிரதமர் மற்றும் குடியரசுத் தலைவருக்கு இடையே அரசியலமைப்புப் பாலத்தை உருவாக்குகிறது.",
    "Confusing Article 78 (PM duties to President) with Article 79 (Structure of Parliament).",
    "விதி 78 மற்றும் விதி 79-ஐக் குழப்பிக் கொள்ளுதல்.",
    source_type="ACTUAL_PYQ",
    exam="TNPSC Group-I Preliminary", year=2021, group="Group 1", question_number=152, verified_answer="A",
    sources=["TNPSC Group-I Preliminary 2021 Q152", "Prime Minister Notes Part 1 & Part 2"]
))

# Q2: ACTUAL PYQ (Group-I 2021 Q157)
q2_opts = [
    make_opt("A", "I and II only true", "I மற்றும் II மட்டும் சரி"),
    make_opt("B", "II only correct", "II மட்டும் சரி"),
    make_opt("C", "I and IV only correct", "I மற்றும் IV மட்டும் சரி"),
    make_opt("D", "IV only correct", "IV மட்டும் சரி")
]
questions.append(build_pyq_item(
    2, "Medium", "Statement-Based",
    "Consider the following statements:\nI. The constitution of India establishes a Parliamentary form of Government\nII. Prime Minister is the Head of the Government\nIII. President is the Head of the Government\nIV. Real executive power rests with the President of India\nChoose the correct answer from the following:",
    "பின்வரும் கூற்றுகளைக் கருத்தில் கொள்க:\nI. இந்திய அரசியலமைப்பு நாடாளுமன்ற முறை அரசாங்கத்தை நிறுவுகிறது.\nII. பிரதமர் அரசாங்கத்தின் தலைவர் ஆவார்.\nIII. குடியரசுத் தலைவர் அரசாங்கத்தின் தலைவர் ஆவார்.\nIV. உண்மையான நிர்வாக அதிகாரம் இந்தியக் குடியரசுத் தலைவரிடம் உள்ளது.\nசரியான விடையைத் தேர்ந்தெடுக்கவும்:",
    q2_opts, "A",
    "Statement I is correct: India has a Westminster Parliamentary system. Statement II is correct: Prime Minister is the Head of Government (De facto executive). Statement III is incorrect: President is the Head of State (De jure executive), not Head of Government. Statement IV is incorrect: Real executive power rests with the Prime Minister, not the President.",
    "கூற்று I சரி: இந்தியா நாடாளுமன்ற அரசாங்க முறையைக் கொண்டுள்ளது. கூற்று II சரி: பிரதமர் அரசாங்கத்தின் தலைவர் (உண்மையான நிர்வாகி). கூற்று III தவறு: குடியரசுத் தலைவர் அரசின் தலைவர் (அரசாங்கத் தலைவர் அல்ல). கூற்று IV தவறு: உண்மையான அதிகாரம் பிரதமரிடம் உள்ளது.",
    "Correct. Statements I and II are accurate. The PM is Head of Government in India's Parliamentary system.",
    "சரி. கூற்றுகள் I மற்றும் II சரியாகும். நாடாளுமன்ற முறையில் பிரதமர் அரசாங்கத்தின் தலைவராவார்.",
    "Incorrect. Statement I is also correct along with II.",
    "தவறு. கூற்று I-ம் சரியானது.",
    "Incorrect. Statement IV is wrong because real executive power rests with PM, while President is nominal head.",
    "தவறு. உண்மையான நிர்வாக அதிகாரம் பிரதமரிடம் உள்ளது, குடியரசுத் தலைவரிடம் அல்ல.",
    "Incorrect. Statement IV is factually wrong in a parliamentary system.",
    "தவறு. கூற்று IV முற்றிலும் தவறானது.",
    "TNPSC Tip: Head of State = President (De jure); Head of Government = Prime Minister (De facto).",
    "தேர்வு உதவி: நாட்டின் தலைவர் = குடியரசுத் தலைவர்; அரசாங்கத்தின் தலைவர் = பிரதமர்.",
    "In the Indian Constitution, the President reigns while the Prime Minister rules in actual execution.",
    "இந்திய அமைப்பில் குடியரசுத் தலைவர் பெயரளவில் ஆட்சி செய்கிறார், பிரதமர் நடைமுறையில் ஆட்சி செய்கிறார்.",
    "Confusing Head of State (President) with Head of Government (Prime Minister).",
    "நாட்டின் தலைவர் மற்றும் அரசாங்கத் தலைவரைக் குழப்பிக் கொள்ளுதல்.",
    source_type="ACTUAL_PYQ",
    exam="TNPSC Group-I Preliminary", year=2021, group="Group 1", question_number=157, verified_answer="A",
    sources=["TNPSC Group-I Preliminary 2021 Q157", "Prime Minister Notes Part 1"]
))

# Q3: ACTUAL PYQ (Group-I 2019 Q134)
q3_opts = [
    make_opt("A", "Jawaharlal Nehru", "ஜவகர்லால் நேரு"),
    make_opt("B", "Lal Bahadur Shastri", "லால் பகதூர் சாஸ்திரி"),
    make_opt("C", "Indira Gandhi", "இந்திரா காந்தி"),
    make_opt("D", "Morarji Desai", "மொரார்ஜி தேசாய்")
]
questions.append(build_pyq_item(
    3, "Easy", "Direct MCQ",
    "Name the Prime Minister when for the first time the No-Confidence was moved in the Parliament?",
    "நாடாளுமன்றத்தில் முதல் முறையாக நம்பிக்கையில்லா தீர்மானம் கொண்டு வந்த போது பிரதம அமைச்சராக இருந்தவர் யார்?",
    q3_opts, "A",
    "The first No-Confidence Motion in the history of Independent India was moved against the government of Prime Minister Jawaharlal Nehru in August 1963 by Acharya J.B. Kripalani in the Lok Sabha following the 1962 Sino-Indian War.",
    "சுதந்திர இந்தியாவின் வரலாற்றில் முதல் நம்பிக்கையில்லாத் தீர்மானம் 1963 ஆகஸ்டில் ஜவகர்லால் நேரு அரசாங்கத்திற்கு எதிராக ஆச்சார்யா ஜே.பி. கிருபாளானியால் கொண்டுவரப்பட்டது.",
    "Correct. Acharya J.B. Kripalani moved the first No-Confidence Motion against Jawaharlal Nehru's ministry in August 1963.",
    "சரி. 1963 ஆகஸ்டில் ஜவகர்லால் நேருவுக்கு எதிராக முதல் நம்பிக்கையில்லா தீர்மானம் கொண்டு வரப்பட்டது.",
    "Incorrect. Lal Bahadur Shastri faced no-confidence motions later in 1964 and 1965.",
    "தவறு. லால் பகதூர் சாஸ்திரி பின்னர் 1964-ல் எதிர்நோக்கினார்.",
    "Incorrect. Indira Gandhi faced the maximum number of No-Confidence Motions (15 times), but not the first one.",
    "தவறு. இந்திரா காந்தி அதிகபட்சமாக 15 முறை எதிர்நோக்கினார், ஆனால் முதன்முறையாக அல்ல.",
    "Incorrect. Morarji Desai's government was the first to fall due to a No-Confidence Motion in 1979.",
    "தவறு. மொரார்ஜி தேசாய் அரசு 1979-ல் நம்பிக்கையில்லா தீர்மானத்தால் கவிழ்ந்த முதல் அரசாகும்.",
    "TNPSC Tip: First No-Confidence Motion = Jawaharlal Nehru (1963 by J.B. Kripalani); Most No-Confidence Motions faced = Indira Gandhi (15 times).",
    "தேர்வு உதவி: முதல் நம்பிக்கையில்லா தீர்மானம் = ஜவகர்லால் நேரு (1963); அதிக முறை எதிர்நோக்கியவர் = இந்திரா காந்தி (15 முறை).",
    "A No-Confidence Motion can be moved only in the Lok Sabha under Rule 198 of Lok Sabha Rules.",
    "நம்பிக்கையில்லா தீர்மானம் மக்களவையில் மட்டுமே விதி 198-ன் கீழ் கொண்டுவரப்பட முடியும்.",
    "Confusing the first motion moved (Nehru, 1963) with the first government defeated (Morarji Desai, 1979).",
    "முதல் தீர்மானம் கொண்டு வரப்பட்டவரையும் (நேரு), தீர்மானத்தால் கவிழ்ந்த முதல் அரசையும் (மொரார்ஜி தேசாய்) குழப்புதல்.",
    source_type="ACTUAL_PYQ",
    exam="TNPSC Group-I Preliminary", year=2019, group="Group 1", question_number=134, verified_answer="A",
    sources=["TNPSC Group-I Preliminary 2019 Q134", "Prime Minister Notes Part 3"]
))

# Q4: ACTUAL PYQ (Group-I 2021 Q35)
q4_opts = [
    make_opt("A", "Prime Minister", "பிரதமர்"),
    make_opt("B", "Home Minister", "உள்துறை அமைச்சர்"),
    make_opt("C", "The President", "குடியரசுத் தலைவர்"),
    make_opt("D", "Defense Minister", "பாதுகாப்புத் துறை அமைச்சர்")
]
questions.append(build_pyq_item(
    4, "Easy", "Direct MCQ",
    "The Chairperson of National Disaster Management Authority (NDMA) is:",
    "தேசிய பேரிடர் மேலாண்மை ஆணையத்தின் (NDMA) தலைவர் யார்?",
    q4_opts, "A",
    "Under the Disaster Management Act, 2005, the Prime Minister of India is the Ex-Officio Chairperson of the National Disaster Management Authority (NDMA). At the State level, the Chief Minister chairs the SDMA.",
    "பேரிடர் மேலாண்மைச் சட்டம் 2005-ன் படி, இந்தியப் பிரதமர் தேசிய பேரிடர் மேலாண்மை ஆணையத்தின் (NDMA) பதவிவழித் தலைவராவார். மாநில அளவில் முதலமைச்சர் SDMA தலைவராக இருப்பார்.",
    "Correct. Prime Minister is the Ex-Officio Chairman of NDMA under Disaster Management Act 2005.",
    "சரி. பேரிடர் மேலாண்மைச் சட்டம் 2005-ன் கீழ் பிரதமர் NDMA-வின் தலைவராவார்.",
    "Incorrect. Union Home Minister is a member/executive committee supervisor, but PM is the ex-officio Chairman.",
    "தவறு. மத்திய உள்துறை அமைச்சர் உறுப்பினராவார், ஆனால் தலைவர் பிரதமராவார்.",
    "Incorrect. President is not involved in statutory administrative authority chairmanships.",
    "தவறு. குடியரசுத் தலைவர் இந்த ஆணையத்தின் தலைவரல்ல.",
    "Incorrect. Defense Minister is involved in armed forces disaster response, not heading NDMA.",
    "தவறு. பாதுகாப்பு அமைச்சர் ராணுவப் பேரிடர் மீட்பில் உதவுபவர், NDMA தலைவர் அல்ல.",
    "TNPSC Tip: Ex-Officio Chairmanships of PM: NITI Aayog, Inter-State Council, NDMA, National Integration Council, National Water Resources Council.",
    "தேர்வு உதவி: பிரதமரின் முக்கிய பதவிவழித் தலைமைகள்: நிதி ஆயோக், மாநிலங்களிடை மன்றம், NDMA, தேசிய ஒருங்கிணைப்புக் குழு.",
    "The Prime Minister heads statutory apex bodies like NDMA while CM heads SDMA at state level.",
    "மத்தியில் பிரதமர் NDMA தலைவராகவும், மாநிலத்தில் முதலமைச்சர் SDMA தலைவராகவும் செயல்படுகின்றனர்.",
    "Assuming Union Home Minister is the Chairman of NDMA because Home Ministry handles disaster management administration.",
    "உள்துறை அமைச்சகம் நிர்வாகத்தைக் கவனிப்பதால் உள்துறை அமைச்சரே தலைவர் எனத் தவறாகக் கருதுதல்.",
    source_type="ACTUAL_PYQ",
    exam="TNPSC Group-I Preliminary", year=2021, group="Group 1", question_number=35, verified_answer="A",
    sources=["TNPSC Group-I Preliminary 2021 Q35", "Prime Minister Notes Part 2"]
))

# Q5: ACTUAL PYQ (Group-I 2021 Q151)
q5_opts = [
    make_opt("A", "Prime Minister", "பிரதமர்"),
    make_opt("B", "President", "குடியரசுத் தலைவர்"),
    make_opt("C", "Parliament", "நாடாளுமன்றம்"),
    make_opt("D", "None of the above", "மேற்கண்ட எதுவும் இல்லை")
]
questions.append(build_pyq_item(
    5, "Medium", "Direct MCQ",
    "The Council of Ministers of the Union holds office during the pleasure of:",
    "மத்திய நாடாளுமன்ற அமைச்சரவை யாருடைய விருப்பம் இருக்கும் வரை பதவியில் நீடிக்கும்?",
    q5_opts, "B",
    "According to Article 75(2) of the Indian Constitution, ministers hold office during the pleasure of the President. However, constitutional convention dictates that the President exercises this pleasure on the advice of the Prime Minister, provided the government maintains Lok Sabha majority.",
    "அரசியலமைப்பு விதி 75(2)-ன் படி அமைச்சர்கள் குடியரசுத் தலைவரின் விருப்பம் உள்ளவரை பதவியில் நீடிப்பர். ஆனால் இவிருப்பம் பிரதமரின் ஆலோசனையின் பேரிலேயே செயல்படுத்தப்படுகிறது.",
    "Incorrect. PM advises the dismissal, but constitutionally office is held during the pleasure of the President.",
    "தவறு. பிரதமர் ஆலோசனை வழங்கினாலும், அரசியலமைப்பு ரீதியாக குடியரசுத் தலைவரின் விருப்பத்தின் பேரிலேயே பதவியில் நீடிக்கின்றனர்.",
    "Correct. Article 75(2) explicitly states that Ministers hold office during the pleasure of the President.",
    "சரி. விதி 75(2) தெளிவுபடுத்துவது போல குடியரசுத் தலைவரின் விருப்பமுள்ளவரையே பதவியில் நீடிப்பர்.",
    "Incorrect. Parliament evaluates collective responsibility under Art 75(3), but pleasure doctrine under Art 75(2) is vested in the President.",
    "தவறு. நாடாளுமன்றம் கூட்டுப் பொறுப்பை மதிப்பிடுகிறது, ஆனால் விருப்பக் கோட்பாடு குடியரசுத் தலைவரிடம் உள்ளது.",
    "Incorrect. Option B is the constitutional text answer.",
    "தவறு. விருப்பக் கோட்பாடு குடியரசுத் தலைவரைக் குறிக்கிறது.",
    "TNPSC Tip: Individual Responsibility (Art 75(2)) = Pleasure of President; Collective Responsibility (Art 75(3)) = Responsible to Lok Sabha.",
    "தேர்வு உதவி: தனிநபர் பொறுப்பு (விதி 75(2)) = குடியரசுத் தலைவர் விருப்பம்; கூட்டுப் பொறுப்பு (விதி 75(3)) = மக்களவைக்குப் பொறுப்பு.",
    "Pleasure of President under Art 75(2) represents individual responsibility of ministers.",
    "விதி 75(2)-ன் கீழ் குடியரசுத் தலைவர் விருப்பம் என்பது அமைச்சர்களின் தனிநபர் பொறுப்பைக் குறிக்கிறது.",
    "Confusing collective responsibility to Lok Sabha (Art 75(3)) with individual holding of office during President's pleasure (Art 75(2)).",
    "மக்களவைக்கான கூட்டுப் பொறுப்பையும் குடியரசுத் தலைவர் விருப்பத்தின் பேரில் பதவி வகிப்பதையும் குழப்புதல்.",
    source_type="ACTUAL_PYQ",
    exam="TNPSC Group-I Preliminary", year=2021, group="Group 1", question_number=151, verified_answer="B",
    sources=["TNPSC Group-I Preliminary 2021 Q151", "Prime Minister Notes Part 1 & Part 3"]
))

# ==============================================================================
# Q6 - Q50: HIGH-QUALITY PYQ PATTERN QUESTIONS
# ==============================================================================

# Q6: PYQ_PATTERN - Constitutional Position (De Jure vs De Facto)
q6_opts = [
    make_opt("A", "President of India", "இந்தியக் குடியரசுத் தலைவர்"),
    make_opt("B", "Prime Minister of India", "இந்தியப் பிரதமர்"),
    make_opt("C", "Chief Justice of India", "இந்திய தலைமை நீதிபதி"),
    make_opt("D", "Speaker of Lok Sabha", "மக்களவை சபாநாயகர்")
]
questions.append(build_pyq_item(
    6, "Easy", "Direct MCQ",
    "In the Indian constitutional framework based on the Westminster system, who is recognized as the 'De Facto' (Real) executive authority?",
    "வெஸ்ட்மின்ஸ்டர் முறையை அடிப்படையாகக் கொண்ட இந்திய அரசியலமைப்பு கட்டமைப்பில், 'உண்மையான' (De Facto) நிர்வாக அதிகாரியாக அங்கீகரிக்கப்படுபவர் யார்?",
    q6_opts, "B",
    "In a parliamentary system of government, the President is the nominal or 'De Jure' (legal) executive head, while the Prime Minister is the real or 'De Facto' executive head who exercises actual political and administrative authority.",
    "நாடாளுமன்ற முறையில், குடியரசுத் தலைவர் பெயரளவு (De Jure) நிர்வாகத் தலைவராகவும், பிரதமர் உண்மையான (De Facto) நிர்வாகத் தலைவராகவும் செயல்படுகிறார்.",
    "Incorrect. President is the De Jure (nominal) executive head.",
    "தவறு. குடியரசுத் தலைவர் பெயரளவு (De Jure) நிர்வாகத் தலைவராவார்.",
    "Correct. Prime Minister is the De Facto (real) executive head in the Parliamentary system.",
    "சரி. நாடாளுமன்ற அமைப்பில் பிரதமர் உண்மையான (De Facto) நிர்வாகத் தலைவராவார்.",
    "Incorrect. Chief Justice heads the Judiciary, not the Executive.",
    "தவறு. தலைமை நீதிபதி நீதித்துறையின் தலைவராவார்.",
    "Incorrect. Speaker presides over Lok Sabha, heading the legislative assembly proceedings.",
    "தவறு. சபாநாயகர் மக்களவையின் தலைவர் ஆவார்.",
    "TNPSC Tip: De Jure Executive = President; De Facto Executive = Prime Minister. Head of State = President; Head of Government = PM.",
    "தேர்வு உதவி: சட்டப்பூர்வ தலைவர் (De Jure) = குடியரசுத் தலைவர்; உண்மையான தலைவர் (De Facto) = பிரதமர்.",
    "The real executive power in India is exercised by the Cabinet headed by the Prime Minister.",
    "இந்தியாவில் உண்மையான நிர்வாக அதிகாரம் பிரதமரைத் தலைவராகக் கொண்ட அமைச்சரவையால் பயன்படுத்தப்படுகிறது.",
    "Confusing De Jure (President) with De Facto (Prime Minister).",
    "De Jure (சட்டப்பூர்வ) மற்றும் De Facto (உண்மையான) தலைவர்களைக் குழப்பிக் கொள்ளுதல்.",
    pattern_basis="Based on standard TNPSC Group 1/2 executive taxonomy questions.",
    pyq_insight_en="TNPSC frequently contrasts De Jure vs De Facto executive authority in Indian Polity.",
    pyq_insight_ta="டிஎன்பிஎஸ்சி பெயரளவு மற்றும் உண்மையான அதிகாரங்களை அடிக்கடி ஒப்பிட்டு வினா கேட்கும்.",
    sources=["Prime Minister Notes Part 1 - Section 2"]
))

# Q7: PYQ_PATTERN - Article 75(1) Appointment
q7_opts = [
    make_opt("A", "Elected directly by the citizens of India", "இந்திய குடிமக்களால் நேரடியாக தேர்ந்தெடுக்கப்படுகிறார்"),
    make_opt("B", "Elected by a joint sitting of both Houses of Parliament", "நாடாளுமன்றத்தின் இரு அவைகளின் கூட்டுக் கூட்டத்தால் தேர்ந்தெடுக்கப்படுகிறார்"),
    make_opt("C", "Appointed by the President of India", "இந்தியக் குடியரசுத் தலைவரால் நியமிக்கப்படுகிறார்"),
    make_opt("D", "Nominated by the Chief Justice of India", "இந்தியத் தலைமை நீதிபதியால் பரிந்துரைக்கப்படுகிறார்")
]
questions.append(build_pyq_item(
    7, "Easy", "Direct MCQ",
    "According to Article 75(1) of the Constitution of India, the Prime Minister shall be:",
    "இந்திய அரசியலமைப்பின் உறுப்பு 75(1)-ன் படி, பிரதமர் எவ்வாறு தேர்ந்தெடுக்கப்படுகிறார் / நியமிக்கப்படுகிறார்?",
    q7_opts, "C",
    "Article 75(1) explicitly states: 'The Prime Minister shall be appointed by the President and the other Ministers shall be appointed by the President on the advice of the Prime Minister.' The PM is NOT directly elected by the public.",
    "அரசியலமைப்பு உறுப்பு 75(1) தெளிவுபடுத்துவது: 'பிரதமர் குடியரசுத் தலைவரால் நியமிக்கப்படுவார், இதர அமைச்சர்கள் பிரதமரின் ஆலோசனையின் பேரில் குடியரசுத் தலைவரால் நியமிக்கப்படுவர்.'",
    "Incorrect. India does not have direct presidential/executive elections by the people.",
    "தவறு. இந்தியாவில் பிரதமருக்கு நேரடி தேர்தல் இல்லை.",
    "Incorrect. There is no provision for a joint sitting election for the Prime Minister.",
    "தவறு. கூட்டுக் கூட்டத் தேர்தல் முறை அரசியலமைப்பில் இல்லை.",
    "Correct. Article 75(1) specifies that the Prime Minister is appointed by the President.",
    "சரி. விதி 75(1)-ன் படி பிரதமர் குடியரசுத் தலைவரால் நியமிக்கப்படுகிறார்.",
    "Incorrect. Judiciary has zero role in the appointment of the Prime Minister.",
    "தவறு. நீதித்துறைக்கு இதில் எந்தப்ங்கும் இல்லை.",
    "TNPSC Tip: PM is APPOINTED by President under Art 75(1). Never select 'elected by Parliament' or 'elected directly'.",
    "தேர்வு உதவி: விதி 75(1)-ன் கீழ் பிரதமர் குடியரசுத் தலைவரால் 'நியமிக்கப்படுகிறார்'. 'தேர்ந்தெடுக்கப்படுகிறார்' என்ற வார்த்தையைத் தவிர்க்கவும்.",
    "Appointment of PM is an executive constitutional act performed under Article 75(1).",
    "பிரதமரின் நியமனம் என்பது விதி 75(1)-ன் கீழ் குடியரசுத் தலைவரால் செய்யப்படும் அரசியலமைப்புச் செயலாகும்.",
    "Choosing 'elected by people' due to general election political campaigns.",
    "தேர்தல் பிரசாரங்களால் பிரதமர் மக்களால் தேர்ந்தெடுக்கப்படுகிறார் எனத் தவறாகக் கருதுதல்.",
    pattern_basis="Based on Article identification and constitutional wording traps in TNPSC.",
    pyq_insight_en="TNPSC tests exact constitutional vocabulary: PM is 'appointed', not 'elected'.",
    pyq_insight_ta="அரசியலமைப்பு வார்த்தைப் பயன்பாடு: பிரதமர் 'நியமிக்கப்படுகிறார்' என்பதே சரி.",
    sources=["Prime Minister Notes Part 1 - Section 3"]
))

# Q8: PYQ_PATTERN - Article 75(5) Six Month Rule
q8_opts = [
    make_opt("A", "3 months", "3 மாதங்கள்"),
    make_opt("B", "6 months", "6 மாதங்கள்"),
    make_opt("C", "1 year", "1 ஆண்டு"),
    make_opt("D", "5 years", "5 ஆண்டுகள்")
]
questions.append(build_pyq_item(
    8, "Easy", "Direct MCQ",
    "Under Article 75(5) of the Constitution, a person who is NOT a member of either House of Parliament can be appointed as Prime Minister, provided he becomes an MP within:",
    "அரசியலமைப்பின் உறுப்பு 75(5)-ன் கீழ், நாடாளுமன்றத்தின் எந்தவொரு அவையிலும் உறுப்பினராக இல்லாத ஒருவர் பிரதமராக நியமிக்கப்பட்டால், அவர் எத்தனை மாதங்களுக்குள் உறுப்பினராக வேண்டும்?",
    q8_opts, "B",
    "Article 75(5) lays down that a minister (including Prime Minister) who for any period of six consecutive months is not a member of either House of Parliament shall at the expiration of that period cease to be a minister. Precedents: H.D. Deve Gowda (1996).",
    "விதி 75(5)-ன் படி, தொடர்ச்சியாக 6 மாதங்கள் நாடாளுமன்றத்தின் எந்த அவையிலும் உறுப்பினராக இல்லாத ஒருவர் அமைச்சர்/பிரதமர் பதவியை இழப்பார். (எ.கா. தேவ கவுடா 1996).",
    "Incorrect. 3 months is not the constitutional timeline for parliamentary membership.",
    "தவறு. 3 மாதங்கள் அரசியலமைப்பு காலக்கெடுவல்ல.",
    "Correct. Article 75(5) allows a non-MP to remain PM for up to 6 months.",
    "சரி. விதி 75(5)-ன் படி 6 மாதங்களுக்குள் எதேனும் ஒரு அவையில் உறுப்பினராக வேண்டும்.",
    "Incorrect. 1 year is invalid for parliamentary membership qualification.",
    "தவறு. 1 ஆண்டு தவறான காலக்கெடுவாகும்.",
    "Incorrect. 5 years is the tenure of Lok Sabha, not membership grace period.",
    "தவறு. 5 ஆண்டுகள் மக்களவை கால அளவு.",
    "TNPSC Tip: Six-month rule applies to both Union PM/Ministers (Art 75(5)) and State CM/Ministers (Art 164(4)).",
    "தேர்வு உதவி: 6 மாத விதி மத்திய அமைச்சர்கள் (விதி 75(5)) மற்றும் மாநில அமைச்சர்கள் (விதி 164(4)) இருவருக்குமே பொருந்தும்.",
    "A non-MP can be appointed PM first and get elected to Lok Sabha or Rajya Sabha within 6 months.",
    "நாடாளுமன்ற உறுப்பினராக இல்லாத ஒருவர் பிரதமராகி 6 மாதங்களுக்குள் எதேனும் ஒரு அவைக்குத் தேர்ந்தெடுக்கப்படலாம்.",
    "Thinking a person must be an MP BEFORE taking oath as Prime Minister.",
    "பிரதமராகப் பதவியேற்கும் முன்பே எம்பி-யாக இருக்க வேண்டும் என நினைப்பது.",
    pattern_basis="Based on Article 75 clause identification in TNPSC Group 1/2.",
    pyq_insight_en="TNPSC frequently tests the 6-month membership window for non-MPs appointed as ministers.",
    pyq_insight_ta="6 மாத கால அவகாசம் குறித்த வினாக்கள் அடிக்கடி கேட்கப்படும்.",
    sources=["Prime Minister Notes Part 1 - Section 4"]
))

# Q9: PYQ_PATTERN - Article 78 Duties of PM
q9_opts = [
    make_opt("A", "Article 78", "உறுப்பு 78"),
    make_opt("B", "Article 74", "உறுப்பு 74"),
    make_opt("C", "Article 75", "உறுப்பு 75"),
    make_opt("D", "Article 77", "உறுப்பு 77")
]
questions.append(build_pyq_item(
    9, "Easy", "Direct MCQ",
    "Which Article of the Indian Constitution defines the constitutional duties of the Prime Minister in respect of furnishing information to the President?",
    "குடியரசுத் தலைவருக்குத் தகவல்களை அளிப்பது தொடர்பாக பிரதமரின் அரசியலமைப்புக் கடமைகளை வரையறுக்கும் விதி எது?",
    q9_opts, "A",
    "Article 78 defines the duties of Prime Minister regarding: (a) communicating decisions of COM to President, (b) furnishing administration/legislative information, and (c) submitting matters for COM consideration if President requires.",
    "உறுப்பு 78 பிரதமரின் கடமைகளைக் குறிப்பிடுகிறது: (அ) முடிவுகளைத் தெரிவித்தல், (ஆ) நிர்வாகத் தகவல்களை அளித்தல், (இ) குடியரசுத் தலைவர் கோரினால் அமைச்சரவை பரிசீலனைக்கு வைப்பது.",
    "Correct. Article 78 explicitly enumerates the duties of the Prime Minister towards the President.",
    "சரி. உறுப்பு 78 பிரதமரின் கடமைகளைத் தெளிவாக விவரிக்கிறது.",
    "Incorrect. Article 74 covers Aid and Advice of the Council of Ministers to the President.",
    "தவறு. உறுப்பு 74 அமைச்சரவையின் ஆலோசனையைக் குறிப்பிடுகிறது.",
    "Incorrect. Article 75 deals with provisions as to Ministers (appointment, tenure, salary).",
    "தவறு. உறுப்பு 75 நியமனம் மற்றும் பதவிக்காலத்தைக் குறிப்பிடுகிறது.",
    "Incorrect. Article 77 deals with Conduct of Business of the Government of India.",
    "தவறு. உறுப்பு 77 இந்திய அரசின் நிர்வாக நடவடிக்கைகள் நடத்தையைக் குறிப்பிடுகிறது.",
    "TNPSC Tip: Article 78 = Duties of PM (Information bridge). Memorize the keywords: Communicate decisions, Furnish info, Submit for consideration.",
    "தேர்வு உதவி: உறுப்பு 78 = பிரதமரின் கடமைகள். முக்கிய சொற்கள்: தகவல்களை அளித்தல், முடிவுகளைத் தெரிவித்தல்.",
    "Article 78 serves as the main constitutional channel of communication between President and Cabinet.",
    "உறுப்பு 78 குடியரசுத் தலைவருக்கும் அமைச்சரவைக்கும் இடையிலான தொடர்புக் கால்வாயாகச் செயல்படுகிறது.",
    "Confusing Article 77 (Executive business in President's name) with Article 78 (PM duties).",
    "உறுப்பு 77 (குடியரசுத் தலைவர் பெயரிலான நிர்வாகம்) மற்றும் உறுப்பு 78 (பிரதமர் கடமைகள்)-ஐக் குழப்புதல்.",
    pattern_basis="Based on executive article matching questions in TNPSC.",
    pyq_insight_en="Article 78 is a top high-yield topic in TNPSC Polity question papers.",
    pyq_insight_ta="உறுப்பு 78 டிஎன்பிஎஸ்சி தேர்வுகளில் அதிகம் கேட்கப்படும் ஒரு முக்கிய விதியாகும்.",
    sources=["Prime Minister Notes Part 2 - Section 1"]
))

# Q10: PYQ_PATTERN - Article 75(3) Collective Responsibility
q10_opts = [
    make_opt("A", "The President of India", "இந்தியக் குடியரசுத் தலைவர்"),
    make_opt("B", "The Rajya Sabha", "மாநிலங்களவை"),
    make_opt("C", "The Supreme Court of India", "இந்திய உச்ச நீதிமன்றம்"),
    make_opt("D", "The House of the People (Lok Sabha)", "மக்களவை (Lok Sabha)")
]
questions.append(build_pyq_item(
    10, "Easy", "Direct MCQ",
    "Under Article 75(3) of the Constitution, the Union Council of Ministers headed by the Prime Minister is collectively responsible to:",
    "அரசியலமைப்பு உறுப்பு 75(3)-ன் கீழ், பிரதமரைத் தலைவராகக் கொண்ட மத்திய அமைச்சரவை யாருக்குக் கூட்டாகப் பொறுப்பேற்கிறது?",
    q10_opts, "D",
    "Article 75(3) strictly dictates: 'The Council of Ministers shall be collectively responsible to the House of the People.' The Council of Ministers is NOT collectively responsible to the Rajya Sabha or Parliament as a whole.",
    "உறுப்பு 75(3) தெளிவாகக் கூறுவது: 'அமைச்சரவை மக்களவைக்குக் (House of the People) கூட்டாகப் பொறுப்பானது.' இது மாநிலங்களவைக்கோ அல்லது முழு நாடாளுமன்றத்திற்கோ கூட்டாகப் பொறுப்பல்ல.",
    "Incorrect. Individual ministers hold office during pleasure of President under Art 75(2), but collective responsibility is to Lok Sabha.",
    "தவறு. தனிநபர் விருப்பம் குடியரசுத் தலைவரிடம் உள்ளது, கூட்டுப் பொறுப்பு மக்களவையிடம் உள்ளது.",
    "Incorrect. Council of Ministers is not responsible to Rajya Sabha.",
    "தவறு. அமைச்சரவை மாநிலங்களவைக்குப் பொறுப்பல்ல.",
    "Incorrect. Council of Ministers is not answerable to Supreme Court for political policy decisions.",
    "தவறு. உச்ச நீதிமன்றத்திற்கு அரசியலமைப்பு கூட்டுப் பொறுப்பு இல்லை.",
    "Correct. Article 75(3) specifies collective responsibility ONLY to Lok Sabha (House of the People).",
    "சரி. உறுப்பு 75(3) மக்களவைக்கு மட்டுமே கூட்டுப் பொறுப்பைக் குறிப்பிடுகிறது.",
    "TNPSC Tip: Collective Responsibility = Lok Sabha ONLY (Art 75(3)). If options mention 'Parliament', beware! The Constitution specifically says 'House of the People'.",
    "தேர்வு உதவி: கூட்டுப் பொறுப்பு = 'மக்களவைக்கு மட்டும்' (விதி 75(3)). 'நாடாளுமன்றம்' என்ற ஆப்ஷனைத் தவிர்க்கவும்.",
    "Collective responsibility means all ministers sink or swim together with the Lok Sabha majority.",
    "கூட்டுப் பொறுப்பு என்றால் அனைத்து அமைச்சர்களும் மக்களவையின் பெரும்பான்மையுடன் இணைந்து செயல்பட வேண்டும்.",
    "Selecting 'Parliament' instead of specifically 'Lok Sabha' (House of the People).",
    "மக்களவை என்று குறிப்பிடுவதற்குப் பதிலாக நாடாளுமன்றம் என்று தவறாகத் தேர்ந்தெடுப்பது.",
    pattern_basis="Based on Article 75(3) constitutional wording focus in TNPSC.",
    pyq_insight_en="TNPSC loves testing the distinction between 'Lok Sabha' vs 'Parliament' for Art 75(3).",
    pyq_insight_ta="விதி 75(3)-ல் 'நாடாளுமன்றம்' என்பதை விட 'மக்களவை' என்பதே துல்லியமான விடையாகும்.",
    sources=["Prime Minister Notes Part 3 - Section 1"]
))

# Q11: PYQ_PATTERN - Individual Responsibility & Dismissal of Ministers
q11_opts = [
    make_opt("A", "Speaker of Lok Sabha", "மக்களவை சபாநாயகர்"),
    make_opt("B", "Prime Minister", "பிரதமர்"),
    make_opt("C", "Vice-President", "துணைக் குடியரசுத் தலைவர்"),
    make_opt("D", "Chief Justice of India", "இந்திய தலைமை நீதிபதி")
]
questions.append(build_pyq_item(
    11, "Medium", "Direct MCQ",
    "While Article 75(2) states that ministers hold office during the pleasure of the President, the President can dismiss a minister ONLY on the advice of:",
    "உறுப்பு 75(2) அமைச்சர்கள் குடியரசுத் தலைவரின் விருப்பம் வரை பதவியில் நீடிப்பர் எனக் கூறினாலும், குடியரசுத் தலைவர் ஒரு அமைச்சரை யாரது ஆலோசனையின் பேரில் மட்டுமே பதவி நீக்கம் செய்ய முடியும்?",
    q11_opts, "B",
    "Under parliamentary convention and Art 75(1)/75(2), the President exercises the power of dismissal of an individual minister ONLY upon the binding recommendation/advice of the Prime Minister.",
    "நாடாளுமன்ற மரபு மற்றும் விதி 75(2)-ன் படி, ஒரு அமைச்சரைப் பதவி நீக்கம் செய்யும் குடியரசுத் தலைவரின் அதிகாரம் பிரதமரின் ஆலோசனையின் பேரிலேயே செயல்படுத்தப்படுகிறது.",
    "Incorrect. Speaker has no constitutional authority over minister appointment or dismissal.",
    "தவறு. சபாநாயகருக்கு அமைச்சர் நீக்கத்தில் அதிகாரமில்லை.",
    "Correct. The President dismisses a minister only on the advice of the Prime Minister.",
    "சரி. பிரதமரின் ஆலோசனையின் பேரிலேயே குடியரசுத் தலைவர் அமைச்சரை நீக்குகிறார்.",
    "Incorrect. Vice-President has no executive role in ministerial dismissals.",
    "தவறு. துணைக் குடியரசுத் தலைவருக்கு இதில் அதிகாரமில்லை.",
    "Incorrect. Chief Justice has no political executive dismissal powers.",
    "தவறு. தலைமை நீதிபதிக்கு இதில் தொடர்பில்லை.",
    "TNPSC Tip: PM can drop a minister either by asking for resignation or advising President to dismiss him.",
    "தேர்வு உதவி: பிரதமர் ஒரு அமைச்சரை ராஜினாமா செய்யக் கேட்கலாம் அல்லது குடியரசுத் தலைவருக்குப் பரிந்துரைத்து நீக்கலாம்.",
    "Individual responsibility under Art 75(2) gives the PM absolute authority over ministerial tenure.",
    "விதி 75(2)-ன் கீழ் தனிநபர் பொறுப்பு என்பது அமைச்சர்களின் பதவிக்காலத்தில் பிரதமரின் மேலாதிக்கத்தைக் காட்டுகிறது.",
    "Thinking the President can dismiss a minister at his own personal discretion without PM advice.",
    "பிரதமர் ஆலோசனையின்றி குடியரசுத் தலைவர் தானாகவே அமைச்சரை நீக்கலாம் என நினைப்பது.",
    pattern_basis="Based on PM-Minister relationship dynamics tested in Group 1.",
    pyq_insight_en="TNPSC tests how formal constitutional powers (President) are guided by real powers (PM).",
    pyq_insight_ta="அரசியலமைப்பு வடிவமும் நடைமுறை அதிகாரமும் ஒப்பிடப்பட்டு வினாக்கள் கேட்கப்படும்.",
    sources=["Prime Minister Notes Part 1 & Part 2"]
))

# Q12: PYQ_PATTERN - Oath Administration
q12_opts = [
    make_opt("A", "Chief Justice of India", "இந்திய தலைமை நீதிபதி"),
    make_opt("B", "Speaker of Lok Sabha", "மக்களவை சபாநாயகர்"),
    make_opt("C", "President of India", "இந்தியக் குடியரசுத் தலைவர்"),
    make_opt("D", "Outgoing Prime Minister", "பதவி விலகும் பிரதமர்")
]
questions.append(build_pyq_item(
    12, "Easy", "Direct MCQ",
    "Before entering upon his office, who administers the Oath of Office and Secrecy to the Prime Minister of India according to Article 75(4)?",
    "அரசியலமைப்பு உறுப்பு 75(4)-ன் படி, பிரதமர் பதவியேற்கும் முன் அவருக்கு பதவிப் பிரமாணமும் இரகசியக் காப்புப் பிரமாணமும் செய்து வைப்பவர் யார்?",
    q12_opts, "C",
    "Under Article 75(4) and the Third Schedule of the Indian Constitution, the President of India (or a person appointed by him) administers the Oath of Office and Oath of Secrecy to the Prime Minister.",
    "அரசியலமைப்பு உறுப்பு 75(4) மற்றும் 3-வது அட்டவணையின் படி, இந்தியக் குடியரசுத் தலைவர் பிரதமருக்குப் பதவிப் பிரமாணமும் இரகசியக் காப்புப் பிரமாணமும் செய்து வைக்கிறார்.",
    "Incorrect. CJI administers oath to the President under Art 60, not to the PM.",
    "தவறு. தலைமை நீதிபதி குடியரசுத் தலைவருக்குப் பிரமாணம் செய்து வைக்கிறார் (விதி 60).",
    "Incorrect. Speaker is elected by Lok Sabha and does not administer PM oath.",
    "தவறு. சபாநாயகர் பிரதமருக்குப் பிரமாணம் செய்து வைப்பதில்லை.",
    "Correct. President of India administers Oath of Office and Secrecy to the PM.",
    "சரி. இந்தியக் குடியரசுத் தலைவர் பிரதமருக்குப் பிரமாணம் செய்து வைக்கிறார்.",
    "Incorrect. Outgoing PM has no constitutional swearing-in role.",
    "தவறு. பதவி விலகும் பிரதமருக்கு இதில் தொடர்பில்லை.",
    "TNPSC Tip: CJI swears in President (Art 60); President swears in PM and Union Ministers (Art 75(4)); Governor swears in CM (Art 164(3)).",
    "தேர்வு உதவி: தலைமை நீதிபதி = குடியரசுத் தலைவருக்கு; குடியரசுத் தலைவர் = பிரதமருக்கு; ஆளுநர் = முதலமைச்சருக்கு.",
    "PM takes two oaths: Oath of Office and Oath of Secrecy, set out in the Third Schedule.",
    "பிரதமர் 3-வது அட்டவணையின் கீழ் இரு பிரமாணங்களை (பதவிப் பிரமாணம் & இரகசியக் காப்புப் பிரமாணம்) ஏற்கிறார்.",
    "Confusing the CJI's role in swearing in the President with the PM's swearing-in ceremony.",
    "தலைமை நீதிபதி குடியரசுத் தலைவருக்குப் பிரமாணம் செய்து வைப்பதையும் பிரதமர் பதவியேற்பையும் குழப்புதல்.",
    pattern_basis="Based on constitutional oath administrators in TNPSC.",
    pyq_insight_en="Oath administering authorities are standard memory-based factual PYQ topics.",
    pyq_insight_ta="பிரமாணம் செய்து வைக்கும் அதிகார அமைப்புகள் குறித்த வினாக்கள் நேரடித் வினாக்களாக வரும்.",
    sources=["Prime Minister Notes Part 1 - Section 5"]
))

# Q13: PYQ_PATTERN - PM from Rajya Sabha (Indira Gandhi 1966)
q13_opts = [
    make_opt("A", "Indira Gandhi (1966)", "இந்திரா காந்தி (1966)"),
    make_opt("B", "H.D. Deve Gowda (1996)", "எச்.டி. தேவ கவுடா (1996)"),
    make_opt("C", "I.K. Gujral (1997)", "ஐ.கே. குஜ்ரால் (1997)"),
    make_opt("D", "Dr. Manmohan Singh (2004)", "டாக்டர் மன்மோகன் சிங் (2004)")
]
questions.append(build_pyq_item(
    13, "Medium", "Direct MCQ",
    "Who was the FIRST Prime Minister of India to be appointed from the Rajya Sabha (Upper House)?",
    "மாநிலங்களவையில் (மேலவை) இருந்து பிரதமராக நியமிக்கப்பட்ட முதல் இந்தியப் பிரதமர் யார்?",
    q13_opts, "A",
    "Indira Gandhi in 1966 became the first Prime Minister appointed from the Rajya Sabha. Later Rajya Sabha PMs include H.D. Deve Gowda (1996), I.K. Gujral (1997), and Dr. Manmohan Singh (2004 & 2009).",
    "1966-ல் இந்திரா காந்தி மாநிலங்களவையிலிருந்து பிரதமராக நியமிக்கப்பட்ட முதல் நபராவார். பின்னர் தேவ கவுடா (1996), ஐ.கே. குஜ்ரால் (1997), மன்மோகன் சிங் (2004, 2009) ஆகியோரும் மாநிலங்களவை எம்பிக்களாக பிரதமரானார்கள்.",
    "Correct. Indira Gandhi was the first RS member to become Prime Minister in 1966.",
    "சரி. 1966-ல் இந்திரா காந்தி மாநிலங்களவையிலிருந்து பிரதமரான முதல் நபராவார்.",
    "Incorrect. Deve Gowda became PM from RS in 1996 (second instance).",
    "தவறு. தேவ கவுடா 1996-ல் மாநிலங்களவையிலிருந்து பிரதமரானார்.",
    "Incorrect. I.K. Gujral became PM from RS in 1997 (third instance).",
    "தவறு. ஐ.கே. குஜ்ரால் 1997-ல் பிரதமரானார்.",
    "Incorrect. Dr. Manmohan Singh served as PM from RS from 2004 to 2014.",
    "தவறு. மன்மோகன் சிங் 2004 முதல் 2014 வரை மாநிலங்களவை எம்பியாகப் பிரதமராக இருந்தார்.",
    "TNPSC Tip: 4 PMs were members of Rajya Sabha when appointed: Indira Gandhi (1966), Deve Gowda (1996), Gujral (1997), Manmohan Singh (2004). In UK, PM MUST be from House of Commons.",
    "தேர்வு உதவி: மாநிலங்களவையிலிருந்து பிரதமரான நால்வர்: இந்திரா காந்தி, தேவ கவுடா, குஜ்ரால், மன்மோகன் சிங். பிரிட்டனில் பிரதமர் கீழவையிலிருந்து மட்டுமே வர முடியும்.",
    "Unlike Britain where PM must belong to House of Commons, Indian PM can belong to either House of Parliament.",
    "பிரிட்டன் போலன்றி இந்தியாவில் பிரதமர் நாடாளுமன்றத்தின் எந்தவொரு அவையிலிருந்தும் வரலாம்.",
    "Thinking Dr. Manmohan Singh was the first Rajya Sabha PM.",
    "மன்மோகன் சிங்கே முதல் மாநிலங்களவை பிரதமர் எனத் தவறாகக் கருதுவது.",
    pattern_basis="Based on historical constitutional conventions and PM membership trends.",
    pyq_insight_en="TNPSC tests constitutional comparisons between Indian and British parliamentary conventions.",
    pyq_insight_ta="இந்திய மற்றும் பிரிட்டிஷ் நாடாளுமன்ற முறைகளின் ஒப்பீட்டு வினாக்கள்.",
    sources=["Prime Minister Notes Part 1 - Section 4"]
))

# Q14: PYQ_PATTERN - Resignation/Death of PM
q14_opts = [
    make_opt("A", "The senior-most minister automatically becomes permanent Prime Minister", "மூத்த அமைச்சர் தானாகவே நிரந்தர பிரதமராகிறார்"),
    make_opt("B", "The President assumes direct rule under Article 356", "குடியரசுத் தலைவர் 356 விதியின் கீழ் நேரடி ஆட்சியை மேற்கொள்கிறார்"),
    make_opt("C", "The Council of Ministers automatically stands dissolved", "அமைச்சரவை தானாகவே கலைக்கப்பட்டதாகிவிடும்"),
    make_opt("D", "The Speaker of Lok Sabha carries out executive duties", "மக்களவை சபாநாயகர் நிர்வாகப் பணிகளை மேற்கொள்கிறார்")
]
questions.append(build_pyq_item(
    14, "Medium", "Direct MCQ",
    "What is the constitutional effect on the Union Council of Ministers if the Prime Minister resigns or dies in office?",
    "பிரதமர் பதவியில் இருக்கும்போதே மரணமடைந்தாலோ அல்லது ராஜினாமா செய்தாலோ மத்திய அமைச்சரவைக்கு ஏற்படும் அரசியலமைப்பு விளைவு என்ன?",
    q14_opts, "C",
    "Since the Prime Minister is the keystone of the Cabinet arch, the resignation or death of an incumbent Prime Minister automatically dissolves the Council of Ministers. In contrast, the death or resignation of an ordinary minister creates only a simple vacancy.",
    "பிரதமர் அமைச்சரவையின் மைய அச்சாணியாக இருப்பதால், அவரது மரணம் அல்லது ராஜினாமா முழு அமைச்சரவையையும் தானாகவே கலைத்துவிடும். சாதாரண அமைச்சரின் மரணம் வெறும் காலிப்பணியிடத்தை மட்டுமே உருவாக்கும்.",
    "Incorrect. Senior minister does not automatically become permanent PM without appointment.",
    "தவறு. மூத்த அமைச்சர் தானாகவே நிரந்தர பிரதமராக முடியாது.",
    "Incorrect. Article 356 applies to State breakdown, not Union government transition.",
    "தவறு. விதி 356 மாநில நெருக்கடி நிலை தொடர்பானது.",
    "Correct. The Council of Ministers automatically dissolves upon PM's resignation or death.",
    "சரி. பிரதமரின் ராஜினாமா அல்லது மரணத்தால் அமைச்சரவை தானாகவே கலைந்துவிடும்.",
    "Incorrect. Speaker has legislative role, no executive governance substitute power.",
    "தவறு. சபாநாயகருக்கு நிர்வாக அதிகாரம் இல்லை.",
    "TNPSC Tip: PM Death/Resignation = Whole Ministry Dissolves; Ordinary Minister Death/Resignation = Vacancy created.",
    "தேர்வு உதவி: பிரதமர் மரணம்/ராஜினாமா = முழு அமைச்சரவையும் கலைந்துவிடும்; சாதாரண அமைச்சர் மரணம்/ராஜினாமா = வெறும் காலிப்பணியிடம்.",
    "The PM is the central pole of the ministry; without the pole, the structure collapses.",
    "பிரதமர் அமைச்சரவையின் முதன்மைத் தூணாவார்; அவர் விலகினால் அமைச்சரவைக் கட்டமைப்பு சரிந்துவிடும்.",
    "Assuming an ordinary minister's resignation also dissolves the Cabinet.",
    "சாதாரண அமைச்சரின் ராஜினாமாவும் அமைச்சரவையைக் கலைக்கும் எனத் தவறாகக் கருதுதல்.",
    pattern_basis="Based on PM role as Keystone of Cabinet Arch in TNPSC.",
    pyq_insight_en="Conceptual questions on the structural role of PM in Cabinet survival.",
    pyq_insight_ta="அமைச்சரவை அமைப்பில் பிரதமரின் அச்சாணிப் பங்கு குறித்த கருத்துரு வினாக்கள்.",
    sources=["Prime Minister Notes Part 1 & Part 2"]
))

# Q15: PYQ_PATTERN - Article 77 Conduct of Business
q15_opts = [
    make_opt("A", "The Prime Minister of India", "இந்தியப் பிரதமர்"),
    make_opt("B", "The President of India", "இந்தியக் குடியரசுத் தலைவர்"),
    make_opt("C", "The Union Cabinet Secretary", "மத்திய அமைச்சரவைச் செயலாளர்"),
    make_opt("D", "The Speaker of Lok Sabha", "மக்களவை சபாநாயகர்")
]
questions.append(build_pyq_item(
    15, "Easy", "Direct MCQ",
    "Under Article 77(1) of the Indian Constitution, all executive actions of the Government of India shall be expressed to be taken in the name of:",
    "இந்திய அரசியலமைப்பின் உறுப்பு 77(1)-ன் படி, இந்திய அரசாங்கத்தின் அனைத்து நிர்வாக நடவடிக்கைகளும் யார் பெயரால் எடுக்கப்படுவதாகக் குறிப்பிடப்பட வேண்டும்?",
    q15_opts, "B",
    "Article 77(1) mandates: 'All executive action of the Government of India shall be expressed to be taken in the name of the President.' Article 77(3) further authorizes the President to make rules for convenient transaction of business.",
    "உறுப்பு 77(1)-ன் படி, இந்திய அரசின் அனைத்து நிர்வாக நடவடிக்கைகளும் குடியரசுத் தலைவரின் பெயராலேயே மேற்கொள்ளப்பட வேண்டும்.",
    "Incorrect. PM exercises real power, but official executive decisions are expressed in President's name.",
    "தவறு. பிரதமர் அதிகாரம் செலுத்தினாலும், ஆணைகள் குடியரசுத் தலைவர் பெயரிலேயே வெளியாகும்.",
    "Correct. Article 77(1) specifies that actions are taken in the name of the President.",
    "சரி. உறுப்பு 77(1)-ன் படி குடியரசுத் தலைவர் பெயரிலேயே நிர்வாக நடவடிக்கைகள் எடுக்கப்படுகின்றன.",
    "Incorrect. Cabinet Secretary authenticates orders, but actions are expressed in President's name.",
    "தவறு. அமைச்சரவைச் செயலாளர் கையொப்பமிட்டாலும் குடியரசுத் தலைவர் பெயரிலேயே ஆணை வெளியாகும்.",
    "Incorrect. Speaker handles parliamentary legislative business.",
    "தவறு. சபாநாயகர் நாடாளுமன்றத்தைக் கவனிப்பவர்.",
    "TNPSC Tip: Art 77 = Government actions in President's name; Art 166 = State Government actions in Governor's name.",
    "தேர்வு உதவி: விதி 77 = மத்திய அரசு ஆணைகள் குடியரசுத் தலைவர் பெயரால்; விதி 166 = மாநில அரசு ஆணைகள் ஆளுநர் பெயரால்.",
    "Even though PM makes the actual decision, the legal notification is issued in the name of the President.",
    "பிரதமர் முடிவு எடுத்தாலும் சட்டப்பூர்வ அறிவிக்கை குடியரசுத் தலைவர் பெயரிலேயே வெளியாகும்.",
    "Selecting Prime Minister because he takes the actual executive decisions.",
    "பிரதமரே முடிவெடுப்பதால் அவர் பெயரிலேயே ஆணைகள் வெளியாகும் என நினைப்பது.",
    pattern_basis="Based on Article 77 executive business pattern.",
    pyq_insight_en="TNPSC tests formal vs real operational execution under Article 77.",
    pyq_insight_ta="விதி 77-ன் கீழ் பெயரளவு நிர்வாக ஆணை வெளியீடு குறித்த வினாக்கள்.",
    sources=["Prime Minister Notes Part 1 - Section 6"]
))

# Q16: PYQ_PATTERN - Statement / PM Powers & Functions
q16_opts = [
    make_opt("A", "1 and 2 only", "1 மற்றும் 2 மட்டும்"),
    make_opt("B", "2 and 3 only", "2 மற்றும் 3 மட்டும்"),
    make_opt("C", "1 and 3 only", "1 மற்றும் 3 மட்டும்"),
    make_opt("D", "1, 2 and 3", "1, 2 மற்றும் 3")
]
questions.append(build_pyq_item(
    16, "Hard", "Statement-Based",
    "Consider the following statements regarding the powers of the Prime Minister:\n1. The PM advises the President regarding the appointment of Chairman and members of UPSC, Election Commissioners, and CAG.\n2. The PM allocates and reshuffles various portfolios among the ministers.\n3. The PM can recommend dissolution of the Lok Sabha to the President at any time.\nWhich of the statements given above are correct?",
    "பிரதமரின் அதிகாரங்கள் தொடர்பான பின்வரும் கூற்றுகளைக் கருத்தில் கொள்க:\n1. UPSC தலைவர், தேர்தல் ஆணையர்கள் மற்றும் CAG நியமனம் குறித்து குடியரசுத் தலைவருக்கு பிரதமர் ஆலோசனை வழங்குகிறார்.\n2. அமைச்சர்களிடையே இலாகாக்களை ஒதுக்குவதையும் மாற்றி அமைப்பதையும் பிரதமர் செய்கிறார்.\n3. மக்களவையை எந்த நேரத்திலும் கலைக்குமாறு குடியரசுத் தலைவருக்கு பிரதமர் பரிந்துரைக்கலாம்.\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானவை?",
    q16_opts, "D",
    "All three statements are correct: (1) PM advises President on major constitutional appointments (UPSC, EC, CAG, AG), (2) PM allocates and reshuffles ministerial portfolios, (3) PM can recommend Lok Sabha dissolution to President if he enjoys majority support.",
    "மூன்று கூற்றுகளும் சரியானவை: (1) UPSC தலைவர், தேர்தல் ஆணையர்கள் நியமன ஆலோசனையை பிரதமர் வழங்குகிறார், (2) இலாகா ஒதுக்கீடு செய்ய அதிகாரமுள்ளது, (3) மக்களவைக் கலைப்பு பரிந்துரை செய்யும் அதிகாரமும் பிரதமருக்கு உண்டு.",
    "Incorrect. Statement 3 is also correct.",
    "தவறு. கூற்று 3-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Correct. Statements 1, 2, and 3 are all accurate powers of the Prime Minister.",
    "சரி. கூற்றுகள் 1, 2 மற்றும் 3 ஆகிய அனைத்தும் பிரதமரின் சரியான அதிகாரங்களாகும்.",
    "TNPSC Tip: PM recommendations for constitutional posts (CAG, UPSC, EC) are binding under cabinet responsibility.",
    "தேர்வு உதவி: அரசியலமைப்புப் பதவிகளுக்கான பிரதமரின் பரிந்துரைகள் குடியரசுத் தலைவரால் ஏற்றுக்கொள்ளப்படும்.",
    "The PM is the principal advisor to the President on constitutional appointments and parliamentary dissolution.",
    "அரசியலமைப்பு நியமனங்கள் மற்றும் அவைக் கலைப்பில் பிரதமரே குடியரசுத் தலைவரின் முதன்மை ஆலோசகர்.",
    "Believing the President appoints UPSC members independently without PM/Cabinet advice.",
    "குடியரசுத் தலைவர் தன்னிச்சையாக UPSC உறுப்பினர்களை நியமிக்கிறார் என நினைப்பது.",
    pattern_basis="Based on multi-statement PM powers evaluation in Group 1.",
    pyq_insight_en="Comprehensive multi-statement evaluation of PM's executive and legislative powers.",
    pyq_insight_ta="பிரதமரின் அனைத்து அதிகாரங்களையும் உள்ளடக்கிய பல-கூற்று வினாக்கள்.",
    sources=["Prime Minister Notes Part 2 - Section 2 & 4"]
))

# Q17: PYQ_PATTERN - Statement / 42nd & 44th Amendments
q17_opts = [
    make_opt("A", "1 only", "1 மட்டும்"),
    make_opt("B", "2 only", "2 மட்டும்"),
    make_opt("C", "Both 1 and 2", "1 மற்றும் 2 இரண்டும்"),
    make_opt("D", "Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை")
]
questions.append(build_pyq_item(
    17, "Hard", "Statement-Based",
    "Consider the following statements regarding Constitutional Amendments to Article 74(1):\n1. The 42nd Amendment Act (1976) made the advice tendered by the Council of Ministers headed by the PM explicitly binding on the President.\n2. The 44th Amendment Act (1978) authorized the President to require the Council of Ministers to reconsider such advice once, but the reconsidered advice is binding.\nWhich of the statements given above is/are correct?",
    "அரசியலமைப்பு விதி 74(1) திருத்தங்கள் பற்றிய பின்வரும் கூற்றுகளைக் கருத்தில் கொள்க:\n1. 42-வது சட்டத்திருத்தம் (1976) பிரதமரைத் தலைவராகக் கொண்ட அமைச்சரவையின் ஆலோசனையைக் குடியரசுத் தலைவர் கட்டாயமாக ஏற்க வேண்டும் என ஆக்கியது.\n2. 44-வது சட்டத்திருத்தம் (1978) அந்த ஆலோசனையை ஒருமுறை மறுபரிசீலனை செய்யத் திருப்பி அனுப்ப குடியரசுத் தலைவருக்கு அதிகாரமளித்தது, ஆனால் மறுபரிசீலனை செய்யப்பட்ட ஆலோசனை கட்டாயமாகும்.\nஎது/எவை சரியானவை?",
    q17_opts, "C",
    "Both statements are constitutionally precise. Indira Gandhi's 42nd Amendment (1976) made COM advice strictly binding on the President. Morarji Desai's 44th Amendment (1978) added a proviso allowing the President to send back advice ONCE for reconsideration; however, if COM sends it back unchanged, President MUST accept it.",
    "இரண்டு கூற்றுகளும் அரசியலமைப்பு ரீதியாகச் சரியானவை. 42-வது திருத்தம் ஆலோசனையைக் கட்டாயமாக்கியது; 44-வது திருத்தம் ஒருமுறை மறுபரிசீலனைக்கு அனுப்பும் உரிமையை வழங்கியது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Correct. Both 1 and 2 accurately describe the 42nd and 44th Amendment changes to Article 74(1).",
    "சரி. 1 மற்றும் 2 ஆகிய இரண்டும் விதி 74(1)-ல் கொண்டுவரப்பட்ட திருத்தங்களைச் சரியாக விவரிக்கின்றன.",
    "Incorrect. Both statements are correct.",
    "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
    "TNPSC Tip: 42nd Amendment = Binding advice (1976); 44th Amendment = Reconsideration ONCE (1978). Reconsidered advice is 100% BINDING.",
    "தேர்வு உதவி: 42-வது திருத்தம் = கட்டாய ஆலோசனை (1976); 44-வது திருத்தம் = ஒருமுறை மறுபரிசீலனை உரிமை (1978).",
    "The President can delay a Cabinet decision by sending it for reconsideration once, but cannot veto it permanently.",
    "குடியரசுத் தலைவர் ஒருமுறை மறுபரிசீலனைக்கு அனுப்பி தாமதிக்கலாமே தவிர நிரந்தரமாக நிராகரிக்க முடியாது.",
    "Thinking the President can reject Cabinet advice multiple times under 44th Amendment.",
    "44-வது திருத்தத்திற்குப் பின் குடியரசுத் தலைவர் பலமுறை ஆலோசனையை நிராகரிக்கலாம் என நினைப்பது.",
    pattern_basis="Based on 42nd vs 44th Amendment comparative questions in Group 1.",
    pyq_insight_en="TNPSC frequently tests the exact mechanism of presidential advice reconsideration under Art 74(1).",
    pyq_insight_ta="விதி 74(1)-ன் கீழ் குடியரசுத் தலைவரின் மறுபரிசீலனை அதிகாரம் குறித்த ஒப்பீட்டு வினாக்கள்.",
    sources=["Prime Minister Notes Part 3 - Section 5"]
))

# Q18: PYQ_PATTERN - Statement / Hung Lok Sabha & Conventions
q18_opts = [
    make_opt("A", "1 only", "1 மட்டும்"),
    make_opt("B", "2 only", "2 மட்டும்"),
    make_opt("C", "Both 1 and 2", "1 மற்றும் 2 இரண்டும்"),
    make_opt("D", "Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை")
]
questions.append(build_pyq_item(
    18, "Hard", "Statement-Based",
    "Consider the following statements regarding a Hung Lok Sabha situation:\n1. In a Hung Lok Sabha, the President has no constitutional discretion and must immediately dissolve the House.\n2. By established constitutional convention, the President may appoint the leader of the largest single party or pre-poll alliance as PM and ask them to prove majority on the floor of the House within a specified period.\nWhich of the statements given above is/are correct?",
    "தொங்கு மக்களவை (Hung Lok Sabha) சூழல் பற்றிய பின்வரும் கூற்றுகளைக் கருத்தில் கொள்க:\n1. தொங்கு மக்களவையில் குடியரசுத் தலைவருக்கு விருப்ப அதிகாரமில்லை, உடனடியாக அவையைக் கலைக்க வேண்டும்.\n2. அரசியலமைப்பு மரபுப்படி, பெரிய தனிப்பட்ட கட்சி அல்லது கூட்டணியின் தலைவரைப் பிரதமராக நியமித்து, குறிப்பிட்ட காலத்திற்குள் மக்களவையில் பெரும்பான்மையை நிரூபிக்க குடியரசுத் தலைவர் கோரலாம்.\nஎது/எவை சரியானவை?",
    q18_opts, "B",
    "Statement 1 is incorrect: In a Hung Lok Sabha, the President exercises individual judgment/discretion to explore government formation before considering dissolution. Statement 2 is correct: Established convention (started by Neelam Sanjiva Reddy in 1979) allows appointing the largest party/coalition leader with a mandate to prove majority on the floor of the House.",
    "கூற்று 1 தவறு: தொங்கு மக்களவையில் குடியரசுத் தலைவருக்கு தனிப்பட்ட விருப்ப அதிகாரம் உண்டு. கூற்று 2 சரி: பெரிய கட்சி அல்லது கூட்டணித் தலைவரை நியமித்து பெரும்பான்மை நிரூபிக்கக் கோரும் மரபு பின்பற்றப்படுகிறது (1979 நீலம் சஞ்சீவ ரெட்டி காலம் முதல்).",
    "Incorrect. Statement 1 is wrong because President has individual discretion in Hung House.",
    "தவறு. கூற்று 1 தவறானது, குடியரசுத் தலைவருக்கு விருப்ப அதிகாரம் உண்டு.",
    "Correct. Only Statement 2 is correct regarding Presidential convention in Hung Lok Sabha.",
    "சரி. கூற்று 2 மட்டுமே சரியானது.",
    "Incorrect. Statement 1 is wrong.",
    "தவறு. கூற்று 1 தவறானது.",
    "Incorrect. Statement 2 is factually correct.",
    "தவறு. கூற்று 2 சரியானது.",
    "TNPSC Tip: Hung Lok Sabha = Real Presidential Discretion. President invites largest pre-poll alliance / party leader and stipulates floor test deadline.",
    "தேர்வு உதவி: தொங்கு மக்களவை = குடியரசுத் தலைவரின் உண்மையான சுயவிருப்ப அதிகாரம். பெரும் கட்சித் தலைவரை அழைத்து பெரும்பான்மை நிரூபிக்க ஆணையிடுவார்.",
    "Presidential discretion in appointing PM arises primarily when no party holds a clear majority in Lok Sabha.",
    "எந்தக் கட்சிக்கும் தெளிவான பெரும்பான்மை இல்லாதபோதே பிரதமரை நியமிப்பதில் குடியரசுத் தலைவரின் சுயவிருப்ப அதிகாரம் எழுகிறது.",
    "Assuming the President MUST dissolve Lok Sabha immediately without exploring coalition government possibilities.",
    "அரசாங்க அமைக்கும் வாய்ப்புகளை ஆராயாமல் குடியரசுத் தலைவர் உடனே அவையைக் கலைக்க வேண்டும் என நினைப்பது.",
    pattern_basis="Based on Hung Lok Sabha discretion & conventions in Group 1.",
    pyq_insight_en="TNPSC tests situations where Presidential discretion comes into real practice.",
    pyq_insight_ta="குடியரசுத் தலைவரின் உண்மையான சுயவிருப்ப அதிகாரம் எழும் சூழல்கள் குறித்த வினாக்கள்.",
    sources=["Prime Minister Notes Part 1 & Part 3"]
))

# Q19: PYQ_PATTERN - Statement / Cabinet vs Council of Ministers
q19_opts = [
    make_opt("A", "1 and 2 only", "1 மற்றும் 2 மட்டும்"),
    make_opt("B", "2 and 3 only", "2 மற்றும் 3 மட்டும்"),
    make_opt("C", "1 and 3 only", "1 மற்றும் 3 மட்டும்"),
    make_opt("D", "1, 2 and 3", "1, 2 மற்றும் 3")
]
questions.append(build_pyq_item(
    19, "Hard", "Statement-Based",
    "Consider the following statements regarding Cabinet vs Council of Ministers:\n1. The Council of Ministers is a wider body comprising all categories of ministers (Cabinet Ministers, Ministers of State, and Deputy Ministers).\n2. The word 'Cabinet' was present in Article 75 of the original Constitution of 1950.\n3. The word 'Cabinet' was inserted into Article 352 of the Constitution by the 44th Constitutional Amendment Act, 1978.\nWhich of the statements given above are correct?",
    "அமைச்சரவை (Cabinet) vs அமைச்சர்கள் குழு (Council of Ministers) பற்றிய கூற்றுகளைக் கருத்தில் கொள்க:\n1. அமைச்சர்கள் குழு என்பது கேபினட் அமைச்சர்கள், இராஜாங்க அமைச்சர்கள் மற்றும் இணை அமைச்சர்களை உள்ளடக்கிய பரந்த அமைப்பாகும்.\n2. 'கேபினட்' என்ற வார்த்தை 1950 மூல அரசியலமைப்பின் 75-வது விதியில் இடம்பெற்றிருந்தது.\n3. 'கேபினட்' என்ற வார்த்தை 1978-ம் ஆண்டின் 44-வது சட்டத்திருத்தத்தின் மூலம் விதி 352-ல் சேர்க்கப்பட்டது.\nஎது/எவை சரியானவை?",
    q19_opts, "C",
    "Statement 1 is correct: Council of Ministers is a larger body (60-70 ministers, 3 tiers). Statement 2 is INCORRECT: The original 1950 Constitution did NOT contain the word 'Cabinet' anywhere. Statement 3 is correct: The word 'Cabinet' was inserted into Article 352(3) by the 44th Amendment Act, 1978.",
    "கூற்று 1 சரி: அமைச்சர்கள் குழு பரந்த அமைப்பாகும். கூற்று 2 தவறு: 1950 மூல அரசியலமைப்பில் 'கேபினட்' என்ற வார்த்தையே இல்லை. கூற்று 3 சரி: 44-வது திருத்தம் மூலம் விதி 352-ல் கேபினட் என்ற வார்த்தை சேர்க்கப்பட்டது.",
    "Incorrect. Statement 2 is false.",
    "தவறு. கூற்று 2 தவறானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Correct. Statements 1 and 3 are correct. 'Cabinet' was never in original 1950 text.",
    "சரி. கூற்றுகள் 1 மற்றும் 3 மட்டுமே சரியானவை.",
    "Incorrect. Statement 2 is false.",
    "தவறு. கூற்று 2 தவறானது.",
    "TNPSC Tip: Original Constitution (1950) had NO word 'Cabinet'. Added ONLY in Art 352 by 44th Amendment 1978.",
    "தேர்வு உதவி: மூல அரசியலமைப்பில் 'கேபினட்' என்ற வார்த்தை இல்லை. 1978 44-வது திருத்தத்தில் விதி 352-ல் மட்டுமே சேர்க்கப்பட்டது.",
    "Council of Ministers is a constitutional body (Art 74 & 75); Cabinet was given constitutional status in Art 352 in 1978.",
    "அமைச்சர்கள் குழு மூல அரசியலமைப்பு அமைப்பு; கேபினட் 1978-ல் விதி 352-ல் சேர்க்கப்பட்டது.",
    "Believing 'Cabinet' and 'Council of Ministers' are identical terms in the original Constitution.",
    "மூல அரசியலமைப்பிலேயே கேபினட் என்ற வார்த்தை இருந்ததாக தவறாக எண்ணுவது.",
    pattern_basis="Based on Cabinet vs COM structural comparison in TNPSC.",
    pyq_insight_en="TNPSC frequently tests the origin of the word 'Cabinet' in the Constitution.",
    pyq_insight_ta="'கேபினட்' என்ற வார்த்தை அரசியலமைப்பில் எப்போது சேர்க்கப்பட்டது என்ற வினாக்கள்.",
    sources=["Prime Minister Notes Part 2 - Section 3"]
))

# Q20: PYQ_PATTERN - Statement / 91st Amendment Act 2003
q20_opts = [
    make_opt("A", "1 only", "1 மட்டும்"),
    make_opt("B", "2 only", "2 மட்டும்"),
    make_opt("C", "Both 1 and 2", "1 மற்றும் 2 இரண்டும்"),
    make_opt("D", "Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை")
]
questions.append(build_pyq_item(
    20, "Medium", "Statement-Based",
    "Consider the following statements regarding the size of the Council of Ministers:\n1. The total number of ministers, including the Prime Minister, in the Union Council of Ministers shall not exceed 15% of the total strength of the Lok Sabha.\n2. This limit was imposed by the 91st Constitutional Amendment Act, 2003.\nWhich of the statements given above is/are correct?",
    "அமைச்சர்கள் குழுவின் எண்ணிக்கை பற்றிய பின்வரும் கூற்றுகளைக் கருத்தில் கொள்க:\n1. பிரதமரையும் சேர்த்து மத்திய அமைச்சரவையின் மொத்த எண்ணிக்கை மக்களவையின் மொத்த உறுப்பினர்களில் 15% மிகக் கூடாது.\n2. இந்த வரம்பு 2003-ம் ஆண்டின் 91-வது அரசியலமைப்புச் சட்டத்திருத்தத்தின் மூலம் கொண்டுவரப்பட்டது.\nஎது/எவை சரியானவை?",
    q20_opts, "C",
    "Both statements are correct. Article 75(1A), inserted by the 91st Amendment Act (2003), caps the total number of ministers including the PM at 15% of the total membership of the Lok Sabha.",
    "இரண்டு கூற்றுகளும் சரியானவை. 91-வது சட்டத்திருத்தம் (2003) மூலம் சேர்க்கப்பட்ட விதி 75(1A), பிரதமரையும் சேர்த்து அமைச்சரவை எண்ணிக்கையை மக்களவை பலத்தில் 15% என உச்சவரம்பு நிர்ணயித்தது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Correct. Both Statements 1 and 2 are constitutionally accurate under Article 75(1A).",
    "சரி. கூற்றுகள் 1 மற்றும் 2 இரண்டும் சரியானவை.",
    "Incorrect. Both statements are valid.",
    "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
    "TNPSC Tip: 91st Amendment 2003 = 15% ceiling on ministers (including PM/CM) based on Lok Sabha / State Legislative Assembly strength.",
    "தேர்வு உதவி: 91-வது திருத்தம் 2003 = பிரதமர்/முதலமைச்சர் உட்பட 15% உச்சவரம்பு (மக்களவை/சட்டமன்ற பலத்தில்).",
    "The 15% ceiling is calculated against Lok Sabha strength, NOT total Parliament strength (LS + RS).",
    "15% வரம்பு மக்களவை பலத்தின் அடிப்படையில் மட்டுமே கணக்கிடப்படும், நாடாளுமன்றத்தின் மொத்த பலத்தில் அல்ல.",
    "Calculating the 15% limit using total Parliament strength (Lok Sabha + Rajya Sabha).",
    "15% வரம்பை நாடாளுமன்றத்தின் இரு அவைகளின் மொத்த எண்ணிக்கையில் கணக்கிடுதல்.",
    pattern_basis="Based on 91st Amendment ceiling questions in TNPSC.",
    pyq_insight_en="91st Amendment (15% limit) is a repeated question area in TNPSC Polity.",
    pyq_insight_ta="91-வது சட்டத்திருத்தம் (15% வரம்பு) அடிக்கடி கேட்கப்படும் தலைப்பாகும்.",
    sources=["Prime Minister Notes Part 1 - Section 4"]
))

# Q21: PYQ_PATTERN - Assertion & Reason / De Facto Head
q21_opts = [
    make_opt("A", "Both (A) and (R) are true and (R) is the correct explanation of (A)", "(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கமாகும்"),
    make_opt("B", "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)", "(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கமல்ல"),
    make_opt("C", "(A) is true but (R) is false", "(A) சரி, ஆனால் (R) தவறு"),
    make_opt("D", "(A) is false but (R) is true", "(A) தவறு, ஆனால் (R) சரி")
]
questions.append(build_pyq_item(
    21, "Hard", "Assertion & Reason",
    "Assertion (A): The Prime Minister of India is described as the real executive (De facto head) of the Indian Union.\nReason (R): Under Article 74(1), the President of India is bound to act in accordance with the advice tendered by the Council of Ministers headed by the Prime Minister.",
    "கூற்று (A): இந்தியப் பிரதமர் இந்திய ஒன்றியத்தின் உண்மையான நிர்வாகத் தலைவராக (De facto head) விவரிக்கப்படுகிறார்.\nகாரணம் (R): விதி 74(1)-ன் கீழ், பிரதமரைத் தலைவராகக் கொண்ட அமைச்சரவையின் ஆலோசனையின் படியே குடியரசுத் தலைவர் செயல்படக் கடமைப்பட்டவர் ஆவார்.",
    q21_opts, "A",
    "Both (A) and (R) are true, and (R) directly explains why the PM is the real executive. Because Article 74(1) makes Cabinet advice binding on the nominal head (President), actual decision-making power resides in the Prime Minister.",
    "(A) மற்றும் (R) இரண்டும் சரி. விதி 74(1) குடியரசுத் தலைவரை அமைச்சரவை ஆலோசனைக்குக் கட்டுப்படுத்துவதால், உண்மையான அதிகாரம் பிரதமரிடமே உள்ளது.",
    "Correct. Assertion (A) is true, Reason (R) is true, and (R) correctly explains why PM is De facto head.",
    "சரி. கூற்று மற்றும் காரணம் இரண்டும் சரி, காரணம் சரியான விளக்கமாகும்.",
    "Incorrect. (R) directly provides the constitutional reason for (A).",
    "தவறு. (R) என்பது (A)-க்கான சரியான அரசியலமைப்பு காரணமாகும்.",
    "Incorrect. Assertion (A) is true.",
    "தவறு. கூற்று (A) சரியானது.",
    "Incorrect. Reason (R) is true.",
    "தவறு. காரணம் (R) சரியானது.",
    "TNPSC Tip: In Assertion-Reason on De Facto head, Art 74(1) binding advice is the exact constitutional link explaining PM's real power.",
    "தேர்வு உதவி: De Facto தலைவர் கூற்றுக்கு விதி 74(1) கட்டாய ஆலோசனையே சரியான அரசியலமைப்பு காரணமாகும்.",
    "The executive power of the Union vested in the President by Art 53 is exercised through ministers headed by PM under Art 74.",
    "விதி 53-ன் கீழ் குடியரசுத் தலைவரிடம் உள்ள அதிகாரம் விதி 74-ன் கீழ் பிரதமரால் செயல்படுத்தப்படுகிறது.",
    "Failing to link binding aid & advice under Art 74(1) with the concept of real executive authority.",
    "விதி 74(1) ஆலோசனையை உண்மையான நிர்வாக அதிகாரத்துடன் இணைத்துப் பார்க்கத் தவறுவது.",
    pattern_basis="Based on executive Assertion-Reason patterns in TNPSC.",
    pyq_insight_en="Assertion-Reason format testing constitutional logic connecting Art 74 to De Facto power.",
    pyq_insight_ta="கூற்று-காரணம் வடிவில் விதி 74 மற்றும் உண்மையான அதிகாரத்தை இணைக்கும் வினாக்கள்.",
    sources=["Prime Minister Notes Part 1 - Section 2"]
))

# Q22: PYQ_PATTERN - Assertion & Reason / Collective Responsibility
q22_opts = [
    make_opt("A", "Both (A) and (R) are true and (R) is the correct explanation of (A)", "(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கமாகும்"),
    make_opt("B", "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)", "(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கமல்ல"),
    make_opt("C", "(A) is true but (R) is false", "(A) சரி, ஆனால் (R) தவறு"),
    make_opt("D", "(A) is false but (R) is true", "(A) தவறு, ஆனால் (R) சரி")
]
questions.append(build_pyq_item(
    22, "Hard", "Assertion & Reason",
    "Assertion (A): A No-Confidence Motion passed against any single Minister in the Lok Sabha leads to the resignation of the entire Council of Ministers including the Prime Minister.\nReason (R): Under Article 75(3), the Council of Ministers is collectively responsible to the House of the People (Lok Sabha).",
    "கூற்று (A): மக்களவையில் ஒரு தனிப்பட்ட அமைச்சருக்கு எதிராக நம்பிக்கையில்லாத் தீர்மானம் நிறைவேற்றப்பட்டால், அது பிரதமர் உட்பட முழு அமைச்சரவையின் ராஜினாமாவுக்கு வழிவகுக்கும்.\nகாரணம் (R): உறுப்பு 75(3)-ன் படி, அமைச்சரவை மக்களவைக்குக் கூட்டாகப் பொறுப்பானது.",
    q22_opts, "A",
    "Both (A) and (R) are true, and (R) explains (A). Collective responsibility under Art 75(3) means the Ministry functions as a indivisible team ('all swim or sink together'). Defeat of one minister on a confidence/policy motion is a defeat of the entire Ministry.",
    "(A) மற்றும் (R) இரண்டும் சரி. விதி 75(3)-ன் கீழ் கூட்டுப் பொறுப்பு என்பது அமைச்சரவை ஒரு குழுவாகச் செயல்படுவதைக் குறிக்கிறது. ஒரு அமைச்சரின் தோல்வி முழு அமைச்சரவையின் தோல்வியாகும்.",
    "Correct. (A) and (R) are true and (R) provides the constitutional doctrine explaining why the whole ministry falls.",
    "சரி. கூற்று மற்றும் காரணம் இரண்டும் சரி, காரணம் சரியான விளக்கமாகும்.",
    "Incorrect. Reason (R) directly explains the collective resignation rule.",
    "தவறு. காரணம் (R) கூட்டு ராஜினாமா விதியை நேரடியாக விவரிக்கிறது.",
    "Incorrect. Assertion (A) is true.",
    "தவறு. கூற்று (A) சரியானது.",
    "Incorrect. Reason (R) is true.",
    "தவறு. காரணம் (R) சரியானது.",
    "TNPSC Tip: Collective Responsibility means No-Confidence Motion CANNOT be moved against an individual minister; it is always against the ENTIRE Council of Ministers.",
    "தேர்வு உதவி: கூட்டுப் பொறுப்பு என்றால் நம்பிக்கையில்லா தீர்மானம் ஒரு தனி அமைச்சருக்கு எதிராகக் கொண்டுவரப்பட முடியாது; அது முழு அமைச்சரவைக்கு எதிரானது.",
    "Under collective responsibility, every minister is bound to support cabinet decisions inside and outside Parliament.",
    "கூட்டுப் பொறுப்பின் கீழ் ஒவ்வொரு அமைச்சரும் கேபினட் முடிவுகளை அவைக்கு உள்ளேயும் வெளியேயும் ஆதரிக்கக் கடமைப்பட்டவர்.",
    "Thinking a No-Confidence motion can be targeted to remove only one minister while keeping the PM in power.",
    "பிரதமரைத் தக்கவைத்துக்கொண்டு ஒரு அமைச்சரை மட்டும் நீக்க நம்பிக்கையில்லா தீர்மானம் கொண்டுவரலாம் என நினைப்பது.",
    pattern_basis="Based on Collective Responsibility Assertion-Reason in Group 1.",
    pyq_insight_en="TNPSC tests the indivisible nature of Cabinet responsibility under Article 75(3).",
    pyq_insight_ta="விதி 75(3)-ன் கீழ் பிரிக்க முடியாத அமைச்சரவைப் பொறுப்பு பற்றிய வினாக்கள்.",
    sources=["Prime Minister Notes Part 3 - Section 1"]
))

# Q23: PYQ_PATTERN - Assertion & Reason / Floor Test Requirement (S.R. Bommai)
q23_opts = [
    make_opt("A", "Both (A) and (R) are true and (R) is the correct explanation of (A)", "(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கமாகும்"),
    make_opt("B", "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)", "(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கமல்ல"),
    make_opt("C", "(A) is true but (R) is false", "(A) சரி, ஆனால் (R) தவறு"),
    make_opt("D", "(A) is false but (R) is true", "(A) தவறு, ஆனால் (R) சரி")
]
questions.append(build_pyq_item(
    23, "Hard", "Assertion & Reason",
    "Assertion (A): In case of doubt regarding majority support in a Hung Lok Sabha, the loss of majority must be tested on the floor of the House.\nReason (R): The Supreme Court in the S.R. Bommai case (1994) ruled that the floor of the House is the sole legal forum to test majority confidence.",
    "கூற்று (A): தொங்கு மக்களவையில் பெரும்பான்மை ஆதரவு குறித்து சந்தேகம் எழுந்தால், பெரும்பான்மை இழப்பு மக்களவையின் தளத்தில் (Floor of the House) சோதிக்கப்பட வேண்டும்.\nகாரணம் (R): எஸ்.ஆர். பொம்மை வழக்கில் (1994) உச்ச நீதிமன்றம் பெரும்பான்மையைச் சோதிக்கும் ஒரே சட்டப்பூர்வ தளம் அவையின் தளமே என்று தீர்ப்பளித்தது.",
    q23_opts, "A",
    "Both (A) and (R) are true, and (R) is the authoritative judicial precedent establishing (A). The 9-judge bench in S.R. Bommai v. Union of India (1994) mandated that majority support must be established through a floor test in the House, not by subjective assessment in Raj Bhavan / Rashtrapati Bhavan.",
    "(A) மற்றும் (R) இரண்டும் சரி. 1994 எஸ்.ஆர். பொம்மை வழக்கில் 9 நீதிபதிகள் கொண்ட அமர்வு அவையின் தளத்தில் வாக்கெடுப்பு நடத்துவதே பெரும்பான்மையை நிரூபிக்கும் ஒரே முறை என உத்தரவிட்டது.",
    "Correct. (A) and (R) are true and S.R. Bommai ruling is the exact justification.",
    "சரி. கூற்று மற்றும் காரணம் இரண்டும் சரி, காரணம் பொம்மை வழக்கு தீர்ப்பை விளக்குகிறது.",
    "Incorrect. (R) directly explains (A).",
    "தவறு. (R) என்பது (A)-க்கான நேரடி விளக்கமாகும்.",
    "Incorrect. Assertion (A) is true.",
    "தவறு. கூற்று (A) சரியானது.",
    "Incorrect. Reason (R) is true.",
    "தவறு. காரணம் (R) சரியானது.",
    "TNPSC Tip: S.R. Bommai Case (1994) = Floor test mandate for checking majority of PM/CM.",
    "தேர்வு உதவி: எஸ்.ஆர். பொம்மை வழக்கு (1994) = பிரதமர்/முதல்வர் பெரும்பான்மையை அவையின் தளத்தில் (Floor test) மட்டுமே சோதிக்க வேண்டும்.",
    "The floor test eliminates subjective arbitrariness in determining whether a government enjoys majority support.",
    "தள வாக்கெடுப்பு (Floor test) பெரும்பான்மையை தீர்மானிப்பதில் தன்னிச்சையான முடிவுகளைத் தவிர்க்கிறது.",
    "Believing the President can dismiss a government based on private letters without ordering a floor test.",
    "அவையில் வாக்கெடுப்பு நடத்தாமல் கடிதங்கள் அடிப்படையில் குடியரசுத் தலைவர் அரசை நீக்கலாம் என நினைப்பது.",
    pattern_basis="Based on S.R. Bommai judicial mandate questions in TNPSC.",
    pyq_insight_en="S.R. Bommai precedent is a frequently queried case law in parliamentary floor test questions.",
    pyq_insight_ta="எஸ்.ஆர். பொம்மை வழக்குத் தீர்ப்பு நாடாளுமன்ற தள வாக்கெடுப்பு வினாக்களில் முக்கியமானது.",
    sources=["Prime Minister Notes Part 3 - Section 3"]
))

# Q24: PYQ_PATTERN - Assertion & Reason / Caretaker Government
q24_opts = [
    make_opt("A", "Both (A) and (R) are true and (R) is the correct explanation of (A)", "(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கமாகும்"),
    make_opt("B", "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)", "(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கமல்ல"),
    make_opt("C", "(A) is true but (R) is false", "(A) சரி, ஆனால் (R) தவறு"),
    make_opt("D", "(A) is false but (R) is true", "(A) தவறு, ஆனால் (R) சரி")
]
questions.append(build_pyq_item(
    24, "Hard", "Assertion & Reason",
    "Assertion (A): A Caretaker Prime Minister and Council of Ministers should not make major policy decisions or announce new financial schemes after Lok Sabha dissolution.\nReason (R): By constitutional convention, a Caretaker Government exists only to carry on day-to-day routine administration until a new government is elected.",
    "கூற்று (A): மக்களவைக் கலைப்பிற்குப் பிறகு, இடைக்காலப் பிரதமர் மற்றும் அமைச்சரவை முக்கிய கொள்கை முடிவுகளையோ புதிய நிதித் திட்டங்களையோ அறிவிக்கக் கூடாது.\nகாரணம் (R): அரசியலமைப்பு மரபுப்படி, புதிய அரசு தேர்ந்தெடுக்கப்படும் வரை அன்றாட நிர்வாகத்தை மட்டுமே கவனித்துக் கொள்ள இடைக்கால அரசு செயல்படுகிறது.",
    q24_opts, "A",
    "Both (A) and (R) are true, and (R) explains (A). A Caretaker Government lacks democratic legitimacy from an active Lok Sabha. Thus, by established convention, it manages only routine day-to-day affairs and avoids major policy commitments.",
    "(A) மற்றும் (R) இரண்டும் சரி. இடைக்கால அரசுக்கு மக்களவையின் புதிய மக்களாணை இல்லாததால், அது அன்றாட நிர்வாகத்தை மட்டுமே கவனிக்க வேண்டும், புதிய கொள்கைகளை அறிவிக்கக் கூடாது.",
    "Correct. (A) and (R) are true and (R) correctly explains caretaker limits.",
    "சரி. கூற்று மற்றும் காரணம் இரண்டும் சரி, காரணம் இடைக்கால அரசின் எல்லையை விவரிக்கிறது.",
    "Incorrect. (R) is the direct explanation of (A).",
    "தவறு. (R) என்பது (A)-க்கான நேரடி விளக்கமாகும்.",
    "Incorrect. Assertion (A) is true.",
    "தவறு. கூற்று (A) சரியானது.",
    "Incorrect. Reason (R) is true.",
    "தவறு. காரணம் (R) சரியானது.",
    "TNPSC Tip: 'Caretaker Government' is NOT defined in the Constitution text; it exists strictly by convention.",
    "தேர்வு உதவி: 'இடைக்கால அரசு' என்ற சொல் அரசியலமைப்பு விதிக் உரையில் இல்லை; இது அரசியலமைப்பு மரபாக மட்டுமே உள்ளது.",
    "Article 74 requires a Council of Ministers at all times, which is why a Caretaker Ministry continues after dissolution.",
    "விதி 74 எப்போதும் ஒரு அமைச்சரவை இருக்க வேண்டும் எனக் கூறுவதால், கலைப்பிற்குப் பிறகும் இடைக்கால அரசு தொடர்கிறது.",
    "Assuming the term 'Caretaker Government' is explicitly written in Article 75.",
    "இடைக்கால அரசு என்ற சொல் விதி 75-ல் உள்ளதாகத் தவறாக நினைப்பது.",
    pattern_basis="Based on Caretaker Government convention questions in Group 1.",
    pyq_insight_en="TNPSC tests constitutional provisions vs unwritten conventions for Caretaker Ministries.",
    pyq_insight_ta="இடைக்கால அரசு பற்றிய அரசியலமைப்பு மரபுகள் குறித்த வினாக்கள்.",
    sources=["Prime Minister Notes Part 3 - Section 4"]
))

# Q25: PYQ_PATTERN - Assertion & Reason / Resignation of Disagreeing Minister
q25_opts = [
    make_opt("A", "Both (A) and (R) are true and (R) is the correct explanation of (A)", "(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கமாகும்"),
    make_opt("B", "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)", "(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கமல்ல"),
    make_opt("C", "(A) is true but (R) is false", "(A) சரி, ஆனால் (R) தவறு"),
    make_opt("D", "(A) is false but (R) is true", "(A) தவறு, ஆனால் (R) சரி")
]
questions.append(build_pyq_item(
    25, "Hard", "Assertion & Reason",
    "Assertion (A): If a Cabinet Minister disagrees with a Cabinet decision, he must either accept the decision or resign from the Ministry.\nReason (R): The principle of collective responsibility mandates that all ministers share joint responsibility and defend Cabinet decisions in Parliament and public.",
    "கூற்று (A): ஒரு கேபினட் முடிவில் ஒரு கேபினட் அமைச்சருக்கு உடன்பாடு இல்லை என்றால், அவர் அந்த முடிவை ஏற்க வேண்டும் அல்லது பதவியை ராஜினாமா செய்ய வேண்டும்.\nகாரணம் (R): கூட்டுப் பொறுப்புக் கோட்பாடு அனைத்து அமைச்சர்களும் இணைப் பொறுப்பைப் பகிர்ந்து கொள்ள வேண்டும் என்றும் நாடாளுமன்றத்திலும் பொதுவெளியிலும் கேபினட் முடிவுகளை ஆதரிக்க வேண்டும் என்றும் கட்டாயப்படுத்துகிறது.",
    q25_opts, "A",
    "Both (A) and (R) are true, and (R) explains (A). Examples: Dr. B.R. Ambedkar resigned in 1951 due to differences over Hindu Code Bill; C.D. Deshmukh resigned over reorganization of states. A minister cannot dissent publicly while remaining in Cabinet.",
    "(A) மற்றும் (R) இரண்டும் சரி. (எ.கா. 1951-ல் இந்து சட்ட மசோதா கருத்து வேறுபாட்டால் பி.ஆர். அம்பேத்கர் ராஜினாமா செய்தார்). கேபினட்டில் இருந்துகொண்டு முடிவை வெளிப்படையாக எதிர்க்க முடியாது.",
    "Correct. (A) and (R) are true and (R) explains the binding nature of collective responsibility.",
    "சரி. கூற்று மற்றும் காரணம் இரண்டும் சரி, காரணம் கூட்டுப் பொறுப்பின் தன்மையை விளக்குகிறது.",
    "Incorrect. (R) directly explains the resignation obligation.",
    "தவறு. (R) என்பது ராஜினாமா கடமைக்கான நேரடி விளக்கமாகும்.",
    "Incorrect. Assertion (A) is true.",
    "தவறு. கூற்று (A) சரியானது.",
    "Incorrect. Reason (R) is true.",
    "தவறு. காரணம் (R) சரியானது.",
    "TNPSC Tip: Famous resignations due to Cabinet disagreement: Dr. B.R. Ambedkar (Hindu Code Bill 1951), C.D. Deshmukh (Reorganization of States 1956).",
    "தேர்வு உதவி: கேபினட் கருத்து வேறுபாட்டால் ராஜினாமா செய்த முக்கியத் தலைவர்கள்: பி.ஆர். அம்பேத்கர் (1951), சி.டி. தேஷ்முக் (1956).",
    "Collective responsibility requires secret debate inside Cabinet but unanimous voice outside Cabinet.",
    "கூட்டுப் பொறுப்பு என்பது கேபினட்டிற்குள் கருத்து வேறுபாடுகள் இருந்தாலும் வெளியே ஒரே குரலாக நிற்க வேண்டும் என்பதாகும்.",
    "Thinking a minister can criticize a Cabinet decision in Parliament while retaining his ministerial post.",
    "அமைச்சர் பதவியில் நீடித்துக்கொண்டே கேபினட் முடிவை நாடாளுமன்றத்தில் விமர்சிக்கலாம் என நினைப்பது.",
    pattern_basis="Based on Collective responsibility dissent precedents in TNPSC.",
    pyq_insight_en="TNPSC tests historical examples of ministerial resignations enforcing collective responsibility.",
    pyq_insight_ta="கூட்டுப் பொறுப்பால் அமைச்சர்கள் ராஜினாமா செய்த வரலாற்று நிகழ்வுகள் பற்றிய வினாக்கள்.",
    sources=["Prime Minister Notes Part 3 - Section 1 & 2"]
))

# Q26: PYQ_PATTERN - Match / Articles Map
q26_opts = [
    make_opt("A", "A-3, B-2, C-4, D-1", "A-3, B-2, C-4, D-1"),
    make_opt("B", "A-2, B-3, C-4, D-1", "A-2, B-3, C-4, D-1"),
    make_opt("C", "A-2, B-3, C-1, D-4", "A-2, B-3, C-1, D-4"),
    make_opt("D", "A-4, B-1, C-2, D-3", "A-4, B-1, C-2, D-3")
]
questions.append(build_pyq_item(
    26, "Medium", "Match the Following",
    "Match List I (Article of Constitution) with List II (Key Provision):\nList I:\nA. Article 74(1)\nB. Article 75(1)\nC. Article 75(3)\nD. Article 78\nList II:\n1. Duties of Prime Minister as respect furnishing information to President\n2. Council of Ministers to aid and advise President\n3. Appointment of Prime Minister by President\n4. Collective responsibility of Council of Ministers to Lok Sabha",
    "பட்டியல் I-ல் உள்ள விதியை பட்டியல் II-ல் உள்ள விதியுடன் பொருத்துக:\nபட்டியல் I:\nA. உறுப்பு 74(1)\nB. உறுப்பு 75(1)\nC. உறுப்பு 75(3)\nD. உறுப்பு 78\nபட்டியல் II:\n1. குடியரசுத் தலைவருக்குத் தகவல்களை வழங்கும் பிரதமரின் கடமைகள்\n2. குடியரசுத் தலைவருக்கு உதவவும் ஆலோசனை வழங்கவும் அமைச்சரவை\n3. குடியரசுத் தலைவரால் பிரதமர் நியமனம்\n4. மக்களவைக்கு அமைச்சரவையின் கூட்டுப் பொறுப்பு",
    q26_opts, "B",
    "Correct matching: A-2 (Art 74(1) Aid & advice), B-3 (Art 75(1) PM appointment), C-4 (Art 75(3) Collective responsibility to LS), D-1 (Art 78 PM duties to President). Combination: A-2, B-3, C-4, D-1.",
    "சரியான பொருத்தம்: A-2 (உறுப்பு 74(1) உதவி & ஆலோசனை), B-3 (உறுப்பு 75(1) பிரதமர் நியமனம்), C-4 (உறுப்பு 75(3) கூட்டுப் பொறுப்பு), D-1 (உறுப்பு 78 பிரதமரின் கடமைகள்).",
    "Incorrect. Check A matching with 2.",
    "தவறு. A-2 பொருத்தத்தைச் சரிபார்க்கவும்.",
    "Correct. A-2, B-3, C-4, D-1 is the precise constitutional match.",
    "சரி. A-2, B-3, C-4, D-1 என்பது சரியான பொருத்தமாகும்.",
    "Incorrect. C matches with 4, not 1.",
    "தவறு. C-4 என்பது சரியான பொருத்தம்.",
    "Incorrect. A matches with 2.",
    "தவறு. A-2 என்பது சரியான பொருத்தம்.",
    "TNPSC Tip: Quick Memory Matrix: 74 = Advice; 75(1) = PM Appointment; 75(3) = Lok Sabha Responsibility; 78 = Info to President.",
    "தேர்வு உதவி: நினைவுக் குறிப்பு: 74 = ஆலோசனை; 75(1) = பிரதமர் நியமனம்; 75(3) = மக்களவைப் பொறுப்பு; 78 = தகவல் அளித்தல்.",
    "Matching individual sub-clauses of Article 75 is essential for Group 1 level questions.",
    "விதி 75-ன் உட்பிரிவுகளைத் துல்லியமாகப் பொருத்துவது குரூப் 1 தேர்வுக்கு மிக முக்கியம்.",
    "Confusing Article 75(1) [Appointment] with Article 75(3) [Collective Responsibility].",
    "விதி 75(1) [நியமனம்] மற்றும் விதி 75(3) [கூட்டுப் பொறுப்பு]-ஐக் குழப்புதல்.",
    pattern_basis="Based on executive article matching pattern in TNPSC Group 1.",
    pyq_insight_en="Match the Following questions testing exact sub-clause provisions of Articles 74, 75, and 78.",
    pyq_insight_ta="விதிகள் 74, 75, 78 உட்பிரிவுகளைப் பொருத்தும் வினாக்கள்.",
    sources=["Prime Minister Notes Part 1 - Section 6"]
))

# Q27: PYQ_PATTERN - Match / Institutional Bodies chaired by PM
q27_opts = [
    make_opt("A", "A-1, B-2, C-3, D-4", "A-1, B-2, C-3, D-4"),
    make_opt("B", "A-2, B-1, C-4, D-3", "A-2, B-1, C-4, D-3"),
    make_opt("C", "A-3, B-4, C-1, D-2", "A-3, B-4, C-1, D-2"),
    make_opt("D", "A-4, B-3, C-2, D-1", "A-4, B-3, C-2, D-1")
]
questions.append(build_pyq_item(
    27, "Medium", "Match the Following",
    "Match List I (Apex Body chaired by PM) with List II (Constitutional / Legal Status):\nList I:\nA. NITI Aayog\nB. Inter-State Council\nC. National Disaster Management Authority (NDMA)\nD. National Development Council (NDC)\nList II:\n1. Non-constitutional, executive body (replaced Planning Commission in 2015)\n2. Constitutional Body created under Article 263\n3. Statutory Body created under Disaster Management Act, 2005\n4. Extra-constitutional, non-statutory body set up in 1952",
    "பட்டியல் I-ல் உள்ள அமைப்புகளை பட்டியல் II-ல் உள்ள சட்டப்பூர்வ நிலைகளுடன் பொருத்துக:\nபட்டியல் I:\nA. நிதி ஆயோக் (NITI Aayog)\nB. மாநிலங்களிடை மன்றம் (Inter-State Council)\nC. தேசிய பேரிடர் மேலாண்மை ஆணையம் (NDMA)\nD. தேசிய வளர்ச்சிக் குழு (NDC)\nபட்டியல் II:\n1. அரசியலமைப்பில் இல்லாத, நிர்வாக அமைப்பு (2015-ல் திட்டக்குழுவுக்குப் பதிலாக அமைக்கப்பட்டது)\n2. உறுப்பு 263-ன் கீழ் உருவாக்கப்பட்ட அரசியலமைப்பு அமைப்பு\n3. பேரிடர் மேலாண்மைச் சட்டம் 2005-ன் கீழ் அமைக்கப்பட்ட சட்டப்பூர்வ அமைப்பு\n4. 1952-ல் அமைக்கப்பட்ட அரசியலமைப்பில் இல்லாத, சட்டப்பூர்வமற்ற அமைப்பு",
    q27_opts, "A",
    "Correct matching: A-1 (NITI Aayog = Executive body), B-2 (Inter-State Council = Art 263 Constitutional body), C-3 (NDMA = Disaster Management Act 2005 Statutory body), D-4 (NDC = Extra-constitutional body 1952). Combination: A-1, B-2, C-3, D-4.",
    "சரியான பொருத்தம்: A-1 (நிதி ஆயோக் - நிர்வாக அமைப்பு), B-2 (மாநிலங்களிடை மன்றம் - விதி 263 அரசியலமைப்பு அமைப்பு), C-3 (NDMA - சட்டப்பூர்வ அமைப்பு), D-4 (NDC - 1952 அமைப்பு).",
    "Correct. A-1, B-2, C-3, D-4 is the exact status matching.",
    "சரி. A-1, B-2, C-3, D-4 என்பது சரியான பொருத்தமாகும்.",
    "Incorrect. Inter-State Council is Constitutional (Art 263).",
    "தவறு. மாநிலங்களிடை மன்றம் அரசியலமைப்பு அமைப்பாகும் (விதி 263).",
    "Incorrect. NITI Aayog is non-constitutional.",
    "தவறு. நிதி ஆயோக் அரசியலமைப்பில் இல்லாத அமைப்பாகும்.",
    "Incorrect. Check A matching with 1.",
    "தவறு. A-1 பொருத்தத்தைச் சரிபார்க்கவும்.",
    "TNPSC Tip: PM chairs bodies with different legal statuses: Inter-State Council = Constitutional (Art 263); NDMA = Statutory (2005 Act); NITI Aayog = Executive Cabinet Resolution (2015).",
    "தேர்வு உதவி: பிரதமர் தலைமை தாங்கும் அமைப்புகளின் சட்ட நிலை: மாநிலங்களிடை மன்றம் = அரசியலமைப்பு அமைப்பு; NDMA = சட்டப்பூர்வ அமைப்பு; நிதி ஆயோக் = நிர்வாக ஆணை அமைப்பு.",
    "The PM heads bodies across constitutional, statutory, and executive domains.",
    "அரசியலமைப்பு, சட்டப்பூர்வ மற்றும் நிர்வாக அமைப்புகளின் உச்சத் தலைவராகப் பிரதமர் உள்ளார்.",
    "Assuming NITI Aayog is a Constitutional body created under an Article.",
    "நிதி ஆயோக் ஒரு அரசியலமைப்பு விதி மூலம் உருவாக்கப்பட்டது என நினைப்பது.",
    pattern_basis="Based on PM-chaired apex bodies matching in TNPSC.",
    pyq_insight_en="Matching question on the legal character of bodies chaired ex-officio by the Prime Minister.",
    pyq_insight_ta="பிரதமர் தலைவராக உள்ள அமைப்புகளின் சட்ட அந்தஸ்தைப் பொருத்தும் வினாக்கள்.",
    sources=["Prime Minister Notes Part 2 - Section 5"]
))

# Q28: PYQ_PATTERN - Match / Political Theorists' Descriptions of PM
q28_opts = [
    make_opt("A", "A-1, B-2, C-3, D-4", "A-1, B-2, C-3, D-4"),
    make_opt("B", "A-2, B-1, C-4, D-3", "A-2, B-1, C-4, D-3"),
    make_opt("C", "A-3, B-4, C-1, D-2", "A-3, B-4, C-1, D-2"),
    make_opt("D", "A-4, B-3, C-2, D-1", "A-4, B-3, C-2, D-1")
]
questions.append(build_pyq_item(
    28, "Hard", "Match the Following",
    "Match List I (Political Scholar / Jurist) with List II (Description of Prime Minister):\nList I:\nA. Lord Morley\nB. Sir William Harcourt\nC. Sir Ivor Jennings\nD. Harold Laski\nList II:\n1. 'Keystone of the Cabinet Arch'\n2. 'Primus inter pares' (First among equals)\n3. 'A sun around which planets revolve'\n4. 'Pivot of the whole system of Government'",
    "பட்டியல் I-ல் உள்ள அரசியல் அறிஞர்களை பட்டியல் II-ல் உள்ள பிரதமரைப் பற்றிய அவர்களின் கூற்றுகளுடன் பொருத்துக:\nபட்டியல் I:\nA. மார்லி பிரபு (Lord Morley)\nB. சர் வில்லியம் ஹார்கோர்ட் (Sir William Harcourt)\nC. சர் ஐவர் ஜென்னிங்ஸ் (Sir Ivor Jennings)\nD. ஹரோல்ட் லாஸ்கி (Harold Laski)\nபட்டியல் II:\n1. 'அமைச்சரவை வளைவின் முதன்மை அச்சாணி' (Keystone of the Cabinet Arch)\n2. 'சமமானவர்களில் முதன்மையானவர்' (Primus inter pares)\n3. 'கிரகங்கள் சுற்றும் சூரியன்' (A sun around which planets revolve)\n4. 'அரசாங்க அமைப்பின் மைய அச்சு' (Pivot of the whole system of Government)",
    q28_opts, "A",
    "Correct matching: A-1 (Lord Morley: Keystone of Cabinet Arch), B-2 (Sir William Harcourt: Primus inter pares), C-3 (Jennings: Sun around which planets revolve), D-4 (Laski: Pivot of the whole system). Combination: A-1, B-2, C-3, D-4.",
    "சரியான பொருத்தம்: A-1 (மார்லி பிரபு - வளைவின் முதன்மை அச்சாணி), B-2 (ஹார்கோர்ட் - சமமானவர்களில் முதன்மையானவர்), C-3 (ஜென்னிங்ஸ் - கிரகங்கள் சுற்றும் சூரியன்), D-4 (லாஸ்கி - மைய அச்சு).",
    "Correct. A-1, B-2, C-3, D-4 is the exact scholar description match.",
    "சரி. A-1, B-2, C-3, D-4 என்பது சரியான பொருத்தமாகும்.",
    "Incorrect. Lord Morley coined 'Keystone of Cabinet Arch'.",
    "தவறு. மார்லி பிரபு 'அமைச்சரவை வளைவின் முதன்மை அச்சாணி' எனக் குறிப்பிட்டார்.",
    "Incorrect. Harcourt described PM as Primus inter pares.",
    "தவறு. ஹார்கோர்ட் 'சமமானவர்களில் முதன்மையானவர்' என்றார்.",
    "Incorrect. Check A matching with 1.",
    "தவறு. A-1 பொருத்தத்தைச் சரிபார்க்கவும்.",
    "TNPSC Tip: Lord Morley = Keystone of Cabinet Arch; Harcourt = Primus Inter Pares; Jennings = Sun around which planets revolve; Laski = Pivot of Government.",
    "தேர்வு உதவி: மார்லி பிரபு = கேபினட் வளைவின் அச்சாணி; ஹார்கோர்ட் = சமமானவர்களில் முதன்மையானவர்; ஜென்னிங்ஸ் = சூரியன்; லாஸ்கி = மைய அச்சு.",
    "These classical political quotes emphasize the central position of the Prime Minister in Cabinet government.",
    "இந்த அரசியல் பொன்மொழிகள் அமைச்சரவையில் பிரதமரின் முதன்மை இடத்தை வலியுறுத்துகின்றன.",
    "Confusing Lord Morley's quote (Keystone) with Harcourt's quote (Primus inter pares).",
    "மார்லி பிரபுவின் கூற்றையும் ஹார்கோர்ட்டின் கூற்றையும் குழப்பிக் கொள்ளுதல்.",
    pattern_basis="Based on political scholars' quotes matching in TNPSC Group 1.",
    pyq_insight_en="Match the Following testing famous political science quotes describing Prime Ministerial supremacy.",
    pyq_insight_ta="பிரதமரின் சிறப்பை விளக்கும் அரசியல் அறிஞர்களின் கூற்றுகளைப் பொருத்தும் வினாக்கள்.",
    sources=["Prime Minister Notes Part 1 - Section 7"]
))

# Q29: PYQ_PATTERN - Match / Prime Ministers from Rajya Sabha Years
q29_opts = [
    make_opt("A", "A-1, B-2, C-3, D-4", "A-1, B-2, C-3, D-4"),
    make_opt("B", "A-2, B-1, C-4, D-3", "A-2, B-1, C-4, D-3"),
    make_opt("C", "A-3, B-4, C-1, D-2", "A-3, B-4, C-1, D-2"),
    make_opt("D", "A-4, B-3, C-2, D-1", "A-4, B-3, C-2, D-1")
]
questions.append(build_pyq_item(
    29, "Medium", "Match the Following",
    "Match List I (Prime Minister appointed from Rajya Sabha) with List II (Year of First Appointment):\nList I:\nA. Indira Gandhi\nB. H.D. Deve Gowda\nC. I.K. Gujral\nD. Dr. Manmohan Singh\nList II:\n1. 1966\n2. 1996\n3. 1997\n4. 2004",
    "பட்டியல் I-ல் உள்ள மாநிலங்களவையிலிருந்து நியமிக்கப்பட்ட பிரதமர்களை பட்டியல் II-ல் உள்ள அவர்கள் முதன்முதலில் நியமிக்கப்பட்ட ஆண்டுகளுடன் பொருத்துக:\nபட்டியல் I:\nA. இந்திரா காந்தி\nB. எச்.டி. தேவ கவுடா\nC. ஐ.கே. குஜ்ரால்\nD. டாக்டர் மன்மோகன் சிங்\nபட்டியல் II:\n1. 1966\n2. 1996\n3. 1997\n4. 2004",
    q29_opts, "A",
    "Correct matching: A-1 (Indira Gandhi 1966), B-2 (H.D. Deve Gowda 1996), C-3 (I.K. Gujral 1997), D-4 (Dr. Manmohan Singh 2004). Combination: A-1, B-2, C-3, D-4.",
    "சரியான பொருத்தம்: A-1 (இந்திரா காந்தி 1966), B-2 (தேவ கவுடா 1996), C-3 (ஐ.கே. குஜ்ரால் 1997), D-4 (மன்மோகன் சிங் 2004).",
    "Correct. A-1, B-2, C-3, D-4 is the exact chronological matching.",
    "சரி. A-1, B-2, C-3, D-4 என்பது சரியான பொருத்தமாகும்.",
    "Incorrect. Indira Gandhi was appointed in 1966.",
    "தவறு. இந்திரா காந்தி 1966-ல் நியமிக்கப்பட்டார்.",
    "Incorrect. Deve Gowda was appointed in 1996.",
    "தவறு. தேவ கவுடா 1996-ல் நியமிக்கப்பட்டார்.",
    "Incorrect. Check A matching with 1.",
    "தவறு. A-1 பொருத்தத்தைச் சரிபார்க்கவும்.",
    "TNPSC Tip: All 4 Rajya Sabha PMs in order: Indira Gandhi (1966) -> Deve Gowda (1996) -> Gujral (1997) -> Manmohan Singh (2004).",
    "தேர்வு உதவி: மாநிலங்களவை பிரதமர்களின் வரிசை: இந்திரா காந்தி (1966) -> தேவ கவுடா (1996) -> குஜ்ரால் (1997) -> மன்மோகன் சிங் (2004).",
    "These four Prime Ministers represented Rajya Sabha at the time of taking oath as PM.",
    "இந்த நான்கு பிரதமர்களும் பதவியேற்கும்போது மாநிலங்களவை உறுப்பினர்களாக இருந்தனர்.",
    "Swapping the appointment years of H.D. Deve Gowda (1996) and I.K. Gujral (1997).",
    "தேவ கவுடா (1996) மற்றும் ஐ.கே. குஜ்ரால் (1997) ஆண்டுகளைக் குழப்பிக் கொள்ளுதல்.",
    pattern_basis="Based on Rajya Sabha PM historical timeline matching in TNPSC.",
    pyq_insight_en="Timeline matching of PMs who originated from the Rajya Sabha.",
    pyq_insight_ta="மாநிலங்களவையிலிருந்து வந்த பிரதமர்களின் காலவரிசைப் பொருத்தம்.",
    sources=["Prime Minister Notes Part 1 - Section 4"]
))

# Q30: PYQ_PATTERN - Match / Cabinet Committees Chairmanship
q30_opts = [
    make_opt("A", "A-1, B-2, C-3, D-4", "A-1, B-2, C-3, D-4"),
    make_opt("B", "A-2, B-1, C-4, D-3", "A-2, B-1, C-4, D-3"),
    make_opt("C", "A-3, B-4, C-1, D-2", "A-3, B-4, C-1, D-2"),
    make_opt("D", "A-4, B-3, C-2, D-1", "A-4, B-3, C-2, D-1")
]
questions.append(build_pyq_item(
    30, "Hard", "Match the Following",
    "Match List I (Cabinet Committee) with List II (Chairperson):\nList I:\nA. Political Affairs Committee ('Super-Cabinet')\nB. Appointments Committee of the Cabinet\nC. Cabinet Committee on Economic Affairs\nD. Cabinet Committee on Parliamentary Affairs\nList II:\n1. Prime Minister\n2. Prime Minister\n3. Prime Minister\n4. Union Home Minister (or senior Cabinet Minister)",
    "பட்டியல் I-ல் உள்ள கேபினட் குழுக்களை பட்டியல் II-ல் உள்ள அவர்களின் தலைவர்களுடன் பொருத்துக:\nபட்டியல் I:\nA. அரசியல் விவகாரங்களுக்கான கேபினட் குழு ('சூப்பர் கேபினட்')\nB. கேபினட் நியமனங்கள் குழு\nC. பொருளாதார விவகாரங்களுக்கான கேபினட் குழு\nD. நாடாளுமன்ற விவகாரங்களுக்கான கேபினட் குழு\nபட்டியல் II:\n1. பிரதமர்\n2. பிரதமர்\n3. பிரதமர்\n4. மத்திய உள்துறை அமைச்சர் (அல்லது மூத்த கேபினட் அமைச்சர்)",
    q30_opts, "A",
    "The PM chairs 3 out of 4 major Standing Cabinet Committees: Political Affairs, Appointments, and Economic Affairs. Parliamentary Affairs Committee is chaired by the Union Home Minister (or Minister of Parliamentary Affairs). Matching: A-1, B-2, C-3, D-4.",
    "பிரதமர் 3 முக்கிய கேபினட் குழுக்களுக்குத் தலைமை தாங்குகிறார் (அரசியல், நியமனங்கள், பொருளாதாரம்). நாடாளுமன்ற விவகாரக் குழுவிற்கு உள்துறை அமைச்சர் தலைமை தாங்குகிறார்.",
    "Correct. A-1, B-2, C-3, D-4 is the exact chairmanship match.",
    "சரி. A-1, B-2, C-3, D-4 என்பது சரியான பொருத்தமாகும்.",
    "Incorrect. PM does NOT chair the Parliamentary Affairs Committee.",
    "தவறு. நாடாளுமன்ற விவகாரக் குழுவிற்கு பிரதமர் தலைவரல்ல.",
    "Incorrect. Political Affairs Committee is chaired by PM.",
    "தவறு. அரசியல் விவகாரக் குழுவிற்கு பிரதமரே தலைவர்.",
    "Incorrect. Check D matching with 4.",
    "தவறு. D-4 பொருத்தத்தைச் சரிபார்க்கவும்.",
    "TNPSC Tip: Cabinet Committees Chaired by PM: Political Affairs, Appointments, Economic Affairs, Security. Exception: Parliamentary Affairs & Accommodation committees are NOT chaired by PM.",
    "தேர்வு உதவி: பிரதமர் தலைமை தாங்கும் குழுக்கள்: அரசியல், நியமனங்கள், பொருளாதாரம், பாதுகாப்பு. விதிவிலக்கு: நாடாளுமன்ற விவகாரக் குழுவிற்கு பிரதமர் தலைவரல்ல.",
    "Political Affairs Committee chaired by PM handles all domestic and foreign policy matters and is called 'Super Cabinet'.",
    "பிரதமர் தலைமை தாங்கும் அரசியல் விவகாரக் குழு 'சூப்பர் கேபினட்' என்று அழைக்கப்படுகிறது.",
    "Assuming the Prime Minister chairs ALL Cabinet Committees without exception.",
    "பிரதமர் அனைத்து கேபினட் குழுக்களுக்கும் விதிவிலக்கின்றி தலைமை தாங்குகிறார் என நினைப்பது.",
    pattern_basis="Based on Cabinet Committees chairmanship pattern in TNPSC Group 1.",
    pyq_insight_en="TNPSC tests the exception in Cabinet Committee chairmanships (Parliamentary Affairs Committee is NOT chaired by PM).",
    pyq_insight_ta="பிரதமர் தலைமை தாங்காத கேபினட் குழு (நாடாளுமன்ற விவகாரக் குழு) பற்றிய விதிவிலக்கு வினாக்கள்.",
    sources=["Prime Minister Notes Part 3 - Section 6"]
))

# Q31: PYQ_PATTERN - Chronology / Rajya Sabha PMs Order
q31_opts = [
    make_opt("A", "1 - 2 - 3 - 4", "1 - 2 - 3 - 4"),
    make_opt("B", "2 - 1 - 3 - 4", "2 - 1 - 3 - 4"),
    make_opt("C", "1 - 3 - 2 - 4", "1 - 3 - 2 - 4"),
    make_opt("D", "4 - 3 - 2 - 1", "4 - 3 - 2 - 1")
]
questions.append(build_pyq_item(
    31, "Medium", "Chronology",
    "Arrange the following Prime Ministers appointed from the Rajya Sabha in chronological order of their first appointment:\n1. Indira Gandhi\n2. H.D. Deve Gowda\n3. I.K. Gujral\n4. Dr. Manmohan Singh\nSelect the correct sequence:",
    "மாநிலங்களவையிலிருந்து நியமிக்கப்பட்ட பின்வரும் பிரதமர்களை அவர்கள் முதன்முதலில் நியமிக்கப்பட்ட காலவரிசையின்படி வரிசைப்படுத்துக:\n1. இந்திரா காந்தி\n2. எச்.டி. தேவ கவுடா\n3. ஐ.கே. குஜ்ரால்\n4. டாக்டர் மன்மோகன் சிங்\nசரியான வரிசையைத் தேர்ந்தெடுக்கவும்:",
    q31_opts, "A",
    "Chronological order: 1. Indira Gandhi (Jan 1966), 2. H.D. Deve Gowda (June 1996), 3. I.K. Gujral (April 1997), 4. Dr. Manmohan Singh (May 2004). Sequence: 1 - 2 - 3 - 4.",
    "சரியான காலவரிசை: 1. இந்திரா காந்தி (1966), 2. தேவ கவுடா (1996), 3. ஐ.கே. குஜ்ரால் (1997), 4. மன்மோகன் சிங் (2004). வரிசை: 1 - 2 - 3 - 4.",
    "Correct. 1 - 2 - 3 - 4 is the exact chronological timeline.",
    "சரி. 1 - 2 - 3 - 4 என்பது சரியான காலவரிசையாகும்.",
    "Incorrect. Deve Gowda (1996) preceded Gujral (1997).",
    "தவறு. தேவ கவுடா (1996) குஜ்ராலுக்கு (1997) முந்தையவர்.",
    "Incorrect. Gujral was appointed after Deve Gowda.",
    "தவறு. குஜ்ரால் தேவ கவுடாவுக்குப் பின் நியமிக்கப்பட்டார்.",
    "Incorrect. Reverse order.",
    "தவறு. தலைகீழ் வரிசை.",
    "TNPSC Tip: Memorize the RS PM sequence: Indira (1966) -> Gowda (1996) -> Gujral (1997) -> Manmohan (2004).",
    "தேர்வு உதவி: மாநிலங்களவை பிரதமர்கள் வரிசை: இந்திரா (1966) -> தேவகவுடா (1996) -> குஜ்ரால் (1997) -> மன்மோகன் (2004).",
    "Indira Gandhi established the precedent that a Rajya Sabha member can hold the premiership.",
    "மாநிலங்களவை உறுப்பினரும் பிரதமராகலாம் என்ற முன்மாதிரியை இந்திரா காந்தி ஏற்படுத்தினார்.",
    "Placing I.K. Gujral before H.D. Deve Gowda in the United Front government timeline.",
    "ஐ.கே. குஜ்ராலை தேவ கவுடாவுக்கு முன் வரிசைப்படுத்துவது.",
    pattern_basis="Based on PM chronological timeline sequence in TNPSC.",
    pyq_insight_en="Chronological arrangement testing the sequence of non-Lok Sabha Prime Ministers.",
    pyq_insight_ta="மாநிலங்களவைப் பிரதமர்களின் காலவரிசை குறித்த வினாக்கள்.",
    sources=["Prime Minister Notes Part 1 - Section 4"]
))

# Q32: PYQ_PATTERN - Chronology / No-Confidence Motions Timeline
q32_opts = [
    make_opt("A", "1 - 2 - 3 - 4", "1 - 2 - 3 - 4"),
    make_opt("B", "2 - 1 - 4 - 3", "2 - 1 - 4 - 3"),
    make_opt("C", "3 - 1 - 2 - 4", "3 - 1 - 2 - 4"),
    make_opt("D", "1 - 3 - 2 - 4", "1 - 3 - 2 - 4")
]
questions.append(build_pyq_item(
    32, "Hard", "Chronology",
    "Arrange the following Prime Ministers in chronological order based on when the FIRST No-Confidence Motion was moved against their respective ministries:\n1. Jawaharlal Nehru (Aug 1963)\n2. Lal Bahadur Shastri (Sept 1964)\n3. Indira Gandhi (Nov 1966)\n4. Morarji Desai (May 1978)\nSelect the correct sequence:",
    "பின்வரும் பிரதமர்களை அவர்களின் அமைச்சரவைக்கு எதிராக முதல் நம்பிக்கையில்லா தீர்மானம் கொண்டு வரப்பட்ட காலவரிசையின்படி வரிசைப்படுத்துக:\n1. ஜவகர்லால் நேரு (ஆகஸ்ட் 1963)\n2. லால் பகதூர் சாஸ்திரி (செப்டம்பர் 1964)\n3. இந்திரா காந்தி (நவம்பர் 1966)\n4. மொரார்ஜி தேசாய் (மே 1978)\nசரியான வரிசையைத் தேர்ந்தெடுக்கவும்:",
    q32_opts, "A",
    "Chronological sequence of first No-Confidence Motions against PMs: 1. Nehru (Aug 1963 by J.B. Kripalani), 2. Shastri (Sept 1964 by N.C. Chatterjee), 3. Indira Gandhi (Nov 1966 by Umanath), 4. Morarji Desai (May 1978). Sequence: 1 - 2 - 3 - 4.",
    "முதல் நம்பிக்கையில்லா தீர்மானம் வரிசை: 1. நேரு (ஆகஸ்ட் 1963), 2. சாஸ்திரி (செப்டம்பர் 1964), 3. இந்திரா காந்தி (நவம்பர் 1966), 4. மொரார்ஜி தேசாய் (மே 1978).",
    "Correct. 1 - 2 - 3 - 4 is the exact chronological sequence.",
    "சரி. 1 - 2 - 3 - 4 என்பது சரியான காலவரிசையாகும்.",
    "Incorrect. Nehru was the first in 1963.",
    "தவறு. நேரு 1963-ல் முதன்மையானவர்.",
    "Incorrect. Indira Gandhi was third in 1966.",
    "தவறு. இந்திரா காந்தி 1966-ல் மூன்றாவதாக எதிர்நோக்கினார்.",
    "Incorrect. Shastri was second in 1964.",
    "தவறு. சாஸ்திரி 1964-ல் இரண்டாவதாக எதிர்நோக்கினார்.",
    "TNPSC Tip: First PM to face No-Confidence = Nehru (1963); First PM whose government FELL due to No-Confidence = Morarji Desai (1979).",
    "தேர்வு உதவி: நம்பிக்கையில்லா தீர்மானத்தை முதலில் எதிர்நோக்கியவர் = நேரு (1963); தீர்மானத்தால் ஆட்சியை இழந்த முதல் பிரதமர் = மொரார்ஜி தேசாய் (1979).",
    "A No-Confidence Motion requires the support of at least 50 members for admission in Lok Sabha under Rule 198.",
    "நம்பிக்கையில்லா தீர்மானம் ஏற்றுக்கொள்ளப்பட மக்களவையில் குறைந்தபட்சம் 50 உறுப்பினர்களின் ஆதரவு தேவை (விதி 198).",
    "Confusing the year of the first motion against Nehru (1963) with Shastri's motion (1964).",
    "நேருவுக்கு எதிரான முதல் தீர்மான ஆண்டையும் (1963) சாஸ்திரியின் ஆண்டையும் (1964) குழப்புதல்.",
    pattern_basis="Based on Parliamentary motion historical chronology in Group 1.",
    pyq_insight_en="Chronological question on parliamentary confidence motions against Union Prime Ministers.",
    pyq_insight_ta="பிரதமர்களுக்கு எதிரான நம்பிக்கையில்லா தீர்மானங்களின் காலவரிசை வினாக்கள்.",
    sources=["Prime Minister Notes Part 3 - Section 1"]
))

# Q33: PYQ_PATTERN - Chronology / Constitutional Amendments related to PM
q33_opts = [
    make_opt("A", "1 - 2 - 3", "1 - 2 - 3"),
    make_opt("B", "2 - 1 - 3", "2 - 1 - 3"),
    make_opt("C", "3 - 1 - 2", "3 - 1 - 2"),
    make_opt("D", "1 - 3 - 2", "1 - 3 - 2")
]
questions.append(build_pyq_item(
    33, "Medium", "Chronology",
    "Arrange the following Constitutional Amendment Acts affecting the PM and Cabinet in chronological order:\n1. 42nd Amendment Act (Made advice of COM headed by PM binding on President)\n2. 44th Amendment Act (Allowed President to send back advice for reconsideration ONCE & defined Cabinet in Art 352)\n3. 91st Amendment Act (Capped Union Council of Ministers strength at 15% of Lok Sabha)\nSelect the correct sequence:",
    "பிரதமர் மற்றும் கேபினட்டை பாதித்த பின்வரும் அரசியலமைப்புச் சட்டத்திருத்தங்களை காலவரிசைப்படி வரிசைப்படுத்துக:\n1. 42-வது சட்டத்திருத்தம் (பிரதமர் தலைமையிலான ஆலோசனையை குடியரசுத் தலைவருக்குக் கட்டாயமாக்கியது)\n2. 44-வது சட்டத்திருத்தம் (ஆலோசனையை ஒருமுறை மறுபரிசீலனைக்கு அனுப்ப அனுமதித்தது & விதி 352-ல் கேபினட்டை வரையறுத்தது)\n3. 91-வது சட்டத்திருத்தம் (அமைச்சரவை எண்ணிக்கையை மக்களவையின் 15% என வரம்பிட்டது)\nசரியான வரிசையைத் தேர்ந்தெடுக்கவும்:",
    q33_opts, "A",
    "Chronological order: 1. 42nd Amendment Act (1976), 2. 44th Amendment Act (1978), 3. 91st Amendment Act (2003). Sequence: 1 - 2 - 3.",
    "சரியான காலவரிசை: 1. 42-வது சட்டத்திருத்தம் (1976), 2. 44-வது சட்டத்திருத்தம் (1978), 3. 91-வது சட்டத்திருத்தம் (2003). வரிசை: 1 - 2 - 3.",
    "Correct. 1 - 2 - 3 is the exact chronological order of these landmark amendments.",
    "சரி. 1 - 2 - 3 என்பது சரியான காலவரிசையாகும்.",
    "Incorrect. 42nd (1976) preceded 44th (1978).",
    "தவறு. 42-வது திருத்தம் (1976) 44-வது திருத்தத்திற்கு (1978) முந்தியது.",
    "Incorrect. 91st Amendment was enacted in 2003.",
    "தவறு. 91-வது திருத்தம் 2003-ல் கொண்டுவரப்பட்டது.",
    "Incorrect. Check sequence.",
    "தவறு. வரிசையைச் சரிபார்க்கவும்.",
    "TNPSC Tip: Landmark Amendment Years: 42nd = 1976; 44th = 1978; 91st = 2003.",
    "தேர்வு உதவி: முக்கியத் திருத்த ஆண்டுகள்: 42-வது = 1976; 44-வது = 1978; 91-வது = 2003.",
    "These three amendments reshaped the executive balance between President, Prime Minister, and Cabinet size.",
    "இந்த மூன்று திருத்தங்களும் குடியரசுத் தலைவர், பிரதமர் மற்றும் கேபினட் இடையிலான தொடர்பை மறுவடிவமைத்தன.",
    "Placing 91st Amendment (2003) before 44th Amendment (1978).",
    "91-வது திருத்தத்தை (2003) 44-வது திருத்தத்திற்கு (1978) முன் வரிசைப்படுத்துவது.",
    pattern_basis="Based on Constitutional Amendment chronological timeline in TNPSC.",
    pyq_insight_en="Chronological question testing major constitutional amendments governing executive cabinet rules.",
    pyq_insight_ta="நிர்வாக கேபினட் விதிகளை மாற்றிய முக்கிய சட்டத்திருத்தங்களின் காலவரிசை.",
    sources=["Prime Minister Notes Part 1, 2 & 3"]
))

# Q34: PYQ_PATTERN - Chronology / Coalition Presidential Precedents
q34_opts = [
    make_opt("A", "1 - 2 - 3 - 4", "1 - 2 - 3 - 4"),
    make_opt("B", "2 - 1 - 3 - 4", "2 - 1 - 3 - 4"),
    make_opt("C", "1 - 3 - 2 - 4", "1 - 3 - 2 - 4"),
    make_opt("D", "4 - 3 - 2 - 1", "4 - 3 - 2 - 1")
]
questions.append(build_pyq_item(
    34, "Hard", "Chronology",
    "Arrange the following historical Presidential invitations to form coalition governments in a Hung Lok Sabha in chronological order:\n1. President Neelam Sanjiva Reddy inviting Charan Singh (1979)\n2. President R. Venkataraman inviting V.P. Singh (1989)\n3. President Shankar Dayal Sharma inviting A.B. Vajpayee (1996)\n4. President K.R. Narayanan inviting A.B. Vajpayee (1998)\nSelect the correct sequence:",
    "தொங்கு மக்களவையில் கூட்டணி அரசு அமைக்க குடியரசுத் தலைவர்கள் அழைப்பு விடுத்த பின்வரும் வரலாற்று நிகழ்வுகளை காலவரிசைப்படி வரிசைப்படுத்துக:\n1. சரண் சிங்கிற்கு குடியரசுத் தலைவர் நீலம் சஞ்சீவ ரெட்டி அழைப்பு (1979)\n2. வி.பி. சிங்கிற்கு குடியரசுத் தலைவர் ஆர். வெங்கடராமன் அழைப்பு (1989)\n3. ஏ.பி. வஜ்பாயிக்கு குடியரசுத் தலைவர் சங்கர் தயாள் சர்மா அழைப்பு (1996)\n4. ஏ.பி. வஜ்பாயிக்கு குடியரசுத் தலைவர் கே.ஆர். நாராயணன் அழைப்பு (1998)\nசரியான வரிசையைத் தேர்ந்தெடுக்கவும்:",
    q34_opts, "A",
    "Chronological sequence of Hung Lok Sabha invitations: 1. N. Sanjiva Reddy -> Charan Singh (1979), 2. R. Venkataraman -> V.P. Singh (1989), 3. S.D. Sharma -> Vajpayee (13-day government 1996), 4. K.R. Narayanan -> Vajpayee (1998). Sequence: 1 - 2 - 3 - 4.",
    "சரியான காலவரிசை: 1. நீலம் சஞ்சீவ ரெட்டி -> சரண் சிங் (1979), 2. ஆர். வெங்கடராமன் -> வி.பி. சிங் (1989), 3. சங்கர் தயாள் சர்மா -> வஜ்பாயி (1996), 4. கே.ஆர். நாராயணன் -> வஜ்பாயி (1998).",
    "Correct. 1 - 2 - 3 - 4 is the exact chronological timeline.",
    "சரி. 1 - 2 - 3 - 4 என்பது சரியான காலவரிசையாகும்.",
    "Incorrect. 1979 was the first hung house exercise by N. Sanjiva Reddy.",
    "தவறு. 1979-ல் நீலம் சஞ்சீவ ரெட்டியே முதன்முறையாக விருப்ப அதிகாரத்தைப் பயன்படுத்தினார்.",
    "Incorrect. Venkataraman invited V.P. Singh in 1989.",
    "தவறு. வெங்கடராமன் 1989-ல் வி.பி. சிங்கிற்கு அழைப்பு விடுத்தார்.",
    "Incorrect. Reverse sequence.",
    "தவறு. தலைகீழ் வரிசை.",
    "TNPSC Tip: 1979 Charan Singh invitation by N. Sanjiva Reddy was the FIRST time a President exercised individual discretion in appointing a coalition PM.",
    "தேர்வு உதவி: 1979-ல் நீலம் சஞ்சீவ ரெட்டி சரண் சிங்கிற்கு அழைப்பு விடுத்ததே குடியரசுத் தலைவர் முதன்முதலில் சுயவிருப்ப அதிகாரத்தைப் பயன்படுத்திய நிகழ்வாகும்.",
    "Presidential discretion in appointing PMs became prominent during the coalition era (1979–1999).",
    "கூட்டணி ஆட்சிக் காலத்தில் (1979-1999) பிரதமரை நியமிப்பதில் குடியரசுத் தலைவரின் விருப்ப அதிகாரம் முதன்மை பெற்றது.",
    "Confusing the 1996 Vajpayee invitation (S.D. Sharma) with the 1998 invitation (K.R. Narayanan).",
    "1996 வஜ்பாயி அழைப்பையும் (சங்கர் தயாள் சர்மா) 1998 அழைப்பையும் (கே.ஆர். நாராயணன்) குழப்புதல்.",
    pattern_basis="Based on Hung Lok Sabha historical timeline matching in TNPSC Group 1.",
    pyq_insight_en="Historical chronology of coalition PM invitations by successive Presidents of India.",
    pyq_insight_ta="கூட்டணி அரசு அமைக்க குடியரசுத் தலைவர்கள் அழைப்பு விடுத்த வரலாற்றுக் காலவரிசை.",
    sources=["Prime Minister Notes Part 3 - Section 3"]
))

# Q35: PYQ_PATTERN - Chronology / PM Milestones
q35_opts = [
    make_opt("A", "1 - 2 - 3", "1 - 2 - 3"),
    make_opt("B", "2 - 1 - 3", "2 - 1 - 3"),
    make_opt("C", "3 - 1 - 2", "3 - 1 - 2"),
    make_opt("D", "1 - 3 - 2", "1 - 3 - 2")
]
questions.append(build_pyq_item(
    35, "Medium", "Chronology",
    "Arrange the following milestones in Indian Prime Ministerial history in chronological order:\n1. First appointment of a Prime Minister who was NOT an MP of either House at the time of taking oath (H.D. Deve Gowda - May 1996)\n2. First non-Congress Prime Minister to complete a full 5-year term in office (A.B. Vajpayee - 1999 to 2004)\n3. First Prime Minister to complete two full consecutive terms while remaining a Rajya Sabha member throughout (Dr. Manmohan Singh - 2004 to 2014)\nSelect the correct sequence:",
    "இந்தியப் பிரதமர்களின் வரலாற்றில் பின்வரும் முக்கிய மைல்கற்களை காலவரிசைப்படி வரிசைப்படுத்துக:\n1. பதவியேற்கும்போது இரு அவைகளிலும் எம்பி-யாக இல்லாத ஒருவர் பிரதமராக முதன்முதலில் நியமிக்கப்பட்டது (தேவ கவுடா - மே 1996)\n2. 5 ஆண்டு கால முழு பதவிக்காலத்தையும் நிறைவு செய்த முதல் காங்கிரஸ் அல்லாத பிரதமர் (ஏ.பி. வஜ்பாயி - 1999-2004)\n3. தொடர்ந்து இரு முழு பதவிக்காலங்களையும் மாநிலங்களவை எம்பியாகவே இருந்து நிறைவு செய்த முதல் பிரதமர் (டாக்டர் மன்மோகன் சிங் - 2004-2014)\nசரியான வரிசையைத் தேர்ந்தெடுக்கவும்:",
    q35_opts, "A",
    "Chronological order of milestones: 1. Deve Gowda appointed non-MP PM (May 1996), 2. Vajpayee completed full non-Congress 5-year term (Oct 1999 - May 2004), 3. Manmohan Singh served two full terms as RS PM (2004 - 2014). Sequence: 1 - 2 - 3.",
    "சரியான காலவரிசை: 1. எம்பி அல்லாத தேவ கவுடா நியமனம் (1996), 2. வஜ்பாயி 5 ஆண்டு ஆட்சியை நிறைவு செய்தது (1999-2004), 3. மன்மோகன் சிங் இரு பதவிக்காலங்களை நிறைவு செய்தது (2004-2014). வரிசை: 1 - 2 - 3.",
    "Correct. 1 - 2 - 3 is the exact chronological milestone sequence.",
    "சரி. 1 - 2 - 3 என்பது சரியான காலவரிசையாகும்.",
    "Incorrect. Deve Gowda's appointment (1996) preceded Vajpayee's full term (1999-2004).",
    "தவறு. தேவ கவுடாவின் நியமனம் (1996) வஜ்பாயியின் முழு ஆட்சிக் காலத்திற்கு (1999) முந்தியது.",
    "Incorrect. Manmohan Singh's terms started in 2004.",
    "தவறு. மன்மோகன் சிங்கின் பதவிக்காலம் 2004-ல் தொடங்கியது.",
    "Incorrect. Check sequence.",
    "தவறு. வரிசையைச் சரிபார்க்கவும்.",
    "TNPSC Tip: First non-Congress PM = Morarji Desai (1977); First non-Congress PM to complete FULL 5 years = A.B. Vajpayee (1999-2004).",
    "தேர்வு உதவி: முதல் காங்கிரஸ் அல்லாத பிரதமர் = மொரார்ஜி தேசாய் (1977); 5 ஆண்டுகள் முழுமையாக ஆட்சி செய்த முதல் காங்கிரஸ் அல்லாதவர் = ஏ.பி. வஜ்பாயி (1999-2004).",
    "Deve Gowda took oath in May 1996 as a non-MP and was subsequently elected to Rajya Sabha from Karnataka in Sept 1996.",
    "தேவ கவுடா எம்பியாக இல்லாமல் பிரதமராகி பின்னர் கர்நாடகாவிலிருந்து மாநிலங்களவைக்குத் தேர்ந்தெடுக்கப்பட்டார்.",
    "Confusing Morarji Desai (first non-Congress PM, 1977) with Vajpayee (first non-Congress PM to complete full 5 years, 1999-2004).",
    "மொரார்ஜி தேசாயையும் (முதல் காங்கிரஸ் அல்லாதவர்) வஜ்பாயியையும் (5 ஆண்டுகள் முழுமையாக நிறைவு செய்த முதல் காங்கிரஸ் அல்லாதவர்) குழப்புதல்.",
    pattern_basis="Based on Prime Ministerial historical milestone ordering in Group 1.",
    pyq_insight_en="Chronological evaluation of distinct political milestones in Prime Ministerial history.",
    pyq_insight_ta="பிரதமர் வரலாற்றின் முக்கிய மைல்கற்களை வரிசைப்படுத்தும் வினாக்கள்.",
    sources=["Prime Minister Notes Part 1 & Part 3"]
))

# Q36: PYQ_PATTERN - Direct / Oath of Secrecy Purpose
q36_opts = [
    make_opt("A", "Not to reveal government decisions to the Election Commission", "அரசு முடிவுகளை தேர்தல் ஆணையத்திற்கு வெளிப்படுத்தக்கூடாது"),
    make_opt("B", "Not to directly or indirectly communicate or reveal any matter brought under consideration as a Minister except as required for discharge of duties", "தன் பரிசீலனைக்குக் கொண்டுவரப்படும் எந்தவொரு விஷயத்தையும் கடமைக்குத் தேவையானதைத் தவிர நேரடியாவோ மறைமுகமாகவோ வெளிப்படுத்தக்கூடாது"),
    make_opt("C", "Not to disclose personal asset details to the Parliament", "நாடாளுமன்றத்திற்குத் தன் தனிப்பட்ட சொத்து விவரங்களை வெளிப்படுத்தக்கூடாது"),
    make_opt("D", "Not to communicate with State Chief Ministers regarding policy matters", "கொள்கை விஷயங்கள் குறித்து மாநில முதலமைச்சர்களுடன் தொடர்பு கொள்ளக்கூடாது")
]
questions.append(build_pyq_item(
    36, "Medium", "Direct MCQ",
    "Under Schedule III of the Constitution, what is the exact constitutional pledge made in the 'Oath of Secrecy' taken by the Prime Minister?",
    "அரசியலமைப்பின் 3-வது அட்டவணையின் கீழ், பிரதமர் ஏற்கும் 'இரகசியக் காப்புப் பிரமாணத்தின்' (Oath of Secrecy) துல்லியமான வாக்குறுதி என்ன?",
    q36_opts, "B",
    "The Oath of Secrecy in the Third Schedule states that the Minister will NOT directly or indirectly communicate or reveal to any person any matter brought under consideration or known to him as a Union Minister except as required for the due discharge of his duties.",
    "3-வது அட்டவணையின் இரகசியக் காப்புப் பிரமாணம் கூறுவது: தன் கடமை ஆற்றுவதற்குத் தேவையானதைத் தவிர வேறு எவருக்கும் தன் பரிசீலனைக்கு வரும் விஷயங்களை நேரடியாவோ மறைமுகமாகவோ தெரிவிக்கக் கூடாது.",
    "Incorrect. Oath of Secrecy does not apply to legal election disclosures.",
    "தவறு. இது தேர்தல் ஆணையத் தகவல்களுடன் தொடர்பில்லாதது.",
    "Correct. Option B reflects the exact text of the Oath of Secrecy under Schedule III.",
    "சரி. விருப்பம் B என்பது 3-வது அட்டவணையில் உள்ள இரகசியக் காப்புப் பிரமாணத்தின் துல்லியமான உரையாகும்.",
    "Incorrect. Asset disclosures are governed by representation of people rules, not secrecy oath.",
    "தவறு. சொத்து விவரங்கள் மக்கள் பிரதிநிதித்துவச் சட்டத்துடன் தொடர்புடையவை.",
    "Incorrect. PM frequently communicates with CMs under federal administration.",
    "தவறு. பிரதமர் முதலமைச்சர்களுடன் தொடர்பு கொள்வது கூட்டாட்சி நிர்வாகத்தின் பகுதியாகும்.",
    "TNPSC Tip: Ministers take TWO separate oaths: (1) Oath of Office, and (2) Oath of Secrecy. Both are prescribed in the Third Schedule.",
    "தேர்வு உதவி: அமைச்சர்கள் இரு பிரமாணங்களை ஏற்கின்றனர்: (1) பதவிப் பிரமாணம், (2) இரகசியக் காப்புப் பிரமாணம். இரண்டும் 3-வது அட்டவணையில் உள்ளன.",
    "Oath of Secrecy preserves Cabinet confidentiality which underpins Cabinet solidarity and collective responsibility.",
    "இரகசியக் காப்புப் பிரமாணம் கேபினட்டின் இரகசியத் தன்மையைப் பாதுகாக்கிறது.",
    "Confusing Oath of Office (faith in Constitution) with Oath of Secrecy (non-disclosure of ministerial business).",
    "பதவிப் பிரமாணத்தையும் இரகசியக் காப்புப் பிரமாணத்தையும் குழப்பிக் கொள்ளுதல்.",
    pattern_basis="Based on Schedule III oath text questions in TNPSC.",
    pyq_insight_en="TNPSC tests the specific wording and purpose of the Oath of Secrecy prescribed in Schedule III.",
    pyq_insight_ta="3-வது அட்டவணையில் உள்ள இரகசியக் காப்புப் பிரமாணத்தின் நோக்கம் பற்றிய வினாக்கள்.",
    sources=["Prime Minister Notes Part 1 - Section 5"]
))

# Q37: PYQ_PATTERN - Direct / Pleasure Doctrine Art 75(2)
q37_opts = [
    make_opt("A", "The President can dismiss the Prime Minister at any time at his sole discretion", "குடியரசுத் தலைவர் தனது விருப்பப்படி எந்த நேரத்திலும் பிரதமரை நீக்கலாம்"),
    make_opt("B", "The President can dismiss any individual minister without taking advice from the Prime Minister", "பிரதமரின் ஆலோசனையின்றி எந்தவொரு தனி அமைச்சரையும் குடியரசுத் தலைவர் நீக்கலாம்"),
    make_opt("C", "The President exercises the power of dismissal ONLY on the advice of the Prime Minister, so long as the ministry retains Lok Sabha majority", "அமைச்சரவை மக்களவை பெரும்பான்மையைத் தக்கவைத்துள்ள வரை, பிரதமரின் ஆலோசனையின் பேரில் மட்டுமே குடியரசுத் தலைவர் நீக்கும் அதிகாரத்தைப் பயன்படுத்துகிறார்"),
    make_opt("D", "The Supreme Court must approve every ministerial dismissal", "அமைச்சரின் ஒவ்வொரு நீக்கத்திற்கும் உச்ச நீதிமன்றம் ஒப்புதல் அளிக்க வேண்டும்")
]
questions.append(build_pyq_item(
    37, "Hard", "Direct MCQ",
    "What is the actual constitutional interpretation of the clause 'ministers hold office during the pleasure of the President' under Article 75(2)?",
    "உறுப்பு 75(2)-ன் கீழ் 'அமைச்சர்கள் குடியரசுத் தலைவரின் விருப்பம் வரை பதவியில் நீடிப்பர்' என்ற தொடரின் உண்மையான அரசியலமைப்பு விளக்கம் என்ன?",
    q37_opts, "C",
    "Under Article 75(2) read with Article 74(1), the 'pleasure of the President' is NOT the personal pleasure of the President. It is exercised on the advice of the Prime Minister. The President CANNOT dismiss a PM or minister who enjoys the confidence of the Lok Sabha.",
    "விதி 75(2) மற்றும் 74(1)-ன் படி, 'குடியரசுத் தலைவரின் விருப்பம்' என்பது அவரது சொந்த தன்னிச்சையான விருப்பமல்ல. அது பிரதமரின் ஆலோசனையின் பேரிலேயே பயன்படுத்தப்படுகிறது.",
    "Incorrect. President cannot dismiss a PM who has Lok Sabha majority.",
    "தவறு. மக்களவை பெரும்பான்மை உள்ள பிரதமரை குடியரசுத் தலைவர் நீக்க முடியாது.",
    "Incorrect. Individual minister dismissal requires PM advice.",
    "தவறு. தனி அமைச்சரையும் பிரதமரின் ஆலோசனையின்றி நீக்க முடியாது.",
    "Correct. Pleasure of President is exercised on PM advice while government enjoys Lok Sabha majority.",
    "சரி. மக்களவை பெரும்பான்மை இருக்கும் வரை பிரதமரின் ஆலோசனையின் பேரிலேயே விருப்ப அதிகாரம் செயல்படுகிறது.",
    "Incorrect. Judiciary does not approve executive ministerial dismissals.",
    "தவறு. நீதித்துறைக்கு இதில் ஒப்புதல் அதிகாரம் இல்லை.",
    "TNPSC Tip: 'Pleasure of President' in Art 75(2) = Controlled by PM advice. 'Pleasure of Governor' in Art 164(1) = Controlled by CM advice.",
    "தேர்வு உதவி: விதி 75(2)-ல் 'குடியரசுத் தலைவர் விருப்பம்' என்பது பிரதமரின் கட்டுப்பாட்டிலும், 164(1)-ல் 'ஆளுநர் விருப்பம்' முதலமைச்சரின் கட்டுப்பாட்டிலும் உள்ளது.",
    "The pleasure doctrine ensures individual responsibility of ministers to the Prime Minister.",
    "விருப்பக் கோட்பாடு அமைச்சர்களின் தனிநபர் பொறுப்பை பிரதமரிடம் உறுதி செய்கிறது.",
    "Assuming 'pleasure of the President' gives the President absolute personal veto power to dismiss ministers independently.",
    "குடியரசுத் தலைவர் தன்னிச்சையாக அமைச்சர்களை நீக்கலாம் என தவறாகக் கருதுதல்.",
    pattern_basis="Based on Article 75(2) pleasure doctrine interpretation in Group 1.",
    pyq_insight_en="TNPSC tests the constitutional convention limiting presidential pleasure by PM advice.",
    pyq_insight_ta="குடியரசுத் தலைவரின் விருப்ப அதிகாரம் பிரதமரின் ஆலோசனைக்கு உட்பட்டது என்ற அரசியலமைப்பு விளக்கம்.",
    sources=["Prime Minister Notes Part 1 - Section 5"]
))

# Q38: PYQ_PATTERN - Direct / Advising Lok Sabha Dissolution
q38_opts = [
    make_opt("A", "Yes, the PM can advise dissolution at any time if he retains majority support in the Lok Sabha", "ஆம், மக்களவையில் பெரும்பான்மை ஆதரவு இருக்கும் வரை பிரதமர் எந்த நேரத்திலும் அவையைக் கலைக்கப் பரிந்துரைக்கலாம்"),
    make_opt("B", "No, Lok Sabha can only be dissolved after completing 5 full years", "இல்லை, 5 ஆண்டுகள் முழுமையாக முடிந்த பிறகே மக்களவையைக் கலைக்க முடியும்"),
    make_opt("C", "Yes, but only with 2/3rd approval of the Rajya Sabha", "ஆம், ஆனால் மாநிலங்களவையின் 2/3 பங்கு ஒப்புதலுடன் மட்டுமே சாத்தியம்"),
    make_opt("D", "No, only the Speaker of Lok Sabha can dissolve the House", "இல்லை, மக்களவை சபாநாயகர் மட்டுமே அவையைக் கலைக்க முடியும்")
]
questions.append(build_pyq_item(
    38, "Medium", "Direct MCQ",
    "Can the Prime Minister advise the President to dissolve the Lok Sabha before the expiry of its normal five-year tenure?",
    "மக்களவையின் இயல்பான 5 ஆண்டு கால அளவு முடிவதற்கு முன்பாகவே அதனைக் கலைக்குமாறு குடியரசுத் தலைவருக்குப் பிரதமர் பரிந்துரைக்க முடியுமா?",
    q38_opts, "A",
    "Under Article 85(2)(b), the President has the power to dissolve the Lok Sabha. By convention, the President accepts the advice of a Prime Minister who enjoys majority support in Lok Sabha to dissolve the House prematurely and call fresh elections.",
    "விதி 85(2)(b)-ன் படி மக்களவையைக் கலைக்கும் அதிகாரம் குடியரசுத் தலைவரிடம் உள்ளது. பெரும்பான்மை உள்ள பிரதமர் 5 ஆண்டுகள் முடியும் முன்பே அவையைக் கலைக்கப் பரிந்துரைக்கலாம், அதனை குடியரசுத் தலைவர் ஏற்பார்.",
    "Correct. PM retaining majority support can advise dissolution of Lok Sabha at any time.",
    "சரி. பெரும்பான்மை உள்ள பிரதமர் எப்போது வேண்டுமானாலும் மக்களவையைக் கலைக்கப் பரிந்துரைக்கலாம்.",
    "Incorrect. Lok Sabha can be dissolved prematurely before 5 years.",
    "தவறு. 5 ஆண்டுகள் முடியும் முன்பே மக்களவையைக் கலைக்க முடியும்.",
    "Incorrect. Rajya Sabha approval is not required for Lok Sabha dissolution.",
    "தவறு. மாநிலங்களவை ஒப்புதல் தேவையில்லை.",
    "Incorrect. Speaker cannot dissolve Lok Sabha; only President can under Art 85(2)(b).",
    "தவறு. சபாநாயகரால் அவையைக் கலைக்க முடியாது, குடியரசுத் தலைவரால் மட்டுமே முடியும்.",
    "TNPSC Tip: Dissolution of Lok Sabha = Article 85(2)(b). Advised by PM. Rajya Sabha CANNOT be dissolved (Permanent Body).",
    "தேர்வு உதவி: மக்களவைக் கலைப்பு = விதி 85(2)(b). பிரதமரின் ஆலோசனையின் படி. மாநிலங்களவை ஒருபோதும் கலைக்கப்பட முடியாது (நிரந்தர அவை).",
    "The power to advise Lok Sabha dissolution is a potent political weapon used by the PM to seek a fresh mandate.",
    "மக்களவையைக் கலைக்கப் பரிந்துரைக்கும் அதிகாரம் புதிய மக்களாணையைக் கோர பிரதமருக்கு உள்ள முக்கிய அரசியல் ஆயுதமாகும்.",
    "Thinking Rajya Sabha must concur before Lok Sabha can be dissolved by the President.",
    "மக்களவையைக் கலைக்க மாநிலங்களவையின் இசைவு தேவை என நினைப்பது.",
    pattern_basis="Based on Article 85(2)(b) dissolution advice questions in TNPSC.",
    pyq_insight_en="TNPSC tests the PM's prerogative to advise premature dissolution of Lok Sabha.",
    pyq_insight_ta="மக்களவையை முன்கூட்டியே கலைக்கப் பரிந்துரைக்கும் பிரதமரின் உரிமை பற்றிய வினாக்கள்.",
    sources=["Prime Minister Notes Part 2 - Section 4"]
))

# Q39: PYQ_PATTERN - Direct / Leader of the House in Lok Sabha
q39_opts = [
    make_opt("A", "Speaker of Lok Sabha automatically becomes Leader of the House", "மக்களவை சபாநாயகர் தானாகவே அவைத் தலைவராகிறார்"),
    make_opt("B", "A senior Cabinet Minister who is a member of Lok Sabha, nominated by the Prime Minister", "பிரதமரால் பரிந்துரைக்கப்படும் மக்களவை உறுப்பினரான ஒரு மூத்த கேபினட் அமைச்சர்"),
    make_opt("C", "Leader of the Opposition in Lok Sabha", "மக்களவை எதிர்க்கட்சித் தலைவர்"),
    make_opt("D", "Deputy Speaker of Lok Sabha", "மக்களவை துணை சபாநாயகர்")
]
questions.append(build_pyq_item(
    39, "Medium", "Direct MCQ",
    "Under the Rules of Procedure of Lok Sabha, if the Prime Minister is a member of the Rajya Sabha, who functions as the 'Leader of the House' in the Lok Sabha?",
    "மக்களவை விதிமுறைகளின் படி, பிரதமர் மாநிலங்களவை உறுப்பினராக இருந்தால், மக்களவையில் 'அவைத் தலைவராக' (Leader of the House) செயல்படுபவர் யார்?",
    q39_opts, "B",
    "Under the Rules of Lok Sabha, 'Leader of the House' means the Prime Minister if he is a member of the House, OR a Minister who is a member of the Lok Sabha and is nominated by the Prime Minister to function as Leader of the House (e.g., Pranab Mukherjee during Dr. Manmohan Singh's premiership).",
    "மக்களவை விதிகளின் படி, பிரதமர் மக்களவை உறுப்பினராக இல்லாவிட்டால், அவரால் பரிந்துரைக்கப்படும் மக்களவை உறுப்பினரான ஒரு மூத்த கேபினட் அமைச்சர் அவைத் தலைவராகச் செயல்படுவார் (எ.கா. மன்மோகன் சிங் காலத்தில் பிரணாப் முகர்ஜி).",
    "Incorrect. Speaker is the neutral presiding officer, not Leader of the House.",
    "தவறு. சபாநாயகர் நடுநிலையான அவைத் தலைவர், ஆளும் கட்சியின் அவைத் தலைவர் அல்ல.",
    "Correct. A senior Cabinet Minister who is an MP of Lok Sabha nominated by PM functions as Leader of the House.",
    "சரி. பிரதமரால் நியமிக்கப்படும் மக்களவை உறுப்பினரான ஒரு மூத்த கேபினட் அமைச்சர் அவைத் தலைவராகச் செயல்படுவார்.",
    "Incorrect. Leader of Opposition leads the minority opposition bench.",
    "தவறு. எதிர்க்கட்சித் தலைவர் எதிர்க்கட்சியை வழிநடத்துபவர்.",
    "Incorrect. Deputy Speaker presides in Speaker's absence.",
    "தவறு. துணை சபாநாயகர் சபாநாயகர் இல்லாதபோது தலைமை தாங்குபவர்.",
    "TNPSC Tip: Leader of Lok Sabha = PM (if LS member) OR nominated senior Cabinet Minister (if PM is RS member). Leader of RS = Senior Minister nominated by PM.",
    "தேர்வு உதவி: மக்களவை அவைத் தலைவர் = பிரதமர் (மக்களவை எம்பியாக இருந்தால்) அல்லது அவரால் நியமிக்கப்படும் மூத்த அமைச்சர்.",
    "The Leader of the House plays a crucial role in conducting government business in the chamber.",
    "அவைத் தலைவர் அவையில் அரசாங்கப் பணிகளை நடத்துவதில் முக்கியப் பங்காற்றுகிறார்.",
    "Confusing the presiding officer (Speaker) with the government floor leader (Leader of the House).",
    "அவையைத் தலைமை தாங்கி நடத்தும் சபாநாயகரையும் ஆளும் கட்சியின் அவைத் தலைவரையும் குழப்புதல்.",
    pattern_basis="Based on Parliamentary Rules on Leader of the House in TNPSC.",
    pyq_insight_en="TNPSC tests parliamentary rules regarding Leader of the House when PM is from Rajya Sabha.",
    pyq_insight_ta="பிரதமர் மாநிலங்களவை உறுப்பினராக இருக்கும் போது மக்களவை அவைத் தலைவர் யார் என்ற வினாக்கள்.",
    sources=["Prime Minister Notes Part 2 - Section 4"]
))

# Q40: PYQ_PATTERN - Direct / Article 74(2) Judicial Immunity
q40_opts = [
    make_opt("A", "High Courts can review Cabinet advice, but not Supreme Court", "உயர் நீதிமன்றங்கள் பரிசீலிக்கலாம், உச்ச நீதிமன்றம் முடியாது"),
    make_opt("B", "Supreme Court can review Cabinet advice during National Emergency", "தேசிய நெருக்கடி நிலையில் உச்ச நீதிமன்றம் பரிசீலிக்கலாம்"),
    make_opt("C", "Any district court can inquire into Cabinet advice", "எந்தவொரு மாவட்ட நீதிமன்றமும் விசாரிக்கலாம்"),
    make_opt("D", "No court has jurisdiction to inquire into what advice was tendered by Ministers to the President", "அமைச்சர்கள் குடியரசுத் தலைவருக்கு வழங்கிய ஆலோசனை என்னவென்று எந்தவொரு நீதிமன்றமும் விசாரிக்க அதிகாரம் இல்லை")
]
questions.append(build_pyq_item(
    40, "Medium", "Direct MCQ",
    "What constitutional protection is provided to the advice tendered by Ministers to the President under Article 74(2) of the Indian Constitution?",
    "இந்திய அரசியலமைப்பின் உறுப்பு 74(2)-ன் கீழ் அமைச்சர்கள் குடியரசுத் தலைவருக்கு வழங்கும் ஆலோசனைக்கு அளிக்கப்பட்டுள்ள அரசியலமைப்புப் பாதுகாப்பு என்ன?",
    q40_opts, "D",
    "Article 74(2) explicitly provides judicial immunity to Cabinet advice: 'The question whether any, and if so what, advice was tendered by Ministers to the President shall not be inquired into in any court.' (Note: Material on which advice is based can be reviewed, e.g. S.R. Bommai case).",
    "உறுப்பு 74(2) தெளிவுபடுத்துவது: 'அமைச்சர்கள் குடியரசுத் தலைவருக்கு ஆலோசனை வழங்கினார்களா, வழங்கினால் என்ன ஆலோசனை வழங்கினார்கள் என்ற வினாவை எந்தவொரு நீதிமன்றமும் விசாரிக்கக் கூடாது.'",
    "Incorrect. Article 74(2) debars all courts including High Courts.",
    "தவறு. விதி 74(2) அனைத்து நீதிமன்றங்களுக்கும் தடை விதிக்கிறது.",
    "Incorrect. Article 74(2) immunity applies equally during normal times and emergencies.",
    "தவறு. நெருக்கடி நிலையிலும் விதி 74(2) பாதுகாப்பு பொருந்தும்.",
    "Incorrect. District courts have zero jurisdiction.",
    "தவறு. கீழ் நீதிமன்றங்களுக்கு இதில் அதிகாரம் இல்லை.",
    "Correct. Article 74(2) bars all courts from inquiring into advice tendered by ministers to the President.",
    "சரி. உறுப்பு 74(2) எந்தவொரு நீதிமன்றமும் அமைச்சர்களின் ஆலோசனையை விசாரிப்பதைத் தடை செய்கிறது.",
    "TNPSC Tip: Art 74(2) protects ADVICE from judicial scrutiny. However, in S.R. Bommai (1994), SC held that the MATERIAL on which advice is based IS subject to judicial review.",
    "தேர்வு உதவி: விதி 74(2) ஆலோசனையை நீதிமன்ற விசாரணையிலிருந்து பாதுகாக்கிறது. ஆனால் பொம்மை வழக்கில் ஆலோசனையின் அடிப்படைச் சான்றுகளை நீதிமன்றம் ஆய்வு செய்யலாம் எனத் தீர்ப்பளிக்கப்பட்டது.",
    "Article 74(2) maintains executive confidentiality between Cabinet and President.",
    "விதி 74(2) அமைச்சரவை மற்றும் குடியரசுத் தலைவர் இடையிலான நிர்வாக இரகசியத் தன்மையைப் பாதுகாக்கிறது.",
    "Confusing the bar on inquiring into 'advice' (Art 74(2)) with the judicial review of the underlying 'material'.",
    "ஆலோசனையை விசாரிக்கக் கூடாது என்ற விதியையும் (74(2)) அதன் அடிப்படை சான்றுகளை நீதிமன்றம் ஆய்வு செய்வதையும் குழப்புதல்.",
    pattern_basis="Based on Article 74(2) judicial bar provisions in Group 1.",
    pyq_insight_en="TNPSC tests the constitutional scope of Article 74(2) judicial exclusion.",
    pyq_insight_ta="விதி 74(2)-ன் கீழ் நீதிமன்ற வரம்புத் தடை பற்றிய அரசியலமைப்பு வினாக்கள்.",
    sources=["Prime Minister Notes Part 1 - Section 1"]
))

# Q41: PYQ_PATTERN - Statement / Foreign Policy & Defense Role
q41_opts = [
    make_opt("A", "1 only", "1 மட்டும்"),
    make_opt("B", "2 only", "2 மட்டும்"),
    make_opt("C", "Both 1 and 2", "1 மற்றும் 2 இரண்டும்"),
    make_opt("D", "Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை")
]
questions.append(build_pyq_item(
    41, "Medium", "Statement-Based",
    "Consider the following statements regarding the Prime Minister's role in foreign policy and national defense:\n1. The Prime Minister is the chief spokesman of the nation on foreign policy affairs.\n2. The Prime Minister is the political head of the Armed Forces and heads the Cabinet Committee on Security (CCS).\nWhich of the statements given above is/are correct?",
    "வெளியுறவுக் கொள்கை மற்றும் தேசிய பாதுகாப்பில் பிரதமரின் பங்கு பற்றிய கூற்றுகளைக் கருத்தில் கொள்க:\n1. வெளியுறவுக் கொள்கை விஷயங்களில் பிரதமர் நாட்டின் முதன்மை செய்தித் தொடர்பாளராக உள்ளார்.\n2. பிரதமர் ஆயுதப் படைகளின் அரசியல் தலைவராகவும், பாதுகாப்புக்கான கேபினட் குழுவின் (CCS) தலைவராகவும் உள்ளார்.\nஎது/எவை சரியானவை?",
    q41_opts, "C",
    "Both statements are correct. The PM represents the nation at international summits (G20, BRICS, UN) as chief foreign policy spokesman. The PM is political head of armed forces (while President is Supreme Commander) and chairs Cabinet Committee on Security (CCS).",
    "இரண்டு கூற்றுகளும் சரியானவை. சர்வதேச மாநாடுகளில் பிரதமர் நாட்டின் முதன்மைப் பேச்சாளராகச் செயல்படுகிறார். குடியரசுத் தலைவர் முப்படைகளின் தலைமைத் தளபதி என்றாலும், பிரதமர் அரசியல் தலைவராகவும் CCS தலைவராகவும் உள்ளார்.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Correct. Both 1 and 2 accurately state PM's role in foreign policy and defense.",
    "சரி. கூற்றுகள் 1 மற்றும் 2 இரண்டும் சரியானவை.",
    "Incorrect. Both statements are correct.",
    "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
    "TNPSC Tip: Supreme Commander of Armed Forces = President (Art 53(2)); Political Head of Armed Forces & Chairman of CCS = Prime Minister.",
    "தேர்வு உதவி: முப்படைகளின் தலைமைத் தளபதி = குடியரசுத் தலைவர் (விதி 53(2)); முப்படைகளின் அரசியல் தலைவர் & CCS தலைவர் = பிரதமர்.",
    "The Cabinet Committee on Security (CCS) chaired by PM makes all apex defense purchases and national security decisions.",
    "பிரதமர் தலைமை தாங்கும் பாதுகாப்புக்கான கேபினட் குழு (CCS) அனைத்து தேசிய பாதுகாப்பு முடிவுகளையும் எடுக்கிறது.",
    "Confusing Supreme Commander of Armed Forces (President) with Political Head of Armed Forces (PM).",
    "முப்படைகளின் தலைமைத் தளபதியையும் (குடியரசுத் தலைவர்) அரசியல் தலைவரையும் (பிரதமர்) குழப்பிக் கொள்ளுதல்.",
    pattern_basis="Based on PM foreign policy & defense leadership in Group 1.",
    pyq_insight_en="Statement-based question testing PM's leadership in international representation and national security.",
    pyq_insight_ta="வெளியுறவு மற்றும் தேசிய பாதுகாப்பில் பிரதமரின் தலைமையை மதிப்பிடும் கூற்று வினாக்கள்.",
    sources=["Prime Minister Notes Part 2 - Section 6"]
))

# Q42: PYQ_PATTERN - Statement / PMO Evolution
q42_opts = [
    make_opt("A", "1 only", "1 மட்டும்"),
    make_opt("B", "2 only", "2 மட்டும்"),
    make_opt("C", "Both 1 and 2", "1 மற்றும் 2 இரண்டும்"),
    make_opt("D", "Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை")
]
questions.append(build_pyq_item(
    42, "Hard", "Statement-Based",
    "Consider the following statements regarding the Prime Minister's Office (PMO):\n1. The PMO is an extra-constitutional administrative body that provides secretarial assistance to the Prime Minister.\n2. It came into existence in 1947 as the 'Prime Minister's Secretariat' and was renamed 'Prime Minister's Office' (PMO) in 1977 during the Morarji Desai ministry.\nWhich of the statements given above is/are correct?",
    "பிரதமர் அலுவலகம் (PMO) பற்றிய பின்வரும் கூற்றுகளைக் கருத்தில் கொள்க:\n1. PMO என்பது பிரதமருக்குச் செயலக உதவிகளை வழங்கும் ஒரு அரசியலமைப்பில் இல்லாத நிர்வாக அமைப்பாகும்.\n2. இது 1947-ல் 'பிரதமரின் செயலகம்' என உருவாக்கப்பட்டு, 1977-ல் மொரார்ஜி தேசாய் ஆட்சிக் காலத்தில் 'பிரதமர் அலுவலகம்' (PMO) என மறுபெயரிடப்பட்டது.\nஎது/எவை சரியானவை?",
    q42_opts, "C",
    "Both statements are correct. PMO is an extra-constitutional staff agency headed politically by the PM and administratively by Principal Secretary to PM. Created in 1947 as PM's Secretariat, it was renamed PMO in 1977.",
    "இரண்டு கூற்றுகளும் சரியானவை. PMO என்பது அரசியலமைப்பில் இல்லாத ஒரு நிர்வாக அமைப்பாகும். 1947-ல் பிரதமரின் செயலகம் எனத் தொடங்கி 1977-ல் PMO என பெயர் மாற்றப்பட்டது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Correct. Both Statements 1 and 2 are historically and constitutionally accurate regarding PMO.",
    "சரி. கூற்றுகள் 1 மற்றும் 2 இரண்டும் சரியானவை.",
    "Incorrect. Both statements are true.",
    "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
    "TNPSC Tip: PMO Evolution: 1947 = Prime Minister's Secretariat; 1977 = Prime Minister's Office (PMO) under Morarji Desai government. Administrative Head = Principal Secretary to PM.",
    "தேர்வு உதவி: PMO வரலாறு: 1947 = பிரதமரின் செயலகம்; 1977 = பிரதமர் அலுவலகம் (PMO - மொரார்ஜி தேசாய் காலம்). நிர்வாகத் தலைவர் = பிரதமரின் முதன்மைச் செயலாளர்.",
    "PMO holds status of a Department of Government of India under Allocation of Business Rules 1961.",
    "1961 வணிகப் பகிர்வு விதிகளின் கீழ் PMO இந்திய அரசின் ஒரு துறையின் அந்தஸ்தைப் பெற்றுள்ளது.",
    "Thinking PMO is a Constitutional body created under Article 77 or Article 78.",
    "PMO என்பது விதி 77 அல்லது 78-ன் கீழ் அமைக்கப்பட்ட அரசியலமைப்பு அமைப்பு என தவறாக நினைப்பது.",
    pattern_basis="Based on PMO institutional evolution questions in Group 1.",
    pyq_insight_en="TNPSC tests the historical renaming (1977) and non-constitutional status of PMO.",
    pyq_insight_ta="பிரதமர் அலுவலகத்தின் வரலாற்றுப் பெயர் மாற்றம் (1977) மற்றும் சட்ட அந்தஸ்து பற்றிய வினாக்கள்.",
    sources=["Prime Minister Notes Part 2 - Section 5"]
))

# Q43: PYQ_PATTERN - Statement / Article 78(c) Provision
q43_opts = [
    make_opt("A", "1 only", "1 மட்டும்"),
    make_opt("B", "2 only", "2 மட்டும்"),
    make_opt("C", "Both 1 and 2", "1 மற்றும் 2 இரண்டும்"),
    make_opt("D", "Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை")
]
questions.append(build_pyq_item(
    43, "Hard", "Statement-Based",
    "Consider the following statements regarding Article 78(c) of the Constitution:\n1. Article 78(c) empowers the President to require the Prime Minister to submit for consideration of the Council of Ministers any matter on which a decision has been taken by an individual minister but has not been considered by the Council.\n2. This provision enforces the principle of collective responsibility among ministers.\nWhich of the statements given above is/are correct?",
    "அரசியலமைப்பு உறுப்பு 78(c) பற்றிய பின்வரும் கூற்றுகளைக் கருத்தில் கொள்க:\n1. ஒரு தனிப்பட்ட அமைச்சரால் முடிவெடுக்கப்பட்டு, ஆனால் அமைச்சரவையால் பரிசீலிக்கப்படாத ஒரு விஷயத்தை, அமைச்சரவையின் பரிசீலனைக்கு வைக்குமாறு பிரதமரிடம் கோர குடியரசுத் தலைவருக்கு உறுப்பு 78(c) அதிகாரமளிக்கிறது.\n2. இந்த விதி அமைச்சர்களிடையே கூட்டுப் பொறுப்புக் கோட்பாட்டை நடைமுறைப்படுத்துகிறது.\nஎது/எவை சரியானவை?",
    q43_opts, "C",
    "Both statements are correct. Article 78(c) provides a constitutional mechanism for the President to ensure that an individual minister's unilateral decision is subjected to collective Cabinet scrutiny before being implemented.",
    "இரண்டு கூற்றுகளும் சரியானவை. விதி 78(c) ஒரு தனி அமைச்சரின் தன்னிச்சையான முடிவை அமைச்சரவையின் கூட்டுப் பரிசீலனைக்கு உட்படுத்துவதை உறுதி செய்கிறது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Correct. Both 1 and 2 are constitutionally accurate regarding Article 78(c).",
    "சரி. கூற்றுகள் 1 மற்றும் 2 இரண்டும் சரியானவை.",
    "Incorrect. Both statements are valid.",
    "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
    "TNPSC Tip: Art 78(a) = Communicate decisions; Art 78(b) = Furnish info requested by President; Art 78(c) = Submit individual minister decision for Cabinet review.",
    "தேர்வு உதவி: விதி 78(a) = முடிவுகளைத் தெரிவித்தல்; 78(b) = கோரப்பட்ட தகவல்களை அளித்தல்; 78(c) = தனி அமைச்சர் முடிவை அமைச்சரவை பரிசீலனைக்கு வைத்தல்.",
    "Article 78(c) reflects the President's constitutional role as a check ensuring Cabinet solidarity.",
    "விதி 78(c) அமைச்சரவையின் கூட்டு ஒருமைப்பாட்டை உறுதி செய்யும் குடியரசுத் தலைவரின் அதிகாரத்தைப் பிரதிபலிக்கிறது.",
    "Confusing Article 78(c) with presidential veto power over parliamentary bills under Article 111.",
    "விதி 78(c)-ஐ விதி 111-ல் உள்ள மசோதா நிராகரிப்பு அதிகாரத்துடன் குழப்பிக் கொள்ளுதல்.",
    pattern_basis="Based on Article 78 sub-clause (c) specific questions in Group 1.",
    pyq_insight_en="TNPSC tests the constitutional rationale of Article 78(c) in reinforcing collective responsibility.",
    pyq_insight_ta="கூட்டுப் பொறுப்பை வலுப்படுத்தும் விதி 78(c)-ன் அரசியலமைப்பு காரணம் பற்றிய வினாக்கள்.",
    sources=["Prime Minister Notes Part 2 - Section 1"]
))

# Q44: PYQ_PATTERN - Reasoning / No-Confidence Motion Admissibility
q44_opts = [
    make_opt("A", "Because Article 75(3) mandates that the Council of Ministers is collectively responsible ONLY to the Lok Sabha", "ஏனெனில் விதி 75(3) அமைச்சரவை மக்களவைக்கு மட்டுமே கூட்டாகப் பொறுப்பானது என ஆணை பிறப்பிக்கிறது"),
    make_opt("B", "Because Rajya Sabha is chaired by the Vice-President who cannot evaluate political motions", "ஏனெனில் மாநிலங்களவையின் தலைவர் துணைக் குடியரசுத் தலைவர் என்பதால் அவர் அரசியல் தீர்மானங்களை ஆய்வு செய்ய முடியாது"),
    make_opt("C", "Because Rajya Sabha members are not directly elected by the public", "ஏனெனில் மாநிலங்களவை உறுப்பினர்கள் மக்களால் நேரடியாகத் தேர்ந்தெடுக்கப்படவில்லை"),
    make_opt("D", "Because Rajya Sabha is dissolved every 6 years", "ஏனெனில் மாநிலங்களவை 6 ஆண்டுகளுக்கு ஒருமுறை கலைக்கப்படுகிறது")
]
questions.append(build_pyq_item(
    44, "Medium", "Reasoning",
    "Why is a No-Confidence Motion against the Union Council of Ministers admissible ONLY in the Lok Sabha and NOT in the Rajya Sabha?",
    "மத்திய அமைச்சரவைக்கு எதிரான நம்பிக்கையில்லாத் தீர்மானம் ஏன் மக்களவையில் மட்டுமே கொண்டுவரப்பட முடியும், மாநிலங்களவையில் கொண்டுவரப்பட முடியாது?",
    q44_opts, "A",
    "Under Article 75(3), the Council of Ministers is collectively responsible specifically to the House of the People (Lok Sabha). Since the government's survival depends on maintaining majority in Lok Sabha, a No-Confidence Motion (Rule 198) can be introduced only in Lok Sabha.",
    "விதி 75(3)-ன் படி அமைச்சரவை மக்களவைக்கு மட்டுமே கூட்டாகப் பொறுப்பானது. அரசாங்கத்தின் நீடிப்பு மக்களவையின் பெரும்பான்மையைச் சார்ந்திருப்பதால், நம்பிக்கையில்லா தீர்மானம் மக்களவையில் மட்டுமே கொண்டுவரப்பட முடியும்.",
    "Correct. Article 75(3) mandates collective responsibility specifically to the Lok Sabha.",
    "சரி. விதி 75(3) மக்களவைக்கு மட்டுமே கூட்டுப் பொறுப்பைக் குறிப்பிடுவதே இதற்குக் காரணமாகும்.",
    "Incorrect. Presiding officer identity is not the constitutional reason.",
    "தவறு. அவைத் தலைவரின் பதவி இதற்கான காரணமல்ல.",
    "Incorrect. Direct vs indirect election is a structural feature, but Art 75(3) text is the legal reason.",
    "தவறு. நேரடித் தேர்தல் முறை ஒரு அம்சம், ஆனால் விதி 75(3) சட்டப்பூர்வ காரணமாகும்.",
    "Incorrect. Rajya Sabha is a permanent body and never dissolved.",
    "தவறு. மாநிலங்களவை ஒருபோதும் கலைக்கப்பட முடியாத நிரந்தர அவையாகும்.",
    "TNPSC Tip: No-Confidence Motion = Lok Sabha ONLY (Rule 198); Censure Motion = Lok Sabha ONLY; Rajya Sabha cannot pass No-Confidence Motion.",
    "தேர்வு உதவி: நம்பிக்கையில்லா தீர்மானம் = மக்களவைக்கு மட்டும் (விதி 198); மாநிலங்களவையில் கொண்டுவர முடியாது.",
    "While Rajya Sabha can discuss policies and ask questions, it cannot remove the government through a No-Confidence Motion.",
    "மாநிலங்களவை விவாதங்கள் நடத்தலாமே தவிர நம்பிக்கையில்லா தீர்மானம் மூலம் அரசைக் கவிழ்க்க முடியாது.",
    "Selecting option D claiming Rajya Sabha dissolves every 6 years (Rajya Sabha is a permanent body!).",
    "மாநிலங்களவை 6 ஆண்டுகளுக்கு ஒருமுறை கலைக்கப்படுகிறது என்ற தவறான கூற்றைத் தேர்ந்தெடுப்பது.",
    pattern_basis="Based on Lok Sabha vs Rajya Sabha confidence motion jurisdiction in TNPSC.",
    pyq_insight_en="Reasoning question explaining the constitutional basis of Lok Sabha exclusivity over No-Confidence motions.",
    pyq_insight_ta="நம்பிக்கையில்லா தீர்மானம் மக்களவையில் மட்டுமே சாத்தியம் என்பதற்கான காரண வினாக்கள்.",
    sources=["Prime Minister Notes Part 3 - Section 1"]
))

# Q45: PYQ_PATTERN - Reasoning / Automatic Resignation on PM Resignation
q45_opts = [
    make_opt("A", "Because Article 75(1) states that all ministers are appointed for a fixed 5-year tenure", "ஏனெனில் விதி 75(1) அனைத்து அமைச்சர்களும் 5 ஆண்டு நிலையான பதவிக்காலம் கொண்டவர்கள் எனக் கூறுகிறது"),
    make_opt("B", "Because the Prime Minister is the head of the Council of Ministers and the central axis around which the entire ministry revolves", "ஏனெனில் பிரதமர் அமைச்சரவையின் தலைவராகவும் முழு அமைச்சரவையும் சுழலும் மைய அச்சாணியாகவும் உள்ளார்"),
    make_opt("C", "Because the Chief Justice of India automatically cancels ministerial appointments", "ஏனெனில் இந்திய தலைமை நீதிபதி அமைச்சர்களின் நியமனங்களைத் தானாகவே ரத்து செய்கிறார்"),
    make_opt("D", "Because the Rajya Sabha passes a resolution dissolving the Cabinet", "ஏனெனில் மாநிலங்களவை அமைச்சரவையைக் கலைக்கத் தீர்மானம் நிறைவேற்றுகிறது")
]
questions.append(build_pyq_item(
    45, "Medium", "Reasoning",
    "Why does the resignation of the Prime Minister automatically lead to the resignation of all other ministers in the Council of Ministers?",
    "பிரதமரின் ராஜினாமா ஏன் தானாகவே அமைச்சரவையில் உள்ள மற்ற அனைத்து அமைச்சர்களின் ராஜினாமாவுக்கு வழிவகுக்கிறது?",
    q45_opts, "B",
    "The Prime Minister is the key pillar of the Cabinet ('Primus inter pares' / 'Keystone of the Cabinet Arch'). Since other ministers are appointed on the PM's advice under Art 75(1), the collapse or resignation of the head automatically dissolves the entire executive council.",
    "பிரதமர் அமைச்சரவையின் முதன்மைத் தூணாவார். இதர அமைச்சர்கள் பிரதமரின் ஆலோசனையின் பேரில் நியமிக்கப்படுவதால் (விதி 75(1)), தலைவரின் ராஜினாமா முழு அமைச்சரவையையும் தானாகவே கலைத்துவிடும்.",
    "Incorrect. Ministers do not have a fixed 5-year tenure.",
    "தவறு. அமைச்சர்களுக்கு நிலையான 5 ஆண்டு பதவிக்காலம் இல்லை.",
    "Correct. The PM is the head and central axis of the ministry; his resignation dissolves the whole body.",
    "சரி. பிரதமர் அமைச்சரவையின் மைய அச்சாணியாக இருப்பதால் அவரது ராஜினாமா முழு அமைப்பையும் கலைத்துவிடும்.",
    "Incorrect. Judiciary plays no role in ministerial resignations.",
    "தவறு. நீதித்துறைக்கு இதில் தொடர்பில்லை.",
    "Incorrect. Rajya Sabha cannot dissolve the Cabinet.",
    "தவறு. மாநிலங்களவை அமைச்சரவையைக் கலைக்க முடியாது.",
    "TNPSC Tip: PM Resignation = Entire Cabinet Dissolves; Individual Minister Resignation = Simple vacancy filled by PM recommendation.",
    "தேர்வு உதவி: பிரதமர் ராஜினாமா = முழு அமைச்சரவையும் கலைந்துவிடும்; தனி அமைச்சர் ராஜினாமா = பிரதமர் நிரப்பும் வெறும் காலிப்பணியிடம்.",
    "Lord Morley described PM as the 'Keystone of the Cabinet Arch' because without the keystone, the arch collapses.",
    "மார்லி பிரபு குறிப்பிட்டது போல அச்சாணி கல் அகற்றப்பட்டால் வளைவு சரிவது போல பிரதமர் விலகினால் அமைச்சரவை சரியும்.",
    "Believing that individual ministers can remain in office independently after the PM resigns.",
    "பிரதமர் ராஜினாமா செய்த பிறகும் தனி அமைச்சர்கள் பதவியில் நீடிக்கலாம் என நினைப்பது.",
    pattern_basis="Based on PM centrality in Cabinet survival in Group 1.",
    pyq_insight_en="Reasoning question testing the principle of PM leadership in Cabinet dissolution dynamics.",
    pyq_insight_ta="அமைச்சரவை கலைப்பில் பிரதமரின் மையப் பங்கு பற்றிய காரண வினாக்கள்.",
    sources=["Prime Minister Notes Part 1 & Part 2"]
))

# Q46: PYQ_PATTERN - Direct / Article 75(6) Salaries
q46_opts = [
    make_opt("A", "The President of India by executive decree", "நிர்வாக ஆணை மூலம் இந்தியக் குடியரசுத் தலைவர்"),
    make_opt("B", "The Finance Commission of India", "இந்திய நிதி ஆணையம்"),
    make_opt("C", "Parliament by law", "சட்டம் மூலம் நாடாளுமன்றம்"),
    make_opt("D", "The Supreme Court of India", "இந்திய உச்ச நீதிமன்றம்")
]
questions.append(build_pyq_item(
    46, "Easy", "Direct MCQ",
    "Under Article 75(6) of the Constitution of India, who determines the salaries and allowances of the Prime Minister and other Ministers?",
    "இந்திய அரசியலமைப்பின் உறுப்பு 75(6)-ன் கீழ், பிரதமர் மற்றும் இதர அமைச்சர்களின் ஊதியங்கள் மற்றும் படிகளைத் தீர்மானிப்பது யார்?",
    q46_opts, "C",
    "Article 75(6) states: 'The salaries and allowances of Ministers shall be such as Parliament may from time to time by law determine.' Until Parliament determines them, they are as specified in the Second Schedule.",
    "அரசியலமைப்பு உறுப்பு 75(6) தெளிவுபடுத்துவது: 'அமைச்சர்களின் ஊதியங்கள் மற்றும் படிகள் நாடாளுமன்றம் அவ்வப்போது சட்டத்தின் மூலம் தீர்மானிப்பவாறு இருக்கும்.'",
    "Incorrect. President does not fix salaries by decree.",
    "தவறு. குடியரசுத் தலைவர் ஆணையால் ஊதியத்தை நிர்ணயிக்க முடியாது.",
    "Incorrect. Finance Commission recommends tax devolution, not salaries.",
    "தவறு. நிதி ஆணையம் வரிப் பங்கீட்டைப் பரிந்துரைக்கும் அமைப்பு.",
    "Correct. Article 75(6) empowers Parliament to determine salaries and allowances by law.",
    "சரி. உறுப்பு 75(6)-ன் படி நாடாளுமன்றம் சட்டத்தின் மூலம் ஊதியங்களை நிர்ணயிக்கிறது.",
    "Incorrect. Judiciary has no salary-fixing executive powers.",
    "தவறு. நீதித்துறைக்கு இதில் அதிகாரமில்லை.",
    "TNPSC Tip: PM/Minister Salaries = Parliament by law (Art 75(6)); President Salary = Parliament by law; Supreme Court Judge Salary = Parliament by law.",
    "தேர்வு உதவி: பிரதமர்/அமைச்சர்கள் ஊதியம் = நாடாளுமன்றம் சட்டத்தின் மூலம் நிர்ணயிக்கிறது (விதி 75(6)).",
    "Ministerial salaries are charged or voted as determined by parliamentary legislation.",
    "அமைச்சர்களின் ஊதியங்கள் நாடாளுமன்றச் சட்டங்கள் மூலம் தீர்மானிக்கப்படுகின்றன.",
    "Selecting President of India assuming executive heads fix their own pay.",
    "குடியரசுத் தலைவரே ஊதியத்தை நிர்ணயிக்கிறார் எனத் தவறாகக் கருதுவது.",
    pattern_basis="Based on Article 75(6) salary determination questions in TNPSC.",
    pyq_insight_en="TNPSC tests the authority responsible for fixing constitutional executive salaries under Art 75(6).",
    pyq_insight_ta="விதி 75(6)-ன் கீழ் ஊதியம் நிர்ணயிக்கும் அதிகாரம் யாருக்கு உள்ளது என்ற வினாக்கள்.",
    sources=["Prime Minister Notes Part 1 - Section 5"]
))

# Q47: PYQ_PATTERN - Statement / PM vs CM Comparison
q47_opts = [
    make_opt("A", "1 only", "1 மட்டும்"),
    make_opt("B", "2 only", "2 மட்டும்"),
    make_opt("C", "Both 1 and 2", "1 மற்றும் 2 இரண்டும்"),
    make_opt("D", "Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை")
]
questions.append(build_pyq_item(
    47, "Medium", "Statement-Based",
    "Consider the following comparison statements between Prime Minister and Chief Minister:\n1. The Prime Minister is the real head of executive at the Union level, while the Chief Minister is the real head of executive at the State level.\n2. The Prime Minister is appointed by the President under Article 75(1), while the Chief Minister is appointed by the Governor under Article 164(1).\nWhich of the statements given above is/are correct?",
    "பிரதமர் மற்றும் முதலமைச்சர் ஒப்பீடு பற்றிய பின்வரும் கூற்றுகளைக் கருத்தில் கொள்க:\n1. பிரதமர் மத்திய அளவில் உண்மையான நிர்வாகத் தலைவராவார், முதலமைச்சர் மாநில அளவில் உண்மையான நிர்வாகத் தலைவராவார்.\n2. பிரதமர் விதி 75(1)-ன் கீழ் குடியரசுத் தலைவரால் நியமிக்கப்படுகிறார், முதலமைச்சர் விதி 164(1)-ன் கீழ் ஆளுநரால் நியமிக்கப்படுகிறார்.\nஎது/எவை சரியானவை?",
    q47_opts, "C",
    "Both statements are correct. The constitutional relationship between President-PM at the Union (Art 74, 75, 78) is mirrored by the Governor-CM relationship at the State level (Art 163, 164, 167).",
    "இரண்டு கூற்றுகளும் சரியானவை. மத்தியில் குடியரசுத் தலைவர்-பிரதமர் உறவு (விதிகள் 74, 75, 78) போல மாநிலத்தில் ஆளுநர்-முதலமைச்சர் உறவு (விதிகள் 163, 164, 167) அமைந்துள்ளது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Correct. Both 1 and 2 are constitutionally accurate parallel comparisons.",
    "சரி. கூற்றுகள் 1 மற்றும் 2 இரண்டும் சரியானவை.",
    "Incorrect. Both statements are correct.",
    "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
    "TNPSC Tip: Parallel Executive Articles: Union PM Appointment = Art 75(1); State CM Appointment = Art 164(1). Union PM Duties = Art 78; State CM Duties = Art 167.",
    "தேர்வு உதவி: இணையான விதிகளின் ஒப்பீடு: பிரதமர் நியமனம் = விதி 75(1); முதலமைச்சர் நியமனம் = விதி 164(1). பிரதமர் கடமைகள் = விதி 78; முதலமைச்சர் கடமைகள் = விதி 167.",
    "The parliamentary model operates identically at the Centre and in the States.",
    "நாடாளுமன்ற அரசாங்க முறை மத்தியிலும் மாநிலத்திலும் ஒரே மாதிரியாக இயங்குகிறது.",
    "Confusing Article 75 (Union PM) with Article 164 (State CM).",
    "விதி 75 (மத்திய பிரதமர்) மற்றும் விதி 164 (மாநில முதலமைச்சர்)-ஐக் குழப்புதல்.",
    pattern_basis="Based on Union vs State executive comparison in TNPSC.",
    pyq_insight_en="Comparative statement question evaluating PM vs CM constitutional alignment.",
    pyq_insight_ta="பிரதமர் மற்றும் முதலமைச்சர் அரசியலமைப்பு ஒப்பீட்டு வினாக்கள்.",
    sources=["Prime Minister Notes Part 1 - Section 7"]
))

# Q48: PYQ_PATTERN - Direct / S.P. Anand v. H.D. Deve Gowda (1997) Supreme Court Ruling
q48_opts = [
    make_opt("A", "S.P. Anand v. H.D. Deve Gowda (1997)", "எஸ்.பி. ஆனந்த் எதிர் எச்.டி. தேவ கவுடா (1997)"),
    make_opt("B", "Keshvananda Bharati v. State of Kerala (1973)", "கேசவாநந்த பாரதி எதிர் கேரள மாநிலம் (1973)"),
    make_opt("C", "Minerva Mills v. Union of India (1980)", "மினர்வா மில்ஸ் எதிர் இந்திய ஒன்றியம் (1980)"),
    make_opt("D", "S.R. Bommai v. Union of India (1994)", "எஸ்.ஆர். பொம்மை எதிர் இந்திய ஒன்றியம் (1994)")
]
questions.append(build_pyq_item(
    48, "Hard", "Direct MCQ",
    "In which landmark case did the Supreme Court of India uphold that a person who is NOT a member of either House of Parliament can be appointed Prime Minister for 6 months under Article 75(5)?",
    "நாடாளுமன்றத்தின் இரு அவைகளிலும் உறுப்பினராக இல்லாத ஒரு நபரை விதி 75(5)-ன் கீழ் 6 மாத காலத்திற்கு பிரதமராக நியமிக்கலாம் என்பதை உச்ச நீதிமன்றம் உறுதி செய்த வரலாற்று சிறப்புமிக்க வழக்கு எது?",
    q48_opts, "A",
    "In S.P. Anand v. H.D. Deve Gowda (1997), the Supreme Court held that just as a non-MP can be appointed a minister for 6 months, a non-MP can also be appointed Prime Minister for 6 months, during which he must secure a seat in either Lok Sabha or Rajya Sabha.",
    "1997-ம் ஆண்டின் எஸ்.பி. ஆனந்த் எதிர் எச்.டி. தேவ கவுடா வழக்கில், எம்பி அல்லாத ஒருவர் 6 மாதங்களுக்கு அமைச்சராக நியமிக்கப்படலாம் என்பது போல பிரதமராகவும் நியமிக்கப்படலாம் என உச்ச நீதிமன்றம் உறுதி செய்தது.",
    "Correct. S.P. Anand v. H.D. Deve Gowda (1997) affirmed that a non-MP can be appointed PM for 6 months.",
    "சரி. எஸ்.பி. ஆனந்த் எதிர் தேவ கவுடா (1997) வழக்கு எம்பி அல்லாதவரும் பிரதமராகலாம் என்பதை உறுதி செய்தது.",
    "Incorrect. Kesavananda Bharati deals with Basic Structure doctrine.",
    "தவறு. கேசவாநந்த பாரதி வழக்கு அடிப்படை அமைப்புக் கோட்பாடு தொடர்பானது.",
    "Incorrect. Minerva Mills deals with fundamental rights & DPSP balance.",
    "தவறு. மினர்வா மில்ஸ் வழக்கு அடிப்படை உரிமைகள் தொடர்பானது.",
    "Incorrect. S.R. Bommai deals with Article 356 and floor test requirement.",
    "தவறு. பொம்மை வழக்கு விதி 356 மற்றும் தள வாக்கெடுப்பு தொடர்பானது.",
    "TNPSC Tip: S.P. Anand v. H.D. Deve Gowda (1997) = Non-MP can be appointed PM for 6 months under Art 75(5). U.N.R. Rao v. Indira Gandhi (1971) = COM must exist even after Lok Sabha dissolution.",
    "தேர்வு உதவி: எஸ்.பி. ஆனந்த் வழக்கு (1997) = எம்பி அல்லாதவரும் 6 மாதங்களுக்குப் பிரதமராகலாம். யு.என்.ஆர். ராவ் வழக்கு (1971) = மக்களவை கலைக்கப்பட்ட பிறகும் அமைச்சரவை தொடர வேண்டும்.",
    "This judicial interpretation confirmed flexibility in parliamentary executive recruitment.",
    "இந்தத் தீர்ப்பு நாடாளுமன்ற நிர்வாக அமைப்பில் உறுப்பினரல்லாதவரும் சேர்வதற்கான நெகிழ்வுத்தன்மையை உறுதி செய்தது.",
    "Confusing S.P. Anand case (Non-MP PM appointment) with S.R. Bommai case (Floor test).",
    "எஸ்.பி. ஆனந்த் வழக்கை (எம்பி அல்லாதவர் பிரதமர் நியமனம்) எஸ்.ஆர். பொம்மை வழக்குடன் (தள வாக்கெடுப்பு) குழப்புதல்.",
    pattern_basis="Based on landmark Supreme Court cases on executive appointment in Group 1.",
    pyq_insight_en="TNPSC tests landmark case laws affirming executive appointment flexibility under Article 75(5).",
    pyq_insight_ta="விதி 75(5)-ன் கீழ் பிரதமர் நியமனம் குறித்த உச்ச நீதிமன்ற முக்கிய வழக்குத் தீர்ப்புகள்.",
    sources=["Prime Minister Notes Part 1 & Part 3"]
))

# Q49: PYQ_PATTERN - Direct / Super Cabinet (Political Affairs Committee)
q49_opts = [
    make_opt("A", "Cabinet Committee on Economic Affairs", "பொருளாதார விவகாரங்களுக்கான கேபினட் குழு"),
    make_opt("B", "Political Affairs Committee", "அரசியல் விவகாரங்களுக்கான கேபினட் குழு"),
    make_opt("C", "Appointments Committee of the Cabinet", "கேபினட் நியமனங்கள் குழு"),
    make_opt("D", "Cabinet Committee on Parliamentary Affairs", "நாடாளுமன்ற விவகாரங்களுக்கான கேபினட் குழு")
]
questions.append(build_pyq_item(
    49, "Medium", "Direct MCQ",
    "Which Cabinet Committee, chaired by the Prime Minister, deals with all domestic and foreign political issues and is often described as the 'Super-Cabinet'?",
    "பிரதமர் தலைமை தாங்கும் எந்தக் கேபினட் குழு அனைத்து உள்நாட்டு மற்றும் வெளிநாட்டு அரசியல் பிரச்சினைகளையும் கையாள்கிறது மற்றும் 'சூப்பர் கேபினட்' என விவரிக்கப்படுகிறது?",
    q49_opts, "B",
    "The Political Affairs Committee, chaired by the Prime Minister, is the most powerful cabinet committee handling all domestic and foreign policy issues. Because of its dominant policy influence, political scientists describe it as the 'Super-Cabinet'.",
    "பிரதமர் தலைமை தாங்கும் அரசியல் விவகாரங்களுக்கான கேபினட் குழு அனைத்து உள்நாட்டு மற்றும் வெளியுறவுக் கொள்கைகளையும் கையாளும் மிகவும் சக்திவாய்ந்த குழுவாகும். இது 'சூப்பர் கேபினட்' என்று அழைக்கப்படுகிறது.",
    "Incorrect. Economic Affairs Committee deals with financial and market policies.",
    "தவறு. பொருளாதார விவகாரக் குழு நிதி மற்றும் சந்தைக் கொள்கைகளைக் கவனிப்பது.",
    "Correct. Political Affairs Committee is chaired by PM and called 'Super-Cabinet'.",
    "சரி. அரசியல் விவகாரக் குழுவே 'சூப்பர் கேபினட்' என்று அழைக்கப்படுகிறது.",
    "Incorrect. Appointments Committee handles high-level administrative postings.",
    "தவறு. நியமனங்கள் குழு உயர் மட்ட அதிகாரி நியமனங்களைக் கவனிப்பது.",
    "Incorrect. Parliamentary Affairs Committee handles legislative business and is NOT chaired by PM.",
    "தவறு. நாடாளுமன்ற விவகாரக் குழு அவைப் பணிகளைக் கவனிப்பது.",
    "TNPSC Tip: Political Affairs Committee = 'Super-Cabinet' (Chaired by PM). Handles all policy and political crises.",
    "தேர்வு உதவி: அரசியல் விவகாரக் குழு = 'சூப்பர் கேபினட்' (பிரதமர் தலைவராவார்). அனைத்து அரசியல் கொள்கைகளையும் கையாளுவது.",
    "The Political Affairs Committee is the apex policy-coordinating body within the Union Cabinet.",
    "அரசியல் விவகாரக் குழு மத்திய கேபினட்டின் உச்ச கொள்கை ஒருங்கிணைப்பு அமைப்பாகும்.",
    "Calling the Appointments Committee or Economic Committee as 'Super-Cabinet'.",
    "நியமனக் குழு அல்லது பொருளாதாரக் குழுவை 'சூப்பர் கேபினட்' எனக் தவறாகக் நினைப்பது.",
    pattern_basis="Based on Cabinet Committees nomenclature questions in TNPSC.",
    pyq_insight_en="TNPSC tests the specific political science title ('Super-Cabinet') given to the Political Affairs Committee.",
    pyq_insight_ta="அரசியல் விவகாரக் குழுவுக்கு வழங்கப்படும் 'சூப்பர் கேபினட்' என்ற சிறப்புப் பெயர் பற்றிய வினாக்கள்.",
    sources=["Prime Minister Notes Part 3 - Section 6"]
))

# Q50: PYQ_PATTERN - Statement / Grand Synthesis on PM Constitutional Mandate
q50_opts = [
    make_opt("A", "1 and 2 only", "1 மற்றும் 2 மட்டும்"),
    make_opt("B", "2 and 3 only", "2 மற்றும் 3 மட்டும்"),
    make_opt("C", "1 and 3 only", "1 மற்றும் 3 மட்டும்"),
    make_opt("D", "1, 2 and 3", "1, 2 மற்றும் 3")
]
questions.append(build_pyq_item(
    50, "Hard", "Statement-Based",
    "Consider the following comprehensive statements regarding the constitutional position of the Prime Minister:\n1. The Prime Minister acts as the chief channel of communication between the President and the Council of Ministers under Article 78.\n2. The Constitution does not specify any fixed term for the Prime Minister, who holds office during the pleasure of the President as long as he enjoys Lok Sabha majority.\n3. The Prime Minister advises the President on the appointment or dismissal of any minister in the Union Council of Ministers.\nWhich of the statements given above are correct?",
    "பிரதமரின் அரசியலமைப்பு நிலை பற்றிய பின்வரும் விரிவான கூற்றுகளைக் கருத்தில் கொள்க:\n1. உறுப்பு 78-ன் கீழ் குடியரசுத் தலைவருக்கும் அமைச்சரவைக்கும் இடையிலான முதன்மைத் தொடர்பு வாயிலாகப் பிரதமர் செயல்படுகிறார்.\n2. அரசியலமைப்பு பிரதமருக்கு எந்தவொரு நிலையான பதவிக்காலத்தையும் குறிப்பிடவில்லை; மக்களவை பெரும்பான்மை இருக்கும் வரை அவர் குடியரசுத் தலைவரின் விருப்பத்தின் பேரில் பதவியில் நீடிக்கிறார்.\n3. மத்திய அமைச்சரவையில் உள்ள எந்தவொரு அமைச்சரின் நியமனம் அல்லது நீக்கம் குறித்து குடியரசுத் தலைவருக்குப் பிரதமர் ஆலோசனை வழங்குகிறார்.\nஎது/எவை சரியானவை?",
    q50_opts, "D",
    "All three statements are constitutionally flawless: (1) Art 78 creates PM communication duty, (2) No fixed term in Constitution; holds office during pleasure of President contingent on Lok Sabha majority, (3) PM holds portfolio recommendation and ministerial appointment/dismissal advice power under Art 75(1)/75(2).",
    "மூன்று கூற்றுகளும் அரசியலமைப்பு ரீதியாகச் சரியானவை: (1) விதி 78 தகவல் தொடர்பு வழியை உருவாக்குகிறது, (2) நிலையான பதவிக்காலம் இல்லை, பெரும்பான்மை உள்ளவரை பதவியில் நீடிப்பார், (3) அமைச்சர்களின் நியமனம்/நீக்க ஆலோசனையை பிரதமர் வழங்குகிறார்.",
    "Incorrect. Statement 3 is also correct.",
    "தவறு. கூற்று 3-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Correct. Statements 1, 2, and 3 are all true and constitutionally sound.",
    "சரி. கூற்றுகள் 1, 2 மற்றும் 3 ஆகிய அனைத்தும் சரியானவை.",
    "TNPSC Tip: Prime Minister Tenure: NOT fixed by Constitution (Art 75(2) pleasure doctrine); practically co-terminus with Lok Sabha majority.",
    "தேர்வு உதவி: பிரதமர் பதவிக்காலம்: அரசியலமைப்பில் நிலையானது அல்ல (விதி 75(2) விருப்பக் கோட்பாடு); நடைமுறையில் மக்களவை பெரும்பான்மையைப் பொறுத்தது.",
    "The Prime Minister is the linchpin of the Indian constitutional governance system.",
    "பிரதமர் இந்திய அரசியலமைப்பு நிர்வாக அமைப்பின் முதன்மை அச்சாணியாவார்.",
    "Believing the Constitution fixes a rigid 5-year tenure for the Prime Minister independently of Lok Sabha majority.",
    "அரசியலமைப்பு பிரதமருக்கு மக்களவை பெரும்பான்மையின்றி தனியாக 5 ஆண்டுகள் நிலையான பதவிக்காலம் அளித்துள்ளதாக நினைப்பது.",
    pattern_basis="Based on Grand synthesis evaluation of PM constitutional role in TNPSC Group 1.",
    pyq_insight_en="Grand synthesis question evaluating the full spectrum of PM's constitutional position, tenure, and duties.",
    pyq_insight_ta="பிரதமரின் அரசியலமைப்பு நிலை, பதவிக்காலம் மற்றும் கடமைகள் பற்றிய முழுமையான மதிப்பீட்டு வினாக்கள்.",
    sources=["Prime Minister Notes Part 1, 2 & 3"]
))

# ==============================================================================
# VALIDATION & FILE SAVE
# ==============================================================================

assert len(questions) == 50, f"Expected 50 questions, got {len(questions)}"

# Check unique IDs
id_set = set()
actual_count = 0
pattern_count = 0

for idx, q in enumerate(questions, 1):
    qid = q["id"]
    expected_id = f"POLITY_PM_PYQ_{idx:03d}"
    assert qid == expected_id, f"Q{idx} ID mismatch: {qid} vs {expected_id}"
    assert qid not in id_set, f"Duplicate ID found: {qid}"
    id_set.add(qid)

    # Check options
    assert len(q["options"]) == 4, f"{qid}: Expected 4 options"
    opt_ids = [o["id"] for o in q["options"]]
    assert opt_ids == ["A", "B", "C", "D"], f"{qid}: Invalid option IDs {opt_ids}"

    # Check correct answer
    assert q["correct_answer"] in ["A", "B", "C", "D"], f"{qid}: Invalid correct_answer {q['correct_answer']}"

    # Check bilingual texts
    assert q["question_en"] and len(q["question_en"].strip()) > 0, f"{qid}: missing question_en"
    assert q["question_ta"] and len(q["question_ta"].strip()) > 0, f"{qid}: missing question_ta"

    assert q["explanation_en"] and len(q["explanation_en"].strip()) > 0, f"{qid}: missing explanation_en"
    assert q["explanation_ta"] and len(q["explanation_ta"].strip()) > 0, f"{qid}: missing explanation_ta"

    # Check distractor analysis for all 4 options
    da = q["distractor_analysis"]
    wno = q["why_not_others"]
    assert isinstance(da, dict) and len(da) == 4, f"{qid}: missing distractor_analysis for 4 options"
    assert isinstance(wno, dict) and len(wno) == 4, f"{qid}: missing why_not_others for 4 options"
    for letter in ["A", "B", "C", "D"]:
        assert letter in da and letter in wno, f"{qid}: Option {letter} missing in analysis"
        assert da[letter]["explanation_english"] and da[letter]["explanation_tamil"], f"{qid}: Option {letter} missing text"

    # Check tip, high-yield fact, trap point
    assert q["tnpsc_expert_tip"]["en"] and q["tnpsc_expert_tip"]["ta"], f"{qid}: missing tip"
    assert q["high_yield_revision_fact"]["en"] and q["high_yield_revision_fact"]["ta"], f"{qid}: missing high-yield fact"
    assert q["trap_point"]["en"] and q["trap_point"]["ta"], f"{qid}: missing trap point"

    # Check metadata by source type
    if q["source_type"] == "ACTUAL_PYQ":
        actual_count += 1
        assert "exam" in q and "year" in q and "group" in q, f"{qid}: Actual PYQ missing exam metadata"
    else:
        pattern_count += 1
        assert "pattern_basis" in q, f"{qid}: PYQ_PATTERN missing pattern_basis"

print(f"Validation Successful!")
print(f"  • Total Questions: {len(questions)}")
print(f"  • Actual Verified PYQs: {actual_count}")
print(f"  • PYQ Pattern Questions: {pattern_count}")

# Save files
target_dir = "data/questions/polity"
os.makedirs(target_dir, exist_ok=True)

file1 = os.path.join(target_dir, "prime_minister_pyq.json")
file2 = os.path.join(target_dir, "prime_minister_pyq_practice.json")

with open(file1, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

with open(file2, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"Saved cleanly to:\n  - {file1}\n  - {file2}")
