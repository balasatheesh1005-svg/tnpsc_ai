# -*- coding: utf-8 -*-
"""
Builder script for 25 TNPSC Group 1 Standard Reasoning / Assertion & Reason MCQs
Topic: Preamble of the Constitution of India
Target Files:
  - data/questions/polity/preamble_assertion_reason.json
  - data/questions/polity/preamble_reasoning.json
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Import existing Q1-Q10 from first build
from build_preamble_reasoning_25 import questions as q_1_to_10

remaining_questions = [
    # =========================================================================
    # Q11: PRE_AR_011 (Answer: A) - Kesavananda Bharati Reversal
    # =========================================================================
    {
        "id": "PRE_AR_011",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Assertion & Reason",
        "question": {
            "en": "Assertion (A): In the Kesavananda Bharati Case (1973), the Supreme Court rejected the earlier Berubari opinion and held that the Preamble IS an integral part of the Constitution.\nReason (R): The Supreme Court recognized that the Preamble was debated, voted upon, and enacted by the Constituent Assembly through the exact same constituent procedure as any other part of the Constitution.",
            "ta": "கூற்று (A): கேசவானந்த பாரதி வழக்கில் (1973), உச்ச நீதிமன்றம் முந்தைய பெருபாரி ஆலோசனைக் கருத்தை நிராகரித்து, முகவுரை அரசியலமைப்பின் ஒரு ஒருங்கிணைந்த பகுதி என்று தீர்ப்பளித்தது.\nகாரணம் (R): அரசியலமைப்பின் மற்ற பகுதிகளைப் போலவே அதே அரசியலமைப்பு நடைமுறையின் மூலம் அரசியலமைப்பு நிர்ணய அவையால் முகவுரையும் விவாதிக்கப்பட்டு, வாக்களிக்கப்பட்டு, இயற்றப்பட்டது என்பதை உச்ச நீதிமன்றம் அங்கீகரித்தது."
        },
        "options": [
            {"id": "A", "en": "Both Assertion and Reason are true and Reason is the correct explanation of Assertion.", "ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்."},
            {"id": "B", "en": "Both Assertion and Reason are true but Reason is NOT the correct explanation.", "ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல."},
            {"id": "C", "en": "Assertion is true but Reason is false.", "ta": "A சரி, ஆனால் R தவறு."},
            {"id": "D", "en": "Assertion is false but Reason is true.", "ta": "A தவறு, ஆனால் R சரி."}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Both Assertion and Reason are true, and Reason correctly explains Assertion. Chief Justice S.M. Sikri and the majority in Kesavananda Bharati (1973) noted that the Constituent Assembly specifically voted to make the Preamble part of the Constitution, making it an integral constituent part.",
            "ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும். தலைமை நீதிபதி எஸ்.எம். சிக்ரி மற்றும் பெரும்பான்மை நீதிபதிகள், அரசியலமைப்பு நிர்ணய அவை முகவுரையை அரசியலமைப்பின் பகுதியாக வாக்களித்து ஏற்றுக்கொண்டதை சுட்டிக்காட்டி, அது ஒரு ஒருங்கிணைந்த பகுதி எனத் தீர்ப்பளித்தனர்."
        },
        "why_not_others": {
            "A": {"en": "Correct. Both statements are true and Reason directly justifies the reversal of the Berubari opinion.", "ta": "சரி. கூற்று மற்றும் காரணம் இரண்டும் உண்மை; R என்பது பெருபாரி கருத்து மாற்றத்திற்கான நேரடி விளக்கம்."},
            "B": {"en": "Incorrect. Reason is the exact ground upon which the 13-judge bench overruled Berubari.", "ta": "தவறு. 13 நீதிபதிகள் அமர்வு பெருபாரியை நிராகரித்ததற்கான சரியான காரணம் இதுவே."},
            "C": {"en": "Incorrect. Reason is factually and historically true.", "ta": "தவறு. காரணம் வரலாற்று ரீதியாக சரியானது."},
            "D": {"en": "Incorrect. Assertion is true.", "ta": "தவறு. கூற்று சரியானது."}
        },
        "tnpsc_tip": {
            "en": "Remember the hierarchy of Preamble cases: Berubari (1960 - NOT part) -> Kesavananda Bharati (1973 - IS part) -> LIC of India (1995 - Integral part).",
            "ta": "வழக்குகளின் வரிசை: பெருபாரி (1960 - பகுதி அல்ல) -> கேசவானந்த பாரதி (1973 - பகுதி தான்) -> LIC வழக்கு (1995 - ஒருங்கிணைந்த பகுதி)."
        },
        "revision_fact": {
            "en": "In LIC of India v. Consumer Education and Research Centre (1995), the Supreme Court again reiterated that the Preamble is an integral part of the Constitution.",
            "ta": "எல்.ஐ.சி வழக்கில் (1995), முகவுரை அரசியலமைப்பின் ஒருங்கிணைந்த பகுதி என்பதை உச்ச நீதிமன்றம் மீண்டும் உறுதிப்படுத்தியது."
        },
        "source_reference": ["Kesavananda Bharati v. State of Kerala (1973)", "M. Laxmikanth - Indian Polity"],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "Kesavananda Bharati 1973", "Constituent Assembly"],
        "question_en": "Assertion (A): In the Kesavananda Bharati Case (1973), the Supreme Court rejected the earlier Berubari opinion and held that the Preamble IS an integral part of the Constitution.\nReason (R): The Supreme Court recognized that the Preamble was debated, voted upon, and enacted by the Constituent Assembly through the exact same constituent procedure as any other part of the Constitution.",
        "question_ta": "கூற்று (A): கேசவானந்த பாரதி வழக்கில் (1973), உச்ச நீதிமன்றம் முந்தைய பெருபாரி ஆலோசனைக் கருத்தை நிராகரித்து, முகவுரை அரசியலமைப்பின் ஒரு ஒருங்கிணைந்த பகுதி என்று தீர்ப்பளித்தது.\nகாரணம் (R): அரசியலமைப்பின் மற்ற பகுதிகளைப் போலவே அதே அரசியலமைப்பு நடைமுறையின் மூலம் அரசியலமைப்பு நிர்ணய அவையால் முகவுரையும் விவாதிக்கப்பட்டு, வாக்களிக்கப்பட்டு, இயற்றப்பட்டது என்பதை உச்ச நீதிமன்றம் அங்கீகரித்தது.",
        "options_en": [
            "Both Assertion and Reason are true and Reason is the correct explanation of Assertion.",
            "Both Assertion and Reason are true but Reason is NOT the correct explanation.",
            "Assertion is true but Reason is false.",
            "Assertion is false but Reason is true."
        ],
        "options_ta": [
            "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்.",
            "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல.",
            "A சரி, ஆனால் R தவறு.",
            "A தவறு, ஆனால் R சரி."
        ],
        "answer": "a",
        "explanation_en": "Both Assertion and Reason are true, and Reason correctly explains Assertion. Chief Justice S.M. Sikri and the majority in Kesavananda Bharati (1973) noted that the Constituent Assembly specifically voted to make the Preamble part of the Constitution, making it an integral constituent part.",
        "explanation_ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும். தலைமை நீதிபதி எஸ்.எம். சிக்ரி மற்றும் பெரும்பான்மை நீதிபதிகள், அரசியலமைப்பு நிர்ணய அவை முகவுரையை அரசியலமைப்பின் பகுதியாக வாக்களித்து ஏற்றுக்கொண்டதை சுட்டிக்காட்டி, அது ஒரு ஒருங்கிணைந்த பகுதி எனத் தீர்ப்பளித்தனர்."
    },

    # =========================================================================
    # Q12: PRE_AR_012 (Answer: C) - Article 368 & 42nd Amendment Trap
    # =========================================================================
    {
        "id": "PRE_AR_012",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Assertion & Reason",
        "question": {
            "en": "Assertion (A): The Preamble of the Constitution has been amended only once so far, by the 42nd Constitutional Amendment Act of 1976.\nReason (R): Article 368 had to be specially amended in 1976 to grant Parliament the constitutional power to amend the Preamble for the first time.",
            "ta": "கூற்று (A): அரசியலமைப்பின் முகவுரை இதுவரை ஒரே ஒரு முறை மட்டுமே 1976 ஆம் ஆண்டின் 42வது அரசியலமைப்புத் திருத்தச் சட்டத்தின் மூலம் திருத்தப்பட்டுள்ளது.\nகாரணம் (R): முகவுரையை முதன்முறையாகத் திருத்துவதற்கான அரசியலமைப்பு அதிகாரத்தை நாடாளுமன்றத்திற்கு வழங்குவதற்காக, 1976-ல் உறுப்பு 368 சிறப்பாகத் திருத்தப்பட வேண்டியிருந்தது."
        },
        "options": [
            {"id": "A", "en": "Both Assertion and Reason are true and Reason is the correct explanation of Assertion.", "ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்."},
            {"id": "B", "en": "Both Assertion and Reason are true but Reason is NOT the correct explanation.", "ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல."},
            {"id": "C", "en": "Assertion is true but Reason is false.", "ta": "A சரி, ஆனால் R தவறு."},
            {"id": "D", "en": "Assertion is false but Reason is true.", "ta": "A தவறு, ஆனால் R சரி."}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "Assertion is TRUE because the Preamble has been amended only once (42nd CAA, 1976 adding Socialist, Secular, Integrity). Reason is FALSE because Article 368 was NOT amended to grant power over the Preamble; Kesavananda Bharati (1973) had already settled that Parliament's existing constituent amending power under Article 368 extends to the Preamble, subject to the basic structure limitation.",
            "ta": "கூற்று A சரி; ஏனெனில் முகவுரை இதுவரை 1976-ல் ஒரே ஒரு முறை மட்டுமே திருத்தப்பட்டுள்ளது. காரணம் R தவறு; ஏனெனில் முகவுரையைத் திருத்த உறுப்பு 368-ல் தனியாக அதிகாரம் சேர்க்கப்படவில்லை; உறுப்பு 368-ன் கீழான நாடாளுமன்றத்தின் பொதுவான திருத்தும் அதிகாரமே அடிப்படை கட்டமைப்பிற்கு உட்பட்டு முகவுரைக்கும் பொருந்தும் என 1973-லேயே உச்ச நீதிமன்றம் தீர்ப்பளித்துவிட்டது."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Reason is false as Article 368 always contained constituent amending power.", "ta": "தவறு. உறுப்பு 368 இயல்பாகவே திருத்தும் அதிகாரத்தைக் கொண்டிருந்ததால் காரணம் தவறானது."},
            "B": {"en": "Incorrect. Reason is false.", "ta": "தவறு. காரணம் தவறானது."},
            "C": {"en": "Correct. Assertion is true; Reason is false.", "ta": "சரி. கூற்று A சரி; காரணம் R தவறு."},
            "D": {"en": "Incorrect. Assertion is true.", "ta": "தவறு. கூற்று சரியானது."}
        },
        "tnpsc_tip": {
            "en": "Parliament can amend the Preamble under Article 368, but CANNOT alter or destroy any 'Basic Feature' contained within it.",
            "ta": "உறுப்பு 368-ன் கீழ் நாடாளுமன்றம் முகவுரையைத் திருத்தலாம், ஆனால் அதில் உள்ள எந்தவொரு 'அடிப்படை அம்சத்தையும்' மாற்றவோ அழிக்கவோ முடியாது."
        },
        "revision_fact": {
            "en": "The 42nd Amendment Act added three new words to the Preamble: 'Socialist', 'Secular', and 'Integrity'.",
            "ta": "42வது திருத்தச் சட்டம் முகவுரையில் மூன்று புதிய சொற்களைச் சேர்த்தது: 'சமதர்ம' (Socialist), 'மதச்சார்பற்ற' (Secular), மற்றும் 'ஒருமைப்பாடு' (Integrity)."
        },
        "source_reference": ["M. Laxmikanth - Indian Polity", "Kesavananda Bharati Case (1973)"],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "Article 368", "42nd Amendment Act 1976"],
        "question_en": "Assertion (A): The Preamble of the Constitution has been amended only once so far, by the 42nd Constitutional Amendment Act of 1976.\nReason (R): Article 368 had to be specially amended in 1976 to grant Parliament the constitutional power to amend the Preamble for the first time.",
        "question_ta": "கூற்று (A): அரசியலமைப்பின் முகவுரை இதுவரை ஒரே ஒரு முறை மட்டுமே 1976 ஆம் ஆண்டின் 42வது அரசியலமைப்புத் திருத்தச் சட்டத்தின் மூலம் திருத்தப்பட்டுள்ளது.\nகாரணம் (R): முகவுரையை முதன்முறையாகத் திருத்துவதற்கான அரசியலமைப்பு அதிகாரத்தை நாடாளுமன்றத்திற்கு வழங்குவதற்காக, 1976-ல் உறுப்பு 368 சிறப்பாகத் திருத்தப்பட வேண்டியிருந்தது.",
        "options_en": [
            "Both Assertion and Reason are true and Reason is the correct explanation of Assertion.",
            "Both Assertion and Reason are true but Reason is NOT the correct explanation.",
            "Assertion is true but Reason is false.",
            "Assertion is false but Reason is true."
        ],
        "options_ta": [
            "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்.",
            "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல.",
            "A சரி, ஆனால் R தவறு.",
            "A தவறு, ஆனால் R சரி."
        ],
        "answer": "c",
        "explanation_en": "Assertion is TRUE because the Preamble has been amended only once (42nd CAA, 1976 adding Socialist, Secular, Integrity). Reason is FALSE because Article 368 was NOT amended to grant power over the Preamble; Kesavananda Bharati (1973) had already settled that Parliament's existing constituent amending power under Article 368 extends to the Preamble, subject to the basic structure limitation.",
        "explanation_ta": "கூற்று A சரி; ஏனெனில் முகவுரை இதுவரை 1976-ல் ஒரே ஒரு முறை மட்டுமே திருத்தப்பட்டுள்ளது. காரணம் R தவறு; ஏனெனில் முகவுரையைத் திருத்த உறுப்பு 368-ல் தனியாக அதிகாரம் சேர்க்கப்படவில்லை; உறுப்பு 368-ன் கீழான நாடாளுமன்றத்தின் பொதுவான திருத்தும் அதிகாரமே அடிப்படை கட்டமைப்பிற்கு உட்பட்டு முகவுரைக்கும் பொருந்தும் என 1973-லேயே உச்ச நீதிமன்றம் தீர்ப்பளித்துவிட்டது."
    },

    # =========================================================================
    # Q13: PRE_AR_013 (Answer: B) - Non-Justiciability of Preamble
    # =========================================================================
    {
        "id": "PRE_AR_013",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Medium",
        "question_type": "Assertion & Reason",
        "question": {
            "en": "Assertion (A): The provisions of the Preamble are non-justiciable and cannot be directly enforced in a court of law to obtain legal relief.\nReason (R): The Preamble is based on the historic 'Objectives Resolution' moved by Jawaharlal Nehru in the Constituent Assembly on December 13, 1946.",
            "ta": "கூற்று (A): முகவுரையின் விதிகள் நீதிமன்றங்களால் நேரடியாக நிலைநிறுத்த முடியாதவை (Non-justiciable) மற்றும் சட்ட நிவாரணம் பெற நீதிமன்றத்தில் நேரடியாக அமல்படுத்தப்பட முடியாது.\nகாரணம் (R): முகவுரை என்பது டிசம்பர் 13, 1946 அன்று ஜவஹர்லால் நேருவால் அரசியலமைப்பு நிர்ணய அவையில் முன்மொழியப்பட்ட வரலாற்றுச் சிறப்புமிக்க 'குறிக்கோள் தீர்மானத்தை' அடிப்படையாகக் கொண்டது."
        },
        "options": [
            {"id": "A", "en": "Both Assertion and Reason are true and Reason is the correct explanation of Assertion.", "ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்."},
            {"id": "B", "en": "Both Assertion and Reason are true but Reason is NOT the correct explanation.", "ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல."},
            {"id": "C", "en": "Assertion is true but Reason is false.", "ta": "A சரி, ஆனால் R தவறு."},
            {"id": "D", "en": "Assertion is false but Reason is true.", "ta": "A தவறு, ஆனால் R சரி."}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "Both Assertion and Reason are true, but Reason is NOT the correct explanation of Assertion. Non-justiciability means its provisions are not enforceable in courts (like DPSP). The drafting origin of the Preamble (Nehru's Objectives Resolution) is an accurate historical fact, but it is not the legal reason why it is non-justiciable.",
            "ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல. நீதிமன்றங்களால் நிலைநிறுத்த முடியாத தன்மை என்பது அரசு வழிகாட்டு நெறிமுறைகளைப் போல அதன் விதிகள் மீது நேரடி வழக்கு தொடர முடியாது என்பதைக் குறிக்கிறது. நேருவின் குறிக்கோள் தீர்மானத்திலிருந்து தோன்றியது என்பது ஒரு வரலாற்று உண்மையே தவிர, நீதிமன்றத்தில் நிலைநிறுத்த முடியாததற்கான சட்ட விளக்கம் அல்ல."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Historical origin does not explain the legal doctrine of non-justiciability.", "ta": "தவறு. வரலாற்று தோற்றம் நீதிமன்றத்தால் நிலைநிறுத்த முடியாத தன்மையை விளக்காது."},
            "B": {"en": "Correct. Both statements are true, but Reason is an independent historical fact.", "ta": "சரி. இரண்டு கூற்றுகளும் உண்மை; காரணம் ஒரு சுயாதீன வரலாற்று உண்மை."},
            "C": {"en": "Incorrect. Reason is true.", "ta": "தவறு. காரணம் சரியானது."},
            "D": {"en": "Incorrect. Assertion is true.", "ta": "தவறு. கூற்று சரியானது."}
        },
        "tnpsc_tip": {
            "en": "Both Preamble and Directive Principles of State Policy (Part IV) are NON-JUSTICIABLE in nature.",
            "ta": "முகவுரை மற்றும் அரசு வழிகாட்டு நெறிமுறைகள் (பகுதி IV) ஆகிய இரண்டும் இயல்பிலேயே நீதிமன்றத்தால் நிலைநிறுத்த முடியாதவை (Non-justiciable)."
        },
        "revision_fact": {
            "en": "The Objectives Resolution was unanimously adopted by the Constituent Assembly on January 22, 1947.",
            "ta": "குறிக்கோள் தீர்மானம் ஜனவரி 22, 1947 அன்று அரசியலமைப்பு நிர்ணய அவையால் ஏகமனதாக ஏற்றுக்கொள்ளப்பட்டது."
        },
        "source_reference": ["M. Laxmikanth - Indian Polity", "DD Basu - Introduction to the Constitution of India"],
        "bloom_level": "Understand",
        "estimated_time_sec": 60,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "Non-Justiciable", "Objectives Resolution"],
        "question_en": "Assertion (A): The provisions of the Preamble are non-justiciable and cannot be directly enforced in a court of law to obtain legal relief.\nReason (R): The Preamble is based on the historic 'Objectives Resolution' moved by Jawaharlal Nehru in the Constituent Assembly on December 13, 1946.",
        "question_ta": "கூற்று (A): முகவுரையின் விதிகள் நீதிமன்றங்களால் நேரடியாக நிலைநிறுத்த முடியாதவை (Non-justiciable) மற்றும் சட்ட நிவாரணம் பெற நீதிமன்றத்தில் நேரடியாக அமல்படுத்தப்பட முடியாது.\nகாரணம் (R): முகவுரை என்பது டிசம்பர் 13, 1946 அன்று ஜவஹர்லால் நேருவால் அரசியலமைப்பு நிர்ணய அவையில் முன்மொழியப்பட்ட வரலாற்றுச் சிறப்புமிக்க 'குறிக்கோள் தீர்மானத்தை' அடிப்படையாகக் கொண்டது.",
        "options_en": [
            "Both Assertion and Reason are true and Reason is the correct explanation of Assertion.",
            "Both Assertion and Reason are true but Reason is NOT the correct explanation.",
            "Assertion is true but Reason is false.",
            "Assertion is false but Reason is true."
        ],
        "options_ta": [
            "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்.",
            "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல.",
            "A சரி, ஆனால் R தவறு.",
            "A தவறு, ஆனால் R சரி."
        ],
        "answer": "b",
        "explanation_en": "Both Assertion and Reason are true, but Reason is NOT the correct explanation of Assertion. Non-justiciability means its provisions are not enforceable in courts (like DPSP). The drafting origin of the Preamble (Nehru's Objectives Resolution) is an accurate historical fact, but it is not the legal reason why it is non-justiciable.",
        "explanation_ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல. நீதிமன்றங்களால் நிலைநிறுத்த முடியாத தன்மை என்பது அரசு வழிகாட்டு நெறிமுறைகளைப் போல அதன் விதிகள் மீது நேரடி வழக்கு தொடர முடியாது என்பதைக் குறிக்கிறது. நேருவின் குறிக்கோள் தீர்மானத்திலிருந்து தோன்றியது என்பது ஒரு வரலாற்று உண்மையே தவிர, நீதிமன்றத்தில் நிலைநிறுத்த முடியாததற்கான சட்ட விளக்கம் அல்ல."
    },

    # =========================================================================
    # Q14: PRE_AR_014 (Answer: D) - Substantive Legislative Power Trap
    # =========================================================================
    {
        "id": "PRE_AR_014",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Assertion & Reason",
        "question": {
            "en": "Assertion (A): The Preamble acts as an independent source of substantive law-making power for the Union Parliament to enact social welfare legislation.\nReason (R): The Preamble is neither a source of power to the legislature nor a prohibition upon the powers of the legislature.",
            "ta": "கூற்று (A): முகவுரை என்பது சமூக நலச் சட்டங்களை இயற்றுவதற்கு மத்திய நாடாளுமன்றத்திற்கான ஒரு சுயாதீனமான சட்டமியற்றும் அதிகாரத்தின் ஆதாரமாகச் செயல்படுகிறது.\nகாரணம் (R): முகவுரை என்பது சட்டமன்றத்திற்கு அதிகாரத்தை வழங்கும் மூலமும் அல்ல, சட்டமன்றத்தின் அதிகாரங்கள் மீதான தடையாகவும் அமையாது."
        },
        "options": [
            {"id": "A", "en": "Both Assertion and Reason are true and Reason is the correct explanation of Assertion.", "ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்."},
            {"id": "B", "en": "Both Assertion and Reason are true but Reason is NOT the correct explanation.", "ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல."},
            {"id": "C", "en": "Assertion is true but Reason is false.", "ta": "A சரி, ஆனால் R தவறு."},
            {"id": "D", "en": "Assertion is false but Reason is true.", "ta": "A தவறு, ஆனால் R சரி."}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "Assertion is FALSE because the Preamble confers no substantive legislative power on Parliament; legislative power must be traced to the Seventh Schedule and specific constitutional articles. Reason is TRUE because it states the well-established legal principle laid down by the Supreme Court.",
            "ta": "கூற்று A தவறு; ஏனெனில் முகவுரை நாடாளுமன்றத்திற்கு எந்தவொரு சட்டமியற்றும் அதிகாரத்தையும் வழங்காது; சட்டமியற்றும் அதிகாரம் ஏழாவது அட்டவணை மற்றும் குறிப்பிட்ட அரசியலமைப்பு உறுப்புகளிலிருந்தே பெறப்பட வேண்டும். காரணம் R சரி; ஏனெனில் உச்ச நீதிமன்றத்தால் வகுக்கப்பட்ட சட்டக் கொள்கையை அது சரியாகக் கூறுகிறது."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Assertion is false.", "ta": "தவறு. கூற்று தவறானது."},
            "B": {"en": "Incorrect. Assertion is false.", "ta": "தவறு. கூற்று தவறானது."},
            "C": {"en": "Incorrect. Assertion is false.", "ta": "தவறு. கூற்று தவறானது."},
            "D": {"en": "Correct. Assertion is false (Preamble is not a source of power); Reason is true.", "ta": "சரி. கூற்று A தவறு (முகவுரை அதிகாரத்தின் மூலம் அல்ல); காரணம் R சரி."}
        },
        "tnpsc_tip": {
            "en": "Two core legal attributes of Preamble: 1. It is neither a source of power nor a prohibition upon power. 2. It is non-justiciable.",
            "ta": "முகவுரையின் இரு முக்கிய சட்டக் கூறுகள்: 1. இது அதிகாரத்தின் மூலமும் அல்ல, அதிகாரத்தின் மீதான தடையுமல்ல. 2. இது நீதிமன்றத்தால் நிலைநிறுத்த முடியாதது."
        },
        "revision_fact": {
            "en": "Parliament's legislative powers are defined in Articles 245-248 and enumerated in the Union, State, and Concurrent lists of the 7th Schedule.",
            "ta": "நாடாளுமன்றத்தின் சட்டமியற்றும் அதிகாரங்கள் உறுப்புகள் 245-248 இல் வரையறுக்கப்பட்டு 7வது அட்டவணையின் ஒன்றிய, மாநில, பொதுப் பட்டியல்களில் பட்டியலிடப்பட்டுள்ளன."
        },
        "source_reference": ["M. Laxmikanth - Indian Polity", "Berubari Union Case (1960)"],
        "bloom_level": "Analyze",
        "estimated_time_sec": 70,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "Legislative Power", "TNPSC Trap"],
        "question_en": "Assertion (A): The Preamble acts as an independent source of substantive law-making power for the Union Parliament to enact social welfare legislation.\nReason (R): The Preamble is neither a source of power to the legislature nor a prohibition upon the powers of the legislature.",
        "question_ta": "கூற்று (A): முகவுரை என்பது சமூக நலச் சட்டங்களை இயற்றுவதற்கு மத்திய நாடாளுமன்றத்திற்கான ஒரு சுயாதீனமான சட்டமியற்றும் அதிகாரத்தின் ஆதாரமாகச் செயல்படுகிறது.\nகாரணம் (R): முகவுரை என்பது சட்டமன்றத்திற்கு அதிகாரத்தை வழங்கும் மூலமும் அல்ல, சட்டமன்றத்தின் அதிகாரங்கள் மீதான தடையாகவும் அமையாது.",
        "options_en": [
            "Both Assertion and Reason are true and Reason is the correct explanation of Assertion.",
            "Both Assertion and Reason are true but Reason is NOT the correct explanation.",
            "Assertion is true but Reason is false.",
            "Assertion is false but Reason is true."
        ],
        "options_ta": [
            "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்.",
            "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல.",
            "A சரி, ஆனால் R தவறு.",
            "A தவறு, ஆனால் R சரி."
        ],
        "answer": "d",
        "explanation_en": "Assertion is FALSE because the Preamble confers no substantive legislative power on Parliament; legislative power must be traced to the Seventh Schedule and specific constitutional articles. Reason is TRUE because it states the well-established legal principle laid down by the Supreme Court.",
        "explanation_ta": "கூற்று A தவறு; ஏனெனில் முகவுரை நாடாளுமன்றத்திற்கு எந்தவொரு சட்டமியற்றும் அதிகாரத்தையும் வழங்காது; சட்டமியற்றும் அதிகாரம் ஏழாவது அட்டவணை மற்றும் குறிப்பிட்ட அரசியலமைப்பு உறுப்புகளிலிருந்தே பெறப்பட வேண்டும். காரணம் R சரி; ஏனெனில் உச்ச நீதிமன்றத்தால் வகுக்கப்பட்ட சட்டக் கொள்கையை அது சரியாகக் கூறுகிறது."
    },

    # =========================================================================
    # Q15: PRE_AR_015 (Answer: A) - Interpretive Role of Preamble
    # =========================================================================
    {
        "id": "PRE_AR_015",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Assertion & Reason",
        "question": {
            "en": "Assertion (A): Where the language of any constitutional provision is ambiguous or capable of two meanings, the interpretation that aligns with the noble vision of the Preamble must be preferred.\nReason (R): The Preamble embodies the fundamental values, philosophy, and basic objective framework which guided the framers of the Constitution.",
            "ta": "கூற்று (A): அரசியலமைப்பு விதியின் வாசகங்கள் தெளிவற்றதாகவோ அல்லது இரு வேறு அர்த்தங்களைக் கொண்டதாகவோ இருக்கும்போது, முகவுரையின் உன்னத நோக்கத்துடன் ஒத்துப்போகும் விளக்கமே முன்னுரிமை பெற வேண்டும்.\nகாரணம் (R): முகவுரை என்பது அரசியலமைப்புச் சிற்பிகளுக்கு வழிகாட்டிய அடிப்படை விழுமியங்கள், தத்துவம் மற்றும் அடிப்படைக் குறிக்கோள் கட்டமைப்பைத் தன்னுள் கொண்டுள்ளது."
        },
        "options": [
            {"id": "A", "en": "Both Assertion and Reason are true and Reason is the correct explanation of Assertion.", "ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்."},
            {"id": "B", "en": "Both Assertion and Reason are true but Reason is NOT the correct explanation.", "ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல."},
            {"id": "C", "en": "Assertion is true but Reason is false.", "ta": "A சரி, ஆனால் R தவறு."},
            {"id": "D", "en": "Assertion is false but Reason is true.", "ta": "A தவறு, ஆனால் R சரி."}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Both Assertion and Reason are true, and Reason is the correct explanation. In Kesavananda Bharati (1973), the Supreme Court affirmed that the Preamble serves as a guiding light and interpretive compass to resolve textual ambiguity in other provisions of the Constitution.",
            "ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும். கேசவானந்த பாரதி வழக்கில் (1973), அரசியலமைப்பின் பிற விதிகளில் உள்ள தெளிவற்ற தன்மையைத் தீர்க்க முகவுரை ஒரு வழிகாட்டும் கலங்கரை விளக்கமாகவும் விளக்கமளிக்கும் திசைகாட்டியாகவும் செயல்படுகிறது என்பதை உச்ச நீதிமன்றம் உறுதிப்படுத்தியது."
        },
        "why_not_others": {
            "A": {"en": "Correct. Both statements are true, and Reason directly explains why Preamble is used as an interpretive tool.", "ta": "சரி. இரண்டும் உண்மை; முகவுரை ஏன் விளக்கக் கருவியாகப் பயன்படுகிறது என்பதை காரணம் விளக்குகிறது."},
            "B": {"en": "Incorrect. Reason is the direct logical foundation for the Assertion.", "ta": "தவறு. கூற்றிற்கான நேரடி தர்க்கரீதியான அடிப்படை காரணம்."},
            "C": {"en": "Incorrect. Reason is true.", "ta": "தவறு. காரணம் சரியானது."},
            "D": {"en": "Incorrect. Assertion is true.", "ta": "தவறு. கூற்று சரியானது."}
        },
        "tnpsc_tip": {
            "en": "If a constitutional article is unambiguous and clear, its literal meaning prevails. Preamble is used as an aid only when ambiguity or double meaning arises.",
            "ta": "அரசியலமைப்பு உறுப்பு தெளிவானதாக இருந்தால், அதன் நேரடிப் பொருளே மேலோங்கும். தெளிவின்மை அல்லது இருபொருள் எழும்போது மட்டுமே முகவுரை விளக்க உதவியாகப் பயன்படுத்தப்படும்."
        },
        "revision_fact": {
            "en": "Sir Alladi Krishnaswami Iyer remarked: 'The Preamble to our Constitution expresses what we had thought or dreamt so long.'",
            "ta": "சர் அல்லாடி கிருஷ்ணசுவாமி ஐயர்: 'நமது அரசியலமைப்பின் முகவுரை நாம் இவ்வளவு காலம் என்ன நினைத்தோம் அல்லது கனவு கண்டோம் என்பதை வெளிப்படுத்துகிறது' என்று கூறினார்."
        },
        "source_reference": ["Kesavananda Bharati Case (1973)", "M. Laxmikanth - Indian Polity"],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "Interpretive Guide", "Judicial Interpretation"],
        "question_en": "Assertion (A): Where the language of any constitutional provision is ambiguous or capable of two meanings, the interpretation that aligns with the noble vision of the Preamble must be preferred.\nReason (R): The Preamble embodies the fundamental values, philosophy, and basic objective framework which guided the framers of the Constitution.",
        "question_ta": "கூற்று (A): அரசியலமைப்பு விதியின் வாசகங்கள் தெளிவற்றதாகவோ அல்லது இரு வேறு அர்த்தங்களைக் கொண்டதாகவோ இருக்கும்போது, முகவுரையின் உன்னத நோக்கத்துடன் ஒத்துப்போகும் விளக்கமே முன்னுரிமை பெற வேண்டும்.\nகாரணம் (R): முகவுரை என்பது அரசியலமைப்புச் சிற்பிகளுக்கு வழிகாட்டிய அடிப்படை விழுமியங்கள், தத்துவம் மற்றும் அடிப்படைக் குறிக்கோள் கட்டமைப்பைத் தன்னுள் கொண்டுள்ளது.",
        "options_en": [
            "Both Assertion and Reason are true and Reason is the correct explanation of Assertion.",
            "Both Assertion and Reason are true but Reason is NOT the correct explanation.",
            "Assertion is true but Reason is false.",
            "Assertion is false but Reason is true."
        ],
        "options_ta": [
            "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்.",
            "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல.",
            "A சரி, ஆனால் R தவறு.",
            "A தவறு, ஆனால் R சரி."
        ],
        "answer": "a",
        "explanation_en": "Both Assertion and Reason are true, and Reason is the correct explanation. In Kesavananda Bharati (1973), the Supreme Court affirmed that the Preamble serves as a guiding light and interpretive compass to resolve textual ambiguity in other provisions of the Constitution.",
        "explanation_ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும். கேசவானந்த பாரதி வழக்கில் (1973), அரசியலமைப்பின் பிற விதிகளில் உள்ள தெளிவற்ற தன்மையைத் தீர்க்க முகவுரை ஒரு வழிகாட்டும் கலங்கரை விளக்கமாகவும் விளக்கமளிக்கும் திசைகாட்டியாகவும் செயல்படுகிறது என்பதை உச்ச நீதிமன்றம் உறுதிப்படுத்தியது."
    },

    # =========================================================================
    # Q16: PRE_AR_016 (Answer: B) - Preamble & Fundamental Rights
    # =========================================================================
    {
        "id": "PRE_AR_016",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Medium",
        "question_type": "Assertion & Reason",
        "question": {
            "en": "Assertion (A): The grand ideals of 'Liberty, Equality, and Fraternity' proclaimed in the Preamble find concrete and enforceable legal expression in Part III (Fundamental Rights).\nReason (R): Article 32 guarantees the Right to Constitutional Remedies, conferring power on the Supreme Court to issue prerogative writs for the enforcement of Fundamental Rights.",
            "ta": "கூற்று (A): முகவுரையில் பிரகடனப்படுத்தப்பட்ட 'சுதந்திரம், சமத்துவம் மற்றும் சகோதரத்துவம்' என்ற உன்னத இலட்சியங்கள் பகுதி III-ல் (அடிப்படை உரிமைகள்) உறுதியான மற்றும் நிலைநிறுத்தக்கூடிய சட்ட வடிவத்தைப் பெறுகின்றன.\nகாரணம் (R): உறுப்பு 32 அரசியலமைப்பு தீர்வுகளுக்கான உரிமையை உத்தரவாதம் செய்கிறது, மேலும் அடிப்படை உரிமைகளை அமல்படுத்துவதற்காக நீதிப்பேராணைகளை வெளியிடும் அதிகாரத்தை உச்ச நீதிமன்றத்திற்கு வழங்குகிறது."
        },
        "options": [
            {"id": "A", "en": "Both Assertion and Reason are true and Reason is the correct explanation of Assertion.", "ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்."},
            {"id": "B", "en": "Both Assertion and Reason are true but Reason is NOT the correct explanation.", "ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல."},
            {"id": "C", "en": "Assertion is true but Reason is false.", "ta": "A சரி, ஆனால் R தவறு."},
            {"id": "D", "en": "Assertion is false but Reason is true.", "ta": "A தவறு, ஆனால் R சரி."}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "Both Assertion and Reason are true, but Reason is NOT the correct explanation of Assertion. Part III translates Preamble's goals into substantive rights (Arts 14-18 Equality, Arts 19-22 Liberty, Arts 25-28 Religious Freedom). Article 32 provides the procedural enforcement mechanism, but is not the substantive reason why Part III embodies Preamble's ideals.",
            "ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல. பகுதி III முகவுரையின் குறிக்கோள்களை நடைமுறை உரிமைகளாக மாற்றுகிறது (உறுப்புகள் 14-18 சமத்துவம், 19-22 சுதந்திரம்). உறுப்பு 32 அவற்றை அமல்படுத்துவதற்கான நடைமுறை பாதுகாப்பு வழியை வழங்குகிறதே தவிர, பகுதி III முகவுரையின் இலட்சியங்களை உள்ளடக்கியிருப்பதற்கான காரணமல்ல."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Article 32 provides the remedy, but does not explain the substantive incorporation of Preamble ideals.", "ta": "தவறு. உறுப்பு 32 தீர்வை வழங்குகிறது, ஆனால் முகவுரை இலட்சியங்கள் அடிப்படை உரிமைகளில் எவ்வாறு அடங்கியுள்ளன என்பதை விளக்கவில்லை."},
            "B": {"en": "Correct. Both statements are true, but Reason describes a procedural enforcement remedy.", "ta": "சரி. இரண்டு கூற்றுகளும் உண்மை; ஆனால் காரணம் ஒரு நடைமுறை அமலாக்கத் தீர்வாகும்."},
            "C": {"en": "Incorrect. Reason is true under Article 32.", "ta": "தவறு. உறுப்பு 32-ன் கீழ் காரணம் சரியானது."},
            "D": {"en": "Incorrect. Assertion is true.", "ta": "தவறு. கூற்று சரியானது."}
        },
        "tnpsc_tip": {
            "en": "Dr. B.R. Ambedkar described Article 32 as the 'Heart and Soul of the Constitution', without which the rights in Part III would be meaningless.",
            "ta": "டாக்டர் பி.ஆர். அம்பேத்கர் உறுப்பு 32-ஐ 'அரசியலமைப்பின் இதயம் மற்றும் ஆன்மா' என்று வர்ணித்தார்."
        },
        "revision_fact": {
            "en": "Both the Supreme Court (Art 32) and High Courts (Art 226) can issue writs: Habeas Corpus, Mandamus, Prohibition, Certiorari, and Quo-Warranto.",
            "ta": "உச்ச நீதிமன்றம் (உறுப்பு 32) மற்றும் உயர் நீதிமன்றங்கள் (உறுப்பு 226) ஆகிய இரண்டும் 5 வகையான நீதிப்பேராணைகளை வெளியிடலாம்."
        },
        "source_reference": ["M. Laxmikanth - Indian Polity", "Constitution of India Part III"],
        "bloom_level": "Analyze",
        "estimated_time_sec": 70,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "Fundamental Rights", "Article 32"],
        "question_en": "Assertion (A): The grand ideals of 'Liberty, Equality, and Fraternity' proclaimed in the Preamble find concrete and enforceable legal expression in Part III (Fundamental Rights).\nReason (R): Article 32 guarantees the Right to Constitutional Remedies, conferring power on the Supreme Court to issue prerogative writs for the enforcement of Fundamental Rights.",
        "question_ta": "கூற்று (A): முகவுரையில் பிரகடனப்படுத்தப்பட்ட 'சுதந்திரம், சமத்துவம் மற்றும் சகோதரத்துவம்' என்ற உன்னத இலட்சியங்கள் பகுதி III-ல் (அடிப்படை உரிமைகள்) உறுதியான மற்றும் நிலைநிறுத்தக்கூடிய சட்ட வடிவத்தைப் பெறுகின்றன.\nகாரணம் (R): உறுப்பு 32 அரசியலமைப்பு தீர்வுகளுக்கான உரிமையை உத்தரவாதம் செய்கிறது, மேலும் அடிப்படை உரிமைகளை அமல்படுத்துவதற்காக நீதிப்பேராணைகளை வெளியிடும் அதிகாரத்தை உச்ச நீதிமன்றத்திற்கு வழங்குகிறது.",
        "options_en": [
            "Both Assertion and Reason are true and Reason is the correct explanation of Assertion.",
            "Both Assertion and Reason are true but Reason is NOT the correct explanation.",
            "Assertion is true but Reason is false.",
            "Assertion is false but Reason is true."
        ],
        "options_ta": [
            "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்.",
            "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல.",
            "A சரி, ஆனால் R தவறு.",
            "A தவறு, ஆனால் R சரி."
        ],
        "answer": "b",
        "explanation_en": "Both Assertion and Reason are true, but Reason is NOT the correct explanation of Assertion. Part III translates Preamble's goals into substantive rights (Arts 14-18 Equality, Arts 19-22 Liberty, Arts 25-28 Religious Freedom). Article 32 provides the procedural enforcement mechanism, but is not the substantive reason why Part III embodies Preamble's ideals.",
        "explanation_ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல. பகுதி III முகவுரையின் குறிக்கோள்களை நடைமுறை உரிமைகளாக மாற்றுகிறது (உறுப்புகள் 14-18 சமத்துவம், 19-22 சுதந்திரம்). உறுப்பு 32 அவற்றை அமல்படுத்துவதற்கான நடைமுறை பாதுகாப்பு வழியை வழங்குகிறதே தவிர, பகுதி III முகவுரையின் இலட்சியங்களை உள்ளடக்கியிருப்பதற்கான காரணமல்ல."
    },

    # =========================================================================
    # Q17: PRE_AR_017 (Answer: A) - Preamble & Directive Principles
    # =========================================================================
    {
        "id": "PRE_AR_017",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Assertion & Reason",
        "question": {
            "en": "Assertion (A): Part IV (Directive Principles of State Policy) acts as the operational instrument to realize the Preamble's vision of a 'Socio-Economic Welfare State'.\nReason (R): Articles 38 and 39 command the State to secure a social order for the promotion of welfare of the people and to minimize inequalities in income, status, facilities, and opportunities.",
            "ta": "கூற்று (A): பகுதி IV (அரசு வழிகாட்டு நெறிமுறைகள்) முகவுரையின் 'சமூக-பொருளாதார நல அரசு' என்ற தொலைநோக்குப் பார்வையை நனவாக்குவதற்கான செயல்பாட்டு கருவியாகச் செயல்படுகிறது.\nகாரணம் (R): உறுப்புகள் 38 மற்றும் 39 மக்களின் நலனை மேம்படுத்துவதற்கான ஒரு சமூக அமைப்பைப் பாதுகாக்கவும், வருமானம், அந்தஸ்து, வசதிகள் மற்றும் வாய்ப்புகளில் உள்ள சமத்துவமின்மையைக் குறைக்கவும் அரசுக்கு ஆணையிடுகின்றன."
        },
        "options": [
            {"id": "A", "en": "Both Assertion and Reason are true and Reason is the correct explanation of Assertion.", "ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்."},
            {"id": "B", "en": "Both Assertion and Reason are true but Reason is NOT the correct explanation.", "ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல."},
            {"id": "C", "en": "Assertion is true but Reason is false.", "ta": "A சரி, ஆனால் R தவறு."},
            {"id": "D", "en": "Assertion is false but Reason is true.", "ta": "A தவறு, ஆனால் R சரி."}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Both Assertion and Reason are true, and Reason correctly explains Assertion. Granville Austin described the Preamble, Fundamental Rights, and DPSP as the 'Conscience of the Constitution', with DPSP specifically designed to achieve the socio-economic revolution pledged in the Preamble.",
            "ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும். கிரான்வில் ஆஸ்டின் முகவுரை, அடிப்படை உரிமைகள் மற்றும் வழிகாட்டு நெறிமுறைகளை 'அரசியலமைப்பின் மனசாட்சி' என்று வர்ணித்தார்; இதில் வழிகாட்டு நெறிமுறைகள் முகவுரையில் உறுதியளிக்கப்பட்ட சமூக-பொருளாதாரப் புரட்சியை அடைய வடிவமைக்கப்பட்டுள்ளன."
        },
        "why_not_others": {
            "A": {"en": "Correct. Both statements are true and Reason explains how DPSP realizes the welfare goals of Preamble.", "ta": "சரி. இரண்டும் உண்மை; முகவுரையின் நல அரசு இலக்குகளை DPSP எவ்வாறு செயல்படுத்துகிறது என்பதை காரணம் விளக்குகிறது."},
            "B": {"en": "Incorrect. Reason directly substantiates the operational connection asserted.", "ta": "தவறு. காரணம் கூற்றிற்கான நேரடி விளக்கத்தை அளிக்கிறது."},
            "C": {"en": "Incorrect. Reason is true under Articles 38 and 39.", "ta": "தவறு. உறுப்புகள் 38 மற்றும் 39-ன் கீழ் காரணம் சரியானது."},
            "D": {"en": "Incorrect. Assertion is true.", "ta": "தவறு. கூற்று சரியானது."}
        },
        "tnpsc_tip": {
            "en": "Fundamental Rights establish Political Democracy, while Directive Principles establish Social and Economic Democracy as promised in the Preamble.",
            "ta": "அடிப்படை உரிமைகள் அரசியல் ஜனநாயகத்தை நிறுவுகின்றன, அதே சமயம் அரசு வழிகாட்டு நெறிமுறைகள் முகவுரையில் வாக்குறுதி அளித்தபடி சமூக மற்றும் பொருளாதார ஜனநாயகத்தை நிறுவுகின்றன."
        },
        "revision_fact": {
            "en": "In Minerva Mills v. Union of India (1980), the Supreme Court observed that the Constitution is founded on the bedrock of the balance between Part III and Part IV.",
            "ta": "மினர்வா மில்ஸ் வழக்கில் (1980), பகுதி III மற்றும் பகுதி IV இடையேயான சமநிலையின் அடித்தளத்திலேயே அரசியலமைப்பு கட்டமைக்கப்பட்டுள்ளது என்று உச்ச நீதிமன்றம் கூறியது."
        },
        "source_reference": ["M. Laxmikanth - Indian Polity", "Granville Austin - The Indian Constitution"],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "DPSP", "Welfare State", "Article 38"],
        "question_en": "Assertion (A): Part IV (Directive Principles of State Policy) acts as the operational instrument to realize the Preamble's vision of a 'Socio-Economic Welfare State'.\nReason (R): Articles 38 and 39 command the State to secure a social order for the promotion of welfare of the people and to minimize inequalities in income, status, facilities, and opportunities.",
        "question_ta": "கூற்று (A): பகுதி IV (அரசு வழிகாட்டு நெறிமுறைகள்) முகவுரையின் 'சமூக-பொருளாதார நல அரசு' என்ற தொலைநோக்குப் பார்வையை நனவாக்குவதற்கான செயல்பாட்டு கருவியாகச் செயல்படுகிறது.\nகாரணம் (R): உறுப்புகள் 38 மற்றும் 39 மக்களின் நலனை மேம்படுத்துவதற்கான ஒரு சமூக அமைப்பைப் பாதுகாக்கவும், வருமானம், அந்தஸ்து, வசதிகள் மற்றும் வாய்ப்புகளில் உள்ள சமத்துவமின்மையைக் குறைக்கவும் அரசுக்கு ஆணையிடுகின்றன.",
        "options_en": [
            "Both Assertion and Reason are true and Reason is the correct explanation of Assertion.",
            "Both Assertion and Reason are true but Reason is NOT the correct explanation.",
            "Assertion is true but Reason is false.",
            "Assertion is false but Reason is true."
        ],
        "options_ta": [
            "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்.",
            "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல.",
            "A சரி, ஆனால் R தவறு.",
            "A தவறு, ஆனால் R சரி."
        ],
        "answer": "a",
        "explanation_en": "Both Assertion and Reason are true, and Reason correctly explains Assertion. Granville Austin described the Preamble, Fundamental Rights, and DPSP as the 'Conscience of the Constitution', with DPSP specifically designed to achieve the socio-economic revolution pledged in the Preamble.",
        "explanation_ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும். கிரான்வில் ஆஸ்டின் முகவுரை, அடிப்படை உரிமைகள் மற்றும் வழிகாட்டு நெறிமுறைகளை 'அரசியலமைப்பின் மனசாட்சி' என்று வர்ணித்தார்; இதில் வழிகாட்டு நெறிமுறைகள் முகவுரையில் உறுதியளிக்கப்பட்ட சமூக-பொருளாதாரப் புரட்சியை அடைய வடிவமைக்கப்பட்டுள்ளன."
    },

    # =========================================================================
    # Q18: PRE_AR_018 (Answer: C) - Secularism Explicit vs Implicit Trap
    # =========================================================================
    {
        "id": "PRE_AR_018",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Assertion & Reason",
        "question": {
            "en": "Assertion (A): The 42nd Amendment Act of 1976 made explicit what was already implicit in the Indian Constitution by inserting the word 'Secular' into the Preamble.\nReason (R): Prior to the 42nd Amendment in 1976, the Constitution contained no fundamental right or constitutional provision protecting the freedom of religion.",
            "ta": "கூற்று (A): 1976 ஆம் ஆண்டின் 42வது திருத்தச் சட்டம் முகவுரையில் 'மதச்சார்பற்ற' என்ற சொல்லைச் சேர்த்ததன் மூலம், இந்திய அரசியலமைப்பில் ஏற்கனவே மறைமுகமாக இருந்த ஒரு கருத்தை வெளிப்படையானதாக மாற்றியது.\nகாரணம் (R): 1976-ன் 42வது திருத்தத்திற்கு முன்பு, மதச் சுதந்திரத்தைப் பாதுகாக்கும் எந்தவொரு அடிப்படை உரிமையோ அல்லது அரசியலமைப்பு விதியோ அரசியலமைப்பில் இடம்பெற்றிருக்கவில்லை."
        },
        "options": [
            {"id": "A", "en": "Both Assertion and Reason are true and Reason is the correct explanation of Assertion.", "ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்."},
            {"id": "B", "en": "Both Assertion and Reason are true but Reason is NOT the correct explanation.", "ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல."},
            {"id": "C", "en": "Assertion is true but Reason is false.", "ta": "A சரி, ஆனால் R தவறு."},
            {"id": "D", "en": "Assertion is false but Reason is true.", "ta": "A தவறு, ஆனால் R சரி."}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "Assertion is TRUE because the Supreme Court in St. Xavier's College (1974) held that India was already a secular state before 1976. Reason is FALSE because Articles 25 to 28 (Freedom of Religion) were already part of the original Constitution since January 26, 1950.",
            "ta": "கூற்று A சரி; ஏனெனில் புனித சேவியர் கல்லூரி வழக்கில் (1974) 1976-க்கு முன்பே இந்தியா ஒரு மதச்சார்பற்ற நாடு என்று உச்ச நீதிமன்றம் உறுதிப்படுத்தியது. காரணம் R தவறு; ஏனெனில் மத சுதந்திரத்திற்கான அடிப்படை உரிமைகளான உறுப்புகள் 25 முதல் 28 வரை ஜனவரி 26, 1950 முதல் அசல் அரசியலமைப்பிலேயே இடம்பெற்றிருந்தன."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Reason is false as Articles 25-28 existed since 1950.", "ta": "தவறு. உறுப்புகள் 25-28 1950 முதலே இருந்ததால் காரணம் தவறானது."},
            "B": {"en": "Incorrect. Reason is false.", "ta": "தவறு. காரணம் தவறானது."},
            "C": {"en": "Correct. Assertion is true; Reason is false.", "ta": "சரி. கூற்று A சரி; காரணம் R தவறு."},
            "D": {"en": "Incorrect. Assertion is true.", "ta": "தவறு. கூற்று சரியானது."}
        },
        "tnpsc_tip": {
            "en": "Even though the word 'Secular' was inserted in 1976, the Constitution makers always intended India to be a secular state through Articles 25-28.",
            "ta": "1976-ல் 'மதச்சார்பற்ற' என்ற சொல் சேர்க்கப்பட்டிருந்தாலும், உறுப்புகள் 25-28 மூலம் அரசியலமைப்புச் சிற்பிகள் ஆரம்பத்திலிருந்தே இந்தியாவை ஒரு மதச்சார்பற்ற நாடாகவே உருவாக்கினர்."
        },
        "revision_fact": {
            "en": "Articles 25 to 28 guarantee freedom of conscience, free profession, practice and propagation of religion, and management of religious affairs.",
            "ta": "உறுப்புகள் 25 முதல் 28 வரை மனசாட்சி சுதந்திரம், மதத்தைப் பின்பற்றும், பரப்பும் உரிமை மற்றும் மத விவகாரங்களை நிர்வகிக்கும் உரிமையை உத்தரவாதம் செய்கின்றன."
        },
        "source_reference": ["M. Laxmikanth - Indian Polity", "St. Xavier's College Case (1974)"],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "Secularism", "42nd Amendment Act 1976", "Articles 25-28"],
        "question_en": "Assertion (A): The 42nd Amendment Act of 1976 made explicit what was already implicit in the Indian Constitution by inserting the word 'Secular' into the Preamble.\nReason (R): Prior to the 42nd Amendment in 1976, the Constitution contained no fundamental right or constitutional provision protecting the freedom of religion.",
        "question_ta": "கூற்று (A): 1976 ஆம் ஆண்டின் 42வது திருத்தச் சட்டம் முகவுரையில் 'மதச்சார்பற்ற' என்ற சொல்லைச் சேர்த்ததன் மூலம், இந்திய அரசியலமைப்பில் ஏற்கனவே மறைமுகமாக இருந்த ஒரு கருத்தை வெளிப்படையானதாக மாற்றியது.\nகாரணம் (R): 1976-ன் 42வது திருத்தத்திற்கு முன்பு, மதச் சுதந்திரத்தைப் பாதுகாக்கும் எந்தவொரு அடிப்படை உரிமையோ அல்லது அரசியலமைப்பு விதியோ அரசியலமைப்பில் இடம்பெற்றிருக்கவில்லை.",
        "options_en": [
            "Both Assertion and Reason are true and Reason is the correct explanation of Assertion.",
            "Both Assertion and Reason are true but Reason is NOT the correct explanation.",
            "Assertion is true but Reason is false.",
            "Assertion is false but Reason is true."
        ],
        "options_ta": [
            "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்.",
            "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல.",
            "A சரி, ஆனால் R தவறு.",
            "A தவறு, ஆனால் R சரி."
        ],
        "answer": "c",
        "explanation_en": "Assertion is TRUE because the Supreme Court in St. Xavier's College (1974) held that India was already a secular state before 1976. Reason is FALSE because Articles 25 to 28 (Freedom of Religion) were already part of the original Constitution since January 26, 1950.",
        "explanation_ta": "கூற்று A சரி; ஏனெனில் புனித சேவியர் கல்லூரி வழக்கில் (1974) 1976-க்கு முன்பே இந்தியா ஒரு மதச்சார்பற்ற நாடு என்று உச்ச நீதிமன்றம் உறுதிப்படுத்தியது. காரணம் R தவறு; ஏனெனில் மத சுதந்திரத்திற்கான அடிப்படை உரிமைகளான உறுப்புகள் 25 முதல் 28 வரை ஜனவரி 26, 1950 முதல் அசல் அரசியலமைப்பிலேயே இடம்பெற்றிருந்தன."
    },

    # =========================================================================
    # Q19: PRE_AR_019 (Answer: C) - Ordinary Statutory Law vs Preamble
    # =========================================================================
    {
        "id": "PRE_AR_019",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Assertion & Reason",
        "question": {
            "en": "Assertion (A): An ordinary Act of Parliament cannot be declared unconstitutional and void solely on the vague ground that it violates the Preamble in the abstract.\nReason (R): The Preamble is an extraneous non-constitutional declaration that holds no legal or constitutional status in Indian jurisprudence.",
            "ta": "கூற்று (A): நாடாளுமன்றத்தின் சாதாரணச் சட்டம் ஒன்று, முகவுரையை அருவமாக மீறுகிறது என்ற தெளிவற்ற காரணத்திற்காக மட்டுமே அரசியலமைப்பிற்கு முரணானது மற்றும் செல்லாதது என அறிவிக்கப்பட முடியாது.\nகாரணம் (R): முகவுரை என்பது ஒரு வெளிப்புற அரசியலமைப்பற்ற பிரகடனம் ஆகும், மேலும் இது இந்திய சட்டவியலில் எந்தவொரு சட்ட அல்லது அரசியலமைப்பு அந்தஸ்தையும் கொண்டிருக்கவில்லை."
        },
        "options": [
            {"id": "A", "en": "Both Assertion and Reason are true and Reason is the correct explanation of Assertion.", "ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்."},
            {"id": "B", "en": "Both Assertion and Reason are true but Reason is NOT the correct explanation.", "ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல."},
            {"id": "C", "en": "Assertion is true but Reason is false.", "ta": "A சரி, ஆனால் R தவறு."},
            {"id": "D", "en": "Assertion is false but Reason is true.", "ta": "A தவறு, ஆனால் R சரி."}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "Assertion is TRUE because a statute can be struck down only if it violates a specific substantive provision of the Constitution or the Basic Structure. Reason is FALSE because the Preamble IS an integral part of the Constitution (Kesavananda Bharati, LIC case) and possesses profound interpretive and constitutional significance.",
            "ta": "கூற்று A சரி; ஏனெனில் ஒரு சட்டம் அரசியலமைப்பின் குறிப்பிட்ட பிரிவையோ அல்லது அடிப்படை கட்டமைப்பையோ மீறினால் மட்டுமே செல்லாது என அறிவிக்கப்படும். காரணம் R தவறு; ஏனெனில் முகவுரை அரசியலமைப்பின் ஒருங்கிணைந்த பகுதியாகும் (கேசவானந்த பாரதி, LIC வழக்குகள்) மற்றும் ஆழ்ந்த அரசியலமைப்பு முக்கியத்துவம் கொண்டது."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Reason is false as Preamble is an integral part of the Constitution.", "ta": "தவறு. முகவுரை அரசியலமைப்பின் ஒரு பகுதி என்பதால் காரணம் தவறானது."},
            "B": {"en": "Incorrect. Reason is false.", "ta": "தவறு. காரணம் தவறானது."},
            "C": {"en": "Correct. Assertion is true; Reason is false.", "ta": "சரி. கூற்று A சரி; காரணம் R தவறு."},
            "D": {"en": "Incorrect. Assertion is true.", "ta": "தவறு. கூற்று சரியானது."}
        },
        "tnpsc_tip": {
            "en": "A law is tested against substantive articles (e.g. Art 13, 14, 19, 21), reading those articles in the light of the Preamble, rather than challenging under the Preamble alone.",
            "ta": "ஒரு சட்டம் முகவுரையின் வெளிச்சத்தில் உறுப்புகள் 14, 19, 21 போன்ற உறுப்புகளுடன் இணைத்தே ஆராயப்படுகிறது, முகவுரையின் கீழ் தனியாக அல்ல."
        },
        "revision_fact": {
            "en": "Article 13 provides that any law inconsistent with or in derogation of Fundamental Rights shall be void to the extent of inconsistency.",
            "ta": "உறுப்பு 13 அடிப்படை உரிமைகளுக்கு முரணான எந்தவொரு சட்டமும் அந்த முரண்பாட்டின் அளவிற்கு செல்லாது என்று கூறுகிறது."
        },
        "source_reference": ["M. Laxmikanth - Indian Polity", "DD Basu - Comparative Constitutional Law"],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "Judicial Review", "Ultra Vires", "Article 13"],
        "question_en": "Assertion (A): An ordinary Act of Parliament cannot be declared unconstitutional and void solely on the vague ground that it violates the Preamble in the abstract.\nReason (R): The Preamble is an extraneous non-constitutional declaration that holds no legal or constitutional status in Indian jurisprudence.",
        "question_ta": "கூற்று (A): நாடாளுமன்றத்தின் சாதாரணச் சட்டம் ஒன்று, முகவுரையை அருவமாக மீறுகிறது என்ற தெளிவற்ற காரணத்திற்காக மட்டுமே அரசியலமைப்பிற்கு முரணானது மற்றும் செல்லாதது என அறிவிக்கப்பட முடியாது.\nகாரணம் (R): முகவுரை என்பது ஒரு வெளிப்புற அரசியலமைப்பற்ற பிரகடனம் ஆகும், மேலும் இது இந்திய சட்டவியலில் எந்தவொரு சட்ட அல்லது அரசியலமைப்பு அந்தஸ்தையும் கொண்டிருக்கவில்லை.",
        "options_en": [
            "Both Assertion and Reason are true and Reason is the correct explanation of Assertion.",
            "Both Assertion and Reason are true but Reason is NOT the correct explanation.",
            "Assertion is true but Reason is false.",
            "Assertion is false but Reason is true."
        ],
        "options_ta": [
            "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்.",
            "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல.",
            "A சரி, ஆனால் R தவறு.",
            "A தவறு, ஆனால் R சரி."
        ],
        "answer": "c",
        "explanation_en": "Assertion is TRUE because a statute can be struck down only if it violates a specific substantive provision of the Constitution or the Basic Structure. Reason is FALSE because the Preamble IS an integral part of the Constitution (Kesavananda Bharati, LIC case) and possesses profound interpretive and constitutional significance.",
        "explanation_ta": "கூற்று A சரி; ஏனெனில் ஒரு சட்டம் அரசியலமைப்பின் குறிப்பிட்ட பிரிவையோ அல்லது அடிப்படை கட்டமைப்பையோ மீறினால் மட்டுமே செல்லாது என அறிவிக்கப்படும். காரணம் R தவறு; ஏனெனில் முகவுரை அரசியலமைப்பின் ஒரு பகுதியாகும் (கேசவானந்த பாரதி, LIC வழக்குகள்) மற்றும் ஆழ்ந்த அரசியலமைப்பு முக்கியத்துவம் கொண்டது."
    },

    # =========================================================================
    # Q20: PRE_AR_020 (Answer: C) - Territorial Cession & Article 1 Trap
    # =========================================================================
    {
        "id": "PRE_AR_020",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Assertion & Reason",
        "question": {
            "en": "Assertion (A): Cession of Indian territory to a foreign country cannot be effected by a mere executive treaty or agreement; it requires a constitutional amendment under Article 368.\nReason (R): Article 1 of the Constitution establishes India as an indestructible union of indestructible states where state borders are permanent and unalterable.",
            "ta": "கூற்று (A): இந்தியப் பகுதியை ஒரு வெளிநாட்டுக்கு விட்டுக்கொடுப்பது என்பது வெறும் நிர்வாக ஒப்பந்தம் அல்லது உடன்படிக்கை மூலம் செய்யப்பட முடியாது; அதற்கு உறுப்பு 368-ன் கீழ் அரசியலமைப்புத் திருத்தம் அவசியம்.\nகாரணம் (R): அரசியலமைப்பின் உறுப்பு 1 இந்தியாவை அழியாத மாநிலங்களின் அழியாத ஒன்றியமாக நிறுவுகிறது, இதில் மாநில எல்லைகள் நிரந்தரமானவை மற்றும் மாற்ற முடியாதவை."
        },
        "options": [
            {"id": "A", "en": "Both Assertion and Reason are true and Reason is the correct explanation of Assertion.", "ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்."},
            {"id": "B", "en": "Both Assertion and Reason are true but Reason is NOT the correct explanation.", "ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல."},
            {"id": "C", "en": "Assertion is true but Reason is false.", "ta": "A சரி, ஆனால் R தவறு."},
            {"id": "D", "en": "Assertion is false but Reason is true.", "ta": "A தவறு, ஆனால் R சரி."}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "Assertion is TRUE because the Supreme Court held in the Berubari Union Case (1960) that Parliament's power to diminish state areas under Article 3 does not cover ceding Indian territory to a foreign country, which necessitates an amendment under Article 368. Reason is FALSE because India is an 'Indestructible Union of Destructible States' where Parliament can alter state boundaries under Article 3 without their consent.",
            "ta": "கூற்று A சரி; ஏனெனில் பெருபாரி யூனியன் வழக்கில் (1960) உறுப்பு 3-ன் கீழ் எல்லைகளை மாற்றும் அதிகாரம் வெளிநாட்டுக்கு நிலத்தை விட்டுக் கொடுப்பதை உள்ளடக்காது, அதற்கு உறுப்பு 368-ன் கீழ் திருத்தம் தேவை என உச்ச நீதிமன்றம் கூறியது. காரணம் R தவறு; ஏனெனில் இந்தியா 'அழியக்கூடிய மாநிலங்களின் அழியாத ஒன்றியம்' ஆகும்; உறுப்பு 3-ன் கீழ் மாநில எல்லைகளை மாற்ற நாடாளுமன்றத்திற்கு முழு அதிகாரம் உண்டு."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Reason is false as Indian states are destructible.", "ta": "தவறு. இந்திய மாநிலங்கள் அழிக்கக்கூடியவை (மாற்றக்கூடியவை) என்பதால் காரணம் தவறானது."},
            "B": {"en": "Incorrect. Reason is false.", "ta": "தவறு. காரணம் தவறானது."},
            "C": {"en": "Correct. Assertion is true; Reason is false.", "ta": "சரி. கூற்று A சரி; காரணம் R தவறு."},
            "D": {"en": "Incorrect. Assertion is true.", "ta": "தவறு. கூற்று சரியானது."}
        },
        "tnpsc_tip": {
            "en": "USA is an 'Indestructible Union of Indestructible States'. India is an 'Indestructible Union of DESTRUCTIBLE States'.",
            "ta": "அமெரிக்கா = 'அழியாத மாநிலங்களின் அழியாத ஒன்றியம்'. இந்தியா = 'அழியக்கூடிய (மாற்றக்கூடிய) மாநிலங்களின் அழியாத ஒன்றியம்'."
        },
        "revision_fact": {
            "en": "The 9th Constitutional Amendment Act (1960) was enacted to transfer the Berubari Union territory to Pakistan.",
            "ta": "பெருபாரி யூனியன் பகுதியை பாகிஸ்தானுக்கு மாற்றுவதற்காக 9வது அரசியலமைப்புத் திருத்தச் சட்டம் (1960) இயற்றப்பட்டது."
        },
        "source_reference": ["In re Berubari Union (1960)", "M. Laxmikanth - Indian Polity"],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "Sovereignty", "Article 1", "Berubari Union 1960"],
        "question_en": "Assertion (A): Cession of Indian territory to a foreign country cannot be effected by a mere executive treaty or agreement; it requires a constitutional amendment under Article 368.\nReason (R): Article 1 of the Constitution establishes India as an indestructible union of indestructible states where state borders are permanent and unalterable.",
        "question_ta": "கூற்று (A): இந்தியப் பகுதியை ஒரு வெளிநாட்டுக்கு விட்டுக்கொடுப்பது என்பது வெறும் நிர்வாக ஒப்பந்தம் அல்லது உடன்படிக்கை மூலம் செய்யப்பட முடியாது; அதற்கு உறுப்பு 368-ன் கீழ் அரசியலமைப்புத் திருத்தம் அவசியம்.\nகாரணம் (R): அரசியலமைப்பின் உறுப்பு 1 இந்தியாவை அழியாத மாநிலங்களின் அழியாத ஒன்றியமாக நிறுவுகிறது, இதில் மாநில எல்லைகள் நிரந்தரமானவை மற்றும் மாற்ற முடியாதவை.",
        "options_en": [
            "Both Assertion and Reason are true and Reason is the correct explanation of Assertion.",
            "Both Assertion and Reason are true but Reason is NOT the correct explanation.",
            "Assertion is true but Reason is false.",
            "Assertion is false but Reason is true."
        ],
        "options_ta": [
            "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்.",
            "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல.",
            "A சரி, ஆனால் R தவறு.",
            "A தவறு, ஆனால் R சரி."
        ],
        "answer": "c",
        "explanation_en": "Assertion is TRUE because the Supreme Court held in the Berubari Union Case (1960) that Parliament's power to diminish state areas under Article 3 does not cover ceding Indian territory to a foreign country, which necessitates an amendment under Article 368. Reason is FALSE because India is an 'Indestructible Union of Destructible States' where Parliament can alter state boundaries under Article 3 without their consent.",
        "explanation_ta": "கூற்று A சரி; ஏனெனில் பெருபாரி யூனியன் வழக்கில் (1960) உறுப்பு 3-ன் கீழ் எல்லைகளை மாற்றும் அதிகாரம் வெளிநாட்டுக்கு நிலத்தை விட்டுக் கொடுப்பதை உள்ளடக்காது, அதற்கு உறுப்பு 368-ன் கீழ் திருத்தம் தேவை என உச்ச நீதிமன்றம் கூறியது. காரணம் R தவறு; ஏனெனில் இந்தியா 'அழியக்கூடிய மாநிலங்களின் அழியாத ஒன்றியம்' ஆகும்; உறுப்பு 3-ன் கீழ் மாநில எல்லைகளை மாற்ற நாடாளுமன்றத்திற்கு முழு அதிகாரம் உண்டு."
    },

    # =========================================================================
    # Q21: PRE_AR_021 (Answer: B) - Representative vs Direct Democracy
    # =========================================================================
    {
        "id": "PRE_AR_021",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Medium",
        "question_type": "Assertion & Reason",
        "question": {
            "en": "Assertion (A): The Constitution of India provides for an indirect representative parliamentary democracy rather than a direct democracy.\nReason (R): Instruments of direct democracy such as Referendum, Initiative, Recall, and Plebiscite are not incorporated in the Constitution of India.",
            "ta": "கூற்று (A): இந்திய அரசியலமைப்பு நேரடி ஜனநாயகத்திற்குப் பதிலாக மறைமுக பிரதிநிதித்துவ நாடாளுமன்ற ஜனநாயகத்தை வழங்குகிறது.\nகாரணம் (R): பொது வாக்கெடுப்பு (Referendum), முன்முயற்சி (Initiative), திரும்ப அழைத்தல் (Recall) மற்றும் மக்கள் கருத்துக்கணிப்பு (Plebiscite) போன்ற நேரடி ஜனநாயகக் கருவிகள் இந்திய அரசியலமைப்பில் சேர்க்கப்படவில்லை."
        },
        "options": [
            {"id": "A", "en": "Both Assertion and Reason are true and Reason is the correct explanation of Assertion.", "ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்."},
            {"id": "B", "en": "Both Assertion and Reason are true but Reason is NOT the correct explanation.", "ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல."},
            {"id": "C", "en": "Assertion is true but Reason is false.", "ta": "A சரி, ஆனால் R தவறு."},
            {"id": "D", "en": "Assertion is false but Reason is true.", "ta": "A தவறு, ஆனால் R சரி."}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "Both Assertion and Reason are true, but Reason is NOT the direct explanation. India adopted indirect parliamentary democracy due to its vast size, huge population, diversity, and familiarity with British parliamentary institutions. The absence of direct democracy devices is a consequence/feature of this choice, not the causal reason for adopting representative democracy.",
            "ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல. நாட்டின் பரந்த அளவு, அதிக மக்கள் தொகை, பன்முகத்தன்மை மற்றும் பிரிட்டிஷ் நாடாளுமன்ற அமைப்பின் மீதான பரிச்சயம் ஆகியவற்றின் காரணமாகவே இந்தியா பிரதிநிதித்துவ ஜனநாயகத்தை ஏற்றுக்கொண்டது. நேரடி ஜனநாயக கருவிகள் இல்லாதிருப்பது இந்த தேர்வின் பண்பே தவிர, பிரதிநிதித்துவ அமைப்பை ஏற்றுக்கொண்டதற்கான முதன்மைக் காரணமல்ல."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Reason lists absent direct democracy tools, but does not explain why representative democracy was chosen.", "ta": "தவறு. காரணம் நேரடி ஜனநாயகக் கருவிகள் இல்லாததை விவரிக்கிறதே தவிர, பிரதிநிதித்துவ அமைப்பு ஏன் தேர்ந்தெடுக்கப்பட்டது என்பதை விளக்கவில்லை."},
            "B": {"en": "Correct. Both statements are true, but Reason is a descriptive characteristic.", "ta": "சரி. இரண்டும் உண்மை; காரணம் ஒரு விவரணப் பண்பு."},
            "C": {"en": "Incorrect. Reason is factually true.", "ta": "தவறு. காரணம் உண்மையானது."},
            "D": {"en": "Incorrect. Assertion is true.", "ta": "தவறு. கூற்று சரியானது."}
        },
        "tnpsc_tip": {
            "en": "Direct Democracy tools: 1. Referendum, 2. Initiative, 3. Recall, 4. Plebiscite (e.g. in Switzerland). India has Indirect Representative Democracy.",
            "ta": "நேரடி ஜனநாயகக் கருவிகள்: 1. பொது வாக்கெடுப்பு, 2. முன்முயற்சி, 3. திரும்ப அழைத்தல், 4. மக்கள் கருத்துக்கணிப்பு (எ.கா: சுவிட்சர்லாந்து). இந்தியாவில் மறைமுக பிரதிநிதித்துவ ஜனநாயகம் உள்ளது."
        },
        "revision_fact": {
            "en": "In a Parliamentary democracy, the executive is collectively responsible to the popularly elected legislature (Lok Sabha/State Legislative Assembly).",
            "ta": "நாடாளுமன்ற ஜனநாயகத்தில், நிர்வாகத்துறை மக்களால் தேர்ந்தெடுக்கப்பட்ட சட்டமன்றத்திற்கு (மக்களவை/சட்டமன்றப் பேரவை) கூட்டாகப் பொறுப்புடையது."
        },
        "source_reference": ["M. Laxmikanth - Indian Polity", "NCERT Class XI - Indian Constitution at Work"],
        "bloom_level": "Understand",
        "estimated_time_sec": 65,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "Democracy", "Representative Democracy", "Direct Democracy"],
        "question_en": "Assertion (A): The Constitution of India provides for an indirect representative parliamentary democracy rather than a direct democracy.\nReason (R): Instruments of direct democracy such as Referendum, Initiative, Recall, and Plebiscite are not incorporated in the Constitution of India.",
        "question_ta": "கூற்று (A): இந்திய அரசியலமைப்பு நேரடி ஜனநாயகத்திற்குப் பதிலாக மறைமுக பிரதிநிதித்துவ நாடாளுமன்ற ஜனநாயகத்தை வழங்குகிறது.\nகாரணம் (R): பொது வாக்கெடுப்பு (Referendum), முன்முயற்சி (Initiative), திரும்ப அழைத்தல் (Recall) மற்றும் மக்கள் கருத்துக்கணிப்பு (Plebiscite) போன்ற நேரடி ஜனநாயகக் கருவிகள் இந்திய அரசியலமைப்பில் சேர்க்கப்படவில்லை.",
        "options_en": [
            "Both Assertion and Reason are true and Reason is the correct explanation of Assertion.",
            "Both Assertion and Reason are true but Reason is NOT the correct explanation.",
            "Assertion is true but Reason is false.",
            "Assertion is false but Reason is true."
        ],
        "options_ta": [
            "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்.",
            "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல.",
            "A சரி, ஆனால் R தவறு.",
            "A தவறு, ஆனால் R சரி."
        ],
        "answer": "b",
        "explanation_en": "Both Assertion and Reason are true, but Reason is NOT the direct explanation. India adopted indirect parliamentary democracy due to its vast size, huge population, diversity, and familiarity with British parliamentary institutions. The absence of direct democracy devices is a consequence/feature of this choice, not the causal reason for adopting representative democracy.",
        "explanation_ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல. நாட்டின் பரந்த அளவு, அதிக மக்கள் தொகை, பன்முகத்தன்மை மற்றும் பிரிட்டிஷ் நாடாளுமன்ற அமைப்பின் மீதான பரிச்சயம் ஆகியவற்றின் காரணமாகவே இந்தியா பிரதிநிதித்துவ ஜனநாயகத்தை ஏற்றுக்கொண்டது. நேரடி ஜனநாயக கருவிகள் இல்லாதிருப்பது இந்த தேர்வின் பண்பே தவிர, பிரதிநிதித்துவ அமைப்பை ஏற்றுக்கொண்டதற்கான முதன்மைக் காரணமல்ல."
    },

    # =========================================================================
    # Q22: PRE_AR_022 (Answer: D) - Enactment Procedure Timing Trap
    # =========================================================================
    {
        "id": "PRE_AR_022",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Assertion & Reason",
        "question": {
            "en": "Assertion (A): The Constituent Assembly debated and enacted the Preamble first, before debating or enacting any other Part of the Constitution, to establish the supreme foundational guiding framework.\nReason (R): The Preamble was enacted by the Constituent Assembly after the rest of the Constitution was already enacted, specifically to ensure that it conformed in every detail to the Constitution as approved by the Assembly.",
            "ta": "கூற்று (A): அரசியலமைப்பு நிர்ணய அவை உச்ச வழிகாட்டும் கட்டமைப்பை நிறுவுவதற்காக, அரசியலமைப்பின் எந்தவொரு பகுதியை விவாதித்து நிறைவேற்றுவதற்கு முன்பாகவே, முதலில் முகவுரையை விவாதித்து நிறைவேற்றியது.\nகாரணம் (R): அரசியலமைப்பு நிர்ணய அவையால் ஏற்றுக்கொள்ளப்பட்ட அரசியலமைப்பின் அனைத்து விதிகளுடனும் முகவுரை முழுமையாக ஒத்துப்போவதை உறுதி செய்வதற்காகவே, அரசியலமைப்பின் மற்ற பகுதிகள் இயற்றப்பட்ட பின்னரே இறுதியாக முகவுரை இயற்றப்பட்டது."
        },
        "options": [
            {"id": "A", "en": "Both Assertion and Reason are true and Reason is the correct explanation of Assertion.", "ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்."},
            {"id": "B", "en": "Both Assertion and Reason are true but Reason is NOT the correct explanation.", "ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல."},
            {"id": "C", "en": "Assertion is true but Reason is false.", "ta": "A சரி, ஆனால் R தவறு."},
            {"id": "D", "en": "Assertion is false but Reason is true.", "ta": "A தவறு, ஆனால் R சரி."}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "Assertion is FALSE because the Preamble was voted and enacted LAST by the Constituent Assembly on October 17, 1949. Reason is TRUE because the explicit reason given by Assembly President Dr. Rajendra Prasad for taking up the Preamble last was to ensure its complete harmony and consistency with the rest of the Constitution.",
            "ta": "கூற்று A தவறு; ஏனெனில் அரசியலமைப்பு அவையால் முகவுரை இறுதியாக அக்டோபர் 17, 1949 அன்றுதான் நிறைவேற்றப்பட்டது. காரணம் R சரி; ஏனெனில் அரசியலமைப்பின் மற்ற அனைத்து பகுதிகளுடனும் முகவுரை முழுமையாக ஒத்துப்போவதை உறுதி செய்வதற்காகவே அது இறுதியில் எடுத்துக்கொள்ளப்பட்டது என்று தலைவர் டாக்டர் ராஜேந்திர பிரசாத் தெளிவுபடுத்தினார்."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Assertion is false.", "ta": "தவறு. கூற்று தவறானது."},
            "B": {"en": "Incorrect. Assertion is false.", "ta": "தவறு. கூற்று தவறானது."},
            "C": {"en": "Incorrect. Assertion is false.", "ta": "தவறு. கூற்று தவறானது."},
            "D": {"en": "Correct. Assertion is false (Preamble was enacted last, not first); Reason is true.", "ta": "சரி. கூற்று A தவறு (முகவுரை இறுதியாக இயற்றப்பட்டது, முதலில் அல்ல); காரணம் R சரி."}
        },
        "tnpsc_tip": {
            "en": "TNPSC Trap: Objectives Resolution was moved FIRST (Dec 13, 1946), but the Preamble was enacted LAST (Oct 17, 1949) after the rest of the Constitution was passed.",
            "ta": "TNPSC பொறி: குறிக்கோள் தீர்மானம் முதலில் முன்மொழியப்பட்டது (டிசம்பர் 13, 1946); ஆனால் முகவுரை அரசியலமைப்பின் மற்ற பகுதிகள் முடிந்த பிறகு இறுதியாக நிறைவேற்றப்பட்டது (அக்டோபர் 17, 1949)."
        },
        "revision_fact": {
            "en": "On October 17, 1949, Dr. Rajendra Prasad put the motion: 'The question is that the Preamble stand part of the Constitution.'",
            "ta": "அக்டோபர் 17, 1949 அன்று, டாக்டர் ராஜேந்திர பிரசாத் 'முகவுரை அரசியலமைப்பின் ஒரு பகுதியாக அமைய வேண்டும்' என்ற பிரேரணையை நிறைவேற்றினார்."
        },
        "source_reference": ["Constituent Assembly Debates", "M. Laxmikanth - Indian Polity"],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "Constituent Assembly", "Enactment Timing"],
        "question_en": "Assertion (A): The Constituent Assembly debated and enacted the Preamble first, before debating or enacting any other Part of the Constitution, to establish the supreme foundational guiding framework.\nReason (R): The Preamble was enacted by the Constituent Assembly after the rest of the Constitution was already enacted, specifically to ensure that it conformed in every detail to the Constitution as approved by the Assembly.",
        "question_ta": "கூற்று (A): அரசியலமைப்பு நிர்ணய அவை உச்ச வழிகாட்டும் கட்டமைப்பை நிறுவுவதற்காக, அரசியலமைப்பின் எந்தவொரு பகுதியை விவாதித்து நிறைவேற்றுவதற்கு முன்பாகவே, முதலில் முகவுரையை விவாதித்து நிறைவேற்றியது.\nகாரணம் (R): அரசியலமைப்பு நிர்ணய அவையால் ஏற்றுக்கொள்ளப்பட்ட அரசியலமைப்பின் அனைத்து விதிகளுடனும் முகவுரை முழுமையாக ஒத்துப்போவதை உறுதி செய்வதற்காகவே, அரசியலமைப்பின் மற்ற பகுதிகள் இயற்றப்பட்ட பின்னரே இறுதியாக முகவுரை இயற்றப்பட்டது.",
        "options_en": [
            "Both Assertion and Reason are true and Reason is the correct explanation of Assertion.",
            "Both Assertion and Reason are true but Reason is NOT the correct explanation.",
            "Assertion is true but Reason is false.",
            "Assertion is false but Reason is true."
        ],
        "options_ta": [
            "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்.",
            "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல.",
            "A சரி, ஆனால் R தவறு.",
            "A தவறு, ஆனால் R சரி."
        ],
        "answer": "d",
        "explanation_en": "Assertion is FALSE because the Preamble was voted and enacted LAST by the Constituent Assembly on October 17, 1949. Reason is TRUE because the explicit reason given by Assembly President Dr. Rajendra Prasad for taking up the Preamble last was to ensure its complete harmony and consistency with the rest of the Constitution.",
        "explanation_ta": "கூற்று A தவறு; ஏனெனில் அரசியலமைப்பு அவையால் முகவுரை இறுதியாக அக்டோபர் 17, 1949 அன்றுதான் நிறைவேற்றப்பட்டது. காரணம் R சரி; ஏனெனில் அரசியலமைப்பின் மற்ற அனைத்து பகுதிகளுடனும் முகவுரை முழுமையாக ஒத்துப்போவதை உறுதி செய்வதற்காகவே அது இறுதியில் எடுத்துக்கொள்ளப்பட்டது என்று தலைவர் டாக்டர் ராஜேந்திர பிரசாத் தெளிவுபடுத்தினார்."
    },

    # =========================================================================
    # Q23: PRE_AR_023 (Answer: D) - Universal Adult Franchise Trap
    # =========================================================================
    {
        "id": "PRE_AR_023",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Assertion & Reason",
        "question": {
            "en": "Assertion (A): The Constitution of India initially restricted voting rights to literate taxpayers and property owners under Article 326, which was later broadened to all adults.\nReason (R): Article 326 established Universal Adult Franchise from the inception of the Constitution without any property, tax, or educational qualification to secure 'Political Justice' as promised in the Preamble.",
            "ta": "கூற்று (A): இந்திய அரசியலமைப்பு ஆரம்பத்தில் உறுப்பு 326-ன் கீழ் கல்வி கற்ற வரி செலுத்துவோர் மற்றும் சொத்துரிமை உள்ளவர்களுக்கு மட்டுமே வாக்குரிமையை மட்டுப்படுத்தியது, பின்னர் அது அனைத்து பெரியவர்களுக்கும் விரிவுபடுத்தப்பட்டது.\nகாரணம் (R): முகவுரையில் வாக்குறுதி அளிக்கப்பட்ட 'அரசியல் நீதியை' உறுதி செய்வதற்காக, உறுப்பு 326 தொடக்கத்திலிருந்தே எந்தவொரு சொத்து, வரி அல்லது கல்வித் தகுதியும் இன்றி வயதுவந்தோர் அனைவருக்கும் வாக்குரிமையை நிறுவியது."
        },
        "options": [
            {"id": "A", "en": "Both Assertion and Reason are true and Reason is the correct explanation of Assertion.", "ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்."},
            {"id": "B", "en": "Both Assertion and Reason are true but Reason is NOT the correct explanation.", "ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல."},
            {"id": "C", "en": "Assertion is true but Reason is false.", "ta": "A சரி, ஆனால் R தவறு."},
            {"id": "D", "en": "Assertion is false but Reason is true.", "ta": "A தவறு, ஆனால் R சரி."}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "Assertion is FALSE because the Government of India Act 1935 restricted voting rights based on property and education (giving only 14% suffrage), but the Constitution of India in 1950 introduced Universal Adult Franchise immediately to all citizens aged 21 and above (reduced to 18 by the 61st Amendment). Reason is TRUE.",
            "ta": "கூற்று A தவறு; ஏனெனில் 1935 ஆம் ஆண்டின் இந்திய அரசுச் சட்டம் சொத்து மற்றும் கல்வி அடிப்படையில் வாக்குரிமையைக் கட்டுப்படுத்தியிருந்தது (14% மக்களுக்கு மட்டுமே), ஆனால் 1950 அரசியலமைப்பு உடனடியாக 21 வயது நிரம்பிய அனைத்து குடிமக்களுக்கும் வயதுவந்தோர் வாக்குரிமையை வழங்கியது (61வது திருத்தத்தால் இது 18 ஆகக் குறைக்கப்பட்டது). காரணம் R சரி."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Assertion is false.", "ta": "தவறு. கூற்று தவறானது."},
            "B": {"en": "Incorrect. Assertion is false.", "ta": "தவறு. கூற்று தவறானது."},
            "C": {"en": "Incorrect. Assertion is false.", "ta": "தவறு. கூற்று தவறானது."},
            "D": {"en": "Correct. Assertion is false (1950 Constitution gave universal adult franchise immediately); Reason is true.", "ta": "சரி. கூற்று A தவறு (1950 அரசியலமைப்பு உடனடியாக அனைவருக்கும் வாக்குரிமை தந்தது); காரணம் R சரி."}
        },
        "tnpsc_tip": {
            "en": "61st Constitutional Amendment Act, 1988 (effective 1989) lowered the voting age from 21 years to 18 years under Article 326.",
            "ta": "61வது அரசியலமைப்புத் திருத்தச் சட்டம் 1988 (நடைமுறை 1989) உறுப்பு 326-ன் கீழ் வாக்களிக்கும் வயதை 21-லிருந்து 18 ஆகக் குறைத்தது."
        },
        "revision_fact": {
            "en": "Alladi Krishnaswami Iyer hailed the introduction of adult franchise as 'an act of faith in the common man of India'.",
            "ta": "அல்லாடி கிருஷ்ணசுவாமி ஐயர் வயதுவந்தோர் வாக்குரிமையை 'இந்திய சாமானிய மனிதன் மீது வைக்கப்பட்ட ஒரு மகத்தான நம்பிக்கை' என்று பாராட்டினார்."
        },
        "source_reference": ["M. Laxmikanth - Indian Polity", "Constitution of India Article 326"],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "Political Justice", "Article 326", "Adult Franchise"],
        "question_en": "Assertion (A): The Constitution of India initially restricted voting rights to literate taxpayers and property owners under Article 326, which was later broadened to all adults.\nReason (R): Article 326 established Universal Adult Franchise from the inception of the Constitution without any property, tax, or educational qualification to secure 'Political Justice' as promised in the Preamble.",
        "question_ta": "கூற்று (A): இந்திய அரசியலமைப்பு ஆரம்பத்தில் உறுப்பு 326-ன் கீழ் கல்வி கற்ற வரி செலுத்துவோர் மற்றும் சொத்துரிமை உள்ளவர்களுக்கு மட்டுமே வாக்குரிமையை மட்டுப்படுத்தியது, பின்னர் அது அனைத்து பெரியவர்களுக்கும் விரிவுபடுத்தப்பட்டது.\nகாரணம் (R): முகவுரையில் வாக்குறுதி அளிக்கப்பட்ட 'அரசியல் நீதியை' உறுதி செய்வதற்காக, உறுப்பு 326 தொடக்கத்திலிருந்தே எந்தவொரு சொத்து, வரி அல்லது கல்வித் தகுதியும் இன்றி வயதுவந்தோர் அனைவருக்கும் வாக்குரிமையை நிறுவியது.",
        "options_en": [
            "Both Assertion and Reason are true and Reason is the correct explanation of Assertion.",
            "Both Assertion and Reason are true but Reason is NOT the correct explanation.",
            "Assertion is true but Reason is false.",
            "Assertion is false but Reason is true."
        ],
        "options_ta": [
            "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்.",
            "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல.",
            "A சரி, ஆனால் R தவறு.",
            "A தவறு, ஆனால் R சரி."
        ],
        "answer": "d",
        "explanation_en": "Assertion is FALSE because the Government of India Act 1935 restricted voting rights based on property and education (giving only 14% suffrage), but the Constitution of India in 1950 introduced Universal Adult Franchise immediately to all citizens aged 21 and above (reduced to 18 by the 61st Amendment). Reason is TRUE.",
        "explanation_ta": "கூற்று A தவறு; ஏனெனில் 1935 ஆம் ஆண்டின் இந்திய அரசுச் சட்டம் சொத்து மற்றும் கல்வி அடிப்படையில் வாக்குரிமையைக் கட்டுப்படுத்தியிருந்தது (14% மக்களுக்கு மட்டுமே), ஆனால் 1950 அரசியலமைப்பு உடனடியாக 21 வயது நிரம்பிய அனைத்து குடிமக்களுக்கும் வயதுவந்தோர் வாக்குரிமையை வழங்கியது (61வது திருத்தத்தால் இது 18 ஆகக் குறைக்கப்பட்டது). காரணம் R சரி."
    },

    # =========================================================================
    # Q24: PRE_AR_024 (Answer: D) - Basic Structure Absolute Immunity Trap
    # =========================================================================
    {
        "id": "PRE_AR_024",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Assertion & Reason",
        "question": {
            "en": "Assertion (A): Parliament can exercise its constituent amending power under Article 368 to completely delete the words 'Secular' or 'Democratic' from the Preamble by passing a constitutional amendment with a two-thirds majority.\nReason (R): In Kesavananda Bharati (1973) and S.R. Bommai (1994), the Supreme Court established that Secularism and Democracy are inviolable parts of the 'Basic Structure' of the Constitution which Parliament cannot abrogate.",
            "ta": "கூற்று (A): நாடாளுமன்றம் மூன்றில் இரண்டு பங்கு பெரும்பான்மையுடன் அரசியலமைப்புத் திருத்தத்தை நிறைவேற்றுவதன் மூலம், முகவுரையிலிருந்து 'மதச்சார்பற்ற' அல்லது 'ஜனநாயக' என்ற சொற்களை முற்றிலும் நீக்குவதற்கு உறுப்பு 368-ன் கீழ் தனது திருத்தும் அதிகாரத்தைப் பயன்படுத்த முடியும்.\nகாரணம் (R): கேசவானந்த பாரதி (1973) மற்றும் எஸ்.ஆர். பொம்மை (1994) வழக்குகளில், மதச்சார்பின்மை மற்றும் ஜனநாயகம் ஆகியவை அரசியலமைப்பின் 'அடிப்படை கட்டமைப்பின்' மீற முடியாத பகுதிகள் என்றும், நாடாளுமன்றம் அவற்றை ரத்து செய்ய முடியாது என்றும் உச்ச நீதிமன்றம் நிறுவியுள்ளது."
        },
        "options": [
            {"id": "A", "en": "Both Assertion and Reason are true and Reason is the correct explanation of Assertion.", "ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்."},
            {"id": "B", "en": "Both Assertion and Reason are true but Reason is NOT the correct explanation.", "ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல."},
            {"id": "C", "en": "Assertion is true but Reason is false.", "ta": "A சரி, ஆனால் R தவறு."},
            {"id": "D", "en": "Assertion is false but Reason is true.", "ta": "A தவறு, ஆனால் R சரி."}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "Assertion is FALSE because Parliament's amending power under Article 368 is limited and cannot be used to alter, damage, or destroy the Basic Structure (which includes Secularism, Democracy, Republic, and Rule of Law). Reason is TRUE because it cites the authoritative constitutional rulings of the Supreme Court.",
            "ta": "கூற்று A தவறு; ஏனெனில் உறுப்பு 368-ன் கீழான நாடாளுமன்றத்தின் அதிகாரம் வரம்புக்குட்பட்டது; மதச்சார்பின்மை, ஜனநாயகம், குடியரசு போன்ற அடிப்படை கட்டமைப்பை மாற்றவோ அழிக்கவோ முடியாது. காரணம் R சரி; ஏனெனில் உச்ச நீதிமன்றத்தின் அதிகாரப்பூர்வ தீர்ப்புகளை அது சரியாகக் குறிப்பிடுகிறது."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Assertion is false as Basic Structure is non-amendable.", "ta": "தவறு. அடிப்படை கட்டமைப்பு திருத்தப்பட முடியாதது என்பதால் கூற்று தவறானது."},
            "B": {"en": "Incorrect. Assertion is false.", "ta": "தவறு. கூற்று தவறானது."},
            "C": {"en": "Incorrect. Assertion is false.", "ta": "தவறு. கூற்று தவறானது."},
            "D": {"en": "Correct. Assertion is false (Basic Structure cannot be destroyed); Reason is true.", "ta": "சரி. கூற்று A தவறு (அடிப்படை கட்டமைப்பை அழிக்க முடியாது); காரணம் R சரி."}
        },
        "tnpsc_tip": {
            "en": "Amendability under Article 368 is subject to the doctrine of Basic Structure. Preamble CAN be amended, but its BASIC FEATURES CANNOT be amended.",
            "ta": "உறுப்பு 368-ன் கீழ் திருத்துவது அடிப்படை கட்டமைப்பு கோட்பாட்டிற்கு உட்பட்டது. முகவுரை திருத்தப்படலாம், ஆனால் அதன் அடிப்படை அம்சங்கள் திருத்தப்பட முடியாது."
        },
        "revision_fact": {
            "en": "In Indira Nehru Gandhi v. Raj Narain (1975), the Supreme Court applied the Basic Structure doctrine for the first time to strike down the 39th Amendment (Article 329A).",
            "ta": "இந்திரா காந்தி வழக்கில் (1975), உச்ச நீதிமன்றம் முதன்முறையாக அடிப்படை கட்டமைப்பு கோட்பாட்டைப் பயன்படுத்தி 39வது திருத்தத்தை (உறுப்பு 329A) ரத்து செய்தது."
        },
        "source_reference": ["Kesavananda Bharati Case (1973)", "S.R. Bommai Case (1994)", "M. Laxmikanth - Indian Polity"],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "Basic Structure", "Article 368", "Kesavananda Bharati"],
        "question_en": "Assertion (A): Parliament can exercise its constituent amending power under Article 368 to completely delete the words 'Secular' or 'Democratic' from the Preamble by passing a constitutional amendment with a two-thirds majority.\nReason (R): In Kesavananda Bharati (1973) and S.R. Bommai (1994), the Supreme Court established that Secularism and Democracy are inviolable parts of the 'Basic Structure' of the Constitution which Parliament cannot abrogate.",
        "question_ta": "கூற்று (A): நாடாளுமன்றம் மூன்றில் இரண்டு பங்கு பெரும்பான்மையுடன் அரசியலமைப்புத் திருத்தத்தை நிறைவேற்றுவதன் மூலம், முகவுரையிலிருந்து 'மதச்சார்பற்ற' அல்லது 'ஜனநாயக' என்ற சொற்களை முற்றிலும் நீக்குவதற்கு உறுப்பு 368-ன் கீழ் தனது திருத்தும் அதிகாரத்தைப் பயன்படுத்த முடியும்.\nகாரணம் (R): கேசவானந்த பாரதி (1973) மற்றும் எஸ்.ஆர். பொம்மை (1994) வழக்குகளில், மதச்சார்பின்மை மற்றும் ஜனநாயகம் ஆகியவை அரசியலமைப்பின் 'அடிப்படை கட்டமைப்பின்' மீற முடியாத பகுதிகள் என்றும், நாடாளுமன்றம் அவற்றை ரத்து செய்ய முடியாது என்றும் உச்ச நீதிமன்றம் நிறுவியுள்ளது.",
        "options_en": [
            "Both Assertion and Reason are true and Reason is the correct explanation of Assertion.",
            "Both Assertion and Reason are true but Reason is NOT the correct explanation.",
            "Assertion is true but Reason is false.",
            "Assertion is false but Reason is true."
        ],
        "options_ta": [
            "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்.",
            "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல.",
            "A சரி, ஆனால் R தவறு.",
            "A தவறு, ஆனால் R சரி."
        ],
        "answer": "d",
        "explanation_en": "Assertion is FALSE because Parliament's amending power under Article 368 is limited and cannot be used to alter, damage, or destroy the Basic Structure (which includes Secularism, Democracy, Republic, and Rule of Law). Reason is TRUE because it cites the authoritative constitutional rulings of the Supreme Court.",
        "explanation_ta": "கூற்று A தவறு; ஏனெனில் உறுப்பு 368-ன் கீழான நாடாளுமன்றத்தின் அதிகாரம் வரம்புக்குட்பட்டது; மதச்சார்பின்மை, ஜனநாயகம், குடியரசு போன்ற அடிப்படை கட்டமைப்பை மாற்றவோ அழிக்கவோ முடியாது. காரணம் R சரி; ஏனெனில் உச்ச நீதிமன்றத்தின் அதிகாரப்பூர்வ தீர்ப்புகளை அது சரியாகக் குறிப்பிடுகிறது."
    },

    # =========================================================================
    # Q25: PRE_AR_025 (Answer: D) - Preamble Juristic Significance Trap
    # =========================================================================
    {
        "id": "PRE_AR_025",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Medium",
        "question_type": "Assertion & Reason",
        "question": {
            "en": "Assertion (A): The Preamble is merely an ornamental preface possessing zero legal, constitutional, or judicial significance in the interpretation of the Indian Constitution.\nReason (R): Eminent constitutional jurists and the Supreme Court have hailed the Preamble as the 'Soul of the Constitution', the 'Horoscope of our Sovereign Democratic Republic', and the 'Key to the minds of the constitution makers'.",
            "ta": "கூற்று (A): முகவுரை என்பது இந்திய அரசியலமைப்பின் விளக்கத்தில் பூஜ்ஜிய சட்ட, அரசியலமைப்பு அல்லது நீதித்துறை முக்கியத்துவம் கொண்ட வெறும் அலங்கார முன்னுரை மட்டுமே ஆகும்.\nகாரணம் (R): புகழ்பெற்ற அரசியலமைப்பு சட்ட வல்லுநர்களும் உச்ச நீதிமன்றமும் முகவுரையை 'அரசியலமைப்பின் ஆன்மா', 'நமது இறையாண்மை ஜனநாயக குடியரசின் ஜாதகம்' மற்றும் 'அரசியலமைப்புச் சிற்பிகளின் மனதைத் திறக்கும் சாவி' என்று போற்றியுள்ளனர்."
        },
        "options": [
            {"id": "A", "en": "Both Assertion and Reason are true and Reason is the correct explanation of Assertion.", "ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்."},
            {"id": "B", "en": "Both Assertion and Reason are true but Reason is NOT the correct explanation.", "ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல."},
            {"id": "C", "en": "Assertion is true but Reason is false.", "ta": "A சரி, ஆனால் R தவறு."},
            {"id": "D", "en": "Assertion is false but Reason is true.", "ta": "A தவறு, ஆனால் R சரி."}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "Assertion is completely FALSE because the Preamble plays a vital role as an interpretive compass, expresses the foundational philosophy of the Constitution, and is an integral part of the Constitution. Reason is TRUE, reflecting famous statements by K.M. Munshi ('Horoscope'), Pandit Thakur Das Bhargava ('Soul'), and Sir Ernest Barker ('Key-note').",
            "ta": "கூற்று A முற்றிலும் தவறு; ஏனெனில் முகவுரை அரசியலமைப்பின் அடித்தள தத்துவத்தை வெளிப்படுத்தும் ஒரு ஒருங்கிணைந்த பகுதியாகும். காரணம் R சரி; கே.எம். முன்ஷி ('ஜாதகம்'), தாகூர் தாஸ் பார்கவா ('ஆன்மா') மற்றும் எர்னஸ்ட் பார்கர் ('முக்கிய குறிப்பு') ஆகியோரின் புகழ்பெற்ற கூற்றுகளை இது பிரதிபலிக்கிறது."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Assertion is false.", "ta": "தவறு. கூற்று தவறானது."},
            "B": {"en": "Incorrect. Assertion is false.", "ta": "தவறு. கூற்று தவறானது."},
            "C": {"en": "Incorrect. Assertion is false.", "ta": "தவறு. கூற்று தவறானது."},
            "D": {"en": "Correct. Assertion is false (Preamble holds immense constitutional value); Reason is true.", "ta": "சரி. கூற்று A தவறு (முகவுரை மகத்தான அரசியலமைப்பு மதிப்புடையது); காரணம் R சரி."}
        },
        "tnpsc_tip": {
            "en": "Key quotes on Preamble: K.M. Munshi = 'Horoscope', Pandit Thakur Das Bhargava = 'Soul / Jewel set in the Constitution', N.A. Palkhivala = 'Identity Card', Sir Ernest Barker = 'Key-note'.",
            "ta": "முகவுரை பற்றிய முக்கிய மேற்கோள்கள்: கே.எம். முன்ஷி = 'ஜாதகம்', தாக்கூர் தாஸ் பார்கவா = 'ஆன்மா / ஆபரணம்', என்.ஏ. பல்கிவாலா = 'அடையாள அட்டை', எர்னஸ்ட் பார்கர் = 'முக்கிய குறிப்பு'."
        },
        "revision_fact": {
            "en": "Sir Ernest Barker, a distinguished English political scientist, paid tribute to the Indian Preamble by quoting it at the opening of his book 'Principles of Social and Political Theory' (1951).",
            "ta": "சர் எர்னஸ்ட் பார்கர் தனது 'சமூக மற்றும் அரசியல் கோட்பாட்டின் கொள்கைகள்' (1951) புத்தகத்தின் தொடக்கத்தில் இந்திய முகவுரையை மேற்கோள் காட்டி பெருமைப்படுத்தினார்."
        },
        "source_reference": ["M. Laxmikanth - Indian Polity", "Ernest Barker - Principles of Social and Political Theory"],
        "bloom_level": "Understand",
        "estimated_time_sec": 60,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "Quotes on Preamble", "K.M. Munshi", "Identity Card"],
        "question_en": "Assertion (A): The Preamble is merely an ornamental preface possessing zero legal, constitutional, or judicial significance in the interpretation of the Indian Constitution.\nReason (R): Eminent constitutional jurists and the Supreme Court have hailed the Preamble as the 'Soul of the Constitution', the 'Horoscope of our Sovereign Democratic Republic', and the 'Key to the minds of the constitution makers'.",
        "question_ta": "கூற்று (A): முகவுரை என்பது இந்திய அரசியலமைப்பின் விளக்கத்தில் பூஜ்ஜிய சட்ட, அரசியலமைப்பு அல்லது நீதித்துறை முக்கியத்துவம் கொண்ட வெறும் அலங்கார முன்னுரை மட்டுமே ஆகும்.\nகாரணம் (R): புகழ்பெற்ற அரசியலமைப்பு சட்ட வல்லுநர்களும் உச்ச நீதிமன்றமும் முகவுரையை 'அரசியலமைப்பின் ஆன்மா', 'நமது இறையாண்மை ஜனநாயக குடியரசின் ஜாதகம்' மற்றும் 'அரசியலமைப்புச் சிற்பிகளின் மனதைத் திறக்கும் சாவி' என்று போற்றியுள்ளனர்.",
        "options_en": [
            "Both Assertion and Reason are true and Reason is the correct explanation of Assertion.",
            "Both Assertion and Reason are true but Reason is NOT the correct explanation.",
            "Assertion is true but Reason is false.",
            "Assertion is false but Reason is true."
        ],
        "options_ta": [
            "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்.",
            "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல.",
            "A சரி, ஆனால் R தவறு.",
            "A தவறு, ஆனால் R சரி."
        ],
        "answer": "d",
        "explanation_en": "Assertion is completely FALSE because the Preamble plays a vital role as an interpretive compass, expresses the foundational philosophy of the Constitution, and is an integral part of the Constitution. Reason is TRUE, reflecting famous statements by K.M. Munshi ('Horoscope'), Pandit Thakur Das Bhargava ('Soul'), and Sir Ernest Barker ('Key-note').",
        "explanation_ta": "கூற்று A முற்றிலும் தவறு; ஏனெனில் முகவுரை அரசியலமைப்பின் அடித்தள தத்துவத்தை வெளிப்படுத்தும் ஒரு ஒருங்கிணைந்த பகுதியாகும். காரணம் R சரி; கே.எம். முன்ஷி ('ஜாதகம்'), தாகூர் தாஸ் பார்கவா ('ஆன்மா') மற்றும் எர்னஸ்ட் பார்கர் ('முக்கிய குறிப்பு') ஆகியோரின் புகழ்பெற்ற கூற்றுகளை இது பிரதிபலிக்கிறது."
    }
]

# Combine all 25 questions
all_questions = q_1_to_10 + remaining_questions
assert len(all_questions) == 25, f"Expected 25 questions, got {len(all_questions)}"

# Write to preamble_assertion_reason.json and preamble_reasoning.json
target_files = [
    "data/questions/polity/preamble_assertion_reason.json",
    "data/questions/polity/preamble_reasoning.json"
]

for tf in target_files:
    os.makedirs(os.path.dirname(tf), exist_ok=True)
    with open(tf, "w", encoding="utf-8") as f:
        json.dump(all_questions, f, ensure_ascii=False, indent=2)
    print(f"Successfully wrote {len(all_questions)} questions to '{tf}'")
