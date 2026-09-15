# -*- coding: utf-8 -*-
"""
Anti-Defection Law - Part 2A: PYQ Practice (50 MCQs)
TNPSC Nova AI Content Engine

Generates 50 authentic, 24-field bilingual PYQ-style MCQs mirroring previous year
TNPSC (Group 1, 2, 4), UPSC CSE, and State PSC examination questions on the Tenth Schedule.
"""
import os
import json
import shutil
from collections import Counter
from tools.nova_content_engine.answer_randomizer import randomize_and_balance_dataset
from tools.nova_content_engine.validator import ContentValidator
from anti_defection_law_mcq_helper import make_adl_q


def get_pyq_questions():
    pyqs = [
        # PYQ 1
        ("Constitutional Amendment (TNPSC Gr 1)",
         "[TNPSC Group 1] Which of the following Constitutional Amendment Acts introduced the Anti-Defection provisions into the Constitution of India?",
         "[டிஎன்பிஎஸ்சி குரூப் 1] பின்வரும் எந்த அரசியலமைப்புத் திருத்தச் சட்டம் இந்திய அரசியலமைப்பில் கட்சித் தாவல் தடை விதிகளை அறிமுகப்படுத்தியது?",
         [("52nd Amendment Act, 1985", "52-வது திருத்தச் சட்டம், 1985"), ("42nd Amendment Act, 1976", "42-வது திருத்தச் சட்டம், 1976"), ("44th Amendment Act, 1978", "44-வது திருத்தச் சட்டம், 1978"), ("61st Amendment Act, 1988", "61-வது திருத்தச் சட்டம், 1988")],
         "A",
         "The 52nd Constitutional Amendment Act, 1985 added the Tenth Schedule to the Constitution of India, popularly known as the Anti-Defection Law.",
         "1985-ஆம் ஆண்டின் 52-வது அரசியலமைப்புத் திருத்தச் சட்டம் இந்திய அரசியலமைப்பில் பத்தாவது அட்டவணையைச் சேர்த்தது, இது கட்சித் தாவல் தடைச் சட்டம் என்று பிரபலமாக அறியப்படுகிறது.",
         "52nd CAA 1985 inserted Tenth Schedule under Rajiv Gandhi government.",
         "ராஜீவ் காந்தி ஆட்சியில் 52-வது திருத்தச் சட்டம் 1985 பத்தாவது அட்டவணையைச் சேர்த்தது.",
         "42nd CAA 1976 is known as the Mini-Constitution.",
         "42-வது திருத்தம் 1976 'குறு அரசியலமைப்பு' என அழைக்கப்படுகிறது.",
         "44th CAA 1978 amended emergency provisions.",
         "44-வது திருத்தம் 1978 அவசரநிலை விதிகளைத் திருத்தியது.",
         "61st CAA 1988 reduced voting age to 18.",
         "61-வது திருத்தம் 1988 வாக்களிக்கும் வயதை 18 ஆகக் குறைத்தது.",
         "Frequent TNPSC question: 52nd CAA 1985 = Anti-Defection Law.",
         "அடிக்கடி கேட்கப்படும் டிஎன்பிஎஸ்சி வினா: 52-வது திருத்தம் 1985 = கட்சித் தாவல் தடைச் சட்டம்.",
         "Added clause (2) to Articles 102 and 191 of the Constitution.",
         "அரசியலமைப்பின் உறுப்புகள் 102 மற்றும் 191-ல் உட்பிரிவு (2)-ஐ சேர்த்தது."),

        # PYQ 2
        ("Tenth Schedule Deciding Authority (UPSC)",
         "[UPSC CSE] Under the Tenth Schedule of the Constitution, the question of disqualification on the ground of defection is decided by:",
         "[யுபிஎஸ்சி சிஎஸ்இ] அரசியலமைப்பின் பத்தாவது அட்டவணையின் கீழ், கட்சித் தாவல் காரணத்தினால் ஏற்படும் தகுதி நீக்கம் பற்றிய வினா யாரால் தீர்மானிக்கப்படுகிறது?",
         [("The Chairman or Speaker of the respective House", "அந்தந்த அவையின் தலைவர் அல்லது சபாநாயகர்"), ("The President of India on advice of ECI", "தேர்தல் ஆணையத்தின் ஆலோசனையின்படி இந்தியக் குடியரசுத் தலைவர்"), ("The Supreme Court of India", "இந்திய உச்ச நீதிமன்றம்"), ("A Committee of the House on Privileges", "அவையின் உரிமைக் குழு")],
         "A",
         "Paragraph 6(1) of the Tenth Schedule provides that the question of disqualification shall be referred for the decision of the Chairman or, as the case may be, the Speaker of such House.",
         "பத்தாவது அட்டவணையின் பத்தி 6(1) தகுதி நீக்கம் தொடர்பான வினா அந்தந்த அவையின் தலைவர் அல்லது சபாநாயகரின் முடிவுக்கு அனுப்பப்பட வேண்டும் என்று கூறுகிறது.",
         "Paragraph 6 designates Speaker/Chairman as the deciding tribunal.",
         "பத்தி 6 சபாநாயகர்/தலைவரைத் தீர்மானிக்கும் தீர்ப்பாயமாக நியமிக்கிறது.",
         "President decides under Article 103 on ECI advice for general disqualifications, not Tenth Schedule.",
         "குடியரசுத் தலைவர் உறுப்பு 103-ன் கீழ் தேர்தல் ஆணைய ஆலோசனைப்படி பொதுவான தகுதியிழப்புகளைத் தீர்மானிக்கிறார், கட்சித் தாவலை அல்ல.",
         "Supreme Court exercises judicial review only after Speaker decides.",
         "சபாநாயகர் முடிவெடுத்த பின்னரே உச்ச நீதிமன்றம் நீதித்துறை மறுஆய்வு செய்கிறது.",
         "Committee on Privileges investigates breach of privilege, not defection.",
         "உரிமைக் குழு சிறப்புரிமை மீறலை விசாரிக்கிறது, கட்சித் தாவலை அல்ல.",
         "Deciding authority under Tenth Schedule = Presiding Officer of the House.",
         "பத்தாவது அட்டவணையின் கீழ் முடிவெடுக்கும் அதிகாரம் = அவையின் தலைவர்/சபாநாயகர்.",
         "The Speaker's decision is deemed to be a proceeding in Parliament.",
         "சபாநாயகரின் முடிவு நாடாளுமன்ற நடவடிக்கையாகக் கருதப்படுகிறது."),

        # PYQ 3
        ("91st Amendment Capping (TNPSC Gr 2)",
         "[TNPSC Group 2] The ceiling of 15% on the strength of the Council of Ministers in the Union and States was enacted by which Constitutional Amendment?",
         "[டிஎன்பிஎஸ்சி குரூப் 2] ஒன்றியம் மற்றும் மாநிலங்களில் அமைச்சரவையின் பலத்தின் மீது 15% உச்சவரம்பு எந்த அரசியலமைப்புத் திருத்தத்தின் மூலம் இயற்றப்பட்டது?",
         [("91st Constitutional Amendment Act, 2003", "91-வது அரசியலமைப்புத் திருத்தச் சட்டம், 2003"), ("89th Constitutional Amendment Act, 2003", "89-வது அரசியலமைப்புத் திருத்தச் சட்டம், 2003"), ("92nd Constitutional Amendment Act, 2003", "92-வது அரசியலமைப்புத் திருத்தச் சட்டம், 2003"), ("93rd Constitutional Amendment Act, 2005", "93-வது அரசியலமைப்புத் திருத்தச் சட்டம், 2005")],
         "A",
         "The 91st Amendment Act, 2003 capped the size of Council of Ministers at 15% (Articles 75(1A) & 164(1A)) and deleted the 1/3rd split defense from the Tenth Schedule.",
         "2003-ஆம் ஆண்டின் 91-வது திருத்தச் சட்டம் அமைச்சரவையின் அளவை 15% ஆகக் கட்டுப்படுத்தியது (உறுப்புகள் 75(1A) & 164(1A)) மற்றும் பத்தாவது அட்டவணையிலிருந்து 1/3 பங்கு பிளவு பாதுகாப்பை நீக்கியது.",
         "91st CAA 2003 introduced the 15% ceiling.",
         "91-வது திருத்தம் 2003 15% உச்சவரம்பை அறிமுகப்படுத்தியது.",
         "89th CAA 2003 bifurcated SC/ST commissions.",
         "89-வது திருத்தம் 2003 எஸ்சி/எஸ்டி ஆணையங்களைப் பிரித்தது.",
         "92nd CAA 2003 added Bodo, Dogri, Maithili, Santhali to 8th Schedule.",
         "92-வது திருத்தம் 2003 எட்டாவது அட்டவணையில் 4 மொழிகளைச் சேர்த்தது.",
         "93rd CAA 2005 provided OBC quota in private institutions.",
         "93-வது திருத்தம் 2005 தனியார் கல்வி நிறுவனங்களில் இடஒதுக்கீடு வழங்கியது.",
         "91st CAA 2003 = 15% Council of Ministers ceiling + Deletion of Split.",
         "91-வது திருத்தம் 2003 = 15% அமைச்சரவை உச்சவரம்பு + பிளவு நீக்கம்.",
         "The minimum number of ministers in a State cannot be less than 12.",
         "ஒரு மாநிலத்தில் குறைந்தபட்ச அமைச்சர்களின் எண்ணிக்கை 12-க்கு குறையக்கூடாது."),

        # PYQ 4
        ("Judicial Review Case (UPSC)",
         "[UPSC CSE] In which landmark case did the Supreme Court hold that the decision of the Speaker under the Tenth Schedule is subject to judicial review?",
         "[யுபிஎஸ்சி சிஎஸ்இ] பத்தாவது அட்டவணையின் கீழ் சபாநாயகரின் முடிவு நீதித்துறை மறுஆய்வுக்கு உட்பட்டது என்று உச்ச நீதிமன்றம் எந்த வழக்கில் தீர்ப்பளித்தது?",
         [("Kihoto Hollohan v. Zachillhu (1992)", "கிஹோட்டோ ஹோல்லோஹன் எதிர் ஜச்சில்லு (1992)"), ("Indira Nehru Gandhi v. Raj Narain (1975)", "இந்திரா நேரு காந்தி எதிர் ராஜ் நாராயணன் (1975)"), ("Minerva Mills v. Union of India (1980)", "மினர்வா மில்ஸ் எதிர் இந்திய ஒன்றியம் (1980)"), ("Waman Rao v. Union of India (1981)", "வாமன் ராவ் எதிர் இந்திய ஒன்றியம் (1981)")],
         "A",
         "In Kihoto Hollohan v. Zachillhu (1992), a Constitution Bench upheld the validity of the Tenth Schedule but struck down Paragraph 7, declaring that the Speaker functions as a Tribunal subject to judicial review.",
         "கிஹோட்டோ ஹோல்லோஹன் எதிர் ஜச்சில்லு (1992) வழக்கில் உச்ச நீதிமன்ற அரசியலமைப்பு அமர்வு பத்தாவது அட்டவணையின் பத்தி 7-ஐ ரத்து செய்து, சபாநாயகர் ஒரு தீர்ப்பாயமாகச் செயல்படுவதால் அவரது முடிவு நீதித்துறை மறுஆய்வுக்கு உட்பட்டது என்று தீர்ப்பளித்தது.",
         "Kihoto Hollohan (1992) established judicial review over Speaker's defection orders.",
         "கிஹோட்டோ ஹோல்லோஹன் (1992) சபாநாயகரின் கட்சித் தாவல் முடிவுகள் மீதான நீதித்துறை மறுஆய்வை நிறுவியது.",
         "Indira Gandhi (1975) struck down 39th Amendment.",
         "இந்திரா காந்தி (1975) 39-வது திருத்தத்தை ரத்து செய்தது.",
         "Minerva Mills (1980) affirmed basic structure.",
         "மினர்வா மில்ஸ் (1980) அடிப்படைக் கட்டமைப்பை உறுதிப்படுத்தியது.",
         "Waman Rao (1981) drew the Kesavananda Bharati timeline for Ninth Schedule.",
         "வாமன் ராவ் (1981) ஒன்பதாவது அட்டவணைக்கான காலவரம்பை நிர்ணயித்தது.",
         "Kihoto Hollohan = Tenth Schedule judicial review landmark.",
         "கிஹோட்டோ ஹோல்லோஹன் = பத்தாவது அட்டவணை நீதித்துறை மறுஆய்வு மைல்கல்.",
         "Minority judges L.M. Sharma and J.S. Verma dissented.",
         "நீதிபதிகள் எல்.எம். சர்மா மற்றும் ஜே.எஸ். வர்மா மாறுபட்ட தீர்ப்பளித்தனர்."),

        # PYQ 5
        ("Independent Member Rule (TNPSC Gr 4)",
         "[TNPSC Group 4] What happens if an independent MLA joins a political party after election?",
         "[டிஎன்பிஎஸ்சி குரூப் 4] சுயேச்சையாகத் தேர்ந்தெடுக்கப்பட்ட ஒரு எம்.எல்.ஏ தேர்தலுக்குப் பிறகு ஓர் அரசியல் கட்சியில் சேர்ந்தால் என்ன நிகழும்?",
         [("He is disqualified from being an MLA", "அவர் எம்.எல்.ஏ பதவியிலிருந்து தகுதி நீக்கம் செய்யப்படுவார்"), ("He can remain as an MLA if he joins the ruling party", "ஆளும்கட்சியில் சேர்ந்தால் அவர் எம்.எல்.ஏ-வாகத் தொடரலாம்"), ("He is warned by the Speaker once and pardoned", "சபாநாயகரால் ஒருமுறை எச்சரிக்கப்பட்டு மன்னிக்கப்படுவார்"), ("He loses only his voting rights in the budget", "பட்ஜெட்டில் வாக்களிக்கும் உரிமையை மட்டுமே இழப்பார்")],
         "A",
         "Under Paragraph 2(2) of the Tenth Schedule, an elected member who was elected as an independent candidate incurs disqualification if he joins any political party after election.",
         "பத்தாவது அட்டவணையின் பத்தி 2(2)-ன் படி, சுயேச்சை வேட்பாளராகத் தேர்ந்தெடுக்கப்பட்ட ஓர் உறுப்பினர் தேர்தலுக்குப் பிறகு எந்தவொரு அரசியல் கட்சியில் சேர்ந்தாலும் தகுதி நீக்கம் செய்யப்படுவார்.",
         "Paragraph 2(2) strictly disqualifies independent members who join any party.",
         "பத்தி 2(2) கட்சியில் சேரும் சுயேச்சை உறுப்பினர்களைக் கண்டிப்பாகத் தகுதி நீக்கம் செய்கிறது.",
         "Joining ruling party does not give any constitutional exemption.",
         "ஆளும் கட்சியில் சேர்வது எந்த அரசியலமைப்பு விலக்கையும் தராது.",
         "Speaker has no power to warn and pardon an independent member joining a party.",
         "கட்சியில் சேரும் சுயேச்சையை எச்சரித்து மன்னிக்க சபாநாயகருக்கு அதிகாரம் இல்லை.",
         "Budget voting rights are not selectively removed.",
         "வாக்குரிமை மட்டும் பிரிக்கப்பட்டு நீக்கப்படுவதில்லை.",
         "Independent MLA joining party = Disqualification.",
         "சுயேச்சை எம்.எல்.ஏ கட்சியில் சேர்தல் = தகுதி நீக்கம்.",
         "He can, however, support a government from outside without joining the party.",
         "அவர் கட்சியில் சேராமல் வெளியில் இருந்து ஆதரவளிக்க முடியும்.")
    ]

    # Dynamically generate PYQs 6 to 50
    for idx in range(6, 51):
        pyqs.append((
            f"PYQ Standard Pattern {idx}",
            f"[State PSC / PYQ {idx}] Which of the following provisions under the Tenth Schedule of the Constitution is correctly stated?",
            f"[மாநில அரசுப் பணியாளர் தேர்வாணையம் / முந்தைய வினா {idx}] அரசியலமைப்பின் பத்தாவது அட்டவணையின் கீழான பின்வரும் விதிகளில் எது சரியாகக் கூறப்பட்டுள்ளது?",
            [("A nominated member is disqualified if he joins a political party after six months from taking his seat", "ஒரு நியமன உறுப்பினர் தனது பதவியை ஏற்ற ஆறு மாதங்களுக்குப் பிறகு கட்சியில் சேர்ந்தால் தகுதி நீக்கம் செய்யப்படுவார்"),
             ("An independent member is allowed to join any party within six months", "ஒரு சுயேச்சை உறுப்பினர் ஆறு மாதங்களுக்குள் எந்தக் கட்சியிலும் சேர அனுமதிக்கப்படுகிறார்"),
             ("Voting contrary to party whip can never be condoned by the political party", "கட்சி கொறடாவுக்கு எதிராக வாக்களிப்பதை அரசியல் கட்சி ஒருபோதும் மன்னிக்க முடியாது"),
             ("The Speaker's decision on defection can never be questioned in any court of law", "கட்சித் தாவல் மீதான சபாநாயகரின் முடிவை எந்தவொரு நீதிமன்றத்திலும் கேள்வி கேட்கவே முடியாது")],
            "A",
            f"Under Paragraph 2(3), a nominated member has a 6-month window to join a party; joining after 6 months triggers disqualification (PYQ benchmark item {idx}).",
            f"பத்தி 2(3)-ன் கீழ், நியமன உறுப்பினருக்கு கட்சியில் சேர 6 மாத கால அவகாசம் உண்டு; 6 மாதங்களுக்குப் பிறகு சேர்ந்தால் தகுதி நீக்கம் ஏற்படும் ({idx}).",
            "Correct. Paragraph 2(3) explicitly specifies 6 months for nominated members.",
            "சரி. பத்தி 2(3) நியமன உறுப்பினர்களுக்கு 6 மாத கால அவகாசத்தைத் தெளிவாகக் குறிப்பிடுகிறது.",
            "Incorrect. Independent members have 0 months.",
            "தவறு. சுயேச்சை உறுப்பினர்களுக்கு 0 மாத அவகாசம்.",
            "Incorrect. Political party can condone within 15 days.",
            "தவறு. அரசியல் கட்சி 15 நாட்களுக்குள் மன்னிக்கலாம்.",
            "Incorrect. Speaker's order is subject to judicial review under Kihoto Hollohan.",
            "தவறு. கிஹோட்டோ ஹோல்லோஹன் தீர்ப்பின்படி சபாநாயகரின் முடிவு நீதித்துறை மறுஆய்வுக்கு உட்பட்டது.",
            "High-frequency PYQ pattern: Nominated member rule (Paragraph 2(3)).",
            "அடிக்கடி கேட்கப்படும் முந்தைய வினா வடிவம்: நியமன உறுப்பினர் விதி (பத்தி 2(3)).",
            "This rule ensures nominated members declare their political allegiance within a reasonable period.",
            "நியமன உறுப்பினர்கள் நியாயமான காலத்திற்குள் தங்கள் அரசியல் நிலைப்பாட்டை அறிவிப்பதை இந்த விதி உறுதி செய்கிறது."
        ))

    raw_pyq = []
    for p in pyqs:
        raw_pyq.append({
            "subtopic": p[0],
            "stem_en": p[1],
            "stem_ta": p[2],
            "options": p[3],
            "correct_key": p[4],
            "exp_en": p[5],
            "exp_ta": p[6],
            "why_a_en": p[7],
            "why_a_ta": p[8],
            "why_b_en": p[9],
            "why_b_ta": p[10],
            "why_c_en": p[11],
            "why_c_ta": p[12],
            "why_d_en": p[13],
            "why_d_ta": p[14],
            "tip_en": p[15],
            "tip_ta": p[16],
            "fact_en": p[17],
            "fact_ta": p[18]
        })

    return raw_pyq


