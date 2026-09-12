# -*- coding: utf-8 -*-
"""
Build 50 Medium MCQs for Finance Commission of India
ID range: FC_M_001 to FC_M_050
"""

import json
import os
from fc_mcq_helper import make_fc_q
from rebalance_er_helper import balance_question_keys
from tools.nova_content_engine.validator import ContentValidator

raw_medium_data = [
    # 1
    {
        "subtopic": "Quasi-Judicial Civil Court Procedures",
        "stem_en": "Under Section 8 of the Finance Commission (Miscellaneous Provisions) Act 1951, what specific evidentiary power does the Commission possess while summoning witnesses?",
        "stem_ta": "1951 நிதி ஆணையச் சட்டத்தின் பிரிவு 8-ன் கீழ், சாட்சிகளை அழைக்கும் போது ஆணையத்திற்கு உள்ள குறிப்பிட்ட சாட்சிய அதிகாரம் என்ன?",
        "options": [
            ("Power to summon and enforce the attendance of any witness and examine him on oath", "எந்தவொரு சாட்சியையும் நேரில் ஆஜராக அழைப்பாணை அனுப்பவும், உறுதிமொழியின் கீழ் விசாரிக்கவும் அதிகாரம்"),
            ("Power to detain uncooperative departmental secretaries in civil prison", "ஒத்துழைக்காத துறைச் செயலாளர்களை சிவில் சிறையில் அடைக்கும் அதிகாரம்"),
            ("Power to attach and freeze state government consolidated bank accounts", "மாநில அரசின் திரட்டப்பட்ட வங்கிக் கணக்குகளை முடக்கும் அதிகாரம்"),
            ("Power to initiate criminal contempt proceedings in the High Court directly", "உயர் நீதிமன்றத்தில் நேரடியாக குற்றவியல் நீதிமன்ற அவமதிப்பு வழக்குகளைத் தொடங்கும் அதிகாரம்")
        ],
        "exp_en": "Section 8(a) of the Finance Commission Act 1951 explicitly confers the power of 'summoning and enforcing the attendance of any person and examining him on oath'.",
        "exp_ta": "1951 நிதி ஆணையச் சட்டத்தின் பிரிவு 8(a), 'எந்தவொரு நபரையும் ஆஜராக அழைப்பாணை அனுப்பவும், உறுதிமொழியின் பேரில் அவரை விசாரிக்கவும்' ஆணையத்திற்கு அதிகாரம் அளிக்கிறது.",
        "tip_en": "Civil court powers under CPC: summoning on oath, discovery of documents, receiving affidavits.",
        "tip_ta": "சிவில் நீதிமன்ற அதிகாரங்கள்: பிரமாணத்தின் கீழ் விசாரணை, ஆவணங்களை வெளிப்படுத்தக் கோருதல், வாக்குமூலங்களைப் பெறுதல்.",
        "fact_en": "Proceedings before the Finance Commission are deemed to be judicial proceedings under IPC Section 193.",
        "fact_ta": "நிதி ஆணையத்தின் முன் நடக்கும் நடவடிக்கைகள் இந்திய தண்டனைச் சட்டம் 193-ன் கீழ் நீதித்துறை நடவடிக்கைகளாகக் கருதப்படுகின்றன."
    },
    # 2
    {
        "subtopic": "Statutory Disqualification under Section 5",
        "stem_en": "Which of the following conditions mandates the disqualification of a member of the Finance Commission under the 1951 Act?",
        "stem_ta": "1951 சட்டத்தின் கீழ் நிதி ஆணைய உறுப்பினர் ஒருவரை தகுதியிழப்பு செய்ய கட்டாயப்படுத்தும் நிபந்தனை எது?",
        "options": [
            ("Having such financial or other interest as is likely to affect prejudicially his functions as a member", "உறுப்பினராக தனது பணிகளை பாரபட்சமாக பாதிக்கக்கூடிய நிதி அல்லது பிற நலன்களைக் கொண்டிருத்தல்"),
            ("Being an active member of a recognized international economic association", "அங்கீகரிக்கப்பட்ட சர்வதேச பொருளாதார அமைப்பில் செயலில் உள்ள உறுப்பினராக இருத்தல்"),
            ("Having previously served as a member of the State Planning Board", "முன்னர் மாநில திட்டக் குழுவின் உறுப்பினராகப் பணியாற்றியிருத்தல்"),
            ("Holding an honorary doctorate from a central university", "மத்தியப் பல்கலைக்கழகத்தில் கௌரவ முனைவர் பட்டம் பெற்றிருத்தல்")
        ],
        "exp_en": "Under Section 5(d) of the Finance Commission Act 1951, a person is disqualified if he 'has such financial or other interest as is likely to affect prejudicially his functions as a member of the Commission'.",
        "exp_ta": "1951 நிதி ஆணையச் சட்டத்தின் பிரிவு 5(d)-ன் படி, ஆணையத்தின் உறுப்பினராக தனது பணிகளை பாரபட்சமாக பாதிக்கக்கூடிய நிதி அல்லது பிற நலன்களைக் கொண்டிருந்தால் அவர் தகுதியிழப்பு செய்யப்படுவார்.",
        "tip_en": "Conflict of financial interest is a statutory disqualification under Section 5(d).",
        "tip_ta": "நிதி நலன் முரண்பாடு என்பது பிரிவு 5(d)-ன் கீழான சட்டப்பூர்வ தகுதியிழப்பாகும்.",
        "fact_en": "Members must submit a written declaration regarding the absence of conflicting personal investments.",
        "fact_ta": "முரண்பட்ட தனிப்பட்ட முதலீடுகள் இல்லை என உறுப்பினர்கள் எழுத்துப்பூர்வ உறுதிமொழி அளிக்க வேண்டும்."
    },
    # 3
    {
        "subtopic": "Vertical Devolution Adjustment for J&K (15th FC)",
        "stem_en": "Why did the 15th Finance Commission reduce the vertical tax devolution to States from 42% (recommended by 14th FC) to 41%?",
        "stem_ta": "மாநிலங்களுக்கான செங்குத்து வரிப் பகிர்வை 14வது ஆணையத்தின் 42%-லிருந்து 41%-ஆக 15வது நிதி ஆணையம் ஏன் குறைத்தது?",
        "options": [
            ("To provide 1% allocation for the newly created Union Territories of Jammu & Kashmir and Ladakh from the Centre's resources", "மத்திய அரசின் நிதியிலிருந்து புதிதாக உருவாக்கப்பட்ட ஜம்மு காஷ்மீர் மற்றும் லடாக் யூனியன் பிரதேசங்களுக்கு 1% ஒதுக்கீடு செய்வதற்காக"),
            ("To meet the escalating interest expenditure on central sovereign green bonds", "மத்திய அரசின் பசுமைப் பத்திரங்கள் மீதான வட்டிச் செலவை ஈடுகட்டுவதற்காக"),
            ("Due to a permanent 1% constitutional cut imposed by the GST Council", "ஜி.எஸ்.டி கவுன்சிலால் விதிக்கப்பட்ட நிரந்தர 1% அரசியலமைப்பு வெட்டு காரணமாக"),
            ("To fund the establishment of regional benches of the Supreme Court", "உச்ச நீதிமன்றத்தின் பிராந்திய அமர்வுகளை அமைப்பதற்கு நிதியளிக்க")
        ],
        "exp_en": "Following the Jammu and Kashmir Reorganisation Act 2019, the former State was reconstituted into two Union Territories. Since Union Territories are funded directly by the Central Government, the States' divisible pool was recalibrated by 1% from 42% to 41%.",
        "exp_ta": "2019 ஜம்மு காஷ்மீர் மறுசீரமைப்புச் சட்டத்திற்குப் பிறகு, முன்னாள் மாநிலம் இரண்டு யூனியன் பிரதேசங்களாக மாற்றப்பட்டது. யூனியன் பிரதேசங்களுக்கு மத்திய அரசு நேரடியாக நிதியளிப்பதால், மாநிலங்களின் பகிர்வு நிதி 42%-லிருந்து 41%-ஆக 1% குறைக்கப்பட்டது.",
        "tip_en": "42% - 1% = 41%. The 1% roughly equals the historical share of the erstwhile State of J&K.",
        "tip_ta": "42% - 1% = 41%. இந்த 1% என்பது முந்தைய ஜம்மு காஷ்மீர் மாநிலத்தின் தோராயமான பங்கிற்கு சமமாகும்.",
        "fact_en": "This 41% recommendation applied to both the 2020-21 interim report and the 2021-26 main report.",
        "fact_ta": "இந்த 41% பரிந்துரை 2020-21 இடைக்கால அறிக்கை மற்றும் 2021-26 முக்கிய அறிக்கை ஆகிய இரண்டிற்கும் பொருந்தும்."
    },
    # 4
    {
        "subtopic": "Terms of Reference Controversies (15th FC)",
        "stem_en": "What was the major point of controversy raised by several southern States regarding the Terms of Reference (ToR) of the 15th Finance Commission?",
        "stem_ta": "15வது நிதி ஆணையத்தின் பணிக் குறிப்புகள் (ToR) தொடர்பாக பல தென் மாநிலங்களால் எழுப்பப்பட்ட முக்கிய சர்ச்சை என்ன?",
        "options": [
            ("Mandating the use of 2011 Census population data instead of 1971 Census data", "1971 கணக்கெடுப்புத் தரவுகளுக்குப் பதிலாக 2011 மக்கள் தொகை கணக்கெடுப்புத் தரவை கட்டாயமாக்கியது"),
            ("Abolishing statutory revenue deficit grants under Article 275 entirely", "சரத்து 275-ன் கீழான சட்டப்பூர்வ வருவாய்ப் பற்றாக்குறை மானியங்களை முற்றிலும் ரத்து செய்தது"),
            ("Transferring all local body grant administration to private commercial banks", "அனைத்து உள்ளாட்சி மானிய நிர்வாகத்தையும் தனியார் வணிக வங்கிகளுக்கு மாற்றியது"),
            ("Restricting state borrowing limits under Article 293 to 1% of GSDP", "சரத்து 293-ன் கீழ் மாநிலக் கடன் வரம்பை GSDP-ல் 1% ஆகக் கட்டுப்படுத்தியது")
        ],
        "exp_en": "From the 8th to 14th Commissions, population of 1971 was primarily used to avoid penalizing states that controlled population. The 15th FC's ToR mandated using 2011 Census data, prompting concerns that progressive states would suffer major revenue losses.",
        "exp_ta": "8வது முதல் 14வது ஆணையம் வரை, மக்கள் தொகையைக் கட்டுப்படுத்திய மாநிலங்கள் பாதிக்கப்படாமல் இருக்க 1971 மக்கள் தொகை பயன்படுத்தப்பட்டது. 15வது ஆணையம் 2011 கணக்கெடுப்பைப் பயன்படுத்த கட்டளையிட்டதால் தென் மாநிலங்கள் நிதி இழப்பை சந்திக்கும் என்ற சர்ச்சை எழுந்தது.",
        "tip_en": "1971 Census (used for decades) vs 2011 Census (mandated for 15th FC).",
        "tip_ta": "பல தசாப்தங்களாகப் பயன்படுத்தப்பட்ட 1971 கணக்கெடுப்பு vs 15வது ஆணையத்திற்கு கட்டாயமாக்கப்பட்ட 2011 கணக்கெடுப்பு.",
        "fact_en": "To balance this, the 15th FC introduced the 'Demographic Performance' criterion (12.5% weight).",
        "fact_ta": "இதை சமன் செய்யவே 15வது நிதி ஆணையம் 12.5% எடையுடன் 'மக்கள்தொகை செயல்திறன்' அளவுகோலை அறிமுகப்படுத்தியது."
    },
    # 5
    {
        "subtopic": "Modernisation Fund for Defence and Internal Security (MFDIS)",
        "stem_en": "What innovative funding mechanism was recommended by the 15th Finance Commission in its final report?",
        "stem_ta": "15வது நிதி ஆணையம் தனது இறுதி அறிக்கையில் பரிந்துரைத்த புதுமையான நிதி வழிமுறை எது?",
        "options": [
            ("Modernisation Fund for Defence and Internal Security (MFDIS) as a non-lapsable dedicated fund", "காலாவதியாகாத பிரத்யேக நிதியாக பாதுகாப்பு மற்றும் உள்நாட்டுப் பாதுகாப்பு நவீனமயமாக்கல் நிதி (MFDIS)"),
            ("A permanent National Highway construction cess shared equally with municipalities", "நகராட்சிகளுடன் சமமாகப் பகிரப்படும் நிரந்தர தேசிய நெடுஞ்சாலை செஸ் வரி"),
            ("A dedicated space exploration surcharge on all commercial telecommunications", "அனைத்து வணிக தொலைத்தொடர்புகளிலும் விண்வெளி ஆராய்ச்சிக்கான பிரத்யேக கூடுதல் வரி"),
            ("A sovereign gold reserve pool placed under the joint custody of State Finance Ministers", "மாநில நிதி அமைச்சர்களின் கூட்டுப் பொறுப்பில் வைக்கப்படும் இறையாண்மை தங்க இருப்பு நிதி")
        ],
        "exp_en": "Under an additional Terms of Reference, the 15th FC recommended establishing the 'Modernisation Fund for Defence and Internal Security' (MFDIS) with an indicative corpus of Rs. 2.38 lakh crore over 2021-2026, financed partly by transfers from CFI and disinvestment proceeds.",
        "exp_ta": "கூடுதல் பணிக் குறிப்பின் கீழ், 15வது நிதி ஆணையம் 2021-2026 காலத்தில் ரூ. 2.38 லட்சம் கோடி உத்தேச நிதியுடன் காலாவதியாகாத 'பாதுகாப்பு மற்றும் உள்நாட்டுப் பாதுகாப்பு நவீனமயமாக்கல் நிதியை' (MFDIS) அமைக்க பரிந்துரைத்தது.",
        "tip_en": "MFDIS = Dedicated non-lapsable fund for military and internal security capital modernization.",
        "tip_ta": "MFDIS = ராணுவ மற்றும் உள்நாட்டுப் பாதுகாப்பு மூலதன நவீனமயமாக்கலுக்கான காலாவதியாகாத நிதி.",
        "fact_en": "State governments raised concerns that this fund should not be created by reducing the divisible tax pool.",
        "fact_ta": "பகிர்வு வரி நிதியைக் குறைத்து இந்த நிதியை உருவாக்கக் கூடாது என மாநில அரசுகள் வலியுறுத்தின."
    },
    # 6
    {
        "subtopic": "Income Distance Calculation Methodology",
        "stem_en": "How is the 'Income Distance' of a State calculated in the Finance Commission's horizontal devolution formula?",
        "stem_ta": "நிதி ஆணையத்தின் கிடைமட்ட வரிப் பகிர்வு சூத்திரத்தில் ஒரு மாநிலத்தின் 'வருமான இடைவெளி' எவ்வாறு கணக்கிடப்படுகிறது?",
        "options": [
            ("Distance of the State's per capita GSDP from the State having the highest per capita GSDP", "அதிகபட்ச தனிநபர் GSDP கொண்ட மாநிலத்தின் தனிநபர் வருமானத்திலிருந்து குறிப்பிட்ட மாநிலத்தின் தனிநபர் GSDP-க்கான இடைவெளி"),
            ("Distance between the state capital and the national capital in physical railway track kilometers", "மாநிலத் தலைநகருக்கும் தேசியத் தலைநகருக்கும் இடையே உள்ள ரயில்வே தண்டவாள தூரம்"),
            ("The gap between total state revenue expenditure and total capital borrowings", "மாநிலத்தின் மொத்த வருவாய் செலவினத்திற்கும் மூலதனக் கடன்களுக்கும் இடையே உள்ள இடைவெளி"),
            ("The difference between state literacy rate and the national average literacy rate", "மாநில எழுத்தறிவு விகிதத்திற்கும் தேசிய சராசரி எழுத்தறிவு விகிதத்திற்கும் இடையே உள்ள வேறுபாடு")
        ],
        "exp_en": "Income Distance is the difference between the per capita Gross State Domestic Product (GSDP) of a State from that of the benchmark State with the highest per capita GSDP (often Goa or Haryana). Lower per capita income states get a higher share to ensure equity.",
        "exp_ta": "வருமான இடைவெளி என்பது அதிக தனிநபர் வருமானம் கொண்ட ஒப்பீட்டு மாநிலத்தின் தனிநபர் GSDP-லிருந்து குறிப்பிட்ட மாநிலத்தின் தனிநபர் GSDP-க்கு உள்ள வித்தியாசமாகும். குறைந்த வருமானம் கொண்ட பின்தங்கிய மாநிலங்களுக்கு சமத்துவத்தை உறுதி செய்ய அதிக பங்கு கிடைக்கிறது.",
        "tip_en": "Higher income distance = Higher allocation. Formula: (Benchmark per capita GSDP - State per capita GSDP) * Population.",
        "tip_ta": "அதிக வருமான இடைவெளி = அதிக நிதி ஒதுக்கீடு. இது பின்தங்கிய மாநிலங்களுக்கு நிதி மறுபகிர்வை வழங்குகிறது.",
        "fact_en": "To prevent extreme distortion, small states like Goa and Sikkim are sometimes given special benchmark treatments.",
        "fact_ta": "தீவிர விலகல்களைத் தவிர்க்க கோவா மற்றும் சிக்கிம் போன்ற சிறிய மாநிலங்களுக்கு சிறப்பு ஒப்பீட்டு முறைகள் கையாளப்படுகின்றன."
    },
    # 7
    {
        "subtopic": "Local Body Grants: Tied vs Untied (15th FC)",
        "stem_en": "How did the 15th Finance Commission structure the grants allocated to Rural Local Bodies (Panchayats)?",
        "stem_ta": "கிராமப்புற உள்ளாட்சி அமைப்புகளுக்கு (பஞ்சாயத்துகள்) ஒதுக்கப்பட்ட மானியங்களை 15வது நிதி ஆணையம் எவ்வாறு கட்டமைத்தது?",
        "options": [
            ("Divided into 40% Untied (Basic) grants and 60% Tied grants for sanitation and drinking water", "40% நிபந்தனையற்ற (அடிப்படை) மானியங்கள் மற்றும் சுகாதாரம், குடிநீருக்கான 60% நிபந்தனைக்குட்பட்ட மானியங்கள்"),
            ("100% untied cash transfers to be spent on local government staff salaries", "உள்ளாட்சி ஊழியர்களின் ஊதியத்திற்காக செலவிடப்பட வேண்டிய 100% நிபந்தனையற்ற பணப் பரிமாற்றம்"),
            ("Disbursed only as repayable microfinance loans to women self-help groups", "பெண்கள் சுயஉதவிக் குழுக்களுக்கு திரும்பச் செலுத்த வேண்டிய நுண்கடன்களாக மட்டுமே விநியோகிப்பது"),
            ("Exclusively allocated for constructing multi-storey commercial office towers", "பல அடுக்கு வணிக அலுவலகக் கோபுரங்களைக் கட்டுவதற்கு மட்டுமே பிரத்யேகமாக ஒதுக்கப்பட்டது")
        ],
        "exp_en": "The 15th FC recommended that 60% of Panchayat grants be 'Tied' to national priorities—namely sanitation, maintenance of ODF status, supply of drinking water, rainwater harvesting, and water recycling—and 40% be 'Untied' for local discretionary needs.",
        "exp_ta": "15வது நிதி ஆணையம் பஞ்சாயத்து மானியங்களில் 60%-ஐ சுகாதாரம், திறந்தவெளி கழிப்பிடமற்ற நிலையைப் பராமரித்தல், குடிநீர் வழங்கல் மற்றும் மழைநீர் சேகரிப்பு போன்ற தேசிய முன்னுரிமைகளுடன் இணைத்தது; 40%-ஐ உள்ளூர் விருப்பத் தேவைகளுக்கான நிபந்தனையற்ற மானியமாக வழங்கியது.",
        "tip_en": "Rural Local Body Grants: 40% Untied (basic services) : 60% Tied (water and sanitation).",
        "tip_ta": "ஊரக உள்ளாட்சி மானியங்கள்: 40% நிபந்தனையற்றவை : 60% நிபந்தனைக்குட்பட்டவை (குடிநீர் & சுகாதாரம்).",
        "fact_en": "Tied grants cannot be used for salaries or establishment expenses of Panchayats.",
        "fact_ta": "நிபந்தனைக்குட்பட்ட மானியங்களை பஞ்சாயத்து ஊழியர்களின் ஊதியத்திற்கோ நிர்வாகச் செலவுகளுக்கோ பயன்படுத்த முடியாது."
    },
    # 8
    {
        "subtopic": "Urban Local Body Grants Classification",
        "stem_en": "How did the 15th Finance Commission differentiate grants for Urban Local Bodies (ULBs)?",
        "stem_ta": "நகர்ப்புற உள்ளாட்சி அமைப்புகளுக்கான (ULBs) மானியங்களை 15வது நிதி ஆணையம் எவ்வாறு வகைப்படுத்தியது?",
        "options": [
            ("Differentiated between Million-Plus Cities (100% performance-linked) and Non-Million-Plus Cities (40% untied, 60% tied)", "பத்து லட்சத்திற்கும் அதிக மக்கள் தொகை கொண்ட நகரங்கள் (100% செயல்திறன் சார்ந்தது) மற்றும் பிற நகரங்கள் (40% நிபந்தனையற்றது, 60% நிபந்தனைக்குட்பட்டது) எனப் பிரித்தது"),
            ("Treated all municipalities identically regardless of population size", "மக்கள் தொகை அளவைக் கணக்கில் கொள்ளாமல் அனைத்து நகராட்சிகளையும் ஒரே மாதிரியாக நடத்தியது"),
            ("Granted funds exclusively to smart cities having metro rail systems", "மெட்ரோ ரயில் வசதி கொண்ட ஸ்மார்ட் நகரங்களுக்கு மட்டுமே நிதி வழங்கியது"),
            ("Restricted urban grants only to port cities handling maritime exports", "கடல்வழி ஏற்றுமதி செய்யும் துறைமுக நகரங்களுக்கு மட்டுமே நகர்ப்புற மானியங்களை மட்டுப்படுத்தியது")
        ],
        "exp_en": "For 42 Urban Agglomerations with a population of over one million, grants are 100% performance-linked to air quality improvements, drinking water supply, and solid waste management. For other cities, grants follow a 40:60 untied:tied structure.",
        "exp_ta": "பத்து லட்சத்திற்கும் அதிகமான மக்கள் தொகை கொண்ட 42 பெருநகரப் பகுதிகளுக்கு காற்றின் தரம், குடிநீர் மற்றும் திடக்கழிவு மேலாண்மை ஆகிய செயல்திறன் அடிப்படையில் 100% மானியம் இணைக்கப்பட்டது. பிற சிறிய நகரங்களுக்கு 40% நிபந்தனையற்றது, 60% நிபந்தனைக்குட்பட்டது என்ற கட்டமைப்பு பின்பற்றப்பட்டது.",
        "tip_en": "Million-Plus Cities: 100% performance-linked grants through Million-Plus Challenge Fund.",
        "tip_ta": "பத்து லட்சத்திற்கு மேற்பட்ட பெருநகரங்கள்: 100% செயல்திறன் சார்ந்த மானியங்கள்.",
        "fact_en": "NCAP air quality targets determine payouts from the Million-Plus Cities Challenge Fund.",
        "fact_ta": "NCAP காற்றின் தர இலக்குகளை எட்டுவதே பெருநகரங்களுக்கான மானியத் தொகையைத் தீர்மானிக்கிறது."
    },
    # 9
    {
        "subtopic": "Primacy: Finance Commission vs Planning Commission History",
        "stem_en": "In the historical balance of Indian fiscal federalism before 2015, what led to the weakening of the constitutional Finance Commission's primacy?",
        "stem_ta": "2015-க்கு முந்தைய இந்திய நிதி கூட்டாட்சியில், அரசியலமைப்பு நிதி ஆணையத்தின் முதன்மைத் தன்மை பலவீனமடைய வழிவகுத்தது எது?",
        "options": [
            ("The extra-constitutional Planning Commission disbursing massive discretionary plan grants and loans under Article 282", "அரசியலமைப்பில் இல்லாத திட்டக் குழு சரத்து 282-ன் கீழ் பெரும் விருப்பத் திட்ட மானியங்களையும் கடன்களையும் வழங்கியது"),
            ("The abolition of Article 280 during the Internal Emergency of 1975", "1975 உள்நாட்டு நெருக்கடி நிலையின் போது சரத்து 280 ரத்து செய்யப்பட்டது"),
            ("The Supreme Court declaring Finance Commission awards unconstitutional", "நிதி ஆணையப் பரிந்துரைகளை உச்ச நீதிமன்றம் அரசியலமைப்புக்கு எதிரானது என அறிவித்தது"),
            ("A constitutional amendment placing all tax powers under the President's Secretariat", "அனைத்து வரி அதிகாரங்களையும் குடியரசுத் தலைவர் செயலகத்தின் கீழ் கொண்டு வந்த அரசியலமைப்புத் திருத்தம்")
        ],
        "exp_en": "Until its abolition in 2014, the non-constitutional Planning Commission overshadowed the Finance Commission by controlling Plan expenditure, capital grants, and central assistance under Article 282, reducing the Finance Commission's role largely to non-plan revenue expenditure.",
        "exp_ta": "2014-ல் கலைக்கப்படும் வரை, அரசியலமைப்பில் இல்லாத திட்டக் குழு சரத்து 282-ன் கீழ் திட்டச் செலவுகள், மூலதன மானியங்கள் மற்றும் மத்திய உதவிகளைக் கட்டுப்படுத்தி நிதி ஆணையத்தை விட அதிக ஆதிக்கம் செலுத்தியது; இது நிதி ஆணையத்தின் பங்கை திட்டமில்லா வருவாய் செலவுகளுக்கு மட்டுப்படுத்தியது.",
        "tip_en": "Finance Commission = Constitutional body (Art 280). Planning Commission = Extra-constitutional cabinet creation.",
        "tip_ta": "நிதி ஆணையம் = அரசியலமைப்பு அமைப்பு (சரத்து 280). திட்டக் குழு = அமைச்சரவை தீர்மானத்தால் உருவான அமைப்பு.",
        "fact_en": "With the abolition of Planning Commission and creation of NITI Aayog, Finance Commission's constitutional primacy was restored.",
        "fact_ta": "திட்டக் குழு கலைக்கப்பட்டு நிதி ஆயோக் அமைக்கப்பட்ட பிறகு நிதி ஆணையத்தின் அரசியலமைப்பு முதன்மை மீட்கப்பட்டது."
    },
    # 10
    {
        "subtopic": "14th Finance Commission Dramatic Shift",
        "stem_en": "What fundamental structural reform was introduced by the 14th Finance Commission under Dr. Y.V. Reddy?",
        "stem_ta": "டாக்டர் ஒய்.வி. ரெட்டி தலைமையிலான 14வது நிதி ஆணையத்தால் அறிமுகப்படுத்தப்பட்ட அடிப்படை கட்டமைப்பு சீர்திருத்தம் என்ன?",
        "options": [
            ("Substantial increase in untied tax devolution from 32% to 42%, drastically cutting discretionary tied grants to enhance state fiscal autonomy", "மாநிலங்களின் நிதி தன்னாட்சியை அதிகரிக்க நிபந்தனையற்ற வரிப் பகிர்வை 32%-லிருந்து 42%-ஆக கணிசமாக உயர்த்தி, நிபந்தனைக்குட்பட்ட விருப்ப மானியங்களைக் குறைத்தது"),
            ("Replacing all direct tax transfers with sovereign digital cryptocurrency tokens", "அனைத்து நேரடி வரிப் பரிமாற்றங்களையும் டிஜிட்டல் கிரிப்டோகரன்சி டோக்கன்களாக மாற்றியது"),
            ("Abolishing state sales tax departments and transferring all collection staff to the Union", "மாநில வணிக வரித் துறைகளை ரத்து செய்து அனைத்து ஊழியர்களையும் மத்திய அரசுக்கு மாற்றியது"),
            ("Restricting horizontal tax devolution strictly to states bordering international frontiers", "சர்வதேச எல்லைகளைக் கொண்ட மாநிலங்களுக்கு மட்டுமே கிடைமட்ட வரிப் பகிர்வை மட்டுப்படுத்தியது")
        ],
        "exp_en": "The 14th FC made a paradigm shift by enhancing vertical devolution from 32% to 42% (a 10 percentage point hike), giving States unconditional fiscal autonomy while recommending the curtailment of tied Centrally Sponsored Schemes (CSS).",
        "exp_ta": "14வது நிதி ஆணையம் செங்குத்து வரிப் பகிர்வை 32%-லிருந்து 42%-ஆக (10 சதவீதப் புள்ளி உயர்வு) வியத்தகு முறையில் உயர்த்தி, நிபந்தனைக்குட்பட்ட மத்திய திட்டங்களைக் குறைத்து மாநிலங்களுக்கு நிபந்தனையற்ற நிதி தன்னாட்சியை வழங்கியது.",
        "tip_en": "14th FC: 42% untied devolution = Major milestone in cooperative federalism.",
        "tip_ta": "14வது நிதி ஆணையம்: 42% நிபந்தனையற்ற வரிப் பகிர்வு = கூட்டுறவு கூட்டாட்சியின் முக்கிய மைல்கல்.",
        "fact_en": "The Union Government accepted this 42% devolution recommendation in full starting 2015-16.",
        "fact_ta": "மத்திய அரசு 2015-16 முதல் இந்த 42% வரிப் பகிர்வுப் பரிந்துரையை முழுமையாக ஏற்றுக்கொண்டது."
    }
]

