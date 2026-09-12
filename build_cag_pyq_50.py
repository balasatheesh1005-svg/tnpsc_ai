# -*- coding: utf-8 -*-
"""
Build 50 PYQ Practice MCQs for CAG (Comptroller & Auditor General of India)
ID range: CAG_PYQ_001 to CAG_PYQ_050
"""

import json
import os
from cag_mcq_helper import make_cag_q
from rebalance_er_helper import balance_question_keys
from tools.nova_content_engine.validator import ContentValidator

raw_pyq_data = [
    # 1
    {
        "subtopic": "Constitutional Articles",
        "stem_en": "Under which Article of the Constitution of India is the Comptroller and Auditor General appointed?\n[TNPSC Group 1 Prelims]",
        "stem_ta": "இந்திய அரசியலமைப்பின் எந்தச் சரத்தின் கீழ் இந்தியத் தலைமைக் கணக்குத் தணிக்கையாளர் நியமிக்கப்படுகிறார்?\n[டி.என்.பி.எஸ்.சி குரூப் 1 முதல்நிலை]",
        "options": [
            ("Article 148", "சரத்து 148"),
            ("Article 149", "சரத்து 149"),
            ("Article 150", "சரத்து 150"),
            ("Article 151", "சரத்து 151")
        ],
        "exp_en": "Article 148 provides that there shall be a Comptroller and Auditor General of India appointed by the President by warrant under his hand and seal.",
        "exp_ta": "சரத்து 148 இந்தியக் குடியரசுத் தலைவரால் கையொப்பம் மற்றும் முத்திரையிட்ட ஆணை மூலம் நியமிக்கப்படும் இந்தியத் தலைமை கணக்குத் தணிக்கையாளர் ஒருவரை வழங்குகிறது.",
        "tip_en": "Article 148 = Office & Appointment of CAG.",
        "tip_ta": "சரத்து 148 = சி.ஏ.ஜி அலுவலகம் மற்றும் நியமனம்.",
        "fact_en": "Article 148 guarantees tenure security on par with Supreme Court judges.",
        "fact_ta": "சரத்து 148 உச்ச நீதிமன்ற நீதிபதிகளுக்கு இணையான பதவிக் காலப் பாதுகாப்பை உறுதி செய்கிறது."
    },
    # 2
    {
        "subtopic": "Tenure and Retirement Age",
        "stem_en": "What is the tenure of the Comptroller and Auditor General of India?\n[TNPSC Group 2 Prelims]",
        "stem_ta": "இந்தியத் தலைமைக் கணக்குத் தணிக்கையாளரின் பதவிக்காலம் என்ன?\n[டி.என்.பி.எஸ்.சி குரூப் 2 முதல்நிலை]",
        "options": [
            ("6 years or 65 years of age, whichever is earlier", "6 ஆண்டுகள் அல்லது 65 வயது, எது முந்தையதோ அதுவரை"),
            ("5 years or 65 years of age, whichever is earlier", "5 ஆண்டுகள் அல்லது 65 வயது, எது முந்தையதோ அதுவரை"),
            ("6 years or 62 years of age, whichever is earlier", "6 ஆண்டுகள் அல்லது 62 வயது, எது முந்தையதோ அதுவரை"),
            ("5 years or 60 years of age, whichever is earlier", "5 ஆண்டுகள் அல்லது 60 வயது, எது முந்தையதோ அதுவரை")
        ],
        "exp_en": "The CAG holds office for a term of six years or until attaining the age of 65 years, whichever is earlier, under Section 4 of the 1971 Act.",
        "exp_ta": "1971 சட்டத்தின் பிரிவு 4-ன் படி சி.ஏ.ஜி 6 ஆண்டுகள் அல்லது 65 வயது வரை, எது முந்தையதோ அதுவரை பதவியில் இருப்பார்.",
        "tip_en": "CAG tenure is 6 years or 65 years (same as UPSC Chairman and CEC).",
        "tip_ta": "சி.ஏ.ஜி பதவிக்காலம் 6 ஆண்டுகள் அல்லது 65 வயது (UPSC தலைவர் மற்றும் CEC போன்றது).",
        "fact_en": "Prior to the 1971 Act, tenure was not fixed uniformly by statute.",
        "fact_ta": "1971 சட்டத்திற்கு முன்பு பதவிக்காலம் சட்டப்பூர்வமாக சீராக நிர்ணயிக்கப்படவில்லை."
    },
    # 3
    {
        "subtopic": "Appointment Instrument",
        "stem_en": "The Comptroller and Auditor General of India is appointed by the President by:\n[TNPSC Group 4 / VAO]",
        "stem_ta": "இந்தியத் தலைமைக் கணக்குத் தணிக்கையாளர் குடியரசுத் தலைவரால் எவ்வாறு நியமிக்கப்படுகிறார்?\n[டி.என்.பி.எஸ்.சி குரூப் 4 / வி.ஏ.ஓ]",
        "options": [
            ("Warrant under his hand and seal", "தனது கையொப்பம் மற்றும் முத்திரையிட்ட ஆணை மூலம்"),
            ("Ordinary executive notification of the Prime Minister's Office", "பிரதமர் அலுவலகத்தின் வழக்கமான நிர்வாக அறிவிக்கை மூலம்"),
            ("Resolution passed by the Lok Sabha", "மக்களவையால் நிறைவேற்றப்படும் தீர்மானம் மூலம்"),
            ("Joint warrant issued with the Chief Justice of India", "தலைமை நீதிபதியுடன் இணைந்து வெளியிடப்படும் கூட்டு ஆணை மூலம்")
        ],
        "exp_en": "Article 148(1) explicitly states that the CAG is appointed by the President by warrant under his hand and seal, indicating high constitutional status.",
        "exp_ta": "சரத்து 148(1) வெளிப்படையாகக் கூறுவது என்னவென்றால், சி.ஏ.ஜி குடியரசுத் தலைவரால் அவரது கையொப்பம் மற்றும் முத்திரையிட்ட ஆணை மூலம் நியமிக்கப்படுகிறார்.",
        "tip_en": "Appointed by 'warrant under hand and seal': President appoints Governors, SC/HC judges, and CAG.",
        "tip_ta": "'கையொப்பம் மற்றும் முத்திரையிட்ட ஆணை' மூலம் நியமிக்கப்படுபவர்கள்: ஆளுநர்கள், நீதிபதிகள் மற்றும் சி.ஏ.ஜி.",
        "fact_en": "This instrument reflects the highest level of constitutional dignity in India.",
        "fact_ta": "இந்த ஆணை இந்தியாவில் மிக உயர்ந்த அரசியலமைப்பு கண்ணியத்தைப் பிரதிபலிக்கிறது."
    },
    # 4
    {
        "subtopic": "Removal Procedure",
        "stem_en": "The Comptroller and Auditor General of India can be removed from office in like manner and on like grounds as:\n[TNPSC Group 1 Mains / Prelims]",
        "stem_ta": "இந்தியத் தலைமைக் கணக்குத் தணிக்கையாளர் யாரை நீக்கும் அதே முறை மற்றும் காரணங்களின் அடிப்படையில் பதவியிலிருந்து நீக்கப்படலாம்?\n[டி.என்.பி.எஸ்.சி குரூப் 1]",
        "options": [
            ("A Judge of the Supreme Court", "உச்ச நீதிமன்ற நீதிபதி"),
            ("The Attorney General of India", "இந்திய தலைமை வழக்கறிஞர்"),
            ("The Prime Minister of India", "இந்தியப் பிரதமர்"),
            ("The Cabinet Secretary", "மத்திய அமைச்சரவைச் செயலாளர்")
        ],
        "exp_en": "Under Article 148(1), the CAG can be removed from office only in like manner and on like grounds as a Judge of the Supreme Court (proved misbehaviour or incapacity under Article 124(4)).",
        "exp_ta": "சரத்து 148(1)-ன் படி, உச்ச நீதிமன்ற நீதிபதியை நீக்கும் அதே நடைமுறை மற்றும் காரணங்களின் (நிரூபிக்கப்பட்ட தவறான நடத்தை அல்லது இயலாமை) அடிப்படையிலேயே சி.ஏ.ஜியை நீக்க முடியும்.",
        "tip_en": "CAG removal requires special majority address from both Houses of Parliament.",
        "tip_ta": "சி.ஏ.ஜி நீக்கத்திற்கு நாடாளுமன்றத்தின் இரு அவைகளிலும் சிறப்பு பெரும்பான்மை தீர்மானம் தேவை.",
        "fact_en": "Special majority: Majority of total membership AND 2/3rd of members present and voting.",
        "fact_ta": "சிறப்பு பெரும்பான்மை: மொத்த உறுப்பினர்களில் பெரும்பான்மை மற்றும் வருகை தந்து வாக்களித்தவர்களில் 2/3 பங்கு."
    },
    # 5
    {
        "subtopic": "Post-Retirement Disqualification",
        "stem_en": "Under Article 148(4), on ceasing to hold office, the CAG is:\n[UPSC Civil Services / TNPSC Group 1]",
        "stem_ta": "சரத்து 148(4)-ன் கீழ், பதவிக்காலம் முடிந்த பிறகு சி.ஏ.ஜி:\n[யு.பி.எஸ்.சி / டி.என்.பி.எஸ்.சி குரூப் 1]",
        "options": [
            ("Ineligible for further office under Government of India or any State Government", "மத்திய அல்லது எந்த மாநில அரசின் கீழும் மறுபதவி வகிக்கத் தகுதியற்றவர்"),
            ("Eligible to be appointed as Governor of a State immediately", "உடனடியாக மாநில ஆளுநராக நியமிக்கப்படத் தகுதியானவர்"),
            ("Eligible to serve as Attorney General of India", "இந்தியத் தலைமை வழக்கறிஞராகப் பணியாற்றத் தகுதியானவர்"),
            ("Eligible for reappointment as CAG for another full term", "மீண்டும் ஒரு முழு பதவிக்காலத்திற்கு சி.ஏ.ஜியாக நியமிக்கப்படத் தகுதியானவர்")
        ],
        "exp_en": "Article 148(4) provides that the CAG shall not be eligible for further office either under the Government of India or under the Government of any State after he has ceased to hold his office.",
        "exp_ta": "சரத்து 148(4)-ன் படி, சி.ஏ.ஜி பதவிக்காலம் முடிந்த பின்னர் மத்திய அல்லது மாநில அரசின் கீழ் எந்தவொரு பதவியையும் வகிக்கத் தகுதியற்றவர் ஆவார்.",
        "tip_en": "Article 148(4) bars further government employment to ensure fearless auditing.",
        "tip_ta": "சரத்து 148(4) அச்சமற்ற தணிக்கையை உறுதி செய்ய எதிர்கால அரசுப் பணிகளைத் தடை செய்கிறது.",
        "fact_en": "This absolute bar prevents the executive from offering post-retirement jobs as quid pro quo.",
        "fact_ta": "ஓய்வுக்குப் பின் சலுகை பதவிகளை நிர்வாகம் வழங்குவதைத் தடுக்கவே இந்த முழுமையான தடை உள்ளது."
    },
    # 6
    {
        "subtopic": "Dr. Ambedkar's Famous Quotation",
        "stem_en": "Who stated in the Constituent Assembly that the CAG 'shall be the most important officer in the Constitution of India'?\n[TNPSC Group 2 / Group 1]",
        "stem_ta": "அரசியலமைப்பு நிர்ணய சபையில் சி.ஏ.ஜி 'இந்திய அரசியலமைப்பின் மிக முக்கியமான அதிகாரியாக இருப்பார்' என்று கூறியவர் யார்?\n[டி.என்.பி.எஸ்.சி குரூப் 2 / குரூப் 1]",
        "options": [
            ("Dr. B.R. Ambedkar", "டாக்டர் பி.ஆர். அம்பேத்கர்"),
            ("Jawaharlal Nehru", "ஜவஹர்லால் நேரு"),
            ("Sardar Vallabhbhai Patel", "சர்தார் வல்லபாய் படேல்"),
            ("Dr. Rajendra Prasad", "டாக்டர் ராஜேந்திர பிரசாத்")
        ],
        "exp_en": "Dr. B.R. Ambedkar stated in the Constituent Assembly: 'The Comptroller and Auditor-General of India is probably the most important officer in the Constitution of India... more important than the judiciary or Election Commission.'",
        "exp_ta": "அரசியலமைப்பு நிர்ணய சபையில் டாக்டர் பி.ஆர். அம்பேத்கர் கூறினார்: 'சி.ஏ.ஜி அநேகமாக இந்திய அரசியலமைப்பின் மிக முக்கியமான அதிகாரியாக இருப்பார்... நீதித்துறை அல்லது தேர்தல் ஆணையத்தை விடவும் முக்கியமானவர்.'",
        "tip_en": "Dr. Ambedkar named CAG, SC, UPSC, and ECI as the four bulwarks of democratic India.",
        "tip_ta": "சி.ஏ.ஜி, உச்ச நீதிமன்றம், UPSC மற்றும் தேர்தல் ஆணையத்தை ஜனநாயகத்தின் நான்கு தூண்களாக அம்பேத்கர் குறிப்பிட்டார்.",
        "fact_en": "Ambedkar emphasized that executive control over spending requires strict independent audit oversight.",
        "fact_ta": "செலவினங்கள் மீதான நிர்வாக அதிகாரத்திற்கு கடுமையான தணிக்கைக் கண்காணிப்பு தேவை என்பதை அம்பேத்கர் வலியுறுத்தினார்."
    },
    # 7
    {
        "subtopic": "Friend, Philosopher and Guide to PAC",
        "stem_en": "The Comptroller and Auditor General acts as a 'friend, philosopher, and guide' to which parliamentary committee?\n[TNPSC Group 1 / Group 2]",
        "stem_ta": "தலைமைக் கணக்குத் தணிக்கையாளர் எந்த நாடாளுமன்றக் குழுவிற்கு 'நண்பர், தத்துவஞானி மற்றும் வழிகாட்டியாகச்' செயல்படுகிறார்?\n[டி.என்.பி.எஸ்.சி குரூப் 1 / குரூப் 2]",
        "options": [
            ("Public Accounts Committee (PAC)", "பொதுக் கணக்குக் குழு (PAC)"),
            ("Estimates Committee", "மதிப்பீட்டுக் குழு"),
            ("Committee on Privileges", "சலுகைகள் குழு"),
            ("Business Advisory Committee", "வணிக ஆலோசனைக் குழு")
        ],
        "exp_en": "The CAG acts as a guide, friend, and philosopher to the Public Accounts Committee (PAC), assisting the committee in scrutinizing audit reports and examining departmental witnesses.",
        "exp_ta": "பொதுக் கணக்குக் குழுவிற்கு (PAC) தணிக்கை அறிக்கைகளை ஆய்வு செய்வதிலும் சாட்சிகளை விசாரிப்பதிலும் உதவுவதன் மூலம் சி.ஏ.ஜி அதன் வழிகாட்டியாகவும் நண்பராகவும் செயல்படுகிறார்.",
        "tip_en": "CAG assists PAC and COPU; CAG has NO role in the Estimates Committee.",
        "tip_ta": "சி.ஏ.ஜி PAC மற்றும் COPU குழுக்களுக்கு உதவுகிறார்; மதிப்பீட்டுக் குழுவில் பங்கு இல்லை.",
        "fact_en": "The PAC was first established in India in 1921 under the Montagu-Chelmsford Reforms.",
        "fact_ta": "பொதுக் கணக்குக் குழு 1921-ல் மான்டேகு-செம்ஸ்போர்டு சீர்திருத்தங்களின் கீழ் முதன்முதலில் இந்தியாவில் அமைக்கப்பட்டது."
    },
    # 8
    {
        "subtopic": "Tabling of Audit Reports (Article 151)",
        "stem_en": "To whom does the CAG submit the audit reports relating to the accounts of the Union?\n[TNPSC Group 4 / Group 2]",
        "stem_ta": "மத்திய அரசின் கணக்குகள் தொடர்பான தணிக்கை அறிக்கைகளை சி.ஏ.ஜி யாரிடம் சமர்ப்பிக்கிறார்?\n[டி.என்.பி.எஸ்.சி குரூப் 4 / குரூப் 2]",
        "options": [
            ("The President of India", "இந்தியக் குடியரசுத் தலைவர்"),
            ("The Speaker of Lok Sabha", "மக்களவைத் தலைவர் (சபாநாயகர்)"),
            ("The Prime Minister of India", "இந்தியப் பிரதமர்"),
            ("The Union Finance Minister", "மத்திய நிதி அமைச்சர்")
        ],
        "exp_en": "Under Article 151(1), the reports of the CAG relating to the accounts of the Union shall be submitted to the President, who shall cause them to be laid before each House of Parliament.",
        "exp_ta": "சரத்து 151(1)-ன் படி, மத்திய கணக்குகள் தொடர்பான சி.ஏ.ஜி அறிக்கைகள் குடியரசுத் தலைவரிடம் சமர்ப்பிக்கப்பட வேண்டும்; அவர் அவற்றை நாடாளுமன்றத்தின் இரு அவைகளிலும் சமர்ப்பிக்கச் செய்வார்.",
        "tip_en": "Union reports -> President -> Parliament. State reports -> Governor -> State Legislature.",
        "tip_ta": "மத்திய அறிக்கை -> குடியரசுத் தலைவர் -> நாடாளுமன்றம். மாநில அறிக்கை -> ஆளுநர் -> சட்டமன்றம்.",
        "fact_en": "The President lays the reports without altering or deleting any audit observation.",
        "fact_ta": "தணிக்கைக் குறிப்புகளை மாற்றவோ நீக்கவோ செய்யாமல் குடியரசுத் தலைவர் நாடாளுமன்றத்தில் வைக்கிறார்."
    },
    # 9
    {
        "subtopic": "Submission of State Audit Reports",
        "stem_en": "The audit reports of the CAG relating to the accounts of a State are submitted to:\n[TNPSC Group 2 / Group 1]",
        "stem_ta": "ஒரு மாநிலத்தின் கணக்குகள் தொடர்பான சி.ஏ.ஜியின் தணிக்கை அறிக்கைகள் யாரிடம் சமர்ப்பிக்கப்படுகின்றன?\n[டி.என்.பி.எஸ்.சி குரூப் 2 / குரூப் 1]",
        "options": [
            ("The Governor of the State", "மாநில ஆளுநர்"),
            ("The Chief Minister of the State", "மாநில முதலமைச்சர்"),
            ("The Speaker of the Legislative Assembly", "சட்டமன்றப் பேரவைத் தலைவர்"),
            ("The State Finance Minister", "மாநில நிதி அமைச்சர்")
        ],
        "exp_en": "Under Article 151(2), the reports of the CAG relating to the accounts of a State shall be submitted to the Governor of the State, who shall cause them to be laid before the Legislature of the State.",
        "exp_ta": "சரத்து 151(2)-ன் படி, ஒரு மாநிலத்தின் கணக்குகள் தொடர்பான சி.ஏ.ஜியின் தணிக்கை அறிக்கைகள் மாநில ஆளுநரிடம் சமர்ப்பிக்கப்பட வேண்டும்; அவர் அவற்றை மாநிலச் சட்டமன்றத்தில் சமர்ப்பிக்கச் செய்வார்.",
        "tip_en": "Article 151(2) explicitly directs state audit reports to the Governor, not the Chief Minister.",
        "tip_ta": "சரத்து 151(2) மாநில அறிக்கைகளை முதலமைச்சரிடம் அல்லாமல் ஆளுநரிடம் சமர்ப்பிக்க உத்தரவிடுகிறது.",
        "fact_en": "In bicameral states, the Governor causes reports to be laid before both Houses.",
        "fact_ta": "ஈரவை சட்டமன்றங்கள் உள்ள மாநிலங்களில் ஆளுநர் இரு அவைகளிலும் அறிக்கைகளை வைக்கச் செய்வார்."
    },
    # 10
    {
        "subtopic": "Form of Accounts Prescription (Article 150)",
        "stem_en": "According to Article 150 of the Constitution, the form in which accounts of the Union and States are kept is prescribed by the President on the advice of:\n[UPSC / TNPSC Group 1]",
        "stem_ta": "அரசியலமைப்புச் சட்டம் சரத்து 150-ன் படி, மத்திய மற்றும் மாநிலங்களின் கணக்குகள் எந்தப் படிவத்தில் வைக்கப்பட வேண்டும் என்பதை குடியரசுத் தலைவர் யாருடைய ஆலோசனையின் பேரில் நிர்ணயிக்கிறார்?\n[டி.என்.பி.எஸ்.சி குரூப் 1]",
        "options": [
            ("The Comptroller and Auditor General of India", "இந்தியத் தலைமைக் கணக்குத் தணிக்கையாளர்"),
            ("The Union Finance Minister", "மத்திய நிதி அமைச்சர்"),
            ("The Controller General of Accounts", "கணக்கு முதன்மைக் கட்டுப்பாட்டாளர்"),
            ("The Public Accounts Committee", "பொதுக் கணக்குக் குழு")
        ],
        "exp_en": "Article 150 provides that the accounts of the Union and of the States shall be kept in such form as the President may, on the advice of the Comptroller and Auditor General of India, prescribe.",
        "exp_ta": "சரத்து 150-ன் படி, இந்தியத் தலைமை கணக்குத் தணிக்கையாளரின் ஆலோசனையின் பேரில் குடியரசுத் தலைவர் நிர்ணயிக்கும் படிவத்தில் மத்திய மற்றும் மாநிலங்களின் கணக்குகள் பராமரிக்கப்பட வேண்டும்.",
        "tip_en": "Article 150: 'on the advice of the CAG' was substituted by the 44th Amendment Act 1978.",
        "tip_ta": "சரத்து 150: 'சி.ஏ.ஜியின் ஆலோசனையின் பேரில்' என்ற சொல் 1978-ல் 44வது திருத்தத்தால் சேர்க்கப்பட்டது.",
        "fact_en": "The 42nd Amendment had weakened this by substituting 'after consultation with'.",
        "fact_ta": "42வது திருத்தம் 'கலந்தாலோசித்த பிறகு' என பலவீனப்படுத்தியதை 44வது திருத்தம் மீட்டெடுத்தது."
    },
    # 11
    {
        "subtopic": "Separation of Accounts from Audit",
        "stem_en": "In which year was the compilation of accounts separated from audit for the Union Government?\n[TNPSC Group 1 / Group 2]",
        "stem_ta": "மத்திய அரசில் கணக்கு வைக்கும் பணி தணிக்கைப் பணியிலிருந்து எந்த ஆண்டு பிரிக்கப்பட்டது?\n[டி.என்.பி.எஸ்.சி குரூப் 1 / குரூப் 2]",
        "options": [
            ("1976", "1976"),
            ("1971", "1971"),
            ("1980", "1980"),
            ("1968", "1968")
        ],
        "exp_en": "In 1976, through the Comptroller and Auditor General's (DPC) Amendment Act 1976, the CAG was relieved of the responsibility of compiling the accounts of the Union Government.",
        "exp_ta": "1976 ஆம் ஆண்டில் சி.ஏ.ஜி சட்டத் திருத்தத்தின் மூலம் மத்திய அரசின் கணக்குகளைத் தொகுக்கும் பொறுப்பிலிருந்து சி.ஏ.ஜி விடுவிக்கப்பட்டார்.",
        "tip_en": "1976 separation applies ONLY to the Union. Most States still have accounts compiled by CAG.",
        "tip_ta": "1976 கணக்குப் பிரிப்பு மத்திய அரசுக்கு மட்டுமே பொருந்தும். பெரும்பாலான மாநிலங்களில் சி.ஏ.ஜியே கணக்குகளைத் தொகுக்கிறார்.",
        "fact_en": "The office of the Controller General of Accounts (CGA) was established following the 1976 reform.",
        "fact_ta": "1976 சீர்திருத்தத்தைத் தொடர்ந்து கணக்கு முதன்மைக் கட்டுப்பாட்டாளர் (CGA) அலுவலகம் உருவாக்கப்பட்டது."
    },
    # 12
    {
        "subtopic": "Controller General of Accounts (CGA)",
        "stem_en": "Which authority is responsible for maintaining the accounts of the Union Government after the 1976 separation?\n[TNPSC Group 2 / Group 1]",
        "stem_ta": "1976 சீர்திருத்தத்திற்குப் பிறகு மத்திய அரசின் கணக்குகளைப் பராமரிக்கும் பொறுப்பு எந்த அதிகாரிக்கு உள்ளது?\n[டி.என்.பி.எஸ்.சி குரூப் 2 / குரூப் 1]",
        "options": [
            ("Controller General of Accounts (CGA)", "கணக்கு முதன்மைக் கட்டுப்பாட்டாளர் (CGA)"),
            ("Comptroller and Auditor General (CAG)", "தலைமைக் கணக்குத் தணிக்கையாளர் (சி.ஏ.ஜி)"),
            ("Governor of Reserve Bank of India", "இந்திய ரிசர்வ் வங்கி ஆளுநர்"),
            ("Finance Secretary of India", "இந்திய நிதிச் செயலாளர்")
        ],
        "exp_en": "The Controller General of Accounts (CGA), working under the Department of Expenditure, Ministry of Finance, maintains and compiles the accounts of the Union Government.",
        "exp_ta": "நிதி அமைச்சகத்தின் செலவினத் துறையின் கீழ் இயங்கும் கணக்கு முதன்மைக் கட்டுப்பாட்டாளர் (CGA) மத்திய அரசின் கணக்குகளைத் தொகுத்து பராமரிக்கிறார்.",
        "tip_en": "CGA is an accounting authority (non-constitutional); CAG is an independent constitutional audit authority.",
        "tip_ta": "CGA என்பது கணக்கு வைக்கும் துறை அதிகாரி; சி.ஏ.ஜி என்பது தன்னாட்சி பெற்ற அரசியலமைப்பு தணிக்கை அதிகாரி.",
        "fact_en": "CGA is the principal accounting advisor to the Government of India.",
        "fact_ta": "CGA இந்திய அரசின் முதன்மை கணக்கியல் ஆலோசகராக உள்ளார்."
    },
    # 13
    {
        "subtopic": "Salary Charged on Consolidated Fund",
        "stem_en": "The salary, allowances, and administrative expenses of the CAG are:\n[TNPSC Group 1 / Group 2]",
        "stem_ta": "சி.ஏ.ஜியின் ஊதியம், படிகள் மற்றும் நிர்வாகச் செலவுகள் எவ்வாறு வகைப்படுத்தப்பட்டுள்ளன?\n[டி.என்.பி.எஸ்.சி குரூப் 1 / குரூப் 2]",
        "options": [
            ("Charged upon the Consolidated Fund of India (non-votable)", "இந்தியத் திரட்டப்பட்ட நிதியிலிருந்து பொறுப்பாக்கப்பட்டது (வாக்கெடுப்பிற்கு உட்படாதது)"),
            ("Voted annually by the Lok Sabha as a general demand for grant", "பொது மானியக் கோரிக்கையாக மக்களவையால் ஆண்டுதோறும் வாக்களிக்கப்படுவது"),
            ("Paid out of the Contingency Fund of India", "இந்திய அவசரகால நிதியிலிருந்து வழங்கப்படுவது"),
            ("Charged upon the Public Account of India", "இந்தியப் பொதுக் கணக்கிலிருந்து பொறுப்பாக்கப்பட்டது")
        ],
        "exp_en": "Under Article 148(6), the administrative expenses of the office of the CAG, including all salaries, allowances, and pensions payable to persons serving in that office, are charged upon the Consolidated Fund of India and are not subject to parliamentary vote.",
        "exp_ta": "சரத்து 148(6)-ன் படி சி.ஏ.ஜி அலுவலகத்தின் அனைத்து நிர்வாகச் செலவுகள், ஊழியர்களின் ஊதியங்கள் அனைத்தும் இந்தியத் திரட்டப்பட்ட நிதியில் சுமத்தப்பட்டவையாகும் (வாக்கெடுப்பிற்கு உட்படாதவை).",
        "tip_en": "Charged expenditures can be discussed in Parliament, but CANNOT be voted upon.",
        "tip_ta": "பொறுப்பாக்கப்பட்ட செலவுகள் மீது விவாதிக்கலாம்; ஆனால் வாக்கெடுப்பு நடத்த முடியாது.",
        "fact_en": "The CAG receives salary equal to that of a Judge of the Supreme Court.",
        "fact_ta": "சி.ஏ.ஜி உச்ச நீதிமன்ற நீதிபதிக்கு இணையான ஊதியத்தைப் பெறுகிறார்."
    },
    # 14
    {
        "subtopic": "Oath Formulation in Third Schedule",
        "stem_en": "The form of oath of office for the Comptroller and Auditor General is prescribed in which Schedule of the Constitution?\n[TNPSC Group 4 / Group 2]",
        "stem_ta": "இந்தியத் தலைமைக் கணக்குத் தணிக்கையாளருக்கான பதவிப் பிரமாணப் படிவம் அரசியலமைப்பின் எந்த அட்டவணையில் குறிப்பிடப்பட்டுள்ளது?\n[டி.என்.பி.எஸ்.சி குரூப் 4 / குரூப் 2]",
        "options": [
            ("Third Schedule", "மூன்றாவது அட்டவணை"),
            ("Second Schedule", "இரண்டாவது அட்டவணை"),
            ("Fourth Schedule", "நான்காவது அட்டவணை"),
            ("Seventh Schedule", "ஏழாவது அட்டவணை")
        ],
        "exp_en": "Under Article 148(2), the CAG before entering upon office makes and subscribes an oath according to Form IV set out in the Third Schedule of the Constitution.",
        "exp_ta": "சரத்து 148(2)-ன் படி, சி.ஏ.ஜி பதவியேற்பதற்கு முன் அரசியலமைப்பின் மூன்றாவது அட்டவணையின் படிவம் IV-ன் படி பதவிப் பிரமாணம் செய்து கையொப்பமிடுகிறார்.",
        "tip_en": "Third Schedule: Oaths of Union Ministers, MPs, Judges of SC/HC, and CAG.",
        "tip_ta": "மூன்றாவது அட்டவணை: அமைச்சர்கள், எம்.பி.க்கள், உச்ச/உயர் நீதிமன்ற நீதிபதிகள் மற்றும் சி.ஏ.ஜியின் உறுதிமொழிகள்.",
        "fact_en": "Second Schedule deals with salaries and allowances.",
        "fact_ta": "இரண்டாவது அட்டவணை ஊதியம் மற்றும் படிகளைக் கையாள்கிறது."
    },
    # 15
    {
        "subtopic": "First CAG of Independent India",
        "stem_en": "Who was the first Comptroller and Auditor General of independent India?\n[TNPSC Group 1 / Group 2 / Group 4]",
        "stem_ta": "சுதந்திர இந்தியாவின் முதல் தலைமைக் கணக்குத் தணிக்கையாளர் யார்?\n[டி.என்.பி.எஸ்.சி குரூப் 1 / குரூப் 2 / குரூப் 4]",
        "options": [
            ("V. Narahari Rao", "வி. நரஹரி ராவ்"),
            ("A.K. Chanda", "ஏ.கே. சந்தா"),
            ("A.K. Roy", "ஏ.கே. ராய்"),
            ("S. Ranganathan", "எஸ். ரங்கநாதன்")
        ],
        "exp_en": "V. Narahari Rao served as the first Comptroller and Auditor General of independent India from 1948 to 1954.",
        "exp_ta": "வி. நரஹரி ராவ் 1948 முதல் 1954 வரை சுதந்திர இந்தியாவின் முதல் தலைமைக் கணக்குத் தணிக்கையாளராகப் பணியாற்றினார்.",
        "tip_en": "V. Narahari Rao (1948-1954) established the modern IA&AD structure.",
        "tip_ta": "வி. நரஹரி ராவ் (1948-1954) நவீன IA&AD கட்டமைப்பை நிறுவினார்.",
        "fact_en": "V. Narahari Rao was awarded the Padma Bhushan in 1954 for his distinguished public service.",
        "fact_ta": "வி. நரஹரி ராவுக்கு 1954-ல் பத்ம பூஷண் விருது வழங்கப்பட்டது."
    },
    # 16
    {
        "subtopic": "Article 279 Net Proceeds Certification",
        "stem_en": "Under Article 279 of the Constitution, who ascertains and certifies the 'net proceeds' of any tax or duty?\n[TNPSC Group 1 / Group 2]",
        "stem_ta": "அரசியலமைப்புச் சட்டம் சரத்து 279-ன் கீழ் எந்தவொரு வரி அல்லது கட்டணத்தின் 'நிகர வருமானத்தை' கணக்கிட்டு சான்றளிப்பவர் யார்?\n[டி.என்.பி.எஸ்.சி குரூப் 1 / குரூப் 2]",
        "options": [
            ("Comptroller and Auditor General of India", "இந்தியத் தலைமைக் கணக்குத் தணிக்கையாளர்"),
            ("Chairman of the Finance Commission", "நிதி ஆணையத்தின் தலைவர்"),
            ("Governor of the Reserve Bank of India", "இந்திய ரிசர்வ் வங்கி ஆளுநர்"),
            ("Union Finance Minister", "மத்திய நிதி அமைச்சர்")
        ],
        "exp_en": "Under Article 279(1), the net proceeds of any tax or duty are ascertained and certified by the Comptroller and Auditor General of India, whose certificate is final and conclusive.",
        "exp_ta": "சரத்து 279(1)-ன் படி, எந்தவொரு வரி அல்லது தீர்வையின் நிகர வருவாயும் இந்தியத் தலைமைக் கணக்குத் தணிக்கையாளரால் கணக்கிடப்பட்டு சான்றளிக்கப்படுகிறது; அவரது சான்றிதழ் இறுதியானது.",
        "tip_en": "Net proceeds = Gross tax revenue collected minus cost of collection.",
        "tip_ta": "நிகர வருமானம் = வசூலிக்கப்பட்ட மொத்த வரி வருவாய் - வசூல் செய்வதற்கான செலவினம்.",
        "fact_en": "The CAG's certificate on net proceeds cannot be challenged in any court or by the Union Ministry.",
        "fact_ta": "நிகர வருமானம் குறித்த சி.ஏ.ஜியின் சான்றிதழை எந்த நீதிமன்றத்திலும் அமைச்சகத்தாலும் கேள்வி கேட்க முடியாது."
    },
    # 17
    {
        "subtopic": "Companies Act Statutory Auditor Appointment",
        "stem_en": "Under Section 139 of the Companies Act 2013, the statutory auditor of a Government Company is appointed by:\n[TNPSC Assistant Director / Group 1]",
        "stem_ta": "நிறுவனங்கள் சட்டம் 2013, பிரிவு 139-ன் கீழ் ஓர் அரசு நிறுவனத்தின் சட்டப்பூர்வ தணிக்கையாளர் யாரால் நியமிக்கப்படுகிறார்?\n[டி.என்.பி.எஸ்.சி]",
        "options": [
            ("The Comptroller and Auditor General of India", "இந்தியத் தலைமைக் கணக்குத் தணிக்கையாளர்"),
            ("The Board of Directors of the Company", "நிறுவனத்தின் இயக்குநர் குழு"),
            ("The Union Ministry of Corporate Affairs", "மத்திய நிறுவன விவகாரங்கள் அமைச்சகம்"),
            ("The Shareholders in the Annual General Meeting", "ஆண்டுப் பொதுக்கூட்டத்தில் பங்குதாரர்கள்")
        ],
        "exp_en": "Under Section 139(5) and 139(7) of the Companies Act 2013, the statutory auditor of a Government Company is appointed by the Comptroller and Auditor General of India within 180 days from the commencement of the financial year.",
        "exp_ta": "நிறுவனங்கள் சட்டம் 2013, பிரிவு 139(5)-ன் படி, ஓர் அரசு நிறுவனத்தின் தணிக்கையாளரை நிதியாண்டு தொடங்கிய 180 நாட்களுக்குள் இந்தியத் தலைமைத் தணிக்கையாளர் நியமிக்கிறார்.",
        "tip_en": "Government Company: CAG appoints the Chartered Accountant auditor + can conduct supplementary audit.",
        "tip_ta": "அரசு நிறுவனம்: பட்டயக் கணக்காளரை சி.ஏ.ஜி நியமிக்கிறார் + துணைத் தணிக்கை நடத்தலாம்.",
        "fact_en": "CAG can conduct a supplementary audit within 60 days of receiving the statutory auditor's report.",
        "fact_ta": "சட்டப்பூர்வ தணிக்கை அறிக்கை கிடைத்த 60 நாட்களுக்குள் துணைத் தணிக்கை நடத்த சி.ஏ.ஜிக்கு அதிகாரம் உண்டு."
    },
    # 18
    {
        "subtopic": "Entities Completely Exempt from CAG Audit",
        "stem_en": "Which of the following public financial institutions is completely audited by private auditors and exempt from CAG audit?\n[TNPSC Group 1 / UPSC]",
        "stem_ta": "பின்வரும் பொது நிதி நிறுவனங்களில் எது முற்றிலும் தனியார் தணிக்கையாளர்களால் தணிக்கை செய்யப்பட்டு சி.ஏ.ஜி தணிக்கையிலிருந்து விலக்கு பெற்றுள்ளது?\n[டி.என்.பி.எஸ்.சி குரூப் 1]",
        "options": [
            ("Reserve Bank of India (RBI)", "இந்திய ரிசர்வ் வங்கி (RBI)"),
            ("Damodar Valley Corporation (DVC)", "தாமோதர் பள்ளத்தாக்கு கழகம் (DVC)"),
            ("Airports Authority of India (AAI)", "இந்திய விமான நிலையங்கள் ஆணையம் (AAI)"),
            ("Oil and Natural Gas Corporation (ONGC)", "எண்ணெய் மற்றும் இயற்கை எரிவாயுக் கழகம் (ONGC)")
        ],
        "exp_en": "The Reserve Bank of India (RBI), State Bank of India (SBI), and Life Insurance Corporation of India (LIC) are audited exclusively by independent private auditors under their respective governing acts, with zero audit involvement by the CAG.",
        "exp_ta": "இந்திய ரிசர்வ் வங்கி (RBI), பாரத ஸ்டேட் வங்கி (SBI) மற்றும் எல்.ஐ.சி ஆகியவை அவற்றின் சட்டங்களின்படி தனியார் பட்டயக் கணக்காளர்களால் மட்டுமே தணிக்கை செய்யப்படுகின்றன; சி.ஏ.ஜிக்கு இதில் பங்கில்லை.",
        "tip_en": "RBI, SBI, and LIC are completely outside the CAG's audit jurisdiction.",
        "tip_ta": "RBI, SBI, மற்றும் LIC ஆகியவை சி.ஏ.ஜியின் தணிக்கை அதிகார வரம்பிற்கு முற்றிலும் அப்பாற்பட்டவை.",
        "fact_en": "DVC and ONGC are subject to direct or supplementary audit by the CAG.",
        "fact_ta": "DVC மற்றும் ONGC ஆகியவை சி.ஏ.ஜியின் நேரடி அல்லது துணைத் தணிக்கைக்கு உட்பட்டவை."
    },
    # 19
    {
        "subtopic": "Propriety Audit Concept",
        "stem_en": "The audit conducted by the CAG to verify whether public money has been spent with wisdom, faithfulness, and public economy is called:\n[TNPSC Group 1 / Group 2]",
        "stem_ta": "பொதுப் பணம் விவேகம், நேர்மை மற்றும் பொதுச் சிக்கனத்துடன் செலவிடப்பட்டுள்ளதா என்பதை சரிபார்க்க சி.ஏ.ஜி நடத்தும் தணிக்கை எவ்வாறு அழைக்கப்படுகிறது?\n[டி.என்.பி.எஸ்.சி குரூப் 1 / குரூப் 2]",
        "options": [
            ("Propriety Audit", "விவேக / நாணயத் தணிக்கை (Propriety Audit)"),
            ("Regulatory Audit", "ஒழுங்குமுறைத் தணிக்கை"),
            ("Statutory Compliance Audit", "சட்டப்பூர்வ இணக்கத் தணிக்கை"),
            ("Appropriation Audit", "ஒதுக்கீட்டுத் தணிக்கை")
        ],
        "exp_en": "Propriety audit goes beyond mere legal rules to examine the wisdom, economy, and ethics of public expenditure, questioning extravagance or wastefulness even if covered by formal sanctions.",
        "exp_ta": "நாணயத் தணிக்கை என்பது சட்ட விதிகளைத் தாண்டி பொதுச் செலவினத்தின் விவேகம், சிக்கனம் மற்றும் நேர்மையை ஆராய்கிறது; முறையான அனுமதி இருந்தாலும் வீண் விரயத்தை கேள்வி கேட்கிறது.",
        "tip_en": "Regulatory audit = Legality check. Propriety audit = Wisdom and economy check.",
        "tip_ta": "ஒழுங்குமுறைத் தணிக்கை = சட்டப்பூர்வ சோதனை. நாணயத் தணிக்கை = விவேகம் மற்றும் சிக்கனச் சோதனை.",
        "fact_en": "Propriety audit is discretionary and guided by professional conventions and INTOSAI standards.",
        "fact_ta": "நாணயத் தணிக்கை என்பது விருப்பத்திற்குரியது மற்றும் தொழில்முறை மரபுகளால் வழிநடத்தப்படுகிறது."
    },
    # 20
    {
        "subtopic": "Performance Audit 3Es",
        "stem_en": "Performance auditing conducted by the CAG assesses which 'Three Es'?\n[TNPSC Group 2 / Group 1]",
        "stem_ta": "சி.ஏ.ஜியால் நடத்தப்படும் செயல்திறன் தணிக்கையானது எந்த 'மூன்று Es'-ஐ மதிப்பிடுகிறது?\n[டி.என்.பி.எஸ்.சி குரூப் 2 / குரூப் 1]",
        "options": [
            ("Economy, Efficiency, and Effectiveness", "சிக்கனம், செயல்திறன் மற்றும் செயலூக்கம் (Economy, Efficiency, Effectiveness)"),
            ("Equity, Equality, and Ethics", "சமபங்கு, சமத்துவம் மற்றும் நெறிமுறைகள்"),
            ("Execution, Expenditure, and Evaluation", "செயல்படுத்தல், செலவினம் மற்றும் மதிப்பீடு"),
            ("Estimation, Expansion, and Enforcement", "மதிப்பீடு, விரிவாக்கம் மற்றும் அமலாக்கம்")
        ],
        "exp_en": "Performance audit is an objective assessment of whether government undertakings and programs operate in accordance with Economy (minimizing cost), Efficiency (maximizing output per input), and Effectiveness (achieving intended objectives).",
        "exp_ta": "செயல்திறன் தணிக்கை என்பது அரசுத் திட்டங்கள் சிக்கனம் (குறைந்த செலவு), செயல்திறன் (அதிகபட்ச உற்பத்தி), மற்றும் செயலூக்கம் (குறிக்கோள்களை அடைதல்) ஆகிய 3Es கொள்கைகளின்படி செயல்படுகின்றனவா என்பதை மதிப்பிடுவதாகும்.",
        "tip_en": "The 3Es of performance audit: Economy (spending less), Efficiency (spending well), Effectiveness (spending wisely).",
        "tip_ta": "செயல்திறன் தணிக்கையின் 3Es: சிக்கனம் (குறைவான செலவு), செயல்திறன் (சரியான செலவு), செயலூக்கம் (நோக்கத்தை அடைதல்).",
        "fact_en": "Performance audit reports are presented under Article 151 and examined by PAC or COPU.",
        "fact_ta": "செயல்திறன் தணிக்கை அறிக்கைகள் சரத்து 151-ன் கீழ் சமர்ப்பிக்கப்பட்டு PAC அல்லது COPU-வால் ஆய்வு செய்யப்படுகின்றன."
    },
    # 21
    {
        "subtopic": "Public-Private Partnership Audit Ruling (2014)",
        "stem_en": "In the landmark AUTSPI judgment (2014), the Supreme Court upheld the CAG's power to audit which entities?\n[TNPSC Group 1 / UPSC]",
        "stem_ta": "வரலாற்று சிறப்புமிக்க AUTSPI வழக்கில் (2014), எந்த அமைப்புகளைத் தணிக்கை செய்ய சி.ஏ.ஜிக்கு உள்ள அதிகாரத்தை உச்ச நீதிமன்றம் உறுதி செய்தது?\n[டி.என்.பி.எஸ்.சி குரூப் 1]",
        "options": [
            ("Private telecom companies sharing revenue with the Union Government", "மத்திய அரசுடன் வருவாயைப் பகிர்ந்துகொள்ளும் தனியார் தொலைத்தொடர்பு நிறுவனங்கள்"),
            ("Foreign airline operators flying into India", "இந்தியாவுக்குள் பறக்கும் வெளிநாட்டு விமான நிறுவனங்கள்"),
            ("All privately held commercial banks", "அனைத்து தனியார் வணிக வங்கிகள்"),
            ("Political parties registered with the Election Commission", "தேர்தல் ஆணையத்தில் பதிவுசெய்யப்பட்ட அரசியல் கட்சிகள்")
        ],
        "exp_en": "In Association of Unified Telecom Service Providers of India (AUTSPI) v. Union of India (2014), the Supreme Court held that under Article 149 and Section 16, the CAG can audit the revenue accounts of private telecom licensees sharing revenue with the government.",
        "exp_ta": "2014 AUTSPI வழக்கில், இயற்கை வளங்களைப் பயன்படுத்தி அரசுடன் வருவாயைப் பகிர்ந்துகொள்ளும் தனியார் தொலைத்தொடர்பு நிறுவனங்களின் வருவாய்க் கணக்குகளை சி.ஏ.ஜி தணிக்கை செய்யலாம் என உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
        "tip_en": "Public Trust Doctrine applies: Spectrum is a national asset, so revenue sharing is subject to CAG audit.",
        "tip_ta": "பொது அறக்கட்டளைக் கோட்பாடு பொருந்தும்: அலைக்கற்றை தேசிய வளம் என்பதால் வருவாய்ப் பகிர்வு சி.ஏ.ஜி தணிக்கைக்கு உட்பட்டது.",
        "fact_en": "The audit is restricted strictly to verifying that the government received its full revenue entitlement.",
        "fact_ta": "அரசுக்குச் சேர வேண்டிய முழு வருவாய்ப் பங்கு கிடைத்ததா என்பதை சரிபார்ப்பதற்கு மட்டுமே இத்தணிக்கை வரையறுக்கப்பட்டுள்ளது."
    },
    # 22
    {
        "subtopic": "Technical Guidance and Supervision (TGS)",
        "stem_en": "Under which scheme does the CAG supervise the accounting and auditing standards of Panchayats and Urban Local Bodies?\n[TNPSC Group 1 / Assistant Director]",
        "stem_ta": "எந்தத் திட்டத்தின் கீழ் பஞ்சாயத்துகள் மற்றும் நகர்ப்புற உள்ளாட்சி அமைப்புகளின் கணக்கு மற்றும் தணிக்கைத் தரங்களை சி.ஏ.ஜி மேற்பார்வையிடுகிறார்?\n[டி.என்.பி.எஸ்.சி]",
        "options": [
            ("Technical Guidance and Supervision (TGS)", "தொழில்நுட்ப வழிகாட்டுதல் மற்றும் மேற்பார்வை (TGS)"),
            ("Direct Executive Audit (DEA)", "நேரடி நிர்வாகத் தணிக்கை"),
            ("Gram Swaraj Audit Control (GSAC)", "கிராம சுவராஜ் தணிக்கைக் கட்டுப்பாடு"),
            ("District Fund Mandate (DFM)", "மாவட்ட நிதி ஆணை")
        ],
        "exp_en": "Under Technical Guidance and Supervision (TGS), first recommended by the Eleventh Finance Commission, the CAG provides technical audit guidance, sets accounting formats, and conducts test audits for local bodies.",
        "exp_ta": "11வது நிதி ஆணையத்தால் பரிந்துரைக்கப்பட்ட தொழில்நுட்ப வழிகாட்டுதல் மற்றும் மேற்பார்வையின் (TGS) கீழ், உள்ளாட்சி அமைப்புகளுக்கு சி.ஏ.ஜி கணக்குப் படிவங்களை அமைத்து மாதிரித் தணிக்கைகளை நடத்துகிறார்.",
        "tip_en": "Primary audit of local bodies is done by the State Local Fund Audit; CAG provides TGS.",
        "tip_ta": "உள்ளாட்சி அமைப்புகளின் முதன்மைத் தணிக்கை மாநில உள்ளாட்சி நிதி தணிக்கையால் செய்யப்படுகிறது; சி.ஏ.ஜி TGS தருகிறார்.",
        "fact_en": "Fifteenth Finance Commission tied local body grant disbursement directly to audited accounts.",
        "fact_ta": "15வது நிதி ஆணையம் உள்ளாட்சி மானியங்களை தணிக்கை செய்யப்பட்ட கணக்குகளுடன் நேரடியாக இணைத்தது."
    },
    # 23
    {
        "subtopic": "Limits on Audit: Secret Service Funds",
        "stem_en": "Which category of government expenditure is subject to limitation where the CAG cannot demand detailed vouchers?\n[TNPSC Group 1 / Group 2]",
        "stem_ta": "எந்த வகை அரசுச் செலவினத்தில் விரிவான ரசீதுகளைக் கோர முடியாமல் சி.ஏ.ஜி தணிக்கை வரம்பிற்கு உட்படுத்தப்பட்டுள்ளது?\n[டி.என்.பி.எஸ்.சி குரூப் 1 / குரூப் 2]",
        "options": [
            ("Secret Service Expenditure", "ரகசிய சேவைச் செலவினங்கள் (Secret Service Expenditure)"),
            ("Railway capital expenditure", "ரயில்வே மூலதனச் செலவினங்கள்"),
            ("Defence procurement of uniforms", "ராணுவ சீருடைகள் கொள்முதல் செலவினம்"),
            ("National Highways toll construction", "தேசிய நெடுஞ்சாலைகள் சுங்கக் கட்டுமானம்")
        ],
        "exp_en": "In secret service expenditure (intelligence operations), the CAG cannot insist on detailed vouchers; the audit is legally bound to accept a certificate from the competent administrative authority confirming expenditure.",
        "exp_ta": "ரகசிய சேவைச் செலவினங்களில் (உளவுத்துறை நடவடிக்கைகள்) சி.ஏ.ஜி விரிவான ரசீதுகளைக் கோர முடியாது; தகுதிவாய்ந்த நிர்வாக அதிகாரி அளிக்கும் சான்றிதழை தணிக்கை ஏற்றுக்கொள்ள வேண்டும்.",
        "tip_en": "Secret service expenditure is a recognized constitutional limitation protecting national security.",
        "tip_ta": "ரகசிய சேவைச் செலவு என்பது தேசியப் பாதுகாப்பைப் பாதுகாக்கும் அங்கீகரிக்கப்பட்ட தணிக்கை வரம்பாகும்.",
        "fact_en": "Applies to intelligence agencies like RAW and Intelligence Bureau.",
        "fact_ta": "ரா (RAW) மற்றும் உளவுத்துறை (IB) போன்ற புலனாய்வு அமைப்புகளுக்கு இது பொருந்தும்."
    },
    # 24
    {
        "subtopic": "Legal Status of Audit Loss Estimates",
        "stem_en": "According to the Supreme Court, what is the legal nature of loss estimates contained in a CAG report?\n[TNPSC Group 1 / UPSC]",
        "stem_ta": "உச்ச நீதிமன்றத்தின்படி, சி.ஏ.ஜி அறிக்கையில் உள்ள இழப்பு மதிப்பீடுகளின் சட்டப்பூர்வ அந்தஸ்து என்ன?\n[டி.என்.பி.எஸ்.சி குரூப் 1]",
        "options": [
            ("They are investigative audit assessments for legislative scrutiny, not conclusive proof in a criminal court", "அவை சட்டமன்ற ஆய்விற்கான தணிக்கை மதிப்பீடுகளே தவிர குற்றவியல் நீதிமன்றத்தில் உறுதியான ஆதாரமல்ல"),
            ("They constitute conclusive judicial decrees executable by high courts", "அவை உயர் நீதிமன்றங்களால் நிறைவேற்றக்கூடிய முடிவான நீதித்துறை தீர்ப்புகளாகும்"),
            ("They automatically convict officials under the Prevention of Corruption Act", "அவை ஊழல் தடுப்புச் சட்டத்தின் கீழ் அதிகாரிகளை தானாகவே குற்றவாளியாக்குகின்றன"),
            ("They have no constitutional standing and can be ignored by Parliament", "அவை அரசியலமைப்பு அந்தஸ்தற்றவை மற்றும் நாடாளுமன்றத்தால் புறக்கணிக்கப்படலாம்")
        ],
        "exp_en": "The Supreme Court has clarified that CAG reports provide material for parliamentary debate and can trigger police investigation, but findings do not constitute conclusive evidence of criminal guilt in a court of law.",
        "exp_ta": "சி.ஏ.ஜி அறிக்கைகள் நாடாளுமன்ற விவாதத்திற்கும் புலனாய்வு அமைப்புகளின் விசாரணைக்கும் உதவுகின்றன; ஆனால் அவை குற்றவியல் நீதிமன்றத்தில் குற்றத்தை நிரூபிக்கும் உறுதியான நேரடி ஆதாரங்கள் ஆகாது.",
        "tip_en": "CAG reports are audited findings for Parliament, not criminal judgments.",
        "tip_ta": "சி.ஏ.ஜி அறிக்கைகள் நாடாளுமன்றத்திற்கான தணிக்கைக் கண்டுபிடிப்புகள்; நீதிமன்றத் தீர்ப்புகள் அல்ல.",
        "fact_en": "Investigative agencies like CBI independently build chargesheets using original evidence.",
        "fact_ta": "சி.பி.ஐ போன்ற புலனாய்வு அமைப்புகள் அசல் ஆதாரங்களைக் கொண்டு தனித்துக் குற்றப்பத்திரிகை தாக்கல் செய்கின்றன."
    },
    # 25
    {
        "subtopic": "Constitutional Chapter and Part",
        "stem_en": "In which Chapter and Part of the Constitution of India is the Comptroller and Auditor General placed?\n[TNPSC Group 4 / Group 2]",
        "stem_ta": "இந்திய அரசியலமைப்பின் எந்தப் பகுதி மற்றும் அத்தியாயத்தில் தலைமைக் கணக்குத் தணிக்கையாளர் இடம்பெற்றுள்ளார்?\n[டி.என்.பி.எஸ்.சி குரூப் 4 / குரூப் 2]",
        "options": [
            ("Chapter V of Part V", "பகுதி V-ன் அத்தியாயம் V"),
            ("Chapter IV of Part V", "பகுதி V-ன் அத்தியாயம் IV"),
            ("Chapter II of Part VI", "பகுதி VI-ன் அத்தியாயம் II"),
            ("Chapter I of Part XII", "பகுதி XII-ன் அத்தியாயம் I")
        ],
        "exp_en": "Articles 148 to 151 forming the Comptroller and Auditor General of India are contained in Chapter V of Part V ('The Union') of the Constitution.",
        "exp_ta": "சி.ஏ.ஜி தொடர்பான சரத்துகள் 148 முதல் 151 வரை அரசியலமைப்பின் பகுதி V ('ஒன்றியம்'), அத்தியாயம் V-ல் இடம்பெற்றுள்ளன.",
        "tip_en": "Part V: Chapter I (Executive), Chapter II (Parliament), Chapter III (President's Legislative Powers), Chapter IV (Supreme Court), Chapter V (CAG).",
        "tip_ta": "பகுதி V: அத்தியாயம் I (நிர்வாகம்), II (நாடாளுமன்றம்), III (சட்டமியற்றும் அதிகாரம்), IV (உச்ச நீதிமன்றம்), V (சி.ஏ.ஜி).",
        "fact_en": "Chapter V contains only four articles: 148, 149, 150, and 151.",
        "fact_ta": "அத்தியாயம் V நான்கு சரத்துகளை மட்டுமே கொண்டுள்ளது: 148, 149, 150, மற்றும் 151."
    },
    # 26
    {
        "subtopic": "Section 14 Autonomous Bodies Audit Threshold",
        "stem_en": "Under Section 14 of the CAG Act 1971, what is the mandatory threshold for audit of bodies substantially financed by government grants?\n[TNPSC Assistant Director / Group 1]",
        "stem_ta": "1971 சி.ஏ.ஜி சட்டத்தின் பிரிவு 14-ன் கீழ், அரசு மானியங்களால் கணிசமாக நிதியளிக்கப்படும் அமைப்புகளின் கட்டாயத் தணிக்கைக்கான வரம்பு என்ன?\n[டி.என்.பி.எஸ்.சி]",
        "options": [
            ("Grant of not less than Rs. 25 lakh and representing at least 75% of total expenditure", "குறைந்தபட்சம் ரூ. 25 லட்சம் மானியம் மற்றும் மொத்த செலவில் குறைந்தது 75%"),
            ("Grant of not less than Rs. 50 lakh and representing at least 50% of total expenditure", "குறைந்தபட்சம் ரூ. 50 லட்சம் மானியம் மற்றும் மொத்த செலவில் குறைந்தது 50%"),
            ("Grant of not less than Rs. 10 lakh and representing at least 90% of total expenditure", "குறைந்தபட்சம் ரூ. 10 லட்சம் மானியம் மற்றும் மொத்த செலவில் குறைந்தது 90%"),
            ("Grant of not less than Rs. 1 crore regardless of percentage", "சதவீதம் பொருட்படுத்தாமல் குறைந்தபட்சம் ரூ. 1 கோடி மானியம்")
        ],
        "exp_en": "Section 14(1) mandates audit of any body or authority where the government grant or loan in a financial year is not less than Rs. 25 lakh and constitutes at least 75% of the total expenditure of that body.",
        "exp_ta": "பிரிவு 14(1)-ன் படி, ஓர் அமைப்பிற்கு ஒரு நிதியாண்டில் கிடைக்கும் அரசு மானியம் அல்லது கடன் ரூ. 25 லட்சத்திற்குக் குறையாமலும், மொத்த செலவில் 75% ஆகவும் இருந்தால் அது கட்டாயமாக சி.ஏ.ஜியால் தணிக்கை செய்யப்பட வேண்டும்.",
        "tip_en": "Section 14(1) twin conditions: Rs. 25 lakh AND 75% of total expenditure.",
        "tip_ta": "பிரிவு 14(1) இரட்டை நிபந்தனைகள்: ரூ. 25 லட்சம் மற்றும் மொத்த செலவில் 75%.",
        "fact_en": "Section 14(2) also enables audit where grant is not less than Rs. 1 crore with prior approval.",
        "fact_ta": "ரூ. 1 கோடிக்கு குறையாத மானியம் பெறும் அமைப்புகளையும் முன் அனுமதியுடன் தணிக்கை செய்ய பிரிவு 14(2) வழிவகுக்கிறது."
    },
    # 27
    {
        "subtopic": "Sixth Schedule District Councils Audit",
        "stem_en": "Under Paragraph 7 of the Sixth Schedule to the Constitution, who audits the accounts of Autonomous District Councils in tribal areas?\n[TNPSC Group 1 / UPSC]",
        "stem_ta": "அரசியலமைப்பின் ஆறாவது அட்டவணை பத்தி 7-ன் கீழ் பழங்குடியினர் பகுதிகளில் உள்ள தன்னாட்சி மாவட்டக் குழுக்களின் கணக்குகளைத் தணிக்கை செய்பவர் யார்?\n[டி.என்.பி.எஸ்.சி குரூப் 1]",
        "options": [
            ("The Comptroller and Auditor General of India", "இந்தியத் தலைமைக் கணக்குத் தணிக்கையாளர்"),
            ("The Union Ministry of Tribal Affairs", "மத்திய பழங்குடியினர் விவகாரங்கள் அமைச்சகம்"),
            ("The National Commission for Scheduled Tribes", "தேசிய பழங்குடியினர் ஆணையம்"),
            ("Private chartered accountants appointed by District Council Chairman", "மாவட்டக் குழுத் தலைவரால் நியமிக்கப்படும் தனியார் பட்டயக் கணக்காளர்கள்")
        ],
        "exp_en": "Under Paragraph 7(1) of the Sixth Schedule, the accounts of Autonomous District and Regional Councils shall be kept in such form as the CAG prescribes and are audited by the CAG.",
        "exp_ta": "ஆறாவது அட்டவணை பத்தி 7(1)-ன் கீழ், தன்னாட்சி மாவட்ட மற்றும் பிராந்தியக் குழுக்களின் கணக்குகள் சி.ஏ.ஜி பரிந்துரைக்கும் படிவத்தில் வைக்கப்பட்டு, சி.ஏ.ஜியாலேயே தணிக்கை செய்யப்படுகின்றன.",
        "tip_en": "Sixth Schedule covers tribal areas of Assam, Meghalaya, Tripura, and Mizoram (AMTM).",
        "tip_ta": "ஆறாவது அட்டவணை அசாம், மேகாலயா, திரிபுரா மற்றும் மிசோரம் (AMTM) பழங்குடியினர் பகுதிகளை உள்ளடக்கியது.",
        "fact_en": "Reports on District Councils are submitted to the State Governor.",
        "fact_ta": "மாவட்டக் குழுக்கள் மீதான தணிக்கை அறிக்கைகள் மாநில ஆளுநரிடம் சமர்ப்பிக்கப்படுகின்றன."
    },
    # 28
    {
        "subtopic": "Section 18 Right to Inspect Records",
        "stem_en": "Which section of the CAG (DPC) Act 1971 empowers the CAG to inspect offices and demand records and books of account?\n[TNPSC Group 1 / Assistant Director]",
        "stem_ta": "அலுவலகங்களை ஆய்வு செய்யவும், ஆவணங்கள் மற்றும் கணக்குப் புத்தகங்களைக் கோரவும் சி.ஏ.ஜிக்கு அதிகாரம் அளிக்கும் 1971 சி.ஏ.ஜி சட்டத்தின் பிரிவு எது?\n[டி.என்.பி.எஸ்.சி]",
        "options": [
            ("Section 18", "பிரிவு 18"),
            ("Section 12", "பிரிவு 12"),
            ("Section 15", "பிரிவு 15"),
            ("Section 22", "பிரிவு 22")
        ],
        "exp_en": "Section 18 confers powers on the CAG to inspect any office of accounts under the Union or a State and require that any books, papers, or documents be sent to specified locations for audit scrutiny.",
        "exp_ta": "பிரிவு 18 மத்திய அல்லது மாநில அரசின் கணக்கு அலுவலகங்களை ஆய்வு செய்யவும், தணிக்கைக்காக எந்தவொரு புத்தகம், ஆவணம் அல்லது பதிவேட்டை சமர்ப்பிக்கக் கோரவும் சி.ஏ.ஜிக்கு அதிகாரம் அளிக்கிறது.",
        "tip_en": "Section 18 guarantees unhindered audit access to official records.",
        "tip_ta": "பிரிவு 18 அரசு ஆவணங்களைத் தடையின்றி அணுகும் தணிக்கை உரிமையை உறுதி செய்கிறது.",
        "fact_en": "Government departments cannot refuse to produce documents citing internal administrative secrecy.",
        "fact_ta": "உள் நிர்வாக ரகசியம் என்று கூறி ஆவணங்களை வழங்க அரசுத் துறைகள் மறுக்க முடியாது."
    },
    # 29
    {
        "subtopic": "Separate Audit Reports (SARs)",
        "stem_en": "The specialized audit reports prepared by the CAG on autonomous central universities and institutes are called:\n[TNPSC Group 1 / Group 2]",
        "stem_ta": "மத்திய தன்னாட்சிப் பல்கலைக்கழகங்கள் மற்றும் நிறுவனங்கள் மீது சி.ஏ.ஜியால் தயாரிக்கப்படும் சிறப்புத் தணிக்கை அறிக்கைகள் எவ்வாறு அழைக்கப்படுகின்றன?\n[டி.என்.பி.எஸ்.சி குரூப் 1 / குரூப் 2]",
        "options": [
            ("Separate Audit Reports (SARs)", "தனித் தணிக்கை அறிக்கைகள் (SARs)"),
            ("Supplementary Review Decrees (SRDs)", "துணை மறுஆய்வு ஆணைகள்"),
            ("General Performance Vouchers (GPVs)", "பொதுச் செயல்திறன் சான்றுகள்"),
            ("Internal Attestation Documents (IADs)", "உள் உறுதிப்படுத்தல் ஆவணங்கள்")
        ],
        "exp_en": "For autonomous bodies (IITs, IIMs, Central Universities) audited under Sections 14 and 19(2), the CAG prepares Separate Audit Reports (SARs) that are tabled individually in Parliament.",
        "exp_ta": "பிரிவுகள் 14 மற்றும் 19(2)-ன் கீழ் தணிக்கை செய்யப்படும் தன்னாட்சி அமைப்புகளுக்கு (IIT, IIM, மத்தியப் பல்கலைக்கழகங்கள்) தனித் தணிக்கை அறிக்கைகளை (SARs) சி.ஏ.ஜி தயாரித்து நாடாளுமன்றத்தில் வைக்கச் செய்கிறார்.",
        "tip_en": "SAR = Separate Audit Report for autonomous educational/research institutions.",
        "tip_ta": "SAR = தன்னாட்சி கல்வி/ஆராய்ச்சி நிறுவனங்களுக்கான தனித் தணிக்கை அறிக்கை.",
        "fact_en": "SARs audit both the annual balance sheet and compliance with grant conditions.",
        "fact_ta": "SAR அறிக்கைகள் ஆண்டு இருப்புநிலை அறிக்கை மற்றும் மானிய நிபந்தனைகள் இணக்கம் இரண்டையுமே தணிக்கை செய்கின்றன."
    },
    # 30
    {
        "subtopic": "Pre-Independence Historical Milestone",
        "stem_en": "In which year was Sir Edward Drummond appointed as the first Auditor General of India?\n[TNPSC Group 1 / Group 2]",
        "stem_ta": "சர் எட்வர்ட் டிரம்மாண்ட் எந்த ஆண்டு இந்தியாவின் முதல் தணிக்கைத் தலைவராக நியமிக்கப்பட்டார்?\n[டி.என்.பி.எஸ்.சி குரூப் 1 / குரூப் 2]",
        "options": [
            ("1860", "1860"),
            ("1858", "1858"),
            ("1872", "1872"),
            ("1919", "1919")
        ],
        "exp_en": "In 1858, Lord Canning created the office of the Accountant General, and in 1860, Sir Edward Drummond was appointed as the first Auditor General of India.",
        "exp_ta": "1858-ல் கானிங் பிரபு கணக்குத் தலைவர் அலுவலகத்தை உருவாக்கினார்; 1860-ல் சர் எட்வர்ட் டிரம்மாண்ட் இந்தியாவின் முதல் தணிக்கைத் தலைவராக நியமிக்கப்பட்டார்.",
        "tip_en": "1858: Lord Canning sets up the department; 1860: Sir Edward Drummond becomes first Auditor General.",
        "tip_ta": "1858: கானிங் பிரபு துறையை உருவாக்கினார்; 1860: எட்வர்ட் டிரம்மாண்ட் முதல் தணிக்கைத் தலைவரானார்.",
        "fact_en": "This marked the foundation of formal state auditing in British India.",
        "fact_ta": "இது பிரிட்டிஷ் இந்தியாவில் முறையான அரசு தணிக்கையின் தொடக்கத்தைக் குறித்தது."
    },
    # 31
    {
        "subtopic": "Absence of Direct Relations with Estimates Committee",
        "stem_en": "Why does the CAG have NO formal relationship with the parliamentary Estimates Committee?\n[TNPSC Group 1 / UPSC]",
        "stem_ta": "நாடாளுமன்ற மதிப்பீட்டுக் குழுவுடன் சி.ஏ.ஜிக்கு ஏன் எவ்வித முறையான தொடர்பும் இல்லை?\n[டி.என்.பி.எஸ்.சி குரூப் 1]",
        "options": [
            ("The Estimates Committee examines future policy economies before expenditure, while CAG conducts ex-post audit", "மதிப்பீட்டுக் குழு செலவுக்கு முன் வருங்காலக் கொள்கை சிக்கனங்களை ஆராய்கிறது; சி.ஏ.ஜி செலவுக்குப் பிந்தைய தணிக்கை செய்கிறார்"),
            ("The Estimates Committee contains only members from Rajya Sabha", "மதிப்பீட்டுக் குழுவில் மாநிலங்களவை உறுப்பினர்கள் மட்டுமே உள்ளனர்"),
            ("The CAG is statutorily prohibited from speaking to Lok Sabha committees", "மக்களவைக் குழுக்களுடன் பேச சி.ஏ.ஜிக்கு சட்டப்படி தடை உள்ளது"),
            ("The Estimates Committee audits private corporations only", "மதிப்பீட்டுக் குழு தனியார் நிறுவனங்களை மட்டுமே தணிக்கை செய்கிறது")
        ],
        "exp_en": "The Estimates Committee evaluates budget estimates and policy economies before expenditure is incurred. Because CAG's constitutional mandate is ex-post financial audit, the CAG assists PAC and COPU, but not the Estimates Committee.",
        "exp_ta": "மதிப்பீட்டுக் குழு செலவு செய்வதற்கு முன் பட்ஜெட் மதிப்பீடுகளையும் கொள்கைச் சிக்கனங்களையும் ஆராய்கிறது. சி.ஏ.ஜியின் பணி செலவுக்குப் பிந்தைய தணிக்கை என்பதால் அவர் PAC மற்றும் COPU-விற்கு உதவுகிறாரே தவிர மதிப்பீட்டுக் குழுவிற்கு அல்ல.",
        "tip_en": "CAG assists PAC and COPU; Estimates Committee operates independently without CAG.",
        "tip_ta": "சி.ஏ.ஜி PAC மற்றும் COPU குழுக்களுக்கு உதவுகிறார்; மதிப்பீட்டுக் குழு சி.ஏ.ஜி இன்றி இயங்குகிறது.",
        "fact_en": "The Estimates Committee consists of 30 members, all elected from Lok Sabha.",
        "fact_ta": "மதிப்பீட்டுக் குழு மக்களவையிலிருந்து தேர்ந்தெடுக்கப்படும் 30 உறுப்பினர்களைக் கொண்டது."
    },
    # 32
    {
        "subtopic": "Opposition Chairman of PAC Convention",
        "stem_en": "Since 1967, by convention, the Chairman of the Public Accounts Committee (which examines CAG reports) is drawn from:\n[TNPSC Group 2 / Group 1]",
        "stem_ta": "1967 ஆம் ஆண்டு முதல் நடைமுறையில் உள்ள மரபின்படி, சி.ஏ.ஜி அறிக்கைகளை ஆய்வு செய்யும் பொதுக் கணக்குக் குழுவின் (PAC) தலைவர் யாரிடமிருந்து நியமிக்கப்படுகிறார்?\n[டி.என்.பி.எஸ்.சி குரூப் 2 / குரூப் 1]",
        "options": [
            ("The Opposition in Lok Sabha", "மக்களவையின் எதிர்க்கட்சி உறுப்பினர்"),
            ("The ruling party in Lok Sabha", "மக்களவையின் ஆளுங்கட்சி உறுப்பினர்"),
            ("The nominated members of Rajya Sabha", "மாநிலங்களவையின் நியமன உறுப்பினர்"),
            ("Retired Supreme Court judges", "ஓய்வுபெற்ற உச்ச நீதிமன்ற நீதிபதிகள்")
        ],
        "exp_en": "Since 1967, a healthy democratic convention has been established whereby the Speaker of Lok Sabha appoints a senior member of the Opposition as the Chairman of the Public Accounts Committee.",
        "exp_ta": "1967 முதல், மக்களவைத் தலைவர் எதிர்க்கட்சியைச் சேர்ந்த ஒரு மூத்த உறுப்பினரை பொதுக் கணக்குக் குழுவின் (PAC) தலைவராக நியமிக்கும் ஆரோக்கியமான ஜனநாயக மரபு பின்பற்றப்படுகிறது.",
        "tip_en": "Minoo Masani (Swatantra Party) was the first Opposition leader appointed PAC Chairman in 1967.",
        "tip_ta": "1967-ல் மினூ மசானி (சுதந்திரா கட்சி) முதல் எதிர்க்கட்சி PAC தலைவராக நியமிக்கப்பட்டார்.",
        "fact_en": "This ensures unbiased scrutiny of government expenditure.",
        "fact_ta": "இது அரசு செலவினங்கள் மீது நடுநிலையான கண்காணிப்பை உறுதி செய்கிறது."
    },
    # 33
    {
        "subtopic": "Voucher-Level Computerization (VLC)",
        "stem_en": "What is the primary objective of the Voucher Level Computerisation (VLC) system in State AG offices?\n[TNPSC Group 1 / Assistant Director]",
        "stem_ta": "மாநில AG அலுவலகங்களில் உள்ள வவுச்சர் அளவிலான கணினிமயமாக்கல் (VLC) அமைப்பின் முதன்மை நோக்கம் என்ன?\n[டி.என்.பி.எஸ்.சி]",
        "options": [
            ("Capturing treasury expenditure at the individual voucher level to compile State Monthly Civil Accounts", "மாநில மாதாந்திர சிவில் கணக்குகளைத் தொகுக்க கருவூல செலவினங்களை தனிப்பட்ட வவுச்சர் அளவில் பதிவு செய்தல்"),
            ("Issuing voter ID cards for state assembly elections", "சட்டமன்றத் தேர்தல்களுக்கான வாக்காளர் அடையாள அட்டைகளை வழங்குதல்"),
            ("Directly disbursing cash subsidies to farmers' bank accounts", "விவசாயிகளின் வங்கிக் கணக்குகளுக்கு பண மானியங்களை நேரடியாக வழங்குதல்"),
            ("Managing state transport bus ticket reservations", "மாநில போக்குவரத்துக் கழக பேருந்து பயணச்சீட்டு முன்பதிவை நிர்வகித்தல்")
        ],
        "exp_en": "VLC captures granular treasury voucher data from district treasuries, enabling state Accountant General (A&E) offices to compile the Monthly Civil Accounts and Finance Accounts of the State Government.",
        "exp_ta": "மாவட்ட கருவூலங்களிலிருந்து வவுச்சர் வாரியான தகவல்களைப் பெற்று, மாநில அரசின் மாதாந்திர சிவில் கணக்குகள் மற்றும் நிதிக் கணக்குகளைத் தொகுக்க AG (A&E) அலுவலகங்களுக்கு VLC உதவுகிறது.",
        "tip_en": "VLC digitizes state treasury accounting and feeds into State Finance Accounts.",
        "tip_ta": "VLC மாநில கருவூல கணக்குகளை டிஜிட்டல் மயமாக்கி மாநில நிதிக் கணக்குகளுக்கு வழிவகுக்கிறது.",
        "fact_en": "VLC was introduced in state AG offices starting in 2004.",
        "fact_ta": "2004 முதல் மாநில AG அலுவலகங்களில் VLC அறிமுகப்படுத்தப்பட்டது."
    },
    # 34
    {
        "subtopic": "Centre for Data Management and Analytics (CDMA)",
        "stem_en": "The CAG established the Centre for Data Management and Analytics (CDMA) in 2016 primarily to:\n[TNPSC Group 1 / Assistant Director]",
        "stem_ta": "2016-ல் சி.ஏ.ஜியால் தரவு மேலாண்மை மற்றும் பகுப்பாய்வு மையம் (CDMA) நிறுவப்பட்டதன் முதன்மை நோக்கம் என்ன?\n[டி.என்.பி.எஸ்.சி]",
        "options": [
            ("Harness Big Data analytics and Artificial Intelligence in public sector audit", "பொதுத்துறை தணிக்கையில் பெருந்தரவு பகுப்பாய்வு மற்றும் செயற்கை நுண்ணறிவைப் பயன்படுத்துதல்"),
            ("Manufacture computer hardware for central universities", "மத்தியப் பல்கலைக்கழகங்களுக்கு கணினி உபகரணங்களைத் தயாரித்தல்"),
            ("Manage criminal records for the Central Bureau of Investigation", "மத்தியப் புலனாய்வு அமைப்பிற்காக குற்றப் பதிவுகளை நிர்வகித்தல்"),
            ("Issue digital driving licenses across all Union Territories", "அனைத்து ஒன்றியப் பிரதேசங்களிலும் டிஜிட்டல் ஓட்டுநர் உரிமங்களை வழங்குதல்")
        ],
        "exp_en": "Established in 2016, CDMA spearheads the CAG's digital audit strategy, institutionalizing big data analytics, automated audit algorithms, and AI tools across massive digital platforms like GSTN and PFMS.",
        "exp_ta": "2016-ல் அமைக்கப்பட்ட CDMA மையம், ஜி.எஸ்.டி மற்றும் PFMS போன்ற பெரிய டிஜிட்டல் தளங்களில் பெருந்தரவு பகுப்பாய்வு மற்றும் செயற்கை நுண்ணறிவை தணிக்கையில் பயன்படுத்த வழிவகுக்கிறது.",
        "tip_en": "CDMA = Centre for Data Management and Analytics (CAG's big data innovation arm).",
        "tip_ta": "CDMA = தரவு மேலாண்மை மற்றும் பகுப்பாய்வு மையம் (சி.ஏ.ஜியின் பெருந்தரவுப் பிரிவு).",
        "fact_en": "CDMA developed the Big Data Management Policy for IA&AD.",
        "fact_ta": "CDMA அமைப்பு IA&AD துறைக்கான பெருந்தரவு மேலாண்மைக் கொள்கையை உருவாக்கியது."
    },
    # 35
    {
        "subtopic": "OIOS Digital Audit Enterprise",
        "stem_en": "What does the abbreviation 'OIOS' stand for in the context of the CAG of India?\n[TNPSC Group 2 / Group 1]",
        "stem_ta": "இந்திய சி.ஏ.ஜி சூழலில் 'OIOS' என்ற சுருக்கத்தின் விரிவாக்கம் என்ன?\n[டி.என்.பி.எஸ்.சி குரூப் 2 / குரூப் 1]",
        "options": [
            ("One IA&AD One System", "One IA&AD One System"),
            ("Online Internal Oversight Scheme", "Online Internal Oversight Scheme"),
            ("Official Indian Organization Standard", "Official Indian Organization Standard"),
            ("Open Information Operating Software", "Open Information Operating Software")
        ],
        "exp_en": "OIOS stands for 'One IA&AD One System'. It is the enterprise-wide web-based end-to-end digital solution that automates audit planning, execution, reporting, and knowledge management.",
        "exp_ta": "OIOS என்பது 'One IA&AD One System' என்பதைக் குறிக்கிறது. இது தணிக்கைத் திட்டமிடல், செயல்படுத்தல் மற்றும் அறிக்கையிடலை தானியங்கி மயமாக்கும் ஒரு ஒருங்கிணைந்த டிஜிட்டல் தளமாகும்.",
        "tip_en": "OIOS replaced physical paper audit files with a fully digital audit workflow.",
        "tip_ta": "OIOS காகித தணிக்கைக் கோப்புகளை மாற்றி முற்றிலும் டிஜிட்டல் தணிக்கை பணிப்பாய்வை உருவாக்கியது.",
        "fact_en": "OIOS was rolled out across all 150+ audit field offices nationwide.",
        "fact_ta": "நாடு முழுவதும் உள்ள 150-க்கும் மேற்பட்ட தணிக்கை அலுவலகங்களில் OIOS செயல்படுத்தப்பட்டுள்ளது."
    },
    # 36
    {
        "subtopic": "International Centre for Environment Audit (iCED)",
        "stem_en": "Where is the International Centre for Environment Audit and Sustainable Development (iCED) located?\n[TNPSC Group 1 / Group 2]",
        "stem_ta": "சுற்றுச்சூழல் தணிக்கை மற்றும் நிலையான வளர்ச்சிக்கான சர்வதேச மையம் (iCED) எங்கு அமைந்துள்ளது?\n[டி.என்.பி.எஸ்.சி குரூப் 1 / குரூப் 2]",
        "options": [
            ("Jaipur, Rajasthan", "ஜெய்ப்பூர், ராஜஸ்தான்"),
            ("New Delhi", "புது தில்லி"),
            ("Shimla, Himachal Pradesh", "சிம்லா, இமாச்சலப் பிரதேசம்"),
            ("Hyderabad, Telangana", "ஹைதராபாத், தெலுங்கானா")
        ],
        "exp_en": "iCED is located in Jaipur, Rajasthan. It was inaugurated in 2013 as a global centre of excellence for capacity building in environmental auditing under the auspices of INTOSAI.",
        "exp_ta": "iCED ராஜஸ்தான் மாநிலம் ஜெய்ப்பூரில் அமைந்துள்ளது. இது INTOSAI-ன் கீழ் சுற்றுச்சூழல் தணிக்கைக்கான உலகளாவிய சிறப்புப் பயிற்சி மையமாக 2013-ல் தொடங்கப்பட்டது.",
        "tip_en": "iCED Jaipur = Environmental audit centre. NAPA Shimla = Civil service training academy.",
        "tip_ta": "iCED ஜெய்ப்பூர் = சுற்றுச்சூழல் தணிக்கை மையம். NAPA சிம்லா = சிவில் சர்வீஸ் பயிற்சி அகாடமி.",
        "fact_en": "iCED is an IGBC Platinum-rated green building complex.",
        "fact_ta": "iCED வளாகம் IGBC பிளாட்டினம் மதிப்பீடு பெற்ற பசுமை கட்டிடமாகும்."
    },
    # 37
    {
        "subtopic": "National Academy of Audit and Accounts (NAPA)",
        "stem_en": "Where is the National Academy of Audit and Accounts (NAAA / NAPA) located?\n[TNPSC Group 1 / Group 2]",
        "stem_ta": "தேசிய தணிக்கை மற்றும் கணக்கு அகாடமி (NAAA / NAPA) எங்கு அமைந்துள்ளது?\n[டி.என்.பி.எஸ்.சி குரூப் 1 / குரூப் 2]",
        "options": [
            ("Shimla, Himachal Pradesh", "சிம்லா, இமாச்சலப் பிரதேசம்"),
            ("Mussoorie, Uttarakhand", "முசோரி, உத்தராகண்ட்"),
            ("Nagpur, Maharashtra", "நாக்பூர், மகாராஷ்டிரா"),
            ("Hyderabad, Telangana", "ஹைதராபாத், தெலுங்கானா")
        ],
        "exp_en": "The National Academy of Audit and Accounts (NAAA) is located in Shimla, Himachal Pradesh. It is the premier training institution for officers of the Indian Audit and Accounts Service (IA&AS).",
        "exp_ta": "தேசிய தணிக்கை மற்றும் கணக்கு அகாடமி (NAAA) இமாச்சலப் பிரதேசத்தின் சிம்லாவில் அமைந்துள்ளது. இது இந்திய தணிக்கை மற்றும் கணக்கு பணி (IA&AS) அதிகாரிகளுக்கான முதன்மை பயிற்சி நிறுவனமாகும்.",
        "tip_en": "LBSNAA is in Mussoorie; NAAA is in Shimla; SVPNPA is in Hyderabad.",
        "tip_ta": "LBSNAA முசோரியில் உள்ளது; NAAA சிம்லாவில் உள்ளது; SVPNPA ஹைதராபாத்தில் உள்ளது.",
        "fact_en": "NAAA Shimla traces its origins back to the 1950s training school in Chennai (Madras).",
        "fact_ta": "NAAA சிம்லா தனது தொடக்கத்தை 1950களில் சென்னையில் இயங்கிய பயிற்சிப் பள்ளியிலிருந்து பெறுகிறது."
    },
    # 38
    {
        "subtopic": "Section 17 Stores and Stock Audit",
        "stem_en": "Under Section 17 of the CAG Act 1971, the CAG has the authority to audit:\n[TNPSC Group 1 / Assistant Director]",
        "stem_ta": "1971 சி.ஏ.ஜி சட்டத்தின் பிரிவு 17-ன் கீழ் எதனைத் தணிக்கை செய்ய சி.ஏ.ஜிக்கு அதிகாரம் உள்ளது?\n[டி.என்.பி.எஸ்.சி]",
        "options": [
            ("Stores and stock kept in any office or department of the Union or States", "மத்திய அல்லது மாநில அரசுகளின் துறைகளில் உள்ள சரக்குகள் மற்றும் இருப்புக் கணக்குகள்"),
            ("Private gold jewellery lockers in commercial banks", "வணிக வங்கிகளில் உள்ள தனியார் தங்க நகை பெட்டகங்கள்"),
            ("Household assets of civil servants", "அரசு ஊழியர்களின் வீட்டுச் சொத்துக்கள்"),
            ("Foreign embassy diplomatic inventories abroad", "வெளிநாடுகளில் உள்ள இந்திய தூதரகங்களின் இருப்புகள்")
        ],
        "exp_en": "Section 17 of the CAG (DPC) Act 1971 gives the CAG statutory authority to audit and report on the accounts of stores and stock kept in any office or department of the Union or of a State.",
        "exp_ta": "1971 சி.ஏ.ஜி சட்டத்தின் பிரிவு 17, மத்திய அல்லது மாநில அரசின் எந்தவொரு அலுவலகம் அல்லது துறையிலும் வைக்கப்பட்டுள்ள சரக்குகள் மற்றும் இருப்புக் கணக்குகளைத் தணிக்கை செய்ய சி.ஏ.ஜிக்கு சட்டப்பூர்வ அதிகாரம் அளிக்கிறது.",
        "tip_en": "Stores audit scrutinizes procurement, wastage, obsolescence, and physical inventory reconciliations.",
        "tip_ta": "சரக்குத் தணிக்கை கொள்முதல், விரயம், காலாவதியாதல் மற்றும் சரக்கு இருப்பை ஆய்வு செய்கிறது.",
        "fact_en": "Critical stores audits cover defence ordnance depots, railway workshops, and medical supplies.",
        "fact_ta": "ராணுவ ஆயுதக் கிடங்குகள், ரயில்வே பணிமனைகள் மற்றும் மருத்துவப் பொருட்கள் சரக்குத் தணிக்கைக்கு உட்பட்டவை."
    },
    # 39
    {
        "subtopic": "Section 20 Entrustment of Audit",
        "stem_en": "Under Section 20 of the CAG Act 1971, who may entrust the audit of any body or authority to the CAG in the public interest?\n[TNPSC Group 1 / Group 2]",
        "stem_ta": "1971 சி.ஏ.ஜி சட்டத்தின் பிரிவு 20-ன் கீழ் பொது நலன் கருதி எந்தவொரு அமைப்பின் தணிக்கையையும் சி.ஏ.ஜியிடம் ஒப்படைக்க அதிகாரம் கொண்டவர் யார்?\n[டி.என்.பி.எஸ்.சி குரூப் 1 / குரூப் 2]",
        "options": [
            ("The President or the Governor", "குடியரசுத் தலைவர் அல்லது ஆளுநர்"),
            ("The Chief Justice of India", "இந்தியத் தலைமை நீதிபதி"),
            ("The Chairman of the Rajya Sabha", "மாநிலங்களவைத் தலைவர்"),
            ("The Cabinet Secretary", "மத்திய அமைச்சரவைச் செயலாளர்")
        ],
        "exp_en": "Under Section 20(1), the President or the Governor of a State may, in the public interest and after consultation with the CAG, entrust the audit of any body or authority to the CAG.",
        "exp_ta": "பிரிவு 20(1)-ன் படி, பொது நலன் கருதி சி.ஏ.ஜியுடன் கலந்தாலோசித்த பின்னர் குடியரசுத் தலைவர் அல்லது ஆளுநர் எந்தவொரு அமைப்பின் தணிக்கையையும் சி.ஏ.ஜியிடம் ஒப்படைக்கலாம்.",
        "tip_en": "Section 20 allows audit of non-mandated bodies (e.g. Discoms, Universities, Trusts) upon executive request.",
        "tip_ta": "பிரிவு 20 நிர்வாகக் கோரிக்கையின் பேரில் பிற அமைப்புகளின் தணிக்கையை மேற்கொள்ள வழிவகுக்கிறது.",
        "fact_en": "The concerned entity must be given a reasonable opportunity to show cause before entrustment under Section 20(2).",
        "fact_ta": "பிரிவு 20(2)-ன் படி தணிக்கையை ஒப்படைக்கும் முன் சம்பந்தப்பட்ட அமைப்பிற்கு விளக்கம் அளிக்க வாய்ப்பளிக்கப்பட வேண்டும்."
    },
    # 40
    {
        "subtopic": "Difference between Appropriation Accounts and Finance Accounts",
        "stem_en": "What is the primary difference between Appropriation Accounts and Finance Accounts audited by the CAG?\n[TNPSC Group 1 / UPSC]",
        "stem_ta": "சி.ஏ.ஜியால் தணிக்கை செய்யப்படும் ஒதுக்கீட்டுக் கணக்குகள் மற்றும் நிதிக் கணக்குகளுக்கு இடையிலான முதன்மை வேறுபாடு என்ன?\n[டி.என்.பி.எஸ்.சி குரூப் 1]",
        "options": [
            ("Appropriation Accounts compare voted grants with actual expenditure; Finance Accounts show total receipts, disbursements, and debt", "ஒதுக்கீட்டுக் கணக்குகள் மானியங்களை உண்மையான செலவுடன் ஒப்பிடுகின்றன; நிதிக் கணக்குகள் மொத்த வரவு, செலவு மற்றும் கடனைக் காட்டுகின்றன"),
            ("Appropriation Accounts deal with private PSUs; Finance Accounts deal with Panchayats", "ஒதுக்கீட்டுக் கணக்குகள் தனியார் நிறுவனங்களைக் கையாள்கின்றன; நிதிக் கணக்குகள் பஞ்சாயத்துகளைக் கையாள்கின்றன"),
            ("Appropriation Accounts are audited by private auditors; Finance Accounts are audited by CGA", "ஒதுக்கீட்டுக் கணக்குகள் தனியார் தணிக்கையாளர்களால் தணிக்கை செய்யப்படுகின்றன; நிதிக் கணக்குகள் CGA-வால் தணிக்கை செய்யப்படுகின்றன"),
            ("Appropriation Accounts are prepared every five years; Finance Accounts are prepared monthly", "ஒதுக்கீட்டுக் கணக்குகள் ஐந்து ஆண்டுகளுக்கு ஒருமுறை தயாரிக்கப்படுகின்றன; நிதிக் கணக்குகள் மாதாந்திரம் தயாரிக்கப்படுகின்றன")
        ],
        "exp_en": "Appropriation Accounts demonstrate legislative compliance by comparing parliamentary grants with actual expenditure. Finance Accounts present the complete balance sheet of revenue/capital receipts, expenditures, public debt, and liabilities.",
        "exp_ta": "ஒதுக்கீட்டுக் கணக்குகள் நாடாளுமன்ற மானியங்களை உண்மையான செலவினங்களுடன் ஒப்பிட்டு சட்ட இணக்கத்தைக் காட்டுகின்றன. நிதிக் கணக்குகள் வருவாய் வரவுகள், மூலதனச் செலவுகள் மற்றும் பொதுக்கடனை விவரிக்கும் முழுமையான இருப்புநிலைக் குறிப்பாகும்.",
        "tip_en": "Appropriation = Voted grant compliance. Finance = Macro balance sheet and debt profile.",
        "tip_ta": "ஒதுக்கீட்டுக் கணக்கு = வாக்களிக்கப்பட்ட மானிய இணக்கம். நிதிக் கணக்கு = ஒட்டுமொத்த நிதிநிலை மற்றும் கடன்.",
        "fact_en": "Both accounts are prepared annually for both the Union and each State Government.",
        "fact_ta": "மத்திய அரசு மற்றும் ஒவ்வொரு மாநில அரசிற்கும் இவ்விரண்டு கணக்குகளும் ஆண்டுதோறும் தயாரிக்கப்படுகின்றன."
    },
    # 41
    {
        "subtopic": "Dissolution of Lok Sabha Impact",
        "stem_en": "What happens to the audit reports of the CAG tabled in Parliament when the Lok Sabha is dissolved?\n[TNPSC Group 1 / Group 2]",
        "stem_ta": "மக்களவை கலைக்கப்படும் போது நாடாளுமன்றத்தில் வைக்கப்பட்டுள்ள சி.ஏ.ஜி தணிக்கை அறிக்கைகளுக்கு என்ன நேரிடும்?\n[டி.என்.பி.எஸ்.சி குரூப் 1 / குரூப் 2]",
        "options": [
            ("They do not lapse; they remain parliamentary records taken up by the succeeding PAC", "அவை காலாவதியாவதில்லை; அடுத்ததாக அமைக்கப்படும் PAC-ஆல் எடுத்துக்கொள்ளப்படும் நாடாளுமன்ற ஆவணங்களாகத் தொடரும்"),
            ("They automatically lapse and must be re-audited completely", "அவை தானாகவே காலாவதியாகிவிடும் மற்றும் மீண்டும் புதிதாக தணிக்கை செய்யப்பட வேண்டும்"),
            ("They are returned to the CAG for re-submission to the new President", "புதிய குடியரசுத் தலைவரிடம் மீண்டும் சமர்ப்பிக்க சி.ஏ.ஜியிடம் திருப்பி அனுப்பப்படும்"),
            ("They are sent to the Supreme Court for judicial disposal", "நீதிமன்றத் தீர்வுக்காக உச்ச நீதிமன்றத்திற்கு அனுப்பி வைக்கப்படும்")
        ],
        "exp_en": "CAG audit reports laid before Parliament do not lapse upon the dissolution of the Lok Sabha; they remain pending parliamentary business taken up by the next Public Accounts Committee.",
        "exp_ta": "நாடாளுமன்றத்தில் சமர்ப்பிக்கப்பட்ட சி.ஏ.ஜி தணிக்கை அறிக்கைகள் மக்களவை கலைக்கப்படும் போது காலாவதியாவதில்லை; அடுத்ததாக வரும் பொதுக் கணக்குக் குழுவால் தொடர்ந்து ஆய்வு செய்யப்படும்.",
        "tip_en": "Bills may lapse on dissolution under Article 107; constitutional reports laid on the table DO NOT lapse.",
        "tip_ta": "சரத்து 107-ன் கீழ் மசோதாக்கள் காலாவதியாகலாம்; ஆனால் நாடாளுமன்றத்தில் வைக்கப்பட்ட அரசியலமைப்பு அறிக்கைகள் காலாவதியாவதில்லை.",
        "fact_en": "The Secretariat of the PAC maintains continuity of pending audit examination files across general elections.",
        "fact_ta": "PAC செயலகம் பொதுத் தேர்தல்களைக் கடந்தும் நிலுவையில் உள்ள தணிக்கைக் கோப்புகளின் தொடர்ச்சியைப் பராமரிக்கிறது."
    },
    # 42
    {
        "subtopic": "Action Taken Notes (ATNs) Mandate",
        "stem_en": "Within what standard timeframe are Union ministries required to submit Action Taken Notes (ATNs) on CAG audit paragraphs to parliamentary committees?\n[TNPSC Group 1 / Assistant Director]",
        "stem_ta": "சி.ஏ.ஜி தணிக்கைப் பத்திகள் மீது மத்திய அமைச்சகங்கள் எத்தனை மாதங்களுக்குள் நாடாளுமன்றக் குழுக்களுக்கு நடவடிக்கை குறிப்புகளை (ATNs) சமர்ப்பிக்க வேண்டும்?\n[டி.என்.பி.எஸ்.சி]",
        "options": [
            ("Within 4 months", "4 மாதங்களுக்குள்"),
            ("Within 12 months", "12 மாதங்களுக்குள்"),
            ("Within 1 month", "1 மாதத்திற்குள்"),
            ("Within 2 years", "2 ஆண்டுகளுக்குள்")
        ],
        "exp_en": "Ministries are required to submit Action Taken Notes (ATNs) on audit paragraphs to the Public Accounts Committee within four months from the date of tabling of the CAG report.",
        "exp_ta": "சி.ஏ.ஜி அறிக்கை நாடாளுமன்றத்தில் வைக்கப்பட்ட தேதியிலிருந்து நான்கு மாதங்களுக்குள் அமைச்சகங்கள் தணிக்கைப் பத்திகள் மீதான நடவடிக்கைக் குறிப்புகளை (ATNs) PAC-க்கு சமர்ப்பிக்க வேண்டும்.",
        "tip_en": "PAC rules prescribe a strict 4-month window for submitting ATNs.",
        "tip_ta": "ATN சமர்ப்பிக்க PAC விதிகள் 4 மாத காலக்கெடுவை நிர்ணயிக்கின்றன.",
        "fact_en": "Delays in submitting ATNs are severely criticized by the PAC in Action Taken Reports.",
        "fact_ta": "ATN சமர்ப்பிக்க தாமதம் செய்வதை நடவடிக்கை அறிக்கைகளில் PAC கடுமையாக விமர்சிக்கிறது."
    },
    # 43
    {
        "subtopic": "Constituent Assembly: K. Santhanam's Observation",
        "stem_en": "In the Constituent Assembly debates, who famously argued that the title 'Comptroller' was a misnomer for the Indian CAG due to the lack of ex-ante control?\n[TNPSC Group 1 / UPSC]",
        "stem_ta": "அரசியலமைப்பு நிர்ணய சபையில், செலவுக்கு முந்தைய கட்டுப்பாடு இல்லாததால் இந்திய சி.ஏ.ஜிக்கு 'கட்டுப்பாட்டாளர்' என்ற பதவிப் பெயர் ஒரு தவறான சொல் என்று வாதிட்டவர் யார்?\n[டி.என்.பி.எஸ்.சி குரூப் 1]",
        "options": [
            ("K. Santhanam", "கே. சந்தானம்"),
            ("Alladi Krishnaswamy Iyer", "அல்லாடி கிருஷ்ணசுவாமி அய்யர்"),
            ("K.M. Munshi", "கே.எம். முன்ஷி"),
            ("N. Gopalaswami Ayyangar", "என். கோபாலசுவாமி அய்யங்கார்")
        ],
        "exp_en": "K. Santhanam pointed out in the Constituent Assembly that because the officer exercises no control over the issue of money from the exchequer, he is essentially an 'Auditor General' and calling him 'Comptroller' is a misnomer.",
        "exp_ta": "கருவூலத்திலிருந்து பணம் வெளியேறுவதைக் கட்டுப்படுத்தும் அதிகாரம் இல்லாததால், இவர் அடிப்படையில் ஒரு 'தணிக்கைத் தலைவர்' மட்டுமே என்றும் 'கட்டுப்பாட்டாளர்' என்று அழைப்பது பொருந்தாது என்றும் கே. சந்தானம் சுட்டிக்காட்டினார்.",
        "tip_en": "UK CAG = Comptroller + Auditor. Indian CAG = Only Auditor (post-facto).",
        "tip_ta": "பிரிட்டன் சி.ஏ.ஜி = கட்டுப்பாட்டாளர் + தணிக்கையாளர். இந்திய சி.ஏ.ஜி = தணிக்கையாளர் மட்டுமே (செலவுக்குப் பின்).",
        "fact_en": "K. Santhanam later chaired the historic Committee on Prevention of Corruption (1962-64).",
        "fact_ta": "கே. சந்தானம் பின்னர் ஊழல் தடுப்புக் குழுவின் (1962-64) தலைவராகப் பணியாற்றினார்."
    },
    # 44
    {
        "subtopic": "2nd Administrative Reforms Commission (ARC) on CAG",
        "stem_en": "What major reform regarding the CAG was recommended by the Second Administrative Reforms Commission (2nd ARC)?\n[TNPSC Group 1 / UPSC]",
        "stem_ta": "சி.ஏ.ஜி தொடர்பாக இரண்டாவது நிர்வாகச் சீர்திருத்தக் குழு (2வது ARC) பரிந்துரைத்த முக்கிய சீர்திருத்தம் என்ன?\n[டி.என்.பி.எஸ்.சி குரூப் 1]",
        "options": [
            ("Instituting a broad-based collegium including the Prime Minister, CJI, and Leader of Opposition for CAG appointment", "பிரதமர், தலைமை நீதிபதி, எதிர்க்கட்சித் தலைவர் அடங்கிய விரிவான கொலீஜியம் மூலம் சி.ஏ.ஜியை நியமித்தல்"),
            ("Abolishing the office of the CAG and privatizing government audit", "சி.ஏ.ஜி பதவியை ஒழித்துவிட்டு அரசுத் தணிக்கையை தனியார்மயமாக்குதல்"),
            ("Subordinating the CAG directly to the Ministry of Finance", "சி.ஏ.ஜியை நிதி அமைச்சகத்தின் நேரடிக் கட்டுப்பாட்டின் கீழ் கொண்டு வருதல்"),
            ("Making the CAG an ex-officio member of the Union Cabinet", "சி.ஏ.ஜியை மத்திய அமைச்சரவையின் அலுவல் வழி உறுப்பினராக்குதல்")
        ],
        "exp_en": "The Second Administrative Reforms Commission (in its report on Ethics in Governance) recommended that the CAG should be appointed by a collegium consisting of the Prime Minister, the Chief Justice of India, and the Leader of the Opposition.",
        "exp_ta": "இரண்டாவது நிர்வாகச் சீர்திருத்தக் குழு, பிரதமர், இந்தியத் தலைமை நீதிபதி மற்றும் எதிர்க்கட்சித் தலைவர் அடங்கிய கொலீஜியம் மூலம் சி.ஏ.ஜி நியமிக்கப்பட வேண்டும் என்று பரிந்துரைத்தது.",
        "tip_en": "Collegium recommendation aims to prevent unilateral executive discretion in CAG selection.",
        "tip_ta": "சி.ஏ.ஜி தேர்வில் நிர்வாகத்தின் தன்னிச்சையான அதிகாரத்தைத் தடுப்பதே கொலீஜியம் பரிந்துரையின் நோக்கமாகும்.",
        "fact_en": "Currently, appointment is made by the President on the sole advice of the Prime Minister.",
        "fact_ta": "தற்போது நடைமுறையில் பிரதமரின் ஆலோசனையின் பேரில் குடியரசுத் தலைவரால் நியமனம் செய்யப்படுகிறது."
    },
    # 45
    {
        "subtopic": "Audit of Disinvestment (BALCO Audit)",
        "stem_en": "In which landmark 2001 performance audit did the CAG scrutinize enterprise valuation methodologies and asset underpricing during disinvestment?\n[TNPSC Group 1 / Group 2]",
        "stem_ta": "பங்கு விலக்கலின் போது நிறுவன மதிப்பீட்டு முறைகள் மற்றும் சொத்து குறைத்து மதிப்பிடப்பட்டதை எந்த வரலாற்று சிறப்புமிக்க 2001 தணிக்கையில் சி.ஏ.ஜி ஆய்வு செய்தது?\n[டி.என்.பி.எஸ்.சி குரூப் 1 / குரூப் 2]",
        "options": [
            ("BALCO Strategic Disinvestment Audit", "பால்கோ (BALCO) உத்திசார் பங்கு விலக்கல் தணிக்கை"),
            ("Air India Privatization Audit", "ஏர் இந்தியா தனியார்மயமாக்கல் தணிக்கை"),
            ("Maruti Udyog Share Offer Audit", "மாருதி உத்யோக் பங்கு விற்பனை தணிக்கை"),
            ("VSNL Land Transfer Review", "வி.எஸ்.என்.எல் நில பரிமாற்ற மதிப்பாய்வு")
        ],
        "exp_en": "The CAG's 2001 performance audit on the strategic sale of Bharat Aluminium Company (BALCO) closely examined valuation models (DCF vs Asset Valuation) and reserve price setting.",
        "exp_ta": "பாரத் அலுமினியம் நிறுவனத்தின் (BALCO) உத்திசார் விற்பனை மீதான சி.ஏ.ஜியின் 2001 செயல்திறன் தணிக்கை மதிப்பீட்டு மாதிரிகள் மற்றும் அடிப்படை விலை நிர்ணயத்தை தீவிரமாக ஆய்வு செய்தது.",
        "tip_en": "BALCO audit set the precedent for auditing public sector disinvestment valuation transparency.",
        "tip_ta": "பால்கோ தணிக்கை பொதுத்துறை பங்கு விலக்கல் மதிப்பீட்டு வெளிப்படைத்தன்மைக்கு வழிகாட்டியாக அமைந்தது.",
        "fact_en": "The Supreme Court in the BALCO case (2001) upheld the government's economic policy of disinvestment.",
        "fact_ta": "2001 பால்கோ வழக்கில் உச்ச நீதிமன்றம் அரசின் பங்கு விலக்கல் பொருளாதாரக் கொள்கையை உறுதி செய்தது."
    },
    # 46
    {
        "subtopic": "Separation of State Accounts Exception (Goa)",
        "stem_en": "Which Indian State has separated the compilation of its state accounts from the CAG under Section 10 of the 1971 Act?\n[TNPSC Group 1 / Assistant Director]",
        "stem_ta": "1971 சட்டத்தின் பிரிவு 10-ன் கீழ் தனது மாநில கணக்குகளைத் தொகுக்கும் பணியை சி.ஏ.ஜியிடமிருந்து பிரித்துள்ள இந்திய மாநிலம் எது?\n[டி.என்.பி.எஸ்.சி]",
        "options": [
            ("Goa", "கோவா"),
            ("Tamil Nadu", "தமிழ்நாடு"),
            ("Maharashtra", "மகாராஷ்டிரா"),
            ("Uttar Pradesh", "உத்தரப் பிரதேசம்")
        ],
        "exp_en": "Goa (and the Union Territory of Puducherry) has separated the compilation and maintenance of its accounts from the CAG under Section 10 of the CAG (DPC) Act 1971. In all other States, CAG compiles the accounts.",
        "exp_ta": "1971 சி.ஏ.ஜி சட்டத்தின் பிரிவு 10-ன் கீழ் கோவா மாநிலம் (மற்றும் புதுச்சேரி ஒன்றியப் பிரதேசம்) தனது கணக்குகளை சி.ஏ.ஜியிடமிருந்து பிரித்துள்ளது; பிற அனைத்து மாநிலங்களிலும் சி.ஏ.ஜியே கணக்குகளைத் தொகுக்கிறார்.",
        "tip_en": "State accounts exception: Goa compiles its own accounts through its Directorate of Accounts.",
        "tip_ta": "மாநில கணக்கு விதிவிலக்கு: கோவா தனது கணக்கு இயக்ககம் மூலம் தனது சொந்த கணக்குகளைத் தொகுக்கிறது.",
        "fact_en": "Tamil Nadu's accounts are compiled by the Principal Accountant General (A&E), Chennai.",
        "fact_ta": "தமிழ்நாட்டின் கணக்குகள் சென்னை முதன்மை கணக்குத் தலைவர் (A&E) அலுவலகத்தால் தொகுக்கப்படுகின்றன."
    },
    # 47
    {
        "subtopic": "Audit of Goods and Services Tax (GST)",
        "stem_en": "Under the 101st Constitutional Amendment Act, what is the CAG's authority regarding the audit of Goods and Services Tax (GST)?\n[TNPSC Group 1 / Group 2]",
        "stem_ta": "101வது அரசியலமைப்புத் திருத்தச் சட்டத்தின் கீழ், சரக்கு மற்றும் சேவை வரி (GST) தணிக்கை தொடர்பான சி.ஏ.ஜியின் அதிகாரம் என்ன?\n[டி.என்.பி.எஸ்.சி குரூப் 1 / குரூப் 2]",
        "options": [
            ("CAG audits CGST and IGST receipts and has full access to GSTN data for audit analysis", "மத்திய ஜி.எஸ்.டி மற்றும் IGST வரவுகளை சி.ஏ.ஜி தணிக்கை செய்கிறார் மற்றும் GSTN தரவுகளை அணுக முழு உரிமை பெற்றுள்ளார்"),
            ("CAG is completely prohibited from accessing GST Network electronic records", "ஜி.எஸ்.டி நெட்வொர்க் மின்னணு பதிவுகளை அணுக சி.ஏ.ஜிக்கு முற்றிலும் தடை விதிக்கப்பட்டுள்ளது"),
            ("GST is audited exclusively by private chartered accountant consortiums", "ஜி.எஸ்.டி முற்றிலும் தனியார் பட்டயக் கணக்காளர் கூட்டமைப்பால் மட்டுமே தணிக்கை செய்யப்படுகிறது"),
            ("CAG can audit state GST only with the unanimous consent of the GST Council", "ஜி.எஸ்.டி கவுன்சிலின் ஒருமனதான ஒப்புதலுடன் மட்டுமே மாநில ஜி.எஸ்.டியை சி.ஏ.ஜி தணிக்கை செய்ய முடியும்")
        ],
        "exp_en": "Under Section 16 of the 1971 Act read with Article 149, the CAG audits central receipts including CGST and IGST, and accesses GSTN data to verify Input Tax Credit (ITC) matching and revenue devolution.",
        "exp_ta": "சரத்து 149 மற்றும் பிரிவு 16-ன் கீழ் மத்திய ஜி.எஸ்.டி மற்றும் IGST வரவுகளை சி.ஏ.ஜி தணிக்கை செய்வதுடன், உள்ளீட்டு வரி வரவு (ITC) மற்றும் வருவாய்ப் பகிர்வை சரிபார்க்க GSTN தரவுகளை ஆய்வு செய்கிறார்.",
        "tip_en": "CAG's GST reports highlight revenue leakages, fake invoice syndicates, and IGST settlement delays.",
        "tip_ta": "சி.ஏ.ஜியின் ஜி.எஸ்.டி அறிக்கைகள் வரி இழப்புகள், போலி ரசீது முறைகேடுகள் மற்றும் IGST தீர்வு தாமதங்களை வெளிப்படுத்துகின்றன.",
        "fact_en": "The CAG has conducted nationwide IT audits of the GSTN architecture.",
        "fact_ta": "GSTN கட்டமைப்பு மீதான நாடு தழுவிய தகவல் தொழில்நுட்ப தணிக்கையை சி.ஏ.ஜி நடத்தியுள்ளார்."
    },
    # 48
    {
        "subtopic": "Constitutional Bulwarks of Democracy",
        "stem_en": "Which of the following institutions was NOT enumerated by Dr. B.R. Ambedkar as one of the four essential bulwarks of democratic governance in India?\n[TNPSC Group 1 / Group 2]",
        "stem_ta": "இந்தியாவின் ஜனநாயக நிர்வாகத்தின் நான்கு முக்கிய தூண்களில் ஒன்றாக டாக்டர் அம்பேத்கர் பட்டியலிடாத அமைப்பு எது?\n[டி.என்.பி.எஸ்.சி குரூப் 1 / குரூப் 2]",
        "options": [
            ("Planning Commission (NITI Aayog)", "திட்டக் குழு (நிதி ஆயோக்)"),
            ("Comptroller and Auditor General of India", "இந்தியத் தலைமைக் கணக்குத் தணிக்கையாளர்"),
            ("Supreme Court of India", "இந்திய உச்ச நீதிமன்றம்"),
            ("Election Commission of India", "இந்தியத் தேர்தல் ஆணையம்")
        ],
        "exp_en": "Dr. Ambedkar identified the Supreme Court, the Comptroller and Auditor General, the Election Commission, and the Union Public Service Commission as the four constitutional bulwarks of democratic India. The Planning Commission was a non-constitutional executive body.",
        "exp_ta": "உச்ச நீதிமன்றம், சி.ஏ.ஜி, தேர்தல் ஆணையம் மற்றும் UPSC ஆகிய நான்கையுமே ஜனநாயக இந்தியாவின் தூண்களாக அம்பேத்கர் குறிப்பிட்டார். திட்டக் குழு என்பது அரசியலமைப்பு சாராத நிர்வாக அமைப்பாகும்.",
        "tip_en": "Ambedkar's 4 bulwarks: SC, CAG, ECI, UPSC.",
        "tip_ta": "அம்பேத்கரின் 4 ஜனநாயகத் தூண்கள்: உச்ச நீதிமன்றம், சி.ஏ.ஜி, தேர்தல் ஆணையம், UPSC.",
        "fact_en": "All four institutions possess constitutional security of tenure and independent expenses.",
        "fact_ta": "இந்த நான்கு அமைப்புகளுமே அரசியலமைப்புப் பதவிக் காலப் பாதுகாப்பையும் நிதி சுதந்திரத்தையும் பெற்றுள்ளன."
    },
    # 49
    {
        "subtopic": "State Disaster Response Fund (SDRF) Audit",
        "stem_en": "What is the primary focus of CAG audits concerning the State Disaster Response Fund (SDRF)?\n[TNPSC Group 1 / Assistant Director]",
        "stem_ta": "மாநில பேரிடர் மீட்பு நிதி (SDRF) மீதான சி.ஏ.ஜி தணிக்கைகளின் முதன்மை நோக்கம் என்ன?\n[டி.என்.பி.எஸ்.சி]",
        "options": [
            ("Verifying timely credit of central and state shares and ensuring relief funds are not diverted for non-disaster expenses", "மத்திய-மாநில பங்குகள் சரியான நேரத்தில் வரவு வைக்கப்படுவதையும் நிவாரண நிதி பிற செலவுகளுக்கு திருப்பிவிடப்படாமல் இருப்பதையும் உறுதி செய்தல்"),
            ("Ordering army deployments during severe cyclonic storms", "கடுமையான புயல்களின் போது ராணுவத்தை களமிறக்க உத்தரவிடுவது"),
            ("Directly purchasing food packets and relief tents for flood victims", "வெள்ளத்தால் பாதிக்கப்பட்டவர்களுக்கு உணவுப் பொட்டலங்கள் மற்றும் கூடாரங்களை நேரடியாக வாங்குவது"),
            ("Fixing compensation rates for damaged private motor vehicles", "சேதமடைந்த தனியார் வாகனங்களுக்கான இழப்பீட்டுத் தொகையை நிர்ணயிப்பது")
        ],
        "exp_en": "CAG's audit of SDRF verifies whether the Union and State statutory shares were deposited on time into the fund, whether unspent balances earned interest, and whether funds were strictly spent on eligible relief items under MHA norms.",
        "exp_ta": "மத்திய மற்றும் மாநில அரசுகளின் சட்டப்பூர்வ பங்குகள் சரியான நேரத்தில் வைப்பு செய்யப்பட்டனவா, செலவிடப்படாத தொகைக்கு வட்டி கிடைத்ததா, மற்றும் மத்திய வழிகாட்டுதலின்படி மட்டுமே நிதி செலவிடப்பட்டதா என்பதை சி.ஏ.ஜி தணிக்கை செய்கிறது.",
        "tip_en": "SDRF audit prevents state finance departments from using disaster money to manage revenue deficits.",
        "tip_ta": "SDRF தணிக்கை மாநில அரசுகள் பேரிடர் நிதியை பட்ஜெட் பற்றாக்குறையை சமாளிக்கப் பயன்படுத்துவதைத் தடுக்கிறது.",
        "fact_en": "Failure by States to release matching share within 15 days attracts penal interest liabilities.",
        "fact_ta": "15 நாட்களுக்குள் மாநிலப் பங்கை வழங்கத் தவறினால் அபராத வட்டி செலுத்த வேண்டியிருக்கும்."
    },
    # 50
    {
        "subtopic": "Present CAG of India (November 2024)",
        "stem_en": "Who assumed office as the 15th Comptroller and Auditor General of India in November 2024?\n[TNPSC Current Affairs / Polity 2024-25]",
        "stem_ta": "நவம்பர் 2024-ல் இந்தியாவின் 15வது தலைமைக் கணக்குத் தணிக்கையாளராகப் பொறுப்பேற்றவர் யார்?\n[நடப்பு நிகழ்வுகள் / ஆட்சியியல்]",
        "options": [
            ("K. Sanjay Murthy", "கே. சஞ்சய் மூர்த்தி"),
            ("G.C. Murmu", "ஜி.சி. முர்மு"),
            ("Rajiv Mehrishi", "ராஜீவ் மெஹ்ரிஷி"),
            ("Shashi Kant Sharma", "சசி காந்த் சர்மா")
        ],
        "exp_en": "K. Sanjay Murthy, a 1989-batch IAS officer of the Himachal Pradesh cadre who served as Secretary of the Department of Higher Education, was sworn in as the 15th CAG of India in November 2024.",
        "exp_ta": "மத்திய உயர் கல்வித் துறைச் செயலாளராகப் பணியாற்றிய இமாச்சலப் பிரதேச கேடர் ஐ.ஏ.எஸ் அதிகாரி கே. சஞ்சய் மூர்த்தி நவம்பர் 2024-ல் இந்தியாவின் 15வது சி.ஏ.ஜியாகப் பதவிப் பிரமாணம் செய்து கொண்டார்.",
        "tip_en": "Current CAG of India: K. Sanjay Murthy (appointed November 2024 succeeding G.C. Murmu).",
        "tip_ta": "இந்தியாவின் தற்போதைய சி.ஏ.ஜி: கே. சஞ்சய் மூர்த்தி (நவம்பர் 2024-ல் ஜி.சி. முர்முவுக்குப் பின் நியமிக்கப்பட்டார்).",
        "fact_en": "Administered the oath of office by President Droupadi Murmu at Rashtrapati Bhavan.",
        "fact_ta": "குடியரசுத் தலைவர் மாளிகையில் குடியரசுத் தலைவர் திரௌபதி முர்மு பதவிப் பிரமாணம் செய்து வைத்தார்."
    }
]

