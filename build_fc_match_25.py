# -*- coding: utf-8 -*-
"""
Build 25 Match the Following MCQs for Finance Commission of India
ID range: FC_MF_001 to FC_MF_025
Target key balance: 7 A, 6 B, 6 C, 6 D
"""

import json
import os
import shutil
from fc_mcq_helper import make_fc_q
from tools.nova_content_engine.validator import ContentValidator

raw_match_data = [
    # 1
    {
        "subtopic": "Constitutional Articles",
        "intro_en": "Match List-I (Constitutional Articles) with List-II (Subject Matter in Federal Finance) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (அரசியலமைப்புச் சரத்துகள்) பட்டியல்-II உடன் (கூட்டாட்சி நிதி தொடர்பான பொருள்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": ["Article 280", "Article 281", "Article 275", "Article 270"],
        "list1_ta": ["சரத்து 280", "சரத்து 281", "சரத்து 275", "சரத்து 270"],
        "list2_en": [
            "Constitution and functions of the Finance Commission",
            "Laying of recommendations with explanatory memorandum before Parliament",
            "Statutory grants-in-aid of revenues to deficit States",
            "Distribution of net proceeds of taxes between Union and States"
        ],
        "list2_ta": [
            "நிதி ஆணையத்தின் அமைப்பு மற்றும் பணிகள்",
            "விளக்கக் குறிப்புடன் பரிந்துரைகளை நாடாளுமன்றத்தில் சமர்ப்பித்தல்",
            "பற்றாக்குறை மாநிலங்களுக்கு வருவாய்க்கான சட்டப்பூர்வ மானியங்கள்",
            "மத்திய மற்றும் மாநிலங்களுக்கு இடையே வரிகளின் நிகர வருவாயைப் பகிர்ந்தளித்தல்"
        ],
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "Article 280 provides for the Finance Commission; Article 281 deals with tabling its report; Article 275 governs grants-in-aid; Article 270 covers the sharing of divisible taxes.",
        "exp_ta": "சரத்து 280 நிதி ஆணையத்தை அமைக்கிறது; சரத்து 281 அறிக்கையை நாடாளுமன்றத்தில் வைப்பதை நிர்வகிக்கிறது; சரத்து 275 மானியங்களை வழங்குகிறது; சரத்து 270 வரிகளைப் பகிர்ந்தளிக்கிறது.",
        "tip_en": "Article 280: Setup; 281: Tabling; 275: Grants; 270: Divisible pool.",
        "tip_ta": "சரத்து 280: அமைப்பு; 281: சமர்ப்பித்தல்; 275: மானியங்கள்; 270: பகிர்வு நிதி.",
        "fact_en": "Articles 268 to 281 in Part XII govern the financial relations between Union and States.",
        "fact_ta": "பகுதி XII-ல் உள்ள சரத்துகள் 268 முதல் 281 வரை மத்திய-மாநில நிதி உறவுகளை நிர்வகிக்கின்றன."
    },
    # 2
    {
        "subtopic": "Sections of Finance Commission Act 1951",
        "intro_en": "Match List-I (Sections of Finance Commission Act 1951) with List-II (Statutory Provisions) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (1951 நிதி ஆணையச் சட்டப் பிரிவுகள்) பட்டியல்-II உடன் (சட்டப்பூர்வ விதிகள்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": ["Section 3", "Section 4", "Section 5", "Section 8"],
        "list1_ta": ["பிரிவு 3", "பிரிவு 4", "பிரிவு 5", "பிரிவு 8"],
        "list2_en": [
            "Composition: Chairman and four other members",
            "Qualifications for appointment as Chairman and members",
            "Disqualifications for membership of the Commission",
            "Powers of the Commission equivalent to a Civil Court"
        ],
        "list2_ta": [
            "கட்டமைப்பு: தலைவர் மற்றும் நான்கு உறுப்பினர்கள்",
            "தலைவர் மற்றும் உறுப்பினர்களுக்கான நியமனத் தகுதிகள்",
            "ஆணைய உறுப்பினர் பதவிகளுக்கான தகுதியிழப்புகள்",
            "சிவில் நீதிமன்றத்திற்கு இணையான ஆணையத்தின் அதிகாரங்கள்"
        ],
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "Section 3 defines composition; Section 4 specifies qualifications; Section 5 lists disqualifications; Section 8 confers Civil Court powers.",
        "exp_ta": "பிரிவு 3 அமைப்பைக் கூறுகிறது; பிரிவு 4 தகுதிகளைக் குறிப்பிடுகிறது; பிரிவு 5 தகுதியிழப்புகளைப் பட்டியலிடுகிறது; பிரிவு 8 சிவில் நீதிமன்ற அதிகாரங்களை வழங்குகிறது.",
        "tip_en": "FC Act 1951 was enacted under Article 280(2) of the Constitution.",
        "tip_ta": "1951 நிதி ஆணையச் சட்டம் அரசியலமைப்பின் சரத்து 280(2)-ன் கீழ் இயற்றப்பட்டது.",
        "fact_en": "The Act was amended in 1955 to refine disqualification rules.",
        "fact_ta": "தகுதியிழப்பு விதிகளை செம்மைப்படுத்த இச்சட்டம் 1955-ல் திருத்தப்பட்டது."
    },
    # 3
    {
        "subtopic": "Landmark Chairmen & Commission Numbers",
        "intro_en": "Match List-I (Finance Commission Number) with List-II (Distinguished Chairman) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (நிதி ஆணையத்தின் எண்) பட்டியல்-II உடன் (புகழ்பெற்ற தலைவர்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": ["First Finance Commission", "Twelfth Finance Commission", "Fourteenth Finance Commission", "Fifteenth Finance Commission"],
        "list1_ta": ["முதலாவது நிதி ஆணையம்", "பன்னிரண்டாவது நிதி ஆணையம்", "பதினான்காவது நிதி ஆணையம்", "பதினைந்தாவது நிதி ஆணையம்"],
        "list2_en": ["K.C. Neogy", "Dr. C. Rangarajan", "Dr. Y.V. Reddy", "N.K. Singh"],
        "list2_ta": ["கே.சி. நியோகி", "டாக்டர் சி. ரங்கராஜன்", "டாக்டர் ஒய்.வி. ரெட்டி", "என்.கே. சிங்"],
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "1st FC: K.C. Neogy (1951); 12th FC: C. Rangarajan (2002); 14th FC: Y.V. Reddy (2013); 15th FC: N.K. Singh (2017).",
        "exp_ta": "1வது: கே.சி. நியோகி (1951); 12வது: சி. ரங்கராஜன் (2002); 14வது: ஒய்.வி. ரெட்டி (2013); 15வது: என்.கே. சிங் (2017).",
        "tip_en": "Neogy was first; Rangarajan (12th), Reddy (14th), N.K. Singh (15th).",
        "tip_ta": "நியோகி முதலாவது; ரங்கராஜன் (12வது), ரெட்டி (14வது), என்.கே. சிங் (15வது).",
        "fact_en": "All these four Commissions introduced paradigm shifts in Indian fiscal transfers.",
        "fact_ta": "இந்த நான்கு ஆணையங்களும் இந்திய நிதிப் பகிர்வில் வரலாற்று மாற்றங்களை ஏற்படுத்தின."
    },
    # 4
    {
        "subtopic": "15th FC Horizontal Devolution Criteria & Weights",
        "intro_en": "Match List-I (Devolution Criterion - 15th FC) with List-II (Assigned Weight) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (15வது நிதி ஆணையப் பகிர்வு அளவுகோல்) பட்டியல்-II உடன் (ஒதுக்கப்பட்ட எடை) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": ["Income Distance", "Population (2011 Census)", "Demographic Performance", "Tax and Fiscal Effort"],
        "list1_ta": ["வருமான இடைவெளி", "மக்கள் தொகை (2011 கணக்கெடுப்பு)", "மக்கள்தொகை செயல்திறன்", "வரி மற்றும் நிதி முயற்சி"],
        "list2_en": ["45.0%", "15.0%", "12.5%", "2.5%"],
        "list2_ta": ["45.0%", "15.0%", "12.5%", "2.5%"],
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "15th FC weights: Income Distance 45%, Population 15%, Demographic Performance 12.5%, Tax Effort 2.5% (plus Area 15%, Forest & Ecology 10%).",
        "exp_ta": "15வது நிதி ஆணைய எடைகள்: வருமான இடைவெளி 45%, மக்கள் தொகை 15%, மக்கள்தொகை செயல்திறன் 12.5%, வரி முயற்சி 2.5% (பரப்பளவு 15%, வனம் & சூழலியல் 10%).",
        "tip_en": "Income Distance has the highest weight (45%); Tax Effort has the lowest (2.5%).",
        "tip_ta": "வருமான இடைவெளி அதிகபட்ச எடையையும் (45%), வரி முயற்சி குறைந்தபட்ச எடையையும் (2.5%) பெற்றுள்ளன.",
        "fact_en": "Total horizontal devolution formula adds up to exactly 100%.",
        "fact_ta": "கிடைமட்ட வரிப் பகிர்வு சூத்திரத்தின் மொத்த கூடுதல் சரியாக 100% ஆகும்."
    },
    # 5
    {
        "subtopic": "Landmark Devolution Percentage Milestones",
        "intro_en": "Match List-I (Commission Milestone) with List-II (Devolution Recommendation) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (ஆணைய மைல்கல்) பட்டியல்-II உடன் (வரிப் பகிர்வுப் பரிந்துரை) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": [
            "First Finance Commission",
            "Seventh Finance Commission",
            "Tenth Finance Commission",
            "Fourteenth Finance Commission"
        ],
        "list1_ta": [
            "முதலாவது நிதி ஆணையம்",
            "ஏழாவது நிதி ஆணையம்",
            "பத்தாவது நிதி ஆணையம்",
            "பதினான்காவது நிதி ஆணையம்"
        ],
        "list2_en": [
            "55% share of net Income Tax to States",
            "Doubled Union Excise Duty share to 40%",
            "Proposed Alternative Devolution of 29% across all taxes",
            "Historic untied tax devolution leap to 42%"
        ],
        "list2_ta": [
            "மாநிலங்களுக்கு 55% நிகர வருமான வரிப் பகிர்வு",
            "மத்திய கலால் வரிப் பங்கை 40% ஆக இரட்டிப்பாக்கியது",
            "அனைத்து வரிகளிலும் 29% மாற்று வரிப் பகிர்வை முன்மொழிந்தது",
            "நிபந்தனையற்ற வரிப் பகிர்வை வரலாற்றுச் சிறப்புமிக்க 42% ஆக உயர்த்தியது"
        ],
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "1st FC gave 55% Income Tax; 7th FC doubled Excise to 40%; 10th FC proposed 29% Alternative Scheme; 14th FC gave 42% untied share.",
        "exp_ta": "1வது ஆணையம் 55% வருமான வரியை அளித்தது; 7வது கலால் வரியை 40% ஆக்கியது; 10வது 29% மாற்றுத் திட்டத்தை தந்தது; 14வது 42% பங்கை வழங்கியது.",
        "tip_en": "14th FC's 42% remains the peak vertical devolution percentage in Indian history.",
        "tip_ta": "14வது ஆணையத்தின் 42% இந்திய வரலாற்றின் மிக உயர்ந்த செங்குத்து வரிப் பகிர்வாகும்.",
        "fact_en": "15th FC adjusted 42% to 41% due to the newly created UTs of J&K and Ladakh.",
        "fact_ta": "ஜம்மு காஷ்மீர் மற்றும் லடாக் யூனியன் பிரதேசங்களுக்காக 15வது ஆணையம் 42%-ஐ 41% ஆக மாற்றியது."
    },
    # 6
    {
        "subtopic": "State Finance Commission Constitutional Linkage",
        "intro_en": "Match List-I (Constitutional Provisions) with List-II (Institutional Mandate) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (அரசியலமைப்பு விதிகள்) பட்டியல்-II உடன் (நிறுவன பணி) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": ["Article 243-I", "Article 243-Y", "Article 280(3)(bb)", "Article 280(3)(c)"],
        "list1_ta": ["சரத்து 243-I", "சரத்து 243-Y", "சரத்து 280(3)(bb)", "சரத்து 280(3)(c)"],
        "list2_en": [
            "Constitution of State Finance Commission for Panchayats by Governor",
            "State Finance Commission review of Municipal finances",
            "Central FC recommendations to augment State Consolidated Fund for Panchayats",
            "Central FC recommendations to augment State Consolidated Fund for Municipalities"
        ],
        "list2_ta": [
            "ஆளுநரால் பஞ்சாயத்துகளுக்காக மாநில நிதி ஆணையம் அமைக்கப்படுதல்",
            "நகராட்சி நிதிகளை மாநில நிதி ஆணையம் மறுஆய்வு செய்தல்",
            "பஞ்சாயத்துகளுக்காக மாநிலத் திரட்டப்பட்ட நிதியை பெருக்க மத்திய FC பரிந்துரை",
            "நகராட்சிகளுக்காக மாநிலத் திரட்டப்பட்ட நிதியை பெருக்க மத்திய FC பரிந்துரை"
        ],
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "Article 243-I governs SFC for Panchayats; 243-Y for Municipalities; 280(3)(bb) mandates Central FC augmentation for Panchayats; 280(3)(c) for Municipalities.",
        "exp_ta": "சரத்து 243-I பஞ்சாயத்து நிதி ஆணையத்தை அமைக்கிறது; 243-Y நகராட்சிகளுக்கானது; 280(3)(bb) பஞ்சாயத்துகளுக்காக மாநில நிதியை பெருக்க மத்திய ஆணையத்திற்கு வழிகாட்டுகிறது; 280(3)(c) நகராட்சிகளுக்கானது.",
        "tip_en": "Sub-clauses (bb) and (c) connect State Finance Commission findings to Central transfers.",
        "tip_ta": "உட்பிரிவுகள் (bb) மற்றும் (c) மாநில நிதி ஆணையத்தின் கண்டுபிடிப்புகளை மத்திய நிதிப் பகிர்வுடன் இணைக்கின்றன.",
        "fact_en": "Inserted by the 73rd and 74th Constitutional Amendment Acts 1992.",
        "fact_ta": "1992-ன் 73 மற்றும் 74வது அரசியலமைப்புத் திருத்தச் சட்டங்கள் மூலம் இவை சேர்க்கப்பட்டன."
    },
    # 7
    {
        "subtopic": "Commissions & Prominent Policy Innovations",
        "intro_en": "Match List-I (Finance Commission) with List-II (Flagship Institutional Policy Innovation) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (நிதி ஆணையம்) பட்டியல்-II உடன் (முக்கிய நிறுவனக் கொள்கை கண்டுபிடிப்பு) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": [
            "Twelfth Finance Commission",
            "Thirteenth Finance Commission",
            "Fourteenth Finance Commission",
            "Fifteenth Finance Commission"
        ],
        "list1_ta": [
            "பன்னிரண்டாவது நிதி ஆணையம்",
            "பதின்மூன்றாவது நிதி ஆணையம்",
            "பதினான்காவது நிதி ஆணையம்",
            "பதினைந்தாவது நிதி ஆணையம்"
        ],
        "list2_en": [
            "Incentivized States to enact Fiscal Responsibility (FRBM) laws via debt relief",
            "Formulated design architecture and Grand Bargain compensation roadmap for GST",
            "Abolished discretion by ending Central plan-schemes grants, raising untied share",
            "Introduced performance grants for Million-Plus cities and Defence Modernisation Fund"
        ],
        "list2_ta": [
            "கடன் நிவாரணம் மூலம் மாநிலங்கள் FRBM சட்டங்களை இயற்ற ஊக்கமளித்தது",
            "ஜிஎஸ்டிக்கான கட்டமைப்பு மற்றும் இழப்பீட்டு வரைபடத்தை உருவாக்கியது",
            "திட்ட மானியங்களை ஒழித்து நிபந்தனையற்ற வரியை 42% ஆக உயர்த்தி தன்னாட்சி அளித்தது",
            "பத்து லட்சத்திற்கும் அதிகமான நகரங்களுக்கான செயல்திறன் மானியம் மற்றும் பாதுகாப்பு நிதியை அறிமுகப்படுத்தியது"
        ],
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "12th FC pioneered state FRBMs; 13th FC laid the groundwork for GST; 14th FC unlocked untied fiscal space (42%); 15th FC linked urban grants to air quality/water and created MFDIS.",
        "exp_ta": "12வது ஆணையம் மாநில FRBM-களை கொண்டுவந்தது; 13வது ஜிஎஸ்டிக்கு அடித்தளமிட்டது; 14வது நிபந்தனையற்ற 42% பகிர்வை தந்தது; 15வது நகர்ப்புற செயல்திறன் மானியங்கள் மற்றும் MFDIS-ஐ உருவாக்கியது.",
        "tip_en": "Each Commission leaves a signature macro-fiscal reform footprint.",
        "tip_ta": "ஒவ்வொரு ஆணையமும் ஒரு குறிப்பிட்ட பேரியல்-நிதி சீர்திருத்த முத்திரையைப் பதிக்கிறது.",
        "fact_en": "Vijay Kelkar (13th FC Chairman) is widely called the father of Indian GST design.",
        "fact_ta": "விஜய் கேல்கர் (13வது ஆணையத் தலைவர்) இந்திய ஜிஎஸ்டி வடிவமைப்பின் தந்தை என அழைக்கப்படுகிறார்."
    },
    # 8
    {
        "subtopic": "Types of Finance Commission Transfers",
        "intro_en": "Match List-I (Transfer Category) with List-II (Functional Purpose) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (பரிமாற்றப் பிரிவு) பட்டியல்-II உடன் (செயல்பாட்டு நோக்கம்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": [
            "Tax Devolution (Art 270)",
            "Revenue Deficit Grants (Art 275)",
            "Local Body Grants (Art 280(3)(bb))",
            "Disaster Management Grants"
        ],
        "list1_ta": [
            "வரிப் பகிர்வு (சரத்து 270)",
            "வருவாய்ப் பற்றாக்குறை மானியம் (சரத்து 275)",
            "உள்ளாட்சி மானியம் (சரத்து 280(3)(bb))",
            "பேரிடர் மேலாண்மை மானியம்"
        ],
        "list2_en": [
            "Unconditional constitutional share of central taxes for general budgetary autonomy",
            "Gap-filling assistance assessed normatively for post-devolution revenue shortfalls",
            "Tied and untied basic grants augmenting rural panchayats and municipal civic services",
            "Cost-shared transfers funding response, relief, and mitigation under SDRMF"
        ],
        "list2_ta": [
            "பொது பட்ஜெட் தன்னாட்சிக்காக மத்திய வரிகளில் நிபந்தனையற்ற அரசியலமைப்புப் பங்கு",
            "வரிப் பகிர்வுக்குப் பிந்தைய வருவாய் பற்றாக்குறையை ஈடுகட்ட வழங்கப்படும் உதவி",
            "ஊரக பஞ்சாயத்துகள் மற்றும் நகராட்சிகளின் அடிப்படை குடிமைப் பணிகளை பெருக்கும் மானியம்",
            "SDRMF-ன் கீழ் நிவாரணம், மீட்பு மற்றும் தணிப்பு நடவடிக்கைகளுக்கான பகிர்வு நிதி"
        ],
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "Tax devolution is untied; Revenue Deficit grants fill assessed post-transfer fiscal gaps; Local body grants support grassroot services; Disaster grants provide emergency safety nets.",
        "exp_ta": "வரிப் பகிர்வு நிபந்தனையற்றது; வருவாய்ப் பற்றாக்குறை மானியம் நிதி இடைவெளியை நிரப்புகிறது; உள்ளாட்சி மானியம் குடிமைப் பணிகளை ஆதரிக்கிறது; பேரிடர் மானியம் அவசர கால பாதுகாப்பை வழங்குகிறது.",
        "tip_en": "Tax devolution accounts for approximately 80% of total Finance Commission transfers.",
        "tip_ta": "நிதி ஆணையத்தின் மொத்த நிதிப் பகிர்வில் வரிப் பகிர்வு சுமார் 80% பங்கைக் கொண்டுள்ளது.",
        "fact_en": "Article 275 grants are non-votable charged expenditures under Article 113.",
        "fact_ta": "சரத்து 275 மானியங்கள் நாடாளுமன்ற வாக்கெடுப்புக்கு உட்படாத பொறுப்பாக்கப்பட்ட செலவுகளாகும்."
    },
    # 9
    {
        "subtopic": "Disaster Financing Cost-Sharing Ratios",
        "intro_en": "Match List-I (Disaster Fund Window) with List-II (Central : State Sharing Ratio) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (பேரிடர் நிதி சாளரம்) பட்டியல்-II உடன் (மத்திய : மாநில பகிர்வு விகிதம்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": [
            "SDRF for General Category States",
            "SDRF for North-Eastern & Himalayan States",
            "National Disaster Response Fund (NDRF)",
            "State Disaster Mitigation Fund (General States)"
        ],
        "list1_ta": [
            "பொதுப் பிரிவு மாநிலங்களுக்கான SDRF",
            "வடகிழக்கு மற்றும் இமயமலை மாநிலங்களுக்கான SDRF",
            "தேசிய பேரிடர் மீட்பு நிதி (NDRF)",
            "மாநில பேரிடர் தணிப்பு நிதி (பொது மாநிலங்கள்)"
        ],
        "list2_en": ["75 : 25", "90 : 10", "100% Central Funding", "75 : 25"],
        "list2_ta": ["75 : 25", "90 : 10", "100% மத்திய நிதி", "75 : 25"],
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "General category states share SDRF and SDMF at 75:25; NE and Himalayan states receive 90:10; NDRF is funded 100% by the Centre through NCCD cess.",
        "exp_ta": "பொது மாநிலங்களுக்கு SDRF மற்றும் SDMF 75:25; வடகிழக்கு மற்றும் மலை மாநிலங்களுக்கு 90:10; NDRF மத்திய அரசால் 100% நிதியளிக்கப்படுகிறது.",
        "tip_en": "90:10 ratio reflects the severe topographical and fiscal disabilities of Himalayan states.",
        "tip_ta": "90:10 விகிதம் இமயமலை மாநிலங்களின் கடுமையான புவியியல் மற்றும் நிதி பலவீனத்தை பிரதிபலிக்கிறது.",
        "fact_en": "National Calamity Contingent Duty (NCCD) finances the NDRF.",
        "fact_ta": "தேசிய பேரிடர் எதிர்பாராத செலவின வரி (NCCD) NDRF-க்கு நிதியளிக்கிறது."
    },
    # 10
    {
        "subtopic": "Articles on Union-State Tax Distribution",
        "intro_en": "Match List-I (Article of Constitution) with List-II (Tax Distribution Scheme) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (அரசியலமைப்புச் சரத்து) பட்டியல்-II உடன் (வரிப் பகிர்வு முறை) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": ["Article 268", "Article 269", "Article 270", "Article 271"],
        "list1_ta": ["சரத்து 268", "சரத்து 269", "சரத்து 270", "சரத்து 271"],
        "list2_en": [
            "Duties levied by Union but collected and appropriated by States (Stamp Duties)",
            "Taxes levied and collected by Union but assigned wholly to States (Inter-state sales)",
            "Taxes levied and collected by Union and distributed between Union and States",
            "Surcharge on certain duties and taxes for purposes of the Union (Excluded from pool)"
        ],
        "list2_ta": [
            "மத்திய அரசால் விதிக்கப்பட்டு மாநிலங்களால் வசூலிக்கப்பட்டு பயன்படுத்தப்படும் வரிகள் (முத்திரைத்தாள்)",
            "மத்திய அரசால் விதிக்கப்பட்டு வசூலிக்கப்பட்டு முழுமையாக மாநிலங்களுக்கு ஒதுக்கப்படும் வரிகள்",
            "மத்திய அரசால் விதிக்கப்பட்டு வசூலிக்கப்பட்டு மத்திய-மாநிலங்களுக்கு இடையே பகிர்ந்தளிக்கப்படும் வரிகள்",
            "மத்திய அரசின் தேவைகளுக்காக சில வரிகள் மீதான கூடுதல் வரி (பகிர்வு நிதியிலிருந்து விலக்கப்பட்டவை)"
        ],
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "Article 268 covers duties collected by states; Article 269 taxes assigned to states; Article 270 the general divisible tax pool; Article 271 surcharges exclusively retained by Union.",
        "exp_ta": "சரத்து 268 மாநிலங்களால் வசூலிக்கப்படும் வரிகள்; சரத்து 269 மாநிலங்களுக்கு ஒதுக்கப்படும் வரிகள்; சரத்து 270 பொது பகிர்வு நிதி; சரத்து 271 மத்திய அரசிற்கு மட்டுமே உரிய கூடுதல் வரிகள்.",
        "tip_en": "Article 270 is the primary engine of Finance Commission recommendations.",
        "tip_ta": "சரத்து 270 நிதி ஆணையத்தின் முதன்மை செயல்பாட்டு விதியாகும்.",
        "fact_en": "GST brought Article 269A into force for inter-state transactions (IGST).",
        "fact_ta": "ஜிஎஸ்டி மூலம் மாநிலங்களுக்கு இடையிலான பரிவர்த்தனைகளுக்கு (IGST) சரத்து 269A கொண்டுவரப்பட்டது."
    },
    # 11
    {
        "subtopic": "Local Body Grants Architecture (15th FC)",
        "intro_en": "Match List-I (Local Body Grant Component) with List-II (Specific Structural Norm) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (உள்ளாட்சி மானியப் பிரிவு) பட்டியல்-II உடன் (குறிப்பிட்ட கட்டமைப்பு விதி) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": [
            "Rural Local Bodies (Panchayats) Split",
            "Million-Plus Urban Agglomerations",
            "Non-Million-Plus Urban Local Bodies",
            "Health Sector Grants via Local Bodies"
        ],
        "list1_ta": [
            "ஊரக உள்ளாட்சி (பஞ்சாயத்துகள்) பகிர்வு",
            "பத்து லட்சத்திற்கும் அதிகமான மக்கள் தொகை கொண்ட நகரங்கள்",
            "பத்து லட்சத்திற்கும் குறைவான மக்கள் தொகை கொண்ட நகராட்சிகள்",
            "உள்ளாட்சிகள் மூலம் சுகாதார துறை மானியங்கள்"
        ],
        "list2_en": [
            "40% untied (basic discretionary) and 60% tied (drinking water & sanitation)",
            "100% performance-linked to air quality metrics and urban water/solid waste outcomes",
            "40% untied and 60% tied to basic civic public services",
            "Rs. 70,051 crore earmarked to convert rural sub-centres into Health & Wellness Centres"
        ],
        "list2_ta": [
            "40% நிபந்தனையற்றவை மற்றும் 60% நிபந்தனைக்குட்பட்டவை (குடிநீர் & சுகாதாரம்)",
            "100% காற்றுத் தரம் மற்றும் குடிநீர்/திடக்கழிவு மேலாண்மை செயல்திறனுடன் இணைக்கப்பட்டது",
            "40% நிபந்தனையற்றவை மற்றும் 60% அடிப்படை குடிமைப் பணிகளுடன் இணைக்கப்பட்டது",
            "துணை சுகாதார நிலையங்களை நலவாழ்வு மையங்களாக மாற்ற ரூ. 70,051 கோடி ஒதுக்கீடு"
        ],
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "Rural split is 40:60 untied:tied; Million-plus cities receive 100% outcome-linked funds; Non-million cities have 40:60 split; Health grants total Rs. 70,051 crore.",
        "exp_ta": "ஊரகப் பகிர்வு 40:60 நிபந்தனையற்றவை:நிபந்தனை; பத்து லட்சத்திற்கும் அதிகமான நகரங்களுக்கு 100% செயல்திறன் நிதி; பிற நகரங்களுக்கு 40:60; சுகாதார மானியம் ரூ. 70,051 கோடி.",
        "tip_en": "Tied grants directly support Swachh Bharat and Jal Jeevan missions at the grassroot tier.",
        "tip_ta": "நிபந்தனை மானியங்கள் தூய்மை பாரதம் மற்றும் ஜல் ஜீவன் இயக்கங்களை அடிமட்டத்தில் ஆதரிக்கின்றன.",
        "fact_en": "Online accounting (e-GramSwaraj) is mandatory for accessing these grants.",
        "fact_ta": "இம்மான்யங்களைப் பெற e-GramSwaraj மூலமான இணையக் கணக்கியல் கட்டாயமாகும்."
    },
    # 12
    {
        "subtopic": "Chairmen of Mid-Era Commissions",
        "intro_en": "Match List-I (Mid-Era Finance Commission) with List-II (Appointed Chairman) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (இடைக்கால நிதி ஆணையம்) பட்டியல்-II உடன் (நியமிக்கப்பட்ட தலைவர்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": [
            "Fourth Finance Commission (1964)",
            "Fifth Finance Commission (1968)",
            "Sixth Finance Commission (1972)",
            "Seventh Finance Commission (1977)"
        ],
        "list1_ta": [
            "நான்காவது நிதி ஆணையம் (1964)",
            "ஐந்தாவது நிதி ஆணையம் (1968)",
            "ஆறாவது நிதி ஆணையம் (1972)",
            "ஏழாவது நிதி ஆணையம் (1977)"
        ],
        "list2_en": ["P.V. Rajamannar", "Mahavir Tyagi", "K. Brahmananda Reddy", "J.M. Shelat"],
        "list2_ta": ["பி.வி. ராஜமன்னார்", "மகாவீர் தியாகி", "கே. பிரம்மானந்த ரெட்டி", "ஜே.எம். ஷெலத்"],
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "4th FC: P.V. Rajamannar; 5th FC: Mahavir Tyagi; 6th FC: K. Brahmananda Reddy; 7th FC: J.M. Shelat.",
        "exp_ta": "4வது: பி.வி. ராஜமன்னார்; 5வது: மகாவீர் தியாகி; 6வது: கே. பிரம்மானந்த ரெட்டி; 7வது: ஜே.எம். ஷெலத்.",
        "tip_en": "Rajamannar was former Chief Justice of Madras High Court.",
        "tip_ta": "ராஜமன்னார் சென்னை உயர் நீதிமன்றத்தின் முன்னாள் தலைமை நீதிபதியாவார்.",
        "fact_en": "Justice Shelat was a former Judge of the Supreme Court of India.",
        "fact_ta": "நீதிபதி ஷெலத் இந்திய உச்ச நீதிமன்றத்தின் முன்னாள் நீதிபதியாவார்."
    },
    # 13
    {
        "subtopic": "Chairmen of Economic Reform Era",
        "intro_en": "Match List-I (Reform Era Finance Commission) with List-II (Appointed Chairman) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (சீர்திருத்த கால நிதி ஆணையம்) பட்டியல்-II உடன் (நியமிக்கப்பட்ட தலைவர்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": [
            "Eighth Finance Commission (1982)",
            "Ninth Finance Commission (1987)",
            "Tenth Finance Commission (1992)",
            "Eleventh Finance Commission (1998)"
        ],
        "list1_ta": [
            "எட்டாவது நிதி ஆணையம் (1982)",
            "ஒன்பதாவது நிதி ஆணையம் (1987)",
            "பத்தாவது நிதி ஆணையம் (1992)",
            "பதினோராவது நிதி ஆணையம் (1998)"
        ],
        "list2_en": ["Y.B. Chavan", "N.K.P. Salve", "K.C. Pant", "A.M. Khusro"],
        "list2_ta": ["ஒய்.பி. சவான்", "என்.கே.பி. சால்வே", "கே.சி. பந்த்", "ஏ.எம். குஸ்ரோ"],
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "8th FC: Y.B. Chavan; 9th FC: N.K.P. Salve; 10th FC: K.C. Pant; 11th FC: A.M. Khusro.",
        "exp_ta": "8வது: ஒய்.பி. சவான்; 9வது: என்.கே.பி. சால்வே; 10வது: கே.சி. பந்த்; 11வது: ஏ.எம். குஸ்ரோ.",
        "tip_en": "Y.B. Chavan was former Deputy Prime Minister of India.",
        "tip_ta": "ஒய்.பி. சவான் இந்தியாவின் முன்னாள் துணைப் பிரதமராவார்.",
        "fact_en": "Prof. A.M. Khusro was a distinguished economist and former Vice-Chancellor of AMU.",
        "fact_ta": "பேராசிரியர் ஏ.எம். குஸ்ரோ புகழ்பெற்ற பொருளாதார நிபுணர் மற்றும் அலிகார் முஸ்லிம் பல்கலைக்கழக முன்னாள் துணைவேந்தராவார்."
    },
    # 14
    {
        "subtopic": "Institutional Roles in Indian Public Finance",
        "intro_en": "Match List-I (Constitutional/Statutory Institution) with List-II (Core Fiscal Role) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (அரசியலமைப்பு/சட்டப்பூர்வ அமைப்பு) பட்டியல்-II உடன் (முதன்மை நிதிப் பணி) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": [
            "Finance Commission (Art 280)",
            "GST Council (Art 279A)",
            "Comptroller & Auditor General (Art 148)",
            "NITI Aayog (Executive Resolution)"
        ],
        "list1_ta": [
            "நிதி ஆணையம் (சரத்து 280)",
            "ஜிஎஸ்டி கவுன்சில் (சரத்து 279A)",
            "கணக்குத் தணிக்கைத் தலைவர் (சரத்து 148)",
            "நிதி ஆயோக் (நிர்வாகத் தீர்மானம்)"
        ],
        "list2_en": [
            "Quinquennial recommendation on tax devolution and revenue deficit grants",
            "Joint federal forum deciding unified indirect tax slabs and exemptions",
            "Auditing of receipts and expenditures and certification of net tax proceeds",
            "Strategic think-tank fostering cooperative federalism without financial allocation powers"
        ],
        "list2_ta": [
            "ஐந்தாண்டு வரிப் பகிர்வு மற்றும் வருவாய்ப் பற்றாக்குறை மானியங்களை பரிந்துரைத்தல்",
            "ஒருங்கிணைந்த மறைமுக வரி விகிதங்கள் மற்றும் விலக்குகளைத் தீர்மானிக்கும் கூட்டாட்சி மன்றம்",
            "வரவு செலவு தணிக்கை மற்றும் நிகர வரி வருவாயை சான்றளித்தல்",
            "நிதி ஒதுக்கீடு அதிகாரமின்றி கூட்டுறவு கூட்டாட்சியை வளர்க்கும் கொள்கை சிந்தனைக் குழு"
        ],
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "FC handles tax devolution; GST Council sets indirect tax rates; CAG certifies audit numbers; NITI Aayog provides strategic policy advice.",
        "exp_ta": "நிதி ஆணையம் வரிப் பகிர்வை கையாள்கிறது; ஜிஎஸ்டி கவுன்சில் வரி விகிதங்களை நிர்ணயிக்கிறது; சி.ஏ.ஜி தணிக்கை புள்ளிவிவரங்களை சான்றளிக்கிறது; நிதி ஆயோக் கொள்கை ஆலோசனைகளை வழங்குகிறது.",
        "tip_en": "None of these institutions duplicate each other's distinct constitutional jurisdictions.",
        "tip_ta": "இவ்வமைப்புகள் எதுவும் தங்களுக்குள் அதிகார வரம்பை மீறுவதில்லை.",
        "fact_en": "GST Council is chaired by the Union Finance Minister with State Finance Ministers as members.",
        "fact_ta": "மத்திய நிதி அமைச்சர் தலைமையில் மாநில நிதி அமைச்சர்களை உறுப்பினர்களாகக் கொண்டு ஜிஎஸ்டி கவுன்சில் இயங்குகிறது."
    },
    # 15
    {
        "subtopic": "Core Concepts in Fiscal Federalism",
        "intro_en": "Match List-I (Fiscal Federalism Concept) with List-II (Theoretical Definition) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (நிதி கூட்டாட்சிக் கோட்பாடு) பட்டியல்-II உடன் (கோட்பாட்டு வரையறை) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": [
            "Vertical Fiscal Imbalance",
            "Horizontal Fiscal Disparity",
            "Divisible Pool",
            "Fiscal Disability"
        ],
        "list1_ta": [
            "செங்குத்து நிதி ஏற்றத்தாழ்வு",
            "கிடைமட்ட நிதி ஏற்றத்தாழ்வு",
            "பகிர்வு நிதி (Divisible Pool)",
            "நிதிப் பலவீனம் (Fiscal Disability)"
        ],
        "list2_en": [
            "Asymmetry between high revenue powers of Centre and heavy expenditure mandates of States",
            "Inequalities in revenue mobilization capacity and development levels across different States",
            "Net proceeds of Union taxes mandated under Article 270 to be shared with States",
            "Exogenous cost disadvantages due to hilly topography, forest cover, or dispersed population"
        ],
        "list2_ta": [
            "மத்தியின் அதிக வருவாய் அதிகாரத்திற்கும் மாநிலங்களின் அதிக செலவின பொறுப்புகளுக்கும் இடையிலான சமச்சீரற்ற தன்மை",
            "பல்வேறு மாநிலங்களுக்கு இடையிலான வருவாய் திரட்டும் திறன் மற்றும் வளர்ச்சி நிலைகளில் உள்ள ஏற்றத்தாழ்வுகள்",
            "சரத்து 270-ன் கீழ் மாநிலங்களுடன் பகிர்ந்தளிக்கப்பட வேண்டிய மத்திய வரிகளின் நிகர வருவாய்",
            "மலை நிலப்பரப்பு, வனப் பரப்பு அல்லது சிதறிய மக்கள் தொகையால் ஏற்படும் வெளிப்புற செலவு பாதகங்கள்"
        ],
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "Vertical imbalance is Centre vs States; Horizontal disparity is State vs State; Divisible pool is shareable tax basket; Fiscal disability represents exogenous structural cost disadvantages.",
        "exp_ta": "செங்குத்து ஏற்றத்தாழ்வு என்பது மத்திய-மாநில சமச்சீரற்ற தன்மை; கிடைமட்ட ஏற்றத்தாழ்வு என்பது மாநிலங்களுக்கு இடையிலான வேறுபாடு; பகிர்வு நிதி என்பது பகிரக்கூடிய வரித் தொகுப்பு; நிதி பலவீனம் என்பது வெளிப்புற செலவு பாதகமாகும்.",
        "tip_en": "Finance Commission tackles vertical imbalance via percentage devolution, and horizontal disparity via formula weighting.",
        "tip_ta": "நிதி ஆணையம் சதவீத பகிர்வு மூலம் செங்குத்து ஏற்றத்தாழ்வையும், சூத்திர எடைகள் மூலம் கிடைமட்ட ஏற்றத்தாழ்வையும் சரிசெய்கிறது.",
        "fact_en": "Horizontal transfers embody the constitutional principle of equalization.",
        "fact_ta": "கிடைமட்ட பகிர்வுகள் சமத்துவ அரசியலமைப்பு கோட்பாட்டை உள்ளடக்கியுள்ளன."
    },
    # 16
    {
        "subtopic": "Qualifications of Members under 1951 Act",
        "intro_en": "Match List-I (Designated Member Slot) with List-II (Statutory Qualification Category) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (நியமிக்கப்படும் உறுப்பினர் பிரிவு) பட்டியல்-II உடன் (சட்டப்பூர்வ தகுதி வகை) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": ["Member 1 (Judicial)", "Member 2 (Accounts)", "Member 3 (Administration)", "Member 4 (Economics)"],
        "list1_ta": ["உறுப்பினர் 1 (நீதித்துறை)", "உறுப்பினர் 2 (கணக்குகள்)", "உறுப்பினர் 3 (நிர்வாகம்)", "உறுப்பினர் 4 (பொருளாதாரம்)"],
        "list2_en": [
            "Qualified to be appointed as a Judge of a High Court",
            "Special knowledge of the finance and accounts of the Government",
            "Wide experience in financial matters and in administration",
            "Special knowledge of economics"
        ],
        "list2_ta": [
            "உயர் நீதிமன்ற நீதிபதியாக நியமிக்கப்பட தகுதியுடையவர்",
            "அரசாங்கத்தின் நிதி மற்றும் கணக்குகள் பற்றிய சிறப்பு அறிவு கொண்டவர்",
            "நிதி விவகாரங்கள் மற்றும் நிர்வாகத்தில் பரந்த அனுபவம் கொண்டவர்",
            "பொருளாதாரத்தில் சிறப்பு அறிவு கொண்டவர்"
        ],
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "Section 4 of the Finance Commission Act 1951 specifies these exact four distinct qualifications for the four members.",
        "exp_ta": "1951 நிதி ஆணையச் சட்டத்தின் பிரிவு 4 நான்கு உறுப்பினர்களுக்கான இந்த நான்கு குறிப்பிட்ட தகுதிகளை வரையறுக்கிறது.",
        "tip_en": "High Court qualification is required for the judicial member, not Supreme Court.",
        "tip_ta": "நீதித்துறை உறுப்பினருக்கு உயர் நீதிமன்ற நீதிபதி தகுதியே தேவை, உச்ச நீதிமன்றம் அல்ல.",
        "fact_en": "Chairman must be an eminent person with experience in public affairs.",
        "fact_ta": "தலைவர் பொது விவகாரங்களில் அனுபவம் வாய்ந்த ஒரு சிறந்த நபராக இருக்க வேண்டும்."
    },
    # 17
    {
        "subtopic": "Federal Committees & Landmark Reports",
        "intro_en": "Match List-I (Federal Inquiry Committee) with List-II (Key Recommendation on Finance Commission) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (கூட்டாட்சி ஆய்வுக் குழு) பட்டியல்-II உடன் (நிதி ஆணையம் குறித்த முக்கிய பரிந்துரை) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": [
            "Rajamannar Committee (1969)",
            "Sarkaria Commission (1988)",
            "Punchhi Commission (2010)",
            "N.K. Singh FRBM Committee (2017)"
        ],
        "list1_ta": [
            "ராஜமன்னார் குழு (1969)",
            "சர்க்காரியா ஆணையம் (1988)",
            "பூஞ்சி ஆணையம் (2010)",
            "என்.கே. சிங் FRBM குழு (2017)"
        ],
        "list2_en": [
            "Recommended making the Finance Commission a permanent constitutional body",
            "Emphasized non-interference with Finance Commission awards and full tax pooling",
            "Advocated institutional coordination between Finance Commission and NITI Aayog",
            "Proposed a debt-to-GDP anchor of 60% (40% Centre, 20% States) by 2023"
        ],
        "list2_ta": [
            "நிதி ஆணையத்தை ஒரு நிரந்தர அரசியலமைப்பு அமைப்பாக மாற்ற பரிந்துரைத்தது",
            "நிதி ஆணையப் பரிந்துரைகளில் தலையிடாமையையும் முழுமையான வரிப் பகிர்வையும் வலியுறுத்தியது",
            "நிதி ஆணையம் மற்றும் நிதி ஆயோக் இடையே நிறுவன ஒருங்கிணைப்பை ஆதரித்தது",
            "2023-க்குள் கடன்-ஜிடிபி விகிதத்தை 60% (மத்திய அரசு 40%, மாநிலங்கள் 20%) ஆக இலக்கு வைக்க முன்மொழிந்தது"
        ],
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "Rajamannar sought a permanent FC; Sarkaria urged sanctity of awards; Punchhi focused on modern institutional synergy; N.K. Singh proposed 60% debt ceiling.",
        "exp_ta": "ராஜமன்னார் நிரந்தர ஆணையத்தை நாடினார்; சர்க்காரியா பரிந்துரைகளின் புனிதத்தை வலியுறுத்தினார்; பூஞ்சி நிறுவன ஒருங்கிணைப்பில் கவனம் செலுத்தினார்; என்.கே. சிங் 60% கடன் வரம்பை முன்மொழிந்தார்.",
        "tip_en": "Rajamannar Committee was set up specifically by the Tamil Nadu Government.",
        "tip_ta": "ராஜமன்னார் குழு தமிழ்நாடு அரசால் பிரத்யேகமாக அமைக்கப்பட்டது.",
        "fact_en": "Sarkaria recommendations paved the way for the 80th Constitutional Amendment.",
        "fact_ta": "சர்க்காரியா பரிந்துரைகள் 80வது அரசியலமைப்புத் திருத்தத்திற்கு வழிவகுத்தன."
    },
    # 18
    {
        "subtopic": "Special Provisions & Asymmetric Federalism",
        "intro_en": "Match List-I (Special Federal Entity) with List-II (FC Treatment / Fiscal Architecture) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (சிறப்பு கூட்டாட்சி அமைப்பு) பட்டியல்-II உடன் (நிதி ஆணைய அணுகுமுறை / நிதி முறை) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": [
            "Sixth Schedule Tribal Councils",
            "Union Territories of J&K and Ladakh",
            "North-Eastern States",
            "Assam Border Development"
        ],
        "list1_ta": [
            "ஆறாவது அட்டவணை பழங்குடியினர் மன்றங்கள்",
            "ஜம்மு காஷ்மீர் & லடாக் யூனியன் பிரதேசங்கள்",
            "வடகிழக்கு மாநிலங்கள்",
            "அசாம் எல்லை வளர்ச்சி"
        ],
        "list2_en": [
            "Received direct Article 275 grants outside standard Parts IX/IXA local bodies",
            "Funded directly from Union's 59% retainable share instead of 41% state pool",
            "Benefit from 90:10 disaster funding and higher forest cover weighting",
            "Guaranteed constitutional grants under the second proviso to Article 275(1)"
        ],
        "list2_ta": [
            "பகுதி IX/IXA உள்ளாட்சி எல்லைக்கு வெளியே சரத்து 275 மூலம் நேரடி மானியங்களைப் பெற்றன",
            "41% மாநில நிதிக்கு பதிலாக மத்திய அரசின் 59% நிதியிலிருந்து நேரடியாகப் பெறுகின்றன",
            "90:10 பேரிடர் நிதி மற்றும் அதிக வனப் பரப்பு எடை மூலம் பலன் பெறுகின்றன",
            "சரத்து 275(1)-ன் இரண்டாவது வரம்புரையின் கீழ் உத்தரவாதமான அரசியலமைப்பு மானியம் பெறுகின்றன"
        ],
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "Sixth Schedule councils get Article 275 direct grants; UTs are funded from Centre's 59% share; NE states enjoy 90:10 disaster matching; Assam has second proviso rights.",
        "exp_ta": "ஆறாவது அட்டவணை மன்றங்கள் சரத்து 275 நேரடி மானியங்களைப் பெறுகின்றன; யூனியன் பிரதேசங்கள் மத்திய அரசின் 59% பங்கிலிருந்து பெறுகின்றன; வடகிழக்கு மாநிலங்கள் 90:10 சலுகை பெறுகின்றன; அசாம் வரம்புரை உரிமையைப் பெற்றுள்ளது.",
        "tip_en": "Asymmetric fiscal federalism accommodates distinct geopolitical realities.",
        "tip_ta": "சமச்சீரற்ற நிதி கூட்டாட்சி பல்வேறு புவிசார் அரசியல் உண்மைகளுக்கு இடமளிக்கிறது.",
        "fact_en": "The second proviso to Article 275(1) was designed specifically for Assam's autonomous tribal areas.",
        "fact_ta": "சரத்து 275(1)-ன் இரண்டாவது வரம்புரை அசாமின் தன்னாட்சிப் பழங்குடியினப் பகுதிகளுக்காக பிரத்யேகமாக உருவாக்கப்பட்டது."
    },
    # 19
    {
        "subtopic": "14th FC Criteria & Weights",
        "intro_en": "Match List-I (14th FC Devolution Criterion) with List-II (Assigned Percentage Weight) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (14வது நிதி ஆணையப் பகிர்வு அளவுகோல்) பட்டியல்-II உடன் (ஒதுக்கப்பட்ட சதவீத எடை) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": ["Income Distance", "Population (1971 Census)", "Demographic Change (2011 Census)", "Forest Cover"],
        "list1_ta": ["வருமான இடைவெளி", "மக்கள் தொகை (1971 கணக்கெடுப்பு)", "மக்கள்தொகை மாற்றம் (2011 கணக்கெடுப்பு)", "வனப் பரப்பு"],
        "list2_en": ["50.0%", "17.5%", "10.0%", "7.5%"],
        "list2_ta": ["50.0%", "17.5%", "10.0%", "7.5%"],
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "14th FC weights: Income Distance 50%, 1971 Population 17.5%, 2011 Population 10%, Forest Cover 7.5% (plus Area 15%).",
        "exp_ta": "14வது நிதி ஆணைய எடைகள்: வருமான இடைவெளி 50%, 1971 மக்கள் தொகை 17.5%, 2011 மக்கள் தொகை 10%, வனப் பரப்பு 7.5% (பரப்பளவு 15%).",
        "tip_en": "14th FC was the first to use 2011 Census population (with 10% weight).",
        "tip_ta": "2011 மக்கள் தொகை கணக்கெடுப்பை (10% எடையுடன்) பயன்படுத்திய முதல் ஆணையம் 14வது நிதி ஆணையமாகும்.",
        "fact_en": "14th FC also introduced Forest Cover for the first time at 7.5%.",
        "fact_ta": "14வது ஆணையம் முதல்முறையாக வனப் பரப்பை 7.5% எடையுடன் அறிமுகப்படுத்தியது."
    },
    # 20
    {
        "subtopic": "Devolution Share Across Modern Commissions",
        "intro_en": "Match List-I (Finance Commission) with List-II (Vertical Devolution Percentage to States) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (நிதி ஆணையம்) பட்டியல்-II உடன் (மாநிலங்களுக்கு வழங்கப்பட்ட செங்குத்து வரிப் பகிர்வு சதவீதம்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": [
            "Eleventh Finance Commission (2000-05)",
            "Twelfth Finance Commission (2005-10)",
            "Thirteenth Finance Commission (2010-15)",
            "Fourteenth Finance Commission (2015-20)"
        ],
        "list1_ta": [
            "பதினோராவது நிதி ஆணையம் (2000-05)",
            "பன்னிரண்டாவது நிதி ஆணையம் (2005-10)",
            "பதின்மூன்றாவது நிதி ஆணையம் (2010-15)",
            "பதினான்காவது நிதி ஆணையம் (2015-20)"
        ],
        "list2_en": ["29.5%", "30.5%", "32.0%", "42.0%"],
        "list2_ta": ["29.5%", "30.5%", "32.0%", "42.0%"],
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "Vertical shares grew steadily: 11th FC: 29.5%; 12th FC: 30.5%; 13th FC: 32.0%; 14th FC: 42.0%.",
        "exp_ta": "செங்குத்துப் பகிர்வு படிப்படியாக உயர்ந்தது: 11வது: 29.5%; 12வது: 30.5%; 13வது: 32.0%; 14வது: 42.0%.",
        "tip_en": "The jump from 32% to 42% in 2015 marked a historic 10-percentage point increase.",
        "tip_ta": "2015-ல் 32%-லிருந்து 42%-ஆக உயர்ந்தது வரலாற்றுச் சிறப்புமிக்க 10 சதவீத புள்ளிகள் உயர்வாகும்.",
        "fact_en": "15th FC adjusted the share to 41% to accommodate J&K and Ladakh.",
        "fact_ta": "15வது ஆணையம் ஜம்மு காஷ்மீர் மற்றும் லடாக்கிற்கு இடமளிக்க பங்கை 41% ஆக மாற்றியது."
    },
    # 21
    {
        "subtopic": "Finance Commission Award Operating Periods",
        "intro_en": "Match List-I (Finance Commission) with List-II (Five-Year Award Period) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (நிதி ஆணையம்) பட்டியல்-II உடன் (ஐந்தாண்டு செயல்பாட்டுக் காலம்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": [
            "Twelfth Finance Commission",
            "Thirteenth Finance Commission",
            "Fourteenth Finance Commission",
            "Fifteenth Finance Commission (Main Report)"
        ],
        "list1_ta": [
            "பன்னிரண்டாவது நிதி ஆணையம்",
            "பதின்மூன்றாவது நிதி ஆணையம்",
            "பதினான்காவது நிதி ஆணையம்",
            "பதினைந்தாவது நிதி ஆணையம் (முதன்மை அறிக்கை)"
        ],
        "list2_en": ["2005 - 2010", "2010 - 2015", "2015 - 2020", "2021 - 2026"],
        "list2_ta": ["2005 - 2010", "2010 - 2015", "2015 - 2020", "2021 - 2026"],
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "12th FC: 2005-10; 13th FC: 2010-15; 14th FC: 2015-20; 15th FC main report: 2021-26 (following an interim report for 2020-21).",
        "exp_ta": "12வது: 2005-10; 13வது: 2010-15; 14வது: 2015-20; 15வது முதன்மை அறிக்கை: 2021-26 (2020-21 இடைக்கால அறிக்கைக்குப் பிறகு).",
        "tip_en": "Award periods always coincide with the financial year starting April 1.",
        "tip_ta": "பரிந்துரைக் காலங்கள் எப்போதும் ஏப்ரல் 1 அன்று தொடங்கும் நிதியாண்டுடன் ஒத்துப்போகின்றன.",
        "fact_en": "16th FC award period will commence from April 1, 2026 to March 31, 2031.",
        "fact_ta": "16வது ஆணையத்தின் செயல்பாட்டுக் காலம் ஏப்ரல் 1, 2026 முதல் மார்ச் 31, 2031 வரை இருக்கும்."
    },
    # 22
    {
        "subtopic": "Terms of Reference (ToR) Strategic Mandates",
        "intro_en": "Match List-I (Specific ToR Clause) with List-II (Strategic Mandate) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (குறிப்பிட்ட பணிக் குறிப்புப் பிரிவு) பட்டியல்-II உடன் (உத்திசார் பணி) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": [
            "Disaster Management Financing",
            "Performance-Based Incentives",
            "Defence & Internal Security Funding",
            "Review of Power Sector Distribution"
        ],
        "list1_ta": [
            "பேரிடர் மேலாண்மை நிதி",
            "செயல்திறன் அடிப்படையிலான ஊக்கத்தொகை",
            "பாதுகாப்பு மற்றும் உள்நாட்டு பாதுகாப்பு நிதி",
            "மின்சார விநியோகத் துறை மறுஆய்வு"
        ],
        "list2_en": [
            "Reviewing SDRF and operationalizing mitigation funds under Disaster Management Act",
            "Rewarding states for demographic transition, ease of doing business, and tax effort",
            "Examining whether a dedicated non-lapsable modernisation fund should be created",
            "Incentivizing reduction in aggregate technical and commercial (AT&C) power losses"
        ],
        "list2_ta": [
            "SDRF-ஐ மறுஆய்வு செய்தல் மற்றும் பேரிடர் சட்டத்தின் கீழ் தணிப்பு நிதியை செயல்படுத்துதல்",
            "மக்கள்தொகை கட்டுப்பாடு, தொழில் தொடங்குதல் எளிமை மற்றும் வரி முயற்சிக்கு வெகுமதி அளித்தல்",
            "காலாவதியாகாத பிரத்யேக நவீனமயமாக்கல் நிதியை உருவாக்கலாமா என ஆய்வு செய்தல்",
            "மின் இழப்புகளைக் (AT&C losses) குறைக்கும் மாநிலங்களுக்கு கூடுதல் கடன் வசதி ஊக்கமளித்தல்"
        ],
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "ToR mandates cover disaster funding, performance incentives, non-lapsable defence funds, and power discom reforms.",
        "exp_ta": "பணிக் குறிப்புகள் பேரிடர் நிதி, செயல்திறன் ஊக்கத்தொகை, காலாவதியாகாத பாதுகாப்பு நிதி மற்றும் மின் விநியோக சீர்திருத்தங்களை உள்ளடக்கியுள்ளன.",
        "tip_en": "Terms of Reference are issued by the President under Article 280(3)(d).",
        "tip_ta": "பணிக் குறிப்புகள் சரத்து 280(3)(d)-ன் கீழ் குடியரசுத் தலைவரால் வெளியிடப்படுகின்றன.",
        "fact_en": "Presidential orders determine the precise scope and duration of each Commission.",
        "fact_ta": "குடியரசுத் தலைவர் ஆணைகள் ஒவ்வொரு ஆணையத்தின் துல்லியமான நோக்கம் மற்றும் காலத்தை நிர்ணயிக்கின்றன."
    },
    # 23
    {
        "subtopic": "15th FC Sector-Specific Local Grants",
        "intro_en": "Match List-I (Local Body Sectoral Earmark) with List-II (Specific Policy Target) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (உள்ளாட்சி துறைசார் ஒதுக்கீடு) பட்டியல்-II உடன் (குறிப்பிட்ட கொள்கை இலக்கு) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": [
            "Million-Plus Air Quality Fund",
            "Rural Drinking Water Tied Grant",
            "Sanitation & ODF Maintenance",
            "Diagnostic Infrastructure in PHCs"
        ],
        "list1_ta": [
            "பத்து லட்சத்திற்கும் அதிகமான நகர காற்றுத் தர நிதி",
            "ஊரக குடிநீர் நிபந்தனை மானியம்",
            "சுகாதாரம் & ODF பராமரிப்பு",
            "ஆரம்ப சுகாதார நிலையங்களில் கண்டறியும் உள்கட்டமைப்பு"
        ],
        "list2_en": [
            "Incentivizing urban agglomerations to reduce PM10 and PM2.5 particulate levels",
            "Supporting supply of clean piped drinking water and rainwater harvesting",
            "Maintaining open-defecation-free status and fecal sludge management systems",
            "Providing essential testing and digital diagnostic tools at rural wellness sub-centres"
        ],
        "list2_ta": [
            "நகர்ப்புறங்களில் PM10 மற்றும் PM2.5 நுண்துகள்களின் அளவைக் குறைக்க ஊக்கமளித்தல்",
            "குழாய் மூலம் சுத்தமான குடிநீர் விநியோகம் மற்றும் மழைநீர் சேகரிப்பை ஆதரித்தல்",
            "திறந்தவெளி கழிப்பிடம் அற்ற நிலையைத் தக்கவைத்தல் மற்றும் கழிவு மேலாண்மை",
            "ஊரக நல மையங்களில் அத்தியாவசிய பரிசோதனை மற்றும் டிஜிட்டல் கருவிகளை வழங்குதல்"
        ],
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "Air quality funds target PM concentrations; Drinking water supports Jal Jeevan; Sanitation supports Swachh Bharat; Diagnostic funds support Ayushman Bharat centres.",
        "exp_ta": "காற்றுத் தர நிதி நுண்துகள்களைக் குறைக்கிறது; குடிநீர் நிதி ஜல் ஜீவன் திட்டத்தை ஆதரிக்கிறது; சுகாதாரம் தூய்மை பாரதத்தை ஆதரிக்கிறது; ஆய்வு நிதி ஆயுஷ்மான் பாரத் மையங்களை ஆதரிக்கிறது.",
        "tip_en": "Grants are strictly performance-monitored before subsequent tranches are credited.",
        "tip_ta": "அடுத்த தவணைகள் வரவு வைக்கப்படும் முன் மானியங்கள் கடுமையான செயல்திறன் ஆய்வுக்கு உட்படுத்தப்படுகின்றன.",
        "fact_en": "e-GramSwaraj and PriyaSoft portals ensure public tracking of all local spending.",
        "fact_ta": "e-GramSwaraj தளம் அனைத்து உள்ளாட்சி செலவுகளையும் பொதுமக்கள் கண்காணிப்பதை உறுதி செய்கிறது."
    },
    # 24
    {
        "subtopic": "Statutory Disqualifications under 1951 Act",
        "intro_en": "Match List-I (Statutory Disqualification Ground) with List-II (Legal Rationale under Section 5) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (சட்டப்பூர்வ தகுதியிழப்பு காரணம்) பட்டியல்-II உடன் (பிரிவு 5-ன் கீழான சட்ட நியாயம்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": [
            "Unsoundness of Mind",
            "Un-discharged Insolvent",
            "Moral Turpitude Conviction",
            "Prejudicial Financial Interest"
        ],
        "list1_ta": [
            "மனநலம் குன்றிய நிலை",
            "திவால் நிலை நீங்காதவர்",
            "ஒழுக்கக்கேடான குற்றத் தண்டனை",
            "சார்பு ஏற்படுத்தும் நிதி ஆர்வம்"
        ],
        "list2_en": [
            "Inability to exercise sound intellectual judgment on macroeconomic policy",
            "Financial vulnerability and compromised personal economic standing",
            "Erosion of moral integrity and public trust required for constitutional office",
            "Potential conflict of interest likely to compromise impartiality as a member"
        ],
        "list2_ta": [
            "பேரியல் பொருளாதார கொள்கைகளில் விவேகமான தீர்ப்பை வழங்க இயலாமை",
            "நிதி ரீதியான பாதிப்பு மற்றும் பலவீனமான தனிப்பட்ட பொருளாதார நிலை",
            "அரசியலமைப்புப் பதவிக்குத் தேவையான தார்மீக ஒருமைப்பாடு மற்றும் பொது நம்பிக்கையின்மை",
            "உறுப்பினரின் நடுநிலைமையை பாதிக்கக்கூடிய சாத்தியமான நல முரண்பாடு"
        ],
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "Section 5 of the Finance Commission Act 1951 lists these four specific grounds of disqualification to guarantee the moral authority and objectivity of the Commission.",
        "exp_ta": "1951 நிதி ஆணையச் சட்டத்தின் பிரிவு 5 ஆணையத்தின் தார்மீக அதிகாரம் மற்றும் நடுநிலைமையை உறுதி செய்ய இந்த நான்கு தகுதியிழப்புகளைப் பட்டியலிடுகிறது.",
        "tip_en": "These disqualifications apply both at initial appointment and during continuing tenure.",
        "tip_ta": "இத்தகுதியிழப்புகள் ஆரம்ப நியமனத்தின் போதும் பதவியில் தொடரும் போதும் பொருந்தும்.",
        "fact_en": "A member must disclose all personal business and investment interests before taking office.",
        "fact_ta": "பதவியேற்பதற்கு முன் ஒரு உறுப்பினர் தனது அனைத்து வணிக மற்றும் முதலீட்டு நலன்களையும் வெளிப்படுத்த வேண்டும்."
    },
    # 25
    {
        "subtopic": "Sixteenth Finance Commission Profile",
        "intro_en": "Match List-I (Sixteenth Finance Commission Dimension) with List-II (Specific Operational Feature) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (பதினாறாவது நிதி ஆணைய பரிமாணம்) பட்டியல்-II உடன் (குறிப்பிட்ட செயல்பாட்டு அம்சம்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": [
            "Chairman",
            "Date of Presidential Notification",
            "Report Submission Deadline",
            "Five-Year Operating Award Period"
        ],
        "list1_ta": [
            "தலைவர்",
            "குடியரசுத் தலைவர் அறிவிக்கை தேதி",
            "அறிக்கை சமர்ப்பிப்பதற்கான காலக்கெடு",
            "ஐந்தாண்டு செயல்பாட்டுப் பரிந்துரைக் காலம்"
        ],
        "list2_en": [
            "Dr. Arvind Panagariya (Former Vice Chairman, NITI Aayog)",
            "December 31, 2023",
            "October 31, 2025",
            "April 1, 2026 to March 31, 2031"
        ],
        "list2_ta": [
            "டாக்டர் அரவிந்த் பனகாரியா (முன்னாள் துணைத் தலைவர், நிதி ஆயோக்)",
            "டிசம்பர் 31, 2023",
            "அக்டோபர் 31, 2025",
            "ஏப்ரல் 1, 2026 முதல் மார்ச் 31, 2031 வரை"
        ],
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "16th FC is chaired by Dr. Arvind Panagariya; constituted on December 31, 2023; report due by October 31, 2025; award period spans 2026 to 2031.",
        "exp_ta": "16வது நிதி ஆணையத்திற்கு டாக்டர் அரவிந்த் பனகாரியா தலைமை தாங்குகிறார்; டிசம்பர் 31, 2023-ல் அமைக்கப்பட்டது; அறிக்கை அக்டோபர் 31, 2025-க்குள் தாக்கல் செய்யப்பட வேண்டும்; செயல்படும் காலம் 2026 முதல் 2031 வரை.",
        "tip_en": "Ritvik Ranjanam Pandey was appointed Secretary to the 16th Finance Commission.",
        "tip_ta": "ரித்விக் ரஞ்சனம் பாண்டே 16வது நிதி ஆணையத்தின் செயலாளராக நியமிக்கப்பட்டார்.",
        "fact_en": "The 16th FC will govern tax devolution during India's transition towards a 5-trillion-dollar economy.",
        "fact_ta": "இந்தியா 5 டிரில்லியன் டாலர் பொருளாதாரத்தை நோக்கி நகரும் காலகட்டத்தில் 16வது ஆணையம் வரிப் பகிர்வை நிர்வகிக்கும்."
    }
]

