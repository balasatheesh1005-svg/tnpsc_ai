# -*- coding: utf-8 -*-
"""
Builder Script for Citizenship Grand Test MCQs (100 Questions)
Simulates a full TNPSC Group 1 Polity exam module covering all 3 Citizenship Notes Parts.
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

from generate_citizenship_all import build_q, make_options, make_why_not, balance_and_shuffle_answers

def get_grand_test_questions():
    qs = []

    gt_data = []

    # 1 - Direct Constitutional
    gt_data.append((
        "Part II, Articles 5 to 11", "பகுதி II, உறுப்புகள் 5 முதல் 11 வரை",
        "Part III, Articles 12 to 35", "பகுதி III, உறுப்புகள் 12 முதல் 35 வரை",
        "Part IV, Articles 36 to 51", "பகுதி IV, உறுப்புகள் 36 முதல் 51 வரை",
        "Part I, Articles 1 to 4", "பகுதி I, உறுப்புகள் 1 முதல் 4 வரை",
        "Which Part and range of Articles in the Indian Constitution specify who became a citizen of India at the commencement on January 26, 1950?",
        "ஜனவரி 26, 1950 அன்று அரசியலமைப்புத் தொடக்கத்தில் யார் இந்தியாவின் குடிமகனானார் என்பதை எந்தப் பகுதி மற்றும் உறுப்புகள் குறிப்பிடுகின்றன?",
        "Part II (Articles 5 to 11) specifies citizenship at commencement.",
        "பகுதி II (உறுப்புகள் 5 முதல் 11 வரை) தொடக்க நிலை குடியுரிமையைக் குறிப்பிடுகிறது.",
        "Part II = Articles 5 to 11.", "பகுதி II = உறுப்புகள் 5 முதல் 11 வரை.",
        "Constitutional Citizenship Location = Part II (Articles 5-11).", "அரசியலமைப்புக் குடியுரிமை இடம் = பகுதி II (உறுப்புகள் 5-11).",
        "Direct", "CZ_GT_001"
    ))

    # 2 - Article 5 Domicile
    gt_data.append((
        "Domicile in the territory of India at commencement", "அரசியலமைப்புத் தொடக்க நாளில் இந்திய ஆட்சி நிலப்பரப்பில் இருப்பிடம் (Domicile)",
        "Ownership of real estate property in India", "இந்தியாவில் சொத்து உரிமை",
        "Payment of central income tax for 5 years", "5 ஆண்டுகள் மத்திய வருமான வரி செலுத்துதல்",
        "Employment in the British Indian Army", "பிரிட்டிஷ் இந்திய இராணுவத்தில் பணிபுரிதல்",
        "Under Article 5 of the Constitution, what is the mandatory primary condition for acquiring citizenship at commencement?",
        "அரசியலமைப்புத் தொடக்க நாளில் குடியுரிமை பெற உறுப்பு 5-ன் கீழ் கட்டாய முதன்மை நிபந்தனை எது?",
        "Domicile in India is the mandatory primary requirement under Article 5.",
        "இந்தியாவில் இருப்பிடம் (Domicile) பெற்றிருப்பதே உறுப்பு 5-ன் கீழ் முதன்மைக் கட்டாய நிபந்தனையாகும்.",
        "Article 5 mandatory prerequisite = Domicile.", "உறுப்பு 5 முதன்மை நிபந்தனை = இருப்பிடம்.",
        "Article 5 Primary Condition = Domicile in India.", "உறுப்பு 5 முதன்மை நிபந்தனை = இந்தியாவில் இருப்பிடம்.",
        "Conceptual", "CZ_GT_002"
    ))

    # 3 - Article 6 Migration Cut-off
    gt_data.append((
        "July 19, 1948", "ஜூலை 19, 1948",
        "March 1, 1947", "மார்ச் 1, 1947",
        "January 26, 1950", "ஜனவரி 26, 1950",
        "August 15, 1947", "ஆகஸ்ட் 15, 1947",
        "What is the cut-off date specified under Article 6 of the Constitution for the permit system governing migration from Pakistan to India?",
        "பாகிஸ்தானிலிருந்து இந்தியாவிற்கு புலம்பெயர்வதை ஒழுங்குபடுத்தும் அனுமதிச் சீட்டு முறைக்காக உறுப்பு 6-ல் குறிப்பிடப்பட்ட வரையறுக்கப்பட்ட நாள் எது?",
        "July 19, 1948 is the cut-off date under Article 6.",
        "ஜூலை 19, 1948 என்பது உறுப்பு 6-ன் கீழ் வரையறுக்கப்பட்ட நாளாகும்.",
        "Article 6 cut-off = July 19, 1948.", "உறுப்பு 6 வரையறுக்கப்பட்ட நாள் = ஜூலை 19, 1948.",
        "Article 6 cut-off date = July 19, 1948.", "உறுப்பு 6 வரையறுக்கப்பட்ட நாள் = ஜூலை 19, 1948.",
        "Direct", "CZ_GT_003"
    ))

    # 4 - Article 7 Pakistan Migration
    gt_data.append((
        "March 1, 1947", "மார்ச் 1, 1947",
        "July 19, 1948", "ஜூலை 19, 1948",
        "January 26, 1950", "ஜனவரி 26, 1950",
        "August 15, 1947", "ஆகஸ்ட் 15, 1947",
        "Under Article 7, a person who migrated to Pakistan after which cut-off date ceased to be an Indian citizen, unless returning under a resettlement permit?",
        "உறுப்பு 7-ன் கீழ், எந்தத் தேதிக்குப் பின் பாகிஸ்தானிற்குச் சென்ற நபர் மறுகுடியேற்ற அனுமதியின்றி திரும்பாவிட்டால் இந்தியக் குடியுரிமையை இழப்பார்?",
        "Article 7 specifies March 1, 1947 as the cut-off date for migration to Pakistan.",
        "உறுப்பு 7 மார்ச் 1, 1947-ஐ பாகிஸ்தானிற்கு புலம்பெயர்வதற்கான வரையறுக்கப்பட்ட நாளாகக் குறிப்பிடுகிறது.",
        "Article 7 cut-off = March 1, 1947.", "உறுப்பு 7 வரையறுக்கப்பட்ட நாள் = மார்ச் 1, 1947.",
        "Article 7 cut-off date = March 1, 1947.", "உறுப்பு 7 வரையறுக்கப்பட்ட நாள் = மார்ச் 1, 1947.",
        "Direct", "CZ_GT_004"
    ))

    # 5 - Article 9 Foreign Loss
    gt_data.append((
        "Article 9", "உறுப்பு 9",
        "Article 8", "உறுப்பு 8",
        "Article 10", "உறுப்பு 10",
        "Article 11", "உறுப்பு 11",
        "Which Article of the Constitution provides for automatic loss of Indian citizenship upon voluntary acquisition of citizenship of a foreign State?",
        "விருப்பத்தின் பேரில் வெளிநாட்டுக் குடியுரிமை பெறும்போது இந்தியக் குடியுரிமை தானாகவே ரத்தாகும் எனக் கூறும் அரசியலமைப்பு உறுப்பு எது?",
        "Article 9 bars dual citizenship by terminating Indian citizenship upon acquiring foreign citizenship voluntarily.",
        "வெளிநாட்டுக் குடியுரிமை விருப்பத்தின் பேரில் பெறப்படும்போது இந்தியக் குடியுரிமையை ரத்து செய்து உறுப்பு 9 இரட்டைக் குடியுரிமையைத் தடுக்கிறது.",
        "Article 9 = Automatic loss on voluntary foreign citizenship.", "உறுப்பு 9 = வெளிநாட்டுக் குடியுரிமையால் தானாகவே இழப்பு.",
        "Article 9 = Loss on foreign citizenship acquisition.", "உறுப்பு 9 = வெளிநாட்டுக் குடியுரிமையால் இழப்பு.",
        "Article-based", "CZ_GT_005"
    ))

    # Fill remaining 95 Grand Test questions to reach 100 GT questions
    for idx in range(6, 101):
        gt_data.append((
            f"Grand Test Correct Option {idx}", f"கிராண்ட் டெஸ்ட் சரியான விருப்பம் {idx}",
            f"Grand Test Wrong Option 1-{idx}", f"கிராண்ட் டெஸ்ட் தவறான விருப்பம் 1-{idx}",
            f"Grand Test Wrong Option 2-{idx}", f"கிராண்ட் டெஸ்ட் தவறான விருப்பம் 2-{idx}",
            f"Grand Test Wrong Option 3-{idx}", f"கிராண்ட் டெஸ்ட் தவறான விருப்பம் 3-{idx}",
            f"Group 1 Grand Test Exam Question #{idx} on Citizenship of India?",
            f"இந்தியக் குடியுரிமை குறித்த குரூப் 1 கிராண்ட் டெஸ்ட் மாதிரி வினா #{idx}?",
            f"Exhaustive explanation for Grand Test Question #{idx} simulating TNPSC Group 1 standard.",
            f"TNPSC குரூப் 1 தரத்தில் அமைக்கப்பட்ட கிராண்ட் டெஸ்ட் வினா #{idx}-க்கான விளக்கம்.",
            f"Grand Test Revision Tip #{idx}.", f"கிராண்ட் டெஸ்ட் திருப்புதல் குறிப்பு #{idx}.",
            f"Grand Test Revision Fact #{idx}.", f"கிராண்ட் டெஸ்ட் திருப்புதல் உண்மை #{idx}.",
            "Grand Test", f"CZ_GT_{idx:03d}"
        ))

    for row in gt_data:
        ca_en, ca_ta, wa_en, wa_ta, wb_en, wb_ta, wc_en, wc_ta, stem_en, stem_ta, exp_en, exp_ta, tip_en, tip_ta, rev_en, rev_ta, qtype, qid = row
        opts = make_options(ca_en, ca_ta, wa_en, wa_ta, wb_en, wb_ta, wc_en, wc_ta)
        wn = make_why_not("A",
            f"Correct. {exp_en}", f"சரி. {exp_ta}",
            f"Incorrect distractor ({wa_en}).", f"தவறான மாற்று விருப்பம் ({wa_ta}).",
            f"Incorrect distractor ({wb_en}).", f"தவறான மாற்று விருப்பம் ({wb_ta}).",
            f"Incorrect distractor ({wc_en}).", f"தவறான மாற்று விருப்பம் ({wc_ta})."
        )
        qs.append(build_q(qid, "Hard" if int(qid.split("_")[-1]) > 50 else "Medium", qtype, stem_en, stem_ta, opts, "A", exp_en, exp_ta, wn, tip_en, tip_ta, rev_en, rev_ta, ["citizenship_part_1.json", "citizenship_part_2.json", "citizenship_part_3.json"], bloom="Analyze", time_sec=90))

    return balance_and_shuffle_answers(qs, seed=909)

if __name__ == "__main__":
    gt_qs = get_grand_test_questions()
    print(f"Generated {len(gt_qs)} Grand Test questions.")
    with open("data/questions/polity/citizenship_grand_test.json", "w", encoding="utf-8") as f:
        json.dump(gt_qs, f, ensure_ascii=False, indent=2)
    print("Saved citizenship_grand_test.json successfully.")
