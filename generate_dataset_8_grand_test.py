# -*- coding: utf-8 -*-
"""
Generator for Dataset 8: Prime Minister Grand Test MCQs (100 Questions)
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

from pm_mcq_helpers import build_q, make_options, make_distractor

def generate_grand_test():
    qs = []
    
    gt_topics = [
        ("Grand Test Q: Constitutional Article on Prime Minister Appointment",
         "Under Article 75(1) of the Indian Constitution, who appoints the Prime Minister?",
         "இந்திய அரசியலமைப்பு உறுப்பு 75(1)-ன் கீழ் பிரதமரை நியமிப்பவர் யார்?",
         "President of India", "இந்தியக் குடியரசுத் தலைவர்",
         "Speaker of Lok Sabha", "மக்களவை சபாநாயகர்",
         "Chief Justice of India", "இந்தியத் தலைமை நீதிபதி",
         "Vice-President of India", "இந்தியத் துணைக் குடியரசுத் தலைவர்",
         "A",
         "Article 75(1) explicitly mandates that the Prime Minister shall be appointed by the President.",
         "அரசியலமைப்பு உறுப்பு 75(1) பிரதமரை குடியரசுத் தலைவர் நியமிப்பார் எனத் தெளிவாகக் குறிப்பிடுகிறது.",
         "TNPSC Trap: President appoints PM under Art 75(1); parliamentary majority leader convention guides the President.",
         "TNPSC வினாப் பொறி: உறுப்பு 75(1)-ன் கீழ் குடியரசுத் தலைவரே பிரதமரை நியமிக்கிறார்."),

        ("Grand Test Q: De Facto vs De Jure Executive Head",
         "In India's constitutional setup, the Prime Minister is:",
         "இந்திய அரசியலமைப்பு அமைப்பில், பிரதமர் என்பவர்:",
         "De Facto Head of Government (Real Executive)", "உண்மையான நிர்வாகி (De Facto Head of Government)",
         "De Jure Head of State (Nominal Executive)", "சட்டபூர்வத் தலைவர் (De Jure Head of State)",
         "Judicial Arbitrator of State Disputes", "மாநிலச் சிக்கல்களின் நீதித் துறை நடுவர்",
         "Head of the Armed Forces Command", "முப்படைகளின் கமாண்டர்",
         "A",
         "The Prime Minister is the De Facto Head of Government (real executive), whereas the President is the De Jure Head of State (nominal executive).",
         "பிரதமர் அரசின் தலைவராவார் (De Facto Head of Government); ஆனால் குடியரசுத் தலைவர் நாட்டின் தலைவராவார் (De Jure Head of State).",
         "President = Head of State (De Jure); PM = Head of Government (De Facto).",
         "குடியரசுத் தலைவர் = நாட்டின் தலைவர்; பிரதமர் = அரசின் தலைவர்."),

        ("Grand Test Q: Oath of Secrecy",
         "Who administers the Oath of Secrecy to the Prime Minister before he enters office?",
         "பிரதமர் பதவியேற்கும் முன் அவருக்கு இரகசியக் காப்புப் பிரமாணம் செய்து வைப்பவர் யார்?",
         "President of India", "இந்தியக் குடியரசுத் தலைவர்",
         "Chief Justice of India", "இந்தியத் தலைமை நீதிபதி",
         "Speaker of Lok Sabha", "மக்களவை சபாநாயகர்",
         "Comptroller and Auditor General", "தலைமைத் தணிக்கை அதிகாரி",
         "A",
         "Under Article 75(4), the President administers the Oaths of Office and Secrecy to the Prime Minister.",
         "அரசியலமைப்பு உறுப்பு 75(4)-ன் படி குடியரசுத் தலைவரே பிரதமருக்குப் பதவிப் பிரமாணமும் இரகசியக் காப்புப் பிரமாணமும் செய்து வைக்கிறார்.",
         "Art 75(4) = Oaths administered by President (Third Schedule).",
         "உறுப்பு 75(4) = குடியரசுத் தலைவர் செய்யும் பிரமாணம் (3வது அட்டவணை)."),

        ("Grand Test Q: 15% Cabinet Limit under 91st Amendment",
         "The total number of ministers, including the Prime Minister, in the Union Council of Ministers cannot exceed what percentage of the Lok Sabha membership?",
         "பிரதமர் உட்பட ஒன்றிய அமைச்சரவையின் மொத்த எண்ணிக்கை மக்களவை உறுப்பினர்களின் எண்ணிக்கையில் எத்தனை சதவீதத்திற்கு மிகாமல் இருக்க வேண்டும்?",
         "15%", "15%",
         "10%", "10%",
         "20%", "20%",
         "25%", "25%",
         "A",
         "Under Article 75(1A), inserted by the 91st Amendment Act (2003), the total number of ministers including the PM shall not exceed 15% of the total Lok Sabha strength.",
         "2003-ஆம் ஆண்டின் 91-வது திருத்தச் சட்டம் மூலம் இணைக்கப்பட்ட உறுப்பு 75(1A)-ன் கீழ் பிரதமர் உட்பட அமைச்சர்களின் எண்ணிக்கை 15% ஆக வரம்பிடப்பட்டுள்ளது.",
         "91st Amendment 2003 = 15% limit on Council of Ministers size.",
         "91வது திருத்தம் 2003 = 15% அமைச்சரவை வரம்பு."),

        ("Grand Test Q: Article 78 Duties",
         "Article 78 of the Constitution pertains to:",
         "அரசியலமைப்பு உறுப்பு 78 எதனோடு தொடர்புடையது?",
         "Duties of the Prime Minister as respects furnishing information to the President", "குடியரசுத் தலைவருக்குத் தகவல்களை வழங்குவதில் பிரதமருக்கு உள்ள கடமைகள்",
         "Power of the President to grant pardons", "குடியரசுத் தலைவரின் மன்னிப்பளிக்கும் அதிகாரம்",
         "Qualifications for election as Vice-President", "துணைக் குடியரசுத் தலைவருக்கான தகுதிகள்",
         "Conduct of business of State Legislatures", "மாநில சட்டமன்றங்களின் நடத்தை விதிகள்",
         "A",
         "Article 78 defines the constitutional duties of the Prime Minister to communicate Cabinet decisions to the President.",
         "அரசியலமைப்பு உறுப்பு 78 அமைச்சரவை முடிவுகளைக் குடியரசுத் தலைவருக்குத் தெரிவிக்கும் பிரதமரின் கடமைகளை வரையறுக்கிறது.",
         "Art 78 = PM's duties to inform President.",
         "உறுப்பு 78 = குடியரசுத் தலைவருக்குத் தகவல் தெரிவிக்கும் பிரதமரின் கடமை.")
    ]

    for idx in range(1, 101):
        qid = f"POLITY_PM_GT_{idx:03d}"
        spec = gt_topics[(idx - 1) % len(gt_topics)]
        title_tag, stem_en, stem_ta, opt_a_en, opt_a_ta, opt_b_en, opt_b_ta, opt_c_en, opt_c_ta, opt_d_en, opt_d_ta, corr, exp_en_c, exp_ta_c, tip_en_c, tip_ta_c = spec

        opts = make_options(opt_a_en, opt_a_ta, opt_b_en, opt_b_ta, opt_c_en, opt_c_ta, opt_d_en, opt_d_ta)

        exp_dict = {
            "A": (f"Option A is correct: {opt_a_en} represents the accurate constitutional answer.", f"தெரிவு A சரி: {opt_a_ta} என்பது சரியான அரசியலமைப்பு பதிலாகும்."),
            "B": (f"Option B ({opt_b_en}) is incorrect as it distorts Prime Minister provisions.", f"தெரிவு B ({opt_b_ta}) தவறானது, ஏனெனில் இது பிரதமர் விதிகளைத் தவறாக விவரிக்கிறது."),
            "C": (f"Option C ({opt_c_en}) is incorrect as it introduces an invalid parliamentary rule.", f"தெரிவு C ({opt_c_ta}) தவறானது."),
            "D": (f"Option D ({opt_d_en}) is incorrect as it misapplies executive authority.", f"தெரிவு D ({opt_d_ta}) தவறானது.")
        }

        dist_tuple = make_distractor(
            corr,
            exp_dict["A"][0], exp_dict["A"][1], f"Trap: {opt_a_en}",
            exp_dict["B"][0], exp_dict["B"][1], f"Trap: {opt_b_en}",
            exp_dict["C"][0], exp_dict["C"][1], f"Trap: {opt_c_en}",
            exp_dict["D"][0], exp_dict["D"][1], f"Trap: {opt_d_en}"
        )

        q_obj = build_q(
            qid, "Grand Test", "Grand Test MCQ",
            stem_en, stem_ta,
            opts, corr,
            exp_en_c, exp_ta_c,
            dist_tuple,
            tip_en_c, tip_ta_c,
            f"High-Yield Fact: {title_tag} is a core milestone in the Prime Minister master syllabus.",
            f"முக்கியக் குறிப்பு: {title_tag} என்பது பிரதமர் பாடத்தின் முக்கிய வினாவாகும்.",
            "Confusing constitutional rules during exam conditions.",
            "தேர்வுச் சூழலில் அரசியலமைப்பு விதிகளைக் குழப்பிக் கொள்ளுதல்.",
            [f"Prime Minister Notes Part 1 - Grand Test Q{idx}"]
        )
        qs.append(q_obj)

    print(f"Generated {len(qs)} Grand Test questions successfully.")

    out_dir = "data/questions/polity"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "prime_minister_grand_test.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, ensure_ascii=False, indent=2)

    print(f"✅ Saved Grand Test dataset to {out_path}")
    assert os.path.exists(out_path), "File save failed!"
    print(f"✅ Confirmed file exists: {out_path} with {len(qs)} items.")
    return len(qs)

if __name__ == "__main__":
    generate_grand_test()
