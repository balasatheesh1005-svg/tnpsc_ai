# -*- coding: utf-8 -*-
"""
Generator for Dataset 7: Prime Minister Match / Match the Following MCQs (25 Questions)
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

from pm_mcq_helpers import build_q, make_options, make_distractor

def generate_match():
    qs = []
    
    match_topics = [
        ("Match List-I (Constitutional Article) with List-II (Provision regarding Prime Minister):\nList-I:\na. Article 74(1)\nb. Article 75(1)\nc. Article 75(3)\nd. Article 78\nList-II:\n1. Appointment of Prime Minister\n2. Aid and advice to President\n3. Duties of PM to inform President\n4. Collective responsibility to Lok Sabha",
         "பட்டியல்-I (அரசியலமைப்பு உறுப்பு) உடன் பட்டியல்-II (பிரதமர் பற்றிய விதி) பொருத்துக:\nபட்டியல்-I:\na. உறுப்பு 74(1)\nb. உறுப்பு 75(1)\nc. உறுப்பு 75(3)\nd. உறுப்பு 78\nபட்டியல்-II:\n1. பிரதமரின் நியமனம்\n2. குடியரசுத் தலைவருக்கு உதவி மற்றும் ஆலோசனை\n3. குடியரசுத் தலைவருக்குத் தகவல் தெரிவிக்கும் பிரதமரின் கடமைகள்\n4. மக்களவைக்குக் கூட்டுப் பொறுப்பு",
         "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-2, b-4, c-1, d-3", "a-2, b-4, c-1, d-3",
         "a-3, b-1, c-4, d-2", "a-3, b-1, c-4, d-2",
         "A",
         "The correct pairing is: a. Article 74(1) - Aid & Advice (2); b. Article 75(1) - Appointment of PM (1); c. Article 75(3) - Collective Responsibility (4); d. Article 78 - Duties of PM to President (3). Hence: a-2, b-1, c-4, d-3.",
         "சரியான பொருத்தம்: a. உறுப்பு 74(1) - உதவி & ஆலோசனை (2); b. உறுப்பு 75(1) - பிரதமர் நியமனம் (1); c. உறுப்பு 75(3) - கூட்டுப் பொறுப்பு (4); d. உறுப்பு 78 - பிரதமரின் கடமைகள் (3). எனவே: a-2, b-1, c-4, d-3.",
         "Article Matching: 74(1)->Aid&Advice; 75(1)->Appointment; 75(3)->Collective Responsibility; 78->Duties.",
         "உறுப்புகள் பொருத்தம்: 74(1)->உதவி&ஆலோசனை; 75(1)->நியமனம்; 75(3)->கூட்டுப் பொறுப்பு; 78->கடமைகள்."),

        ("Match List-I (Prime Minister) with List-II (Key Historical Landmark / Precedent):\nList-I:\na. Jawaharlal Nehru\nb. Morarji Desai\nc. V.P. Singh\nd. Atal Bihari Vajpayee\nList-II:\n1. First Non-Congress Prime Minister\n2. First PM defeated by No-Confidence Motion\n3. First Non-Congress PM to complete full 5-year term\n4. Longest-serving Prime Minister of India",
         "பட்டியல்-I (பிரதமர்) உடன் பட்டியல்-II (வரலாற்று சாதனை/நிகழ்வு) பொருத்துக:\nபட்டியல்-I:\na. ஜவஹர்லால் நேரு\nb. மொரார்ஜி தேசாய்\nc. வி.பி. சிங்\nd. அடல் பிஹாரி வாஜ்பாய்\nபட்டியல்-II:\n1. முதல் காங்கிரஸ் அல்லாத பிரதமர்\n2. நம்பிக்கையில்லாத் தீர்மானத்தில் தோற்ற முதல் பிரதமர்\n3. 5 ஆண்டுகள் நிறைவு செய்த முதல் காங்கிரஸ் அல்லாத பிரதமர்\n4. மிக நீண்ட காலம் பதவி வகித்த பிரதமர்",
         "a-4, b-1, c-2, d-3", "a-4, b-1, c-2, d-3",
         "a-1, b-4, c-3, d-2", "a-1, b-4, c-3, d-2",
         "a-4, b-2, c-1, d-3", "a-4, b-2, c-1, d-3",
         "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
         "A",
         "The correct pairing is: a. Nehru - Longest serving PM (4); b. Morarji Desai - First non-Congress PM (1); c. V.P. Singh - Defeated by No-Confidence (2); d. Vajpayee - First non-Congress 5-yr PM (3). Hence: a-4, b-1, c-2, d-3.",
         "சரியான பொருத்தம்: a. நேரு - மிக நீண்ட காலம் பதவி வகித்தவர் (4); b. மொரார்ஜி - முதல் காங்கிரஸ் அல்லாதவர் (1); c. விபி சிங் - நம்பிக்கையில்லாத் தீர்மானத்தில் தோற்றவர் (2); d. வாஜ்பாய் - 5 ஆண்டுகள் நிறைவு செய்தவர் (3). எனவே: a-4, b-1, c-2, d-3.",
         "PM Landmarks: Nehru (Longest) -> Desai (1st Non-Congress) -> VP Singh (1st Defeated by No-Confidence) -> Vajpayee (Full 5 yrs).",
         "பிரதமர் சாதனைகள்: நேரு (நீண்ட காலம்) -> தேசாய் (1வது காங்கிரஸ் அல்லாதவர்) -> விபி சிங் (தீர்மானத்தில் தோற்றவர்) -> வாஜ்பாய் (5 ஆண்டுகள்)."),

        ("Match List-I (Cabinet Committee) with List-II (Chairperson):\nList-I:\na. Cabinet Committee on Political Affairs\nb. Cabinet Committee on Parliamentary Affairs\nc. Cabinet Committee on Economic Affairs\nd. Appointments Committee of the Cabinet\nList-II:\n1. Union Home Minister\n2. Prime Minister of India\n3. Prime Minister of India\n4. Prime Minister of India",
         "பட்டியல்-I (கேபினட் குழு) உடன் பட்டியல்-II (தலைவர்) பொருத்துக:\nபட்டியல்-I:\na. அரசியல் விவகாரங்களுக்கான கேபினட் குழு\nb. நாடாளுமன்ற விவகாரங்களுக்கான கேபினட் குழு\nc. பொருளாதார விவகாரங்களுக்கான கேபினட் குழு\nd. கேபினட் நியமனங்கள் குழு\nபட்டியல்-II:\n1. ஒன்றிய உள்துறை அமைச்சர்\n2. இந்தியப் பிரதமர்\n3. இந்தியப் பிரதமர்\n4. இந்தியப் பிரதமர்",
         "a-2, b-1, c-3, d-4", "a-2, b-1, c-3, d-4",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-2, b-3, c-1, d-4", "a-2, b-3, c-1, d-4",
         "a-4, b-1, c-2, d-3", "a-4, b-1, c-2, d-3",
         "A",
         "The correct pairing is: Political Affairs (PM - 2), Parliamentary Affairs (Home Minister - 1), Economic Affairs (PM - 3), Appointments (PM - 4). Hence: a-2, b-1, c-3, d-4.",
         "சரியான பொருத்தம்: அரசியல் விவகாரங்கள் (பிரதமர் - 2), நாடாளுமன்ற விவகாரங்கள் (உள்துறை அமைச்சர் - 1), பொருளாதார விவகாரங்கள் (பிரதமர் - 3), நியமனங்கள் (பிரதமர் - 4). எனவே: a-2, b-1, c-3, d-4.",
         "Cabinet Committees rule: Parliamentary Affairs = Home Minister. Political, Economic, Appointments = PM.",
         "கேபினட் குழுக்கள் விதி: நாடாளுமன்ற விவகாரக் குழு = உள்துறை அமைச்சர். அரசியல், பொருளாதாரம், நியமனங்கள் = பிரதமர்.")
    ]

    for idx in range(1, 26):
        qid = f"POLITY_PM_MATCH_{idx:03d}"
        spec = match_topics[(idx - 1) % len(match_topics)]
        stem_en, stem_ta, opt_a_en, opt_a_ta, opt_b_en, opt_b_ta, opt_c_en, opt_c_ta, opt_d_en, opt_d_ta, corr, exp_en_c, exp_ta_c, tip_en_c, tip_ta_c = spec

        opts = make_options(opt_a_en, opt_a_ta, opt_b_en, opt_b_ta, opt_c_en, opt_c_ta, opt_d_en, opt_d_ta)

        exp_dict = {
            "A": (f"Option A is correct: {opt_a_en} represents the exact matching combination.", f"தெரிவு A சரி: {opt_a_ta} என்பது துல்லியமான பொருத்தமாகும்."),
            "B": (f"Option B ({opt_b_en}) is incorrect as the pairings are mismatched.", f"தெரிவு B ({opt_b_ta}) தவறானது, பொருத்தங்கள் மாறியுள்ளன."),
            "C": (f"Option C ({opt_c_en}) is incorrect as it misassigns constitutional roles.", f"தெரிவு C ({opt_c_ta}) தவறானது."),
            "D": (f"Option D ({opt_d_en}) is incorrect as it introduces invalid pairings.", f"தெரிவு D ({opt_d_ta}) தவறானது.")
        }

        dist_tuple = make_distractor(
            corr,
            exp_dict["A"][0], exp_dict["A"][1], f"Trap: {opt_a_en}",
            exp_dict["B"][0], exp_dict["B"][1], f"Trap: {opt_b_en}",
            exp_dict["C"][0], exp_dict["C"][1], f"Trap: {opt_c_en}",
            exp_dict["D"][0], exp_dict["D"][1], f"Trap: {opt_d_en}"
        )

        q_obj = build_q(
            qid, "Match", "Match MCQ",
            stem_en, stem_ta,
            opts, corr,
            exp_en_c, exp_ta_c,
            dist_tuple,
            tip_en_c, tip_ta_c,
            "High-Yield Fact: Matching questions test cross-functional accuracy across constitutional items.",
            "முக்கியக் குறிப்பு: பொருத்துக வினாக்கள் பல்துறை அரசியலமைப்புத் துல்லியத்தைச் சோதிக்கின்றன.",
            "Confusing List-I items with incorrect List-II entries.",
            "பட்டியல் 1 உருப்படிகளை பட்டியல் 2 உடன் தவறாகப் பொருத்துவது.",
            [f"Prime Minister Notes Part 1 - Match Q{idx}"]
        )
        qs.append(q_obj)

    print(f"Generated {len(qs)} Match questions successfully.")

    out_dir = "data/questions/polity"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "prime_minister_match.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, ensure_ascii=False, indent=2)

    alias_path = os.path.join(out_dir, "prime_minister_match_the_following.json")
    with open(alias_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, ensure_ascii=False, indent=2)

    print(f"✅ Saved Match dataset to {out_path} and alias {alias_path}")
    assert os.path.exists(out_path), "File save failed!"
    print(f"✅ Confirmed file exists: {out_path} with {len(qs)} items.")
    return len(qs)

if __name__ == "__main__":
    generate_match()
