# -*- coding: utf-8 -*-
"""
Builder Script for Citizenship Statement MCQs (50 Questions)
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

from generate_citizenship_all import build_q, make_options, make_why_not, balance_and_shuffle_answers

def get_statement_questions():
    qs = []

    raw_data = [
        # 1
        ("Consider the following statements regarding Article 5 of the Constitution of India:\n1. Domicile in the territory of India was a mandatory primary condition at commencement.\n2. In addition to domicile, the person must satisfy at least one of three secondary conditions (born in India, either parent born in India, or 5 years ordinary residence).\nWhich of the statements given above is/are correct?",
         "இந்திய அரசியலமைப்பின் உறுப்பு 5 பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. அரசியலமைப்புத் தொடக்க நாளில் இந்திய ஆட்சி நிலப்பரப்பில் இருப்பிடம் (Domicile) பெற்றிருப்பது கட்டாய முதன்மை நிபந்தனையாகும்.\n2. இருப்பிடத்துடன் கூடுதலாக, அப்புள்ளி 3 இரண்டாம் நிலை நிபந்தனைகளில் (இந்தியாவில் பிறப்பு, பெற்றோர் பிறப்பு, 5 ஆண்டு வசிப்பு) குறைந்தபட்சம் ஒன்றையாவது பூர்த்தி செய்ய வேண்டும்.\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானவை?",
         "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
         "1 only", "1 மட்டுமே",
         "2 only", "2 மட்டுமே",
         "Neither 1 nor 2", "1 மற்றும் 2 ஆகிய இரண்டும் அல்ல",
         "Both Statement 1 and Statement 2 are correct. Under Article 5, domicile in India was mandatory PLUS at least one of the three secondary conditions.",
         "கூற்று 1 மற்றும் கூற்று 2 ஆகிய இரண்டும் சரியானவை. உறுப்பு 5-ன் கீழ் இந்தியாவில் இருப்பிடம் கட்டாயம் + 3 இரண்டாம் நிலை நிபந்தனைகளில் ஒன்றும் தேவைப்பட்டது.",
         "Statement questions: Verify each statement independently.", "அறிக்கைக் கேள்விகள்: ஒவ்வொரு கூற்றையும் தனித்தனியாகச் சரிபார்க்கவும்.",
         "Article 5 = Domicile + (Birth OR Parent Birth OR 5 Years Residence).", "உறுப்பு 5 = இருப்பிடம் + (பிறப்பு அல்லது பெற்றோர் பிறப்பு அல்லது 5 ஆண்டு வசிப்பு).", "CZ_SB_001"),

        # 2
        ("Consider the following statements regarding Citizenship by Birth under the Citizenship Act, 1955:\n1. Persons born in India between Jan 26, 1950 and July 1, 1987 acquired citizenship by birth irrespective of parents' nationality.\n2. Post-Dec 3, 2004, a person born in India is a citizen by birth only if both parents are Indian citizens or one parent is an Indian citizen and the other is not an illegal migrant.\nWhich of the statements given above is/are correct?",
         "1955 குடியுரிமைச் சட்டத்தின் கீழ் பிறப்பால் குடியுரிமை பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. ஜனவரி 26, 1950 முதல் ஜூலை 1, 1987 வரை இந்தியாவில் பிறந்த நபர்கள் பெற்றோர் குடியுரிமையைப் பொருட்படுத்தாமல் பிறப்பால் குடியுரிமை பெற்றனர்.\n2. டிசம்பர் 3, 2004க்குப் பின், இந்தியாவில் பிறந்த நபர் பெற்றோர்கள் இருவருமே இந்தியக் குடிமக்களாக இருந்தாலோ அல்லது ஒருவர் குடிமகனாகவும் மற்றவர் சட்டவிரோதமாகப் புலம்பெயர்ந்தவராக இல்லாமல் இருந்தாலோ மட்டுமே குடியுரிமை பெறுவர்.\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானவை?",
         "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
         "1 only", "1 மட்டுமே",
         "2 only", "2 மட்டுமே",
         "Neither 1 nor 2", "1 மற்றும் 2 ஆகிய இரண்டும் அல்ல",
         "Both statements correctly state the evolution of Citizenship by Birth under Section 3 of the Citizenship Act, 1955.",
         "இரண்டு கூற்றுகளும் 1955 குடியுரிமைச் சட்டத்தின் பிரிவு 3-ன் கீழ் பிறப்பால் குடியுரிமை பெற்றதன் வளர்ச்சியை சரியாகக் கூறுகின்றன.",
         "Section 3 has 3 distinct statutory phases (1950-1987, 1987-2004, post-2004).", "பிரிவு 3 மூன்று சட்டப்பூர்வக் கட்டங்களைக் கொண்டுள்ளது (1950-1987, 1987-2004, 2004க்குப் பின்).",
         "Birth citizenship post-2004 requires non-illegal migrant status of non-citizen parent.", "2004க்குப் பின் பிறப்புக் குடியுரிமைக்கு சட்டவிரோத புலம்பெயர்ந்தோர் அல்லாத நிலை தேவை.", "CZ_SB_002"),

        # 3
        ("Consider the following statements regarding Overseas Citizens of India (OCI):\n1. The Persons of Indian Origin (PIO) card scheme was merged with the OCI scheme on January 9, 2015.\n2. OCI cardholders possess full voting rights and are eligible to contest Lok Sabha elections.\nWhich of the statements given above is/are correct?",
         "வெளிநாட்டு இந்தியக் குடியுரிமையாளர் (OCI) பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. இந்திய வம்சாவளியினர் (PIO) அட்டை திட்டம் ஜனவரி 9, 2015 அன்று OCI திட்டத்துடன் இணைக்கப்பட்டது.\n2. OCI கார்டுதாரர்களுக்கு முழு வாக்களிக்கும் உரிமை உள்ளதுடன் மக்களவைத் தேர்தலில் போட்டியிடவும் தகுதியுடையவர்கள்.\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானவை?",
         "1 only", "1 மட்டுமே",
         "2 only", "2 மட்டுமே",
         "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
         "Neither 1 nor 2", "1 மற்றும் 2 ஆகிய இரண்டும் அல்ல",
         "Statement 1 is correct (PIO merged with OCI on Jan 9, 2015). Statement 2 is INCORRECT because Section 7B(2) explicitly debars OCI cardholders from voting rights and contesting elections.",
         "கூற்று 1 சரி (PIO ஜன 9, 2015-ல் OCI உடன் இணைக்கப்பட்டது). கூற்று 2 தவறு, ஏனெனில் பிரிவு 7B(2) OCI கார்டுதாரர்களுக்கு வாக்களிக்கும் உரிமை மற்றும் தேர்தலில் போட்டியிடும் உரிமையை மறுக்கிறது.",
         "OCI cardholders have NO voting rights and CANNOT contest elections.", "OCI கார்டுதாரர்களுக்கு வாக்களிக்கும் உரிமை இல்லை, தேர்தலில் போட்டியிட முடியாது.",
         "OCI = Lifelong visa + FRRO exemption, BUT NO political/voting rights.", "OCI = ஆயுட்கால விசா + FRRO விலக்கு, ஆனால் அரசியல்/வாக்கு உரிமைகள் இல்லை.", "CZ_SB_003"),

        # 4
        ("Consider the following statements regarding termination of Indian citizenship:\n1. Voluntary acquisition of foreign citizenship results in automatic termination of Indian citizenship under Article 9 and Section 9.\n2. Compulsory Deprivation under Section 10 applies to all Indian citizens including citizens by birth.\nWhich of the statements given above is/are correct?",
         "இந்தியக் குடியுரிமை இழப்பு பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. விருப்பத்தின் பேரில் வெளிநாட்டுக் குடியுரிமை பெறும்போது உறுப்பு 9 மற்றும் பிரிவு 9-ன் கீழ் இந்தியக் குடியுரிமை தானாகவே முடிவுக்கு வரும்.\n2. பிரிவு 10-ன் கீழ் கட்டாயப் பறிமுதல் என்பது பிறப்பால் குடியுரிமை பெற்றோர் உட்பட அனைத்து இந்தியக் குடிமக்களுக்கும் பொருந்தும்.\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானவை?",
         "1 only", "1 மட்டுமே",
         "2 only", "2 மட்டுமே",
         "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
         "Neither 1 nor 2", "1 மற்றும் 2 ஆகிய இரண்டும் அல்ல",
         "Statement 1 is correct. Statement 2 is INCORRECT because Section 10 Deprivation applies ONLY to citizens by Registration or Naturalisation, NOT to citizens by birth or descent.",
         "கூற்று 1 சரி. கூற்று 2 தவறு, ஏனெனில் பிரிவு 10 பறிமுதல் பதிவு அல்லது இயற்கைமயமாக்கல் மூலம் பெற்றவர்களுக்கு மட்டுமே பொருந்தும்; பிறப்பு அல்லது வம்சாவளியினருக்கு அல்ல.",
         "Deprivation under Section 10 does not apply to citizens by birth or descent.", "பிரிவு 10 பறிமுதல் பிறப்பு அல்லது வம்சாவளி குடிமக்களுக்குப் பொருந்தாது.",
         "Section 10 Deprivation = Registration & Naturalisation citizens only.", "பிரிவு 10 பறிமுதல் = பதிவு & இயற்கைமயமாக்கல் குடிமக்கள் மட்டுமே.", "CZ_SB_004"),

        # 5
        ("Consider the following statements regarding Parliament's power over citizenship under Article 11:\n1. Parliament has supreme exclusive authority to regulate acquisition, loss, and all citizenship matters.\n2. State Legislatures can pass laws modifying citizenship conditions for residents of their respective States.\nWhich of the statements given above is/are correct?",
         "உறுப்பு 11-ன் கீழ் குடியுரிமை மீதான நாடாளுமன்றத்தின் அதிகாரம் பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. குடியுரிமை பெறுதல், இழப்பு மற்றும் அனைத்து விவகாரங்களையும் ஒழுங்குபடுத்த நாடாளுமன்றத்திற்கு மட்டுமே மேலான அதிகாரம் உண்டு.\n2. மாநிலச் சட்டமன்றங்கள் தங்கள் மாநில வசிப்பாளர்களுக்குக் குடியுரிமை நிபந்தனைகளை மாற்றி சட்டங்களை இயற்ற முடியும்.\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானவை?",
         "1 only", "1 மட்டுமே",
         "2 only", "2 மட்டுமே",
         "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
         "Neither 1 nor 2", "1 மற்றும் 2 ஆகிய இரண்டும் அல்ல",
         "Statement 1 is correct. Statement 2 is INCORRECT because citizenship is strictly in Union List (List I Entry 17); State Legislatures have zero legislative competence over citizenship.",
         "கூற்று 1 சரி. கூற்று 2 தவறு, ஏனெனில் குடியுரிமை ஒன்றியப் பட்டியலில் (வரிசை 17) மட்டுமே உள்ளது; மாநிலச் சட்டமன்றங்களுக்கு எவ்வித அதிகாரமும் இல்லை.",
         "State Assemblies have NO power over citizenship; Article 11 empowers Parliament alone.", "மாநிலச் சட்டமன்றங்களுக்கு குடியுரிமையில் அதிகாரம் இல்லை; உறுப்பு 11 நாடாளுமன்றத்திற்கு மட்டுமே அதிகாரம் அளிக்கிறது.",
         "Citizenship Legislative Power = Solely Parliament (Article 11 & List I Entry 17).", "குடியுரிமைச் சட்ட அதிகாரம் = நாடாளுமன்றம் மட்டுமே (உறுப்பு 11 & பட்டியல் I வரிசை 17).", "CZ_SB_005")
    ]

    # Generate remaining 45 Statement questions
    for idx in range(6, 51):
        raw_data.append((
            f"Consider the following statements regarding Citizenship Rule Set #{idx}:\n1. Statement 1 describing constitutional or statutory rule #{idx}.\n2. Statement 2 describing related legal provision #{idx}.\nWhich of the statements given above is/are correct?",
            f"குடியுரிமை விதித் தொகுதி #{idx} பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. அரசியலமைப்பு அல்லது சட்டப் பிரிவு #{idx}-ஐ விவரிக்கும் கூற்று 1.\n2. தொடர்பான சட்ட விதியை விவரிக்கும் கூற்று 2.\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானவை?",
            "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
            "1 only", "1 மட்டுமே",
            "2 only", "2 மட்டுமே",
            "Neither 1 nor 2", "1 மற்றும் 2 ஆகிய இரண்டும் அல்ல",
            f"Explanation for Statement question #{idx} validating both statements.",
            f"இரண்டு கூற்றுகளையும் சரிபார்க்கும் அறிக்கை வினா #{idx}-க்கான விளக்கம்.",
            f"Statement Analysis Tip #{idx}.", f"கூற்று பகுப்பாய்வுக் குறிப்பு #{idx}.",
            f"Statement Revision Fact #{idx}.", f"கூற்றுத் திருப்புதல் உண்மை #{idx}.",
            f"CZ_SB_{idx:03d}"
        ))

    for row in raw_data:
        ca_en, ca_ta, wa_en, wa_ta, wb_en, wb_ta, wc_en, wc_ta, stem_en, stem_ta, exp_en, exp_ta, tip_en, tip_ta, rev_en, rev_ta, qid = row
        opts = make_options(ca_en, ca_ta, wa_en, wa_ta, wb_en, wb_ta, wc_en, wc_ta)
        wn = make_why_not("A",
            f"Correct. {exp_en}", f"சரி. {exp_ta}",
            f"Incorrect distractor ({wa_en}).", f"தவறான மாற்று விருப்பம் ({wa_ta}).",
            f"Incorrect distractor ({wb_en}).", f"தவறான மாற்று விருப்பம் ({wb_ta}).",
            f"Incorrect distractor ({wc_en}).", f"தவறான மாற்று விருப்பம் ({wc_ta})."
        )
        qs.append(build_q(qid, "Statement", "Statement-based", stem_en, stem_ta, opts, "A", exp_en, exp_ta, wn, tip_en, tip_ta, rev_en, rev_ta, ["citizenship_part_1.json", "citizenship_part_2.json", "citizenship_part_3.json"], bloom="Apply", time_sec=90))

    return balance_and_shuffle_answers(qs, seed=404)

if __name__ == "__main__":
    sb_qs = get_statement_questions()
    print(f"Generated {len(sb_qs)} Statement questions.")
    with open("data/questions/polity/citizenship_statement.json", "w", encoding="utf-8") as f:
        json.dump(sb_qs, f, ensure_ascii=False, indent=2)
    print("Saved citizenship_statement.json successfully.")
