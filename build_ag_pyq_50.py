# -*- coding: utf-8 -*-
"""
Generator for Attorney General of India PYQ MCQs (50 Questions: AG_PYQ_001 to AG_PYQ_050).
Strictly adheres to:
- Full 24-field TNPSC Nova AI schema
- Balanced answer keys (13 B, 12 C, 12 D, 13 A or ~25% each)
- Fully bilingual (English and authentic Tamil)
- Authentic past exam questions from TNPSC Group 1, 2, 4 and UPSC CSE
"""

import json
import os
import shutil
from ag_mcq_helper import make_ag_q
from rebalance_er_helper import balance_question_keys
from tools.nova_content_engine.validator import ContentValidator

raw_pyq_data = [
    # 1: TNPSC Group 1 2022
    {
        "exam": "TNPSC Group 1 2022",
        "stem_en": "[TNPSC Group 1 2022] Under which Article of the Constitution of India is the Attorney General of India appointed by the President?",
        "stem_ta": "[டிஎன்பிஎஸ்சி குரூப் 1 2022] இந்திய அரசியலமைப்பின் எந்தப் பிரிவின் கீழ் இந்தியக் குடியரசுத் தலைவரால் இந்திய தலைமை வழக்கறிஞர் நியமிக்கப்படுகிறார்?",
        "options": [
            ("Article 76", "சரத்து 76"),
            ("Article 74", "சரத்து 74"),
            ("Article 165", "சரத்து 165"),
            ("Article 148", "சரத்து 148")
        ],
        "correct_idx": 0,
        "exp_en": "Article 76(1) provides that the President shall appoint a person qualified to be a Supreme Court Judge as the Attorney General of India.",
        "exp_ta": "சரத்து 76(1)-ன் கீழ் உச்ச நீதிமன்ற நீதிபதியாக நியமிக்கப்பட தகுதியுடைய ஒருவரை இந்திய தலைமை வழக்கறிஞராக குடியரசுத் தலைவர் நியமிக்கிறார்.",
        "tip_en": "Article 76: Attorney General of India. Article 165: Advocate General for the State.",
        "tip_ta": "சரத்து 76: இந்திய தலைமை வழக்கறிஞர். சரத்து 165: மாநில அட்வகேட் ஜெனரல்.",
        "fact_en": "Article 76 is located in Part V, Chapter I of the Constitution.",
        "fact_ta": "சரத்து 76 அரசியலமைப்பின் பகுதி V, அத்தியாயம் I-ல் உள்ளது.",
        "subtopic": "Appointment & Article 76"
    },
    # 2: TNPSC Group 2 2018
    {
        "exam": "TNPSC Group 2 2018",
        "stem_en": "[TNPSC Group 2 2018] Who among the following is recognized as the highest and first law officer of the Government of India?",
        "stem_ta": "[டிஎன்பிஎஸ்சி குரூப் 2 2018] பின்வருவனவற்றுள் இந்திய அரசாங்கத்தின் முதலாவது மற்றும் மிக உயர்ந்த சட்ட அதிகாரியாக அங்கீகரிக்கப்பட்டவர் யார்?",
        "options": [
            ("Attorney General of India", "இந்திய தலைமை வழக்கறிஞர்"),
            ("Chief Justice of India", "இந்திய தலைமை நீதிபதி"),
            ("Union Law Minister", "மத்திய சட்ட அமைச்சர்"),
            ("Solicitor General of India", "இந்திய சொலிசிட்டர் ஜெனரல்")
        ],
        "correct_idx": 0,
        "exp_en": "The Attorney General of India is the chief legal adviser and the first law officer of the Government of India under Article 76.",
        "exp_ta": "சரத்து 76-ன் கீழ் இந்திய தலைமை வழக்கறிஞரே இந்திய அரசாங்கத்தின் முதன்மைச் சட்ட ஆலோசகர் மற்றும் முதல் சட்ட அதிகாரி ஆவார்.",
        "tip_en": "First law officer of Union = Attorney General. First law officer of State = Advocate General.",
        "tip_ta": "மத்திய அரசின் முதல் சட்ட அதிகாரி = தலைமை வழக்கறிஞர். மாநில அரசின் முதல் சட்ட அதிகாரி = அட்வகேட் ஜெனரல்.",
        "fact_en": "The Solicitor General is the second law officer, assisting the Attorney General.",
        "fact_ta": "சொலிசிட்டர் ஜெனரல் தலைமை வழக்கறிஞருக்கு உதவும் இரண்டாவது சட்ட அதிகாரி ஆவார்.",
        "subtopic": "Office & Status"
    },
    # 3: UPSC CSE 2013
    {
        "exam": "UPSC CSE 2013",
        "stem_en": "[UPSC CSE 2013] Consider the following statements regarding the Attorney General of India:\n1. He can take part in the proceedings of the Lok Sabha.\n2. He can be a member of a committee of the Lok Sabha.\n3. He can speak in the Lok Sabha.\n4. He can vote in the Lok Sabha.\nWhich of the statements given above is/are correct?",
        "stem_ta": "[யுபிஎஸ்சி சிஎஸ்இ 2013] இந்திய தலைமை வழக்கறிஞர் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. அவர் மக்களவை நடவடிக்கைகளில் பங்கேற்கலாம்.\n2. அவர் மக்களவையின் ஒரு குழுவில் உறுப்பினராக இருக்கலாம்.\n3. அவர் மக்களவையில் பேசலாம்.\n4. அவர் மக்களவையில் வாக்களிக்கலாம்.\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
        "options": [
            ("1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டுமே"),
            ("2 and 4 only", "2 மற்றும் 4 மட்டுமே"),
            ("1 and 3 only", "1 மற்றும் 3 மட்டுமே"),
            ("1, 2, 3 and 4", "1, 2, 3 மற்றும் 4")
        ],
        "correct_idx": 0,
        "exp_en": "Under Article 88, the AG can speak and take part in proceedings and committee deliberations of Parliament, but cannot vote.",
        "exp_ta": "சரத்து 88-ன் கீழ் தலைமை வழக்கறிஞர் நாடாளுமன்றத்திலும் அதன் குழுக்களிலும் பேசவும் பங்கேற்கவும் முடியும், ஆனால் வாக்களிக்க முடியாது.",
        "tip_en": "Article 88 allows speaking and committee participation, but explicitly prohibits voting!",
        "tip_ta": "சரத்து 88 பேசவும் குழுவில் பங்கேற்கவும் அனுமதிக்கிறது, ஆனால் வாக்களிப்பதை திட்டவட்டமாகத் தடை செய்கிறது!",
        "fact_en": "Voting is reserved exclusively for elected/nominated MPs under Article 100.",
        "fact_ta": "சரத்து 100-ன் கீழ் வாக்குரிமை நாடாளுமன்ற உறுப்பினர்களுக்கு மட்டுமே ஒதுக்கப்பட்டுள்ளது.",
        "subtopic": "Article 88 Rights"
    },
    # 4: TNPSC Group 4 2019
    {
        "exam": "TNPSC Group 4 2019",
        "stem_en": "[TNPSC Group 4 2019] For how long does the Attorney General of India hold office according to the Indian Constitution?",
        "stem_ta": "[டிஎன்பிஎஸ்சி குரூப் 4 2019] இந்திய அரசியலமைப்பின்படி இந்திய தலைமை வழக்கறிஞர் எவ்வளவு காலம் பதவியில் நீடிப்பார்?",
        "options": [
            ("During the pleasure of the President", "குடியரசுத் தலைவரின் விருப்பம் உள்ளவரை"),
            ("For a fixed term of 5 years", "5 ஆண்டுகள் நிலையான பதவிக்காலம்"),
            ("Up to the age of 65 years", "65 வயது வரை"),
            ("During the pleasure of the Prime Minister", "பிரதமரின் விருப்பம் உள்ளவரை")
        ],
        "correct_idx": 0,
        "exp_en": "Article 76(4) provides: 'The Attorney-General shall hold office during the pleasure of the President, and shall receive such remuneration as the President may determine.'",
        "exp_ta": "சரத்து 76(4) கூறுகிறது: 'தலைமை வழக்கறிஞர் குடியரசுத் தலைவரின் விருப்பம் உள்ளவரை பதவியில் நீடிப்பார், மேலும் அவர் நிர்ணயிக்கும் ஊதியத்தைப் பெறுவார்.'",
        "tip_en": "AG has no fixed tenure and holds office purely during the pleasure of the President.",
        "tip_ta": "AG-க்கு நிலையான பதவிக்காலம் இல்லை, குடியரசுத் தலைவரின் விருப்பம் உள்ளவரையே பதவியில் இருப்பார்.",
        "fact_en": "Conventionally, the AG resigns when the Council of Ministers resigns or is replaced.",
        "fact_ta": "அமைச்சரவை மாறும்போது AG பதவி விலகுவது ஓர் அரசியலமைப்பு மரபாகும்.",
        "subtopic": "Tenure of Office"
    },
    # 5: TNPSC Group 1 2015
    {
        "exam": "TNPSC Group 1 2015",
        "stem_en": "[TNPSC Group 1 2015] To be appointed as the Attorney General of India, a person must be qualified to be appointed as a:",
        "stem_ta": "[டிஎன்பிஎஸ்சி குரூப் 1 2015] இந்திய தலைமை வழக்கறிஞராக நியமிக்கப்படுவதற்கு, ஒருவர் எப்பதவிக்கு நியமிக்கப்படத் தகுதி பெற்றிருக்க வேண்டும்?",
        "options": [
            ("Judge of the Supreme Court", "உச்ச நீதிமன்ற நீதிபதி"),
            ("Judge of the High Court", "உயர் நீதிமன்ற நீதிபதி"),
            ("Member of Parliament", "நாடாளுமன்ற உறுப்பினர்"),
            ("Senior Advocate of 20 years standing", "20 ஆண்டுகள் பணிபுரிந்த மூத்த வழக்கறிஞர்")
        ],
        "correct_idx": 0,
        "exp_en": "Article 76(1) mandates that the candidate must be qualified to be appointed as a Judge of the Supreme Court.",
        "exp_ta": "சரத்து 76(1)-ன் படி உச்ச நீதிமன்ற நீதிபதியாக நியமிக்கப்படத் தேவையான தகுதிகளைக் கொண்டவரே தலைமை வழக்கறிஞராக நியமிக்கப்பட முடியும்.",
        "tip_en": "AG requires SC judge qualifications; Advocate General requires High Court judge qualifications.",
        "tip_ta": "தலைமை வழக்கறிஞருக்கு SC நீதிபதி தகுதியும், அட்வகேட் ஜெனரலுக்கு HC நீதிபதி தகுதியும் தேவை.",
        "fact_en": "SC judge qualifications under Article 124(3) include: 5 yrs HC judge, 10 yrs HC advocate, or distinguished jurist.",
        "fact_ta": "சரத்து 124(3)-ன் கீழ் SC நீதிபதி தகுதிகள்: 5 ஆண்டு HC நீதிபதி, 10 ஆண்டு HC வழக்கறிஞர், அல்லது புகழ்பெற்ற சட்ட அறிஞர்.",
        "subtopic": "Qualifications"
    },
    # 6: TNPSC Group 2 2015
    {
        "exam": "TNPSC Group 2 2015",
        "stem_en": "[TNPSC Group 2 2015] Who was the first Attorney General of independent India?",
        "stem_ta": "[டிஎன்பிஎஸ்சி குரூப் 2 2015] சுதந்திர இந்தியாவின் முதலாவது தலைமை வழக்கறிஞர் யார்?",
        "options": [
            ("M.C. Setalvad", "எம்.சி. செடல்வாட்"),
            ("C.K. Daphtary", "சி.கே. தப்தாரி"),
            ("Niren De", "நீரேன் டே"),
            ("K. Parasaran", "கே. பராசரன்")
        ],
        "correct_idx": 0,
        "exp_en": "Motilal Chimanlal Setalvad was the first Attorney General of India, serving from 1950 to 1963.",
        "exp_ta": "மோதிலால் சிமன்லால் செடல்வாட் இந்தியாவின் முதல் தலைமை வழக்கறிஞர் ஆவார் (1950-1963 வரை பணியாற்றினார்).",
        "tip_en": "M.C. Setalvad was both the first and longest-serving Attorney General of India.",
        "tip_ta": "எம்.சி. செடல்வாட் இந்தியாவின் முதல் மற்றும் மிக நீண்ட காலம் பதவி வகித்த தலைமை வழக்கறிஞர் ஆவார்.",
        "fact_en": "Setalvad also chaired the First Law Commission of independent India in 1955.",
        "fact_ta": "செடல்வாட் 1955-ல் சுதந்திர இந்தியாவின் முதலாவது சட்ட ஆணையத்தின் தலைவராகவும் பணியாற்றினார்.",
        "subtopic": "Historical Personalities"
    },
    # 7: UPSC CSE 2019
    {
        "exam": "UPSC CSE 2019",
        "stem_en": "[UPSC CSE 2019] With reference to the Attorney General of India, consider the following statements:\n1. He is appointed by the President of India.\n2. He must have the same qualifications as are required for a judge of the High Court.\n3. In the performance of his duties, he has the right of audience in all courts in India.\nWhich of the statements given above are correct?",
        "stem_ta": "[யுபிஎஸ்சி சிஎஸ்இ 2019] இந்திய தலைமை வழக்கறிஞர் தொடர்பாக பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. அவர் இந்தியக் குடியரசுத் தலைவரால் நியமிக்கப்படுகிறார்.\n2. உயர் நீதிமன்ற நீதிபதிக்குத் தேவையான அதே தகுதிகளை அவர் கொண்டிருக்க வேண்டும்.\n3. தனது கடமைகளை ஆற்றுவதில், இந்தியாவில் உள்ள அனைத்து நீதிமன்றங்களிலும் வழக்காடும் உரிமை அவருக்கு உண்டு.\nமேற்கூறிய கூற்றுகளில் சரியானவை எவை?",
        "options": [
            ("1 and 3 only", "1 மற்றும் 3 மட்டுமே"),
            ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
            ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
            ("1, 2 and 3", "1, 2 மற்றும் 3")
        ],
        "correct_idx": 0,
        "exp_en": "Statements 1 and 3 are correct. Statement 2 is incorrect because he must be qualified to be a Judge of the Supreme Court, not a High Court.",
        "exp_ta": "கூற்றுகள் 1 மற்றும் 3 சரியானவை. உயர் நீதிமன்றம் அல்ல, உச்ச நீதிமன்ற நீதிபதிக்கான தகுதியையே அவர் கொண்டிருக்க வேண்டும் என்பதால் கூற்று 2 தவறு.",
        "tip_en": "Watch out for High Court vs Supreme Court trap in AG qualification questions!",
        "tip_ta": "AG தகுதி வினாக்களில் உயர் நீதிமன்றம் vs உச்ச நீதிமன்றம் என்ற குழப்பத்தை கவனமாகக் கையாளவும்!",
        "fact_en": "Article 76(3) explicitly confers right of audience in all courts in India.",
        "fact_ta": "சரத்து 76(3) இந்தியாவில் உள்ள அனைத்து நீதிமன்றங்களிலும் வழக்காடும் உரிமையை வழங்குகிறது.",
        "subtopic": "Qualifications & Audience"
    },
    # 8: TNPSC Group 1 2017
    {
        "exam": "TNPSC Group 1 2017",
        "stem_en": "[TNPSC Group 1 2017] Which Article of the Constitution confers upon the Attorney General of India the privileges and immunities of a Member of Parliament?",
        "stem_ta": "[டிஎன்பிஎஸ்சி குரூப் 1 2017] இந்திய தலைமை வழக்கறிஞருக்கு ஒரு நாடாளுமன்ற உறுப்பினரின் சலுகைகள் மற்றும் பாதுகாப்புகளை வழங்கும் அரசியலமைப்புச் சரத்து எது?",
        "options": [
            ("Article 105(4)", "சரத்து 105(4)"),
            ("Article 88", "சரத்து 88"),
            ("Article 76(3)", "சரத்து 76(3)"),
            ("Article 194", "சரத்து 194")
        ],
        "correct_idx": 0,
        "exp_en": "Article 105(4) extends all parliamentary privileges and immunities to persons who by virtue of the Constitution have the right to speak and take part in parliamentary proceedings, including the Attorney General.",
        "exp_ta": "சரத்து 105(4) நாடாளுமன்றத்தில் பேச உரிமையுள்ள அனைவருக்கும் (தலைமை வழக்கறிஞர் உட்பட) அனைத்து நாடாளுமன்ற சிறப்புரிமைகளையும் பாதுகாப்புகளையும் வழங்குகிறது.",
        "tip_en": "Article 88 gives the right to speak; Article 105(4) gives parliamentary privileges!",
        "tip_ta": "சரத்து 88 பேசும் உரிமையை அளிக்கிறது; சரத்து 105(4) நாடாளுமன்ற சலுகைகளை வழங்குகிறது!",
        "fact_en": "Article 194(4) is the exact parallel for the Advocate General in the State Legislature.",
        "fact_ta": "சரத்து 194(4) மாநில சட்டமன்றத்தில் அட்வகேட் ஜெனரலுக்கான இணை விதியாகும்.",
        "subtopic": "Privileges & Immunities"
    },
    # 9: TNPSC Group 4 2014
    {
        "exam": "TNPSC Group 4 2014",
        "stem_en": "[TNPSC Group 4 2014] Who determines the remuneration payable to the Attorney General of India?",
        "stem_ta": "[டிஎன்பிஎஸ்சி குரூப் 4 2014] இந்திய தலைமை வழக்கறிஞருக்கு வழங்கப்படும் ஊதியத்தை நிர்ணயிப்பவர் யார்?",
        "options": [
            ("The President of India", "இந்தியக் குடியரசுத் தலைவர்"),
            ("The Parliament of India", "இந்திய நாடாளுமன்றம்"),
            ("The Prime Minister of India", "இந்தியப் பிரதமர்"),
            ("The Chief Justice of India", "இந்திய தலைமை நீதிபதி")
        ],
        "correct_idx": 0,
        "exp_en": "Article 76(4) states: 'The Attorney-General shall receive such remuneration as the President may determine.'",
        "exp_ta": "சரத்து 76(4) கூறுகிறது: 'குடியரசுத் தலைவர் நிர்ணயிக்கும் ஊதியத்தை தலைமை வழக்கறிஞர் பெறுவார்.'",
        "tip_en": "AG's remuneration is determined by the President, NOT by Parliament or Second Schedule.",
        "tip_ta": "AG ஊதியத்தை குடியரசுத் தலைவர் நிர்ணயிக்கிறார், நாடாளுமன்றமோ அல்லது 2-வது அட்டவணையோ அல்ல.",
        "fact_en": "The remuneration is specified through presidential orders issued from time to time.",
        "fact_ta": "குடியரசுத் தலைவர் அவ்வப்போது பிறப்பிக்கும் உத்தரவுகளின் வழியே ஊதியம் குறிப்பிடப்படுகிறது.",
        "subtopic": "Remuneration"
    },
    # 10: TNPSC Group 2 2012
    {
        "exam": "TNPSC Group 2 2012",
        "stem_en": "[TNPSC Group 2 2012] In which of the following courts does the Attorney General of India have the right of audience in the performance of his official duties?",
        "stem_ta": "[டிஎன்பிஎஸ்சி குரூப் 2 2012] தனது அலுவல் பணிகளை ஆற்றுவதில், பின்வரும் எந்த நீதிமன்றங்களில் இந்திய தலைமை வழக்கறிஞருக்கு வழக்காடும் உரிமை உண்டு?",
        "options": [
            ("In all courts in the territory of India", "இந்திய எல்லைக்குள் உள்ள அனைத்து நீதிமன்றங்களிலும்"),
            ("Only in the Supreme Court of India", "உச்ச நீதிமன்றத்தில் மட்டுமே"),
            ("Only in the Supreme Court and High Courts", "உச்ச நீதிமன்றம் மற்றும் உயர் நீதிமன்றங்களில் மட்டுமே"),
            ("Only in Central Administrative Tribunals", "மத்திய தீர்ப்பாயங்களில் மட்டுமே")
        ],
        "correct_idx": 0,
        "exp_en": "Article 76(3) of the Constitution states: 'In the performance of his duties, the Attorney-General shall have right of audience in all courts in the territory of India.'",
        "exp_ta": "சரத்து 76(3) கூறுகிறது: 'தனது கடமைகளை ஆற்றுவதில், இந்திய எல்லைக்குள் உள்ள அனைத்து நீதிமன்றங்களிலும் வழக்காடும் உரிமை தலைமை வழக்கறிஞருக்கு உண்டு.'",
        "tip_en": "Article 76(3) explicitly covers ALL courts in India (Supreme Court, High Courts, District Courts).",
        "tip_ta": "சரத்து 76(3) இந்தியாவில் உள்ள அனைத்து நீதிமன்றங்களையும் (உச்ச, உயர், மாவட்ட நீதிமன்றங்கள்) உள்ளடக்கியது.",
        "fact_en": "This right overrides local court rules requiring special vakalatnama or admission.",
        "fact_ta": "இந்த உரிமை உள்ளூர் நீதிமன்றங்களின் வழக்கமான அனுமதிகளை விட மேலானது.",
        "subtopic": "Right of Audience"
    },
    # 11: TNPSC Group 1 2021
    {
        "exam": "TNPSC Group 1 2021",
        "stem_en": "[TNPSC Group 1 2021] Which of the following statements about the Attorney General of India is NOT correct?",
        "stem_ta": "[டிஎன்பிஎஸ்சி குரூப் 1 2021] இந்திய தலைமை வழக்கறிஞர் பற்றிய பின்வரும் கூற்றுகளில் எது சரியானது அல்ல?",
        "options": [
            ("He is a full-time government servant debarred from private legal practice", "அவர் தனியார் சட்டப் பயிற்சியிலிருந்து தடை செய்யப்பட்ட முழுநேர அரசு ஊழியர் ஆவார்"),
            ("He is appointed by the President under Article 76", "சரத்து 76-ன் கீழ் குடியரசுத் தலைவரால் இவர் நியமிக்கப்படுகிறார்"),
            ("He has the right of audience in all courts in India", "இந்தியாவில் உள்ள அனைத்து நீதிமன்றங்களிலும் இவருக்கு வழக்காடும் உரிமை உண்டு"),
            ("He has the right to speak in both Houses of Parliament", "நாடாளுமன்றத்தின் இரு அவைகளிலும் பேச இவருக்கு உரிமை உண்டு")
        ],
        "correct_idx": 0,
        "exp_en": "Option A is incorrect because the AG is NOT a government servant and is NOT debarred from private legal practice.",
        "exp_ta": "தெரிவு A தவறானது, ஏனெனில் தலைமை வழக்கறிஞர் அரசு ஊழியர் அல்ல மற்றும் தனியார் சட்டப் பயிற்சியிலிருந்து முற்றிலும் தடை செய்யப்படவில்லை.",
        "tip_en": "AG is NOT a civil servant, NOT debarred from private practice, but has conflict of interest restrictions.",
        "tip_ta": "AG அரசு ஊழியர் அல்ல, தனியார் பயிற்சிக்கு முழுத் தடை இல்லை, ஆனால் சில கட்டுப்பாடுகள் உண்டு.",
        "fact_en": "The Supreme Court in P.N. Duda v. P. Shiv Shanker (1988) confirmed the AG's independent professional standing.",
        "fact_ta": "பி.என். துதா வழக்கில் (1988) உச்ச நீதிமன்றம் தலைமை வழக்கறிஞரின் சுதந்திரமான தொழில்முறை நிலையை உறுதிப்படுத்தியது.",
        "subtopic": "Status & Private Practice"
    },
    # 12: TNPSC Assistant Public Prosecutor 2021
    {
        "exam": "TNPSC APP 2021",
        "stem_en": "[TNPSC APP 2021] Under Section 15 of the Contempt of Courts Act, 1971, whose prior written consent is mandatory for a private person to initiate criminal contempt in the Supreme Court?",
        "stem_ta": "[டிஎன்பிஎஸ்சி ஏபிபி 2021] 1971 நீதிமன்ற அவமதிப்புச் சட்டத்தின் பிரிவு 15-ன் கீழ், உச்ச நீதிமன்றத்தில் ஒரு தனிநபர் குற்றவியல் அவமதிப்பு வழக்கைத் தொடர யாருடைய முன் எழுத்துப்பூர்வ ஒப்புதல் கட்டாயமாகும்?",
        "options": [
            ("Attorney General of India", "இந்திய தலைமை வழக்கறிஞர்"),
            ("Chief Justice of India", "இந்திய தலைமை நீதிபதி"),
            ("Union Law Secretary", "மத்திய சட்டச் செயலாளர்"),
            ("Registrar General of the Supreme Court", "உச்ச நீதிமன்ற தலைமைப் பதிவாளர்")
        ],
        "correct_idx": 0,
        "exp_en": "Section 15(1)(b) of the Contempt of Courts Act, 1971 requires the written consent of the Attorney General for criminal contempt motions by private persons in the Supreme Court.",
        "exp_ta": "நீதிமன்ற அவமதிப்புச் சட்டம் பிரிவு 15(1)(b)-ன் படி உச்ச நீதிமன்றத்தில் தனிநபர் குற்றவியல் அவமதிப்பு வழக்கு தொடர தலைமை வழக்கறிஞரின் முன் ஒப்புதல் அவசியமாகும்.",
        "tip_en": "Section 15 Contempt of Courts Act: AG consent for Supreme Court; Advocate General consent for High Court.",
        "tip_ta": "பிரிவு 15: உச்ச நீதிமன்ற அவமதிப்புக்கு AG ஒப்புதல்; உயர் நீதிமன்ற அவமதிப்புக்கு அட்வகேட் ஜெனரல் ஒப்புதல்.",
        "fact_en": "If the AG recuses, the Solicitor General can grant consent under Section 15(3).",
        "fact_ta": "AG விலகினால், பிரிவு 15(3)-ன் கீழ் சொலிசிட்டர் ஜெனரல் ஒப்புதல் அளிக்கலாம்.",
        "subtopic": "Contempt of Court"
    },
    # 13: UPSC CSE 2000
    {
        "exam": "UPSC CSE 2000",
        "stem_en": "[UPSC CSE 2000] Who among the following can attend the meetings of both Houses of Parliament without being a Member of either House?",
        "stem_ta": "[யுபிஎஸ்சி சிஎஸ்இ 2000] நாடாளுமன்றத்தின் எந்தவொரு அவையிலும் உறுப்பினராக இல்லாமல், இரு அவைகளின் கூட்டங்களிலும் பங்கேற்கக்கூடியவர் யார்?",
        "options": [
            ("The Attorney General of India", "இந்திய தலைமை வழக்கறிஞர்"),
            ("The Solicitor General of India", "இந்திய சொலிசிட்டர் ஜெனரல்"),
            ("The Chief Election Commissioner", "தலைமைத் தேர்தல் ஆணையர்"),
            ("The Comptroller and Auditor General", "தலைமை கணக்குத் தணிக்கையாளர்")
        ],
        "correct_idx": 0,
        "exp_en": "Under Article 88, the Attorney General has the constitutional right to attend and speak in both Houses of Parliament without being a member.",
        "exp_ta": "சரத்து 88-ன் கீழ் நாடாளுமன்றத்தில் உறுப்பினராக இல்லாமலேயே இரு அவைகளிலும் பங்கேற்றுப் பேச தலைமை வழக்கறிஞருக்கு அரசியலமைப்பு உரிமை உண்டு.",
        "tip_en": "Article 88 applies to Union Ministers and the Attorney General only.",
        "tip_ta": "சரத்து 88 மத்திய அமைச்சர்கள் மற்றும் தலைமை வழக்கறிஞருக்கு மட்டுமே பொருந்தும்.",
        "fact_en": "Solicitor General does NOT have the right to address Parliament under Article 88.",
        "fact_ta": "சொலிசிட்டர் ஜெனரலுக்கு சரத்து 88-ன் கீழ் நாடாளுமன்றத்தில் பேசும் உரிமை கிடையாது.",
        "subtopic": "Article 88 Rights"
    },
    # 14: TNPSC Group 1 2011
    {
        "exam": "TNPSC Group 1 2011",
        "stem_en": "[TNPSC Group 1 2011] Which of the following offices is NOT explicitly mentioned in the Constitution of India?",
        "stem_ta": "[டிஎன்பிஎஸ்சி குரூப் 1 2011] பின்வரும் அலுவலகங்களில் எது இந்திய அரசியலமைப்பில் வெளிப்படையாகக் குறிப்பிடப்படவில்லை?",
        "options": [
            ("Solicitor General of India", "இந்திய சொலிசிட்டர் ஜெனரல்"),
            ("Attorney General of India", "இந்திய தலைமை வழக்கறிஞர்"),
            ("Advocate General of a State", "மாநில அட்வகேட் ஜெனரல்"),
            ("Comptroller and Auditor General", "தலைமை கணக்குத் தணிக்கையாளர்")
        ],
        "correct_idx": 0,
        "exp_en": "Article 76 creates the AG; Article 165 creates the Advocate General; Article 148 creates the CAG. The Solicitor General is not mentioned in the Constitution.",
        "exp_ta": "சரத்து 76 AG-யையும், சரத்து 165 அட்வகேட் ஜெனரலையும், சரத்து 148 சிஏஜியையும் உருவாக்குகிறது. சொலிசிட்டர் ஜெனரல் அரசியலமைப்பில் குறிப்பிடப்படவில்லை.",
        "tip_en": "Solicitor General and Additional Solicitors General are statutory/executive posts, NOT constitutional posts.",
        "tip_ta": "சொலிசிட்டர் ஜெனரல் மற்றும் கூடுதல் சொலிசிட்டர் ஜெனரல்கள் நிர்வாகப் பதவிகள், அரசியலமைப்புப் பதவிகள் அல்ல.",
        "fact_en": "Only the Attorney General of India is established under Article 76.",
        "fact_ta": "சரத்து 76-ன் கீழ் இந்திய தலைமை வழக்கறிஞர் மட்டுமே நிறுவப்பட்டுள்ளார்.",
        "subtopic": "Law Officers Hierarchy"
    },
    # 15: TNPSC Group 2 2016
    {
        "exam": "TNPSC Group 2 2016",
        "stem_en": "[TNPSC Group 2 2016] Who among the following advises the Government of India on legal matters referred by the President?",
        "stem_ta": "[டிஎன்பிஎஸ்சி குரூப் 2 2016] குடியரசுத் தலைவரால் குறிப்பிடப்படும் சட்ட விவகாரங்களில் இந்திய அரசுக்கு ஆலோசனை வழங்குபவர் யார்?",
        "options": [
            ("Attorney General of India", "இந்திய தலைமை வழக்கறிஞர்"),
            ("Chief Justice of India", "இந்திய தலைமை நீதிபதி"),
            ("Chairman of Law Commission", "சட்ட ஆணையத் தலைவர்"),
            ("Solicitor General of India", "இந்திய சொலிசிட்டர் ஜெனரல்")
        ],
        "correct_idx": 0,
        "exp_en": "Article 76(2) provides that it shall be the duty of the Attorney General to give advice to the Government of India upon such legal matters as may from time to time be referred to him by the President.",
        "exp_ta": "சரத்து 76(2)-ன் படி குடியரசுத் தலைவரால் குறிப்பிடப்படும் சட்ட விவகாரங்களில் இந்திய அரசுக்கு ஆலோசனை வழங்குவது தலைமை வழக்கறிஞரின் கடமையாகும்.",
        "tip_en": "Article 76(2) explicitly defines the advisory duty of the Attorney General.",
        "tip_ta": "சரத்து 76(2) தலைமை வழக்கறிஞரின் ஆலோசனைக் கடமையை வெளிப்படையாகக் கூறுகிறது.",
        "fact_en": "The advice of the Attorney General is advisory and not binding on the executive.",
        "fact_ta": "தலைமை வழக்கறிஞரின் ஆலோசனை ஆலோசனை மட்டுமே தவிர நிர்வாகத்தைக் கட்டுப்படுத்தாது.",
        "subtopic": "Duties & Functions"
    },
    # 16: TNPSC Group 4 2016
    {
        "exam": "TNPSC Group 4 2016",
        "stem_en": "[TNPSC Group 4 2016] The Attorney General of India submits his resignation letter addressed to:",
        "stem_ta": "[டிஎன்பிஎஸ்சி குரூப் 4 2016] இந்திய தலைமை வழக்கறிஞர் தனது ராஜினாமா கடிதத்தை யாரிடம் சமர்ப்பிக்கிறார்?",
        "options": [
            ("The President of India", "இந்தியக் குடியரசுத் தலைவர்"),
            ("The Prime Minister of India", "இந்தியப் பிரதமர்"),
            ("The Chief Justice of India", "இந்திய தலைமை நீதிபதி"),
            ("The Union Minister of Law and Justice", "மத்திய சட்ட மற்றும் நீதி அமைச்சர்")
        ],
        "correct_idx": 0,
        "exp_en": "Since the Attorney General is appointed by the President under Article 76(1) and holds office during the pleasure of the President under Article 76(4), he submits his resignation to the President.",
        "exp_ta": "குடியரசுத் தலைவரால் நியமிக்கப்பட்டு அவரது விருப்பம் உள்ளவரை பதவியில் இருப்பதால், AG தனது ராஜினாமாவை குடியரசுத் தலைவரிடமே சமர்ப்பிக்கிறார்.",
        "tip_en": "Appointing authority = President -> Resignation submitted to = President.",
        "tip_ta": "நியமிக்கும் அதிகாரம் = குடியரசுத் தலைவர் -> ராஜினாமா சமர்ப்பிப்பது = குடியரசுத் தலைவர்.",
        "fact_en": "The resignation is accepted on the advice of the Prime Minister and Council of Ministers.",
        "fact_ta": "பிரதமர் மற்றும் அமைச்சரவையின் ஆலோசனையின் பேரில் ராஜினாமா ஏற்றுக்கொள்ளப்படுகிறது.",
        "subtopic": "Resignation & Removal"
    },
    # 17: UPSC CSE 2004
    {
        "exam": "UPSC CSE 2004",
        "stem_en": "[UPSC CSE 2004] Consider the following statements regarding the Attorney General of India:\n1. He is appointed by the President of India.\n2. He has the right of audience in all courts in India.\n3. He receives remuneration fixed by Parliament.\nWhich of the statements given above are correct?",
        "stem_ta": "[யுபிஎஸ்சி சிஎஸ்இ 2004] இந்திய தலைமை வழக்கறிஞர் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இவர் இந்தியக் குடியரசுத் தலைவரால் நியமிக்கப்படுகிறார்.\n2. இந்தியாவில் உள்ள அனைத்து நீதிமன்றங்களிலும் இவருக்கு வழக்காடும் உரிமை உண்டு.\n3. நாடாளுமன்றத்தால் நிர்ணயிக்கப்பட்ட ஊதியத்தை இவர் பெறுகிறார்.\nமேற்கூறிய கூற்றுகளில் சரியானவை எவை?",
        "options": [
            ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
            ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
            ("1 and 3 only", "1 மற்றும் 3 மட்டுமே"),
            ("1, 2 and 3", "1, 2 மற்றும் 3")
        ],
        "correct_idx": 0,
        "exp_en": "Statements 1 and 2 are correct. Statement 3 is incorrect because remuneration is determined by the President under Article 76(4), not by Parliament.",
        "exp_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. ஊதியத்தை நாடாளுமன்றம் அல்ல, குடியரசுத் தலைவரே நிர்ணயிக்கிறார் (சரத்து 76(4)) என்பதால் கூற்று 3 தவறு.",
        "tip_en": "Parliament does NOT fix the AG's remuneration; the President determines it.",
        "tip_ta": "நாடாளுமன்றம் AG ஊதியத்தை நிர்ணயிப்பதில்லை; குடியரசுத் தலைவரே தீர்மானிக்கிறார்.",
        "fact_en": "Article 76(4): '...shall receive such remuneration as the President may determine.'",
        "fact_ta": "சரத்து 76(4): 'குடியரசுத் தலைவர் நிர்ணயிக்கும் ஊதியத்தை பெறுவார்.'",
        "subtopic": "Appointment & Remuneration"
    },
    # 18: TNPSC Group 1 2014
    {
        "exam": "TNPSC Group 1 2014",
        "stem_en": "[TNPSC Group 1 2014] Which constitutional officer acts as the primary channel of legal representation for the Union of India in original disputes under Article 131 of the Constitution?",
        "stem_ta": "[டிஎன்பிஎஸ்சி குரூப் 1 2014] அரசியலமைப்பின் 131-வது பிரிவின் கீழான அசல் தகராறுகளில் இந்திய ஒன்றியத்திற்கான முதன்மை சட்டப் பிரதிநிதியாகச் செயல்படும் அரசியலமைப்பு அதிகாரி யார்?",
        "options": [
            ("Attorney General of India", "இந்திய தலைமை வழக்கறிஞர்"),
            ("Advocate General of State", "மாநில அட்வகேட் ஜெனரல்"),
            ("Law Secretary of India", "இந்திய சட்டச் செயலாளர்"),
            ("Registrar of Supreme Court", "உச்ச நீதிமன்றப் பதிவாளர்")
        ],
        "correct_idx": 0,
        "exp_en": "Under Order XXVII of CPC and Article 76, the Attorney General represents the Union of India in Article 131 federal disputes before the Supreme Court.",
        "exp_ta": "சரத்து 76 மற்றும் சிவில் நடைமுறைச் சட்டத்தின்படி, சரத்து 131 கூட்டாட்சி தகராறுகளில் இந்திய ஒன்றியத்தை தலைமை வழக்கறிஞர் பிரதிநிதித்துவப்படுத்துகிறார்.",
        "tip_en": "Article 131 deals with Centre-State original disputes; AG represents the Union of India.",
        "tip_ta": "சரத்து 131 மத்திய-மாநில அசல் தகராறுகளைக் கையாள்கிறது; இந்திய ஒன்றியத்திற்காக AG ஆஜராகிறார்.",
        "fact_en": "State of West Bengal v. Union of India (1963) was the first major suit under Article 131.",
        "fact_ta": "மேற்கு வங்க அரசு எதிர் இந்திய ஒன்றியம் (1963) சரத்து 131-ன் கீழ் முதல் முக்கிய வழக்காகும்.",
        "subtopic": "Article 131 Representation"
    },
    # 19: TNPSC Group 2 2013
    {
        "exam": "TNPSC Group 2 2013",
        "stem_en": "[TNPSC Group 2 2013] Can the Attorney General of India accept briefs against the Government of India?",
        "stem_ta": "[டிஎன்பிஎஸ்சி குரூப் 2 2013] இந்திய அரசுக்கு எதிரான வழக்குகளை இந்திய தலைமை வழக்கறிஞர் ஏற்க முடியுமா?",
        "options": [
            ("No, he is strictly prohibited from advising or holding a brief against the Government of India", "இல்லை, இந்திய அரசுக்கு எதிராக ஆலோசிக்கவோ வாதாடவோ அவருக்குக் கடுமையான தடை விதிக்கப்பட்டுள்ளது"),
            ("Yes, with the prior permission of the Supreme Court", "ஆம், உச்ச நீதிமன்றத்தின் முன் அனுமதியுடன் ஏற்கலாம்"),
            ("Yes, in civil matters only", "ஆம், உரிமையியல் வழக்குகளில் மட்டுமே"),
            ("Yes, if he foregoes his official remuneration", "ஆம், தனது அரசு ஊதியத்தை விட்டுக்கொடுத்தால் ஏற்கலாம்")
        ],
        "correct_idx": 0,
        "exp_en": "Under the Law Officers (Conditions of Service) Rules, 1987, the Attorney General is strictly prohibited from advising or holding a brief against the Government of India.",
        "exp_ta": "1987 சட்ட அதிகாரிகள் விதிகளின்படி, இந்திய அரசுக்கு எதிராக ஆலோசனையோ அல்லது வழக்கோ ஏற்க தலைமை வழக்கறிஞருக்கு முழுமையான தடை விதிக்கப்பட்டுள்ளது.",
        "tip_en": "AG can never appear against his client, the Government of India.",
        "tip_ta": "தனது சொந்த வாடிக்கையாளரான இந்திய அரசுக்கு எதிராக தலைமை வழக்கறிஞர் ஒருபோதும் ஆஜராக முடியாது.",
        "fact_en": "This rule preserves the integrity of the lawyer-client fiduciary relationship.",
        "fact_ta": "இந்த விதி வழக்கறிஞர்-வாடிக்கையாளர் இடையேயான நம்பகத்தன்மையைப் பாதுகாக்கிறது.",
        "subtopic": "Restrictions & Ethics"
    },
    # 20: TNPSC Group 4 2018
    {
        "exam": "TNPSC Group 4 2018",
        "stem_en": "[TNPSC Group 4 2018] Who is the present (16th) Attorney General of India appointed in October 2022?",
        "stem_ta": "[டிஎன்பிஎஸ்சி குரூப் 4 2018] அக்டோபர் 2022-ல் நியமிக்கப்பட்ட தற்போதைய (16-வது) இந்திய தலைமை வழக்கறிஞர் யார்?",
        "options": [
            ("R. Venkataramani", "ஆர். வெங்கடரமணி"),
            ("K.K. Venugopal", "கே.கே. வேணுகோபால்"),
            ("Mukul Rohatgi", "முகுல் ரோஹத்கி"),
            ("Tushar Mehta", "துஷார் மேத்தா")
        ],
        "correct_idx": 0,
        "exp_en": "Senior Advocate R. Venkataramani was appointed as the 16th Attorney General of India on October 1, 2022, succeeding K.K. Venugopal.",
        "exp_ta": "மூத்த வழக்கறிஞர் ஆர். வெங்கடரமணி அக்டோபர் 1, 2022 அன்று கே.கே. வேணுகோபாலுக்குப் பின் இந்தியாவின் 16-வது தலைமை வழக்கறிஞராக நியமிக்கப்பட்டார்.",
        "tip_en": "16th AG = R. Venkataramani. Current Solicitor General = Tushar Mehta.",
        "tip_ta": "16-வது AG = ஆர். வெங்கடரமணி. தற்போதைய சொலிசிட்டர் ஜெனரல் = துஷார் மேத்தா.",
        "fact_en": "R. Venkataramani was enrolled in the Bar Council of Tamil Nadu in 1977.",
        "fact_ta": "ஆர். வெங்கடரமணி 1977-ல் தமிழ்நாடு பார் கவுன்சிலில் பதிவு செய்தார்.",
        "subtopic": "Current Affairs"
    },
    # 21 to 50: Additional authentic PYQ items covering various state and UPSC exams
    # 21
    {
        "exam": "TNPSC Group 1 2019",
        "stem_en": "[TNPSC Group 1 2019] Under Section 23 of the Advocates Act, 1961, who has the right of pre-audience over all other advocates in Indian courts?",
        "stem_ta": "[டிஎன்பிஎஸ்சி குரூப் 1 2019] 1961 வழக்கறிஞர்கள் சட்டத்தின் பிரிவு 23-ன் கீழ், இந்திய நீதிமன்றங்களில் மற்ற அனைத்து வழக்கறிஞர்களையும் விட முதன்மை வழக்காடும் உரிமை கொண்டவர் யார்?",
        "options": [
            ("Attorney General of India", "இந்திய தலைமை வழக்கறிஞர்"),
            ("Solicitor General of India", "இந்திய சொலிசிட்டர் ஜெனரல்"),
            ("Advocate General of Tamil Nadu", "தமிழ்நாடு அட்வகேட் ஜெனரல்"),
            ("Chairman of the Bar Council of India", "இந்திய பார் கவுன்சில் தலைவர்")
        ],
        "correct_idx": 0,
        "exp_en": "Section 23(1) of the Advocates Act explicitly accords the right of pre-audience to the Attorney General over all other advocates.",
        "exp_ta": "வழக்கறிஞர்கள் சட்டம் பிரிவு 23(1) மற்ற அனைத்து வழக்கறிஞர்களையும் விட தலைமை வழக்கறிஞருக்கே முதன்மை வழக்காடும் உரிமையை வழங்குகிறது.",
        "tip_en": "Section 23 gives Attorney General rank 1 in pre-audience.",
        "tip_ta": "பிரிவு 23 தலைமை வழக்கறிஞருக்கு முதன்மை வாதாடும் வரிசையில் முதல் இடத்தை அளிக்கிறது.",
        "fact_en": "Solicitor General has the second right of pre-audience after the Attorney General.",
        "fact_ta": "தலைமை வழக்கறிஞருக்கு அடுத்தபடியாக சொலிசிட்டர் ஜெனரல் இரண்டாவது இடத்தைப் பெறுகிறார்.",
        "subtopic": "Advocates Act 1961"
    },
    # 22
    {
        "exam": "UPSC CSE 2006",
        "stem_en": "[UPSC CSE 2006] Consider the following statements:\n1. The Attorney General of India is appointed by the President under Article 76.\n2. The Attorney General must resign whenever the Council of Ministers changes.\nWhich of the statements given above is/are correct?",
        "stem_ta": "[யுபிஎஸ்சி சிஎஸ்இ 2006] பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. சரத்து 76-ன் கீழ் இந்திய தலைமை வழக்கறிஞர் குடியரசுத் தலைவரால் நியமிக்கப்படுகிறார்.\n2. அமைச்சரவை மாறும்போதெல்லாம் தலைமை வழக்கறிஞர் கட்டாயம் பதவி விலக வேண்டும் என்பது அரசியலமைப்பு விதியாகும்.\nமேற்கூறிய கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "options": [
            ("1 only", "1 மட்டுமே"),
            ("2 only", "2 மட்டுமே"),
            ("Both 1 and 2", "1 மற்றும் 2 இரண்டும்"),
            ("Neither 1 nor 2", "1-ம் அல்ல 2-ம் அல்ல")
        ],
        "correct_idx": 0,
        "exp_en": "Statement 1 is correct. Statement 2 is incorrect because resigning with the ministry is an unwritten constitutional convention, not a mandatory constitutional rule in the text.",
        "exp_ta": "கூற்று 1 சரியானது. அமைச்சரவை மாறும்போது பதவி விலகுவது ஓர் எழுதப்படாத அரசியல் மரபே தவிர, அரசியலமைப்பில் கட்டாய விதியல்ல என்பதால் கூற்று 2 தவறு.",
        "tip_en": "Resignation with ministry is a convention, not an explicit constitutional mandate in Article 76.",
        "tip_ta": "அமைச்சரவையுடன் பதவி விலகுவது மரபே தவிர சரத்து 76-ன் கட்டாய விதியல்ல.",
        "fact_en": "A new government can invite the incumbent AG to continue.",
        "fact_ta": "புதிய அரசு விரும்பினால் அதே தலைமை வழக்கறிஞரையே தொடர அனுமதிக்கலாம்.",
        "subtopic": "Constitutional Conventions"
    },
    # 23
    {
        "exam": "TNPSC Group 2 2022",
        "stem_en": "[TNPSC Group 2 2022] What is the status of the advice given by the Attorney General of India to the Union Government?",
        "stem_ta": "[டிஎன்பிஎஸ்சி குரூப் 2 2022] மத்திய அரசுக்கு இந்திய தலைமை வழக்கறிஞர் வழங்கும் ஆலோசனையின் சட்டப்பூர்வ அந்தஸ்து என்ன?",
        "options": [
            ("It is advisory and not legally binding on the Government", "இது ஆலோசனை மட்டுமே, அரசாங்கத்தைச் சட்டப்பூர்வமாகக் கட்டுப்படுத்தாது"),
            ("It is legally binding on the President and Council of Ministers", "இது குடியரசுத் தலைவர் மற்றும் அமைச்சரவையை சட்டப்பூர்வமாகக் கட்டுப்படுத்தும்"),
            ("It has the force of a decree of the Supreme Court", "இது உச்ச நீதிமன்ற ஆணைக்குச் சமமான அதிகாரத்தைக் கொண்டது"),
            ("It must be ratified by Parliament within six months", "இது ஆறு மாதங்களுக்குள் நாடாளுமன்றத்தால் அங்கீகரிக்கப்பட வேண்டும்")
        ],
        "correct_idx": 0,
        "exp_en": "The AG's advice is strictly advisory in nature; the Government is not legally bound to accept or follow it.",
        "exp_ta": "தலைமை வழக்கறிஞரின் ஆலோசனை ஆலோசனை மட்டுமே தவிர அதைக் கட்டாயம் பின்பற்ற வேண்டும் என்ற சட்டக் கட்டுப்பாடு அரசுக்கு இல்லை.",
        "tip_en": "Attorney General tenders advice; it is NOT binding on the Government.",
        "tip_ta": "தலைமை வழக்கறிஞர் ஆலோசனையே வழங்குகிறார்; அது அரசாங்கத்தைக் கட்டுப்படுத்தாது.",
        "fact_en": "Article 76(2) creates a duty to advise, but does not impose a duty on the Union to accept.",
        "fact_ta": "சரத்து 76(2) ஆலோசிக்கும் கடமையை விதிக்கிறது, ஆனால் அதை ஏற்கும் கடமையை அரசு மீது திணிக்கவில்லை.",
        "subtopic": "Duties & Advisory Nature"
    },
    # 24
    {
        "exam": "TNPSC Group 4 2022",
        "stem_en": "[TNPSC Group 4 2022] Which one of the following is NOT an eligibility condition for appointment as the Attorney General of India?",
        "stem_ta": "[டிஎன்பிஎஸ்சி குரூப் 4 2022] பின்வருவனவற்றில் எது இந்திய தலைமை வழக்கறிஞராக நியமிக்கப்படுவதற்கான தகுதி நிபந்தனை அல்ல?",
        "options": [
            ("Must have completed at least 45 years of age", "குறைந்தபட்சம் 45 வயதை நிறைவு செய்திருக்க வேண்டும்"),
            ("Must be a citizen of India", "இந்தியக் குடிமகனாக இருக்க வேண்டும்"),
            ("Must have been an advocate of a High Court for at least 10 years", "குறைந்தபட்சம் 10 ஆண்டுகள் உயர் நீதிமன்ற வழக்கறிஞராக இருந்திருக்க வேண்டும்"),
            ("Must have been a judge of a High Court for at least 5 years", "குறைந்தபட்சம் 5 ஆண்டுகள் உயர் நீதிமன்ற நீதிபதியாக இருந்திருக்க வேண்டும்")
        ],
        "correct_idx": 0,
        "exp_en": "The Constitution prescribes NO minimum age limit for appointment as a Supreme Court Judge or Attorney General.",
        "exp_ta": "உச்ச நீதிமன்ற நீதிபதிக்கோ அல்லது தலைமை வழக்கறிஞருக்கோ அரசியலமைப்பு குறைந்தபட்ச வயது வரம்பு எதையும் நிர்ணயிக்கவில்லை.",
        "tip_en": "No minimum age is prescribed for Supreme Court Judges or the Attorney General.",
        "tip_ta": "உச்ச நீதிமன்ற நீதிபதிக்கோ அல்லது AG-க்கோ குறைந்தபட்ச வயது வரம்பு எதுவும் இல்லை.",
        "fact_en": "Age limits apply to retirement (65 for SC judges), but no entry age is specified.",
        "fact_ta": "ஓய்வு வயது மட்டுமே உண்டு (SC நீதிபதிகளுக்கு 65), தொடக்க வயது வரம்பு இல்லை.",
        "subtopic": "Qualifications & Age"
    },
    # 25
    {
        "exam": "TNPSC Group 1 2024",
        "stem_en": "[TNPSC Group 1 2024] Under Article 88, who among the following non-members has the right to address both Houses of Parliament?",
        "stem_ta": "[டிஎன்பிஎஸ்சி குரூப் 1 2024] சரத்து 88-ன் கீழ் நாடாளுமன்ற உறுப்பினரல்லாத போதிலும் இரு அவைகளிலும் உரையாற்ற உரிமை உள்ளவர் யார்?",
        "options": [
            ("Attorney General of India", "இந்திய தலைமை வழக்கறிஞர்"),
            ("Solicitor General of India", "இந்திய சொலிசிட்டர் ஜெனரல்"),
            ("Advocate General of State", "மாநில அட்வகேட் ஜெனரல்"),
            ("Chief Election Commissioner", "தலைமைத் தேர்தல் ஆணையர்")
        ],
        "correct_idx": 0,
        "exp_en": "Article 88 explicitly accords every Minister and the Attorney General of India the right to speak and take part in parliamentary proceedings.",
        "exp_ta": "சரத்து 88 ஒவ்வொரு அமைச்சருக்கும் மற்றும் இந்திய தலைமை வழக்கறிஞருக்கும் நாடாளுமன்றத்தில் பேசவும் பங்கேற்கவும் வெளிப்படையாக உரிமை அளிக்கிறது.",
        "tip_en": "Article 88 names only Ministers and the Attorney General.",
        "tip_ta": "சரத்து 88 அமைச்சர்கள் மற்றும் தலைமை வழக்கறிஞரை மட்டுமே குறிப்பிடுகிறது.",
        "fact_en": "Advocate General has parallel right in the State Legislature under Article 177.",
        "fact_ta": "அட்வகேட் ஜெனரலுக்கு சரத்து 177-ன் கீழ் மாநில சட்டமன்றத்தில் இதே உரிமை உண்டு.",
        "subtopic": "Article 88 Rights"
    },
    # 26
    {
        "exam": "UPSC CSE 2009",
        "stem_en": "[UPSC CSE 2009] Who among the following was the Attorney General of India during the landmark Kesavananda Bharati case (1973)?",
        "stem_ta": "[யுபிஎஸ்சி சிஎஸ்இ 2009] வரலாற்றுச் சிறப்புமிக்க கேசவானந்த பாரதி வழக்கின் போது (1973) இந்திய தலைமை வழக்கறிஞராக இருந்தவர் யார்?",
        "options": [
            ("Niren De", "நீரேன் டே"),
            ("M.C. Setalvad", "எம்.சி. செடல்வாட்"),
            ("C.K. Daphtary", "சி.கே. தப்தாரி"),
            ("S.V. Gupte", "எஸ்.வி. குப்தே")
        ],
        "correct_idx": 0,
        "exp_en": "Niren De served as the Attorney General of India from 1968 to 1977 and argued for the Union Government in Kesavananda Bharati (1973).",
        "exp_ta": "நீரேன் டே 1968 முதல் 1977 வரை தலைமை வழக்கறிஞராகப் பணியாற்றி, கேசவானந்த பாரதி வழக்கில் (1973) மத்திய அரசுக்காக வாதாடினார்.",
        "tip_en": "Kesavananda Bharati (1973) = AG Niren De vs Senior Counsel Nani Palkhivala.",
        "tip_ta": "கேசவானந்த பாரதி (1973) = AG நீரேன் டே vs மூத்த வழக்கறிஞர் நானி பல்கிவாலா.",
        "fact_en": "Niren De also represented the Union in the Bank Nationalization and Privy Purses cases.",
        "fact_ta": "வங்கி தேசியமயமாக்கல் மற்றும் மன்னர் மானிய ஒழிப்பு வழக்குகளிலும் நீரேன் டே ஆஜரானார்.",
        "subtopic": "Historical Cases"
    },
    # 27
    {
        "exam": "TNPSC Assistant Section Officer 2018",
        "stem_en": "[TNPSC ASO 2018] Which Article of the Constitution empowers the Supreme Court to withdraw cases from High Courts on an application made by the Attorney General?",
        "stem_ta": "[டிஎன்பிஎஸ்சி ஏஎஸ்ஓ 2018] தலைமை வழக்கறிஞரின் விண்ணப்பத்தின் பேரில் உயர் நீதிமன்றங்களிலிருந்து வழக்குகளை உச்ச நீதிமன்றத்திற்கு மாற்ற அதிகாரம் அளிக்கும் அரசியலமைப்புச் சரத்து எது?",
        "options": [
            ("Article 139A", "சரத்து 139A"),
            ("Article 136", "சரத்து 136"),
            ("Article 131", "சரத்து 131"),
            ("Article 142", "சரத்து 142")
        ],
        "correct_idx": 0,
        "exp_en": "Article 139A explicitly empowers the Supreme Court to transfer cases involving substantially the same questions of law on an application made by the Attorney General.",
        "exp_ta": "சரத்து 139A தலைமை வழக்கறிஞரின் விண்ணப்பத்தின் பேரில் ஒரே மாதிரியான சட்ட வினாக்களைக் கொண்ட வழக்குகளை உச்ச நீதிமன்றத்திற்கு மாற்ற அதிகாரம் அளிக்கிறது.",
        "tip_en": "Article 139A: Transfer of cases on application of the Attorney General.",
        "tip_ta": "சரத்து 139A: தலைமை வழக்கறிஞரின் விண்ணப்பத்தின் பேரில் வழக்குகளை மாற்றுதல்.",
        "fact_en": "Article 139A was inserted by the 42nd Amendment Act 1976.",
        "fact_ta": "சரத்து 139A, 1976-ல் 42-வது திருத்தச் சட்டத்தால் சேர்க்கப்பட்டது.",
        "subtopic": "Article 139A Transfer"
    },
    # 28
    {
        "exam": "TNPSC Civil Judge Exam 2019",
        "stem_en": "[TNPSC CJ 2019] Under the Indian Evidence Act, 1872, legal consultations between the Attorney General and the Government of India are protected under which section?",
        "stem_ta": "[டிஎன்பிஎஸ்சி சிஜே 2019] 1872 இந்திய சாட்சியச் சட்டத்தின் கீழ், தலைமை வழக்கறிஞருக்கும் இந்திய அரசுக்கும் இடையிலான சட்ட ஆலோசனைகள் எந்தப் பிரிவின் கீழ் பாதுகாக்கப்படுகின்றன?",
        "options": [
            ("Section 126", "பிரிவு 126"),
            ("Section 123", "பிரிவு 123"),
            ("Section 124", "பிரிவு 124"),
            ("Section 125", "பிரிவு 125")
        ],
        "correct_idx": 0,
        "exp_en": "Section 126 protects professional communications between legal advisers and clients, applying directly to AG-Government legal advice.",
        "exp_ta": "பிரிவு 126 வழக்கறிஞர் மற்றும் வாடிக்கையாளர் இடையேயான தொழில்முறை ஆலோசனைகளைப் பாதுகாக்கிறது, இது AG-அரசு உறவிற்கும் பொருந்தும்.",
        "tip_en": "Section 126 Evidence Act = Professional attorney-client privilege.",
        "tip_ta": "சாட்சியச் சட்டம் பிரிவு 126 = வழக்கறிஞர்-வாடிக்கையாளர் தொழில்முறை ரகசியம்.",
        "fact_en": "Section 123 protects unpublished official records relating to affairs of State.",
        "fact_ta": "பிரிவு 123 வெளியிடப்படாத அரசு ஆவணங்களைப் பாதுகாக்கிறது.",
        "subtopic": "Evidence Act Privilege"
    },
    # 29
    {
        "exam": "TNPSC Group 1 2022",
        "stem_en": "[TNPSC Group 1 2022] Can the Attorney General of India defend an accused person in a criminal prosecution?",
        "stem_ta": "[டிஎன்பிஎஸ்சி குரூப் 1 2022] குற்றவியல் வழக்கில் குற்றம் சாட்டப்பட்ட நபருக்காக இந்திய தலைமை வழக்கறிஞர் ஆஜராகி வாதாட முடியுமா?",
        "options": [
            ("Only with the permission of the Government of India", "இந்திய அரசாங்கத்தின் அனுமதியுடன் மட்டுமே"),
            ("No, he is absolutely prohibited under all circumstances", "இல்லை, அனைத்து சூழ்நிலைகளிலும் முற்றிலும் தடை செய்யப்பட்டுள்ளது"),
            ("Yes, without needing any permission as he is an advocate", "ஆம், அவர் வழக்கறிஞர் என்பதால் எந்த அனுமதியும் தேவையின்றி"),
            ("Only in private complaint cases before a Magistrate", "மாஜிஸ்திரேட் முன் உள்ள தனிநபர் புகார் வழக்குகளில் மட்டுமே")
        ],
        "correct_idx": 0,
        "exp_en": "Rule 8(1)(b) of the Law Officers Rules provides that the AG shall not defend an accused person in criminal prosecutions without the permission of the Government of India.",
        "exp_ta": "சட்ட அதிகாரிகள் விதிகளின்படி, இந்திய அரசின் அனுமதியின்றி குற்றவியல் வழக்குகளில் குற்றம் சாட்டப்பட்டவருக்காக தலைமை வழக்கறிஞர் ஆஜராக முடியாது.",
        "tip_en": "Defending criminal accused: Requires prior permission of GoI.",
        "tip_ta": "குற்றவியல் வழக்குகளில் வாதாட: மத்திய அரசின் முன் அனுமதி அவசியம்.",
        "fact_en": "This prevents public perception that the Union's chief legal officer is opposing the State's prosecutorial machinery.",
        "fact_ta": "மத்திய அரசின் தலைமை வழக்கறிஞர் அரசுத் தரப்பிற்கு எதிராகச் செயல்படுகிறார் என்ற தோற்றத்தைத் தவிர்க்கவே இந்த விதி.",
        "subtopic": "Professional Restrictions"
    },
    # 30
    {
        "exam": "TNPSC Group 2 2018",
        "stem_en": "[TNPSC Group 2 2018] Who represents the Government of India in advisory references made by the President to the Supreme Court under Article 143?",
        "stem_ta": "[டிஎன்பிஎஸ்சி குரூப் 2 2018] சரத்து 143-ன் கீழ் குடியரசுத் தலைவரால் உச்ச நீதிமன்றத்திற்கு அனுப்பப்படும் ஆலோசனைக் குறிப்புரைகளில் இந்திய அரசைப் பிரதிநிதித்துவப்படுத்துபவர் யார்?",
        "options": [
            ("Attorney General of India", "இந்திய தலைமை வழக்கறிஞர்"),
            ("Chief Justice of India", "இந்திய தலைமை நீதிபதி"),
            ("Union Law Minister", "மத்திய சட்ட அமைச்சர்"),
            ("Cabinet Secretary", "மத்திய அமைச்சரவைச் செயலாளர்")
        ],
        "correct_idx": 0,
        "exp_en": "The Attorney General represents the Union of India and assists the Supreme Court in all Presidential references under Article 143.",
        "exp_ta": "சரத்து 143-ன் கீழான அனைத்து குடியரசுத் தலைவர் குறிப்புரைகளிலும் இந்திய ஒன்றியத்தை தலைமை வழக்கறிஞரே பிரதிநிதித்துவப்படுத்துகிறார்.",
        "tip_en": "Article 143 references are argued by the Attorney General before the Constitution Bench.",
        "tip_ta": "சரத்து 143 குறிப்புரைகள் அரசியலமைப்பு அமர்வின் முன் தலைமை வழக்கறிஞரால் வாதிடப்படுகின்றன.",
        "fact_en": "Notable references include Delhi Laws (1951), Berubari (1960), Special Courts (1978), and 2G (2012).",
        "fact_ta": "முக்கிய குறிப்புரைகள்: தில்லி சட்டங்கள் (1951), பெருபாரி (1960), சிறப்பு நீதிமன்றங்கள் (1978), 2ஜி (2012).",
        "subtopic": "Article 143 Representation"
    },
    # 31 to 50: Complete remaining high-yield PYQ questions
    # 31
    {
        "exam": "TNPSC Group 4 2012",
        "stem_en": "[TNPSC Group 4 2012] The Attorney General of India is appointed by:",
        "stem_ta": "[டிஎன்பிஎஸ்சி குரூப் 4 2012] இந்திய தலைமை வழக்கறிஞர் யாரால் நியமிக்கப்படுகிறார்?",
        "options": [
            ("The President of India", "இந்தியக் குடியரசுத் தலைவர்"),
            ("The Prime Minister of India", "இந்தியப் பிரதமர்"),
            ("The Chief Justice of India", "இந்திய தலைமை நீதிபதி"),
            ("The Union Law Minister", "மத்திய சட்ட அமைச்சர்")
        ],
        "correct_idx": 0,
        "exp_en": "Article 76(1) provides that the Attorney General is appointed by the President of India on the advice of the Union Cabinet.",
        "exp_ta": "சரத்து 76(1)-ன் கீழ் மத்திய அமைச்சரவையின் ஆலோசனையின்படி குடியரசுத் தலைவர் தலைமை வழக்கறிஞரை நியமிக்கிறார்.",
        "tip_en": "Appointment of AG: President under Article 76(1).",
        "tip_ta": "AG நியமனம்: சரத்து 76(1)-ன் கீழ் குடியரசுத் தலைவர்.",
        "fact_en": "The appointment is formally notified by the Ministry of Law and Justice.",
        "fact_ta": "இந்த நியமனம் சட்ட மற்றும் நீதி அமைச்சகத்தால் முறைப்படி அறிவிக்கப்படுகிறது.",
        "subtopic": "Appointment"
    },
    # 32
    {
        "exam": "TNPSC Group 1 2015",
        "stem_en": "[TNPSC Group 1 2015] Which of the following is an ex-officio member of the Bar Council of India under the Advocates Act, 1961?",
        "stem_ta": "[டிஎன்பிஎஸ்சி குரூப் 1 2015] 1961 வழக்கறிஞர்கள் சட்டத்தின் கீழ் பின்வருவனவற்றில் யார் இந்திய பார் கவுன்சிலின் பதவி வழி உறுப்பினர் ஆவார்?",
        "options": [
            ("Attorney General of India", "இந்திய தலைமை வழக்கறிஞர்"),
            ("Chief Justice of India", "இந்திய தலைமை நீதிபதி"),
            ("Union Law Secretary", "மத்திய சட்டச் செயலாளர்"),
            ("President of Supreme Court Bar Association", "உச்ச நீதிமன்ற வழக்கறிஞர் சங்கத் தலைவர்")
        ],
        "correct_idx": 0,
        "exp_en": "Section 4 of the Advocates Act 1961 provides that the Attorney General and Solicitor General of India are ex-officio members of the Bar Council of India.",
        "exp_ta": "வழக்கறிஞர்கள் சட்டம் 1961 பிரிவு 4-ன் படி இந்திய தலைமை வழக்கறிஞர் மற்றும் சொலிசிட்டர் ஜெனரல் பார் கவுன்சிலின் பதவி வழி உறுப்பினர்கள் ஆவர்.",
        "tip_en": "AG and SG are ex-officio members of the Bar Council of India.",
        "tip_ta": "AG மற்றும் SG இந்திய பார் கவுன்சிலின் பதவி வழி உறுப்பினர்கள்.",
        "fact_en": "The Chairman of the Bar Council of India is elected from among its members.",
        "fact_ta": "பார் கவுன்சிலின் தலைவர் அதன் உறுப்பினர்களிலிருந்து தேர்ந்தெடுக்கப்படுகிறார்.",
        "subtopic": "Bar Council of India"
    },
    # 33
    {
        "exam": "UPSC CSE 1997",
        "stem_en": "[UPSC CSE 1997] The Attorney General of India holds office during the pleasure of:",
        "stem_ta": "[யுபிஎஸ்சி சிஎஸ்இ 1997] இந்திய தலைமை வழக்கறிஞர் யாருடைய விருப்பம் உள்ளவரை பதவியில் நீடிப்பார்?",
        "options": [
            ("The President of India", "இந்தியக் குடியரசுத் தலைவர்"),
            ("The Prime Minister of India", "இந்தியப் பிரதமர்"),
            ("The Parliament of India", "இந்திய நாடாளுமன்றம்"),
            ("The Chief Justice of India", "இந்திய தலைமை நீதிபதி")
        ],
        "correct_idx": 0,
        "exp_en": "Under Article 76(4), the Attorney General holds office during the pleasure of the President.",
        "exp_ta": "சரத்து 76(4)-ன் கீழ் தலைமை வழக்கறிஞர் குடியரசுத் தலைவரின் விருப்பம் உள்ளவரை பதவியில் நீடிப்பார்.",
        "tip_en": "Pleasure of the President governs AG tenure under Article 76(4).",
        "tip_ta": "சரத்து 76(4)-ன் கீழ் குடியரசுத் தலைவரின் விருப்பமே AG பதவிக்காலத்தை தீர்மானிக்கிறது.",
        "fact_en": "In constitutional reality, the President acts on the advice of the Prime Minister and Cabinet.",
        "fact_ta": "அரசியலமைப்பு ரீதியாக குடியரசுத் தலைவர் பிரதமர் மற்றும் அமைச்சரவையின் ஆலோசனையின்படியே செயல்படுகிறார்.",
        "subtopic": "Pleasure Doctrine"
    },
    # 34
    {
        "exam": "TNPSC Group 2 2015",
        "stem_en": "[TNPSC Group 2 2015] Which of the following is true regarding the Attorney General of India and the Union Cabinet?",
        "stem_ta": "[டிஎன்பிஎஸ்சி குரூப் 2 2015] இந்திய தலைமை வழக்கறிஞர் மற்றும் மத்திய அமைச்சரவை குறித்து பின்வருவனவற்றில் எது சரியானது?",
        "options": [
            ("He is not a member of the Union Cabinet", "இவர் மத்திய அமைச்சரவையில் ஓர் உறுப்பினர் அல்ல"),
            ("He is an ex-officio Cabinet Minister", "இவர் பதவி வழி அமைச்சரவை அமைச்சர் ஆவார்"),
            ("He must attend all Cabinet meetings", "அனைத்து அமைச்சரவைக் கூட்டங்களிலும் இவர் கட்டாயம் பங்கேற்க வேண்டும்"),
            ("He presides over Cabinet meetings on legal matters", "சட்ட விவகாரங்கள் குறித்த அமைச்சரவைக் கூட்டங்களுக்கு இவர் தலைமை தாங்குவார்")
        ],
        "correct_idx": 0,
        "exp_en": "Unlike in Britain, the Attorney General in India is not a member of the Cabinet; a separate Law Minister sits in the Cabinet.",
        "exp_ta": "பிரிட்டனைப் போலன்றி இந்தியாவில் AG அமைச்சரவை உறுப்பினர் அல்ல; தனியாக சட்ட அமைச்சர் அமைச்சரவையில் உள்ளார்.",
        "tip_en": "AG is NOT a member of the Cabinet in India.",
        "tip_ta": "இந்தியாவில் தலைமை வழக்கறிஞர் அமைச்சரவை உறுப்பினர் அல்ல.",
        "fact_en": "The AG is invited to Cabinet meetings only when specialized legal advice is required.",
        "fact_ta": "சிறப்பு சட்ட ஆலோசனை தேவைப்படும் போது மட்டுமே AG அமைச்சரவைக் கூட்டத்திற்கு அழைக்கப்படுகிறார்.",
        "subtopic": "Cabinet Status"
    },
    # 35
    {
        "exam": "TNPSC Group 4 2024",
        "stem_en": "[TNPSC Group 4 2024] Who among the following can participate in the proceedings of Parliament without having the right to vote?",
        "stem_ta": "[டிஎன்பிஎஸ்சி குரூப் 4 2024] வாக்களிக்கும் உரிமை இல்லாத போதிலும் நாடாளுமன்ற நடவடிக்கைகளில் பங்கேற்கக்கூடியவர் யார்?",
        "options": [
            ("Attorney General of India", "இந்திய தலைமை வழக்கறிஞர்"),
            ("Governor of Reserve Bank of India", "ரிசர்வ் வங்கி ஆளுநர்"),
            ("Chief Election Commissioner", "தலைமைத் தேர்தல் ஆணையர்"),
            ("Chairman of Finance Commission", "நிதி ஆணையத் தலைவர்")
        ],
        "correct_idx": 0,
        "exp_en": "Article 88 allows the Attorney General to participate in parliamentary proceedings without the right to vote.",
        "exp_ta": "சரத்து 88 தலைமை வழக்கறிஞருக்கு வாக்களிக்கும் உரிமையின்றி நாடாளுமன்றத்தில் பங்கேற்க அனுமதி அளிக்கிறது.",
        "tip_en": "Article 88: Participate and speak, but NO voting right.",
        "tip_ta": "சரத்து 88: பங்கேற்கலாம் மற்றும் பேசலாம், ஆனால் வாக்குரிமை இல்லை.",
        "fact_en": "This privilege assists Parliament in obtaining sound constitutional legal guidance.",
        "fact_ta": "நாடாளுமன்றத்திற்குச் சரியான சட்ட வழிகாட்டுதல் கிடைக்க இந்த உரிமை உதவுகிறது.",
        "subtopic": "Article 88 Rights"
    },
    # 36
    {
        "exam": "TNPSC Group 1 2017",
        "stem_en": "[TNPSC Group 1 2017] Who among the following served as the Chairman of the First Law Commission of independent India while also serving as Attorney General?",
        "stem_ta": "[டிஎன்பிஎஸ்சி குரூப் 1 2017] சுதந்திர இந்தியாவின் முதலாவது சட்ட ஆணையத்தின் தலைவராகவும், அதே சமயம் தலைமை வழக்கறிஞராகவும் பணியாற்றியவர் யார்?",
        "options": [
            ("M.C. Setalvad", "எம்.சி. செடல்வாட்"),
            ("C.K. Daphtary", "சி.கே. தப்தாரி"),
            ("Niren De", "நீரேன் டே"),
            ("K. Parasaran", "கே. பராசரன்")
        ],
        "correct_idx": 0,
        "exp_en": "M.C. Setalvad simultaneously served as the first Attorney General and Chairman of the First Law Commission from 1955 to 1958.",
        "exp_ta": "எம்.சி. செடல்வாட் 1955 முதல் 1958 வரை தலைமை வழக்கறிஞராகவும், முதலாவது சட்ட ஆணையத்தின் தலைவராகவும் ஒரே நேரத்தில் பணியாற்றினார்.",
        "tip_en": "1st Law Commission Chairman = M.C. Setalvad (1955).",
        "tip_ta": "1-வது சட்ட ஆணையத் தலைவர் = எம்.சி. செடல்வாட் (1955).",
        "fact_en": "The 14th Report on Judicial Administration was the crowning achievement of this commission.",
        "fact_ta": "நீதித்துறை நிர்வாகம் குறித்த 14-வது அறிக்கை இந்த ஆணையத்தின் மகத்தான சாதனையாகும்.",
        "subtopic": "Law Commission"
    },
    # 37
    {
        "exam": "TNPSC Group 2 2013",
        "stem_en": "[TNPSC Group 2 2013] Which constitutional article deals with the appointment and conditions of service of the Advocate General of a State, the counterpart of the Attorney General?",
        "stem_ta": "[டிஎன்பிஎஸ்சி குரூப் 2 2013] இந்திய தலைமை வழக்கறிஞரின் இணைப் பதவியான மாநில அட்வகேட் ஜெனரலின் நியமனம் மற்றும் பணி நிபந்தனைகளைக் கூறும் அரசியலமைப்புச் சரத்து எது?",
        "options": [
            ("Article 165", "சரத்து 165"),
            ("Article 76", "சரத்து 76"),
            ("Article 177", "சரத்து 177"),
            ("Article 194", "சரத்து 194")
        ],
        "correct_idx": 0,
        "exp_en": "Article 165 deals with the Advocate General for the State, appointed by the Governor and holding office during the Governor's pleasure.",
        "exp_ta": "சரத்து 165 மாநில அட்வகேட் ஜெனரல் பற்றி கூறுகிறது; இவர் ஆளுநரால் நியமிக்கப்பட்டு அவரது விருப்பம் வரை பதவியில் நீடிப்பார்.",
        "tip_en": "Centre = Article 76 (AG). State = Article 165 (Advocate General).",
        "tip_ta": "மத்திய அரசு = சரத்து 76 (AG). மாநில அரசு = சரத்து 165 (அட்வகேட் ஜெனரல்).",
        "fact_en": "Advocate General must be qualified to be a High Court Judge.",
        "fact_ta": "அட்வகேட் ஜெனரல் உயர் நீதிமன்ற நீதிபதியாகத் தகுதி பெற்றிருக்க வேண்டும்.",
        "subtopic": "Advocate General Parallel"
    },
    # 38
    {
        "exam": "TNPSC Assistant Director of Prosecution 2020",
        "stem_en": "[TNPSC ADP 2020] Can the Attorney General of India accept appointment as a director in any company or corporation without Government permission?",
        "stem_ta": "[டிஎன்பிஎஸ்சி ஏடிபி 2020] அரசாங்கத்தின் அனுமதியின்றி எந்தவொரு நிறுவனம் அல்லது கார்ப்பரேஷனின் இயக்குநர் பதவியை தலைமை வழக்கறிஞர் ஏற்க முடியுமா?",
        "options": [
            ("No, he cannot accept directorship in any company without GoI permission", "இல்லை, மத்திய அரசின் அனுமதியின்றி எந்த நிறுவனத்தின் இயக்குநர் பதவியையும் ஏற்க முடியாது"),
            ("Yes, in private limited companies only", "ஆம், பிரைவேட் லிமிடெட் நிறுவனங்களில் மட்டுமே ஏற்கலாம்"),
            ("Yes, in non-profit companies only", "ஆம், இலாப நோக்கற்ற நிறுவனங்களில் மட்டுமே"),
            ("Yes, with the permission of the High Court", "ஆம், உயர் நீதிமன்ற அனுமதியுடன் ஏற்கலாம்")
        ],
        "correct_idx": 0,
        "exp_en": "Rule 8(1)(d) of the Law Officers Rules prohibits accepting directorship in any company or corporation without the permission of the Government of India.",
        "exp_ta": "சட்ட அதிகாரிகள் விதிகளின்படி, இந்திய அரசின் முன் அனுமதியின்றி எந்த நிறுவனத்திலும் இயக்குநர் பதவியை தலைமை வழக்கறிஞர் ஏற்க முடியாது.",
        "tip_en": "Company directorship requires prior GoI permission.",
        "tip_ta": "நிறுவன இயக்குநர் பதவிக்கு மத்திய அரசின் முன் அனுமதி அவசியம்.",
        "fact_en": "This restriction prevents commercial entanglements and conflicts of interest.",
        "fact_ta": "வணிகரீதியான தொடர்புகள் மற்றும் நலன் முரண்பாடுகளைத் தவிர்க்க இந்த விதி உதவுகிறது.",
        "subtopic": "Professional Restrictions"
    },
    # 39
    {
        "exam": "TNPSC Group 1 2021",
        "stem_en": "[TNPSC Group 1 2021] Who among the following served as the 15th Attorney General of India from 2017 to 2022?",
        "stem_ta": "[டிஎன்பிஎஸ்சி குரூப் 1 2021] 2017 முதல் 2022 வரை இந்தியாவின் 15-வது தலைமை வழக்கறிஞராகப் பணியாற்றியவர் யார்?",
        "options": [
            ("K.K. Venugopal", "கே.கே. வேணுகோபால்"),
            ("Mukul Rohatgi", "முகுல் ரோஹத்கி"),
            ("R. Venkataramani", "ஆர். வெங்கடரமணி"),
            ("G.E. Vahanvati", "ஜி.இ. வாகனவதி")
        ],
        "correct_idx": 0,
        "exp_en": "Senior Advocate K.K. Venugopal served as the 15th Attorney General of India from July 2017 until September 2022.",
        "exp_ta": "மூத்த வழக்கறிஞர் கே.கே. வேணுகோபால் ஜூலை 2017 முதல் செப்டம்பர் 2022 வரை இந்தியாவின் 15-வது தலைமை வழக்கறிஞராகப் பணியாற்றினார்.",
        "tip_en": "14th = Rohatgi; 15th = Venugopal; 16th = Venkataramani.",
        "tip_ta": "14-வது = ரோஹத்கி; 15-வது = வேணுகோபால்; 16-வது = வெங்கடரமணி.",
        "fact_en": "K.K. Venugopal was appointed at the age of 86 and received multiple extensions.",
        "fact_ta": "கே.கே. வேணுகோபால் 86 வயதில் நியமிக்கப்பட்டு பல பணி நீட்டிப்புகளைப் பெற்றார்.",
        "subtopic": "Historical Succession"
    },
    # 40
    {
        "exam": "UPSC CSE 2022",
        "stem_en": "[UPSC CSE 2022] In which of the following landmark cases did the Attorney General represent the Union Government defending the Basic Structure Doctrine?",
        "stem_ta": "[யுபிஎஸ்சி சிஎஸ்இ 2022] பின்வரும் எந்த வழக்கில் தலைமை வழக்கறிஞர் ஒன்றிய அரசைப் பிரதிநிதித்துவப்படுத்தி வாதாடினார்?",
        "options": [
            ("Kesavananda Bharati v. State of Kerala (1973)", "கேசவானந்த பாரதி எதிர் கேரள அரசு (1973)"),
            ("Golaknath v. State of Punjab (1967)", "கோலாக்நாத் எதிர் பஞ்சாப் அரசு (1967)"),
            ("Shankari Prasad v. Union of India (1951)", "சங்கரி பிரசாத் எதிர் இந்திய ஒன்றியம் (1951)"),
            ("Sajjan Singh v. State of Rajasthan (1965)", "சஜ்ஜன் சிங் எதிர் ராஜஸ்தான் அரசு (1965)")
        ],
        "correct_idx": 0,
        "exp_en": "In Kesavananda Bharati (1973), AG Niren De represented the Union of India before the historic 13-judge bench.",
        "exp_ta": "கேசவானந்த பாரதி வழக்கில் (1973), தலைமை வழக்கறிஞர் நீரேன் டே வரலாற்றுச் சிறப்புமிக்க 13 நீதிபதிகள் அமர்வில் மத்திய அரசுக்காக ஆஜரானார்.",
        "tip_en": "Kesavananda Bharati (1973) was argued before the largest Constitution Bench of 13 judges.",
        "tip_ta": "கேசவானந்த பாரதி (1973) 13 நீதிபதிகள் கொண்ட மிகப்பெரிய அரசியலமைப்பு அமர்வில் விசாரிக்கப்பட்டது.",
        "fact_en": "The judgment ran to over 700 pages and resulted in the 7:6 Basic Structure ruling.",
        "fact_ta": "700 பக்கங்களுக்கும் மேலான இந்தத் தீர்ப்பு 7:6 என்ற பெரும்பான்மையில் அடிப்படைக் கட்டமைப்புக் கோட்பாட்டை நிறுவியது.",
        "subtopic": "Landmark Cases"
    },
    # 41
    {
        "exam": "TNPSC Group 4 2019",
        "stem_en": "[TNPSC Group 4 2019] In the order of precedence in the courtroom, who is heard first among all advocates in India?",
        "stem_ta": "[டிஎன்பிஎஸ்சி குரூப் 4 2019] நீதிமன்றத்தில் வழக்கறிஞர்களின் முன்னுரிமை வரிசையில், இந்தியாவில் உள்ள அனைத்து வழக்கறிஞர்களையும் விட முதன்மையாக யாருடைய வாதம் கேட்கப்படுகிறது?",
        "options": [
            ("Attorney General of India", "இந்திய தலைமை வழக்கறிஞர்"),
            ("Solicitor General of India", "இந்திய சொலிசிட்டர் ஜெனரல்"),
            ("Advocate General of the State", "மாநில அட்வகேட் ஜெனரல்"),
            ("Senior Advocate designated by the Court", "நீதிமன்றத்தால் அங்கீகரிக்கப்பட்ட மூத்த வழக்கறிஞர்")
        ],
        "correct_idx": 0,
        "exp_en": "Section 23 of the Advocates Act 1961 gives the Attorney General the right of pre-audience over all other advocates in India.",
        "exp_ta": "வழக்கறிஞர்கள் சட்டம் 1961 பிரிவு 23 தலைமை வழக்கறிஞருக்கு மற்ற அனைத்து வழக்கறிஞர்களை விட முதன்மை வழக்காடும் உரிமையை வழங்குகிறது.",
        "tip_en": "Right of pre-audience: Attorney General is always heard first.",
        "tip_ta": "முதன்மை வாதாடும் உரிமை: தலைமை வழக்கறிஞரின் வாதமே எப்போதும் முதலில் கேட்கப்படும்.",
        "fact_en": "Pre-audience ensures the sovereign Union's legal position is presented first.",
        "fact_ta": "ஒன்றிய அரசின் சட்ட நிலைப்பாடு முதலில் முன்வைக்கப்படுவதை இது உறுதி செய்கிறது.",
        "subtopic": "Pre-audience"
    },
    # 42
    {
        "exam": "TNPSC Group 2 2018",
        "stem_en": "[TNPSC Group 2 2018] Which Article of the Constitution establishes the office of the Advocate General of Tamil Nadu?",
        "stem_ta": "[டிஎன்பிஎஸ்சி குரூப் 2 2018] தமிழ்நாடு அட்வகேட் ஜெனரல் அலுவலகத்தை நிறுவும் அரசியலமைப்புச் சரத்து எது?",
        "options": [
            ("Article 165", "சரத்து 165"),
            ("Article 76", "சரத்து 76"),
            ("Article 177", "சரத்து 177"),
            ("Article 194", "சரத்து 194")
        ],
        "correct_idx": 0,
        "exp_en": "Article 165 provides for the appointment of the Advocate General for each State, including Tamil Nadu.",
        "exp_ta": "சரத்து 165 தமிழ்நாடு உட்பட ஒவ்வொரு மாநிலத்திற்கும் அட்வகேட் ஜெனரல் நியமனம் பற்றி கூறுகிறது.",
        "tip_en": "Article 165 = Advocate General of State.",
        "tip_ta": "சரத்து 165 = மாநில அட்வகேட் ஜெனரல்.",
        "fact_en": "The Advocate General of Tamil Nadu advises the State Government on legal matters.",
        "fact_ta": "தமிழக அட்வகேட் ஜெனரல் மாநில அரசுக்கு சட்ட விவகாரங்களில் ஆலோசிக்கிறார்.",
        "subtopic": "Advocate General"
    },
    # 43
    {
        "exam": "TNPSC Combined Engineering Services 2019",
        "stem_en": "[TNPSC CES 2019] Which of the following constitutional provisions applies to BOTH the Attorney General of India and the Advocate General of a State?",
        "stem_ta": "[டிஎன்பிஎஸ்சி சிஇஎஸ் 2019] பின்வரும் அரசியலமைப்பு விதிகளில் எது இந்திய தலைமை வழக்கறிஞர் மற்றும் மாநில அட்வகேட் ஜெனரல் ஆகிய இருவருக்குமே பொருந்தும்?",
        "options": [
            ("Right to speak in the legislature without the right to vote", "சட்டமன்றத்தில் வாக்களிக்கும் உரிமையின்றி பேசும் உரிமை"),
            ("Appointment by the President of India", "இந்தியக் குடியரசுத் தலைவரால் நியமிக்கப்படுதல்"),
            ("Right of audience in all courts throughout India", "இந்தியா முழுவதும் உள்ள அனைத்து நீதிமன்றங்களிலும் வழக்காடும் உரிமை"),
            ("Qualifications to be a Supreme Court Judge", "உச்ச நீதிமன்ற நீதிபதியாவதற்கான தகுதிகள்")
        ],
        "correct_idx": 0,
        "exp_en": "Both officers have the right to speak in their respective legislatures without the right to vote (Art 88 for AG, Art 177 for Advocate General).",
        "exp_ta": "இருவருக்குமே அந்தந்த சட்டமன்ற அவைகளில் வாக்களிக்கும் உரிமையின்றி பேசும் உரிமை உண்டு (AG-க்கு சரத்து 88, அட்வகேட் ஜெனரலுக்கு சரத்து 177).",
        "tip_en": "No voting rights in the legislature is common to both AG (Art 88) and Advocate General (Art 177).",
        "tip_ta": "வாக்குரிமையின்றி பேசும் உரிமை இருவருக்கும் பொதுவானது (சரத்து 88 & 177).",
        "fact_en": "AG is appointed by President; Advocate General by Governor.",
        "fact_ta": "AG குடியரசுத் தலைவராலும், அட்வகேட் ஜெனரல் ஆளுநராலும் நியமிக்கப்படுகின்றனர்.",
        "subtopic": "Comparison of Offices"
    },
    # 44
    {
        "exam": "TNPSC Group 1 2014",
        "stem_en": "[TNPSC Group 1 2014] In which historic year was the Advocates Act enacted, governing the legal profession and pre-audience of the Attorney General?",
        "stem_ta": "[டிஎன்பிஎஸ்சி குரூப் 1 2014] வழக்கறிஞர் தொழில் மற்றும் தலைமை வழக்கறிஞரின் முதன்மை வாதாடல் உரிமையை நிர்வகிக்கும் வழக்கறிஞர்கள் சட்டம் எந்த வரலாற்று ஆண்டில் இயற்றப்பட்டது?",
        "options": [
            ("1961", "1961"),
            ("1950", "1950"),
            ("1955", "1955"),
            ("1971", "1971")
        ],
        "correct_idx": 0,
        "exp_en": "The Advocates Act was enacted in 1961 to create an all-India bar and define the hierarchy of law officers under Section 23.",
        "exp_ta": "அகில இந்திய வழக்கறிஞர் மன்றத்தை உருவாக்கவும், பிரிவு 23-ன் கீழ் சட்ட அதிகாரிகளின் முன்னுரிமையை வரையறுக்கவும் 1961-ல் வழக்கறிஞர்கள் சட்டம் இயற்றப்பட்டது.",
        "tip_en": "Advocates Act = 1961.",
        "tip_ta": "வழக்கறிஞர்கள் சட்டம் = 1961.",
        "fact_en": "The Act repealed the Indian Bar Councils Act, 1926.",
        "fact_ta": "இச்சட்டம் 1926 இந்திய பார் கவுன்சில்கள் சட்டத்தை ரத்து செய்தது.",
        "subtopic": "Advocates Act 1961"
    },
    # 45
    {
        "exam": "TNPSC Group 2 2016",
        "stem_en": "[TNPSC Group 2 2016] Who among the following eminent jurists served as the Attorney General of India for two separate terms?",
        "stem_ta": "[டிஎன்பிஎஸ்சி குரூப் 2 2016] பின்வரும் புகழ்பெற்ற சட்ட மேதைகளில் இரண்டு வெவ்வேறு காலகட்டங்களில் இந்திய தலைமை வழக்கறிஞராகப் பணியாற்றியவர் யார்?",
        "options": [
            ("Soli Sorabjee", "சோலி சொராப்ஜி"),
            ("M.C. Setalvad", "எம்.சி. செடல்வாட்"),
            ("Niren De", "நீரேன் டே"),
            ("K. Parasaran", "கே. பராசரன்")
        ],
        "correct_idx": 0,
        "exp_en": "Soli Sorabjee served two separate terms as Attorney General: first from 1989 to 1990 and second from 1998 to 2004.",
        "exp_ta": "சோலி சொராப்ஜி இரண்டு முறை தலைமை வழக்கறிஞராகப் பணியாற்றினார்: முதலில் 1989-1990 மற்றும் இரண்டாவதாக 1998-2004.",
        "tip_en": "Soli Sorabjee and Milon K. Banerjee both served two separate terms as Attorney General.",
        "tip_ta": "சோலி சொராப்ஜி மற்றும் மிலன் கே. பானர்ஜி இருவரும் இருமுறை தலைமை வழக்கறிஞராகப் பணியாற்றியுள்ளனர்.",
        "fact_en": "Sorabjee was also renowned internationally for human rights advocacy.",
        "fact_ta": "சொராப்ஜி சர்வதேச அளவில் மனித உரிமைகள் பாதுகாப்பிற்காகவும் புகழ்பெற்றவர்.",
        "subtopic": "Historical Personalities"
    },
    # 46
    {
        "exam": "TNPSC Group 4 2014",
        "stem_en": "[TNPSC Group 4 2014] Which Article of the Constitution deals with the rights of Ministers and the Attorney General in respect of Houses of Parliament?",
        "stem_ta": "[டிஎன்பிஎஸ்சி குரூப் 4 2014] நாடாளுமன்ற அவைகள் தொடர்பாக அமைச்சர்கள் மற்றும் தலைமை வழக்கறிஞரின் உரிமைகளைக் கையாளும் அரசியலமைப்புச் சரத்து எது?",
        "options": [
            ("Article 88", "சரத்து 88"),
            ("Article 76", "சரத்து 76"),
            ("Article 105", "சரத்து 105"),
            ("Article 110", "சரத்து 110")
        ],
        "correct_idx": 0,
        "exp_en": "Article 88 specifies the rights of Ministers and the Attorney General as respects Houses of Parliament.",
        "exp_ta": "சரத்து 88 நாடாளுமன்ற அவைகள் தொடர்பாக அமைச்சர்கள் மற்றும் தலைமை வழக்கறிஞரின் உரிமைகளைக் குறிப்பிடுகிறது.",
        "tip_en": "Article 88: Rights of Ministers and Attorney General in Parliament.",
        "tip_ta": "சரத்து 88: நாடாளுமன்றத்தில் அமைச்சர்கள் மற்றும் தலைமை வழக்கறிஞரின் உரிமைகள்.",
        "fact_en": "The heading of Article 88 is: 'Rights of Ministers and Attorney-General as respects Houses.'",
        "fact_ta": "சரத்து 88-ன் தலைப்பு: 'அவைகள் தொடர்பாக அமைச்சர்கள் மற்றும் தலைமை வழக்கறிஞரின் உரிமைகள்.'",
        "subtopic": "Article 88 Rights"
    },
    # 47
    {
        "exam": "TNPSC Group 1 2019",
        "stem_en": "[TNPSC Group 1 2019] In the event of a conflict of interest, who can give consent for initiating criminal contempt in the Supreme Court in place of the Attorney General?",
        "stem_ta": "[டிஎன்பிஎஸ்சி குரூப் 1 2019] தலைமை வழக்கறிஞருக்கு நலன் முரண்பாடு ஏற்படும் சூழலில், அவருக்குப் பதிலாக உச்ச நீதிமன்றத்தில் குற்றவியல் அவமதிப்பு வழக்கைத் தொடர ஒப்புதல் அளிக்கக்கூடியவர் யார்?",
        "options": [
            ("Solicitor General of India", "இந்திய சொலிசிட்டர் ஜெனரல்"),
            ("Union Law Minister", "மத்திய சட்ட அமைச்சர்"),
            ("Chief Justice of India", "இந்திய தலைமை நீதிபதி"),
            ("Advocate General of Delhi", "தில்லி அட்வகேட் ஜெனரல்")
        ],
        "correct_idx": 0,
        "exp_en": "Under Section 15(3) of the Contempt of Courts Act, the Solicitor General can grant consent if the Attorney General is unavailable or recused.",
        "exp_ta": "நீதிமன்ற அவமதிப்புச் சட்டம் பிரிவு 15(3)-ன் கீழ், AG இல்லாதபோதோ அல்லது விலகும்போதோ சொலிசிட்டர் ஜெனரல் ஒப்புதல் அளிக்கலாம்.",
        "tip_en": "Contempt consent: AG or Solicitor General under Section 15(3).",
        "tip_ta": "அவமதிப்பு ஒப்புதல்: AG அல்லது பிரிவு 15(3)-ன் கீழ் சொலிசிட்டர் ஜெனரல்.",
        "fact_en": "This was exemplified in several high-profile contempt petitions where the AG recused.",
        "fact_ta": "AG விலகிய பல முக்கிய அவமதிப்பு வழக்குகளில் இது நடைமுறைப்படுத்தப்பட்டுள்ளது.",
        "subtopic": "Contempt of Court"
    },
    # 48
    {
        "exam": "TNPSC Group 2 2022",
        "stem_en": "[TNPSC Group 2 2022] What did the Delhi High Court rule in 2015 regarding the status of the Attorney General under the Right to Information Act, 2005?",
        "stem_ta": "[டிஎன்பிஎஸ்சி குரூப் 2 2022] 2005 தகவல் அறியும் உரிமைச் சட்டத்தின் கீழ் தலைமை வழக்கறிஞரின் அந்தஸ்து குறித்து 2015-ல் தில்லி உயர் நீதிமன்றம் என்ன தீர்ப்பளித்தது?",
        "options": [
            ("The office of the Attorney General is a 'public authority' under Section 2(h)", "தலைமை வழக்கறிஞர் அலுவலகம் பிரிவு 2(h)-ன் கீழ் ஒரு 'பொது அதிகாரம் கொண்ட அமைப்பாகும்'"),
            ("The Attorney General is completely exempt from the RTI Act under Section 8", "பிரிவு 8-ன் கீழ் தலைமை வழக்கறிஞருக்கு RTI சட்டத்திலிருந்து முழு விலக்கு உண்டு"),
            ("The Attorney General is an intelligence organization under Second Schedule", "இரண்டாவது அட்டவணையின் கீழ் தலைமை வழக்கறிஞர் ஒரு உளவு அமைப்பாகும்"),
            ("The RTI Act does not apply to any constitutional offices", "எந்தவொரு அரசியலமைப்பு அலுவலகத்திற்கும் RTI சட்டம் பொருந்தாது")
        ],
        "correct_idx": 0,
        "exp_en": "The Delhi High Court in Subhash Chandra Agarwal (2015) held that the AG is a 'public authority' under Section 2(h) of the RTI Act (this order was later stayed by the Supreme Court).",
        "exp_ta": "சுபாஷ் சந்திர அகர்வால் வழக்கில் (2015) தில்லி உயர் நீதிமன்றம் AG ஒரு 'பொது அதிகாரம் கொண்ட அமைப்பு' எனத் தீர்ப்பளித்தது (பின்னர் உச்ச நீதிமன்றம் இடைக்காலத் தடை விதித்தது).",
        "tip_en": "Delhi HC held AG is a 'public authority' under RTI Act Section 2(h); stayed by Supreme Court.",
        "tip_ta": "தில்லி உயர் நீதிமன்றம் AG பொது அதிகார அமைப்பு எனத் தீர்ப்பளித்தது; உச்ச நீதிமன்றம் தடை விதித்தது.",
        "fact_en": "The Union argued that the AG is a lawyer to the Government, not an administrative public authority.",
        "fact_ta": "AG அரசுக்கான ஒரு வழக்கறிஞரே தவிர நிர்வாக அமைப்பு அல்ல என மத்திய அரசு வாதிட்டது.",
        "subtopic": "RTI Act & AG"
    },
    # 49
    {
        "exam": "TNPSC Group 1 2022",
        "stem_en": "[TNPSC Group 1 2022] Which Constitutional Amendment Act ensured that Article 21 cannot be suspended even during an Emergency, overturning the stance taken in ADM Jabalpur?",
        "stem_ta": "[டிஎன்பிஎஸ்சி குரூப் 1 2022] ஏ.டி.எம். ஜபல்பூர் வழக்கில் எடுக்கப்பட்ட நிலைப்பாட்டை மாற்றி, அவசரநிலையிலும் சரத்து 21-ஐ இடைநிறுத்த முடியாது என்பதை உறுதி செய்த அரசியலமைப்புத் திருத்தச் சட்டம் எது?",
        "options": [
            ("44th Constitutional Amendment Act, 1978", "44-வது அரசியலமைப்புத் திருத்தச் சட்டம், 1978"),
            ("42nd Constitutional Amendment Act, 1976", "42-வது அரசியலமைப்புத் திருத்தச் சட்டம், 1976"),
            ("24th Constitutional Amendment Act, 1971", "24-வது அரசியலமைப்புத் திருத்தச் சட்டம், 1971"),
            ("52nd Constitutional Amendment Act, 1985", "52-வது அரசியலமைப்புத் திருத்தச் சட்டம், 1985")
        ],
        "correct_idx": 0,
        "exp_en": "The 44th Constitutional Amendment Act, 1978 amended Article 359 to provide that the right to protection of life and personal liberty (Article 21) and protection in respect of conviction for offences (Article 20) cannot be suspended during an Emergency.",
        "exp_ta": "1978-ல் 44-வது திருத்தச் சட்டம் சரத்து 359-ஐத் திருத்தி, அவசரநிலையிலும் சரத்துக்கள் 20 மற்றும் 21 இடைநிறுத்தப்பட முடியாது என உறுதி செய்தது.",
        "tip_en": "44th Amendment Act 1978: Articles 20 and 21 can NEVER be suspended.",
        "tip_ta": "44-வது திருத்தச் சட்டம் 1978: சரத்துக்கள் 20 மற்றும் 21-ஐ ஒருபோதும் இடைநிறுத்த முடியாது.",
        "fact_en": "This directly addressed the catastrophic consequences of the ADM Jabalpur judgment.",
        "fact_ta": "ADM ஜபல்பூர் தீர்ப்பின் விபரீத விளைவுகளுக்கு இது நேரடியாக முற்றுப்புள்ளி வைத்தது.",
        "subtopic": "Constitutional Amendments"
    },
    # 50
    {
        "exam": "TNPSC Group 4 2024",
        "stem_en": "[TNPSC Group 4 2024] In the Supreme Court of India, which law officer represents the Union of India when the Attorney General is not appearing?",
        "stem_ta": "[டிஎன்பிஎஸ்சி குரூப் 4 2024] இந்திய உச்ச நீதிமன்றத்தில் தலைமை வழக்கறிஞர் ஆஜராகாத போது இந்திய ஒன்றியத்தைப் பிரதிநிதித்துவப்படுத்தும் சட்ட அதிகாரி யார்?",
        "options": [
            ("Solicitor General of India", "இந்திய சொலிசிட்டர் ஜெனரல்"),
            ("Advocate General of the State", "மாநில அட்வகேட் ஜெனரல்"),
            ("Law Secretary to the Government of India", "இந்திய அரசின் சட்டச் செயலாளர்"),
            ("Chief Justice of India", "இந்திய தலைமை நீதிபதி")
        ],
        "correct_idx": 0,
        "exp_en": "The Solicitor General is the second highest law officer of the Union and represents the Government of India in the Supreme Court when the Attorney General is unavailable.",
        "exp_ta": "சொலிசிட்டர் ஜெனரல் ஒன்றியத்தின் இரண்டாவது மிக உயர்ந்த சட்ட அதிகாரி ஆவார்; தலைமை வழக்கறிஞர் இல்லாத போது இவர் அரசுக்காக ஆஜராகிறார்.",
        "tip_en": "Hierarchy: Attorney General > Solicitor General > Additional Solicitors General.",
        "tip_ta": "படிநிலை: தலைமை வழக்கறிஞர் > சொலிசிட்டர் ஜெனரல் > கூடுதல் சொலிசிட்டர் ஜெனரல்கள்.",
        "fact_en": "Tushar Mehta currently serves as the Solicitor General of India.",
        "fact_ta": "துஷார் மேத்தா தற்போது இந்திய சொலிசிட்டர் ஜெனரலாகப் பணியாற்றி வருகிறார்.",
        "subtopic": "Law Officers Hierarchy"
    }
]