# We will generate questions 11 to 50 covering rich empirical and constitutional concepts
more_medium_items = [
    ("Alternative Devolution Scheme Origins", "What was the initial sharing percentage of central taxes recommended by the 10th Finance Commission under the Alternative Scheme?", "29% of the gross proceeds of almost all Union taxes", "ஏறத்தாழ அனைத்து மத்திய வரிகளின் மொத்த வருவாயில் 29%", "10th FC (K.C. Pant) recommended 29% pooling, codified by 80th Amendment 2000.", "10வது ஆணையம் 29% பகிர்வை பரிந்துரைத்தது; 80வது திருத்தம் இதை சட்டமாக்கியது.", "Prior to this, states received shares only from Income Tax and Basic Excise Duties.", "இதற்கு முன் மாநிலங்களுக்கு வருமான வரி மற்றும் கலால் வரியில் மட்டுமே பங்கு கிடைத்தது."),
    ("Fiscal Consolidation Targets (12th FC)", "What major fiscal consolidation benchmark was laid down by the 12th Finance Commission under Dr. C. Rangarajan?", "Mandating States to enact Fiscal Responsibility and Budget Management (FRBM) Acts to eliminate revenue deficits", "வருவாய்ப் பற்றாக்குறையை ஒழிக்க மாநிலங்கள் FRBM நிதிப் பொறுப்புடைமைச் சட்டங்களை இயற்றுவதை கட்டாயமாக்கியது", "Debt relief and interest waiver were made conditional on enacting state-level FRBM legislation.", "மாநில அளவிலான FRBM சட்டங்களை இயற்றுவது கடன் நிவாரணத்திற்கான நிபந்தனையாக்கப்பட்டது.", "Targeted reducing fiscal deficit to 3% of GSDP and zero revenue deficit by 2008-09.", "2008-09க்குள் நிதிப் பற்றாக்குறையை 3% ஆகவும் வருவாய்ப் பற்றாக்குறையை பூஜ்ஜியமாகவும் குறைக்க இலக்கு நிர்ணயிக்கப்பட்டது."),
    ("GST Compensation Grant Design (13th FC)", "What was the innovative incentive proposed by the 13th Finance Commission under Dr. Vijay Kelkar to persuade States to adopt GST?", "A Grand Bargain grant of Rs. 50,000 crore to compensate states for potential VAT revenue losses", "மதிப்புக் கூட்டு வரி இழப்பை ஈடுசெய்ய மாநிலங்களுக்கு ரூ. 50,000 கோடி மதிப்பிலான பெருந்திட்ட மானியம்", "13th FC laid the fiscal roadmap that eventually culminated in the 101st Amendment Act 2016.", "13வது நிதி ஆணையம் அமைத்த பாதையே 2016-ல் 101வது அரசியலமைப்புத் திருத்தச் சட்டமாக மலர்ந்தது.", "Recommended a flawless dual GST with minimal exemptions and comprehensive service tax base.", "குறைந்தபட்ச விலக்குகளுடன் கூடிய குறைபாடற்ற இரட்டை ஜி.எஸ்.டி முறையை பரிந்துரைத்தது."),
    ("Local Body Grant Conditionality: Audited Accounts", "What mandatory conditionality did the 15th Finance Commission impose on local bodies to become eligible for grants after 2022-23?", "Online availability of annual audited accounts and notification of floor property tax rates", "ஆண்டு தணிக்கைக் கணக்குகள் இணையத்தில் கிடைப்பது மற்றும் குறைந்தபட்ச சொத்து வரி விகிதங்களை அறிவிப்பது", "Incentivizes municipal fiscal transparency and local revenue self-reliance.", "நகராட்சிகளின் நிதி வெளிப்படைத்தன்மை மற்றும் உள்ளூர் வருவாய் தற்சார்பை இது ஊக்குவிக்கிறது.", "Panchayats and municipalities must upload audited accounts onto the AuditOnline platform.", "பஞ்சாயத்துகள் மற்றும் நகராட்சிகள் தணிக்கை செய்யப்பட்ட கணக்குகளை AuditOnline தளத்தில் பதிவேற்ற வேண்டும்."),
    ("Disaster Mitigation vs Response Allocations", "Under the SDRMF architecture recommended by the 15th FC, what is the allocation ratio between response and mitigation?", "80% for Response (SDRF) and 20% for Mitigation (SDMF)", "80% மீட்பு மற்றும் நிவாரணம் (SDRF) மற்றும் 20% பேரிடர் தணிப்பு (SDMF)", "Ensures dedicated ring-fenced resources for disaster risk reduction and climate resilience.", "பேரிடர் அபாயத்தைக் குறைப்பதற்கும் காலநிலை மாற்றத் தணிப்பிற்கும் பிரத்யேக நிதியை உறுதி செய்கிறது.", "The Response fund is further divided into Response (40%), Recovery (30%), and Preparedness (10%).", "மீட்பு நிதி மேலும் மீட்பு (40%), சீரமைப்பு (30%) மற்றும் தயார்நிலை (10%) எனப் பிரிக்கப்பட்டுள்ளது."),
    ("Criteria for Inter-Se Allocation Evolution", "How did the 15th Finance Commission evaluate 'Tax and Fiscal Effort' compared to earlier commissions?", "Calculated the ratio of Own Tax Revenue to GSDP relative to the State's per capita income potential", "மாநிலத்தின் தனிநபர் வருமானத் திறனுடன் ஒப்பிட்டு சொந்த வரி வருவாய்க்கும் GSDP-க்கும் உள்ள விகிதத்தைக் கணக்கிட்டது", "Rewards states that exert genuine effort to mobilize their tax bases rather than relying solely on central transfers.", "மத்திய நிதிப் பகிர்வை மட்டுமே நம்பியிருக்காமல் சொந்த வரிகளை வசூலிக்கும் மாநிலங்களுக்கு வெகுமதி அளிக்கிறது.", "Weight was maintained at 2.5% to provide a modest efficiency signal.", "திறமையான நிர்வாகத்திற்கான சமிக்ஞையாக 2.5% எடை பராமரிக்கப்பட்டது."),
    ("Role of State Finance Commission Reports Delay", "What systemic problem regarding State Finance Commissions was flagged by the 15th Finance Commission?", "States delay constituting SFCs and frequently fail to table Action Taken Reports on SFC recommendations", "மாநிலங்கள் SFC-ஐ அமைக்க தாமதிக்கின்றன மற்றும் அவற்றின் பரிந்துரைகள் மீதான நடவடிக்கை அறிக்கைகளை வைப்பதில்லை", "Under Article 243-I(4), the Governor must cause SFC recommendations to be laid before the State Legislature.", "சரத்து 243-I(4)-ன் படி ஆளுநர் SFC பரிந்துரைகளை மாநில சட்டமன்றத்தில் வைக்க வேண்டும்.", "15th FC made adherence to SFC constitution a key benchmark for release of local body grants.", "SFC அமைப்பதை உள்ளாட்சி மானியங்களை விடுவிப்பதற்கான முக்கிய அளவுகோலாக 15வது ஆணையம் மாற்றியது."),
    ("Equalization Principle in Fiscal Federalism", "What is the core objective of the 'Equalization Principle' applied by the Finance Commission in horizontal devolution?", "Ensuring that every citizen receives a comparable standard of basic public services irrespective of their state of residence", "குடிமக்கள் எந்த மாநிலத்தில் வசித்தாலும் அவர்களுக்கு இணையான அடிப்படை பொதுச் சேவைகள் கிடைப்பதை உறுதி செய்தல்", "Compensates for horizontal fiscal disabilities (low tax base, hilly terrain, high poverty).", "குறைந்த வரி வருவாய், மலைப்பாங்கான நிலப்பரப்பு போன்ற மாநிலக் குறைபாடுகளை ஈடுசெய்கிறது.", "Income Distance and Area criteria embody this equity-focused equalization transfer.", "வருமான இடைவெளி மற்றும் பரப்பளவு அளவுகோல்கள் இந்த சமத்துவக் கொள்கையை நிலைநிறுத்துகின்றன."),
    ("Sector-Specific Grants Status in 15th FC", "Why were the sector-specific grants recommended by the 15th Finance Commission (such as for health and judiciary) not implemented by the Union Government?", "The Union Government accepted tax devolution and revenue deficit grants but stated that sector grants would be reviewed within CSS frameworks", "மத்திய அரசு வரிப் பகிர்வு மற்றும் பற்றாக்குறை மானியங்களை ஏற்றது; ஆனால் துறைசார் மானியங்கள் மத்திய திட்டங்கள் மூலம் பரிசீலிக்கப்படும் எனக் கூறியது", "Article 281 explanatory memorandum allows the Union executive to accept, modify, or reject specific recommendations.", "சரத்து 281 விளக்கக் குறிப்பு குறிப்பிட்ட பரிந்துரைகளை ஏற்கவோ, மாற்றவோ அல்லது நிராகரிக்கவோ மத்திய நிர்வாகத்தை அனுமதிக்கிறது.", "Sector grants for health (Rs. 31,755 cr) and agriculture were largely re-routed through Centrally Sponsored Schemes.", "சுகாதாரம் மற்றும் விவசாயத்திற்கான துறைசார் மானியங்கள் மத்திய திட்டங்கள் வழியே மாற்றியமைக்கப்பட்டன."),
    ("Performance Incentives for Agricultural Reforms", "What performance criteria were proposed by the 15th FC for incentive grants to States in agriculture?", "Enactment of model land leasing laws, promotion of water-efficient crops, and direct benefit transfers for power subsidies", "மாதிரி நில குத்தகைச் சட்டங்களை இயற்றுதல், நீர் திறன் கொண்ட பயிர்களை ஊக்குவித்தல் மற்றும் மின் மானியங்களுக்கான நேரடி பணப் பரிமாற்றம்", "Promotes market-oriented agricultural reforms without compromising small farmer tenure security.", "சிறு விவசாயிகளின் நிலப் பாதுகாப்பைப் பாதிக்காமல் சந்தை சார்ந்த வேளாண் சீர்திருத்தங்களை ஊக்குவிக்கிறது.", "States reforming agricultural marketing infrastructure were eligible for bonus grants.", "விவசாய சந்தை உள்கட்டமைப்பை சீர்திருத்தும் மாநிலங்களுக்கு ஊக்க மானியங்கள் வழங்க பரிந்துரைக்கப்பட்டது."),
    ("Performance Grants for Power Sector Viability", "How did the 15th Finance Commission link additional borrowing space to power sector reforms in States?", "Allowed an extra 0.5% of GSDP borrowing space conditional on reducing AT&C losses and clearing discom subsidy dues", "AT&C மின் இழப்புகளைக் குறைத்தல் மற்றும் மானிய நிலுவைகளைத் தீர்ப்பதன் நிபந்தனையின் பேரில் கூடுதல் 0.5% கடன் வரம்பை அனுமதித்தது", "Addressed the recurring problem of massive state electricity discom accumulated debts.", "மாநில மின் விநியோக நிறுவனங்களின் பெரும் கடன் சுமைக்கு தீர்வுகாண இது கொண்டுவரப்பட்டது.", "Monitored under the Revamped Distribution Sector Scheme (RDSS).", "மறுசீரமைக்கப்பட்ட மின் விநியோகத் துறை திட்டத்தின் (RDSS) கீழ் கண்காணிக்கப்படுகிறது."),
    ("Health Grants to Local Bodies (15th FC)", "Why did the 15th Finance Commission channel Rs. 70,000 crore of health grants directly through local bodies?", "To strengthen primary healthcare infrastructure, convert sub-centres into Health and Wellness Centres, and support diagnostic testing", "ஆரம்ப சுகாதார உள்கட்டமைப்பை வலுப்படுத்தவும் துணை மையங்களை நலவாழ்வு மையங்களாக மாற்றவும் ஆய்வகப் பரிசோதனைகளுக்கு உதவவும்", "Direct funding to local bodies ensures grassroot healthcare resilience exposed during the COVID-19 pandemic.", "உள்ளாட்சி அமைப்புகளுக்கு நேரடியாக நிதியளிப்பது கோவிட் பெருந்தொற்றின் போது வெளிப்பட்ட சுகாதார பலவீனங்களை சரிசெய்கிறது.", "Rural and urban local bodies manage grassroot public health centres under the 11th and 12th Schedules.", "11வது மற்றும் 12வது அட்டவணைகளின் கீழ் கிராம மற்றும் நகர்ப்புற உள்ளாட்சிகள் பொது சுகாதார மையங்களை நிர்வகிக்கின்றன."),
    ("Inclusion of Cess in Divisible Pool Debate", "What is the primary argument raised by States demanding constitutional amendment of Article 271?", "The growing share of cesses and surcharges shrinks the effective divisible pool despite a nominal 41% devolution headline", "செஸ் மற்றும் கூடுதல் வரிகள் அதிகரிப்பதால் 41% வரிப் பகிர்வு இருந்தாலும் உண்மையான பகிர்வு நிதி கணிசமாக சுருங்குகிறது", "Cesses and surcharges belong 100% to the Union under Article 271.", "சரத்து 271-ன் கீழ் செஸ் மற்றும் கூடுதல் வரிகள் 100% மத்திய அரசுக்கே சொந்தமானவையாகும்.", "States argue that their effective devolution share drops from 41% to around 30-32% of gross tax revenues.", "மொத்த வரி வருவாயில் தங்களுக்குக் கிடைக்கும் உண்மையான பங்கு 30-32% ஆகக் குறைகிறது என மாநிலங்கள் வாதிடுகின்றன."),
    ("Finance Commission and Fiscal Council Debate", "Why did the 14th and 15th Finance Commissions recommend the establishment of an independent Fiscal Council in India?", "To provide unbiased macro-fiscal projections, independently monitor FRBM compliance, and assess off-budget borrowings", "நடுநிலையான நிதி முன்கணிப்புகளை வழங்கவும் FRBM இணக்கத்தை தன்னிச்சையாக கண்காணிக்கவும் பட்ஜெட்டுக்கு புறம்பான கடன்களை மதிப்பிடவும்", "An independent fiscal council eliminates political bias in revenue forecasts and deficit calculations.", "சுயாதீன நிதிக் கவுன்சில் வருவாய் மதிப்பீடுகள் மற்றும் பற்றாக்குறைக் கணக்கீடுகளில் அரசியல் தலையீட்டை நீக்குகிறது.", "FRBM Review Committee headed by N.K. Singh in 2017 also strongly recommended a Fiscal Council.", "2017-ல் என்.கே. சிங் தலைமையிலான FRBM மறுஆய்வுக் குழுவும் நிதிக் கவுன்சிலை அமைக்க கடுமையாகப் பரிந்துரைத்தது."),
    ("Article 280 vs Article 263 Inter-State Council", "How do the constitutional mandates of the Finance Commission and the Inter-State Council interrelate?", "Finance Commission is a specialized quasi-judicial fiscal devolution body, whereas the Inter-State Council is a broad executive forum for political consensus", "நிதி ஆணையம் ஒரு பிரத்யேக பகுதி-நீதித்துறை நிதிப் பகிர்வு அமைப்பாகும்; ஆனால் மாநிலங்களுக்கு இடையேயான கவுன்சில் அரசியல் ஒருமித்த கருத்தை உருவாக்கும் நிர்வாக மன்றமாகும்", "Article 263 sets up the Inter-State Council; Article 280 sets up the Finance Commission.", "சரத்து 263 மாநிலங்களுக்கு இடையேயான கவுன்சிலையும், சரத்து 280 நிதி ஆணையத்தையும் நிறுவுகிறது.", "Sarkaria Commission recommended strengthening both institutions to foster cooperative federalism.", "சர்க்காரியா ஆணையம் கூட்டுறவு கூட்டாட்சியை வளர்க்க இவ்விரு அமைப்புகளையும் வலுப்படுத்த பரிந்துரைத்தது."),
    ("Article 275 Specific Proviso for Scheduled Tribes", "What does the first proviso to Article 275(1) specifically mandate regarding grants to States?", "Mandatory capital and recurring grants from CFI to promote the welfare of Scheduled Tribes and raise administration standards in Scheduled Areas", "பழங்குடியினர் நலனை மேம்படுத்தவும் அட்டவணைப் பகுதிகளின் நிர்வாகத் தரத்தை உயர்த்தவும் CFI-லிருந்து கட்டாய மூலதன மற்றும் தொடர் மானியங்கள்", "Proviso grants under Article 275(1) are constitutional guarantees independent of general revenue deficit grants.", "சரத்து 275(1)-ன் முதல் வரம்புரை மானியங்கள் பொது வருவாய்ப் பற்றாக்குறை மானியங்களிலிருந்து மாறுபட்ட அரசியலமைப்பு உத்தரவாதங்களாகும்.", "Assam receives specific grants under the second proviso to Article 275(1).", "சரத்து 275(1)-ன் இரண்டாவது வரம்புரையின் கீழ் அசாம் மாநிலத்திற்கு குறிப்பிட்ட மானியங்கள் வழங்கப்படுகின்றன."),
    ("Seventh FC Landmark Doubling of Excise Duties", "What was the path-breaking contribution of the Seventh Finance Commission under Justice J.M. Shelat (1979-84)?", "Doubled the States' share of Union Excise Duties from 20% to 40%, drastically reducing reliance on discretionary Article 282 grants", "மத்திய கலால் வரியில் மாநிலங்களின் பங்கை 20%-லிருந்து 40%-ஆக இரட்டிப்பாக்கி விருப்ப மானியங்கள் மீதான சார்பை பெருமளவில் குறைத்தது", "Shelat Commission prioritized statutory tax devolution over discretionary central assistance.", "ஷெலத் ஆணையம் நிர்வாக விருப்ப உதவிகளை விட சட்டப்பூர்வ வரிப் பகிர்வுக்கு முன்னுரிமை அளித்தது.", "Significantly empowered States' non-plan revenue balances for the Sixth Five-Year Plan.", "ஆறாவது ஐந்தாண்டுத் திட்டத்திற்கான மாநிலங்களின் திட்டமில்லா வருவாய் நிலுவைகளை இது கணிசமாக வலுப்படுத்தியது."),
    ("Eighth FC Uniform Devolution Formula", "What major methodological consistency was introduced by the Eighth Finance Commission under Y.B. Chavan?", "Introduced a uniform common formula for distributing both Income Tax and Union Excise Duties among States", "வருமான வரி மற்றும் மத்திய கலால் வரிகள் இரண்டையும் மாநிலங்களுக்கு இடையே பகிர்ந்தளிக்க ஒரே மாதிரியான பொதுவான சூத்திரத்தை அறிமுகப்படுத்தியது", "Prior to 8th FC, different disparate formulas were used for Income Tax (population/collection) and Excise Duties.", "8வது ஆணையத்திற்கு முன்பு வருமான வரிக்கும் கலால் வரிக்கும் வெவ்வேறு மாறுபட்ட சூத்திரங்கள் பயன்படுத்தப்பட்டன.", "Formula gave 90% weight to economic backwardness (Income Distance + Inverse Income) and population.", "இந்த சூத்திரம் பொருளாதாரப் பின்னடைவு மற்றும் மக்கள் தொகைக்கு 90% எடையை வழங்கியது."),
    ("Normative Approach of the Ninth FC", "What was the distinguishing methodology of the Ninth Finance Commission under N.K.P. Salve?", "Adopting a normative approach to assess revenues and expenditures instead of relying purely on historic trends", "வரலாற்றுப் போக்குகளை மட்டும் நம்பாமல் வருவாய் மற்றும் செலவினங்களை மதிப்பிட நெறிமுறை (Normative) அணுகுமுறையைக் கையாண்டது", "Normative approach penalizes fiscal profligacy and rewards tax effort and expenditure containment.", "நெறிமுறை அணுகுமுறை வீண் செலவுகளைக் கட்டுப்படுத்தி வரி முயற்சியையும் சிக்கனத்தையும் ஊக்குவிக்கிறது.", "Assessed taxable capacity based on macroeconomic indicators rather than actual past collection figures.", "முந்தைய வசூல் தரவுகளுக்குப் பதிலாக பேரியல் பொருளாதாரக் குறியீடுகளின் அடிப்படையில் வரித் திறனை மதிப்பிட்டது."),
    ("Third FC Proposal on Planning Commission", "What radical organizational change was recommended by A.K. Chanda in the Third Finance Commission report?", "Either transform the Planning Commission into the constitutional Finance Commission or enlarge the Finance Commission to handle plan finance", "திட்டக் குழுவை அரசியலமைப்பு நிதி ஆணையமாக மாற்ற வேண்டும் அல்லது திட்ட நிதியைக் கையாள நிதி ஆணையத்தை விரிவுபடுத்த வேண்டும்", "Highlighted the severe constitutional anomaly of an executive body deciding the vast majority of federal transfers.", "பெரும்பாலான கூட்டாட்சி நிதிப் பகிர்வை ஒரு நிர்வாக அமைப்பு தீர்மானிக்கும் அரசியலமைப்பு முரண்பாட்டை சுட்டிக்காட்டியது.", "Government rejected the recommendation, preserving the dominance of the Planning Commission for decades.", "மத்திய அரசு இப்பரிந்துரையை நிராகரித்து திட்டக் குழுவின் ஆதிக்கத்தை பல தசாப்தங்களுக்கு நீடித்தது."),
    ("Finance Commission and Off-Budget Borrowings", "How did the 15th Finance Commission treat extra-budgetary and off-budget borrowings of the Union and State Governments?", "Urged full fiscal transparency and recommended reporting all off-budget borrowings against the FRBM debt limits", "முழு நிதி வெளிப்படைத்தன்மையை வலியுறுத்தியதுடன் அனைத்து பட்ஜெட்டுக்கு புறம்பான கடன்களையும் FRBM கடன் வரம்பிற்குள் கொண்டுவர பரிந்துரைத்தது", "Prevents governments from hiding fiscal deficits through state-owned corporations and special purpose vehicles.", "பொதுத்துறை நிறுவனங்கள் மூலம் நிதிப் பற்றாக்குறையை மறைப்பதை இது தடுக்கிறது.", "Union Government brought extra-budgetary resources (EBR) like FCI borrowings back into the formal budget in 2021-22.", "2021-22ல் FCI கடன்கள் போன்ற கூடுதல் பட்ஜெட் வளங்களை மத்திய அரசு பட்ஜெட்டிற்குள் கொண்டு வந்தது."),
    ("Article 280(3)(bb) SFC Linkage Reality", "Why is the Finance Commission's mandate under Article 280(3)(bb) described as an 'organic operational link'?", "It requires the Central Finance Commission to build its local body grants directly on the foundation of State Finance Commission awards", "மாநில நிதி ஆணையங்களின் பரிந்துரைகளின் அடிப்படையிலேயே மத்திய நிதி ஆணையம் தனது உள்ளாட்சி மானியங்களை கட்டமைக்க வேண்டும் என்பதால்", "Links constitutional fiscal federalism from the Union down to the tier of Gram Panchayats.", "மத்திய அரசிலிருந்து கிராம பஞ்சாயத்து வரை அரசியலமைப்பு நிதி கூட்டாட்சியை இணைக்கிறது.", "Where SFC reports are unavailable, Central FC makes independent baseline allocations to prevent rural distress.", "SFC அறிக்கைகள் இல்லாத போது கிராமப்புற பாதிப்பைத் தடுக்க மத்திய ஆணையமே நேரடி ஒதுக்கீடுகளைச் செய்கிறது."),
    ("Constitutional Protection of Tax Devolution", "Can the President alter or reduce the tax devolution percentages recommended by the Finance Commission after they are notified?", "No, once the Presidential Order under Article 270 is issued and approved, devolution has statutory force for the award period", "இல்லை, சரத்து 270-ன் கீழ் குடியரசுத் தலைவரின் ஆணை வெளியிடப்பட்டு அங்கீகரிக்கப்பட்ட பின், அது விருது காலத்திற்கு சட்டப்பூர்வ வலிமை பெறுகிறது", "Article 270 presidential order guarantees reliable non-discretionary revenue streams to States.", "சரத்து 270 குடியரசுத் தலைவர் ஆணை மாநிலங்களுக்கு நம்பகமான தன்னிச்சையற்ற வருவாய் வரவை உறுதி செய்கிறது.", "Devolution occurs automatically every month through RBI treasury clearances.", "ஒவ்வொரு மாதமும் ரிசர்வ் வங்கி கருவூல தீர்வுகள் மூலம் வரிப் பகிர்வு தானாகவே நடைபெறுகிறது."),
    ("15th FC Demographic Transition Bonus", "How was the Demographic Performance score mathematically calculated in the 15th FC formula?", "Reciprocal of the Total Fertility Rate (TFR) multiplied by 1971 population of the State", "மாநிலத்தின் 1971 மக்கள் தொகையுடன் பெருக்கப்பட்ட மொத்த கருவுறுதல் விகிதத்தின் (TFR) தலைகீழ் மதிப்பு", "Ensures that states with low fertility rates receive a proportionately larger demographic reward.", "குறைந்த பிறப்பு விகிதத்தைக் கொண்ட மாநிலங்களுக்கு விகிதாசார ரீதியாக அதிக மக்கள்தொகை வெகுமதி கிடைப்பதை உறுதி செய்கிறது.", "Kerala, Tamil Nadu, Andhra Pradesh, and Punjab scored the highest points under this criterion.", "கேரளா, தமிழ்நாடு, ஆந்திரா மற்றும் பஞ்சாப் ஆகிய மாநிலங்கள் இதில் அதிக மதிப்பெண்களைப் பெற்றன."),
    ("Article 275 Grants Non-Votable Character", "Are the grants-in-aid recommended under Article 275 subject to the annual vote of Parliament?", "No, they are charged on the Consolidated Fund of India and are not submitted to the vote of Parliament", "இல்லை, அவை இந்தியத் திரட்டப்பட்ட நிதியில் பொறுப்பாக்கப்பட்டவை (Charged) என்பதால் நாடாளுமன்ற வாக்கெடுப்புக்கு உட்பட்டவை அல்ல", "Article 275(1) states grants shall be 'charged on the Consolidated Fund of India'.", "சரத்து 275(1) மானியங்கள் 'இந்தியத் திரட்டப்பட்ட நிதியில் பொறுப்பாக்கப்படும்' எனக் கூறுகிறது.", "Protects state fiscal allocations from annual political horse-trading in the Lok Sabha.", "மக்களவையின் வருடாந்திர அரசியல் பேரங்களிலிருந்து மாநில நிதி ஒதுக்கீடுகளை இது பாதுகாக்கிறது."),
    ("15th FC Two-Report Precedent", "Why did the 15th Finance Commission submit two separate reports (interim for 2020-21 and final for 2021-26)?", "Due to the economic uncertainty caused by COVID-19 pandemic and the reorganization of Jammu & Kashmir in late 2019", "கோவிட்-19 பெருந்தொற்றினால் ஏற்பட்ட பொருளாதார நிச்சயமற்ற தன்மை மற்றும் 2019 இறுதியில் ஜம்மு காஷ்மீர் மறுசீரமைப்பு காரணமாக", "Terms of Reference were amended in November 2019 to extend the submission deadline.", "சமர்ப்பிக்கும் காலக்கெடுவை நீட்டிக்க நவம்பர் 2019-ல் பணிக் குறிப்புகள் திருத்தப்பட்டன.", "The interim report covered fiscal year 2020-21, while the main report covered 2021-22 to 2025-26.", "இடைக்கால அறிக்கை 2020-21 நிதியாண்டையும், முதன்மை அறிக்கை 2021-22 முதல் 2025-26 வரையிலான காலத்தையும் உள்ளடக்கியது."),
    ("Forest and Ecology vs Dense Forest Cover", "Why did the 15th FC rename the 'Forest Cover' criterion of the 14th FC to 'Forest and Ecology'?", "To explicitly account for dense and moderately dense forest canopies and compensate for loss of economic opportunity", "அடர்ந்த மற்றும் மிதமான வன விதானங்களை வெளிப்படையாகக் கணக்கில் கொண்டு பொருளாதார வாய்ப்பு இழப்பை ஈடுசெய்ய", "Maintains ecological carbon sinks that provide national and global environmental externalities.", "தேசிய மற்றும் உலகளாவிய சுற்றுச்சூழல் நன்மைகளை வழங்கும் கார்பன் மூழ்கிகளைப் பராமரிக்கிறது.", "Arunachal Pradesh, Madhya Pradesh, and Chhattisgarh emerged as the top beneficiaries of this weight.", "அருணாச்சல பிரதேசம், மத்திய பிரதேசம் மற்றும் சத்தீஸ்கர் ஆகியவை இதனால் அதிக பயனடைந்தன."),
    ("Horizontal Devolution: Area Criterion Rationale", "What is the economic rationale for allocating 15% weight to 'Area' in the horizontal devolution formula?", "Larger geographical territory imposes higher per-unit unit costs on delivery of public administrative services", "பெரிய புவியியல் பரப்பளவு பொது நிர்வாக சேவைகளை வழங்குவதில் அதிக தனிநபர் செலவை ஏற்படுத்துகிறது", "Sparsely populated large states face severe logistical diseconomies of scale.", "குறைந்த மக்கள் அடர்த்தி கொண்ட பெரிய மாநிலங்கள் நிர்வாக தளவாடங்களில் அதிக செலவுகளை எதிர்கொள்கின்றன.", "Rajasthan and Madhya Pradesh receive substantial allocations under the Area criterion.", "ராஜஸ்தான் மற்றும் மத்திய பிரதேசம் பரப்பளவு அளவுகோலின் கீழ் கணிசமான நிதிப் பங்கைப் பெறுகின்றன."),
    ("Sixteenth Finance Commission Mandate", "What are the core pillars of the Terms of Reference notified for the 16th Finance Commission under Dr. Arvind Panagariya?", "Tax devolution, principles of Article 275 grants, measures to augment state consolidated funds for local bodies, and disaster financing", "வரிப் பகிர்வு, சரத்து 275 மானியக் கொள்கைகள், உள்ளாட்சிகளுக்கான மாநில நிதி பெருக்கும் வழிகள் மற்றும் பேரிடர் நிதி", "Constituted on December 31, 2023 for the award period April 1, 2026 to March 31, 2031.", "ஏப்ரல் 1, 2026 முதல் மார்ச் 31, 2031 வரையிலான காலத்திற்கு டிசம்பர் 31, 2023 அன்று அமைக்கப்பட்டது.", "Final recommendations are due to be submitted to the President by October 31, 2025.", "இறுதிப் பரிந்துரைகள் அக்டோபர் 31, 2025-க்குள் குடியரசுத் தலைவரிடம் சமர்ப்பிக்கப்பட வேண்டும்."),
    ("Tax Devolution vs Grants-in-Aid Dominance", "What has been the enduring institutional preference of all Finance Commissions regarding federal transfers?", "Preferring unconditional tax devolution as the primary instrument, using grants-in-aid only as a residual balancing mechanism", "நிபந்தனையற்ற வரிப் பகிர்வை முதன்மைக் கருவியாகப் பயன்படுத்துவது; மானியங்களை பற்றாக்குறையை சமன் செய்யும் இறுதி கருவியாக மட்டுமே பயன்படுத்துவது", "Tax devolution gives States full democratic freedom to allocate resources to local priorities.", "வரிப் பகிர்வு மாநிலங்கள் தங்களது உள்ளூர் முன்னுரிமைகளுக்கு நிதியை ஒதுக்க முழு தன்னாட்சியை வழங்குகிறது.", "Over 80-85% of total federal transfers recommended by the 14th and 15th FCs consist of tax devolution.", "14 மற்றும் 15வது நிதி ஆணையங்களால் பரிந்துரைக்கப்பட்ட மொத்த நிதியில் 80-85% வரிப் பகிர்வாகவே உள்ளது."),
    ("AuditOnline Platform Integration", "Why did the 15th Finance Commission mandate the use of the AuditOnline platform for local bodies?", "To ensure digital audit trails, timely completion of local body accounts, and public access to financial statements", "டிஜிட்டல் தணிக்கைத் தடங்கள், உள்ளாட்சி கணக்குகளை சரியான நேரத்தில் முடித்தல் மற்றும் நிதி அறிக்கைகளை பொதுமக்களுக்குக் கிடைக்கச் செய்ய", "AuditOnline is an open-source application developed by the Ministry of Panchayati Raj.", "AuditOnline என்பது பஞ்சாயத்து ராஜ் அமைச்சகத்தால் உருவாக்கப்பட்ட பயன்பாடாகும்.", "Unlocking performance grants requires 100% online audit report uploads.", "செயல்திறன் மானியங்களைப் பெற 100% தணிக்கை அறிக்கைகளை இணையத்தில் பதிவேற்ற வேண்டும்."),
    ("Fiscal Capacity vs Revenue Capacity", "How does the Finance Commission distinguish between fiscal capacity and actual revenue collection of a State?", "Fiscal capacity measures the potential tax revenue a state can raise given its macroeconomic base, while collection reflects actual effort", "நிதித் திறன் என்பது ஒரு மாநிலம் தனது பொருளாதார அடித்தளத்திலிருந்து திரட்டக்கூடிய உத்தேச வரி வருவாயைக் குறிக்கிறது; வசூல் என்பது உண்மையான முயற்சியைக் காட்டுகிறது", "Prevents rewarding states that deliberately under-tax to qualify for higher equalization grants.", "அதிக மானியங்களைப் பெறுவதற்காக வேண்டுமென்றே குறைந்த வரிகளை விதிக்கும் மாநிலங்களுக்கு நிதி கிடைப்பதை இது தடுக்கிறது.", "Normative tax estimation relies on regression modeling of state GSDP sectoral composition.", "நெறிமுறை வரி மதிப்பீடு மாநில GSDP-ன் துறைசார் கட்டமைப்பை அடிப்படையாகக் கொண்டது."),
    ("Intergovernmental Fiscal Transfers Typology", "How are Finance Commission transfers classified in international public finance terminology?", "General-purpose untied equalizing formulaic transfers supplemented by targeted fiscal need grants", "இலக்கு நிர்ணயிக்கப்பட்ட நிதித் தேவை மானியங்களுடன் கூடிய பொது நோக்கத்திற்கான நிபந்தனையற்ற சமத்துவ சூத்திரப் பரிமாற்றங்கள்", "Combines macroeconomic equity with sub-national expenditure autonomy.", "பேரியல் பொருளாதார சமத்துவத்தை துணை-தேசிய செலவின தன்னாட்சியுடன் இணைக்கிறது.", "Widely cited as a global model of federal resource equalization in multi-tier federations.", "பல அடுக்கு கூட்டாட்சிகளில் வள சமத்துவத்திற்கான உலகளாவிய முன்மாதிரியாகக் குறிப்பிடப்படுகிறது."),
    ("Article 275 Capital Grants for Special Problems", "Under what rationale did earlier Finance Commissions recommend special capital grants under Article 275?", "To address idiosyncratic state disabilities like border fencing, police housing, and judicial complexes", "எல்லை வேலி அமைத்தல், காவலர் குடியிருப்புகள் மற்றும் நீதிமன்ற வளாகங்கள் போன்ற குறிப்பிட்ட மாநில குறைபாடுகளைத் தீர்க்க", "Upgrades administrative infrastructure in historically underdeveloped regions.", "வரலாற்று ரீதியாக பின்தங்கிய பகுதிகளில் நிர்வாக உள்கட்டமைப்பை மேம்படுத்துகிறது.", "Discontinued by the 14th FC to subsume all untied capital spending within the 42% devolution.", "42% வரிப் பகிர்விற்குள் அனைத்து மூலதனச் செலவுகளையும் உள்ளடக்க 14வது நிதி ஆணையத்தால் இது நிறுத்தப்பட்டது."),
    ("Disaster Mitigation Fund Allocation Formula", "How is the inter-se allocation of the State Disaster Mitigation Fund (SDMF) determined among States?", "Combination of disaster vulnerability index, past five years' disaster expenditure, and geographical area", "பேரிடர் பாதிப்பு குறியீடு, கடந்த ஐந்து ஆண்டுகளின் பேரிடர் செலவினம் மற்றும் புவியியல் பரப்பளவு ஆகியவற்றின் கலவை", "Shifts focus from post-calamity relief to pre-disaster climate resilience and structural risk reduction.", "பேரிடருக்குப் பிந்தைய நிவாரணத்திலிருந்து பேரிடர் தடுப்பு மற்றும் கட்டமைப்பு இடர் குறைப்பிற்கு கவனத்தை மாற்றுகிறது.", "NDMA vulnerability atlas serves as a primary input for risk profiling.", "NDMA பேரிடர் பாதிப்பு வரைபடம் இடர் மதிப்பீட்டிற்கான முதன்மை உள்ளீடாக செயல்படுகிறது."),
    ("Finance Commission and Centrally Sponsored Schemes Rationalization", "What consistent recommendation have successive Finance Commissions made regarding Centrally Sponsored Schemes (CSS)?", "Drastically reduce the number of CSS, eliminate schematic micromanagement, and provide higher untied funding to States", "மத்திய திட்டங்களின் எண்ணிக்கையைக் கணிசமாகக் குறைத்தல், திட்ட அளவிலான நுண் நிர்வாகத்தை நீக்குதல் மற்றும் மாநிலங்களுக்கு அதிக நிபந்தனையற்ற நிதி வழங்குதல்", "CSS proliferation restricts state fiscal priorities and distorts local budget preferences.", "மத்திய திட்டங்களின் பெருக்கம் மாநில நிதி முன்னுரிமைகளைக் கட்டுப்படுத்துகிறது மற்றும் உள்ளூர் விருப்பங்களை சிதைக்கிறது.", "14th FC urged the Centre to limit CSS strictly to core national constitutional priorities.", "முக்கிய தேசிய அரசியலமைப்பு முன்னுரிமைகளுக்கு மட்டுமே மத்திய திட்டங்களை மட்டுப்படுத்த 14வது ஆணையம் வலியுறுத்தியது."),
    ("Article 280(3)(a) Net Proceeds Netting Meaning", "What does 'cost of collection' subtracted from gross proceeds to calculate 'net proceeds' under Article 279 cover?", "Direct administrative salaries, office overheads, and enforcement expenditures of the CBDT and CBIC revenue departments", "CBDT மற்றும் CBIC வருவாய்த் துறைகளின் நேரடி நிர்வாக ஊதியங்கள், அலுவலக செலவுகள் மற்றும் அமலாக்க செலவினங்கள்", "The net divisible pool is gross collections minus the verified actual cost of collecting those taxes.", "நிகர பகிர்வு நிதி என்பது மொத்த வசூலிலிருந்து அந்த வரிகளை வசூலிப்பதற்கான உண்மையான செலவைக் கழித்த தொகையாகும்.", "CAG audit certification ensures the Union does not artificially inflate collection charges to shrink the pool.", "மத்திய அரசு வசூல் செலவை செயற்கையாக உயர்த்தி பகிர்வு நிதியைக் குறைக்காமல் இருப்பதை சி.ஏ.ஜி சான்றிதழ் உறுதி செய்கிறது."),
    ("Fiscal Consolidation Roadmap: Post-COVID Path", "What post-COVID fiscal deficit target did the 15th Finance Commission recommend for the Union Government by 2025-26?", "Reducing the Union fiscal deficit to 4.0% of GDP by fiscal year 2025-26", "2025-26 நிதியாண்டிற்குள் மத்திய அரசின் நிதிப் பற்றாக்குறையை GDP-ல் 4.0% ஆகக் குறைத்தல்", "Provides a realistic fiscal consolidation glide path after the massive pandemic-induced debt expansion.", "பெருந்தொற்றினால் ஏற்பட்ட பெரும் கடன் விரிவாக்கத்திற்குப் பிறகு ஒரு யதார்த்தமான நிதி ஒருங்கிணைப்புப் பாதையை வழங்குகிறது.", "Recommended establishing an overarching debt-to-GDP target of 60% (40% Union, 20% States).", "மொத்த கடன்-GDP இலக்கை 60% ஆக (மத்திய அரசு 40%, மாநிலங்கள் 20%) நிர்ணயிக்க பரிந்துரைத்தது."),
    ("Continuity vs Change in Finance Commission Methodologies", "Why does each Finance Commission typically retain the broad structure of its predecessor while introducing incremental innovations?", "To provide macroeconomic stability and budgetary predictability to States while responding to evolving federal realities", "மாநிலங்களுக்கு பேரியல் பொருளாதார ஸ்திரத்தன்மை மற்றும் பட்ஜெட் முன்கணிப்பை வழங்குவதோடு மாறிவரும் கூட்டாட்சி சூழலுக்கு ஏற்ப செயல்பட", "Sudden drastic formulaic swings could destabilize state fiscal planning and public service delivery.", "திடீர் தீவிர மாற்றங்கள் மாநில நிதித் திட்டமிடலையும் பொதுச் சேவை வழங்கலையும் சீர்குலைத்துவிடும்.", "Hence criteria like Income Distance and Population remain foundational anchors across commissions.", "எனவே வருமான இடைவெளி மற்றும் மக்கள் தொகை போன்ற அளவுகோல்கள் அனைத்து ஆணையங்களிலும் அடிப்படை தூண்களாகத் தொடர்கின்றன."),
    ("Fiscal Federalism Equilibrium", "Why is the Finance Commission characterized as the balancing wheel of Indian fiscal federalism?", "It resolves vertical fiscal imbalances between the Centre and States and horizontal fiscal disparities among diverse States", "மத்திய மற்றும் மாநிலங்களுக்கு இடையிலான செங்குத்து நிதி ஏற்றத்தாழ்வையும் மாநிலங்களுக்கு இடையிலான கிடைமட்ட ஏற்றத்தாழ்வையும் தீர்க்கிறது", "Coined originally by Dr. K.V. Rao to describe the Finance Commission's role in the Constitution.", "நிதி ஆணையத்தின் பங்கை விவரிக்க டாக்டர் கே.வி. ராவ் முதலில் உருவாக்கிய சொல் இதுவாகும்.", "Ensures national economic unity while honoring regional diversity.", "பிராந்திய பன்முகத்தன்மையை மதிக்கும் அதே வேளையில் தேசிய பொருளாதார ஒற்றுமையை உறுதி செய்கிறது.")
]

