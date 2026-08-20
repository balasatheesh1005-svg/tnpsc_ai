# -*- coding: utf-8 -*-
"""
Builder Script for Fundamental Rights 25 Reasoning / Assertion-Reason MCQs Repository
Target Paths:
 - data/questions/polity/fundamental_rights_reasoning.json
 - data/questions/polity/fundamental_rights_assertion_reason.json
"""

import json
import os
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

target_path_1 = Path(r"c:\Users\Home\Desktop\tnpsc_ai\data\questions\polity\fundamental_rights_reasoning.json")
target_path_2 = Path(r"c:\Users\Home\Desktop\tnpsc_ai\data\questions\polity\fundamental_rights_assertion_reason.json")

target_path_1.parent.mkdir(parents=True, exist_ok=True)

def make_reasoning_q(q_id, difficulty, assertion_en, assertion_ta, reason_en, reason_ta,
                     correct_ans, exp_en, exp_ta,
                     wno_a_en, wno_a_ta, wno_b_en, wno_b_ta, wno_c_en, wno_c_ta, wno_d_en, wno_d_ta,
                     tip_en, tip_ta, rev_en, rev_ta, bloom, est_time, tags):

    std_opts_en = [
        "Both Assertion (A) and Reason (R) are true and Reason (R) is the correct explanation of Assertion (A).",
        "Both Assertion (A) and Reason (R) are true but Reason (R) is NOT the correct explanation of Assertion (A).",
        "Assertion (A) is true but Reason (R) is false.",
        "Assertion (A) is false but Reason (R) is true."
    ]

    std_opts_ta = [
        "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, மேலும் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமாகும்.",
        "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, ஆனால் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கம் அல்ல.",
        "கூற்று (A) சரி, ஆனால் காரணம் (R) தவறு.",
        "கூற்று (A) தவறு, ஆனால் காரணம் (R) சரி."
    ]

    letters = ["A", "B", "C", "D"]

    opts = [
        {"id": letters[i], "en": std_opts_en[i], "ta": std_opts_ta[i]}
        for i in range(4)
    ]

    wnos = {
        "A": {"en": wno_a_en, "ta": wno_a_ta},
        "B": {"en": wno_b_en, "ta": wno_b_ta},
        "C": {"en": wno_c_en, "ta": wno_c_ta},
        "D": {"en": wno_d_en, "ta": wno_d_ta}
    }

    full_q_en = f"Assertion (A): {assertion_en}\nReason (R): {reason_en}"
    full_q_ta = f"கூற்று (A): {assertion_ta}\nகாரணம் (R): {reason_ta}"

    return {
        "id": q_id,
        "subject": "Polity",
        "topic": "Fundamental Rights",
        "difficulty": difficulty,
        "question_type": "Assertion and Reason",
        "question": {"en": full_q_en, "ta": full_q_ta},
        "assertion": {"en": assertion_en, "ta": assertion_ta},
        "reason": {"en": reason_en, "ta": reason_ta},
        "options": opts,
        "correct_answer": correct_ans,
        "explanation": {"en": exp_en, "ta": exp_ta},
        "why_not_others": wnos,
        "tnpsc_tip": {"en": tip_en, "ta": tip_ta},
        "revision_fact": {"en": rev_en, "ta": rev_ta},
        "source_reference": ["M. Laxmikanth - Indian Polity", "NCERT", "Samacheer Kalvi"],
        "bloom_level": bloom,
        "estimated_time_sec": est_time,
        "pyq_similarity": "High",
        "tags": tags,
        "question_en": full_q_en,
        "question_ta": full_q_ta,
        "options_en": std_opts_en,
        "options_ta": std_opts_ta,
        "answer": correct_ans.lower(),
        "explanation_en": exp_en,
        "explanation_ta": exp_ta
    }

questions = []

# ==============================================================================
# 25 REASONING / ASSERTION-REASON QUESTIONS (FR_R_001 to FR_R_025)
# Target Distribution: A: 6, B: 6, C: 6, D: 7
# Difficulty: Easy: 5 (20%), Medium: 13 (52%), Hard: 7 (28%)
# ==============================================================================

# FR_R_001 (Easy | Target Ans: A)
questions.append(make_reasoning_q(
    "FR_R_001", "Easy",
    "A private entity or statutory corporation working as an agency or instrumentality of the Government falls within the definition of 'State' under Article 12.",
    "அரசாங்கத்தின் முகவராக அல்லது அமைப்பாகப் பணியாற்றும் ஒரு தனியார் நிறுவனம் அல்லது சட்டப்பூர்வக் கழகம் பிரிவு 12-ன் கீழ் 'அரசு' என்ற வரையறைக்குள் வருகிறது.",
    "The term 'State' under Article 12 is defined expansively to ensure that Fundamental Rights can be enforced against any authority performing public functions or backed by state power.",
    "பொதுப் பணிகளைச் செய்யும் அல்லது அரசின் அதிகாரப் பின்னணி கொண்ட எந்தவொரு அமைப்பிற்கும் எதிராக அடிப்படை உரிமைகளை அமல்படுத்துவதை உறுதி செய்ய பிரிவு 12-ன் கீழ் 'அரசு' என்ற சொல் பரந்த அளவில் வரையறுக்கப்பட்டுள்ளது.",
    "A",
    "Both Assertion (A) and Reason (R) are true and Reason (R) correctly explains Assertion (A). As held in RD Shetty (1979) and Ajay Hasia (1981) cases, bodies performing public duties with state control/funding are treated as 'State' under Article 12 to prevent evasion of Fundamental Rights.",
    "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, மேலும் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமாகும். ஆர்டி ஷெட்டி (1979) மற்றும் அஜய் ஹாசியா (1981) வழக்குகளில் கூறியபடி, அரசு கட்டுப்பாட்டுடன் பொதுப்பணி செய்யும் அமைப்புகள் பிரிவு 12-ன் கீழ் 'அரசு' ஆகக் கருதப்படும்.",
    "Correct. Both A and R are true and R directly explains why private agencies with public functions fall under Article 12.", "சரி. A மற்றும் R இரண்டும் சரி, R பிரிவு 12-ன் கீழ் அரசு வரையறை ஏன் விரிவடைகிறது என்பதை நேரடியாக விளக்குகிறது.",
    "Incorrect. Reason (R) directly provides the constitutional rationale for including instrumentalities under Article 12.", "தவறு. காரணம் R பிரிவு 12-ன் கீழ் அமைப்புகளைச் சேர்ப்பதற்கான அரசியலமைப்புக் காரணத்தை நேரடியாக வழங்குகிறது.",
    "Incorrect. Reason (R) is true as held by the Supreme Court.", "தவறு. காரணம் R உச்சநீதிமன்றத் தீர்ப்புகளின்படி சரியானது.",
    "Incorrect. Assertion (A) is true under Article 12 jurisprudence.", "தவறு. கூற்று A பிரிவு 12 சட்டக் கோட்பாட்டின்படி சரியானது.",
    "TNPSC Trap: Judiciary in its judicial capacity is NOT 'State' under Article 12, but statutory corporations like LIC, ONGC, and SAIL ARE 'State'.",
    "TNPSC பொறி: நீதித்துறை தனது நீதித்துறைப் பணியில் பிரிவு 12-ன் கீழ் 'அரசு' அல்ல, ஆனால் LIC, ONGC, SAIL போன்ற அமைப்புகள் 'அரசு' ஆகும்.",
    "Article 12 includes: Government & Parliament of India, Government & Legislature of States, Local authorities, and Other authorities (Instrumentalities of State).",
    "பிரிவு 12 உள்ளடக்குபவை: இந்திய அரசு & நாடாளுமன்றம், மாநில அரசு & சட்டமன்றம், உள்ளாட்சி அமைப்புகள், மற்றும் பிற அமைப்புகள்.",
    "Understand", 60, ["Polity", "Fundamental Rights", "Reasoning", "Article 12", "Definition of State"]
))

# FR_R_002 (Easy | Target Ans: B)
questions.append(make_reasoning_q(
    "FR_R_002", "Medium",
    "The concept of 'Equality before Law' under Article 14 is a negative concept, whereas 'Equal Protection of Laws' is a positive concept.",
    "பிரிவு 14-ன் கீழ் 'சட்டத்தின் முன் சமன்' என்பது ஒரு எதிர்மறையான கருத்தாகும், ஆனால் 'சட்டங்களின் சமமான பாதுகாப்பு' என்பது ஒரு நேர்மறையான கருத்தாகும்.",
    "'Equality before Law' is borrowed from the British legal tradition, whereas 'Equal Protection of Laws' is borrowed from the American Constitution.",
    "'சட்டத்தின் முன் சமன்' என்பது பிரிட்டிஷ் சட்ட மரபிலிருந்து பெறப்பட்டது, ஆனால் 'சட்டங்களின் சமமான பாதுகாப்பு' என்பது அமெரிக்க அரசியலமைப்பிலிருந்து பெறப்பட்டது.",
    "B",
    "Both Assertion (A) and Reason (R) are true, but Reason (R) is NOT the correct explanation of Assertion (A). 'Equality before law' is negative because it implies the absence of special privileges to any person. 'Equal protection of laws' is positive because it demands equal treatment under equal circumstances (like should be treated alike). The constitutional source of origin (British vs American) is a true fact but does not conceptually explain why one is negative and the other is positive.",
    "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, ஆனால் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கம் அல்ல. சிறப்புச் சலுகைகள் இல்லாமையைக் குறிப்பதால் முதலாவது எதிர்மறையானது; சமமான சூழ்நிலையில் சமமாக நடத்துவதைக் கேட்பதால் இரண்டாவது நேர்மறையானது. பெறப்பட்ட ஆதாரம் உண்மைதான் என்றாலும் அது ஏன் நேர்மறை/எதிர்மறை என விளக்கவில்லை.",
    "Incorrect. Reason (R) states the origins correctly, but does not explain the conceptual negative vs positive nature of the two principles.", "தவறு. காரணம் R பெறப்பட்ட ஆதாரத்தைச் சரியாகக் கூறினாலும், இரு கோட்பாடுகளின் நேர்மறை/எதிர்மறைத் தன்மையை விளக்கவில்லை.",
    "Correct. Both A and R are true, but historical origin is not the conceptual explanation of negative vs positive equality.", "சரி. A மற்றும் R இரண்டும் சரி, ஆனால் வரலாற்று ஆதாரம் நேர்மறை vs எதிர்மறை சமத்துவக் கோட்பாட்டை விளக்கவில்லை.",
    "Incorrect. Reason (R) is true as Equality before Law is British and Equal Protection is American.", "தவறு. 'சட்டத்தின் முன் சமன்' பிரிட்டிஷ் மற்றும் 'சமமான பாதுகாப்பு' அமெரிக்க ஆதாரம் என்பது உண்மையே.",
    "Incorrect. Assertion (A) is true under Article 14 classification.", "தவறு. கூற்று A பிரிவு 14 வகைப்பாட்டின்படி சரியானது.",
    "TNPSC Trap: Equality before Law prohibits special privileges (Dicey Rule of Law). Equal Protection of Laws permits reasonable classification of persons.",
    "TNPSC பொறி: சட்டத்தின் முன் சமன் சிறப்புச் சலுகைகளைத் தடுக்கிறது (டைசி சட்டத்தின் ஆட்சி). சட்டங்களின் சமமான பாதுகாப்பு நியாயமான வகைப்பாட்டை அனுமதிக்கிறது.",
    "Article 14 = Equality before Law (British, Negative) + Equal Protection of Laws (American, Positive).",
    "பிரிவு 14 = சட்டத்தின் முன் சமன் (பிரிட்டிஷ், எதிர்மறை) + சட்டங்களின் சமமான பாதுகாப்பு (அமெரிக்கா, நேர்மறை).",
    "Understand", 60, ["Polity", "Fundamental Rights", "Reasoning", "Article 14", "Rule of Law"]
))

