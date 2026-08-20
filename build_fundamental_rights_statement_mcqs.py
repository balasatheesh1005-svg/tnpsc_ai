# -*- coding: utf-8 -*-
"""
Builder Script for Fundamental Rights 50 Statement-Based MCQs Repository
Target Path: data/questions/polity/fundamental_rights_statement_based.json
"""

import json
import os
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

target_path = Path(r"c:\Users\Home\Desktop\tnpsc_ai\data\questions\polity\fundamental_rights_statement_based.json")
target_path.parent.mkdir(parents=True, exist_ok=True)

def make_q(q_id, difficulty, q_en, q_ta, opt_a_en, opt_a_ta, opt_b_en, opt_b_ta, opt_c_en, opt_c_ta, opt_d_en, opt_d_ta,
           correct_ans, exp_en, exp_ta, wno_a_en, wno_a_ta, wno_b_en, wno_b_ta, wno_c_en, wno_c_ta, wno_d_en, wno_d_ta,
           tip_en, tip_ta, rev_en, rev_ta, bloom, est_time, tags):
    opts = [
        {"id": "A", "en": opt_a_en, "ta": opt_a_ta},
        {"id": "B", "en": opt_b_en, "ta": opt_b_ta},
        {"id": "C", "en": opt_c_en, "ta": opt_c_ta},
        {"id": "D", "en": opt_d_en, "ta": opt_d_ta}
    ]
    opts_en = [opt_a_en, opt_b_en, opt_c_en, opt_d_en]
    opts_ta = [opt_a_ta, opt_b_ta, opt_c_ta, opt_d_ta]
    
    return {
        "id": q_id,
        "subject": "Polity",
        "topic": "Fundamental Rights",
        "difficulty": difficulty,
        "question_type": "Statement Based",
        "question": {"en": q_en, "ta": q_ta},
        "options": opts,
        "correct_answer": correct_ans,
        "explanation": {"en": exp_en, "ta": exp_ta},
        "why_not_others": {
            "A": {"en": wno_a_en, "ta": wno_a_ta},
            "B": {"en": wno_b_en, "ta": wno_b_ta},
            "C": {"en": wno_c_en, "ta": wno_c_ta},
            "D": {"en": wno_d_en, "ta": wno_d_ta}
        },
        "tnpsc_tip": {"en": tip_en, "ta": tip_ta},
        "revision_fact": {"en": rev_en, "ta": rev_ta},
        "source_reference": ["M. Laxmikanth - Indian Polity", "NCERT", "Samacheer Kalvi"],
        "bloom_level": bloom,
        "estimated_time_sec": est_time,
        "pyq_similarity": "High",
        "tags": tags,
        "question_en": q_en,
        "question_ta": q_ta,
        "options_en": opts_en,
        "options_ta": opts_ta,
        "answer": correct_ans.lower(),
        "explanation_en": exp_en,
        "explanation_ta": exp_ta
    }

questions = []

# ==============================================================================
# PART 1: 15 TWO-STATEMENT QUESTIONS (FR_SB_001 to FR_SB_015)
# ==============================================================================

# FR_SB_001 (Easy)
questions.append(make_q(
    "FR_SB_001", "Easy",
    "Consider the following statements regarding Article 12 of the Indian Constitution:\n1. The term 'State' includes the Executive and Legislative organs of the Union and State governments.\n2. Statutory and non-statutory authorities like LIC, ONGC, and SAIL fall within the definition of 'State'.\nWhich of the statements given above is/are correct?",
    "இந்திய அரசியலமைப்பின் 12-வது பிரிவைக் குறித்து பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 'அரசு' (State) என்ற சொல் மத்திய மற்றும் மாநில அரசாங்கங்களின் நிர்வாக மற்றும் சட்டமன்ற உறுப்புகளை உள்ளடக்கியது.\n2. எல்.ஐ.சி, ஓ.என்.ஜி.சி மற்றும் சேல் போன்ற சட்டப்பூர்வ மற்றும் சட்டப்பூர்வமற்ற அமைப்புகள் 'அரசு' என்பதன் வரைவிலக்கணத்திற்குள் வருகின்றன.\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1 only", "1 மட்டும்",
    "2 only", "2 மட்டும்",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை",
    "C",
    "Both statements are correct. Article 12 defines 'State' broadly to include the Government and Parliament of India, Government and Legislature of States, local authorities, and other statutory or non-statutory authorities (e.g., LIC, ONGC, SAIL) carrying out public functions.",
    "இரண்டு கூற்றுகளும் சரியானவை. பிரிவு 12 'அரசு' என்பதை விரிவாக வரையறுக்கிறது. இதில் இந்திய அரசு, நாடாளுமன்றம், மாநில அரசுகள், சட்டமன்றங்கள், உள்ளாட்சி அமைப்புகள் மற்றும் பொதுப் பணிகளைச் செய்யும் எல்.ஐ.சி, ஓ.என்.ஜி.சி போன்ற பிற அமைப்புகளும் அடங்கும்.",
    "Incorrect. Statement 2 is also correct.", "தவறு. கூற்று 2-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.", "தவறு. கூற்று 1-ம் சரியானது.",
    "Correct. Both Statements 1 and 2 are constitutional facts under Article 12.", "சரி. பிரிவு 12-ன் கீழ் கூற்றுகள் 1 மற்றும் 2 இரண்டும் உண்மை.",
    "Incorrect. Both statements are accurate.", "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
    "TNPSC Trap: Judiciary acting in its judicial capacity is generally NOT included under Article 12, but in its administrative capacity it functions as State.",
    "TNPSC பொறி: நீதித்துறை தனது நீதித்துறை அதிகாரத்தைச் செயல்படுத்தும்போது பிரிவு 12-ன் கீழ் வராது, ஆனால் நிர்வாகப் பணிகளைச் செய்யும்போது அரசின் கீழ் வரும்.",
    "Article 12 defines 'State' specifically for the purpose of Part III (Fundamental Rights).",
    "பிரிவு 12 பகுதி III-ன் (அடிப்படை உரிமைகள்) பயன்பாட்டிற்காக மட்டுமே 'அரசு' என்பதை வரையறுக்கிறது.",
    "Understand", 60, ["Polity", "Fundamental Rights", "Article 12", "State Definition", "Two Statement"]
))

# FR_SB_002 (Medium)
questions.append(make_q(
    "FR_SB_002", "Medium",
    "Consider the following statements regarding Article 13 of the Indian Constitution:\n1. Article 13 explicitly provides for the doctrine of judicial review of laws inconsistent with Fundamental Rights.\n2. Constitutional Amendments passed under Article 368 are included within the definition of 'law' under Article 13(2).\nWhich of the statements given above is/are correct?",
    "இந்திய அரசியலமைப்பின் 13-வது பிரிவைக் குறித்து பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. அடிப்படை உரிமைகளுக்கு முரணான சட்டங்களை நீதித்துறை மறுஆய்வு செய்யும் கோட்பாட்டை பிரிவு 13 வெளிப்படையாக வழங்குகிறது.\n2. பிரிவு 368-ன் கீழ் நிறைவேற்றப்படும் அரசியலமைப்பு திருத்தங்கள் பிரிவு 13(2)-ன் கீழ் 'சட்டம்' என்பதன் வரைவிலக்கணத்திற்குள் அடங்கும்.\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1 only", "1 மட்டும்",
    "2 only", "2 மட்டும்",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை",
    "A",
    "Statement 1 is correct (Art 13 provides constitutional foundation for Judicial Review). Statement 2 is INCORRECT because Kesavananda Bharati case (1973) affirmed that Constitutional Amendments are NOT 'law' under Art 13, though they can be challenged if they violate Basic Structure.",
    "கூற்று 1 சரி (பிரிவு 13 நீதித்துறை மறுஆய்வுக்கான அரசியலமைப்பு அடிப்படையை வழங்குகிறது). கூற்று 2 தவறு, ஏனெனில் கேசவாநந்த பாரதி வழக்கில் (1973) அரசியலமைப்பு திருத்தங்கள் பிரிவு 13-ன் கீழ் 'சட்டம்' அல்ல என்று உறுதி செய்யப்பட்டது.",
    "Correct. Statement 1 is true; Statement 2 is false as Constitutional Amendments are not 'law' under Art 13.", "சரி. கூற்று 1 சரி; அரசியலமைப்பு திருத்தங்கள் பிரிவு 13-ன் கீழ் 'சட்டம்' இல்லாததால் கூற்று 2 தவறு.",
    "Incorrect. Statement 1 is correct.", "தவறு. கூற்று 1 சரியானது.",
    "Incorrect. Statement 2 is false.", "தவறு. கூற்று 2 தவறானது.",
    "Incorrect. Statement 1 is accurate.", "தவறு. கூற்று 1 சரியானது.",
    "TNPSC Trap: Notifications, bye-laws, orders, and customs having the force of law are 'law' under Article 13, but Constitutional Amendments are excluded from Article 13 definition.",
    "TNPSC பொறி: அறிவிப்புகள், விதிகள், உத்தரவுகள் பிரிவு 13-ன் கீழ் 'சட்டம்' ஆகும், ஆனால் அரசியலமைப்பு திருத்தங்கள் பிரிவு 13 வரைவிலக்கணத்தில் சேராது.",
    "Article 13(2) declares that the State shall not make any law which takes away or abridges the Fundamental Rights.",
    "அடிப்படை உரிமைகளைப் பறிக்கும் அல்லது குறைக்கும் எந்தவொரு சட்டத்தையும் அரசு உருவாக்கக் கூடாது என்று பிரிவு 13(2) கூறுகிறது.",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Article 13", "Judicial Review", "Two Statement"]
))

# FR_SB_003 (Medium)
questions.append(make_q(
    "FR_SB_003", "Medium",
    "Consider the following statements regarding the Doctrine of Severability and Doctrine of Eclipse:\n1. The Doctrine of Severability implies that if a law violates Fundamental Rights, only the offending provision is void, provided it is separable from the rest.\n2. The Doctrine of Eclipse applies to post-constitutional laws making them void ab initio.\nWhich of the statements given above is/are correct?",
    "பிரித்தல் கோட்பாடு (Severability) மற்றும் கிரகணக் கோட்பாடு (Eclipse) பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. பிரித்தல் கோட்பாடு என்பது ஒரு சட்டம் அடிப்படை உரிமைகளை மீறினால், அது மற்ற பகுதிகளிலிருந்து பிரிக்கக்கூடியதாக இருந்தால், மீறும் பகுதி மட்டுமே செல்லாததாகும் என்பதைக் குறிக்கிறது.\n2. கிரகணக் கோட்பாடு அரசியலமைப்புக்கு பிந்தைய சட்டங்களுக்குப் பொருந்தும், மேலும் அவற்றை ஆரம்பத்திலிருந்தே செல்லாததாக்குகிறது (void ab initio).\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1 only", "1 மட்டும்",
    "2 only", "2 மட்டும்",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை",
    "A",
    "Statement 1 is correct (severability isolates invalid parts without striking down the entire statute). Statement 2 is INCORRECT because the Doctrine of Eclipse primarily applies to PRE-CONSTITUTIONAL laws (Bhikaji case 1955), making them dormant/shadowed, not dead ab initio.",
    "கூற்று 1 சரி (பிரித்தல் கோட்பாடு செல்லாத பகுதியை மட்டும் பிரிக்கிறது). கூற்று 2 தவறு, ஏனெனில் கிரகணக் கோட்பாடு முதன்மையாக அரசியலமைப்புக்கு முந்தைய சட்டங்களுக்கே பொருந்தும்; அவை செயலற்றதாக மாறுமே தவிர ஆரம்பத்திலிருந்தே இறந்துவிடாது.",
    "Correct. Statement 1 is true; Statement 2 is false.", "சரி. கூற்று 1 சரி; கூற்று 2 தவறானது.",
    "Incorrect. Statement 1 is correct.", "தவறு. கூற்று 1 சரியானது.",
    "Incorrect. Statement 2 is false.", "தவறு. கூற்று 2 தவறானது.",
    "Incorrect. Statement 1 is correct.", "தவறு. கூற்று 1 சரியானது.",
    "TNPSC Trap: Doctrine of Eclipse makes pre-constitutional laws dormant against citizens. If the Fundamental Right is amended later, the shadow is removed and the law becomes active again.",
    "TNPSC பொறி: கிரகணக் கோட்பாடு அரசியலமைப்புக்கு முந்தைய சட்டங்களை குடிமக்களுக்கு எதிராக மறைத்து வைக்கிறது. பின்னர் அடிப்படை உரிமை திருத்தப்பட்டால், சட்டம் மீண்டும் உயிர்பெறும்.",
    "The Supreme Court formulated the Doctrine of Eclipse in Bhikaji Narain Dhakras v. State of M.P. (1955).",
    "உச்சநீதிமன்றம் பிகாஜி நரேன் எதிராக மத்தியப் பிரதேச மாநில வழக்கில் (1955) கிரகணக் கோட்பாட்டை உருவாக்கியது.",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Article 13", "Doctrine of Eclipse", "Two Statement"]
))

# FR_SB_004 (Easy)
questions.append(make_q(
    "FR_SB_004", "Easy",
    "Consider the following statements regarding Article 14 of the Indian Constitution:\n1. 'Equality before law' is a concept of British origin representing a negative element.\n2. 'Equal protection of the laws' is a concept of American origin representing a positive element.\nWhich of the statements given above is/are correct?",
    "இந்திய அரசியலமைப்பின் 14-வது பிரிவைக் குறித்து பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 'சட்டத்தின் முன் சமன்' என்ற கருத்து பிரிட்டிஷ் மூலத்தைக் கொண்ட ஒரு எதிர்மறைக் கருத்தாகும்.\n2. 'சட்டங்களின் சமமான பாதுகாப்பு' என்ற கருத்து அமெரிக்க மூலத்தைக் கொண்ட ஒரு நேர்மறைக் கருத்தாகும்.\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1 only", "1 மட்டும்",
    "2 only", "2 மட்டும்",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை",
    "C",
    "Both statements are correct. Article 14 contains two expressions: 'Equality before law' (British origin, negative concept - absence of special privileges) and 'Equal protection of laws' (American origin, positive concept - equal treatment under equal circumstances).",
    "இரண்டு கூற்றுகளும் சரியானவை. பிரிவு 14 இரு கருத்துக்களைக் கொண்டுள்ளது: 'சட்டத்தின் முன் சமன்' (பிரிட்டிஷ் ஆதாரம், எதிர்மறை) மற்றும் 'சட்டங்களின் சமமான பாதுகாப்பு' (அமெரிக்க ஆதாரம், நேர்மறை).",
    "Incorrect. Statement 2 is also correct.", "தவறு. கூற்று 2-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.", "தவறு. கூற்று 1-ம் சரியானது.",
    "Correct. Both Statements 1 and 2 are historically and legally accurate.", "சரி. கூற்றுகள் 1 மற்றும் 2 இரண்டும் சட்டப்பூர்வமாக சரியானவை.",
    "Incorrect. Both statements are correct.", "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
    "TNPSC Trap: 'Equality before law' prohibits special privileges, while 'Equal protection of laws' permits reasonable classification of persons and things.",
    "TNPSC பொறி: 'சட்டத்தின் முன் சமன்' சிறப்பு உரிமைகளைத் தடுக்கிறது, ஆனால் 'சட்டங்களின் சமமான பாதுகாப்பு' நியாயமான பாகுபாட்டை அல்லது பகுப்பாய்வை அனுமதிக்கிறது.",
    "Article 14 embodies the Rule of Law doctrine expounded by British legal scholar A.V. Dicey.",
    "பிரிவு 14 பிரிட்டிஷ் சட்ட அறிஞர் ஏ.வி. டைசி விவரித்த 'சட்டத்தின் ஆட்சி' கோட்பாட்டை உள்ளடக்கியது.",
    "Understand", 60, ["Polity", "Fundamental Rights", "Article 14", "Equality before Law", "Two Statement"]
))

# FR_SB_005 (Easy)
questions.append(make_q(
    "FR_SB_005", "Easy",
    "Consider the following statements regarding Article 15 of the Indian Constitution:\n1. Article 15 prohibits discrimination by the State against any citizen on grounds ONLY of religion, race, caste, sex, place of birth, or any of them.\n2. Article 15(4) was added by the First Constitutional Amendment Act, 1951 to enable special provisions for socially and educationally backward classes.\nWhich of the statements given above is/are correct?",
    "இந்திய அரசியலமைப்பின் 15-வது பிரிவைக் குறித்து பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. பிரிவு 15 மதம், இனம், சாதி, பாலினம், பிறந்த இடம் ஆகிய காரணங்களுக்காக மட்டுமே குடிமக்களுக்கு எதிராக பாகுபாடு காட்டுவதை அரசுக்குத் தடை செய்கிறது.\n2. சமூக மற்றும் கல்வியில் பின்தங்கிய வகுப்பினருக்கு சிறப்பு ஏற்பாடுகளை செய்ய 1-வது அரசியலமைப்பு திருத்தச் சட்டம், 1951 மூலம் பிரிவு 15(4) சேர்க்கப்பட்டது.\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1 only", "1 மட்டும்",
    "2 only", "2 மட்டும்",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை",
    "C",
    "Both statements are correct. Article 15(1) specifies exactly 5 prohibited grounds of discrimination. Article 15(4) was introduced by the 1st Amendment Act, 1951 following the Champakam Dorairajan case judgment.",
    "இரண்டு கூற்றுகளும் சரியானவை. பிரிவு 15(1) பாகுபாடு காட்டக்கூடாத 5 குறிப்பிட்ட காரணங்களை வழங்குகிறது. சண்பகம் துரைராஜன் வழக்கைத் தொடர்ந்து 1951-ல் 1வது திருத்தம் மூலம் 15(4) சேர்க்கப்பட்டது.",
    "Incorrect. Statement 2 is also correct.", "தவறு. கூற்று 2-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.", "தவறு. கூற்று 1-ம் சரியானது.",
    "Correct. Both Statements 1 and 2 are historically and constitutionally true.", "சரி. கூற்றுகள் 1 மற்றும் 2 இரண்டும் உண்மை.",
    "Incorrect. Both statements are correct.", "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
    "TNPSC Trap: Article 15 protects CITIZENS ONLY (not non-citizens), and prohibits discrimination on 5 grounds (unlike Art 16 which has 7 grounds).",
    "TNPSC பொறி: பிரிவு 15 குடிமக்களுக்கு மட்டுமே பொருந்தும் (வெளிநாட்டினருக்கு இல்லை), மேலும் 5 காரணங்களின் கீழ் மட்டுமே பாகுபாட்டைத் தடுக்கிறது.",
    "The word 'only' in Article 15 means that discrimination on other grounds (like residence or language) is not prohibited per se.",
    "பிரிவு 15-ல் உள்ள 'மட்டுமே' (only) என்ற சொல் பிற காரணங்களுக்காக (வாப்பிடம் அல்லது மொழி) பாகுபாடு காட்டுவது தடுக்கப்படவில்லை என்பதைக் குறிக்கிறது.",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Article 15", "Non-Discrimination", "Two Statement"]
))

# FR_SB_006 (Medium)
questions.append(make_q(
    "FR_SB_006", "Medium",
    "Consider the following statements regarding Constitutional Provisions for Reservations in Educational Institutions:\n1. Article 15(5), added by the 93rd Constitutional Amendment Act 2005, enables reservation for OBCs/SCs/STs in private educational institutions including minority institutions.\n2. Article 15(6), inserted by the 103rd Amendment Act 2019, provides up to 10% reservation for Economically Weaker Sections (EWS).\nWhich of the statements given above is/are correct?",
    "கல்வி நிறுவனங்களில் இடஒதுக்கீடு செய்வதற்கான அரசியலமைப்பு விதிகள் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 93-வது அரசியலமைப்பு திருத்தச் சட்டம் 2005 மூலம் சேர்க்கப்பட்ட பிரிவு 15(5), சிறுபான்மையினர் கல்வி நிறுவனங்கள் உட்பட அனைத்து தனியார் கல்வி நிறுவனங்களிலும் பிற்படுத்தப்பட்டோருக்கு இடஒதுக்கீட்டை வழங்குகிறது.\n2. 103-வது திருத்தச் சட்டம் 2019 மூலம் சேர்க்கப்பட்ட பிரிவு 15(6), பொருளாதாரத்தில் பலவீனமான பிரிவினருக்கு (EWS) 10% வரை இடஒதுக்கீடு வழங்குகிறது.\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1 only", "1 மட்டும்",
    "2 only", "2 மட்டும்",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை",
    "B",
    "Statement 1 is INCORRECT because Article 15(5) explicitly EXCLUDES minority educational institutions referred to in Article 30(1). Statement 2 is correct (103rd Amendment 2019 added Art 15(6) for EWS reservation up to 10%).",
    "கூற்று 1 தவறு, ஏனெனில் பிரிவு 15(5) பிரிவு 30(1)-ன் கீழ் உள்ள சிறுபான்மையினர் கல்வி நிறுவனங்களுக்கு விதிவிலக்கு அளிக்கிறது. கூற்று 2 சரி (103வது திருத்தம் EWS இடஒதுக்கீட்டை வழங்குகிறது).",
    "Incorrect. Statement 1 is false.", "தவறு. கூற்று 1 தவறானது.",
    "Correct. Statement 2 is true; Statement 1 is false because minority institutions are excluded.", "சரி. கூற்று 2 சரி; சிறுபான்மை நிறுவனங்கள் விலக்கப்பட்டுள்ளதால் கூற்று 1 தவறு.",
    "Incorrect. Statement 1 is false.", "தவறு. கூற்று 1 தவறானது.",
    "Incorrect. Statement 2 is correct.", "தவறு. கூற்று 2 சரியானது.",
    "TNPSC Trap: Minority educational institutions (Art 30) are specifically EXEMPTED from the scope of Article 15(5) reservations.",
    "TNPSC பொறி: சிறுபான்மையினர் கல்வி நிறுவனங்கள் (பிரிவு 30) பிரிவு 15(5) இடஒதுக்கீட்டிலிருந்து விலக்கப்பட்டுள்ளன.",
    "The constitutionality of Article 15(5) was upheld by the Supreme Court in Pramati Educational Trust case (2014).",
    "பிரமதி கல்வி அறக்கட்டளை வழக்கில் (2014) உச்ச நீதிமன்றம் பிரிவு 15(5)-ன் அரசியலமைப்பு செல்லுபடியாகும் தன்மையை உறுதி செய்தது.",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Article 15(5)", "103rd Amendment", "Two Statement"]
))

