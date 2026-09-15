# -*- coding: utf-8 -*-
"""
State Election & Finance Commissions - Part 2A Statement-Based MCQs Generator (50 MCQs: SEFC_S_001 to SEFC_S_050)
TNPSC Nova AI Content Engine
"""
import json
import os
from state_election_finance_commissions_mcq_helper import make_sefc_q
from tools.nova_content_engine.answer_randomizer import randomize_and_balance_dataset
from tools.nova_content_engine.validator import ContentValidator


def get_statement_questions():
    raw_data = [
        # 1
        {
            "subtopic": "State Election Commission - Constitutional Mandate & Provisions (Articles 243K & 243ZA)",
            "stem_en": "Consider the following statements regarding the State Election Commission (SEC):\n1. Article 243K vests the superintendence, direction, and control of the preparation of electoral rolls and the conduct of all elections to the Panchayats in the SEC.\n2. Article 243ZA extends identical powers to the SEC for conducting elections to Municipalities.\n3. The SEC also conducts elections to the State Legislative Assemblies.\nWhich of the statements given above is/are correct?",
            "stem_ta": "மாநில தேர்தல் ஆணையம் (SEC) தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. சரத்து 243K பஞ்சாயத்துகளுக்கான அனைத்துத் தேர்தல்களையும் நடத்துதல் மற்றும் வாக்காளர் பட்டியல்களைத் தயாரிப்பதற்கான மேற்பார்வை, வழிகாட்டுதல் மற்றும் கட்டுப்பாட்டு அதிகாரத்தை SEC-யிடம் வழங்குகிறது.\n2. சரத்து 243ZA நகராட்சிகளுக்கான தேர்தல்களை நடத்துவதற்கும் இதேபோன்ற அதிகாரங்களை SEC-க்கு விரிவுபடுத்துகிறது.\n3. மாநில சட்டமன்றப் பேரவைகளுக்கான தேர்தல்களையும் SEC நடத்துகிறது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
            "options": [
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("1 only", "1 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்")
            ],
            "correct_key": "A",
            "exp_en": "Statements 1 and 2 are correct. Statement 3 is incorrect because elections to Parliament and State Legislative Assemblies are conducted exclusively by the Election Commission of India (ECI) under Article 324.",
            "exp_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் நாடாளுமன்றம் மற்றும் மாநில சட்டமன்றங்களுக்கான தேர்தல்கள் சரத்து 324-ன் கீழ் இந்திய தேர்தல் ஆணையத்தால் (ECI) மட்டுமே நடத்தப்படுகின்றன.",
            "why_a_en": "Statements 1 and 2 are correct; statement 3 is incorrect.",
            "why_a_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை; கூற்று 3 தவறானது.",
            "why_b_en": "Statement 2 is also correct.",
            "why_b_ta": "கூற்று 2-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "why_c_en": "Statement 3 is incorrect.",
            "why_c_ta": "கூற்று 3 தவறானது.",
            "why_d_en": "Statement 3 is incorrect; ECI conducts assembly polls.",
            "why_d_ta": "கூற்று 3 தவறானது; ECI சட்டமன்றத் தேர்தல்களை நடத்துகிறது.",
            "tip_en": "SEC = Local bodies (Articles 243K & 243ZA). ECI = Parliament, State Assemblies, President, VP (Article 324).",
            "tip_ta": "SEC = உள்ளாட்சி அமைப்புகள் (சரத்துகள் 243K & 243ZA). ECI = நாடாளுமன்றம், சட்டமன்றங்கள், குடியரசுத் தலைவர் (சரத்து 324).",
            "fact_en": "Articles 243K and 243ZA were inserted by the 73rd and 74th Amendments in 1992.",
            "fact_ta": "சரத்துகள் 243K மற்றும் 243ZA 1992-ல் 73வது மற்றும் 74வது திருத்தங்களால் சேர்க்கப்பட்டன."
        },

        # 2
        {
            "subtopic": "State Election Commissioner - Appointment, Tenure, Removal & Autonomy",
            "stem_en": "Consider the following statements regarding the appointment and removal of the State Election Commissioner:\n1. The State Election Commissioner is appointed by the Governor of the State.\n2. The conditions of service and tenure of office of the SEC are determined by the Governor subject to any law made by the State Legislature.\n3. The SEC can be removed from office at the absolute pleasure of the Chief Minister.\nWhich of the statements given above are correct?",
            "stem_ta": "மாநில தேர்தல் ஆணையரின் நியமனம் மற்றும் பதவி நீக்கம் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. மாநில தேர்தல் ஆணையர் மாநில ஆளுநரால் நியமிக்கப்படுகிறார்.\n2. SEC-ன் பணி நிபந்தனைகள் மற்றும் பதவிக்காலம் மாநில சட்டமன்றம் இயற்றும் சட்டத்திற்கு உட்பட்டு ஆளுநரால் தீர்மானிக்கப்படுகிறது.\n3. முதலமைச்சரின் விருப்பத்தின் பேரில் எப்போது வேண்டுமானாலும் SEC-ஐ பதவியிலிருந்து நீக்க முடியும்.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?",
            "options": [
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("1 and 3 only", "1 மற்றும் 3 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்")
            ],
            "correct_key": "A",
            "exp_en": "Statements 1 and 2 are correct. Statement 3 is incorrect because under Article 243K(2), the SEC can only be removed in like manner and on like grounds as a Judge of a High Court (Parliamentary address/impeachment).",
            "exp_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் சரத்து 243K(2)-ன் கீழ், உயர் நீதிமன்ற நீதிபதியை நீக்கும் அதே முறையில் மட்டுமே (நாடாளுமன்ற பதவி நீக்கத் தீர்மானம்) SEC-ஐ நீக்க முடியும்.",
            "why_a_en": "Statements 1 and 2 correctly reflect Article 243K(1) & (2).",
            "why_a_ta": "கூற்றுகள் 1 மற்றும் 2 சரத்து 243K(1) & (2)-ஐ சரியாகப் பிரதிபலிக்கின்றன.",
            "why_b_en": "Statement 3 is incorrect.",
            "why_b_ta": "கூற்று 3 தவறானது.",
            "why_c_en": "Statement 1 is also correct while statement 3 is incorrect.",
            "why_c_ta": "கூற்று 1-ம் சரியானது மற்றும் கூற்று 3 தவறானது.",
            "why_d_en": "Statement 3 is incorrect; CM has no removal power.",
            "why_d_ta": "கூற்று 3 தவறானது; முதல்வருக்கு நீக்கும் அதிகாரம் இல்லை.",
            "tip_en": "SEC has High Court Judge protection against arbitrary executive dismissal.",
            "tip_ta": "நிர்வாகத் தன்னிச்சையான பணிநீக்கத்திற்கு எதிராக உயர் நீதிமன்ற நீதிபதிக்கான பாதுகாப்பு SEC-க்கு உண்டு.",
            "fact_en": "Conditions of service of an SEC cannot be varied to their disadvantage after appointment.",
            "fact_ta": "நியமனத்திற்குப் பிறகு ஒரு SEC-ன் பணி நிபந்தனைகளை அவருக்கு பாதகமாக மாற்ற முடியாது."
        },

        # 3
        {
            "subtopic": "State Finance Commission - Constitutional Mandate, Composition & Role (Articles 243I & 243Y)",
            "stem_en": "Consider the following statements regarding the State Finance Commission (SFC):\n1. It is constituted by the Governor every five years under Article 243-I.\n2. Article 243Y mandates that the SFC constituted under Article 243-I shall also review the financial position of Municipalities.\n3. The recommendations of the SFC are automatically binding on the State Government without any legislative tabling.\nWhich of the statements given above is/are correct?",
            "stem_ta": "மாநில நிதி ஆணையம் (SFC) தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது சரத்து 243-I-ன் கீழ் ஒவ்வொரு ஐந்து ஆண்டுகளுக்கும் ஒருமுறை ஆளுநரால் அமைக்கப்படுகிறது.\n2. சரத்து 243-I-ன் கீழ் அமைக்கப்பட்ட SFC நகராட்சிகளின் நிதி நிலையையும் மறுஆய்வு செய்ய வேண்டும் என்று சரத்து 243Y கட்டாயப்படுத்துகிறது.\n3. SFC-ன் பரிந்துரைகள் சட்டமன்றத்தில் வைக்கப்படாமலேயே மாநில அரசைக் கட்டாயமாகக் கட்டுப்படுத்தும்.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
            "options": [
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("1 only", "1 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்")
            ],
            "correct_key": "A",
            "exp_en": "Statements 1 and 2 are correct. Statement 3 is incorrect because the recommendations are advisory in nature and must be laid before the State Legislature along with an Explanatory Memorandum (Action Taken Report) under Article 243-I(4).",
            "exp_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் பரிந்துரைகள் ஆலோசனைத் தன்மை கொண்டவை மற்றும் சரத்து 243-I(4)-ன் கீழ் எடுக்கப்பட்ட நடவடிக்கை அறிக்கையுடன் மாநில சட்டமன்றத்தின் முன் வைக்கப்பட வேண்டும்.",
            "why_a_en": "Statements 1 and 2 are correct; recommendations are advisory, not automatically binding.",
            "why_a_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை; பரிந்துரைகள் ஆலோசனைத் தன்மை கொண்டவை.",
            "why_b_en": "Statement 2 is also correct.",
            "why_b_ta": "கூற்று 2-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "why_c_en": "Statement 3 is incorrect.",
            "why_c_ta": "கூற்று 3 தவறானது.",
            "why_d_en": "Statement 3 is incorrect; SFC recommendations require legislative tabling.",
            "why_d_ta": "கூற்று 3 தவறானது; SFC பரிந்துரைகள் சட்டமன்றத்தில் வைக்கப்பட வேண்டும்.",
            "tip_en": "Article 243-I covers Panchayats; Article 243Y covers Municipalities using the same Commission.",
            "tip_ta": "சரத்து 243-I பஞ்சாயத்துகளையும், சரத்து 243Y அதே ஆணையத்தைப் பயன்படுத்தி நகராட்சிகளையும் உள்ளடக்கியது.",
            "fact_en": "Single SFC reviews both rural and urban local bodies in all states.",
            "fact_ta": "அனைத்து மாநிலங்களிலும் ஒரே SFC ஊரக மற்றும் நகர்ப்புற உள்ளாட்சி அமைப்புகளை மறுஆய்வு செய்கிறது."
        },

        # 4
        {
            "subtopic": "Financial Devolution, Intergovernmental Transfers & Local Governance",
            "stem_en": "Consider the following statements regarding the role of Central Finance Commission vis-a-vis State Finance Commissions:\n1. Article 280(3)(bb) requires the Central Finance Commission to suggest measures to augment the State's Consolidated Fund to supplement Panchayat resources.\n2. Article 280(3)(c) requires similar measures for Municipalities.\n3. Both sub-clauses mandate that these measures be recommended 'on the basis of the recommendations made by the Finance Commission of the State'.\nWhich of the statements given above are correct?",
            "stem_ta": "மாநில நிதி ஆணையங்களுடன் மத்திய நிதி ஆணையத்தின் பங்கு தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. பஞ்சாயத்து வளங்களை அதிகரிக்க மாநிலத்தின் தொகுப்பு நிதியை பெருக்குவதற்கான நடவடிக்கைகளை பரிந்துரைக்க மத்திய நிதி ஆணையத்திற்கு சரத்து 280(3)(bb) தேவைப்படுகிறது.\n2. சரத்து 280(3)(c) நகராட்சிகளுக்கும் இதேபோன்ற நடவடிக்கைகளை கோருகிறது.\n3. இரு உட்பிரிவுகளும் இந்த நடவடிக்கைகள் 'மாநில நிதி ஆணையத்தின் பரிந்துரைகளின் அடிப்படையில்' பரிந்துரைக்கப்பட வேண்டும் என்று கட்டாயப்படுத்துகின்றன.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?",
            "options": [
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்"),
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1 and 3 only", "1 மற்றும் 3 மட்டுமே")
            ],
            "correct_key": "A",
            "exp_en": "All three statements are correct. The 73rd and 74th Amendments inserted Article 280(3)(bb) and (c) to organically link the Central Finance Commission with State Finance Commissions.",
            "exp_ta": "மூன்று கூற்றுகளும் சரியானவை. 73வது மற்றும் 74வது திருத்தங்கள் மத்திய நிதி ஆணையத்தை மாநில நிதி ஆணையங்களுடன் இணைக்க சரத்து 280(3)(bb) மற்றும் (c)-ஐ சேர்த்தன.",
            "why_a_en": "All three statements accurately recite Article 280(3)(bb) & (c).",
            "why_a_ta": "மூன்று கூற்றுகளும் சரத்து 280(3)(bb) & (c)-ஐ துல்லியமாக விவரிக்கின்றன.",
            "why_b_en": "Statement 3 is also correct.",
            "why_b_ta": "கூற்று 3-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "why_c_en": "Statement 1 is also correct.",
            "why_c_ta": "கூற்று 1-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "why_d_en": "Statement 2 is also correct.",
            "why_d_ta": "கூற்று 2-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "tip_en": "Article 280(3)(bb) = Panchayats; 280(3)(c) = Municipalities; linked to SFC recommendations.",
            "tip_ta": "சரத்து 280(3)(bb) = பஞ்சாயத்துகள்; 280(3)(c) = நகராட்சிகள்; SFC பரிந்துரைகளுடன் இணைக்கப்பட்டது.",
            "fact_en": "The 11th Central Finance Commission was the first to recommend grants under these amended clauses.",
            "fact_ta": "11வது மத்திய நிதி ஆணையமே இந்த திருத்தப்பட்ட விதிகளின் கீழ் மானியங்களை பரிந்துரைத்த முதல் ஆணையமாகும்."
        },

        # 5
        {
            "subtopic": "Tamil Nadu State Election & Finance Commissions - Legal Framework, Rules & Precedents",
            "stem_en": "Consider the following statements regarding the Tamil Nadu State Election Commission:\n1. It was established in 1994 following the enactment of the Tamil Nadu Panchayats Act, 1994.\n2. Its headquarters is located in Chennai.\n3. The Tamil Nadu State Election Commissioner is appointed by the Chief Justice of the Madras High Court.\nWhich of the statements given above is/are correct?",
            "stem_ta": "தமிழ்நாடு மாநில தேர்தல் ஆணையம் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது 1994 தமிழ்நாடு பஞ்சாயத்துகள் சட்டம் இயற்றப்பட்டதைத் தொடர்ந்து 1994-ல் நிறுவப்பட்டது.\n2. இதன் தலைமையகம் சென்னையில் அமைந்துள்ளது.\n3. தமிழ்நாடு மாநில தேர்தல் ஆணையர் மெட்ராஸ் உயர் நீதிமன்ற தலைமை நீதிபதியால் நியமிக்கப்படுகிறார்.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
            "options": [
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("1 only", "1 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்")
            ],
            "correct_key": "A",
            "exp_en": "Statements 1 and 2 are correct. Statement 3 is incorrect because the State Election Commissioner is appointed by the Governor of Tamil Nadu under Section 239 of the Tamil Nadu Panchayats Act 1994 and Article 243K.",
            "exp_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் மாநில தேர்தல் ஆணையர் சரத்து 243K மற்றும் 1994 சட்டத்தின் பிரிவு 239-ன் கீழ் தமிழ்நாடு ஆளுநரால் நியமிக்கப்படுகிறார்.",
            "why_a_en": "Statements 1 and 2 are correct; Governor appoints the SEC, not Chief Justice.",
            "why_a_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை; ஆளுநர் SEC-ஐ நியமிக்கிறார், தலைமை நீதிபதி அல்ல.",
            "why_b_en": "Statement 2 is also correct.",
            "why_b_ta": "கூற்று 2-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "why_c_en": "Statement 3 is incorrect.",
            "why_c_ta": "கூற்று 3 தவறானது.",
            "why_d_en": "Statement 3 is incorrect; Chief Justice has no appointment power.",
            "why_d_ta": "கூற்று 3 தவறானது; தலைமை நீதிபதிக்கு நியமன அதிகாரம் இல்லை.",
            "tip_en": "TN SEC was established under statutory and constitutional reforms in 1994.",
            "tip_ta": "1994-ல் சட்டப்பூர்வ மற்றும் அரசியலமைப்பு சீர்திருத்தங்களின் கீழ் TN SEC நிறுவப்பட்டது.",
            "fact_en": "The first statutory local body elections under the new system in Tamil Nadu were conducted in October 1996.",
            "fact_ta": "தமிழ்நாட்டில் புதிய அமைப்பின் கீழ் முதல் சட்டப்பூர்வ உள்ளாட்சித் தேர்தல்கள் அக்டோபர் 1996-ல் நடத்தப்பட்டன."
        },

        # 6
        {
            "subtopic": "State Election Commission - Constitutional Mandate & Provisions (Articles 243K & 243ZA)",
            "stem_en": "Consider the following statements regarding the Supreme Court's ruling in Kishan Singh Tomar v. Municipal Corporation of Ahmedabad (2006):\n1. State Election Commissions enjoy independence on par with the Election Commission of India under Article 324.\n2. State Governments are constitutionally bound to render full assistance and provide necessary staff to the SEC.\n3. The SEC has no power to issue directives to administrative machinery during municipal elections.\nWhich of the statements given above are correct?",
            "stem_ta": "கிஷன் சிங் தோமர் எதிர் அகமதாபாத் மாநகராட்சி (2006) வழக்கில் உச்ச நீதிமன்றத்தின் தீர்ப்பு தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. மாநில தேர்தல் ஆணையங்கள் சரத்து 324-ன் கீழ் இந்திய தேர்தல் ஆணையத்திற்கு இணையான சுதந்திரத்தை அனுபவிக்கின்றன.\n2. SEC-க்கு முழு உதவி செய்யவும் தேவையான பணியாளர்களை வழங்கவும் மாநில அரசுகள் அரசியலமைப்பு ரீதியாக கடமைப்பட்டுள்ளன.\n3. நகராட்சித் தேர்தல்களின் போது நிர்வாக இயந்திரங்களுக்கு உத்தரவுகளைப் பிறப்பிக்க SEC-க்கு எந்த அதிகாரமும் இல்லை.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?",
            "options": [
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("1 and 3 only", "1 மற்றும் 3 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்")
            ],
            "correct_key": "A",
            "exp_en": "Statements 1 and 2 are correct. Statement 3 is incorrect because the Supreme Court explicitly affirmed that the SEC possesses plenary powers of superintendence, direction, and control, including directing administrative machinery during elections.",
            "exp_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் தேர்தலின் போது நிர்வாக இயந்திரங்களை வழிநடத்துவது உட்பட மேற்பார்வை, வழிகாட்டுதல் மற்றும் கட்டுப்பாட்டின் முழுமையான அதிகாரங்களை SEC கொண்டுள்ளது என்று உச்ச நீதிமன்றம் உறுதிப்படுத்தியது.",
            "why_a_en": "Statements 1 and 2 are correct; statement 3 is incorrect.",
            "why_a_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை; கூற்று 3 தவறானது.",
            "why_b_en": "Statement 3 is incorrect.",
            "why_b_ta": "கூற்று 3 தவறானது.",
            "why_c_en": "Statement 1 is also correct while statement 3 is incorrect.",
            "why_c_ta": "கூற்று 1-ம் சரியானது மற்றும் கூற்று 3 தவறானது.",
            "why_d_en": "Statement 3 is incorrect; SEC has plenary control over election machinery.",
            "why_d_ta": "கூற்று 3 தவறானது; தேர்தல் இயந்திரத்தின் மீது SEC-க்கு முழு அதிகாரம் உண்டு.",
            "tip_en": "Kishan Singh Tomar (2006) established constitutional equivalence between SEC and ECI.",
            "tip_ta": "கிஷன் சிங் தோமர் (2006) SEC மற்றும் ECI இடையே அரசியலமைப்பு சமத்துவத்தை நிறுவியது.",
            "fact_en": "The judgment held that Article 243-U mandatory 5-year election deadline cannot be bypassed by state executive inaction.",
            "fact_ta": "சரத்து 243-U கட்டாய 5 ஆண்டு தேர்தல் காலக்கெடுவை மாநில அரசின் செயலற்ற தன்மையால் புறக்கணிக்க முடியாது என்று தீர்ப்பளித்தது."
        },

        # 7
        {
            "subtopic": "State Election Commissioner - Appointment, Tenure, Removal & Autonomy",
            "stem_en": "Consider the following statements regarding the second proviso to Article 243K(2):\n1. The conditions of service of the State Election Commissioner shall not be varied to his disadvantage after his appointment.\n2. The salary of the SEC can be reduced by an ordinary executive notification at any time.\n3. This protection is similar to that provided to High Court Judges under Article 221(2).\nWhich of the statements given above are correct?",
            "stem_ta": "சரத்து 243K(2)-ன் இரண்டாவது வரம்புரை தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. மாநில தேர்தல் ஆணையரின் பணி நிபந்தனைகள் அவரது நியமனத்திற்குப் பிறகு அவருக்கு பாதகமாக மாற்றப்படக் கூடாது.\n2. ஒரு சாதாரண நிர்வாக அறிவிப்பின் மூலம் SEC-ன் ஊதியத்தை எந்த நேரத்திலும் குறைக்க முடியும்.\n3. இந்தப் பாதுகாப்பு சரத்து 221(2)-ன் கீழ் உயர் நீதிமன்ற நீதிபதிகளுக்கு வழங்கப்பட்டுள்ள பாதுகாப்பைப் போன்றதாகும்.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?",
            "options": [
                ("1 and 3 only", "1 மற்றும் 3 மட்டுமே"),
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்")
            ],
            "correct_key": "A",
            "exp_en": "Statements 1 and 3 are correct. Statement 2 is incorrect because the second proviso explicitly protects the SEC's salary and service conditions from being varied to their disadvantage during their tenure.",
            "exp_ta": "கூற்றுகள் 1 மற்றும் 3 சரியானவை. கூற்று 2 தவறானது, ஏனெனில் இரண்டாவது வரம்புரை SEC-ன் ஊதியம் மற்றும் பணி நிபந்தனைகள் அவர்களின் பதவிக்காலத்தில் அவர்களுக்கு பாதகமாக மாற்றப்படுவதிலிருந்து வெளிப்படையாகப் பாதுகாக்கிறது.",
            "why_a_en": "Statements 1 and 3 are correct; statement 2 contradicts the non-diminution guarantee.",
            "why_a_ta": "கூற்றுகள் 1 மற்றும் 3 சரியானவை; கூற்று 2 குறைப்பு செய்யக்கூடாது என்ற உத்தரவாதத்திற்கு எதிரானது.",
            "why_b_en": "Statement 2 is incorrect.",
            "why_b_ta": "கூற்று 2 தவறானது.",
            "why_c_en": "Statement 2 is incorrect while statement 1 is correct.",
            "why_c_ta": "கூற்று 2 தவறானது மற்றும் கூற்று 1 சரியானது.",
            "why_d_en": "Statement 2 is false.",
            "why_d_ta": "கூற்று 2 தவறானது.",
            "tip_en": "Proviso to 243K(2) mirrors Art 221(2) (HC Judges) and Art 324(5) (CEC).",
            "tip_ta": "243K(2)-ன் வரம்புரை சரத்து 221(2) (உயர் நீதிமன்ற நீதிபதிகள்) மற்றும் சரத்து 324(5) (CEC)-ஐப் பிரதிபலிக்கிறது.",
            "fact_en": "In AP SEC case (2020), reducing tenure mid-way was held to be varying conditions of service to disadvantage.",
            "fact_ta": "ஆந்திரா SEC வழக்கில் (2020), பதவிக்காலத்தை பாதியில் குறைப்பது பாதகமான மாற்றமாக கருதப்பட்டது."
        },

        # 8
        {
            "subtopic": "State Finance Commission - Constitutional Mandate, Composition & Role (Articles 243I & 243Y)",
            "stem_en": "Consider the following statements regarding the functions of the State Finance Commission under Article 243-I(1):\n1. It reviews the financial position of the Panchayats.\n2. It recommends the principles governing the distribution between the State and the Panchayats of net proceeds of taxes, duties, tolls, and fees.\n3. It determines the taxes, duties, tolls, and fees which may be assigned to, or appropriated by, the Panchayats.\nWhich of the statements given above are correct?",
            "stem_ta": "சரத்து 243-I(1)-ன் கீழ் மாநில நிதி ஆணையத்தின் பணிகள் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது பஞ்சாயத்துகளின் நிதி நிலையை மறுஆய்வு செய்கிறது.\n2. வரிகள், தீர்வைகள், சுங்கக் கட்டணங்கள் ஆகியவற்றின் நிகர வருவாயை மாநிலத்திற்கும் பஞ்சாயத்துகளுக்கும் இடையே பகிர்ந்தளிப்பதற்கான கொள்கைகளை இது பரிந்துரைக்கிறது.\n3. பஞ்சாயத்துகளுக்கு ஒதுக்கப்படக்கூடிய அல்லது பஞ்சாயத்துகளால் பயன்படுத்தப்படக்கூடிய வரிகள், தீர்வைகள் மற்றும் கட்டணங்களை இது தீர்மானிக்கிறது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?",
            "options": [
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்"),
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1 and 3 only", "1 மற்றும் 3 மட்டுமே")
            ],
            "correct_key": "A",
            "exp_en": "All three statements accurately state the core constitutional responsibilities of the SFC outlined under Article 243-I(1)(a)(i) and (ii).",
            "exp_ta": "மூன்று கூற்றுகளும் சரத்து 243-I(1)(a)(i) மற்றும் (ii)-ன் கீழ் கோடிட்டுக் காட்டப்பட்டுள்ள SFC-ன் முக்கிய அரசியலமைப்புப் பொறுப்புகளை துல்லியமாகக் கூறுகின்றன.",
            "why_a_en": "All three statements accurately reflect Article 243-I(1).",
            "why_a_ta": "மூன்று கூற்றுகளும் சரத்து 243-I(1)-ஐ துல்லியமாகப் பிரதிபலிக்கின்றன.",
            "why_b_en": "Statement 3 is also correct.",
            "why_b_ta": "கூற்று 3-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "why_c_en": "Statement 1 is also correct.",
            "why_c_ta": "கூற்று 1-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "why_d_en": "Statement 2 is also correct.",
            "why_d_ta": "கூற்று 2-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "tip_en": "SFC mandate: Devolution (Sharing), Assignment (Taxes given to local bodies), and Grants-in-aid.",
            "tip_ta": "SFC கட்டளை: பகிர்வு (வரிப் பகிர்வு), ஒதுக்கீடு (உள்ளாட்சி வரிகள்), மற்றும் மானியங்கள்.",
            "fact_en": "SFC also recommends measures to improve the overall financial health of local bodies.",
            "fact_ta": "உள்ளாட்சி அமைப்புகளின் ஒட்டுமொத்த நிதி நிலையை மேம்படுத்துவதற்கான நடவடிக்கைகளையும் SFC பரிந்துரைக்கிறது."
        },

        # 9
        {
            "subtopic": "Financial Devolution, Intergovernmental Transfers & Local Governance",
            "stem_en": "Consider the following statements regarding devolution formulas adopted in Indian States:\n1. 'Vertical devolution' refers to the percentage of State taxes transferred to local bodies as an aggregate pool.\n2. 'Horizontal devolution' refers to the formula by which the aggregate pool is divided among different tiers and individual local bodies.\n3. Population and area are the only factors ever used in horizontal devolution formulas.\nWhich of the statements given above is/are correct?",
            "stem_ta": "இந்திய மாநிலங்களில் பின்பற்றப்படும் நிதிப் பகிர்வு சூத்திரங்கள் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 'செங்குத்துப் பகிர்வு' என்பது ஒரு ஒருங்கிணைந்த தொகுப்பாக உள்ளாட்சி அமைப்புகளுக்கு மாற்றப்படும் மாநில வரிகளின் சதவீதத்தைக் குறிக்கிறது.\n2. 'கிடைமட்டப் பகிர்வு' என்பது வெவ்வேறு அடுக்குகள் மற்றும் தனிப்பட்ட உள்ளாட்சி அமைப்புகளிடையே ஒருங்கிணைந்த நிதி எவ்வாறு பிரிக்கப்படுகிறது என்பதற்கான சூத்திரத்தைக் குறிக்கிறது.\n3. மக்கள் தொகை மற்றும் பரப்பளவு மட்டுமே கிடைமட்டப் பகிர்வு சூத்திரங்களில் எப்போதும் பயன்படுத்தப்படும் காரணிகளாகும்.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
            "options": [
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("1 only", "1 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்")
            ],
            "correct_key": "A",
            "exp_en": "Statements 1 and 2 are correct. Statement 3 is incorrect because SFCs also consider equity indicators, SC/ST population, per capita income distance, infrastructure backwardness, and own-revenue mobilization effort.",
            "exp_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் SFC-கள் சமத்துவக் குறியீடுகள், SC/ST மக்கள் தொகை, தனிநபர் வருமான தூரம், உள்கட்டமைப்பு பின்தங்கிய நிலை மற்றும் சொந்த வருவாய் திரட்டும் முயற்சி ஆகியவற்றையும் கருத்தில் கொள்கின்றன.",
            "why_a_en": "Statements 1 and 2 are correct; statement 3 wrongly claims only population and area are used.",
            "why_a_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை; கூற்று 3 மக்கள் தொகை மற்றும் பரப்பளவு மட்டுமே பயன்படுத்தப்படுகிறது என தவறாகக் கூறுகிறது.",
            "why_b_en": "Statement 2 is also correct.",
            "why_b_ta": "கூற்று 2-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "why_c_en": "Statement 3 is incorrect.",
            "why_c_ta": "கூற்று 3 தவறானது.",
            "why_d_en": "Statement 3 is incorrect.",
            "why_d_ta": "கூற்று 3 தவறானது.",
            "tip_en": "Vertical = State to Local Bodies pool. Horizontal = Distribution among local bodies.",
            "tip_ta": "செங்குத்து = மாநிலத்திலிருந்து உள்ளாட்சி அமைப்புகளுக்கான நிதி. கிடைமட்ட = உள்ளாட்சி அமைப்புகளுக்கு இடையிலான பகிர்வு.",
            "fact_en": "Tamil Nadu allocates roughly 10% of its State's Own Tax Revenue (SOTR) as vertical devolution.",
            "fact_ta": "தமிழ்நாடு தனது சொந்த வரி வருவாயில் (SOTR) சுமார் 10%-ஐ செங்குத்துப் பகிர்வாக ஒதுக்குகிறது."
        },

        # 10
        {
            "subtopic": "Tamil Nadu State Election & Finance Commissions - Legal Framework, Rules & Precedents",
            "stem_en": "Consider the following statements regarding the Sixth State Finance Commission of Tamil Nadu:\n1. It submitted its report with recommendations for the period 2022-2027.\n2. It recommended continuing the devolution ratio between Rural and Urban Local Bodies.\n3. It recommended abolishing all local body property taxes across Tamil Nadu.\nWhich of the statements given above is/are correct?",
            "stem_ta": "தமிழ்நாட்டின் ஆறாவது மாநில நிதி ஆணையம் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது 2022-2027 காலத்திற்கான தனது பரிந்துரைகளுடன் அறிக்கையை சமர்ப்பித்தது.\n2. இது ஊரக மற்றும் நகர்ப்புற உள்ளாட்சி அமைப்புகளுக்கு இடையிலான நிதிப் பகிர்வு விகிதத்தைத் தொடர பரிந்துரைத்தது.\n3. இது தமிழ்நாடு முழுவதும் உள்ள அனைத்து உள்ளாட்சி சொத்து வரிகளையும் ரத்து செய்ய பரிந்துரைத்தது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
            "options": [
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("1 only", "1 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்")
            ],
            "correct_key": "A",
            "exp_en": "Statements 1 and 2 are correct. Statement 3 is incorrect because the SFC recommended strengthening property tax assessments and periodic revisions, not abolishing property tax which is the primary source of own revenue.",
            "exp_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் சொந்த வருவாயின் முதன்மை ஆதாரமான சொத்து வரியை ரத்து செய்வதற்குப் பதிலாக, சொத்து வரி மதிப்பீடுகள் மற்றும் அவ்வப்போதைய திருத்தங்களை வலுப்படுத்தவே SFC பரிந்துரைத்தது.",
            "why_a_en": "Statements 1 and 2 are correct; statement 3 is incorrect.",
            "why_a_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை; கூற்று 3 தவறானது.",
            "why_b_en": "Statement 2 is also correct.",
            "why_b_ta": "கூற்று 2-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "why_c_en": "Statement 3 is incorrect.",
            "why_c_ta": "கூற்று 3 தவறானது.",
            "why_d_en": "Statement 3 is incorrect; property tax was not abolished.",
            "why_d_ta": "கூற்று 3 தவறானது; சொத்து வரி ரத்து செய்யப்படவில்லை.",
            "tip_en": "6th SFC award covers 2022-2027, aligned with 15th FC period.",
            "tip_ta": "6வது SFC விருது காலம் 2022-2027 ஆகும், இது 15வது FC காலத்துடன் ஒத்துப்போகிறது.",
            "fact_en": "Tamil Nadu has constituted six State Finance Commissions since the 73rd/74th amendments.",
            "fact_ta": "73/74வது திருத்தங்களுக்குப் பிறகு தமிழ்நாடு ஆறு மாநில நிதி ஆணையங்களை அமைத்துள்ளது."
        },

        # 11
        {
            "subtopic": "State Election Commission - Constitutional Mandate & Provisions (Articles 243K & 243ZA)",
            "stem_en": "Consider the following statements regarding the constitutional bar on court interference under Article 243-O and 243ZG:\n1. No election to any Panchayat or Municipality shall be called in question except by an election petition.\n2. An election petition must be presented to such authority and in such manner as provided by State law.\n3. High Courts can stall an ongoing election process at any intermediate stage under Article 226 without waiting for polling to finish.\nWhich of the statements given above are correct?",
            "stem_ta": "சரத்துகள் 243-O மற்றும் 243ZG-ன் கீழ் நீதிமன்ற தலையீட்டிற்கான அரசியலமைப்புத் தடை தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. தேர்தல் மனு மூலமாகத் தவிர எந்தவொரு பஞ்சாயத்து அல்லது நகராட்சித் தேர்தலையும் கேள்விக்குள்ளாக்க முடியாது.\n2. மாநில சட்டம் வழங்கும் அத்தகைய அதிகாரியிடம் மற்றும் அத்தகைய முறையில் தேர்தல் மனு சமர்ப்பிக்கப்பட வேண்டும்.\n3. வாக்குப்பதிவு முடியும் வரை காத்திருக்காமல் சரத்து 226-ன் கீழ் எந்த இடைப்பட்ட நிலையிலும் உயர் நீதிமன்றங்கள் நடந்து கொண்டிருக்கும் தேர்தல் செயல்முறையை நிறுத்த முடியும்.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?",
            "options": [
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("1 and 3 only", "1 மற்றும் 3 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்")
            ],
            "correct_key": "A",
            "exp_en": "Statements 1 and 2 are correct. Statement 3 is incorrect because established judicial precedent (Ponnuswami, Ashok Kumar, Kishan Singh Tomar) dictates that courts cannot stall ongoing election processes; challenges are maintainable only via election petition after declaration of results.",
            "exp_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் நிறுவப்பட்ட நீதித்துறை முன்மாதிரிகளின்படி நீதிமன்றங்கள் நடந்து கொண்டிருக்கும் தேர்தல் செயல்முறையை நிறுத்த முடியாது; முடிவுகள் அறிவிக்கப்பட்ட பின்னரே தேர்தல் மனு மூலம் மட்டுமே சவால் செய்ய முடியும்.",
            "why_a_en": "Statements 1 and 2 correctly describe 243-O(b) & 243ZG(b).",
            "why_a_ta": "கூற்றுகள் 1 மற்றும் 2 சரத்துகள் 243-O(b) & 243ZG(b)-ஐ சரியாக விவரிக்கின்றன.",
            "why_b_en": "Statement 3 is incorrect.",
            "why_b_ta": "கூற்று 3 தவறானது.",
            "why_c_en": "Statement 1 is also correct while statement 3 is incorrect.",
            "why_c_ta": "கூற்று 1-ம் சரியானது மற்றும் கூற்று 3 தவறானது.",
            "why_d_en": "Statement 3 is incorrect; courts do not stall midway elections.",
            "why_d_ta": "கூற்று 3 தவறானது; நீதிமன்றங்கள் நடுவழியில் தேர்தல்களை நிறுத்துவதில்லை.",
            "tip_en": "Bar on interference: Challenge ONLY via election petition AFTER elections conclude.",
            "tip_ta": "தலையீட்டிற்கான தடை: தேர்தல் முடிந்த பின்னரே தேர்தல் மனு மூலம் மட்டுமே சவால் செய்ய முடியும்.",
            "fact_en": "Writ jurisdiction under Art 226 can only be invoked in aid of completing elections, not stalling them.",
            "fact_ta": "சரத்து 226-ன் கீழான நீதிப்பேராணை தேர்தலை நடத்துவதற்கு உதவ மட்டுமே பயன்படுத்தப்படலாம், அதை நிறுத்த அல்ல."
        },

        # 12
        {
            "subtopic": "State Election Commissioner - Appointment, Tenure, Removal & Autonomy",
            "stem_en": "Consider the following statements regarding the role of State Election Commissioner in disqualification of members:\n1. Under Article 243F(2) and 243V(2), questions of disqualification are referred to the authority provided by State law.\n2. In several states, the State Election Commission is statutorily designated to hear disqualification matters.\n3. The SEC has the power to pardon any candidate convicted of a serious crime under IPC.\nWhich of the statements given above is/are correct?",
            "stem_ta": "உறுப்பினர்களின் தகுதியிழப்பில் மாநில தேர்தல் ஆணையரின் பங்கு தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. சரத்துகள் 243F(2) மற்றும் 243V(2)-ன் கீழ், தகுதியிழப்பு குறித்த கேள்விகள் மாநில சட்டம் வழங்கும் அதிகாரியிடம் பரிந்துரைக்கப்படுகின்றன.\n2. பல மாநிலங்களில் தகுதியிழப்பு விவகாரங்களை விசாரிக்க மாநில தேர்தல் ஆணையம் சட்டப்பூர்வமாக நியமிக்கப்பட்டுள்ளது.\n3. IPC-ன் கீழ் கடுமையான குற்றத்திற்காக தண்டிக்கப்பட்ட எந்தவொரு வேட்பாளரையும் மன்னிக்கும் அதிகாரம் SEC-க்கு உண்டு.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
            "options": [
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("1 only", "1 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்")
            ],
            "correct_key": "A",
            "exp_en": "Statements 1 and 2 are correct. Statement 3 is incorrect because the pardoning power belongs exclusively to the President (Article 72) and Governor (Article 161); the SEC has no pardoning power.",
            "exp_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் மன்னிக்கும் அதிகாரம் குடியரசுத் தலைவர் (சரத்து 72) மற்றும் ஆளுநருக்கு (சரத்து 161) மட்டுமே உரியது; SEC-க்கு மன்னிக்கும் அதிகாரம் இல்லை.",
            "why_a_en": "Statements 1 and 2 are correct; SEC has no pardoning powers.",
            "why_a_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை; SEC-க்கு மன்னிக்கும் அதிகாரம் இல்லை.",
            "why_b_en": "Statement 2 is also correct.",
            "why_b_ta": "கூற்று 2-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "why_c_en": "Statement 3 is incorrect.",
            "why_c_ta": "கூற்று 3 தவறானது.",
            "why_d_en": "Statement 3 is incorrect; pardoning is an executive prerogative of President/Governor.",
            "why_d_ta": "கூற்று 3 தவறானது; மன்னிப்பு வழங்குவது குடியரசுத் தலைவர்/ஆளுநரின் அதிகாரம்.",
            "tip_en": "Disqualification disputes are referred to the authority specified by State Legislature by law.",
            "tip_ta": "தகுதியிழப்பு சர்ச்சைகள் மாநில சட்டமன்றத்தால் சட்டத்தின் மூலம் குறிப்பிடப்பட்ட அதிகாரியிடம் பரிந்துரைக்கப்படுகின்றன.",
            "fact_en": "In Tamil Nadu, disputes regarding disqualification of panchayat members go to the District Judge.",
            "fact_ta": "தமிழ்நாட்டில் பஞ்சாயத்து உறுப்பினர்களின் தகுதியிழப்பு சர்ச்சைகள் மாவட்ட நீதிபதியிடம் செல்கின்றன."
        },

        # 13
        {
            "subtopic": "State Finance Commission - Constitutional Mandate, Composition & Role (Articles 243I & 243Y)",
            "stem_en": "Consider the following statements regarding the composition and powers of the State Finance Commission:\n1. The State Legislature may, by law, determine the qualifications requisite for appointment as members of the Commission.\n2. State Finance Commissions generally enjoy the powers of a Civil Court under the Code of Civil Procedure, 1908.\n3. The SFC members must all be serving sitting judges of the Supreme Court of India.\nWhich of the statements given above are correct?",
            "stem_ta": "மாநில நிதி ஆணையத்தின் அமைப்பு மற்றும் அதிகாரங்கள் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. ஆணையத்தின் உறுப்பினர்களாக நியமிக்கப்படுவதற்குத் தேவையான தகுதிகளை மாநில சட்டமன்றம் சட்டத்தின் மூலம் தீர்மானிக்கலாம்.\n2. மாநில நிதி ஆணையங்கள் பொதுவாக சிவில் நடைமுறைச் சட்டம் 1908-ன் கீழ் ஒரு சிவில் நீதிமன்றத்தின் அதிகாரங்களை அனுபவிக்கின்றன.\n3. SFC உறுப்பினர்கள் அனைவரும் இந்திய உச்ச நீதிமன்றத்தின் பதவியில் உள்ள நீதிபதிகளாக இருக்க வேண்டும்.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?",
            "options": [
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("1 and 3 only", "1 மற்றும் 3 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்")
            ],
            "correct_key": "A",
            "exp_en": "Statements 1 and 2 are correct. Statement 3 is incorrect because SFC members are usually experts in public finance, economics, administration, or local government, not sitting Supreme Court judges.",
            "exp_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் SFC உறுப்பினர்கள் பொதுவாக பொது நிதி, பொருளாதாரம், நிர்வாகம் அல்லது உள்ளாட்சித் துறையில் நிபுணர்களாக இருப்பார்கள், உச்ச நீதிமன்ற நீதிபதிகள் அல்ல.",
            "why_a_en": "Statements 1 and 2 are correct; statement 3 is incorrect.",
            "why_a_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை; கூற்று 3 தவறானது.",
            "why_b_en": "Statement 3 is incorrect.",
            "why_b_ta": "கூற்று 3 தவறானது.",
            "why_c_en": "Statement 1 is also correct while statement 3 is incorrect.",
            "why_c_ta": "கூற்று 1-ம் சரியானது மற்றும் கூற்று 3 தவறானது.",
            "why_d_en": "Statement 3 is incorrect; SC judges do not serve as SFC members.",
            "why_d_ta": "கூற்று 3 தவறானது; உச்ச நீதிமன்ற நீதிபதிகள் SFC உறுப்பினர்களாக இருப்பதில்லை.",
            "tip_en": "Article 243-I(2) leaves qualification and selection of members to the State Legislature.",
            "tip_ta": "சரத்து 243-I(2) உறுப்பினர்களின் தகுதி மற்றும் தேர்வை மாநில சட்டமன்றத்திடம் விட்டுவிடுகிறது.",
            "fact_en": "Civil court powers enable the SFC to summon witnesses and requisition public records.",
            "fact_ta": "சிவில் நீதிமன்ற அதிகாரங்கள் SFC-க்கு சாட்சிகளை அழைக்கவும் பொது ஆவணங்களைக் கோரவும் உதவுகின்றன."
        },

        # 14
        {
            "subtopic": "Financial Devolution, Intergovernmental Transfers & Local Governance",
            "stem_en": "Consider the following statements regarding the types of grants devolved to local bodies:\n1. 'Untied Grants' can be utilized by local bodies for location-specific civic needs as determined by the local council.\n2. 'Tied Grants' are earmarked for specific national or state priorities such as sanitation, drinking water, and waste management.\n3. The 15th Finance Commission recommended a mix of both untied and tied grants for local self-governments.\nWhich of the statements given above are correct?",
            "stem_ta": "உள்ளாட்சி அமைப்புகளுக்கு வழங்கப்படும் மானியங்களின் வகைகள் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 'கட்டுப்பாடற்ற மானியங்கள்' உள்ளூர் மன்றத்தால் தீர்மானிக்கப்படும் குறிப்பிட்ட குடிமைத் தேவைகளுக்குப் பயன்படுத்தப்படலாம்.\n2. 'நிபந்தனைக்குட்பட்ட மானியங்கள்' சுகாதாரம், குடிநீர் மற்றும் கழிவு மேலாண்மை போன்ற குறிப்பிட்ட முன்னுரிமைகளுக்காக ஒதுக்கப்படுகின்றன.\n3. உள்ளாட்சி அமைப்புகளுக்கு கட்டுப்பாடற்ற மற்றும் நிபந்தனைக்குட்பட்ட மானியங்கள் இரண்டின் கலவையையும் 15வது நிதி ஆணையம் பரிந்துரைத்தது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?",
            "options": [
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்"),
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1 and 3 only", "1 மற்றும் 3 மட்டுமே")
            ],
            "correct_key": "A",
            "exp_en": "All three statements are correct. Untied grants provide local expenditure flexibility, tied grants target core basic services (water and sanitation), and the 15th FC allocated 40% untied and 60% tied grants for rural local bodies.",
            "exp_ta": "மூன்று கூற்றுகளும் சரியானவை. கட்டுப்பாடற்ற மானியங்கள் உள்ளூர் செலவு நெகிழ்வுத்தன்மையை வழங்குகின்றன, நிபந்தனை மானியங்கள் குடிநீர் மற்றும் சுகாதாரத்தை இலக்காகக் கொண்டுள்ளன, மேலும் 15வது FC ஊரக அமைப்புகளுக்கு 40% கட்டுப்பாடற்ற மற்றும் 60% நிபந்தனை மானியங்களை ஒதுக்கியது.",
            "why_a_en": "All three statements accurately characterize local grant typologies.",
            "why_a_ta": "மூன்று கூற்றுகளும் உள்ளாட்சி மானிய வகைகளை துல்லியமாக விவரிக்கின்றன.",
            "why_b_en": "Statement 3 is also correct.",
            "why_b_ta": "கூற்று 3-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "why_c_en": "Statement 1 is also correct.",
            "why_c_ta": "கூற்று 1-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "why_d_en": "Statement 2 is also correct.",
            "why_d_ta": "கூற்று 2-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "tip_en": "Untied = Flexible local autonomy. Tied = Mandatory basic services (WASH).",
            "tip_ta": "கட்டுப்பாடற்றது = நெகிழ்வான உள்ளூர் சுயாட்சி. நிபந்தனை = கட்டாய அடிப்படைச் சேவைகள்.",
            "fact_en": "For Million-Plus urban agglomerations, the 15th FC tied grants focus on ambient air quality and urban water supply.",
            "fact_ta": "பத்து லட்சத்திற்கும் அதிகமான மக்கள் தொகை கொண்ட நகரங்களுக்கு 15வது FC காற்றின் தரம் மற்றும் குடிநீர் விநியோகத்தில் கவனம் செலுத்தியது."
        },

        # 15
        {
            "subtopic": "Tamil Nadu State Election & Finance Commissions - Legal Framework, Rules & Precedents",
            "stem_en": "Consider the following statements regarding the reservation of seats in Tamil Nadu local bodies:\n1. Tamil Nadu amended its municipal and panchayat laws to provide 50% reservation for women in local bodies.\n2. Reservation for Scheduled Castes and Scheduled Tribes is provided in proportion to their population.\n3. The office of Village Panchayat President cannot be reserved for women under Tamil Nadu law.\nWhich of the statements given above is/are correct?",
            "stem_ta": "தமிழ்நாடு உள்ளாட்சி அமைப்புகளில் இடஒதுக்கீடு தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. தமிழ்நாடு தனது நகராட்சி மற்றும் பஞ்சாயத்து சட்டங்களைத் திருத்தி உள்ளாட்சி அமைப்புகளில் பெண்களுக்கு 50% இடஒதுக்கீட்டை வழங்கியது.\n2. பட்டியல் சாதியினர் மற்றும் பழங்குடியினருக்கான இடஒதுக்கீடு அவர்களின் மக்கள் தொகை விகிதத்திற்கு ஏற்ப வழங்கப்படுகிறது.\n3. தமிழ்நாடு சட்டத்தின் கீழ் கிராம பஞ்சாயத்து தலைவர் பதவியை பெண்களுக்கு ஒதுக்க முடியாது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
            "options": [
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("1 only", "1 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்")
            ],
            "correct_key": "A",
            "exp_en": "Statements 1 and 2 are correct. Statement 3 is incorrect because the office of Village Panchayat President is also reserved for women (including SC/ST women) on a rotation basis up to 50%.",
            "exp_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் கிராம பஞ்சாயத்து தலைவர் பதவியும் சுழற்சி முறையில் பெண்களுக்கு (SC/ST பெண்கள் உட்பட) 50% வரை ஒதுக்கப்படுகிறது.",
            "why_a_en": "Statements 1 and 2 are correct; women's reservation covers chairperson posts as well.",
            "why_a_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை; பெண்கள் இடஒதுக்கீடு தலைவர் பதவிகளுக்கும் பொருந்தும்.",
            "why_b_en": "Statement 2 is also correct.",
            "why_b_ta": "கூற்று 2-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "why_c_en": "Statement 3 is incorrect.",
            "why_c_ta": "கூற்று 3 தவறானது.",
            "why_d_en": "Statement 3 is incorrect; president offices are reserved for women.",
            "why_d_ta": "கூற்று 3 தவறானது; தலைவர் பதவிகள் பெண்களுக்கு ஒதுக்கப்படுகின்றன.",
            "tip_en": "Tamil Nadu enhanced women's reservation from 33% to 50% in 2016.",
            "tip_ta": "தமிழ்நாடு 2016-ல் பெண்களுக்கான இடஒதுக்கீட்டை 33%-லிருந்து 50%-ஆக உயர்த்தியது.",
            "fact_en": "The 50% reservation applies to ward members, panchayat presidents, and municipal chairpersons/mayors.",
            "fact_ta": "50% இடஒதுக்கீடு வார்டு உறுப்பினர்கள், பஞ்சாயத்து தலைவர்கள் மற்றும் மேயர்களுக்குப் பொருந்தும்."
        },

        # 16
        {
            "subtopic": "State Election Commission - Constitutional Mandate & Provisions (Articles 243K & 243ZA)",
            "stem_en": "Consider the following statements regarding the preparation of electoral rolls for local bodies:\n1. The State Election Commission is constitutionally empowered to prepare the electoral rolls for Panchayats and Municipalities.\n2. In many states, the SEC adopts the electoral rolls prepared by the Election Commission of India for assembly constituencies as the basis.\n3. The SEC has no constitutional power to conduct ward-wise delimitation or mapping of voters.\nWhich of the statements given above are correct?",
            "stem_ta": "உள்ளாட்சி அமைப்புகளுக்கான வாக்காளர் பட்டியலைத் தயாரிப்பது தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. பஞ்சாயத்துகள் மற்றும் நகராட்சிகளுக்கான வாக்காளர் பட்டியலைத் தயாரிக்க மாநில தேர்தல் ஆணையத்திற்கு அரசியலமைப்பு ரீதியாக அதிகாரம் அளிக்கப்பட்டுள்ளது.\n2. பல மாநிலங்களில் சட்டசபைத் தொகுதிகளுக்காக இந்திய தேர்தல் ஆணையத்தால் தயாரிக்கப்பட்ட வாக்காளர் பட்டியலை SEC அடிப்படையாக ஏற்றுக்கொள்கிறது.\n3. வாக்காளர்களை வார்டு வாரியாகப் பிரிப்பதற்கோ அல்லது வரைபடமாக்குவதற்கோ SEC-க்கு அரசியலமைப்பு அதிகாரம் இல்லை.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?",
            "options": [
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("1 and 3 only", "1 மற்றும் 3 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்")
            ],
            "correct_key": "A",
            "exp_en": "Statements 1 and 2 are correct. Statement 3 is incorrect because the SEC has plenary constitutional and statutory powers under Articles 243K/243ZA to split, reorganize, and map assembly rolls into territorial local body wards.",
            "exp_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் சட்டமன்றப் பட்டியல்களை உள்ளாட்சி வார்டுகளாகப் பிரிக்கவும் வரைபடமாக்கவும் சரத்துகள் 243K/243ZA-ன் கீழ் SEC-க்கு முழு அதிகாரம் உண்டு.",
            "why_a_en": "Statements 1 and 2 are correct; statement 3 is incorrect.",
            "why_a_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை; கூற்று 3 தவறானது.",
            "why_b_en": "Statement 3 is incorrect.",
            "why_b_ta": "கூற்று 3 தவறானது.",
            "why_c_en": "Statement 1 is also correct while statement 3 is incorrect.",
            "why_c_ta": "கூற்று 1-ம் சரியானது மற்றும் கூற்று 3 தவறானது.",
            "why_d_en": "Statement 3 is incorrect; SEC maps rolls into wards.",
            "why_d_ta": "கூற்று 3 தவறானது; வாக்காளர் பட்டியலை வார்டுகளாக SEC பிரிக்கிறது.",
            "tip_en": "ECI rolls serve as the master database, which SEC segregates into panchayat and municipal wards.",
            "tip_ta": "ECI பட்டியல் முதன்மை தரவுத்தளமாக செயல்படுகிறது, அதை SEC உள்ளாட்சி வார்டுகளாக பிரிக்கிறது.",
            "fact_en": "A person registered in the ECI assembly roll within that local area is eligible to be enrolled on the local roll.",
            "fact_ta": "அந்தப் பகுதியில் உள்ள ECI சட்டமன்றப் பட்டியலில் உள்ள நபர் உள்ளாட்சிப் பட்டியலில் சேர தகுதியுடையவர்."
        },

        # 17
        {
            "subtopic": "State Election Commissioner - Appointment, Tenure, Removal & Autonomy",
            "stem_en": "Consider the following statements regarding the landmark case State of Andhra Pradesh v. N. Ramesh Kumar (2020):\n1. An ordinance reducing the SEC's tenure from 5 years to 3 years to unseat the sitting Commissioner was struck down.\n2. The High Court and Supreme Court held that tenure of an incumbent SEC cannot be curtailed indirectly via ordinance.\n3. The court ruled that State Election Commissioners have no constitutional protections against arbitrary removal.\nWhich of the statements given above are correct?",
            "stem_ta": "ஆந்திரப் பிரதேச அரசு எதிர் என். ரமேஷ் குமார் (2020) முக்கிய வழக்கு தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. பதவியில் உள்ள ஆணையரை நீக்குவதற்காக SEC-ன் பதவிக்காலத்தை 5 ஆண்டுகளில் இருந்து 3 ஆண்டுகளாகக் குறைத்த அவசரச் சட்டம் ரத்து செய்யப்பட்டது.\n2. அவசரச் சட்டம் மூலம் பதவியில் உள்ள ஒரு SEC-ன் பதவிக்காலத்தை மறைமுகமாகக் குறைக்க முடியாது என்று உயர் நீதிமன்றமும் உச்ச நீதிமன்றமும் தீர்ப்பளித்தன.\n3. தன்னிச்சையான பணிநீக்கத்திற்கு எதிராக மாநில தேர்தல் ஆணையர்களுக்கு எந்த அரசியலமைப்புப் பாதுகாப்பும் இல்லை என்று நீதிமன்றம் தீர்ப்பளித்தது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?",
            "options": [
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("1 and 3 only", "1 மற்றும் 3 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்")
            ],
            "correct_key": "A",
            "exp_en": "Statements 1 and 2 are correct. Statement 3 is incorrect because the courts firmly upheld that Article 243K(2) grants SECs constitutional insulation identical to High Court judges.",
            "exp_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் சரத்து 243K(2) SEC-க்கு உயர் நீதிமன்ற நீதிபதிகளுக்கு இணையான அரசியலமைப்புப் பாதுகாப்பை வழங்குகிறது என்பதை நீதிமன்றங்கள் உறுதிப்படுத்தின.",
            "why_a_en": "Statements 1 and 2 are correct; statement 3 is contradicted by the judgment.",
            "why_a_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை; கூற்று 3 தீர்ப்பிற்கு எதிரானது.",
            "why_b_en": "Statement 3 is incorrect.",
            "why_b_ta": "கூற்று 3 தவறானது.",
            "why_c_en": "Statement 1 is also correct while statement 3 is incorrect.",
            "why_c_ta": "கூற்று 1-ம் சரியானது மற்றும் கூற்று 3 தவறானது.",
            "why_d_en": "Statement 3 is incorrect; SEC has High Court Judge status protection.",
            "why_d_ta": "கூற்று 3 தவறானது; உயர் நீதிமன்ற நீதிபதி அந்தஸ்து பாதுகாப்பு SEC-க்கு உண்டு.",
            "tip_en": "Ramesh Kumar case (2020) affirmed that ordinance route cannot be used to remove an SEC mid-term.",
            "tip_ta": "ரமேஷ் குமார் வழக்கு (2020) அவசரச் சட்டம் மூலம் SEC-ஐ பதவிக்காலத்தில் நீக்க முடியாது என்பதை உறுதிப்படுத்தியது.",
            "fact_en": "The Commissioner was reinstated with full powers following the Supreme Court's dismissal of the State's appeal.",
            "fact_ta": "மாநில அரசின் மேல்முறையீட்டை உச்ச நீதிமன்றம் தள்ளுபடி செய்ததைத் தொடர்ந்து ஆணையர் மீண்டும் பணியில் அமர்த்தப்பட்டார்."
        },

        # 18
        {
            "subtopic": "State Finance Commission - Constitutional Mandate, Composition & Role (Articles 243I & 243Y)",
            "stem_en": "Consider the following statements regarding the Action Taken Report (ATR) under Article 243-I(4):\n1. The Governor must cause the recommendations and the explanatory memorandum to be laid before the State Legislature.\n2. The explanatory memorandum must explain the action taken on each recommendation of the Commission.\n3. If the State Government rejects any SFC recommendation, it is not required to provide any reasons to the Legislature.\nWhich of the statements given above is/are correct?",
            "stem_ta": "சரத்து 243-I(4)-ன் கீழ் எடுக்கப்பட்ட நடவடிக்கை அறிக்கை (ATR) தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. ஆளுநர் பரிந்துரைகளையும் விளக்கக் குறிப்பையும் மாநில சட்டமன்றத்தின் முன் வைக்கச் செய்ய வேண்டும்.\n2. விளக்கக் குறிப்பானது ஆணையத்தின் ஒவ்வொரு பரிந்துரையின் மீதும் எடுக்கப்பட்ட நடவடிக்கையை விளக்க வேண்டும்.\n3. மாநில அரசு ஏதேனும் ஒரு SFC பரிந்துரையை நிராகரித்தால், அது சட்டமன்றத்திற்கு எந்த காரணங்களையும் தெரிவிக்க வேண்டியதில்லை.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
            "options": [
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("1 only", "1 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்")
            ],
            "correct_key": "A",
            "exp_en": "Statements 1 and 2 are correct. Statement 3 is incorrect because the Explanatory Memorandum must explicitly state reasons for accepting, modifying, or rejecting each recommendation.",
            "exp_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் ஒவ்வொரு பரிந்துரையையும் ஏற்றுக்கொள்வது, மாற்றுவது அல்லது நிராகரிப்பதற்கான காரணங்களை விளக்கக் குறிப்பு வெளிப்படையாகக் குறிப்பிட வேண்டும்.",
            "why_a_en": "Statements 1 and 2 are correct; statement 3 is incorrect.",
            "why_a_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை; கூற்று 3 தவறானது.",
            "why_b_en": "Statement 2 is also correct.",
            "why_b_ta": "கூற்று 2-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "why_c_en": "Statement 3 is incorrect.",
            "why_c_ta": "கூற்று 3 தவறானது.",
            "why_d_en": "Statement 3 is incorrect; reasons for non-acceptance must be provided.",
            "why_d_ta": "கூற்று 3 தவறானது; நிராகரிப்பதற்கான காரணங்கள் தெரிவிக்கப்பட வேண்டும்.",
            "tip_en": "Explanatory memorandum = Action Taken Report (ATR) placed before the State Assembly.",
            "tip_ta": "விளக்கக் குறிப்பு = மாநில சட்டமன்றத்தின் முன் வைக்கப்படும் நடவடிக்கை எடுக்கப்பட்ட அறிக்கை (ATR).",
            "fact_en": "Similar provision exists for the Union Finance Commission under Article 281 in Parliament.",
            "fact_ta": "நாடாளுமன்றத்தில் மத்திய நிதி ஆணையத்திற்கு சரத்து 281-ன் கீழ் இதேபோன்ற விதி உள்ளது."
        },

        # 19
        {
            "subtopic": "Financial Devolution, Intergovernmental Transfers & Local Governance",
            "stem_en": "Consider the following statements regarding Own Source Revenue (OSR) of local bodies:\n1. Property tax on lands and buildings is the largest source of own tax revenue for urban local bodies.\n2. Village Panchayats in Tamil Nadu are empowered to levy house tax, professional tax, and advertisement tax.\n3. Local bodies have the constitutional authority to levy customs duties on international trade.\nWhich of the statements given above are correct?",
            "stem_ta": "உள்ளாட்சி அமைப்புகளின் சொந்த மூல வருவாய் (OSR) தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. நிலங்கள் மற்றும் கட்டிடங்கள் மீதான சொத்து வரி நகர்ப்புற உள்ளாட்சி அமைப்புகளின் சொந்த வரி வருவாயின் மிகப்பெரிய ஆதாரமாகும்.\n2. தமிழ்நாட்டில் உள்ள கிராம பஞ்சாயத்துகள் வீட்டு வரி, தொழில் வரி மற்றும் விளம்பர வரி விதிக்க அதிகாரம் பெற்றுள்ளன.\n3. சர்வதேச வர்த்தகத்தின் மீது சுங்க வரிகளை விதிக்க உள்ளாட்சி அமைப்புகளுக்கு அரசியலமைப்பு அதிகாரம் உள்ளது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?",
            "options": [
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("1 and 3 only", "1 மற்றும் 3 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்")
            ],
            "correct_key": "A",
            "exp_en": "Statements 1 and 2 are correct. Statement 3 is incorrect because customs duties fall exclusively under Entry 83 of the Union List (List I) in the Seventh Schedule and can only be levied by Parliament.",
            "exp_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் சுங்க வரிகள் ஏழாவது அட்டவணையில் உள்ள மத்திய பட்டியலில் (பட்டியல் I, பதிவு 83) மட்டுமே வருகின்றன மற்றும் நாடாளுமன்றத்தால் மட்டுமே விதிக்கப்பட முடியும்.",
            "why_a_en": "Statements 1 and 2 are correct; statement 3 is an exclusive Union subject.",
            "why_a_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை; கூற்று 3 மத்திய அரசின் பிரத்யேகப் பாடமாகும்.",
            "why_b_en": "Statement 3 is incorrect.",
            "why_b_ta": "கூற்று 3 தவறானது.",
            "why_c_en": "Statement 1 is also correct while statement 3 is incorrect.",
            "why_c_ta": "கூற்று 1-ம் சரியானது மற்றும் கூற்று 3 தவறானது.",
            "why_d_en": "Statement 3 is incorrect; local bodies cannot levy customs duties.",
            "why_d_ta": "கூற்று 3 தவறானது; உள்ளாட்சி அமைப்புகள் சுங்க வரி விதிக்க முடியாது.",
            "tip_en": "Local taxes = Property tax, professional tax, user charges. Customs/Income tax = Union List.",
            "tip_ta": "உள்ளாட்சி வரிகள் = சொத்து வரி, தொழில் வரி. சுங்கம்/வருமான வரி = மத்திய பட்டியல்.",
            "fact_en": "House tax is mandatory for Village Panchayats under Section 171 of the Tamil Nadu Panchayats Act 1994.",
            "fact_ta": "1994 தமிழ்நாடு பஞ்சாயத்துகள் சட்டத்தின் பிரிவு 171-ன் கீழ் கிராம பஞ்சாயத்துகளுக்கு வீட்டு வரி கட்டாயமாகும்."
        },

        # 20
        {
            "subtopic": "Tamil Nadu State Election & Finance Commissions - Legal Framework, Rules & Precedents",
            "stem_en": "Consider the following statements regarding the Tamil Nadu Delimitation Commission Act, 2017:\n1. It constituted a dedicated Delimitation Commission for local bodies in Tamil Nadu.\n2. The State Election Commissioner serves as the ex-officio Chairman of the Delimitation Commission.\n3. The Delimitation Commission delimits parliamentary Lok Sabha constituencies in Tamil Nadu.\nWhich of the statements given above is/are correct?",
            "stem_ta": "தமிழ்நாடு மறுவரையறை ஆணையச் சட்டம், 2017 தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது தமிழ்நாட்டில் உள்ளாட்சி அமைப்புகளுக்காக ஒரு பிரத்யேக மறுவரையறை ஆணையத்தை அமைத்தது.\n2. மாநில தேர்தல் ஆணையர் மறுவரையறை ஆணையத்தின் பதவி வழித் தலைவராக பணியாற்றுகிறார்.\n3. இந்த மறுவரையறை ஆணையம் தமிழ்நாட்டில் நாடாளுமன்ற மக்களவைத் தொகுதிகளை மறுவரையறை செய்கிறது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
            "options": [
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("1 only", "1 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்")
            ],
            "correct_key": "A",
            "exp_en": "Statements 1 and 2 are correct. Statement 3 is incorrect because Lok Sabha and Assembly constituencies are delimited exclusively by the Central Delimitation Commission constituted by Parliament under Article 82.",
            "exp_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் மக்களவை மற்றும் சட்டமன்றத் தொகுதிகள் சரத்து 82-ன் கீழ் நாடாளுமன்றத்தால் அமைக்கப்பட்ட மத்திய மறுவரையறை ஆணையத்தால் மட்டுமே மறுவரையறை செய்யப்படுகின்றன.",
            "why_a_en": "Statements 1 and 2 are correct; statement 3 is handled by the Central Delimitation Commission.",
            "why_a_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை; கூற்று 3 மத்திய மறுவரையறை ஆணையத்தால் கையாளப்படுகிறது.",
            "why_b_en": "Statement 2 is also correct.",
            "why_b_ta": "கூற்று 2-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "why_c_en": "Statement 3 is incorrect.",
            "why_c_ta": "கூற்று 3 தவறானது.",
            "why_d_en": "Statement 3 is incorrect; state commission only delimits local body wards.",
            "why_d_ta": "கூற்று 3 தவறானது; மாநில ஆணையம் உள்ளாட்சி வார்டுகளை மட்டுமே மறுவரையறை செய்கிறது.",
            "tip_en": "TN Delimitation Commission = Local body wards only. Central Commission = Lok Sabha & State Assembly.",
            "tip_ta": "TN மறுவரையறை ஆணையம் = உள்ளாட்சி வார்டுகள் மட்டுமே. மத்திய ஆணையம் = மக்களவை மற்றும் சட்டமன்றம்.",
            "fact_en": "The Director of Rural Development and Commissioner of Municipal Administration serve as ex-officio members.",
            "fact_ta": "ஊரக வளர்ச்சி இயக்குநர் மற்றும் நகராட்சி நிர்வாக ஆணையர் பதவி வழி உறுப்பினர்களாக பணியாற்றுகின்றனர்."
        },

        # 21
        {
            "subtopic": "State Election Commission - Constitutional Mandate & Provisions (Articles 243K & 243ZA)",
            "stem_en": "Consider the following statements regarding the duration of local bodies under Article 243-E and Article 243-U:\n1. Every Panchayat and Municipality continues for five years from the date appointed for its first meeting and no longer.\n2. An election to constitute a Panchayat must be completed before the expiry of its duration of five years.\n3. In case of dissolution, elections must be completed within six months from the date of dissolution.\nWhich of the statements given above are correct?",
            "stem_ta": "சரத்துகள் 243-E மற்றும் 243-U-ன் கீழ் உள்ளாட்சி அமைப்புகளின் கால அளவு தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. ஒவ்வொரு பஞ்சாயத்தும் நகராட்சியும் அதன் முதல் கூட்டத்திற்காக நிர்ணயிக்கப்பட்ட தேதியிலிருந்து ஐந்து ஆண்டுகள் வரை மட்டுமே நீடிக்கும்.\n2. ஒரு பஞ்சாயத்தை அமைப்பதற்கான தேர்தல் அதன் ஐந்து ஆண்டு காலம் முடிவதற்குள் முடிக்கப்பட வேண்டும்.\n3. கலைக்கப்பட்டால், கலைக்கப்பட்ட தேதியிலிருந்து ஆறு மாதங்களுக்குள் தேர்தல்கள் முடிக்கப்பட வேண்டும்.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?",
            "options": [
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்"),
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1 and 3 only", "1 மற்றும் 3 மட்டுமே")
            ],
            "correct_key": "A",
            "exp_en": "All three statements are correct under Articles 243-E(1), (3)(a), and (3)(b) (and identical provisions for municipalities under Article 243-U).",
            "exp_ta": "மூன்று கூற்றுகளும் சரத்துகள் 243-E(1), (3)(a) மற்றும் (3)(b) (மற்றும் நகராட்சிகளுக்கான சரத்து 243-U)-ன் கீழ் சரியானவை.",
            "why_a_en": "All statements accurately state the 5-year and 6-month rules under Articles 243-E & 243-U.",
            "why_a_ta": "அனைத்து கூற்றுகளும் சரத்துகள் 243-E & 243-U-ன் கீழ் உள்ள 5 ஆண்டுகள் மற்றும் 6 மாத விதிகளை சரியாகக் கூறுகின்றன.",
            "why_b_en": "Statement 3 is also correct.",
            "why_b_ta": "கூற்று 3-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "why_c_en": "Statement 1 is also correct.",
            "why_c_ta": "கூற்று 1-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "why_d_en": "Statement 2 is also correct.",
            "why_d_ta": "கூற்று 2-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "tip_en": "5 years from first meeting; elections before expiry; within 6 months if dissolved prematurely.",
            "tip_ta": "முதல் கூட்டத்திலிருந்து 5 ஆண்டுகள்; காலாவதியாகும் முன் தேர்தல்; முன்கூட்டியே கலைக்கப்பட்டால் 6 மாதங்களுக்குள்.",
            "fact_en": "If remainder of period is less than 6 months, no election is necessary.",
            "fact_ta": "மீதமுள்ள காலம் 6 மாதங்களுக்கும் குறைவாக இருந்தால் தேர்தல் நடத்த தேவையில்லை."
        },

        # 22
        {
            "subtopic": "State Election Commissioner - Appointment, Tenure, Removal & Autonomy",
            "stem_en": "Consider the following statements regarding the post-tenure restrictions on the State Election Commissioner:\n1. In several states, the SEC is disqualified from further appointment under the State Government upon demitting office.\n2. The SEC can immediately be appointed as a Minister in the State Cabinet without any election.\n3. Independence of the SEC requires institutional insulation from post-retirement executive inducements.\nWhich of the statements given above are correct?",
            "stem_ta": "மாநில தேர்தல் ஆணையரின் பதவிக்காலத்திற்குப் பிந்தைய கட்டுப்பாடுகள் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. பல மாநிலங்களில், பதவியிலிருந்து விலகியவுடன் மாநில அரசின் கீழ் மேலும் எந்தப் பதவியிலும் நியமிக்கப்படுவதற்கு SEC தகுதியற்றவர் ஆகிறார்.\n2. எந்தத் தேர்தலும் இன்றி SEC உடனடியாக மாநில அமைச்சரவையில் அமைச்சராக நியமிக்கப்படலாம்.\n3. SEC-ன் சுதந்திரத்திற்கு ஓய்வுக்குப் பிந்தைய நிர்வாக கவர்ச்சிகளிலிருந்து நிறுவனப் பாதுகாப்பு தேவைப்படுகிறது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?",
            "options": [
                ("1 and 3 only", "1 மற்றும் 3 மட்டுமே"),
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்")
            ],
            "correct_key": "A",
            "exp_en": "Statements 1 and 3 are correct. Statement 2 is incorrect because ministerial appointment requires being elected to the legislature within 6 months, and an SEC cannot be arbitrarily granted ministerial posts.",
            "exp_ta": "கூற்றுகள் 1 மற்றும் 3 சரியானவை. கூற்று 2 தவறானது, ஏனெனில் அமைச்சராக நியமிக்கப்படுவதற்கு 6 மாதங்களுக்குள் சட்டமன்றத்திற்குத் தேர்ந்தெடுக்கப்பட வேண்டும், மேலும் ஒரு SEC தன்னிச்சையாக அமைச்சராக்கப்பட முடியாது.",
            "why_a_en": "Statements 1 and 3 are correct; statement 2 is legally unfounded.",
            "why_a_ta": "கூற்றுகள் 1 மற்றும் 3 சரியானவை; கூற்று 2 சட்டப்படி ஆதாரமற்றது.",
            "why_b_en": "Statement 2 is incorrect.",
            "why_b_ta": "கூற்று 2 தவறானது.",
            "why_c_en": "Statement 1 is also correct while statement 2 is incorrect.",
            "why_c_ta": "கூற்று 1-ம் சரியானது மற்றும் கூற்று 2 தவறானது.",
            "why_d_en": "Statement 2 is incorrect.",
            "why_d_ta": "கூற்று 2 தவறானது.",
            "tip_en": "Post-tenure ban prevents SEC from acting in favor of ruling government during elections.",
            "tip_ta": "பதவிக்குப் பிந்தைய தடை தேர்தலின் போது ஆளும் அரசுக்கு ஆதரவாக SEC செயல்படுவதைத் தடுக்கிறது.",
            "fact_en": "Section 239(3) of Tamil Nadu Panchayats Act 1994 specifies this post-retirement disqualification.",
            "fact_ta": "1994 தமிழ்நாடு பஞ்சாயத்துகள் சட்டத்தின் பிரிவு 239(3) இந்த ஓய்வுக்குப் பிந்தைய தகுதியிழப்பைக் குறிப்பிடுகிறது."
        },

        # 23
        {
            "subtopic": "State Finance Commission - Constitutional Mandate, Composition & Role (Articles 243I & 243Y)",
            "stem_en": "Consider the following statements regarding the synchronization of Finance Commissions:\n1. The 13th, 14th, and 15th Central Finance Commissions urged States to synchronize SFC reports with Central FC award periods.\n2. Delay in submitting SFC reports hampers the Central Finance Commission's ability to assess local body requirements.\n3. The Constitution mandates that Central FC and SFC must be headed by the exact same Chairman.\nWhich of the statements given above are correct?",
            "stem_ta": "நிதி ஆணையங்களின் ஒத்திசைவு தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 13, 14 மற்றும் 15வது மத்திய நிதி ஆணையங்கள் SFC அறிக்கைகளை மத்திய FC விருது காலங்களுடன் ஒத்திசைக்க மாநிலங்களை வலியுறுத்தின.\n2. SFC அறிக்கைகளை சமர்ப்பிப்பதில் ஏற்படும் தாமதம் உள்ளாட்சி தேவைகளை மதிப்பிடும் மத்திய நிதி ஆணையத்தின் திறனை பாதிக்கிறது.\n3. மத்திய FC மற்றும் SFC இரண்டும் ஒரே தலைவரால் வழிநடத்தப்பட வேண்டும் என்று அரசியலமைப்பு கட்டாயப்படுத்துகிறது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?",
            "options": [
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("1 and 3 only", "1 மற்றும் 3 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்")
            ],
            "correct_key": "A",
            "exp_en": "Statements 1 and 2 are correct. Statement 3 is incorrect because Central FC and SFCs are completely separate constitutional bodies constituted under Article 280 and Article 243-I respectively, headed by different persons.",
            "exp_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் மத்திய FC மற்றும் SFC ஆகியவை முறையே சரத்து 280 மற்றும் சரத்து 243-I-ன் கீழ் வெவ்வேறு நபர்களால் வழிநடத்தப்படும் தனித்தனி அரசியலமைப்பு அமைப்புகளாகும்.",
            "why_a_en": "Statements 1 and 2 are correct; statement 3 is false.",
            "why_a_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை; கூற்று 3 தவறானது.",
            "why_b_en": "Statement 3 is incorrect.",
            "why_b_ta": "கூற்று 3 தவறானது.",
            "why_c_en": "Statement 1 is also correct while statement 3 is incorrect.",
            "why_c_ta": "கூற்று 1-ம் சரியானது மற்றும் கூற்று 3 தவறானது.",
            "why_d_en": "Statement 3 is incorrect; they have distinct chairpersons.",
            "why_d_ta": "கூற்று 3 தவறானது; அவை தனித்தனி தலைவர்களைக் கொண்டுள்ளன.",
            "tip_en": "Synchronization improves data flow under Article 280(3)(bb) & (c).",
            "tip_ta": "ஒத்திசைவு சரத்து 280(3)(bb) & (c)-ன் கீழ் தரவுப் பகிர்வை மேம்படுத்துகிறது.",
            "fact_en": "Several states experienced delays of several years in constituting their SFCs.",
            "fact_ta": "பல மாநிலங்கள் தங்கள் SFC-களை அமைப்பதில் பல ஆண்டுகள் தாமதத்தை சந்தித்தன."
        },

        # 24
        {
            "subtopic": "Financial Devolution, Intergovernmental Transfers & Local Governance",
            "stem_en": "Consider the following statements regarding the financial accountability of Panchayati Raj Institutions:\n1. Article 243J empowers the State Legislature to make provisions with respect to maintenance and auditing of Panchayat accounts.\n2. Local Fund Audit Department conducts statutory audits of local bodies in many States.\n3. The Comptroller and Auditor General (CAG) provides Technical Guidance and Supervision (TG&S) to local fund audit.\nWhich of the statements given above are correct?",
            "stem_ta": "பஞ்சாயத்து ராஜ் நிறுவனங்களின் நிதிப் பொறுப்புடைமை தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. பஞ்சாயத்துக் கணக்குகளைப் பராமரித்தல் மற்றும் தணிக்கை செய்வது தொடர்பாக விதிகளை உருவாக்க சரத்து 243J மாநில சட்டமன்றத்திற்கு அதிகாரம் அளிக்கிறது.\n2. பல மாநிலங்களில் உள்ளாட்சி நிதித் தணிக்கைத் துறை உள்ளாட்சி அமைப்புகளின் சட்டப்பூர்வ தணிக்கைகளை நடத்துகிறது.\n3. இந்திய தலைமை கணக்குத் தணிக்கையாளர் (CAG) உள்ளாட்சி நிதித் தணிக்கைக்கு தொழில்நுட்ப வழிகாட்டுதல் மற்றும் மேற்பார்வையை (TG&S) வழங்குகிறார்.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?",
            "options": [
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்"),
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1 and 3 only", "1 மற்றும் 3 மட்டுமே")
            ],
            "correct_key": "A",
            "exp_en": "All three statements are correct. Article 243J vests legislative power regarding audits; Local Fund Audit conducts state-level audits, and the CAG exercises TG&S over local fund accounting standards.",
            "exp_ta": "மூன்று கூற்றுகளும் சரியானவை. சரத்து 243J தணிக்கை தொடர்பான சட்ட அதிகாரத்தை வழங்குகிறது; உள்ளாட்சி நிதித் தணிக்கைத் துறை தணிக்கைகளை நடத்துகிறது மற்றும் CAG தொழில்நுட்ப வழிகாட்டுதல் மற்றும் மேற்பார்வையை (TG&S) வழங்குகிறது.",
            "why_a_en": "All three statements accurately summarize the audit architecture.",
            "why_a_ta": "மூன்று கூற்றுகளும் தணிக்கைக் கட்டமைப்பை துல்லியமாக சுருக்கமாகக் கூறுகின்றன.",
            "why_b_en": "Statement 3 is also correct.",
            "why_b_ta": "கூற்று 3-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "why_c_en": "Statement 1 is also correct.",
            "why_c_ta": "கூற்று 1-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "why_d_en": "Statement 2 is also correct.",
            "why_d_ta": "கூற்று 2-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "tip_en": "Art 243J = Panchayats audit. Art 243Z = Municipalities audit. CAG provides TG&S.",
            "tip_ta": "சரத்து 243J = பஞ்சாயத்து தணிக்கை. சரத்து 243Z = நகராட்சி தணிக்கை. CAG TG&S வழங்குகிறது.",
            "fact_en": "AuditOnline platform was launched by MoPR to facilitate 100% online auditing of panchayats.",
            "fact_ta": "பஞ்சாயத்துகளின் 100% ஆன்லைன் தணிக்கையை எளிதாக்க MoPR ஆல் AuditOnline தளம் தொடங்கப்பட்டது."
        },

        # 25
        {
            "subtopic": "Tamil Nadu State Election & Finance Commissions - Legal Framework, Rules & Precedents",
            "stem_en": "Consider the following statements regarding the Tamil Nadu Panchayats Act, 1994:\n1. Section 239 provides for the appointment of the State Election Commissioner.\n2. Section 240 provides for the constitution of the State Finance Commission.\n3. Section 241 specifies the powers of the State Finance Commission.\nWhich of the statements given above are correct?",
            "stem_ta": "1994 தமிழ்நாடு பஞ்சாயத்துகள் சட்டம் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. பிரிவு 239 மாநில தேர்தல் ஆணையர் நியமனம் பற்றி கூறுகிறது.\n2. பிரிவு 240 மாநில நிதி ஆணையத்தை அமைப்பது பற்றி கூறுகிறது.\n3. பிரிவு 241 மாநில நிதி ஆணையத்தின் அதிகாரங்களைக் குறிப்பிடுகிறது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?",
            "options": [
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்"),
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1 and 3 only", "1 மற்றும் 3 மட்டுமே")
            ],
            "correct_key": "A",
            "exp_en": "All three statements are correct. Sections 239, 240, and 241 of the Tamil Nadu Panchayats Act 1994 are the specific statutory provisions operationalizing Articles 243K and 243-I in Tamil Nadu.",
            "exp_ta": "மூன்று கூற்றுகளும் சரியானவை. 1994 தமிழ்நாடு பஞ்சாயத்துகள் சட்டத்தின் பிரிவுகள் 239, 240 மற்றும் 241 தமிழ்நாட்டில் சரத்துகள் 243K மற்றும் 243-I-ஐ செயல்படுத்தும் குறிப்பிட்ட சட்ட விதிகளாகும்.",
            "why_a_en": "All three sections match the statutory framework of TN Panchayats Act 1994.",
            "why_a_ta": "மூன்று பிரிவுகளும் 1994 TN பஞ்சாயத்துகள் சட்டத்தின் சட்டக் கட்டமைப்போடு ஒத்துப்போகின்றன.",
            "why_b_en": "Statement 3 is also correct.",
            "why_b_ta": "கூற்று 3-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "why_c_en": "Statement 1 is also correct.",
            "why_c_ta": "கூற்று 1-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "why_d_en": "Statement 2 is also correct.",
            "why_d_ta": "கூற்று 2-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "tip_en": "TN Panchayats Act 1994: Sec 239 = SEC; Sec 240 = SFC; Sec 241 = SFC powers.",
            "tip_ta": "TN பஞ்சாயத்துகள் சட்டம் 1994: பிரிவு 239 = SEC; பிரிவு 240 = SFC; பிரிவு 241 = SFC அதிகாரங்கள்.",
            "fact_en": "These sections were enacted to bring state laws in conformity with Part IX of the Constitution.",
            "fact_ta": "அரசியலமைப்பின் பகுதி IX-க்கு ஏற்ப மாநில சட்டங்களைக் கொண்டு வர இந்த பிரிவுகள் இயற்றப்பட்டன."
        },

        # 26
        {
            "subtopic": "State Election Commission - Constitutional Mandate & Provisions (Articles 243K & 243ZA)",
            "stem_en": "Consider the following statements regarding the disqualification of candidates under Article 243F and 243V:\n1. A person disqualified under any law for the time being in force for the purposes of elections to the State Legislature is disqualified for local bodies.\n2. No person shall be disqualified on the ground that he is less than 25 years of age, if he has attained the age of 21 years.\n3. The minimum age to contest local body elections is 18 years.\nWhich of the statements given above is/are correct?",
            "stem_ta": "சரத்துகள் 243F மற்றும் 243V-ன் கீழ் வேட்பாளர்களின் தகுதியிழப்பு தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. மாநில சட்டமன்றத் தேர்தல்களின் நோக்கங்களுக்காக நடைமுறையில் உள்ள எந்தவொரு சட்டத்தின் கீழும் தகுதி நீக்கம் செய்யப்பட்ட ஒருவர் உள்ளாட்சி அமைப்புகளுக்கும் தகுதியற்றவர் ஆவார்.\n2. ஒருவர் 21 வயதை அடைந்திருந்தால், அவர் 25 வயதுக்குக் குறைவானவர் என்ற காரணத்திற்காக தகுதி நீக்கம் செய்யப்பட மாட்டார்.\n3. உள்ளாட்சித் தேர்தலில் போட்டியிடுவதற்கான குறைந்தபட்ச வயது 18 ஆண்டுகள் ஆகும்.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
            "options": [
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("1 only", "1 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்")
            ],
            "correct_key": "A",
            "exp_en": "Statements 1 and 2 are correct under the explicit proviso to Article 243F(1)(a) and 243V(1)(a). Statement 3 is incorrect because 18 years is the voting age (elector eligibility), whereas 21 years is the minimum age to contest an election.",
            "exp_ta": "சரத்துகள் 243F(1)(a) மற்றும் 243V(1)(a)-ன் வரம்புரையின் கீழ் கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் 18 வயது என்பது வாக்களிக்கும் வயது, தேர்தலில் போட்டியிடுவதற்கான குறைந்தபட்ச வயது 21 ஆண்டுகள் ஆகும்.",
            "why_a_en": "Statements 1 and 2 are correct; minimum age to contest is 21, not 18.",
            "why_a_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை; போட்டியிட குறைந்தபட்ச வயது 21, 18 அல்ல.",
            "why_b_en": "Statement 2 is also correct.",
            "why_b_ta": "கூற்று 2-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "why_c_en": "Statement 3 is incorrect.",
            "why_c_ta": "கூற்று 3 தவறானது.",
            "why_d_en": "Statement 3 is incorrect; 18 is voting age, 21 is contesting age.",
            "why_d_ta": "கூற்று 3 தவறானது; 18 வாக்களிக்கும் வயது, 21 போட்டியிடும் வயது.",
            "tip_en": "Contesting age: MPs/MLAs = 25 years. Local bodies = 21 years. Voting age for all = 18 years.",
            "tip_ta": "போட்டியிடும் வயது: எம்.பி./எம்.எல்.ஏ. = 25 வயது. உள்ளாட்சி = 21 வயது. வாக்களிக்கும் வயது = 18 வயது.",
            "fact_en": "This 21-year exception enables greater youth participation in grassroots democracy.",
            "fact_ta": "இந்த 21 வயது விதிவிலக்கு அடிமட்ட ஜனநாயகத்தில் இளைஞர்களின் அதிக பங்கேற்பை செயல்படுத்துகிறது."
        },

        # 27
        {
            "subtopic": "State Election Commissioner - Appointment, Tenure, Removal & Autonomy",
            "stem_en": "Consider the following statements regarding the role of Returning Officers in local body elections:\n1. Returning Officers are designated or nominated by the State Election Commission.\n2. Returning Officers scrutinize nomination papers and decide on their acceptance or rejection.\n3. A Returning Officer's decision to reject a nomination paper can be immediately stayed by a Civil Judge prior to polling.\nWhich of the statements given above is/are correct?",
            "stem_ta": "உள்ளாட்சித் தேர்தல்களில் தேர்தல் நடத்தும் அதிகாரிகளின் (Returning Officers) பங்கு தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. தேர்தல் நடத்தும் அதிகாரிகள் மாநில தேர்தல் ஆணையத்தால் நியமிக்கப்படுகிறார்கள் அல்லது பரிந்துரைக்கப்படுகிறார்கள்.\n2. தேர்தல் நடத்தும் அதிகாரிகள் வேட்புமனுக்களை ஆய்வு செய்து அவற்றை ஏற்பது அல்லது நிராகரிப்பது குறித்து முடிவெடுக்கிறார்கள்.\n3. வேட்புமனுவை நிராகரிக்கும் தேர்தல் நடத்தும் அதிகாரியின் முடிவை வாக்கெடுப்புக்கு முன்னதாக ஒரு சிவில் நீதிபதியால் உடனடியாக நிறுத்தி வைக்க முடியும்.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
            "options": [
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("1 only", "1 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்")
            ],
            "correct_key": "A",
            "exp_en": "Statements 1 and 2 are correct. Statement 3 is incorrect because under Article 243-O and settled jurisprudence (NP Ponnuswami), civil courts have no jurisdiction to stall elections or stay returning officer decisions midway; challenges lie exclusively via election petition after polls.",
            "exp_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் சரத்து 243-O மற்றும் பொன்னுசாமி வழக்கின்படி தேர்தலை நடுவழியில் நிறுத்தவோ அல்லது RO முடிவை தடையாணை மூலம் நிறுத்தவோ சிவில் நீதிமன்றங்களுக்கு அதிகாரம் இல்லை; தேர்தலுக்குப் பின் தேர்தல் மனு மட்டுமே வழி.",
            "why_a_en": "Statements 1 and 2 are correct; statement 3 violates the constitutional bar on court interference.",
            "why_a_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை; கூற்று 3 நீதிமன்ற தலையீட்டிற்கான அரசியலமைப்புத் தடையை மீறுகிறது.",
            "why_b_en": "Statement 2 is also correct.",
            "why_b_ta": "கூற்று 2-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "why_c_en": "Statement 3 is incorrect.",
            "why_c_ta": "கூற்று 3 தவறானது.",
            "why_d_en": "Statement 3 is incorrect; no mid-election stays allowed.",
            "why_d_ta": "கூற்று 3 தவறானது; தேர்தல் நடுவழியில் தடைகள் அனுமதிக்கப்படாது.",
            "tip_en": "Ponnuswami principle: Returning officer's rejection of nomination can only be questioned in an election petition.",
            "tip_ta": "பொன்னுசாமி கொள்கை: வேட்புமனு நிராகரிப்பை தேர்தல் மனுவில் மட்டுமே கேள்வி கேட்க முடியும்.",
            "fact_en": "District Collectors typically serve as District Election Officers coordinating Returning Officers across blocks.",
            "fact_ta": "மாவட்ட ஆட்சியர்கள் பொதுவாக தேர்தல் நடத்தும் அதிகாரிகளை ஒருங்கிணைக்கும் மாவட்ட தேர்தல் அதிகாரிகளாக செயல்படுகிறார்கள்."
        },

        # 28
        {
            "subtopic": "State Finance Commission - Constitutional Mandate, Composition & Role (Articles 243I & 243Y)",
            "stem_en": "Consider the following statements regarding the criteria for determining grants-in-aid under Article 243-I(1)(a)(iii):\n1. The SFC recommends the principles that govern the grants-in-aid to the Panchayats from the Consolidated Fund of the State.\n2. These grants assist Panchayats in bridging fiscal deficits arising from statutory civic duties.\n3. Grants-in-aid must be repaid with compound interest by the Panchayats to the State Treasury.\nWhich of the statements given above are correct?",
            "stem_ta": "சரத்து 243-I(1)(a)(iii)-ன் கீழ் உதவி மானியங்களை (grants-in-aid) தீர்மானிப்பதற்கான அளவுகோல்கள் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. மாநிலத்தின் தொகுப்பு நிதியிலிருந்து பஞ்சாயத்துகளுக்கு வழங்கப்படும் உதவி மானியங்களை நிர்வகிக்கும் கொள்கைகளை SFC பரிந்துரைக்கிறது.\n2. சட்டப்பூர்வ குடிமைப் பணிகளால் ஏற்படும் நிதிப் பற்றாக்குறையைக் குறைக்க இந்த மானியங்கள் பஞ்சாயத்துகளுக்கு உதவுகின்றன.\n3. உதவி மானியங்களை பஞ்சாயத்துகள் மாநில கருவூலத்திற்கு கூட்டு வட்டியுடன் திருப்பிச் செலுத்த வேண்டும்.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?",
            "options": [
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("1 and 3 only", "1 மற்றும் 3 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்")
            ],
            "correct_key": "A",
            "exp_en": "Statements 1 and 2 are correct. Statement 3 is incorrect because grants-in-aid are non-repayable transfers from the Consolidated Fund of the State, not loans.",
            "exp_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் உதவி மானியங்கள் மாநில தொகுப்பு நிதியிலிருந்து திருப்பிச் செலுத்தத் தேவையில்லாத நிதி மாற்றங்கள், கடன்கள் அல்ல.",
            "why_a_en": "Statements 1 and 2 are correct; grants are non-repayable.",
            "why_a_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை; மானியங்கள் திருப்பிச் செலுத்தத் தேவையில்லாதவை.",
            "why_b_en": "Statement 3 is incorrect.",
            "why_b_ta": "கூற்று 3 தவறானது.",
            "why_c_en": "Statement 1 is also correct while statement 3 is incorrect.",
            "why_c_ta": "கூற்று 1-ம் சரியானது மற்றும் கூற்று 3 தவறானது.",
            "why_d_en": "Statement 3 is incorrect; grants are not loans with compound interest.",
            "why_d_ta": "கூற்று 3 தவறானது; மானியங்கள் கூட்டு வட்டிக் கடன்கள் அல்ல.",
            "tip_en": "Grants-in-aid = Non-repayable fiscal transfers to support local service delivery.",
            "tip_ta": "உதவி மானியங்கள் = உள்ளூர் சேவை வழங்கலை ஆதரிக்கும் திருப்பிச் செலுத்தத் தேவையில்லாத நிதிப் பகிர்வுகள்.",
            "fact_en": "Article 243Y(1)(a)(ii) provides identical grants-in-aid provisions for Municipalities.",
            "fact_ta": "சரத்து 243Y(1)(a)(ii) நகராட்சிகளுக்கும் இதேபோன்ற உதவி மானிய விதிகளை வழங்குகிறது."
        },

        # 29
        {
            "subtopic": "Financial Devolution, Intergovernmental Transfers & Local Governance",
            "stem_en": "Consider the following statements regarding the 14th Finance Commission recommendations on local bodies:\n1. It significantly increased local body grant allocations compared to previous commissions.\n2. It recommended dividing grants into basic grants (90% for rural, 80% for urban) and performance grants (10% for rural, 20% for urban).\n3. It recommended abolishing all municipal corporations in India.\nWhich of the statements given above is/are correct?",
            "stem_ta": "உள்ளாட்சி அமைப்புகள் குறித்த 14வது நிதி ஆணையத்தின் பரிந்துரைகள் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது முந்தைய ஆணையங்களுடன் ஒப்பிடும்போது உள்ளாட்சி மானிய ஒதுக்கீட்டை கணிசமாக உயர்த்தியது.\n2. இது மானியங்களை அடிப்படை மானியங்கள் (ஊரகத்திற்கு 90%, நகர்ப்புறத்திற்கு 80%) மற்றும் செயல்திறன் மானியங்கள் (ஊரகத்திற்கு 10%, நகர்ப்புறத்திற்கு 20%) என பிரிக்க பரிந்துரைத்தது.\n3. இது இந்தியாவில் உள்ள அனைத்து மாநகராட்சிகளையும் கலைக்க பரிந்துரைத்தது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
            "options": [
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("1 only", "1 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்")
            ],
            "correct_key": "A",
            "exp_en": "Statements 1 and 2 are correct. Statement 3 is incorrect because the 14th FC sought to empower urban local bodies, allocating over Rs. 87,000 crores to municipalities and corporations.",
            "exp_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் 14வது FC நகர்ப்புற உள்ளாட்சி அமைப்புகளை வலுப்படுத்த முற்பட்டது மற்றும் நகராட்சிகள் மற்றும் மாநகராட்சிகளுக்கு ரூ. 87,000 கோடிக்கு மேல் ஒதுக்கியது.",
            "why_a_en": "Statements 1 and 2 correctly outline 14th FC local body architecture.",
            "why_a_ta": "கூற்றுகள் 1 மற்றும் 2 14வது FC உள்ளாட்சி கட்டமைப்பை சரியாகக் கோடிட்டுக் காட்டுகின்றன.",
            "why_b_en": "Statement 2 is also correct.",
            "why_b_ta": "கூற்று 2-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "why_c_en": "Statement 3 is incorrect.",
            "why_c_ta": "கூற்று 3 தவறானது.",
            "why_d_en": "Statement 3 is incorrect; municipal corporations were empowered, not abolished.",
            "why_d_ta": "கூற்று 3 தவறானது; மாநகராட்சிகள் வலுப்படுத்தப்பட்டன, கலைக்கப்படவில்லை.",
            "tip_en": "14th FC introduced the 90:10 (rural) and 80:20 (urban) basic vs performance grant formula.",
            "tip_ta": "14வது FC அடிப்படை மற்றும் செயல்திறன் மானியங்களுக்கு 90:10 (ஊரகம்) மற்றும் 80:20 (நகர்ப்புறம்) சூத்திரத்தை அறிமுகப்படுத்தியது.",
            "fact_en": "Total grants allocated to local bodies under 14th FC exceeded Rs. 2.87 lakh crore.",
            "fact_ta": "14வது FC-ன் கீழ் உள்ளாட்சி அமைப்புகளுக்கு ஒதுக்கப்பட்ட மொத்த மானியம் ரூ. 2.87 லட்சம் கோடியைத் தாண்டியது."
        },

        # 30
        {
            "subtopic": "Tamil Nadu State Election & Finance Commissions - Legal Framework, Rules & Precedents",
            "stem_en": "Consider the following statements regarding the election of Mayors of Municipal Corporations in Tamil Nadu:\n1. The system of electing Mayors has alternated between direct election by voters and indirect election by councillors.\n2. Under current statutory rules, Mayors are elected indirectly from among the elected councillors.\n3. The Mayor is appointed directly by the Union Home Minister without any local election.\nWhich of the statements given above are correct?",
            "stem_ta": "தமிழ்நாட்டில் மாநகராட்சி மேயர்கள் தேர்தல் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. மேயர்களைத் தேர்ந்தெடுக்கும் முறை வாக்காளர்களால் நேரடித் தேர்தல் மற்றும் கவுன்சிலர்களால் மறைமுகத் தேர்தல் ஆகியவற்றுக்கு இடையே மாறி மாறி வந்துள்ளது.\n2. தற்போதைய சட்ட விதிகளின் கீழ், தேர்ந்தெடுக்கப்பட்ட கவுன்சிலர்களிடையே இருந்து மேயர்கள் மறைமுகமாகத் தேர்ந்தெடுக்கப்படுகிறார்கள்.\n3. எந்தவொரு உள்ளூர் தேர்தலும் இன்றி மத்திய உள்துறை அமைச்சரால் மேயர் நேரடியாக நியமிக்கப்படுகிறார்.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?",
            "options": [
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("1 and 3 only", "1 மற்றும் 3 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்")
            ],
            "correct_key": "A",
            "exp_en": "Statements 1 and 2 are correct. Statement 3 is incorrect because Mayors in India are never appointed by the Union Home Minister; they are elected representatives governed by state municipal acts.",
            "exp_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் இந்தியாவில் மேயர்கள் ஒருபோதும் மத்திய உள்துறை அமைச்சரால் நியமிக்கப்படுவதில்லை; அவர்கள் மாநில நகராட்சிச் சட்டங்களால் நிர்வகிக்கப்படும் தேர்ந்தெடுக்கப்பட்ட பிரதிநிதிகள்.",
            "why_a_en": "Statements 1 and 2 are correct; statement 3 is incorrect.",
            "why_a_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை; கூற்று 3 தவறானது.",
            "why_b_en": "Statement 3 is incorrect.",
            "why_b_ta": "கூற்று 3 தவறானது.",
            "why_c_en": "Statement 1 is also correct while statement 3 is incorrect.",
            "why_c_ta": "கூற்று 1-ம் சரியானது மற்றும் கூற்று 3 தவறானது.",
            "why_d_en": "Statement 3 is incorrect; Mayors are elected, not appointed by Union Minister.",
            "why_d_ta": "கூற்று 3 தவறானது; மேயர்கள் தேர்ந்தெடுக்கப்படுகிறார்கள், மத்திய அமைச்சரால் நியமிக்கப்படுவதில்லை.",
            "tip_en": "Tamil Nadu has used both direct (1996, 2006) and indirect (2001, 2011, 2022) systems for Mayors.",
            "tip_ta": "தமிழ்நாடு மேயர்களுக்கு நேரடி (1996, 2006) மற்றும் மறைமுக (2001, 2011, 2022) முறைகள் இரண்டையும் பயன்படுத்தியுள்ளது.",
            "fact_en": "Article 243R(2)(b) leaves the manner of election of chairperson of a Municipality to the State Legislature.",
            "fact_ta": "சரத்து 243R(2)(b) நகராட்சித் தலைவரைத் தேர்ந்தெடுக்கும் முறையை மாநில சட்டமன்றத்திடம் விட்டுவிடுகிறது."
        },

        # 31
        {
            "subtopic": "State Election Commission - Constitutional Mandate & Provisions (Articles 243K & 243ZA)",
            "stem_en": "Consider the following statements regarding the powers of the State Election Commission during an election:\n1. The SEC can issue directions to prevent misuse of official machinery by ministers.\n2. All officers and staff deployed for election duty are subject to the superintendence and discipline of the SEC.\n3. The SEC can order repolls in specific polling stations if booth capturing or ballot tampering occurs.\nWhich of the statements given above are correct?",
            "stem_ta": "தேர்தலின் போது மாநில தேர்தல் ஆணையத்தின் அதிகாரங்கள் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. அமைச்சர்கள் உத்தியோகபூர்வ இயந்திரங்களை தவறாகப் பயன்படுத்துவதைத் தடுக்க SEC வழிகாட்டுதல்களை வழங்க முடியும்.\n2. தேர்தல் பணிக்காக நியமிக்கப்பட்ட அனைத்து அதிகாரிகள் மற்றும் ஊழியர்கள் SEC-ன் மேற்பார்வை மற்றும் ஒழுங்குமுறைக்கு உட்பட்டவர்கள்.\n3. வாக்குச்சாவடி கைப்பற்றப்படுதல் அல்லது வாக்குச்சீட்டு முறைகேடுகள் நடந்தால் குறிப்பிட்ட வாக்குச்சாவடிகளில் மறுவாக்குப்பதிவுக்கு SEC உத்தரவிடலாம்.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?",
            "options": [
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்"),
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1 and 3 only", "1 மற்றும் 3 மட்டுமே")
            ],
            "correct_key": "A",
            "exp_en": "All three statements are correct. Articles 243K and 243ZA vest full superintendence, direction, and control in the SEC, granting regulatory control over deputed personnel, enforcement of the Model Code, and ordering repolls.",
            "exp_ta": "மூன்று கூற்றுகளும் சரியானவை. சரத்துகள் 243K மற்றும் 243ZA முழு மேற்பார்வை, வழிகாட்டுதல் மற்றும் கட்டுப்பாட்டை SEC-யிடம் வழங்குகின்றன, இது அயல்பணி ஊழியர்கள் மீதான ஒழுங்குமுறை கட்டுப்பாடு, நடத்தை விதிகளின் அமலாக்கம் மற்றும் மறுவாக்குப்பதிவு உத்தரவு ஆகியவற்றை செயல்படுத்துகிறது.",
            "why_a_en": "All three statements correctly describe SEC powers.",
            "why_a_ta": "மூன்று கூற்றுகளும் SEC அதிகாரங்களை சரியாக விவரிக்கின்றன.",
            "why_b_en": "Statement 3 is also correct.",
            "why_b_ta": "கூற்று 3-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "why_c_en": "Statement 1 is also correct.",
            "why_c_ta": "கூற்று 1-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "why_d_en": "Statement 2 is also correct.",
            "why_d_ta": "கூற்று 2-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "tip_en": "SEC powers mirror ECI under Article 324 during the election period.",
            "tip_ta": "தேர்தல் காலத்தில் SEC அதிகாரங்கள் சரத்து 324-ன் கீழ் ECI அதிகாரங்களைப் போன்றது.",
            "fact_en": "Deputed state police personnel are deemed to be on deputation to the SEC during local elections.",
            "fact_ta": "உள்ளாட்சித் தேர்தலின் போது பணியில் உள்ள காவல்துறையினர் SEC-க்கு அயல்பணியில் இருப்பதாகக் கருதப்படுகிறார்கள்."
        },

        # 32
        {
            "subtopic": "State Election Commissioner - Appointment, Tenure, Removal & Autonomy",
            "stem_en": "Consider the following statements regarding the removal procedure for a State Election Commissioner:\n1. A resolution for removal must be passed by each House of Parliament by a special majority.\n2. The grounds for removal are 'proved misbehaviour or incapacity'.\n3. The Governor can remove the SEC solely upon receiving a petition from the State Cabinet.\nWhich of the statements given above are correct?",
            "stem_ta": "மாநில தேர்தல் ஆணையரை நீக்கும் நடைமுறை தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. பதவி நீக்கத்திற்கான தீர்மானம் நாடாளுமன்றத்தின் ஒவ்வொரு அவையிலும் சிறப்புப் பெரும்பான்மையுடன் நிறைவேற்றப்பட வேண்டும்.\n2. நீக்கத்திற்கான அடிப்படைகள் 'நிரூபிக்கப்பட்ட தவறான நடத்தை அல்லது திறமையின்மை' ஆகும்.\n3. மாநில அமைச்சரவையிடமிருந்து மனுவைப் பெற்றவுடன் மட்டுமே ஆளுநரால் SEC-ஐ நீக்க முடியும்.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?",
            "options": [
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("1 and 3 only", "1 மற்றும் 3 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்")
            ],
            "correct_key": "A",
            "exp_en": "Statements 1 and 2 are correct under Article 243K(2) read with Article 217(1)(b) and 124(4). Statement 3 is incorrect because the Governor has no power of unilateral removal; removal requires Parliamentary impeachment.",
            "exp_ta": "சரத்து 243K(2) மற்றும் சரத்து 217(1)(b), 124(4)-ன் கீழ் கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் ஆளுநருக்கு ஒருதலைப்பட்சமாக நீக்கும் அதிகாரம் இல்லை; இதற்கு நாடாளுமன்ற பதவி நீக்கம் தேவைப்படுகிறது.",
            "why_a_en": "Statements 1 and 2 are correct; statement 3 is incorrect.",
            "why_a_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை; கூற்று 3 தவறானது.",
            "why_b_en": "Statement 3 is incorrect.",
            "why_b_ta": "கூற்று 3 தவறானது.",
            "why_c_en": "Statement 1 is also correct while statement 3 is incorrect.",
            "why_c_ta": "கூற்று 1-ம் சரியானது மற்றும் கூற்று 3 தவறானது.",
            "why_d_en": "Statement 3 is incorrect; Governor cannot remove on cabinet petition.",
            "why_d_ta": "கூற்று 3 தவறானது; அமைச்சரவை மனுவின் பேரில் ஆளுநர் நீக்க முடியாது.",
            "tip_en": "SEC removal = High Court Judge removal = Parliamentary impeachment under Article 124(4).",
            "tip_ta": "SEC நீக்கம் = உயர் நீதிமன்ற நீதிபதி நீக்கம் = சரத்து 124(4)-ன் கீழ் நாடாளுமன்ற பதவி நீக்கத் தீர்மானம்.",
            "fact_en": "This is one of the highest constitutional protections granted to a state-level statutory/constitutional post.",
            "fact_ta": "இது ஒரு மாநில அளவிலான பதவிக்கு வழங்கப்படும் மிக உயர்ந்த அரசியலமைப்புப் பாதுகாப்புகளில் ஒன்றாகும்."
        },

        # 33
        {
            "subtopic": "State Finance Commission - Constitutional Mandate, Composition & Role (Articles 243I & 243Y)",
            "stem_en": "Consider the following statements regarding the timing and constitution of State Finance Commissions:\n1. The first SFC was to be constituted within one year from the commencement of the 73rd Amendment Act, 1992.\n2. Subsequent SFCs must be constituted at the expiration of every fifth year.\n3. The Governor can never constitute an SFC earlier than five years under any circumstances.\nWhich of the statements given above is/are correct?",
            "stem_ta": "மாநில நிதி ஆணையங்களின் காலம் மற்றும் அமைப்பு தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 73வது திருத்தச் சட்டம், 1992 தொடங்கியதிலிருந்து ஒரு வருடத்திற்குள் முதல் SFC அமைக்கப்பட வேண்டும்.\n2. அடுத்தடுத்த SFC-கள் ஒவ்வொரு ஐந்தாவது ஆண்டின் முடிவிலும் அமைக்கப்பட வேண்டும்.\n3. எந்த சூழ்நிலையிலும் ஐந்து ஆண்டுகளுக்கு முன்னதாக ஆளுநர் ஒருபோதும் SFC-ஐ அமைக்க முடியாது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
            "options": [
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("1 only", "1 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்")
            ],
            "correct_key": "A",
            "exp_en": "Statements 1 and 2 are correct. Statement 3 is incorrect because Article 243-I(1) allows the Governor to constitute an SFC 'at such earlier time' as considered necessary.",
            "exp_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் சரத்து 243-I(1) ஆளுநர் அவசியம் என்று கருதும் போது 'முன்னரே உள்ள நேரத்திலும்' SFC-ஐ அமைக்க அனுமதிக்கிறது.",
            "why_a_en": "Statements 1 and 2 are correct; Governor can constitute earlier if necessary.",
            "why_a_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை; ஆளுநர் அவசியமெனில் முன்னரே அமைக்கலாம்.",
            "why_b_en": "Statement 2 is also correct.",
            "why_b_ta": "கூற்று 2-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "why_c_en": "Statement 3 is incorrect.",
            "why_c_ta": "கூற்று 3 தவறானது.",
            "why_d_en": "Statement 3 is incorrect; earlier constitution is permissible.",
            "why_d_ta": "கூற்று 3 தவறானது; முன்கூட்டியே அமைப்பது அனுமதிக்கப்படுகிறது.",
            "tip_en": "Article 243-I(1): At the expiration of every fifth year, OR earlier as Governor considers necessary.",
            "tip_ta": "சரத்து 243-I(1): ஒவ்வொரு ஐந்தாவது ஆண்டின் முடிவிலும், அல்லது ஆளுநர் அவசியம் என்று கருதும் முன்னரே.",
            "fact_en": "The wording mirrors Article 280(1) for the Union Finance Commission.",
            "fact_ta": "இந்த வாசகம் மத்திய நிதி ஆணையத்திற்கான சரத்து 280(1)-ஐப் பிரதிபலிக்கிறது."
        },

        # 34
        {
            "subtopic": "Financial Devolution, Intergovernmental Transfers & Local Governance",
            "stem_en": "Consider the following statements regarding the Capital Grant Fund (CGF) in Tamil Nadu:\n1. It is created from the devolution funds allocated to local bodies.\n2. It is utilized to finance capital works, bridge infrastructure deficits, and execute priority civic schemes.\n3. It is used exclusively to pay pensions of retired IAS officers.\nWhich of the statements given above are correct?",
            "stem_ta": "தமிழ்நாட்டில் மூலதன மானிய நிதி (CGF) தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது உள்ளாட்சி அமைப்புகளுக்கு ஒதுக்கப்படும் பகிர்வு நிதியிலிருந்து உருவாக்கப்படுகிறது.\n2. இது மூலதனப் பணிகளுக்கு நிதியளிக்கவும், உள்கட்டமைப்பு பற்றாக்குறையைக் குறைக்கவும் மற்றும் முன்னுரிமைத் திட்டங்களை செயல்படுத்தவும் பயன்படுத்தப்படுகிறது.\n3. இது ஓய்வுபெற்ற IAS அதிகாரிகளின் ஓய்வூதியத்தை வழங்க மட்டுமே பிரத்யேகமாகப் பயன்படுத்தப்படுகிறது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?",
            "options": [
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("1 and 3 only", "1 மற்றும் 3 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்")
            ],
            "correct_key": "A",
            "exp_en": "Statements 1 and 2 are correct. Statement 3 is incorrect because the CGF is strictly intended for public infrastructure development (water projects, solid waste, road works) in local bodies, not for civil service pensions.",
            "exp_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் CGF உள்ளாட்சி அமைப்புகளில் பொது உள்கட்டமைப்பு மேம்பாட்டிற்காக (குடிநீர்த் திட்டங்கள், கழிவு மேலாண்மை, சாலைப் பணிகள்) மட்டுமே பயன்படுத்தப்படுகிறது, அரசு ஊழியர்களின் ஓய்வூதியத்திற்காக அல்ல.",
            "why_a_en": "Statements 1 and 2 correctly define the purpose of CGF.",
            "why_a_ta": "கூற்றுகள் 1 மற்றும் 2 CGF-ன் நோக்கத்தை சரியாக வரையறுக்கின்றன.",
            "why_b_en": "Statement 3 is incorrect.",
            "why_b_ta": "கூற்று 3 தவறானது.",
            "why_c_en": "Statement 1 is also correct while statement 3 is incorrect.",
            "why_c_ta": "கூற்று 1-ம் சரியானது மற்றும் கூற்று 3 தவறானது.",
            "why_d_en": "Statement 3 is incorrect; CGF is for capital infrastructure, not pensions.",
            "why_d_ta": "கூற்று 3 தவறானது; CGF உள்கட்டமைப்பிற்கானது, ஓய்வூதியத்திற்கு அல்ல.",
            "tip_en": "CGF is operated at both rural and urban levels to fund major local asset creation.",
            "tip_ta": "முக்கிய உள்ளூர் சொத்து உருவாக்கத்திற்கு நிதியளிக்க ஊரக மற்றும் நகர்ப்புற நிலைகளில் CGF இயக்கப்படுகிறது.",
            "fact_en": "A committee chaired by the Chief Secretary or Secretary, RD & PR oversees CGF sanctions.",
            "fact_ta": "தலைமைச் செயலாளர் அல்லது ஊரக வளர்ச்சித் துறைச் செயலாளர் தலைமையிலான குழு CGF அனுமதிகளைக் கண்காணிக்கிறது."
        },

        # 35
        {
            "subtopic": "Tamil Nadu State Election & Finance Commissions - Legal Framework, Rules & Precedents",
            "stem_en": "Consider the following statements regarding the non-party nature of Village Panchayat elections in Tamil Nadu:\n1. Elections to Village Panchayat Ward Members and Village Panchayat Presidents are conducted on a non-party basis.\n2. Candidates for these posts cannot contest using symbols of recognized political parties.\n3. Political parties are legally permitted to issue formal whips for voting in Village Panchayat council meetings.\nWhich of the statements given above are correct?",
            "stem_ta": "தமிழ்நாட்டில் கிராம பஞ்சாயத்து தேர்தல்களின் கட்சி சாரா தன்மை தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. கிராம பஞ்சாயத்து வார்டு உறுப்பினர்கள் மற்றும் கிராம பஞ்சாயத்து தலைவர்களுக்கான தேர்தல்கள் கட்சி சாரா அடிப்படையில் நடத்தப்படுகின்றன.\n2. இந்தப் பதவிகளுக்கான வேட்பாளர்கள் அங்கீகரிக்கப்பட்ட அரசியல் கட்சிகளின் சின்னங்களைப் பயன்படுத்தி போட்டியிட முடியாது.\n3. கிராம பஞ்சாயத்து மன்றக் கூட்டங்களில் வாக்களிக்க அரசியல் கட்சிகள் சட்டப்பூர்வமாக முறையான கொறடா உத்தரவுகளை பிறப்பிக்க அனுமதிக்கப்படுகின்றன.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?",
            "options": [
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("1 and 3 only", "1 மற்றும் 3 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்")
            ],
            "correct_key": "A",
            "exp_en": "Statements 1 and 2 are correct. Statement 3 is incorrect because since Village Panchayat elections are non-party, party whips have no legal validity or enforceability in Village Panchayat meetings.",
            "exp_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் கிராம பஞ்சாயத்து தேர்தல்கள் கட்சி சாரா என்பதால், கிராம பஞ்சாயத்து கூட்டங்களில் கட்சி கொறடாக்களுக்கு எந்த சட்டப்பூர்வ செல்லுபடியும் அமலாக்கமும் இல்லை.",
            "why_a_en": "Statements 1 and 2 are correct; statement 3 is incorrect.",
            "why_a_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை; கூற்று 3 தவறானது.",
            "why_b_en": "Statement 3 is incorrect.",
            "why_b_ta": "கூற்று 3 தவறானது.",
            "why_c_en": "Statement 1 is also correct while statement 3 is incorrect.",
            "why_c_ta": "கூற்று 1-ம் சரியானது மற்றும் கூற்று 3 தவறானது.",
            "why_d_en": "Statement 3 is incorrect; party whips do not apply to non-party village panchayats.",
            "why_d_ta": "கூற்று 3 தவறானது; கட்சி கொறடாக்கள் கிராம பஞ்சாயத்துகளுக்குப் பொருந்தாது.",
            "tip_en": "Non-party posts in TN: Village Panchayat President & Ward Members. Party posts: Panchayat Union & District Panchayat wards, Town Panchayat, Municipality, Corporation wards.",
            "tip_ta": "TN-ல் கட்சி சாரா பதவிகள்: கிராம பஞ்சாயத்து தலைவர் & வார்டு உறுப்பினர்கள். கட்சிப் பதவிகள்: ஒன்றியம், மாவட்டம், பேரூராட்சி, நகராட்சி, மாநகராட்சி வார்டுகள்.",
            "fact_en": "Free symbols are allotted to Village Panchayat contestants by the Returning Officer.",
            "fact_ta": "கிராம பஞ்சாயத்துப் போட்டியாளர்களுக்கு தேர்தல் நடத்தும் அதிகாரியால் இலவச சின்னங்கள் ஒதுக்கப்படுகின்றன."
        },

        # 36
        {
            "subtopic": "State Election Commission - Constitutional Mandate & Provisions (Articles 243K & 243ZA)",
            "stem_en": "Consider the following statements regarding the role of District Planning Committee (DPC) under Article 243ZD:\n1. It consolidates the plans prepared by Panchayats and Municipalities in the district.\n2. At least four-fifths of the total members of the DPC must be elected by and from among the elected members of the District Panchayat and Municipalities.\n3. The SEC conducts elections to elect the members of the District Planning Committee.\nWhich of the statements given above are correct?",
            "stem_ta": "சரத்து 243ZD-ன் கீழ் மாவட்ட திட்டக் குழுவின் (DPC) பங்கு தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது மாவட்டத்தில் உள்ள பஞ்சாயத்துகள் மற்றும் நகராட்சிகளால் தயாரிக்கப்பட்ட திட்டங்களை ஒருங்கிணைக்கிறது.\n2. DPC-ன் மொத்த உறுப்பினர்களில் குறைந்தது ஐந்தில் நான்கு பங்கு உறுப்பினர்கள் மாவட்ட பஞ்சாயத்து மற்றும் நகராட்சிகளின் தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்களால் தேர்ந்தெடுக்கப்பட வேண்டும்.\n3. மாவட்ட திட்டக் குழுவின் உறுப்பினர்களைத் தேர்ந்தெடுப்பதற்கான தேர்தல்களை SEC நடத்துகிறது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?",
            "options": [
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்"),
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1 and 3 only", "1 மற்றும் 3 மட்டுமே")
            ],
            "correct_key": "A",
            "exp_en": "All three statements are correct under Article 243ZD and statutory rules. The DPC consolidates plans, has a 4/5ths elected membership proportion from local representatives, and its member elections are conducted by the SEC.",
            "exp_ta": "சரத்து 243ZD மற்றும் சட்ட விதிகளின் கீழ் மூன்று கூற்றுகளும் சரியானவை. DPC திட்டங்களை ஒருங்கிணைக்கிறது, உள்ளூர் பிரதிநிதிகளிலிருந்து 4/5 பங்கு தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்களைக் கொண்டுள்ளது மற்றும் அதன் உறுப்பினர் தேர்தல்கள் SEC-ஆல் நடத்தப்படுகின்றன.",
            "why_a_en": "All three statements correctly describe Article 243ZD provisions.",
            "why_a_ta": "மூன்று கூற்றுகளும் சரத்து 243ZD-ன் விதிகளை சரியாக விவரிக்கின்றன.",
            "why_b_en": "Statement 3 is also correct.",
            "why_b_ta": "கூற்று 3-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "why_c_en": "Statement 1 is also correct.",
            "why_c_ta": "கூற்று 1-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "why_d_en": "Statement 2 is also correct.",
            "why_d_ta": "கூற்று 2-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "tip_en": "DPC ratio: 4/5th elected from rural and urban local bodies in proportion to rural/urban population.",
            "tip_ta": "DPC விகிதம்: ஊரக/நகர்ப்புற மக்கள் தொகைக்கு ஏற்ப உள்ளாட்சி அமைப்புகளிலிருந்து 4/5 பங்கு தேர்ந்தெடுக்கப்படுகிறது.",
            "fact_en": "The DPC submits the draft development plan to the State Government.",
            "fact_ta": "DPC வரைவு வளர்ச்சித் திட்டத்தை மாநில அரசுக்கு சமர்ப்பிக்கிறது."
        },

        # 37
        {
            "subtopic": "State Election Commissioner - Appointment, Tenure, Removal & Autonomy",
            "stem_en": "Consider the following statements regarding the powers of the SEC under the Model Code of Conduct (MCC):\n1. It can restrain the announcement of new financial grants or welfare schemes during the election period.\n2. It can transfer civil or police officials if their conduct is found to be politically biased.\n3. It can permanently ban any political party from participating in all future national elections.\nWhich of the statements given above is/are correct?",
            "stem_ta": "தேர்தல் நடத்தை விதிகளின் (MCC) கீழ் SEC-ன் அதிகாரங்கள் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. தேர்தல் காலத்தில் புதிய நிதி மானியங்கள் அல்லது நலத்திட்டங்கள் அறிவிக்கப்படுவதை இது கட்டுப்படுத்த முடியும்.\n2. சிவில் அல்லது காவல் துறை அதிகாரிகளின் நடத்தை அரசியல் சார்புடையதாகக் காணப்பட்டால் அவர்களை இடமாற்றம் செய்ய முடியும்.\n3. எந்தவொரு அரசியல் கட்சியும் எதிர்கால அனைத்து தேசிய தேர்தல்களிலும் பங்கேற்க நிரந்தரமாக தடை விதிக்க முடியும்.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
            "options": [
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("1 only", "1 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்")
            ],
            "correct_key": "A",
            "exp_en": "Statements 1 and 2 are correct. Statement 3 is incorrect because the SEC has no power to deregister or permanently ban political parties from national elections; registration of parties is handled by the Election Commission of India under Section 29A of the RPA 1951.",
            "exp_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் தேசியத் தேர்தல்களில் அரசியல் கட்சிகளைப் பதிவு நீக்கம் செய்யவோ அல்லது நிரந்தரமாகத் தடை செய்யவோ SEC-க்கு அதிகாரம் இல்லை; கட்சிகளைப் பதிவு செய்வது RPA 1951 பிரிவு 29A-ன் கீழ் இந்திய தேர்தல் ஆணையத்தால் கையாளப்படுகிறது.",
            "why_a_en": "Statements 1 and 2 are correct; statement 3 is beyond SEC jurisdiction.",
            "why_a_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை; கூற்று 3 SEC அதிகார வரம்பிற்கு அப்பாற்பட்டது.",
            "why_b_en": "Statement 2 is also correct.",
            "why_b_ta": "கூற்று 2-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "why_c_en": "Statement 3 is incorrect.",
            "why_c_ta": "கூற்று 3 தவறானது.",
            "why_d_en": "Statement 3 is incorrect; ECI handles party registrations.",
            "why_d_ta": "கூற்று 3 தவறானது; ECI கட்சிப் பதிவுகளைக் கையாள்கிறது.",
            "tip_en": "MCC powers cover transfers, stopping announcements, and ensuring level playing field.",
            "tip_ta": "MCC அதிகாரங்கள் இடமாற்றங்கள், புதிய அறிவிப்புகளை நிறுத்துதல் மற்றும் சம வாய்ப்பை உறுதி செய்தல் ஆகியவற்றை உள்ளடக்கியது.",
            "fact_en": "MCC takes effect immediately upon the announcement of election dates by the SEC.",
            "fact_ta": "SEC தேர்தல் தேதிகளை அறிவித்த உடனேயே MCC நடைமுறைக்கு வருகிறது."
        },

        # 38
        {
            "subtopic": "State Finance Commission - Constitutional Mandate, Composition & Role (Articles 243I & 243Y)",
            "stem_en": "Consider the following statements regarding the role of Metropolitan Planning Committee (MPC) under Article 243ZE:\n1. It is constituted in every Metropolitan area having a population of 10 lakhs or more.\n2. At least two-thirds of the members of the MPC must be elected by and from among the elected members of the Municipalities and Chairpersons of Panchayats in the Metropolitan area.\n3. The MPC prepares a draft development plan for the metropolitan area as a whole.\nWhich of the statements given above are correct?",
            "stem_ta": "சரத்து 243ZE-ன் கீழ் பெருநகர திட்டக் குழுவின் (MPC) பங்கு தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது 10 லட்சம் அல்லது அதற்கு மேற்பட்ட மக்கள் தொகை கொண்ட ஒவ்வொரு பெருநகரப் பகுதியிலும் அமைக்கப்படுகிறது.\n2. MPC உறுப்பினர்களில் குறைந்தது மூன்றில் இரண்டு பங்கு உறுப்பினர்கள் அப்பகுதியில் உள்ள நகராட்சிகளின் தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்கள் மற்றும் பஞ்சாயத்து தலைவர்களால் தேர்ந்தெடுக்கப்பட வேண்டும்.\n3. MPC ஒட்டுமொத்த பெருநகரப் பகுதிக்கும் ஒரு வரைவு வளர்ச்சித் திட்டத்தைத் தயாரிக்கிறது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?",
            "options": [
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்"),
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1 and 3 only", "1 மற்றும் 3 மட்டுமே")
            ],
            "correct_key": "A",
            "exp_en": "All three statements are correct under Article 243ZE. MPCs are mandated for 10-lakh-plus metropolitan areas, 2/3rds are elected from municipal and panchayat leaders, and they prepare metropolitan development plans.",
            "exp_ta": "சரத்து 243ZE-ன் கீழ் மூன்று கூற்றுகளும் சரியானவை. 10 லட்சத்திற்கும் அதிகமான பெருநகரப் பகுதிகளுக்கு MPC கட்டாயமாக்கப்பட்டுள்ளது, 2/3 பங்கு உள்ளாட்சித் தலைவர்களிடமிருந்து தேர்ந்தெடுக்கப்படுகிறது மற்றும் அவை பெருநகர வளர்ச்சித் திட்டங்களைத் தயாரிக்கின்றன.",
            "why_a_en": "All three statements accurately state Article 243ZE requirements.",
            "why_a_ta": "மூன்று கூற்றுகளும் சரத்து 243ZE-ன் தேவைகளை துல்லியமாகக் கூறுகின்றன.",
            "why_b_en": "Statement 3 is also correct.",
            "why_b_ta": "கூற்று 3-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "why_c_en": "Statement 1 is also correct.",
            "why_c_ta": "கூற்று 1-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "why_d_en": "Statement 2 is also correct.",
            "why_d_ta": "கூற்று 2-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "tip_en": "Contrast: DPC (Article 243ZD) = 4/5th elected. MPC (Article 243ZE) = 2/3rd elected.",
            "tip_ta": "வேறுபாடு: DPC (சரத்து 243ZD) = 4/5 தேர்ந்தெடுக்கப்பட்டது. MPC (சரத்து 243ZE) = 2/3 தேர்ந்தெடுக்கப்பட்டது.",
            "fact_en": "Chennai Metropolitan Development Authority (CMDA) functions in the Chennai metropolitan area.",
            "fact_ta": "சென்னை பெருநகரப் பகுதியில் சென்னை பெருநகர வளர்ச்சிக் குழுமம் (CMDA) செயல்படுகிறது."
        },

        # 39
        {
            "subtopic": "Financial Devolution, Intergovernmental Transfers & Local Governance",
            "stem_en": "Consider the following statements regarding the Pooled Assigned Revenue in Tamil Nadu:\n1. It includes assigned revenues such as stamp duty surcharge and entertainment tax.\n2. A portion of pooled assigned revenue is distributed to local bodies based on formula recommendations of the SFC.\n3. Pooled assigned revenues can only be distributed in foreign currencies.\nWhich of the statements given above is/are correct?",
            "stem_ta": "தமிழ்நாட்டில் தொகுக்கப்பட்ட ஒதுக்கப்பட்ட வருவாய் (Pooled Assigned Revenue) தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இதில் முத்திரைத் தாள் கூடுதல் கட்டணம் மற்றும் கேளிக்கை வரி போன்ற ஒதுக்கப்பட்ட வருவாய்கள் அடங்கும்.\n2. தொகுக்கப்பட்ட வருவாயின் ஒரு பகுதி SFC-ன் சூத்திரப் பரிந்துரைகளின் அடிப்படையில் உள்ளாட்சி அமைப்புகளுக்கு விநியோகிக்கப்படுகிறது.\n3. தொகுக்கப்பட்ட வருவாயை வெளிநாட்டு நாணயங்களில் மட்டுமே விநியோகிக்க முடியும்.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
            "options": [
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("1 only", "1 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்")
            ],
            "correct_key": "A",
            "exp_en": "Statements 1 and 2 are correct. Statement 3 is incorrect because all state revenue transfers occur in Indian Rupees via the state treasury system.",
            "exp_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் அனைத்து மாநில வருவாய் பரிமாற்றங்களும் மாநில கருவூல அமைப்பு மூலம் இந்திய ரூபாயில் நடைபெறுகின்றன.",
            "why_a_en": "Statements 1 and 2 are correct; statement 3 is incorrect.",
            "why_a_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை; கூற்று 3 தவறானது.",
            "why_b_en": "Statement 2 is also correct.",
            "why_b_ta": "கூற்று 2-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "why_c_en": "Statement 3 is incorrect.",
            "why_c_ta": "கூற்று 3 தவறானது.",
            "why_d_en": "Statement 3 is incorrect; transfers are made in Indian rupees.",
            "why_d_ta": "கூற்று 3 தவறானது; பரிமாற்றங்கள் இந்திய ரூபாயில் செய்யப்படுகின்றன.",
            "tip_en": "Assigned revenue = State taxes assigned by law directly to local bodies (e.g. Surcharge on Stamp Duty).",
            "tip_ta": "ஒதுக்கப்பட்ட வருவாய் = சட்டப்படி உள்ளாட்சி அமைப்புகளுக்கு நேரடியாக ஒதுக்கப்படும் மாநில வரிகள் (முத்திரைத் தாள் கூடுதல் கட்டணம்).",
            "fact_en": "Surcharge on Stamp Duty under Section 175 of the TN Panchayats Act is a significant assigned revenue.",
            "fact_ta": "TN பஞ்சாயத்துகள் சட்டத்தின் பிரிவு 175-ன் கீழ் முத்திரைத் தாள் மீதான கூடுதல் கட்டணம் ஒரு முக்கிய ஒதுக்கப்பட்ட வருவாயாகும்."
        },

        # 40
        {
            "subtopic": "Tamil Nadu State Election & Finance Commissions - Legal Framework, Rules & Precedents",
            "stem_en": "Consider the following statements regarding the Tamil Nadu Panchayats (Election) Rules:\n1. The District Collector is designated as the District Election Officer.\n2. Returning Officers and Assistant Returning Officers are appointed for each local body ward/post.\n3. Polling agents must be appointed exclusively from sitting Members of Parliament.\nWhich of the statements given above is/are correct?",
            "stem_ta": "தமிழ்நாடு பஞ்சாயத்துகள் (தேர்தல்) விதிகள் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. மாவட்ட ஆட்சியர் மாவட்ட தேர்தல் அதிகாரியாக நியமிக்கப்படுகிறார்.\n2. ஒவ்வொரு உள்ளாட்சி வார்டு/பதவிக்கும் தேர்தல் நடத்தும் அதிகாரிகள் மற்றும் உதவி தேர்தல் நடத்தும் அதிகாரிகள் நியமிக்கப்படுகிறார்கள்.\n3. வாக்குச்சாவடி முகவர்கள் பதவியில் உள்ள நாடாளுமன்ற உறுப்பினர்களிலிருந்து மட்டுமே நியமிக்கப்பட வேண்டும்.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
            "options": [
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("1 only", "1 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்")
            ],
            "correct_key": "A",
            "exp_en": "Statements 1 and 2 are correct. Statement 3 is incorrect because polling agents are appointed by the candidates from among ordinary local electors of the polling station area; MPs are not required, and security-protected persons are barred from being polling agents.",
            "exp_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் வாக்குச்சாவடி முகவர்கள் வேட்பாளர்களால் அந்த வாக்குச்சாவடி பகுதியின் சாதாரண வாக்காளர்களிடமிருந்து நியமிக்கப்படுகிறார்கள்; எம்.பி.-க்கள் இதற்கு தேவையில்லை மற்றும் பாதுகாப்பு வழங்கப்பட்ட நபர்கள் முகவர்களாக இருக்க தடை விதிக்கப்பட்டுள்ளது.",
            "why_a_en": "Statements 1 and 2 are correct; statement 3 is incorrect.",
            "why_a_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை; கூற்று 3 தவறானது.",
            "why_b_en": "Statement 2 is also correct.",
            "why_b_ta": "கூற்று 2-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "why_c_en": "Statement 3 is incorrect.",
            "why_c_ta": "கூற்று 3 தவறானது.",
            "why_d_en": "Statement 3 is incorrect; polling agents are local electors.",
            "why_d_ta": "கூற்று 3 தவறானது; வாக்குச்சாவடி முகவர்கள் உள்ளூர் வாக்காளர்கள்.",
            "tip_en": "Collector = District Election Officer (DEO). BDO = Returning Officer for Panchayat Union wards.",
            "tip_ta": "ஆட்சியர் = மாவட்ட தேர்தல் அதிகாரி (DEO). BDO = ஒன்றிய வார்டுகளுக்கான தேர்தல் நடத்தும் அதிகாரி.",
            "fact_en": "Tahsildars and BDOs handle ground-level election logistics across the district.",
            "fact_ta": "வட்டாட்சியர்கள் மற்றும் BDO-க்கள் மாவட்டம் முழுவதும் தேர்தல் தளவாடங்களைக் கையாளுகின்றனர்."
        },

        # 41
        {
            "subtopic": "State Election Commission - Constitutional Mandate & Provisions (Articles 243K & 243ZA)",
            "stem_en": "Consider the following statements regarding the 50% reservation ceiling in local bodies:\n1. In K. Krishna Murthy v. Union of India (2010), the Supreme Court ruled that vertical reservations in local bodies cannot exceed 50%.\n2. In Vikas Kishanrao Gawali (2021), the Supreme Court mandated the 'triple test' for OBC reservations in local bodies.\n3. The 50% ceiling applies only to parliamentary elections and does not apply to local bodies.\nWhich of the statements given above are correct?",
            "stem_ta": "உள்ளாட்சி அமைப்புகளில் 50% இடஒதுக்கீடு உச்சவரம்பு தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. கே. கிருஷ்ண மூர்த்தி எதிர் இந்திய அரசு (2010) வழக்கில், உள்ளாட்சி அமைப்புகளில் செங்குத்து இடஒதுக்கீடு 50%-ஐ தாண்டக்கூடாது என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது.\n2. விகாஸ் கிஷன்ராவ் கவாலி (2021) வழக்கில், உள்ளாட்சி அமைப்புகளில் OBC இடஒதுக்கீட்டிற்கு 'மூன்று கட்ட சோதனையை' உச்ச நீதிமன்றம் கட்டாயமாக்கியது.\n3. 50% உச்சவரம்பு நாடாளுமன்றத் தேர்தல்களுக்கு மட்டுமே பொருந்தும் மற்றும் உள்ளாட்சி அமைப்புகளுக்குப் பொருந்தாது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?",
            "options": [
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("1 and 3 only", "1 மற்றும் 3 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்")
            ],
            "correct_key": "A",
            "exp_en": "Statements 1 and 2 are correct. Statement 3 is incorrect because the 50% ceiling laid down in Indra Sawhney was explicitly held applicable to local body reservations in K. Krishna Murthy and Vikas Gawali.",
            "exp_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் இந்திரா சாஹ்னி வழக்கில் நிர்ணயிக்கப்பட்ட 50% உச்சவரம்பு உள்ளாட்சி இடஒதுக்கீட்டிற்கும் பொருந்தும் என்று கிருஷ்ண மூர்த்தி மற்றும் விகாஸ் கவாலி வழக்குகளில் வெளிப்படையாக தீர்ப்பளிக்கப்பட்டது.",
            "why_a_en": "Statements 1 and 2 are correct; statement 3 contradicts constitutional jurisprudence.",
            "why_a_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை; கூற்று 3 அரசியலமைப்பு தீர்ப்புகளுக்கு எதிரானது.",
            "why_b_en": "Statement 3 is incorrect.",
            "why_b_ta": "கூற்று 3 தவறானது.",
            "why_c_en": "Statement 1 is also correct while statement 3 is incorrect.",
            "why_c_ta": "கூற்று 1-ம் சரியானது மற்றும் கூற்று 3 தவறானது.",
            "why_d_en": "Statement 3 is incorrect; 50% ceiling strictly binds local body quotas.",
            "why_d_ta": "கூற்று 3 தவறானது; 50% உச்சவரம்பு உள்ளாட்சி ஒதுக்கீடுகளையும் கட்டுப்படுத்துகிறது.",
            "tip_en": "Triple test for OBC quotas in local bodies: 1. Dedicated Commission, 2. Empirical study, 3. Aggregate <= 50%.",
            "tip_ta": "உள்ளாட்சி OBC இடஒதுக்கீட்டிற்கான மூன்று சோதனை: 1. பிரத்யேக ஆணையம், 2. அனுபவ ஆய்வு, 3. மொத்தம் <= 50%.",
            "fact_en": "Local body elections in several states were directed to proceed without OBC quotas where the triple test was unfulfilled.",
            "fact_ta": "மூன்று சோதனை பூர்த்தி செய்யப்படாத இடங்களில் OBC ஒதுக்கீடு இல்லாமல் தேர்தலை நடத்த உச்ச நீதிமன்றம் உத்தரவிட்டது."
        },

        # 42
        {
            "subtopic": "State Election Commissioner - Appointment, Tenure, Removal & Autonomy",
            "stem_en": "Consider the following statements regarding the role of Police Machinery during local body elections:\n1. Police forces within the State are placed under the operational superintendence and direction of the State Election Commission during elections.\n2. The SEC can order the deployment of special striking forces or paramilitary personnel in sensitive booths.\n3. Police officers on election duty can independently declare an election result invalid without informing the SEC.\nWhich of the statements given above is/are correct?",
            "stem_ta": "உள்ளாட்சித் தேர்தல்களின் போது காவல்துறை இயந்திரத்தின் பங்கு தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. தேர்தலின் போது மாநிலத்தில் உள்ள காவல் படைகள் மாநில தேர்தல் ஆணையத்தின் செயல்பாட்டு மேற்பார்வை மற்றும் வழிகாட்டுதலின் கீழ் வைக்கப்படுகின்றன.\n2. பதட்டமான வாக்குச்சாவடிகளில் சிறப்பு அதிரடிப் படைகள் அல்லது துணை ராணுவப் படையினரை நிறுத்த SEC உத்தரவிட முடியும்.\n3. தேர்தல் பணியில் உள்ள காவல் அதிகாரிகள் SEC-க்கு தெரிவிக்காமல் ஒரு தேர்தல் முடிவை தன்னிச்சையாக செல்லாது என்று அறிவிக்க முடியும்.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
            "options": [
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("1 only", "1 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்")
            ],
            "correct_key": "A",
            "exp_en": "Statements 1 and 2 are correct. Statement 3 is incorrect because declaration of results is a statutory function of the Returning Officer under the supervision of the SEC; police officers have zero authority to invalidate election results.",
            "exp_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் முடிவுகளை அறிவிப்பது SEC-ன் மேற்பார்வையில் தேர்தல் நடத்தும் அதிகாரியின் சட்டப்பூர்வ பணியாகும்; தேர்தல் முடிவுகளை ரத்து செய்ய காவல்துறை அதிகாரிகளுக்கு எந்த அதிகாரமும் இல்லை.",
            "why_a_en": "Statements 1 and 2 are correct; statement 3 is legally incorrect.",
            "why_a_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை; கூற்று 3 சட்டப்படி தவறானது.",
            "why_b_en": "Statement 2 is also correct.",
            "why_b_ta": "கூற்று 2-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "why_c_en": "Statement 3 is incorrect.",
            "why_c_ta": "கூற்று 3 தவறானது.",
            "why_d_en": "Statement 3 is incorrect; police cannot invalidate elections.",
            "why_d_ta": "கூற்று 3 தவறானது; காவல்துறை தேர்தல்களை ரத்து செய்ய முடியாது.",
            "tip_en": "Police assist in maintaining law and order, under SEC control during polls.",
            "tip_ta": "வாக்குப்பதிவின் போது SEC கட்டுப்பாட்டின் கீழ் சட்டம் ஒழுங்கை பராமரிக்க காவல்துறை உதவுகிறது.",
            "fact_en": "Vulnerable and sensitive polling booths are mapped by the district administration and SEC observers.",
            "fact_ta": "பதட்டமான மற்றும் முக்கியமான வாக்குச்சாவடிகள் மாவட்ட நிர்வாகம் மற்றும் SEC பார்வையாளர்களால் அடையாளம் காணப்படுகின்றன."
        },

        # 43
        {
            "subtopic": "State Finance Commission - Constitutional Mandate, Composition & Role (Articles 243I & 243Y)",
            "stem_en": "Consider the following statements regarding the criteria for municipal devolution recommended by SFCs:\n1. Urban devolution often assigns weightage to population density and slum population.\n2. Infrastructure deficiency index is frequently incorporated into the municipal horizontal sharing formula.\n3. All municipal corporations receive equal grants irrespective of population size.\nWhich of the statements given above are correct?",
            "stem_ta": "SFC-களால் பரிந்துரைக்கப்படும் நகராட்சிப் பகிர்வுக்கான அளவுகோல்கள் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. நகர்ப்புறப் பகிர்வு பெரும்பாலும் மக்கள் தொகை அடர்த்தி மற்றும் சேரி மக்கள் தொகைக்கு முக்கியத்துவம் அளிக்கிறது.\n2. உள்கட்டமைப்பு பற்றாக்குறைக் குறியீடு பெரும்பாலும் நகராட்சி கிடைமட்டப் பகிர்வு சூத்திரத்தில் இணைக்கப்படுகிறது.\n3. மக்கள் தொகை அளவைப் பொருட்படுத்தாமல் அனைத்து மாநகராட்சிகளும் சமமான மானியங்களைப் பெறுகின்றன.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?",
            "options": [
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("1 and 3 only", "1 மற்றும் 3 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்")
            ],
            "correct_key": "A",
            "exp_en": "Statements 1 and 2 are correct. Statement 3 is incorrect because municipal devolution is formula-based and predominantly driven by population size, so larger corporations (like Chennai) receive significantly larger total grants than smaller corporations.",
            "exp_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் நகராட்சிப் பகிர்வு சூத்திர அடிப்படையிலானது மற்றும் முக்கியமாக மக்கள் தொகை அளவால் தீர்மானிக்கப்படுகிறது, எனவே பெரிய மாநகராட்சிகள் (சென்னை போன்றவை) சிறிய மாநகராட்சிகளை விட கணிசமாக அதிக மொத்த மானியங்களைப் பெறுகின்றன.",
            "why_a_en": "Statements 1 and 2 are correct; statement 3 is incorrect.",
            "why_a_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை; கூற்று 3 தவறானது.",
            "why_b_en": "Statement 3 is incorrect.",
            "why_b_ta": "கூற்று 3 தவறானது.",
            "why_c_en": "Statement 1 is also correct while statement 3 is incorrect.",
            "why_c_ta": "கூற்று 1-ம் சரியானது மற்றும் கூற்று 3 தவறானது.",
            "why_d_en": "Statement 3 is incorrect; grants vary according to population and formula.",
            "why_d_ta": "கூற்று 3 தவறானது; மக்கள் தொகை மற்றும் சூத்திரத்திற்கு ஏற்ப மானியங்கள் மாறுபடும்.",
            "tip_en": "Urban formula: Population (Need) + Area (Cost) + Slum/SC-ST population (Equity).",
            "tip_ta": "நகர்ப்புற சூத்திரம்: மக்கள் தொகை (தேவை) + பரப்பளவு (செலவு) + சேரி/SC-ST மக்கள் தொகை (சமத்துவம்).",
            "fact_en": "Greater Chennai Corporation accounts for the single largest share among urban local bodies in Tamil Nadu.",
            "fact_ta": "தமிழ்நாட்டில் உள்ள நகர்ப்புற உள்ளாட்சி அமைப்புகளில் பெருநகர சென்னை மாநகராட்சி மிகப்பெரிய பங்கைக் கொண்டுள்ளது."
        },

        # 44
        {
            "subtopic": "Financial Devolution, Intergovernmental Transfers & Local Governance",
            "stem_en": "Consider the following statements regarding the 15th Finance Commission conditions on property tax:\n1. It mandated that urban local bodies must notify property tax floors and show growth in property tax collections consistent with GSDP growth to qualify for grants.\n2. It encouraged state governments to transition from annual rental value (ARV) to capital value or unit area value systems.\n3. It prohibited local bodies from collecting any water charges or user fees.\nWhich of the statements given above is/are correct?",
            "stem_ta": "சொத்து வரி தொடர்பான 15வது நிதி ஆணையத்தின் நிபந்தனைகள் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. மானியங்களைப் பெறுவதற்கு நகர்ப்புற உள்ளாட்சி அமைப்புகள் சொத்து வரி அடிப்படை வரம்புகளை அறிவிக்க வேண்டும் மற்றும் GSDP வளர்ச்சிக்கு ஏற்ப சொத்து வரி வசூலில் வளர்ச்சியைக் காட்ட வேண்டும் என்று அது கட்டாயப்படுத்தியது.\n2. மாநில அரசுகள் வருடாந்திர வாடகை மதிப்பு (ARV) முறையிலிருந்து மூலதன மதிப்பு அல்லது அலகு பரப்பளவு மதிப்பு முறைகளுக்கு மாறுவதை அது ஊக்குவித்தது.\n3. உள்ளாட்சி அமைப்புகள் குடிநீர்க் கட்டணம் அல்லது பயனர் கட்டணங்களை வசூலிப்பதை அது தடை செய்தது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
            "options": [
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("1 only", "1 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்")
            ],
            "correct_key": "A",
            "exp_en": "Statements 1 and 2 are correct. Statement 3 is incorrect because the 15th FC strongly advocated recovering operation and maintenance costs through rational water supply charges and solid waste user fees.",
            "exp_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் 15வது FC நியாயமான குடிநீர் விநியோகக் கட்டணங்கள் மற்றும் திடக்கழிவு பயனர் கட்டணங்கள் மூலம் செயல்பாட்டு மற்றும் பராமரிப்புச் செலவுகளை மீட்டெடுப்பதை தீவிரமாக ஆதரித்தது.",
            "why_a_en": "Statements 1 and 2 are correct; statement 3 is incorrect.",
            "why_a_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை; கூற்று 3 தவறானது.",
            "why_b_en": "Statement 2 is also correct.",
            "why_b_ta": "கூற்று 2-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "why_c_en": "Statement 3 is incorrect.",
            "why_c_ta": "கூற்று 3 தவறானது.",
            "why_d_en": "Statement 3 is incorrect; user charges were encouraged, not banned.",
            "why_d_ta": "கூற்று 3 தவறானது; பயனர் கட்டணங்கள் ஊக்குவிக்கப்பட்டன, தடை செய்யப்படவில்லை.",
            "tip_en": "15th FC conditionality: Property tax reform is mandatory for accessing urban performance grants.",
            "tip_ta": "15வது FC நிபந்தனை: நகர்ப்புற செயல்திறன் மானியங்களை அணுக சொத்து வரி சீர்திருத்தம் கட்டாயமாகும்.",
            "fact_en": "Tamil Nadu notified property tax revisions across all Municipal Corporations and Municipalities in 2022.",
            "fact_ta": "தமிழ்நாடு 2022-ல் அனைத்து மாநகராட்சிகள் மற்றும் நகராட்சிகளிலும் சொத்து வரி திருத்தங்களை அறிவித்தது."
        },

        # 45
        {
            "subtopic": "Tamil Nadu State Election & Finance Commissions - Legal Framework, Rules & Precedents",
            "stem_en": "Consider the following statements regarding the powers of the District Collector under Section 205 of the Tamil Nadu Panchayats Act, 1994:\n1. The Collector functions as the Inspector of Panchayats.\n2. The Collector can initiate proceedings to remove a Village Panchayat President for wilful omission or refusal to carry out statutory duties.\n3. The President can be removed without providing any show-cause notice or recording the views of the village panchayat.\nWhich of the statements given above is/are correct?",
            "stem_ta": "1994 தமிழ்நாடு பஞ்சாயத்துகள் சட்டத்தின் பிரிவு 205-ன் கீழ் மாவட்ட ஆட்சியரின் அதிகாரங்கள் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. ஆட்சியர் பஞ்சாயத்துகளின் ஆய்வாளராக செயல்படுகிறார்.\n2. சட்டப்பூர்வ கடமைகளைச் செய்ய வேண்டுமென்றே தவறினால் அல்லது மறுத்தால் கிராம பஞ்சாயத்து தலைவரை நீக்க ஆட்சியர் நடவடிக்கைகளைத் தொடங்கலாம்.\n3. விளக்கம் கேட்கும் நோட்டீஸ் வழங்காமலோ அல்லது கிராம பஞ்சாயத்தின் கருத்துக்களைப் பதிவு செய்யாமலோ தலைவரை நீக்க முடியும்.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
            "options": [
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("1 only", "1 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்")
            ],
            "correct_key": "A",
            "exp_en": "Statements 1 and 2 are correct. Statement 3 is incorrect because Section 205 strictly mandates issuing a show-cause notice, convening a special meeting by the Tahsildar to record the panchayat's views, and publishing an official gazette notification stating grounds.",
            "exp_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் பிரிவு 205 விளக்கம் கேட்கும் நோட்டீஸ் வழங்குதல், வட்டாட்சியர் மூலம் பஞ்சாயத்தின் கருத்துக்களைப் பதிவு செய்ய சிறப்புக் கூட்டத்தைக் கூட்டுதல் மற்றும் காரணங்களைக் கூறி அரசிதழில் அதிகாரப்பூர்வ அறிவிப்பை வெளியிடுதல் ஆகியவற்றை கண்டிப்பாக கட்டாயப்படுத்துகிறது.",
            "why_a_en": "Statements 1 and 2 are correct; statement 3 violates statutory procedure and natural justice.",
            "why_a_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை; கூற்று 3 சட்டப்பூர்வ நடைமுறை மற்றும் இயற்கை நீதியை மீறுகிறது.",
            "why_b_en": "Statement 2 is also correct.",
            "why_b_ta": "கூற்று 2-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "why_c_en": "Statement 3 is incorrect.",
            "why_c_ta": "கூற்று 3 தவறானது.",
            "why_d_en": "Statement 3 is incorrect; notice and panchayat consultation are mandatory.",
            "why_d_ta": "கூற்று 3 தவறானது; நோட்டீஸ் மற்றும் பஞ்சாயத்து ஆலோசனை கட்டாயமாகும்.",
            "tip_en": "Collector = Inspector of Panchayats under TN Panchayats Act 1994.",
            "tip_ta": "TN பஞ்சாயத்துகள் சட்டம் 1994-ன் கீழ் ஆட்சியர் = பஞ்சாயத்துகளின் ஆய்வாளர்.",
            "fact_en": "Removal under Section 205 is subject to appeal before the State Government.",
            "fact_ta": "பிரிவு 205-ன் கீழான பதவி நீக்கம் மாநில அரசிடம் மேல்முறையீட்டிற்கு உட்பட்டது."
        },

        # 46
        {
            "subtopic": "State Election Commission - Constitutional Mandate & Provisions (Articles 243K & 243ZA)",
            "stem_en": "Consider the following statements regarding the role of State Election Commission in local body casual vacancies:\n1. A casual vacancy must generally be filled within six months of its occurrence.\n2. If the remaining tenure of the local body is less than six months, no by-election is required.\n3. The SEC can choose to leave seats permanently vacant for 10 years without any justification.\nWhich of the statements given above are correct?",
            "stem_ta": "உள்ளாட்சி அமைப்புகளின் தற்காலிக காலியிடங்களில் மாநில தேர்தல் ஆணையத்தின் பங்கு தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. ஒரு தற்காலிக காலியிடம் பொதுவாக அது ஏற்பட்ட ஆறு மாதங்களுக்குள் நிரப்பப்பட வேண்டும்.\n2. உள்ளாட்சி அமைப்பின் மீதமுள்ள பதவிக்காலம் ஆறு மாதங்களுக்கும் குறைவாக இருந்தால் இடைத்தேர்தல் தேவையில்லை.\n3. எந்த நியாயமும் இன்றி 10 ஆண்டுகளுக்கு இடங்களை நிரந்தரமாக காலியாக வைத்திருக்க SEC தேர்வு செய்யலாம்.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?",
            "options": [
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("1 and 3 only", "1 மற்றும் 3 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்")
            ],
            "correct_key": "A",
            "exp_en": "Statements 1 and 2 are correct. Statement 3 is incorrect because the Constitution mandates periodic elections and filling vacancies promptly within 6 months, unless the remaining duration is under 6 months.",
            "exp_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் மீதமுள்ள காலம் 6 மாதங்களுக்கு குறைவாக இருந்தால் தவிர, காலியிடங்களை 6 மாதங்களுக்குள் நிரப்ப வேண்டும் என்று அரசியலமைப்பு கட்டாயப்படுத்துகிறது.",
            "why_a_en": "Statements 1 and 2 are correct; statement 3 violates constitutional mandates.",
            "why_a_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை; கூற்று 3 அரசியலமைப்பு கட்டளைகளை மீறுகிறது.",
            "why_b_en": "Statement 3 is incorrect.",
            "why_b_ta": "கூற்று 3 தவறானது.",
            "why_c_en": "Statement 1 is also correct while statement 3 is incorrect.",
            "why_c_ta": "கூற்று 1-ம் சரியானது மற்றும் கூற்று 3 தவறானது.",
            "why_d_en": "Statement 3 is incorrect; vacancies cannot be left unaddressed indefinitely.",
            "why_d_ta": "கூற்று 3 தவறானது; காலியிடங்களை காலவரையின்றி நிரப்பாமல் விட்டுவிட முடியாது.",
            "tip_en": "Vacancy rule: 6 months limit; exception if remaining term < 6 months.",
            "tip_ta": "காலியிட விதி: 6 மாத வரம்பு; மீதமுள்ள காலம் < 6 மாதங்கள் என்றால் விதிவிலக்கு.",
            "fact_en": "Articles 243-E(3) and 243-U(3) govern the timeline for casual vacancies.",
            "fact_ta": "சரத்துகள் 243-E(3) மற்றும் 243-U(3) தற்காலிக காலியிடங்களுக்கான காலக்கெடுவை நிர்வகிக்கின்றன."
        },

        # 47
        {
            "subtopic": "State Election Commissioner - Appointment, Tenure, Removal & Autonomy",
            "stem_en": "Consider the following statements regarding the appointment procedure of State Election Commissioners across Indian States:\n1. The appointment is formally made by the Governor under Article 243K(1).\n2. The Law Commission and Supreme Court have recommended broad-based bipartisan selection committees to ensure independence.\n3. The SEC must mandatorily be an active member of the state ruling political party.\nWhich of the statements given above are correct?",
            "stem_ta": "இந்திய மாநிலங்களில் மாநில தேர்தல் ஆணையர்களின் நியமன நடைமுறை தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இந்த நியமனம் சரத்து 243K(1)-ன் கீழ் ஆளுநரால் முறையாக செய்யப்படுகிறது.\n2. சுதந்திரத்தை உறுதி செய்வதற்காக பரந்த அடிப்படையிலான இரு கட்சி தேர்வுக் குழுக்களை சட்ட ஆணையமும் உச்ச நீதிமன்றமும் பரிந்துரைத்துள்ளன.\n3. SEC கட்டாயமாக மாநில ஆளும் அரசியல் கட்சியின் தீவிர உறுப்பினராக இருக்க வேண்டும்.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?",
            "options": [
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("1 and 3 only", "1 மற்றும் 3 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்")
            ],
            "correct_key": "A",
            "exp_en": "Statements 1 and 2 are correct. Statement 3 is incorrect because partisan political affiliation violates the constitutional independence and non-partisan neutrality required of an election commissioner.",
            "exp_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் கட்சி சார்பு என்பது தேர்தல் ஆணையருக்குத் தேவையான அரசியலமைப்பு சுதந்திரம் மற்றும் நடுநிலையை மீறுகிறது.",
            "why_a_en": "Statements 1 and 2 are correct; statement 3 is incorrect.",
            "why_a_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை; கூற்று 3 தவறானது.",
            "why_b_en": "Statement 3 is incorrect.",
            "why_b_ta": "கூற்று 3 தவறானது.",
            "why_c_en": "Statement 1 is also correct while statement 3 is incorrect.",
            "why_c_ta": "கூற்று 1-ம் சரியானது மற்றும் கூற்று 3 தவறானது.",
            "why_d_en": "Statement 3 is incorrect; political party membership is barred.",
            "why_d_ta": "கூற்று 3 தவறானது; அரசியல் கட்சி உறுப்பினர் பதவி தடை செய்யப்பட்டுள்ளது.",
            "tip_en": "Independent selection committees enhance public trust in free and fair local elections.",
            "tip_ta": "சுயாதீன தேர்வுக் குழுக்கள் நியாயமான உள்ளாட்சித் தேர்தல்களில் பொதுமக்களின் நம்பிக்கையை மேம்படுத்துகின்றன.",
            "fact_en": "In Anoop Baranwal (2023), the SC established a collegium for Central ECI; similar reforms are advocated for SECs.",
            "fact_ta": "அனூப் பரன்வால் (2023) வழக்கில் உச்ச நீதிமன்றம் மத்திய ECI-க்கு கொலீஜியத்தை நிறுவியது; SEC-களுக்கும் இதே போன்ற சீர்திருத்தங்கள் பரிந்துரைக்கப்படுகின்றன."
        },

        # 48
        {
            "subtopic": "State Finance Commission - Constitutional Mandate, Composition & Role (Articles 243I & 243Y)",
            "stem_en": "Consider the following statements regarding the role of Gram Sabha in financial accountability:\n1. The Gram Sabha approves the village budget and development plans.\n2. The Gram Sabha conducts social audits of local schemes and public expenditure.\n3. The Gram Sabha has the constitutional authority to abolish the State Finance Commission.\nWhich of the statements given above is/are correct?",
            "stem_ta": "நிதிப் பொறுப்புடைமையில் கிராம சபையின் பங்கு தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. கிராம சபை கிராம பட்ஜெட் மற்றும் வளர்ச்சித் திட்டங்களுக்கு ஒப்புதல் அளிக்கிறது.\n2. கிராம சபை உள்ளூர் திட்டங்கள் மற்றும் பொதுச் செலவினங்களின் சமூகத் தணிக்கையை நடத்துகிறது.\n3. மாநில நிதி ஆணையத்தை கலைக்க கிராம சபைக்கு அரசியலமைப்பு அதிகாரம் உள்ளது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
            "options": [
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("1 only", "1 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்")
            ],
            "correct_key": "A",
            "exp_en": "Statements 1 and 2 are correct. Statement 3 is incorrect because the State Finance Commission is a constitutional body created under Article 243-I and can only be amended or altered by Parliament through a constitutional amendment under Article 368.",
            "exp_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் மாநில நிதி ஆணையம் சரத்து 243-I-ன் கீழ் உருவாக்கப்பட்ட ஒரு அரசியலமைப்பு அமைப்பாகும் மற்றும் சரத்து 368-ன் கீழ் நாடாளுமன்றத்தால் மட்டுமே அரசியலமைப்பு திருத்தம் மூலம் மாற்றப்பட முடியும்.",
            "why_a_en": "Statements 1 and 2 are correct; statement 3 is incorrect.",
            "why_a_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை; கூற்று 3 தவறானது.",
            "why_b_en": "Statement 2 is also correct.",
            "why_b_ta": "கூற்று 2-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "why_c_en": "Statement 3 is incorrect.",
            "why_c_ta": "கூற்று 3 தவறானது.",
            "why_d_en": "Statement 3 is incorrect; Gram Sabha cannot abolish SFC.",
            "why_d_ta": "கூற்று 3 தவறானது; கிராம சபையால் SFC-ஐ கலைக்க முடியாது.",
            "tip_en": "Gram Sabha = Grassroots watchdog ensuring social audit and budgetary transparency.",
            "tip_ta": "கிராம சபை = சமூகத் தணிக்கை மற்றும் பட்ஜெட் வெளிப்படைத்தன்மையை உறுதி செய்யும் அடிமட்ட கண்காணிப்பாளர்.",
            "fact_en": "In Tamil Nadu, Gram Sabha meetings are statutorily mandated on specific key dates (Jan 26, May 1, Aug 15, Oct 2, etc.).",
            "fact_ta": "தமிழ்நாட்டில் குறிப்பிட்ட முக்கிய நாட்களில் (ஜனவரி 26, மே 1, ஆகஸ்ட் 15, அக்டோபர் 2 போன்றவை) கிராம சபை கூட்டங்கள் சட்டப்பூர்வமாக கட்டாயமாக்கப்பட்டுள்ளன."
        },

        # 49
        {
            "subtopic": "Financial Devolution, Intergovernmental Transfers & Local Governance",
            "stem_en": "Consider the following statements regarding the role of SFCs in municipal solid waste and sanitation:\n1. SFCs recommend earmarked funds for solid waste management machinery and processing facilities.\n2. Swachh Bharat Mission grants are complemented by State devolution transfers to ensure sustainable ODF-plus outcomes.\n3. SFCs recommend that local bodies abandon all waste collection and dump garbage in water bodies.\nWhich of the statements given above is/are correct?",
            "stem_ta": "நகராட்சி திடக்கழிவு மற்றும் சுகாதாரத்தில் SFC-களின் பங்கு தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. திடக்கழிவு மேலாண்மை இயந்திரங்கள் மற்றும் செயலாக்க வசதிகளுக்காக ஒதுக்கப்பட்ட நிதியை SFC-கள் பரிந்துரைக்கின்றன.\n2. நிலையான ODF-பிளஸ் விளைவுகளை உறுதி செய்வதற்காக ஸ்வச் பாரத் திட்ட மானியங்கள் மாநில பகிர்வு நிதி மூலம் நிறைவு செய்யப்படுகின்றன.\n3. உள்ளாட்சி அமைப்புகள் அனைத்து கழிவு சேகரிப்பையும் கைவிட்டு நீர்நிலைகளில் குப்பைகளை கொட்ட வேண்டும் என்று SFC-கள் பரிந்துரைக்கின்றன.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
            "options": [
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("1 only", "1 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்")
            ],
            "correct_key": "A",
            "exp_en": "Statements 1 and 2 are correct. Statement 3 is incorrect because dumping garbage in water bodies is strictly illegal under environmental protection laws and SFCs fund scientific waste processing and recycling.",
            "exp_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் நீர்நிலைகளில் குப்பைகளைக் கொட்டுவது சுற்றுச்சூழல் பாதுகாப்புச் சட்டங்களின் கீழ் சட்டவிரோதமானது மற்றும் அறிவியல் பூர்வமான கழிவு செயலாக்கத்திற்கு SFC-கள் நிதியளிக்கின்றன.",
            "why_a_en": "Statements 1 and 2 are correct; statement 3 is absurd and illegal.",
            "why_a_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை; கூற்று 3 அபத்தமானது மற்றும் சட்டவிரோதமானது.",
            "why_b_en": "Statement 2 is also correct.",
            "why_b_ta": "கூற்று 2-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "why_c_en": "Statement 3 is incorrect.",
            "why_c_ta": "கூற்று 3 தவறானது.",
            "why_d_en": "Statement 3 is incorrect.",
            "why_d_ta": "கூற்று 3 தவறானது.",
            "tip_en": "Sanitation and waste management are core functional mandates under the 11th and 12th Schedules.",
            "tip_ta": "சுகாதாரம் மற்றும் கழிவு மேலாண்மை ஆகியவை 11 மற்றும் 12வது அட்டவணைகளின் கீழ் முக்கியப் பணிகளாகும்.",
            "fact_en": "Solid Waste Management Rules 2016 place statutory duties on local authorities to achieve 100% door-to-door collection.",
            "fact_ta": "திடக்கழிவு மேலாண்மை விதிகள் 2016 உள்ளாட்சி அமைப்புகளுக்கு 100% வீடு வீடாகச் சென்று சேகரிக்கும் சட்டப்பூர்வ கடமைகளை விதிக்கின்றன."
        },

        # 50
        {
            "subtopic": "Tamil Nadu State Election & Finance Commissions - Legal Framework, Rules & Precedents",
            "stem_en": "Consider the following statements regarding the horizontal distribution of rural devolution in Tamil Nadu:\n1. The rural pool (approx. 56% of total devolution) is divided among Village Panchayats, Panchayat Unions, and District Panchayats.\n2. Village Panchayats receive the largest portion (around 55% - 60%) of the rural pool.\n3. District Panchayats receive 90% of the rural pool while Village Panchayats receive zero.\nWhich of the statements given above is/are correct?",
            "stem_ta": "தமிழ்நாட்டில் ஊரகப் பகிர்வின் கிடைமட்ட விநியோகம் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. ஊரகப் பங்கு (மொத்தப் பகிர்வில் சுமார் 56%) கிராம பஞ்சாயத்துகள், பஞ்சாயத்து ஒன்றியங்கள் மற்றும் மாவட்ட பஞ்சாயத்துகளிடையே பிரிக்கப்படுகிறது.\n2. ஊரகப் பங்கில் கிராம பஞ்சாயத்துகள் மிகப்பெரிய பகுதியை (சுமார் 55% - 60%) பெறுகின்றன.\n3. மாவட்ட பஞ்சாயத்துகள் ஊரகப் பங்கில் 90%-ஐ பெறுகின்றன, அதே நேரத்தில் கிராம பஞ்சாயத்துகள் பூஜ்ஜியத்தைப் பெறுகின்றன.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
            "options": [
                ("1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
                ("1 only", "1 மட்டுமே"),
                ("2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
                ("1, 2 and 3", "1, 2 மற்றும் 3 ஆகிய அனைத்தும்")
            ],
            "correct_key": "A",
            "exp_en": "Statements 1 and 2 are correct. Statement 3 is incorrect because Village Panchayats deliver frontline basic services (drinking water, street lights, sanitation) and thus receive the lion's share (~55-60%), while District Panchayats receive roughly 8-10%.",
            "exp_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் கிராம பஞ்சாயத்துகள் நேரடி அடிப்படை சேவைகளை (குடிநீர், தெருவிளக்கு, சுகாதாரம்) வழங்குவதால் பெரும்பகுதியைப் (~55-60%) பெறுகின்றன; மாவட்ட பஞ்சாயத்துகள் சுமார் 8-10% மட்டுமே பெறுகின்றன.",
            "why_a_en": "Statements 1 and 2 are correct; statement 3 reverses the actual devolution shares.",
            "why_a_ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை; கூற்று 3 உண்மையான பகிர்வுப் பங்குகளை மாற்றியமைக்கிறது.",
            "why_b_en": "Statement 2 is also correct.",
            "why_b_ta": "கூற்று 2-ம் சரியானது என்பதால் இது முழுமையற்றது.",
            "why_c_en": "Statement 3 is incorrect.",
            "why_c_ta": "கூற்று 3 தவறானது.",
            "why_d_en": "Statement 3 is incorrect; village panchayats receive the highest rural share.",
            "why_d_ta": "கூற்று 3 தவறானது; கிராம பஞ்சாயத்துகள் அதிக ஊரகப் பங்கைப் பெறுகின்றன.",
            "tip_en": "Rural pool formula in TN: Village Panchayats (~60%) > Panchayat Unions (~32%) > District Panchayats (~8%).",
            "tip_ta": "TN ஊரகப் பகிர்வு சூத்திரம்: கிராம பஞ்சாயத்துகள் (~60%) > பஞ்சாயத்து ஒன்றியங்கள் (~32%) > மாவட்ட பஞ்சாயத்துகள் (~8%).",
            "fact_en": "This distribution ensures that grassroots village institutions have adequate funds for daily maintenance of basic utilities.",
            "fact_ta": "இந்த விநியோகம் அடிமட்ட கிராம நிறுவனங்களுக்கு அடிப்படை பயன்பாடுகளைப் பராமரிக்க போதுமான நிதி இருப்பதை உறுதி செய்கிறது."
        }
    ]

    questions = []
    for i, item in enumerate(raw_data, start=1):
        opts = item["options"]
        correct_key = item["correct_key"]

        q = make_sefc_q(
            qid=f"SEFC_S_{i:03d}",
            diff="medium" if i % 2 == 1 else "hard",
            qtype="statement",
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
            tags=["polity", "state_election_finance_commissions", "statement", item["subtopic"].lower().replace(" ", "_")]
        )
        questions.append(q)
    return questions


def build_statement_file():
    qs = get_statement_questions()
    print(f"Generated {len(qs)} raw Statement questions for State Election & Finance Commissions.")
    balanced = randomize_and_balance_dataset(qs, seed=45)

    out_dir = os.path.join("data", "questions", "polity")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "state_election_finance_commissions_statement_based.json")
    alias_path = os.path.join(out_dir, "state_election_finance_commissions_statement.json")

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)
    with open(alias_path, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)
    print(f"Saved balanced Statement MCQs to {out_path} and alias {alias_path}")

    rep = ContentValidator.validate_file(out_path, expected_count=50, expected_prefix="SEFC_S_")
    print(f"Validation: {'PASS' if rep.is_valid else 'FAIL'} | Total: {rep.total_audited}")
    print(f"Keys: {rep.key_distribution}")
    if not rep.is_valid:
        for iss in rep.issues:
            print("  Issue:", iss.severity, iss.field_name, iss.message)
    return rep.is_valid


if __name__ == "__main__":
    success = build_statement_file()
    if not success:
        exit(1)