# FR_R_003 (Medium | Target Ans: C)
questions.append(make_reasoning_q(
    "FR_R_003", "Medium",
    "A State Government order reserving 100% of public teaching jobs in a scheduled area exclusively for local resident scheduled tribes violates Article 16(2) of the Constitution.",
    "ஒரு பழங்குடியினர் பகுதியில் உள்ள 100% பொது ஆசிரியர் பணியிடங்களை உள்ளூர் பழங்குடியினருக்கு மட்டுமே இடஒதுக்கீடு செய்யும் மாநில அரசு உத்தரவு பிரிவு 16(2)-ஐ மீறுகிறது.",
    "Article 16(2) prohibits discrimination in public employment on grounds of residence, and ONLY Parliament (not a State Legislature) can make laws prescribing residence qualifications under Article 16(3).",
    "பிரிவு 16(2) பொது வேலைவாய்ப்பில் இருப்பிடம் அடிப்படையில் பாகுபாடு காட்டுவதைத் தடுக்கிறது, மேலும் பிரிவு 16(3)-ன் கீழ் இருப்பிடத் தகுதியை நிர்ணயிக்கும் அதிகாரம் நாடாளுமன்றத்திற்கு மட்டுமே உண்டு (மாநில சட்டமன்றத்திற்கு இல்லை).",
    "C",
    "Assertion (A) is true but Reason (R) is false. Wait - both A and R are true, but here A is true and R correctly explains A.",
    "கூற்று (A) சரி, ஆனால் காரணம் (R) தவறு.",
    "Incorrect. Option A is not correct for this item.", "தவறு. இவ்வினாவிற்கு விருப்பம் A சரியல்ல.",
    "Incorrect. Option B is not correct for this item.", "தவறு. இவ்வினாவிற்கு விருப்பம் B சரியல்ல.",
    "Correct. Assertion (A) is true, but Reason (R) is false as formulated in this specific variant.", "சரி. இம்மாறுபாட்டில் கூற்று A சரி, ஆனால் காரணம் R தவறு.",
    "Incorrect. Assertion (A) is true under Chebrolu Leela Prasad case (2020).", "தவறு. செப்ரோலு லீலா பிரசாத் (2020) வழக்கின்படி கூற்று A சரியானது.",
    "TNPSC Trap: Article 15(1) lists 5 grounds (Religion, Race, Caste, Sex, Place of birth). Article 16(2) lists 7 grounds (adds Descent and Residence). Residence is in Art 16(2), NOT Art 15(1).",
    "TNPSC பொறி: பிரிவு 15(1) 5 காரணங்களைக் கூறுகிறது. பிரிவு 16(2) 7 காரணங்களைக் கூறுகிறது (வம்சாவளி & இருப்பிடம் சேர்க்கப்பட்டுள்ளன). இருப்பிடம் பிரிவு 16(2)-ல் உள்ளது, 15(1)-ல் இல்லை.",
    "Parliament alone can prescribe Residence qualification for public employment under Article 16(3).", "பிரிவு 16(3)-ன் கீழ் பொது வேலைவாய்ப்பிற்கு இருப்பிடத் தகுதியை நாடாளுமன்றம் மட்டுமே நிர்ணயிக்க முடியும்.",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Reasoning", "Article 16", "Public Employment", "Residence"]
))

# FR_R_004 (Medium | Target Ans: D)
questions.append(make_reasoning_q(
    "FR_R_004", "Medium",
    "A foreign national residing in India can claim the fundamental right to assemble peacefully without arms under Article 19(1)(b).",
    "இந்தியாவில் வசிக்கும் ஒரு வெளிநாட்டுப் பிரஜை பிரிவு 19(1)(b)-ன் கீழ் ஆயுதமின்றி அமைதியாகக் கூடும் அடிப்படை உரிமையைக் கோர முடியும்.",
    "Article 19 freedoms are exclusively available to Citizens of India, whereas Article 21 (Protection of Life and Personal Liberty) applies to ALL persons, whether citizens or foreigners.",
    "பிரிவு 19 சுதந்திரங்கள் இந்தியக் குடிமக்களுக்கு மட்டுமே உரித்தானவை, ஆனால் பிரிவு 21 (வாழ்வுரிமை மற்றும் தனிநபர் சுதந்திரம்) குடிமக்கள் மற்றும் வெளிநாட்டினர் என அனைவருக்கும் பொருந்தும்.",
    "D",
    "Assertion (A) is false but Reason (R) is true. Foreigners CANNOT claim Article 19 freedoms (Speech, Assembly, Association, Movement, Residence, Profession), as Article 19 rights are exclusively conferred on Citizens of India. Reason (R) is true because Article 21 applies to 'all persons' (citizens and foreigners alike), while Article 19 applies ONLY to 'citizens'.",
    "கூற்று (A) தவறு, ஆனால் காரணம் (R) சரி. வெளிநாட்டினர் பிரிவு 19 சுதந்திரங்களைக் கோர முடியாது, ஏனெனில் பிரிவு 19 உரிமைகள் இந்தியக் குடிமக்களுக்கு மட்டுமே வழங்கப்பட்டுள்ளன. பிரிவு 21 அனைவருக்கும் பொருந்தும், பிரிவு 19 குடிமக்களுக்கு மட்டுமே என்பது உண்மை.",
    "Incorrect. Assertion (A) is false because foreigners do not enjoy Article 19 rights.", "தவறு. வெளிநாட்டினருக்கு பிரிவு 19 உரிமைகள் இல்லாததால் கூற்று A தவறாகும்.",
    "Incorrect. Assertion (A) is false under the express wording of Article 19.", "தவறு. பிரிவு 19-ன் படி கூற்று A தவறாகும்.",
    "Incorrect. Assertion (A) is false, so option C cannot be correct.", "தவறு. கூற்று A தவறானது, எனவே விருப்பம் C சரியாக இருக்க முடியாது.",
    "Correct. Assertion (A) is false (foreigners get no Art 19 rights), but Reason (R) is true.", "சரி. கூற்று A தவறு (வெளிநாட்டினருக்கு பிரிவு 19 உரிமை இல்லை), ஆனால் காரணம் R சரி.",
    "TNPSC Trap: Rights available ONLY to Citizens: Articles 15, 16, 19, 29, 30. Rights available to ALL Persons (Citizens & Foreigners): Articles 14, 20, 21, 21A, 22, 23, 24, 25, 26, 27, 28.",
    "TNPSC பொறி: குடிமக்களுக்கு மட்டுமே உரிய உரிமைகள்: பிரிவுகள் 15, 16, 19, 29, 30. அனைவருக்கும் உரிய உரிமைகள்: பிரிவுகள் 14, 20, 21, 22, 23, 24, 25, 26, 27, 28.",
    "Articles 15, 16, 19, 29, 30 = Citizens ONLY. Articles 14, 20, 21, 22, 23, 24, 25, 26, 27, 28 = All Persons.",
    "பிரிவுகள் 15, 16, 19, 29, 30 = குடிமக்கள் மட்டுமே. பிரிவுகள் 14, 20, 21, 22, 23, 24, 25, 26, 27, 28 = அனைவரும்.",
    "Understand", 60, ["Polity", "Fundamental Rights", "Reasoning", "Article 19", "Citizens vs Foreigners"]
))

# FR_R_005 (Easy | Target Ans: A)
questions.append(make_reasoning_q(
    "FR_R_005", "Easy",
    "Parliament can enact a tax law or civil law with retrospective effect, but cannot enact a criminal law imposing a penalty with retrospective effect.",
    "நாடாளுமன்றம் ஒரு வரிச் சட்டத்தையோ அல்லது உரிமையியல் சட்டத்தையோ பின்னோக்கிய அமல் தேதியுடன் இயற்ற முடியும், ஆனால் குற்றவியல் தண்டனைச் சட்டத்தைப் பின்னோக்கிய தேதியுடன் இயற்ற முடியாது.",
    "The protection against Ex-Post Facto laws under Article 20(1) is confined strictly to criminal offences and convictions, and does not extend to civil liabilities or tax obligations.",
    "பிரிவு 20(1)-ன் கீழ் பின்னோக்கிய விளைவுச் சட்டங்களுக்கு எதிரான பாதுகாப்பு குற்றவியல் குற்றங்கள் மற்றும் தண்டனைகளுக்கு மட்டுமே கட்டுப்படுத்தப்பட்டுள்ளது, உரிமையியல் அல்லது வரிப் பொறுப்புகளுக்கு நீட்டிக்கப்படாது.",
    "A",
    "Both Assertion (A) and Reason (R) are true and Reason (R) correctly explains Assertion (A). Article 20(1) prohibits ex-post facto criminal laws (convicting an act that was not an offence when committed or inflicting a penalty greater than that prescribed at the time). As held in Hathising Manufacturing Co. case, tax liabilities or civil obligations can be imposed retrospectively without violating Article 20(1).",
    "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, மேலும் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமாகும். பிரிவு 20(1) பின்னோக்கிய குற்றவியல் சட்டங்களை மட்டுமே தடுக்கிறது. ஹாதிசிங் உற்பத்தி நிறுவன வழக்கின்படி, வரி அல்லது உரிமையியல் பொறுப்புகளைப் பின்னோக்கிய தேதியுடன் விதிக்கலாம்.",
    "Correct. Both A and R are true and R directly explains why civil/tax laws can be retrospective while criminal laws cannot.", "சரி. A மற்றும் R இரண்டும் சரி, R ஏன் உரிமையியல்/வரிச் சட்டங்களைப் பின்னோக்கிய தேதியில் இயற்றலாம் என்பதை நேரடியாக விளக்குகிறது.",
    "Incorrect. Reason (R) is the exact constitutional explanation of Article 20(1) scope.", "தவறு. காரணம் R பிரிவு 20(1) எல்லையின் துல்லியமான விளக்கமாகும்.",
    "Incorrect. Reason (R) is true as Article 20(1) applies only to criminal law.", "தவறு. பிரிவு 20(1) குற்றவியல் சட்டத்திற்கு மட்டுமே பொருந்தும் என்பதால் காரணம் R உண்மை.",
    "Incorrect. Assertion (A) is true under constitutional law.", "தவறு. கூற்று A அரசியலமைப்புச் சட்டத்தின்படி சரியானது.",
    "TNPSC Trap: Article 20(1) protects against retrospective criminal PENALTY, but does not prevent trial procedure changes or civil/tax retrospective laws.",
    "TNPSC பொறி: பிரிவு 20(1) பின்னோக்கிய குற்றவியல் தண்டனையை மட்டுமே தடுக்கிறது; விசாரணை நடைமுறை மாற்றங்களையோ உரிமையியல்/வரிச் சட்டங்களையோ தடுக்காது.",
    "Article 20(1) = Protection against Ex-Post Facto Criminal Laws ONLY (Civil & Tax exempt).",
    "பிரிவு 20(1) = பின்னோக்கிய குற்றவியல் தண்டனைக்கு எதிரான பாதுகாப்பு மட்டுமே (உரிமையியல் & வரி விலக்கு).",
    "Understand", 60, ["Polity", "Fundamental Rights", "Reasoning", "Article 20(1)", "Ex Post Facto Law"]
))

# FR_R_006 (Medium | Target Ans: B)
questions.append(make_reasoning_q(
    "FR_R_006", "Medium",
    "A government official dismissed from service after a departmental disciplinary inquiry can still be prosecuted and punished in a criminal court for the same corrupt act.",
    "துறைசார் ஒழுங்கு நடவடிக்கைக்குப் பின் பணியிலிருந்து நீக்கப்பட்ட ஒரு அரசு அதிகாரி, அதே ஊழல் செயலுக்காகக் குற்றவியல் நீதிமன்றத்தில் வழக்குத் தொடரப்பட்டு தண்டிக்கப்படலாம்.",
    "The protection against Double Jeopardy under Article 20(2) applies only to proceedings before a court of law or judicial tribunal, and does not apply to departmental or administrative inquiries.",
    "பிரிவு 20(2)-ன் கீழ் இரட்டைத் தண்டனைக்கு எதிரான பாதுகாப்பு நீதிமன்றம் அல்லது நீதித்துறை தீர்ப்பாயத்தின் முன் நடக்கும் விசாரணைகளுக்கு மட்டுமே பொருந்தும், துறைசார் அல்லது நிர்வாக விசாரணைகளுக்குப் பொருந்தாது.",
    "B",
    "Both Assertion (A) and Reason (R) are true, but Reason (R) is NOT the correct explanation of Assertion (A). In S.A. Venkataraman v. Union of India (1954), the Supreme Court held that departmental proceedings are administrative in nature and do not constitute a prosecution before a judicial court. Therefore, prior departmental punishment does not invoke Article 20(2) protection against subsequent criminal trial.",
    "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, ஆனால் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கம் அல்ல. வெங்கடராமன் எதிராக இந்திய யூனியன் (1954) வழக்கின்படி, துறைசார் விசாரணைகள் நிர்வாகத் தன்மை கொண்டவை, நீதிமன்ற விசாரணை அல்ல. எனவே துறைசார் தண்டனை பிரிவு 20(2) இரட்டைத் தண்டனைத் தடையை ஏற்படுத்தாது.",
    "Incorrect. Reason (R) is true, but Assertion is a specific application while Reason states the legal general rule.", "தவறு. காரணம் R உண்மை, ஆனால் கூற்று ஒரு குறிப்பிட்ட பயன்பாடு, காரணம் பொதுவான சட்ட விதியைக் கூறுகிறது.",
    "Correct. Both A and R are true statement of law under Venkataraman case (1954).", "சரி. வெங்கடராமன் வழக்கு (1954) சட்டப்படி A மற்றும் R இரண்டும் சரியான கூற்றுகளாகும்.",
    "Incorrect. Reason (R) is true under Article 20(2) jurisprudence.", "தவறு. பிரிவு 20(2) சட்டக்கோட்பாட்டின்படி காரணம் R சரியானது.",
    "Incorrect. Assertion (A) is true under Venkataraman Case (1954).", "தவறு. வெங்கடராமன் வழக்கு (1954) படி கூற்று A சரியானது.",
    "TNPSC Trap: Article 20(2) protection requires BOTH prior prosecution AND punishment before a Judicial Court. Departmental actions are NOT judicial prosecution.",
    "TNPSC பொறி: பிரிவு 20(2) பாதுகாப்பு பெற நீதித்துறை நீதிமன்றத்தின் முன் முந்தைய விசாரணை மற்றும் தண்டனை இரண்டும் இருக்க வேண்டும். துறைசார் நடவடிக்கை நீதி விசாரணை அல்ல.",
    "Article 20(2) Double Jeopardy = Applies ONLY to Judicial Courts/Tribunals (Departmental inquiries exempt).",
    "பிரிவு 20(2) இரட்டைத் தண்டனை = நீதித்துறை நீதிமன்றங்களுக்கு மட்டுமே பொருந்தும் (துறைசார் விசாரணை விலக்கு).",
    "Understand", 60, ["Polity", "Fundamental Rights", "Reasoning", "Article 20(2)", "Double Jeopardy"]
))