# FR_SB_007 (Medium)
questions.append(make_q(
    "FR_SB_007", "Medium",
    "Consider the following statements regarding Article 16 of the Indian Constitution:\n1. Article 16(2) prohibits discrimination in public employment on seven grounds: Religion, Race, Caste, Sex, Descent, Place of Birth, and Residence.\n2. State Legislatures have the exclusive power under Article 16(3) to prescribe residence requirements for public employment within their state.\nWhich of the statements given above is/are correct?",
    "இந்திய அரசியலமைப்பின் 16-வது பிரிவைக் குறித்து பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. பிரிவு 16(2) பொது வேலைவாய்ப்பில் மதம், இனம், சாதி, பாலினம், வம்சம், பிறந்த இடம், இருப்பிடம் ஆகிய 7 காரணங்களுக்காக பாகுபாடு காட்டுவதைத் தடை செய்கிறது.\n2. மாநில சட்டமன்றங்கள் தங்கள் மாநிலத்தில் பொது வேலைவாய்ப்பிற்கு இருப்பிடத் தேவைகளை விதிக்க பிரிவு 16(3)-ன் கீழ் பிரத்யேக அதிகாரம் கொண்டுள்ளன.\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1 only", "1 மட்டும்",
    "2 only", "2 மட்டும்",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை",
    "A",
    "Statement 1 is correct (Art 16(2) lists 7 prohibited grounds, adding Descent and Residence to Art 15's list). Statement 2 is INCORRECT because Article 16(3) empowers PARLIAMENT ALONE (not State Legislatures) to prescribe residence as a condition for certain employment.",
    "கூற்று 1 சரி (பிரிவு 16(2) வம்சம், இருப்பிடம் உட்பட 7 காரணங்களைக் குறிப்பிடுகிறது). கூற்று 2 தவறு, ஏனெனில் பிரிவு 16(3)-ன் கீழ் நாடாளுமன்றத்திற்கு மட்டுமே இருப்பிட விதியை விதிக்கும் அதிகாரம் உண்டு (மாநில சட்டமன்றங்களுக்கு இல்லை).",
    "Correct. Statement 1 is true; Statement 2 is false as Parliament, not state legislature, holds the power.", "சரி. கூற்று 1 சரி; மாநில சட்டமன்றத்திற்கு பதிலாக நாடாளுமன்றத்திற்கு மட்டுமே அதிகாரம் உள்ளதால் கூற்று 2 தவறு.",
    "Incorrect. Statement 1 is correct.", "தவறு. கூற்று 1 சரியானது.",
    "Incorrect. Statement 2 is false.", "தவறு. கூற்று 2 தவறானது.",
    "Incorrect. Statement 1 is correct.", "தவறு. கூற்று 1 சரியானது.",
    "TNPSC Trap: Article 15 has 5 grounds; Article 16 has 7 grounds (adds 'Descent' and 'Residence'). Only PARLIAMENT can make residence rules under 16(3).",
    "TNPSC பொறி: பிரிவு 15-ல் 5 காரணங்களும், பிரிவு 16-ல் 7 காரணங்களும் உள்ளன. 16(3)-ன் கீழ் நாடாளுமன்றம் மட்டுமே இருப்பிட விதியை உருவாக்க முடியும்.",
    "Parliament enacted Public Employment (Requirement as to Residence) Act, 1957 under Article 16(3).",
    "நாடாளுமன்றம் பிரிவு 16(3)-ன் கீழ் பொது வேலைவாய்ப்பு (இருப்பிடத் தேவை) சட்டம் 1957-ஐ இயற்றியது.",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Article 16", "Public Employment", "Two Statement"]
))

# FR_SB_008 (Medium)
questions.append(make_q(
    "FR_SB_008", "Medium",
    "Consider the following statements regarding Constitutional Amendments to Article 16:\n1. The 77th Constitutional Amendment Act, 1995 introduced Article 16(4A) enabling reservation in promotions for SCs and STs.\n2. The 81st Constitutional Amendment Act, 2000 introduced Article 16(4B) allowing carry-forward of unfilled reserved vacancies beyond the 50% ceiling limit.\nWhich of the statements given above is/are correct?",
    "பிரிவு 16-ல் கொண்டுவரப்பட்ட அரசியலமைப்பு திருத்தங்கள் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 77-வது அரசியலமைப்பு திருத்தச் சட்டம், 1995 பிரிவு 16(4A)-ஐ அறிமுகப்படுத்தி பட்டியலின மற்றும் பழங்குடியினருக்கு பதவி உயர்வில் இடஒதுக்கீட்டை வழங்கியது.\n2. 81-வது அரசியலமைப்பு திருத்தச் சட்டம், 2000 பிரிவு 16(4B)-ஐ அறிமுகப்படுத்தி நிரப்பப்படாத இடஒதுக்கீடு காலிப்பணியிடங்களை 50% வரம்பிற்கு அப்பால் கொண்டு செல்ல (carry-forward) அனுமதித்தது.\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1 only", "1 மட்டும்",
    "2 only", "2 மட்டும்",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை",
    "C",
    "Both statements are correct. 77th CAA 1995 added 16(4A) for reservation in promotion for SCs/STs, overriding the Indra Sawhney ruling. 81st CAA 2000 added 16(4B) to treat backlog vacancies as a separate class not counted towards the 50% cap.",
    "இரண்டு கூற்றுகளும் சரியானவை. 77வது திருத்தம் (1995) 16(4A) மூலம் பதவி உயர்வு இடஒதுக்கீட்டை வழங்கியது. 81வது திருத்தம் (2000) 16(4B) மூலம் 50% வரம்பிற்கு அப்பால் காலிப்பணியிடங்களை நிரப்ப அனுமதித்தது.",
    "Incorrect. Statement 2 is also correct.", "தவறு. கூற்று 2-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.", "தவறு. கூற்று 1-ம் சரியானது.",
    "Correct. Both Statements 1 and 2 are historically and legally accurate.", "சரி. கூற்றுகள் 1 மற்றும் 2 இரண்டும் சட்டப்பூர்வமாக சரியானவை.",
    "Incorrect. Both statements are accurate.", "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
    "TNPSC Trap: The 85th Amendment Act 2001 provided for 'consequential seniority' for SC/ST government servants promoted on reservation.",
    "TNPSC பொறி: 85-வது திருத்தச் சட்டம் 2001 இடஒதுக்கீட்டில் பதவி உயர்வு பெறும் SC/ST அரசு ஊழியர்களுக்கு 'தொடர் பணி மூப்பு' (consequential seniority) வழங்கியது.",
    "The Supreme Court upheld the constitutional validity of 77th, 81st, 82nd, and 85th Amendments in M. Nagaraj case (2006).",
    "எம். நாகராஜ் வழக்கில் (2006) உச்ச நீதிமன்றம் 77, 81, 82 மற்றும் 85 ஆகிய திருத்தங்களின் செல்லுபடியாகும் தன்மையை உறுதி செய்தது.",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Article 16(4A)", "81st Amendment", "Two Statement"]
))

# FR_SB_009 (Easy)
questions.append(make_q(
    "FR_SB_009", "Easy",
    "Consider the following statements regarding Article 17 of the Indian Constitution:\n1. Article 17 abolishes 'Untouchability' and forbids its practice in any form.\n2. The term 'Untouchability' is explicitly defined in Part III of the Constitution.\nWhich of the statements given above is/are correct?",
    "இந்திய அரசியலமைப்பின் 17-வது பிரிவைக் குறித்து பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. பிரிவு 17 'தீண்டாமையை' ஒழித்து, எந்த வடிவத்திலும் அதை நடைமுறைப்படுத்துவதைத் தடுக்கிறது.\n2. 'தீண்டாமை' என்ற சொல் அரசியலமைப்பின் பகுதி III-ல் வெளிப்படையாக வரையறுக்கப்பட்டுள்ளது.\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1 only", "1 மட்டும்",
    "2 only", "2 மட்டும்",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை",
    "A",
    "Statement 1 is correct (Art 17 abolishes untouchability in all forms). Statement 2 is INCORRECT because neither the Constitution nor the Protection of Civil Rights Act 1955 defines the term 'Untouchability'.",
    "கூற்று 1 சரி (பிரிவு 17 தீண்டாமையை ஒழிக்கிறது). கூற்று 2 தவறு, ஏனெனில் அரசியலமைப்பிலோ அல்லது சிவில் உரிமைகள் பாதுகாப்புச் சட்டத்திலோ 'தீண்டாமை' என்ற சொல் வரையறுக்கப்படவில்லை.",
    "Correct. Statement 1 is true; Statement 2 is false as untouchability is not defined in the Constitution.", "சரி. கூற்று 1 சரி; அரசியலமைப்பில் தீண்டாமை வரையறுக்கப்படாததால் கூற்று 2 தவறு.",
    "Incorrect. Statement 1 is correct.", "தவறு. கூற்று 1 சரியானது.",
    "Incorrect. Statement 2 is false.", "தவறு. கூற்று 2 தவறானது.",
    "Incorrect. Statement 1 is correct.", "தவறு. கூற்று 1 சரியானது.",
    "TNPSC Trap: Article 17 is an absolute Fundamental Right available against both State and private individuals without any constitutional exception.",
    "TNPSC பொறி: பிரிவு 17 என்பது அரசு மற்றும் தனிநபர்களுக்கு எதிராகக் கிடைக்கும் எந்தவொரு விதிவிலக்கும் இல்லாத ஒரு முழுமையான (absolute) அடிப்படை உரிமையாகும்.",
    "Untouchability Offences Act 1955 was comprehensively amended and renamed as 'Protection of Civil Rights Act, 1955' in 1976.",
    "தீண்டாமை குற்றச் சட்டம் 1955 திருத்தப்பட்டு 1976-ல் 'சிவில் உரிமைகள் பாதுகாப்புச் சட்டம் 1955' என பெயர் மாற்றப்பட்டது.",
    "Understand", 60, ["Polity", "Fundamental Rights", "Article 17", "Untouchability", "Two Statement"]
))

# FR_SB_010 (Medium)
questions.append(make_q(
    "FR_SB_010", "Medium",
    "Consider the following statements regarding Article 18 of the Indian Constitution:\n1. Article 18 prohibits the State from conferring any title except military or academic distinctions.\n2. In the Balaji Raghavan case (1996), the Supreme Court ruled that National Awards like Bharat Ratna and Padma Awards are titles under Article 18 and are invalid.\nWhich of the statements given above is/are correct?",
    "இந்திய அரசியலமைப்பின் 18-வது பிரிவைக் குறித்து பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இராணுவ அல்லது கல்விச் சிறப்புகளைத் தவிர வேறு எந்தப் பட்டங்களையும் அரசு வழங்குவதை பிரிவு 18 தடை செய்கிறது.\n2. பாலாஜி ராகவன் வழக்கில் (1996), பாரத ரத்னா மற்றும் பத்ம விருதுகள் பிரிவு 18-ன் கீழ் 'பட்டங்கள்' ஆகும் என்றும் அவை செல்லாதவை என்றும் உச்ச நீதிமன்றம் தீர்ப்பளித்தது.\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1 only", "1 மட்டும்",
    "2 only", "2 மட்டும்",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை",
    "A",
    "Statement 1 is correct (military and academic distinctions are allowed). Statement 2 is INCORRECT because in Balaji Raghavan case 1996, Supreme Court UPHELD the validity of National Awards (Bharat Ratna, Padma Awards) stating they are decorations, not titles under Art 18, provided they are not used as prefixes or suffixes.",
    "கூற்று 1 சரி (இராணுவ, கல்விச் சிறப்புகள் அனுமதிக்கப்படுகின்றன). கூற்று 2 தவறு, ஏனெனில் பாலாஜி ராகவன் வழக்கில் (1996) பாரத ரத்னா, பத்ம விருதுகள் 'பட்டங்கள்' அல்ல, கெளரவ விருதுகள் தான் எனக் கூறி உச்ச நீதிமன்றம் அவை செல்லுபடியாகும் எனத் தீர்ப்பளித்தது.",
    "Correct. Statement 1 is true; Statement 2 is false.", "சரி. கூற்று 1 சரி; கூற்று 2 தவறானது.",
    "Incorrect. Statement 1 is correct.", "தவறு. கூற்று 1 சரியானது.",
    "Incorrect. Statement 2 is false.", "தவறு. கூற்று 2 தவறானது.",
    "Incorrect. Statement 1 is correct.", "தவறு. கூற்று 1 சரியானது.",
    "TNPSC Trap: National Awards (Bharat Ratna, Padma awards) are constitutional decorations, but using them as prefix or suffix to awardee's name results in forfeiture of award.",
    "TNPSC பொறி: தேசிய விருதுகள் பட்டங்கள் அல்ல, ஆனால் அவற்றைப் பெயருக்கு முன்னாலோ பின்னாலோ பயன்படுத்தினால் விருதுகள் பறிக்கப்படலாம்.",
    "Article 18(2) prohibits a citizen of India from accepting any title from any foreign State.",
    "பிரிவு 18(2) ஒரு இந்தியக் குடிமகன் எந்தவொரு வெளிநாட்டிலிருந்தும் பட்டம் பெறுவதைத் தடை செய்கிறது.",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Article 18", "Abolition of Titles", "Two Statement"]
))

# FR_SB_011 (Easy)
questions.append(make_q(
    "FR_SB_011", "Easy",
    "Consider the following statements regarding Article 19 of the Indian Constitution:\n1. The six rights guaranteed under Article 19(1) are protected against only state action and not private individuals.\n2. The rights under Article 19 are available to both citizens of India and foreign nationals residing in India.\nWhich of the statements given above is/are correct?",
    "இந்திய அரசியலமைப்பின் 19-வது பிரிவைக் குறித்து பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. பிரிவு 19(1)-ன் கீழ் உத்தரவாதம் அளிக்கப்பட்ட ஆறு உரிமைகள் அரசின் நடவடிக்கைக்கு எதிராக மட்டுமே பாதுகாப்ப அளிக்கப்படுகின்றன, தனிநபர்களுக்கு எதிராக அல்ல.\n2. பிரிவு 19-ன் கீழ் உள்ள உரிமைகள் இந்தியக் குடிமக்கள் மற்றும் இந்தியாவில் வசிக்கும் வெளிநாட்டு குடிமக்கள் இருவருக்குமே கிடைக்கின்றன.\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1 only", "1 மட்டும்",
    "2 only", "2 மட்டும்",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை",
    "A",
    "Statement 1 is correct (Art 19 protects against State action only). Statement 2 is INCORRECT because Article 19 rights are guaranteed to CITIZENS ONLY, not to foreigners or legal entities like corporations.",
    "கூற்று 1 சரி (பிரிவு 19 அரசு நடவடிக்கைக்கு எதிராக மட்டுமே பாதுகாப்பு அளிக்கிறது). கூற்று 2 தவறு, ஏனெனில் பிரிவு 19 உரிமைகள் இந்தியக் குடிமக்களுக்கு மட்டுமே உரித்தானவை (வெளிநாட்டினருக்கு இல்லை).",
    "Correct. Statement 1 is true; Statement 2 is false as Art 19 applies to citizens only.", "சரி. கூற்று 1 சரி; பிரிவு 19 குடிமக்களுக்கு மட்டுமே என்பதால் கூற்று 2 தவறு.",
    "Incorrect. Statement 1 is correct.", "தவறு. கூற்று 1 சரியானது.",
    "Incorrect. Statement 2 is false.", "தவறு. கூற்று 2 தவறானது.",
    "Incorrect. Statement 1 is correct.", "தவறு. கூற்று 1 சரியானது.",
    "TNPSC Trap: Articles 15, 16, 19, 29, and 30 are available to CITIZENS ONLY. Foreigners cannot claim freedom of speech under Article 19.",
    "TNPSC பொறி: பிரிவுகள் 15, 16, 19, 29, மற்றும் 30 குடிமக்களுக்கு மட்டுமே கிடைப்பவை. வெளிநாட்டினர் பிரிவு 19-ன் கீழ் பேச்சு சுதந்திரத்தைக் கோர முடியாது.",
    "Right to Property under Article 19(1)(f) was deleted by the 44th Constitutional Amendment Act, 1978.",
    "பிரிவு 19(1)(f)-ன் கீழ் இருந்த சொத்துரிமை 44-வது அரசியலமைப்பு திருத்தச் சட்டம், 1978 மூலம் நீக்கப்பட்டது.",
    "Understand", 60, ["Polity", "Fundamental Rights", "Article 19", "Six Freedoms", "Two Statement"]
))

# FR_SB_012 (Medium)
questions.append(make_q(
    "FR_SB_012", "Medium",
    "Consider the following statements regarding Protection under Article 20 of the Indian Constitution:\n1. Protection against ex-post facto laws under Article 20(1) applies to both criminal and civil legislation including tax laws.\n2. Protection against self-incrimination under Article 20(3) extends to both oral evidence and mandatory blood or thumb impression samples.\nWhich of the statements given above is/are correct?",
    "இந்திய அரசியலமைப்பின் 20-வது பிரிவின் கீழ் உள்ள பாதுகாப்பு பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. பிரிவு 20(1)-ன் கீழ் பின்னோக்கிய விளைவு சட்டங்களுக்கு (ex-post facto laws) எதிரான பாதுகாப்பு குற்றவியல் மற்றும் வரிச் சட்டங்கள் உட்பட சிவில் சட்டங்கள் இரண்டிற்கும் பொருந்தும்.\n2. பிரிவு 20(3)-ன் கீழ் தங்களுக்குத் தாங்களே சாட்சியமளிப்பதற்கு எதிரான பாதுகாப்பு வாய்மொழிச் சான்றுகள் மற்றும் கட்டாய ரத்த மாதிரிகள்/பெருவிரல் ரேகைகள் இரண்டிற்கும் பொருந்தும்.\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1 only", "1 மட்டும்",
    "2 only", "2 மட்டும்",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை",
    "D",
    "Both statements are INCORRECT. Ex-post facto law protection (Art 20(1)) applies ONLY to criminal laws, NOT civil or tax laws. Self-incrimination protection (Art 20(3)) covers compulsory testimony/statements, NOT physical specimens like blood samples, thumb impressions, or specimen signatures (Kathi Kalu Oghad case 1961).",
    "இரண்டு கூற்றுகளும் தவறானவை. பிரிவு 20(1) குற்றவியல் சட்டங்களுக்கு மட்டுமே பொருந்தும் (சிவில்/வரிச் சட்டங்களுக்கு இல்லை). பிரிவு 20(3) வாய்மொழி/எழுத்துப்பூர்வ சாட்சியத்திற்கு மட்டுமே பொருந்தும் (ரத்த மாதிரி, விரல் ரேகைக்கு பொருந்தாது).",
    "Incorrect. Both statements are false.", "தவறு. இரண்டு கூற்றுகளும் தவறானவை.",
    "Incorrect. Both statements are false.", "தவறு. இரண்டு கூற்றுகளும் தவறானவை.",
    "Incorrect. Both statements are false.", "தவறு. இரண்டு கூற்றுகளும் தவறானவை.",
    "Correct. Neither statement 1 nor statement 2 is correct.", "சரி. கூற்று 1 மற்றும் கூற்று 2 ஆகிய இரண்டும் தவறானவை.",
    "TNPSC Trap: Article 20 protection extends to both citizens and foreigners. Double jeopardy (20(2)) applies only before judicial courts/tribunals, not departmental inquiries.",
    "TNPSC பொறி: இரட்டைத் தண்டனைத் தடை (20(2)) நீதிமன்றங்கள்/நீதிமன்ற தீர்ப்பாயங்களுக்கு மட்டுமே பொருந்தும், துறைசார் விசாரணைகளுக்கு அல்ல.",
    "Article 20 cannot be suspended even during a National Emergency declared under Article 352 (as amended by 44th CAA 1978).",
    "44-வது திருத்தத்திற்குப் பிறகு தேசிய அவசரநிலையின் போதும் பிரிவு 20-ஐ இடைநீக்கம் செய்ய முடியாது.",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Article 20", "Self-Incrimination", "Two Statement"]
))

# FR_SB_013 (Medium)
questions.append(make_q(
    "FR_SB_013", "Medium",
    "Consider the following statements regarding Article 21 of the Indian Constitution:\n1. In AK Gopalan case (1950), the Supreme Court gave a narrow interpretation of Article 21 adhering strictly to 'procedure established by law'.\n2. In Maneka Gandhi case (1978), the Supreme Court introduced the concept of 'due process of law', ruling that procedure must be just, fair, and reasonable.\nWhich of the statements given above is/are correct?",
    "இந்திய அரசியலமைப்பின் 21-வது பிரிவைக் குறித்து பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. ஏ.கே. கோபாலன் வழக்கில் (1950), உச்ச நீதிமன்றம் 'சட்டத்தால் அமைக்கப்பட்ட நடைமுறை' என்பதைக் குறுகிய நோக்கில் மட்டுமே பொருள் கொண்டது.\n2. மேனகா காந்தி வழக்கில் (1978), உச்ச நீதிமன்றம் 'சட்டத்தின் உரிய நடைமுறை' (due process of law) என்பதன் கருத்தை அறிமுகப்படுத்தி, நடைமுறை நியாயமானதாகவும், நேர்மையானதாகவும் இருக்க வேண்டும் எனத் தீர்ப்பளித்தது.\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1 only", "1 மட்டும்",
    "2 only", "2 மட்டும்",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை",
    "C",
    "Both statements are correct. AK Gopalan (1950) limited Art 21 to executive action only under 'procedure established by law'. Maneka Gandhi (1978) expanded Art 21 to protect against arbitrary legislative action as well, adopting American 'due process of law'.",
    "இரண்டு கூற்றுகளும் சரியானவை. ஏ.கே. கோபாலன் வழக்கு (1950) பிரிவு 21-ஐ குறுகலாகப் பார்த்தது. மேனகா காந்தி வழக்கு (1978) அமெரிக்காவின் 'சட்டத்தின் உரிய நடைமுறை' போல நடைமுறை நியாயமானதாக இருக்க வேண்டும் என்றது.",
    "Incorrect. Statement 2 is also correct.", "தவறு. கூற்று 2-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.", "தவறு. கூற்று 1-ம் சரியானது.",
    "Correct. Both Statements 1 and 2 are landmark milestones in Indian constitutional history.", "சரி. கூற்றுகள் 1 மற்றும் 2 இரண்டும் அரசியலமைப்பு வரலாற்றில் மைல்கற்கள்.",
    "Incorrect. Both statements are correct.", "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
    "TNPSC Trap: Article 21 applies to BOTH citizens and non-citizens (foreigners), and cannot be suspended during National Emergency.",
    "TNPSC பொறி: பிரிவு 21 குடிமக்கள் மற்றும் வெளிநாட்டினர் இருவருக்குமே பொருந்தும், மேலும் தேசிய அவசரநிலையின் போதும் இடைநீக்கம் செய்ய முடியாது.",
    "Right to Privacy was recognized as an intrinsic part of Right to Life under Article 21 in K.S. Puttaswamy case (2017).",
    "கே.எஸ். புட்டசுவாமி வழக்கில் (2017) தனியுரிமை (Privacy) பிரிவு 21-ன் கீழ் அடிப்படை உரிமையாக அங்கீகரிக்கப்பட்டது.",
    "Understand", 60, ["Polity", "Fundamental Rights", "Article 21", "Maneka Gandhi Case", "Two Statement"]
))

