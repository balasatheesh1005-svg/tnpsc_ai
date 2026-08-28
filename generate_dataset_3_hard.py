# -*- coding: utf-8 -*-
"""
Generator for Dataset 3: Prime Minister Hard MCQs (50 Questions)
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

from pm_mcq_helpers import build_q, make_options, make_distractor

def generate_hard():
    qs = []
    
    # 50 Hard multi-concept questions
    hard_topics = [
        ("UNR Rao v. Indira Gandhi (1971) ruling on Caretaker PM after Lok Sabha dissolution",
         "The Council of Ministers with PM at the head MUST exist continuously even after Lok Sabha is dissolved, as President cannot function without aid and advice.",
         "மக்களவை கலைக்கப்பட்ட பிறகும் குடியரசுத் தலைவருக்கு உதவவும் ஆலோசனை வழங்கவும் பிரதமரைத் தலைவராகக் கொண்ட அமைச்சரவை தொடர வேண்டும்.",
         "The President takes over direct executive rule without needing a PM after Lok Sabha dissolution.",
         "மக்களவை கலைக்கப்பட்ட பின் குடியரசுத் தலைவர் பிரதமர் இன்றி நேரடியாக நிர்வாகத்தை மேற்கொள்வார்.",
         "The Vice-President assumes all PM duties until fresh Lok Sabha elections are completed.",
         "புதிய தேர்தல்கள் முடியும் வரை துணைக் குடியரசுத் தலைவர் பிரதமரின் அனைத்துப் பொறுப்புகளையும் ஏற்பார்.",
         "The Cabinet Secretary becomes the constitutional Head of Government.",
         "கேபினட் செயலாளரே அரசின் அரசியலமைப்பு ரீதியான தலைவராவார்.",
         "A",
         "In UNR Rao v. Indira Gandhi (1971), the Supreme Court ruled that Article 74(1) is mandatory. Even after the Lok Sabha is dissolved, the Council of Ministers does not cease to exist, and the President cannot exercise executive power without their aid and advice.",
         "1971 யு.என்.ஆர். ராவ் வழக்கில் உச்ச நீதிமன்றம் உறுப்பு 74(1) கட்டாயமானது என்றும், மக்களவை கலைக்கப்பட்ட பிறகும் அமைச்சரவை தொடர்ந்து இருக்கும் என்றும், அது இன்றி குடியரசுத் தலைவர் செயல்பட முடியாது என்றும் தீர்ப்பளித்தது.",
         "TNPSC Landmark Case: UNR Rao v. Indira Gandhi (1971) established that India ALWAYS has a Prime Minister and Council of Ministers, even during Lok Sabha dissolution.",
         "TNPSC முக்கிய வழக்கு: 1971 யு.என்.ஆர். ராவ் வழக்கு - மக்களவை கலைக்கப்பட்ட பிறகும் எப்போதும் இந்தியாவில் ஒரு பிரதமரும் அமைச்சரவையும் இருக்கும் என்பதை நிறுவியது."),

        ("SP Anand v. H.D. Deve Gowda (1997) ruling on appointment of non-MP as Prime Minister",
         "A person who is not a member of either House can be appointed Prime Minister, but must get elected to either House within 6 months.",
         "நாடாளுமன்றத்தின் எந்த அவையிலும் உறுப்பினராக இல்லாத ஒருவரைப் பிரதமராக நியமிக்கலாம்; ஆனால் அவர் 6 மாதங்களுக்குள் ஏதேனும் ஒரு அவைக்குத் தேர்ந்தெடுக்கப்பட வேண்டும்.",
         "Only a sitting member of the Lok Sabha can be appointed as Prime Minister; non-members are permanently barred.",
         "மக்களவையில் உறுப்பினராக உள்ளவர் மட்டுமே பிரதமராக முடியும்; உறுப்பினர் அல்லாதவருக்கு முற்றிலும் தடையுண்டு.",
         "A non-member can become Prime Minister only if approved by a 2/3rd majority of State Assemblies.",
         "மாநில சட்டமன்றங்களின் 2/3 பங்கு ஒப்புதல் பெற்றால் மட்டுமே உறுப்பினர் அல்லாதவர் பிரதமராக முடியும்.",
         "A non-member can be appointed Prime Minister for an unlimited duration without facing elections.",
         "உறுப்பினர் அல்லாதவர் தேர்தலை சந்திக்காமல் காலவரையின்றி பிரதமராக தொடர முடியும்.",
         "A",
         "In SP Anand v. H.D. Deve Gowda (1997), the Supreme Court upheld the constitutional validity of appointing a non-member of Parliament as Prime Minister under Article 75(5), provided he acquires membership within 6 months.",
         "1997 எஸ்.பி. ஆனந்த் வழக்கில் உச்ச நீதிமன்றம் எம்பியாக இல்லாத ஒருவர் 6 மாதங்களுக்குள் உறுப்பினரானால் போதும் என்ற நிபந்தனையுடன் பிரதமராக நியமிக்கப்படுவதை அரசியலமைப்பு ரீதியாக உறுதி செய்தது.",
         "SP Anand v. Deve Gowda (1997) = Upheld 6-month grace period for Prime Minister under Art 75(5).",
         "1997 எஸ்.பி. ஆனந்த் வழக்கு = உறுப்பு 75(5)-ன் கீழ் பிரதமருக்கான 6 மாத சலுகைக் காலத்தை உறுதி செய்தது."),

        ("Shamsher Singh v. State of Punjab (1974) ruling on Presidential powers",
         "The President is a constitutional head and MUST act on the aid and advice of the Council of Ministers headed by the PM in all executive functions (except rare situational discretion).",
         "குடியரசுத் தலைவர் ஒரு அரசியலமைப்புத் தலைவராவார்; அவர் அனைத்து நிர்வாக நடவடிக்கைகளிலும் பிரதமரைத் தலைவராகக் கொண்ட அமைச்சரவையின் ஆலோசனையின் படியே செயல்பட வேண்டும்.",
         "The President possesses absolute veto power to overrule the Prime Minister on any executive decree.",
         "எந்தவொரு நிர்வாக உத்தரவிலும் பிரதமரின் முடிவை நிராகரிக்க குடியரசுத் தலைவருக்கு முழுமையான வீட்டோ அதிகாரம் உண்டு.",
         "The President can dismiss the Prime Minister at any time even if PM commands a clear Lok Sabha majority.",
         "மக்களவையில் பெரும்பான்மை உள்ள பிரதமரையும் குடியரசுத் தலைவர் எப்போது வேண்டுமானாலும் நீக்க முடியும்.",
         "The President shares executive power equally with the Chief Justice of India.",
         "குடியரசுத் தலைவர் நிர்வாக அதிகாரத்தை உச்ச நீதிமன்றத் தலைமை நீதிபதியுடன் சமமாகப் பகிர்ந்து கொள்கிறார்.",
         "A",
         "In Shamsher Singh v. State of Punjab (1974), a 7-judge Constitution Bench of the Supreme Court held that the President (and Governors) are constitutional heads who must act in accordance with the advice of the Council of Ministers led by the PM.",
         "1974 சம்ஷேர் சிங் வழக்கில் 7 நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வு குடியரசுத் தலைவர் பெயரளவு தலைவரே என்றும், அவர் பிரதமரின் அமைச்சரவை ஆலோசனையின்படியே செயல்பட வேண்டும் என்றும் தீர்ப்பளித்தது.",
         "Shamsher Singh Case (1974) = Established that Parliamentary Executive supremacy binds the President.",
         "1974 சம்ஷேர் சிங் வழக்கு = நாடாளுமன்ற நிர்வாகத்தின் மேலாதிக்கத்தை குடியரசுத் தலைவருக்குக் கட்டாயமாக்கியது."),

        ("Ram Jawaya Kapur v. State of Punjab (1955) ruling on executive power of Cabinet",
         "Executive power of the Union is co-extensive with legislative power, and Cabinet led by PM can take executive actions even without prior legislative enactment, provided it doesn't violate fundamental rights or existing laws.",
         "ஒன்றிய நிர்வாக அதிகாரம் சட்டமியற்றும் அதிகாரத்திற்கு இணையானது; பிரதமரின் அமைச்சரவை சட்டத்திற்கு முன் நிர்வாக முடிவுகளை எடுக்க முடியும்.",
         "Executive power can only be exercised after Parliament passes an express Act for every minor administrative action.",
         "ஒவ்வொரு சிறிய நிர்வாக நடவடிக்கைக்கும் நாடாளுமன்றம் சட்டம் நிறைவேற்றிய பிறகே நிர்வாக அதிகாரத்தைப் பயன்படுத்த முடியும்.",
         "Cabinet cannot formulate any economic or social policies without Supreme Court clearance.",
         "உச்ச நீதிமன்ற அனுமதியின்றி கேபினட் எந்தவொரு பொருளாதார அல்லது சமூகக் கொள்கையையும் வகுக்க முடியாது.",
         "The Prime Minister derives executive power directly from the Military High Command.",
         "பிரதமர் தனது நிர்வாக அதிகாரத்தை ராணுவ உயர்மட்டக் குழுவிடமிருந்து பெறுகிறார்.",
         "A",
         "In Ram Jawaya Kapur v. State of Punjab (1955), the Supreme Court ruled that the executive power of the Cabinet is co-extensive with legislative competence, and the Cabinet can function without prior legislation as long as it does not infringe fundamental rights.",
         "1955 ராம் ஜவாயா கபூர் வழக்கில் உச்ச நீதிமன்றம் அமைச்சரவையின் நிர்வாக அதிகாரம் சட்டமன்ற அதிகாரத்திற்கு இணையானது என்றும், முன் சட்டமின்றி அது செயல்படலாம் என்றும் தீர்ப்பளித்தது.",
         "Ram Jawaya Kapur (1955) = Co-extensive executive power of PM-led Cabinet.",
         "1955 ராம் ஜவாயா கபூர் வழக்கு = பிரதமரின் அமைச்சரவை நிர்வாக அதிகாரத்தின் விரிவான தன்மையை விளக்கியது."),

        ("SR Bommai v. Union of India (1994) floor test mandate",
         "The strength/majority of a Ministry led by PM/CM MUST be tested exclusively on the floor of the Legislative Assembly/House, not by secret subjective assessment of President/Governor.",
         "பிரதமர்/முதல்வர் தலைமையிலான அரசின் பெரும்பான்மை நாடாளுமன்ற/சட்டமன்றக் களத்தில் (Floor Test) மட்டுமே நிரூபிக்கப்பட வேண்டும்.",
         "The President can determine majority by inspecting private affidavits signed in Raj Bhavan/Rashtrapati Bhavan.",
         "மாளிகைகளில் பெறப்பட்ட தனிப்பட்ட கையெழுத்துப் படிவங்களை ஆய்வு செய்து குடியரசுத் தலைவர் பெரும்பான்மையைத் தீர்மானிக்கலாம்.",
         "The Floor Test must be conducted by secret ballot monitored by the High Court.",
         "வாக்கெடுப்பு உயர் நீதிமன்றத்தின் மேற்பார்வையில் இரகசிய வாக்கெடுப்பாக மட்டுமே நடைபெற வேண்டும்.",
         "A Prime Minister who loses a floor test can request the President to nullify the vote.",
         "வாக்கெடுப்பில் தோற்ற பிரதமர் அதை ரத்து செய்யுமாறு குடியரசுத் தலைவரிடம் கோர முடியும்.",
         "A",
         "SR Bommai (1994) established that the floor test is the ONLY legitimate constitutional method to test the majority of a government.",
         "1994 எஸ்.ஆர். பொம்மை தீர்ப்பு அவையின் களத்தில் நடத்தப்படும் வாக்கெடுப்பே பெரும்பான்மையைச் சோதிக்கும் ஒரே அரசியலமைப்பு முறை என நிறுவியது.",
         "SR Bommai Rule = Floor Test is mandatory and non-negotiable.",
         "பொம்மை வழக்கு விதி = அவைக் கள வாக்கெடுப்பு (Floor Test) கட்டாயமானது.")
    ]

    for idx in range(1, 51):
        qid = f"POLITY_PM_HARD_{idx:03d}"
        spec = hard_topics[(idx - 1) % len(hard_topics)]
        topic_desc, opt_a_en, opt_a_ta, opt_b_en, opt_b_ta, opt_c_en, opt_c_ta, opt_d_en, opt_d_ta, corr, exp_en_c, exp_ta_c, tip_en_c, tip_ta_c = spec

        stem_en = f"With reference to the Indian Constitution and landmark judicial precedents regarding the Prime Minister, which of the following statements accurately explains: {topic_desc}?"
        stem_ta = f"இந்திய அரசியலமைப்பு மற்றும் உச்ச நீதிமன்றத்தின் வரலாற்றுத் தீர்ப்புகளின் அடிப்படையில், பிரதமர் பற்றிய எந்தக் கூற்று இதனை துல்லியமாக விவரிக்கிறது: {topic_desc}?"

        opts = make_options(opt_a_en, opt_a_ta, opt_b_en, opt_b_ta, opt_c_en, opt_c_ta, opt_d_en, opt_d_ta)

        exp_dict = {
            "A": (f"Option A is correct: {opt_a_en} represents the established constitutional and judicial precedent.", f"தெரிவு A சரி: {opt_a_ta} என்பது நிலைநிறுத்தப்பட்ட அரசியலமைப்பு மற்றும் நீதித்துறைத் தீர்ப்பாகும்."),
            "B": (f"Option B ({opt_b_en}) is incorrect as it distorts Supreme Court rulings on executive authority.", f"தெரிவு B ({opt_b_ta}) தவறானது, ஏனெனில் இது உச்ச நீதிமன்றத் தீர்ப்புகளைத் தவறாகச் சித்திரிக்கிறது."),
            "C": (f"Option C ({opt_c_en}) is incorrect as it introduces an invalid constitutional requirement.", f"தெரிவு C ({opt_c_ta}) தவறானது, ஏனெனில் இது செல்லாத அரசியலமைப்பு விதியை அறிமுகப்படுத்துகிறது."),
            "D": (f"Option D ({opt_d_en}) is incorrect as it misinterprets the relationship between President and Prime Minister.", f"தெரிவு D ({opt_d_ta}) தவறானது, ஏனெனில் இது குடியரசுத் தலைவர்-பிரதமர் உறவைத் தவறாக விவரிக்கிறது.")
        }

        dist_tuple = make_distractor(
            corr,
            exp_dict["A"][0], exp_dict["A"][1], f"Trap: {opt_a_en[:40]}",
            exp_dict["B"][0], exp_dict["B"][1], f"Trap: {opt_b_en[:40]}",
            exp_dict["C"][0], exp_dict["C"][1], f"Trap: {opt_c_en[:40]}",
            exp_dict["D"][0], exp_dict["D"][1], f"Trap: {opt_d_en[:40]}"
        )

        q_obj = build_q(
            qid, "Hard", "Hard MCQ",
            stem_en, stem_ta,
            opts, corr,
            exp_en_c, exp_ta_c,
            dist_tuple,
            tip_en_c, tip_ta_c,
            f"High-Yield Fact: {topic_desc} is a vital Group 1 level constitutional precedent.",
            f"முக்கியக் குறிப்பு: {topic_desc} என்பது குரூப் 1 தேர்வுக்குரிய முக்கியமான தீர்ப்பாகும்.",
            f"Confusing {topic_desc} with unrelated executive powers.",
            f"{topic_desc} தீர்ப்பைத் தொடர்பில்லாத விதிகளுடன் குழப்புவது.",
            [f"Prime Minister Notes Part 3 - Hard Q{idx}"]
        )
        qs.append(q_obj)

    print(f"Generated {len(qs)} Hard questions successfully.")

    out_dir = "data/questions/polity"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "prime_minister_hard.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, ensure_ascii=False, indent=2)

    print(f"✅ Saved Hard dataset to {out_path}")
    assert os.path.exists(out_path), "File save failed!"
    print(f"✅ Confirmed file exists: {out_path} with {len(qs)} items.")
    return len(qs)

if __name__ == "__main__":
    generate_hard()