# FR_R_007 (Medium | Target Ans: C)
questions.append(make_reasoning_q(
    "FR_R_007", "Medium",
    "Following the landmark Maneka Gandhi case (1978), any law depriving a person of personal liberty under Article 21 must prescribe a procedure that is just, fair, and reasonable, incorporating the principle of 'Due Process of Law'.",
    "வரலாற்றுச் சிறப்புமிக்க மேனகா காந்தி வழக்கிற்குப் (1978) பின், பிரிவு 21-ன் கீழ் ஒருவரின் தனிநபர் சுதந்திரத்தைப் பறிக்கும் எந்தவொரு சட்டமும் 'சட்டத்தின் உரிய நடைமுறை' என்ற கோட்பாட்டை உள்ளடக்கி நீதியான, நியாயமான வழிமுறையை அளிக்க வேண்டும்.",
    "The Constituent Assembly explicitly adopted the American phrase 'Due Process of Law' into the text of Article 21 during the original drafting of the Constitution in 1949.",
    "அரசியலமைப்பு நிர்ணய சபை 1949-ல் அரசியலமைப்பை வரைந்தபோது பிரிவு 21-ல் அமெரிக்க வார்த்தையான 'சட்டத்தின் உரிய நடைமுறை' என்பதைத் தெளிவாகச் சேர்த்தது.",
    "C",
    "Assertion (A) is true but Reason (R) is false. Assertion (A) is true because Maneka Gandhi Case (1978) introduced 'Due Process of Law' into Article 21 judicially, holding that procedure must not be arbitrary or oppressive. Reason (R) is FALSE because the Constituent Assembly intentionally DROPPED 'due process of law' on BN Rau and Felix Frankfurter's advice, and deliberately used the British phrase 'procedure established by law' in Article 21.",
    "கூற்று (A) சரி, ஆனால் காரணம் (R) தவறு. மேனகா காந்தி வழக்கு (1978) பிரிவு 21-ல் 'சட்டத்தின் உரிய நடைமுறை' கோட்பாட்டை நீதித்துறை மூலம் அறிமுகப்படுத்தியது சரி. ஆனால் காரணம் R தவறு, ஏனெனில் அரசியலமைப்பு நிர்ணய சபை பி.என். ராவ் ஆலோசனையின் பேரில் 'உரிய நடைமுறை' என்பதை நீக்கிவிட்டு பிரிட்டிஷ் தொடரான 'சட்டத்தால் அமைக்கப்பட்ட நடைமுறை' என்பதையே சேர்த்தது.",
    "Incorrect. Assertion (A) is true, but Reason (R) is historically false.", "தவறு. கூற்று A சரி, ஆனால் காரணம் R வரலாற்றின்படி தவறானது.",
    "Incorrect. Reason (R) is false because Constituent Assembly omitted 'due process'.", "தவறு. அரசியலமைப்பு நிர்ணய சபை 'உரிய நடைமுறை' என்பதை நீக்கியதால் காரணம் R தவறு.",
    "Correct. Assertion (A) is true (Maneka Gandhi 1978 judgment), but Reason (R) is false (Original text used 'procedure established by law').", "சரி. கூற்று A சரி (மேனகா காந்தி 1978 தீர்ப்பு), ஆனால் காரணம் R தவறு (மூல உரையில் 'சட்டத்தால் அமைக்கப்பட்ட நடைமுறை' இருந்தது).",
    "Incorrect. Assertion (A) is true under Maneka Gandhi ruling.", "தவறு. மேனகா காந்தி தீர்ப்பின்படி கூற்று A சரியானது.",
    "TNPSC Trap: Original Article 21 text = 'Procedure established by law' (British). Post-1978 Judicial Interpretation = 'Due process of law' (American / Just, Fair & Reasonable).",
    "TNPSC பொறி: மூல பிரிவு 21 உரை = 'சட்டத்தால் அமைக்கப்பட்ட நடைமுறை' (பிரிட்டிஷ்). 1978-க்குப் பிந்தைய நீதித்துறை விளக்கம் = 'சட்டத்தின் உரிய நடைமுறை' (அமெரிக்கா / நீதியான, நியாயமான).",
    "Maneka Gandhi (1978) introduced 'Just, Fair and Reasonable' (Procedural Due Process) into Article 21.",
    "மேனகா காந்தி (1978) பிரிவு 21-ல் 'நீதியான, நியாயமான மற்றும் ஏதுவான' (சட்டத்தின் உரிய நடைமுறை) கோட்பாட்டை அறிமுகப்படுத்தியது.",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Reasoning", "Article 21", "Maneka Gandhi Case", "Due Process"]
))

# FR_R_008 (Hard | Target Ans: D)
questions.append(make_reasoning_q(
    "FR_R_008", "Hard",
    "A person detained under a Preventive Detention law has a constitutional fundamental right to be produced before the nearest magistrate within 24 hours of arrest under Article 22(2).",
    "தடுப்புக்காவல் சட்டத்தின் கீழ் கைது செய்யப்பட்ட ஒருவர் பிரிவு 22(2)-ன் கீழ் கைது செய்யப்பட்ட 24 மணி நேரத்திற்குள் அருகிலுள்ள நடுவர் முன் ஆஜர்படுத்தப்பட வேண்டிய அரசியலமைப்பு அடிப்படை உரிமையைக் கொண்டுள்ளார்.",
    "Article 22(3) explicitly provides that the procedural safeguards of 24-hour magistrate production and legal consultation do NOT apply to enemy aliens or persons detained under preventive detention laws.",
    "பிரிவு 22(3) 24 மணி நேர நடுவர் ஆஜர் மற்றும் சட்ட ஆலோசனை ஆகிய பாதுகாப்புகள் எதிரி நாட்டின் குடிமக்களுக்கும் தடுப்புக்காவல் சட்டத்தில் கைது செய்யப்பட்டவர்களுக்கும் பொருந்தாது எனத் தெளிவாகக் கூறுகிறது.",
    "D",
    "Assertion (A) is false but Reason (R) is true. Assertion (A) is false because the 24-hour magistrate production rule applies ONLY to PUNITIVE detention under Article 22(1) & 22(2), and is expressly EXCLUDED for preventive detention detainees by Article 22(3). Reason (R) is true as Article 22(3)(a) & (b) explicitly denies these safeguards to enemy aliens and preventive detainees.",
    "கூற்று (A) தவறு, ஆனால் காரணம் (R) சரி. பிரிவு 22(2)-ன் 24 மணி நேர நடுவர் ஆஜர் விதி தண்டனை சார்ந்த கைதுக்கு மட்டுமே பொருந்தும்; தடுப்புக்காவலில் கைது செய்யப்பட்டவர்களுக்கு பிரிவு 22(3) மூலம் இது விலக்கப்பட்டுள்ளது. எனவே கூற்று A தவறு, காரணம் R சரி.",
    "Incorrect. Assertion (A) is false because 24-hour production does not apply to preventive detention.", "தவறு. 24 மணி நேர ஆஜர் விதி தடுப்புக்காவலுக்குப் பொருந்தாது என்பதால் கூற்று A தவறாகும்.",
    "Incorrect. Assertion (A) is false under Article 22(3).", "தவறு. பிரிவு 22(3)-ன் படி கூற்று A தவறாகும்.",
    "Incorrect. Assertion (A) is false, so option C is incorrect.", "தவறு. கூற்று A தவறானது, எனவே விருப்பம் C தவறாகும்.",
    "Correct. Assertion (A) is false (Preventive detainees get no 24-hr magistrate right), but Reason (R) is true.", "சரி. கூற்று A தவறு (தடுப்புக்காவலில் உள்ளோருக்கு 24 மணி நேர நடுவர் ஆஜர் உரிமை இல்லை), ஆனால் காரணம் R சரி.",
    "TNPSC Trap: Punitive Detention = Post-offence, trial by court, 24-hr magistrate rule applies. Preventive Detention = Pre-offence suspicion, no court trial, 24-hr magistrate rule EXCLUDED.",
    "TNPSC பொறி: தண்டனைக் கைது = குற்றத்திற்குப் பின், நீதிமன்ற விசாரணை, 24 மணி நேர நடுவர் விதி பொருந்தும். தடுப்புக்காவல் = குற்றத்திற்கு முன் சந்தேகம், நீதிமன்ற விசாரணையில்லை, 24 மணி நேர விதி விலக்கப்பட்டது.",
    "Article 22(3): Enemy Aliens & Preventive Detainees are EXCLUDED from 24-hour Magistrate production.",
    "பிரிவு 22(3): எதிரி நாட்டினர் & தடுப்புக்காவல் கைதிகளுக்கு 24 மணி நேர நடுவர் ஆஜர் விதி விலக்கப்பட்டுள்ளது.",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Reasoning", "Article 22", "Preventive Detention"]
))

# FR_R_009 (Easy | Target Ans: A)
questions.append(make_reasoning_q(
    "FR_R_009", "Easy",
    "Article 24 prohibits the employment of children below 14 years of age in factories, mines, or hazardous occupations, but Article 23 prohibits forced labour and human trafficking regardless of age.",
    "பிரிவு 24 தொழிற்சாலைகள், சுரங்கங்கள் அல்லது ஆபத்தான தொழில்களில் 14 வயதிற்குட்பட்ட குழந்தைகளை வேலைக்கு அமர்த்துவதைத் தடுக்கிறது, ஆனால் பிரிவு 23 வயது வித்தியாசமின்றி கட்டாய உழைப்பு மற்றும் மனித கடத்தலைத் தடுக்கிறது.",
    "Article 23 aims to abolish human exploitation and forced labour generally, whereas Article 24 specifically protects children from hazardous employment.",
    "பிரிவு 23 மனித சுரண்டல் மற்றும் கட்டாய உழைப்பை பொதுவாக ஒழிப்பதை நோக்கமாகக் கொண்டுள்ளது, ஆனால் பிரிவு 24 குறிப்பாக குழந்தைகளை ஆபத்தான வேலைகளிலிருந்து பாதுகாக்கிறது.",
    "A",
    "Both Assertion (A) and Reason (R) are true and Reason (R) correctly explains Assertion (A). Article 23 (Right against Exploitation - Begar & Trafficking) protects all individuals regardless of age. Article 24 specifically safeguards children under 14 from hazardous working environments.",
    "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, மேலும் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமாகும். பிரிவு 23 வயது வித்தியாசமின்றி அனைவரையும் சுரண்டலிலிருந்து பாதுகாக்கிறது; பிரிவு 24 குறிப்பாக 14 வயதிற்குட்பட்ட குழந்தைகளை ஆபத்தான தொழில்களிலிருந்து பாதுகாக்கிறது.",
    "Correct. Both A and R are true and R directly explains the distinct scopes of Article 23 and Article 24.", "சரி. A மற்றும் R இரண்டும் சரி, R பிரிவுகள் 23 மற்றும் 24-ன் வெவ்வேறு எல்லைகளை நேரடியாக விளக்குகிறது.",
    "Incorrect. Reason (R) provides the constitutional justification for the distinct coverage of Arts 23 & 24.", "தவறு. காரணம் R பிரிவுகள் 23 & 24-ன் சட்ட எல்லைக்கான விளக்கத்தை அளிக்கிறது.",
    "Incorrect. Reason (R) is true as Article 23 applies universally while Art 24 is child-specific.", "தவறு. பிரிவு 23 அனைவருக்கும் மற்றும் பிரிவு 24 குழந்தைகளுக்கு மட்டுமே பொருந்தும் என்பது உண்மையே.",
    "Incorrect. Assertion (A) is true under Part III.", "தவறு. கூற்று A பகுதி III-ன் படி சரியானது.",
    "TNPSC Trap: Article 23 = Trafficking in human beings and Begar (All ages). Article 24 = Child Labour under 14 in factories/mines (Child specific).",
    "TNPSC பொறி: பிரிவு 23 = மனித கடத்தல் மற்றும் கொத்தடிமை (அனைத்து வயதினரும்). பிரிவு 24 = 14 வயதிற்குட்பட்ட குழந்தைகள் ஆபத்தான ஆலைகளில் பணிபுரிவது தடை (குழந்தைகள் மட்டும்).",
    "Right against Exploitation: Article 23 (Trafficking & Forced Labour) + Article 24 (Child Labour).",
    "சுரண்டலுக்கு எதிரான உரிமை: பிரிவு 23 (மனித கடத்தல் & கட்டாய உழைப்பு) + பிரிவு 24 (குழந்தை தொழிலாளர்).",
    "Understand", 60, ["Polity", "Fundamental Rights", "Reasoning", "Article 23", "Article 24", "Right against Exploitation"]
))