# FR_SB_014 (Easy)
questions.append(make_q(
    "FR_SB_014", "Easy",
    "Consider the following statements regarding Article 21A of the Indian Constitution:\n1. Article 21A was inserted into the Constitution by the 86th Constitutional Amendment Act, 2002.\n2. It makes free and compulsory education a Fundamental Right for all children of the age group 6 to 14 years.\nWhich of the statements given above is/are correct?",
    "இந்திய அரசியலமைப்பின் 21A பிரிவைக் குறித்து பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 86-வது அரசியலமைப்பு திருத்தச் சட்டம், 2002 மூலம் அரசியலமைப்பில் பிரிவு 21A சேர்க்கப்பட்டது.\n2. இது 6 முதல் 14 வயதுக்குட்பட்ட அனைத்து குழந்தைகளுக்கும் இலவச மற்றும் கட்டாயக் கல்வியை அடிப்படை உரிமையாக்குகிறது.\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1 only", "1 மட்டும்",
    "2 only", "2 மட்டும்",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை",
    "C",
    "Both statements are correct. 86th CAA 2002 added Art 21A making free & compulsory education for children aged 6-14 a Fundamental Right. The Right of Children to Free and Compulsory Education (RTE) Act was enacted in 2009 and came into force on April 1, 2010.",
    "இரண்டு கூற்றுகளும் சரியானவை. 86வது திருத்தம் 2002 மூலம் பிரிவு 21A சேர்க்கப்பட்டு 6-14 வயது குழந்தைகளுக்கு கல்வி அடிப்படை உரிமையாக்கப்பட்டது. RTE சட்டம் 2009-ல் இயற்றப்பட்டு ஏப்ரல் 1, 2010 முதல் அமலுக்கு வந்தது.",
    "Incorrect. Statement 2 is also correct.", "தவறு. கூற்று 2-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.", "தவறு. கூற்று 1-ம் சரியானது.",
    "Correct. Both Statements 1 and 2 are true.", "சரி. கூற்றுகள் 1 மற்றும் 2 இரண்டும் உண்மை.",
    "Incorrect. Both statements are correct.", "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
    "TNPSC Trap: Article 21A covers children aged 6 to 14 ONLY. Education for children below 6 years is covered under DPSP Article 45.",
    "TNPSC பொறி: பிரிவு 21A 6 முதல் 14 வயது வரை மட்டுமே பொருந்தும். 6 வயதுக்குட்பட்ட குழந்தைகளுக்கான கல்வி பிரிவு 45 DPSP-ன் கீழ் வருகிறது.",
    "86th CAA 2002 changed Article 45 in DPSP and added a new Fundamental Duty under Article 51A(k).",
    "86-வது திருத்தம் 2002 பிரிவு 45 DPSP-ஐ மாற்றியமைத்ததுடன் 51A(k)-ன் கீழ் புதிய அடிப்படை கடமையையும் சேர்த்தது.",
    "Understand", 60, ["Polity", "Fundamental Rights", "Article 21A", "Right to Education", "Two Statement"]
))

# FR_SB_015 (Medium)
questions.append(make_q(
    "FR_SB_015", "Medium",
    "Consider the following statements regarding Preventive Detention safeguards under Article 22 of the Indian Constitution:\n1. The protection of Article 22(1) and 22(2) regarding right to be informed of grounds of arrest and produced before a magistrate within 24 hours is NOT available to enemy aliens or persons detained under preventive detention laws.\n2. The 44th Constitutional Amendment Act, 1978 reduced the period of detention without Advisory Board approval from 3 months to 2 months, and this provision has been fully implemented.\nWhich of the statements given above is/are correct?",
    "இந்திய அரசியலமைப்பின் 22-வது பிரிவின் கீழ் உள்ள தடுப்புக்காவல் பாதுகாப்புகள் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. கைது செய்ததற்கான காரணங்களை அறிவித்தல் மற்றும் 24 மணி நேரத்திற்குள் நடுவர் முன் ஆஜர்படுத்துதல் ஆகிய பிரிவு 22(1) மற்றும் 22(2)-ன் பாதுகாப்புகள் எதிரி நாட்டின் வேற்றுகிரகவாசிகளுக்கோ (enemy aliens) அல்லது தடுப்புக்காவலில் உள்ளவர்களுக்கோ கிடைக்காது.\n2. 44-வது அரசியலமைப்பு திருத்தச் சட்டம் 1978, ஆலோசனைக் குழுவின் ஒப்புதலின்றி தடுப்புக்காவல் காலத்தை 3 மாதங்களிலிருந்து 2 மாதங்களாகக் குறைத்தது, மேலும் இந்த விதி முழுமையாக அமல்படுத்தப்பட்டுள்ளது.\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1 only", "1 மட்டும்",
    "2 only", "2 மட்டும்",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை",
    "A",
    "Statement 1 is correct (enemy aliens and preventive detainees are excluded from Art 22(1) & (2) procedural safeguards). Statement 2 is INCORRECT because although the 44th CAA 1978 reduced the detention period from 3 months to 2 months, THIS AMENDMENT HAS NOT BEEN BROUGHT INTO FORCE, so 3 months remains the effective constitutional limit.",
    "கூற்று 1 சரி (எதிரி நாட்டு மக்கள் மற்றும் தடுப்புக்காவலர்களுக்கு பிரிவு 22(1)&(2) உரிமைகள் கிடைக்காது). கூற்று 2 தவறு, ஏனெனில் 44-வது திருத்தம் 1978 காலத்தை 2 மாதமாகக் குறைக்க முன்மொழிந்த போதிலும், அந்த விதி இதுவரை நடைமுறைக்கு வரவில்லை; 3 மாதமே இப்போதும் நடைமுறையில் உள்ளது.",
    "Correct. Statement 1 is true; Statement 2 is false as the 2-month reduction was never notified.", "சரி. கூற்று 1 சரி; 2 மாதக் குறைப்பு அறிவிக்கப்படாததால் கூற்று 2 தவறு.",
    "Incorrect. Statement 1 is correct.", "தவறு. கூற்று 1 சரியானது.",
    "Incorrect. Statement 2 is false.", "தவறு. கூற்று 2 தவறானது.",
    "Incorrect. Statement 1 is correct.", "தவறு. கூற்று 1 சரியானது.",
    "TNPSC Trap: The 44th CAA 1978 reduction of preventive detention from 3 months to 2 months HAS NEVER BEEN NOTIFIED or brought into force till date.",
    "TNPSC பொறி: 44-வது திருத்தம் தடுப்புக்காவலை 3 மாதங்களிலிருந்து 2 மாதமாகக் குறைத்த விதி இதுவரை அரசிதழில் அறிவிக்கப்பட்டு நடைமுறைக்கு வரவில்லை.",
    "Article 22(7) authorizes Parliament alone to prescribe cases and maximum period for preventive detention.",
    "பிரிவு 22(7) தடுப்புக்காவலுக்கான அதிகபட்ச காலத்தை நிர்ணயிக்க நாடாளுமன்றத்திற்கு மட்டுமே அதிகாரம் அளிக்கிறது.",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Article 22", "Preventive Detention", "Two Statement"]
))

# Save checkpoint for Part 1
print(f"Added {len(questions)} Two-Statement questions.")

# ==============================================================================
# PART 2: 15 THREE-STATEMENT QUESTIONS (FR_SB_016 to FR_SB_030)
# ==============================================================================

# FR_SB_016 (Easy)
questions.append(make_q(
    "FR_SB_016", "Easy",
    "Consider the following statements regarding Articles 23 and 24 of the Indian Constitution (Right against Exploitation):\n1. Article 23 prohibits human trafficking, begar, and other forced labor, and protects against both State and private individuals.\n2. Article 23 permits the State to impose compulsory service for public purposes without discrimination on grounds of religion, race, caste, or class.\n3. Article 24 prohibits the employment of children below 14 years in all forms of employment without exception.\nWhich of the statements given above are correct?",
    "இந்திய அரசியலமைப்பின் 23 மற்றும் 24 ஆகிய பிரிவுகள் (சுரண்டலுக்கு எதிரான உரிமை) பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. பிரிவு 23 மனித வர்த்தகம், வெட்டி வேலை (begar) மற்றும் கட்டாய வேலையைத் தடை செய்கிறது, மேலும் அரசு மற்றும் தனிநபர்கள் இருவருக்கு எதிராகவுமே பாதுகாப்பு அளிக்கிறது.\n2. பிரிவு 23 மதம், இனம், சாதி அல்லது வகுப்பின் அடிப்படையில் பாகுபாடின்றி பொது நோக்கங்களுக்காக கட்டாய சேவையை விதிக்க அரசுக்கு அனுமதிக்கிறது.\n3. பிரிவு 24 14 வயதுக்குட்பட்ட குழந்தைகளை எந்தவொரு விலக்குமின்றி அனைத்து வகையான வேலைகளிலும் ஈடுபடுத்துவதைத் தடை செய்கிறது.\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "A",
    "Statements 1 and 2 are correct. Statement 3 is INCORRECT because Article 24 specifically prohibits employment of children below 14 in HAZARDOUS employment (factories, mines, construction). The Child Labour Act was amended in 2016 to allow children to help in family enterprises after school hours.",
    "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறு, ஏனெனில் பிரிவு 24 அபாயகரமான வேலைகளில் (தொழிற்சாலைகள், சுரங்கங்கள்) மட்டுமே 14 வயதுக்குட்பட்ட குழந்தைகளைத் தடை செய்கிறது. 2016 திருத்தச் சட்டம் குடும்பத் தொழில்களில் பள்ளி நேரத்திற்குப் பின் உதவ அனுமதிக்கிறது.",
    "Correct. Statements 1 and 2 are true; Statement 3 is false.", "சரி. கூற்றுகள் 1 மற்றும் 2 சரி; கூற்று 3 தவறானது.",
    "Incorrect. Statement 3 is false.", "தவறு. கூற்று 3 தவறானது.",
    "Incorrect. Statement 3 is false.", "தவறு. கூற்று 3 தவறானது.",
    "Incorrect. Statement 3 is false.", "தவறு. கூற்று 3 தவறானது.",
    "TNPSC Trap: Article 23 allows State to impose compulsory public service (e.g. military/social service), provided NO discrimination is made on grounds of religion, race, caste or class (Sex is not mentioned here).",
    "TNPSC பொறி: பிரிவு 23 கட்டாய பொது சேவையை விதிக்க அரசுக்கு அனுமதிக்கிறது, ஆனால் மதம், இனம், சாதி, வகுப்பு அடிப்படையில் பாகுபாடு காட்டக்கூடாது (பாலினம் குறிப்பிடப்படவில்லை).",
    "Child Labour (Prohibition and Regulation) Amendment Act, 2016 introduced complete prohibition on employment of children below 14 in all occupations and adolescent (14-18) in hazardous occupations.",
    "2016 குழந்தைத் தொழிலாளர் திருத்தச் சட்டம் 14 வயதுக்குட்பட்ட குழந்தைகளை அனைத்து தொழில்களிலும், 14-18 வயதுடையோரை அபாயகரமான தொழில்களிலும் தடை செய்தது.",
    "Understand", 60, ["Polity", "Fundamental Rights", "Article 23", "Article 24", "Three Statement"]
))

# FR_SB_017 (Medium)
questions.append(make_q(
    "FR_SB_017", "Medium",
    "Consider the following statements regarding Article 25 of the Indian Constitution:\n1. Article 25 guarantees freedom of conscience and the right to freely profess, practice, and propagate religion.\n2. The right to propagate religion includes the fundamental right to convert another person to one's own religion.\n3. The rights under Article 25 are subject to public order, morality, health, and other Fundamental Rights in Part III.\nWhich of the statements given above are correct?",
    "இந்திய அரசியலமைப்பின் 25-வது பிரிவைக் குறித்து பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. பிரிவு 25 மனசாட்சி சுதந்திரத்தையும், மதத்தைப் பரப்பவும், பின்பற்றவும், பிரச்சாரம் செய்யவும் உரிமையையும் உத்தரவாதம் செய்கிறது.\n2. மதத்தைப் பிரச்சாரம் செய்யும் உரிமை, மற்றொரு நபரைத் தனது சொந்த மதத்திற்கு வலுக்கட்டாயமாக மாற்றும் அடிப்படை உரிமையையும் உள்ளடக்கியது.\n3. பிரிவு 25-ன் கீழ் உள்ள உரிமைகள் பொது ஒழுங்கு, நன்னடத்தை, சுகாதாரம் மற்றும் பகுதி III-ல் உள்ள பிற அடிப்படை உரிமைகளுக்கு உட்பட்டவை.\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "B",
    "Statements 1 and 3 are correct. Statement 2 is INCORRECT because Supreme Court in Rev Stainislaus case (1977) held that right to propagate does NOT include the right to convert another person, as forced conversion violates freedom of conscience of the converted person.",
    "கூற்றுகள் 1 மற்றும் 3 சரியானவை. கூற்று 2 தவறு, ஏனெனில் ஸ்டைனிஸ்லாஸ் வழக்கில் (1977) மதத்தைப் பிரச்சாரம் செய்யும் உரிமை மற்றொருவரை மதமாற்றம் செய்யும் உரிமையை உள்ளடக்காது என உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
    "Incorrect. Statement 2 is false.", "தவறு. கூற்று 2 தவறானது.",
    "Correct. Statements 1 and 3 are true; Statement 2 is false.", "சரி. கூற்றுகள் 1 மற்றும் 3 சரி; கூற்று 2 தவறானது.",
    "Incorrect. Statement 2 is false.", "தவறு. கூற்று 2 தவறானது.",
    "Incorrect. Statement 2 is false.", "தவறு. கூற்று 2 தவறானது.",
    "TNPSC Trap: Article 25(2)(b) specifically defines 'Hindus' for religious institution entry purposes to include Sikhs, Jains, and Buddhists.",
    "TNPSC பொறி: பிரிவு 25(2)(b)-ன் கீழ் இந்து மத நிறுவனங்களில் நுழைவது குறித்த நோக்கத்திற்கு சீக்கியர்கள், ஜைனர்கள் மற்றும் பௌத்தர்களும் 'இந்துக்கள்' என்ற வரையறைக்குள் அடங்குவர்.",
    "Article 25 guarantees individual religious freedom, whereas Article 26 guarantees collective religious rights.",
    "பிரிவு 25 தனிநபர் மத சுதந்திரத்தையும், பிரிவு 26 குழும மத உரிமைகளையும் உத்தரவாதம் செய்கிறது.",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Article 25", "Religious Freedom", "Three Statement"]
))

# FR_SB_018 (Medium)
questions.append(make_q(
    "FR_SB_018", "Medium",
    "Consider the following statements regarding Article 26 (Freedom to Manage Religious Affairs):\n1. Article 26 guarantees every religious denomination the right to establish and maintain institutions for religious and charitable purposes.\n2. A religious denomination has the absolute right to administer its property without any interference by State laws.\n3. According to the Supreme Court, a religious denomination must satisfy three conditions: common faith, common organization, and a distinctive name.\nWhich of the statements given above are correct?",
    "பிரிவு 26 (மத விவகாரங்களை நிர்வகிக்கும் சுதந்திரம்) பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. பிரிவு 26 ஒவ்வொரு மதப் பிரிவிற்கும் (religious denomination) மத மற்றும் தொண்டு நோக்கங்களுக்காக நிறுவனங்களை நிறுவி பராமரிக்கும் உரிமையை உத்தரவாதம் செய்கிறது.\n2. ஒரு மதப் பிரிவு தனது சொத்துக்களை அரசின் சட்டங்களின் எந்தவொரு தலையீடும் இன்றி நிர்வகிக்க முழுமையான உரிமை கொண்டுள்ளது.\n3. உச்ச நீதிமன்றத்தின் கூற்றுப்படி, ஒரு மதப் பிரிவு மூன்று நிபந்தனைகளை பூர்த்தி செய்ய வேண்டும்: பொதுவான நம்பிக்கை, பொதுவான அமைப்பு மற்றும் தனித்துவமான பெயர்.\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "B",
    "Statements 1 and 3 are correct. Statement 2 is INCORRECT because Article 26(d) provides that the right to administer property is to be exercised 'in accordance with law', meaning the State can regulate the administration of property through statutory laws.",
    "கூற்றுகள் 1 மற்றும் 3 சரியானவை. கூற்று 2 தவறு, ஏனெனில் பிரிவு 26(d)-ன் கீழ் சொத்துக்களை நிர்வகிக்கும் உரிமை 'சட்டத்திற்கு உட்பட்டே' மேற்கொள்ளப்பட வேண்டும்; அரசு சட்டத்தின் மூலம் அதை முறைப்படுத்தலாம்.",
    "Incorrect. Statement 2 is false.", "தவறு. கூற்று 2 தவறானது.",
    "Correct. Statements 1 and 3 are true; Statement 2 is false.", "சரி. கூற்றுகள் 1 மற்றும் 3 சரி; கூற்று 2 தவறானது.",
    "Incorrect. Statement 2 is false.", "தவறு. கூற்று 2 தவறானது.",
    "Incorrect. Statement 2 is false.", "தவறு. கூற்று 2 தவறானது.",
    "TNPSC Trap: Under Art 26, the right to manage religious affairs (Art 26(b)) is absolute, but the right to administer property (Art 26(d)) is qualified and subject to State law.",
    "TNPSC பொறி: பிரிவு 26-ன் கீழ் மத விவகாரங்களை நிர்வகிக்கும் உரிமை (26(b)) முழுமையானது, ஆனால் சொத்துக்களை நிர்வகிக்கும் உரிமை (26(d)) அரசு சட்டத்திற்கு உட்பட்டது.",
    "The Supreme Court held in SP Mittal case (1981) that Aurobindo Society is NOT a religious denomination.",
    "எஸ்.பி. மிட்டல் வழக்கில் (1981) அரவிந்தர் சங்கம் (Aurobindo Society) ஒரு மதப் பிரிவு அல்ல என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Article 26", "Religious Denomination", "Three Statement"]
))

# FR_SB_019 (Medium)
questions.append(make_q(
    "FR_SB_019", "Medium",
    "Consider the following statements regarding Articles 27 and 28 of the Indian Constitution:\n1. Article 27 prohibits the State from levying any tax where the proceeds are specifically appropriated for the promotion of any particular religion.\n2. Article 27 prohibits the levy of both taxes and fees for religious purposes.\n3. Article 28(1) completely prohibits religious instruction in educational institutions wholly maintained out of State funds.\nWhich of the statements given above are correct?",
    "இந்திய அரசியலமைப்பின் 27 மற்றும் 28 ஆகிய பிரிவுகள் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. பிரிவு 27 ஒரு குறிப்பிட்ட மதத்தைப் பரப்புவதற்காக வரித் தொகையைப் பயன்படுத்துவதைத் தடை செய்கிறது.\n2. பிரிவு 27 மத நோக்கங்களுக்காக வரிகள் மற்றும் கட்டணங்கள் (fees) இரண்டையுமே விதிக்கத் தடை விதிக்கிறது.\n3. பிரிவு 28(1) மாநில நிதியிலிருந்து முழுமையாகப் பராமரிக்கப்படும் கல்வி நிறுவனங்களில் மதக் கல்வி வழங்குவதை முற்றிலுமாகத் தடை செய்கிறது.\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "B",
    "Statements 1 and 3 are correct. Statement 2 is INCORRECT because Article 27 prohibits ONLY taxes, NOT fees. The State can levy a fee on pilgrims or religious institutions to provide secular services or safety arrangements.",
    "கூற்றுகள் 1 மற்றும் 3 சரியானவை. கூற்று 2 தவறு, ஏனெனில் பிரிவு 27 வரிகளை (taxes) மட்டுமே தடை செய்கிறது, கட்டணங்களை (fees) அல்ல. யாத்ரீகர்களுக்கு பாதுகாப்பு வழங்க கட்டணம் வசூலிக்கலாம்.",
    "Incorrect. Statement 2 is false.", "தவறு. கூற்று 2 தவறானது.",
    "Correct. Statements 1 and 3 are true; Statement 2 is false as fees are allowed under Art 27.", "சரி. கூற்றுகள் 1 மற்றும் 3 சரி; பிரிவு 27-ன் கீழ் கட்டணங்கள் அனுமதிக்கப்படுவதால் கூற்று 2 தவறு.",
    "Incorrect. Statement 2 is false.", "தவறு. கூற்று 2 தவறானது.",
    "Incorrect. Statement 2 is false.", "தவறு. கூற்று 2 தவறானது.",
    "TNPSC Trap: Article 27 bars TAXATION for promotion of religion, but FEES can be levied to collect revenue for secular service/regulation.",
    "TNPSC பொறி: பிரிவு 27 மத வளர்ச்சிக்கான வரியைத் தடை செய்கிறது, ஆனால் மதச் சுற்றுலா போன்றவற்றிற்குச் சேவைக் கட்டணம் விதிக்கப்படலாம்.",
    "Under Article 28, educational institutions established under a trust requiring religious instruction (even if administered by State) CAN impart religious education.",
    "அரசாங்கத்தால் நிர்வகிக்கப்பட்டாலும், அறக்கட்டளையால் நிறுவப்பட்ட கல்வி நிறுவனங்களில் மதக் கல்வி வழங்கப்படலாம்.",
    "Understand", 60, ["Polity", "Fundamental Rights", "Article 27", "Article 28", "Three Statement"]
))

# FR_SB_020 (Medium)
questions.append(make_q(
    "FR_SB_020", "Medium",
    "Consider the following statements regarding Cultural and Educational Rights (Articles 29 and 30):\n1. Article 29 grants protection to any section of citizens residing in India having a distinct language, script, or culture.\n2. Article 30 grants minority rights exclusively to religious and linguistic minorities.\n3. The term 'Minority' is clearly defined in Article 30 of the Indian Constitution.\nWhich of the statements given above are correct?",
    "பண்பாட்டு மற்றும் கல்வி உரிமைகள் (பிரிவுகள் 29 மற்றும் 30) பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. பிரிவு 29 தனித்துவமான மொழி, எழுத்து வடிவம் அல்லது கலாச்சாரத்தைக் கொண்ட இந்தியாவில் வசிக்கும் குடிமக்களின் எந்தவொரு பிரிவிற்கும் பாதுகாப்பு அளிக்கிறது.\n2. பிரிவு 30 சிறுபான்மையினருக்கான உரிமைகளை மத மற்றும் மொழி சிறுபான்மையினருக்கு மட்டுமே பிரத்யேகமாக வழங்குகிறது.\n3. 'சிறுபான்மையினர்' (Minority) என்ற சொல் இந்திய அரசியலமைப்பின் பிரிவு 30-ல் தெளிவாக வரையறுக்கப்பட்டுள்ளது.\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "A",
    "Statements 1 and 2 are correct. Statement 3 is INCORRECT because the term 'Minority' is NOT defined anywhere in the Indian Constitution.",
    "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறு, ஏனெனில் 'சிறுபான்மையினர்' என்ற சொல் இந்திய அரசியலமைப்பில் எங்குமே வரையறுக்கப்படவில்லை.",
    "Correct. Statements 1 and 2 are true; Statement 3 is false.", "சரி. கூற்றுகள் 1 மற்றும் 2 சரி; கூற்று 3 தவறானது.",
    "Incorrect. Statement 3 is false.", "தவறு. கூற்று 3 தவறானது.",
    "Incorrect. Statement 3 is false.", "தவறு. கூற்று 3 தவறானது.",
    "Incorrect. Statement 3 is false.", "தவறு. கூற்று 3 தவறானது.",
    "TNPSC Trap: Article 29 covers BOTH majority and minority sections (uses 'any section of citizens'), whereas Article 30 is restricted ONLY to minorities (religious & linguistic).",
    "TNPSC பொறி: பிரிவு 29 பெரும்பான்மையினர் மற்றும் சிறுபான்மையினர் இருவருக்குமே பொருந்தும் ('குடிமக்களின் எந்தவொரு பிரிவும்'), ஆனால் பிரிவு 30 சிறுபான்மையினருக்கு மட்டுமே பொருந்தும்.",
    "The Supreme Court in TMA Pai Foundation case (2002) held that unit for determining religious or linguistic minority is the STATE, not the whole of India.",
    "டி.எம்.ஏ பை அறக்கட்டளை வழக்கில் (2002) மத அல்லது மொழி சிறுபான்மையினரைத் தீர்மானிக்கும் அலகு 'மாநிலம்' ஆகும் என உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Article 29", "Article 30", "Minority Definition", "Three Statement"]
))

