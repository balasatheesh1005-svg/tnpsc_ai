# -*- coding: utf-8 -*-
"""
Generator for Comptroller & Auditor General of India (CAG) Easy MCQs (50 Questions: CAG_E_001 to CAG_E_050).
Strictly adheres to:
- Full 24-field TNPSC Nova AI schema
- Balanced answer keys (13 A, 13 B, 12 C, 12 D)
- Fully bilingual (English and authentic Tamil)
- Complete why_not_others dict with A, B, C, D in both languages
"""

import json
import os
from cag_mcq_helper import make_cag_q
from rebalance_er_helper import balance_question_keys
from tools.nova_content_engine.validator import ContentValidator

raw_easy_data = [
    # 1
    {
        "subtopic": "Constitutional Provision",
        "stem_en": "Which Article of the Constitution of India provides for the office of the Comptroller and Auditor General of India?",
        "stem_ta": "இந்திய அரசியலமைப்பின் எந்தச் சரத்து இந்தியத் தலைமைக் கணக்குத் தணிக்கையாளர் (CAG) அலுவலகத்திற்கு வகை செய்கிறது?",
        "options": [
            ("Article 148", "சரத்து 148"),
            ("Article 76", "சரத்து 76"),
            ("Article 165", "சரத்து 165"),
            ("Article 280", "சரத்து 280")
        ],
        "exp_en": "Article 148 of the Constitution establishes the office of the Comptroller and Auditor General of India as an independent constitutional authority.",
        "exp_ta": "இந்திய அரசியலமைப்பின் சரத்து 148 இந்தியத் தலைமைக் கணக்குத் தணிக்கையாளர் (CAG) அலுவலகத்தை ஒரு சுயாதீன அரசியலமைப்பு அமைப்பாக நிறுவுகிறது.",
        "tip_en": "Article 148: CAG of India; Article 76: Attorney General; Article 165: Advocate General; Article 280: Finance Commission.",
        "tip_ta": "சரத்து 148: இந்திய சி.ஏ.ஜி; சரத்து 76: தலைமை வழக்கறிஞர்; சரத்து 165: அட்வகேட் ஜெனரல்; சரத்து 280: நிதி ஆணையம்.",
        "fact_en": "Chapter V of Part V of the Constitution (Articles 148-151) deals with the Comptroller and Auditor General of India.",
        "fact_ta": "அரசியலமைப்பின் பகுதி V, அத்தியாயம் V (சரத்துகள் 148-151) இந்தியத் தலைமைக் கணக்குத் தணிக்கையாளரைக் கையாள்கிறது."
    },
    # 2
    {
        "subtopic": "Appointment Authority",
        "stem_en": "Who appoints the Comptroller and Auditor General of India?",
        "stem_ta": "இந்தியத் தலைமைக் கணக்குத் தணிக்கையாளரை (CAG) நியமிப்பவர் யார்?",
        "options": [
            ("The President of India by warrant under his hand and seal", "குடியரசுத் தலைவர் தனது கையொப்பம் மற்றும் முத்திரையிட்ட ஆணை மூலம்"),
            ("The Prime Minister of India directly", "இந்தியப் பிரதமர் நேரடியாக"),
            ("The Chief Justice of India", "இந்தியத் தலைமை நீதிபதி"),
            ("The Public Accounts Committee of Parliament", "நாடாளுமன்றத்தின் பொதுக் கணக்குக் குழு")
        ],
        "exp_en": "Under Article 148(1), the Comptroller and Auditor General of India is appointed by the President by warrant under his hand and seal.",
        "exp_ta": "சரத்து 148(1)-ன் கீழ் இந்தியத் தலைமைக் கணக்குத் தணிக்கையாளர் குடியரசுத் தலைவரால் தனது கையொப்பம் மற்றும் முத்திரையிட்ட ஆணை (warrant under hand and seal) மூலம் நியமிக்கப்படுகிறார்.",
        "tip_en": "Officers appointed by warrant under President's hand and seal: SC/HC Judges, CAG, Governors.",
        "tip_ta": "குடியரசுத் தலைவரின் கைப்பட கையொப்பமிட்ட ஆணை மூலம் நியமிக்கப்படுபவர்கள்: உச்ச/உயர் நீதிமன்ற நீதிபதிகள், CAG, ஆளுநர்கள்.",
        "fact_en": "Appointment by warrant signifies high constitutional status and independence.",
        "fact_ta": "முத்திரையிட்ட ஆணை மூலம் நியமிக்கப்படுவது உயரிய அரசியலமைப்பு அந்தஸ்தையும் சுதந்திரத்தையும் குறிக்கிறது."
    },
    # 3
    {
        "subtopic": "Tenure of Office",
        "stem_en": "What is the term of office of the Comptroller and Auditor General of India?",
        "stem_ta": "இந்தியத் தலைமைக் கணக்குத் தணிக்கையாளரின் பதவிக்காலம் என்ன?",
        "options": [
            ("6 years or up to 65 years of age, whichever is earlier", "6 ஆண்டுகள் அல்லது 65 வயது நிறைவடையும் வரை, எது முந்தையதோ அது"),
            ("5 years or up to 62 years of age, whichever is earlier", "5 ஆண்டுகள் அல்லது 62 வயது நிறைவடையும் வரை, எது முந்தையதோ அது"),
            ("5 years or up to 65 years of age, whichever is earlier", "5 ஆண்டுகள் அல்லது 65 வயது நிறைவடையும் வரை, எது முந்தையதோ அது"),
            ("Holds office during the pleasure of the President", "குடியரசுத் தலைவரின் விருப்பம் உள்ளவரை பதவியில் நீடிப்பார்")
        ],
        "exp_en": "Under the CAG's (Duties, Powers and Conditions of Service) Act, 1971, the CAG holds office for a term of 6 years or until he attains the age of 65 years, whichever is earlier.",
        "exp_ta": "1971-ம் ஆண்டின் CAG (கடமைகள், அதிகாரங்கள் மற்றும் பணி நிபந்தனைகள்) சட்டத்தின்படி, சி.ஏ.ஜி 6 ஆண்டுகள் அல்லது 65 வயது வரை, எது முந்தையதோ அதுவரை பதவி வகிக்கிறார்.",
        "tip_en": "CAG tenure: 6 years or 65 years (same as UPSC Chairman, CEC).",
        "tip_ta": "CAG பதவிக்காலம்: 6 ஆண்டுகள் அல்லது 65 வயது (UPSC தலைவர், CEC போன்றே).",
        "fact_en": "CAG does not hold office during the pleasure of the President; he has constitutional security of tenure.",
        "fact_ta": "CAG குடியரசுத் தலைவரின் விருப்பம் உள்ளவரை பதவி வகிப்பதில்லை; அவருக்கு அரசியலமைப்புப் பணிப் பாதுகாப்பு உண்டு."
    },
    # 4
    {
        "subtopic": "Removal Procedure",
        "stem_en": "The Comptroller and Auditor General of India can be removed from office only in like manner and on like grounds as:",
        "stem_ta": "இந்தியத் தலைமைக் கணக்குத் தணிக்கையாளர் பின்வரும் எந்தப் பதவிக்குரிய அதே நடைமுறை மற்றும் காரணங்களின் அடிப்படையில் மட்டுமே நீக்கப்பட முடியும்?",
        "options": [
            ("A Judge of the Supreme Court of India", "இந்திய உச்ச நீதிமன்ற நீதிபதி"),
            ("The Attorney General of India", "இந்தியத் தலைமை வழக்கறிஞர்"),
            ("The Cabinet Secretary to the Government of India", "இந்திய அரசாங்கத்தின் தலைமைச் செயலாளர்"),
            ("A Member of the Union Council of Ministers", "மத்திய அமைச்சரவை உறுப்பினர்")
        ],
        "exp_en": "Article 148(1) provides that the CAG can be removed from office only in like manner and on like grounds as a Judge of the Supreme Court (proved misbehaviour or incapacity, with special majority in Parliament).",
        "exp_ta": "சரத்து 148(1)-ன் படி, உச்ச நீதிமன்ற நீதிபதியை நீக்கும் அதே நடைமுறை மற்றும் காரணங்களின் அடிப்படையில் (நிரூபிக்கப்பட்ட தவறான நடத்தை அல்லது திறமையின்மை, நாடாளுமன்ற சிறப்பு பெரும்பான்மை) மட்டுமே CAG-ஐ நீக்க முடியும்.",
        "tip_en": "Removed like SC Judge: CAG, Chief Election Commissioner, State Election Commissioner.",
        "tip_ta": "உச்ச நீதிமன்ற நீதிபதி போல நீக்கப்படுபவர்கள்: CAG, தலைமைத் தேர்தல் ஆணையர், மாநிலத் தேர்தல் ஆணையர்.",
        "fact_en": "No Comptroller and Auditor General of India has ever been impeached or removed from office.",
        "fact_ta": "இந்திய வரலாற்றில் இதுவரை எந்த ஒரு CAG-யும் பதவிநீக்கம் செய்யப்பட்டதில்லை."
    },
    # 5
    {
        "subtopic": "Post-Retirement Disqualification",
        "stem_en": "Under Article 148(4), what is the constitutional restriction placed on the Comptroller and Auditor General after vacating office?",
        "stem_ta": "சரத்து 148(4)-ன் கீழ், பதவிக்காலம் முடிந்த பிறகு இந்தியத் தலைமைக் கணக்குத் தணிக்கையாளர் மீது விதிக்கப்படும் அரசியலமைப்புத் தடை என்ன?",
        "options": [
            ("Ineligible for further office either under the Government of India or under the Government of any State", "இந்திய அரசாங்கத்தின் கீழோ அல்லது எந்தவொரு மாநில அரசாங்கத்தின் கீழோ மேலும் எந்தப் பதவியும் வகிக்க தகுதியற்றவர்"),
            ("Cannot practice as a lawyer in any court for three years only", "மூன்று ஆண்டுகளுக்கு மட்டுமே எந்த நீதிமன்றத்திலும் வழக்கறிஞராகப் பணியாற்ற முடியாது"),
            ("Eligible only to become the Governor of a State immediately", "உடனடியாக ஒரு மாநிலத்தின் ஆளுநராக மட்டுமே ஆகத் தகுதியுடையவர்"),
            ("Can accept any private commercial appointment without permission", "அனுமதியின்றி எந்தவொரு தனியார் வணிகப் பதவியையும் ஏற்கலாம்")
        ],
        "exp_en": "Article 148(4) explicitly provides: 'The Comptroller and Auditor-General shall not be eligible for further office either under the Government of India or under the Government of any State after he has ceased to hold his office.'",
        "exp_ta": "சரத்து 148(4) தெளிவாகக் கூறுகிறது: 'தலைமைக் கணக்குத் தணிக்கையாளர் தனது பதவிக்காலம் முடிந்த பிறகு, இந்திய அரசாங்கத்தின் கீழோ அல்லது எந்தவொரு மாநில அரசாங்கத்தின் கீழோ மேலும் எந்தவொரு பதவியையும் வகிக்க தகுதியற்றவர் ஆவார்.'",
        "tip_en": "Post-retirement ban on government office protects the CAG from executive blandishments or post-retirement favors.",
        "tip_ta": "ஓய்வுக்குப் பிந்தைய அரசுப் பதவித் தடை, நிர்வாகத்தின் கவர்ச்சிகரமான வாக்குறுதிகளிலிருந்து சி.ஏ.ஜி-யின் நடுநிலைமையைப் பாதுகாக்கிறது.",
        "fact_en": "This is an absolute constitutional bar against both Union and State Government employment.",
        "fact_ta": "இது மத்திய மற்றும் மாநில அரசுப் பணிகள் இரண்டிற்குமான முழுமையான அரசியலமைப்புத் தடையாகும்."
    },
    # 6
    {
        "subtopic": "Constitutional Oath",
        "stem_en": "Under which Schedule of the Constitution of India does the Comptroller and Auditor General take the oath of office?",
        "stem_ta": "இந்திய அரசியலமைப்பின் எந்த அட்டவணையின் கீழ் தலைமைக் கணக்குத் தணிக்கையாளர் பதவிப் பிரமாணம் எடுத்துக் கொள்கிறார்?",
        "options": [
            ("Third Schedule (Form IV)", "மூன்றாவது அட்டவணை (படிவம் IV)"),
            ("Second Schedule", "இரண்டாவது அட்டவணை"),
            ("Fourth Schedule", "நான்காவது அட்டவணை"),
            ("Seventh Schedule", "ஏழாவது அட்டவணை")
        ],
        "exp_en": "Under Article 148(2), the CAG makes and subscribes an oath or affirmation before the President according to Form IV set out in the Third Schedule.",
        "exp_ta": "சரத்து 148(2)-ன் படி, மூன்றாவது அட்டவணையின் படிவம் IV-ல் குறிப்பிடப்பட்டுள்ளவாறு குடியரசுத் தலைவரின் முன்னிலையில் CAG பதவிப் பிரமாணம் எடுத்துக் கொள்கிறார்.",
        "tip_en": "Third Schedule: Form IV = CAG of India. (Remember Attorney General has NO oath in 3rd Schedule).",
        "tip_ta": "மூன்றாவது அட்டவணை: படிவம் IV = இந்திய CAG. (அட்டர்னி ஜெனரலுக்கு 3-வது அட்டவணையில் உறுதிமொழி இல்லை).",
        "fact_en": "The oath binds the CAG to perform his duties without fear or favour, affection or ill-will.",
        "fact_ta": "பயமோ தயவோ, விருப்போ வெறுப்போ இன்றி கடமைகளைச் செய்ய இந்த உறுதிமொழி CAG-ஐக் கட்டுப்படுத்துகிறது."
    },
    # 7
    {
        "subtopic": "Charging of Expenses",
        "stem_en": "Where are the salary, allowances, and administrative expenses of the office of the Comptroller and Auditor General charged?",
        "stem_ta": "இந்தியத் தலைமைக் கணக்குத் தணிக்கையாளர் அலுவலகத்தின் ஊதியம், படிகள் மற்றும் நிர்வாகச் செலவுகள் எதிலிருந்து செலவிடப்படுகின்றன?",
        "options": [
            ("Consolidated Fund of India (non-votable by Parliament)", "இந்தியத் திரட்டப்பட்ட நிதி (நாடாளுமன்றத்தில் வாக்கெடுப்புக்கு உட்படாதது)"),
            ("Contingency Fund of India", "இந்திய அவசரகால நிதி"),
            ("Public Account of India", "இந்தியப் பொதுக் கணக்கு"),
            ("Voted annually in the budget by the Lok Sabha", "மக்களவையில் பட்ஜெட்டில் ஆண்டுதோறும் வாக்களிக்கப்படும் நிதி")
        ],
        "exp_en": "Under Article 148(6), the administrative expenses of the office of the CAG, including all salaries, allowances, and pensions, are charged upon the Consolidated Fund of India and are non-votable.",
        "exp_ta": "சரத்து 148(6)-ன் கீழ், ஊதியங்கள், படிகள் மற்றும் ஓய்வூதியங்கள் உட்பட CAG அலுவலகத்தின் நிர்வாகச் செலவுகள் இந்தியத் திரட்டப்பட்ட நிதியில் சார்ஜ் செய்யப்படுகின்றன மற்றும் வாக்கெடுப்புக்கு அப்பாற்பட்டவை.",
        "tip_en": "'Charged upon' means Parliament can discuss it, but cannot vote or reduce it.",
        "tip_ta": "'சார்ஜ் செய்யப்பட்டது' என்றால் நாடாளுமன்றத்தில் விவாதிக்கலாமே தவிர, வாக்கெடுப்பு நடத்தவோ குறைக்கவோ முடியாது.",
        "fact_en": "Article 112(3)(e) also lists CAG expenses as charged expenditure on the Consolidated Fund of India.",
        "fact_ta": "சரத்து 112(3)(e)-ம் CAG செலவினங்களை இந்தியத் திரட்டப்பட்ட நிதியில் சார்ஜ் செய்யப்பட்ட செலவாகப் பட்டியலிடுகிறது."
    },
    # 8
    {
        "subtopic": "Constitutional Title and Role",
        "stem_en": "The Comptroller and Auditor General of India is widely described by constitutional experts and courts as the:",
        "stem_ta": "அரசியலமைப்பு வல்லுநர்கள் மற்றும் நீதிமன்றங்களால் இந்தியத் தலைமைக் கணக்குத் தணிக்கையாளர் பரவலாக எவ்வாறு வர்ணிக்கப்படுகிறார்?",
        "options": [
            ("Guardian of the Public Purse", "பொதுக் கருவூலத்தின் பாதுகாவலர் (Guardian of the Public Purse)"),
            ("Supreme Commander of Financial Armed Forces", "நிதிப் படைகளின் தலைமைத் தளபதி"),
            ("Chief Executive Officer of the Reserve Bank of India", "இந்திய ரிசர்வ் வங்கியின் முதன்மைச் செயல் அதிகாரி"),
            ("Permanent Chairman of the Planning Commission", "திட்டக் குழுவின் நிரந்தரத் தலைவர்")
        ],
        "exp_en": "The CAG is the guardian of the public purse, ensuring that not a single paisa is spent from the Consolidated Fund without parliamentary sanction.",
        "exp_ta": "நாடாளுமன்றத்தின் அனுமதியின்றி திரட்டப்பட்ட நிதியிலிருந்து ஒரு பைசா கூட செலவிடப்படாமல் இருப்பதை உறுதி செய்யும் பொதுக் கருவூலத்தின் பாதுகாவலராக சி.ஏ.ஜி விளங்குகிறார்.",
        "tip_en": "Guardian of Public Purse = CAG; Guardian of Constitution / Fundamental Rights = Supreme Court.",
        "tip_ta": "பொதுக் கருவூலத்தின் பாதுகாவலர் = CAG; அரசியலமைப்பு மற்றும் அடிப்படை உரிமைகளின் பாதுகாவலர் = உச்ச நீதிமன்றம்.",
        "fact_en": "The CAG controls the entire financial system of the country at both Union and State levels.",
        "fact_ta": "மத்திய மற்றும் மாநில ஆகிய இரு நிலைகளிலும் நாட்டின் ஒட்டுமொத்த நிதி அமைப்பையும் சி.ஏ.ஜி கண்காணிக்கிறார்."
    },
    # 9
    {
        "subtopic": "Dr. B.R. Ambedkar's Tribute",
        "stem_en": "Who in the Constituent Assembly observed: 'The Comptroller and Auditor General is by far the most important officer under the Constitution of India'?",
        "stem_ta": "'இந்திய அரசியலமைப்பின் கீழ் உள்ள மிக முக்கியமான அதிகாரி தலைமைக் கணக்குத் தணிக்கையாளர் ஆவார்' என்று அரசியல் நிர்ணய சபையில் குறிப்பிட்டவர் யார்?",
        "options": [
            ("Dr. B.R. Ambedkar", "டாக்டர் பி.ஆர். அம்பேத்கர்"),
            ("Jawaharlal Nehru", "ஜவஹர்லால் நேரு"),
            ("Sardar Vallabhbhai Patel", "சர்தார் வல்லபாய் படேல்"),
            ("Dr. Rajendra Prasad", "டாக்டர் ராஜேந்திர பிரசாத்")
        ],
        "exp_en": "Dr. B.R. Ambedkar stated in the Constituent Assembly that the CAG is by far the most important officer under the Constitution of India, ranking him among the four bulwarks of Indian democracy.",
        "exp_ta": "இந்திய ஜனநாயகத்தின் நான்கு தூண்களில் ஒன்றாக சி.ஏ.ஜி-யைக் குறிப்பிட்ட டாக்டர் பி.ஆர். அம்பேத்கர், அரசியலமைப்பின் கீழ் உள்ள மிக முக்கியமான அதிகாரி சி.ஏ.ஜி என்று கூறினார்.",
        "tip_en": "Ambedkar's 4 democratic bulwarks: Supreme Court, Election Commission, UPSC, and CAG.",
        "tip_ta": "அம்பேத்கரின் 4 ஜனநாயகத் தூண்கள்: உச்ச நீதிமன்றம், தேர்தல் ஆணையம், யு.பி.எஸ்.சி, மற்றும் சி.ஏ.ஜி.",
        "fact_en": "Ambedkar placed the duties of the CAG above even those of the judiciary in financial accountability.",
        "fact_ta": "நிதிப் பொறுப்புடைமையில் நீதித்துறையை விடவும் சி.ஏ.ஜி-யின் கடமைகள் முதன்மையானவை என்று அம்பேத்கர் கருதினார்."
    },
    # 10
    {
        "subtopic": "Submission of Audit Reports",
        "stem_en": "Under Article 151(1) of the Constitution, to whom does the Comptroller and Auditor General submit his audit reports relating to the accounts of the Union?",
        "stem_ta": "அரசியலமைப்பின் சரத்து 151(1)-ன் கீழ், மத்திய அரசின் கணக்குகள் தொடர்பான தணிக்கை அறிக்கைகளை சி.ஏ.ஜி யாரிடம் சமர்ப்பிக்கிறார்?",
        "options": [
            ("The President of India", "இந்தியக் குடியரசுத் தலைவர்"),
            ("The Prime Minister of India", "இந்தியப் பிரதமர்"),
            ("The Speaker of the Lok Sabha", "மக்களவைத் தலைவர் (சபாநாயகர்)"),
            ("The Union Finance Minister", "மத்திய நிதி அமைச்சர்")
        ],
        "exp_en": "Article 151(1) states that the reports of the CAG relating to the accounts of the Union shall be submitted to the President, who causes them to be laid before each House of Parliament.",
        "exp_ta": "சரத்து 151(1)-ன் படி, மத்திய அரசின் கணக்குகள் தொடர்பான CAG-யின் அறிக்கைகள் குடியரசுத் தலைவரிடம் சமர்ப்பிக்கப்படும்; அவர் அவற்றை நாடாளுமன்றத்தின் இரு அவைகளிலும் வைப்பார்.",
        "tip_en": "Union audit reports -> President -> Parliament. State audit reports -> Governor -> State Legislature.",
        "tip_ta": "மத்திய தணிக்கை அறிக்கைகள் -> குடியரசுத் தலைவர் -> நாடாளுமன்றம். மாநில அறிக்கைகள் -> ஆளுநர் -> சட்டமன்றம்.",
        "fact_en": "Article 151 is the direct constitutional bridge connecting the audit findings of the CAG to the legislature.",
        "fact_ta": "சரத்து 151 என்பது CAG-யின் தணிக்கை முடிவுகளை சட்டமன்றத்துடன் இணைக்கும் நேரடி அரசியலமைப்புப் பாலமாகும்."
    },
    # 11
    {
        "subtopic": "State Audit Reports",
        "stem_en": "Under Article 151(2) of the Constitution, to whom does the Comptroller and Auditor General submit audit reports relating to the accounts of a State?",
        "stem_ta": "அரசியலமைப்பின் சரத்து 151(2)-ன் கீழ், ஒரு மாநிலத்தின் கணக்குகள் தொடர்பான தணிக்கை அறிக்கைகளை சி.ஏ.ஜி யாரிடம் சமர்ப்பிக்கிறார்?",
        "options": [
            ("The Governor of the State", "மாநில ஆளுநர்"),
            ("The Chief Minister of the State", "மாநில முதலமைச்சர்"),
            ("The Speaker of the Legislative Assembly", "சட்டமன்றப் பேரவைத் தலைவர்"),
            ("The State Finance Minister", "மாநில நிதி அமைச்சர்")
        ],
        "exp_en": "Under Article 151(2), the reports of the CAG relating to the accounts of a State are submitted to the Governor of the State, who causes them to be laid before the State Legislature.",
        "exp_ta": "சரத்து 151(2)-ன் கீழ், மாநிலக் கணக்குகள் தொடர்பான CAG-யின் அறிக்கைகள் மாநில ஆளுநரிடம் சமர்ப்பிக்கப்படும்; அவர் அவற்றை மாநில சட்டமன்றத்தில் சமர்ப்பிக்கச் செய்வார்.",
        "tip_en": "CAG submits reports to the constitutional head: President for Union, Governor for State.",
        "tip_ta": "அரசியலமைப்புத் தலைவரிடமே CAG அறிக்கைகளைச் சமர்ப்பிக்கிறார்: மத்திய அரசுக்கு குடியரசுத் தலைவர், மாநில அரசுக்கு ஆளுநர்.",
        "fact_en": "In the State Legislature, the report is examined in detail by the State Public Accounts Committee.",
        "fact_ta": "மாநில சட்டமன்றத்தில் இந்த அறிக்கை மாநிலப் பொதுக் கணக்குக் குழுவால் விரிவாக ஆராயப்படுகிறது."
    },
    # 12
    {
        "subtopic": "Parliamentary Committee Interface",
        "stem_en": "The Comptroller and Auditor General of India acts as a 'friend, philosopher, and guide' to which parliamentary committee?",
        "stem_ta": "இந்தியத் தலைமைக் கணக்குத் தணிக்கையாளர் பின்வரும் எந்த நாடாளுமன்றக் குழுவின் 'நண்பன், தத்துவவாதி மற்றும் வழிகாட்டியாக' செயல்படுகிறார்?",
        "options": [
            ("Public Accounts Committee (PAC)", "பொதுக் கணக்குக் குழு (PAC)"),
            ("Estimates Committee", "மதிப்பீட்டுக் குழு"),
            ("Committee on Petitions", "மனுக்கள் மீதான குழு"),
            ("Business Advisory Committee", "அலுவல் ஆலோசனைக் குழு")
        ],
        "exp_en": "The CAG acts as a guide, friend, and philosopher to the Public Accounts Committee (PAC) of Parliament, assisting it in examining audit reports and holding the executive accountable.",
        "exp_ta": "நாடாளுமன்றத்தின் பொதுக் கணக்குக் குழுவிற்கு (PAC) தணிக்கை அறிக்கைகளை ஆராய்வதிலும் நிர்வாகத்தை பொறுப்பேற்கச் செய்வதிலும் CAG ஒரு நண்பன், தத்துவவாதி மற்றும் வழிகாட்டியாக உதவுகிறார்.",
        "tip_en": "CAG assists PAC (Public Accounts Committee) and COPU (Committee on Public Undertakings).",
        "tip_ta": "சி.ஏ.ஜி பொதுக் கணக்குக் குழு (PAC) மற்றும் பொதுத்துறை நிறுவனங்கள் குழுவுக்கு (COPU) உதவுகிறார்.",
        "fact_en": "The PAC is always headed by a senior member from the Opposition party by convention since 1967.",
        "fact_ta": "1967 முதல் உள்ள மரபுப்படி பொதுக் கணக்குக் குழுவின் தலைவராக எதிர்க்கட்சியைச் சேர்ந்த மூத்த உறுப்பினரே நியமிக்கப்படுகிறார்."
    },
    # 13
    {
        "subtopic": "Audit Reports Classification",
        "stem_en": "How many annual audit reports are submitted by the Comptroller and Auditor General to the President of India?",
        "stem_ta": "இந்தியக் குடியரசுத் தலைவரிடம் தலைமைக் கணக்குத் தணிக்கையாளரால் ஆண்டுதோறும் எத்தனை தணிக்கை அறிக்கைகள் சமர்ப்பிக்கப்படுகின்றன?",
        "options": [
            ("Three reports: Appropriation Accounts, Finance Accounts, and Commercial/Public Undertakings", "மூன்று அறிக்கைகள்: ஒதுக்கீட்டுக் கணக்குகள், நிதிக் கணக்குகள் மற்றும் வணிக/பொதுத்துறை நிறுவனங்கள்"),
            ("Only one consolidated report", "ஒரே ஒரு ஒருங்கிணைந்த அறிக்கை மட்டுமே"),
            ("Two reports: Revenue and Capital accounts", "இரண்டு அறிக்கைகள்: வருவாய் மற்றும் மூலதனக் கணக்குகள்"),
            ("Five reports, one for each economic sector", "ஒவ்வொரு பொருளாதாரத் துறைக்கும் ஒன்றாக ஐந்து அறிக்கைகள்")
        ],
        "exp_en": "The CAG submits three audit reports to the President: (1) Audit report on Appropriation Accounts, (2) Audit report on Finance Accounts, and (3) Audit report on Commercial / Public Undertakings.",
        "exp_ta": "குடியரசுத் தலைவரிடம் CAG மூன்று தணிக்கை அறிக்கைகளைச் சமர்ப்பிக்கிறார்: (1) ஒதுக்கீட்டுக் கணக்குகள் மீதான தணிக்கை அறிக்கை, (2) நிதிக் கணக்குகள் மீதான அறிக்கை, மற்றும் (3) வணிக/பொதுத்துறை நிறுவனங்கள் மீதான அறிக்கை.",
        "tip_en": "Remember the three reports: Appropriation, Finance, and Public Undertakings.",
        "tip_ta": "மூன்று அறிக்கைகளை நினைவில் வையுங்கள்: ஒதுக்கீட்டுக் கணக்குகள், நிதிக் கணக்குகள், பொதுத்துறை நிறுவனங்கள்.",
        "fact_en": "Appropriation accounts compare actual expenditure with the expenditure sanctioned by Parliament via Appropriation Act.",
        "fact_ta": "ஒதுக்கீட்டுக் கணக்குகள் நாடாளுமன்றத்தால் அனுமதிக்கப்பட்ட தொகையுடன் உண்மையான செலவினங்களை ஒப்பிடுகின்றன."
    },
    # 14
    {
        "subtopic": "Separation of Accounts from Audit",
        "stem_en": "In which year was the accounting function separated from the auditing function for the Union Government, relieving the CAG of bookkeeping duties?",
        "stem_ta": "மத்திய அரசில் கணக்கு வைக்கும் பணியிலிருந்து தணிக்கைப் பணி எந்த ஆண்டு பிரிக்கப்பட்டு, சி.ஏ.ஜி கணக்கு எழுதும் பொறுப்பிலிருந்து விடுவிக்கப்பட்டார்?",
        "options": [
            ("1976", "1976"),
            ("1950", "1950"),
            ("1971", "1971"),
            ("1991", "1991")
        ],
        "exp_en": "In 1976, through an amendment to the CAG's (DPC) Act 1971, the compilation of accounts of the Union was separated from audit. Accounting was departmentalised under the Controller General of Accounts (CGA).",
        "exp_ta": "1976-ல், 1971-ம் ஆண்டின் CAG சட்டத்தில் செய்யப்பட்ட திருத்தத்தின் மூலம், மத்திய அரசின் கணக்குகள் தணிக்கையிலிருந்து பிரிக்கப்பட்டு, கணக்குத் துறை கட்டுப்பாட்டு அதிகாரி (CGA) வசம் ஒப்படைக்கப்பட்டது.",
        "tip_en": "1976: Separation of Accounts and Audit for Union. For States, CAG still maintains both accounts and audit in most States.",
        "tip_ta": "1976: மத்திய அரசில் கணக்கும் தணிக்கையும் பிரிப்பு. ஆனால் மாநிலங்களில் CAG இன்னும் கணக்கு மற்றும் தணிக்கை இரண்டையுமே செய்கிறார்.",
        "fact_en": "The Controller General of Accounts (CGA) is in the Department of Expenditure, Ministry of Finance, and is not a constitutional post.",
        "fact_ta": "கணக்குத் துறை கட்டுப்பாட்டு அதிகாரி (CGA) நிதி அமைச்சகத்தின் கீழ் உள்ள அதிகாரி ஆவார், அரசியலமைப்புப் பதவி அல்ல."
    },
    # 15
    {
        "subtopic": "First CAG of Independent India",
        "stem_en": "Who served as the first Comptroller and Auditor General of Independent India?",
        "stem_ta": "சுதந்திர இந்தியாவின் முதலாவது தலைமைக் கணக்குத் தணிக்கையாளராகப் (CAG) பணியாற்றியவர் யார்?",
        "options": [
            ("V. Narahari Rao", "வி. நரஹரி ராவ்"),
            ("A.K. Chanda", "ஏ.கே. சந்தா"),
            ("A.K. Roy", "ஏ.கே. ராய்"),
            ("S. Ranganathan", "எஸ். ரங்கநாதன்")
        ],
        "exp_en": "V. Narahari Rao served as the first Comptroller and Auditor General of independent India from 1948 to 1954.",
        "exp_ta": "வி. நரஹரி ராவ் 1948 முதல் 1954 வரை சுதந்திர இந்தியாவின் முதல் தலைமைக் கணக்குத் தணிக்கையாளராகப் பணியாற்றினார்.",
        "tip_en": "First CAG of India = V. Narahari Rao (1948-1954). First Attorney General = M.C. Setalvad.",
        "tip_ta": "முதல் இந்திய CAG = வி. நரஹரி ராவ் (1948-1954). முதல் தலைமை வழக்கறிஞர் = எம்.சி. செடல்வாட்.",
        "fact_en": "V. Narahari Rao laid the institutional foundations of the Indian Audit and Accounts Department in free India.",
        "fact_ta": "வி. நரஹரி ராவ் சுதந்திர இந்தியாவில் இந்தியத் தணிக்கை மற்றும் கணக்குத் துறையின் நிறுவன அடித்தளத்தை அமைத்தார்."
    },
    # 16
    {
        "subtopic": "Net Proceeds Certification",
        "stem_en": "Under Article 279 of the Constitution, whose certificate is final regarding the ascertainment and determination of the 'net proceeds' of any tax or duty?",
        "stem_ta": "அரசியலமைப்பின் சரத்து 279-ன் கீழ், எந்தவொரு வரி அல்லது கட்டணத்தின் 'நிகர வருவாயைக்' கணக்கிட்டு தீர்மானிப்பதில் யாருடைய சான்றிதழ் இறுதியானது?",
        "options": [
            ("The Comptroller and Auditor General of India", "இந்தியத் தலைமைக் கணக்குத் தணிக்கையாளர் (CAG)"),
            ("The Chairman of the Finance Commission", "நிதி ஆணையத்தின் தலைவர்"),
            ("The Governor of the Reserve Bank of India", "இந்திய ரிசர்வ் வங்கியின் ஆளுநர்"),
            ("The Union Finance Minister", "மத்திய நிதி அமைச்சர்")
        ],
        "exp_en": "Under Article 279(1), the net proceeds of any tax or duty are ascertained and certified by the Comptroller and Auditor General of India, whose certificate is final.",
        "exp_ta": "சரத்து 279(1)-ன் கீழ், எந்தவொரு வரியின் நிகர வருவாயும் சி.ஏ.ஜி-யால் கணக்கிடப்பட்டு சான்றளிக்கப்படுகிறது, மேலும் அவரது சான்றிதழே இறுதியானது.",
        "tip_en": "Article 279: Calculation of Net Proceeds = Certified by CAG (final and conclusive).",
        "tip_ta": "சரத்து 279: நிகர வருவாயைக் கணக்கிடுதல் = CAG சான்றளிக்கிறார் (இதுவே இறுதியானது).",
        "fact_en": "This certified figure forms the statutory basis for tax devolution by the Finance Commission under Article 280.",
        "fact_ta": "இந்த சான்றளிக்கப்பட்ட தொகையே சரத்து 280-ன் கீழ் நிதி ஆணையம் வரிப் பகிர்வு செய்வதற்கான சட்டப்பூர்வ அடிப்படையாகும்."
    },
    # 17
    {
        "subtopic": "Form of Accounts",
        "stem_en": "Under Article 150 of the Constitution, who advises the President regarding the form in which the accounts of the Union and the States shall be kept?",
        "stem_ta": "அரசியலமைப்பின் சரத்து 150-ன் கீழ், மத்திய மற்றும் மாநிலங்களின் கணக்குகள் எந்தப் படிவத்தில் வைக்கப்பட வேண்டும் என்பது குறித்து குடியரசுத் தலைவருக்கு ஆலோசிப்பவர் யார்?",
        "options": [
            ("The Comptroller and Auditor General of India", "இந்தியத் தலைமைக் கணக்குத் தணிக்கையாளர் (CAG)"),
            ("The Union Minister of Corporate Affairs", "மத்திய கார்ப்பரேட் விவகாரங்கள் அமைச்சர்"),
            ("The Chairman of the Law Commission of India", "இந்திய சட்ட ஆணையத்தின் தலைவர்"),
            ("The Governor of each respective State", "அந்தந்த மாநிலங்களின் ஆளுநர்கள்")
        ],
        "exp_en": "Article 150 provides that the accounts of the Union and the States shall be kept in such form as the President may, on the advice of the Comptroller and Auditor-General of India, prescribe.",
        "exp_ta": "சரத்து 150-ன் படி, இந்தியத் தலைமைக் கணக்குத் தணிக்கையாளரின் ஆலோசனையின் பேரில், குடியரசுத் தலைவர் பரிந்துரைக்கும் படிவத்தில் மத்திய மற்றும் மாநில அரசுகளின் கணக்குகள் வைக்கப்பட வேண்டும்.",
        "tip_en": "Article 150: Form of Accounts = President prescribes on the ADVICE of the CAG.",
        "tip_ta": "சரத்து 150: கணக்குகளின் படிவம் = CAG ஆலோசனையின் பேரில் குடியரசுத் தலைவர் பரிந்துரைக்கிறார்.",
        "fact_en": "This ensures uniform accounting classifications throughout the country.",
        "fact_ta": "இது நாடு முழுவதிலும் ஒரே மாதிரியான கணக்கியல் முறையை உறுதி செய்கிறது."
    },
    # 18
    {
        "subtopic": "British vs Indian CAG Comparison",
        "stem_en": "In what crucial respect does the office of the Indian CAG differ from the Comptroller and Auditor General of the United Kingdom?",
        "stem_ta": "ஐக்கிய இராச்சியத்தின் (UK) தலைமைத் தணிக்கையாளரிடமிருந்து இந்திய CAG எந்த முக்கிய அம்சத்தில் வேறுபடுகிறார்?",
        "options": [
            ("The UK CAG has power to control the issue of money from the exchequer, whereas the Indian CAG audits only after money is spent", "பிரிட்டன் CAG கருவூலத்திலிருந்து பணம் எடுப்பதைக் கட்டுப்படுத்துகிறார், ஆனால் இந்திய CAG பணம் செலவிடப்பட்ட பின்னரே தணிக்கை செய்கிறார்"),
            ("The Indian CAG is appointed by the Prime Minister directly", "இந்திய CAG பிரதமரால் நேரடியாக நியமிக்கப்படுகிறார்"),
            ("The UK CAG has no power to audit military expenditures", "பிரிட்டன் CAG-க்கு ராணுவச் செலவினங்களைத் தணிக்கை செய்ய அதிகாரம் இல்லை"),
            ("The Indian CAG is an elected Member of the Lok Sabha", "இந்திய CAG மக்களவையின் தேர்ந்தெடுக்கப்பட்ட உறுப்பினர் ஆவார்")
        ],
        "exp_en": "In the UK, executive departments cannot withdraw money from the public exchequer without the prior approval of the Comptroller. In India, the CAG has no control over the issue of money; he audits expenditure post-facto.",
        "exp_ta": "பிரிட்டனில் அரசின் கருவூலத்திலிருந்து பணம் எடுப்பதற்கு முன் சி.ஏ.ஜி-யின் அனுமதி கட்டாயம். இந்தியாவில் பணம் எடுப்பதில் சி.ஏ.ஜி-க்கு கட்டுப்பாடில்லை; செலவு செய்யப்பட்ட பிறகே தணிக்கை செய்கிறார்.",
        "tip_en": "Indian CAG is practically an Auditor-General only; UK CAG is both Comptroller (controls issue) and Auditor.",
        "tip_ta": "இந்திய சி.ஏ.ஜி நடைமுறையில் தணிக்கையாளர் மட்டுமே; பிரிட்டன் சி.ஏ.ஜி நிதியைக் கட்டுப்படுத்துபவராகவும் தணிக்கையாளராகவும் உள்ளார்.",
        "fact_en": "The Constitution retained the colonial title 'Comptroller and Auditor General' despite having no comptroller functions over money issuance.",
        "fact_ta": "பணம் எடுப்பதைக் கட்டுப்படுத்தும் அதிகாரம் இல்லாவிட்டாலும் காலனித்துவ காலப் பெயரான 'Comptroller and Auditor General' என்பது தொடர்கிறது."
    },
    # 19
    {
        "subtopic": "Secret Service Expenditure",
        "stem_en": "What is the limitation on the Comptroller and Auditor General regarding the audit of secret service expenditures of the Union?",
        "stem_ta": "மத்திய அரசின் உளவு மற்றும் இரகசியப் பணிச் செலவினங்களைத் (Secret service expenditure) தணிக்கை செய்வதில் சி.ஏ.ஜி-க்கு உள்ள வரம்பு என்ன?",
        "options": [
            ("CAG must accept a certificate of expenditure from the competent administrative authority without demanding vouchers", "ஆவணங்களைக் கோராமல் தகுதிவாய்ந்த நிர்வாக அதிகாரியின் செலவுச் சான்றிதழை CAG ஏற்றுக்கொள்ள வேண்டும்"),
            ("CAG conducts open public broadcast of all secret service vouchers", "அனைத்து இரகசிய செலவு ஆவணங்களையும் CAG பகிரங்கமாக வெளியிடுகிறார்"),
            ("CAG has unlimited power to interrogate secret service intelligence agents", "இரகசிய உளவுத்துறை அதிகாரிகளை விசாரிக்க CAG-க்கு வரம்பற்ற அதிகாரம் உண்டு"),
            ("CAG cannot audit any ministry that handles defense intelligence", "பாதுகாப்பு உளவுத்துறையைக் கையாளும் எந்த அமைச்சகத்தையும் CAG தணிக்கை செய்ய முடியாது")
        ],
        "exp_en": "Regarding secret service expenditure, the CAG cannot call for detailed vouchers; he accepts a certificate issued by the competent administrative authority stating that money has been spent under proper authority.",
        "exp_ta": "இரகசியப் பணிச் செலவுகளில் விரிவான பற்றுச்சீட்டுகளை (vouchers) CAG கோர முடியாது; தகுதிவாய்ந்த அதிகாரியால் பணம் முறையாக செலவிடப்பட்டது என அளிக்கப்படும் சான்றிதழை அவர் ஏற்றுக்கொள்ள வேண்டும்.",
        "tip_en": "Secret service expenditure: Certificate of competent authority is accepted in lieu of vouchers.",
        "tip_ta": "இரகசியப் பணிச் செலவு: ஆவணங்களுக்குப் பதிலாக தகுதிவாய்ந்த அதிகாரியின் சான்றிதழ் ஏற்றுக்கொள்ளப்படுகிறது.",
        "fact_en": "This limitation prevents leakage of sensitive national security operations.",
        "fact_ta": "இந்த வரம்பு நாட்டின் பாதுகாப்பு நடவடிக்கைகள் கசிவதைத் தடுக்கிறது."
    },
    # 20
    {
        "subtopic": "Indian Audit and Accounts Department",
        "stem_en": "Who is the administrative and institutional head of the Indian Audit and Accounts Department (IA&AD)?",
        "stem_ta": "இந்தியத் தணிக்கை மற்றும் கணக்குத் துறையின் (IA&AD) நிர்வாக மற்றும் நிறுவனத் தலைவர் யார்?",
        "options": [
            ("The Comptroller and Auditor General of India", "இந்தியத் தலைமைக் கணக்குத் தணிக்கையாளர் (CAG)"),
            ("The Union Cabinet Secretary", "மத்திய அமைச்சரவைச் செயலாளர்"),
            ("The Union Finance Secretary", "மத்திய நிதிச் செயலாளர்"),
            ("The Director of Enforcement", "அமலாக்கத்துறை இயக்குநர்")
        ],
        "exp_en": "The Comptroller and Auditor General of India is the head of the Indian Audit and Accounts Department (IA&AD), which assists him in executing constitutional and statutory duties.",
        "exp_ta": "இந்தியத் தலைமைக் கணக்குத் தணிக்கையாளர் இந்தியத் தணிக்கை மற்றும் கணக்குத் துறையின் (IA&AD) தலைவராக விளங்கி, தனது அரசியலமைப்பு மற்றும் சட்டப்பூர்வ கடமைகளைச் செயல்படுத்துகிறார்.",
        "tip_en": "IA&AD is one of the oldest specialized civil services in India, functioning under the sole direction of the CAG.",
        "tip_ta": "IA&AD இந்தியாவில் உள்ள மிகப்பழமையான சிறப்பு சிவில் பணிகளில் ஒன்றாகும், இது சி.ஏ.ஜி-யின் கீழ் மட்டுமே செயல்படுகிறது.",
        "fact_en": "Officers of the Indian Audit and Accounts Service (IA&AS) are recruited through the UPSC Civil Services Examination.",
        "fact_ta": "இந்தியத் தணிக்கை மற்றும் கணக்குப் பணி (IA&AS) அதிகாரிகள் யு.பி.எஸ்.சி குடிமைப் பணிகள் தேர்வு மூலம் தேர்ந்தெடுக்கப்படுகின்றனர்."
    },
    # 21
    {
        "subtopic": "Statutory Act of 1971",
        "stem_en": "Under Article 149, which parliamentary statute defines the duties, powers, and conditions of service of the CAG?",
        "stem_ta": "சரத்து 149-ன் கீழ், சி.ஏ.ஜி-யின் கடமைகள், அதிகாரங்கள் மற்றும் பணி நிபந்தனைகளை வரையறுக்கும் நாடாளுமன்றச் சட்டம் எது?",
        "options": [
            ("CAG's (Duties, Powers and Conditions of Service) Act, 1971", "சி.ஏ.ஜி (கடமைகள், அதிகாரங்கள் மற்றும் பணி நிபந்தனைகள்) சட்டம், 1971"),
            ("Public Financial Management Act, 1950", "பொது நிதி மேலாண்மைச் சட்டம், 1950"),
            ("Fiscal Responsibility and Budget Management Act, 2003", "நிதிப் பொறுப்புடைமை மற்றும் வரவு-செலவு மேலாண்மைச் சட்டம், 2003"),
            ("Indian Audit Department Act, 1961", "இந்தியத் தணிக்கைத் துறை சட்டம், 1961")
        ],
        "exp_en": "Article 149 empowered Parliament to prescribe the duties and powers of the CAG. Accordingly, Parliament enacted the CAG's (Duties, Powers and Conditions of Service) Act in 1971.",
        "exp_ta": "சரத்து 149 CAG-ன் அதிகாரங்களையும் கடமைகளையும் பரிந்துரைக்க நாடாளுமன்றத்திற்கு அதிகாரம் அளித்தது. அதன்படி நாடாளுமன்றம் 1971-ல் CAG (DPC) சட்டத்தை இயற்றியது.",
        "tip_en": "Article 148 = Office of CAG; Article 149 = Duties and Powers prescribed by Parliament (Act of 1971).",
        "tip_ta": "சரத்து 148 = CAG அலுவலகம்; சரத்து 149 = நாடாளுமன்றத்தால் நிர்ணயிக்கப்படும் கடமைகள் மற்றும் அதிகாரங்கள் (1971 சட்டம்).",
        "fact_en": "Until 1971, the CAG functioned under the Government of India (Audit and Accounts) Order, 1936.",
        "fact_ta": "1971 வரை சி.ஏ.ஜி 1936-ம் ஆண்டின் இந்திய அரசு (தணிக்கை மற்றும் கணக்குகள்) ஆணையின் கீழேயே பணியாற்றினார்."
    },
    # 22
    {
        "subtopic": "Propriety Audit",
        "stem_en": "What is meant by 'Propriety Audit' conducted by the Comptroller and Auditor General of India?",
        "stem_ta": "இந்தியத் தலைமைக் கணக்குத் தணிக்கையாளரால் நடத்தப்படும் 'முறையுடைமைத் தணிக்கை' (Propriety Audit) என்பது எதனைக் குறிக்கிறது?",
        "options": [
            ("Auditing whether expenditure conforms to wisdom, faithfulness, economy, and checking wastefulness", "செலவினங்கள் அறிவுடைமை, விசுவாசம் மற்றும் சிக்கனத்துடன் உள்ளதா என்பதையும் வீண் விரயங்களைச் சரிபார்ப்பதையும் குறிக்கும்"),
            ("Verifying only the grammatical spelling of vouchers", "பற்றுச்சீட்டுகளின் இலக்கணப் பிழைகளை மட்டும் சரிபார்த்தல்"),
            ("Auditing the private personal income tax of citizens", "குடிமக்களின் தனிப்பட்ட வருமான வரியைத் தணிக்கை செய்தல்"),
            ("Investigating criminal conspiracies of foreign embassies", "வெளிநாட்டுத் தூதரகங்களின் குற்றவியல் சதியை விசாரித்தல்")
        ],
        "exp_en": "Propriety audit goes beyond mere legal regularity; it looks into the wisdom, faithfulness, and economy of government expenditure to check wastefulness and extravagance.",
        "exp_ta": "முறையுடைமைத் தணிக்கை என்பது வெறும் சட்ட ஒழுங்கைத் தாண்டி, அரசின் செலவினங்களில் உள்ள சிக்கனம், விவேகம் மற்றும் வீண் விரயங்களைத் தடுப்பதை ஆராய்கிறது.",
        "tip_en": "Regulatory Audit = Legal compliance (mandatory); Propriety Audit = Wisdom and economy (discretionary).",
        "tip_ta": "ஒழுங்குமுறைத் தணிக்கை = சட்ட இணக்கம் (கட்டாயம்); முறையுடைமைத் தணிக்கை = விவேகம் மற்றும் சிக்கனம் (விருப்பத்திற்குரியது).",
        "fact_en": "Propriety audit allows the CAG to comment on cases of loss or infructuous expenditure even if legally authorized.",
        "fact_ta": "சட்டப்பூர்வமாக அனுமதிக்கப்பட்டிருந்தாலும், வீணான செலவினங்கள் குறித்து கருத்து தெரிவிக்க முறையுடைமைத் தணிக்கை CAG-க்கு அதிகாரம் அளிக்கிறது."
    },
    # 23
    {
        "subtopic": "Audit of Government Companies",
        "stem_en": "How does the Comptroller and Auditor General audit Government Companies under the Companies Act, 2013?",
        "stem_ta": "நிறுவனங்கள் சட்டம் 2013-ன் கீழ் அரசு நிறுவனங்களை சி.ஏ.ஜி எவ்வாறு தணிக்கை செய்கிறார்?",
        "options": [
            ("CAG appoints the statutory auditor and can conduct supplementary or test audits", "CAG சட்டப்பூர்வ தணிக்கையாளரை நியமிக்கிறார் மற்றும் துணை அல்லது மாதிரி தணிக்கைகளை நடத்தலாம்"),
            ("CAG cannot audit any company having government shares", "அரசுப் பங்குகள் உள்ள எந்த நிறுவனத்தையும் CAG தணிக்கை செய்ய முடியாது"),
            ("CAG takes over the board of directors of all government companies", "அனைத்து அரசு நிறுவனங்களின் இயக்குநர் குழுவையும் CAG தனது கட்டுப்பாட்டில் எடுக்கிறார்"),
            ("CAG only verifies the stock market price of shares", "பங்குகளின் பங்குச் சந்தை விலையை மட்டுமே CAG சரிபார்க்கிறார்")
        ],
        "exp_en": "Under Section 139 and 143 of the Companies Act 2013, the CAG appoints the statutory auditor for government companies and has the power to direct supplementary audits or test audits.",
        "exp_ta": "நிறுவனங்கள் சட்டம் 2013-ன் பிரிவுகள் 139 மற்றும் 143-ன் கீழ், அரசு நிறுவனங்களுக்கான தணிக்கையாளரை CAG நியமிக்கிறார், மேலும் துணைத் தணிக்கை அல்லது மாதிரித் தணிக்கை நடத்த அதிகாரம் கொண்டுள்ளார்.",
        "tip_en": "Government Company = Company where >= 51% of paid-up share capital is held by Central/State Government.",
        "tip_ta": "அரசு நிறுவனம் = மத்திய அல்லது மாநில அரசால் 51% அல்லது அதற்கு மேற்பட்ட பங்குகள் வைத்திருக்கப்படும் நிறுவனம்.",
        "fact_en": "Supplementary audit reports are submitted to the company's annual general meeting.",
        "fact_ta": "துணைத் தணிக்கை அறிக்கைகள் நிறுவனத்தின் வருடாந்திர பொதுக் கூட்டத்தில் சமர்ப்பிக்கப்படுகின்றன."
    },
    # 24
    {
        "subtopic": "Audit of Statutory Corporations",
        "stem_en": "Which of the following statutory public corporations is audited COMPLETELY AND DIRECTLY by the Comptroller and Auditor General?",
        "stem_ta": "பின்வரும் எந்த சட்டப்பூர்வ பொதுத்துறை நிறுவனம் சி.ஏ.ஜி-யால் முழுமையாகவும் நேரடியாகவும் தணிக்கை செய்யப்படுகிறது?",
        "options": [
            ("Damodar Valley Corporation (DVC)", "தாமோதர் பள்ளத்தாக்கு கழகம் (DVC)"),
            ("Life Insurance Corporation of India (LIC)", "இந்திய ஆயுள் காப்பீட்டுக் கழகம் (LIC)"),
            ("Reserve Bank of India (RBI)", "இந்திய ரிசர்வ் வங்கி (RBI)"),
            ("State Bank of India (SBI)", "பாரத ஸ்டேட் வங்கி (SBI)")
        ],
        "exp_en": "Damodar Valley Corporation, Oil and Natural Gas Commission (earlier), Air India (earlier) were directly audited by CAG. LIC, RBI, and SBI are audited exclusively by private professional auditors appointed by the Government.",
        "exp_ta": "தாமோதர் பள்ளத்தாக்கு கழகம் (DVC) போன்றவை CAG-யால் நேரடியாகத் தணிக்கை செய்யப்படுகின்றன. ஆனால் LIC, RBI மற்றும் SBI ஆகியவை அரசால் நியமிக்கப்படும் தனியார் தணிக்கையாளர்களால் மட்டுமே தணிக்கை செய்யப்படுகின்றன.",
        "tip_en": "Corporations audited directly by CAG: DVC, ONGC. Corporations audited ONLY by private auditors: RBI, SBI, LIC.",
        "tip_ta": "CAG-யால் நேரடியாகத் தணிக்கை செய்யப்படுபவை: DVC. தனியார் தணிக்கையாளர்களால் மட்டுமே செய்யப்படுபவை: RBI, SBI, LIC.",
        "fact_en": "Audit jurisdiction over statutory corporations depends on the specific enabling Act passed by Parliament.",
        "fact_ta": "சட்டப்பூர்வ நிறுவனங்கள் மீதான தணிக்கை அதிகாரம் நாடாளுமன்றத்தால் இயற்றப்படும் அந்தந்த நிறுவனச் சட்டத்தைப் பொறுத்தது."
    },
    # 25
    {
        "subtopic": "Local Bodies Audit",
        "stem_en": "What is the nature of the CAG's role in the audit of Panchayati Raj Institutions and Urban Local Bodies?",
        "stem_ta": "ஊராட்சி அமைப்புகள் மற்றும் நகர்ப்புற உள்ளாட்சி அமைப்புகளின் தணிக்கையில் சி.ஏ.ஜி-யின் பங்கின் தன்மை என்ன?",
        "options": [
            ("Provides Technical Guidance and Supervision (TGS) to the primary state audit agencies", "முதன்மை மாநில தணிக்கை அமைப்புகளுக்கு தொழில்நுட்ப வழிகாட்டுதல் மற்றும் மேற்பார்வையை (TGS) வழங்குகிறது"),
            ("Directly maintains the daily petty cash of all gram panchayats", "அனைத்து கிராம ஊராட்சிகளின் தினசரி சில்லறை பணக் கணக்கை நேரடியாகப் பராமரிக்கிறது"),
            ("Has no jurisdiction or involvement whatsoever in local bodies", "உள்ளாட்சி அமைப்புகளில் எவ்வித அதிகார வரம்போ அல்லது தொடர்போ இல்லை"),
            ("Can dismiss elected Panchayat Presidents for audit delays", "தணிக்கைத் தாமதத்திற்காக தேர்ந்தெடுக்கப்பட்ட ஊராட்சித் தலைவர்களைப் பதவிநீக்கம் செய்யலாம்")
        ],
        "exp_en": "On the recommendations of the Eleventh Finance Commission, the CAG provides Technical Guidance and Supervision (TGS) to primary state audit agencies for local bodies audit.",
        "exp_ta": "பதினோராவது நிதி ஆணையத்தின் பரிந்துரைகளின்படி, உள்ளாட்சி தணிக்கைகளுக்காக முதன்மை மாநில தணிக்கை முகமைகளுக்கு தொழில்நுட்ப வழிகாட்டுதல் மற்றும் மேற்பார்வையை (TGS) CAG வழங்குகிறார்.",
        "tip_en": "Local bodies primary audit is done by State Local Fund Audit; CAG provides Technical Guidance & Supervision (TGS).",
        "tip_ta": "உள்ளாட்சி தணிக்கையை மாநில உள்ளாட்சி நிதித் தணிக்கை செய்கிறது; CAG தொழில்நுட்ப வழிகாட்டுதலை (TGS) வழங்குகிறார்.",
        "fact_en": "The Eleventh Finance Commission institutionalized this TGS framework to enhance grassroots fiscal transparency.",
        "fact_ta": "11-வது நிதி ஆணையம் அடிமட்ட நிதி வெளிப்படைத்தன்மையை மேம்படுத்த இந்த TGS முறையை முறைப்படுத்தியது."
    },
    # 26
    {
        "subtopic": "Historical Precursor",
        "stem_en": "In which year was the office of Accountant General first established under Lord Canning in British India?",
        "stem_ta": "பிரிட்டிஷ் இந்தியாவில் கானிங் பிரபுவின் கீழ் கணக்குத் துறை பொது அதிகாரி (Accountant General) அலுவலகம் முதன்முதலில் எந்த ஆண்டு நிறுவப்பட்டது?",
        "options": [
            ("1858", "1858"),
            ("1885", "1885"),
            ("1909", "1909"),
            ("1935", "1935")
        ],
        "exp_en": "In 1858, following the transfer of power from the East India Company to the British Crown, Lord Canning established the office of Accountant General.",
        "exp_ta": "1858-ல், கிழக்கிந்திய கம்பெனியிடமிருந்து பிரிட்டிஷ் அரச மகுடத்திற்கு அதிகாரம் மாற்றப்பட்டதைத் தொடர்ந்து, கானிங் பிரபுவால் Accountant General அலுவலகம் நிறுவப்பட்டது.",
        "tip_en": "1858: Office of Accountant General established -> 1860: Sir Edward Drummond appointed first Auditor General.",
        "tip_ta": "1858: அக்கவுண்டன்ட் ஜெனரல் பதவி உருவாக்கம் -> 1860: சர் எட்வர்ட் ட்ரம்மண்ட் முதல் தணிக்கை ஜெனரலாக நியமனம்.",
        "fact_en": "Sir Edward Drummond took charge as the first Auditor General of India in November 1860.",
        "fact_ta": "1860 நவம்பரில் சர் எட்வர்ட் ட்ரம்மண்ட் இந்தியாவின் முதல் தணிக்கை அதிகாரியாகப் பொறுப்பேற்றார்."
    },
    # 27
    {
        "subtopic": "Government of India Act, 1919",
        "stem_en": "Which constitutional reform act first gave statutory recognition and independence to the Auditor General in British India?",
        "stem_ta": "பிரிட்டிஷ் இந்தியாவில் தணிக்கை ஜெனரலுக்கு முதன்முதலில் சட்டப்பூர்வ அங்கீகாரத்தையும் சுதந்திரத்தையும் வழங்கிய அரசியலமைப்புச் சீர்திருத்தச் சட்டம் எது?",
        "options": [
            ("Government of India Act, 1919", "இந்திய அரசுச் சட்டம், 1919"),
            ("Indian Councils Act, 1861", "இந்திய கவுன்சில்கள் சட்டம், 1861"),
            ("Morley-Minto Reforms, 1909", "மார்லே-மிண்டோ சீர்திருத்தங்கள், 1909"),
            ("Charter Act of 1833", "சாசனச் சட்டம் 1833")
        ],
        "exp_en": "The Government of India Act, 1919 freed the Auditor General from the control of the executive government in India, making him statutory and appointed directly by the Secretary of State.",
        "exp_ta": "1919 இந்திய அரசுச் சட்டம் தணிக்கை ஜெனரலை இந்திய நிர்வாகக் கட்டுப்பாட்டிலிருந்து விடுவித்து, இந்திய விவகாரங்களுக்கான அரசுச் செயலாளரால் நியமிக்கப்படும் சட்டப்பூர்வ அதிகாரியாக்கியது.",
        "tip_en": "GOI Act 1919: Established statutory independence of the Auditor General.",
        "tip_ta": "1919 சட்டம்: தணிக்கை ஜெனரலின் சட்டப்பூர்வ சுதந்திரத்தை நிறுவியது.",
        "fact_en": "Under the 1919 Act, the Auditor General submitted reports directly to the Secretary of State for India in Council.",
        "fact_ta": "1919 சட்டத்தின் கீழ் தணிக்கை ஜெனரல் தனது அறிக்கைகளை லண்டனில் உள்ள அரசுச் செயலாளரிடம் சமர்ப்பித்தார்."
    },
    # 28
    {
        "subtopic": "Government of India Act, 1935",
        "stem_en": "Under the Government of India Act, 1935, what designation was given to the chief federal audit authority?",
        "stem_ta": "1935 இந்திய அரசுச் சட்டத்தின் கீழ், கூட்டாட்சி தலைமைத் தணிக்கை அதிகாரியின் பதவிப் பெயர் என்னவாக இருந்தது?",
        "options": [
            ("Auditor-General for the Federation", "கூட்டாட்சிக்கான தணிக்கை ஜெனரல் (Auditor-General for the Federation)"),
            ("Comptroller General of the East India Company", "கிழக்கிந்திய கம்பெனியின் தலைமைப் பதிவாளர்"),
            ("Director General of Finance", "நிதித் தலைமை இயக்குநர்"),
            ("Chief Accountant of India", "இந்தியத் தலைமை கணக்காளர்")
        ],
        "exp_en": "Section 166 of the Government of India Act, 1935 provided for the appointment of an 'Auditor-General for the Federation' appointed by the British King-Emperor.",
        "exp_ta": "1935 இந்திய அரசுச் சட்டத்தின் பிரிவு 166 பிரிட்டிஷ் மன்னரால் நியமிக்கப்படும் 'கூட்டாட்சிக்கான தணிக்கை ஜெனரல்' பதவிக்கு வகை செய்தது.",
        "tip_en": "GOI Act 1935 Section 166 = Auditor-General of the Federation; Section 55 = Provincial Advocate-General.",
        "tip_ta": "1935 சட்டம் பிரிவு 166 = கூட்டாட்சி தணிக்கை ஜெனரல்; பிரிவு 55 = மாகாண அட்வகேட் ஜெனரல்.",
        "fact_en": "The provisions of Section 166 were substantially incorporated into Article 148 in 1950.",
        "fact_ta": "பிரிவு 166-ன் விதிகள் 1950-ல் சரத்து 148-ல் பெருமளவில் இணைக்கப்பட்டன."
    },
    # 29
    {
        "subtopic": "Conditions of Service Protection",
        "stem_en": "Under Article 148(3), what constitutional guarantee is given regarding the salary and rights in respect of leave of absence of the CAG?",
        "stem_ta": "சரத்து 148(3)-ன் கீழ், சி.ஏ.ஜி-யின் ஊதியம் மற்றும் விடுப்பு உரிமைகள் குறித்து என்ன அரசியலமைப்பு உத்தரவாதம் அளிக்கப்பட்டுள்ளது?",
        "options": [
            ("Shall not be varied to his disadvantage after his appointment", "அவரது நியமனத்திற்குப் பிறகு அவருக்கு பாதகமாக மாற்றப்படக்கூடாது"),
            ("Can be reduced at any time by executive notification", "நிர்வாக அறிவிக்கை மூலம் எந்த நேரத்திலும் குறைக்கப்படலாம்"),
            ("Are subject to annual deduction based on inflation", "பணவீக்கத்தின் அடிப்படையில் ஆண்டுதோறும் பிடித்தம் செய்யப்படும்"),
            ("Are determined on a weekly basis by the Cabinet", "அமைச்சரவையால் வாராந்திர அடிப்படையில் தீர்மானிக்கப்படும்")
        ],
        "exp_en": "Article 148(3) states that neither the salary of the CAG nor his rights in respect of leave of absence, pension, or age of retirement shall be varied to his disadvantage after his appointment.",
        "exp_ta": "சரத்து 148(3) சி.ஏ.ஜி-யின் ஊதியமோ அல்லது அவரது விடுப்பு, ஓய்வூதியம் அல்லது ஓய்வு பெறும் வயது தொடர்பான உரிமைகளோ அவரது நியமனத்திற்குப் பிறகு அவருக்கு பாதகமாக மாற்றப்படக்கூடாது எனக் கூறுகிறது.",
        "tip_en": "Non-variation to disadvantage protects judicial and audit independence from political vendetta.",
        "tip_ta": "பாதகமாக மாற்றப்படக்கூடாது என்ற விதி அரசியல் பழிவாங்கல்களிலிருந்து தணிக்கை சுதந்திரத்தைப் பாதுகாக்கிறது.",
        "fact_en": "This protection is identical to that granted to Judges of the Supreme Court under Article 125(2).",
        "fact_ta": "இந்த பாதுகாப்பு சரத்து 125(2)-ன் கீழ் உச்ச நீதிமன்ற நீதிபதிகளுக்கு வழங்கப்பட்டுள்ள அதே போன்றதாகும்."
    },
    # 30
    {
        "subtopic": "Staff and Administrative Powers",
        "stem_en": "Under Article 148(5), who makes the rules governing the administrative powers of the CAG and the conditions of service of staff in the IA&AD?",
        "stem_ta": "சரத்து 148(5)-ன் கீழ், சி.ஏ.ஜி-யின் நிர்வாக அதிகாரங்கள் மற்றும் தணிக்கைத் துறைப் பணியாளர்களின் பணி நிபந்தனைகளுக்கான விதிகளை உருவாக்குபவர் யார்?",
        "options": [
            ("The President, after consultation with the Comptroller and Auditor General", "தலைமைக் கணக்குத் தணிக்கையாளரைக் கலந்தாலோசித்த பிறகு குடியரசுத் தலைவர்"),
            ("The Union Public Service Commission exclusively", "மத்திய அரசுப் பணியாளர் தேர்வாணையம் மட்டுமே பிரத்தியேகமாக"),
            ("The Prime Minister directly by decree", "பிரதமர் தனது நேரடி ஆணை மூலம்"),
            ("The Chief Justice of India", "இந்தியத் தலைமை நீதிபதி")
        ],
        "exp_en": "Under Article 148(5), the administrative powers of the CAG and the conditions of service of persons serving in the IA&AD are prescribed by rules made by the President after consultation with the CAG.",
        "exp_ta": "சரத்து 148(5)-ன் கீழ், CAG-ஐக் கலந்தாலோசித்த பிறகு குடியரசுத் தலைவர் உருவாக்கும் விதிகளின்படி அவரது நிர்வாக அதிகாரங்களும் பணியாளர்களின் பணி நிபந்தனைகளும் பரிந்துரைக்கப்படுகின்றன.",
        "tip_en": "President makes rules AFTER consultation with CAG under Article 148(5).",
        "tip_ta": "சரத்து 148(5)-ன் கீழ் CAG-உடன் கலந்தாலோசித்த பிறகே குடியரசுத் தலைவர் விதிகளை உருவாக்குகிறார்.",
        "fact_en": "Consultation ensures that administrative control over audit staff remains insulated from executive interference.",
        "fact_ta": "இந்த ஆலோசனை தணிக்கைப் பணியாளர்கள் மீதான நிர்வாகக் கட்டுப்பாடு நிர்வாகத் தலையீடின்றி இருப்பதை உறுதி செய்கிறது."
    },
    # 31
    {
        "subtopic": "Appropriation Accounts",
        "stem_en": "What is the primary objective of the Appropriation Accounts prepared by the Government and audited by the CAG?",
        "stem_ta": "அரசாங்கத்தால் தயாரிக்கப்பட்டு சி.ஏ.ஜி-யால் தணிக்கை செய்யப்படும் ஒதுக்கீட்டுக் கணக்குகளின் (Appropriation Accounts) முதன்மை நோக்கம் என்ன?",
        "options": [
            ("To compare the actual expenditure with the grants sanctioned by Parliament under the Appropriation Act", "நாடாளுமன்றத்தால் ஒதுக்கீட்டுச் சட்டத்தின் கீழ் அனுமதிக்கப்பட்ட மானியங்களுடன் உண்மையான செலவினங்களை ஒப்பிடுதல்"),
            ("To calculate the personal income tax of all members of Parliament", "நாடாளுமன்ற உறுப்பினர்களின் தனிப்பட்ட வருமான வரியைக் கணக்கிடுதல்"),
            ("To forecast the national gross domestic product for the next decade", "அடுத்த பத்தாண்டுகளுக்கான தேசிய மொத்த உள்நாட்டு உற்பத்தியைக் கணித்தல்"),
            ("To print new currency notes for commercial banks", "வணிக வங்கிகளுக்கு புதிய ரூபாய் நோட்டுகளை அச்சிடுதல்")
        ],
        "exp_en": "Appropriation Accounts compare the expenditure sanctioned by Parliament in the Appropriation Act with the actual expenditure incurred, highlighting savings, excesses, or unauthorized re-appropriations.",
        "exp_ta": "ஒதுக்கீட்டுக் கணக்குகள் நாடாளுமன்றத்தால் அனுமதிக்கப்பட்ட தொகையையும் உண்மையான செலவுகளையும் ஒப்பிட்டு, மிச்சம் அல்லது அதிகப்படியான செலவினங்களை வெளிச்சமிட்டுக் காட்டுகின்றன.",
        "tip_en": "Appropriation Accounts = Actual expenditure vs Parliament grants. Finance Accounts = Annual receipts and disbursements.",
        "tip_ta": "ஒதுக்கீட்டுக் கணக்குகள் = உண்மையான செலவு vs நாடாளுமன்ற மானியங்கள். நிதிக் கணக்குகள் = வரவு மற்றும் செலவுகளின் முழு விவரம்.",
        "fact_en": "If actual expenditure exceeds approved grants, the Public Accounts Committee must examine the excess before regularisation.",
        "fact_ta": "அனுமதிக்கப்பட்ட மானியத்தை விட கூடுதல் செலவு ஏற்பட்டால், அதை முறைப்படுத்துவதற்கு முன் PAC ஆராய வேண்டும்."
    },
    # 32
    {
        "subtopic": "Finance Accounts",
        "stem_en": "What do the Finance Accounts audited by the Comptroller and Auditor General represent?",
        "stem_ta": "தலைமைக் கணக்குத் தணிக்கையாளரால் தணிக்கை செய்யப்படும் நிதிக் கணக்குகள் (Finance Accounts) எதனைப் பிரதிபலிக்கின்றன?",
        "options": [
            ("The annual receipts and disbursements of the Government under Consolidated, Contingency, and Public Accounts", "திரட்டப்பட்ட நிதி, அவசரகால நிதி மற்றும் பொதுக் கணக்குகளின் கீழான அரசாங்கத்தின் வருடாந்திர வரவு மற்றும் செலவுகள்"),
            ("The balance sheets of all private corporate banks in India", "இந்தியாவில் உள்ள அனைத்து தனியார் கார்ப்பரேட் வங்கிகளின் இருப்புநிலைக் குறிப்புகள்"),
            ("The personal assets declared by election candidates", "தேர்தல் வேட்பாளர்கள் அறிவித்த தனிப்பட்ட சொத்துக்கள்"),
            ("The internal military defense strategies of the Armed Forces", "முப்படைகளின் உள்நாட்டு ராணுவப் பாதுகாப்பு உத்திகள்")
        ],
        "exp_en": "Finance Accounts present the comprehensive annual financial accounts of the government, detailing all tax and non-tax revenues, capital receipts, expenditures, debt liabilities, and loans.",
        "exp_ta": "நிதிக் கணக்குகள் அரசாங்கத்தின் விரிவான வருடாந்திர நிதிக் கணக்குகளைக் காட்டுகின்றன; வரி, வரியல்லா வருவாய்கள், மூலதன வரவுகள், செலவுகள் மற்றும் கடன்களை விளக்குகின்றன.",
        "tip_en": "Appropriation Accounts deal with expenditure against budget votes; Finance Accounts show the complete financial picture.",
        "tip_ta": "ஒதுக்கீட்டுக் கணக்குகள் பட்ஜெட் ஒதுக்கீட்டுக்கு எதிரான செலவைக் காட்டுகின்றன; நிதிக் கணக்குகள் முழுமையான நிதி நிலவரத்தைக் காட்டுகின்றன.",
        "fact_en": "Both accounts are compiled annually and presented to the legislature under Article 151.",
        "fact_ta": "இரு கணக்குகளும் ஆண்டுதோறும் தொகுக்கப்பட்டு சரத்து 151-ன் கீழ் சட்டமன்றத்தில் வைக்கப்படுகின்றன."
    },
    # 33
    {
        "subtopic": "Performance Audit",
        "stem_en": "What is the core focus of a 'Performance Audit' (also known as Efficiency-cum-Economy audit) conducted by the CAG?",
        "stem_ta": "சி.ஏ.ஜி-யால் நடத்தப்படும் 'செயல்திறன் தணிக்கையின்' (Performance Audit) முக்கியக் கவனம் என்ன?",
        "options": [
            ("Evaluating the 3 Es: Economy, Efficiency, and Effectiveness of government programs and schemes", "அரசுத் திட்டங்களின் 3 E-க்கள்: சிக்கனம் (Economy), செயல்திறன் (Efficiency) மற்றும் பலன் தருதல் (Effectiveness) ஆகியவற்றை மதிப்பீடு செய்தல்"),
            ("Checking only whether vouchers are stamped with red ink", "பற்றுச்சீட்டுகள் சிவப்பு மையினால் முத்திரையிடப்பட்டுள்ளதா என்பதை மட்டும் சோதித்தல்"),
            ("Calculating the daily travel distance of government vehicles", "அரசு வாகனங்களின் தினசரி பயண தூரத்தைக் கணக்கிடுதல்"),
            ("Testing the physical fitness of civil servants", "அரசு ஊழியர்களின் உடற்தகுதியைச் சோதித்தல்")
        ],
        "exp_en": "Performance audit assesses whether government programs, activities, or organizations are executing their functions in accordance with the principles of Economy, Efficiency, and Effectiveness (the 3 Es).",
        "exp_ta": "செயல்திறன் தணிக்கை என்பது அரசுத் திட்டங்கள் சிக்கனம், செயல்திறன் மற்றும் பலன்தரும் தன்மை (3 Es) ஆகிய கொள்கைகளின்படி செயல்படுத்தப்படுகிறதா என்பதை மதிப்பீடு செய்கிறது.",
        "tip_en": "Performance Audit = 3 Es: Economy (cost minimization), Efficiency (output vs input), Effectiveness (goal achievement).",
        "tip_ta": "செயல்திறன் தணிக்கை = 3 E-க்கள்: சிக்கனம் (Economy), செயல்திறன் (Efficiency), பலன் தருதல் (Effectiveness).",
        "fact_en": "Performance audits of spectrum allocation (2G) and coal block allocations generated massive public debates in India.",
        "fact_ta": "2G அலைக்கற்றை ஒதுக்கீடு மற்றும் நிலக்கரி சுரங்க ஒதுக்கீடு மீதான செயல்திறன் தணிக்கைகள் இந்தியாவில் பெரும் பொது விவாதங்களை உருவாக்கின."
    },
    # 34
    {
        "subtopic": "Audit of Autonomous Bodies",
        "stem_en": "Under Section 14 of the CAG's (DPC) Act 1971, when does an autonomous body become subject to mandatory audit by the CAG?",
        "stem_ta": "CAG சட்டத்தின் (1971) பிரிவு 14-ன் கீழ், ஒரு தன்னாட்சி அமைப்பு எப்போது சி.ஏ.ஜி-யின் கட்டாயத் தணிக்கைக்கு உட்பட்டதாகிறது?",
        "options": [
            ("When government grants or loans constitute not less than Rs. 25 lakh and not less than 75% of its total expenditure in a year", "அரசு மானியங்கள் அல்லது கடன்கள் ரூ. 25 லட்சத்திற்குக் குறையாமலும் அதன் மொத்த செலவில் 75%-க்கு குறையாமலும் இருக்கும் போது"),
            ("Only if the body is located in New Delhi", "அந்த அமைப்பு புதுதில்லியில் அமைந்திருந்தால் மட்டுமே"),
            ("Only if the body employs more than 10,000 workers", "அந்த அமைப்பு 10,000-க்கும் மேற்பட்ட தொழிலாளர்களைப் பணியமர்த்தினால் மட்டுமே"),
            ("If the Prime Minister is an ex-officio patron of the body", "பிரதமர் அந்த அமைப்பின் புரவலராக இருந்தால் மட்டுமே")
        ],
        "exp_en": "Under Section 14, where any body or authority is substantially financed by grants or loans from the Consolidated Fund (not less than Rs. 25 lakh and >= 75% of total expenditure), the CAG mandatorily audits it.",
        "exp_ta": "பிரிவு 14-ன் கீழ், திரட்டப்பட்ட நிதியிலிருந்து கணிசமான நிதி உதவி (ரூ. 25 லட்சத்திற்கு குறையாமல் மற்றும் மொத்த செலவில் 75% அல்லது அதற்கு மேல்) பெறும் அமைப்புகளை CAG கட்டாயமாகத் தணிக்கை செய்கிறார்.",
        "tip_en": "Section 14 CAG Act = Substantially financed bodies (Rs. 25 lakh and 75% threshold).",
        "tip_ta": "CAG சட்டம் பிரிவு 14 = அரசின் கணிசமான நிதி பெறும் அமைப்புகள் (ரூ. 25 லட்சம் மற்றும் 75% வரம்பு).",
        "fact_en": "Universities, research councils, and registered societies receiving large state grants fall under Section 14.",
        "fact_ta": "அரசு மானியம் பெறும் பல்கலைக்கழகங்கள், ஆராய்ச்சி கவுன்சில்கள் ஆகியவை பிரிவு 14-ன் கீழ் வருகின்றன."
    },
    # 35
    {
        "subtopic": "Right to Inspect Records",
        "stem_en": "Under Section 18 of the CAG's (DPC) Act, 1971, what power does the CAG possess regarding government offices and records?",
        "stem_ta": "1971-ம் ஆண்டின் CAG சட்டத்தின் பிரிவு 18-ன் கீழ், அரசு அலுவலகங்கள் மற்றும் ஆவணங்கள் தொடர்பாக சி.ஏ.ஜி-க்கு உள்ள அதிகாரம் என்ன?",
        "options": [
            ("Authority to inspect any office, call for books of accounts, vouchers, and put questions to responsible officers", "எந்தவொரு அலுவலகத்தையும் ஆய்வு செய்யவும், கணக்குப் புத்தகங்கள், பற்றுச்சீட்டுகளைக் கோரவும், அதிகாரிகளிடம் கேள்வி கேட்கவும் அதிகாரம்"),
            ("Power to arrest and imprison accounting staff immediately", "கணக்குப் பணியாளர்களை உடனடியாகக் கைது செய்து சிறையில் அடைக்கும் அதிகாரம்"),
            ("Power to physically demolish government buildings failing audit", "தணிக்கையில் தோல்வியடையும் அரசு கட்டிடங்களை இடிக்கும் அதிகாரம்"),
            ("Authority to declare financial emergency under Article 360", "சரத்து 360-ன் கீழ் நிதி அவசரநிலையைப் பிரகடனம் செய்யும் அதிகாரம்")
        ],
        "exp_en": "Section 18 empowers the CAG to inspect any office under the control of the Union or States, require the production of books, papers, and other documents, and ask questions to obtain required information.",
        "exp_ta": "பிரிவு 18 மத்திய அல்லது மாநில அரசுகளின் கீழ் உள்ள எந்தவொரு அலுவலகத்தையும் ஆய்வு செய்யவும், ஆவணங்களைப் பெறவும், தகவல்களைப் பெற அதிகாரிகளிடம் கேள்விகள் கேட்கவும் CAG-க்கு அதிகாரம் அளிக்கிறது.",
        "tip_en": "Section 18 gives the CAG statutory access to all books of accounts and records.",
        "tip_ta": "பிரிவு 18 அனைத்து கணக்குப் புத்தகங்களையும் ஆவணங்களையும் அணுகும் சட்டப்பூர்வ உரிமையை CAG-க்கு வழங்குகிறது.",
        "fact_en": "Executive departments cannot refuse production of files to the CAG, subject to constitutional privileges.",
        "fact_ta": "அரசியலமைப்புச் சலுகைகளுக்கு உட்பட்டு, கோப்புகளை சி.ஏ.ஜி-க்கு அளிக்க அரசுத் துறைகள் மறுக்க முடியாது."
    },
    # 36
    {
        "subtopic": "Vinod Rai Era",
        "stem_en": "Who served as the Comptroller and Auditor General during the exposure of the 2G Spectrum and Coal Block allocation audits?",
        "stem_ta": "2G அலைக்கற்றை மற்றும் நிலக்கரி சுரங்க ஒதுக்கீடு தணிக்கைகளின் போது இந்தியாவின் தலைமைக் கணக்குத் தணிக்கையாளராகப் பணியாற்றியவர் யார்?",
        "options": [
            ("Vinod Rai", "வினோத் ராய்"),
            ("T.N. Chaturvedi", "டி.என். சதுர்வேதி"),
            ("C.G. Somiah", "சி.ஜி. சோமையா"),
            ("V.K. Shunglu", "வி.கே. சுங்லு")
        ],
        "exp_en": "Vinod Rai served as the 11th CAG of India from 2008 to 2013, during which landmark performance audit reports on 2G Spectrum, Coal Blocks, and Commonwealth Games were tabled.",
        "exp_ta": "வினோத் ராய் 2008 முதல் 2013 வரை இந்தியாவின் 11-வது CAG ஆகப் பணியாற்றினார்; இக்காலகட்டத்தில் 2G அலைக்கற்றை, நிலக்கரிச் சுரங்கங்கள் மற்றும் காமன்வெல்த் போட்டிகள் மீதான வரலாற்று சிறப்புமிக்க தணிக்கை அறிக்கைகள் தாக்கல் செய்யப்பட்டன.",
        "tip_en": "Vinod Rai (2008-2013): Known for activist auditing bringing presumptive loss concepts into public discourse.",
        "tip_ta": "வினோத் ராய் (2008-2013): ஊக இழப்பு (presumptive loss) கருத்துக்களை பொது விவாதத்திற்குக் கொண்டுவந்தவர்.",
        "fact_en": "He authored the book 'Not Just an Accountant' detailing his experiences as CAG.",
        "fact_ta": "அவர் தனது சி.ஏ.ஜி அனுபவங்களை 'Not Just an Accountant' என்ற நூலில் பதிவு செய்தார்."
    },
    # 37
    {
        "subtopic": "Bofors Audit",
        "stem_en": "Which Comptroller and Auditor General authored the 1989 audit report on the Bofors Howitzer gun deal that created widespread political reverberations?",
        "stem_ta": "பெரும் அரசியல் அதிர்வுகளை ஏற்படுத்திய 1989 போஃபோர்ஸ் பீரங்கி ஒப்பந்தம் மீதான தணிக்கை அறிக்கையை வெளியிட்ட தலைமைக் கணக்குத் தணிக்கையாளர் யார்?",
        "options": [
            ("T.N. Chaturvedi", "டி.என். சதுர்வேதி"),
            ("Gian Prakash", "கியான் பிரகாஷ்"),
            ("A. Bakshi", "ஏ. பக்ஷி"),
            ("S. Ranganathan", "எஸ். ரங்கநாதன்")
        ],
        "exp_en": "T.N. Chaturvedi was the CAG of India who presented the 1989 audit report highlighting procedural lapses and financial irregularities in the Bofors gun purchase.",
        "exp_ta": "போஃபோர்ஸ் பீரங்கி வாங்கியதில் நடைமுறை முறைகேடுகளையும் நிதி விதிமீறல்களையும் சுட்டிக்காட்டிய 1989 தணிக்கை அறிக்கையை வெளியிட்ட சி.ஏ.ஜி டி.என். சதுர்வேதி ஆவார்.",
        "tip_en": "T.N. Chaturvedi: 1989 Bofors audit report; later served as Governor of Karnataka.",
        "tip_ta": "டி.என். சதுர்வேதி: 1989 போஃபோர்ஸ் தணிக்கை அறிக்கை; பின்னர் கர்நாடக ஆளுநராகப் பணியாற்றினார்.",
        "fact_en": "The Bofors audit established the power of CAG reports to impact national electoral politics.",
        "fact_ta": "தேசிய தேர்தல் அரசியலில் தாக்கத்தை ஏற்படுத்தும் சி.ஏ.ஜி அறிக்கைகளின் ஆற்றலை போஃபோர்ஸ் தணிக்கை நிரூபித்தது."
    },
    # 38
    {
        "subtopic": "G.C. Murmu Tenure",
        "stem_en": "Who served as the 14th Comptroller and Auditor General of India from August 2020 to November 2024, previously having been the first Lieutenant Governor of Jammu and Kashmir?",
        "stem_ta": "ஜம்மு காஷ்மீரின் முதல் துணை நிலை ஆளுநராக இருந்து, பின்னர் ஆகஸ்ட் 2020 முதல் நவம்பர் 2024 வரை இந்தியாவின் 14-வது தலைமைக் கணக்குத் தணிக்கையாளராகப் பணியாற்றியவர் யார்?",
        "options": [
            ("G.C. Murmu", "ஜி.சி. முர்மு"),
            ("Rajiv Mehrishi", "ராஜீவ் மெஹ்ரிஷி"),
            ("Shashi Kant Sharma", "சசி காந்த் சர்மா"),
            ("K. Sanjay Murthy", "கே. சஞ்சய் மூர்த்தி")
        ],
        "exp_en": "Girish Chandra Murmu served as the 14th CAG of India from 8 August 2020 to 20 November 2024. He was previously the first Lieutenant Governor of the UT of Jammu and Kashmir.",
        "exp_ta": "கிரிஷ் சந்திர முர்மு 2020 ஆகஸ்ட் 8 முதல் 2024 நவம்பர் 20 வரை இந்தியாவின் 14-வது CAG ஆகப் பணியாற்றினார். முன்னதாக இவர் ஜம்மு காஷ்மீர் ஒன்றியப் பிரதேசத்தின் முதல் துணை நிலை ஆளுநராக இருந்தார்.",
        "tip_en": "G.C. Murmu was succeeded by K. Sanjay Murthy in November 2024.",
        "tip_ta": "2024 நவம்பரில் ஜி.சி. முர்முவைத் தொடர்ந்து கே. சஞ்சய் மூர்த்தி சி.ஏ.ஜி-யாகப் பொறுப்பேற்றார்.",
        "fact_en": "G.C. Murmu was also elected as the Chair of the UN Panel of External Auditors.",
        "fact_ta": "ஜி.சி. முர்மு ஐ.நா. வெளித் தணிக்கையாளர்கள் குழுவின் தலைவராகவும் தேர்ந்தெடுக்கப்பட்டார்."
    },
    # 39
    {
        "subtopic": "Current CAG",
        "stem_en": "Who was appointed as the Comptroller and Auditor General of India in November 2024?",
        "stem_ta": "நவம்பர் 2024-ல் இந்தியாவின் தலைமைக் கணக்குத் தணிக்கையாளராக (CAG) நியமிக்கப்பட்டவர் யார்?",
        "options": [
            ("K. Sanjay Murthy", "கே. சஞ்சய் மூர்த்தி"),
            ("G.C. Murmu", "ஜி.சி. முர்மு"),
            ("Rajiv Mehrishi", "ராஜீவ் மெஹ்ரிஷி"),
            ("Vinod Rai", "வினோத் ராய்")
        ],
        "exp_en": "K. Sanjay Murthy, a 1989-batch IAS officer who served as Secretary, Higher Education, was appointed as the Comptroller and Auditor General of India in November 2024.",
        "exp_ta": "உயர்கல்வித் துறைச் செயலாளராகப் பணியாற்றிய 1989-ம் ஆண்டு பேட்ச் ஐ.ஏ.எஸ் அதிகாரி கே. சஞ்சய் மூர்த்தி 2024 நவம்பரில் இந்தியத் தலைமைக் கணக்குத் தணிக்கையாளராக நியமிக்கப்பட்டார்.",
        "tip_en": "Current CAG (from Nov 2024): K. Sanjay Murthy.",
        "tip_ta": "தற்போதைய சி.ஏ.ஜி (நவம்பர் 2024 முதல்): கே. சஞ்சய் மூர்த்தி.",
        "fact_en": "He took the oath administered by President Droupadi Murmu at Rashtrapati Bhavan.",
        "fact_ta": "குடியரசுத் தலைவர் மாளிகையில் குடியரசுத் தலைவர் திரௌபதி முர்மு முன்னிலையில் இவர் பதவிப் பிரமாணம் செய்தார்."
    },
    # 40
    {
        "subtopic": "Auditing of Contingency Fund",
        "stem_en": "Under Article 149 and the 1971 Act, which funds of the Union and States are subject to mandatory audit by the CAG?",
        "stem_ta": "சரத்து 149 மற்றும் 1971 சட்டத்தின் கீழ், மத்திய மற்றும் மாநிலங்களின் எந்த நிதிகள் சி.ஏ.ஜி-யின் கட்டாயத் தணிக்கைக்கு உட்பட்டவை?",
        "options": [
            ("Consolidated Fund, Contingency Fund, and Public Account of both Union and States", "மத்திய மற்றும் மாநிலங்களின் திரட்டப்பட்ட நிதி, அவசரகால நிதி மற்றும் பொதுக் கணக்கு"),
            ("Only the Consolidated Fund of India exclusively", "இந்தியத் திரட்டப்பட்ட நிதி மட்டுமே பிரத்தியேகமாக"),
            ("Only the Contingency Fund of the Union", "மத்திய அரசின் அவசரகால நிதி மட்டுமே"),
            ("Only the private accounts of public sector banks", "பொதுத்துறை வங்கிகளின் தனியார் கணக்குகள் மட்டுமே")
        ],
        "exp_en": "Under Section 13 of the CAG's (DPC) Act 1971, the CAG audits all expenditure from the Consolidated Fund of the Union, each State, and UTs having an assembly, as well as all transactions relating to the Contingency Funds and Public Accounts.",
        "exp_ta": "1971 சட்டத்தின் பிரிவு 13-ன் படி, மத்திய, மாநில மற்றும் சட்டமன்றம் கொண்ட யூனியன் பிரதேசங்களின் திரட்டப்பட்ட நிதி, அவசரகால நிதி மற்றும் பொதுக் கணக்கின் அனைத்துப் பணப்பரிவர்த்தனைகளையும் CAG தணிக்கை செய்கிறார்.",
        "tip_en": "All 3 constitutional funds (Consolidated, Contingency, Public Account) at both Union and State levels are audited by CAG.",
        "tip_ta": "மத்திய மற்றும் மாநில அளவிலான 3 அரசியலமைப்பு நிதிகளுமே (திரட்டப்பட்ட, அவசரகால, பொதுக் கணக்கு) சி.ஏ.ஜி-யால் தணிக்கை செய்யப்படுகின்றன.",
        "fact_en": "This universal jurisdiction establishes an integrated audit system for Indian federalism.",
        "fact_ta": "இந்த விரிவான அதிகார வரம்பு இந்தியக் கூட்டாட்சிக்கு ஒரு ஒருங்கிணைந்த தணிக்கை அமைப்பை நிறுவுகிறது."
    },
    # 41
    {
        "subtopic": "Audit of Receipts",
        "stem_en": "Under Section 16 of the CAG's (DPC) Act 1971, what is the CAG's mandate regarding the revenues and receipts of the Union and States?",
        "stem_ta": "1971-ம் ஆண்டின் CAG சட்டத்தின் பிரிவு 16-ன் கீழ், மத்திய மற்றும் மாநிலங்களின் வருவாய்கள் மற்றும் வரவுகள் மீதான சி.ஏ.ஜி-யின் ஆணை என்ன?",
        "options": [
            ("Auditing all revenues and receipts to ensure rules and procedures are designed to secure effective assessment and collection", "மதிப்பீடு மற்றும் வசூலைச் சரியாகப் பாதுகாக்க விதிகள் வடிவமைக்கப்பட்டுள்ளதா என்பதை உறுதி செய்ய அனைத்து வருவாய்களையும் வரவுகளையும் தணிக்கை செய்தல்"),
            ("Directly fixing income tax rates for individual citizens", "தனிநபர் குடிமக்களுக்கான வருமான வரி விகிதங்களை நேரடியாக நிர்ணயித்தல்"),
            ("Seizing cash from defaulting corporate taxpayers", "வரி செலுத்தாத கார்ப்பரேட் நிறுவனங்களிடமிருந்து ரொக்கத்தைப் பறிமுதல் செய்தல்"),
            ("Cancelling GST registrations of private retail shops", "தனியார் சில்லறை கடைகளின் ஜிஎஸ்டி பதிவுகளை ரத்து செய்தல்")
        ],
        "exp_en": "Section 16 requires the CAG to audit all receipts payable into the Consolidated Fund of the Union and of each State, satisfying himself that the rules and procedures adequately check leakage and secure proper collection.",
        "exp_ta": "பிரிவு 16 திரட்டப்பட்ட நிதியில் செலுத்த வேண்டிய அனைத்து வருவாய் வரவுகளையும் தணிக்கை செய்து, வரி ஏய்ப்பைத் தடுக்கவும் சரியான வசூலை உறுதிப்படுத்தவும் விதிகள் சரியாக உள்ளதா என்பதை சி.ஏ.ஜி உறுதி செய்ய வேண்டும் எனக் கூறுகிறது.",
        "tip_en": "CAG audits both EXPENDITURE (Sec 13) and RECEIPTS/REVENUES (Sec 16).",
        "tip_ta": "CAG செலவினங்கள் (பிரிவு 13) மற்றும் வருவாய் வரவுகள் (பிரிவு 16) இரண்டையுமே தணிக்கை செய்கிறார்.",
        "fact_en": "Receipt audit covers direct taxes (income tax, corporate tax) and indirect taxes (customs, central excise, GST).",
        "fact_ta": "வரவுத் தணிக்கை நேர்முக வரிகள் (வருமான வரி) மற்றும் மறைமுக வரிகள் (ஜிஎஸ்டி, சுங்கம்) இரண்டையும் உள்ளடக்கியது."
    },
    # 42
    {
        "subtopic": "Audit of Stores and Stock",
        "stem_en": "Under Section 17 of the CAG's (DPC) Act 1971, the CAG has the statutory power to audit which of the following?",
        "stem_ta": "1971-ம் ஆண்டின் CAG சட்டத்தின் பிரிவு 17-ன் கீழ், பின்வருவனவற்றில் எதனைத் தணிக்கை செய்ய சி.ஏ.ஜி-க்கு சட்டப்பூர்வ அதிகாரம் உண்டு?",
        "options": [
            ("Stores and stock kept in any office or department of the Union or of a State", "மத்திய அல்லது மாநில அரசின் எந்தவொரு அலுவலகம் அல்லது துறையில் வைக்கப்பட்டுள்ள சரக்குகள் மற்றும் கையிருப்பு (Stores and Stock)"),
            ("Personal jewellery of government servants", "அரசு ஊழியர்களின் தனிப்பட்ட நகைகள்"),
            ("Stock exchanges and privately held mutual fund warehouses", "பங்குச் சந்தைகள் மற்றும் தனியார் பரஸ்பர நிதி சேமிப்புக் கிடங்குகள்"),
            ("Privately owned retail shopping malls", "தனியாருக்குச் சொந்தமான சில்லறை வணிக வளாகங்கள்")
        ],
        "exp_en": "Section 17 provides that the CAG shall have authority to audit and report on the accounts of stores and stock kept in any office or department of the Union or of a State.",
        "exp_ta": "பிரிவு 17 மத்திய அல்லது மாநில அரசுகளின் அலுவலகங்களில் உள்ள சரக்குகள் மற்றும் இருப்புக்களின் கணக்குகளைத் தணிக்கை செய்து அறிக்கை அளிக்க CAG-க்கு அதிகாரம் அளிக்கிறது.",
        "tip_en": "Section 17 covers physical inventory, stores, and stock audits (e.g. military ordnance, food grains in FCI).",
        "tip_ta": "பிரிவு 17 சேமிப்புக் கிடங்கு, சரக்குகள் மற்றும் இருப்புத் தணிக்கைகளை உள்ளடக்கியது (எ.கா. ராணுவ தளவாடங்கள், FCI உணவு தானியங்கள்).",
        "fact_en": "Store audit verifies whether balances of stock are correctly accounted for and physical verification rules followed.",
        "fact_ta": "சரக்குத் தணிக்கை இருப்புக்கள் சரியாக கணக்கில் காட்டப்பட்டுள்ளதா மற்றும் ஆய்வுகள் முறையாக நடக்கிறதா என்பதைச் சரிபார்க்கிறது."
    },
    # 43
    {
        "subtopic": "Auditing Grants and Loans",
        "stem_en": "Under Section 15 of the CAG's (DPC) Act 1971, what is the CAG empowered to verify regarding grants and loans given to authorities or bodies?",
        "stem_ta": "1971 சட்டத்தின் பிரிவு 15-ன் கீழ், அமைப்புகளுக்கு வழங்கப்படும் மானியங்கள் மற்றும் கடன்கள் குறித்து சி.ஏ.ஜி எதனைச் சரிபார்க்க அதிகாரம் பெற்றுள்ளார்?",
        "options": [
            ("Verifying whether the conditions governing the grant or loan are fulfilled and the money applied for the specific purpose", "மானியம் அல்லது கடன் வழங்கப்பட்ட நிபந்தனைகள் பூர்த்தி செய்யப்பட்டுள்ளனவா என்பதையும் குறிப்பிட்ட நோக்கத்திற்காகப் பயன்படுத்தப்பட்டதா என்பதையும் சரிபார்த்தல்"),
            ("Cancelling the charter of the recipient authority unilaterally", "நிதி பெற்ற அமைப்பின் சாசனத்தை தன்னிச்சையாக ரத்து செய்தல்"),
            ("Directing the recipient authority to invest in foreign shares", "நிதி பெற்ற அமைப்பை வெளிநாட்டுப் பங்குகளில் முதலீடு செய்ய உத்தரவிடுதல்"),
            ("Demanding the immediate physical repayment of all grants as cash", "அனைத்து மானியங்களையும் உடனடியாக ரொக்கமாகத் திருப்பித் தருமாறு கோருதல்")
        ],
        "exp_en": "Section 15 empowers the CAG to scrutinize the procedures by which the sanctioning authority satisfies itself as to the fulfillment of conditions on which grants or loans were given for specific purposes.",
        "exp_ta": "பிரிவு 15 குறிப்பிட்ட நோக்கங்களுக்காக வழங்கப்பட்ட மானியங்கள் அல்லது கடன்களின் நிபந்தனைகள் முறையாகப் பூர்த்தி செய்யப்பட்டுள்ளனவா என்பதைச் சரிபார்க்கும் நடைமுறைகளை ஆய்வு செய்ய CAG-க்கு அதிகாரம் அளிக்கிறது.",
        "tip_en": "Section 15 = Audit of grants/loans to ensure purpose fulfillment and utilization certificates.",
        "tip_ta": "பிரிவு 15 = நோக்கப் பயன்பாடு மற்றும் பயன்பாட்டுச் சான்றிதழ்களை உறுதி செய்யும் மானியங்கள்/கடன்கள் தணிக்கை.",
        "fact_en": "This power extends even to non-government bodies that receive conditional public grants.",
        "fact_ta": "நிபந்தனைக்குட்பட்ட அரசு மானியங்களைப் பெறும் அரசு சாரா அமைப்புகளுக்கும் இந்த அதிகாரம் பொருந்தும்."
    },
    # 44
    {
        "subtopic": "CAG and Federal Character",
        "stem_en": "Why is the Comptroller and Auditor General of India considered a single integrated authority in India's federal system?",
        "stem_ta": "இந்தியாவின் கூட்டாட்சி அமைப்பில் தலைமைக் கணக்குத் தணிக்கையாளர் ஏன் ஒற்றை ஒருங்கிணைந்த அதிகார அமைப்பாகக் கருதப்படுகிறார்?",
        "options": [
            ("Because the CAG audits the accounts of both the Central Government and all State Governments", "ஏனெனில் CAG மத்திய அரசு மற்றும் அனைத்து மாநில அரசுகள் ஆகிய இரண்டின் கணக்குகளையுமே தணிக்கை செய்கிறார்"),
            ("Because each State has an independent constitutional State CAG", "ஏனெனில் ஒவ்வொரு மாநிலத்திற்கும் தனித்தனி அரசியலமைப்பு மாநில CAG உள்ளது"),
            ("Because the CAG is elected jointly by all 28 State Governors", "ஏனெனில் 28 மாநில ஆளுநர்களால் CAG கூட்டாகத் தேர்ந்தெடுக்கப்படுகிறார்"),
            ("Because the CAG only audits the Union Government and never touches State accounts", "ஏனெனில் CAG மத்திய அரசை மட்டுமே தணிக்கை செய்கிறார், மாநில கணக்குகளைத் தொடுவதில்லை")
        ],
        "exp_en": "India has a single unified audit machinery. Unlike the USA where federal and state audits are entirely separate, the Indian CAG audits both the Union and the States.",
        "exp_ta": "இந்தியா ஒற்றை ஒருங்கிணைந்த தணிக்கை அமைப்பைக் கொண்டுள்ளது. மத்திய மற்றும் மாகாண தணிக்கைகள் தனித்தனியாக உள்ள அமெரிக்கா போலன்றி, இந்திய CAG மத்திய மற்றும் மாநிலங்கள் இரண்டையுமே தணிக்கை செய்கிறார்.",
        "tip_en": "Unified judiciary and unified audit (CAG) are two key unitary features of the Indian federal constitution.",
        "tip_ta": "ஒருங்கிணைந்த நீதித்துறை மற்றும் ஒருங்கிணைந்த தணிக்கை (CAG) ஆகியவை இந்திய அரசியலமைப்பின் இரு முக்கிய ஒற்றையாட்சி அம்சங்களாகும்.",
        "fact_en": "There is no post of 'State Auditor General' under the Constitution; State Accountants General work under the CAG.",
        "fact_ta": "அரசியலமைப்பில் 'மாநில தணிக்கை ஜெனரல்' என்ற பதவி இல்லை; மாநில முதன்மைக் கணக்காயர்கள் (AG) இந்திய CAG-ன் கீழேயே பணியாற்றுகின்றனர்."
    },
    # 45
    {
        "subtopic": "Legal and Regulatory Audit",
        "stem_en": "What is the mandatory first step of the CAG's audit, known as 'Legal and Regulatory Audit'?",
        "stem_ta": "சி.ஏ.ஜி தணிக்கையின் கட்டாய முதல் படியான 'சட்ட மற்றும் ஒழுங்குமுறைத் தணிக்கை' (Legal & Regulatory Audit) என்பது என்ன?",
        "options": [
            ("Verifying whether expenditure was sanctioned by appropriate authority and backed by a valid legislative law", "செலவினங்கள் தகுதியான அதிகாரியால் அங்கீகரிக்கப்பட்டுள்ளதா என்பதையும் செல்லுபடியாகும் சட்டமன்றச் சட்டத்தின் ஆதரவு உள்ளதா என்பதையும் சரிபார்த்தல்"),
            ("Conducting criminal trials of corrupt ministers in open court", "ஊழல் அமைச்சர்கள் மீது நீதிமன்றத்தில் குற்றவியல் விசாரணை நடத்துதல்"),
            ("Rewriting the statutory financial rules of the Finance Ministry", "நிதி அமைச்சகத்தின் சட்டப்பூர்வ நிதி விதிகளை மாற்றி எழுதுதல்"),
            ("Estimating the total black money circulating in the economy", "பொருளாதாரத்தில் புழங்கும் மொத்த கருப்புப் பணத்தைக் கணக்கிடுதல்")
        ],
        "exp_en": "Legal and regulatory audit is an obligatory function ensuring that money shown in accounts as dispersed was legally available, sanctioned by competent authority, and conforms to governing laws.",
        "exp_ta": "சட்ட மற்றும் ஒழுங்குமுறைத் தணிக்கை என்பது கணக்குகளில் காட்டப்பட்ட செலவு சட்டப்பூர்வமாக அனுமதிக்கப்பட்டதா, தகுதிவாய்ந்த அதிகாரியால் ஒப்பளிக்கப்பட்டு உரிய சட்ட விதிகளுக்கு உட்பட்டுள்ளதா என்பதைச் சரிபார்க்கும் கட்டாயப் பணியாகும்.",
        "tip_en": "Legal/Regulatory Audit is compulsory; Propriety Audit is discretionary.",
        "tip_ta": "சட்ட/ஒழுங்குமுறைத் தணிக்கை கட்டாயமானது; முறையுடைமைத் தணிக்கை விருப்பத்திற்குரியது.",
        "fact_en": "This primary audit ensures that executive expenditure strictly obeys legislative will.",
        "fact_ta": "இந்த முதன்மைத் தணிக்கை நிர்வாகச் செலவினங்கள் நாடாளுமன்ற விருப்பத்திற்கு உட்பட்டிருப்பதை உறுதி செய்கிறது."
    },
    # 46
    {
        "subtopic": "Administrative Ministry Role",
        "stem_en": "Which department in the Government of India provides budget allocation and administrative interface for the IA&AD, while maintaining the CAG's functional independence?",
        "stem_ta": "சி.ஏ.ஜி-யின் செயல்பாட்டு சுதந்திரத்தைப் பராமரிக்கும் அதே வேளையில், IA&AD-க்கான பட்ஜெட் ஒதுக்கீடு மற்றும் நிர்வாகத் தொடர்பை வழங்கும் மத்திய அரசுத் துறை எது?",
        "options": [
            ("Ministry of Finance (Department of Expenditure)", "நிதி அமைச்சகம் (செலவினத் துறை)"),
            ("Ministry of Home Affairs", "உள்துறை அமைச்சகம்"),
            ("Prime Minister's Office directly", "பிரதமர் அலுவலகம் நேரடியாக"),
            ("Ministry of Parliamentary Affairs", "நாடாளுமன்ற விவகாரங்கள் அமைச்சகம்")
        ],
        "exp_en": "The Ministry of Finance (Department of Expenditure) coordinates the budgetary allocations for the CAG's office, though expenses are charged on the Consolidated Fund of India.",
        "exp_ta": "செலவினங்கள் இந்தியத் திரட்டப்பட்ட நிதியில் சார்ஜ் செய்யப்பட்டாலும், நிதி அமைச்சகத்தின் செலவினத் துறை CAG அலுவலகத்திற்கான பட்ஜெட் ஏற்பாடுகளை ஒருங்கிணைக்கிறது.",
        "tip_en": "Ministry of Finance provides the administrative interface, but CANNOT alter CAG's audit findings.",
        "tip_ta": "நிதி அமைச்சகம் நிர்வாக ஏற்பாடுகளைக் கையாள்கிறது, ஆனால் CAG-யின் தணிக்கை முடிவுகளில் தலையிட முடியாது.",
        "fact_en": "The CAG's independence ensures that he reports directly to Parliament through the President, not to any ministry.",
        "fact_ta": "சி.ஏ.ஜி எந்த அமைச்சகத்திற்கும் பொறுப்பல்லாமல், குடியரசுத் தலைவர் மூலம் நேரடியாக நாடாளுமன்றத்திற்கே அறிக்கை அளிக்கிறார்."
    },
    # 47
    {
        "subtopic": "Accountability of Government Corporations",
        "stem_en": "Why are bodies like the Reserve Bank of India (RBI) and Life Insurance Corporation (LIC) kept outside the direct audit jurisdiction of the CAG?",
        "stem_ta": "இந்திய ரிசர்வ் வங்கி (RBI) மற்றும் எல்.ஐ.சி (LIC) போன்ற அமைப்புகள் ஏன் சி.ஏ.ஜி-யின் நேரடித் தணிக்கை வரம்பிற்கு வெளியே வைக்கப்பட்டுள்ளன?",
        "options": [
            ("Their governing parliamentary statutes specifically provide for audit by private chartered accountants to maintain commercial flexibility", "அவற்றின் நாடாளுமன்றச் சட்டங்கள் வணிக நெகிழ்வுத்தன்மையைப் பாதுகாக்க தனியார் தணிக்கையாளர்கள் மூலமே தணிக்கை செய்ய வகைசெய்துள்ளன"),
            ("Because they do not handle any public or sovereign funds", "ஏனெனில் அவை எந்தவொரு பொது அல்லது இறையாண்மை நிதியையும் கையாள்வதில்லை"),
            ("Because the Supreme Court has declared all financial corporations private", "ஏனெனில் உச்ச நீதிமன்றம் அனைத்து நிதி நிறுவனங்களையும் தனியார் நிறுவனங்கள் என அறிவித்துவிட்டது"),
            ("Because their accounts are classified as national military secrets", "ஏனெனில் அவற்றின் கணக்குகள் தேசிய ராணுவ ரகசியங்களாக வகைப்படுத்தப்பட்டுள்ளன")
        ],
        "exp_en": "Certain financial and banking institutions require operational autonomy and commercial flexibility; their governing Acts provide for audit by chartered accountants appointed by the Government.",
        "exp_ta": "சில நிதி மற்றும் வங்கி நிறுவனங்களுக்கு செயல்பாட்டு சுயாட்சியும் வணிக நெகிழ்வுத்தன்மையும் தேவைப்படுவதால், அவற்றின் சட்டங்கள் அரசால் நியமிக்கப்படும் பட்டயக் கணக்காளர்கள் மூலம் தணிக்கை செய்ய வகைசெய்துள்ளன.",
        "tip_en": "RBI, SBI, LIC: Audited exclusively by private chartered accountants, NOT directly by CAG.",
        "tip_ta": "RBI, SBI, LIC: தனியார் பட்டயக் கணக்காளர்களால் மட்டுமே தணிக்கை செய்யப்படுகின்றன, CAG-யால் நேரடியாக அல்ல.",
        "fact_en": "However, the CAG can audit the government's share of profits received from these institutions.",
        "fact_ta": "எனினும் இந்த நிறுவனங்களிலிருந்து அரசு பெறும் லாபப் பங்கீட்டை CAG தணிக்கை செய்ய முடியும்."
    },
    # 48
    {
        "subtopic": "Controller General of Accounts vs CAG",
        "stem_en": "What is the key difference between the Comptroller and Auditor General (CAG) and the Controller General of Accounts (CGA)?",
        "stem_ta": "தலைமைக் கணக்குத் தணிக்கையாளருக்கும் (CAG) கணக்குத் துறை கட்டுப்பாட்டு அதிகாரிக்கும் (CGA) இடையிலான முக்கிய வேறுபாடு என்ன?",
        "options": [
            ("CAG is an independent constitutional audit authority under Art 148; CGA is an executive accounting officer under the Ministry of Finance", "CAG சரத்து 148-ன் கீழ் உள்ள சுதந்திர அரசியலமைப்புத் தணிக்கை அதிகாரி; CGA நிதி அமைச்சகத்தின் கீழ் உள்ள நிர்வாகக் கணக்கு அதிகாரி"),
            ("CAG maintains accounting registers; CGA conducts independent audit of Parliament", "CAG கணக்கு ஏடுகளைப் பராமரிக்கிறார்; CGA நாடாளுமன்றத்தின் சுதந்திரத் தணிக்கையை நடத்துகிறார்"),
            ("Both are identical constitutional posts under Part V Chapter V", "இருவருமே பகுதி V அத்தியாயம் V-ன் கீழ் உள்ள ஒரே மாதிரியான அரசியலமைப்புப் பதவிகள்"),
            ("CGA outranks the CAG in the constitutional Table of Precedence", "அரசியலமைப்பு முன்னுரிமைப் பட்டியலில் CGA சி.ஏ.ஜி-யை விட உயர்ந்தவர்"),
        ],
        "exp_en": "The CAG is an independent constitutional authority under Article 148 responsible for audit. The CGA is an officer in the Department of Expenditure, Ministry of Finance, responsible for accounting and payment functions for the Union Government.",
        "exp_ta": "CAG சரத்து 148-ன் கீழான தணிக்கைக்குப் பொறுப்பான சுதந்திர அரசியலமைப்பு அதிகாரி. CGA நிதி அமைச்சகத்தின் கீழ் மத்திய அரசின் கணக்குகளைப் பராமரிக்கும் நிர்வாக அதிகாரி ஆவார்.",
        "tip_en": "CAG = Constitutional, Auditing, Independent. CGA = Non-constitutional, Accounting, Ministry of Finance.",
        "tip_ta": "CAG = அரசியலமைப்பு, தணிக்கை, சுதந்திரமானது. CGA = அரசியலமைப்பற்றது, கணக்கு வைப்பது, நிதி அமைச்சகம்.",
        "fact_en": "CGA prepares the Monthly Accounts and Annual Appropriation/Finance accounts of the Union Government.",
        "fact_ta": "மத்திய அரசின் மாதாந்திர மற்றும் வருடாந்திர நிதிக் கணக்குகளை CGA தயாரிக்கிறார்."
    },
    # 49
    {
        "subtopic": "Audit Quality and Guidelines",
        "stem_en": "Under which international organization of supreme audit institutions does the CAG of India formulate and benchmark national auditing standards?",
        "stem_ta": "எந்த சர்வதேச உச்ச தணிக்கை அமைப்புகள் நிறுவனத்தின் கீழ் இந்திய CAG தேசியத் தணிக்கைத் தரங்களை வடிவமைத்து ஒப்பிடுகிறார்?",
        "options": [
            ("INTOSAI (International Organization of Supreme Audit Institutions)", "INTOSAI (சர்வதேச உச்ச தணிக்கை அமைப்புகள் நிறுவனம்)"),
            ("International Monetary Fund (IMF)", "சர்வதேச நாணய நிதியம் (IMF)"),
            ("World Intellectual Property Organization (WIPO)", "உலக அறிவுசார் சொத்து நிறுவனம் (WIPO)"),
            ("Financial Action Task Force (FATF)", "நிதி நடவடிக்கை பணிக்குழு (FATF)")
        ],
        "exp_en": "The CAG of India is a prominent member of INTOSAI (International Organization of Supreme Audit Institutions) and aligns Indian auditing standards with international best practices.",
        "exp_ta": "இந்திய CAG, சர்வதேச உச்ச தணிக்கை அமைப்புகள் நிறுவனத்தின் (INTOSAI) முக்கிய உறுப்பினராக விளங்கி, இந்தியத் தணிக்கைத் தரங்களை சர்வதேச சிறந்த நடைமுறைகளுடன் இணைக்கிறார்.",
        "tip_en": "INTOSAI is the global umbrella organization for external government audit institutions.",
        "tip_ta": "INTOSAI என்பது அரசாங்க வெளித் தணிக்கை நிறுவனங்களுக்கான உலகளாவிய குடை அமைப்பாகும்.",
        "fact_en": "The CAG of India also plays a leading role in ASOSAI (Asian Organization of Supreme Audit Institutions).",
        "fact_ta": "ஆசிய உச்ச தணிக்கை நிறுவன அமைப்பிலும் (ASOSAI) இந்திய CAG முன்னணிப் பங்கு வகிக்கிறார்."
    },
    # 50
    {
        "subtopic": "Constitutional Chapter Summary",
        "stem_en": "Which of the following summaries correctly captures Articles 148 to 151 in Part V of the Constitution of India?",
        "stem_ta": "இந்திய அரசியலமைப்பின் பகுதி V-ல் உள்ள சரத்துகள் 148 முதல் 151 வரையிலான சரியான சுருக்கம் எது?",
        "options": [
            ("148: Office of CAG, 149: Duties & Powers, 150: Form of Accounts, 151: Audit Reports", "148: CAG அலுவலகம், 149: கடமைகள் & அதிகாரங்கள், 150: கணக்குகளின் படிவம், 151: தணிக்கை அறிக்கைகள்"),
            ("148: Finance Commission, 149: Election Commission, 150: UPSC, 151: Attorney General", "148: நிதி ஆணையம், 149: தேர்தல் ஆணையம், 150: யுபிஎஸ்சி, 151: தலைமை வழக்கறிஞர்"),
            ("148: Supreme Court Judges, 149: High Court Judges, 150: District Judges, 151: Tribunals", "148: உச்ச நீதிமன்ற நீதிபதிகள், 149: உயர் நீதிமன்ற நீதிபதிகள், 150: மாவட்ட நீதிபதிகள், 151: தீர்ப்பாயங்கள்"),
            ("148: President, 149: Vice-President, 150: Prime Minister, 151: Council of Ministers", "148: குடியரசுத் தலைவர், 149: துணைக் குடியரசுத் தலைவர், 150: பிரதமர், 151: அமைச்சரவை")
        ],
        "exp_en": "Articles 148-151 form Chapter V of Part V: Art 148 (Comptroller and Auditor-General of India), Art 149 (Duties and powers of the CAG), Art 150 (Form of accounts of the Union and States), Art 151 (Audit reports).",
        "exp_ta": "பகுதி V அத்தியாயம் V-ல் உள்ள சரத்துகள்: சரத்து 148 (CAG அலுவலகம்), சரத்து 149 (கடமைகள் & அதிகாரங்கள்), சரத்து 150 (கணக்குகளின் படிவம்), சரத்து 151 (தணிக்கை அறிக்கைகள்).",
        "tip_en": "Memorize the core quartet: 148 (Post), 149 (Powers), 150 (Form), 151 (Reports).",
        "tip_ta": "நான்கு முக்கிய சரத்துகளை நினைவில் வையுங்கள்: 148 (பதவி), 149 (அதிகாரங்கள்), 150 (படிவம்), 151 (அறிக்கைகள்).",
        "fact_en": "These four articles constitute the entire constitutional chapter dedicated to financial oversight in India.",
        "fact_ta": "இந்த நான்கு சரத்துகளும் இந்தியாவில் நிதி மேற்பார்வைக்கு அர்ப்பணிக்கப்பட்ட முழுமையான அரசியலமைப்பு அத்தியாயத்தை உருவாக்குகின்றன."
    }
]

def build_questions():
    questions = []
    for i, item in enumerate(raw_easy_data):
        qid = f"CAG_E_{i+1:03d}"
        opts = item["options"]
        correct_key = "A" # Initially option index 0 is correct
        
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
            diff="Easy",
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
            tags=["polity", "comptroller_and_auditor_general", "easy", item["subtopic"].lower().replace(" ", "_")]
        )
        questions.append(q)
    return questions

if __name__ == "__main__":
    qs = build_questions()
    print(f"Generated {len(qs)} raw Easy questions for CAG.")
    
    balanced_qs = balance_question_keys(qs)
    
    out_path = os.path.join("data", "questions", "polity", "cag_easy.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(balanced_qs, f, ensure_ascii=False, indent=2)
        
    print(f"Saved balanced Easy MCQs to {out_path}")
    
    val = ContentValidator()
    report = val.validate_file(out_path, expected_count=50, expected_prefix="CAG_E_")
    print(f"Validation Report: {'PASS' if report.is_valid else 'FAIL'} | Total: {report.total_audited}")
    if not report.is_valid:
        for iss in report.issues[:10]:
            print(f"  Issue: {iss}")
    print(f"Key Distribution: {report.key_distribution}")
