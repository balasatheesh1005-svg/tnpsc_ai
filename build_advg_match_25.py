# -*- coding: utf-8 -*-
"""
Generator for Advocate General of a State Match the Following MCQs (25 Questions: ADVG_MF_001 to ADVG_MF_025).
Strictly adheres to:
- Full 24-field TNPSC Nova AI schema
- Balanced answer keys (7 A, 6 B, 6 C, 6 D)
- Fully bilingual (English and authentic Tamil)
- Standard List-I and List-II matching format
"""

import json
import os
import shutil
from advg_mcq_helper import make_advg_q
from rebalance_er_helper import balance_question_keys
from tools.nova_content_engine.validator import ContentValidator

raw_match_data = [
    # 1: Constitutional Articles Part 1
    {
        "subtopic": "Constitutional Articles",
        "title_en": "Match List-I (Constitutional Articles) with List-II (Provisions concerning Advocate General of the State) and select the correct code:",
        "title_ta": "பட்டியல்-I-ஐ (அரசியலமைப்புச் சரத்துகள்) பட்டியல்-II உடன் (மாநில அட்வகேட் ஜெனரல் தொடர்பான விதிகள்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "l1_en": [("a. Article 165(1)", "1. Appointment and qualifications of the Advocate General"),
                  ("b. Article 165(2)", "2. Constitutional duties to advise the State Government on legal matters"),
                  ("c. Article 165(3)", "3. Tenure during pleasure of Governor and remuneration determined by Governor"),
                  ("d. Article 177", "4. Rights to speak and participate in the proceedings of the State Legislature")],
        "l1_ta": [("a. சரத்து 165(1)", "1. அட்வகேட் ஜெனரலின் நியமனம் மற்றும் தகுதிகள்"),
                  ("b. சரத்து 165(2)", "2. சட்ட விவகாரங்களில் மாநில அரசுக்கு ஆலோசனையளிக்கும் அரசியலமைப்பு கடமைகள்"),
                  ("c. சரத்து 165(3)", "3. ஆளுநரின் விருப்பம் உள்ளவரை பதவி வகித்தல் மற்றும் ஆளுநரால் ஊதியம் நிர்ணயிக்கப்படுதல்"),
                  ("d. சரத்து 177", "4. மாநில சட்டமன்ற நடவடிக்கைகளில் பேசவும் பங்கேற்கவும் உள்ள உரிமைகள்")],
        "correct_map": "a-1, b-2, c-3, d-4",
        "options_perms": [
            "a-1, b-2, c-3, d-4",
            "a-2, b-1, c-4, d-3",
            "a-3, b-4, c-1, d-2",
            "a-4, b-3, c-2, d-1"
        ],
        "exp_en": "Article 165(1) governs appointment; 165(2) outlines legal duties; 165(3) deals with tenure at Governor's pleasure and remuneration; Article 177 gives the right to speak in State Legislature without voting rights.",
        "exp_ta": "சரத்து 165(1) நியமனத்தை நிர்வகிக்கிறது; 165(2) சட்டக் கடமைகளை வரையறுக்கிறது; 165(3) ஆளுநரின் விருப்பப்படி பதவிக்காலம் மற்றும் ஊதியத்தைக் குறிக்கிறது; சரத்து 177 வாக்களிக்கும் உரிமையின்றி சட்டமன்றத்தில் பேசும் உரிமையை வழங்குகிறது.",
        "tip_en": "Remember Article 165 has 3 distinct clauses: (1) Appointment/Qualifications, (2) Duties, (3) Tenure/Remuneration.",
        "tip_ta": "சரத்து 165-ல் 3 தனித்தனி பிரிவுகள் உள்ளன: (1) நியமனம்/தகுதிகள், (2) கடமைகள், (3) பதவிக்காலம்/ஊதியம்.",
        "fact_en": "Article 165 is the primary constitutional anchor for the Advocate General of a State.",
        "fact_ta": "சரத்து 165 மாநில அட்வகேட் ஜெனரலுக்கான முதன்மை அரசியலமைப்பு அடிப்படையாகும்."
    },
    # 2: Union vs State Parallel Provisions
    {
        "subtopic": "Union vs State Constitutional Parallels",
        "title_en": "Match List-I (Office of Attorney General of India) with List-II (Parallel Office of Advocate General of a State):",
        "title_ta": "பட்டியல்-I-ஐ (இந்திய தலைமை வழக்கறிஞர் அலுவலகம்) பட்டியல்-II உடன் (மாநில அட்வகேட் ஜெனரல் அலுவலக இணை விதிகள்) பொருத்துக:",
        "l1_en": [("a. Article 76(1) [Appointed by President]", "1. Article 165(1) [Appointed by Governor]"),
                  ("b. Article 88 [Right to speak in Parliament]", "2. Article 177 [Right to speak in State Legislature]"),
                  ("c. Article 105(4) [Privileges of an MP]", "3. Article 194(4) [Privileges of an MLA]"),
                  ("d. Qualified to be Supreme Court Judge", "4. Qualified to be High Court Judge")],
        "l1_ta": [("a. சரத்து 76(1) [குடியரசுத் தலைவரால் நியமனம்]", "1. சரத்து 165(1) [ஆளுநரால் நியமனம்]"),
                  ("b. சரத்து 88 [நாடாளுமன்றத்தில் பேசும் உரிமை]", "2. சரத்து 177 [மாநில சட்டமன்றத்தில் பேசும் உரிமை]"),
                  ("c. சரத்து 105(4) [நாடாளுமன்ற உறுப்பினர் சலுகைகள்]", "3. சரத்து 194(4) [சட்டமன்ற உறுப்பினர் சலுகைகள்]"),
                  ("d. உச்ச நீதிமன்ற நீதிபதிக்கான தகுதி", "4. உயர் நீதிமன்ற நீதிபதிக்கான தகுதி")],
        "correct_map": "a-1, b-2, c-3, d-4",
        "options_perms": [
            "a-1, b-2, c-3, d-4",
            "a-2, b-1, c-4, d-3",
            "a-4, b-3, c-2, d-1",
            "a-3, b-4, c-1, d-2"
        ],
        "exp_en": "The parallel provisions follow the '+89 rule': Art 76 + 89 = Art 165; Art 88 + 89 = Art 177; Art 105 + 89 = Art 194; qualification is SC judge vs HC judge.",
        "exp_ta": "+89 விதிப்படி: சரத்து 76 + 89 = சரத்து 165; சரத்து 88 + 89 = சரத்து 177; சரத்து 105 + 89 = சரத்து 194; தகுதி உச்ச நீதிமன்ற நீதிபதி vs உயர் நீதிமன்ற நீதிபதி.",
        "tip_en": "Add 89 to Union constitutional articles (76, 88, 105) to get corresponding State articles (165, 177, 194).",
        "tip_ta": "ஒன்றிய சரத்துகளுடன் 89-ஐக் கூட்டினால் (76, 88, 105) தொடர்புடைய மாநில சரத்துகள் (165, 177, 194) கிடைக்கும்.",
        "fact_en": "Both AG and Advocate General hold office during the pleasure of their respective appointing executives.",
        "fact_ta": "இருவருமே தங்களை நியமிக்கும் நிர்வாகத் தலைவரின் விருப்பம் உள்ளவரையே பதவியில் நீடிக்கின்றனர்."
    },
    # 3: Statutory Provisions
    {
        "subtopic": "Statutory Powers and Functions",
        "title_en": "Match List-I (Statutes and Sections) with List-II (Statutory Functions of the Advocate General):",
        "title_ta": "பட்டியல்-I-ஐ (சட்டங்கள் மற்றும் பிரிவுகள்) பட்டியல்-II உடன் (அட்வகேட் ஜெனரலின் சட்டப்பூர்வ பணிகள்) பொருத்துக:",
        "l1_en": [("a. Section 23(2), Advocates Act, 1961", "1. Statutory right of pre-audience over all advocates in the State"),
                  ("b. Section 15(1)(b), Contempt of Courts Act, 1971", "2. Granting written consent for criminal contempt motions in High Court"),
                  ("c. Section 91, Code of Civil Procedure, 1908", "3. Instituting civil suit or granting consent for public nuisance"),
                  ("d. Section 301, Code of Criminal Procedure, 1973", "4. Appearance and conduct of prosecution in criminal courts without written authority")],
        "l1_ta": [("a. பிரிவு 23(2), வழக்கறிஞர்கள் சட்டம், 1961", "1. மாநிலத்தில் உள்ள அனைத்து வழக்கறிஞர்களையும் விட முதன்மை வழக்காடும் சட்டப்பூர்வ உரிமை"),
                  ("b. பிரிவு 15(1)(b), நீதிமன்ற அவமதிப்புச் சட்டம், 1971", "2. உயர் நீதிமன்ற குற்றவியல் அவமதிப்பு மனுக்களுக்கு எழுத்துப்பூர்வ ஒப்புதல் அளித்தல்"),
                  ("c. பிரிவு 91, உரிமையியல் நடைமுறைச் சட்டம், 1908", "3. பொதுத்தொல்லை தொடர்பாக வழக்கு தொடருதல் அல்லது ஒப்புதல் அளித்தல்"),
                  ("d. பிரிவு 301, குற்றவியல் நடைமுறைச் சட்டம், 1973", "4. குற்றவியல் நீதிமன்றங்களில் எழுத்துப்பூர்வ அதிகாரமின்றி முன்னிலையாகி அரசு வழக்கை நடத்துதல்")],
        "correct_map": "a-1, b-2, c-3, d-4",
        "options_perms": [
            "a-1, b-2, c-3, d-4",
            "a-3, b-4, c-1, d-2",
            "a-2, b-1, c-4, d-3",
            "a-4, b-2, c-1, d-3"
        ],
        "exp_en": "Section 23(2) gives Advocate General pre-audience; Section 15(1)(b) mandates AG consent for criminal contempt; Section 91 CPC empowers AG for public nuisance; Section 301 CrPC permits appearance without formal vakalatnama.",
        "exp_ta": "வழக்கறிஞர்கள் சட்டம் பிரிவு 23(2) முதன்மை வாதாடும் உரிமையையும்; அவமதிப்புச் சட்டம் பிரிவு 15(1)(b) குற்றவியல் அவமதிப்பு ஒப்புதலையும்; CPC பிரிவு 91 பொதுத்தொல்லை வழக்கையும்; CrPC பிரிவு 301 வக்காலத்து இன்றி முன்னிலையாகும் அதிகாரத்தையும் வழங்குகிறது.",
        "tip_en": "Remember the key sections: Advocates Act Sec 23, Contempt Act Sec 15, CPC Sec 91/92, CrPC Sec 301/302.",
        "tip_ta": "முக்கிய பிரிவுகள்: வழக்கறிஞர்கள் சட்டம் பிரிவு 23, அவமதிப்புச் சட்டம் பிரிவு 15, CPC பிரிவு 91/92, CrPC பிரிவு 301/302.",
        "fact_en": "Advocate General exercises both constitutional advisory powers and statutory prosecutorial/supervisory powers.",
        "fact_ta": "அட்வகேட் ஜெனரல் அரசியலமைப்பு ஆலோசனை அதிகாரங்களையும் சட்டப்பூர்வ கண்காணிப்பு அதிகாரங்களையும் கொண்டுள்ளார்."
    },
    # 4: Landmark Judgments
    {
        "subtopic": "Landmark Judgments",
        "title_en": "Match List-I (Landmark Judicial Cases) with List-II (Core Legal Rulings regarding Advocate General):",
        "title_ta": "பட்டியல்-I-ஐ (முக்கிய தீர்ப்பு வழக்குகள்) பட்டியல்-II உடன் (அட்வகேட் ஜெனரல் தொடர்பான முக்கிய சட்டத் தீர்ப்புகள்) பொருத்துக:",
        "l1_en": [("a. G.D. Karkare v. T.L. Shevde (1952)", "1. Age limit of 62 years applies to HC judges, not to eligibility of Advocate General"),
                  ("b. M.T. Khan v. Govt. of A.P. (2004)", "2. Article 165 permits only one Advocate General; Additional AG is not a constitutional post"),
                  ("c. P.N. Duda v. P. Shiv Shanker (1988)", "3. Power to grant consent under Contempt of Courts Act is quasi-judicial and cannot be compelled by Mandamus"),
                  ("d. State of UP v. UP Law Officers Assn (1994)", "4. Office of Advocate General is a public trust, not a mere client-lawyer relationship")],
        "l1_ta": [("a. ஜி.டி. கார்கரே எதிர் டி.எல். ஷேவ்டே (1952)", "1. 62 வயது வரம்பு உயர் நீதிமன்ற நீதிபதிகளுக்கு மட்டுமே பொருந்தும், அட்வகேட் ஜெனரலுக்கு அல்ல"),
                  ("b. எம்.டி. கான் எதிர் ஆந்திர அரசு (2004)", "2. சரத்து 165 ஒரே ஒரு அட்வகேட் ஜெனரலை மட்டுமே அனுமதிக்கிறது; கூடுதல் AG அரசியலமைப்பு பதவி அல்ல"),
                  ("c. பி.என். தூடா எதிர் பி. சிவ சங்கர் (1988)", "3. அவமதிப்பு சட்டத்தில் ஒப்புதல் அளிக்கும் அதிகாரம் நீதித்துறை போன்றது; கட்டளை நீதிப்பேராணை பிறப்பிக்க முடியாது"),
                  ("d. உ.பி. அரசு எதிர் உ.பி. சட்ட அதிகாரிகள் சங்கம் (1994)", "4. அட்வகேட் ஜெனரல் பதவி பொது நம்பிக்கைக்குரிய பொது அலுவலகம், வெறும் வாடிக்கையாளர் உறவு அல்ல")],
        "correct_map": "a-1, b-2, c-3, d-4",
        "options_perms": [
            "a-1, b-2, c-3, d-4",
            "a-2, b-1, c-4, d-3",
            "a-3, b-4, c-1, d-2",
            "a-4, b-3, c-2, d-1"
        ],
        "exp_en": "G.D. Karkare settled the 62-year age limit; M.T. Khan held only one constitutional AG exists per State; P.N. Duda held contempt consent is quasi-judicial; UP Law Officers established public trust nature of law officers.",
        "exp_ta": "கார்கரே வழக்கு 62 வயது வரம்பைத் தீர்த்தது; எம்.டி. கான் ஒரு மாநிலத்திற்கு ஒரு AG மட்டுமே அரசியலமைப்பு பதவி என்றது; தூடா அவமதிப்பு ஒப்புதல் நீதி போன்றது என்றது; உ.பி. வழக்கு பொது நம்பிக்கை இயல்பை நிறுவியது.",
        "tip_en": "Karkare = Age limit not applicable; M.T. Khan = Only one AG; Duda = Contempt quasi-judicial.",
        "tip_ta": "கார்கரே = வயது வரம்பு பொருந்தாது; எம்.டி. கான் = ஒரு AG மட்டுமே; தூடா = அவமதிப்பு ஒப்புதல் quasi-judicial.",
        "fact_en": "Nagpur HC judgment in Karkare was later affirmed by the Supreme Court in Atlas Cycle (1962).",
        "fact_ta": "கார்கரே வழக்கில் நாக்பூர் உயர் நீதிமன்ற தீர்ப்பை பின்னர் 1962-ல் உச்ச நீதிமன்றம் உறுதி செய்தது."
    },
    # 5: State Law Officers Hierarchy
    {
        "subtopic": "State Law Officers and Structure",
        "title_en": "Match List-I (Designation of State Law Officers) with List-II (Nature and Character of their Post):",
        "title_ta": "பட்டியல்-I-ஐ (மாநில சட்ட அதிகாரிகள் பதவிப்பெயர்) பட்டியல்-II உடன் (பதவியின் தன்மை மற்றும் இயல்பு) பொருத்துக:",
        "l1_en": [("a. Advocate General of the State", "1. Sole Constitutional Law Officer under Article 165"),
                  ("b. Additional Advocate General", "2. Statutory / Executive appointment under Article 162 executive power"),
                  ("c. Government Pleader", "3. Officer appointed to represent the State in civil proceedings"),
                  ("d. Public Prosecutor", "4. Officer appointed under Section 24 of CrPC for criminal prosecutions")],
        "l1_ta": [("a. மாநில அட்வகேட் ஜெனரல்", "1. சரத்து 165-ன் கீழ் உள்ள ஒரே அரசியலமைப்பு சட்ட அதிகாரி"),
                  ("b. கூடுதல் அட்வகேட் ஜெனரல்", "2. சரத்து 162 நிர்வாக அதிகாரத்தின் கீழ் செய்யப்படும் நிர்வாக/சட்டப்பூர்வ நியமனம்"),
                  ("c. அரசு வழக்கறிஞர் (Government Pleader)", "3. உரிமையியல் வழக்குகளில் மாநில அரசைப் பிரதிநிதித்துவப்படுத்த நியமிக்கப்படும் அதிகாரி"),
                  ("d. அரசு குற்றவியல் வழக்கறிஞர் (Public Prosecutor)", "4. குற்றவியல் வழக்குகளுக்காக CrPC பிரிவு 24-ன் கீழ் நியமிக்கப்படும் அதிகாரி")],
        "correct_map": "a-1, b-2, c-3, d-4",
        "options_perms": [
            "a-1, b-2, c-3, d-4",
            "a-2, b-1, c-4, d-3",
            "a-3, b-4, c-1, d-2",
            "a-4, b-3, c-2, d-1"
        ],
        "exp_en": "Advocate General is constitutional under Art 165; Additional AG is executive under Art 162; Government Pleader handles civil side; Public Prosecutor is under Sec 24 CrPC.",
        "exp_ta": "அட்வகேட் ஜெனரல் சரத்து 165-ன் கீழ் அரசியலமைப்பு அதிகாரி; கூடுதல் AG சரத்து 162 நிர்வாக நியமனம்; அரசு பிளீடர் சிவில் வழக்குகளைக் கவனிக்கிறார்; பப்ளிக் பிராசிகியூட்டர் CrPC 24-ன் கீழ் வருகிறார்.",
        "tip_en": "Only the Advocate General is a constitutional authority in the State; all other law officers are non-constitutional.",
        "tip_ta": "மாநிலத்தில் அட்வகேட் ஜெனரல் மட்டுமே அரசியலமைப்பு அதிகாரி; பிற அனைத்து சட்ட அதிகாரிகளும் அரசியலமைப்பு அந்தஸ்தற்றவர்கள்.",
        "fact_en": "M.T. Khan (2004) explicitly ruled that Additional Advocate General is not governed by Article 165.",
        "fact_ta": "கூடுதல் அட்வகேட் ஜெனரல் பதவி சரத்து 165-ன் கீழ் வராது என்று எம்.டி. கான் (2004) வழக்கில் திட்டவட்டமாக தீர்ப்பளிக்கப்பட்டது."
    },
    # 6: Pre-Audience Hierarchy under Section 23 Advocates Act
    {
        "subtopic": "Advocates Act and Pre-Audience",
        "title_en": "Match List-I (Order of Pre-Audience under Section 23 of Advocates Act, 1961) with List-II (Designated Law Officers):",
        "title_ta": "பட்டியல்-I-ஐ (வழக்கறிஞர்கள் சட்டம் 1961 பிரிவு 23-ன் கீழ் முதன்மை வாதாடும் வரிசை) பட்டியல்-II உடன் (சட்ட அதிகாரிகள்) பொருத்துக:",
        "l1_en": [("a. First Rank in Pre-Audience", "1. Attorney General of India"),
                  ("b. Second Rank in Pre-Audience", "2. Solicitor General of India"),
                  ("c. Third Rank in Pre-Audience", "3. Additional Solicitor General of India"),
                  ("d. Fourth Rank (Rank 1 within own State Courts)", "4. Advocate General of the respective State")],
        "l1_ta": [("a. முதன்மை வாதாடலில் முதல் இடம்", "1. இந்திய தலைமை வழக்கறிஞர் (Attorney General)"),
                  ("b. முதன்மை வாதாடலில் இரண்டாம் இடம்", "2. இந்திய சொலிசிட்டர் ஜெனரல்"),
                  ("c. முதன்மை வாதாடலில் மூன்றாம் இடம்", "3. இந்திய கூடுதல் சொலிசிட்டர் ஜெனரல்"),
                  ("d. நான்காம் இடம் (தனது மாநில நீதிமன்றங்களில் முதல் இடம்)", "4. அந்தந்த மாநில அட்வகேட் ஜெனரல்")],
        "correct_map": "a-1, b-2, c-3, d-4",
        "options_perms": [
            "a-1, b-2, c-3, d-4",
            "a-2, b-1, c-4, d-3",
            "a-4, b-3, c-2, d-1",
            "a-3, b-4, c-1, d-2"
        ],
        "exp_en": "Under Section 23 of Advocates Act: AG has pre-audience over all; Solicitor General is second; Addl SG is third; Advocate General ranks fourth in Supreme Court, but ranks FIRST over all advocates in courts of his own State.",
        "exp_ta": "வழக்கறிஞர்கள் சட்டம் பிரிவு 23-ன் கீழ்: AG முதலிடம்; சொலிசிட்டர் ஜெனரல் இரண்டாமிடம்; கூடுதல் SG மூன்றாமிடம்; அட்வகேட் ஜெனரல் உச்ச நீதிமன்றத்தில் 4-வது இடமும், தனது சொந்த மாநில நீதிமன்றங்களில் முதலிடமும் வகிக்கிறார்.",
        "tip_en": "Within State High Court: Advocate General of that State has the highest pre-audience over Senior Advocates and other State AGs.",
        "tip_ta": "மாநில உயர் நீதிமன்றத்தில்: அந்த மாநில அட்வகேட் ஜெனரல் அனைத்து மூத்த வழக்கறிஞர்களை விடவும் முதன்மை வாதாடும் உரிமை கொண்டவர்.",
        "fact_en": "Section 23(2) gives Advocate General pre-audience over all advocates in the State.",
        "fact_ta": "பிரிவு 23(2) மாநில அட்வகேட் ஜெனரலுக்கு மாநிலத்தில் உள்ள அனைத்து வழக்கறிஞர்களை விடவும் முதன்மை வாதாடும் உரிமையை அளிக்கிறது."
    },
    # 7: Historical Evolution of Madras Advocate General
    {
        "subtopic": "Madras Presidency Legal History",
        "title_en": "Match List-I (Distinguished Historic Advocates General of Madras) with List-II (Their Notable Milestone or Contribution):",
        "title_ta": "பட்டியல்-I-ஐ (மெட்ராஸின் புகழ்பெற்ற வரலாற்று அட்வகேட் ஜெனரல்கள்) பட்டியல்-II உடன் (அவர்களின் குறிப்பிடத்தக்க சாதனை அல்லது பங்களிப்பு) பொருத்துக:",
        "l1_en": [("a. Sir V. Bhashyam Aiyangar", "1. First Indian Advocate General of Madras (appointed in 1899/1900)"),
                  ("b. Sir P.S. Sivaswami Iyer", "2. Advocate General of Madras (1907-1912) and distinguished educationist"),
                  ("c. S. Srinivasa Iyengar", "3. Renowned Advocate General (1916-1920) who later resigned and joined Congress"),
                  ("d. K. Rajah Iyer", "4. First Advocate General of Madras State in independent India (1947-1950)")],
        "l1_ta": [("a. சர் வி. பாஷ்யம் ஐயங்கார்", "1. மெட்ராஸின் முதல் இந்திய அட்வகேட் ஜெனரல் (1899/1900-ல் நியமனம்)"),
                  ("b. சர் பி.எஸ். சிவசுவாமி ஐயர்", "2. மெட்ராஸ் அட்வகேட் ஜெனரல் (1907-1912) மற்றும் சிறந்த கல்வியாளர்"),
                  ("c. எஸ். சீனிவாச ஐயங்கார்", "3. புகழ்பெற்ற அட்வகேட் ஜெனரல் (1916-1920), பின் பதவியை ராஜினாமா செய்து காங்கிரஸில் சேர்ந்தவர்"),
                  ("d. கே. ராஜா ஐயர்", "4. சுதந்திர இந்தியாவின் மெட்ராஸ் மாநிலத்தின் முதல் அட்வகேட் ஜெனரல் (1947-1950)")],
        "correct_map": "a-1, b-2, c-3, d-4",
        "options_perms": [
            "a-1, b-2, c-3, d-4",
            "a-2, b-1, c-4, d-3",
            "a-3, b-4, c-1, d-2",
            "a-4, b-3, c-2, d-1"
        ],
        "exp_en": "Sir V. Bhashyam Aiyangar was the first Indian Advocate General of Madras; Sir P.S. Sivaswami Iyer served 1907-1912; S. Srinivasa Iyengar served 1916-1920; K. Rajah Iyer was the first Advocate General of post-independence Madras State.",
        "exp_ta": "சர் வி. பாஷ்யம் ஐயங்கார் முதல் இந்திய மெட்ராஸ் AG; பி.எஸ். சிவசுவாமி ஐயர் 1907-1912-ல் பணியாற்றினார்; எஸ். சீனிவாச ஐயங்கார் 1916-1920-ல் பணியாற்றினார்; கே. ராஜா ஐயர் சுதந்திர மெட்ராஸ் மாநிலத்தின் முதல் AG.",
        "tip_en": "Sir V. Bhashyam Aiyangar broke the British monopoly by becoming Madras Advocate General.",
        "tip_ta": "சர் வி. பாஷ்யம் ஐயங்கார் பிரிட்டிஷ் ஆதிக்கத்தை உடைத்து மெட்ராஸ் அட்வகேட் ஜெனரலான முதல் இந்தியர் ஆவார்.",
        "fact_en": "The Advocate General of Madras Presidency was historically one of the most prestigious legal positions in British India.",
        "fact_ta": "மெட்ராஸ் மாகாண அட்வகேட் ஜெனரல் பதவி பிரிட்டிஷ் இந்தியாவில் மிக மதிப்புமிக்க சட்டப் பதவிகளில் ஒன்றாக விளங்கியது."
    },
    # 8: Constitutional Articles in Part VI
    {
        "subtopic": "Constitutional Articles in Part VI",
        "title_en": "Match List-I (Articles in Part VI of the Constitution) with List-II (Constitutional Subject Matter):",
        "title_ta": "பட்டியல்-I-ஐ (அரசியலமைப்பின் பகுதி VI-ல் உள்ள சரத்துகள்) பட்டியல்-II உடன் (அரசியலமைப்பு பொருள்) பொருத்துக:",
        "l1_en": [("a. Article 163", "1. Council of Ministers to aid and advise the Governor"),
                  ("b. Article 165", "2. Advocate General for the State"),
                  ("c. Article 166", "3. Conduct of business of the Government of a State"),
                  ("d. Article 167", "4. Duties of Chief Minister as respects the furnishing of information to Governor")],
        "l1_ta": [("a. சரத்து 163", "1. ஆளுநருக்கு உதவவும் ஆலோசனையளிக்கவும் அமைச்சரவை"),
                  ("b. சரத்து 165", "2. மாநிலத்திற்கான அட்வகேட் ஜெனரல்"),
                  ("c. சரத்து 166", "3. மாநில அரசாங்கத்தின் அலுவல் நடத்தை"),
                  ("d. சரத்து 167", "4. ஆளுநருக்கு தகவல்களை வழங்குவது தொடர்பான முதலமைச்சரின் கடமைகள்")],
        "correct_map": "a-1, b-2, c-3, d-4",
        "options_perms": [
            "a-1, b-2, c-3, d-4",
            "a-2, b-1, c-4, d-3",
            "a-4, b-3, c-2, d-1",
            "a-3, b-4, c-1, d-2"
        ],
        "exp_en": "Articles 163 to 167 form the core of Chapter II (The Executive) of Part VI: 163 is Council of Ministers; 165 is Advocate General; 166 is Conduct of Business; 167 is CM duties.",
        "exp_ta": "பகுதி VI அத்தியாயம் II-ல் உள்ள முக்கிய சரத்துகள்: 163 அமைச்சரவை; 165 அட்வகேட் ஜெனரல்; 166 அலுவல் நடத்தை; 167 முதலமைச்சரின் கடமைகள்.",
        "tip_en": "Part VI Chapter II covers the State Executive: Governor (153-162), Council of Ministers (163-164), Advocate General (165), Government Business (166-167).",
        "tip_ta": "பகுதி VI அத்தியாயம் II மாநில நிர்வாகம்: ஆளுநர் (153-162), அமைச்சரவை (163-164), அட்வகேட் ஜெனரல் (165), அரசு அலுவல் (166-167).",
        "fact_en": "The Advocate General is an integral component of the constitutional State Executive.",
        "fact_ta": "அட்வகேட் ஜெனரல் மாநில நிர்வாக அமைப்பின் ஒருங்கிணைந்த அரசியலமைப்பு அங்கம் ஆவார்."
    },
    # 9: Comparative Tenures and Age Limits
    {
        "subtopic": "Comparison of Tenures and Limits",
        "title_en": "Match List-I (Constitutional Offices in the State) with List-II (Tenure and Age Limit Provisions):",
        "title_ta": "பட்டியல்-I-ஐ (மாநில அரசியலமைப்பு பதவிகள்) பட்டியல்-II உடன் (பதவிக்காலம் மற்றும் வயது வரம்பு விதிகள்) பொருத்துக:",
        "l1_en": [("a. Advocate General of the State", "1. No fixed tenure and no retirement age (pleasure of Governor)"),
                  ("b. High Court Judge", "2. Up to 62 years of age"),
                  ("c. State Public Service Commission Member", "3. 6 years or 62 years of age, whichever is earlier"),
                  ("d. State Election Commissioner", "4. Fixed tenure governed by State Legislature Act (cannot be removed except like HC Judge)")],
        "l1_ta": [("a. மாநில அட்வகேட் ஜெனரல்", "1. நிலையான பதவிக்காலமும் ஓய்வுபெறும் வயதும் இல்லை (ஆளுநரின் விருப்பம் வரை)"),
                  ("b. உயர் நீதிமன்ற நீதிபதி", "2. 62 வயது வரை"),
                  ("c. மாநில அரசுப் பணியாளர் தேர்வாணைய உறுப்பினர்", "3. 6 ஆண்டுகள் அல்லது 62 வயது, எது முந்தையதோ அதுவரை"),
                  ("d. மாநில தேர்தல் ஆணையர்", "4. சட்டமன்ற சட்டத்தால் நிர்ணயிக்கப்பட்ட பதவிக்காலம் (HC நீதிபதி போல மட்டுமே நீக்க முடியும்)")],
        "correct_map": "a-1, b-2, c-3, d-4",
        "options_perms": [
            "a-1, b-2, c-3, d-4",
            "a-3, b-4, c-1, d-2",
            "a-2, b-1, c-4, d-3",
            "a-4, b-2, c-1, d-3"
        ],
        "exp_en": "Advocate General has no fixed tenure or age limit (pleasure of Governor); HC Judges retire at 62; SPSC members serve 6 years/62 years; State Election Commissioner has fixed statutory tenure protected like HC judge.",
        "exp_ta": "அட்வகேட் ஜெனரலுக்கு நிலையான காலமோ வயது வரம்போ இல்லை (ஆளுநர் விருப்பம்); HC நீதிபதிகள் 62 வயதில் ஓய்வுபெறுவர்; TNPSC உறுப்பினர்கள் 6 ஆண்டுகள்/62 வயது; மாநில தேர்தல் ஆணையர் HC நீதிபதிக்கு இணையான பாதுகாப்புடையவர்.",
        "tip_en": "Advocate General and Attorney General are among the very few constitutional posts without a statutory or constitutional retirement age.",
        "tip_ta": "அரசியலமைப்பில் ஓய்வுபெறும் வயது நிர்ணயிக்கப்படாத மிகச்சில பதவிகளில் அட்வகேட் ஜெனரல் மற்றும் தலைமை வழக்கறிஞர் அடங்குவர்.",
        "fact_en": "The age limit of 62 years applies only to sitting High Court judges, not to the Advocate General (G.D. Karkare case).",
        "fact_ta": "62 வயது வரம்பு உயர் நீதிமன்றத்தில் பணிபுரியும் நீதிபதிகளுக்கே பொருந்தும், அட்வகேட் ஜெனரலுக்கு பொருந்தாது (கார்கரே வழக்கு)."
    },
    # 10: Legal Enactments and State Representation
    {
        "subtopic": "Representation of State in Courts",
        "title_en": "Match List-I (Legal Matters & Statutes) with List-II (Role and Mandate of the Advocate General):",
        "title_ta": "பட்டியல்-I-ஐ (சட்ட விவகாரங்கள் & சட்டங்கள்) பட்டியல்-II உடன் (அட்வகேட் ஜெனரலின் பங்கு மற்றும் ஆணை) பொருத்துக:",
        "l1_en": [("a. Suits involving Public Charities (CPC Sec 92)", "1. AG files suit or grants written leave for private individuals to institute suit"),
                  ("b. Criminal Contempt of High Court (Contempt Act Sec 15)", "2. AG provides consent on motion by any other person"),
                  ("c. Withdrawal from Criminal Prosecution (CrPC Sec 321)", "3. Handled by Public Prosecutor with consent of court, often on AG advice"),
                  ("d. References by Governor under Article 165(2)", "4. AG gives formal constitutional opinion on questions of law")],
        "l1_ta": [("a. பொது அறக்கட்டளைகள் தொடர்பான வழக்குகள் (CPC பிரிவு 92)", "1. AG நேரடியாக வழக்கு தொடரலாம் அல்லது தனிநபர்கள் தொடர எழுத்துப்பூர்வ அனுமதி அளிக்கலாம்"),
                  ("b. உயர் நீதிமன்ற குற்றவியல் அவமதிப்பு (அவமதிப்பு சட்டம் பிரிவு 15)", "2. பிற நபர்களின் மனுவின் மீது AG தனது ஒப்புதலை வழங்குகிறார்"),
                  ("c. குற்றவியல் வழக்கைத் திரும்பப் பெறுதல் (CrPC பிரிவு 321)", "3. நீதிமன்ற அனுமதியுடன் பப்ளிக் பிராசிகியூட்டர் செய்கிறார் (பெரும்பாலும் AG ஆலோசனையின்படி)"),
                  ("d. சரத்து 165(2)-ன் கீழ் ஆளுநரின் சட்டக் குறிப்புரைகள்", "4. சட்டக் கேள்விகள் மீது AG முறையான அரசியலமைப்பு ஆலோசனையை வழங்குகிறார்")],
        "correct_map": "a-1, b-2, c-3, d-4",
        "options_perms": [
            "a-1, b-2, c-3, d-4",
            "a-2, b-1, c-4, d-3",
            "a-3, b-4, c-1, d-2",
            "a-4, b-3, c-2, d-1"
        ],
        "exp_en": "Under CPC Sec 92, AG acts as parens patriae for charities; under Contempt Act Sec 15, AG screens frivolous motions; under CrPC 321, prosecution withdrawal is guided; under Art 165(2), AG advises Governor.",
        "exp_ta": "CPC 92-ன் கீழ் அறக்கட்டளைகளின் பாதுகாவலராக AG செயல்படுகிறார்; அவமதிப்பு சட்டம் 15-ன் கீழ் தேவையற்ற மனுக்களைத் தடுக்கிறார்; CrPC 321 திரும்பப் பெறுதலுக்கு வழிகாட்டுகிறது; சரத்து 165(2) ஆளுநருக்கு ஆலோசனையளிக்கிறது.",
        "tip_en": "CPC Section 91 relates to Public Nuisance; Section 92 relates to Public Charities.",
        "tip_ta": "CPC பிரிவு 91 பொதுத்தொல்லை; பிரிவு 92 பொது அறக்கட்டளைகள் தொடர்புடையது.",
        "fact_en": "The doctrine of parens patriae historically vests in the Advocate General the duty to protect public charities.",
        "fact_ta": "பொது அறக்கட்டளைகளைப் பாதுகாக்கும் 'parens patriae' கடமை வரலாற்று ரீதியாக அட்வகேட் ஜெனரலிடம் உள்ளது."
    },
    # 11: Bar Council Functions
    {
        "subtopic": "Bar Council of the State",
        "title_en": "Match List-I (Statutory Bodies and Offices) with List-II (Status of Advocate General):",
        "title_ta": "பட்டியல்-I-ஐ (சட்டப்பூர்வ அமைப்புகள் மற்றும் பதவிகள்) பட்டியல்-II உடன் (அட்வகேட் ஜெனரலின் அந்தஸ்து) பொருத்துக:",
        "l1_en": [("a. Bar Council of the State (Sec 3, Advocates Act)", "1. Ex-officio Member of the State Bar Council"),
                  ("b. Bar Council of India (Sec 4, Advocates Act)", "2. Attorney General and Solicitor General are Ex-officio Members (not State AG)"),
                  ("c. Disciplinary Committee of State Bar Council", "4. Receives notices in professional misconduct appeals"),
                  ("d. High Court Rule Committee (Sec 123, CPC)", "3. Member of the High Court Rule-Making Committee")],
        "l1_ta": [("a. மாநில பார் கவுன்சில் (வழக்கறிஞர்கள் சட்டம் பிரிவு 3)", "1. மாநில பார் கவுன்சிலின் பதவி வழி உறுப்பினர்"),
                  ("b. இந்திய பார் கவுன்சில் (வழக்கறிஞர்கள் சட்டம் பிரிவு 4)", "2. இந்திய தலைமை வழக்கறிஞர் மற்றும் சொலிசிட்டர் ஜெனரல் மட்டுமே பதவி வழி உறுப்பினர்கள்"),
                  ("c. மாநில பார் கவுன்சில் ஒழுங்கு நடவடிக்கைக் குழு", "4. தொழில்முறை தவறான நடத்தை மேல்முறையீடுகளில் அறிவிப்புகளைப் பெறுகிறார்"),
                  ("d. உயர் நீதிமன்ற விதிகள் குழு (CPC பிரிவு 123)", "3. உயர் நீதிமன்ற விதிகள் உருவாக்கும் குழுவின் உறுப்பினர்")],
        "correct_map": "a-1, b-2, c-4, d-3",
        "options_perms": [
            "a-1, b-2, c-4, d-3",
            "a-1, b-2, c-3, d-4",
            "a-2, b-1, c-4, d-3",
            "a-3, b-4, c-1, d-2"
        ],
        "exp_en": "Under Advocates Act Sec 3, the Advocate General is ex-officio member of the State Bar Council; Sec 4 reserves BCI membership to AG and SG; Sec 123 CPC includes AG in the Rule Committee.",
        "exp_ta": "வழக்கறிஞர்கள் சட்டம் பிரிவு 3-ன் கீழ் AG மாநில பார் கவுன்சிலின் பதவி வழி உறுப்பினர்; பிரிவு 4 BCI-ல் இந்திய AG/SG-க்கு மட்டுமே உறுப்பினர் பதவி அளிக்கிறது; CPC 123-ன் கீழ் விதிகள் குழுவில் உறுப்பினர்.",
        "tip_en": "Advocate General is ex-officio member of STATE Bar Council, NOT the Bar Council of India.",
        "tip_ta": "அட்வகேட் ஜெனரல் மாநில பார் கவுன்சிலின் பதவி வழி உறுப்பினர் ஆவார், இந்திய பார் கவுன்சில் அல்ல.",
        "fact_en": "The State Bar Council recognizes the Advocate General as the leader of the State Bar.",
        "fact_ta": "மாநில பார் கவுன்சில் அட்வகேட் ஜெனரலை மாநில வழக்கறிஞர் மன்றத்தின் தலைவராக (Leader of the Bar) அங்கீகரிக்கிறது."
    },
    # 12: Pre-Independence Legal Landmarks
    {
        "subtopic": "Pre-Independence Evolution",
        "title_en": "Match List-I (Pre-Independence Acts and Documents) with List-II (Provisions regarding Advocate General):",
        "title_ta": "பட்டியல்-I-ஐ (சுதந்திரத்திற்கு முந்தைய சட்டங்கள் மற்றும் ஆவணங்கள்) பட்டியல்-II உடன் (அட்வகேட் ஜெனரல் தொடர்பான விதிகள்) பொருத்துக:",
        "l1_en": [("a. East India Company Charter Act, 1813", "1. Confirmed statutory status of Advocate-General in Presidencies"),
                  ("b. Indian Councils Act, 1861", "2. Empowered Advocate General to speak in Governor's Legislative Council"),
                  ("c. Government of India Act, 1919", "3. Continued Advocate General's right of audience in provincial councils"),
                  ("d. Government of India Act, 1935 (Section 55)", "4. Formalized appointment of Advocate-General for every Province by Governor")],
        "l1_ta": [("a. கிழக்கிந்திய கம்பெனி சாசனச் சட்டம், 1813", "1. மாகாணங்களில் அட்வகேட்-ஜெனரலின் சட்டப்பூர்வ அந்தஸ்தை உறுதிப்படுத்தியது"),
                  ("b. இந்திய கவுன்சில்கள் சட்டம், 1861", "2. ஆளுநரின் சட்டமன்ற கவுன்சிலில் பேச அட்வகேட் ஜெனரலுக்கு அதிகாரம் அளித்தது"),
                  ("c. இந்திய அரசுச் சட்டம், 1919", "3. மாகாண கவுன்சில்களில் அட்வகேட் ஜெனரலின் வாதாடும் உரிமையைத் தொடர்ந்தது"),
                  ("d. இந்திய அரசுச் சட்டம், 1935 (பிரிவு 55)", "4. ஒவ்வொரு மாகாணத்திற்கும் ஆளுநரால் அட்வகேட்-ஜெனரல் நியமிக்கப்படுவதை முறைப்படுத்தியது")],
        "correct_map": "a-1, b-2, c-3, d-4",
        "options_perms": [
            "a-1, b-2, c-3, d-4",
            "a-2, b-1, c-4, d-3",
            "a-4, b-3, c-2, d-1",
            "a-3, b-4, c-1, d-2"
        ],
        "exp_en": "Section 55 of GOI Act 1935 is the direct predecessor of Article 165; Indian Councils Act 1861 first gave legislative participation rights; Charter Act 1813 recognized legal officers in Presidencies.",
        "exp_ta": "1935 இந்திய அரசுச் சட்டம் பிரிவு 55 தற்போதைய சரத்து 165-ன் நேரடி முன்னோடியாகும்; 1861 கவுன்சில்கள் சட்டம் முதன்முதலில் சட்டமன்றத்தில் பேசும் உரிமையை வழங்கியது.",
        "tip_en": "Section 55 of the Government of India Act 1935 corresponds directly to Article 165 of the Constitution of India.",
        "tip_ta": "1935 இந்திய அரசுச் சட்டத்தின் பிரிவு 55, இந்திய அரசியலமைப்பின் சரத்து 165-க்கு நேரடியாகப் பொருந்துகிறது.",
        "fact_en": "Under GOI Act 1935, Advocate General for the Federation was created under Section 16, and Provincial AGs under Section 55.",
        "fact_ta": "1935 சட்டத்தில் கூட்டாட்சி AG பிரிவு 16-ன் கீழும், மாகாண AG பிரிவு 55-ன் கீழும் உருவாக்கப்பட்டனர்."
    },
    # 13: Constitutional Limitations
    {
        "subtopic": "Constitutional Limitations and Disabilities",
        "title_en": "Match List-I (Constitutional and Professional Limitations) with List-II (Legal Source or Justification):",
        "title_ta": "பட்டியல்-I-ஐ (அரசியலமைப்பு மற்றும் தொழில்முறை கட்டுப்பாடுகள்) பட்டியல்-II உடன் (சட்ட மூலம் அல்லது நியாயம்) பொருத்துக:",
        "l1_en": [("a. Barred from voting in State Legislature", "1. Article 177 explicit constitutional exclusion"),
                  ("b. Barred from advising parties against State Government", "2. Conflict of interest and fiduciary duty to the State"),
                  ("c. Barred from defending accused in criminal cases without permission", "3. State Law Officers Rules and professional conduct"),
                  ("d. Barred from accepting directorship in commercial companies without sanction", "4. Executive service conditions preventing pecuniary conflicts")],
        "l1_ta": [("a. சட்டமன்றத்தில் வாக்களிக்கத் தடை", "1. சரத்து 177-ன் வெளிப்படையான அரசியலமைப்பு விலக்கு"),
                  ("b. மாநில அரசுக்கு எதிராகத் தரப்பினருக்கு ஆலோசனையளிக்கத் தடை", "2. நலன் முரண்பாடு மற்றும் மாநிலத்திற்கான விசுவாசக் கடமை"),
                  ("c. அனுமதியின்றி குற்றவியல் வழக்குகளில் குற்றவாளிகளைப் பாதுகாக்கத் தடை", "3. மாநில சட்ட அதிகாரிகள் விதிகள் மற்றும் தொழில் ஒழுக்கம்"),
                  ("d. அரசு அனுமதியின்றி வணிக நிறுவனங்களில் இயக்குநர் பதவி ஏற்கத் தடை", "4. நிதி சார்ந்த முரண்பாடுகளைத் தடுக்கும் நிர்வாகப் பணி நிபந்தனைகள்")],
        "correct_map": "a-1, b-2, c-3, d-4",
        "options_perms": [
            "a-1, b-2, c-3, d-4",
            "a-3, b-4, c-1, d-2",
            "a-2, b-1, c-4, d-3",
            "a-4, b-2, c-1, d-3"
        ],
        "exp_en": "Article 177 bars voting; conflict of interest prevents advising opposing parties; defending accused without permission is barred to prevent conflict with State prosecutors; corporate directorships require government sanction.",
        "exp_ta": "சரத்து 177 வாக்களிப்பதைத் தடுக்கிறது; நலன் முரண்பாடு அரசுக்கு எதிராக வாதாடுவதைத் தடுக்கிறது; குற்றவியல் வழக்குகளில் ஆஜராக அனுமதி தேவை; நிறுவன இயக்குநர் பதவிக்கு அரசு ஒப்புதல் அவசியம்.",
        "tip_en": "Advocate General is NOT a government servant, so private practice is permitted, but subject to strict ethical limitations.",
        "tip_ta": "அட்வகேட் ஜெனரல் அரசு ஊழியர் அல்ல, எனவே தனியார் வழக்காட அனுமதிக்கப்படுகிறார், ஆனால் கடுமையான கட்டுப்பாடுகளுக்கு உட்பட்டது.",
        "fact_en": "Unlike the Advocate General, judges of High Courts are completely prohibited from private legal practice during their tenure.",
        "fact_ta": "உயர் நீதிமன்ற நீதிபதிகள் போலன்றி, அட்வகேட் ஜெனரல் நிபந்தனைகளுக்கு உட்பட்டு தனியார் வழக்குகளில் ஆஜராகலாம்."
    },
    # 14: Legislative Rights under Article 177
    {
        "subtopic": "Rights in State Legislature",
        "title_en": "Match List-I (Legislative Proceedings in State Legislature) with List-II (Specific Rights of Advocate General):",
        "title_ta": "பட்டியல்-I-ஐ (மாநில சட்டமன்ற நடவடிக்கைகள்) பட்டியல்-II உடன் (அட்வகேட் ஜெனரலின் குறிப்பிட்ட உரிமைகள்) பொருத்துக:",
        "l1_en": [("a. Legislative Assembly / Council Debates", "1. Entitled to speak and participate without being an elected member"),
                  ("b. Select Committee of the Legislature", "2. Entitled to be named a member and take part in proceedings"),
                  ("c. Voting on Bills and Resolutions", "3. Explicitly excluded from voting by virtue of Article 177"),
                  ("d. Immunity from Judicial Proceedings for speeches", "4. Fully protected under Article 194(2) like an elected MLA")],
        "l1_ta": [("a. சட்டமன்றப் பேரவை / மேலவை விவாதங்கள்", "1. தேர்ந்தெடுக்கப்பட்ட உறுப்பினராக இல்லாமலேயே பேசவும் பங்கேற்கவும் உரிமை உண்டு"),
                  ("b. சட்டமன்ற தேர்வுக் குழு (Select Committee)", "2. உறுப்பினராகப் பெயரிடப்படவும் நடவடிக்கைகளில் பங்கெடுக்கவும் உரிமை உண்டு"),
                  ("c. சட்டமுன்வடிவுகள் மற்றும் தீர்மானங்கள் மீதான வாக்கெடுப்பு", "4. சரத்து 177-ன் படி வாக்களிப்பதில் இருந்து வெளிப்படையாக விலக்கப்பட்டுள்ளார்"),
                  ("d. உரைகளுக்காக நீதிமன்ற நடவடிக்கைகளிலிருந்து பாதுகாப்பு", "3. தேர்ந்தெடுக்கப்பட்ட எம்.எல்.ஏ போல சரத்து 194(2)-ன் கீழ் முழு பாதுகாப்பு உண்டு")],
        "correct_map": "a-1, b-2, c-4, d-3",
        "options_perms": [
            "a-1, b-2, c-4, d-3",
            "a-1, b-2, c-3, d-4",
            "a-2, b-1, c-4, d-3",
            "a-3, b-4, c-1, d-2"
        ],
        "exp_en": "Article 177 grants speaking rights in Assembly/Council and committees where named, but prohibits voting. Article 194(2) extends speech immunity to Advocate General.",
        "exp_ta": "சரத்து 177 சட்டமன்றத்திலும் குழுக்களிலும் பேச உரிமை அளிக்கிறது, ஆனால் வாக்களிக்கத் தடை செய்கிறது. சரத்து 194(2) பேச்சுரிமைப் பாதுகாப்பை அட்வகேட் ஜெனரலுக்கும் நீட்டிக்கிறது.",
        "tip_en": "Article 177 = Right to speak and participate; Article 194(4) = Immunities and privileges as an MLA.",
        "tip_ta": "சரத்து 177 = பேசவும் பங்கேற்கவும் உரிமை; சரத்து 194(4) = சட்டமன்ற உறுப்பினருக்கான சலுகைகள் மற்றும் பாதுகாப்புகள்.",
        "fact_en": "The Advocate General cannot be held liable in any court for anything said or any vote omitted in the Legislature.",
        "fact_ta": "சட்டமன்றத்தில் பேசிய எதற்கும் அட்வகேட் ஜெனரல் மீது எந்த நீதிமன்றத்திலும் வழக்கு தொடர முடியாது."
    },
    # 15: Appointment and Removal Mechanism
    {
        "subtopic": "Appointment and Removal Mechanism",
        "title_en": "Match List-I (Constitutional Offices) with List-II (Removal Authority and Procedure):",
        "title_ta": "பட்டியல்-I-ஐ (அரசியலமைப்புப் பதவிகள்) பட்டியல்-II உடன் (நீக்கும் அதிகாரம் மற்றும் நடைமுறை) பொருத்துக:",
        "l1_en": [("a. Advocate General of the State", "1. Removed by Governor at any time without grounds (pleasure of Governor)"),
                  ("b. High Court Judge", "2. Removed by President following parliamentary address with special majority"),
                  ("c. State Election Commissioner", "3. Removed by President in like manner and on like grounds as a High Court Judge"),
                  ("d. Chairman, State Public Service Commission", "4. Removed by President only, on grounds of misbehavior after Supreme Court inquiry")],
        "l1_ta": [("a. மாநில அட்வகேட் ஜெனரல்", "1. எந்த காரணமும் கூறாமல் ஆளுநரால் எந்த நேரத்திலும் நீக்கப்படலாம் (ஆளுநரின் விருப்பம்)"),
                  ("b. உயர் நீதிமன்ற நீதிபதி", "2. சிறப்பு பெரும்பான்மையுடன் நாடாளுமன்ற தீர்மானத்திற்குப் பிறகு குடியரசுத் தலைவரால் நீக்கம்"),
                  ("c. மாநில தேர்தல் ஆணையர்", "3. உயர் நீதிமன்ற நீதிபதியைப் போன்ற நடைமுறை மற்றும் காரணங்களின் அடிப்படையில் குடியரசுத் தலைவரால் நீக்கம்"),
                  ("d. தலைவர், மாநில அரசுப் பணியாளர் தேர்வாணையம்", "4. உச்ச நீதிமன்ற விசாரணைக்குப் பிறகு நடத்தை தவறிய காரணத்திற்காக குடியரசுத் தலைவரால் மட்டுமே நீக்கம்")],
        "correct_map": "a-1, b-2, c-3, d-4",
        "options_perms": [
            "a-1, b-2, c-3, d-4",
            "a-2, b-1, c-4, d-3",
            "a-4, b-3, c-2, d-1",
            "a-3, b-4, c-1, d-2"
        ],
        "exp_en": "Advocate General is removable by Governor at pleasure; HC Judge by President via Parliament impeachment; SEC by President like HC judge; SPSC Chairman by President after SC inquiry under Art 317.",
        "exp_ta": "அட்வகேட் ஜெனரலை ஆளுநர் எப்போது வேண்டுமானாலும் நீக்கலாம்; HC நீதிபதியை நாடாளுமன்ற பதவிநீக்கத் தீர்மானம் மூலம் குடியரசுத் தலைவர் நீக்குவார்; SEC-ஐ HC நீதிபதி போலவும்; TNPSC தலைவரை உச்ச நீதிமன்ற விசாரணைக்குப் பின் குடியரசுத் தலைவர் நீக்குவார்.",
        "tip_en": "Even though appointed by Governor, SPSC Chairman and State Election Commissioner can ONLY be removed by the President.",
        "tip_ta": "ஆளுநரால் நியமிக்கப்பட்டாலும், TNPSC தலைவர் மற்றும் தேர்தல் ஆணையரை குடியரசுத் தலைவர் மட்டுமே நீக்க முடியும்.",
        "fact_en": "Advocate General has no security of tenure, unlike High Court judges or Public Service Commission members.",
        "fact_ta": "உயர் நீதிமன்ற நீதிபதிகள் அல்லது தேர்வாணைய உறுப்பினர்களைப் போல அட்வகேட் ஜெனரலுக்கு பதவிக் காலப் பாதுகாப்பு கிடையாது."
    },
    # 16: CPC Powers
    {
        "subtopic": "Powers under Code of Civil Procedure",
        "title_en": "Match List-I (Provisions of CPC, 1908) with List-II (Application to Advocate General):",
        "title_ta": "பட்டியல்-I-ஐ (CPC, 1908-ன் விதிகள்) பட்டியல்-II உடன் (அட்வகேட் ஜெனரலுக்கான பயன்பாடு) பொருத்துக:",
        "l1_en": [("a. Section 91(1)(a)", "1. Suit relating to public nuisance instituted directly by Advocate General"),
                  ("b. Section 91(1)(b)", "2. Suit relating to public nuisance instituted by two or more persons with leave of the Court"),
                  ("c. Section 92(1)", "3. Suit for breach of trust in public charities instituted by Advocate General"),
                  ("d. Order XXVII, Rule 8B", "4. Definition of Government Pleader including Advocate General for State notices")],
        "l1_ta": [("a. பிரிவு 91(1)(a)", "1. பொதுத்தொல்லை தொடர்பாக அட்வகேட் ஜெனரலால் நேரடியாகத் தொடரப்படும் வழக்கு"),
                  ("b. பிரிவு 91(1)(b)", "2. நீதிமன்ற அனுமதியுடன் இரண்டு அல்லது அதற்கு மேற்பட்ட நபர்களால் தொடரப்படும் பொதுத்தொல்லை வழக்கு"),
                  ("c. பிரிவு 92(1)", "3. பொது அறக்கட்டளைகளில் நம்பிக்கை மீறலுக்காக அட்வகேட் ஜெனரலால் தொடரப்படும் வழக்கு"),
                  ("d. கட்டளை XXVII, விதி 8B", "4. மாநில அரசு அறிவிப்புகளுக்கான அரசு பிளீடர் என்ற வரையறையில் அட்வகேட் ஜெனரலும் அடங்குதல்")],
        "correct_map": "a-1, b-2, c-3, d-4",
        "options_perms": [
            "a-1, b-2, c-3, d-4",
            "a-3, b-4, c-1, d-2",
            "a-2, b-1, c-4, d-3",
            "a-4, b-2, c-1, d-3"
        ],
        "exp_en": "CPC Sec 91(1)(a) empowers AG to file public nuisance suits; Sec 91(1)(b) allows private suits with court leave; Sec 92(1) empowers AG for public charities; Order 27 Rule 8B recognizes AG in government litigation.",
        "exp_ta": "CPC 91(1)(a) பொதுத்தொல்லை வழக்கு தொடர அதிகாரம் அளிக்கிறது; 91(1)(b) நீதிமன்ற அனுமதியுடன் தனிநபர் வழக்குகளை அனுமதிக்கிறது; 92(1) பொது அறக்கட்டளை வழக்குகளுக்கு அதிகாரம் அளிக்கிறது; கட்டளை 27 விதி 8B அரசு வழக்குகளில் அங்கீகரிக்கிறது.",
        "tip_en": "Prior to the 1976 CPC Amendment, private suits under Sec 91/92 required the consent of the Advocate General.",
        "tip_ta": "1976 CPC திருத்தத்திற்கு முன்பு, பிரிவு 91/92-ன் கீழ் தனிநபர் வழக்குகளுக்கு அட்வகேட் ஜெனரலின் ஒப்புதல் அவசியமாக இருந்தது.",
        "fact_en": "Advocate General exercises the ancient Crown prerogative of protecting charitable endowments in the State.",
        "fact_ta": "மாநிலத்தில் உள்ள அறக்கட்டளைகளைப் பாதுகாக்கும் தொன்மையான அதிகாரத்தை அட்வகேட் ஜெனரல் செலுத்துகிறார்."
    },
    # 17: Legal Principles on Advocate General's Office
    {
        "subtopic": "Legal Principles and Judicial Doctrines",
        "title_en": "Match List-I (Legal Principles & Doctrines) with List-II (Their Significance for the Advocate General):",
        "title_ta": "பட்டியல்-I-ஐ (சட்டக் கோட்பாடுகள் & கொள்கைகள்) பட்டியல்-II உடன் (அட்வகேட் ஜெனரலுக்கான அவற்றின் முக்கியத்துவம்) பொருத்துக:",
        "l1_en": [("a. Doctrine of Pleasure", "1. Office is held without fixed term, terminable without showing cause (Art 165(3))"),
                  ("b. Parens Patriae Jurisdiction", "2. Legal guardian role protecting public charities and vulnerable trusts (CPC Sec 92)"),
                  ("c. Quasi-Judicial Function", "3. Impartial decision-making when granting consent for contempt motions"),
                  ("d. Fiduciary Duty to Public", "4. High constitutional officer accountable to the Constitution and rule of law, not partisan interest")],
        "l1_ta": [("a. விருப்பக் கோட்பாடு (Doctrine of Pleasure)", "1. குறிப்பிட்ட காலமின்றி பதவி வகித்தல், காரணம் கூறாமல் நீக்கப்படலாம் (சரத்து 165(3))"),
                  ("b. பெற்றோரின் பாதுகாவலர் அதிகாரம் (Parens Patriae)", "2. பொது அறக்கட்டளைகளைப் பாதுகாக்கும் பாதுகாவலர் பங்கு (CPC பிரிவு 92)"),
                  ("c. நீதித்துறை போன்ற பணி (Quasi-Judicial Function)", "3. அவமதிப்பு மனுக்களுக்கு ஒப்புதல் அளிக்கும்போது பாரபட்சமின்றி முடிவெடுத்தல்"),
                  ("d. பொதுமக்களுக்கான விசுவாசக் கடமை (Fiduciary Duty)", "4. கட்சி நலன்களுக்கு அப்பாற்பட்டு அரசியலமைப்பு மற்றும் சட்டத்தின் ஆட்சிக்கு பொறுப்பேற்றல்")],
        "correct_map": "a-1, b-2, c-3, d-4",
        "options_perms": [
            "a-1, b-2, c-3, d-4",
            "a-2, b-1, c-4, d-3",
            "a-4, b-3, c-2, d-1",
            "a-3, b-4, c-1, d-2"
        ],
        "exp_en": "Pleasure doctrine governs tenure; Parens patriae guides charity oversight; Quasi-judicial applies to contempt consent; Fiduciary duty was affirmed in UP Law Officers case.",
        "exp_ta": "விருப்பக் கோட்பாடு பதவிக்காலத்தை நிர்வகிக்கிறது; Parens patriae அறக்கட்டளைகளைக் கண்காணிக்கிறது; Quasi-judicial அவமதிப்பு ஒப்புதலுக்குப் பொருந்தும்; விசுவாசக் கடமை உ.பி. வழக்கில் உறுதி செய்யப்பட்டது.",
        "tip_en": "The Advocate General is not a political mouthpiece; he owes allegiance to the Constitution.",
        "tip_ta": "அட்வகேட் ஜெனரல் அரசியல் ஊதுகுழல் அல்ல; அவர் அரசியலமைப்புக்கு மட்டுமே விசுவாசமாக இருக்க வேண்டும்.",
        "fact_en": "Supreme Court held that the Advocate General is an officer of the Court first, and counsel for the Government second.",
        "fact_ta": "அட்வகேட் ஜெனரல் முதலில் நீதிமன்றத்தின் அதிகாரி, இரண்டாவதாகவே அரசின் வழக்கறிஞர் என்று உச்ச நீதிமன்றம் கூறியுள்ளது."
    },
    # 18: Comparison with Other State Institutions
    {
        "subtopic": "State Constitutional Authorities",
        "title_en": "Match List-I (State Constitutional Entities) with List-II (Their Respective Constitutional Article):",
        "title_ta": "பட்டியல்-I-ஐ (மாநில அரசியலமைப்பு அமைப்புகள்) பட்டியல்-II உடன் (அவற்றின் அரசியலமைப்புச் சரத்து) பொருத்துக:",
        "l1_en": [("a. Advocate General of the State", "1. Article 165"),
                  ("b. State Election Commission", "2. Article 243K"),
                  ("c. State Finance Commission", "3. Article 243I"),
                  ("d. State Public Service Commission", "4. Article 315")],
        "l1_ta": [("a. மாநில அட்வகேட் ஜெனரல்", "1. சரத்து 165"),
                  ("b. மாநில தேர்தல் ஆணையம்", "2. சரத்து 243K"),
                  ("c. மாநில நிதி ஆணையம்", "3. சரத்து 243I"),
                  ("d. மாநில அரசுப் பணியாளர் தேர்வாணையம்", "4. சரத்து 315")],
        "correct_map": "a-1, b-2, c-3, d-4",
        "options_perms": [
            "a-1, b-2, c-3, d-4",
            "a-2, b-1, c-4, d-3",
            "a-3, b-4, c-1, d-2",
            "a-4, b-3, c-2, d-1"
        ],
        "exp_en": "Article 165 establishes Advocate General; 243K establishes SEC; 243I establishes State Finance Commission; 315 establishes Public Service Commissions.",
        "exp_ta": "சரத்து 165 அட்வகேட் ஜெனரலையும்; 243K மாநில தேர்தல் ஆணையத்தையும்; 243I மாநில நிதி ஆணையத்தையும்; 315 அரசுப் பணியாளர் தேர்வாணையத்தையும் நிறுவுகிறது.",
        "tip_en": "Memorize State constitutional bodies: 165 (Advocate General), 243I (Finance), 243K (Election), 315 (PSC).",
        "tip_ta": "மாநில அரசியலமைப்பு அமைப்புகள்: 165 (அட்வகேட் ஜெனரல்), 243I (நிதி), 243K (தேர்தல்), 315 (தேர்வாணையம்).",
        "fact_en": "Of all these constitutional posts, only the Advocate General has the explicit right to address the State Legislative Assembly.",
        "fact_ta": "இவற்றில் அட்வகேட் ஜெனரலுக்கு மட்டுமே மாநில சட்டமன்றப் பேரவையில் பேசும் வெளிப்படையான உரிமை உள்ளது."
    },
    # 19: High Court Qualifications
    {
        "subtopic": "Qualifications under Article 217(2)",
        "title_en": "Match List-I (Eligibility Criteria under Article 217(2)) with List-II (Application to Advocate General):",
        "title_ta": "பட்டியல்-I-ஐ (சரத்து 217(2)-ன் தகுதி வரம்புகள்) பட்டியல்-II உடன் (அட்வகேட் ஜெனரலுக்கான பயன்பாடு) பொருத்துக:",
        "l1_en": [("a. Citizenship of India", "1. Mandatory prerequisite under Article 217(2)"),
                  ("b. Judicial Office in India", "2. Held for at least 10 years qualifies a person"),
                  ("c. Advocate in a High Court", "3. Practiced for at least 10 years qualifies a person"),
                  ("d. Distinguished Jurist Category", "4. Available for Supreme Court/AG, but NOT for High Court/Advocate General")],
        "l1_ta": [("a. இந்தியக் குடியுரிமை", "1. சரத்து 217(2)-ன் கீழ் கட்டாய முன்நிபந்தனை"),
                  ("b. இந்தியாவில் நீதித்துறை பதவி", "2. குறைந்தபட்சம் 10 ஆண்டுகள் பதவி வகித்திருப்பது தகுதியளிக்கும்"),
                  ("c. உயர் நீதிமன்றத்தில் வழக்கறிஞர் பணி", "3. குறைந்தபட்சம் 10 ஆண்டுகள் வாதாடிய அனுபவம் தகுதியளிக்கும்"),
                  ("d. புகழ்பெற்ற சட்ட வல்லுநர் வகை", "4. உச்ச நீதிமன்றம்/AG-க்கு உண்டு, ஆனால் உயர் நீதிமன்றம்/அட்வகேட் ஜெனரலுக்கு இல்லை")],
        "correct_map": "a-1, b-2, c-3, d-4",
        "options_perms": [
            "a-1, b-2, c-3, d-4",
            "a-3, b-4, c-1, d-2",
            "a-2, b-1, c-4, d-3",
            "a-4, b-2, c-1, d-3"
        ],
        "exp_en": "Under Art 217(2), a person must be an Indian citizen and have held judicial office for 10 years or been a High Court advocate for 10 years. The 'distinguished jurist' category exists only under Art 124(3)(c) for SC, not for HC.",
        "exp_ta": "சரத்து 217(2)-ன் கீழ், இந்தியக் குடிமகனாகவும், 10 ஆண்டுகள் நீதித்துறை பதவி அல்லது 10 ஆண்டுகள் HC வழக்கறிஞராகவும் இருக்க வேண்டும். 'புகழ்பெற்ற சட்ட வல்லுநர்' உச்ச நீதிமன்றத்திற்கு மட்டுமே பொருந்தும்.",
        "tip_en": "A distinguished jurist CANNOT be appointed as a High Court Judge or Advocate General of a State!",
        "tip_ta": "புகழ்பெற்ற சட்ட வல்லுநர் ஒருவரை உயர் நீதிமன்ற நீதிபதியாகவோ மாநில அட்வகேட் ஜெனரலாகவோ நியமிக்க முடியாது!",
        "fact_en": "This critical omission in Article 217(2) was intentionally made by the Constituent Assembly.",
        "fact_ta": "அரசியலமைப்பு நிர்ணய சபையால் வேண்டுமென்றே சரத்து 217(2)-ல் இந்த விதி தவிர்க்கப்பட்டது."
    },
    # 20: Contempt of Courts Act Procedures
    {
        "subtopic": "Contempt of Courts Act, 1971",
        "title_en": "Match List-I (Contempt of Courts Act Provisions) with List-II (Specific Meaning / AG Authority):",
        "title_ta": "பட்டியல்-I-ஐ (நீதிமன்ற அவமதிப்புச் சட்ட விதிகள்) பட்டியல்-II உடன் (குறிப்பிட்ட பொருள் / AG அதிகாரம்) பொருத்துக:",
        "l1_en": [("a. Section 15(1)(a)", "1. Criminal contempt motion brought on High Court's own motion (suo motu)"),
                  ("b. Section 15(1)(b)", "2. Criminal contempt motion brought by Advocate General of the State"),
                  ("c. Section 15(1)(c)", "3. Criminal contempt motion brought by any other person with AG's written consent"),
                  ("d. Section 15(3)", "4. Specifies that for High Court, 'Advocate-General' means the Advocate General of that State")],
        "l1_ta": [("a. பிரிவு 15(1)(a)", "1. உயர் நீதிமன்றம் தனது சொந்த முயற்சியில் (suo motu) எடுக்கும் குற்றவியல் அவமதிப்பு"),
                  ("b. பிரிவு 15(1)(b)", "2. மாநில அட்வகேட் ஜெனரலால் கொண்டுவரப்படும் குற்றவியல் அவமதிப்பு நடவடிக்கை"),
                  ("c. பிரிவு 15(1)(c)", "3. AG-ன் முன் எழுத்துப்பூர்வ ஒப்புதலுடன் பிற நபரால் கொண்டுவரப்படும் அவமதிப்பு நடவடிக்கை"),
                  ("d. பிரிவு 15(3)", "4. உயர் நீதிமன்றத்தைப் பொறுத்தவரை 'அட்வகேட்-ஜெனரல்' என்பது அந்த மாநில அட்வகேட் ஜெனரலைக் குறிக்கும்")],
        "correct_map": "a-1, b-2, c-3, d-4",
        "options_perms": [
            "a-1, b-2, c-3, d-4",
            "a-2, b-1, c-4, d-3",
            "a-4, b-3, c-2, d-1",
            "a-3, b-4, c-1, d-2"
        ],
        "exp_en": "Section 15 of Contempt of Courts Act 1971 governs cognizance of criminal contempt: suo motu, on motion by AG, or on motion with AG consent. Section 15(3) defines AG for High Courts.",
        "exp_ta": "நீதிமன்ற அவமதிப்புச் சட்டம் 1971 பிரிவு 15 குற்றவியல் அவமதிப்பை வரையறுக்கிறது: தானாக முன்வந்து, AG மனு மூலம், அல்லது AG ஒப்புதலுடன். பிரிவு 15(3) உயர் நீதிமன்ற AG-ஐ வரையறுக்கிறது.",
        "tip_en": "A private individual cannot move criminal contempt in High Court without written consent of the Advocate General.",
        "tip_ta": "அட்வகேட் ஜெனரலின் எழுத்துப்பூர்வ ஒப்புதலின்றி தனிநபர் உயர் நீதிமன்றத்தில் குற்றவியல் அவமதிப்பு மனு தாக்கல் செய்ய முடியாது.",
        "fact_en": "The requirement of AG consent acts as a filter against vexatious and publicity-seeking contempt petitions.",
        "fact_ta": "விளம்பரத்திற்காகவும் பழிவாங்கும் நோக்கிலும் தாக்கல் செய்யப்படும் அவமதிப்பு மனுக்களை வடிகட்ட AG ஒப்புதல் பயன்படுகிறது."
    },
    # 21: Constitutional Oaths Comparison
    {
        "subtopic": "Oaths and Affirmations",
        "title_en": "Match List-I (Constitutional Offices) with List-II (Constitutional Oath Requirement):",
        "title_ta": "பட்டியல்-I-ஐ (அரசியலமைப்புப் பதவிகள்) பட்டியல்-II உடன் (அரசியலமைப்பு பதவிப் பிரமாணத் தேவை) பொருத்துக:",
        "l1_en": [("a. Advocate General of the State", "1. No oath prescribed under the Third Schedule of the Constitution"),
                  ("b. High Court Judge", "2. Oath prescribed under Form VIII of the Third Schedule"),
                  ("c. Governor of the State", "3. Oath prescribed under Article 159 itself (not Third Schedule)"),
                  ("d. Minister for the State", "4. Oath of office and secrecy under Form V of the Third Schedule")],
        "l1_ta": [("a. மாநில அட்வகேட் ஜெனரல்", "1. அரசியலமைப்பின் மூன்றாவது அட்டவணையின் கீழ் எந்த பதவிப் பிரமாணமும் பரிந்துரைக்கப்படவில்லை"),
                  ("b. உயர் நீதிமன்ற நீதிபதி", "2. மூன்றாவது அட்டவணையின் படிவம் VIII-ன் கீழ் பதவிப் பிரமாணம்"),
                  ("c. மாநில ஆளுநர்", "3. சரத்து 159-ன் கீழேயே பதவிப் பிரமாணம் (மூன்றாவது அட்டவணை அல்ல)"),
                  ("d. மாநில அமைச்சர்", "4. மூன்றாவது அட்டவணையின் படிவம் V-ன் கீழ் பதவி மற்றும் இரகசியக் காப்புப் பிரமாணம்")],
        "correct_map": "a-1, b-2, c-3, d-4",
        "options_perms": [
            "a-1, b-2, c-3, d-4",
            "a-3, b-4, c-1, d-2",
            "a-2, b-1, c-4, d-3",
            "a-4, b-2, c-1, d-3"
        ],
        "exp_en": "Neither Attorney General nor Advocate General has an oath prescribed in the Third Schedule; HC Judges use Form VIII; Governor swears under Art 159; State Ministers swear under Form V.",
        "exp_ta": "தலைமை வழக்கறிஞர் மற்றும் அட்வகேட் ஜெனரல் இருவருக்கும் 3-வது அட்டவணையில் பதவிப் பிரமாணம் கிடையாது; HC நீதிபதி படிவம் VIII; ஆளுநர் சரத்து 159; அமைச்சர்கள் படிவம் V.",
        "tip_en": "A favorite TNPSC trap: Neither the Attorney General nor the Advocate General takes an oath under the Third Schedule!",
        "tip_ta": "TNPSC முக்கிய கேள்வி: தலைமை வழக்கறிஞர் மற்றும் அட்வகேட் ஜெனரல் இருவருக்குமே 3-வது அட்டவணையில் பதவிப் பிரமாணம் இல்லை!",
        "fact_en": "Law officers are governed by professional ethics and Bar Council rules rather than a constitutional oath.",
        "fact_ta": "சட்ட அதிகாரிகள் அரசியலமைப்பு பதவிப் பிரமாணத்தைக் காட்டிலும் தொழில் தர்மம் மற்றும் பார் கவுன்சில் விதிகளால் நிர்வகிக்கப்படுகின்றனர்."
    },
    # 22: Advice and Executive Relations
    {
        "subtopic": "Executive Relationship",
        "title_en": "Match List-I (Constitutional Entities) with List-II (Constitutional Interaction with Advocate General):",
        "title_ta": "பட்டியல்-I-ஐ (அரசியலமைப்பு நிறுவனங்கள்) பட்டியல்-II உடன் (அட்வகேட் ஜெனரலுடனான அரசியலமைப்பு தொடர்பு) பொருத்துக:",
        "l1_en": [("a. Governor of the State", "1. Formally appoints AG, determines remuneration, and refers legal matters"),
                  ("b. Chief Minister & Council of Ministers", "2. Effectively selects and recommends appointment / resignation of AG"),
                  ("c. Speaker of the Legislative Assembly", "3. Presides when AG addresses the Assembly and regulates floor participation"),
                  ("d. Chief Justice of the High Court", "4. Heads the judicial institution where AG is leader of the Bar")],
        "l1_ta": [("a. மாநில ஆளுநர்", "1. AG-ஐ முறையாக நியமிக்கிறார், ஊதியம் நிர்ணயிக்கிறார், சட்ட விவகாரங்களைக் குறிப்பிடுகிறார்"),
                  ("b. முதலமைச்சர் & அமைச்சரவை", "2. AG-ன் நியமனம் மற்றும் ராஜினாமாவை நடைமுறையில் தீர்மானித்து பரிந்துரை செய்கிறது"),
                  ("c. சட்டமன்றப் பேரவைத் தலைவர்", "3. AG பேரவையில் உரையாற்றும்போது தலைமை தாங்கி நடவடிக்கைகளை ஒழுங்குபடுத்துகிறார்"),
                  ("d. உயர் நீதிமன்ற தலைமை நீதிபதி", "4. AG வழக்கறிஞர் மன்றத் தலைவராக உள்ள நீதித்துறை அமைப்பிற்கு தலைமை தாங்குகிறார்")],
        "correct_map": "a-1, b-2, c-3, d-4",
        "options_perms": [
            "a-1, b-2, c-3, d-4",
            "a-2, b-1, c-4, d-3",
            "a-4, b-3, c-2, d-1",
            "a-3, b-4, c-1, d-2"
        ],
        "exp_en": "Governor is the formal appointing authority; Council of Ministers exercises the real selection power; Speaker presides in the Assembly; Chief Justice heads the High Court where AG practices.",
        "exp_ta": "ஆளுநர் பெயரளவு நியமன அதிகாரி; அமைச்சரவை உண்மையான தேர்வு அதிகாரம் கொண்டது; சபாநாயகர் சட்டமன்றத்தில் தலைமை தாங்குகிறார்; தலைமை நீதிபதி உயர் நீதிமன்றத்திற்கு தலைமை தாங்குகிறார்.",
        "tip_en": "By convention, when a State Ministry resigns, the Advocate General also tenders resignation.",
        "tip_ta": "மரபுப்படி, மாநில அமைச்சரவை ராஜினாமா செய்யும்போது அட்வகேட் ஜெனரலும் தனது ராஜினாமா கடிதத்தை அளிக்கிறார்.",
        "fact_en": "This convention highlights that the Advocate General is the government's trusted principal legal adviser.",
        "fact_ta": "இந்த மரபு அட்வகேட் ஜெனரல் அரசின் முதன்மை சட்ட ஆலோசகர் என்பதை வெளிப்படுத்துகிறது."
    },
    # 23: State Litigation Hierarchy
    {
        "subtopic": "State Litigation Management",
        "title_en": "Match List-I (Litigation Functions of the State) with List-II (Responsible Legal Functionary):",
        "title_ta": "பட்டியல்-I-ஐ (மாநில அரசின் வழக்கு மேலாண்மைப் பணிகள்) பட்டியல்-II உடன் (பொறுப்பான சட்ட அலுவலர்) பொருத்துக:",
        "l1_en": [("a. Leader of State Legal Team in Constitutional Benches", "1. Advocate General of the State"),
                  ("b. Assisting the Advocate General in major High Court litigation", "2. Additional Advocate General"),
                  ("c. Day-to-day civil representation of Government departments", "3. Government Pleader / Special Government Pleader"),
                  ("d. Conducting prosecution in Sessions Court", "4. Public Prosecutor / Additional Public Prosecutor")],
        "l1_ta": [("a. அரசியலமைப்பு அமர்வுகளில் மாநில சட்டக் குழுவின் தலைவர்", "1. மாநில அட்வகேட் ஜெனரல்"),
                  ("b. முக்கிய உயர் நீதிமன்ற வழக்குகளில் AG-க்கு உதவுதல்", "2. கூடுதல் அட்வகேட் ஜெனரல்"),
                  ("c. அரசுத் துறைகளின் அன்றாட உரிமையியல் வழக்குகளில் முன்னிலையாதல்", "3. அரசு பிளீடர் / சிறப்பு அரசு வழக்கறிஞர்"),
                  ("d. அமர்வு நீதிமன்றத்தில் குற்றவியல் வழக்குகளை நடத்துதல்", "4. அரசு குற்றவியல் வழக்கறிஞர் / கூடுதல் குற்றவியல் வழக்கறிஞர்")],
        "correct_map": "a-1, b-2, c-3, d-4",
        "options_perms": [
            "a-1, b-2, c-3, d-4",
            "a-2, b-1, c-4, d-3",
            "a-3, b-4, c-1, d-2",
            "a-4, b-3, c-2, d-1"
        ],
        "exp_en": "Advocate General leads constitutional matters; Additional AG assists; Government Pleaders handle civil cases; Public Prosecutors handle criminal trials.",
        "exp_ta": "அட்வகேட் ஜெனரல் அரசியலமைப்பு விவகாரங்களுக்குத் தலைமை தாங்குகிறார்; கூடுதல் AG உதவுகிறார்; அரசு பிளீடர் சிவில் வழக்குகளையும்; குற்றவியல் வழக்கறிஞர் குற்ற வழக்குகளையும் நடத்துகின்றனர்.",
        "tip_en": "Government Pleader is on the civil side; Public Prosecutor is on the criminal side.",
        "tip_ta": "அரசு பிளீடர் உரிமையியல் (சிவில்) பக்கம்; பப்ளிக் பிராசிகியூட்டர் குற்றவியல் பக்கம்.",
        "fact_en": "The Advocate General oversees the coordination of both civil and criminal representation of the State.",
        "fact_ta": "மாநில அரசின் உரிமையியல் மற்றும் குற்றவியல் வழக்கு பிரதிநிதித்துவத்தை அட்வகேட் ஜெனரல் மேற்பார்வையிடுகிறார்."
    },
    # 24: Key Constitutional Terms
    {
        "subtopic": "Constitutional Vocabulary and Terms",
        "title_en": "Match List-I (Constitutional Phrases) with List-II (Application to Advocate General):",
        "title_ta": "பட்டியல்-I-ஐ (அரசியலமைப்பு சொற்றொடர்கள்) பட்டியல்-II உடன் (அட்வகேட் ஜெனரலுக்கான பயன்பாடு) பொருத்துக:",
        "l1_en": [("a. 'During the pleasure of the Governor'", "1. Article 165(3) tenure and security of office"),
                  ("b. 'Right of audience in all courts'", "2. Right to appear in all courts within the territory of the State"),
                  ("c. 'Without the right to vote'", "3. Article 177 limitation in State Legislative Assembly/Council"),
                  ("d. 'Remuneration as Governor may determine'", "4. Article 165(3) financial compensation not fixed by Legislature Act")],
        "l1_ta": [("a. 'ஆளுநரின் விருப்பம் உள்ளவரை'", "1. சரத்து 165(3) பதவிக்காலம் மற்றும் பணிப் பாதுகாப்பு"),
                  ("b. 'அனைத்து நீதிமன்றங்களிலும் வாதாடும் உரிமை'", "2. மாநில எல்லைக்குள் உள்ள அனைத்து நீதிமன்றங்களிலும் ஆஜராகும் உரிமை"),
                  ("c. 'வாக்களிக்கும் உரிமையின்றி'", "3. சட்டமன்றப் பேரவை/மேலவையில் சரத்து 177 விதிக்கும் கட்டுப்பாடு"),
                  ("d. 'ஆளுநர் நிர்ணயிக்கும் ஊதியம்'", "4. சட்டமன்ற சட்டத்தால் நிர்ணயிக்கப்படாமல் ஆளுநரால் தீர்மானிக்கப்படும் நிதி ஊதியம்")],
        "correct_map": "a-1, b-2, c-3, d-4",
        "options_perms": [
            "a-1, b-2, c-3, d-4",
            "a-3, b-4, c-1, d-2",
            "a-2, b-1, c-4, d-3",
            "a-4, b-2, c-1, d-3"
        ],
        "exp_en": "Pleasure of Governor governs tenure; Right of audience applies in State courts; Without right to vote is Art 177 rule; Remuneration is determined by Governor.",
        "exp_ta": "ஆளுநரின் விருப்பம் பதவிக்காலத்தை நிர்வகிக்கிறது; அனைத்து நீதிமன்றங்களிலும் ஆஜராகும் உரிமை மாநிலத்திற்கு உட்பட்டது; வாக்களிக்கும் உரிமையின்மை சரத்து 177; ஊதியம் ஆளுநரால் நிர்ணயிக்கப்படுகிறது.",
        "tip_en": "Unlike HC judges whose salaries are charged on the Consolidated Fund and determined by Parliament, AG remuneration is determined by the Governor.",
        "tip_ta": "நாடாளுமன்றத்தால் நிர்ணயிக்கப்படும் HC நீதிபதிகளின் ஊதியம் போலன்றி, AG ஊதியத்தை ஆளுநர் நிர்வாக ரீதியாக நிர்ணயிக்கிறார்.",
        "fact_en": "Article 165(3) deliberately leaves remuneration to executive discretion rather than statutory enactment.",
        "fact_ta": "சரத்து 165(3) ஊதியத்தை சட்டமியற்றலுக்கு விடாமல் நிர்வாக முடிவுக்கு விட்டுள்ளது."
    },
    # 25: Chronological Evolution of Law Officers
    {
        "subtopic": "Chronological Landmarks",
        "title_en": "Match List-I (Milestone Years in Law Officer History) with List-II (Significant Statutory or Constitutional Event):",
        "title_ta": "பட்டியல்-I-ஐ (சட்ட அதிகாரிகள் வரலாற்றின் மைல்கல் ஆண்டுகள்) பட்டியல்-II உடன் (குறிப்பிடத்தக்க சட்ட அல்லது அரசியலமைப்பு நிகழ்வு) பொருத்துக:",
        "l1_en": [("a. 1801", "1. Supreme Court of Judicature established at Madras"),
                  ("b. 1862", "2. High Court of Madras established under Letters Patent"),
                  ("c. 1935", "3. Section 55 created statutory Advocate-General for every Province"),
                  ("d. 1950", "4. Article 165 came into force establishing Advocate General in Constitution of India")],
        "l1_ta": [("a. 1801", "1. மெட்ராஸில் உச்ச நீதிமன்ற நீதித்துறை அமைப்பு (Supreme Court of Judicature) நிறுவப்பட்டது"),
                  ("b. 1862", "2. காப்புரிமை கடிதங்களின் (Letters Patent) கீழ் மெட்ராஸ் உயர் நீதிமன்றம் நிறுவப்பட்டது"),
                  ("c. 1935", "3. பிரிவு 55 ஒவ்வொரு மாகாணத்திற்கும் சட்டப்பூர்வ அட்வகேட்-ஜெனரலை உருவாக்கியது"),
                  ("d. 1950", "4. இந்திய அரசியலமைப்பில் அட்வகேட் ஜெனரலை நிறுவும் சரத்து 165 நடைமுறைக்கு வந்தது")],
        "correct_map": "a-1, b-2, c-3, d-4",
        "options_perms": [
            "a-1, b-2, c-3, d-4",
            "a-2, b-1, c-4, d-3",
            "a-4, b-3, c-2, d-1",
            "a-3, b-4, c-1, d-2"
        ],
        "exp_en": "1801 Supreme Court at Madras; 1862 High Court of Madras; 1935 GOI Act Section 55; 1950 Article 165 of the Constitution of India.",
        "exp_ta": "1801 மெட்ராஸ் உச்ச நீதிமன்றம்; 1862 மெட்ராஸ் உயர் நீதிமன்றம்; 1935 இந்திய அரசுச் சட்டம் பிரிவு 55; 1950 இந்திய அரசியலமைப்புச் சரத்து 165.",
        "tip_en": "Madras legal history: 1801 (Supreme Court), 1862 (High Court), 1935 (GOI Act Sec 55), 1950 (Article 165).",
        "tip_ta": "மெட்ராஸ் சட்ட வரலாறு: 1801 (உச்ச நீதிமன்றம்), 1862 (உயர் நீதிமன்றம்), 1935 (1935 சட்டம் பிரிவு 55), 1950 (சரத்து 165).",
        "fact_en": "The legal heritage of Madras High Court produced some of the greatest Advocates General in Commonwealth legal history.",
        "fact_ta": "மெட்ராஸ் உயர் நீதிமன்றத்தின் பாரம்பரியம் காமன்வெல்த் சட்ட வரலாற்றிலேயே மிகச்சிறந்த அட்வகேட் ஜெனரல்களை உருவாக்கியுள்ளது."
    }
]

