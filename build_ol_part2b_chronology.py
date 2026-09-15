# -*- coding: utf-8 -*-
"""
Official Language - Part 2B Chronology MCQs Generator (25 MCQs: OL_C_001 to OL_C_025)
Strictly adheres to:
- 24 required fields schema
- ChronologyValidator rules:
  * Exactly 4 numbered events (1., 2., 3., 4.) in English & Tamil stems
  * Presented order in stem is NOT chronological (correct sequence != 1-2-3-4)
  * Options are valid, unique permutations of [1, 2, 3, 4] formatted as "x - y - z - w"
  * Explanations explicitly teach chronology with 4-digit years and sequence arrows (→)
- Balanced answer keys (6-7 per option)
- ContentValidator & Audit pass
"""
import json
import os
from official_language_mcq_helper import make_ol_q
from tools.nova_content_engine.answer_randomizer import randomize_and_balance_dataset
from tools.nova_content_engine.validator import ContentValidator
from tools.nova_content_engine.chronology_validator import ChronologyValidator

def get_chronology_questions():
    raw_data = [
        # 1
        {
            "subtopic": "Constitutional and Statutory Milestones",
            "stem_en": "Arrange the following historic language policy milestones in chronological order:\n1. Enactment of the Official Languages Act by Parliament\n2. Adoption of Hindi in Devanagari script by the Constituent Assembly\n3. Enactment of the Official Languages (Amendment) Act providing the non-Hindi veto\n4. Expiry of the initial 15-year constitutional transition period for English\nSelect the correct answer using the codes given below:",
            "stem_ta": "பின்வரும் வரலாற்றுச் சிறப்புமிக்க மொழிக் கொள்கை மைல்கற்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. நாடாளுமன்றத்தால் அதிகாரப்பூர்வ மொழிகள் சட்டம் இயற்றப்படுதல்\n2. அரசியலமைப்பு நிர்ணய சபையால் தேவநாகரி இந்தி ஏற்றுக்கொள்ளப்படுதல்\n3. இந்தி பேசாத மாநிலங்களுக்கு மறுப்புரிமை அளித்த அதிகாரப்பூர்வ மொழிகள் (திருத்தச்) சட்டம் இயற்றப்படுதல்\n4. ஆங்கிலத்திற்கான தொடக்க 15 ஆண்டு அரசியலமைப்பு இடைக்கால அவகாசம் முடிவடைதல்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("2 - 1 - 4 - 3", "2 - 1 - 4 - 3"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4"),
                ("2 - 4 - 1 - 3", "2 - 4 - 1 - 3"),
                ("3 - 1 - 4 - 2", "3 - 1 - 4 - 2")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is:\n2. Adoption of Hindi by Constituent Assembly (14 September 1949)\n→ 1. Official Languages Act enacted (10 May 1963)\n→ 4. Expiry of 15-year transition period (26 January 1965)\n→ 3. Official Languages (Amendment) Act passed (8 January 1968 / enacted 1967).\nSequence: 2 → 1 → 4 → 3.",
            "exp_ta": "சரியான காலவரிசை:\n2. அரசியலமைப்பு நிர்ணய சபையால் இந்தி ஏற்றுக்கொள்ளப்படுதல் (14 செப்டம்பர் 1949)\n→ 1. அதிகாரப்பூர்வ மொழிகள் சட்டம் இயற்றப்படுதல் (10 மே 1963)\n→ 4. 15 ஆண்டு இடைக்கால அவகாசம் முடிவடைதல் (26 ஜனவரி 1965)\n→ 3. அதிகாரப்பூர்வ மொழிகள் (திருத்தச்) சட்டம் நிறைவேற்றப்படுதல் (1967).\nவரிசை: 2 → 1 → 4 → 3.",
            "why_a_en": "Correctly follows the chronological sequence from 1949 to 1967.",
            "why_a_ta": "1949 முதல் 1967 வரையிலான காலவரிசையைச் சரியாகப் பின்பற்றுகிறது.",
            "why_b_en": "Incorrect presented stem sequence.",
            "why_b_ta": "வினாவில் கொடுக்கப்பட்ட தவறான வரிசை.",
            "why_c_en": "Places expiry in 1965 before 1963 Act.",
            "why_c_ta": "1963 சட்டத்திற்கு முன் 1965 கெடு முடிவை தவறாக வைக்கிறது.",
            "why_d_en": "Places 1967 amendment first.",
            "why_d_ta": "1967 திருத்தத்தை முதலில் தவறாக வைக்கிறது.",
            "tip_en": "Constituent Assembly (1949) → Act (1963) → 15-yr Deadline (1965) → Amendment (1967).",
            "tip_ta": "அரசியலமைப்பு சபை (1949) → சட்டம் (1963) → 15 ஆண்டு கெடு (1965) → திருத்தம் (1967).",
            "fact_en": "Nehru's assurance in 1959 motivated the passage of the 1963 Act and 1967 Amendment.",
            "fact_ta": "1959-ல் நேரு அளித்த உறுதிமொழி 1963 சட்டம் மற்றும் 1967 திருத்தத்திற்கு உந்துதலாக இருந்தது."
        },
        # 2
        {
            "subtopic": "Eighth Schedule Language Additions",
            "stem_en": "Arrange the following additions to the Eighth Schedule of the Indian Constitution in chronological order:\n1. Addition of Bodo, Dogri, Maithili, and Santhali (92nd Amendment Act)\n2. Recognition of the original 14 languages at the commencement of the Constitution\n3. Addition of Konkani, Manipuri, and Nepali (71st Amendment Act)\n4. Addition of Sindhi as the 15th language (21st Amendment Act)\nSelect the correct answer using the codes given below:",
            "stem_ta": "இந்திய அரசியலமைப்பின் எட்டாவது அட்டவணையில் சேர்க்கப்பட்ட பின்வரும் சேர்க்கைகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. போடோ, டோக்ரி, மைதிலி மற்றும் சந்தாலி சேர்க்கப்படுதல் (92வது திருத்தச் சட்டம்)\n2. அரசியலமைப்பு அமலுக்கு வந்தபோது அசல் 14 மொழிகள் அங்கீகரிக்கப்படுதல்\n3. கொங்கணி, மணிப்பூரி மற்றும் நேபாளி சேர்க்கப்படுதல் (71வது திருத்தச் சட்டம்)\n4. சிந்தி 15வது மொழியாக சேர்க்கப்படுதல் (21வது திருத்தச் சட்டம்)\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("2 - 4 - 3 - 1", "2 - 4 - 3 - 1"),
                ("4 - 2 - 3 - 1", "4 - 2 - 3 - 1"),
                ("2 - 3 - 4 - 1", "2 - 3 - 4 - 1"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order of Eighth Schedule growth is:\n2. Original 14 languages (26 January 1950)\n→ 4. Sindhi added by 21st Amendment (10 April 1967)\n→ 3. Konkani, Manipuri, Nepali added by 71st Amendment (31 August 1992)\n→ 1. Bodo, Dogri, Maithili, Santhali added by 92nd Amendment (7 January 2004 / passed 2003).\nSequence: 2 → 4 → 3 → 1.",
            "exp_ta": "எட்டாவது அட்டவணை வளர்ச்சியின் சரியான காலவரிசை:\n2. அசல் 14 மொழிகள் (26 ஜனவரி 1950)\n→ 4. 21வது திருத்தம் மூலம் சிந்தி சேர்க்கப்பட்டது (1967)\n→ 3. 71வது திருத்தம் மூலம் கொங்கணி, மணிப்பூரி, நேபாளி சேர்க்கப்பட்டது (1992)\n→ 1. 92வது திருத்தம் மூலம் போடோ, டோக்ரி, மைதிலி, சந்தாலி சேர்க்கப்பட்டது (2003).\nவரிசை: 2 → 4 → 3 → 1.",
            "why_a_en": "Correct sequence matching 1950, 1967, 1992, and 2003.",
            "why_a_ta": "1950, 1967, 1992 மற்றும் 2003 ஆகிய ஆண்டுகளைச் சரியாகப் பொருத்தும் வரிசை.",
            "why_b_en": "Places Sindhi before the 1950 commencement.",
            "why_b_ta": "1950 தொடக்கத்திற்கு முன் சிந்தியை வைக்கிறது.",
            "why_c_en": "Swaps 71st and 21st Amendments.",
            "why_c_ta": "71வது மற்றும் 21வது திருத்தங்களை மாற்றுகிறது.",
            "why_d_en": "Incorrect presented stem order.",
            "why_d_ta": "வினாவில் கொடுக்கப்பட்ட தவறான வரிசை.",
            "tip_en": "Remember the formula: 14 (1950) → 15 (1967) → 18 (1992) → 22 (2003).",
            "tip_ta": "சூத்திரத்தை நினைவில் கொள்க: 14 (1950) → 15 (1967) → 18 (1992) → 22 (2003).",
            "fact_en": "96th Amendment in 2011 substituted Odia for Oriya without changing the total count of 22.",
            "fact_ta": "2011-ன் 96வது திருத்தம் மொத்த எண்ணிக்கை 22-ஐ மாற்றாமல் ஒரியாவை ஒடியா என மாற்றியது."
        },
        # 3
        {
            "subtopic": "Classical Language Declarations First Phase",
            "stem_en": "Arrange the declaration of the following Classical Languages in chronological order:\n1. Confertment of Classical status on Telugu and Kannada\n2. Confertment of Classical status on Sanskrit\n3. Confertment of Classical status on Odia\n4. Confertment of Classical status on Tamil\nSelect the correct answer using the codes given below:",
            "stem_ta": "பின்வரும் செம்மொழிகள் அறிவிக்கப்பட்டதை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. தெலுங்கு மற்றும் கன்னடத்திற்கு செம்மொழித் தகுதி வழங்கப்படுதல்\n2. சமஸ்கிருதத்திற்கு செம்மொழித் தகுதி வழங்கப்படுதல்\n3. ஒடியாவுக்கு செம்மொழித் தகுதி வழங்கப்படுதல்\n4. தமிழுக்கு செம்மொழித் தகுதி வழங்கப்படுதல்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("4 - 2 - 1 - 3", "4 - 2 - 1 - 3"),
                ("2 - 4 - 1 - 3", "2 - 4 - 1 - 3"),
                ("4 - 1 - 2 - 3", "4 - 1 - 2 - 3"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order of Classical Language declarations is:\n4. Tamil (12 October 2004)\n→ 2. Sanskrit (25 November 2005)\n→ 1. Telugu and Kannada (31 October 2008)\n→ 3. Odia (20 February 2014).\nSequence: 4 → 2 → 1 → 3.",
            "exp_ta": "செம்மொழி அறிவிப்புகளின் சரியான காலவரிசை:\n4. தமிழ் (12 அக்டோபர் 2004)\n→ 2. சமஸ்கிருதம் (25 நவம்பர் 2005)\n→ 1. தெலுங்கு மற்றும் கன்னடம் (31 அக்டோபர் 2008)\n→ 3. ஒடியா (20 பிப்ரவரி 2014).\nவரிசை: 4 → 2 → 1 → 3.",
            "why_a_en": "Correct sequence from 2004 to 2014.",
            "why_a_ta": "2004 முதல் 2014 வரையிலான சரியான வரிசை.",
            "why_b_en": "Places Sanskrit before Tamil.",
            "why_b_ta": "தமிழுக்கு முன் சமஸ்கிருதத்தை வைக்கிறது.",
            "why_c_en": "Places Telugu & Kannada before Sanskrit.",
            "why_c_ta": "சமஸ்கிருதத்திற்கு முன் தெலுங்கு மற்றும் கன்னடத்தை வைக்கிறது.",
            "why_d_en": "Incorrect presented stem order.",
            "why_d_ta": "வினாவில் கொடுக்கப்பட்ட தவறான வரிசை.",
            "tip_en": "Tamil (2004) was first; Sanskrit (2005) was second; Kannada & Telugu (2008); Malayalam (2013); Odia (2014).",
            "tip_ta": "தமிழ் (2004) முதன்மையானது; சமஸ்கிருதம் (2005) இரண்டாவது; கன்னடம் & தெலுங்கு (2008); மலையாளம் (2013); ஒடியா (2014).",
            "fact_en": "Central Institute of Classical Tamil was established in Chennai following Tamil's declaration.",
            "fact_ta": "தமிழ் அறிவிப்பைத் தொடர்ந்து சென்னையில் செம்மொழித் தமிழாய்வு மத்திய நிறுவனம் நிறுவப்பட்டது."
        },
        # 4
        {
            "subtopic": "Classical Languages Overall Sequence",
            "stem_en": "Arrange the conferment of Classical status on the following languages in chronological order:\n1. Malayalam\n2. Assamese, Bengali, Marathi, Pali, and Prakrit\n3. Odia\n4. Sanskrit\nSelect the correct answer using the codes given below:",
            "stem_ta": "பின்வரும் மொழிகளுக்கு செம்மொழித் தகுதி வழங்கப்பட்டதை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. மலையாளம்\n2. அஸ்ஸாமி, வங்காள மொழி, மராத்தி, பாலி மற்றும் பிராகிருதம்\n3. ஒடியா\n4. சமஸ்கிருதம்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("4 - 1 - 3 - 2", "4 - 1 - 3 - 2"),
                ("1 - 4 - 3 - 2", "1 - 4 - 3 - 2"),
                ("4 - 3 - 1 - 2", "4 - 3 - 1 - 2"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is:\n4. Sanskrit (2005)\n→ 1. Malayalam (May 2013)\n→ 3. Odia (February 2014)\n→ 2. Assamese, Bengali, Marathi, Pali, Prakrit (3 October 2024).\nSequence: 4 → 1 → 3 → 2.",
            "exp_ta": "சரியான காலவரிசை:\n4. சமஸ்கிருதம் (2005)\n→ 1. மலையாளம் (மே 2013)\n→ 3. ஒடியா (பிப்ரவரி 2014)\n→ 2. அஸ்ஸாமி, வங்காள மொழி, மராத்தி, பாலி, பிராகிருதம் (3 அக்டோபர் 2024).\nவரிசை: 4 → 1 → 3 → 2.",
            "why_a_en": "Accurate timeline spanning 2005, 2013, 2014, and 2024.",
            "why_a_ta": "2005, 2013, 2014 மற்றும் 2024 ஆகிய ஆண்டுகளை உள்ளடக்கிய துல்லியமான காலக்கோடு.",
            "why_b_en": "Places Malayalam before Sanskrit.",
            "why_b_ta": "சமஸ்கிருதத்திற்கு முன் மலையாளத்தை வைக்கிறது.",
            "why_c_en": "Swaps Odia and Malayalam.",
            "why_c_ta": "ஒடியா மற்றும் மலையாளத்தை மாற்றுகிறது.",
            "why_d_en": "Incorrect presented stem order.",
            "why_d_ta": "வினாவில் கொடுக்கப்பட்ட தவறான வரிசை.",
            "tip_en": "Remember the 11 classical languages: 1 in 2004, 1 in 2005, 2 in 2008, 1 in 2013, 1 in 2014, and 5 in 2024!",
            "tip_ta": "11 செம்மொழிகளை நினைவில் கொள்க: 2004-ல் 1, 2005-ல் 1, 2008-ல் 2, 2013-ல் 1, 2014-ல் 1, மற்றும் 2024-ல் 5!",
            "fact_en": "Pali and Prakrit are classical but not part of the Eighth Schedule.",
            "fact_ta": "பாலி மற்றும் பிராகிருதம் செம்மொழிகள் ஆனால் எட்டாவது அட்டவணையின் பகுதியாக இல்லை."
        },
        # 5
        {
            "subtopic": "Early Language Commissions and Pant Committee",
            "stem_en": "Arrange the following events relating to the initial review of Official Language in chronological order:\n1. Constitution of the Parliamentary Committee on Official Language under Govind Ballabh Pant\n2. Appointment of the First Official Language Commission under B.G. Kher\n3. Issuance of the Presidential Order on Official Language based on Pant Committee findings\n4. Submission of the B.G. Kher Official Language Commission Report\nSelect the correct answer using the codes given below:",
            "stem_ta": "அதிகாரப்பூர்வ மொழி தொடர்பான தொடக்கக்கால மறுஆய்வு நிகழ்வுகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. கோவிந்த் வல்லப் பந்த் தலைமையில் அதிகாரப்பூர்வ மொழிக்கான நாடாளுமன்றக் குழு அமைக்கப்படுதல்\n2. பி.ஜி. கேர் தலைமையில் முதலாவது அதிகாரப்பூர்வ மொழி ஆணையம் நியமிக்கப்படுதல்\n3. பந்த் குழு பரிந்துரைகளின் அடிப்படையில் அதிகாரப்பூர்வ மொழி குறித்த குடியரசுத் தலைவர் உத்தரவு பிறப்பிக்கப்படுதல்\n4. பி.ஜி. கேர் அதிகாரப்பூர்வ மொழி ஆணைய அறிக்கை சமர்ப்பிக்கப்படுதல்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("2 - 4 - 1 - 3", "2 - 4 - 1 - 3"),
                ("4 - 2 - 1 - 3", "4 - 2 - 1 - 3"),
                ("2 - 1 - 4 - 3", "2 - 1 - 4 - 3"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is:\n2. Kher Commission appointed (7 June 1955)\n→ 4. Kher Commission submits report (31 July 1956)\n→ 1. Pant Parliamentary Committee constituted (September 1957)\n→ 3. Presidential Order issued (27 April 1960).\nSequence: 2 → 4 → 1 → 3.",
            "exp_ta": "சரியான காலவரிசை:\n2. கேர் ஆணையம் நியமிக்கப்படுதல் (ஜூன் 1955)\n→ 4. கேர் ஆணையம் அறிக்கை சமர்ப்பித்தல் (1956)\n→ 1. பந்த் நாடாளுமன்றக் குழு அமைக்கப்படுதல் (செப்டம்பர் 1957)\n→ 3. குடியரசுத் தலைவர் உத்தரவு பிறப்பிக்கப்படுதல் (ஏப்ரல் 1960).\nவரிசை: 2 → 4 → 1 → 3.",
            "why_a_en": "Accurately traces the Article 344 process from 1955 appointment to 1960 Presidential Order.",
            "why_a_ta": "1955 நியமனம் முதல் 1960 குடியரசுத் தலைவர் உத்தரவு வரையிலான சரத்து 344 நடைமுறையைத் துல்லியமாகப் பின்பற்றுகிறது.",
            "why_b_en": "Places report submission before commission appointment.",
            "why_b_ta": "ஆணைய நியமனத்திற்கு முன் அறிக்கை சமர்ப்பிப்பை வைக்கிறது.",
            "why_c_en": "Places Pant committee before Kher report.",
            "why_c_ta": "கேர் அறிக்கை சமர்ப்பிப்பிற்கு முன் பந்த் குழுவை வைக்கிறது.",
            "why_d_en": "Incorrect presented stem order.",
            "why_d_ta": "வினாவில் கொடுக்கப்பட்ட தவறான வரிசை.",
            "tip_en": "Art 344 cycle: Commission (1955) → Report (1956) → Parliamentary Committee (1957) → Order (1960).",
            "tip_ta": "சரத்து 344 சுழற்சி: ஆணையம் (1955) → அறிக்கை (1956) → நாடாளுமன்றக் குழு (1957) → உத்தரவு (1960).",
            "fact_en": "President Dr. Rajendra Prasad issued directions in 1960 preparing for Hindi terminology and training.",
            "fact_ta": "குடியரசுத் தலைவர் டாக்டர் ராஜேந்திர பிரசாத் 1960-ல் இந்தி கலைச்சொற்கள் மற்றும் பயிற்சிக்கான வழிகாட்டுதல்களைப் பிறப்பித்தார்."
        },
        # 6
        {
            "subtopic": "Tamil Nadu Language Policy Evolution",
            "stem_en": "Arrange the following milestones of language struggle and policy in Tamil Nadu in chronological order:\n1. Tamil Nadu Legislative Assembly passes landmark resolution establishing Two-Language Policy\n2. Madras Official Language Act passed declaring Tamil as official language of the State\n3. Massive statewide anti-Hindi agitations in Madras State peak upon arrival of 15-year deadline\n4. Anti-Hindi agitation led by Periyar E.V.R. against compulsory Hindi in schools\nSelect the correct answer using the codes given below:",
            "stem_ta": "தமிழ்நாட்டின் மொழிப் போராட்டம் மற்றும் மொழிக் கொள்கையின் பின்வரும் மைல்கற்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. தமிழ்நாடு சட்டமன்றம் இருமொழிக் கொள்கையை நிறுவி வரலாற்றுத் தீர்மானத்தை நிறைவேற்றுதல்\n2. தமிழை மாநிலத்தின் அதிகாரப்பூர்வ மொழியாக அறிவித்து மதராஸ் அதிகாரப்பூர்வ மொழிச் சட்டம் நிறைவேற்றப்படுதல்\n3. 15 ஆண்டு காலக்கெடு முடிவடைந்ததைத் தொடர்ந்து மதராஸ் மாகாணத்தில் தீவிர இந்தி எதிர்ப்புப் போராட்டங்கள் உச்சமடைதல்\n4. பள்ளிகளில் கட்டாய இந்திக்கு எதிராக தந்தை பெரியார் தலைமையில் இந்தி எதிர்ப்புப் போராட்டம் நடைபெறுதல்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("4 - 2 - 3 - 1", "4 - 2 - 3 - 1"),
                ("2 - 4 - 3 - 1", "2 - 4 - 3 - 1"),
                ("4 - 3 - 2 - 1", "4 - 3 - 2 - 1"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is:\n4. First anti-Hindi agitation under Periyar (1937–1939)\n→ 2. Madras Official Language Act (1956)\n→ 3. Peak 1965 anti-Hindi agitations (January–February 1965)\n→ 1. Two-Language Policy Assembly resolution under Annadurai (23 January 1968).\nSequence: 4 → 2 → 3 → 1.",
            "exp_ta": "சரியான காலவரிசை:\n4. பெரியார் தலைமையில் முதல் இந்தி எதிர்ப்புப் போராட்டம் (1938)\n→ 2. மதராஸ் அதிகாரப்பூர்வ மொழிச் சட்டம் (1956)\n→ 3. தீவிர 1965 இந்தி எதிர்ப்புப் போராட்டங்கள் (ஜனவரி-பிப்ரவரி 1965)\n→ 1. அண்ணா தலைமையில் இருமொழிக் கொள்கைத் தீர்மானம் (23 ஜனவரி 1968).\nவரிசை: 4 → 2 → 3 → 1.",
            "why_a_en": "Accurately spans the historic timeline from 1938 to 1968.",
            "why_a_ta": "1938 முதல் 1968 வரையிலான வரலாற்று காலக்கோடு துல்லியமாகப் பொருந்துகிறது.",
            "why_b_en": "Places 1956 Act before the 1938 agitation.",
            "why_b_ta": "1938 போராட்டத்திற்கு முன் 1956 சட்டத்தை வைக்கிறது.",
            "why_c_en": "Places 1965 agitations before the 1956 Act.",
            "why_c_ta": "1956 சட்டத்திற்கு முன் 1965 போராட்டங்களை வைக்கிறது.",
            "why_d_en": "Incorrect presented stem order.",
            "why_d_ta": "வினாவில் கொடுக்கப்பட்ட தவறான வரிசை.",
            "tip_en": "1938 (Periyar/Rajaji era) → 1956 (Kamaraj era) → 1965 (Bhakthavatsalam era) → 1968 (Annadurai era).",
            "tip_ta": "1938 (பெரியார்/ராஜாஜி காலம்) → 1956 (காமராஜர் காலம்) → 1965 (பக்தவத்சலம் காலம்) → 1968 (அண்ணா காலம்).",
            "fact_en": "C.N. Annadurai took office as Chief Minister in March 1967 following the anti-Hindi political shift.",
            "fact_ta": "இந்தி எதிர்ப்பு அரசியல் மாற்றத்தைத் தொடர்ந்து மார்ச் 1967-ல் சி.என். அண்ணாதுரை முதலமைச்சரானார்."
        },
        # 7
        {
            "subtopic": "Language Governance Institutional Setup",
            "stem_en": "Arrange the creation/framing of the following official language institutions and statutory rules in chronological order:\n1. Official Languages (Use for Official Purposes of the Union) Rules\n2. Department of Official Language under the Ministry of Home Affairs\n3. Kendriya Hindi Samiti chaired by the Prime Minister\n4. Office of the Commissioner for Linguistic Minorities\nSelect the correct answer using the codes given below:",
            "stem_ta": "பின்வரும் அதிகாரப்பூர்வ மொழி நிறுவனங்கள் மற்றும் சட்டப்பூர்வ விதிகள் உருவாக்கப்பட்டதை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. அதிகாரப்பூர்வ மொழிகள் (ஒன்றியத்தின் அதிகாரப்பூர்வ நோக்கங்களுக்கான பயன்பாடு) விதிகள்\n2. உள்துறை அமைச்சகத்தின் கீழ் அதிகாரப்பூர்வ மொழித் துறை\n3. பிரதமர் தலைமையிலான கேந்திரிய இந்தி சமிதி\n4. மொழிச் சிறுபான்மையினருக்கான ஆணையர் அலுவலகம்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("4 - 3 - 2 - 1", "4 - 3 - 2 - 1"),
                ("4 - 2 - 3 - 1", "4 - 2 - 3 - 1"),
                ("3 - 4 - 2 - 1", "3 - 4 - 2 - 1"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is:\n4. Commissioner for Linguistic Minorities created (1957)\n→ 3. Kendriya Hindi Samiti established (1967)\n→ 2. Department of Official Language set up (June 1975)\n→ 1. Official Languages Rules framed (1976).\nSequence: 4 → 3 → 2 → 1.",
            "exp_ta": "சரியான காலவரிசை:\n4. மொழிச் சிறுபான்மையினர் ஆணையர் அலுவலகம் உருவாக்கப்படுதல் (1957)\n→ 3. கேந்திரிய இந்தி சமிதி அமைக்கப்படுதல் (1967)\n→ 2. அதிகாரப்பூர்வ மொழித் துறை உருவாக்கப்படுதல் (ஜூன் 1975)\n→ 1. அதிகாரப்பூர்வ மொழிகள் விதிகள் உருவாக்கப்படுதல் (1976).\nவரிசை: 4 → 3 → 2 → 1.",
            "why_a_en": "Accurately orders institutions: 1957, 1967, 1975, and 1976.",
            "why_a_ta": "1957, 1967, 1975 மற்றும் 1976 ஆகிய ஆண்டுகளின்படி நிறுவனங்களைச் சரியாக வரிசைப்படுத்துகிறது.",
            "why_b_en": "Places 1975 Department before 1967 Samiti.",
            "why_b_ta": "1967 சமிதிக்கு முன் 1975 துறையை வைக்கிறது.",
            "why_c_en": "Places 1967 Samiti before 1957 CLM.",
            "why_c_ta": "1957 CLM-க்கு முன் 1967 சமிதியை வைக்கிறது.",
            "why_d_en": "Incorrect presented stem order.",
            "why_d_ta": "வினாவில் கொடுக்கப்பட்ட தவறான வரிசை.",
            "tip_en": "CLM (1957) → Hindi Samiti (1967) → Department (1975) → Rules (1976).",
            "tip_ta": "CLM (1957) → இந்தி சமிதி (1967) → துறை (1975) → விதிகள் (1976).",
            "fact_en": "CLM headquarters is at Prayagraj (Allahabad) with regional offices at Belgaum, Chennai, and Kolkata.",
            "fact_ta": "CLM தலைமையகம் பிரயாக்ராஜில் (அலகாபாத்) உள்ளது; பெல்காம், சென்னை மற்றும் கொல்கத்தாவில் மண்டல அலுவலகங்கள் உள்ளன."
        },
        # 8
        {
            "subtopic": "Criteria & Dravidian Classical Declarations",
            "stem_en": "Arrange the following milestones relating to Classical Languages in chronological order:\n1. Malayalam notified as Classical Language\n2. Tamil notified as the first Classical Language\n3. Kannada and Telugu notified concurrently as Classical Languages\n4. Government of India creates the category of 'Classical Languages' and notifies initial criteria\nSelect the correct answer using the codes given below:",
            "stem_ta": "செம்மொழிகள் தொடர்பான பின்வரும் மைல்கற்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. மலையாளம் செம்மொழியாக அறிவிக்கப்படுதல்\n2. தமிழ் முதல் செம்மொழியாக அறிவிக்கப்படுதல்\n3. கன்னடம் மற்றும் தெலுங்கு ஒரே நேரத்தில் செம்மொழிகளாக அறிவிக்கப்படுதல்\n4. இந்திய அரசு 'செம்மொழிகள்' என்ற புதிய பிரிவை உருவாக்கி ஆரம்ப அளவுகோல்களை அறிவித்தல்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("4 - 2 - 3 - 1", "4 - 2 - 3 - 1"),
                ("2 - 4 - 3 - 1", "2 - 4 - 3 - 1"),
                ("4 - 3 - 2 - 1", "4 - 3 - 2 - 1"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is:\n4. Category of Classical Languages created (early 2004)\n→ 2. Tamil declared first Classical Language (12 October 2004)\n→ 3. Kannada and Telugu declared (31 October 2008)\n→ 1. Malayalam declared (23 May 2013).\nSequence: 4 → 2 → 3 → 1.",
            "exp_ta": "சரியான காலவரிசை:\n4. செம்மொழிகள் பிரிவு உருவாக்கப்பட்டு அளவுகோல்கள் வெளியிடப்படுதல் (ஆரம்ப 2004)\n→ 2. தமிழ் முதல் செம்மொழியாக அறிவிக்கப்படுதல் (12 அக்டோபர் 2004)\n→ 3. கன்னடம் மற்றும் தெலுங்கு அறிவிக்கப்படுதல் (31 அக்டோபர் 2008)\n→ 1. மலையாளம் அறிவிக்கப்படுதல் (23 மே 2013).\nவரிசை: 4 → 2 → 3 → 1.",
            "why_a_en": "Correct progression from category establishment in 2004 to Malayalam in 2013.",
            "why_a_ta": "2004-ல் பிரிவு உருவாக்கப்பட்டது முதல் 2013-ல் மலையாளம் வரையிலான சரியான வளர்ச்சி.",
            "why_b_en": "Places Tamil declaration before criteria notification.",
            "why_b_ta": "அளவுகோல் அறிவிப்புக்கு முன் தமிழ் அறிவிப்பை வைக்கிறது.",
            "why_c_en": "Places Telugu & Kannada before Tamil.",
            "why_c_ta": "தமிழுக்கு முன் தெலுங்கு & கன்னடத்தை வைக்கிறது.",
            "why_d_en": "Incorrect presented stem order.",
            "why_d_ta": "வினாவில் கொடுக்கப்பட்ட தவறான வரிசை.",
            "tip_en": "Remember criteria was framed in 2004 specifically leading to the declaration of Tamil in Oct 2004.",
            "tip_ta": "அக்டோபர் 2004-ல் தமிழ் அறிவிக்கப்படுவதற்கு வழிவகுக்கும் வகையில் 2004-ல் அளவுகோல்கள் உருவாக்கப்பட்டன.",
            "fact_en": "Central Institute of Classical Tamil (CICT) operates under Ministry of Education.",
            "fact_ta": "செம்மொழித் தமிழாய்வு மத்திய நிறுவனம் (CICT) மத்திய கல்வி அமைச்சகத்தின் கீழ் செயல்படுகிறது."
        },
        # 9
        {
            "subtopic": "Post-Independence Enactments Sequence",
            "stem_en": "Arrange the following statutory enactments and regulatory actions in chronological order:\n1. Notification of the Official Languages Rules\n2. Enactment of the Official Languages Act\n3. Enactment of the Official Languages (Amendment) Act\n4. Adoption of the Official Language Resolution by both Houses of Parliament\nSelect the correct answer using the codes given below:",
            "stem_ta": "பின்வரும் சட்டப்பூர்வ இயற்றல்கள் மற்றும் ஒழுங்குமுறை நடவடிக்கைகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. அதிகாரப்பூர்வ மொழிகள் விதிகள் அறிவிக்கப்படுதல்\n2. அதிகாரப்பூர்வ மொழிகள் சட்டம் இயற்றப்படுதல்\n3. அதிகாரப்பூர்வ மொழிகள் (திருத்தச்) சட்டம் இயற்றப்படுதல்\n4. நாடாளுமன்றத்தின் இரு அவைகளாலும் அதிகாரப்பூர்வ மொழித் தீர்மானம் ஏற்றுக்கொள்ளப்படுதல்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("2 - 3 - 4 - 1", "2 - 3 - 4 - 1"),
                ("3 - 2 - 4 - 1", "3 - 2 - 4 - 1"),
                ("2 - 4 - 3 - 1", "2 - 4 - 3 - 1"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is:\n2. Official Languages Act (1963)\n→ 3. Official Languages (Amendment) Act (passed December 1967)\n→ 4. Official Language Resolution passed by Parliament (18 January 1968)\n→ 1. Official Languages Rules notified (1976).\nSequence: 2 → 3 → 4 → 1.",
            "exp_ta": "சரியான காலவரிசை:\n2. அதிகாரப்பூர்வ மொழிகள் சட்டம் (1963)\n→ 3. அதிகாரப்பூர்வ மொழிகள் (திருத்தச்) சட்டம் (டிசம்பர் 1967)\n→ 4. நாடாளுமன்ற அதிகாரப்பூர்வ மொழித் தீர்மானம் (18 ஜனவரி 1968)\n→ 1. அதிகாரப்பூர்வ மொழிகள் விதிகள் (1976).\nவரிசை: 2 → 3 → 4 → 1.",
            "why_a_en": "Correct sequence matching 1963, 1967, 1968, and 1976.",
            "why_a_ta": "1963, 1967, 1968 மற்றும் 1976 ஆகிய ஆண்டுகளைச் சரியாகப் பொருத்தும் வரிசை.",
            "why_b_en": "Places 1967 amendment before 1963 Act.",
            "why_b_ta": "1963 சட்டத்திற்கு முன் 1967 திருத்தத்தை வைக்கிறது.",
            "why_c_en": "Places 1968 resolution before 1967 amendment.",
            "why_c_ta": "1967 திருத்தத்திற்கு முன் 1968 தீர்மானத்தை வைக்கிறது.",
            "why_d_en": "Incorrect presented stem order.",
            "why_d_ta": "வினாவில் கொடுக்கப்பட்ட தவறான வரிசை.",
            "tip_en": "Act (1963) → Amendment (1967) → Resolution (1968) → Rules (1976).",
            "tip_ta": "சட்டம் (1963) → திருத்தம் (1967) → தீர்மானம் (1968) → விதிகள் (1976).",
            "fact_en": "The 1968 Resolution urged the intensive development of Hindi and all 14 languages of the Eighth Schedule.",
            "fact_ta": "1968 தீர்மானம் இந்தி மற்றும் எட்டாவது அட்டவணையின் அனைத்து 14 மொழிகளையும் தீவிரமாக வளர்க்க வலியுறுத்தியது."
        },
        # 10
        {
            "subtopic": "Linguistic Minority Safeguards Timeline",
            "stem_en": "Arrange the following events concerning linguistic minorities in chronological order:\n1. 7th Constitutional Amendment Act inserts Articles 350A and 350B\n2. Constitution commences with original Article 350 on grievance representation\n3. First Annual Report of Commissioner for Linguistic Minorities tabled in Parliament\n4. States Reorganisation Commission (Fazal Ali) recommends mother-tongue primary education safeguards\nSelect the correct answer using the codes given below:",
            "stem_ta": "மொழிச் சிறுபான்மையினர் தொடர்பான பின்வரும் நிகழ்வுகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. 7வது அரசியலமைப்பு திருத்தச் சட்டம் சரத்துகள் 350A மற்றும் 350B-ஐச் சேர்த்தல்\n2. குறைதீர்ப்பு மனு தொடர்பான அசல் சரத்து 350-உடன் அரசியலமைப்பு நடைமுறைக்கு வருதல்\n3. மொழிச் சிறுபான்மையினர் ஆணையரின் முதல் வருடாந்திர அறிக்கை நாடாளுமன்றத்தில் சமர்ப்பிக்கப்படுதல்\n4. தாய்மொழி வழிக் கல்விப் பாதுகாப்புகளை மாநில மறுசீரமைப்பு ஆணையம் (பசல் அலி) பரிந்துரைத்தல்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("2 - 4 - 1 - 3", "2 - 4 - 1 - 3"),
                ("4 - 2 - 1 - 3", "4 - 2 - 1 - 3"),
                ("2 - 1 - 4 - 3", "2 - 1 - 4 - 3"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is:\n2. Constitution commences with Art 350 (26 January 1950)\n→ 4. States Reorganisation Commission report (October 1955)\n→ 1. 7th Amendment Act inserts Arts 350A & 350B (November 1956)\n→ 3. First CLM Report presented (1958).\nSequence: 2 → 4 → 1 → 3.",
            "exp_ta": "சரியான காலவரிசை:\n2. சரத்து 350-உடன் அரசியலமைப்பு தொடங்குதல் (1950)\n→ 4. மாநில மறுசீரமைப்பு ஆணைய அறிக்கை (1955)\n→ 1. 7வது திருத்தம் மூலம் 350A & 350B சேர்க்கப்படுதல் (1956)\n→ 3. முதல் CLM அறிக்கை சமர்ப்பிக்கப்படுதல் (1958).\nவரிசை: 2 → 4 → 1 → 3.",
            "why_a_en": "Chronologically tracks the evolution of linguistic minority protections from 1950 to 1958.",
            "why_a_ta": "1950 முதல் 1958 வரையிலான மொழிச் சிறுபான்மையினர் பாதுகாப்பு வளர்ச்சியை துல்லியமாகக் கண்காணிக்கிறது.",
            "why_b_en": "Places SRC report before 1950 Constitution.",
            "why_b_ta": "1950 அரசியலமைப்புக்கு முன் SRC அறிக்கையை வைக்கிறது.",
            "why_c_en": "Places 7th Amendment before SRC report.",
            "why_c_ta": "SRC அறிக்கைக்கு முன் 7வது திருத்தத்தை வைக்கிறது.",
            "why_d_en": "Incorrect presented stem order.",
            "why_d_ta": "வினாவில் கொடுக்கப்பட்ட தவறான வரிசை.",
            "tip_en": "SRC (1955) directly triggered the 7th Amendment (1956) inserting 350A and 350B.",
            "tip_ta": "SRC (1955) நேரடியாக 350A மற்றும் 350B-ஐச் சேர்த்த 7வது திருத்தத்தைத் (1956) தூண்டியது.",
            "fact_en": "The Commissioner for Linguistic Minorities was formally appointed in July 1957.",
            "fact_ta": "மொழிச் சிறுபான்மையினர் ஆணையர் ஜூலை 1957-ல் முறையாக நியமிக்கப்பட்டார்."
        },
        # 11
        {
            "subtopic": "Eighth Schedule Language Growth Milestones",
            "stem_en": "Arrange the following stages of Eighth Schedule strength in chronological order:\n1. Total reaches 18 languages\n2. Total reaches 15 languages\n3. Total reaches 22 languages\n4. Original 14 languages in the Schedule\nSelect the correct answer using the codes given below:",
            "stem_ta": "எட்டாவது அட்டவணை மொழி வலிமையின் பின்வரும் நிலைகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. மொத்த எண்ணிக்கை 18 மொழிகளை எட்டுதல்\n2. மொத்த எண்ணிக்கை 15 மொழிகளை எட்டுதல்\n3. மொத்த எண்ணிக்கை 22 மொழிகளை எட்டுதல்\n4. அட்டவணையில் அசல் 14 மொழிகள் இருத்தல்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("4 - 2 - 1 - 3", "4 - 2 - 1 - 3"),
                ("2 - 4 - 1 - 3", "2 - 4 - 1 - 3"),
                ("4 - 1 - 2 - 3", "4 - 1 - 2 - 3"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological progression is:\n4. 14 languages (1950)\n→ 2. 15 languages (Sindhi added, 1967)\n→ 1. 18 languages (Konkani, Manipuri, Nepali added, 1992)\n→ 3. 22 languages (BDMS added, 2003).\nSequence: 4 → 2 → 1 → 3.",
            "exp_ta": "சரியான காலவரிசை வளர்ச்சி:\n4. 14 மொழிகள் (1950)\n→ 2. 15 மொழிகள் (சிந்தி சேர்க்கப்பட்டது, 1967)\n→ 1. 18 மொழிகள் (கொங்கணி, மணிப்பூரி, நேபாளி சேர்க்கப்பட்டது, 1992)\n→ 3. 22 மொழிகள் (BDMS சேர்க்கப்பட்டது, 2003).\nவரிசை: 4 → 2 → 1 → 3.",
            "why_a_en": "Correct count progression: 14 (1950) -> 15 (1967) -> 18 (1992) -> 22 (2003).",
            "why_a_ta": "சரியான எண்ணிக்கை வளர்ச்சி: 14 (1950) -> 15 (1967) -> 18 (1992) -> 22 (2003).",
            "why_b_en": "Places 15 languages before 14 languages.",
            "why_b_ta": "14 மொழிகளுக்கு முன் 15 மொழிகளை வைக்கிறது.",
            "why_c_en": "Swaps 15 and 18 languages.",
            "why_c_ta": "15 மற்றும் 18 மொழிகளை மாற்றுகிறது.",
            "why_d_en": "Incorrect presented stem order.",
            "why_d_ta": "வினாவில் கொடுக்கப்பட்ட தவறான வரிசை.",
            "tip_en": "Count jumps: +1 in 1967, +3 in 1992, +4 in 2003.",
            "tip_ta": "எண்ணிக்கை உயர்வு: 1967-ல் +1, 1992-ல் +3, 2003-ல் +4.",
            "fact_en": "There have been no additions to the Eighth Schedule since 2003.",
            "fact_ta": "2003-க்குப் பிறகு எட்டாவது அட்டவணையில் புதிய மொழிகள் எதுவும் சேர்க்கப்படவில்லை."
        },
        # 12
        {
            "subtopic": "1965 Crisis and Aftermath",
            "stem_en": "Arrange the following events surrounding the 1965 language crisis in chronological order:\n1. Prime Minister Lal Bahadur Shastri's radio broadcast assuring that Nehru's promises will be honoured\n2. Enactment of the Official Languages (Amendment) Act giving statutory veto to non-Hindi States\n3. Widespread student self-immolations and agitations across Tamil Nadu in January–February\n4. Prime Minister Jawaharlal Nehru gives solemn assurance on English in the Lok Sabha\nSelect the correct answer using the codes given below:",
            "stem_ta": "1965 மொழி நெருக்கடி தொடர்பான பின்வரும் நிகழ்வுகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. நேருவின் வாக்குறுதிகள் மதிக்கப்படும் என பிரதமர் லால் பகதூர் சாஸ்திரியின் வானொலி உரை\n2. இந்தி பேசாத மாநிலங்களுக்கு சட்டப்பூர்வ மறுப்புரிமை அளிக்கும் அதிகாரப்பூர்வ மொழிகள் (திருத்தச்) சட்டம் இயற்றப்படுதல்\n3. ஜனவரி-பிப்ரவரியில் தமிழ்நாடு முழுவதும் தீவிர மாணவர் தீக்குளிப்புகள் மற்றும் போராட்டங்கள் வெடித்தல்\n4. மக்களவையில் ஆங்கிலம் குறித்து பிரதமர் ஜவஹர்லால் நேரு வரலாற்று உறுதிமொழி அளித்தல்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("4 - 3 - 1 - 2", "4 - 3 - 1 - 2"),
                ("3 - 4 - 1 - 2", "3 - 4 - 1 - 2"),
                ("4 - 1 - 3 - 2", "4 - 1 - 3 - 2"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is:\n4. Nehru's Lok Sabha assurance (7 August / 4 September 1959)\n→ 3. Anti-Hindi agitations in Madras (January–February 1965)\n→ 1. Shastri's broadcast promising Nehru's assurance (11 February 1965)\n→ 2. 1967 Amendment Act enacting Section 3(5) (December 1967 / January 1968).\nSequence: 4 → 3 → 1 → 2.",
            "exp_ta": "சரியான காலவரிசை:\n4. நேருவின் மக்களவை உறுதிமொழி (1959)\n→ 3. மதராஸில் இந்தி எதிர்ப்புப் போராட்டங்கள் (ஜனவரி-பிப்ரவரி 1965)\n→ 1. நேருவின் வாக்குறுதியை உறுதி செய்யும் சாஸ்திரியின் வானொலி உரை (11 பிப்ரவரி 1965)\n→ 2. பிரிவு 3(5)-ஐச் சேர்த்த 1967 திருத்தச் சட்டம் (1967).\nவரிசை: 4 → 3 → 1 → 2.",
            "why_a_en": "Accurately traces the chain reaction from 1959 assurance to 1967 statutory enactment.",
            "why_a_ta": "1959 உறுதிமொழி முதல் 1967 சட்ட அமலாக்கம் வரையிலான சங்கிலித் தொடர் நிகழ்வுகளைத் துல்லியமாகப் பின்பற்றுகிறது.",
            "why_b_en": "Places 1965 riots before Nehru's 1959 assurance.",
            "why_b_ta": "நேருவின் 1959 உறுதிமொழிக்கு முன் 1965 போராட்டங்களை வைக்கிறது.",
            "why_c_en": "Places Shastri's broadcast before the 1965 riots that prompted it.",
            "why_c_ta": "அதற்குக் காரணமான 1965 போராட்டங்களுக்கு முன் சாஸ்திரியின் உரையை வைக்கிறது.",
            "why_d_en": "Incorrect presented stem order.",
            "why_d_ta": "வினாவில் கொடுக்கப்பட்ட தவறான வரிசை.",
            "tip_en": "Nehru (1959) → 1965 Agitation → Shastri Broadcast (1965) → Indira Gandhi 1967 Amendment.",
            "tip_ta": "நேரு (1959) → 1965 போராட்டம் → சாஸ்திரி உரை (1965) → இந்திரா காந்தி 1967 திருத்தம்.",
            "fact_en": "Kinnasamy, Sarangapani, and others sacrificed their lives during the 1965 language agitation in Tamil Nadu.",
            "fact_ta": "தமிழ்நாட்டில் நடந்த 1965 மொழிப் போராட்டத்தின் போது கீழப்பழுவூர் சின்னச்சாமி, சாரங்கபாணி உள்ளிட்ட பலர் தீக்குளித்து உயிர்நீத்தனர்."
        },
        # 13
        {
            "subtopic": "State Official Language Legislative Actions",
            "stem_en": "Arrange the adoption of official languages by the following States in chronological order:\n1. Nagaland adopts English as its sole official language\n2. Madras State adopts Tamil as its official language\n3. Goa enacts Official Language Act adopting Konkani in Devanagari script\n4. Jammu and Kashmir enacts Official Languages Act establishing five official languages\nSelect the correct answer using the codes given below:",
            "stem_ta": "பின்வரும் மாநிலங்களால் அதிகாரப்பூர்வ மொழிகள் ஏற்றுக்கொள்ளப்பட்டதை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. நாகாலாந்து ஆங்கிலத்தை தனது ஒரே அதிகாரப்பூர்வ மொழியாக ஏற்றுக்கொள்வது\n2. மதராஸ் மாநிலம் தமிழை தனது அதிகாரப்பூர்வ மொழியாக ஏற்றுக்கொள்வது\n3. கோவா தேவநாகரி வரிவடிவ கொங்கணியை ஏற்றுக்கொண்டு அதிகாரப்பூர்வ மொழிச் சட்டத்தை இயற்றுவது\n4. ஜம்மு காஷ்மீர் ஐந்து அதிகாரப்பூர்வ மொழிகளை நிறுவி அதிகாரப்பூர்வ மொழிகள் சட்டத்தை இயற்றுவது\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("2 - 1 - 3 - 4", "2 - 1 - 3 - 4"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4"),
                ("2 - 3 - 1 - 4", "2 - 3 - 1 - 4"),
                ("3 - 2 - 1 - 4", "3 - 2 - 1 - 4")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is:\n2. Madras State adopts Tamil (1956)\n→ 1. Nagaland adopts English (1967)\n→ 3. Goa adopts Konkani (1987)\n→ 4. J&K adopts five official languages (2020).\nSequence: 2 → 1 → 3 → 4.",
            "exp_ta": "சரியான காலவரிசை:\n2. மதராஸ் மாநிலம் தமிழை ஏற்றல் (1956)\n→ 1. நாகாலாந்து ஆங்கிலத்தை ஏற்றல் (1967)\n→ 3. கோவா கொங்கணியை ஏற்றல் (1987)\n→ 4. ஜம்மு காஷ்மீர் ஐந்து மொழிகளை ஏற்றல் (2020).\nவரிசை: 2 → 1 → 3 → 4.",
            "why_a_en": "Accurately traces Article 345 state enactments in 1956, 1967, 1987, and 2020.",
            "why_a_ta": "சரத்து 345-ன் கீழான மாநிலச் சட்டங்களை 1956, 1967, 1987 மற்றும் 2020 ஆகிய ஆண்டுகளில் துல்லியமாகப் பின்பற்றுகிறது.",
            "why_b_en": "Incorrect presented stem order (though presented was 1-2-3-4, chronological is 2-1-3-4).",
            "why_b_ta": "வினா வரிசை (2-1-3-4 என்பது சரியான காலவரிசை).",
            "why_c_en": "Places Goa before Nagaland.",
            "why_c_ta": "நாகாலாந்துக்கு முன் கோவாவை வைக்கிறது.",
            "why_d_en": "Places Goa before Madras.",
            "why_d_ta": "மதராஸுக்கு முன் கோவாவை வைக்கிறது.",
            "tip_en": "Tamil (1956) → Nagaland English (1967) → Goa Konkani (1987) → J&K 5 languages (2020).",
            "tip_ta": "தமிழ் (1956) → நாகாலாந்து ஆங்கிலம் (1967) → கோவா கொங்கணி (1987) → ஜம்மு காஷ்மீர் 5 மொழிகள் (2020).",
            "fact_en": "J&K Official Languages Act 2020 was enacted by Parliament under J&K Reorganisation framework.",
            "fact_ta": "ஜம்மு காஷ்மீர் அதிகாரப்பூர்வ மொழிகள் சட்டம் 2020 நாடாளுமன்றத்தால் இயற்றப்பட்டது."
        },
        # 14
        {
            "subtopic": "Judicial Precedents on Language Rights",
            "stem_en": "Arrange the following judicial rulings on language in chronological order:\n1. Gujarat High Court clarifies Hindi is not the National Language in Suresh Kachhadia case\n2. Supreme Court upholds presidential directives on voluntary Hindi training in Murasoli Maran case\n3. Supreme Court upholds mother-tongue medium in Anglo-Indian schools in Bombay Education Society case\n4. Supreme Court dismisses petition demanding civil services examinations solely in Hindi in Hindi Hitrakshak Samiti case\nSelect the correct answer using the codes given below:",
            "stem_ta": "மொழி தொடர்பான பின்வரும் நீதிமன்றத் தீர்ப்புகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. சுரேஷ் கச்சாடியா வழக்கில் இந்தி தேசிய மொழி அல்ல என குஜராத் உயர் நீதிமன்றம் தெளிவுபடுத்துதல்\n2. முரசொலி மாறன் வழக்கில் விருப்ப இந்திப் பயிற்சி தொடர்பான குடியரசுத் தலைவர் உத்தரவுகளை உச்ச நீதிமன்றம் உறுதி செய்தல்\n3. பம்பாய் கல்வி சங்க வழக்கில் ஆங்கிலோ-இந்தியப் பள்ளிகளில் தாய்மொழி வழிக் கல்வியை உச்ச நீதிமன்றம் உறுதி செய்தல்\n4. இந்தி ஹித்ரக்ஷக் சமிதி வழக்கில் குடிமைப் பணித் தேர்வுகளை இந்தியில் மட்டுமே நடத்தக் கோரிய மனுவை உச்ச நீதிமன்றம் தள்ளுபடி செய்தல்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("3 - 2 - 4 - 1", "3 - 2 - 4 - 1"),
                ("2 - 3 - 4 - 1", "2 - 3 - 4 - 1"),
                ("3 - 4 - 2 - 1", "3 - 4 - 2 - 1"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is:\n3. State of Bombay v. Bombay Education Society (1954)\n→ 2. Union of India v. Murasoli Maran (1977)\n→ 4. Hindi Hitrakshak Samiti v. Union of India (1990)\n→ 1. Suresh Kachhadia v. Union of India (2010).\nSequence: 3 → 2 → 4 → 1.",
            "exp_ta": "சரியான காலவரிசை:\n3. பம்பாய் கல்வி சங்க வழக்கு (1954)\n→ 2. முரசொலி மாறன் வழக்கு (1977)\n→ 4. இந்தி ஹித்ரக்ஷக் சமிதி வழக்கு (1990)\n→ 1. சுரேஷ் கச்சாடியா வழக்கு (2010).\nவரிசை: 3 → 2 → 4 → 1.",
            "why_a_en": "Correct sequence matching 1954, 1977, 1990, and 2010 judicial landmarks.",
            "why_a_ta": "1954, 1977, 1990 மற்றும் 2010 ஆகிய முக்கிய நீதித்துறை மைல்கற்களைச் சரியாகப் பொருத்தும் வரிசை.",
            "why_b_en": "Places 1977 Murasoli Maran before 1954 Bombay Education Society.",
            "why_b_ta": "1954 பம்பாய் வழக்கிற்கு முன் 1977 முரசொலி மாறன் வழக்கை வைக்கிறது.",
            "why_c_en": "Swaps 1977 and 1990 cases.",
            "why_c_ta": "1977 மற்றும் 1990 வழக்குகளை மாற்றுகிறது.",
            "why_d_en": "Incorrect presented stem order.",
            "why_d_ta": "வினாவில் கொடுக்கப்பட்ட தவறான வரிசை.",
            "tip_en": "Bombay (1954) → Murasoli Maran (1977) → Hindi Hitrakshak (1990) → Kachhadia (2010).",
            "tip_ta": "பம்பாய் (1954) → முரசொலி மாறன் (1977) → இந்தி ஹித்ரக்ஷக் (1990) → கச்சாடியா (2010).",
            "fact_en": "All four cases are landmark precedents frequently tested in Indian constitutional law.",
            "fact_ta": "இந்நான்கு வழக்குகளும் இந்திய அரசியலமைப்புச் சட்டத்தில் அடிக்கடி கேட்கப்படும் முக்கிய முன்னுதாரணங்களாகும்."
        },
        # 15
        {
            "subtopic": "Chronology of Classical Language Notifications",
            "stem_en": "Arrange the following notifications granting Classical status in chronological order:\n1. Odia notified as Classical Language\n2. Sanskrit notified as Classical Language\n3. Assamese and Marathi notified as Classical Languages\n4. Tamil notified as Classical Language\nSelect the correct answer using the codes given below:",
            "stem_ta": "செம்மொழித் தகுதி வழங்கிய பின்வரும் அறிவிப்புகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. ஒடியா செம்மொழியாக அறிவிக்கப்படுதல்\n2. சமஸ்கிருதம் செம்மொழியாக அறிவிக்கப்படுதல்\n3. அஸ்ஸாமி மற்றும் மராத்தி செம்மொழிகளாக அறிவிக்கப்படுதல்\n4. தமிழ் செம்மொழியாக அறிவிக்கப்படுதல்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("4 - 2 - 1 - 3", "4 - 2 - 1 - 3"),
                ("2 - 4 - 1 - 3", "2 - 4 - 1 - 3"),
                ("4 - 1 - 2 - 3", "4 - 1 - 2 - 3"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is:\n4. Tamil (2004)\n→ 2. Sanskrit (2005)\n→ 1. Odia (2014)\n→ 3. Assamese and Marathi (October 2024).\nSequence: 4 → 2 → 1 → 3.",
            "exp_ta": "சரியான காலவரிசை:\n4. தமிழ் (2004)\n→ 2. சமஸ்கிருதம் (2005)\n→ 1. ஒடியா (2014)\n→ 3. அஸ்ஸாமி மற்றும் மராத்தி (அக்டோபர் 2024).\nவரிசை: 4 → 2 → 1 → 3.",
            "why_a_en": "Accurately reflects 2004, 2005, 2014, and 2024 notifications.",
            "why_a_ta": "2004, 2005, 2014 மற்றும் 2024 அறிவிப்புகளைத் துல்லியமாகப் பிரதிபலிக்கிறது.",
            "why_b_en": "Places Sanskrit before Tamil.",
            "why_b_ta": "தமிழுக்கு முன் சமஸ்கிருதத்தை வைக்கிறது.",
            "why_c_en": "Places Odia before Sanskrit.",
            "why_c_ta": "சமஸ்கிருதத்திற்கு முன் ஒடியாவை வைக்கிறது.",
            "why_d_en": "Incorrect presented stem order.",
            "why_d_ta": "வினாவில் கொடுக்கப்பட்ட தவறான வரிசை.",
            "tip_en": "First was Tamil (2004); 6th was Odia (2014); 7th-11th came in Oct 2024.",
            "tip_ta": "முதலில் தமிழ் (2004); 6வதாக ஒடியா (2014); 7 முதல் 11வது வரை அக் 2024-ல் வந்தன.",
            "fact_en": "October 2024 was the largest single addition to the Classical Language list (5 languages).",
            "fact_ta": "அக்டோபர் 2024 செம்மொழிப் பட்டியலில் ஒரே நேரத்தில் செய்யப்பட்ட மிகப்பெரிய சேர்க்கையாகும் (5 மொழிகள்)."
        },
        # 16
        {
            "subtopic": "Parliamentary Language Developments",
            "stem_en": "Arrange the following developments concerning language in Parliament in chronological order:\n1. Operationalization of simultaneous interpretation in all 22 Eighth Schedule languages in Rajya Sabha\n2. Commencement of Article 120 permitting Hindi or English in Parliament\n3. Section 3 of Official Languages Act extends English in Parliament beyond 1965\n4. Prime Minister Nehru assures non-Hindi members regarding parliamentary business language\nSelect the correct answer using the codes given below:",
            "stem_ta": "நாடாளுமன்றத்தில் மொழி பயன்பாடு தொடர்பான பின்வரும் நிகழ்வுகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. மாநிலங்களவையில் 22 எட்டாவது அட்டவணை மொழிகளிலும் உடனடி மொழிபெயர்ப்பு வசதி பயன்பாட்டுக்கு வருதல்\n2. நாடாளுமன்றத்தில் இந்தி அல்லது ஆங்கிலத்தை அனுமதிக்கும் சரத்து 120 நடைமுறைக்கு வருதல்\n3. அதிகாரப்பூர்வ மொழிகள் சட்டத்தின் பிரிவு 3 நாடாளுமன்றத்தில் 1965-க்குப் பிறகும் ஆங்கிலத்தை நீட்டித்தல்\n4. நாடாளுமன்ற அலுவல் மொழி தொடர்பாக இந்தி பேசாத உறுப்பினர்களுக்கு பிரதமர் நேரு உறுதியளித்தல்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("2 - 4 - 3 - 1", "2 - 4 - 3 - 1"),
                ("4 - 2 - 3 - 1", "4 - 2 - 3 - 1"),
                ("2 - 3 - 4 - 1", "2 - 3 - 4 - 1"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is:\n2. Article 120 commences (26 January 1950)\n→ 4. Nehru's parliamentary assurance (1959)\n→ 3. Section 3 of Official Languages Act passed (1963)\n→ 1. Simultaneous interpretation in all 22 languages operationalized (July 2018).\nSequence: 2 → 4 → 3 → 1.",
            "exp_ta": "சரியான காலவரிசை:\n2. சரத்து 120 நடைமுறைக்கு வருதல் (1950)\n→ 4. நேருவின் நாடாளுமன்ற உறுதிமொழி (1959)\n→ 3. அதிகாரப்பூர்வ மொழிகள் சட்டம் பிரிவு 3 (1963)\n→ 1. 22 மொழிகளிலும் உடனடி மொழிபெயர்ப்பு வசதி (2018).\nவரிசை: 2 → 4 → 3 → 1.",
            "why_a_en": "Correct sequence matching 1950, 1959, 1963, and 2018.",
            "why_a_ta": "1950, 1959, 1963 மற்றும் 2018 ஆகிய ஆண்டுகளைச் சரியாகப் பொருத்தும் வரிசை.",
            "why_b_en": "Places Nehru's 1959 speech before 1950 Constitution.",
            "why_b_ta": "1950 அரசியலமைப்புக்கு முன் நேருவின் 1959 உரையை வைக்கிறது.",
            "why_c_en": "Places 1963 Act before 1959 assurance.",
            "why_c_ta": "1959 உறுதிமொழிக்கு முன் 1963 சட்டத்தை வைக்கிறது.",
            "why_d_en": "Incorrect presented stem order.",
            "why_d_ta": "வினாவில் கொடுக்கப்பட்ட தவறான வரிசை.",
            "tip_en": "Art 120 (1950) → Nehru (1959) → Act (1963) → 22 Languages Interpretation (2018).",
            "tip_ta": "சரத்து 120 (1950) → நேரு (1959) → சட்டம் (1963) → 22 மொழி மொழிபெயர்ப்பு (2018).",
            "fact_en": "Rajya Sabha Chairman M. Venkaiah Naidu inaugurated the 22-language interpretation facility in 2018.",
            "fact_ta": "மாநிலங்களவைத் தலைவர் எம். வெங்கையா நாயுடு 2018-ல் 22 மொழிகளிலான மொழிபெயர்ப்பு வசதியைத் தொடங்கி வைத்தார்."
        },
        # 17
        {
            "subtopic": "Ancient Texts Antiquity Sequence",
            "stem_en": "Arrange the approximate historical composition / codification of the following foundational texts in chronological order:\n1. Dnyaneshwari composed in early Marathi\n2. Rigveda codified in early Vedic Sanskrit\n3. Tolkappiyam and early Sangam poems codified in Classical Tamil\n4. Madala Panji temple records written in early Odia\nSelect the correct answer using the codes given below:",
            "stem_ta": "பின்வரும் அடிப்படை இலக்கிய நூல்கள் இயற்றப்பட்ட / தொகுக்கப்பட்ட தோராயமான காலத்தை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. ஆரம்பகால மராத்தியில் ஞானேஸ்வரி இயற்றப்படுதல்\n2. ஆரம்பகால வேத சமஸ்கிருதத்தில் ரிக்வேதம் தொகுக்கப்படுதல்\n3. செவ்வியல் தமிழில் தொல்காப்பியம் மற்றும் ஆரம்பகால சங்கப் பாடல்கள் தொகுக்கப்படுதல்\n4. ஆரம்பகால ஒடியாவில் மடலா பாஞ்சி கோயில் ஆவணங்கள் எழுதப்படுதல்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("2 - 3 - 4 - 1", "2 - 3 - 4 - 1"),
                ("3 - 2 - 4 - 1", "3 - 2 - 4 - 1"),
                ("2 - 3 - 1 - 4", "2 - 3 - 1 - 4"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order of classical literary milestones is:\n2. Rigveda (c. 1500–1000 BCE)\n→ 3. Tolkappiyam & Sangam corpus (c. 300 BCE – 300 CE)\n→ 4. Madala Panji temple chronicles (c. 11th–12th Century CE)\n→ 1. Dnyaneshwari by Sant Dnyaneshwar (1290 CE).\nSequence: 2 → 3 → 4 → 1.",
            "exp_ta": "செவ்வியல் இலக்கிய மைல்கற்களின் சரியான காலவரிசை:\n2. ரிக்வேதம் (பொ.ஆ.மு. 1500–1000)\n→ 3. தொல்காப்பியம் & சங்க இலக்கியங்கள் (பொ.ஆ.மு. 300 – பொ.ஆ. 300)\n→ 4. மடலா பாஞ்சி கோயில் பதிவுகள் (பொ.ஆ. 11–12 ஆம் நூற்றாண்டு)\n→ 1. ஞானேஸ்வரி (பொ.ஆ. 1290).\nவரிசை: 2 → 3 → 4 → 1.",
            "why_a_en": "Chronologically tracks Vedic (1500 BCE) -> Sangam (300 BCE) -> Madala Panji (11th C) -> Dnyaneshwari (1290 CE).",
            "why_a_ta": "வேதம் (பொ.ஆ.மு 1500) -> சங்கம் (பொ.ஆ.மு 300) -> மடலா பாஞ்சி (11-ஆம் நூ) -> ஞானேஸ்வரி (1290) என காலவரிசையைப் பின்பற்றுகிறது.",
            "why_b_en": "Places Sangam before Rigveda.",
            "why_b_ta": "ரிக்வேதத்திற்கு முன் சங்க இலக்கியத்தை வைக்கிறது.",
            "why_c_en": "Swaps Dnyaneshwari and Madala Panji.",
            "why_c_ta": "ஞானேஸ்வரி மற்றும் மடலா பாஞ்சியை மாற்றுகிறது.",
            "why_d_en": "Incorrect presented stem order.",
            "why_d_ta": "வினாவில் கொடுக்கப்பட்ட தவறான வரிசை.",
            "tip_en": "High antiquity (>1500 years) is a primary test for Classical status.",
            "tip_ta": "உயர்ந்த தொன்மை (>1500 ஆண்டுகள்) செம்மொழித் தகுதிக்கான முதன்மைத் தேர்வாகும்.",
            "fact_en": "Tolkappiyam is the oldest extant Tamil grammatical work.",
            "fact_ta": "தொல்காப்பியம் தற்போது கிடைத்துள்ள மிகப்பழமையான தமிழ் இலக்கண நூலாகும்."
        },
        # 18
        {
            "subtopic": "Official Languages Rules Evolution",
            "stem_en": "Arrange the following regulatory steps concerning the Official Languages Rules in chronological order:\n1. Framing and notification of the principal Official Languages Rules\n2. Major amendment to the Rules regarding communications in Region B\n3. Central Government amends rules regarding modern electronic communications\n4. Official Languages Act enacted containing rule-making power under Section 8\nSelect the correct answer using the codes given below:",
            "stem_ta": "அதிகாரப்பூர்வ மொழிகள் விதிகள் தொடர்பான பின்வரும் ஒழுங்குமுறை நடவடிக்கைகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. முதன்மை அதிகாரப்பூர்வ மொழிகள் விதிகள் உருவாக்கப்பட்டு அறிவிக்கப்படுதல்\n2. பிராந்தியம் B-ல் தகவல்தொடர்புகள் குறித்த விதிகளில் முக்கிய திருத்தம் மேற்கொள்ளப்படுதல்\n3. நவீன மின்னணு தகவல்தொடர்புகள் குறித்த விதிகளை மத்திய அரசு திருத்துதல்\n4. பிரிவு 8-ன் கீழ் விதி உருவாக்கும் அதிகாரத்தைக் கொண்ட அதிகாரப்பூர்வ மொழிகள் சட்டம் இயற்றப்படுதல்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("4 - 1 - 2 - 3", "4 - 1 - 2 - 3"),
                ("1 - 4 - 2 - 3", "1 - 4 - 2 - 3"),
                ("4 - 2 - 1 - 3", "4 - 2 - 1 - 3"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is:\n4. Section 8 rule-making power in Official Languages Act (1963)\n→ 1. Principal Official Languages Rules notified (1976)\n→ 2. First major amendment to the Rules (1987)\n→ 3. Amendment addressing electronic communications (2007).\nSequence: 4 → 1 → 2 → 3.",
            "exp_ta": "சரியான காலவரிசை:\n4. அதிகாரப்பூர்வ மொழிகள் சட்டம் பிரிவு 8 அதிகாரம் (1963)\n→ 1. முதன்மை அதிகாரப்பூர்வ மொழிகள் விதிகள் அறிவிக்கப்படுதல் (1976)\n→ 2. விதிகளில் முதல் முக்கிய திருத்தம் (1987)\n→ 3. மின்னணு தகவல்தொடர்பு திருத்தம் (2007).\nவரிசை: 4 → 1 → 2 → 3.",
            "why_a_en": "Correct progression: 1963 -> 1976 -> 1987 -> 2007.",
            "why_a_ta": "சரியான வளர்ச்சி: 1963 -> 1976 -> 1987 -> 2007.",
            "why_b_en": "Places 1976 Rules before parent 1963 Act.",
            "why_b_ta": "தாய் சட்டமான 1963-க்கு முன் 1976 விதிகளை வைக்கிறது.",
            "why_c_en": "Places 1987 amendment before 1976 principal rules.",
            "why_c_ta": "1976 முதன்மை விதிகளுக்கு முன் 1987 திருத்தத்தை வைக்கிறது.",
            "why_d_en": "Incorrect presented stem order.",
            "why_d_ta": "வினாவில் கொடுக்கப்பட்ட தவறான வரிசை.",
            "tip_en": "Subordinate legislation: Act (1963) → Rules (1976) → Amendments (1987, 2007).",
            "tip_ta": "துணைச் சட்டம்: சட்டம் (1963) → விதிகள் (1976) → திருத்தங்கள் (1987, 2007).",
            "fact_en": "The 1976 Rules were framed pursuant to Section 8 of the 1963 Act.",
            "fact_ta": "1976 விதிகள் 1963 சட்டத்தின் பிரிவு 8-ன் படி உருவாக்கப்பட்டன."
        },
        # 19
        {
            "subtopic": "Language Amendments Sequence",
            "stem_en": "Arrange the following Constitutional Amendment Acts concerning the Eighth Schedule in chronological order:\n1. 96th Constitutional Amendment Act (substituting 'Odia' for 'Oriya')\n2. 21st Constitutional Amendment Act (adding Sindhi)\n3. 92nd Constitutional Amendment Act (adding Bodo, Dogri, Maithili, Santhali)\n4. 71st Constitutional Amendment Act (adding Konkani, Manipuri, Nepali)\nSelect the correct answer using the codes given below:",
            "stem_ta": "எட்டாவது அட்டவணை தொடர்பான பின்வரும் அரசியலமைப்பு திருத்தச் சட்டங்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. 96வது அரசியலமைப்பு திருத்தச் சட்டம் ('ஒரியா' என்பதற்குப் பதிலாக 'ஒடியா' என மாற்றம்)\n2. 21வது அரசியலமைப்பு திருத்தச் சட்டம் (சிந்தியைச் சேர்த்தல்)\n3. 92வது அரசியலமைப்பு திருத்தச் சட்டம் (போடோ, டோக்ரி, மைதிலி, சந்தாலியைச் சேர்த்தல்)\n4. 71வது அரசியலமைப்பு திருத்தச் சட்டம் (கொங்கணி, மணிப்பூரி, நேபாளியைச் சேர்த்தல்)\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("2 - 4 - 3 - 1", "2 - 4 - 3 - 1"),
                ("4 - 2 - 3 - 1", "4 - 2 - 3 - 1"),
                ("2 - 3 - 4 - 1", "2 - 3 - 4 - 1"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order of the Amendment Acts is:\n2. 21st Amendment Act (1967)\n→ 4. 71st Amendment Act (1992)\n→ 3. 92nd Amendment Act (2003)\n→ 1. 96th Amendment Act (2011).\nSequence: 2 → 4 → 3 → 1.",
            "exp_ta": "திருத்தச் சட்டங்களின் சரியான காலவரிசை:\n2. 21வது திருத்தச் சட்டம் (1967)\n→ 4. 71வது திருத்தச் சட்டம் (1992)\n→ 3. 92வது திருத்தச் சட்டம் (2003)\n→ 1. 96வது திருத்தச் சட்டம் (2011).\nவரிசை: 2 → 4 → 3 → 1.",
            "why_a_en": "Matches 1967, 1992, 2003, and 2011 amendment enactments.",
            "why_a_ta": "1967, 1992, 2003 மற்றும் 2011 திருத்தச் சட்டங்களைச் சரியாகப் பொருத்துகிறது.",
            "why_b_en": "Places 71st before 21st.",
            "why_b_ta": "21வதுக்கு முன் 71வது திருத்தத்தை வைக்கிறது.",
            "why_c_en": "Places 92nd before 71st.",
            "why_c_ta": "71வதுக்கு முன் 92வது திருத்தத்தை வைக்கிறது.",
            "why_d_en": "Incorrect presented stem order.",
            "why_d_ta": "வினாவில் கொடுக்கப்பட்ட தவறான வரிசை.",
            "tip_en": "Remember the amendment numbers: 21st (1967) → 71st (1992) → 92nd (2003) → 96th (2011).",
            "tip_ta": "திருத்த எண்களை நினைவில் கொள்க: 21வது (1967) → 71வது (1992) → 92வது (2003) → 96வது (2011).",
            "fact_en": "The 96th Amendment Act was notified on 23 September 2011.",
            "fact_ta": "96வது திருத்தச் சட்டம் 23 செப்டம்பர் 2011 அன்று அறிவிக்கப்பட்டது."
        },
        # 20
        {
            "subtopic": "Hindi Institutions Founding Timeline",
            "stem_en": "Arrange the founding of the following language promotional bodies in chronological order:\n1. Kendriya Hindi Sansthan established at Agra\n2. Dakshin Bharat Hindi Prachar Sabha founded by Mahatma Gandhi\n3. Department of Official Language established under Ministry of Home Affairs\n4. Kendriya Hindi Samiti constituted under the Prime Minister\nSelect the correct answer using the codes given below:",
            "stem_ta": "பின்வரும் மொழி மேம்பாட்டு அமைப்புகள் நிறுவப்பட்டதை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. ஆக்ராவில் கேந்திரிய இந்தி சன்ஸ்தான் நிறுவப்படுதல்\n2. மகாத்மா காந்தியால் தட்சிண பாரத இந்தி பிரச்சார சபா நிறுவப்படுதல்\n3. உள்துறை அமைச்சகத்தின் கீழ் அதிகாரப்பூர்வ மொழித் துறை நிறுவப்படுதல்\n4. பிரதமர் தலைமையில் கேந்திரிய இந்தி சமிதி அமைக்கப்படுதல்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("2 - 1 - 4 - 3", "2 - 1 - 4 - 3"),
                ("1 - 2 - 4 - 3", "1 - 2 - 4 - 3"),
                ("2 - 4 - 1 - 3", "2 - 4 - 1 - 3"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is:\n2. Dakshin Bharat Hindi Prachar Sabha founded (1918)\n→ 1. Kendriya Hindi Sansthan established (1960)\n→ 4. Kendriya Hindi Samiti constituted (1967)\n→ 3. Department of Official Language created (1975).\nSequence: 2 → 1 → 4 → 3.",
            "exp_ta": "சரியான காலவரிசை:\n2. தட்சிண பாரத இந்தி பிரச்சார சபா நிறுவப்படுதல் (1918)\n→ 1. கேந்திரிய இந்தி சன்ஸ்தான் நிறுவப்படுதல் (1960)\n→ 4. கேந்திரிய இந்தி சமிதி அமைக்கப்படுதல் (1967)\n→ 3. அதிகாரப்பூர்வ மொழித் துறை உருவாக்கப்படுதல் (1975).\nவரிசை: 2 → 1 → 4 → 3.",
            "why_a_en": "Accurately traces 1918, 1960, 1967, and 1975 institutional milestones.",
            "why_a_ta": "1918, 1960, 1967 மற்றும் 1975 ஆகிய நிறுவன மைல்கற்களைத் துல்லியமாகப் பின்பற்றுகிறது.",
            "why_b_en": "Places 1960 Sansthan before 1918 DBHPS.",
            "why_b_ta": "1918 சபாவுக்கு முன் 1960 சன்ஸ்தானை வைக்கிறது.",
            "why_c_en": "Places 1967 Samiti before 1960 Sansthan.",
            "why_c_ta": "1960 சன்ஸ்தானுக்கு முன் 1967 சமிதியை வைக்கிறது.",
            "why_d_en": "Incorrect presented stem order.",
            "why_d_ta": "வினாவில் கொடுக்கப்பட்ட தவறான வரிசை.",
            "tip_en": "Gandhi founded DBHPS in Madras in 1918 to voluntarily popularize Hindi in South India.",
            "tip_ta": "தென்னிந்தியாவில் இந்தியை விருப்பத்தின் பேரில் பரப்ப காந்தி 1918-ல் மதராஸில் தட்சிண பாரத இந்தி பிரச்சார சபையைத் தொடங்கினார்.",
            "fact_en": "Parliament declared DBHPS an Institution of National Importance in 1964.",
            "fact_ta": "நாடாளுமன்றம் 1964-ல் DBHPS-ஐ தேசிய முக்கியத்துவம் வாய்ந்த நிறுவனமாக அறிவித்தது."
        },
        # 21
        {
            "subtopic": "North-Eastern Languages Recognition Timeline",
            "stem_en": "Arrange the following recognition milestones of North-Eastern languages in chronological order:\n1. Manipuri (Meitei) included in the Eighth Schedule\n2. Assamese recognized in the original Eighth Schedule\n3. Bodo included in the Eighth Schedule\n4. Assamese conferred Classical Language status\nSelect the correct answer using the codes given below:",
            "stem_ta": "வடகிழக்கு மொழிகளின் பின்வரும் அங்கீகார மைல்கற்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. மணிப்பூரி (மெய்தேய்) எட்டாவது அட்டவணையில் சேர்க்கப்படுதல்\n2. அசல் எட்டாவது அட்டவணையில் அஸ்ஸாமி அங்கீகரிக்கப்படுதல்\n3. போடோ எட்டாவது அட்டவணையில் சேர்க்கப்படுதல்\n4. அஸ்ஸாமிக்கு செம்மொழித் தகுதி வழங்கப்படுதல்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("2 - 1 - 3 - 4", "2 - 1 - 3 - 4"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4"),
                ("2 - 3 - 1 - 4", "2 - 3 - 1 - 4"),
                ("3 - 2 - 1 - 4", "3 - 2 - 1 - 4")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is:\n2. Assamese in original 8th Schedule (1950)\n→ 1. Manipuri added by 71st Amendment (1992)\n→ 3. Bodo added by 92nd Amendment (2003)\n→ 4. Assamese declared Classical Language (October 2024).\nSequence: 2 → 1 → 3 → 4.",
            "exp_ta": "சரியான காலவரிசை:\n2. அசல் 8வது அட்டவணையில் அஸ்ஸாமி (1950)\n→ 1. 71வது திருத்தத்தால் மணிப்பூரி சேர்க்கப்படுதல் (1992)\n→ 3. 92வது திருத்தத்தால் போடோ சேர்க்கப்படுதல் (2003)\n→ 4. அஸ்ஸாமி செம்மொழியாக அறிவிக்கப்படுதல் (அக்டோபர் 2024).\nவரிசை: 2 → 1 → 3 → 4.",
            "why_a_en": "Accurately follows 1950, 1992, 2003, and 2024 milestones.",
            "why_a_ta": "1950, 1992, 2003 மற்றும் 2024 மைல்கற்களைத் துல்லியமாகப் பின்பற்றுகிறது.",
            "why_b_en": "Places Manipuri before original Assamese recognition.",
            "why_b_ta": "அஸ்ஸாமி அங்கீகாரத்திற்கு முன் மணிப்பூரியை வைக்கிறது.",
            "why_c_en": "Swaps Manipuri (1992) and Bodo (2003).",
            "why_c_ta": "மணிப்பூரி (1992) மற்றும் போடோவை (2003) மாற்றுகிறது.",
            "why_d_en": "Places Bodo first.",
            "why_d_ta": "போடோவை முதலில் வைக்கிறது.",
            "tip_en": "Assamese (1950) → Manipuri (1992) → Bodo (2003) → Assamese Classical (2024).",
            "tip_ta": "அஸ்ஸாமி (1950) → மணிப்பூரி (1992) → போடோ (2003) → அஸ்ஸாமி செம்மொழி (2024).",
            "fact_en": "Manipuri is written in Bengali script and the indigenous Meitei Mayek script.",
            "fact_ta": "மணிப்பூரி வங்காள வரிவடிவத்திலும் சுதேச மெய்தேய் மாயேக் வரிவடிவத்திலும் எழுதப்படுகிறது."
        },
        # 22
        {
            "subtopic": "1950s Language Commission Timeline",
            "stem_en": "Arrange the following procedural steps of the first language review under Article 344 in chronological order:\n1. B.G. Kher Commission Report formally tabled in Parliament\n2. Appointment of the Official Language Commission by the President\n3. Report of the Parliamentary Committee under G.B. Pant submitted to the President\n4. B.G. Kher Commission submits its Report to President Dr. Rajendra Prasad\nSelect the correct answer using the codes given below:",
            "stem_ta": "சரத்து 344-ன் கீழான முதல் மொழி மறுஆய்வின் பின்வரும் நடைமுறைப் படிகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. பி.ஜி. கேர் ஆணைய அறிக்கை நாடாளுமன்றத்தில் முறையாக வைக்கப்படுதல்\n2. குடியரசுத் தலைவரால் அதிகாரப்பூர்வ மொழி ஆணையம் நியமிக்கப்படுதல்\n3. ஜி.பி. பந்த் தலைமையிலான நாடாளுமன்றக் குழு அறிக்கை குடியரசுத் தலைவரிடம் சமர்ப்பிக்கப்படுதல்\n4. பி.ஜி. கேர் ஆணையம் தனது அறிக்கையை குடியரசுத் தலைவர் டாக்டர் ராஜேந்திர பிரசாத்திடம் சமர்ப்பித்தல்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("2 - 4 - 1 - 3", "2 - 4 - 1 - 3"),
                ("4 - 2 - 1 - 3", "4 - 2 - 1 - 3"),
                ("2 - 1 - 4 - 3", "2 - 1 - 4 - 3"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is:\n2. Kher Commission appointed (June 1955)\n→ 4. Kher Commission submits report to President (July 1956)\n→ 1. Report tabled in Parliament (August 1957)\n→ 3. Pant Committee submits its report to President (February 1959 / completed 1958).\nSequence: 2 → 4 → 1 → 3.",
            "exp_ta": "சரியான காலவரிசை:\n2. கேர் ஆணையம் நியமிக்கப்படுதல் (ஜூன் 1955)\n→ 4. கேர் ஆணையம் அறிக்கை சமர்ப்பித்தல் (ஜூலை 1956)\n→ 1. அறிக்கை நாடாளுமன்றத்தில் வைக்கப்படுதல் (ஆகஸ்ட் 1957)\n→ 3. பந்த் குழு அறிக்கை குடியரசுத் தலைவரிடம் சமர்ப்பிக்கப்படுதல் (1958/1959).\nவரிசை: 2 → 4 → 1 → 3.",
            "why_a_en": "Accurately sequences the 1955-1959 Article 344 procedural timeline.",
            "why_a_ta": "1955-1959 சரத்து 344 நடைமுறை காலக்கோடு துல்லியமாகப் பொருந்துகிறது.",
            "why_b_en": "Places report submission before commission appointment.",
            "why_b_ta": "நியமனத்திற்கு முன் அறிக்கை சமர்ப்பிப்பை வைக்கிறது.",
            "why_c_en": "Places tabling in Parliament before report submission.",
            "why_c_ta": "அறிக்கை சமர்ப்பிப்பிற்கு முன் நாடாளுமன்றத்தில் வைப்பதை வைக்கிறது.",
            "why_d_en": "Incorrect presented stem order.",
            "why_d_ta": "வினாவில் கொடுக்கப்பட்ட தவறான வரிசை.",
            "tip_en": "Appointment (1955) → Submission (1956) → Tabled in Parliament (1957) → Pant Committee Report (1958/59).",
            "tip_ta": "நியமனம் (1955) → சமர்ப்பிப்பு (1956) → நாடாளுமன்றத்தில் வைத்தல் (1957) → பந்த் குழு அறிக்கை (1958/59).",
            "fact_en": "Article 344(5) requires the Committee to report its opinion to the President.",
            "fact_ta": "சரத்து 344(5) நாடாளுமன்றக் குழு தனது கருத்தை குடியரசுத் தலைவரிடம் அறிக்கையாகச் சமர்ப்பிக்க வேண்டும் எனக் கூறுகிறது."
        },
        # 23
        {
            "subtopic": "Indo-Aryan Classical Languages Sequence",
            "stem_en": "Arrange the conferment of Classical status on the following Indo-Aryan languages in chronological order:\n1. Odia\n2. Sanskrit\n3. Bengali, Marathi, and Assamese\n4. Formulation of Classical criteria\nSelect the correct answer using the codes given below:",
            "stem_ta": "பின்வரும் இந்தோ-ஆரிய மொழிகளுக்கு செம்மொழித் தகுதி வழங்கப்பட்டதை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. ஒடியா\n2. சமஸ்கிருதம்\n3. வங்காள மொழி, மராத்தி மற்றும் அஸ்ஸாமி\n4. செம்மொழி அளவுகோல்கள் உருவாக்கப்படுதல்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("4 - 2 - 1 - 3", "4 - 2 - 1 - 3"),
                ("2 - 4 - 1 - 3", "2 - 4 - 1 - 3"),
                ("4 - 1 - 2 - 3", "4 - 1 - 2 - 3"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is:\n4. Criteria formulated (2004)\n→ 2. Sanskrit declared Classical (2005)\n→ 1. Odia declared Classical (2014)\n→ 3. Bengali, Marathi, Assamese declared Classical (October 2024).\nSequence: 4 → 2 → 1 → 3.",
            "exp_ta": "சரியான காலவரிசை:\n4. அளவுகோல்கள் உருவாக்கப்படுதல் (2004)\n→ 2. சமஸ்கிருதம் அறிவிக்கப்படுதல் (2005)\n→ 1. ஒடியா அறிவிக்கப்படுதல் (2014)\n→ 3. வங்காள மொழி, மராத்தி, அஸ்ஸாமி அறிவிக்கப்படுதல் (அக்டோபர் 2024).\nவரிசை: 4 → 2 → 1 → 3.",
            "why_a_en": "Correct sequence matching 2004, 2005, 2014, and 2024.",
            "why_a_ta": "2004, 2005, 2014 மற்றும் 2024 ஆகிய ஆண்டுகளைச் சரியாகப் பொருத்தும் வரிசை.",
            "why_b_en": "Places Sanskrit before criteria creation.",
            "why_b_ta": "அளவுகோல் உருவாக்கத்திற்கு முன் சமஸ்கிருதத்தை வைக்கிறது.",
            "why_c_en": "Places Odia before Sanskrit.",
            "why_c_ta": "சமஸ்கிருதத்திற்கு முன் ஒடியாவை வைக்கிறது.",
            "why_d_en": "Incorrect presented stem order.",
            "why_d_ta": "வினாவில் கொடுக்கப்பட்ட தவறான வரிசை.",
            "tip_en": "Indo-Aryan classical timeline: Sanskrit (2005) → Odia (2014) → Bengali, Marathi, Assamese (2024).",
            "tip_ta": "இந்தோ-ஆரிய செம்மொழி காலக்கோடு: சமஸ்கிருதம் (2005) → ஒடியா (2014) → பெங்காலி, மராத்தி, அஸ்ஸாமி (2024).",
            "fact_en": "Odia was the first modern Indo-Aryan language to receive classical status.",
            "fact_ta": "நவீன இந்தோ-ஆரிய மொழிகளில் முதலில் செம்மொழித் தகுதி பெற்றது ஒடியா ஆகும்."
        },
        # 24
        {
            "subtopic": "Tamil Nadu Anti-Hindi Milestones",
            "stem_en": "Arrange the following anti-Hindi resistance milestones in Tamil Nadu in chronological order:\n1. State-wide anti-Hindi student protests result in violence and self-immolations\n2. Tamil Nadu Assembly passes official resolution adopting Two-Language Policy\n3. First anti-Hindi agitation launched by Periyar and Thalamuthu-Natarajan sacrifice\n4. Parliament enacts Official Languages Act with ambiguous 'may' clause provoking outrage\nSelect the correct answer using the codes given below:",
            "stem_ta": "தமிழ்நாட்டின் இந்தி எதிர்ப்புப் போராட்ட மைல்கற்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. மாநிலம் தழுவிய இந்தி எதிர்ப்பு மாணவர் போராட்டங்கள் மற்றும் தீக்குளிப்பு தியாகங்கள் ஏற்படுதல்\n2. தமிழ்நாடு சட்டமன்றம் இருமொழிக் கொள்கையை ஏற்று அதிகாரப்பூர்வ தீர்மானம் நிறைவேற்றுதல்\n3. தாளமுத்து-நடராசன் தியாகத்துடன் பெரியாரால் முதல் இந்தி எதிர்ப்புப் போராட்டம் தொடங்கப்படுதல்\n4. எதிர்ப்பைத் தூண்டிய தெளிவற்ற 'may' பிரிவுடன் நாடாளுமன்றம் அதிகாரப்பூர்வ மொழிகள் சட்டத்தை இயற்றுதல்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("3 - 4 - 1 - 2", "3 - 4 - 1 - 2"),
                ("4 - 3 - 1 - 2", "4 - 3 - 1 - 2"),
                ("3 - 1 - 4 - 2", "3 - 1 - 4 - 2"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is:\n3. First anti-Hindi agitation with Thalamuthu and Natarajan sacrifices (1938–1939)\n→ 4. Official Languages Act with 'may' clause enacted (1963)\n→ 1. Anti-Hindi student protests and self-immolations peak (January–February 1965)\n→ 2. Two-Language Policy Assembly resolution passed under Annadurai (23 January 1968).\nSequence: 3 → 4 → 1 → 2.",
            "exp_ta": "சரியான காலவரிசை:\n3. தாளமுத்து-நடராசன் தியாகத்துடன் முதல் போராட்டம் (1938)\n→ 4. அதிகாரப்பூர்வ மொழிகள் சட்டம் 1963 இயற்றப்படுதல் (1963)\n→ 1. தீவிர மாணவர் போராட்டங்கள் மற்றும் தீக்குளிப்புகள் (1965)\n→ 2. அண்ணா தலைமையில் இருமொழிக் கொள்கைத் தீர்மானம் (1968).\nவரிசை: 3 → 4 → 1 → 2.",
            "why_a_en": "Accurately spans the heroic resistance timeline from 1938 to 1968.",
            "why_a_ta": "1938 முதல் 1968 வரையிலான வீரமிக்க போராட்ட காலக்கோடு துல்லியமாகப் பொருந்துகிறது.",
            "why_b_en": "Places 1963 Act before 1938 first agitation.",
            "why_b_ta": "1938 முதல் போராட்டத்திற்கு முன் 1963 சட்டத்தை வைக்கிறது.",
            "why_c_en": "Places 1965 agitation before 1963 Act.",
            "why_c_ta": "1963 சட்டத்திற்கு முன் 1965 போராட்டத்தை வைக்கிறது.",
            "why_d_en": "Incorrect presented stem order.",
            "why_d_ta": "வினாவில் கொடுக்கப்பட்ட தவறான வரிசை.",
            "tip_en": "Thalamuthu and Natarajan died in prison during the 1938–39 agitation against Rajaji's ministry.",
            "tip_ta": "ராஜாஜி அமைச்சரவைக்கு எதிரான 1938-39 போராட்டத்தின் போது தாளமுத்துவும் நடராசனும் சிறையிலேயே வீரமரணமடைந்தனர்.",
            "fact_en": "The Chennai Central Railway station and several public buildings commemorate language martyrs.",
            "fact_ta": "மொழிப்போர் தியாகிகளை நினைவுகூரும் வகையில் தமிழ்நாட்டில் நினைவுத் தூண்கள் அமைக்கப்பட்டுள்ளன."
        },
        # 25
        {
            "subtopic": "Overall Constitutional Language Roadmap (1949–2024)",
            "stem_en": "Arrange the following panoramic milestones in the history of Indian language policy in chronological order:\n1. Tamil Nadu Legislative Assembly adopts Two-Language Policy resolution under C.N. Annadurai\n2. Constituent Assembly adopts Munshi-Ayyangar formula establishing Hindi in Devanagari script as official language\n3. 92nd Constitutional Amendment Act expands the Eighth Schedule to 22 languages\n4. Union Cabinet confers Classical Language status upon five languages expanding the classical list to 11\nSelect the correct answer using the codes given below:",
            "stem_ta": "இந்திய மொழிக் கொள்கை வரலாற்றின் பின்வரும் விரிவான மைல்கற்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. சி.என். அண்ணாதுரை தலைமையில் தமிழ்நாடு சட்டமன்றம் இருமொழிக் கொள்கைத் தீர்மானத்தை ஏற்றுக்கொள்வது\n2. அரசியலமைப்பு நிர்ணய சபை தேவநாகரி இந்தியை அதிகாரப்பூர்வ மொழியாக முன்ஷி-அய்யங்கார் சூத்திரத்தை ஏற்றுக்கொள்வது\n3. 92வது அரசியலமைப்பு திருத்தச் சட்டம் எட்டாவது அட்டவணையை 22 மொழிகளாக விரிவாக்குவது\n4. மத்திய அமைச்சரவை ஐந்து மொழிகளுக்கு செம்மொழித் தகுதி வழங்கி செம்மொழிப் பட்டியலை 11 ஆக விரிவாக்குவது\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("2 - 1 - 3 - 4", "2 - 1 - 3 - 4"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4"),
                ("2 - 3 - 1 - 4", "2 - 3 - 1 - 4"),
                ("3 - 2 - 1 - 4", "3 - 2 - 1 - 4")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order spanning 75 years is:\n2. Munshi-Ayyangar formula adopted (14 September 1949)\n→ 1. Tamil Nadu Two-Language resolution (23 January 1968)\n→ 3. 92nd Amendment Act takes Eighth Schedule to 22 languages (January 2004 / enacted 2003)\n→ 4. Union Cabinet declares 5 new Classical Languages (3 October 2024).\nSequence: 2 → 1 → 3 → 4.",
            "exp_ta": "75 ஆண்டுகால வரலாற்றின் சரியான காலவரிசை:\n2. முன்ஷி-அய்யங்கார் சூத்திரம் ஏற்கப்படுதல் (14 செப்டம்பர் 1949)\n→ 1. தமிழ்நாடு இருமொழிக் கொள்கைத் தீர்மானம் (23 ஜனவரி 1968)\n→ 3. 92வது திருத்தம் 22 மொழிகளாக உயர்த்துதல் (2003)\n→ 4. மத்திய அமைச்சரவை 5 புதிய செம்மொழிகளை அறிவித்தல் (3 அக்டோபர் 2024).\nவரிசை: 2 → 1 → 3 → 4.",
            "why_a_en": "Accurately spans the 75-year timeline from 1949 to 2024.",
            "why_a_ta": "1949 முதல் 2024 வரையிலான 75 ஆண்டுகால காலக்கோட்டை துல்லியமாகப் பொருத்துகிறது.",
            "why_b_en": "Places 1968 resolution before 1949 Constituent Assembly.",
            "why_b_ta": "1949 அரசியலமைப்பு சபைக்கு முன் 1968 தீர்மானத்தை வைக்கிறது.",
            "why_c_en": "Places 2003 amendment before 1968 resolution.",
            "why_c_ta": "1968 தீர்மானத்திற்கு முன் 2003 திருத்தத்தை வைக்கிறது.",
            "why_d_en": "Places 2003 amendment first.",
            "why_d_ta": "2003 திருத்தத்தை முதலில் வைக்கிறது.",
            "tip_en": "Pan-Indian roadmap: Munshi-Ayyangar (1949) → TN Two-Language (1968) → 22 Languages (2003) → 11 Classical (2024).",
            "tip_ta": "அகில இந்திய வரைபடம்: முன்ஷி-அய்யங்கார் (1949) → தமிழக இருமொழி (1968) → 22 மொழிகள் (2003) → 11 செம்மொழிகள் (2024).",
            "fact_en": "Language policy reflects India's vibrant federal bargaining and constitutional evolution.",
            "fact_ta": "மொழிக் கொள்கை இந்தியாவின் துடிப்பான கூட்டாட்சி மற்றும் அரசியலமைப்பு பரிணாமத்தைப் பிரதிபலிக்கிறது."
        }
    ]

    questions = []
    for idx, item in enumerate(raw_data, start=1):
        qid = f"OL_C_{idx:03d}"
        opts = item["options"]
        correct_key = item["correct_key"]
        
        q = make_ol_q(
            qid=qid,
            diff="Medium" if idx <= 15 else "Hard",
            qtype="Chronology",
            subtopic=item["subtopic"],
            en_stem=item["stem_en"],
            ta_stem=item["stem_ta"],
            en_a=opts[0][0],
            ta_a=opts[0][1],
            en_b=opts[1][0],
            ta_b=opts[1][1],
            en_c=opts[2][0],
            ta_c=opts[2][1],
            en_d=opts[3][0],
            ta_d=opts[3][1],
            correct_key=correct_key,
            exp_en=item["exp_en"],
            exp_ta=item["exp_ta"],
            why_a_en=item["why_a_en"],
            why_a_ta=item["why_a_ta"],
            why_b_en=item["why_b_en"],
            why_b_ta=item["why_b_ta"],
            why_c_en=item["why_c_en"],
            why_c_ta=item["why_c_ta"],
            why_d_en=item["why_d_en"],
            why_d_ta=item["why_d_ta"],
            tip_en=item["tip_en"],
            tip_ta=item["tip_ta"],
            fact_en=item["fact_en"],
            fact_ta=item["fact_ta"],
            tags=["polity", "official_language", "chronology", item["subtopic"].lower().replace(" ", "_")]
        )
        questions.append(q)
    return questions

def build_chronology_file():
    qs = get_chronology_questions()
    print(f"Generated {len(qs)} raw Chronology questions for Official Language.")
    balanced = randomize_and_balance_dataset(qs, seed=63)
    
    out_dir = os.path.join("data", "questions", "polity")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "official_language_chronology.json")
    
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)
    print(f"Saved balanced Chronology MCQs to {out_path}")
    
    rep = ContentValidator.validate_file(out_path, expected_count=25, expected_prefix="OL_C_")
    print(f"ContentValidator: {'PASS' if rep.is_valid else 'FAIL'} | Total: {rep.total_audited}")
    print(f"Keys: {rep.key_distribution}")
    if not rep.is_valid:
        for iss in rep.issues:
            print("  Issue:", iss.severity, iss.field_name, iss.message)
            
    c_rep = ChronologyValidator.validate_file(out_path)
    print(f"ChronologyValidator: {'PASS' if c_rep.is_valid else 'FAIL'}")
    if not c_rep.is_valid:
        for iss in c_rep.issues:
            print("  Chronology Issue:", iss)
    return rep.is_valid and c_rep.is_valid

if __name__ == "__main__":
    build_chronology_file()
