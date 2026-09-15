# -*- coding: utf-8 -*-
"""
State Election & Finance Commissions - Part 2A PYQ Practice MCQs Generator (50 MCQs: SEFC_PYQ_001 to SEFC_PYQ_050)
TNPSC Nova AI Content Engine
"""
import json
import os
from state_election_finance_commissions_mcq_helper import make_sefc_q
from tools.nova_content_engine.answer_randomizer import randomize_and_balance_dataset
from tools.nova_content_engine.validator import ContentValidator


def get_pyq_questions():
    raw_data = [
        # 1
        {
            "subtopic": "State Election Commission - Constitutional Mandate & Provisions (Articles 243K & 243ZA)",
            "stem_en": "[TNPSC Group 1 2014, Group 2 2018]\nWhich Article of the Constitution of India provides for the establishment of the State Election Commission for conducting elections to Panchayats?",
            "stem_ta": "[TNPSC குரூப் 1 2014, குரூப் 2 2018]\nபஞ்சாயத்துகளுக்கான தேர்தல்களை நடத்துவதற்கு மாநில தேர்தல் ஆணையத்தை நிறுவ வகை செய்யும் இந்திய அரசியலமைப்பின் சரத்து எது?",
            "options": [
                ("Article 243K", "சரத்து 243K"),
                ("Article 243-I", "சரத்து 243-I"),
                ("Article 243D", "சரத்து 243D"),
                ("Article 243E", "சரத்து 243E")
            ],
            "correct_key": "A",
            "exp_en": "Article 243K provides for elections to the Panchayats and vests the superintendence, direction, and control of the preparation of electoral rolls and the conduct of all elections in the State Election Commission.",
            "exp_ta": "சரத்து 243K பஞ்சாயத்துகளுக்கான தேர்தல்களை வழங்குகிறது மற்றும் வாக்காளர் பட்டியல்களைத் தயாரித்தல் மற்றும் அனைத்துத் தேர்தல்களையும் நடத்துவதற்கான மேற்பார்வை, வழிகாட்டல் மற்றும் கட்டுப்பாட்டை மாநில தேர்தல் ஆணையத்திடம் ஒப்படைக்கிறது.",
            "why_a_en": "Article 243K specifically establishes the State Election Commission for Panchayats.",
            "why_a_ta": "சரத்து 243K குறிப்பாக பஞ்சாயத்துகளுக்கான மாநில தேர்தல் ஆணையத்தை நிறுவுகிறது.",
            "why_b_en": "Article 243-I provides for the State Finance Commission.",
            "why_b_ta": "சரத்து 243-I மாநில நிதி ஆணையத்தை வழங்குகிறது.",
            "why_c_en": "Article 243D provides for reservation of seats in Panchayats.",
            "why_c_ta": "சரத்து 243D பஞ்சாயத்துகளில் இடஒதுக்கீட்டை வழங்குகிறது.",
            "why_d_en": "Article 243E provides for the duration of Panchayats (5 years).",
            "why_d_ta": "சரத்து 243E பஞ்சாயத்துகளின் கால அளவை (5 ஆண்டுகள்) வழங்குகிறது.",
            "tip_en": "Remember: 243K = Kalagam / Kondattam / Kommission (Election Commission).",
            "tip_ta": "நினைவில் கொள்க: 243K = மாநில தேர்தல் ஆணையம் (Panchayat Elections).",
            "fact_en": "Article 243ZA mirrors Article 243K for Municipalities.",
            "fact_ta": "சரத்து 243ZA நகராட்சிகளுக்கு சரத்து 243K-ஐப் பிரதிபலிக்கிறது."
        },

        # 2
        {
            "subtopic": "State Finance Commission - Constitutional Mandate, Composition & Role (Articles 243I & 243Y)",
            "stem_en": "[TNPSC Group 2 2015, Group 4 2019]\nUnder which Article of the Constitution of India is the State Finance Commission constituted by the Governor?",
            "stem_ta": "[TNPSC குரூப் 2 2015, குரூப் 4 2019]\nஇந்திய அரசியலமைப்பின் எந்த சரத்தின் கீழ் ஆளுநரால் மாநில நிதி ஆணையம் அமைக்கப்படுகிறது?",
            "options": [
                ("Article 243-I", "சரத்து 243-I"),
                ("Article 243K", "சரத்து 243K"),
                ("Article 243Z", "சரத்து 243Z"),
                ("Article 280", "சரத்து 280")
            ],
            "correct_key": "A",
            "exp_en": "Under Article 243-I, the Governor of a State is mandated to constitute a Finance Commission at the expiration of every fifth year to review the financial position of the Panchayats.",
            "exp_ta": "சரத்து 243-I-ன் கீழ், பஞ்சாயத்துகளின் நிதி நிலையை மறுஆய்வு செய்வதற்காக ஒவ்வொரு ஐந்தாவது ஆண்டின் முடிவிலும் ஒரு நிதி ஆணையத்தை அமைக்க மாநில ஆளுநர் கடமைப்பட்டுள்ளார்.",
            "why_a_en": "Article 243-I provides for the constitution of the State Finance Commission.",
            "why_a_ta": "சரத்து 243-I மாநில நிதி ஆணையத்தை அமைப்பதற்கு வகை செய்கிறது.",
            "why_b_en": "Article 243K provides for the State Election Commission.",
            "why_b_ta": "சரத்து 243K மாநில தேர்தல் ஆணையத்தை வழங்குகிறது.",
            "why_c_en": "Article 243Z provides for the audit of accounts of Municipalities.",
            "why_c_ta": "சரத்து 243Z நகராட்சிகளின் கணக்குகளை தணிக்கை செய்வதை வழங்குகிறது.",
            "why_d_en": "Article 280 provides for the Union Finance Commission constituted by the President.",
            "why_d_ta": "சரத்து 280 குடியரசுத் தலைவரால் அமைக்கப்படும் மத்திய நிதி ஆணையத்தை வழங்குகிறது.",
            "tip_en": "Article 243-I = Income / Investment / Finance Commission for Panchayats.",
            "tip_ta": "சரத்து 243-I = வருமானம் / நிதி ஆணையம் (பஞ்சாயத்துகள்).",
            "fact_en": "Article 243Y mandates the same Commission to review municipal finances.",
            "fact_ta": "சரத்து 243Y நகராட்சி நிதியையும் மறுஆய்வு செய்ய அதே ஆணையத்தை பணிக்கிறது."
        },

        # 3
        {
            "subtopic": "State Election Commissioner - Appointment, Tenure, Removal & Autonomy",
            "stem_en": "[TNPSC Group 1 2017]\nWho appoints the State Election Commissioner under Article 243K of the Indian Constitution?",
            "stem_ta": "[TNPSC குரூப் 1 2017]\nஇந்திய அரசியலமைப்பின் சரத்து 243K-ன் கீழ் மாநில தேர்தல் ஆணையரை நியமிப்பவர் யார்?",
            "options": [
                ("The Governor of the State", "மாநில ஆளுநர்"),
                ("The Chief Election Commissioner of India", "இந்திய தலைமை தேர்தல் ஆணையர்"),
                ("The Chief Minister of the State", "மாநில முதலமைச்சர்"),
                ("The Chief Justice of the High Court", "உயர் நீதிமன்ற தலைமை நீதிபதி")
            ],
            "correct_key": "A",
            "exp_en": "Article 243K(1) explicitly provides that the State Election Commissioner shall be appointed by the Governor of the State.",
            "exp_ta": "சரத்து 243K(1) மாநில தேர்தல் ஆணையர் மாநில ஆளுநரால் நியமிக்கப்படுவார் என்று வெளிப்படையாகக் கூறுகிறது.",
            "why_a_en": "The Governor is the constitutional appointing authority under Article 243K(1).",
            "why_a_ta": "சரத்து 243K(1)-ன் கீழ் ஆளுநரே அரசியலமைப்பு நியமன அதிகாரியாவார்.",
            "why_b_en": "The Chief Election Commissioner has no role in appointing the SEC.",
            "why_b_ta": "தலைமை தேர்தல் ஆணையருக்கு SEC-ஐ நியமிப்பதில் எந்த பங்கும் இல்லை.",
            "why_c_en": "The Chief Minister does not make formal constitutional appointments.",
            "why_c_ta": "முதலமைச்சர் முறையான அரசியலமைப்பு நியமனங்களை மேற்கொள்வதில்லை.",
            "why_d_en": "The High Court Chief Justice has no appointment power for the SEC.",
            "why_d_ta": "உயர் நீதிமன்ற தலைமை நீதிபதிக்கு SEC நியமன அதிகாரம் இல்லை.",
            "tip_en": "Appointment of SEC: Governor. Removal of SEC: In like manner as a High Court Judge.",
            "tip_ta": "SEC நியமனம்: ஆளுநர். SEC நீக்கம்: உயர் நீதிமன்ற நீதிபதியைப் போன்ற முறையில்.",
            "fact_en": "The Governor acts on the aid and advice of the Council of Ministers while appointing the SEC.",
            "fact_ta": "SEC-ஐ நியமிக்கும் போது அமைச்சரவையின் உதவி மற்றும் ஆலோசனையின் பேரில் ஆளுநர் செயல்படுகிறார்."
        },

        # 4
        {
            "subtopic": "State Election Commissioner - Appointment, Tenure, Removal & Autonomy",
            "stem_en": "[TNPSC Group 2 2018, Group 4 2021]\nA State Election Commissioner can be removed from office only in like manner and on like grounds as:",
            "stem_ta": "[TNPSC குரூப் 2 2018, குரூப் 4 2021]\nஒரு மாநில தேர்தல் ஆணையரை எந்த முறையில் மற்றும் எந்த அடிப்படைகளில் மட்டுமே பதவியில் இருந்து நீக்க முடியும்?",
            "options": [
                ("A Judge of a High Court", "ஒரு உயர் நீதிமன்ற நீதிபதி"),
                ("The Advocate General of the State", "மாநிலத்தின் தலைமை வழக்கறிஞர் (Advocate General)"),
                ("A Member of the State Public Service Commission", "மாநில அரசுப் பணியாளர் தேர்வாணையத்தின் உறுப்பினர்"),
                ("The Chief Secretary to the State Government", "மாநில அரசின் தலைமைச் செயலாளர்")
            ],
            "correct_key": "A",
            "exp_en": "Under the first proviso to Article 243K(2), the State Election Commissioner shall not be removed from his office except in like manner and on the like grounds as a Judge of a High Court.",
            "exp_ta": "சரத்து 243K(2)-ன் முதல் வரம்புரையின் கீழ், ஒரு உயர் நீதிமன்ற நீதிபதியை நீக்கும் முறையிலும் அடிப்படைகளிலும் தவிர மாநில தேர்தல் ஆணையரை அவரது பதவியில் இருந்து நீக்க முடியாது.",
            "why_a_en": "The constitutional benchmark for removing an SEC is that of a High Court Judge.",
            "why_a_ta": "SEC-ஐ நீக்குவதற்கான அரசியலமைப்பு அளவுகோல் ஒரு உயர் நீதிமன்ற நீதிபதியினுடையதாகும்.",
            "why_b_en": "Advocate General holds office during the pleasure of the Governor.",
            "why_b_ta": "அட்வகேட் ஜெனரல் ஆளுநரின் விருப்பம் உள்ளவரை பதவியில் இருப்பார்.",
            "why_c_en": "SPSC members are removed by the President under Article 317 after SC inquiry.",
            "why_c_ta": "SPSC உறுப்பினர்கள் உச்ச நீதிமன்ற விசாரணைக்குப் பின் குடியரசுத் தலைவரால் நீக்கப்படுகிறார்கள்.",
            "why_d_en": "Chief Secretary is an executive civil servant subject to state service rules.",
            "why_d_ta": "தலைமைச் செயலாளர் என்பவர் மாநில அரசுப் பணி விதிகளுக்கு உட்பட்ட ஒரு அரசு ஊழியர்.",
            "tip_en": "SEC removal security = High Court Judge removal security (Parliamentary address).",
            "tip_ta": "SEC நீக்கப் பாதுகாப்பு = உயர் நீதிமன்ற நீதிபதி நீக்கப் பாதுகாப்பு (நாடாளுமன்றத் தீர்மானம்).",
            "fact_en": "This ensures complete independence of local elections from arbitrary state government dismissal.",
            "fact_ta": "இது மாநில அரசின் தன்னிச்சையான பணிநீக்கத்திலிருந்து உள்ளாட்சித் தேர்தல்களின் முழு சுதந்திரத்தை உறுதி செய்கிறது."
        },

        # 5
        {
            "subtopic": "State Finance Commission - Constitutional Mandate, Composition & Role (Articles 243I & 243Y)",
            "stem_en": "[TNPSC Assistant Section Officer 2016, Group 2 2019]\nThe recommendations made by the State Finance Commission are submitted to whom?",
            "stem_ta": "[TNPSC உதவிப் பிரிவு அலுவலர் 2016, குரூப் 2 2019]\nமாநில நிதி ஆணையத்தால் செய்யப்படும் பரிந்துரைகள் யாரிடம் சமர்ப்பிக்கப்படுகின்றன?",
            "options": [
                ("The Governor of the State", "மாநில ஆளுநர்"),
                ("The Speaker of the Legislative Assembly", "சட்டமன்றப் பேரவைத் தலைவர்"),
                ("The Chief Minister of the State", "மாநில முதலமைச்சர்"),
                ("The Union Finance Minister", "மத்திய நிதி அமைச்சர்")
            ],
            "correct_key": "A",
            "exp_en": "Under Article 243-I(4), the SFC submits its report to the Governor, who then causes every recommendation along with an explanatory memorandum to be laid before the State Legislature.",
            "exp_ta": "சரத்து 243-I(4)-ன் கீழ், SFC தனது அறிக்கையை ஆளுநரிடம் சமர்ப்பிக்கிறது, பின்னர் ஆளுநர் ஒவ்வொரு பரிந்துரையையும் ஒரு விளக்கக் குறிப்புடன் மாநில சட்டமன்றத்தின் முன் வைக்கச் செய்கிறார்.",
            "why_a_en": "The Governor is the constitutional recipient of the SFC report.",
            "why_a_ta": "ஆளுநரே SFC அறிக்கையைப் பெறும் அரசியலமைப்பு அதிகாரியாவார்.",
            "why_b_en": "The Speaker presides over the Assembly where the report is later tabled by the government.",
            "why_b_ta": "அறிக்கை சட்டமன்றத்தில் வைக்கப்படும் போது சபாநாயகர் தலைமை தாங்குகிறார்.",
            "why_c_en": "The Chief Minister heads the cabinet which prepares the action taken report.",
            "why_c_ta": "முதலமைச்சர் நடவடிக்கை எடுக்கப்பட்ட அறிக்கையைத் தயாரிக்கும் அமைச்சரவைக்குத் தலைமை தாங்குகிறார்.",
            "why_d_en": "The Union Finance Minister receives the Central Finance Commission report via the President.",
            "why_d_ta": "மத்திய நிதி அமைச்சர் குடியரசுத் தலைவர் மூலம் மத்திய நிதி ஆணைய அறிக்கையைப் பெறுகிறார்.",
            "tip_en": "SFC submits to Governor -> Governor causes it to be laid before State Legislature.",
            "tip_ta": "SFC ஆளுநரிடம் சமர்ப்பிக்கிறது -> ஆளுநர் அதை மாநில சட்டமன்றத்தின் முன் வைக்கச் செய்கிறார்.",
            "fact_en": "The Governor causes the report to be laid together with an explanatory memorandum (Action Taken Report).",
            "fact_ta": "ஆளுநர் இந்த அறிக்கையை எடுக்கப்பட்ட நடவடிக்கை அறிக்கையுடன் (ATR) சட்டமன்றத்தில் வைக்கச் செய்கிறார்."
        },

        # 6
        {
            "subtopic": "State Election Commission - Constitutional Mandate & Provisions (Articles 243K & 243ZA)",
            "stem_en": "[TNPSC Group 4 2016, VAO 2017]\nWhich Article of the Constitution of India provides for the conduct of municipal elections by the State Election Commission?",
            "stem_ta": "[TNPSC குரூப் 4 2016, VAO 2017]\nநகராட்சித் தேர்தல்களை மாநில தேர்தல் ஆணையம் நடத்துவதற்கு வகை செய்யும் இந்திய அரசியலமைப்பின் சரத்து எது?",
            "options": [
                ("Article 243ZA", "சரத்து 243ZA"),
                ("Article 243K", "சரத்து 243K"),
                ("Article 243Y", "சரத்து 243Y"),
                ("Article 243ZG", "சரத்து 243ZG")
            ],
            "correct_key": "A",
            "exp_en": "Article 243ZA applies the provisions of Article 243K to Municipalities, vesting the superintendence, direction, and control of elections to Municipalities in the State Election Commission.",
            "exp_ta": "சரத்து 243ZA சரத்து 243K-ன் விதிகளை நகராட்சிகளுக்குப் பயன்படுத்துகிறது, நகராட்சிகளுக்கான தேர்தல்களின் மேற்பார்வை, வழிகாட்டுதல் மற்றும் கட்டுப்பாட்டை மாநில தேர்தல் ஆணையத்திடம் ஒப்படைக்கிறது.",
            "why_a_en": "Article 243ZA specifically governs elections to Municipalities.",
            "why_a_ta": "சரத்து 243ZA குறிப்பாக நகராட்சிகளுக்கான தேர்தல்களை நிர்வகிக்கிறது.",
            "why_b_en": "Article 243K governs elections to Panchayats.",
            "why_b_ta": "சரத்து 243K பஞ்சாயத்துகளுக்கான தேர்தல்களை நிர்வகிக்கிறது.",
            "why_c_en": "Article 243Y governs the Finance Commission for Municipalities.",
            "why_c_ta": "சரத்து 243Y நகராட்சிகளுக்கான நிதி ஆணையத்தை நிர்வகிக்கிறது.",
            "why_d_en": "Article 243ZG bars interference by courts in municipal electoral matters.",
            "why_d_ta": "சரத்து 243ZG நகராட்சி தேர்தல் விவகாரங்களில் நீதிமன்றங்கள் தலையிடுவதைத் தடை செய்கிறது.",
            "tip_en": "Panchayat Elections = 243K. Municipality Elections = 243ZA.",
            "tip_ta": "பஞ்சாயத்து தேர்தல்கள் = 243K. நகராட்சி தேர்தல்கள் = 243ZA.",
            "fact_en": "Part IXA was inserted by the 74th Constitutional Amendment Act, 1992.",
            "fact_ta": "பகுதி IXA 1992-ல் 74வது அரசியலமைப்பு திருத்தச் சட்டத்தால் சேர்க்கப்பட்டது."
        },

        # 7
        {
            "subtopic": "Tamil Nadu State Election & Finance Commissions - Legal Framework, Rules & Precedents",
            "stem_en": "[TNPSC Group 1 2019]\nIn which year was the first statutory State Finance Commission constituted in Tamil Nadu following the 73rd and 74th Amendments?",
            "stem_ta": "[TNPSC குரூப் 1 2019]\n73 மற்றும் 74வது திருத்தங்களைத் தொடர்ந்து தமிழ்நாட்டில் முதல் சட்டப்பூர்வ மாநில நிதி ஆணையம் எந்த ஆண்டு அமைக்கப்பட்டது?",
            "options": [
                ("1994", "1994"),
                ("1992", "1992"),
                ("1996", "1996"),
                ("2000", "2000")
            ],
            "correct_key": "A",
            "exp_en": "The First State Finance Commission in Tamil Nadu was constituted in April 1994 under Section 240 of the Tamil Nadu Panchayats Act, 1994, and submitted its report in 1996.",
            "exp_ta": "தமிழ்நாட்டில் முதல் மாநில நிதி ஆணையம் 1994 தமிழ்நாடு பஞ்சாயத்துகள் சட்டத்தின் பிரிவு 240-ன் கீழ் ஏப்ரல் 1994-ல் அமைக்கப்பட்டு, 1996-ல் தனது அறிக்கையை சமர்ப்பித்தது.",
            "why_a_en": "1994 was the year when the First SFC was constituted in Tamil Nadu.",
            "why_a_ta": "1994-ல் தமிழ்நாட்டில் முதல் SFC அமைக்கப்பட்டது.",
            "why_b_en": "1992 was the year of passing of the 73rd and 74th Amendments.",
            "why_b_ta": "1992 என்பது 73 மற்றும் 74வது திருத்தங்கள் நிறைவேற்றப்பட்ட ஆண்டாகும்.",
            "why_c_en": "1996 was the year when the First SFC submitted its recommendations.",
            "why_c_ta": "1996 என்பது முதல் SFC தனது பரிந்துரைகளை சமர்ப்பித்த ஆண்டாகும்.",
            "why_d_en": "2000 was the year of constitution of the Second SFC.",
            "why_d_ta": "2000 என்பது இரண்டாவது SFC அமைக்கப்பட்ட ஆண்டாகும்.",
            "tip_en": "TN 1st SFC: Constituted 1994, submitted 1996, devolved funds starting 1997-98.",
            "tip_ta": "TN முதல் SFC: 1994-ல் அமைக்கப்பட்டது, 1996-ல் சமர்ப்பிக்கப்பட்டது, 1997-98 முதல் நிதியை பகிர்ந்தளித்தது.",
            "fact_en": "Tamil Nadu was among the earliest states to implement SFC recommendations systematically.",
            "fact_ta": "SFC பரிந்துரைகளை முறையாக செயல்படுத்திய ஆரம்பகால மாநிலங்களில் தமிழ்நாடும் ஒன்றாகும்."
        },

        # 8
        {
            "subtopic": "State Election Commission - Constitutional Mandate & Provisions (Articles 243K & 243ZA)",
            "stem_en": "[TNPSC Group 2 2017, Group 4 2018]\nWhat is the minimum age prescribed for contesting elections to a Panchayat or Municipality under Article 243F and 243V?",
            "stem_ta": "[TNPSC குரூப் 2 2017, குரூப் 4 2018]\nசரத்துகள் 243F மற்றும் 243V-ன் கீழ் ஒரு பஞ்சாயத்து அல்லது நகராட்சித் தேர்தலில் போட்டியிடுவதற்கு நிர்ணயிக்கப்பட்டுள்ள குறைந்தபட்ச வயது என்ன?",
            "options": [
                ("21 years", "21 வயது"),
                ("18 years", "18 வயது"),
                ("25 years", "25 வயது"),
                ("30 years", "30 வயது")
            ],
            "correct_key": "A",
            "exp_en": "Articles 243F(1)(a) and 243V(1)(a) provide that no person shall be disqualified on the ground that he is less than 25 years of age, if he has attained the age of 21 years.",
            "exp_ta": "சரத்துகள் 243F(1)(a) மற்றும் 243V(1)(a) ஒருவர் 21 வயதை அடைந்திருந்தால், அவர் 25 வயதுக்குக் குறைவானவர் என்ற காரணத்திற்காக தகுதி நீக்கம் செய்யப்பட மாட்டார் என்று கூறுகின்றன.",
            "why_a_en": "21 years is the constitutional minimum age for contesting local body polls.",
            "why_a_ta": "உள்ளாட்சித் தேர்தலில் போட்டியிட அரசியலமைப்பு குறைந்தபட்ச வயது 21 ஆகும்.",
            "why_b_en": "18 years is the minimum voting age (elector eligibility under Art 326).",
            "why_b_ta": "18 வயது என்பது வாக்களிப்பதற்கான குறைந்தபட்ச வயது (சரத்து 326).",
            "why_c_en": "25 years is the minimum age to contest Lok Sabha and State Legislative Assembly.",
            "why_c_ta": "25 வயது என்பது மக்களவை மற்றும் சட்டமன்றத்திற்கு போட்டியிடுவதற்கான குறைந்தபட்ச வயது.",
            "why_d_en": "30 years is the minimum age to contest Rajya Sabha and State Legislative Council.",
            "why_d_ta": "30 வயது என்பது மாநிலங்களவை மற்றும் சட்ட மேலவைக்கு போட்டியிடுவதற்கான குறைந்தபட்ச வயது.",
            "tip_en": "Local bodies contest age = 21 years. Assembly/Lok Sabha = 25 years. Rajya Sabha/Council = 30 years.",
            "tip_ta": "உள்ளாட்சிப் போட்டி வயது = 21. சட்டமன்றம்/மக்களவை = 25. மாநிலங்களவை/மேலவை = 30.",
            "fact_en": "The 61st Amendment reduced voting age to 18, but contesting age for local bodies remains 21.",
            "fact_ta": "61வது திருத்தம் வாக்களிக்கும் வயதை 18-ஆகக் குறைத்தது, ஆனால் உள்ளாட்சிப் போட்டி வயது 21-ஆகவே உள்ளது."
        },

        # 9
        {
            "subtopic": "Financial Devolution, Intergovernmental Transfers & Local Governance",
            "stem_en": "[TNPSC Executive Officer 2018, Group 2A 2017]\nWhich constitutional amendment act inserted Article 280(3)(bb) and Article 280(3)(c) relating to local bodies?",
            "stem_ta": "[TNPSC செயல் அலுவலர் 2018, குரூப் 2A 2017]\nஉள்ளாட்சி அமைப்புகள் தொடர்பான சரத்து 280(3)(bb) மற்றும் சரத்து 280(3)(c)-ஐ சேர்த்த அரசியலமைப்பு திருத்தச் சட்டங்கள் எவை?",
            "options": [
                ("73rd and 74th Constitutional Amendment Acts, 1992", "73வது மற்றும் 74வது அரசியலமைப்பு திருத்தச் சட்டங்கள், 1992"),
                ("42nd and 44th Constitutional Amendment Acts, 1976 and 1978", "42வது மற்றும் 44வது அரசியலமைப்பு திருத்தச் சட்டங்கள், 1976 மற்றும் 1978"),
                ("86th Constitutional Amendment Act, 2002", "86வது அரசியலமைப்பு திருத்தச் சட்டம், 2002"),
                ("101st Constitutional Amendment Act, 2016", "101வது அரசியலமைப்பு திருத்தச் சட்டம், 2016")
            ],
            "correct_key": "A",
            "exp_en": "The 73rd Amendment inserted Article 280(3)(bb) for Panchayats, and the 74th Amendment inserted Article 280(3)(c) for Municipalities, linking Central Finance Commission recommendations to State Finance Commission reports.",
            "exp_ta": "73வது திருத்தம் பஞ்சாயத்துகளுக்கு சரத்து 280(3)(bb)-ஐயும், 74வது திருத்தம் நகராட்சிகளுக்கு சரத்து 280(3)(c)-ஐயும் சேர்த்தது, இது மத்திய நிதி ஆணையத்தின் பரிந்துரைகளை மாநில நிதி ஆணைய அறிக்கைகளுடன் இணைக்கிறது.",
            "why_a_en": "The 73rd and 74th Amendments inserted these vital intergovernmental fiscal linkages.",
            "why_a_ta": "73 மற்றும் 74வது திருத்தங்கள் இந்த முக்கியமான நிதி இணைப்புகளைச் சேர்த்தன.",
            "why_b_en": "The 42nd and 44th Amendments were enacted prior to constitutionalizing local bodies.",
            "why_b_ta": "42 மற்றும் 44வது திருத்தங்கள் உள்ளாட்சிகளுக்கு அரசியலமைப்பு அந்தஸ்து வழங்குவதற்கு முன் இயற்றப்பட்டன.",
            "why_c_en": "The 86th Amendment relates to Right to Education (Article 21A).",
            "why_c_ta": "86வது திருத்தம் கல்வி உரிமை (சரத்து 21A) பற்றியது.",
            "why_d_en": "The 101st Amendment relates to Goods and Services Tax (GST).",
            "why_d_ta": "101வது திருத்தம் சரக்கு மற்றும் சேவை வரி (GST) பற்றியது.",
            "tip_en": "73rd = 280(3)(bb) for Panchayats. 74th = 280(3)(c) for Municipalities.",
            "tip_ta": "73வது = பஞ்சாயத்துகளுக்கு 280(3)(bb). 74வது = நகராட்சிகளுக்கு 280(3)(c).",
            "fact_en": "These sub-clauses empower Central FC to recommend grants-in-aid to augment State Consolidated Funds.",
            "fact_ta": "இந்த உட்பிரிவுகள் மாநில தொகுப்பு நிதியை பெருக்க மானியங்களை பரிந்துரைக்க மத்திய FC-க்கு அதிகாரம் அளிக்கின்றன."
        },

        # 10
        {
            "subtopic": "State Election Commission - Constitutional Mandate & Provisions (Articles 243K & 243ZA)",
            "stem_en": "[TNPSC Group 1 2021]\nUnder Article 243-O of the Constitution of India, an election to any Panchayat can be called in question ONLY through:",
            "stem_ta": "[TNPSC குரூப் 1 2021]\nஇந்திய அரசியலமைப்பின் சரத்து 243-O-ன் கீழ், எந்தவொரு பஞ்சாயத்துக்கான தேர்தலையும் எதன் மூலம் மட்டுமே கேள்விக்குள்ளாக்க முடியும்?",
            "options": [
                ("An Election Petition presented to the authority provided by State law", "மாநில சட்டம் வழங்கும் அதிகாரியிடம் சமர்ப்பிக்கப்படும் தேர்தல் மனு"),
                ("A Public Interest Litigation (PIL) filed in the Supreme Court before polling", "வாக்குப்பதிவுக்கு முன் உச்ச நீதிமன்றத்தில் தாக்கல் செய்யப்படும் பொது நல வழக்கு (PIL)"),
                ("A memorandum submitted directly to the District Collector", "மாவட்ட ஆட்சியரிடம் நேரடியாக சமர்ப்பிக்கப்படும் ஒரு மனு"),
                ("An adjournment motion moved in the State Legislative Assembly", "மாநில சட்டமன்றத்தில் கொண்டு வரப்படும் ஒத்திவைப்புத் தீர்மானம்")
            ],
            "correct_key": "A",
            "exp_en": "Article 243-O(b) mandates that no election to any Panchayat shall be called in question except by an election petition presented to such authority and in such manner as is provided by or under any law made by the Legislature of a State.",
            "exp_ta": "சரத்து 243-O(b) மாநில சட்டமன்றத்தால் இயற்றப்பட்ட சட்டத்தின் கீழ் அல்லது அதன்படி வழங்கப்பட்டுள்ள அத்தகைய அதிகாரியிடம் மற்றும் அத்தகைய முறையில் சமர்ப்பிக்கப்படும் தேர்தல் மனுவைத் தவிர வேறு எதன் மூலமும் எந்தவொரு பஞ்சாயத்துத் தேர்தலையும் கேள்விக்குள்ளாக்க முடியாது என்று கட்டாயப்படுத்துகிறது.",
            "why_a_en": "Election Petition is the sole constitutional method prescribed under Article 243-O(b).",
            "why_a_ta": "சரத்து 243-O(b)-ன் கீழ் பரிந்துரைக்கப்பட்ட ஒரே அரசியலமைப்பு முறை தேர்தல் மனு மட்டுமே.",
            "why_b_en": "PILs to stall or challenge elections during polling are barred by Article 243-O.",
            "why_b_ta": "வாக்குப்பதிவின் போது தேர்தலை நிறுத்த அல்லது சவால் செய்ய PIL-கள் சரத்து 243-O-ஆல் தடை செய்யப்பட்டுள்ளன.",
            "why_c_en": "Memorandums to Collectors are not judicial election dispute petitions.",
            "why_c_ta": "ஆட்சியர்களிடம் அளிக்கப்படும் மனுக்கள் நீதித்துறை தேர்தல் சர்ச்சை மனுக்கள் அல்ல.",
            "why_d_en": "Adjournment motions are legislative debate mechanisms, not election challenge forums.",
            "why_d_ta": "ஒத்திவைப்புத் தீர்மானங்கள் சட்டமன்ற விவாத வழிமுறைகளே தவிர தேர்தல் மன்றங்கள் அல்ல.",
            "tip_en": "Article 243-O = Bar on court interference; remedy ONLY via Election Petition.",
            "tip_ta": "சரத்து 243-O = நீதிமன்ற தலையீட்டிற்கான தடை; தேர்தல் மனு மூலம் மட்டுமே தீர்வு.",
            "fact_en": "Article 243ZG provides an identical bar for municipal elections.",
            "fact_ta": "சரத்து 243ZG நகராட்சித் தேர்தல்களுக்கும் இதேபோன்ற தடையை வழங்குகிறது."
        },

        # 11
        {
            "subtopic": "State Finance Commission - Constitutional Mandate, Composition & Role (Articles 243I & 243Y)",
            "stem_en": "[TNPSC Group 2 2012, Group 4 2015]\nHow often must a State Finance Commission be constituted under the Indian Constitution?",
            "stem_ta": "[TNPSC குரூப் 2 2012, குரூப் 4 2015]\nஇந்திய அரசியலமைப்பின் கீழ் மாநில நிதி ஆணையம் எவ்வளவு அடிக்கடி அமைக்கப்பட வேண்டும்?",
            "options": [
                ("Every 5 years", "ஒவ்வொரு 5 ஆண்டுகளுக்கும் ஒருமுறை"),
                ("Every 3 years", "ஒவ்வொரு 3 ஆண்டுகளுக்கும் ஒருமுறை"),
                ("Every 6 years", "ஒவ்வொரு 6 ஆண்டுகளுக்கும் ஒருமுறை"),
                ("Every 10 years", "ஒவ்வொரு 10 ஆண்டுகளுக்கும் ஒருமுறை")
            ],
            "correct_key": "A",
            "exp_en": "Article 243-I(1) mandates that the Governor shall constitute a Finance Commission at the expiration of every fifth year or at such earlier time as considered necessary.",
            "exp_ta": "சரத்து 243-I(1) ஒவ்வொரு ஐந்தாவது ஆண்டின் முடிவிலும் அல்லது அவசியமெனக் கருதப்படும் முன்னரே உள்ள நேரத்திலும் ஆளுநர் ஒரு நிதி ஆணையத்தை அமைக்க வேண்டும் என்று கட்டாயப்படுத்துகிறது.",
            "why_a_en": "Every 5 years is the constitutional periodicity under Article 243-I(1).",
            "why_a_ta": "ஒவ்வொரு 5 ஆண்டுகளும் என்பது சரத்து 243-I(1)-ன் கீழான அரசியலமைப்பு கால இடைவெளியாகும்.",
            "why_b_en": "3 years is incorrect.",
            "why_b_ta": "3 ஆண்டுகள் என்பது தவறானது.",
            "why_c_en": "6 years is incorrect.",
            "why_c_ta": "6 ஆண்டுகள் என்பது தவறானது.",
            "why_d_en": "10 years is the decennial census period, not the SFC frequency.",
            "why_d_ta": "10 ஆண்டுகள் என்பது மக்கள் தொகை கணக்கெடுப்பு காலம், SFC காலம் அல்ல.",
            "tip_en": "Both Central FC (Art 280) and State FC (Art 243-I) are constituted every 5 years.",
            "tip_ta": "மத்திய FC (சரத்து 280) மற்றும் மாநில FC (சரத்து 243-I) இரண்டும் ஒவ்வொரு 5 ஆண்டுகளுக்கும் அமைக்கப்படுகின்றன.",
            "fact_en": "The Governor may also constitute an SFC earlier if fiscal circumstances warrant.",
            "fact_ta": "நிதி சூழ்நிலைகள் அவசியமானால் ஆளுநர் முன்னரே SFC-ஐ அமைக்கலாம்."
        },

        # 12
        {
            "subtopic": "Tamil Nadu State Election & Finance Commissions - Legal Framework, Rules & Precedents",
            "stem_en": "[TNPSC Combined Engineering Services 2019]\nUnder Section 239 of the Tamil Nadu Panchayats Act, 1994, what is the initial term of office of the Tamil Nadu State Election Commissioner?",
            "stem_ta": "[TNPSC ஒருங்கிணைந்த பொறியியல் பணிகள் 2019]\n1994 தமிழ்நாடு பஞ்சாயத்துகள் சட்டத்தின் பிரிவு 239-ன் கீழ், தமிழ்நாடு மாநில தேர்தல் ஆணையரின் ஆரம்ப பதவிக்காலம் என்ன?",
            "options": [
                ("Two years", "இரண்டு ஆண்டுகள்"),
                ("Five years", "ஐந்து ஆண்டுகள்"),
                ("Six years", "ஆறு ஆண்டுகள்"),
                ("Three years", "மூன்று ஆண்டுகள்")
            ],
            "correct_key": "A",
            "exp_en": "Under Section 239 of the Tamil Nadu Panchayats Act, 1994 and the service rules, the State Election Commissioner holds office for an initial term of 2 years and is eligible for reappointment for two successive terms.",
            "exp_ta": "1994 தமிழ்நாடு பஞ்சாயத்துகள் சட்டத்தின் பிரிவு 239 மற்றும் பணி விதிகளின் கீழ், மாநில தேர்தல் ஆணையர் ஆரம்பத்தில் 2 ஆண்டுகள் பதவிக்காலம் வகிக்கிறார் மற்றும் அடுத்தடுத்த இரண்டு முறை மறுநியமனம் செய்ய தகுதியுடையவர்.",
            "why_a_en": "Two years is the initial statutory tenure prescribed in Tamil Nadu rules.",
            "why_a_ta": "தமிழ்நாடு விதிகளில் பரிந்துரைக்கப்பட்ட ஆரம்ப சட்டப்பூர்வ பதவிக்காலம் இரண்டு ஆண்டுகள் ஆகும்.",
            "why_b_en": "Five years is the duration of local bodies, not the statutory tenure of TN SEC.",
            "why_b_ta": "ஐந்து ஆண்டுகள் என்பது உள்ளாட்சி அமைப்புகளின் கால அளவு, TN SEC-ன் சட்டப்பூர்வ பதவிக்காலம் அல்ல.",
            "why_c_en": "Six years is the tenure of Central Election Commissioners under the EC Act 1991.",
            "why_c_ta": "ஆறு ஆண்டுகள் என்பது 1991 சட்டத்தின் கீழ் மத்திய தேர்தல் ஆணையர்களின் பதவிக்காலமாகும்.",
            "why_d_en": "Three years is incorrect for Tamil Nadu.",
            "why_d_ta": "மூன்று ஆண்டுகள் என்பது தமிழ்நாட்டிற்கு தவறானது.",
            "tip_en": "TN SEC tenure: 2 years initially, re-eligible up to maximum age of 65 years.",
            "tip_ta": "TN SEC பதவிக்காலம்: தொடக்கத்தில் 2 ஆண்டுகள், அதிகபட்சமாக 65 வயது வரை மறுநியமனம் பெற தகுதி.",
            "fact_en": "Maximum age limit for holding the post of TN SEC is 65 years.",
            "fact_ta": "TN SEC பதவியை வகிப்பதற்கான அதிகபட்ச வயது வரம்பு 65 ஆண்டுகள் ஆகும்."
        },

        # 13
        {
            "subtopic": "State Election Commission - Constitutional Mandate & Provisions (Articles 243K & 243ZA)",
            "stem_en": "[TNPSC Group 1 2015, Group 2 2018]\nIn which landmark judgment did the Supreme Court hold that the powers of the State Election Commission are on par with the Election Commission of India?",
            "stem_ta": "[TNPSC குரூப் 1 2015, குரூப் 2 2018]\nமாநில தேர்தல் ஆணையத்தின் அதிகாரங்கள் இந்திய தேர்தல் ஆணையத்திற்கு இணையானவை என்று உச்ச நீதிமன்றம் எந்த வரலாற்று சிறப்புமிக்க தீர்ப்பில் கூறியது?",
            "options": [
                ("Kishan Singh Tomar v. Municipal Corporation of Ahmedabad (2006)", "கிஷன் சிங் தோமர் எதிர் அகமதாபாத் மாநகராட்சி (2006)"),
                ("Indra Sawhney v. Union of India (1992)", "இந்திரா சாஹ்னி எதிர் இந்திய அரசு (1992)"),
                ("Kesavananda Bharati v. State of Kerala (1973)", "கேசவானந்த பாரதி எதிர் கேரள அரசு (1973)"),
                ("Minerva Mills v. Union of India (1980)", "மினர்வா மில்ஸ் எதிர் இந்திய அரசு (1980)")
            ],
            "correct_key": "A",
            "exp_en": "In Kishan Singh Tomar (2006), a Constitution Bench of the Supreme Court held that the powers and status of the State Election Commission under Articles 243K and 243ZA are on par with those of the Election Commission of India under Article 324.",
            "exp_ta": "கிஷன் சிங் தோமர் (2006) வழக்கில், சரத்துகள் 243K மற்றும் 243ZA-ன் கீழ் மாநில தேர்தல் ஆணையத்தின் அதிகாரங்கள் மற்றும் அந்தஸ்து சரத்து 324-ன் கீழ் இந்திய தேர்தல் ஆணையத்திற்கு இணையானவை என்று உச்ச நீதிமன்ற அரசியலமைப்பு அமர்வு தீர்ப்பளித்தது.",
            "why_a_en": "Kishan Singh Tomar (2006) is the landmark authority on SEC parity with ECI.",
            "why_a_ta": "கிஷன் சிங் தோமர் (2006) ECI-யுடன் SEC சமத்துவத்தை நிறுவிய முக்கிய தீர்ப்பாகும்.",
            "why_b_en": "Indra Sawhney relates to OBC reservation and the 50% ceiling.",
            "why_b_ta": "இந்திரா சாஹ்னி OBC இடஒதுக்கீடு மற்றும் 50% உச்சவரம்பு பற்றியது.",
            "why_c_en": "Kesavananda Bharati established the Basic Structure doctrine.",
            "why_c_ta": "கேசவானந்த பாரதி அடிப்படை கட்டமைப்பு கோட்பாட்டை நிறுவியது.",
            "why_d_en": "Minerva Mills reinforced judicial review and balance between Fundamental Rights and DPSPs.",
            "why_d_ta": "மினர்வா மில்ஸ் நீதித்துறை மறுஆய்வு மற்றும் அடிப்படை உரிமைகள் - வழிகாட்டு நெறிமுறைகள் சமநிலையை வலியுறுத்தியது.",
            "tip_en": "Kishan Singh Tomar = SEC has plenary powers identical to ECI under Article 324.",
            "tip_ta": "கிஷன் சிங் தோமர் = சரத்து 324-ன் கீழ் ECI-க்கு உள்ள அதே முழு அதிகாரங்கள் SEC-க்கும் உண்டு.",
            "fact_en": "The Court ruled that the State Government must act in aid of the SEC during local elections.",
            "fact_ta": "உள்ளாட்சித் தேர்தலின் போது மாநில அரசு SEC-க்கு துணையாகச் செயல்பட வேண்டும் என்று நீதிமன்றம் தீர்ப்பளித்தது."
        },

        # 14
        {
            "subtopic": "Financial Devolution, Intergovernmental Transfers & Local Governance",
            "stem_en": "[TNPSC Group 2 2015, Group 4 2019]\nWhat is the primary source of 'Own Tax Revenue' for Municipal Corporations and Municipalities in Tamil Nadu?",
            "stem_ta": "[TNPSC குரூப் 2 2015, குரூப் 4 2019]\nதமிழ்நாட்டில் மாநகராட்சிகள் மற்றும் நகராட்சிகளுக்கு 'சொந்த வரி வருவாயின்' முதன்மை ஆதாரம் எது?",
            "options": [
                ("Property Tax", "சொத்து வரி"),
                ("Agricultural Income Tax", "விவசாய வருமான வரி"),
                ("Corporation Income Tax", "நிறுவன வருமான வரி (Corporation Tax)"),
                ("Customs Duty", "சுங்க வரி")
            ],
            "correct_key": "A",
            "exp_en": "Property tax on lands and buildings is the bedrock and single largest component of own tax revenue for urban local bodies across Tamil Nadu.",
            "exp_ta": "நிலங்கள் மற்றும் கட்டிடங்கள் மீதான சொத்து வரி தமிழ்நாடு முழுவதும் உள்ள நகர்ப்புற உள்ளாட்சி அமைப்புகளின் சொந்த வரி வருவாயின் மிகப்பெரிய அங்கமாகும்.",
            "why_a_en": "Property tax is the principal own tax revenue for urban local bodies.",
            "why_a_ta": "சொத்து வரி நகர்ப்புற உள்ளாட்சி அமைப்புகளின் முதன்மை சொந்த வரி வருவாயாகும்.",
            "why_b_en": "Agricultural income tax is levied by the state on plantations, not by municipalities.",
            "why_b_ta": "விவசாய வருமான வரி மாநில அரசால் தோட்டங்களின் மீது விதிக்கப்படுகிறது, நகராட்சிகளால் அல்ல.",
            "why_c_en": "Corporation Tax is a Union tax levied by Parliament under Entry 85 of List I.",
            "why_c_ta": "கார்ப்பரேஷன் வரி என்பது பட்டியல் I-ன் பதிவு 85-ன் கீழ் நாடாளுமன்றத்தால் விதிக்கப்படும் மத்திய வரியாகும்.",
            "why_d_en": "Customs duty is an exclusive Union subject.",
            "why_d_ta": "சுங்க வரி என்பது பிரத்யேக மத்திய பாடமாகும்.",
            "tip_en": "Property Tax + Professional Tax + Water Charges = Core municipal own revenue.",
            "tip_ta": "சொத்து வரி + தொழில் வரி + குடிநீர்க் கட்டணம் = முக்கிய நகராட்சி சொந்த வருவாய்.",
            "fact_en": "Property tax revision in Tamil Nadu is governed by statutory municipal rules.",
            "fact_ta": "தமிழ்நாட்டில் சொத்து வரி திருத்தம் சட்டப்பூர்வ நகராட்சி விதிகளால் நிர்வகிக்கப்படுகிறது."
        },

        # 15
        {
            "subtopic": "Tamil Nadu State Election & Finance Commissions - Legal Framework, Rules & Precedents",
            "stem_en": "[TNPSC Group 1 2022]\nIn Tamil Nadu, which of the following local body positions is filled through an INDIRECT election?",
            "stem_ta": "[TNPSC குரூப் 1 2022]\nதமிழ்நாட்டில் பின்வரும் உள்ளாட்சிப் பதவிகளில் எது மறைமுகத் தேர்தல் மூலம் நிரப்பப்படுகிறது?",
            "options": [
                ("Panchayat Union Chairman", "பஞ்சாயத்து ஒன்றியத் தலைவர்"),
                ("Village Panchayat President", "கிராம பஞ்சாயத்து தலைவர்"),
                ("Village Panchayat Ward Member", "கிராம பஞ்சாயத்து வார்டு உறுப்பினர்"),
                ("Panchayat Union Ward Member", "பஞ்சாயத்து ஒன்றிய வார்டு உறுப்பினர்")
            ],
            "correct_key": "A",
            "exp_en": "In Tamil Nadu, the Panchayat Union Chairman is elected indirectly by and from among the elected Panchayat Union Ward Members (Councillors). Village Panchayat Presidents and Ward Members are directly elected.",
            "exp_ta": "தமிழ்நாட்டில், பஞ்சாயத்து ஒன்றியத் தலைவர் தேர்ந்தெடுக்கப்பட்ட பஞ்சாயத்து ஒன்றிய வார்டு உறுப்பினர்களிடையே (கவுன்சிலர்கள்) இருந்து மறைமுகமாகத் தேர்ந்தெடுக்கப்படுகிறார். கிராம பஞ்சாயத்து தலைவர்கள் மற்றும் வார்டு உறுப்பினர்கள் நேரடியாக தேர்ந்தெடுக்கப்படுகிறார்கள்.",
            "why_a_en": "Panchayat Union Chairman is elected through indirect election by councillors.",
            "why_a_ta": "பஞ்சாயத்து ஒன்றியத் தலைவர் கவுன்சிலர்களால் மறைமுகத் தேர்தல் மூலம் தேர்ந்தெடுக்கப்படுகிறார்.",
            "why_b_en": "Village Panchayat President is directly elected by registered voters.",
            "why_b_ta": "கிராம பஞ்சாயத்து தலைவர் பதிவு செய்யப்பட்ட வாக்காளர்களால் நேரடியாக தேர்ந்தெடுக்கப்படுகிறார்.",
            "why_c_en": "Village Panchayat Ward Member is directly elected by ward voters.",
            "why_c_ta": "கிராம பஞ்சாயத்து வார்டு உறுப்பினர் வார்டு வாக்காளர்களால் நேரடியாக தேர்ந்தெடுக்கப்படுகிறார்.",
            "why_d_en": "Panchayat Union Ward Member is directly elected by voters of that union ward.",
            "why_d_ta": "ஒன்றிய வார்டு உறுப்பினர் அந்த வார்டு வாக்காளர்களால் நேரடியாக தேர்ந்தெடுக்கப்படுகிறார்.",
            "tip_en": "TN: Direct = Village President & all Ward Councillors. Indirect = Union Chairman, District Chairman, Mayor, Municipal Chairman.",
            "tip_ta": "TN: நேரடி = கிராம தலைவர் & அனைத்து வார்டு கவுன்சிலர்கள். மறைமுக = ஒன்றிய தலைவர், மாவட்ட தலைவர், மேயர், நகராட்சி தலைவர்.",
            "fact_en": "District Panchayat Chairman is also elected indirectly by District Panchayat Ward Members.",
            "fact_ta": "மாவட்ட பஞ்சாயத்து தலைவரும் மாவட்ட பஞ்சாயத்து வார்டு உறுப்பினர்களால் மறைமுகமாகத் தேர்ந்தெடுக்கப்படுகிறார்."
        },

        # 16
        {
            "subtopic": "State Election Commission - Constitutional Mandate & Provisions (Articles 243K & 243ZA)",
            "stem_en": "[TNPSC Group 4 2018, Group 2 2019]\nAccording to Article 243-E and Article 243-U, what is the normal constitutional duration of Panchayats and Municipalities?",
            "stem_ta": "[TNPSC குரூப் 4 2018, குரூப் 2 2019]\nசரத்துகள் 243-E மற்றும் 243-U-ன் படி, பஞ்சாயத்துகள் மற்றும் நகராட்சிகளின் வழக்கமான அரசியலமைப்பு கால அளவு என்ன?",
            "options": [
                ("5 years from the date appointed for its first meeting", "அதன் முதல் கூட்டத்திற்காக நிர்ணயிக்கப்பட்ட தேதியிலிருந்து 5 ஆண்டுகள்"),
                ("6 years from the date of election notification", "தேர்தல் அறிவிப்பு தேதியிலிருந்து 6 ஆண்டுகள்"),
                ("3 years from the date of oath taking", "பதவியேற்பு தேதியிலிருந்து 3 ஆண்டுகள்"),
                ("4 years renewable once by the Governor", "ஆளுநரால் ஒருமுறை புதுப்பிக்கத்தக்க 4 ஆண்டுகள்")
            ],
            "correct_key": "A",
            "exp_en": "Articles 243-E(1) and 243-U(1) state that every Panchayat and Municipality shall continue for five years from the date appointed for its first meeting and no longer.",
            "exp_ta": "சரத்துகள் 243-E(1) மற்றும் 243-U(1) ஒவ்வொரு பஞ்சாயத்தும் நகராட்சியும் அதன் முதல் கூட்டத்திற்காக நிர்ணயிக்கப்பட்ட தேதியிலிருந்து ஐந்து ஆண்டுகள் மட்டுமே நீடிக்கும் என்று கூறுகின்றன.",
            "why_a_en": "5 years from first meeting is the exact constitutional duration.",
            "why_a_ta": "முதல் கூட்டத்திலிருந்து 5 ஆண்டுகள் என்பது சரியான அரசியலமைப்பு கால அளவாகும்.",
            "why_b_en": "6 years is incorrect.",
            "why_b_ta": "6 ஆண்டுகள் என்பது தவறானது.",
            "why_c_en": "3 years is incorrect.",
            "why_c_ta": "3 ஆண்டுகள் என்பது தவறானது.",
            "why_d_en": "Duration cannot be extended arbitrarily by the Governor.",
            "why_d_ta": "ஆளுநரால் கால அளவை தன்னிச்சையாக நீட்டிக்க முடியாது.",
            "tip_en": "Duration starts from the date of FIRST MEETING, not election result date.",
            "tip_ta": "கால அளவு தேர்தல் முடிவு தேதியிலிருந்து அல்ல, முதல் கூட்டத்தின் தேதியிலிருந்து தொடங்குகிறது.",
            "fact_en": "An election to reconstitute must be completed before the 5-year duration expires.",
            "fact_ta": "5 ஆண்டு காலம் முடிவதற்குள் மீண்டும் அமைப்பதற்கான தேர்தல் முடிக்கப்பட வேண்டும்."
        },

        # 17
        {
            "subtopic": "State Finance Commission - Constitutional Mandate, Composition & Role (Articles 243I & 243Y)",
            "stem_en": "[TNPSC Group 1 2017, Group 2A 2018]\nWhich Article of the Constitution requires the State Finance Commission's recommendations to be laid before the State Legislature?",
            "stem_ta": "[TNPSC குரூப் 1 2017, குரூப் 2A 2018]\nமாநில நிதி ஆணையத்தின் பரிந்துரைகளை மாநில சட்டமன்றத்தின் முன் வைக்க வேண்டும் என்று கோரும் அரசியலமைப்பு சரத்து எது?",
            "options": [
                ("Article 243-I(4)", "சரத்து 243-I(4)"),
                ("Article 243-I(1)", "சரத்து 243-I(1)"),
                ("Article 243K(2)", "சரத்து 243K(2)"),
                ("Article 281", "சரத்து 281")
            ],
            "correct_key": "A",
            "exp_en": "Article 243-I(4) mandates that the Governor shall cause every recommendation made by the Commission together with an explanatory memorandum as to action taken to be laid before the Legislature of the State.",
            "exp_ta": "சரத்து 243-I(4) ஆணையம் அளித்த ஒவ்வொரு பரிந்துரையையும் அதன் மீது எடுக்கப்பட்ட நடவடிக்கை குறித்த விளக்கக் குறிப்புடன் மாநில சட்டமன்றத்தின் முன் ஆளுநர் வைக்கச் செய்ய வேண்டும் என்று கட்டாயப்படுத்துகிறது.",
            "why_a_en": "Article 243-I(4) specifically governs the tabling of the SFC report before the Legislature.",
            "why_a_ta": "சரத்து 243-I(4) சட்டமன்றத்தில் SFC அறிக்கையை சமர்ப்பிப்பதை குறிப்பாக நிர்வகிக்கிறது.",
            "why_b_en": "Article 243-I(1) deals with the constitution of the SFC by the Governor.",
            "why_b_ta": "சரத்து 243-I(1) ஆளுநரால் SFC அமைக்கப்படுவதைக் கையாள்கிறது.",
            "why_c_en": "Article 243K(2) deals with tenure and conditions of service of the SEC.",
            "why_c_ta": "சரத்து 243K(2) SEC-ன் பதவிக்காலம் மற்றும் பணி நிபந்தனைகளைக் கையாள்கிறது.",
            "why_d_en": "Article 281 deals with tabling the Central Finance Commission report in Parliament.",
            "why_d_ta": "சரத்து 281 நாடாளுமன்றத்தில் மத்திய நிதி ஆணைய அறிக்கையை வைப்பதைக் கையாள்கிறது.",
            "tip_en": "Article 281 = Central FC laid before Parliament. Article 243-I(4) = State FC laid before State Assembly.",
            "tip_ta": "சரத்து 281 = நாடாளுமன்றத்தில் மத்திய FC. சரத்து 243-I(4) = சட்டமன்றத்தில் மாநில FC.",
            "fact_en": "Tabling includes the Action Taken Report (ATR) explaining acceptance or reasons for non-acceptance.",
            "fact_ta": "சமர்ப்பிப்பில் ஏற்பு அல்லது ஏற்காததற்கான காரணங்களை விளக்கும் நடவடிக்கை அறிக்கை (ATR) அடங்கும்."
        },

        # 18
        {
            "subtopic": "State Election Commissioner - Appointment, Tenure, Removal & Autonomy",
            "stem_en": "[TNPSC Assistant Director of Panchayats 2019]\nWho determines the conditions of service and tenure of office of the State Election Commissioner?",
            "stem_ta": "[TNPSC உதவி பஞ்சாயத்து இயக்குநர் 2019]\nமாநில தேர்தல் ஆணையரின் பணி நிபந்தனைகள் மற்றும் பதவிக்காலத்தை தீர்மானிப்பவர் யார்?",
            "options": [
                ("The Governor, subject to the provisions of any law made by the State Legislature", "மாநில சட்டமன்றம் இயற்றும் எந்தவொரு சட்டத்தின் விதிகளுக்கு உட்பட்டு, ஆளுநர்"),
                ("The President of India on the advice of the Union Cabinet", "மத்திய அமைச்சரவையின் ஆலோசனையின் பேரில் இந்திய குடியரசுத் தலைவர்"),
                ("The Chief Justice of the High Court in consultation with the Bar Council", "பார் கவுன்சிலுடன் கலந்தாலோசித்து உயர் நீதிமன்ற தலைமை நீதிபதி"),
                ("The Chairman of the Union Public Service Commission", "மத்திய அரசுப் பணியாளர் தேர்வாணையத்தின் தலைவர்")
            ],
            "correct_key": "A",
            "exp_en": "Under Article 243K(2), subject to the provisions of any law made by the Legislature of the State, the conditions of service and tenure of office of the State Election Commissioner shall be such as the Governor may by rule determine.",
            "exp_ta": "சரத்து 243K(2)-ன் கீழ், மாநில சட்டமன்றம் இயற்றும் சட்டத்தின் விதிகளுக்கு உட்பட்டு, மாநில தேர்தல் ஆணையரின் பணி நிபந்தனைகள் மற்றும் பதவிக்காலம் ஆளுநர் விதி மூலம் தீர்மானிப்பதாக இருக்கும்.",
            "why_a_en": "Article 243K(2) vests this power in the Governor subject to state legislative enactment.",
            "why_a_ta": "சரத்து 243K(2) மாநில சட்டமன்ற சட்டத்திற்கு உட்பட்டு இந்த அதிகாரத்தை ஆளுநரிடம் வழங்குகிறது.",
            "why_b_en": "The President has no role in determining SEC service conditions.",
            "why_b_ta": "SEC பணி நிபந்தனைகளைத் தீர்மானிப்பதில் குடியரசுத் தலைவருக்கு எந்த பங்கும் இல்லை.",
            "why_c_en": "The Chief Justice does not frame administrative service conditions for the SEC.",
            "why_c_ta": "தலைமை நீதிபதி SEC-க்கான பணி நிபந்தனைகளை உருவாக்குவதில்லை.",
            "why_d_en": "UPSC Chairman has no authority over state election commissioners.",
            "why_d_ta": "UPSC தலைவருக்கு மாநில தேர்தல் ஆணையர்கள் மீது எந்த அதிகாரமும் இல்லை.",
            "tip_en": "Governor determines conditions by rule, but cannot vary them to disadvantage after appointment.",
            "tip_ta": "ஆளுநர் விதி மூலம் தீர்மானிக்கிறார், ஆனால் நியமனத்திற்குப் பின் பாதகமாக மாற்ற முடியாது.",
            "fact_en": "Tamil Nadu framed the Tamil Nadu State Election Commissioner Conditions of Service Rules in 1994.",
            "fact_ta": "தமிழ்நாடு 1994-ல் தமிழ்நாடு மாநில தேர்தல் ஆணையர் பணி நிபந்தனைகள் விதிகளை உருவாக்கியது."
        },

        # 19
        {
            "subtopic": "Tamil Nadu State Election & Finance Commissions - Legal Framework, Rules & Precedents",
            "stem_en": "[TNPSC Group 4 2019, Group 2 2022]\nWhat percentage of seats in local bodies is reserved for women in Tamil Nadu under the amended Panchayat and Municipal laws?",
            "stem_ta": "[TNPSC குரூப் 4 2019, குரூப் 2 2022]\nதிருத்தப்பட்ட பஞ்சாயத்து மற்றும் நகராட்சி சட்டங்களின் கீழ் தமிழ்நாட்டில் உள்ளாட்சி அமைப்புகளில் பெண்களுக்கு எத்தனை சதவீத இடங்கள் ஒதுக்கப்பட்டுள்ளன?",
            "options": [
                ("50%", "50%"),
                ("33%", "33%"),
                ("25%", "25%"),
                ("69%", "69%")
            ],
            "correct_key": "A",
            "exp_en": "In 2016, Tamil Nadu passed amendments to the Tamil Nadu Panchayats Act 1994 and Tamil Nadu Municipal Laws enhancing the reservation for women in local bodies from 33% to 50%.",
            "exp_ta": "2016-ல் தமிழ்நாடு உள்ளாட்சி அமைப்புகளில் பெண்களுக்கான இடஒதுக்கீட்டை 33%-லிருந்து 50%-ஆக உயர்த்தி தமிழ்நாடு பஞ்சாயத்துகள் சட்டம் 1994 மற்றும் நகராட்சி சட்டங்களில் திருத்தங்களை நிறைவேற்றியது.",
            "why_a_en": "50% is the current statutory quota for women in Tamil Nadu local bodies.",
            "why_a_ta": "50% என்பது தமிழ்நாட்டில் உள்ளாட்சி அமைப்புகளில் பெண்களுக்கான தற்போதைய சட்டப்பூர்வ ஒதுக்கீடாகும்.",
            "why_b_en": "33% was the original constitutional minimum under Article 243D(3), enhanced in 2016.",
            "why_b_ta": "33% என்பது சரத்து 243D(3)-ன் கீழ் அசல் அரசியலமைப்பு குறைந்தபட்ச ஒதுக்கீடாகும், இது 2016-ல் உயர்த்தப்பட்டது.",
            "why_c_en": "25% is incorrect.",
            "why_c_ta": "25% என்பது தவறானது.",
            "why_d_en": "69% is the total reservation for backward classes in state educational/employment quotas in TN.",
            "why_d_ta": "69% என்பது தமிழ்நாட்டில் கல்வி/வேலைவாய்ப்பில் பின்தங்கிய வகுப்பினருக்கான மொத்த இடஒதுக்கீடாகும்.",
            "tip_en": "Constitutional minimum under 243D = not less than 1/3rd (33%). TN provided 50% in 2016.",
            "tip_ta": "243D-ன் கீழ் அரசியலமைப்பு குறைந்தபட்சம் = மூன்றில் ஒரு பங்கு (33%). தமிழ்நாடு 2016-ல் 50% வழங்கியது.",
            "fact_en": "The 50% reservation applies to ward seats as well as chairperson/mayor posts.",
            "fact_ta": "50% இடஒதுக்கீடு வார்டு இடங்கள் மற்றும் தலைவர்/மேயர் பதவிகளுக்கும் பொருந்தும்."
        },

        # 20
        {
            "subtopic": "Financial Devolution, Intergovernmental Transfers & Local Governance",
            "stem_en": "[TNPSC Group 1 2019, Group 2 2021]\nWhat is the approximate percentage of State's Own Tax Revenue (SOTR) traditionally recommended as vertical devolution to local bodies by State Finance Commissions in Tamil Nadu?",
            "stem_ta": "[TNPSC குரூப் 1 2019, குரூப் 2 2021]\nதமிழ்நாட்டில் உள்ள மாநில நிதி ஆணையங்களால் உள்ளாட்சி அமைப்புகளுக்கு செங்குத்துப் பகிர்வாக பாரம்பரியமாக பரிந்துரைக்கப்படும் மாநில சொந்த வரி வருவாயின் (SOTR) தோராயமான சதவீதம் என்ன?",
            "options": [
                ("10%", "10%"),
                ("25%", "25%"),
                ("5%", "5%"),
                ("50%", "50%")
            ],
            "correct_key": "A",
            "exp_en": "Successive SFCs in Tamil Nadu (Fourth, Fifth, and Sixth SFCs) have recommended devolving roughly 10% of the net State's Own Tax Revenue (SOTR) to rural and urban local bodies.",
            "exp_ta": "தமிழ்நாட்டின் அடுத்தடுத்த SFC-கள் (நான்காவது, ஐந்தாவது மற்றும் ஆறாவது) நிகர மாநில சொந்த வரி வருவாயில் (SOTR) சுமார் 10%-ஐ ஊரக மற்றும் நகர்ப்புற உள்ளாட்சி அமைப்புகளுக்கு பகிர்ந்தளிக்க பரிந்துரைத்துள்ளன.",
            "why_a_en": "10% of SOTR is the benchmark vertical devolution rate in Tamil Nadu.",
            "why_a_ta": "SOTR-ல் 10% என்பது தமிழ்நாட்டில் நிலையான செங்குத்துப் பகிர்வு விகிதமாகும்.",
            "why_b_en": "25% is excessively high and never adopted.",
            "why_b_ta": "25% என்பது மிக அதிகமானது மற்றும் ஒருபோதும் ஏற்றுக்கொள்ளப்படவில்லை.",
            "why_c_en": "5% was the initial rate in the First SFC before being progressively raised.",
            "why_c_ta": "5% என்பது முதல் SFC-ல் ஆரம்ப விகிதமாக இருந்தது, பின்னர் படிப்படியாக உயர்த்தப்பட்டது.",
            "why_d_en": "50% is incorrect.",
            "why_d_ta": "50% என்பது தவறானது.",
            "tip_en": "Vertical devolution in TN = 10% of net SOTR. Horizontal split = 56% (Rural) : 44% (Urban).",
            "tip_ta": "TN-ல் செங்குத்துப் பகிர்வு = நிகர SOTR-ல் 10%. கிடைமட்டப் பகிர்வு = 56% (ஊரகம்) : 44% (நகர்ப்புறம்).",
            "fact_en": "The 10% divisible pool is distributed horizontally among Rural and Urban local bodies.",
            "fact_ta": "இந்த 10% பகிர்வுத் தொகுப்பு ஊரக மற்றும் நகர்ப்புற உள்ளாட்சி அமைப்புகளிடையே கிடைமட்டமாக விநியோகிக்கப்படுகிறது."
        },

        # 21
        {
            "subtopic": "State Election Commission - Constitutional Mandate & Provisions (Articles 243K & 243ZA)",
            "stem_en": "[TNPSC Statistical Inspector 2018]\nWhich Article of the Constitution bars courts from questioning the validity of any law relating to delimitation of constituencies or allotment of seats to local bodies?",
            "stem_ta": "[TNPSC புள்ளிவிவர ஆய்வாளர் 2018]\nதொகுதிகள் மறுவரையறை அல்லது உள்ளாட்சி அமைப்புகளுக்கு இடங்கள் ஒதுக்கீடு தொடர்பான எந்தவொரு சட்டத்தின் செல்லுபடியாகும் தன்மையையும் நீதிமன்றங்கள் கேள்வி கேட்பதை தடை செய்யும் அரசியலமைப்பு சரத்து எது?",
            "options": [
                ("Article 243-O(a)", "சரத்து 243-O(a)"),
                ("Article 243-O(b)", "சரத்து 243-O(b)"),
                ("Article 243K(3)", "சரத்து 243K(3)"),
                ("Article 243D(4)", "சரத்து 243D(4)")
            ],
            "correct_key": "A",
            "exp_en": "Article 243-O(a) bars the interference of courts in laws relating to the delimitation of constituencies or the allotment of seats to such constituencies under Article 243K.",
            "exp_ta": "சரத்து 243-O(a) சரத்து 243K-ன் கீழ் தொகுதிகள் மறுவரையறை அல்லது இடங்கள் ஒதுக்கீடு தொடர்பான சட்டங்களில் நீதிமன்றங்கள் தலையிடுவதைத் தடை செய்கிறது.",
            "why_a_en": "Article 243-O(a) explicitly immunizes delimitation laws from court challenges.",
            "why_a_ta": "சரத்து 243-O(a) மறுவரையறை சட்டங்களை நீதிமன்ற சவால்களிலிருந்து பாதுகாக்கிறது.",
            "why_b_en": "Article 243-O(b) mandates that elections can only be questioned via election petitions.",
            "why_b_ta": "சரத்து 243-O(b) தேர்தல் மனு மூலமாக மட்டுமே தேர்தலை எதிர்க்க முடியும் எனக் கூறுகிறது.",
            "why_c_en": "Article 243K(3) requires the Governor to provide staff to the SEC.",
            "why_c_ta": "சரத்து 243K(3) ஆளுநர் SEC-க்கு பணியாளர்களை வழங்க வேண்டும் எனக் கூறுகிறது.",
            "why_d_en": "Article 243D(4) provides for reservation of offices of Chairpersons in Panchayats.",
            "why_d_ta": "சரத்து 243D(4) பஞ்சாயத்துகளில் தலைவர் பதவிகளுக்கான இடஒதுக்கீட்டை வழங்குகிறது.",
            "tip_en": "243-O(a) = Delimitation immunity. 243-O(b) = Election petition requirement.",
            "tip_ta": "243-O(a) = மறுவரையறை பாதுகாப்பு. 243-O(b) = தேர்தல் மனு தேவை.",
            "fact_en": "Article 243ZG(a) provides an identical delimitation bar for municipal constituencies.",
            "fact_ta": "சரத்து 243ZG(a) நகராட்சித் தொகுதிகளுக்கு இதேபோன்ற மறுவரையறைத் தடையை வழங்குகிறது."
        },

        # 22
        {
            "subtopic": "State Finance Commission - Constitutional Mandate, Composition & Role (Articles 243I & 243Y)",
            "stem_en": "[TNPSC Group 2 2013, Group 4 2016]\nWhich Article of the Constitution requires the State Finance Commission to review the financial position of Municipalities?",
            "stem_ta": "[TNPSC குரூப் 2 2013, குரூப் 4 2016]\nநகராட்சிகளின் நிதி நிலையை மறுஆய்வு செய்ய மாநில நிதி ஆணையத்திற்கு கட்டளையிடும் அரசியலமைப்பு சரத்து எது?",
            "options": [
                ("Article 243Y", "சரத்து 243Y"),
                ("Article 243-I", "சரத்து 243-I"),
                ("Article 243X", "சரத்து 243X"),
                ("Article 243Z", "சரத்து 243Z")
            ],
            "correct_key": "A",
            "exp_en": "Article 243Y mandates that the Finance Commission constituted under Article 243-I shall also review the financial position of the Municipalities and make recommendations to the Governor.",
            "exp_ta": "சரத்து 243-I-ன் கீழ் அமைக்கப்பட்ட நிதி ஆணையம் நகராட்சிகளின் நிதி நிலையையும் மறுஆய்வு செய்து ஆளுநருக்கு பரிந்துரைகளை வழங்க வேண்டும் என்று சரத்து 243Y கட்டாயப்படுத்துகிறது.",
            "why_a_en": "Article 243Y specifically extends the SFC's remit to Municipalities.",
            "why_a_ta": "சரத்து 243Y SFC-ன் அதிகார வரம்பை குறிப்பாக நகராட்சிகளுக்கு விரிவுபடுத்துகிறது.",
            "why_b_en": "Article 243-I governs the constitution of the SFC for Panchayats.",
            "why_b_ta": "சரத்து 243-I பஞ்சாயத்துகளுக்கான SFC அமைப்பை நிர்வகிக்கிறது.",
            "why_c_en": "Article 243X deals with the power to impose taxes by Municipalities.",
            "why_c_ta": "சரத்து 243X நகராட்சிகள் வரி விதிக்கும் அதிகாரத்தைக் கையாள்கிறது.",
            "why_d_en": "Article 243Z deals with audit of accounts of Municipalities.",
            "why_d_ta": "சரத்து 243Z நகராட்சிகளின் கணக்குகள் தணிக்கையைக் கையாள்கிறது.",
            "tip_en": "243-I = Finance Commission for Panchayats. 243Y = Same Finance Commission for Municipalities.",
            "tip_ta": "243-I = பஞ்சாயத்துகளுக்கான நிதி ஆணையம். 243Y = நகராட்சிகளுக்கான அதே நிதி ஆணையம்.",
            "fact_en": "India does not have separate municipal and panchayat finance commissions; one commission covers both.",
            "fact_ta": "இந்தியாவில் தனித்தனி நகராட்சி மற்றும் பஞ்சாயத்து நிதி ஆணையங்கள் இல்லை; ஒரு ஆணையமே இரண்டையும் உள்ளடக்கியது."
        },

        # 23
        {
            "subtopic": "State Election Commissioner - Appointment, Tenure, Removal & Autonomy",
            "stem_en": "[TNPSC Group 1 2018]\nUnder Article 243K(3), whose duty is it to make available to the State Election Commissioner the staff necessary for conducting local body elections?",
            "stem_ta": "[TNPSC குரூப் 1 2018]\nசரத்து 243K(3)-ன் கீழ், உள்ளாட்சித் தேர்தல்களை நடத்துவதற்குத் தேவையான பணியாளர்களை மாநில தேர்தல் ஆணையருக்கு கிடைக்கச் செய்வது யாருடைய கடமையாகும்?",
            "options": [
                ("The Governor of the State", "மாநில ஆளுநர்"),
                ("The Chief Justice of the High Court", "உயர் நீதிமன்ற தலைமை நீதிபதி"),
                ("The President of India", "இந்திய குடியரசுத் தலைவர்"),
                ("The Chief Election Commissioner of India", "இந்திய தலைமை தேர்தல் ஆணையர்")
            ],
            "correct_key": "A",
            "exp_en": "Article 243K(3) states that the Governor of a State shall, when so requested by the State Election Commissioner, make available to the Commission such staff as may be necessary for the discharge of its functions.",
            "exp_ta": "சரத்து 243K(3) மாநில தேர்தல் ஆணையர் கோரும் போது, அதன் பணிகளைச் செய்வதற்குத் தேவையான பணியாளர்களை ஆணையத்திற்கு மாநில ஆளுநர் கிடைக்கச் செய்ய வேண்டும் என்று கூறுகிறது.",
            "why_a_en": "The Governor is constitutionally tasked with making staff available upon request.",
            "why_a_ta": "கோரிக்கையின் பேரில் பணியாளர்களை கிடைக்கச் செய்ய அரசியலமைப்பு ரீதியாக ஆளுநரே பணிக்கப்பட்டுள்ளார்.",
            "why_b_en": "The Chief Justice has no staff requisition duties for elections.",
            "why_b_ta": "தலைமை நீதிபதிக்கு தேர்தல் பணியாளர்களை வழங்கும் கடமைகள் இல்லை.",
            "why_c_en": "The President provides staff to the Central ECI under Article 324(6), not the SEC.",
            "why_c_ta": "குடியரசுத் தலைவர் சரத்து 324(6)-ன் கீழ் மத்திய ECI-க்கு பணியாளர்களை வழங்குகிறார், SEC-க்கு அல்ல.",
            "why_d_en": "The Chief Election Commissioner does not control state administrative staff allocations.",
            "why_d_ta": "தலைமை தேர்தல் ஆணையர் மாநில நிர்வாகப் பணியாளர்கள் ஒதுக்கீட்டைக் கட்டுப்படுத்துவதில்லை.",
            "tip_en": "Article 324(6) = President/Governor provides staff to ECI. Article 243K(3) = Governor provides staff to SEC.",
            "tip_ta": "சரத்து 324(6) = ECI-க்கு குடியரசுத் தலைவர்/ஆளுநர் பணியாளர்களை வழங்குகிறார். சரத்து 243K(3) = SEC-க்கு ஆளுநர் பணியாளர்களை வழங்குகிறார்.",
            "fact_en": "Article 243ZA(2) mirrors this provision for municipal elections.",
            "fact_ta": "சரத்து 243ZA(2) நகராட்சித் தேர்தல்களுக்கு இந்த விதியைப் பிரதிபலிக்கிறது."
        },

        # 24
        {
            "subtopic": "Tamil Nadu State Election & Finance Commissions - Legal Framework, Rules & Precedents",
            "stem_en": "[TNPSC Junior Employment Officer 2017]\nUnder the Tamil Nadu Panchayats Act, 1994, which section provides for the constitution of the State Finance Commission?",
            "stem_ta": "[TNPSC இளநிலை வேலைவாய்ப்பு அலுவலர் 2017]\n1994 தமிழ்நாடு பஞ்சாயத்துகள் சட்டத்தின் கீழ், மாநில நிதி ஆணையத்தை அமைக்க வகை செய்யும் பிரிவு எது?",
            "options": [
                ("Section 240", "பிரிவு 240"),
                ("Section 239", "பிரிவு 239"),
                ("Section 241", "பிரிவு 241"),
                ("Section 242", "பிரிவு 242")
            ],
            "correct_key": "A",
            "exp_en": "Section 240 of the Tamil Nadu Panchayats Act, 1994 explicitly provides for the constitution of the Finance Commission to review the financial position of the Panchayats.",
            "exp_ta": "1994 தமிழ்நாடு பஞ்சாயத்துகள் சட்டத்தின் பிரிவு 240 பஞ்சாயத்துகளின் நிதி நிலையை மறுஆய்வு செய்வதற்கான நிதி ஆணையத்தை அமைக்க வெளிப்படையாக வகை செய்கிறது.",
            "why_a_en": "Section 240 governs the constitution of the State Finance Commission.",
            "why_a_ta": "பிரிவு 240 மாநில நிதி ஆணையத்தின் அமைப்பை நிர்வகிக்கிறது.",
            "why_b_en": "Section 239 governs the State Election Commission.",
            "why_b_ta": "பிரிவு 239 மாநில தேர்தல் ஆணையத்தை நிர்வகிக்கிறது.",
            "why_c_en": "Section 241 governs the powers of the State Finance Commission.",
            "why_c_ta": "பிரிவு 241 மாநில நிதி ஆணையத்தின் அதிகாரங்களை நிர்வகிக்கிறது.",
            "why_d_en": "Section 242 deals with other transitional matters.",
            "why_d_ta": "பிரிவு 242 இதர இடைக்கால விவகாரங்களைக் கையாள்கிறது.",
            "tip_en": "Sec 239 = SEC. Sec 240 = SFC. Sec 241 = SFC powers.",
            "tip_ta": "பிரிவு 239 = SEC. பிரிவு 240 = SFC. பிரிவு 241 = SFC அதிகாரங்கள்.",
            "fact_en": "The SFC under Section 240 consists of a Chairman and not more than four other members.",
            "fact_ta": "பிரிவு 240-ன் கீழான SFC ஒரு தலைவர் மற்றும் நான்கு உறுப்பினர்களுக்கு மிகாமல் கொண்டுள்ளது."
        },

        # 25
        {
            "subtopic": "Financial Devolution, Intergovernmental Transfers & Local Governance",
            "stem_en": "[TNPSC Group 4 2014, Group 2 2017]\nWhich Finance Commission recommended the establishment of a dedicated 'Panchayat Performance Grant' to reward local tax collection efficiency?",
            "stem_ta": "[TNPSC குரூப் 4 2014, குரூப் 2 2017]\nஉள்ளூர் வரி வசூல் திறனை ஊக்குவிக்க ஒரு பிரத்யேக 'பஞ்சாயத்து செயல்திறன் மானியத்தை' நிறுவ பரிந்துரைத்த மத்திய நிதி ஆணையம் எது?",
            "options": [
                ("13th Finance Commission", "13வது நிதி ஆணையம்"),
                ("10th Finance Commission", "10வது நிதி ஆணையம்"),
                ("11th Finance Commission", "11வது நிதி ஆணையம்"),
                ("12th Finance Commission", "12வது நிதி ஆணையம்")
            ],
            "correct_key": "A",
            "exp_en": "The 13th Finance Commission (chaired by Dr. Vijay Kelkar) introduced the landmark concept of Performance Grants linked to specific governance reforms and revenue mobilization for local bodies.",
            "exp_ta": "13வது நிதி ஆணையம் (டாக்டர் விஜய் கேல்கர் தலைமையில்) குறிப்பிட்ட நிர்வாக சீர்திருத்தங்கள் மற்றும் உள்ளாட்சி வருவாய் திரட்டலுடன் இணைக்கப்பட்ட செயல்திறன் மானியங்களின் முக்கிய கருத்தை அறிமுகப்படுத்தியது.",
            "why_a_en": "The 13th FC pioneered the structured performance grant framework.",
            "why_a_ta": "13வது FC கட்டமைக்கப்பட்ட செயல்திறன் மானிய கட்டமைப்பை முன்னோடியாக அறிமுகப்படுத்தியது.",
            "why_b_en": "10th FC made ad-hoc lump sum allocations without performance conditionality.",
            "why_b_ta": "10வது FC செயல்திறன் நிபந்தனைகள் இன்றி தற்காலிக மொத்த ஒதுக்கீடுகளை செய்தது.",
            "why_c_en": "11th FC provided basic untied local body grants.",
            "why_c_ta": "11வது FC அடிப்படை கட்டுப்பாடற்ற உள்ளாட்சி மானியங்களை வழங்கியது.",
            "why_d_en": "12th FC emphasized water supply and sanitation but did not introduce structured performance grants.",
            "why_d_ta": "12வது FC குடிநீர் மற்றும் சுகாதாரத்தை வலியுறுத்தியது, ஆனால் செயல்திறன் மானியங்களை அறிமுகப்படுத்தவில்லை.",
            "tip_en": "13th FC = First structured Performance Grants for local bodies.",
            "tip_ta": "13வது FC = உள்ளாட்சி அமைப்புகளுக்கான முதல் கட்டமைக்கப்பட்ட செயல்திறன் மானியங்கள்.",
            "fact_en": "This performance grant model was expanded further by the 14th and 15th Finance Commissions.",
            "fact_ta": "இந்த செயல்திறன் மானிய மாதிரி 14 மற்றும் 15வது நிதி ஆணையங்களால் மேலும் விரிவுபடுத்தப்பட்டது."
        },

        # 26
        {
            "subtopic": "State Election Commission - Constitutional Mandate & Provisions (Articles 243K & 243ZA)",
            "stem_en": "[TNPSC Group 1 2021]\nWhat constitutional protection is provided to the delimitation of constituencies under Article 243ZG for Municipalities?",
            "stem_ta": "[TNPSC குரூப் 1 2021]\nநகராட்சிகளுக்கான சரத்து 243ZG-ன் கீழ் தொகுதிகள் மறுவரையறைக்கு என்ன அரசியலமைப்பு பாதுகாப்பு வழங்கப்படுகிறது?",
            "options": [
                ("The validity of any delimitation law or allotment of seats cannot be called in question in any court", "எந்தவொரு மறுவரையறை சட்டம் அல்லது இடங்கள் ஒதுக்கீட்டின் செல்லுபடியாகும் தன்மையையும் எந்த நீதிமன்றத்திலும் கேள்வி கேட்க முடியாது"),
                ("Delimitation must be approved annually by the Supreme Court of India", "மறுவரையறை ஆண்டுதோறும் இந்திய உச்ச நீதிமன்றத்தால் அங்கீகரிக்கப்பட வேண்டும்"),
                ("Delimitation is purely advisory and municipal councils can ignore it at will", "மறுவரையறை வெறும் ஆலோசனை மட்டுமே மற்றும் நகராட்சி மன்றங்கள் அதை விருப்பப்படி புறக்கணிக்கலாம்"),
                ("Courts can cancel municipal delimitation at any time upon oral request", "வாய்மொழி கோரிக்கையின் பேரில் நீதிமன்றங்கள் எந்த நேரத்திலும் நகராட்சி மறுவரையறையை ரத்து செய்யலாம்")
            ],
            "correct_key": "A",
            "exp_en": "Article 243ZG(a) provides that the validity of any law relating to the delimitation of constituencies or the allotment of seats to such constituencies shall not be called in question in any court.",
            "exp_ta": "சரத்து 243ZG(a) தொகுதிகள் மறுவரையறை அல்லது அத்தகைய தொகுதிகளுக்கு இடங்கள் ஒதுக்கீடு தொடர்பான எந்தவொரு சட்டத்தின் செல்லுபடியாகும் தன்மையையும் எந்த நீதிமன்றத்திலும் கேள்வி கேட்க முடியாது என்று கூறுகிறது.",
            "why_a_en": "Article 243ZG(a) grants complete judicial immunity to delimitation laws.",
            "why_a_ta": "சரத்து 243ZG(a) மறுவரையறை சட்டங்களுக்கு முழுமையான நீதித்துறை பாதுகாப்பை வழங்குகிறது.",
            "why_b_en": "SC approval is not required for local delimitation.",
            "why_b_ta": "உள்ளூர் மறுவரையறைக்கு உச்ச நீதிமன்ற ஒப்புதல் தேவையில்லை.",
            "why_c_en": "Delimitation is binding and mandatory, not advisory.",
            "why_c_ta": "மறுவரையறை கட்டாயமானது, வெறும் ஆலோசனை அல்ல.",
            "why_d_en": "Courts cannot casually cancel delimitation on oral requests.",
            "why_d_ta": "வாய்மொழி கோரிக்கைகளின் பேரில் நீதிமன்றங்கள் மறுவரையறையை தன்னிச்சையாக ரத்து செய்ய முடியாது.",
            "tip_en": "243-O(a) (Panchayats) = 243ZG(a) (Municipalities): Delimitation laws cannot be questioned in court.",
            "tip_ta": "243-O(a) (பஞ்சாயத்துகள்) = 243ZG(a) (நகராட்சிகள்): மறுவரையறை சட்டங்களை நீதிமன்றத்தில் கேள்வி கேட்க முடியாது.",
            "fact_en": "This provision prevents unending judicial stays from derailing periodic elections.",
            "fact_ta": "இந்த விதி முடிவில்லாத நீதிமன்றத் தடைகள் குறிப்பிட்ட காலத் தேர்தல்களை சீர்குலைப்பதைத் தடுக்கிறது."
        },

        # 27
        {
            "subtopic": "State Finance Commission - Constitutional Mandate, Composition & Role (Articles 243I & 243Y)",
            "stem_en": "[TNPSC Group 2 2018, Group 4 2021]\nWhich among the following is NOT a subject on which the State Finance Commission makes recommendations under Article 243-I?",
            "stem_ta": "[TNPSC குரூப் 2 2018, குரூப் 4 2021]\nபின்வருவனவற்றில் எது சரத்து 243-I-ன் கீழ் மாநில நிதி ஆணையம் பரிந்துரைகளை வழங்கும் ஒரு விஷயம் அல்ல?",
            "options": [
                ("Devolution of Union Income Tax between the Union and the States", "மத்திய அரசுக்கும் மாநிலங்களுக்கும் இடையே மத்திய வருமான வரிப் பகிர்வு"),
                ("Distribution of net proceeds of State taxes between the State and Panchayats", "மாநில வரிகளின் நிகர வருவாயை மாநிலத்திற்கும் பஞ்சாயத்துகளுக்கும் இடையே பகிர்ந்தளித்தல்"),
                ("Determination of taxes, duties, and tolls which may be assigned to Panchayats", "பஞ்சாயத்துகளுக்கு ஒதுக்கப்படக்கூடிய வரிகள், தீர்வைகள் மற்றும் கட்டணங்களை தீர்மானித்தல்"),
                ("Grants-in-aid to Panchayats from the Consolidated Fund of the State", "மாநிலத்தின் தொகுப்பு நிதியிலிருந்து பஞ்சாயத்துகளுக்கு வழங்கப்படும் உதவி மானியங்கள்")
            ],
            "correct_key": "A",
            "exp_en": "Devolution of Union Income Tax between the Union and the States is the exclusive constitutional domain of the Central Finance Commission under Article 280(3)(a), not the State Finance Commission.",
            "exp_ta": "மத்திய அரசுக்கும் மாநிலங்களுக்கும் இடையே மத்திய வருமான வரியைப் பகிர்ந்தளிப்பது சரத்து 280(3)(a)-ன் கீழ் மத்திய நிதி ஆணையத்தின் பிரத்யேக அரசியலமைப்பு அதிகாரமாகும், மாநில நிதி ஆணையத்தினுடையது அல்ல.",
            "why_a_en": "Union tax devolution is handled exclusively by the Central Finance Commission under Article 280.",
            "why_a_ta": "மத்திய வரிப் பகிர்வு சரத்து 280-ன் கீழ் மத்திய நிதி ஆணையத்தால் மட்டுமே கையாளப்படுகிறது.",
            "why_b_en": "State-Panchayat tax distribution is a core function of the SFC under Article 243-I(1)(a)(i).",
            "why_b_ta": "மாநில-பஞ்சாயத்து வரிப் பகிர்வு சரத்து 243-I(1)(a)(i)-ன் கீழ் SFC-ன் முக்கிய பணியாகும்.",
            "why_c_en": "Tax assignment to Panchayats is a core SFC function under Article 243-I(1)(a)(ii).",
            "why_c_ta": "பஞ்சாயத்துகளுக்கு வரி ஒதுக்கீடு செய்வது சரத்து 243-I(1)(a)(ii)-ன் கீழ் SFC-ன் பணியாகும்.",
            "why_d_en": "Grants-in-aid from State Consolidated Fund is a core SFC function under Article 243-I(1)(a)(iii).",
            "why_d_ta": "மாநில தொகுப்பு நிதியிலிருந்து உதவி மானியம் வழங்குவது சரத்து 243-I(1)(a)(iii)-ன் கீழ் SFC-ன் பணியாகும்.",
            "tip_en": "Central FC = Union taxes sharing. State FC = State taxes sharing with local bodies.",
            "tip_ta": "மத்திய FC = மத்திய வரிகள் பகிர்வு. மாநில FC = உள்ளாட்சி அமைப்புகளுடன் மாநில வரிகள் பகிர்வு.",
            "fact_en": "Article 243-I covers state net proceeds, not union taxes.",
            "fact_ta": "சரத்து 243-I மாநில நிகர வருவாயை உள்ளடக்கியது, மத்திய வரிகளை அல்ல."
        },

        # 28
        {
            "subtopic": "State Election Commissioner - Appointment, Tenure, Removal & Autonomy",
            "stem_en": "[TNPSC Group 1 2019]\nWhat constitutional remedy did the Supreme Court affirm in State of AP v. N. Ramesh Kumar (2020) regarding arbitrary tenure curtailment of an SEC?",
            "stem_ta": "[TNPSC குரூப் 1 2019]\nஆந்திரப் பிரதேச அரசு எதிர் என். ரமேஷ் குமார் (2020) வழக்கில் SEC-ன் பதவிக்காலத்தை தன்னிச்சையாகக் குறைப்பது குறித்து உச்ச நீதிமன்றம் உறுதிப்படுத்திய அரசியலமைப்புத் தீர்வு என்ன?",
            "options": [
                ("The ordinance curtailing tenure was declared unconstitutional and the Commissioner was reinstated", "பதவிக்காலத்தைக் குறைத்த அவசரச் சட்டம் அரசியலமைப்பிற்கு முரணானது என அறிவிக்கப்பட்டு ஆணையர் மீண்டும் பணியமர்த்தப்பட்டார்"),
                ("The Governor was stripped of all constitutional powers permanently", "ஆளுநரின் அனைத்து அரசியலமைப்பு அதிகாரங்களும் நிரந்தரமாக பறிக்கப்பட்டன"),
                ("The State Election Commission was abolished and merged with the state police", "மாநில தேர்தல் ஆணையம் கலைக்கப்பட்டு மாநில காவல்துறையுடன் இணைக்கப்பட்டது"),
                ("The High Court bench was transferred to a foreign country", "உயர் நீதிமன்ற அமர்வு வெளிநாட்டிற்கு மாற்றப்பட்டது")
            ],
            "correct_key": "A",
            "exp_en": "The High Court and Supreme Court struck down the ordinance reducing tenure from 5 to 3 years as a colorable exercise of power violating the second proviso to Article 243K(2), and directed the reinstatement of Commissioner N. Ramesh Kumar.",
            "exp_ta": "உயர் நீதிமன்றமும் உச்ச நீதிமன்றமும் பதவிக்காலத்தை 5-லிருந்து 3 ஆண்டுகளாகக் குறைத்த அவசரச் சட்டத்தை சரத்து 243K(2)-ன் இரண்டாவது வரம்புரையை மீறும் சட்டவிரோத நடவடிக்கை என ரத்து செய்து, ஆணையர் என். ரமேஷ் குமாரை மீண்டும் பணியில் அமர்த்த உத்தரவிட்டது.",
            "why_a_en": "Reinstatement and invalidation of the ordinance was the direct judicial outcome.",
            "why_a_ta": "மீண்டும் பணியமர்த்துதல் மற்றும் அவசரச் சட்டத்தை ரத்து செய்தல் ஆகியவை நேரடி நீதித்துறை முடிவாகும்.",
            "why_b_en": "The Governor's office was not abolished.",
            "why_b_ta": "ஆளுநர் அலுவலகம் ஒழிக்கப்படவில்லை.",
            "why_c_en": "The SEC remains an independent constitutional body.",
            "why_c_ta": "SEC ஒரு சுதந்திரமான அரசியலமைப்பு அமைப்பாகவே தொடர்கிறது.",
            "why_d_en": "High Courts operate under Part VI of the Indian Constitution within India.",
            "why_d_ta": "உயர் நீதிமன்றங்கள் பகுதி VI-ன் கீழ் இந்தியாவிற்குள் செயல்படுகின்றன.",
            "tip_en": "Ramesh Kumar (2020): Executive cannot shorten SEC tenure mid-way to effect removal.",
            "tip_ta": "ரமேஷ் குமார் (2020): பதவி நீக்கம் செய்வதற்காக நிர்வாகத்தால் SEC பதவிக்காலத்தை பாதியில் குறைக்க முடியாது.",
            "fact_en": "The Supreme Court dismissed the State of AP's Special Leave Petition upholding the High Court ruling.",
            "fact_ta": "உயர் நீதிமன்றத் தீர்ப்பை உறுதிசெய்து ஆந்திர அரசின் மேல்முறையீட்டு மனுவை உச்ச நீதிமன்றம் தள்ளுபடி செய்தது."
        },

        # 29
        {
            "subtopic": "Tamil Nadu State Election & Finance Commissions - Legal Framework, Rules & Precedents",
            "stem_en": "[TNPSC Group 4 2016, VAO 2017]\nIn Tamil Nadu, the Village Panchayat President is elected through:",
            "stem_ta": "[TNPSC குரூப் 4 2016, VAO 2017]\nதமிழ்நாட்டில் கிராம பஞ்சாயத்து தலைவர் எவ்வாறு தேர்ந்தெடுக்கப்படுகிறார்?",
            "options": [
                ("Direct election by all registered voters of the village panchayat on a non-party basis", "கட்சி சாரா அடிப்படையில் கிராம பஞ்சாயத்தின் அனைத்து பதிவு செய்யப்பட்ட வாக்காளர்களாலும் நேரடித் தேர்தல் மூலம்"),
                ("Indirect election by the ward members from among themselves", "வார்டு உறுப்பினர்களால் தங்களுக்குள் இருந்து மறைமுகத் தேர்தல் மூலம்"),
                ("Nomination by the District Collector based on seniority", "மூப்பு அடிப்படையில் மாவட்ட ஆட்சியரால் நியமனம் செய்யப்படுதல்"),
                ("Voice vote in the State Legislative Assembly", "மாநில சட்டமன்றத்தில் குரல் வாக்கெடுப்பு மூலம்")
            ],
            "correct_key": "A",
            "exp_en": "Under Section 36 of the Tamil Nadu Panchayats Act 1994, the President of a Village Panchayat is elected directly by the persons whose names appear in the electoral roll for that village panchayat, conducted on a non-party basis.",
            "exp_ta": "1994 தமிழ்நாடு பஞ்சாயத்துகள் சட்டத்தின் பிரிவு 36-ன் கீழ், கிராம பஞ்சாயத்து தலைவர் அந்த கிராம பஞ்சாயத்திற்கான வாக்காளர் பட்டியலில் பெயர் உள்ள நபர்களால் நேரடியாகவும், கட்சி சாரா அடிப்படையிலும் தேர்ந்தெடுக்கப்படுகிறார்.",
            "why_a_en": "Village Panchayat President is elected directly on a non-party basis in Tamil Nadu.",
            "why_a_ta": "தமிழ்நாட்டில் கிராம பஞ்சாயத்து தலைவர் கட்சி சாரா அடிப்படையில் நேரடியாக தேர்ந்தெடுக்கப்படுகிறார்.",
            "why_b_en": "Ward members elect the Vice-President indirectly, not the President.",
            "why_b_ta": "வார்டு உறுப்பினர்கள் துணைத் தலைவரை மறைமுகமாகத் தேர்ந்தெடுக்கிறார்கள், தலைவரை அல்ல.",
            "why_c_en": "Collectors cannot nominate panchayat presidents.",
            "why_c_ta": "ஆட்சியர்களால் பஞ்சாயத்து தலைவர்களை நியமிக்க முடியாது.",
            "why_d_en": "The Legislative Assembly has no role in electing village presidents.",
            "why_d_ta": "கிராம தலைவர்களைத் தேர்ந்தெடுப்பதில் சட்டமன்றத்திற்கு எந்த பங்கும் இல்லை.",
            "tip_en": "Village President in TN = Direct election. Vice-President in TN = Indirect election by ward members.",
            "tip_ta": "TN கிராம தலைவர் = நேரடித் தேர்தல். TN கிராம துணைத் தலைவர் = வார்டு உறுப்பினர்களால் மறைமுகத் தேர்தல்.",
            "fact_en": "Village Panchayat President cannot contest on any registered political party symbol.",
            "fact_ta": "கிராம பஞ்சாயத்து தலைவர் எந்தவொரு பதிவு செய்யப்பட்ட அரசியல் கட்சி சின்னத்திலும் போட்டியிட முடியாது."
        },

        # 30
        {
            "subtopic": "Financial Devolution, Intergovernmental Transfers & Local Governance",
            "stem_en": "[TNPSC Group 1 2022]\nWhat was the landmark recommendation of the 15th Finance Commission regarding rural local body grants?",
            "stem_ta": "[TNPSC குரூப் 1 2022]\nஊரக உள்ளாட்சி மானியங்கள் தொடர்பாக 15வது நிதி ஆணையத்தின் முக்கிய பரிந்துரை என்ன?",
            "options": [
                ("Grants divided into 40% untied (basic) and 60% tied grants earmarked for sanitation, drinking water, and rainwater harvesting", "மானியங்கள் 40% கட்டுப்பாடற்றவை மற்றும் 60% சுகாதாரம், குடிநீர், மழைநீர் சேகரிப்புக்கு ஒதுக்கப்பட்ட நிபந்தனை மானியங்கள் என பிரிக்கப்பட்டன"),
                ("Abolition of all grants to village panchayats", "கிராம பஞ்சாயத்துகளுக்கான அனைத்து மானியங்களையும் ரத்து செய்தல்"),
                ("Conversion of all local body grants into interest-bearing loans", "அனைத்து உள்ளாட்சி மானியங்களையும் வட்டியுடன் கூடிய கடன்களாக மாற்றுதல்"),
                ("Directing that local body funds be transferred to foreign banks", "உள்ளாட்சி நிதியை வெளிநாட்டு வங்கிகளுக்கு மாற்ற உத்தரவிடுதல்")
            ],
            "correct_key": "A",
            "exp_en": "The 15th Finance Commission recommended allocating rural grants in a 40:60 ratio: 40% untied basic grants for local felt needs, and 60% tied grants specifically earmarked for drinking water, sanitation, ODF sustainability, and rainwater harvesting.",
            "exp_ta": "15வது நிதி ஆணையம் ஊரக மானியங்களை 40:60 என்ற விகிதத்தில் ஒதுக்க பரிந்துரைத்தது: உள்ளூர் தேவைகளுக்கான 40% கட்டுப்பாடற்ற அடிப்படை மானியங்கள், மற்றும் குடிநீர், சுகாதாரம், ODF பராமரிப்பு மற்றும் மழைநீர் சேகரிப்புக்காக பிரத்யேகமாக ஒதுக்கப்பட்ட 60% நிபந்தனை மானியங்கள்.",
            "why_a_en": "40% untied and 60% tied is the hallmark 15th FC formula for rural local bodies.",
            "why_a_ta": "40% கட்டுப்பாடற்ற மற்றும் 60% நிபந்தனை என்பது ஊரக உள்ளாட்சிகளுக்கான 15வது FC சூத்திரமாகும்.",
            "why_b_en": "Grants to village panchayats were increased, not abolished.",
            "why_b_ta": "கிராம பஞ்சாயத்துகளுக்கான மானியங்கள் அதிகரிக்கப்பட்டன, ரத்து செய்யப்படவில்லை.",
            "why_c_en": "Finance commission transfers are grants, never loans.",
            "why_c_ta": "நிதி ஆணையப் பகிர்வுகள் மானியங்களே தவிர, கடன்கள் அல்ல.",
            "why_d_en": "Transfers are routed through RBI and State Treasuries in Indian currency.",
            "why_d_ta": "பரிமாற்றங்கள் ரிசர்வ் வங்கி மற்றும் மாநில கருவூலங்கள் மூலம் இந்திய ரூபாயில் செலுத்தப்படுகின்றன.",
            "tip_en": "15th FC Rural Grants: 40% Untied + 60% Tied (WASH priorities).",
            "tip_ta": "15வது FC ஊரக மானியங்கள்: 40% கட்டுப்பாடற்றவை + 60% நிபந்தனைக்குட்பட்டவை (சுகாதாரம், குடிநீர்).",
            "fact_en": "Release of tied grants is conditional on online uploading of accounts on AuditOnline.",
            "fact_ta": "AuditOnline-ல் கணக்குகளைப் பதிவேற்றுவதன் அடிப்படையிலேயே நிபந்தனை மானியங்கள் வெளியிடப்படுகின்றன."
        },

        # 31
        {
            "subtopic": "State Election Commission - Constitutional Mandate & Provisions (Articles 243K & 243ZA)",
            "stem_en": "[TNPSC Assistant Section Officer 2018]\nWhich Article of the Constitution provides that elections to Municipalities shall be held before the expiration of a period of six months from the date of dissolution?",
            "stem_ta": "[TNPSC உதவிப் பிரிவு அலுவலர் 2018]\nநகராட்சி கலைக்கப்பட்ட தேதியிலிருந்து ஆறு மாத காலத்திற்குள் நகராட்சிகளுக்கான தேர்தல்கள் நடத்தப்பட வேண்டும் என்று கூறும் அரசியலமைப்பு சரத்து எது?",
            "options": [
                ("Article 243-U(3)(b)", "சரத்து 243-U(3)(b)"),
                ("Article 243-U(1)", "சரத்து 243-U(1)"),
                ("Article 243-E(1)", "சரத்து 243-E(1)"),
                ("Article 243ZA(1)", "சரத்து 243ZA(1)")
            ],
            "correct_key": "A",
            "exp_en": "Article 243-U(3)(b) mandates that an election to constitute a Municipality shall be completed before the expiration of a period of six months from the date of its dissolution.",
            "exp_ta": "சரத்து 243-U(3)(b) ஒரு நகராட்சி கலைக்கப்பட்ட தேதியிலிருந்து ஆறு மாத காலம் முடிவதற்குள் அதை அமைப்பதற்கான தேர்தல் முடிக்கப்பட வேண்டும் என்று கட்டாயப்படுத்துகிறது.",
            "why_a_en": "Article 243-U(3)(b) specifically prescribes the 6-month post-dissolution election deadline.",
            "why_a_ta": "சரத்து 243-U(3)(b) கலைக்கப்பட்ட பின் 6 மாத தேர்தல் காலக்கெடுவை குறிப்பாக பரிந்துரைக்கிறது.",
            "why_b_en": "Article 243-U(1) provides for the 5-year duration from first meeting.",
            "why_b_ta": "சரத்து 243-U(1) முதல் கூட்டத்திலிருந்து 5 ஆண்டு கால அளவை வழங்குகிறது.",
            "why_c_en": "Article 243-E(1) provides for the duration of Panchayats.",
            "why_c_ta": "சரத்து 243-E(1) பஞ்சாயத்துகளின் கால அளவை வழங்குகிறது.",
            "why_d_en": "Article 243ZA(1) provides for SEC conduct of municipal elections.",
            "why_d_ta": "சரத்து 243ZA(1) நகராட்சித் தேர்தல்களை SEC நடத்துவதை வழங்குகிறது.",
            "tip_en": "Both 243-E(3)(b) (Panchayats) and 243-U(3)(b) (Municipalities) enforce the strict 6-month dissolution rule.",
            "tip_ta": "243-E(3)(b) (பஞ்சாயத்துகள்) மற்றும் 243-U(3)(b) (நகராட்சிகள்) இரண்டும் கடுமையான 6 மாத கலைப்பு விதியை அமல்படுத்துகின்றன.",
            "fact_en": "The newly constituted body continues only for the remainder of the original 5-year term.",
            "fact_ta": "புதிதாக அமைக்கப்பட்ட அமைப்பு அசல் 5 ஆண்டு காலத்தின் மீதமுள்ள காலத்திற்கு மட்டுமே நீடிக்கும்."
        },

        # 32
        {
            "subtopic": "State Finance Commission - Constitutional Mandate, Composition & Role (Articles 243I & 243Y)",
            "stem_en": "[TNPSC Group 2 2015]\nWhich constitutional body recommends measures to augment the Consolidated Fund of a State to supplement the resources of Panchayats?",
            "stem_ta": "[TNPSC குரூப் 2 2015]\nபஞ்சாயத்துகளின் வளங்களை அதிகரிக்க மாநிலத்தின் தொகுப்பு நிதியை பெருக்குவதற்கான நடவடிக்கைகளை பரிந்துரைக்கும் அரசியலமைப்பு அமைப்பு எது?",
            "options": [
                ("The Central Finance Commission under Article 280(3)(bb)", "சரத்து 280(3)(bb)-ன் கீழ் மத்திய நிதி ஆணையம்"),
                ("The Planning Commission of India", "இந்திய திட்டக் குழு"),
                ("The Reserve Bank of India", "இந்திய ரிசர்வ் வங்கி"),
                ("The Comptroller and Auditor General of India", "இந்திய தலைமை கணக்குத் தணிக்கையாளர்")
            ],
            "correct_key": "A",
            "exp_en": "Under Article 280(3)(bb), the Central Finance Commission recommends measures needed to augment the Consolidated Fund of a State to supplement the resources of the Panchayats on the basis of SFC recommendations.",
            "exp_ta": "சரத்து 280(3)(bb)-ன் கீழ், SFC பரிந்துரைகளின் அடிப்படையில் பஞ்சாயத்துகளின் வளங்களை அதிகரிக்க மாநில தொகுப்பு நிதியை பெருக்குவதற்கு தேவையான நடவடிக்கைகளை மத்திய நிதி ஆணையம் பரிந்துரைக்கிறது.",
            "why_a_en": "Central Finance Commission under Article 280(3)(bb) performs this constitutional role.",
            "why_a_ta": "சரத்து 280(3)(bb)-ன் கீழ் மத்திய நிதி ஆணையம் இந்த அரசியலமைப்பு பணியைச் செய்கிறது.",
            "why_b_en": "Planning Commission was an extra-constitutional body, replaced by NITI Aayog.",
            "why_b_ta": "திட்டக் குழு அரசியலமைப்புக்கு அப்பாற்பட்ட அமைப்பு, தற்போது நிதி ஆயோக் மாற்றியுள்ளது.",
            "why_c_en": "RBI manages monetary policy and public debt, not local body fiscal augmentation.",
            "why_c_ta": "ரிசர்வ் வங்கி பணவியல் கொள்கையை நிர்வகிக்கிறது, உள்ளாட்சி நிதிப் பகிர்வை அல்ல.",
            "why_d_en": "CAG conducts audits under Article 148-151.",
            "why_d_ta": "CAG சரத்து 148-151-ன் கீழ் தணிக்கைகளை நடத்துகிறது.",
            "tip_en": "Article 280(3)(bb) = Central FC supplements Panchayats. Article 280(3)(c) = Central FC supplements Municipalities.",
            "tip_ta": "சரத்து 280(3)(bb) = பஞ்சாயத்துகளுக்கு மத்திய FC. சரத்து 280(3)(c) = நகராட்சிகளுக்கு மத்திய FC.",
            "fact_en": "This constitutional bridge was created by the 73rd Amendment Act 1992.",
            "fact_ta": "இந்த அரசியலமைப்புப் பாலம் 1992-ல் 73வது திருத்தச் சட்டத்தால் உருவாக்கப்பட்டது."
        },

        # 33
        {
            "subtopic": "State Election Commissioner - Appointment, Tenure, Removal & Autonomy",
            "stem_en": "[TNPSC Group 4 2012, Group 2 2015]\nCan the salary and conditions of service of a State Election Commissioner be varied to his disadvantage after appointment?",
            "stem_ta": "[TNPSC குரூப் 4 2012, குரூப் 2 2015]\nநியமனத்திற்குப் பிறகு ஒரு மாநில தேர்தல் ஆணையரின் ஊதியம் மற்றும் பணி நிபந்தனைகளை அவருக்கு பாதகமாக மாற்ற முடியுமா?",
            "options": [
                ("No, the second proviso to Article 243K(2) strictly prohibits varying them to his disadvantage", "இல்லை, சரத்து 243K(2)-ன் இரண்டாவது வரம்புரை அவற்றை அவருக்கு பாதகமாக மாற்றுவதை கண்டிப்பாகத் தடை செய்கிறது"),
                ("Yes, by an executive order of the District Collector at any time", "ஆம், மாவட்ட ஆட்சியரின் நிர்வாக உத்தரவின் மூலம் எந்த நேரத்திலும் மாற்றலாம்"),
                ("Yes, if the state ruling party loses an election", "ஆம், மாநில ஆளும் கட்சி தேர்தலில் தோற்றால் மாற்றலாம்"),
                ("Yes, by an ordinary resolution passed in a Village Panchayat Gram Sabha", "ஆம், கிராம பஞ்சாயத்து கிராம சபையில் நிறைவேற்றப்படும் சாதாரண தீர்மானம் மூலம்")
            ],
            "correct_key": "A",
            "exp_en": "The second proviso to Article 243K(2) explicitly provides: 'Provided further that the conditions of service of the State Election Commissioner shall not be varied to his disadvantage after his appointment.'",
            "exp_ta": "சரத்து 243K(2)-ன் இரண்டாவது வரம்புரை வெளிப்படையாகக் கூறுகிறது: 'மாநில தேர்தல் ஆணையரின் பணி நிபந்தனைகள் அவரது நியமனத்திற்குப் பிறகு அவருக்கு பாதகமாக மாற்றப்படக் கூடாது.'",
            "why_a_en": "The Constitution provides absolute immunity against disadvantageous variation of service conditions.",
            "why_a_ta": "பணி நிபந்தனைகளை பாதகமாக மாற்றுவதற்கு எதிராக அரசியலமைப்பு முழுமையான பாதுகாப்பை வழங்குகிறது.",
            "why_b_en": "Collectors have zero authority over SEC service conditions.",
            "why_b_ta": "SEC பணி நிபந்தனைகள் மீது ஆட்சியர்களுக்கு எந்த அதிகாரமும் இல்லை.",
            "why_c_en": "Electoral outcomes cannot affect constitutional service protections.",
            "why_c_ta": "தேர்தல் முடிவுகள் அரசியலமைப்புப் பணிப் பாதுகாப்புகளை பாதிக்க முடியாது.",
            "why_d_en": "Gram Sabha has no power over state constitutional functionaries.",
            "why_d_ta": "கிராம சபைக்கு மாநில அரசியலமைப்பு அதிகாரிகள் மீது எந்த அதிகாரமும் இல்லை.",
            "tip_en": "Non-diminution rule protects judicial and election authorities (Supreme Court Judges, HC Judges, CEC, SEC).",
            "tip_ta": "குறைப்பு செய்யக்கூடாது என்ற விதி நீதித்துறை மற்றும் தேர்தல் அதிகாரிகளைப் பாதுகாக்கிறது.",
            "fact_en": "This protection prevents executive coercion and intimidation during controversial election phases.",
            "fact_ta": "இந்த பாதுகாப்பு சர்ச்சைக்குரிய தேர்தல் கட்டங்களில் நிர்வாக அச்சுறுத்தல்களைத் தடுக்கிறது."
        },

        # 34
        {
            "subtopic": "Tamil Nadu State Election & Finance Commissions - Legal Framework, Rules & Precedents",
            "stem_en": "[TNPSC Group 1 2021]\nWhat is the composition of the State Finance Commission in Tamil Nadu under Section 240 of the Tamil Nadu Panchayats Act, 1994?",
            "stem_ta": "[TNPSC குரூப் 1 2021]\n1994 தமிழ்நாடு பஞ்சாயத்துகள் சட்டத்தின் பிரிவு 240-ன் கீழ் தமிழ்நாட்டில் மாநில நிதி ஆணையத்தின் கட்டமைப்பு என்ன?",
            "options": [
                ("A Chairman and not more than four other members", "ஒரு தலைவர் மற்றும் நான்கு உறுப்பினர்களுக்கு மிகாமல்"),
                ("A Chairman and ten other members", "ஒரு தலைவர் மற்றும் பத்து உறுப்பினர்கள்"),
                ("A single member serving as the sole Commissioner", "ஒற்றை உறுப்பினர் மட்டுமே ஆணையராக சேவை செய்தல்"),
                ("A committee comprising all 234 Members of Legislative Assembly", "அனைத்து 234 சட்டமன்ற உறுப்பினர்களையும் கொண்ட ஒரு குழு")
            ],
            "correct_key": "A",
            "exp_en": "Under Section 240(1) of the Tamil Nadu Panchayats Act, 1994, the State Finance Commission consists of a Chairman and not more than four other members appointed by the Governor.",
            "exp_ta": "1994 தமிழ்நாடு பஞ்சாயத்துகள் சட்டத்தின் பிரிவு 240(1)-ன் கீழ், மாநில நிதி ஆணையம் ஆளுநரால் நியமிக்கப்படும் ஒரு தலைவர் மற்றும் நான்கு உறுப்பினர்களுக்கு மிகாமல் கொண்டுள்ளது.",
            "why_a_en": "A Chairman and not more than 4 members is the statutory composition under Section 240.",
            "why_a_ta": "பிரிவு 240-ன் கீழ் ஒரு தலைவர் மற்றும் 4 உறுப்பினர்களுக்கு மிகாமல் என்பது சட்டப்பூர்வ கட்டமைப்பாகும்.",
            "why_b_en": "Ten members is incorrect.",
            "why_b_ta": "பத்து உறுப்பினர்கள் என்பது தவறானது.",
            "why_c_en": "SFC is a multi-member commission, not a single-member body.",
            "why_c_ta": "SFC என்பது பல உறுப்பினர்களைக் கொண்ட ஒரு ஆணையம், ஒற்றை உறுப்பினர் அமைப்பு அல்ல.",
            "why_d_en": "MLAs do not compose the State Finance Commission.",
            "why_d_ta": "சட்டமன்ற உறுப்பினர்கள் மாநில நிதி ஆணையத்தில் இடம்பெறுவதில்லை.",
            "tip_en": "Central FC (Art 280) = Chairman + 4 members. TN SFC (Sec 240) = Chairman + not more than 4 members.",
            "tip_ta": "மத்திய FC (சரத்து 280) = தலைவர் + 4 உறுப்பினர்கள். TN SFC (பிரிவு 240) = தலைவர் + 4 உறுப்பினர்களுக்கு மிகாமல்.",
            "fact_en": "Members are selected from experts in administration, public finance, economics, and local government.",
            "fact_ta": "நிர்வாகம், பொது நிதி, பொருளாதாரம் மற்றும் உள்ளாட்சித் துறை நிபுணர்களிலிருந்து உறுப்பினர்கள் தேர்ந்தெடுக்கப்படுகின்றனர்."
        },

        # 35
        {
            "subtopic": "State Election Commission - Constitutional Mandate & Provisions (Articles 243K & 243ZA)",
            "stem_en": "[TNPSC Group 2 2017, Group 4 2019]\nWho conducts elections to the offices of District Panchayat Chairman and Panchayat Union Chairman in Tamil Nadu?",
            "stem_ta": "[TNPSC குரூப் 2 2017, குரூப் 4 2019]\nதமிழ்நாட்டில் மாவட்ட பஞ்சாயத்து தலைவர் மற்றும் பஞ்சாயத்து ஒன்றியத் தலைவர் பதவிகளுக்கான தேர்தல்களை நடத்துவது யார்?",
            "options": [
                ("The Tamil Nadu State Election Commission", "தமிழ்நாடு மாநில தேர்தல் ஆணையம்"),
                ("The Election Commission of India", "இந்திய தேர்தல் ஆணையம்"),
                ("The Union Ministry of Panchayati Raj", "மத்திய பஞ்சாயத்து ராஜ் அமைச்சகம்"),
                ("The Law Commission of India", "இந்திய சட்ட ஆணையம்")
            ],
            "correct_key": "A",
            "exp_en": "Under Article 243K and the Tamil Nadu Panchayats Act 1994, all elections to local bodies—both direct (ward members/presidents) and indirect (Chairmen/Vice-Chairmen)—are conducted by the Tamil Nadu State Election Commission.",
            "exp_ta": "சரத்து 243K மற்றும் 1994 தமிழ்நாடு பஞ்சாயத்துகள் சட்டத்தின் கீழ், உள்ளாட்சி அமைப்புகளுக்கான அனைத்துத் தேர்தல்களும்—நேரடி (வார்டு உறுப்பினர்கள்/தலைவர்கள்) மற்றும் மறைமுக (ஒன்றிய/மாவட்ட தலைவர்கள்)—தமிழ்நாடு மாநில தேர்தல் ஆணையத்தால் நடத்தப்படுகின்றன.",
            "why_a_en": "TN SEC conducts both direct and indirect elections for all local bodies.",
            "why_a_ta": "TN SEC அனைத்து உள்ளாட்சி அமைப்புகளுக்கான நேரடி மற்றும் மறைமுகத் தேர்தல்கள் இரண்டையும் நடத்துகிறது.",
            "why_b_en": "ECI conducts elections to Parliament, State Legislatures, and President/VP.",
            "why_b_ta": "ECI நாடாளுமன்றம், சட்டமன்றங்கள் மற்றும் குடியரசுத் தலைவர் தேர்தல்களை நடத்துகிறது.",
            "why_c_en": "Ministry of Panchayati Raj is an administrative ministry, not an election body.",
            "why_c_ta": "பஞ்சாயத்து ராஜ் அமைச்சகம் ஒரு நிர்வாக அமைச்சகம், தேர்தல் நடத்தும் அமைப்பு அல்ல.",
            "why_d_en": "Law Commission is an advisory legal research body.",
            "why_d_ta": "சட்ட ஆணையம் ஒரு ஆலோசனை சட்ட ஆராய்ச்சி அமைப்பாகும்.",
            "tip_en": "ALL local body elections (Panchayats, Municipalities, Corporations, direct or indirect) = SEC.",
            "tip_ta": "அனைத்து உள்ளாட்சித் தேர்தல்களும் (நேரடி அல்லது மறைமுக) = SEC.",
            "fact_en": "Indirect elections are held in the council meeting hall presided over by the designated Returning Officer.",
            "fact_ta": "மறைமுகத் தேர்தல்கள் நியமிக்கப்பட்ட தேர்தல் நடத்தும் அதிகாரி தலைமையில் மன்றக் கூட்ட அரங்கில் நடத்தப்படுகின்றன."
        },

        # 36
        {
            "subtopic": "Financial Devolution, Intergovernmental Transfers & Local Governance",
            "stem_en": "[TNPSC Group 1 2015, Group 2 2018]\nWhich of the following taxes is levied and collected by Village Panchayats in Tamil Nadu under the Tamil Nadu Panchayats Act, 1994?",
            "stem_ta": "[TNPSC குரூப் 1 2015, குரூப் 2 2018]\n1994 தமிழ்நாடு பஞ்சாயத்துகள் சட்டத்தின் கீழ் தமிழ்நாட்டில் கிராம பஞ்சாயத்துகளால் விதிக்கப்பட்டு வசூலிக்கப்படும் வரி எது?",
            "options": [
                ("House Tax", "வீட்டு வரி"),
                ("Corporation Income Tax", "நிறுவன வருமான வரி"),
                ("Goods and Services Tax (GST)", "சரக்கு மற்றும் சேவை வரி (GST)"),
                ("Central Excise Duty", "மத்திய கலால் வரி")
            ],
            "correct_key": "A",
            "exp_en": "Under Section 171 of the Tamil Nadu Panchayats Act, 1994, every Village Panchayat shall levy a house tax on all buildings situated within the village panchayat limits.",
            "exp_ta": "1994 தமிழ்நாடு பஞ்சாயத்துகள் சட்டத்தின் பிரிவு 171-ன் கீழ், ஒவ்வொரு கிராம பஞ்சாயத்தும் தனது எல்லைக்குள் உள்ள அனைத்து கட்டிடங்கள் மீதும் வீட்டு வரி விதிக்க வேண்டும்.",
            "why_a_en": "House tax is a mandatory local tax levied directly by Village Panchayats.",
            "why_a_ta": "வீட்டு வரி என்பது கிராம பஞ்சாயத்துகளால் நேரடியாக விதிக்கப்படும் கட்டாய உள்ளூர் வரியாகும்.",
            "why_b_en": "Corporation tax is a Union tax.",
            "why_b_ta": "நிறுவன வரி என்பது மத்திய வரியாகும்.",
            "why_c_en": "GST is levied by Central and State Governments under Article 246A.",
            "why_c_ta": "GST சரத்து 246A-ன் கீழ் மத்திய மற்றும் மாநில அரசுகளால் விதிக்கப்படுகிறது.",
            "why_d_en": "Central Excise is levied by the Union Government.",
            "why_d_ta": "மத்திய கலால் வரி மத்திய அரசால் விதிக்கப்படுகிறது.",
            "tip_en": "House tax is the foundational own source tax revenue of Village Panchayats.",
            "tip_ta": "வீட்டு வரி என்பது கிராம பஞ்சாயத்துகளின் அடிப்படை சொந்த வரி வருவாயாகும்.",
            "fact_en": "Failure to assess house tax is a violation of statutory duties under the Act.",
            "fact_ta": "வீட்டு வரியை மதிப்பீடு செய்யத் தவறுவது சட்டப்பூர்வ கடமைகளை மீறுவதாகும்."
        },

        # 37
        {
            "subtopic": "State Election Commissioner - Appointment, Tenure, Removal & Autonomy",
            "stem_en": "[TNPSC Group 2 2019]\nUnder Article 243K, what is the legal effect of an election schedule announced by the State Election Commission?",
            "stem_ta": "[TNPSC குரூப் 2 2019]\nசரத்து 243K-ன் கீழ், மாநில தேர்தல் ஆணையத்தால் அறிவிக்கப்பட்ட தேர்தல் அட்டவணையின் சட்டரீதியான விளைவு என்ன?",
            "options": [
                ("The Model Code of Conduct immediately comes into operation and polling must proceed without court disruption", "தேர்தல் நடத்தை விதிகள் உடனடியாக செயல்பாட்டுக்கு வருகின்றன மற்றும் நீதிமன்ற இடையூறுகள் இன்றி வாக்கெடுப்பு நடைபெற வேண்டும்"),
                ("All state laws are automatically suspended permanently", "அனைத்து மாநில சட்டங்களும் தானாகவே நிரந்தரமாக இடைநிறுத்தப்படுகின்றன"),
                ("The Governor must immediately resign from office", "ஆளுநர் உடனடியாக தனது பதவியை ராஜினாமா செய்ய வேண்டும்"),
                ("Citizens lose their right to life and personal liberty under Article 21", "குடிமக்கள் சரத்து 21-ன் கீழான தங்களின் வாழ்வு மற்றும் தனிநபர் சுதந்திர உரிமையை இழக்கிறார்கள்")
            ],
            "correct_key": "A",
            "exp_en": "Upon notification of the election schedule by the SEC, the Model Code of Conduct comes into force immediately, the election machinery is under SEC control, and courts refrain from stalling the continuous electoral process.",
            "exp_ta": "SEC-ஆல் தேர்தல் அட்டவணை அறிவிக்கப்பட்டவுடன், தேர்தல் நடத்தை விதிகள் உடனடியாக நடைமுறைக்கு வருகின்றன, தேர்தல் இயந்திரம் SEC கட்டுப்பாட்டில் வருகிறது, மேலும் தேர்தல் செயல்முறையை நிறுத்துவதிலிருந்து நீதிமன்றங்கள் விலகி நிற்கின்றன.",
            "why_a_en": "MCC activation and continuous electoral process are the immediate legal consequences.",
            "why_a_ta": "MCC அமலாக்கம் மற்றும் தொடர்ச்சியான தேர்தல் செயல்முறை ஆகியவை உடனடி சட்டரீதியான விளைவுகளாகும்.",
            "why_b_en": "State laws remain in force except as modified by MCC rules.",
            "why_b_ta": "MCC விதிகளால் மாற்றியமைக்கப்பட்டதைத் தவிர மற்ற மாநில சட்டங்கள் தொடர்ந்து நடைமுறையில் இருக்கும்.",
            "why_c_en": "The Governor continues in office as constitutional head.",
            "why_c_ta": "ஆளுநர் அரசியலமைப்புத் தலைவராக தொடர்ந்து பதவியில் இருக்கிறார்.",
            "why_d_en": "Fundamental rights under Article 21 remain fully in force.",
            "why_d_ta": "சரத்து 21-ன் கீழான அடிப்படை உரிமைகள் முழுமையாக நடைமுறையில் இருக்கும்.",
            "tip_en": "Election announcement = MCC takes effect + Bar on midway court interference becomes operative.",
            "tip_ta": "தேர்தல் அறிவிப்பு = MCC நடைமுறைக்கு வருகிறது + நீதிமன்ற தலையீட்டுத் தடை செயல்பாட்டுக்கு வருகிறது.",
            "fact_en": "Electoral process must be completed before the expiration of the incumbent term.",
            "fact_ta": "பதவியில் உள்ளவர்களின் பதவிக்காலம் முடிவதற்குள் தேர்தல் செயல்முறை முடிக்கப்பட வேண்டும்."
        },

        # 38
        {
            "subtopic": "State Finance Commission - Constitutional Mandate, Composition & Role (Articles 243I & 243Y)",
            "stem_en": "[TNPSC Group 1 2022]\nWhat is the nature of the recommendations of the State Finance Commission?",
            "stem_ta": "[TNPSC குரூப் 1 2022]\nமாநில நிதி ஆணையத்தின் பரிந்துரைகளின் தன்மை என்ன?",
            "options": [
                ("Advisory in nature and not automatically binding on the State Government", "ஆலோசனைத் தன்மை கொண்டவை மற்றும் மாநில அரசைக் கட்டாயமாகக் கட்டுப்படுத்தாது"),
                ("Legally binding as an executable High Court decree", "உயர் நீதிமன்ற ஆணை போல சட்டப்பூர்வமாக கட்டாயக் கட்டுப்பாடு உடையது"),
                ("Direct constitutional amendments that bypass the Legislature", "சட்டமன்றத்தைத் தவிர்த்து நேரடியாக அரசியலமைப்பைத் திருத்துபவை"),
                ("Subject to veto by the local Village Administrative Officer", "உள்ளூர் கிராம நிர்வாக அலுவலரின் (VAO) வீட்டோ அதிகாரத்திற்கு உட்பட்டது")
            ],
            "correct_key": "A",
            "exp_en": "Like the Central Finance Commission, the recommendations of the State Finance Commission are advisory and recommendatory in nature. However, the Government must explain any non-acceptance in the Explanatory Memorandum.",
            "exp_ta": "மத்திய நிதி ஆணையத்தைப் போலவே, மாநில நிதி ஆணையத்தின் பரிந்துரைகளும் ஆலோசனைத் தன்மை கொண்டவை. இருப்பினும், ஏற்காததற்கான காரணங்களை அரசு விளக்கக் குறிப்பில் விளக்க வேண்டும்.",
            "why_a_en": "SFC recommendations are advisory, just like Article 280 recommendations.",
            "why_a_ta": "சரத்து 280-ன் பரிந்துரைகளைப் போலவே SFC பரிந்துரைகளும் ஆலோசனைத் தன்மை கொண்டவை.",
            "why_b_en": "They are not judicial decrees.",
            "why_b_ta": "அவை நீதித்துறை ஆணைகள் அல்ல.",
            "why_c_en": "They cannot amend the Constitution.",
            "why_c_ta": "அவை அரசியலமைப்பைத் திருத்த முடியாது.",
            "why_d_en": "VAO has no authority over SFC recommendations.",
            "why_d_ta": "SFC பரிந்துரைகள் மீது VAO-விற்கு எந்த அதிகாரமும் இல்லை.",
            "tip_en": "Recommendations = Advisory. Explanatory Memorandum (ATR) = Mandatory.",
            "tip_ta": "பரிந்துரைகள் = ஆலோசனை. விளக்கக் குறிப்பு (ATR) = கட்டாயம்.",
            "fact_en": "Democracies maintain high rates of acceptance for FC formulas to ensure institutional credibility.",
            "fact_ta": "நிறுவன நம்பகத்தன்மையை உறுதி செய்ய FC சூத்திரங்களை அரசாங்கங்கள் பொதுவாக ஏற்றுக்கொள்கின்றன."
        },

        # 39
        {
            "subtopic": "Tamil Nadu State Election & Finance Commissions - Legal Framework, Rules & Precedents",
            "stem_en": "[TNPSC Group 4 2019]\nUnder Section 258 of the Tamil Nadu Panchayats Act 1994, within how many days from the declaration of results must an election petition be filed?",
            "stem_ta": "[TNPSC குரூப் 4 2019]\n1994 தமிழ்நாடு பஞ்சாயத்துகள் சட்டத்தின் பிரிவு 258-ன் கீழ், தேர்தல் முடிவுகள் அறிவிக்கப்பட்டதிலிருந்து எத்தனை நாட்களுக்குள் தேர்தல் மனு தாக்கல் செய்யப்பட வேண்டும்?",
            "options": [
                ("45 days", "45 நாட்கள்"),
                ("30 days", "30 நாட்கள்"),
                ("60 days", "60 நாட்கள்"),
                ("90 days", "90 நாட்கள்")
            ],
            "correct_key": "A",
            "exp_en": "Section 258 of the Tamil Nadu Panchayats Act 1994 prescribes a limitation period of 45 days from the date of declaration of results for presenting an election petition to the Principal District Judge.",
            "exp_ta": "1994 தமிழ்நாடு பஞ்சாயத்துகள் சட்டத்தின் பிரிவு 258, முதன்மை மாவட்ட நீதிபதியிடம் தேர்தல் மனுவை தாக்கல் செய்வதற்கு முடிவுகள் அறிவிக்கப்பட்ட தேதியிலிருந்து 45 நாட்கள் கால வரம்பை நிர்ணயிக்கிறது.",
            "why_a_en": "45 days is the statutory limitation period under Section 258.",
            "why_a_ta": "பிரிவு 258-ன் கீழ் 45 நாட்கள் என்பது சட்டப்பூர்வ கால வரம்பாகும்.",
            "why_b_en": "30 days is incorrect.",
            "why_b_ta": "30 நாட்கள் என்பது தவறானது.",
            "why_c_en": "60 days is incorrect.",
            "why_c_ta": "60 நாட்கள் என்பது தவறானது.",
            "why_d_en": "90 days is incorrect.",
            "why_d_ta": "90 நாட்கள் என்பது தவறானது.",
            "tip_en": "Election Petition limitation = 45 days (matches Section 81 of RPA 1951 for MP/MLA polls).",
            "tip_ta": "தேர்தல் மனு கால வரம்பு = 45 நாட்கள் (நாடாளுமன்ற/சட்டமன்ற தேர்தல்களுக்கான RPA 1951 பிரிவு 81-ஐப் போன்றது).",
            "fact_en": "The Principal District Judge serves as the statutory election tribunal.",
            "fact_ta": "முதன்மை மாவட்ட நீதிபதி சட்டப்பூர்வ தேர்தல் தீர்ப்பாயமாக செயல்படுகிறார்."
        },

        # 40
        {
            "subtopic": "State Election Commission - Constitutional Mandate & Provisions (Articles 243K & 243ZA)",
            "stem_en": "[TNPSC Group 1 2017, Group 2 2019]\nIn which Article of the Constitution are the superintendence, direction, and control of elections to Municipalities vested in the State Election Commission?",
            "stem_ta": "[TNPSC குரூப் 1 2017, குரூப் 2 2019]\nநகராட்சிகளுக்கான தேர்தல்களின் மேற்பார்வை, வழிகாட்டுதல் மற்றும் கட்டுப்பாடு மாநில தேர்தல் ஆணையத்திடம் ஒப்படைக்கப்பட்டுள்ளதாகக் கூறும் அரசியலமைப்பு சரத்து எது?",
            "options": [
                ("Article 243ZA", "சரத்து 243ZA"),
                ("Article 243K", "சரத்து 243K"),
                ("Article 243ZG", "சரத்து 243ZG"),
                ("Article 243ZD", "சரத்து 243ZD")
            ],
            "correct_key": "A",
            "exp_en": "Article 243ZA(1) provides: 'The superintendence, direction and control of the preparation of electoral rolls for, and the conduct of, all elections to the Municipalities shall be vested in the State Election Commission referred to in article 243K.'",
            "exp_ta": "சரத்து 243ZA(1) கூறுகிறது: 'நகராட்சிகளுக்கான அனைத்துத் தேர்தல்களையும் நடத்துதல் மற்றும் வாக்காளர் பட்டியல்களைத் தயாரிப்பதற்கான மேற்பார்வை, வழிகாட்டுதல் மற்றும் கட்டுப்பாடு சரத்து 243K-ல் குறிப்பிடப்பட்டுள்ள மாநில தேர்தல் ஆணையத்திடம் ஒப்படைக்கப்படும்.'",
            "why_a_en": "Article 243ZA specifically governs municipal election superintendence.",
            "why_a_ta": "சரத்து 243ZA நகராட்சித் தேர்தல் மேற்பார்வையை குறிப்பாக நிர்வகிக்கிறது.",
            "why_b_en": "Article 243K governs panchayat elections.",
            "why_b_ta": "சரத்து 243K பஞ்சாயத்து தேர்தல்களை நிர்வகிக்கிறது.",
            "why_c_en": "Article 243ZG bars court interference in municipal elections.",
            "why_c_ta": "சரத்து 243ZG நகராட்சித் தேர்தல்களில் நீதிமன்ற தலையீட்டைத் தடை செய்கிறது.",
            "why_d_en": "Article 243ZD provides for District Planning Committees.",
            "why_d_ta": "சரத்து 243ZD மாவட்ட திட்டக் குழுக்களை வழங்குகிறது.",
            "tip_en": "243K = Panchayats. 243ZA = Municipalities.",
            "tip_ta": "243K = பஞ்சாயத்துகள். 243ZA = நகராட்சிகள்.",
            "fact_en": "Both provisions ensure uniform single election commission administration across the State.",
            "fact_ta": "இரு விதிகளும் மாநிலம் முழுவதும் ஒரே தேர்தல் ஆணைய நிர்வாகத்தை உறுதி செய்கின்றன."
        },

        # 41
        {
            "subtopic": "Financial Devolution, Intergovernmental Transfers & Local Governance",
            "stem_en": "[TNPSC Combined Civil Services 2018]\nWhat is meant by 'Horizontal Devolution' in the context of State Finance Commission recommendations?",
            "stem_ta": "[TNPSC ஒருங்கிணைந்த குடிமைப் பணிகள் 2018]\nமாநில நிதி ஆணையப் பரிந்துரைகளின் சூழலில் 'கிடைமட்டப் பகிர்வு' (Horizontal Devolution) என்பது எதைக் குறிக்கிறது?",
            "options": [
                ("The formula-based distribution of the divisible devolution pool among different tiers and individual local bodies", "வெவ்வேறு அடுக்குகள் மற்றும் தனிப்பட்ட உள்ளாட்சி அமைப்புகளிடையே பகிர்வுத் தொகுப்பை சூத்திர அடிப்படையில் விநியோகித்தல்"),
                ("The division of tax revenues between the Union Government and State Governments", "மத்திய அரசுக்கும் மாநில அரசுகளுக்கும் இடையே வரி வருவாயைப் பிரித்தல்"),
                ("The transfer of foreign aid directly to private commercial contractors", "வெளிநாட்டு உதவியை நேரடியாக தனியார் வணிக ஒப்பந்ததாரர்களுக்கு மாற்றுதல்"),
                ("The allocation of budget funds exclusively to the Governor's official residence", "பட்ஜெட் நிதியை ஆளுநரின் அதிகாரப்பூர்வ இல்லத்திற்கு மட்டுமே ஒதுக்குதல்")
            ],
            "correct_key": "A",
            "exp_en": "Horizontal devolution refers to the inter-se allocation of the total local body devolution pool among different tiers (Village, Union, District Panchayats, Municipalities, Corporations) and among individual bodies based on criteria like population and area.",
            "exp_ta": "கிடைமட்டப் பகிர்வு என்பது வெவ்வேறு அடுக்குகளுக்கு இடையே (கிராமம், ஒன்றியம், மாவட்டம், நகராட்சி, மாநகராட்சி) மற்றும் தனிப்பட்ட உள்ளாட்சி அமைப்புகளுக்கு இடையே மக்கள் தொகை மற்றும் பரப்பளவு போன்ற அளவுகோல்களின் அடிப்படையில் மொத்த உள்ளாட்சிப் பகிர்வுத் தொகுப்பை விநியோகிப்பதைக் குறிக்கிறது.",
            "why_a_en": "Formula distribution among local bodies is the exact definition of horizontal devolution.",
            "why_a_ta": "உள்ளாட்சி அமைப்புகளிடையே சூத்திர விநியோகம் என்பதே கிடைமட்டப் பகிர்வின் துல்லியமான வரையறையாகும்.",
            "why_b_en": "Union-State division is vertical devolution at the national level.",
            "why_b_ta": "மத்திய-மாநிலப் பகிர்வு என்பது தேசிய அளவிலான செங்குத்துப் பகிர்வாகும்.",
            "why_c_en": "Foreign aid is not horizontal devolution.",
            "why_c_ta": "வெளிநாட்டு உதவி கிடைமட்டப் பகிர்வு அல்ல.",
            "why_d_en": "Governor's residence expenses are charged on the Consolidated Fund under Article 202.",
            "why_d_ta": "ஆளுநரின் இல்லச் செலவுகள் சரத்து 202-ன் கீழ் தொகுப்பு நிதியில் சுமத்தப்படும் செலவுகளாகும்.",
            "tip_en": "Vertical = State to Local Bodies. Horizontal = Among Local Bodies (Rural vs Urban, and among panchayats).",
            "tip_ta": "செங்குத்து = மாநிலத்திலிருந்து உள்ளாட்சிகளுக்கு. கிடைமட்ட = உள்ளாட்சிகளுக்கு இடையே.",
            "fact_en": "Population weightage typically exceeds 50% in horizontal devolution formulas.",
            "fact_ta": "கிடைமட்டப் பகிர்வு சூத்திரங்களில் மக்கள் தொகை முக்கியத்துவம் பொதுவாக 50%-ஐத் தாண்டுகிறது."
        },

        # 42
        {
            "subtopic": "Tamil Nadu State Election & Finance Commissions - Legal Framework, Rules & Precedents",
            "stem_en": "[TNPSC Group 2 2015, Group 4 2018]\nWhich authority conducts elections to Town Panchayats, Municipalities, and Municipal Corporations in Tamil Nadu?",
            "stem_ta": "[TNPSC குரூப் 2 2015, குரூப் 4 2018]\nதமிழ்நாட்டில் பேரூராட்சிகள், நகராட்சிகள் மற்றும் மாநகராட்சிகளுக்கான தேர்தல்களை நடத்தும் அதிகாரம் எது?",
            "options": [
                ("Tamil Nadu State Election Commission", "தமிழ்நாடு மாநில தேர்தல் ஆணையம்"),
                ("Election Commission of India", "இந்திய தேர்தல் ஆணையம்"),
                ("Union Ministry of Housing and Urban Affairs", "மத்திய வீட்டுவசதி மற்றும் நகர்ப்புற விவகாரங்கள் அமைச்சகம்"),
                ("Madras Municipal Corporation Council", "மெட்ராஸ் மாநகராட்சி மன்றம்")
            ],
            "correct_key": "A",
            "exp_en": "The Tamil Nadu State Election Commission, established under Article 243K and 243ZA read with Tamil Nadu Urban Local Bodies Acts, conducts elections to all Town Panchayats, Municipalities, and Corporations.",
            "exp_ta": "சரத்துகள் 243K மற்றும் 243ZA-ன் கீழ் நிறுவப்பட்ட தமிழ்நாடு மாநில தேர்தல் ஆணையம் அனைத்து பேரூராட்சிகள், நகராட்சிகள் மற்றும் மாநகராட்சிகளுக்கான தேர்தல்களை நடத்துகிறது.",
            "why_a_en": "TN SEC conducts all urban local body elections.",
            "why_a_ta": "TN SEC அனைத்து நகர்ப்புற உள்ளாட்சித் தேர்தல்களையும் நடத்துகிறது.",
            "why_b_en": "ECI does not conduct municipal or corporation elections.",
            "why_b_ta": "ECI நகராட்சி அல்லது மாநகராட்சித் தேர்தல்களை நடத்துவதில்லை.",
            "why_c_en": "The Union Ministry is an executive policy-making department.",
            "why_c_ta": "மத்திய அமைச்சகம் ஒரு நிர்வாகக் கொள்கை வகுக்கும் துறையாகும்.",
            "why_d_en": "Municipal councils are contested bodies, not election-conducting authorities.",
            "why_d_ta": "நகராட்சி மன்றங்கள் போட்டியிடப்படும் அமைப்புகளே தவிர தேர்தல் நடத்தும் அமைப்புகள் அல்ல.",
            "tip_en": "Town Panchayats, Municipalities, Corporations = Urban Local Bodies (Article 243ZA) -> SEC.",
            "tip_ta": "பேரூராட்சிகள், நகராட்சிகள், மாநகராட்சிகள் = நகர்ப்புற உள்ளாட்சிகள் (சரத்து 243ZA) -> SEC.",
            "fact_en": "EVMs are deployed in municipal corporation ward elections in Tamil Nadu.",
            "fact_ta": "தமிழ்நாட்டில் மாநகராட்சி வார்டு தேர்தல்களில் EVM-கள் பயன்படுத்தப்படுகின்றன."
        },

        # 43
        {
            "subtopic": "State Election Commissioner - Appointment, Tenure, Removal & Autonomy",
            "stem_en": "[TNPSC Group 1 2014]\nCan a State Government postpone local body elections indefinitely by issuing an executive notification?",
            "stem_ta": "[TNPSC குரூப் 1 2014]\nநிர்வாக அறிவிப்பை வெளியிடுவதன் மூலம் உள்ளாட்சித் தேர்தல்களை மாநில அரசு காலவரையின்றி ஒத்திவைக்க முடியுமா?",
            "options": [
                ("No, holding elections before the expiry of the five-year term is a mandatory constitutional obligation upheld in Kishan Singh Tomar (2006)", "இல்லை, ஐந்து ஆண்டு பதவிக்காலம் முடிவதற்குள் தேர்தலை நடத்துவது கிஷன் சிங் தோமர் (2006) வழக்கில் உறுதிப்படுத்தப்பட்ட கட்டாய அரசியலமைப்பு கடமையாகும்"),
                ("Yes, the State Cabinet has unchecked discretion to postpone elections for any number of years", "ஆம், எத்தனை ஆண்டுகளுக்கு வேண்டுமானாலும் தேர்தலை ஒத்திவைக்க மாநில அமைச்சரவைக்கு வரம்பற்ற விருப்ப உரிமை உண்டு"),
                ("Yes, by passing an executive order signed by the Chief Secretary", "ஆம், தலைமைச் செயலாளர் கையொப்பமிட்ட நிர்வாக உத்தரவை பிறப்பிப்பதன் மூலம்"),
                ("Yes, if any single political party files an objection", "ஆம், ஏதேனும் ஒரு அரசியல் கட்சி ஆட்சேபனை தெரிவித்தால்")
            ],
            "correct_key": "A",
            "exp_en": "In Kishan Singh Tomar (2006), the Supreme Court ruled that holding elections to local bodies prior to the expiration of the 5-year duration under Articles 243-E and 243-U is mandatory, and cannot be postponed by executive action except in force majeure situations (natural calamity/war).",
            "exp_ta": "கிஷன் சிங் தோமர் (2006) வழக்கில், சரத்துகள் 243-E மற்றும் 243-U-ன் கீழ் 5 ஆண்டு காலம் முடிவதற்குள் உள்ளாட்சித் தேர்தல்களை நடத்துவது கட்டாயமானது என்றும், இயற்கை பேரழிவு போன்ற அசாதாரண சூழ்நிலைகளைத் தவிர நிர்வாக நடவடிக்கைகளால் அதை ஒத்திவைக்க முடியாது என்றும் உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
            "why_a_en": "Periodic elections before tenure expiry are a mandatory constitutional command.",
            "why_a_ta": "பதவிக்காலம் முடிவதற்குள் குறிப்பிட்ட காலத் தேர்தல்களை நடத்துவது கட்டாய அரசியலமைப்பு உத்தரவாகும்.",
            "why_b_en": "State cabinets do not possess unchecked discretion to derail democracy.",
            "why_b_ta": "ஜனநாயகத்தை சீர்குலைக்க மாநில அமைச்சரவைகளுக்கு தடையற்ற அதிகாரம் இல்லை.",
            "why_c_en": "Executive orders cannot supersede Articles 243-E and 243-U.",
            "why_c_ta": "நிர்வாக உத்தரவுகள் சரத்துகள் 243-E மற்றும் 243-U-ஐ மீற முடியாது.",
            "why_d_en": "Party objections cannot dispense with constitutional mandates.",
            "why_d_ta": "கட்சி ஆட்சேபனைகள் அரசியலமைப்பு கட்டளைகளை ரத்து செய்ய முடியாது.",
            "tip_en": "Mandate under 243-E & 243-U: Elections MUST be held before duration expires.",
            "tip_ta": "243-E & 243-U-ன் கீழான கட்டளை: பதவிக்காலம் முடிவதற்குள் தேர்தல் கட்டாயம் நடத்தப்பட வேண்டும்.",
            "fact_en": "Special Officers can be appointed only as a brief stopgap arrangement during genuine emergencies.",
            "fact_ta": "உண்மையான அவசரநிலைகளின் போது குறுகிய இடைக்கால ஏற்பாடாக மட்டுமே சிறப்பு அதிகாரிகள் நியமிக்கப்படலாம்."
        },

        # 44
        {
            "subtopic": "State Finance Commission - Constitutional Mandate, Composition & Role (Articles 243I & 243Y)",
            "stem_en": "[TNPSC Group 2 2017]\nUnder Article 243-I(2), who is empowered to determine the qualifications of the members of the State Finance Commission?",
            "stem_ta": "[TNPSC குரூப் 2 2017]\nசரத்து 243-I(2)-ன் கீழ், மாநில நிதி ஆணைய உறுப்பினர்களின் தகுதிகளைத் தீர்மானிக்க யாருக்கு அதிகாரம் அளிக்கப்பட்டுள்ளது?",
            "options": [
                ("The Legislature of a State, by law", "மாநில சட்டமன்றம், சட்டத்தின் மூலம்"),
                ("The Union Finance Ministry", "மத்திய நிதி அமைச்சகம்"),
                ("The Chief Justice of the High Court", "உயர் நீதிமன்ற தலைமை நீதிபதி"),
                ("The Comptroller and Auditor General of India", "இந்திய தலைமை கணக்குத் தணிக்கையாளர்")
            ],
            "correct_key": "A",
            "exp_en": "Article 243-I(2) provides that the Legislature of a State may, by law, determine the qualifications which shall be requisite for appointment as members of the Commission and the manner in which they shall be selected.",
            "exp_ta": "சரத்து 243-I(2) ஆணையத்தின் உறுப்பினர்களாக நியமிக்கப்படுவதற்குத் தேவையான தகுதிகளையும், அவர்கள் தேர்ந்தெடுக்கப்படும் முறையையும் மாநில சட்டமன்றம் சட்டத்தின் மூலம் தீர்மானிக்கலாம் என்று கூறுகிறது.",
            "why_a_en": "Article 243-I(2) explicitly vests qualification determination in the State Legislature.",
            "why_a_ta": "சரத்து 243-I(2) தகுதிகளைத் தீர்மானிக்கும் அதிகாரத்தை மாநில சட்டமன்றத்திற்கு வெளிப்படையாக வழங்குகிறது.",
            "why_b_en": "Union Finance Ministry determines qualifications for Central FC under Article 280(2).",
            "why_b_ta": "மத்திய நிதி அமைச்சகம் சரத்து 280(2)-ன் கீழ் மத்திய FC-க்கான தகுதிகளைத் தீர்மானிக்கிறது.",
            "why_c_en": "High Court Chief Justice has no role in SFC qualifications.",
            "why_c_ta": "SFC தகுதிகளில் உயர் நீதிமன்ற தலைமை நீதிபதிக்கு எந்த பங்கும் இல்லை.",
            "why_d_en": "CAG does not prescribe SFC qualifications.",
            "why_d_ta": "CAG SFC தகுதிகளை பரிந்துரைப்பதில்லை.",
            "tip_en": "Qualifications of SFC = State Legislature by law (e.g. Sec 240 of TN Panchayats Act 1994).",
            "tip_ta": "SFC தகுதிகள் = மாநில சட்டமன்றம் சட்டத்தின் மூலம் (1994 TN பஞ்சாயத்துகள் சட்டத்தின் பிரிவு 240 போன்றவை).",
            "fact_en": "The qualifications typically mirror public finance, economics, and administrative expertise.",
            "fact_ta": "தகுதிகள் பொதுவாக பொது நிதி, பொருளாதாரம் மற்றும் நிர்வாக நிபுணத்துவத்தைப் பிரதிபலிக்கின்றன."
        },

        # 45
        {
            "subtopic": "Tamil Nadu State Election & Finance Commissions - Legal Framework, Rules & Precedents",
            "stem_en": "[TNPSC Assistant Director of Rural Development 2019]\nIn Tamil Nadu, the Inspector of Panchayats empowered to oversee village panchayats and take action under Section 205 is:",
            "stem_ta": "[TNPSC உதவி ஊரக வளர்ச்சி இயக்குநர் 2019]\nதமிழ்நாட்டில் கிராம பஞ்சாயத்துகளைக் கண்காணிக்கவும் பிரிவு 205-ன் கீழ் நடவடிக்கை எடுக்கவும் அதிகாரம் பெற்ற பஞ்சாயத்துகளின் ஆய்வாளர் யார்?",
            "options": [
                ("The District Collector", "மாவட்ட ஆட்சியர்"),
                ("The State Election Commissioner", "மாநில தேர்தல் ஆணையர்"),
                ("The Tahsildar", "வட்டாட்சியர்"),
                ("The Village Administrative Officer", "கிராம நிர்வாக அலுவலர்")
            ],
            "correct_key": "A",
            "exp_en": "Under the Tamil Nadu Panchayats Act 1994, the District Collector is designated as the Inspector of Panchayats with powers to inspect, supervise, and initiate removal proceedings under Section 205.",
            "exp_ta": "1994 தமிழ்நாடு பஞ்சாயத்துகள் சட்டத்தின் கீழ், மாவட்ட ஆட்சியர் பஞ்சாயத்துகளின் ஆய்வாளராக நியமிக்கப்பட்டு, பிரிவு 205-ன் கீழ் ஆய்வு செய்யவும், மேற்பார்வையிடவும் மற்றும் பதவி நீக்க நடவடிக்கைகளைத் தொடங்கவும் அதிகாரம் பெற்றுள்ளார்.",
            "why_a_en": "The District Collector is the designated Inspector of Panchayats in Tamil Nadu.",
            "why_a_ta": "தமிழ்நாட்டில் மாவட்ட ஆட்சியரே நியமிக்கப்பட்ட பஞ்சாயத்துகளின் ஆய்வாளராவார்.",
            "why_b_en": "The SEC conducts elections and does not act as Inspector of Panchayats.",
            "why_b_ta": "SEC தேர்தல்களை நடத்துகிறது மற்றும் பஞ்சாயத்துகளின் ஆய்வாளராக செயல்படுவதில்லை.",
            "why_c_en": "Tahsildar presides over the meeting convened under Sec 205, but is not the Inspector.",
            "why_c_ta": "வட்டாட்சியர் பிரிவு 205-ன் கீழ் கூட்டப்படும் கூட்டத்திற்கு தலைமை தாங்குகிறார், ஆனால் ஆய்வாளர் அல்ல.",
            "why_d_en": "VAO is a subordinate village-level revenue officer.",
            "why_d_ta": "VAO என்பது கிராம அளவிலான கீழ்நிலை வருவாய் அதிகாரி.",
            "tip_en": "Collector = Inspector of Panchayats in Tamil Nadu.",
            "tip_ta": "தமிழ்நாட்டில் ஆட்சியர் = பஞ்சாயத்துகளின் ஆய்வாளர்.",
            "fact_en": "Director of Rural Development and Panchayat Raj acts as the Commissioner of Panchayats at the state level.",
            "fact_ta": "ஊரக வளர்ச்சி மற்றும் பஞ்சாயத்து ராஜ் இயக்குநர் மாநில அளவில் பஞ்சாயத்துகளின் ஆணையராகச் செயல்படுகிறார்."
        },

        # 46
        {
            "subtopic": "State Election Commission - Constitutional Mandate & Provisions (Articles 243K & 243ZA)",
            "stem_en": "[TNPSC Group 1 2017, Group 2 2019]\nUnder Article 243D(3) and 243T(3), what is the minimum constitutional reservation mandated for women in local body seats?",
            "stem_ta": "[TNPSC குரூப் 1 2017, குரூப் 2 2019]\nசரத்துகள் 243D(3) மற்றும் 243T(3)-ன் கீழ், உள்ளாட்சி அமைப்புகளில் பெண்களுக்காக கட்டாயமாக்கப்பட்டுள்ள குறைந்தபட்ச அரசியலமைப்பு இடஒதுக்கீடு என்ன?",
            "options": [
                ("Not less than one-third (33%) of the total number of seats", "மொத்த இடங்களில் மூன்றில் ஒரு பங்கிற்கு குறையாமல் (33%)"),
                ("Exactly 50% of the total number of seats", "மொத்த இடங்களில் சரியாக 50%"),
                ("Not more than 10% of the total number of seats", "மொத்த இடங்களில் 10%க்கு மிகாமல்"),
                ("Zero reservation; women's quota is strictly voluntary", "இடஒதுக்கீடு இல்லை; பெண்கள் ஒதுக்கீடு முற்றிலும் விருப்பத்திற்குரியது")
            ],
            "correct_key": "A",
            "exp_en": "Articles 243D(3) and 243T(3) mandate that not less than one-third (including the number of seats reserved for women belonging to SCs and STs) of the total number of seats shall be reserved for women. States like Tamil Nadu have enhanced this to 50%.",
            "exp_ta": "சரத்துகள் 243D(3) மற்றும் 243T(3) மொத்த இடங்களில் மூன்றில் ஒரு பங்கிற்கு குறையாமல் பெண்களுக்கு ஒதுக்கப்பட வேண்டும் என்று கட்டாயப்படுத்துகின்றன. தமிழ்நாடு போன்ற மாநிலங்கள் இதை 50%-ஆக உயர்த்தியுள்ளன.",
            "why_a_en": "Not less than one-third is the baseline constitutional mandate.",
            "why_a_ta": "மூன்றில் ஒரு பங்கிற்கு குறையாமல் என்பது அடிப்படை அரசியலமைப்பு கட்டளையாகும்.",
            "why_b_en": "50% is provided by state legislation in TN, but 1/3rd is the constitutional floor.",
            "why_b_ta": "TN-ல் 50% மாநில சட்டத்தால் வழங்கப்பட்டுள்ளது, ஆனால் 1/3 அரசியலமைப்பு குறைந்தபட்ச வரம்பாகும்.",
            "why_c_en": "10% is incorrect.",
            "why_c_ta": "10% என்பது தவறானது.",
            "why_d_en": "Women's reservation is mandatory, not voluntary.",
            "why_d_ta": "பெண்கள் இடஒதுக்கீடு கட்டாயமானது, விருப்பத்திற்குரியது அல்ல.",
            "tip_en": "Constitutional floor = 33% (1/3rd). State enhancement (TN) = 50%.",
            "tip_ta": "அரசியலமைப்பு குறைந்தபட்ச வரம்பு = 33% (1/3). மாநில உயர்வு (TN) = 50%.",
            "fact_en": "Over 20 states in India have enhanced women's local body reservation to 50%.",
            "fact_ta": "இந்தியாவில் 20-க்கும் மேற்பட்ட மாநிலங்கள் உள்ளாட்சிகளில் பெண்கள் இடஒதுக்கீட்டை 50%-ஆக உயர்த்தியுள்ளன."
        },

        # 47
        {
            "subtopic": "Financial Devolution, Intergovernmental Transfers & Local Governance",
            "stem_en": "[TNPSC Executive Officer 2017, Group 2A 2019]\nWhat does 'Vertical Devolution' signify in the fiscal transfers recommended by State Finance Commissions?",
            "stem_ta": "[TNPSC செயல் அலுவலர் 2017, குரூப் 2A 2019]\nமாநில நிதி ஆணையங்களால் பரிந்துரைக்கப்படும் நிதிப் பகிர்வுகளில் 'செங்குத்துப் பகிர்வு' (Vertical Devolution) என்பது எதைக் குறிக்கிறது?",
            "options": [
                ("The proportion of the State's own tax revenue shared with all local bodies as an aggregate divisible pool", "அனைத்து உள்ளாட்சி அமைப்புகளுடனும் ஒரு ஒருங்கிணைந்த பகிர்வுத் தொகுப்பாகப் பகிரப்படும் மாநில சொந்த வரி வருவாயின் விகிதம்"),
                ("The division of funds between adjacent village panchayats", "அருகிலுள்ள கிராம பஞ்சாயத்துகளிடையே நிதிப் பகிர்வு"),
                ("The allocation of central defense spending to state police", "மாநில காவல்துறைக்கு மத்திய பாதுகாப்பு செலவினங்களை ஒதுக்குதல்"),
                ("The repayment of foreign currency loans to the World Bank", "உலக வங்கிக்கு வெளிநாட்டு நாணயக் கடன்களை திருப்பிச் செலுத்துதல்")
            ],
            "correct_key": "A",
            "exp_en": "Vertical devolution is the top-down fiscal allocation from the State Government's tax revenue pool to the local government sector as a whole (e.g., 10% of SOTR in Tamil Nadu).",
            "exp_ta": "செங்குத்துப் பகிர்வு என்பது மாநில அரசின் வரி வருவாய் தொகுப்பிலிருந்து உள்ளாட்சித் துறைக்கு ஒட்டுமொத்தமாக வழங்கப்படும் மேல்-கீழ் நிதி ஒதுக்கீடாகும் (எ.கா. தமிழ்நாட்டில் SOTR-ல் 10%).",
            "why_a_en": "Vertical devolution represents the state-to-local bodies share.",
            "why_a_ta": "செங்குத்துப் பகிர்வு என்பது மாநிலத்திலிருந்து உள்ளாட்சிகளுக்கான பங்கைக் குறிக்கிறது.",
            "why_b_en": "Division between panchayats is horizontal devolution.",
            "why_b_ta": "பஞ்சாயத்துகளுக்கு இடையேயான பிரிவு கிடைமட்டப் பகிர்வாகும்.",
            "why_c_en": "Defense spending is entirely federal under Union List.",
            "why_c_ta": "பாதுகாப்பு செலவு மத்திய பட்டியலின் கீழ் முற்றிலும் மத்திய அரசினுடையது.",
            "why_d_en": "External debt repayment is an international sovereign function.",
            "why_d_ta": "வெளிநாட்டுக் கடன் திருப்பிச் செலுத்துதல் ஒரு சர்வதேச இறையாண்மைப் பணியாகும்.",
            "tip_en": "Vertical = State to Local Bodies. Horizontal = Distribution among local bodies.",
            "tip_ta": "செங்குத்து = மாநிலத்திலிருந்து உள்ளாட்சிகளுக்கு. கிடைமட்ட = உள்ளாட்சிகளுக்கு இடையே பகிர்வு.",
            "fact_en": "First SFC in TN recommended 8% of SOTR, which was raised to 9% by 3rd SFC and 10% by 4th/5th SFCs.",
            "fact_ta": "TN-ல் முதல் SFC SOTR-ல் 8%-ஐ பரிந்துரைத்தது, இது 3வது SFC-ல் 9%-ஆகவும், 4/5வது SFC-களில் 10%-ஆகவும் உயர்த்தப்பட்டது."
        },

        # 48
        {
            "subtopic": "State Election Commissioner - Appointment, Tenure, Removal & Autonomy",
            "stem_en": "[TNPSC Group 4 2015, Group 2 2017]\nWhat happens if a State Election Commissioner's office falls vacant due to death, resignation, or removal?",
            "stem_ta": "[TNPSC குரூப் 4 2015, குரூப் 2 2017]\nமரணம், ராஜினாமா அல்லது பதவி நீக்கம் காரணமாக மாநில தேர்தல் ஆணையர் பதவி காலியானால் என்ன நடக்கும்?",
            "options": [
                ("The Governor appoints a qualified person as the State Election Commissioner under Article 243K", "சரத்து 243K-ன் கீழ் ஆளுநர் ஒரு தகுதியான நபரை மாநில தேர்தல் ஆணையராக நியமிக்கிறார்"),
                ("The State Election Commission is permanently abolished", "மாநில தேர்தல் ஆணையம் நிரந்தரமாக ஒழிக்கப்படுகிறது"),
                ("The District Judge of the largest district automatically becomes the Commissioner for life", "மிகப்பெரிய மாவட்டத்தின் மாவட்ட நீதிபதி தானாகவே வாழ்நாள் ஆணையராகிறார்"),
                ("Local elections can never be held again in that state", "அந்த மாநிலத்தில் உள்ளாட்சித் தேர்தல்களை இனி ஒருபோதும் நடத்த முடியாது")
            ],
            "correct_key": "A",
            "exp_en": "Under Article 243K(1), the Governor is the appointing authority and appoints a new State Election Commissioner to fill the vacancy and maintain uninterrupted constitutional functioning.",
            "exp_ta": "சரத்து 243K(1)-ன் கீழ், ஆளுநர் நியமன அதிகாரியாவார் மற்றும் தடையற்ற அரசியலமைப்பு செயல்பாட்டைப் பராமரிக்க காலியிடத்தை நிரப்ப ஒரு புதிய மாநில தேர்தல் ஆணையரை நியமிக்கிறார்.",
            "why_a_en": "The Governor promptly appoints a successor under Article 243K.",
            "why_a_ta": "சரத்து 243K-ன் கீழ் ஆளுநர் உடனடியாக ஒரு வாரிசை நியமிக்கிறார்.",
            "why_b_en": "Constitutional bodies cannot be permanently abolished over vacancies.",
            "why_b_ta": "காலியிடங்கள் ஏற்பட்டதால் அரசியலமைப்பு அமைப்புகளை நிரந்தரமாக ஒழிக்க முடியாது.",
            "why_c_en": "There is no automatic succession for District Judges.",
            "why_c_ta": "மாவட்ட நீதிபதிகளுக்கு தானியங்கி வாரிசுரிமை எதுவும் இல்லை.",
            "why_d_en": "Elections are a mandatory periodic feature of local governance.",
            "why_d_ta": "தேர்தல்கள் உள்ளாட்சி நிர்வாகத்தின் கட்டாய குறிப்பிட்ட கால அம்சமாகும்.",
            "tip_en": "Vacancy in SEC is filled by Governor's appointment under Article 243K(1).",
            "tip_ta": "SEC காலியிடம் சரத்து 243K(1)-ன் கீழ் ஆளுநரின் நியமனத்தால் நிரப்பப்படுகிறது.",
            "fact_en": "Senior retired or serving senior IAS officers of Chief Secretary / Additional Chief Secretary rank are conventionally appointed.",
            "fact_ta": "தலைமைச் செயலாளர் / கூடுதல் தலைமைச் செயலாளர் அந்தஸ்திலான மூத்த IAS அதிகாரிகள் வழக்கமாக நியமிக்கப்படுகின்றனர்."
        },

        # 49
        {
            "subtopic": "Tamil Nadu State Election & Finance Commissions - Legal Framework, Rules & Precedents",
            "stem_en": "[TNPSC Group 1 2018]\nIn Tamil Nadu, which body consolidates the development plans prepared by Panchayats and Municipalities under Article 243ZD?",
            "stem_ta": "[TNPSC குரூப் 1 2018]\nதமிழ்நாட்டில் சரத்து 243ZD-ன் கீழ் பஞ்சாயத்துகள் மற்றும் நகராட்சிகளால் தயாரிக்கப்பட்ட வளர்ச்சித் திட்டங்களை ஒருங்கிணைக்கும் அமைப்பு எது?",
            "options": [
                ("District Planning Committee (DPC)", "மாவட்ட திட்டக் குழு (DPC)"),
                ("State Planning Commission", "மாநில திட்டக் குழு"),
                ("Central Finance Commission", "மத்திய நிதி ஆணையம்"),
                ("District Revenue Advisory Council", "மாவட்ட வருவாய் ஆலோசனைக் குழு")
            ],
            "correct_key": "A",
            "exp_en": "Article 243ZD mandates the constitution of a District Planning Committee (DPC) at the district level to consolidate the plans prepared by the Panchayats and Municipalities in the district and to prepare a draft development plan for the district as a whole.",
            "exp_ta": "சரத்து 243ZD மாவட்டத்தில் உள்ள பஞ்சாயத்துகள் மற்றும் நகராட்சிகளால் தயாரிக்கப்பட்ட திட்டங்களை ஒருங்கிணைக்கவும், ஒட்டுமொத்த மாவட்டத்திற்கான வரைவு வளர்ச்சித் திட்டத்தைத் தயாரிக்கவும் மாவட்ட அளவில் ஒரு மாவட்ட திட்டக் குழுவை (DPC) அமைக்க கட்டாயப்படுத்துகிறது.",
            "why_a_en": "District Planning Committee is specifically constituted under Article 243ZD.",
            "why_a_ta": "மாவட்ட திட்டக் குழு குறிப்பாக சரத்து 243ZD-ன் கீழ் அமைக்கப்படுகிறது.",
            "why_b_en": "State Planning Commission plans for the entire state, not district-level consolidation.",
            "why_b_ta": "மாநில திட்டக் குழு முழு மாநிலத்திற்கும் திட்டமிடுகிறது, மாவட்ட அளவில் ஒருங்கிணைப்பதில்லை.",
            "why_c_en": "Central Finance Commission recommends revenue transfers, not local project plans.",
            "why_c_ta": "மத்திய நிதி ஆணையம் நிதிப் பகிர்வை பரிந்துரைக்கிறது, திட்டங்களை அல்ல.",
            "why_d_en": "District Revenue Advisory Council is not a constitutional planning body.",
            "why_d_ta": "மாவட்ட வருவாய் ஆலோசனைக் குழு அரசியலமைப்பு திட்டமிடல் அமைப்பு அல்ல.",
            "tip_en": "Article 243ZD = District Planning Committee (DPC). Article 243ZE = Metropolitan Planning Committee (MPC).",
            "tip_ta": "சரத்து 243ZD = மாவட்ட திட்டக் குழு (DPC). சரத்து 243ZE = பெருநகர திட்டக் குழு (MPC).",
            "fact_en": "In Tamil Nadu, the District Panchayat Chairman heads the DPC, and the District Collector serves as Member-Secretary.",
            "fact_ta": "தமிழ்நாட்டில் மாவட்ட பஞ்சாயத்து தலைவர் DPC-க்கு தலைமை தாங்குகிறார், மாவட்ட ஆட்சியர் உறுப்பினர்-செயலாளராக பணியாற்றுகிறார்."
        },

        # 50
        {
            "subtopic": "Financial Devolution, Intergovernmental Transfers & Local Governance",
            "stem_en": "[TNPSC Group 2 2018, Group 4 2022]\nWhat is the primary objective of establishing State Finance Commissions under the 73rd and 74th Amendments?",
            "stem_ta": "[TNPSC குரூப் 2 2018, குரூப் 4 2022]\n73 மற்றும் 74வது திருத்தங்களின் கீழ் மாநில நிதி ஆணையங்களை நிறுவுவதன் முதன்மை நோக்கம் என்ன?",
            "options": [
                ("To ensure fiscal decentralization, predictable revenue sharing, and financial autonomy for local self-government institutions", "நிதி அதிகாரப் பரவலாக்கம், கணிக்கக்கூடிய வருவாய் பகிர்வு மற்றும் உள்ளாட்சி அமைப்புகளுக்கான நிதி சுயாட்சியை உறுதி செய்தல்"),
                ("To abolish all village panchayats and centralize taxation in New Delhi", "அனைத்து கிராம பஞ்சாயத்துகளையும் ஒழித்து புது தில்லியில் வரிவிதிப்பை மையப்படுத்துதல்"),
                ("To privatize all public drinking water and sanitation services", "அனைத்து பொது குடிநீர் மற்றும் சுகாதார சேவைகளையும் தனியார்மயமாக்குதல்"),
                ("To dissolve state legislative assemblies every five years without election", "தேர்தல் இன்றி ஒவ்வொரு ஐந்து ஆண்டுகளுக்கும் மாநில சட்டமன்றங்களை கலைத்தல்")
            ],
            "correct_key": "A",
            "exp_en": "The core constitutional vision of Articles 243-I and 243Y was to provide institutionalized financial stability to local self-governments, moving from discretionary political handouts to statutory, formula-based devolution of fiscal resources.",
            "exp_ta": "சரத்துகள் 243-I மற்றும் 243Y-ன் முக்கிய அரசியலமைப்பு நோக்கம், உள்ளாட்சி அமைப்புகளுக்கு நிறுவனமயமாக்கப்பட்ட நிதி ஸ்திரத்தன்மையை வழங்குவதும், விருப்ப அரசியல் உதவிகளிலிருந்து சட்டப்பூர்வ, சூத்திர அடிப்படையிலான நிதிப் பகிர்வுக்கு மாறுவதும் ஆகும்.",
            "why_a_en": "Fiscal decentralization and local financial strengthening are the primary objectives of SFCs.",
            "why_a_ta": "நிதி அதிகாரப் பரவலாக்கம் மற்றும் உள்ளாட்சி நிதி வலுவூட்டல் ஆகியவை SFC-களின் முதன்மை நோக்கங்களாகும்.",
            "why_b_en": "The 73rd/74th amendments constitutionalized local bodies, not abolished them.",
            "why_b_ta": "73/74வது திருத்தங்கள் உள்ளாட்சி அமைப்புகளுக்கு அரசியலமைப்பு அங்கீகாரம் அளித்தன, அவற்றை ஒழிக்கவில்லை.",
            "why_c_en": "SFCs fund public service delivery, not mandatory privatization.",
            "why_c_ta": "SFC-கள் பொது சேவை வழங்கலுக்கு நிதியளிக்கின்றன, கட்டாய தனியார்மயமாக்கலுக்கு அல்ல.",
            "why_d_en": "SFCs have no role in dissolving state assemblies.",
            "why_d_ta": "மாநில சட்டமன்றங்களை கலைப்பதில் SFC-களுக்கு எந்த பங்கும் இல்லை.",
            "tip_en": "SFC = The fiscal backbone of democratic decentralization in India.",
            "tip_ta": "SFC = இந்தியாவில் ஜனநாயக அதிகாரப் பரவலாக்கத்தின் நிதி முதுகெலும்பு.",
            "fact_en": "Without financial devolution, political decentralization remains hollow and ineffective.",
            "fact_ta": "நிதிப் பகிர்வு இல்லாமல் அரசியல் அதிகாரப் பரவலாக்கம் பயனற்றதாகவே இருக்கும்."
        }
    ]

    questions = []
    for i, item in enumerate(raw_data, start=1):
        opts = item["options"]
        correct_key = item["correct_key"]

        q = make_sefc_q(
            qid=f"SEFC_PYQ_{i:03d}",
            diff="medium" if i % 2 == 0 else "easy",
            qtype="pyq",
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
            tags=["polity", "state_election_finance_commissions", "pyq", item["subtopic"].lower().replace(" ", "_")]
        )
        questions.append(q)
    return questions


def build_pyq_file():
    qs = get_pyq_questions()
    print(f"Generated {len(qs)} raw PYQ questions for State Election & Finance Commissions.")
    balanced = randomize_and_balance_dataset(qs, seed=52)

    out_dir = os.path.join("data", "questions", "polity")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "state_election_finance_commissions_pyq.json")
    alias_path = os.path.join(out_dir, "state_election_finance_commissions_pyq_practice.json")

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)
    with open(alias_path, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)
    print(f"Saved balanced PYQ MCQs to {out_path} and alias {alias_path}")

    rep = ContentValidator.validate_file(out_path, expected_count=50, expected_prefix="SEFC_PYQ_")
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