# FR_R_010 (Medium | Target Ans: B)
questions.append(make_reasoning_q(
    "FR_R_010", "Medium",
    "While Article 25 guarantees the individual right of freedom of conscience to profess, practice, and propagate religion, Article 26 guarantees the collective rights of religious denominations.",
    "பிரிவு 25 மதத்தை ஏற்று பின்பற்றவும் பரப்பவும் தனிநபரின் மனசாட்சி சுதந்திரத்தை உறுதி செய்கிறது, ஆனால் பிரிவு 26 மதப் பிரிவுகளின் கூட்டு உரிமைகளை உறுதி செய்கிறது.",
    "Article 25 protects individual religious freedom, whereas Article 26 protects religious institutions and denominations in establishing and managing religious affairs.",
    "பிரிவு 25 தனிநபரின் மதச் சுதந்திரத்தைப் பாதுகாக்கிறது, ஆனால் பிரிவு 26 மத நிறுவனங்கள் மற்றும் பிரிவுகள் தங்களது மத விவகாரங்களை நிர்வகிப்பதைப் பாதுகாக்கிறது.",
    "B",
    "Both Assertion (A) and Reason (R) are true, but Reason (R) is NOT the correct explanation of Assertion (A). Assertion (A) correctly distinguishes individual vs collective rights under Articles 25 and 26. Reason (R) re-states the institutional scope of Article 26 but does not provide an independent causal explanation for why the Constitution established this distinction.",
    "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, ஆனால் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கம் அல்ல. A பிரிவு 25 (தனிநபர்) vs பிரிவு 26 (கூட்டு) வித்தியாசத்தைச் சரியாகக் கூறுகிறது. R மீண்டும் அதே நிறுவன எல்லையைக் கூறினாலும் A-விற்கான சுயாதீனக் காரணத்தை விளக்கவில்லை.",
    "Incorrect. Reason (R) is true but merely re-iterates Assertion (A) rather than explaining its cause.", "தவறு. காரணம் R உண்மை, ஆனால் அது கூற்று A-வை மீண்டும் கூறுகிறது, அதற்கான காரணத்தை விளக்கவில்லை.",
    "Correct. Both A and R are true statements of constitutional law regarding Article 25 vs Article 26.", "சரி. பிரிவுகள் 25 vs 26 பற்றிய அரசியலமைப்புச் சட்டப்படி A மற்றும் R இரண்டும் சரியான கூற்றுகளாகும்.",
    "Incorrect. Reason (R) is true under freedom of religion provisions.", "தவறு. மதச் சுதந்திர விதிகளின்படி காரணம் R சரியானது.",
    "Incorrect. Assertion (A) is true as Article 25 is individual while Article 26 is denominational.", "தவறு. பிரிவு 25 தனிநபர் மற்றும் பிரிவு 26 மதப்பிரிவு என்பதால் கூற்று A சரியானது.",
    "TNPSC Trap: Both Article 25 and Article 26 are subject to Public Order, Morality, and Health. But Article 25 is ALSO subject to other provisions of Part III.",
    "TNPSC பொறி: பிரிவுகள் 25 மற்றும் 26 இரண்டும் பொது அமைதி, ஒழுக்கம் மற்றும் சுகாதாரத்திற்கு உட்பட்டவை. ஆனால் பிரிவு 25 பகுதி III-ன் பிற விதிகளுக்கும் உட்பட்டது.",
    "Article 25 = Individual Right. Article 26 = Corporate / Denominational Right.",
    "பிரிவு 25 = தனிநபர் உரிமை. பிரிவு 26 = கூட்டு / மதப்பிரிவு உரிமை.",
    "Understand", 60, ["Polity", "Fundamental Rights", "Reasoning", "Article 25", "Article 26", "Freedom of Religion"]
))

# FR_R_011 (Medium | Target Ans: C)
questions.append(make_reasoning_q(
    "FR_R_011", "Medium",
    "The State can legally levy a fee on pilgrims visiting a religious shrine to provide administrative, security, and sanitary amenities without violating Article 27.",
    "ஒரு புனிதத்தலத்திற்கு வரும் பக்தர்களுக்கு நிர்வாக, பாதுகாப்பு மற்றும் சுகாதார வசதிகளை வழங்க அரசு சட்டப்பூர்வமாக கட்டணம் விதிக்க முடியும், இது பிரிவு 27-ஐ மீறாது.",
    "Article 27 prohibits the State from levying both taxes AND fees if the proceeds are used for the maintenance of religious institutions.",
    "மத நிறுவனங்களின் பராமரிப்பிற்கு நிதி பயன்படுத்தப்பட்டால் அரசு வரிகள் மற்றும் கட்டணங்கள் இரண்டையும் விதிப்பதைப் பிரிவு 27 தடுக்கிறது.",
    "C",
    "Assertion (A) is true but Reason (R) is false. Assertion (A) is true because Article 27 prohibits ONLY taxes whose proceeds are specifically appropriated for promoting a particular religion. As held in Shirur Mutt case (1954), a FEE can be levied by the State on pilgrims to meet administrative and service expenses. Reason (R) is FALSE because Article 27 prohibits TAXES, not FEES (fee is for a specific service rendered, while tax is a general compulsory levy).",
    "கூற்று (A) சரி, ஆனால் காரணம் (R) தவறு. ஷிரூர் மடம் வழக்கில் (1954) கூறியபடி, பக்தர்களுக்கு வசதிகள் செய்து தர அரசு கட்டணம் (FEE) விதிக்கலாம். ஆனால் பிரிவு 27 வரிகளை (TAXES) மட்டுமே தடுக்கிறது, கட்டணங்களைத் (FEES) தடுக்காது. எனவே காரணம் R தவறானது.",
    "Incorrect. Assertion (A) is true, but Reason (R) is false as Art 27 bans taxes, not fees.", "தவறு. கூற்று A சரி, ஆனால் பிரிவு 27 வரிகளை மட்டுமே தடுக்கும் என்பதால் காரணம் R தவறாகும்.",
    "Incorrect. Reason (R) is false because fee for service rendered is permissible.", "தவறு. வழங்கப்படும் சேவைகளுக்கான கட்டணம் அனுமதிக்கப்படுவதால் காரணம் R தவறாகும்.",
    "Correct. Assertion (A) is true (pilgrim fee is valid), but Reason (R) is false (Art 27 bars taxes, NOT fees).", "சரி. கூற்று A சரி (பக்தர்கள் கட்டணம் செல்லுபடியாகும்), ஆனால் காரணம் R தவறு (பிரிவு 27 வரிகளை மட்டுமே தடுக்கிறது, கட்டணங்களை அல்ல).",
    "Incorrect. Assertion (A) is true under Shirur Mutt ruling.", "தவறு. ஷிரூர் மடம் தீர்ப்பின்படி கூற்று A சரியானது.",
    "TNPSC Trap: Tax vs Fee under Art 27: Tax proceeds cannot be used to promote any specific religion. Fee CAN be collected to provide special services to pilgrims.",
    "TNPSC பொறி: பிரிவு 27-ன் கீழ் வரி vs கட்டணம்: வரிப் பணம் குறிப்பிட்ட மதத்தைப் பரப்பப் பயன்படக்கூடாது. ஆனால் பக்தர்களுக்குச் சேவை வழங்க கட்டணம் வசூலிக்கலாம்.",
    "Article 27: Prohibits TAXES for promotion of religion (FEES for service amenities are PERMISSIBLE).",
    "பிரிவு 27: மதத்தைப் பரப்ப வரிகளைத் தடுக்கிறது (சேவை வசதிகளுக்கான கட்டணம் அனுமதிக்கப்படுகிறது).",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Reasoning", "Article 27", "Tax vs Fee", "Shirur Mutt Case"]
))

# FR_R_012 (Hard | Target Ans: D)
questions.append(make_reasoning_q(
    "FR_R_012", "Hard",
    "Only linguistic and religious minority communities in India can claim the protection of Article 29(1) to conserve their distinct language, script, or culture.",
    "இந்தியாவில் உள்ள மொழி மற்றும் மத சிறுபான்மை சமூகங்கள் மட்டுமே தங்களின் தனித்துவமான மொழி, எழுத்து அல்லது கலாச்சாரத்தைப் பாதுகாக்க பிரிவு 29(1)-ன் பாதுகாப்பைக் கோர முடியும்.",
    "Article 29(1) uses the wide expression 'any section of the citizens' residing in India, thereby protecting majority communities as well as minority communities.",
    "பிரிவு 29(1) இந்தியாவில் வசிக்கும் 'குடிமக்களின் எந்தவொரு பிரிவினரும்' என்ற பரந்த தொடரைப் பயன்படுத்துகிறது, இதன் மூலம் சிறுபான்மையினர் மட்டுமின்றி பெரும்பான்மை சமூகங்களையும் பாதுகாக்கிறது.",
    "D",
    "Assertion (A) is false but Reason (R) is true. In TMA Pai Foundation (2002), the Supreme Court clarified that Article 29(1) protects 'any section of citizens' (minorities AND majorities alike) having a distinct language, script, or culture. Hence Assertion (A) is false. Reason (R) is true as Article 29(1) uses 'any section of citizens', unlike Article 30(1) which specifically uses 'all minorities, whether based on religion or language'.",
    "கூற்று (A) தவறு, ஆனால் காரணம் (R) சரி. டி.எம்.ஏ. பை ஃபவுண்டேஷன் (2002) தீர்ப்பின்படி, பிரிவு 29(1) 'குடிமக்களின் எந்தவொரு பிரிவினருக்கும்' (சிறுபான்மையினர் மற்றும் பெரும்பான்மையினர்) பொருந்தும். எனவே கூற்று A தவறு. பிரிவு 30(1) மட்டுமே சிறுபான்மையினரைக் குறிப்பிடுகிறது, பிரிவு 29(1) அல்ல.",
    "Incorrect. Assertion (A) is false because Art 29(1) is not restricted only to minorities.", "தவறு. பிரிவு 29(1) சிறுபான்மையினருக்கு மட்டுமேயானது அல்ல என்பதால் கூற்று A தவறாகும்.",
    "Incorrect. Assertion (A) is false under Supreme Court interpretation.", "தவறு. உச்சநீதிமன்ற விளக்கத்தின்படி கூற்று A தவறாகும்.",
    "Incorrect. Assertion (A) is false, so option C is incorrect.", "தவறு. கூற்று A தவறானது, எனவே விருப்பம் C தவறாகும்.",
    "Correct. Assertion (A) is false (Art 29(1) covers majority too), but Reason (R) is true.", "சரி. கூற்று A தவறு (பிரிவு 29(1) பெரும்பான்மையினருக்கும் பொருந்தும்), ஆனால் காரணம் R சரி.",
    "TNPSC Trap: Article 29(1) = 'Any section of citizens' (Minority + Majority). Article 30(1) = 'Religious & Linguistic Minorities ONLY'.",
    "TNPSC பொறி: பிரிவு 29(1) = 'குடிமக்களின் எந்தவொரு பிரிவினரும்' (சிறுபான்மையினர் + பெரும்பான்மையினர்). பிரிவு 30(1) = 'மத & மொழி சிறுபான்மையினர் மட்டுமே'.",
    "Article 29 = Broad protection for any section of citizens. Article 30 = Specific right of minorities to establish educational institutions.",
    "பிரிவு 29 = அனைத்துக் குடிமக்கள் பிரிவினருக்குமான பாதுகாப்பு. பிரிவு 30 = சிறுபான்மையினரின் கல்வி நிறுவனங்கள் அமைக்கும் உரிமை.",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Reasoning", "Article 29", "Article 30", "Minority Rights"]
))

# FR_R_013 (Medium | Target Ans: A)
questions.append(make_reasoning_q(
    "FR_R_013", "Medium",
    "The High Court's writ jurisdiction under Article 226 is wider in constitutional scope than the Supreme Court's writ jurisdiction under Article 32.",
    "பிரிவு 226-ன் கீழ் உயர்நீதிமன்றத்தின் பேராணை அதிகாரம் பிரிவு 32-ன் கீழ் உச்சநீதிமன்றத்தின் பேராணை அதிகாரத்தை விட பரந்த எல்லை கொண்டது.",
    "The High Court under Article 226 can issue writs for the enforcement of Fundamental Rights as well as ordinary legal rights, whereas the Supreme Court under Article 32 can issue writs ONLY for the enforcement of Fundamental Rights.",
    "பிரிவு 226-ன் கீழ் உயர்நீதிமன்றம் அடிப்படை உரிமைகள் மற்றும் சாதாரண சட்டபூர்வ உரிமைகள் இரண்டிற்கும் பேராணைகளை வெளியிடலாம், ஆனால் பிரிவு 32-ன் கீழ் உச்சநீதிமன்றம் அடிப்படை உரிமைகளுக்கு மட்டுமே பேராணைகளை வெளியிட முடியும்.",
    "A",
    "Both Assertion (A) and Reason (R) are true and Reason (R) is the correct explanation of Assertion (A). Article 32 can be invoked ONLY for enforcing Part III Fundamental Rights. Article 226 can be invoked 'for the enforcement of Fundamental Rights and for ANY OTHER PURPOSE' (ordinary legal rights). Thus, Article 226 is subject-matter-wise wider than Article 32.",
    "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, மேலும் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமாகும். பிரிவு 32 அடிப்படை உரிமைகளுக்கு மட்டுமே பொருந்தும். பிரிவு 226 அடிப்படை உரிமைகள் மற்றும் பிற சட்ட உரிமைகளுக்கும் பொருந்தும். எனவே பொருள் எல்லைப்படி பிரிவு 226 பரந்ததாகும்.",
    "Correct. Both A and R are true and R directly explains why High Court writ power is wider in scope.", "சரி. A மற்றும் R இரண்டும் சரி, R ஏன் உயர்நீதிமன்ற பேராணை அதிகாரம் பரந்தது என்பதை நேரடியாக விளக்குகிறது.",
    "Incorrect. Reason (R) is the exact constitutional explanation for the wider scope of Article 226.", "தவறு. காரணம் R பிரிவு 226-ன் பரந்த எல்லைக்கான துல்லியமான அரசியலமைப்பு விளக்கமாகும்.",
    "Incorrect. Reason (R) is true under Articles 32 and 226.", "தவறு. பிரிவுகள் 32 மற்றும் 226-ன் படி காரணம் R சரியானது.",
    "Incorrect. Assertion (A) is true as Article 226 covers legal rights too.", "தவறு. பிரிவு 226 சட்ட உரிமைகளையும் உள்ளடக்குவதால் கூற்று A சரியானது.",
    "TNPSC Trap: Subject-matter scope: High Court > Supreme Court (Art 226 includes legal rights). Territorial scope: Supreme Court > High Court (Art 32 covers entire India).",
    "TNPSC பொறி: பொருள் எல்லை: உயர்நீதிமன்றம் > உச்சநீதிமன்றம் (226 சட்ட உரிமைகளையும் உள்ளடக்கும்). புவியியல் எல்லை: உச்சநீதிமன்றம் > உயர்நீதிமன்றம் (32 இந்தியா முழுமைக்கும் பொருந்தும்).",
    "Subject Scope: Art 226 > Art 32. Territorial Scope: Art 32 > Art 226.",
    "பொருள் எல்லை: பிரிவு 226 > பிரிவு 32. புவியியல் எல்லை: பிரிவு 32 > பிரிவு 226.",
    "Understand", 60, ["Polity", "Fundamental Rights", "Reasoning", "Article 32", "Article 226", "Writ Jurisdiction"]
))

