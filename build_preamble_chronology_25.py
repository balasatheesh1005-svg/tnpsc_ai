# -*- coding: utf-8 -*-
"""
Builder script to generate 25 TNPSC Group 1 standard Chronology MCQs for Preamble of the Constitution of India.
Saves to data/questions/polity/preamble_chronology.json with full dual-schema compliance.
"""

import json
import os

questions = [
    # -------------------------------------------------------------------------
    # Q1: PRE_CHRONO_001
    # -------------------------------------------------------------------------
    {
        "id": "PRE_CHRONO_001",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Chronology",
        "question": {
            "en": "Arrange the following historic events relating to the drafting and adoption of the Preamble in correct chronological order:\n1. Jawaharlal Nehru introduces the historic 'Objectives Resolution' in the Constituent Assembly\n2. Constituent Assembly unanimously adopts the Objectives Resolution\n3. Constituent Assembly debates and votes that the Preamble stands part of the Constitution\n4. People of India adopt, enact, and give to themselves the Constitution and Preamble",
            "ta": "முகவுரையை வரைதல் மற்றும் ஏற்றுக்கொள்வது தொடர்பான பின்வரும் வரலாற்று நிகழ்வுகளை சரியான காலவரிசையில் அமைக்கவும்:\n1. ஜவஹர்லால் நேரு வரலாற்றுச் சிறப்புமிக்க 'குறிக்கோள் தீர்மானத்தை' அரசியலமைப்பு நிர்ணய அவையில் அறிமுகப்படுத்துகிறார்\n2. அரசியலமைப்பு நிர்ணய அவை குறிக்கோள் தீர்மானத்தை ஏகமனதாக ஏற்றுக்கொள்கிறது\n3. முகவுரை அரசியலமைப்பின் ஒரு பகுதியாக அமைகிறது என்ற தீர்மானத்தின் மீது அரசியலமைப்பு நிர்ணய அவை விவாதித்து வாக்களிக்கிறது\n4. இந்திய மக்கள் அரசியலமைப்பு மற்றும் முகவுரையை ஏற்றுக்கொண்டு, இயற்றி, தங்களுக்குத் தாங்களே வழங்குகின்றனர்"
        },
        "events": [
            {
                "id": "1",
                "en": "Jawaharlal Nehru introduces the historic 'Objectives Resolution' in the Constituent Assembly",
                "ta": "ஜவஹர்லால் நேரு வரலாற்றுச் சிறப்புமிக்க 'குறிக்கோள் தீர்மானத்தை' அரசியலமைப்பு நிர்ணய அவையில் அறிமுகப்படுத்துகிறார்"
            },
            {
                "id": "2",
                "en": "Constituent Assembly unanimously adopts the Objectives Resolution",
                "ta": "அரசியலமைப்பு நிர்ணய அவை குறிக்கோள் தீர்மானத்தை ஏகமனதாக ஏற்றுக்கொள்கிறது"
            },
            {
                "id": "3",
                "en": "Constituent Assembly debates and votes that the Preamble stands part of the Constitution",
                "ta": "முகவுரை அரசியலமைப்பின் ஒரு பகுதியாக அமைகிறது என்ற தீர்மானத்தின் மீது அரசியலமைப்பு நிர்ணய அவை விவாதித்து வாக்களிக்கிறது"
            },
            {
                "id": "4",
                "en": "People of India adopt, enact, and give to themselves the Constitution and Preamble",
                "ta": "இந்திய மக்கள் அரசியலமைப்பு மற்றும் முகவுரையை ஏற்றுக்கொண்டு, இயற்றி, தங்களுக்குத் தாங்களே வழங்குகின்றனர்"
            }
        ],
        "options": [
            {"id": "A", "en": "1 -> 2 -> 3 -> 4", "ta": "1 -> 2 -> 3 -> 4"},
            {"id": "B", "en": "2 -> 1 -> 3 -> 4", "ta": "2 -> 1 -> 3 -> 4"},
            {"id": "C", "en": "1 -> 3 -> 2 -> 4", "ta": "1 -> 3 -> 2 -> 4"},
            {"id": "D", "en": "2 -> 3 -> 1 -> 4", "ta": "2 -> 3 -> 1 -> 4"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Correct Chronological Sequence: 1 (Objectives Resolution moved: Dec 13, 1946) -> 2 (Objectives Resolution adopted: Jan 22, 1947) -> 3 (Preamble voted into Constitution: Oct 17, 1949) -> 4 (Constitution & Preamble adopted: Nov 26, 1949).",
            "ta": "சரியான காலவரிசை: 1 (குறிக்கோள் தீர்மானம் முன்மொழியப்பட்டது: டிசம்பர் 13, 1946) -> 2 (குறிக்கோள் தீர்மானம் ஏற்கப்பட்டது: ஜனவரி 22, 1947) -> 3 (முகவுரை மீதான வாக்கெடுப்பு: அக்டோபர் 17, 1949) -> 4 (அரசியலமைப்பு & முகவுரை ஏற்கப்பட்டது: நவம்பர் 26, 1949)."
        },
        "why_not_others": {
            "A": {"en": "Correct. Dec 13, 1946 -> Jan 22, 1947 -> Oct 17, 1949 -> Nov 26, 1949 follows the exact Constituent Assembly chronology.", "ta": "சரி. டிசம்பர் 13, 1946 -> ஜனவரி 22, 1947 -> அக்டோபர் 17, 1949 -> நவம்பர் 26, 1949 சரியான காலவரிசையாகும்."},
            "B": {"en": "Incorrect. Objectives Resolution was moved by Nehru on Dec 13, 1946 (1) before it was adopted on Jan 22, 1947 (2).", "ta": "தவறு. குறிக்கோள் தீர்மானம் டிசம்பர் 13, 1946-ல் முன்மொழியப்பட்டது (1), பின்னரே ஜனவரி 22, 1947-ல் ஏற்கப்பட்டது (2)."},
            "C": {"en": "Incorrect. Resolution adoption (Jan 1947) preceded the final Preamble voting in the Assembly (Oct 1949).", "ta": "தவறு. தீர்மானம் ஏற்கப்பட்டது (ஜனவரி 1947) முகவுரை மீதான இறுதி வாக்கெடுப்பிற்கு (அக்டோபர் 1949) முந்தையது."},
            "D": {"en": "Incorrect. Moving the resolution (1) was the very first step in Dec 1946.", "ta": "தவறு. தீர்மானத்தை முன்மொழிவதே (1) டிசம்பர் 1946-ன் முதல் படியாகும்."}
        },
        "tnpsc_tip": {
            "en": "TNPSC Trap: The Preamble was voted upon by the Constituent Assembly on Oct 17, 1949, AFTER the rest of the Constitution was finalized to ensure conformity.",
            "ta": "TNPSC பொறி: அரசியலமைப்பின் இதர பகுதிகளுடன் முழுமையாக ஒத்துப்போவதை உறுதி செய்வதற்காக, மற்ற பகுதிகள் முடிந்த பின்னரே அக்டோபர் 17, 1949 அன்று முகவுரை மீது வாக்களிக்கப்பட்டது."
        },
        "revision_fact": {
            "en": "The motion put forth by Assembly President Dr. Rajendra Prasad was: 'The question is that the Preamble stands part of the Constitution.'",
            "ta": "அவைத் தலைவர் டாக்டர் ராஜேந்திர பிரசாத் முன்வைத்த தீர்மானம்: 'கேள்வி என்னவென்றால், முகவுரை அரசியலமைப்பின் ஒரு பகுதியாக அமைகிறது என்பதாகும்.'"
        },
        "source_reference": [
            "M. Laxmikanth - Indian Polity (Preamble)",
            "NCERT Class XI - Indian Constitution at Work",
            "Constituent Assembly Debates (Vol. X)"
        ],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "Chronology", "Objectives Resolution", "Constituent Assembly"],
        "question_en": "Arrange the following historic events relating to the drafting and adoption of the Preamble in correct chronological order:\n1. Jawaharlal Nehru introduces the historic 'Objectives Resolution' in the Constituent Assembly\n2. Constituent Assembly unanimously adopts the Objectives Resolution\n3. Constituent Assembly debates and votes that the Preamble stands part of the Constitution\n4. People of India adopt, enact, and give to themselves the Constitution and Preamble",
        "question_ta": "முகவுரையை வரைதல் மற்றும் ஏற்றுக்கொள்வது தொடர்பான பின்வரும் வரலாற்று நிகழ்வுகளை சரியான காலவரிசையில் அமைக்கவும்:\n1. ஜவஹர்லால் நேரு வரலாற்றுச் சிறப்புமிக்க 'குறிக்கோள் தீர்மானத்தை' அரசியலமைப்பு நிர்ணய அவையில் அறிமுகப்படுத்துகிறார்\n2. அரசியலமைப்பு நிர்ணய அவை குறிக்கோள் தீர்மானத்தை ஏகமனதாக ஏற்றுக்கொள்கிறது\n3. முகவுரை அரசியலமைப்பின் ஒரு பகுதியாக அமைகிறது என்ற தீர்மானத்தின் மீது அரசியலமைப்பு நிர்ணய அவை விவாதித்து வாக்களிக்கிறது\n4. இந்திய மக்கள் அரசியலமைப்பு மற்றும் முகவுரையை ஏற்றுக்கொண்டு, இயற்றி, தங்களுக்குத் தாங்களே வழங்குகின்றனர்",
        "options_en": ["1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "2 -> 3 -> 1 -> 4"],
        "options_ta": ["1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "2 -> 3 -> 1 -> 4"],
        "answer": "a",
        "explanation_en": "Correct Chronological Sequence: 1 (Objectives Resolution moved: Dec 13, 1946) -> 2 (Objectives Resolution adopted: Jan 22, 1947) -> 3 (Preamble voted into Constitution: Oct 17, 1949) -> 4 (Constitution & Preamble adopted: Nov 26, 1949).",
        "explanation_ta": "சரியான காலவரிசை: 1 (குறிக்கோள் தீர்மானம் முன்மொழியப்பட்டது: டிசம்பர் 13, 1946) -> 2 (குறிக்கோள் தீர்மானம் ஏற்கப்பட்டது: ஜனவரி 22, 1947) -> 3 (முகவுரை மீதான வாக்கெடுப்பு: அக்டோபர் 17, 1949) -> 4 (அரசியலமைப்பு & முகவுரை ஏற்கப்பட்டது: நவம்பர் 26, 1949)."
    },

    # -------------------------------------------------------------------------
    # Q2: PRE_CHRONO_002
    # -------------------------------------------------------------------------
    {
        "id": "PRE_CHRONO_002",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Chronology",
        "question": {
            "en": "Arrange the following landmark Supreme Court judgments regarding the constitutional status and interpretation of the Preamble in correct chronological order:\n1. Supreme Court rules in Berubari Union Reference that the Preamble is NOT a part of the Constitution\n2. 13-Judge Bench in Kesavananda Bharati Case declares the Preamble IS a part of the Constitution\n3. Supreme Court in S.R. Bommai Case holds Secularism in the Preamble to be an essential feature of Basic Structure\n4. Supreme Court in LIC of India Case explicitly reaffirms that the Preamble is an 'integral part' of the Constitution",
            "ta": "முகவுரையின் அரசியலமைப்பு அந்தஸ்து மற்றும் விளக்கம் தொடர்பான உச்ச நீதிமன்றத்தின் வரலாற்றுச் சிறப்புமிக்க தீர்ப்புகளை சரியான காலவரிசையில் அமைக்கவும்:\n1. பெருபாரி யூனியன் வழக்கில் முகவுரை அரசியலமைப்பின் ஒரு பகுதி அல்ல என்று உச்ச நீதிமன்றம் தீர்ப்பளிக்கிறது\n2. கேசவானந்த பாரதி வழக்கில் 13 நீதிபதிகள் கொண்ட அமர்வு முகவுரை அரசியலமைப்பின் ஒரு பகுதி என்று அறிவிக்கிறது\n3. எஸ்.ஆர். பொம்மை வழக்கில் முகவுரையில் உள்ள மதச்சார்பின்மை அடிப்படை கட்டமைப்பின் இன்றியமையாத அம்சம் என உச்ச நீதிமன்றம் தீர்ப்பளிக்கிறது\n4. எல்.ஐ.சி வழக்கில் முகவுரை அரசியலமைப்பின் 'ஒருங்கிணைந்த பகுதி' என்பதை உச்ச நீதிமன்றம் மீண்டும் உறுதிப்படுத்துகிறது"
        },
        "events": [
            {
                "id": "1",
                "en": "Supreme Court rules in Berubari Union Reference that the Preamble is NOT a part of the Constitution",
                "ta": "பெருபாரி யூனியன் வழக்கில் முகவுரை அரசியலமைப்பின் ஒரு பகுதி அல்ல என்று உச்ச நீதிமன்றம் தீர்ப்பளிக்கிறது"
            },
            {
                "id": "2",
                "en": "13-Judge Bench in Kesavananda Bharati Case declares the Preamble IS a part of the Constitution",
                "ta": "கேசவானந்த பாரதி வழக்கில் 13 நீதிபதிகள் கொண்ட அமர்வு முகவுரை அரசியலமைப்பின் ஒரு பகுதி என்று அறிவிக்கிறது"
            },
            {
                "id": "3",
                "en": "Supreme Court in S.R. Bommai Case holds Secularism in the Preamble to be an essential feature of Basic Structure",
                "ta": "எஸ்.ஆர். பொம்மை வழக்கில் முகவுரையில் உள்ள மதச்சார்பின்மை அடிப்படை கட்டமைப்பின் இன்றியமையாத அம்சம் என உச்ச நீதிமன்றம் தீர்ப்பளிக்கிறது"
            },
            {
                "id": "4",
                "en": "Supreme Court in LIC of India Case explicitly reaffirms that the Preamble is an 'integral part' of the Constitution",
                "ta": "எல்.ஐ.சி வழக்கில் முகவுரை அரசியலமைப்பின் 'ஒருங்கிணைந்த பகுதி' என்பதை உச்ச நீதிமன்றம் மீண்டும் உறுதிப்படுத்துகிறது"
            }
        ],
        "options": [
            {"id": "A", "en": "2 -> 1 -> 3 -> 4", "ta": "2 -> 1 -> 3 -> 4"},
            {"id": "B", "en": "1 -> 2 -> 3 -> 4", "ta": "1 -> 2 -> 3 -> 4"},
            {"id": "C", "en": "1 -> 3 -> 2 -> 4", "ta": "1 -> 3 -> 2 -> 4"},
            {"id": "D", "en": "1 -> 2 -> 4 -> 3", "ta": "1 -> 2 -> 4 -> 3"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "Chronological Sequence: 1 (Berubari Union Reference: 1960) -> 2 (Kesavananda Bharati Case: April 24, 1973) -> 3 (S.R. Bommai Case: 1994) -> 4 (LIC of India Case: 1995).",
            "ta": "சரியான காலவரிசை: 1 (பெருபாரி யூனியன் வழக்கு: 1960) -> 2 (கேசவானந்த பாரதி வழக்கு: ஏப்ரல் 24, 1973) -> 3 (எஸ்.ஆர். பொம்மை வழக்கு: 1994) -> 4 (எல்.ஐ.சி வழக்கு: 1995)."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Berubari Union (1960) came before Kesavananda Bharati (1973).", "ta": "தவறு. பெருபாரி யூனியன் (1960) கேசவானந்த பாரதிக்கு (1973) முந்தையது."},
            "B": {"en": "Correct. 1960 (Berubari) -> 1973 (Kesavananda) -> 1994 (Bommai) -> 1995 (LIC of India) is the accurate judicial timeline.", "ta": "சரி. 1960 (பெருபாரி) -> 1973 (கேசவானந்தா) -> 1994 (பொம்மை) -> 1995 (எல்ஐசி) துல்லியமான நீதித்துறை காலவரிசை."},
            "C": {"en": "Incorrect. S.R. Bommai case was decided in 1994, long after Kesavananda Bharati in 1973.", "ta": "தவறு. எஸ்.ஆர். பொம்மை வழக்கு 1994-ல் தீர்ப்பளிக்கப்பட்டது, இது 1973 கேசவானந்த பாரதிக்கு பல ஆண்டுகள் பிந்தையது."},
            "D": {"en": "Incorrect. S.R. Bommai (1994) preceded LIC of India (1995).", "ta": "தவறு. எஸ்.ஆர். பொம்மை (1994) எல்ஐசி வழக்குக்கு (1995) முந்தையது."}
        },
        "tnpsc_tip": {
            "en": "TNPSC Key Rule: Berubari (1960) = NOT part; Kesavananda (1973) = IS part; LIC of India (1995) = INTEGRAL part.",
            "ta": "TNPSC முக்கிய விதி: பெருபாரி (1960) = பகுதி அல்ல; கேசவானந்தா (1973) = ஒரு பகுதி; எல்ஐசி (1995) = ஒருங்கிணைந்த பகுதி."
        },
        "revision_fact": {
            "en": "In S.R. Bommai (1994), the Supreme Court upheld the dismissal of state governments under Article 356 for anti-secular policies, citing Preamble secularism.",
            "ta": "எஸ்.ஆர். பொம்மை (1994) வழக்கில், முகவுரையின் மதச்சார்பின்மையை மேற்கோள் காட்டி, மதச்சார்பற்ற கொள்கைகளுக்கு எதிராக செயல்பட்ட மாநில அரசுகளை உறுப்பு 356-ன் கீழ் கலைத்தது செல்லும் என உறுதி செய்யப்பட்டது."
        },
        "source_reference": [
            "M. Laxmikanth - Indian Polity (Preamble & Basic Structure)",
            "Supreme Court Reports (1960, 1973, 1994, 1995)"
        ],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "Judicial Evolution", "Kesavananda Bharati", "Berubari Union", "SR Bommai", "LIC Case"],
        "question_en": "Arrange the following landmark Supreme Court judgments regarding the constitutional status and interpretation of the Preamble in correct chronological order:\n1. Supreme Court rules in Berubari Union Reference that the Preamble is NOT a part of the Constitution\n2. 13-Judge Bench in Kesavananda Bharati Case declares the Preamble IS a part of the Constitution\n3. Supreme Court in S.R. Bommai Case holds Secularism in the Preamble to be an essential feature of Basic Structure\n4. Supreme Court in LIC of India Case explicitly reaffirms that the Preamble is an 'integral part' of the Constitution",
        "question_ta": "முகவுரையின் அரசியலமைப்பு அந்தஸ்து மற்றும் விளக்கம் தொடர்பான உச்ச நீதிமன்றத்தின் வரலாற்றுச் சிறப்புமிக்க தீர்ப்புகளை சரியான காலவரிசையில் அமைக்கவும்:\n1. பெருபாரி யூனியன் வழக்கில் முகவுரை அரசியலமைப்பின் ஒரு பகுதி அல்ல என்று உச்ச நீதிமன்றம் தீர்ப்பளிக்கிறது\n2. கேசவானந்த பாரதி வழக்கில் 13 நீதிபதிகள் கொண்ட அமர்வு முகவுரை அரசியலமைப்பின் ஒரு பகுதி என்று அறிவிக்கிறது\n3. எஸ்.ஆர். பொம்மை வழக்கில் முகவுரையில் உள்ள மதச்சார்பின்மை அடிப்படை கட்டமைப்பின் இன்றியமையாத அம்சம் என உச்ச நீதிமன்றம் தீர்ப்பளிக்கிறது\n4. எல்.ஐ.சி வழக்கில் முகவுரை அரசியலமைப்பின் 'ஒருங்கிணைந்த பகுதி' என்பதை உச்ச நீதிமன்றம் மீண்டும் உறுதிப்படுத்துகிறது",
        "options_en": ["2 -> 1 -> 3 -> 4", "1 -> 2 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "1 -> 2 -> 4 -> 3"],
        "options_ta": ["2 -> 1 -> 3 -> 4", "1 -> 2 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "1 -> 2 -> 4 -> 3"],
        "answer": "b",
        "explanation_en": "Chronological Sequence: 1 (Berubari Union Reference: 1960) -> 2 (Kesavananda Bharati Case: April 24, 1973) -> 3 (S.R. Bommai Case: 1994) -> 4 (LIC of India Case: 1995).",
        "explanation_ta": "சரியான காலவரிசை: 1 (பெருபாரி யூனியன் வழக்கு: 1960) -> 2 (கேசவானந்த பாரதி வழக்கு: ஏப்ரல் 24, 1973) -> 3 (எஸ்.ஆர். பொம்மை வழக்கு: 1994) -> 4 (எல்.ஐ.சி வழக்கு: 1995)."
    },

    # -------------------------------------------------------------------------
    # Q3: PRE_CHRONO_003
    # -------------------------------------------------------------------------
    {
        "id": "PRE_CHRONO_003",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Chronology",
        "question": {
            "en": "Arrange the following constitutional developments concerning the amendability and text of the Preamble in correct chronological sequence:\n1. Supreme Court holds Preamble cannot be amended as it is not part of Constitution (Berubari Opinion)\n2. Supreme Court rules Preamble can be amended under Article 368 subject to Basic Structure (Kesavananda Bharati)\n3. Enactment of the 42nd Constitutional Amendment Act inserting Socialist, Secular, and Integrity into Preamble\n4. Formal enforcement date of the 42nd Constitutional Amendment Act provisions amending the Preamble",
            "ta": "முகவுரையின் திருத்தப்படும் தன்மை மற்றும் உரை தொடர்பான பின்வரும் அரசியலமைப்பு முன்னேற்றங்களை சரியான காலவரிசையில் அமைக்கவும்:\n1. முகவுரை அரசியலமைப்பின் பகுதி அல்ல என்பதால் அதைத் திருத்த முடியாது என உச்ச நீதிமன்றம் கருதுகிறது (பெருபாரி கருத்து)\n2. அடிப்படை கட்டமைப்பிற்கு உட்பட்டு உறுப்பு 368-ன் கீழ் முகவுரையைத் திருத்த முடியும் என உச்ச நீதிமன்றம் தீர்ப்பளிக்கிறது (கேசவானந்த பாரதி)\n3. முகவுரையில் சமதர்ம, மதச்சார்பற்ற மற்றும் ஒருமைப்பாடு ஆகிய சொற்களைச் சேர்க்கும் 42வது அரசியலமைப்புத் திருத்தச் சட்டம் இயற்றப்படுதல்\n4. முகவுரையைத் திருத்திய 42வது அரசியலமைப்புத் திருத்தச் சட்ட விதிகள் முறையாக நடைமுறைக்கு வந்த நாள்"
        },
        "events": [
            {
                "id": "1",
                "en": "Supreme Court holds Preamble cannot be amended as it is not part of Constitution (Berubari Opinion)",
                "ta": "முகவுரை அரசியலமைப்பின் பகுதி அல்ல என்பதால் அதைத் திருத்த முடியாது என உச்ச நீதிமன்றம் கருதுகிறது (பெருபாரி கருத்து)"
            },
            {
                "id": "2",
                "en": "Supreme Court rules Preamble can be amended under Article 368 subject to Basic Structure (Kesavananda Bharati)",
                "ta": "அடிப்படை கட்டமைப்பிற்கு உட்பட்டு உறுப்பு 368-ன் கீழ் முகவுரையைத் திருத்த முடியும் என உச்ச நீதிமன்றம் தீர்ப்பளிக்கிறது (கேசவானந்த பாரதி)"
            },
            {
                "id": "3",
                "en": "Enactment of the 42nd Constitutional Amendment Act inserting Socialist, Secular, and Integrity into Preamble",
                "ta": "முகவுரையில் சமதர்ம, மதச்சார்பற்ற மற்றும் ஒருமைப்பாடு ஆகிய சொற்களைச் சேர்க்கும் 42வது அரசியலமைப்புத் திருத்தச் சட்டம் இயற்றப்படுதல்"
            },
            {
                "id": "4",
                "en": "Formal enforcement date of the 42nd Constitutional Amendment Act provisions amending the Preamble",
                "ta": "முகவுரையைத் திருத்திய 42வது அரசியலமைப்புத் திருத்தச் சட்ட விதிகள் முறையாக நடைமுறைக்கு வந்த நாள்"
            }
        ],
        "options": [
            {"id": "A", "en": "2 -> 1 -> 3 -> 4", "ta": "2 -> 1 -> 3 -> 4"},
            {"id": "B", "en": "1 -> 3 -> 2 -> 4", "ta": "1 -> 3 -> 2 -> 4"},
            {"id": "C", "en": "1 -> 2 -> 3 -> 4", "ta": "1 -> 2 -> 3 -> 4"},
            {"id": "D", "en": "1 -> 2 -> 4 -> 3", "ta": "1 -> 2 -> 4 -> 3"}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "Correct Sequence: 1 (Berubari view: 1960) -> 2 (Kesavananda Bharati verdict on Art 368: 1973) -> 3 (42nd Amendment passed: 1976) -> 4 (42nd Amendment enforced: January 3, 1977).",
            "ta": "சரியான வரிசை: 1 (பெருபாரி பார்வை: 1960) -> 2 (உறுப்பு 368 மீதான கேசவானந்த பாரதி தீர்ப்பு: 1973) -> 3 (42வது திருத்தம் இயற்றப்பட்டது: 1976) -> 4 (42வது திருத்தம் அமலானது: ஜனவரி 3, 1977)."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Berubari opinion (1960) preceded Kesavananda Bharati (1973).", "ta": "தவறு. பெருபாரி கருத்து (1960) கேசவானந்த பாரதிக்கு (1973) முந்தையது."},
            "B": {"en": "Incorrect. Kesavananda Bharati (1973) provided the legal basis for amending the Preamble in 1976 (3).", "ta": "தவறு. கேசவானந்த பாரதி (1973) தீர்ப்பே 1976-ல் முகவுரையைத் திருத்துவதற்கான சட்ட அடிப்படையை வழங்கியது."},
            "C": {"en": "Correct. 1 (1960) -> 2 (1973) -> 3 (Enacted 1976) -> 4 (Enforced Jan 3, 1977) follows the exact sequence.", "ta": "சரி. 1 (1960) -> 2 (1973) -> 3 (இயற்றப்பட்டது 1976) -> 4 (அமலானது ஜனவரி 3, 1977) துல்லியமான வரிசையாகும்."},
            "D": {"en": "Incorrect. The 42nd Amendment was passed in 1976 (3) before its enforcement on Jan 3, 1977 (4).", "ta": "தவறு. 42வது திருத்தம் 1976-ல் இயற்றப்பட்டது (3), பின்னரே ஜனவரி 3, 1977-ல் அமலானது (4)."}
        },
        "tnpsc_tip": {
            "en": "TNPSC Trap: Do NOT confuse enactment year (1976) with enforcement date (January 3, 1977) for the 42nd Amendment.",
            "ta": "TNPSC பொறி: 42வது திருத்தச் சட்டத்தின் இயற்றப்பட்ட ஆண்டு (1976) மற்றும் நடைமுறைக்கு வந்த நாள் (ஜனவரி 3, 1977) ஆகியவற்றை குழப்பிக் கொள்ளக் கூடாது."
        },
        "revision_fact": {
            "en": "The Preamble has been amended only once in constitutional history till date, by the 42nd Constitutional Amendment Act.",
            "ta": "இந்திய அரசியலமைப்பு வரலாற்றில் முகவுரை இதுவரை ஒரே ஒரு முறை மட்டுமே 42வது அரசியலமைப்புத் திருத்தச் சட்டத்தால் திருத்தப்பட்டுள்ளது."
        },
        "source_reference": [
            "M. Laxmikanth - Indian Polity",
            "Constitution (Forty-second Amendment) Act, 1976",
            "NCERT Class XI - Indian Constitution at Work"
        ],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "42nd Amendment", "Article 368", "Kesavananda Bharati"],
        "question_en": "Arrange the following constitutional developments concerning the amendability and text of the Preamble in correct chronological sequence:\n1. Supreme Court holds Preamble cannot be amended as it is not part of Constitution (Berubari Opinion)\n2. Supreme Court rules Preamble can be amended under Article 368 subject to Basic Structure (Kesavananda Bharati)\n3. Enactment of the 42nd Constitutional Amendment Act inserting Socialist, Secular, and Integrity into Preamble\n4. Formal enforcement date of the 42nd Constitutional Amendment Act provisions amending the Preamble",
        "question_ta": "முகவுரையின் திருத்தப்படும் தன்மை மற்றும் உரை தொடர்பான பின்வரும் அரசியலமைப்பு முன்னேற்றங்களை சரியான காலவரிசையில் அமைக்கவும்:\n1. முகவுரை அரசியலமைப்பின் பகுதி அல்ல என்பதால் அதைத் திருத்த முடியாது என உச்ச நீதிமன்றம் கருதுகிறது (பெருபாரி கருத்து)\n2. அடிப்படை கட்டமைப்பிற்கு உட்பட்டு உறுப்பு 368-ன் கீழ் முகவுரையைத் திருத்த முடியும் என உச்ச நீதிமன்றம் தீர்ப்பளிக்கிறது (கேசவானந்த பாரதி)\n3. முகவுரையில் சமதர்ம, மதச்சார்பற்ற மற்றும் ஒருமைப்பாடு ஆகிய சொற்களைச் சேர்க்கும் 42வது அரசியலமைப்புத் திருத்தச் சட்டம் இயற்றப்படுதல்\n4. முகவுரையைத் திருத்திய 42வது அரசியலமைப்புத் திருத்தச் சட்ட விதிகள் முறையாக நடைமுறைக்கு வந்த நாள்",
        "options_en": ["2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "1 -> 2 -> 3 -> 4", "1 -> 2 -> 4 -> 3"],
        "options_ta": ["2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "1 -> 2 -> 3 -> 4", "1 -> 2 -> 4 -> 3"],
        "answer": "c",
        "explanation_en": "Correct Sequence: 1 (Berubari view: 1960) -> 2 (Kesavananda Bharati verdict on Art 368: 1973) -> 3 (42nd Amendment passed: 1976) -> 4 (42nd Amendment enforced: January 3, 1977).",
        "explanation_ta": "சரியான வரிசை: 1 (பெருபாரி பார்வை: 1960) -> 2 (உறுப்பு 368 மீதான கேசவானந்த பாரதி தீர்ப்பு: 1973) -> 3 (42வது திருத்தம் இயற்றப்பட்டது: 1976) -> 4 (42வது திருத்தம் அமலானது: ஜனவரி 3, 1977)."
    },

    # -------------------------------------------------------------------------
    # Q4: PRE_CHRONO_004
    # -------------------------------------------------------------------------
    {
        "id": "PRE_CHRONO_004",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Chronology",
        "question": {
            "en": "Arrange the following key terms defining the 'Nature of the Indian State' in the exact textual sequence as they appear in the Preamble:\n1. Sovereign\n2. Socialist\n3. Secular\n4. Democratic",
            "ta": "முகவுரையில் இடம்பெற்றுள்ளவாறு 'இந்திய அரசின் தன்மையை' வரையறுக்கும் பின்வரும் முக்கிய சொற்களை சரியான உரை வரிசையில் அமைக்கவும்:\n1. இறையாண்மை (Sovereign)\n2. சமதர்ம (Socialist)\n3. மதச்சார்பற்ற (Secular)\n4. ஜனநாயக (Democratic)"
        },
        "events": [
            {
                "id": "1",
                "en": "Sovereign",
                "ta": "இறையாண்மை"
            },
            {
                "id": "2",
                "en": "Socialist",
                "ta": "சமதர்ம"
            },
            {
                "id": "3",
                "en": "Secular",
                "ta": "மதச்சார்பற்ற"
            },
            {
                "id": "4",
                "en": "Democratic",
                "ta": "ஜனநாயக"
            }
        ],
        "options": [
            {"id": "A", "en": "1 -> 3 -> 2 -> 4", "ta": "1 -> 3 -> 2 -> 4"},
            {"id": "B", "en": "2 -> 3 -> 1 -> 4", "ta": "2 -> 3 -> 1 -> 4"},
            {"id": "C", "en": "1 -> 4 -> 2 -> 3", "ta": "1 -> 4 -> 2 -> 3"},
            {"id": "D", "en": "1 -> 2 -> 3 -> 4", "ta": "1 -> 2 -> 3 -> 4"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "Textual Sequence in Preamble: 'SOVEREIGN SOCIALIST SECULAR DEMOCRATIC REPUBLIC' (S-S-S-D-R). Hence, 1 (Sovereign) -> 2 (Socialist) -> 3 (Secular) -> 4 (Democratic).",
            "ta": "முகவுரையின் உரை வரிசை: 'இறையாண்மை சமதர்ம மதச்சார்பற்ற ஜனநாயக குடியரசு' (S-S-S-D-R). எனவே, 1 (இறையாண்மை) -> 2 (சமதர்ம) -> 3 (மதச்சார்பற்ற) -> 4 (ஜனநாயக)."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. 'Socialist' appears before 'Secular' in the Preamble text.", "ta": "தவறு. முகவுரையில் 'சமதர்ம' என்பது 'மதச்சார்பற்ற' என்பதற்கு முன்பாக வருகிறது."},
            "B": {"en": "Incorrect. 'Sovereign' is the very first adjective declaring India's status.", "ta": "தவறு. 'இறையாண்மை' என்பதே இந்தியாவின் நிலையை அறிவிக்கும் முதல் சொல்லாகும்."},
            "C": {"en": "Incorrect. 'Democratic' appears after Socialist and Secular in the amended text.", "ta": "தவறு. திருத்தப்பட்ட உரையில் 'ஜனநாயக' என்பது சமதர்ம மற்றும் மதச்சார்பற்ற சொற்களுக்குப் பின்னரே வருகிறது."},
            "D": {"en": "Correct. 1 (Sovereign) -> 2 (Socialist) -> 3 (Secular) -> 4 (Democratic) -> followed by Republic represents the exact textual sequence.", "ta": "சரி. 1 (இறையாண்மை) -> 2 (சமதர்ம) -> 3 (மதச்சார்பற்ற) -> 4 (ஜனநாயக) -> குடியரசு என்பது துல்லியமான உரை வரிசையாகும்."}
        },
        "tnpsc_tip": {
            "en": "Mnemonic for TNPSC: S-S-S-D-R (Sovereign, Socialist, Secular, Democratic, Republic). Original 1950 Preamble was S-D-R.",
            "ta": "TNPSC நினைவூட்டல்: S-S-S-D-R (இறையாண்மை, சமதர்ம, மதச்சார்பற்ற, ஜனநாயக, குடியரசு). அசல் 1950 முகவுரையில் S-D-R என இருந்தது."
        },
        "revision_fact": {
            "en": "The 42nd Amendment of 1976 changed 'SOVEREIGN DEMOCRATIC REPUBLIC' to 'SOVEREIGN SOCIALIST SECULAR DEMOCRATIC REPUBLIC'.",
            "ta": "1976-ன் 42வது திருத்தம் 'இறையாண்மை ஜனநாயகக் குடியரசு' என்பதை 'இறையாண்மை சமதர்ம மதச்சார்பற்ற ஜனநாயகக் குடியரசு' என மாற்றியது."
        },
        "source_reference": [
            "Text of the Constitution of India (Preamble)",
            "M. Laxmikanth - Indian Polity",
            "Samacheer Kalvi - Standard 11 Political Science"
        ],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "Nature of State", "Sequence", "Textual Order"],
        "question_en": "Arrange the following key terms defining the 'Nature of the Indian State' in the exact textual sequence as they appear in the Preamble:\n1. Sovereign\n2. Socialist\n3. Secular\n4. Democratic",
        "question_ta": "முகவுரையில் இடம்பெற்றுள்ளவாறு 'இந்திய அரசின் தன்மையை' வரையறுக்கும் பின்வரும் முக்கிய சொற்களை சரியான உரை வரிசையில் அமைக்கவும்:\n1. இறையாண்மை (Sovereign)\n2. சமதர்ம (Socialist)\n3. மதச்சார்பற்ற (Secular)\n4. ஜனநாயக (Democratic)",
        "options_en": ["1 -> 3 -> 2 -> 4", "2 -> 3 -> 1 -> 4", "1 -> 4 -> 2 -> 3", "1 -> 2 -> 3 -> 4"],
        "options_ta": ["1 -> 3 -> 2 -> 4", "2 -> 3 -> 1 -> 4", "1 -> 4 -> 2 -> 3", "1 -> 2 -> 3 -> 4"],
        "answer": "d",
        "explanation_en": "Textual Sequence in Preamble: 'SOVEREIGN SOCIALIST SECULAR DEMOCRATIC REPUBLIC' (S-S-S-D-R). Hence, 1 (Sovereign) -> 2 (Socialist) -> 3 (Secular) -> 4 (Democratic).",
        "explanation_ta": "முகவுரையின் உரை வரிசை: 'இறையாண்மை சமதர்ம மதச்சார்பற்ற ஜனநாயக குடியரசு' (S-S-S-D-R). எனவே, 1 (இறையாண்மை) -> 2 (சமதர்ம) -> 3 (மதச்சார்பற்ற) -> 4 (ஜனநாயக)."
    },

    # -------------------------------------------------------------------------
    # Q5: PRE_CHRONO_005
    # -------------------------------------------------------------------------
    {
        "id": "PRE_CHRONO_005",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Chronology",
        "question": {
            "en": "Arrange the following four fundamental 'Objectives of the Constitution' in the exact sequential order as stated in the Preamble:\n1. JUSTICE (Social, Economic, and Political)\n2. LIBERTY (of thought, expression, belief, faith, and worship)\n3. EQUALITY (of status and of opportunity)\n4. FRATERNITY (assuring the dignity of the individual and unity & integrity of the Nation)",
            "ta": "முகவுரையில் குறிப்பிடப்பட்டுள்ள 'அரசியலமைப்பின் நான்கு அடிப்படை இலக்குகளை' சரியான உரை வரிசையில் அமைக்கவும்:\n1. நீதி (சமூக, பொருளாதார மற்றும் அரசியல்)\n2. சுதந்திரம் (சிந்தனை, வெளிப்பாடு, நம்பிக்கை, சமயம் மற்றும் வழிபாடு)\n3. சமத்துவம் (தகுதி மற்றும் வாய்ப்பு)\n4. சகோதரத்துவம் (தனிமனித கண்ணியம் மற்றும் தேசத்தின் ஒற்றுமை, ஒருமைப்பாடு)"
        },
        "events": [
            {
                "id": "1",
                "en": "JUSTICE (Social, Economic, and Political)",
                "ta": "நீதி (சமூக, பொருளாதார மற்றும் அரசியல்)"
            },
            {
                "id": "2",
                "en": "LIBERTY (of thought, expression, belief, faith, and worship)",
                "ta": "சுதந்திரம் (சிந்தனை, வெளிப்பாடு, நம்பிக்கை, சமயம் மற்றும் வழிபாடு)"
            },
            {
                "id": "3",
                "en": "EQUALITY (of status and of opportunity)",
                "ta": "சமத்துவம் (தகுதி மற்றும் வாய்ப்பு)"
            },
            {
                "id": "4",
                "en": "FRATERNITY (assuring the dignity of the individual and unity & integrity of the Nation)",
                "ta": "சகோதரத்துவம் (தனிமனித கண்ணியம் மற்றும் தேசத்தின் ஒற்றுமை, ஒருமைப்பாடு)"
            }
        ],
        "options": [
            {"id": "A", "en": "1 -> 2 -> 3 -> 4", "ta": "1 -> 2 -> 3 -> 4"},
            {"id": "B", "en": "2 -> 1 -> 3 -> 4", "ta": "2 -> 1 -> 3 -> 4"},
            {"id": "C", "en": "1 -> 3 -> 2 -> 4", "ta": "1 -> 3 -> 2 -> 4"},
            {"id": "D", "en": "3 -> 1 -> 2 -> 4", "ta": "3 -> 1 -> 2 -> 4"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Textual Sequence of Objectives: JUSTICE -> LIBERTY -> EQUALITY -> FRATERNITY (J-L-E-F). Hence, 1 -> 2 -> 3 -> 4 is the exact sequence.",
            "ta": "இலக்குகளின் உரை வரிசை: நீதி -> சுதந்திரம் -> சமத்துவம் -> சகோதரத்துவம் (J-L-E-F). எனவே, 1 -> 2 -> 3 -> 4 என்பது சரியான வரிசையாகும்."
        },
        "why_not_others": {
            "A": {"en": "Correct. J-L-E-F (Justice -> Liberty -> Equality -> Fraternity) exactly mirrors the constitutional text.", "ta": "சரி. J-L-E-F (நீதி -> சுதந்திரம் -> சமத்துவம் -> சகோதரத்துவம்) அரசியலமைப்பு உரையைத் துல்லியமாகப் பிரதிபலிக்கிறது."},
            "B": {"en": "Incorrect. Justice precedes Liberty in the Preamble.", "ta": "தவறு. முகவுரையில் சுதந்திரத்திற்கு முன்பாக நீதி வருகிறது."},
            "C": {"en": "Incorrect. Liberty precedes Equality in the Preamble.", "ta": "தவறு. முகவுரையில் சமத்துவத்திற்கு முன்பாக சுதந்திரம் வருகிறது."},
            "D": {"en": "Incorrect. Equality is not the first objective; Justice is the first.", "ta": "தவறு. சமத்துவம் முதல் இலக்கல்ல; நீதியே முதல் இலக்காகும்."}
        },
        "tnpsc_tip": {
            "en": "Mnemonic for TNPSC: J-L-E-F (Justice, Liberty, Equality, Fraternity). High-frequency TNPSC sequence question.",
            "ta": "TNPSC நினைவூட்டல்: J-L-E-F (நீதி, சுதந்திரம், சமத்துவம், சகோதரத்துவம்). அடிக்கடி கேட்கப்படும் வரிசை வினா."
        },
        "revision_fact": {
            "en": "The ideals of Justice (Social, Economic, Political) were inspired by the Russian Revolution (1917), while Liberty, Equality, Fraternity came from the French Revolution (1789).",
            "ta": "நீதி (சமூக, பொருளாதார, அரசியல்) இலக்குகள் ரஷ்யப் புரட்சியிலிருந்தும் (1917), சுதந்திரம், சமத்துவம், சகோதரத்துவம் ஆகியவை பிரெஞ்சுப் புரட்சியிலிருந்தும் (1789) பெறப்பட்டன."
        },
        "source_reference": [
            "Text of the Constitution of India (Preamble)",
            "M. Laxmikanth - Indian Polity",
            "NCERT Class XI - Indian Constitution at Work"
        ],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "Objectives", "Sequence", "Justice Liberty Equality Fraternity"],
        "question_en": "Arrange the following four fundamental 'Objectives of the Constitution' in the exact sequential order as stated in the Preamble:\n1. JUSTICE (Social, Economic, and Political)\n2. LIBERTY (of thought, expression, belief, faith, and worship)\n3. EQUALITY (of status and of opportunity)\n4. FRATERNITY (assuring the dignity of the individual and unity & integrity of the Nation)",
        "question_ta": "முகவுரையில் குறிப்பிடப்பட்டுள்ள 'அரசியலமைப்பின் நான்கு அடிப்படை இலக்குகளை' சரியான உரை வரிசையில் அமைக்கவும்:\n1. நீதி (சமூக, பொருளாதார மற்றும் அரசியல்)\n2. சுதந்திரம் (சிந்தனை, வெளிப்பாடு, நம்பிக்கை, சமயம் மற்றும் வழிபாடு)\n3. சமத்துவம் (தகுதி மற்றும் வாய்ப்பு)\n4. சகோதரத்துவம் (தனிமனித கண்ணியம் மற்றும் தேசத்தின் ஒற்றுமை, ஒருமைப்பாடு)",
        "options_en": ["1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "3 -> 1 -> 2 -> 4"],
        "options_ta": ["1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "3 -> 1 -> 2 -> 4"],
        "answer": "a",
        "explanation_en": "Textual Sequence of Objectives: JUSTICE -> LIBERTY -> EQUALITY -> FRATERNITY (J-L-E-F). Hence, 1 -> 2 -> 3 -> 4 is the exact sequence.",
        "explanation_ta": "இலக்குகளின் உரை வரிசை: நீதி -> சுதந்திரம் -> சமத்துவம் -> சகோதரத்துவம் (J-L-E-F). எனவே, 1 -> 2 -> 3 -> 4 என்பது சரியான வரிசையாகும்."
    },

    # -------------------------------------------------------------------------
    # Q6: PRE_CHRONO_006
    # -------------------------------------------------------------------------
    {
        "id": "PRE_CHRONO_006",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Chronology",
        "question": {
            "en": "Arrange the following landmark Supreme Court judgments that shaped the judicial interpretation of Preamble ideals in correct chronological order:\n1. Kesavananda Bharati Case (Derives Basic Structure Doctrine using Preamble philosophy)\n2. Maneka Gandhi Case (Uses Preamble ideals of Liberty and Justice to expand Article 21)\n3. Minerva Mills Case (Affirms harmony between Fundamental Rights and DPSP as Basic Structure to achieve Preamble goals)\n4. S.R. Bommai Case (Declares Secularism in the Preamble as part of the Basic Structure)",
            "ta": "முகவுரைக் கோட்பாடுகளின் நீதித்துறை விளக்கத்தை வடிவமைத்த உச்ச நீதிமன்றத்தின் வரலாற்றுச் சிறப்புமிக்க தீர்ப்புகளை சரியான காலவரிசையில் அமைக்கவும்:\n1. கேசவானந்த பாரதி வழக்கு (முகவுரை தத்துவத்தைப் பயன்படுத்தி அடிப்படை கட்டமைப்புக் கோட்பாட்டை உருவாக்குகிறது)\n2. மேனகா காந்தி வழக்கு (சுதந்திரம் மற்றும் நீதி என்ற முகவுரை இலக்குகளைப் பயன்படுத்தி உறுப்பு 21-ஐ விரிவுபடுத்துகிறது)\n3. மினர்வா மில்ஸ் வழக்கு (முகவுரை இலக்குகளை அடைய அடிப்படை உரிமைகள் மற்றும் DPSP இடையேயான சமநிலையே அடிப்படை கட்டமைப்பு என உறுதிப்படுத்துகிறது)\n4. எஸ்.ஆர். பொம்மை வழக்கு (முகவுரையில் உள்ள மதச்சார்பின்மை அடிப்படை கட்டமைப்பின் ஒரு பகுதி என அறிவிக்கிறது)"
        },
        "events": [
            {
                "id": "1",
                "en": "Kesavananda Bharati Case (Derives Basic Structure Doctrine using Preamble philosophy)",
                "ta": "கேசவானந்த பாரதி வழக்கு (முகவுரை தத்துவத்தைப் பயன்படுத்தி அடிப்படை கட்டமைப்புக் கோட்பாட்டை உருவாக்குகிறது)"
            },
            {
                "id": "2",
                "en": "Maneka Gandhi Case (Uses Preamble ideals of Liberty and Justice to expand Article 21)",
                "ta": "மேனகா காந்தி வழக்கு (சுதந்திரம் மற்றும் நீதி என்ற முகவுரை இலக்குகளைப் பயன்படுத்தி உறுப்பு 21-ஐ விரிவுபடுத்துகிறது)"
            },
            {
                "id": "3",
                "en": "Minerva Mills Case (Affirms harmony between Fundamental Rights and DPSP as Basic Structure to achieve Preamble goals)",
                "ta": "மினர்வா மில்ஸ் வழக்கு (முகவுரை இலக்குகளை அடைய அடிப்படை உரிமைகள் மற்றும் DPSP இடையேயான சமநிலையே அடிப்படை கட்டமைப்பு என உறுதிப்படுத்துகிறது)"
            },
            {
                "id": "4",
                "en": "S.R. Bommai Case (Declares Secularism in the Preamble as part of the Basic Structure)",
                "ta": "எஸ்.ஆர். பொம்மை வழக்கு (முகவுரையில் உள்ள மதச்சார்பின்மை அடிப்படை கட்டமைப்பின் ஒரு பகுதி என அறிவிக்கிறது)"
            }
        ],
        "options": [
            {"id": "A", "en": "2 -> 1 -> 3 -> 4", "ta": "2 -> 1 -> 3 -> 4"},
            {"id": "B", "en": "1 -> 2 -> 3 -> 4", "ta": "1 -> 2 -> 3 -> 4"},
            {"id": "C", "en": "1 -> 3 -> 2 -> 4", "ta": "1 -> 3 -> 2 -> 4"},
            {"id": "D", "en": "1 -> 2 -> 4 -> 3", "ta": "1 -> 2 -> 4 -> 3"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "Correct Chronological Order: 1 (Kesavananda Bharati: 1973) -> 2 (Maneka Gandhi: 1978) -> 3 (Minerva Mills: 1980) -> 4 (S.R. Bommai: 1994).",
            "ta": "சரியான காலவரிசை: 1 (கேசவானந்த பாரதி: 1973) -> 2 (மேனகா காந்தி: 1978) -> 3 (மினர்வா மில்ஸ்: 1980) -> 4 (எஸ்.ஆர். பொம்மை: 1994)."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Kesavananda Bharati (1973) preceded Maneka Gandhi (1978).", "ta": "தவறு. கேசவானந்த பாரதி (1973) மேனகா காந்திக்கு (1978) முந்தையது."},
            "B": {"en": "Correct. 1973 -> 1978 -> 1980 -> 1994 accurately traces the jurisprudence.", "ta": "சரி. 1973 -> 1978 -> 1980 -> 1994 வழக்கியல் காலவரிசையைத் துல்லியமாகப் பின்பற்றுகிறது."},
            "C": {"en": "Incorrect. Maneka Gandhi (1978) was decided before Minerva Mills (1980).", "ta": "தவறு. மேனகா காந்தி (1978) மினர்வா மில்ஸுக்கு (1980) முன்பாகத் தீர்ப்பளிக்கப்பட்டது."},
            "D": {"en": "Incorrect. Minerva Mills was decided in 1980, before S.R. Bommai in 1994.", "ta": "தவறு. மினர்வா மில்ஸ் 1980-ல் தீர்ப்பளிக்கப்பட்டது, இது 1994 எஸ்.ஆர். பொம்மைக்கு முந்தையது."}
        },
        "tnpsc_tip": {
            "en": "TNPSC Case Timeline: Kesavananda (1973) -> Maneka Gandhi (1978) -> Minerva Mills (1980) -> S.R. Bommai (1994).",
            "ta": "TNPSC வழக்கு காலவரிசை: கேசவானந்தா (1973) -> மேனகா காந்தி (1978) -> மினர்வா மில்ஸ் (1980) -> எஸ்.ஆர். பொம்மை (1994)."
        },
        "revision_fact": {
            "en": "In Minerva Mills (1980), the SC observed that Part III (FRs) and Part IV (DPSPs) are like two wheels of a chariot, working together to achieve Preamble goals.",
            "ta": "மினர்வா மில்ஸ் (1980) வழக்கில், பகுதி III (அடிப்படை உரிமைகள்) மற்றும் பகுதி IV (DPSP) ஆகியவை முகவுரை இலக்குகளை அடையும் ஒரு ரதத்தின் இரு சக்கரங்கள் போன்றது என உச்ச நீதிமன்றம் குறிப்பிட்டது."
        },
        "source_reference": [
            "M. Laxmikanth - Indian Polity",
            "DD Basu - Introduction to the Constitution of India",
            "Supreme Court Judgments (1973, 1978, 1980, 1994)"
        ],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "Judicial Interpretation", "Basic Structure", "Case Chronology"],
        "question_en": "Arrange the following landmark Supreme Court judgments that shaped the judicial interpretation of Preamble ideals in correct chronological order:\n1. Kesavananda Bharati Case (Derives Basic Structure Doctrine using Preamble philosophy)\n2. Maneka Gandhi Case (Uses Preamble ideals of Liberty and Justice to expand Article 21)\n3. Minerva Mills Case (Affirms harmony between Fundamental Rights and DPSP as Basic Structure to achieve Preamble goals)\n4. S.R. Bommai Case (Declares Secularism in the Preamble as part of the Basic Structure)",
        "question_ta": "முகவுரைக் கோட்பாடுகளின் நீதித்துறை விளக்கத்தை வடிவமைத்த உச்ச நீதிமன்றத்தின் வரலாற்றுச் சிறப்புமிக்க தீர்ப்புகளை சரியான காலவரிசையில் அமைக்கவும்:\n1. கேசவானந்த பாரதி வழக்கு (முகவுரை தத்துவத்தைப் பயன்படுத்தி அடிப்படை கட்டமைப்புக் கோட்பாட்டை உருவாக்குகிறது)\n2. மேனகா காந்தி வழக்கு (சுதந்திரம் மற்றும் நீதி என்ற முகவுரை இலக்குகளைப் பயன்படுத்தி உறுப்பு 21-ஐ விரிவுபடுத்துகிறது)\n3. மினர்வா மில்ஸ் வழக்கு (முகவுரை இலக்குகளை அடைய அடிப்படை உரிமைகள் மற்றும் DPSP இடையேயான சமநிலையே அடிப்படை கட்டமைப்பு என உறுதிப்படுத்துகிறது)\n4. எஸ்.ஆர். பொம்மை வழக்கு (முகவுரையில் உள்ள மதச்சார்பின்மை அடிப்படை கட்டமைப்பின் ஒரு பகுதி என அறிவிக்கிறது)",
        "options_en": ["2 -> 1 -> 3 -> 4", "1 -> 2 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "1 -> 2 -> 4 -> 3"],
        "options_ta": ["2 -> 1 -> 3 -> 4", "1 -> 2 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "1 -> 2 -> 4 -> 3"],
        "answer": "b",
        "explanation_en": "Correct Chronological Order: 1 (Kesavananda Bharati: 1973) -> 2 (Maneka Gandhi: 1978) -> 3 (Minerva Mills: 1980) -> 4 (S.R. Bommai: 1994).",
        "explanation_ta": "சரியான காலவரிசை: 1 (கேசவானந்த பாரதி: 1973) -> 2 (மேனகா காந்தி: 1978) -> 3 (மினர்வா மில்ஸ்: 1980) -> 4 (எஸ்.ஆர். பொம்மை: 1994)."
    },

    # -------------------------------------------------------------------------
    # Q7: PRE_CHRONO_007 (MODEL 3: Latest to Earliest)
    # -------------------------------------------------------------------------
    {
        "id": "PRE_CHRONO_007",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Chronology",
        "question": {
            "en": "Arrange the following Preamble-related judicial and constitutional milestones in reverse chronological order (from LATEST to EARLIEST):\n1. LIC of India Case reaffirming Preamble as an integral part of the Constitution\n2. S.R. Bommai Case establishing Secularism in Preamble as Basic Structure\n3. Enactment of 42nd Constitutional Amendment Act inserting Socialist, Secular, Integrity\n4. Berubari Union Case holding Preamble is NOT part of the Constitution",
            "ta": "முகவுரை தொடர்பான பின்வரும் நீதித்துறை மற்றும் அரசியலமைப்பு மைல்கற்களை தலைகீழ் காலவரிசையில் (மிகப் பிந்தையதிலிருந்து மிக முந்தையது வரை) அமைக்கவும்:\n1. எல்.ஐ.சி வழக்கில் முகவுரை அரசியலமைப்பின் ஒரு ஒருங்கிணைந்த பகுதி என மீண்டும் உறுதிப்படுத்தப்படுதல்\n2. எஸ்.ஆர். பொம்மை வழக்கில் முகவுரையில் உள்ள மதச்சார்பின்மை அடிப்படை கட்டமைப்பு என நிறுவப்படுதல்\n3. சமதர்ம, மதச்சார்பற்ற, ஒருமைப்பாடு ஆகியவற்றைச் சேர்க்கும் 42வது அரசியலமைப்புத் திருத்தச் சட்டம் இயற்றப்படுதல்\n4. பெருபாரி யூனியன் வழக்கில் முகவுரை அரசியலமைப்பின் பகுதி அல்ல எனத் தீர்ப்பளிக்கப்படுதல்"
        },
        "events": [
            {
                "id": "1",
                "en": "LIC of India Case reaffirming Preamble as an integral part of the Constitution (1995)",
                "ta": "எல்.ஐ.சி வழக்கில் முகவுரை அரசியலமைப்பின் ஒரு ஒருங்கிணைந்த பகுதி என மீண்டும் உறுதிப்படுத்தப்படுதல் (1995)"
            },
            {
                "id": "2",
                "en": "S.R. Bommai Case establishing Secularism in Preamble as Basic Structure (1994)",
                "ta": "எஸ்.ஆர். பொம்மை வழக்கில் முகவுரையில் உள்ள மதச்சார்பின்மை அடிப்படை கட்டமைப்பு என நிறுவப்படுதல் (1994)"
            },
            {
                "id": "3",
                "en": "Enactment of 42nd Constitutional Amendment Act inserting Socialist, Secular, Integrity (1976)",
                "ta": "சமதர்ம, மதச்சார்பற்ற, ஒருமைப்பாடு ஆகியவற்றைச் சேர்க்கும் 42வது அரசியலமைப்புத் திருத்தச் சட்டம் இயற்றப்படுதல் (1976)"
            },
            {
                "id": "4",
                "en": "Berubari Union Case holding Preamble is NOT part of the Constitution (1960)",
                "ta": "பெருபாரி யூனியன் வழக்கில் முகவுரை அரசியலமைப்பின் பகுதி அல்ல எனத் தீர்ப்பளிக்கப்படுதல் (1960)"
            }
        ],
        "options": [
            {"id": "A", "en": "4 -> 3 -> 2 -> 1", "ta": "4 -> 3 -> 2 -> 1"},
            {"id": "B", "en": "1 -> 3 -> 2 -> 4", "ta": "1 -> 3 -> 2 -> 4"},
            {"id": "C", "en": "1 -> 2 -> 3 -> 4", "ta": "1 -> 2 -> 3 -> 4"},
            {"id": "D", "en": "2 -> 1 -> 3 -> 4", "ta": "2 -> 1 -> 3 -> 4"}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "Reverse Chronology (Latest to Earliest): 1 (LIC of India: 1995) -> 2 (S.R. Bommai: 1994) -> 3 (42nd Amendment: 1976) -> 4 (Berubari Union: 1960).",
            "ta": "தலைகீழ் காலவரிசை (பிந்தையதிலிருந்து முந்தையது): 1 (எல்ஐசி வழக்கு: 1995) -> 2 (எஸ்.ஆர். பொம்மை: 1994) -> 3 (42வது திருத்தம்: 1976) -> 4 (பெருபாரி யூனியன்: 1960)."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. 4 -> 3 -> 2 -> 1 is earliest to latest, but the question specifically asks for latest to earliest.", "ta": "தவறு. 4 -> 3 -> 2 -> 1 என்பது முந்தையதிலிருந்து பிந்தையது; ஆனால் வினா பிந்தையதிலிருந்து முந்தையதைக் கேட்கிறது."},
            "B": {"en": "Incorrect. S.R. Bommai (1994) occurred after the 42nd Amendment (1976).", "ta": "தவறு. எஸ்.ஆர். பொம்மை (1994) 42வது திருத்தத்திற்கு (1976) பின்னரே நடந்தது."},
            "C": {"en": "Correct. 1 (1995) -> 2 (1994) -> 3 (1976) -> 4 (1960) accurately arranges events from latest to earliest.", "ta": "சரி. 1 (1995) -> 2 (1994) -> 3 (1976) -> 4 (1960) நிகழ்வுகளைப் பிந்தையதிலிருந்து முந்தையதாகத் துல்லியமாக அமைக்கிறது."},
            "D": {"en": "Incorrect. LIC of India (1995) is more recent than S.R. Bommai (1994).", "ta": "தவறு. எல்ஐசி வழக்கு (1995) எஸ்.ஆர். பொம்மையை (1994) விட பிந்தையது."}
        },
        "tnpsc_tip": {
            "en": "TNPSC Alert: Carefully read the question direction. 'Latest to earliest' requires reversing standard chronological flow.",
            "ta": "TNPSC எச்சரிக்கை: வினாவின் திசையைக் கவனமாகப் படிக்கவும். 'மிகப் பிந்தையதிலிருந்து மிக முந்தையது' எனில் தலைகீழ் வரிசையைத் தேர்ந்தெடுக்க வேண்டும்."
        },
        "revision_fact": {
            "en": "In LIC of India case (1995), the Supreme Court bench comprising Justices K. Ramaswamy and B.L. Hansaria reiterated that the Preamble is an integral part of the Constitution.",
            "ta": "எல்ஐசி வழக்கில் (1995), நீதிபதிகள் கே. ராமசுவாமி மற்றும் பி.எல். ஹன்சாரியா அடங்கிய அமர்வு முகவுரை அரசியலமைப்பின் ஒருங்கிணைந்த பகுதி என்பதை மீண்டும் உறுதிப்படுத்தியது."
        },
        "source_reference": [
            "M. Laxmikanth - Indian Polity",
            "NCERT Class XI - Indian Constitution at Work"
        ],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "Reverse Chronology", "Latest to Earliest", "Milestones"],
        "question_en": "Arrange the following Preamble-related judicial and constitutional milestones in reverse chronological order (from LATEST to EARLIEST):\n1. LIC of India Case reaffirming Preamble as an integral part of the Constitution\n2. S.R. Bommai Case establishing Secularism in Preamble as Basic Structure\n3. Enactment of 42nd Constitutional Amendment Act inserting Socialist, Secular, Integrity\n4. Berubari Union Case holding Preamble is NOT part of the Constitution",
        "question_ta": "முகவுரை தொடர்பான பின்வரும் நீதித்துறை மற்றும் அரசியலமைப்பு மைல்கற்களை தலைகீழ் காலவரிசையில் (மிகப் பிந்தையதிலிருந்து மிக முந்தையது வரை) அமைக்கவும்:\n1. எல்.ஐ.சி வழக்கில் முகவுரை அரசியலமைப்பின் ஒரு ஒருங்கிணைந்த பகுதி என மீண்டும் உறுதிப்படுத்தப்படுதல்\n2. எஸ்.ஆர். பொம்மை வழக்கில் முகவுரையில் உள்ள மதச்சார்பின்மை அடிப்படை கட்டமைப்பு என நிறுவப்படுதல்\n3. சமதர்ம, மதச்சார்பற்ற, ஒருமைப்பாடு ஆகியவற்றைச் சேர்க்கும் 42வது அரசியலமைப்புத் திருத்தச் சட்டம் இயற்றப்படுதல்\n4. பெருபாரி யூனியன் வழக்கில் முகவுரை அரசியலமைப்பின் பகுதி அல்ல எனத் தீர்ப்பளிக்கப்படுதல்",
        "options_en": ["4 -> 3 -> 2 -> 1", "1 -> 3 -> 2 -> 4", "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4"],
        "options_ta": ["4 -> 3 -> 2 -> 1", "1 -> 3 -> 2 -> 4", "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4"],
        "answer": "c",
        "explanation_en": "Reverse Chronology (Latest to Earliest): 1 (LIC of India: 1995) -> 2 (S.R. Bommai: 1994) -> 3 (42nd Amendment: 1976) -> 4 (Berubari Union: 1960).",
        "explanation_ta": "தலைகீழ் காலவரிசை (பிந்தையதிலிருந்து முந்தையது): 1 (எல்ஐசி வழக்கு: 1995) -> 2 (எஸ்.ஆர். பொம்மை: 1994) -> 3 (42வது திருத்தம்: 1976) -> 4 (பெருபாரி யூனியன்: 1960)."
    },

    # -------------------------------------------------------------------------
    # Q8: PRE_CHRONO_008
    # -------------------------------------------------------------------------
    {
        "id": "PRE_CHRONO_008",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Chronology",
        "question": {
            "en": "Arrange the following historic constitutional events between 1946 and 1950 in correct chronological order:\n1. Moving of the historic Objectives Resolution by Pandit Jawaharlal Nehru\n2. Constituent Assembly ratifies India's full membership in the Commonwealth of Nations\n3. Adoption and enactment of the Constitution and Preamble by the Constituent Assembly\n4. Commencement of the Constitution and establishment of India as a Sovereign Democratic Republic",
            "ta": "1946 மற்றும் 1950-க்கு இடைப்பட்ட பின்வரும் வரலாற்றுச் சிறப்புமிக்க அரசியலமைப்பு நிகழ்வுகளை சரியான காலவரிசையில் அமைக்கவும்:\n1. பண்டிட் ஜவஹர்லால் நேருவால் வரலாற்றுச் சிறப்புமிக்க குறிக்கோள் தீர்மானம் முன்மொழியப்படுதல்\n2. காமன்வெல்த் நாடுகளில் இந்தியாவின் முழு உறுப்பினர் தகுதியை அரசியலமைப்பு நிர்ணய அவை அங்கீகரித்தல்\n3. அரசியலமைப்பு மற்றும் முகவுரை அரசியலமைப்பு நிர்ணய அவையால் ஏற்றுக்கொள்ளப்பட்டு இயற்றப்படுதல்\n4. அரசியலமைப்பு நடைமுறைக்கு வந்து இந்தியா இறையாண்மை ஜனநாயகக் குடியரசாக மலருதல்"
        },
        "events": [
            {
                "id": "1",
                "en": "Moving of the historic Objectives Resolution by Pandit Jawaharlal Nehru",
                "ta": "பண்டிட் ஜவஹர்லால் நேருவால் வரலாற்றுச் சிறப்புமிக்க குறிக்கோள் தீர்மானம் முன்மொழியப்படுதல்"
            },
            {
                "id": "2",
                "en": "Constituent Assembly ratifies India's full membership in the Commonwealth of Nations",
                "ta": "காமன்வெல்த் நாடுகளில் இந்தியாவின் முழு உறுப்பினர் தகுதியை அரசியலமைப்பு நிர்ணய அவை அங்கீகரித்தல்"
            },
            {
                "id": "3",
                "en": "Adoption and enactment of the Constitution and Preamble by the Constituent Assembly",
                "ta": "அரசியலமைப்பு மற்றும் முகவுரை அரசியலமைப்பு நிர்ணய அவையால் ஏற்றுக்கொள்ளப்பட்டு இயற்றப்படுதல்"
            },
            {
                "id": "4",
                "en": "Commencement of the Constitution and establishment of India as a Sovereign Democratic Republic",
                "ta": "அரசியலமைப்பு நடைமுறைக்கு வந்து இந்தியா இறையாண்மை ஜனநாயகக் குடியரசாக மலருதல்"
            }
        ],
        "options": [
            {"id": "A", "en": "1 -> 3 -> 2 -> 4", "ta": "1 -> 3 -> 2 -> 4"},
            {"id": "B", "en": "2 -> 1 -> 3 -> 4", "ta": "2 -> 1 -> 3 -> 4"},
            {"id": "C", "en": "1 -> 2 -> 4 -> 3", "ta": "1 -> 2 -> 4 -> 3"},
            {"id": "D", "en": "1 -> 2 -> 3 -> 4", "ta": "1 -> 2 -> 3 -> 4"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "Chronological Sequence: 1 (Objectives Resolution moved: Dec 13, 1946) -> 2 (Commonwealth membership ratified: May 1949) -> 3 (Constitution adopted: Nov 26, 1949) -> 4 (Constitution commenced: Jan 26, 1950).",
            "ta": "சரியான காலவரிசை: 1 (குறிக்கோள் தீர்மானம்: டிசம்பர் 13, 1946) -> 2 (காமன்வெல்த் ஏற்பு: மே 1949) -> 3 (அரசியலமைப்பு ஏற்பு: நவம்பர் 26, 1949) -> 4 (அரசியலமைப்பு அமல்: ஜனவரி 26, 1950)."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Commonwealth membership ratification was in May 1949 (2), before Constitution adoption in Nov 1949 (3).", "ta": "தவறு. காமன்வெல்த் உறுப்பினர் ஏற்பு மே 1949-ல் (2) நடந்தது, இது நவம்பர் 1949 அரசியலமைப்பு ஏற்பிற்கு (3) முந்தையது."},
            "B": {"en": "Incorrect. Objectives Resolution was moved in Dec 1946 (1), long before 1949.", "ta": "தவறு. குறிக்கோள் தீர்மானம் டிசம்பர் 1946-ல் (1) முன்மொழியப்பட்டது."},
            "C": {"en": "Incorrect. Constitution adoption (Nov 26, 1949) preceded its commencement (Jan 26, 1950).", "ta": "தவறு. அரசியலமைப்பு ஏற்பு (நவம்பர் 26, 1949) நடைமுறைக்கு வந்த நாளுக்கு (ஜனவரி 26, 1950) முந்தையது."},
            "D": {"en": "Correct. 1 (Dec 1946) -> 2 (May 1949) -> 3 (Nov 1949) -> 4 (Jan 1950) represents the accurate historical timeline.", "ta": "சரி. 1 (டிசம்பர் 1946) -> 2 (மே 1949) -> 3 (நவம்பர் 1949) -> 4 (ஜனவரி 1950) துல்லியமான வரலாற்று காலவரிசை."}
        },
        "tnpsc_tip": {
            "en": "TNPSC Concept: Nehru clarified in May 1949 that Commonwealth membership does NOT compromise India's Sovereign Republic status declared in the Preamble.",
            "ta": "TNPSC கருத்து: காமன்வெல்த் உறுப்பினர் தகுதி முகவுரையில் அறிவிக்கப்பட்டுள்ள இந்தியாவின் இறையாண்மையை எந்த வகையிலும் பாதிக்காது என நேரு மே 1949-ல் தெளிவுபடுத்தினார்."
        },
        "revision_fact": {
            "en": "On 26 November 1949, articles relating to Citizenship, Elections, and Provisional Parliament (Articles 5, 6, 7, 8, 9, 60, 324, etc.) came into force immediately; the remaining Constitution and Preamble commenced on 26 January 1950.",
            "ta": "26 நவம்பர் 1949 அன்று குடியுரிமை, தேர்தல்கள் தொடர்பான விதிகள் உடனடியாக அமலுக்கு வந்தன; முகவுரை உட்பட எஞ்சிய அரசியலமைப்பு 26 ஜனவரி 1950 அன்று நடைமுறைக்கு வந்தது."
        },
        "source_reference": [
            "M. Laxmikanth - Indian Polity (Preamble & Making of Constitution)",
            "Constituent Assembly Debates (Vol. VIII & XI)"
        ],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "Foundational Timeline", "Commonwealth", "Republic Day"],
        "question_en": "Arrange the following historic constitutional events between 1946 and 1950 in correct chronological order:\n1. Moving of the historic Objectives Resolution by Pandit Jawaharlal Nehru\n2. Constituent Assembly ratifies India's full membership in the Commonwealth of Nations\n3. Adoption and enactment of the Constitution and Preamble by the Constituent Assembly\n4. Commencement of the Constitution and establishment of India as a Sovereign Democratic Republic",
        "question_ta": "1946 மற்றும் 1950-க்கு இடைப்பட்ட பின்வரும் வரலாற்றுச் சிறப்புமிக்க அரசியலமைப்பு நிகழ்வுகளை சரியான காலவரிசையில் அமைக்கவும்:\n1. பண்டிட் ஜவஹர்லால் நேருவால் வரலாற்றுச் சிறப்புமிக்க குறிக்கோள் தீர்மானம் முன்மொழியப்படுதல்\n2. காமன்வெல்த் நாடுகளில் இந்தியாவின் முழு உறுப்பினர் தகுதியை அரசியலமைப்பு நிர்ணய அவை அங்கீகரித்தல்\n3. அரசியலமைப்பு மற்றும் முகவுரை அரசியலமைப்பு நிர்ணய அவையால் ஏற்றுக்கொள்ளப்பட்டு இயற்றப்படுதல்\n4. அரசியலமைப்பு நடைமுறைக்கு வந்து இந்தியா இறையாண்மை ஜனநாயகக் குடியரசாக மலருதல்",
        "options_en": ["1 -> 3 -> 2 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 2 -> 4 -> 3", "1 -> 2 -> 3 -> 4"],
        "options_ta": ["1 -> 3 -> 2 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 2 -> 4 -> 3", "1 -> 2 -> 3 -> 4"],
        "answer": "d",
        "explanation_en": "Chronological Sequence: 1 (Objectives Resolution moved: Dec 13, 1946) -> 2 (Commonwealth membership ratified: May 1949) -> 3 (Constitution adopted: Nov 26, 1949) -> 4 (Constitution commenced: Jan 26, 1950).",
        "explanation_ta": "சரியான காலவரிசை: 1 (குறிக்கோள் தீர்மானம்: டிசம்பர் 13, 1946) -> 2 (காமன்வெல்த் ஏற்பு: மே 1949) -> 3 (அரசியலமைப்பு ஏற்பு: நவம்பர் 26, 1949) -> 4 (அரசியலமைப்பு அமல்: ஜனவரி 26, 1950)."
    },

    # -------------------------------------------------------------------------
    # Q9: PRE_CHRONO_009
    # -------------------------------------------------------------------------
    {
        "id": "PRE_CHRONO_009",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Chronology",
        "question": {
            "en": "Arrange the following developments regarding constitutional amendments affecting the Preamble in correct chronological order:\n1. Kesavananda Bharati verdict establishing that Preamble is amendable under Article 368 subject to Basic Structure\n2. Swaran Singh Committee appointed to recommend constitutional changes including Preamble amendments\n3. 42nd Constitutional Amendment Act passed by Parliament amending the Preamble\n4. 44th Constitutional Amendment Act enacted retaining the 42nd Amendment changes made to the Preamble",
            "ta": "முகவுரையைப் பாதித்த அரசியலமைப்புத் திருத்தங்கள் தொடர்பான பின்வரும் முன்னேற்றங்களை சரியான காலவரிசையில் அமைக்கவும்:\n1. அடிப்படை கட்டமைப்புக்கு உட்பட்டு உறுப்பு 368-ன் கீழ் முகவுரையைத் திருத்தலாம் என கேசவானந்த பாரதி தீர்ப்பளித்தல்\n2. முகவுரைத் திருத்தங்கள் உட்பட அரசியலமைப்பு மாற்றங்களைப் பரிந்துரைக்க ஸ்வரன் சிங் குழு அமைக்கப்படுதல்\n3. முகவுரையைத் திருத்தி நாடாளுமன்றத்தால் 42வது அரசியலமைப்புத் திருத்தச் சட்டம் நிறைவேற்றப்படுதல்\n4. முகவுரையில் செய்யப்பட்ட 42வது திருத்த மாற்றங்களைத் தக்கவைத்து 44வது அரசியலமைப்புத் திருத்தச் சட்டம் இயற்றப்படுதல்"
        },
        "events": [
            {
                "id": "1",
                "en": "Kesavananda Bharati verdict establishing that Preamble is amendable under Article 368 subject to Basic Structure",
                "ta": "அடிப்படை கட்டமைப்புக்கு உட்பட்டு உறுப்பு 368-ன் கீழ் முகவுரையைத் திருத்தலாம் என கேசவானந்த பாரதி தீர்ப்பளித்தல்"
            },
            {
                "id": "2",
                "en": "Swaran Singh Committee appointed to recommend constitutional changes including Preamble amendments",
                "ta": "முகவுரைத் திருத்தங்கள் உட்பட அரசியலமைப்பு மாற்றங்களைப் பரிந்துரைக்க ஸ்வரன் சிங் குழு அமைக்கப்படுதல்"
            },
            {
                "id": "3",
                "en": "42nd Constitutional Amendment Act passed by Parliament amending the Preamble",
                "ta": "முகவுரையைத் திருத்தி நாடாளுமன்றத்தால் 42வது அரசியலமைப்புத் திருத்தச் சட்டம் நிறைவேற்றப்படுதல்"
            },
            {
                "id": "4",
                "en": "44th Constitutional Amendment Act enacted retaining the 42nd Amendment changes made to the Preamble",
                "ta": "முகவுரையில் செய்யப்பட்ட 42வது திருத்த மாற்றங்களைத் தக்கவைத்து 44வது அரசியலமைப்புத் திருத்தச் சட்டம் இயற்றப்படுதல்"
            }
        ],
        "options": [
            {"id": "A", "en": "1 -> 2 -> 3 -> 4", "ta": "1 -> 2 -> 3 -> 4"},
            {"id": "B", "en": "2 -> 1 -> 3 -> 4", "ta": "2 -> 1 -> 3 -> 4"},
            {"id": "C", "en": "1 -> 3 -> 2 -> 4", "ta": "1 -> 3 -> 2 -> 4"},
            {"id": "D", "en": "1 -> 2 -> 4 -> 3", "ta": "1 -> 2 -> 4 -> 3"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Chronological Sequence: 1 (Kesavananda Bharati: 1973) -> 2 (Swaran Singh Committee: Early 1976) -> 3 (42nd Amendment Act: Late 1976) -> 4 (44th Amendment Act: 1978).",
            "ta": "சரியான காலவரிசை: 1 (கேசவானந்த பாரதி: 1973) -> 2 (ஸ்வரன் சிங் குழு: தொடக்க 1976) -> 3 (42வது திருத்தச் சட்டம்: பிற்பகுதி 1976) -> 4 (44வது திருத்தச் சட்டம்: 1978)."
        },
        "why_not_others": {
            "A": {"en": "Correct. 1 (1973) -> 2 (1976) -> 3 (1976) -> 4 (1978) precisely tracks the amendment trajectory.", "ta": "சரி. 1 (1973) -> 2 (1976) -> 3 (1976) -> 4 (1978) திருத்தப் பாதையைத் துல்லியமாகப் பின்பற்றுகிறது."},
            "B": {"en": "Incorrect. Kesavananda Bharati (1973) came before the Swaran Singh Committee (1976).", "ta": "தவறு. கேசவானந்த பாரதி (1973) ஸ்வரன் சிங் குழுவிற்கு (1976) முந்தையது."},
            "C": {"en": "Incorrect. Swaran Singh Committee (2) recommendations led directly to the 42nd Amendment (3).", "ta": "தவறு. ஸ்வரன் சிங் குழுவின் (2) பரிந்துரைகளே 42வது திருத்தத்திற்கு (3) வழிவகுத்தன."},
            "D": {"en": "Incorrect. 44th Amendment was enacted in 1978 (4), after the 42nd Amendment in 1976 (3).", "ta": "தவறு. 44வது திருத்தம் 1978-ல் (4) இயற்றப்பட்டது, இது 1976 42வது திருத்தத்திற்குப் (3) பின்னராகும்."}
        },
        "tnpsc_tip": {
            "en": "TNPSC Nuance: The Janata Party Government passed the 44th Amendment (1978) to nullify several emergency distortions, but chose NOT to alter the words 'Socialist', 'Secular', and 'Integrity' in the Preamble.",
            "ta": "TNPSC நுணுக்கம்: 44வது திருத்தத்தின் (1978) மூலம் நெருக்கடி நிலை மாற்றங்கள் பல ரத்து செய்யப்பட்ட போதிலும், முகவுரையில் சேர்க்கப்பட்ட 'சமதர்ம', 'மதச்சார்பற்ற', 'ஒருமைப்பாடு' சொற்கள் அப்படியே தக்கவைக்கப்பட்டன."
        },
        "revision_fact": {
            "en": "The Swaran Singh Committee was appointed by the Congress Party President D.K. Barooah in 1976 to study constitutional changes.",
            "ta": "அரசியலமைப்பு மாற்றங்களை ஆராய 1976-ல் காங்கிரஸ் தலைவர் டி.கே. பரூவாவால் ஸ்வரன் சிங் குழு அமைக்கப்பட்டது."
        },
        "source_reference": [
            "M. Laxmikanth - Indian Polity",
            "DD Basu - Introduction to the Constitution of India"
        ],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "42nd Amendment", "44th Amendment", "Swaran Singh Committee"],
        "question_en": "Arrange the following developments regarding constitutional amendments affecting the Preamble in correct chronological order:\n1. Kesavananda Bharati verdict establishing that Preamble is amendable under Article 368 subject to Basic Structure\n2. Swaran Singh Committee appointed to recommend constitutional changes including Preamble amendments\n3. 42nd Constitutional Amendment Act passed by Parliament amending the Preamble\n4. 44th Constitutional Amendment Act enacted retaining the 42nd Amendment changes made to the Preamble",
        "question_ta": "முகவுரையைப் பாதித்த அரசியலமைப்புத் திருத்தங்கள் தொடர்பான பின்வரும் முன்னேற்றங்களை சரியான காலவரிசையில் அமைக்கவும்:\n1. அடிப்படை கட்டமைப்புக்கு உட்பட்டு உறுப்பு 368-ன் கீழ் முகவுரையைத் திருத்தலாம் என கேசவானந்த பாரதி தீர்ப்பளித்தல்\n2. முகவுரைத் திருத்தங்கள் உட்பட அரசியலமைப்பு மாற்றங்களைப் பரிந்துரைக்க ஸ்வரன் சிங் குழு அமைக்கப்படுதல்\n3. முகவுரையைத் திருத்தி நாடாளுமன்றத்தால் 42வது அரசியலமைப்புத் திருத்தச் சட்டம் நிறைவேற்றப்படுதல்\n4. முகவுரையில் செய்யப்பட்ட 42வது திருத்த மாற்றங்களைத் தக்கவைத்து 44வது அரசியலமைப்புத் திருத்தச் சட்டம் இயற்றப்படுதல்",
        "options_en": ["1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "1 -> 2 -> 4 -> 3"],
        "options_ta": ["1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "1 -> 2 -> 4 -> 3"],
        "answer": "a",
        "explanation_en": "Chronological Sequence: 1 (Kesavananda Bharati: 1973) -> 2 (Swaran Singh Committee: Early 1976) -> 3 (42nd Amendment Act: Late 1976) -> 4 (44th Amendment Act: 1978).",
        "explanation_ta": "சரியான காலவரிசை: 1 (கேசவானந்த பாரதி: 1973) -> 2 (ஸ்வரன் சிங் குழு: தொடக்க 1976) -> 3 (42வது திருத்தச் சட்டம்: பிற்பகுதி 1976) -> 4 (44வது திருத்தச் சட்டம்: 1978)."
    },

    # -------------------------------------------------------------------------
    # Q10: PRE_CHRONO_010
    # -------------------------------------------------------------------------
    {
        "id": "PRE_CHRONO_010",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Chronology",
        "question": {
            "en": "Arrange the three dimensions of 'JUSTICE' in the exact sequential order as they are enumerated in the Preamble of India:\n1. Social Justice\n2. Economic Justice\n3. Political Justice\n4. Liberty of Thought, Expression, Belief, Faith, and Worship (Subsequent Objective)",
            "ta": "இந்திய முகவுரையில் குறிப்பிடப்பட்டுள்ள 'நீதியின்' மூன்று பரிமாணங்களை சரியான உரை வரிசையில் அமைக்கவும்:\n1. சமூக நீதி (Social Justice)\n2. பொருளாதார நீதி (Economic Justice)\n3. அரசியல் நீதி (Political Justice)\n4. சிந்தனை, வெளிப்பாடு, நம்பிக்கை, சமயம் மற்றும் வழிபாட்டுச் சுதந்திரம் (அடுத்த இலக்கு)"
        },
        "events": [
            {
                "id": "1",
                "en": "Social Justice",
                "ta": "சமூக நீதி"
            },
            {
                "id": "2",
                "en": "Economic Justice",
                "ta": "பொருளாதார நீதி"
            },
            {
                "id": "3",
                "en": "Political Justice",
                "ta": "அரசியல் நீதி"
            },
            {
                "id": "4",
                "en": "Liberty of Thought, Expression, Belief, Faith, and Worship (Subsequent Objective)",
                "ta": "சிந்தனை, வெளிப்பாடு, நம்பிக்கை, சமயம் மற்றும் வழிபாட்டுச் சுதந்திரம் (அடுத்த இலக்கு)"
            }
        ],
        "options": [
            {"id": "A", "en": "2 -> 1 -> 3 -> 4", "ta": "2 -> 1 -> 3 -> 4"},
            {"id": "B", "en": "1 -> 2 -> 3 -> 4", "ta": "1 -> 2 -> 3 -> 4"},
            {"id": "C", "en": "1 -> 3 -> 2 -> 4", "ta": "1 -> 3 -> 2 -> 4"},
            {"id": "D", "en": "3 -> 1 -> 2 -> 4", "ta": "3 -> 1 -> 2 -> 4"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "Textual Sequence of Justice in Preamble: 'JUSTICE, social, economic and political;'. Hence, 1 (Social) -> 2 (Economic) -> 3 (Political) -> followed by Liberty (4).",
            "ta": "முகவுரையில் நீதியின் உரை வரிசை: 'நீதி, சமூக, பொருளாதார மற்றும் அரசியல்;'. எனவே, 1 (சமூக) -> 2 (பொருளாதார) -> 3 (அரசியல்) -> சுதந்திரம் (4)."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Social Justice comes before Economic Justice.", "ta": "தவறு. பொருளாதார நீதிக்கு முன்பாக சமூக நீதி வருகிறது."},
            "B": {"en": "Correct. 1 (Social) -> 2 (Economic) -> 3 (Political) -> 4 (Liberty) matches the exact phrasing.", "ta": "சரி. 1 (சமூக) -> 2 (பொருளாதார) -> 3 (அரசியல்) -> 4 (சுதந்திரம்) துல்லியமான உரை வரிசையாகும்."},
            "C": {"en": "Incorrect. Economic Justice precedes Political Justice in the text.", "ta": "தவறு. உரையில் அரசியல் நீதிக்கு முன்பாக பொருளாதார நீதி வருகிறது."},
            "D": {"en": "Incorrect. Political Justice is the third dimension, not the first.", "ta": "தவறு. அரசியல் நீதி மூன்றாவது பரிமாணமாகும், முதலாவது அல்ல."}
        },
        "tnpsc_tip": {
            "en": "TNPSC Mnemonic: S-E-P (Social, Economic, Political Justice). Always remember the order.",
            "ta": "TNPSC நினைவூட்டல்: S-E-P (சமூக, பொருளாதார, அரசியல் நீதி). எப்போதும் இந்த வரிசையை நினைவில் கொள்ளவும்."
        },
        "revision_fact": {
            "en": "Social and Economic Justice combined form 'Distributive Justice', as held by the Supreme Court.",
            "ta": "சமூக மற்றும் பொருளாதார நீதி இரண்டும் இணைந்து 'பகிர்ந்தளிக்கும் நீதி' (Distributive Justice) என அழைக்கப்படுகிறது என உச்ச நீதிமன்றம் கூறியுள்ளது."
        },
        "source_reference": [
            "Text of the Constitution of India (Preamble)",
            "M. Laxmikanth - Indian Polity"
        ],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "Justice", "Sequence", "Social Economic Political"],
        "question_en": "Arrange the three dimensions of 'JUSTICE' in the exact sequential order as they are enumerated in the Preamble of India:\n1. Social Justice\n2. Economic Justice\n3. Political Justice\n4. Liberty of Thought, Expression, Belief, Faith, and Worship (Subsequent Objective)",
        "question_ta": "இந்திய முகவுரையில் குறிப்பிடப்பட்டுள்ள 'நீதியின்' மூன்று பரிமாணங்களை சரியான உரை வரிசையில் அமைக்கவும்:\n1. சமூக நீதி (Social Justice)\n2. பொருளாதார நீதி (Economic Justice)\n3. அரசியல் நீதி (Political Justice)\n4. சிந்தனை, வெளிப்பாடு, நம்பிக்கை, சமயம் மற்றும் வழிபாட்டுச் சுதந்திரம் (அடுத்த இலக்கு)",
        "options_en": ["2 -> 1 -> 3 -> 4", "1 -> 2 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "3 -> 1 -> 2 -> 4"],
        "options_ta": ["2 -> 1 -> 3 -> 4", "1 -> 2 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "3 -> 1 -> 2 -> 4"],
        "answer": "b",
        "explanation_en": "Textual Sequence of Justice in Preamble: 'JUSTICE, social, economic and political;'. Hence, 1 (Social) -> 2 (Economic) -> 3 (Political) -> followed by Liberty (4).",
        "explanation_ta": "முகவுரையில் நீதியின் உரை வரிசை: 'நீதி, சமூக, பொருளாதார மற்றும் அரசியல்;'. எனவே, 1 (சமூக) -> 2 (பொருளாதார) -> 3 (அரசியல்) -> சுதந்திரம் (4)."
    },

    # -------------------------------------------------------------------------
    # Q11: PRE_CHRONO_011
    # -------------------------------------------------------------------------
    {
        "id": "PRE_CHRONO_011",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Chronology",
        "question": {
            "en": "Arrange the five aspects of 'LIBERTY' in the exact sequential order as they appear in the Preamble:\n1. Liberty of Thought\n2. Liberty of Expression\n3. Liberty of Belief\n4. Liberty of Faith and Worship",
            "ta": "முகவுரையில் இடம்பெற்றுள்ளவாறு 'சுதந்திரத்தின்' ஐந்து அம்சங்களை சரியான உரை வரிசையில் அமைக்கவும்:\n1. சிந்தனை சுதந்திரம் (Thought)\n2. கருத்து வெளிப்பாட்டுச் சுதந்திரம் (Expression)\n3. நம்பிக்கை சுதந்திரம் (Belief)\n4. சமயம் மற்றும் வழிபாட்டுச் சுதந்திரம் (Faith and Worship)"
        },
        "events": [
            {
                "id": "1",
                "en": "Liberty of Thought",
                "ta": "சிந்தனை சுதந்திரம்"
            },
            {
                "id": "2",
                "en": "Liberty of Expression",
                "ta": "கருத்து வெளிப்பாட்டுச் சுதந்திரம்"
            },
            {
                "id": "3",
                "en": "Liberty of Belief",
                "ta": "நம்பிக்கை சுதந்திரம்"
            },
            {
                "id": "4",
                "en": "Liberty of Faith and Worship",
                "ta": "சமயம் மற்றும் வழிபாட்டுச் சுதந்திரம்"
            }
        ],
        "options": [
            {"id": "A", "en": "2 -> 1 -> 3 -> 4", "ta": "2 -> 1 -> 3 -> 4"},
            {"id": "B", "en": "1 -> 3 -> 2 -> 4", "ta": "1 -> 3 -> 2 -> 4"},
            {"id": "C", "en": "1 -> 2 -> 3 -> 4", "ta": "1 -> 2 -> 3 -> 4"},
            {"id": "D", "en": "1 -> 2 -> 4 -> 3", "ta": "1 -> 2 -> 4 -> 3"}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "Textual Sequence of Liberty in Preamble: 'LIBERTY of thought, expression, belief, faith and worship;'. Hence, 1 -> 2 -> 3 -> 4.",
            "ta": "முகவுரையில் சுதந்திரத்தின் உரை வரிசை: 'சிந்தனை, வெளிப்பாடு, நம்பிக்கை, சமயம் மற்றும் வழிபாட்டுச் சுதந்திரம்;'. எனவே, 1 -> 2 -> 3 -> 4."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Thought comes before Expression.", "ta": "தவறு. வெளிப்பாட்டிற்கு முன்பாக சிந்தனை வருகிறது."},
            "B": {"en": "Incorrect. Expression precedes Belief in the text.", "ta": "தவறு. உரையில் நம்பிக்கைக்கு முன்பாக கருத்து வெளிப்பாடு வருகிறது."},
            "C": {"en": "Correct. 1 (Thought) -> 2 (Expression) -> 3 (Belief) -> 4 (Faith and Worship) accurately represents the constitutional text.", "ta": "சரி. 1 (சிந்தனை) -> 2 (வெளிப்பாடு) -> 3 (நம்பிக்கை) -> 4 (சமயம் மற்றும் வழிபாடு) அரசியலமைப்பு உரையைத் துல்லியமாகக் காட்டுகிறது."},
            "D": {"en": "Incorrect. Belief precedes Faith and Worship.", "ta": "தவறு. சமயம் மற்றும் வழிபாட்டிற்கு முன்பாக நம்பிக்கை வருகிறது."}
        },
        "tnpsc_tip": {
            "en": "TNPSC Mnemonic: T-E-B-F-W (Thought, Expression, Belief, Faith, Worship).",
            "ta": "TNPSC நினைவூட்டல்: T-E-B-F-W (சிந்தனை, வெளிப்பாடு, நம்பிக்கை, சமயம், வழிபாடு)."
        },
        "revision_fact": {
            "en": "Liberty in the Preamble is secured through Fundamental Rights under Articles 19 (Freedom of Speech and Expression) and Articles 25-28 (Freedom of Religion).",
            "ta": "முகவுரையில் உள்ள சுதந்திரம் உறுப்பு 19 (பேச்சு மற்றும் கருத்து சுதந்திரம்) மற்றும் உறுப்புகள் 25-28 (மத சுதந்திரம்) ஆகிய அடிப்படை உரிமைகள் மூலம் உறுதி செய்யப்படுகிறது."
        },
        "source_reference": [
            "Text of the Constitution of India (Preamble)",
            "M. Laxmikanth - Indian Polity"
        ],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "Liberty", "Sequence", "Thought Expression Belief Faith Worship"],
        "question_en": "Arrange the five aspects of 'LIBERTY' in the exact sequential order as they appear in the Preamble:\n1. Liberty of Thought\n2. Liberty of Expression\n3. Liberty of Belief\n4. Liberty of Faith and Worship",
        "question_ta": "முகவுரையில் இடம்பெற்றுள்ளவாறு 'சுதந்திரத்தின்' ஐந்து அம்சங்களை சரியான உரை வரிசையில் அமைக்கவும்:\n1. சிந்தனை சுதந்திரம் (Thought)\n2. கருத்து வெளிப்பாட்டுச் சுதந்திரம் (Expression)\n3. நம்பிக்கை சுதந்திரம் (Belief)\n4. சமயம் மற்றும் வழிபாட்டுச் சுதந்திரம் (Faith and Worship)",
        "options_en": ["2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "1 -> 2 -> 3 -> 4", "1 -> 2 -> 4 -> 3"],
        "options_ta": ["2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "1 -> 2 -> 3 -> 4", "1 -> 2 -> 4 -> 3"],
        "answer": "c",
        "explanation_en": "Textual Sequence of Liberty in Preamble: 'LIBERTY of thought, expression, belief, faith and worship;'. Hence, 1 -> 2 -> 3 -> 4.",
        "explanation_ta": "முகவுரையில் சுதந்திரத்தின் உரை வரிசை: 'சிந்தனை, வெளிப்பாடு, நம்பிக்கை, சமயம் மற்றும் வழிபாட்டுச் சுதந்திரம்;'. எனவே, 1 -> 2 -> 3 -> 4."
    },

    # -------------------------------------------------------------------------
    # Q12: PRE_CHRONO_012
    # -------------------------------------------------------------------------
    {
        "id": "PRE_CHRONO_012",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Chronology",
        "question": {
            "en": "Arrange the following judicial and legislative milestones regarding the concept of 'Secularism' in India's constitutional history in correct chronological order:\n1. Supreme Court holds Preamble is not part of Constitution, though general spirit guides ambiguity (Berubari)\n2. Supreme Court rules that secular character of Constitution is part of Basic Structure (Kesavananda Bharati)\n3. Word 'SECULAR' is explicitly inserted into the Preamble by 42nd Constitutional Amendment Act\n4. Supreme Court rules that state governments pursuing anti-secular policies can be dismissed under Article 356 (S.R. Bommai)",
            "ta": "இந்திய அரசியலமைப்பு வரலாற்றில் 'மதச்சார்பின்மை' என்ற கருத்து தொடர்பான பின்வரும் நீதித்துறை மற்றும் சட்டமியற்றல் மைல்கற்களை சரியான காலவரிசையில் அமைக்கவும்:\n1. தெளிவற்ற நிலையில் பொது உணர்வு வழிகாட்டினாலும், முகவுரை அரசியலமைப்பின் பகுதி அல்ல என உச்ச நீதிமன்றம் கூறுதல் (பெருபாரி)\n2. அரசியலமைப்பின் மதச்சார்பற்ற தன்மை அடிப்படை கட்டமைப்பின் ஒரு பகுதி என உச்ச நீதிமன்றம் தீர்ப்பளித்தல் (கேசவானந்த பாரதி)\n3. 42வது அரசியலமைப்புத் திருத்தச் சட்டத்தின் மூலம் 'மதச்சார்பற்ற' என்ற சொல் முகவுரையில் வெளிப்படையாகச் சேர்க்கப்படுதல்\n4. மதச்சார்பற்ற கொள்கைகளுக்கு எதிராகச் செயல்படும் மாநில அரசுகளை உறுப்பு 356-ன் கீழ் கலைக்கலாம் என உச்ச நீதிமன்றம் தீர்ப்பளித்தல் (எஸ்.ஆர். பொம்மை)"
        },
        "events": [
            {
                "id": "1",
                "en": "Supreme Court holds Preamble is not part of Constitution, though general spirit guides ambiguity (Berubari)",
                "ta": "தெளிவற்ற நிலையில் பொது உணர்வு வழிகாட்டினாலும், முகவுரை அரசியலமைப்பின் பகுதி அல்ல என உச்ச நீதிமன்றம் கூறுதல் (பெருபாரி)"
            },
            {
                "id": "2",
                "en": "Supreme Court rules that secular character of Constitution is part of Basic Structure (Kesavananda Bharati)",
                "ta": "அரசியலமைப்பின் மதச்சார்பற்ற தன்மை அடிப்படை கட்டமைப்பின் ஒரு பகுதி என உச்ச நீதிமன்றம் தீர்ப்பளித்தல் (கேசவானந்த பாரதி)"
            },
            {
                "id": "3",
                "en": "Word 'SECULAR' is explicitly inserted into the Preamble by 42nd Constitutional Amendment Act",
                "ta": "42வது அரசியலமைப்புத் திருத்தச் சட்டத்தின் மூலம் 'மதச்சார்பற்ற' என்ற சொல் முகவுரையில் வெளிப்படையாகச் சேர்க்கப்படுதல்"
            },
            {
                "id": "4",
                "en": "Supreme Court rules that state governments pursuing anti-secular policies can be dismissed under Article 356 (S.R. Bommai)",
                "ta": "மதச்சார்பற்ற கொள்கைகளுக்கு எதிராகச் செயல்படும் மாநில அரசுகளை உறுப்பு 356-ன் கீழ் கலைக்கலாம் என உச்ச நீதிமன்றம் தீர்ப்பளித்தல் (எஸ்.ஆர். பொம்மை)"
            }
        ],
        "options": [
            {"id": "A", "en": "2 -> 1 -> 3 -> 4", "ta": "2 -> 1 -> 3 -> 4"},
            {"id": "B", "en": "1 -> 3 -> 2 -> 4", "ta": "1 -> 3 -> 2 -> 4"},
            {"id": "C", "en": "1 -> 2 -> 4 -> 3", "ta": "1 -> 2 -> 4 -> 3"},
            {"id": "D", "en": "1 -> 2 -> 3 -> 4", "ta": "1 -> 2 -> 3 -> 4"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "Chronological Sequence: 1 (Berubari Union: 1960) -> 2 (Kesavananda Bharati secularism ruling: 1973) -> 3 (42nd Amendment insertion: 1976) -> 4 (S.R. Bommai secularism ruling: 1994).",
            "ta": "சரியான காலவரிசை: 1 (பெருபாரி யூனியன்: 1960) -> 2 (கேசவானந்த பாரதி மதச்சார்பின்மை தீர்ப்பு: 1973) -> 3 (42வது திருத்தச் சேர்க்கை: 1976) -> 4 (எஸ்.ஆர். பொம்மை தீர்ப்பு: 1994)."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Berubari (1960) was decided before Kesavananda Bharati (1973).", "ta": "தவறு. பெருபாரி (1960) கேசவானந்த பாரதிக்கு (1973) முந்தையது."},
            "B": {"en": "Incorrect. Kesavananda Bharati (1973) recognized secularism as Basic Structure before the word was added to the Preamble in 1976 (3).", "ta": "தவறு. 1976-ல் முகவுரையில் சொல் சேர்க்கப்படுவதற்கு முன்பே கேசவானந்த பாரதி (1973) மதச்சார்பின்மையை அடிப்படை அமைப்பாக அங்கீகரித்தது."},
            "C": {"en": "Incorrect. 42nd Amendment occurred in 1976 (3), long before S.R. Bommai in 1994 (4).", "ta": "தவறு. 42வது திருத்தம் 1976-ல் (3) நடந்தது, இது 1994 எஸ்.ஆர். பொம்மைக்கு (4) முந்தையது."},
            "D": {"en": "Correct. 1 (1960) -> 2 (1973) -> 3 (1976) -> 4 (1994) follows the complete legal development of Indian Secularism.", "ta": "சரி. 1 (1960) -> 2 (1973) -> 3 (1976) -> 4 (1994) இந்திய மதச்சார்பின்மையின் முழு சட்ட வளர்ச்சியைப் பின்பற்றுகிறது."}
        },
        "tnpsc_tip": {
            "en": "TNPSC Key Concept: Indian Secularism is 'positive secularism' (Sarva Dharma Sambhava - equal respect to all religions), not anti-religious or strict wall of separation.",
            "ta": "TNPSC முக்கிய கருத்து: இந்திய மதச்சார்பின்மை என்பது 'நேர்மறை மதச்சார்பின்மை' (சர்வ தர்ம சம்பவ - அனைத்து மதங்களுக்கும் சமமான மரியாதை), இது மேற்கத்திய மத எதிர்ப்பு அல்ல."
        },
        "revision_fact": {
            "en": "Even before the 42nd Amendment of 1976, Articles 25 to 28 of the original Constitution guaranteed Freedom of Religion as Fundamental Rights.",
            "ta": "1976-ன் 42வது திருத்தத்திற்கு முன்பே, அசல் அரசியலமைப்பின் 25 முதல் 28 வரையிலான உறுப்புகள் மத சுதந்திரத்தை அடிப்படை உரிமைகளாக உத்தரவாதம் செய்திருந்தன."
        },
        "source_reference": [
            "M. Laxmikanth - Indian Polity",
            "NCERT Class XI - Indian Constitution at Work"
        ],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "Secularism", "Chronology", "SR Bommai", "42nd Amendment"],
        "question_en": "Arrange the following judicial and legislative milestones regarding the concept of 'Secularism' in India's constitutional history in correct chronological order:\n1. Supreme Court holds Preamble is not part of Constitution, though general spirit guides ambiguity (Berubari)\n2. Supreme Court rules that secular character of Constitution is part of Basic Structure (Kesavananda Bharati)\n3. Word 'SECULAR' is explicitly inserted into the Preamble by 42nd Constitutional Amendment Act\n4. Supreme Court rules that state governments pursuing anti-secular policies can be dismissed under Article 356 (S.R. Bommai)",
        "question_ta": "இந்திய அரசியலமைப்பு வரலாற்றில் 'மதச்சார்பின்மை' என்ற கருத்து தொடர்பான பின்வரும் நீதித்துறை மற்றும் சட்டமியற்றல் மைல்கற்களை சரியான காலவரிசையில் அமைக்கவும்:\n1. தெளிவற்ற நிலையில் பொது உணர்வு வழிகாட்டினாலும், முகவுரை அரசியலமைப்பின் பகுதி அல்ல என உச்ச நீதிமன்றம் கூறுதல் (பெருபாரி)\n2. அரசியலமைப்பின் மதச்சார்பற்ற தன்மை அடிப்படை கட்டமைப்பின் ஒரு பகுதி என உச்ச நீதிமன்றம் தீர்ப்பளித்தல் (கேசவானந்த பாரதி)\n3. 42வது அரசியலமைப்புத் திருத்தச் சட்டத்தின் மூலம் 'மதச்சார்பற்ற' என்ற சொல் முகவுரையில் வெளிப்படையாகச் சேர்க்கப்படுதல்\n4. மதச்சார்பற்ற கொள்கைகளுக்கு எதிராகச் செயல்படும் மாநில அரசுகளை உறுப்பு 356-ன் கீழ் கலைக்கலாம் என உச்ச நீதிமன்றம் தீர்ப்பளித்தல் (எஸ்.ஆர். பொம்மை)",
        "options_en": ["2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "1 -> 2 -> 4 -> 3", "1 -> 2 -> 3 -> 4"],
        "options_ta": ["2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "1 -> 2 -> 4 -> 3", "1 -> 2 -> 3 -> 4"],
        "answer": "d",
        "explanation_en": "Chronological Sequence: 1 (Berubari Union: 1960) -> 2 (Kesavananda Bharati secularism ruling: 1973) -> 3 (42nd Amendment insertion: 1976) -> 4 (S.R. Bommai secularism ruling: 1994).",
        "explanation_ta": "சரியான காலவரிசை: 1 (பெருபாரி யூனியன்: 1960) -> 2 (கேசவானந்த பாரதி மதச்சார்பின்மை தீர்ப்பு: 1973) -> 3 (42வது திருத்தச் சேர்க்கை: 1976) -> 4 (எஸ்.ஆர். பொம்மை தீர்ப்பு: 1994)."
    },

    # -------------------------------------------------------------------------
    # Q13: PRE_CHRONO_013
    # -------------------------------------------------------------------------
    {
        "id": "PRE_CHRONO_013",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Chronology",
        "question": {
            "en": "Arrange the following four major historical developments relating to the origin, interpretation, and amendment of the Preamble in correct chronological order:\n1. Drafting and unanimous adoption of the Objectives Resolution by the Constituent Assembly\n2. Supreme Court advisory opinion in Berubari Union Case declaring Preamble is NOT part of the Constitution\n3. 13-Judge Constitutional Bench in Kesavananda Bharati Case declaring Preamble IS part of the Constitution\n4. Parliament enacts the 42nd Constitutional Amendment Act inserting Socialist, Secular, and Integrity",
            "ta": "முகவுரையின் தோற்றம், விளக்கம் மற்றும் திருத்தம் தொடர்பான பின்வரும் நான்கு முக்கிய வரலாற்று நிகழ்வுகளை சரியான காலவரிசையில் அமைக்கவும்:\n1. அரசியலமைப்பு நிர்ணய அவையால் குறிக்கோள் தீர்மானம் வரைவு செய்யப்பட்டு ஏகமனதாக ஏற்றுக்கொள்ளப்படுதல்\n2. பெருபாரி யூனியன் வழக்கில் முகவுரை அரசியலமைப்பின் பகுதி அல்ல என உச்ச நீதிமன்றம் ஆலோசனைக் கருத்து தெரிவித்தல்\n3. கேசவானந்த பாரதி வழக்கில் 13 நீதிபதிகள் அமர்வு முகவுரை அரசியலமைப்பின் ஒரு பகுதி எனத் தீர்ப்பளித்தல்\n4. நாடாளுமன்றம் 42வது அரசியலமைப்புத் திருத்தச் சட்டத்தை இயற்றி சமதர்ம, மதச்சார்பற்ற, ஒருமைப்பாடு சொற்களைச் சேர்த்தல்"
        },
        "events": [
            {
                "id": "1",
                "en": "Drafting and unanimous adoption of the Objectives Resolution by the Constituent Assembly",
                "ta": "அரசியலமைப்பு நிர்ணய அவையால் குறிக்கோள் தீர்மானம் வரைவு செய்யப்பட்டு ஏகமனதாக ஏற்றுக்கொள்ளப்படுதல்"
            },
            {
                "id": "2",
                "en": "Supreme Court advisory opinion in Berubari Union Case declaring Preamble is NOT part of the Constitution",
                "ta": "பெருபாரி யூனியன் வழக்கில் முகவுரை அரசியலமைப்பின் பகுதி அல்ல என உச்ச நீதிமன்றம் ஆலோசனைக் கருத்து தெரிவித்தல்"
            },
            {
                "id": "3",
                "en": "13-Judge Constitutional Bench in Kesavananda Bharati Case declaring Preamble IS part of the Constitution",
                "ta": "கேசவானந்த பாரதி வழக்கில் 13 நீதிபதிகள் அமர்வு முகவுரை அரசியலமைப்பின் ஒரு பகுதி எனத் தீர்ப்பளித்தல்"
            },
            {
                "id": "4",
                "en": "Parliament enacts the 42nd Constitutional Amendment Act inserting Socialist, Secular, and Integrity",
                "ta": "நாடாளுமன்றம் 42வது அரசியலமைப்புத் திருத்தச் சட்டத்தை இயற்றி சமதர்ம, மதச்சார்பற்ற, ஒருமைப்பாடு சொற்களைச் சேர்த்தல்"
            }
        ],
        "options": [
            {"id": "A", "en": "2 -> 1 -> 3 -> 4", "ta": "2 -> 1 -> 3 -> 4"},
            {"id": "B", "en": "1 -> 3 -> 2 -> 4", "ta": "1 -> 3 -> 2 -> 4"},
            {"id": "C", "en": "1 -> 2 -> 3 -> 4", "ta": "1 -> 2 -> 3 -> 4"},
            {"id": "D", "en": "1 -> 2 -> 4 -> 3", "ta": "1 -> 2 -> 4 -> 3"}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "Chronological Sequence: 1 (Objectives Resolution: 1946-1947) -> 2 (Berubari Union: 1960) -> 3 (Kesavananda Bharati: 1973) -> 4 (42nd Amendment Act: 1976).",
            "ta": "சரியான காலவரிசை: 1 (குறிக்கோள் தீர்மானம்: 1946-1947) -> 2 (பெருபாரி யூனியன்: 1960) -> 3 (கேசவானந்த பாரதி: 1973) -> 4 (42வது திருத்தச் சட்டம்: 1976)."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Objectives Resolution (1946-1947) preceded the Berubari Union case (1960).", "ta": "தவறு. குறிக்கோள் தீர்மானம் (1946-1947) பெருபாரி யூனியன் வழக்குக்கு (1960) முந்தையது."},
            "B": {"en": "Incorrect. Berubari (1960) was decided before Kesavananda Bharati (1973).", "ta": "தவறு. பெருபாரி (1960) கேசவானந்த பாரதிக்கு (1973) முந்தையது."},
            "C": {"en": "Correct. 1 (1946-47) -> 2 (1960) -> 3 (1973) -> 4 (1976) accurately reflects the sequence from origin to amendment.", "ta": "சரி. 1 (1946-47) -> 2 (1960) -> 3 (1973) -> 4 (1976) தோற்றத்திலிருந்து திருத்தம் வரையிலான வரிசையைத் துல்லியமாகப் பிரதிபலிக்கிறது."},
            "D": {"en": "Incorrect. Kesavananda Bharati in 1973 (3) paved the way for the 42nd Amendment in 1976 (4).", "ta": "தவறு. 1973-ன் கேசவானந்த பாரதி தீர்ப்பே (3) 1976-ன் 42வது திருத்தத்திற்கு (4) வழிவகுத்தது."}
        },
        "tnpsc_tip": {
            "en": "TNPSC Trap: Always remember that the 42nd Amendment in 1976 was passed AFTER Kesavananda Bharati (1973) had already declared that the Preamble is a part of the Constitution and can be amended.",
            "ta": "TNPSC பொறி: முகவுரை அரசியலமைப்பின் ஒரு பகுதி மற்றும் திருத்தத்தக்கது என கேசவானந்த பாரதி (1973) அறிவித்த பின்னரே 42வது திருத்தம் (1976) நிறைவேற்றப்பட்டது என்பதை நினைவில் கொள்ளவும்."
        },
        "revision_fact": {
            "en": "The Kesavananda Bharati judgment was delivered on April 24, 1973, by the largest ever 13-judge constitutional bench.",
            "ta": "கேசவானந்த பாரதி தீர்ப்பு ஏப்ரல் 24, 1973 அன்று உச்ச நீதிமன்ற வரலாற்றிலேயே மிகப்பெரிய 13 நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வால் வழங்கப்பட்டது."
        },
        "source_reference": [
            "M. Laxmikanth - Indian Polity",
            "Constitution of India Documents"
        ],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "Chronology", "Objectives Resolution", "Berubari", "Kesavananda Bharati", "42nd Amendment"],
        "question_en": "Arrange the following four major historical developments relating to the origin, interpretation, and amendment of the Preamble in correct chronological order:\n1. Drafting and unanimous adoption of the Objectives Resolution by the Constituent Assembly\n2. Supreme Court advisory opinion in Berubari Union Case declaring Preamble is NOT part of the Constitution\n3. 13-Judge Constitutional Bench in Kesavananda Bharati Case declaring Preamble IS part of the Constitution\n4. Parliament enacts the 42nd Constitutional Amendment Act inserting Socialist, Secular, and Integrity",
        "question_ta": "முகவுரையின் தோற்றம், விளக்கம் மற்றும் திருத்தம் தொடர்பான பின்வரும் நான்கு முக்கிய வரலாற்று நிகழ்வுகளை சரியான காலவரிசையில் அமைக்கவும்:\n1. அரசியலமைப்பு நிர்ணய அவையால் குறிக்கோள் தீர்மானம் வரைவு செய்யப்பட்டு ஏகமனதாக ஏற்றுக்கொள்ளப்படுதல்\n2. பெருபாரி யூனியன் வழக்கில் முகவுரை அரசியலமைப்பின் பகுதி அல்ல என உச்ச நீதிமன்றம் ஆலோசனைக் கருத்து தெரிவித்தல்\n3. கேசவானந்த பாரதி வழக்கில் 13 நீதிபதிகள் அமர்வு முகவுரை அரசியலமைப்பின் ஒரு பகுதி எனத் தீர்ப்பளித்தல்\n4. நாடாளுமன்றம் 42வது அரசியலமைப்புத் திருத்தச் சட்டத்தை இயற்றி சமதர்ம, மதச்சார்பற்ற, ஒருமைப்பாடு சொற்களைச் சேர்த்தல்",
        "options_en": ["2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "1 -> 2 -> 3 -> 4", "1 -> 2 -> 4 -> 3"],
        "options_ta": ["2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "1 -> 2 -> 3 -> 4", "1 -> 2 -> 4 -> 3"],
        "answer": "c",
        "explanation_en": "Chronological Sequence: 1 (Objectives Resolution: 1946-1947) -> 2 (Berubari Union: 1960) -> 3 (Kesavananda Bharati: 1973) -> 4 (42nd Amendment Act: 1976).",
        "explanation_ta": "சரியான காலவரிசை: 1 (குறிக்கோள் தீர்மானம்: 1946-1947) -> 2 (பெருபாரி யூனியன்: 1960) -> 3 (கேசவானந்த பாரதி: 1973) -> 4 (42வது திருத்தச் சட்டம்: 1976)."
    },

    # -------------------------------------------------------------------------
    # Q14: PRE_CHRONO_014
    # -------------------------------------------------------------------------
    {
        "id": "PRE_CHRONO_014",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Chronology",
        "question": {
            "en": "Arrange the following stages in the evolution of the Preamble's textual description of the Indian Republic in correct chronological order:\n1. Original Preamble declaring India as a 'SOVEREIGN DEMOCRATIC REPUBLIC'\n2. Original Fraternity clause containing 'unity of the Nation'\n3. 42nd Amendment substituting 'SOVEREIGN SOCIALIST SECULAR DEMOCRATIC REPUBLIC'\n4. 42nd Amendment substituting 'unity and integrity of the Nation'",
            "ta": "இந்தியக் குடியரசின் முகவுரை உரையின் பரிணாம வளர்ச்சியில் பின்வரும் நிலைகளை சரியான காலவரிசையில் அமைக்கவும்:\n1. இந்தியாவை 'இறையாண்மை ஜனநாயகக் குடியரசு' என அறிவித்த அசல் முகவுரை\n2. 'தேசத்தின் ஒற்றுமை' என்பதைக் கொண்டிருந்த அசல் சகோதரத்துவ வாசகம்\n3. 'இறையாண்மை சமதர்ம மதச்சார்பற்ற ஜனநாயகக் குடியரசு' என மாற்றிய 42வது திருத்தம்\n4. 'தேசத்தின் ஒற்றுமையும் ஒருமைப்பாடும்' என மாற்றிய 42வது திருத்தம்"
        },
        "events": [
            {
                "id": "1",
                "en": "Original Preamble declaring India as a 'SOVEREIGN DEMOCRATIC REPUBLIC'",
                "ta": "இந்தியாவை 'இறையாண்மை ஜனநாயகக் குடியரசு' என அறிவித்த அசல் முகவுரை"
            },
            {
                "id": "2",
                "en": "Original Fraternity clause containing 'unity of the Nation'",
                "ta": "'தேசத்தின் ஒற்றுமை' என்பதைக் கொண்டிருந்த அசல் சகோதரத்துவ வாசகம்"
            },
            {
                "id": "3",
                "en": "42nd Amendment substituting 'SOVEREIGN SOCIALIST SECULAR DEMOCRATIC REPUBLIC'",
                "ta": "'இறையாண்மை சமதர்ம மதச்சார்பற்ற ஜனநாயகக் குடியரசு' என மாற்றிய 42வது திருத்தம்"
            },
            {
                "id": "4",
                "en": "42nd Amendment substituting 'unity and integrity of the Nation'",
                "ta": "'தேசத்தின் ஒற்றுமையும் ஒருமைப்பாடும்' என மாற்றிய 42வது திருத்தம்"
            }
        ],
        "options": [
            {"id": "A", "en": "1 -> 2 -> 3 -> 4", "ta": "1 -> 2 -> 3 -> 4"},
            {"id": "B", "en": "3 -> 4 -> 1 -> 2", "ta": "3 -> 4 -> 1 -> 2"},
            {"id": "C", "en": "1 -> 3 -> 2 -> 4", "ta": "1 -> 3 -> 2 -> 4"},
            {"id": "D", "en": "2 -> 1 -> 4 -> 3", "ta": "2 -> 1 -> 4 -> 3"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Chronological Evolution: 1 & 2 (Original 1950 text: Sovereign Democratic Republic & unity of the Nation) -> 3 & 4 (1976 42nd Amendment: Socialist, Secular added to nature; Integrity added to Fraternity).",
            "ta": "காலவரிசை வளர்ச்சி: 1 & 2 (அசல் 1950 உரை: இறையாண்மை ஜனநாயகக் குடியரசு & தேசத்தின் ஒற்றுமை) -> 3 & 4 (1976 42வது திருத்தம்: சமதர்ம, மதச்சார்பற்ற சேர்க்கை & ஒருமைப்பாடு சேர்க்கை)."
        },
        "why_not_others": {
            "A": {"en": "Correct. 1 & 2 represent the 1950 original text, while 3 & 4 represent the 1976 amended text.", "ta": "சரி. 1 & 2 அசல் 1950 உரையையும், 3 & 4 1976 திருத்தப்பட்ட உரையையும் குறிக்கின்றன."},
            "B": {"en": "Incorrect. The 1976 amendments (3, 4) cannot precede the 1950 original provisions (1, 2).", "ta": "தவறு. 1976 திருத்தங்கள் (3, 4) 1950 அசல் விதிகளுக்கு (1, 2) முந்தையதாக இருக்க முடியாது."},
            "C": {"en": "Incorrect. Original provisions existed simultaneously in 1950 before 1976 amendments.", "ta": "தவறு. அசல் விதிகள் 1976 திருத்தங்களுக்கு முன்பே 1950-ல் ஒன்றாக இருந்தன."},
            "D": {"en": "Incorrect. Sovereign Democratic Republic (1) was in paragraph 1 of the original 1950 text, while unity of the Nation (2) was in paragraph 4.", "ta": "தவறு. இறையாண்மை ஜனநாயகக் குடியரசு (1) அசல் உரையின் முதல் பத்தியிலும், தேசத்தின் ஒற்றுமை (2) 4வது பத்தியிலும் அமைந்திருந்தது."}
        },
        "tnpsc_tip": {
            "en": "TNPSC Question Trap: 'Integrity' was added to the Fraternity paragraph ('unity and integrity of the Nation'), NOT to the opening 'Sovereign Democratic Republic' declaration.",
            "ta": "TNPSC வினாப் பொறி: 'ஒருமைப்பாடு' என்ற சொல் தொடக்கப் பத்தியில் சேர்க்கப்படவில்லை; சகோதரத்துவப் பகுதியில் ('தேசத்தின் ஒற்றுமையும் ஒருமைப்பாடும்') சேர்க்கப்பட்டது."
        },
        "revision_fact": {
            "en": "Before 1976, the Preamble contained only 81 words; the 42nd Amendment added 4 words ('Socialist', 'Secular', 'and', 'Integrity').",
            "ta": "1976-க்கு முன்பு முகவுரையில் 81 சொற்களே இருந்தன; 42வது திருத்தம் 'சமதர்ம', 'மதச்சார்பற்ற', 'மற்றும்', 'ஒருமைப்பாடு' ஆகிய சொற்களைச் சேர்த்தது."
        },
        "source_reference": [
            "Text of the Constitution of India",
            "M. Laxmikanth - Indian Polity",
            "Samacheer Kalvi - Standard 11 Political Science"
        ],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "Textual Evolution", "42nd Amendment", "Integrity"],
        "question_en": "Arrange the following stages in the evolution of the Preamble's textual description of the Indian Republic in correct chronological order:\n1. Original Preamble declaring India as a 'SOVEREIGN DEMOCRATIC REPUBLIC'\n2. Original Fraternity clause containing 'unity of the Nation'\n3. 42nd Amendment substituting 'SOVEREIGN SOCIALIST SECULAR DEMOCRATIC REPUBLIC'\n4. 42nd Amendment substituting 'unity and integrity of the Nation'",
        "question_ta": "இந்தியக் குடியரசின் முகவுரை உரையின் பரிணாம வளர்ச்சியில் பின்வரும் நிலைகளை சரியான காலவரிசையில் அமைக்கவும்:\n1. இந்தியாவை 'இறையாண்மை ஜனநாயகக் குடியரசு' என அறிவித்த அசல் முகவுரை\n2. 'தேசத்தின் ஒற்றுமை' என்பதைக் கொண்டிருந்த அசல் சகோதரத்துவ வாசகம்\n3. 'இறையாண்மை சமதர்ம மதச்சார்பற்ற ஜனநாயகக் குடியரசு' என மாற்றிய 42வது திருத்தம்\n4. 'தேசத்தின் ஒற்றுமையும் ஒருமைப்பாடும்' என மாற்றிய 42வது திருத்தம்",
        "options_en": ["1 -> 2 -> 3 -> 4", "3 -> 4 -> 1 -> 2", "1 -> 3 -> 2 -> 4", "2 -> 1 -> 4 -> 3"],
        "options_ta": ["1 -> 2 -> 3 -> 4", "3 -> 4 -> 1 -> 2", "1 -> 3 -> 2 -> 4", "2 -> 1 -> 4 -> 3"],
        "answer": "a",
        "explanation_en": "Chronological Evolution: 1 & 2 (Original 1950 text: Sovereign Democratic Republic & unity of the Nation) -> 3 & 4 (1976 42nd Amendment: Socialist, Secular added to nature; Integrity added to Fraternity).",
        "explanation_ta": "காலவரிசை வளர்ச்சி: 1 & 2 (அசல் 1950 உரை: இறையாண்மை ஜனநாயகக் குடியரசு & தேசத்தின் ஒற்றுமை) -> 3 & 4 (1976 42வது திருத்தம்: சமதர்ம, மதச்சார்பற்ற சேர்க்கை & ஒருமைப்பாடு சேர்க்கை)."
    },

    # -------------------------------------------------------------------------
    # Q15: PRE_CHRONO_015
    # -------------------------------------------------------------------------
    {
        "id": "PRE_CHRONO_015",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Chronology",
        "question": {
            "en": "Arrange the following milestones in the historical debate over whether the Preamble is a part of the Constitution in correct chronological order:\n1. Constituent Assembly formally adopts the motion that 'the Preamble stands part of the Constitution'\n2. Supreme Court in Berubari Union Reference holds that the Preamble is NOT a part of the Constitution\n3. Supreme Court in Kesavananda Bharati Case overrules Berubari and holds that the Preamble IS a part of the Constitution\n4. Supreme Court in LIC of India Case reaffirms that the Preamble is an 'integral part' of the Constitution",
            "ta": "முகவுரை அரசியலமைப்பின் ஒரு பகுதியா என்ற வரலாற்று விவாதத்தின் பின்வரும் மைல்கற்களை சரியான காலவரிசையில் அமைக்கவும்:\n1. 'முகவுரை அரசியலமைப்பின் ஒரு பகுதியாக அமைகிறது' என்ற தீர்மானத்தை அரசியலமைப்பு நிர்ணய அவை முறையாக ஏற்றுக்கொள்கிறது\n2. பெருபாரி யூனியன் வழக்கில் முகவுரை அரசியலமைப்பின் ஒரு பகுதி அல்ல என்று உச்ச நீதிமன்றம் தீர்ப்பளிக்கிறது\n3. கேசவானந்த பாரதி வழக்கில் உச்ச நீதிமன்றம் பெருபாரி தீர்ப்பை ரத்து செய்து முகவுரை அரசியலமைப்பின் ஒரு பகுதியே எனத் தீர்ப்பளிக்கிறது\n4. எல்.ஐ.சி வழக்கில் முகவுரை அரசியலமைப்பின் 'ஒருங்கிணைந்த பகுதி' என்பதை உச்ச நீதிமன்றம் மீண்டும் உறுதிப்படுத்துகிறது"
        },
        "events": [
            {
                "id": "1",
                "en": "Constituent Assembly formally adopts the motion that 'the Preamble stands part of the Constitution'",
                "ta": "'முகவுரை அரசியலமைப்பின் ஒரு பகுதியாக அமைகிறது' என்ற தீர்மானத்தை அரசியலமைப்பு நிர்ணய அவை முறையாக ஏற்றுக்கொள்கிறது"
            },
            {
                "id": "2",
                "en": "Supreme Court in Berubari Union Reference holds that the Preamble is NOT a part of the Constitution",
                "ta": "பெருபாரி யூனியன் வழக்கில் முகவுரை அரசியலமைப்பின் ஒரு பகுதி அல்ல என்று உச்ச நீதிமன்றம் தீர்ப்பளிக்கிறது"
            },
            {
                "id": "3",
                "en": "Supreme Court in Kesavananda Bharati Case overrules Berubari and holds that the Preamble IS a part of the Constitution",
                "ta": "கேசவானந்த பாரதி வழக்கில் உச்ச நீதிமன்றம் பெருபாரி தீர்ப்பை ரத்து செய்து முகவுரை அரசியலமைப்பின் ஒரு பகுதியே எனத் தீர்ப்பளிக்கிறது"
            },
            {
                "id": "4",
                "en": "Supreme Court in LIC of India Case reaffirms that the Preamble is an 'integral part' of the Constitution",
                "ta": "எல்.ஐ.சி வழக்கில் முகவுரை அரசியலமைப்பின் 'ஒருங்கிணைந்த பகுதி' என்பதை உச்ச நீதிமன்றம் மீண்டும் உறுதிப்படுத்துகிறது"
            }
        ],
        "options": [
            {"id": "A", "en": "2 -> 1 -> 3 -> 4", "ta": "2 -> 1 -> 3 -> 4"},
            {"id": "B", "en": "1 -> 2 -> 3 -> 4", "ta": "1 -> 2 -> 3 -> 4"},
            {"id": "C", "en": "1 -> 3 -> 2 -> 4", "ta": "1 -> 3 -> 2 -> 4"},
            {"id": "D", "en": "2 -> 3 -> 1 -> 4", "ta": "2 -> 3 -> 1 -> 4"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "Historical Progression: 1 (Constituent Assembly vote: Oct 17, 1949) -> 2 (Berubari Reference: 1960) -> 3 (Kesavananda Bharati: 1973) -> 4 (LIC of India: 1995).",
            "ta": "வரலாற்று வளர்ச்சி: 1 (அரசியலமைப்பு சபை வாக்கு: அக்டோபர் 17, 1949) -> 2 (பெருபாரி வழக்கு: 1960) -> 3 (கேசவானந்த பாரதி: 1973) -> 4 (எல்ஐசி வழக்கு: 1995)."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. The Constituent Assembly vote in 1949 (1) happened before the Berubari Case in 1960 (2).", "ta": "தவறு. 1949 அரசியலமைப்பு சபை வாக்கெடுப்பு (1) 1960 பெருபாரி வழக்குக்கு (2) முந்தையது."},
            "B": {"en": "Correct. 1 (1949) -> 2 (1960) -> 3 (1973) -> 4 (1995) accurately captures the complete 46-year debate.", "ta": "சரி. 1 (1949) -> 2 (1960) -> 3 (1973) -> 4 (1995) 46 ஆண்டுகால விவாதத்தை முழுமையாகப் பிரதிபலிக்கிறது."},
            "C": {"en": "Incorrect. Berubari (1960) came before Kesavananda Bharati (1973).", "ta": "தவறு. பெருபாரி (1960) கேசவானந்த பாரதிக்கு (1973) முந்தையது."},
            "D": {"en": "Incorrect. Constituent Assembly adoption occurred at the inception in 1949.", "ta": "தவறு. அரசியலமைப்பு சபை ஏற்பு தொடக்கத்திலேயே 1949-ல் நடந்தது."}
        },
        "tnpsc_tip": {
            "en": "TNPSC Key Takeaway: The Supreme Court in Kesavananda Bharati relied heavily on the fact that Dr. Rajendra Prasad had put the motion 'that the Preamble stands part of the Constitution' to reverse Berubari.",
            "ta": "TNPSC முக்கிய குறிப்பு: பெருபாரி தீர்ப்பை ரத்து செய்ய, டாக்டர் ராஜேந்திர பிரசாத் 'முகவுரை அரசியலமைப்பின் ஒரு பகுதியாக அமைகிறது' என வாக்கெடுப்பு நடத்திய வரலாற்று உண்மையை கேசவானந்த பாரதி அமர்வு முக்கிய ஆதாரமாகப் பயன்படுத்தியது."
        },
        "revision_fact": {
            "en": "Despite being an integral part of the Constitution, the Preamble is non-justiciable (not directly enforceable in courts) and is neither a source of power nor a limitation on legislative powers.",
            "ta": "முகவுரை அரசியலமைப்பின் ஒருங்கிணைந்த பகுதியாக இருந்தபோதிலும், அது நீதிமன்றங்களால் நிலைநிறுத்த முடியாதது மற்றும் சட்டமன்றத்திற்கு அதிகார மூலமோ அல்லது அதிகாரத்தின் மீதான வரம்போ அல்ல."
        },
        "source_reference": [
            "M. Laxmikanth - Indian Polity",
            "Constituent Assembly Debates (Vol. X)",
            "Supreme Court Reports (1960, 1973, 1995)"
        ],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "Constitutional Status", "Part of Constitution", "Debate"],
        "question_en": "Arrange the following milestones in the historical debate over whether the Preamble is a part of the Constitution in correct chronological order:\n1. Constituent Assembly formally adopts the motion that 'the Preamble stands part of the Constitution'\n2. Supreme Court in Berubari Union Reference holds that the Preamble is NOT a part of the Constitution\n3. Supreme Court in Kesavananda Bharati Case overrules Berubari and holds that the Preamble IS a part of the Constitution\n4. Supreme Court in LIC of India Case reaffirms that the Preamble is an 'integral part' of the Constitution",
        "question_ta": "முகவுரை அரசியலமைப்பின் ஒரு பகுதியா என்ற வரலாற்று விவாதத்தின் பின்வரும் மைல்கற்களை சரியான காலவரிசையில் அமைக்கவும்:\n1. 'முகவுரை அரசியலமைப்பின் ஒரு பகுதியாக அமைகிறது' என்ற தீர்மானத்தை அரசியலமைப்பு நிர்ணய அவை முறையாக ஏற்றுக்கொள்கிறது\n2. பெருபாரி யூனியன் வழக்கில் முகவுரை அரசியலமைப்பின் ஒரு பகுதி அல்ல என்று உச்ச நீதிமன்றம் தீர்ப்பளிக்கிறது\n3. கேசவானந்த பாரதி வழக்கில் உச்ச நீதிமன்றம் பெருபாரி தீர்ப்பை ரத்து செய்து முகவுரை அரசியலமைப்பின் ஒரு பகுதியே எனத் தீர்ப்பளிக்கிறது\n4. எல்.ஐ.சி வழக்கில் முகவுரை அரசியலமைப்பின் 'ஒருங்கிணைந்த பகுதி' என்பதை உச்ச நீதிமன்றம் மீண்டும் உறுதிப்படுத்துகிறது",
        "options_en": ["2 -> 1 -> 3 -> 4", "1 -> 2 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "2 -> 3 -> 1 -> 4"],
        "options_ta": ["2 -> 1 -> 3 -> 4", "1 -> 2 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "2 -> 3 -> 1 -> 4"],
        "answer": "b",
        "explanation_en": "Historical Progression: 1 (Constituent Assembly vote: Oct 17, 1949) -> 2 (Berubari Reference: 1960) -> 3 (Kesavananda Bharati: 1973) -> 4 (LIC of India: 1995).",
        "explanation_ta": "வரலாற்று வளர்ச்சி: 1 (அரசியலமைப்பு சபை வாக்கு: அக்டோபர் 17, 1949) -> 2 (பெருபாரி வழக்கு: 1960) -> 3 (கேசவானந்த பாரதி: 1973) -> 4 (எல்ஐசி வழக்கு: 1995)."
    },

    # -------------------------------------------------------------------------
    # Q16: PRE_CHRONO_016 (MODEL 3: Latest to Earliest)
    # -------------------------------------------------------------------------
    {
        "id": "PRE_CHRONO_016",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Chronology",
        "question": {
            "en": "Arrange the following historic events related to the Preamble in reverse chronological order (from LATEST to EARLIEST):\n1. 42nd Constitutional Amendment Act inserts 'Socialist', 'Secular', and 'Integrity'\n2. Kesavananda Bharati Case judgment establishes Basic Structure Doctrine and Preamble amendability\n3. Berubari Union Case advisory opinion rules Preamble is not a part of the Constitution\n4. Constituent Assembly unanimously adopts the Objectives Resolution moved by Nehru",
            "ta": "முகவுரை தொடர்பான பின்வரும் வரலாற்று நிகழ்வுகளை தலைகீழ் காலவரிசையில் (மிகப் பிந்தையதிலிருந்து மிக முந்தையது வரை) அமைக்கவும்:\n1. 42வது அரசியலமைப்புத் திருத்தச் சட்டம் 'சமதர்ம', 'மதச்சார்பற்ற' மற்றும் 'ஒருமைப்பாடு' ஆகிய சொற்களைச் சேர்த்தல்\n2. கேசவானந்த பாரதி தீர்ப்பு அடிப்படை கட்டமைப்புக் கோட்பாடு மற்றும் முகவுரையின் திருத்தப்படும் தன்மையை நிறுவுதல்\n3. பெருபாரி யூனியன் ஆலோசனைக் கருத்து முகவுரை அரசியலமைப்பின் பகுதி அல்ல எனத் தீர்ப்பளித்தல்\n4. நேருவால் முன்மொழியப்பட்ட குறிக்கோள் தீர்மானத்தை அரசியலமைப்பு நிர்ணய அவை ஏகமனதாக ஏற்றுக்கொள்வது"
        },
        "events": [
            {
                "id": "1",
                "en": "42nd Constitutional Amendment Act inserts 'Socialist', 'Secular', and 'Integrity' (1976)",
                "ta": "42வது அரசியலமைப்புத் திருத்தச் சட்டம் 'சமதர்ம', 'மதச்சார்பற்ற' மற்றும் 'ஒருமைப்பாடு' ஆகிய சொற்களைச் சேர்த்தல் (1976)"
            },
            {
                "id": "2",
                "en": "Kesavananda Bharati Case judgment establishes Basic Structure Doctrine and Preamble amendability (1973)",
                "ta": "கேசவானந்த பாரதி தீர்ப்பு அடிப்படை கட்டமைப்புக் கோட்பாடு மற்றும் முகவுரையின் திருத்தப்படும் தன்மையை நிறுவுதல் (1973)"
            },
            {
                "id": "3",
                "en": "Berubari Union Case advisory opinion rules Preamble is not a part of the Constitution (1960)",
                "ta": "பெருபாரி யூனியன் ஆலோசனைக் கருத்து முகவுரை அரசியலமைப்பின் பகுதி அல்ல எனத் தீர்ப்பளித்தல் (1960)"
            },
            {
                "id": "4",
                "en": "Constituent Assembly unanimously adopts the Objectives Resolution moved by Nehru (1947)",
                "ta": "நேருவால் முன்மொழியப்பட்ட குறிக்கோள் தீர்மானத்தை அரசியலமைப்பு நிர்ணய அவை ஏகமனதாக ஏற்றுக்கொள்வது (1947)"
            }
        ],
        "options": [
            {"id": "A", "en": "4 -> 3 -> 2 -> 1", "ta": "4 -> 3 -> 2 -> 1"},
            {"id": "B", "en": "1 -> 3 -> 2 -> 4", "ta": "1 -> 3 -> 2 -> 4"},
            {"id": "C", "en": "2 -> 1 -> 3 -> 4", "ta": "2 -> 1 -> 3 -> 4"},
            {"id": "D", "en": "1 -> 2 -> 3 -> 4", "ta": "1 -> 2 -> 3 -> 4"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "Reverse Chronological Order (Latest to Earliest): 1 (42nd Amendment: 1976) -> 2 (Kesavananda Bharati: 1973) -> 3 (Berubari Union: 1960) -> 4 (Objectives Resolution adopted: 1947).",
            "ta": "தலைகீழ் காலவரிசை (பிந்தையதிலிருந்து முந்தையது): 1 (42வது திருத்தம்: 1976) -> 2 (கேசவானந்த பாரதி: 1973) -> 3 (பெருபாரி யூனியன்: 1960) -> 4 (குறிக்கோள் தீர்மானம் ஏற்பு: 1947)."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. 4 -> 3 -> 2 -> 1 is earliest to latest, not latest to earliest.", "ta": "தவறு. 4 -> 3 -> 2 -> 1 என்பது முந்தையதிலிருந்து பிந்தையது; பிந்தையதிலிருந்து முந்தையது அல்ல."},
            "B": {"en": "Incorrect. Kesavananda Bharati (1973) is more recent than Berubari Union (1960).", "ta": "தவறு. கேசவானந்த பாரதி (1973) பெருபாரி யூனியனை (1960) விட பிந்தையது."},
            "C": {"en": "Incorrect. 42nd Amendment (1976) is more recent than Kesavananda Bharati (1973).", "ta": "தவறு. 42வது திருத்தம் (1976) கேசவானந்த பாரதியை (1973) விட பிந்தையது."},
            "D": {"en": "Correct. 1 (1976) -> 2 (1973) -> 3 (1960) -> 4 (1947) follows the exact reverse chronological order.", "ta": "சரி. 1 (1976) -> 2 (1973) -> 3 (1960) -> 4 (1947) துல்லியமான தலைகீழ் காலவரிசையாகும்."}
        },
        "tnpsc_tip": {
            "en": "TNPSC Practice Tip: Whenever 'reverse chronological order' or 'latest to earliest' is tested, identify the newest event (1976 here) and oldest event (1947 here) first.",
            "ta": "TNPSC பயிற்சி குறிப்பு: 'தலைகீழ் காலவரிசை' கேட்கப்படும் போது, மிக அண்மைய நிகழ்வையும் (1976), மிக முந்தைய நிகழ்வையும் (1947) முதலில் அடையாளம் காணவும்."
        },
        "revision_fact": {
            "en": "The Objectives Resolution contained 8 paragraphs outlining the future democratic, sovereign republic structure of India.",
            "ta": "குறிக்கோள் தீர்மானம் இந்தியாவின் எதிர்கால ஜனநாயக, இறையாண்மை குடியரசு கட்டமைப்பை கோடிட்டுக் காட்டும் 8 பத்திகளைக் கொண்டிருந்தது."
        },
        "source_reference": [
            "M. Laxmikanth - Indian Polity",
            "NCERT Class XI - Indian Constitution at Work"
        ],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "Reverse Chronology", "Latest to Earliest", "Core Timeline"],
        "question_en": "Arrange the following historic events related to the Preamble in reverse chronological order (from LATEST to EARLIEST):\n1. 42nd Constitutional Amendment Act inserts 'Socialist', 'Secular', and 'Integrity'\n2. Kesavananda Bharati Case judgment establishes Basic Structure Doctrine and Preamble amendability\n3. Berubari Union Case advisory opinion rules Preamble is not a part of the Constitution\n4. Constituent Assembly unanimously adopts the Objectives Resolution moved by Nehru",
        "question_ta": "முகவுரை தொடர்பான பின்வரும் வரலாற்று நிகழ்வுகளை தலைகீழ் காலவரிசையில் (மிகப் பிந்தையதிலிருந்து மிக முந்தையது வரை) அமைக்கவும்:\n1. 42வது அரசியலமைப்புத் திருத்தச் சட்டம் 'சமதர்ம', 'மதச்சார்பற்ற' மற்றும் 'ஒருமைப்பாடு' ஆகிய சொற்களைச் சேர்த்தல்\n2. கேசவானந்த பாரதி தீர்ப்பு அடிப்படை கட்டமைப்புக் கோட்பாடு மற்றும் முகவுரையின் திருத்தப்படும் தன்மையை நிறுவுதல்\n3. பெருபாரி யூனியன் ஆலோசனைக் கருத்து முகவுரை அரசியலமைப்பின் பகுதி அல்ல எனத் தீர்ப்பளித்தல்\n4. நேருவால் முன்மொழியப்பட்ட குறிக்கோள் தீர்மானத்தை அரசியலமைப்பு நிர்ணய அவை ஏகமனதாக ஏற்றுக்கொள்வது",
        "options_en": ["4 -> 3 -> 2 -> 1", "1 -> 3 -> 2 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 2 -> 3 -> 4"],
        "options_ta": ["4 -> 3 -> 2 -> 1", "1 -> 3 -> 2 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 2 -> 3 -> 4"],
        "answer": "d",
        "explanation_en": "Reverse Chronological Order (Latest to Earliest): 1 (42nd Amendment: 1976) -> 2 (Kesavananda Bharati: 1973) -> 3 (Berubari Union: 1960) -> 4 (Objectives Resolution adopted: 1947).",
        "explanation_ta": "தலைகீழ் காலவரிசை (பிந்தையதிலிருந்து முந்தையது): 1 (42வது திருத்தம்: 1976) -> 2 (கேசவானந்த பாரதி: 1973) -> 3 (பெருபாரி யூனியன்: 1960) -> 4 (குறிக்கோள் தீர்மானம் ஏற்பு: 1947)."
    },

    # -------------------------------------------------------------------------
    # Q17: PRE_CHRONO_017
    # -------------------------------------------------------------------------
    {
        "id": "PRE_CHRONO_017",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Chronology",
        "question": {
            "en": "Arrange the four core ingredients of the Preamble in the exact sequential order as they appear from beginning to end in the constitutional text:\n1. Source of Authority of the Constitution ('WE, THE PEOPLE OF INDIA')\n2. Nature of the Indian State ('SOVEREIGN SOCIALIST SECULAR DEMOCRATIC REPUBLIC')\n3. Statement of Constitutional Objectives ('JUSTICE, LIBERTY, EQUALITY, FRATERNITY')\n4. Date of Adoption and Enactment ('twenty-sixth day of November, 1949')",
            "ta": "அரசியலமைப்பு உரையில் தொடக்கத்திலிருந்து இறுதி வரை காணப்படும் நான்கு முக்கிய கூறுகளை சரியான வரிசையில் அமைக்கவும்:\n1. அரசியலமைப்பு அதிகாரத்தின் மூலம் ('இந்திய மக்களாகிய நாம்')\n2. இந்திய அரசின் தன்மை ('இறையாண்மை சமதர்ம மதச்சார்பற்ற ஜனநாயக குடியரசு')\n3. அரசியலமைப்பு இலக்குகளின் பிரகடனம் ('நீதி, சுதந்திரம், சமத்துவம், சகோதரத்துவம்')\n4. ஏற்றுக்கொள்ளப்பட்டு இயற்றப்பட்ட நாள் ('நவம்பர் இருபத்தாறாம் நாள், 1949')"
        },
        "events": [
            {
                "id": "1",
                "en": "Source of Authority of the Constitution ('WE, THE PEOPLE OF INDIA')",
                "ta": "அரசியலமைப்பு அதிகாரத்தின் மூலம் ('இந்திய மக்களாகிய நாம்')"
            },
            {
                "id": "2",
                "en": "Nature of the Indian State ('SOVEREIGN SOCIALIST SECULAR DEMOCRATIC REPUBLIC')",
                "ta": "இந்திய அரசின் தன்மை ('இறையாண்மை சமதர்ம மதச்சார்பற்ற ஜனநாயக குடியரசு')"
            },
            {
                "id": "3",
                "en": "Statement of Constitutional Objectives ('JUSTICE, LIBERTY, EQUALITY, FRATERNITY')",
                "ta": "அரசியலமைப்பு இலக்குகளின் பிரகடனம் ('நீதி, சுதந்திரம், சமத்துவம், சகோதரத்துவம்')"
            },
            {
                "id": "4",
                "en": "Date of Adoption and Enactment ('twenty-sixth day of November, 1949')",
                "ta": "ஏற்றுக்கொள்ளப்பட்டு இயற்றப்பட்ட நாள் ('நவம்பர் இருபத்தாறாம் நாள், 1949')"
            }
        ],
        "options": [
            {"id": "A", "en": "1 -> 2 -> 3 -> 4", "ta": "1 -> 2 -> 3 -> 4"},
            {"id": "B", "en": "2 -> 1 -> 3 -> 4", "ta": "2 -> 1 -> 3 -> 4"},
            {"id": "C", "en": "1 -> 3 -> 2 -> 4", "ta": "1 -> 3 -> 2 -> 4"},
            {"id": "D", "en": "1 -> 2 -> 4 -> 3", "ta": "1 -> 2 -> 4 -> 3"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Structural Sequence of Preamble: 1 (Source of Authority: 'We, the People...') -> 2 (Nature of State: 'Sovereign Socialist...') -> 3 (Objectives: 'Justice, Liberty...') -> 4 (Date of Adoption: '26th November 1949').",
            "ta": "முகவுரையின் கட்டமைப்பு வரிசை: 1 (அதிகார மூலம்: 'இந்திய மக்களாகிய நாம்...') -> 2 (அரசின் தன்மை: 'இறையாண்மை சமதர்ம...') -> 3 (இலக்குகள்: 'நீதி, சுதந்திரம்...') -> 4 (ஏற்றுக்கொள்ளப்பட்ட நாள்: '26 நவம்பர் 1949')."
        },
        "why_not_others": {
            "A": {"en": "Correct. 1 -> 2 -> 3 -> 4 matches the vertical reading order of the Preamble text from top to bottom.", "ta": "சரி. 1 -> 2 -> 3 -> 4 முகவுரை உரையை மேலிருந்து கீழாகப் படிக்கும் சரியான வரிசையாகும்."},
            "B": {"en": "Incorrect. The Source of Authority ('We, the People') is the opening phrase before Nature of State.", "ta": "தவறு. அதிகாரத்தின் மூலம் ('மக்களாகிய நாம்') அரசின் தன்மைக்கு முந்தைய தொடக்க வாசகமாகும்."},
            "C": {"en": "Incorrect. Nature of State precedes Objectives in the text.", "ta": "தவறு. உரையில் இலக்குகளுக்கு முன்பாக அரசின் தன்மை வருகிறது."},
            "D": {"en": "Incorrect. Date of adoption is the closing sentence, not placed before Objectives.", "ta": "தவறு. ஏற்றுக்கொள்ளப்பட்ட நாள் இறுதி வாக்கியமாகும், இலக்குகளுக்கு முன்பாக அல்ல."}
        },
        "tnpsc_tip": {
            "en": "TNPSC 4-Ingredient Breakdown: (1) Source of Authority, (2) Nature of State, (3) Objectives, (4) Date of Adoption. Crucial structural concept.",
            "ta": "TNPSC 4-கூறு கட்டமைப்பு: (1) அதிகார மூலம், (2) அரசின் தன்மை, (3) இலக்குகள், (4) ஏற்றுக்கொள்ளப்பட்ட நாள்."
        },
        "revision_fact": {
            "en": "The date mentioned in the Preamble is November 26, 1949, celebrated annually as National Constitution Day (Samvidhan Divas).",
            "ta": "முகவுரையில் குறிப்பிடப்பட்டுள்ள நாள் நவம்பர் 26, 1949 ஆகும், இது ஆண்டுதோறும் தேசிய அரசியலமைப்பு தினமாக (சம்விதான் திவாஸ்) கொண்டாடப்படுகிறது."
        },
        "source_reference": [
            "Text of the Constitution of India (Preamble)",
            "M. Laxmikanth - Indian Polity"
        ],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "Four Ingredients", "Structural Sequence", "Constitution Day"],
        "question_en": "Arrange the four core ingredients of the Preamble in the exact sequential order as they appear from beginning to end in the constitutional text:\n1. Source of Authority of the Constitution ('WE, THE PEOPLE OF INDIA')\n2. Nature of the Indian State ('SOVEREIGN SOCIALIST SECULAR DEMOCRATIC REPUBLIC')\n3. Statement of Constitutional Objectives ('JUSTICE, LIBERTY, EQUALITY, FRATERNITY')\n4. Date of Adoption and Enactment ('twenty-sixth day of November, 1949')",
        "question_ta": "அரசியலமைப்பு உரையில் தொடக்கத்திலிருந்து இறுதி வரை காணப்படும் நான்கு முக்கிய கூறுகளை சரியான வரிசையில் அமைக்கவும்:\n1. அரசியலமைப்பு அதிகாரத்தின் மூலம் ('இந்திய மக்களாகிய நாம்')\n2. இந்திய அரசின் தன்மை ('இறையாண்மை சமதர்ம மதச்சார்பற்ற ஜனநாயக குடியரசு')\n3. அரசியலமைப்பு இலக்குகளின் பிரகடனம் ('நீதி, சுதந்திரம், சமத்துவம், சகோதரத்துவம்')\n4. ஏற்றுக்கொள்ளப்பட்டு இயற்றப்பட்ட நாள் ('நவம்பர் இருபத்தாறாம் நாள், 1949')",
        "options_en": ["1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "1 -> 2 -> 4 -> 3"],
        "options_ta": ["1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "1 -> 2 -> 4 -> 3"],
        "answer": "a",
        "explanation_en": "Structural Sequence of Preamble: 1 (Source of Authority: 'We, the People...') -> 2 (Nature of State: 'Sovereign Socialist...') -> 3 (Objectives: 'Justice, Liberty...') -> 4 (Date of Adoption: '26th November 1949').",
        "explanation_ta": "முகவுரையின் கட்டமைப்பு வரிசை: 1 (அதிகார மூலம்: 'இந்திய மக்களாகிய நாம்...') -> 2 (அரசின் தன்மை: 'இறையாண்மை சமதர்ம...') -> 3 (இலக்குகள்: 'நீதி, சுதந்திரம்...') -> 4 (ஏற்றுக்கொள்ளப்பட்ட நாள்: '26 நவம்பர் 1949')."
    },

    # -------------------------------------------------------------------------
    # Q18: PRE_CHRONO_018
    # -------------------------------------------------------------------------
    {
        "id": "PRE_CHRONO_018",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Chronology",
        "question": {
            "en": "Arrange the following developments regarding the power of Parliament to amend the Constitution (Article 368) vis-a-vis the Preamble in correct chronological order:\n1. Supreme Court holds that Preamble is neither a source of power nor a limitation on legislative powers (Berubari)\n2. Parliament enacts the 24th Constitutional Amendment Act clarifying its constituent power under Article 368\n3. Supreme Court upholds Article 368 power to amend Preamble subject to Basic Structure (Kesavananda Bharati)\n4. Parliament amends the Preamble for the first and only time by passing the 42nd Amendment Act",
            "ta": "முகவுரை மற்றும் அரசியலமைப்பைத் திருத்துவதற்கான நாடாளுமன்றத்தின் அதிகாரம் (உறுப்பு 368) தொடர்பான பின்வரும் முன்னேற்றங்களை சரியான காலவரிசையில் அமைக்கவும்:\n1. முகவுரை சட்டமன்றத்திற்கு அதிகார மூலமும் அல்ல, அதிகாரத்தின் மீதான வரம்பும் அல்ல என உச்ச நீதிமன்றம் தீர்ப்பளித்தல் (பெருபாரி)\n2. உறுப்பு 368-ன் கீழ் தனது அரசியலமைப்பு அதிகாரத்தை தெளிவுபடுத்தி நாடாளுமன்றம் 24வது அரசியலமைப்புத் திருத்தச் சட்டத்தை இயற்றுதல்\n3. அடிப்படை கட்டமைப்புக்கு உட்பட்டு முகவுரையைத் திருத்த உறுப்பு 368 அதிகாரம் அளிக்கிறது என உச்ச நீதிமன்றம் உறுதி செய்தல் (கேசவானந்த பாரதி)\n4. 42வது திருத்தச் சட்டத்தை நிறைவேற்றி நாடாளுமன்றம் முதன்முறையாகவும் ஒரே முறையாகவும் முகவுரையைத் திருத்துதல்"
        },
        "events": [
            {
                "id": "1",
                "en": "Supreme Court holds that Preamble is neither a source of power nor a limitation on legislative powers (Berubari)",
                "ta": "முகவுரை சட்டமன்றத்திற்கு அதிகார மூலமும் அல்ல, அதிகாரத்தின் மீதான வரம்பும் அல்ல என உச்ச நீதிமன்றம் தீர்ப்பளித்தல் (பெருபாரி)"
            },
            {
                "id": "2",
                "en": "Parliament enacts the 24th Constitutional Amendment Act clarifying its constituent power under Article 368",
                "ta": "உறுப்பு 368-ன் கீழ் தனது அரசியலமைப்பு அதிகாரத்தை தெளிவுபடுத்தி நாடாளுமன்றம் 24வது அரசியலமைப்புத் திருத்தச் சட்டத்தை இயற்றுதல்"
            },
            {
                "id": "3",
                "en": "Supreme Court upholds Article 368 power to amend Preamble subject to Basic Structure (Kesavananda Bharati)",
                "ta": "அடிப்படை கட்டமைப்புக்கு உட்பட்டு முகவுரையைத் திருத்த உறுப்பு 368 அதிகாரம் அளிக்கிறது என உச்ச நீதிமன்றம் உறுதி செய்தல் (கேசவானந்த பாரதி)"
            },
            {
                "id": "4",
                "en": "Parliament amends the Preamble for the first and only time by passing the 42nd Amendment Act",
                "ta": "42வது திருத்தச் சட்டத்தை நிறைவேற்றி நாடாளுமன்றம் முதன்முறையாகவும் ஒரே முறையாகவும் முகவுரையைத் திருத்துதல்"
            }
        ],
        "options": [
            {"id": "A", "en": "1 -> 3 -> 2 -> 4", "ta": "1 -> 3 -> 2 -> 4"},
            {"id": "B", "en": "1 -> 2 -> 3 -> 4", "ta": "1 -> 2 -> 3 -> 4"},
            {"id": "C", "en": "2 -> 1 -> 3 -> 4", "ta": "2 -> 1 -> 3 -> 4"},
            {"id": "D", "en": "1 -> 2 -> 4 -> 3", "ta": "1 -> 2 -> 4 -> 3"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "Chronological Sequence: 1 (Berubari: 1960) -> 2 (24th Amendment: 1971) -> 3 (Kesavananda Bharati: 1973) -> 4 (42nd Amendment: 1976).",
            "ta": "சரியான காலவரிசை: 1 (பெருபாரி: 1960) -> 2 (24வது திருத்தம்: 1971) -> 3 (கேசவானந்த பாரதி: 1973) -> 4 (42வது திருத்தம்: 1976)."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. 24th Amendment (1971) was enacted before Kesavananda Bharati was decided in 1973.", "ta": "தவறு. 24வது திருத்தம் (1971) கேசவானந்த பாரதி தீர்ப்பிற்கு (1973) முன்பாக இயற்றப்பட்டது."},
            "B": {"en": "Correct. 1 (1960) -> 2 (1971) -> 3 (1973) -> 4 (1976) reflects the exact constitutional and legislative timeline.", "ta": "சரி. 1 (1960) -> 2 (1971) -> 3 (1973) -> 4 (1976) துல்லியமான அரசியலமைப்பு மற்றும் சட்ட காலவரிசையைப் பிரதிபலிக்கிறது."},
            "C": {"en": "Incorrect. Berubari (1960) came before the 24th Amendment (1971).", "ta": "தவறு. பெருபாரி (1960) 24வது திருத்தத்திற்கு (1971) முந்தையது."},
            "D": {"en": "Incorrect. 42nd Amendment in 1976 (4) followed Kesavananda Bharati in 1973 (3).", "ta": "தவறு. 1976-ன் 42வது திருத்தம் (4) 1973-ன் கேசவானந்த பாரதிக்கு (3) பின்னரே வந்தது."}
        },
        "tnpsc_tip": {
            "en": "TNPSC Connection: 24th Amendment (1971) made it obligatory for the President to give assent to constitutional amendment bills; Kesavananda Bharati (1973) upheld the 24th Amendment while introducing the Basic Structure limitation.",
            "ta": "TNPSC இணைப்பு: 24வது திருத்தம் (1971) அரசியலமைப்பு திருத்த மசோதாக்களுக்கு குடியரசுத் தலைவர் ஒப்புதல் அளிப்பதைக் கட்டாயமாக்கியது; கேசவானந்த பாரதி (1973) 24வது திருத்தத்தை உறுதி செய்து அடிப்படை கட்டமைப்பு வரம்பை அறிமுகப்படுத்தியது."
        },
        "revision_fact": {
            "en": "Article 368 is contained in Part XX of the Indian Constitution, titled 'Amendment of the Constitution'.",
            "ta": "உறுப்பு 368 இந்திய அரசியலமைப்பின் பகுதி XX இல் 'அரசியலமைப்பின் திருத்தம்' என்ற தலைப்பின் கீழ் அமைந்துள்ளது."
        },
        "source_reference": [
            "M. Laxmikanth - Indian Polity (Amendment of the Constitution)",
            "DD Basu - Introduction to the Constitution of India"
        ],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "Article 368", "24th Amendment", "42nd Amendment", "Amendability"],
        "question_en": "Arrange the following developments regarding the power of Parliament to amend the Constitution (Article 368) vis-a-vis the Preamble in correct chronological order:\n1. Supreme Court holds that Preamble is neither a source of power nor a limitation on legislative powers (Berubari)\n2. Parliament enacts the 24th Constitutional Amendment Act clarifying its constituent power under Article 368\n3. Supreme Court upholds Article 368 power to amend Preamble subject to Basic Structure (Kesavananda Bharati)\n4. Parliament amends the Preamble for the first and only time by passing the 42nd Amendment Act",
        "question_ta": "முகவுரை மற்றும் அரசியலமைப்பைத் திருத்துவதற்கான நாடாளுமன்றத்தின் அதிகாரம் (உறுப்பு 368) தொடர்பான பின்வரும் முன்னேற்றங்களை சரியான காலவரிசையில் அமைக்கவும்:\n1. முகவுரை சட்டமன்றத்திற்கு அதிகார மூலமும் அல்ல, அதிகாரத்தின் மீதான வரம்பும் அல்ல என உச்ச நீதிமன்றம் தீர்ப்பளித்தல் (பெருபாரி)\n2. உறுப்பு 368-ன் கீழ் தனது அரசியலமைப்பு அதிகாரத்தை தெளிவுபடுத்தி நாடாளுமன்றம் 24வது அரசியலமைப்புத் திருத்தச் சட்டத்தை இயற்றுதல்\n3. அடிப்படை கட்டமைப்புக்கு உட்பட்டு முகவுரையைத் திருத்த உறுப்பு 368 அதிகாரம் அளிக்கிறது என உச்ச நீதிமன்றம் உறுதி செய்தல் (கேசவானந்த பாரதி)\n4. 42வது திருத்தச் சட்டத்தை நிறைவேற்றி நாடாளுமன்றம் முதன்முறையாகவும் ஒரே முறையாகவும் முகவுரையைத் திருத்துதல்",
        "options_en": ["1 -> 3 -> 2 -> 4", "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 2 -> 4 -> 3"],
        "options_ta": ["1 -> 3 -> 2 -> 4", "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 2 -> 4 -> 3"],
        "answer": "b",
        "explanation_en": "Chronological Sequence: 1 (Berubari: 1960) -> 2 (24th Amendment: 1971) -> 3 (Kesavananda Bharati: 1973) -> 4 (42nd Amendment: 1976).",
        "explanation_ta": "சரியான காலவரிசை: 1 (பெருபாரி: 1960) -> 2 (24வது திருத்தம்: 1971) -> 3 (கேசவானந்த பாரதி: 1973) -> 4 (42வது திருத்தம்: 1976)."
    },

    # -------------------------------------------------------------------------
    # Q19: PRE_CHRONO_019 (TNPSC Trap: Detailed Dates)
    # -------------------------------------------------------------------------
    {
        "id": "PRE_CHRONO_019",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Chronology",
        "question": {
            "en": "Arrange the following four specific calendar dates related to the evolution and enactment of the Preamble and Constitution in exact chronological order:\n1. December 13, 1946: Jawaharlal Nehru moves the Objectives Resolution\n2. January 22, 1947: Constituent Assembly adopts the Objectives Resolution\n3. November 26, 1949: Constitution and Preamble are adopted and enacted\n4. January 26, 1950: Constitution and Preamble come into full commencement",
            "ta": "முகவுரை மற்றும் அரசியலமைப்பின் உருவாக்கம் தொடர்பான பின்வரும் நான்கு குறிப்பிட்ட தேதிகளை சரியான காலவரிசையில் அமைக்கவும்:\n1. டிசம்பர் 13, 1946: ஜவஹர்லால் நேரு குறிக்கோள் தீர்மானத்தை முன்மொழிகிறார்\n2. ஜனவரி 22, 1947: அரசியலமைப்பு நிர்ணய அவை குறிக்கோள் தீர்மானத்தை ஏற்றுக்கொள்கிறது\n3. நவம்பர் 26, 1949: அரசியலமைப்பு மற்றும் முகவுரை ஏற்றுக்கொள்ளப்பட்டு இயற்றப்படுகிறது\n4. ஜனவரி 26, 1950: அரசியலமைப்பு மற்றும் முகவுரை முழுமையாக நடைமுறைக்கு வருகிறது"
        },
        "events": [
            {
                "id": "1",
                "en": "December 13, 1946: Jawaharlal Nehru moves the Objectives Resolution",
                "ta": "டிசம்பர் 13, 1946: ஜவஹர்லால் நேரு குறிக்கோள் தீர்மானத்தை முன்மொழிகிறார்"
            },
            {
                "id": "2",
                "en": "January 22, 1947: Constituent Assembly adopts the Objectives Resolution",
                "ta": "ஜனவரி 22, 1947: அரசியலமைப்பு நிர்ணய அவை குறிக்கோள் தீர்மானத்தை ஏற்றுக்கொள்கிறது"
            },
            {
                "id": "3",
                "en": "November 26, 1949: Constitution and Preamble are adopted and enacted",
                "ta": "நவம்பர் 26, 1949: அரசியலமைப்பு மற்றும் முகவுரை ஏற்றுக்கொள்ளப்பட்டு இயற்றப்படுகிறது"
            },
            {
                "id": "4",
                "en": "January 26, 1950: Constitution and Preamble come into full commencement",
                "ta": "ஜனவரி 26, 1950: அரசியலமைப்பு மற்றும் முகவுரை முழுமையாக நடைமுறைக்கு வருகிறது"
            }
        ],
        "options": [
            {"id": "A", "en": "2 -> 1 -> 3 -> 4", "ta": "2 -> 1 -> 3 -> 4"},
            {"id": "B", "en": "1 -> 3 -> 2 -> 4", "ta": "1 -> 3 -> 2 -> 4"},
            {"id": "C", "en": "1 -> 2 -> 3 -> 4", "ta": "1 -> 2 -> 3 -> 4"},
            {"id": "D", "en": "1 -> 2 -> 4 -> 3", "ta": "1 -> 2 -> 4 -> 3"}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "Exact Date Sequence: 1 (Dec 13, 1946) -> 2 (Jan 22, 1947) -> 3 (Nov 26, 1949) -> 4 (Jan 26, 1950).",
            "ta": "துல்லியமான தேதி வரிசை: 1 (டிசம்பர் 13, 1946) -> 2 (ஜனவரி 22, 1947) -> 3 (நவம்பர் 26, 1949) -> 4 (ஜனவரி 26, 1950)."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Moving the resolution (Dec 13, 1946) came before its adoption (Jan 22, 1947).", "ta": "தவறு. தீர்மானத்தை முன்மொழிந்தது (டிசம்பர் 13, 1946) அது ஏற்றுக்கொள்ளப்பட்டதற்கு (ஜனவரி 22, 1947) முந்தையது."},
            "B": {"en": "Incorrect. Jan 22, 1947 (2) preceded Nov 26, 1949 (3).", "ta": "தவறு. ஜனவரி 22, 1947 (2) நவம்பர் 26, 1949-க்கு (3) முந்தையது."},
            "C": {"en": "Correct. Dec 13, 1946 -> Jan 22, 1947 -> Nov 26, 1949 -> Jan 26, 1950 is the exact chronological date sequence.", "ta": "சரி. டிசம்பர் 13, 1946 -> ஜனவரி 22, 1947 -> நவம்பர் 26, 1949 -> ஜனவரி 26, 1950 துல்லியமான காலவரிசைத் தேதிகள்."},
            "D": {"en": "Incorrect. Adoption date (Nov 26, 1949) preceded commencement date (Jan 26, 1950).", "ta": "தவறு. ஏற்றுக்கொள்ளப்பட்ட நாள் (நவம்பர் 26, 1949) நடைமுறைக்கு வந்த நாளுக்கு (ஜனவரி 26, 1950) முந்தையது."}
        },
        "tnpsc_tip": {
            "en": "TNPSC Trap: Candidates frequently mix up Dec 13, 1946 (Moved) and Jan 22, 1947 (Adopted), as well as Nov 26, 1949 (Adopted) and Jan 26, 1950 (Commenced).",
            "ta": "TNPSC பொறி: டிசம்பர் 13, 1946 (முன்மொழியப்பட்டது) மற்றும் ஜனவரி 22, 1947 (ஏற்கப்பட்டது) ஆகியவற்றையும், நவம்பர் 26, 1949 (ஏற்கப்பட்டது) மற்றும் ஜனவரி 26, 1950 (அமலானது) ஆகியவற்றையும் தேர்வர்கள் அடிக்கடி குழப்பிக் கொள்வர்."
        },
        "revision_fact": {
            "en": "January 26 was specifically chosen as the Commencement Day because on that day in 1930, Purna Swaraj Day was celebrated following the Lahore Session of the INC (1929).",
            "ta": "1929 லாகூர் காங்கிரஸ் மாநாட்டைத் தொடர்ந்து 1930 இல் 'பூரண சுயராஜ்ய தினம்' கொண்டாடப்பட்டதன் நினைவாகவே ஜனவரி 26 நடைமுறை நாளாகத் தேர்ந்தெடுக்கப்பட்டது."
        },
        "source_reference": [
            "M. Laxmikanth - Indian Polity",
            "NCERT Class XI - Indian Constitution at Work",
            "Constituent Assembly Debates"
        ],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "Key Dates", "Objectives Resolution", "Adoption vs Commencement"],
        "question_en": "Arrange the following four specific calendar dates related to the evolution and enactment of the Preamble and Constitution in exact chronological order:\n1. December 13, 1946: Jawaharlal Nehru moves the Objectives Resolution\n2. January 22, 1947: Constituent Assembly adopts the Objectives Resolution\n3. November 26, 1949: Constitution and Preamble are adopted and enacted\n4. January 26, 1950: Constitution and Preamble come into full commencement",
        "question_ta": "முகவுரை மற்றும் அரசியலமைப்பின் உருவாக்கம் தொடர்பான பின்வரும் நான்கு குறிப்பிட்ட தேதிகளை சரியான காலவரிசையில் அமைக்கவும்:\n1. டிசம்பர் 13, 1946: ஜவஹர்லால் நேரு குறிக்கோள் தீர்மானத்தை முன்மொழிகிறார்\n2. ஜனவரி 22, 1947: அரசியலமைப்பு நிர்ணய அவை குறிக்கோள் தீர்மானத்தை ஏற்றுக்கொள்கிறது\n3. நவம்பர் 26, 1949: அரசியலமைப்பு மற்றும் முகவுரை ஏற்றுக்கொள்ளப்பட்டு இயற்றப்படுகிறது\n4. ஜனவரி 26, 1950: அரசியலமைப்பு மற்றும் முகவுரை முழுமையாக நடைமுறைக்கு வருகிறது",
        "options_en": ["2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "1 -> 2 -> 3 -> 4", "1 -> 2 -> 4 -> 3"],
        "options_ta": ["2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "1 -> 2 -> 3 -> 4", "1 -> 2 -> 4 -> 3"],
        "answer": "c",
        "explanation_en": "Exact Date Sequence: 1 (Dec 13, 1946) -> 2 (Jan 22, 1947) -> 3 (Nov 26, 1949) -> 4 (Jan 26, 1950).",
        "explanation_ta": "துல்லியமான தேதி வரிசை: 1 (டிசம்பர் 13, 1946) -> 2 (ஜனவரி 22, 1947) -> 3 (நவம்பர் 26, 1949) -> 4 (ஜனவரி 26, 1950)."
    },

    # -------------------------------------------------------------------------
    # Q20: PRE_CHRONO_020
    # -------------------------------------------------------------------------
    {
        "id": "PRE_CHRONO_020",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Chronology",
        "question": {
            "en": "Arrange the following landmark Supreme Court cases citing and interpreting the Preamble in correct chronological order:\n1. In re Berubari Union Case\n2. Kesavananda Bharati v. State of Kerala\n3. Maneka Gandhi v. Union of India\n4. LIC of India v. Consumer Education and Research Centre",
            "ta": "முகவுரையை மேற்கோள் காட்டி விளக்கிய உச்ச நீதிமன்றத்தின் பின்வரும் முக்கிய வழக்குகளை சரியான காலவரிசையில் அமைக்கவும்:\n1. பெருபாரி யூனியன் வழக்கு (In re Berubari Union)\n2. கேசவானந்த பாரதி எதிர் கேரள அரசு (Kesavananda Bharati v. State of Kerala)\n3. மேனகா காந்தி எதிர் இந்திய யூனியன் (Maneka Gandhi v. Union of India)\n4. எல்.ஐ.சி எதிர் நுகர்வோர் கல்வி மற்றும் ஆராய்ச்சி மையம் (LIC of India v. CERC)",
        },
        "events": [
            {
                "id": "1",
                "en": "In re Berubari Union Case",
                "ta": "பெருபாரி யூனியன் வழக்கு"
            },
            {
                "id": "2",
                "en": "Kesavananda Bharati v. State of Kerala",
                "ta": "கேசவானந்த பாரதி எதிர் கேரள அரசு"
            },
            {
                "id": "3",
                "en": "Maneka Gandhi v. Union of India",
                "ta": "மேனகா காந்தி எதிர் இந்திய யூனியன்"
            },
            {
                "id": "4",
                "en": "LIC of India v. Consumer Education and Research Centre",
                "ta": "எல்.ஐ.சி எதிர் நுகர்வோர் கல்வி மற்றும் ஆராய்ச்சி மையம்"
            }
        ],
        "options": [
            {"id": "A", "en": "2 -> 1 -> 3 -> 4", "ta": "2 -> 1 -> 3 -> 4"},
            {"id": "B", "en": "1 -> 3 -> 2 -> 4", "ta": "1 -> 3 -> 2 -> 4"},
            {"id": "C", "en": "1 -> 2 -> 4 -> 3", "ta": "1 -> 2 -> 4 -> 3"},
            {"id": "D", "en": "1 -> 2 -> 3 -> 4", "ta": "1 -> 2 -> 3 -> 4"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "Chronological Sequence: 1 (Berubari Union: 1960) -> 2 (Kesavananda Bharati: 1973) -> 3 (Maneka Gandhi: 1978) -> 4 (LIC of India: 1995).",
            "ta": "சரியான காலவரிசை: 1 (பெருபாரி யூனியன்: 1960) -> 2 (கேசவானந்த பாரதி: 1973) -> 3 (மேனகா காந்தி: 1978) -> 4 (எல்ஐசி வழக்கு: 1995)."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Berubari (1960) preceded Kesavananda Bharati (1973).", "ta": "தவறு. பெருபாரி (1960) கேசவானந்த பாரதிக்கு (1973) முந்தையது."},
            "B": {"en": "Incorrect. Kesavananda Bharati (1973) preceded Maneka Gandhi (1978).", "ta": "தவறு. கேசவானந்த பாரதி (1973) மேனகா காந்திக்கு (1978) முந்தையது."},
            "C": {"en": "Incorrect. Maneka Gandhi (1978) came before LIC of India (1995).", "ta": "தவறு. மேனகா காந்தி (1978) எல்ஐசி வழக்குக்கு (1995) முந்தையது."},
            "D": {"en": "Correct. 1 (1960) -> 2 (1973) -> 3 (1978) -> 4 (1995) is the accurate chronological order.", "ta": "சரி. 1 (1960) -> 2 (1973) -> 3 (1978) -> 4 (1995) துல்லியமான காலவரிசையாகும்."}
        },
        "tnpsc_tip": {
            "en": "Case Bench Size Tip: Berubari (8 judges), Kesavananda (13 judges - largest ever), Bommai (9 judges).",
            "ta": "நீதிபதிகள் அமர்வு அளவு: பெருபாரி (8 நீதிபதிகள்), கேசவானந்தா (13 நீதிபதிகள் - வரலாற்றிலேயே மிகப்பெரியது), பொம்மை (9 நீதிபதிகள்)."
        },
        "revision_fact": {
            "en": "The Kesavananda Bharati decision was delivered by a wafer-thin 7-6 majority on April 24, 1973.",
            "ta": "கேசவானந்த பாரதி தீர்ப்பு ஏப்ரல் 24, 1973 அன்று மிகக் குறுகிய 7-6 பெரும்பான்மையில் வழங்கப்பட்டது."
        },
        "source_reference": [
            "M. Laxmikanth - Indian Polity",
            "Supreme Court Law Reports"
        ],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "Case Chronology", "Judicial Precedents"],
        "question_en": "Arrange the following landmark Supreme Court cases citing and interpreting the Preamble in correct chronological order:\n1. In re Berubari Union Case\n2. Kesavananda Bharati v. State of Kerala\n3. Maneka Gandhi v. Union of India\n4. LIC of India v. Consumer Education and Research Centre",
        "question_ta": "முகவுரையை மேற்கோள் காட்டி விளக்கிய உச்ச நீதிமன்றத்தின் பின்வரும் முக்கிய வழக்குகளை சரியான காலவரிசையில் அமைக்கவும்:\n1. பெருபாரி யூனியன் வழக்கு (In re Berubari Union)\n2. கேசவானந்த பாரதி எதிர் கேரள அரசு (Kesavananda Bharati v. State of Kerala)\n3. மேனகா காந்தி எதிர் இந்திய யூனியன் (Maneka Gandhi v. Union of India)\n4. எல்.ஐ.சி எதிர் நுகர்வோர் கல்வி மற்றும் ஆராய்ச்சி மையம் (LIC of India v. CERC)",
        "options_en": ["2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "1 -> 2 -> 4 -> 3", "1 -> 2 -> 3 -> 4"],
        "options_ta": ["2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "1 -> 2 -> 4 -> 3", "1 -> 2 -> 3 -> 4"],
        "answer": "d",
        "explanation_en": "Chronological Sequence: 1 (Berubari Union: 1960) -> 2 (Kesavananda Bharati: 1973) -> 3 (Maneka Gandhi: 1978) -> 4 (LIC of India: 1995).",
        "explanation_ta": "சரியான காலவரிசை: 1 (பெருபாரி யூனியன்: 1960) -> 2 (கேசவானந்த பாரதி: 1973) -> 3 (மேனகா காந்தி: 1978) -> 4 (எல்ஐசி வழக்கு: 1995)."
    },

    # -------------------------------------------------------------------------
    # Q21: PRE_CHRONO_021
    # -------------------------------------------------------------------------
    {
        "id": "PRE_CHRONO_021",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Chronology",
        "question": {
            "en": "Arrange the following sub-clauses of 'EQUALITY' and 'FRATERNITY' in the exact textual sequence as they appear in the Preamble:\n1. Equality of status\n2. Equality of opportunity\n3. Fraternity assuring the dignity of the individual\n4. Fraternity assuring the unity and integrity of the Nation",
            "ta": "முகவுரையில் இடம்பெற்றுள்ளவாறு 'சமத்துவம்' மற்றும் 'சகோதரத்துவம்' ஆகியவற்றின் பின்வரும் உட்பிரிவுகளை சரியான உரை வரிசையில் அமைக்கவும்:\n1. தகுதி சமத்துவம் (Status)\n2. வாய்ப்பு சமத்துவம் (Opportunity)\n3. தனிமனித கண்ணியத்தை உறுதிப்படுத்தும் சகோதரத்துவம் (Dignity of the individual)\n4. தேசத்தின் ஒற்றுமையையும் ஒருமைப்பாட்டையும் உறுதிப்படுத்தும் சகோதரத்துவம் (Unity and integrity of the Nation)"
        },
        "events": [
            {
                "id": "1",
                "en": "Equality of status",
                "ta": "தகுதி சமத்துவம்"
            },
            {
                "id": "2",
                "en": "Equality of opportunity",
                "ta": "வாய்ப்பு சமத்துவம்"
            },
            {
                "id": "3",
                "en": "Fraternity assuring the dignity of the individual",
                "ta": "தனிமனித கண்ணியத்தை உறுதிப்படுத்தும் சகோதரத்துவம்"
            },
            {
                "id": "4",
                "en": "Fraternity assuring the unity and integrity of the Nation",
                "ta": "தேசத்தின் ஒற்றுமையையும் ஒருமைப்பாட்டையும் உறுதிப்படுத்தும் சகோதரத்துவம்"
            }
        ],
        "options": [
            {"id": "A", "en": "1 -> 2 -> 3 -> 4", "ta": "1 -> 2 -> 3 -> 4"},
            {"id": "B", "en": "2 -> 1 -> 3 -> 4", "ta": "2 -> 1 -> 3 -> 4"},
            {"id": "C", "en": "1 -> 2 -> 4 -> 3", "ta": "1 -> 2 -> 4 -> 3"},
            {"id": "D", "en": "3 -> 4 -> 1 -> 2", "ta": "3 -> 4 -> 1 -> 2"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Textual Sequence in Preamble: 'EQUALITY of status and of opportunity; and to promote among them all FRATERNITY assuring the dignity of the individual and the unity and integrity of the Nation;'. Hence, 1 -> 2 -> 3 -> 4.",
            "ta": "முகவுரையின் உரை வரிசை: 'தகுதி மற்றும் வாய்ப்பு சமத்துவம்; மற்றும் அவர்கள் அனைவரிடையேயும் தனிமனித கண்ணியத்தையும், தேசத்தின் ஒற்றுமையையும் ஒருமைப்பாட்டையும் உறுதிப்படுத்தும் சகோதரத்துவம்;'. எனவே, 1 -> 2 -> 3 -> 4."
        },
        "why_not_others": {
            "A": {"en": "Correct. 1 (Status) -> 2 (Opportunity) -> 3 (Dignity of individual) -> 4 (Unity and integrity) exactly follows the text.", "ta": "சரி. 1 (தகுதி) -> 2 (வாய்ப்பு) -> 3 (தனிமனித கண்ணியம்) -> 4 (ஒற்றுமை மற்றும் ஒருமைப்பாடு) உரையைத் துல்லியமாகப் பின்பற்றுகிறது."},
            "B": {"en": "Incorrect. Equality of status precedes Equality of opportunity.", "ta": "தவறு. வாய்ப்பு சமத்துவத்திற்கு முன்பாக தகுதி சமத்துவம் வருகிறது."},
            "C": {"en": "Incorrect. Dignity of the individual precedes unity and integrity of the Nation.", "ta": "தவறு. தேசத்தின் ஒற்றுமைக்கு முன்பாக தனிமனித கண்ணியம் வருகிறது."},
            "D": {"en": "Incorrect. Equality clauses precede Fraternity clauses in the Preamble.", "ta": "தவறு. முகவுரையில் சகோதரத்துவத்திற்கு முன்பாக சமத்துவ வாசகங்கள் வருகின்றன."}
        },
        "tnpsc_tip": {
            "en": "TNPSC Phrasing Trap: Equality has TWO dimensions (Status, Opportunity); Fraternity assures TWO things (Dignity of Individual, Unity and Integrity of Nation).",
            "ta": "TNPSC உரைப் பொறி: சமத்துவம் இரண்டு பரிமாணங்களைக் கொண்டது (தகுதி, வாய்ப்பு); சகோதரத்துவம் இரண்டு காரியங்களை உறுதிப்படுத்துகிறது (தனிமனித கண்ணியம், தேசத்தின் ஒற்றுமையும் ஒருமைப்பாடும்)."
        },
        "revision_fact": {
            "en": "Equality of status and opportunity is practically realized through Article 14 (Equality before Law), Article 15 (Prohibition of Discrimination), Article 16 (Equal Opportunity in Public Employment), Article 17 (Abolition of Untouchability), and Article 18 (Abolition of Titles).",
            "ta": "தகுதி மற்றும் வாய்ப்பு சமத்துவம் உறுப்புகள் 14, 15, 16, 17 மற்றும் 18 ஆகியவற்றின் மூலம் நடைமுறையில் உறுதி செய்யப்படுகிறது."
        },
        "source_reference": [
            "Text of the Constitution of India (Preamble)",
            "M. Laxmikanth - Indian Polity"
        ],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "Equality", "Fraternity", "Textual Sequence"],
        "question_en": "Arrange the following sub-clauses of 'EQUALITY' and 'FRATERNITY' in the exact textual sequence as they appear in the Preamble:\n1. Equality of status\n2. Equality of opportunity\n3. Fraternity assuring the dignity of the individual\n4. Fraternity assuring the unity and integrity of the Nation",
        "question_ta": "முகவுரையில் இடம்பெற்றுள்ளவாறு 'சமத்துவம்' மற்றும் 'சகோதரத்துவம்' ஆகியவற்றின் பின்வரும் உட்பிரிவுகளை சரியான உரை வரிசையில் அமைக்கவும்:\n1. தகுதி சமத்துவம் (Status)\n2. வாய்ப்பு சமத்துவம் (Opportunity)\n3. தனிமனித கண்ணியத்தை உறுதிப்படுத்தும் சகோதரத்துவம் (Dignity of the individual)\n4. தேசத்தின் ஒற்றுமையையும் ஒருமைப்பாட்டையும் உறுதிப்படுத்தும் சகோதரத்துவம் (Unity and integrity of the Nation)",
        "options_en": ["1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 2 -> 4 -> 3", "3 -> 4 -> 1 -> 2"],
        "options_ta": ["1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 2 -> 4 -> 3", "3 -> 4 -> 1 -> 2"],
        "answer": "a",
        "explanation_en": "Textual Sequence in Preamble: 'EQUALITY of status and of opportunity; and to promote among them all FRATERNITY assuring the dignity of the individual and the unity and integrity of the Nation;'. Hence, 1 -> 2 -> 3 -> 4.",
        "explanation_ta": "முகவுரையின் உரை வரிசை: 'தகுதி மற்றும் வாய்ப்பு சமத்துவம்; மற்றும் அவர்கள் அனைவரிடையேயும் தனிமனித கண்ணியத்தையும், தேசத்தின் ஒற்றுமையையும் ஒருமைப்பாட்டையும் உறுதிப்படுத்தும் சகோதரத்துவம்;'. எனவே, 1 -> 2 -> 3 -> 4."
    },

    # -------------------------------------------------------------------------
    # Q22: PRE_CHRONO_022
    # -------------------------------------------------------------------------
    {
        "id": "PRE_CHRONO_022",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Chronology",
        "question": {
            "en": "Arrange the following chronological stages in the legislative enactment and implementation of the 42nd Constitutional Amendment Act affecting the Preamble:\n1. Swaran Singh Committee submits its recommendations on constitutional amendments\n2. 42nd Constitutional Amendment Bill is passed by both Houses of Parliament\n3. President of India gives assent to the 42nd Constitutional Amendment Act\n4. Provisions of the 42nd Amendment amending the Preamble are brought into force",
            "ta": "முகவுரையைத் திருத்திய 42வது அரசியலமைப்புத் திருத்தச் சட்டத்தின் சட்டமியற்றல் மற்றும் நடைமுறைப்படுத்தலின் பின்வரும் காலவரிசை நிலைகளை அமைக்கவும்:\n1. ஸ்வரன் சிங் குழு அரசியலமைப்பு திருத்தங்கள் குறித்த தனது பரிந்துரைகளைச் சமர்ப்பித்தல்\n2. 42வது அரசியலமைப்புத் திருத்த மசோதா நாடாளுமன்றத்தின் இரு அவைகளாலும் நிறைவேற்றப்படுதல்\n3. இந்தியக் குடியரசுத் தலைவர் 42வது அரசியலமைப்புத் திருத்தச் சட்டத்திற்கு ஒப்புதல் அளித்தல்\n4. முகவுரையைத் திருத்திய 42வது திருத்தத்தின் விதிகள் அதிகாரப்பூர்வமாக நடைமுறைக்குக் கொண்டுவரப்படுதல்"
        },
        "events": [
            {
                "id": "1",
                "en": "Swaran Singh Committee submits its recommendations on constitutional amendments",
                "ta": "ஸ்வரன் சிங் குழு அரசியலமைப்பு திருத்தங்கள் குறித்த தனது பரிந்துரைகளைச் சமர்ப்பித்தல்"
            },
            {
                "id": "2",
                "en": "42nd Constitutional Amendment Bill is passed by both Houses of Parliament",
                "ta": "42வது அரசியலமைப்புத் திருத்த மசோதா நாடாளுமன்றத்தின் இரு அவைகளாலும் நிறைவேற்றப்படுதல்"
            },
            {
                "id": "3",
                "en": "President of India gives assent to the 42nd Constitutional Amendment Act",
                "ta": "இந்தியக் குடியரசுத் தலைவர் 42வது அரசியலமைப்புத் திருத்தச் சட்டத்திற்கு ஒப்புதல் அளித்தல்"
            },
            {
                "id": "4",
                "en": "Provisions of the 42nd Amendment amending the Preamble are brought into force",
                "ta": "முகவுரையைத் திருத்திய 42வது திருத்தத்தின் விதிகள் அதிகாரப்பூர்வமாக நடைமுறைக்குக் கொண்டுவரப்படுதல்"
            }
        ],
        "options": [
            {"id": "A", "en": "2 -> 1 -> 3 -> 4", "ta": "2 -> 1 -> 3 -> 4"},
            {"id": "B", "en": "1 -> 2 -> 3 -> 4", "ta": "1 -> 2 -> 3 -> 4"},
            {"id": "C", "en": "1 -> 3 -> 2 -> 4", "ta": "1 -> 3 -> 2 -> 4"},
            {"id": "D", "en": "1 -> 2 -> 4 -> 3", "ta": "1 -> 2 -> 4 -> 3"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "Chronological Sequence: 1 (Swaran Singh Report: May 1976) -> 2 (Parliament passage: Nov 1976) -> 3 (Presidential assent: Dec 18, 1976) -> 4 (Enforcement: Jan 3, 1977).",
            "ta": "சரியான காலவரிசை: 1 (ஸ்வரன் சிங் அறிக்கை: மே 1976) -> 2 (நாடாளுமன்ற நிறைவேற்றம்: நவம்பர் 1976) -> 3 (குடியரசுத் தலைவர் ஒப்புதல்: டிசம்பர் 18, 1976) -> 4 (அமலாக்கம்: ஜனவரி 3, 1977)."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Swaran Singh Committee report (1) came before the bill was introduced and passed in Parliament (2).", "ta": "தவறு. ஸ்வரன் சிங் குழு அறிக்கை (1) மசோதா நிறைவேற்றப்படுவதற்கு (2) முந்தையது."},
            "B": {"en": "Correct. 1 (Report) -> 2 (Passage) -> 3 (Assent) -> 4 (Enforcement on Jan 3, 1977) represents the exact legislative timeline.", "ta": "சரி. 1 (அறிக்கை) -> 2 (நிறைவேற்றம்) -> 3 (ஒப்புதல்) -> 4 (அமலாக்கம் ஜனவரி 3, 1977) துல்லியமான சட்டமியற்றல் காலவரிசையாகும்."},
            "C": {"en": "Incorrect. Presidential assent (3) occurs after bill passage in Parliament (2).", "ta": "தவறு. நாடாளுமன்றத்தில் மசோதா நிறைவேற்றப்பட்ட பின்னரே (2) குடியரசுத் தலைவர் ஒப்புதல் (3) அளிக்கப்படும்."},
            "D": {"en": "Incorrect. Presidential assent (Dec 1976) occurred before enforcement (Jan 3, 1977).", "ta": "தவறு. குடியரசுத் தலைவர் ஒப்புதல் (டிசம்பர் 1976) நடைமுறைக்கு வந்ததற்கு (ஜனவரி 3, 1977) முந்தையது."}
        },
        "tnpsc_tip": {
            "en": "TNPSC Exact Date: The 42nd Constitutional Amendment Act received Presidential assent on December 18, 1976, and Section 2 (amending Preamble) came into force on January 3, 1977.",
            "ta": "TNPSC துல்லியத் தேதி: 42வது திருத்தச் சட்டம் டிசம்பர் 18, 1976 அன்று குடியரசுத் தலைவர் ஒப்புதல் பெற்றது; முகவுரையைத் திருத்திய பிரிவு 2 ஜனவரி 3, 1977 அன்று அமலுக்கு வந்தது."
        },
        "revision_fact": {
            "en": "The 42nd Amendment is famously known as the 'Mini-Constitution' because of its extensive alterations across multiple parts of the Constitution.",
            "ta": "அரசியலமைப்பின் பல்வேறு பகுதிகளில் விரிவான மாற்றங்களைச் செய்ததால் 42வது திருத்தம் 'குறு அரசியலமைப்பு' (Mini-Constitution) என அழைக்கப்படுகிறது."
        },
        "source_reference": [
            "Constitution (Forty-second Amendment) Act, 1976",
            "M. Laxmikanth - Indian Polity",
            "Gazette of India Notifications (1976, 1977)"
        ],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "42nd Amendment", "Legislative Sequence", "Enforcement Date"],
        "question_en": "Arrange the following chronological stages in the legislative enactment and implementation of the 42nd Constitutional Amendment Act affecting the Preamble:\n1. Swaran Singh Committee submits its recommendations on constitutional amendments\n2. 42nd Constitutional Amendment Bill is passed by both Houses of Parliament\n3. President of India gives assent to the 42nd Constitutional Amendment Act\n4. Provisions of the 42nd Amendment amending the Preamble are brought into force",
        "question_ta": "முகவுரையைத் திருத்திய 42வது அரசியலமைப்புத் திருத்தச் சட்டத்தின் சட்டமியற்றல் மற்றும் நடைமுறைப்படுத்தலின் பின்வரும் காலவரிசை நிலைகளை அமைக்கவும்:\n1. ஸ்வரன் சிங் குழு அரசியலமைப்பு திருத்தங்கள் குறித்த தனது பரிந்துரைகளைச் சமர்ப்பித்தல்\n2. 42வது அரசியலமைப்புத் திருத்த மசோதா நாடாளுமன்றத்தின் இரு அவைகளாலும் நிறைவேற்றப்படுதல்\n3. இந்தியக் குடியரசுத் தலைவர் 42வது அரசியலமைப்புத் திருத்தச் சட்டத்திற்கு ஒப்புதல் அளித்தல்\n4. முகவுரையைத் திருத்திய 42வது திருத்தத்தின் விதிகள் அதிகாரப்பூர்வமாக நடைமுறைக்குக் கொண்டுவரப்படுதல்",
        "options_en": ["2 -> 1 -> 3 -> 4", "1 -> 2 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "1 -> 2 -> 4 -> 3"],
        "options_ta": ["2 -> 1 -> 3 -> 4", "1 -> 2 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "1 -> 2 -> 4 -> 3"],
        "answer": "b",
        "explanation_en": "Chronological Sequence: 1 (Swaran Singh Report: May 1976) -> 2 (Parliament passage: Nov 1976) -> 3 (Presidential assent: Dec 18, 1976) -> 4 (Enforcement: Jan 3, 1977).",
        "explanation_ta": "சரியான காலவரிசை: 1 (ஸ்வரன் சிங் அறிக்கை: மே 1976) -> 2 (நாடாளுமன்ற நிறைவேற்றம்: நவம்பர் 1976) -> 3 (குடியரசுத் தலைவர் ஒப்புதல்: டிசம்பர் 18, 1976) -> 4 (அமலாக்கம்: ஜனவரி 3, 1977)."
    },

    # -------------------------------------------------------------------------
    # Q23: PRE_CHRONO_023
    # -------------------------------------------------------------------------
    {
        "id": "PRE_CHRONO_023",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Chronology",
        "question": {
            "en": "Arrange the following historical milestones representing the international sources of inspiration for the Indian Preamble in correct chronological order:\n1. American Constitution becomes the first written constitution to begin with a Preamble\n2. French Revolution proclaims the ideals of Liberty, Equality, and Fraternity\n3. Russian Revolution introduces the ideal of Social, Economic, and Political Justice\n4. Indian Constituent Assembly incorporates these ideals into the Preamble of India",
            "ta": "இந்திய முகவுரையின் சர்வதேச உத்வேக மூலங்களைக் குறிக்கும் பின்வரும் வரலாற்று மைல்கற்களை சரியான காலவரிசையில் அமைக்கவும்:\n1. அமெரிக்க அரசியலமைப்பு முகவுரையுடன் தொடங்கிய உலகின் முதல் எழுதப்பட்ட அரசியலமைப்பாக அமைதல்\n2. பிரெஞ்சுப் புரட்சி சுதந்திரம், சமத்துவம் மற்றும் சகோதரத்துவம் ஆகிய உன்னத இலக்குகளைப் பிரகடனப்படுத்துதல்\n3. ரஷ்யப் புரட்சி சமூக, பொருளாதார மற்றும் அரசியல் நீதி என்ற கருத்தை அறிமுகப்படுத்துதல்\n4. இந்திய அரசியலமைப்பு நிர்ணய அவை இந்த சர்வதேச இலக்குகளை இந்திய முகவுரையில் இணைத்தல்"
        },
        "events": [
            {
                "id": "1",
                "en": "American Constitution becomes the first written constitution to begin with a Preamble (1787)",
                "ta": "அமெரிக்க அரசியலமைப்பு முகவுரையுடன் தொடங்கிய உலகின் முதல் எழுதப்பட்ட அரசியலமைப்பாக அமைதல் (1787)"
            },
            {
                "id": "2",
                "en": "French Revolution proclaims the ideals of Liberty, Equality, and Fraternity (1789-1799)",
                "ta": "பிரெஞ்சுப் புரட்சி சுதந்திரம், சமத்துவம் மற்றும் சகோதரத்துவம் ஆகிய உன்னத இலக்குகளைப் பிரகடனப்படுத்துதல் (1789-1799)"
            },
            {
                "id": "3",
                "en": "Russian Revolution introduces the ideal of Social, Economic, and Political Justice (1917)",
                "ta": "ரஷ்யப் புரட்சி சமூக, பொருளாதார மற்றும் அரசியல் நீதி என்ற கருத்தை அறிமுகப்படுத்துதல் (1917)"
            },
            {
                "id": "4",
                "en": "Indian Constituent Assembly incorporates these ideals into the Preamble of India (1946-1949)",
                "ta": "இந்திய அரசியலமைப்பு நிர்ணய அவை இந்த சர்வதேச இலக்குகளை இந்திய முகவுரையில் இணைத்தல் (1946-1949)"
            }
        ],
        "options": [
            {"id": "A", "en": "2 -> 1 -> 3 -> 4", "ta": "2 -> 1 -> 3 -> 4"},
            {"id": "B", "en": "1 -> 3 -> 2 -> 4", "ta": "1 -> 3 -> 2 -> 4"},
            {"id": "C", "en": "1 -> 2 -> 3 -> 4", "ta": "1 -> 2 -> 3 -> 4"},
            {"id": "D", "en": "3 -> 1 -> 2 -> 4", "ta": "3 -> 1 -> 2 -> 4"}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "Chronological Sequence: 1 (American Constitution Preamble: 1787) -> 2 (French Revolution ideals: 1789) -> 3 (Russian Revolution Justice: 1917) -> 4 (Indian Preamble: 1946-1949).",
            "ta": "சரியான காலவரிசை: 1 (அமெரிக்க முகவுரை மரபு: 1787) -> 2 (பிரெஞ்சுப் புரட்சி இலக்குகள்: 1789) -> 3 (ரஷ்யப் புரட்சி நீதி: 1917) -> 4 (இந்திய முகவுரை: 1946-1949)."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. American Constitution (1787) preceded the outbreak of the French Revolution (1789).", "ta": "தவறு. அமெரிக்க அரசியலமைப்பு (1787) பிரெஞ்சுப் புரட்சிக்கு (1789) முந்தையது."},
            "B": {"en": "Incorrect. French Revolution (1789) took place before the Russian Revolution (1917).", "ta": "தவறு. பிரெஞ்சுப் புரட்சி (1789) ரஷ்யப் புரட்சிக்கு (1917) முந்தையது."},
            "C": {"en": "Correct. 1 (1787) -> 2 (1789) -> 3 (1917) -> 4 (1946-1949) accurately represents the global historical timeline.", "ta": "சரி. 1 (1787) -> 2 (1789) -> 3 (1917) -> 4 (1946-1949) உலக வரலாற்று காலவரிசையைத் துல்லியமாகக் காட்டுகிறது."},
            "D": {"en": "Incorrect. Russian Revolution occurred in the 20th century (1917), after 18th century American and French events.", "ta": "தவறு. ரஷ்யப் புரட்சி 20ஆம் நூற்றாண்டில் (1917) நடந்தது, இது 18ஆம் நூற்றாண்டு அமெரிக்க, பிரெஞ்சு நிகழ்வுகளுக்குப் பின்னராகும்."}
        },
        "tnpsc_tip": {
            "en": "TNPSC Source Match: Preamble tradition = USA; Liberty, Equality, Fraternity = French Revolution; Social, Economic, Political Justice = Russian Revolution.",
            "ta": "TNPSC மூலப் பொருத்தம்: முகவுரை மரபு = அமெரிக்கா; சுதந்திரம், சமத்துவம், சகோதரத்துவம் = பிரெஞ்சுப் புரட்சி; சமூக, பொருளாதார, அரசியல் நீதி = ரஷ்யப் புரட்சி."
        },
        "revision_fact": {
            "en": "The concept of 'Republic' and ideals of 'Liberty, Equality and Fraternity' were borrowed from the French Constitution.",
            "ta": "'குடியரசு' என்ற கருத்து மற்றும் 'சுதந்திரம், சமத்துவம், சகோதரத்துவம்' ஆகிய உன்னத இலக்குகள் பிரெஞ்சு அரசியலமைப்பிலிருந்து பெறப்பட்டன."
        },
        "source_reference": [
            "M. Laxmikanth - Indian Polity (Preamble Sources)",
            "NCERT Class XI - Indian Constitution at Work",
            "Samacheer Kalvi - Standard 11 Political Science"
        ],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "Sources of Inspiration", "USA", "French Revolution", "Russian Revolution"],
        "question_en": "Arrange the following historical milestones representing the international sources of inspiration for the Indian Preamble in correct chronological order:\n1. American Constitution becomes the first written constitution to begin with a Preamble\n2. French Revolution proclaims the ideals of Liberty, Equality, and Fraternity\n3. Russian Revolution introduces the ideal of Social, Economic, and Political Justice\n4. Indian Constituent Assembly incorporates these ideals into the Preamble of India",
        "question_ta": "இந்திய முகவுரையின் சர்வதேச உத்வேக மூலங்களைக் குறிக்கும் பின்வரும் வரலாற்று மைல்கற்களை சரியான காலவரிசையில் அமைக்கவும்:\n1. அமெரிக்க அரசியலமைப்பு முகவுரையுடன் தொடங்கிய உலகின் முதல் எழுதப்பட்ட அரசியலமைப்பாக அமைதல்\n2. பிரெஞ்சுப் புரட்சி சுதந்திரம், சமத்துவம் மற்றும் சகோதரத்துவம் ஆகிய உன்னத இலக்குகளைப் பிரகடனப்படுத்துதல்\n3. ரஷ்யப் புரட்சி சமூக, பொருளாதார மற்றும் அரசியல் நீதி என்ற கருத்தை அறிமுகப்படுத்துதல்\n4. இந்திய அரசியலமைப்பு நிர்ணய அவை இந்த சர்வதேச இலக்குகளை இந்திய முகவுரையில் இணைத்தல்",
        "options_en": ["2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "1 -> 2 -> 3 -> 4", "3 -> 1 -> 2 -> 4"],
        "options_ta": ["2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "1 -> 2 -> 3 -> 4", "3 -> 1 -> 2 -> 4"],
        "answer": "c",
        "explanation_en": "Chronological Sequence: 1 (American Constitution Preamble: 1787) -> 2 (French Revolution ideals: 1789) -> 3 (Russian Revolution Justice: 1917) -> 4 (Indian Preamble: 1946-1949).",
        "explanation_ta": "சரியான காலவரிசை: 1 (அமெரிக்க முகவுரை மரபு: 1787) -> 2 (பிரெஞ்சுப் புரட்சி இலக்குகள்: 1789) -> 3 (ரஷ்யப் புரட்சி நீதி: 1917) -> 4 (இந்திய முகவுரை: 1946-1949)."
    },

    # -------------------------------------------------------------------------
    # Q24: PRE_CHRONO_024
    # -------------------------------------------------------------------------
    {
        "id": "PRE_CHRONO_024",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Chronology",
        "question": {
            "en": "Arrange the following four landmark constitutional benches of the Supreme Court of India dealing with Preamble interpretation in correct chronological order:\n1. 8-Judge Bench in In re Berubari Union Case\n2. 13-Judge Bench in Kesavananda Bharati v. State of Kerala\n3. 5-Judge Bench in Minerva Mills v. Union of India\n4. 9-Judge Bench in S.R. Bommai v. Union of India",
            "ta": "முகவுரை விளக்கத்தைக் கையாண்ட இந்திய உச்ச நீதிமன்றத்தின் பின்வரும் நான்கு முக்கிய அரசியலமைப்பு அமர்வுகளை சரியான காலவரிசையில் அமைக்கவும்:\n1. பெருபாரி யூனியன் வழக்கில் 8 நீதிபதிகள் கொண்ட அமர்வு\n2. கேசவானந்த பாரதி வழக்கில் 13 நீதிபதிகள் கொண்ட அமர்வு\n3. மினர்வா மில்ஸ் வழக்கில் 5 நீதிபதிகள் கொண்ட அமர்வு\n4. எஸ்.ஆர். பொம்மை வழக்கில் 9 நீதிபதிகள் கொண்ட அமர்வு"
        },
        "events": [
            {
                "id": "1",
                "en": "8-Judge Bench in In re Berubari Union Case (1960)",
                "ta": "பெருபாரி யூனியன் வழக்கில் 8 நீதிபதிகள் கொண்ட அமர்வு (1960)"
            },
            {
                "id": "2",
                "en": "13-Judge Bench in Kesavananda Bharati v. State of Kerala (1973)",
                "ta": "கேசவானந்த பாரதி வழக்கில் 13 நீதிபதிகள் கொண்ட அமர்வு (1973)"
            },
            {
                "id": "3",
                "en": "5-Judge Bench in Minerva Mills v. Union of India (1980)",
                "ta": "மினர்வா மில்ஸ் வழக்கில் 5 நீதிபதிகள் கொண்ட அமர்வு (1980)"
            },
            {
                "id": "4",
                "en": "9-Judge Bench in S.R. Bommai v. Union of India (1994)",
                "ta": "எஸ்.ஆர். பொம்மை வழக்கில் 9 நீதிபதிகள் கொண்ட அமர்வு (1994)"
            }
        ],
        "options": [
            {"id": "A", "en": "2 -> 1 -> 3 -> 4", "ta": "2 -> 1 -> 3 -> 4"},
            {"id": "B", "en": "1 -> 3 -> 2 -> 4", "ta": "1 -> 3 -> 2 -> 4"},
            {"id": "C", "en": "1 -> 2 -> 4 -> 3", "ta": "1 -> 2 -> 4 -> 3"},
            {"id": "D", "en": "1 -> 2 -> 3 -> 4", "ta": "1 -> 2 -> 3 -> 4"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "Chronological Sequence: 1 (Berubari 8-judge bench: 1960) -> 2 (Kesavananda 13-judge bench: 1973) -> 3 (Minerva Mills 5-judge bench: 1980) -> 4 (S.R. Bommai 9-judge bench: 1994).",
            "ta": "சரியான காலவரிசை: 1 (பெருபாரி 8 நீதிபதிகள் அமர்வு: 1960) -> 2 (கேசவானந்தா 13 நீதிபதிகள் அமர்வு: 1973) -> 3 (மினர்வா மில்ஸ் 5 நீதிபதிகள் அமர்வு: 1980) -> 4 (எஸ்.ஆர். பொம்மை 9 நீதிபதிகள் அமர்வு: 1994)."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Berubari (1960) preceded Kesavananda Bharati (1973).", "ta": "தவறு. பெருபாரி (1960) கேசவானந்த பாரதிக்கு (1973) முந்தையது."},
            "B": {"en": "Incorrect. Kesavananda Bharati (1973) preceded Minerva Mills (1980).", "ta": "தவறு. கேசவானந்த பாரதி (1973) மினர்வா மில்ஸுக்கு (1980) முந்தையது."},
            "C": {"en": "Incorrect. Minerva Mills (1980) was decided before S.R. Bommai (1994).", "ta": "தவறு. மினர்வா மில்ஸ் (1980) எஸ்.ஆர். பொம்மைக்கு (1994) முன்பாகத் தீர்ப்பளிக்கப்பட்டது."},
            "D": {"en": "Correct. 1 (1960) -> 2 (1973) -> 3 (1980) -> 4 (1994) reflects the exact progression of landmark constitutional benches.", "ta": "சரி. 1 (1960) -> 2 (1973) -> 3 (1980) -> 4 (1994) வரலாற்றுச் சிறப்புமிக்க அரசியலமைப்பு அமர்வுகளின் சரியான காலவரிசையாகும்."}
        },
        "tnpsc_tip": {
            "en": "TNPSC Bench Knowledge: The 13-judge bench in Kesavananda Bharati is the largest constitutional bench ever constituted in Supreme Court history, led by Chief Justice S.M. Sikri.",
            "ta": "TNPSC அமர்வு அறிவு: தலைமை நீதிபதி எஸ்.எம். சிக்ரி தலைமையில் அமைந்த 13 நீதிபதிகள் கொண்ட கேசவானந்த பாரதி அமர்வே உச்ச நீதிமன்ற வரலாற்றிலேயே மிகப்பெரிய அரசியலமைப்பு அமர்வாகும்."
        },
        "revision_fact": {
            "en": "Chief Justice B.P. Sinha headed the 8-judge bench in In re Berubari Union (1960), which was a Presidential Reference under Article 143.",
            "ta": "உறுப்பு 143-ன் கீழ் குடியரசுத் தலைவரின் ஆலோசனைக் கோரிக்கையான பெருபாரி வழக்கில் (1960) தலைமை நீதிபதி பி.பி. சின்ஹா தலைமையிலான 8 நீதிபதிகள் அமர்வு விசாரித்தது."
        },
        "source_reference": [
            "Supreme Court Reports (1960, 1973, 1980, 1994)",
            "M. Laxmikanth - Indian Polity"
        ],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "Constitutional Benches", "Judicial Chronology", "Bench Size"],
        "question_en": "Arrange the following four landmark constitutional benches of the Supreme Court of India dealing with Preamble interpretation in correct chronological order:\n1. 8-Judge Bench in In re Berubari Union Case\n2. 13-Judge Bench in Kesavananda Bharati v. State of Kerala\n3. 5-Judge Bench in Minerva Mills v. Union of India\n4. 9-Judge Bench in S.R. Bommai v. Union of India",
        "question_ta": "முகவுரை விளக்கத்தைக் கையாண்ட இந்திய உச்ச நீதிமன்றத்தின் பின்வரும் நான்கு முக்கிய அரசியலமைப்பு அமர்வுகளை சரியான காலவரிசையில் அமைக்கவும்:\n1. பெருபாரி யூனியன் வழக்கில் 8 நீதிபதிகள் கொண்ட அமர்வு\n2. கேசவானந்த பாரதி வழக்கில் 13 நீதிபதிகள் கொண்ட அமர்வு\n3. மினர்வா மில்ஸ் வழக்கில் 5 நீதிபதிகள் கொண்ட அமர்வு\n4. எஸ்.ஆர். பொம்மை வழக்கில் 9 நீதிபதிகள் கொண்ட அமர்வு",
        "options_en": ["2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "1 -> 2 -> 4 -> 3", "1 -> 2 -> 3 -> 4"],
        "options_ta": ["2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "1 -> 2 -> 4 -> 3", "1 -> 2 -> 3 -> 4"],
        "answer": "d",
        "explanation_en": "Chronological Sequence: 1 (Berubari 8-judge bench: 1960) -> 2 (Kesavananda 13-judge bench: 1973) -> 3 (Minerva Mills 5-judge bench: 1980) -> 4 (S.R. Bommai 9-judge bench: 1994).",
        "explanation_ta": "சரியான காலவரிசை: 1 (பெருபாரி 8 நீதிபதிகள் அமர்வு: 1960) -> 2 (கேசவானந்தா 13 நீதிபதிகள் அமர்வு: 1973) -> 3 (மினர்வா மில்ஸ் 5 நீதிபதிகள் அமர்வு: 1980) -> 4 (எஸ்.ஆர். பொம்மை 9 நீதிபதிகள் அமர்வு: 1994)."
    },

    # -------------------------------------------------------------------------
    # Q25: PRE_CHRONO_025 (Comprehensive 50-Year Jurisprudence Master Chronology)
    # -------------------------------------------------------------------------
    {
        "id": "PRE_CHRONO_025",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Chronology",
        "question": {
            "en": "Arrange the following comprehensive 50-year master milestones in Preamble jurisprudence from 1946 to 1995 in correct chronological order:\n1. Jawaharlal Nehru introduces the Objectives Resolution laying the philosophical foundation of the Preamble\n2. Berubari Union Case advisory opinion declaring the Preamble is NOT a part of the Constitution\n3. 42nd Constitutional Amendment Act inserting 'Socialist', 'Secular', and 'Integrity'\n4. LIC of India Case explicitly reaffirming that the Preamble is an 'integral part' of the Constitution",
            "ta": "1946 முதல் 1995 வரையிலான முகவுரை வழக்கியலின் 50 ஆண்டுகால வரலாற்று மைல்கற்களை சரியான காலவரிசையில் அமைக்கவும்:\n1. ஜவஹர்லால் நேரு முகவுரையின் தத்துவ அடித்தளத்தை அமைக்கும் குறிக்கோள் தீர்மானத்தை அறிமுகப்படுத்துதல்\n2. பெருபாரி யூனியன் ஆலோசனைக் கருத்து முகவுரை அரசியலமைப்பின் ஒரு பகுதி அல்ல என அறிவித்தல்\n3. 42வது அரசியலமைப்புத் திருத்தச் சட்டம் 'சமதர்ம', 'மதச்சார்பற்ற' மற்றும் 'ஒருமைப்பாடு' ஆகிய சொற்களைச் சேர்த்தல்\n4. எல்.ஐ.சி வழக்கில் முகவுரை அரசியலமைப்பின் 'ஒருங்கிணைந்த பகுதி' என்பதை உச்ச நீதிமன்றம் திட்டவட்டமாக மீண்டும் உறுதிப்படுத்துதல்"
        },
        "events": [
            {
                "id": "1",
                "en": "Jawaharlal Nehru introduces the Objectives Resolution laying the philosophical foundation of the Preamble",
                "ta": "ஜவஹர்லால் நேரு முகவுரையின் தத்துவ அடித்தளத்தை அமைக்கும் குறிக்கோள் தீர்மானத்தை அறிமுகப்படுத்துதல்"
            },
            {
                "id": "2",
                "en": "Berubari Union Case advisory opinion declaring the Preamble is NOT a part of the Constitution",
                "ta": "பெருபாரி யூனியன் ஆலோசனைக் கருத்து முகவுரை அரசியலமைப்பின் ஒரு பகுதி அல்ல என அறிவித்தல்"
            },
            {
                "id": "3",
                "en": "42nd Constitutional Amendment Act inserting 'Socialist', 'Secular', and 'Integrity'",
                "ta": "42வது அரசியலமைப்புத் திருத்தச் சட்டம் 'சமதர்ம', 'மதச்சார்பற்ற' மற்றும் 'ஒருமைப்பாடு' ஆகிய சொற்களைச் சேர்த்தல்"
            },
            {
                "id": "4",
                "en": "LIC of India Case explicitly reaffirming that the Preamble is an 'integral part' of the Constitution",
                "ta": "எல்.ஐ.சி வழக்கில் முகவுரை அரசியலமைப்பின் 'ஒருங்கிணைந்த பகுதி' என்பதை உச்ச நீதிமன்றம் திட்டவட்டமாக மீண்டும் உறுதிப்படுத்துதல்"
            }
        ],
        "options": [
            {"id": "A", "en": "1 -> 2 -> 3 -> 4", "ta": "1 -> 2 -> 3 -> 4"},
            {"id": "B", "en": "2 -> 1 -> 3 -> 4", "ta": "2 -> 1 -> 3 -> 4"},
            {"id": "C", "en": "1 -> 3 -> 2 -> 4", "ta": "1 -> 3 -> 2 -> 4"},
            {"id": "D", "en": "1 -> 2 -> 4 -> 3", "ta": "1 -> 2 -> 4 -> 3"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Master Chronology: 1 (Objectives Resolution: Dec 13, 1946) -> 2 (Berubari Case: 1960) -> 3 (42nd Amendment: 1976) -> 4 (LIC of India Case: 1995).",
            "ta": "முதன்மை காலவரிசை: 1 (குறிக்கோள் தீர்மானம்: டிசம்பர் 13, 1946) -> 2 (பெருபாரி வழக்கு: 1960) -> 3 (42வது திருத்தம்: 1976) -> 4 (எல்ஐசி வழக்கு: 1995)."
        },
        "why_not_others": {
            "A": {"en": "Correct. 1 (1946) -> 2 (1960) -> 3 (1976) -> 4 (1995) covers the entire 50-year journey of the Indian Preamble accurately.", "ta": "சரி. 1 (1946) -> 2 (1960) -> 3 (1976) -> 4 (1995) இந்திய முகவுரையின் 50 ஆண்டுகால முழுப் பயணத்தையும் துல்லியமாக உள்ளடக்கியுள்ளது."},
            "B": {"en": "Incorrect. Objectives Resolution (1946) was moved before the Berubari Case (1960).", "ta": "தவறு. குறிக்கோள் தீர்மானம் (1946) பெருபாரி வழக்குக்கு (1960) பல ஆண்டுகளுக்கு முந்தையது."},
            "C": {"en": "Incorrect. Berubari Case (1960) occurred before the 42nd Amendment (1976).", "ta": "தவறு. பெருபாரி வழக்கு (1960) 42வது திருத்தத்திற்கு (1976) முந்தையது."},
            "D": {"en": "Incorrect. 42nd Amendment (1976) occurred before the LIC of India Case (1995).", "ta": "தவறு. 42வது திருத்தம் (1976) எல்ஐசி வழக்குக்கு (1995) முந்தையது."}
        },
        "tnpsc_tip": {
            "en": "Final TNPSC Takeaway: Preamble originated from Objectives Resolution (1946), was held 'not part' in 1960 (Berubari), declared 'part & amendable' in 1973 (Kesavananda), amended once in 1976 (42nd Amendment), and reaffirmed 'integral part' in 1995 (LIC).",
            "ta": "இறுதி TNPSC நினைவு குறிப்பு: முகவுரை குறிக்கோள் தீர்மானத்தில் பிறந்து (1946), 1960 இல் 'பகுதி அல்ல' எனப்பட்டு (பெருபாரி), 1973 இல் 'பகுதி & திருத்தத்தக்கது' என அறிவிக்கப்பட்டு (கேசவானந்தா), 1976 இல் ஒரே முறை திருத்தப்பட்டு (42வது திருத்தம்), 1995 இல் 'ஒருங்கிணைந்த பகுதி' என மீண்டும் உறுதி செய்யப்பட்டது (எல்ஐசி)."
        },
        "revision_fact": {
            "en": "Eminent jurist Sir Alladi Krishnaswami Ayyar stated: 'The Preamble to our Constitution expresses what we had thought or dreamed so long.'",
            "ta": "பிரபல சட்ட மேதை சர் அல்லாடி கிருஷ்ணசாமி ஐயர் கூறினார்: 'நமது அரசியலமைப்பின் முகவுரை நாம் இவ்வளவு காலம் சிந்தித்ததை அல்லது கனவு கண்டதை வெளிப்படுத்துகிறது.'"
        },
        "source_reference": [
            "M. Laxmikanth - Indian Polity",
            "NCERT Class XI - Indian Constitution at Work",
            "Constituent Assembly Debates & Supreme Court Reports"
        ],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "Master Chronology", "50-Year Jurisprudence", "TNPSC Group 1"],
        "question_en": "Arrange the following comprehensive 50-year master milestones in Preamble jurisprudence from 1946 to 1995 in correct chronological order:\n1. Jawaharlal Nehru introduces the Objectives Resolution laying the philosophical foundation of the Preamble\n2. Berubari Union Case advisory opinion declaring the Preamble is NOT a part of the Constitution\n3. 42nd Constitutional Amendment Act inserting 'Socialist', 'Secular', and 'Integrity'\n4. LIC of India Case explicitly reaffirming that the Preamble is an 'integral part' of the Constitution",
        "question_ta": "1946 முதல் 1995 வரையிலான முகவுரை வழக்கியலின் 50 ஆண்டுகால வரலாற்று மைல்கற்களை சரியான காலவரிசையில் அமைக்கவும்:\n1. ஜவஹர்லால் நேரு முகவுரையின் தத்துவ அடித்தளத்தை அமைக்கும் குறிக்கோள் தீர்மானத்தை அறிமுகப்படுத்துதல்\n2. பெருபாரி யூனியன் ஆலோசனைக் கருத்து முகவுரை அரசியலமைப்பின் ஒரு பகுதி அல்ல என அறிவித்தல்\n3. 42வது அரசியலமைப்புத் திருத்தச் சட்டம் 'சமதர்ம', 'மதச்சார்பற்ற' மற்றும் 'ஒருமைப்பாடு' ஆகிய சொற்களைச் சேர்த்தல்\n4. எல்.ஐ.சி வழக்கில் முகவுரை அரசியலமைப்பின் 'ஒருங்கிணைந்த பகுதி' என்பதை உச்ச நீதிமன்றம் திட்டவட்டமாக மீண்டும் உறுதிப்படுத்துதல்",
        "options_en": ["1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "1 -> 2 -> 4 -> 3"],
        "options_ta": ["1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "1 -> 2 -> 4 -> 3"],
        "answer": "a",
        "explanation_en": "Master Chronology: 1 (Objectives Resolution: Dec 13, 1946) -> 2 (Berubari Case: 1960) -> 3 (42nd Amendment: 1976) -> 4 (LIC of India Case: 1995).",
        "explanation_ta": "முதன்மை காலவரிசை: 1 (குறிக்கோள் தீர்மானம்: டிசம்பர் 13, 1946) -> 2 (பெருபாரி வழக்கு: 1960) -> 3 (42வது திருத்தம்: 1976) -> 4 (எல்ஐசி வழக்கு: 1995)."
    }
]

def build():
    output_path = "data/questions/polity/preamble_chronology.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print(f"Successfully generated {len(questions)} chronology questions in '{output_path}'.")

if __name__ == "__main__":
    build()