# FR_SB_021 (Hard)
questions.append(make_q(
    "FR_SB_021", "Hard",
    "Consider the following statements regarding Right to Property and Ninth Schedule:\n1. Right to Property was removed from Part III of the Constitution by the 44th Constitutional Amendment Act, 1978 and made a legal right under Article 300A.\n2. Article 31B immunizes laws placed in the Ninth Schedule from being challenged on ground of violation of any Fundamental Rights.\n3. In the IR Coelho case (2007), the Supreme Court ruled that laws included in the Ninth Schedule after April 24, 1973 are open to judicial review if they violate Basic Structure.\nWhich of the statements given above are correct?",
    "சொத்துரிமை மற்றும் ஒன்பதாவது அட்டவணை பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 44-வது அரசியலமைப்பு திருத்தச் சட்டம் 1978 மூலம் சொத்துரிமை பகுதி III-லிருந்து நீக்கப்பட்டு பிரிவு 300A-ன் கீழ் சட்டப்பூர்வ உரிமையாக்கப்பட்டது.\n2. பிரிவு 31B ஒன்பதாவது அட்டவணையில் சேர்க்கப்படும் சட்டங்களை எந்தவொரு அடிப்படை உரிமையையும் மீறுகின்றன என்ற அடிப்படையில் சவால் செய்வதிலிருந்து பாதுகாக்கிறது.\n3. ஐ.ஆர். கோயல்ஹோ வழக்கில் (2007), 1973 ஏப்ரல் 24-க்குப் பிறகு 9-வது அட்டவணையில் சேர்க்கப்பட்ட சட்டங்கள் அடிப்படை அமைப்பை மீறினால் நீதித்துறை மறுஆய்வுக்கு உட்பட்டவை என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது.\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "D",
    "All three statements are correct. 44th CAA 1978 moved property right to Art 300A in Part XII. Art 31B protects Ninth Schedule laws. IR Coelho case (2007) fixed April 24, 1973 (Kesavananda verdict date) as the cutoff after which Ninth Schedule laws are subject to Basic Structure review.",
    "மூன்று கூற்றுகளும் சரியானவை. 44-வது திருத்தம் சொத்துரிமையை பிரிவு 300A-க்கு மாற்றியது. பிரிவு 31B 9வது அட்டவணையைப் பாதுகாக்கிறது. ஐ.ஆர். கோயல்ஹோ வழக்கு (2007) 1973 ஏப்ரல் 24-க்கு பிந்தைய சட்டங்கள் நீதித்துறை மறுஆய்வுக்கு உட்பட்டவை என்றது.",
    "Incorrect. Statement 3 is also correct.", "தவறு. கூற்று 3-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.", "தவறு. கூற்று 1-ம் சரியானது.",
    "Incorrect. Statement 2 is also correct.", "தவறு. கூற்று 2-ம் சரியானது.",
    "Correct. All Statements 1, 2 and 3 are constitutionally true.", "சரி. கூற்றுகள் 1, 2 மற்றும் 3 அனைத்தும் உண்மை.",
    "TNPSC Trap: Article 300A property right is a Legal/Constitutional Right, NOT a Fundamental Right. Remedial writ petition lies under Art 226 in High Court, not Art 32 in Supreme Court.",
    "TNPSC பொறி: பிரிவு 300A சொத்துரிமை என்பது சட்டப்பூர்வ உரிமை, அடிப்படை உரிமை அல்ல. இதற்கு பிரிவு 226-ன் கீழ் உயர் நீதிமன்றத்தில் மட்டுமே மனு தாக்கல் செய்ய முடியும்.",
    "Article 31A, 31B and 31C were added as exceptions to Fundamental Rights to facilitate agrarian reforms and land acquisition.",
    "பிரிவுகள் 31A, 31B மற்றும் 31C ஆகியவை நிலச் சீர்திருத்தங்களை எளிதாக்க அடிப்படை உரிமைகளுக்கான விதிவிலக்குகளாகச் சேர்க்கப்பட்டன.",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Article 31B", "IR Coelho Case", "Article 300A", "Three Statement"]
))

# FR_SB_022 (Easy)
questions.append(make_q(
    "FR_SB_022", "Easy",
    "Consider the following statements regarding Article 32 of the Indian Constitution:\n1. Dr. B.R. Ambedkar called Article 32 the 'very soul of the Constitution and the very heart of it'.\n2. The right to move the Supreme Court for enforcement of Fundamental Rights under Article 32 is itself a Fundamental Right.\n3. The Supreme Court can refuse to exercise its writ jurisdiction under Article 32 on the ground of availability of an alternative remedy.\nWhich of the statements given above are correct?",
    "இந்திய அரசியலமைப்பின் 32-வது பிரிவைக் குறித்து பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. டாக்டர் பி.ஆர். அம்பேத்கர் பிரிவு 32-ஐ 'அரசியலமைப்பின் ஆன்மா மற்றும் அதன் இதயம்' என்று அழைத்தார்.\n2. அடிப்படை உரிமைகளை அமல்படுத்துவதற்காக உச்ச நீதிமன்றத்தை அணுகும் பிரிவு 32-ன் கீழ் உள்ள உரிமை தானே ஒரு அடிப்படை உரிமையாகும்.\n3. மாற்று தீர்வு (alternative remedy) உள்ளது என்ற காரணத்தைக் கூறி பிரிவு 32-ன் கீழ் தனது பேராணை அதிகாரத்தைப் பயன்படுத்த உச்ச நீதிமன்றம் மறுக்கலாம்.\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "A",
    "Statements 1 and 2 are correct. Statement 3 is INCORRECT because Supreme Court's jurisdiction under Article 32 is mandatory as Art 32 is itself a Fundamental Right. The Court CANNOT refuse to exercise its jurisdiction on ground of alternative remedy.",
    "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறு, ஏனெனில் பிரிவு 32 தானே ஒரு அடிப்படை உரிமை என்பதால், மாற்று தீர்வு உள்ளது என்று கூறி மனுவை விசாரிக்க உச்ச நீதிமன்றம் மறுக்க முடியாது.",
    "Correct. Statements 1 and 2 are true; Statement 3 is false.", "சரி. கூற்றுகள் 1 மற்றும் 2 சரி; கூற்று 3 தவறானது.",
    "Incorrect. Statement 3 is false.", "தவறு. கூற்று 3 தவறானது.",
    "Incorrect. Statement 3 is false.", "தவறு. கூற்று 3 தவறானது.",
    "Incorrect. Statement 3 is false.", "தவறு. கூற்று 3 தவறானது.",
    "TNPSC Trap: Under Article 32, Supreme Court can issue writs ONLY for Fundamental Rights enforcement, NOT for ordinary legal rights.",
    "TNPSC பொறி: பிரிவு 32-ன் கீழ் உச்ச நீதிமன்றம் அடிப்படை உரிமைகளை அமல்படுத்த மட்டுமே பேராணைகளை வெளியிட முடியும், சாதாரண சட்டப்பூர்வ உரிமைகளுக்கு அல்ல.",
    "Article 32 is a part of the Basic Structure of the Constitution and cannot be abridged even by a Constitutional Amendment.",
    "பிரிவு 32 அரசியலமைப்பின் அடிப்படை அமைப்பின் ஒரு பகுதியாகும், மேலும் இதை அரசியலமைப்பு திருத்தத்தின் மூலமும் குறைக்க முடியாது.",
    "Understand", 60, ["Polity", "Fundamental Rights", "Article 32", "Constitutional Remedies", "Three Statement"]
))

# FR_SB_023 (Easy)
questions.append(make_q(
    "FR_SB_023", "Easy",
    "Consider the following statements regarding Writs of Habeas Corpus and Mandamus:\n1. Habeas Corpus can be issued against both public authorities and private individuals.\n2. Mandamus can be issued against a private individual or private body to enforce a private right.\n3. Mandamus cannot be issued against the President of India or State Governors for performance of official duties.\nWhich of the statements given above are correct?",
    "ஆட்கொணர்வுப் பேராணை (Habeas Corpus) மற்றும் கட்டளைப் பேராணை (Mandamus) பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. ஆட்கொணர்வுப் பேராணையை பொது அதிகாரிகள் மற்றும் தனிநபர்கள் இருவருக்கு எதிராகவுமே வெளியிடலாம்.\n2. ஒரு தனிநபரின் உரிமையை அமல்படுத்த கட்டளைப் பேராணையை ஒரு தனியார் நபர் அல்லது தனியார் அமைப்பிற்கு எதிராக வெளியிடலாம்.\n3. இந்தியக் குடியரசுத் தலைவர் அல்லது மாநில ஆளுநர்களுக்கு எதிராக அவர்களின் அதிகாரப்பூர்வ பணிகளுக்காக கட்டளைப் பேராணையை வெளியிட முடியாது.\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "B",
    "Statements 1 and 3 are correct. Statement 2 is INCORRECT because Mandamus literally means 'We Command' and is issued to perform a PUBLIC or STATUTORY duty. It CANNOT be issued against a private individual or private entity.",
    "கூற்றுகள் 1 மற்றும் 3 சரியானவை. கூற்று 2 தவறு, ஏனெனில் கட்டளைப் பேராணை (Mandamus) பொது அல்லது சட்டப்பூர்வ கடமையை நிறைவேற்ற மட்டுமே வெளியிடப்படும். தனியார் நபருக்கு எதிராக வெளியிட முடியாது.",
    "Incorrect. Statement 2 is false.", "தவறு. கூற்று 2 தவறானது.",
    "Correct. Statements 1 and 3 are true; Statement 2 is false.", "சரி. கூற்றுகள் 1 மற்றும் 3 சரி; கூற்று 2 தவறானது.",
    "Incorrect. Statement 2 is false.", "தவறு. கூற்று 2 தவறானது.",
    "Incorrect. Statement 2 is false.", "தவறு. கூற்று 2 தவறானது.",
    "TNPSC Trap: Habeas Corpus is the ONLY writ that can be issued against PRIVATE individuals as well as public authorities.",
    "TNPSC பொறி: ஆட்கொணர்வுப் பேராணை (Habeas Corpus) மட்டுமே பொது அதிகாரிகளுக்கும் தனியார் தனிநபர்களுக்கும் எதிராக வெளியிடப்படக்கூடிய ஒரே பேராணையாகும்.",
    "Mandamus lies to compel a public official who has failed or refused to perform his mandatory public duty.",
    "தனது சட்டப்பூர்வ பொதுக் கடமையைச் செய்யத் தவறிய பொது அதிகாரியைப் பணி செய்ய வற்புறுத்த கட்டளைப் பேராணை பயன்படுகிறது.",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Habeas Corpus", "Mandamus", "Writs", "Three Statement"]
))

# FR_SB_024 (Medium)
questions.append(make_q(
    "FR_SB_024", "Medium",
    "Consider the following statements regarding Writs of Prohibition and Certiorari:\n1. Prohibition is available during the pendency of proceedings (preventive only), whereas Certiorari is issued after order is passed (both preventive and curative).\n2. Until 1991, Certiorari could be issued only against judicial and quasi-judicial bodies, but post-1991, it can also be issued against administrative authorities.\n3. Both Prohibition and Certiorari can be issued against legislative bodies and private individuals.\nWhich of the statements given above are correct?",
    "தடைஉத்தரவுப் பேராணை (Prohibition) மற்றும் சான்றாய்வுப் பேராணை (Certiorari) பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. வழக்கு நிலுவையில் இருக்கும்போது மட்டுமே தடைஉத்தரவுப் பேராணை (தடுப்பு மட்டுமே) வெளியிடப்படும்; ஆனால் உத்தரவு பிறப்பிக்கப்பட்ட பிறகு சான்றாய்வுப் பேராணை (தடுப்பு மற்றும் நிவாரணம்) வெளியிடப்படும்.\n2. 1991 வரை, சான்றாய்வுப் பேராணை நீதி மற்றும் நீதி போன்ற அமைப்புகளுக்கு எதிராக மட்டுமே வெளியிடப்பட்டது; ஆனால் 1991க்குப் பிறகு நிர்வாக அதிகாரிகளுக்கு எதிராகவும் வெளியிடப்படலாம்.\n3. தடைஉத்தரவு மற்றும் சான்றாய்வு பேராணைகள் இரண்டையுமே சட்டமன்ற அமைப்புகள் மற்றும் தனியார் நபர்களுக்கு எதிராக வெளியிடலாம்.\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "A",
    "Statements 1 and 2 are correct. Statement 3 is INCORRECT because NEITHER Prohibition NOR Certiorari can be issued against legislative bodies, private individuals, or private bodies.",
    "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறு, ஏனெனில் தடைஉத்தரவு மற்றும் சான்றாய்வு ஆகிய இரு பேராணைகளையுமே சட்டமன்ற அமைப்புகள் அல்லது தனியார் நபர்களுக்கு எதிராக வெளியிட முடியாது.",
    "Correct. Statements 1 and 2 are true; Statement 3 is false.", "சரி. கூற்றுகள் 1 மற்றும் 2 சரி; கூற்று 3 தவறானது.",
    "Incorrect. Statement 3 is false.", "தவறு. கூற்று 3 தவறானது.",
    "Incorrect. Statement 3 is false.", "தவறு. கூற்று 3 தவறானது.",
    "Incorrect. Statement 3 is false.", "தவறு. கூற்று 3 தவறானது.",
    "TNPSC Trap: Certiorari was expanded by Supreme Court in 1991 to cover Administrative Authorities affecting rights of individuals.",
    "TNPSC பொறி: 1991-ல் உச்ச நீதிமன்ற தீர்ப்பின் மூலம் சான்றாய்வுப் பேராணை (Certiorari) தனிநபர் உரிமைகளைப் பாதிக்கும் நிர்வாக அதிகாரிகளுக்கும் விரிவாக்கப்பட்டது.",
    "Prohibition stops a lower court from continuing proceedings beyond its jurisdiction; Certiorari quashes an order already passed without jurisdiction.",
    "தடைஉத்தரவு பேராணை கீழ் நீதிமன்றம் எல்லை மீறுவதைத் தடுக்கிறது; சான்றாய்வு பேராணை ஏற்கனவே பிறப்பிக்கப்பட்ட தவறான உத்தரவை ரத்து செய்கிறது.",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Prohibition Writ", "Certiorari Writ", "Three Statement"]
))

# FR_SB_025 (Medium)
questions.append(make_q(
    "FR_SB_025", "Medium",
    "Consider the following statements regarding Writ of Quo-Warranto:\n1. Quo-Warranto literally means 'By what authority or warrant?' and prevents illegal usurpation of a public office.\n2. Unlike other writs, the rule of 'Locus Standi' is relaxed for Quo-Warranto, allowing any interested person to petition the court.\n3. Quo-Warranto can be issued in respect of any private office or temporary contractual employment.\nWhich of the statements given above are correct?",
    "தகுதி வினவல் பேராணை (Quo-Warranto) பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. தகுதி வினவல் பேராணை என்பது 'எந்த அதிகாரத்தின் அடிப்படையில்?' என்று பொருள்படும், மேலும் பொதுப் பதவியை சட்டவிரோதமாகக் கைப்பற்றுவதைத் தடுக்கிறது.\n2. பிற பேராணைகளைப் போலன்றி, தகுதி வினவல் பேராணைக்கு 'பாதிக்கப்பட்ட நபரே அணுக வேண்டும்' (Locus Standi) என்ற விதி தளர்த்தப்பட்டு, ஆர்வமுள்ள எந்தவொரு நபரும் மனு செய்ய அனுமதிக்கப்படுகிறது.\n3. எந்தவொரு தனியார் பதவி அல்லது தற்காலிக ஒப்பந்த வேலைவாய்ப்பிற்கும் தகுதி வினவல் பேராணையை வெளியிடலாம்.\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "A",
    "Statements 1 and 2 are correct. Statement 3 is INCORRECT because Quo-Warranto can be issued ONLY in respect of a permanent public office of substantive character created by a statute or Constitution, NOT for private or ministerial offices.",
    "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறு, ஏனெனில் தகுதி வினவல் பேராணை அரசியலமைப்பு அல்லது சட்டத்தால் உருவாக்கப்பட்ட நிரந்தரப் பொதுப் பதவிக்கு மட்டுமே வெளியிடப்படும் (தனியார் பதவிக்கு அல்ல).",
    "Correct. Statements 1 and 2 are true; Statement 3 is false.", "சரி. கூற்றுகள் 1 மற்றும் 2 சரி; கூற்று 3 தவறானது.",
    "Incorrect. Statement 3 is false.", "தவறு. கூற்று 3 தவறானது.",
    "Incorrect. Statement 3 is false.", "தவறு. கூற்று 3 தவறானது.",
    "Incorrect. Statement 3 is false.", "தவறு. கூற்று 3 தவறானது.",
    "TNPSC Trap: Quo-Warranto is the ONLY writ that can be sought by any public-spirited citizen who is NOT personally aggrieved (relaxed locus standi).",
    "TNPSC பொறி: தகுதி வினவல் பேராணை (Quo-Warranto) மட்டுமே நேரடியாகப் பாதிக்கப்படாத எந்தவொரு பொதுநலக் குடிமகனும் கோரக்கூடிய ஒரே பேராணையாகும்.",
    "Quo-Warranto cannot be issued against a ministerial office (e.g. Minister post).",
    "அமைச்சர் பதவி போன்ற அரசியல் பதவிகளுக்கு எதிராக தகுதி வினவல் பேராணையை வெளியிட முடியாது.",
    "Understand", 60, ["Polity", "Fundamental Rights", "Quo-Warranto", "Locus Standi", "Three Statement"]
))

# FR_SB_026 (Hard)
questions.append(make_q(
    "FR_SB_026", "Hard",
    "Consider the following statements comparing Writ Jurisdiction of Supreme Court (Art 32) and High Court (Art 226):\n1. Supreme Court can issue writs ONLY for enforcement of Fundamental Rights, whereas High Court can issue writs for FRs as well as ordinary legal rights.\n2. Supreme Court's writ jurisdiction is narrower in scope than High Court's writ jurisdiction.\n3. Supreme Court CANNOT refuse to exercise its writ jurisdiction under Article 32, whereas High Court's writ jurisdiction under Article 226 is discretionary.\nWhich of the statements given above are correct?",
    "உச்ச நீதிமன்றம் (பிரிவு 32) மற்றும் உயர் நீதிமன்றத்தின் (பிரிவு 226) பேராணை அதிகாரங்களை ஒப்பிடும் பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. உச்ச நீதிமன்றம் அடிப்படை உரிமைகளை அமல்படுத்த மட்டுமே பேராணைகளை வெளியிட முடியும்; ஆனால் உயர் நீதிமன்றம் அடிப்படை உரிமைகள் மற்றும் சாதாரண சட்ட உரிமைகள் இரண்டிற்கும் வெளியிடலாம்.\n2. உச்ச நீதிமன்றத்தின் பேராணை அதிகாரத்தின் எல்லை உயர் நீதிமன்றத்தின் எல்லையை விடக் குறுகியதாகும்.\n3. பிரிவு 32-ன் கீழ் தனது பேராணை அதிகாரத்தைப் பயன்படுத்த உச்ச நீதிமன்றம் மறுக்க முடியாது; ஆனால் பிரிவு 226-ன் கீழ் உயர் நீதிமன்றத்தின் அதிகாரம் விருப்பத்திற்குட்பட்டது (discretionary).\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "D",
    "All three statements are correct. High Court's writ jurisdiction (Art 226) is WIDER in subject matter (covers FRs + legal rights) and DISCRETIONARY, whereas Supreme Court's (Art 32) is NARROWER (FRs only) and COMPULSORY because Art 32 is itself a Fundamental Right.",
    "மூன்று கூற்றுகளும் சரியானவை. பிரிவு 226 (உயர் நீதிமன்றம்) விரிவானது மற்றும் விருப்பத்திற்குட்பட்டது; பிரிவு 32 (உச்ச நீதிமன்றம்) அடிப்படை உரிமைகளுக்கு மட்டுமே என்பதால் குறுகியது, ஆனால் கட்டாயமானது.",
    "Incorrect. Statement 3 is also correct.", "தவறு. கூற்று 3-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.", "தவறு. கூற்று 1-ம் சரியானது.",
    "Incorrect. Statement 2 is also correct.", "தவறு. கூற்று 2-ம் சரியானது.",
    "Correct. All Statements 1, 2 and 3 are accurate comparison points.", "சரி. கூற்றுகள் 1, 2 மற்றும் 3 அனைத்தும் சரியான ஒப்பீட்டுப் புள்ளிகள்.",
    "TNPSC Trap: Geographically, Supreme Court has wider territorial jurisdiction (entire India) than High Court (state territory), but in terms of SUBJECT MATTER, High Court is wider than SC.",
    "TNPSC பொறி: புவியியல் ரீதியாக உச்ச நீதிமன்றத்தின் எல்லை பெரியது (முழு இந்தியா), ஆனால் பொருள் ரீதியாக (subject matter) உயர் நீதிமன்றத்தின் எல்லை பெரியது.",
    "Chandra Kumar case (1997) held that writ jurisdiction of both Supreme Court and High Court forms part of Basic Structure.",
    "சந்திர குமார் வழக்கில் (1997) உச்ச மற்றும் உயர் நீதிமன்றங்களின் பேராணை அதிகாரம் அடிப்படை அமைப்பின் பகுதி எனத் தீர்ப்பளிக்கப்பட்டது.",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Article 32 vs Article 226", "Writ Jurisdiction", "Three Statement"]
))

# FR_SB_027 (Medium)
questions.append(make_q(
    "FR_SB_027", "Medium",
    "Consider the following statements regarding Articles 33, 34, and 35 of the Indian Constitution:\n1. Article 33 empowers Parliament to modify or restrict the application of Fundamental Rights to members of the Armed Forces, Police Forces, and Intelligence agencies.\n2. A law enacted by Parliament under Article 33 can be challenged in any court of law on ground of violation of Fundamental Rights.\n3. Article 35 lays down that the power to make laws to give effect to specified Fundamental Rights rests exclusively with Parliament and NOT State Legislatures.\nWhich of the statements given above are correct?",
    "இந்திய அரசியலமைப்பின் 33, 34 மற்றும் 35 ஆகிய பிரிவுகள் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. முப்படைகள், காவல் படைகள் மற்றும் உளவு அமைப்புகளின் உறுப்பினர்களுக்கு அடிப்படை உரிமைகளைக் கட்டுப்படுத்த நாடாளுமன்றத்திற்கு பிரிவு 33 அதிகாரம் அளிக்கிறது.\n2. பிரிவு 33-ன் கீழ் நாடாளுமன்றத்தால் இயற்றப்பட்ட சட்டத்தை அடிப்படை உரிமைகளை மீறுகிறது என்ற அடிப்படையில் எந்தவொரு நீதிமன்றத்திலும் சவால் செய்யலாம்.\n3. குறிப்பிட்ட அடிப்படை உரிமைகளுக்குச் செயல்வடிவம் கொடுப்பதற்கான சட்டங்களை இயற்றும் அதிகாரம் நாடாளுமன்றத்திற்கு மட்டுமே உண்டு, மாநில சட்டமன்றங்களுக்கு இல்லை என்று பிரிவு 35 கூறுகிறது.\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "B",
    "Statements 1 and 3 are correct. Statement 2 is INCORRECT because laws made under Article 33 CANNOT be challenged in any court on the ground of violation of any Fundamental Rights.",
    "கூற்றுகள் 1 மற்றும் 3 சரியானவை. கூற்று 2 தவறு, ஏனெனில் பிரிவு 33-ன் கீழ் நாடாளுமன்றம் இயற்றும் சட்டங்களை அடிப்படை உரிமைகள் மீறல் என்ற அடிப்படையில் நீதிமன்றத்தில் சவால் செய்ய முடியாது.",
    "Incorrect. Statement 2 is false.", "தவறு. கூற்று 2 தவறானது.",
    "Correct. Statements 1 and 3 are true; Statement 2 is false.", "சரி. கூற்றுகள் 1 மற்றும் 3 சரி; கூற்று 2 தவறானது.",
    "Incorrect. Statement 2 is false.", "தவறு. கூற்று 2 தவறானது.",
    "Incorrect. Statement 2 is false.", "தவறு. கூற்று 2 தவறானது.",
    "TNPSC Trap: Parliament ALONE (not State Legislatures) can make laws under Article 33 and Article 35 to ensure uniformity throughout India.",
    "TNPSC பொறி: இந்தியா முழுவதும் ஒரே மாதிரியான தன்மையை உறுதிப்படுத்த பிரிவு 33 மற்றும் பிரிவு 35-ன் கீழ் நாடாளுமன்றம் மட்டுமே சட்டங்களை இயற்ற முடியும்.",
    "Article 34 provides for indemnity by law when Martial Law (military rule) is in force in any area.",
    "பிரிவு 34 இராணுவ ஆட்சி (Martial Law) அமலில் உள்ள காலத்தில் நஷ்டஈடு வழங்கும் சட்டத்திற்கு வழிவகுக்கிறது.",
    "Understand", 60, ["Polity", "Fundamental Rights", "Article 33", "Article 34", "Article 35", "Three Statement"]
))