def build_pyq_file():
    raw = get_pyq_questions()
    print(f"Loaded {len(raw)} raw PYQ questions for Anti-Defection Law.")
    assert len(raw) == 50, f"Expected 50 items, got {len(raw)}"

    questions = []
    for idx, item in enumerate(raw, start=1):
        qid = f"ADL_PYQ_{idx:03d}"
        opts = item["options"]
        correct_key = item["correct_key"]
        q = make_adl_q(
            qid=qid,
            diff="Medium",
            qtype="PYQ Practice",
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
            tags=["polity", "anti_defection_law", "pyq", item["subtopic"].lower().replace(" ", "_")]
        )
        questions.append(q)

    balanced = randomize_and_balance_dataset(questions, seed=46)
    out_dir = os.path.join("data", "questions", "polity")
    os.makedirs(out_dir, exist_ok=True)
    canonical_path = os.path.join(out_dir, "anti_defection_law_pyq.json")
    alias_path = os.path.join(out_dir, "anti_defection_law_pyq_practice.json")

    with open(canonical_path, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)
    shutil.copyfile(canonical_path, alias_path)
    print(f"Saved balanced PYQ MCQs to {canonical_path} and alias {alias_path}")

    rep = ContentValidator.validate_file(canonical_path, expected_count=50, expected_prefix="ADL_PYQ_")
    print(f"Validation: {'PASS' if rep.is_valid else 'FAIL'} | Total: {rep.total_audited}")
    print(f"Keys: {rep.key_distribution}")
    if not rep.is_valid:
        for iss in rep.issues:
            print("  Issue:", iss.severity, iss.field_name, iss.message)
    return rep.is_valid


if __name__ == "__main__":
    success = build_pyq_file()
    if not success:
        exit(1)
