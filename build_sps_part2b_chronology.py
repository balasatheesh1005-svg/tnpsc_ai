# -*- coding: utf-8 -*-
"""
Special Provisions for States - Part 2B Chronology MCQs Generator (25 MCQs: SPS_C_001 to SPS_C_025)
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
from special_provisions_states_mcq_helper import make_sps_q
from tools.nova_content_engine.answer_randomizer import randomize_and_balance_dataset
from tools.nova_content_engine.validator import ContentValidator
from tools.nova_content_engine.chronology_validator import ChronologyValidator

def get_chronology_questions():
    raw_data = [
        # 1
        {
            "subtopic": "Early Constitutional Amendments on Special Provisions",
            "stem_en": "Arrange the following Constitutional Amendment Acts in chronological order:\n1. 32nd Constitutional Amendment Act (Article 371D for Andhra Pradesh)\n2. 13th Constitutional Amendment Act (Article 371A for Nagaland)\n3. 27th Constitutional Amendment Act (Article 371C for Manipur)\n4. 22nd Constitutional Amendment Act (Article 371B for Assam)\nSelect the correct answer using the codes given below:",
            "stem_ta": "பின்வரும் அரசியலமைப்பு திருத்தச் சட்டங்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. 32வது அரசியலமைப்பு திருத்தச் சட்டம் (ஆந்திராவிற்கு சரத்து 371D)\n2. 13வது அரசியலமைப்பு திருத்தச் சட்டம் (நாகாலாந்திற்கு சரத்து 371A)\n3. 27வது அரசியலமைப்பு திருத்தச் சட்டம் (மணிப்பூருக்கு சரத்து 371C)\n4. 22வது அரசியலமைப்பு திருத்தச் சட்டம் (அசாமிற்கு சரத்து 371B)\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("2 - 4 - 3 - 1", "2 - 4 - 3 - 1"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4"),
                ("2 - 3 - 4 - 1", "2 - 3 - 4 - 1"),
                ("4 - 2 - 3 - 1", "4 - 2 - 3 - 1")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is:\n2. 13th Amendment Act (1962)\n→ 4. 22nd Amendment Act (1969)\n→ 3. 27th Amendment Act (1971)\n→ 1. 32nd Amendment Act (1973).\nSequence: 2 → 4 → 3 → 1.",
            "exp_ta": "சரியான காலவரிசை:\n2. 13வது திருத்தச் சட்டம் (1962)\n→ 4. 22வது திருத்தச் சட்டம் (1969)\n→ 3. 27வது திருத்தச் சட்டம் (1971)\n→ 1. 32வது திருத்தச் சட்டம் (1973).\nவரிசை: 2 → 4 → 3 → 1.",
            "why_a_en": "Correctly follows the chronological sequence: 1962 -> 1969 -> 1971 -> 1973.",
            "why_a_ta": "1962 -> 1969 -> 1971 -> 1973 என்ற காலவரிசையைச் சரியாகப் பின்பற்றுகிறது.",
            "why_b_en": "Incorrect presented stem sequence.",
            "why_b_ta": "வினாவில் கொடுக்கப்பட்ட தவறான வரிசை.",
            "why_c_en": "Places 27th Amendment before 22nd Amendment.",
            "why_c_ta": "22வது திருத்தத்திற்கு முன் 27வது திருத்தத்தை தவறாக வைக்கிறது.",
            "why_d_en": "Places 22nd Amendment before 13th Amendment.",
            "why_d_ta": "13வது திருத்தத்திற்கு முன் 22வது திருத்தத்தை தவறாக வைக்கிறது.",
            "tip_en": "Order: 13th (1962) -> 22nd (1969) -> 27th (1971) -> 32nd (1973).",
            "tip_ta": "வரிசை: 13வது (1962) -> 22வது (1969) -> 27வது (1971) -> 32வது (1973).",
            "fact_en": "These amendments reflected the progressive reorganisation of north-eastern tribal regions.",
            "fact_ta": "இத்திருத்தங்கள் வடகிழக்கு பழங்குடியினர் பகுதிகளின் படிப்படியான மறுசீரமைப்பைப் பிரதிபலித்தன."
        },
        # 2
        {
            "subtopic": "Statehood Dates of North-Eastern States",
            "stem_en": "Arrange the following North-Eastern States in the chronological order of their attainment of full statehood:\n1. Sikkim\n2. Nagaland\n3. Mizoram\n4. Manipur\nSelect the correct answer using the codes given below:",
            "stem_ta": "பின்வரும் வடகிழக்கு மாநிலங்களை அவை முழு மாநில அந்தஸ்து பெற்ற காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. சிக்கிம்\n2. நாகாலாந்து\n3. மிசோரம்\n4. மணிப்பூர்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("2 - 4 - 1 - 3", "2 - 4 - 1 - 3"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4"),
                ("2 - 1 - 4 - 3", "2 - 1 - 4 - 3"),
                ("4 - 2 - 1 - 3", "4 - 2 - 1 - 3")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is:\n2. Nagaland (1 December 1963)\n→ 4. Manipur (21 January 1972)\n→ 1. Sikkim (16 May 1975)\n→ 3. Mizoram (20 February 1987).\nSequence: 2 → 4 → 1 → 3.",
            "exp_ta": "சரியான காலவரிசை:\n2. நாகாலாந்து (1 டிசம்பர் 1963)\n→ 4. மணிப்பூர் (21 ஜனவரி 1972)\n→ 1. சிக்கிம் (16 மே 1975)\n→ 3. மிசோரம் (20 பிப்ரவரி 1987).\nவரிசை: 2 → 4 → 1 → 3.",
            "why_a_en": "Correct sequence: 1963 -> 1972 -> 1975 -> 1987.",
            "why_a_ta": "சரியான வரிசை: 1963 -> 1972 -> 1975 -> 1987.",
            "why_b_en": "Incorrect presented stem sequence.",
            "why_b_ta": "வினாவில் கொடுக்கப்பட்ட தவறான வரிசை.",
            "why_c_en": "Places Sikkim before Manipur.",
            "why_c_ta": "மணிப்பூருக்கு முன் சிக்கிமைத் தவறாக வைக்கிறது.",
            "why_d_en": "Places Manipur before Nagaland.",
            "why_d_ta": "நாகாலாந்திற்கு முன் மணிப்பூரைத் தவறாக வைக்கிறது.",
            "tip_en": "Statehood order: Nagaland (1963) -> Manipur (1972) -> Sikkim (1975) -> Mizoram (1987).",
            "tip_ta": "மாநில அந்தஸ்து வரிசை: நாகாலாந்து (1963) -> மணிப்பூர் (1972) -> சிக்கிம் (1975) -> மிசோரம் (1987).",
            "fact_en": "Manipur gained statehood alongside Meghalaya and Tripura on 21 January 1972.",
            "fact_ta": "மணிப்பூர் மேகாலயா மற்றும் திரிபுராவுடன் இணைந்து 1972 ஜனவரி 21 அன்று மாநில அந்தஸ்தைப் பெற்றது."
        },
        # 3
        {
            "subtopic": "Historic Political Accords in North-East",
            "stem_en": "Arrange the following historic political accords and agreements in chronological order:\n1. Mizo Peace Accord\n2. 16-Point Agreement with Naga People's Convention\n3. Shillong Accord\n4. North-Eastern Areas Reorganisation Act\nSelect the correct answer using the codes given below:",
            "stem_ta": "பின்வரும் வரலாற்றுச் சிறப்புமிக்க அரசியல் உடன்படிக்கைகள் மற்றும் ஒப்பந்தங்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. மிசோ அமைதி ஒப்பந்தம்\n2. நாகா மக்கள் மாநாட்டுடனான 16 அம்ச ஒப்பந்தம்\n3. ஷில்லாங் ஒப்பந்தம்\n4. வடகிழக்குப் பகுதிகள் மறுசீரமைப்புச் சட்டம்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("2 - 4 - 3 - 1", "2 - 4 - 3 - 1"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4"),
                ("2 - 3 - 4 - 1", "2 - 3 - 4 - 1"),
                ("4 - 2 - 3 - 1", "4 - 2 - 3 - 1")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is:\n2. 16-Point Agreement (July 1960)\n→ 4. North-Eastern Areas Reorganisation Act (December 1971)\n→ 3. Shillong Accord (November 1975)\n→ 1. Mizo Peace Accord (June 1986).\nSequence: 2 → 4 → 3 → 1.",
            "exp_ta": "சரியான காலவரிசை:\n2. 16 அம்ச ஒப்பந்தம் (ஜூலை 1960)\n→ 4. வடகிழக்குப் பகுதிகள் மறுசீரமைப்புச் சட்டம் (டிசம்பர் 1971)\n→ 3. ஷில்லாங் ஒப்பந்தம் (நவம்பர் 1975)\n→ 1. மிசோ அமைதி ஒப்பந்தம் (ஜூன் 1986).\nவரிசை: 2 → 4 → 3 → 1.",
            "why_a_en": "Accurately follows 1960 -> 1971 -> 1975 -> 1986.",
            "why_a_ta": "1960 -> 1971 -> 1975 -> 1986 என்ற காலவரிசையைத் துல்லியமாகப் பின்பற்றுகிறது.",
            "why_b_en": "Incorrect presented stem order.",
            "why_b_ta": "வினாவில் கொடுக்கப்பட்ட தவறான வரிசை.",
            "why_c_en": "Places Shillong Accord before 1971 Act.",
            "why_c_ta": "1971 சட்டத்திற்கு முன் ஷில்லாங் ஒப்பந்தத்தை வைக்கிறது.",
            "why_d_en": "Places 1971 Act first.",
            "why_d_ta": "1971 சட்டத்தை முதலில் தவறாக வைக்கிறது.",
            "tip_en": "Key accords: 16-Point (1960) -> Shillong (1975) -> Mizo Accord (1986).",
            "tip_ta": "முக்கிய ஒப்பந்தங்கள்: 16 அம்ச (1960) -> ஷில்லாங் (1975) -> மிசோ ஒப்பந்தம் (1986).",
            "fact_en": "Shillong Accord was signed with the Naga underground leaders under Governor L.P. Singh.",
            "fact_ta": "ஆளுநர் எல்.பி. சிங் முன்னிலையில் நாகா தலைவர்களுடன் ஷில்லாங் ஒப்பந்தம் கையெழுத்தானது."
        },
        # 4
        {
            "subtopic": "Special Provisions Amendments Later Phase",
            "stem_en": "Arrange the following Constitutional Amendment Acts in chronological order:\n1. 98th Constitutional Amendment Act (Article 371J for Karnataka)\n2. 36th Constitutional Amendment Act (Article 371F for Sikkim)\n3. 55th Constitutional Amendment Act (Article 371H for Arunachal Pradesh)\n4. 53rd Constitutional Amendment Act (Article 371G for Mizoram)\nSelect the correct answer using the codes given below:",
            "stem_ta": "பின்வரும் அரசியலமைப்பு திருத்தச் சட்டங்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. 98வது அரசியலமைப்பு திருத்தச் சட்டம் (கர்நாடகாவிற்கு சரத்து 371J)\n2. 36வது அரசியலமைப்பு திருத்தச் சட்டம் (சிக்கிமிற்கு சரத்து 371F)\n3. 55வது அரசியலமைப்பு திருத்தச் சட்டம் (அருணாச்சலப் பிரதேசத்திற்கு சரத்து 371H)\n4. 53வது அரசியலமைப்பு திருத்தச் சட்டம் (மிசோரமிற்கு சரத்து 371G)\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("2 - 4 - 3 - 1", "2 - 4 - 3 - 1"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4"),
                ("2 - 3 - 4 - 1", "2 - 3 - 4 - 1"),
                ("4 - 2 - 3 - 1", "4 - 2 - 3 - 1")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is:\n2. 36th Amendment Act (May 1975)\n→ 4. 53rd Amendment Act (August 1986)\n→ 3. 55th Amendment Act (December 1986)\n→ 1. 98th Amendment Act (January 2013 / enacted 2012).\nSequence: 2 → 4 → 3 → 1.",
            "exp_ta": "சரியான காலவரிசை:\n2. 36வது திருத்தச் சட்டம் (மே 1975)\n→ 4. 53வது திருத்தச் சட்டம் (ஆகஸ்ட் 1986)\n→ 3. 55வது திருத்தச் சட்டம் (டிசம்பர் 1986)\n→ 1. 98வது திருத்தச் சட்டம் (2012).\nவரிசை: 2 → 4 → 3 → 1.",
            "why_a_en": "Correctly follows: 1975 -> 1986 (Aug) -> 1986 (Dec) -> 2012.",
            "why_a_ta": "1975 -> 1986 (ஆகஸ்ட்) -> 1986 (டிசம்பர்) -> 2012 என்ற வரிசையைச் சரியாகப் பின்பற்றுகிறது.",
            "why_b_en": "Incorrect presented stem sequence.",
            "why_b_ta": "வினாவில் கொடுக்கப்பட்ட தவறான வரிசை.",
            "why_c_en": "Inverts 53rd and 55th Amendments.",
            "why_c_ta": "53வது மற்றும் 55வது திருத்தங்களை மாற்றுகிறது.",
            "why_d_en": "Places 53rd Amendment before 36th Amendment.",
            "why_d_ta": "36வது திருத்தத்திற்கு முன் 53வது திருத்தத்தை வைக்கிறது.",
            "tip_en": "Order: 36th (1975) -> 53rd (1986) -> 55th (1986) -> 98th (2012).",
            "tip_ta": "வரிசை: 36வது (1975) -> 53வது (1986) -> 55வது (1986) -> 98வது (2012).",
            "fact_en": "98th CAA is the latest amendment in the Article 371 series.",
            "fact_ta": "சரத்து 371 தொடரில் 98வது திருத்தமே மிகச் சமீபத்திய திருத்தமாகும்."
        },
        # 5
        {
            "subtopic": "Andhra Pradesh Regional Milestones",
            "stem_en": "Arrange the following regional and statutory developments concerning Andhra Pradesh in chronological order:\n1. Andhra Pradesh Reorganisation Act (bifurcation into AP and Telangana)\n2. Eight-Point Formula announced by Prime Minister Indira Gandhi\n3. Six-Point Formula and enactment of the 32nd Constitutional Amendment Act\n4. Five-Point Formula announced by Central Government\nSelect the correct answer using the codes given below:",
            "stem_ta": "ஆந்திரப் பிரதேசம் தொடர்பான பின்வரும் பிராந்திய மற்றும் சட்டப்பூர்வ நிகழ்வுகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. ஆந்திரப் பிரதேச மறுசீரமைப்புச் சட்டம் (ஆந்திரா மற்றும் தெலங்கானாவாகப் பிரிப்பு)\n2. பிரதமர் இந்திரா காந்தியால் அறிவிக்கப்பட்ட எட்டு அம்ச சூத்திரம்\n3. ஆறு அம்ச சூத்திரம் மற்றும் 32வது அரசியலமைப்பு திருத்தச் சட்டம் இயற்றப்படுதல்\n4. மத்திய அரசால் அறிவிக்கப்பட்ட ஐந்து அம்ச சூத்திரம்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("2 - 4 - 3 - 1", "2 - 4 - 3 - 1"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4"),
                ("2 - 3 - 4 - 1", "2 - 3 - 4 - 1"),
                ("4 - 2 - 3 - 1", "4 - 2 - 3 - 1")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is:\n2. Eight-Point Formula (April 1969)\n→ 4. Five-Point Formula (November 1971)\n→ 3. Six-Point Formula & 32nd Amendment (September/December 1973)\n→ 1. Andhra Pradesh Reorganisation Act (March/June 2014).\nSequence: 2 → 4 → 3 → 1.",
            "exp_ta": "சரியான காலவரிசை:\n2. எட்டு அம்ச சூத்திரம் (ஏப்ரல் 1969)\n→ 4. ஐந்து அம்ச சூத்திரம் (நவம்பர் 1971)\n→ 3. ஆறு அம்ச சூத்திரம் & 32வது திருத்தம் (1973)\n→ 1. ஆந்திரப் பிரதேச மறுசீரமைப்புச் சட்டம் (2014).\nவரிசை: 2 → 4 → 3 → 1.",
            "why_a_en": "Correct sequence: 1969 -> 1971 -> 1973 -> 2014.",
            "why_a_ta": "சரியான வரிசை: 1969 -> 1971 -> 1973 -> 2014.",
            "why_b_en": "Incorrect presented stem sequence.",
            "why_b_ta": "வினாவில் கொடுக்கப்பட்ட தவறான வரிசை.",
            "why_c_en": "Places Six-Point Formula before Five-Point Formula.",
            "why_c_ta": "ஐந்து அம்ச சூத்திரத்திற்கு முன் ஆறு அம்ச சூத்திரத்தை வைக்கிறது.",
            "why_d_en": "Places Five-Point Formula before Eight-Point Formula.",
            "why_d_ta": "எட்டு அம்ச சூத்திரத்திற்கு முன் ஐந்து அம்ச சூத்திரத்தை வைக்கிறது.",
            "tip_en": "AP formulas progression: 8-point (1969) -> 5-point (1971) -> 6-point (1973).",
            "tip_ta": "ஆந்திர சூத்திரங்களின் வளர்ச்சி: 8 அம்ச (1969) -> 5 அம்ச (1971) -> 6 அம்ச (1973).",
            "fact_en": "The 2014 Act amended Article 371D to preserve local reservations in both new states.",
            "fact_ta": "2014 சட்டம் இரு புதிய மாநிலங்களிலும் உள்ளூர் இடஒதுக்கீட்டைப் பாதுகாக்க சரத்து 371D-ஐ திருத்தியது."
        },
        # 6
        {
            "subtopic": "Sikkim Integration Milestones",
            "stem_en": "Arrange the following historic steps in the integration of Sikkim with India in chronological order:\n1. 36th Constitutional Amendment Act conferring full statehood and Article 371F\n2. Indo-Sikkim Peace Treaty making Sikkim a protectorate\n3. 35th Constitutional Amendment Act introducing 'Associate State' status\n4. Tripartite Agreement between Government of India, Chogyal, and political parties\nSelect the correct answer using the codes given below:",
            "stem_ta": "சிக்கிம் இந்தியாவுடன் ஒருங்கிணைக்கப்பட்ட பின்வரும் வரலாற்றுப் படிகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. முழு மாநில அந்தஸ்து மற்றும் சரத்து 371F-ஐ வழங்கிய 36வது அரசியலமைப்பு திருத்தச் சட்டம்\n2. சிக்கிமை பாதுகாக்கப்பட்ட பகுதியாக மாற்றிய இந்திய-சிக்கிம் அமைதி ஒப்பந்தம்\n3. 'இணைப்பு மாநில' அந்தஸ்தை அறிமுகப்படுத்திய 35வது அரசியலமைப்பு திருத்தச் சட்டம்\n4. இந்திய அரசு, சோக்யால் மற்றும் அரசியல் கட்சிகளுக்கிடையிலான முத்தரப்பு ஒப்பந்தம்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("2 - 4 - 3 - 1", "2 - 4 - 3 - 1"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4"),
                ("2 - 3 - 4 - 1", "2 - 3 - 4 - 1"),
                ("4 - 2 - 3 - 1", "4 - 2 - 3 - 1")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is:\n2. Indo-Sikkim Peace Treaty (5 December 1950)\n→ 4. Tripartite Agreement (8 May 1973)\n→ 3. 35th Amendment Act (September 1974)\n→ 1. 36th Amendment Act (16 May 1975).\nSequence: 2 → 4 → 3 → 1.",
            "exp_ta": "சரியான காலவரிசை:\n2. இந்திய-சிக்கிம் அமைதி ஒப்பந்தம் (5 டிசம்பர் 1950)\n→ 4. முத்தரப்பு ஒப்பந்தம் (8 மே 1973)\n→ 3. 35வது திருத்தச் சட்டம் (செப்டம்பர் 1974)\n→ 1. 36வது திருத்தச் சட்டம் (16 மே 1975).\nவரிசை: 2 → 4 → 3 → 1.",
            "why_a_en": "Correctly traces Sikkim's progression: 1950 -> 1973 -> 1974 -> 1975.",
            "why_a_ta": "சிக்கிமின் வளர்ச்சியைக் காலவரிசைப்படி துல்லியமாகப் பின்பற்றுகிறது: 1950 -> 1973 -> 1974 -> 1975.",
            "why_b_en": "Incorrect presented stem sequence.",
            "why_b_ta": "வினாவில் கொடுக்கப்பட்ட தவறான வரிசை.",
            "why_c_en": "Places 35th Amendment before 1973 Tripartite Agreement.",
            "why_c_ta": "1973 முத்தரப்பு ஒப்பந்தத்திற்கு முன் 35வது திருத்தத்தை வைக்கிறது.",
            "why_d_en": "Places 1973 Tripartite Agreement before 1950 Treaty.",
            "why_d_ta": "1950 ஒப்பந்தத்திற்கு முன் 1973 முத்தரப்பு ஒப்பந்தத்தை வைக்கிறது.",
            "tip_en": "Milestones: Treaty (1950) -> Accord (1973) -> Associate (1974) -> Full State (1975).",
            "tip_ta": "மைல்கற்கள்: ஒப்பந்தம் (1950) -> உடன்படிக்கை (1973) -> இணைப்பு (1974) -> முழு மாநிலம் (1975).",
            "fact_en": "The 35th Amendment inserted Article 2A and the Tenth Schedule, both repealed by the 36th Amendment.",
            "fact_ta": "35வது திருத்தம் சரத்து 2A மற்றும் பத்தாவது அட்டவணையைச் சேர்த்தது; இரண்டும் 36வது திருத்தத்தால் நீக்கப்பட்டன."
        },
        # 7
        {
            "subtopic": "Key Supreme Court Judgments on Special Provisions",
            "stem_en": "Arrange the following landmark Supreme Court judgments in chronological order:\n1. In Re: Article 370 of the Constitution (abrogation upheld)\n2. Shamsher Singh v. State of Punjab (Governor's discretion analyzed)\n3. R.C. Poudyal v. Union of India (Article 371F upheld)\n4. P. Sambamurthy v. State of Andhra Pradesh (Article 371D(5) struck down)\nSelect the correct answer using the codes given below:",
            "stem_ta": "பின்வரும் மைல்கல் உச்ச நீதிமன்றத் தீர்ப்புகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. சரத்து 370 மறுஆய்வு வழக்கு (ரத்து செய்யப்பட்டது உறுதி செய்யப்பட்டது)\n2. ஷம்ஷேர் சிங் எதிர் பஞ்சாப் அரசு (ஆளுநரின் விருப்புரிமை பகுப்பாய்வு)\n3. ஆர்.சி. பௌடியால் எதிர் இந்திய ஒன்றியம் (சரத்து 371F உறுதி செய்யப்பட்டது)\n4. பி. சாம்பமூர்த்தி எதிர் ஆந்திரப் பிரதேச அரசு (சரத்து 371D(5) ரத்து செய்யப்பட்டது)\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("2 - 4 - 3 - 1", "2 - 4 - 3 - 1"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4"),
                ("2 - 3 - 4 - 1", "2 - 3 - 4 - 1"),
                ("4 - 2 - 3 - 1", "4 - 2 - 3 - 1")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is:\n2. Shamsher Singh v. State of Punjab (1974)\n→ 4. P. Sambamurthy v. State of AP (1987)\n→ 3. R.C. Poudyal v. Union of India (1994)\n→ 1. In Re: Article 370 (11 December 2023).\nSequence: 2 → 4 → 3 → 1.",
            "exp_ta": "சரியான காலவரிசை:\n2. ஷம்ஷேர் சிங் எதிர் பஞ்சாப் அரசு (1974)\n→ 4. பி. சாம்பமூர்த்தி எதிர் ஆந்திர அரசு (1987)\n→ 3. ஆர்.சி. பௌடியால் எதிர் இந்திய ஒன்றியம் (1994)\n→ 1. சரத்து 370 மறுஆய்வு வழக்கு (11 டிசம்பர் 2023).\nவரிசை: 2 → 4 → 3 → 1.",
            "why_a_en": "Chronological order: 1974 -> 1987 -> 1994 -> 2023.",
            "why_a_ta": "காலவரிசை: 1974 -> 1987 -> 1994 -> 2023.",
            "why_b_en": "Incorrect presented stem order.",
            "why_b_ta": "வினாவில் கொடுக்கப்பட்ட தவறான வரிசை.",
            "why_c_en": "Places 1994 Poudyal before 1987 Sambamurthy.",
            "why_c_ta": "1987 சாம்பமூர்த்திக்கு முன் 1994 பௌடியாலை வைக்கிறது.",
            "why_d_en": "Places 1987 Sambamurthy before 1974 Shamsher Singh.",
            "why_d_ta": "1974 ஷம்ஷேர் சிங்கிற்கு முன் 1987 சாம்பமூர்த்தியை வைக்கிறது.",
            "tip_en": "Timeline: Shamsher Singh (1974) -> Sambamurthy (1987) -> Poudyal (1994) -> Art 370 Bench (2023).",
            "tip_ta": "காலவரிசை: ஷம்ஷேர் சிங் (1974) -> சாம்பமூர்த்தி (1987) -> பௌடியால் (1994) -> சரத்து 370 அமர்வு (2023).",
            "fact_en": "All four cases are landmark Constitution Bench judgments shaping asymmetric federalism in India.",
            "fact_ta": "இந்த நான்கு வழக்குகளும் இந்தியாவில் சமச்சீரற்ற கூட்டாட்சியை வடிவமைத்த மைல்கல் அரசியலமைப்பு அமர்வுத் தீர்ப்புகளாகும்."
        },
        # 8
        {
            "subtopic": "Jammu and Kashmir Constitutional Milestones",
            "stem_en": "Arrange the following constitutional milestones concerning Jammu and Kashmir in chronological order:\n1. Constitution Order 272 and 273 (Abrogation of Article 370)\n2. Signing of the Instrument of Accession by Maharaja Hari Singh\n3. Constitution Order 48 (Application of Constitution Order)\n4. Commencement of the Indian Constitution with Article 370\nSelect the correct answer using the codes given below:",
            "stem_ta": "ஜம்மு மற்றும் காஷ்மீர் தொடர்பான பின்வரும் அரசியலமைப்பு மைல்கற்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. அரசியலமைப்பு உத்தரவு 272 மற்றும் 273 (சரத்து 370 ரத்து செய்யப்படுதல்)\n2. மகாராஜா ஹரி சிங் இணைப்பு ஆவணத்தில் கையெழுத்திடுதல்\n3. அரசியலமைப்பு உத்தரவு 48 (அரசியலமைப்பு பயன்பாட்டு உத்தரவு)\n4. சரத்து 370 உடன் இந்திய அரசியலமைப்பு நடைமுறைக்கு வருதல்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("2 - 4 - 3 - 1", "2 - 4 - 3 - 1"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4"),
                ("2 - 3 - 4 - 1", "2 - 3 - 4 - 1"),
                ("4 - 2 - 3 - 1", "4 - 2 - 3 - 1")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is:\n2. Instrument of Accession (26 October 1947)\n→ 4. Indian Constitution commences with Art 370 (26 January 1950)\n→ 3. Constitution Order 48 (14 May 1954)\n→ 1. Constitution Orders 272 & 273 (5-6 August 2019).\nSequence: 2 → 4 → 3 → 1.",
            "exp_ta": "சரியான காலவரிசை:\n2. இணைப்பு ஆவணம் (26 அக்டோபர் 1947)\n→ 4. சரத்து 370 உடன் அரசியலமைப்பு தொடக்கம் (26 ஜனவரி 1950)\n→ 3. அரசியலமைப்பு உத்தரவு 48 (14 மே 1954)\n→ 1. அரசியலமைப்பு உத்தரவுகள் 272 & 273 (ஆகஸ்ட் 2019).\nவரிசை: 2 → 4 → 3 → 1.",
            "why_a_en": "Correct progression: 1947 -> 1950 -> 1954 -> 2019.",
            "why_a_ta": "சரியான வளர்ச்சி: 1947 -> 1950 -> 1954 -> 2019.",
            "why_b_en": "Incorrect presented stem sequence.",
            "why_b_ta": "வினாவில் கொடுக்கப்பட்ட தவறான வரிசை.",
            "why_c_en": "Places 1954 C.O. 48 before 1950 Constitution commencement.",
            "why_c_ta": "1950 அரசியலமைப்பு தொடக்கத்திற்கு முன் 1954 C.O. 48-ஐ வைக்கிறது.",
            "why_d_en": "Places 1950 Constitution commencement before 1947 Accession.",
            "why_d_ta": "1947 இணைப்பிற்கு முன் 1950 அரசியலமைப்பு தொடக்கத்தை வைக்கிறது.",
            "tip_en": "Progression: Accession (1947) -> Art 370 (1950) -> C.O. 48 (1954) -> C.O. 272/273 (2019).",
            "tip_ta": "வளர்ச்சி: இணைப்பு (1947) -> சரத்து 370 (1950) -> C.O. 48 (1954) -> C.O. 272/273 (2019).",
            "fact_en": "C.O. 48 formed the bedrock of the Union's relationship with J&K for 65 years until 2019.",
            "fact_ta": "2019 வரை 65 ஆண்டுகளாக ஒன்றியத்திற்கும் ஜம்மு காஷ்மீருக்கும் இடையிலான உறவின் அடித்தளமாக C.O. 48 அமைந்தது."
        },
        # 9
        {
            "subtopic": "Formation of States with Special Provisions",
            "stem_en": "Arrange the following events relating to the formation of States under Part XXI in chronological order:\n1. Formation of Goa as a full State\n2. Bifurcation of Bombay State into Maharashtra and Gujarat\n3. Admission of Sikkim as the 22nd State\n4. Inauguration of the State of Nagaland\nSelect the correct answer using the codes given below:",
            "stem_ta": "பகுதி XXI-ன் கீழ் உள்ள மாநிலங்கள் உருவாக்கப்பட்ட பின்வரும் நிகழ்வுகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. கோவா ஒரு முழு மாநிலமாக உருவாவது\n2. பம்பாய் மாநிலம் மகாராஷ்டிரா மற்றும் குஜராத் என பிரிக்கப்படுவது\n3. சிக்கிம் 22வது மாநிலமாக இணைக்கப்படுவது\n4. நாகாலாந்து மாநிலம் முறைப்படி தொடங்கப்படுவது\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("2 - 4 - 3 - 1", "2 - 4 - 3 - 1"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4"),
                ("2 - 3 - 4 - 1", "2 - 3 - 4 - 1"),
                ("4 - 2 - 3 - 1", "4 - 2 - 3 - 1")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is:\n2. Bifurcation of Bombay (1 May 1960)\n→ 4. Inauguration of Nagaland (1 December 1963)\n→ 3. Admission of Sikkim (16 May 1975)\n→ 1. Formation of Goa (30 May 1987).\nSequence: 2 → 4 → 3 → 1.",
            "exp_ta": "சரியான காலவரிசை:\n2. பம்பாய் பிரிப்பு (1 மே 1960)\n→ 4. நாகாலாந்து தொடக்கம் (1 டிசம்பர் 1963)\n→ 3. சிக்கிம் இணைப்பு (16 மே 1975)\n→ 1. கோவா உருவாக்கம் (30 மே 1987).\nவரிசை: 2 → 4 → 3 → 1.",
            "why_a_en": "Follows exact statehood formation dates: 1960 -> 1963 -> 1975 -> 1987.",
            "why_a_ta": "மாநில உருவாக்கப்பட்ட சரியான தேதிகளைப் பின்பற்றுகிறது: 1960 -> 1963 -> 1975 -> 1987.",
            "why_b_en": "Incorrect presented stem sequence.",
            "why_b_ta": "வினாவில் கொடுக்கப்பட்ட தவறான வரிசை.",
            "why_c_en": "Places Sikkim before Nagaland.",
            "why_c_ta": "நாகாலாந்திற்கு முன் சிக்கிமை வைக்கிறது.",
            "why_d_en": "Places Nagaland before Bombay bifurcation.",
            "why_d_ta": "பம்பாய் பிரிப்பிற்கு முன் நாகாலாந்தை வைக்கிறது.",
            "tip_en": "State formation order: Bombay split (1960) -> Nagaland (1963) -> Sikkim (1975) -> Goa (1987).",
            "tip_ta": "மாநில உருவாக்கம்: பம்பாய் பிரிப்பு (1960) -> நாகாலாந்து (1963) -> சிக்கிம் (1975) -> கோவா (1987).",
            "fact_en": "Goa was liberated from Portuguese rule in 1961 and waited 26 years for statehood in 1987.",
            "fact_ta": "1961-ல் போர்ச்சுகீசிய ஆதிக்கத்திலிருந்து விடுவிக்கப்பட்ட கோவா, 1987-ல் மாநில அந்தஸ்து பெற 26 ஆண்டுகள் காத்திருந்தது."
        },
        # 10
        {
            "subtopic": "Regional Development Boards Evolution",
            "stem_en": "Arrange the following milestones relating to regional development boards and backward region mechanisms in chronological order:\n1. 98th Constitutional Amendment Act inserting Article 371J for Kalyana Karnataka\n2. 7th Constitutional Amendment Act restructuring Article 371\n3. High Power Committee Report on Regional Imbalances (Dr. D.M. Nanjundappa Committee)\n4. Presidential Orders formally setting up Development Boards in Maharashtra\nSelect the correct answer using the codes given below:",
            "stem_ta": "பிராந்திய வளர்ச்சி வாரியங்கள் மற்றும் பின்தங்கிய பகுதி வழிமுறைகள் தொடர்பான பின்வரும் மைல்கற்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. கல்யாண கர்நாடகாவிற்காக சரத்து 371J-ஐ சேர்த்த 98வது அரசியலமைப்பு திருத்தச் சட்டம்\n2. சரத்து 371-ஐ மறுசீரமைத்த 7வது அரசியலமைப்பு திருத்தச் சட்டம்\n3. பிராந்திய ஏற்றத்தாழ்வுகள் குறித்த உயர்மட்டக் குழு அறிக்கை (டாக்டர் டி.எம். நஞ்சுண்டப்பா குழு)\n4. மகாராஷ்டிராவில் வளர்ச்சி வாரியங்களை அமைத்த குடியரசுத் தலைவர் உத்தரவுகள்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("2 - 4 - 3 - 1", "2 - 4 - 3 - 1"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4"),
                ("2 - 3 - 4 - 1", "2 - 3 - 4 - 1"),
                ("4 - 2 - 3 - 1", "4 - 2 - 3 - 1")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is:\n2. 7th Amendment Act (1956)\n→ 4. Presidential Orders creating MH boards (1994)\n→ 3. Nanjundappa Committee Report (2002)\n→ 1. 98th Amendment Act (2012).\nSequence: 2 → 4 → 3 → 1.",
            "exp_ta": "சரியான காலவரிசை:\n2. 7வது திருத்தச் சட்டம் (1956)\n→ 4. மகாராஷ்டிர வாரியங்களை அமைத்த உத்தரவுகள் (1994)\n→ 3. நஞ்சுண்டப்பா கமிட்டி அறிக்கை (2002)\n→ 1. 98வது திருத்தச் சட்டம் (2012).\nவரிசை: 2 → 4 → 3 → 1.",
            "why_a_en": "Accurately follows 1956 -> 1994 -> 2002 -> 2012.",
            "why_a_ta": "1956 -> 1994 -> 2002 -> 2012 என்ற காலவரிசையைத் துல்லியமாகப் பின்பற்றுகிறது.",
            "why_b_en": "Incorrect presented stem sequence.",
            "why_b_ta": "வினாவில் கொடுக்கப்பட்ட தவறான வரிசை.",
            "why_c_en": "Places Nanjundappa Report before 1994 Presidential Orders.",
            "why_c_ta": "1994 குடியரசுத் தலைவர் உத்தரவுகளுக்கு முன் நஞ்சுண்டப்பா அறிக்கையை வைக்கிறது.",
            "why_d_en": "Places 1994 orders before 1956 7th Amendment.",
            "why_d_ta": "1956 7வது திருத்தத்திற்கு முன் 1994 உத்தரவுகளை வைக்கிறது.",
            "tip_en": "7th CAA (1956) -> MH Boards (1994) -> Nanjundappa (2002) -> 98th CAA (2012).",
            "tip_ta": "7வது திருத்தம் (1956) -> மகாராஷ்டிர வாரியங்கள் (1994) -> நஞ்சுண்டப்பா (2002) -> 98வது திருத்தம் (2012).",
            "fact_en": "Vidarbha, Marathwada, and Rest of Maharashtra boards functioned until their terms expired in 2020.",
            "fact_ta": "விதர்பா, மராத்வாடா மற்றும் எஞ்சிய மகாராஷ்டிர வாரியங்கள் அவற்றின் பதவிக்காலம் 2020-ல் முடியும் வரை செயல்பட்டன."
        },
        # 11
        {
            "subtopic": "Nagaland Article 371A Milestones",
            "stem_en": "Arrange the following milestones concerning Nagaland and Article 371A in chronological order:\n1. Formal inauguration of the State of Nagaland by President Dr. S. Radhakrishnan\n2. First Naga People's Convention at Kohima demanding a separate administrative unit\n3. Passing of the 13th Constitutional Amendment Act by Parliament\n4. Signing of the 16-Point Agreement between Prime Minister Nehru and NPC leaders\nSelect the correct answer using the codes given below:",
            "stem_ta": "நாகாலாந்து மற்றும் சரத்து 371A தொடர்பான பின்வரும் மைல்கற்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. குடியரசுத் தலைவர் டாக்டர் எஸ். ராதாகிருஷ்ணனால் நாகாலாந்து மாநிலம் முறைப்படி தொடங்கப்படுதல்\n2. தனி நிர்வாகப் பிரிவு கோரி கோஹிமாவில் நடைபெற்ற முதலாவது நாகா மக்கள் மாநாடு\n3. நாடாளுமன்றத்தால் 13வது அரசியலமைப்பு திருத்தச் சட்டம் நிறைவேற்றப்படுதல்\n4. பிரதமர் நேரு மற்றும் NPC தலைவர்களுக்கிடையே 16 அம்ச ஒப்பந்தம் கையெழுத்தாதல்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("2 - 4 - 3 - 1", "2 - 4 - 3 - 1"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4"),
                ("2 - 3 - 4 - 1", "2 - 3 - 4 - 1"),
                ("4 - 2 - 3 - 1", "4 - 2 - 3 - 1")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is:\n2. First Naga People's Convention (August 1957)\n→ 4. 16-Point Agreement (July 1960)\n→ 3. 13th Amendment Act enacted (December 1962)\n→ 1. Formal inauguration of State (1 December 1963).\nSequence: 2 → 4 → 3 → 1.",
            "exp_ta": "சரியான காலவரிசை:\n2. முதலாவது நாகா மக்கள் மாநாடு (ஆகஸ்ட் 1957)\n→ 4. 16 அம்ச ஒப்பந்தம் (ஜூலை 1960)\n→ 3. 13வது திருத்தச் சட்டம் இயற்றப்படுதல் (டிசம்பர் 1962)\n→ 1. மாநிலம் முறைப்படி தொடங்கப்படுதல் (1 டிசம்பர் 1963).\nவரிசை: 2 → 4 → 3 → 1.",
            "why_a_en": "Chronological order: 1957 -> 1960 -> 1962 -> 1963.",
            "why_a_ta": "காலவரிசை: 1957 -> 1960 -> 1962 -> 1963.",
            "why_b_en": "Incorrect presented stem sequence.",
            "why_b_ta": "வினாவில் கொடுக்கப்பட்ட தவறான வரிசை.",
            "why_c_en": "Inverts 1960 Accord and 1962 Amendment.",
            "why_c_ta": "1960 ஒப்பந்தம் மற்றும் 1962 திருத்தத்தை மாற்றுகிறது.",
            "why_d_en": "Places 16-Point Agreement before NPC Convention.",
            "why_d_ta": "NPC மாநாட்டிற்கு முன் 16 அம்ச ஒப்பந்தத்தை வைக்கிறது.",
            "tip_en": "Convention (1957) -> Agreement (1960) -> 13th CAA (1962) -> Statehood (1963).",
            "tip_ta": "மாநாடு (1957) -> ஒப்பந்தம் (1960) -> 13வது திருத்தம் (1962) -> மாநில அந்தஸ்து (1963).",
            "fact_en": "Shilu Ao was the first Chief Executive Councillor and later Chief Minister of Nagaland.",
            "fact_ta": "ஷிலு ஆவோ நாகாலாந்தின் முதல் தலைமை நிர்வாக கவுன்சிலராகவும் பின்னர் முதல்வராகவும் இருந்தார்."
        },
        # 12
        {
            "subtopic": "Mizoram Statehood Evolution",
            "stem_en": "Arrange the following stages in the political and constitutional evolution of Mizoram in chronological order:\n1. Attainment of Statehood under the 53rd Constitutional Amendment Act\n2. Establishment of the Lushai Hills Autonomous District Council under Sixth Schedule\n3. Signing of the historic Mizo Peace Accord\n4. Reorganisation as a Union Territory under North-Eastern Areas Reorganisation Act\nSelect the correct answer using the codes given below:",
            "stem_ta": "மிசோரமின் அரசியல் மற்றும் அரசியலமைப்பு வளர்ச்சியின் பின்வரும் நிலைகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. 53வது அரசியலமைப்பு திருத்தச் சட்டம் மூலம் மாநில அந்தஸ்து பெறுதல்\n2. ஆறாவது அட்டவணையின் கீழ் லுஷாய் மலை தன்னாட்சி மாவட்டக் குழு நிறுவப்படுதல்\n3. வரலாற்றுச் சிறப்புமிக்க மிசோ அமைதி ஒப்பந்தம் கையெழுத்தாதல்\n4. வடகிழக்குப் பகுதிகள் மறுசீரமைப்புச் சட்டத்தின் கீழ் யூனியன் பிரதேசமாக மறுசீரமைக்கப்படுதல்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("2 - 4 - 3 - 1", "2 - 4 - 3 - 1"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4"),
                ("2 - 3 - 4 - 1", "2 - 3 - 4 - 1"),
                ("4 - 2 - 3 - 1", "4 - 2 - 3 - 1")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is:\n2. Lushai Hills District Council (1952)\n→ 4. Union Territory status (21 January 1972)\n→ 3. Mizo Peace Accord (30 June 1986)\n→ 1. Full Statehood via 53rd CAA (20 February 1987).\nSequence: 2 → 4 → 3 → 1.",
            "exp_ta": "சரியான காலவரிசை:\n2. லுஷாய் மலை மாவட்டக் குழு (1952)\n→ 4. யூனியன் பிரதேச அந்தஸ்து (21 ஜனவரி 1972)\n→ 3. மிசோ அமைதி ஒப்பந்தம் (30 ஜூன் 1986)\n→ 1. 53வது திருத்தம் மூலம் முழு மாநில அந்தஸ்து (20 பிப்ரவரி 1987).\nவரிசை: 2 → 4 → 3 → 1.",
            "why_a_en": "Accurately follows 1952 -> 1972 -> 1986 -> 1987.",
            "why_a_ta": "1952 -> 1972 -> 1986 -> 1987 என்ற காலவரிசையைத் துல்லியமாகப் பின்பற்றுகிறது.",
            "why_b_en": "Incorrect presented stem sequence.",
            "why_b_ta": "வினாவில் கொடுக்கப்பட்ட தவறான வரிசை.",
            "why_c_en": "Places Peace Accord before UT status.",
            "why_c_ta": "யூனியன் பிரதேச அந்தஸ்திற்கு முன் அமைதி ஒப்பந்தத்தை வைக்கிறது.",
            "why_d_en": "Places UT status before District Council.",
            "why_d_ta": "மாவட்டக் குழுவிற்கு முன் யூனியன் பிரதேச அந்தஸ்தை வைக்கிறது.",
            "tip_en": "Lushai Hills (1952) -> UT Mizoram (1972) -> Accord (1986) -> State (1987).",
            "tip_ta": "லுஷாய் மலை (1952) -> யூனியன் பிரதேசம் (1972) -> ஒப்பந்தம் (1986) -> மாநிலம் (1987).",
            "fact_en": "Lushai Hills was renamed Mizo Hills District in 1954.",
            "fact_ta": "லுஷாய் மலை மாவட்டம் 1954-ல் மிசோ மலை மாவட்டம் எனப் பெயர் மாற்றப்பட்டது."
        },
        # 13
        {
            "subtopic": "Andhra Pradesh Article 371D Preceding Agitations",
            "stem_en": "Arrange the following political and legal events leading to Article 371D in chronological order:\n1. Passing of the 32nd Constitutional Amendment Act inserting Article 371D\n2. Gentlemen's Agreement of Andhra Pradesh assuring Telangana safeguards\n3. Jai Andhra agitation demanding bifurcation of Andhra Pradesh\n4. Telangana agitation over Mulki rules violation\nSelect the correct answer using the codes given below:",
            "stem_ta": "சரத்து 371D-க்கு வழிவகுத்த பின்வரும் அரசியல் மற்றும் சட்ட நிகழ்வுகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. சரத்து 371D-ஐ சேர்த்த 32வது அரசியலமைப்பு திருத்தச் சட்டம் நிறைவேற்றப்படுதல்\n2. தெலங்கானா பாதுகாப்புகளை உறுதி செய்த ஆந்திரப் பிரதேச பெரிய மனிதர்கள் ஒப்பந்தம்\n3. ஆந்திரப் பிரதேசத்தைப் பிரிக்கக் கோரிய ஜெய் ஆந்திரா போராட்டம்\n4. முல்கி விதிகள் மீறல் தொடர்பான தெலங்கானா போராட்டம்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("2 - 4 - 3 - 1", "2 - 4 - 3 - 1"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4"),
                ("2 - 3 - 4 - 1", "2 - 3 - 4 - 1"),
                ("4 - 2 - 3 - 1", "4 - 2 - 3 - 1")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is:\n2. Gentlemen's Agreement (February 1956)\n→ 4. Telangana agitation (1969)\n→ 3. Jai Andhra agitation (1972)\n→ 1. 32nd Amendment Act (December 1973).\nSequence: 2 → 4 → 3 → 1.",
            "exp_ta": "சரியான காலவரிசை:\n2. பெரிய மனிதர்கள் ஒப்பந்தம் (பிப்ரவரி 1956)\n→ 4. தெலங்கானா போராட்டம் (1969)\n→ 3. ஜெய் ஆந்திரா போராட்டம் (1972)\n→ 1. 32வது திருத்தச் சட்டம் (டிசம்பர் 1973).\nவரிசை: 2 → 4 → 3 → 1.",
            "why_a_en": "Accurately follows: 1956 -> 1969 -> 1972 -> 1973.",
            "why_a_ta": "1956 -> 1969 -> 1972 -> 1973 என்ற காலவரிசையைச் சரியாகப் பின்பற்றுகிறது.",
            "why_b_en": "Incorrect presented stem sequence.",
            "why_b_ta": "வினாவில் கொடுக்கப்பட்ட தவறான வரிசை.",
            "why_c_en": "Places Jai Andhra before 1969 Telangana movement.",
            "why_c_ta": "1969 தெலங்கானா போராட்டத்திற்கு முன் ஜெய் ஆந்திரா போராட்டத்தை வைக்கிறது.",
            "why_d_en": "Places Telangana agitation before 1956 Gentlemen's Agreement.",
            "why_d_ta": "1956 ஒப்பந்தத்திற்கு முன் தெலங்கானா போராட்டத்தை வைக்கிறது.",
            "tip_en": "Gentlemen's Accord (1956) -> Telangana riot (1969) -> Jai Andhra (1972) -> 32nd CAA (1973).",
            "tip_ta": "ஒப்பந்தம் (1956) -> தெலங்கானா போராட்டம் (1969) -> ஜெய் ஆந்திரா (1972) -> 32வது திருத்தம் (1973).",
            "fact_en": "Bifurcation was averted in 1973 by enacting Article 371D.",
            "fact_ta": "சரத்து 371D-ஐ இயற்றியதன் மூலம் 1973-ல் மாநிலப் பிரிப்பு தவிர்க்கப்பட்டது."
        },
        # 14
        {
            "subtopic": "North-East Territorial Evolution",
            "stem_en": "Arrange the following territorial reorganisation events of North-East India in chronological order:\n1. Full statehood granted to Arunachal Pradesh\n2. Nagaland inaugurated as the 16th State\n3. North-Eastern Areas Reorganisation Act enacted\n4. Sub-state of Meghalaya created within Assam by 22nd Amendment Act\nSelect the correct answer using the codes given below:",
            "stem_ta": "வடகிழக்கு இந்தியாவின் பின்வரும் பிராந்திய மறுசீரமைப்பு நிகழ்வுகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. அருணாச்சலப் பிரதேசத்திற்கு முழு மாநில அந்தஸ்து வழங்கப்படுதல்\n2. நாகாலாந்து 16வது மாநிலமாகத் தொடங்கப்படுதல்\n3. வடகிழக்குப் பகுதிகள் மறுசீரமைப்புச் சட்டம் இயற்றப்படுதல்\n4. 22வது திருத்தச் சட்டம் மூலம் அசாமிற்குள் மேகாலயா துணை மாநிலம் உருவாக்கப்படுதல்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("2 - 4 - 3 - 1", "2 - 4 - 3 - 1"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4"),
                ("2 - 3 - 4 - 1", "2 - 3 - 4 - 1"),
                ("4 - 2 - 3 - 1", "4 - 2 - 3 - 1")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is:\n2. Nagaland statehood (1 December 1963)\n→ 4. Meghalaya autonomous sub-state (1969)\n→ 3. North-Eastern Areas Reorganisation Act (1971)\n→ 1. Arunachal Pradesh statehood (20 February 1987).\nSequence: 2 → 4 → 3 → 1.",
            "exp_ta": "சரியான காலவரிசை:\n2. நாகாலாந்து மாநில அந்தஸ்து (1 டிசம்பர் 1963)\n→ 4. மேகாலயா தன்னாட்சி துணை மாநிலம் (1969)\n→ 3. வடகிழக்குப் பகுதிகள் மறுசீரமைப்புச் சட்டம் (1971)\n→ 1. அருணாச்சலப் பிரதேச மாநில அந்தஸ்து (20 பிப்ரவரி 1987).\nவரிசை: 2 → 4 → 3 → 1.",
            "why_a_en": "Accurately follows: 1963 -> 1969 -> 1971 -> 1987.",
            "why_a_ta": "1963 -> 1969 -> 1971 -> 1987 என்ற காலவரிசையைத் துல்லியமாகப் பின்பற்றுகிறது.",
            "why_b_en": "Incorrect presented stem order.",
            "why_b_ta": "வினாவில் கொடுக்கப்பட்ட தவறான வரிசை.",
            "why_c_en": "Places 1971 Act before 1969 sub-state creation.",
            "why_c_ta": "1969 துணை மாநில உருவாக்கத்திற்கு முன் 1971 சட்டத்தை வைக்கிறது.",
            "why_d_en": "Places 1969 sub-state before 1963 Nagaland.",
            "why_d_ta": "1963 நாகாலாந்திற்கு முன் 1969 துணை மாநிலத்தை வைக்கிறது.",
            "tip_en": "Nagaland (1963) -> Meghalaya sub-state (1969) -> NE Reorg (1971) -> Arunachal (1987).",
            "tip_ta": "நாகாலாந்து (1963) -> மேகாலயா துணை மாநிலம் (1969) -> வடகிழக்கு மறுசீரமைப்பு (1971) -> அருணாச்சல் (1987).",
            "fact_en": "Arunachal Pradesh became the 24th state of India on 20 February 1987.",
            "fact_ta": "அருணாச்சலப் பிரதேசம் 1987 பிப்ரவரி 20 அன்று இந்தியாவின் 24வது மாநிலமாக உருவானது."
        },
        # 15
        {
            "subtopic": "August 2019 Article 370 Sequence",
            "stem_en": "Arrange the following sequential steps of August 2019 regarding Jammu and Kashmir in chronological order:\n1. Jammu and Kashmir Reorganisation Act comes into force\n2. Constitution Order 272 issued amending Article 367\n3. Constitution Order 273 issued declaring Article 370 inoperative\n4. Parliament passes Statutory Resolution recommending declaration under Article 370(3)\nSelect the correct answer using the codes given below:",
            "stem_ta": "ஜம்மு காஷ்மீர் தொடர்பான ஆகஸ்ட் 2019-ன் பின்வரும் தொடர் படிநிலைகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. ஜம்மு காஷ்மீர் மறுசீரமைப்புச் சட்டம் நடைமுறைக்கு வருதல்\n2. சரத்து 367-ஐ திருத்தி அரசியலமைப்பு உத்தரவு 272 பிறப்பிக்கப்படுதல்\n3. சரத்து 370 செயலிழந்துவிட்டதாக அறிவித்து அரசியலமைப்பு உத்தரவு 273 பிறப்பிக்கப்படுதல்\n4. சரத்து 370(3)-ன் கீழ் பிரகடனம் செய்யப் பரிந்துரைக்கும் சட்டப்பூர்வ தீர்மானத்தை நாடாளுமன்றம் நிறைவேற்றுதல்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("2 - 4 - 3 - 1", "2 - 4 - 3 - 1"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4"),
                ("2 - 3 - 4 - 1", "2 - 3 - 4 - 1"),
                ("4 - 2 - 3 - 1", "4 - 2 - 3 - 1")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is:\n2. C.O. 272 issued (5 August 2019 morning)\n→ 4. Statutory Resolution passed by Parliament (5-6 August 2019)\n→ 3. C.O. 273 issued (6 August 2019)\n→ 1. J&K Reorganisation Act takes effect (31 October 2019).\nSequence: 2 → 4 → 3 → 1.",
            "exp_ta": "சரியான காலவரிசை:\n2. C.O. 272 பிறப்பிக்கப்படுதல் (5 ஆகஸ்ட் 2019 காலை)\n→ 4. நாடாளுமன்றத்தில் சட்டப்பூர்வ தீர்மானம் நிறைவேற்றப்படுதல் (5-6 ஆகஸ்ட் 2019)\n→ 3. C.O. 273 பிறப்பிக்கப்படுதல் (6 ஆகஸ்ட் 2019)\n→ 1. ஜம்மு காஷ்மீர் மறுசீரமைப்புச் சட்டம் நடைமுறைக்கு வருதல் (31 அக்டோபர் 2019).\nவரிசை: 2 → 4 → 3 → 1.",
            "why_a_en": "Matches the exact day-by-day legislative and presidential sequence of August-October 2019.",
            "why_a_ta": "ஆகஸ்ட்-அக்டோபர் 2019-ன் நாடாளுமன்ற மற்றும் குடியரசுத் தலைவர் படிநிலைகளைத் துல்லியமாகப் பொருத்துகிறது.",
            "why_b_en": "Incorrect presented stem sequence.",
            "why_b_ta": "வினாவில் கொடுக்கப்பட்ட தவறான வரிசை.",
            "why_c_en": "Places C.O. 273 before Parliamentary resolution.",
            "why_c_ta": "நாடாளுமன்றத் தீர்மானத்திற்கு முன் C.O. 273-ஐ வைக்கிறது.",
            "why_d_en": "Places Parliamentary resolution before C.O. 272.",
            "why_d_ta": "C.O. 272-க்கு முன் நாடாளுமன்றத் தீர்மானத்தை வைக்கிறது.",
            "tip_en": "August 2019 timeline: C.O. 272 (Aug 5) -> Resolution (Aug 5-6) -> C.O. 273 (Aug 6) -> Reorg (Oct 31).",
            "tip_ta": "ஆகஸ்ட் 2019 காலவரிசை: C.O. 272 (ஆக 5) -> தீர்மானம் (ஆக 5-6) -> C.O. 273 (ஆக 6) -> மறுசீரமைப்பு (அக் 31).",
            "fact_en": "31 October is National Unity Day (Sardar Vallabhbhai Patel's birth anniversary).",
            "fact_ta": "அக்டோபர் 31 தேசிய ஒற்றுமை தினமாகும் (சர்தார் வல்லபாய் படேலின் பிறந்த நாள்)."
        },
        # 16
        {
            "subtopic": "Special Provisions Amendments Later Sequence",
            "stem_en": "Arrange the following statutory and constitutional enactments in chronological order:\n1. Andhra Pradesh Reorganisation Act (amending Article 371D)\n2. 53rd Constitutional Amendment Act (Article 371G for Mizoram)\n3. 98th Constitutional Amendment Act (Article 371J for Karnataka)\n4. 56th Constitutional Amendment Act (Article 371I for Goa)\nSelect the correct answer using the codes given below:",
            "stem_ta": "பின்வரும் சட்டப்பூர்வ மற்றும் அரசியலமைப்புச் சட்டங்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. ஆந்திரப் பிரதேச மறுசீரமைப்புச் சட்டம் (சரத்து 371D-ஐ திருத்துதல்)\n2. 53வது அரசியலமைப்பு திருத்தச் சட்டம் (மிசோரமிற்கு சரத்து 371G)\n3. 98வது அரசியலமைப்பு திருத்தச் சட்டம் (கர்நாடகாவிற்கு சரத்து 371J)\n4. 56வது அரசியலமைப்பு திருத்தச் சட்டம் (கோவாவிற்கு சரத்து 371I)\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("2 - 4 - 3 - 1", "2 - 4 - 3 - 1"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4"),
                ("2 - 3 - 4 - 1", "2 - 3 - 4 - 1"),
                ("4 - 2 - 3 - 1", "4 - 2 - 3 - 1")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is:\n2. 53rd Amendment Act (August 1986)\n→ 4. 56th Amendment Act (May 1987)\n→ 3. 98th Amendment Act (December 2012 / Jan 2013)\n→ 1. Andhra Pradesh Reorganisation Act (March 2014).\nSequence: 2 → 4 → 3 → 1.",
            "exp_ta": "சரியான காலவரிசை:\n2. 53வது திருத்தச் சட்டம் (1986)\n→ 4. 56வது திருத்தச் சட்டம் (1987)\n→ 3. 98வது திருத்தச் சட்டம் (2012)\n→ 1. ஆந்திரப் பிரதேச மறுசீரமைப்புச் சட்டம் (2014).\nவரிசை: 2 → 4 → 3 → 1.",
            "why_a_en": "Accurately traces: 1986 -> 1987 -> 2012 -> 2014.",
            "why_a_ta": "1986 -> 1987 -> 2012 -> 2014 என்ற காலவரிசையைத் துல்லியமாகப் பின்பற்றுகிறது.",
            "why_b_en": "Incorrect presented stem sequence.",
            "why_b_ta": "வினாவில் கொடுக்கப்பட்ட தவறான வரிசை.",
            "why_c_en": "Places 98th Amendment before 56th Amendment.",
            "why_c_ta": "56வது திருத்தத்திற்கு முன் 98வது திருத்தத்தை வைக்கிறது.",
            "why_d_en": "Places 56th Amendment before 53rd Amendment.",
            "why_d_ta": "53வது திருத்தத்திற்கு முன் 56வது திருத்தத்தை வைக்கிறது.",
            "tip_en": "Order: 53rd (1986) -> 56th (1987) -> 98th (2012) -> AP Reorg (2014).",
            "tip_ta": "வரிசை: 53வது (1986) -> 56வது (1987) -> 98வது (2012) -> ஆந்திர மறுசீரமைப்பு (2014).",
            "fact_en": "The 2014 Act bifurcated Andhra Pradesh to create Telangana as the 29th State.",
            "fact_ta": "2014 சட்டம் ஆந்திரப் பிரதேசத்தைப் பிரித்து தெலங்கானாவை 29வது மாநிலமாக உருவாக்கியது."
        },
        # 17
        {
            "subtopic": "Assam Reorganisation Milestones",
            "stem_en": "Arrange the following developments regarding Assam's tribal governance in chronological order:\n1. Creation of Bodoland Territorial Council (BTC)\n2. Inauguration of Sixth Schedule District Councils in Assam\n3. North-Eastern Areas Reorganisation Act carving out territories from Assam\n4. 22nd Constitutional Amendment Act inserting Article 371B and Article 244A\nSelect the correct answer using the codes given below:",
            "stem_ta": "அசாமின் பழங்குடியினர் நிர்வாகம் தொடர்பான பின்வரும் நிகழ்வுகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. போடோலாந்து பிராந்தியக் குழு (BTC) உருவாக்கப்படுதல்\n2. அசாமில் ஆறாவது அட்டவணை மாவட்டக் குழுக்கள் தொடங்கப்படுதல்\n3. அசாமிலிருந்து பகுதிகளைப் பிரித்த வடகிழக்குப் பகுதிகள் மறுசீரமைப்புச் சட்டம்\n4. சரத்து 371B மற்றும் சரத்து 244A-ஐ சேர்த்த 22வது அரசியலமைப்பு திருத்தச் சட்டம்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("2 - 4 - 3 - 1", "2 - 4 - 3 - 1"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4"),
                ("2 - 3 - 4 - 1", "2 - 3 - 4 - 1"),
                ("4 - 2 - 3 - 1", "4 - 2 - 3 - 1")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is:\n2. Sixth Schedule District Councils established (1952)\n→ 4. 22nd Amendment Act inserting Art 371B (September 1969)\n→ 3. North-Eastern Areas Reorganisation Act (December 1971)\n→ 1. Bodoland Territorial Council created (February 2003).\nSequence: 2 → 4 → 3 → 1.",
            "exp_ta": "சரியான காலவரிசை:\n2. ஆறாவது அட்டவணை மாவட்டக் குழுக்கள் நிறுவுதல் (1952)\n→ 4. சரத்து 371B-ஐ சேர்த்த 22வது திருத்தம் (1969)\n→ 3. வடகிழக்குப் பகுதிகள் மறுசீரமைப்புச் சட்டம் (1971)\n→ 1. போடோலாந்து பிராந்தியக் குழு உருவாக்கப்படுதல் (2003).\nவரிசை: 2 → 4 → 3 → 1.",
            "why_a_en": "Accurately traces: 1952 -> 1969 -> 1971 -> 2003.",
            "why_a_ta": "1952 -> 1969 -> 1971 -> 2003 என்ற காலவரிசையைத் துல்லியமாகப் பின்பற்றுகிறது.",
            "why_b_en": "Incorrect presented stem sequence.",
            "why_b_ta": "வினாவில் கொடுக்கப்பட்ட தவறான வரிசை.",
            "why_c_en": "Places 1971 Act before 1969 Amendment.",
            "why_c_ta": "1969 திருத்தத்திற்கு முன் 1971 சட்டத்தை வைக்கிறது.",
            "why_d_en": "Places 1969 Amendment before 1952 Sixth Schedule councils.",
            "why_d_ta": "1952 ஆறாவது அட்டவணை குழுக்களுக்கு முன் 1969 திருத்தத்தை வைக்கிறது.",
            "tip_en": "Sixth Schedule (1952) -> 22nd CAA (1969) -> Reorg (1971) -> BTC (2003).",
            "tip_ta": "ஆறாவது அட்டவணை (1952) -> 22வது திருத்தம் (1969) -> மறுசீரமைப்பு (1971) -> BTC (2003).",
            "fact_en": "BTC was established under the Sixth Schedule following the Bodo Accord of 2003.",
            "fact_ta": "2003 போடோ அமைதி ஒப்பந்தத்தைத் தொடர்ந்து ஆறாவது அட்டவணையின் கீழ் BTC நிறுவப்பட்டது."
        },
        # 18
        {
            "subtopic": "Manipur Integration Milestones",
            "stem_en": "Arrange the following historical milestones concerning Manipur in chronological order:\n1. Manipur attains full Statehood\n2. Signing of Merger Agreement by Maharaja Bodhchandra\n3. 27th Constitutional Amendment Act inserting Article 371C\n4. Manipur categorized as a Union Territory under States Reorganisation Act\nSelect the correct answer using the codes given below:",
            "stem_ta": "மணிப்பூர் தொடர்பான பின்வரும் வரலாற்று மைல்கற்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. மணிப்பூர் முழு மாநில அந்தஸ்து பெறுதல்\n2. மகாராஜா போத்சந்திரா இணைப்பு ஒப்பந்தத்தில் கையெழுத்திடுதல்\n3. சரத்து 371C-ஐ சேர்த்த 27வது அரசியலமைப்பு திருத்தச் சட்டம்\n4. மாநிலங்கள் மறுசீரமைப்புச் சட்டத்தின் கீழ் மணிப்பூர் யூனியன் பிரதேசமாக வகைப்படுத்தப்படுதல்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("2 - 4 - 3 - 1", "2 - 4 - 3 - 1"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4"),
                ("2 - 3 - 4 - 1", "2 - 3 - 4 - 1"),
                ("4 - 2 - 3 - 1", "4 - 2 - 3 - 1")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is:\n2. Merger Agreement (21 September 1949)\n→ 4. Manipur becomes a Union Territory (1 November 1956)\n→ 3. 27th Amendment Act inserting Art 371C (30 December 1971)\n→ 1. Full Statehood inaugurated (21 January 1972).\nSequence: 2 → 4 → 3 → 1.",
            "exp_ta": "சரியான காலவரிசை:\n2. இணைப்பு ஒப்பந்தம் (செப்டம்பர் 1949)\n→ 4. மணிப்பூர் யூனியன் பிரதேசம் ஆகுதல் (நவம்பர் 1956)\n→ 3. சரத்து 371C-ஐ சேர்த்த 27வது திருத்தம் (டிசம்பர் 1971)\n→ 1. முழு மாநில அந்தஸ்து பெறுதல் (21 ஜனவரி 1972).\nவரிசை: 2 → 4 → 3 → 1.",
            "why_a_en": "Accurately follows: 1949 -> 1956 -> 1971 -> 1972.",
            "why_a_ta": "1949 -> 1956 -> 1971 -> 1972 என்ற காலவரிசையைத் துல்லியமாகப் பின்பற்றுகிறது.",
            "why_b_en": "Incorrect presented stem sequence.",
            "why_b_ta": "வினாவில் கொடுக்கப்பட்ட தவறான வரிசை.",
            "why_c_en": "Places 1971 Amendment before 1956 UT reorganization.",
            "why_c_ta": "1956 மறுசீரமைப்புக்கு முன் 1971 திருத்தத்தை வைக்கிறது.",
            "why_d_en": "Places 1956 UT status before 1949 Merger.",
            "why_d_ta": "1949 இணைப்பிற்கு முன் 1956 யூனியன் பிரதேச அந்தஸ்தை வைக்கிறது.",
            "tip_en": "Merger (1949) -> UT (1956) -> 27th CAA (1971) -> State (1972).",
            "tip_ta": "இணைப்பு (1949) -> யூனியன் பிரதேசம் (1956) -> 27வது திருத்தம் (1971) -> மாநிலம் (1972).",
            "fact_en": "Maharaja Bodhchandra Singh was the ruler who signed the merger agreement with India.",
            "fact_ta": "மகாராஜா போத்சந்திர சிங் இந்தியாவுடன் இணைப்பு ஒப்பந்தத்தில் கையெழுத்திட்ட ஆட்சியாளர் ஆவார்."
        },
        # 19
        {
            "subtopic": "Kalyana Karnataka Historic Milestones",
            "stem_en": "Arrange the following historic milestones concerning the Hyderabad-Karnataka region in chronological order:\n1. 98th Constitutional Amendment Act enters into force\n2. Operation Polo and accession of Hyderabad State\n3. Submission of the Dr. D.M. Nanjundappa Committee Report\n4. Transfer of Kannada-speaking districts of Hyderabad to Mysore State\nSelect the correct answer using the codes given below:",
            "stem_ta": "ஹைதராபாத்-கர்நாடகா பகுதி தொடர்பான பின்வரும் வரலாற்று மைல்கற்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. 98வது அரசியலமைப்பு திருத்தச் சட்டம் நடைமுறைக்கு வருதல்\n2. ஆபரேஷன் போலோ மற்றும் ஹைதராபாத் சமஸ்தானத்தின் இணைப்பு\n3. டாக்டர் டி.எம். நஞ்சுண்டப்பா கமிட்டி அறிக்கை சமர்ப்பிக்கப்படுதல்\n4. ஹைதராபாத்தின் கன்னடம் பேசும் மாவட்டங்கள் மைசூர் மாநிலத்திற்கு மாற்றப்படுதல்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("2 - 4 - 3 - 1", "2 - 4 - 3 - 1"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4"),
                ("2 - 3 - 4 - 1", "2 - 3 - 4 - 1"),
                ("4 - 2 - 3 - 1", "4 - 2 - 3 - 1")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is:\n2. Operation Polo (September 1948)\n→ 4. Transfer of Kannada districts to Mysore State (1 November 1956)\n→ 3. Nanjundappa Committee Report submitted (2002)\n→ 1. 98th Amendment Act in force (1 January 2013).\nSequence: 2 → 4 → 3 → 1.",
            "exp_ta": "சரியான காலவரிசை:\n2. ஆபரேஷன் போலோ (செப்டம்பர் 1948)\n→ 4. கன்னட மாவட்டங்கள் மைசூருடன் இணைக்கப்படுதல் (1 நவம்பர் 1956)\n→ 3. நஞ்சுண்டப்பா கமிட்டி அறிக்கை சமர்ப்பிக்கப்படுதல் (2002)\n→ 1. 98வது திருத்தச் சட்டம் நடைமுறைக்கு வருதல் (1 ஜனவரி 2013).\nவரிசை: 2 → 4 → 3 → 1.",
            "why_a_en": "Accurately follows: 1948 -> 1956 -> 2002 -> 2013.",
            "why_a_ta": "1948 -> 1956 -> 2002 -> 2013 என்ற காலவரிசையைத் துல்லியமாகப் பின்பற்றுகிறது.",
            "why_b_en": "Incorrect presented stem sequence.",
            "why_b_ta": "வினாவில் கொடுக்கப்பட்ட தவறான வரிசை.",
            "why_c_en": "Places Nanjundappa Report before 1956 reorganisation.",
            "why_c_ta": "1956 மறுசீரமைப்புக்கு முன் நஞ்சுண்டப்பா அறிக்கையை வைக்கிறது.",
            "why_d_en": "Places 1956 transfer before 1948 Operation Polo.",
            "why_d_ta": "1948 ஆபரேஷன் போலோவிற்கு முன் 1956 இணைப்பை வைக்கிறது.",
            "tip_en": "Operation Polo (1948) -> Mysore Reorg (1956) -> Nanjundappa (2002) -> 98th CAA (2013).",
            "tip_ta": "ஆபரேஷன் போலோ (1948) -> மைசூர் மறுசீரமைப்பு (1956) -> நஞ்சுண்டப்பா (2002) -> 98வது திருத்தம் (2013).",
            "fact_en": "Mysore State was formally renamed Karnataka in 1973.",
            "fact_ta": "மைசூர் மாநிலம் 1973-ல் கர்நாடகா என அதிகாரப்பூர்வமாகப் பெயர் மாற்றப்பட்டது."
        },
        # 20
        {
            "subtopic": "Affirmative Action Constitutional Milestones",
            "stem_en": "Arrange the following affirmative action and special reservation amendments in chronological order:\n1. 103rd Constitutional Amendment Act (10% EWS reservation)\n2. 1st Constitutional Amendment Act (Article 15(4) inserted)\n3. 98th Constitutional Amendment Act (Article 371J regional reservation)\n4. 32nd Constitutional Amendment Act (Article 371D local reservation)\nSelect the correct answer using the codes given below:",
            "stem_ta": "பின்வரும் சாதகமான நடவடிக்கை மற்றும் சிறப்பு இடஒதுக்கீட்டு திருத்தங்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. 103வது அரசியலமைப்பு திருத்தச் சட்டம் (10% EWS இடஒதுக்கீடு)\n2. 1வது அரசியலமைப்பு திருத்தச் சட்டம் (சரத்து 15(4) சேர்க்கப்பட்டது)\n3. 98வது அரசியலமைப்பு திருத்தச் சட்டம் (சரத்து 371J பிராந்திய இடஒதுக்கீடு)\n4. 32வது அரசியலமைப்பு திருத்தச் சட்டம் (சரத்து 371D உள்ளூர் இடஒதுக்கீடு)\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("2 - 4 - 3 - 1", "2 - 4 - 3 - 1"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4"),
                ("2 - 3 - 4 - 1", "2 - 3 - 4 - 1"),
                ("4 - 2 - 3 - 1", "4 - 2 - 3 - 1")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is:\n2. 1st Amendment Act (June 1951)\n→ 4. 32nd Amendment Act (December 1973)\n→ 3. 98th Amendment Act (December 2012)\n→ 1. 103rd Amendment Act (January 2019).\nSequence: 2 → 4 → 3 → 1.",
            "exp_ta": "சரியான காலவரிசை:\n2. 1வது திருத்தச் சட்டம் (ஜூன் 1951)\n→ 4. 32வது திருத்தச் சட்டம் (டிசம்பர் 1973)\n→ 3. 98வது திருத்தச் சட்டம் (டிசம்பர் 2012)\n→ 1. 103வது திருத்தச் சட்டம் (ஜனவரி 2019).\nவரிசை: 2 → 4 → 3 → 1.",
            "why_a_en": "Accurately follows: 1951 -> 1973 -> 2012 -> 2019.",
            "why_a_ta": "1951 -> 1973 -> 2012 -> 2019 என்ற காலவரிசையைத் துல்லியமாகப் பின்பற்றுகிறது.",
            "why_b_en": "Incorrect presented stem sequence.",
            "why_b_ta": "வினாவில் கொடுக்கப்பட்ட தவறான வரிசை.",
            "why_c_en": "Places 98th Amendment before 32nd Amendment.",
            "why_c_ta": "32வது திருத்தத்திற்கு முன் 98வது திருத்தத்தை வைக்கிறது.",
            "why_d_en": "Places 32nd Amendment before 1st Amendment.",
            "why_d_ta": "1வது திருத்தத்திற்கு முன் 32வது திருத்தத்தை வைக்கிறது.",
            "tip_en": "Reservation amendments: 1st (1951) -> 32nd (1973) -> 98th (2012) -> 103rd (2019).",
            "tip_ta": "இடஒதுக்கீட்டு திருத்தங்கள்: 1வது (1951) -> 32வது (1973) -> 98வது (2012) -> 103வது (2019).",
            "fact_en": "The 1st Amendment was passed by the provisional Parliament following Champakam Dorairajan case.",
            "fact_ta": "செண்பகம் துரைராஜன் வழக்கைத் தொடர்ந்து இடைக்கால நாடாளுமன்றத்தால் 1வது திருத்தம் நிறைவேற்றப்பட்டது."
        },
        # 21
        {
            "subtopic": "Constitutional Jurisprudence Timeline",
            "stem_en": "Arrange the following landmark Supreme Court judgments touching upon Part XXI and federalism in chronological order:\n1. Supreme Court Constitution Bench verdict upholding abrogation of Article 370\n2. Kesavananda Bharati v. State of Kerala (Basic Structure Doctrine)\n3. R.C. Poudyal v. Union of India (Article 371F upheld)\n4. P. Sambamurthy v. State of Andhra Pradesh (Article 371D(5) invalidation)\nSelect the correct answer using the codes given below:",
            "stem_ta": "பகுதி XXI மற்றும் கூட்டாட்சி தொடர்பான பின்வரும் மைல்கல் உச்ச நீதிமன்றத் தீர்ப்புகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. சரத்து 370 ரத்து செய்யப்பட்டதை உறுதி செய்த உச்ச நீதிமன்ற அரசியலமைப்பு அமர்வுத் தீர்ப்பு\n2. கேசவானந்த பாரதி எதிர் கேரள அரசு (அடிப்படை கட்டமைப்புக் கோட்பாடு)\n3. ஆர்.சி. பௌடியால் எதிர் இந்திய ஒன்றியம் (சரத்து 371F உறுதி செய்யப்பட்டது)\n4. பி. சாம்பமூர்த்தி எதிர் ஆந்திரப் பிரதேச அரசு (சரத்து 371D(5) ரத்து செய்யப்பட்டது)\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("2 - 4 - 3 - 1", "2 - 4 - 3 - 1"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4"),
                ("2 - 3 - 4 - 1", "2 - 3 - 4 - 1"),
                ("4 - 2 - 3 - 1", "4 - 2 - 3 - 1")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is:\n2. Kesavananda Bharati (24 April 1973)\n→ 4. P. Sambamurthy (1987)\n→ 3. R.C. Poudyal (1994)\n→ 1. In Re: Article 370 (11 December 2023).\nSequence: 2 → 4 → 3 → 1.",
            "exp_ta": "சரியான காலவரிசை:\n2. கேசவானந்த பாரதி (24 ஏப்ரல் 1973)\n→ 4. பி. சாம்பமூர்த்தி (1987)\n→ 3. ஆர்.சி. பௌடியால் (1994)\n→ 1. சரத்து 370 தீர்ப்பு (11 டிசம்பர் 2023).\nவரிசை: 2 → 4 → 3 → 1.",
            "why_a_en": "Accurately follows 1973 -> 1987 -> 1994 -> 2023.",
            "why_a_ta": "1973 -> 1987 -> 1994 -> 2023 என்ற காலவரிசையைத் துல்லியமாகப் பின்பற்றுகிறது.",
            "why_b_en": "Incorrect presented stem sequence.",
            "why_b_ta": "வினாவில் கொடுக்கப்பட்ட தவறான வரிசை.",
            "why_c_en": "Inverts Sambamurthy and Poudyal.",
            "why_c_ta": "சாம்பமூர்த்தி மற்றும் பௌடியாலை மாற்றுகிறது.",
            "why_d_en": "Places Sambamurthy before Kesavananda Bharati.",
            "why_d_ta": "கேசவானந்த பாரதிக்கு முன் சாம்பமூர்த்தியை வைக்கிறது.",
            "tip_en": "Kesavananda (1973) -> Sambamurthy (1987) -> Poudyal (1994) -> Art 370 verdict (2023).",
            "tip_ta": "கேசவானந்தா (1973) -> சாம்பமூர்த்தி (1987) -> பௌடியால் (1994) -> சரத்து 370 தீர்ப்பு (2023).",
            "fact_en": "Basic Structure Doctrine from Kesavananda was applied in Sambamurthy to invalidate Art 371D(5).",
            "fact_ta": "சாம்பமூர்த்தி வழக்கில் சரத்து 371D(5)-ஐ ரத்து செய்ய கேசவானந்தாவின் அடிப்படைக் கட்டமைப்புக் கோட்பாடு பயன்படுத்தப்பட்டது."
        },
        # 22
        {
            "subtopic": "Goa Integration Milestones",
            "stem_en": "Arrange the following historic milestones in the constitutional journey of Goa in chronological order:\n1. 56th Constitutional Amendment Act granting Statehood with Article 371I\n2. Operation Vijay liberating Goa from Portuguese colonial rule\n3. Historic Goa Opinion Poll rejecting merger with Maharashtra\n4. 12th Constitutional Amendment Act incorporating Goa, Daman and Diu as a Union Territory\nSelect the correct answer using the codes given below:",
            "stem_ta": "கோவாவின் அரசியலமைப்புப் பயணத்தில் பின்வரும் வரலாற்று மைல்கற்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. சரத்து 371I-வுடன் மாநில அந்தஸ்து வழங்கிய 56வது அரசியலமைப்பு திருத்தச் சட்டம்\n2. போர்ச்சுகீசிய காலனித்துவ ஆட்சியிலிருந்து கோவாவை விடுவித்த ஆபரேஷன் விஜய்\n3. மகாராஷ்டிராவுடன் இணைவதை நிராகரித்த வரலாற்றுச் சிறப்புமிக்க கோவா கருத்துக்கணிப்பு\n4. கோவா, டாமன் மற்றும் டையூவை யூனியன் பிரதேசமாக இணைத்த 12வது அரசியலமைப்பு திருத்தச் சட்டம்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("2 - 4 - 3 - 1", "2 - 4 - 3 - 1"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4"),
                ("2 - 3 - 4 - 1", "2 - 3 - 4 - 1"),
                ("4 - 2 - 3 - 1", "4 - 2 - 3 - 1")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is:\n2. Operation Vijay (19 December 1961)\n→ 4. 12th Amendment Act (March 1962)\n→ 3. Goa Opinion Poll (16 January 1967)\n→ 1. 56th Amendment Act (30 May 1987).\nSequence: 2 → 4 → 3 → 1.",
            "exp_ta": "சரியான காலவரிசை:\n2. ஆபரேஷன் விஜய் (19 டிசம்பர் 1961)\n→ 4. 12வது திருத்தச் சட்டம் (மார்ச் 1962)\n→ 3. கோவா கருத்துக்கணிப்பு (16 ஜனவரி 1967)\n→ 1. 56வது திருத்தச் சட்டம் (30 மே 1987).\nவரிசை: 2 → 4 → 3 → 1.",
            "why_a_en": "Accurately traces: 1961 -> 1962 -> 1967 -> 1987.",
            "why_a_ta": "1961 -> 1962 -> 1967 -> 1987 என்ற காலவரிசையைத் துல்லியமாகப் பின்பற்றுகிறது.",
            "why_b_en": "Incorrect presented stem sequence.",
            "why_b_ta": "வினாவில் கொடுக்கப்பட்ட தவறான வரிசை.",
            "why_c_en": "Places 1967 Opinion Poll before 1962 12th Amendment.",
            "why_c_ta": "1962 12வது திருத்தத்திற்கு முன் 1967 கருத்துக்கணிப்பை வைக்கிறது.",
            "why_d_en": "Places 12th Amendment before Operation Vijay.",
            "why_d_ta": "ஆபரேஷன் விஜய்க்கு முன் 12வது திருத்தத்தை வைக்கிறது.",
            "tip_en": "Liberation (1961) -> 12th CAA (1962) -> Opinion Poll (1967) -> Statehood (1987).",
            "tip_ta": "விடுதலை (1961) -> 12வது திருத்தம் (1962) -> கருத்துக்கணிப்பு (1967) -> மாநில அந்தஸ்து (1987).",
            "fact_en": "The 1967 Opinion Poll is India's only official referendum held so far in independent India.",
            "fact_ta": "1967 கருத்துக்கணிப்பு சுதந்திர இந்தியாவில் இதுவரை நடத்தப்பட்ட ஒரே அதிகாரப்பூர்வ பொது வாக்கெடுப்பாகும்."
        },
        # 23
        {
            "subtopic": "Arunachal Pradesh Evolution Timeline",
            "stem_en": "Arrange the following stages in the evolution of Arunachal Pradesh in chronological order:\n1. 55th Constitutional Amendment Act granting Statehood with Article 371H\n2. Demarcation of the McMahon Line at the Simla Convention\n3. Renaming of NEFA as Arunachal Pradesh and conversion into Union Territory\n4. North-East Frontier Agency (NEFA) created under special administrative framework\nSelect the correct answer using the codes given below:",
            "stem_ta": "அருணாச்சலப் பிரதேசத்தின் வளர்ச்சியில் பின்வரும் நிலைகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. சரத்து 371H-வுடன் மாநில அந்தஸ்து வழங்கிய 55வது அரசியலமைப்பு திருத்தச் சட்டம்\n2. சிம்லா மாநாட்டில் மக்மஹோன் கோடு வரையறுக்கப்படுதல்\n3. நெஃபா அருணாச்சலப் பிரதேசம் எனப் பெயர் மாற்றப்பட்டு யூனியன் பிரதேசமாக மாற்றப்படுதல்\n4. சிறப்பு நிர்வாகக் கட்டமைப்பின் கீழ் வடகிழக்கு எல்லைப்புற முகமை (NEFA) உருவாக்கப்படுதல்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("2 - 4 - 3 - 1", "2 - 4 - 3 - 1"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4"),
                ("2 - 3 - 4 - 1", "2 - 3 - 4 - 1"),
                ("4 - 2 - 3 - 1", "4 - 2 - 3 - 1")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is:\n2. McMahon Line (1914)\n→ 4. NEFA created (1954)\n→ 3. Renamed Arunachal Pradesh & made UT (20 January 1972)\n→ 1. Full Statehood via 55th CAA (20 February 1987 / enacted 1986).\nSequence: 2 → 4 → 3 → 1.",
            "exp_ta": "சரியான காலவரிசை:\n2. மக்மஹோன் கோடு (1914)\n→ 4. நெஃபா உருவாக்கப்படுதல் (1954)\n→ 3. அருணாச்சல் எனப் பெயர் மாற்றம் & யூனியன் பிரதேசம் (1972)\n→ 1. 55வது திருத்தம் மூலம் முழு மாநில அந்தஸ்து (1987).\nவரிசை: 2 → 4 → 3 → 1.",
            "why_a_en": "Accurately traces: 1914 -> 1954 -> 1972 -> 1987.",
            "why_a_ta": "1914 -> 1954 -> 1972 -> 1987 என்ற காலவரிசையைத் துல்லியமாகப் பின்பற்றுகிறது.",
            "why_b_en": "Incorrect presented stem sequence.",
            "why_b_ta": "வினாவில் கொடுக்கப்பட்ட தவறான வரிசை.",
            "why_c_en": "Places 1972 UT status before 1954 NEFA creation.",
            "why_c_ta": "1954 நெஃபா உருவாக்கத்திற்கு முன் 1972 யூனியன் பிரதேச நிலையை வைக்கிறது.",
            "why_d_en": "Places 1954 NEFA before 1914 McMahon line.",
            "why_d_ta": "1914 மக்மஹோன் கோட்டிற்கு முன் 1954 நெஃபாவை வைக்கிறது.",
            "tip_en": "McMahon (1914) -> NEFA (1954) -> UT Arunachal (1972) -> Statehood (1987).",
            "tip_ta": "மக்மஹோன் (1914) -> நெஃபா (1954) -> அருணாச்சல் யூனியன் பிரதேசம் (1972) -> மாநில அந்தஸ்து (1987).",
            "fact_en": "Bibhabasu Das Shastri suggested the name 'Arunachal Pradesh' (Land of the Dawn-lit Mountains).",
            "fact_ta": "பிபாபாசு தாஸ் சாஸ்திரி 'அருணாச்சலப் பிரதேசம்' (சூரிய உதயம் தோன்றும் மலைகளின் நிலம்) என்ற பெயரைப் பரிந்துரைத்தார்."
        },
        # 24
        {
            "subtopic": "Part XXI Title and Amendments Evolution",
            "stem_en": "Arrange the following developmental stages of Part XXI of the Constitution in chronological order:\n1. 98th Constitutional Amendment Act inserts Article 371J\n2. Part XXI commences titled 'Temporary and Transitional Provisions'\n3. 13th Constitutional Amendment Act adds 'and Special' to Part XXI title\n4. 7th Constitutional Amendment Act amends Article 371\nSelect the correct answer using the codes given below:",
            "stem_ta": "அரசியலமைப்பின் பகுதி XXI-ன் பின்வரும் வளர்ச்சிப் படிகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. 98வது அரசியலமைப்பு திருத்தச் சட்டம் சரத்து 371J-ஐ சேர்த்தல்\n2. 'தற்காலிக மற்றும் இடைமாற்ற ஏற்பாடுகள்' என்ற தலைப்புடன் பகுதி XXI தொடங்குதல்\n3. 13வது அரசியலமைப்பு திருத்தச் சட்டம் பகுதி XXI தலைப்பில் 'மற்றும் சிறப்பு' என்பதைச் சேர்த்தல்\n4. 7வது அரசியலமைப்பு திருத்தச் சட்டம் சரத்து 371-ஐ திருத்துதல்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("2 - 4 - 3 - 1", "2 - 4 - 3 - 1"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4"),
                ("2 - 3 - 4 - 1", "2 - 3 - 4 - 1"),
                ("4 - 2 - 3 - 1", "4 - 2 - 3 - 1")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is:\n2. Original Constitution commences Part XXI (26 January 1950)\n→ 4. 7th Amendment Act amends Art 371 (1 November 1956)\n→ 3. 13th Amendment Act adds 'and Special' (December 1962)\n→ 1. 98th Amendment Act adds Art 371J (January 2013 / enacted 2012).\nSequence: 2 → 4 → 3 → 1.",
            "exp_ta": "சரியான காலவரிசை:\n2. அசல் அரசியலமைப்பு பகுதி XXI தொடங்குதல் (26 ஜனவரி 1950)\n→ 4. 7வது திருத்தம் சரத்து 371-ஐ திருத்துதல் (1956)\n→ 3. 13வது திருத்தம் 'மற்றும் சிறப்பு' என்பதைச் சேர்த்தல் (1962)\n→ 1. 98வது திருத்தம் சரத்து 371J-ஐ சேர்த்தல் (2012).\nவரிசை: 2 → 4 → 3 → 1.",
            "why_a_en": "Accurately traces: 1950 -> 1956 -> 1962 -> 2012.",
            "why_a_ta": "1950 -> 1956 -> 1962 -> 2012 என்ற காலவரிசையைத் துல்லியமாகப் பின்பற்றுகிறது.",
            "why_b_en": "Incorrect presented stem sequence.",
            "why_b_ta": "வினாவில் கொடுக்கப்பட்ட தவறான வரிசை.",
            "why_c_en": "Places 1962 Amendment before 1956 Amendment.",
            "why_c_ta": "1956 திருத்தத்திற்கு முன் 1962 திருத்தத்தை வைக்கிறது.",
            "why_d_en": "Places 1956 Amendment before 1950 commencement.",
            "why_d_ta": "1950 தொடக்கத்திற்கு முன் 1956 திருத்தத்தை வைக்கிறது.",
            "tip_en": "Part XXI evolution: 1950 (orig) -> 1956 (7th CAA) -> 1962 (13th CAA) -> 2012 (98th CAA).",
            "tip_ta": "பகுதி XXI வளர்ச்சி: 1950 (அசல்) -> 1956 (7வது திருத்தம்) -> 1962 (13வது திருத்தம்) -> 2012 (98வது திருத்தம்).",
            "fact_en": "Part XXI today houses 12 states across Articles 371 to 371-J.",
            "fact_ta": "பகுதி XXI இன்று சரத்துகள் 371 முதல் 371-J வரை 12 மாநிலங்களை உள்ளடக்கியுள்ளது."
        },
        # 25
        {
            "subtopic": "Supreme Court J&K Jurisprudence",
            "stem_en": "Arrange the following decisions of the Supreme Court concerning Article 370 in chronological order:\n1. In Re: Article 370 of the Constitution (5-judge bench unanimous verdict)\n2. Prem Nath Kaul v. State of Jammu and Kashmir\n3. Mohd. Maqbool Damnoo v. State of Jammu and Kashmir\n4. Sampat Prakash v. State of Jammu and Kashmir\nSelect the correct answer using the codes given below:",
            "stem_ta": "சரத்து 370 தொடர்பான உச்ச நீதிமன்றத்தின் பின்வரும் தீர்ப்புகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:\n1. சரத்து 370 மறுஆய்வு வழக்கு (5 நீதிபதிகள் அமர்வின் ஒருமனதான தீர்ப்பு)\n2. பிரேம் நாத் கவுல் எதிர் ஜம்மு காஷ்மீர் அரசு\n3. முகமது மக்பூல் தம்னூ எதிர் ஜம்மு காஷ்மீர் அரசு\n4. சம்பத் பிரகாஷ் எதிர் ஜம்மு காஷ்மீர் அரசு\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
            "options": [
                ("2 - 4 - 3 - 1", "2 - 4 - 3 - 1"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4"),
                ("2 - 3 - 4 - 1", "2 - 3 - 4 - 1"),
                ("4 - 2 - 3 - 1", "4 - 2 - 3 - 1")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is:\n2. Prem Nath Kaul (1959)\n→ 4. Sampat Prakash (1968)\n→ 3. Mohd. Maqbool Damnoo (1972)\n→ 1. In Re: Article 370 (11 December 2023).\nSequence: 2 → 4 → 3 → 1.",
            "exp_ta": "சரியான காலவரிசை:\n2. பிரேம் நாத் கவுல் (1959)\n→ 4. சம்பத் பிரகாஷ் (1968)\n→ 3. முகமது மக்பூல் தம்னூ (1972)\n→ 1. சரத்து 370 தீர்ப்பு (11 டிசம்பர் 2023).\nவரிசை: 2 → 4 → 3 → 1.",
            "why_a_en": "Accurately follows: 1959 -> 1968 -> 1972 -> 2023.",
            "why_a_ta": "1959 -> 1968 -> 1972 -> 2023 என்ற காலவரிசையைத் துல்லியமாகப் பின்பற்றுகிறது.",
            "why_b_en": "Incorrect presented stem sequence.",
            "why_b_ta": "வினாவில் கொடுக்கப்பட்ட தவறான வரிசை.",
            "why_c_en": "Places 1972 Damnoo before 1968 Sampat Prakash.",
            "why_c_ta": "1968 சம்பத் பிரகாஷுக்கு முன் 1972 தம்னூவை வைக்கிறது.",
            "why_d_en": "Places 1968 Sampat Prakash before 1959 Prem Nath Kaul.",
            "why_d_ta": "1959 பிரேம் நாத் கவுலுக்கு முன் 1968 சம்பத் பிரகாஷை வைக்கிறது.",
            "tip_en": "J&K cases: Prem Nath Kaul (1959) -> Sampat Prakash (1968) -> Damnoo (1972) -> 2023 Bench.",
            "tip_ta": "ஜம்மு காஷ்மீர் வழக்குகள்: பிரேம் நாத் கவுல் (1959) -> சம்பத் பிரகாஷ் (1968) -> தம்னூ (1972) -> 2023 அமர்வு.",
            "fact_en": "The 2023 Bench reconciled these historical precedents to affirm Article 370 was temporary.",
            "fact_ta": "2023 அமர்வு இந்த வரலாற்று முன்னுதாரணங்களை ஒருங்கிணைத்து சரத்து 370 தற்காலிகமானது என்பதை உறுதி செய்தது."
        }
    ]

    questions = []
    for i, item in enumerate(raw_data, 1):
        qid = f"SPS_C_{i:03d}"
        opts = item["options"]
        correct_key = item["correct_key"]
        q = make_sps_q(
            qid=qid,
            diff="Hard",
            qtype="Chronology MCQ",
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
            tags=["polity", "special_provisions_states", "chronology", item["subtopic"].lower().replace(" ", "_")]
        )
        questions.append(q)
    return questions

def build_chronology_file():
    qs = get_chronology_questions()
    print(f"Generated {len(qs)} raw Chronology questions for Special Provisions for States.")
    balanced = randomize_and_balance_dataset(qs, seed=42)
    
    out_dir = os.path.join("data", "questions", "polity")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "special_provisions_states_chronology.json")
    
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)
    print(f"Saved balanced Chronology MCQs to {out_path}")
    
    rep = ContentValidator.validate_file(out_path, expected_count=25, expected_prefix="SPS_C_")
    print(f"Content Validation: {'PASS' if rep.is_valid else 'FAIL'} | Total: {rep.total_audited}")
    print(f"Keys: {rep.key_distribution}")
    if not rep.is_valid:
        for iss in rep.issues:
            print("  Issue:", iss.severity, iss.field_name, iss.message)
            
    chrono_rep = ChronologyValidator.validate_file(out_path)
    print(f"Chronology Validation: {'PASS' if chrono_rep.is_valid else 'FAIL'} | Total: {chrono_rep.total_questions}")
    if not chrono_rep.is_valid:
        for iss in chrono_rep.issues:
            print("  Chrono Issue:", iss)
            
    return rep.is_valid and chrono_rep.is_valid

if __name__ == "__main__":
    build_chronology_file()
