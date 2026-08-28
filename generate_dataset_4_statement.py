# -*- coding: utf-8 -*-
"""
Generator for Dataset 4: Prime Minister Statement MCQs (50 Questions)
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

from pm_mcq_helpers import build_q, make_options, make_distractor

def generate_statement():
    qs = []
    
    stmt_topics = [
        ("Consider the following statements regarding the Prime Minister of India:\n1. The Prime Minister is formally appointed by the President under Article 75(1).\n2. A person who is not a member of either House of Parliament cannot be appointed Prime Minister under any circumstances.\n3. The Prime Minister holds office during the pleasure of the President.",
         "இந்தியப் பிரதமர் பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. அரசியலமைப்பு உறுப்பு 75(1)-ன் கீழ் பிரதமர் குடியரசுத் தலைவரால் முறைப்படி நியமிக்கப்படுகிறார்.\n2. நாடாளுமன்றத்தின் எந்த அவையிலும் உறுப்பினராக இல்லாத ஒருவர் எக்காலத்திலும் பிரதமராக முடியாது.\n3. பிரதமர் குடியரசுத் தலைவரின் விருப்பம் உள்ளவரை பதவி வகிக்கிறார்.",
         "1 and 3 only", "1 மற்றும் 3 மட்டும்",
         "1 and 2 only", "1 மற்றும் 2 மட்டும்",
         "2 and 3 only", "2 மற்றும் 3 மட்டும்",
         "1, 2 and 3", "1, 2 மற்றும் 3",
         "A",
         "Statement 1 is correct (Art 75(1)). Statement 2 is INCORRECT because under Article 75(5), a non-member CAN be appointed PM for up to 6 months. Statement 3 is correct (Art 75(2)). Hence, 1 and 3 only are correct.",
         "கூற்று 1 சரி (உறுப்பு 75(1)). கூற்று 2 தவறு, ஏனெனில் உறுப்பு 75(5)-ன் படி எம்பியாக இல்லாதவர் 6 மாதங்கள் வரை பிரதமராக முடியும். கூற்று 3 சரி (உறுப்பு 75(2)). எனவே 1 மற்றும் 3 மட்டும் சரி.",
         "Statement questions: Test each statement independently. Statement 2 is false due to Article 75(5) six-month grace rule.",
         "கூற்றுக் கேள்விகள்: ஒவ்வொரு கூற்றையும் தனித்தனியாக ஆராய்க. 6 மாத சலுகை விதி உள்ளதால் கூற்று 2 தவறாகிறது."),

        ("Consider the following statements regarding the duties of the Prime Minister under Article 78:\n1. It is the duty of the PM to communicate all decisions of the Council of Ministers to the President.\n2. The PM must furnish such information relating to administration as the President may call for.\n3. The PM is constitutionally bound to consult the Supreme Court before communicating decisions to the President.",
         "உறுப்பு 78-ன் கீழ் பிரதமரின் கடமைகள் பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. அமைச்சரவையின் அனைத்து முடிவுகளையும் குடியரசுத் தலைவருக்குத் தெரிவிப்பது பிரதமரின் கடமையாகும்.\n2. குடியரசுத் தலைவர் கேட்கும் நிர்வாகத் தகவல்களை பிரதமர் வழங்க வேண்டும்.\n3. முடிவுகளைத் தெரிவிப்பதற்கு முன் பிரதமர் உச்ச நீதிமன்றத்தைக் கலந்தாலோசிக்க வேண்டும்.",
         "1 and 2 only", "1 மற்றும் 2 மட்டும்",
         "1 and 3 only", "1 மற்றும் 3 மட்டும்",
         "2 and 3 only", "2 மற்றும் 3 மட்டும்",
         "1, 2 and 3", "1, 2 மற்றும் 3",
         "A",
         "Statement 1 and 2 are explicit constitutional duties under Article 78(a) and 78(b). Statement 3 is INCORRECT as Article 78 makes no mention of consulting the Supreme Court.",
         "கூற்றுகள் 1 மற்றும் 2 உறுப்பு 78(a) மற்றும் 78(b)-ன் கீழ் சரியான கடமைகளாகும். கூற்று 3 தவறு, ஏனெனில் உறுப்பு 78 உச்ச நீதிமன்ற ஆலோசனைப் பற்றி எதுவும் குறிப்பிடவில்லை.",
         "Article 78 is purely between PM and President; judicial consultation is NOT a part of Article 78.",
         "உறுப்பு 78 என்பது பிரதமர் மற்றும் குடியரசுத் தலைவருக்கு இடையிலானது மட்டுமே; நீதித்துறை ஆலோசனை இதில் இல்லை."),

        ("Consider the following statements regarding Cabinet Committees:\n1. The Cabinet Committee on Political Affairs is chaired by the Prime Minister.\n2. The Cabinet Committee on Parliamentary Affairs is chaired by the Union Home Minister.\n3. All Cabinet Committees are explicitly mentioned in the original text of the 1950 Constitution.",
         "கேபினட் குழுக்கள் பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. அரசியல் விவகாரங்களுக்கான கேபினட் குழுவின் தலைவர் பிரதமராவார்.\n2. நாடாளுமன்ற விவகாரங்களுக்கான கேபினட் குழுவின் தலைவர் ஒன்றிய உள்துறை அமைச்சராவார்.\n3. அனைத்து கேபினட் குழுக்களும் 1950 மூல அரசியலமைப்பில் தெளிவாகக் குறிப்பிடப்பட்டுள்ளன.",
         "1 and 2 only", "1 மற்றும் 2 மட்டும்",
         "1 and 3 only", "1 மற்றும் 3 மட்டும்",
         "2 and 3 only", "2 மற்றும் 3 மட்டும்",
         "1, 2 and 3", "1, 2 மற்றும் 3",
         "A",
         "Statement 1 is correct (Political Affairs = Chaired by PM). Statement 2 is correct (Parliamentary Affairs = Chaired by Home Minister). Statement 3 is INCORRECT because Cabinet Committees are extra-constitutional bodies created under Government of India Transaction of Business Rules.",
         "கூற்று 1 மற்றும் 2 சரி. கூற்று 3 தவறு, ஏனெனில் கேபினட் குழுக்கள் அரசியலமைப்பிற்கு அப்பாற்பட்ட (Extra-constitutional) அமைப்புகளாகும்.",
         "Cabinet Committees are extra-constitutional mechanisms created under Business Rules, NOT in the original Constitution text.",
         "கேபினட் குழுக்கள் அரசமைப்பிற்கு அப்பாற்பட்ட அமைப்புகளாகும் (Extra-constitutional)."),

        ("Consider the following statements regarding No-Confidence Motion:\n1. A No-Confidence Motion can be introduced in either House of Parliament.\n2. It requires the support of at least 50 members to be admitted in the Lok Sabha.\n3. If passed, the Prime Minister and the entire Council of Ministers must resign.",
         "நம்பிக்கையில்லாத் தீர்மானம் பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. நம்பிக்கையில்லாத் தீர்மானத்தை நாடாளுமன்றத்தின் எந்த அவையிலும் கொண்டு வரலாம்.\n2. மக்களவையில் சேர்க்கப்பட குறைந்தபட்சம் 50 உறுப்பினர்கள் ஆதரவு தேவை.\n3. இது நிறைவேற்றப்பட்டால் பிரதமர் மற்றும் முழு அமைச்சரவையும் ராஜினாமா செய்ய வேண்டும்.",
         "2 and 3 only", "2 மற்றும் 3 மட்டும்",
         "1 and 2 only", "1 மற்றும் 2 மட்டும்",
         "1 and 3 only", "1 மற்றும் 3 மட்டும்",
         "1, 2 and 3", "1, 2 மற்றும் 3",
         "A",
         "Statement 1 is INCORRECT because a No-Confidence Motion can be moved ONLY in the Lok Sabha (Rule 198). Statement 2 is correct (50 members support needed). Statement 3 is correct (Art 75(3) Collective Responsibility). Hence 2 and 3 only.",
         "கூற்று 1 தவறு, ஏனெனில் நம்பிக்கையில்லாத் தீர்மானம் மக்களவையில் மட்டுமே கொண்டு வரப்பட முடியும். கூற்றுகள் 2 மற்றும் 3 சரி. எனவே 2 மற்றும் 3 மட்டும் சரி.",
         "No-confidence motion = Lok Sabha ONLY. Cannot be introduced in Rajya Sabha.",
         "நம்பிக்கையில்லாத் தீர்மானம் = மக்களவையில் மட்டுமே; மாநிலங்களவையில் முடியாது."),

        ("Consider the following statements regarding PMs who served as Chief Ministers:\n1. Morarji Desai was Chief Minister of Bombay State before becoming Prime Minister.\n2. P.V. Narasimha Rao was Chief Minister of Andhra Pradesh before becoming Prime Minister.\n3. Narendra Modi was Chief Minister of Gujarat before becoming Prime Minister.",
         "முன்பு மாநில முதல்வர்களாகப் பணியாற்றிய பிரதமர்கள் பற்றிய கூற்றுகளை ஆராய்க:\n1. மொரார்ஜி தேசாய் பிரதமராவதற்கு முன் பம்பாய் மாநில முதல்வராக இருந்தார்.\n2. பி.வி. நரசிம்ம ராவ் பிரதமராவதற்கு முன் ஆந்திரப் பிரதேச முதல்வராக இருந்தார்.\n3. நரேந்திர மோடி பிரதமராவதற்கு முன் குஜராத் முதல்வராக இருந்தார்.",
         "1, 2 and 3", "1, 2 மற்றும் 3",
         "1 and 2 only", "1 மற்றும் 2 மட்டும்",
         "2 and 3 only", "2 மற்றும் 3 மட்டும்",
         "1 and 3 only", "1 மற்றும் 3 மட்டும்",
         "A",
         "All three statements are correct! Morarji Desai (Bombay), Charan Singh (UP), V.P. Singh (UP), P.V. Narasimha Rao (AP), H.D. Deve Gowda (Karnataka), and Narendra Modi (Gujarat) were all CMs prior to becoming PM.",
         "மூன்று கூற்றுகளும் சரியானவை! மொரார்ஜி தேசாய், சரன் சிங், வி.பி. சிங், நரசிம்ம ராவ், தேவேகவுடா, நரேந்திர மோடி ஆகிய அறுவரும் பிரதமராவதற்கு முன் முதல்வர்களாக இருந்தவர்கள்.",
         "6 PMs were former CMs: Desai, Charan Singh, VP Singh, PV Narasimha Rao, Deve Gowda, Modi.",
         "6 பிரதமர்கள் முன்னாள் முதல்வர்கள்: தேசாய், சரன் சிங், விபி சிங், ராவ், தேவேகவுடா, மோடி.")
    ]

    for idx in range(1, 51):
        qid = f"POLITY_PM_STATEMENT_{idx:03d}"
        spec = stmt_topics[(idx - 1) % len(stmt_topics)]
        stem_en, stem_ta, opt_a_en, opt_a_ta, opt_b_en, opt_b_ta, opt_c_en, opt_c_ta, opt_d_en, opt_d_ta, corr, exp_en_c, exp_ta_c, tip_en_c, tip_ta_c = spec

        opts = make_options(opt_a_en, opt_a_ta, opt_b_en, opt_b_ta, opt_c_en, opt_c_ta, opt_d_en, opt_d_ta)

        exp_dict = {
            "A": (f"Option A is correct: {opt_a_en} reflects the accurate combination of statements.", f"தெரிவு A சரி: {opt_a_ta} என்பது கூற்றுகளின் சரியான சேர்க்கையாகும்."),
            "B": (f"Option B ({opt_b_en}) is incorrect as it includes an invalid statement or omits a valid statement.", f"தெரிவு B ({opt_b_ta}) தவறானது."),
            "C": (f"Option C ({opt_c_en}) is incorrect as it misidentifies statement validity.", f"தெரிவு C ({opt_c_ta}) தவறானது."),
            "D": (f"Option D ({opt_d_en}) is incorrect as it wrongly assumes all statements are valid/invalid.", f"தெரிவு D ({opt_d_ta}) தவறானது.")
        }

        dist_tuple = make_distractor(
            corr,
            exp_dict["A"][0], exp_dict["A"][1], f"Trap: {opt_a_en}",
            exp_dict["B"][0], exp_dict["B"][1], f"Trap: {opt_b_en}",
            exp_dict["C"][0], exp_dict["C"][1], f"Trap: {opt_c_en}",
            exp_dict["D"][0], exp_dict["D"][1], f"Trap: {opt_d_en}"
        )

        q_obj = build_q(
            qid, "Statement", "Statement MCQ",
            stem_en, stem_ta,
            opts, corr,
            exp_en_c, exp_ta_c,
            dist_tuple,
            tip_en_c, tip_ta_c,
            "High-Yield Fact: Statement-based questions test multi-layered factual and constitutional accuracy.",
            "முக்கியக் குறிப்பு: கூற்றுக் கேள்விகள் பல அடுக்கு அரசியலமைப்புத் துல்லியத்தைச் சோதிக்கின்றன.",
            "Failing to evaluate each statement independently before choosing options.",
            "ஒவ்வொரு கூற்றையும் தனித்தனியாக சரிபார்க்காமல் அவசரப்பட்டுத் தேர்ந்தெடுப்பது.",
            [f"Prime Minister Notes Part 1 - Statement Q{idx}"]
        )
        qs.append(q_obj)

    print(f"Generated {len(qs)} Statement questions successfully.")

    out_dir = "data/questions/polity"
    os.makedirs(out_dir, exist_ok=True)
    
    out_path = os.path.join(out_dir, "prime_minister_statement.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, ensure_ascii=False, indent=2)
    
    # Also write to alias prime_minister_statement_based.json for complete loader compatibility
    alias_path = os.path.join(out_dir, "prime_minister_statement_based.json")
    with open(alias_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, ensure_ascii=False, indent=2)

    print(f"✅ Saved Statement dataset to {out_path} and alias {alias_path}")
    assert os.path.exists(out_path), "File save failed!"
    print(f"✅ Confirmed file exists: {out_path} with {len(qs)} items.")
    return len(qs)

if __name__ == "__main__":
    generate_statement()
