# -*- coding: utf-8 -*-
"""
Generator for Electoral Reforms Past Year Questions (PYQ) (50 Questions: ER_PYQ_001 to ER_PYQ_050).
Strictly adheres to:
- Real TNPSC Group 1, Group 2, Group 4, and UPSC CSE past papers on Electoral Reforms.
- Fully bilingual (English and authentic Tamil).
- 24-field TNPSC Nova AI schema.
- Balanced answer keys (13 B, 12 C, 12 D, 13 A or similar ~12-13 each).
- Saves to data/questions/polity/electoral_reforms_pyq.json and electoral_reforms_pyq_practice.json.
"""
import json
import os
from er_mcq_helper import make_er_q
from rebalance_er_helper import balance_question_keys
from tools.nova_content_engine.validator import ContentValidator

raw_pyq_data = [
    # 1
    {
        "exam": "TNPSC Group 1 2015",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 1 2015",
        "stem_en": "Which committee on electoral reforms was appointed in 1974 by Jayaprakash Narayan on behalf of the 'Citizens for Democracy'?",
        "stem_ta": "'மக்களாட்சிக்கான குடிமக்கள்' அமைப்பின் சார்பில் ஜெயபிரகாஷ் நாராயணனால் 1974-ல் நியமிக்கப்பட்ட தேர்தல் சீர்திருத்தக் குழு எது?",
        "options": [
            ("Dinesh Goswami Committee", "தினேஷ் கோஸ்வாமி குழு"),
            ("Tarkunde Committee", "தர்குண்டே குழு"),
            ("Indrajit Gupta Committee", "இந்திரஜித் குப்தா குழு"),
            ("K. Santhanam Committee", "கே. சந்தானம் குழு")
        ],
        "correct_idx": 1, # Tarkunde Committee
        "exp_en": "The Tarkunde Committee (also known as the J.P. Committee) was appointed in 1974 by Jayaprakash Narayan under the banner of Citizens for Democracy to study and suggest electoral reforms.",
        "exp_ta": "தேர்தல் சீர்திருத்தங்களை ஆய்வு செய்து பரிந்துரைக்க 1974-ல் 'மக்களாட்சிக்கான குடிமக்கள்' அமைப்பின் கீழ் ஜெயபிரகாஷ் நாராயணனால் தர்குண்டே குழு (வி.எம். தர்குண்டே தலைமையில்) நியமிக்கப்பட்டது.",
        "tip": "Tarkunde Committee (1974) submitted its landmark report in 1975 recommending an 18-year voting age.",
        "fact": "V.M. Tarkunde was a former judge of the Bombay High Court and a prominent civil liberties activist.",
        "diff": "Medium",
        "subtopic": "Electoral Reform Committees"
    },

    # 2
    {
        "exam": "TNPSC Group 1 2017",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 1 2017",
        "stem_en": "The Dinesh Goswami Committee on Electoral Reforms (1990) was appointed during the tenure of which Prime Minister of India?",
        "stem_ta": "தேர்தல் சீர்திருத்தங்கள் குறித்த தினேஷ் கோஸ்வாமி குழு (1990) இந்தியாவின் எந்தப் பிரதமரின் ஆட்சிக் காலத்தில் நியமிக்கப்பட்டது?",
        "options": [
            ("Rajiv Gandhi", "ராஜீவ் காந்தி"),
            ("V.P. Singh", "வி.பி. சிங்"),
            ("P.V. Narasimha Rao", "பி.வி. நரசிம்ம ராவ்"),
            ("Atal Bihari Vajpayee", "அடல் பிகாரி வாஜ்பாய்")
        ],
        "correct_idx": 1, # V.P. Singh
        "exp_en": "The Dinesh Goswami Committee was set up in 1990 by the National Front Government headed by Prime Minister V.P. Singh to make comprehensive recommendations on electoral reforms.",
        "exp_ta": "தேர்தல் சீர்திருத்தங்கள் குறித்து விரிவான பரிந்துரைகளை வழங்க பிரதமர் வி.பி. சிங் தலைமையிலான தேசிய முன்னணி அரசாங்கத்தால் 1990-ல் தினேஷ் கோஸ்வாமி குழு அமைக்கப்பட்டது.",
        "tip": "Dinesh Goswami was the Union Law Minister in the V.P. Singh cabinet.",
        "fact": "The committee strongly recommended the introduction of Electronic Voting Machines and state assistance in kind.",
        "diff": "Medium",
        "subtopic": "Electoral Reform Committees"
    },

    # 3
    {
        "exam": "TNPSC Group 2 2018",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 2 2018",
        "stem_en": "The Indrajit Gupta Committee (1998) on Electoral Reforms was specifically constituted to examine which subject?",
        "stem_ta": "தேர்தல் சீர்திருத்தங்கள் குறித்த இந்திரஜித் குப்தா குழு (1998) குறிப்பாக எந்த விவகாரத்தை ஆராய அமைக்கப்பட்டது?",
        "options": [
            ("Criminalization of politics", "அரசியல் குற்றமயமாதல்"),
            ("State funding of elections", "தேர்தல்களுக்கு அரசு நிதி உதவி"),
            ("Use of EVMs in general elections", "பொதுத்தேர்தலில் வாக்குப்பதிவு இயந்திரங்களின் பயன்பாடு"),
            ("Delimitation of constituencies", "தொகுதி மறுவரையறை")
        ],
        "correct_idx": 1, # State funding of elections
        "exp_en": "The Indrajit Gupta Committee (1998), an 8-member all-party committee, was specifically set up to examine state funding of elections and recommended state financial assistance in kind only.",
        "exp_ta": "இந்திரஜித் குப்தா குழு (1998) தேர்தல்களுக்கான அரசு நிதி உதவி குறித்து ஆராய்வதற்காக பிரத்யேகமாக அமைக்கப்பட்டு, பொருள் வடிவில் மட்டுமே அரசு நிதி உதவி வழங்க வேண்டும் என பரிந்துரைத்தது.",
        "tip": "Indrajit Gupta = State funding of elections in kind to recognized political parties.",
        "fact": "The committee recommended a dedicated Election Fund with Rs 600 crore corpus contributed equally by Centre and States.",
        "diff": "Easy",
        "subtopic": "State Funding of Elections"
    },

    # 4
    {
        "exam": "TNPSC Group 1 2019",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 1 2019",
        "stem_en": "The N.N. Vohra Committee (1993) was constituted by the Government of India to investigate which serious issue?",
        "stem_ta": "இந்திய அரசால் என்.என். வோரா குழு (1993) எந்த தீவிரமான பிரச்சனையை விசாரிக்க அமைக்கப்பட்டது?",
        "options": [
            ("Border security management", "எல்லை பாதுகாப்பு மேலாண்மை"),
            ("Nexus among crime syndicates, politicians, and bureaucrats", "குற்றக்கும்பல்கள், அரசியல்வாதிகள் மற்றும் அதிகாரிகளின் தொடர்பு"),
            ("Reorganization of states", "மாநிலங்கள் மறுசீரமைப்பு"),
            ("Financial devolution to Panchayats", "ஊராட்சிகளுக்கு நிதிப் பகிர்வு")
        ],
        "correct_idx": 1, # Nexus among crime syndicates, politicians, and bureaucrats
        "exp_en": "The Vohra Committee, headed by former Union Home Secretary N.N. Vohra, submitted its explosive report in October 1993 on the unholy nexus between mafia syndicates, corrupt bureaucrats, and politicians.",
        "exp_ta": "முன்னாள் மத்திய உள்துறைச் செயலாளர் என்.என். வோரா தலைமையிலான வோரா குழு, மாஃபியா குற்றக்கும்பல்கள், ஊழல் அதிகாரிகள் மற்றும் அரசியல்வாதிகளுக்கு இடையிலான ஆபத்தான தொடர்பு குறித்து 1993-ல் அறிக்கை சமர்ப்பித்தது.",
        "tip": "The Vohra Committee report directly led to urgent demands for decriminalization of politics.",
        "fact": "The committee was formed following the March 1993 Bombay serial bomb blasts.",
        "diff": "Medium",
        "subtopic": "Decriminalization of Politics"
    },

    # 5
    {
        "exam": "TNPSC Group 4 2018",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 4 2018",
        "stem_en": "By which Constitutional Amendment Act was the voting age in India reduced from 21 years to 18 years?",
        "stem_ta": "எந்த அரசியலமைப்பு திருத்தச் சட்டத்தின் மூலம் இந்தியாவில் வாக்களிக்கும் வயது 21-லிருந்து 18 ஆக குறைக்கப்பட்டது?",
        "options": [
            ("42nd Amendment Act", "42-வது திருத்தச் சட்டம்"),
            ("61st Amendment Act", "61-வது திருத்தச் சட்டம்"),
            ("44th Amendment Act", "44-வது திருத்தச் சட்டம்"),
            ("73rd Amendment Act", "73-வது திருத்தச் சட்டம்")
        ],
        "correct_idx": 1, # 61st Amendment Act
        "exp_en": "The Constitution (61st Amendment) Act, 1988 amended Article 326 of the Constitution to reduce the voting age for Lok Sabha and State Legislative Assembly elections from 21 to 18 years.",
        "exp_ta": "61-வது அரசியலமைப்பு திருத்தச் சட்டம், 1988 சரத்து 326-ஐ திருத்தி, மக்களவை மற்றும் மாநில சட்டமன்றத் தேர்தல்களுக்கான வாக்களிக்கும் வயதை 21-லிருந்து 18 ஆக குறைத்தது.",
        "tip": "61st Amendment was passed under Prime Minister Rajiv Gandhi.",
        "fact": "The Act received the assent of the President on 28 December 1988 and came into force on 28 March 1989.",
        "diff": "Easy",
        "subtopic": "Voting Rights & Franchise"
    },

    # 6
    {
        "exam": "TNPSC Group 2A 2017",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 2A 2017",
        "stem_en": "In which year did the Constitution (61st Amendment) Act lowering the voting age to 18 come into force?",
        "stem_ta": "வாக்களிக்கும் வயதை 18 ஆக குறைத்த 61-வது அரசியலமைப்பு திருத்தச் சட்டம் எந்த ஆண்டில் அமலுக்கு வந்தது?",
        "options": [
            ("1988", "1988"),
            ("1989", "1989"),
            ("1990", "1990"),
            ("1991", "1991")
        ],
        "correct_idx": 1, # 1989
        "exp_en": "Though enacted as the Constitution (61st Amendment) Act, 1988, it officially came into force on 28 March 1989 upon receiving state ratifications and presidential notification.",
        "exp_ta": "61-வது அரசியலமைப்பு திருத்தச் சட்டம் 1988-ல் இயற்றப்பட்டாலும், மாநிலங்களின் ஒப்புதலைப் பெற்று அதிகாரப்பூர்வமாக 1989 மார்ச் 28 அன்று அமலுக்கு வந்தது.",
        "tip": "Passed in 1988, but enforced on 28 March 1989.",
        "fact": "This historic reform expanded the Indian electorate by over 35 million young voters in one stroke.",
        "diff": "Medium",
        "subtopic": "Voting Rights & Franchise"
    },

    # 7
    {
        "exam": "TNPSC Group 1 2021",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 1 2021",
        "stem_en": "In the landmark judgment of Lily Thomas v. Union of India (2013), the Supreme Court of India declared which statutory provision unconstitutional?",
        "stem_ta": "லில்லி தாமஸ் எதிர் இந்திய ஒன்றியம் (2013) வழக்கின் வரலாற்று சிறப்புமிக்க தீர்ப்பில், உச்ச நீதிமன்றம் எந்த சட்டப்பிரிவை அரசியலமைப்பிற்கு எதிரானது என அறிவித்தது?",
        "options": [
            ("Section 8(1) of RPA 1951", "1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 8(1)"),
            ("Section 8(4) of RPA 1951", "1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 8(4)"),
            ("Section 123 of RPA 1951", "1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 123"),
            ("Section 29A of RPA 1951", "1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 29A")
        ],
        "correct_idx": 1, # Section 8(4) of RPA 1951
        "exp_en": "In Lily Thomas v. Union of India (July 2013), the Supreme Court struck down Section 8(4) of the Representation of the People Act 1951, which gave convicted sitting MPs/MLAs a 3-month protection period to file an appeal without immediate disqualification.",
        "exp_ta": "லில்லி தாமஸ் எதிர் இந்திய ஒன்றியம் (2013) வழக்கில், தண்டனை பெற்ற எம்.பி/எம்.எல்.ஏ-க்கள் மேல்முறையீடு செய்ய 3 மாத கால அவகாசம் வழங்கிய மக்கள் பிரதிநிதித்துவச் சட்டம் 1951-ன் பிரிவு 8(4)-ஐ உச்ச நீதிமன்றம் ரத்து செய்தது.",
        "tip": "Striking down Sec 8(4) resulted in instant disqualification of convicted legislators upon sentencing.",
        "fact": "The judgment was delivered by a bench comprising Justice A.K. Patnaik and Justice S.J. Mukhopadhaya.",
        "diff": "Hard",
        "subtopic": "Decriminalization of Politics"
    },

    # 8
    {
        "exam": "TNPSC Group 2 2015",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 2 2015",
        "stem_en": "In which landmark case did the Supreme Court of India direct the Election Commission to provide a 'None of the Above' (NOTA) option on EVMs?",
        "stem_ta": "எந்த வரலாற்று சிறப்புமிக்க வழக்கில் EVM இயந்திரங்களில் 'நோட்டா' (NOTA) விருப்பத்தை வழங்குமாறு இந்திய தேர்தல் ஆணையத்திற்கு உச்ச நீதிமன்றம் உத்தரவிட்டது?",
        "options": [
            ("Indira Nehru Gandhi v. Raj Narain (1975)", "இந்திரா நேரு காந்தி எதிர் ராஜ் நாராயண் (1975)"),
            ("People's Union for Civil Liberties (PUCL) v. Union of India (2013)", "மக்கள் குடிமக்கள் உரிமை சங்கம் (PUCL) எதிர் இந்திய ஒன்றியம் (2013)"),
            ("ADR v. Union of India (2002)", "ADR எதிர் இந்திய ஒன்றியம் (2002)"),
            ("Kuldip Nayar v. Union of India (2006)", "குல்தீப் நய்யார் எதிர் இந்திய ஒன்றியம் (2006)")
        ],
        "correct_idx": 1, # PUCL v. UOI (2013)
        "exp_en": "On 27 September 2013, the Supreme Court ruled in People's Union for Civil Liberties (PUCL) v. Union of India that voters have a fundamental right under Article 19(1)(a) to express their rejection of all candidates by pressing the NOTA button.",
        "exp_ta": "2013 செப்டம்பர் 27 அன்று, PUCL எதிர் இந்திய ஒன்றியம் வழக்கில், அனைத்து வேட்பாளர்களையும் நிராகரிக்கும் உரிமை வாக்காளர்களுக்கு சரத்து 19(1)(a)-ன் கீழ் உண்டு என கூறி நோட்டா பொத்தானை வழங்க உச்ச நீதிமன்றம் உத்தரவிட்டது.",
        "tip": "CJI P. Sathasivam headed the bench that delivered the NOTA judgment.",
        "fact": "India became the 14th country in the world to introduce a negative voting option in its ballot.",
        "diff": "Medium",
        "subtopic": "NOTA & Voter Rights"
    },

    # 9
    {
        "exam": "TNPSC Group 1 2022",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 1 2022",
        "stem_en": "The Supreme Court judgment in Association for Democratic Reforms (ADR) v. Union of India (2002) held that a voter's right to know candidate credentials flows from which Fundamental Right?",
        "stem_ta": "ஏடிஆர் (ADR) எதிர் இந்திய ஒன்றியம் (2002) வழக்கின் உச்ச நீதிமன்றத் தீர்ப்பு, வேட்பாளரின் விவரங்களை அறியும் வாக்காளரின் உரிமை எந்த அடிப்படை உரிமையிலிருந்து வெளிப்படுகிறது என தீர்ப்பளித்தது?",
        "options": [
            ("Article 14 (Right to Equality)", "சரத்து 14 (சமத்துவ உரிமை)"),
            ("Article 19(1)(a) (Freedom of Speech and Expression)", "சரத்து 19(1)(a) (பேச்சு மற்றும் கருத்து சுதந்திரம்)"),
            ("Article 21 (Right to Life and Personal Liberty)", "சரத்து 21 (வாழ்வுரிமை மற்றும் தனிநபர் சுதந்திரம்)"),
            ("Article 25 (Freedom of Conscience)", "சரத்து 25 (மனசாட்சி சுதந்திரம்)")
        ],
        "correct_idx": 1, # Article 19(1)(a)
        "exp_en": "In Union of India v. Association for Democratic Reforms (2002), the Supreme Court held that the right to vote is meaningless without informed choice, and that the voter's 'right to know' the educational, financial, and criminal antecedents of candidates is part of Article 19(1)(a).",
        "exp_ta": "இந்திய ஒன்றியம் எதிர் ஏடிஆர் (2002) வழக்கில், வேட்பாளர்களின் கல்வி, சொத்துக்கள் மற்றும் குற்றப்பின்னணியை அறியும் வாக்காளரின் உரிமை சரத்து 19(1)(a) கருத்து சுதந்திரத்தின் ஒருங்கிணைந்த பகுதி என உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
        "tip": "Voter's right to know = Article 19(1)(a) fundamental right.",
        "fact": "This ruling directly resulted in the creation and statutory notification of Form 26 under Conduct of Elections Rules.",
        "diff": "Hard",
        "subtopic": "Decriminalization of Politics"
    },

    # 10
    {
        "exam": "TNPSC Group 1 2020",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 1 2020",
        "stem_en": "In Shailesh Manubhai Parmar v. Election Commission of India (2018), the Supreme Court ruled that NOTA is NOT applicable to which elections?",
        "stem_ta": "சைலேஷ் மனுபாய் பர்மர் எதிர் இந்திய தேர்தல் ஆணையம் (2018) வழக்கில், நோட்டா (NOTA) எந்த தேர்தல்களுக்கு பொருந்தாது என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது?",
        "options": [
            ("State Legislative Assembly elections", "மாநில சட்டமன்றத் தேர்தல்கள்"),
            ("Rajya Sabha elections", "மாநிலங்களவைத் தேர்தல்கள்"),
            ("Lok Sabha general elections", "மக்களவை பொதுத்தேர்தல்கள்"),
            ("Municipal Corporation elections", "மாநகராட்சி மன்றத் தேர்தல்கள்")
        ],
        "correct_idx": 1, # Rajya Sabha elections
        "exp_en": "In August 2018, a three-judge Supreme Court bench headed by CJI Dipak Misra ruled that NOTA is meant solely for direct general elections with secret ballot and cannot be applied to indirect elections like Rajya Sabha held via proportional representation with open ballot.",
        "exp_ta": "2018 ஆகஸ்டில், நேரடி பொதுத்தேர்தல்களுக்கு மட்டுமே நோட்டா பொருந்தும் என்றும், விகிதாச்சார திறந்த வாக்குச்சீட்டு முறையில் நடைபெறும் மாநிலங்களவைத் தேர்தல்களுக்கு நோட்டா பொருந்தாது என்றும் உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
        "tip": "NOTA is inapplicable to Rajya Sabha elections and Legislative Council elections.",
        "fact": "The Court observed that allowing NOTA in Rajya Sabha could encourage horse-trading and violate party whip discipline.",
        "diff": "Hard",
        "subtopic": "NOTA & Voter Rights"
    },

    # 11
    {
        "exam": "TNPSC Group 2 2019",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 2 2019",
        "stem_en": "Which section was inserted into the Representation of the People Act 1951 in 2009 to prohibit the conduct and publication of exit polls during elections?",
        "stem_ta": "தேர்தல் காலங்களில் எக்சிட் போல் (Exit Poll) நடத்துவதையும் வெளியிடுவதையும் தடை செய்ய 2009-ல் 1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தில் சேர்க்கப்பட்ட பிரிவு எது?",
        "options": [
            ("Section 126", "பிரிவு 126"),
            ("Section 126A", "பிரிவு 126A"),
            ("Section 127", "பிரிவு 127"),
            ("Section 128", "பிரிவு 128")
        ],
        "correct_idx": 1, # Section 126A
        "exp_en": "Section 126A was inserted into RPA 1951 by Act 41 of 2009, imposing a complete statutory ban on exit polls from the start of the first voting phase until half an hour after polling closes in the final phase.",
        "exp_ta": "2009-ல் இயற்றப்பட்ட திருத்தச் சட்டம் மூலம் பிரிவு 126A சேர்க்கப்பட்டு, முதல் கட்ட வாக்குப்பதிவு தொடங்கியது முதல் இறுதிக் கட்ட வாக்குப்பதிவு முடிந்து அரை மணி நேரம் வரை எக்சிட் போல் வெளியிட முழு தடை விதிக்கப்பட்டது.",
        "tip": "Sec 126 covers the 48-hour silent period; Sec 126A covers the exit poll ban.",
        "fact": "Violation of Section 126A carries imprisonment for a term up to two years or fine or both.",
        "diff": "Medium",
        "subtopic": "Campaign Regulations"
    },

    # 12
    {
        "exam": "TNPSC Group 1 2019",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 1 2019",
        "stem_en": "Under Section 33(7) of the Representation of the People Act 1951, inserted in 1996, a candidate can contest a general election from how many constituencies at most?",
        "stem_ta": "1996-ல் சேர்க்கப்பட்ட 1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 33(7)-ன் கீழ், ஒரு வேட்பாளர் பொதுத்தேர்தலில் அதிகபட்சமாக எத்தனை தொகுதிகளிலிருந்து மட்டுமே போட்டியிட முடியும்?",
        "options": [
            ("Only one constituency", "ஒரே ஒரு தொகுதியில் மட்டும்"),
            ("Maximum two constituencies", "அதிகபட்சம் இரண்டு தொகுதிகளில்"),
            ("Maximum three constituencies", "அதிகபட்சம் மூன்று தொகுதிகளில்"),
            ("No restriction on number of constituencies", "தொகுதிகளின் எண்ணிக்கையில் எந்தக் கட்டுப்பாடும் இல்லை")
        ],
        "correct_idx": 1, # Maximum two constituencies
        "exp_en": "By the Representation of the People (Amendment) Act 1996, Section 33(7) was inserted restricting a candidate from contesting from more than two parliamentary or assembly constituencies in a general or bye-election.",
        "exp_ta": "1996-ல் மக்கள் பிரதிநிதித்துவச் சட்டத்தில் சேர்க்கப்பட்ட பிரிவு 33(7)-ன் கீழ், ஒரு வேட்பாளர் அதிகபட்சமாக இரண்டு பாராளுமன்ற அல்லது சட்டமன்ற தொகுதிகளில் மட்டுமே போட்டியிட முடியும்.",
        "tip": "Prior to 1996, a candidate could contest from any number of constituencies.",
        "fact": "The Law Commission and ECI have consistently recommended amending Section 33(7) to restrict candidates to a single seat.",
        "diff": "Easy",
        "subtopic": "Candidate Nominations"
    },

    # 13
    {
        "exam": "TNPSC Group 2 2018",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 2 2018",
        "stem_en": "Which section was inserted into the Representation of the People Act 1951 in 1989 empowering the Election Commission to countermand an election or adjourn polling in cases of booth capturing?",
        "stem_ta": "வாக்குச்சாவடி கைப்பற்றப்படும் நிகழ்வுகளில் தேர்தலை ரத்து செய்ய அல்லது ஒத்திவைக்க தேர்தல் ஆணையத்திற்கு அதிகாரமளித்து 1989-ல் 1951 சட்டத்தில் சேர்க்கப்பட்ட பிரிவு எது?",
        "options": [
            ("Section 57", "பிரிவு 57"),
            ("Section 58A", "பிரிவு 58A"),
            ("Section 60", "பிரிவு 60"),
            ("Section 62", "பிரிவு 62")
        ],
        "correct_idx": 1, # Section 58A
        "exp_en": "Section 58A was inserted into the RPA 1951 with effect from 15 March 1989, specifically conferring power upon the Election Commission to adjourn poll or countermand election in that constituency upon booth capturing.",
        "exp_ta": "1989 மார்ச் 15 முதல் அமலுக்கு வந்த மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 58A, பூத் கைப்பற்றல் நடந்தால் வாக்குப்பதிவை ஒத்திவைக்க அல்லது தேர்தலை ரத்து செய்ய தேர்தல் ஆணையத்திற்கு அதிகாரம் அளிக்கிறது.",
        "tip": "Booth capturing was made a corrupt practice under Sec 123(8) and an offence under Sec 135A in 1989.",
        "fact": "Under Section 135A, booth capturing is punishable with imprisonment up to 5 years for government servants.",
        "diff": "Medium",
        "subtopic": "Electoral Offences"
    },

    # 14
    {
        "exam": "TNPSC Group 1 2017",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 1 2017",
        "stem_en": "Under which section of the Representation of the People Act 1951 are political parties in India registered with the Election Commission?",
        "stem_ta": "1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் எந்தப் பிரிவின் கீழ் இந்தியாவில் உள்ள அரசியல் கட்சிகள் தேர்தல் ஆணையத்தில் பதிவு செய்யப்படுகின்றன?",
        "options": [
            ("Section 25", "பிரிவு 25"),
            ("Section 29A", "பிரிவு 29A"),
            ("Section 32", "பிரிவு 32"),
            ("Section 35", "பிரிவு 35")
        ],
        "correct_idx": 1, # Section 29A
        "exp_en": "Section 29A was inserted into Part IVA of the Representation of the People Act 1951 in 1988, providing the statutory mechanism for registration of associations and political parties with the Election Commission.",
        "exp_ta": "1988-ல் மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பகுதி IVA-ல் சேர்க்கப்பட்ட பிரிவு 29A, அரசியல் கட்சிகள் தேர்தல் ஆணையத்தில் பதிவு செய்வதற்கான சட்டப்பூர்வ வழிமுறையை வழங்குகிறது.",
        "tip": "A party must apply for registration within 30 days of its formation under Section 29A.",
        "fact": "Parties registered under Section 29A must bear true faith and allegiance to the Constitution of India.",
        "diff": "Easy",
        "subtopic": "Political Parties"
    },

    # 15
    {
        "exam": "TNPSC Group 1 2019",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 1 2019",
        "stem_en": "Under Section 10A of the Representation of the People Act 1951, what is the maximum period of disqualification imposed on a candidate for failing to lodge an account of election expenses?",
        "stem_ta": "1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 10A-ன் கீழ், தேர்தல் செலவுக் கணக்கை தாக்கல் செய்யத் தவறும் ஒரு வேட்பாளருக்கு விதிக்கப்படும் அதிகபட்ச தகுதிநீக்கக் காலம் என்ன?",
        "options": [
            ("1 year", "1 ஆண்டு"),
            ("3 years", "3 ஆண்டுகள்"),
            ("5 years", "5 ஆண்டுகள்"),
            ("6 years", "6 ஆண்டுகள்")
        ],
        "correct_idx": 1, # 3 years
        "exp_en": "Under Section 10A of RPA 1951, if the Election Commission is satisfied that a person has failed to lodge an account of election expenses within time without good reason, it shall declare him disqualified for 3 years from the date of the order.",
        "exp_ta": "1951 சட்டத்தின் பிரிவு 10A-ன் கீழ், தேர்தல் செலவு கணக்கை குறித்த காலத்திற்குள் தாக்கல் செய்யாத வேட்பாளரை தேர்தல் ஆணையம் தனது உத்தரவு தேதியிலிருந்து 3 ஆண்டுகளுக்கு தகுதிநீக்கம் செய்ய முடியும்.",
        "tip": "Section 10A = 3 years disqualification by Election Commission.",
        "fact": "Under Section 11, the Election Commission has the statutory power to remove or reduce the period of disqualification.",
        "diff": "Medium",
        "subtopic": "Electoral Expenditure"
    },

    # 16
    {
        "exam": "TNPSC Group 4 2019",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 4 2019",
        "stem_en": "Under Section 126 of the Representation of the People Act 1951, public meetings and election campaign propaganda must cease how many hours before the conclusion of the poll?",
        "stem_ta": "1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 126-ன் கீழ், வாக்குப்பதிவு முடிவடைவதற்கு எத்தனை மணி நேரத்திற்கு முன்னதாக பொதுக்கூட்டங்கள் மற்றும் பிரச்சாரங்கள் நிறுத்தப்பட வேண்டும்?",
        "options": [
            ("24 hours", "24 மணி நேரம்"),
            ("48 hours", "48 மணி நேரம்"),
            ("72 hours", "72 மணி நேரம்"),
            ("36 hours", "36 மணி நேரம்")
        ],
        "correct_idx": 1, # 48 hours
        "exp_en": "Section 126 of the RPA 1951 prohibits holding public meetings, processions, musical concerts, and theatrical performances during the period of 48 hours ending with the hour fixed for the conclusion of the poll.",
        "exp_ta": "1951 சட்டத்தின் பிரிவு 126-ன் கீழ், வாக்குப்பதிவு முடிவடைய நிர்ணயிக்கப்பட்ட நேரத்திற்கு முந்தைய 48 மணி நேர அமைதிக்காலத்தில் எந்தவொரு பொதுக்கூட்டமோ பிரச்சாரமோ நடத்த தடை விதிக்கப்பட்டுள்ளது.",
        "tip": "Known as the 'Silence Period' or 'Cooling-off Period' lasting 48 hours.",
        "fact": "Door-to-door campaigning by candidates is permitted during this 48-hour window as long as no public gathering is formed.",
        "diff": "Easy",
        "subtopic": "Campaign Regulations"
    },

    # 17
    {
        "exam": "TNPSC Group 2 2018",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 2 2018",
        "stem_en": "In 1996, the minimum campaign period between the last date for withdrawal of candidatures and the date of polling was reduced from 21 days to how many days?",
        "stem_ta": "1996-ல், வேட்புமனு திரும்பப் பெறுவதற்கான கடைசி தேதிக்கும் வாக்குப்பதிவு தேதிக்கும் இடைப்பட்ட குறைந்தபட்ச பிரச்சார காலம் 21 நாட்களிலிருந்து எத்தனை நாட்களாக குறைக்கப்பட்டது?",
        "options": [
            ("10 days", "10 நாட்கள்"),
            ("14 days", "14 நாட்கள்"),
            ("15 days", "15 நாட்கள்"),
            ("18 days", "18 நாட்கள்")
        ],
        "correct_idx": 1, # 14 days
        "exp_en": "Under Section 30(c) of RPA 1951 amended in 1996, the minimum campaign period was shortened from 21 days to 14 days to reduce election costs, voter fatigue, and law-and-order strains.",
        "exp_ta": "1996-ல் திருத்தப்பட்ட 1951 சட்டத்தின் பிரிவு 30(c)-ன் கீழ், தேர்தல் செலவு மற்றும் பாதுகாப்பு சிரமங்களைக் குறைக்க பிரச்சார காலம் 21 நாட்களிலிருந்து 14 நாட்களாக குறைக்கப்பட்டது.",
        "tip": "Minimum campaign period is now 14 days.",
        "fact": "This reform was recommended by the Dinesh Goswami Committee (1990).",
        "diff": "Medium",
        "subtopic": "Campaign Regulations"
    },

    # 18
    {
        "exam": "TNPSC Group 1 2011",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 1 2011",
        "stem_en": "Which Article of the Constitution of India provides that elections to the Lok Sabha and State Legislative Assemblies shall be on the basis of adult suffrage?",
        "stem_ta": "மக்களவை மற்றும் மாநில சட்டமன்றங்களுக்கான தேர்தல்கள் வயதுவந்தோர் வாக்குரிமையின் அடிப்படையில் அமைய வேண்டும் என்று கூறும் இந்திய அரசியலமைப்பு சரத்து எது?",
        "options": [
            ("Article 324", "சரத்து 324"),
            ("Article 326", "சரத்து 326"),
            ("Article 327", "சரத்து 327"),
            ("Article 328", "சரத்து 328")
        ],
        "correct_idx": 1, # Article 326
        "exp_en": "Article 326 explicitly provides that elections to the House of the People and to the Legislative Assembly of every State shall be on the basis of adult suffrage for every citizen who is not less than eighteen years of age.",
        "exp_ta": "சரத்து 326, 18 வயதுக்கு குறையாத ஒவ்வொரு குடிமகனுக்கும் வயதுவந்தோர் வாக்குரிமை அடிப்படையில் மக்களவை மற்றும் சட்டமன்ற தேர்தல்கள் நடைபெற வேண்டும் என்று தெளிவாக கூறுகிறது.",
        "tip": "Article 326 is the constitutional bedrock of universal adult franchise in India.",
        "fact": "Article 326 allows disqualification on grounds of non-residence, unsoundness of mind, crime, or corrupt or illegal practice.",
        "diff": "Easy",
        "subtopic": "Constitutional Provisions"
    },

    # 19
    {
        "exam": "TNPSC Group 1 2015",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 1 2015",
        "stem_en": "Under Article 329(a) of the Constitution of India, the validity of any law relating to the delimitation of constituencies cannot be called in question in which forum?",
        "stem_ta": "இந்திய அரசியலமைப்பின் சரத்து 329(a)-ன் கீழ், தொகுதி மறுவரையறை தொடர்பான எந்தவொரு சட்டத்தின் செல்லுபடியாகும் தன்மையையும் எந்த அமைப்பிலும் கேள்வி கேட்க முடியாது?",
        "options": [
            ("Only in the Supreme Court", "உச்ச நீதிமன்றத்தில் மட்டுமே"),
            ("In any court of law", "எந்தவொரு நீதிமன்றத்திலும்"),
            ("Only in the Parliament", "நாடாளுமன்றத்தில் மட்டுமே"),
            ("Only before the Election Commission", "தேர்தல் ஆணையத்தின் முன் மட்டுமே")
        ],
        "correct_idx": 1, # In any court of law
        "exp_en": "Article 329(a) imposes an absolute constitutional bar stating that the validity of any law relating to the delimitation of constituencies or allotment of seats shall not be called in question in any court.",
        "exp_ta": "சரத்து 329(a), தொகுதி மறுவரையறை அல்லது இடங்கள் ஒதுக்கீடு தொடர்பான எந்தவொரு சட்டத்தின் செல்லுபடியாகும் தன்மையையும் எந்தவொரு நீதிமன்றத்திலும் கேள்வி கேட்க முடியாது என்று முழுமையான தடை விதிக்கிறது.",
        "tip": "Article 329 bars judicial interference in delimitation orders and election processes.",
        "fact": "Once published in the Gazette of India, Delimitation Commission orders have the full force of law.",
        "diff": "Medium",
        "subtopic": "Delimitation & Judicial Review"
    },

    # 20
    {
        "exam": "UPSC CSE 2017 / TNPSC Gr 1 2022",
        "exam_ta": "யுபிஎஸ்சி 2017 / டிஎன்பிஎஸ்சி குரூப் 1 2022",
        "stem_en": "Right to vote and to be elected in India is classified legally as which of the following?",
        "stem_ta": "இந்தியாவில் வாக்களிக்கும் உரிமை மற்றும் தேர்தலில் போட்டியிடும் உரிமை சட்டப்பூர்வமாக எவ்வாறு வகைப்படுத்தப்படுகிறது?",
        "options": [
            ("Fundamental Right", "அடிப்படை உரிமை"),
            ("Constitutional / Statutory Right", "அரசியலமைப்பு / சட்டப்பூர்வ உரிமை"),
            ("Natural Right", "இயற்கை உரிமை"),
            ("Fundamental Duty", "அடிப்படை கடமை")
        ],
        "correct_idx": 1, # Constitutional / Statutory Right
        "exp_en": "In Jyoti Basu v. Debi Ghosal (1982) and PUCL (2003), the Supreme Court ruled that the right to vote and contest an election is not a common law right or Fundamental Right, but a statutory/constitutional right subject to statutory limitations.",
        "exp_ta": "ஜோதி பாசு எதிர் தேபி கோஷல் (1982) வழக்கில், வாக்களிக்கும் மற்றும் போட்டியிடும் உரிமை என்பது அடிப்படை உரிமை அல்ல, மாறாக சட்டத்தால் ஒழுங்குபடுத்தப்படும் அரசியலமைப்பு / சட்டப்பூர்வ உரிமை என உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
        "tip": "Right to vote is rooted in Article 326 and governed by RPA 1950/1951.",
        "fact": "In Anoop Baranwal (2023), Justice K.M. Joseph noted that right to vote is a constitutional right under Article 326.",
        "diff": "Medium",
        "subtopic": "Voting Rights & Franchise"
    },

    # 21
    {
        "exam": "TNPSC Group 1 2014",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 1 2014",
        "stem_en": "Which Constitutional Amendment Act froze the readjustment of Lok Sabha and State Legislative Assembly seats till the year 2026?",
        "stem_ta": "எந்த அரசியலமைப்பு திருத்தச் சட்டம் மக்களவை மற்றும் சட்டமன்ற இடங்களின் மறுசீரமைப்பை 2026 ஆம் ஆண்டு வரை முடக்கியது?",
        "options": [
            ("42nd Amendment Act (1976)", "42-வது திருத்தச் சட்டம் (1976)"),
            ("84th Amendment Act (2001)", "84-வது திருத்தச் சட்டம் (2001)"),
            ("87th Amendment Act (2003)", "87-வது திருத்தச் சட்டம் (2003)"),
            ("91st Amendment Act (2003)", "91-வது திருத்தச் சட்டம் (2003)"),
        ],
        "correct_idx": 1, # 84th Amendment Act (2001)
        "exp_en": "The Constitution (84th Amendment) Act 2001 extended the freeze on total seats in Lok Sabha and Legislative Assemblies (originally imposed by 42nd Amendment till 2000) up to the year 2026.",
        "exp_ta": "84-வது அரசியலமைப்பு திருத்தச் சட்டம் 2001, மக்களவை மற்றும் சட்டமன்றங்களின் மொத்த இடங்கள் மீதான முடக்கத்தை (முதலில் 42-வது திருத்தத்தால் 2000 வரை விதிக்கப்பட்டது) 2026 வரை நீட்டித்தது.",
        "tip": "The freeze ensures states with successful population control are not penalized with fewer parliamentary seats.",
        "fact": "The freeze will remain in place until the first census taken after the year 2026 is published.",
        "diff": "Easy",
        "subtopic": "Delimitation of Constituencies"
    },

    # 22
    {
        "exam": "TNPSC Group 2 2015",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 2 2015",
        "stem_en": "The 87th Constitutional Amendment Act 2003 provided for the delimitation of constituencies on the basis of which Census figures?",
        "stem_ta": "87-வது அரசியலமைப்பு திருத்தச் சட்டம் 2003 எந்த மக்கள் தொகை கணக்கெடுப்பின் அடிப்படையில் தொகுதி மறுவரையறை செய்ய வகை செய்தது?",
        "options": [
            ("1971 Census", "1971 மக்கள் தொகை கணக்கெடுப்பு"),
            ("2001 Census", "2001 மக்கள் தொகை கணக்கெடுப்பு"),
            ("1991 Census", "1991 மக்கள் தொகை கணக்கெடுப்பு"),
            ("2011 Census", "2011 மக்கள் தொகை கணக்கெடுப்பு")
        ],
        "correct_idx": 1, # 2001 Census
        "exp_en": "The 84th Amendment Act 2001 had initially provided for rationalization of constituencies based on the 1991 Census. The 87th Amendment Act 2003 amended this to the 2001 Census without altering total state seats.",
        "exp_ta": "84-வது திருத்தம் 1991 கணக்கெடுப்பை நிர்ணயித்திருந்த நிலையில், 87-வது திருத்தச் சட்டம் 2003 அதை மாற்றி 2001 மக்கள் தொகை கணக்கெடுப்பின் அடிப்படையில் தொகுதி மறுவரையறை செய்ய வகை செய்தது.",
        "tip": "Total seats were kept constant, but constituency boundaries within each state were adjusted.",
        "fact": "The Delimitation Commission chaired by Justice Kuldip Singh completed this exercise in 2008.",
        "diff": "Medium",
        "subtopic": "Delimitation of Constituencies"
    },

    # 23
    {
        "exam": "TNPSC Group 4 2016",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 4 2016",
        "stem_en": "Electronic Voting Machines (EVMs) were first used on an experimental pilot basis in 1982 in which Legislative Assembly constituency?",
        "stem_ta": "1982-ல் மின்னணு வாக்குப்பதிவு இயந்திரங்கள் (EVM) முதன்முதலில் எந்த சட்டமன்றத் தொகுதியில் முன்னோடி அடிப்படையில் பயன்படுத்தப்பட்டன?",
        "options": [
            ("Noksen (Nagaland)", "நோக்சென் (நாகாலாந்து)"),
            ("Paravur (Kerala)", "பரவூர் (கேரளா)"),
            ("Bodinayakanur (Tamil Nadu)", "போடிநாயக்கனூர் (தமிழ்நாடு)"),
            ("Rajouri (Jammu & Kashmir)", "ரஜோரி (ஜம்மு & காஷ்மீர்)")
        ],
        "correct_idx": 1, # Paravur (Kerala)
        "exp_en": "EVMs were first deployed in May 1982 in 50 polling stations of the Paravur Assembly Constituency in Kerala during bye-elections.",
        "exp_ta": "1982 மே மாதம் கேரள மாநிலத்தின் பரவூர் சட்டமன்றத் தொகுதி இடைத்தேர்தலில் 50 வாக்குச்சாவடிகளில் EVM முதன்முதலில் சோதனை முறையில் பயன்படுத்தப்பட்டது.",
        "tip": "Paravur is in Ernakulam district of Kerala.",
        "fact": "The Supreme Court later set aside the Paravur election in A.C. Jose v. Sivan Pillai because the law had not yet authorized EVM use.",
        "diff": "Easy",
        "subtopic": "Electronic Voting & Technology"
    },

    # 24
    {
        "exam": "TNPSC Group 2 2019",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 2 2019",
        "stem_en": "Which section was added to the Representation of the People Act 1951 in 1989 providing express legal sanction for the use of Electronic Voting Machines?",
        "stem_ta": "மின்னணு வாக்குப்பதிவு இயந்திரங்களின் பயன்பாட்டிற்கு தெளிவான சட்டப்பூர்வ அனுமதியை வழங்க 1989-ல் 1951 சட்டத்தில் சேர்க்கப்பட்ட பிரிவு எது?",
        "options": [
            ("Section 58", "பிரிவு 58"),
            ("Section 61A", "பிரிவு 61A"),
            ("Section 65", "பிரிவு 65"),
            ("Section 69", "பிரிவு 69")
        ],
        "correct_idx": 1, # Section 61A
        "exp_en": "Following the Supreme Court's ruling in A.C. Jose, Parliament enacted Section 61A of RPA 1951 in December 1988 (effective March 1989) empowering the ECI to specify voting by voting machines.",
        "exp_ta": "ஏ.சி. ஜோஸ் வழக்கைத் தொடர்ந்து, 1989 மார்ச்சில் அமலுக்கு வந்த பிரிவு 61A மூலம் வாக்குப்பதிவு இயந்திரங்களைப் பயன்படுத்த தேர்தல் ஆணையத்திற்கு சட்டப்பூர்வ அதிகாரம் வழங்கப்பட்டது.",
        "tip": "Section 61A provides the statutory foundation for EVM usage in India.",
        "fact": "The validity of Section 61A was upheld by the Madras High Court in 2001.",
        "diff": "Medium",
        "subtopic": "Electronic Voting & Technology"
    },

    # 25
    {
        "exam": "TNPSC Group 1 2017",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 1 2017",
        "stem_en": "In which General Elections to the Lok Sabha were Electronic Voting Machines (EVMs) used 100% across all polling stations in the country for the first time?",
        "stem_ta": "இந்தியாவில் எந்த மக்களவை பொதுத்தேர்தலில் முதன்முதலாக நாடு முழுவதும் உள்ள அனைத்து வாக்குச்சாவடிகளிலும் 100% EVM பயன்படுத்தப்பட்டது?",
        "options": [
            ("1999 General Elections", "1999 பொதுத்தேர்தல்"),
            ("2004 General Elections", "2004 பொதுத்தேர்தல்"),
            ("2009 General Elections", "2009 பொதுத்தேர்தல்"),
            ("2014 General Elections", "2014 பொதுத்தேர்தல்")
        ],
        "correct_idx": 1, # 2004 General Elections
        "exp_en": "In the 14th Lok Sabha General Elections in 2004, EVMs were deployed across all 543 parliamentary constituencies across India, completely replacing paper ballots.",
        "exp_ta": "2004-ல் நடைபெற்ற 14-வது மக்களவை பொதுத்தேர்தலில், நாடு முழுவதும் உள்ள அனைத்து 543 தொகுதிகளிலும் காகித வாக்குச்சீட்டுகளுக்கு பதிலாக 100% EVM பயன்படுத்தப்பட்டது.",
        "tip": "2004 was the historic transition point to nationwide electronic voting.",
        "fact": "Over 1 million EVMs were used in the 2004 elections, saving thousands of tonnes of paper.",
        "diff": "Easy",
        "subtopic": "Electronic Voting & Technology"
    },

    # 26
    {
        "exam": "TNPSC Group 2 2018",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 2 2018",
        "stem_en": "In which constituency was the Voter Verifiable Paper Audit Trail (VVPAT) system first deployed on a pilot basis in September 2013?",
        "stem_ta": "2013 செப்டம்பரில் விவிபேட் (VVPAT) முறை முதன்முதலில் எந்த சட்டமன்றத் தொகுதியில் முன்னோடி அடிப்படையில் பயன்படுத்தப்பட்டது?",
        "options": [
            ("Tuensang (Nagaland)", "துயேன்சாங் (நாகாலாந்து)"),
            ("Noksen (Nagaland)", "நோக்சென் (நாகாலாந்து)"),
            ("Wokha (Nagaland)", "வோகா (நாகாலாந்து)"),
            ("Mokokchung (Nagaland)", "மோகோக்சுங் (நாகாலாந்து)")
        ],
        "correct_idx": 1, # Noksen (Nagaland)
        "exp_en": "VVPAT was first deployed on 4 September 2013 in the bye-election to the Noksen Assembly Constituency in Nagaland.",
        "exp_ta": "2013 செப்டம்பர் 4 அன்று நாகாலாந்து மாநிலத்தின் நோக்சென் சட்டமன்றத் தொகுதி இடைத்தேர்தலில் VVPAT முதன்முதலில் பயன்படுத்தப்பட்டது.",
        "tip": "VVPAT print slip is visible behind a transparent glass window for 7 seconds.",
        "fact": "The Conduct of Elections Rules 1961 were amended on 14 August 2013 to formally notify Rule 49A allowing VVPATs.",
        "diff": "Medium",
        "subtopic": "VVPAT System"
    },

    # 27
    {
        "exam": "TNPSC Group 1 2019",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 1 2019",
        "stem_en": "In Dr. Subramanian Swamy v. Election Commission of India (2013), what did the Supreme Court hold regarding the VVPAT system?",
        "stem_ta": "டாக்டர் சுப்பிரமணியன் சுவாமி எதிர் இந்திய தேர்தல் ஆணையம் (2013) வழக்கில், VVPAT முறை குறித்து உச்ச நீதிமன்றம் என்ன தீர்ப்பளித்தது?",
        "options": [
            ("EVMs should be discontinued and paper ballots restored", "EVM இயந்திரங்கள் கைவிடப்பட்டு காகித வாக்குச்சீட்டுகள் மீண்டும் கொண்டுவரப்பட வேண்டும்"),
            ("A paper trail (VVPAT) is an indispensable requirement of free and fair elections", "காகித தணிக்கைத்தாள் (VVPAT) என்பது சுதந்திரமான மற்றும் நேர்மையான தேர்தலுக்கு இன்றியமையாதது"),
            ("VVPAT is optional and left to state discretion", "VVPAT என்பது விருப்பத்தேர்வு மட்டுமே, மாநிலங்களின் முடிவுக்கு விடப்படுகிறது"),
            ("VVPAT should be used only in urban constituencies", "நகர்ப்புற தொகுதிகளில் மட்டுமே VVPAT பயன்படுத்தப்பட வேண்டும்")
        ],
        "correct_idx": 1, # indispensable requirement
        "exp_en": "On 8 October 2013, a Supreme Court bench headed by Justice P. Sathasivam held that 'paper trail is an indispensable requirement of free and fair elections' and directed the Centre to provide funds for phased VVPAT rollout.",
        "exp_ta": "2013 அக்டோபர் 8 அன்று, 'சுதந்திரமான மற்றும் நேர்மையான தேர்தலுக்கு காகித தணிக்கைத்தாள் (VVPAT) இன்றியமையாதது' என்று உச்ச நீதிமன்றம் தீர்ப்பளித்து, படிப்படியாக விவிபேட் வாங்க நிதி ஒதுக்க மத்திய அரசுக்கு உத்தரவிட்டது.",
        "tip": "This judgment paved the way for 100% VVPAT deployment across all polling booths by 2019.",
        "fact": "The Court recognized that VVPAT guarantees voter confidence by providing immediate physical verification.",
        "diff": "Hard",
        "subtopic": "VVPAT System"
    },

    # 28
    {
        "exam": "TNPSC Group 1 2021",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 1 2021",
        "stem_en": "In N. Chandrababu Naidu v. Union of India (April 2019), the Supreme Court increased mandatory physical VVPAT slip verification from 1 polling station to how many per Assembly constituency?",
        "stem_ta": "என். சந்திரபாபு நாயுடு எதிர் இந்திய ஒன்றியம் (ஏப்ரல் 2019) வழக்கில், கட்டாய VVPAT சீட்டு சரிபார்ப்பை ஒரு வாக்குச்சாவடியிலிருந்து ஒரு சட்டமன்றத் தொகுதிக்கு எத்தனை வாக்குச்சாவடிகளாக உச்ச நீதிமன்றம் உயர்த்தியது?",
        "options": [
            ("2 polling stations", "2 வாக்குச்சாவடிகள்"),
            ("5 polling stations", "5 வாக்குச்சாவடிகள்"),
            ("10 polling stations", "10 வாக்குச்சாவடிகள்"),
            ("50% of all polling stations", "50% வாக்குச்சாவடிகள்")
        ],
        "correct_idx": 1, # 5 polling stations
        "exp_en": "On 8 April 2019, CJI Ranjan Gogoi's bench directed the ECI to increase physical verification of VVPAT slips from 1 to 5 randomly selected polling stations per assembly segment in every Parliamentary and Assembly constituency.",
        "exp_ta": "2019 ஏப்ரல் 8 அன்று, ஒவ்வொரு சட்டமன்ற தொகுதியிலும் குலுக்கல் முறையில் தேர்ந்தெடுக்கப்படும் 5 வாக்குச்சாவடிகளில் VVPAT சீட்டுகளை கட்டாயம் சரிபார்க்க வேண்டும் என உச்ச நீதிமன்றம் உத்தரவிட்டது.",
        "tip": "Increased from 1 to 5 randomly selected polling booths per assembly segment.",
        "fact": "The Court observed that this enhanced verification would satisfy both public confidence and counting speed.",
        "diff": "Medium",
        "subtopic": "VVPAT System"
    },

    # 29
    {
        "exam": "TNPSC Group 2 2016",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 2 2016",
        "stem_en": "Voting rights were extended to Non-Resident Indians (NRIs) who have not acquired citizenship of any other country through which legislative amendment?",
        "stem_ta": "வேறு எந்த நாட்டின் குடியுரிமையையும் பெறாத வெளிநாடு வாழ் இந்தியர்களுக்கு (NRI) எந்த சட்டத் திருத்தத்தின் மூலம் வாக்களிக்கும் உரிமை வழங்கப்பட்டது?",
        "options": [
            ("Representation of the People (Amendment) Act, 1996", "மக்கள் பிரதிநிதித்துவ (திருத்த) சட்டம், 1996"),
            ("Representation of the People (Amendment) Act, 2010", "மக்கள் பிரதிநிதித்துவ (திருத்த) சட்டம், 2010"),
            ("Election Laws (Amendment) Act, 2016", "தேர்தல் சட்டங்கள் (திருத்த) சட்டம், 2016"),
            ("Citizenship (Amendment) Act, 2003", "குடியுரிமை (திருத்த) சட்டம், 2003")
        ],
        "correct_idx": 1, # Act of 2010
        "exp_en": "The Representation of the People (Amendment) Act 2010 inserted Section 20A into the RPA 1950, allowing overseas Indian citizens who hold valid Indian passports to register as electors and cast their vote in person.",
        "exp_ta": "2010-ல் மக்கள் பிரதிநிதித்துவச் சட்டத்தில் சேர்க்கப்பட்ட பிரிவு 20A மூலம், செல்லுபடியாகும் இந்திய பாஸ்போர்ட் வைத்துள்ள வெளிநாடு வாழ் இந்தியர்கள் வாக்காளராகப் பதிவு செய்து நேரில் வாக்களிக்க அனுமதிக்கப்பட்டனர்.",
        "tip": "NRIs can vote in person at the polling booth where their passport address is registered.",
        "fact": "Over 1.15 lakh overseas electors are enrolled on Indian electoral rolls.",
        "diff": "Medium",
        "subtopic": "Voting Rights & Franchise"
    },

    # 30
    {
        "exam": "TNPSC Group 1 2022",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 1 2022",
        "stem_en": "The Electronically Transmitted Postal Ballot System (ETPBS) was introduced by the Election Commission of India for which category of electors?",
        "stem_ta": "மின்னணு முறையில் அனுப்பப்படும் தபால் வாக்கு முறை (ETPBS) இந்திய தேர்தல் ஆணையத்தால் எந்த வகை வாக்காளர்களுக்காக அறிமுகப்படுத்தப்பட்டது?",
        "options": [
            ("Overseas / NRI voters", "வெளிநாடு வாழ் இந்திய வாக்காளர்கள்"),
            ("Service Voters (Armed Forces & Central Armed Police Forces)", "பணி வாக்காளர்கள் (இராணுவம் மற்றும் மத்திய ஆயுதக் காவல் படைகள்)"),
            ("Private sector corporate employees", "தனியார் துறை கார்ப்பரேட் ஊழியர்கள்"),
            ("All senior citizen electors", "அனைத்து மூத்த குடிமக்கள் வாக்காளர்கள்")
        ],
        "correct_idx": 1, # Service Voters
        "exp_en": "ETPBS was launched in 2016 for service voters, allowing postal ballots to be transmitted electronically to designated service voters to eliminate postal transit delays.",
        "exp_ta": "அஞ்சல் தாமதங்களைத் தவிர்க்க, இராணுவ மற்றும் பாதுகாப்புப் படை பணி வாக்காளர்களுக்கு மின்னணு முறையில் தபால் வாக்குகளை அனுப்ப 2016-ல் ETPBS திட்டம் தொடங்கப்பட்டது.",
        "tip": "Ballot is sent electronically to the voter, but returned by ordinary post in encrypted envelope.",
        "fact": "ETPBS is secured using two layers of PIN and a unique QR code on each ballot.",
        "diff": "Medium",
        "subtopic": "Voting Rights & Franchise"
    },

    # 31
    {
        "exam": "TNPSC Group 1 2022",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 1 2022",
        "stem_en": "The Election Laws (Amendment) Act, 2021 amended the Representation of the People Act 1950 to provide how many qualifying dates per year for voter registration?",
        "stem_ta": "தேர்தல் சட்டங்கள் (திருத்த) சட்டம் 2021, வாக்காளர் பதிவுக்கு ஆண்டுக்கு எத்தனை தகுதி தேதிகளை வழங்க 1950 சட்டத்தைத் திருத்தியது?",
        "options": [
            ("Two qualifying dates", "இரண்டு தகுதி தேதிகள்"),
            ("Four qualifying dates (Jan 1, Apr 1, Jul 1, Oct 1)", "நான்கு தகுதி தேதிகள் (ஜனவரி 1, ஏப்ரல் 1, ஜூலை 1, அக்டோபர் 1)"),
            ("Three qualifying dates", "மூன்று தகுதி தேதிகள்"),
            ("Continuous daily registration throughout the year", "ஆண்டு முழுவதும் தொடர்ச்சியான தினசரி பதிவு")
        ],
        "correct_idx": 1, # Four qualifying dates
        "exp_en": "Under the Election Laws (Amendment) Act 2021, Section 14(b) of RPA 1950 was amended to replace the single 1st January qualifying date with four qualifying dates: 1st January, 1st April, 1st July, and 1st October.",
        "exp_ta": "2021 தேர்தல் சட்டத் திருத்தத்தின் மூலம் பிரிவு 14(b) திருத்தப்பட்டு, ஜனவரி 1 என்ற ஒற்றைத் தேதிக்கு பதிலாக ஜனவரி 1, ஏப்ரல் 1, ஜூலை 1, அக்டோபர் 1 என நான்கு தகுதி தேதிகள் அறிமுகப்படுத்தப்பட்டன.",
        "tip": "Young citizens turning 18 don't have to wait an entire year to register as voters.",
        "fact": "This historic reform enacted recommendations made by the Election Commission over several decades.",
        "diff": "Easy",
        "subtopic": "Electoral Roll Reforms"
    },

    # 32
    {
        "exam": "TNPSC Group 2 2022",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 2 2022",
        "stem_en": "Which statutory form was introduced by the Election Commission in 2022 for the voluntary collection and authentication of Aadhaar numbers of registered electors?",
        "stem_ta": "பதிவு செய்யப்பட்ட வாக்காளர்களின் ஆதார் எண்களை விருப்பத்தின் பேரில் பெற்று இணைக்க 2022-ல் தேர்தல் ஆணையத்தால் அறிமுகப்படுத்தப்பட்ட படிவம் எது?",
        "options": [
            ("Form 6A", "படிவம் 6A"),
            ("Form 6B", "படிவம் 6B"),
            ("Form 8A", "படிவம் 8A"),
            ("Form 12D", "படிவம் 12D")
        ],
        "correct_idx": 1, # Form 6B
        "exp_en": "Form 6B was introduced under the Registration of Electors (Amendment) Rules 2022 effective from 1 August 2022 for existing electors to furnish their Aadhaar number voluntarily.",
        "exp_ta": "2022 ஆகஸ்ட் 1 முதல் வாக்காளர்கள் தங்கள் ஆதார் எண்ணை விருப்பத்தின் பேரில் சமர்ப்பிக்க தேர்தல் விதிகளின் கீழ் படிவம் 6B அறிமுகப்படுத்தப்பட்டது.",
        "tip": "Submitting Aadhaar is voluntary; non-submission cannot lead to deletion of voter names.",
        "fact": "Form 6B can be submitted online through the Voter Helpline App or via Booth Level Officers (BLOs).",
        "diff": "Medium",
        "subtopic": "Electoral Roll Reforms"
    },

    # 33
    {
        "exam": "TNPSC Group 1 2020",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 1 2020",
        "stem_en": "Under Rule 4A of the Conduct of Elections Rules 1961, every candidate contesting an election must submit which affidavit along with nomination papers?",
        "stem_ta": "1961 தேர்தல் நடத்தை விதிகளின் விதி 4A-ன் கீழ், தேர்தலில் போட்டியிடும் ஒவ்வொரு வேட்பாளரும் வேட்புமனுவுடன் எந்த பிரமாணப் பத்திரத்தை தாக்கல் செய்ய வேண்டும்?",
        "options": [
            ("Form 20", "படிவம் 20"),
            ("Form 26", "படிவம் 26"),
            ("Form 16", "படிவம் 16"),
            ("Form 7A", "படிவம் 7A")
        ],
        "correct_idx": 1, # Form 26
        "exp_en": "Form 26 is the statutory affidavit prescribed under Rule 4A, in which candidates must swear details of criminal cases, convictions, pending FIRs, movable and immovable assets, liabilities, and educational qualifications.",
        "exp_ta": "விதி 4A-ன் கீழ் பரிந்துரைக்கப்பட்ட படிவம் 26 என்பது, வேட்பாளர்கள் தங்களின் குற்ற வழக்குகள், சொத்துக்கள், கடன்கள் மற்றும் கல்வித் தகுதியை பிரமாணப் பத்திரமாக தாக்கல் செய்யும் படிவமாகும்.",
        "tip": "Form 26 was introduced following the Supreme Court's ADR judgment in 2002.",
        "fact": "Filing a false affidavit or concealing information in Form 26 is punishable under Section 125A of RPA 1951.",
        "diff": "Easy",
        "subtopic": "Candidate Nominations"
    },

    # 34
    {
        "exam": "TNPSC Group 1 2022",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 1 2022",
        "stem_en": "In Public Interest Foundation v. Union of India (2018), what did the Supreme Court mandate regarding candidates with pending criminal cases?",
        "stem_ta": "பப்ளிக் இன்ட்ரஸ்ட் ஃபவுண்டேஷன் எதிர் இந்திய ஒன்றியம் (2018) வழக்கில், குற்ற வழக்கு நிலுவையில் உள்ள வேட்பாளர்கள் குறித்து உச்ச நீதிமன்றம் என்ன கட்டாயமாக்கியது?",
        "options": [
            ("Automatic debarment from contesting elections", "தேர்தலில் போட்டியிட தானியங்கி தடை"),
            ("Publishing their criminal antecedents in widely circulated newspapers and TV channels at least three times", "அதிக புழக்கத்தில் உள்ள செய்தித்தாள்கள் மற்றும் தொலைக்காட்சிகளில் குறைந்தது மூன்று முறை குற்ற விவரங்களை விளம்பரப்படுத்துதல்"),
            ("Submitting a separate security deposit of Rs 1 Lakh", "ரூ.1 லட்சம் தனி காப்புத்தொகை செலுத்துதல்"),
            ("Seeking prior clearance from the High Court", "உயர்நீதிமன்றத்தில் முன் அனுமதி பெறுதல்")
        ],
        "correct_idx": 1, # Publishing criminal antecedents 3 times
        "exp_en": "In September 2018, a 5-judge Constitution Bench directed that candidates with pending criminal cases and their political parties must publish declarations in newspapers and TV channels on three separate dates during the campaign.",
        "exp_ta": "குற்ற வழக்கு உள்ள வேட்பாளர்களும் அவர்களின் அரசியல் கட்சிகளும் பிரச்சார காலத்தில் குறைந்தது மூன்று முறை பரவலாக விநியோகிக்கப்படும் நாளிதழ்கள் மற்றும் தொலைக்காட்சிகளில் தங்களின் குற்ற விவரங்களை வெளியிட வேண்டும் என உச்ச நீதிமன்றம் உத்தரவிட்டது.",
        "tip": "Published at 3 intervals: within first 4 days, between 5th-8th day, and from 9th day to 48 hours before poll.",
        "fact": "This directive applies to both recognized political parties and independent candidates.",
        "diff": "Hard",
        "subtopic": "Decriminalization of Politics"
    },

    # 35
    {
        "exam": "TNPSC Group 2 2018",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 2 2018",
        "stem_en": "In Resurgence India v. Election Commission of India (2013), what did the Supreme Court direct the Returning Officer to do if a candidate leaves columns blank in Form 26 affidavit?",
        "stem_ta": "ரீசர்ஜன்ஸ் இந்தியா எதிர் தேர்தல் ஆணையம் (2013) வழக்கில், ஒரு வேட்பாளர் படிவம் 26 பிரமாணப் பத்திரத்தில் கட்டங்களை காலியாக விட்டுவிட்டால் தேர்தல் நடத்தும் அதிகாரி என்ன செய்ய வேண்டும் என உச்ச நீதிமன்றம் உத்தரவிட்டது?",
        "options": [
            ("Accept the nomination and ignore the blank columns", "வேட்புமனுவை ஏற்றுக்கொண்டு காலி கட்டங்களை புறக்கணிக்க வேண்டும்"),
            ("Reject the nomination paper of the candidate after giving reminder", "நினைவூட்டல் வழங்கிய பிறகும் நிரப்பப்படாவிட்டால் வேட்புமனுவை நிராகரிக்க வேண்டும்"),
            ("Impose a financial penalty on the candidate", "வேட்பாளருக்கு அபராதம் விதிக்க வேண்டும்"),
            ("Allow the candidate to contest without party symbol", "கட்சி சின்னம் இல்லாமல் சுயேச்சையாக போட்டியிட அனுமதிக்க வேண்டும்")
        ],
        "correct_idx": 1, # Reject the nomination
        "exp_en": "In Resurgence India (2013), the Supreme Court held that leaving columns blank defeats the voter's right to know under Article 19(1)(a). If a candidate fails to fill all columns despite notice, the Returning Officer must reject the nomination paper.",
        "exp_ta": "ரீசர்ஜன்ஸ் இந்தியா வழக்கில், பிரமாணப் பத்திரத்தில் கட்டங்களை காலியாக விடுவது வாக்காளரின் அறியும் உரிமையை பாதிக்கிறது என்றும், எச்சரித்தும் நிரப்பாத வேட்புமனுவை தேர்தல் அதிகாரி நிராகரிக்க வேண்டும் என்றும் உத்தரவிடப்பட்டது.",
        "tip": "Candidates must write 'Nil' or 'Not Applicable'; blank spaces are not permitted.",
        "fact": "Nominations with blank columns are invalid under Section 36(2) of the RPA 1951.",
        "diff": "Hard",
        "subtopic": "Candidate Nominations"
    },

    # 36
    {
        "exam": "TNPSC Group 1 2019",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 1 2019",
        "stem_en": "Under the Electoral Trusts Scheme notified by the Central Government in 2013, what percentage of the total contributions received in a financial year must be distributed to registered political parties?",
        "stem_ta": "2013-ல் மத்திய அரசால் அறிவிக்கப்பட்ட தேர்தல் அறக்கட்டளை திட்டத்தின் கீழ், ஒரு நிதியாண்டில் பெறப்பட்ட மொத்த பங்களிப்பில் எத்தனை சதவீதம் பதிவு செய்யப்பட்ட கட்சிகளுக்கு விநியோகிக்கப்பட வேண்டும்?",
        "options": [
            ("At least 50%", "குறைந்தது 50%"),
            ("At least 95%", "குறைந்தது 95%"),
            ("At least 75%", "குறைந்தது 75%"),
            ("At least 80%", "குறைந்தது 80%")
        ],
        "correct_idx": 1, # At least 95%
        "exp_en": "Under the Electoral Trusts Scheme 2013 notified under Section 2(22AAA) of the Income Tax Act, an Electoral Trust must distribute at least 95% of total contributions received in that financial year to eligible registered political parties.",
        "exp_ta": "2013 தேர்தல் அறக்கட்டளை திட்டத்தின் கீழ், ஒரு தேர்தல் அறக்கட்டளை அந்த நிதியாண்டில் திரட்டிய மொத்த நன்கொடையில் குறைந்தபட்சம் 95 சதவீதத்தை பதிவு செய்யப்பட்ட அரசியல் கட்சிகளுக்கு வழங்க வேண்டும்.",
        "tip": "Electoral Trusts cannot accept cash donations or foreign contributions.",
        "fact": "Trusts submit audited annual contribution reports to both CBDT and the Election Commission of India.",
        "diff": "Hard",
        "subtopic": "Political Financing"
    },

    # 37
    {
        "exam": "TNPSC Group 1 2020",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 1 2020",
        "stem_en": "In the Union Budget 2017, the maximum limit for anonymous cash donation that a political party can receive from a single source was reduced from Rs 20,000 to how much?",
        "stem_ta": "2017 மத்திய பட்ஜெட்டில், ஒரு அரசியல் கட்சி ஒருவரிடமிருந்து ரொக்கமாகப் பெறக்கூடிய பெயரற்ற நன்கொடை உச்சவரம்பு ரூ.20,000-லிருந்து எவ்வளவு ரூபாயாக குறைக்கப்பட்டது?",
        "options": [
            ("Rs 5,000", "ரூ. 5,000"),
            ("Rs 2,000", "ரூ. 2,000"),
            ("Rs 1,000", "ரூ. 1,000"),
            ("Rs 500", "ரூ. 500")
        ],
        "correct_idx": 1, # Rs 2,000
        "exp_en": "The Finance Act 2017 amended Section 13A of the Income Tax Act, slashing the maximum cash donation acceptable by political parties from any individual from Rs 20,000 down to Rs 2,000.",
        "exp_ta": "2017 நிதிச் சட்டம் மூலம் வருமான வரிச் சட்டத்தின் பிரிவு 13A திருத்தப்பட்டு, அரசியல் கட்சிகள் பெறக்கூடிய ரொக்க நன்கொடை வரம்பு ரூ.20,000-லிருந்து ரூ.2,000 ஆக குறைக்கப்பட்டது.",
        "tip": "Any donation above Rs 2,000 must be made via cheque, digital transfer, or electoral instrument.",
        "fact": "This was introduced by Finance Minister Arun Jaitley to enhance transparency in political finance.",
        "diff": "Easy",
        "subtopic": "Political Financing"
    },

    # 38
    {
        "exam": "TNPSC Group 1 2024",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 1 2024",
        "stem_en": "In Association for Democratic Reforms v. Union of India (February 2024), a 5-judge Constitution Bench struck down the Electoral Bond Scheme because it violated which Fundamental Right?",
        "stem_ta": "ஏடிஆர் எதிர் இந்திய ஒன்றியம் (பிப்ரவரி 2024) வழக்கில், 5 நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வு தேர்தல் பத்திரத் திட்டத்தை எந்த அடிப்படை உரிமையை மீறியதற்காக ரத்து செய்தது?",
        "options": [
            ("Article 14 (Right to Equality)", "சரத்து 14 (சமத்துவ உரிமை)"),
            ("Article 19(1)(a) (Right to Information / Freedom of Expression)", "சரத்து 19(1)(a) (தகவல் அறியும் உரிமை / கருத்து சுதந்திரம்)"),
            ("Article 21 (Right to Privacy)", "சரத்து 21 (தனிநபர் அந்தரங்க உரிமை)"),
            ("Article 32 (Right to Constitutional Remedies)", "சரத்து 32 (அரசியலமைப்பு பரிகார உரிமை)")
        ],
        "correct_idx": 1, # Article 19(1)(a)
        "exp_en": "On 15 February 2024, a unanimous 5-judge bench headed by CJI D.Y. Chandrachud invalidated the Electoral Bonds Scheme, holding that anonymous political donations infringe upon the voter's fundamental right to information under Article 19(1)(a).",
        "exp_ta": "2024 பிப்ரவரி 15 அன்று, தலைமை நீதிபதி சந்திரசூட் தலைமையிலான 5 நீதிபதிகள் கொண்ட அமர்வு, பெயரற்ற தேர்தல் பத்திரங்கள் வாக்காளரின் தகவல் அறியும் உரிமையை (சரத்து 19(1)(a)) மீறுகிறது எனக் கூறி அத்திட்டத்தை ரத்து செய்தது.",
        "tip": "The Supreme Court also directed SBI to disclose all bond purchaser and redeemer details.",
        "fact": "The Court struck down amendments to Section 31(3) of the RBI Act, RPA 1951, and Companies Act 2013.",
        "diff": "Hard",
        "subtopic": "Political Financing"
    },

    # 39
    {
        "exam": "TNPSC Group 2 2022",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 2 2022",
        "stem_en": "Which flagship mobile app was developed by the Election Commission of India allowing citizens to report Model Code of Conduct violations with real-time geo-location tagging within 100 minutes?",
        "stem_ta": "தேர்தல் நடத்தை விதிமீறல்களை 100 நிமிடங்களுக்குள் ஜிபிஎஸ் இருப்பிடக் குறிப்புடன் பொதுமக்கள் நேரடியாகப் புகாரளிக்க இந்திய தேர்தல் ஆணையத்தால் உருவாக்கப்பட்ட முதன்மை செயலி எது?",
        "options": [
            ("Garuda App", "கருடா செயலி"),
            ("cVIGIL App", "சிவிஜில் (cVIGIL) செயலி"),
            ("Suvidha App", "சுவிதா செயலி"),
            ("Saksham App", "சாக்ஷம் செயலி")
        ],
        "correct_idx": 1, # cVIGIL
        "exp_en": "cVIGIL (Citizen Vigilance) was rolled out by the ECI, enabling any citizen to photograph or video-record an MCC violation; the app auto-captures GIS location and alerts the nearest Flying Squad to act within 100 minutes.",
        "exp_ta": "சிவிஜில் (cVIGIL) செயலி மூலம் பொதுமக்கள் தேர்தல் விதிமீறல்களை புகைப்படம் அல்லது வீடியோ எடுத்து புகாரளிக்கலாம்; இது 100 நிமிடங்களுக்குள் பறக்கும் படையால் நடவடிக்கை எடுக்கப்படுவதை உறுதி செய்கிறது.",
        "tip": "cVIGIL stands for Citizen Vigilance.",
        "fact": "Complainants can choose to lodge reports anonymously without revealing their identity.",
        "diff": "Easy",
        "subtopic": "Election Technology"
    },

    # 40
    {
        "exam": "TNPSC Group 1 2024",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 1 2024",
        "stem_en": "The Constitution (106th Amendment) Act, 2023, also known as the Nari Shakti Vandan Adhiniyam, provides what percentage of reservation for women in Lok Sabha and State Legislative Assemblies?",
        "stem_ta": "நாரி சக்தி வந்தன் அதினியம் என அழைக்கப்படும் 106-வது அரசியலமைப்பு திருத்தச் சட்டம் 2023, மக்களவை மற்றும் மாநில சட்டமன்றங்களில் பெண்களுக்கு எத்தனை சதவீத இடஒதுக்கீட்டை வழங்குகிறது?",
        "options": [
            ("25% reservation", "25% இடஒதுக்கீடு"),
            ("One-third (33%) of total seats", "மொத்த இடங்களில் மூன்றில் ஒரு பங்கு (33%)"),
            ("50% reservation", "50% இடஒதுக்கீடு"),
            ("30% reservation", "30% இடஒதுக்கீடு")
        ],
        "correct_idx": 1, # One-third (33%)
        "exp_en": "The 106th Constitutional Amendment Act 2023 inserted Articles 330A and 332A, providing 33% reservation for women in the Lok Sabha and State Legislative Assemblies for an initial period of 15 years.",
        "exp_ta": "106-வது அரசியலமைப்பு திருத்தச் சட்டம் 2023 சரத்துகள் 330A மற்றும் 332A-ஐ சேர்த்து, மக்களவை மற்றும் மாநில சட்டமன்றங்களில் பெண்களுக்கு 33% இடஒதுக்கீட்டை 15 ஆண்டு காலத்திற்கு வழங்குகிறது.",
        "tip": "Inserted Article 330A (Lok Sabha) and Article 332A (State Assemblies).",
        "fact": "The Act also inserted Article 239AA(2)(b) reserving 33% seats for women in the Delhi Legislative Assembly.",
        "diff": "Easy",
        "subtopic": "Women's Representation"
    },

    # 41
    {
        "exam": "TNPSC Group 1 2018",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 1 2018",
        "stem_en": "Which Joint Parliamentary Committee examined the Constitution (81st Amendment) Bill, 1996 for Women's Reservation and recommended extending 33% quota to OBC women as well?",
        "stem_ta": "மகளிர் இடஒதுக்கீட்டுக்கான 81-வது அரசியலமைப்பு திருத்த மசோதாவை (1996) ஆய்வு செய்து, 33% ஒதுக்கீட்டை ஓபிசி பெண்களுக்கும் நீட்டிக்க பரிந்துரைத்த நாடாளுமன்ற கூட்டுக்குழு எது?",
        "options": [
            ("Margret Alva Committee", "மார்கரெட் ஆல்வா குழு"),
            ("Geeta Mukherjee Committee", "கீதா முகர்ஜி குழு"),
            ("Sushma Swaraj Committee", "சுஷ்மா சுவராஜ் குழு"),
            ("Najma Heptulla Committee", "நஜ்மா ஹெப்துல்லா குழு")
        ],
        "correct_idx": 1, # Geeta Mukherjee Committee
        "exp_en": "The 31-member Joint Parliamentary Committee chaired by CPI MP Geeta Mukherjee examined the 1996 Women's Reservation Bill and presented its historic report recommending reservation for women in Parliament and Assemblies.",
        "exp_ta": "சிபிஐ நாடாளுமன்ற உறுப்பினர் கீதா முகர்ஜி தலைமையிலான 31 உறுப்பினர்களைக் கொண்ட கூட்டுக்குழு, 1996 மகளிர் இடஒதுக்கீடு மசோதாவை ஆய்வு செய்து தனது வரலாற்று சிறப்புமிக்க அறிக்கையை சமர்ப்பித்தது.",
        "tip": "Geeta Mukherjee was a veteran Communist parliamentarian and women's rights crusader.",
        "fact": "The committee also recommended that reservation should initially be for 15 years.",
        "diff": "Hard",
        "subtopic": "Women's Representation"
    },

    # 42
    {
        "exam": "TNPSC Group 1 2016",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 1 2016",
        "stem_en": "The 170th Report of the Law Commission of India (1999) headed by Justice B.P. Jeevan Reddy was entitled which of the following?",
        "stem_ta": "நீதிபதி பி.பி. ஜீவன் ரெட்டி தலைமையிலான இந்திய சட்ட ஆணையத்தின் 170-வது அறிக்கை (1999) எவ்வாறு அழைக்கப்பட்டது?",
        "options": [
            ("Review of the Constitution", "அரசியலமைப்பு மறுஆய்வு"),
            ("Reform of the Electoral Laws", "தேர்தல் சட்டங்களின் சீர்திருத்தம்"),
            ("Electoral Disqualifications", "தேர்தல் தகுதிநீக்கங்கள்"),
            ("Ethics in Governance", "ஆளுகையில் நெறிமுறைகள்")
        ],
        "correct_idx": 1, # Reform of the Electoral Laws
        "exp_en": "The Law Commission of India submitted its landmark 170th Report titled 'Reform of the Electoral Laws' in May 1999, recommending list-system proportional representation, simultaneous elections, and internal party democracy.",
        "exp_ta": "சட்ட ஆணையம் 1999 மே மாதம் 'தேர்தல் சட்டங்களின் சீர்திருத்தம்' என்ற தலைப்பில் தனது 170-வது அறிக்கையை சமர்ப்பித்து, பட்டியல் முறை பிரதிநிதித்துவம் மற்றும் ஒரே நேர தேர்தலை பரிந்துரைத்தது.",
        "tip": "170th Report (1999) is widely considered one of the most comprehensive official blueprints on election law.",
        "fact": "It recommended introducing an additional 25% seats to be filled through proportional representation.",
        "diff": "Medium",
        "subtopic": "Law Commission Reports"
    },

    # 43
    {
        "exam": "TNPSC Group 2 2017",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 2 2017",
        "stem_en": "Which report of the Law Commission of India submitted in 2014 exclusively addressed 'Electoral Disqualifications' and proposed disqualification upon framing of charges for heinous crimes?",
        "stem_ta": "2014-ல் சமர்ப்பிக்கப்பட்ட இந்திய சட்ட ஆணையத்தின் எந்த அறிக்கை பிரத்யேகமாக 'தேர்தல் தகுதிநீக்கங்கள்' குறித்து ஆராய்ந்து, கொடூர குற்றங்களுக்கு குற்றப்பத்திரிகை தாக்கல் செய்யப்பட்டாலே தகுதிநீக்கம் செய்ய பரிந்துரைத்தது?",
        "options": [
            ("230th Report", "230-வது அறிக்கை"),
            ("244th Report", "244-வது அறிக்கை"),
            ("255th Report", "255-வது அறிக்கை"),
            ("262nd Report", "262-வது அறிக்கை")
        ],
        "correct_idx": 1, # 244th Report
        "exp_en": "In February 2014, the 20th Law Commission chaired by Justice A.P. Shah submitted Report No. 244 on 'Electoral Disqualifications', recommending disqualification at the stage of framing of charges by a competent court for offences punishable with 5+ years imprisonment.",
        "exp_ta": "2014 பிப்ரவரியில் நீதிபதி ஏ.பி. ஷா தலைமையிலான 244-வது சட்ட ஆணைய அறிக்கை, 5 ஆண்டுகளுக்கு மேல் சிறை தண்டனைக்குரிய குற்றங்களுக்கு நீதிமன்றத்தில் குற்றப்பத்திரிகை தாக்கல் செய்யப்பட்டாலே தகுதிநீக்கம் செய்ய பரிந்துரைத்தது.",
        "tip": "Report 244 = Electoral Disqualifications (2014).",
        "fact": "The Supreme Court requested the Law Commission to examine this issue in Public Interest Foundation case.",
        "diff": "Hard",
        "subtopic": "Law Commission Reports"
    },

    # 44
    {
        "exam": "TNPSC Group 1 2020",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 1 2020",
        "stem_en": "The 255th Report of the Law Commission of India (March 2015) dealt with comprehensive reforms including which of the following areas?",
        "stem_ta": "இந்திய சட்ட ஆணையத்தின் 255-வது அறிக்கை (மார்ச் 2015) கீழ்க்கண்ட எந்த பகுதிகள் உள்ளிட்ட விரிவான தேர்தல் சீர்திருத்தங்களை கையாண்டது?",
        "options": [
            ("Judicial appointments only", "நீதிமன்ற நியமனங்கள் மட்டுமே"),
            ("Paid news, government sponsored advertisements, and regulation of political finance", "கட்டணச் செய்தி, அரசு விளம்பரங்கள் மற்றும் அரசியல் நிதி ஒழுங்குமுறை"),
            ("Goods and Services Tax framework", "சரக்கு மற்றும் சேவை வரி கட்டமைப்பு"),
            ("National security doctrines", "தேசிய பாதுகாப்பு கோட்பாடுகள்")
        ],
        "correct_idx": 1, # Paid news, advertising & finance
        "exp_en": "The 255th Law Commission Report (2015) titled 'Electoral Reforms' recommended statutory curbs on paid news, banning government advertisements 6 months prior to polls, capping party expenditure, and regulating opinion polls.",
        "exp_ta": "சட்ட ஆணையத்தின் 255-வது அறிக்கை (2015) தேர்தல் சீர்திருத்தங்கள் குறித்து விரிவாக ஆராய்ந்து, கட்டணச் செய்திகளுக்கு தடை, தேர்தலுக்கு 6 மாதங்களுக்கு முன் அரசு விளம்பரங்களுக்கு தடை மற்றும் அரசியல் நிதி வரம்புகளை பரிந்துரைத்தது.",
        "tip": "Report 255 focused heavily on curbing the misuse of money and media power in elections.",
        "fact": "It also recommended making paid news an electoral offence under the Representation of the People Act 1951.",
        "diff": "Medium",
        "subtopic": "Law Commission Reports"
    },

    # 45
    {
        "exam": "TNPSC Group 1 2015",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 1 2015",
        "stem_en": "The Second Administrative Reforms Commission (ARC) in its 4th Report titled 'Ethics in Governance' (2007) recommended that election petitions should be adjudicated by whom?",
        "stem_ta": "இரண்டாவது நிர்வாக சீர்திருத்த ஆணையம் (ARC) தனது 4-வது அறிக்கையான 'ஆளுகையில் நெறிமுறைகள்' (2007)-ல் தேர்தல் மனுக்கள் யாரால் விசாரிக்கப்பட வேண்டும் என பரிந்துரைத்தது?",
        "options": [
            ("Supreme Court directly", "உச்ச நீதிமன்றத்தால் நேரடியாக"),
            ("Special Election Benches of High Courts or dedicated National Election Tribunals", "உயர்நீதிமன்றங்களின் சிறப்பு தேர்தல் அமர்வுகள் அல்லது பிரத்யேக தேர்தல் தீர்ப்பாயங்கள்"),
            ("District Magistrates exclusively", "மாவட்ட ஆட்சித் தலைவர்களால் மட்டுமே"),
            ("Parliamentary Privileges Committee", "நாடாளுமன்ற சிறப்புரிமைக் குழு")
        ],
        "correct_idx": 1, # Special Election Benches / Tribunals
        "exp_en": "The Second ARC recommended establishing dedicated National Election Tribunals or Special Election Benches in High Courts to expedite election petitions within 6 months, avoiding prolonged delays.",
        "exp_ta": "தேர்தல் மனுக்களை 6 மாதங்களுக்குள் விரைந்து முடிப்பதற்காக, உயர்நீதிமன்றங்களில் சிறப்பு தேர்தல் அமர்வுகள் அல்லது பிரத்யேக தேசிய தேர்தல் தீர்ப்பாயங்களை அமைக்க இரண்டாவது ARC பரிந்துரைத்தது.",
        "tip": "Second ARC 4th report = Ethics in Governance (headed by Veerappa Moily).",
        "fact": "Section 86(7) of RPA 1951 already provides that election petitions should be concluded within 6 months, but in practice they take years.",
        "diff": "Hard",
        "subtopic": "Administrative Reforms"
    },

    # 46
    {
        "exam": "TNPSC Group 1 2017",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 1 2017",
        "stem_en": "The National Commission to Review the Working of the Constitution (NCRWC, 2002) was headed by which former Chief Justice of India?",
        "stem_ta": "அரசியலமைப்பின் செயல்பாட்டை மறுஆய்வு செய்வதற்கான தேசிய ஆணையம் (NCRWC, 2002) இந்தியாவின் எந்த முன்னாள் தலைமை நீதிபதி தலைமையில் அமைக்கப்பட்டது?",
        "options": [
            ("Justice P.N. Bhagwati", "நீதிபதி பி.என். பகவதி"),
            ("Justice M.N. Venkatachaliah", "நீதிபதி எம்.என். வெங்கடாசலையா"),
            ("Justice J.S. Verma", "நீதிபதி ஜே.எஸ். வர்மா"),
            ("Justice Kuldip Singh", "நீதிபதி குல்தீப் சிங்")
        ],
        "correct_idx": 1, # Justice M.N. Venkatachaliah
        "exp_en": "The NCRWC was set up in February 2000 by the Atal Bihari Vajpayee government and was chaired by former Chief Justice of India Justice M.N. Venkatachaliah; it submitted its final report in March 2002.",
        "exp_ta": "வாஜ்பாய் அரசால் 2000 பிப்ரவரியில் அமைக்கப்பட்ட அரசியலமைப்பு மறுஆய்வு தேசிய ஆணையம் (NCRWC), முன்னாள் தலைமை நீதிபதி எம்.என். வெங்கடாசலையா தலைமையில் செயல்பட்டு 2002 மார்ச்சில் அறிக்கை சமர்ப்பித்தது.",
        "tip": "Commonly known as the Venkatachaliah Commission.",
        "fact": "The commission recommended a constructive vote of no-confidence to ensure political stability.",
        "diff": "Easy",
        "subtopic": "Committees and Commissions"
    },

    # 47
    {
        "exam": "TNPSC Group 1 2023",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 1 2023",
        "stem_en": "In Anoop Baranwal v. Union of India (March 2023), the Supreme Court ruled that appointments to the Election Commission should be made by the President on the advice of a committee comprising whom?",
        "stem_ta": "அனூப் பரன்வால் எதிர் இந்திய ஒன்றியம் (மார்ச் 2023) வழக்கில், தேர்தல் ஆணையர்களை நியமிக்க குடியரசுத் தலைவருக்கு பரிந்துரைக்கும் குழுவில் யார் யார் இடம்பெற வேண்டும் என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது?",
        "options": [
            ("Prime Minister, Home Minister, and Law Minister", "பிரதமர், உள்துறை அமைச்சர் மற்றும் சட்ட அமைச்சர்"),
            ("Prime Minister, Leader of Opposition in Lok Sabha, and Chief Justice of India", "பிரதமர், மக்களவை எதிர்க்கட்சித் தலைவர் மற்றும் உச்ச நீதிமன்ற தலைமை நீதிபதி"),
            ("President, Vice President, and Prime Minister", "குடியரசுத் தலைவர், துணை குடியரசுத் தலைவர் மற்றும் பிரதமர்"),
            ("Chief Justice of India and two senior-most Supreme Court Judges", "உச்ச நீதிமன்ற தலைமை நீதிபதி மற்றும் இரண்டு மூத்த நீதிபதிகள்")
        ],
        "correct_idx": 1, # PM, LoP, CJI
        "exp_en": "On 2 March 2023, a unanimous 5-judge Constitution Bench held that to ensure institutional independence under Article 324(2), the CEC and ECs must be appointed on the recommendation of a Committee consisting of the Prime Minister, Leader of Opposition in Lok Sabha, and the Chief Justice of India.",
        "exp_ta": "2023 மார்ச் 2 அன்று, தேர்தல் ஆணையத்தின் சுதந்திரத்தைப் பாதுகாக்க சரத்து 324(2)-ன் கீழ் நாடாளுமன்றம் சட்டம் இயற்றும் வரை பிரதமர், மக்களவை எதிர்க்கட்சித் தலைவர் மற்றும் உச்ச நீதிமன்ற தலைமை நீதிபதி அடங்கிய குழு பரிந்துரைக்க வேண்டும் என தீர்ப்பளிக்கப்பட்டது.",
        "tip": "The judgment was delivered by a bench led by Justice K.M. Joseph.",
        "fact": "The Court invoked Article 324(2) noting that Parliament had failed to enact a selection law for over 70 years.",
        "diff": "Hard",
        "subtopic": "Election Commission Appointments"
    },

    # 48
    {
        "exam": "TNPSC Group 1 2024",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 1 2024",
        "stem_en": "Under the Chief Election Commissioner and other Election Commissioners (Appointment, Conditions of Service and Term of Office) Act, 2023, who replaced the Chief Justice of India in the Selection Committee?",
        "stem_ta": "2023 தலைமை தேர்தல் ஆணையர் மற்றும் பிற தேர்தல் ஆணையர்கள் சட்டத்தின் கீழ், தேர்வு குழுவில் உச்ச நீதிமன்ற தலைமை நீதிபதிக்கு பதிலாக யார் சேர்க்கப்பட்டார்?",
        "options": [
            ("Lok Sabha Speaker", "மக்களவை சபாநாயகர்"),
            ("A Union Cabinet Minister nominated by the Prime Minister", "பிரதமரால் பரிந்துரைக்கப்படும் ஒரு மத்திய கேபினட் அமைச்சர்"),
            ("Attorney General of India", "இந்திய தலைமை வழக்கறிஞர் (அட்டர்னி ஜெனரல்)"),
            ("Chairman of Rajya Sabha", "மாநிலங்களவைத் தலைவர்")
        ],
        "correct_idx": 1, # Union Cabinet Minister nominated by PM
        "exp_en": "Section 7(1) of the Chief Election Commissioner and other Election Commissioners Act 2023 provides that the Selection Committee consists of the Prime Minister (Chairperson), Leader of the Opposition in Lok Sabha, and a Union Cabinet Minister to be nominated by the Prime Minister.",
        "exp_ta": "2023 சட்டத்தின் பிரிவு 7(1)-ன் கீழ், தலைமை நீதிபதிக்கு பதிலாக பிரதமரால் பரிந்துரைக்கப்படும் ஒரு மத்திய கேபினட் அமைச்சர் தேர்வு குழுவில் சேர்க்கப்பட்டுள்ளார்.",
        "tip": "The Selection Committee has a 2:1 executive majority (PM + Union Minister vs LoP).",
        "fact": "The Act also established a Search Committee headed by the Minister of Law and Justice.",
        "diff": "Medium",
        "subtopic": "Election Commission Appointments"
    },

    # 49
    {
        "exam": "TNPSC Group 1 2018",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 1 2018",
        "stem_en": "In which landmark decision did Justice V.R. Krishna Iyer declare that Article 324 operates as a 'reservoir of plenary powers' when statutes are silent?",
        "stem_ta": "சட்டங்கள் மௌனமாக இருக்கும் சூழலில் சரத்து 324 என்பது 'முழுமையான அதிகாரங்களின் தேக்கம்' என்று நீதிபதி வி.ஆர். கிருஷ்ண ஐயர் எந்த முக்கிய வழக்கில் பிரகடனப்படுத்தினார்?",
        "options": [
            ("Saka Venkata Rao case (1953)", "சாகா வெங்கட ராவ் வழக்கு (1953)"),
            ("Mohinder Singh Gill v. Chief Election Commissioner (1978)", "மொகிந்தர் சிங் கில் எதிர் தலைமை தேர்தல் ஆணையர் (1978)"),
            ("S.S. Dhanoa v. Union of India (1991)", "எஸ்.எஸ். தனோவா எதிர் இந்திய ஒன்றியம் (1991)"),
            ("T.N. Seshan v. Union of India (1995)", "டி.என். சேஷன் எதிர் இந்திய ஒன்றியம் (1995)")
        ],
        "correct_idx": 1, # Mohinder Singh Gill
        "exp_en": "In Mohinder Singh Gill v. CEC (1978), the Supreme Court ruled that Article 324 is a constitutional reservoir of inherent executive power enabling the ECI to pass necessary orders to ensure free and fair elections where enacted laws are silent.",
        "exp_ta": "மொகிந்தர் சிங் கில் எதிர் தலைமை தேர்தல் ஆணையர் (1978) வழக்கில், சட்டம் இல்லாத இடங்களில் சுதந்திரமான தேர்தலை உறுதி செய்ய சரத்து 324 தேர்தல் ஆணையத்திற்கு முழுமையான அதிகாரங்களை வழங்குகிறது என நீதிபதி கிருஷ்ண ஐயர் தீர்ப்பளித்தார்.",
        "tip": "Article 324 supplements, but cannot supplant enacted law.",
        "fact": "The Court also held that natural justice must be complied with to the extent possible during election administration.",
        "diff": "Hard",
        "subtopic": "Constitutional Powers of ECI"
    },

    # 50
    {
        "exam": "TNPSC Group 1 2019",
        "exam_ta": "டிஎன்பிஎஸ்சி குரூப் 1 2019",
        "stem_en": "In Kuldip Nayar v. Union of India (2006), a 5-judge Constitution Bench upheld the constitutionality of which electoral reform introduced in 2003?",
        "stem_ta": "குல்தீப் நய்யார் எதிர் இந்திய ஒன்றியம் (2006) வழக்கில், 5 நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வு 2003-ல் அறிமுகப்படுத்தப்பட்ட எந்த தேர்தல் சீர்திருத்தத்தின் சட்டப்பூர்வ செல்லுபடியை உறுதி செய்தது?",
        "options": [
            ("Use of EVMs in all parliamentary elections", "அனைத்து நாடாளுமன்ற தேர்தல்களிலும் EVM பயன்பாடு"),
            ("Removal of domicile requirement and introduction of Open Ballot for Rajya Sabha", "இருப்பிடத் தகுதி நீக்கம் மற்றும் மாநிலங்களவைக்கான திறந்த வாக்குச்சீட்டு முறை அறிமுகம்"),
            ("Introduction of NOTA on ballot papers", "வாக்குச்சீட்டில் நோட்டா (NOTA) அறிமுகம்"),
            ("Direct elections to Rajya Sabha by universal adult franchise", "வயதுவந்தோர் வாக்குரிமை மூலம் மாநிலங்களவைக்கு நேரடி தேர்தல்")
        ],
        "correct_idx": 1, # Open Ballot and domicile removal for RS
        "exp_en": "In Kuldip Nayar v. Union of India (August 2006), the Supreme Court unanimously upheld the 2003 amendment to RPA 1951 removing the requirement of domicile in the state and substituting secret voting with open ballot in Rajya Sabha elections to prevent cross-voting and bribery.",
        "exp_ta": "குல்தீப் நய்யார் வழக்கில் (2006), மாநிலங்களவைத் தேர்தலில் குதிரை பேரம் மற்றும் கட்சி தாவலைத் தடுக்க இருப்பிடத் தகுதியை நீக்கியதையும், திறந்த வாக்குச்சீட்டு முறையை அறிமுகப்படுத்தியதையும் உச்ச நீதிமன்றம் உறுதி செய்தது.",
        "tip": "Open ballot applies only to Rajya Sabha indirect elections, not direct elections.",
        "fact": "MLAs must show their marked ballot paper to the authorized party agent before casting it.",
        "diff": "Hard",
        "subtopic": "Rajya Sabha Electoral Reforms"
    }
]