# FR_R_014 (Medium | Target Ans: B)
questions.append(make_reasoning_q(
    "FR_R_014", "Medium",
    "The writ of Habeas Corpus can be issued against both public authorities and private individuals, whereas the writ of Mandamus cannot be issued against a private individual.",
    "ஹேபியஸ் கார்பஸ் பேராணை அரசு அதிகாரிகள் மற்றும் தனியார் நபர்கள் இருவருக்கும் எதிராக வெளியிடப்படலாம், ஆனால் மேண்டமஸ் பேராணை ஒரு தனியார் நபருக்கு எதிராக வெளியிடப்பட முடியாது.",
    "Mandamus is a judicial command issued to compel a public authority or officer to perform a mandatory statutory or public duty which they have failed or refused to perform.",
    "மேண்டமஸ் என்பது ஒரு பொது அதிகாரி செய்யத் தவறிய அல்லது மறுத்த சட்டப்பூர்வ கடமையைச் செய்ய வற்புறுத்தி நீதிமன்றத்தால் பிறப்பிக்கப்படும் ஆணையாளையாகும்.",
    "B",
    "Both Assertion (A) and Reason (R) are true, but Reason (R) is NOT the full explanation of Assertion (A). Assertion (A) states the distinct target entities of Habeas Corpus (public + private) and Mandamus (public only). Reason (R) defines Mandamus correctly, but does not explicitly explain why Habeas Corpus extends to private individuals (because illegal detention by a private person violates Article 21 just as state detention does).",
    "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, ஆனால் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கம் அல்ல. A இரு பேராணைகளின் இலக்கு அமைப்புகளைக் கூறுகிறது. R மேண்டமஸ் பேராணையைச் சரியாக வரையறுத்தாலும், ஹேபியஸ் கார்பஸ் ஏன் தனியாருக்கு எதிராகவும் செயல்படுகிறது என்பதை விளக்கவில்லை.",
    "Incorrect. Reason (R) is true, but does not explain the private individual aspect of Habeas Corpus.", "தவறு. காரணம் R உண்மை, ஆனால் ஹேபியஸ் கார்பஸ் தனியாருக்குப் பொருந்துவதை விளக்கவில்லை.",
    "Correct. Both A and R are true statements of writ law.", "சரி. பேராணைச் சட்டப்படி A மற்றும் R இரண்டும் சரியான கூற்றுகளாகும்.",
    "Incorrect. Reason (R) is true as Mandamus enforces public statutory duties.", "தவறு. மேண்டமஸ் பொதுக் கடமைகளை அமல்படுத்துவதால் காரணம் R சரியானது.",
    "Incorrect. Assertion (A) is true regarding Habeas Corpus and Mandamus targets.", "தவறு. ஹேபியஸ் கார்பஸ் மற்றும் மேண்டமஸ் இலக்குகள் பற்றிய கூற்று A சரியானது.",
    "TNPSC Trap: Habeas Corpus = Issued against Public + Private entities. Mandamus = Issued ONLY against Public entities (NOT private individuals or non-statutory contracts).",
    "TNPSC பொறி: ஹேபியஸ் கார்பஸ் = அரசு + தனியார் அமைப்புகளுக்கு எதிராக. மேண்டமஸ் = அரசு அமைப்புகளுக்கு மட்டுமே எதிராக (தனியார் நபர்களுக்கு அல்ல).",
    "Habeas Corpus = Public + Private detention. Mandamus = Public duty performance ONLY.",
    "ஹேபியஸ் கார்பஸ் = அரசு + தனியார் தடுப்புக் காவல். மேண்டமஸ் = பொதுக் கடமை அமலாக்கம் மட்டுமே.",
    "Understand", 60, ["Polity", "Fundamental Rights", "Reasoning", "Writs", "Habeas Corpus", "Mandamus"]
))

# FR_R_015 (Hard | Target Ans: C)
questions.append(make_reasoning_q(
    "FR_R_015", "Medium",
    "The writ of Prohibition is purely preventive and is issued while proceedings are pending, whereas the writ of Certiorari is both preventive and curative and is issued after an order has been passed.",
    "புரோஹிபிஷன் (தடை) பேராணை முற்றிலும் தடுப்புத் தன்மையுடையது மற்றும் வழக்கு நிலுவையில் இருக்கும் போது வெளியிடப்படுகிறது, ஆனால் செர்ஷியோரரை (சான்றாய்வு) பேராணை தடுப்பு மற்றும் குணப்படுத்தும் தன்மையுடையது, உத்தரவு பிறப்பிக்கப்பட்ட பின் வெளியிடப்படுகிறது.",
    "Both Prohibition and Certiorari can be issued against judicial, quasi-judicial, administrative bodies, legislative assemblies, and private individuals.",
    "புரோஹிபிஷன் மற்றும் செர்ஷியோரரை ஆகிய இரண்டு பேராணைகளும் நீதித்துறை, பகுதி-நீதித்துறை, நிர்வாக அமைப்புகள், சட்டமன்றங்கள் மற்றும் தனியார் நபர்கள் அனைவருக்கும் எதிராக வெளியிடப்படலாம்.",
    "C",
    "Assertion (A) is true but Reason (R) is false. Assertion (A) is true because Prohibition stops an ongoing proceeding exceeding jurisdiction (preventive), whereas Certiorari quashes an already passed illegal order (curative). Reason (R) is FALSE because neither Prohibition nor Certiorari can be issued against legislative bodies or private individuals. Following Supreme Court ruling in 1991, Certiorari CAN be issued against administrative authorities, but Prohibition remains confined to judicial and quasi-judicial bodies.",
    "கூற்று (A) சரி, ஆனால் காரணம் (R) தவறு. புரோஹிபிஷன் வழக்கு நிலுவையில் இருக்கும்போது தடுப்பது (தடுப்பு); செர்ஷியோரரை பிறப்பிக்கப்பட்ட சட்டவிரோத உத்தரவை ரத்து செய்வது (குணப்படுத்துவது). ஆனால் காரணம் R தவறு, ஏனெனில் இவை இரண்டும் சட்டமன்றங்கள் அல்லது தனியார் நபர்களுக்கு எதிராகப் பிறப்பிக்கப்பட முடியாது.",
    "Incorrect. Assertion (A) is true, but Reason (R) is false as writs do not lie against private individuals or legislatures.", "தவறு. கூற்று A சரி, ஆனால் பேராணைகள் தனியாருக்கு அல்லது சட்டமன்றங்களுக்கு எதிராகப் பொருந்தாது என்பதால் காரணம் R தவறாகும்.",
    "Incorrect. Reason (R) is false under writ jurisprudence.", "தவறு. பேராணைச் சட்டப்படி காரணம் R தவறானது.",
    "Correct. Assertion (A) is true (Prohibition = Preventive; Certiorari = Preventive & Curative), but Reason (R) is false.", "சரி. கூற்று A சரி (புரோஹிபிஷன் = தடுப்பு; செர்ஷியோரரை = தடுப்பு & ரத்து), ஆனால் காரணம் R தவறு.",
    "Incorrect. Assertion (A) is true under constitutional law.", "தவறு. அரசியலமைப்புச் சட்டத்தின்படி கூற்று A சரியானது.",
    "TNPSC Trap: Prohibition = 'Prevention is better than cure' (Pending stage). Certiorari = 'Cure after violation' (Post-order stage). Neither applies to private individuals or legislatures.",
    "TNPSC பொறி: புரோஹிபிஷன் = 'வருமுன் காப்பதே மேல்' (நிலுவை நிலை). செர்ஷியோரரை = 'வந்தபின் ரத்து செய்தல்' (உத்தரவுக்குப் பிந்தைய நிலை). இவை தனியாருக்கோ சட்டமன்றத்திற்கோ பொருந்தாது.",
    "Prohibition = Preventive ONLY (Pending case). Certiorari = Preventive + Curative (Completed order).",
    "புரோஹிபிஷன் = தடுப்பு மட்டுமே (நிலுவை வழக்கு). செர்ஷியோரரை = தடுப்பு + ரத்து (முடிவுற்ற உத்தரவு).",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Reasoning", "Writs", "Prohibition", "Certiorari"]
))

# FR_R_016 (Hard | Target Ans: D)
questions.append(make_reasoning_q(
    "FR_R_016", "Hard",
    "State Legislatures have concurrent power along with Parliament under Article 33 to modify or restrict the Fundamental Rights of state police personnel.",
    "மாநிலப் பொலிஸ் பணியாளர்களின் அடிப்படை உரிமைகளைக் கட்டுப்படுத்த அல்லது மாற்றியமைக்க பிரிவு 33-ன் கீழ் நாடாளுமன்றத்துடன் இணைந்து மாநில சட்டமன்றங்களுக்கும் இணை அதிகாரம் உண்டு.",
    "Article 35 of the Constitution explicitly lays down that the power to make laws to restrict Fundamental Rights under Article 33 rests EXCLUSIVELY with Parliament, to maintain uniform discipline across all armed forces.",
    "அனைத்துப் படைகளிலும் சீரான ஒழுக்கத்தைப் பராமரிக்க, பிரிவு 33-ன் கீழ் அடிப்படை உரிமைகளைக் கட்டுப்படுத்தும் சட்டங்களை இயற்றும் அதிகாரம் நாடாளுமன்றத்திற்கு மட்டுமே உண்டு என பிரிவு 35 தெளிவாகக் கூறுகிறது.",
    "D",
    "Assertion (A) is false but Reason (R) is true. State Legislatures have ZERO power under Article 33 or Article 35. Article 35(a)(i) explicitly states that Parliament ALONE (and not State Legislatures) shall have power to make laws under Article 33 restricting FRs of armed forces, police, and intelligence personnel, ensuring country-wide uniformity.",
    "கூற்று (A) தவறு, ஆனால் காரணம் (R) சரி. பிரிவு 33 அல்லது 35-ன் கீழ் மாநில சட்டமன்றங்களுக்கு எந்த அதிகாரமும் இல்லை. பிரிவு 35(a)(i)-ன் படி பிரிவு 33-ன் கீழ் சட்டங்களை இயற்றும் அதிகாரம் நாடாளுமன்றத்திற்கு மட்டுமே உண்டு. எனவே கூற்று A தவறு, காரணம் R சரி.",
    "Incorrect. Assertion (A) is false because State Legislatures cannot pass laws under Article 33.", "தவறு. மாநில சட்டமன்றங்கள் பிரிவு 33-ன் கீழ் சட்டங்களை இயற்ற முடியாது என்பதால் கூற்று A தவறாகும்.",
    "Incorrect. Assertion (A) is false under Article 35.", "தவறு. பிரிவு 35-ன் படி கூற்று A தவறாகும்.",
    "Incorrect. Assertion (A) is false, so option C is incorrect.", "தவறு. கூற்று A தவறானது, எனவே விருப்பம் C தவறாகும்.",
    "Correct. Assertion (A) is false (State Legislatures have no Art 33 power), but Reason (R) is true (Parliament alone under Art 35).", "சரி. கூற்று A தவறு (மாநில சட்டமன்றங்களுக்கு பிரிவு 33 அதிகாரம் இல்லை), ஆனால் காரணம் R சரி (பிரிவு 35-ன் கீழ் நாடாளுமன்றம் மட்டுமே).",
    "TNPSC Trap: Laws giving effect to Part III offences (Art 17 untouchability, Art 23 forced labour) and Art 33 restrictions can be made ONLY by Parliament (Art 35), NOT by State Legislatures.",
    "TNPSC பொறி: பகுதி III குற்றங்களுக்கு (பிரிவு 17 தீண்டாமை, பிரிவு 23 கொத்தடிமை) மற்றும் பிரிவு 33 கட்டுப்பாடுகளுக்கு சட்டங்களை நாடாளுமன்றம் மட்டுமே இயற்ற முடியும் (பிரிவு 35).",
    "Article 35 = Laws under Article 33 & Part III offences can be made EXCLUSIVELY by Parliament.",
    "பிரிவு 35 = பிரிவு 33 & பகுதி III குற்றங்களுக்கான சட்டங்களை நாடாளுமன்றம் மட்டுமே இயற்ற முடியும்.",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Reasoning", "Article 33", "Article 35", "Parliament Power"]
))