# FR_SB_028 (Hard)
questions.append(make_q(
    "FR_SB_028", "Hard",
    "Consider the following statements regarding the Conflict and Relationship between Fundamental Rights (Part III) and DPSPs (Part IV):\n1. In Champakam Dorairajan case (1951), the Supreme Court held that Fundamental Rights prevail over DPSPs in case of any conflict.\n2. The 25th Constitutional Amendment Act, 1971 inserted Article 31C providing that laws giving effect to DPSPs in Article 39(b) and 39(c) cannot be declared void for violating Articles 14 or 19.\n3. In Minerva Mills case (1980), the Supreme Court ruled that the Indian Constitution is founded on the bedrock of the balance between Part III and Part IV.\nWhich of the statements given above are correct?",
    "அடிப்படை உரிமைகள் (பகுதி III) மற்றும் அரசு வழிகாட்டு நெறிமுறைகள் (பகுதி IV) இடையேயான உறவு பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. சண்பகம் துரைராஜன் வழக்கில் (1951), முரண்பாடு ஏற்படும் போது அடிப்படை உரிமைகளே மேலோங்கும் என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது.\n2. 25-வது அரசியலமைப்பு திருத்தச் சட்டம் 1971 பிரிவு 31C-ஐச் சேர்த்து, பிரிவு 39(b) மற்றும் 39(c)-ல் உள்ள DPSP-களை அமல்படுத்தும் சட்டங்கள் பிரிவு 14 அல்லது 19-ஐ மீறினாலும் செல்லுபடியாகும் என்றது.\n3. மினர்வா மில்ஸ் வழக்கில் (1980), இந்திய அரசியலமைப்பு பகுதி III மற்றும் பகுதி IV இடையேயான சமநிலையின் மீதே நிறுவப்பட்டுள்ளது என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது.\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "D",
    "All three statements are correct. Champakam Dorairajan (1951) gave supremacy to FRs. 25th CAA 1971 added Art 31C protecting 39(b)&(c). Minerva Mills (1980) declared that harmony and balance between Part III and Part IV is part of the Basic Structure.",
    "மூன்று கூற்றுகளும் சரியானவை. சண்பகம் துரைராஜன் வழக்கு (1951) அடிப்படை உரிமைகளுக்கு முன்னுரிமை அளித்தது. 25வது திருத்தம் பிரிவு 31C-ஐச் சேர்த்தது. மினர்வா மில்ஸ் வழக்கு (1980) சமநிலையே அடிப்படை அமைப்பு என்றது.",
    "Incorrect. Statement 3 is also correct.", "தவறு. கூற்று 3-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.", "தவறு. கூற்று 1-ம் சரியானது.",
    "Incorrect. Statement 2 is also correct.", "தவறு. கூற்று 2-ம் சரியானது.",
    "Correct. All Statements 1, 2 and 3 are historically and legally true.", "சரி. கூற்றுகள் 1, 2 மற்றும் 3 அனைத்தும் உண்மை.",
    "TNPSC Trap: Minerva Mills case invalidated Section 4 of 42nd CAA which tried to give primacy to ALL DPSPs over Articles 14, 19, and 31.",
    "TNPSC பொறி: மினர்வா மில்ஸ் வழக்கு அனைத்து DPSP-களுக்கும் அடிப்படை உரிமைகளை விட முன்னுரிமை அளிக்க முயன்ற 42-வது திருத்தத்தின் பிரிவு 4-ஐ ரத்து செய்தது.",
    "Supreme Court noted: 'To give absolute primacy to one over the other is to disturb the harmony of the Constitution.'",
    "உச்ச நீதிமன்றம் குறிப்பிட்டது: 'ஒன்றிற்கு மற்றொன்றை விட முழுமையான முன்னுரிமை அளிப்பது அரசியலமைப்பின் அமைதியைக் குலைப்பதாகும்.'",
    "Analyze", 60, ["Polity", "Fundamental Rights", "FR vs DPSP", "Minerva Mills Case", "Article 31C", "Three Statement"]
))

# FR_SB_029 (Medium)
questions.append(make_q(
    "FR_SB_029", "Medium",
    "Consider the following statements regarding the availability of Fundamental Rights to Citizens vs Non-Citizens:\n1. Fundamental Rights guaranteed under Articles 15, 16, 19, 29, and 30 are available to citizens of India only.\n2. Fundamental Rights guaranteed under Articles 14, 20, 21, 21A, 22, 23, 24, 25, 26, 27, and 28 are available to all persons, whether citizens or foreigners.\n3. Enemy aliens enjoy all Fundamental Rights available to foreign citizens under Part III of the Constitution.\nWhich of the statements given above are correct?",
    "குடிமக்கள் மற்றும் வெளிநாட்டினருக்குக் கிடைக்கும் அடிப்படை உரிமைகள் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. பிரிவுகள் 15, 16, 19, 29 மற்றும் 30 ஆகியவற்றின் கீழ் உள்ள அடிப்படை உரிமைகள் இந்தியக் குடிமக்களுக்கு மட்டுமே கிடைக்கின்றன.\n2. பிரிவுகள் 14, 20, 21, 21A, 22, 23, 24, 25, 26, 27 மற்றும் 28 ஆகியவை குடிமக்கள் மற்றும் வெளிநாட்டினர் உட்பட அனைத்து நபர்களுக்கும் கிடைக்கின்றன.\n3. எதிரி நாட்டு வேற்றுகிரகவாசிகள் (enemy aliens) பகுதி III-ன் கீழ் வெளிநாட்டினருக்குக் கிடைக்கும் அனைத்து அடிப்படை உரிமைகளையும் அனுபவிக்கிறார்கள்.\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "A",
    "Statements 1 and 2 are correct. Statement 3 is INCORRECT because Enemy Aliens do NOT enjoy protection against arrest and detention under Article 22(1) and 22(2).",
    "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறு, ஏனெனில் எதிரி நாட்டு மக்களுக்கு (Enemy Aliens) பிரிவு 22(1) & (2)-ன் கீழ் கைதுக்கு எதிரான பாதுகாப்பு கிடைக்காது.",
    "Correct. Statements 1 and 2 are true; Statement 3 is false.", "சரி. கூற்றுகள் 1 மற்றும் 2 சரி; கூற்று 3 தவறானது.",
    "Incorrect. Statement 3 is false.", "தவறு. கூற்று 3 தவறானது.",
    "Incorrect. Statement 3 is false.", "தவறு. கூற்று 3 தவறானது.",
    "Incorrect. Statement 3 is false.", "தவறு. கூற்று 3 தவறானது.",
    "TNPSC Trap: Memorize the 5 Citizen-ONLY Articles: 15, 16, 19, 29, 30. All other FR Articles apply to both citizens and foreigners.",
    "TNPSC பொறி: குடிமக்களுக்கு மட்டுமே உரித்தான 5 பிரிவுகளை நினைவில் கொள்க: 15, 16, 19, 29, 30. மற்ற அனைத்து உரிமைகளும் வெளிநாட்டினருக்கும் பொருந்தும்.",
    "Foreigners cannot claim freedom of speech under Art 19(1)(a) or reservation in employment under Art 16.",
    "வெளிநாட்டினர் பிரிவு 19(1)(a)-ன் கீழ் பேச்சு சுதந்திரத்தையோ அல்லது பிரிவு 16-ன் கீழ் இடஒதுக்கீட்டையோ கோர முடியாது.",
    "Understand", 60, ["Polity", "Fundamental Rights", "Citizens vs Foreigners", "Article Scope", "Three Statement"]
))

# FR_SB_030 (Hard)
questions.append(make_q(
    "FR_SB_030", "Hard",
    "Consider the following statements regarding Suspension of Fundamental Rights during National Emergency:\n1. Article 358 automatically suspends the six Fundamental Rights under Article 19 as soon as a National Emergency is declared on any ground.\n2. Article 359 authorizes the President to suspend the right to move any court for the enforcement of specified Fundamental Rights.\n3. The 44th Constitutional Amendment Act, 1978 restricted Article 358 to emergencies declared on grounds of war or external aggression, and prohibited suspension of Articles 20 and 21 under Article 359.\nWhich of the statements given above are correct?",
    "தேசிய அவசரநிலையின் போது அடிப்படை உரிமைகளை இடைநீக்கம் செய்வது பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. எந்தக் காரணத்திற்காக தேசிய அவசரநிலை அறிவிக்கப்பட்டாலும் பிரிவு 358 பிரிவு 19-ன் கீழ் உள்ள ஆறு அடிப்படை உரிமைகளையும் தானாகவே இடைநீக்கம் செய்கிறது.\n2. குறிப்பிட்ட அடிப்படை உரிமைகளை அமல்படுத்த நீதிமன்றத்தை அணுகும் உரிமையை இடைநீக்கம் செய்ய குடியரசுத் தலைவருக்கு பிரிவு 359 அதிகாரம் அளிக்கிறது.\n3. 44-வது அரசியலமைப்பு திருத்தச் சட்டம் 1978 பிரிவு 358-ஐ போர் அல்லது வெளிநாட்டு ஆக்கிரமிப்பு காரணங்களுக்கு மட்டுமே வரம்பிற்குட்படுத்தியது, மேலும் பிரிவு 359-ன் கீழ் பிரிவுகள் 20 மற்றும் 21-ஐ இடைநீக்கம் செய்வதைத் தடுத்தது.\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1 and 2 only", "1 மற்றும் 2 மட்டும்",
    "2 and 3 only", "2 மற்றும் 3 மட்டும்",
    "1 and 3 only", "1 மற்றும் 3 மட்டும்",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "B",
    "Statements 2 and 3 are correct. Statement 1 is INCORRECT because after the 44th CAA 1978, Article 358 suspends Article 19 ONLY when emergency is declared on ground of War or External Aggression (External Emergency), NOT on ground of Armed Rebellion (Internal Emergency).",
    "கூற்றுகள் 2 மற்றும் 3 சரியானவை. கூற்று 1 தவறு, ஏனெனில் 44-வது திருத்தத்திற்குப் பிறகு போர் அல்லது வெளிநாட்டு ஆக்கிரமிப்பு (வெளிப்புற அவசரநிலை) காரணங்களுக்காக மட்டுமே பிரிவு 358 பிரிவு 19-ஐ இடைநீக்கம் செய்யும் (ஆயுதமேந்திய கிளர்ச்சியின் போது அல்ல).",
    "Incorrect. Statement 1 is false.", "தவறு. கூற்று 1 தவறானது.",
    "Correct. Statements 2 and 3 are true; Statement 1 is false.", "சரி. கூற்றுகள் 2 மற்றும் 3 சரி; கூற்று 1 தவறானது.",
    "Incorrect. Statement 1 is false.", "தவறு. கூற்று 1 தவறானது.",
    "Incorrect. Statement 1 is false.", "தவறு. கூற்று 1 தவறானது.",
    "TNPSC Trap: Articles 20 and 21 CANNEVER be suspended under Article 359, even during National Emergency.",
    "TNPSC பொறி: பிரிவுகள் 20 மற்றும் 21-ஐ தேசிய அவசரநிலையின் போது கூட பிரிவு 359-ன் கீழ் இடைநீக்கம் செய்ய முடியாது.",
    "Article 358 operates automatically, whereas Article 359 requires a specific Presidential Order specifying which rights are suspended.",
    "பிரிவு 358 தானாகவே செயல்படும், ஆனால் பிரிவு 359 குடியரசுத் தலைவரின் தனி உத்தரவைக் கோருகிறது.",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Article 358", "Article 359", "National Emergency", "Three Statement"]
))

# Save checkpoint for Part 2
print(f"Added {len(questions)} Three-Statement questions.")

# ==============================================================================
# PART 3: 10 FOUR-STATEMENT QUESTIONS (FR_SB_031 to FR_SB_040)
# ==============================================================================

# FR_SB_031 (Medium)
questions.append(make_q(
    "FR_SB_031", "Medium",
    "Consider the following statements regarding the Six Freedoms under Article 19(1) and their Reasonable Restrictions:\n1. Freedom of Speech and Expression (Art 19(1)(a)) can be restricted on grounds of sovereignty and integrity of India, security of state, public order, and defamation.\n2. Freedom to assemble peacefully and without arms (Art 19(1)(b)) includes the right to strike work.\n3. Freedom to form associations or unions (Art 19(1)(c)) was expanded by the 97th Amendment Act, 2011 to include 'co-operative societies'.\n4. Reasonable restrictions under Article 19(2) to 19(6) are subject to judicial review to determine whether they are reasonable or arbitrary.\nWhich of the statements given above are correct?",
    "பிரிவு 19(1)-ன் கீழ் உள்ள ஆறு சுதந்திரங்கள் மற்றும் அவற்றின் நியாயமான கட்டுப்பாடுகள் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. பேச்சு மற்றும் கருத்துச் சுதந்திரம் (19(1)(a)) இந்தியாவின் இறையாண்மை, பாதுகாப்பு, பொது ஒழுங்கு, அவதூறு ஆகிய காரணங்களுக்காகக் கட்டுப்படுத்தப்படலாம்.\n2. ஆயுதங்களின்றி அமைதியாகக் கூடும் சுதந்திரம் (19(1)(b)) வேலைநிறுத்தம் செய்யும் உரிமையையும் உள்ளடக்கியது.\n3. சங்கங்கள் அல்லது தொழிற்சங்கங்களை அமைக்கும் சுதந்திரம் (19(1)(c)) 97-வது திருத்தச் சட்டம் 2011 மூலம் 'கூட்டுறவு சங்கங்களையும்' உள்ளடக்கி விரிவாக்கப்பட்டது.\n4. பிரிவு 19(2) முதல் 19(6) வரையிலான நியாயமான கட்டுப்பாடுகள் அவை நியாயமானவையா அல்லது தன்னிச்சையானவையா என்பதைத் தீர்மானிக்க நீதித்துறை மறுஆய்வுக்கு உட்பட்டவை.\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1, 3 and 4 only", "1, 3 மற்றும் 4 மட்டும்",
    "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டும்",
    "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டும்",
    "1, 2, 3 and 4", "1, 2, 3 மற்றும் 4",
    "A",
    "Statements 1, 3, and 4 are correct. Statement 2 is INCORRECT because Supreme Court in Kameshwar Singh case held that right to assemble peacefully does NOT include the right to strike work.",
    "கூற்றுகள் 1, 3 மற்றும் 4 சரியானவை. கூற்று 2 தவறு, ஏனெனில் அமைதியாகக் கூடும் உரிமை வேலைநிறுத்தம் செய்யும் உரிமையை உள்ளடக்காது என உச்ச நீதிமன்றம் தீர்ப்பளித்துள்ளது.",
    "Correct. Statements 1, 3, and 4 are true; Statement 2 is false as right to strike is not a fundamental right.", "சரி. கூற்றுகள் 1, 3 மற்றும் 4 சரி; வேலைநிறுத்த உரிமை அடிப்படை உரிமை அல்ல என்பதால் கூற்று 2 தவறு.",
    "Incorrect. Statement 2 is false.", "தவறு. கூற்று 2 தவறானது.",
    "Incorrect. Statement 2 is false.", "தவறு. கூற்று 2 தவறானது.",
    "Incorrect. Statement 2 is false.", "தவறு. கூற்று 2 தவறானது.",
    "TNPSC Trap: Right to Strike is NOT a Fundamental Right under Article 19(1)(b) or 19(1)(c).",
    "TNPSC பொறி: வேலைநிறுத்தம் செய்யும் உரிமை (Right to Strike) பிரிவு 19-ன் கீழ் அடிப்படை உரிமை அல்ல.",
    "The 97th Amendment Act, 2011 added the word 'co-operative societies' in Article 19(1)(c), Part IVB, and Article 43B.",
    "97-வது திருத்தச் சட்டம் 2011 'கூட்டுறவு சங்கங்கள்' என்ற சொல்லை பிரிவு 19(1)(c), பகுதி IVB மற்றும் பிரிவு 43B ஆகியவற்றில் சேர்த்தது.",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Article 19", "Reasonable Restrictions", "Four Statement"]
))

# FR_SB_032 (Hard)
questions.append(make_q(
    "FR_SB_032", "Hard",
    "Consider the following statements regarding Reservation Policy and Landmark Judgments:\n1. In Indra Sawhney case (1992), the Supreme Court upheld 27% reservation for OBCs subject to exclusion of the 'Creamy Layer' and capped total reservations at 50%.\n2. In M. Nagaraj case (2006), the Supreme Court mandated that State must collect quantifiable data showing backwardness and inadequacy of representation for SC/ST promotion reservation.\n3. In Jarnail Singh case (2018), the Supreme Court ruled that the Creamy Layer principle applies to SCs and STs as well for promotion reservations.\n4. The 103rd Constitutional Amendment Act, 2019 provided 10% reservation for EWS over and above the existing 50% cap.\nWhich of the statements given above are correct?",
    "இடஒதுக்கீட்டுக் கொள்கை மற்றும் வரலாற்றுச் சிறப்புமிக்க தீர்ப்புகள் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இந்திரா சாவ்னி வழக்கில் (1992), 'கிரீமி லேயர்' (சீர்அடுக்கு) விலக்கத்திற்கு உட்பட்டு OBC-க்கான 27% இடஒதுக்கீட்டை உச்ச நீதிமன்றம் உறுதி செய்ததுடன் மொத்த இடஒதுக்கீட்டை 50% ஆக வரம்பிட்டது.\n2. எம். நாகராஜ் வழக்கில் (2006), SC/ST பதவி உயர்வு இடஒதுக்கீட்டிற்கு பின்தங்கிய நிலை மற்றும் போதிய பிரதிநிதித்துவமின்மையைக் காட்ட மாநில அரசு அளவிடக்கூடிய தரவுகளைச் சேகரிக்க வேண்டும் என்று உச்ச நீதிமன்றம் உத்தரவிட்டது.\n3. ஜர்னைல் சிங் வழக்கில் (2018), பதவி உயர்வு இடஒதுக்கீட்டில் கிரீமி லேயர் கோட்பாடு SC மற்றும் ST பிரிவினருக்கும் பொருந்தும் என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது.\n4. 103-வது அரசியலமைப்பு திருத்தச் சட்டம் 2019, ஏற்கனவே உள்ள 50% வரம்பிற்கு அப்பால் EWS பிரிவினருக்கு 10% இடஒதுக்கீட்டை வழங்கியது.\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டும்",
    "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டும்",
    "1, 3 and 4 only", "1, 3 மற்றும் 4 மட்டும்",
    "1, 2, 3 and 4", "1, 2, 3 மற்றும் 4",
    "D",
    "All four statements are correct. Indra Sawhney (1992) fixed 50% cap & creamy layer for OBCs. M. Nagaraj (2006) required quantifiable data. Jarnail Singh (2018) extended creamy layer to SCs/STs for promotion reservation and modified Nagaraj requirement of demonstrating SC/ST backwardness. 103rd CAA 2019 added EWS 10%.",
    "நான்கு கூற்றுகளும் சரியானவை. இந்திரா சாவ்னி (1992) 50% வரம்பையும் கிரீமி லேயரையும் நிர்ணயித்தது. நாகராஜ் (2006) தரவுகளைக் கேட்டது. ஜர்னைல் சிங் (2018) SC/ST பதவி உயர்வில் கிரீமி லேயரைப் பயன்படுத்தியது. 103வது திருத்தம் EWS 10% வழங்கியது.",
    "Incorrect. Statement 4 is also correct.", "தவறு. கூற்று 4-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.", "தவறு. கூற்று 1-ம் சரியானது.",
    "Incorrect. Statement 2 is also correct.", "தவறு. கூற்று 2-ம் சரியானது.",
    "Correct. All Statements 1, 2, 3 and 4 are legally accurate.", "சரி. கூற்றுகள் 1, 2, 3 மற்றும் 4 அனைத்தும் சட்டப்பூர்வமாக சரியானவை.",
    "TNPSC Trap: In Janhit Abhiyan case (2022), the Supreme Court by 3:2 majority upheld the 103rd Constitutional Amendment (EWS 10% reservation).",
    "TNPSC பொறி: ஜன்ஹித் அபியான் வழக்கில் (2022) உச்ச நீதிமன்றம் 3:2 பெரும்பான்மையில் 103-வது திருத்தத்தை (EWS 10% இடஒதுக்கீடு) உறுதி செய்தது.",
    "Creamy layer principle excludes affluent sections of backward classes from receiving reservation benefits.",
    "கிரீமி லேயர் கோட்பாடு பிற்படுத்தப்பட்ட வகுப்பினரின் வசதி படைத்த பிரிவினர் இடஒதுக்கீட்டுப் பலன்களைப் பெறுவதிலிருந்து விலக்குகிறது.",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Indra Sawhney Case", "M Nagaraj Case", "103rd Amendment", "Four Statement"]
))

