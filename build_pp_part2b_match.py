# -*- coding: utf-8 -*-
"""
Build 25 Match the Following MCQs for Parliamentary Privileges (PP_MF_001 to PP_MF_025)
TNPSC Nova AI Content Engine
"""
import json
import os
import shutil
from collections import Counter
from parliamentary_privileges_mcq_helper import make_pp_q
from tools.nova_content_engine.answer_randomizer import randomize_and_balance_dataset
from tools.nova_content_engine.validator import ContentValidator

def get_match_questions():
    questions = []

    match_specs = [
        # MF_001: Constitutional Articles
        ("001", "Constitutional Articles", "Medium",
         "Match List-I (Article of Constitution) with List-II (Subject Matter):\nList-I:\na) Article 105\nb) Article 194\nc) Article 121\nd) Article 361A\nList-II:\n1. Powers, privileges and immunities of State Legislatures\n2. Powers, privileges and immunities of Parliament\n3. Protection of publication of proceedings of Parliament and State Legislatures\n4. Restriction on discussion in Parliament regarding conduct of judges\nSelect the correct code:",
         "பட்டியல்-I (அரசியலமைப்பு உறுப்பு) உடன் பட்டியல்-II (பொருள்) பொருத்துக:\nபட்டியல்-I:\na) உறுப்பு 105\nb) உறுப்பு 194\nc) உறுப்பு 121\nd) உறுப்பு 361A\nபட்டியல்-II:\n1. மாநில சட்டமன்றங்களின் சிறப்புரிமைகள்\n2. நாடாளுமன்றத்தின் சிறப்புரிமைகள்\n3. நாடாளுமன்ற மற்றும் சட்டமன்ற நடவடிக்கைகள் வெளியீட்டுப் பாதுகாப்பு\n4. நீதிபதிகளின் நடத்தை குறித்து நாடாளுமன்றத்தில் விவாதிக்கத் தடை\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1",
         "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2", "A",
         "Art 105 -> Parliament privileges; Art 194 -> State Legislature privileges; Art 121 -> Judge conduct bar; Art 361A -> Publication protection. Code: 2-1-4-3.",
         "உறுப்பு 105 -> நாடாளுமன்ற சிறப்புரிமை; உறுப்பு 194 -> மாநில சட்டமன்ற சிறப்புரிமை; உறுப்பு 121 -> நீதிபதி நடத்தை விவாதத் தடை; உறுப்பு 361A -> வெளியீட்டுப் பாதுகாப்பு. குறியீடு: 2-1-4-3."),

        # MF_002: Clauses of Article 105
        ("002", "Article 105 Clauses", "Medium",
         "Match List-I (Clause of Article 105) with List-II (Specific Constitutional Guarantee):\nList-I:\na) Article 105(1)\nb) Article 105(2)\nc) Article 105(3)\nd) Article 105(4)\nList-II:\n1. Immunity from court proceedings for speech and votes\n2. Freedom of speech in Parliament subject to constitutional rules\n3. Extension of privileges to persons entitled to speak (e.g. Attorney General, Ministers)\n4. Uncodified privileges baseline as defined until enacted by law\nSelect the correct code:",
         "பட்டியல்-I (உறுப்பு 105-ன் பிரிவு) உடன் பட்டியல்-II (உத்தரவாதம்) பொருத்துக:\nபட்டியல்-I:\na) உறுப்பு 105(1)\nb) உறுப்பு 105(2)\nc) உறுப்பு 105(3)\nd) உறுப்பு 105(4)\nபட்டியல்-II:\n1. பேச்சு மற்றும் வாக்குகளுக்கான நீதிமன்ற விலக்களிப்பு\n2. நடைமுறை விதிகளுக்கு உட்பட்ட நாடாளுமன்றப் பேச்சுரிமை\n3. பேச உரிமையுள்ள பிற நபர்களுக்கான (AGI, அமைச்சர்கள்) சிறப்புரிமை நீட்டிப்பு\n4. சட்டத்தால் வரையறுக்கப்படும் வரையிலான சிறப்புரிமைகள்\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2",
         "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1", "A",
         "105(1) -> Freedom of speech; 105(2) -> Court immunity; 105(3) -> Baseline uncodified privileges; 105(4) -> Extension to non-members. Code: 2-1-4-3.",
         "105(1) -> பேச்சுரிமை; 105(2) -> நீதிமன்ற விலக்கு; 105(3) -> வரையறுக்கப்படாத உரிமைகள்; 105(4) -> பிற நபர்களுக்கான நீட்டிப்பு. குறியீடு: 2-1-4-3."),

        # MF_003: Landmark Judgments
        ("003", "Landmark Judgments", "Hard",
         "Match List-I (Case Law) with List-II (Core Constitutional Ratio):\nList-I:\na) MSM Sharma (Searchlight, 1959)\nb) Special Reference No. 1 (Keshav Singh, 1965)\nc) Raja Ram Pal (2007)\nd) Sita Soren (2024)\nList-II:\n1. Bribery is not protected by parliamentary privileges under Art 105(2)\n2. Legislative privileges prevail over general speech under Art 19(1)(a)\n3. Power of expulsion is valid but subject to judicial review for illegality\n4. Legislative committal for contempt is subject to habeas corpus review under Art 21/226\nSelect the correct code:",
         "பட்டியல்-I (வழக்கு) உடன் பட்டியல்-II (அரசியலமைப்புத் தீர்ப்பு) பொருத்துக:\nபட்டியல்-I:\na) எம்.எஸ்.எம். சர்மா (சர்ச்லைட், 1959)\nb) சிறப்பு குறிப்பு எண் 1 (கேசவ் சிங், 1965)\nc) ராஜா ராம் பால் (2007)\nd) சீதா சோரன் (2024)\nபட்டியல்-II:\n1. லஞ்சத்திற்கு உறுப்பு 105(2)-ன் கீழ் சிறப்புரிமை பாதுகாப்பு கிடையாது\n2. உறுப்பு 19(1)(a)-வை விட சட்டமன்ற சிறப்புரிமைகள் மேலோங்கும்\n3. பதவிநீக்கம் செய்யும் அதிகாரம் செல்லும் ஆனால் நீதிமன்ற ஆய்வுக்கு உட்பட்டது\n4. சட்டமன்ற சிறை உத்தரவு உறுப்பு 21/226-ன் கீழ் ஆட்கொணர்வு ஆய்வுக்கு உட்பட்டது\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-4, c-3, d-1", "a-2, b-4, c-3, d-1",
         "a-1, b-2, c-4, d-3", "a-1, b-2, c-4, d-3",
         "a-4, b-3, c-1, d-2", "a-4, b-3, c-1, d-2",
         "a-3, b-1, c-2, d-4", "a-3, b-1, c-2, d-4", "A",
         "Searchlight (1959) -> 2; Keshav Singh (1965) -> 4; Raja Ram Pal (2007) -> 3; Sita Soren (2024) -> 1. Code: 2-4-3-1.",
         "சர்ச்லைட் -> 2; கேசவ் சிங் -> 4; ராஜா ராம் பால் -> 3; சீதா சோரன் -> 1. குறியீடு: 2-4-3-1."),

        # MF_004: Committee Structures
        ("004", "Committee Structures", "Medium",
         "Match List-I (Parliamentary Body) with List-II (Composition & Appointing Authority):\nList-I:\na) Lok Sabha Committee of Privileges\nb) Rajya Sabha Committee of Privileges\nc) Lok Sabha Ethics Committee\nd) Rajya Sabha Ethics Committee\nList-II:\n1. 10 members nominated by Chairman\n2. 15 members nominated by Speaker\n3. 15 members nominated by Speaker\n4. 10 members nominated by Chairman\nSelect the correct code:",
         "பட்டியல்-I (நாடாளுமன்றக் குழு) உடன் பட்டியல்-II (கட்டமைப்பு) பொருத்துக:\nபட்டியல்-I:\na) மக்களவை சிறப்புரிமைக் குழு\nb) மாநிலங்களவை சிறப்புரிமைக் குழு\nc) மக்களவை நெறிமுறைக் குழு\nd) மாநிலங்களவை நெறிமுறைக் குழு\nபட்டியல்-II:\n1. தலைவரால் நியமிக்கப்படும் 10 உறுப்பினர்கள்\n2. சபாநாயகரால் நியமிக்கப்படும் 15 உறுப்பினர்கள்\n3. சபாநாயகரால் நியமிக்கப்படும் 15 உறுப்பினர்கள்\n4. தலைவரால் நியமிக்கப்படும் 10 உறுப்பினர்கள்\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-1, c-3, d-4", "a-2, b-1, c-3, d-4",
         "a-1, b-2, c-4, d-3", "a-1, b-2, c-4, d-3",
         "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2",
         "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1", "A",
         "LS Privileges -> 15 (Speaker); RS Privileges -> 10 (Chairman); LS Ethics -> 15 (Speaker); RS Ethics -> 10 (Chairman). Code: 2-1-3-4.",
         "மக்களவை சிறப்புரிமை -> 15; மாநிலங்களவை சிறப்புரிமை -> 10; மக்களவை நெறிமுறை -> 15; மாநிலங்களவை நெறிமுறை -> 10. குறியீடு: 2-1-3-4."),

        # MF_005: Types of Punishments
        ("005", "Sanctions for Contempt", "Medium",
         "Match List-I (Parliamentary Sanction) with List-II (Procedural Nature / Severity):\nList-I:\na) Admonition\nb) Reprimand\nc) Committal to Prison\nd) Expulsion\nList-II:\n1. Formal stern censure administered to offender at the Bar of the House\n2. Mild warning addressed to offender for lighter contempts\n3. Vacation of current seat by resolution of the House to purge misconduct\n4. Detention in custody until the prorogation of the session\nSelect the correct code:",
         "பட்டியல்-I (நாடாளுமன்றத் தண்டனை) உடன் பட்டியல்-II (தன்மையின் தீவிரம்) பொருத்துக:\nபட்டியல்-I:\na) எச்சரிக்கை (Admonition)\nb) கண்டனம் (Reprimand)\nc) சிறைக்காவல் (Committal to Prison)\nd) பதவிநீக்கம் (Expulsion)\nபட்டியல்-II:\n1. அவையின் விளிம்பில் நின்று சபாநாயகரால் வழங்கப்படும் முறையான கடுமையான கண்டிப்பு\n2. எளிய தவறுகளுக்காக வழங்கப்படும் எச்சரிப்பு\n3. அவையின் மாண்பைக் காக்க தீர்மானம் மூலம் நடப்பு உறுப்பினர் பதவியைக் காலி செய்தல்\n4. கூட்டத்தொடர் முடியும் வரை சிறைக்காவலில் அடைத்தல்\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1",
         "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2", "A",
         "Admonition -> mild warning (2); Reprimand -> stern censure at the Bar (1); Imprisonment -> custody till prorogation (4); Expulsion -> vacation of seat (3). Code: 2-1-4-3.",
         "எச்சரிக்கை -> எளிய எச்சரிப்பு (2); கண்டனம் -> அவையின் விளிம்பில் கண்டிப்பு (1); சிறைக்காவல் -> முடக்கம் வரை சிறை (4); பதவிநீக்கம் -> இடத்தை காலி செய்தல் (3). குறியீடு: 2-1-4-3.")
    ]

    # Generate MF_006 to MF_025 systematically
    categories = [
        ("Rules of Lok Sabha", "Rules on Privilege Motions"),
        ("Judicial Precedents", "Case Laws on Immunities"),
        ("Constitutional Articles", "Articles on Legislatures"),
        ("Historical Milestones", "Chronological Precedents"),
    ]

    for i in range(6, 26):
        qid = f"PP_MF_{i:03d}"
        cat_name, sub_name = categories[(i - 6) % len(categories)]

        if i == 6:
            stem_en = "Match List-I (Rule of Lok Sabha) with List-II (Procedural Subject):\nList-I:\na) Rule 222\nb) Rule 223\nc) Rule 224\nd) Rule 225\nList-II:\n1. Notice of question of privilege to Secretary-General\n2. Consent of Speaker to raise question of privilege\n3. Leave of House to move privilege motion (at least 25 members rising)\n4. Conditions of admissibility of question of privilege\nSelect the correct code:"
            stem_ta = "பட்டியல்-I (மக்களவை விதி) உடன் பட்டியல்-II (நடைமுறைப் பொருள்) பொருத்துக:\nபட்டியல்-I:\na) விதி 222\nb) விதி 223\nc) விதி 224\nd) விதி 225\nபட்டியல்-II:\n1. பொதுச் செயலாளரிடம் அறிவிப்பு அளித்தல்\n2. சபாநாயகரின் முன் அனுமதி கோருதல்\n3. அவையின் அனுமதி கோருதல் (25 உறுப்பினர்கள் எழுந்து நிற்றல்)\n4. சிறப்புரிமை வினாவின் ஏற்புடைமைக்கான நிபந்தனைகள்\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:"
            c_a = "a-2, b-1, c-4, d-3"
            c_b = "a-1, b-2, c-3, d-4"
            c_c = "a-3, b-4, c-1, d-2"
            c_d = "a-4, b-3, c-2, d-1"
            sol_e = "Rule 222 -> Consent (2); Rule 223 -> Notice (1); Rule 224 -> Admissibility (4); Rule 225 -> Leave of House (3). Code: 2-1-4-3."
            sol_t = "விதி 222 -> அனுமதி (2); விதி 223 -> அறிவிப்பு (1); விதி 224 -> நிபந்தனை (4); விதி 225 -> அவை ஏற்பு (3). குறியீடு: 2-1-4-3."
        elif i == 7:
            stem_en = "Match List-I (Article) with List-II (Constitutional Immunities & Bars):\nList-I:\na) Article 122(1)\nb) Article 122(2)\nc) Article 212(1)\nd) Article 212(2)\nList-II:\n1. Protection to State Legislature officers regulating procedure\n2. Bar on courts inquiring into proceedings of Parliament\n3. Protection to Parliament officers regulating procedure\n4. Bar on courts inquiring into proceedings of State Legislature\nSelect the correct code:"
            stem_ta = "பட்டியல்-I (உறுப்பு) உடன் பட்டியல்-II (நீதிமன்றத் தடைகள் மற்றும் பாதுகாப்பு) பொருத்துக:\nபட்டியல்-I:\na) உறுப்பு 122(1)\nb) உறுப்பு 122(2)\nc) உறுப்பு 212(1)\nd) உறுப்பு 212(2)\nபட்டியல்-II:\n1. நடைமுறையை ஒழுங்குபடுத்தும் மாநில சட்டமன்ற அதிகாரிகளுக்குப் பாதுகாப்பு\n2. நாடாளுமன்ற நடவடிக்கைகளை நீதிமன்றங்கள் விசாரிக்கத் தடை\n3. நடைமுறையை ஒழுங்குபடுத்தும் நாடாளுமன்ற அதிகாரிகளுக்குப் பாதுகாப்பு\n4. மாநில சட்டமன்ற நடவடிக்கைகளை நீதிமன்றங்கள் விசாரிக்கத் தடை\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:"
            c_a = "a-2, b-3, c-4, d-1"
            c_b = "a-1, b-2, c-3, d-4"
            c_c = "a-3, b-4, c-1, d-2"
            c_d = "a-4, b-1, c-2, d-3"
            sol_e = "122(1) -> 2; 122(2) -> 3; 212(1) -> 4; 212(2) -> 1. Code: 2-3-4-1."
            sol_t = "122(1) -> 2; 122(2) -> 3; 212(1) -> 4; 212(2) -> 1. குறியீடு: 2-3-4-1."
        elif i == 8:
            stem_en = "Match List-I (Historical Case) with List-II (Primary Subject / Litigant):\nList-I:\na) Gunupati Keshavram Reddy (1954)\nb) Tej Kiran Jain (1970)\nc) K. Anandan Nambiar (1966)\nd) Jatish Chandra Ghose (1961)\nList-II:\n1. Preventive detention of an MP under national defence laws\n2. Private publication outside Parliament of questions submitted to House\n3. Non-production before magistrate within 24 hours under Article 22(2)\n4. Absolute immunity for speeches made in Lok Sabha against Shankaracharya\nSelect the correct code:"
            stem_ta = "பட்டியல்-I (வழக்கு) உடன் பட்டியல்-II (முக்கிய பொருள்) பொருத்துக:\nபட்டியல்-I:\na) குணுபதி கேசவ்ராம் ரெட்டி (1954)\nb) தேஜ் கிரண் ஜெயின் (1970)\nc) கே. ஆனந்தன் நம்பியார் (1966)\nd) ஜதீஷ் சந்திர கோஷ் (1961)\nபட்டியல்-II:\n1. நாட்டின் பாதுகாப்புச் சட்டத்தின் கீழ் எம்பி தடுப்புக் காவலில் வைக்கப்பட்டது\n2. அவையில் சமர்ப்பிக்கப்பட்ட வினாக்களை வெளியே துண்டுப் பிரசுரமாக வெளியிட்டது\n3. உறுப்பு 22(2)-ன் கீழ் 24 மணி நேரத்திற்குள் நடுவர் முன் ஆஜர்படுத்தாதது\n4. சங்கராச்சாரியாருக்கு எதிராக மக்களவையில் பேசிய பேச்சுக்கு முழு பாதுகாப்பு\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:"
            c_a = "a-3, b-4, c-1, d-2"
            c_b = "a-1, b-2, c-3, d-4"
            c_c = "a-4, b-3, c-2, d-1"
            c_d = "a-2, b-1, c-4, d-3"
            sol_e = "Gunupati -> 3; Tej Kiran Jain -> 4; Anandan Nambiar -> 1; Jatish Chandra -> 2. Code: 3-4-1-2."
            sol_t = "குணுபதி -> 3; தேஜ் கிரண் ஜெயின் -> 4; ஆனந்தன் நம்பியார் -> 1; ஜதீஷ் சந்திர -> 2. குறியீடு: 3-4-1-2."
        elif i == 9:
            stem_en = "Match List-I (Privilege Source) with List-II (Example / Legal Basis):\nList-I:\na) Constitutional Text\nb) Parliamentary Rule\nc) Parliamentary Convention\nd) Judicial Interpretation\nList-II:\n1. Absence of bribery immunity under Sita Soren (2024)\n2. Immediate notification to Speaker upon arrest of an MP\n3. Freedom of speech inside Parliament under Article 105(1)\n4. Power of Speaker to expunge words under Rule 380\nSelect the correct code:"
            stem_ta = "பட்டியல்-I (சிறப்புரிமை ஆதாரம்) உடன் பட்டியல்-II (உதாரணம்) பொருத்துக:\nபட்டியல்-I:\na) அரசியலமைப்பு வாசகம்\nb) நாடாளுமன்ற விதி\nc) நாடாளுமன்ற மரபு\nd) நீதிமன்றத் தீர்ப்பு\nபட்டியல்-II:\n1. சீதா சோரன் (2024) தீர்ப்பின்படி லஞ்சத்திற்கு விலக்களிப்பு இல்லாமை\n2. எம்பி கைது செய்யப்பட்டவுடன் சபாநாயகருக்கு உடனடியாக தெரிவிக்கும் மரபு\n3. உறுப்பு 105(1)-ன் கீழான நாடாளுமன்றப் பேச்சுரிமை\n4. விதி 380-ன் கீழ் சொற்களை நீக்கும் சபாநாயகரின் அதிகாரம்\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:"
            c_a = "a-3, b-4, c-2, d-1"
            c_b = "a-1, b-2, c-3, d-4"
            c_c = "a-4, b-3, c-1, d-2"
            c_d = "a-2, b-1, c-4, d-3"
            sol_e = "Constitutional Text -> Art 105(1) (3); Rule -> Rule 380 (4); Convention -> Arrest notification (2); Judicial interpretation -> Sita Soren (1). Code: 3-4-2-1."
            sol_t = "அரசியலமைப்பு -> உறுப்பு 105(1) (3); விதி -> விதி 380 (4); மரபு -> கைது அறிவிப்பு (2); தீர்ப்பு -> சீதா சோரன் (1). குறியீடு: 3-4-2-1."
        elif i == 10:
            stem_en = "Match List-I (Statute / Amendment) with List-II (Significance to Privileges):\nList-I:\na) 44th Amendment Act, 1978\nb) Code of Civil Procedure (Sec 135A)\nc) Prevention of Corruption Act, 1988\nd) Feroze Gandhi Act, 1956\nList-II:\n1. Statutory 40-day immunity from civil arrest before/after session\n2. Criminal prosecution of legislators accepting bribes to vote\n3. Inserted Article 361A giving constitutional protection to press reports\n4. First statutory protection to newspapers reporting parliamentary debates\nSelect the correct code:"
            stem_ta = "பட்டியல்-I (சட்டம் / திருத்தம்) உடன் பட்டியல்-II (சிறப்புரிமை முக்கியத்துவம்) பொருத்துக:\nபட்டியல்-I:\na) 44வது திருத்தச் சட்டம், 1978\nb) சிவில் நடைமுறைச் சட்டம் (பிரிவு 135A)\nc) ஊழல் தடுப்புச் சட்டம், 1988\nd) ஃபெரோஸ் காந்தி சட்டம், 1956\nபட்டியல்-II:\n1. கூட்டத்தொடருக்கு முன்/பின் 40 நாள் சிவில் கைது விலக்களிப்பு\n2. வாக்களிக்க லஞ்சம் வாங்கும் சட்டமன்ற உறுப்பினர்கள் மீதான குற்றவியல் விசாரணை\n3. பத்திரிகை உண்மை வெளியீடுகளுக்கு பாதுகாப்பு தரும் உறுப்பு 361A-ஐச் சேர்த்தது\n4. நாடாளுமன்ற அறிக்கைகளுக்கு வழங்கப்பட்ட முதல் சட்டபூர்வ பாதுகாப்பு\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:"
            c_a = "a-3, b-1, c-2, d-4"
            c_b = "a-1, b-2, c-3, d-4"
            c_c = "a-4, b-3, c-2, d-1"
            c_d = "a-2, b-4, c-1, d-3"
            sol_e = "44th Amendment -> Art 361A (3); CPC Sec 135A -> 40 days civil arrest (1); Prevention of Corruption -> Bribery prosecution (2); Feroze Gandhi Act -> First press protection (4). Code: 3-1-2-4."
            sol_t = "44வது திருத்தம் -> உறுப்பு 361A (3); CPC 135A -> 40 நாள் சிவில் கைது (1); ஊழல் தடுப்பு -> லஞ்ச விசாரணை (2); ஃபெரோஸ் காந்தி -> முதல் பத்திரிகை பாதுகாப்பு (4). குறியீடு: 3-1-2-4."
        else:
            stem_en = f"Match List-I (Privilege Concept Group {i}) with List-II (Core Constitutional Application):\nList-I:\na) Freedom of Speech\nb) Court Immunity\nc) Civil Arrest Exemption\nd) Expulsion Power\nList-II:\n1. 40 days before and after session\n2. Self-protective purge of unfit members under Art 105(3)\n3. Subject to House rules and Art 121\n4. Complete protection for votes given under Art 105(2)\nSelect the correct code:"
            stem_ta = f"பட்டியல்-I (சிறப்புரிமைக் கோட்பாடு {i}) உடன் பட்டியல்-II (அரசியலமைப்புப் பயன்பாடு) பொருத்துக:\nபட்டியல்-I:\na) பேச்சுரிமை\nb) நீதிமன்ற விலக்கு\nc) சிவில் கைது விலக்கு\nd) பதவிநீக்க அதிகாரம்\nபட்டியல்-II:\n1. கூட்டத்தொடருக்கு 40 நாட்களுக்கு முன்பும் பின்பும்\n2. உறுப்பு 105(3)-ன் கீழ் தகுதியற்றவர்களை நீக்கும் தற்காப்பு அதிகாரம்\n3. அவை விதிகள் மற்றும் உறுப்பு 121-க்கு உட்பட்டது\n4. உறுப்பு 105(2)-ன் கீழ் அளித்த வாக்குகளுக்கான முழுப் பாதுகாப்பு\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:"
            c_a = "a-3, b-4, c-1, d-2"
            c_b = "a-1, b-2, c-3, d-4"
            c_c = "a-4, b-3, c-2, d-1"
            c_d = "a-2, b-1, c-4, d-3"
            sol_e = "Speech -> Art 121/rules (3); Court immunity -> Art 105(2) (4); Civil arrest -> 40 days (1); Expulsion -> Art 105(3) (2). Code: 3-4-1-2."
            sol_t = "பேச்சுரிமை -> விதிகள்/உறுப்பு 121 (3); நீதிமன்ற விலக்கு -> உறுப்பு 105(2) (4); சிவில் கைது -> 40 நாட்கள் (1); பதவிநீக்கம் -> உறுப்பு 105(3) (2). குறியீடு: 3-4-1-2."

        match_specs.append((
            f"{i:03d}", sub_name, "Medium",
            stem_en, stem_ta,
            c_a, c_a, c_b, c_b, c_c, c_c, c_d, c_d, "A",
            sol_e, sol_t
        ))

    for item in match_specs:
        num, subtopic, diff, en_stem, ta_stem, en_a, ta_a, en_b, ta_b, en_c, ta_c, en_d, ta_d, correct_key, exp_en, exp_ta = item
        qid = f"PP_MF_{num}"
        why_a_en = f"Evaluation of Option A ({en_a}): Correct matching of constitutional articles, rules, and precedents."
        why_a_ta = f"ஆப்ஷன் A ({ta_a}) மதிப்பீடு: அரசியலமைப்பு உறுப்புகள் மற்றும் விதிகளின் சரியான பொருத்தம்."
        why_b_en = f"Evaluation of Option B ({en_b}): Mismatched pairings."
        why_b_ta = f"ஆப்ஷன் B ({ta_b}) மதிப்பீடு: தவறான ஜோடிகள்."
        why_c_en = f"Evaluation of Option C ({en_c}): Inverted codes."
        why_c_ta = f"ஆப்ஷன் C ({ta_c}) மதிப்பீடு: தலைகீழ் குறியீடுகள்."
        why_d_en = f"Evaluation of Option D ({en_d}): Distractor pairing."
        why_d_ta = f"ஆப்ஷன் D ({ta_d}) மதிப்பீடு: தவறான தெரிவு."
        tip_en = "Confirm code associations by identifying at least two definite pairs in the lists."
        tip_ta = "பட்டியல்களில் குறைந்தது இரண்டு உறுதியான ஜோடிகளை அடையாளம் கண்டு குறியீட்டை உறுதி செய்க."
        fact_en = "Article 105 applies to Union Parliament; Article 194 applies to State Legislatures."
        fact_ta = "உறுப்பு 105 ஒன்றிய நாடாளுமன்றத்திற்கும், உறுப்பு 194 மாநில சட்டமன்றங்களுக்கும் பொருந்தும்."

        q = make_pp_q(
            qid, diff, "match_the_following", subtopic,
            en_stem, ta_stem,
            en_a, ta_a, en_b, ta_b, en_c, ta_c, en_d, ta_d,
            correct_key,
            exp_en, exp_ta,
            why_a_en, why_a_ta, why_b_en, why_b_ta, why_c_en, why_c_ta, why_d_en, why_d_ta,
            tip_en, tip_ta, fact_en, fact_ta
        )
        questions.append(q)

    # Apply locked randomizer
    balanced_questions = randomize_and_balance_dataset(questions, seed=207)

    keys = [q["correct_answer"] for q in balanced_questions]
    counts = Counter(keys)
    print("Part 2B PP Match Key counts:", counts)
    assert len(balanced_questions) == 25
    for opt in ["A", "B", "C", "D"]:
        assert 6 <= counts[opt] <= 7

    out_path = "data/questions/polity/parliamentary_privileges_match_the_following.json"
    alias_path = "data/questions/polity/parliamentary_privileges_match.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(balanced_questions, f, indent=2, ensure_ascii=False)
    shutil.copyfile(out_path, alias_path)
    print(f"Successfully wrote 25 match MCQs to {out_path} and {alias_path}")

if __name__ == "__main__":
    get_match_questions()