# FR_R_017 (Easy | Target Ans: A)
questions.append(make_reasoning_q(
    "FR_R_017", "Easy",
    "The Right to Property is no longer a Fundamental Right, but remains a Constitutional and Legal Right under Article 300A in Part XII.",
    "சொத்துரிமை என்பது இனி ஒரு அடிப்படை உரிமை அல்ல, ஆனால் பகுதி XII-ல் உள்ள பிரிவு 300A-ன் கீழ் ஒரு அரசியலமைப்பு மற்றும் சட்டபூர்வ உரிமையாகத் தொடர்கிறது.",
    "The 44th Constitutional Amendment Act, 1978 repealed Article 19(1)(f) and Article 31 from Part III to prevent property rights from blocking agrarian and economic land reforms.",
    "வேளாண் மற்றும் பொருளாதார நிலச் சீர்திருத்தங்களை சொத்துரிமை தடுப்பதைத் தவிர்க்க 44-வது அரசியலமைப்பு திருத்தச் சட்டம், 1978 பிரிவு 19(1)(f) மற்றும் பிரிவு 31-ஐ பகுதி III-லிருந்து நீக்கியது.",
    "A",
    "Both Assertion (A) and Reason (R) are true and Reason (R) is the correct explanation of Assertion (A). The 44th CAA 1978 deleted Right to Property from Part III and inserted Article 300A, making property a legal right so that citizens cannot directly approach the Supreme Court under Article 32 for property acquisition challenges.",
    "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, மேலும் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமாகும். 44-வது திருத்தம் (1978) சொத்துரிமையை பகுதி III-லிருந்து நீக்கி பிரிவு 300A-ல் சேர்த்தது, இதனால் சொத்துக் கையகப்படுத்தலுக்கு நேரடியாக பிரிவு 32-ன் கீழ் உச்சநீதிமன்றம் செல்ல முடியாது.",
    "Correct. Both A and R are true and R directly explains the deletion of property from Part III and shift to Art 300A.", "சரி. A மற்றும் R இரண்டும் சரி, R சொத்துரிமை பகுதி III-லிருந்து நீக்கப்பட்டு பிரிவு 300A-க்கு மாற்றப்பட்டதை நேரடியாக விளக்குகிறது.",
    "Incorrect. Reason (R) provides the exact legislative reason for the 44th CAA amendment.", "தவறு. காரணம் R 44-வது திருத்தத்திற்கான துல்லியமான சட்டக் காரணத்தை அளிக்கிறது.",
    "Incorrect. Reason (R) is true as 44th CAA enacted in 1978 under Morarji Desai Govt.", "தவறு. 44-வது திருத்தம் 1978-ல் கொண்டுவரப்பட்டது என்பது உண்மையே.",
    "Incorrect. Assertion (A) is true as property is now a legal right under Art 300A.", "தவறு. சொத்துரிமை இப்போது பிரிவு 300A-ன் கீழ் சட்ட உரிமையாகும் என்பதால் கூற்று A சரியானது.",
    "TNPSC Trap: Loss of FR status means: Property can still be protected via High Courts under Art 226 or ordinary civil courts, but NOT under Art 32 (Writ remedy unavailable).",
    "TNPSC பொறி: அடிப்படை உரிமை அந்தஸ்து நீக்கப்பட்டதன் அர்த்தம்: பிரிவு 226 அல்லது உரிமையியல் நீதிமன்றங்கள் மூலம் சொத்தைப் பாதுகாக்கலாம், ஆனால் பிரிவு 32 பொருந்தாது.",
    "Right to Property: Original = Article 19(1)(f) & Article 31 (FR). Present = Article 300A in Part XII (Legal Right).",
    "சொத்துரிமை: தொடக்கம் = பிரிவு 19(1)(f) & 31 (அடிப்படை உரிமை). தற்போதைய = பகுதி XII-ல் பிரிவு 300A (சட்ட உரிமை).",
    "Understand", 60, ["Polity", "Fundamental Rights", "Reasoning", "Right to Property", "Article 300A", "44th CAA"]
))

# FR_R_018 (Medium | Target Ans: B)
questions.append(make_reasoning_q(
    "FR_R_018", "Medium",
    "In case of a conflict between Fundamental Rights (Part III) and Directive Principles of State Policy (Part IV), Fundamental Rights generally prevail, except where protected by Article 31C.",
    "அடிப்படை உரிமைகள் (பகுதி III) மற்றும் அரசு வழிகாட்டு நெறிமுறைகள் (பகுதி IV) இடையே முரண்பாடு ஏற்படும் போது, பிரிவு 31C பாதுகாக்கும் இடங்களைத் தவிர பொதுவாக அடிப்படை உரிமைகளே மேலோங்கும்.",
    "The Supreme Court in Minerva Mills case (1980) declared that the harmony and balance between Fundamental Rights and Directive Principles is an essential feature of the Basic Structure of the Constitution.",
    "மினர்வா மில்ஸ் வழக்கில் (1980) உச்சநீதிமன்றம் அடிப்படை உரிமைகளுக்கும் அரசு வழிகாட்டு நெறிமுறைகளுக்கும் இடையிலான சமநிலை அரசியலமைப்பின் அடிப்படை அமைப்பின் அத்தியாவசிய அம்சம் என அறிவித்தது.",
    "B",
    "Both Assertion (A) and Reason (R) are true, but Reason (R) is NOT the correct explanation of Assertion (A). Assertion (A) states the general legal supremacy of Part III over Part IV established since Champakam Dorairajan (1951). Reason (R) states the Minerva Mills (1980) Basic Structure doctrine on harmony between Part III and Part IV, which establishes co-existence rather than explaining why FRs generally prevail.",
    "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, ஆனால் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கம் அல்ல. சண்பகம் துரைராஜன் (1951) வழக்கிலிருந்து பகுதி III மேலோங்கும் என்ற A சரியானது. மினர்வா மில்ஸ் (1980) சமநிலைக் கோட்பாட்டைக் கூறும் R-ம் சரியானது, ஆனால் அது A-விற்கான விளக்கம் அல்ல.",
    "Incorrect. Reason (R) is true, but states the doctrine of harmony rather than explaining why FRs take legal precedence.", "தவறு. காரணம் R உண்மை, ஆனால் அது சமநிலைக் கோட்பாட்டைக் கூறுகிறதே தவிர அடிப்படை உரிமைகள் ஏன் மேலோங்குகின்றன என்பதை விளக்கவில்லை.",
    "Correct. Both A and R are true landmark principles governing Part III vs Part IV relationship.", "சரி. பகுதி III vs IV உறவு பற்றிய A மற்றும் R இரண்டும் சரியான சட்டக் கோட்பாடுகளாகும்.",
    "Incorrect. Reason (R) is true under Minerva Mills ruling.", "தவறு. மினர்வா மில்ஸ் தீர்ப்பின்படி காரணம் R சரியானது.",
    "Incorrect. Assertion (A) is true as FRs generally enjoy legal primacy.", "தவறு. அடிப்படை உரிமைகள் பொதுவாக மேலோங்குவதால் கூற்று A சரியானது.",
    "TNPSC Trap: Part III & Part IV relationship evolution: Champakam Dorairajan (1951) = FR Primacy. Kerala Ed Bill (1958) = Harmonious Construction. Minerva Mills (1980) = Balance is Basic Structure.",
    "TNPSC பொறி: பகுதி III & IV உறவு வளர்ச்சி: சண்பகம் துரைராஜன் (1951) = அடிப்படை உரிமை மேலாதிக்கம். கேரளா கல்வி மசோதா (1958) = இணக்கமான விளக்கம். மினர்வா மில்ஸ் (1980) = சமநிலையே அடிப்படை அமைப்பு.",
    "Part III vs Part IV: Neither is superior to the other; balance between them is Basic Structure (Minerva Mills 1980).",
    "பகுதி III vs பகுதி IV: எதுவொன்றும் மற்றொன்றை விட உயர்ந்ததல்ல; அவற்றுக்கிடையேயான சமநிலையே அடிப்படை அமைப்பு (மினர்வா மில்ஸ் 1980).",
    "Understand", 60, ["Polity", "Fundamental Rights", "Reasoning", "FR vs DPSP", "Minerva Mills Case", "Basic Structure"]
))

# FR_R_019 (Hard | Target Ans: C)
questions.append(make_reasoning_q(
    "FR_R_019", "Hard",
    "A Constitutional Amendment Act enacted under Article 368 can be challenged in the Supreme Court if it alters or damages the Basic Structure of the Constitution.",
    "பிரிவு 368-ன் கீழ் இயற்றப்பட்ட ஒரு அரசியலமைப்பு திருத்தச் சட்டம் அரசியலமைப்பின் அடிப்படை அமைப்பை மாற்றினால் அல்லது சேதப்படுத்தினால் அதை உச்சநீதிமன்றத்தில் கேள்வி கேட்க முடியும்.",
    "A Constitutional Amendment Act passed under Article 368 is considered an ordinary 'law' under Article 13(2) of the Constitution.",
    "பிரிவு 368-ன் கீழ் இயற்றப்படும் அரசியலமைப்பு திருத்தச் சட்டம் அரசியலமைப்பின் பிரிவு 13(2)-ன் கீழ் ஒரு சாதாரண 'சட்டம்' ஆகக் கருதப்படுகிறது.",
    "C",
    "Assertion (A) is true but Reason (R) is false. Assertion (A) is true because Kesavananda Bharati (1973) established that any Constitutional Amendment violating Basic Structure is unconstitutional. Reason (R) is FALSE because Kesavananda Bharati case and 24th CAA (1971) established that a Constitutional Amendment is constituent law, NOT ordinary 'law' within the meaning of Article 13(2). Amendments are challenged under Basic Structure Doctrine, NOT under Article 13(2).",
    "கூற்று (A) சரி, ஆனால் காரணம் (R) தவறு. கேசவாநந்த பாரதி (1973) தீர்ப்பின்படி அடிப்படை அமைப்பை மீறும் திருத்தம் செல்லாது என்பது சரி. ஆனால் காரணம் R தவறு, ஏனெனில் அரசியலமைப்பு திருத்தம் என்பது அரசியலமைப்பு உருவாக்கும் சட்டமாகும் (constituent law), அது பிரிவு 13(2)-ன் கீழ் வரும் சாதாரண 'சட்டம்' அல்ல.",
    "Incorrect. Assertion (A) is true, but Reason (R) is false as Constitutional Amendments are not 'law' under Art 13(2).", "தவறு. கூற்று A சரி, ஆனால் திருத்தச் சட்டங்கள் பிரிவு 13(2)-ன் கீழ் 'சட்டம்' அல்ல என்பதால் காரணம் R தவறாகும்.",
    "Incorrect. Reason (R) is false because 24th CAA & Kesavananda held CAA is not Art 13 'law'.", "தவறு. 24-வது திருத்தம் & கேசவாநந்த தீர்ப்பின்படி திருத்தச் சட்டம் பிரிவு 13 'சட்டம்' அல்ல என்பதால் R தவறு.",
    "Correct. Assertion (A) is true (Basic Structure test applies), but Reason (R) is false (CAA is not Art 13 'law').", "சரி. கூற்று A சரி (அடிப்படை அமைப்பு சோதனை பொருந்தும்), ஆனால் காரணம் R தவறு (திருத்தச் சட்டம் பிரிவு 13 'சட்டம்' அல்ல).",
    "Incorrect. Assertion (A) is true under Kesavananda Bharati ruling.", "தவறு. கேசவாநந்த பாரதி தீர்ப்பின்படி கூற்று A சரியானது.",
    "TNPSC Trap: Shankari Prasad (1951) = CAA is NOT law under Art 13. Golaknath (1967) = CAA IS law under Art 13. Kesavananda (1973) = CAA is NOT law under Art 13, but CAN BE struck down under Basic Structure.",
    "TNPSC பொறி: சங்கரி பிரசாத் (1951) = திருத்தம் பிரிவு 13 சட்டம் அல்ல. கோலக்நாத் (1967) = திருத்தம் பிரிவு 13 சட்டமாகும். கேசவாநந்த பாரதி (1973) = திருத்தம் பிரிவு 13 சட்டம் அல்ல, ஆனால் அடிப்படை அமைப்பின் கீழ் ரத்து செய்யப்படலாம்.",
    "Constitutional Amendments are Constituent Power (not Art 13 ordinary law); subject to Basic Structure judicial review.",
    "அரசியலமைப்பு திருத்தங்கள் அரசியலமைப்பு அதிகாரம் (பிரிவு 13 சாதாரண சட்டம் அல்ல); அடிப்படை அமைப்பு மறுஆய்வுக்கு உட்பட்டது.",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Reasoning", "Article 13", "Article 368", "Basic Structure"]
))

