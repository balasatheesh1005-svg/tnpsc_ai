# -*- coding: utf-8 -*-
"""
Generator for Attorney General of India Hard MCQs (50 Questions: AG_H_001 to AG_H_050).
Strictly adheres to:
- Full 24-field TNPSC Nova AI schema
- Balanced answer keys (13 B, 12 C, 12 D, 13 A)
- Fully bilingual (English and authentic Tamil)
- Advanced constitutional jurisprudence, case laws, procedural rules
"""
import json
import os
from ag_mcq_helper import make_ag_q
from rebalance_er_helper import balance_question_keys
from tools.nova_content_engine.validator import ContentValidator

raw_hard_data = [
    # 1
    {
        "stem_en": "Under the Right to Information (RTI) Act 2005, what did the Delhi High Court rule in Subhash Chandra Agarwal v. Office of Attorney General of India (2015) regarding the constitutional status of the Attorney General?",
        "stem_ta": "தகவல் அறியும் உரிமைச் சட்டம் 2005-ன் கீழ், சுபாஷ் சந்திர அகர்வால் எதிர் இந்திய தலைமை வழக்கறிஞர் அலுவலகம் (2015) வழக்கில் தில்லி உயர்நீதிமன்றம் என்ன தீர்ப்பளித்தது?",
        "options": [
            ("The AG is not a public authority because he is an advocate in private practice", "AG ஒரு பொது அதிகாரி அல்ல, ஏனெனில் அவர் தனியார் தொழில் செய்யும் வழக்கறிஞர்"),
            ("The office of the Attorney General is a 'Public Authority' under Section 2(h) of the RTI Act as it is an office established by the Constitution under Article 76", "சரத்து 76-ன் கீழ் அரசியலமைப்பால் நிறுவப்பட்ட அலுவலகம் என்பதால், தகவல் அறியும் உரிமைச் சட்டத்தின் பிரிவு 2(h)-ன் கீழ் தலைமை வழக்கறிஞர் அலுவலகம் ஒரு 'பொது அதிகாரி' (Public Authority) ஆகும்"),
            ("Only the Solicitor General is a public authority", "சொலிசிட்டர் ஜெனரல் மட்டுமே பொது அதிகாரி"),
            ("The AG is exempt from RTI under Section 8(1)(a) unconditionally", "பிரிவு 8(1)(a)-ன் கீழ் AG-க்கு RTI-லிருந்து நிபந்தனையற்ற விலக்கு உண்டு")
        ],
        "correct_idx": 1,
        "exp_en": "In 2015, a division bench of the Delhi High Court held that since the Attorney General of India performs constitutional functions and is appointed under Article 76, his office constitutes a 'Public Authority' within the meaning of Section 2(h) of the RTI Act 2005.",
        "exp_ta": "2015-ல் தில்லி உயர்நீதிமன்ற அமர்வு, சரத்து 76-ன் கீழ் அரசியலமைப்பு பணிகளை ஆற்றுவதால் தலைமை வழக்கறிஞர் அலுவலகம் தகவல் அறியும் உரிமைச் சட்டத்தின் பிரிவு 2(h)-ன் கீழ் ஒரு 'பொது அதிகாரி' (Public Authority) என தீர்ப்பளித்தது.",
        "tip": "As a public authority, the AG must appoint a Central Public Information Officer (CPIO) to process RTI applications.",
        "fact": "However, privileged professional legal advice given to the government can be exempted under Section 8(1)(e)."
    },
    # 2
    {
        "stem_en": "In P.N. Duda v. P. Shiv Shanker (1988), what did the Supreme Court hold regarding the refusal of the Attorney General to grant consent for criminal contempt under Section 15 of the Contempt of Courts Act 1971?",
        "stem_ta": "பி.என். தூதா எதிர் பி. சிவ சங்கர் (1988) வழக்கில், 1971 நீதிமன்ற அவமதிப்புச் சட்டத்தின் பிரிவு 15-ன் கீழ் குற்றவியல் அவமதிப்புக்கு ஒப்புதல் அளிக்க தலைமை வழக்கறிஞர் மறுப்பது குறித்து உச்ச நீதிமன்றம் என்ன தீர்ப்பளித்தது?",
        "options": [
            ("The AG's refusal can be overturned by Parliament", "AG-யின் மறுப்பை நாடாளுமன்றம் ரத்து செய்யலாம்"),
            ("The grant or refusal of consent by the Attorney General is a statutory discretion; while it cannot be challenged by appeal, the Supreme Court's inherent suo motu contempt power under Article 129 remains unaffected", "தலைமை வழக்கறிஞரின் ஒப்புதல் அல்லது மறுப்பு சட்டப்பூர்வ விருப்பத்திற்கு உட்பட்டது; அதை எதிர்த்து மேல்முறையீடு செய்ய முடியாது என்றாலும், சரத்து 129-ன் கீழான உச்ச நீதிமன்றத்தின் தானாக முன்வரும் அதிகாரம் பாதிக்கப்படாது"),
            ("The refusal of the AG automatically dissolves the contempt bench", "AG மறுத்துவிட்டால் அவமதிப்பு அமர்வு தானாக கலைந்துவிடும்"),
            ("The AG must pay compensation if he refuses consent", "ஒப்புதல் மறுத்தால் AG இழப்பீடு வழங்க வேண்டும்")
        ],
        "correct_idx": 1,
        "exp_en": "In P.N. Duda (1988), the Supreme Court ruled that the AG's refusal to grant consent under Section 15 is an administrative discretion not subject to ordinary appeal, but the Court's inherent power under Article 129 to initiate suo motu contempt is unfettered by the AG's decision.",
        "exp_ta": "1988-ல் பி.என். தூதா வழக்கில், பிரிவு 15-ன் கீழ் ஒப்புதல் அளிப்பது அல்லது மறுப்பது AG-யின் சட்டப்பூர்வ முடிவு என்றும், AG மறுத்தாலும் சரத்து 129-ன் கீழ் உச்ச நீதிமன்றம் தானாக முன்வந்து வழக்கை விசாரிக்க தடை இல்லை என்றும் தீர்ப்பளிக்கப்பட்டது.",
        "tip": "Article 129 makes the Supreme Court a court of record with inherent power to punish for contempt.",
        "fact": "The AG's consent acts as a procedural filter, not an absolute constitutional bar on the Supreme Court."
    },
    # 3
    {
        "stem_en": "Under Sections 91 and 92 of the Code of Civil Procedure 1908 (CPC), what special statutory power was historically vested in the Advocate General and Attorney General regarding public causes?",
        "stem_ta": "1908 சிவில் நடைமுறைச் சட்டத்தின் (CPC) பிரிவு 91 மற்றும் 92-ன் கீழ், பொது விவகாரங்கள் தொடர்பாக தலைமை வழக்கறிஞருக்கு வரலாற்று ரீதியாக வழங்கப்பட்ட சிறப்பு அதிகாரம் எது?",
        "options": [
            ("Power to dissolve private trusts", "தனியார் அறக்கட்டளைகளை கலைக்கும் அதிகாரம்"),
            ("Power to institute a suit or grant consent to two or more persons to file a suit in cases of public nuisance (Sec 91) or breach of public charitable/religious trusts (Sec 92)", "பொதுத் தொல்லைகள் (பிரிவு 91) அல்லது பொது தொண்டு/மத அறக்கட்டளை விதிமீறல்கள் (பிரிவு 92) விவகாரங்களில் வழக்கு தொடர அல்லது இரு நபர்கள் வழக்கு தொடர ஒப்புதல் அளிக்கும் அதிகாரம்"),
            ("Power to seize trust properties directly", "அறக்கட்டளை சொத்துக்களை நேரடியாக பறிமுதல் செய்யும் அதிகாரம்"),
            ("Power to appoint trustees without court order", "நீதிமன்ற உத்தரவின்றி அறங்காவலர்களை நியமிக்கும் அதிகாரம்")
        ],
        "correct_idx": 1,
        "exp_en": "Under Sections 91 and 92 of CPC, the Advocate General (or outside presidency towns, with leave of the court) can institute suits or grant sanction to two or more persons to file representative suits regarding public nuisances and public charitable or religious trusts.",
        "exp_ta": "சிபிசி பிரிவு 91 மற்றும் 92, பொதுத் தொல்லைகள் மற்றும் பொது அறக்கட்டளை முறைகேடுகளுக்கு எதிராக நீதிமன்றத்தில் வழக்கு தொடர அல்லது தனிநபர்கள் வழக்கு தொடர ஒப்புதல் (Sanction) அளிக்க தலைமை வழக்கறிஞருக்கு அதிகாரம் அளிக்கிறது.",
        "tip": "Derived from the ancient doctrine of 'Parens Patriae' (father of the people).",
        "fact": "By the 1976 CPC amendment, suits under Section 91/92 can also be filed with the direct leave of the court."
    },
    # 4
    {
        "stem_en": "Unlike the Comptroller and Auditor General (Article 148(4)) and the Chairman of UPSC (Article 319(a)), is the Attorney General of India barred from future government appointment after leaving office?",
        "stem_ta": "தலைமை கணக்கு தணிக்கையாளர் (சரத்து 148(4)) மற்றும் UPSC தலைவர் (சரத்து 319(a)) போலன்றி, பதவி விலகிய பிறகு எதிர்காலத்தில் அரசு பதவிகளை வகிக்க இந்திய தலைமை வழக்கறிஞருக்கு தடை உண்டா?",
        "options": [
            ("Yes, permanently barred from all government employment", "ஆம், அனைத்து அரசு வேலைகளிலிருந்தும் நிரந்தர தடை உண்டு"),
            ("No, there is no constitutional or statutory bar on the Attorney General accepting subsequent employment under the Union or State Government", "இல்லை, மத்திய அல்லது மாநில அரசுகளின் கீழ் எதிர்காலத்தில் பதவிகளை ஏற்க தலைமை வழக்கறிஞருக்கு எந்த அரசியலமைப்பு அல்லது சட்டப்பூர்வ தடையும் இல்லை"),
            ("Barred for a period of 5 years only", "5 ஆண்டுகளுக்கு மட்டுமே தடை உண்டு"),
            ("Barred only from judicial offices", "நீதித்துறை பதவிகளுக்கு மட்டுமே தடை உண்டு")
        ],
        "correct_idx": 1,
        "exp_en": "Articles 148(4) and 319 explicitly prohibit the CAG and UPSC members from further government employment to guarantee their independence. Article 76 contains NO such bar for the Attorney General, who can accept any public or judicial office.",
        "exp_ta": "CAG (சரத்து 148(4)) மற்றும் UPSC தலைவர் (சரத்து 319) ஆகியோர் ஓய்வுக்குப் பின் அரசு பதவிகளை வகிக்க அரசியலமைப்பு தடை விதித்துள்ளது; ஆனால் சரத்து 76 தலைமை வழக்கறிஞருக்கு அத்தகைய எந்த தடையையும் விதிக்கவில்லை.",
        "tip": "Former law officers can be appointed as Governors, Judges, or Cabinet Ministers.",
        "fact": "Former AG C.K. Daphtary was later nominated to the Rajya Sabha."
    },
    # 5
    {
        "stem_en": "In 1963, Attorney General C.K. Daphtary was summoned to the Lok Sabha to tender his legal opinion on which controversial legislative measure?",
        "stem_ta": "1963-ல் எந்த சர்ச்சைக்குரிய சட்ட நடவடிக்கை குறித்து தனது சட்டக் கருத்தைத் தெரிவிக்க தலைமை வழக்கறிஞர் சி.கே. தப்தாரி மக்களவைக்கு வரவழைக்கப்பட்டார்?",
        "options": [
            ("Armed Forces Special Powers Act", "ஆயுதப்படைகள் சிறப்பு அதிகாரச் சட்டம்"),
            ("Compulsory Deposit Scheme Bill, 1963", "கட்டாய வைப்புத் திட்டம் (Compulsory Deposit Scheme) மசோதா, 1963"),
            ("Bank Nationalization Bill", "வங்கி தேசியமயமாக்கல் மசோதா"),
            ("Official Languages Act", "அதிகாரப்பூர்வ மொழிகள் சட்டம்")
        ],
        "correct_idx": 1,
        "exp_en": "In April 1963, Attorney General C.K. Daphtary was requested under Article 88 to address the Lok Sabha on the constitutional validity of the Compulsory Deposit Scheme Bill 1963, which was challenged by the Opposition as unconstitutional.",
        "exp_ta": "1963 ஏப்ரலில், எதிர்க்கட்சிகளால் எதிர்க்கப்பட்ட கட்டாய வைப்புத் திட்டம் (Compulsory Deposit Scheme) மசோதாவின் அரசியலமைப்பு செல்லுபடியாகும் தன்மை குறித்து மக்களவையில் விளக்கமளிக்க சரத்து 88-ன் கீழ் சி.கே. தப்தாரி அழைக்கப்பட்டார்.",
        "tip": "Daphtary defended the legislative competence of Parliament to enact the scheme.",
        "fact": "This was one of the rare instances where an Attorney General formally addressed the Lok Sabha."
    },
    # 6
    {
        "stem_en": "Under Order IV of the Supreme Court Rules 2013, can the Attorney General of India appear before the Supreme Court without filing a formal Vakalatnama or memo of appearance?",
        "stem_ta": "உச்ச நீதிமன்ற விதிகள் 2013-ன் உத்தரவு IV-ன் கீழ், முறையான வக்காலத்து (Vakalatnama) தாக்கல் செய்யாமல் இந்திய தலைமை வழக்கறிஞர் உச்ச நீதிமன்றத்தில் ஆஜராக முடியுமா?",
        "options": [
            ("No, every advocate must file a vakalatnama", "இல்லை, அனைத்து வழக்கறிஞர்களும் வக்காலத்து தாக்கல் செய்ய வேண்டும்"),
            ("Yes, by virtue of his high constitutional office, the Attorney General represents the Union without needing a formal vakalatnama or power of attorney", "ஆம், தனது உயர் அரசியலமைப்பு பதவி காரணமாக, முறையான வக்காலத்து அல்லது பவர் ஆஃப் அட்டர்னி இன்றியே தலைமை வழக்கறிஞர் இந்திய அரசுக்காக ஆஜராக முடியும்"),
            ("Only during vacation benches", "விடுமுறைக்கால அமர்வுகளில் மட்டுமே"),
            ("Only in criminal appeals", "குற்றவியல் மேல்முறையீடுகளில் மட்டுமே")
        ],
        "correct_idx": 1,
        "exp_en": "Under Supreme Court practice and rules, the Attorney General and Solicitor General appear ex-officio on behalf of the Union of India upon instructions from the Central Agency Section without the necessity of filing a Vakalatnama.",
        "exp_ta": "உச்ச நீதிமன்ற நடைமுறை மற்றும் விதிகளின்படி, மத்திய முகமைப் பிரிவின் அறிவுறுத்தலின் பேரில் வக்காலத்து தாக்கல் செய்யாமலேயே பதவிவழி உரிமையுடன் தலைமை வழக்கறிஞர் இந்திய அரசுக்காக ஆஜராக முடியும்.",
        "tip": "An Advocate-on-Record (AoR) files the formal appearance memo, but the AG needs no personal power of attorney.",
        "fact": "This procedural privilege is shared with the Solicitor General of India."
    },
    # 7
    {
        "stem_en": "Under Rule 7 of the Law Officers (Conditions of Service) Rules 1987, what is the monthly retainership fee currently paid to the Attorney General of India?",
        "stem_ta": "1987 சட்ட அதிகாரிகள் விதிகளின் விதி 7-ன் கீழ், இந்திய தலைமை வழக்கறிஞருக்கு வழங்கப்படும் மாதாந்திர தக்கவைப்புக் கட்டணம் (Monthly Retainership) எவ்வளவு?",
        "options": [
            ("Rs 10,000 per month", "மாதம் ரூ. 10,000"),
            ("Rs 50,000 per month", "மாதம் ரூ. 50,000"),
            ("Rs 2,50,000 per month (equal to Supreme Court Judge)", "மாதம் ரூ. 2,50,000 (உச்ச நீதிமன்ற நீதிபதிக்கு சமமானது)"),
            ("Rs 5,00,000 per month", "மாதம் ரூ. 5,00,000")
        ],
        "correct_idx": 1,
        "exp_en": "Under Rule 7 of the Law Officers (Conditions of Service) Rules 1987 (as revised in 2018), the Attorney General receives a monthly retainership fee of Rs 50,000, supplemented by daily appearance fees for court hearings and outstation allowances.",
        "exp_ta": "1987 சட்ட அதிகாரிகள் விதிகளின் விதி 7-ன் கீழ் (2018-ல் திருத்தப்பட்டது), தலைமை வழக்கறிஞருக்கு மாதம் ரூ. 50,000 தக்கவைப்புக் கட்டணமும், அத்துடன் நீதிமன்றத்தில் ஆஜராவதற்கான தனித்தனி தினசரி கட்டணங்களும் வழங்கப்படுகின்றன.",
        "tip": "He does not draw a monthly salary of Rs 2.5 Lakh like a Supreme Court Judge.",
        "fact": "His income is predominantly generated through per-appearance brief fees."
    },
    # 8
    {
        "stem_en": "In the historic Bofors scandal debate in Parliament in 1987, which Attorney General was requested to explain the legal parameters of the Joint Parliamentary Committee (JPC) inquiry?",
        "stem_ta": "1987-ல் போஃபர்ஸ் விவகாரம் குறித்த நாடாளுமன்ற விவாதத்தில், நாடாளுமன்றக் கூட்டுக்குழு (JPC) விசாரணையின் சட்ட வரம்புகளை விளக்க அழைக்கப்பட்ட தலைமை வழக்கறிஞர் யார்?",
        "options": [
            ("M.C. Setalvad", "எம்.சி. செதல்வாட்"),
            ("K. Parasaran", "கே. பராசரன்"),
            ("Soli Sorabjee", "சோலி சோராப்ஜி"),
            ("Niren De", "நிரேன் டே")
        ],
        "correct_idx": 1,
        "exp_en": "During the intense Bofors debate in 1987, Attorney General K. Parasaran was summoned under Article 88 to address the Lok Sabha, advising Parliament on the scope, powers, and procedure of the proposed Joint Parliamentary Committee inquiry.",
        "exp_ta": "1987-ல் போஃபர்ஸ் ஊழல் விவாதத்தின் போது, நாடாளுமன்றக் கூட்டுக்குழுவின் (JPC) அதிகார வரம்புகள் மற்றும் நடைமுறைகள் குறித்து விளக்கம் அளிக்க சரத்து 88-ன் கீழ் தலைமை வழக்கறிஞர் கே. பராசரன் மக்களவையில் உரையாற்றினார்.",
        "tip": "K. Parasaran was renowned for quoting both legal precedents and the Bhagavad Gita / Ramayana in constitutional arguments.",
        "fact": "His scholarly address clarified the jurisdiction of parliamentary inquiry committees vis-à-vis criminal investigations."
    },
    # 9
    {
        "stem_en": "Which of the following is true regarding the Attorney General's power to advise the President on whether a Bill should be reserved for reconsideration under Article 111?",
        "stem_ta": "சரத்து 111-ன் கீழ் ஒரு மசோதாவை மறுபரிசீலனைக்கு அனுப்பலாமா என்பது குறித்து குடியரசுத் தலைவருக்கு ஆலோசனை வழங்கும் தலைமை வழக்கறிஞரின் அதிகாரம் பற்றி எது சரியானது?",
        "options": [
            ("The AG can unilaterally veto any Bill passed by Parliament", "நாடாளுமன்றம் நிறைவேற்றிய எந்த மசோதாவையும் AG தன்னிச்சையாக ரத்து செய்யலாம்"),
            ("The President can consult the Attorney General on the constitutionality of a Bill, but the advice given is confidential and advisory, and the President acts on the aid and advice of the Council of Ministers", "மசோதாவின் அரசியலமைப்பு ஏற்புடைமை குறித்து குடியரசுத் தலைவர் AG-யிடம் ஆலோசனை கேட்கலாம்; ஆனால் அந்த ஆலோசனை ரகசியமானது மற்றும் குடியரசுத் தலைவர் அமைச்சரவையின் ஆலோசனையின் பேரிலேயே முடிவெடுக்கிறார்"),
            ("The AG's signature is mandatory on all Acts of Parliament", "நாடாளுமன்றத்தின் அனைத்து சட்டங்களிலும் AG-யின் கையொப்பம் கட்டாயம்"),
            ("The AG has no power to read legislative bills", "சட்ட மசோதாக்களை வாசிக்கும் அதிகாரம் AG-க்கு இல்லை")
        ],
        "correct_idx": 1,
        "exp_en": "The President may seek the legal opinion of the Attorney General under Article 76(2) on the constitutional validity of a Bill passed by Parliament. However, the advice is advisory and the President ultimately functions under Article 74 on Cabinet advice.",
        "exp_ta": "மசோதாவின் அரசியலமைப்பு செல்லுபடியாகும் தன்மை குறித்து சரத்து 76(2)-ன் கீழ் குடியரசுத் தலைவர் AG-யிடம் ஆலோசனை கேட்கலாம்; ஆனால் அது ஆலோசனை மட்டுமே, குடியரசுத் தலைவர் சரத்து 74-ன் கீழ் அமைச்சரவை முடிவின்படியே செயல்படுகிறார்.",
        "tip": "Article 111 governs Presidential assent to Bills.",
        "fact": "President Giani Zail Singh consulted several jurists, including former law officers, during the Indian Post Office (Amendment) Bill controversy in 1986."
    },
    # 10
    {
        "stem_en": "In the landmark Triple Talaq case (Shayara Bano v. Union of India, 2017), who appeared as the Attorney General representing the Government of India in support of declaring Talaq-e-Biddat unconstitutional?",
        "stem_ta": "முத்தலாக் வழக்கில் (ஷயாரா பானோ எதிர் இந்திய ஒன்றியம், 2017), தலாக்-இ-பித்தத் அரசியலமைப்பிற்கு எதிரானது என வாதிட்டு மத்திய அரசுக்காக ஆஜரான தலைமை வழக்கறிஞர் யார்?",
        "options": [
            ("M.C. Setalvad", "எம்.சி. செதல்வாட்"),
            ("Mukul Rohatgi", "முகுல் ரோஹத்கி"),
            ("G.E. Vahanvati", "ஜி.இ. வாகனவதி"),
            ("Milon Banerjee", "மிலன் பானர்ஜி")
        ],
        "correct_idx": 1,
        "exp_en": "Attorney General Mukul Rohatgi led the Government of India's arguments in the Supreme Court in May 2017, arguing that Triple Talaq violates gender equality under Article 14 and dignity under Article 21, and does not form an essential religious practice under Article 25.",
        "exp_ta": "2017 மே மாதம், முத்தலாக் முறை சரத்து 14 பாலின சமத்துவம் மற்றும் சரத்து 21 கண்ணியத்தை மீறுகிறது என்று உச்ச நீதிமன்றத்தில் மத்திய அரசுக்காக தலைமை வழக்கறிஞர் முகுல் ரோஹத்கி வாதாடினார்.",
        "tip": "A 5-judge multi-faith Constitution Bench struck down Triple Talaq by a 3:2 majority in August 2017.",
        "fact": "Mukul Rohatgi demitted office shortly after concluding these arguments in June 2017."
    },
    # 11
    {
        "stem_en": "Can the Attorney General of India challenge the constitutional validity of a Central statute enacted by Parliament while holding office?",
        "stem_ta": "பதவியில் இருக்கும் போது, நாடாளுமன்றத்தால் இயற்றப்பட்ட ஒரு மத்திய சட்டத்தின் அரசியலமைப்பு செல்லுபடியாகும் தன்மையை எதிர்த்து தலைமை வழக்கறிஞர் நீதிமன்றத்தில் சவால் செய்ய முடியுமா?",
        "options": [
            ("Yes, if he personally believes it is unconstitutional", "ஆம், அது அரசியலமைப்பிற்கு எதிரானது என அவர் தனிப்பட்ட முறையில் கருதினால்"),
            ("No, the Attorney General is under an absolute constitutional duty to defend the validity of Parliamentary enactments on behalf of the Union of India", "இல்லை, இந்திய அரசாங்கத்தின் சார்பில் நாடாளுமன்ற சட்டங்களின் சட்டப்பூர்வ செல்லுபடியை நீதிமன்றத்தில் பாதுகாக்க வேண்டிய முழுமையான அரசியலமைப்பு கடமை தலைமை வழக்கறிஞருக்கு உண்டு"),
            ("Only in the High Court of Delhi", "தில்லி உயர்நீதிமன்றத்தில் மட்டுமே"),
            ("Only if joined by the Leader of the Opposition", "எதிர்க்கட்சித் தலைவர் அவருடன் இணைந்தால் மட்டுமே")
        ],
        "correct_idx": 1,
        "exp_en": "The Attorney General is the counsel for the Union of India. He is bound by his constitutional remit to defend the legal and constitutional validity of statutes enacted by Parliament before the courts, and cannot assail a parliamentary law.",
        "exp_ta": "தலைமை வழக்கறிஞர் இந்திய அரசின் வழக்கறிஞராவார். நாடாளுமன்றம் இயற்றிய சட்டங்களின் செல்லுபடியை நீதிமன்றங்களில் பாதுகாக்க வேண்டிய அரசியலமைப்பு கடமை அவருக்கு உண்டு; அவர் அச்சட்டங்களை எதிர்த்து வாதிட முடியாது.",
        "tip": "If the AG has fundamental moral or legal disagreements, his ethical recourse is to resign from office.",
        "fact": "This principle is consistent with the duty of an advocate to zealously represent the client's case."
    },
    # 12
    {
        "stem_en": "Under Article 76, if a question arises as to whether an advocate possesses the qualifications of an 'eminent jurist', whose opinion is constitutionally determinative?",
        "stem_ta": "சரத்து 76-ன் கீழ், ஒரு வழக்கறிஞர் 'சிறந்த சட்ட அறிஞர்' (Eminent Jurist) என்ற தகுதியைக் கொண்டுள்ளாரா என்ற கேள்வி எழுந்தால், யாருடைய கருத்து அரசியலமைப்பு ரீதியாக இறுதியானது?",
        "options": [
            ("Chief Justice of India", "இந்திய தலைமை நீதிபதி"),
            ("President of India", "இந்திய குடியரசுத் தலைவர்"),
            ("Bar Council of India", "இந்திய பார் கவுன்சில்"),
            ("Supreme Court Collegium", "உச்ச நீதிமன்ற கொலீஜியம்")
        ],
        "correct_idx": 1,
        "exp_en": "Article 124(3)(c) explicitly states: 'an eminent jurist in the opinion of the President'. Therefore, the satisfaction and subjective opinion of the President (acting on Cabinet advice) is the sole constitutional benchmark.",
        "exp_ta": "சரத்து 124(3)(c) 'குடியரசுத் தலைவரின் பார்வையில் சிறந்த சட்ட அறிஞர்' என்று தெளிவாக கூறுகிறது. எனவே குடியரசுத் தலைவரின் (அமைச்சரவை ஆலோசனை) திருப்தியும் கருத்தும் மட்டுமே அரசியலமைப்பு ரீதியாக இறுதியானது.",
        "tip": "Neither the Supreme Court nor the Bar Council can substitute its opinion for the President's opinion.",
        "fact": "This category was introduced by the framers inspired by the US Supreme Court appointments practice."
    },
    # 13
    {
        "stem_en": "Under Rule 8(1)(d) of the Law Officers (Conditions of Service) Rules 1987, what restriction is placed on the Attorney General regarding public commentary in the media?",
        "stem_ta": "1987 சட்ட அதிகாரிகள் விதிகளின் விதி 8(1)(d)-ன் கீழ், ஊடகங்களில் பொதுக் கருத்துக்களை தெரிவிப்பது தொடர்பாக தலைமை வழக்கறிஞருக்கு விதிக்கப்பட்டுள்ள கட்டுப்பாடு என்ன?",
        "options": [
            ("He cannot write legal textbooks", "அவர் சட்டப் புத்தகங்களை எழுத முடியாது"),
            ("He shall not communicate with the press or media on any matter which is sub-judice or subject matter of an advice tendered to the Government", "நீதிமன்ற விசாரணையில் உள்ள வழக்குகள் அல்லது அரசுக்கு வழங்கிய ஆலோசனைகள் குறித்து பத்திரிகைகள் அல்லது ஊடகங்களுடன் தொடர்பு கொள்ளக்கூடாது"),
            ("He cannot appear on televised legal education programs", "தொலைக்காட்சி சட்டக் கல்வி நிகழ்ச்சிகளில் தோன்ற முடியாது"),
            ("He must submit daily social media logs to the Home Ministry", "தினசரி சமூக ஊடக பதிவுகளை உள்துறை அமைச்சகத்திற்கு அளிக்க வேண்டும்")
        ],
        "correct_idx": 1,
        "exp_en": "Rule 8(1)(d) prohibits a law officer from communicating with the press or media regarding any matter pending before any court or on which advice has been given or is being tendered to the Government.",
        "exp_ta": "விதி 8(1)(d), நீதிமன்றத்தில் நிலுவையிலுள்ள விவகாரங்கள் அல்லது அரசுக்கு அளிக்கப்பட்ட சட்ட ஆலோசனைகள் குறித்து ஊடகங்கள் அல்லது பத்திரிகைகளில் பேசுவதை சட்ட அதிகாரிகளுக்கு தடை செய்கிறது.",
        "tip": "Preserves sub-judice integrity and attorney-client confidentiality.",
        "fact": "Violations of this rule can lead to termination of assignment under Rule 12."
    },
    # 14
    {
        "stem_en": "Who served as the 12th Attorney General of India from July 2004 to June 2009, handling the Bihar Assembly dissolution case (Rameshwar Prasad v. UOI)?",
        "stem_ta": "2004 ஜூலை முதல் 2009 ஜூன் வரை 12-வது தலைமை வழக்கறிஞராக பணியாற்றி, பீகார் சட்டமன்ற கலைப்பு வழக்கை (ராமேஷ்வர் பிரசாத் வழக்கு) நடத்தியவர் யார்?",
        "options": [
            ("M.C. Setalvad", "எம்.சி. செதல்வாட்"),
            ("Milon K. Banerjee", "மிலன் கே. பானர்ஜி"),
            ("G.E. Vahanvati", "ஜி.இ. வாகனவதி"),
            ("Ashok Desai", "அசோக் தேசாய்")
        ],
        "correct_idx": 1,
        "exp_en": "Milon K. Banerjee served his second term as Attorney General from July 2004 to June 2009 under the UPA-1 government, defending the presidential proclamation dissolving the Bihar Assembly in Rameshwar Prasad (2006).",
        "exp_ta": "மிலன் கே. பானர்ஜி 2004 முதல் 2009 வரை தனது இரண்டாவது பதவிக்காலத்தில் UPA-1 அரசில் தலைமை வழக்கறிஞராக இருந்து, பீகார் சட்டமன்றத்தை கலைத்த குடியரசுத் தலைவர் பிரகடனத்தை உச்ச நீதிமன்றத்தில் ஆதரித்து வாதாடினார்.",
        "tip": "The Supreme Court in Rameshwar Prasad (2006) held the dissolution of Bihar Assembly to be unconstitutional and malafide.",
        "fact": "Milon Banerjee is one of only two AGs (along with Soli Sorabjee) to serve two distinct terms."
    },
    # 15
    {
        "stem_en": "Can the Attorney General of India be appointed as a Senior Advocate by the Supreme Court of India under Section 16 of the Advocates Act 1961?",
        "stem_ta": "1961 வழக்கறிஞர்கள் சட்டத்தின் பிரிவு 16-ன் கீழ் இந்திய தலைமை வழக்கறிஞரை உச்ச நீதிமன்றம் மூத்த வழக்கறிஞராக (Senior Advocate) நியமிக்க முடியுமா?",
        "options": [
            ("No, constitutional officers cannot be designated", "இல்லை, அரசியலமைப்பு அதிகாரிகளை அவ்வாறு நியமிக்க முடியாது"),
            ("Practically all Attorneys General are already designated Senior Advocates of extraordinary standing prior to their appointment as AG", "நடைமுறையில் அனைத்து தலைமை வழக்கறிஞர்களும் AG-யாக நியமிக்கப்படுவதற்கு முன்பே உச்ச நீதிமன்றத்தால் மூத்த வழக்கறிஞர்களாக (Senior Advocates) அங்கீகரிக்கப்பட்டவர்களாகவே உள்ளனர்"),
            ("He is automatically deemed a Senior Advocate for life only upon retirement", "ஓய்வுபெற்ற பிறகு மட்டுமே அவர் தானாக மூத்த வழக்கறிஞராக கருதப்படுவார்"),
            ("Designation requires clearance from the Law Commission", "மூத்த வழக்கறிஞர் அந்தஸ்திற்கு சட்ட ஆணைய அனுமதி தேவை")
        ],
        "correct_idx": 1,
        "exp_en": "Under Section 16 of the Advocates Act 1961, the Supreme Court or High Courts designate advocates as Senior Advocates based on their ability, standing at the Bar, and experience. In practice, only senior designated advocates are considered for appointment as AG.",
        "exp_ta": "1961 வழக்கறிஞர்கள் சட்டத்தின் பிரிவு 16-ன் கீழ் நீதிமன்றங்கள் மூத்த வழக்கறிஞர் அந்தஸ்தை வழங்குகின்றன. நடைமுறையில், மிகச்சிறந்த அனுபவமும் நற்பெயரும் கொண்ட மூத்த வழக்கறிஞர்களே தலைமை வழக்கறிஞராக நியமிக்கப்படுகின்றனர்.",
        "tip": "Senior Advocates wear a gown with flaps and cannot file a vakalatnama directly (they must be briefed by an AoR).",
        "fact": "Both K.K. Venugopal and R. Venkataramani were designated Senior Advocates decades before becoming AG."
    },
    # 16
    {
        "stem_en": "Under Article 76, can an Attorney General who has tendered legal advice to a Union Ministry later accept a private brief to challenge that very advice in court after resigning?",
        "stem_ta": "சரத்து 76-ன் கீழ், ஒரு மத்திய அமைச்சகத்திற்கு சட்ட ஆலோசனை வழங்கிய தலைமை வழக்கறிஞர், பதவி விலகிய பிறகு அந்த ஆலோசனையை நீதிமன்றத்தில் எதிர்த்து ஒரு தனியார் கட்சிக்காக வாதாட முடியுமா?",
        "options": [
            ("Yes, once resigned all obligations cease", "ஆம், பதவி விலகியவுடன் அனைத்து கடமைகளும் முடிந்துவிடுவதால்"),
            ("No, professional ethics (Bar Council of India Rules) and fiduciary duty strictly prohibit an advocate from appearing against advice previously given by him to a former client", "இல்லை, தொழில்முறை நெறிமுறைகள் (பார் கவுன்சில் விதிகள்) தனது முன்னாள் வாடிக்கையாளருக்கு தானே முன்பு வழங்கிய சட்ட ஆலோசனைக்கு எதிராக வாதாடுவதை கடுமையாக தடை செய்கின்றன"),
            ("Only with the permission of the new Prime Minister", "புதிய பிரதமரின் அனுமதியுடன் மட்டுமே"),
            ("Only after a cooling-off period of 10 years", "10 ஆண்டு அமைதிக்காலத்திற்குப் பிறகு மட்டுமே")
        ],
        "correct_idx": 1,
        "exp_en": "Under Rule 9 of the Bar Council of India Rules (Standards of Professional Conduct and Etiquette), an advocate shall not appear for any party against a former client in any matter where he has advised or acquired confidential information, maintaining fiduciary integrity.",
        "exp_ta": "இந்திய பார் கவுன்சில் விதிகளின் கீழ், ஒரு வழக்கறிஞர் தான் முன்பு சட்ட ஆலோசனை வழங்கிய அல்லது ரகசிய தகவல்களைப் பெற்ற ஒரு விவகாரத்தில் தனது முன்னாள் வாடிக்கையாளருக்கு எதிராக பின்னர் ஆஜராக முடியாது.",
        "tip": "Fiduciary duty of confidentiality outlasts the tenure of office.",
        "fact": "Section 126 of the Evidence Act explicitly provides that professional privilege continues after the employment has ceased."
    },
    # 17
    {
        "stem_en": "In what way does the office of the Attorney General of India interact with the Supreme Court's 'Original Jurisdiction' under Article 131?",
        "stem_ta": "சரத்து 131-ன் கீழான உச்ச நீதிமன்றத்தின் 'அசல் அதிகார வரம்பு' விவகாரங்களில் இந்திய தலைமை வழக்கறிஞர் அலுவலகம் எவ்வாறு செயல்படுகிறது?",
        "options": [
            ("The AG acts as the sole judge in Article 131 disputes", "சரத்து 131 வழக்குகளில் AG மட்டுமே தனி நீதிபதியாக செயல்படுகிறார்"),
            ("The AG leads the legal team defending the Union of India when one or more States file an original suit against the Centre", "மத்திய அரசுக்கு எதிராக ஒன்று அல்லது அதற்கு மேற்பட்ட மாநிலங்கள் அசல் வழக்கு தாக்கல் செய்யும் போது இந்திய அரசைப் பாதுகாக்கும் சட்டக் குழுவிற்கு தலைமை தாங்குகிறார்"),
            ("The AG decides whether the Supreme Court can hear the case", "உச்ச நீதிமன்றம் வழக்கை விசாரிக்கலாமா என்பதை AG தீர்மானிக்கிறார்"),
            ("Article 131 suits can only be filed by the AG personally", "சரத்து 131 வழக்குகளை AG மட்டுமே நேரில் தாக்கல் செய்ய முடியும்")
        ],
        "correct_idx": 1,
        "exp_en": "Article 131 gives the Supreme Court exclusive original jurisdiction over disputes between the Centre and one or more States. In such federal constitutional battles, the Attorney General represents the Union of India as its chief advocate.",
        "exp_ta": "மத்திய-மாநில அரசுகளுக்கு இடையிலான தகராறுகளை விசாரிக்கும் சரத்து 131 அசல் அதிகார வரம்பு வழக்குகளில், இந்திய அரசாங்கத்தின் சார்பில் தலைமை வழக்கறிஞர் உச்ச நீதிமன்றத்தில் வாதிடுகிறார்.",
        "tip": "Recent Article 131 suits include challenges by Kerala and Punjab to the Citizenship Amendment Act (CAA).",
        "fact": "State Governments are represented by their respective Advocates General or Senior Advocates."
    },
    # 18
    {
        "stem_en": "In the landmark Berubari Union Reference (1960) under Article 143, who appeared as the Attorney General representing the Government of India on the cession of Indian territory to Pakistan?",
        "stem_ta": "1960-ல் இந்திய நிலப்பரப்பை பாகிஸ்தானுக்கு மாற்றுவது தொடர்பான பெருபாரி யூனியன் ஆலோசனைக் குறிப்பில் (சரத்து 143) மத்திய அரசுக்காக ஆஜரான தலைமை வழக்கறிஞர் யார்?",
        "options": [
            ("C.K. Daphtary", "சி.கே. தப்தாரி"),
            ("M.C. Setalvad", "எம்.சி. செதல்வாட்"),
            ("Niren De", "நிரேன் டே"),
            ("S.V. Gupte", "எஸ்.வி. குப்தே")
        ],
        "correct_idx": 1,
        "exp_en": "Attorney General M.C. Setalvad represented the Government of India in the historic In re Berubari Union (1960) reference, where the Supreme Court held that cession of Indian territory to a foreign country requires a constitutional amendment under Article 368.",
        "exp_ta": "1960-ல் பெருபாரி யூனியன் ஆலோசனைக் குறிப்பில் மத்திய அரசுக்காக தலைமை வழக்கறிஞர் எம்.சி. செதல்வாட் ஆஜரானார்; இந்திய நிலப்பகுதியை வெளிநாட்டுக்கு வழங்க சரத்து 368-ன் கீழ் அரசியலமைப்பு திருத்தம் அவசியம் என நீதிமன்றம் தீர்ப்பளித்தது.",
        "tip": "Led to the enactment of the Constitution (9th Amendment) Act, 1960.",
        "fact": "The Court also famously remarked that the Preamble was not a part of the Constitution (later overruled in Kesavananda Bharati)."
    },
    # 19
    {
        "stem_en": "Under the Law Officers Rules, can the Attorney General of India give an opinion or advice to any Ministry on a matter without a formal reference from the Ministry of Law and Justice?",
        "stem_ta": "சட்ட அதிகாரிகள் விதிகளின் கீழ், மத்திய சட்ட அமைச்சகத்தின் முறையான பரிந்துரை இன்றி எந்தவொரு அமைச்சகத்திற்கும் தலைமை வழக்கறிஞர் நேரடியாக கருத்து அல்லது ஆலோசனை வழங்க முடியுமா?",
        "options": [
            ("Yes, any minister can directly call the AG for advice", "ஆம், எந்த அமைச்சரும் நேரடியாக AG-யை அழைத்து ஆலோசனை பெறலாம்"),
            ("No, all matters requiring the opinion of the Attorney General must be formally routed through the Ministry of Law and Justice (Department of Legal Affairs)", "இல்லை, தலைமை வழக்கறிஞரின் ஆலோசனை தேவைப்படும் அனைத்து விவகாரங்களும் மத்திய சட்ட அமைச்சகத்தின் (சட்ட விவகாரங்கள் துறை) வழியாகவே முறையாக அனுப்பப்பட வேண்டும்"),
            ("Only the Prime Minister's Office can bypass the Law Ministry", "பிரதமர் அலுவலகம் மட்டுமே சட்ட அமைச்சகத்தை புறக்கணிக்க முடியும்"),
            ("Only during wartime", "போர்க் காலத்தில் மட்டுமே")
        ],
        "correct_idx": 1,
        "exp_en": "Under Rule 4 of the Law Officers Rules, all references for the opinion of the Attorney General must be prepared and referred exclusively by the Department of Legal Affairs of the Ministry of Law and Justice. Administrative ministries cannot write directly to the AG.",
        "exp_ta": "விதி 4-ன் படி, தலைமை வழக்கறிஞரின் கருத்து தேவைப்படும் அனைத்து கோப்புகளும் சட்ட அமைச்சகத்தின் சட்ட விவகாரங்கள் துறை மூலமாக மட்டுமே அனுப்பப்பட வேண்டும்; அமைச்சகங்கள் நேரடியாக AG-யை அணுக முடியாது.",
        "tip": "Ensures systematic scrutiny and prevents conflicting legal opinions across ministries.",
        "fact": "The Law Secretary reviews the reference file before placing it before the Attorney General."
    },
    # 20
    {
        "stem_en": "In the landmark Golaknath v. State of Punjab (1967) case, which Attorney General represented the Union of India defending Parliament's unlimited constituent power to amend Fundamental Rights?",
        "stem_ta": "அடிப்படை உரிமைகளைத் திருத்தும் நாடாளுமன்றத்தின் அதிகாரத்தை ஆதரித்து கோலக்நாத் எதிர் பஞ்சாப் மாநிலம் (1967) வழக்கில் மத்திய அரசுக்காக ஆஜரான தலைமை வழக்கறிஞர் யார்?",
        "options": [
            ("M.C. Setalvad", "எம்.சி. செதல்வாட்"),
            ("C.K. Daphtary", "சி.கே. தப்தாரி"),
            ("Niren De", "நிரேன் டே"),
            ("Soli Sorabjee", "சோலி சோராப்ஜி")
        ],
        "correct_idx": 1,
        "exp_en": "Attorney General C.K. Daphtary represented the Union of India before the 11-judge bench in Golaknath (1967), arguing that Article 368 contains plenary constituent power to amend any provision of the Constitution, including Part III.",
        "exp_ta": "1967-ல் 11 நீதிபதிகள் கொண்ட அமர்வில் கோலக்நாத் வழக்கில் தலைமை வழக்கறிஞர் சி.கே. தப்தாரி ஆஜராகி, சரத்து 368-ன் கீழ் அடிப்படை உரிமைகள் உட்பட அரசியலமைப்பின் எந்தப் பகுதியையும் திருத்த நாடாளுமன்றத்திற்கு முழு அதிகாரம் உண்டு என வாதாடினார்.",
        "tip": "The Supreme Court ruled 6:5 that Parliament cannot abridge Fundamental Rights under Article 368.",
        "fact": "This ruling was later overturned by the 13-judge bench in Kesavananda Bharati (1973)."
    },
    # 21
    {
        "stem_en": "Does the Attorney General of India have the constitutional power to issue binding directions to the Advocate General of any State?",
        "stem_ta": "எந்தவொரு மாநில தலைமை வழக்கறிஞருக்கும் (Advocate General) கட்டாய உத்தரவுகளைப் பிறப்பிக்கும் அரசியலமைப்பு அதிகாரம் இந்திய தலைமை வழக்கறிஞருக்கு உண்டா?",
        "options": [
            ("Yes, the Advocate General is an administrative subordinate of the AG", "ஆம், அட்வகேட் ஜெனரல் AG-க்கு நிர்வாக ரீதியாக கீழ்ப்பட்டவர்"),
            ("No, the Advocate General is an independent constitutional authority under Article 165 for the State, not subordinate to the Attorney General", "இல்லை, அட்வகேட் ஜெனரல் சரத்து 165-ன் கீழ் மாநிலத்திற்கான சுயாதீன அரசியலமைப்பு அதிகாரியாவார்; அவர் இந்திய AG-க்கு கீழ்ப்பட்டவர் அல்ல"),
            ("Yes, but only in matters relating to national security", "ஆம், ஆனால் தேசிய பாதுகாப்பு விவகாரங்களில் மட்டுமே"),
            ("Yes, under Article 256 of the Constitution", "ஆம், அரசியலமைப்பின் சரத்து 256-ன் கீழ்")
        ],
        "correct_idx": 1,
        "exp_en": "In our federal constitutional structure, the Advocate General under Article 165 is an independent constitutional functionary of the State appointed by the Governor. He is NOT a subordinate of the Attorney General of India and receives no directions from him.",
        "exp_ta": "கூட்டாட்சி அமைப்பில், அட்வகேட் ஜெனரல் ஆளுநரால் நியமிக்கப்படும் மாநிலத்தின் தனித்துவமான அரசியலமைப்பு அதிகாரியாவார். அவர் இந்திய தலைமை வழக்கறிஞருக்கு கீழ்ப்பட்டவர் அல்ல; அவரிடமிருந்து உத்தரவுகளைப் பெறுவதில்லை.",
        "tip": "Federal distribution of powers: AG represents the Union; Advocate General represents the State.",
        "fact": "They operate as co-equal leaders of their respective Union and State Bars."
    },
    # 22
    {
        "stem_en": "In the landmark Sea Customs Act Reference (1963) under Article 143, what federal constitutional issue did Attorney General C.K. Daphtary argue regarding Article 289?",
        "stem_ta": "1963-ல் கடல் சுங்கச் சட்ட ஆலோசனைக் குறிப்பில் (சரத்து 143), சரத்து 289 தொடர்பாக தலைமை வழக்கறிஞர் சி.கே. தப்தாரி முன்வைத்த கூட்டாட்சி அரசியலமைப்பு வாதம் என்ன?",
        "options": [
            ("States are exempt from all central customs and excise duties", "மத்திய சுங்க மற்றும் கலால் வரிகளிலிருந்து மாநிலங்களுக்கு முழு விலக்கு உண்டு"),
            ("Article 289 exempts State property from direct Union taxes, but the Union can levy indirect taxes like customs and excise duties on goods imported or produced by States", "சரத்து 289 மாநில சொத்துக்களுக்கு மத்திய நேரடி வரிகளிலிருந்து மட்டுமே விலக்கு அளிக்கிறது; மாநிலங்கள் இறக்குமதி செய்யும் பொருட்களின் மீது சுங்க மற்றும் கலால் போன்ற மறைமுக வரிகளை மத்திய அரசு விதிக்க முடியும்"),
            ("Customs duties are collected by State Governments", "சுங்க வரிகளை மாநில அரசுகளே வசூலிக்கின்றன"),
            ("Sea Customs Act was struck down as unconstitutional", "கடல் சுங்கச் சட்டம் அரசியலமைப்பிற்கு எதிரானது என ரத்து செய்யப்பட்டது")
        ],
        "correct_idx": 1,
        "exp_en": "In In re Sea Customs Act (1963), the 9-judge bench upheld Attorney General C.K. Daphtary's argument that Article 289(1) exempts State property from direct Union taxation only; the Union has the power to levy customs and excise duties (indirect taxes) on goods owned by State Governments.",
        "exp_ta": "1963 கடல் சுங்கச் சட்ட வழக்கில், சரத்து 289(1) நேரடி வரிகளுக்கு மட்டுமே விலக்கு அளிக்கிறது என்றும், மாநில அரசுக்கு சொந்தமான பொருட்களின் மீது மத்திய அரசு மறைமுக வரிகளை (சுங்க/கலால் வரி) விதிக்க முடியும் என்ற AG தப்தாரியின் வாதத்தை 9 நீதிபதிகள் கொண்ட அமர்வு ஏற்றுக்கொண்டது.",
        "tip": "Fundamental ruling on Union-State financial relations and tax immunity under Article 289.",
        "fact": "Delivered by a 5:4 majority led by Chief Justice B.P. Sinha."
    },
    # 23
    {
        "stem_en": "Can the Attorney General of India appear in a High Court on behalf of a private party to challenge an order passed by a State Government?",
        "stem_ta": "ஒரு மாநில அரசு பிறப்பித்த உத்தரவை எதிர்த்து ஒரு தனியார் வாடிக்கையாளரின் சார்பில் உயர்நீதிமன்றத்தில் தலைமை வழக்கறிஞர் ஆஜராகி வாதாட முடியுமா?",
        "options": [
            ("No, he cannot appear against any government in India", "இல்லை, இந்தியாவில் உள்ள எந்த அரசுக்கும் எதிராக அவர் ஆஜராக முடியாது"),
            ("Yes, provided the Government of India is not an adverse party and has no contrary interest in the litigation", "ஆம், இந்திய அரசாங்கம் அதில் எதிர் தரப்பாக இல்லாமலும் வழக்கில் மத்திய அரசின் நலன்களுக்கு முரண்பாடு இல்லாமலும் இருந்தால் ஆஜராகலாம்"),
            ("Only with the written consent of the State Chief Minister", "மாநில முதல்வரின் எழுத்துப்பூர்வ ஒப்புதலுடன் மட்டுமே"),
            ("Only in civil property disputes above Rs 10 Crore", "ரூ.10 கோடிக்கு மேற்பட்ட சொத்து வழக்குகளில் மட்டுமே")
        ],
        "correct_idx": 1,
        "exp_en": "The Attorney General's duty of loyalty is strictly to the Government of India (Union executive). He is not barred from representing a private client against a State Government in a High Court, provided the Union of India's interests are not affected.",
        "exp_ta": "தலைமை வழக்கறிஞரின் விசுவாசம் இந்திய அரசாங்கத்திற்கு மட்டுமே உரியது. மத்திய அரசின் நலன்கள் பாதிக்கப்படாத வரை, உயர்நீதிமன்றத்தில் ஒரு மாநில அரசுக்கு எதிராக தனியார் வாடிக்கையாளருக்காக அவர் ஆஜராக எந்த தடையும் இல்லை.",
        "tip": "State Governments are defended by their own Advocates General or Standing Counsels.",
        "fact": "This reinforces that the AG is not a general government employee of all governments in India."
    },
    # 24
    {
        "stem_en": "In the historic Cauvery Water Disputes Tribunal Reference (1991) under Article 143, who appeared as the Attorney General for the Union of India?",
        "stem_ta": "1991-ல் காவேரி நதிநீர் தீர்ப்பாய ஆலோசனைக் குறிப்பில் (சரத்து 143) மத்திய அரசுக்காக ஆஜரான இந்திய தலைமை வழக்கறிஞர் யார்?",
        "options": [
            ("M.C. Setalvad", "எம்.சி. செதல்வாட்"),
            ("G. Ramaswamy", "ஜி. ராமசுவாமி"),
            ("K. Parasaran", "கே. பராசரன்"),
            ("Soli Sorabjee", "சோலி சோராப்ஜி")
        ],
        "correct_idx": 1,
        "exp_en": "Senior Advocate G. Ramaswamy was the 8th Attorney General of India (1990-1992) and represented the Union Government in the landmark 1991 Cauvery Water Disputes Tribunal Reference under Article 143.",
        "exp_ta": "மூத்த வழக்கறிஞர் ஜி. ராமசுவாமி 1990 முதல் 1992 வரை இந்தியாவின் 8-வது தலைமை வழக்கறிஞராக பணியாற்றி, 1991 காவேரி நதிநீர் தீர்ப்பாய சரத்து 143 ஆலோசனைக் குறிப்பில் மத்திய அரசுக்காக ஆஜரானார்.",
        "tip": "The Supreme Court held that the Karnataka ordinance overriding the Tribunal's interim order was unconstitutional.",
        "fact": "G. Ramaswamy was previously the Advocate General of Tamil Nadu and Solicitor General of India."
    },
    # 25
    {
        "stem_en": "Under the Supreme Court Rules, when the Attorney General appears in a matter, where is he traditionally seated in the courtroom of the Chief Justice of India?",
        "stem_ta": "உச்ச நீதிமன்ற நடைமுறைப்படி, தலைமை வழக்கறிஞர் ஆஜராகும்போது தலைமை நீதிபதியின் நீதிமன்ற அறையில் அவர் பாரம்பரியமாக எங்கு அமர்கிறார்?",
        "options": [
            ("Any random seat in the back rows", "பின் வரிசையில் ஏதேனும் ஓர் இருக்கை"),
            ("The first seat on the extreme right of the front row (facing the Judges) traditionally reserved for the leader of the Bar", "பார் கவுன்சிலின் தலைவருக்காக முன்வரிசையில் தீவிர வலதுபுறத்தில் (நீதிபதிகளை நோக்கிய நிலையில்) பாரம்பரியமாக ஒதுக்கப்பட்டுள்ள முதல் இருக்கை"),
            ("Beside the court registrar", "நீதிமன்ற பதிவாளர் அருகில்"),
            ("On the judicial dias alongside the judges", "நீதிபதிகளுடன் மேடையில்")
        ],
        "correct_idx": 1,
        "exp_en": "In Courtroom No. 1 (and all other benches) of the Supreme Court, the first seat on the extreme right of the front counsel table is historically and permanently reserved for the Attorney General of India as the leader of the Indian Bar.",
        "exp_ta": "உச்ச நீதிமன்றத்தின் முதலாவது நீதிமன்ற அறையில், வழக்கறிஞர்களின் முன்வரிசையில் வலதுபுறத்தில் உள்ள முதல் இருக்கை இந்திய பார் கவுன்சிலின் தலைவர் என்ற முறையில் தலைமை வழக்கறிஞருக்காகவே நிரந்தரமாக ஒதுக்கப்பட்டுள்ளது.",
        "tip": "Reflects the AG's statutory right of pre-audience under Section 23 of Advocates Act 1961.",
        "fact": "The Solicitor General sits immediately next to the Attorney General."
    },
    # 26
    {
        "stem_en": "Who among the following served the shortest single continuous tenure as the Attorney General of India?",
        "stem_ta": "இந்திய தலைமை வழக்கறிஞராக மிகக் குறுகிய ஒற்றை தொடர்ச்சியான பதவிக்காலம் பணியாற்றியவர் யார்?",
        "options": [
            ("M.C. Setalvad", "எம்.சி. செதல்வாட்"),
            ("Soli Sorabjee (first term: December 1989 to December 1990, ~1 year)", "சோலி சோராப்ஜி (முதல் பதவிக்காலம்: டிசம்பர் 1989 முதல் டிசம்பர் 1990 வரை, ~1 ஆண்டு)"),
            ("K. Parasaran", "கே. பராசரன்"),
            ("Milon K. Banerjee", "மிலன் கே. பானர்ஜி")
        ],
        "correct_idx": 1,
        "exp_en": "Soli Sorabjee's first term as Attorney General lasted exactly one year (9 December 1989 to 2 December 1990) during the National Front government of Prime Minister V.P. Singh, representing the shortest tenure among full-term appointees.",
        "exp_ta": "வி.பி. சிங் ஆட்சிக் காலத்தில் சோலி சோராப்ஜியின் முதல் பதவிக்காலம் சரியாக ஒரு ஆண்டு மட்டுமே நீடித்தது (1989 டிசம்பர் முதல் 1990 டிசம்பர் வரை); இதுவே மிகக் குறுகிய பதவிக்காலமாகும்.",
        "tip": "Longest tenure = M.C. Setalvad (13 years); Shortest full-term tenure = Soli Sorabjee (1st term, 1 year).",
        "fact": "He resigned when the V.P. Singh government collapsed following the withdrawal of support."
    },
    # 27
    {
        "stem_en": "In the historic Kesavananda Bharati case (1973), which private Senior Advocate appeared against Attorney General Niren De and formulated the 'Basic Structure' doctrine?",
        "stem_ta": "1973-ல் வரலாற்று சிறப்புமிக்க கேசவானந்த பாரதி வழக்கில், தலைமை வழக்கறிஞர் நிரேன் டே-வுக்கு எதிராக ஆஜராகி 'அடிப்படை கட்டமைப்பு' கோட்பாட்டை வாதாடி நிலைநாட்டிய மூத்த வழக்கறிஞர் யார்?",
        "options": [
            ("Fali S. Nariman", "பாலி எஸ். நாரிமன்"),
            ("Nanabhoy (Nani) Palkhivala", "நானாபாய் (நானி) பால்கிவாலா"),
            ("M.C. Chagla", "எம்.சி. சாக்லா"),
            ("Ram Jethmalani", "ராம் ஜெத்மலானி")
        ],
        "correct_idx": 1,
        "exp_en": "Legendary constitutional jurist Nani Palkhivala argued for Kesavananda Bharati and the petitioners across 66 days before the 13-judge bench, defeating the Union Government's argument of unlimited amending power led by AG Niren De.",
        "exp_ta": "புகழ்பெற்ற சட்ட அறிஞர் நானி பால்கிவாலா 13 நீதிபதிகள் கொண்ட அமர்வின் முன் 66 நாட்கள் வாதாடி, தலைமை வழக்கறிஞர் நிரேன் டே முன்வைத்த வரம்பற்ற திருத்த அதிகார வாதத்தை முறியடித்து அடிப்படைக் கட்டமைப்பு கோட்பாட்டை நிறுவினார்.",
        "tip": "Palkhivala was offered the office of Attorney General by the Janata government in 1977, but declined.",
        "fact": "The 7:6 majority judgment saved constitutional democracy from executive authoritarianism."
    },
    # 28
    {
        "stem_en": "What is the constitutional significance of Article 76(1) stating that the Attorney General must be a person 'qualified to be appointed a Judge of the Supreme Court' rather than 'a retired Supreme Court Judge'?",
        "stem_ta": "சரத்து 76(1)-ல் தலைமை வழக்கறிஞர் 'ஓய்வுபெற்ற உச்ச நீதிமன்ற நீதிபதியாக' இருக்க வேண்டும் என்று கூறாமல், 'உச்ச நீதிமன்ற நீதிபதியாக நியமிக்கப்பட தகுதியுள்ளவராக' இருக்க வேண்டும் என்று கூறுவதன் அரசியலமைப்பு முக்கியத்துவம் என்ன?",
        "options": [
            ("It is a drafting error by the Constituent Assembly", "இது அரசியலமைப்பு நிர்ணய சபையின் வரைவுப் பிழை"),
            ("It intentionally allows active practicing senior advocates of the Bar to be appointed, preserving the tradition of appointing an independent practicing leader of the Bar rather than an ex-judge", "ஓய்வுபெற்ற நீதிபதிக்கு பதிலாக நீதிமன்றத்தில் வழக்கறிஞராக வாதாடும் ஒரு சுதந்திரமான மூத்த வழக்கறிஞரை நியமிக்க வேண்டும் என்ற மரபைப் பாதுகாப்பதற்காக இது திட்டமிட்டு வைக்கப்பட்டது"),
            ("It prevents advocates from ever becoming AG", "வழக்கறிஞர்கள் AG ஆவதை தடுக்க"),
            ("It allows foreign lawyers to be appointed", "வெளிநாட்டு வழக்கறிஞர்களை நியமிக்க அனுமதிக்க")
        ],
        "correct_idx": 1,
        "exp_en": "The framers deliberately drafted Article 76(1) to enable the appointment of distinguished practicing advocates who have the vigor to argue in courts daily as counsel for the Republic, rather than retired judges who might not actively practice.",
        "exp_ta": "அரசியலமைப்பை உருவாக்கியவர்கள் திட்டமிட்டே இந்நிபந்தனையை வைத்தனர்; ஓய்வுபெற்ற நீதிபதியை விட, நீதிமன்றத்தில் தினமும் விறுவிறுப்பாக வழக்காடும் ஆற்றல் கொண்ட முன்னணி மூத்த வழக்கறிஞரே குடியரசின் வழக்குகளை நடத்த தகுதியானவர் என்பதால் இந்நிலை எடுக்கப்பட்டது.",
        "tip": "The AG is an active courtroom advocate, not an adjudicator.",
        "fact": "Under Article 124(7), a retired Supreme Court judge is permanently debarred from practicing in any court in India."
    },
    # 29
    {
        "stem_en": "In the landmark judgment of Supreme Court Bar Association v. Union of India (1998), who appeared as the Attorney General assisting the Court on the scope of contempt powers under Article 129?",
        "stem_ta": "உச்ச நீதிமன்ற பார் அசோசியேஷன் எதிர் இந்திய ஒன்றியம் (1998) வழக்கில், சரத்து 129-ன் கீழான அவமதிப்பு அதிகாரங்களின் வரம்பு குறித்து நீதிமன்றத்திற்கு உதவிய தலைமை வழக்கறிஞர் யார்?",
        "options": [
            ("M.C. Setalvad", "எம்.சி. செதல்வாட்"),
            ("Ashok Desai", "அசோக் தேசாய்"),
            ("Soli Sorabjee", "சோலி சோராப்ஜி"),
            ("Niren De", "நிரேன் டே")
        ],
        "correct_idx": 1,
        "exp_en": "Senior Advocate Ashok Desai served as Attorney General of India from 1996 to 1998 under the United Front governments and assisted the Constitution Bench in Supreme Court Bar Association (1998) on contempt powers.",
        "exp_ta": "அசோக் தேசாய் 1996 முதல் 1998 வரை ஐக்கிய முன்னணி ஆட்சியில் தலைமை வழக்கறிஞராக பணியாற்றி, உச்ச நீதிமன்ற பார் அசோசியேஷன் வழக்கில் (1998) நீதிமன்ற அவமதிப்பு அதிகாரங்கள் குறித்து நீதிமன்றத்திற்கு உதவினார்.",
        "tip": "The SC held that it cannot suspend an advocate's license under contempt powers (only BCI can).",
        "fact": "Ashok Desai was awarded the Padma Bhushan in 2001."
    },
    # 30
    {
        "stem_en": "Under Section 55 of the Code of Criminal Procedure 1973 (CrPC) and contemporary laws, does the Attorney General of India have the power to enter a 'Nolle Prosequi' (withdraw a prosecution) on behalf of the State?",
        "stem_ta": "குற்றவியல் நடைமுறைச் சட்டத்தின் கீழ், தலைமை வழக்கறிஞர் அரசின் சார்பில் ஒரு குற்றவியல் வழக்கை திரும்பப் பெறும் (Nolle Prosequi) அதிகாரத்தைக் கொண்டுள்ளாரா?",
        "options": [
            ("Yes, absolute unilateral power without court permission", "ஆம், நீதிமன்ற அனுமதியின்றி முழுமையான அதிகாரம் உண்டு"),
            ("No, in India the statutory power to withdraw a prosecution under Section 321 CrPC (now BNSS) is vested exclusively in the Public Prosecutor or Assistant Public Prosecutor in charge of the case, subject to court consent", "இல்லை, இந்தியாவில் ஒரு வழக்கை திரும்பப் பெறும் அதிகாரம் பிரிவு 321 CrPC-ன் கீழ் சம்பந்தப்பட்ட அரசு வழக்கறிஞருக்கு மட்டுமே (Public Prosecutor) நீதிமன்ற அனுமதியுடன் உண்டு; AG-க்கு இல்லை"),
            ("Yes, in all High Courts", "ஆம், அனைத்து உயர்நீதிமன்றங்களிலும் உண்டு"),
            ("Yes, with the consent of the Chief Justice of India", "ஆம், இந்திய தலைமை நீதிபதியின் ஒப்புதலுடன்")
        ],
        "correct_idx": 1,
        "exp_en": "Unlike in England where the Attorney General can enter a nolle prosequi stopping criminal proceedings at will, in India Section 321 of CrPC (now Section 360 of BNSS) empowers only the Public Prosecutor in charge of the case to withdraw with the consent of the court.",
        "exp_ta": "பிரிட்டனைப் போலன்றி, இந்தியாவில் தலைமை வழக்கறிஞர் தன்னிச்சையாக குற்றவியல் வழக்குகளை திரும்பப் பெற முடியாது; பிரிவு 321 CrPC-ன் கீழ் வழக்கை நடத்தும் அரசு வழக்கறிஞர் (Public Prosecutor) மட்டுமே நீதிமன்ற அனுமதியுடன் திரும்பப் பெற முடியும்.",
        "tip": "State of Bihar v. Ram Naresh Pandey (1957) is the leading precedent on Section 321.",
        "fact": "This separation prevents political interference in criminal prosecutions by high officers of state."
    },
    # 31
    {
        "stem_en": "In which landmark case did the Supreme Court examine whether the Attorney General of India is an 'officer of the court' first and a 'counsel for the government' second?",
        "stem_ta": "தலைமை வழக்கறிஞர் முதலில் 'நீதிமன்றத்தின் அதிகாரி' (Officer of the Court) என்றும், இரண்டாவதாகவே 'அரசின் வழக்கறிஞர்' என்றும் உச்ச நீதிமன்றம் எந்த முக்கிய வழக்கில் குறிப்பிட்டது?",
        "options": [
            ("Kesavananda Bharati case", "கேசவானந்த பாரதி வழக்கு"),
            ("Re: Sanjiv Datta, Deputy Secretary, Ministry of Information (1995)", "சஞ்சீவ் தத்தா வழக்கு (1995)"),
            ("Minerva Mills case", "மினர்வா மில்ஸ் வழக்கு"),
            ("Maneka Gandhi case", "மேனகா காந்தி வழக்கு")
        ],
        "correct_idx": 1,
        "exp_en": "In Re: Sanjiv Datta (1995), the Supreme Court observed that the Attorney General, like all advocates but to an even higher degree, is an officer of the court whose first loyalty is to the administration of justice and truth, and not merely to winning a case for the government.",
        "exp_ta": "1995-ல் சஞ்சீவ் தத்தா வழக்கில், தலைமை வழக்கறிஞர் மற்ற வழக்கறிஞர்களை விடவும் மிக உயர்ந்த அளவில் நீதிமன்றத்தின் அதிகாரியாவார் என்றும், அவரது முதல் கடமை நீதி நிர்வாகத்திற்கும் உண்மைக்கும் உரியதே தவிர அரசுக்காக வழக்கை வெல்வது மட்டுமே அல்ல என்றும் உச்ச நீதிமன்றம் குறிப்பிட்டது.",
        "tip": "High constitutional ethics govern the conduct of law officers in India.",
        "fact": "The AG is expected to concede points of law if the government's stance is constitutionally untenable."
    },
    # 32
    {
        "stem_en": "During the Sino-Indian War of 1962, which Attorney General advised the Government on the proclamation of the first National Emergency under Article 352?",
        "stem_ta": "1962 இந்தியா-சீனா போரின் போது, சரத்து 352-ன் கீழ் நாட்டின் முதல் தேசிய அவசரநிலையை பிரகடனப்படுத்துவது குறித்து அரசுக்கு ஆலோசனை வழங்கிய தலைமை வழக்கறிஞர் யார்?",
        "options": [
            ("C.K. Daphtary", "சி.கே. தப்தாரி"),
            ("M.C. Setalvad", "எம்.சி. செதல்வாட்"),
            ("Niren De", "நிரேன் டே"),
            ("S.V. Gupte", "எஸ்.வி. குப்தே")
        ],
        "correct_idx": 1,
        "exp_en": "M.C. Setalvad was the Attorney General when the first National Emergency was proclaimed on 26 October 1962 following Chinese aggression, advising the Nehru government on the Defence of India Act and fundamental rights suspension under Article 359.",
        "exp_ta": "1962 அக்டோபர் 26 அன்று சீன ஆக்கிரமிப்பைத் தொடர்ந்து நாட்டின் முதல் தேசிய அவசரநிலை பிரகடனம் செய்யப்பட்ட போது, இந்திய பாதுகாப்புச் சட்டம் குறித்து நேரு அரசுக்கு ஆலோசனை வழங்கிய தலைமை வழக்கறிஞர் எம்.சி. செதல்வாட் ஆவார்.",
        "tip": "First National Emergency lasted from October 1962 to January 1968.",
        "fact": "Makhan Singh v. State of Punjab (1964) tested the constitutional validity of detentions under this emergency."
    },
    # 33
    {
        "stem_en": "Under Article 76, can Parliament by ordinary legislation alter or diminish the constitutional powers of the Attorney General of India?",
        "stem_ta": "சரத்து 76-ன் கீழ் உள்ள இந்திய தலைமை வழக்கறிஞரின் அரசியலமைப்பு அதிகாரங்களை நாடாளுமன்றம் ஒரு சாதாரண சட்டத்தின் மூலம் மாற்றவோ அல்லது குறைக்கவோ முடியுமா?",
        "options": [
            ("Yes, by simple majority", "ஆம், எளிய பெரும்பான்மை மூலம்"),
            ("No, constitutional powers conferred by Articles 76, 88, and 105 cannot be abrogated or diminished by ordinary legislation without a formal constitutional amendment under Article 368", "இல்லை, சரத்து 76, 88 மற்றும் 105 வழங்கும் அரசியலமைப்பு அதிகாரங்களை சரத்து 368-ன் கீழான முறையான அரசியலமைப்பு திருத்தம் இன்றி சாதாரண சட்டத்தால் ரத்து செய்யவோ குறைக்கவோ முடியாது"),
            ("Yes, with approval of the President", "ஆம், குடியரசுத் தலைவரின் ஒப்புதலுடன்"),
            ("Only during emergency", "அவசரநிலையின் போது மட்டுமே")
        ],
        "correct_idx": 1,
        "exp_en": "Since the powers of the Attorney General (right of audience in all courts, right to speak in Parliament, and parliamentary privileges) flow directly from Articles 76, 88, and 105, they cannot be whittled down by ordinary parliamentary statute.",
        "exp_ta": "தலைமை வழக்கறிஞரின் அதிகாரங்கள் (அனைத்து நீதிமன்றங்களிலும் வாதாடும் உரிமை, நாடாளுமன்றத்தில் பேசும் உரிமை, சிறப்புரிமைகள்) சரத்து 76, 88, 105 ஆகியவற்றிலிருந்து நேரடியாகப் பெறப்படுவதால், சாதாரண சட்டத்தால் அவற்றை குறைக்க முடியாது.",
        "tip": "Constitutional rights can only be amended via Article 368.",
        "fact": "Parliament can, however, confer additional statutory duties upon the AG."
    },
    # 34
    {
        "stem_en": "In the NJAC judgment (2015), what controversial argument advanced by Attorney General Mukul Rohatgi regarding the appointment of judges was rejected by the Constitution Bench?",
        "stem_ta": "2015 NJAC தீர்ப்பில், நீதிபதிகள் நியமனம் தொடர்பாக தலைமை வழக்கறிஞர் முகுல் ரோஹத்கி முன்வைத்த எந்த வாதத்தை உச்ச நீதிமன்ற அரசியலமைப்பு அமர்வு நிராகரித்தது?",
        "options": [
            ("That judges should be elected by direct public vote", "நீதிபதிகள் நேரடி மக்கள் வாக்களிப்பு மூலம் தேர்ந்தெடுக்கப்பட வேண்டும்"),
            ("That the primacy of the judiciary in judicial appointments is not an essential element of judicial independence or the Basic Structure", "நீதிபதிகள் நியமனத்தில் நீதித்துறையின் முதன்மைத்துவம் என்பது நீதித்துறை சுதந்திரத்தின் அல்லது அடிப்படைக் கட்டமைப்பின் இன்றியமையாத பகுதி அல்ல"),
            ("That the President has no power to sign warrants", "குடியரசுத் தலைவருக்கு நியமன ஆணையில் கையொப்பமிட அதிகாரம் இல்லை"),
            ("That High Courts should be abolished", "உயர்நீதிமன்றங்கள் ரத்து செய்யப்பட வேண்டும்")
        ],
        "correct_idx": 1,
        "exp_en": "The Attorney General argued that judicial primacy in appointments is not part of the Basic Structure and that the Second and Third Judges cases should be overruled. The 4:1 majority firmly rejected this, holding that judicial primacy is an indispensable facet of judicial independence.",
        "exp_ta": "நீதிபதிகள் நியமனத்தில் நீதித்துறையின் முதன்மைத்துவம் அடிப்படைக் கட்டமைப்பு அல்ல என்ற தலைமை வழக்கறிஞரின் வாதத்தை உச்ச நீதிமன்றம் நிராகரித்து, நீதித்துறை முதன்மைத்துவம் நீதித்துறை சுதந்திரத்தின் பிரிக்க முடியாத பகுதி என தீர்ப்பளித்தது.",
        "tip": "Justice J.S. Khehar authored the leading majority opinion.",
        "fact": "Justice J. Chelameswar was the lone dissenting judge upholding the NJAC Act."
    },
    # 35
    {
        "stem_en": "Who served as the 15th Attorney General of India and famously offered to resign multiple times due to advanced age before finally demitting office in September 2022?",
        "stem_ta": "தனது முதுமை காரணமாக பலமுறை பதவி விலக முன்வந்தும், இறுதியாக 2022 செப்டம்பரில் ஓய்வுபெற்ற இந்தியாவின் 15-வது தலைமை வழக்கறிஞர் யார்?",
        "options": [
            ("Mukul Rohatgi", "முகுல் ரோஹத்கி"),
            ("Kottayan Katankot (K.K.) Venugopal", "கே.கே. வேணுகோபால்"),
            ("R. Venkataramani", "ஆர். வெங்கடரமணி"),
            ("Milon Banerjee", "மிலன் பானர்ஜி")
        ],
        "correct_idx": 1,
        "exp_en": "Senior Advocate K.K. Venugopal was appointed as the 15th Attorney General in July 2017. Due to his advanced age (in his late 80s and 90s), he repeatedly requested to be relieved, but the Union Government persuaded him to take multiple one-year extensions until September 2022.",
        "exp_ta": "மூத்த வழக்கறிஞர் கே.கே. வேணுகோபால் 2017 ஜூலை முதல் 15-வது தலைமை வழக்கறிஞராக பொறுப்பேற்று, தனது 91-வது வயது வரை பல நீட்டிப்புகளைப் பெற்று 2022 செப்டம்பர் வரை சிறப்பான முறையில் பணியாற்றினார்.",
        "tip": "One of the most revered and experienced constitutional doyens in modern Indian history.",
        "fact": "He argued critical cases including the Article 370 revocation challenge, Rafale review, and Electoral Bonds."
    },
    # 36
    {
        "stem_en": "Under Article 76, can an Attorney General who resigns with the outgoing Council of Ministers be immediately reappointed by the incoming Council of Ministers?",
        "stem_ta": "சரத்து 76-ன் கீழ், பதவி விலகும் அமைச்சரவையுடன் சேர்ந்து ராஜினாமா செய்யும் தலைமை வழக்கறிஞரை, புதிதாக பொறுப்பேற்கும் அமைச்சரவை மீண்டும் உடனடியாக நியமிக்க முடியுமா?",
        "options": [
            ("No, re-appointment is unconstitutional", "இல்லை, மறுநியமனம் அரசியலமைப்பிற்கு எதிரானது"),
            ("Yes, there is no constitutional bar on reappointment, and the incoming government may choose to reappoint the same individual", "ஆம், மறுநியமனத்திற்கு எந்த அரசியலமைப்பு தடையும் இல்லை; புதிய அரசாங்கம் அதே நபரை மீண்டும் நியமிக்க தேர்வு செய்யலாம்"),
            ("Only if approved by the Chief Justice of India", "தலைமை நீதிபதி ஒப்புதல் அளித்தால் மட்டுமே"),
            ("Only after an interval of 3 years", "3 ஆண்டுகள் இடைவெளிக்குப் பிறகு மட்டுமே")
        ],
        "correct_idx": 1,
        "exp_en": "There is no constitutional bar on reappointment. When a new government takes office, it possesses full executive discretion to either appoint a new counsel or reappoint the incumbent Attorney General.",
        "exp_ta": "மறுநியமனத்திற்கு அரசியலமைப்பு ரீதியாக எந்த தடையும் இல்லை. புதிய அரசாங்கம் பதவியேற்கும் போது, புதிய ஒருவரை நியமிக்கவோ அல்லது பழைய தலைமை வழக்கறிஞரையே மீண்டும் தொடரச் செய்யவோ முழு உரிமை உண்டு.",
        "tip": "M.C. Setalvad continued across multiple general elections and successive Nehru cabinets.",
        "fact": "Soli Sorabjee and Milon Banerjee served across different governments in non-consecutive terms."
    },
    # 37
    {
        "stem_en": "In the landmark judgment of State of Punjab v. Satya Pal Dang (1969), what constitutional principle regarding the Advocate General's and Attorney General's presence in legislative proceedings was reaffirmed?",
        "stem_ta": "சத்யா பால் டாங் வழக்கில் (1969), சட்டமன்ற நடவடிக்கைகளில் தலைமை வழக்கறிஞரின் பங்கேற்பு குறித்து உறுதிப்படுத்தப்பட்ட அரசியலமைப்பு கொள்கை என்ன?",
        "options": [
            ("The law officer has casting vote", "சட்ட அதிகாரிக்கு சமநிலை வாக்குரிமை உண்டு"),
            ("The law officer's presence and advice in the House cannot validate unconstitutional legislative procedures, but enables the House to receive objective legal guidance", "அவையில் சட்ட அதிகாரியின் ஆலோசனையோ இருப்போ அரசியலமைப்புக்கு எதிரான நடைமுறைகளை சட்டப்பூர்வமாக்காது; ஆனால் அவைக்கு புறநிலையான சட்ட வழிகாட்டுதலை வழங்குகிறது"),
            ("The law officer can adjourn the House", "சட்ட அதிகாரி அவையை ஒத்திவைக்கலாம்"),
            ("The law officer sits as Speaker", "சட்ட அதிகாரி சபாநாயகராக அமர்கிறார்")
        ],
        "correct_idx": 1,
        "exp_en": "In Satya Pal Dang (1969), the Supreme Court ruled that while the law officer (Advocate General / Attorney General under Art 177 / 88) can address the legislature to assist on legal issues, their opinion cannot supersede or cure an illegal constitutional violation committed by the House.",
        "exp_ta": "1969 சத்யா பால் டாங் வழக்கில், சட்டமன்றத்தில் சட்ட அதிகாரி ஆலோசனை வழங்கினாலும், அவையினால் செய்யப்படும் அரசியலமைப்பு விதிமீறல்களை அந்த ஆலோசனை சட்டப்பூர்வமாக்க முடியாது என உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
        "tip": "The legislature remains subordinate to the Constitution, regardless of law officer opinions.",
        "fact": "This case dealt with the Punjab Governor's ordinance regulating legislative financial business."
    },
    # 38
    {
        "stem_en": "Under Article 76(4), does the Attorney General of India receive a constitutional pension upon retirement?",
        "stem_ta": "சரத்து 76(4)-ன் கீழ், ஓய்வுக்குப் பிறகு இந்திய தலைமை வழக்கறிஞருக்கு அரசியலமைப்பு ஓய்வூதியம் (Pension) வழங்கப்படுகிறதா?",
        "options": [
            ("Yes, equal to 50% of last drawn salary", "ஆம், கடைசியாக பெற்ற ஊதியத்தில் 50%"),
            ("No, there is no constitutional or statutory provision for pension for the Attorney General of India", "இல்லை, இந்திய தலைமை வழக்கறிஞருக்கு ஓய்வூதியம் வழங்க அரசியலமைப்பிலோ அல்லது சட்டத்திலோ எந்த விதியும் இல்லை"),
            ("Yes, if he has served for at least 5 years", "ஆம், குறைந்தது 5 ஆண்டுகள் பணியாற்றியிருந்தால்"),
            ("Pension is paid from the Supreme Court budget", "உச்ச நீதிமன்ற பட்ஜெட்டில் இருந்து ஓய்வூதியம் வழங்கப்படுகிறது")
        ],
        "correct_idx": 1,
        "exp_en": "Unlike Supreme Court and High Court judges who receive statutory pensions under the Judges Conditions of Service Acts, the Attorney General is a practicing advocate receiving retainership and fees, with NO pension entitlement upon demitting office.",
        "exp_ta": "உச்ச நீதிமன்ற மற்றும் உயர்நீதிமன்ற நீதிபதிகளைப் போலன்றி, தலைமை வழக்கறிஞர் தக்கவைப்புக் கட்டணம் மற்றும் வழக்குக் கட்டணம் மட்டுமே பெறும் ஒரு வழக்கறிஞர் என்பதால், அவருக்கு ஓய்வூதிய உரிமை எதுவும் இல்லை.",
        "tip": "High-yield comparison point: SC Judges get statutory pensions; the AG gets NO pension.",
        "fact": "Upon leaving office, the AG simply resumes full-time private legal practice at the Bar."
    },
    # 39
    {
        "stem_en": "In which landmark 2019 proceedings did Attorney General K.K. Venugopal invoke the Official Secrets Act 1923 regarding leaked documents in the Rafale fighter jet deal review?",
        "stem_ta": "ரஃபேல் போர் விமான ஒப்பந்த மறுஆய்வு வழக்கில், கசிந்த ஆவணங்கள் தொடர்பாக 1923 உத்தியோகபூர்வ ரகசியங்கள் சட்டத்தை தலைமை வழக்கறிஞர் கே.கே. வேணுகோபால் எந்த ஆண்டு உச்ச நீதிமன்றத்தில் குறிப்பிட்டார்?",
        "options": [
            ("2014", "2014"),
            ("2019 (Yashwant Sinha v. CBI / Rafale Review Petitions)", "2019 (யஷ்வந்த் சின்ஹா எதிர் சிபிஐ / ரஃபேல் மறுஆய்வு மனுக்கள்)"),
            ("2011", "2011"),
            ("2008", "2008")
        ],
        "correct_idx": 1,
        "exp_en": "In March 2019, Attorney General K.K. Venugopal argued before the Supreme Court that leaked MoD documents published by 'The Hindu' were stolen and covered by the Official Secrets Act. The Court, however, held that even stolen documents are admissible in evidence if relevant.",
        "exp_ta": "2019 மார்ச்சில் ரஃபேல் மறுஆய்வு வழக்கில், 'தி இந்து' நாளிதழில் வெளியான ஆவணங்கள் பாதுகாப்பு அமைச்சகத்திலிருந்து திருடப்பட்டவை என்றும் உத்தியோகபூர்வ ரகசியங்கள் சட்டத்தின் கீழ் வருபவை என்றும் AG வாதிட்டார்; ஆனால் அவை தொடர்புடையவை என்பதால் ஆதாரமாக ஏற்கப்படும் என நீதிமன்றம் தீர்ப்பளித்தது.",
        "tip": "Landmark ruling on evidentiary admissibility of leaked documents in constitutional litigation.",
        "fact": "The Court dismissed the review petitions on merits in November 2019."
    },
    # 40
    {
        "stem_en": "Under the Constitution of India, if an Attorney General of India dies in office, how is the temporary vacancy filled?",
        "stem_ta": "இந்திய அரசியலமைப்பின் கீழ், தலைமை வழக்கறிஞர் பதவியில் இருக்கும் போது மரணமடைந்தால் அந்த தற்காலிக காலிப்பணியிடம் எவ்வாறு நிரப்பப்படுகிறது?",
        "options": [
            ("The Solicitor General automatically becomes the Attorney General by constitutional succession", "அரசியலமைப்பு வாரிசுரிமைப்படி சொலிசிட்டர் ஜெனரல் தானாக தலைமை வழக்கறிஞராவார்"),
            ("There is no provision for acting or automatic succession; the President must appoint a new Attorney General under Article 76(1), while the Solicitor General manages urgent government litigation in the interim", "தானாக வாரிசுரிமை பெறும் விதி எதுவும் இல்லை; சரத்து 76(1)-ன் கீழ் குடியரசுத் தலைவர் புதிய ஒருவரை நியமிக்க வேண்டும், இடைக்காலத்தில் சொலிசிட்டர் ஜெனரல் அவசர அரசு வழக்குகளை நடத்துவார்"),
            ("The Chief Justice of India assumes the duties", "தலைமை நீதிபதி அப்பணிகளை ஏற்றுக்கொள்வார்"),
            ("The seniormost High Court judge is appointed", "மூத்த உயர்நீதிமன்ற நீதிபதி நியமிக்கப்படுவார்")
        ],
        "correct_idx": 1,
        "exp_en": "Article 76 does not provide for an 'Acting Attorney General'. In the event of death or sudden vacancy, the President appoints a new AG under Article 76(1). In the interim, the Solicitor General leads the government legal team.",
        "exp_ta": "சரத்து 76-ல் 'பொறுப்பு தலைமை வழக்கறிஞர்' என்ற பதவி எதுவும் இல்லை. மரணம் அல்லது திடீர் காலியிடம் ஏற்பட்டால் குடியரசுத் தலைவர் சரத்து 76(1)-ன் கீழ் புதிய AG-யை நியமிப்பார்; அதுவரை சொலிசிட்டர் ஜெனரல் பணிகளை நடத்துவார்.",
        "tip": "High-yield trap: There is NO 'Acting AG' in the Constitution.",
        "fact": "Unlike Article 126 (Acting Chief Justice) or Article 223, Article 76 has no acting provision."
    },
    # 41
    {
        "stem_en": "Which of the following constitutional provisions prevents the Attorney General from being sued for defamation for remarks made during Parliamentary debate?",
        "stem_ta": "நாடாளுமன்ற விவாதத்தின் போது தெரிவித்த கருத்துக்களுக்காக தலைமை வழக்கறிஞர் மீது அவதூறு வழக்கு தொடரப்படுவதை தடுக்கும் அரசியலமைப்பு சரத்து எது?",
        "options": [
            ("Article 76(3)", "சரத்து 76(3)"),
            ("Article 105(2) read with Article 105(4)", "சரத்து 105(4)-டன் இணைந்த சரத்து 105(2)"),
            ("Article 143", "சரத்து 143"),
            ("Article 300", "சரத்து 300")
        ],
        "correct_idx": 1,
        "exp_en": "Article 105(2) grants absolute immunity for anything said in Parliament, and Article 105(4) explicitly extends this immunity to persons who have the right to speak under Article 88, including the Attorney General.",
        "exp_ta": "சரத்து 105(2) நாடாளுமன்றத்தில் பேசியதற்கு முழுமையான நீதிமன்ற பாதுகாப்பை வழங்குகிறது; சரத்து 105(4) இந்நீதிமன்ற விலக்கு உரிமையை பேச உரிமை பெற்றுள்ள தலைமை வழக்கறிஞருக்கும் நீட்டிக்கிறது.",
        "tip": "Article 105(2) + 105(4) = Absolute immunity from judicial proceedings for parliamentary speeches.",
        "fact": "This immunity is absolute and cannot be challenged even on grounds of malice."
    },
    # 42
    {
        "stem_en": "Can the Attorney General of India be appointed to a Commission of Inquiry constituted under the Commissions of Inquiry Act 1952?",
        "stem_ta": "1952 விசாரணை ஆணையச் சட்டத்தின் கீழ் அமைக்கப்படும் விசாரணை ஆணையத்தில் தலைமை வழக்கறிஞர் நியமிக்கப்பட முடியுமா?",
        "options": [
            ("No, constitutional officers cannot serve on statutory inquiry commissions", "இல்லை, அரசியலமைப்பு அதிகாரிகள் விசாரணை ஆணையங்களில் பணியாற்ற முடியாது"),
            ("Yes, the Government may appoint the Attorney General or request his assistance as counsel to the Commission", "ஆம், அரசு தலைமை வழக்கறிஞரை ஆணையத்தின் தலைவராகவோ அல்லது ஆணையத்திற்கு உதவும் முதன்மை வழக்கறிஞராகவோ நியமிக்க முடியும்"),
            ("Only if retired judges are unavailable", "ஓய்வுபெற்ற நீதிபதிகள் கிடைக்காத போது மட்டுமே"),
            ("Only with the consent of the Chief Election Commissioner", "தலைமை தேர்தல் ஆணையரின் ஒப்புதலுடன் மட்டுமே")
        ],
        "correct_idx": 1,
        "exp_en": "There is no constitutional bar. The Attorney General or other law officers frequently assist major Commissions of Inquiry as Senior Counsel to lead evidence and present findings.",
        "exp_ta": "அரசியலமைப்பு தடை எதுவும் இல்லை. முக்கிய விசாரணை ஆணையங்களில் ஆதாரங்களை சமர்ப்பிக்கவும் உதவவும் மூத்த வழக்கறிஞராக தலைமை வழக்கறிஞர் அல்லது சட்ட அதிகாரிகளை அரசு நியமிக்கலாம்.",
        "tip": "M.C. Setalvad assisted multiple historical commissions of inquiry.",
        "fact": "The Attorney General can also be requested to assist parliamentary committees."
    },
    # 43
    {
        "stem_en": "Under Article 76, can an Attorney General of India simultaneously hold an elected political office, such as Mayor of a Municipal Corporation or Member of a Legislative Assembly?",
        "stem_ta": "சரத்து 76-ன் கீழ், இந்திய தலைமை வழக்கறிஞர் ஒரே நேரத்தில் மேயர் அல்லது சட்டமன்ற உறுப்பினர் (MLA) போன்ற தேர்ந்தெடுக்கப்பட்ட அரசியல் பதவிகளை வகிக்க முடியுமா?",
        "options": [
            ("Yes, dual offices are permitted", "ஆம், இரட்டைப் பதவிகள் அனுமதிக்கப்படுகின்றன"),
            ("No, by constitutional incompatibility, office of profit rules, and professional ethics, holding an elected legislative/civic office is incompatible with serving as AG", "இல்லை, அரசியலமைப்பு பொருத்தமின்மை, ஆதாயம் தரும் பதவி விதிகள் மற்றும் தொழில்முறை நெறிமுறைகளின்படி தேர்ந்தெடுக்கப்பட்ட மக்கள் பிரதிநிதி பதவியை வகிக்க முடியாது"),
            ("Only with Prime Minister's special permission", "பிரதமரின் சிறப்பு அனுமதியுடன் மட்டுமே"),
            ("Only in Union Territories", "யூனியன் பிரதேசங்களில் மட்டுமே")
        ],
        "correct_idx": 1,
        "exp_en": "Under office of profit provisions (Article 102 and 191) and the Bar Council of India rules, a practicing advocate holding the full-time constitutional post of Attorney General cannot simultaneously serve as an elected MLA, MP, or Mayor.",
        "exp_ta": "ஆதாயம் தரும் பதவி விதிகள் (சரத்து 102 மற்றும் 191) மற்றும் பார் கவுன்சில் விதிகளின் கீழ், தலைமை வழக்கறிஞராக இருப்பவர் ஒரே நேரத்தில் தேர்ந்தெடுக்கப்பட்ட சட்டமன்ற உறுப்பினர் அல்லது மேயர் பதவியை வகிக்க முடியாது.",
        "tip": "Separation of law officer duties from partisan elected offices.",
        "fact": "If an MP or MLA is appointed AG, he must resign his legislative seat."
    },
    # 44
    {
        "stem_en": "Who was the Attorney General of India when the Supreme Court delivered the historic Right to Privacy judgment (K.S. Puttaswamy v. UOI) in August 2017?",
        "stem_ta": "2017 ஆகஸ்டில் உச்ச நீதிமன்றம் வரலாற்று சிறப்புமிக்க தனிநபர் அந்தரங்க உரிமைத் தீர்ப்பை (புட்டசுவாமி வழக்கு) வழங்கிய போது இந்திய தலைமை வழக்கறிஞராக இருந்தவர் யார்?",
        "options": [
            ("Mukul Rohatgi", "முகுல் ரோஹத்கி"),
            ("K.K. Venugopal", "கே.கே. வேணுகோபால்"),
            ("R. Venkataramani", "ஆர். வெங்கடரமணி"),
            ("G.E. Vahanvati", "ஜி.இ. வாகனவதி")
        ],
        "correct_idx": 1,
        "exp_en": "K.K. Venugopal, who assumed office as the 15th Attorney General on 3 July 2017, represented the Union of India before the 9-judge Constitution Bench which delivered the unanimous Privacy verdict on 24 August 2017.",
        "exp_ta": "2017 ஜூலை 3 அன்று 15-வது தலைமை வழக்கறிஞராக பொறுப்பேற்ற கே.கே. வேணுகோபால், 2017 ஆகஸ்ட் 24 அன்று ஒருமனதாக தீர்ப்பளிக்கப்பட்ட 9 நீதிபதிகள் கொண்ட அந்தரங்க உரிமை அமர்வில் மத்திய அரசுக்காக ஆஜரானார்.",
        "tip": "Mukul Rohatgi had argued the preliminary hearings prior to July 2017; K.K. Venugopal argued the final 9-judge bench reference.",
        "fact": "The Court held that Privacy is an intrinsic part of Article 21 and Part III."
    },
    # 45
    {
        "stem_en": "Can the Attorney General of India be appointed as an arbitrator in an international commercial arbitration between two private foreign entities?",
        "stem_ta": "இரு வெளிநாட்டு தனியார் நிறுவனங்களுக்கு இடையிலான சர்வதேச வணிக நடுவர் மன்றத்தில் தலைமை வழக்கறிஞர் நடுவராக (Arbitrator) நியமிக்கப்பட முடியுமா?",
        "options": [
            ("No, he can never act as arbitrator", "இல்லை, நடுவராக ஒருபோதும் செயல்பட முடியாது"),
            ("Yes, subject to obtaining prior permission of the Government of India and ensuring that no conflict of interest exists with the Union", "ஆம், இந்திய அரசாங்கத்தின் முன்அனுமதியைப் பெற்று மற்றும் மத்திய அரசின் நலன்களுக்கு முரண்பாடு இல்லை என்பதை உறுதிசெய்து நியமிக்கப்படலாம்"),
            ("Only if appointed by the International Court of Justice", "சர்வதேச நீதிமன்றத்தால் நியமிக்கப்பட்டால் மட்டுமே"),
            ("Only in maritime shipping disputes", "கடல்சார் கப்பல் போக்குவரத்து வழக்குகளில் மட்டுமே")
        ],
        "correct_idx": 1,
        "exp_en": "Under Rule 8 of Law Officers Rules, with the permission of the Government of India, the Attorney General can act as an arbitrator in commercial disputes, provided the Union of India has no adverse interest in the subject matter.",
        "exp_ta": "சட்ட அதிகாரிகள் விதி 8-ன் கீழ், இந்திய அரசின் முன்அனுமதியைப் பெற்று, மத்திய அரசின் நலன்களுக்கு முரண்படாத வணிக வழக்குகளில் நடுவராக (Arbitrator) செயல்பட தலைமை வழக்கறிஞருக்கு அனுமதி உண்டு.",
        "tip": "Permission from the Ministry of Law and Justice is mandatory.",
        "fact": "Arbitration proceedings must not interfere with his primary duties to the Supreme Court."
    },
    # 46
    {
        "stem_en": "What is the historical origin of the rule that the Attorney General of India has precedence over all other advocates at the Bar?",
        "stem_ta": "பார் கவுன்சிலில் உள்ள பிற அனைத்து வழக்கறிஞர்களையும் விட இந்திய தலைமை வழக்கறிஞருக்கு முதலிட முன்னுரிமை உண்டு என்ற விதியின் வரலாற்று பின்னணி என்ன?",
        "options": [
            ("Originates from ancient Roman Law", "பண்டைய ரோமானிய சட்டத்திலிருந்து தோன்றியது"),
            ("Inherited from the English Common Law tradition where the King's Attorney General enjoys pre-audience as leader of the Bar, codified in Section 23 of the Advocates Act 1961", "ஆங்கில பொதுச் சட்ட மரபில் மன்னரின் தலைமை வழக்கறிஞர் பெற்றிருந்த 'முன்னுரிமை' (Pre-audience) மரபிலிருந்து பெறப்பட்டு, 1961 வழக்கறிஞர்கள் சட்டத்தின் பிரிவு 23-ல் சட்டப்பூர்வமாக்கப்பட்டது"),
            ("Invented by the First Law Commission in 1955", "1955-ல் முதல் சட்ட ஆணையத்தால் புதிதாக உருவாக்கப்பட்டது"),
            ("Derived from the French Civil Code", "பிரெஞ்சு சிவில் சட்டத்திலிருந்து பெறப்பட்டது")
        ],
        "correct_idx": 1,
        "exp_en": "In English Common Law, the Attorney-General was the King's representative in court and was granted pre-audience over all serjeants-at-law and barristers. Independent India codified this historical tradition in Section 23(1) of the Advocates Act 1961.",
        "exp_ta": "ஆங்கிலேயர் ஆட்சிக் காலத்தில் மன்னரின் பிரதிநிதியான அட்டர்னி ஜெனரலுக்கு நீதிமன்றத்தில் வழங்கப்பட்ட முதலிட முன்னுரிமை மரபே, சுதந்திர இந்தியாவில் 1961 வழக்கறிஞர்கள் சட்டத்தின் பிரிவு 23(1)-ன் கீழ் சட்டப்பூர்வமாக்கப்பட்டது.",
        "tip": "Pre-audience means the right to be heard before other advocates.",
        "fact": "Section 23 establishes the order of pre-audience across all courts and tribunals."
    },
    # 47
    {
        "stem_en": "In the landmark Sub-Judice convention debate in Parliament, what has been the consistent advice of Attorneys General regarding parliamentary discussion of cases pending in courts?",
        "stem_ta": "நீதிமன்றங்களில் நிலுவையிலுள்ள வழக்குகள் (Sub-Judice) குறித்து நாடாளுமன்றத்தில் விவாதிப்பது தொடர்பாக தலைமை வழக்கறிஞர்கள் தொடர்ந்து வழங்கி வந்துள்ள ஆலோசனை என்ன?",
        "options": [
            ("Parliament can freely retry any criminal case", "நாடாளுமன்றம் எந்த வழக்கையும் சுதந்திரமாக மறுவிசாரணை செய்யலாம்"),
            ("While Parliament has sovereign freedom of speech under Article 105, it self-imposes the Sub-Judice rule to avoid prejudicing fair judicial trials and maintain constitutional comity", "சரத்து 105-ன் கீழ் நாடாளுமன்றத்திற்கு முழு பேச்சு சுதந்திரம் இருந்தாலும், நீதிமன்ற விசாரணையின் நேர்மையைப் பாதுகாக்கவும் அரசியலமைப்பு கண்ணியத்தை நிலைநிறுத்தவும் நீதிமன்ற வழக்குகளை விவாதிப்பதில் நாடாளுமன்றமே சுயமாக கட்டுப்பாடு (Sub-Judice) விதித்துக்கொள்கிறது"),
            ("Courts can issue injunctions to stop parliamentary debates", "நாடாளுமன்ற விவாதங்களை நிறுத்த நீதிமன்றங்கள் தடை உத்தரவு பிறப்பிக்கலாம்"),
            ("Sub-judice rule has no application in India", "இந்தியாவில் சப்-ஜூடிஸ் விதியே கிடையாது")
        ],
        "correct_idx": 1,
        "exp_en": "Attorneys General have consistently advised that the sub-judice rule is a voluntary parliamentary self-restraint under House Rules (e.g., Rule 352 of Lok Sabha Rules) to ensure court proceedings are not prejudiced, maintaining institutional balance.",
        "exp_ta": "நீதிமன்ற விசாரணையை பாதிக்காமல் இருக்கவும் நிறுவனங்களுக்கிடையிலான சமநிலையைப் பேணவும், நிலுவை வழக்குகள் குறித்து விவாதிக்காமல் இருக்க நாடாளுமன்றமே தனது விதிகளின் கீழ் (Rule 352) சுயமாக கட்டுப்பாடு விதித்துக்கொள்கிறது என்று AG-க்கள் அறிவுறுத்தியுள்ளனர்.",
        "tip": "Parliamentary rules bar discussion on matters under adjudication by a court of law.",
        "fact": "The Speaker enforces the sub-judice convention on a case-by-case basis."
    },
    # 48
    {
        "stem_en": "Who was the Attorney General of India when the Supreme Court delivered the historic judgment in the Article 370 revocation challenge in December 2023?",
        "stem_ta": "2023 டிசம்பரில் சரத்து 370 ரத்து செய்யப்பட்டதை எதிர்த்த வழக்கில் உச்ச நீதிமன்றம் தீர்ப்பளித்த போது இந்திய தலைமை வழக்கறிஞராக இருந்தவர் யார்?",
        "options": [
            ("K.K. Venugopal", "கே.கே. வேணுகோபால்"),
            ("R. Venkataramani (along with Solicitor General Tushar Mehta)", "ஆர். வெங்கடரமணி (சொலிசிட்டர் ஜெனரல் துஷார் மேத்தாவுடன் இணைந்து)"),
            ("Mukul Rohatgi", "முகுல் ரோஹத்கி"),
            ("Soli Sorabjee", "சோலி சோராப்ஜி")
        ],
        "correct_idx": 1,
        "exp_en": "Attorney General R. Venkataramani, alongside Solicitor General Tushar Mehta, led the Union of India's arguments before the 5-judge Constitution Bench headed by CJI D.Y. Chandrachud, which unanimously upheld the revocation of Article 370 on 11 December 2023.",
        "exp_ta": "2023 டிசம்பர் 11 அன்று சரத்து 370 நீக்கத்தை உச்ச நீதிமன்றம் ஒருமனதாக உறுதி செய்த வழக்கில், மத்திய அரசுக்காக தலைமை வழக்கறிஞர் ஆர். வெங்கடரமணி மற்றும் சொலிசிட்டர் ஜெனரல் துஷார் மேத்தா ஆகியோர் முன்னின்று வாதாடினர்.",
        "tip": "The 5-judge bench held that Article 370 was a temporary, transitional provision.",
        "fact": "The Court directed that assembly elections in Jammu & Kashmir be held by September 2024."
    },
    # 49
    {
        "stem_en": "Can the Attorney General of India give a legal opinion directly to the Chief Justice of India or the Supreme Court Registry on administrative matters?",
        "stem_ta": "நிர்வாக விவகாரங்களில் இந்திய தலைமை நீதிபதிக்கோ அல்லது உச்ச நீதிமன்ற பதிவாளருக்கோ தலைமை வழக்கறிஞர் நேரடியாக சட்ட ஆலோசனை வழங்க முடியுமா?",
        "options": [
            ("Yes, the CJI is his administrative head", "ஆம், தலைமை நீதிபதியே அவரது நிர்வாகத் தலைவர்"),
            ("No, the Attorney General is the counsel for the Executive (Government of India); the Supreme Court has its own independent administrative apparatus and legal officers", "இல்லை, தலைமை வழக்கறிஞர் மத்திய நிர்வாகத்தின் (அரசாங்கத்தின்) வழக்கறிஞர் ஆவார்; உச்ச நீதிமன்றத்திற்கு சொந்த சுயாதீன நிர்வாக அமைப்புகளும் சட்டப் பிரிவுகளும் உள்ளன"),
            ("Only in matters concerning judicial pensions", "நீதிபதிகள் ஓய்வூதியம் தொடர்பான விவகாரங்களில் மட்டுமே"),
            ("Only if directed by the President under Article 143", "சரத்து 143-ன் கீழ் குடியரசுத் தலைவர் உத்தரவிட்டால் மட்டுமே")
        ],
        "correct_idx": 1,
        "exp_en": "Under the doctrine of separation of powers, the Attorney General is an integral part of the Union Executive under Part V, Chapter I. The Supreme Court operates under Chapter IV as an independent judiciary and does not take administrative advice from the AG.",
        "exp_ta": "அதிகாரப் பகிர்வு கோட்பாட்டின் கீழ், தலைமை வழக்கறிஞர் மத்திய நிர்வாகத்தின் அங்கமாவார். உச்ச நீதிமன்றம் பகுதி V அத்தியாயம் IV-ன் கீழ் செயல்படும் சுயாதீன நீதித்துறை என்பதால், அது AG-யிடம் நிர்வாக ஆலோசனை பெறுவதில்லை.",
        "tip": "Preserves institutional separation between Executive Counsel and the Judiciary.",
        "fact": "The Supreme Court appoints its own amicus curiae or standing counsels for administrative litigation."
    },
    # 50
    {
        "stem_en": "Under Article 76, if a person appointed as the Attorney General is subsequently discovered to have lacked the mandatory 10-year High Court advocate qualification at the time of appointment, what is the constitutional validity of the official acts performed by him?",
        "stem_ta": "சரத்து 76-ன் கீழ், நியமிக்கப்பட்ட ஒரு தலைமை வழக்கறிஞர் நியமனத்தின் போது கட்டாய 10 ஆண்டு வழக்கறிஞர் தகுதியைக் கொண்டிருக்கவில்லை என்பது பின்னர் தெரியவந்தால், அவர் ஆற்றிய அதிகாரப்பூர்வ பணிகளின் செல்லுபடியாகும் தன்மை என்ன?",
        "options": [
            ("All his previous appearances and legal opinions are automatically declared void ab initio", "அவரது முந்தைய அனைத்து வாதங்களும் ஆலோசனைகளும் தொடக்கத்திலிருந்தே செல்லாது என அறிவிக்கப்படும்"),
            ("Under the 'De Facto Doctrine', his official acts and opinions remain valid and binding to protect public interest, though he can be removed via a writ of Quo Warranto", "டி ஃபேக்டோ கோட்பாட்டின் (De Facto Doctrine) கீழ், அவரது முந்தைய அதிகாரப்பூர்வ பணிகளும் ஆலோசனைகளும் பொது நலனைக் காக்க செல்லுபடியாகும்; ஆனால் கோ வாரண்டோ (Quo Warranto) நீதிப்பேராணை மூலம் அவரை பதவியிலிருந்து நீக்கலாம்"),
            ("The Government of India is fined by the Supreme Court", "இந்திய அரசுக்கு உச்ச நீதிமன்றம் அபராதம் விதிக்கும்"),
            ("Parliament must ratify each of his previous opinions", "நாடாளுமன்றம் அவரது முந்தைய ஒவ்வொரு கருத்தையும் அங்கீகரிக்க வேண்டும்")
        ],
        "correct_idx": 1,
        "exp_en": "Under the well-settled 'De Facto Doctrine' (reaffirmed in Gokaraju Rangaraju v. State of AP, 1981), the official acts performed by a de facto constitutional officer before his appointment is declared defective are treated as valid to prevent public chaos, though his title to office can be ousted via Quo Warranto.",
        "exp_ta": "கோகராஜு ரங்கராஜு வழக்கில் (1981) உறுதிப்படுத்தப்பட்ட 'டி ஃபேக்டோ கோட்பாட்டின்' கீழ், நியமனக் குறைபாடு வெளிப்படுவதற்கு முன் அவரால் ஆற்றிய அரசுப் பணிகள் பொது நலன் கருதி செல்லுபடியாகும்; ஆனால் கோ வாரண்டோ (Quo Warranto) பேராணை மூலம் அவரை பதவியிலிருந்து நீக்க முடியும்.",
        "tip": "De Facto doctrine protects administrative and judicial certainty from collapsing retrospectively.",
        "fact": "A writ of Quo Warranto challenges the legal title of a person holding a public constitutional office."
    }
]

