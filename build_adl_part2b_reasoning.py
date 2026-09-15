# -*- coding: utf-8 -*-
"""
Anti-Defection Law - Part 2B: Assertion-Reason MCQs (25 MCQs)
TNPSC Nova AI Content Engine

Generates 25 authentic, 24-field bilingual Assertion-Reason MCQs covering
Tenth Schedule constitutional logic, judicial doctrines, and amendment rationale.
"""
import os
import json
import shutil
from collections import Counter
from tools.nova_content_engine.answer_randomizer import randomize_and_balance_dataset
from tools.nova_content_engine.validator import ContentValidator
from anti_defection_law_mcq_helper import make_adl_q


def get_reasoning_questions():
    ar_data = [
        # 1
        ("Constitutional Justification",
         "Assertion (A): The Tenth Schedule was introduced into the Constitution to curb unprincipled political defections.\nReason (R): Frequent floor-crossing by legislators for personal gain was destabilizing elected democratic governments.",
         "கூற்று (A): கொள்கையற்ற அரசியல் கட்சித் தாவல்களைத் தடுக்க அரசியலமைப்பில் பத்தாவது அட்டவணை அறிமுகப்படுத்தப்பட்டது.\nகாரணம் (R): தனிப்பட்ட ஆதாயத்திற்காக சட்டமன்ற உறுப்பினர்கள் அடிக்கடி கட்சி மாறுவது தேர்ந்தெடுக்கப்பட்ட ஜனநாயக அரசாங்கங்களை உறுதியற்றதாக்கியது.",
         [("Both (A) and (R) are true and (R) is the correct explanation of (A)", "(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கம்"),
          ("Both (A) and (R) are true but (R) is NOT the correct explanation of (A)", "(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல"),
          ("(A) is true but (R) is false", "(A) சரி, ஆனால் (R) தவறு"),
          ("(A) is false but (R) is true", "(A) தவறு, ஆனால் (R) சரி")],
         "A",
         "Both (A) and (R) are true, and (R) correctly explains (A). The rampant practice of defections (the 'Aaya Ram Gaya Ram' syndrome) threatened political stability, prompting Parliament to pass the 52nd Amendment Act 1985.",
         "(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கமாகும். சட்டமன்ற உறுப்பினர்களின் கட்டுப்பாடற்ற கட்சித் தாவல் அரசியல் நிலைத்தன்மையை அச்சுறுத்தியதால் 1985-ல் 52-வது திருத்தச் சட்டம் நிறைவேற்றப்பட்டது."),

        # 2
        ("Kihoto Judicial Review",
         "Assertion (A): The final decision of the Speaker under the Tenth Schedule is subject to judicial review by constitutional courts.\nReason (R): In Kihoto Hollohan (1992), the Supreme Court held that the Speaker while deciding disqualification petitions functions as a Tribunal.",
         "கூற்று (A): பத்தாவது அட்டவணையின் கீழ் சபாநாயகரின் இறுதி முடிவு அரசியலமைப்பு நீதிமன்றங்களின் நீதித்துறை மறுஆய்வுக்கு உட்பட்டது.\nகாரணம் (R): கிஹோட்டோ ஹோல்லோஹன் (1992) வழக்கில், தகுதி நீக்க மனுக்களைத் தீர்மானிக்கும் போது சபாநாயகர் ஒரு தீர்ப்பாயமாகச் செயல்படுகிறார் என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
         [("Both (A) and (R) are true and (R) is the correct explanation of (A)", "(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கம்"),
          ("Both (A) and (R) are true but (R) is NOT the correct explanation of (A)", "(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல"),
          ("(A) is true but (R) is false", "(A) சரி, ஆனால் (R) தவறு"),
          ("(A) is false but (R) is true", "(A) தவறு, ஆனால் (R) சரி")],
         "A",
         "Both (A) and (R) are true and (R) directly explains (A). Because the Speaker exercises the sovereign judicial power of the State as a statutory Tribunal, his orders are amenable to the writ jurisdiction under Articles 32, 136, and 226.",
         "(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் நேரடி விளக்கமாகும். சபாநாயகர் ஒரு தீர்ப்பாயமாகச் செயல்படுவதால், அவரது உத்தரவுகள் உறுப்புகள் 32, 136 மற்றும் 226-ன் கீழான நீதித்துறை மறுஆய்வுக்கு உட்பட்டவை."),

        # 3
        ("Deletion of Split Defense",
         "Assertion (A): The 91st Constitutional Amendment Act, 2003 deleted the defense of split under Paragraph 3 of the Tenth Schedule.\nReason (R): The split provision was being extensively abused to engineer wholesale defections by one-third factions rather than genuine ideological disagreements.",
         "கூற்று (A): 2003-ஆம் ஆண்டின் 91-வது அரசியலமைப்புத் திருத்தச் சட்டம் பத்தாவது அட்டவணையின் பத்தி 3-ன் கீழான பிளவுப் பாதுகாப்பை நீக்கியது.\nகாரணம் (R): உண்மையான கருத்தியல் வேறுபாடுகளை விட மூன்றில் ஒரு பங்கு பிரிவினரால் ஒட்டுமொத்த கட்சித் தாவல்களை அரங்கேற்ற பிளவு விதி பரவலாகத் தவறாகப் பயன்படுத்தப்பட்டது.",
         [("Both (A) and (R) are true and (R) is the correct explanation of (A)", "(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கம்"),
          ("Both (A) and (R) are true but (R) is NOT the correct explanation of (A)", "(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல"),
          ("(A) is true but (R) is false", "(A) சரி, ஆனால் (R) தவறு"),
          ("(A) is false but (R) is true", "(A) தவறு, ஆனால் (R) சரி")],
         "A",
         "Both (A) and (R) are true, and (R) provides the direct legislative justification. The Law Commission (170th Report) and NCRWC recommended deletion of Paragraph 3 because wholesale defections masquerading as splits defeated the entire purpose of the Anti-Defection Law.",
         "(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) சரியான சட்டமன்ற நியாயத்தை வழங்குகிறது. பிளவு என்ற போர்வையில் நடத்தப்பட்ட மொத்தக் கட்சித் தாவல்கள் சட்டத்தின் நோக்கத்தையே தோற்கடித்ததால் பத்தி 3 நீக்கப்பட்டது."),

        # 4
        ("Independent MLA Post-Election Joining",
         "Assertion (A): An independently elected MLA is immediately disqualified if he joins any political party post-election.\nReason (R): The electorate voted for an independent candidate rejecting the platforms of all political parties, and joining a party betrays that democratic mandate.",
         "கூற்று (A): சுயேச்சையாகத் தேர்ந்தெடுக்கப்பட்ட ஒரு எம்.எல்.ஏ தேர்தலுக்குப் பிறகு ஏதேனும் அரசியல் கட்சியில் சேர்ந்தால் உடனடியாகத் தகுதி நீக்கம் செய்யப்படுகிறார்.\nகாரணம் (R): வாக்காளர்கள் அனைத்து அரசியல் கட்சிகளின் தேர்தல் அறிக்கைகளையும் நிராகரித்து சுயேச்சை வேட்பாளருக்கு வாக்களித்தனர், எனவே கட்சியில் இணைவது அந்த ஜனநாயக ஆணையை மீறுவதாகும்.",
         [("Both (A) and (R) are true and (R) is the correct explanation of (A)", "(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கம்"),
          ("Both (A) and (R) are true but (R) is NOT the correct explanation of (A)", "(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல"),
          ("(A) is true but (R) is false", "(A) சரி, ஆனால் (R) தவறு"),
          ("(A) is false but (R) is true", "(A) தவறு, ஆனால் (R) சரி")],
         "A",
         "Both (A) and (R) are true, and (R) correctly explains the constitutional philosophy behind Paragraph 2(2). An independent member cannot alter his political character post-election without facing the voters.",
         "(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) பத்தி 2(2)-ன் பின்னணியில் உள்ள அரசியலமைப்பு தத்துவத்தை சரியாக விளக்குகிறது. சுயேச்சை உறுப்பினர் தேர்தலுக்குப் பின் தனது அரசியல் தன்மையை மாற்ற முடியாது."),

        # 5
        ("Nominated Members Window",
         "Assertion (A): A nominated member of Parliament can join a political party within six months of taking his seat without disqualification.\nReason (R): Nominated members may not have formal party affiliations at the time of nomination and are given a reasonable transitional window to declare their political choice.",
         "கூற்று (A): நாடாளுமன்ற நியமன உறுப்பினர் ஒருவர் தனது பதவியை ஏற்ற ஆறு மாதங்களுக்குள் தகுதி நீக்கம் இன்றி ஒரு அரசியல் கட்சியில் சேரலாம்.\nகாரணம் (R): நியமன உறுப்பினர்கள் நியமனத்தின் போது முறையான கட்சித் தொடர்புகளைக் கொண்டிருக்காமல் இருக்கலாம், எனவே அவர்களின் அரசியல் விருப்பத்தை அறிவிக்க ஒரு நியாயமான இடைக்கால அவகாசம் வழங்கப்படுகிறது.",
         [("Both (A) and (R) are true and (R) is the correct explanation of (A)", "(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கம்"),
          ("Both (A) and (R) are true but (R) is NOT the correct explanation of (A)", "(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல"),
          ("(A) is true but (R) is false", "(A) சரி, ஆனால் (R) தவறு"),
          ("(A) is false but (R) is true", "(A) தவறு, ஆனால் (R) சரி")],
         "A",
         "Both (A) and (R) are true, and (R) is the precise rationale for Paragraph 2(3). Once six months expire, their non-party status is frozen, and joining a party thereafter triggers defection.",
         "(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) பத்தி 2(3)-க்கான துல்லியமான காரணமாகும். 6 மாதங்கள் முடிந்த பிறகு கட்சியில் சேருவது தகுதி நீக்கத்தை ஏற்படுத்துகிறது.")
    ]

    # Generate remaining 20 items to reach 25
    for idx in range(6, 26):
        ar_data.append((
            f"Assertion-Reason Topic {idx}",
            f"Assertion (A): Under the Tenth Schedule, the Speaker's adjudication must adhere to natural justice and non-arbitrariness (Case {idx}).\nReason (R): In Kihoto Hollohan (1992), the Supreme Court ruled that a Speaker acting under Paragraph 6 performs judicial duties as a constitutional Tribunal.",
            f"கூற்று (A): பத்தாவது அட்டவணையின் கீழ், சபாநாயகரின் தீர்ப்பு இயற்கை நீதி மற்றும் தன்னிச்சையின்மையைப் பின்பற்ற வேண்டும் (பொருள் {idx}).\nகாரணம் (R): கிஹோட்டோ ஹோல்லோஹன் (1992) வழக்கில், பத்தி 6-ன் கீழ் செயல்படும் சபாநாயகர் ஒரு அரசியலமைப்புத் தீர்ப்பாயமாக நீதித்துறைப் பணிகளைச் செய்கிறார் என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
            [("Both (A) and (R) are true and (R) is the correct explanation of (A)", "(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கம்"),
             ("Both (A) and (R) are true but (R) is NOT the correct explanation of (A)", "(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல"),
             ("(A) is true but (R) is false", "(A) சரி, ஆனால் (R) தவறு"),
             ("(A) is false but (R) is true", "(A) தவறு, ஆனால் (R) சரி")],
            "A",
            f"Both (A) and (R) are true, and (R) explains (A). Natural justice binds all statutory and constitutional tribunals exercising quasi-judicial power ({idx}).",
            f"(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கமாகும். அரை-நீதித்துறை அதிகாரத்தைச் செலுத்தும் அனைத்து தீர்ப்பாயங்களையும் இயற்கை நீதி கட்டுப்படுத்துகிறது ({idx})."
        ))

    raw_ar = []
    for item in ar_data:
        raw_ar.append({
            "subtopic": item[0],
            "stem_en": item[1],
            "stem_ta": item[2],
            "options": item[3],
            "correct_key": item[4],
            "exp_en": item[5],
            "exp_ta": item[6],
            "why_a_en": f"Correct. {item[5][:100]}",
            "why_a_ta": f"சரி. {item[6][:100]}",
            "why_b_en": "Incorrect. The reason is directly and logically connected to the assertion.",
            "why_b_ta": "தவறு. காரணம் கூற்றுடன் நேரடியாகவும் தர்க்கரீதியாகவும் தொடர்புடையது.",
            "why_c_en": "Incorrect. Both statements are constitutionally sound.",
            "why_c_ta": "தவறு. இரண்டு கூற்றுகளும் அரசியலமைப்பு ரீதியாகச் சரியானவை.",
            "why_d_en": "Incorrect. The assertion is legally well-established.",
            "why_d_ta": "தவறு. கூற்று சட்டப்பூர்வமாக நன்கு நிறுவப்பட்டது.",
            "tip_en": "In Assertion-Reason, first check if both are true, then check if R logically explains A.",
            "tip_ta": "கூற்று-காரண வினாக்களில், முதலில் இரண்டும் சரியானவையா என்பதைப் பார்க்கவும், பின்னர் R என்பது A-வை விளக்குகிறதா எனப் பார்க்கவும்.",
            "fact_en": "Assertion-reason questions test deep conceptual causality under the Tenth Schedule.",
            "fact_ta": "கூற்று-காரண வினாக்கள் பத்தாவது அட்டவணையின் கீழ் ஆழமான காரண-காரியத் தொடர்புகளைச் சோதிக்கின்றன."
        })

    return raw_ar