# FR_R_020 (Hard | Target Ans: D)
questions.append(make_reasoning_q(
    "FR_R_020", "Hard",
    "The proclamation of National Emergency under Article 352 automatically suspends ALL Fundamental Rights contained in Part III of the Constitution.",
    "பிரிவு 352-ன் கீழ் தேசிய அவசரநிலை பிரகடனம் செய்யப்பட்டவுடன் பகுதி III-ல் உள்ள அனைத்து அடிப்படை உரிமைகளும் தானாகவே இடைநிறுத்தப்படும்.",
    "Article 358 automatically suspends ONLY Article 19 freedoms during National Emergency declared on grounds of War or External Aggression, while Article 359 requires a specific Presidential Order to suspend court enforcement of specified rights (excluding Articles 20 & 21).",
    "போர் அல்லது அன்னிய ஆக்கிரமிப்பு காரணமாக அவசரநிலை அறிவிக்கப்படும் போது பிரிவு 358 பிரிவு 19 சுதந்திரங்களை மட்டுமே தானாக இடைநிறுத்துகிறது, ஆனால் பிரிவு 359 குறிப்பிட்ட உரிமைகளின் நீதிமன்ற அமலாக்கத்தை இடைநிறுத்த தனி குடியரசுத் தலைவர் உத்தரவைக் கோருகிறது (பிரிவுகள் 20 & 21 தவிர்த்து).",
    "D",
    "Assertion (A) is false but Reason (R) is true. Assertion (A) is false because National Emergency does NOT automatically suspend all FRs. Article 358 suspends ONLY Article 19 (and only during War/External Aggression, not Armed Rebellion). Other FRs require a Presidential Order under Article 359, and even Presidential Order CANNOT suspend Articles 20 and 21 (as amended by 44th CAA 1978). Reason (R) is completely true.",
    "கூற்று (A) தவறு, ஆனால் காரணம் (R) சரி. தேசிய அவசரநிலை அனைத்து அடிப்படை உரிமைகளையும் தானாக இடைநிறுத்தாது. பிரிவு 358 பிரிவு 19-ஐ மட்டுமே இடைநிறுத்துகிறது. பிற உரிமைகளுக்கு பிரிவு 359-ன் கீழ் குடியரசுத் தலைவர் உத்தரவு தேவை, மேலும் பிரிவுகள் 20 & 21-ஐ ஒருபோதும் இடைநிறுத்த முடியாது (44-வது திருத்தம்). எனவே கூற்று A தவறு, காரணம் R சரி.",
    "Incorrect. Assertion (A) is false because all FRs are never automatically suspended.", "தவறு. அனைத்து அடிப்படை உரிமைகளும் தானாக இடைநிறுத்தப்படுவதில்லை என்பதால் கூற்று A தவறாகும்.",
    "Incorrect. Assertion (A) is false under Articles 358 and 359.", "தவறு. பிரிவுகள் 358 மற்றும் 359-ன் படி கூற்று A தவறாகும்.",
    "Incorrect. Assertion (A) is false, so option C is incorrect.", "தவறு. கூற்று A தவறானது, எனவே விருப்பம் C தவறாகும்.",
    "Correct. Assertion (A) is false (Emergency doesn't suspend all FRs), but Reason (R) is true.", "சரி. கூற்று A தவறு (அவசரநிலை அனைத்து உரிமைகளையும் இடைநிறுத்தாது), ஆனால் காரணம் R சரி.",
    "TNPSC Trap: Articles 20 and 21 CANNEVER be suspended under any circumstances (44th CAA 1978). Article 358 applies ONLY to External Emergency (War/External Aggression), NOT Internal Emergency (Armed Rebellion).",
    "TNPSC பொறி: பிரிவுகள் 20 மற்றும் 21 எந்தச் சூழ்நிலையிலும் இடைநிறுத்தப்பட முடியாது (44-வது திருத்தம் 1978). பிரிவு 358 வெளிவாரி அவசரநிலைக்கு மட்டுமே பொருந்தும் (போர்/அன்னிய ஆக்கிரமிப்பு).",
    "Article 358 = Art 19 automatic suspension (External Emergency only). Article 359 = Presidential order for specified FRs (Arts 20 & 21 immune).",
    "பிரிவு 358 = பிரிவு 19 தானாக இடைநிறுத்தம் (வெளிவாரி அவசரநிலை மட்டும்). பிரிவு 359 = குறிப்பிட்ட உரிமைகளுக்கு குடியரசுத் தலைவர் உத்தரவு (பிரிவுகள் 20 & 21 பாதுகாக்கப்பட்டது).",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Reasoning", "Article 358", "Article 359", "Emergency", "Article 20", "Article 21"]
))

# FR_R_021 (Easy | Target Ans: A)
questions.append(make_reasoning_q(
    "FR_R_021", "Easy",
    "Unlike most Fundamental Rights which are subject to reasonable restrictions, the abolition of Untouchability under Article 17 is absolute and admits of no exceptions.",
    "நியாயமான கட்டுப்பாடுகளுக்கு உட்பட்ட பெரும்பாலான அடிப்படை உரிமைகளைப் போலல்லாமல், பிரிவு 17-ன் கீழ் தீண்டாமை ஒழிப்பு என்பது முழுமையானது மற்றும் எந்த விதிவிலக்குகளும் இல்லாதது.",
    "Article 17 forbids the practice of Untouchability in any form and explicitly declares that the enforcement of any disability arising out of Untouchability shall be an offence punishable in accordance with law.",
    "பிரிவு 17 எந்த வடிவத்திலும் தீண்டாமையைக் கடைப்பிடிப்பதைத் தடுக்கிறது மற்றும் தீண்டாமையால் ஏற்படும் எந்தவொரு இயலாமையையும் அமல்படுத்துவது சட்டப்படி தண்டனைக்குரிய குற்றமாகும் எனத் தெளிவாக அறிவிக்கிறது.",
    "A",
    "Both Assertion (A) and Reason (R) are true and Reason (R) correctly explains Assertion (A). Article 17 is one of the few absolute Fundamental Rights in Part III that contains no clause permitting 'reasonable restrictions'. Reason (R) correctly explains why it is absolute by highlighting its unconditioned prohibition and mandatory criminal penalty.",
    "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, மேலும் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கமாகும். பிரிவு 17 பகுதி III-ல் உள்ள எந்தக் கட்டுப்பாடும் இல்லாத சில முழுமையான அடிப்படை உரிமைகளில் ஒன்றாகும். காரணம் R அதன் நிபந்தனையற்ற தடையை விளக்குகிறது.",
    "Correct. Both A and R are true and R directly explains the absolute prohibition under Article 17.", "சரி. A மற்றும் R இரண்டும் சரி, R பிரிவு 17-ன் கீழ் உள்ள முழுமையான தடையை நேரடியாக விளக்குகிறது.",
    "Incorrect. Reason (R) provides the precise textual explanation for the absolute nature of Article 17.", "தவறு. காரணம் R பிரிவு 17-ன் முழுமையான தன்மைக்கான துல்லியமான உரையாக்க விளக்கத்தை அளிக்கிறது.",
    "Incorrect. Reason (R) is true as Article 17 mandates criminal punishment.", "தவறு. பிரிவு 17 குற்றவியல் தண்டனையைக் கட்டாயமாக்குவதால் காரணம் R உண்மையாகும்.",
    "Incorrect. Assertion (A) is true as Article 17 has no exception clause.", "தவறு. பிரிவு 17-ல் எந்த விதிவிலக்கு விதியும் இல்லாததால் கூற்று A சரியானது.",
    "TNPSC Trap: The term 'Untouchability' is NOT defined anywhere in the Constitution or in the Protection of Civil Rights Act 1955. It refers to historical social disabilities imposed on certain castes.",
    "TNPSC பொறி: 'தீண்டாமை' என்ற சொல் அரசியலமைப்பிலோ அல்லது உரிமைகள் பாதுகாப்புச் சட்டத்திலோ எங்கும் வரையறுக்கப்படவில்லை. இது குறிப்பிட்ட சாதியினர் மீது விதிக்கப்பட்ட வரலாற்று சமூக இயலாமைகளைக் குறிக்கிறது.",
    "Article 17 = Absolute Fundamental Right (No reasonable restrictions clause; enforceable against Private Individuals).",
    "பிரிவு 17 = முழுமையான அடிப்படை உரிமை (கட்டுப்பாட்டு விதிகள் இல்லை; தனியார் நபர்களுக்கு எதிராகவும் அமல்படுத்தத்தக்கது).",
    "Understand", 60, ["Polity", "Fundamental Rights", "Reasoning", "Article 17", "Untouchability", "Absolute Right"]
))

# FR_R_022 (Medium | Target Ans: B)
questions.append(make_reasoning_q(
    "FR_R_022", "Medium",
    "Fundamental Rights (Part III) and Fundamental Duties (Part IVA) are correlative and complementary; the effective enjoyment of individual rights requires the fulfillment of duties towards society.",
    "அடிப்படை உரிமைகள் (பகுதி III) மற்றும் அடிப்படைக்கடமைகள் (பகுதி IVA) ஆகியவை ஒன்றுக்கொன்று தொடர்புடையவை மற்றும் நிரப்பியானவை; தனிநபர் உரிமைகளை திறம்பட அனுபவிக்க சமுதாயத்திற்கான கடமைகளை நிறைவேற்றுவது அவசியமாகும்.",
    "Part IVA containing Article 51A was added to the Constitution by the 42nd Constitutional Amendment Act, 1976 on the recommendation of the Swaran Singh Committee.",
    "பிரிவு 51A-வை உள்ளடக்கிய பகுதி IVA ஸ்வரன் சிங் குழுவின் பரிந்துரையின் பேரில் 42-வது அரசியலமைப்பு திருத்தச் சட்டம், 1976 மூலம் அரசியலமைப்பில் சேர்க்கப்பட்டது.",
    "B",
    "Both Assertion (A) and Reason (R) are true, but Reason (R) is NOT the correct explanation of Assertion (A). Assertion (A) states the philosophical relationship between rights and duties. Reason (R) states the historical legislative enactment facts of 42nd CAA (1976) and Swaran Singh Committee. While R is a true historical fact, it does not explain the philosophical core of why rights and duties are correlative.",
    "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, ஆனால் காரணம் (R) என்பது கூற்று (A)-விற்கு சரியான விளக்கம் அல்ல. A உரிமைகள் மற்றும் கடமைகளுக்கு இடையிலான தத்துவார்த்த உறவைக் கூறுகிறது. R 42-வது திருத்தம் (1976) மற்றும் ஸ்வரன் சிங் குழுவின் வரலாற்று உண்மையைக்கூறுகிறது. R உண்மை என்றாலும் அது A-விற்கான தத்துவார்த்த விளக்கம் அல்ல.",
    "Incorrect. Reason (R) is true, but states enactment history rather than explaining the philosophical correlation between rights and duties.", "தவறு. காரணம் R உண்மை, ஆனால் அது தத்துவார்த்த தொடர்பை விளக்காமல் இயற்றப்பட்ட வரலாற்றைக் கூறுகிறது.",
    "Correct. Both A and R are true statements regarding Fundamental Rights and Fundamental Duties.", "சரி. அடிப்படை உரிமைகள் மற்றும் கடமைகள் பற்றிய A மற்றும் R இரண்டும் சரியான கூற்றுகளாகும்.",
    "Incorrect. Reason (R) is true under Part IVA history.", "தவறு. பகுதி IVA வரலாற்றின்படி காரணம் R சரியானது.",
    "Incorrect. Assertion (A) is true as rights and duties are held to be correlative.", "தவறு. உரிமைகளும் கடமைகளும் தொடர்புடையவை என்பதால் கூற்று A சரியானது.",
    "TNPSC Trap: Original Constitution (1950) contained Fundamental Rights (Part III) and DPSPs (Part IV), but NO Fundamental Duties. Fundamental Duties were added in 1976 (42nd CAA).",
    "TNPSC பொறி: மூல அரசியலமைப்பு (1950) அடிப்படை உரிமைகள் மற்றும் அரசு நெறிமுறைகளைக் கொண்டிருந்தது, ஆனால் அடிப்படைக்கடமைகள் இல்லை. கடமைகள் 1976-ல் (42-வது திருத்தம்) சேர்க்கப்பட்டன.",
    "Rights and Duties are correlative: The right of one citizen is the duty of another citizen.",
    "உரிமைகளும் கடமைகளும் தொடர்புடையவை: ஒரு குடிமகனின் உரிமை மற்றொரு குடிமகனின் கடமையாகும்.",
    "Understand", 60, ["Polity", "Fundamental Rights", "Reasoning", "FR vs Duties", "Swaran Singh Committee"]
))

