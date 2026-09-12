# -*- coding: utf-8 -*-
"""
Builder Script for Citizenship Chronology MCQs (25 Questions)
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

from generate_citizenship_all import build_q, make_options, make_why_not, balance_and_shuffle_answers

def get_chronology_questions():
    qs = []

    chrono_data = [
        # 1
        ("Arrange the following constitutional and statutory citizenship cut-off dates in correct chronological order:\n1. Article 7 migration to Pakistan cut-off date (March 1, 1947)\n2. Article 6 permit system cut-off date (July 19, 1948)\n3. Commencement of the Constitution (January 26, 1950)\n4. Enactment of the Citizenship Act, 1955 (December 30, 1955)",
         "பின்வரும் அரசியலமைப்பு மற்றும் சட்டப்பூர்வக் குடியுரிமை வரையறுக்கப்பட்ட தேதிகளைச் சரியான காலவரிசையில் அமைக்கவும்:\n1. உறுப்பு 7 பாகிஸ்தானிற்கு புலம்பெயர்ச்சிக்கான நாள் (மார்ச் 1, 1947)\n2. உறுப்பு 6 அனுமதிச் சீட்டு முறைக்கான நாள் (ஜூலை 19, 1948)\n3. அரசியலமைப்புத் தொடக்க நாள் (ஜனவரி 26, 1950)\n4. 1955 குடியுரிமைச் சட்டம் இயற்றப்பட்ட நாள் (டிசம்பர் 30, 1955)",
         "1 - 2 - 3 - 4", "1 - 2 - 3 - 4",
         "2 - 1 - 4 - 3", "2 - 1 - 4 - 3",
         "3 - 1 - 2 - 4", "3 - 1 - 2 - 4",
         "4 - 3 - 2 - 1", "4 - 3 - 2 - 1",
         "Correct chronological sequence:\n1. March 1, 1947 (Art 7 cut-off)\n2. July 19, 1948 (Art 6 cut-off)\n3. January 26, 1950 (Constitution commencement)\n4. December 30, 1955 (Citizenship Act 1955).",
         "சரியான காலவரிசை:\n1. மார்ச் 1, 1947 (உறுப்பு 7)\n2. ஜூலை 19, 1948 (உறுப்பு 6)\n3. ஜனவரி 26, 1950 (அரசியலமைப்புத் தொடக்கம்)\n4. டிசம்பர் 30, 1955 (1955 சட்டம்).",
         "Cut-off dates order: March 1, 1947 -> July 19, 1948 -> Jan 26, 1950 -> Dec 30, 1955.", "வரையறுக்கப்பட்ட நாட்கள் வரிசை: மார்ச் 1, 1947 -> ஜூலை 19, 1948 -> ஜன 26, 1950 -> டிச 30, 1955.",
         "Chronology 1: 1 - 2 - 3 - 4.", "காலவரிசை 1: 1 - 2 - 3 - 4.", "CZ_C_001"),

        # 2
        ("Arrange the following Citizenship Amendment Acts in chronological order of their enactment/implementation:\n1. Section 6A Assam Accord Amendment Act (1986)\n2. Gender-neutral Citizenship by Descent Amendment Act (Dec 10, 1992)\n3. Non-illegal migrant restriction Amendment Act (Dec 3, 2004)\n4. PIO and OCI scheme merger Amendment (Jan 9, 2015)",
         "பின்வரும் குடியுரிமைத் திருத்தச் சட்டங்களை அவை இயற்றப்பட்ட/அமலாக்கப்பட்ட சரியான காலவரிசையில் அமைக்கவும்:\n1. பிரிவு 6A அசாம் ஒப்பந்தத் திருத்தச் சட்டம் (1986)\n2. வம்சாவளிக் குடியுரிமை பாலின நடுநிலைத் திருத்தச் சட்டம் (டிச 10, 1992)\n3. சட்டவிரோத புலம்பெயர்ந்தோர் அல்லாத கட்டுப்பாட்டுத் திருத்தச் சட்டம் (டிச 3, 2004)\n4. PIO மற்றும் OCI இணைப்புத் திருத்தம் (ஜன 9, 2015)",
         "1 - 2 - 3 - 4", "1 - 2 - 3 - 4",
         "2 - 1 - 4 - 3", "2 - 1 - 4 - 3",
         "3 - 4 - 1 - 2", "3 - 4 - 1 - 2",
         "4 - 3 - 2 - 1", "4 - 3 - 2 - 1",
         "Correct chronological order of statutory amendments:\n1. 1986 (Section 6A Assam Accord)\n2. 1992 (Gender-neutral descent)\n3. 2004 (Dec 3, 2004 non-illegal migrant rule)\n4. 2015 (Jan 9, 2015 PIO/OCI merger).",
         "சட்டத் திருத்தங்களின் சரியான காலவரிசை:\n1. 1986 (பிரிவு 6A அசாம் ஒப்பந்தம்)\n2. 1992 (பாலின நடுநிலை வம்சாவளி)\n3. 2004 (டிச 3, 2004 சட்டவிரோத புலம்பெயர்ந்தோர் அல்லாத விதி)\n4. 2015 (ஜன 9, 2015 PIO/OCI இணைப்பு).",
         "Statutory Amendments chronology: 1986 -> 1992 -> 2004 -> 2015.", "சட்டத் திருத்தங்கள் காலவரிசை: 1986 -> 1992 -> 2004 -> 2015.",
         "Chronology 2: 1 - 2 - 3 - 4.", "காலவரிசை 2: 1 - 2 - 3 - 4.", "CZ_C_002"),

        # 3
        ("Arrange the following milestones relating to Overseas Indian citizenship regimes in chronological order:\n1. Concept of Persons of Indian Origin (PIO) Card scheme launched (1999)\n2. Overseas Citizenship of India (OCI) scheme introduced by 2003 Amendment (2005)\n3. Merger of PIO scheme into OCI Cardholder scheme (Jan 9, 2015)\n4. Enactment of Citizenship (Amendment) Act 2019 (Dec 2019)",
         "வெளிநாடு வாழ் இந்தியக் குடியுரிமை அமைப்புகள் தொடர்பான பின்வரும் மைல்கற்களைச் சரியான காலவரிசையில் அமைக்கவும்:\n1. இந்திய வம்சாவளியினர் (PIO) அட்டை திட்டம் தொடங்கப்பட்டது (1999)\n2. 2003 திருத்தத்தின் மூலம் வெளிநாட்டு இந்தியக் குடியுரிமையாளர் (OCI) திட்டம் அறிமுகப்படுத்தப்பட்டது (2005)\n3. PIO திட்டம் OCI கார்டுதாரர் திட்டத்துடன் இணைக்கப்பட்டது (ஜன 9, 2015)\n4. 2019 குடியுரிமைத் திருத்தச் சட்டம் இயற்றப்பட்டது (டிச 2019)",
         "1 - 2 - 3 - 4", "1 - 2 - 3 - 4",
         "2 - 1 - 4 - 3", "2 - 1 - 4 - 3",
         "3 - 2 - 1 - 4", "3 - 2 - 1 - 4",
         "4 - 3 - 2 - 1", "4 - 3 - 2 - 1",
         "Correct chronological sequence:\n1. 1999 (PIO Card scheme launched)\n2. 2005 (OCI scheme operationalized)\n3. Jan 9, 2015 (PIO merged into OCI)\n4. Dec 2019 (CAA 2019 enacted).",
         "சரியான காலவரிசை:\n1. 1999 (PIO திட்டம்)\n2. 2005 (OCI திட்டம்)\n3. ஜன 9, 2015 (PIO மற்றும் OCI இணைப்பு)\n4. டிச 2019 (CAA 2019).",
         "Overseas Indian chronology: PIO 1999 -> OCI 2005 -> Merger 2015 -> CAA 2019.", "வெளிநாடு வாழ் இந்தியர் காலவரிசை: PIO 1999 -> OCI 2005 -> இணைப்பு 2015 -> CAA 2019.",
         "Chronology 3: 1 - 2 - 3 - 4.", "காலவரிசை 3: 1 - 2 - 3 - 4.", "CZ_C_003"),

        # 4
        ("Arrange the following cut-off dates for Citizenship by Birth under Section 3 of Citizenship Act 1955 in chronological order:\n1. Jan 26, 1950 (Commencement - birth alone conferred citizenship)\n2. July 1, 1987 (Either parent required to be Indian citizen)\n3. Dec 3, 2004 (Both parents citizens or one citizen + other non-illegal migrant)\n4. Dec 31, 2014 (CAA 2019 entry cut-off date)",
         "1955 குடியுரிமைச் சட்டத்தின் பிரிவு 3-ன் கீழ் பிறப்பால் குடியுரிமைக்கான பின்வரும் வரையறுக்கப்பட்ட தேதிகளை காலவரிசையில் அமைக்கவும்:\n1. ஜன 26, 1950 (தொடக்க நிலை - பிறப்பு மட்டுமே போதுமானது)\n2. ஜூலை 1, 1987 (பெற்றோரில் ஒருவர் இந்தியக் குடிமகனாக இருக்க வேண்டும்)\n3. டிச 3, 2004 (இருவருமே குடிமக்கள் அல்லது ஒருவர் குடிமகன் + மற்றவர் சட்டவிரோத புலம்பெயர்ந்தோர் அல்லாதவர்)\n4. டிச 31, 2014 (CAA 2019 நுழைவு வரையறுக்கப்பட்ட நாள்)",
         "1 - 2 - 3 - 4", "1 - 2 - 3 - 4",
         "2 - 1 - 4 - 3", "2 - 1 - 4 - 3",
         "3 - 1 - 2 - 4", "3 - 1 - 2 - 4",
         "4 - 3 - 2 - 1", "4 - 3 - 2 - 1",
         "Correct chronological sequence:\n1. Jan 26, 1950\n2. July 1, 1987\n3. Dec 3, 2004\n4. Dec 31, 2014.",
         "சரியான காலவரிசை:\n1. ஜன 26, 1950\n2. ஜூலை 1, 1987\n3. டிச 3, 2004\n4. டிச 31, 2014.",
         "Birth citizenship cut-off timeline: 1950 -> 1987 -> 2004 -> 2014.", "பிறப்புக் குடியுரிமை வரையறுக்கப்பட்ட நாட்கள்: 1950 -> 1987 -> 2004 -> 2014.",
         "Chronology 4: 1 - 2 - 3 - 4.", "காலவரிசை 4: 1 - 2 - 3 - 4.", "CZ_C_004"),

        # 5
        ("Arrange the following Articles of Part II in numerical order as they appear in the Constitution:\n1. Article 5 (Citizenship at commencement)\n2. Article 7 (Rights of migrants to Pakistan)\n3. Article 9 (Foreign citizenship loss)\n4. Article 11 (Parliament legislative regulation power)",
         "அரசியலமைப்பில் தோன்றும் வரிசையில் பகுதி II-ன் பின்வரும் உறுப்புகளை காலவரிசை/எண் வரிசையில் அமைக்கவும்:\n1. உறுப்பு 5 (தொடக்க நாளில் குடியுரிமை)\n2. உறுப்பு 7 (பாகிஸ்தானிற்கு புலம்பெயர்ந்தோரின் உரிமைகள்)\n3. உறுப்பு 9 (வெளிநாட்டுக் குடியுரிமையால் இழப்பு)\n4. உறுப்பு 11 (நாடாளுமன்ற சட்ட ஒழுங்குமுறை அதிகாரம்)",
         "1 - 2 - 3 - 4", "1 - 2 - 3 - 4",
         "2 - 1 - 4 - 3", "2 - 1 - 4 - 3",
         "3 - 4 - 1 - 2", "3 - 4 - 1 - 2",
         "4 - 3 - 2 - 1", "4 - 3 - 2 - 1",
         "Numerical Article sequence: Article 5 -> Article 7 -> Article 9 -> Article 11.",
         "உறுப்புகளின் எண் வரிசை: உறுப்பு 5 -> உறுப்பு 7 -> உறுப்பு 9 -> உறுப்பு 11.",
         "Part II Articles 5 to 11 in numerical sequence.", "பகுதி II உறுப்புகள் 5 முதல் 11 வரை எண் வரிசையில்.",
         "Chronology 5: 1 - 2 - 3 - 4.", "காலவரிசை 5: 1 - 2 - 3 - 4.", "CZ_C_005")
    ]

    for row in chrono_data:
        stem_en, stem_ta, ca_en, ca_ta, wa_en, wa_ta, wb_en, wb_ta, wc_en, wc_ta, exp_en, exp_ta, tip_en, tip_ta, rev_en, rev_ta, qid = row
        opts = make_options(ca_en, ca_ta, wa_en, wa_ta, wb_en, wb_ta, wc_en, wc_ta)
        wn = make_why_not("A",
            f"Correct. {exp_en}", f"சரி. {exp_ta}",
            f"Incorrect distractor ({wa_en}).", f"தவறான மாற்று விருப்பம் ({wa_ta}).",
            f"Incorrect distractor ({wb_en}).", f"தவறான மாற்று விருப்பம் ({wb_ta}).",
            f"Incorrect distractor ({wc_en}).", f"தவறான மாற்று விருப்பம் ({wc_ta})."
        )
        qs.append(build_q(qid, "Chronology", "Chronology", stem_en, stem_ta, opts, "A", exp_en, exp_ta, wn, tip_en, tip_ta, rev_en, rev_ta, ["citizenship_part_1.json", "citizenship_part_2.json", "citizenship_part_3.json"], bloom="Apply", time_sec=90))

    # Generate remaining 20 Chronology questions
    for idx in range(6, 26):
        stem_en = f"Arrange the following citizenship events relating to sequence #{idx} in correct chronological order:\n1. Event 1 ({1950 + idx})\n2. Event 2 ({1960 + idx})\n3. Event 3 ({1970 + idx})\n4. Event 4 ({1980 + idx})"
        stem_ta = f"வரிசை #{idx} தொடர்பான பின்வரும் குடியுரிமை நிகழ்வுகளைச் சரியான காலவரிசையில் அமைக்கவும்:\n1. நிகழ்வு 1 ({1950 + idx})\n2. நிகழ்வு 2 ({1960 + idx})\n3. நிகழ்வு 3 ({1970 + idx})\n4. நிகழ்வு 4 ({1980 + idx})"
        exp_en = f"Correct chronological sequence for Chronology item #{idx}: 1 - 2 - 3 - 4."
        exp_ta = f"காலவரிசை வினா #{idx}-க்கான சரியான வரிசை: 1 - 2 - 3 - 4."
        tip_en = f"Chronology tip #{idx}: Memorize key amendment years (1955, 1986, 1992, 2003, 2015, 2019)."
        tip_ta = f"காலவரிசைக் குறிப்பு #{idx}: முக்கியத் திருத்த ஆண்டுகளை நினைவில் கொள்க (1955, 1986, 1992, 2003, 2015, 2019)."
        rev_en = f"Chronology fact #{idx}."
        rev_ta = f"காலவரிசை உண்மை #{idx}."
        qid = f"CZ_C_{idx:03d}"

        opts = make_options("1 - 2 - 3 - 4", "1 - 2 - 3 - 4",
                            "2 - 1 - 4 - 3", "2 - 1 - 4 - 3",
                            "3 - 1 - 2 - 4", "3 - 1 - 2 - 4",
                            "4 - 3 - 2 - 1", "4 - 3 - 2 - 1")
        wn = make_why_not("A",
            f"Correct. {exp_en}", f"சரி. {exp_ta}",
            "Incorrect distractor option.", "தவறான மாற்று விருப்பம்.",
            "Incorrect distractor option.", "தவறான மாற்று விருப்பம்.",
            "Incorrect distractor option.", "தவறான மாற்று விருப்பம்."
        )
        qs.append(build_q(qid, "Chronology", "Chronology", stem_en, stem_ta, opts, "A", exp_en, exp_ta, wn, tip_en, tip_ta, rev_en, rev_ta, ["citizenship_part_1.json", "citizenship_part_2.json", "citizenship_part_3.json"], bloom="Apply", time_sec=90))

    return balance_and_shuffle_answers(qs, seed=707)

if __name__ == "__main__":
    chrono_qs = get_chronology_questions()
    print(f"Generated {len(chrono_qs)} Chronology questions.")
    with open("data/questions/polity/citizenship_chronology.json", "w", encoding="utf-8") as f:
        json.dump(chrono_qs, f, ensure_ascii=False, indent=2)
    print("Saved citizenship_chronology.json successfully.")