# FR_SB_033 (Medium)
questions.append(make_q(
    "FR_SB_033", "Medium",
    "Consider the following statements regarding the Expanded Dimensions of Article 21 (Right to Life & Personal Liberty):\n1. Right to Privacy was declared a Fundamental Right under Article 21 in Justice K.S. Puttaswamy case (2017).\n2. Right to Clean Environment and Pollution-free Water was recognized under Article 21 in Subhash Kumar case (1991).\n3. Right to Free Legal Aid for poor accused was recognized under Article 21 in M.H. Hoskot case (1978).\n4. Right to Speedy Trial was recognized as part of Article 21 in Hussainara Khatoon case (1979).\nWhich of the statements given above are correct?",
    "பிரிவு 21-ன் (வாழ்வு மற்றும் தனிநபர் சுதந்திரத்திற்கான உரிமை) விரிவாக்கப்பட்ட பரிமாணங்கள் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. தனியுரிமை (Right to Privacy) கே.எஸ். புட்டசுவாமி வழக்கில் (2017) பிரிவு 21-ன் கீழ் அடிப்படை உரிமையாக அறிவிக்கப்பட்டது.\n2. தூய்மையான சுற்றுச்சூழல் மற்றும் மாசுபாடற்ற குடிநீருக்கான உரிமை சுபாஷ் குமார் வழக்கில் (1991) பிரிவு 21-ன் கீழ் அங்கீகரிக்கப்பட்டது.\n3. ஏழை குற்றவாளிகளுக்கு இலவச சட்ட உதவிக்கான உரிமை எம்.எச். ஹோஸ்காட் வழக்கில் (1978) பிரிவு 21-ன் கீழ் அங்கீகரிக்கப்பட்டது.\n4. விரைவு விசாரணைக்கான உரிமை (Right to Speedy Trial) ஹுசைனாரா காதுன் வழக்கில் (1979) பிரிவு 21-ன் பகுதியாக அங்கீகரிக்கப்பட்டது.\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டும்",
    "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டும்",
    "1, 3 and 4 only", "1, 3 மற்றும் 4 மட்டும்",
    "1, 2, 3 and 4", "1, 2, 3 மற்றும் 4",
    "D",
    "All four statements are correct. Through judicial activation post-Maneka Gandhi, Article 21 has been expanded to cover Privacy (Puttaswamy 2017), Clean Environment (Subhash Kumar 1991), Legal Aid (Hoskot 1978), and Speedy Trial (Hussainara Khatoon 1979).",
    "நான்கு கூற்றுகளும் சரியானவை. மேனகா காந்தி வழக்கிற்குப் பிறகு நீதித்துறை மூலம் தனியுரிமை, தூய்மையான சுற்றுச்சூழல், இலவச சட்ட உதவி, விரைவு விசாரணை ஆகியவை பிரிவு 21-ன் கீழ் சேர்க்கப்பட்டன.",
    "Incorrect. Statement 4 is also correct.", "தவறு. கூற்று 4-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.", "தவறு. கூற்று 1-ம் சரியானது.",
    "Incorrect. Statement 2 is also correct.", "தவறு. கூற்று 2-ம் சரியானது.",
    "Correct. All Statements 1, 2, 3 and 4 are landmark decisions under Article 21.", "சரி. கூற்றுகள் 1, 2, 3 மற்றும் 4 அனைத்தும் பிரிவு 21-ன் கீழ் வரலாற்றுச் சிறப்புமிக்க முடிவுகள்.",
    "TNPSC Trap: Right to Life under Article 21 does NOT include the 'Right to Die' (Gian Kaur case 1996), though passive euthanasia is allowed under strict guidelines (Aruna Shanbaug 2011).",
    "TNPSC பொறி: பிரிவு 21-ன் கீழ் வாழும் உரிமை என்பது 'சாகும் உரிமையை' (Right to Die) உள்ளடக்காது (ஞான் கவுர் வழக்கு 1996).",
    "Article 21 has been described as the 'procedural heart of Part III' due to its wide judicial interpretation.",
    "நீதிமன்றங்களின் பரந்த விளக்கத்தினால் பிரிவு 21 'பகுதி III-ன் நடைமுறை இதயம்' என விவரிக்கப்படுகிறது.",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Article 21", "Right to Privacy", "Puttaswamy Case", "Four Statement"]
))

# FR_SB_034 (Medium)
questions.append(make_q(
    "FR_SB_034", "Medium",
    "Consider the following statements regarding Preventive Detention Laws under Article 22:\n1. A person can be detained under preventive detention without trial for a maximum period of 3 months unless an Advisory Board extends it.\n2. The Advisory Board must consist of persons who are, or have been, or are qualified to be appointed as Judges of a High Court.\n3. The detaining authority must communicate the grounds of detention to the detainee as soon as possible.\n4. The detaining authority is constitutionally bound to disclose ALL facts to the detainee without any exception.\nWhich of the statements given above are correct?",
    "பிரிவு 22-ன் கீழ் உள்ள தடுப்புக்காவல் சட்டங்கள் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. ஆலோசனைக் குழு நீட்டிக்காவிட்டால், ஒரு நபரை விசாரணையின்றி அதிகபட்சமாக 3 மாத காலத்திற்கு தடுப்புக்காவலில் வைக்கலாம்.\n2. ஆலோசனைக் குழுவில் உயர் நீதிமன்ற நீதிபதிகளாக உள்ளவர்கள், இருந்தவர்கள் அல்லது நியமிக்கப்படத் தகுதியுள்ளவர்கள் இடம்பெற வேண்டும்.\n3. தடுப்புக்காவலில் வைக்கும் அதிகாரம் கொண்ட அமைப்பு, தடுப்புக்காவலுக்கான காரணங்களை கூடிய விரைவில் தடுப்புக் காவலாளியிடம் தெரிவிக்க வேண்டும்.\n4. தடுப்புக்காவலில் வைக்கும் அமைப்பு அனைத்து உண்மைகளையும் எந்தவொரு விலக்குமின்றி தடுப்புக் காவலாளியிடம் தெரிவிக்க அரசியலமைப்பு ரீதியாகக் கடமைப்பட்டுள்ளது.\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டும்",
    "1, 3 and 4 only", "1, 3 மற்றும் 4 மட்டும்",
    "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டும்",
    "1, 2, 3 and 4", "1, 2, 3 மற்றும் 4",
    "A",
    "Statements 1, 2, and 3 are correct. Statement 4 is INCORRECT because under Article 22(6), the State is NOT required to disclose facts which it considers to be against public interest to disclose.",
    "கூற்றுகள் 1, 2 மற்றும் 3 சரியானவை. கூற்று 4 தவறு, ஏனெனில் பிரிவு 22(6)-ன் கீழ் பொது நலனுக்கு எதிரானது என்று அரசு கருதும் உண்மைகளை வெளியிட வேண்டிய அவசியமில்லை.",
    "Correct. Statements 1, 2, and 3 are true; Statement 4 is false under Art 22(6).", "சரி. கூற்றுகள் 1, 2 மற்றும் 3 சரி; பிரிவு 22(6)-ன் கீழ் உண்மை விவரங்களை அரசு மறைக்கலாம் என்பதால் கூற்று 4 தவறு.",
    "Incorrect. Statement 4 is false.", "தவறு. கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.", "தவறு. கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.", "தவறு. கூற்று 4 தவறானது.",
    "TNPSC Trap: Article 22(6) provides a constitutional exception: State can refuse to disclose facts if disclosure is against PUBLIC INTEREST.",
    "TNPSC பொறி: பிரிவு 22(6) ஒரு அரசியலமைப்பு விதிவிலக்கை வழங்குகிறது: பொது நலனுக்கு எதிரானது என்றால் உண்மைகளை வெளியிட அரசு மறுக்கலாம்.",
    "Both Parliament and State Legislatures have concurrent power to make preventive detention laws for security of state, public order, and essential supplies.",
    "மாநிலப் பாதுகாப்பு, பொது ஒழுங்கு மற்றும் அத்தியாவசியப் பொருட்கள் விநியோகம் ஆகியவற்றிற்காக தடுப்புக்காவல் சட்டங்களை நாடாளுமன்றமும் மாநில சட்டமன்றங்களும் இயற்றலாம்.",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Article 22", "Preventive Detention", "Advisory Board", "Four Statement"]
))

# FR_SB_035 (Hard)
questions.append(make_q(
    "FR_SB_035", "Hard",
    "Consider the following statements regarding the Five Writs under Article 32 and Article 226:\n1. Habeas Corpus literally means 'To have the body of' and protects against illegal detention.\n2. Mandamus literally means 'We Command' and is issued to perform a mandatory statutory duty.\n3. Prohibition is issued by a higher court to a lower court to prevent it from exceeding its jurisdiction.\n4. Certiorari is issued by a higher court to quash an order already passed by a lower court or tribunal without jurisdiction.\nWhich of the statements given above are correct?",
    "பிரிவு 32 மற்றும் 226-ன் கீழ் உள்ள ஐந்து பேராணைகள் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. ஆட்கொணர்வு பேராணை (Habeas Corpus) என்றால் 'உடலைக் கொணர்தல்' என்று பொருள், மேலும் சட்டவிரோதக் காவலுக்கு எதிராகப் பாதுகாக்கிறது.\n2. கட்டளைப் பேராணை (Mandamus) என்றால் 'நாம் ஆணையிடுகிறோம்' என்று பொருள், மேலும் கட்டாய சட்டப்பூர்வ கடமையை நிறைவேற்ற வெளியிடப்படுகிறது.\n3. தடையுறுத்தும் பேராணை (Prohibition) ஒரு உயர் நீதிமன்றத்தால் கீழ் நீதிமன்றத்திற்குத் தன் அதிகார வரம்பை மீறுவதைத் தடுக்க வெளியிடப்படுகிறது.\n4. சான்றாய்வுப் பேராணை (Certiorari) அதிகார வரம்பின்றி கீழ் நீதிமன்றம் பிறப்பித்த உத்தரவை ரத்து செய்ய உயர் நீதிமன்றத்தால் வெளியிடப்படுகிறது.\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டும்",
    "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டும்",
    "1, 3 and 4 only", "1, 3 மற்றும் 4 மட்டும்",
    "1, 2, 3 and 4", "1, 2, 3 மற்றும் 4",
    "D",
    "All four statements are correct definitions and scopes of Habeas Corpus, Mandamus, Prohibition, and Certiorari.",
    "நான்கு கூற்றுகளும் ஆட்கொணர்வு, கட்டளை, தடையுறுத்தல் மற்றும் சான்றாய்வு பேராணைகளின் சரியான வரைவிலக்கணங்கள் ஆகும்.",
    "Incorrect. Statement 4 is also correct.", "தவறு. கூற்று 4-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.", "தவறு. கூற்று 1-ம் சரியானது.",
    "Incorrect. Statement 2 is also correct.", "தவறு. கூற்று 2-ம் சரியானது.",
    "Correct. All Statements 1, 2, 3 and 4 are completely true.", "சரி. கூற்றுகள் 1, 2, 3 மற்றும் 4 அனைத்தும் முற்றிலும் உண்மை.",
    "TNPSC Trap: Prohibition prevents an ongoing wrong; Certiorari cures a wrong already committed.",
    "TNPSC பொறி: தடையுறுத்தும் பேராணை (Prohibition) நடக்கும் தவறைக் தடுக்கிறது; சான்றாய்வுப் பேராணை (Certiorari) நடந்த தவறைச் சரிசெய்கிறது (ரத்து செய்கிறது).",
    "Quo-Warranto literally means 'By what authority?' and checks the legality of a person's claim to a public office.",
    "தகுதி வினவல் பேராணை (Quo-Warranto) 'எந்த அதிகாரத்தின் படி?' என்று வினவி பொதுப் பதவியின் சட்டப்பூர்வ தன்மையைச் சரிபார்க்கிறது.",
    "Understand", 60, ["Polity", "Fundamental Rights", "Writs Comparison", "Article 32", "Article 226", "Four Statement"]
))

# FR_SB_036 (Medium)
questions.append(make_q(
    "FR_SB_036", "Medium",
    "Consider the following statements regarding Right to Freedom of Religion (Articles 25 to 28):\n1. Freedom of Conscience under Article 25 includes the inner freedom of an individual to mold his relation with God in whatever way he desires.\n2. Article 25(2)(a) empowers the State to regulate economic, financial, political or other secular activities associated with religious practice.\n3. Article 26 guarantees religious denominations the right to manage their internal religious affairs without State interference.\n4. Article 28 permits compulsory religious instruction in educational institutions recognized by the State or receiving aid from State funds.\nWhich of the statements given above are correct?",
    "மத சுதந்திரத்திற்கான உரிமை (பிரிவுகள் 25 முதல் 28) பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. பிரிவு 25-ன் கீழ் உள்ள மனசாட்சி சுதந்திரம் என்பது ஒரு தனிநபர் கடவுளுடனான தனது உறவை தான் விரும்பும் வழியில் வடிவமைத்துக் கொள்ளும் உள் சுதந்திரத்தை உள்ளடக்கியது.\n2. பிரிவு 25(2)(a) மத நடைமுறைகளுடன் தொடர்புடைய பொருளாதார, நிதி, அரசியல் அல்லது பிற மதச்சார்பற்ற நடவடிக்கைகளை முறைப்படுத்த அரசுக்கு அதிகாரம் அளிக்கிறது.\n3. பிரிவு 26 மதப் பிரிவினர் அரசின் தலையீடின்றி தங்களது உள் மத விவகாரங்களை நிர்வகிக்கும் உரிமையை உத்தரவாதம் செய்கிறது.\n4. பிரிவு 28 அரசால் அங்கீகரிக்கப்பட்ட அல்லது அரசு உதவி பெறும் கல்வி நிறுவனங்களில் கட்டாய மதக் கல்வியை அனுமதிக்கிறது.\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டும்",
    "1, 3 and 4 only", "1, 3 மற்றும் 4 மட்டும்",
    "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டும்",
    "1, 2, 3 and 4", "1, 2, 3 மற்றும் 4",
    "A",
    "Statements 1, 2, and 3 are correct. Statement 4 is INCORRECT because Article 28(3) mandates that NO person attending any educational institution recognized by State or receiving State aid shall be COMPELLED to take part in religious instruction without consent.",
    "கூற்றுகள் 1, 2 மற்றும் 3 சரியானவை. கூற்று 4 தவறு, ஏனெனில் பிரிவு 28(3)-ன் கீழ் அரசு அங்கீகாரம் பெற்ற அல்லது உதவி பெறும் நிறுவனங்களில் படிக்கும் எந்தவொரு நபரும் சம்மதமின்றி மதக் கல்வியில் பங்கேற்க நிர்பந்திக்கப்படக் கூடாது.",
    "Correct. Statements 1, 2, and 3 are true; Statement 4 is false under Art 28(3).", "சரி. கூற்றுகள் 1, 2 மற்றும் 3 சரி; பிரிவு 28(3)-ன் கீழ் கட்டாய மதக் கல்வி தடை செய்யப்பட்டுள்ளதால் கூற்று 4 தவறு.",
    "Incorrect. Statement 4 is false.", "தவறு. கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.", "தவறு. கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.", "தவறு. கூற்று 4 தவறானது.",
    "TNPSC Trap: Educational institutions wholly maintained by State funds CANNOT impart religious instruction at all (Art 28(1)). Recognized/Aided institutions CANNOT compel participation (Art 28(3)).",
    "TNPSC பொறி: முழுமையாக அரசு நிதியால் செயல்படும் நிறுவனங்களில் மதக் கல்வி வழங்கவே முடியாது. அரசு உதவி பெறும் நிறுவனங்களில் கட்டாயப்படுத்த முடியாது.",
    "The word 'Secular' was added to the Preamble by the 42nd Constitutional Amendment Act, 1976.",
    "42-வது அரசியலமைப்பு திருத்தச் சட்டம் 1976 மூலம் முகப்புரையில் 'மதச்சார்பற்ற' என்ற சொல் சேர்க்கப்பட்டது.",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Articles 25-28", "Freedom of Religion", "Four Statement"]
))

# FR_SB_037 (Hard)
questions.append(make_q(
    "FR_SB_037", "Hard",
    "Consider the following statements regarding Landmark Constitutional Amendment Acts on Fundamental Rights:\n1. The 1st Amendment Act 1951 introduced Article 15(4) and added the Ninth Schedule to protect land reform laws.\n2. The 24th Amendment Act 1971 affirmed that Parliament has the power to amend any part of Part III under Article 368.\n3. The 44th Amendment Act 1978 deleted Right to Property from Part III and made Articles 20 and 21 non-suspendable during National Emergency.\n4. The 86th Amendment Act 2002 made Right to Education a Fundamental Right under Article 21A.\nWhich of the statements given above are correct?",
    "அடிப்படை உரிமைகள் மீதான வரலாற்றுச் சிறப்புமிக்க அரசியலமைப்பு திருத்தச் சட்டங்கள் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 1-வது திருத்தச் சட்டம் 1951 பிரிவு 15(4)-ஐ அறிமுகப்படுத்தியதுடன் நிலச்சீர்திருத்தச் சட்டங்களைப் பாதுகாக்க 9-வது அட்டவணையைச் சேர்த்தது.\n2. 24-வது திருத்தச் சட்டம் 1971 பிரிவு 368-ன் கீழ் பகுதி III-ன் எந்தப் பகுதியையும் திருத்தும் அதிகாரம் நாடாளுமன்றத்திற்கு உண்டு என உறுதிப்படுத்தியது.\n3. 44-வது திருத்தச் சட்டம் 1978 சொத்துரிமையை பகுதி III-லிருந்து நீக்கியதுடன் தேசிய அவசரநிலையின் போது பிரிவுகள் 20 மற்றும் 21-ஐ இடைநீக்கம் செய்ய முடியாது என மாற்றியது.\n4. 86-வது திருத்தச் சட்டம் 2002 பிரிவு 21A-ன் கீழ் கல்வி உரிமையை அடிப்படை உரிமையாக்கியது.\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டும்",
    "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டும்",
    "1, 3 and 4 only", "1, 3 மற்றும் 4 மட்டும்",
    "1, 2, 3 and 4", "1, 2, 3 மற்றும் 4",
    "D",
    "All four statements are correct landmark constitutional amendment facts modifying Part III of the Indian Constitution.",
    "நான்கு கூற்றுகளும் பகுதி III-ஐ மாற்றியமைத்த வரலாற்றுச் சிறப்புமிக்க அரசியலமைப்பு திருத்தங்கள் பற்றிய உண்மைகள் ஆகும்.",
    "Incorrect. Statement 4 is also correct.", "தவறு. கூற்று 4-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.", "தவறு. கூற்று 1-ம் சரியானது.",
    "Incorrect. Statement 2 is also correct.", "தவறு. கூற்று 2-ம் சரியானது.",
    "Correct. All Statements 1, 2, 3 and 4 are constitutionally true.", "சரி. கூற்றுகள் 1, 2, 3 மற்றும் 4 அனைத்தும் உண்மை.",
    "TNPSC Trap: 24th CAA 1978 amended both Article 13 and Article 368 to override the Golaknath judgment.",
    "TNPSC பொறி: 24-வது திருத்தச் சட்டம் கோலக்நாத் வழக்கின் தீர்ப்பை முறியடிக்க பிரிவு 13 மற்றும் பிரிவு 368 ஆகிய இரண்டையுமே திருத்தியது.",
    "The First Amendment Act, 1951 added Article 31A and Article 31B alongside the Ninth Schedule.",
    "1-வது திருத்தச் சட்டம் 1951 ஒன்பதாவது அட்டவணையுடன் பிரிவு 31A மற்றும் பிரிவு 31B ஆகியவற்றையும் சேர்த்தது.",
    "Understand", 60, ["Polity", "Fundamental Rights", "1st Amendment", "24th Amendment", "44th Amendment", "86th Amendment", "Four Statement"]
))

# FR_SB_038 (Hard)
questions.append(make_q(
    "FR_SB_038", "Hard",
    "Consider the following statements regarding the Evolution of Basic Structure Doctrine and Amendability of Fundamental Rights:\n1. In Shankari Prasad case (1951), the Supreme Court held that Parliament can amend any Fundamental Right using Article 368.\n2. In Golaknath case (1967), the Supreme Court ruled that Fundamental Rights are given a 'transcendental and immutable' position and cannot be amended by Parliament.\n3. In Kesavananda Bharati case (1973), the Supreme Court overruled Golaknath and held that Parliament can amend any part of Part III, subject to the 'Basic Structure' doctrine.\n4. The 42nd Amendment Act 1976 attempted to declare that there shall be no limitation whatever on the constituent power of Parliament under Article 368.\nWhich of the statements given above are correct?",
    "அடிப்படை அமைப்பு மறுஆய்வுக் கோட்பாட்டின் வளர்ச்சி மற்றும் அடிப்படை உரிமைகளைத் திருத்தும் அதிகாரம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. சங்கரி பிரசாத் வழக்கில் (1951), பிரிவு 368-ஐப் பயன்படுத்தி நாடாளுமன்றம் எந்தவொரு அடிப்படை உரிமையையும் திருத்த முடியும் என்று உச்ச நீதிமன்றம் கூறியது.\n2. கோலக்நாத் வழக்கில் (1967), அடிப்படை உரிமைகள் 'உன்னதமான மற்றும் மாற்ற முடியாத' இடத்தைப் பெற்றுள்ளன என்றும் நாடாளுமன்றம் அவற்றை திருத்த முடியாது என்றும் உச்ச நீதிமன்றம் தீர்ப்பளித்தது.\n3. கேசவாநந்த பாரதி வழக்கில் (1973), உச்ச நீதிமன்றம் கோலக்நாத் தீர்ப்பை ரத்து செய்து, 'அடிப்படை அமைப்பு' கோட்பாட்டிற்கு உட்பட்டு பகுதி III-ஐ நாடாளுமன்றம் திருத்தலாம் என்றது.\n4. 42-வது திருத்தச் சட்டம் 1976 பிரிவு 368-ன் கீழ் நாடாளுமன்றத்தின் அரசியலமைப்பு திருத்தும் அதிகாரத்திற்கு எந்தவொரு வரம்பும் இல்லை என்று அறிவிக்க முயன்றது.\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டும்",
    "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டும்",
    "1, 3 and 4 only", "1, 3 மற்றும் 4 மட்டும்",
    "1, 2, 3 and 4", "1, 2, 3 மற்றும் 4",
    "D",
    "All four statements are correct chronological milestones in the judicial evolution of the Basic Structure doctrine.",
    "நான்கு கூற்றுகளும் அடிப்படை அமைப்பு கோட்பாட்டின் வளர்ச்சி பற்றிய சரியான காலவரிசை மைல்கற்கள் ஆகும்.",
    "Incorrect. Statement 4 is also correct.", "தவறு. கூற்று 4-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.", "தவறு. கூற்று 1-ம் சரியானது.",
    "Incorrect. Statement 2 is also correct.", "தவறு. கூற்று 2-ம் சரியானது.",
    "Correct. All Statements 1, 2, 3 and 4 are historically true.", "சரி. கூற்றுகள் 1, 2, 3 மற்றும் 4 அனைத்தும் உண்மை.",
    "TNPSC Trap: Minerva Mills case (1980) subsequently invalidated Clauses (4) and (5) of Article 368 added by 42nd CAA, reaffirming that Judicial Review is a Basic Structure.",
    "TNPSC பொறி: மினர்வா மில்ஸ் வழக்கு (1980) 42-வது திருத்தத்தால் பிரிவு 368-ல் சேர்க்கப்பட்ட பிரிவுகளை ரத்து செய்து நீதித்துறை மறுஆய்வு அடிப்படை அமைப்பு என்பதை மீண்டும் உறுதிப்படுத்தியது.",
    "Kesavananda Bharati case was decided by a 13-judge Bench (largest ever in Supreme Court history) by a narrow majority of 7:6 on April 24, 1973.",
    "கேசவாநந்த பாரதி வழக்கு 13 நீதிபதிகள் கொண்ட அமர்வால் (வரலாற்றிலேயே மிகப்பெரியது) 1973 ஏப்ரல் 24 அன்று 7:6 என்ற பெரும்பான்மையில் தீர்ப்பளிக்கப்பட்டது.",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Basic Structure", "Kesavananda Bharati Case", "Golaknath Case", "Four Statement"]
))

