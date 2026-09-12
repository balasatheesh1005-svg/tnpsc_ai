# -*- coding: utf-8 -*-
"""
Builder for 25 Chronology MCQs on Union & Its Territory (polity_union_territory).
IDs: UT_C_001 to UT_C_025.
Strictly conforms to TNPSC 24-field schema, bilingual parity, audit rules (len(set(opts)) == 4).
"""
import json
import os
import sys
from ut_mcq_helper import make_ut_q, balance_question_keys
from tools.nova_content_engine.validator import ContentValidator

def get_chronology_questions():
    questions = []

    # C01: Early States Formation (1953-1963)
    questions.append(make_ut_q(
        qid="UT_C_001", diff="Medium", qtype="Chronology",
        subtopic="Linguistic Reorganisation and Evolution of States",
        en_stem="Arrange the following Indian States in the correct chronological order of their formation / statehood:\n1. Andhra State\n2. Kerala\n3. Gujarat\n4. Nagaland\nSelect the correct answer using the codes given below:",
        ta_stem="பின்வரும் இந்திய மாநிலங்கள் உருவான / மாநில அந்தஸ்து பெற்ற சரியான காலவரிசையை ஒழுங்கமைக்கவும்:\n1. ஆந்திர மாநிலம்\n2. கேரளா\n3. குஜராத்\n4. நாகாலாந்து\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="1 - 2 - 3 - 4", ta_a="1 - 2 - 3 - 4",
        en_b="2 - 1 - 3 - 4", ta_b="2 - 1 - 3 - 4",
        en_c="1 - 3 - 2 - 4", ta_c="1 - 3 - 2 - 4",
        en_d="3 - 1 - 2 - 4", ta_d="3 - 1 - 2 - 4",
        correct_key="A",
        exp_en="1. Andhra State: October 1, 1953; 2. Kerala: November 1, 1956; 3. Gujarat: May 1, 1960; 4. Nagaland: December 1, 1963. Hence, the correct chronological order is 1 - 2 - 3 - 4.",
        exp_ta="1. ஆந்திர மாநிலம்: அக்டோபர் 1, 1953; 2. கேரளா: நவம்பர் 1, 1956; 3. குஜராத்: மே 1, 1960; 4. நாகாலாந்து: டிசம்பர் 1, 1963. எனவே சரியான காலவரிசை 1 - 2 - 3 - 4 ஆகும்.",
        why_a_en="Exact chronological sequence: Andhra (1953) -> Kerala (1956) -> Gujarat (1960) -> Nagaland (1963).",
        why_a_ta="துல்லியமான காலவரிசை: ஆந்திரா (1953) -> கேரளா (1956) -> குஜராத் (1960) -> நாகாலாந்து (1963).",
        why_b_en="Andhra (1953) was formed before Kerala (1956).",
        why_b_ta="ஆந்திரா 1953-ல் உருவானது, கேரளாவிற்கு (1956) முந்தையது.",
        why_c_en="Kerala (1956) was formed before Gujarat (1960).",
        why_c_ta="கேரளா 1956-ல் உருவானது, குஜராத்திற்கு (1960) முந்தையது.",
        why_d_en="Gujarat was 1960, not first.",
        why_d_ta="குஜராத் 1960.",
        tip_en="Andhra (1953, 1st linguistic) -> Kerala (1956, SRC) -> Gujarat (1960, 15th) -> Nagaland (1963, 16th).",
        tip_ta="ஆந்திரா (1953) -> கேரளா (1956) -> குஜராத் (1960) -> நாகாலாந்து (1963).",
        fact_en="Andhra State merged with Telangana on Nov 1, 1956 to become Andhra Pradesh.",
        fact_ta="1956 நவம்பர் 1 அன்று ஆந்திர மாநிலம் தெலுங்கானாவுடன் இணைந்து ஆந்திரப் பிரதேசம் ஆனது.",
        tags=["polity", "union_territory", "chronology", "states"]
    ))

    # C02: Committees / Commissions (1948-1966)
    questions.append(make_ut_q(
        qid="UT_C_002", diff="Easy", qtype="Chronology",
        subtopic="Linguistic Reorganisation and Evolution of States",
        en_stem="Arrange the following Commissions and Committees on State Reorganisation in the correct chronological order of their appointment:\n1. Dhar Commission\n2. JVP Committee\n3. Fazl Ali Commission (SRC)\n4. Shah Commission\nSelect the correct answer using the codes given below:",
        ta_stem="மாநில மறுசீரமைப்பு தொடர்பான பின்வரும் ஆணையங்கள் மற்றும் குழுக்கள் அமைக்கப்பட்ட சரியான காலவரிசையை ஒழுங்கமைக்கவும்:\n1. தார் ஆணையம்\n2. ஜே.வி.பி குழு\n3. பசல் அலி ஆணையம் (SRC)\n4. ஷா ஆணையம்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="1 - 2 - 3 - 4", ta_a="1 - 2 - 3 - 4",
        en_b="2 - 1 - 3 - 4", ta_b="2 - 1 - 3 - 4",
        en_c="1 - 3 - 2 - 4", ta_c="1 - 3 - 2 - 4",
        en_d="3 - 2 - 1 - 4", ta_d="3 - 2 - 1 - 4",
        correct_key="A",
        exp_en="1. Dhar Commission: June 1948; 2. JVP Committee: December 1948; 3. Fazl Ali Commission: December 1953; 4. Shah Commission: April 1966. Hence, the correct order is 1 - 2 - 3 - 4.",
        exp_ta="1. தார் ஆணையம்: ஜூன் 1948; 2. ஜே.வி.பி குழு: டிசம்பர் 1948; 3. பசல் அலி ஆணையம்: டிசம்பர் 1953; 4. ஷா ஆணையம்: ஏப்ரல் 1966. எனவே சரியான காலவரிசை 1 - 2 - 3 - 4 ஆகும்.",
        why_a_en="Exact chronological sequence: Dhar (Jun 1948) -> JVP (Dec 1948) -> Fazl Ali (Dec 1953) -> Shah (Apr 1966).",
        why_a_ta="துல்லியமான வரிசை: தார் (ஜூன் 1948) -> JVP (டிச 1948) -> பசல் அலி (டிச 1953) -> ஷா (ஏப் 1966).",
        why_b_en="Dhar Commission (June 1948) came before JVP Committee (December 1948).",
        why_b_ta="தார் ஆணையம் JVP குழுவிற்கு முன்பு அமைக்கப்பட்டது.",
        why_c_en="JVP (1948) came before Fazl Ali Commission (1953).",
        why_c_ta="JVP குழு பசல் அலி ஆணையத்திற்கு முன்பு அமைக்கப்பட்டது.",
        why_d_en="Fazl Ali was 1953, not before Dhar.",
        why_d_ta="பசல் அலி 1953.",
        tip_en="Dhar (Jun 1948) -> JVP (Dec 1948) -> Fazl Ali (Dec 1953) -> Shah (Apr 1966).",
        tip_ta="தார் (ஜூன் 1948) -> JVP (டிச 1948) -> பசல் அலி (டிச 1953) -> ஷா (ஏப் 1966).",
        fact_en="Dhar Commission submitted in Dec 1948; JVP in Apr 1949; Fazl Ali in Sep 1955; Shah in May 1966.",
        fact_ta="தார் அறிக்கை டிச 1948; JVP ஏப் 1949; பசல் அலி செப் 1955; ஷா மே 1966.",
        tags=["polity", "union_territory", "chronology", "committees"]
    ))

    # C03: States 1966-1975
    questions.append(make_ut_q(
        qid="UT_C_003", diff="Medium", qtype="Chronology",
        subtopic="Linguistic Reorganisation and Evolution of States",
        en_stem="Arrange the following States in the correct chronological order of achieving full statehood:\n1. Haryana\n2. Himachal Pradesh\n3. Manipur\n4. Sikkim\nSelect the correct answer using the codes given below:",
        ta_stem="முழு மாநில அந்தஸ்து பெற்றதன் அடிப்படையில் பின்வரும் மாநிலங்களை சரியான காலவரிசையில் ஒழுங்கமைக்கவும்:\n1. ஹரியானா\n2. இமாச்சல பிரதேசம்\n3. மணிப்பூர்\n4. சிக்கிம்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="1 - 2 - 3 - 4", ta_a="1 - 2 - 3 - 4",
        en_b="2 - 1 - 3 - 4", ta_b="2 - 1 - 3 - 4",
        en_c="1 - 3 - 2 - 4", ta_c="1 - 3 - 2 - 4",
        en_d="3 - 1 - 2 - 4", ta_d="3 - 1 - 2 - 4",
        correct_key="A",
        exp_en="1. Haryana: November 1, 1966 (17th state); 2. Himachal Pradesh: January 25, 1971 (18th state); 3. Manipur: January 21, 1972 (19th state); 4. Sikkim: May 16, 1975 (22nd state). Hence, 1 - 2 - 3 - 4.",
        exp_ta="1. ஹரியானா: நவம்பர் 1, 1966 (17-வது மாநிலம்); 2. இமாச்சல பிரதேசம்: ஜனவரி 25, 1971 (18-வது மாநிலம்); 3. மணிப்பூர்: ஜனவரி 21, 1972 (19-வது மாநிலம்); 4. சிக்கிம்: மே 16, 1975 (22-வது மாநிலம்). எனவே சரியான வரிசை 1 - 2 - 3 - 4 ஆகும்.",
        why_a_en="Exact chronological statehood: Haryana (1966) -> HP (1971) -> Manipur (1972) -> Sikkim (1975).",
        why_a_ta="துல்லியமான வரிசை: ஹரியானா (1966) -> இமாச்சலம் (1971) -> மணிப்பூர் (1972) -> சிக்கிம் (1975).",
        why_b_en="Haryana (1966) came before Himachal Pradesh (1971).",
        why_b_ta="ஹரியானா இமாச்சலத்திற்கு முந்தையது.",
        why_c_en="HP (1971) was before Manipur (1972).",
        why_c_ta="இமாச்சலம் மணிப்பூருக்கு முந்தையது.",
        why_d_en="Manipur was 1972, not first.",
        why_d_ta="மணிப்பூர் 1972.",
        tip_en="Statehood ranks: 17th Haryana (1966), 18th HP (1971), 19th Manipur (1972), 22nd Sikkim (1975).",
        tip_ta="வரிசை எண்கள்: 17 ஹரியானா (1966), 18 இமாச்சலம் (1971), 19 மணிப்பூர் (1972), 22 சிக்கிம் (1975).",
        fact_en="Tripura and Meghalaya also became states on the same day as Manipur (January 21, 1972).",
        fact_ta="மணிப்பூருடன் ஒரே நாளில் (ஜனவரி 21, 1972) திரிபுராவும் மேகாலயாவும் மாநிலங்களாயின.",
        tags=["polity", "union_territory", "chronology", "statehood"]
    ))

    # C04: States 1975-2000
    questions.append(make_ut_q(
        qid="UT_C_004", diff="Medium", qtype="Chronology",
        subtopic="Linguistic Reorganisation and Evolution of States",
        en_stem="Arrange the following States in the correct chronological order of their creation / statehood:\n1. Sikkim\n2. Mizoram\n3. Goa\n4. Chhattisgarh\nSelect the correct answer using the codes given below:",
        ta_stem="பின்வரும் மாநிலங்கள் உருவான / மாநில அந்தஸ்து பெற்ற சரியான காலவரிசையை ஒழுங்கமைக்கவும்:\n1. சிக்கிம்\n2. மிசோரம்\n3. கோவா\n4. சத்தீஸ்கர்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="1 - 2 - 3 - 4", ta_a="1 - 2 - 3 - 4",
        en_b="2 - 1 - 3 - 4", ta_b="2 - 1 - 3 - 4",
        en_c="1 - 3 - 2 - 4", ta_c="1 - 3 - 2 - 4",
        en_d="3 - 2 - 1 - 4", ta_d="3 - 2 - 1 - 4",
        correct_key="A",
        exp_en="1. Sikkim: May 1975 (22nd state); 2. Mizoram: February 1987 (23rd state); 3. Goa: May 1987 (25th state); 4. Chhattisgarh: November 1, 2000 (26th state). Hence, 1 - 2 - 3 - 4.",
        exp_ta="1. சிக்கிம்: மே 1975 (22-வது மாநிலம்); 2. மிசோரம்: பிப்ரவரி 1987 (23-வது மாநிலம்); 3. கோவா: மே 1987 (25-வது மாநிலம்); 4. சத்தீஸ்கர்: நவம்பர் 1, 2000 (26-வது மாநிலம்). எனவே சரியான காலவரிசை 1 - 2 - 3 - 4 ஆகும்.",
        why_a_en="Exact chronological sequence: Sikkim (1975) -> Mizoram (Feb 1987) -> Goa (May 1987) -> Chhattisgarh (Nov 2000).",
        why_a_ta="துல்லியமான காலவரிசை: சிக்கிம் (1975) -> மிசோரம் (பிப் 1987) -> கோவா (மே 1987) -> சத்தீஸ்கர் (நவ 2000).",
        why_b_en="Sikkim was 1975, before Mizoram (1987).",
        why_b_ta="சிக்கிம் 1975, மிசோரத்திற்கு (1987) முந்தையது.",
        why_c_en="Mizoram (Feb 1987) attained statehood before Goa (May 1987).",
        why_c_ta="மிசோரம் கோவாவிற்கு முந்தையது.",
        why_d_en="Goa was 1987, not first.",
        why_d_ta="கோவா 1987.",
        tip_en="Sikkim (22nd, 1975) -> Mizoram (23rd, 1987) -> Goa (25th, 1987) -> Chhattisgarh (26th, 2000).",
        tip_ta="சிக்கிம் (22) -> மிசோரம் (23) -> கோவா (25) -> சத்தீஸ்கர் (26).",
        fact_en="Arunachal Pradesh became the 24th state on February 20, 1987, alongside Mizoram.",
        fact_ta="அருணாச்சல பிரதேசம் மிசோரத்துடன் இணைந்து 1987 பிப்ரவரி 20 அன்று 24-வது மாநிலமானது.",
        tags=["polity", "union_territory", "chronology", "states"]
    ))

    # C05: Formation of November 2000 States & Telangana
    questions.append(make_ut_q(
        qid="UT_C_005", diff="Easy", qtype="Chronology",
        subtopic="Linguistic Reorganisation and Evolution of States",
        en_stem="Arrange the following 21st-century States in the correct chronological order of their formation:\n1. Chhattisgarh\n2. Uttarakhand (Uttaranchal)\n3. Jharkhand\n4. Telangana\nSelect the correct answer using the codes given below:",
        ta_stem="21-ஆம் நூற்றாண்டில் உருவான பின்வரும் மாநிலங்களை அவை அமைக்கப்பட்ட சரியான காலவரிசையில் ஒழுங்கமைக்கவும்:\n1. சத்தீஸ்கர்\n2. உத்தராகண்ட் (உத்தராஞ்சல்)\n3. ஜார்க்கண்ட்\n4. தெலுங்கானா\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="1 - 2 - 3 - 4", ta_a="1 - 2 - 3 - 4",
        en_b="2 - 1 - 3 - 4", ta_b="2 - 1 - 3 - 4",
        en_c="1 - 3 - 2 - 4", ta_c="1 - 3 - 2 - 4",
        en_d="3 - 1 - 2 - 4", ta_d="3 - 1 - 2 - 4",
        correct_key="A",
        exp_en="1. Chhattisgarh: November 1, 2000 (26th state); 2. Uttarakhand: November 9, 2000 (27th state); 3. Jharkhand: November 15, 2000 (28th state); 4. Telangana: June 2, 2014 (29th state). Hence, 1 - 2 - 3 - 4.",
        exp_ta="1. சத்தீஸ்கர்: நவம்பர் 1, 2000 (26-வது மாநிலம்); 2. உத்தராகண்ட்: நவம்பர் 9, 2000 (27-வது மாநிலம்); 3. ஜார்க்கண்ட்: நவம்பர் 15, 2000 (28-வது மாநிலம்); 4. தெலுங்கானா: ஜூன் 2, 2014 (29-வது மாநிலம்). எனவே சரியான காலவரிசை 1 - 2 - 3 - 4 ஆகும்.",
        why_a_en="Exact chronological dates: Chhattisgarh (Nov 1, 2000) -> Uttarakhand (Nov 9, 2000) -> Jharkhand (Nov 15, 2000) -> Telangana (June 2, 2014).",
        why_a_ta="துல்லியமான தேதிகள்: சத்தீஸ்கர் (நவ 1, 2000) -> உத்தராகண்ட் (நவ 9, 2000) -> ஜார்க்கண்ட் (நவ 15, 2000) -> தெலுங்கானா (ஜூன் 2, 2014).",
        why_b_en="Chhattisgarh was Nov 1, before Uttarakhand (Nov 9).",
        why_b_ta="சத்தீஸ்கர் நவம்பர் 1, உத்தராகண்டிற்கு (நவம்பர் 9) முந்தையது.",
        why_c_en="Uttarakhand was Nov 9, before Jharkhand (Nov 15).",
        why_c_ta="உத்தராகண்ட் நவம்பர் 9, ஜார்க்கண்டிற்கு (நவம்பர் 15) முந்தையது.",
        why_d_en="Jharkhand was Nov 15, not first.",
        why_d_ta="ஜார்க்கண்ட் நவம்பர் 15.",
        tip_en="Mnemonic: C-U-J-T (Nov 1, Nov 9, Nov 15 of 2000, then June 2, 2014).",
        tip_ta="நினைவுக்குறி: சத்தீஸ்கர் (நவ 1), உத்தராகண்ட் (நவ 9), ஜார்க்கண்ட் (நவ 15), தெலுங்கானா (ஜூன் 2, 2014).",
        fact_en="Telangana was the 29th State, but with J&K reorganisation in 2019, India now has 28 states.",
        fact_ta="தெலுங்கானா 29-வது மாநிலமாக உருவானது; ஆனால் 2019-ல் ஜம்மு காஷ்மீர் மாற்றத்திற்குப் பின் இந்தியாவில் இப்போது 28 மாநிலங்கள் உள்ளன.",
        tags=["polity", "union_territory", "chronology", "2000_states", "telangana"]
    ))

    # C06: Integration of Princely / Foreign Territories (1947-1961)
    questions.append(make_ut_q(
        qid="UT_C_006", diff="Hard", qtype="Chronology",
        subtopic="Integration of Princely States",
        en_stem="Arrange the following territorial integrations into India in the correct chronological order:\n1. Accession of Jammu and Kashmir\n2. Junagadh Plebiscite\n3. Police Action in Hyderabad (Operation Polo)\n4. Liberation of Goa, Daman and Diu (Operation Vijay)\nSelect the correct answer using the codes given below:",
        ta_stem="இந்தியாவுடன் நிலப்பகுதிகள் இணைக்கப்பட்ட பின்வரும் நிகழ்வுகளை சரியான காலவரிசையில் ஒழுங்கமைக்கவும்:\n1. ஜம்மு காஷ்மீர் இணைப்பு ஒப்பந்தம்\n2. ஜூனாகத் பொது வாக்கெடுப்பு\n3. ஹைதராபாத்தில் காவல்துறை நடவடிக்கை (ஆபரேஷன் போலோ)\n4. கோவா, தாமன் மற்றும் தியூ விடுதலை (ஆபரேஷன் விஜய்)\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="1 - 2 - 3 - 4", ta_a="1 - 2 - 3 - 4",
        en_b="2 - 1 - 3 - 4", ta_b="2 - 1 - 3 - 4",
        en_c="1 - 3 - 2 - 4", ta_c="1 - 3 - 2 - 4",
        en_d="3 - 1 - 2 - 4", ta_d="3 - 1 - 2 - 4",
        correct_key="A",
        exp_en="1. J&K Accession: October 26, 1947; 2. Junagadh Plebiscite: February 1948; 3. Hyderabad Operation Polo: September 1948; 4. Goa Liberation Operation Vijay: December 1961. Hence, 1 - 2 - 3 - 4.",
        exp_ta="1. ஜம்மு காஷ்மீர் இணைப்பு: அக்டோபர் 26, 1947; 2. ஜூனாகத் வாக்கெடுப்பு: பிப்ரவரி 1948; 3. ஹைதராபாத் ஆபரேஷன் போலோ: செப்டம்பர் 1948; 4. கோவா ஆபரேஷன் விஜய்: டிசம்பர் 1961. எனவே சரியான காலவரிசை 1 - 2 - 3 - 4 ஆகும்.",
        why_a_en="Exact chronological order: Kashmir (Oct 1947) -> Junagadh (Feb 1948) -> Hyderabad (Sep 1948) -> Goa (Dec 1961).",
        why_a_ta="துல்லியமான காலவரிசை: காஷ்மீர் (அக் 1947) -> ஜூனாகத் (பிப் 1948) -> ஹைதராபாத் (செப் 1948) -> கோவா (டிச 1961).",
        why_b_en="Kashmir signed the Instrument of Accession in Oct 1947, before Junagadh plebiscite in Feb 1948.",
        why_b_ta="காஷ்மீர் இணைப்பு அக்டோபர் 1947-ல் நடந்தது.",
        why_c_en="Junagadh plebiscite (Feb 1948) was before Hyderabad action (Sep 1948).",
        why_c_ta="ஜூனாகத் வாக்கெடுப்பு பிப்ரவரி 1948-ல் நடந்தது.",
        why_d_en="Hyderabad was Sep 1948, not first.",
        why_d_ta="ஹைதராபாத் செப்டம்பர் 1948.",
        tip_en="Kashmir (Oct 1947) -> Junagadh (Feb 1948) -> Hyderabad (Sep 1948) -> Goa (Dec 1961).",
        tip_ta="காஷ்மீர் (அக் 1947) -> ஜூனாகத் (பிப் 1948) -> ஹைதராபாத் (செப் 1948) -> கோவா (டிச 1961).",
        fact_en="Hyderabad was the largest princely state in India, ruled by Mir Osman Ali Khan.",
        fact_ta="ஹைதராபாத் சமஸ்தானம் இந்தியாவின் மிகப்பெரிய சமஸ்தானமாக இருந்தது, நிஜாம் மீர் உஸ்மான் அலி கானால் ஆளப்பட்டது.",
        tags=["polity", "union_territory", "chronology", "integration"]
    ))

    # C07: Renaming of States Chronology
    questions.append(make_ut_q(
        qid="UT_C_007", diff="Medium", qtype="Chronology",
        subtopic="Renaming of States and UTs",
        en_stem="Arrange the following renaming of States / Union Territories in the correct chronological order:\n1. United Provinces renamed as Uttar Pradesh\n2. Madras State renamed as Tamil Nadu\n3. Mysore State renamed as Karnataka\n4. Pondicherry renamed as Puducherry\nSelect the correct answer using the codes given below:",
        ta_stem="மாநிலங்கள் / யூனியன் பிரதேசங்களின் பெயர் மாற்றப்பட்ட பின்வரும் நிகழ்வுகளை சரியான காலவரிசையில் ஒழுங்கமைக்கவும்:\n1. ஐக்கிய மாகாணம் உத்தரப் பிரதேசம் எனப் பெயர் மாற்றம்\n2. மெட்ராஸ் மாநிலம் தமிழ்நாடு எனப் பெயர் மாற்றம்\n3. மைசூர் மாநிலம் கர்நாடகா எனப் பெயர் மாற்றம்\n4. பாண்டிச்சேரி புதுச்சேரி எனப் பெயர் மாற்றம்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="1 - 2 - 3 - 4", ta_a="1 - 2 - 3 - 4",
        en_b="2 - 1 - 3 - 4", ta_b="2 - 1 - 3 - 4",
        en_c="1 - 3 - 2 - 4", ta_c="1 - 3 - 2 - 4",
        en_d="3 - 2 - 1 - 4", ta_d="3 - 2 - 1 - 4",
        correct_key="A",
        exp_en="1. Uttar Pradesh: January 1950; 2. Tamil Nadu: January 1969; 3. Karnataka: November 1973; 4. Puducherry: October 2006. Hence, 1 - 2 - 3 - 4.",
        exp_ta="1. உத்தரப் பிரதேசம்: ஜனவரி 1950; 2. தமிழ்நாடு: ஜனவரி 1969; 3. கர்நாடகா: நவம்பர் 1973; 4. புதுச்சேரி: அக்டோபர் 2006. எனவே சரியான காலவரிசை 1 - 2 - 3 - 4 ஆகும்.",
        why_a_en="Exact chronological dates: UP (1950) -> TN (1969) -> Karnataka (1973) -> Puducherry (2006).",
        why_a_ta="துல்லியமான ஆண்டுகள்: உ.பி (1950) -> தமிழ்நாடு (1969) -> கர்நாடகா (1973) -> புதுச்சேரி (2006).",
        why_b_en="UP (1950) was renamed well before Tamil Nadu (1969).",
        why_b_ta="உத்தரப் பிரதேசம் 1950-லேயே மாற்றப்பட்டது.",
        why_c_en="TN (1969) was before Karnataka (1973).",
        why_c_ta="தமிழ்நாடு 1969, கர்நாடகாவிற்கு (1973) முந்தையது.",
        why_d_en="Mysore was 1973, not first.",
        why_d_ta="மைசூர் 1973.",
        tip_en="Renaming: UP (1950) -> TN (1969) -> Karnataka (1973) -> Puducherry (2006) -> Uttarakhand (2007) -> Odisha (2011).",
        tip_ta="பெயர் மாற்றங்கள்: உ.பி (1950) -> தமிழ்நாடு (1969) -> கர்நாடகா (1973) -> புதுச்சேரி (2006) -> உத்தராகண்ட் (2007) -> ஒடிசா (2011).",
        fact_en="All state renaming is done under Article 3 through ordinary parliamentary legislation.",
        fact_ta="அனைத்து மாநிலப் பெயர் மாற்றங்களும் உறுப்பு 3-ன் கீழ் நாடாளுமன்றத்தின் சாதாரண சட்டத்தால் செய்யப்படுகின்றன.",
        tags=["polity", "union_territory", "chronology", "renaming"]
    ))

    # C08: Constitutional Amendments on Union & Territories
    questions.append(make_ut_q(
        qid="UT_C_008", diff="Medium", qtype="Chronology",
        subtopic="Article 2: Admission or Establishment of New States",
        en_stem="Arrange the following Constitutional Amendment Acts in the correct chronological order of their enactment:\n1. 7th Amendment Act (States Reorganisation)\n2. 10th Amendment Act (Dadra and Nagar Haveli)\n3. 12th Amendment Act (Goa, Daman and Diu)\n4. 14th Amendment Act (Puducherry & UT Legislatures)\nSelect the correct answer using the codes given below:",
        ta_stem="அரசியலமைப்புத் திருத்தச் சட்டங்களை அவை இயற்றப்பட்ட சரியான காலவரிசையில் ஒழுங்கமைக்கவும்:\n1. 7-வது திருத்தச் சட்டம் (மாநில மறுசீரமைப்பு)\n2. 10-வது திருத்தச் சட்டம் (தாத்ரா மற்றும் நகர் ஹவேலி)\n3. 12-வது திருத்தச் சட்டம் (கோவா, தாமன் மற்றும் தியூ)\n4. 14-வது திருத்தச் சட்டம் (புதுச்சேரி & UT சட்டமன்றங்கள்)\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="1 - 2 - 3 - 4", ta_a="1 - 2 - 3 - 4",
        en_b="2 - 1 - 3 - 4", ta_b="2 - 1 - 3 - 4",
        en_c="1 - 3 - 2 - 4", ta_c="1 - 3 - 2 - 4",
        en_d="3 - 2 - 1 - 4", ta_d="3 - 2 - 1 - 4",
        correct_key="A",
        exp_en="1. 7th CAA: 1956; 2. 10th CAA: August 1961; 3. 12th CAA: March 1962; 4. 14th CAA: December 1962. Hence, the chronological order is 1 - 2 - 3 - 4.",
        exp_ta="1. 7-வது திருத்தம்: 1956; 2. 10-வது திருத்தம்: ஆகஸ்ட் 1961; 3. 12-வது திருத்தம்: மார்ச் 1962; 4. 14-வது திருத்தம்: டிசம்பர் 1962. எனவே சரியான காலவரிசை 1 - 2 - 3 - 4 ஆகும்.",
        why_a_en="Exact chronological sequence of amendments: 7th (1956) -> 10th (1961) -> 12th (early 1962) -> 14th (late 1962).",
        why_a_ta="துல்லியமான திருத்தச் சட்ட வரிசை: 7-வது (1956) -> 10-வது (1961) -> 12-வது (மார்ச் 1962) -> 14-வது (டிசம்பர் 1962).",
        why_b_en="7th CAA (1956) came before 10th CAA (1961).",
        why_b_ta="7-வது திருத்தம் 1956-ல் வந்தது.",
        why_c_en="10th CAA was 1961, before 12th CAA (1962).",
        why_c_ta="10-வது திருத்தம் 1961.",
        why_d_en="12th CAA was 1962, not first.",
        why_d_ta="12-வது திருத்தம் 1962.",
        tip_en="Amendments: 7th (1956) -> 10th (1961, DNH) -> 12th (1962, Goa) -> 14th (1962, Puducherry).",
        tip_ta="திருத்தங்கள்: 7-வது (1956) -> 10-வது (1961, DNH) -> 12-வது (1962, கோவா) -> 14-வது (1962, புதுச்சேரி).",
        fact_en="14th CAA inserted Article 239A creating legislatures for UTs.",
        fact_ta="14-வது திருத்தம் யூனியன் பிரதேசங்களுக்கு சட்டமன்றங்களை உருவாக்க உறுப்பு 239A-வைச் சேர்த்தது.",
        tags=["polity", "union_territory", "chronology", "amendments"]
    ))

    # C09: Amendments 1966-1991
    questions.append(make_ut_q(
        qid="UT_C_009", diff="Hard", qtype="Chronology",
        subtopic="Special Provisions for Delhi (Article 239AA)",
        en_stem="Arrange the following Constitutional Amendment Acts relating to territory and UTs in correct chronological order:\n1. 18th Amendment Act (Explanation to Article 3)\n2. 35th Amendment Act (Sikkim Associate State)\n3. 36th Amendment Act (Sikkim Full State)\n4. 69th Amendment Act (NCT of Delhi - Article 239AA)\nSelect the correct answer using the codes given below:",
        ta_stem="நிலப்பரப்பு மற்றும் UT-கள் தொடர்பான பின்வரும் அரசியலமைப்பு திருத்தச் சட்டங்களை சரியான காலவரிசையில் ஒழுங்கமைக்கவும்:\n1. 18-வது திருத்தச் சட்டம் (உறுப்பு 3-க்கான விளக்கம்)\n2. 35-வது திருத்தச் சட்டம் (சிக்கிம் இணை மாநிலம்)\n3. 36-வது திருத்தச் சட்டம் (சிக்கிம் முழு மாநிலம்)\n4. 69-வது திருத்தச் சட்டம் (டெல்லி NCT - உறுப்பு 239AA)\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="1 - 2 - 3 - 4", ta_a="1 - 2 - 3 - 4",
        en_b="2 - 1 - 3 - 4", ta_b="2 - 1 - 3 - 4",
        en_c="1 - 3 - 2 - 4", ta_c="1 - 3 - 2 - 4",
        en_d="3 - 2 - 1 - 4", ta_d="3 - 2 - 1 - 4",
        correct_key="A",
        exp_en="1. 18th CAA: 1966; 2. 35th CAA: 1974; 3. 36th CAA: 1975; 4. 69th CAA: 1991. Hence, 1 - 2 - 3 - 4.",
        exp_ta="1. 18-வது திருத்தம்: 1966; 2. 35-வது திருத்தம்: 1974; 3. 36-வது திருத்தம்: 1975; 4. 69-வது திருத்தம்: 1991. எனவே சரியான காலவரிசை 1 - 2 - 3 - 4 ஆகும்.",
        why_a_en="Exact chronological sequence: 18th (1966) -> 35th (1974) -> 36th (1975) -> 69th (1991).",
        why_a_ta="துல்லியமான வரிசை: 18-வது (1966) -> 35-வது (1974) -> 36-வது (1975) -> 69-வது (1991).",
        why_b_en="18th CAA was 1966, before 35th CAA (1974).",
        why_b_ta="18-வது திருத்தம் 1966.",
        why_c_en="35th CAA (1974) came before 36th CAA (1975).",
        why_c_ta="35-வது திருத்தம் 36-வது திருத்தத்திற்கு முந்தையது.",
        why_d_en="36th CAA was 1975, not first.",
        why_d_ta="36-வது திருத்தம் 1975.",
        tip_en="18th (1966) -> 35th (1974) -> 36th (1975) -> 69th (1991).",
        tip_ta="18-வது (1966) -> 35-வது (1974) -> 36-வது (1975) -> 69-வது (1991).",
        fact_en="The 70th CAA (1992) followed the 69th CAA to add Delhi MLAs to Presidential Electoral College.",
        fact_ta="69-வது திருத்தத்தைத் தொடர்ந்து 70-வது திருத்தம் (1992) தில்லி எம்.எல்.ஏ-க்களை குடியரசுத் தலைவர் தேர்தலில் சேர்த்தது.",
        tags=["polity", "union_territory", "chronology", "amendments"]
    ))

    # C10: Judicial Pronouncements Chronology
    questions.append(make_ut_q(
        qid="UT_C_010", diff="Hard", qtype="Chronology",
        subtopic="Article 3: Formation of New States and Alteration of Areas",
        en_stem="Arrange the following landmark Supreme Court judgments on Union and territory in the correct chronological order:\n1. Babulal Parate v. State of Bombay (State views under Art 3 not binding)\n2. Berubari Union Reference (Cession requires Art 368 amendment)\n3. Supreme Court Ruling on Demarcation of International Boundary Disputes\n4. Govt. of NCT of Delhi v. Union of India (LG powers and ministerial advice)\nSelect the correct answer using the codes given below:",
        ta_stem="ஒன்றியம் மற்றும் நிலப்பரப்பு தொடர்பான உச்சநீதிமன்றத்தின் வரலாற்று முக்கியத்துவம் வாய்ந்த தீர்ப்புகளை சரியான காலவரிசையில் ஒழுங்கமைக்கவும்:\n1. பாபுலால் பாரட்டே எதிர் பம்பாய் மாநிலம் (உறுப்பு 3 மாநில கருத்து கட்டுப்படுத்தாது)\n2. பெருபாரி யூனியன் வழக்கு (நிலத்தை விட உறுப்பு 368 திருத்தம் தேவை)\n3. சர்வதேச எல்லை நிர்ணய தகராறுகள் மீதான உச்சநீதிமன்றத் தீர்ப்பு\n4. டெல்லி அரசு எதிர் இந்திய ஒன்றியம் (LG அதிகாரங்கள் மற்றும் அமைச்சரவை ஆலோசனை)\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="1 - 2 - 3 - 4", ta_a="1 - 2 - 3 - 4",
        en_b="2 - 1 - 3 - 4", ta_b="2 - 1 - 3 - 4",
        en_c="1 - 3 - 2 - 4", ta_c="1 - 3 - 2 - 4",
        en_d="3 - 1 - 2 - 4", ta_d="3 - 1 - 2 - 4",
        correct_key="A",
        exp_en="1. Babulal Parate: Decided in early 1960 (Jan 1960); 2. Berubari Union Reference: Decided in March 1960; 3. Boundary Demarcation Ruling: 1969; 4. Govt of NCT of Delhi: July 2018. Hence, 1 - 2 - 3 - 4.",
        exp_ta="1. பாபுலால் பாரட்டே: ஜனவரி 1960; 2. பெருபாரி யூனியன்: மார்ச் 1960; 3. எல்லை நிர்ணயத் தீர்ப்பு: 1969; 4. தில்லி அரசு வழக்கு: ஜூலை 2018. எனவே சரியான காலவரிசை 1 - 2 - 3 - 4 ஆகும்.",
        why_a_en="Exact chronological sequence of landmark judicial rulings: Babulal Parate (Jan 1960) -> Berubari (Mar 1960) -> 1969 Demarcation -> NCT Delhi (2018).",
        why_a_ta="நீதிமன்றத் தீர்ப்புகளின் துல்லியமான காலவரிசை: பாபுலால் பாரட்டே (ஜன 1960) -> பெருபாரி (மார்ச் 1960) -> 1969 எல்லைத் தீர்ப்பு -> தில்லி அரசு (2018).",
        why_b_en="Babulal Parate was decided on Jan 14, 1960, prior to Berubari Reference on Mar 14, 1960.",
        why_b_ta="பாபுலால் பாரட்டே ஜனவரி 14, 1960-ல் வழங்கப்பட்டது.",
        why_c_en="Berubari was 1960, before 1969.",
        why_c_ta="பெருபாரி 1960, 1969-க்கு முந்தையது.",
        why_d_en="1969 ruling was not first.",
        why_d_ta="1969 தீர்ப்பு முதலாவதல்ல.",
        tip_en="1960 pair: Babulal Parate (Jan) & Berubari (Mar) -> 1969 -> 2018.",
        tip_ta="1960 ஜோடி தீர்ப்புகள்: பாபுலால் பாரட்டே & பெருபாரி -> 1969 -> 2018.",
        fact_en="The 2018 NCT Delhi Constitution Bench comprised 5 judges headed by CJI Dipak Misra.",
        fact_ta="2018 தில்லி வழக்கில் தலைமை நீதிபதி தீபக் மிஸ்ரா தலைமையிலான 5 நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வு தீர்ப்பளித்தது.",
        tags=["polity", "union_territory", "chronology", "case_laws"]
    ))

    # C11: North-Eastern States Statehood Chronology
    questions.append(make_ut_q(
        qid="UT_C_011", diff="Medium", qtype="Chronology",
        subtopic="Linguistic Reorganisation and Evolution of States",
        en_stem="Arrange the following North-Eastern States in the correct chronological order of achieving full statehood:\n1. Nagaland\n2. Meghalaya\n3. Sikkim\n4. Arunachal Pradesh\nSelect the correct answer using the codes given below:",
        ta_stem="முழு மாநில அந்தஸ்து பெற்றதன் அடிப்படையில் பின்வரும் வடகிழக்கு மாநிலங்களை சரியான காலவரிசையில் ஒழுங்கமைக்கவும்:\n1. நாகாலாந்து\n2. மேகாலயா\n3. சிக்கிம்\n4. அருணாச்சல பிரதேசம்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="1 - 2 - 3 - 4", ta_a="1 - 2 - 3 - 4",
        en_b="2 - 1 - 3 - 4", ta_b="2 - 1 - 3 - 4",
        en_c="1 - 3 - 2 - 4", ta_c="1 - 3 - 2 - 4",
        en_d="3 - 2 - 1 - 4", ta_d="3 - 2 - 1 - 4",
        correct_key="A",
        exp_en="1. Nagaland: December 1, 1963 (16th state); 2. Meghalaya: January 21, 1972 (21st state); 3. Sikkim: May 16, 1975 (22nd state); 4. Arunachal Pradesh: February 20, 1987 (24th state). Hence, 1 - 2 - 3 - 4.",
        exp_ta="1. நாகாலாந்து: டிசம்பர் 1, 1963 (16-வது மாநிலம்); 2. மேகாலயா: ஜனவரி 21, 1972 (21-வது மாநிலம்); 3. சிக்கிம்: மே 16, 1975 (22-வது மாநிலம்); 4. அருணாச்சல பிரதேசம்: பிப்ரவரி 20, 1987 (24-வது மாநிலம்). எனவே சரியான காலவரிசை 1 - 2 - 3 - 4 ஆகும்.",
        why_a_en="Exact chronological sequence of North-Eastern statehood: Nagaland (1963) -> Meghalaya (1972) -> Sikkim (1975) -> Arunachal (1987).",
        why_a_ta="வடகிழக்கு மாநிலங்களின் துல்லியமான காலவரிசை: நாகாலாந்து (1963) -> மேகாலயா (1972) -> சிக்கிம் (1975) -> அருணாச்சல் (1987).",
        why_b_en="Nagaland was 1963, before Meghalaya (1972).",
        why_b_ta="நாகாலாந்து 1963, மேகாலயாவிற்கு (1972) முந்தையது.",
        why_c_en="Meghalaya was 1972, before Sikkim (1975).",
        why_c_ta="மேகாலயா 1972, சிக்கிமுக்கு (1975) முந்தையது.",
        why_d_en="Sikkim was 1975, not first.",
        why_d_ta="சிக்கிம் 1975.",
        tip_en="North-East statehood: Nagaland (1963) -> MMT (Manipur, Meghalaya, Tripura 1972) -> Sikkim (1975) -> Mizoram & Arunachal (1987).",
        tip_ta="வடகிழக்கு மாநிலங்கள்: நாகாலாந்து (1963) -> மேகாலயா, மணிப்பூர், திரிபுரா (1972) -> சிக்கிம் (1975) -> மிசோரம், அருணாச்சல் (1987).",
        fact_en="Assam was the parent state from which Nagaland, Meghalaya, and Mizoram were carved out.",
        fact_ta="நாகாலாந்து, மேகாலயா, மிசோரம் ஆகியவை அசாமிலிருந்து பிரிக்கப்பட்டு உருவாக்கப்பட்டன.",
        tags=["polity", "union_territory", "chronology", "northeast"]
    ))

    # C12: Steps in Formation of a New State under Article 3
    questions.append(make_ut_q(
        qid="UT_C_012", diff="Hard", qtype="Chronology",
        subtopic="Article 3: Formation of New States and Alteration of Areas",
        en_stem="Arrange the procedural steps for the formation of a new State under Article 3 of the Constitution in correct chronological order:\n1. Prior recommendation of the President obtained for the Bill\n2. Reference of the Bill by the President to the concerned State Legislature for views\n3. Introduction of the Bill in either House of Parliament\n4. Passage of the Bill by simple majority and Presidential assent\nSelect the correct answer using the codes given below:",
        ta_stem="அரசியலமைப்பின் உறுப்பு 3-ன் கீழ் ஒரு புதிய மாநிலத்தை உருவாக்குவதற்கான நடைமுறைப் படிகளை சரியான காலவரிசையில் ஒழுங்கமைக்கவும்:\n1. மசோதாவிற்கு குடியரசுத் தலைவரின் முன் பரிந்துரை பெறுதல்\n2. மசோதாவை குடியரசுத் தலைவர் சம்பந்தப்பட்ட மாநில சட்டமன்றத்தின் கருத்திற்கு அனுப்புதல்\n3. நாடாளுமன்றத்தின் ஏதேனும் ஒரு அவையில் மசோதாவை அறிமுகப்படுத்துதல்\n4. சாதாரண பெரும்பான்மையுடன் மசோதா நிறைவேற்றப்பட்டு குடியரசுத் தலைவரின் ஒப்புதல் பெறுதல்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="2 - 1 - 3 - 4", ta_a="2 - 1 - 3 - 4",
        en_b="1 - 2 - 3 - 4", ta_b="1 - 2 - 3 - 4",
        en_c="2 - 3 - 1 - 4", ta_c="2 - 3 - 1 - 4",
        en_d="3 - 2 - 1 - 4", ta_d="3 - 2 - 1 - 4",
        correct_key="A",
        exp_en="Under the proviso to Article 3, before the President recommends the bill (1), the President must refer the bill to the state legislature for expressing views (2). Once the time expires or views are received, the President gives recommendation (1), the bill is introduced in Parliament (3), and passed by simple majority (4). Hence, the constitutional sequence is 2 - 1 - 3 - 4.",
        exp_ta="உறுப்பு 3-ன் நிபந்தனையின்படி, குடியரசுத் தலைவர் பரிந்துரைப்பதற்கு முன்பு மசோதாவை மாநில சட்டமன்றத்திற்கு அனுப்ப வேண்டும் (2). பின்னர் குடியரசுத் தலைவர் பரிந்துரை அளிக்க (1), நாடாளுமன்றத்தில் அறிமுகப்படுத்தப்பட்டு (3), சாதாரண பெரும்பான்மையால் நிறைவேற்றப்பட்டு ஒப்புதல் பெறப்படுகிறது (4). எனவே சரியான வரிசை 2 - 1 - 3 - 4 ஆகும்.",
        why_a_en="Proviso to Article 3 mandates reference to state legislature BEFORE the President recommends the introduction of the bill.",
        why_a_ta="உறுப்பு 3-ன் நிபந்தனை குடியரசுத் தலைவர் முன் பரிந்துரை செய்வதற்கு முன்பே மாநில சட்டமன்றத்திற்கு அனுப்பப்பட வேண்டும் எனக் கூறுகிறது.",
        why_b_en="Recommendation comes after the state legislature reference under the proviso.",
        why_b_ta="மாநில கருத்தைக் கேட்ட பிறகே முன் பரிந்துரை வழங்கப்படுகிறது.",
        why_c_en="Bill cannot be introduced before President's recommendation.",
        why_c_ta="முன் பரிந்துரை இன்றி அறிமுகப்படுத்த முடியாது.",
        why_d_en="Introduction cannot precede reference.",
        why_d_ta="அறிமுகம் செய்வதற்கு முன்பே அனுப்ப வேண்டும்.",
        tip_en="Article 3 Proviso: '...no Bill... shall be introduced... unless referred by the President to the Legislature... and recommended by President'.",
        tip_ta="உறுப்பு 3 நிபந்தனை: மாநில சட்டமன்றத்திற்கு அனுப்பப்பட்டு, குடியரசுத் தலைவரால் பரிந்துரைக்கப்பட்ட பின்னரே அறிமுகப்படுத்தப்பட வேண்டும்.",
        fact_en="No reference to state legislature is required when reorganisation affects a Union Territory.",
        fact_ta="மறுசீரமைப்பு ஒரு யூனியன் பிரதேசத்தைப் பாதிக்கும் போது சட்டமன்றத்திற்கு அனுப்ப வேண்டிய அவசியமில்லை.",
        tags=["polity", "union_territory", "chronology", "procedure", "article_3"]
    ))

    # C13: Renaming of Recent States / UTs (1973-2011)
    questions.append(make_ut_q(
        qid="UT_C_013", diff="Medium", qtype="Chronology",
        subtopic="Renaming of States and UTs",
        en_stem="Arrange the following renaming of States / UTs in the correct chronological order:\n1. Laccadive, Minicoy and Amindivi Islands renamed as Lakshadweep\n2. Pondicherry renamed as Puducherry\n3. Uttaranchal renamed as Uttarakhand\n4. Orissa renamed as Odisha\nSelect the correct answer using the codes given below:",
        ta_stem="மாநிலங்கள் / யூனியன் பிரதேசங்களின் பெயர் மாற்றப்பட்ட பின்வரும் நிகழ்வுகளை சரியான காலவரிசையில் ஒழுங்கமைக்கவும்:\n1. லட்சத்தீவு, மினிகாய் மற்றும் அமினிதிவி தீவுகள் லட்சத்தீவு எனப் பெயர் மாற்றம்\n2. பாண்டிச்சேரி புதுச்சேரி எனப் பெயர் மாற்றம்\n3. உத்தராஞ்சல் உத்தராகண்ட் எனப் பெயர் மாற்றம்\n4. ஒரிசா ஒடிசா எனப் பெயர் மாற்றம்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="1 - 2 - 3 - 4", ta_a="1 - 2 - 3 - 4",
        en_b="2 - 1 - 3 - 4", ta_b="2 - 1 - 3 - 4",
        en_c="1 - 3 - 2 - 4", ta_c="1 - 3 - 2 - 4",
        en_d="3 - 2 - 1 - 4", ta_d="3 - 2 - 1 - 4",
        correct_key="A",
        exp_en="1. Lakshadweep: November 1973; 2. Puducherry: October 2006; 3. Uttarakhand: January 2007; 4. Odisha: November 2011. Hence, 1 - 2 - 3 - 4.",
        exp_ta="1. லட்சத்தீவு: நவம்பர் 1973; 2. புதுச்சேரி: அக்டோபர் 2006; 3. உத்தராகண்ட்: ஜனவரி 2007; 4. ஒடிசா: நவம்பர் 2011. எனவே சரியான காலவரிசை 1 - 2 - 3 - 4 ஆகும்.",
        why_a_en="Exact chronological sequence: Lakshadweep (1973) -> Puducherry (2006) -> Uttarakhand (2007) -> Odisha (2011).",
        why_a_ta="துல்லியமான ஆண்டுகள்: லட்சத்தீவு (1973) -> புதுச்சேரி (2006) -> உத்தராகண்ட் (2007) -> ஒடிசா (2011).",
        why_b_en="Lakshadweep was 1973, before Puducherry (2006).",
        why_b_ta="லட்சத்தீவு 1973-ல் மாற்றப்பட்டது.",
        why_c_en="Puducherry (2006) was renamed before Uttarakhand (2007).",
        why_c_ta="புதுச்சேரி (2006) உத்தராகண்டிற்கு (2007) முந்தையது.",
        why_d_en="Uttarakhand was 2007, not first.",
        why_d_ta="உத்தராகண்ட் 2007.",
        tip_en="Renaming: Lakshadweep (1973) -> Puducherry (2006) -> Uttarakhand (2007) -> Odisha (2011).",
        tip_ta="பெயர் மாற்றங்கள்: லட்சத்தீவு (1973) -> புதுச்சேரி (2006) -> உத்தராகண்ட் (2007) -> ஒடிசா (2011).",
        fact_en="Odisha renaming was accompanied by the 96th CAA 2011 which changed 'Oriya' to 'Odia' in the 8th Schedule.",
        fact_ta="ஒடிசா பெயர் மாற்றத்துடன் 96-வது திருத்தம் 2011 மூலம் 8-வது அட்டவணையில் 'ஒரியா' என்பது 'ஒடியா' என மாற்றப்பட்டது.",
        tags=["polity", "union_territory", "chronology", "renaming"]
    ))

    # C14: Andhra State Creation Sequence of Events (1948-1953)
    questions.append(make_ut_q(
        qid="UT_C_014", diff="Medium", qtype="Chronology",
        subtopic="Linguistic Reorganisation and Evolution of States",
        en_stem="Arrange the events leading to the creation of Andhra State in correct chronological order:\n1. Dhar Commission Report rejecting linguistic reorganisation\n2. JVP Committee Report postponing linguistic reorganisation\n3. Death of Potti Sriramulu after a 56-day hunger strike\n4. Inauguration of Andhra State at Kurnool\nSelect the correct answer using the codes given below:",
        ta_stem="ஆந்திர மாநில உருவாக்கத்திற்கு வழிவகுத்த நிகழ்வுகளை சரியான காலவரிசையில் ஒழுங்கமைக்கவும்:\n1. மொழிவாரி மறுசீரமைப்பை நிராகரித்த தார் ஆணைய அறிக்கை\n2. மொழிவாரி மறுசீரமைப்பை ஒத்திவைத்த ஜே.வி.பி குழு அறிக்கை\n3. 56 நாள் உண்ணாவிரதத்திற்குப் பின் பொட்டி ஸ்ரீராமுலுவின் மறைவு\n4. கர்னூலில் ஆந்திர மாநிலம் தொடங்கி வைக்கப்படுதல்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="1 - 2 - 3 - 4", ta_a="1 - 2 - 3 - 4",
        en_b="2 - 1 - 3 - 4", ta_b="2 - 1 - 3 - 4",
        en_c="1 - 3 - 2 - 4", ta_c="1 - 3 - 2 - 4",
        en_d="3 - 1 - 2 - 4", ta_d="3 - 1 - 2 - 4",
        correct_key="A",
        exp_en="1. Dhar Report: December 1948; 2. JVP Report: April 1949; 3. Sriramulu's death: December 15, 1952; 4. Inauguration of Andhra State: October 1, 1953. Hence, 1 - 2 - 3 - 4.",
        exp_ta="1. தார் அறிக்கை: டிசம்பர் 1948; 2. JVP அறிக்கை: ஏப்ரல் 1949; 3. ஸ்ரீராமுலு மறைவு: டிசம்பர் 15, 1952; 4. ஆந்திர மாநில தொடக்கம்: அக்டோபர் 1, 1953. எனவே சரியான காலவரிசை 1 - 2 - 3 - 4 ஆகும்.",
        why_a_en="Exact chronological sequence of events culminating in Andhra State.",
        why_a_ta="ஆந்திர மாநில உருவாக்கத்திற்கான துல்லியமான வரலாற்று காலவரிசை.",
        why_b_en="Dhar report was Dec 1948, JVP report was Apr 1949.",
        why_b_ta="தார் அறிக்கை டிச 1948, JVP அறிக்கை ஏப் 1949.",
        why_c_en="JVP report was before Sriramulu's fast.",
        why_c_ta="JVP அறிக்கை உண்ணாவிரதத்திற்கு முந்தையது.",
        why_d_en="Sriramulu died in 1952, not before the reports.",
        why_d_ta="ஸ்ரீராமுலு 1952-ல் மறைந்தார்.",
        tip_en="Dhar Report (Dec 1948) -> JVP Report (Apr 1949) -> Fast death (Dec 1952) -> State inaugurated (Oct 1953).",
        tip_ta="தார் அறிக்கை (டிச 1948) -> JVP அறிக்கை (ஏப் 1949) -> உயிர் தியாகம் (டிச 1952) -> மாநில உதயம் (அக் 1953).",
        fact_en="Jawaharlal Nehru inaugurated the new Andhra State at Kurnool on October 1, 1953.",
        fact_ta="ஜவஹர்லால் நேரு 1953 அக்டோபர் 1 அன்று கர்னூலில் புதிய ஆந்திர மாநிலத்தை தொடங்கி வைத்தார்.",
        tags=["polity", "union_territory", "chronology", "andhra"]
    ))

    # C15: States Reorganisation Milestones (1953-1956)
    questions.append(make_ut_q(
        qid="UT_C_015", diff="Medium", qtype="Chronology",
        subtopic="Linguistic Reorganisation and Evolution of States",
        en_stem="Arrange the milestones of the States Reorganisation process in correct chronological order:\n1. Appointment of the Fazl Ali Commission\n2. Submission of the Fazl Ali Commission Report\n3. Passage of the States Reorganisation Act by Parliament\n4. Implementation of 14 States and 6 Union Territories\nSelect the correct answer using the codes given below:",
        ta_stem="மாநில மறுசீரமைப்பு செயல்முறையின் முக்கிய மைல்கல்களை சரியான காலவரிசையில் ஒழுங்கமைக்கவும்:\n1. பசல் அலி ஆணையம் நியமிக்கப்படுதல்\n2. பசல் அலி ஆணையம் அறிக்கை சமர்ப்பித்தல்\n3. நாடாளுமன்றத்தால் மாநில மறுசீரமைப்புச் சட்டம் நிறைவேற்றப்படுதல்\n4. 14 மாநிலங்கள் மற்றும் 6 யூனியன் பிரதேசங்கள் நடைமுறைக்கு வருதல்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="1 - 2 - 3 - 4", ta_a="1 - 2 - 3 - 4",
        en_b="2 - 1 - 3 - 4", ta_b="2 - 1 - 3 - 4",
        en_c="1 - 3 - 2 - 4", ta_c="1 - 3 - 2 - 4",
        en_d="3 - 1 - 2 - 4", ta_d="3 - 1 - 2 - 4",
        correct_key="A",
        exp_en="1. Commission appointed: December 1953; 2. Report submitted: September 1955; 3. Act passed: August 1956; 4. Implementation: November 1, 1956. Hence, 1 - 2 - 3 - 4.",
        exp_ta="1. ஆணையம் நியமனம்: டிசம்பர் 1953; 2. அறிக்கை சமர்ப்பிப்பு: செப்டம்பர் 1955; 3. சட்டம் நிறைவேற்றம்: ஆகஸ்ட் 1956; 4. அமலாக்கம்: நவம்பர் 1, 1956. எனவே சரியான காலவரிசை 1 - 2 - 3 - 4 ஆகும்.",
        why_a_en="Exact chronological progression of the States Reorganisation Commission and Act.",
        why_a_ta="மாநில மறுசீரமைப்பு ஆணையம் மற்றும் சட்டத்தின் துல்லியமான காலவரிசை நிகழ்வுகள்.",
        why_b_en="Appointment (Dec 1953) preceded report submission (Sep 1955).",
        why_b_ta="நியமனம் அறிக்கைக்கு முந்தையது.",
        why_c_en="Report submission (1955) preceded passage of Act (1956).",
        why_c_ta="அறிக்கை சட்டத்திற்கு முந்தையது.",
        why_d_en="Act passed after report, not before.",
        why_d_ta="சட்டம் அறிக்கைக்குப் பின் இயற்றப்பட்டது.",
        tip_en="Appointed Dec 1953 -> Report Sep 1955 -> Act Aug 1956 -> Effective Nov 1, 1956.",
        tip_ta="நியமனம் டிச 1953 -> அறிக்கை செப் 1955 -> சட்டம் ஆக 1956 -> அமல் நவ 1, 1956.",
        fact_en="Nov 1 is celebrated as State Formation Day by many states (TN, Karnataka, Kerala, MP, Haryana).",
        fact_ta="நவம்பர் 1 பல மாநிலங்களால் மாநில உதய தினமாகக் கொண்டாடப்படுகிறது.",
        tags=["polity", "union_territory", "chronology", "src_milestones"]
    ))

    # C16: Portuguese Territories Evolution (1954-1987)
    questions.append(make_ut_q(
        qid="UT_C_016", diff="Hard", qtype="Chronology",
        subtopic="Article 2: Admission or Establishment of New States",
        en_stem="Arrange the historical milestones regarding Portuguese territories in India in correct chronological order:\n1. Liberation of Dadra and Nagar Haveli\n2. Incorporation of Dadra and Nagar Haveli as a UT (10th Amendment Act)\n3. Liberation of Goa, Daman and Diu by Operation Vijay\n4. Goa conferred full statehood (25th State)\nSelect the correct answer using the codes given below:",
        ta_stem="இந்தியாவில் போர்த்துகீசிய பகுதிகள் தொடர்பான வரலாற்று மைல்கல்களை சரியான காலவரிசையில் ஒழுங்கமைக்கவும்:\n1. தாத்ரா மற்றும் நகர் ஹவேலி விடுதலை செய்யப்படுதல்\n2. 10-வது திருத்தச் சட்டம் மூலம் தாத்ரா நகர் ஹவேலி UT ஆக இணைக்கப்படுதல்\n3. ஆபரேஷன் விஜய் மூலம் கோவா, தாமன் மற்றும் தியூ விடுவிக்கப்படுதல்\n4. கோவாவிற்கு முழு மாநில அந்தஸ்து வழங்கப்படுதல் (25-வது மாநிலம்)\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="1 - 2 - 3 - 4", ta_a="1 - 2 - 3 - 4",
        en_b="2 - 1 - 3 - 4", ta_b="2 - 1 - 3 - 4",
        en_c="1 - 3 - 2 - 4", ta_c="1 - 3 - 2 - 4",
        en_d="3 - 1 - 2 - 4", ta_d="3 - 1 - 2 - 4",
        correct_key="A",
        exp_en="1. DNH liberation: 1954; 2. 10th CAA: August 1961; 3. Operation Vijay (Goa liberation): December 1961; 4. Goa full statehood: May 30, 1987. Hence, 1 - 2 - 3 - 4.",
        exp_ta="1. DNH விடுதலை: 1954; 2. 10-வது திருத்தம்: ஆகஸ்ட் 1961; 3. ஆபரேஷன் விஜய் (கோவா விடுதலை): டிசம்பர் 1961; 4. கோவா மாநில அந்தஸ்து: மே 30, 1987. எனவே சரியான காலவரிசை 1 - 2 - 3 - 4 ஆகும்.",
        why_a_en="Exact chronological sequence: DNH liberated (1954) -> 10th CAA (Aug 1961) -> Goa liberated (Dec 1961) -> Goa state (1987).",
        why_a_ta="துல்லியமான காலவரிசை: DNH விடுதலை (1954) -> 10-வது திருத்தம் (ஆக 1961) -> கோவா விடுதலை (டிச 1961) -> கோவா மாநிலம் (1987).",
        why_b_en="DNH was liberated in 1954, long before the 10th CAA in 1961.",
        why_b_ta="DNH 1954-லேயே விடுவிக்கப்பட்டது.",
        why_c_en="10th CAA was enacted in August 1961, prior to Operation Vijay in December 1961.",
        why_c_ta="10-வது திருத்தம் ஆகஸ்ட் 1961, ஆபரேஷன் விஜய் டிசம்பர் 1961.",
        why_d_en="Operation Vijay was Dec 1961, not first.",
        why_d_ta="ஆபரேஷன் விஜய் டிசம்பர் 1961.",
        tip_en="DNH: Liberated 1954 -> Made UT 1961 (10th CAA). Goa: Liberated Dec 1961 (12th CAA) -> State 1987.",
        tip_ta="DNH: விடுதலை 1954 -> UT 1961 (10-வது திருத்தம்). கோவா: விடுதலை 1961 -> மாநிலம் 1987.",
        fact_en="May 30 is celebrated annually as Goa Statehood Day.",
        fact_ta="மே 30 ஆண்டுதோறும் கோவா மாநில உதய தினமாகக் கொண்டாடப்படுகிறது.",
        tags=["polity", "union_territory", "chronology", "portuguese_territories"]
    ))

    # C17: French Establishments Integration (1951-1962)
    questions.append(make_ut_q(
        qid="UT_C_017", diff="Hard", qtype="Chronology",
        subtopic="Article 2: Admission or Establishment of New States",
        en_stem="Arrange the following events regarding the integration of French establishments into India in correct chronological order:\n1. Chandernagore ceded to India by Treaty\n2. De facto transfer of Pondicherry, Karaikal, Mahe, and Yanam\n3. Ratification of Treaty of Cession by French Parliament (De jure)\n4. 14th Amendment Act integrating Puducherry as a Union Territory\nSelect the correct answer using the codes given below:",
        ta_stem="இந்தியாவில் பிரெஞ்சு பகுதிகள் இணைக்கப்பட்ட பின்வரும் நிகழ்வுகளை சரியான காலவரிசையில் ஒழுங்கமைக்கவும்:\n1. ஒப்பந்தம் மூலம் சந்தன்நகர் இந்தியாவுக்கு விட்டுக்கொடுக்கப்படுதல்\n2. பாண்டிச்சேரி, காரைக்கால், மாஹே, ஏனாம் நடைமுறை அதிகார மாற்றம் (De facto)\n3. பிரெஞ்சு நாடாளுமன்றத்தால் நிலப்பரப்பு ஒப்படைப்பு ஒப்பந்தம் ஏற்பளிக்கப்படுதல் (De jure)\n4. 14-வது திருத்தச் சட்டம் மூலம் புதுச்சேரி யூனியன் பிரதேசமாக இணைக்கப்படுதல்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="1 - 2 - 3 - 4", ta_a="1 - 2 - 3 - 4",
        en_b="2 - 1 - 3 - 4", ta_b="2 - 1 - 3 - 4",
        en_c="1 - 3 - 2 - 4", ta_c="1 - 3 - 2 - 4",
        en_d="3 - 1 - 2 - 4", ta_d="3 - 1 - 2 - 4",
        correct_key="A",
        exp_en="1. Chandernagore ceded: February 1951; 2. De facto transfer: November 1, 1954; 3. De jure ratification: May/August 1962; 4. 14th CAA: December 1962. Hence, 1 - 2 - 3 - 4.",
        exp_ta="1. சந்தன்நகர் ஒப்படைப்பு: பிப்ரவரி 1951; 2. நடைமுறை மாற்றம் (De facto): நவம்பர் 1, 1954; 3. சட்டப்பூர்வ மாற்றம் (De jure): மே/ஆகஸ்ட் 1962; 4. 14-வது திருத்தம்: டிசம்பர் 1962. எனவே சரியான காலவரிசை 1 - 2 - 3 - 4 ஆகும்.",
        why_a_en="Exact chronological sequence of French territories integration into the Indian Union.",
        why_a_ta="பிரெஞ்சு பகுதிகள் இந்திய ஒன்றியத்துடன் இணைக்கப்பட்ட துல்லியமான காலவரிசை.",
        why_b_en="Chandernagore was ceded in 1951, before the 1954 de facto transfer.",
        why_b_ta="சந்தன்நகர் 1951-லேயே ஒப்படைக்கப்பட்டது.",
        why_c_en="De facto transfer (1954) was before de jure ratification (1962).",
        why_c_ta="நடைமுறை மாற்றம் (1954) சட்டப்பூர்வ மாற்றத்திற்கு (1962) முந்தையது.",
        why_d_en="De jure ratification was 1962, not first.",
        why_d_ta="சட்டப்பூர்வ ஏற்பளிப்பு 1962.",
        tip_en="Chandernagore (1951) -> De facto (1954) -> De jure (1962) -> 14th CAA (1962).",
        tip_ta="சந்தன்நகர் (1951) -> நடைமுறை மாற்றம் (1954) -> சட்டப்பூர்வ மாற்றம் (1962) -> 14-வது திருத்தம் (1962).",
        fact_en="Chandernagore was merged into the State of West Bengal in 1954.",
        fact_ta="சந்தன்நகர் 1954-ல் மேற்கு வங்க மாநிலத்துடன் இணைக்கப்பட்டது.",
        tags=["polity", "union_territory", "chronology", "french_territories"]
    ))

    # C18: Evolution of Punjab (1948-1966)
    questions.append(make_ut_q(
        qid="UT_C_018", diff="Hard", qtype="Chronology",
        subtopic="Linguistic Reorganisation and Evolution of States",
        en_stem="Arrange the historical developments regarding Punjab in the correct chronological order:\n1. Formation of Patiala and East Punjab States Union (PEPSU)\n2. Merger of PEPSU into Punjab under States Reorganisation Act\n3. Appointment of Shah Commission by the Union Government\n4. Creation of Haryana and Union Territory of Chandigarh\nSelect the correct answer using the codes given below:",
        ta_stem="பஞ்சாப் மாநிலம் தொடர்பான பின்வரும் வரலாற்று நிகழ்வுகளை சரியான காலவரிசையில் ஒழுங்கமைக்கவும்:\n1. பட்டியாலா மற்றும் கிழக்கு பஞ்சாப் மாநிலங்கள் ஒன்றியம் (PEPSU) உருவாக்கப்படுதல்\n2. மாநில மறுசீரமைப்புச் சட்டத்தின் கீழ் PEPSU பஞ்சாப்புடன் இணைக்கப்படுதல்\n3. ஒன்றிய அரசால் ஷா ஆணையம் நியமிக்கப்படுதல்\n4. ஹரியானா மற்றும் சண்டிகர் யூனியன் பிரதேசம் உருவாக்கப்படுதல்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="1 - 2 - 3 - 4", ta_a="1 - 2 - 3 - 4",
        en_b="2 - 1 - 3 - 4", ta_b="2 - 1 - 3 - 4",
        en_c="1 - 3 - 2 - 4", ta_c="1 - 3 - 2 - 4",
        en_d="3 - 2 - 1 - 4", ta_d="3 - 2 - 1 - 4",
        correct_key="A",
        exp_en="1. PEPSU formed: July 1948; 2. PEPSU merged into Punjab: November 1, 1956; 3. Shah Commission appointed: April 1966; 4. Haryana and Chandigarh created: November 1, 1966. Hence, 1 - 2 - 3 - 4.",
        exp_ta="1. PEPSU உருவாக்கம்: ஜூலை 1948; 2. PEPSU பஞ்சாபுடன் இணைப்பு: நவம்பர் 1, 1956; 3. ஷா ஆணையம் நியமனம்: ஏப்ரல் 1966; 4. ஹரியானா & சண்டிகர் உருவாக்கம்: நவம்பர் 1, 1966. எனவே சரியான காலவரிசை 1 - 2 - 3 - 4 ஆகும்.",
        why_a_en="Exact chronological sequence of Punjab's reorganisations.",
        why_a_ta="பஞ்சாப் மறுசீரமைப்பின் துல்லியமான வரலாற்று காலவரிசை.",
        why_b_en="PEPSU was formed in 1948, merged in 1956.",
        why_b_ta="PEPSU 1948-ல் உருவானது, 1956-ல் இணைந்தது.",
        why_c_en="Merger of PEPSU was 1956, before Shah Commission (1966).",
        why_c_ta="PEPSU இணைப்பு 1956.",
        why_d_en="Shah Commission was 1966, not first.",
        why_d_ta="ஷா ஆணையம் 1966.",
        tip_en="PEPSU (1948) -> Merged to Punjab (1956) -> Shah Commission (Apr 1966) -> Haryana created (Nov 1966).",
        tip_ta="PEPSU (1948) -> பஞ்சாபுடன் இணைப்பு (1956) -> ஷா ஆணையம் (1966) -> ஹரியானா உதயம் (1966).",
        fact_en="Chandigarh was designed by French architect Le Corbusier as the capital of Punjab.",
        fact_ta="சண்டிகர் நகரம் பிரெஞ்சு கட்டிடக் கலைஞர் லீ கார்பூசியரால் பஞ்சாபின் தலைநகராக வடிவமைக்கப்பட்டது.",
        tags=["polity", "union_territory", "chronology", "punjab"]
    ))

    # C19: Evolution of Delhi (1950-1991)
    questions.append(make_ut_q(
        qid="UT_C_019", diff="Hard", qtype="Chronology",
        subtopic="Special Provisions for Delhi (Article 239AA)",
        en_stem="Arrange the constitutional milestones in the governance of Delhi in correct chronological order:\n1. Delhi categorized as a Part C State with a Legislative Assembly\n2. Delhi converted into a Union Territory without a legislature (7th Amendment)\n3. Establishment of a separate High Court for Delhi\n4. Insertion of Article 239AA designating Delhi as NCT with an Assembly (69th Amendment)\nSelect the correct answer using the codes given below:",
        ta_stem="டெல்லி நிர்வாகத்தின் அரசியலமைப்பு மைல்கல்களை சரியான காலவரிசையில் ஒழுங்கமைக்கவும்:\n1. டெல்லி சட்டப்பேரவையுடன் கூடிய பகுதி C மாநிலமாக வகைப்படுத்தப்படுதல்\n2. டெல்லி சட்டமன்றம் இல்லாத யூனியன் பிரதேசமாக மாற்றப்படுதல் (7-வது திருத்தம்)\n3. டெல்லிக்கு தனியாக ஒரு உயர்நீதிமன்றம் அமைக்கப்படுதல்\n4. 69-வது திருத்தம் மூலம் உறுப்பு 239AA சேர்க்கப்பட்டு டெல்லி சட்டமன்றத்துடன் கூடிய NCT ஆக மாறுதல்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="1 - 2 - 3 - 4", ta_a="1 - 2 - 3 - 4",
        en_b="2 - 1 - 3 - 4", ta_b="2 - 1 - 3 - 4",
        en_c="1 - 3 - 2 - 4", ta_c="1 - 3 - 2 - 4",
        en_d="3 - 1 - 2 - 4", ta_d="3 - 1 - 2 - 4",
        correct_key="A",
        exp_en="1. Part C State: 1950 (Assembly created 1952); 2. UT under 7th CAA: 1956 (Assembly abolished); 3. Delhi High Court: 1966; 4. NCT under 69th CAA: 1991. Hence, 1 - 2 - 3 - 4.",
        exp_ta="1. பகுதி C மாநிலம்: 1950 (சட்டமன்றம் 1952); 2. UT ஆக மாற்றம்: 1956 (சட்டமன்றம் நீக்கம்); 3. தில்லி உயர்நீதிமன்றம்: 1966; 4. 69-வது திருத்த NCT: 1991. எனவே சரியான காலவரிசை 1 - 2 - 3 - 4 ஆகும்.",
        why_a_en="Exact chronological evolution of Delhi's administrative and constitutional status.",
        why_a_ta="தில்லியின் நிர்வாக மற்றும் அரசியலமைப்பு நிலையின் துல்லியமான காலவரிசை பரிணாமம்.",
        why_b_en="Part C state (1950) was before UT status in 1956.",
        why_b_ta="பகுதி C மாநிலம் 1950, UT அந்தஸ்து 1956.",
        why_c_en="UT status was 1956, before High Court in 1966.",
        why_c_ta="UT அந்தஸ்து 1956, உயர்நீதிமன்றம் 1966.",
        why_d_en="High Court was 1966, not first.",
        why_d_ta="உயர்நீதிமன்றம் 1966.",
        tip_en="Delhi: Part C (1950) -> UT without assembly (1956) -> High Court (1966) -> NCT with assembly (1991).",
        tip_ta="தில்லி: பகுதி C (1950) -> சட்டமன்றமில்லா UT (1956) -> உயர்நீதிமன்றம் (1966) -> சட்டமன்றமுள்ள NCT (1991).",
        fact_en="Chaudhary Brahm Perkash was the first Chief Minister of Delhi in 1952.",
        fact_ta="1952-ல் சவுத்ரி பிரம்ம பிரகாஷ் தில்லியின் முதல் முதலமைச்சராகப் பொறுப்பேற்றார்.",
        tags=["polity", "union_territory", "chronology", "delhi"]
    ))

    # C20: Jammu and Kashmir Milestones (1947-2019)
    questions.append(make_ut_q(
        qid="UT_C_020", diff="Medium", qtype="Chronology",
        subtopic="Jammu & Kashmir Reorganisation (2019)",
        en_stem="Arrange the historical milestones regarding Jammu and Kashmir in correct chronological order:\n1. Maharaja Hari Singh signs the Instrument of Accession\n2. Delhi Agreement signed by Jawaharlal Nehru and Sheikh Abdullah\n3. Adoption of the separate Constitution of Jammu and Kashmir\n4. Enactment of the Jammu and Kashmir Reorganisation Act\nSelect the correct answer using the codes given below:",
        ta_stem="ஜம்மு காஷ்மீர் தொடர்பான வரலாற்று மைல்கல்களை சரியான காலவரிசையில் ஒழுங்கமைக்கவும்:\n1. மகாராஜா ஹரி சிங் இணைப்பு ஒப்பந்தத்தில் கையெழுத்திடுதல்\n2. ஜவஹர்லால் நேரு மற்றும் ஷேக் அப்துல்லா இடையே டெல்லி ஒப்பந்தம் கையெழுத்தாதல்\n3. ஜம்மு காஷ்மீரின் தனி அரசியலமைப்பு ஏற்றுக்கொள்ளப்படுதல்\n4. ஜம்மு காஷ்மீர் மறுசீரமைப்புச் சட்டம் இயற்றப்படுதல்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="1 - 2 - 3 - 4", ta_a="1 - 2 - 3 - 4",
        en_b="2 - 1 - 3 - 4", ta_b="2 - 1 - 3 - 4",
        en_c="1 - 3 - 2 - 4", ta_c="1 - 3 - 2 - 4",
        en_d="3 - 1 - 2 - 4", ta_d="3 - 1 - 2 - 4",
        correct_key="A",
        exp_en="1. Instrument of Accession: October 26, 1947; 2. Delhi Agreement: 1952; 3. J&K Constitution adopted: November 17, 1956 (effective Jan 26, 1957); 4. J&K Reorganisation Act: August 2019 (effective Oct 31, 2019). Hence, 1 - 2 - 3 - 4.",
        exp_ta="1. இணைப்பு ஒப்பந்தம்: அக்டோபர் 26, 1947; 2. டெல்லி ஒப்பந்தம்: 1952; 3. ஜம்மு காஷ்மீர் அரசியலமைப்பு ஏற்பு: நவம்பர் 17, 1956 (நடைமுறை ஜன 26, 1957); 4. மறுசீரமைப்புச் சட்டம்: ஆகஸ்ட் 2019. எனவே சரியான காலவரிசை 1 - 2 - 3 - 4 ஆகும்.",
        why_a_en="Exact chronological sequence of key constitutional milestones of J&K.",
        why_a_ta="ஜம்மு காஷ்மீரின் முக்கிய அரசியலமைப்பு மைல்கல்களின் துல்லியமான காலவரிசை.",
        why_b_en="Instrument of Accession (1947) was before Delhi Agreement (1952).",
        why_b_ta="இணைப்பு ஒப்பந்தம் (1947) டெல்லி ஒப்பந்தத்திற்கு (1952) முந்தையது.",
        why_c_en="Delhi Agreement was 1952, before J&K Constitution in 1956.",
        why_c_ta="டெல்லி ஒப்பந்தம் 1952.",
        why_d_en="J&K Constitution was 1956, not first.",
        why_d_ta="ஜம்மு காஷ்மீர் அரசியலமைப்பு 1956.",
        tip_en="Accession (1947) -> Delhi Agreement (1952) -> J&K Constitution (1956) -> Reorganisation Act (2019).",
        tip_ta="இணைப்பு ஒப்பந்தம் (1947) -> டெல்லி ஒப்பந்தம் (1952) -> காஷ்மீர் அரசியலமைப்பு (1956) -> மறுசீரமைப்புச் சட்டம் (2019).",
        fact_en="Section 3 of the J&K Constitution explicitly stated that J&K is and shall be an integral part of the Union of India.",
        fact_ta="ஜம்மு காஷ்மீர் அரசியலமைப்பின் பிரிவு 3 ஜம்மு காஷ்மீர் இந்திய ஒன்றியத்தின் ஒருங்கிணைந்த பகுதி எனத் தெளிவாகக் கூறியது.",
        tags=["polity", "union_territory", "chronology", "jammu_kashmir"]
    ))

    # C21: Recent Territorial Milestones (2000-2020)
    questions.append(make_ut_q(
        qid="UT_C_021", diff="Easy", qtype="Chronology",
        subtopic="Merger of Dadra & Nagar Haveli and Daman & Diu (2020)",
        en_stem="Arrange the following 21st-century territorial reorganisations in the correct chronological order:\n1. Creation of Chhattisgarh, Uttarakhand, and Jharkhand\n2. Renaming of Uttaranchal as Uttarakhand\n3. Formation of the State of Telangana\n4. Merger of Dadra & Nagar Haveli and Daman & Diu\nSelect the correct answer using the codes given below:",
        ta_stem="21-ஆம் நூற்றாண்டின் பின்வரும் நிலப்பரப்பு மறுசீரமைப்பு நிகழ்வுகளை சரியான காலவரிசையில் ஒழுங்கமைக்கவும்:\n1. சத்தீஸ்கர், உத்தராகண்ட் மற்றும் ஜார்க்கண்ட் உருவாக்கம்\n2. உத்தராஞ்சல் உத்தராகண்ட் எனப் பெயர் மாற்றம்\n3. தெலுங்கானா மாநில உருவாக்கம்\n4. தாத்ரா நகர் ஹவேலி மற்றும் தாமன் தியூ இணைப்பு\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="1 - 2 - 3 - 4", ta_a="1 - 2 - 3 - 4",
        en_b="2 - 1 - 3 - 4", ta_b="2 - 1 - 3 - 4",
        en_c="1 - 3 - 2 - 4", ta_c="1 - 3 - 2 - 4",
        en_d="3 - 1 - 2 - 4", ta_d="3 - 1 - 2 - 4",
        correct_key="A",
        exp_en="1. Three States formed: November 2000; 2. Uttarakhand renamed: January 1, 2007; 3. Telangana formed: June 2, 2014; 4. DNHDD merger: January 26, 2020. Hence, 1 - 2 - 3 - 4.",
        exp_ta="1. மூன்று மாநிலங்கள் உதயம்: நவம்பர் 2000; 2. உத்தராகண்ட் பெயர் மாற்றம்: ஜனவரி 1, 2007; 3. தெலுங்கானா உருவாக்கம்: ஜூன் 2, 2014; 4. DNHDD இணைப்பு: ஜனவரி 26, 2020. எனவே சரியான காலவரிசை 1 - 2 - 3 - 4 ஆகும்.",
        why_a_en="Exact chronological dates: Nov 2000 -> Jan 2007 -> June 2014 -> Jan 2020.",
        why_a_ta="துல்லியமான தேதிகள்: நவம்பர் 2000 -> ஜனவரி 2007 -> ஜூன் 2014 -> ஜனவரி 2020.",
        why_b_en="State formation was 2000, renaming was 2007.",
        why_b_ta="மாநிலங்கள் உருவானது 2000, பெயர் மாற்றம் 2007.",
        why_c_en="Renaming was 2007, before Telangana (2014).",
        why_c_ta="பெயர் மாற்றம் 2007, தெலுங்கானாவிற்கு (2014) முந்தையது.",
        why_d_en="Telangana was 2014, not first.",
        why_d_ta="தெலுங்கானா 2014.",
        tip_en="21st century timeline: Nov 2000 (3 states) -> 2006 (Puducherry) -> 2007 (Uttarakhand) -> 2011 (Odisha) -> 2014 (Telangana) -> 2019 (J&K) -> 2020 (DNHDD).",
        tip_ta="21-ம் நூற்றாண்டு காலவரிசை: 2000 (3 மாநிலங்கள்) -> 2007 (உத்தராகண்ட்) -> 2014 (தெலுங்கானா) -> 2020 (DNHDD).",
        fact_en="The merger in 2020 reduced India's UTs from 9 to 8.",
        fact_ta="2020 இணைப்பு இந்தியாவின் யூனியன் பிரதேசங்களின் எண்ணிக்கையை 9-லிருந்து 8 ஆகக் குறைத்தது.",
        tags=["polity", "union_territory", "chronology", "21st_century"]
    ))

    # C22: UTs Elevated to Statehood (1971-1987)
    questions.append(make_ut_q(
        qid="UT_C_022", diff="Medium", qtype="Chronology",
        subtopic="Linguistic Reorganisation and Evolution of States",
        en_stem="Arrange the following former Union Territories in the correct chronological order of their elevation to full statehood:\n1. Himachal Pradesh\n2. Manipur\n3. Mizoram\n4. Goa\nSelect the correct answer using the codes given below:",
        ta_stem="முன்னாள் யூனியன் பிரதேசங்கள் முழு மாநில அந்தஸ்துக்கு உயர்த்தப்பட்ட சரியான காலவரிசையை ஒழுங்கமைக்கவும்:\n1. இமாச்சல பிரதேசம்\n2. மணிப்பூர்\n3. மிசோரம்\n4. கோவா\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="1 - 2 - 3 - 4", ta_a="1 - 2 - 3 - 4",
        en_b="2 - 1 - 3 - 4", ta_b="2 - 1 - 3 - 4",
        en_c="1 - 3 - 2 - 4", ta_c="1 - 3 - 2 - 4",
        en_d="3 - 2 - 1 - 4", ta_d="3 - 2 - 1 - 4",
        correct_key="A",
        exp_en="1. Himachal Pradesh: January 1971; 2. Manipur: January 1972; 3. Mizoram: February 1987; 4. Goa: May 1987. Hence, 1 - 2 - 3 - 4.",
        exp_ta="1. இமாச்சல பிரதேசம்: ஜனவரி 1971; 2. மணிப்பூர்: ஜனவரி 1972; 3. மிசோரம்: பிப்ரவரி 1987; 4. கோவா: மே 1987. எனவே சரியான காலவரிசை 1 - 2 - 3 - 4 ஆகும்.",
        why_a_en="Exact chronological statehood: HP (1971) -> Manipur (1972) -> Mizoram (Feb 1987) -> Goa (May 1987).",
        why_a_ta="துல்லியமான காலவரிசை: இமாச்சலம் (1971) -> மணிப்பூர் (1972) -> மிசோரம் (பிப் 1987) -> கோவா (மே 1987).",
        why_b_en="HP was 1971, before Manipur (1972).",
        why_b_ta="இமாச்சலம் 1971, மணிப்பூருக்கு (1972) முந்தையது.",
        why_c_en="Manipur was 1972, before Mizoram (1987).",
        why_c_ta="மணிப்பூர் 1972, மிசோரத்திற்கு முந்தையது.",
        why_d_en="Mizoram was 1987, not first.",
        why_d_ta="மிசோரம் 1987.",
        tip_en="UTs to States: HP (1971) -> Manipur & Tripura (1972) -> Mizoram & Arunachal (Feb 1987) -> Goa (May 1987).",
        tip_ta="UT முதல் மாநிலம் வரை: இமாச்சலம் (1971) -> மணிப்பூர் (1972) -> மிசோரம் (பிப் 1987) -> கோவா (மே 1987).",
        fact_en="All these entities were Union Territories before they became full-fledged States.",
        fact_ta="இப்பகுதிகள் அனைத்தும் முழு மாநிலங்களாக மாறுவதற்கு முன்பு யூனியன் பிரதேசங்களாக இருந்தன.",
        tags=["polity", "union_territory", "chronology", "ut_to_state"]
    ))

    # C23: Alteration of Name Acts Chronology
    questions.append(make_ut_q(
        qid="UT_C_023", diff="Hard", qtype="Chronology",
        subtopic="Renaming of States and UTs",
        en_stem="Arrange the following Parliamentary Acts for the alteration of names of States in the correct chronological order:\n1. The Madras State (Alteration of Name) Act\n2. The Mysore State (Alteration of Name) Act\n3. The Uttaranchal (Alteration of Name) Act\n4. The Orissa (Alteration of Name) Act\nSelect the correct answer using the codes given below:",
        ta_stem="மாநிலங்களின் பெயர்களை மாற்றுவதற்காக நாடாளுமன்றத்தால் இயற்றப்பட்ட பின்வரும் சட்டங்களை சரியான காலவரிசையில் ஒழுங்கமைக்கவும்:\n1. மெட்ராஸ் மாநில (பெயர் மாற்றம்) சட்டம்\n2. மைசூர் மாநில (பெயர் மாற்றம்) சட்டம்\n3. உத்தராஞ்சல் (பெயர் மாற்றம்) சட்டம்\n4. ஒரிசா (பெயர் மாற்றம்) சட்டம்\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="1 - 2 - 3 - 4", ta_a="1 - 2 - 3 - 4",
        en_b="2 - 1 - 3 - 4", ta_b="2 - 1 - 3 - 4",
        en_c="1 - 3 - 2 - 4", ta_c="1 - 3 - 2 - 4",
        en_d="3 - 2 - 1 - 4", ta_d="3 - 2 - 1 - 4",
        correct_key="A",
        exp_en="1. Madras State Act: 1968 (effective Jan 14, 1969); 2. Mysore State Act: 1973 (effective Nov 1, 1973); 3. Uttaranchal Act: 2006 (effective Jan 1, 2007); 4. Orissa Act: 2011 (effective Nov 1, 2011). Hence, 1 - 2 - 3 - 4.",
        exp_ta="1. மெட்ராஸ் சட்டம்: 1968 (அமலாக்கம் 14 ஜனவரி 1969); 2. மைசூர் சட்டம்: 1973 (அமலாக்கம் 1 நவம்பர் 1973); 3. உத்தராஞ்சல் சட்டம்: 2006 (அமலாக்கம் 1 ஜனவரி 2007); 4. ஒரிசா சட்டம்: 2011 (அமலாக்கம் 1 நவம்பர் 2011). எனவே சரியான காலவரிசை 1 - 2 - 3 - 4 ஆகும்.",
        why_a_en="Exact chronological enactment of Parliamentary name alteration statutes: 1968 -> 1973 -> 2006 -> 2011.",
        why_a_ta="நாடாளுமன்ற பெயர் மாற்றச் சட்டங்களின் துல்லியமான காலவரிசை: 1968 -> 1973 -> 2006 -> 2011.",
        why_b_en="Madras Act (1968) was enacted before Mysore Act (1973).",
        why_b_ta="மெட்ராஸ் சட்டம் (1968) மைசூர் சட்டத்திற்கு (1973) முந்தையது.",
        why_c_en="Mysore was 1973, before Uttaranchal (2006).",
        why_c_ta="மைசூர் சட்டம் 1973.",
        why_d_en="Uttaranchal was 2006, not first.",
        why_d_ta="உத்தராஞ்சல் சட்டம் 2006.",
        tip_en="Name alteration Acts: Madras (1968), Mysore (1973), Pondicherry (2006), Uttaranchal (2006), Orissa (2011).",
        tip_ta="பெயர் மாற்றச் சட்டங்கள்: மெட்ராஸ் (1968), மைசூர் (1973), புதுச்சேரி (2006), உத்தராஞ்சல் (2006), ஒரிசா (2011).",
        fact_en="Article 3 gives Parliament the plenary power to alter state names by an ordinary law.",
        fact_ta="உறுப்பு 3 மாநிலப் பெயர்களை சாதாரண சட்டம் மூலம் மாற்ற நாடாளுமன்றத்திற்கு முழு அதிகாரம் அளிக்கிறது.",
        tags=["polity", "union_territory", "chronology", "name_acts"]
    ))

    # C24: 21st-Century Constitutional / Reorganisation Milestones
    questions.append(make_ut_q(
        qid="UT_C_024", diff="Hard", qtype="Chronology",
        subtopic="Article 1: Name and Territory of the Union",
        en_stem="Arrange the following 21st-century constitutional and territorial milestones in the correct chronological order:\n1. 84th Amendment Act (freezing parliamentary seats based on 1971 census until 2026)\n2. 100th Amendment Act (Exchange of enclaves with Bangladesh)\n3. The Jammu and Kashmir Reorganisation Act\n4. Merger of Dadra and Nagar Haveli and Daman and Diu\nSelect the correct answer using the codes given below:",
        ta_stem="21-ஆம் நூற்றாண்டின் பின்வரும் அரசியலமைப்பு மற்றும் நிலப்பரப்பு மைல்கல்களை சரியான காலவரிசையில் ஒழுங்கமைக்கவும்:\n1. 84-வது திருத்தச் சட்டம் (1971 மக்கள் தொகை கணக்கெடுப்பின்படி நாடாளுமன்ற இடங்களை 2026 வரை முடக்குதல்)\n2. 100-வது திருத்தச் சட்டம் (வங்கதேசத்துடன் சிற்றெல்லைப் பகுதிகள் பரிமாற்றம்)\n3. ஜம்மு காஷ்மீர் மறுசீரமைப்புச் சட்டம்\n4. தாத்ரா நகர் ஹவேலி மற்றும் தாமன் தியூ இணைப்பு\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="1 - 2 - 3 - 4", ta_a="1 - 2 - 3 - 4",
        en_b="2 - 1 - 3 - 4", ta_b="2 - 1 - 3 - 4",
        en_c="1 - 3 - 2 - 4", ta_c="1 - 3 - 2 - 4",
        en_d="3 - 1 - 2 - 4", ta_d="3 - 1 - 2 - 4",
        correct_key="A",
        exp_en="1. 84th CAA: 2001; 2. 100th CAA: May 2015; 3. J&K Reorganisation: August / October 2019; 4. DNHDD Merger: December 2019 / January 26, 2020. Hence, 1 - 2 - 3 - 4.",
        exp_ta="1. 84-வது திருத்தம்: 2001; 2. 100-வது திருத்தம்: மே 2015; 3. ஜம்மு காஷ்மீர் மறுசீரமைப்பு: ஆகஸ்ட்/அக்டோபர் 2019; 4. DNHDD இணைப்பு: ஜனவரி 26, 2020. எனவே சரியான காலவரிசை 1 - 2 - 3 - 4 ஆகும்.",
        why_a_en="Exact chronological sequence: 84th CAA (2001) -> 100th CAA (2015) -> J&K Act (2019) -> DNHDD Merger (2020).",
        why_a_ta="துல்லியமான வரிசை: 84-வது திருத்தம் (2001) -> 100-வது திருத்தம் (2015) -> ஜம்மு காஷ்மீர் சட்டம் (2019) -> DNHDD இணைப்பு (2020).",
        why_b_en="84th CAA was 2001, before 100th CAA (2015).",
        why_b_ta="84-வது திருத்தம் 2001.",
        why_c_en="100th CAA was 2015, before J&K Act (2019).",
        why_c_ta="100-வது திருத்தம் 2015.",
        why_d_en="J&K Act was 2019, not first.",
        why_d_ta="ஜம்மு காஷ்மீர் சட்டம் 2019.",
        tip_en="21st century: 2001 (84th CAA) -> 2015 (100th CAA) -> 2019 (J&K) -> 2020 (DNHDD).",
        tip_ta="21-ம் நூற்றாண்டு: 2001 (84-வது திருத்தம்) -> 2015 (100-வது திருத்தம்) -> 2019 (J&K) -> 2020 (DNHDD).",
        fact_en="The 84th CAA froze Lok Sabha constituency delimitation until the first census after 2026.",
        fact_ta="84-வது திருத்தம் 2026-க்குப் பிந்தைய முதல் மக்கள் தொகை கணக்கெடுப்பு வரை மக்களவைத் தொகுதிகளின் எண்ணிக்கையை முடக்கியது.",
        tags=["polity", "union_territory", "chronology", "21st_century_amendments"]
    ))

    # C25: Evolution of Number of States / UTs
    questions.append(make_ut_q(
        qid="UT_C_025", diff="Medium", qtype="Chronology",
        subtopic="Article 1: Name and Territory of the Union",
        en_stem="Arrange the following phases in the count of States and Union Territories in correct chronological order:\n1. 14 States and 6 Union Territories (States Reorganisation Act)\n2. 25 States and 7 Union Territories (after Goa became a state in 1987)\n3. 29 States and 7 Union Territories (after Telangana was created in 2014)\n4. 28 States and 8 Union Territories (after J&K reorganisation and DNHDD merger)\nSelect the correct answer using the codes given below:",
        ta_stem="மாநிலங்கள் மற்றும் யூனியன் பிரதேசங்களின் எண்ணிக்கையின் பின்வரும் கட்டங்களை சரியான காலவரிசையில் ஒழுங்கமைக்கவும்:\n1. 14 மாநிலங்கள் மற்றும் 6 யூனியன் பிரதேசங்கள் (மாநில மறுசீரமைப்புச் சட்டம்)\n2. 25 மாநிலங்கள் மற்றும் 7 யூனியன் பிரதேசங்கள் (1987-ல் கோவா மாநிலமான பின்)\n3. 29 மாநிலங்கள் மற்றும் 7 யூனியன் பிரதேசங்கள் (2014-ல் தெலுங்கானா உருவான பின்)\n4. 28 மாநிலங்கள் மற்றும் 8 யூனியன் பிரதேசங்கள் (ஜம்மு காஷ்மீர் மறுசீரமைப்பு மற்றும் DNHDD இணைப்பிற்குப் பின்)\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        en_a="1 - 2 - 3 - 4", ta_a="1 - 2 - 3 - 4",
        en_b="2 - 1 - 3 - 4", ta_b="2 - 1 - 3 - 4",
        en_c="1 - 3 - 2 - 4", ta_c="1 - 3 - 2 - 4",
        en_d="3 - 2 - 1 - 4", ta_d="3 - 2 - 1 - 4",
        correct_key="A",
        exp_en="1. 14 States + 6 UTs: November 1956; 2. 25 States + 7 UTs: May 1987; 3. 29 States + 7 UTs: June 2014; 4. 28 States + 8 UTs: January 2020 to present. Hence, the correct order is 1 - 2 - 3 - 4.",
        exp_ta="1. 14 மாநிலங்கள் + 6 UTக்கள்: நவம்பர் 1956; 2. 25 மாநிலங்கள் + 7 UTக்கள்: மே 1987; 3. 29 மாநிலங்கள் + 7 UTக்கள்: ஜூன் 2014; 4. 28 மாநிலங்கள் + 8 UTக்கள்: ஜனவரி 2020 முதல் தற்போது வரை. எனவே சரியான காலவரிசை 1 - 2 - 3 - 4 ஆகும்.",
        why_a_en="Exact chronological progression of the quantitative strength of the Indian Union.",
        why_a_ta="இந்திய ஒன்றியத்தின் மாநிலங்கள் மற்றும் UT-களின் எண்ணிக்கைப் பரிணாமத்தின் துல்லியமான காலவரிசை.",
        why_b_en="14 States + 6 UTs was 1956, before 1987.",
        why_b_ta="14 மாநிலங்கள் + 6 UTக்கள் 1956-ல் நிலவியது.",
        why_c_en="25 states was 1987, before 2014.",
        why_c_ta="25 மாநிலங்கள் 1987-ல் நிலவியது.",
        why_d_en="29 states was 2014, not first.",
        why_d_ta="29 மாநிலங்கள் 2014-ல் இருந்தது.",
        tip_en="Evolution of numbers: 1956 (14+6) -> 1987 (25+7) -> 2000 (28+7) -> 2014 (29+7) -> Oct 2019 (28+9) -> Jan 2020-Present (28+8).",
        tip_ta="எண்ணிக்கைப் பரிணாமம்: 1956 (14+6) -> 1987 (25+7) -> 2000 (28+7) -> 2014 (29+7) -> அக் 2019 (28+9) -> ஜன 2020 முதல் (28+8).",
        fact_en="India's current federal count: 28 States and 8 Union Territories.",
        fact_ta="இந்தியாவின் தற்போதைய கூட்டாட்சி எண்ணிக்கை: 28 மாநிலங்கள் மற்றும் 8 யூனியன் பிரதேசங்கள்.",
        tags=["polity", "union_territory", "chronology", "evolution_count"]
    ))

    return questions

def main():
    questions = get_chronology_questions()
    print(f"Generated {len(questions)} Chronology questions.")
    
    for idx, q in enumerate(questions, 1):
        q["id"] = f"UT_C_{idx:03d}"
        
    balanced = balance_question_keys(questions)
    out_dir = os.path.join("data", "questions", "polity")
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "union_territory_chronology.json")
    
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(balanced)} questions to {out_file}")
    
    res = ContentValidator.validate_file(out_file, expected_count=25, expected_prefix="UT_C_")
    print("\n--- ContentValidator Summary ---")
    print(res.summary())
    if not res.is_valid:
        print("Issues found:")
        for issue in res.issues:
            print(f" - [{issue.severity}] {issue.field}: {issue.message}")
        sys.exit(1)
    else:
        print("\nALL 25 CHRONOLOGY QUESTIONS VALIDATED PERFECTLY! (PASS)")

if __name__ == "__main__":
    main()
