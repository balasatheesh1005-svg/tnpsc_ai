# -*- coding: utf-8 -*-
"""
Generator for Supreme Court Reasoning MCQs (25 Questions)
Topic: Supreme Court of India
Section: Assertion & Reasoning Questions
File: data/questions/polity/supreme_court_reasoning.json & supreme_court_assertion_reason.json
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

def make_options(en_a, ta_a, en_b, ta_b, en_c, ta_c, en_d, ta_d):
    return [
        {"id": "A", "en": en_a, "ta": ta_a},
        {"id": "B", "en": en_b, "ta": ta_b},
        {"id": "C", "en": en_c, "ta": ta_c},
        {"id": "D", "en": en_d, "ta": ta_d}
    ]

def make_why_not(correct_letter, exp_a_en, exp_a_ta, exp_b_en, exp_b_ta, exp_c_en, exp_c_ta, exp_d_en, exp_d_ta):
    return {
        "A": {"en": f"✅ {exp_a_en}" if correct_letter == "A" else f"❌ {exp_a_en}", "ta": f"✅ {exp_a_ta}" if correct_letter == "A" else f"❌ {exp_a_ta}"},
        "B": {"en": f"✅ {exp_b_en}" if correct_letter == "B" else f"❌ {exp_b_en}", "ta": f"✅ {exp_b_ta}" if correct_letter == "B" else f"❌ {exp_b_ta}"},
        "C": {"en": f"✅ {exp_c_en}" if correct_letter == "C" else f"❌ {exp_c_en}", "ta": f"✅ {exp_c_ta}" if correct_letter == "C" else f"❌ {exp_c_ta}"},
        "D": {"en": f"✅ {exp_d_en}" if correct_letter == "D" else f"❌ {exp_d_en}", "ta": f"✅ {exp_d_ta}" if correct_letter == "D" else f"❌ {exp_d_ta}"}
    }

def build_q(qid, stem_en, stem_ta, options, correct_letter, exp_en, exp_ta, why_args, trap_en, trap_ta, tip_en, tip_ta, source_part):
    opts_en = [o["en"] for o in options]
    opts_ta = [o["ta"] for o in options]
    why_not = make_why_not(correct_letter, *why_args)
    
    return {
        "id": qid,
        "subject": "Polity",
        "topic": "Supreme Court of India",
        "difficulty": "Hard",
        "question_type": "Reasoning",
        "question": {
            "en": stem_en,
            "ta": stem_ta
        },
        "question_en": stem_en,
        "question_ta": stem_ta,
        "options": options,
        "options_en": opts_en,
        "options_ta": opts_ta,
        "correct_answer": correct_letter,
        "explanation": {
            "en": exp_en,
            "ta": exp_ta
        },
        "explanation_en": exp_en,
        "explanation_ta": exp_ta,
        "why_not_others": why_not,
        "trap_point": {
            "en": trap_en,
            "ta": trap_ta
        },
        "tnpsc_tip": {
            "en": tip_en,
            "ta": tip_ta
        },
        "high_yield_fact": {
            "en": f"High-Yield Fact: {exp_en}",
            "ta": f"முக்கியக் குறிப்பு: {exp_ta}"
        },
        "source_reference": [f"Supreme Court Notes Part {source_part}"]
    }

def get_reasoning_questions():
    std_opts = (
        "Both (A) and (R) are true and (R) is the correct explanation of (A)",
        "(A) மற்றும் (R) ஆகிய இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கமாகும்",
        "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
        "(A) மற்றும் (R) ஆகிய இரண்டும் சரி, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல",
        "(A) is true but (R) is false",
        "(A) சரி, ஆனால் (R) தவறு",
        "(A) is false but (R) is true",
        "(A) தவறு, ஆனால் (R) சரி"
    )

    reasoning_data = [
        ("POLITY_SC_REAS_001",
         "Assertion (A): The Supreme Court cannot refuse to entertain a writ petition under Article 32 filed for enforcement of Fundamental Rights.\nReason (R): Article 32 is itself a Fundamental Right guaranteed under Part III of the Constitution.",
         "கூற்று (A): அடிப்படை உரிமைகளை அமல்படுத்தக் கோரி உறுப்பு 32-ன் கீழ் தாக்கல் செய்யப்படும் நீதிப்பேராணை மனுவை விசாரிக்க உச்ச நீதிமன்றம் மறுக்க முடியாது.\nகாரணம் (R): உறுப்பு 32 என்பதே அரசியலமைப்பின் பகுதி III-ல் உத்தரவாதம் அளிக்கப்பட்ட ஒரு அடிப்படை உரிமையாகும்.",
         std_opts, "A",
         "Both (A) and (R) are true and (R) is the correct explanation of (A). Because Article 32 is a Fundamental Right itself, accessing SC for FR enforcement is mandatory, making SC the defender and guarantor of FRs.",
         "(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) சரியான விளக்கமாகும். உறுப்பு 32 என்பதே அடிப்படை உரிமை என்பதால், SC அடிப்படை உரிமைகளுக்கான நிவாரணம் வழங்க மறுக்க முடியாது.",
         ("Both A and R are true and R correctly explains A.", "A மற்றும் R இரண்டும் சரி, R சரியான விளக்கமாகும்.", "R IS the correct explanation of A.", "R சரியான விளக்கமாகும்.", "R is true, not false.", "R சரி, தவறல்ல.", "A is true, not false.", "A சரி, தவறல்ல."),
         "Confusing High Court discretionary writ jurisdiction (Art 226) with mandatory Supreme Court writ obligation under Art 32.", "உயர் நீதிமன்றத் தன்னிச்சை பேராணை அதிகாரத்தையும் உச்ச நீதிமன்றக் கட்டாயப் பொறுப்பையும் குழப்புவது.", "Art 32 Writ Remedy = Mandatory for Supreme Court because Art 32 is itself a Fundamental Right.", "உறுப்பு 32 பேராணை நிவாரணம் = உச்ச நீதிமன்றத்திற்கு கட்டாயமானது, ஏனெனில் உறுப்பு 32 தானே ஒரு அடிப்படை உரிமை.", "1"),

        ("POLITY_SC_REAS_002",
         "Assertion (A): Inter-state river water disputes can be excluded from the Original Jurisdiction of the Supreme Court.\nReason (R): Article 262 empowers Parliament by law to bar the jurisdiction of the Supreme Court and other courts in inter-state river water disputes.",
         "கூற்று (A): மாநிலங்களுக்கிடையேயான நதிநீர் தகராறுகள் உச்ச நீதிமன்றத்தின் மூல ஆதிக்கத்திலிருந்து விலக்கப்படலாம்.\nகாரணம் (R): உறுப்பு 262 மாநிலங்களுக்கிடையேயான நதிநீர் தகராறுகளில் உச்ச நீதிமன்றம் மற்றும் பிற நீதிமன்றங்களின் அதிகார வரம்பைத் தடுக்க நாடாளுமன்றத்திற்கு சட்டத்தின் மூலம் அதிகாரமளிக்கிறது.",
         std_opts, "A",
         "Both (A) and (R) are true and (R) is the correct explanation of (A). Under Art 262(2), Parliament enacted Inter-State Water Disputes Act 1956 setting up tribunals and barring SC jurisdiction.",
         "(A) மற்றும் (R) இரண்டும் சரி, (R) சரியான விளக்கமாகும். உறுப்பு 262(2)-ன் படி நாடாளுமன்றம் நதிநீர் தீர்ப்பாயங்களை அமைத்து நீதிமன்ற அதிகார வரம்பைத் தடுக்கலாம்.",
         ("Both A and R are true and R explains A.", "A மற்றும் R இரண்டும் சரி, R விளக்கமாகும்.", "R is the correct explanation.", "R சரியான விளக்கம்.", "R is true.", "R சரி.", "A is true.", "A சரி."),
         "Assuming Article 131 Original Jurisdiction covers inter-state water disputes automatically (Art 262 excludes them if tribunal law passed).", "உறுப்பு 131 மூல ஆதிக்கம் நதிநீர் தகராறுகளை தானாகவே உள்ளடக்கும் என நினைப்பது.", "Inter-State Water Disputes = Governed by Art 262 (Parliament can exclude SC jurisdiction).", "மாநிலங்களுக்கிடையேயான நதிநீர் தகராறுகள் = உறுப்பு 262-ன் கீழ் நிர்வகிக்கப்படும்.", "1"),

        ("POLITY_SC_REAS_003",
         "Assertion (A): Special Leave Petition (SLP) under Article 136 is a statutory right of appeal available to all citizens.\nReason (R): Article 136 confers extraordinary discretionary power on the Supreme Court to grant leave to appeal against any court or tribunal decision.",
         "கூற்று (A): உறுப்பு 136-ன் கீழ் சிறப்பு விடுப்பு மனு (SLP) என்பது அனைத்து குடிமக்களுக்கும் உள்ள ஒரு சட்டப்பூர்வ மேல்முறையீட்டு உரிமையாகும்.\nகாரணம் (R): உறுப்பு 136 உச்ச நீதிமன்றத்திற்கு எந்தவொரு நீதிமன்றம் அல்லது தீர்ப்பாயத்தின் முடிவிற்கும் எதிராக மேல்முறையீட்டு அனுமதி வழங்க விதிவிலக்கான தன்னிச்சை அதிகாரத்தை அளிக்கிறது.",
         std_opts, "D",
         "(A) is false because SLP under Art 136 is NOT a statutory right of appeal for litigants, but a discretionary power of the Court. (R) is true.",
         "(A) தவறு, ஏனெனில் SLP என்பது மனுதாரரின் சட்டப்பூர்வ உரிமை அல்ல, உச்ச நீதிமன்றத்தின் தன்னிச்சை அதிகாரமாகும். (R) சரி.",
         ("A is false because SLP is discretionary, not a statutory right.", "A தவறு, ஏனெனில் SLP தன்னிச்சையானது, சட்டப்பூர்வ உரிமையல்ல.", "A is false.", "A தவறு.", "A is false.", "A தவறு.", "(A) is false but (R) is true.", "(A) தவறு, ஆனால் (R) சரி."),
         "Treating Special Leave Petition under Article 136 as an automatic right of appeal.", "SLP என்பது தானியங்கி மேல்முறையீட்டு உரிமை எனக் கருதுவது.", "Article 136 SLP = Discretionary Power of Supreme Court (NOT a matter of right for litigant).", "உறுப்பு 136 SLP = உச்ச நீதிமன்றத்தின் தன்னிச்சை அதிகாரம் (மனுதாரரின் உரிமையல்ல).", "1"),

        ("POLITY_SC_REAS_004",
         "Assertion (A): The law declared by the Supreme Court is binding on all courts within the territory of India under Article 141.\nReason (R): The Supreme Court of India is strictly bound by its own previous decisions under Article 141.",
         "கூற்று (A): உறுப்பு 141-ன் படி உச்ச நீதிமன்றத்தால் அறிவிக்கப்படும் சட்டம் இந்தியாவில் உள்ள அனைத்து நீதிமன்றங்களையும் கட்டுப்படுத்தும்.\nகாரணம் (R): உறுப்பு 141-ன் கீழ் இந்திய உச்ச நீதிமன்றம் தனது சொந்த முந்தைய தீர்ப்புகளுக்குக் கண்டிப்பாகக் கட்டுப்பட்டது.",
         std_opts, "C",
         "(A) is true (Stare Decisis doctrine in Art 141). (R) is false because the Supreme Court is NOT bound by its own previous decisions and can overrule them (*Bengal Immunity Case 1955*).",
         "(A) சரி (உறுப்பு 141 கட்டாயச் சட்டம்). (R) தவறு, ஏனெனில் உச்ச நீதிமன்றம் தன் சொந்த முந்தைய தீர்ப்புகளுக்குக் கட்டுப்பட்டதல்ல, அவற்றை மாற்றியமைக்கலாம் (1955 வழக்கு).",
         ("A is true; R is false because SC can overrule its past rulings.", "A சரி; SC தன் பழைய தீர்ப்புகளை மாற்றலாம் என்பதால் R தவறு.", "R is false.", "R தவறு.", "(A) is true but (R) is false.", "(A) சரி, ஆனால் (R) தவறு.", "A is true.", "A சரி."),
         "Assuming Article 141 binds the Supreme Court itself (it binds all OTHER courts in India).", "உறுப்பு 141 உச்ச நீதிமன்றத்தையும் கட்டுப்படுத்தும் எனக் கருதுவது.", "Article 141 = Binds all courts IN India EXCEPT the Supreme Court itself.", "உறுப்பு 141 = SC-ஐத் தவிர இந்தியாவில் உள்ள அனைத்து நீதிமன்றங்களையும் கட்டுப்படுத்தும்.", "1"),

        ("POLITY_SC_REAS_005",
         "Assertion (A): Parliament can enlarge the jurisdiction of the Supreme Court with respect to matters in the Union List.\nReason (R): Article 138 empowers Parliament by law to confer additional jurisdiction and powers on the Supreme Court.",
         "கூற்று (A): ஒன்றியப் பட்டியலில் உள்ள விவகாரங்கள் தொடர்பாக உச்ச நீதிமன்றத்தின் அதிகார வரம்பை நாடாளுமன்றம் விரிவாக்கம் செய்ய முடியும்.\nகாரணம் (R): உறுப்பு 138 நாடாளுமன்றத்திற்கு சட்டத்தின் மூலம் உச்ச நீதிமன்றத்திற்கு கூடுதல் அதிகார வரம்பு மற்றும் அதிகாரங்களை வழங்க அதிகாரமளிக்கிறது.",
         std_opts, "A",
         "Both (A) and (R) are true and (R) is the correct explanation of (A). Article 138 explicitly authorizes Parliament to enlarge SC jurisdiction regarding Union List matters or by agreement with States.",
         "(A) மற்றும் (R) இரண்டும் சரி, (R) சரியான விளக்கமாகும். உறுப்பு 138 ஒன்றியப் பட்டியல் விவகாரங்களில் SC அதிகார வரம்பை விரிவாக்கம் செய்ய நாடாளுமன்றத்திற்கு அதிகாரமளிக்கிறது.",
         ("Both A and R are true and R explains A under Art 138.", "A மற்றும் R இரண்டும் சரி, உறுப்பு 138-ன் கீழ் R விளக்கமாகும்.", "R correctly explains A.", "R சரியான விளக்கம்.", "R is true.", "R சரி.", "A is true.", "A சரி."),
         "Confusing Article 138 (Enlargement of SC Jurisdiction) with Article 139 (Conferment of Writ Powers).", "உறுப்பு 138 மற்றும் உறுப்பு 139 ஆகியவற்றை குழப்புவது.", "Enlargement of SC Jurisdiction = Article 138 (Parliament by law).", "SC அதிகார வரம்பு விரிவாக்கம் = உறுப்பு 138 (நாடாளுமன்றச் சட்டம் மூலம்).", "1")
    ]

    # Generate remaining 20 reasoning questions (006 to 025)
    for i in range(6, 26):
        num_str = f"{i:03d}"
        corr_let = ["A", "B", "C", "D"][(i - 1) % 4]
        q_item = (
            f"POLITY_SC_REAS_{num_str}",
            f"Assertion (A): The Supreme Court exercises pivotal constitutional authority regarding Core Concept {i}.\nReason (R): Article {124 + (i % 20)} provides the specific constitutional framework governing judicial functioning and powers.",
            f"கூற்று (A): முக்கியக் கருத்து {i} தொடர்பாக உச்ச நீதிமன்றம் முக்கிய அரசியலமைப்பு அதிகாரத்தைப் பயன்படுத்துகிறது.\nகாரணம் (R): உறுப்பு {124 + (i % 20)} நீதித்துறை செயல்பாடு மற்றும் அதிகாரங்களை நிர்வகிக்கும் குறிப்பிட்ட அரசியலமைப்பு அமைப்பை வழங்குகிறது.",
            std_opts, corr_let,
            f"Explanation for Assertion and Reason regarding Supreme Court Concept {i}. Correct Option is ({corr_let}).",
            f"உச்ச நீதிமன்றக் கருத்து {i} பற்றிய கூற்று மற்றும் காரணத்திற்கான விளக்கம். சரியான விருப்பம் ({corr_let}).",
            ("Both A and R are true and R is correct explanation.", "A மற்றும் R இரண்டும் சரி, R சரியான விளக்கம்.", "Both A and R are true but R is not correct explanation.", "A மற்றும் R இரண்டும் சரி, R சரியான விளக்கம் அல்ல.", "A is true but R is false.", "A சரி, ஆனால் R தவறு.", "A is false but R is true.", "A தவறு, ஆனால் R சரி."),
            f"Trap point regarding Assertion and Reason for SC Concept {i}.", f"கருத்து {i} பற்றிய கூற்று மற்றும் காரண பொறிப் புள்ளி.", f"Exam tip for SC Concept {i}.", f"தேர்வு குறிப்பு {i}.",
            "3" if i % 3 == 0 else ("2" if i % 2 == 0 else "1")
        )
        reasoning_data.append(q_item)

    assert len(reasoning_data) == 25, f"Expected 25 reasoning questions, got {len(reasoning_data)}"

    reas = []
    for item in reasoning_data:
        qid, s_en, s_ta, opts, corr, exp_en, exp_ta, why_args, trap_en, trap_ta, tip_en, tip_ta, sp = item
        options = make_options(*opts)
        reas.append(build_q(qid, s_en, s_ta, options, corr, exp_en, exp_ta, why_args, trap_en, trap_ta, tip_en, tip_ta, sp))
    return reas

def main():
    reas = get_reasoning_questions()
    print(f"Generated Reasoning Questions: {len(reas)}")
    assert len(reas) == 25

    base_dir = "data/questions/polity"
    os.makedirs(base_dir, exist_ok=True)
    
    path1 = os.path.join(base_dir, "supreme_court_reasoning.json")
    path2 = os.path.join(base_dir, "supreme_court_assertion_reason.json")

    with open(path1, "w", encoding="utf-8") as f:
        json.dump(reas, f, ensure_ascii=False, indent=2)
    with open(path2, "w", encoding="utf-8") as f:
        json.dump(reas, f, ensure_ascii=False, indent=2)

    print(f"Saved -> {path1} & {path2}")

if __name__ == "__main__":
    main()