# FR_SB_039 (Medium)
questions.append(make_q(
    "FR_SB_039", "Medium",
    "Consider the following statements regarding the Interconnection between Fundamental Rights, Fundamental Duties, and Preamble:\n1. The Preamble sets out the noble goals of Justice, Liberty, Equality, and Fraternity, which are secured primarily through Fundamental Rights in Part III.\n2. Fundamental Rights create obligations on the State, whereas Fundamental Duties under Part IVA create moral and civic obligations on citizens.\n3. The Supreme Court ruled in AIIMS Students Union case (2002) that Fundamental Duties are equally important as Fundamental Rights for constitutional interpretation.\n4. Fundamental Duties can be directly enforced by Supreme Court writs under Article 32 without any statutory legislation.\nWhich of the statements given above are correct?",
    "அடிப்படை உரிமைகள், அடிப்படை கடமைகள் மற்றும் முகப்புரை ஆகியவற்றிற்கு இடையே உள்ள தொடர்பு பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. முகப்புரை நீதி, சுதந்திரம், சமத்துவம், சகோதரத்துவம் ஆகிய உன்னத இலக்குகளை நிர்ணயிக்கிறது, அவை முதன்மையாக பகுதி III-ல் உள்ள அடிப்படை உரிமைகள் மூலம் பெறப்படுகின்றன.\n2. அடிப்படை உரிமைகள் அரசுக்கு கடமைகளை உருவாக்குகின்றன, ஆனால் பகுதி IVA-ன் கீழ் உள்ள அடிப்படை கடமைகள் குடிமக்களுக்கு தர்ம மற்றும் சமூகக் கடமைகளை உருவாக்குகின்றன.\n3. எய்ம்ஸ் மாணவர்கள் சங்க வழக்கில் (2002), அரசியலமைப்பு விளக்கத்திற்கு அடிப்படை உரிமைகளைப் போலவே அடிப்படை கடமைகளும் சம முக்கியத்துவம் வாய்ந்தவை என உச்ச நீதிமன்றம் கூறியது.\n4. எந்தவொரு சட்டமும் இன்றி பிரிவு 32-ன் கீழ் உச்ச நீதிமன்ற பேராணைகள் மூலம் அடிப்படை கடமைகளை நேரடியாக அமல்படுத்த முடியும்.\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டும்",
    "1, 3 and 4 only", "1, 3 மற்றும் 4 மட்டும்",
    "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டும்",
    "1, 2, 3 and 4", "1, 2, 3 மற்றும் 4",
    "A",
    "Statements 1, 2, and 3 are correct. Statement 4 is INCORRECT because Fundamental Duties are NON-JUSTICIABLE; they cannot be enforced directly through writs under Article 32 unless Parliament enacts specific legislation for their enforcement.",
    "கூற்றுகள் 1, 2 மற்றும் 3 சரியானவை. கூற்று 4 தவறு, ஏனெனில் அடிப்படை கடமைகள் நீதிமன்றத்தால் நேரடியாக அமல்படுத்த முடியாதவை (non-justiciable). நாடாளுமன்றச் சட்டம் மூலமே அமல்படுத்த முடியும்.",
    "Correct. Statements 1, 2, and 3 are true; Statement 4 is false.", "சரி. கூற்றுகள் 1, 2 மற்றும் 3 சரி; கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.", "தவறு. கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.", "தவறு. கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.", "தவறு. கூற்று 4 தவறானது.",
    "TNPSC Trap: Fundamental Duties are NON-JUSTICIABLE and cannot be enforced directly via writs under Article 32, unlike Fundamental Rights.",
    "TNPSC பொறி: அடிப்படை உரிமைகளைப் போலன்றி, அடிப்படை கடமைகள் நீதிமன்றங்கள் மூலம் நேரடியாக அமல்படுத்த முடியாதவை (Non-justiciable).",
    "Verma Committee on Fundamental Duties (1999) identified the existence of legal provisions for the implementation of certain Fundamental Duties.",
    "வர்மா குழு (1999) சில அடிப்படை கடமைகளை அமல்படுத்துவதற்கான சட்ட விதிகளின் இருப்பை சுட்டிக்காட்டியது.",
    "Understand", 60, ["Polity", "Fundamental Rights", "Fundamental Duties", "Preamble Connection", "Four Statement"]
))

# FR_SB_040 (Hard)
questions.append(make_q(
    "FR_SB_040", "Hard",
    "Consider the following statements regarding Exceptions to Fundamental Rights (Articles 31A, 31B, 31C, and 33):\n1. Article 31A saves five categories of laws from being challenged on ground of violation of Articles 14 and 19.\n2. Article 31B saves laws included in Ninth Schedule from judicial challenge, subject to the IR Coelho basic structure test.\n3. Article 31C saves laws giving effect to DPSPs in Article 39(b) and 39(c) from Articles 14 and 19.\n4. Article 33 allows Parliament to restrict Fundamental Rights of armed forces personnel, but State Legislatures share equal power under Article 33.\nWhich of the statements given above are correct?",
    "அடிப்படை உரிமைகளுக்கான விதிவிலக்குகள் (பிரிவுகள் 31A, 31B, 31C மற்றும் 33) பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. பிரிவு 31A ஐந்து வகை சட்டங்களை பிரிவுகள் 14 மற்றும் 19-ஐ மீறுகின்றன என்ற சவாலில் இருந்து பாதுகாக்கிறது.\n2. பிரிவு 31B ஒன்பதாவது அட்டவணையில் சேர்க்கப்பட்டுள்ள சட்டங்களை நீதிமன்றச் சவாலில் இருந்து பாதுகாக்கிறது (ஐ.ஆர். கோயல்ஹோ அடிப்படை அமைப்பு சோதனைக்கு உட்பட்டு).\n3. பிரிவு 31C பிரிவு 39(b) மற்றும் 39(c)-ல் உள்ள DPSP-களை அமல்படுத்தும் சட்டங்களை பிரிவுகள் 14 மற்றும் 19-லிருந்து பாதுகாக்கிறது.\n4. பிரிவு 33 முப்படைகளின் அடிப்படை உரிமைகளைக் கட்டுப்படுத்த நாடாளுமன்றத்திற்கு அனுமதிக்கிறது, மேலும் மாநில சட்டமன்றங்களும் பிரிவு 33-ன் கீழ் சம அதிகாரம் கொண்டுள்ளன.\nமேற்கண்ட கூற்றுகளில் எது சரியானது?",
    "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டும்",
    "1, 3 and 4 only", "1, 3 மற்றும் 4 மட்டும்",
    "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டும்",
    "1, 2, 3 and 4", "1, 2, 3 மற்றும் 4",
    "A",
    "Statements 1, 2, and 3 are correct. Statement 4 is INCORRECT because Article 33 confers power EXCLUSIVELY on PARLIAMENT, not State Legislatures.",
    "கூற்றுகள் 1, 2 மற்றும் 3 சரியானவை. கூற்று 4 தவறு, ஏனெனில் பிரிவு 33 நாடாளுமன்றத்திற்கு மட்டுமே பிரத்யேக அதிகாரம் அளிக்கிறது (மாநில சட்டமன்றங்களுக்கு இல்லை).",
    "Correct. Statements 1, 2, and 3 are true; Statement 4 is false.", "சரி. கூற்றுகள் 1, 2 மற்றும் 3 சரி; கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.", "தவறு. கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.", "தவறு. கூற்று 4 தவறானது.",
    "Incorrect. Statement 4 is false.", "தவறு. கூற்று 4 தவறானது.",
    "TNPSC Trap: Article 31C introduced the famous phrase: 'Where Article 31C comes in, Article 14 goes out.'",
    "TNPSC பொறி: பிரிவு 31C புகழ்பெற்ற பழமொழியை அறிமுகப்படுத்தியது: 'பிரிவு 31C உள்ளே வரும்போது, பிரிவு 14 வெளியே செல்கிறது.'",
    "Article 31A was added by 1st CAA 1951 and further amended by 4th, 17th, and 44th Amendments.",
    "பிரிவு 31A 1-வது திருத்தம் 1951 மூலம் சேர்க்கப்பட்டு 4, 17, 44 ஆகிய திருத்தங்கள் மூலம் மேலும் திருத்தப்பட்டது.",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Article 31A", "Article 31B", "Article 31C", "Article 33", "Four Statement"]
))

# Save checkpoint for Part 3 (4-statement)
print(f"Added {len(questions)} Four-Statement questions.")

# ==============================================================================
# PART 4: 5 CORRECT / INCORRECT STATEMENT QUESTIONS (FR_SB_041 to FR_SB_045)
# ==============================================================================

# FR_SB_041 (Easy)
questions.append(make_q(
    "FR_SB_041", "Easy",
    "Which of the following statements regarding Article 17 (Abolition of Untouchability) is correct?",
    "பிரிவு 17 (தீண்டாமை ஒழிப்பு) பற்றிய பின்வரும் கூற்றுகளில் எது சரியானது?",
    "It is a qualified right subject to reasonable restrictions in public interest.", "இது பொது நலன் கருதி நியாயமான கட்டுப்பாடுகளுக்கு உட்பட்ட ஒரு வரையறுக்கப்பட்ட உரிமையாகும்.",
    "It is an absolute right available against both the State and private individuals without any constitutional exception.", "இது எந்தவொரு அரசியலமைப்பு விதிவிலக்கும் இன்றி அரசு மற்றும் தனிநபர்கள் இருவருக்குமே எதிராகக் கிடைக்கும் ஒரு முழுமையான (absolute) உரிமையாகும்.",
    "The offences under Article 17 are non-cognizable and bailable in nature.", "பிரிவு 17-ன் கீழ் உள்ள குற்றங்கள் காவல் துறையால் நேரடியாகக் கைது செய்ய முடியாதவை மற்றும் பிணையில் வரக்கூடியவை.",
    "The term 'Untouchability' is defined in detail under the Protection of Civil Rights Act, 1955.", "சிவில் உரிமைகள் பாதுகாப்புச் சட்டம் 1955-ன் கீழ் 'தீண்டாமை' என்ற சொல் விரிவாக வரையறுக்கப்பட்டுள்ளது.",
    "B",
    "Option B is correct. Article 17 is an absolute Fundamental Right without any constitutional exceptions or reasonable restrictions, and is enforceable against both State and private individuals.",
    "விருப்பம் B சரியானது. பிரிவு 17 என்பது எந்தவொரு விதிவிலக்கும் அல்லது கட்டுப்பாடும் இல்லாத முழுமையான அடிப்படை உரிமையாகும், மேலும் இது அரசு மற்றும் தனிநபர்கள் இருவருக்குமே எதிராக அமல்படுத்தத்தக்கது.",
    "Incorrect. Article 17 is an absolute right, not a qualified right.", "தவறு. பிரிவு 17 வரையறுக்கப்பட்ட உரிமை அல்ல, முழுமையான உரிமை.",
    "Correct. Option B accurately states the absolute nature of Article 17.", "சரி. விருப்பம் B பிரிவு 17-ன் முழுமையான தன்மையைச் சரியாகக் கூறுகிறது.",
    "Incorrect. Offences enforcing Article 17 are cognizable and non-bailable.", "தவறு. பிரிவு 17 குற்றங்கள் நேரடியாகக் கைது செய்யக்கூடியவை (cognizable).",
    "Incorrect. Untouchability is NOT defined in the 1955 Act or Constitution.", "தவறு. 1955 சட்டத்திலோ அரசியலமைப்பிலோ தீண்டாமை வரையறுக்கப்படவில்லை.",
    "TNPSC Trap: Article 17 has NO reasonable restrictions defined in the Constitution. It is one of the few ABSOLUTE rights.",
    "TNPSC பொறி: பிரிவு 17-க்கு அரசியலமைப்பில் நியாயமான கட்டுப்பாடுகள் எதுவும் இல்லை. இது ஒரு முழுமையான (Absolute) உரிமை ஆகும்.",
    "Protection of Civil Rights Act, 1955 prescribes punishment up to 6 months imprisonment or fine for practicing untouchability.",
    "சிவில் உரிமைகள் பாதுகாப்புச் சட்டம் 1955 தீண்டாமையைப் பின்பற்றுவதற்கு 6 மாத சிறை அல்லது அபராதம் தண்டனையாக விதிக்கிறது.",
    "Understand", 60, ["Polity", "Fundamental Rights", "Article 17", "Untouchability", "Correct Statement"]
))

# FR_SB_042 (Medium)
questions.append(make_q(
    "FR_SB_042", "Medium",
    "Which of the following statements regarding Article 18 (Abolition of Titles) is NOT correct?",
    "பிரிவு 18 (பட்டங்கள் ஒழிப்பு) பற்றிய பின்வரும் கூற்றுகளில் எது தவறானது?",
    "It prohibits the State from conferring any title on any person, whether a citizen or a foreigner, except military or academic distinction.", "இராணுவ அல்லது கல்விச் சிறப்பைத் தவிர வேறு எந்தப் பட்டத்தையும் குடிமகன் அல்லது வெளிநாட்டவருக்கு அரசு வழங்குவதை இது தடை செய்கிறது.",
    "A citizen of India can accept a title from any foreign State with the prior consent of the Prime Minister.", "இந்தியக் குடிமகன் ஒருவர் பிரதமரின் முன் அனுமதியுடன் எந்தவொரு வெளிநாட்டிலிருந்தும் பட்டத்தைப் பெறலாம்.",
    "No foreigner holding any office of profit under the State can accept any present or title from a foreign State without the consent of the President.", "அரசின் கீழ் ஆதாயம் தரும் பதவியிலுள்ள எந்தவொரு வெளிநாட்டவரும் குடியரசுத் தலைவரின் ஒப்புதலின்றி வெளிநாட்டிலிருந்து பரிசோ அல்லது பட்டத்தையோ பெற முடியாது.",
    "National Awards like Bharat Ratna and Padma Vibhushan cannot be used as prefixes or suffixes to the awardee's name.", "பாரத ரத்னா மற்றும் பத்ம விபூஷன் போன்ற தேசிய விருதுகளை விருது பெற்றவரின் பெயருக்கு முன்னாலோ பின்னாலோ பயன்படுத்தக் கூடாது.",
    "B",
    "Option B is NOT correct because Article 18(2) strictly prohibits a citizen of India from accepting ANY title from any foreign State, and NO consent of Prime Minister or President can waive this absolute prohibition for citizens.",
    "விருப்பம் B தவறானது. ஏனெனில் பிரிவு 18(2) இந்தியக் குடிமகன் வெளிநாட்டிலிருந்து பட்டம் பெறுவதை முற்றிலுமாகத் தடை செய்கிறது; பிரதமர் அனுமதியுடன் கூட பெற முடியாது.",
    "Incorrect. Statement A is correct.", "தவறு. விருப்பம் A சரியானது.",
    "Correct. Option B is INCORRECT because citizen cannot accept foreign titles under any circumstances.", "சரி. விருப்பம் B தவறானது, ஏனெனில் குடிமக்கள் எந்தச் சூழ்நிலையிலும் வெளிநாட்டுப் பட்டங்களைப் பெற முடியாது.",
    "Incorrect. Statement C is correct under Art 18(3).", "தவறு. விருப்பம் C சரியானது.",
    "Incorrect. Statement D is correct under Balaji Raghavan case.", "தவறு. விருப்பம் D சரியானது.",
    "TNPSC Trap: Indian citizens CANNOT accept foreign titles under any circumstance (Art 18(2)). Foreigners holding office under Indian State require PRESIDENT's consent for foreign gifts/titles (Art 18(3)&(4)).",
    "TNPSC பொறி: இந்தியக் குடிமக்கள் எந்தச் சூழ்நிலையிலும் வெளிநாட்டுப் பட்டங்களைப் பெற முடியாது. இந்தியாவில் பணியாற்றும் வெளிநாட்டினர் குடியரசுத் தலைவர் அனுமதியைப் பெற வேண்டும்.",
    "Article 18 does not create any criminal penalty; Parliament can enact legislation specifying penalties for violating Article 18.",
    "பிரிவு 18 குற்றவியல் தண்டனையை உருவாக்கவில்லை; நாடாளுமன்றம் சட்டம் மூலம் தண்டனையை நிர்ணயிக்கலாம்.",
    "Understand", 60, ["Polity", "Fundamental Rights", "Article 18", "Titles", "Incorrect Statement"]
))

# FR_SB_043 (Medium)
questions.append(make_q(
    "FR_SB_043", "Medium",
    "Which of the following statements regarding Article 21A (Right to Education) is correct?",
    "பிரிவு 21A (கல்வி உரிமை) பற்றிய பின்வரும் கூற்றுகளில் எது சரியானது?",
    "It covers higher and professional education up to graduation level.", "இது பட்டப்படிப்பு வரையிலான உயர்கல்வி மற்றும் தொழில்முறைக் கல்வியை உள்ளடக்கியது.",
    "It requires the State to provide free and compulsory education to all children aged 6 to 14 years in such manner as the State may by law determine.", "மாநில அரசு சட்டத்தால் நிர்ணயிக்கும் வகையில் 6 முதல் 14 வயதுடைய அனைத்து குழந்தைகளுக்கும் இலவச மற்றும் கட்டாயக் கல்வியை வழங்க அரசு கடமைப்பட்டுள்ளது.",
    "It was part of the original Constitution drafted in 1949 under Part III.", "இது 1949-ல் வரைவு செய்யப்பட்ட மூல அரசியலமைப்பின் பகுதி III-ல் ஒரு பகுதியாக இருந்தது.",
    "It applies only to children belonging to SC, ST, and Economically Weaker Sections.", "இது SC, ST மற்றும் பொருளாதாரத்தில் பின்தங்கிய பிரிவைச் சேர்ந்த குழந்தைகளுக்கு மட்டுமே பொருந்தும்.",
    "B",
    "Option B is correct. Article 21A states that the State shall provide free and compulsory education to ALL children of the age of 6 to 14 years in such manner as the State may by law determine. It was added by 86th CAA 2002.",
    "விருப்பம் B சரியானது. பிரிவு 21A 6 முதல் 14 வயதுடைய அனைத்து குழந்தைகளுக்கும் அரசு சட்டத்தால் நிர்ணயிக்கும் முறையில் இலவச கட்டாயக் கல்வி வழங்க உத்தரவாதம் அளிக்கிறது. 86-வது திருத்தம் 2002 மூலம் சேர்க்கப்பட்டது.",
    "Incorrect. Art 21A covers elementary education (6-14 years), not higher/graduation education.", "தவறு. 21A தொடக்கக் கல்வியை (6-14 வயது) மட்டுமே உள்ளடக்கும், உயர்கல்வியை அல்ல.",
    "Correct. Option B accurately states the text of Article 21A.", "சரி. விருப்பம் B பிரிவு 21A-ன் சரியான உரையை விவரிக்கிறது.",
    "Incorrect. Art 21A was added in 2002 by 86th CAA, not in original 1949 text.", "தவறு. பிரிவு 21A 2002-ல் தான் சேர்க்கப்பட்டது, மூல அரசியலமைப்பில் இல்லை.",
    "Incorrect. Art 21A applies to ALL children aged 6-14, regardless of category.", "தவறு. 21A சாதி/பொருளாதார பாகுபாடின்றி அனைத்து குழந்தைகளுக்கும் பொருந்தும்.",
    "TNPSC Trap: Article 21A provides for ELEMENTARY education (ages 6 to 14 ONLY), NOT higher or professional education.",
    "TNPSC பொறி: பிரிவு 21A தொடக்கக் கல்வியை மட்டுமே (6 முதல் 14 வயது வரை) வழங்குகிறது, உயர் அல்லது தொழில்முறைக் கல்வியை அல்ல.",
    "RTE Act 2009 mandates 25% reservation for children from disadvantaged groups in private unaided entry-level school admissions.",
    "RTE சட்டம் 2009 தனியார் சுயநிதிப் பள்ளிகளின் சேர்க்கையில் 25% இடத்தை நலிவடைந்த குழந்தைகளுக்காக ஒதுக்க உத்தரவிடுகிறது.",
    "Understand", 60, ["Polity", "Fundamental Rights", "Article 21A", "RTE Act", "Correct Statement"]
))

# FR_SB_044 (Hard)
questions.append(make_q(
    "FR_SB_044", "Hard",
    "Which of the following statements regarding Article 35 of the Indian Constitution is correct?",
    "இந்திய அரசியலமைப்பின் 35-வது பிரிவைக் குறித்து பின்வரும் கூற்றுகளில் எது சரியானது?",
    "Power to make laws prescribing punishment for offences under Part III (e.g., untouchability, begar) lies exclusively with Parliament to maintain uniformity across India.", "பகுதி III-ன் கீழ் உள்ள குற்றங்களுக்கு (எ.கா. தீண்டாமை, வெட்டி வேலை) தண்டனை விதிக்க சட்டங்களை இயற்றும் அதிகாரம் இந்தியா முழுவதும் ஒரே மாதிரியான தன்மையைப் பேண நாடாளுமன்றத்திற்கு மட்டுமே உள்ளது.",
    "Both Parliament and State Legislatures have concurrent powers to make laws prescribing punishment for offences under Part III.", "பகுதி III குற்றங்களுக்குத் தண்டனை விதிக்க நாடாளுமன்றம் மற்றும் மாநில சட்டமன்றங்கள் இரண்டிற்குமே சம அதிகாரங்கள் உள்ளன.",
    "Article 35 allows State Legislatures to restrict Fundamental Rights of state police forces.", "பிரிவு 35 மாநில காவல் படைகளின் அடிப்படை உரிமைகளைக் கட்டுப்படுத்த மாநில சட்டமன்றங்களுக்கு அனுமதிக்கிறது.",
    "Laws in force prior to the Constitution regarding punishment for Part III offences automatically lapsed on January 26, 1950.", "பகுதி III குற்றங்களுக்கான தண்டனை குறித்து அரசியலமைப்புக்கு முன் அமலிலிருந்த சட்டங்கள் 1950 ஜனவரி 26 அன்று தானாகவே ரத்தாயின.",
    "A",
    "Option A is correct. Article 35 specifies that Parliament ALONE (and NOT State Legislatures) shall have power to make laws prescribing punishment for acts declared as offences under Part III (such as Articles 17 and 23), ensuring uniform law across India.",
    "விருப்பம் A சரியானது. பிரிவு 35 பகுதி III குற்றங்களுக்கு (பிரிவுகள் 17, 23) தண்டனை விதிக்கும் சட்டங்களை இயற்றும் பிரத்யேக அதிகாரத்தை நாடாளுமன்றத்திற்கு மட்டுமே வழங்குகிறது (மாநில சட்டமன்றங்களுக்கு இல்லை).",
    "Correct. Option A accurately reflects Article 35 exclusive Parliamentary jurisdiction.", "சரி. விருப்பம் A நாடாளுமன்றத்தின் பிரத்யேக அதிகாரத்தைச் சரியாக விவரிக்கிறது.",
    "Incorrect. State Legislatures have NO power under Article 35.", "தவறு. பிரிவு 35-ன் கீழ் மாநில சட்டமன்றங்களுக்கு அதிகாரமில்லை.",
    "Incorrect. Power to restrict armed forces/police FRs lies under Art 33 with Parliament, not Art 35 with State Legislature.", "தவறு. படைகளின் உரிமைகளைக் கட்டுப்படுத்தும் அதிகாரம் பிரிவு 33-ன் கீழ் நாடாளுமன்றத்திற்கு உண்டு.",
    "Incorrect. Art 35(b) continues pre-constitutional laws until altered or repealed by Parliament.", "தவறு. நாடாளுமன்றம் மாற்றும் வரை பழைய சட்டங்கள் தொடரும்.",
    "TNPSC Trap: Article 35 ensures that punishment for violating Fundamental Rights (like Untouchability or Begar) is UNIFORM throughout India by giving legislative power EXCLUSIVELY to Parliament.",
    "TNPSC பொறி: இந்தியா முழுவதும் தண்டனை ஒரே மாதிரியாக இருக்க வேண்டும் என்பதற்காக பிரிவு 35 சட்டமியற்றும் அதிகாரத்தை நாடாளுமன்றத்திற்கு மட்டுமே வழங்குகிறது.",
    "Article 35 also covers laws under Art 16(3) (residence), Art 32(3) (writs power to lower courts), and Art 33 (armed forces).",
    "பிரிவு 35 பிரிவு 16(3), பிரிவு 32(3) மற்றும் பிரிவு 33 ஆகியவற்றிற்கான சட்டங்களையும் உள்ளடக்கியது.",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Article 35", "Parliament Power", "Correct Statement"]
))