for item in more_medium_items:
    topic, stem, correct_en, correct_ta, tip_en, tip_ta, fact_en, fact_ta = item
    raw_medium_data.append({
        "subtopic": topic,
        "stem_en": f"{stem}?",
        "stem_ta": f"{correct_ta[:40]}... தொடர்பாக {stem}?",
        "options": [
            (correct_en, correct_ta),
            ("Subject to unilateral executive veto by the Union Cabinet Secretary", "மத்திய அமைச்சரவைச் செயலாளரின் ஒருதலைப்பட்ச வீட்டோ அதிகாரத்திற்கு உட்பட்டது"),
            ("Decided purely by arbitrary lottery draws conducted during Parliamentary sessions", "நாடாளுமன்றக் கூட்டத்தொடரின் போது நடத்தப்படும் தன்னிச்சையான குலுக்கல் முறையில் தீர்மானிக்கப்படுவது"),
            ("Governed strictly by private corporate shareholder agreements", "தனியார் கார்ப்பரேட் பங்குதாரர் ஒப்பந்தங்களின்படி மட்டுமே நிர்வகிக்கப்படுவது")
        ],
        "exp_en": f"{correct_en}. This constitutional mechanism ensures stability and equity in Indian fiscal federalism.",
        "exp_ta": f"{correct_ta}. இந்த அரசியலமைப்பு வழிமுறை இந்திய நிதி கூட்டாட்சியில் ஸ்திரத்தன்மையையும் சமத்துவத்தையும் உறுதி செய்கிறது.",
        "tip_en": tip_en,
        "tip_ta": tip_ta,
        "fact_en": fact_en,
        "fact_ta": fact_ta
    })

def build_questions():
    questions = []
    for idx, item in enumerate(raw_medium_data, start=1):
        qid = f"FC_M_{idx:03d}"
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
        
        q = make_fc_q(
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
            tags=["polity", "finance_commission", "medium", item["subtopic"].lower().replace(" ", "_")]
        )
        questions.append(q)
    return questions

if __name__ == "__main__":
    qs = build_questions()
    print(f"Generated {len(qs)} raw Medium questions for Finance Commission.")
    assert len(qs) == 50, f"Expected 50 questions, got {len(qs)}"
    
    balanced_qs = balance_question_keys(qs)
    
    out_path = os.path.join("data", "questions", "polity", "fc_medium.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(balanced_qs, f, ensure_ascii=False, indent=2)
    print(f"Saved balanced Medium MCQs to {out_path}")
    
    val = ContentValidator()
    report = val.validate_file(out_path, expected_count=50, expected_prefix="FC_M_")
    print(f"Validation Report: {'PASS' if report.is_valid else 'FAIL'} | Total: {report.total_audited}")
    if not report.is_valid:
        for iss in report.issues[:10]:
            print(f"  Issue: {iss}")
    print(f"Key Distribution: {report.key_distribution}")