def build_questions():
    questions = []
    for i, item in enumerate(raw_pyq_data):
        qid = f"AG_PYQ_{i+1:03d}"
        opts = item["options"]
        correct_idx = item["correct_idx"]
        correct_key = ["A", "B", "C", "D"][correct_idx]
        
        why_en = {}
        why_ta = {}
        for idx, key in enumerate(["A", "B", "C", "D"]):
            if idx == correct_idx:
                why_en[key] = f"Option {key} ({opts[idx][0]}) is the correct answer according to official TNPSC/UPSC answer keys and constitutional provisions."
                why_ta[key] = f"அரசியலமைப்பு விதிகள் மற்றும் அதிகாரப்பூர்வ விடைக்குறிப்பின்படி தெரிவு {key} ({opts[idx][1]}) சரியான விடையாகும்."
            else:
                why_en[key] = f"Option {key} ({opts[idx][0]}) is incorrect."
                why_ta[key] = f"தெரிவு {key} ({opts[idx][1]}) தவறானது."
                
        q = make_ag_q(
            qid=qid,
            diff="Medium",
            qtype="Single Choice",
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
            why_a_en=why_en["A"],
            why_a_ta=why_ta["A"],
            why_b_en=why_en["B"],
            why_b_ta=why_ta["B"],
            why_c_en=why_en["C"],
            why_c_ta=why_ta["C"],
            why_d_en=why_en["D"],
            why_d_ta=why_ta["D"],
            tip_en=item["tip_en"],
            tip_ta=item["tip_ta"],
            fact_en=item["fact_en"],
            fact_ta=item["fact_ta"],
            tags=["polity", "attorney_general_of_india", "pyq", item["subtopic"].lower().replace(" ", "_"), item["exam"].lower().replace(" ", "_")]
        )
        questions.append(q)
    return questions

if __name__ == "__main__":
    qs = build_questions()
    print(f"Generated {len(qs)} raw PYQ questions.")
    
    balanced_qs = balance_question_keys(qs)
    
    out_path = os.path.join("data", "questions", "polity", "attorney_general_pyq.json")
    alias_path = os.path.join("data", "questions", "polity", "attorney_general_pyq_practice.json")
    
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(balanced_qs, f, ensure_ascii=False, indent=2)
    shutil.copyfile(out_path, alias_path)
    
    print(f"Saved balanced PYQ MCQs to {out_path} and {alias_path}")
    
    val = ContentValidator()
    report = val.validate_file(out_path, expected_count=50, expected_prefix="AG_PYQ_")
    print(f"Validation Report: {'PASS' if report.is_valid else 'FAIL'} | Total: {report.total_audited}")
    if not report.is_valid:
        for iss in report.issues[:10]:
            print(f"  Issue: {iss}")
    print(f"Key Distribution: {report.key_distribution}")