def build_questions():
    questions = []
    for i, item in enumerate(raw_match_data):
        qid = f"ADVG_MF_{i+1:03d}"
        
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
                
        q = make_advg_q(
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
            tags=["polity", "advocate_general_of_a_state", "match_the_following", item["subtopic"].lower().replace(" ", "_")]
        )
        questions.append(q)
        
    return questions

if __name__ == "__main__":
    qs = build_questions()
    print(f"Generated {len(qs)} raw Match the Following questions.")
    
    balanced_qs = balance_question_keys(qs)
    
    out_path = os.path.join("data", "questions", "polity", "advocate_general_match_the_following.json")
    alias_path = os.path.join("data", "questions", "polity", "advocate_general_match.json")
    
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(balanced_qs, f, ensure_ascii=False, indent=2)
    shutil.copyfile(out_path, alias_path)
    
    print(f"Saved balanced Match MCQs to {out_path} and {alias_path}")
    
    val = ContentValidator()
    report = val.validate_file(out_path, expected_count=25, expected_prefix="ADVG_MF_")
    print(f"Validation Report: {'PASS' if report.is_valid else 'FAIL'} | Total: {report.total_audited}")
    if not report.is_valid:
        for iss in report.issues[:10]:
            print(f"  Issue: {iss}")
    print(f"Key Distribution: {report.key_distribution}")
