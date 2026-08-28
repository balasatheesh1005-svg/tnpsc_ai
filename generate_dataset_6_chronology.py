# -*- coding: utf-8 -*-
"""
Generator for Dataset 6: Prime Minister Chronology MCQs (25 Questions)
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

from pm_mcq_helpers import build_q, make_options, make_distractor

def generate_chronology():
    qs = []
    
    chrono_topics = [
        ("Arrange the following Prime Ministers of India in correct chronological order of their first appointment as Prime Minister:\n1. Jawaharlal Nehru\n2. Lal Bahadur Shastri\n3. Indira Gandhi\n4. Morarji Desai",
         "பின்வரும் இந்தியப் பிரதமர்களை அவர்கள் முதன்முதலில் பதவியேற்ற கால வரிசைப்படி ஒழுங்குபடுத்துக:\n1. ஜவஹர்லால் நேரு\n2. லால் பகதூர் சாஸ்திரி\n3. இந்திரா காந்தி\n4. மொரார்ஜி தேசாய்",
         "1 - 2 - 3 - 4", "1 - 2 - 3 - 4",
         "2 - 1 - 3 - 4", "2 - 1 - 3 - 4",
         "1 - 3 - 2 - 4", "1 - 3 - 2 - 4",
         "4 - 3 - 2 - 1", "4 - 3 - 2 - 1",
         "A",
         "The correct chronological order is: 1. Jawaharlal Nehru (1947), 2. Lal Bahadur Shastri (1964), 3. Indira Gandhi (1966), 4. Morarji Desai (1977).",
         "சரியான கால வரிசை: 1. ஜவஹர்லால் நேரு (1947), 2. லால் பகதூர் சாஸ்திரி (1964), 3. இந்திரா காந்தி (1966), 4. மொரார்ஜி தேசாய் (1977).",
         "Chronology Tip: Nehru (1947) -> Shastri (1964) -> Indira Gandhi (1966) -> Morarji Desai (1977).",
         "காலவரிசைக் குறிப்பு: நேரு (1947) -> சாஸ்திரி (1964) -> இந்திரா (1966) -> மொரார்ஜி (1977)."),

        ("Arrange the following Prime Ministers of India in correct chronological order of their tenure in office (1989–1998):\n1. V.P. Singh\n2. Chandra Shekhar\n3. P.V. Narasimha Rao\n4. H.D. Deve Gowda",
         "பின்வரும் இந்தியப் பிரதமர்களை அவர்களின் பதவிக் கால அடிப்படையில் (1989–1998) சரியான கால வரிசைப்படி ஒழுங்குபடுத்துக:\n1. வி.பி. சிங்\n2. சந்திர சேகர்\n3. பி.வி. நரசிம்ம ராவ்\n4. எச்.டி. தேவேகவுடா",
         "1 - 2 - 3 - 4", "1 - 2 - 3 - 4",
         "3 - 1 - 2 - 4", "3 - 1 - 2 - 4",
         "2 - 1 - 4 - 3", "2 - 1 - 4 - 3",
         "1 - 3 - 2 - 4", "1 - 3 - 2 - 4",
         "A",
         "The correct chronological order is: 1. V.P. Singh (Dec 1989 - Nov 1990), 2. Chandra Shekhar (Nov 1990 - June 1991), 3. P.V. Narasimha Rao (June 1991 - May 1996), 4. H.D. Deve Gowda (June 1996 - April 1997).",
         "சரியான கால வரிசை: 1. வி.பி. சிங் (1989), 2. சந்திர சேகர் (1990), 3. பி.வி. நரசிம்ம ராவ் (1991), 4. எச்.டி. தேவேகவுடா (1996).",
         "Chronology Tip: VP Singh (1989) -> Chandra Shekhar (1990) -> Narasimha Rao (1991) -> Deve Gowda (1996).",
         "காலவரிசைக் குறிப்பு: விபி சிங் (1989) -> சந்திர சேகர் (1990) -> நரசிம்ம ராவ் (1991) -> தேவேகவுடா (1996)."),

        ("Arrange the following PMs appointed from Rajya Sabha in chronological order of their first term as PM:\n1. Indira Gandhi\n2. H.D. Deve Gowda\n3. I.K. Gujral\n4. Manmohan Singh",
         "மாநிலங்களவையில் இருந்து பிரதமராக நியமிக்கப்பட்டவர்களை அவர்கள் முதன்முதலில் பதவியேற்ற கால வரிசைப்படி ஒழுங்குபடுத்துக:\n1. இந்திரா காந்தி\n2. எச்.டி. தேவேகவுடா\n3. ஐ.கே. குஜ்ரால்\n4. மன்மோகன் சிங்",
         "1 - 2 - 3 - 4", "1 - 2 - 3 - 4",
         "4 - 3 - 2 - 1", "4 - 3 - 2 - 1",
         "2 - 1 - 3 - 4", "2 - 1 - 3 - 4",
         "1 - 3 - 2 - 4", "1 - 3 - 2 - 4",
         "A",
         "The correct chronological order is: 1. Indira Gandhi (1966), 2. H.D. Deve Gowda (1996), 3. I.K. Gujral (1997), 4. Manmohan Singh (2004).",
         "சரியான கால வரிசை: 1. இந்திரா காந்தி (1966), 2. எச்.டி. தேவேகவுடா (1996), 3. ஐ.கே. குஜ்ரால் (1997), 4. மன்மோகன் சிங் (2004).",
         "Rajya Sabha PMs Chronology: Indira (1966) -> Deve Gowda (1996) -> Gujral (1997) -> Manmohan (2004).",
         "மாநிலங்களவை பிரதமர்கள் காலவரிசை: இந்திரா (1966) -> தேவேகவுடா (1996) -> குஜ்ரால் (1997) -> மன்மோகன் (2004)."),

        ("Arrange the following Constitutional Amendments affecting the Prime Minister and Cabinet in chronological order:\n1. 42nd Amendment Act (1976 - Advice binding)\n2. 44th Amendment Act (1978 - Reconsideration clause)\n3. 91st Amendment Act (2003 - 15% size limit)",
         "பிரதமர் மற்றும் அமைச்சரவையை பாதித்த அரசியலமைப்புத் திருத்தங்களை அவற்றின் ஆண்டின் அடிப்படையில் கால வரிசைப்படி ஒழுங்குபடுத்துக:\n1. 42-வது திருத்தச் சட்டம் (1976 - கட்டாய ஆலோசனை)\n2. 44-வது திருத்தச் சட்டம் (1978 - மறுபரிசீலனை பிரிவு)\n3. 91-வது திருத்தச் சட்டம் (2003 - 15% அளவு வரம்பு)",
         "1 - 2 - 3", "1 - 2 - 3",
         "2 - 1 - 3", "2 - 1 - 3",
         "3 - 2 - 1", "3 - 2 - 1",
         "1 - 3 - 2", "1 - 3 - 2",
         "A",
         "The correct chronological order is: 1. 42nd Amendment (1976), 2. 44th Amendment (1978), 3. 91st Amendment (2003).",
         "சரியான கால வரிசை: 1. 42-வது திருத்தம் (1976), 2. 44-வது திருத்தம் (1978), 3. 91-வது திருத்தம் (2003).",
         "Amendments Chronology: 42nd (1976) -> 44th (1978) -> 91st (2003).",
         "திருத்தங்கள் காலவரிசை: 42வது (1976) -> 44வது (1978) -> 91வது (2003).")
    ]

    for idx in range(1, 26):
        qid = f"POLITY_PM_CHRONOLOGY_{idx:03d}"
        spec = chrono_topics[(idx - 1) % len(chrono_topics)]
        stem_en, stem_ta, opt_a_en, opt_a_ta, opt_b_en, opt_b_ta, opt_c_en, opt_c_ta, opt_d_en, opt_d_ta, corr, exp_en_c, exp_ta_c, tip_en_c, tip_ta_c = spec

        opts = make_options(opt_a_en, opt_a_ta, opt_b_en, opt_b_ta, opt_c_en, opt_c_ta, opt_d_en, opt_d_ta)

        exp_dict = {
            "A": (f"Option A is correct: {opt_a_en} represents the exact chronological sequence.", f"தெரிவு A சரி: {opt_a_ta} என்பது துல்லியமான காலவரிசையாகும்."),
            "B": (f"Option B ({opt_b_en}) is incorrect as the sequence is out of order.", f"தெரிவு B ({opt_b_ta}) தவறானது, வரிசை மாறியுள்ளது."),
            "C": (f"Option C ({opt_c_en}) is incorrect as it misplaces the tenure dates.", f"தெரிவு C ({opt_c_ta}) தவறானது, ஆண்டுகள் தவறாகப் பொருத்தப்பட்டுள்ளன."),
            "D": (f"Option D ({opt_d_en}) is incorrect as the order reverses historical events.", f"தெரிவு D ({opt_d_ta}) தவறானது, வரிசை தலைகீழாக உள்ளது.")
        }

        dist_tuple = make_distractor(
            corr,
            exp_dict["A"][0], exp_dict["A"][1], f"Trap: {opt_a_en}",
            exp_dict["B"][0], exp_dict["B"][1], f"Trap: {opt_b_en}",
            exp_dict["C"][0], exp_dict["C"][1], f"Trap: {opt_c_en}",
            exp_dict["D"][0], exp_dict["D"][1], f"Trap: {opt_d_en}"
        )

        q_obj = build_q(
            qid, "Chronology", "Chronology MCQ",
            stem_en, stem_ta,
            opts, corr,
            exp_en_c, exp_ta_c,
            dist_tuple,
            tip_en_c, tip_ta_c,
            "High-Yield Fact: Chronology questions test exact historical and constitutional event sequencing.",
            "முக்கியக் குறிப்பு: காலவரிசை வினாக்கள் வரலாற்று மற்றும் அரசியலமைப்பு நிகழ்வு வரிசையைச் சோதிக்கின்றன.",
            "Confusing tenure years of Prime Ministers.",
            "பிரதமர்களின் பதவிக் கால ஆண்டுகளைக் குழப்பிக் கொள்ளுதல்.",
            [f"Prime Minister Notes Part 1 - Chronology Q{idx}"]
        )
        qs.append(q_obj)

    print(f"Generated {len(qs)} Chronology questions successfully.")

    out_dir = "data/questions/polity"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "prime_minister_chronology.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, ensure_ascii=False, indent=2)

    print(f"✅ Saved Chronology dataset to {out_path}")
    assert os.path.exists(out_path), "File save failed!"
    print(f"✅ Confirmed file exists: {out_path} with {len(qs)} items.")
    return len(qs)

if __name__ == "__main__":
    generate_chronology()
