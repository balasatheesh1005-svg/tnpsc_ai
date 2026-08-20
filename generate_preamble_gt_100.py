# -*- coding: utf-8 -*-
"""
Generator Script for 100 TNPSC Group 1 Standard Grand Test MCQs
Topic: Preamble of the Constitution of India
Target Output: data/questions/polity/preamble_grand_test.json
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# We will define all 100 questions programmatically with complete dual-schema
raw_gt_questions = [
    # 1 (C) - Direct
    {
        "type": "Direct MCQ", "diff": "Easy", "ans": "C",
        "q_en": "Which date is explicitly mentioned in the Preamble of the Constitution of India as the date of its adoption and enactment?",
        "q_ta": "இந்திய அரசியலமைப்பின் முகவுரையில் அரசியலமைப்பு ஏற்றுக்கொள்ளப்பட்ட மற்றும் இயற்றப்பட்ட நாளாக வெளிப்படையாகக் குறிப்பிடப்பட்டுள்ள தேதி எது?",
        "opts": [
            {"id": "A", "en": "26th January 1950", "ta": "26 ஜனவரி 1950"},
            {"id": "B", "en": "15th August 1947", "ta": "15 ஆகஸ்ட் 1947"},
            {"id": "C", "en": "26th November 1949", "ta": "26 நவம்பர் 1949"},
            {"id": "D", "en": "9th December 1946", "ta": "9 டிசம்பர் 1946"}
        ],
        "exp_en": "The Preamble explicitly mentions 26th November 1949 as the date of adoption, enactment, and giving to ourselves the Constitution.",
        "exp_ta": "முகவுரை 26 நவம்பர் 1949 ஆம் தேதியை அரசியலமைப்பு ஏற்றுக்கொள்ளப்பட்ட மற்றும் இயற்றப்பட்ட நாளாக வெளிப்படையாகக் குறிப்பிடுகிறது."
    },

    # 2 (A) - Conceptual
    {
        "type": "Conceptual MCQ", "diff": "Easy", "ans": "A",
        "q_en": "The doctrine of 'Popular Sovereignty' in the Indian Constitution is explicitly reflected in which opening phrase of the Preamble?",
        "q_ta": "இந்திய அரசியலமைப்பில் 'மக்களின் இறையாண்மை' என்ற கோட்பாடு முகவுரையின் எந்தத் தொடக்கச் சொற்றொடரில் வெளிப்படையாகப் பிரதிபலிக்கிறது?",
        "opts": [
            {"id": "A", "en": "'We, the People of India'", "ta": "'இந்திய மக்களாகிய நாம்'"},
            {"id": "B", "en": "'Sovereign Socialist Secular'", "ta": "'இறையாண்மை சமதர்ம மதச்சார்பற்ற'"},
            {"id": "C", "en": "'In our Constituent Assembly'", "ta": "'நமது அரசியலமைப்பு நிர்ணய அவையில்'"},
            {"id": "D", "en": "'Give to ourselves this Constitution'", "ta": "'நமக்கு நாமே இந்த அரசியலமைப்பை வழங்கிக் கொள்கிறோம்'"}
        ],
        "exp_en": "The phrase 'We, the People of India' signifies Popular Sovereignty—that all authority of the Constitution is derived directly from the citizens of India.",
        "exp_ta": "'இந்திய மக்களாகிய நாம்' என்ற சொற்றொடர் மக்களின் இறையாண்மையைக் குறிக்கிறது; அரசியலமைப்பின் அனைத்து அதிகாரங்களும் இந்திய மக்களிடமிருந்தே பெறப்படுகின்றன."
    },

    # 3 (B) - Statement-Based
    {
        "type": "Statement-Based", "diff": "Medium", "ans": "B",
        "q_en": "Consider the following statements regarding the 42nd Constitutional Amendment Act of 1976:\n1. It inserted the words 'Socialist', 'Secular', and 'Integrity' into the Preamble.\n2. It substituted the phrase 'Unity of the Nation' with 'Unity and Integrity of the Nation'.\n3. It was enacted based on the recommendations of the Sarkaria Commission.\nWhich of the statements given above are CORRECT?",
        "q_ta": "1976 ஆம் ஆண்டின் 42வது அரசியலமைப்புத் திருத்தச் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் ஆராய்க:\n1. இது 'சமதர்ம', 'மதச்சார்பற்ற' மற்றும் 'ஒருமைப்பாடு' ஆகிய சொற்களை முகவுரையில் சேர்த்தது.\n2. இது 'நாட்டின் ஒற்றுமை' என்ற தொடருக்குப் பதிலாக 'நாட்டின் ஒற்றுமை மற்றும் ஒருமைப்பாடு' என மாற்றியது.\n3. இது சர்க்காரியா ஆணையத்தின் பரிந்துரைகளின் அடிப்படையில் இயற்றப்பட்டது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எவை சரியானவை?",
        "opts": [
            {"id": "A", "en": "1 and 3 only", "ta": "1 மற்றும் 3 மட்டுமே"},
            {"id": "B", "en": "1 and 2 only", "ta": "1 மற்றும் 2 மட்டுமே"},
            {"id": "C", "en": "2 and 3 only", "ta": "2 மற்றும் 3 மட்டுமே"},
            {"id": "D", "en": "1, 2 and 3", "ta": "1, 2 மற்றும் 3"}
        ],
        "exp_en": "Statements 1 and 2 are CORRECT. Statement 3 is INCORRECT because the 42nd Amendment was enacted based on the Swaran Singh Committee recommendations (1976), not Sarkaria Commission.",
        "exp_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது; ஏனெனில் 42வது திருத்தம் சர்க்காரியா ஆணையத்திற்குப் பதிலாக சுரன் சிங் குழுவின் பரிந்துரைகளின் அடிப்படையில் இயற்றப்பட்டது."
    },

    # 4 (D) - Hard Analytical
    {
        "type": "Hard Analytical", "diff": "Hard", "ans": "D",
        "q_en": "Which of the following correctly describes the constitutional boundary of Parliament's power to amend the Preamble under Article 368 as established in Kesavananda Bharati case (1973)?",
        "q_ta": "கேசவானந்த பாரதி வழக்கில் (1973) நிறுவப்பட்டபடி, உறுப்பு 368-ன் கீழ் முகவுரையைத் திருத்துவதற்கான நாடாளுமன்றத்தின் அதிகாரத்தின் அரசியலமைப்பு வரம்பை பின்வருவனவற்றில் எது சரியாக விவரிக்கிறது?",
        "opts": [
            {"id": "A", "en": "Parliament cannot amend the Preamble under any circumstances as it is not a part of the Constitution", "ta": "முகவுரை அரசியலமைப்பின் ஒரு பகுதி அல்ல என்பதால் நாடாளுமன்றம் எந்தச் சூழ்நிலையிலும் அதைத் திருத்த முடியாது"},
            {"id": "B", "en": "Parliament has absolute sovereign power to delete any word or provision from the Preamble without judicial review", "ta": "நீதிமன்ற ஆய்வின்றி முகவுரையிலிருந்து எந்தவொரு சொல்லையோ விதியையோ நீக்க நாடாளுமன்றத்திற்கு முழுமையான இறையாண்மை அதிகாரம் உள்ளது"},
            {"id": "C", "en": "Preamble can be amended only by a simple majority like ordinary legislation", "ta": "சாதாரணச் சட்டத்தைப் போல சாதாரண பெரும்பான்மையால் மட்டுமே முகவுரையைத் திருத்த முடியும்"},
            {"id": "D", "en": "Parliament can amend the Preamble under Article 368, provided the 'Basic Features' or basic structure contained in it are not damaged or destroyed", "ta": "முகவுரையில் உள்ள 'அடிப்படை அம்சங்கள்' அல்லது அடிப்படை கட்டமைப்பு சேதமடையாமலும் அழிக்கப்படாமலும் இருக்கும் வரம்பிற்கு உட்பட்டு நாடாளுமன்றம் உறுப்பு 368-ன் கீழ் முகவுரையைத் திருத்தலாம்"}
        ],
        "exp_en": "In Kesavananda Bharati (1973), the Supreme Court ruled that Parliament can amend the Preamble under Article 368, but cannot alter or destroy its Basic Features.",
        "exp_ta": "கேசவானந்த பாரதி வழக்கில் (1973), அடிப்படை அம்சங்கள் சேதமடையாத வரம்பிற்கு உட்பட்டு நாடாளுமன்றம் உறுப்பு 368-ன் கீழ் முகவுரையைத் திருத்தலாம் என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது."
    },

    # 5 (A) - Reasoning
    {
        "type": "Assertion & Reason", "diff": "Hard", "ans": "A",
        "q_en": "Assertion (A): India's continued membership of the Commonwealth of Nations does not compromise its constitutional sovereignty proclaimed in the Preamble.\nReason (R): Commonwealth membership is an extra-constitutional voluntary declaration that can be terminated at India's own free will.",
        "q_ta": "கூற்று (A): காமன்வெல்த் நாடுகளின் கூட்டமைப்பில் இந்தியா தொடர்ந்து உறுப்பினராக இருப்பது முகவுரையில் பிரகடனப்படுத்தப்பட்ட அதன் அரசியலமைப்பு இறையாண்மையைப் பாதிக்காது.\nகாரணம் (R): காமன்வெல்த் உறுப்பினர் நிலை என்பது அரசியலமைப்புக்கு அப்பாற்பட்ட ஒரு தன்னார்வப் பிரகடனமாகும், இது இந்தியாவின் சொந்த விருப்பத்தின் பேரில் ரத்து செய்யப்படலாம்.",
        "opts": [
            {"id": "A", "en": "Both A and R are true and R is the correct explanation of A", "ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்"},
            {"id": "B", "en": "Both A and R are true but R is NOT the correct explanation of A", "ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல"},
            {"id": "C", "en": "A is true but R is false", "ta": "A சரி, ஆனால் R தவறு"},
            {"id": "D", "en": "A is false but R is true", "ta": "A தவறு, ஆனால் R சரி"}
        ],
        "exp_en": "Both A and R are true, and R correctly explains A. India's association with the Commonwealth is voluntary and does not impair its external or internal sovereignty.",
        "exp_ta": "A மற்றும் R இரண்டும் சரி, R என்பது A விற்கு சரியான விளக்கமாகும். காமன்வெல்த் கூட்டமைப்புடனான இந்தியாவின் உறவு தன்னார்வமானது, அது இறையாண்மையைக் குறைக்காது."
    }
]

print(f"Base setup with {len(raw_gt_questions)} questions initialized.")