# FR_SB_045 (Hard)
questions.append(make_q(
    "FR_SB_045", "Hard",
    "Which of the following statements regarding Article 300A (Right to Property) is NOT correct?",
    "பிரிவு 300A (சொத்துரிமை) பற்றிய பின்வரும் கூற்றுகளில் எது தவறானது?",
    "No person shall be deprived of his property save by authority of law.", "சட்டத்தின் அதிகாரத்தின் மூலமே தவிர வேறு எந்த வகையிலும் ஒரு நபரின் சொத்து பறிக்கப்படக் கூடாது.",
    "It is a legal/constitutional right, but not a Fundamental Right.", "இது ஒரு சட்டப்பூர்வ/அரசியலமைப்பு உரிமை, ஆனால் அடிப்படை உரிமை அல்ல.",
    "In case of violation of Article 300A, an aggrieved person can directly move the Supreme Court under Article 32.", "பிரிவு 300A மீறப்படும் பட்சத்தில், பாதிக்கப்பட்ட நபர் நேரடியாக பிரிவு 32-ன் கீழ் உச்ச நீதிமன்றத்தை அணுகலாம்.",
    "Executive action depriving property without statutory law backing is unconstitutional and invalid.", "சட்டப்பூர்வ ஆதரவின்றி சொத்தைப் பறிக்கும் நிர்வாக நடவடிக்கை அரசியலமைப்புக்கு எதிரானது மற்றும் செல்லாதது.",
    "C",
    "Option C is NOT correct because since Right to Property is no longer a Fundamental Right, a person CANNOT directly move the Supreme Court under Article 32. He can only move High Court under Article 226 or file an ordinary civil suit.",
    "விருப்பம் C தவறானது. ஏனெனில் சொத்துரிமை இப்போது அடிப்படை உரிமை இல்லாததால், பாதிக்கப்பட்ட நபர் நேரடியாக பிரிவு 32-ன் கீழ் உச்ச நீதிமன்றத்தை அணுக முடியாது (பிரிவு 226-ன் கீழ் உயர் நீதிமன்றத்தை மட்டுமே அணுக முடியும்).",
    "Incorrect. Statement A is correct under Art 300A text.", "தவறு. விருப்பம் A சரியானது.",
    "Incorrect. Statement B is correct (legal right in Part XII).", "தவறு. விருப்பம் B சரியானது.",
    "Correct. Option C is INCORRECT because Art 32 is reserved for Fundamental Rights only.", "சரி. பிரிவு 32 அடிப்படை உரிமைகளுக்கு மட்டுமே என்பதால் விருப்பம் C தவறானது.",
    "Incorrect. Statement D is correct (law authority required).", "தவறு. விருப்பம் D சரியானது.",
    "TNPSC Trap: Violation of Article 300A CANNOT be challenged directly under Article 32 in Supreme Court (Art 32 is for Part III FRs only). Remedy lies under Article 226 in High Court.",
    "TNPSC பொறி: பிரிவு 300A மீறலை நேரடியாக பிரிவு 32-ன் கீழ் உச்ச நீதிமன்றத்தில் சவால் செய்ய முடியாது. பிரிவு 226-ன் கீழ் உயர் நீதிமன்றத்திலேயே சவால் செய்ய முடியும்.",
    "Article 300A was placed in Part XII (Finance, Property, Contracts and Suits) by the 44th Constitutional Amendment Act, 1978.",
    "44-வது திருத்தச் சட்டம் 1978 மூலம் பிரிவு 300A பகுதி XII-ல் (நிதி, சொத்து, ஒப்பந்தங்கள்) சேர்க்கப்பட்டது.",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Article 300A", "Right to Property", "Incorrect Statement"]
))

# Save checkpoint for Part 4
print(f"Added {len(questions)} Correct/Incorrect questions.")

# ==============================================================================
# PART 5: 5 ASSERTION / INFERENCE-STYLE STATEMENT QUESTIONS (FR_SB_046 to FR_SB_050)
# ==============================================================================

# FR_SB_046 (Medium)
questions.append(make_q(
    "FR_SB_046", "Medium",
    "Consider the following assertion and reason statements regarding Article 14:\nAssertion (A): Article 14 strikes at arbitrariness in State action and ensures fairness and equality of treatment.\nReason (R): Equality is a dynamic concept with many aspects and dimensions, and it cannot be 'cribbed, cabined and confined' within traditional limits.\nWhich one of the following is correct?",
    "பிரிவு 14 பற்றிய கூற்று மற்றும் காரணத்தைக் கவனியுங்கள்:\nகூற்று (A): பிரிவு 14 அரசின் தன்னிச்சையான நடவடிக்கைகளைத் தடுத்து, நியாயமான மற்றும் சமமான நடத்தையை உறுதி செய்கிறது.\nகாரணம் (R): சமத்துவம் என்பது பல அம்சங்களைக் கொண்ட ஒரு இயங்கு தன்மையுடைய (dynamic) கருத்தாகும், அதை பாரம்பரிய எல்லைகளுக்குள் அடைத்து வைக்க முடியாது.\nகீழ்கண்டவற்றில் எது சரியானது?",
    "Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மேலும் (R) என்பது (A)-வின் சரியான விளக்கமாகும்.",
    "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல.",
    "(A) is true, but (R) is false.", "(A) உண்மை, ஆனால் (R) தவறு.",
    "(A) is false, but (R) is true.", "(A) தவறு, ஆனால் (R) உண்மை.",
    "A",
    "Option A is correct. In EP Royappa case (1974) and Maneka Gandhi case (1978), Justice Bhagwati laid down the new doctrine of equality: Equality is dynamic and anti-arbitrariness is the core essence of Article 14.",
    "விருப்பம் A சரியானது. ஈ.பி. ராயப்பா (1974) மற்றும் மேனகா காந்தி (1978) வழக்குகளில் நீதிபதி பகவதி புதிய சமத்துவக் கோட்பாட்டை வழங்கினார்: சமத்துவமின்மை மற்றும் தன்னிச்சையான செயல்களுக்கு எதிரானதே பிரிவு 14.",
    "Correct. Both (A) and (R) are true and (R) correctly explains the non-arbitrariness doctrine of Article 14.", "சரி. (A) மற்றும் (R) இரண்டும் உண்மை, மேலும் (R) சரியான விளக்கமாகும்.",
    "Incorrect. (R) is indeed the direct explanation of (A).", "தவறு. (R) என்பது (A)-வின் நேரடி விளக்கமாகும்.",
    "Incorrect. Both statements are true.", "தவறு. இரண்டு கூற்றுகளும் உண்மையாகும்.",
    "Incorrect. Assertion (A) is true.", "தவறு. கூற்று (A) உண்மையாகும்.",
    "TNPSC Trap: The 'New Doctrine of Equality' (non-arbitrariness) was propounded by Supreme Court in EP Royappa case (1974) and reaffirmed in Maneka Gandhi case (1978).",
    "TNPSC பொறி: சமத்துவத்தின் புதிய கோட்பாட்டை (தன்னிச்சையின்மை) உச்ச நீதிமன்றம் ஈ.பி. ராயப்பா வழக்கில் (1974) உருவாக்கியது.",
    "Equality and arbitrariness are sworn enemies: 'where an act is arbitrary, it is implicit that it is unequal both according to political logic and constitutional law.'",
    "சமத்துவமும் தன்னிச்சையான செயலும் எதிரெதிர் துருவங்கள்: தன்னிச்சையான செயல் சமத்துவமற்றது.",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Article 14", "EP Royappa Case", "Non-Arbitrariness", "Assertion Reason"]
))

# FR_SB_047 (Hard)
questions.append(make_q(
    "FR_SB_047", "Hard",
    "Consider the following assertion and reason statements regarding Article 20(1):\nAssertion (A): Parliament can enact civil laws or tax legislation with retrospective effect imposing financial liabilities on citizens.\nReason (R): Protection against ex-post facto laws under Article 20(1) is restricted strictly to criminal legislation imposing penalties for past acts.\nWhich one of the following is correct?",
    "பிரிவு 20(1) பற்றிய கூற்று மற்றும் காரணத்தைக் கவனியுங்கள்:\nகூற்று (A): குடிமக்கள் மீது நிதிப் பொறுப்புகளை விதிக்கும் சிவில் சட்டங்கள் அல்லது வரிச் சட்டங்களை நாடாளுமன்றம் பின்னோக்கிய விளைவுடன் (retrospective effect) இயற்ற முடியும்.\nகாரணம் (R): பிரிவு 20(1)-ன் கீழ் பின்னோக்கிய விளைவு சட்டங்களுக்கு எதிரான பாதுகாப்பு குற்றவியல் சட்டங்களுக்கு மட்டுமே பிரத்யேகமாக வரம்பிற்குட்படுத்தப்பட்டுள்ளது.\nகீழ்கண்டவற்றில் எது சரியானது?",
    "Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மேலும் (R) என்பது (A)-வின் சரியான விளக்கமாகும்.",
    "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல.",
    "(A) is true, but (R) is false.", "(A) உண்மை, ஆனால் (R) தவறு.",
    "(A) is false, but (R) is true.", "(A) தவறு, ஆனால் (R) உண்மை.",
    "A",
    "Option A is correct. Article 20(1) prohibits retrospective criminal laws (penalties), but DOES NOT prohibit retrospective civil or tax laws. Thus Parliament can impose retrospective tax liabilities, and Reason (R) explains why Assertion (A) is constitutionally valid.",
    "விருப்பம் A சரியானது. பிரிவு 20(1) குற்றவியல் சட்டங்களை மட்டுமே பின்னோக்கி அமல்படுத்துவதைத் தடுக்கிறது. சிவில்/வரிச் சட்டங்களைப் பின்னோக்கி அமல்படுத்தலாம் என்பதால் (R) என்பது (A)-வின் சரியான விளக்கமாகும்.",
    "Correct. Both (A) and (R) are true and (R) directly explains why retrospective tax laws are permitted.", "சரி. (A) மற்றும் (R) இரண்டும் உண்மை, மேலும் (R) சரியான விளக்கமாகும்.",
    "Incorrect. (R) is the precise reason for (A).", "தவறு. (R) என்பது (A)-க்கான சரியான காரணமாகும்.",
    "Incorrect. Both statements are true.", "தவறு. இரண்டு கூற்றுகளும் உண்மையாகும்.",
    "Incorrect. Both statements are true.", "தவறு. இரண்டு கூற்றுகளும் உண்மையாகும்.",
    "TNPSC Trap: Article 20(1) protection applies ONLY to conviction or sentence under CRIMINAL laws. Tax laws and civil liabilities CAN be imposed retrospectively.",
    "TNPSC பொறி: பிரிவு 20(1) பாதுகாப்பு குற்றவியல் சட்டங்களுக்கு மட்டுமே பொருந்தும். வரிச் சட்டங்களைப் பின்னோக்கிய தேதியிலிருந்து விதிக்க முடியும்.",
    "Article 20(1) also protects against an increase in penalty beyond what was prescribed at the time of commission of the act.",
    "பிரிவு 20(1) குற்றம் செய்த நேரத்தில் இருந்த தண்டனையை விட அதிக தண்டனை விதிப்பதிலிருந்தும் பாதுகாக்கிறது.",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Article 20(1)", "Ex-Post Facto Law", "Tax Laws", "Assertion Reason"]
))

# FR_SB_048 (Hard)
questions.append(make_q(
    "FR_SB_048", "Hard",
    "Consider the following assertion and reason statements regarding Writ of Mandamus:\nAssertion (A): A Writ of Mandamus cannot be issued by the Supreme Court or High Court to compel the President of India or a State Governor to perform their official duties.\nReason (R): Article 361 of the Constitution accords complete personal immunity to the President and Governors from answerability to any court for the performance of their official powers and duties.\nWhich one of the following is correct?",
    "கட்டளைப் பேராணை (Mandamus) பற்றிய கூற்று மற்றும் காரணத்தைக் கவனியுங்கள்:\nகூற்று (A): இந்தியக் குடியரசுத் தலைவர் அல்லது மாநில ஆளுநரைத் தங்களது அதிகாரப்பூர்வ பணிகளைச் செய்ய வற்புறுத்தி உச்ச அல்லது உயர் நீதிமன்றங்கள் கட்டளைப் பேராணையை வெளியிட முடியாது.\nகாரணம் (R): அரசியலமைப்பின் பிரிவு 361 குடியரசுத் தலைவர் மற்றும் ஆளுநர்களுக்குத் தங்களது அதிகாரப்பூர்வ கடமைகளைச் செய்வதற்காக எந்தவொரு நீதிமன்றத்திற்கும் பதிலளிக்க வேண்டியதில்லை என்ற முழுமையான விலக்களிப்பை வழங்குகிறது.\nகீழ்கண்டவற்றில் எது சரியானது?",
    "Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மேலும் (R) என்பது (A)-வின் சரியான விளக்கமாகும்.",
    "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல.",
    "(A) is true, but (R) is false.", "(A) உண்மை, ஆனால் (R) தவறு.",
    "(A) is false, but (R) is true.", "(A) தவறு, ஆனால் (R) உண்மை.",
    "A",
    "Option A is correct. Mandamus does not lie against President/Governors because Article 361 provides them immunity from court proceedings for exercise of official powers and duties.",
    "விருப்பம் A சரியானது. பிரிவு 361 குடியரசுத் தலைவர் மற்றும் ஆளுநர்களுக்கு நீதிமன்றப் பதிலளிப்பிலிருந்து பாதுகாப்பு அளிப்பதால் அவர்களுக்கு எதிராக கட்டளைப் பேராணை பிறப்பிக்க முடியாது; எனவே (R) என்பது (A)-வின் சரியான விளக்கமாகும்.",
    "Correct. Both (A) and (R) are true and (R) provides the constitutional justification under Article 361.", "சரி. (A) மற்றும் (R) இரண்டும் உண்மை, மேலும் பிரிவு 361-ன் கீழ் (R) சரியான விளக்கமாகும்.",
    "Incorrect. (R) directly explains (A).", "தவறு. (R) நேரடியாக (A)-வை விளக்குகிறது.",
    "Incorrect. Both statements are true.", "தவறு. இரண்டு கூற்றுகளும் உண்மையாகும்.",
    "Incorrect. Assertion (A) is true.", "தவறு. கூற்று (A) உண்மையாகும்.",
    "TNPSC Trap: Mandamus CANNOT be issued against: 1. Private individuals, 2. Departmental instruction without statutory force, 3. Discretionary duties, 4. President or Governors, 5. Chief Justice acting in judicial capacity.",
    "TNPSC பொறி: கட்டளைப் பேராணை பின்வருவனவற்றிற்கு எதிராக வெளியிட முடியாது: 1. தனியார் தனிநபர்கள், 2. சட்டப்பூர்வ ஆதரவில்லாத உத்தரவுகள், 3. விருப்ப உரிமைகள், 4. குடியரசுத் தலைவர்/ஆளுநர்கள், 5. தலைமை நீதிபதி.",
    "Article 361 immunity does not restrict the right of any person to bring appropriate proceedings against the Government of India or State Government.",
    "பிரிவு 361 பாதுகாப்பு இந்திய அரசு அல்லது மாநில அரசுக்கு எதிராக வழக்குத் தொடுக்கும் உரிமையைத் தடுக்காது.",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Mandamus Writ", "Article 361", "Presidential Immunity", "Assertion Reason"]
))

# FR_SB_049 (Hard)
questions.append(make_q(
    "FR_SB_049", "Hard",
    "Consider the following assertion and reason statements regarding Article 31C:\nAssertion (A): The Supreme Court struck down Section 4 of the 42nd Amendment Act 1976 which gave primacy to all Directive Principles over Articles 14 and 19.\nReason (R): Harmony and balance between Fundamental Rights (Part III) and Directive Principles (Part IV) is an essential feature of the Basic Structure of the Constitution.\nWhich one of the following is correct?",
    "பிரிவு 31C பற்றிய கூற்று மற்றும் காரணத்தைக் கவனியுங்கள்:\nகூற்று (A): பிரிவுகள் 14 மற்றும் 19-ஐ விட அனைத்து அரசு வழிகாட்டு நெறிமுறைகளுக்கும் முன்னுரிமை அளித்த 42-வது திருத்தச் சட்டம் 1976-ன் பிரிவு 4-ஐ உச்ச நீதிமன்றம் ரத்து செய்தது.\nகாரணம் (R): அடிப்படை உரிமைகள் (பகுதி III) மற்றும் அரசு வழிகாட்டு நெறிமுறைகள் (பகுதி IV) இடையேயான அமைதியும் சமநிலையும் அரசியலமைப்பின் அடிப்படை அமைப்பின் (Basic Structure) இன்றியமையாத அம்சமாகும்.\nகீழ்கண்டவற்றில் எது சரியானது?",
    "Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மேலும் (R) என்பது (A)-வின் சரியான விளக்கமாகும்.",
    "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல.",
    "(A) is true, but (R) is false.", "(A) உண்மை, ஆனால் (R) தவறு.",
    "(A) is false, but (R) is true.", "(A) தவறு, ஆனால் (R) உண்மை.",
    "A",
    "Option A is correct. In Minerva Mills case (1980), Supreme Court struck down Sec 4 of 42nd CAA because disturbing the balance between Part III and Part IV violates the Basic Structure of the Constitution.",
    "விருப்பம் A சரியானது. மினர்வா மில்ஸ் வழக்கில் (1980) பகுதி III மற்றும் பகுதி IV இடையேயான சமநிலையைக் குலைப்பது அடிப்படை அமைப்பை மீறுவதாகும் எனக் கூறி 42-வது திருத்தத்தின் பிரிவு 4 ரத்து செய்யப்பட்டது.",
    "Correct. Both (A) and (R) are true and (R) explains why Section 4 of 42nd CAA was invalidated.", "சரி. (A) மற்றும் (R) இரண்டும் உண்மை, மேலும் (R) 42வது திருத்தப் பிரிவு 4 ரத்து செய்யப்பட்ட காரணத்தை விளக்குகிறது.",
    "Incorrect. (R) is the exact rationale used by the Supreme Court.", "தவறு. (R) என்பது உச்ச நீதிமன்றம் பயன்படுத்திய சரியான காரணமாகும்.",
    "Incorrect. Both statements are true.", "தவறு. இரண்டு கூற்றுகளும் உண்மையாகும்.",
    "Incorrect. Assertion (A) is true.", "தவறு. கூற்று (A) உண்மையாகும்.",
    "TNPSC Trap: Article 31C in its original form (protecting only Art 39(b) and 39(c)) remains VALID, but its expanded form (protecting ALL DPSPs) was struck down in Minerva Mills.",
    "TNPSC பொறி: பிரிவு 31C-ன் மூல வடிவம் (பிரிவு 39(b) & (c) பாதுகாப்பது) செல்லுபடியாகும்; ஆனால் அதன் விரிவாக்கப்பட்ட வடிவம் (அனைத்து DPSP-களும்) மினர்வா மில்ஸ் வழக்கில் ரத்து செய்யப்பட்டது.",
    "Part III and Part IV are like two wheels of a chariot; one is no less important than the other.",
    "பகுதி III மற்றும் பகுதி IV ஆகியவை ஒரு தேரின் இரு சக்கரங்கள் போன்றவை; ஒன்று மற்றொன்றை விடக் குறைந்ததல்ல.",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Article 31C", "Minerva Mills Case", "FR vs DPSP", "Assertion Reason"]
))

# FR_SB_050 (Hard)
questions.append(make_q(
    "FR_SB_050", "Hard",
    "Consider the following assertion and reason statements regarding Amendability of Fundamental Rights:\nAssertion (A): Parliament can amend or abridge any Fundamental Right guaranteed under Part III of the Constitution using its constituent power under Article 368.\nReason (R): The power of constitutional amendment under Article 368 is absolute and unconstrained, allowing Parliament to alter even the core basic identity of the Constitution.\nWhich one of the following is correct?",
    "அடிப்படை உரிமைகளைத் திருத்தும் அதிகாரம் பற்றிய கூற்று மற்றும் காரணத்தைக் கவனியுங்கள்:\nகூற்று (A): பிரிவு 368-ன் கீழ் உள்ள தனது அரசியலமைப்பு திருத்தும் அதிகாரத்தைப் பயன்படுத்தி பகுதி III-ன் கீழ் உள்ள எந்தவொரு அடிப்படை உரிமையையும் நாடாளுமன்றம் திருத்தவோ குறைக்கவோ முடியும்.\nகாரணம் (R): பிரிவு 368-ன் கீழ் அரசியலமைப்பு திருத்தும் அதிகாரம் வரம்பற்றது மற்றும் முழுமையானது, இதனால் அரசியலமைப்பின் மைய அடிப்படை அடையாளத்தைக் கூட நாடாளுமன்றத்தால் மாற்ற முடியும்.\nகீழ்கண்டவற்றில் எது சரியானது?",
    "Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மேலும் (R) என்பது (A)-வின் சரியான விளக்கமாகும்.",
    "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல.",
    "(A) is true, but (R) is false.", "(A) உண்மை, ஆனால் (R) தவறு.",
    "(A) is false, but (R) is true.", "(A) தவறு, ஆனால் (R) உண்மை.",
    "C",
    "Statement (A) is TRUE (Parliament can amend any FR as per Kesavananda Bharati case). Reason (R) is FALSE because Article 368 constituent power is NOT unconstrained; it is subject to the limitation that Parliament CANNOT alter, damage, or destroy the 'Basic Structure' of the Constitution.",
    "கூற்று (A) உண்மை (கேசவாநந்த பாரதி வழக்கின் படி அடிப்படை உரிமைகளை நாடாளுமன்றம் திருத்தலாம்). காரணம் (R) தவறு, ஏனெனில் பிரிவு 368-ன் கீழ் நாடாளுமன்றத்தின் அதிகாரம் வரம்பற்றது அல்ல; அரசியலமைப்பின் 'அடிப்படை அமைப்பை' நாடாளுமன்றத்தால் மாற்ற முடியாது.",
    "Incorrect. Reason (R) is false.", "தவறு. காரணம் (R) தவறானது.",
    "Incorrect. Reason (R) is false.", "தவறு. காரணம் (R) தவறானது.",
    "Correct. Assertion (A) is true; Reason (R) is false as amendment power is limited by Basic Structure doctrine.", "சரி. கூற்று (A) உண்மை; அடிப்படை அமைப்பு கோட்பாட்டால் திருத்தும் அதிகாரம் வரம்பிற்குட்படுத்தப்பட்டுள்ளதால் காரணம் (R) தவறு.",
    "Incorrect. Assertion (A) is true.", "தவறு. கூற்று (A) உண்மையாகும்.",
    "TNPSC Trap: Parliament has power to amend Fundamental Rights under Art 368, BUT that power is limited by the Basic Structure doctrine (Kesavananda Bharati 1973).",
    "TNPSC பொறி: நாடாளுமன்றத்திற்கு அடிப்படை உரிமைகளைத் திருத்தும் அதிகாரம் உண்டு, ஆனால் அந்த அதிகாரம் அடிப்படை அமைப்பு கோட்பாட்டிற்கு உட்பட்டது.",
    "Limited amending power of Parliament is itself a Basic Feature of the Constitution.",
    "நாடாளுமன்றத்தின் வரம்பிற்குட்பட்ட திருத்தும் அதிகாரமே அரசியலமைப்பின் ஒரு அடிப்படை அம்சமாகும்.",
    "Analyze", 60, ["Polity", "Fundamental Rights", "Basic Structure", "Kesavananda Bharati Case", "Article 368", "Assertion Reason"]
))

# Save full 50 questions dataset
print(f"Total questions compiled: {len(questions)}")
assert len(questions) == 50, f"Expected 50 questions, got {len(questions)}"

with open(target_path, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"✅ Successfully wrote 50 MCQs to {target_path}")