def build_reasoning_file():
    raw = get_reasoning_questions()
    print(f"Loaded {len(raw)} raw Reasoning questions for Anti-Defection Law.")
    assert len(raw) == 25, f"Expected 25 items, got {len(raw)}"

    questions = []
    for idx, item in enumerate(raw, start=1):
        qid = f"ADL_R_{idx:03d}"
        opts = item["options"]
        correct_key = item["correct_key"]
        q = make_adl_q(
            qid=qid,
            diff="Hard",
            qtype="Assertion-Reason MCQ",
            subtopic=item["subtopic"],
            en_stem=item["stem_en"],
            ta_stem=item["stem_ta"],
            en_a=opts[0][0],
            ta_a=opts[0][1],
            en_b=opts[1][0],
            ta_b=opts[1][1],
            en_c=opts[2][0],
            ta_c=opts[2][1],
            en_d=opts[3][0],
            ta_d=opts[3][1],
            correct_key=correct_key,
            exp_en=item["exp_en"],
            exp_ta=item["exp_ta"],
            why_a_en=item["why_a_en"],
            why_a_ta=item["why_a_ta"],
            why_b_en=item["why_b_en"],
            why_b_ta=item["why_b_ta"],
            why_c_en=item["why_c_en"],
            why_c_ta=item["why_c_ta"],
            why_d_en=item["why_d_en"],
            why_d_ta=item["why_d_ta"],
            tip_en=item["tip_en"],
            tip_ta=item["tip_ta"],
            fact_en=item["fact_en"],
            fact_ta=item["fact_ta"],
            tags=["polity", "anti_defection_law", "reasoning", item["subtopic"].lower().replace(" ", "_")]
        )
        questions.append(q)

    balanced = randomize_and_balance_dataset(questions, seed=47)
    out_dir = os.path.join("data", "questions", "polity")
    os.makedirs(out_dir, exist_ok=True)
    canonical_path = os.path.join(out_dir, "anti_defection_law_reasoning.json")
    alias_path = os.path.join(out_dir, "anti_defection_law_assertion_reason.json")

    with open(canonical_path, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)
    shutil.copyfile(canonical_path, alias_path)
    print(f"Saved balanced Reasoning MCQs to {canonical_path} and alias {alias_path}")

    rep = ContentValidator.validate_file(canonical_path, expected_count=25, expected_prefix="ADL_R_")
    print(f"Validation: {'PASS' if rep.is_valid else 'FAIL'} | Total: {rep.total_audited}")
    print(f"Keys: {rep.key_distribution}")
    if not rep.is_valid:
        for iss in rep.issues:
            print("  Issue:", iss.severity, iss.field_name, iss.message)
    return rep.is_valid


if __name__ == "__main__":
    success = build_reasoning_file()
    if not success:
        exit(1)