def generate_match_options(correct_mapping):
    correct_str = f"a-{correct_mapping[0]}, b-{correct_mapping[1]}, c-{correct_mapping[2]}, d-{correct_mapping[3]}"
    d1 = f"a-{correct_mapping[1]}, b-{correct_mapping[0]}, c-{correct_mapping[3]}, d-{correct_mapping[2]}"
    d2 = f"a-{correct_mapping[2]}, b-{correct_mapping[3]}, c-{correct_mapping[0]}, d-{correct_mapping[1]}"
    d3 = f"a-{correct_mapping[3]}, b-{correct_mapping[2]}, c-{correct_mapping[1]}, d-{correct_mapping[0]}"
    return [correct_str, d1, d2, d3]

def build_questions():
    # 25 questions: 7 A, 6 B, 6 C, 6 D
    key_assignment = ["A", "B", "C", "D", "A", "B", "C", "D", "A", "B", "C", "D",
                      "A", "B", "C", "D", "A", "B", "C", "D", "A", "B", "C", "D", "A"]
    questions = []
    for idx, item in enumerate(raw_match_data, start=1):
        qid = f"FC_MF_{idx:03d}"
        correct_key = key_assignment[idx - 1]
        
        stem_en = (
            f"{item['intro_en']}\n"
            f"List-I:\n"
            f"a. {item['list1_en'][0]}\n"
            f"b. {item['list1_en'][1]}\n"
            f"c. {item['list1_en'][2]}\n"
            f"d. {item['list1_en'][3]}\n"
            f"List-II:\n"
            f"1. {item['list2_en'][0]}\n"
            f"2. {item['list2_en'][1]}\n"
            f"3. {item['list2_en'][2]}\n"
            f"4. {item['list2_en'][3]}"
        )
        stem_ta = (
            f"{item['intro_ta']}\n"
            f"பட்டியல்-I:\n"
            f"a. {item['list1_ta'][0]}\n"
            f"b. {item['list1_ta'][1]}\n"
            f"c. {item['list1_ta'][2]}\n"
            f"d. {item['list1_ta'][3]}\n"
            f"பட்டியல்-II:\n"
            f"1. {item['list2_ta'][0]}\n"
            f"2. {item['list2_ta'][1]}\n"
            f"3. {item['list2_ta'][2]}\n"
            f"4. {item['list2_ta'][3]}"
        )
        
        all_opts = generate_match_options(item["correct_mapping"])
        key_to_pos = {"A": 0, "B": 1, "C": 2, "D": 3}
        target_pos = key_to_pos[correct_key]
        
        arranged_opts = list(all_opts[1:])
        arranged_opts.insert(target_pos, all_opts[0])
        correct_opt_str = arranged_opts[target_pos]
        
        why_en = {}
        why_ta = {}
        for k_idx, k in enumerate(["A", "B", "C", "D"]):
            if k == correct_key:
                why_en[k] = f"Option {k} ({arranged_opts[k_idx]}) is the correct matching: {item['exp_en']}"
                why_ta[k] = f"தெரிவு {k} ({arranged_opts[k_idx]}) சரியான பொருத்தம்: {item['exp_ta']}"
            else:
                why_en[k] = f"Option {k} ({arranged_opts[k_idx]}) contains incorrect pairings."
                why_ta[k] = f"தெரிவு {k} ({arranged_opts[k_idx]}) தவறான பொருத்தங்களைக் கொண்டுள்ளது."
                
        q = make_fc_q(
            qid=qid,
            diff="Medium",
            qtype="Match the Following",
            subtopic=item["subtopic"],
            en_stem=stem_en,
            ta_stem=stem_ta,
            en_a=arranged_opts[0],
            ta_a=arranged_opts[0],
            en_b=arranged_opts[1],
            ta_b=arranged_opts[1],
            en_c=arranged_opts[2],
            ta_c=arranged_opts[2],
            en_d=arranged_opts[3],
            ta_d=arranged_opts[3],
            correct_key=correct_key,
            exp_en=f"The correct match is {correct_opt_str}.\n{item['exp_en']}",
            exp_ta=f"சரியான பொருத்தம்: {correct_opt_str}.\n{item['exp_ta']}",
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
            tags=["polity", "finance_commission", "match_the_following", item["subtopic"].lower().replace(" ", "_")]
        )
        questions.append(q)
    return questions

if __name__ == "__main__":
    qs = build_questions()
    print(f"Generated {len(qs)} raw Match the Following questions for Finance Commission.")
    assert len(qs) == 25, f"Expected 25 questions, got {len(qs)}"
    
    out_path = os.path.join("data", "questions", "polity", "fc_match_the_following.json")
    alias_path = os.path.join("data", "questions", "polity", "fc_match.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, ensure_ascii=False, indent=2)
    shutil.copyfile(out_path, alias_path)
    print(f"Saved Match the Following MCQs to {out_path} and alias {alias_path}")
    
    val = ContentValidator()
    report = val.validate_file(out_path, expected_count=25, expected_prefix="FC_MF_")
    print(f"Validation Report: {'PASS' if report.is_valid else 'FAIL'} | Total: {report.total_audited}")
    if not report.is_valid:
        for iss in report.issues[:10]:
            print(f"  Issue: {iss}")
    print(f"Key Distribution: {report.key_distribution}")