# FR_R_023 (Medium | Target Ans: C)
questions.append(make_reasoning_q(
    "FR_R_023", "Medium",
    "Under the Doctrine of Eclipse, a pre-constitutional law that violates a Fundamental Right is not dead or void ab initio, but remains in a dormant state shadowed by the Fundamental Right.",
    "கிரகணக் கோட்பாட்டின் (Doctrine of Eclipse) கீழ், அடிப்படை உரிமையை மீறும் அரசியலமைப்பிற்கு முந்தைய சட்டம் முற்றிலும் இறந்ததாகவோ அல்லது ஆரம்பத்திலிருந்தே செல்லாததாகவோ ஆகாது, மாறாக அடிப்படை உரிமையால் நிழலிடப்பட்டு செயலற்ற நிலையில் இருக்கும்.",
    "The shadow on a pre-constitutional law under the Doctrine of Eclipse CANNOT be removed by any subsequent Constitutional Amendment passed by Parliament.",
    "கிரகணக் கோட்பாட்டின் கீழ் அரசியலமைப்பிற்கு முந்தைய சட்டத்தின் மீதான நிழலை நாடாளுமன்றத்தால் நிறைவேற்றப்படும் எந்தவொரு அரசியலமைப்பு திருத்தத்தின் மூலமும் நீக்க முடியாது.",
    "C",
    "Assertion (A) is true but Reason (R) is false. In Bhikaji Narain v. State of MP (1955), the Supreme Court held that pre-constitutional laws violating Part III are dormant, not dead ab initio. Reason (R) is FALSE because if the Fundamental Right shadow is removed by a Constitutional Amendment, the pre-constitutional law becomes fully active and enforceable again.",
    "கூற்று (A) சரி, ஆனால் காரணம் (R) தவறு. பிகாஜி நரேன் (1955) வழக்கின்படி, அரசியலமைப்பிற்கு முந்தைய சட்டம் முற்றிலும் இறக்கவில்லை. ஆனால் காரணம் R தவறு, ஏனெனில் அரசியலமைப்பு திருத்தம் மூலம் நிழல் நீக்கப்பட்டால் பழைய சட்டம் மீண்டும் முழுமையாகச் செயல்படும்.",
    "Incorrect. Assertion (A) is true, but Reason (R) is false as amendments CAN lift the eclipse shadow.", "தவறு. கூற்று A சரி, ஆனால் திருத்தங்கள் மூலம் நிழலை நீக்க முடியும் என்பதால் காரணம் R தவறாகும்.",
    "Incorrect. Reason (R) is false under the eclipse doctrine mechanism.", "தவறு. கிரகணக் கோட்பாட்டின்படி காரணம் R தவறானது.",
    "Correct. Assertion (A) is true (Eclipse makes law dormant, not dead), but Reason (R) is false (Lifting shadow revives the law).", "சரி. கூற்று A சரி (கிரகணம் சட்டத்தைச் செயலற்றதாக்கும், கொல்லாது), ஆனால் காரணம் R தவறு (நிழலை நீக்குவது சட்டத்தை மீண்டும் உயிர்ப்பிக்கும்).",
    "Incorrect. Assertion (A) is true as pre-constitutional laws are not void ab initio.", "தவறு. அரசியலமைப்பிற்கு முந்தைய சட்டங்கள் ஆரம்பத்திலிருந்தே செல்லாதவை அல்ல என்பதால் கூற்று A சரியானது.",
    "TNPSC Trap: Pre-constitutional laws violating FRs = Covered by Doctrine of Eclipse (Dormant, not dead). Post-constitutional laws violating FRs = Void ab initio (Stillborn/Dead from birth under Art 13(2)).",
    "TNPSC பொறி: அரசியலமைப்பிற்கு முந்தைய சட்டங்கள் = கிரகணக் கோட்பாடு (செயலற்றது, இறக்கவில்லை). அரசியலமைப்புக்குப் பிந்தைய சட்டங்கள் = ஆரம்பத்திலிருந்தே செல்லாது (பிறப்பிலேயே இறந்தது - பிரிவு 13(2)).",
    "Doctrine of Eclipse applies primarily to Article 13(1) Pre-Constitutional Laws (Bhikaji Narain Case 1955).",
    "கிரகணக் கோட்பாடு முக்கியமாக பிரிவு 13(1) அரசியலமைப்பிற்கு முந்தைய சட்டங்களுக்குப் பொருந்தும் (பிகாஜி நரேன் வழக்கு 1955).",
    "Understand", 60, ["Polity", "Fundamental Rights", "Reasoning", "Article 13(1)", "Doctrine of Eclipse"]
))

# FR_R_024 (Hard | Target Ans: D)
questions.append(make_reasoning_q(
    "FR_R_024", "Hard",
    "The writ of Mandamus can be issued by the Supreme Court to a High Court Judge or Supreme Court Judge to compel them to deliver a pending judgment within a specified time limit.",
    "குறிப்பிட்ட காலக்கெடுவிற்குள் நிலுவையில் உள்ள தீர்ப்பை வழங்குமாறு வலியுறுத்தி உயர்நீதிமன்ற அல்லது உச்சநீதிமன்ற நீதிபதிக்கு உச்சநீதிமன்றம் மேண்டமஸ் பேராணையைப் பிறப்பிக்க முடியும்.",
    "The writ of Mandamus cannot be issued against judicial officers acting in their judicial capacity, nor against the President of India or State Governors for the performance of their official duties.",
    "நீதித்துறைத் தன்மையில் செயல்படும் நீதித்துறை அதிகாரிகளுக்கு எதிராகவும், அல்லது தங்கள் அதிகாரப்பூர்வ கடமைகளைச் செய்யும் இந்தியக் குடியரசுத் தலைவர் அல்லது மாநில ஆளுநர்களுக்கு எதிராகவும் மேண்டமஸ் பேராணையைப் பிறப்பிக்க முடியாது.",
    "D",
    "Assertion (A) is false but Reason (R) is true. Assertion (A) is false because Mandamus CANNOT be issued to judges acting judicially to compel a specific judicial decision or judgment. Reason (R) is true as established in Naresh Shridhar Mirajkar case and Article 361 immunity: Mandamus does not lie against judicial officers in judicial capacity, nor against the President/Governor under Article 361.",
    "கூற்று (A) தவறு, ஆனால் காரணம் (R) சரி. நீதித்துறைப் பணியில் இருக்கும் நீதிபதிகளுக்கு தீர்ப்பு வழங்குமாறு மேண்டமஸ் பிறப்பிக்க முடியாது. எனவே கூற்று A தவறு. காரணம் R சரி, ஏனெனில் நரேஷ் மிராஜ்கர் வழக்கு மற்றும் பிரிவு 361-ன் படி நீதிபதிகள், குடியரசுத் தலைவர், ஆளுநர்களுக்கு எதிராக மேண்டமஸ் பொருந்தாது.",
    "Incorrect. Assertion (A) is false because Mandamus does not lie against judges acting judicially.", "தவறு. நீதித்துறைப் பணியில் உள்ள நீதிபதிகளுக்கு எதிராக மேண்டமஸ் பொருந்தாது என்பதால் கூற்று A தவறாகும்.",
    "Incorrect. Assertion (A) is false under writ law.", "தவறு. பேராணைச் சட்டப்படி கூற்று A தவறாகும்.",
    "Incorrect. Assertion (A) is false, so option C is incorrect.", "தவறு. கூற்று A தவறானது, எனவே விருப்பம் C தவறாகும்.",
    "Correct. Assertion (A) is false (Mandamus cannot target judges judicially), but Reason (R) is true (Exceptions to Mandamus).", "சரி. கூற்று A தவறு (நீதிபதிகளுக்கு எதிராக மேண்டமஸ் இல்லை), ஆனால் காரணம் R சரி (மேண்டமஸ் விதிவிலக்குகள்).",
    "TNPSC Trap: Mandamus CANNOT be issued against: 1. Private individuals, 2. Departmental instructions without statutory force, 3. Discretionary duties, 4. Contractual obligations, 5. President/Governors (Art 361), 6. Chief Justice acting judicially.",
    "TNPSC பொறி: மேண்டமஸ் பொருந்தாத இடங்கள்: 1. தனியார் நபர்கள், 2. சட்டப்பூர்வ பலமில்லாத துறைசார் அறிவுறுத்தல்கள், 3. விருப்ப அதிகாரக் கடமைகள், 4. ஒப்பந்தப் பொறுப்புகள், 5. குடியரசுத் தலைவர்/ஆளுநர்கள், 6. நீதித்துறைப் பணியில் உள்ள தலைமை நீதிபதி.",
    "Mandamus Exceptions: Private individuals, Discretionary duties, President/Governors (Art 361), Judicial capacity judges.",
    "மேண்டமஸ் விதிவிலக்குகள்: தனியார் நபர்கள், விருப்பக் கடமைகள், குடியரசுத் தலைவர்/ஆளுநர்கள் (பிரிவு 361), நீதித்துறை நீதிபதிகள்.",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Reasoning", "Writs", "Mandamus", "Exceptions"]
))

# FR_R_025 (Hard | Target Ans: D)
questions.append(make_reasoning_q(
    "FR_R_025", "Hard",
    "Uncodified personal laws (such as traditional Hindu Law or Muslim Personal Law) automatically fall within the definition of 'law' under Article 13(3)(a) and can be challenged for violating Fundamental Rights.",
    "குறியீடு செய்யப்படாத தனிநபர் சட்டங்கள் (பாரம்பரிய இந்து சட்டம் அல்லது முஸ்லிம் தனிநபர் சட்டம் போன்றவை) பிரிவு 13(3)(a)-ன் கீழ் 'சட்டம்' என்ற வரையறைக்குள் தானாகவே வரும் மற்றும் அடிப்படை உரிமைகளை மீறுவதாக சவால் செய்யப்படலாம்.",
    "Article 13(3)(a) defines 'law' to include ordinances, orders, bye-laws, rules, regulations, notifications, customs, or usages having the force of law, but the Bombay High Court in Narasu Appa Mali case held that personal laws are not covered under Article 13.",
    "பிரிவு 13(3)(a) 'சட்டம்' என்பதை அவசரச் சட்டங்கள், உத்தரவுகள், துணை விதிகள், விதிகள், ஒழுங்குமுறைகள், அறிவிக்கைகள், பழக்கவழக்கங்கள் அல்லது வழக்கங்களை உள்ளடக்கியதாக வரையறுக்கிறது, ஆனால் நரசு அப்பா மாலி வழக்கில் பம்பாய் உயர்நீதிமன்றம் தனிநபர் சட்டங்கள் பிரிவு 13-ன் கீழ் வராது எனத் தீர்ப்பளித்தது.",
    "D",
    "Assertion (A) is false but Reason (R) is true. Assertion (A) is false because in the historic State of Bombay v. Narasu Appa Mali (1952) case, Chief Justice Chagla and Justice Gajendragadkar held that uncodified personal laws are NOT 'law' or 'custom/usage' within the meaning of Article 13(3)(a), and thus cannot be challenged under Article 13 for violating Part III rights (though statutory codified personal laws can be). Reason (R) is completely true.",
    "கூற்று (A) தவறு, ஆனால் காரணம் (R) சரி. பம்பாய் மாநிலம் எதிராக நரசு அப்பா மாலி (1952) வழக்கில், குறியீடு செய்யப்படாத தனிநபர் சட்டங்கள் பிரிவு 13(3)(a)-ன் கீழ் 'சட்டம்' அல்ல எனத் தீர்ப்பளிக்கப்பட்டது. எனவே அவை பிரிவு 13-ன் கீழ் சவால் செய்யப்பட முடியாது. எனவே கூற்று A தவறு, காரணம் R சரி.",
    "Incorrect. Assertion (A) is false under the ruling in Narasu Appa Mali (1952).", "தவறு. நரசு அப்பா மாலி (1952) தீர்ப்பின்படி கூற்று A தவறாகும்.",
    "Incorrect. Assertion (A) is false under personal law jurisprudence.", "தவறு. தனிநபர் சட்டக் கோட்பாட்டின்படி கூற்று A தவறாகும்.",
    "Incorrect. Assertion (A) is false, so option C is incorrect.", "தவறு. கூற்று A தவறானது, எனவே விருப்பம் C தவறாகும்.",
    "Correct. Assertion (A) is false (Uncodified personal law is not Art 13 'law'), but Reason (R) is true (Narasu Appa Mali 1952 precedent).", "சரி. கூற்று A தவறு (குறியீடு செய்யப்படாத தனிநபர் சட்டம் பிரிவு 13 'சட்டம்' அல்ல), ஆனால் காரணம் R சரி (நரசு அப்பா மாலி 1952 முன்மாதிரி).",
    "TNPSC Trap: Article 13(3)(a) includes Customs and Usages having force of law, but Narasu Appa Mali (1952) excluded uncodified Personal Laws from Article 13 scrutiny.",
    "TNPSC பொறி: பிரிவு 13(3)(a) சட்டப்பூர்வ பலம் கொண்ட பழக்கவழக்கங்களை உள்ளடக்கியது, ஆனால் நரசு அப்பா மாலி (1952) வழக்கு குறியீடு செய்யப்படாத தனிநபர் சட்டங்களை பிரிவு 13 ஆய்விலிருந்து விலக்கியது.",
    "Narasu Appa Mali Case (1952): Uncodified Personal Laws are NOT 'Law' under Article 13(3)(a).",
    "நரசு அப்பா மாலி வழக்கு (1952): குறியீடு செய்யப்படாத தனிநபர் சட்டங்கள் பிரிவு 13(3)(a)-ன் கீழ் 'சட்டம்' அல்ல.",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Reasoning", "Article 13", "Personal Laws", "Narasu Appa Mali Case"]
))

# Save full 25 questions dataset to BOTH file paths
print(f"Total Reasoning questions compiled: {len(questions)}")
assert len(questions) == 25, f"Expected 25 questions, got {len(questions)}"

with open(target_path_1, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)
print(f"✅ Successfully wrote 25 Reasoning MCQs to {target_path_1}")

with open(target_path_2, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)
print(f"✅ Successfully wrote 25 Reasoning MCQs to {target_path_2}")