def build_questions():
    questions = []
    for idx, item in enumerate(raw_pyq_data, start=1):
        qid = f"CAG_PYQ_{idx:03d}"
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
            tags=["polity", "comptroller_and_auditor_general", "pyq_practice", item["subtopic"].lower().replace(" ", "_")]
        )
        questions.append(q)
    return questions

if __name__ == "__main__":
    qs = build_questions()
    print(f"Generated {len(qs)} raw PYQ questions for CAG.")
    
    balanced_qs = balance_question_keys(qs)
    
    out_path = os.path.join("data", "questions", "polity", "cag_pyq.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(balanced_qs, f, ensure_ascii=False, indent=2)
    print(f"Saved balanced PYQ MCQs to {out_path}")
    
    # Also save alias
    alias_path = os.path.join("data", "questions", "polity", "cag_pyq_practice.json")
    with open(alias_path, "w", encoding="utf-8") as f:
        json.dump(balanced_qs, f, ensure_ascii=False, indent=2)
    print(f"Saved alias to {alias_path}")
    
    val = ContentValidator()
    report = val.validate_file(out_path, expected_count=50, expected_prefix="CAG_PYQ_")
    print(f"Validation Report: {'PASS' if report.is_valid else 'FAIL'} | Total: {report.total_audited}")
    if not report.is_valid:
        for iss in report.issues[:10]:
            print(f"  Issue: {iss}")
    print(f"Key Distribution: {report.key_distribution}")
