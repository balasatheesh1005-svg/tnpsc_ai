# -*- coding: utf-8 -*-
"""
Generator for Attorney General of India Match the Following MCQs (25 Questions: AG_MF_001 to AG_MF_025).
Strictly adheres to:
- Full 24-field TNPSC Nova AI schema
- Balanced answer keys (~6-7 of each A, B, C, D)
- Fully bilingual (English and authentic Tamil)
- Standard List-I and List-II matching format
"""

import json
import os
import shutil
from ag_mcq_helper import make_ag_q
from rebalance_er_helper import balance_question_keys
from tools.nova_content_engine.validator import ContentValidator

raw_match_data = [
    # 1: Articles Part 1
    {
        "subtopic": "Constitutional Articles",
        "title_en": "Match List-I (Constitutional Articles) with List-II (Subject Matter relating to the Attorney General) and select the correct code:",
        "title_ta": "பட்டியல்-I-ஐ (அரசியலமைப்புச் சரத்துகள்) பட்டியல்-II உடன் (தலைமை வழக்கறிஞர் தொடர்பான பொருள்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "l1_en": [("a. Article 76", "1. Office, appointment, and duties of Attorney General of India"),
                  ("b. Article 88", "2. Rights of Attorney General to speak in Parliament and committees"),
                  ("c. Article 105(4)", "3. Powers, privileges, and immunities of the Attorney General as an MP"),
                  ("d. Article 143", "4. Representation of the Union in Presidential advisory references")],
        "l1_ta": [("a. சரத்து 76", "1. இந்திய தலைமை வழக்கறிஞரின் பதவி, நியமனம் மற்றும் கடமைகள்"),
                  ("b. சரத்து 88", "2. நாடாளுமன்றத்திலும் குழுக்களிலும் பேச தலைமை வழக்கறிஞரின் உரிமை"),
                  ("c. சரத்து 105(4)", "3. நாடாளுமன்ற உறுப்பினராக தலைமை வழக்கறிஞரின் அதிகாரங்கள் மற்றும் சலுகைகள்"),
                  ("d. சரத்து 143", "4. குடியரசுத் தலைவர் ஆலோசனை குறிப்புரைகளில் ஒன்றிய அரசைப் பிரதிநிதித்துவப்படுத்துதல்")],
        "correct_map": "a-1, b-2, c-3, d-4",
        "options_perms": [
            "a-1, b-2, c-3, d-4",
            "a-2, b-1, c-4, d-3",
            "a-3, b-4, c-1, d-2",
            "a-4, b-3, c-2, d-1"
        ],
        "exp_en": "Under the Constitution: Article 76 establishes the AG; Article 88 grants parliamentary audience without vote; Article 105(4) confers MP privileges; Article 143 involves AG arguing Presidential references.",
        "exp_ta": "அரசியலமைப்பின் கீழ்: சரத்து 76 தலைமை வழக்கறிஞரை உருவாக்குகிறது; சரத்து 88 வாக்குரிமையின்றி பேசும் உரிமையை அளிக்கிறது; சரத்து 105(4) எம்பி சலுகைகளை வழங்குகிறது; சரத்து 143 குடியரசுத் தலைவர் குறிப்புரைகளில் AG வாதாடுவதைக் குறிக்கிறது.",
        "tip_en": "Master Articles 76, 88, 105(4), and 143 for all Attorney General questions.",
        "tip_ta": "தலைமை வழக்கறிஞர் தொடர்பான சரத்துக்கள் 76, 88, 105(4), மற்றும் 143-ஐ கட்டாயம் நினைவில் வையுங்கள்.",
        "fact_en": "Part V Chapter I covers Article 76; Chapter II covers Articles 88 and 105; Chapter IV covers Article 143.",
        "fact_ta": "பகுதி V அத்தியாயம் I சரத்து 76-ஐயும்; அத்தியாயம் II சரத்துக்கள் 88 மற்றும் 105-ஐயும்; அத்தியாயம் IV சரத்து 143-ஐயும் உள்ளடக்கியது."
    },
    # 2: Parallel State Provisions
    {
        "subtopic": "Union vs State Parallel Provisions",
        "title_en": "Match List-I (Provisions for Attorney General of India) with List-II (Parallel Provisions for Advocate General of State):",
        "title_ta": "பட்டியல்-I-ஐ (இந்திய தலைமை வழக்கறிஞருக்கான விதிகள்) பட்டியல்-II உடன் (மாநில அட்வகேட் ஜெனரலுக்கான இணை விதிகள்) பொருத்துக:",
        "l1_en": [("a. Article 76 (Office of Attorney General)", "1. Article 165 (Office of Advocate General)"),
                  ("b. Article 88 (Right to speak in Union Parliament)", "2. Article 177 (Right to speak in State Legislature)"),
                  ("c. Article 105(4) (Parliamentary Privileges of AG)", "3. Article 194(4) (State Legislative Privileges of Advocate General)"),
                  ("d. Qualification to be Supreme Court Judge", "4. Qualification to be High Court Judge")],
        "l1_ta": [("a. சரத்து 76 (தலைமை வழக்கறிஞர் அலுவலகம்)", "1. சரத்து 165 (அட்வகேட் ஜெனரல் அலுவலகம்)"),
                  ("b. சரத்து 88 (நாடாளுமன்றத்தில் பேசும் உரிமை)", "2. சரத்து 177 (மாநில சட்டமன்றத்தில் பேசும் உரிமை)"),
                  ("c. சரத்து 105(4) (நாடாளுமன்ற சலுகைகள்)", "3. சரத்து 194(4) (சட்டமன்ற சலுகைகள்)"),
                  ("d. உச்ச நீதிமன்ற நீதிபதிக்கான தகுதி", "4. உயர் நீதிமன்ற நீதிபதிக்கான தகுதி")],
        "correct_map": "a-1, b-2, c-3, d-4",
        "options_perms": [
            "a-1, b-2, c-3, d-4",
            "a-2, b-1, c-4, d-3",
            "a-4, b-3, c-2, d-1",
            "a-3, b-4, c-1, d-2"
        ],
        "exp_en": "Constitutional parallels: Art 76 matches Art 165; Art 88 matches Art 177; Art 105(4) matches Art 194(4); AG requires SC judge qualifications while Advocate General requires HC judge qualifications.",
        "exp_ta": "அரசியலமைப்பு இணை விதிகள்: சரத்து 76 இணை 165; சரத்து 88 இணை 177; சரத்து 105(4) இணை 194(4); AG உச்ச நீதிமன்ற நீதிபதி தகுதியையும், அட்வகேட் ஜெனரல் உயர் நீதிமன்ற நீதிபதி தகுதியையும் கொண்டிருக்க வேண்டும்.",
        "tip_en": "Remember the 89-rule: 76+89=165, 88+89=177, 105+89=194!",
        "tip_ta": "89 கூட்டல் விதியை நினைவில் வையுங்கள்: 76+89=165, 88+89=177, 105+89=194!",
        "fact_en": "The constitutional architecture of the Advocate General directly mirrors the Attorney General.",
        "fact_ta": "மாநில அட்வகேட் ஜெனரலின் அரசியலமைப்பு கட்டமைப்பு தலைமை வழக்கறிஞரை அப்படியே பிரதிபலிக்கிறது."
    },
    # 3: Statutory Provisions
    {
        "subtopic": "Statutory Provisions",
        "title_en": "Match List-I (Statutes and Legal Provisions) with List-II (Specific Application to Law Officers):",
        "title_ta": "பட்டியல்-I-ஐ (சட்டங்கள் மற்றும் சட்ட விதிகள்) பட்டியல்-II உடன் (சட்ட அதிகாரிகளுக்கான குறிப்பிட்ட பயன்பாடுகள்) பொருத்துக:",
        "l1_en": [("a. Section 23, Advocates Act 1961", "1. Statutory right of pre-audience over all advocates"),
                  ("b. Section 4, Advocates Act 1961", "2. Ex-officio membership in the Bar Council of India"),
                  ("c. Section 15, Contempt of Courts Act 1971", "3. Prior written consent required for private criminal contempt motions"),
                  ("d. Section 126, Indian Evidence Act 1872", "4. Professional privilege protecting attorney-client legal consultations")],
        "l1_ta": [("a. பிரிவு 23, வழக்கறிஞர்கள் சட்டம் 1961", "1. அனைத்து வழக்கறிஞர்களையும் விட முதன்மை வழக்காடும் சட்டப்பூர்வ உரிமை"),
                  ("b. பிரிவு 4, வழக்கறிஞர்கள் சட்டம் 1961", "2. இந்திய பார் கவுன்சிலின் பதவி வழி உறுப்பினர் பதவி"),
                  ("c. பிரிவு 15, நீதிமன்ற அவமதிப்புச் சட்டம் 1971", "3. தனிநபர் குற்றவியல் அவமதிப்பு மனுக்களுக்கு முன் எழுத்துப்பூர்வ ஒப்புதல்"),
                  ("d. பிரிவு 126, இந்திய சாட்சியச் சட்டம் 1872", "4. வழக்கறிஞர்-வாடிக்கையாளர் சட்ட ஆலோசனைகளைப் பாதுகாக்கும் தொழில்முறை ரகசியம்")],
        "correct_map": "a-1, b-2, c-3, d-4",
        "options_perms": [
            "a-1, b-2, c-3, d-4",
            "a-3, b-4, c-1, d-2",
            "a-2, b-1, c-4, d-3",
            "a-4, b-2, c-1, d-3"
        ],
        "exp_en": "Section 23 of Advocates Act gives pre-audience; Section 4 gives BCI ex-officio membership; Section 15 of Contempt Act requires AG consent; Section 126 Evidence Act protects legal advice privilege.",
        "exp_ta": "வழக்கறிஞர்கள் சட்டம் பிரிவு 23 முதன்மை வாதாடும் உரிமையையும்; பிரிவு 4 பார் கவுன்சில் உறுப்பினர் பதவியையும்; நீதிமன்ற அவமதிப்புச் சட்டம் பிரிவு 15 AG ஒப்புதலையும்; சாட்சியச் சட்டம் பிரிவு 126 தொழில்முறை ரகசியத்தையும் வழங்குகிறது.",
        "tip_en": "Section 23 = Pre-audience; Section 15 Contempt = AG consent; Section 4 = BCI membership.",
        "tip_ta": "பிரிவு 23 = முதன்மை வாதாடல்; பிரிவு 15 = அவமதிப்பு ஒப்புதல்; பிரிவு 4 = பார் கவுன்சில் உறுப்பினர்.",
        "fact_en": "These statutory provisions anchor the Attorney General's unique position in Indian law.",
        "fact_ta": "இந்த சட்ட விதிகள் இந்திய சட்டத்துறையில் தலைமை வழக்கறிஞரின் தனித்துவமான நிலையை உறுதிப்படுத்துகின்றன."
    },
    # 4: Historical Law Officers
    {
        "subtopic": "Historical Evolution of Law Officers",
        "title_en": "Match List-I (Historical Eras & Enactments) with List-II (Designation of Chief Law Officer):",
        "title_ta": "பட்டியல்-I-ஐ (வரலாற்று காலகட்டங்கள் மற்றும் சட்டங்கள்) பட்டியல்-II உடன் (தலைமைச் சட்ட அதிகாரியின் பதவிப் பெயர்) பொருத்துக:",
        "l1_en": [("a. East India Company Administration (1684)", "1. Advocate-General of Bengal"),
                  ("b. Government of India Act, 1935", "2. Advocate-General for the Federation"),
                  ("c. Constitution of India (1950)", "3. Attorney General of India"),
                  ("d. Modern Executive Rules (1987)", "4. Law Officers (Conditions of Service) Rules")],
        "l1_ta": [("a. கிழக்கிந்திய கம்பெனி நிர்வாகம் (1684)", "1. வங்காள அட்வகேட்-ஜெனரல்"),
                  ("b. இந்திய அரசுச் சட்டம், 1935", "2. கூட்டாட்சிக்கான அட்வகேட்-ஜெனரல்"),
                  ("c. இந்திய அரசியலமைப்பு (1950)", "3. இந்திய தலைமை வழக்கறிஞர்"),
                  ("d. நவீன நிர்வாக விதிகள் (1987)", "4. சட்ட அதிகாரிகள் (பணி நிபந்தனைகள்) விதிகள்")],
        "correct_map": "a-1, b-2, c-3, d-4",
        "options_perms": [
            "a-1, b-2, c-3, d-4",
            "a-2, b-1, c-4, d-3",
            "a-3, b-4, c-1, d-2",
            "a-4, b-3, c-2, d-1"
        ],
        "exp_en": "In 1684, the Advocate-General of Bengal was established; in 1935, Section 16 created Advocate-General for the Federation; in 1950, Article 76 established the Attorney General; in 1987, the Law Officers Rules were promulgated.",
        "exp_ta": "1684-ல் வங்காள அட்வகேட் ஜெனரல்; 1935-ல் கூட்டாட்சி அட்வகேட் ஜெனரல்; 1950-ல் சரத்து 76 தலைமை வழக்கறிஞர்; 1987-ல் சட்ட அதிகாரிகள் விதிகள் கொண்டுவரப்பட்டன.",
        "tip_en": "Advocate-General of Bengal (1684) -> Advocate-General for Federation (1935) -> Attorney General of India (1950).",
        "tip_ta": "வங்காள அட்வகேட் ஜெனரல் (1684) -> கூட்டாட்சி அட்வகேட் ஜெனரல் (1935) -> இந்திய தலைமை வழக்கறிஞர் (1950).",
        "fact_en": "The transition from 'Advocate-General' to 'Attorney General' occurred on January 26, 1950.",
        "fact_ta": "ஜனவரி 26, 1950 அன்று 'அட்வகேட் ஜெனரல்' என்ற பதவி 'தலைமை வழக்கறிஞர்' (Attorney General) என மாறியது."
    },
    # 5: Early Attorneys General
    {
        "subtopic": "Early Attorneys General",
        "title_en": "Match List-I (Early Attorneys General) with List-II (Distinguishing Feature / Key Achievement):",
        "title_ta": "பட்டியல்-I-ஐ (ஆரம்பகால தலைமை வழக்கறிஞர்கள்) பட்டியல்-II உடன் (தனித்துவமான சாதனை / சிறப்பு) பொருத்துக:",
        "l1_en": [("a. M.C. Setalvad", "1. Longest-serving AG (13+ years) and 1st Law Commission Chairman"),
                  ("b. C.K. Daphtary", "2. First Solicitor General who was later elevated to Attorney General"),
                  ("c. Niren De", "3. Defended Union in Kesavananda Bharati (1973) and ADM Jabalpur (1976)"),
                  ("d. S.V. Gupte", "4. First Attorney General appointed by a non-Congress Central Government (1977)")],
        "l1_ta": [("a. எம்.சி. செடல்வாட்", "1. மிக நீண்ட காலம் பதவி வகித்தவர் (13+ ஆண்டுகள்) மற்றும் 1-வது சட்ட ஆணையத் தலைவர்"),
                  ("b. சி.கே. தப்தாரி", "2. தலைமை வழக்கறிஞராக பதவி உயர்த்தப்பட்ட முதல் சொலிசிட்டர் ஜெனரல்"),
                  ("c. நீரேன் டே", "3. கேசவானந்த பாரதி (1973) மற்றும் ஏ.டி.எம். ஜபல்பூர் (1976) வழக்குகளில் வாதாடியவர்"),
                  ("d. எஸ்.வி. குப்தே", "4. காங்கிரஸ் அல்லாத மத்திய அரசால் நியமிக்கப்பட்ட முதல் தலைமை வழக்கறிஞர் (1977)")],
        "correct_map": "a-1, b-2, c-3, d-4",
        "options_perms": [
            "a-1, b-2, c-3, d-4",
            "a-2, b-1, c-4, d-3",
            "a-3, b-4, c-1, d-2",
            "a-4, b-3, c-2, d-1"
        ],
        "exp_en": "Setalvad served 1950-1963; Daphtary was 1st SG and 2nd AG; Niren De argued Basic Structure and Emergency cases; S.V. Gupte was appointed by the Morarji Desai Janata government in 1977.",
        "exp_ta": "செடல்வாட் 1950-1963 வரை பணியாற்றினார்; தப்தாரி முதல் SG மற்றும் 2-வது AG; நீரேன் டே அடிப்படைக் கட்டமைப்பு மற்றும் அவசரநிலை வழக்குகளில் ஆஜரானார்; எஸ்.வி. குப்தே 1977 மொரார்ஜி தேசாய் அரசால் நியமிக்கப்பட்டார்.",
        "tip_en": "Setalvad = Longest tenure; Daphtary = Ex-SG; Niren De = Emergency AG; Gupte = Janata era AG.",
        "tip_ta": "செடல்வாட் = நீண்ட காலம்; தப்தாரி = முன்னாள் SG; நீரேன் டே = அவசரநிலைக் கால AG; குப்தே = ஜனதா கட்சி கால AG.",
        "fact_en": "S.V. Gupte previously served as Additional Solicitor General under Daphtary.",
        "fact_ta": "எஸ்.வி. குப்தே தப்தாரியின் கீழ் கூடுதல் சொலிசிட்டர் ஜெனரலாகப் பணியாற்றியுள்ளார்."
    },
    # 6: Landmark Cases (Part 1)
    {
        "subtopic": "Landmark Cases Argued by AGs",
        "title_en": "Match List-I (Landmark Cases) with List-II (Constitutional Principle / Core Legal Subject):",
        "title_ta": "பட்டியல்-I-ஐ (வரலாற்றுச் சிறப்புமிக்க வழக்குகள்) பட்டியல்-II உடன் (அரசியலமைப்பு கோட்பாடு / முக்கிய சட்டப் பொருள்) பொருத்துக:",
        "l1_en": [("a. In re Berubari Union (1960)", "1. Cession of Indian territory requires constitutional amendment under Art 368"),
                  ("b. Kesavananda Bharati (1973)", "2. Parliament's amending power is limited by the Basic Structure Doctrine"),
                  ("c. ADM Jabalpur (1976)", "3. Suspension of fundamental rights enforcement under Article 359 during Emergency"),
                  ("d. Maneka Gandhi (1978)", "4. Procedure established by law under Article 21 must be just, fair, and reasonable")],
        "l1_ta": [("a. பெருபாரி யூனியன் குறிப்புரை (1960)", "1. நிலப்பரப்பை விட்டுக்கொடுக்க சரத்து 368-ன் கீழ் அரசியலமைப்பு திருத்தம் கட்டாயம்"),
                  ("b. கேசவானந்த பாரதி (1973)", "2. நாடாளுமன்றத்தின் திருத்தும் அதிகாரம் அடிப்படைக் கட்டமைப்பு கோட்பாட்டிற்கு உட்பட்டது"),
                  ("c. ஏ.டி.எம். ஜபல்பூர் (1976)", "3. அவசரநிலையின் போது சரத்து 359-ன் கீழ் அடிப்படை உரிமைகளை நிலைநாட்ட முடியாது"),
                  ("d. மேனகா காந்தி (1978)", "4. சரத்து 21-ன் கீழான சட்ட நடைமுறை நியாயமானதாகவும், சரியானதாகவும் இருக்க வேண்டும்")],
        "correct_map": "a-1, b-2, c-3, d-4",
        "options_perms": [
            "a-1, b-2, c-3, d-4",
            "a-2, b-1, c-4, d-3",
            "a-3, b-4, c-1, d-2",
            "a-4, b-3, c-2, d-1"
        ],
        "exp_en": "Berubari Union established necessity of Art 368 amendment for territory cession; Kesavananda Bharati established Basic Structure; ADM Jabalpur dealt with Art 359 suspension; Maneka Gandhi established substantive due process in Art 21.",
        "exp_ta": "பெருபாரி நிலப்பரப்பு திருத்தம் தொடர்பானது; கேசவானந்த பாரதி அடிப்படைக் கட்டமைப்பை நிறுவியது; ADM ஜபல்பூர் அவசரநிலை சரத்து 359 தொடர்பானது; மேனகா காந்தி சரத்து 21-ன் நியாயமான நடைமுறையை நிறுவியது.",
        "tip_en": "Berubari = Territory cession; Kesavananda = Basic structure; ADM Jabalpur = Emergency Art 21; Maneka Gandhi = Fair procedure.",
        "tip_ta": "பெருபாரி = நிலப்பரப்பு; கேசவானந்தா = அடிப்படைக் கட்டமைப்பு; ஜபல்பூர் = அவசரநிலை; மேனகா = நியாயமான நடைமுறை.",
        "fact_en": "All four cases saw profound arguments presented by Attorneys General representing the Union of India.",
        "fact_ta": "இந்த நான்கு வழக்குகளிலுமே இந்திய தலைமை வழக்கறிஞர்கள் மிக முக்கியமான வாதங்களை முன்வைத்தனர்."
    },
    # 7: Modern Landmark Cases (Part 2)
    {
        "subtopic": "Modern Landmark Cases",
        "title_en": "Match List-I (Modern Landmark Cases) with List-II (Attorney General Representing the Union):",
        "title_ta": "பட்டியல்-I-ஐ (நவீன வரலாற்று வழக்குகள்) பட்டியல்-II உடன் (ஒன்றிய அரசின் சார்பில் வாதாடிய தலைமை வழக்கறிஞர்) பொருத்துக:",
        "l1_en": [("a. NJAC Act case (2015)", "1. Mukul Rohatgi"),
                  ("b. Aadhaar Constitution Bench (2018)", "2. K.K. Venugopal"),
                  ("c. Article 370 Abrogation hearings (2023)", "3. R. Venkataramani"),
                  ("d. 2G Natural Resources Allocation Reference (2012)", "4. G.E. Vahanvati")],
        "l1_ta": [("a. NJAC சட்ட வழக்கு (2015)", "1. முகுல் ரோஹத்கி"),
                  ("b. ஆதார் அரசியலமைப்பு அமர்வு வழக்கு (2018)", "2. கே.கே. வேணுகோபால்"),
                  ("c. சரத்து 370 ரத்து வழக்கு (2023)", "3. ஆர். வெங்கடரமணி"),
                  ("d. 2ஜி இயற்கை வளங்கள் ஒதுக்கீடு குறிப்புரை (2012)", "4. ஜி.இ. வாகனவதி")],
        "correct_map": "a-1, b-2, c-3, d-4",
        "options_perms": [
            "a-1, b-2, c-3, d-4",
            "a-2, b-1, c-4, d-3",
            "a-3, b-4, c-1, d-2",
            "a-4, b-3, c-2, d-1"
        ],
        "exp_en": "Mukul Rohatgi argued NJAC in 2015; K.K. Venugopal argued Aadhaar in 2018; R. Venkataramani argued Article 370 in 2023; G.E. Vahanvati argued the 2G Presidential Reference in 2012.",
        "exp_ta": "2015-ல் NJAC வழக்கில் முகுல் ரோஹத்கி; 2018-ல் ஆதார் வழக்கில் கே.கே. வேணுகோபால்; 2023-ல் சரத்து 370 வழக்கில் ஆர். வெங்கடரமணி; 2012-ல் 2ஜி வழக்கில் ஜி.இ. வாகனவதி ஆஜரானார்கள்.",
        "tip_en": "NJAC = Rohatgi; Aadhaar = Venugopal; Art 370 = Venkataramani; 2G Reference = Vahanvati.",
        "tip_ta": "NJAC = ரோஹத்கி; ஆதார் = வேணுகோபால்; சரத்து 370 = வெங்கடரமணி; 2G = வாகனவதி.",
        "fact_en": "These cases represent the defining constitutional battles of the 21st century in India.",
        "fact_ta": "இவ்வழக்குகள் 21-ஆம் நூற்றாண்டின் மிக முக்கியமான அரசியலமைப்புப் போர்களைக் குறிக்கின்றன."
    },
    # 8: Attorneys General & Prime Ministers
    {
        "subtopic": "Attorneys General & Prime Ministers",
        "title_en": "Match List-I (Attorney General of India) with List-II (Prime Minister during initial appointment):",
        "title_ta": "பட்டியல்-I-ஐ (இந்திய தலைமை வழக்கறிஞர்) பட்டியல்-II உடன் (அவர் முதலில் நியமிக்கப்பட்ட போது இருந்த பிரதமர்) பொருத்துக:",
        "l1_en": [("a. M.C. Setalvad", "1. Jawaharlal Nehru"),
                  ("b. Niren De", "2. Indira Gandhi"),
                  ("c. K. Parasaran", "3. Indira Gandhi / Rajiv Gandhi"),
                  ("d. Soli Sorabjee (1st term)", "4. V.P. Singh")],
        "l1_ta": [("a. எம்.சி. செடல்வாட்", "1. ஜவஹர்லால் நேரு"),
                  ("b. நீரேன் டே", "2. இந்திரா காந்தி"),
                  ("c. கே. பராசரன்", "3. இந்திரா காந்தி / ராஜீவ் காந்தி"),
                  ("d. சோலி சொராப்ஜி (முதல் முறை)", "4. வி.பி. சிங்")],
        "correct_map": "a-1, b-2, c-3, d-4",
        "options_perms": [
            "a-1, b-2, c-3, d-4",
            "a-2, b-1, c-4, d-3",
            "a-3, b-4, c-1, d-2",
            "a-4, b-3, c-2, d-1"
        ],
        "exp_en": "Setalvad was appointed under Nehru in 1950; Niren De under Indira Gandhi in 1968; K. Parasaran under Indira/Rajiv in 1983; Soli Sorabjee under V.P. Singh in 1989.",
        "exp_ta": "1950-ல் நேரு ஆட்சியில் செடல்வாட்; 1968-ல் இந்திரா காந்தி ஆட்சியில் நீரேன் டே; 1983-ல் இந்திரா/ராஜீவ் ஆட்சியில் கே. பராசரன்; 1989-ல் வி.பி. சிங் ஆட்சியில் சோலி சொராப்ஜி நியமிக்கப்பட்டனர்.",
        "tip_en": "Setalvad = Nehru; Niren De = Indira; Parasaran = Indira/Rajiv; Sorabjee = V.P. Singh (1st term).",
        "tip_ta": "செடல்வாட் = நேரு; நீரேன் டே = இந்திரா; பராசரன் = இந்திரா/ராஜீவ்; சொராப்ஜி = வி.பி. சிங்.",
        "fact_en": "Because AG is appointed on the advice of the Prime Minister/Cabinet, their appointments align with changes in government.",
        "fact_ta": "பிரதமர் மற்றும் அமைச்சரவையின் ஆலோசனையின் பேரில் நியமிக்கப்படுவதால், ஆட்சி மாற்றங்களுடன் AG நியமனங்கள் பொருந்துகின்றன."
    },
    # 9: Remuneration Determining Authorities
    {
        "subtopic": "Remuneration of Functionaries",
        "title_en": "Match List-I (Constitutional Functionary) with List-II (Authority Determining Remuneration / Salary):",
        "title_ta": "பட்டியல்-I-ஐ (அரசியலமைப்பு அலுவலர்கள்) பட்டியல்-II உடன் (ஊதியத்தை நிர்ணயிக்கும் அதிகாரம்) பொருத்துக:",
        "l1_en": [("a. Attorney General of India", "1. Determined by the President of India (Art 76(4))"),
                  ("b. Advocate General of a State", "2. Determined by the Governor of the State (Art 165(3))"),
                  ("c. Supreme Court Judges", "3. Determined by Parliament by law (Art 125(1))"),
                  ("d. Comptroller and Auditor General", "4. Determined by Parliament by law / Second Schedule (Art 148(3))")],
        "l1_ta": [("a. இந்திய தலைமை வழக்கறிஞர்", "1. இந்தியக் குடியரசுத் தலைவரால் நிர்ணயிக்கப்படுகிறது (சரத்து 76(4))"),
                  ("b. மாநில அட்வகேட் ஜெனரல்", "2. மாநில ஆளுநரால் நிர்ணயிக்கப்படுகிறது (சரத்து 165(3))"),
                  ("c. உச்ச நீதிமன்ற நீதிபதிகள்", "3. நாடாளுமன்றச் சட்டத்தால் நிர்ணயிக்கப்படுகிறது (சரத்து 125(1))"),
                  ("d. இந்திய தலைமை கணக்குத் தணிக்கையாளர்", "4. நாடாளுமன்றச் சட்டம் / இரண்டாவது அட்டவணை மூலம் (சரத்து 148(3))")],
        "correct_map": "a-1, b-2, c-3, d-4",
        "options_perms": [
            "a-1, b-2, c-3, d-4",
            "a-2, b-1, c-4, d-3",
            "a-3, b-4, c-1, d-2",
            "a-4, b-3, c-2, d-1"
        ],
        "exp_en": "AG remuneration is determined by the President; Advocate General by the Governor; SC Judges by Parliament; CAG by Parliament under Art 148.",
        "exp_ta": "AG ஊதியம் குடியரசுத் தலைவராலும்; அட்வகேட் ஜெனரல் ஊதியம் ஆளுநராலும்; உச்ச நீதிமன்ற நீதிபதிகள் ஊதியம் நாடாளுமன்றத்தாலும்; சிஏஜி ஊதியம் நாடாளுமன்றச் சட்டத்தாலும் நிர்ணயிக்கப்படுகிறது.",
        "tip_en": "AG -> President; Advocate General -> Governor; Judges & CAG -> Parliament.",
        "tip_ta": "AG -> குடியரசுத் தலைவர்; அட்வகேட் ஜெனரல் -> ஆளுநர்; நீதிபதிகள் & CAG -> நாடாளுமன்றம்.",
        "fact_en": "Unlike SC Judges and CAG, the AG's remuneration is not charged upon the Consolidated Fund of India.",
        "fact_ta": "உச்ச நீதிமன்ற நீதிபதிகள் மற்றும் சிஏஜியைப் போலன்றி, தலைமை வழக்கறிஞரின் ஊதியம் இந்திய ஒருங்கிணைந்த நிதியின் மீது கட்டாயச் செலவாக வைக்கப்படவில்லை."
    },
    # 10: Pre-audience Hierarchy
    {
        "subtopic": "Hierarchy of Law Officers",
        "title_en": "Match List-I (Order of Precedence in Indian Bar) with List-II (Law Officer under Section 23 of Advocates Act):",
        "title_ta": "பட்டியல்-I-ஐ (இந்திய வழக்கறிஞர் மன்றத்தின் முன்னுரிமை வரிசை) பட்டியல்-II உடன் (வழக்கறிஞர்கள் சட்டம் பிரிவு 23-ன் கீழ் சட்ட அதிகாரி) பொருத்துக:",
        "l1_en": [("a. Rank 1 in pre-audience", "1. Attorney General of India"),
                  ("b. Rank 2 in pre-audience", "2. Solicitor General of India"),
                  ("c. Rank 3 in pre-audience", "3. Additional Solicitor General of India"),
                  ("d. Rank 4 in pre-audience", "4. Advocate General of the respective State")],
        "l1_ta": [("a. முதன்மை வழக்காடும் வரிசையில் 1-வது இடம்", "1. இந்திய தலைமை வழக்கறிஞர்"),
                  ("b. முதன்மை வழக்காடும் வரிசையில் 2-வது இடம்", "2. இந்திய சொலிசிட்டர் ஜெனரல்"),
                  ("c. முதன்மை வழக்காடும் வரிசையில் 3-வது இடம்", "3. இந்திய கூடுதல் சொலிசிட்டர் ஜெனரல்"),
                  ("d. முதன்மை வழக்காடும் வரிசையில் 4-வது இடம்", "4. சம்பந்தப்பட்ட மாநிலத்தின் அட்வகேட் ஜெனரல்")],
        "correct_map": "a-1, b-2, c-3, d-4",
        "options_perms": [
            "a-1, b-2, c-3, d-4",
            "a-2, b-1, c-4, d-3",
            "a-3, b-4, c-1, d-2",
            "a-4, b-3, c-2, d-1"
        ],
        "exp_en": "Section 23 of Advocates Act sets order of pre-audience: 1. Attorney General, 2. Solicitor General, 3. Additional Solicitor General, 4. Advocate General of the State.",
        "exp_ta": "வழக்கறிஞர்கள் சட்டம் பிரிவு 23 முன்னுரிமை வரிசையை அமைக்கிறது: 1. தலைமை வழக்கறிஞர், 2. சொலிசிட்டர் ஜெனரல், 3. கூடுதல் சொலிசிட்டர் ஜெனரல், 4. மாநில அட்வகேட் ஜெனரல்.",
        "tip_en": "Pre-audience: AG > SG > ASG > Advocate General of State.",
        "tip_ta": "முதன்மை வாதாடும் வரிசை: AG > SG > ASG > மாநில அட்வகேட் ஜெனரல்.",
        "fact_en": "In a state High Court, the Advocate General takes precedence immediately after the Union law officers.",
        "fact_ta": "மாநில உயர் நீதிமன்றத்தில், மத்திய சட்ட அதிகாரிகளுக்கு அடுத்தபடியாக மாநில அட்வகேட் ஜெனரலுக்கு முன்னுரிமை அளிக்கப்படுகிறது."
    },
    # 11: Key Legal Terms
    {
        "subtopic": "Legal Terminology & Concepts",
        "title_en": "Match List-I (Legal Terminology / Latin Maxim) with List-II (Meaning in Context of Attorney General):",
        "title_ta": "பட்டியல்-I-ஐ (சட்டச் சொற்கள் / லத்தீன் பழமொழிகள்) பட்டியல்-II உடன் (தலைமை வழக்கறிஞர் சூழலில் பொருள்) பொருத்துக:",
        "l1_en": [("a. Durante bene placito", "1. Doctrine of Pleasure governing tenure under Article 76(4)"),
                  ("b. Pre-audience", "2. Statutory priority to address court before all other advocates"),
                  ("c. Amicus Curiae", "3. Impartial friend of the court assisting in complex public litigation"),
                  ("d. Nolle Prosequi", "4. Prerogative power to drop prosecution (not possessed by Indian AG)")],
        "l1_ta": [("a. Durante bene placito", "1. சரத்து 76(4)-ன் கீழ் பதவிக்காலத்தை நிர்வகிக்கும் விருப்பக் கோட்பாடு"),
                  ("b. Pre-audience", "2. பிற அனைத்து வழக்கறிஞர்களுக்கும் முன் நீதிமன்றத்தில் வாதாடும் சட்டப்பூர்வ முன்னுரிமை"),
                  ("c. Amicus Curiae", "3. பொது நல வழக்குகளில் நீதிமன்றத்திற்கு உதவும் நடுநிலையான ஆலோசகர் (நீதிமன்ற நண்பர்)"),
                  ("d. Nolle Prosequi", "4. வழக்குகளை தன்னிச்சையாக ரத்து செய்யும் அதிகாரம் (இந்திய AG-க்கு இது கிடையாது)")],
        "correct_map": "a-1, b-2, c-3, d-4",
        "options_perms": [
            "a-1, b-2, c-3, d-4",
            "a-2, b-1, c-4, d-3",
            "a-3, b-4, c-1, d-2",
            "a-4, b-3, c-2, d-1"
        ],
        "exp_en": "Durante bene placito refers to pleasure tenure; Pre-audience is priority of speech; Amicus Curiae is friend of court; Nolle Prosequi is prosecutorial withdrawal power not available to Indian AG.",
        "exp_ta": "Durante bene placito என்பது விருப்பக் கோட்பாடு; Pre-audience என்பது முன்னுரிமை வாதாடல்; Amicus Curiae என்பது நீதிமன்ற நண்பர்; Nolle Prosequi என்பது இந்திய AG-க்கு இல்லாத தன்னிச்சை வழக்கு ரத்து அதிகாரம்.",
        "tip_en": "Latin legal terms frequently appear in TNPSC Group 1 questions testing constitutional jurisprudence.",
        "tip_ta": "TNPSC குரூப் 1 தேர்வுகளில் இத்தகைய லத்தீன் சட்ட கலைச்சொற்கள் அடிக்கடி கேட்கப்படுகின்றன.",
        "fact_en": "Section 321 CrPC replaces common law nolle prosequi with judicial supervision.",
        "fact_ta": "CrPC பிரிவு 321 காமன் லா nolle prosequi-க்கு பதிலாக நீதிமன்ற மேற்பார்வையை நிறுவுகிறது."
    },
    # 12: Tenure of Constitutional Functionaries
    {
        "subtopic": "Tenures of Constitutional Posts",
        "title_en": "Match List-I (Constitutional Post) with List-II (Prescribed Tenure / Security of Office):",
        "title_ta": "பட்டியல்-I-ஐ (அரசியலமைப்புப் பதவிகள்) பட்டியல்-II உடன் (நிர்ணயிக்கப்பட்ட பதவிக்காலம் / பணிப் பாதுகாப்பு) பொருத்துக:",
        "l1_en": [("a. Attorney General of India", "1. No fixed tenure (holds office during pleasure of President)"),
                  ("b. Comptroller and Auditor General", "2. 6 years or up to 65 years of age (whichever is earlier)"),
                  ("c. Supreme Court Judge", "3. Up to 65 years of age (impeachment by Parliament required for removal)"),
                  ("d. High Court Judge", "4. Up to 62 years of age (impeachment by Parliament required for removal)")],
        "l1_ta": [("a. இந்திய தலைமை வழக்கறிஞர்", "1. நிலையான பதவிக்காலம் இல்லை (குடியரசுத் தலைவரின் விருப்பம் வரை)"),
                  ("b. இந்திய தலைமை கணக்குத் தணிக்கையாளர் (CAG)", "2. 6 ஆண்டுகள் அல்லது 65 வயது வரை (எது முந்தையதோ அது)"),
                  ("c. உச்ச நீதிமன்ற நீதிபதி", "3. 65 வயது வரை (பதவி நீக்கத்திற்கு நாடாளுமன்ற சிறப்பு தீர்மானம் தேவை)"),
                  ("d. உயர் நீதிமன்ற நீதிபதி", "4. 62 வயது வரை (பதவி நீக்கத்திற்கு நாடாளுமன்ற சிறப்பு தீர்மானம் தேவை)")],
        "correct_map": "a-1, b-2, c-3, d-4",
        "options_perms": [
            "a-1, b-2, c-3, d-4",
            "a-2, b-1, c-4, d-3",
            "a-3, b-4, c-1, d-2",
            "a-4, b-3, c-2, d-1"
        ],
        "exp_en": "AG has no fixed tenure under Art 76(4); CAG has 6 yrs / 65 yrs under Art 148; SC Judge serves up to 65 yrs; HC Judge serves up to 62 yrs.",
        "exp_ta": "AG-க்கு நிலையான பதவிக்காலம் இல்லை (சரத்து 76(4)); CAG 6 ஆண்டுகள்/65 வயது; SC நீதிபதி 65 வயது வரை; HC நீதிபதி 62 வயது வரை பதவி வகிக்கின்றனர்.",
        "tip_en": "AG is the ONLY top constitutional authority among these who has NO security of tenure.",
        "tip_ta": "இப்பதவிகளில் அரசியலமைப்பு பதவிக்காலப் பாதுகாப்பு இல்லாத ஒரே பதவி தலைமை வழக்கறிஞர் பதவி மட்டுமே.",
        "fact_en": "The absence of tenure security allows the Government to change its chief legal adviser at will.",
        "fact_ta": "பதவிக்கால பாதுகாப்பு இல்லாததால் அரசு தனது தலைமை சட்ட ஆலோசகரை விருப்பப்படி மாற்றிக் கொள்ள முடிகிறது."
    },
    # 13: Roles of Law Officers
    {
        "subtopic": "Roles of Law Officers",
        "title_en": "Match List-I (Law Officer Designation) with List-II (Primary Constitutional / Statutory Role):",
        "title_ta": "பட்டியல்-I-ஐ (சட்ட அதிகாரிகளின் பதவிகள்) பட்டியல்-II உடன் (முதன்மை அரசியலமைப்பு / சட்டப்பூர்வப் பணி) பொருத்துக:",
        "l1_en": [("a. Attorney General of India", "1. Chief legal adviser to Union Government under Article 76"),
                  ("b. Solicitor General of India", "2. Senior non-constitutional law officer assisting AG"),
                  ("c. Advocate General of State", "3. Chief legal adviser to State Government under Article 165"),
                  ("d. Public Prosecutor", "4. Statutory officer conducting criminal prosecution on behalf of the State")],
        "l1_ta": [("a. இந்திய தலைமை வழக்கறிஞர்", "1. சரத்து 76-ன் கீழ் மத்திய அரசின் தலைமைச் சட்ட ஆலோசகர்"),
                  ("b. இந்திய சொலிசிட்டர் ஜெனரல்", "2. AG-க்கு உதவும் மூத்த அரசியலமைப்பு சாரா சட்ட அதிகாரி"),
                  ("c. மாநில அட்வகேட் ஜெனரல்", "3. சரத்து 165-ன் கீழ் மாநில அரசின் தலைமைச் சட்ட ஆலோசகர்"),
                  ("d. அரசு வழக்கறிஞர் (Public Prosecutor)", "4. அரசின் சார்பில் குற்றவியல் வழக்குகளை நடத்தும் சட்டப்பூர்வ அதிகாரி")],
        "correct_map": "a-1, b-2, c-3, d-4",
        "options_perms": [
            "a-1, b-2, c-3, d-4",
            "a-3, b-4, c-1, d-2",
            "a-2, b-1, c-4, d-3",
            "a-4, b-2, c-1, d-3"
        ],
        "exp_en": "AG advises Union (Art 76); SG assists AG (executive post); Advocate General advises State (Art 165); Public Prosecutor conducts criminal trials (CrPC Sec 24).",
        "exp_ta": "AG மத்திய அரசுக்கு ஆலோசிக்கிறார் (சரத்து 76); SG அவருக்கு உதவுகிறார்; அட்வகேட் ஜெனரல் மாநிலத்திற்கு ஆலோசிக்கிறார் (சரத்து 165); அரசு வழக்கறிஞர் குற்றவியல் வழக்குகளை நடத்துகிறார் (CrPC பிரிவு 24).",
        "tip_en": "Know the distinct roles of AG, SG, Advocate General, and Public Prosecutor.",
        "tip_ta": "AG, SG, அட்வகேட் ஜெனரல் மற்றும் அரசு வழக்கறிஞரின் தனித்துவமான பணிகளை அறிந்து கொள்ளுங்கள்.",
        "fact_en": "Public Prosecutors are appointed under Section 24 of CrPC 1973 (now Section 18 of BNSS 2023).",
        "fact_ta": "அரசு வழக்கறிஞர்கள் குற்றவியல் நடைமுறைச் சட்டம் பிரிவு 24-ன் கீழ் நியமிக்கப்படுகிறார்கள்."
    },
    # 14: Restrictions on AG
    {
        "subtopic": "Limitations & Restrictions",
        "title_en": "Match List-I (Nature of Professional Legal Activity) with List-II (Permissibility for Attorney General under 1987 Rules):",
        "title_ta": "பட்டியல்-I-ஐ (தொழில்முறை சட்ட நடவடிக்கைகள்) பட்டியல்-II உடன் (1987 விதிகளின் கீழ் AG-க்கான அனுமதி நிலை) பொருத்துக:",
        "l1_en": [("a. Advising or holding brief against Government of India", "1. Absolutely prohibited without any exception"),
                  ("b. Defending an accused in criminal prosecution", "2. Prohibited without prior permission of Government of India"),
                  ("c. Accepting directorship in a company", "3. Prohibited without prior permission of Government of India"),
                  ("d. Private civil litigation not involving GoI", "4. Permitted without needing separate governmental sanction")],
        "l1_ta": [("a. இந்திய அரசுக்கு எதிராக ஆலோசிப்பது அல்லது வாதாடுவது", "1. எந்த விதிவிலக்கும் இன்றி முற்றிலும் தடை செய்யப்பட்டுள்ளது"),
                  ("b. குற்ற வழக்கில் குற்றம் சாட்டப்பட்டவருக்காக ஆஜராவது", "2. இந்திய அரசின் முன் அனுமதியின்றி தடை செய்யப்பட்டுள்ளது"),
                  ("c. ஒரு நிறுவனத்தின் இயக்குநர் பதவியை ஏற்பது", "3. இந்திய அரசின் முன் அனுமதியின்றி தடை செய்யப்பட்டுள்ளது"),
                  ("d. மத்திய அரசு தொடர்பில்லாத தனியார் சிவில் வழக்குகள்", "4. அரசின் தனி அனுமதி இன்றியே அனுமதிக்கப்படுகிறது")],
        "correct_map": "a-1, b-2, c-3, d-4",
        "options_perms": [
            "a-1, b-2, c-3, d-4",
            "a-2, b-1, c-4, d-3",
            "a-3, b-4, c-1, d-2",
            "a-4, b-3, c-2, d-1"
        ],
        "exp_en": "Briefs against GoI are strictly barred; criminal defense and company directorship require GoI permission; independent private civil litigation is allowed.",
        "exp_ta": "மத்திய அரசுக்கு எதிரான வழக்குகள் முற்றிலும் தடை செய்யப்பட்டுள்ளன; குற்றவியல் வழக்குகளில் ஆஜராவதும் நிறுவன இயக்குநர் பதவியும் அரசின் அனுமதிக்கு உட்பட்டவை; தனியார் சிவில் வழக்குகள் அனுமதிக்கப்படுகின்றன.",
        "tip_en": "AG is NOT debarred from private practice, but has conflict of interest restrictions.",
        "tip_ta": "AG தனியார் பயிற்சி செய்ய தடை இல்லை, ஆனால் நலன் முரண்பாட்டு கட்டுப்பாடுகள் உண்டு.",
        "fact_en": "Rule 8 of Law Officers Rules codifies these professional boundaries.",
        "fact_ta": "1987 சட்ட அதிகாரிகள் விதிகளின் விதி 8 இந்த தொழில்முறை வரம்புகளை வரையறுக்கிறது."
    },
    # 15: 21st Century AGs Succession
    {
        "subtopic": "21st Century AGs Succession",
        "title_en": "Match List-I (21st Century Attorneys General) with List-II (Period of Service as AG):",
        "title_ta": "பட்டியல்-I-ஐ (21-ஆம் நூற்றாண்டு தலைமை வழக்கறிஞர்கள்) பட்டியல்-II உடன் (அவர்கள் பதவி வகித்த காலம்) பொருத்துக:",
        "l1_en": [("a. G.E. Vahanvati", "1. 2009 to 2014"),
                  ("b. Mukul Rohatgi", "2. 2014 to 2017"),
                  ("c. K.K. Venugopal", "3. 2017 to 2022"),
                  ("d. R. Venkataramani", "4. 2022 to Present")],
        "l1_ta": [("a. ஜி.இ. வாகனவதி", "1. 2009 முதல் 2014 வரை"),
                  ("b. முகுல் ரோஹத்கி", "2. 2014 முதல் 2017 வரை"),
                  ("c. கே.கே. வேணுகோபால்", "3. 2017 முதல் 2022 வரை"),
                  ("d. ஆர். வெங்கடரமணி", "4. 2022 முதல் தற்போது வரை")],
        "correct_map": "a-1, b-2, c-3, d-4",
        "options_perms": [
            "a-1, b-2, c-3, d-4",
            "a-2, b-1, c-4, d-3",
            "a-3, b-4, c-1, d-2",
            "a-4, b-3, c-2, d-1"
        ],
        "exp_en": "G.E. Vahanvati served 2009-2014; Mukul Rohatgi served 2014-2017; K.K. Venugopal served 2017-2022; R. Venkataramani took charge in October 2022.",
        "exp_ta": "ஜி.இ. வாகனவதி 2009-2014; முகுல் ரோஹத்கி 2014-2017; கே.கே. வேணுகோபால் 2017-2022; ஆர். வெங்கடரமணி அக்டோபர் 2022 முதல் பணியாற்றி வருகிறார்.",
        "tip_en": "Recent AG sequence: Vahanvati (2009) -> Rohatgi (2014) -> Venugopal (2017) -> Venkataramani (2022).",
        "tip_ta": "சமீபத்திய AG வரிசை: வாகனவதி (2009) -> ரோஹத்கி (2014) -> வேணுகோபால் (2017) -> வெங்கடரமணி (2022).",
        "fact_en": "G.E. Vahanvati was the first Muslim Attorney General of India.",
        "fact_ta": "ஜி.இ. வாகனவதி இந்தியாவின் முதல் முஸ்லிம் தலைமை வழக்கறிஞர் ஆவார்."
    },
    # 16: Parts and Chapters
    {
        "subtopic": "Constitutional Location of Provisions",
        "title_en": "Match List-I (Article of the Constitution) with List-II (Part and Chapter where located):",
        "title_ta": "பட்டியல்-I-ஐ (அரசியலமைப்புச் சரத்து) பட்டியல்-II உடன் (அது அமைந்துள்ள பகுதி மற்றும் அத்தியாயம்) பொருத்துக:",
        "l1_en": [("a. Article 76", "1. Part V, Chapter I (The Executive)"),
                  ("b. Article 88", "2. Part V, Chapter II (Parliament - General Provisions)"),
                  ("c. Article 105", "3. Part V, Chapter II (Parliament - Powers & Privileges)"),
                  ("d. Article 143", "4. Part V, Chapter IV (The Union Judiciary)")],
        "l1_ta": [("a. சரத்து 76", "1. பகுதி V, அத்தியாயம் I (மத்திய நிர்வாகம்)"),
                  ("b. சரத்து 88", "2. பகுதி V, அத்தியாயம் II (நாடாளுமன்றம் - பொது விதிகள்)"),
                  ("c. சரத்து 105", "3. பகுதி V, அத்தியாயம் II (நாடாளுமன்றம் - அதிகாரங்கள் மற்றும் சலுகைகள்)"),
                  ("d. சரத்து 143", "4. பகுதி V, அத்தியாயம் IV (மத்திய நீதித்துறை)")],
        "correct_map": "a-1, b-2, c-3, d-4",
        "options_perms": [
            "a-1, b-2, c-3, d-4",
            "a-2, b-1, c-4, d-3",
            "a-3, b-4, c-1, d-2",
            "a-4, b-3, c-2, d-1"
        ],
        "exp_en": "All these articles reside in Part V (The Union): Art 76 in Chapter I; Arts 88 & 105 in Chapter II; Art 143 in Chapter IV.",
        "exp_ta": "இவை அனைத்தும் பகுதி V-ல் (ஒன்றியம்) உள்ளன: சரத்து 76 அத்தியாயம் I; சரத்து 88 & 105 அத்தியாயம் II; சரத்து 143 அத்தியாயம் IV.",
        "tip_en": "Part V contains Union executive (Ch I), Parliament (Ch II), Legislative powers of President (Ch III), Union judiciary (Ch IV), CAG (Ch V).",
        "tip_ta": "பகுதி V-ல் நிர்வாகம் (I), நாடாளுமன்றம் (II), அவசரச் சட்டம் (III), நீதித்துறை (IV), CAG (V) ஆகியவை உள்ளன.",
        "fact_en": "Article 76 is the sole article dedicated entirely to the Attorney General of India.",
        "fact_ta": "சரத்து 76 தலைமை வழக்கறிஞருக்காக மட்டுமே முழுமையாக ஒதுக்கப்பட்ட ஒரே சரத்தாகும்."
    },
    # 17: Legal Advice and Consultation Articles
    {
        "subtopic": "Articles on Advice & Consultation",
        "title_en": "Match List-I (Article relating to Advice) with List-II (Nature of Constitutional Advice / Consultation):",
        "title_ta": "பட்டியல்-I-ஐ (ஆலோசனை தொடர்பான சரத்துகள்) பட்டியல்-II உடன் (அரசியலமைப்பு ஆலோசனை / கலந்தாலோசனையின் தன்மை) பொருத்துக:",
        "l1_en": [("a. Article 74(1)", "1. Council of Ministers to aid and advise the President (binding advice)"),
                  ("b. Article 76(2)", "2. Attorney General to give advice to Government of India on legal matters"),
                  ("c. Article 143(1)", "3. Power of President to consult Supreme Court on questions of law/fact"),
                  ("d. Article 163(1)", "4. Council of Ministers to aid and advise the Governor of a State")],
        "l1_ta": [("a. சரத்து 74(1)", "1. குடியரசுத் தலைவருக்கு உதவவும் ஆலோசிக்கவும் மத்திய அமைச்சரவை (கட்டுப்படுத்தும் ஆலோசனை)"),
                  ("b. சரத்து 76(2)", "2. இந்திய அரசுக்கு சட்ட விவகாரங்களில் தலைமை வழக்கறிஞர் வழங்கும் ஆலோசனை"),
                  ("c. சரத்து 143(1)", "3. சட்டம்/உண்மை வினாக்களில் குடியரசுத் தலைவர் உச்ச நீதிமன்றத்தைக் கலந்தாலோசித்தல்"),
                  ("d. சரத்து 163(1)", "4. மாநில ஆளுநருக்கு உதவவும் ஆலோசிக்கவும் மாநில அமைச்சரவை")],
        "correct_map": "a-1, b-2, c-3, d-4",
        "options_perms": [
            "a-1, b-2, c-3, d-4",
            "a-2, b-1, c-4, d-3",
            "a-3, b-4, c-1, d-2",
            "a-4, b-3, c-2, d-1"
        ],
        "exp_en": "Article 74 is Cabinet advice to President; Article 76(2) is AG advice to Government; Article 143 is Presidential reference to SC; Article 163 is Cabinet advice to Governor.",
        "exp_ta": "சரத்து 74 குடியரசுத் தலைவருக்கு அமைச்சரவை ஆலோசனை; சரத்து 76(2) அரசுக்கு AG ஆலோசனை; சரத்து 143 உச்ச நீதிமன்றக் குறிப்புரை; சரத்து 163 ஆளுநருக்கு அமைச்சரவை ஆலோசனை.",
        "tip_en": "Cabinet advice under Art 74 is binding on President; AG advice under Art 76 is NOT binding on Government.",
        "tip_ta": "சரத்து 74 அமைச்சரவை ஆலோசனை குடியரசுத் தலைவரைக் கட்டுப்படுத்தும்; சரத்து 76 AG ஆலோசனை அரசைக் கட்டுப்படுத்தாது.",
        "fact_en": "The 42nd Amendment Act 1976 made the advice of the Council of Ministers explicitly binding on the President.",
        "fact_ta": "1976-ல் 42-வது திருத்தச் சட்டம் அமைச்சரவையின் ஆலோசனையைக் குடியரசுத் தலைவர் மீது கட்டாயமாக்கியது."
    },
    # 18: Bar Backgrounds of AGs
    {
        "subtopic": "Bar Affiliations of AGs",
        "title_en": "Match List-I (Attorney General of India) with List-II (Parent Bar / Judicial Background):",
        "title_ta": "பட்டியல்-I-ஐ (இந்திய தலைமை வழக்கறிஞர்) பட்டியல்-II உடன் (அவர் பயிற்சி பெற்ற முதன்மை வழக்கறிஞர் மன்றம்) பொருத்துக:",
        "l1_en": [("a. M.C. Setalvad", "1. Bombay Bar (Advocate General of Bombay prior to 1950)"),
                  ("b. K. Parasaran", "2. Madras Bar (Advocate General of Tamil Nadu 1976-1977)"),
                  ("c. Soli Sorabjee", "3. Bombay Bar (Renowned constitutional expert and UN Rapporteur)"),
                  ("d. R. Venkataramani", "4. Madras Bar / Supreme Court Senior Advocate")],
        "l1_ta": [("a. எம்.சி. செடல்வாட்", "1. பம்பாய் பார் (1950-க்கு முன் பம்பாய் அட்வகேட் ஜெனரலாக இருந்தவர்)"),
                  ("b. கே. பராசரன்", "2. மதராஸ் பார் (1976-1977-ல் தமிழக அட்வகேட் ஜெனரலாக இருந்தவர்)"),
                  ("c. சோலி சொராப்ஜி", "3. பம்பாய் பார் (புகழ்பெற்ற அரசியலமைப்பு நிபுணர் & ஐ.நா. அறிக்கையாளர்)"),
                  ("d. ஆர். வெங்கடரமணி", "4. மதராஸ் பார் / உச்ச நீதிமன்ற மூத்த வழக்கறிஞர்")],
        "correct_map": "a-1, b-2, c-3, d-4",
        "options_perms": [
            "a-1, b-2, c-3, d-4",
            "a-2, b-1, c-4, d-3",
            "a-3, b-4, c-1, d-2",
            "a-4, b-3, c-2, d-1"
        ],
        "exp_en": "Setalvad and Sorabjee hailed from the Bombay Bar; K. Parasaran and R. Venkataramani originated from the Madras Bar.",
        "exp_ta": "செடல்வாட் மற்றும் சொராப்ஜி பம்பாய் பார் அசோசியேஷனையும்; கே. பராசரன் மற்றும் ஆர். வெங்கடரமணி மதராஸ் பார் அசோசியேஷனையும் பூர்வீகமாகக் கொண்டவர்கள்.",
        "tip_en": "Bombay and Madras bars produced the majority of India's most celebrated Attorneys General.",
        "tip_ta": "பம்பாய் மற்றும் மதராஸ் வழக்கறிஞர் மன்றங்களே இந்தியாவின் மிகச் சிறந்த தலைமை வழக்கறிஞர்களை உருவாக்கியுள்ளன.",
        "fact_en": "Both K. Parasaran and R. Venkataramani began their legal careers under legendary Madras jurists.",
        "fact_ta": "கே. பராசரன் மற்றும் ஆர். வெங்கடரமணி இருவரும் புகழ்பெற்ற மதராஸ் சட்ட நிபுணர்களின் கீழ் தங்களது சட்டப் பணியைத் தொடங்கினர்."
    },
    # 19: Law Commissions & Bodies
    {
        "subtopic": "Legal Institutions & AG Connection",
        "title_en": "Match List-I (Legal Institution / Body) with List-II (Specific Connection to Attorney General):",
        "title_ta": "பட்டியல்-I-ஐ (சட்ட அமைப்புகள்) பட்டியல்-II உடன் (தலைமை வழக்கறிஞருடனான குறிப்பிட்ட தொடர்பு) பொருத்துக:",
        "l1_en": [("a. First Law Commission (1955)", "1. Chaired by the first Attorney General, M.C. Setalvad"),
                  ("b. Bar Council of India", "2. Attorney General serves as permanent statutory ex-officio member"),
                  ("c. Central Agency Section", "3. Departmental unit coordinating Supreme Court litigation with AG"),
                  ("d. Department of Legal Affairs", "4. Nodal ministry department routing legal references to the AG")],
        "l1_ta": [("a. முதலாவது சட்ட ஆணையம் (1955)", "1. முதல் தலைமை வழக்கறிஞர் எம்.சி. செடல்வாட் தலைமையில் அமைக்கப்பட்டது"),
                  ("b. இந்திய பார் கவுன்சில்", "2. தலைமை வழக்கறிஞர் நிரந்தர பதவி வழி உறுப்பினராக உள்ளார்"),
                  ("c. மத்திய ஏஜென்சி பிரிவு (Central Agency)", "3. உச்ச நீதிமன்ற வழக்குகளை AG-யுடன் ஒருங்கிணைக்கும் துறைப் பிரிவு"),
                  ("d. சட்ட விவகாரங்கள் துறை", "4. AG-க்கான சட்டக் குறிப்புகளை அனுப்பும் முதன்மை அமைச்சகத் துறை")],
        "correct_map": "a-1, b-2, c-3, d-4",
        "options_perms": [
            "a-1, b-2, c-3, d-4",
            "a-2, b-1, c-4, d-3",
            "a-3, b-4, c-1, d-2",
            "a-4, b-3, c-2, d-1"
        ],
        "exp_en": "Setalvad chaired the 1st Law Commission; AG is ex-officio BCI member; Central Agency coordinates SC litigation; Dept of Legal Affairs routes references.",
        "exp_ta": "செடல்வாட் 1-வது சட்ட ஆணையத் தலைவராக இருந்தார்; AG பார் கவுன்சில் உறுப்பினர்; சென்ட்ரல் ஏஜென்சி SC வழக்குகளை ஒருங்கிணைக்கிறது; சட்ட விவகாரங்கள் துறை குறிப்புகளை அனுப்புகிறது.",
        "tip_en": "Central Agency Section is located within the Supreme Court compound to coordinate Union litigation.",
        "tip_ta": "மத்திய ஏஜென்சி பிரிவு உச்ச நீதிமன்ற வளாகத்தில் இயங்கி ஒன்றிய அரசு வழக்குகளை ஒருங்கிணைக்கிறது.",
        "fact_en": "The Central Agency Section was established in 1953.",
        "fact_ta": "மத்திய ஏஜென்சி பிரிவு 1953-ல் நிறுவப்பட்டது."
    },
    # 20: Advocates Act Sections
    {
        "subtopic": "Advocates Act Sections",
        "title_en": "Match List-I (Section of Advocates Act, 1961) with List-II (Subject Matter):",
        "title_ta": "பட்டியல்-I-ஐ (வழக்கறிஞர்கள் சட்டம் 1961-ன் பிரிவு) பட்டியல்-II உடன் (பொருள்) பொருத்துக:",
        "l1_en": [("a. Section 23", "1. Right of pre-audience of Attorney General, Solicitor General, and others"),
                  ("b. Section 4", "2. Composition of Bar Council of India with ex-officio law officers"),
                  ("c. Section 16", "3. Senior Advocates and other advocates classification"),
                  ("d. Section 35", "4. Punishment of advocates for professional or other misconduct")],
        "l1_ta": [("a. பிரிவு 23", "1. தலைமை வழக்கறிஞர், சொலிசிட்டர் ஜெனரல் ஆகியோரின் முதன்மை வழக்காடும் உரிமை"),
                  ("b. பிரிவு 4", "2. பதவி வழி சட்ட அதிகாரிகளுடன் கூடிய இந்திய பார் கவுன்சிலின் கட்டமைப்பு"),
                  ("c. பிரிவு 16", "3. மூத்த வழக்கறிஞர்கள் மற்றும் பிற வழக்கறிஞர்கள் வகைப்பாடு"),
                  ("d. பிரிவு 35", "4. வழக்கறிஞர்களின் தொழில்முறை தவறுகளுக்கான ஒழுங்கு நடவடிக்கை மற்றும் தண்டனை")],
        "correct_map": "a-1, b-2, c-3, d-4",
        "options_perms": [
            "a-1, b-2, c-3, d-4",
            "a-2, b-1, c-4, d-3",
            "a-3, b-4, c-1, d-2",
            "a-4, b-3, c-2, d-1"
        ],
        "exp_en": "Section 23 deals with pre-audience; Section 4 with BCI structure; Section 16 with senior advocate designation; Section 35 with disciplinary proceedings.",
        "exp_ta": "பிரிவு 23 முதன்மை வாதாடல்; பிரிவு 4 பார் கவுன்சில் கட்டமைப்பு; பிரிவு 16 மூத்த வழக்கறிஞர் அந்தஸ்து; பிரிவு 35 ஒழுங்கு நடவடிக்கைகள் பற்றியதாகும்.",
        "tip_en": "Section 23 is vital for Attorney General questions as it establishes the order of pre-audience.",
        "tip_ta": "பிரிவு 23 மிக முக்கியமானது, ஏனெனில் இதுவே தலைமை வழக்கறிஞரின் முதன்மை வாதாடும் உரிமையை வழங்குகிறது.",
        "fact_en": "Senior Advocates under Section 16 cannot file vakalatnama or appear without an instructing advocate.",
        "fact_ta": "பிரிவு 16-ன் கீழ் மூத்த வழக்கறிஞர்கள் மற்றொரு வழக்கறிஞர் இன்றி தனியாக வக்காலத்து தாக்கல் செய்ய முடியாது."
    },
    # 21: Removal Procedures Comparison
    {
        "subtopic": "Removal & Termination Procedures",
        "title_en": "Match List-I (Constitutional Office) with List-II (Removal Procedure):",
        "title_ta": "பட்டியல்-I-ஐ (அரசியலமைப்புப் பதவிகள்) பட்டியல்-II உடன் (பதவி நீக்க நடைமுறை) பொருத்துக:",
        "l1_en": [("a. Attorney General of India", "1. Removed by President at any time under pleasure doctrine (Art 76(4))"),
                  ("b. Judge of Supreme Court", "2. Removed by Presidential order after special majority address by Parliament (Art 124(4))"),
                  ("c. Comptroller and Auditor General", "3. Removed in like manner and on like grounds as a Supreme Court Judge (Art 148(1))"),
                  ("d. Chief Election Commissioner", "4. Removed in like manner and on like grounds as a Supreme Court Judge (Art 324(5))")],
        "l1_ta": [("a. இந்திய தலைமை வழக்கறிஞர்", "1. குடியரசுத் தலைவரால் எந்த நேரத்திலும் விருப்பக் கோட்பாட்டின் கீழ் நீக்கப்படுதல்"),
                  ("b. உச்ச நீதிமன்ற நீதிபதி", "2. நாடாளுமன்றத்தின் சிறப்புப் பெரும்பான்மை தீர்மானத்திற்குப் பின் நீக்கப்படுதல்"),
                  ("c. இந்திய தலைமை கணக்குத் தணிக்கையாளர்", "3. உச்ச நீதிமன்ற நீதிபதியை நீக்கும் அதே நடைமுறை மற்றும் காரணங்களின் அடிப்படையில்"),
                  ("d. தலைமைத் தேர்தல் ஆணையர்", "4. உச்ச நீதிமன்ற நீதிபதியை நீக்கும் அதே நடைமுறை மற்றும் காரணங்களின் அடிப்படையில்")],
        "correct_map": "a-1, b-2, c-3, d-4",
        "options_perms": [
            "a-1, b-2, c-3, d-4",
            "a-2, b-1, c-4, d-3",
            "a-3, b-4, c-1, d-2",
            "a-4, b-3, c-2, d-1"
        ],
        "exp_en": "AG holds office during pleasure of President; SC Judge, CAG, and CEC can only be removed by parliamentary address by special majority under Art 124(4).",
        "exp_ta": "AG குடியரசுத் தலைவரின் விருப்பப்படி நீக்கப்படுகிறார்; SC நீதிபதி, CAG மற்றும் CEC ஆகியோர் சரத்து 124(4)-ன் படி நாடாளுமன்ற சிறப்பு பெரும்பான்மை தீர்மானம் மூலமே நீக்கப்பட முடியும்.",
        "tip_en": "CAG and CEC share identical removal procedure with Supreme Court Judges; AG has NO removal procedure.",
        "tip_ta": "சிஏஜி மற்றும் சிஇசி உச்ச நீதிமன்ற நீதிபதியைப் போன்றே நீக்கப்படுகின்றனர்; AG-க்கு எந்த நடைமுறையும் தேவையில்லை.",
        "fact_en": "Security of tenure is deliberately denied to the AG to ensure alignment with the governing administration.",
        "fact_ta": "ஆளும் அரசுடன் இணக்கத்தை உறுதிப்படுத்தவே தலைமை வழக்கறிஞருக்கு பதவிக்கால பாதுகாப்பு வழங்கப்படவில்லை."
    },
    # 22: Landmark Cases & Issues
    {
        "subtopic": "Core Issues in AG Landmark Cases",
        "title_en": "Match List-I (Landmark Case argued by AG) with List-II (Core Constitutional Question Decided):",
        "title_ta": "பட்டியல்-I-ஐ (AG வாதிட்ட முக்கிய வழக்கு) பட்டியல்-II உடன் (தீர்மானிக்கப்பட்ட முதன்மை அரசியலமைப்பு வினா) பொருத்துக:",
        "l1_en": [("a. Shankari Prasad (1951)", "1. Constitutional amendments under Article 368 are not 'law' under Article 13(2)"),
                  ("b. Golaknath (1967)", "2. Fundamental rights are transcendental and Parliament cannot abridge them"),
                  ("c. Kesavananda Bharati (1973)", "3. Article 368 amending power cannot alter the Basic Structure of Constitution"),
                  ("d. Minerva Mills (1980)", "4. Directive Principles cannot be given absolute primacy over Fundamental Rights")],
        "l1_ta": [("a. சங்கரி பிரசாத் (1951)", "1. சரத்து 368-ன் கீழான அரசியலமைப்பு திருத்தங்கள் சரத்து 13(2)-ன் கீழ் 'சட்டம்' அல்ல"),
                  ("b. கோலாக்நாத் (1967)", "2. அடிப்படை உரிமைகள் மேலானவை; நாடாளுமன்றத்தால் அவற்றை குறைக்க முடியாது"),
                  ("c. கேசவானந்த பாரதி (1973)", "3. சரத்து 368 திருத்தும் அதிகாரம் அரசியலமைப்பின் அடிப்படைக் கட்டமைப்பை மாற்ற முடியாது"),
                  ("d. மினர்வா மில்ஸ் (1980)", "4. வழிகாட்டு நெறிமுறைகளுக்கு அடிப்படை உரிமைகளை விட முழுமையான முன்னுரிமை அளிக்க முடியாது")],
        "correct_map": "a-1, b-2, c-3, d-4",
        "options_perms": [
            "a-1, b-2, c-3, d-4",
            "a-2, b-1, c-4, d-3",
            "a-3, b-4, c-1, d-2",
            "a-4, b-3, c-2, d-1"
        ],
        "exp_en": "Shankari Prasad upheld 1st Amendment; Golaknath barred fundamental rights curtailment; Kesavananda created Basic Structure; Minerva Mills restored balance between Part III and Part IV.",
        "exp_ta": "சங்கரி பிரசாத் 1-வது திருத்தத்தை உறுதி செய்தது; கோலாக்நாத் உரிமைகள் குறைப்பைத் தடுத்தது; கேசவானந்தா அடிப்படைக் கட்டமைப்பை உருவாக்கியது; மினர்வா மில்ஸ் பகுதி III மற்றும் IV இடையேயான சமநிலையை மீட்டெடுத்தது.",
        "tip_en": "Follow the sequence: Shankari Prasad (1951) -> Golaknath (1967) -> Kesavananda (1973) -> Minerva Mills (1980).",
        "tip_ta": "வரிசையை நினைவில் வையுங்கள்: சங்கரி பிரசாத் (1951) -> கோலாக்நாத் (1967) -> கேசவானந்தா (1973) -> மினர்வா மில்ஸ் (1980).",
        "fact_en": "These four cases trace the entire evolution of judicial review over constitutional amendments in India.",
        "fact_ta": "இந்தியாவில் அரசியலமைப்பு திருத்தங்கள் மீதான நீதித்துறை மறுஆய்வின் முழுமையான பரிணாமத்தை இந்த நான்கு வழக்குகளும் விவரிக்கின்றன."
    },
    # 23: Legislative Participation
    {
        "subtopic": "Legislative Participation Rules",
        "title_en": "Match List-I (Constitutional Article) with List-II (Specific Rule on Legislative Participation / Voting):",
        "title_ta": "பட்டியல்-I-ஐ (அரசியலமைப்புச் சரத்து) பட்டியல்-II உடன் (சட்டமன்ற பங்கேற்பு / வாக்களிப்பு தொடர்பான விதி) பொருத்துக:",
        "l1_en": [("a. Article 88", "1. Attorney General has right to speak in Parliament but no right to vote"),
                  ("b. Article 100", "2. Voting in Houses of Parliament, power to act notwithstanding vacancies, and quorum"),
                  ("c. Article 177", "3. Advocate General has right to speak in State Legislature but no right to vote"),
                  ("d. Article 189", "4. Voting in Houses of State Legislature and quorum provisions")],
        "l1_ta": [("a. சரத்து 88", "1. நாடாளுமன்றத்தில் பேச AG-க்கு உரிமை உண்டு ஆனால் வாக்களிக்க உரிமை இல்லை"),
                  ("b. சரத்து 100", "2. நாடாளுமன்ற அவைகளில் வாக்கெடுப்பு, காலியிடங்கள் இருப்பினும் செயல்படும் அதிகாரம், கோரம்"),
                  ("c. சரத்து 177", "3. சட்டமன்றத்தில் பேச அட்வகேட் ஜெனரலுக்கு உரிமை உண்டு ஆனால் வாக்களிக்க உரிமை இல்லை"),
                  ("d. சரத்து 189", "4. மாநில சட்டமன்ற அவைகளில் வாக்கெடுப்பு மற்றும் கோரம் விதிகள்")],
        "correct_map": "a-1, b-2, c-3, d-4",
        "options_perms": [
            "a-1, b-2, c-3, d-4",
            "a-2, b-1, c-4, d-3",
            "a-3, b-4, c-1, d-2",
            "a-4, b-3, c-2, d-1"
        ],
        "exp_en": "Article 88 allows AG to speak without vote; Art 100 governs parliamentary voting; Art 177 allows Advocate General to speak without vote; Art 189 governs state legislative voting.",
        "exp_ta": "சரத்து 88 AG-க்கு வாக்கின்றி பேச உரிமை அளிக்கிறது; சரத்து 100 நாடாளுமன்ற வாக்கெடுப்பு; சரத்து 177 அட்வகேட் ஜெனரலுக்கு வாக்கின்றி பேச உரிமை அளிக்கிறது; சரத்து 189 சட்டமன்ற வாக்கெடுப்பு.",
        "tip_en": "Voting is governed by Art 100 (Centre) and Art 189 (State); Non-member speaking is Art 88 (Centre) and Art 177 (State).",
        "tip_ta": "வாக்கெடுப்பு: சரத்து 100 (மத்திய) மற்றும் 189 (மாநில); உறுப்பினரல்லாதோர் பேசுதல்: சரத்து 88 (மத்திய) மற்றும் 177 (மாநில).",
        "fact_en": "Article 88 and Article 177 are identical in text, adapted for the Union and States respectively.",
        "fact_ta": "சரத்து 88 மற்றும் சரத்து 177 ஆகியவை ஒன்றியம் மற்றும் மாநிலங்களுக்கான ஒத்த வாசகங்களைக் கொண்டுள்ளன."
    },
    # 24: Legal Terminology Latin Roots
    {
        "subtopic": "Legal Maxims in AG Practice",
        "title_en": "Match List-I (Legal Maxim / Latin Term) with List-II (Literal Meaning in Constitutional Law):",
        "title_ta": "பட்டியல்-I-ஐ (சட்டப் பழமொழிகள் / லத்தீன் சொற்கள்) பட்டியல்-II உடன் (அரசியலமைப்புச் சட்டத்தில் அதன் நேரடிப் பொருள்) பொருத்துக:",
        "l1_en": [("a. Audi alteram partem", "1. Listen to the other side (fundamental principle of natural justice)"),
                  ("b. Nemo judex in causa sua", "2. No one should be a judge in their own cause (rule against bias)"),
                  ("c. Locus standi", "3. Right or capacity to bring an action or appear before a court"),
                  ("d. Quo warranto", "4. Writ inquiring by what warrant or authority a person holds a public office")],
        "l1_ta": [("a. Audi alteram partem", "1. மறுதரப்பின் வாதத்தையும் கேட்க வேண்டும் (இயற்கை நீதியின் அடிப்படைக் கோட்பாடு)"),
                  ("b. Nemo judex in causa sua", "2. எவரும் தன் சொந்த வழக்கில் தானே நீதிபதியாக இருக்கக் கூடாது (சார்பற்ற தன்மை)"),
                  ("c. Locus standi", "3. நீதிமன்றத்தை அணுகுவதற்கான சட்டப்பூர்வ தகுதி அல்லது உரிமை"),
                  ("d. Quo warranto", "4. எந்த தகுதியின் அடிப்படையில் ஒரு பொதுப் பதவியை ஒருவர் வகிக்கிறார் என வினவும் பேராணை")],
        "correct_map": "a-1, b-2, c-3, d-4",
        "options_perms": [
            "a-1, b-2, c-3, d-4",
            "a-2, b-1, c-4, d-3",
            "a-3, b-4, c-1, d-2",
            "a-4, b-3, c-2, d-1"
        ],
        "exp_en": "Audi alteram partem means hear the other side; Nemo judex means no one is judge in their own case; Locus standi is standing to sue; Quo warranto tests right to hold public office.",
        "exp_ta": "Audi alteram partem என்பது இரு தரப்பும் கேட்கப்பட வேண்டும்; Nemo judex என்பது தன் வழக்கில் தானே நீதிபதி அல்ல; Locus standi என்பது நீதிமன்றம் செல்லும் தகுதி; Quo warranto என்பது தகுதி வினவும் பேராணை.",
        "tip_en": "A writ of Quo Warranto can be filed against an Attorney General if they lack prescribed constitutional qualifications.",
        "tip_ta": "அரசியலமைப்புத் தகுதிகள் இல்லாத ஒருவருக்கு எதிராக Quo Warranto பேராணை தாக்கல் செய்யப்படலாம்.",
        "fact_en": "The Supreme Court has entertained Quo Warranto petitions questioning appointments to high constitutional posts.",
        "fact_ta": "உயர் அரசியலமைப்புப் பதவி நியமனங்களை எதிர்த்து தொடரப்படும் Quo Warranto மனுக்களை உச்ச நீதிமன்றம் விசாரித்துள்ளது."
    },
    # 25: Chronological Decades of AGs
    {
        "subtopic": "Decades of Prominent Attorneys General",
        "title_en": "Match List-I (Decade) with List-II (Attorney General who Served Extensively in that Decade):",
        "title_ta": "பட்டியல்-I-ஐ (பத்தாண்டு காலம்) பட்டியல்-II உடன் (அக்காலகட்டத்தில் விரிவாகப் பணியாற்றிய தலைமை வழக்கறிஞர்) பொருத்துக:",
        "l1_en": [("a. 1950s", "1. M.C. Setalvad (1950–1963)"),
                  ("b. 1970s", "2. Niren De (1968–1977)"),
                  ("c. 1980s", "3. K. Parasaran (1983–1989)"),
                  ("d. 2010s", "4. K.K. Venugopal (2017–2022)")],
        "l1_ta": [("a. 1950-கள்", "1. எம்.சி. செடல்வாட் (1950–1963)"),
                  ("b. 1970-கள்", "2. நீரேன் டே (1968–1977)"),
                  ("c. 1980-கள்", "3. கே. பராசரன் (1983–1989)"),
                  ("d. 2010-கள்", "4. கே.கே. வேணுகோபால் (2017–2022)")],
        "correct_map": "a-1, b-2, c-3, d-4",
        "options_perms": [
            "a-1, b-2, c-3, d-4",
            "a-2, b-1, c-4, d-3",
            "a-3, b-4, c-1, d-2",
            "a-4, b-3, c-2, d-1"
        ],
        "exp_en": "Setalvad dominated the 1950s; Niren De the 1970s; K. Parasaran the 1980s; K.K. Venugopal the late 2010s.",
        "exp_ta": "1950-களில் செடல்வாட்; 1970-களில் நீரேன் டே; 1980-களில் கே. பராசரன்; 2010-களில் கே.கே. வேணுகோபால் முக்கியப் பங்காற்றினர்.",
        "tip_en": "Setalvad (1950s), Niren De (1970s), Parasaran (1980s), Venugopal (2010s).",
        "tip_ta": "செடல்வாட் (1950-கள்), நீரேன் டே (1970-கள்), பராசரன் (1980-கள்), வேணுகோபால் (2010-கள்).",
        "fact_en": "Each of these jurists left an indelible mark on Indian constitutional jurisprudence.",
        "fact_ta": "இந்த சட்ட மேதைகள் ஒவ்வொருவரும் இந்திய அரசியலமைப்புச் சட்ட வரலாற்றில் அழியாத முத்திரையைப் பதித்துள்ளனர்."
    }
]

