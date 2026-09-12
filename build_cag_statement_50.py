# -*- coding: utf-8 -*-
"""
Build 50 Statement-Based MCQs for CAG (Comptroller & Auditor General of India)
ID range: CAG_S_001 to CAG_S_050
"""

import json
import os
from cag_mcq_helper import make_cag_q
from rebalance_er_helper import balance_question_keys
from tools.nova_content_engine.validator import ContentValidator

raw_statement_data = [
    # 1
    {
        "subtopic": "Constitutional Status & Articles",
        "stem_en": "Consider the following statements regarding the constitutional position of the Comptroller and Auditor General (CAG) of India:\n1. The office of the CAG is provided under Chapter V of Part V of the Constitution of India.\n2. The CAG is an independent constitutional authority under Article 148.\nWhich of the statements given above is/are correct?",
        "stem_ta": "இந்தியத் தலைமைக் கணக்குத் தணிக்கையாளரின் (சி.ஏ.ஜி) அரசியலமைப்பு நிலை குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இந்திய அரசியலமைப்பின் பகுதி V, அத்தியாயம் V-ன் கீழ் சி.ஏ.ஜி அலுவலகம் வழங்கப்பட்டுள்ளது.\n2. சரத்து 148-ன் கீழ் சி.ஏ.ஜி ஒரு தன்னாட்சி பெற்ற அரசியலமைப்பு அதிகார அமைப்பாகும்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("1 only", "1 மட்டும்"),
            ("2 only", "2 மட்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Both statements are correct. Articles 148 to 151 in Chapter V of Part V of the Constitution deal with the Comptroller and Auditor General of India, establishing the office as an independent constitutional body.",
        "exp_ta": "இரண்டு கூற்றுகளும் சரியானவை. அரசியலமைப்பின் பகுதி V, அத்தியாயம் V-ல் உள்ள சரத்துகள் 148 முதல் 151 வரை தலைமைத் தணிக்கையாளரைக் கையாள்கின்றன; சரத்து 148 இதை ஒரு தன்னாட்சி அரசியலமைப்பு அமைப்பாக நிறுவுகிறது.",
        "tip_en": "Part V, Chapter V (Articles 148-151) deals with the Comptroller and Auditor General.",
        "tip_ta": "பகுதி V, அத்தியாயம் V (சரத்துகள் 148-151) இந்தியத் தலைமைக் கணக்குத் தணிக்கையாளரைக் கையாள்கிறது.",
        "fact_en": "Article 148(1) provides for appointment by the President by warrant under his hand and seal.",
        "fact_ta": "சரத்து 148(1) குடியரசுத் தலைவரால் முத்திரையுடன் கூடிய ஆணை மூலம் நியமிக்கப்படுவதை உறுதி செய்கிறது."
    },
    # 2
    {
        "subtopic": "Appointment and Removal",
        "stem_en": "Consider the following statements regarding the appointment and removal of the CAG:\n1. The CAG is appointed by the President by warrant under his hand and seal.\n2. The CAG can be removed from office by the President on his own pleasure without parliamentary address.\nWhich of the statements given above is/are correct?",
        "stem_ta": "சி.ஏ.ஜியின் நியமனம் மற்றும் பதவி நீக்கம் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. சி.ஏ.ஜி குடியரசுத் தலைவரால் கையொப்பம் மற்றும் முத்திரையிட்ட ஆணை மூலம் நியமிக்கப்படுகிறார்.\n2. நாடாளுமன்ற தீர்மானமின்றி குடியரசுத் தலைவர் தனது சொந்த விருப்பத்தின் பேரில் சி.ஏ.ஜியைப் பதவி நீக்கம் செய்யலாம்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("1 only", "1 மட்டும்"),
            ("2 only", "2 மட்டும்"),
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Statement 1 is correct. Statement 2 is incorrect because the CAG does not hold office during the pleasure of the President; he can only be removed in like manner and on like grounds as a Judge of the Supreme Court (Article 124(4)).",
        "exp_ta": "கூற்று 1 சரி. கூற்று 2 தவறு, ஏனெனில் சி.ஏ.ஜி குடியரசுத் தலைவரின் விருப்பத்தின் அடிப்படையில் பதவியில் இருப்பதில்லை; உச்ச நீதிமன்ற நீதிபதியை நீக்கும் அதே நடைமுறை மற்றும் காரணங்களின் அடிப்படையிலேயே அவரை நீக்க முடியும்.",
        "tip_en": "CAG does NOT hold office during presidential pleasure; removal requires special majority address by both Houses.",
        "tip_ta": "சி.ஏ.ஜி குடியரசுத் தலைவரின் விருப்பத்தின் பேரில் பதவியில் இருப்பதில்லை; உச்ச நீதிமன்ற நீதிபதிக்கு இணையான நீக்க நடைமுறை தேவை.",
        "fact_en": "Grounds of removal: Proved misbehaviour or incapacity under Article 124(4).",
        "fact_ta": "நீக்குவதற்கான காரணங்கள்: நிரூபிக்கப்பட்ட தவறான நடத்தை அல்லது இயலாமை (சரத்து 124(4))."
    },
    # 3
    {
        "subtopic": "Tenure and Resignation",
        "stem_en": "Consider the following statements regarding the tenure and resignation of the CAG:\n1. The CAG holds office for a term of 6 years or up to 65 years of age, whichever is earlier.\n2. The CAG can resign from office at any time by addressing his resignation letter to the Chief Justice of India.\nWhich of the statements given above is/are correct?",
        "stem_ta": "சி.ஏ.ஜியின் பதவிக்காலம் மற்றும் ராஜினாமா குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. சி.ஏ.ஜி 6 ஆண்டுகள் அல்லது 65 வயது வரை, எது முந்தையதோ அதுவரை பதவியில் இருப்பார்.\n2. சி.ஏ.ஜி எந்த நேரத்திலும் தனது ராஜினாமா கடிதத்தை இந்தியத் தலைமை நீதிபதிக்கு அனுப்பி பதவி விலகலாம்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("1 only", "1 மட்டும்"),
            ("2 only", "2 மட்டும்"),
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Statement 1 is correct. Statement 2 is incorrect because the CAG submits his resignation letter to the President of India, not to the Chief Justice.",
        "exp_ta": "கூற்று 1 சரி. கூற்று 2 தவறு, ஏனெனில் சி.ஏ.ஜி தனது ராஜினாமா கடிதத்தை இந்தியக் குடியரசுத் தலைவரிடம் சமர்ப்பிக்க வேண்டுமே தவிர தலைமை நீதிபதியிடம் அல்ல.",
        "tip_en": "Tenure: 6 years or 65 years. Resignation addressed to: President of India.",
        "tip_ta": "பதவிக்காலம்: 6 ஆண்டுகள் அல்லது 65 வயது. ராஜினாமா கடிதம்: குடியரசுத் தலைவருக்கு அனுப்பப்பட வேண்டும்.",
        "fact_en": "Tenure is regulated by Section 4 of the CAG (Duties, Powers and Conditions of Service) Act, 1971.",
        "fact_ta": "பதவிக்காலம் 1971 ஆம் ஆண்டின் சி.ஏ.ஜி சட்டத்தின் பிரிவு 4-ன் கீழ் முறைப்படுத்தப்படுகிறது."
    },
    # 4
    {
        "subtopic": "Post-Retirement Ineligibility",
        "stem_en": "Consider the following statements regarding the post-retirement restrictions on the CAG:\n1. Under Article 148(4), the CAG is ineligible for further office either under the Government of India or under the Government of any State.\n2. The CAG is constitutionally barred from becoming a member of any non-governmental charitable trust.\nWhich of the statements given above is/are correct?",
        "stem_ta": "சி.ஏ.ஜியின் ஓய்வுக்குப் பிந்தைய கட்டுப்பாடுகள் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. சரத்து 148(4)-ன் கீழ், சி.ஏ.ஜி ஓய்வு பெற்ற பின்னர் மத்திய அல்லது மாநில அரசின் கீழ் எந்தவொரு பதவியையும் வகிக்கத் தகுதியற்றவர்.\n2. எந்தவொரு அரசு சாரா தொண்டு அறக்கட்டளையிலும் உறுப்பினராவதற்கு சி.ஏ.ஜிக்கு அரசியலமைப்பு ரீதியாகத் தடை விதிக்கப்பட்டுள்ளது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("1 only", "1 மட்டும்"),
            ("2 only", "2 மட்டும்"),
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Statement 1 is correct under Article 148(4). Statement 2 is incorrect because the constitutional prohibition applies only to employment under the Government of India or State Governments, not private or charitable trust activities.",
        "exp_ta": "கூற்று 1 சரத்து 148(4)-ன் கீழ் சரியானது. கூற்று 2 தவறு, ஏனெனில் அரசியலமைப்புத் தடை மத்திய அல்லது மாநில அரசுப் பணிகளுக்கு மட்டுமே பொருந்தும்; தனியார் அல்லது தொண்டுப் பணிகளுக்குப் பொருந்தாது.",
        "tip_en": "Article 148(4) bars further government employment to ensure fearless auditing without expecting executive favours.",
        "tip_ta": "சரத்து 148(4) எதிர்கால அரசுப் பதவிகளைத் தடை செய்வதன் மூலம் நடுநிலையான தணிக்கையை உறுதி செய்கிறது.",
        "fact_en": "Former CAG Vinod Rai served as Chairman of the Banks Board Bureau, an advisory body.",
        "fact_ta": "முன்னாள் சி.ஏ.ஜி வினோத் ராய் வங்கி வாரிய பணியகத்தின் (BBB) தலைவராகப் பணியாற்றினார்."
    },
    # 5
    {
        "subtopic": "Charged Expenditure & Administrative Expenses",
        "stem_en": "Consider the following statements regarding the salary and expenses of the CAG:\n1. The salary and allowances of the CAG are charged upon the Consolidated Fund of India.\n2. The administrative expenses of the office of the CAG, including salaries of all staff, are subject to the annual vote of Parliament.\nWhich of the statements given above is/are correct?",
        "stem_ta": "சி.ஏ.ஜியின் ஊதியம் மற்றும் செலவினங்கள் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. சி.ஏ.ஜியின் ஊதியம் மற்றும் படிகள் இந்தியத் திரட்டப்பட்ட நிதியிலிருந்து பொறுப்பாக்கப்பட்ட செலவினமாகும் (charged expenditure).\n2. சி.ஏ.ஜி அலுவலகத்தின் அனைத்துப் பணியாளர்களின் ஊதியம் உள்ளிட்ட நிர்வாகச் செலவுகள் நாடாளுமன்றத்தின் வருடாந்திர வாக்கெடுப்பிற்கு உட்பட்டவை.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("1 only", "1 மட்டும்"),
            ("2 only", "2 மட்டும்"),
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Statement 1 is correct. Statement 2 is incorrect because under Article 148(6), the entire administrative expenses of the office of the CAG, including all salaries, allowances, and pensions of persons serving in that office, are charged upon the Consolidated Fund of India and are non-votable.",
        "exp_ta": "கூற்று 1 சரி. கூற்று 2 தவறு, ஏனெனில் சரத்து 148(6)-ன் கீழ், சி.ஏ.ஜி அலுவலகத்தின் அனைத்து நிர்வாகச் செலவுகள் மற்றும் ஊழியர்களின் ஊதியங்கள் அனைத்தும் திரட்டப்பட்ட நிதியில் சுமத்தப்பட்டவை (non-votable) ஆகும்; நாடாளுமன்ற வாக்கெடுப்பிற்கு உட்பட்டவை அல்ல.",
        "tip_en": "Article 148(6): Both CAG's salary AND staff administrative expenses are charged on CFI (non-votable).",
        "tip_ta": "சரத்து 148(6): சி.ஏ.ஜியின் ஊதியம் மற்றும் ஊழியர்களின் நிர்வாகச் செலவுகள் இரண்டும் திரட்டப்பட்ட நிதியில் சுமத்தப்பட்டவை.",
        "fact_en": "Charged expenditures can be discussed in Parliament, but cannot be voted upon.",
        "fact_ta": "பொறுப்பாக்கப்பட்ட செலவினங்கள் மீது நாடாளுமன்றத்தில் விவாதிக்கலாமே தவிர வாக்கெடுப்பு நடத்த முடியாது."
    },
    # 6
    {
        "subtopic": "Form of Accounts (Article 150)",
        "stem_en": "Consider the following statements regarding Article 150 of the Constitution:\n1. The accounts of the Union and the States shall be kept in such form as the President prescribes.\n2. The President prescribes the form of accounts strictly on the advice of the Comptroller and Auditor General of India.\nWhich of the statements given above is/are correct?",
        "stem_ta": "அரசியலமைப்புச் சட்டம் சரத்து 150 குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. மத்திய மற்றும் மாநிலங்களின் கணக்குகள் குடியரசுத் தலைவர் பரிந்துரைக்கும் படிவத்தில் வைக்கப்பட வேண்டும்.\n2. இந்தியத் தலைமைத் தணிக்கையாளரின் ஆலோசனையின் பேரில் மட்டுமே குடியரசுத் தலைவர் கணக்குகளின் படிவத்தை நிர்ணயிக்கிறார்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("1 only", "1 மட்டும்"),
            ("2 only", "2 மட்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Both statements are correct. Article 150 (as amended by the 42nd and 44th Constitutional Amendments) mandates that the accounts of the Union and States shall be kept in such form as the President may, on the advice of the CAG, prescribe.",
        "exp_ta": "இரண்டு கூற்றுகளும் சரியானவை. சரத்து 150-ன் படி, சி.ஏ.ஜியின் ஆலோசனையின் பேரில் குடியரசுத் தலைவர் பரிந்துரைக்கும் படிவத்தில் மத்திய மற்றும் மாநில அரசுகளின் கணக்குகள் பராமரிக்கப்பட வேண்டும்.",
        "tip_en": "Article 150: President prescribes accounting forms ON THE ADVICE of the CAG.",
        "tip_ta": "சரத்து 150: சி.ஏ.ஜியின் ஆலோசனையின் பேரில் குடியரசுத் தலைவர் கணக்குப் படிவத்தை நிர்ணயிக்கிறார்.",
        "fact_en": "The 44th Amendment in 1978 substituted 'on the advice of' for 'after consultation with'.",
        "fact_ta": "1978-ல் 44வது திருத்தம் 'கலந்தாலோசித்த பிறகு' என்பதற்குப் பதிலாக 'ஆலோசனையின் பேரில்' என மாற்றியது."
    },
    # 7
    {
        "subtopic": "Submission of Reports (Article 151)",
        "stem_en": "Consider the following statements regarding the submission of CAG audit reports under Article 151:\n1. The reports relating to the accounts of the Union are submitted to the President, who causes them to be laid before each House of Parliament.\n2. The reports relating to the accounts of a State are submitted to the Chief Minister of the State, who places them before the Legislative Assembly.\nWhich of the statements given above is/are correct?",
        "stem_ta": "சரத்து 151-ன் கீழ் சி.ஏ.ஜி தணிக்கை அறிக்கைகளை சமர்ப்பித்தல் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. மத்திய அரசின் கணக்குகள் தொடர்பான அறிக்கைகள் குடியரசுத் தலைவரிடம் சமர்ப்பிக்கப்பட்டு, அவர் அவற்றை நாடாளுமன்றத்தின் இரு அவைகளிலும் வைக்கச் செய்கிறார்.\n2. ஒரு மாநிலத்தின் கணக்குகள் தொடர்பான அறிக்கைகள் மாநில முதலமைச்சரிடம் சமர்ப்பிக்கப்பட்டு, அவர் அவற்றைச் சட்டமன்றப் பேரவையில் சமர்ப்பிக்கிறார்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("1 only", "1 மட்டும்"),
            ("2 only", "2 மட்டும்"),
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Statement 1 is correct under Article 151(1). Statement 2 is incorrect because under Article 151(2), reports relating to a State are submitted to the Governor of the State, not to the Chief Minister.",
        "exp_ta": "கூற்று 1 சரத்து 151(1)-ன் கீழ் சரி. கூற்று 2 தவறு, ஏனெனில் சரத்து 151(2)-ன் படி மாநில அறிக்கைகள் ஆளுநரிடம் சமர்ப்பிக்கப்பட வேண்டுமே தவிர முதலமைச்சரிடம் அல்ல; ஆளுநரே அதைச் சட்டமன்றத்தில் வைக்கச் செய்கிறார்.",
        "tip_en": "Article 151(1): Reports on Union -> President -> Parliament. Article 151(2): Reports on States -> Governor -> State Legislature.",
        "tip_ta": "சரத்து 151(1): மத்திய அறிக்கை -> குடியரசுத் தலைவர் -> நாடாளுமன்றம். சரத்து 151(2): மாநில அறிக்கை -> ஆளுநர் -> சட்டமன்றம்.",
        "fact_en": "CAG submits three reports for Union: Appropriation Accounts, Finance Accounts, and Public Undertakings.",
        "fact_ta": "மத்திய அரசுக்காக ஒதுக்கீட்டுக் கணக்குகள், நிதிக் கணக்குகள் மற்றும் பொதுத்துறை நிறுவனங்கள் என 3 அறிக்கைகளை சி.ஏ.ஜி சமர்ப்பிக்கிறார்."
    },
    # 8
    {
        "subtopic": "CAG and Public Accounts Committee (PAC)",
        "stem_en": "Consider the following statements regarding the CAG and the Public Accounts Committee (PAC):\n1. The CAG acts as a guide, friend, and philosopher to the Public Accounts Committee of Parliament.\n2. The CAG is an elected voting member of the Public Accounts Committee.\nWhich of the statements given above is/are correct?",
        "stem_ta": "சி.ஏ.ஜி மற்றும் பொதுக் கணக்குக் குழு (PAC) குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. நாடாளுமன்றத்தின் பொதுக் கணக்குக் குழுவிற்கு சி.ஏ.ஜி வழிகாட்டியாகவும், நண்பராகவும், தத்துவஞானியாகவும் செயல்படுகிறார்.\n2. பொதுக் கணக்குக் குழுவில் வாக்களிக்கும் உரிமை கொண்ட தேர்ந்தெடுக்கப்பட்ட உறுப்பினராக சி.ஏ.ஜி உள்ளார்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("1 only", "1 மட்டும்"),
            ("2 only", "2 மட்டும்"),
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Statement 1 is correct. Statement 2 is incorrect because the CAG is not a member of Parliament or the PAC; he attends PAC meetings as an expert invitee to assist members in scrutinizing audit reports.",
        "exp_ta": "கூற்று 1 சரி. கூற்று 2 தவறு, ஏனெனில் சி.ஏ.ஜி நாடாளுமன்ற உறுப்பினரோ அல்லது PAC உறுப்பினரோ அல்ல; அவர் தணிக்கை அறிக்கைகளை ஆய்வு செய்ய உதவும் சிறப்பு அழைப்பாளராக மட்டுமே பங்கேற்கிறார்.",
        "tip_en": "CAG assists PAC, but is NOT a member and has NO voting rights.",
        "tip_ta": "சி.ஏ.ஜி பொதுக் கணக்குக் குழுவிற்கு உதவுகிறார்; ஆனால் அதில் உறுப்பினரோ வாக்களிக்கும் உரிமையோ கிடையாது.",
        "fact_en": "PAC examines whether moneys were applied to the purposes intended by Parliament without waste.",
        "fact_ta": "நாடாளுமன்றம் ஒதுக்கிய நோக்கத்திற்காகவே வீண் விரயமின்றி நிதி செலவிடப்பட்டதா என்பதை PAC ஆராய்கிறது."
    },
    # 9
    {
        "subtopic": "1976 Separation of Accounts and Audit",
        "stem_en": "Consider the following statements regarding the 1976 reform of accounting functions in India:\n1. In 1976, the CAG was relieved of the responsibility of compiling the accounts of the Union Government.\n2. Following the 1976 reform, the CAG was also completely relieved of the duty of compiling the accounts of all State Governments.\nWhich of the statements given above is/are correct?",
        "stem_ta": "1976 ஆம் ஆண்டு இந்தியாவில் கணக்கு வைக்கும் பணிகளில் செய்யப்பட்ட சீர்திருத்தம் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 1976-ல் மத்திய அரசின் கணக்குகளைத் தொகுக்கும் பொறுப்பிலிருந்து சி.ஏ.ஜி விடுவிக்கப்பட்டார்.\n2. 1976 சீர்திருத்தத்தைத் தொடர்ந்து, அனைத்து மாநில அரசுகளின் கணக்குகளைத் தொகுக்கும் பணியிலிருந்தும் சி.ஏ.ஜி முற்றிலும் விடுவிக்கப்பட்டார்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("1 only", "1 மட்டும்"),
            ("2 only", "2 மட்டும்"),
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Statement 1 is correct. Statement 2 is incorrect because the 1976 separation applied only to the Union Government; in almost all States, the CAG continues to compile and maintain state accounts through the Accountants General (A&E).",
        "exp_ta": "கூற்று 1 சரி. கூற்று 2 தவறு, ஏனெனில் 1976 சீர்திருத்தம் மத்திய அரசுக்கு மட்டுமே பொருந்தியது; பெரும்பாலான மாநிலங்களில் இன்றும் சி.ஏ.ஜியே கணக்குகளைத் தொகுத்து பராமரிக்கும் பணியைத் தொடர்ந்து செய்து வருகிறார்.",
        "tip_en": "Separation of accounts in 1976: Applies to Union. States still rely on CAG for compilation of accounts.",
        "tip_ta": "1976 கணக்குப் பிரிப்பு: மத்திய அரசுக்கு மட்டுமே பொருந்தும். மாநிலங்களில் சி.ஏ.ஜியே கணக்குகளைத் தொகுக்கிறார்.",
        "fact_en": "Controller General of Accounts (CGA) under Ministry of Finance manages Union Government accounting.",
        "fact_ta": "நிதி அமைச்சகத்தின் கீழ் உள்ள கணக்கு முதன்மைக் கட்டுப்பாட்டாளர் (CGA) மத்திய அரசின் கணக்குகளை நிர்வகிக்கிறார்."
    },
    # 10
    {
        "subtopic": "Audit of Autonomous Bodies (Section 14)",
        "stem_en": "Consider the following statements regarding Section 14 of the CAG (DPC) Act 1971:\n1. The CAG audits bodies substantially financed by government grants or loans.\n2. Substantial financing is defined where government grant/loan is not less than Rs. 25 lakhs and represents at least 75% of total expenditure.\nWhich of the statements given above is/are correct?",
        "stem_ta": "1971 சி.ஏ.ஜி சட்டத்தின் பிரிவு 14 குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. அரசு மானியங்கள் அல்லது கடன்கள் மூலம் கணிசமாக நிதியளிக்கப்படும் அமைப்புகளை சி.ஏ.ஜி தணிக்கை செய்கிறார்.\n2. அரசு மானியம்/கடன் ரூ. 25 லட்சத்திற்குக் குறையாமலும், மொத்த செலவில் குறைந்தது 75% ஆகவும் இருந்தால் அது கணிசமான நிதியுதவியாகக் கருதப்படுகிறது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("1 only", "1 மட்டும்"),
            ("2 only", "2 மட்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Both statements are correct under Section 14(1) of the 1971 Act, which sets the mandatory threshold for audit of substantially funded autonomous bodies at Rs. 25 lakhs and 75% of total expenditure.",
        "exp_ta": "இரண்டு கூற்றுகளும் சரியானவை. 1971 சட்டத்தின் பிரிவு 14(1)-ன் படி, ரூ. 25 லட்சத்திற்குக் குறையாமலும் மொத்த செலவில் 75% ஆகவும் மானியம் பெறும் அமைப்புகளை சி.ஏ.ஜி தணிக்கை செய்வது கட்டாயமாகும்.",
        "tip_en": "Section 14(1) criteria: Minimum Rs. 25 lakhs AND 75% of total expenditure.",
        "tip_ta": "பிரிவு 14(1) நிபந்தனை: குறைந்தபட்சம் ரூ. 25 லட்சம் மற்றும் மொத்த செலவில் 75%.",
        "fact_en": "Section 14(2) also enables audit of bodies receiving grants of Rs. 1 crore or more with prior sanction.",
        "fact_ta": "ரூ. 1 கோடிக்கு மேல் மானியம் பெறும் அமைப்புகளையும் முன் அனுமதியுடன் தணிக்கை செய்ய பிரிவு 14(2) வழிவகுக்கிறது."
    },
    # 11
    {
        "subtopic": "Audit of Government Companies",
        "stem_en": "Consider the following statements regarding CAG's audit of Government Companies:\n1. The statutory auditors of government companies are appointed by the CAG under the Companies Act.\n2. The CAG has the power to conduct a supplementary audit of such companies within 60 days of the statutory audit report.\nWhich of the statements given above is/are correct?",
        "stem_ta": "அரசு நிறுவனங்கள் மீதான சி.ஏ.ஜியின் தணிக்கை குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. நிறுவனங்கள் சட்டத்தின் கீழ் அரசு நிறுவனங்களுக்கான சட்டப்பூர்வ தணிக்கையாளர்களை சி.ஏ.ஜி நியமிக்கிறார்.\n2. சட்டப்பூர்வ தணிக்கை அறிக்கை கிடைத்த 60 நாட்களுக்குள் அத்தகைய நிறுவனங்களின் துணைத் தணிக்கையை நடத்தும் அதிகாரம் சி.ஏ.ஜிக்கு உண்டு.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("1 only", "1 மட்டும்"),
            ("2 only", "2 மட்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Both statements are correct. Under Section 143 of the Companies Act 2013 and Section 19(1) of the CAG Act, CAG appoints the chartered accountants for government companies and can conduct a supplementary audit within 60 days.",
        "exp_ta": "இரண்டு கூற்றுகளும் சரியானவை. நிறுவனங்கள் சட்டம் பிரிவு 143 மற்றும் சி.ஏ.ஜி சட்டத்தின்படி, அரசு நிறுவனங்களுக்கு பட்டயக் கணக்காளர்களை சி.ஏ.ஜி நியமிப்பதுடன், 60 நாட்களுக்குள் துணைத் தணிக்கை நடத்தவும் அதிகாரம் பெற்றுள்ளார்.",
        "tip_en": "Government Companies: CAG appoints auditor + conducts supplementary audit within 60 days.",
        "tip_ta": "அரசு நிறுவனங்கள்: தணிக்கையாளரை சி.ஏ.ஜி நியமிக்கிறார் + 60 நாட்களுக்குள் துணைத் தணிக்கை செய்கிறார்.",
        "fact_en": "CAG's comments on the supplementary audit must be placed before the company's AGM and Parliament.",
        "fact_ta": "துணைத் தணிக்கை மீதான சி.ஏ.ஜியின் குறிப்புகள் நிறுவனத்தின் பொதுக்குழு மற்றும் நாடாளுமன்றத்தில் வைக்கப்பட வேண்டும்."
    },
    # 12
    {
        "subtopic": "Audit Scope: Corporations Exempted",
        "stem_en": "Consider the following statements regarding the audit of public statutory corporations:\n1. Damodar Valley Corporation (DVC) and Oil and Natural Gas Corporation (ONGC) are audited exclusively by private auditors with zero CAG involvement.\n2. Reserve Bank of India (RBI) and Life Insurance Corporation (LIC) are audited exclusively by private auditors and are exempt from CAG's regular audit.\nWhich of the statements given above is/are correct?",
        "stem_ta": "பொது சட்டப்பூர்வ நிறுவனங்களின் தணிக்கை குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. தாமோதர் பள்ளத்தாக்கு கழகம் (DVC) மற்றும் எண்ணெய் மற்றும் இயற்கை எரிவாயுக் கழகம் (ONGC) ஆகியவை சி.ஏ.ஜியின் தலையீடின்றி முற்றிலும் தனியார் தணிக்கையாளர்களால் மட்டுமே தணிக்கை செய்யப்படுகின்றன.\n2. இந்திய ரிசர்வ் வங்கி (RBI) மற்றும் ஆயுள் காப்பீட்டுக் கழகம் (LIC) ஆகியவை முற்றிலும் தனியார் தணிக்கையாளர்களால் தணிக்கை செய்யப்படுகின்றன மற்றும் சி.ஏ.ஜியின் வழக்கமான தணிக்கையிலிருந்து விலக்கு பெற்றுள்ளன.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("2 only", "2 மட்டும்"),
            ("1 only", "1 மட்டும்"),
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Statement 1 is incorrect because DVC and ONGC are directly/supplementarily audited by the CAG. Statement 2 is correct because financial institutions like RBI, SBI, and LIC are audited exclusively by independent private auditors under their respective Acts without CAG involvement.",
        "exp_ta": "கூற்று 1 தவறு, ஏனெனில் DVC மற்றும் ONGC சி.ஏ.ஜியால் நேரடியாக/துணைத் தணிக்கை செய்யப்படுகின்றன. கூற்று 2 சரி, ஏனெனில் RBI, SBI மற்றும் LIC போன்ற நிதி நிறுவனங்கள் அவற்றின் சொந்தச் சட்டங்களின்படி தனியார் தணிக்கையாளர்களால் மட்டுமே தணிக்கை செய்யப்படுகின்றன.",
        "tip_en": "RBI, LIC, SBI: 100% private audit. DVC, AAI: CAG audit.",
        "tip_ta": "RBI, LIC, SBI: முற்றிலும் தனியார் தணிக்கை. DVC, AAI: சி.ஏ.ஜி தணிக்கை.",
        "fact_en": "The exemption of banking institutions preserves commercial flexibility and confidentiality.",
        "fact_ta": "வங்கி நிறுவனங்களுக்கு விலக்கு அளிப்பது வணிக ரகசியம் மற்றும் செயல்பாட்டு வேகத்தைப் பாதுகாக்கிறது."
    },
    # 13
    {
        "subtopic": "Net Proceeds Calculation (Article 279)",
        "stem_en": "Consider the following statements regarding the certification of 'net proceeds' of taxes under Article 279:\n1. The net proceeds of any tax or duty are ascertained and certified by the Comptroller and Auditor General of India.\n2. The certificate given by the CAG regarding net proceeds can be challenged and revised by the Union Finance Ministry.\nWhich of the statements given above is/are correct?",
        "stem_ta": "சரத்து 279-ன் கீழ் வரிகளின் 'நிகர வருமானம்' சான்றளிக்கப்படுவது குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. எந்தவொரு வரி அல்லது தீர்வையின் நிகர வருவாயும் இந்தியத் தலைமைக் கணக்குத் தணிக்கையாளரால் கணக்கிடப்பட்டு சான்றளிக்கப்படுகிறது.\n2. நிகர வருமானம் குறித்து சி.ஏ.ஜி வழங்கும் சான்றிதழை மத்திய நிதி அமைச்சகம் சவாலுக்கு உட்படுத்தி திருத்த முடியும்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("1 only", "1 மட்டும்"),
            ("2 only", "2 மட்டும்"),
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Statement 1 is correct. Statement 2 is incorrect because under Article 279(1), the certificate of the CAG regarding the net proceeds of any tax or duty is final and cannot be questioned by any authority.",
        "exp_ta": "கூற்று 1 சரி. கூற்று 2 தவறு, ஏனெனில் சரத்து 279(1)-ன் படி வரிகளின் நிகர வருமானம் குறித்த சி.ஏ.ஜியின் சான்றிதழ் இறுதியானது (final) மற்றும் யாராலும் கேள்வி கேட்க முடியாது.",
        "tip_en": "Article 279(1): CAG's certificate on net proceeds is FINAL and binding.",
        "tip_ta": "சரத்து 279(1): நிகர வருவாய் மீதான சி.ஏ.ஜியின் சான்றிதழ் இறுதியானது மற்றும் கட்டுப்படுத்தக்கூடியது.",
        "fact_en": "Net proceeds = Gross tax revenue collected minus cost of collection.",
        "fact_ta": "நிகர வருமானம் = வசூலிக்கப்பட்ட மொத்த வரி வருவாய் - வசூல் செய்வதற்கான செலவினம்."
    },
    # 14
    {
        "subtopic": "Indian Audit & Accounts Department (IA&AD)",
        "stem_en": "Consider the following statements regarding the Indian Audit and Accounts Department (IA&AD):\n1. The IA&AD functions directly under the administrative control of the Union Ministry of Finance.\n2. The CAG is the supreme head of the Indian Audit and Accounts Department.\nWhich of the statements given above is/are correct?",
        "stem_ta": "இந்திய தணிக்கை மற்றும் கணக்குத் துறை (IA&AD) குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. IA&AD மத்திய நிதி அமைச்சகத்தின் நேரடி நிர்வாகக் கட்டுப்பாட்டின் கீழ் இயங்குகிறது.\n2. இந்திய தணிக்கை மற்றும் கணக்குத் துறையின் உச்சபட்சத் தலைவர் சி.ஏ.ஜி ஆவார்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("2 only", "2 மட்டும்"),
            ("1 only", "1 மட்டும்"),
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Statement 1 is incorrect because the IA&AD is an independent institution headed by the CAG and is completely separate from the Ministry of Finance. Statement 2 is correct.",
        "exp_ta": "கூற்று 1 தவறு, ஏனெனில் IA&AD நிதி அமைச்சகத்தின் கீழ் இயங்காமல் சி.ஏ.ஜியின் கீழ் இயங்கும் ஒரு சுதந்திரமான தன்னாட்சி அமைப்பாகும். கூற்று 2 சரி.",
        "tip_en": "IA&AD is headed by CAG and is constitutionally autonomous from all executive ministries.",
        "tip_ta": "IA&AD துறை சி.ஏ.ஜியின் தலைமையில் இயங்குகிறது மற்றும் அமைச்சகங்களிலிருந்து தன்னாட்சி பெற்றது.",
        "fact_en": "Officers of IA&AS are recruited via the UPSC Civil Services Examination.",
        "fact_ta": "IA&AS அதிகாரிகள் UPSC குடிமைப் பணிகள் தேர்வு மூலம் தேர்ந்தெடுக்கப்படுகின்றனர்."
    },
    # 15
    {
        "subtopic": "Propriety Audit Nature",
        "stem_en": "Consider the following statements regarding 'Propriety Audit' conducted by the CAG:\n1. Propriety audit examines whether expenditure was incurred with wisdom, faithfulness, and public economy.\n2. Propriety audit is an explicit constitutional obligation mandatorily prescribed under Article 149.\nWhich of the statements given above is/are correct?",
        "stem_ta": "சி.ஏ.ஜியால் நடத்தப்படும் 'விவேக/நாணயத் தணிக்கை' (Propriety Audit) குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. செலவினமானது விவேகம், நேர்மை மற்றும் பொதுச் சிக்கனத்துடன் செய்யப்பட்டதா என்பதை நாணயத் தணிக்கை ஆராய்கிறது.\n2. நாணயத் தணிக்கை என்பது சரத்து 149-ன் கீழ் வெளிப்படையாகக் கட்டாயமாக்கப்பட்ட ஒரு அரசியலமைப்பு விதியாகும்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("1 only", "1 மட்டும்"),
            ("2 only", "2 மட்டும்"),
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Statement 1 is correct. Statement 2 is incorrect because propriety audit is discretionary and evolved through audit standards and conventions, whereas regulatory/legal audit is the direct statutory mandate.",
        "exp_ta": "கூற்று 1 சரி. கூற்று 2 தவறு, ஏனெனில் நாணயத் தணிக்கை என்பது தணிக்கை மரபுகள் மற்றும் வழிகாட்டுதல்கள் மூலம் உருவான ஒரு விருப்பத்திற்குரிய தணிக்கையே தவிர, சரத்து 149-ன் நேரடி கட்டாய விதியல்ல.",
        "tip_en": "Legal audit = Mandatory compliance check. Propriety audit = Discretionary check on wisdom and economy.",
        "tip_ta": "சட்டத் தணிக்கை = கட்டாய விதிமுறை சரிபார்ப்பு. நாணயத் தணிக்கை = விவேகம் மற்றும் சிக்கனத்தின் மீதான விருப்பத் தணிக்கை.",
        "fact_en": "Propriety audit questions wastefulness and extravagance even if legal sanctions exist.",
        "fact_ta": "சட்டப்பூர்வ அனுமதி இருந்தாலும் கூட வீண் விரயம் மற்றும் ஆடம்பரத்தை நாணயத் தணிக்கை கேள்வி கேட்கிறது."
    },
    # 16
    {
        "subtopic": "Secret Service Expenditure Audit",
        "stem_en": "Consider the following statements regarding CAG's audit of Secret Service Expenditure:\n1. The CAG cannot demand detailed vouchers for expenditures incurred on secret intelligence operations.\n2. The CAG must accept an administrative certificate from the competent authority stating that the money was spent under proper authority.\nWhich of the statements given above is/are correct?",
        "stem_ta": "ரகசிய சேவைச் செலவினங்கள் மீதான சி.ஏ.ஜி தணிக்கை குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. ரகசிய உளவுத்துறை நடவடிக்கைகளுக்கு செய்யப்பட்ட செலவுகளுக்கான விரிவான ரசீதுகளை சி.ஏ.ஜி கோர முடியாது.\n2. உரிய அதிகாரத்தின் கீழ் பணம் செலவிடப்பட்டது என்று தகுதிவாய்ந்த நிர்வாக அதிகாரி அளிக்கும் சான்றிதழை சி.ஏ.ஜி ஏற்றுக்கொள்ள வேண்டும்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("1 only", "1 மட்டும்"),
            ("2 only", "2 மட்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Both statements are correct. In secret service expenditure, CAG's audit is legally limited: audit accepts a certificate from the competent administrative authority confirming expenditure without demanding detailed vouchers.",
        "exp_ta": "இரண்டு கூற்றுகளும் சரியானவை. ரகசிய சேவைச் செலவினங்களில் சி.ஏ.ஜி விரிவான ரசீதுகளைக் கோர முடியாது; மாறாக தகுதிவாய்ந்த அதிகாரி அளிக்கும் சான்றிதழை மட்டுமே ஏற்றுக்கொள்கிறார்.",
        "tip_en": "Secret service expenditure is a known limitation on the scope of CAG's audit.",
        "tip_ta": "ரகசிய சேவைச் செலவு தணிக்கை என்பது சி.ஏ.ஜி தணிக்கை வரம்பிற்கு ஒரு விதிவிலக்காகும்.",
        "fact_en": "This protects national security sources while maintaining formal administrative oversight.",
        "fact_ta": "இது தேசியப் பாதுகாப்பு ரகசியங்களைப் பாதுகாக்கும் அதே வேளையில் நிர்வாகக் கண்காணிப்பையும் உறுதி செய்கிறது."
    },
    # 17
    {
        "subtopic": "Performance Audit & 3Es",
        "stem_en": "Consider the following statements regarding Performance Audits conducted by the CAG:\n1. Performance audit assesses the 3Es: Economy, Efficiency, and Effectiveness of government programs.\n2. Performance audit reports cannot be examined by the Public Accounts Committee.\nWhich of the statements given above is/are correct?",
        "stem_ta": "சி.ஏ.ஜி நடத்தும் செயல்திறன் தணிக்கை குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. செயல்திறன் தணிக்கையானது அரசுத் திட்டங்களின் சிக்கனம், செயல்திறன் மற்றும் செயலூக்கம் (3Es) ஆகியவற்றை மதிப்பிடுகிறது.\n2. செயல்திறன் தணிக்கை அறிக்கைகளை பொதுக் கணக்குக் குழு ஆய்வு செய்ய முடியாது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("1 only", "1 மட்டும்"),
            ("2 only", "2 மட்டும்"),
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Statement 1 is correct (Economy, Efficiency, Effectiveness). Statement 2 is incorrect because performance audit reports are presented to Parliament and rigorously examined by the Public Accounts Committee (PAC) or COPU.",
        "exp_ta": "கூற்று 1 சரி (சிக்கனம், செயல்திறன், செயலூக்கம்). கூற்று 2 தவறு, ஏனெனில் செயல்திறன் தணிக்கை அறிக்கைகள் நாடாளுமன்றத்தில் வைக்கப்பட்டு பொதுக் கணக்குக் குழுவால் (PAC) தீவிரமாக ஆய்வு செய்யப்படுகின்றன.",
        "tip_en": "All CAG reports tabled under Article 151 are examined by parliamentary financial committees.",
        "tip_ta": "சரத்து 151-ன் கீழ் வைக்கப்படும் அனைத்து அறிக்கைகளும் நாடாளுமன்ற நிதிக் குழுக்களால் ஆய்வு செய்யப்படுகின்றன.",
        "fact_en": "CAG's performance audit on 2G spectrum allocation led to landmark PAC discussions.",
        "fact_ta": "2G அலைக்கற்றை ஒதுக்கீடு மீதான சி.ஏ.ஜியின் செயல்திறன் தணிக்கை அறிக்கை வரலாற்றுச் சிறப்புமிக்க PAC விவாதங்களுக்கு வழிவகுத்தது."
    },
    # 18
    {
        "subtopic": "Comparison: British vs Indian CAG",
        "stem_en": "Consider the following statements comparing the Indian CAG with the Comptroller and Auditor General of the United Kingdom:\n1. In Britain, no money can be issued from the exchequer without the prior approval of the Comptroller.\n2. In India, the CAG has no ex-ante control over the issue of money from the Consolidated Fund and audits expenditure only post-facto.\nWhich of the statements given above is/are correct?",
        "stem_ta": "இந்திய சி.ஏ.ஜி மற்றும் பிரிட்டன் தலைமைக் கணக்குத் தணிக்கையாளரை ஒப்பிடும் பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. பிரிட்டனில், தணிக்கையாளரின் முன் அனுமதியின்றி கருவூலத்திலிருந்து எந்தப் பணமும் வெளியே வழங்கப்பட முடியாது.\n2. இந்தியாவில், திரட்டப்பட்ட நிதியிலிருந்து பணம் எடுப்பது மீது சி.ஏ.ஜிக்கு முன் கட்டுப்பாடு இல்லை மற்றும் அவர் செலவுக்குப் பின்னரே தணிக்கை செய்கிறார்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("1 only", "1 மட்டும்"),
            ("2 only", "2 மட்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Both statements are correct. In Britain, the CAG exercises control over the issue of public money (true Comptroller). In India, the executive withdraws money independently, and the CAG audits it ex-post (only an Auditor General).",
        "exp_ta": "இரண்டு கூற்றுகளும் சரியானவை. பிரிட்டனில் தணிக்கையாளர் கருவூலத்திலிருந்து பணம் வழங்கப்படுவதைக் கட்டுப்படுத்துகிறார்; ஆனால் இந்தியாவில் சி.ஏ.ஜி செலவுக்குப் பின்னரே தணிக்கை செய்கிறார்.",
        "tip_en": "UK CAG = Comptroller (ex-ante) + Auditor (ex-post). Indian CAG = Only Auditor (ex-post).",
        "tip_ta": "பிரிட்டன் சி.ஏ.ஜி = முன் அனுமதி + பின் தணிக்கை. இந்திய சி.ஏ.ஜி = பின் தணிக்கை மட்டுமே.",
        "fact_en": "The title 'Comptroller' in India is largely inherited from the British administrative lexicon.",
        "fact_ta": "'கம்ப்ரோலர்' (கட்டுப்பாட்டாளர்) என்ற பதவிப் பெயர் இந்தியாவில் பிரிட்டிஷ் நிர்வாக மரபிலிருந்து பெறப்பட்டதாகும்."
    },
    # 19
    {
        "subtopic": "Supreme Court Ruling on Telecom Revenue (2014)",
        "stem_en": "Consider the following statements regarding the Supreme Court's 2014 judgment on CAG audit of private telecom companies:\n1. The Supreme Court held that CAG can audit the revenue receipts of private telecom licensees sharing revenue with the government.\n2. The judgment was based on the Public Trust Doctrine regarding national natural resources like spectrum.\nWhich of the statements given above is/are correct?",
        "stem_ta": "தனியார் தொலைத்தொடர்பு நிறுவனங்கள் மீதான சி.ஏ.ஜி தணிக்கை குறித்த உச்ச நீதிமன்றத்தின் 2014 தீர்ப்பு தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. அரசுடன் வருவாயைப் பகிர்ந்துகொள்ளும் தனியார் தொலைத்தொடர்பு நிறுவனங்களின் வருவாய் வரவுகளை சி.ஏ.ஜி தணிக்கை செய்யலாம் என உச்ச நீதிமன்றம் தீர்ப்பளித்தது.\n2. அலைக்கற்றை போன்ற தேசிய இயற்கை வளங்கள் தொடர்பான 'பொது அறக்கட்டளைக் கோட்பாட்டின்' அடிப்படையில் இத்தீர்ப்பு வழங்கப்பட்டது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("1 only", "1 மட்டும்"),
            ("2 only", "2 மட்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Both statements are correct. In AUTSPI v. Union of India (2014), the Supreme Court ruled that since spectrum is a sovereign natural resource held in public trust, the CAG has constitutional power under Article 149 to audit revenue accounts of private licensees.",
        "exp_ta": "இரண்டு கூற்றுகளும் சரியானவை. 2014 உச்ச நீதிமன்றத் தீர்ப்பில், அலைக்கற்றை என்பது பொது அறக்கட்டளையின் கீழ் உள்ள இயற்கை வளம் என்பதால், அரசுடன் வருவாயைப் பகிரும் தனியார் நிறுவனங்களை சரத்து 149-ன் கீழ் தணிக்கை செய்ய சி.ஏ.ஜிக்கு அதிகாரம் உண்டு என உறுதி செய்யப்பட்டது.",
        "tip_en": "AUTSPI v. Union of India (2014): Revenue sharing private entities using public resources are subject to CAG audit.",
        "tip_ta": "2014 தீர்ப்பு: பொது வளங்களைப் பயன்படுத்தி அரசுடன் வருவாய் பகிரும் தனியார் நிறுவனங்கள் சி.ஏ.ஜி தணிக்கைக்கு உட்பட்டவை.",
        "fact_en": "The audit is restricted to verifying that the government received its lawful share of revenue.",
        "fact_ta": "அரசுக்குச் சேர வேண்டிய முறையான வருவாய்ப் பங்கு கிடைத்ததா என்பதை சரிபார்ப்பதற்கு மட்டுமே இத்தணிக்கை வரையறுக்கப்பட்டுள்ளது."
    },
    # 20
    {
        "subtopic": "Audit of Local Bodies and TGS",
        "stem_en": "Consider the following statements regarding CAG's role in local body finances:\n1. Under Technical Guidance and Supervision (TGS), CAG sets accounting and auditing standards for Panchayats and Urban Local Bodies.\n2. The CAG is constitutionally mandated under the 73rd and 74th Amendments to personally audit every village panchayat annually.\nWhich of the statements given above is/are correct?",
        "stem_ta": "உள்ளாட்சி நிதி அமைப்புகளில் சி.ஏ.ஜியின் பங்கு குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. தொழில்நுட்ப வழிகாட்டுதல் மற்றும் மேற்பார்வையின் (TGS) கீழ், பஞ்சாயத்துகள் மற்றும் நகர்ப்புற உள்ளாட்சி அமைப்புகளுக்கு சி.ஏ.ஜி கணக்கு மற்றும் தணிக்கைத் தரநிலைகளை நிர்ணயிக்கிறார்.\n2. ஒவ்வொரு கிராம பஞ்சாயத்தையும் ஆண்டுதோறும் நேரில் தணிக்கை செய்ய வேண்டும் என 73 மற்றும் 74வது திருத்தங்கள் சி.ஏ.ஜிக்கு அரசியலமைப்பு ரீதியாக உத்தரவிட்டுள்ளன.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("1 only", "1 மட்டும்"),
            ("2 only", "2 மட்டும்"),
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Statement 1 is correct under TGS recommended by Finance Commissions. Statement 2 is incorrect because primary audit of local bodies is the responsibility of State Local Fund Audit departments; CAG only exercises technical supervision and test audits.",
        "exp_ta": "கூற்று 1 சரி. கூற்று 2 தவறு, ஏனெனில் உள்ளாட்சி அமைப்புகளின் நேரடி முதன்மைத் தணிக்கை மாநில உள்ளாட்சி நிதி தணிக்கைத் துறையின் பொறுப்பாகும்; சி.ஏ.ஜி வழிகாட்டுதல் மற்றும் மாதிரித் தணிக்கை மட்டுமே செய்கிறார்.",
        "tip_en": "Local bodies audit: State Local Fund Audit conducts primary audit; CAG provides TGS.",
        "tip_ta": "உள்ளாட்சி தணிக்கை: மாநில உள்ளாட்சி நிதி தணிக்கை முதன்மை தணிக்கை செய்கிறது; சி.ஏ.ஜி தொழில்நுட்ப வழிகாட்டுதல் (TGS) தருகிறார்.",
        "fact_en": "11th Finance Commission first recommended CAG's supervisory role over local body accounts.",
        "fact_ta": "11வது நிதி ஆணையம் முதன்முதலில் உள்ளாட்சி கணக்குகளின் மீது சி.ஏ.ஜியின் மேற்பார்வைப் பங்கை பரிந்துரைத்தது."
    },
    # 21
    {
        "subtopic": "Oath of Office (Third Schedule)",
        "stem_en": "Consider the following statements regarding the oath of office of the CAG:\n1. The CAG takes an oath before the President or some person appointed on his behalf according to the Third Schedule.\n2. In his oath, the CAG swears to uphold the sovereignty and integrity of India and perform duties without fear or favour.\nWhich of the statements given above is/are correct?",
        "stem_ta": "சி.ஏ.ஜியின் பதவிப் பிரமாணம் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. மூன்றாவது அட்டவணையின்படி சி.ஏ.ஜி குடியரசுத் தலைவர் அல்லது அவரால் நியமிக்கப்பட்ட நபர் முன்னிலையில் பதவிப் பிரமாணம் செய்கிறார்.\n2. தனது பதவிப் பிரமாணத்தில், இந்தியாவின் இறையாண்மை மற்றும் ஒருமைப்பாட்டை நிலைநிறுத்துவதாகவும், பயம் அல்லது தயவின்றி கடமைகளை ஆற்றுவதாகவும் சி.ஏ.ஜி உறுதியளிக்கிறார்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("1 only", "1 மட்டும்"),
            ("2 only", "2 மட்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Both statements are correct. Article 148(2) mandates that the CAG before entering upon office shall make and subscribe an oath according to Form IV of the Third Schedule before the President.",
        "exp_ta": "இரண்டு கூற்றுகளும் சரியானவை. சரத்து 148(2)-ன் படி, சி.ஏ.ஜி பதவியேற்பதற்கு முன் மூன்றாவது அட்டவணையின் படிவம் IV-ன் படி குடியரசுத் தலைவர் முன் உறுதிமொழி ஏற்க வேண்டும்.",
        "tip_en": "CAG's oath: Under Third Schedule (Form IV), identical to Supreme Court Judges.",
        "tip_ta": "சி.ஏ.ஜியின் உறுதிமொழி: மூன்றாவது அட்டவணை (படிவம் IV), உச்ச நீதிமன்ற நீதிபதிகளுக்கு இணையானது.",
        "fact_en": "The oath emphasizes upholding the Constitution and the laws without fear or favour, affection or ill-will.",
        "fact_ta": "உறுதிமொழி அரசியலமைப்பு மற்றும் சட்டங்களை பயம், தயவு அல்லது விருப்பு வெறுப்பின்றி நிலைநிறுத்துவதை வலியுறுத்துகிறது."
    },
    # 22
    {
        "subtopic": "Section 18 Powers: Inspection and Records",
        "stem_en": "Consider the following statements regarding Section 18 of the CAG (DPC) Act 1971:\n1. The CAG has the power to inspect any office of accounts under the Union or a State.\n2. The CAG has the power to arrest public servants who refuse to submit financial documents.",
        "stem_ta": "1971 சி.ஏ.ஜி சட்டத்தின் பிரிவு 18 குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. மத்திய அல்லது மாநில அரசின் எந்தவொரு கணக்கு அலுவலகத்தையும் ஆய்வு செய்ய சி.ஏ.ஜிக்கு அதிகாரம் உண்டு.\n2. நிதி ஆவணங்களைச் சமர்ப்பிக்க மறுக்கும் அரசு ஊழியர்களைக் கைது செய்யும் அதிகாரம் சி.ஏ.ஜிக்கு உண்டு.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("1 only", "1 மட்டும்"),
            ("2 only", "2 மட்டும்"),
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Statement 1 is correct under Section 18. Statement 2 is incorrect because the CAG is an auditing and reporting authority with no police, prosecutorial, or arrest powers.",
        "exp_ta": "கூற்று 1 பிரிவு 18-ன் கீழ் சரி. கூற்று 2 தவறு, ஏனெனில் சி.ஏ.ஜி ஒரு தணிக்கை அதிகாரி மட்டுமே; அவருக்கு காவல் அல்லது கைது செய்யும் அதிகாரம் கிடையாது.",
        "tip_en": "CAG can inspect and demand records, but has NO arrest or punitive powers.",
        "tip_ta": "சி.ஏ.ஜி ஆவணங்களை ஆய்வு செய்து கோரலாம்; ஆனால் கைது செய்யும் அதிகாரம் கிடையாது.",
        "fact_en": "Non-production of records can be reported to Parliament or State Legislature as an audit impediment.",
        "fact_ta": "ஆவணங்கள் வழங்கப்படாவிட்டால் அது தணிக்கைத் தடையாக நாடாளுமன்றம் அல்லது சட்டமன்றத்தில் தெரிவிக்கப்படும்."
    },
    # 23
    {
        "subtopic": "Autonomous District Councils Audit (Sixth Schedule)",
        "stem_en": "Consider the following statements regarding the Sixth Schedule and the CAG:\n1. The accounts of Autonomous District Councils in tribal areas are audited by the CAG under Paragraph 7 of the Sixth Schedule.\n2. The audit reports of Autonomous District Councils are submitted to the Union Home Minister for approval.\nWhich of the statements given above is/are correct?",
        "stem_ta": "ஆறாவது அட்டவணை மற்றும் சி.ஏ.ஜி குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. பழங்குடியினர் பகுதிகளில் உள்ள தன்னாட்சி மாவட்டக் குழுக்களின் கணக்குகள் ஆறாவது அட்டவணையின் பத்தி 7-ன் கீழ் சி.ஏ.ஜியால் தணிக்கை செய்யப்படுகின்றன.\n2. தன்னாட்சி மாவட்டக் குழுக்களின் தணிக்கை அறிக்கைகள் மத்திய உள்துறை அமைச்சரிடம் ஒப்புதலுக்காக சமர்ப்பிக்கப்படுகின்றன.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("1 only", "1 மட்டும்"),
            ("2 only", "2 மட்டும்"),
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Statement 1 is correct. Statement 2 is incorrect because under Paragraph 7(2) of the Sixth Schedule, the reports of the CAG are submitted to the Governor of the concerned State, who causes them to be laid before the Council.",
        "exp_ta": "கூற்று 1 சரி. கூற்று 2 தவறு, ஏனெனில் ஆறாவது அட்டவணை பத்தி 7(2)-ன் படி சி.ஏ.ஜியின் அறிக்கைகள் சம்பந்தப்பட்ட மாநில ஆளுநரிடம் சமர்ப்பிக்கப்பட்டு, அவரால் மாவட்டக் குழுவின் முன் வைக்கப்படுகின்றன.",
        "tip_en": "Sixth Schedule District Councils: CAG audits accounts; reports submitted to the Governor.",
        "tip_ta": "ஆறாவது அட்டவணை மாவட்டக் குழுக்கள்: சி.ஏ.ஜி தணிக்கை செய்கிறார்; அறிக்கைகள் ஆளுநரிடம் அளிக்கப்படுகின்றன.",
        "fact_en": "Applies to tribal areas of Assam, Meghalaya, Tripura, and Mizoram.",
        "fact_ta": "அசாம், மேகாலயா, திரிபுரா மற்றும் மிசோரம் ஆகிய மாநிலங்களின் பழங்குடியினர் பகுதிகளுக்கு இது பொருந்தும்."
    },
    # 24
    {
        "subtopic": "CAG and Judicial Nature of Findings",
        "stem_en": "Consider the following statements regarding the legal weight of CAG audit reports in criminal trials:\n1. The findings and loss estimates in a CAG report constitute conclusive legal proof of guilt in a criminal court.\n2. A CAG report is an administrative audit evaluation that serves as material for parliamentary review and investigative agency probing.\nWhich of the statements given above is/are correct?",
        "stem_ta": "குற்றவியல் வழக்குகளில் சி.ஏ.ஜி தணிக்கை அறிக்கைகளின் சட்டப்பூர்வ அந்தஸ்து குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. சி.ஏ.ஜி அறிக்கையில் உள்ள கண்டுபிடிப்புகள் மற்றும் இழப்பு மதிப்பீடுகள் குற்றவியல் நீதிமன்றத்தில் குற்றத்தை நிரூபிக்கும் உறுதியான சட்ட ஆதாரமாகும்.\n2. சி.ஏ.ஜி அறிக்கை என்பது நாடாளுமன்ற ஆய்வுக்கும் புலனாய்வு அமைப்புகளின் விசாரணைக்கும் உதவும் ஒரு தணிக்கை மதிப்பீட்டு ஆவணமாகும்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("2 only", "2 மட்டும்"),
            ("1 only", "1 மட்டும்"),
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Statement 1 is incorrect because the Supreme Court has clarified that CAG reports do not constitute conclusive evidence of criminal guilt. Statement 2 is correct.",
        "exp_ta": "கூற்று 1 தவறு, ஏனெனில் உச்ச நீதிமன்றம் சி.ஏ.ஜி அறிக்கைகள் குற்றத்தை நிரூபிக்கும் நேரடி சாட்சியங்களாகாது என்று தெளிவுபடுத்தியுள்ளது. கூற்று 2 சரி.",
        "tip_en": "CAG reports indicate systemic irregularities; criminal liability must be independently investigated and proven.",
        "tip_ta": "சி.ஏ.ஜி அறிக்கைகள் முறைகேடுகளைச் சுட்டிக்காட்டுகின்றன; குற்றப் பொறுப்பு தனித்து சட்டப்படி நிரூபிக்கப்பட வேண்டும்.",
        "fact_en": "CBI and ED can use CAG reports as primary intelligence to initiate preliminary enquiries (PE).",
        "fact_ta": "சி.பி.ஐ மற்றும் அமலாக்கத்துறை சி.ஏ.ஜி அறிக்கைகளை முதற்கட்ட விசாரணையைத் தொடங்கப் பயன்படுத்தலாம்."
    },
    # 25
    {
        "subtopic": "Audit of Receipts (Section 16)",
        "stem_en": "Consider the following statements regarding the audit of receipts by the CAG under Section 16:\n1. The CAG audits all receipts payable into the Consolidated Fund of India and the Consolidated Fund of each State.\n2. The audit of receipts covers both tax revenues (such as GST, Customs, Income Tax) and non-tax revenues.\nWhich of the statements given above is/are correct?",
        "stem_ta": "பிரிவு 16-ன் கீழ் சி.ஏ.ஜியால் நடத்தப்படும் வரவுத் தணிக்கை குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இந்தியத் திரட்டப்பட்ட நிதி மற்றும் ஒவ்வொரு மாநில திரட்டப்பட்ட நிதிக்குச் சேர வேண்டிய அனைத்து வரவுகளையும் சி.ஏ.ஜி தணிக்கை செய்கிறார்.\n2. வரவுத் தணிக்கையானது வரி வருவாய்கள் (ஜி.எஸ்.டி, சுங்கம், வருமான வரி) மற்றும் வரி அல்லாத வருவாய்கள் இரண்டையுமே உள்ளடக்கியது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("1 only", "1 மட்டும்"),
            ("2 only", "2 மட்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Both statements are correct. Under Section 16 of the CAG Act 1971, CAG has the duty to audit all tax and non-tax receipts payable into the Consolidated Funds of the Union and States.",
        "exp_ta": "இரண்டு கூற்றுகளும் சரியானவை. 1971 சி.ஏ.ஜி சட்டத்தின் பிரிவு 16-ன் கீழ், மத்திய மற்றும் மாநில திரட்டப்பட்ட நிதிகளுக்குச் சேர வேண்டிய வரி மற்றும் வரி அல்லாத அனைத்து வரவுகளையும் தணிக்கை செய்வது சி.ஏ.ஜியின் கடமையாகும்.",
        "tip_en": "Section 16: Comprehensive audit of receipts ensuring no revenue leakage or illegal exemptions.",
        "tip_ta": "பிரிவு 16: வருவாய் கசிவு அல்லது சட்டவிரோத வரி விலக்குகளைத் தடுக்கும் விரிவான வரவுத் தணிக்கை.",
        "fact_en": "Receipt audit checks whether the assessment, collection, and allocation of revenue adhere to law.",
        "fact_ta": "மதிப்பீடு, வசூல் மற்றும் நிதி ஒதுக்கீடு ஆகியவை சட்டப்படி நடக்கிறதா என்பதை வரவுத் தணிக்கை சோதிக்கிறது."
    },
    # 26
    {
        "subtopic": "Service Conditions of IA&AD Staff (Article 148(5))",
        "stem_en": "Consider the following statements regarding Article 148(5) of the Constitution:\n1. The conditions of service of persons serving in the Indian Audit and Accounts Department are prescribed by rules made by the President.\n2. The President makes these service rules strictly after mandatory consultation with the CAG.\nWhich of the statements given above is/are correct?",
        "stem_ta": "அரசியலமைப்புச் சட்டம் சரத்து 148(5) குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இந்திய தணிக்கை மற்றும் கணக்குத் துறையில் பணியாற்றும் நபர்களின் சேவை நிபந்தனைகள் குடியரசுத் தலைவரால் விதிகளாக நிர்ணயிக்கப்படுகின்றன.\n2. குடியரசுத் தலைவர் இந்த சேவை விதிகளை கட்டாயமாக சி.ஏ.ஜியைக் கலந்தாலோசித்த பின்னரே உருவாக்குகிறார்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("1 only", "1 மட்டும்"),
            ("2 only", "2 மட்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Both statements are correct. Under Article 148(5), rules governing conditions of service of IA&AD personnel and administrative powers of the CAG are made by the President after consultation with the CAG.",
        "exp_ta": "இரண்டு கூற்றுகளும் சரியானவை. சரத்து 148(5)-ன் படி, IA&AD ஊழியர்களின் சேவை விதிகள் மற்றும் சி.ஏ.ஜியின் நிர்வாக அதிகாரங்கள் ஆகியவை சி.ஏ.ஜியைக் கலந்தாலோசித்த பின்னர் குடியரசுத் தலைவரால் உருவாக்கப்படுகின்றன.",
        "tip_en": "Article 148(5): Mandatory consultation with CAG protects staff independence from executive interference.",
        "tip_ta": "சரத்து 148(5): சி.ஏ.ஜியுடனான கட்டாயக் கலந்தாலோசனை தணிக்கைப் பணியாளர்களின் சுதந்திரத்தைப் பாதுகாக்கிறது.",
        "fact_en": "This ensures that the executive cannot arbitrarily alter audit staff recruitment or service conditions.",
        "fact_ta": "இது நிர்வாகத் துறை தன்னிச்சையாக தணிக்கை ஊழியர்களின் விதிகளை மாற்றுவதைத் தடுக்கிறது."
    },
    # 27
    {
        "subtopic": "Historical Evolution: Lord Canning to Constitution",
        "stem_en": "Consider the following statements regarding the historical evolution of the CAG in India:\n1. The office of the Auditor General was first established under Lord Canning in 1858 following the Government of India Act 1858.\n2. V. Narahari Rao served as the first Comptroller and Auditor General of independent India.\nWhich of the statements given above is/are correct?",
        "stem_ta": "இந்தியாவில் சி.ஏ.ஜியின் வரலாற்று வளர்ச்சி குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 1858 ஆம் ஆண்டின் இந்திய அரசுச் சட்டத்தைத் தொடர்ந்து 1858-ல் கானிங் பிரபுவின் கீழ் முதன்முதலில் தணிக்கைத் தலைவர் அலுவலகம் உருவாக்கப்பட்டது.\n2. வி. நரஹரி ராவ் சுதந்திர இந்தியாவின் முதல் தலைமைக் கணக்குத் தணிக்கையாளராகப் பணியாற்றினார்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("1 only", "1 மட்டும்"),
            ("2 only", "2 மட்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Both statements are correct. In 1858, Lord Canning created the office of the Accountant General, and Sir Edward Drummond was appointed the first Auditor General in 1860. In 1948, V. Narahari Rao became the first Indian CAG.",
        "exp_ta": "இரண்டு கூற்றுகளும் சரியானவை. 1858-ல் கானிங் பிரபு தணிக்கைத் தலைவர் அலுவலகத்தை உருவாக்கினார்; 1860-ல் எட்வர்ட் டிரம்மாண்ட் முதல் தணிக்கைத் தலைவரானார். 1948-ல் வி. நரஹரி ராவ் சுதந்திர இந்தியாவின் முதல் சி.ஏ.ஜியானார்.",
        "tip_en": "1858: Lord Canning sets up office. 1860: Sir Edward Drummond. 1948-54: V. Narahari Rao (first Indian CAG).",
        "tip_ta": "1858: கானிங் பிரபு அமைத்தார். 1860: எட்வர்ட் டிரம்மாண்ட். 1948-54: வி. நரஹரி ராவ் (முதல் இந்திய சி.ஏ.ஜி).",
        "fact_en": "The Government of India Act 1935 granted statutory status and independence to the Auditor General.",
        "fact_ta": "1935 இந்திய அரசுச் சட்டம் தணிக்கைத் தலைவருக்கு சட்டப்பூர்வ அந்தஸ்தையும் சுதந்திரத்தையும் வழங்கியது."
    },
    # 28
    {
        "subtopic": "Audit of Grants and Loans (Section 15)",
        "stem_en": "Consider the following statements regarding Section 15 of the CAG Act 1971:\n1. The CAG scrutinizes the procedures by which authorities satisfy themselves that conditions of specific purpose grants/loans are fulfilled.\n2. The CAG is strictly barred from inspecting the books and accounts of any non-governmental recipient of public grants.\nWhich of the statements given above is/are correct?",
        "stem_ta": "1971 சி.ஏ.ஜி சட்டத்தின் பிரிவு 15 குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. குறிப்பிட்ட நோக்கத்திற்கான மானியங்கள்/கடன்களின் நிபந்தனைகள் பூர்த்தி செய்யப்பட்டுள்ளனவா என்பதை அதிகாரிகள் சரிபார்க்கும் நடைமுறைகளை சி.ஏ.ஜி ஆய்வு செய்கிறார்.\n2. அரசு மானியங்களைப் பெறும் எந்தவொரு அரசு சாரா அமைப்பின் கணக்குப் புத்தகங்களையும் ஆய்வு செய்வதற்கு சி.ஏ.ஜிக்கு கடுமையான தடை உள்ளது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("1 only", "1 மட்டும்"),
            ("2 only", "2 மட்டும்"),
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Statement 1 is correct. Statement 2 is incorrect because Section 15 expressly gives the CAG the right of access to the books and accounts of any body or authority receiving specific grants/loans, unless expressly exempted.",
        "exp_ta": "கூற்று 1 சரி. கூற்று 2 தவறு, ஏனெனில் பிரிவு 15-ன் படி குறிப்பிட்ட மானியம் பெறும் எந்தவொரு அமைப்பின் கணக்குகளையும் ஆய்வு செய்ய சி.ஏ.ஜிக்கு சட்டப்பூர்வ அணுகல் உரிமை உண்டு.",
        "tip_en": "Section 15 ensures that public grant money is utilized for its intended purpose.",
        "tip_ta": "பிரிவு 15 பொது மானிய நிதி அதன் குறிப்பிட்ட நோக்கத்திற்காகப் பயன்படுத்தப்படுவதை உறுதி செய்கிறது.",
        "fact_en": "This enables tracking of grants disbursed to NGOs and autonomous educational societies.",
        "fact_ta": "தொண்டு நிறுவனங்கள் மற்றும் கல்விச் சங்கங்களுக்கு வழங்கப்படும் மானியங்களைக் கண்காணிக்க இது உதவுகிறது."
    },
    # 29
    {
        "subtopic": "Estimates Committee Relationship",
        "stem_en": "Consider the following statements regarding the CAG and parliamentary committees:\n1. The CAG assists both the Public Accounts Committee (PAC) and the Committee on Public Undertakings (COPU).\n2. The CAG has a statutory mandate to guide the Estimates Committee in budget policy formulation.\nWhich of the statements given above is/are correct?",
        "stem_ta": "சி.ஏ.ஜி மற்றும் நாடாளுமன்றக் குழுக்கள் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. பொதுக் கணக்குக் குழு (PAC) மற்றும் பொதுத்துறை நிறுவனங்களுக்கான குழு (COPU) ஆகிய இரண்டிற்கும் சி.ஏ.ஜி உதவுகிறார்.\n2. பட்ஜெட் கொள்கை உருவாக்கத்தில் மதிப்பீட்டுக் குழுவிற்கு வழிகாட்ட சி.ஏ.ஜிக்கு சட்டப்பூர்வ ஆணை உள்ளது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("1 only", "1 மட்டும்"),
            ("2 only", "2 மட்டும்"),
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Statement 1 is correct. Statement 2 is incorrect because the CAG has NO formal relationship with the Estimates Committee; the Estimates Committee evaluates budget estimates and policy economies before expenditure occurs.",
        "exp_ta": "கூற்று 1 சரி. கூற்று 2 தவறு, ஏனெனில் மதிப்பீட்டுக் குழுவிற்கும் சி.ஏ.ஜிக்கும் முறையான தொடர்பு இல்லை; மதிப்பீட்டுக் குழு கொள்கை சிக்கனங்களை முன்கூட்டியே ஆராய்கிறது.",
        "tip_en": "CAG assists PAC and COPU, but NOT the Estimates Committee.",
        "tip_ta": "சி.ஏ.ஜி PAC மற்றும் COPU-விற்கு உதவுகிறார்; ஆனால் மதிப்பீட்டுக் குழுவிற்கு அல்ல.",
        "fact_en": "The Estimates Committee has 30 members exclusively from Lok Sabha.",
        "fact_ta": "மதிப்பீட்டுக் குழு மக்களவையிலிருந்து மட்டுமே 30 உறுப்பினர்களைக் கொண்டுள்ளது."
    },
    # 30
    {
        "subtopic": "Cess and Reserve Funds Audit",
        "stem_en": "Consider the following statements regarding CAG's audit findings on cesses and surcharges:\n1. The CAG has repeatedly criticized the non-transfer of collected cess revenues into dedicated non-lapsable reserve funds.\n2. Under Article 271, surcharges and cesses collected by the Union are mandatorily distributed to the States through Finance Commission devolution.\nWhich of the statements given above is/are correct?",
        "stem_ta": "செஸ் மற்றும் கூடுதல் கட்டணங்கள் மீதான சி.ஏ.ஜியின் தணிக்கைக் கண்டுபிடிப்புகள் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. வசூலிக்கப்பட்ட செஸ் வருவாயை பிரத்யேக நிதிகளுக்கு மாற்றாமல் இருப்பதை சி.ஏ.ஜி தொடர்ந்து விமர்சித்துள்ளது.\n2. சரத்து 271-ன் கீழ், மத்திய அரசால் வசூலிக்கப்படும் கூடுதல் கட்டணங்கள் மற்றும் செஸ் தொகைகள் நிதி ஆணையப் பகிர்வு மூலம் கட்டாயமாக மாநிலங்களுக்குப் பகிர்ந்தளிக்கப்படுகின்றன.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("1 only", "1 மட்டும்"),
            ("2 only", "2 மட்டும்"),
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Statement 1 is correct. Statement 2 is incorrect because under Article 271, surcharges and cesses form part of the Consolidated Fund of India exclusively for Union purposes and are excluded from the divisible pool shared with States.",
        "exp_ta": "கூற்று 1 சரி. கூற்று 2 தவறு, ஏனெனில் சரத்து 271-ன் படி செஸ் மற்றும் கூடுதல் கட்டணங்கள் மத்திய அரசின் பயன்பாட்டிற்கானவை; அவை மாநிலங்களுடன் பகிரப்படும் பொது நிதித் தொகுப்பில் சேர்க்கப்படுவதில்லை.",
        "tip_en": "Cesses/surcharges: Not shareable with States under Article 271; must be transferred to dedicated reserve funds.",
        "tip_ta": "செஸ்/கூடுதல் கட்டணம்: சரத்து 271-ன் கீழ் மாநிலங்களுடன் பகிரப்படுவதில்லை; பிரத்யேக நிதிகளுக்கு மாற்றப்பட வேண்டும்.",
        "fact_en": "Retaining cess proceeds in CFI artificially deflates the fiscal deficit figure.",
        "fact_ta": "செஸ் நிதியை CFI-ல் வைத்திருப்பது நிதிப் பற்றாக்குறை அளவை செயற்கையாகக் குறைத்துக் காட்டுகிறது."
    },
    # 31
    {
        "subtopic": "International Standing: UN Board of Auditors",
        "stem_en": "Consider the following statements regarding the international role of the CAG of India:\n1. The CAG of India has served as a member and Chairman of the United Nations Board of Auditors.\n2. The CAG has served as the External Auditor of specialized UN agencies such as WHO, FAO, and IAEA.\nWhich of the statements given above is/are correct?",
        "stem_ta": "இந்திய சி.ஏ.ஜியின் சர்வதேசப் பங்கு குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இந்திய சி.ஏ.ஜி ஐக்கிய நாடுகள் தணிக்கையாளர் வாரியத்தின் உறுப்பினர் மற்றும் தலைவராகப் பணியாற்றியுள்ளார்.\n2. உலக சுகாதார நிறுவனம் (WHO), உணவு மற்றும் வேளாண்மை அமைப்பு (FAO), மற்றும் சர்வதேச அணுசக்தி முகமை (IAEA) போன்ற ஐ.நா அமைப்புகளின் வெளித் தணிக்கையாளராக சி.ஏ.ஜி பணியாற்றியுள்ளார்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("1 only", "1 மட்டும்"),
            ("2 only", "2 மட்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Both statements are correct. The CAG of India is globally recognized and has been repeatedly elected to the UN Board of Auditors and as External Auditor for prestigious multilateral organizations.",
        "exp_ta": "இரண்டு கூற்றுகளும் சரியானவை. இந்திய சி.ஏ.ஜி உலகளவில் அங்கீகரிக்கப்பட்டு, ஐ.நா தணிக்கையாளர் வாரியத்திலும், WHO, FAO போன்ற பல்வேறு முக்கிய அமைப்புகளின் வெளித் தணிக்கையாளராகவும் பணியாற்றியுள்ளார்.",
        "tip_en": "CAG represents India on global audit bodies including INTOSAI, ASOSAI, and the UN Board of Auditors.",
        "tip_ta": "INTOSAI, ASOSAI மற்றும் ஐ.நா தணிக்கையாளர் வாரியம் போன்ற உலகளாவிய அமைப்புகளில் சி.ஏ.ஜி இந்தியாவைப் பிரதிநிதித்துவப்படுத்துகிறார்.",
        "fact_en": "In September 2024, the CAG assumed the Chairmanship of ASOSAI for 2024-2027.",
        "fact_ta": "செப்டம்பர் 2024-ல் சி.ஏ.ஜி 2024-2027 காலகட்டத்திற்கான ASOSAI அமைப்பின் தலைவராகப் பொறுப்பேற்றார்."
    },
    # 32
    {
        "subtopic": "Environmental Auditing & iCED",
        "stem_en": "Consider the following statements regarding Environmental Auditing by the CAG:\n1. The CAG has established the International Centre for Environment Audit and Sustainable Development (iCED) in Jaipur.\n2. The CAG conducts environmental audits evaluating compliance with environmental protection acts and biodiversity preservation.\nWhich of the statements given above is/are correct?",
        "stem_ta": "சி.ஏ.ஜியின் சுற்றுச்சூழல் தணிக்கை குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. சி.ஏ.ஜி ஜெய்ப்பூரில் சுற்றுச்சூழல் தணிக்கை மற்றும் நிலையான வளர்ச்சிக்கான சர்வதேச மையத்தை (iCED) நிறுவியுள்ளார்.\n2. சுற்றுச்சூழல் பாதுகாப்புச் சட்டங்கள் மற்றும் பல்லுயிர் பாதுகாப்பை மதிப்பீடு செய்யும் சுற்றுச்சூழல் தணிக்கைகளை சி.ஏ.ஜி நடத்துகிறது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("1 only", "1 மட்டும்"),
            ("2 only", "2 மட்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Both statements are correct. The CAG conducts specialized environmental audits and established iCED in Jaipur, an INTOSAI-designated global training facility for environmental auditing.",
        "exp_ta": "இரண்டு கூற்றுகளும் சரியானவை. சி.ஏ.ஜி சிறப்பு சுற்றுச்சூழல் தணிக்கைகளை நடத்துகிறது மற்றும் ஜெய்ப்பூரில் உலகளாவிய பயிற்சி மையமான iCED-ஐ நிறுவியுள்ளது.",
        "tip_en": "iCED Jaipur is the premier global hub for training auditors in environmental governance.",
        "tip_ta": "ஜெய்ப்பூர் iCED சுற்றுச்சூழல் ஆளுகை தணிக்கையாளர்களுக்கான முதன்மை உலகளாவிய பயிற்சி மையமாகும்.",
        "fact_en": "CAG has conducted comprehensive audits on Ganga rejuvenation, air quality, and renewable energy.",
        "fact_ta": "கங்கை தூய்மைப்படுத்தல், காற்றின் தரம் மற்றும் புதுப்பிக்கத்தக்க ஆற்றல் குறித்து சி.ஏ.ஜி விரிவான தணிக்கைகளை நடத்தியுள்ளது."
    },
    # 33
    {
        "subtopic": "Article 148(3) Salary Disadvantage Clause",
        "stem_en": "Consider the following statements regarding Article 148(3) of the Constitution:\n1. The salary and service conditions of the CAG shall not be varied to his disadvantage after appointment.\n2. During a Financial Emergency under Article 360, the President has no power to reduce the salary of the CAG.\nWhich of the statements given above is/are correct?",
        "stem_ta": "அரசியலமைப்புச் சட்டம் சரத்து 148(3) குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. நியமனத்திற்குப் பிறகு சி.ஏ.ஜியின் ஊதியம் மற்றும் சேவை நிபந்தனைகள் அவருக்கு பாதகமாக மாற்றப்படக் கூடாது.\n2. சரத்து 360-ன் கீழ் நிதி அவசரநிலையின் போது கூட சி.ஏ.ஜியின் ஊதியத்தைக் குறைக்க குடியரசுத் தலைவருக்கு அதிகாரம் இல்லை.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("1 only", "1 மட்டும்"),
            ("2 only", "2 மட்டும்"),
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Statement 1 is correct under Article 148(3). Statement 2 is incorrect because during a Financial Emergency proclaimed under Article 360(4)(b), the President can direct salary reductions for all persons serving the Union, including Supreme Court judges and the CAG.",
        "exp_ta": "கூற்று 1 சரி. கூற்று 2 தவறு, ஏனெனில் சரத்து 360-ன் கீழ் நிதி அவசரநிலை பிரகடனப்படுத்தப்படும் போது, உச்ச நீதிமன்ற நீதிபதிகள் மற்றும் சி.ஏ.ஜி உள்ளிட்ட அனைவரது ஊதியத்தையும் குறைக்க குடியரசுத் தலைவருக்கு அதிகாரம் உண்டு.",
        "tip_en": "Salary cannot be varied to disadvantage EXCEPT during a Financial Emergency (Article 360).",
        "tip_ta": "நிதி அவசரநிலையின் போது தவிர (சரத்து 360), மற்ற நேரங்களில் ஊதியத்தை பாதகமாகக் குறைக்க முடியாது.",
        "fact_en": "India has never declared a Financial Emergency under Article 360 to date.",
        "fact_ta": "இந்தியாவில் இதுவரை சரத்து 360-ன் கீழ் நிதி அவசரநிலை அறிவிக்கப்பட்டதில்லை."
    },
    # 34
    {
        "subtopic": "Disinvestment Audit Focus",
        "stem_en": "Consider the following statements regarding the CAG audit of public sector disinvestment:\n1. The CAG examines whether valuation methodologies and reserve prices properly protected public interest.\n2. The CAG has the statutory authority to reverse and cancel disinvestment transactions concluded by the government.\nWhich of the statements given above is/are correct?",
        "stem_ta": "பொதுத்துறை பங்கு விலக்கல் (Disinvestment) மீதான சி.ஏ.ஜி தணிக்கை குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. மதிப்பீட்டு முறைகள் மற்றும் அடிப்படை விலை நிர்ணயம் ஆகியவை பொது நலனைப் பாதுகாத்தனவா என்பதை சி.ஏ.ஜி ஆராய்கிறது.\n2. அரசால் முடிக்கப்பட்ட பங்கு விலக்கல் பரிவர்த்தனைகளை ரத்து செய்யும் சட்டப்பூர்வ அதிகாரம் சி.ஏ.ஜிக்கு உண்டு.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("1 only", "1 மட்டும்"),
            ("2 only", "2 மட்டும்"),
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Statement 1 is correct. Statement 2 is incorrect because the CAG cannot cancel government contracts or disinvestment sales; audit reports can only highlight undervaluation and procedural lapses to Parliament.",
        "exp_ta": "கூற்று 1 சரி. கூற்று 2 தவறு, ஏனெனில் சி.ஏ.ஜியால் அரசு ஒப்பந்தங்களையோ பங்கு விற்பனையையோ ரத்து செய்ய முடியாது; குறைபாடுகளை நாடாளுமன்றத்திற்கு சுட்டிக்காட்ட மட்டுமே முடியும்.",
        "tip_en": "CAG audits financial propriety and valuation, but has no executive power to cancel commercial contracts.",
        "tip_ta": "சி.ஏ.ஜி மதிப்பீடு மற்றும் நிதி ஒழுங்கைத் தணிக்கை செய்கிறது; ஆனால் வணிக ஒப்பந்தங்களை ரத்து செய்யும் நிர்வாக அதிகாரம் இல்லை.",
        "fact_en": "Notable disinvestment audits include BALCO, Centaur Hotels, and ITDC properties.",
        "fact_ta": "பால்கோ மற்றும் சென்டார் ஹோட்டல் பங்கு விற்பனை மீதான தணிக்கைகள் குறிப்பிடத்தக்கவை."
    },
    # 35
    {
        "subtopic": "OIOS Digital Audit Platform",
        "stem_en": "Consider the following statements regarding digital auditing and modernization in the CAG office:\n1. One IA&AD One System (OIOS) is the digital enterprise platform used to manage end-to-end audit processes.\n2. The Centre for Data Management and Analytics (CDMA) was established by the CAG to leverage Big Data and Artificial Intelligence in audit.\nWhich of the statements given above is/are correct?",
        "stem_ta": "சி.ஏ.ஜி அலுவலகத்தின் டிஜிட்டல் தணிக்கை மற்றும் நவீனமயமாக்கல் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. One IA&AD One System (OIOS) என்பது முழுமையான தணிக்கை செயல்முறைகளை நிர்வகிக்கப் பயன்படும் டிஜிட்டல் தளமாகும்.\n2. தணிக்கையில் பெருந்தரவு (Big Data) மற்றும் செயற்கை நுண்ணறிவைப் (AI) பயன்படுத்த தரவு மேலாண்மை மற்றும் பகுப்பாய்வு மையத்தை (CDMA) சி.ஏ.ஜி அமைத்தது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("1 only", "1 மட்டும்"),
            ("2 only", "2 மட்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Both statements are correct. OIOS is the paperless end-to-end enterprise solution for IA&AD, and CDMA was established in 2016 to institutionalize big data analytics and AI-driven audit methodologies.",
        "exp_ta": "இரண்டு கூற்றுகளும் சரியானவை. OIOS என்பது காகிதமற்ற முழுமையான தணிக்கை மேலாண்மை தளமாகும்; CDMA மையம் 2016-ல் பெரிய தரவு மற்றும் AI தணிக்கைக்காக நிறுவப்பட்டது.",
        "tip_en": "Modern CAG operations rely on OIOS for workflow and CDMA for data-driven auditing.",
        "tip_ta": "நவீன சி.ஏ.ஜி செயல்பாடுகள் பணிப்பாய்வுக்கு OIOS தளத்தையும், தரவுத் தணிக்கைக்கு CDMA மையத்தையும் நம்பியுள்ளன.",
        "fact_en": "Digital auditing enables cross-verification of massive GST and direct benefit transfer datasets.",
        "fact_ta": "டிஜிட்டல் தணிக்கை ஜி.எஸ்.டி மற்றும் நேரடிப் பணப் பரிமாற்றங்களின் மிகப்பெரிய தரவுகளை சரிபார்க்க உதவுகிறது."
    },
    # 36
    {
        "subtopic": "Contingency Fund Scrutiny",
        "stem_en": "Consider the following statements regarding the Contingency Fund of India and the CAG:\n1. The Contingency Fund of India is held by the Finance Secretary on behalf of the President under Article 267.\n2. Advances taken from the Contingency Fund and their subsequent recoupment from the Consolidated Fund are subject to audit by the CAG.\nWhich of the statements given above is/are correct?",
        "stem_ta": "இந்திய அவசரகால நிதி மற்றும் சி.ஏ.ஜி குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. சரத்து 267-ன் கீழ் குடியரசுத் தலைவரின் சார்பில் நிதிச் செயலாளரால் இந்திய அவசரகால நிதி நிர்வகிக்கப்படுகிறது.\n2. அவசரகால நிதியிலிருந்து எடுக்கப்படும் முன்பணங்கள் மற்றும் திரட்டப்பட்ட நிதியிலிருந்து அவை மீண்டும் ஈடுசெய்யப்படுவது ஆகியவை சி.ஏ.ஜியின் தணிக்கைக்கு உட்பட்டவை.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("1 only", "1 மட்டும்"),
            ("2 only", "2 மட்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Both statements are correct. The Contingency Fund of India (Article 267) is placed at the disposal of the President, operated by the Finance Secretary, and all advances and recoupments are rigorously audited by the CAG under Section 13.",
        "exp_ta": "இரண்டு கூற்றுகளும் சரியானவை. அவசரகால நிதி சரத்து 267-ன் கீழ் குடியரசுத் தலைவரின் சார்பில் செயல்படுகிறது; அதிலிருந்து எடுக்கப்படும் முன்பணங்கள் மற்றும் ஈடுசெய்தல் ஆகியவை சி.ஏ.ஜியால் முழுமையாகத் தணிக்கை செய்யப்படுகின்றன.",
        "tip_en": "Advances from the Contingency Fund must be recouped through parliamentary supplementary appropriation.",
        "tip_ta": "அவசரகால நிதியிலிருந்து எடுக்கப்படும் தொகை நாடாளுமன்ற கூடுதல் ஒதுக்கீடு மூலம் மீண்டும் ஈடுசெய்யப்பட வேண்டும்.",
        "fact_en": "The corpus of the Contingency Fund of India was enhanced to Rs. 30,000 crore via the Finance Act 2021.",
        "fact_ta": "இந்திய அவசரகால நிதியின் இருப்பு 2021 நிதிச் சட்டம் மூலம் ரூ. 30,000 கோடியாக உயர்த்தப்பட்டது."
    },
    # 37
    {
        "subtopic": "Public Account Audit",
        "stem_en": "Consider the following statements regarding the Public Account of India under Article 266(2):\n1. All public moneys received by or on behalf of the Government of India (other than Consolidated Fund) are credited to the Public Account.\n2. Transactions in the Public Account (e.g., provident funds, small savings) are completely exempt from CAG audit.\nWhich of the statements given above is/are correct?",
        "stem_ta": "சரத்து 266(2)-ன் கீழ் உள்ள இந்தியப் பொதுக் கணக்கு (Public Account) குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. மத்திய அரசால் பெறப்படும் அனைத்து பொதுப் பணங்களும் (திரட்டப்பட்ட நிதி தவிர) பொதுக் கணக்கில் வரவு வைக்கப்படுகின்றன.\n2. பொதுக் கணக்கில் உள்ள பரிவர்த்தனைகள் (எ.கா. வருங்கால வைப்பு நிதி, சிறு சேமிப்பு) சி.ஏ.ஜி தணிக்கையிலிருந்து முற்றிலும் விலக்கு அளிக்கப்பட்டுள்ளன.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("1 only", "1 மட்டும்"),
            ("2 only", "2 மட்டும்"),
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Statement 1 is correct under Article 266(2). Statement 2 is incorrect because the CAG audits all transactions relating to debt, deposits, suspense, remittances, and provident funds in the Public Account under Section 13 of the 1971 Act.",
        "exp_ta": "கூற்று 1 சரத்து 266(2)-ன் படி சரி. கூற்று 2 தவறு, ஏனெனில் பொதுக் கணக்கில் உள்ள கடன், வைப்பு நிதி மற்றும் சேமிப்பு தொடர்பான அனைத்து பரிவர்த்தனைகளையும் 1971 சட்டத்தின் பிரிவு 13-ன் கீழ் சி.ஏ.ஜி தணிக்கை செய்கிறார்.",
        "tip_en": "CAG audits all three funds: Consolidated Fund, Contingency Fund, and Public Account.",
        "tip_ta": "சி.ஏ.ஜி மூன்று நிதிகளையுமே தணிக்கை செய்கிறார்: திரட்டப்பட்ட நிதி, அவசரகால நிதி, மற்றும் பொதுக் கணக்கு.",
        "fact_en": "Payments from the Public Account do not require prior parliamentary appropriation.",
        "fact_ta": "பொதுக் கணக்கிலிருந்து பணம் எடுக்க நாடாளுமன்றத்தின் முன் அனுமதி தேவையில்லை."
    },
    # 38
    {
        "subtopic": "Audit of Public-Private Partnerships (PPP)",
        "stem_en": "Consider the following statements regarding CAG's audit of Public-Private Partnership (PPP) projects:\n1. The CAG audits PPP concession agreements to verify whether revenue sharing and viability gap funding conform to rules.\n2. The CAG is empowered to take over the daily management and traffic toll collection of highway concessionaires.\nWhich of the statements given above is/are correct?",
        "stem_ta": "அரசு-தனியார் கூட்டு (PPP) திட்டங்கள் மீதான சி.ஏ.ஜி தணிக்கை குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. வருவாய்ப் பகிர்வு மற்றும் சாத்தியக்கூறு இடைவெளி நிதி (VGF) விதிகளுக்கு உட்பட்டுள்ளதா என்பதை சரிபார்க்க PPP ஒப்பந்தங்களை சி.ஏ.ஜி தணிக்கை செய்கிறார்.\n2. நெடுஞ்சாலை நிறுவனங்களின் தினசரி நிர்வாகத்தையும் சுங்கக் கட்டண வசூலையும் தன்வசப்படுத்த சி.ஏ.ஜிக்கு அதிகாரம் உண்டு.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("1 only", "1 மட்டும்"),
            ("2 only", "2 மட்டும்"),
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Statement 1 is correct. Statement 2 is incorrect because the CAG does not participate in project execution, operational toll collection, or management of private concessionaires.",
        "exp_ta": "கூற்று 1 சரி. கூற்று 2 தவறு, ஏனெனில் சி.ஏ.ஜி திட்ட நிர்வாகத்திலோ, சுங்கக் கட்டணம் வசூலிப்பதிலோ அல்லது நேரடி நிர்வாகத்திலோ தலையிட முடியாது.",
        "tip_en": "PPP audit examines whether the government's financial interests and sovereign assets are safeguarded.",
        "tip_ta": "PPP தணிக்கை அரசின் நிதி நலன்களும் அரசு சொத்துக்களும் பாதுகாக்கப்படுகின்றனவா என்பதை ஆராய்கிறது.",
        "fact_en": "Major PPP audits include Delhi Airport (DIAL) and Mumbai Airport (MIAL) concession agreements.",
        "fact_ta": "டெல்லி (DIAL) மற்றும் மும்பை (MIAL) விமான நிலைய ஒப்பந்தங்கள் முக்கிய PPP தணிக்கைகளாகும்."
    },
    # 39
    {
        "subtopic": "CAG (DPC) Act 1971 Amendment Power",
        "stem_en": "Consider the following statements regarding the regulation of duties and powers of the CAG under Article 149:\n1. Parliament has the constitutional power to make laws determining the duties and powers of the CAG.\n2. Until Parliament enacted the CAG (DPC) Act 1971, the Auditor General functioned under transitional provisions adapted from the Government of India Act 1935.\nWhich of the statements given above is/are correct?",
        "stem_ta": "சரத்து 149-ன் கீழ் சி.ஏ.ஜியின் பணிகள் மற்றும் அதிகாரங்களை ஒழுங்குபடுத்துவது குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. சி.ஏ.ஜியின் பணிகள் மற்றும் அதிகாரங்களை நிர்ணயிக்கும் சட்டங்களை இயற்ற நாடாளுமன்றத்திற்கு அரசியலமைப்பு அதிகாரம் உண்டு.\n2. 1971-ல் நாடாளுமன்றம் சி.ஏ.ஜி சட்டத்தை இயற்றும் வரை, 1935 இந்திய அரசுச் சட்டத்தின் தழுவல் விதிகளின் கீழேயே தணிக்கைத் தலைவர் செயல்பட்டார்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("1 only", "1 மட்டும்"),
            ("2 only", "2 மட்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Both statements are correct. Article 149 empowers Parliament to prescribe the duties and powers of the CAG. Parliament enacted the landmark CAG (DPC) Act in 1971; until then, the 1935 Act framework served as the transitional law.",
        "exp_ta": "இரண்டு கூற்றுகளும் சரியானவை. சரத்து 149 நாடாளுமன்றத்திற்கு அதிகாரங்களை வகுக்க அதிகாரம் அளிக்கிறது; 1971-ல் சட்டம் இயற்றப்படும் வரை 1935 சட்டத்தின் தழுவல் விதிகளே நடைமுறையில் இருந்தன.",
        "tip_en": "Article 149 leaves the specification of CAG duties and powers to parliamentary legislation.",
        "tip_ta": "சரத்து 149 சி.ஏ.ஜியின் பணிகள் மற்றும் அதிகாரங்களை நிர்ணயிக்கும் உரிமையை நாடாளுமன்றச் சட்டத்திற்கு விட்டுவிடுகிறது.",
        "fact_en": "The CAG Act of 1971 was amended in 1976 to separate accounts from audit at the Union level.",
        "fact_ta": "1971 ஆம் ஆண்டு சட்டம் 1976-ல் மத்திய அரசில் கணக்கைத் தணிக்கையிலிருந்து பிரிக்க திருத்தப்பட்டது."
    },
    # 40
    {
        "subtopic": "Appropriation Accounts vs Finance Accounts",
        "stem_en": "Consider the following statements regarding the annual accounts audited by the CAG:\n1. Appropriation Accounts compare actual expenditure with the voted budget grants authorized by Parliament.\n2. Finance Accounts present a comprehensive statement of the annual receipts, disbursements, and public debt of the government.\nWhich of the statements given above is/are correct?",
        "stem_ta": "சி.ஏ.ஜியால் தணிக்கை செய்யப்படும் வருடாந்திர கணக்குகள் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. ஒதுக்கீட்டுக் கணக்குகள் நாடாளுமன்றத்தால் வாக்களிக்கப்பட்ட பட்ஜெட் மானியங்களுடன் உண்மையான செலவினங்களை ஒப்பிடுகின்றன.\n2. நிதிக் கணக்குகள் அரசின் வருடாந்திர வரவுகள், செலவுகள் மற்றும் பொதுக்கடன்கள் பற்றிய விரிவான அறிக்கையை முன்வைக்கின்றன.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("1 only", "1 மட்டும்"),
            ("2 only", "2 மட்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Both statements are correct. Appropriation Accounts focus on legislative grant compliance, while Finance Accounts present the overall financial balance sheet of receipts, revenue/capital spend, and debt.",
        "exp_ta": "இரண்டு கூற்றுகளும் சரியானவை. ஒதுக்கீட்டுக் கணக்குகள் சட்டமன்ற மானியங்களை ஒப்பிடுகின்றன; நிதிக் கணக்குகள் அரசின் ஒட்டுமொத்த வரவு, செலவு மற்றும் கடன் நிலவரங்களை விவரிக்கின்றன.",
        "tip_en": "Appropriation Accounts = Voted Grants vs Expenditure. Finance Accounts = Government's complete balance sheet.",
        "tip_ta": "ஒதுக்கீட்டுக் கணக்கு = அங்கீகரிக்கப்பட்ட மானியம் vs செலவு. நிதிக் கணக்கு = அரசின் முழுமையான நிதி நிலை அறிக்கை.",
        "fact_en": "Both sets of accounts are prepared for both the Union and each of the State Governments.",
        "fact_ta": "மத்திய அரசு மற்றும் ஒவ்வொரு மாநில அரசிற்கும் இவ்விரண்டு கணக்குகளும் தயாரிக்கப்படுகின்றன."
    },
    # 41
    {
        "subtopic": "Action Taken Notes (ATNs)",
        "stem_en": "Consider the following statements regarding executive follow-up on CAG audit reports:\n1. Ministries must submit Action Taken Notes (ATNs) to parliamentary committees on paragraphs included in CAG reports.\n2. The CAG is empowered to impose punitive pay cuts on civil servants whose departments fail to submit ATNs.\nWhich of the statements given above is/are correct?",
        "stem_ta": "சி.ஏ.ஜி தணிக்கை அறிக்கைகள் மீதான நிர்வாக நடவடிக்கைகள் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. சி.ஏ.ஜி அறிக்கைகளில் உள்ள பத்திகள் மீது அமைச்சகங்கள் நாடாளுமன்றக் குழுக்களுக்கு நடவடிக்கை குறிப்புகளை (ATNs) சமர்ப்பிக்க வேண்டும்.\n2. ATN சமர்ப்பிக்கத் தவறும் அரசு ஊழியர்களுக்கு ஊதியக் குறைப்பு தண்டனை விதிக்க சி.ஏ.ஜிக்கு அதிகாரம் உண்டு.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("1 only", "1 மட்டும்"),
            ("2 only", "2 மட்டும்"),
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Statement 1 is correct. Statement 2 is incorrect because the CAG cannot punish or reduce the pay of civil servants; disciplinary action is strictly an executive prerogative overseen by Parliament.",
        "exp_ta": "கூற்று 1 சரி. கூற்று 2 தவறு, ஏனெனில் சி.ஏ.ஜி அதிகாரிகளுக்கு தண்டனை வழங்கவோ ஊதியத்தைக் குறைக்கவோ முடியாது; அது நாடாளுமன்றத்தின் மேற்பார்வையில் நிர்வாகத்தின் பொறுப்பாகும்.",
        "tip_en": "CAG assists PAC in vetting ATNs, but disciplinary punishment is an executive power.",
        "tip_ta": "ATN-களை ஆய்வு செய்ய சி.ஏ.ஜி PAC-க்கு உதவுகிறார்; ஆனால் தண்டனை வழங்கும் அதிகாரம் நிர்வாகத்திற்கே உண்டு.",
        "fact_en": "The PAC can summon Departmental Secretaries to explain unexplained audit delays.",
        "fact_ta": "விளக்கமளிக்கப்படாத தணிக்கைத் தாமதங்களுக்கு துறைச் செயலாளர்களை நேரில் அழைக்க PAC-க்கு அதிகாரம் உண்டு."
    },
    # 42
    {
        "subtopic": "Section 20 - Audit of Other Authorities",
        "stem_en": "Consider the following statements regarding Section 20 of the CAG Act 1971:\n1. The President or Governor may entrust the audit of any body or authority to the CAG in the public interest.\n2. Such entrustment can only be made after consultation with the CAG and giving reasonable opportunity to the body concerned.\nWhich of the statements given above is/are correct?",
        "stem_ta": "1971 சி.ஏ.ஜி சட்டத்தின் பிரிவு 20 குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. பொது நலன் கருதி குடியரசுத் தலைவர் அல்லது ஆளுநர் எந்தவொரு அமைப்பின் தணிக்கையையும் சி.ஏ.ஜியிடம் ஒப்படைக்கலாம்.\n2. சி.ஏ.ஜியுடன் கலந்தாலோசித்து, சம்பந்தப்பட்ட அமைப்பிற்கு நியாயமான வாய்ப்பளித்த பின்னரே அவ்வாறு ஒப்படைக்க முடியும்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("1 only", "1 மட்டும்"),
            ("2 only", "2 மட்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Both statements are correct under Section 20(1) and 20(2) of the CAG (DPC) Act 1971.",
        "exp_ta": "இரண்டு கூற்றுகளும் சரியானவை. 1971 சி.ஏ.ஜி சட்டத்தின் பிரிவு 20(1) மற்றும் 20(2)-ன் கீழ் பொது நலன் கருதி சி.ஏ.ஜியிடம் கலந்தாலோசித்து பிற அமைப்புகளின் தணிக்கை ஒப்படைக்கப்படலாம்.",
        "tip_en": "Section 20: Audit of bodies outside standard mandate on request of President/Governor.",
        "tip_ta": "பிரிவு 20: குடியரசுத் தலைவர்/ஆளுநரின் கோரிக்கையின் பேரில் பிற அமைப்புகளின் தணிக்கையை மேற்கொள்ளுதல்.",
        "fact_en": "Procedural fairness requires giving the entity a chance to show cause before entrustment.",
        "fact_ta": "தணிக்கையை ஒப்படைக்கும் முன் சம்பந்தப்பட்ட அமைப்பிற்கு விளக்கம் அளிக்க வாய்ப்பளிப்பது அவசியமாகும்."
    },
    # 43
    {
        "subtopic": "Stores and Stock Audit (Section 17)",
        "stem_en": "Consider the following statements regarding Section 17 of the CAG Act 1971:\n1. The CAG has authority to audit and report on the accounts of stores and stock kept in any office or department of the Union or a State.\n2. Stores audit examines physical losses, unserviceable accumulations, and adherence to purchase rules.\nWhich of the statements given above is/are correct?",
        "stem_ta": "1971 சி.ஏ.ஜி சட்டத்தின் பிரிவு 17 குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. மத்திய அல்லது மாநில அரசின் எந்தவொரு அலுவலகம் அல்லது துறையிலும் வைக்கப்பட்டுள்ள சரக்குகள் மற்றும் இருப்புக் கணக்குகளைத் தணிக்கை செய்ய சி.ஏ.ஜிக்கு அதிகாரம் உண்டு.\n2. சரக்குத் தணிக்கையானது சேத இழப்புகள், தேவையற்ற பொருட்கள் தேங்குதல் மற்றும் கொள்முதல் விதிகள் பின்பற்றப்படுவதை ஆராய்கிறது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("1 only", "1 மட்டும்"),
            ("2 only", "2 மட்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Both statements are correct under Section 17, which covers inventory management, avoidance of wasteful accumulation, and compliance with procurement guidelines.",
        "exp_ta": "இரண்டு கூற்றுகளும் சரியானவை. பிரிவு 17-ன் படி, அரசுத் துறைகளில் சரக்குகள் மற்றும் இருப்புக் கணக்குகளைத் தணிக்கை செய்து அறிக்கை அளிக்க சி.ஏ.ஜிக்கு அதிகாரம் உண்டு.",
        "tip_en": "Section 17: Stores and stock audit in defence, railways, health, and civil departments.",
        "tip_ta": "பிரிவு 17: பாதுகாப்பு, ரயில்வே, சுகாதாரம் போன்ற துறைகளில் சரக்கு மற்றும் இருப்புக் கணக்குத் தணிக்கை.",
        "fact_en": "Stores audit often uncovers critical shortages or expired medicines in public hospitals.",
        "fact_ta": "சரக்குத் தணிக்கை அரசு மருத்துவமனைகளில் மருந்துப் பற்றாக்குறை அல்லது காலாவதியான மருந்துகளை வெளிக்கொணர்கிறது."
    },
    # 44
    {
        "subtopic": "Audit of Autonomous Educational Institutions",
        "stem_en": "Consider the following statements regarding the audit of Central Universities, IITs, and AIIMS:\n1. The CAG audits the annual accounts of central autonomous higher educational institutions substantially funded by Union grants.\n2. The CAG submits Separate Audit Reports (SARs) for each autonomous institution to be placed in Parliament.\nWhich of the statements given above is/are correct?",
        "stem_ta": "மத்தியப் பல்கலைக்கழகங்கள், ஐ.ஐ.டி மற்றும் எய்ம்ஸ் தணிக்கை குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. மத்திய அரசு மானியங்களால் கணிசமாக நிதியளிக்கப்படும் தன்னாட்சி உயர் கல்வி நிறுவனங்களின் ஆண்டு கணக்குகளை சி.ஏ.ஜி தணிக்கை செய்கிறது.\n2. ஒவ்வொரு தன்னாட்சி நிறுவனத்திற்கும் தனித் தணிக்கை அறிக்கைகளை (SARs) சி.ஏ.ஜி தயாரித்து நாடாளுமன்றத்தில் வைக்கச் செய்கிறது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("1 only", "1 மட்டும்"),
            ("2 only", "2 மட்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Both statements are correct. Autonomous higher educational institutions receiving major grants under Section 14/19(2) are audited by the CAG, and Separate Audit Reports (SARs) are tabled annually in Parliament.",
        "exp_ta": "இரண்டு கூற்றுகளும் சரியானவை. மத்திய மானியங்களைப் பெறும் உயர் கல்வி நிறுவனங்கள் சி.ஏ.ஜியால் தணிக்கை செய்யப்பட்டு, அவற்றுக்கான தனித் தணிக்கை அறிக்கைகள் (SARs) நாடாளுமன்றத்தில் சமர்ப்பிக்கப்படுகின்றன.",
        "tip_en": "Separate Audit Reports (SARs) are specific audit products for autonomous institutions.",
        "tip_ta": "தனித் தணிக்கை அறிக்கைகள் (SARs) தன்னாட்சி நிறுவனங்களுக்கான பிரத்யேக தணிக்கை ஆவணங்களாகும்.",
        "fact_en": "SARs highlight utilization certificate delays and unspent grant balances.",
        "fact_ta": "SAR அறிக்கைகள் பயன்பாட்டுச் சான்றிதழ் தாமதங்கள் மற்றும் செலவிடப்படாத மானிய இருப்புகளைச் சுட்டிக்காட்டுகின்றன."
    },
    # 45
    {
        "subtopic": "Constituent Assembly Views: Ambedkar vs Santhanam",
        "stem_en": "Consider the following statements regarding the Constituent Assembly debates on the CAG:\n1. Dr. B.R. Ambedkar regarded the CAG as potentially the most important officer in the Constitution of India.\n2. K. Santhanam pointed out that the officer is essentially an 'Auditor General' rather than a true 'Comptroller'.\nWhich of the statements given above is/are correct?",
        "stem_ta": "சி.ஏ.ஜி குறித்த அரசியலமைப்பு நிர்ணய சபை விவாதங்கள் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. டாக்டர் பி.ஆர். அம்பேத்கர் சி.ஏ.ஜியை இந்திய அரசியலமைப்பின் மிக முக்கியமான அதிகாரியாகக் கருதினார்.\n2. கே. சந்தானம் இப்பொறுப்பு உண்மையான 'கட்டுப்பாட்டாளர்' என்பதை விட அடிப்படையில் ஒரு 'தணிக்கைத் தலைவர்' மட்டுமே என்று சுட்டிக்காட்டினார்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("1 only", "1 மட்டும்"),
            ("2 only", "2 மட்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Both statements are correct. Dr. Ambedkar emphasized CAG's primacy among constitutional watchdogs, while K. Santhanam astutely noted that without ex-ante control over money issue, the title 'Comptroller' was a misnomer.",
        "exp_ta": "இரண்டு கூற்றுகளும் சரியானவை. டாக்டர் அம்பேத்கர் சி.ஏ.ஜி பதவியை மிக முக்கியமான அரசியலமைப்பு அமைப்பாகக் கருதினார்; அதே சமயம் முன் அனுமதி அதிகாரம் இல்லாததால் 'கட்டுப்பாட்டாளர்' என்பது பொருத்தமற்றது என கே. சந்தானம் குறிப்பிட்டார்.",
        "tip_en": "Ambedkar: Most important officer. Santhanam: An Auditor General, not a Comptroller.",
        "tip_ta": "அம்பேத்கர்: மிக முக்கியமான அதிகாரி. சந்தானம்: கட்டுப்பாட்டாளர் அல்ல, தணிக்கைத் தலைவர் மட்டுமே.",
        "fact_en": "The Constituent Assembly rejected amendments proposing a multi-member Audit Commission.",
        "fact_ta": "பல உறுப்பினர்களைக் கொண்ட தணிக்கை ஆணையத்தை அமைக்கக் கோரிய திருத்தங்களை நிர்ணய சபை நிராகரித்தது."
    },
    # 46
    {
        "subtopic": "Section 21 - Delegation of Powers",
        "stem_en": "Consider the following statements regarding Section 21 of the CAG Act 1971:\n1. Any power exercisable by the CAG under the Act may be exercised by such officer of his department as authorized by him.\n2. The CAG can delegate his power to sign the final audit report submitted to the President to a private chartered accountant.\nWhich of the statements given above is/are correct?",
        "stem_ta": "1971 சி.ஏ.ஜி சட்டத்தின் பிரிவு 21 குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. சட்டத்தின் கீழ் சி.ஏ.ஜியால் செயல்படுத்தக்கூடிய எந்தவொரு அதிகாரமும் அவரால் அங்கீகரிக்கப்பட்ட தணிக்கைத் துறை அதிகாரியால் செயல்படுத்தப்படலாம்.\n2. குடியரசுத் தலைவரிடம் சமர்ப்பிக்கப்படும் இறுதி தணிக்கை அறிக்கையில் கையொப்பமிடும் அதிகாரத்தை ஒரு தனியார் பட்டயக் கணக்காளருக்கு சி.ஏ.ஜி வழங்க முடியும்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("1 only", "1 மட்டும்"),
            ("2 only", "2 மட்டும்"),
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Statement 1 is correct under Section 21. Statement 2 is incorrect because the constitutional report submitted to the President/Governor under Article 151 must be authenticated under the personal authority of the CAG, not private individuals.",
        "exp_ta": "கூற்று 1 சரி. கூற்று 2 தவறு, ஏனெனில் சரத்து 151-ன் கீழ் குடியரசுத் தலைவர்/ஆளுநரிடம் சமர்ப்பிக்கப்படும் அரசியலமைப்பு அறிக்கைகள் சி.ஏ.ஜியின் தனிப்பட்ட அதிகாரத்தின் கீழேயே சமர்ப்பிக்கப்பட வேண்டும்.",
        "tip_en": "Section 21 enables institutional functioning through Principal Accountants General and Directors General.",
        "tip_ta": "பிரிவு 21 முதன்மை கணக்குத் தலைவர்கள் மற்றும் இயக்குநர்கள் மூலம் துறையின் செயல்பாட்டை உறுதி செய்கிறது.",
        "fact_en": "Field inspections and draft paragraphs are routinely finalized by delegated IA&AD officers.",
        "fact_ta": "கள ஆய்வுகள் மற்றும் வரைவு தணிக்கைப் பத்திகள் துறை அதிகாரிகளால் இறுதி செய்யப்படுகின்றன."
    },
    # 47
    {
        "subtopic": "Separation of Accounts in States Exception",
        "stem_en": "Consider the following statements regarding state account compilation:\n1. Section 10 of the 1971 Act empowers the President, after consultation with the Governor, to relieve the CAG from compiling accounts of a State.\n2. As of date, all 28 Indian States have fully separated their accounting cadres from the CAG.\nWhich of the statements given above is/are correct?",
        "stem_ta": "மாநில கணக்குத் தொகுப்பு குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 1971 சட்டத்தின் பிரிவு 10-ன் படி, ஆளுநரைக் கலந்தாலோசித்த பின்னர் ஒரு மாநிலத்தின் கணக்குகளைத் தொகுப்பதிலிருந்து சி.ஏ.ஜியை விடுவிக்க குடியரசுத் தலைவருக்கு அதிகாரம் உண்டு.\n2. தற்போதைய நிலவரப்படி, அனைத்து 28 இந்திய மாநிலங்களும் தங்கள் கணக்குப் பணிகளை சி.ஏ.ஜியிடமிருந்து முழுமையாகப் பிரித்துவிட்டன.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("1 only", "1 மட்டும்"),
            ("2 only", "2 மட்டும்"),
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Statement 1 is correct under Section 10. Statement 2 is incorrect because almost all States (except Goa and UT of Puducherry) still entrust the compilation of their monthly and annual accounts to the CAG.",
        "exp_ta": "கூற்று 1 சரி. கூற்று 2 தவறு, ஏனெனில் கோவா மற்றும் புதுச்சேரி தவிர பெரும்பாலான மாநிலங்கள் தங்கள் கணக்குகளைத் தொகுக்கும் பணியை இன்றும் சி.ஏ.ஜியிடமே ஒப்படைத்துள்ளன.",
        "tip_en": "State accounts compilation: Remains with CAG (via AG A&E offices) in almost all States.",
        "tip_ta": "மாநிலக் கணக்குகள் தொகுப்பு: கோவா தவிர பெரும்பாலான மாநிலங்களில் இன்றும் சி.ஏ.ஜியிடமே உள்ளது.",
        "fact_en": "Accountant General (A&E) prepares the Monthly Civil Accounts for state finance departments.",
        "fact_ta": "முதன்மை கணக்குத் தலைவர் (A&E) மாநில நிதித் துறைகளுக்கான மாதாந்திர சிவில் கணக்குகளைத் தயாரிக்கிறார்."
    },
    # 48
    {
        "subtopic": "Disaster Relief Funds Audit",
        "stem_en": "Consider the following statements regarding the audit of State Disaster Response Funds (SDRF):\n1. The CAG audits whether the mandated state and central shares were credited to the SDRF within statutory timeframes.\n2. The CAG is legally barred from questioning expenditure incurred on disaster relief supplies during declared emergencies.\nWhich of the statements given above is/are correct?",
        "stem_ta": "மாநில பேரிடர் மீட்பு நிதி (SDRF) தணிக்கை குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. சட்டப்பூர்வ காலக்கெடுவிற்குள் மத்திய மற்றும் மாநில பங்குகள் SDRF-ல் வரவு வைக்கப்பட்டனவா என்பதை சி.ஏ.ஜி தணிக்கை செய்கிறார்.\n2. அவசரநிலைகளின் போது பேரிடர் நிவாரணப் பொருட்களுக்கு செய்யப்படும் செலவினங்களை கேள்வி கேட்க சி.ஏ.ஜிக்கு சட்டப்படி தடை உள்ளது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("1 only", "1 மட்டும்"),
            ("2 only", "2 மட்டும்"),
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Statement 1 is correct. Statement 2 is incorrect because relief expenditures are fully auditable to detect diversion of calamity funds for non-relief purposes.",
        "exp_ta": "கூற்று 1 சரி. கூற்று 2 தவறு, ஏனெனில் பேரிடர் நிதியானது நிவாரணம் அல்லாத பிற வழிகளுக்குத் திருப்பி விடப்படுவதைத் தடுக்க அனைத்து நிவாரணச் செலவுகளும் சி.ஏ.ஜியின் தணிக்கைக்கு உட்பட்டவை.",
        "tip_en": "SDRF audit examines timely fund credit, investment of surplus, and legitimacy of relief spend.",
        "tip_ta": "SDRF தணிக்கை சரியான நேரத்தில் நிதி வரவு, உபரி முதலீடு மற்றும் நிவாரணச் செலவுகளின் சட்டபூர்வ தன்மையை ஆராய்கிறது.",
        "fact_en": "Delays in crediting state share to SDRF attract interest liability payable by the State Government.",
        "fact_ta": "SDRF-க்கு மாநிலப் பங்கை வழங்க தாமதம் செய்தால் மாநில அரசு வட்டி செலுத்த வேண்டிய பொறுப்பு ஏற்படும்."
    },
    # 49
    {
        "subtopic": "Section 23 - Promulgation of Regulations",
        "stem_en": "Consider the following statements regarding Section 23 of the CAG Act 1971:\n1. The CAG is empowered to make regulations for carrying into effect the provisions of the Act relating to audit.\n2. Under Section 23, the CAG promulgated the Regulations on Audit and Accounts, 2007 (updated in 2020).\nWhich of the statements given above is/are correct?",
        "stem_ta": "1971 சி.ஏ.ஜி சட்டத்தின் பிரிவு 23 குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. தணிக்கை தொடர்பான சட்டத்தின் விதிகளைச் செயல்படுத்த ஒழுங்குமுறைகளை (Regulations) உருவாக்க சி.ஏ.ஜிக்கு அதிகாரம் உண்டு.\n2. பிரிவு 23-ன் கீழ், 2007 ஆம் ஆண்டின் தணிக்கை மற்றும் கணக்குகள் ஒழுங்குமுறைகளை (2020-ல் புதுப்பிக்கப்பட்டது) சி.ஏ.ஜி வெளியிட்டார்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("1 only", "1 மட்டும்"),
            ("2 only", "2 மட்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Both statements are correct under Section 23 of the CAG Act 1971.",
        "exp_ta": "இரண்டு கூற்றுகளும் சரியானவை. 1971 சி.ஏ.ஜி சட்டத்தின் பிரிவு 23 தணிக்கை விதிமுறைகளை உருவாக்க அதிகாரம் அளிக்கிறது; இதன் கீழ் 2007/2020 ஒழுங்குமுறைகள் நடைமுறைப்படுத்தப்பட்டன.",
        "tip_en": "Regulations on Audit and Accounts guide the day-to-day methodology and scope of government audit.",
        "tip_ta": "தணிக்கை ஒழுங்குமுறைகள் அரசு தணிக்கையின் அன்றாட வழிமுறைகள் மற்றும் வரம்பை வழிநடத்துகின்றன.",
        "fact_en": "Rules under Section 22 are made by Central Government in consultation with CAG; Regulations under Section 23 are made directly by CAG.",
        "fact_ta": "பிரிவு 22 விதிகளை சி.ஏ.ஜியைக் கலந்தாலோசித்து மத்திய அரசு உருவாக்குகிறது; பிரிவு 23 ஒழுங்குமுறைகளை சி.ஏ.ஜியே நேரடியாக உருவாக்குகிறார்."
    },
    # 50
    {
        "subtopic": "Overall Constitutional Summary",
        "stem_en": "Consider the following statements regarding the overarching role of the CAG in the Indian polity:\n1. The CAG is an officer of Parliament upholding the financial accountability of the executive to the legislature.\n2. The CAG's reports automatically lapse if Parliament is dissolved before taking them into consideration.\nWhich of the statements given above is/are correct?",
        "stem_ta": "இந்திய ஆட்சி முறையில் சி.ஏ.ஜியின் ஒட்டுமொத்தப் பங்கு குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. சட்டமன்றத்திற்கு நிர்வாகத்தின் நிதிப் பொறுப்புடைமையை நிலைநிறுத்தும் நாடாளுமன்றத்தின் ஒரு முகவராக சி.ஏ.ஜி செயல்படுகிறார்.\n2. நாடாளுமன்றம் பரிசீலிப்பதற்கு முன் மக்களவை கலைக்கப்பட்டால் சி.ஏ.ஜியின் அறிக்கைகள் தானாகவே காலாவதியாகிவிடும்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எது/எவை சரியானது?",
        "options": [
            ("1 only", "1 மட்டும்"),
            ("2 only", "2 மட்டும்"),
            ("Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்"),
            ("Neither 1 nor 2", "இரண்டும் இல்லை")
        ],
        "exp_en": "Statement 1 is correct: CAG acts on behalf of Parliament to enforce executive financial accountability. Statement 2 is incorrect because audit reports do not lapse upon dissolution of Lok Sabha; they are taken up by the succeeding Public Accounts Committee.",
        "exp_ta": "கூற்று 1 சரி: சட்டமன்றத்திற்கு நிர்வாகத்தின் பொறுப்புடைமையை நிலைநாட்டும் நாடாளுமன்றத்தின் அமைப்பாக சி.ஏ.ஜி உள்ளார். கூற்று 2 தவறு, ஏனெனில் மக்களவை கலைக்கப்பட்டாலும் தணிக்கை அறிக்கைகள் காலாவதியாவதில்லை; அடுத்ததாக வரும் PAC அதை ஆய்வு செய்யும்.",
        "tip_en": "CAG reports do NOT lapse on Lok Sabha dissolution; they remain pending before the next Parliament.",
        "tip_ta": "மக்களவை கலைக்கப்பட்டாலும் சி.ஏ.ஜி அறிக்கைகள் காலாவதியாவதில்லை; அடுத்த நாடாளுமன்றக் குழு அதைத் தொடரும்.",
        "fact_en": "CAG ensures that tax money authorized by Parliament is spent strictly as sanctioned without leakage.",
        "fact_ta": "நாடாளுமன்றம் அனுமதித்த வரிப் பணம் கசிவின்றி முறையாகச் செலவிடப்படுவதை சி.ஏ.ஜி உறுதி செய்கிறார்."
    }
]

def build_questions():
    questions = []
    for idx, item in enumerate(raw_statement_data, start=1):
        qid = f"CAG_S_{idx:03d}"
        opts = item["options"]
        correct_key = "A"
        
        why_en = {
            "A": f"Option A is correct: {item['exp_en']}",
            "B": f"Option B ({opts[1][0]}) is incorrect in this constitutional context.",
            "C": f"Option C ({opts[2][0]}) is incorrect in this constitutional context.",
            "D": f"Option D ({opts[3][0]}) is incorrect in this constitutional context."
        }
        why_ta = {
            "A": f"தெரிவு A சரி: {item['exp_ta']}",
            "B": f"தெரிவு B ({opts[1][1]}) இந்த அரசியலமைப்புச் சூழலில் தவறானதாகும்.",
            "C": f"தெரிவு C ({opts[2][1]}) இந்த அரசியலமைப்புச் சூழலில் தவறானதாகும்.",
            "D": f"தெரிவு D ({opts[3][1]}) இந்த அரசியலமைப்புச் சூழலில் தவறானதாகும்."
        }
        
        q = make_cag_q(
            qid=qid,
            diff="Medium",
            qtype="Statement Based",
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
            tags=["polity", "comptroller_and_auditor_general", "statement_based", item["subtopic"].lower().replace(" ", "_")]
        )
        questions.append(q)
    return questions

if __name__ == "__main__":
    qs = build_questions()
    print(f"Generated {len(qs)} raw Statement questions for CAG.")
    
    balanced_qs = balance_question_keys(qs)
    
    out_path = os.path.join("data", "questions", "polity", "cag_statement_based.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(balanced_qs, f, ensure_ascii=False, indent=2)
    print(f"Saved balanced Statement MCQs to {out_path}")
    
    # Also save alias
    alias_path = os.path.join("data", "questions", "polity", "cag_statement.json")
    with open(alias_path, "w", encoding="utf-8") as f:
        json.dump(balanced_qs, f, ensure_ascii=False, indent=2)
    print(f"Saved alias to {alias_path}")
    
    val = ContentValidator()
    report = val.validate_file(out_path, expected_count=50, expected_prefix="CAG_S_")
    print(f"Validation Report: {'PASS' if report.is_valid else 'FAIL'} | Total: {report.total_audited}")
    if not report.is_valid:
        for iss in report.issues[:10]:
            print(f"  Issue: {iss}")
    print(f"Key Distribution: {report.key_distribution}")
