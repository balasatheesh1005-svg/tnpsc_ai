# -*- coding: utf-8 -*-
"""
Generator for Dataset 5: Prime Minister Reasoning / Assertion-Reason MCQs (25 Questions)
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

from pm_mcq_helpers import build_q, make_options, make_distractor

def generate_reasoning():
    qs = []
    
    reasoning_topics = [
        ("Assertion (A): The Prime Minister is the real executive head (De Facto Head) of the Indian Union.\nReason (R): Under Article 74(1), the President acts on the aid and advice of the Council of Ministers headed by the Prime Minister.",
         "கூற்று (A): இந்திய ஒன்றியத்தின் உண்மையான நிர்வாகத் தலைவர் (De Facto Head) பிரதமராவார்.\nகாரணம் (R): உறுப்பு 74(1)-ன் படி, பிரதமரைத் தலைவராகக் கொண்ட அமைச்சரவையின் உதவி மற்றும் ஆலோசனையின் படியே குடியரசுத் தலைவர் செயல்படுகிறார்.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி; மேலும் (R) என்பது (A)-விற்கு சரியான விளக்கமாகும்",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி; ஆனால் (R) என்பது (A)-விற்கு சரியான விளக்கம் அல்ல",
         "(A) is true but (R) is false", "கூற்று (A) சரி; ஆனால் காரணம் (R) தவறு",
         "(A) is false but (R) is true", "கூற்று (A) தவறு; ஆனால் காரணம் (R) சரி",
         "A",
         "Assertion (A) is true: PM is the De Facto Head of Government. Reason (R) is true and correctly explains why PM is real executive: because the President is bound by the aid and advice of the Council of Ministers headed by the PM (Art 74(1)).",
         "கூற்று (A) சரி: பிரதமர் உண்மையான நிர்வாகியாவார். காரணம் (R) சரி: குடியரசுத் தலைவர் பிரதமரின் அமைச்சரவை ஆலோசனைக்கேற்ப செயல்பட வேண்டும் என்று உறுப்பு 74(1) கூறுவதே இதற்குச் சரியான விளக்கமாகும்.",
         "Reasoning questions test causality: Check if Reason (R) logically causes Assertion (A).",
         "காரண வினாக்கள்: காரணம் (R) என்பது கூற்று (A)-விற்கு நேரடிக் காரணமா என்பதைச் சரிபார்க்கவும்."),

        ("Assertion (A): The resignation of the Prime Minister automatically dissolves the Council of Ministers.\nReason (R): The Prime Minister is the keystone of the cabinet arch and holds the central leadership of the Council of Ministers.",
         "கூற்று (A): பிரதமரின் ராஜினாமா அமைச்சரவையைத் தானாகவே கலைத்துவிடும்.\nகாரணம் (R): பிரதமர் அமைச்சரவை வளைவின் மையத் தூணாக (Keystone of Cabinet arch) விளங்குவதுடன் அதன் மையத் தலைவராகவும் உள்ளார்.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி; மேலும் (R) என்பது (A)-விற்கு சரியான விளக்கமாகும்",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி; ஆனால் (R) என்பது (A)-விற்கு சரியான விளக்கம் அல்ல",
         "(A) is true but (R) is false", "கூற்று (A) சரி; ஆனால் காரணம் (R) தவறு",
         "(A) is false but (R) is true", "கூற்று (A) தவறு; ஆனால் காரணம் (R) சரி",
         "A",
         "Assertion (A) is true. Reason (R) is true and gives the exact constitutional logic why the Council collapses: because the PM is the apex center around which ministers are appointed and function.",
         "கூற்று (A) சரி. காரணம் (R) சரி: பிரதமர் அமைச்சரவையின் மையத் தூணாக இருப்பதாலேயே அவர் விலகும்போது அமைச்சரவை முழுவதுமாகக் கலைகிறது.",
         "Keystone principle: PM's resignation = Council of Ministers collapses. Individual minister resignation = simple vacancy.",
         "மையத் தூண் கோட்பாடு: பிரதமர் ராஜினாமா = அமைச்சரவை கலைப்பு. அமைச்சர் ராஜினாமா = காலியிடம் மட்டுமே."),

        ("Assertion (A): A person who is not a member of either House of Parliament can be appointed as Prime Minister.\nReason (R): Under Article 75(5), such a person gets a grace period of 6 months to secure membership in either House of Parliament.",
         "கூற்று (A): நாடாளுமன்றத்தின் எந்த அவையிலும் உறுப்பினராக இல்லாத ஒருவரைப் பிரதமராக நியமிக்க முடியும்.\nகாரணம் (R): உறுப்பு 75(5)-ன் படி, அத்தகைய நபர் நாடாளுமன்றத்தின் ஏதேனும் ஒரு அவையில் உறுப்பினராக 6 மாத சலுகைக் காலம் வழங்கப்படுகிறது.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி; மேலும் (R) என்பது (A)-விற்கு சரியான விளக்கமாகும்",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி; ஆனால் (R) என்பது (A)-விற்கு சரியான விளக்கம் அல்ல",
         "(A) is true but (R) is false", "கூற்று (A) சரி; ஆனால் காரணம் (R) தவறு",
         "(A) is false but (R) is true", "கூற்று (A) தவறு; ஆனால் காரணம் (R) சரி",
         "A",
         "Assertion (A) is true. Reason (R) is true and directly provides the constitutional provision (Art 75(5)) that enables a non-member to be appointed PM for up to 6 months.",
         "கூற்று (A) சரி. காரணம் (R) சரி: உறுப்பு 75(5)-ன் கீழ் உள்ள 6 மாத அவகாச விதியே எம்பியாக இல்லாதவர் பிரதமராக நியமிக்கப்படுவதை அரசியலமைப்பு ரீதியாகச் சாத்தியமாக்குகிறது.",
         "Art 75(5) six-month grace period applies equally to PM and Ministers.",
         "உறுப்பு 75(5) சலுகைக் காலம் பிரதமர் மற்றும் அமைச்சர்கள் அனைவருக்கும் பொருந்தும்."),

        ("Assertion (A): The Council of Ministers is collectively responsible strictly to the Lok Sabha and not to the Rajya Sabha.\nReason (R): The Lok Sabha consists of directly elected representatives of the people who hold the power to pass a No-Confidence Motion.",
         "கூற்று (A): அமைச்சரவை மாநிலங்களவைக்கு அல்லாமல் மக்களவைக்கே கூட்டாகப் பொறுப்புடையது.\nகாரணம் (R): மக்களவை நேரடித் பிரதிநிதிகளைக் கொண்டதுடன் நம்பிக்கையில்லாத் தீர்மானத்தை நிறைவேற்றும் அதிகாரத்தையும் கொண்டுள்ளது.",
         "Both (A) and (R) are true and (R) is the correct explanation of (A)", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி; மேலும் (R) என்பது (A)-விற்கு சரியான விளக்கமாகும்",
         "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி; ஆனால் (R) என்பது (A)-விற்கு சரியான விளக்கம் அல்ல",
         "(A) is true but (R) is false", "கூற்று (A) சரி; ஆனால் காரணம் (R) தவறு",
         "(A) is false but (R) is true", "கூற்று (A) தவறு; ஆனால் காரணம் (R) சரி",
         "A",
         "Assertion (A) is true (Art 75(3)). Reason (R) is true and explains the democratic logic: since Lok Sabha represents popular mandate, only Lok Sabha can pass a No-Confidence Motion.",
         "கூற்று (A) சரி (உறுப்பு 75(3)). காரணம் (R) சரி: மக்களவை மக்களால் நேரடியாகத் தேர்ந்தெடுக்கப்பட்டு நம்பிக்கையில்லாத் தீர்மானத்தைக் கொண்டுவரும் அதிகாரம் பெற்றதே இதற்குச் சரியான விளக்கமாகும்.",
         "Collective responsibility = Lok Sabha (Art 75(3)). Rajya Sabha cannot pass No-Confidence Motion.",
         "கூட்டுப் பொறுப்பு = மக்களவை மட்டுமே; மாநிலங்களவையில் நம்பிக்கையில்லாத் தீர்மானம் கொண்டுவர முடியாது.")
    ]

    for idx in range(1, 26):
        qid = f"POLITY_PM_REASONING_{idx:03d}"
        spec = reasoning_topics[(idx - 1) % len(reasoning_topics)]
        stem_en, stem_ta, opt_a_en, opt_a_ta, opt_b_en, opt_b_ta, opt_c_en, opt_c_ta, opt_d_en, opt_d_ta, corr, exp_en_c, exp_ta_c, tip_en_c, tip_ta_c = spec

        opts = make_options(opt_a_en, opt_a_ta, opt_b_en, opt_b_ta, opt_c_en, opt_c_ta, opt_d_en, opt_d_ta)

        exp_dict = {
            "A": (f"Option A is correct: Both Assertion and Reason are true and Reason accurately explains Assertion.", f"தெரிவு A சரி: கூற்று மற்றும் காரணம் இரண்டும் சரி, மேலும் காரணம் சரியான விளக்கமாகும்."),
            "B": (f"Option B ({opt_b_en}) is incorrect as Reason IS the direct explanation of Assertion.", f"தெரிவு B ({opt_b_ta}) தவறானது, ஏனெனில் காரணம் நேரடி விளக்கமாகும்."),
            "C": (f"Option C ({opt_c_en}) is incorrect as Reason is factually true.", f"தெரிவு C ({opt_c_ta}) தவறானது, ஏனெனில் காரணம் உண்மையாகும்."),
            "D": (f"Option D ({opt_d_en}) is incorrect as Assertion is factually true.", f"தெரிவு D ({opt_d_ta}) தவறானது, ஏனெனில் கூற்று உண்மையாகும்.")
        }

        dist_tuple = make_distractor(
            corr,
            exp_dict["A"][0], exp_dict["A"][1], f"Trap: {opt_a_en}",
            exp_dict["B"][0], exp_dict["B"][1], f"Trap: {opt_b_en}",
            exp_dict["C"][0], exp_dict["C"][1], f"Trap: {opt_c_en}",
            exp_dict["D"][0], exp_dict["D"][1], f"Trap: {opt_d_en}"
        )

        q_obj = build_q(
            qid, "Reasoning", "Reasoning MCQ",
            stem_en, stem_ta,
            opts, corr,
            exp_en_c, exp_ta_c,
            dist_tuple,
            tip_en_c, tip_ta_c,
            "High-Yield Fact: Assertion-Reason questions test constitutional cause-and-effect logic.",
            "முக்கியக் குறிப்பு: கூற்று-காரண வினாக்கள் அரசியலமைப்பின் காரண-காரியத் தொடர்பைச் சோதிக்கின்றன.",
            "Failing to check if Reason directly explains Assertion.",
            "காரணம் கூற்றை நேரடியாக விளக்குகிறதா என சோதிக்கத் தவறுவது.",
            [f"Prime Minister Notes Part 1 - Reasoning Q{idx}"]
        )
        qs.append(q_obj)

    print(f"Generated {len(qs)} Reasoning questions successfully.")

    out_dir = "data/questions/polity"
    os.makedirs(out_dir, exist_ok=True)
    
    out_path = os.path.join(out_dir, "prime_minister_reasoning.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, ensure_ascii=False, indent=2)
    
    alias_path = os.path.join(out_dir, "prime_minister_assertion_reason.json")
    with open(alias_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, ensure_ascii=False, indent=2)

    print(f"✅ Saved Reasoning dataset to {out_path} and alias {alias_path}")
    assert os.path.exists(out_path), "File save failed!"
    print(f"✅ Confirmed file exists: {out_path} with {len(qs)} items.")
    return len(qs)

if __name__ == "__main__":
    generate_reasoning()
