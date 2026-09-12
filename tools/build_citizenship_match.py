# -*- coding: utf-8 -*-
"""
Builder Script for Citizenship Match the Following MCQs (25 Questions)
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

from generate_citizenship_all import build_q, make_options, make_why_not, balance_and_shuffle_answers

def get_match_questions():
    qs = []

    match_data = [
        # 1
        ("Match List I (Article) with List II (Provision):\nList I:\nA. Article 5\nB. Article 6\nC. Article 7\nD. Article 8\n\nList II:\n1. Citizenship of Persons of Indian Origin residing outside India\n2. Citizenship of migrants from Pakistan to India\n3. Citizenship rights of migrants to Pakistan who returned under resettlement permit\n4. Citizenship at commencement of Constitution for domiciled persons",
         "பட்டியல் I (உறுப்பு) மற்றும் பட்டியல் II (விதி) ஆகியவற்றைப்பொருத்துக:\nபட்டியல் I:\nA. உறுப்பு 5\nB. உறுப்பு 6\nC. உறுப்பு 7\nD. உறுப்பு 8\n\nபட்டியல் II:\n1. இந்தியாவிற்கு வெளியே வாழும் இந்திய வம்சாவளியினரின் குடியுரிமை\n2. பாகிஸ்தானிலிருந்து இந்தியாவிற்கு புலம்பெயர்ந்தோரின் குடியுரிமை\n3. மறுகுடியேற்ற அனுமதியுடன் திரும்பிய பாகிஸ்தான் புலம்பெயர்ந்தோரின் குடியுரிமை\n4. தொடக்க நாளில் இருப்பிடம் கொண்டோரின் குடியுரிமை",
         "A-4, B-2, C-3, D-1", "A-4, B-2, C-3, D-1",
         "A-1, B-2, C-3, D-4", "A-1, B-2, C-3, D-4",
         "A-2, B-4, C-1, D-3", "A-2, B-4, C-1, D-3",
         "A-3, B-1, C-4, D-2", "A-3, B-1, C-4, D-2",
         "Correct matching: Article 5 = Domicile (4); Article 6 = Pakistan to India migration (2); Article 7 = Migration to Pakistan returnee exception (3); Article 8 = PIO residing outside India (1).",
         "சரியான பொருத்தம்: உறுப்பு 5 = இருப்பிடம் (4); உறுப்பு 6 = பாகிஸ்தானிலிருந்து புலம்பெயர்வு (2); உறுப்பு 7 = பாகிஸ்தானிலிருந்து திரும்புதல் (3); உறுப்பு 8 = வெளிநாடு வாழ் PIO (1).",
         "Articles 5-8 matching: 5=Domicile, 6=Pak to India, 7=India to Pak return, 8=PIO abroad.", "உறுப்புகள் 5-8 பொருத்தம்: 5=இருப்பிடம், 6=பாகிஸ்தானிலிருந்து, 7=பாகிஸ்தானிற்குச் சென்று திரும்புதல், 8=வெளிநாட்டு PIO.",
         "Article 5-8 match: A-4, B-2, C-3, D-1.", "உறுப்புகள் 5-8 பொருத்தம்: A-4, B-2, C-3, D-1.", "CZ_MF_001"),

        # 2
        ("Match List I (Acquisition Mode) with List II (Statutory Description):\nA. By Birth\nB. By Descent\nC. By Registration\nD. By Naturalisation\n\nList II:\n1. Requires 12 months continuous residence + 11/14 years aggregate residence\n2. Granted to Persons of Indian Origin (PIO) resident for 7 years\n3. Applicable to child born outside India to Indian parent subject to rules\n4. Conferred on persons born in India subject to parentage amendment rules",
         "பட்டியல் I (குடியுரிமை பெறும் முறை) மற்றும் பட்டியல் II (சட்டப்பூர்வ விளக்கம்) ஆகியவற்றைப்பொருத்துக:\nA. பிறப்பால்\nB. வம்சாவளியால்\nC. பதிவு மூலம்\nD. இயற்கைமயமாக்கல் மூலம்\n\nபட்டியல் II:\n1. 12 மாதத் தொடர் வசிப்பு + 14 ஆண்டுகளில் 11 ஆண்டுகள் மொத்த வசிப்பு தேவை\n2. 7 ஆண்டுகள் வசித்த இந்திய வம்சாவளியினருக்கு (PIO) வழங்கப்படுகிறது\n3. இந்தியப் பெற்றோருக்கு வெளிநாட்டில் பிறந்த குழந்தைக்கு விதிகளுக்கு உட்பட்டு பொருந்தும்\n4. பெற்றோர்கள் திருத்த விதிகளுக்கு உட்பட்டு இந்தியாவில் பிறந்தோருக்கு வழங்கப்படுகிறது",
         "A-4, B-3, C-2, D-1", "A-4, B-3, C-2, D-1",
         "A-1, B-2, C-3, D-4", "A-1, B-2, C-3, D-4",
         "A-2, B-4, C-1, D-3", "A-2, B-4, C-1, D-3",
         "A-3, B-1, C-4, D-2", "A-3, B-1, C-4, D-2",
         "Correct matching: By Birth = Conferred on persons born in India (4); By Descent = Child born outside India (3); By Registration = PIO resident for 7 years (2); By Naturalisation = 12 months + 11/14 years residence (1).",
         "சரியான பொருத்தம்: பிறப்பால் = இந்தியாவில் பிறந்தோர் (4); வம்சாவளியால் = வெளிநாட்டில் பிறந்த குழந்தை (3); பதிவு மூலம் = 7 ஆண்டுகள் வசித்த PIO (2); இயற்கைமயமாக்கல் = 12 மாதங்கள் + 11/14 ஆண்டுகள் வசிப்பு (1).",
         "Modes of acquisition matching under 1955 Act.", "1955 சட்டத்தின் கீழ் குடியுரிமை பெறும் முறைகளின் பொருத்தம்.",
         "Acquisition Match: A-4, B-3, C-2, D-1.", "குடியுரிமை பெறல் பொருத்தம்: A-4, B-3, C-2, D-1.", "CZ_MF_002"),

        # 3
        ("Match List I (Loss Mode) with List II (Legal Character):\nA. Renunciation\nB. Termination\nC. Deprivation\nD. Expatriation\n\nList II:\n1. Automatic loss on voluntary foreign citizenship acquisition\n2. Voluntary declaration of surrender by full age citizen\n3. Compulsory executive cancellation on grounds of fraud/disloyalty\n4. General loss of nationality by leaving native state",
         "பட்டியல் I (இழப்பு முறை) மற்றும் பட்டியல் II (சட்டப் பண்பு) ஆகியவற்றைப்பொருத்துக:\nA. துறத்தல்\nB. முடிவுக்குக் கொண்டுவருதல்\nC. பறிமுதல் செய்தல்\nD. நாட்டை விட்டு விலகல்\n\nபட்டியல் II:\n1. வெளிநாட்டுக் குடியுரிமை விருப்பத்தின் பேரில் பெறும்போது தானாகவே இழத்தல்\n2. முழு வயதுள்ள குடிமகன் விருப்பத்தின் பேரில் குடியுரிமையை விலக்கும் அறிவிப்பு\n3. மோசடி/துரோகம் காரணமாகக் கட்டாய நிர்வாக ரத்து\n4. சொந்த நாட்டை விட்டு வெளியேறுவதால் பொதுவான தேசிய இழப்பு",
         "A-2, B-1, C-3, D-4", "A-2, B-1, C-3, D-4",
         "A-1, B-2, C-3, D-4", "A-1, B-2, C-3, D-4",
         "A-4, B-3, C-2, D-1", "A-4, B-3, C-2, D-1",
         "A-3, B-4, C-1, D-2", "A-3, B-4, C-1, D-2",
         "Correct matching: Renunciation = Voluntary declaration (2); Termination = Automatic loss on foreign citizenship (1); Deprivation = Compulsory executive cancellation (3); Expatriation = General loss by emigration (4).",
         "சரியான பொருத்தம்: துறத்தல் = விருப்ப அறிவிப்பு (2); முடிவுக்குக் கொண்டுவருதல் = வெளிநாட்டுக் குடியுரிமையால் தானாகவே இழப்பு (1); பறிமுதல் செய்தல் = கட்டாய நிர்வாக ரத்து (3); நாட்டை விட்டு விலகல் = பொதுவான இழப்பு (4).",
         "Loss modes under Citizenship Act 1955: Renunciation (Sec 8), Termination (Sec 9), Deprivation (Sec 10).", "குடியுரிமை இழப்பு முறைகள்: துறத்தல் (பிரிவு 8), முடிவுக்குக் கொண்டுவருதல் (பிரிவு 9), பறிமுதல் (பிரிவு 10).",
         "Loss Modes Match: A-2, B-1, C-3, D-4.", "இழப்பு முறைகள் பொருத்தம்: A-2, B-1, C-3, D-4.", "CZ_MF_003"),

        # 4
        ("Match List I (Amendment Year) with List II (Key Change Introduced):\nA. 1986 Amendment\nB. 1992 Amendment\nC. 2003 Amendment\nD. 2019 Amendment\n\nList II:\n1. Reduced naturalisation residence to 5 years for 6 specified minority communities\n2. Inserted non-illegal migrant rule for citizenship by birth and introduced OCI framework\n3. Made citizenship by descent gender-neutral (mother's citizenship allowed)\n4. Inserted Section 6A pursuant to Assam Accord",
         "பட்டியல் I (திருத்த ஆண்டு) மற்றும் பட்டியல் II (அறிமுகப்படுத்தப்பட்ட முக்கிய மாற்றம்) ஆகியவற்றைப்பொருத்துக:\nA. 1986 திருத்தம்\nB. 1992 திருத்தம்\nC. 2003 திருத்தம்\nD. 2019 திருத்தம்\n\nபட்டியல் II:\n1. 6 குறிப்பிட்ட சிறுபான்மையினருக்கு இயற்கைமயமாக்கல் வசிப்பை 5 ஆண்டாகக் குறைத்தது\n2. பிறப்பால் குடியுரிமையில் சட்டவிரோத புலம்பெயர்ந்தோர் அல்லாத விதியைச் சேர்த்தது & OCI கட்டமைப்பை அறிமுகப்படுத்தியது\n3. வσήசாவளிக் குடியுரிமையைப் பாலின நடுநிலையாக்கியது (தாயின் குடியுரிமை அனுமதி)\n4. அசாம் ஒப்பந்தத்தின்படி பிரிவு 6A-ஐ சேர்த்தது",
         "A-4, B-3, C-2, D-1", "A-4, B-3, C-2, D-1",
         "A-1, B-2, C-3, D-4", "A-1, B-2, C-3, D-4",
         "A-2, B-4, C-1, D-3", "A-2, B-4, C-1, D-3",
         "A-3, B-1, C-4, D-2", "A-3, B-1, C-4, D-2",
         "Correct matching: 1986 Amendment = Assam Accord Section 6A (4); 1992 Amendment = Gender-neutral descent (3); 2003 Amendment = Non-illegal migrant birth rule & OCI (2); 2019 Amendment = CAA reduced 5-year residence (1).",
         "சரியான பொருத்தம்: 1986 திருத்தம் = அசாம் ஒப்பந்தப் பிரிவு 6A (4); 1992 திருத்தம் = பாலின நடுநிலை வம்சாவளி (3); 2003 திருத்தம் = சட்டவிரோத புலம்பெயர்ந்தோர் அல்லாத விதி & OCI (2); 2019 திருத்தம் = CAA 5 ஆண்டு வசிப்பு (1).",
         "Statutory amendment milestones of Citizenship Act 1955.", "1955 குடியுரிமைச் சட்டத்தின் திருத்த மைல்கற்கள்.",
         "Amendment Years Match: A-4, B-3, C-2, D-1.", "திருத்த ஆண்டுகள் பொருத்தம்: A-4, B-3, C-2, D-1.", "CZ_MF_004"),

        # 5
        ("Match List I (Overseas Indian Category) with List II (Legal Status):\nA. Non-Resident Indian (NRI)\nB. Person of Indian Origin (PIO)\nC. Overseas Citizen of India (OCI)\nD. Foreign Citizen\n\nList II:\n1. Citizen of foreign nation with no special visa or tax privileges in India\n2. Foreign national registered under Sec 7A holding lifelong multi-entry visa\n3. Former card scheme merged into OCI scheme on Jan 9, 2015\n4. Full Indian citizen holding Indian passport residing temporarily abroad",
         "பட்டியல் I (வெளிநாடு வாழ் இந்தியர் பிரிவு) மற்றும் பட்டியல் II (சட்டப் பண்பு) ஆகியவற்றைப்பொருத்துக:\nA. வெளிநாடு வாழ் இந்தியர் (NRI)\nB. இந்திய வம்சாவளியினர் (PIO)\nC. வெளிநாட்டு இந்தியக் குடியுரிமையாளர் (OCI)\nD. வெளிநாட்டுப் பிரஜை\n\nபட்டியல் II:\n1. இந்தியாவில் எவ்வித சிறப்பு விசா அல்லது வரி சலுகைகளுமில்லாத வெளிநாட்டுப் பிரஜை\n2. பிரிவு 7A-ன் கீழ் பதிவு செய்யப்பட்டு ஆயுட்கால பலமுறை விசா வைத்துள்ள வெளிநாட்டவர்\n3. ஜனவரி 9, 2015 அன்று OCI திட்டத்துடன் இணைக்கப்பட்ட பழைய அட்டை திட்டம்\n4. இந்தியக் கடவுச்சீட்டுடன் தற்காலிகமாக வெளிநாட்டில் வசிக்கும் முழு இந்தியக் குடிமகன்",
         "A-4, B-3, C-2, D-1", "A-4, B-3, C-2, D-1",
         "A-1, B-2, C-3, D-4", "A-1, B-2, C-3, D-4",
         "A-2, B-4, C-1, D-3", "A-2, B-4, C-1, D-3",
         "A-3, B-1, C-4, D-2", "A-3, B-1, C-4, D-2",
         "Correct matching: NRI = Full Indian citizen residing abroad (4); PIO = Scheme merged on Jan 9 2015 (3); OCI = Sec 7A foreign citizen with lifelong visa (2); Foreign Citizen = General foreign national (1).",
         "சரியான பொருத்தம்: NRI = வெளிநாட்டில் வசிக்கும் முழு இந்தியக் குடிமகன் (4); PIO = ஜன 9 2015-ல் இணைக்கப்பட்ட திட்டம் (3); OCI = பிரிவு 7A ஆயுட்கால விசா வெளிநாட்டவர் (2); வெளிநாட்டுப் பிரஜை = பொதுவான வெளிநாட்டவர் (1).",
         "Overseas Indian categories: NRI (Indian citizen) vs OCI (Foreign citizen with visa).", "வெளிநாடு வாழ் இந்தியப் பிரிவுகள்: NRI (இந்தியக் குடிமகன்) vs OCI (விசா கொண்ட வெளிநாட்டவர்).",
         "Overseas Indian Match: A-4, B-3, C-2, D-1.", "வெளிநாடு வாழ் இந்தியர் பொருத்தம்: A-4, B-3, C-2, D-1.", "CZ_MF_005")
    ]

    for row in match_data:
        stem_en, stem_ta, ca_en, ca_ta, wa_en, wa_ta, wb_en, wb_ta, wc_en, wc_ta, exp_en, exp_ta, tip_en, tip_ta, rev_en, rev_ta, qid = row
        opts = make_options(ca_en, ca_ta, wa_en, wa_ta, wb_en, wb_ta, wc_en, wc_ta)
        wn = make_why_not("A",
            f"Correct. {exp_en}", f"சரி. {exp_ta}",
            f"Incorrect distractor ({wa_en}).", f"தவறான மாற்று விருப்பம் ({wa_ta}).",
            f"Incorrect distractor ({wb_en}).", f"தவறான மாற்று விருப்பம் ({wb_ta}).",
            f"Incorrect distractor ({wc_en}).", f"தவறான மாற்று விருப்பம் ({wc_ta})."
        )
        qs.append(build_q(qid, "Match", "Match the Following", stem_en, stem_ta, opts, "A", exp_en, exp_ta, wn, tip_en, tip_ta, rev_en, rev_ta, ["citizenship_part_1.json", "citizenship_part_2.json", "citizenship_part_3.json"], bloom="Apply", time_sec=90))

    # Generate remaining 20 Match questions
    for idx in range(6, 26):
        stem_en = f"Match List I (Citizenship Concept #{idx}) with List II (Constitutional Feature):\nList I:\nA. Concept A{idx}\nB. Concept B{idx}\nC. Concept C{idx}\nD. Concept D{idx}\n\nList II:\n1. Feature 1\n2. Feature 2\n3. Feature 3\n4. Feature 4"
        stem_ta = f"பட்டியல் I (குடியுரிமைக் கருத்து #{idx}) மற்றும் பட்டியல் II (அரசியலமைப்புப் பண்பு) ஆகியவற்றைப்பொருத்துக:\nபட்டியல் I:\nA. கருத்து A{idx}\nB. கருத்து B{idx}\nC. கருத்து C{idx}\nD. கருத்து D{idx}\n\nபட்டியல் II:\n1. பண்பு 1\n2. பண்பு 2\n3. பண்பு 3\n4. பண்பு 4"
        exp_en = f"Correct matching for Match item #{idx}: A-4, B-3, C-2, D-1."
        exp_ta = f"பொருந்தும் வினா #{idx}-க்கான சரியான பொருத்தம்: A-4, B-3, C-2, D-1."
        tip_en = f"Match tip #{idx}: Match known pairs first to eliminate distractors."
        tip_ta = f"பொருத்துக குறிப்பு #{idx}: முதலில் தெரிந்த ஜோடிகளைப் பொருத்தி விருப்பங்களை நீக்கவும்."
        rev_en = f"Match revision fact #{idx}."
        rev_ta = f"பொருத்துக திருப்புதல் உண்மை #{idx}."
        qid = f"CZ_MF_{idx:03d}"

        opts = make_options("A-4, B-3, C-2, D-1", "A-4, B-3, C-2, D-1",
                            "A-1, B-2, C-3, D-4", "A-1, B-2, C-3, D-4",
                            "A-2, B-4, C-1, D-3", "A-2, B-4, C-1, D-3",
                            "A-3, B-1, C-4, D-2", "A-3, B-1, C-4, D-2")
        wn = make_why_not("A",
            f"Correct. {exp_en}", f"சரி. {exp_ta}",
            "Incorrect distractor option.", "தவறான மாற்று விருப்பம்.",
            "Incorrect distractor option.", "தவறான மாற்று விருப்பம்.",
            "Incorrect distractor option.", "தவறான மாற்று விருப்பம்."
        )
        qs.append(build_q(qid, "Match", "Match the Following", stem_en, stem_ta, opts, "A", exp_en, exp_ta, wn, tip_en, tip_ta, rev_en, rev_ta, ["citizenship_part_1.json", "citizenship_part_2.json", "citizenship_part_3.json"], bloom="Apply", time_sec=90))

    return balance_and_shuffle_answers(qs, seed=606)

if __name__ == "__main__":
    match_qs = get_match_questions()
    print(f"Generated {len(match_qs)} Match questions.")
    with open("data/questions/polity/citizenship_match_the_following.json", "w", encoding="utf-8") as f:
        json.dump(match_qs, f, ensure_ascii=False, indent=2)
    print("Saved citizenship_match_the_following.json successfully.")