def build_pyq_questions():
    questions = []
    
    for i, item in enumerate(raw_pyq_data):
        qid = f"ER_PYQ_{i+1:03d}"
        stem_en = f"[{item['exam']}] {item['stem_en']}"
        stem_ta = f"[{item['exam_ta']}] {item['stem_ta']}"
        
        opts = item["options"]
        correct_idx = item["correct_idx"]
        correct_key = ["A", "B", "C", "D"][correct_idx]
        
        why_en = {}
        why_ta = {}
        for idx, key in enumerate(["A", "B", "C", "D"]):
            if idx == correct_idx:
                why_en[key] = f"Option {key} is the correct answer according to official {item['exam']} answer key."
                why_ta[key] = f"அதிகாரப்பூர்வ {item['exam_ta']} விடைக்குறிப்பின்படி தெரிவு {key} சரியான விடையாகும்."
            else:
                why_en[key] = f"Option {key} ({opts[idx][0]}) is incorrect for this question."
                why_ta[key] = f"இக்கேள்விக்கு தெரிவு {key} ({opts[idx][1]}) தவறானது."
                
        tip_en = item["tip"]
        tip_ta = f"நினைவில் கொள்க: {item['tip']}"
        fact_en = item["fact"]
        fact_ta = f"முக்கிய தகவல்: {item['fact']}"
        
        q = make_er_q(
            qid=qid,
            diff=item["diff"],
            qtype="PYQ",
            subtopic=item["subtopic"],
            en_stem=stem_en,
            ta_stem=stem_ta,
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
            tip_en=tip_en,
            tip_ta=tip_ta,
            fact_en=fact_en,
            fact_ta=fact_ta,
            tags=["polity", "electoral_reforms", "pyq", item["exam"]]
        )
        questions.append(q)
        
    return questions

def main():
    questions = build_pyq_questions()
    print(f"Total raw PYQ questions: {len(questions)}")
    
    # Rebalance keys to ~13 B, 12 C, 12 D, 13 A
    balanced = balance_question_keys(questions, {"A": 13, "B": 13, "C": 12, "D": 12})
    
    out_dir = "data/questions/polity"
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "electoral_reforms_pyq.json")
    alias_file = os.path.join(out_dir, "electoral_reforms_pyq_practice.json")
    
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(balanced, f, indent=2, ensure_ascii=False)
    with open(alias_file, "w", encoding="utf-8") as f:
        json.dump(balanced, f, indent=2, ensure_ascii=False)
        
    print(f"Saved to {out_file} and alias {alias_file}")
    
    validator = ContentValidator()
    report = validator.validate_file(out_file, expected_count=50, expected_prefix="ER_PYQ_")
    print(f"Validation Report: {'PASS' if report.is_valid else 'FAIL'} | Total: {report.total_audited}")
    print(f"Key Distribution: {report.key_distribution}")
    if not report.is_valid:
        for iss in report.issues:
            print("Issue:", iss.message)

if __name__ == "__main__":
    main()
