# -*- coding: utf-8 -*-
"""
Builder for 25 Match the Following MCQs on Union & Its Territory (polity_union_territory).
IDs: UT_MF_001 to UT_MF_025.
Strictly conforms to TNPSC 24-field schema, bilingual parity, audit rules ("Match" and "List").
"""
import json
import os
import sys
from ut_mcq_helper import make_ut_q, balance_question_keys
from tools.nova_content_engine.validator import ContentValidator

def get_match_questions():
    questions = []

    # MF01: Articles 1-4
    questions.append(make_ut_q(
        qid="UT_MF_001", diff="Medium", qtype="Match the following",
        subtopic="Articles 1-4 of the Constitution",
        en_stem="Match List-I (Constitutional Articles) with List-II (Provisions) and select the correct answer using the codes given below the lists:\nList-I:\n(A) Article 1\n(B) Article 2\n(C) Article 3\n(D) Article 4\nList-II:\n1. Admission or establishment of new States\n2. Formation of new States and alteration of areas, boundaries or names\n3. Name and territory of the Union\n4. Laws made under Articles 2 and 3 not deemed to be constitutional amendments",
        ta_stem="பட்டியல்-I (அரசியலமைப்பு உறுப்புகள்) உடன் பட்டியல்-II (விதிகளை) பொருத்தி கீழே உள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\n(A) உறுப்பு 1\n(B) உறுப்பு 2\n(C) உறுப்பு 3\n(D) உறுப்பு 4\nபட்டியல்-II:\n1. புதிய மாநிலங்களை அனுமதித்தல் அல்லது நிறுவுதல்\n2. புதிய மாநிலங்களை உருவாக்குதல் மற்றும் எல்லைகள், பெயர்களை மாற்றுதல்\n3. ஒன்றியத்தின் பெயர் மற்றும் நிலப்பரப்பு\n4. உறுப்புகள் 2 மற்றும் 3-ன் கீழ் இயற்றப்படும் சட்டங்கள் அரசியலமைப்பு திருத்தமாகக் கருதப்படாது",
        en_a="A-3, B-1, C-2, D-4", ta_a="A-3, B-1, C-2, D-4",
        en_b="A-1, B-3, C-2, D-4", ta_b="A-1, B-3, C-2, D-4",
        en_c="A-3, B-2, C-1, D-4", ta_c="A-3, B-2, C-1, D-4",
        en_d="A-2, B-1, C-3, D-4", ta_d="A-2, B-1, C-3, D-4",
        correct_key="A",
        exp_en="Article 1 deals with Name and territory of the Union (3). Article 2 deals with Admission or establishment of new States (1). Article 3 deals with Formation of new States and alteration of areas/boundaries/names (2). Article 4 provides that laws under Articles 2 and 3 are not deemed amendments under Article 368 (4). Hence, A-3, B-1, C-2, D-4.",
        exp_ta="உறுப்பு 1: ஒன்றியத்தின் பெயர் மற்றும் எல்லை (3). உறுப்பு 2: புதிய மாநிலங்களை இணைத்தல்/நிறுவுதல் (1). உறுப்பு 3: புதிய மாநிலங்களை உருவாக்குதல், எல்லை/பெயர் மாற்றம் (2). உறுப்பு 4: உறுப்புகள் 2 & 3-ன் சட்டங்கள் அரசியலமைப்புத் திருத்தமாகாது (4). எனவே சரியான பொருத்தம் A-3, B-1, C-2, D-4.",
        why_a_en="Direct matching: Article 1 = 3, Article 2 = 1, Article 3 = 2, Article 4 = 4.",
        why_a_ta="நேரடிப் பொருத்தம்: உறுப்பு 1 = 3, உறுப்பு 2 = 1, உறுப்பு 3 = 2, உறுப்பு 4 = 4.",
        why_b_en="Article 1 is not 1; Article 1 defines Name and territory.",
        why_b_ta="உறுப்பு 1 என்பது புதிய மாநிலங்களை அனுமதிப்பது அல்ல.",
        why_c_en="Article 2 and Article 3 are swapped.",
        why_c_ta="உறுப்பு 2 மற்றும் 3 மாற்றி அமைக்கப்பட்டுள்ளன.",
        why_d_en="Article 1 is not 2.",
        why_d_ta="உறுப்பு 1 என்பது 2 அல்ல.",
        tip_en="Articles 1-4 cover Part I: Name/territory (1), External admission (2), Internal reorganisation (3), Consequential simple laws (4).",
        tip_ta="பகுதி I (உறுப்புகள் 1-4): பெயர்/நிலப்பரப்பு (1), வெளிப்பகுதி ஏற்பு (2), உள் மறுசீரமைப்பு (3), சாதாரண பெரும்பான்மை (4).",
        fact_en="Part I of the Constitution contains only four articles (Articles 1 to 4).",
        fact_ta="அரசியலமைப்பின் பகுதி I வெறும் நான்கு உறுப்புகளை மட்டுமே கொண்டுள்ளது (உறுப்புகள் 1 முதல் 4).",
        tags=["polity", "union_territory", "articles_1_4", "match_the_following"]
    ))

    # MF02: Committees on Linguistic Reorganisation
    questions.append(make_ut_q(
        qid="UT_MF_002", diff="Medium", qtype="Match the following",
        subtopic="Linguistic Reorganisation and Evolution of States",
        en_stem="Match List-I (Committees / Commissions) with List-II (Year Appointed) and select the correct answer using the codes given below the lists:\nList-I:\n(A) Dhar Commission\n(B) JVP Committee\n(C) Fazl Ali Commission (SRC)\n(D) Shah Commission\nList-II:\n1. June 1948\n2. December 1948\n3. December 1953\n4. April 1966",
        ta_stem="பட்டியல்-I (குழுக்கள் / ஆணையங்கள்) உடன் பட்டியல்-II (அமைக்கப்பட்ட ஆண்டு) பொருத்தி கீழே உள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\n(A) தார் ஆணையம்\n(B) ஜே.வி.பி குழு\n(C) பசல் அலி ஆணையம் (SRC)\n(D) ஷா ஆணையம்\nபட்டியல்-II:\n1. ஜூன் 1948\n2. டிசம்பர் 1948\n3. டிசம்பர் 1953\n4. ஏப்ரல் 1966",
        en_a="A-1, B-2, C-3, D-4", ta_a="A-1, B-2, C-3, D-4",
        en_b="A-2, B-1, C-3, D-4", ta_b="A-2, B-1, C-3, D-4",
        en_c="A-1, B-3, C-2, D-4", ta_c="A-1, B-3, C-2, D-4",
        en_d="A-4, B-2, C-3, D-1", ta_d="A-4, B-2, C-3, D-1",
        correct_key="A",
        exp_en="Dhar Commission was appointed in June 1948 (1). JVP Committee was formed in December 1948 (2). Fazl Ali Commission was appointed in December 1953 (3). Shah Commission was appointed in April 1966 (4). Hence, A-1, B-2, C-3, D-4.",
        exp_ta="தார் ஆணையம் ஜூன் 1948-ல் அமைக்கப்பட்டது (1). ஜே.வி.பி குழு டிசம்பர் 1948-ல் அமைக்கப்பட்டது (2). பசல் அலி ஆணையம் டிசம்பர் 1953-ல் அமைக்கப்பட்டது (3). ஷா ஆணையம் ஏப்ரல் 1966-ல் அமைக்கப்பட்டது (4). எனவே சரியான பொருத்தம் A-1, B-2, C-3, D-4.",
        why_a_en="All committees match their respective chronological appointment dates.",
        why_a_ta="அனைத்து குழுக்களும் அவற்றின் காலவரிசை நியமன தேதிகளுடன் சரியாகப் பொருந்துகின்றன.",
        why_b_en="Dhar and JVP dates are inverted.",
        why_b_ta="தார் மற்றும் JVP தேதிகள் தலைகீழாக உள்ளன.",
        why_c_en="JVP was Dec 1948, not Dec 1953.",
        why_c_ta="JVP 1948-ல் அமைக்கப்பட்டது, 1953-ல் அல்ல.",
        why_d_en="Shah commission was in 1966, not 1948.",
        why_d_ta="ஷா ஆணையம் 1966-ல் அமைக்கப்பட்டது.",
        tip_en="Chronology: Dhar (Jun 1948) -> JVP (Dec 1948) -> Fazl Ali (Dec 1953) -> Shah (Apr 1966).",
        tip_ta="காலவரிசை: தார் (ஜூன் 1948) -> JVP (டிச 1948) -> பசல் அலி (டிச 1953) -> ஷா (ஏப் 1966).",
        fact_en="All four committees shaped the modern federal map of India.",
        fact_ta="இந்த நான்கு குழுக்களுமே இந்தியாவின் நவீன கூட்டாட்சி வரைபடத்தை உருவாக்கின.",
        tags=["polity", "union_territory", "committees", "match_the_following"]
    ))

    # MF03: Constitutional Amendments and Territories
    questions.append(make_ut_q(
        qid="UT_MF_003", diff="Medium", qtype="Match the following",
        subtopic="Article 2: Admission or Establishment of New States",
        en_stem="Match List-I (Constitutional Amendment Act) with List-II (Territory Integrated) and select the correct answer using the codes given below the lists:\nList-I:\n(A) 10th Amendment Act, 1961\n(B) 12th Amendment Act, 1962\n(C) 14th Amendment Act, 1962\n(D) 36th Amendment Act, 1975\nList-II:\n1. Dadra and Nagar Haveli\n2. Goa, Daman and Diu\n3. Puducherry\n4. Sikkim (Full Statehood)",
        ta_stem="பட்டியல்-I (அரசியலமைப்புத் திருத்தச் சட்டம்) உடன் பட்டியல்-II (இணைக்கப்பட்ட நிலப்பரப்பு) பொருத்தி கீழே உள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\n(A) 10-வது திருத்தச் சட்டம், 1961\n(B) 12-வது திருத்தச் சட்டம், 1962\n(C) 14-வது திருத்தச் சட்டம், 1962\n(D) 36-வது திருத்தச் சட்டம், 1975\nபட்டியல்-II:\n1. தாத்ரா மற்றும் நகர் ஹவேலி\n2. கோவா, தாமன் மற்றும் தியூ\n3. புதுச்சேரி\n4. சிக்கிம் (முழு மாநில அந்தஸ்து)",
        en_a="A-1, B-2, C-3, D-4", ta_a="A-1, B-2, C-3, D-4",
        en_b="A-2, B-1, C-3, D-4", ta_b="A-2, B-1, C-3, D-4",
        en_c="A-1, B-3, C-2, D-4", ta_c="A-1, B-3, C-2, D-4",
        en_d="A-3, B-2, C-1, D-4", ta_d="A-3, B-2, C-1, D-4",
        correct_key="A",
        exp_en="10th CAA 1961 integrated Dadra and Nagar Haveli (1). 12th CAA 1962 integrated Goa, Daman and Diu (2). 14th CAA 1962 integrated Puducherry (3). 36th CAA 1975 admitted Sikkim as a full-fledged State (4). Hence, A-1, B-2, C-3, D-4.",
        exp_ta="10-வது திருத்தம் 1961: தாத்ரா நகர் ஹவேலி (1). 12-வது திருத்தம் 1962: கோவா தாமன் தியூ (2). 14-வது திருத்தம் 1962: புதுச்சேரி (3). 36-வது திருத்தம் 1975: சிக்கிம் முழு மாநிலம் (4). எனவே சரியான பொருத்தம் A-1, B-2, C-3, D-4.",
        why_a_en="Exact matching between constitutional amendments and the territories integrated.",
        why_a_ta="திருத்தச் சட்டங்களுக்கும் இணைக்கப்பட்ட பகுதிகளுக்கும் இடையிலான துல்லியமான பொருத்தம்.",
        why_b_en="10th CAA was Dadra & Nagar Haveli, not Goa.",
        why_b_ta="10-வது திருத்தம் தாத்ரா நகர் ஹவேலிக்கு உரியது, கோவாவிற்கு அல்ல.",
        why_c_en="12th CAA was Goa, Daman & Diu, not Puducherry.",
        why_c_ta="12-வது திருத்தம் கோவாவிற்கு உரியது.",
        why_d_en="10th CAA is not Puducherry.",
        why_d_ta="10-வது திருத்தம் புதுச்சேரி அல்ல.",
        tip_en="Amendments sequence: 10th (DNH 1961) -> 12th (Goa 1962) -> 14th (Puducherry 1962) -> 36th (Sikkim 1975).",
        tip_ta="திருத்தங்கள் வரிசை: 10-வது (DNH 1961) -> 12-வது (கோவா 1962) -> 14-வது (புதுச்சேரி 1962) -> 36-வது (சிக்கிம் 1975).",
        fact_en="All these acquisitions were made through Article 2 powers of Parliament.",
        fact_ta="இவை அனைத்தும் நாடாளுமன்றத்தின் உறுப்பு 2 அதிகாரங்களின் கீழ் மேற்கொள்ளப்பட்டன.",
        tags=["polity", "union_territory", "amendments", "territories", "match_the_following"]
    ))

    # MF04: States and Years of Formation (1960s-1970s)
    questions.append(make_ut_q(
        qid="UT_MF_004", diff="Medium", qtype="Match the following",
        subtopic="Linguistic Reorganisation and Evolution of States",
        en_stem="Match List-I (State Created) with List-II (Year of Creation) and select the correct answer using the codes given below the lists:\nList-I:\n(A) Gujarat\n(B) Nagaland\n(C) Haryana\n(D) Himachal Pradesh\nList-II:\n1. 1960\n2. 1963\n3. 1966\n4. 1971",
        ta_stem="பட்டியல்-I (உருவாக்கப்பட்ட மாநிலம்) உடன் பட்டியல்-II (உருவான ஆண்டு) பொருத்தி கீழே உள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\n(A) குஜராத்\n(B) நாகாலாந்து\n(C) ஹரியானா\n(D) இமாச்சல பிரதேசம்\nபட்டியல்-II:\n1. 1960\n2. 1963\n3. 1966\n4. 1971",
        en_a="A-1, B-2, C-3, D-4", ta_a="A-1, B-2, C-3, D-4",
        en_b="A-2, B-1, C-3, D-4", ta_b="A-2, B-1, C-3, D-4",
        en_c="A-1, B-3, C-2, D-4", ta_c="A-1, B-3, C-2, D-4",
        en_d="A-3, B-2, C-1, D-4", ta_d="A-3, B-2, C-1, D-4",
        correct_key="A",
        exp_en="Gujarat was created as the 15th state in 1960 (1). Nagaland as 16th state in 1963 (2). Haryana as 17th state in 1966 (3). Himachal Pradesh elevated to 18th state in 1971 (4). Hence, A-1, B-2, C-3, D-4.",
        exp_ta="குஜராத் 15-வது மாநிலமாக 1960-ல் உருவானது (1). நாகாலாந்து 16-வது மாநிலமாக 1963-ல் உருவானது (2). ஹரியானா 17-வது மாநிலமாக 1966-ல் உருவானது (3). இமாச்சல பிரதேசம் 18-வது மாநிலமாக 1971-ல் உருவானது (4). எனவே சரியான பொருத்தம் A-1, B-2, C-3, D-4.",
        why_a_en="Exact chronological match: Gujarat (1960), Nagaland (1963), Haryana (1966), HP (1971).",
        why_a_ta="துல்லியமான காலவரிசைப் பொருத்தம்: குஜராத் (1960), நாகாலாந்து (1963), ஹரியானா (1966), இமாச்சலம் (1971).",
        why_b_en="Nagaland was 1963, not 1960.",
        why_b_ta="நாகாலாந்து 1963, 1960 அல்ல.",
        why_c_en="Nagaland and Haryana years are swapped.",
        why_c_ta="நாகாலாந்து மற்றும் ஹரியானா ஆண்டுகள் மாற்றப்பட்டுள்ளன.",
        why_d_en="Gujarat was 1960, not 1966.",
        why_d_ta="குஜராத் 1960.",
        tip_en="States numbers 15 to 18: Gujarat (15th, 1960), Nagaland (16th, 1963), Haryana (17th, 1966), HP (18th, 1971).",
        tip_ta="15 முதல் 18 வரை மாநிலங்கள்: குஜராத் (15, 1960), நாகாலாந்து (16, 1963), ஹரியானா (17, 1966), இமாச்சலம் (18, 1971).",
        fact_en="All these states were created by simple majority laws under Article 3/4.",
        fact_ta="இம்மாநிலங்கள் அனைத்தும் உறுப்பு 3/4-ன் கீழ் சாதாரண பெரும்பான்மை சட்டங்களால் உருவாக்கப்பட்டன.",
        tags=["polity", "union_territory", "states_formation", "match_the_following"]
    ))

    # MF05: States Formed in 1987 & 2000
    questions.append(make_ut_q(
        qid="UT_MF_005", diff="Medium", qtype="Match the following",
        subtopic="Linguistic Reorganisation and Evolution of States",
        en_stem="Match List-I (State) with List-II (Statehood Rank / Number) and select the correct answer using the codes given below the lists:\nList-I:\n(A) Mizoram\n(B) Arunachal Pradesh\n(C) Goa\n(D) Chhattisgarh\nList-II:\n1. 23rd State\n2. 24th State\n3. 25th State\n4. 26th State",
        ta_stem="பட்டியல்-I (மாநிலம்) உடன் பட்டியல்-II (மாநிலத்தின் வரிசை எண்) பொருத்தி கீழே உள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\n(A) மிசோரம்\n(B) அருணாச்சல பிரதேசம்\n(C) கோவா\n(D) சத்தீஸ்கர்\nபட்டியல்-II:\n1. 23-வது மாநிலம்\n2. 24-வது மாநிலம்\n3. 25-வது மாநிலம்\n4. 26-வது மாநிலம்",
        en_a="A-1, B-2, C-3, D-4", ta_a="A-1, B-2, C-3, D-4",
        en_b="A-2, B-1, C-3, D-4", ta_b="A-2, B-1, C-3, D-4",
        en_c="A-1, B-3, C-2, D-4", ta_c="A-1, B-3, C-2, D-4",
        en_d="A-3, B-2, C-1, D-4", ta_d="A-3, B-2, C-1, D-4",
        correct_key="A",
        exp_en="Mizoram became the 23rd State in Feb 1987 (1). Arunachal Pradesh became 24th State in Feb 1987 (2). Goa became 25th State in May 1987 (3). Chhattisgarh became 26th State on Nov 1, 2000 (4). Hence, A-1, B-2, C-3, D-4.",
        exp_ta="மிசோரம் பிப்ரவரி 1987-ல் 23-வது மாநிலமானது (1). அருணாச்சல பிரதேசம் பிப்ரவரி 1987-ல் 24-வது மாநிலமானது (2). கோவா மே 1987-ல் 25-வது மாநிலமானது (3). சத்தீஸ்கர் நவம்பர் 1, 2000-ல் 26-வது மாநிலமானது (4). எனவே சரியான பொருத்தம் A-1, B-2, C-3, D-4.",
        why_a_en="Exact sequential rank of Indian states: Mizoram (23), Arunachal (24), Goa (25), Chhattisgarh (26).",
        why_a_ta="இந்திய மாநிலங்களின் துல்லியமான வரிசை எண்: மிசோரம் (23), அருணாச்சல் (24), கோவா (25), சத்தீஸ்கர் (26).",
        why_b_en="Mizoram was 23rd, not 24th.",
        why_b_ta="மிசோரம் 23-வது மாநிலமாகும்.",
        why_c_en="Arunachal and Goa ranks are swapped.",
        why_c_ta="அருணாச்சல் மற்றும் கோவா எண்கள் மாற்றப்பட்டுள்ளன.",
        why_d_en="Goa is 25th, not 23rd.",
        why_d_ta="கோவா 25-வது மாநிலம்.",
        tip_en="1987 trio: Mizoram (23), Arunachal (24), Goa (25). Followed by Nov 2000: Chhattisgarh (26), Uttarakhand (27), Jharkhand (28).",
        tip_ta="1987 முப்பெரும் மாநிலங்கள்: மிசோரம் (23), அருணாச்சல் (24), கோவா (25). 2000-ல்: சத்தீஸ்கர் (26), உத்தராகண்ட் (27), ஜார்க்கண்ட் (28).",
        fact_en="Telangana was the 29th State (2014), but total states became 28 after J&K reorganisation in 2019.",
        fact_ta="தெலுங்கானா 29-வது மாநிலமாக உருவானது (2014), ஆனால் 2019 ஜம்மு காஷ்மீர் மாற்றத்திற்குப் பின் மாநிலங்கள் 28 ஆயின.",
        tags=["polity", "union_territory", "statehood_rank", "match_the_following"]
    ))

    # MF06: Renaming of States / UTs and Years
    questions.append(make_ut_q(
        qid="UT_MF_006", diff="Medium", qtype="Match the following",
        subtopic="Renaming of States and UTs",
        en_stem="Match List-I (Old Name -> New Name) with List-II (Year of Renaming) and select the correct answer using the codes given below the lists:\nList-I:\n(A) Madras State -> Tamil Nadu\n(B) Mysore State -> Karnataka\n(C) Uttaranchal -> Uttarakhand\n(D) Orissa -> Odisha\nList-II:\n1. 1969\n2. 1973\n3. 2007\n4. 2011",
        ta_stem="பட்டியல்-I (பழைய பெயர் -> புதிய பெயர்) உடன் பட்டியல்-II (பெயர் மாற்றப்பட்ட ஆண்டு) பொருத்தி கீழே உள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\n(A) மெட்ராஸ் மாகாணம் -> தமிழ்நாடு\n(B) மைசூர் மாநிலம் -> கர்நாடகா\n(C) உத்தராஞ்சல் -> உத்தராகண்ட்\n(D) ஒரிசா -> ஒடிசா\nபட்டியல்-II:\n1. 1969\n2. 1973\n3. 2007\n4. 2011",
        en_a="A-1, B-2, C-3, D-4", ta_a="A-1, B-2, C-3, D-4",
        en_b="A-2, B-1, C-3, D-4", ta_b="A-2, B-1, C-3, D-4",
        en_c="A-1, B-3, C-2, D-4", ta_c="A-1, B-3, C-2, D-4",
        en_d="A-4, B-2, C-3, D-1", ta_d="A-4, B-2, C-3, D-1",
        correct_key="A",
        exp_en="Madras State was renamed Tamil Nadu in 1969 (1). Mysore State was renamed Karnataka in 1973 (2). Uttaranchal became Uttarakhand in 2007 (3). Orissa became Odisha in 2011 (4). Hence, A-1, B-2, C-3, D-4.",
        exp_ta="மெட்ராஸ் மாநிலம் 1969-ல் தமிழ்நாடு என மாறியது (1). மைசூர் 1973-ல் கர்நாடகா என மாறியது (2). உத்தராஞ்சல் 2007-ல் உத்தராகண்ட் என மாறியது (3). ஒரிசா 2011-ல் ஒடிசா என மாறியது (4). எனவே சரியான பொருத்தம் A-1, B-2, C-3, D-4.",
        why_a_en="Exact chronological matches: Tamil Nadu (1969), Karnataka (1973), Uttarakhand (2007), Odisha (2011).",
        why_a_ta="துல்லியமான ஆண்டுகள்: தமிழ்நாடு (1969), கர்நாடகா (1973), உத்தராகண்ட் (2007), ஒடிசா (2011).",
        why_b_en="Tamil Nadu and Karnataka years are swapped.",
        why_b_ta="தமிழ்நாடு மற்றும் கர்நாடகா ஆண்டுகள் மாற்றப்பட்டுள்ளன.",
        why_c_en="Mysore was renamed in 1973, not 2007.",
        why_c_ta="மைசூர் 1973-ல் மாற்றப்பட்டது.",
        why_d_en="Madras was renamed in 1969, not 2011.",
        why_d_ta="மெட்ராஸ் 1969-ல் மாற்றப்பட்டது.",
        tip_en="Renaming years: UP (1950) -> TN (1969) -> Karnataka & Lakshadweep (1973) -> Puducherry (2006) -> Uttarakhand (2007) -> Odisha (2011).",
        tip_ta="பெயர் மாற்றங்கள்: உ.பி (1950) -> தமிழ்நாடு (1969) -> கர்நாடகா & லட்சத்தீவு (1973) -> புதுச்சேரி (2006) -> உத்தராகண்ட் (2007) -> ஒடிசா (2011).",
        fact_en="Article 3 empowers Parliament to alter the name of any State by simple majority.",
        fact_ta="உறுப்பு 3 எந்தவொரு மாநிலத்தின் பெயரையும் மாற்ற சாதாரண பெரும்பான்மை மூலம் நாடாளுமன்றத்திற்கு அதிகாரம் அளிக்கிறது.",
        tags=["polity", "union_territory", "renaming", "match_the_following"]
    ))

    # MF07: High Courts and UTs
    questions.append(make_ut_q(
        qid="UT_MF_007", diff="Medium", qtype="Match the following",
        subtopic="Administration of Union Territories",
        en_stem="Match List-I (High Court) with List-II (Union Territory Jurisdiction) and select the correct answer using the codes given below the lists:\nList-I:\n(A) Madras High Court\n(B) Kerala High Court\n(C) Calcutta High Court\n(D) Bombay High Court\nList-II:\n1. Puducherry\n2. Lakshadweep\n3. Andaman and Nicobar Islands\n4. Dadra and Nagar Haveli and Daman and Diu",
        ta_stem="பட்டியல்-I (உயர்நீதிமன்றம்) உடன் பட்டியல்-II (யூனியன் பிரதேச அதிகார வரம்பு) பொருத்தி கீழே உள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\n(A) சென்னை உயர்நீதிமன்றம்\n(B) கேரள உயர்நீதிமன்றம்\n(C) கல்கத்தா உயர்நீதிமன்றம்\n(D) பம்பாய் உயர்நீதிமன்றம்\nபட்டியல்-II:\n1. புதுச்சேரி\n2. லட்சத்தீவு\n3. அந்தமான் மற்றும் நிக்கோபார் தீவுகள்\n4. தாத்ரா மற்றும் நகர் ஹவேலி மற்றும் தாமன் மற்றும் தியூ",
        en_a="A-1, B-2, C-3, D-4", ta_a="A-1, B-2, C-3, D-4",
        en_b="A-2, B-1, C-3, D-4", ta_b="A-2, B-1, C-3, D-4",
        en_c="A-1, B-3, C-2, D-4", ta_c="A-1, B-3, C-2, D-4",
        en_d="A-3, B-2, C-1, D-4", ta_d="A-3, B-2, C-1, D-4",
        correct_key="A",
        exp_en="Madras HC has jurisdiction over Puducherry (1). Kerala HC has jurisdiction over Lakshadweep (2). Calcutta HC has jurisdiction over Andaman and Nicobar Islands (3). Bombay HC has jurisdiction over DNHDD (4). Hence, A-1, B-2, C-3, D-4.",
        exp_ta="சென்னை உயர்நீதிமன்றம்: புதுச்சேரி (1). கேரள உயர்நீதிமன்றம்: லட்சத்தீவு (2). கல்கத்தா உயர்நீதிமன்றம்: அந்தமான் நிக்கோபார் தீவுகள் (3). பம்பாய் உயர்நீதிமன்றம்: தாத்ரா நகர் ஹவேலி மற்றும் தாமன் தியூ (4). எனவே சரியான பொருத்தம் A-1, B-2, C-3, D-4.",
        why_a_en="Exact jurisdictional matches as established under Article 241 and relevant Parliamentary Acts.",
        why_a_ta="உறுப்பு 241 மற்றும் நாடாளுமன்றச் சட்டங்களின் கீழ் நிறுவப்பட்ட துல்லியமான அதிகார வரம்புகள்.",
        why_b_en="Madras HC does not have jurisdiction over Lakshadweep.",
        why_b_ta="சென்னை உயர்நீதிமன்ற வரம்பில் லட்சத்தீவு இல்லை.",
        why_c_en="Kerala HC does not have jurisdiction over Andaman.",
        why_c_ta="கேரள உயர்நீதிமன்ற வரம்பில் அந்தமான் இல்லை.",
        why_d_en="Calcutta HC is Andaman, not Puducherry.",
        why_d_ta="கல்கத்தா உயர்நீதிமன்ற வரம்பில் அந்தமான் உள்ளது, புதுச்சேரி அல்ல.",
        tip_en="Court jurisdictions: Madras -> Puducherry; Kerala -> Lakshadweep; Calcutta -> A&N; Bombay -> DNHDD; Punjab & Haryana -> Chandigarh.",
        tip_ta="நீதிமன்ற வரம்புகள்: சென்னை -> புதுச்சேரி; கேரளா -> லட்சத்தீவு; கல்கத்தா -> அந்தமான்; பம்பாய் -> DNHDD; பஞ்சாப் & ஹரியானா -> சண்டிகர்.",
        fact_en="Article 241 gives Parliament power to extend or exclude High Court jurisdiction for Union Territories.",
        fact_ta="உறுப்பு 241 உயர்நீதிமன்ற அதிகார வரம்பை யூனியன் பிரதேசங்களுக்கு நீட்டிக்க அல்லது விலக்க நாடாளுமன்றத்திற்கு அதிகாரம் அளிக்கிறது.",
        tags=["polity", "union_territory", "high_courts", "jurisdiction", "match_the_following"]
    ))

    # MF08: Part VIII Constitutional Articles
    questions.append(make_ut_q(
        qid="UT_MF_008", diff="Hard", qtype="Match the following",
        subtopic="Administration of Union Territories",
        en_stem="Match List-I (Article of Part VIII) with List-II (Constitutional Subject Matter) and select the correct answer using the codes given below the lists:\nList-I:\n(A) Article 239\n(B) Article 239A\n(C) Article 239AA\n(D) Article 241\nList-II:\n1. Administration of Union Territories by the President\n2. Creation of local Legislatures or Council of Ministers for certain UTs\n3. Special provisions with respect to Delhi\n4. High Courts for Union Territories",
        ta_stem="பட்டியல்-I (பகுதி VIII-ன் உறுப்புகள்) உடன் பட்டியல்-II (அரசியலமைப்புப் பொருள்) பொருத்தி கீழே உள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\n(A) உறுப்பு 239\n(B) உறுப்பு 239A\n(C) உறுப்பு 239AA\n(D) உறுப்பு 241\nபட்டியல்-II:\n1. குடியரசுத் தலைவரால் யூனியன் பிரதேசங்களை நிர்வகித்தல்\n2. குறிப்பிட்ட UT-களுக்கு உள்ளூர் சட்டமன்றங்கள் அல்லது அமைச்சரவை உருவாக்குதல்\n3. டெல்லி தொடர்பான சிறப்பு விதிகள்\n4. யூனியன் பிரதேசங்களுக்கான உயர்நீதிமன்றங்கள்",
        en_a="A-1, B-2, C-3, D-4", ta_a="A-1, B-2, C-3, D-4",
        en_b="A-2, B-1, C-3, D-4", ta_b="A-2, B-1, C-3, D-4",
        en_c="A-1, B-3, C-2, D-4", ta_c="A-1, B-3, C-2, D-4",
        en_d="A-3, B-2, C-1, D-4", ta_d="A-3, B-2, C-1, D-4",
        correct_key="A",
        exp_en="Article 239: Administration of UTs (1). Article 239A: Creation of legislatures for certain UTs (2). Article 239AA: Special provisions for Delhi (3). Article 241: High Courts for UTs (4). Hence, A-1, B-2, C-3, D-4.",
        exp_ta="உறுப்பு 239: UT-களின் நிர்வாகம் (1). உறுப்பு 239A: UT-களுக்கு சட்டமன்றங்கள் அமைத்தல் (2). உறுப்பு 239AA: டெல்லி சிறப்பு விதிகள் (3). உறுப்பு 241: UT-களுக்கான உயர்நீதிமன்றங்கள் (4). எனவே சரியான பொருத்தம் A-1, B-2, C-3, D-4.",
        why_a_en="Exact match of Part VIII constitutional articles with their respective subjects.",
        why_a_ta="பகுதி VIII அரசியலமைப்பு பிரிவுகளின் துல்லியமான நேரடிப் பொருத்தம்.",
        why_b_en="Article 239 and 239A are inverted.",
        why_b_ta="உறுப்புகள் 239 மற்றும் 239A மாற்றப்பட்டுள்ளன.",
        why_c_en="Article 239A is legislatures, not Delhi provisions.",
        why_c_ta="உறுப்பு 239A என்பது சட்டமன்றங்கள் பற்றியது.",
        why_d_en="Article 239 is not Delhi provisions.",
        why_d_ta="உறுப்பு 239 டெல்லி பற்றியது அல்ல.",
        tip_en="Part VIII articles: 239 (Administration), 239A (Legislatures), 239AA (Delhi), 239AB (Failure of machinery in Delhi), 239B (Ordinance), 240 (Regulations), 241 (High Courts).",
        tip_ta="பகுதி VIII: 239 (நிர்வாகம்), 239A (சட்டமன்றம்), 239AA (டெல்லி), 239AB (டெல்லி ஆட்சி கலைப்பு), 239B (அவசரச் சட்டம்), 240 (விதிமுறைகள்), 241 (உயர்நீதிமன்றங்கள்).",
        fact_en="Article 239AA was inserted by the 69th Constitutional Amendment Act, 1991.",
        fact_ta="உறுப்பு 239AA 1991-ல் 69-வது அரசியலமைப்புத் திருத்தச் சட்டத்தின் மூலம் சேர்க்கப்பட்டது.",
        tags=["polity", "union_territory", "part_viii", "articles", "match_the_following"]
    ))

    # MF09: Administrative Heads of UTs
    questions.append(make_ut_q(
        qid="UT_MF_009", diff="Medium", qtype="Match the following",
        subtopic="Administration of Union Territories",
        en_stem="Match List-I (Union Territory) with List-II (Official Designation of Head) and select the correct answer using the codes given below the lists:\nList-I:\n(A) Delhi\n(B) Chandigarh\n(C) Lakshadweep\n(D) Ladakh\nList-II:\n1. Lieutenant Governor\n2. Administrator (Governor of Punjab ex-officio)\n3. Administrator\n4. Lieutenant Governor",
        ta_stem="பட்டியல்-I (யூனியன் பிரதேசம்) உடன் பட்டியல்-II (நிர்வாகத் தலைவரின் பதவிப் பெயர்) பொருத்தி கீழே உள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\n(A) தில்லி\n(B) சண்டிகர்\n(C) லட்சத்தீவு\n(D) லடாக்\nபட்டியல்-II:\n1. துணைநிலை ஆளுநர் (LG)\n2. நிர்வாகி (பஞ்சாப் ஆளுநர் பதவிவழி)\n3. நிர்வாகி (Administrator)\n4. துணைநிலை ஆளுநர் (LG)",
        en_a="A-1, B-2, C-3, D-4", ta_a="A-1, B-2, C-3, D-4",
        en_b="A-2, B-1, C-3, D-4", ta_b="A-2, B-1, C-3, D-4",
        en_c="A-1, B-3, C-2, D-4", ta_c="A-1, B-3, C-2, D-4",
        en_d="A-3, B-2, C-1, D-4", ta_d="A-3, B-2, C-1, D-4",
        correct_key="A",
        exp_en="Delhi is administered by a Lieutenant Governor (1). Chandigarh is administered by an Administrator who is the ex-officio Governor of Punjab (2). Lakshadweep is administered by an Administrator (3). Ladakh is administered by a Lieutenant Governor (4). Hence, A-1, B-2, C-3, D-4.",
        exp_ta="தில்லி: துணைநிலை ஆளுநர் (1). சண்டிகர்: நிர்வாகி - பஞ்சாப் ஆளுநர் பதவிவழி (2). லட்சத்தீவு: நிர்வாகி (3). லடாக்: துணைநிலை ஆளுநர் (4). எனவே சரியான பொருத்தம் A-1, B-2, C-3, D-4.",
        why_a_en="Exact designations: Delhi (LG), Chandigarh (Administrator/Pb Gov), Lakshadweep (Administrator), Ladakh (LG).",
        why_a_ta="துல்லியமான பதவிப் பெயர்கள்: தில்லி (LG), சண்டிகர் (நிர்வாகி/பஞ்சாப் ஆளுநர்), லட்சத்தீவு (நிர்வாகி), லடாக் (LG).",
        why_b_en="Delhi head is Lieutenant Governor, not Administrator.",
        why_b_ta="தில்லித் தலைவர் துணைநிலை ஆளுநர் ஆவார்.",
        why_c_en="Chandigarh has Governor of Punjab, not Lakshadweep.",
        why_c_ta="சண்டிகருக்கு பஞ்சாப் ஆளுநர் நிர்வாகி.",
        why_d_en="Delhi is not Administrator.",
        why_d_ta="தில்லி நிர்வாகி அல்ல.",
        tip_en="LG designated UTs: Delhi, Puducherry, A&N Islands, J&K, Ladakh. Administrator designated: Chandigarh, Lakshadweep, DNHDD.",
        tip_ta="துணைநிலை ஆளுநர் உள்ளவை: தில்லி, புதுச்சேரி, அந்தமான், ஜம்மு காஷ்மீர், லடாக். நிர்வாகி உள்ளவை: சண்டிகர், லட்சத்தீவு, DNHDD.",
        fact_en="The President has the power under Article 239 to decide the designation of each administrator.",
        fact_ta="ஒவ்வொரு நிர்வாகியின் பதவிப் பெயரையும் தீர்மானிக்க உறுப்பு 239 குடியரசுத் தலைவருக்கு அதிகாரம் அளிக்கிறது.",
        tags=["polity", "union_territory", "designations", "administrators", "match_the_following"]
    ))

    # MF10: Integration of Princely States
    questions.append(make_ut_q(
        qid="UT_MF_010", diff="Easy", qtype="Match the following",
        subtopic="Integration of Princely States",
        en_stem="Match List-I (Princely State) with List-II (Mode of Integration into India) and select the correct answer using the codes given below the lists:\nList-I:\n(A) Hyderabad\n(B) Junagadh\n(C) Jammu and Kashmir\n(D) Bhopal\nList-II:\n1. Police Action (Operation Polo)\n2. Plebiscite / Referendum\n3. Instrument of Accession\n4. Merger Agreement signed by Nawab after initial refusal",
        ta_stem="பட்டியல்-I (சுதேச சமஸ்தானம்) உடன் பட்டியல்-II (இந்தியாவுடன் இணைக்கப்பட்ட முறை) பொருத்தி கீழே உள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\n(A) ஹைதராபாத்\n(B) ஜூனாகத்\n(C) ஜம்மு மற்றும் காஷ்மீர்\n(D) போபால்\nபட்டியல்-II:\n1. காவல்துறை நடவடிக்கை (ஆபரேஷன் போலோ)\n2. பொது வாக்கெடுப்பு (Plebiscite)\n3. இணைப்பு ஒப்பந்தம் (Instrument of Accession)\n4. நவாப் ஆரம்பத்தில் மறுத்து பின்னர் கையெழுத்திட்ட இணைப்பு ஒப்பந்தம்",
        en_a="A-1, B-2, C-3, D-4", ta_a="A-1, B-2, C-3, D-4",
        en_b="A-2, B-1, C-3, D-4", ta_b="A-2, B-1, C-3, D-4",
        en_c="A-1, B-3, C-2, D-4", ta_c="A-1, B-3, C-2, D-4",
        en_d="A-3, B-2, C-1, D-4", ta_d="A-3, B-2, C-1, D-4",
        correct_key="A",
        exp_en="Hyderabad was integrated through Police Action / Operation Polo in Sep 1948 (1). Junagadh through Plebiscite in Feb 1948 (2). Jammu and Kashmir through Instrument of Accession on Oct 26, 1947 (3). Bhopal through merger agreement signed by Nawab Hamidullah Khan in 1949 (4). Hence, A-1, B-2, C-3, D-4.",
        exp_ta="ஹைதராபாத்: காவல்துறை நடவடிக்கை / ஆபரேஷன் போலோ (செப் 1948) (1). ஜூனாகத்: பொது வாக்கெடுப்பு (பிப் 1948) (2). ஜம்மு காஷ்மீர்: இணைப்பு ஒப்பந்தம் (அக் 26, 1947) (3). போபால்: 1949-ல் நவாப் கையெழுத்திட்ட இணைப்பு ஒப்பந்தம் (4). எனவே சரியான பொருத்தம் A-1, B-2, C-3, D-4.",
        why_a_en="Exact matching between princely states and their respective modes of integration.",
        why_a_ta="சமஸ்தானங்களுக்கும் அவை இணைக்கப்பட்ட முறைகளுக்கும் இடையிலான துல்லியமான பொருத்தம்.",
        why_b_en="Hyderabad was not integrated through plebiscite; Junagadh was.",
        why_b_ta="ஹைதராபாத் பொது வாக்கெடுப்பு மூலம் இணையவில்லை.",
        why_c_en="Junagadh was plebiscite, not Instrument of Accession.",
        why_c_ta="ஜூனாகத் பொது வாக்கெடுப்பு மூலம் இணைந்தது.",
        why_d_en="Hyderabad was Operation Polo, not Accession.",
        why_d_ta="ஹைதராபாத் ஆபரேஷன் போலோ மூலம் இணைந்தது.",
        tip_en="Sardar Patel and V.P. Menon successfully integrated 552 princely states situated within Indian geographical boundaries.",
        tip_ta="சர்தார் படேலும் வி.பி. மேனனும் இந்திய எல்லைக்குள் இருந்த 552 சுதேச சமஸ்தானங்களை வெற்றிகரமாக இணைத்தனர்.",
        fact_en="Only 3 states initially hesitated: Hyderabad, Junagadh, and Kashmir.",
        fact_ta="தொடக்கத்தில் இணைய மறுத்த மூன்று சமஸ்தானங்கள்: ஹைதராபாத், ஜூனாகத் மற்றும் காஷ்மீர்.",
        tags=["polity", "union_territory", "princely_states", "integration", "match_the_following"]
    ))

    # MF11: States Created in 2000 from Parent States
    questions.append(make_ut_q(
        qid="UT_MF_011", diff="Easy", qtype="Match the following",
        subtopic="Linguistic Reorganisation and Evolution of States",
        en_stem="Match List-I (New State Created in 2000) with List-II (Parent State Bifurcated) and select the correct answer using the codes given below the lists:\nList-I:\n(A) Chhattisgarh\n(B) Uttarakhand (Uttaranchal)\n(C) Jharkhand\n(D) Telangana (Created 2014)\nList-II:\n1. Madhya Pradesh\n2. Uttar Pradesh\n3. Bihar\n4. Andhra Pradesh",
        ta_stem="பட்டியல்-I (புதிய மாநிலம்) உடன் பட்டியல்-II (பிரிக்கப்பட்ட தாய் மாநிலம்) பொருத்தி கீழே உள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\n(A) சத்தீஸ்கர் (2000)\n(B) உத்தராகண்ட் (2000)\n(C) ஜார்க்கண்ட் (2000)\n(D) தெலுங்கானா (2014)\nபட்டியல்-II:\n1. மத்தியப் பிரதேசம்\n2. உத்தரப் பிரதேசம்\n3. பீகார்\n4. ஆந்திரப் பிரதேசம்",
        en_a="A-1, B-2, C-3, D-4", ta_a="A-1, B-2, C-3, D-4",
        en_b="A-2, B-1, C-3, D-4", ta_b="A-2, B-1, C-3, D-4",
        en_c="A-1, B-3, C-2, D-4", ta_c="A-1, B-3, C-2, D-4",
        en_d="A-3, B-2, C-1, D-4", ta_d="A-3, B-2, C-1, D-4",
        correct_key="A",
        exp_en="Chhattisgarh was carved out of Madhya Pradesh (1). Uttarakhand was carved out of Uttar Pradesh (2). Jharkhand was carved out of Bihar (3). Telangana was carved out of Andhra Pradesh in 2014 (4). Hence, A-1, B-2, C-3, D-4.",
        exp_ta="சத்தீஸ்கர்: மத்தியப் பிரதேசத்திலிருந்து பிரிக்கப்பட்டது (1). உத்தராகண்ட்: உத்தரப் பிரதேசத்திலிருந்து பிரிக்கப்பட்டது (2). ஜார்க்கண்ட்: பீகாரிலிருந்து பிரிக்கப்பட்டது (3). தெலுங்கானா: ஆந்திரப் பிரதேசத்திலிருந்து 2014-ல் பிரிக்கப்பட்டது (4). எனவே சரியான பொருத்தம் A-1, B-2, C-3, D-4.",
        why_a_en="Exact matching between newly created states and their respective parent states.",
        why_a_ta="புதிய மாநிலங்களுக்கும் அவற்றின் தாய் மாநிலங்களுக்கும் இடையிலான துல்லியமான பொருத்தம்.",
        why_b_en="Chhattisgarh is from MP, not UP.",
        why_b_ta="சத்தீஸ்கர் மத்தியப் பிரதேசத்திலிருந்து உருவானது.",
        why_c_en="Uttarakhand is from UP, not Bihar.",
        why_c_ta="உத்தராகண்ட் உ.பி-யிலிருந்து உருவானது.",
        why_d_en="Jharkhand is from Bihar, not MP.",
        why_d_ta="ஜார்க்கண்ட் பீகாரிலிருந்து உருவானது.",
        tip_en="Mnemonic: C-U-J from MP-UP-Bihar in Nov 2000 (Dates: Nov 1, Nov 9, Nov 15).",
        tip_ta="நினைவுக்குறி: 2000 நவம்பரில் சத்தீஸ்கர் (ம.பி), உத்தராகண்ட் (உ.பி), ஜார்க்கண்ட் (பீகார்) - தேதிகள்: நவ 1, 9, 15.",
        fact_en="All four states were created under Article 3 through ordinary reorganisation acts passed by simple majority.",
        fact_ta="இந்த நான்கு மாநிலங்களுமே உறுப்பு 3-ன் கீழ் சாதாரண பெரும்பான்மை சட்டங்கள் மூலம் உருவாக்கப்பட்டன.",
        tags=["polity", "union_territory", "2000_states", "parent_states", "match_the_following"]
    ))

    # MF12: Special Provisions Articles (371 series)
    questions.append(make_ut_q(
        qid="UT_MF_012", diff="Hard", qtype="Match the following",
        subtopic="Special Provisions for States (Article 371)",
        en_stem="Match List-I (Article of the Constitution) with List-II (State with Special Provisions) and select the correct answer using the codes given below the lists:\nList-I:\n(A) Article 371\n(B) Article 371A\n(C) Article 371D\n(D) Article 371F\nList-II:\n1. Maharashtra and Gujarat\n2. Nagaland\n3. Andhra Pradesh and Telangana\n4. Sikkim",
        ta_stem="பட்டியல்-I (அரசியலமைப்பு உறுப்பு) உடன் பட்டியல்-II (சிறப்பு விதிகள் கொண்ட மாநிலம்) பொருத்தி கீழே உள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\n(A) உறுப்பு 371\n(B) உறுப்பு 371A\n(C) உறுப்பு 371D\n(D) உறுப்பு 371F\nபட்டியல்-II:\n1. மகாராஷ்டிரா மற்றும் குஜராத்\n2. நாகாலாந்து\n3. ஆந்திரப் பிரதேசம் மற்றும் தெலுங்கானா\n4. சிக்கிம்",
        en_a="A-1, B-2, C-3, D-4", ta_a="A-1, B-2, C-3, D-4",
        en_b="A-2, B-1, C-3, D-4", ta_b="A-2, B-1, C-3, D-4",
        en_c="A-1, B-3, C-2, D-4", ta_c="A-1, B-3, C-2, D-4",
        en_d="A-4, B-2, C-3, D-1", ta_d="A-4, B-2, C-3, D-1",
        correct_key="A",
        exp_en="Article 371 provides special provisions for Maharashtra and Gujarat (1). Article 371A for Nagaland (2). Article 371D for Andhra Pradesh and Telangana (3). Article 371F for Sikkim (4). Hence, A-1, B-2, C-3, D-4.",
        exp_ta="உறுப்பு 371: மகாராஷ்டிரா மற்றும் குஜராத் (1). உறுப்பு 371A: நாகாலாந்து (2). உறுப்பு 371D: ஆந்திரா மற்றும் தெலுங்கானா (3). உறுப்பு 371F: சிக்கிம் (4). எனவே சரியான பொருத்தம் A-1, B-2, C-3, D-4.",
        why_a_en="Exact match of Article 371 special provisions articles with their respective beneficiary states.",
        why_a_ta="உறுப்பு 371 தொடரின் சிறப்புப் பிரிவுகளுக்கான சரியான மாநிலப் பொருத்தம்.",
        why_b_en="Article 371 is Maharashtra/Gujarat, not Nagaland.",
        why_b_ta="உறுப்பு 371 மகாராஷ்டிரா/குஜராத்திற்கு உரியது.",
        why_c_en="Article 371A is Nagaland, not Andhra Pradesh.",
        why_c_ta="உறுப்பு 371A நாகாலாந்திற்கு உரியது.",
        why_d_en="Article 371 is not Sikkim.",
        why_d_ta="உறுப்பு 371 சிக்கிம் அல்ல.",
        tip_en="Article 371 sequence: 371 (Maha/Guj), 371A (Nagaland), 371B (Assam), 371C (Manipur), 371D (AP/Telangana), 371F (Sikkim), 371G (Mizoram), 371H (Arunachal), 371-I (Goa), 371J (Karnataka).",
        tip_ta="உறுப்பு 371 வரிசை: 371 (மகா/குஜ்), 371A (நாகாலாந்து), 371B (அசாம்), 371C (மணிப்பூர்), 371D (ஆந்திரா), 371F (சிக்கிம்), 371J (கர்நாடகா).",
        fact_en="These articles are contained in Part XXI (Temporary, Transitional and Special Provisions).",
        fact_ta="இப்பிரிவுகள் அரசியலமைப்பின் பகுதி XXI-ல் (தற்காலிக, இடைக்கால மற்றும் சிறப்பு விதிகள்) இடம்பெற்றுள்ளன.",
        tags=["polity", "union_territory", "article_371", "special_provisions", "match_the_following"]
    ))

    # MF13: Leaders and State Reorganisation Milestones
    questions.append(make_ut_q(
        qid="UT_MF_013", diff="Medium", qtype="Match the following",
        subtopic="Linguistic Reorganisation and Evolution of States",
        en_stem="Match List-I (Leader / Personality) with List-II (Historic Contribution / Movement) and select the correct answer using the codes given below the lists:\nList-I:\n(A) Potti Sriramulu\n(B) Sankaralinganar\n(C) Master Tara Singh\n(D) Sardar Vallabhbhai Patel\nList-II:\n1. 56-day hunger strike for separate Andhra State (1952)\n2. 76-day hunger strike for renaming Madras to Tamil Nadu (1956)\n3. Leadership of the Punjabi Suba movement for Punjabi-speaking state\n4. Integration of 552 Princely States into the Indian Union",
        ta_stem="பட்டியல்-I (தலைவர் / ஆளுமை) உடன் பட்டியல்-II (வரலாற்றுப் பங்களிப்பு / இயக்கம்) பொருத்தி கீழே உள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\n(A) பொட்டி ஸ்ரீராமுலு\n(B) சங்கரலிங்கனார்\n(C) மாஸ்டர் தாரா சிங்\n(D) சர்தார் வல்லபாய் படேல்\nபட்டியல்-II:\n1. தனி ஆந்திர மாநிலத்திற்காக 56 நாட்கள் உண்ணாவிரதம் (1952)\n2. மெட்ராஸ் மாநிலத்தை தமிழ்நாடு என மாற்ற 76 நாட்கள் உண்ணாவிரதம் (1956)\n3. பஞ்சாபி மொழி மாநிலத்திற்கான பஞ்சாபி சுபா இயக்கத்தின் தலைமை\n4. 552 சுதேச சமஸ்தானங்களை இந்திய ஒன்றியத்துடன் இணைத்தல்",
        en_a="A-1, B-2, C-3, D-4", ta_a="A-1, B-2, C-3, D-4",
        en_b="A-2, B-1, C-3, D-4", ta_b="A-2, B-1, C-3, D-4",
        en_c="A-1, B-3, C-2, D-4", ta_c="A-1, B-3, C-2, D-4",
        en_d="A-4, B-2, C-3, D-1", ta_d="A-4, B-2, C-3, D-1",
        correct_key="A",
        exp_en="Potti Sriramulu undertook 56-day fast for Andhra (1). Sankaralinganar undertook 76-day fast for Tamil Nadu renaming (2). Master Tara Singh led the Punjabi Suba movement (3). Sardar Patel integrated 552 princely states (4). Hence, A-1, B-2, C-3, D-4.",
        exp_ta="பொட்டி ஸ்ரீராமுலு: ஆந்திராவுக்காக 56 நாள் உண்ணாநோன்பு (1). சங்கரலிங்கனார்: தமிழ்நாடு பெயருக்காக 76 நாள் உண்ணாநோன்பு (2). மாஸ்டர் தாரா சிங்: பஞ்சாபி சுபா இயக்கம் (3). சர்தார் படேல்: 552 சமஸ்தானங்கள் இணைப்பு (4). எனவே சரியான பொருத்தம் A-1, B-2, C-3, D-4.",
        why_a_en="Exact match of historical leaders with their monumental contributions to Indian state boundaries.",
        why_a_ta="வரலாற்றுத் தலைவர்களுக்கும் அவர்களின் மறுசீரமைப்புப் பங்களிப்புகளுக்கும் இடையிலான துல்லியமான பொருத்தம்.",
        why_b_en="Sriramulu was Andhra (56 days), Sankaralinganar was TN (76 days).",
        why_b_ta="ஸ்ரீராமுலு 56 நாட்கள் (ஆந்திரா), சங்கரலிங்கனார் 76 நாட்கள் (தமிழ்நாடு).",
        why_c_en="Master Tara Singh led Punjabi Suba, not fasting in TN.",
        why_c_ta="தாரா சிங் பஞ்சாபி சுபா இயக்கத் தலைவர்.",
        why_d_en="Patel was integration of princely states, not Andhra fast.",
        why_d_ta="படேல் சமஸ்தானங்கள் இணைப்பின் சிற்பி.",
        tip_en="Fasting days: Potti Sriramulu = 56 days; Sankaralinganar = 76 days; Jatin Das = 63 days.",
        tip_ta="உண்ணாவிரத நாட்கள்: பொட்டி ஸ்ரீராமுலு = 56 நாட்கள்; சங்கரலிங்கனார் = 76 நாட்கள்; ஜதீன் தாஸ் = 63 நாட்கள்.",
        fact_en="Sardar Patel is known as the 'Bismarck of India' and 'Iron Man of India'.",
        fact_ta="சர்தார் படேல் 'இந்தியாவின் பிஸ்மார்க்' மற்றும் 'இந்தியாவின் இரும்பு மனிதர்' என அழைக்கப்படுகிறார்.",
        tags=["polity", "union_territory", "leaders", "movements", "match_the_following"]
    ))

    # MF14: Landmark Supreme Court Cases
    questions.append(make_ut_q(
        qid="UT_MF_014", diff="Hard", qtype="Match the following",
        subtopic="Article 3: Formation of New States and Alteration of Areas",
        en_stem="Match List-I (Case Law / Supreme Court Ruling) with List-II (Core Constitutional Principle) and select the correct answer using the codes given below the lists:\nList-I:\n(A) Berubari Union Case (1960)\n(B) Supreme Court Ruling (1969)\n(C) Babulal Parate v. State of Bombay (1960)\n(D) Govt. of NCT of Delhi v. Union of India (2018)\nList-II:\n1. Cession of Indian territory requires Constitutional Amendment under Article 368\n2. Settlement of boundary dispute does not require amendment; executive action suffices\n3. Views of State Legislature on Article 3 Bills are not binding on Parliament\n4. Lieutenant Governor of Delhi is bound by the aid and advice of the Council of Ministers except in excluded areas",
        ta_stem="பட்டியல்-I (வழக்கு / உச்சநீதிமன்றத் தீர்ப்பு) உடன் பட்டியல்-II (முக்கிய அரசியலமைப்புக் கோட்பாடு) பொருத்தி கீழே உள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\n(A) பெருபாரி யூனியன் வழக்கு (1960)\n(B) உச்சநீதிமன்றத் தீர்ப்பு (1969)\n(C) பாபுலால் பாரட்டே எதிர் பம்பாய் மாநிலம் (1960)\n(D) டெல்லி அரசு எதிர் இந்திய ஒன்றியம் (2018)\nபட்டியல்-II:\n1. இந்திய நிலப்பகுதியை விட்டுக்கொடுக்க உறுப்பு 368-ன் கீழ் அரசியலமைப்பு திருத்தம் தேவை\n2. எல்லைத் தகராறைத் தீர்க்க திருத்தம் தேவையில்லை; நிர்வாக நடவடிக்கையே போதும்\n3. உறுப்பு 3 மசோதாக்கள் மீதான மாநில சட்டமன்றத்தின் கருத்துக்கள் நாடாளுமன்றத்தைக் கட்டுப்படுத்தாது\n4. விலக்கப்பட்ட துறைகளைத் தவிர மற்றவற்றில் தில்லி துணைநிலை ஆளுநர் அமைச்சரவையின் உதவி மற்றும் ஆலோசனைக்குக் கட்டுப்பட்டவர்",
        en_a="A-1, B-2, C-3, D-4", ta_a="A-1, B-2, C-3, D-4",
        en_b="A-2, B-1, C-3, D-4", ta_b="A-2, B-1, C-3, D-4",
        en_c="A-1, B-3, C-2, D-4", ta_c="A-1, B-3, C-2, D-4",
        en_d="A-4, B-2, C-3, D-1", ta_d="A-4, B-2, C-3, D-1",
        correct_key="A",
        exp_en="Berubari Union (1960): Cession requires Article 368 amendment (1). 1969 Ruling: Boundary settlement by executive action (2). Babulal Parate (1960): State views under Article 3 not binding (3). NCT Delhi (2018): LG bound by aid and advice except in 3 excluded subjects (4). Hence, A-1, B-2, C-3, D-4.",
        exp_ta="பெருபாரி யூனியன் (1960): நிலத்தை விட உறுப்பு 368 திருத்தம் தேவை (1). 1969 தீர்ப்பு: எல்லைத் தகராறுக்கு நிர்வாக நடவடிக்கை போதும் (2). பாபுலால் பாரட்டே (1960): மாநிலத்தின் கருத்து நாடாளுமன்றத்தைக் கட்டுப்படுத்தாது (3). தில்லி அரசு (2018): விலக்கப்பட்ட துறைகளைத் தவிர LG அமைச்சரவை ஆலோசனைக்கு கட்டுப்பட்டவர் (4). எனவே சரியான பொருத்தம் A-1, B-2, C-3, D-4.",
        why_a_en="Exact match of landmark constitutional cases with their held legal doctrines.",
        why_a_ta="வரலாற்றுச் சிறப்புமிக்க உச்சநீதிமன்ற வழக்குகளுக்கும் அவற்றின் தீர்ப்பு கோட்பாடுகளுக்கும் இடையிலான துல்லியமான பொருத்தம்.",
        why_b_en="Berubari is cession (1), not executive boundary settlement (2).",
        why_b_ta="பெருபாரி என்பது நிலத்தை விட்டுக் கொடுப்பது தொடர்பானது.",
        why_c_en="1969 ruling is boundary dispute, not state legislature views.",
        why_c_ta="1969 தீர்ப்பு எல்லைத் தகராறு தொடர்பானது.",
        why_d_en="NCT Delhi is 2018, not Berubari.",
        why_d_ta="டெல்லி வழக்கு 2018-ல் வழங்கப்பட்டது.",
        tip_en="Berubari = Article 368 needed. 1969 = Executive action OK. Babulal = State views advisory.",
        tip_ta="பெருபாரி = உறுப்பு 368 தேவை. 1969 = நிர்வாக நடவடிக்கை போதும். பாபுலால் = மாநில கருத்து ஆலோசனையே.",
        fact_en="Babulal Parate case arose from the bilingual Bombay reorganisation challenge.",
        fact_ta="பாபுலால் பாரட்டே வழக்கு பம்பாய் மறுசீரமைப்பின் போது தொடரப்பட்டது.",
        tags=["polity", "union_territory", "case_laws", "supreme_court", "match_the_following"]
    ))

    # MF15: 1950 Four-fold Classification of States
    questions.append(make_ut_q(
        qid="UT_MF_015", diff="Hard", qtype="Match the following",
        subtopic="Article 1: Name and Territory of the Union",
        en_stem="Match List-I (1950 Constitutional Classification) with List-II (Number and Description of States) and select the correct answer using the codes given below the lists:\nList-I:\n(A) Part A States\n(B) Part B States\n(C) Part C States\n(D) Part D Territories\nList-II:\n1. 9 States (Former British Governors' Provinces)\n2. 9 States (Former Princely States with Legislatures)\n3. 10 States (Former Chief Commissioners' Provinces and small Princely States)\n4. 1 Territory (Andaman and Nicobar Islands)",
        ta_stem="பட்டியல்-I (1950 அரசியலமைப்பு வகைப்பாடு) உடன் பட்டியல்-II (மாநிலங்களின் எண்ணிக்கை மற்றும் விளக்கம்) பொருத்தி கீழே உள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\n(A) பகுதி A மாநிலங்கள்\n(B) பகுதி B மாநிலங்கள்\n(C) பகுதி C மாநிலங்கள்\n(D) பகுதி D பகுதிகள்\nபட்டியல்-II:\n1. 9 மாநிலங்கள் (முன்னாள் பிரிட்டிஷ் ஆளுநர் மாகாணங்கள்)\n2. 9 மாநிலங்கள் (சட்டமன்றங்களைக் கொண்ட முன்னாள் சமஸ்தானங்கள்)\n3. 10 மாநிலங்கள் (முன்னாள் தலைமை ஆணையர் மாகாணங்கள் மற்றும் சிறிய சமஸ்தானங்கள்)\n4. 1 பகுதி (அந்தமான் மற்றும் நிக்கோபார் தீவுகள்)",
        en_a="A-1, B-2, C-3, D-4", ta_a="A-1, B-2, C-3, D-4",
        en_b="A-2, B-1, C-3, D-4", ta_b="A-2, B-1, C-3, D-4",
        en_c="A-1, B-3, C-2, D-4", ta_c="A-1, B-3, C-2, D-4",
        en_d="A-3, B-2, C-1, D-4", ta_d="A-3, B-2, C-1, D-4",
        correct_key="A",
        exp_en="Under the 1950 Constitution: Part A had 9 states (1). Part B had 9 states (2). Part C had 10 states (3). Part D had 1 territory (Andaman and Nicobar) (4). Totaling 29 entities. Hence, A-1, B-2, C-3, D-4.",
        exp_ta="1950 அரசியலமைப்பில்: பகுதி A-ல் 9 மாநிலங்கள் (1). பகுதி B-ல் 9 மாநிலங்கள் (2). பகுதி C-ல் 10 மாநிலங்கள் (3). பகுதி D-ல் 1 பகுதி (அந்தமான் நிக்கோபார்) (4). மொத்தம் 29 பகுதிகள். எனவே சரியான பொருத்தம் A-1, B-2, C-3, D-4.",
        why_a_en="Exact matching for the 1950 original constitutional classification (9 + 9 + 10 + 1 = 29).",
        why_a_ta="1950 அசல் அரசியலமைப்பு வகைப்பாட்டிற்கான துல்லியமான பொருத்தம் (9 + 9 + 10 + 1 = 29).",
        why_b_en="Part A and Part B were both 9 states, but Part A was Governors' provinces.",
        why_b_ta="பகுதி A என்பது ஆளுநர் மாகாணங்களாகும்.",
        why_c_en="Part C had 10 states, not Part B.",
        why_c_ta="பகுதி C-ல் 10 மாநிலங்கள் இருந்தன.",
        why_d_en="Part A was not 10 states.",
        why_d_ta="பகுதி A 10 மாநிலங்கள் அல்ல.",
        tip_en="1950 classification: Part A (9), Part B (9), Part C (10), Part D (1). Total = 29.",
        tip_ta="1950 வகைப்பாடு: பகுதி A (9), பகுதி B (9), பகுதி C (10), பகுதி D (1). மொத்தம் = 29.",
        fact_en="The 7th Amendment 1956 replaced all 4 parts with 14 States and 6 UTs.",
        fact_ta="1956-ன் 7-வது திருத்தம் இந்த 4 பிரிவுகளையும் நீக்கி 14 மாநிலங்கள் மற்றும் 6 UTகளை உருவாக்கியது.",
        tags=["polity", "union_territory", "1950_classification", "match_the_following"]
    ))

    # MF16: Union Territories and their Headquarters / Capitals
    questions.append(make_ut_q(
        qid="UT_MF_016", diff="Easy", qtype="Match the following",
        subtopic="Administration of Union Territories",
        en_stem="Match List-I (Union Territory) with List-II (Administrative Capital / Headquarters) and select the correct answer using the codes given below the lists:\nList-I:\n(A) Andaman and Nicobar Islands\n(B) Lakshadweep\n(C) Dadra and Nagar Haveli and Daman and Diu\n(D) Ladakh\nList-II:\n1. Port Blair (Sri Vijaya Puram)\n2. Kavaratti\n3. Daman\n4. Leh",
        ta_stem="பட்டியல்-I (யூனியன் பிரதேசம்) உடன் பட்டியல்-II (நிர்வாகத் தலைநகரம் / தலைமையகம்) பொருத்தி கீழே உள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\n(A) அந்தமான் மற்றும் நிக்கோபார் தீவுகள்\n(B) லட்சத்தீவு\n(C) தாத்ரா மற்றும் நகர் ஹவேலி மற்றும் தாமன் மற்றும் தியூ\n(D) லடாக்\nபட்டியல்-II:\n1. போர்ட் பிளேயர் (ஸ்ரீ விஜய புரம்)\n2. கவரத்தி\n3. தாமன்\n4. லே",
        en_a="A-1, B-2, C-3, D-4", ta_a="A-1, B-2, C-3, D-4",
        en_b="A-2, B-1, C-3, D-4", ta_b="A-2, B-1, C-3, D-4",
        en_c="A-1, B-3, C-2, D-4", ta_c="A-1, B-3, C-2, D-4",
        en_d="A-3, B-2, C-1, D-4", ta_d="A-3, B-2, C-1, D-4",
        correct_key="A",
        exp_en="Andaman & Nicobar headquarters is Port Blair / Sri Vijaya Puram (1). Lakshadweep headquarters is Kavaratti (2). Merged DNHDD headquarters is Daman (3). Ladakh headquarters is Leh (4). Hence, A-1, B-2, C-3, D-4.",
        exp_ta="அந்தமான் நிக்கோபார் தலைமையகம்: போர்ட் பிளேயர் / ஸ்ரீ விஜய புரம் (1). லட்சத்தீவு தலைமையகம்: கவரத்தி (2). இணைக்கப்பட்ட DNHDD தலைமையகம்: தாமன் (3). லடாக் தலைமையகம்: லே (4). எனவே சரியான பொருத்தம் A-1, B-2, C-3, D-4.",
        why_a_en="Exact match between Union Territories and their administrative headquarters.",
        why_a_ta="யூனியன் பிரதேசங்களுக்கும் அவற்றின் தலைநகரங்களுக்கும் இடையிலான துல்லியமான பொருத்தம்.",
        why_b_en="Andaman headquarters is Port Blair, not Kavaratti.",
        why_b_ta="அந்தமான் தலைநகரம் போர்ட் பிளேயர் ஆகும்.",
        why_c_en="Lakshadweep headquarters is Kavaratti, not Daman.",
        why_c_ta="லட்சத்தீவு தலைநகரம் கவரத்தி ஆகும்.",
        why_d_en="Andaman is not Daman.",
        why_d_ta="அந்தமான் தாமன் அல்ல.",
        tip_en="Recently in 2024, Port Blair was officially renamed 'Sri Vijaya Puram'.",
        tip_ta="2024-ல் போர்ட் பிளேயர் அதிகாரப்பூர்வமாக 'ஸ்ரீ விஜய புரம்' என மறுபெயரிடப்பட்டது.",
        fact_en="Kargil serves as the joint capital of Ladakh alongside Leh.",
        fact_ta="லே உடன் இணைந்து கார்கிலும் லடாக்கின் கூட்டுத் தலைநகரமாக செயல்படுகிறது.",
        tags=["polity", "union_territory", "capitals", "headquarters", "match_the_following"]
    ))

    # MF17: Enclaves of Puducherry and Surrounding States
    questions.append(make_ut_q(
        qid="UT_MF_017", diff="Medium", qtype="Match the following",
        subtopic="Article 1: Name and Territory of the Union",
        en_stem="Match List-I (Puducherry Enclave) with List-II (Geographical Coast / Surrounding State) and select the correct answer using the codes given below the lists:\nList-I:\n(A) Puducherry (proper)\n(B) Karaikal\n(C) Mahe\n(D) Yanam\nList-II:\n1. Enclave embedded in Tamil Nadu (Coromandel Coast)\n2. Enclave south of Puducherry in Tamil Nadu (Coromandel Coast)\n3. Enclave on the Arabian Sea / Malabar Coast (surrounded by Kerala)\n4. Enclave on the Bay of Bengal / Godavari delta (surrounded by Andhra Pradesh)",
        ta_stem="பட்டியல்-I (புதுச்சேரி சிற்றெல்லைப் பகுதி) உடன் பட்டியல்-II (புவியியல் கடற்கரை / சூழ்ந்துள்ள மாநிலம்) பொருத்தி கீழே உள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\n(A) புதுச்சேரி\n(B) காரைக்கால்\n(C) மாஹே\n(D) ஏனாம்\nபட்டியல்-II:\n1. தமிழ்நாட்டிற்குள் அமைந்துள்ள பகுதி (கோரமண்டல் கடற்கரை)\n2. தமிழ்நாட்டின் தெற்கே அமைந்துள்ள பகுதி (கோரமண்டல் கடற்கரை)\n3. அரபிக்கடல் / மலபார் கடற்கரைப் பகுதி (கேரளாவால் சூழப்பட்டது)\n4. வங்காள விரிகுடா / கோதாவரி டெல்டா பகுதி (ஆந்திராவால் சூழப்பட்டது)",
        en_a="A-1, B-2, C-3, D-4", ta_a="A-1, B-2, C-3, D-4",
        en_b="A-2, B-1, C-3, D-4", ta_b="A-2, B-1, C-3, D-4",
        en_c="A-1, B-3, C-2, D-4", ta_c="A-1, B-3, C-2, D-4",
        en_d="A-3, B-2, C-1, D-4", ta_d="A-3, B-2, C-1, D-4",
        correct_key="A",
        exp_en="Puducherry and Karaikal are enclaves in Tamil Nadu (1 & 2). Mahe is located on the Malabar coast surrounded by Kerala (3). Yanam is located in the Godavari delta surrounded by Andhra Pradesh (4). Hence, A-1, B-2, C-3, D-4.",
        exp_ta="புதுச்சேரி மற்றும் காரைக்கால் தமிழ்நாட்டில் உள்ளன (1 & 2). மாஹே கேரளாவால் சூழப்பட்ட மலபார் கடற்கரையில் உள்ளது (3). ஏனாம் ஆந்திராவால் சூழப்பட்ட கோதாவரி டெல்டாவில் உள்ளது (4). எனவே சரியான பொருத்தம் A-1, B-2, C-3, D-4.",
        why_a_en="Exact geographical distribution of the four enclaves of UT of Puducherry.",
        why_a_ta="புதுச்சேரி யூனியன் பிரதேசத்தின் நான்கு பகுதிகளுக்கான துல்லியமான புவியியல் இருப்பிடம்.",
        why_b_en="Puducherry and Karaikal are both on Tamil Nadu coast, but correctly ordered in A.",
        why_b_ta="புதுச்சேரி மற்றும் காரைக்கால் இரண்டும் தமிழகக் கடற்கரையில் உள்ளன.",
        why_c_en="Mahe is on Kerala coast, not Yanam.",
        why_c_ta="மாஹே கேரளக் கடற்கரையில் உள்ளது.",
        why_d_en="Puducherry is not Malabar coast.",
        why_d_ta="புதுச்சேரி மலபார் கடற்கரை அல்ல.",
        tip_en="Puducherry enclaves: Puducherry & Karaikal (TN), Mahe (Kerala), Yanam (Andhra Pradesh).",
        tip_ta="புதுச்சேரி பகுதிகள்: புதுச்சேரி & காரைக்கால் (தமிழ்நாடு), மாஹே (கேரளா), ஏனாம் (ஆந்திரா).",
        fact_en="Mahe is the smallest district in India by land area (only 9 sq km).",
        fact_ta="மாஹே பரப்பளவில் இந்தியாவின் மிகச்சிறிய மாவட்டம் ஆகும் (வெறும் 9 சதுர கி.மீ).",
        tags=["polity", "union_territory", "puducherry_enclaves", "geography", "match_the_following"]
    ))

    # MF18: Reorganisation Acts and Years
    questions.append(make_ut_q(
        qid="UT_MF_018", diff="Medium", qtype="Match the following",
        subtopic="Linguistic Reorganisation and Evolution of States",
        en_stem="Match List-I (Reorganisation Act passed by Parliament) with List-II (Year of Enactment) and select the correct answer using the codes given below the lists:\nList-I:\n(A) States Reorganisation Act\n(B) Bombay Reorganisation Act\n(C) Punjab Reorganisation Act\n(D) North-Eastern Areas (Reorganisation) Act\nList-II:\n1. 1956\n2. 1960\n3. 1966\n4. 1971",
        ta_stem="பட்டியல்-I (நாடாளுமன்றம் இயற்றிய மறுசீரமைப்புச் சட்டம்) உடன் பட்டியல்-II (இயற்றப்பட்ட ஆண்டு) பொருத்தி கீழே உள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\n(A) மாநில மறுசீரமைப்புச் சட்டம்\n(B) பம்பாய் மறுசீரமைப்புச் சட்டம்\n(C) பஞ்சாப் மறுசீரமைப்புச் சட்டம்\n(D) வடகிழக்குப் பகுதிகள் (மறுசீரமைப்பு) சட்டம்\nபட்டியல்-II:\n1. 1956\n2. 1960\n3. 1966\n4. 1971",
        en_a="A-1, B-2, C-3, D-4", ta_a="A-1, B-2, C-3, D-4",
        en_b="A-2, B-1, C-3, D-4", ta_b="A-2, B-1, C-3, D-4",
        en_c="A-1, B-3, C-2, D-4", ta_c="A-1, B-3, C-2, D-4",
        en_d="A-4, B-2, C-3, D-1", ta_d="A-4, B-2, C-3, D-1",
        correct_key="A",
        exp_en="States Reorganisation Act was passed in 1956 (1). Bombay Reorganisation Act in 1960 (2). Punjab Reorganisation Act in 1966 (3). North-Eastern Areas Reorganisation Act in 1971 (4). Hence, A-1, B-2, C-3, D-4.",
        exp_ta="மாநில மறுசீரமைப்புச் சட்டம்: 1956 (1). பம்பாய் மறுசீரமைப்புச் சட்டம்: 1960 (2). பஞ்சாப் மறுசீரமைப்புச் சட்டம்: 1966 (3). வடகிழக்குப் பகுதிகள் மறுசீரமைப்புச் சட்டம்: 1971 (4). எனவே சரியான பொருத்தம் A-1, B-2, C-3, D-4.",
        why_a_en="Exact match of Parliamentary reorganisation acts with their enactment years.",
        why_a_ta="நாடாளுமன்ற மறுசீரமைப்புச் சட்டங்களுக்கும் அவற்றின் இயற்றப்பட்ட ஆண்டுகளுக்கும் இடையிலான துல்லியமான பொருத்தம்.",
        why_b_en="States Reorganisation Act was 1956, not 1960.",
        why_b_ta="மாநில மறுசீரமைப்புச் சட்டம் 1956.",
        why_c_en="Punjab was 1966, not 1960.",
        why_c_ta="பஞ்சாப் சட்டம் 1966.",
        why_d_en="States Reorganisation Act is not 1971.",
        why_d_ta="மாநில மறுசீரமைப்புச் சட்டம் 1971 அல்ல.",
        tip_en="All passed under Article 3 & 4 by simple majority.",
        tip_ta="இவை அனைத்தும் உறுப்பு 3 & 4-ன் கீழ் சாதாரண பெரும்பான்மையால் இயற்றப்பட்டன.",
        fact_en="Later reorganisation acts include: MP, UP, and Bihar Reorganisation Acts (2000), AP Reorganisation Act (2014), J&K Reorganisation Act (2019).",
        fact_ta="பிற்கால சட்டங்கள்: ம.பி, உ.பி, பீகார் மறுசீரமைப்பு சட்டங்கள் (2000), ஆந்திர மறுசீரமைப்பு சட்டம் (2014), ஜம்மு காஷ்மீர் மறுசீரமைப்பு சட்டம் (2019).",
        tags=["polity", "union_territory", "acts", "reorganisation", "match_the_following"]
    ))

    # MF19: Legislative Assemblies Strength in UTs
    questions.append(make_ut_q(
        qid="UT_MF_019", diff="Hard", qtype="Match the following",
        subtopic="Administration of Union Territories",
        en_stem="Match List-I (Union Territory) with List-II (Legislative Assembly Structure) and select the correct answer using the codes given below the lists:\nList-I:\n(A) National Capital Territory of Delhi\n(B) Union Territory of Puducherry\n(C) Union Territory of Jammu and Kashmir\n(D) Union Territory of Ladakh\nList-II:\n1. 70 directly elected members (Article 239AA)\n2. 30 elected + 3 nominated members (Article 239A)\n3. 90 elected seats (+ 24 seats kept vacant for PoK)\n4. No Legislative Assembly (governed solely by LG under Article 239)",
        ta_stem="பட்டியல்-I (யூனியன் பிரதேசம்) உடன் பட்டியல்-II (சட்டமன்ற கட்டமைப்பு) பொருத்தி கீழே உள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\n(A) தில்லி தேசிய தலைநகர் பகுதி\n(B) புதுச்சேரி யூனியன் பிரதேசம்\n(C) ஜம்மு காஷ்மீர் யூனியன் பிரதேசம்\n(D) லடாக் யூனியன் பிரதேசம்\nபட்டியல்-II:\n1. நேரடியாக தேர்ந்தெடுக்கப்படும் 70 உறுப்பினர்கள் (உறுப்பு 239AA)\n2. 30 தேர்ந்தெடுக்கப்பட்ட + 3 நியமன உறுப்பினர்கள் (உறுப்பு 239A)\n3. 90 தேர்ந்தெடுக்கப்படும் இடங்கள் (+ பாகிஸ்தான் ஆக்கிரமிப்பு காஷ்மீருக்கு 24 இடங்கள் காலியாக வைக்கப்பட்டுள்ளன)\n4. சட்டப்பேரவை இல்லை (உறுப்பு 239-ன் கீழ் துணைநிலை ஆளுநரால் மட்டுமே நிர்வகிக்கப்படுகிறது)",
        en_a="A-1, B-2, C-3, D-4", ta_a="A-1, B-2, C-3, D-4",
        en_b="A-2, B-1, C-3, D-4", ta_b="A-2, B-1, C-3, D-4",
        en_c="A-1, B-3, C-2, D-4", ta_c="A-1, B-3, C-2, D-4",
        en_d="A-3, B-2, C-1, D-4", ta_d="A-3, B-2, C-1, D-4",
        correct_key="A",
        exp_en="Delhi has 70 elected members (1). Puducherry has 30 elected + 3 nominated (2). J&K has 90 elected seats (+ 24 for PoK) (3). Ladakh has no legislative assembly (4). Hence, A-1, B-2, C-3, D-4.",
        exp_ta="தில்லி: 70 உறுப்பினர்கள் (1). புதுச்சேரி: 30 + 3 நியமன உறுப்பினர்கள் (2). ஜம்மு காஷ்மீர்: 90 இடங்கள் + 24 PoK (3). லடாக்: சட்டப்பேரவை கிடையாது (4). எனவே சரியான பொருத்தம் A-1, B-2, C-3, D-4.",
        why_a_en="Exact match of legislative assembly strengths and structures among the Union Territories.",
        why_a_ta="யூனியன் பிரதேசங்களின் சட்டமன்ற பலம் மற்றும் கட்டமைப்பிற்கான துல்லியமான பொருத்தம்.",
        why_b_en="Delhi has 70, not 30.",
        why_b_ta="தில்லியில் 70 உறுப்பினர்கள் உள்ளனர்.",
        why_c_en="Puducherry has 30 elected, not 90.",
        why_c_ta="புதுச்சேரியில் 30 தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்கள் உள்ளனர்.",
        why_d_en="Delhi is not 90 seats.",
        why_d_ta="தில்லி 90 இடங்கள் அல்ல.",
        tip_en="Only 3 UTs currently have provisions for Legislative Assemblies: Delhi, Puducherry, and Jammu & Kashmir.",
        tip_ta="தற்போது 3 யூனியன் பிரதேசங்களுக்கு மட்டுமே சட்டப்பேரவைக்கான விதிகள் உள்ளன: தில்லி, புதுச்சேரி, ஜம்மு காஷ்மீர்.",
        fact_en="Nominated members in Puducherry have voting rights in assembly proceedings, but cannot vote in Presidential elections.",
        fact_ta="புதுச்சேரி நியமன உறுப்பினர்களுக்கு சட்டப்பேரவையில் வாக்களிக்கும் உரிமை உண்டு, ஆனால் குடியரசுத் தலைவர் தேர்தலில் இல்லை.",
        tags=["polity", "union_territory", "legislative_assemblies", "assembly_seats", "match_the_following"]
    ))

    # MF20: Important Dates in Union & Territory Evolution
    questions.append(make_ut_q(
        qid="UT_MF_020", diff="Medium", qtype="Match the following",
        subtopic="Linguistic Reorganisation and Evolution of States",
        en_stem="Match List-I (Historic Milestone) with List-II (Exact Effective Date) and select the correct answer using the codes given below the lists:\nList-I:\n(A) Inauguration of Andhra State\n(B) States Reorganisation Act took effect\n(C) Bifurcation of Bombay into Maharashtra & Gujarat\n(D) Creation of UTs of J&K and Ladakh\nList-II:\n1. October 1, 1953\n2. November 1, 1956\n3. May 1, 1960\n4. October 31, 2019",
        ta_stem="பட்டியல்-I (வரலாற்று மைல்கல்) உடன் பட்டியல்-II (நடைமுறைக்கு வந்த துல்லியமான தேதி) பொருத்தி கீழே உள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\n(A) ஆந்திர மாநில தொடக்கம்\n(B) மாநில மறுசீரமைப்புச் சட்டம் அமலானது\n(C) பம்பாய் மகாராஷ்டிரா & குஜராத் எனப் பிரிக்கப்பட்டது\n(D) ஜம்மு காஷ்மீர் மற்றும் லடாக் UTக்கள் உருவாக்கம்\nபட்டியல்-II:\n1. அக்டோபர் 1, 1953\n2. நவம்பர் 1, 1956\n3. மே 1, 1960\n4. அக்டோபர் 31, 2019",
        en_a="A-1, B-2, C-3, D-4", ta_a="A-1, B-2, C-3, D-4",
        en_b="A-2, B-1, C-3, D-4", ta_b="A-2, B-1, C-3, D-4",
        en_c="A-1, B-3, C-2, D-4", ta_c="A-1, B-3, C-2, D-4",
        en_d="A-4, B-2, C-3, D-1", ta_d="A-4, B-2, C-3, D-1",
        correct_key="A",
        exp_en="Andhra State was inaugurated on Oct 1, 1953 (1). States Reorganisation took effect on Nov 1, 1956 (2). Bombay bifurcated on May 1, 1960 (3). J&K and Ladakh UTs formed on Oct 31, 2019 (4). Hence, A-1, B-2, C-3, D-4.",
        exp_ta="ஆந்திர மாநிலம்: அக்டோபர் 1, 1953 (1). மாநில மறுசீரமைப்பு: நவம்பர் 1, 1956 (2). பம்பாய் பிரிவினை: மே 1, 1960 (3). ஜம்மு காஷ்மீர் & லடாக்: அக்டோபர் 31, 2019 (4). எனவே சரியான பொருத்தம் A-1, B-2, C-3, D-4.",
        why_a_en="Exact chronological dates match the milestones in Indian political evolution.",
        why_a_ta="இந்திய அரசியல் எல்லை பரிணாம வளர்ச்சியின் வரலாற்றுத் தேதிகளுக்கான துல்லியமான பொருத்தம்.",
        why_b_en="Andhra was Oct 1, 1953, not Nov 1, 1956.",
        why_b_ta="ஆந்திரா அக்டோபர் 1, 1953.",
        why_c_en="Bombay bifurcation was May 1, 1960.",
        why_c_ta="பம்பாய் பிரிவினை மே 1, 1960.",
        why_d_en="Andhra is not 2019.",
        why_d_ta="ஆந்திரா 2019 அல்ல.",
        tip_en="Key milestone dates: Oct 1, 1953 (Andhra); Nov 1, 1956 (SRC); May 1, 1960 (Maha/Guj); Oct 31, 2019 (J&K UTs); Jan 26, 2020 (DNHDD merger).",
        tip_ta="முக்கிய தேதிகள்: அக் 1, 1953 (ஆந்திரா); நவ 1, 1956 (SRC); மே 1, 1960 (பம்பாய்); அக் 31, 2019 (J&K UTக்கள்); ஜன 26, 2020 (DNHDD இணைப்பு).",
        fact_en="October 31 is celebrated as Rashtriya Ekta Diwas (National Unity Day) honoring Sardar Patel.",
        fact_ta="அக்டோபர் 31 சர்தார் படேலை கௌரவிக்கும் தேசிய ஒற்றுமை தினமாகக் கொண்டாடப்படுகிறது.",
        tags=["polity", "union_territory", "dates", "milestones", "match_the_following"]
    ))

    # MF21: Fazl Ali Commission Criteria
    questions.append(make_ut_q(
        qid="UT_MF_021", diff="Hard", qtype="Match the following",
        subtopic="Linguistic Reorganisation and Evolution of States",
        en_stem="Match List-I (Fazl Ali Commission Factor) with List-II (Constitutional / Practical Rationale) and select the correct answer using the codes given below the lists:\nList-I:\n(A) Primary Factor\n(B) Cultural Factor\n(C) Economic Factor\n(D) Administrative Factor\nList-II:\n1. Preservation and strengthening of the unity and security of India\n2. Linguistic and cultural homogeneity\n3. Financial, economic and administrative viability\n4. Successful working of national five-year development plans and people's welfare",
        ta_stem="பட்டியல்-I (பசல் அலி ஆணையக் காரணி) உடன் பட்டியல்-II (அரசியலமைப்பு / நடைமுறை நியாயம்) பொருத்தி கீழே உள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\n(A) முதன்மைக் காரணி\n(B) கலாச்சாரக் காரணி\n(C) பொருளாதாரக் காரணி\n(D) நிர்வாகக் காரணி\nபட்டியல்-II:\n1. இந்தியாவின் ஒற்றுமை மற்றும் பாதுகாப்பைப் பாதுகாத்தல் மற்றும் பலப்படுத்துதல்\n2. மொழி மற்றும் கலாச்சார ஒருமைப்பாடு\n3. நிதி, பொருளாதார மற்றும் நிர்வாக நிலைத்தன்மை\n4. தேசிய ஐந்தாண்டு திட்டங்களின் வெற்றி மற்றும் மக்களின் நலன்",
        en_a="A-1, B-2, C-3, D-4", ta_a="A-1, B-2, C-3, D-4",
        en_b="A-2, B-1, C-3, D-4", ta_b="A-2, B-1, C-3, D-4",
        en_c="A-1, B-3, C-2, D-4", ta_c="A-1, B-3, C-2, D-4",
        en_d="A-3, B-2, C-1, D-4", ta_d="A-3, B-2, C-1, D-4",
        correct_key="A",
        exp_en="The Fazl Ali Commission laid down 4 major criteria: (1) Preservation of unity & security (Primary factor); (2) Linguistic & cultural homogeneity; (3) Financial, economic and administrative viability; (4) Planning and welfare of the nation as a whole. Hence, A-1, B-2, C-3, D-4.",
        exp_ta="பசல் அலி ஆணையம் 4 முக்கிய காரணிகளை வகுத்தது: (1) நாட்டின் ஒற்றுமை மற்றும் பாதுகாப்பு (முதன்மைக் காரணி); (2) மொழி மற்றும் கலாச்சார ஒருமைப்பாடு; (3) நிதி மற்றும் நிர்வாக நிலைத்தன்மை; (4) திட்டமிடல் மற்றும் மக்கள் நலன். எனவே சரியான பொருத்தம் A-1, B-2, C-3, D-4.",
        why_a_en="Exact match of the four major criteria laid down in Chapter II of the Fazl Ali Commission Report (1955).",
        why_a_ta="பசல் அலி ஆணைய அறிக்கையில் குறிப்பிடப்பட்டுள்ள நான்கு காரணிகளுக்கான துல்லியமான பொருத்தம்.",
        why_b_en="Unity and security was the primary factor (1), not linguistic homogeneity.",
        why_b_ta="ஒற்றுமை மற்றும் பாதுகாப்பே முதன்மைக் காரணியாகும்.",
        why_c_en="Economic factor is viability (3).",
        why_c_ta="பொருளாதாரக் காரணி என்பது நிதி நிலைத்தன்மை.",
        why_d_en="Primary factor is not financial viability.",
        why_d_ta="முதன்மைக் காரணி என்பது நிதி நிலைத்தன்மை அல்ல.",
        tip_en="Fazl Ali Commission rejected 'one language, one state' and emphasized national unity above language.",
        tip_ta="பசல் அலி ஆணையம் 'ஒரு மொழி ஒரு மாநிலம்' என்பதை நிராகரித்து, மொழிக்கு மேலாக தேசிய ஒற்றுமையை வலியுறுத்தியது.",
        fact_en="The Commission submitted its comprehensive 267-page report on September 30, 1955.",
        fact_ta="ஆணையம் தனது 267 பக்க விரிவான அறிக்கையை செப்டம்பர் 30, 1955 அன்று சமர்ப்பித்தது.",
        tags=["polity", "union_territory", "fazl_ali_criteria", "match_the_following"]
    ))

    # MF22: Delhi State List Excluded Entries
    questions.append(make_ut_q(
        qid="UT_MF_022", diff="Hard", qtype="Match the following",
        subtopic="Special Provisions for Delhi (Article 239AA)",
        en_stem="Match List-I (Excluded State List Entry for Delhi) with List-II (Subject Description) and select the correct answer using the codes given below the lists:\nList-I:\n(A) State List Entry 1\n(B) State List Entry 2\n(C) State List Entry 18\n(D) State List Entry 64, 65, 66 (insofar as they relate to Entries 1, 2, 18)\nList-II:\n1. Public Order\n2. Police\n3. Land (rights in or over land, land tenures, etc.)\n4. Offences, jurisdiction of courts, and fees with respect to Public Order, Police, and Land",
        ta_stem="பட்டியல்-I (டெல்லிக்கு விலக்கப்பட்ட மாநிலப் பட்டியல் பதிவு) உடன் பட்டியல்-II (விவகார விளக்கம்) பொருத்தி கீழே உள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\n(A) மாநிலப் பட்டியல் பதிவு 1\n(B) மாநிலப் பட்டியல் பதிவு 2\n(C) மாநிலப் பட்டியல் பதிவு 18\n(D) மாநிலப் பட்டியல் பதிவுகள் 64, 65, 66 (பதிவுகள் 1, 2, 18 தொடர்பானவை)\nபட்டியல்-II:\n1. பொது ஒழுங்கு (Public Order)\n2. காவல்துறை (Police)\n3. நிலம் (நிலத்தின் மீதான உரிமைகள், குத்தகை போன்றவை)\n4. பொது ஒழுங்கு, காவல்துறை மற்றும் நிலம் தொடர்பான குற்றங்கள், நீதிமன்ற அதிகார வரம்பு மற்றும் கட்டணங்கள்",
        en_a="A-1, B-2, C-3, D-4", ta_a="A-1, B-2, C-3, D-4",
        en_b="A-2, B-1, C-3, D-4", ta_b="A-2, B-1, C-3, D-4",
        en_c="A-1, B-3, C-2, D-4", ta_c="A-1, B-3, C-2, D-4",
        en_d="A-3, B-2, C-1, D-4", ta_d="A-3, B-2, C-1, D-4",
        correct_key="A",
        exp_en="Under Article 239AA(3)(a), Delhi Assembly cannot legislate on: Entry 1 = Public Order (1); Entry 2 = Police (2); Entry 18 = Land (3); and incidental entries 64, 65, 66 relating to them (4). Hence, A-1, B-2, C-3, D-4.",
        exp_ta="உறுப்பு 239AA(3)(a)-ன் படி, தில்லி சட்டப்பேரவை சட்டமியற்ற முடியாதவை: பதிவு 1 = பொது ஒழுங்கு (1); பதிவு 2 = காவல்துறை (2); பதிவு 18 = நிலம் (3); மற்றும் அவற்றோடு தொடர்புடைய பதிவுகள் 64, 65, 66 (4). எனவே சரியான பொருத்தம் A-1, B-2, C-3, D-4.",
        why_a_en="Exact constitutional matching with the 7th Schedule State List entries excluded under Article 239AA.",
        why_a_ta="உறுப்பு 239AA-ல் விலக்கப்பட்ட 7-வது அட்டவணை மாநிலப் பட்டியல் பதிவுகளுக்கான துல்லியமான பொருத்தம்.",
        why_b_en="Entry 1 is Public Order, Entry 2 is Police.",
        why_b_ta="பதிவு 1 என்பது பொது ஒழுங்கு, பதிவு 2 என்பது காவல்துறை.",
        why_c_en="Entry 2 is Police, not Land.",
        why_c_ta="பதிவு 2 என்பது காவல்துறை.",
        why_d_en="Entry 1 is not Land.",
        why_d_ta="பதிவு 1 நிலம் அல்ல.",
        tip_en="Mnemonic: POL - Public Order (1), Police (2), Land (18).",
        tip_ta="நினைவுக்குறி: பொது ஒழுங்கு (1), காவல்துறை (2), நிலம் (18).",
        fact_en="Services (Entry 41) was a subject of major litigation in 2023, following which Parliament enacted the GNCTD (Amendment) Act, 2023.",
        fact_ta="பணிகள் (பதிவு 41) 2023-ல் பெரும் வழக்காகி, பின்னர் நாடாளுமன்றம் திருத்தச் சட்டம் இயற்றி தன் வசம் எடுத்தது.",
        tags=["polity", "union_territory", "delhi", "state_list_entries", "match_the_following"]
    ))

    # MF23: Major Land Boundary / Territorial Agreements
    questions.append(make_ut_q(
        qid="UT_MF_023", diff="Hard", qtype="Match the following",
        subtopic="Article 1: Name and Territory of the Union",
        en_stem="Match List-I (Treaty / Constitutional Amendment) with List-II (Territorial Settlement) and select the correct answer using the codes given below the lists:\nList-I:\n(A) 9th Constitutional Amendment Act, 1960\n(B) 100th Constitutional Amendment Act, 2015\n(C) Indo-Ceylon Agreement, 1974\n(D) Treaty of Cession, 1956 (ratified 1962)\nList-II:\n1. Transfer of Berubari Union No. 12 to Pakistan\n2. Exchange of 111 Indian and 51 Bangladeshi enclaves\n3. Cession / demarcation of Katchatheevu Island to Sri Lanka\n4. Cession of French establishments of Pondicherry, Karaikal, Mahe, and Yanam to India",
        ta_stem="பட்டியல்-I (ஒப்பந்தம் / அரசியலமைப்பு திருத்தம்) உடன் பட்டியல்-II (நிலப்பரப்பு தீர்வு) பொருத்தி கீழே உள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\n(A) 9-வது அரசியலமைப்பு திருத்தச் சட்டம், 1960\n(B) 100-வது அரசியலமைப்பு திருத்தச் சட்டம், 2015\n(C) இந்திய-இலங்கை ஒப்பந்தம், 1974\n(D) நிலப்பரப்பு ஒப்படைப்பு ஒப்பந்தம், 1956 (1962-ல் ஏற்பளிப்பு)\nபட்டியல்-II:\n1. பெருபாரி யூனியன் எண் 12-ஐ பாகிஸ்தானுக்கு மாற்றுதல்\n2. இந்தியா-வங்கதேசம் இடையே 111 மற்றும் 51 சிற்றெல்லைப் பகுதிகள் பரிமாற்றம்\n3. கச்சத்தீவு தீவை இலங்கைக்கு விட்டுக்கொடுத்தல் / எல்லை நிர்ணயம்\n4. பாண்டிச்சேரி, காரைக்கால், மாஹே, ஏனாம் ஆகிய பிரெஞ்சு பகுதிகளை இந்தியாவிடம் ஒப்படைத்தல்",
        en_a="A-1, B-2, C-3, D-4", ta_a="A-1, B-2, C-3, D-4",
        en_b="A-2, B-1, C-3, D-4", ta_b="A-2, B-1, C-3, D-4",
        en_c="A-1, B-3, C-2, D-4", ta_c="A-1, B-3, C-2, D-4",
        en_d="A-4, B-2, C-3, D-1", ta_d="A-4, B-2, C-3, D-1",
        correct_key="A",
        exp_en="9th CAA 1960 transferred Berubari to Pakistan (1). 100th CAA 2015 exchanged enclaves with Bangladesh (2). 1974 agreement settled boundary including Katchatheevu with Sri Lanka (3). 1956 Treaty transferred French establishments to India (4). Hence, A-1, B-2, C-3, D-4.",
        exp_ta="9-வது திருத்தம் 1960: பெருபாரி பாகிஸ்தானுக்கு மாற்றம் (1). 100-வது திருத்தம் 2015: வங்கதேச எல்லை ஒப்பந்தம் (2). 1974 ஒப்பந்தம்: கச்சத்தீவு இலங்கை வசம் செல்லுதல் (3). 1956 ஒப்பந்தம்: பிரெஞ்சு பகுதிகள் இந்தியாவிடம் ஒப்படைப்பு (4). எனவே சரியான பொருத்தம் A-1, B-2, C-3, D-4.",
        why_a_en="Exact match of international territorial settlements involving India with their corresponding constitutional/treaty instruments.",
        why_a_ta="இந்தியாவின் சர்வதேச நிலப்பரப்பு ஒப்பந்தங்களுக்கும் அவற்றுக்கான திருத்தச் சட்டங்களுக்கும் இடையிலான துல்லியமான பொருத்தம்.",
        why_b_en="9th CAA was Berubari, not Bangladesh enclaves.",
        why_b_ta="9-வது திருத்தம் பெருபாரி தொடர்பானது.",
        why_c_en="100th CAA was Bangladesh, not Katchatheevu.",
        why_c_ta="100-வது திருத்தம் வங்கதேசம் தொடர்பானது.",
        why_d_en="French treaty was Puducherry, not Berubari.",
        why_d_ta="பிரெஞ்சு ஒப்பந்தம் புதுச்சேரி தொடர்பானது.",
        tip_en="Territorial adjustments: 9th CAA (1960, Berubari), 100th CAA (2015, Bangladesh).",
        tip_ta="நிலப்பரப்பு திருத்தங்கள்: 9-வது திருத்தம் (1960, பெருபாரி), 100-வது திருத்தம் (2015, வங்கதேசம்).",
        fact_en="Under the 100th CAA 2015, India transferred 111 enclaves to Bangladesh and received 51 enclaves from Bangladesh.",
        fact_ta="100-வது திருத்தம் 2015-ன் கீழ், இந்தியா 111 பகுதிகளை வங்கதேசத்திற்கு அளித்து 51 பகுதிகளைப் பெற்றது.",
        tags=["polity", "union_territory", "treaties", "boundaries", "match_the_following"]
    ))

    # MF24: Procedural Requirements under Articles 2, 3, 4, 368
    questions.append(make_ut_q(
        qid="UT_MF_024", diff="Hard", qtype="Match the following",
        subtopic="Article 4: Laws under Articles 2 and 3",
        en_stem="Match List-I (Type of Territorial Action) with List-II (Required Constitutional Procedure) and select the correct answer using the codes given below the lists:\nList-I:\n(A) Formation of a new State from existing states\n(B) Admission of a foreign territory as a new State\n(C) Cession of Indian territory to a foreign country\n(D) Renaming an existing State\nList-II:\n1. Article 3 (Prior Presidential recommendation + Simple majority in Parliament)\n2. Article 2 (Simple majority in Parliament under Article 4)\n3. Article 368 (Special majority in Parliament + Constitutional Amendment Act)\n4. Article 3 (Reference to State Legislature for views + Simple majority in Parliament)",
        ta_stem="பட்டியல்-I (நிலப்பரப்பு நடவடிக்கை வகை) உடன் பட்டியல்-II (தேவையான அரசியலமைப்பு நடைமுறை) பொருத்தி கீழே உள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\n(A) தற்போதுள்ள மாநிலங்களிலிருந்து புதிய மாநிலத்தை உருவாக்குதல்\n(B) வெளிநாட்டுப் பகுதியை புதிய மாநிலமாக சேர்த்தல்\n(C) இந்திய நிலப்பகுதியை அயல்நாட்டுக்கு விட்டுக் கொடுத்தல்\n(D) தற்போதுள்ள ஒரு மாநிலத்தின் பெயரை மாற்றுதல்\nபட்டியல்-II:\n1. உறுப்பு 3 (குடியரசுத் தலைவரின் முன் பரிந்துரை + நாடாளுமன்றத்தில் சாதாரண பெரும்பான்மை)\n2. உறுப்பு 2 (உறுப்பு 4-ன் கீழ் நாடாளுமன்றத்தில் சாதாரண பெரும்பான்மை)\n3. உறுப்பு 368 (நாடாளுமன்ற சிறப்பு பெரும்பான்மை + அரசியலமைப்பு திருத்தச் சட்டம்)\n4. உறுப்பு 3 (மாநில சட்டமன்றத்தின் கருத்து கேட்பு + நாடாளுமன்றத்தில் சாதாரண பெரும்பான்மை)",
        en_a="A-1, B-2, C-3, D-4", ta_a="A-1, B-2, C-3, D-4",
        en_b="A-2, B-1, C-3, D-4", ta_b="A-2, B-1, C-3, D-4",
        en_c="A-1, B-3, C-2, D-4", ta_c="A-1, B-3, C-2, D-4",
        en_d="A-3, B-2, C-1, D-4", ta_d="A-3, B-2, C-1, D-4",
        correct_key="A",
        exp_en="Formation of new states: Article 3 with Presidential recommendation & simple majority (1). Admission of foreign territory: Article 2 by simple majority (2). Cession of territory: Article 368 special majority (3). Renaming a state: Article 3 with state reference & simple majority (4). Hence, A-1, B-2, C-3, D-4.",
        exp_ta="புதிய மாநிலம் உருவாக்குதல்: உறுப்பு 3 முன் பரிந்துரை & சாதாரண பெரும்பான்மை (1). வெளிப்பகுதி ஏற்பு: உறுப்பு 2 சாதாரண பெரும்பான்மை (2). நிலத்தை விட்டுக் கொடுத்தல்: உறுப்பு 368 சிறப்பு பெரும்பான்மை (3). பெயர் மாற்றம்: உறுப்பு 3 கருத்து கேட்பு & சாதாரண பெரும்பான்மை (4). எனவே சரியான பொருத்தம் A-1, B-2, C-3, D-4.",
        why_a_en="Exact constitutional procedures mapped to each respective territorial reorganisation action.",
        why_a_ta="ஒவ்வொரு நிலப்பரப்பு நடவடிக்கைக்குமான சரியான அரசியலமைப்பு நடைமுறைகளின் பொருத்தம்.",
        why_b_en="Formation of new states is Article 3, not Article 2.",
        why_b_ta="புதிய மாநில உருவாக்கம் உறுப்பு 3.",
        why_c_en="Cession requires Article 368, not simple majority.",
        why_c_ta="நிலத்தை விட உறுப்பு 368 திருத்தம் தேவை.",
        why_d_en="Article 3 is not special majority.",
        why_d_ta="உறுப்பு 3-க்கு சிறப்பு பெரும்பான்மை தேவையில்லை.",
        tip_en="All internal reorganisations need ONLY simple majority. Only cession to foreign country needs Article 368 special majority.",
        tip_ta="அனைத்து உள்நாட்டு மாற்றங்களுக்கும் சாதாரண பெரும்பான்மை மட்டுமே போதும். வெளிநாட்டுக்கு விட்டுக் கொடுக்க மட்டுமே உறுப்பு 368 சிறப்பு பெரும்பான்மை தேவை.",
        fact_en="Article 4 explicitly shields internal reorganisation laws from Article 368 scrutiny.",
        fact_ta="உறுப்பு 4 உள்நாட்டு மறுசீரமைப்புச் சட்டங்களை உறுப்பு 368-லிருந்து வெளிப்படையாகப் பாதுகாக்கிறது.",
        tags=["polity", "union_territory", "procedures", "article_4", "match_the_following"]
    ))

    # MF25: States Reorganisation Evolution Key Numbers
    questions.append(make_ut_q(
        qid="UT_MF_025", diff="Easy", qtype="Match the following",
        subtopic="Article 1: Name and Territory of the Union",
        en_stem="Match List-I (Historical Epoch / Event) with List-II (Number of States and Union Territories) and select the correct answer using the codes given below the lists:\nList-I:\n(A) Original Constitution (1950)\n(B) States Reorganisation Act (1956)\n(C) Just after Telangana formation (June 2014)\n(D) Present Day (2024 / after Jan 2020)\nList-II:\n1. 29 States/Territories in 4 Parts (A, B, C, D)\n2. 14 States and 6 Union Territories\n3. 29 States and 7 Union Territories\n4. 28 States and 8 Union Territories",
        ta_stem="பட்டியல்-I (வரலாற்றுக் காலகட்டம் / நிகழ்வு) உடன் பட்டியல்-II (மாநிலங்கள் மற்றும் யூனியன் பிரதேசங்களின் எண்ணிக்கை) பொருத்தி கீழே உள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\n(A) அசல் அரசியலமைப்பு (1950)\n(B) மாநில மறுசீரமைப்புச் சட்டம் (1956)\n(C) தெலுங்கானா உருவான உடனடி நிலை (ஜூன் 2014)\n(D) தற்போதைய நிலை (2024 / ஜனவரி 2020-க்குப் பின்)\nபட்டியல்-II:\n1. 4 பிரிவுகளில் 29 மாநிலங்கள்/பகுதிகள் (A, B, C, D)\n2. 14 மாநிலங்கள் மற்றும் 6 யூனியன் பிரதேசங்கள்\n3. 29 மாநிலங்கள் மற்றும் 7 யூனியன் பிரதேசங்கள்\n4. 28 மாநிலங்கள் மற்றும் 8 யூனியன் பிரதேசங்கள்",
        en_a="A-1, B-2, C-3, D-4", ta_a="A-1, B-2, C-3, D-4",
        en_b="A-2, B-1, C-3, D-4", ta_b="A-2, B-1, C-3, D-4",
        en_c="A-1, B-3, C-2, D-4", ta_c="A-1, B-3, C-2, D-4",
        en_d="A-4, B-2, C-3, D-1", ta_d="A-4, B-2, C-3, D-1",
        correct_key="A",
        exp_en="1950 had 29 states in 4 parts (1). 1956 had 14 States and 6 UTs (2). June 2014 had 29 States and 7 UTs (3). Today (after 2019 J&K reorganisation and 2020 DNHDD merger), India has 28 States and 8 UTs (4). Hence, A-1, B-2, C-3, D-4.",
        exp_ta="1950: 4 பிரிவுகளில் 29 மாநிலங்கள் (1). 1956: 14 மாநிலங்கள் மற்றும் 6 UTக்கள் (2). ஜூன் 2014: 29 மாநிலங்கள் மற்றும் 7 UTக்கள் (3). தற்போதைய நிலை: 28 மாநிலங்கள் மற்றும் 8 UTக்கள் (4). எனவே சரியான பொருத்தம் A-1, B-2, C-3, D-4.",
        why_a_en="Exact quantitative matching across key evolutionary milestones of the Indian federal map.",
        why_a_ta="இந்தியக் கூட்டாட்சி வரைபடத்தின் முக்கிய மைல்கல்களுக்கான துல்லியமான புள்ளிவிவரப் பொருத்தம்.",
        why_b_en="1950 was 29 states/territories, not 14 states.",
        why_b_ta="1950-ல் 29 மாநிலங்கள்/பகுதிகள் இருந்தன.",
        why_c_en="1956 had 14 states, not 29.",
        why_c_ta="1956-ல் 14 மாநிலங்கள் இருந்தன.",
        why_d_en="Present status is 28 states and 8 UTs.",
        why_d_ta="தற்போதைய நிலை 28 மாநிலங்கள் மற்றும் 8 UTக்கள்.",
        tip_en="Evolution: 1950 (29) -> 1956 (14+6) -> 2014 (29+7) -> Oct 2019 (28+9) -> Jan 2020 to Present (28+8).",
        tip_ta="பரிணாமம்: 1950 (29) -> 1956 (14+6) -> 2014 (29+7) -> அக் 2019 (28+9) -> ஜன 2020 முதல் தற்போது வரை (28+8).",
        fact_en="First Schedule of the Constitution lists all 28 States and 8 Union Territories.",
        fact_ta="அரசியலமைப்பின் முதல் அட்டவணை அனைத்து 28 மாநிலங்களையும் 8 யூனியன் பிரதேசங்களையும் பட்டியலிடுகிறது.",
        tags=["polity", "union_territory", "evolution_numbers", "match_the_following"]
    ))

    return questions

def main():
    questions = get_match_questions()
    print(f"Generated {len(questions)} Match the Following questions.")
    
    for idx, q in enumerate(questions, 1):
        q["id"] = f"UT_MF_{idx:03d}"
        
    balanced = balance_question_keys(questions)
    out_dir = os.path.join("data", "questions", "polity")
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "union_territory_match_the_following.json")
    
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(balanced)} questions to {out_file}")
    
    res = ContentValidator.validate_file(out_file, expected_count=25, expected_prefix="UT_MF_")
    print("\n--- ContentValidator Summary ---")
    print(res.summary())
    if not res.is_valid:
        print("Issues found:")
        for issue in res.issues:
            print(f" - [{issue.severity}] {issue.field}: {issue.message}")
        sys.exit(1)
    else:
        print("\nALL 25 MATCH THE FOLLOWING QUESTIONS VALIDATED PERFECTLY! (PASS)")

if __name__ == "__main__":
    main()