def build_ag_hard():
    questions = []
    for i, item in enumerate(raw_hard_data):
        qid = f"AG_H_{i+1:03d}"
        opts = item["options"]
        correct_idx = item["correct_idx"]
        correct_key = ["A", "B", "C", "D"][correct_idx]
        
        why_en = {}
        why_ta = {}
        for idx, key in enumerate(["A", "B", "C", "D"]):
            if idx == correct_idx:
                why_en[key] = f"Option {key} is the correct legal and constitutional position based on Supreme Court precedents and statutory rules."
                why_ta[key] = f"உச்ச நீதிமன்ற தீர்ப்புகள் மற்றும் சட்ட விதிகளின்படி தெரிவு {key} சரியான சட்டப்பூர்வ நிலையாகும்."
            else:
                why_en[key] = f"Option {key} ({opts[idx][0]}) is incorrect."
                why_ta[key] = f"தெரிவு {key} ({opts[idx][1]}) தவறானது."
                
        q = make_ag_q(
            qid=qid,
            diff="Hard",
            qtype="Single Choice",
            subtopic="Jurisprudence & Case Laws on Attorney General",
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
            tip_en=item["tip"],
            tip_ta=f"நினைவில் கொள்க: {item['tip']}",
            fact_en=item["fact"],
            fact_ta=f"முக்கிய தகவல்: {item['fact']}",
            tags=["polity", "attorney_general_of_india", "hard"]
        )
        questions.append(q)
    return questions

def main():
    questions = build_ag_hard()
    print(f"Generated {len(questions)} raw Hard questions.")
    
    # Balance keys to 13 B, 12 C, 12 D, 13 A
    balanced = balance_question_keys(questions, {"A": 13, "B": 13, "C": 12, "D": 12})
    
    out_dir = "data/questions/polity"
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "attorney_general_hard.json")
    
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(balanced, f, indent=2, ensure_ascii=False)
        
    print(f"Saved balanced Hard MCQs to {out_file}")
    
    validator = ContentValidator()
    report = validator.validate_file(out_file, expected_count=50, expected_prefix="AG_H_")
    print(f"Validation Report: {'PASS' if report.is_valid else 'FAIL'} | Total: {report.total_audited}")
    print(f"Key Distribution: {report.key_distribution}")
    if not report.is_valid:
        for iss in report.issues:
            print("Issue:", iss.message)

if __name__ == "__main__":
    main()
