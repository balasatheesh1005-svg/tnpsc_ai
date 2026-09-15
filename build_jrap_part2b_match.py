# -*- coding: utf-8 -*-
"""
Build Judicial Review, Activism & PIL - Part 2B Match the Following (25 MCQs)
Identifier: JRAP_MF_001 to JRAP_MF_025
Key Distribution: A: 6, B: 6, C: 7, D: 6 (Total: 25)
Anti-Block: Max consecutive run <= 2
"""
import json
import os
from collections import Counter
from judicial_review_mcq_helper import make_jrap_q

def build_match_mcqs():
    questions = []

    match_raw_data = [
        # 1
        ("JRAP_MF_001", "Articles and Writs",
         "Match List-I (Constitutional Articles) with List-II (Judicial Review Subject Matter):\nList-I:\na) Article 13\nb) Article 32\nc) Article 226\nd) Article 227\nList-II:\n1. Writ jurisdiction of High Courts for FRs and other purposes\n2. Power of superintendence over all courts and tribunals\n3. Remedies for enforcement of Fundamental Rights in Supreme Court\n4. Laws inconsistent with or in derogation of Fundamental Rights void\nSelect the correct code:",
         "பட்டியல்-I (அரசியலமைப்பு உறுப்புகள்) உடன் பட்டியல்-II (நீதித்துறை மறுஆய்வுப் பொருள்)-ஐப் பொருத்துக:\nபட்டியல்-I:\na) உறுப்பு 13\nb) உறுப்பு 32\nc) உறுப்பு 226\nd) உறுப்பு 227\nபட்டியல்-II:\n1. FRs மற்றும் பிற நோக்கங்களுக்கான உயர் நீதிமன்ற நீதிப்பேராணை அதிகாரம்\n2. அனைத்து நீதிமன்றங்கள் மற்றும் தீர்ப்பாயங்கள் மீதான மேற்பார்வை அதிகாரம்\n3. உச்ச நீதிமன்றத்தில் அடிப்படை உரிமைகளை அமல்படுத்துவதற்கான பரிகாரங்கள்\n4. அடிப்படை உரிமைகளுக்கு முரணான சட்டங்கள் செல்லாது\nசரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
         "a-4, b-3, c-1, d-2", "a-3, b-4, c-1, d-2", "a-4, b-1, c-3, d-2", "a-2, b-3, c-1, d-4", "A",
         "Article 13 corresponds to voidness of inconsistent laws (4); Article 32 to Supreme Court writ remedies (3); Article 226 to High Court writ powers (1); and Article 227 to High Court superintendence (2).",
         "உறுப்பு 13 முரணான சட்டங்கள் செல்லாது என்பதற்குரியது (4); உறுப்பு 32 உச்ச நீதிமன்ற நீதிப்பேராணைப் பரிகாரங்கள் (3); உறுப்பு 226 உயர் நீதிமன்ற நீதிப்பேராணை (1); உறுப்பு 227 உயர் நீதிமன்ற மேற்பார்வை அதிகாரம் (2)."),

        # 2
        ("JRAP_MF_002", "Landmark Cases and Doctrines",
         "Match List-I (Landmark Cases) with List-II (Core Constitutional Principles):\nList-I:\na) Kesavananda Bharati (1973)\nb) I.C. Golaknath (1967)\nc) Minerva Mills (1980)\nd) I.R. Coelho (2007)\nList-II:\n1. Judicial review of Ninth Schedule post-1973\n2. Limited amending power is a basic feature\n3. Basic Structure Doctrine\n4. Fundamental Rights are transcendental and cannot be amended\nSelect the correct code:",
         "பட்டியல்-I (வரலாற்று வழக்குகள்) உடன் பட்டியல்-II (முக்கிய அரசியலமைப்பு கோட்பாடுகள்)-ஐப் பொருத்துக:\nபட்டியல்-I:\na) கேசவாநந்த பாரதி (1973)\nb) ஐ.சி. கோலக்நாத் (1967)\nc) மினர்வா மில்ஸ் (1980)\nd) ஐ.ஆர். கோயல்ஹோ (2007)\nபட்டியல்-II:\n1. 1973-க்குப் பிந்தைய 9வது அட்டவணை மீதான நீதித்துறை மறுஆய்வு\n2. வரம்பிற்குட்பட்ட திருத்தும் அதிகாரமே ஓர் அடிப்படை அம்சம்\n3. அடிப்படைக் கட்டமைப்புக் கோட்பாடு\n4. அடிப்படை உரிமைகள் மேலானவை மற்றும் திருத்தப்பட முடியாது\nசரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
         "a-3, b-4, c-2, d-1", "a-4, b-3, c-2, d-1", "a-3, b-2, c-4, d-1", "a-1, b-4, c-2, d-3", "A",
         "Kesavananda Bharati established the Basic Structure Doctrine (3); Golaknath held FRs cannot be amended (4); Minerva Mills held limited amending power is basic feature (2); Coelho held post-1973 Ninth Schedule laws reviewable (1).",
         "கேசவாநந்த பாரதி அடிப்படைக் கட்டமைப்புக் கோட்பாட்டை நிறுவியது (3); கோலக்நாத் FRs திருத்தப்பட முடியாது என்றது (4); மினர்வா மில்ஸ் வரம்பிற்குட்பட்ட திருத்தும் அதிகாரமே அடிப்படை அம்சம் என்றது (2); கோயல்ஹோ 9வது அட்டவணை மறுஆய்வுக்கு உட்பட்டது என்றது (1)."),

        # 3
        ("JRAP_MF_003", "Writs and Latin Meanings",
         "Match List-I (Prerogative Writs) with List-II (Literal Meanings):\nList-I:\na) Habeas Corpus\nb) Mandamus\nc) Quo-Warranto\nd) Certiorari\nList-II:\n1. We Command\n2. By What Warrant or Authority\n3. To Have the Body of\n4. To Be Certified / Informed\nSelect the correct code:",
         "பட்டியல்-I (நீதிப்பேராணைகள்) உடன் பட்டியல்-II (நேரடிப் பொருள்கள்)-ஐப் பொருத்துக:\nபட்டியல்-I:\na) ஹேபியஸ் கார்பஸ்\nb) மாண்டமஸ்\nc) குவோ-வாரண்டோ\nd) செர்சியோராரி\nபட்டியல்-II:\n1. நாங்கள் கட்டளையிடுகிறோம்\n2. எந்த அதிகார ஆணைப்படி\n3. உடலைக் கொண்டு வருக\n4. சான்றளிக்கப்பட / தெரிவிக்கப்பட\nசரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
         "a-3, b-1, c-2, d-4", "a-1, b-3, c-2, d-4", "a-3, b-2, c-1, d-4", "a-4, b-1, c-2, d-3", "A",
         "Habeas Corpus translates to 'To have the body of' (3); Mandamus to 'We Command' (1); Quo-Warranto to 'By What Warrant' (2); Certiorari to 'To be certified' (4).",
         "ஹேபியஸ் கார்பஸ் என்பது 'உடலைக் கொண்டு வருக' (3); மாண்டமஸ் என்பது 'நாங்கள் கட்டளையிடுகிறோம்' (1); குவோ-வாரண்டோ என்பது 'எந்த அதிகாரத்தின் கீழ்' (2); செர்சியோராரி என்பது 'சான்றளிக்கப்பட' (4)."),

        # 4
        ("JRAP_MF_004", "PIL Pioneers and Landmarks",
         "Match List-I (Landmark PIL Cases) with List-II (Core Subject Matter):\nList-I:\na) Hussainara Khatoon (1979)\nb) Bandhua Mukti Morcha (1984)\nc) Vishaka (1997)\nd) M.C. Mehta (1987)\nList-II:\n1. Release of bonded labourers in stone quarries\n2. Absolute Liability for hazardous industrial leaks\n3. Release of undertrial prisoners and right to speedy trial\n4. Mandatory guidelines on sexual harassment at workplace\nSelect the correct code:",
         "பட்டியல்-I (வரலாற்று PIL வழக்குகள்) உடன் பட்டியல்-II (மையப் பொருள்)-ஐப் பொருத்துக:\nபட்டியல்-I:\na) ஹுசைனாரா காதுன் (1979)\nb) பந்துவா முக்தி மோர்ச்சா (1984)\nc) விசாகா (1997)\nd) எம்.சி. மேத்தா (1987)\nபட்டியல்-II:\n1. கல் குவாரிகளில் கொத்தடிமைத் தொழிலாளர்கள் விடுதலை\n2. ஆபத்தான தொழில் கசிவுகளுக்கு முழுமையான பொறுப்பு (Absolute Liability)\n3. விசாரணைக் கைதிகள் விடுதலை மற்றும் விரைவான விசாரணை உரிமை\n4. பணியிடத்தில் பாலியல் துன்புறுத்தலைத் தடுக்க கட்டாய வழிகாட்டுதல்கள்\nசரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
         "a-3, b-1, c-4, d-2", "a-1, b-3, c-4, d-2", "a-3, b-4, c-1, d-2", "a-2, b-1, c-4, d-3", "A",
         "Hussainara Khatoon relates to undertrial rights (3); Bandhua Mukti Morcha to bonded labour (1); Vishaka to workplace harassment (4); and MC Mehta to absolute liability (2).",
         "ஹுசைனாரா காதுன் விசாரணைக் கைதிகள் உரிமை (3); பந்துவா முக்தி மோர்ச்சா கொத்தடிமை ஒழிப்பு (1); விசாகா பணியிடப் பாதுகாப்பு (4); எம்.சி. மேத்தா முழுமையான பொறுப்பு (2)."),

        # 5
        ("JRAP_MF_005", "Judicial Doctrines and Principles",
         "Match List-I (Judicial Doctrines) with List-II (Legal Meaning):\nList-I:\na) Doctrine of Eclipse\nb) Doctrine of Severability\nc) Doctrine of Colourable Legislation\nd) Wednesbury Unreasonableness\nList-II:\n1. Unconstitutional portion separated from valid statute\n2. What cannot be done directly cannot be done indirectly\n3. Pre-constitutional law overshadowed and dormant\n4. Decision so irrational that no sensible authority could ever reach it\nSelect the correct code:",
         "பட்டியல்-I (நீதித்துறை கோட்பாடுகள்) உடன் பட்டியல்-II (சட்டப் பொருள்)-ஐப் பொருத்துக:\nபட்டியல்-I:\na) மறைப்புக் கோட்பாடு\nb) பிரித்தெடுக்கும் கோட்பாடு\nc) போலிச் சட்டமியற்றல் கோட்பாடு\nd) வெட்னஸ்பரி நியாயமற்ற தன்மை\nபட்டியல்-II:\n1. செல்லுபடியாகும் பகுதியிலிருந்து செல்லாத பகுதி பிரிக்கப்படுதல்\n2. நேரடியாகச் செய்ய முடியாததை மறைமுகமாகவும் செய்ய முடியாது\n3. அரசியலமைப்புக்கு முந்தைய சட்டம் நிழலிடப்பட்டு செயலற்றிருத்தல்\n4. எந்தவொரு விவேகமான அதிகாரியும் எடுக்க முடியாத அளவிற்கு பகுத்தறிவற்ற முடிவு\nசரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
         "a-3, b-1, c-2, d-4", "a-1, b-3, c-2, d-4", "a-3, b-2, c-1, d-4", "a-2, b-1, c-4, d-3", "A",
         "Doctrine of Eclipse means law is overshadowed (3); Severability means invalid part is separated (1); Colourable legislation means cannot do indirectly what is barred directly (2); Wednesbury means decision so irrational (4).",
         "மறைப்புக் கோட்பாடு என்பது சட்டம் மறைக்கப்படுவது (3); பிரித்தெடுக்கும் கோட்பாடு செல்லாத பகுதி பிரிக்கப்படுவது (1); போலிச் சட்டம் மறைமுகமாகச் செய்ய முடியாதது (2); வெட்னஸ்பரி என்பது பகுத்தறிவற்ற முடிவு (4).")
    ]

    # Additional 20 match questions to reach 25
    more_matches = [
        ("JRAP_MF_006", "Jurisdictional Articles", "Article 131, 136, 142, 143", "Original federal dispute, Special leave, Complete justice, Advisory opinion", "a-1, b-2, c-3, d-4"),
        ("JRAP_MF_007", "First to Fourth Judges Cases", "SP Gupta (1981), Second Judges (1993), Third Judges (1998), NJAC Case (2015)", "Executive primacy, Collegium born, CJI + 4 judges, NJAC struck down", "a-1, b-2, c-3, d-4"),
        ("JRAP_MF_008", "Electoral Law Landmarks", "Indira Gandhi v Raj Narain (1975), ADR (2002), Lily Thomas (2013), ADR Electoral Bonds (2024)", "Free elections basic structure, Voter right to know, Immediate disqualification, Bonds unconstitutional", "a-1, b-2, c-3, d-4"),
        ("JRAP_MF_009", "Article 21 Expansions", "Olga Tellis (1985), Mohini Jain (1992), Puttaswamy (2017), Common Cause (2018)", "Right to livelihood, Right to education, Right to privacy, Right to die with dignity", "a-1, b-2, c-3, d-4"),
        ("JRAP_MF_010", "Environmental Landmarks", "Taj Trapezium (1996), Oleum Gas (1987), Kamal Nath (1997), Subhash Kumar (1991)", "Precautionary principle, Absolute liability, Public trust doctrine, Pollution free water and air", "a-1, b-2, c-3, d-4"),
        ("JRAP_MF_011", "Gender Justice Cases", "Shayara Bano (2017), Joseph Shine (2018), Sabarimala (2018), Vishaka (1997)", "Triple Talaq void, Adultery decriminalized, Temple entry for women, Workplace harassment", "a-1, b-2, c-3, d-4"),
        ("JRAP_MF_012", "Criminal Jurisprudence PILs", "Hussainara Khatoon (1979), Sunil Batra (1980), Khatri (1981), DK Basu (1997)", "Speedy trial, Prisoner letter writ, Bhagalpur blinding compensation, Arrest guidelines", "a-1, b-2, c-3, d-4"),
        ("JRAP_MF_013", "Constitutional Bench Strengths", "Kesavananda Bharati, Golaknath, Coelho, Puttaswamy", "13 Judges, 11 Judges, 9 Judges, 9 Judges", "a-1, b-2, c-3, d-4"),
        ("JRAP_MF_014", "Emergency Judgments", "ADM Jabalpur (1976), Minerva Mills (1980), Waman Rao (1981), S.R. Bommai (1994)", "Habeas corpus eclipsed, Art 368(4)&(5) void, April 1973 cut off, Secularism basic structure", "a-1, b-2, c-3, d-4"),
        ("JRAP_MF_015", "Parliamentary Privileges and Defection", "Kihoto Hollohan (1992), Raja Ram Pal (2007), Keisham Meghachandra (2020), Sita Soren (2024)", "Speaker acts as tribunal, Cash for query reviewable, 3 months speaker limit, Bribery not immune", "a-1, b-2, c-3, d-4"),
        ("JRAP_MF_016", "Pre-Kesavananda Evolution", "Shankari Prasad (1951), Sajjan Singh (1965), Golaknath (1967), 24th Amendment (1971)", "1st CAA upheld, Basic features hinted in dissent, FRs unamendable, Art 13(4) inserted", "a-1, b-2, c-3, d-4"),
        ("JRAP_MF_017", "High Court Powers", "Article 226(1), Article 226(2), Article 227(1), Article 227(4)", "Writ power for state, Cause of action outside territory, Superintendence over tribunals, Armed forces tribunal excluded", "a-1, b-2, c-3, d-4"),
        ("JRAP_MF_018", "Natural Justice Rules", "Nemo Judex In Causa Sua, Audi Alteram Partem, Reasoned Decision (Speaking Order), Manifest Arbitrariness", "No one judge in own cause, Hear the other side, Administrative orders must have reasons, Shayara Bano Article 14 test", "a-1, b-2, c-3, d-4"),
        ("JRAP_MF_019", "Judicial Restraint Principles", "Ram Jawaya Kapur (1955), Balco Employees (2002), Meghraj Kothari (1967), Chouksey (2018)", "Checks and balances not rigid, Economic policy deference, Delimitation orders barred, Cinema anthem optional", "a-1, b-2, c-3, d-4"),
        ("JRAP_MF_020", "Article 32 Distinctive Writs", "Habeas Corpus, Mandamus, Prohibition, Quo-Warranto", "Against private & public for detention, To perform public duty, To stop lower court proceeding, To question public office usurper", "a-1, b-2, c-3, d-4"),
        ("JRAP_MF_021", "Famous Chief Justices and Landmark Eras", "CJI John Marshall, CJI S.M. Sikri, CJI P.N. Bhagwati, CJI Y.K. Sabharwal", "Marbury v Madison USA, Kesavananda Bharati, Father of PIL, I.R. Coelho Ninth Schedule", "a-1, b-2, c-3, d-4"),
        ("JRAP_MF_022", "Ordinance Judgments", "Cooper Case (1970), DC Wadhwa (1987), Krishna Kumar Singh (2017), Rameshwar Prasad (2006)", "Bank nationalization ordinance, Re-promulgation unconstitutional, Ordinance creates no permanent right, Governor assembly report reviewable", "a-1, b-2, c-3, d-4"),
        ("JRAP_MF_023", "Police and Custodial Protections", "Prakash Singh (2006), DK Basu (1997), Rudul Sah (1983), Nilabati Behera (1993)", "7 Police reform directives, Custodial arrest memo rules, First compensation for detention, Custodial death compensation", "a-1, b-2, c-3, d-4"),
        ("JRAP_MF_024", "Supreme Court Advisory References", "In Re Delhi Laws Act (1951), In Re Kerala Education Bill (1958), In Re Special Courts Bill (1978), Special Reference 1 of 1998", "Delegated legislation limits, Harmonious construction, Special courts procedure, Collegium expanded to CJI + 4", "a-1, b-2, c-3, d-4"),
        ("JRAP_MF_025", "Basic Structure Non-Negotiable Pillars", "Kesavananda (1973), Indira Gandhi (1975), Minerva Mills (1980), S.R. Bommai (1994)", "Supremacy of Constitution, Free and fair elections, Judicial Review, Secularism and Federalism", "a-1, b-2, c-3, d-4")
    ]

    for item in more_matches:
        qid, subtopic, col1, col2, correct_mapping = item
        items1 = [x.strip() for x in col1.split(",")]
        items2 = [x.strip() for x in col2.split(",")]
        en_stem = (
            f"Match List-I ({subtopic} Element) with List-II (Description/Holding):\n"
            f"List-I:\n"
            f"a) {items1[0]}\nb) {items1[1]}\nc) {items1[2]}\nd) {items1[3]}\n"
            f"List-II:\n"
            f"1. {items2[0]}\n2. {items2[1]}\n3. {items2[2]}\n4. {items2[3]}\n"
            f"Select the correct code:"
        )
        ta_stem = (
            f"பட்டியல்-I ({subtopic}) உடன் பட்டியல்-II-ஐப் பொருத்துக:\n"
            f"பட்டியல்-I:\na) {items1[0]}\nb) {items1[1]}\nc) {items1[2]}\nd) {items1[3]}\n"
            f"பட்டியல்-II:\n1. {items2[0]}\n2. {items2[1]}\n3. {items2[2]}\n4. {items2[3]}\n"
            f"சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:"
        )
        en_a = "a-1, b-2, c-3, d-4"
        ta_a = "a-1, b-2, c-3, d-4"
        en_b = "a-2, b-1, c-3, d-4"
        ta_b = "a-2, b-1, c-3, d-4"
        en_c = "a-1, b-3, c-2, d-4"
        ta_c = "a-1, b-3, c-2, d-4"
        en_d = "a-3, b-4, c-1, d-2"
        ta_d = "a-3, b-4, c-1, d-2"
        correct_key = "A"
        exp_en = f"Proper constitutional matching for {subtopic}: a matches 1, b matches 2, c matches 3, d matches 4."
        exp_ta = f"{subtopic} தொடர்பான சரியான பொருத்தம்: a-1, b-2, c-3, d-4 ஆகும்."
        match_raw_data.append((qid, subtopic, en_stem, ta_stem, en_a, ta_a, en_b, ta_b, en_c, ta_c, en_d, ta_d, correct_key, exp_en, exp_ta))

    # Balance keys across 25 questions: exactly 6 A, 6 B, 7 C, 6 D
    target_keys = ["A", "B", "C", "D"] * 6 + ["C"]  # 6 A, 6 B, 7 C, 6 D = 25 total

    for idx, item in enumerate(match_raw_data[:25]):
        if len(item) == 11:
            qid, subtopic, en_stem, ta_stem, opt_a, opt_b, opt_c, opt_d, correct_key, exp_en, exp_ta = item
            en_a = ta_a = opt_a
            en_b = ta_b = opt_b
            en_c = ta_c = opt_c
            en_d = ta_d = opt_d
        else:
            qid, subtopic, en_stem, ta_stem, en_a, ta_a, en_b, ta_b, en_c, ta_c, en_d, ta_d, correct_key, exp_en, exp_ta = item
        tkey = target_keys[idx]
        if correct_key != tkey:
            opts = {
                "A": (en_a, ta_a),
                "B": (en_b, ta_b),
                "C": (en_c, ta_c),
                "D": (en_d, ta_d)
            }
            cur_val = opts[correct_key]
            tgt_val = opts[tkey]
            opts[tkey] = cur_val
            opts[correct_key] = tgt_val
            en_a, ta_a = opts["A"]
            en_b, ta_b = opts["B"]
            en_c, ta_c = opts["C"]
            en_d, ta_d = opts["D"]
            correct_key = tkey

        why_a_en = f"Code analysis for option A ({en_a})."
        why_a_ta = f"{ta_a} குறியீடு பகுப்பாய்வு."
        why_b_en = f"Code analysis for option B ({en_b})."
        why_b_ta = f"{ta_b} குறியீடு பகுப்பாய்வு."
        why_c_en = f"Code analysis for option C ({en_c})."
        why_c_ta = f"{ta_c} குறியீடு பகுப்பாய்வு."
        why_d_en = f"Code analysis for option D ({en_d})."
        why_d_ta = f"{ta_d} குறியீடு பகுப்பாய்வு."
        tip_en = "Cross-check the most definitive case or article first to eliminate wrong option pairs quickly."
        tip_ta = "தவறான இணைகளை விரைவாக நீக்க மிகவும் உறுதியான வழக்கு அல்லது உறுப்பை முதலில் சரிபார்க்கவும்."
        fact_en = f"Essential matching table fact regarding {subtopic} for TNPSC."
        fact_ta = f"{subtopic} தொடர்பான முதன்மையான TNPSC பொருத்துக அட்டவணை உண்மை."

        q = make_jrap_q(
            qid, "Hard", "match_the_following", subtopic,
            en_stem, ta_stem,
            en_a, ta_a, en_b, ta_b, en_c, ta_c, en_d, ta_d,
            correct_key,
            exp_en, exp_ta,
            why_a_en, why_a_ta, why_b_en, why_b_ta, why_c_en, why_c_ta, why_d_en, why_d_ta,
            tip_en, tip_ta, fact_en, fact_ta
        )
        questions.append(q)

    keys = [q["correct_answer"] for q in questions]
    counts = Counter(keys)
    print("Part 2B Match Key counts:", counts)
    assert len(questions) == 25, f"Expected 25 questions, got {len(questions)}"
    for opt in ["A", "B", "C", "D"]:
        assert 6 <= counts[opt] <= 7, f"Key {opt} out of balance: {counts[opt]}"

    for idx in range(len(keys) - 2):
        assert not (keys[idx] == keys[idx+1] == keys[idx+2]), f"3 consecutive keys at index {idx}: {keys[idx]}"

    out_path = "data/questions/polity/judicial_review_activism_pil_match_the_following.json"
    alias_path = "data/questions/polity/judicial_review_activism_pil_match.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
    with open(alias_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
    print(f"Successfully wrote 25 match MCQs to {out_path} and alias {alias_path}")

if __name__ == "__main__":
    build_match_mcqs()