def build_questions():
    questions = []
    
    for i, item in enumerate(raw_match_data):
        qid = f"AG_MF_{i+1:03d}"
        
        # Build stem
        stem_en_lines = [
            item["title_en"],
            "List-I:"
        ]
        for a, b in item["l1_en"]:
            stem_en_lines.append(f"{a}")
        stem_en_lines.append("List-II:")
        for a, b in item["l1_en"]:
            stem_en_lines.append(f"{b}")
            
        stem_ta_lines = [
            item["title_ta"],
            "பட்டியல்-I:"
        ]
        for a, b in item["l1_ta"]:
            stem_ta_lines.append(f"{a}")
        stem_ta_lines.append("பட்டியல்-II:")
        for a, b in item["l1_ta"]:
            stem_ta_lines.append(f"{b}")
            
        stem_en = "\n".join(stem_en_lines)
        stem_ta = "\n".join(stem_ta_lines)
        
        opts = item["options_perms"] # 4 permutations of matching code
        correct_key = "A" # initially index 0 is correct
        
        why_en = {}
        why_ta = {}
        for idx, key in enumerate(["A", "B", "C", "D"]):
            if idx == 0:
                why_en[key] = f"Option {key} ({opts[idx]}) correctly matches all four items in List-I with List-II."
                why_ta[key] = f"தெரிவு {key} ({opts[idx]}) பட்டியல்-I-ல் உள்ள நான்கு கூறுகளையும் பட்டியல்-II உடன் சரியாகப் பொருத்துகிறது."
            else:
                why_en[key] = f"Option {key} ({opts[idx]}) contains mismatched pairs."
                why_ta[key] = f"தெரிவு {key} ({opts[idx]}) தவறாகப் பொருத்தப்பட்ட இணைகளைக் கொண்டுள்ளது."
                
        q = make_ag_q(
            qid=qid,
            diff="Medium",
            qtype="Match the Following",
            subtopic=item["subtopic"],
            en_stem=stem_en,
            ta_stem=stem_ta,
            en_a=opts[0],
            ta_a=opts[0],
            en_b=opts[1],
            ta_b=opts[1],
            en_c=opts[2],
            ta_c=opts[2],
            en_d=opts[3],
            ta_d=opts[3],
            correct_key=correct_key,
            exp_en=item["exp_en"],
            exp_ta=item["exp_ta"],
            why_a_en=why_en["A"],
            why_a_ta=why_ta["A"],
            why_b_en=why_en["B"],
            why_b_ta=why_ta["B"],
            why_c_en=why_en["C"],
            why_c_ta=why_ta["C"],
            why_d_en=why_en["D"],
            why_d_ta=why_ta["D"],
            tip_en=item["tip_en"],
            tip_ta=item["tip_ta"],
            fact_en=item["fact_en"],
            fact_ta=item["fact_ta"],
            tags=["polity", "attorney_general_of_india", "match_the_following", item["subtopic"].lower().replace(" ", "_")]
        )
        questions.append(q)
        
    return questions

if __name__ == "__main__":
    qs = build_questions()
    print(f"Generated {len(qs)} raw Match the Following questions.")
    
    balanced_qs = balance_question_keys(qs)
    
    out_path = os.path.join("data", "questions", "polity", "attorney_general_match_the_following.json")
    alias_path = os.path.join("data", "questions", "polity", "attorney_general_match.json")
    
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(balanced_qs, f, ensure_ascii=False, indent=2)
    shutil.copyfile(out_path, alias_path)
    
    print(f"Saved balanced Match MCQs to {out_path} and {alias_path}")
    
    val = ContentValidator()
    report = val.validate_file(out_path, expected_count=25, expected_prefix="AG_MF_")
    print(f"Validation Report: {'PASS' if report.is_valid else 'FAIL'} | Total: {report.total_audited}")
    if not report.is_valid:
        for iss in report.issues[:10]:
            print(f"  Issue: {iss}")
    print(f"Key Distribution: {report.key_distribution}")
