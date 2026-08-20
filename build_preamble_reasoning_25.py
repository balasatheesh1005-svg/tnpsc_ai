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

questions = [
    # =========================================================================
    # Q1: PRE_AR_001 (Answer: A) - Popular Sovereignty
    # =========================================================================
    {
        "id": "PRE_AR_001",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Medium",
        "question_type": "Assertion & Reason",
        "question": {
            "en": "Assertion (A): The opening words of the Preamble, 'We, the People of India', declare that the ultimate sovereignty in India resides in the people.\nReason (R): The Constitution of India was framed and adopted by the Constituent Assembly acting on behalf of and in the name of the people of India, not granted by any foreign monarch or parliament.",
            "ta": "கூற்று (A): முகவுரையின் தொடக்க வார்த்தைகளான 'இந்திய மக்களாகிய நாம்' என்பது, இந்தியாவின் இறுதி இறையாண்மை மக்களிடமே உள்ளது என்பதை அறிவிக்கிறது.\nகாரணம் (R): இந்திய அரசியலமைப்பு எந்தவொரு வெளிநாட்டு மன்னராலோ அல்லது நாடாளுமன்றத்தாலோ வழங்கப்படாமல், இந்திய மக்களின் சார்பாகவும் அவர்களின் பெயரிலும் அரசியலமைப்பு நிர்ணய அவையால் உருவாக்கப்பட்டு ஏற்றுக்கொள்ளப்பட்டது."
        },
        "options": [
            {"id": "A", "en": "Both Assertion and Reason are true and Reason is the correct explanation of Assertion.", "ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்."},
            {"id": "B", "en": "Both Assertion and Reason are true but Reason is NOT the correct explanation.", "ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல."},
            {"id": "C", "en": "Assertion is true but Reason is false.", "ta": "A சரி, ஆனால் R தவறு."},
            {"id": "D", "en": "Assertion is false but Reason is true.", "ta": "A தவறு, ஆனால் R சரி."}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Both Assertion and Reason are true, and Reason is the correct explanation. The doctrine of Popular Sovereignty emphasizes that all constitutional authority originates from the people of India, who enacted the Constitution through their representatives in the Constituent Assembly.",
            "ta": "கூற்று A மற்றும் காரணம் R இரண்டும் சரி, மேலும் R என்பது A-விற்கு சரியான விளக்கம். மக்களின் இறையாண்மை கோட்பாடு என்பது அனைத்து அரசியலமைப்பு அதிகாரங்களும் இந்திய மக்களிடமிருந்தே தோன்றுகின்றன என்பதை வலியுறுத்துகிறது."
        },
        "why_not_others": {
            "A": {"en": "Correct. Both statements are true and Reason directly justifies the assertion of popular sovereignty.", "ta": "சரி. கூற்று மற்றும் காரணம் இரண்டும் உண்மை; R என்பது A-வின் நேரடி விளக்கம்."},
            "B": {"en": "Incorrect. Reason is the exact constitutional justification for Assertion.", "ta": "தவறு. காரணம் என்பது கூற்றிற்கான துல்லியமான அரசியலமைப்பு விளக்கம்."},
            "C": {"en": "Incorrect. Reason is factually and constitutionally true.", "ta": "தவறு. காரணம் வரலாற்று மற்றும் அரசியலமைப்பு ரீதியாக சரியானது."},
            "D": {"en": "Incorrect. Assertion is true as held by the Supreme Court.", "ta": "தவறு. உச்ச நீதிமன்றத் தீர்ப்புகளின்படி கூற்று சரியானது."}
        },
        "tnpsc_tip": {
            "en": "Popular Sovereignty is the fundamental bedrock of the Indian Constitution, deriving all power from the citizens rather than an external authority.",
            "ta": "மக்களின் இறையாண்மை என்பது இந்திய அரசியலமைப்பின் அடித்தளமாகும், இது வெளிப்புற அதிகாரத்திற்குப் பதிலாக குடிமக்களிடமிருந்தே அனைத்து அதிகாரங்களையும் பெறுகிறது."
        },
        "revision_fact": {
            "en": "The phrase 'We, the People' was inspired by the Preamble of the Constitution of the United States of America (1787).",
            "ta": "'மக்களாகிய நாம்' என்ற சொற்றொடர் அமெரிக்க அரசியலமைப்பின் (1787) முகவுரையிலிருந்து ஈர்க்கப்பட்டது."
        },
        "source_reference": ["M. Laxmikanth - Indian Polity", "DD Basu - Introduction to the Constitution of India"],
        "bloom_level": "Understand",
        "estimated_time_sec": 60,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "Popular Sovereignty", "We The People"],
        "question_en": "Assertion (A): The opening words of the Preamble, 'We, the People of India', declare that the ultimate sovereignty in India resides in the people.\nReason (R): The Constitution of India was framed and adopted by the Constituent Assembly acting on behalf of and in the name of the people of India, not granted by any foreign monarch or parliament.",
        "question_ta": "கூற்று (A): முகவுரையின் தொடக்க வார்த்தைகளான 'இந்திய மக்களாகிய நாம்' என்பது, இந்தியாவின் இறுதி இறையாண்மை மக்களிடமே உள்ளது என்பதை அறிவிக்கிறது.\nகாரணம் (R): இந்திய அரசியலமைப்பு எந்தவொரு வெளிநாட்டு மன்னராலோ அல்லது நாடாளுமன்றத்தாலோ வழங்கப்படாமல், இந்திய மக்களின் சார்பாகவும் அவர்களின் பெயரிலும் அரசியலமைப்பு நிர்ணய அவையால் உருவாக்கப்பட்டு ஏற்றுக்கொள்ளப்பட்டது.",
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
        "explanation_en": "Both Assertion and Reason are true, and Reason is the correct explanation. The doctrine of Popular Sovereignty emphasizes that all constitutional authority originates from the people of India, who enacted the Constitution through their representatives in the Constituent Assembly.",
        "explanation_ta": "கூற்று A மற்றும் காரணம் R இரண்டும் சரி, மேலும் R என்பது A-விற்கு சரியான விளக்கம். மக்களின் இறையாண்மை கோட்பாடு என்பது அனைத்து அரசியலமைப்பு அதிகாரங்களும் இந்திய மக்களிடமிருந்தே தோன்றுகின்றன என்பதை வலியுறுத்துகிறது."
    },

    # =========================================================================
    # Q2: PRE_AR_002 (Answer: A) - Sovereignty and External Relations
    # =========================================================================
    {
        "id": "PRE_AR_002",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Assertion & Reason",
        "question": {
            "en": "Assertion (A): India's continued membership of the Commonwealth of Nations and acceptance of the British Crown as the symbolic head of the association does not limit or compromise its constitutional sovereignty.\nReason (R): India's membership in the Commonwealth is an extra-constitutional voluntary declaration and can be terminated at any time at India's own free will.",
            "ta": "கூற்று (A): காமன்வெல்த் நாடுகளின் கூட்டமைப்பில் இந்தியா தொடர்ந்து உறுப்பினராக இருப்பதும், பிரிட்டிஷ் மன்னரை அமைப்பின் அடையாளத் தலைவராக ஏற்றுக்கொள்வதும் இந்தியாவின் அரசியலமைப்பு இறையாண்மையை எவ்வகையிலும் மட்டுப்படுத்தவோ பாதிக்கவோ இல்லை.\nகாரணம் (R): காமன்வெல்த்தில் இந்தியாவின் உறுப்பினர் நிலை என்பது அரசியலமைப்புக்கு அப்பாற்பட்ட ஒரு தன்னார்வப் பிரகடனமாகும், மேலும் இந்தியாவின் சொந்த விருப்பத்தின் பேரில் எப்போது வேண்டுமானாலும் இதை ரத்து செய்ய முடியும்."
        },
        "options": [
            {"id": "A", "en": "Both Assertion and Reason are true and Reason is the correct explanation of Assertion.", "ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்."},
            {"id": "B", "en": "Both Assertion and Reason are true but Reason is NOT the correct explanation.", "ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல."},
            {"id": "C", "en": "Assertion is true but Reason is false.", "ta": "A சரி, ஆனால் R தவறு."},
            {"id": "D", "en": "Assertion is false but Reason is true.", "ta": "A தவறு, ஆனால் R சரி."}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Both Assertion and Reason are true, and Reason correctly explains Assertion. India became a fully sovereign republic on January 26, 1950. Its association with the Commonwealth is entirely voluntary without any legal allegiance to the British Crown or impairment of external sovereignty.",
            "ta": "A மற்றும் R இரண்டும் சரி, R என்பது A விற்கு சரியான விளக்கமாகும். இந்தியா ஜனவரி 26, 1950 அன்று முழு இறையாண்மை கொண்ட குடியரசானது. காமன்வெல்த் கூட்டமைப்புடனான உறவு முற்றிலும் தன்னார்வமானது மற்றும் பிரிட்டிஷ் மகுடத்திற்கு சட்டபூர்வ விசுவாசம் இல்லாதது."
        },
        "why_not_others": {
            "A": {"en": "Correct. Both statements are true and Reason explains why sovereignty remains intact.", "ta": "சரி. இரண்டும் சரி மற்றும் காரணம் இறையாண்மை எவ்வாறு முழுமையாக உள்ளது என்பதை விளக்குகிறது."},
            "B": {"en": "Incorrect. Reason provides the direct logical ground for the Assertion.", "ta": "தவறு. காரணம் கூற்றிற்கான நேரடி தர்க்கரீதியான அடிப்படையை வழங்குகிறது."},
            "C": {"en": "Incorrect. Reason is true as declared by Jawaharlal Nehru in 1949.", "ta": "தவறு. 1949 இல் நேரு அறிவித்தபடி காரணம் சரியானது."},
            "D": {"en": "Incorrect. Assertion is true.", "ta": "தவறு. கூற்று சரியானது."}
        },
        "tnpsc_tip": {
            "en": "Neither Commonwealth membership nor United Nations membership curtails Indian sovereignty in any legal or constitutional manner.",
            "ta": "காமன்வெல்த் உறுப்பினர் அந்தஸ்தோ அல்லது ஐக்கிய நாடுகள் சபை உறுப்பினர் அந்தஸ்தோ இந்தியாவின் இறையாண்மையை எந்த வகையிலும் குறைக்காது."
        },
        "revision_fact": {
            "en": "Jawaharlal Nehru made the London Declaration in April 1949 affirming India's Commonwealth membership as a Sovereign Independent Republic.",
            "ta": "ஏப்ரல் 1949 இல் லண்டன் பிரகடனத்தின் மூலம் இந்தியா ஒரு இறையாண்மை கொண்ட குடியரசாக காமன்வெல்த்தில் நீடிக்கும் என ஜவஹர்லால் நேரு உறுதிப்படுத்தினார்."
        },
        "source_reference": ["M. Laxmikanth - Indian Polity", "Constituent Assembly Debates"],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "Sovereignty", "Commonwealth"],
        "question_en": "Assertion (A): India's continued membership of the Commonwealth of Nations and acceptance of the British Crown as the symbolic head of the association does not limit or compromise its constitutional sovereignty.\nReason (R): India's membership in the Commonwealth is an extra-constitutional voluntary declaration and can be terminated at any time at India's own free will.",
        "question_ta": "கூற்று (A): காமன்வெல்த் நாடுகளின் கூட்டமைப்பில் இந்தியா தொடர்ந்து உறுப்பினராக இருப்பதும், பிரிட்டிஷ் மன்னரை அமைப்பின் அடையாளத் தலைவராக ஏற்றுக்கொள்வதும் இந்தியாவின் அரசியலமைப்பு இறையாண்மையை எவ்வகையிலும் மட்டுப்படுத்தவோ பாதிக்கவோ இல்லை.\nகாரணம் (R): காமன்வெல்த்தில் இந்தியாவின் உறுப்பினர் நிலை என்பது அரசியலமைப்புக்கு அப்பாற்பட்ட ஒரு தன்னார்வப் பிரகடனமாகும், மேலும் இந்தியாவின் சொந்த விருப்பத்தின் பேரில் எப்போது வேண்டுமானாலும் இதை ரத்து செய்ய முடியும்.",
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
        "explanation_en": "Both Assertion and Reason are true, and Reason correctly explains Assertion. India became a fully sovereign republic on January 26, 1950. Its association with the Commonwealth is entirely voluntary without any legal allegiance to the British Crown or impairment of external sovereignty.",
        "explanation_ta": "A மற்றும் R இரண்டும் சரி, R என்பது A விற்கு சரியான விளக்கமாகும். இந்தியா ஜனவரி 26, 1950 அன்று முழு இறையாண்மை கொண்ட குடியரசானது. காமன்வெல்த் கூட்டமைப்புடனான உறவு முற்றிலும் தன்னார்வமானது மற்றும் பிரிட்டிஷ் மகுடத்திற்கு சட்டபூர்வ விசுவாசம் இல்லாதது."
    },

    # =========================================================================
    # Q3: PRE_AR_003 (Answer: A) - Democratic Socialism
    # =========================================================================
    {
        "id": "PRE_AR_003",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Medium",
        "question_type": "Assertion & Reason",
        "question": {
            "en": "Assertion (A): The Indian brand of socialism envisaged in the Constitution is 'Democratic Socialism' rather than 'Communistic/Marxist Socialism'.\nReason (R): Indian socialism believes in a mixed economy where both the public and private sectors co-exist side by side, aiming to eliminate poverty, ignorance, disease, and inequality of opportunity through democratic means.",
            "ta": "கூற்று (A): இந்திய அரசியலமைப்பில் உத்தேசிக்கப்பட்டுள்ள சமதர்மம் என்பது 'கம்யூனிச/மார்க்சிய சமதர்மம்' அல்லாமல் 'ஜனநாயக சமதர்மம்' ஆகும்.\nகாரணம் (R): இந்திய சமதர்மம் ஒரு கலப்புப் பொருளாதாரத்தை நம்புகிறது, இதில் பொதுத்துறை மற்றும் தனியார் துறை இரண்டும் அருகருகே இணைந்து செயல்படுகின்றன; மேலும் ஜனநாயக வழிகளில் வறுமை, அறியாமை, நோய் மற்றும் சமத்துவமின்மையை ஒழிப்பதை நோக்கமாகக் கொண்டுள்ளது."
        },
        "options": [
            {"id": "A", "en": "Both Assertion and Reason are true and Reason is the correct explanation of Assertion.", "ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்."},
            {"id": "B", "en": "Both Assertion and Reason are true but Reason is NOT the correct explanation.", "ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல."},
            {"id": "C", "en": "Assertion is true but Reason is false.", "ta": "A சரி, ஆனால் R தவறு."},
            {"id": "D", "en": "Assertion is false but Reason is true.", "ta": "A தவறு, ஆனால் R சரி."}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Both Assertion and Reason are true, and Reason correctly explains Assertion. In Excel Wear v. Union of India (1978) and D.S. Nakara v. Union of India (1983), the Supreme Court observed that Indian socialism is a blend of Marxism and Gandhism, leaning heavily towards Gandhian socialism, favoring a mixed economy rather than state monopolization.",
            "ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும். டி.எஸ். நகாரா வழக்கில் (1983) உச்ச நீதிமன்றம் இந்திய சமதர்மம் மார்க்சியம் மற்றும் காந்தியத்தின் கலவை என்றும், குறிப்பாக காந்திய சமதர்மத்தை நோக்கி அதிகம் சாய்ந்து கலப்புப் பொருளாதாரத்தை ஆதரிக்கிறது என்றும் தீர்ப்பளித்தது."
        },
        "why_not_others": {
            "A": {"en": "Correct. Both statements are true and Reason accurately defines Indian democratic socialism.", "ta": "சரி. இரண்டும் உண்மை மற்றும் காரணம் இந்திய ஜனநாயக சமதர்மத்தை துல்லியமாக வரையறுக்கிறது."},
            "B": {"en": "Incorrect. Reason explains the exact nature of Democratic Socialism in contrast to Communist Socialism.", "ta": "தவறு. கம்யூனிச சமதர்மத்திற்கு மாறாக ஜனநாயக சமதர்மத்தின் சரியான தன்மையை காரணம் விளக்குகிறது."},
            "C": {"en": "Incorrect. Reason is true.", "ta": "தவறு. காரணம் சரியானது."},
            "D": {"en": "Incorrect. Assertion is true.", "ta": "தவறு. கூற்று சரியானது."}
        },
        "tnpsc_tip": {
            "en": "Communistic socialism involves nationalisation of all means of production and abolition of private property. Democratic socialism holds faith in a mixed economy.",
            "ta": "கம்யூனிச சமதர்மம் அனைத்து உற்பத்தி வழிமுறைகளையும் அரசுடைமையாக்குதல் மற்றும் தனியார் சொத்துரிமையை ஒழிப்பதை உள்ளடக்கியது. ஜனநாயக சமதர்மம் கலப்பு பொருளாதாரத்தை நம்புகிறது."
        },
        "revision_fact": {
            "en": "The term 'Socialist' was added to the Preamble by the 42nd Constitutional Amendment Act, 1976.",
            "ta": "'சமதர்ம' என்ற சொல் 1976-ன் 42வது அரசியலமைப்புத் திருத்தச் சட்டத்தின் மூலம் முகவுரையில் சேர்க்கப்பட்டது."
        },
        "source_reference": ["M. Laxmikanth - Indian Polity", "D.S. Nakara Case (1983)"],
        "bloom_level": "Understand",
        "estimated_time_sec": 60,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "Socialism", "Democratic Socialism"],
        "question_en": "Assertion (A): The Indian brand of socialism envisaged in the Constitution is 'Democratic Socialism' rather than 'Communistic/Marxist Socialism'.\nReason (R): Indian socialism believes in a mixed economy where both the public and private sectors co-exist side by side, aiming to eliminate poverty, ignorance, disease, and inequality of opportunity through democratic means.",
        "question_ta": "கூற்று (A): இந்திய அரசியலமைப்பில் உத்தேசிக்கப்பட்டுள்ள சமதர்மம் என்பது 'கம்யூனிச/மார்க்சிய சமதர்மம்' அல்லாமல் 'ஜனநாயக சமதர்மம்' ஆகும்.\nகாரணம் (R): இந்திய சமதர்மம் ஒரு கலப்புப் பொருளாதாரத்தை நம்புகிறது, இதில் பொதுத்துறை மற்றும் தனியார் துறை இரண்டும் அருகருகே இணைந்து செயல்படுகின்றன; மேலும் ஜனநாயக வழிகளில் வறுமை, அறியாமை, நோய் மற்றும் சமத்துவமின்மையை ஒழிப்பதை நோக்கமாகக் கொண்டுள்ளது.",
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
        "explanation_en": "Both Assertion and Reason are true, and Reason correctly explains Assertion. In Excel Wear v. Union of India (1978) and D.S. Nakara v. Union of India (1983), the Supreme Court observed that Indian socialism is a blend of Marxism and Gandhism, leaning heavily towards Gandhian socialism, favoring a mixed economy rather than state monopolization.",
        "explanation_ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும். டி.எஸ். நகாரா வழக்கில் (1983) உச்ச நீதிமன்றம் இந்திய சமதர்மம் மார்க்சியம் மற்றும் காந்தியத்தின் கலவை என்றும், குறிப்பாக காந்திய சமதர்மத்தை நோக்கி அதிகம் சாய்ந்து கலப்புப் பொருளாதாரத்தை ஆதரிக்கிறது என்றும் தீர்ப்பளித்தது."
    },

    # =========================================================================
    # Q4: PRE_AR_004 (Answer: C) - Secularism Wall of Separation Trap
    # =========================================================================
    {
        "id": "PRE_AR_004",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Assertion & Reason",
        "question": {
            "en": "Assertion (A): The Constitution of India embodies the 'positive concept of secularism' rather than the Western negative concept of secularism.\nReason (R): The Indian State maintains an absolute wall of separation between religion and state, completely prohibiting any state support, aid, or regulatory intervention in religious institutions.",
            "ta": "கூற்று (A): இந்திய அரசியலமைப்பு மேற்கத்திய எதிர்மறை மதச்சார்பின்மை கருத்துக்கு மாறாக 'நேர்மறை மதச்சார்பின்மை' கருத்தை உள்ளடக்கியுள்ளது.\nகாரணம் (R): இந்திய அரசு மதம் மற்றும் அரசுக்கு இடையே முழுமையான பிரிப்புச் சுவரைப் பராமரிக்கிறது, மேலும் மத நிறுவனங்களுக்கு எந்தவொரு அரசு ஆதரவு, நிதி உதவி அல்லது ஒழுங்குமுறை தலையீட்டையும் முற்றிலும் தடை செய்கிறது."
        },
        "options": [
            {"id": "A", "en": "Both Assertion and Reason are true and Reason is the correct explanation of Assertion.", "ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்."},
            {"id": "B", "en": "Both Assertion and Reason are true but Reason is NOT the correct explanation.", "ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல."},
            {"id": "C", "en": "Assertion is true but Reason is false.", "ta": "A சரி, ஆனால் R தவறு."},
            {"id": "D", "en": "Assertion is false but Reason is true.", "ta": "A தவறு, ஆனால் R சரி."}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "Assertion is true because Indian secularism means equal respect and protection for all religions ('Sarva Dharma Sambhava'). Reason is FALSE because the Indian State does NOT follow rigid Western separation; it provides equal treatment, permits state aid to religious minority institutions (Art 30), and allows reformative state intervention (Art 25(2)(b)).",
            "ta": "கூற்று A சரி, ஏனெனில் இந்திய மதச்சார்பின்மை அனைத்து மதங்களுக்கும் சமமான மரியாதை மற்றும் பாதுகாப்பை ('சர்வ தர்ம சமபாவா') அளிக்கிறது. காரணம் R தவறு, ஏனெனில் இந்திய அரசு மதத்திலிருந்து முழுமையான கண்டிப்பான பிரிவினையைப் பின்பற்றுவதில்லை; சிறுபான்மை கல்வி நிறுவனங்களுக்கு அரசு உதவி பெற அனுமதிப்பதுடன் சமூக சீர்திருத்த தலையீடுகளையும் அனுமதிக்கிறது."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Reason (R) describes Western negative secularism, which is not followed in India.", "ta": "தவறு. காரணம் (R) மேற்கத்திய எதிர்மறை மதச்சார்பின்மையை விவரிக்கிறது, இது இந்தியாவில் பின்பற்றப்படவில்லை."},
            "B": {"en": "Incorrect. Reason is factually false.", "ta": "தவறு. காரணம் தவறானது."},
            "C": {"en": "Correct. Assertion is true; Reason is false.", "ta": "சரி. கூற்று A சரி; காரணம் R தவறு."},
            "D": {"en": "Incorrect. Assertion is true.", "ta": "தவறு. கூற்று சரியானது."}
        },
        "tnpsc_tip": {
            "en": "Western secularism = Strict separation of Church and State. Indian secularism = Equal status and support to all religions (Positive Secularism).",
            "ta": "மேற்கத்திய மதச்சார்பின்மை = மதம் மற்றும் அரசுக்கிடையே கடுமையான பிரிவினை. இந்திய மதச்சார்பின்மை = அனைத்து மதங்களுக்கும் சமமான மதிப்பும் ஆதரவும் (நேர்மறை மதச்சார்பின்மை)."
        },
        "revision_fact": {
            "en": "In S.R. Bommai v. Union of India (1994), the Supreme Court ruled that Secularism is a part of the 'Basic Structure' of the Indian Constitution.",
            "ta": "எஸ்.ஆர். பொம்மை வழக்கில் (1994) மதச்சார்பின்மை அரசியலமைப்பின் 'அடிப்படை கட்டமைப்பு' என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது."
        },
        "source_reference": ["M. Laxmikanth - Indian Polity", "S.R. Bommai Case (1994)"],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "Secularism", "Positive Secularism"],
        "question_en": "Assertion (A): The Constitution of India embodies the 'positive concept of secularism' rather than the Western negative concept of secularism.\nReason (R): The Indian State maintains an absolute wall of separation between religion and state, completely prohibiting any state support, aid, or regulatory intervention in religious institutions.",
        "question_ta": "கூற்று (A): இந்திய அரசியலமைப்பு மேற்கத்திய எதிர்மறை மதச்சார்பின்மை கருத்துக்கு மாறாக 'நேர்மறை மதச்சார்பின்மை' கருத்தை உள்ளடக்கியுள்ளது.\nகாரணம் (R): இந்திய அரசு மதம் மற்றும் அரசுக்கு இடையே முழுமையான பிரிப்புச் சுவரைப் பராமரிக்கிறது, மேலும் மத நிறுவனங்களுக்கு எந்தவொரு அரசு ஆதரவு, நிதி உதவி அல்லது ஒழுங்குமுறை தலையீட்டையும் முற்றிலும் தடை செய்கிறது.",
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
        "explanation_en": "Assertion is true because Indian secularism means equal respect and protection for all religions ('Sarva Dharma Sambhava'). Reason is FALSE because the Indian State does NOT follow rigid Western separation; it provides equal treatment, permits state aid to religious minority institutions (Art 30), and allows reformative state intervention (Art 25(2)(b)).",
        "explanation_ta": "கூற்று A சரி, ஏனெனில் இந்திய மதச்சார்பின்மை அனைத்து மதங்களுக்கும் சமமான மரியாதை மற்றும் பாதுகாப்பை ('சர்வ தர்ம சமபாவா') அளிக்கிறது. காரணம் R தவறு, ஏனெனில் இந்திய அரசு மதத்திலிருந்து முழுமையான கண்டிப்பான பிரிவினையைப் பின்பற்றுவதில்லை; சிறுபான்மை கல்வி நிறுவனங்களுக்கு அரசு உதவி பெற அனுமதிப்பதுடன் சமூக சீர்திருத்த தலையீடுகளையும் அனுமதிக்கிறது."
    },

    # =========================================================================
    # Q5: PRE_AR_005 (Answer: A) - Republic Definition
    # =========================================================================
    {
        "id": "PRE_AR_005",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Medium",
        "question_type": "Assertion & Reason",
        "question": {
            "en": "Assertion (A): India is designated as a 'Republic' in the Preamble, distinguishing it from constitutional monarchies like Great Britain.\nReason (R): In India, the Head of the State (President) is elected indirectly for a fixed term, and all public offices are open to every citizen without any discrimination.",
            "ta": "கூற்று (A): முகவுரையில் இந்தியா ஒரு 'குடியரசு' என்று குறிப்பிடப்பட்டுள்ளது, இது பிரிட்டன் போன்ற அரசியலமைப்பு முடியாட்சிகளிலிருந்து இந்தியாவை வேறுபடுத்துகிறது.\nகாரணம் (R): இந்தியாவில், நாட்டின் தலைவர் (குடியரசுத் தலைவர்) ஒரு குறிப்பிட்ட காலத்திற்கு மறைமுகமாகத் தேர்ந்தெடுக்கப்படுகிறார், மேலும் அனைத்து பொதுப் பதவிகளும் எந்தவொரு பாகுபாடுமின்றி ஒவ்வொரு குடிமகனுக்கும் திறக்கப்பட்டுள்ளன."
        },
        "options": [
            {"id": "A", "en": "Both Assertion and Reason are true and Reason is the correct explanation of Assertion.", "ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்."},
            {"id": "B", "en": "Both Assertion and Reason are true but Reason is NOT the correct explanation.", "ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல."},
            {"id": "C", "en": "Assertion is true but Reason is false.", "ta": "A சரி, ஆனால் R தவறு."},
            {"id": "D", "en": "Assertion is false but Reason is true.", "ta": "A தவறு, ஆனால் R சரி."}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Both Assertion and Reason are true, and Reason is the correct explanation. A republic means two things: vesting of political sovereignty in the people (no single hereditary monarch) and absence of any privileged class (all public offices open to all).",
            "ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும். குடியரசு என்பது இரு முக்கிய கூறுகளைக் குறிக்கிறது: அரசியல் இறையாண்மை மக்களிடம் இருப்பது (பரம்பரை மன்னர் இல்லாமை) மற்றும் சலுகை பெற்ற வர்க்கம் இல்லாமை (அனைத்து பொதுப்பதவிகளும் அனைவருக்கும் திறந்திருப்பது)."
        },
        "why_not_others": {
            "A": {"en": "Correct. Both A and R are true and R provides the foundational definition of Republic.", "ta": "சரி. A மற்றும் R இரண்டும் சரி; R குடியரசுக்கான அடிப்படை வரையறையை வழங்குகிறது."},
            "B": {"en": "Incorrect. Reason directly explains why India is defined as a Republic.", "ta": "தவறு. இந்தியா ஏன் குடியரசு என்று வரையறுக்கப்படுகிறது என்பதை காரணம் நேரடியாக விளக்குகிறது."},
            "C": {"en": "Incorrect. Reason is true.", "ta": "தவறு. காரணம் சரியானது."},
            "D": {"en": "Incorrect. Assertion is true.", "ta": "தவறு. கூற்று சரியானது."}
        },
        "tnpsc_tip": {
            "en": "In a Republic, the head of state is always elected (directly or indirectly) for a fixed period, unlike a Monarchy where the head of state holds a hereditary position.",
            "ta": "குடியரசில் நாட்டின் தலைவர் எப்போதும் ஒரு குறிப்பிட்ட காலத்திற்கு தேர்ந்தெடுக்கப்படுகிறார்; முடியாட்சியில் நாட்டின் தலைவர் பரம்பரை பதவியை வகிக்கிறார்."
        },
        "revision_fact": {
            "en": "The ideals of Republic, Liberty, Equality, and Fraternity in the Indian Preamble were borrowed from the French Revolution (1789-1799).",
            "ta": "இந்திய முகவுரையில் உள்ள குடியரசு, சுதந்திரம், சமத்துவம் மற்றும் சகோதரத்துவம் ஆகிய இலட்சியங்கள் பிரெஞ்சுப் புரட்சியிலிருந்து (1789-1799) பெறப்பட்டன."
        },
        "source_reference": ["M. Laxmikanth - Indian Polity", "NCERT Class XI - Indian Constitution at Work"],
        "bloom_level": "Understand",
        "estimated_time_sec": 60,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "Republic", "Democratic Republic"],
        "question_en": "Assertion (A): India is designated as a 'Republic' in the Preamble, distinguishing it from constitutional monarchies like Great Britain.\nReason (R): In India, the Head of the State (President) is elected indirectly for a fixed term, and all public offices are open to every citizen without any discrimination.",
        "question_ta": "கூற்று (A): முகவுரையில் இந்தியா ஒரு 'குடியரசு' என்று குறிப்பிடப்பட்டுள்ளது, இது பிரிட்டன் போன்ற அரசியலமைப்பு முடியாட்சிகளிலிருந்து இந்தியாவை வேறுபடுத்துகிறது.\nகாரணம் (R): இந்தியாவில், நாட்டின் தலைவர் (குடியரசுத் தலைவர்) ஒரு குறிப்பிட்ட காலத்திற்கு மறைமுகமாகத் தேர்ந்தெடுக்கப்படுகிறார், மேலும் அனைத்து பொதுப் பதவிகளும் எந்தவொரு பாகுபாடுமின்றி ஒவ்வொரு குடிமகனுக்கும் திறக்கப்பட்டுள்ளன.",
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
        "explanation_en": "Both Assertion and Reason are true, and Reason is the correct explanation. A republic means two things: vesting of political sovereignty in the people (no single hereditary monarch) and absence of any privileged class (all public offices open to all).",
        "explanation_ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும். குடியரசு என்பது இரு முக்கிய கூறுகளைக் குறிக்கிறது: அரசியல் இறையாண்மை மக்களிடம் இருப்பது (பரம்பரை மன்னர் இல்லாமை) மற்றும் சலுகை பெற்ற வர்க்கம் இல்லாமை (அனைத்து பொதுப்பதவிகளும் அனைவருக்கும் திறந்திருப்பது)."
    },

    # =========================================================================
    # Q6: PRE_AR_006 (Answer: B) - Distributive Justice and Historical Origin
    # =========================================================================
    {
        "id": "PRE_AR_006",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Medium",
        "question_type": "Assertion & Reason",
        "question": {
            "en": "Assertion (A): The Preamble secures 'Justice - Social, Economic and Political' to all citizens, where social justice and economic justice together constitute what is known as 'Distributive Justice'.\nReason (R): The ideal of justice—social, economic, and political—in the Indian Preamble was inspired by the Russian Revolution of 1917.",
            "ta": "கூற்று (A): முகவுரை அனைத்து குடிமக்களுக்கும் 'சமூக, பொருளாதார மற்றும் அரசியல் நீதியை' உறுதி செய்கிறது, இதில் சமூக நீதியும் பொருளாதார நீதியும் இணைந்து 'பகிர்வு நீதி' (Distributive Justice) என்று அழைக்கப்படுகிறது.\nகாரணம் (R): இந்திய முகவுரையில் உள்ள நீதி (சமூக, பொருளாதார, அரசியல்) என்ற உன்னத இலட்சியம் 1917 ஆம் ஆண்டின் ரஷ்யப் புரட்சியிலிருந்து ஈர்க்கப்பட்டது."
        },
        "options": [
            {"id": "A", "en": "Both Assertion and Reason are true and Reason is the correct explanation of Assertion.", "ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்."},
            {"id": "B", "en": "Both Assertion and Reason are true but Reason is NOT the correct explanation.", "ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல."},
            {"id": "C", "en": "Assertion is true but Reason is false.", "ta": "A சரி, ஆனால் R தவறு."},
            {"id": "D", "en": "Assertion is false but Reason is true.", "ta": "A தவறு, ஆனால் R சரி."}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "Both Assertion and Reason are true, but Reason is NOT the correct explanation of Assertion. Distributive justice means removing economic and social inequalities (a concept of welfare jurisprudence). While the ideal was indeed borrowed from the 1917 Russian Revolution, historical borrowing does not explain the internal legal concept of distributive justice.",
            "ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல. பகிர்வு நீதி என்பது சமூக மற்றும் பொருளாதார சமத்துவமின்மையை நீக்குவதைக் குறிக்கிறது. 1917 ரஷ்யப் புரட்சியிலிருந்து இந்த இலட்சியம் பெறப்பட்டது என்பது வரலாற்று உண்மையே தவிர, பகிர்வு நீதியின் சட்டபூர்வ விளக்கமல்ல."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Historical source of inspiration (Russian Revolution) does not explain the concept of distributive justice.", "ta": "தவறு. வரலாற்று தோற்றுவாய் (ரஷ்யப் புரட்சி) பகிர்வு நீதியின் தத்துவார்த்த விளக்கமாக அமையாது."},
            "B": {"en": "Correct. Both statements are factually true, but Reason is an independent historical fact.", "ta": "சரி. இரண்டு கூற்றுகளும் உண்மை, ஆனால் காரணம் ஒரு சுயாதீன வரலாற்று உண்மையாகும்."},
            "C": {"en": "Incorrect. Reason is true.", "ta": "தவறு. காரணம் சரியானது."},
            "D": {"en": "Incorrect. Assertion is true.", "ta": "தவறு. கூற்று சரியானது."}
        },
        "tnpsc_tip": {
            "en": "Distributive Justice = Social Justice + Economic Justice. (Article 38 & 39 of DPSP give practical effect to Distributive Justice).",
            "ta": "பகிர்வு நீதி = சமூக நீதி + பொருளாதார நீதி. (அரசு வழிகாட்டு நெறிமுறைகளின் உறுப்பு 38 மற்றும் 39 பகிர்வு நீதிக்கு நடைமுறை வடிவம் தருகின்றன)."
        },
        "revision_fact": {
            "en": "In Dr. Ambedkar's final speech in the Constituent Assembly (Nov 25, 1949), he warned that political democracy cannot survive without social democracy.",
            "ta": "அரசியலமைப்பு அவையில் டாக்டர் அம்பேத்கரின் இறுதி உரையில் (நவம்பர் 25, 1949), சமூக ஜனநாயகம் இன்றி அரசியல் ஜனநாயகம் நிலைக்க முடியாது என்று எச்சரித்தார்."
        },
        "source_reference": ["M. Laxmikanth - Indian Polity", "Constituent Assembly Debates"],
        "bloom_level": "Analyze",
        "estimated_time_sec": 65,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "Justice", "Distributive Justice"],
        "question_en": "Assertion (A): The Preamble secures 'Justice - Social, Economic and Political' to all citizens, where social justice and economic justice together constitute what is known as 'Distributive Justice'.\nReason (R): The ideal of justice—social, economic, and political—in the Indian Preamble was inspired by the Russian Revolution of 1917.",
        "question_ta": "கூற்று (A): முகவுரை அனைத்து குடிமக்களுக்கும் 'சமூக, பொருளாதார மற்றும் அரசியல் நீதியை' உறுதி செய்கிறது, இதில் சமூக நீதியும் பொருளாதார நீதியும் இணைந்து 'பகிர்வு நீதி' (Distributive Justice) என்று அழைக்கப்படுகிறது.\nகாரணம் (R): இந்திய முகவுரையில் உள்ள நீதி (சமூக, பொருளாதார, அரசியல்) என்ற உன்னத இலட்சியம் 1917 ஆம் ஆண்டின் ரஷ்யப் புரட்சியிலிருந்து ஈர்க்கப்பட்டது.",
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
        "explanation_en": "Both Assertion and Reason are true, but Reason is NOT the correct explanation of Assertion. Distributive justice means removing economic and social inequalities (a concept of welfare jurisprudence). While the ideal was indeed borrowed from the 1917 Russian Revolution, historical borrowing does not explain the internal legal concept of distributive justice.",
        "explanation_ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல. பகிர்வு நீதி என்பது சமூக மற்றும் பொருளாதார சமத்துவமின்மையை நீக்குவதைக் குறிக்கிறது. 1917 ரஷ்யப் புரட்சியிலிருந்து இந்த இலட்சியம் பெறப்பட்டது என்பது வரலாற்று உண்மையே தவிர, பகிர்வு நீதியின் சட்டபூர்வ விளக்கமல்ல."
    },

    # =========================================================================
    # Q7: PRE_AR_007 (Answer: B) - Liberty is Qualified, Not Absolute
    # =========================================================================
    {
        "id": "PRE_AR_007",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Assertion & Reason",
        "question": {
            "en": "Assertion (A): The 'Liberty of thought, expression, belief, faith and worship' secured by the Preamble is essential for the successful functioning of Indian democratic system.\nReason (R): The Fundamental Rights under Article 19 are not absolute and are subject to reasonable restrictions specified under Article 19(2) to 19(6).",
            "ta": "கூற்று (A): முகவுரையால் உறுதிசெய்யப்பட்ட 'எண்ணம், கருத்து வெளிப்பாடு, நம்பிக்கை, பக்தி மற்றும் வழிபாடு ஆகியவற்றின் சுதந்திரம்' இந்திய ஜனநாயக அமைப்பு வெற்றிகரமாகச் செயல்படுவதற்கு இன்றியமையாததாகும்.\nகாரணம் (R): உறுப்பு 19-ன் கீழான அடிப்படை உரிமைகள் வரம்பற்றவை அல்ல; அவை உறுப்பு 19(2) முதல் 19(6) வரை குறிப்பிடப்பட்டுள்ள நியாயமான கட்டுப்பாடுகளுக்கு உட்பட்டவை."
        },
        "options": [
            {"id": "A", "en": "Both Assertion and Reason are true and Reason is the correct explanation of Assertion.", "ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்."},
            {"id": "B", "en": "Both Assertion and Reason are true but Reason is NOT the correct explanation.", "ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல."},
            {"id": "C", "en": "Assertion is true but Reason is false.", "ta": "A சரி, ஆனால் R தவறு."},
            {"id": "D", "en": "Assertion is false but Reason is true.", "ta": "A தவறு, ஆனால் R சரி."}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "Both Assertion and Reason are true, but Reason is NOT the direct explanation of Assertion. Liberty is essential for individual development and democratic debate (Assertion). Reason correctly states the constitutional doctrine that liberty is qualified by reasonable restrictions, but it does not explain why liberty is indispensable to democratic functioning.",
            "ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல. தனிநபர் வளர்ச்சிக்கும் ஜனநாயக விவாதத்திற்கும் சுதந்திரம் இன்றியமையாதது (கூற்று). சுதந்திரம் நியாயமான கட்டுப்பாடுகளுக்கு உட்பட்டது என்ற அரசியலமைப்பு விதியை காரணம் கூறுகிறது, ஆனால் சுதந்திரம் ஏன் ஜனநாயகத்திற்கு முக்கியம் என்பதை அது விளக்கவில்லை."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Reason explains limitation on liberty, not the necessity of liberty for democracy.", "ta": "தவறு. காரணம் சுதந்திரத்தின் மீதான கட்டுப்பாடுகளை விளக்குகிறதே தவிர, ஜனநாயகத்திற்கான அதன் தேவையை விளக்கவில்லை."},
            "B": {"en": "Correct. Both statements are true, but Reason addresses restrictions rather than the democratic necessity stated in Assertion.", "ta": "சரி. இரண்டும் சரி, ஆனால் காரணம் கட்டுப்பாடுகளை விளக்குகிறது."},
            "C": {"en": "Incorrect. Reason is true under Article 19.", "ta": "தவறு. உறுப்பு 19-ன் கீழ் காரணம் சரியானது."},
            "D": {"en": "Incorrect. Assertion is true.", "ta": "தவறு. கூற்று சரியானது."}
        },
        "tnpsc_tip": {
            "en": "Liberty conceived by the Preamble or Fundamental Rights is NOT absolute but qualified. Liberty does not mean 'license' to do what one likes.",
            "ta": "முகவுரை அல்லது அடிப்படை உரிமைகளால் உத்தேசிக்கப்பட்ட சுதந்திரம் முழுமையானதல்ல (Absolute அல்ல), மாறாக தகுதிவாய்ந்தது (Qualified). சுதந்திரம் என்பது தன் விருப்பப்படி செயல்படும் 'வரம்பற்ற உரிமம்' அல்ல."
        },
        "revision_fact": {
            "en": "The Preamble secures 5 specific types of liberty: Thought, Expression, Belief, Faith, and Worship.",
            "ta": "முகவுரை 5 வகையான சுதந்திரங்களை உறுதி செய்கிறது: எண்ணம், கருத்து வெளிப்பாடு, நம்பிக்கை, பக்தி மற்றும் வழிபாடு."
        },
        "source_reference": ["M. Laxmikanth - Indian Polity", "Constitution of India - Article 19"],
        "bloom_level": "Analyze",
        "estimated_time_sec": 70,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "Liberty", "Article 19", "Reasonable Restrictions"],
        "question_en": "Assertion (A): The 'Liberty of thought, expression, belief, faith and worship' secured by the Preamble is essential for the successful functioning of Indian democratic system.\nReason (R): The Fundamental Rights under Article 19 are not absolute and are subject to reasonable restrictions specified under Article 19(2) to 19(6).",
        "question_ta": "கூற்று (A): முகவுரையால் உறுதிசெய்யப்பட்ட 'எண்ணம், கருத்து வெளிப்பாடு, நம்பிக்கை, பக்தி மற்றும் வழிபாடு ஆகியவற்றின் சுதந்திரம்' இந்திய ஜனநாயக அமைப்பு வெற்றிகரமாகச் செயல்படுவதற்கு இன்றியமையாததாகும்.\nகாரணம் (R): உறுப்பு 19-ன் கீழான அடிப்படை உரிமைகள் வரம்பற்றவை அல்ல; அவை உறுப்பு 19(2) முதல் 19(6) வரை குறிப்பிடப்பட்டுள்ள நியாயமான கட்டுப்பாடுகளுக்கு உட்பட்டவை.",
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
        "explanation_en": "Both Assertion and Reason are true, but Reason is NOT the direct explanation of Assertion. Liberty is essential for individual development and democratic debate (Assertion). Reason correctly states the constitutional doctrine that liberty is qualified by reasonable restrictions, but it does not explain why liberty is indispensable to democratic functioning.",
        "explanation_ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல. தனிநபர் வளர்ச்சிக்கும் ஜனநாயக விவாதத்திற்கும் சுதந்திரம் இன்றியமையாதது (கூற்று). சுதந்திரம் நியாயமான கட்டுப்பாடுகளுக்கு உட்பட்டது என்ற அரசியலமைப்பு விதியை காரணம் கூறுகிறது, ஆனால் சுதந்திரம் ஏன் ஜனநாயகத்திற்கு முக்கியம் என்பதை அது விளக்கவில்லை."
    },

    # =========================================================================
    # Q8: PRE_AR_008 (Answer: D) - Economic Liberty Trap
    # =========================================================================
    {
        "id": "PRE_AR_008",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Assertion & Reason",
        "question": {
            "en": "Assertion (A): The Preamble explicitly guarantees 'Economic Liberty' to all citizens to carry on any business, trade, or profession free from state economic regulations.\nReason (R): Article 19(1)(g) guarantees the right to practice any profession or to carry on any occupation, trade or business, subject to reasonable restrictions under Article 19(6).",
            "ta": "கூற்று (A): முகவுரை அனைத்து குடிமக்களுக்கும் அரசின் பொருளாதாரக் கட்டுப்பாடுகளிலிருந்து விடுபட்டு எந்தவொரு வணிகம், தொழில் அல்லது வியாபாரத்தையும் நடத்துவதற்கான 'பொருளாதார சுதந்திரத்தை' வெளிப்படையாக உத்தரவாதம் செய்கிறது.\nகாரணம் (R): உறுப்பு 19(1)(g) எந்தவொரு தொழிலையும் செய்ய அல்லது எந்தவொரு தொழில், வர்த்தகம் அல்லது வணிகத்தை மேற்கொள்வதற்கான உரிமையை உத்தரவாதம் செய்கிறது, இது உறுப்பு 19(6)-ன் கீழான நியாயமான கட்டுப்பாடுகளுக்கு உட்பட்டது."
        },
        "options": [
            {"id": "A", "en": "Both Assertion and Reason are true and Reason is the correct explanation of Assertion.", "ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்."},
            {"id": "B", "en": "Both Assertion and Reason are true but Reason is NOT the correct explanation.", "ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல."},
            {"id": "C", "en": "Assertion is true but Reason is false.", "ta": "A சரி, ஆனால் R தவறு."},
            {"id": "D", "en": "Assertion is false but Reason is true.", "ta": "A தவறு, ஆனால் R சரி."}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "Assertion is FALSE because the Preamble secures 'Economic Justice', NOT 'Economic Liberty'. The Preamble provides Liberty of Thought, Expression, Belief, Faith, and Worship only. Reason is TRUE because Article 19(1)(g) and 19(6) provide the qualified fundamental right to trade and occupation.",
            "ta": "கூற்று A தவறு; ஏனெனில் முகவுரை 'பொருளாதார நீதியை' வழங்குகிறதே தவிர 'பொருளாதார சுதந்திரத்தை' அல்ல. முகவுரை எண்ணம், கருத்து வெளிப்பாடு, நம்பிக்கை, பக்தி மற்றும் வழிபாடு ஆகிய 5 சுதந்திரங்களை மட்டுமே வழங்குகிறது. காரணம் R சரி, ஏனெனில் உறுப்பு 19(1)(g) மற்றும் 19(6) தொழிலுக்கான தகுதிவாய்ந்த அடிப்படை உரிமையை வழங்குகின்றன."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Assertion is false.", "ta": "தவறு. கூற்று தவறானது."},
            "B": {"en": "Incorrect. Assertion is false.", "ta": "தவறு. கூற்று தவறானது."},
            "C": {"en": "Incorrect. Assertion is false.", "ta": "தவறு. கூற்று தவறானது."},
            "D": {"en": "Correct. Assertion is false (Preamble gives Economic Justice, not Economic Liberty); Reason is true.", "ta": "சரி. கூற்று A தவறு (பொருளாதார நீதி உண்டு, பொருளாதார சுதந்திரம் முகவுரையில் இல்லை); காரணம் R சரி."}
        },
        "tnpsc_tip": {
            "en": "TNPSC Trap: Preamble has 'Economic Justice' and 'Equality of Opportunity', but NO 'Economic Liberty' or 'Religious Equality'.",
            "ta": "TNPSC பொறி: முகவுரையில் 'பொருளாதார நீதி' மற்றும் 'வாய்ப்பில் சமத்துவம்' உள்ளன; ஆனால் 'பொருளாதார சுதந்திரம்' அல்லது 'மதச் சமத்துவம்' என்ற வார்த்தைகள் இல்லை."
        },
        "revision_fact": {
            "en": "Justice is mentioned in 3 dimensions: Social, Economic, and Political. Liberty is mentioned in 5 dimensions: Thought, Expression, Belief, Faith, and Worship.",
            "ta": "நீதி 3 பரிமாணங்களில் (சமூக, பொருளாதார, அரசியல்) குறிப்பிடப்பட்டுள்ளது. சுதந்திரம் 5 பரிமாணங்களில் (எண்ணம், கருத்து வெளிப்பாடு, நம்பிக்கை, பக்தி, வழிபாடு) குறிப்பிடப்பட்டுள்ளது."
        },
        "source_reference": ["M. Laxmikanth - Indian Polity", "Text of the Preamble"],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "TNPSC Trap", "Economic Justice vs Economic Liberty"],
        "question_en": "Assertion (A): The Preamble explicitly guarantees 'Economic Liberty' to all citizens to carry on any business, trade, or profession free from state economic regulations.\nReason (R): Article 19(1)(g) guarantees the right to practice any profession or to carry on any occupation, trade or business, subject to reasonable restrictions under Article 19(6).",
        "question_ta": "கூற்று (A): முகவுரை அனைத்து குடிமக்களுக்கும் அரசின் பொருளாதாரக் கட்டுப்பாடுகளிலிருந்து விடுபட்டு எந்தவொரு வணிகம், தொழில் அல்லது வியாபாரத்தையும் நடத்துவதற்கான 'பொருளாதார சுதந்திரத்தை' வெளிப்படையாக உத்தரவாதம் செய்கிறது.\nகாரணம் (R): உறுப்பு 19(1)(g) எந்தவொரு தொழிலையும் செய்ய அல்லது எந்தவொரு தொழில், வர்த்தகம் அல்லது வணிகத்தை மேற்கொள்வதற்கான உரிமையை உத்தரவாதம் செய்கிறது, இது உறுப்பு 19(6)-ன் கீழான நியாயமான கட்டுப்பாடுகளுக்கு உட்பட்டது.",
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
        "explanation_en": "Assertion is FALSE because the Preamble secures 'Economic Justice', NOT 'Economic Liberty'. The Preamble provides Liberty of Thought, Expression, Belief, Faith, and Worship only. Reason is TRUE because Article 19(1)(g) and 19(6) provide the qualified fundamental right to trade and occupation.",
        "explanation_ta": "கூற்று A தவறு; ஏனெனில் முகவுரை 'பொருளாதார நீதியை' வழங்குகிறதே தவிர 'பொருளாதார சுதந்திரத்தை' அல்ல. முகவுரை எண்ணம், கருத்து வெளிப்பாடு, நம்பிக்கை, பக்தி மற்றும் வழிபாடு ஆகிய 5 சுதந்திரங்களை மட்டுமே வழங்குகிறது. காரணம் R சரி, ஏனெனில் உறுப்பு 19(1)(g) மற்றும் 19(6) தொழிலுக்கான தகுதிவாய்ந்த அடிப்படை உரிமையை வழங்குகின்றன."
    },

    # =========================================================================
    # Q9: PRE_AR_009 (Answer: B) - Fraternity and Integrity
    # =========================================================================
    {
        "id": "PRE_AR_009",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Medium",
        "question_type": "Assertion & Reason",
        "question": {
            "en": "Assertion (A): Fraternity in the Preamble assures two vital things: the dignity of the individual and the unity and integrity of the nation.\nReason (R): The word 'Integrity' was added to the Preamble by the 42nd Constitutional Amendment Act of 1976.",
            "ta": "கூற்று (A): முகவுரையில் உள்ள சகோதரத்துவம் இரண்டு முக்கிய விஷயங்களை உறுதி செய்கிறது: தனிநபரின் கண்ணியம் மற்றும் நாட்டின் ஒற்றுமை மற்றும் ஒருமைப்பாடு.\nகாரணம் (R): 1976 ஆம் ஆண்டின் 42வது அரசியலமைப்புத் திருத்தச் சட்டத்தின் மூலம் 'ஒருமைப்பாடு' (Integrity) என்ற சொல் முகவுரையில் சேர்க்கப்பட்டது."
        },
        "options": [
            {"id": "A", "en": "Both Assertion and Reason are true and Reason is the correct explanation of Assertion.", "ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்."},
            {"id": "B", "en": "Both Assertion and Reason are true but Reason is NOT the correct explanation.", "ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல."},
            {"id": "C", "en": "Assertion is true but Reason is false.", "ta": "A சரி, ஆனால் R தவறு."},
            {"id": "D", "en": "Assertion is false but Reason is true.", "ta": "A தவறு, ஆனால் R சரி."}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "Both Assertion and Reason are true, but Reason is NOT the direct logical explanation of Assertion. Fraternity promotes a sense of common brotherhood to ensure individual dignity and national unity. The fact that 'Integrity' was added in 1976 is an accurate historical event, but it does not explain why fraternity assures individual dignity.",
            "ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல. சகோதரத்துவம் என்பது பொதுவான சகோதரத்துவ உணர்வை வளர்த்து தனிநபர் கண்ணியத்தையும் தேசிய ஒற்றுமையையும் உறுதி செய்கிறது. 1976 இல் 'ஒருமைப்பாடு' சேர்க்கப்பட்டது ஒரு வரலாற்று உண்மையே தவிர, சகோதரத்துவத்தின் தத்துவார்த்த விளக்கமல்ல."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Amendment history does not explain the conceptual link between fraternity and individual dignity.", "ta": "தவறு. திருத்த வரலாறு சகோதரத்துவத்திற்கும் தனிநபர் கண்ணியத்திற்கும் இடையிலான கருத்தியல் இணைப்பை விளக்கவில்லை."},
            "B": {"en": "Correct. Both statements are true, and Reason is an independent historical fact.", "ta": "சரி. இரண்டும் உண்மை; காரணம் ஒரு வரலாற்று உண்மை."},
            "C": {"en": "Incorrect. Reason is true.", "ta": "தவறு. காரணம் சரியானது."},
            "D": {"en": "Incorrect. Assertion is true.", "ta": "தவறு. கூற்று சரியானது."}
        },
        "tnpsc_tip": {
            "en": "Originally, the Preamble contained 'Unity of the Nation'. The 42nd Amendment Act (1976) replaced it with 'Unity and Integrity of the Nation'.",
            "ta": "முதலில் முகவுரையில் 'நாட்டின் ஒற்றுமை' என்று மட்டுமே இருந்தது. 42வது திருத்தச் சட்டம் (1976) அதை 'நாட்டின் ஒற்றுமை மற்றும் ஒருமைப்பாடு' என்று மாற்றியது."
        },
        "revision_fact": {
            "en": "Article 51A(e) of Fundamental Duties explicitly directs every citizen to promote harmony and the spirit of common brotherhood (Fraternity).",
            "ta": "அடிப்படை கடமைகளின் உறுப்பு 51A(e) அனைத்து குடிமக்களும் நல்லிணக்கத்தையும் பொதுவான சகோதரத்துவ உணர்வையும் வளர்க்க வேண்டும் என்று வெளிப்படையாகக் கட்டளையிடுகிறது."
        },
        "source_reference": ["M. Laxmikanth - Indian Polity", "42nd Amendment Act 1976"],
        "bloom_level": "Understand",
        "estimated_time_sec": 60,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "Fraternity", "Integrity", "42nd Amendment"],
        "question_en": "Assertion (A): Fraternity in the Preamble assures two vital things: the dignity of the individual and the unity and integrity of the nation.\nReason (R): The word 'Integrity' was added to the Preamble by the 42nd Constitutional Amendment Act of 1976.",
        "question_ta": "கூற்று (A): முகவுரையில் உள்ள சகோதரத்துவம் இரண்டு முக்கிய விஷயங்களை உறுதி செய்கிறது: தனிநபரின் கண்ணியம் மற்றும் நாட்டின் ஒற்றுமை மற்றும் ஒருமைப்பாடு.\nகாரணம் (R): 1976 ஆம் ஆண்டின் 42வது அரசியலமைப்புத் திருத்தச் சட்டத்தின் மூலம் 'ஒருமைப்பாடு' (Integrity) என்ற சொல் முகவுரையில் சேர்க்கப்பட்டது.",
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
        "explanation_en": "Both Assertion and Reason are true, but Reason is NOT the direct logical explanation of Assertion. Fraternity promotes a sense of common brotherhood to ensure individual dignity and national unity. The fact that 'Integrity' was added in 1976 is an accurate historical event, but it does not explain why fraternity assures individual dignity.",
        "explanation_ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல. சகோதரத்துவம் என்பது பொதுவான சகோதரத்துவ உணர்வை வளர்த்து தனிநபர் கண்ணியத்தையும் தேசிய ஒற்றுமையையும் உறுதி செய்கிறது. 1976 இல் 'ஒருமைப்பாடு' சேர்க்கப்பட்டது ஒரு வரலாற்று உண்மையே தவிர, சகோதரத்துவத்தின் தத்துவார்த்த விளக்கமல்ல."
    },

    # =========================================================================
    # Q10: PRE_AR_010 (Answer: C) - Berubari Case Reasoning Error Trap
    # =========================================================================
    {
        "id": "PRE_AR_010",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Assertion & Reason",
        "question": {
            "en": "Assertion (A): In the Berubari Union Reference Case (1960), the Supreme Court opined that the Preamble is NOT a part of the Constitution.\nReason (R): The Supreme Court based this ruling on the fact that the Preamble was never debated, voted upon, or formally moved in the Constituent Assembly.",
            "ta": "கூற்று (A): பெருபாரி யூனியன் ஆலோசனைக் கருத்து வழக்கில் (1960), முகவுரை என்பது அரசியலமைப்பின் ஒரு பகுதி அல்ல என்று உச்ச நீதிமன்றம் கருத்து தெரிவித்தது.\nகாரணம் (R): அரசியலமைப்பு நிர்ணய அவையில் முகவுரை ஒருபோதும் விவாதிக்கப்படவோ, வாக்களிக்கப்படவோ அல்லது முறைப்படி முன்மொழியப்படவோ இல்லை என்ற உண்மையை அடிப்படையாகக் கொண்டு உச்ச நீதிமன்றம் இந்தத் தீர்ப்பை வழங்கியது."
        },
        "options": [
            {"id": "A", "en": "Both Assertion and Reason are true and Reason is the correct explanation of Assertion.", "ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்."},
            {"id": "B", "en": "Both Assertion and Reason are true but Reason is NOT the correct explanation.", "ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல."},
            {"id": "C", "en": "Assertion is true but Reason is false.", "ta": "A சரி, ஆனால் R தவறு."},
            {"id": "D", "en": "Assertion is false but Reason is true.", "ta": "A தவறு, ஆனால் R சரி."}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "Assertion is TRUE because the Supreme Court in Berubari (1960) held that the Preamble is a key to open the mind of the makers, but nevertheless not a part of the Constitution. Reason is FALSE because the Preamble WAS extensively debated, voted upon, and adopted by the Constituent Assembly under the motion 'that the Preamble stand part of the Constitution'.",
            "ta": "கூற்று A சரி; ஏனெனில் பெருபாரி (1960) வழக்கில் முகவுரை அரசியலமைப்பை உருவாக்கியவர்களின் மனதைத் திறக்கும் சாவி என்றாலும், அது அரசியலமைப்பின் ஒரு பகுதி அல்ல என்று உச்ச நீதிமன்றம் கூறியது. காரணம் R தவறு; ஏனெனில் அரசியலமைப்பு நிர்ணய அவையில் 'முகவுரை அரசியலமைப்பின் ஒரு பகுதியாக நிற்க வேண்டும்' என்ற பிரேரணையுடன் முகவுரை விரிவாக விவாதிக்கப்பட்டு, வாக்களிக்கப்பட்டு ஏற்றுக்கொள்ளப்பட்டது."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Reason is historically and procedurally false.", "ta": "தவறு. காரணம் வரலாற்று மற்றும் நடைமுறை ரீதியாக தவறானது."},
            "B": {"en": "Incorrect. Reason is false.", "ta": "தவறு. காரணம் தவறானது."},
            "C": {"en": "Correct. Assertion is true; Reason is completely false.", "ta": "சரி. கூற்று A சரி; காரணம் R முற்றிலும் தவறு."},
            "D": {"en": "Incorrect. Assertion is true.", "ta": "தவறு. கூற்று சரியானது."}
        },
        "tnpsc_tip": {
            "en": "Constituent Assembly President Dr. Rajendra Prasad specifically put the question: 'The question is that the Preamble stand part of the Constitution. The motion was adopted.'",
            "ta": "அரசியலமைப்பு அவையின் தலைவர் டாக்டர் ராஜேந்திர பிரசாத்: 'முகவுரை அரசியலமைப்பின் ஒரு பகுதியாக அமைய வேண்டும் என்பதே கேள்வி' எனக் கூறி பிரேரணையை முறைப்படி அவையில் நிறைவேற்றினார்."
        },
        "revision_fact": {
            "en": "The Berubari ruling (1960) was explicitly overturned by a 13-judge bench in Kesavananda Bharati v. State of Kerala (1973).",
            "ta": "பெருபாரி தீர்ப்பு (1960) கேசவானந்த பாரதி வழக்கில் (1973) 13 நீதிபதிகள் கொண்ட அமர்வால் வெளிப்படையாக ரத்து செய்யப்பட்டது."
        },
        "source_reference": ["In re Berubari Union Case (1960)", "M. Laxmikanth - Indian Polity"],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Preamble", "Berubari Union 1960", "Constituent Assembly Voting"],
        "question_en": "Assertion (A): In the Berubari Union Reference Case (1960), the Supreme Court opined that the Preamble is NOT a part of the Constitution.\nReason (R): The Supreme Court based this ruling on the fact that the Preamble was never debated, voted upon, or formally moved in the Constituent Assembly.",
        "question_ta": "கூற்று (A): பெருபாரி யூனியன் ஆலோசனைக் கருத்து வழக்கில் (1960), முகவுரை என்பது அரசியலமைப்பின் ஒரு பகுதி அல்ல என்று உச்ச நீதிமன்றம் கருத்து தெரிவித்தது.\nகாரணம் (R): அரசியலமைப்பு நிர்ணய அவையில் முகவுரை ஒருபோதும் விவாதிக்கப்படவோ, வாக்களிக்கப்படவோ அல்லது முறைப்படி முன்மொழியப்படவோ இல்லை என்ற உண்மையை அடிப்படையாகக் கொண்டு உச்ச நீதிமன்றம் இந்தத் தீர்ப்பை வழங்கியது.",
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
        "explanation_en": "Assertion is TRUE because the Supreme Court in Berubari (1960) held that the Preamble is a key to open the mind of the makers, but nevertheless not a part of the Constitution. Reason is FALSE because the Preamble WAS extensively debated, voted upon, and adopted by the Constituent Assembly under the motion 'that the Preamble stand part of the Constitution'.",
        "explanation_ta": "கூற்று A சரி; ஏனெனில் பெருபாரி (1960) வழக்கில் முகவுரை அரசியலமைப்பை உருவாக்கியவர்களின் மனதைத் திறக்கும் சாவி என்றாலும், அது அரசியலமைப்பின் ஒரு பகுதி அல்ல என்று உச்ச நீதிமன்றம் கூறியது. காரணம் R தவறு; ஏனெனில் அரசியலமைப்பு நிர்ணய அவையில் 'முகவுரை அரசியலமைப்பின் ஒரு பகுதியாக நிற்க வேண்டும்' என்ற பிரேரணையுடன் முகவுரை விரிவாக விவாதிக்கப்பட்டு, வாக்களிக்கப்பட்டு ஏற்றுக்கொள்ளப்பட்டது."
    }
]

print(f"Loaded questions up to Q10: {len(questions)}")
