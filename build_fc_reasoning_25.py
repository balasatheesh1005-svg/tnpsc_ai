# -*- coding: utf-8 -*-
"""
Build 25 Assertion and Reasoning MCQs for Finance Commission of India
ID range: FC_R_001 to FC_R_025
Target key distribution: {'A': 7, 'B': 6, 'C': 6, 'D': 6}
"""

import json
import os
import shutil
from fc_mcq_helper import make_fc_q
from tools.nova_content_engine.validator import ContentValidator

opts_en = [
    "Both (A) and (R) are true and (R) is the correct explanation of (A)",
    "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
    "(A) is true but (R) is false",
    "(A) is false but (R) is true"
]

opts_ta = [
    "(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கமாகும்",
    "(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல",
    "(A) சரி ஆனால் (R) தவறு",
    "(A) தவறு ஆனால் (R) சரி"
]

raw_reasoning_items = [
    # 1: A
    {
        "subtopic": "Article 280 Constitutional Status",
        "key": "A",
        "a_en": "Assertion (A): The Finance Commission is considered the balancing wheel of fiscal federalism in India.",
        "a_ta": "கூற்று (A): நிதி ஆணையம் இந்தியாவில் நிதி கூட்டாட்சியின் சமநிலைப்படுத்தும் சக்கரமாகக் கருதப்படுகிறது.",
        "r_en": "Reason (R): It rectifies the vertical imbalance between Union resources and State expenditure mandates, and horizontal disparities among States.",
        "r_ta": "காரணம் (R): இது மத்திய வளங்களுக்கும் மாநில செலவினப் பொறுப்புகளுக்கும் இடையிலான செங்குத்து ஏற்றத்தாழ்வையும், மாநிலங்களுக்கு இடையிலான கிடைமட்ட ஏற்றத்தாழ்வுகளையும் சரிசெய்கிறது.",
        "exp_en": "Both (A) and (R) are true and (R) is the correct explanation of (A). The constitutional mechanism of quinquennial devolution balances resource asymmetries across federal tiers.",
        "exp_ta": "(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கமாகும். ஐந்தாண்டு வரிப் பகிர்வு அரசியலமைப்பு முறை கூட்டாட்சி அடுக்குகளுக்கு இடையிலான வள ஏற்றத்தாழ்வுகளை சமன் செய்கிறது.",
        "tip_en": "K.V. Rao coined 'balancing wheel of fiscal federalism' for the Finance Commission.",
        "tip_ta": "நிதி ஆணையத்தை 'நிதி கூட்டாட்சியின் சமநிலைப்படுத்தும் சக்கரம்' என்று கே.வி. ராவ் வர்ணித்தார்.",
        "fact_en": "Article 280 was designed to provide periodic institutional correction to federal fiscal imbalances.",
        "fact_ta": "கூட்டாட்சி நிதி ஏற்றத்தாழ்வுகளை காலமுறை நிறுவன ரீதியாக திருத்தவே சரத்து 280 உருவாக்கப்பட்டது."
    },
    # 2: A
    {
        "subtopic": "Quasi-Judicial Civil Court Character",
        "key": "A",
        "a_en": "Assertion (A): The Finance Commission is vested with powers of a Civil Court under the Code of Civil Procedure 1908.",
        "a_ta": "கூற்று (A): நிதி ஆணையத்திற்கு 1908 சிவில் நடைமுறைச் சட்டத்தின் கீழ் சிவில் நீதிமன்றத்தின் அதிகாரங்கள் வழங்கப்பட்டுள்ளன.",
        "r_en": "Reason (R): It requires statutory authority to summon witnesses, examine them on oath, and requisition public records to assess state fiscal data.",
        "r_ta": "காரணம் (R): மாநில நிதித் தரவுகளை மதிப்பிடுவதற்கு சாட்சிகளை அழைக்கவும், உறுதிமொழியின் கீழ் விசாரிக்கவும், பொது ஆவணங்களைக் கோரவும் இதற்கு சட்டப்பூர்வ அதிகாரம் தேவைப்படுகிறது.",
        "exp_en": "Both (A) and (R) are true and (R) correctly explains why the 1951 Act vested civil court powers in the Commission.",
        "exp_ta": "(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கமாகும். 1951 சட்டம் ஆணையத்திற்கு சிவில் நீதிமன்ற அதிகாரங்களை ஏன் வழங்கியது என்பதை காரணம் விளக்குகிறது.",
        "tip_en": "Section 8 of the Finance Commission Act 1951 specifies Civil Court powers.",
        "tip_ta": "1951 நிதி ஆணையச் சட்டத்தின் பிரிவு 8 சிவில் நீதிமன்ற அதிகாரங்களைக் குறிப்பிடுகிறது.",
        "fact_en": "Proceedings before the FC are treated as judicial proceedings under Sections 193 and 228 of the IPC.",
        "fact_ta": "நிதி ஆணையத்தின் முன் நடக்கும் நடவடிக்கைகள் இந்திய தண்டனைச் சட்டம் 193 மற்றும் 228-ன் கீழ் நீதித்துறை நடவடிக்கைகளாகக் கருதப்படுகின்றன."
    },
    # 3: A
    {
        "subtopic": "Vertical Devolution Recalibration (15th FC)",
        "key": "A",
        "a_en": "Assertion (A): The 15th Finance Commission recommended a vertical devolution of 41% to States compared to 42% by the 14th FC.",
        "a_ta": "கூற்று (A): 14வது நிதி ஆணையம் பரிந்துரைத்த 42%-க்கு பதிலாக 15வது நிதி ஆணையம் மாநிலங்களுக்கு 41% செங்குத்து வரிப் பகிர்வை பரிந்துரைத்தது.",
        "r_en": "Reason (R): The 1% downward adjustment was made to provide financial resources for the newly created Union Territories of Jammu & Kashmir and Ladakh from the Centre's resources.",
        "r_ta": "காரணம் (R): புதிதாக உருவாக்கப்பட்ட ஜம்மு காஷ்மீர் மற்றும் லடாக் யூனியன் பிரதேசங்களுக்கு மத்திய அரசின் நிதியிலிருந்து வளங்களை ஒதுக்க இந்த 1% குறைப்பு செய்யப்பட்டது.",
        "exp_en": "Both (A) and (R) are true and (R) is the direct and accurate constitutional reason for reducing the percentage from 42% to 41%.",
        "exp_ta": "(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கமாகும். சதவீதம் 42%-லிருந்து 41%-ஆகக் குறைக்கப்பட்டதற்கான நேரடி காரணம் இதுவே.",
        "tip_en": "Reorganization of J&K into UTs transferred their funding directly to the Union Government budget.",
        "tip_ta": "ஜம்மு காஷ்மீர் யூனியன் பிரதேசங்களாக மாற்றப்பட்டதால் அவற்றின் நிதி மத்திய அரசின் நேரடிப் பொறுப்பானது.",
        "fact_en": "1% roughly matched the historical devolution share of the erstwhile State of Jammu & Kashmir.",
        "fact_ta": "இந்த 1% முந்தைய ஜம்மு காஷ்மீர் மாநிலத்தின் தோராயமான பகிர்வுப் பங்கிற்கு சமமாகும்."
    },
    # 4: A
    {
        "subtopic": "Demographic Performance Metric Rationale",
        "key": "A",
        "a_en": "Assertion (A): The 15th Finance Commission introduced 'Demographic Performance' as a specific horizontal devolution criterion.",
        "a_ta": "கூற்று (A): 15வது நிதி ஆணையம் 'மக்கள்தொகை செயல்திறனை' ஒரு குறிப்பிட்ட கிடைமட்ட வரிப் பகிர்வு அளவுகோலாக அறிமுகப்படுத்தியது.",
        "r_en": "Reason (R): It wanted to incentivize and reward States that successfully implemented population control policies and lowered their fertility rates.",
        "r_ta": "காரணம் (R): மக்கள்தொகைக் கட்டுப்பாட்டுக் கொள்கைகளை வெற்றிகரமாக செயல்படுத்தி பிறப்பு விகிதத்தைக் குறைத்த மாநிலங்களை ஊக்குவிக்கவும் வெகுமதி அளிக்கவும் அது விரும்பியது.",
        "exp_en": "Both (A) and (R) are true and (R) provides the exact policy rationale for introducing the 12.5% demographic performance weight.",
        "exp_ta": "(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கமாகும். 12.5% எடையுடன் மக்கள்தொகை செயல்திறன் அறிமுகப்படுத்தப்பட்டதற்கான சரியான காரணம் இதுவாகும்.",
        "tip_en": "Demographic Performance countered the penalty Southern states faced by using 2011 Census population.",
        "tip_ta": "2011 மக்கள் தொகை கணக்கெடுப்பைப் பயன்படுத்தியதால் தென் மாநிலங்கள் சந்தித்த நிதிப் பாதிப்பை இது சமன் செய்தது.",
        "fact_en": "Total Fertility Rate (TFR) inverse multiplied by 1971 population was used to compute the score.",
        "fact_ta": "1971 மக்கள் தொகையால் பெருக்கப்பட்ட TFR-ன் தலைகீழ் மதிப்பு இந்த மதிப்பெண்ணைக் கணக்கிடப் பயன்பட்டது."
    },
    # 5: A
    {
        "subtopic": "Article 275 Charged Expenditure Status",
        "key": "A",
        "a_en": "Assertion (A): Grants-in-aid recommended under Article 275 are not subjected to voting in the Lok Sabha.",
        "a_ta": "கூற்று (A): சரத்து 275-ன் கீழ் பரிந்துரைக்கப்படும் மானியங்கள் மக்களவையின் வாக்கெடுப்புக்கு உட்படுத்தப்படுவதில்லை.",
        "r_en": "Reason (R): Under the express terms of Article 275(1), these grants are charged on the Consolidated Fund of India.",
        "r_ta": "காரணம் (R): சரத்து 275(1)-ன் வெளிப்படையான விதிகளின்படி, இந்த மானியங்கள் இந்தியத் திரட்டப்பட்ட நிதியில் பொறுப்பாக்கப்பட்டுள்ளன (Charged).",
        "exp_en": "Both (A) and (R) are true and (R) correctly explains why the grants are non-votable under Article 113.",
        "exp_ta": "(A) மற்றும் (R) இரண்டும் சரி, மேலும் சரத்து 113-ன் கீழ் இந்த மானியங்கள் ஏன் வாக்கெடுப்புக்கு உட்பட்டவை அல்ல என்பதை (R) சரியாக விளக்குகிறது.",
        "tip_en": "Charged expenditures are discussed in Parliament but not voted upon under Article 113(1).",
        "tip_ta": "பொறுப்பாக்கப்பட்ட செலவுகள் நாடாளுமன்றத்தில் விவாதிக்கப்படலாம், ஆனால் வாக்கெடுப்புக்கு விடப்படுவதில்லை.",
        "fact_en": "Assam receives special constitutional grants under the second proviso to Article 275(1).",
        "fact_ta": "சரத்து 275(1)-ன் இரண்டாவது வரம்புரையின் கீழ் அசாம் மாநிலம் சிறப்பு அரசியலமைப்பு மானியங்களைப் பெறுகிறது."
    },
    # 6: A
    {
        "subtopic": "Alternative Devolution Scheme Pooling Rationale",
        "key": "A",
        "a_en": "Assertion (A): The 80th Constitutional Amendment Act 2000 pooled almost all Central taxes into a single divisible pool.",
        "a_ta": "கூற்று (A): 2000 ஆம் ஆண்டின் 80வது அரசியலமைப்புத் திருத்தச் சட்டம் ஏறத்தாழ அனைத்து மத்திய வரிகளையும் ஒரே பகிர்வு நிதிக்குள் கொண்டு வந்தது.",
        "r_en": "Reason (R): It eliminated the Centre's disincentive to raise taxes like Corporation Tax and Customs that were previously non-shareable with States.",
        "r_ta": "காரணம் (R): முன்னர் மாநிலங்களுடன் பகிரப்படாத நிறுவன வரி மற்றும் சுங்க வரி போன்ற வரிகளை உயர்த்துவதில் மத்திய அரசு காட்டிய ஆர்வமின்மையை இது ஒழித்தது.",
        "exp_en": "Both (A) and (R) are true and (R) correctly explains the economic rationale of the Tenth FC's Alternative Scheme enacted by the 80th Amendment.",
        "exp_ta": "(A) மற்றும் (R) இரண்டும் சரி, மேலும் 80வது திருத்தம் மூலம் நடைமுறைப்படுத்தப்பட்ட 10வது நிதி ஆணையத்தின் மாற்றுத் திட்டத்தின் பொருளாதாரக் காரணத்தை (R) சரியாக விளக்குகிறது.",
        "tip_en": "The 80th Amendment amended Article 270 retrospectively from April 1, 1996.",
        "tip_ta": "80வது திருத்தம் சரத்து 270-ஐ ஏப்ரல் 1, 1996 முதல் முன்தேதியிட்டு திருத்தியது.",
        "fact_en": "Under the new system, both Union and States share the buoyancy of the entire national tax basket.",
        "fact_ta": "புதிய அமைப்பில், மத்திய மற்றும் மாநிலங்கள் இரண்டும் நாட்டின் ஒட்டுமொத்த வரி வளர்ச்சியின் பலனைப் பகிர்ந்து கொள்கின்றன."
    },
    # 7: A
    {
        "subtopic": "Income Distance Equalization Function",
        "key": "A",
        "a_en": "Assertion (A): Income Distance receives the highest weighting in the horizontal devolution formula across Finance Commissions.",
        "a_ta": "கூற்று (A): நிதி ஆணையங்களின் கிடைமட்ட வரிப் பகிர்வு சூத்திரத்தில் வருமான இடைவெளி மிக அதிக எடையைப் பெறுகிறது.",
        "r_en": "Reason (R): It acts as the primary progressive redistributive instrument to bridge fiscal capacity disparities between richer and poorer States.",
        "r_ta": "காரணம் (R): பணக்கார மற்றும் ஏழை மாநிலங்களுக்கு இடையிலான நிதித் திறன் இடைவெளியைக் குறைப்பதற்கான முதன்மை முற்போக்கு மறுபகிர்வு கருவியாக இது செயல்படுகிறது.",
        "exp_en": "Both (A) and (R) are true and (R) is the fundamental economic justification for giving 45-50% weight to Income Distance.",
        "exp_ta": "(A) மற்றும் (R) இரண்டும் சரி, மேலும் வருமான இடைவெளிக்கு 45-50% எடை வழங்கப்படுவதற்கான அடிப்படை பொருளாதார நியாயத்தை (R) விளக்குகிறது.",
        "tip_en": "Equalization transfer bridges the gap between state revenue capacity and public expenditure needs.",
        "tip_ta": "சமத்துவப் பகிர்வு மாநில வருவாய் திறனுக்கும் பொதுச் செலவினத் தேவைகளுக்கும் இடையிலான இடைவெளியைக் குறைக்கிறது.",
        "fact_en": "14th FC allocated 50% and 15th FC allocated 45% weight to Income Distance.",
        "fact_ta": "14வது ஆணையம் 50% மற்றும் 15வது ஆணையம் 45% எடையை வருமான இடைவெளிக்கு ஒதுக்கின."
    },
    # 8: B
    {
        "subtopic": "Advisory Status vs Political Weight",
        "key": "B",
        "a_en": "Assertion (A): The recommendations of the Finance Commission are legally advisory and not binding on the Union Government.",
        "a_ta": "கூற்று (A): நிதி ஆணையத்தின் பரிந்துரைகள் சட்டப்பூர்வமாக ஆலோசனை இயல்புடையவையே தவிர மத்திய அரசைக் கட்டுப்படுத்துபவை அல்ல.",
        "r_en": "Reason (R): The Chairman of the Finance Commission enjoys the rank and status of a Cabinet Minister in the Union Government.",
        "r_ta": "காரணம் (R): நிதி ஆணையத்தின் தலைவர் மத்திய அரசில் கேபினட் அமைச்சர் அந்தஸ்தையும் தகுதியையும் அனுபவிக்கிறார்.",
        "exp_en": "Both (A) and (R) are true statements, but (R) is not the correct explanation of (A). The advisory nature stems from the constitutional wording of Article 280, not the ministerial protocol rank of the Chairman.",
        "exp_ta": "(A) மற்றும் (R) இரண்டும் சரியான கூற்றுகள், ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல. ஆலோசனை இயல்பு என்பது சரத்து 280-ன் அரசியலமைப்பு வாசகங்களிலிருந்து எழுகிறதே தவிர தலைவரின் அமைச்சர் அந்தஸ்தால் அல்ல.",
        "tip_en": "Advisory nature is a constitutional design choice; protocol rank is an administrative convention.",
        "tip_ta": "ஆலோசனை தன்மை என்பது அரசியலமைப்பு வடிவம்; நெறிமுறை அந்தஸ்து என்பது நிர்வாக மரபு.",
        "fact_en": "Finance Commission members enjoy the rank of a Minister of State.",
        "fact_ta": "நிதி ஆணைய உறுப்பினர்கள் இணை அமைச்சர் அந்தஸ்தை அனுபவிக்கின்றனர்."
    },
    # 9: B
    {
        "subtopic": "State Finance Commission Linkage",
        "key": "B",
        "a_en": "Assertion (A): The Central Finance Commission recommends measures to augment state consolidated funds for local bodies based on State Finance Commission reports.",
        "a_ta": "கூற்று (A): மாநில நிதி ஆணைய அறிக்கைகளின் அடிப்படையில் உள்ளாட்சி அமைப்புகளுக்காக மாநிலத் திரட்டப்பட்ட நிதியை பெருக்க மத்திய நிதி ஆணையம் பரிந்துரைக்கிறது.",
        "r_en": "Reason (R): The 73rd and 74th Constitutional Amendments came into force in 1993.",
        "r_ta": "காரணம் (R): 73 மற்றும் 74வது அரசியலமைப்புத் திருத்தங்கள் 1993-ல் நடைமுறைக்கு வந்தன.",
        "exp_en": "Both (A) and (R) are true facts, but (R) simply states when the amendments came into effect and does not explain the functional mechanics of Article 280(3)(bb) and (c).",
        "exp_ta": "(A) மற்றும் (R) இரண்டும் சரியான உண்மைகள், ஆனால் (R) திருத்தங்கள் எப்போது நடைமுறைக்கு வந்தன என்பதைக் குறிப்பிடுகிறதே தவிர செயல்பாட்டு முறையை விளக்கவில்லை.",
        "tip_en": "73rd/74th CAA inserted sub-clauses (bb) and (c) into Article 280(3).",
        "tip_ta": "73 மற்றும் 74வது திருத்தங்கள் சரத்து 280(3)-ல் (bb) மற்றும் (c) உட்பிரிவுகளைச் சேர்த்தன.",
        "fact_en": "Eleventh FC was the first to implement the amended sub-clauses (bb) and (c) in full.",
        "fact_ta": "திருத்தப்பட்ட (bb) மற்றும் (c) பிரிவுகளை முழுமையாக செயல்படுத்திய முதல் ஆணையம் 11வது நிதி ஆணையமாகும்."
    },
    # 10: B
    {
        "subtopic": "Tenure of the Commission",
        "key": "B",
        "a_en": "Assertion (A): A Finance Commission is constituted by the President every fifth year or at such earlier time as he considers necessary.",
        "a_ta": "கூற்று (A): நிதி ஆணையம் ஒவ்வொரு ஐந்தாவது ஆண்டிலும் அல்லது அவசியமெனக் கருதும் முந்தைய நேரத்திலும் குடியரசுத் தலைவரால் அமைக்கப்படுகிறது.",
        "r_en": "Reason (R): Dr. Arvind Panagariya was appointed as the Chairman of the 16th Finance Commission in December 2023.",
        "r_ta": "காரணம் (R): டாக்டர் அரவிந்த் பனகாரியா டிசம்பர் 2023-ல் 16வது நிதி ஆணையத்தின் தலைவராக நியமிக்கப்பட்டார்.",
        "exp_en": "Both (A) and (R) are true statements, but (R) is a specific factual occurrence and not the explanation for the constitutional rule in (A).",
        "exp_ta": "(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) ஒரு குறிப்பிட்ட உண்மை நிகழ்வே அன்றி (A)-ல் உள்ள அரசியலமைப்பு விதியின் விளக்கம் அல்ல.",
        "tip_en": "Article 280(1) prescribes the quinquennial appointment schedule.",
        "tip_ta": "சரத்து 280(1) ஐந்தாண்டு நியமன அட்டவணையை நிர்ணயிக்கிறது.",
        "fact_en": "The 16th FC is scheduled to submit its recommendations by October 31, 2025.",
        "fact_ta": "16வது நிதி ஆணையம் தனது பரிந்துரைகளை அக்டோபர் 31, 2025-க்குள் சமர்ப்பிக்க வேண்டும்."
    },
    # 11: B
    {
        "subtopic": "Tied vs Untied Local Body Grants",
        "key": "B",
        "a_en": "Assertion (A): The 15th Finance Commission bifurcated rural local body grants into 40% untied and 60% tied grants.",
        "a_ta": "கூற்று (A): 15வது நிதி ஆணையம் ஊரக உள்ளாட்சி மானியங்களை 40% நிபந்தனையற்றவை மற்றும் 60% நிபந்தனைக்குட்பட்டவை எனப் பிரித்தது.",
        "r_en": "Reason (R): Local self-governments are listed under Entry 5 of the State List in the Seventh Schedule.",
        "r_ta": "காரணம் (R): உள்ளாட்சி அமைப்புகள் ஏழாவது அட்டவணையில் மாநிலப் பட்டியலின் பிரிவு 5-ன் கீழ் பட்டியலிடப்பட்டுள்ளன.",
        "exp_en": "Both (A) and (R) are correct, but (R) explains the legislative jurisdiction of States over local bodies and not the 40:60 grant allocation ratio.",
        "exp_ta": "(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) உள்ளாட்சிகள் மீதான மாநில சட்டமன்ற அதிகார வரம்பை விவரிக்கிறதே தவிர 40:60 மானிய விகிதத்தை விளக்கவில்லை.",
        "tip_en": "Tied grants fund national priority goals: water supply and sanitation under Swachh Bharat and Jal Jeevan Mission.",
        "tip_ta": "நிபந்தனை மானியங்கள் தூய்மை பாரதம் மற்றும் ஜல் ஜீவன் இயக்கத்தின் கீழ் குடிநீர் மற்றும் சுகாதாரத்திற்கு நிதியளிக்கின்றன.",
        "fact_en": "Untied grants give Panchayats fiscal autonomy for local discretionary community assets.",
        "fact_ta": "நிபந்தனையற்ற மானியங்கள் உள்ளூர் சமூக சொத்துக்களை உருவாக்க பஞ்சாயத்துகளுக்கு நிதி தன்னாட்சியை வழங்குகின்றன."
    },
    # 12: B
    {
        "subtopic": "Planning Commission Historical Primacy",
        "key": "B",
        "a_en": "Assertion (A): Before 2014, the Planning Commission overshadowed the constitutional Finance Commission in total federal resource transfers.",
        "a_ta": "கூற்று (A): 2014-க்கு முன், ஒட்டுமொத்த கூட்டாட்சி வளப் பகிர்வில் திட்டக் குழு அரசியலமைப்பு நிதி ஆணையத்தை விட அதிக ஆதிக்கம் செலுத்தியது.",
        "r_en": "Reason (R): The Planning Commission was established through an executive resolution of the Union Cabinet in March 1950.",
        "r_ta": "காரணம் (R): திட்டக் குழு மார்ச் 1950-ல் மத்திய அமைச்சரவையின் நிர்வாகத் தீர்மானத்தின் மூலம் நிறுவப்பட்டது.",
        "exp_en": "Both (A) and (R) are correct historical facts, but (R) merely gives the origin date and does not explain why discretionary Article 282 plan grants outgrew statutory transfers.",
        "exp_ta": "(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) திட்டக் குழு உருவான தேதியைக் குறிப்பிடுகிறதே தவிர விருப்ப மானியங்கள் ஏன் சட்டப்பூர்வ மானியங்களை விட அதிகரித்தன என்பதை விளக்கவில்லை.",
        "tip_en": "Planning Commission allocated plan assistance; Finance Commission handled non-plan transfers.",
        "tip_ta": "திட்டக் குழு திட்ட உதவிகளையும், நிதி ஆணையம் திட்டமில்லா நிதிப் பகிர்வையும் கையாண்டன.",
        "fact_en": "NITI Aayog does not distribute financial grants, restoring the Finance Commission's primacy.",
        "fact_ta": "நிதி ஆயோக் நிதி மானியங்களை வழங்குவதில்லை, இது நிதி ஆணையத்தின் முதன்மையை மீட்டெடுத்துள்ளது."
    },
    # 13: B
    {
        "subtopic": "Disaster Response Funding (SDRF)",
        "key": "B",
        "a_en": "Assertion (A): The Central Government contributes 90% of the SDRF allocation for North-Eastern and Himalayan States.",
        "a_ta": "கூற்று (A): வடகிழக்கு மற்றும் இமயமலை மாநிலங்களுக்கான SDRF ஒதுக்கீட்டில் மத்திய அரசு 90% பங்களிக்கிறது.",
        "r_en": "Reason (R): The Disaster Management Act was enacted by the Indian Parliament in 2005.",
        "r_ta": "காரணம் (R): பேரிடர் மேலாண்மைச் சட்டம் 2005-ல் இந்திய நாடாளுமன்றத்தால் இயற்றப்பட்டது.",
        "exp_en": "Both (A) and (R) are true, but (R) states the year of the DM Act and does not explain the ecological and fiscal vulnerability that justifies the 90:10 funding asymmetry.",
        "exp_ta": "(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) சட்டம் இயற்றப்பட்ட ஆண்டைக் குறிப்பிடுகிறதே தவிர 90:10 நிதி சமச்சீரற்ற தன்மையை நியாயப்படுத்தும் சூழலியல் மற்றும் நிதி பலவீனத்தை விளக்கவில்லை.",
        "tip_en": "General category states receive 75% central contribution to SDRF.",
        "tip_ta": "பொதுப் பிரிவு மாநிலங்கள் SDRF-ல் 75% மத்தியப் பங்களிப்பைப் பெறுகின்றன.",
        "fact_en": "Section 48 of the DM Act 2005 governs the constitution of SDRF.",
        "fact_ta": "பேரிடர் மேலாண்மைச் சட்டம் 2005-ன் பிரிவு 48 SDRF உருவாக்கத்தை நிர்வகிக்கிறது."
    },
    # 14: C
    {
        "subtopic": "Binding Power Misconception",
        "key": "C",
        "a_en": "Assertion (A): The President causes every recommendation of the Finance Commission to be laid before each House of Parliament under Article 281.",
        "a_ta": "கூற்று (A): குடியரசுத் தலைவர் சரத்து 281-ன் கீழ் நிதி ஆணையத்தின் ஒவ்வொரு பரிந்துரையையும் நாடாளுமன்றத்தின் இரு அவைகளிலும் வைக்கச் செய்கிறார்.",
        "r_en": "Reason (R): The Constitution declares that all recommendations of the Finance Commission are legally binding on the Government.",
        "r_ta": "காரணம் (R): நிதி ஆணையத்தின் அனைத்து பரிந்துரைகளும் அரசாங்கத்தைக் கட்டுப்படுத்தும் சட்டப்பூர்வ கட்டாயம் கொண்டவை என்று அரசியலமைப்பு அறிவிக்கிறது.",
        "exp_en": "(A) is true because Article 281 mandates tabling the report. (R) is false because recommendations of the Finance Commission are advisory and not legally binding.",
        "exp_ta": "(A) சரி, ஏனெனில் சரத்து 281 அறிக்கையை நாடாளுமன்றத்தில் வைப்பதை கட்டாயமாக்குகிறது. ஆனால் (R) தவறு, ஏனெனில் நிதி ஆணையத்தின் பரிந்துரைகள் ஆலோசனை இயல்புடையவையே அன்றி சட்டப்பூர்வமாகக் கட்டுப்படுத்துபவை அல்ல.",
        "tip_en": "Article 281: Tabling of recommendations with explanatory memorandum.",
        "tip_ta": "சரத்து 281: விளக்கக் குறிப்புடன் பரிந்துரைகளை நாடாளுமன்றத்தில் சமர்ப்பித்தல்.",
        "fact_en": "No provision in the Constitution makes Finance Commission awards legally enforceable decrees.",
        "fact_ta": "நிதி ஆணைய முடிவுகளை சட்டப்பூர்வ தீர்ப்புகளாக மாற்றும் எந்த விதியும் அரசியலமைப்பில் இல்லை."
    },
    # 15: C
    {
        "subtopic": "Cesses Divisible Pool Inclusion Fallacy",
        "key": "C",
        "a_en": "Assertion (A): Several States have petitioned the Union Government demanding a share in cesses and surcharges.",
        "a_ta": "கூற்று (A): செஸ் மற்றும் கூடுதல் வரிகளில் பங்கு கோரி பல மாநிலங்கள் மத்திய அரசிடம் மனு அளித்துள்ளன.",
        "r_en": "Reason (R): Article 271 explicitly includes all surcharges and cesses within the divisible pool distributed to States.",
        "r_ta": "காரணம் (R): சரத்து 271 அனைத்து செஸ் மற்றும் கூடுதல் வரிகளையும் மாநிலங்களுக்குப் பகிர்ந்தளிக்கப்படும் நிதிக்குள் வெளிப்படையாக இணைக்கிறது.",
        "exp_en": "(A) is true as States actively lobby for this reform. (R) is false because Article 271 explicitly excludes surcharges from the divisible pool shared under Article 270.",
        "exp_ta": "(A) சரி, ஏனெனில் மாநிலங்கள் இக்கோரிக்கையை தீவிரமாக முன்வைக்கின்றன. ஆனால் (R) தவறு, ஏனெனில் சரத்து 271 கூடுதல் வரிகளை சரத்து 270 பகிர்வு நிதியிலிருந்து வெளிப்படையாக விலக்குகிறது.",
        "tip_en": "Article 271 surcharges belong entirely to the Union Government.",
        "tip_ta": "சரத்து 271-ன் கீழான கூடுதல் வரிகள் முழுமையாக மத்திய அரசிற்கே உரியவை.",
        "fact_en": "States demand capping cesses at a fixed percentage of Gross Tax Revenue.",
        "fact_ta": "மொத்த வரி வருவாயில் செஸ் வரிகளை ஒரு குறிப்பிட்ட சதவீதத்திற்குள் கட்டுப்படுத்த மாநிலங்கள் கோருகின்றன."
    },
    # 16: C
    {
        "subtopic": "High Court Qualifications Requirement",
        "key": "C",
        "a_en": "Assertion (A): The qualifications of Finance Commission members are determined by Parliament by law under Article 280(2).",
        "a_ta": "கூற்று (A): நிதி ஆணைய உறுப்பினர்களின் தகுதிகள் சரத்து 280(2)-ன் கீழ் சட்டத்தின் மூலம் நாடாளுமன்றத்தால் தீர்மானிக்கப்படுகின்றன.",
        "r_en": "Reason (R): The 1951 Act requires that all four members must be retired Chief Justices of High Courts.",
        "r_ta": "காரணம் (R): நான்கு உறுப்பினர்களும் உயர் நீதிமன்றங்களின் ஓய்வுபெற்ற தலைமை நீதிபதிகளாக இருக்க வேண்டும் என்று 1951 சட்டம் கட்டாயப்படுத்துகிறது.",
        "exp_en": "(A) is true under Article 280(2). (R) is false because only one member needs judicial qualification (High Court judge standard), while others represent accounts, administration, and economics.",
        "exp_ta": "(A) சரி, ஏனெனில் சரத்து 280(2) நாடாளுமன்றத்திற்கு அதிகாரம் அளிக்கிறது. ஆனால் (R) தவறு, ஏனெனில் ஒரு உறுப்பினர் மட்டுமே உயர் நீதிமன்ற நீதிபதி தகுதி கொண்டிருக்க வேண்டும்; மற்றவர்கள் கணக்கு, நிர்வாகம் மற்றும் பொருளாதார நிபுணர்களாவர்.",
        "tip_en": "One judicial member + three members from accounts, finance/admin, and economics.",
        "tip_ta": "ஒரு நீதித்துறை உறுப்பினர் + கணக்கு, நிதி/நிர்வாகம் மற்றும் பொருளாதாரத்திலிருந்து மூன்று உறுப்பினர்கள்.",
        "fact_en": "The multi-disciplinary composition ensures holistic assessment of macro-fiscal federalism.",
        "fact_ta": "பல்துறை கலவை கூட்டாட்சி நிதியின் முழுமையான மதிப்பீட்டை உறுதி செய்கிறது."
    },
    # 17: C
    {
        "subtopic": "Panchayat Grants Substitution Fallacy",
        "key": "C",
        "a_en": "Assertion (A): The 15th Finance Commission allocated Rs. 4.36 lakh crore in grants to local self-governments for 2021-26.",
        "a_ta": "கூற்று (A): 15வது நிதி ஆணையம் 2021-26 காலத்திற்கு உள்ளாட்சி அமைப்புகளுக்கு ரூ. 4.36 லட்சம் கோடி மானியங்களை ஒதுக்கியது.",
        "r_en": "Reason (R): Central Finance Commission grants are designed to replace and extinguish all State budgetary transfers to local bodies.",
        "r_ta": "காரணம் (R): மத்திய நிதி ஆணைய மானியங்கள் உள்ளாட்சி அமைப்புகளுக்கான மாநில பட்ஜெட் நிதிப் பகிர்வை முழுமையாக மாற்றி ஒழிக்கும் வகையில் வடிவமைக்கப்பட்டுள்ளன.",
        "exp_en": "(A) is true as Rs. 4.36 lakh crore was allocated. (R) is completely false because Central grants are supplementary and can never replace state budgetary transfers.",
        "exp_ta": "(A) சரி, ஏனெனில் ரூ. 4.36 லட்சம் கோடி ஒதுக்கப்பட்டது. ஆனால் (R) முற்றிலும் தவறு, ஏனெனில் மத்திய மானியங்கள் கூடுதல் நிதியேயன்றி மாநில நிதிப் பகிர்வுக்கு மாற்றாகாது.",
        "tip_en": "Article 280(3)(bb) uses the specific phrase 'supplement the resources of the Panchayats'.",
        "tip_ta": "சரத்து 280(3)(bb) 'பஞ்சாயத்துகளின் வளங்களை நிரப்புதல்' என்ற குறிப்பிட்ட சொற்றொடரைப் பயன்படுத்துகிறது.",
        "fact_en": "State Finance Commissions continue to recommend separate mandatory state tax devolutions.",
        "fact_ta": "மாநில நிதி ஆணையங்கள் தனித்தனியான கட்டாய மாநில வரிப் பகிர்வுகளை தொடர்ந்து பரிந்துரைக்கின்றன."
    },
    # 18: C
    {
        "subtopic": "Permanent Body Fallacy",
        "key": "C",
        "a_en": "Assertion (A): The Finance Commission is an ad-hoc, temporary body constituted periodically by the President.",
        "a_ta": "கூற்று (A): நிதி ஆணையம் என்பது குடியரசுத் தலைவரால் அவ்வப்போது அமைக்கப்படும் ஒரு தற்காலிக அமைப்பாகும்.",
        "r_en": "Reason (R): Article 280 mandates that the Finance Commission shall function as a continuous permanent institution with fixed tenured commissioners.",
        "r_ta": "காரணம் (R): நிதி ஆணையம் நிலையான பதவிக்காலம் கொண்ட ஆணையாளர்களுடன் ஒரு தொடர்ச்சியான நிரந்தர அமைப்பாக செயல்பட வேண்டும் என்று சரத்து 280 கட்டாயப்படுத்துகிறது.",
        "exp_en": "(A) is true because it dissolves after submitting its report. (R) is false because Article 280 establishes it as a periodic quinquennial body, not a permanent commission.",
        "exp_ta": "(A) சரி, ஏனெனில் அறிக்கையை சமர்ப்பித்த பின் ஆணையம் கலைக்கப்படுகிறது. ஆனால் (R) தவறு, ஏனெனில் சரத்து 280 இதை ஐந்து ஆண்டுகளுக்கு ஒருமுறை கூடும் தற்காலிக அமைப்பாக நிறுவுகிறதே தவிர நிரந்தர அமைப்பாக அல்ல.",
        "tip_en": "Rajamannar Commission recommended making FC a permanent body, but it remains periodic.",
        "tip_ta": "ராஜமன்னார் ஆணையம் நிதி ஆணையத்தை நிரந்தர அமைப்பாக மாற்ற பரிந்துரைத்தது, ஆனால் அது இன்னும் காலமுறை அமைப்பாகவே உள்ளது.",
        "fact_en": "The Commission dissolves immediately once its final report and accounts are submitted to the President.",
        "fact_ta": "இறுதி அறிக்கை மற்றும் கணக்குகளை குடியரசுத் தலைவரிடம் சமர்ப்பித்தவுடன் ஆணையம் கலைக்கப்படுகிறது."
    },
    # 19: C
    {
        "subtopic": "2011 Census Standalone Weight Fallacy",
        "key": "C",
        "a_en": "Assertion (A): The 15th Finance Commission assigned 15% weight to Population in its horizontal devolution formula.",
        "a_ta": "கூற்று (A): 15வது நிதி ஆணையம் தனது கிடைமட்ட வரிப் பகிர்வு சூத்திரத்தில் மக்கள் தொகைக்கு 15% எடையை ஒதுக்கியது.",
        "r_en": "Reason (R): The 15th Finance Commission exclusively utilized the 1971 Census to calculate this 15% population share.",
        "r_ta": "காரணம் (R): இந்த 15% மக்கள் தொகை பங்கை கணக்கிட 15வது நிதி ஆணையம் 1971 மக்கள் தொகை கணக்கெடுப்பை மட்டுமே பயன்படுத்தியது.",
        "exp_en": "(A) is true as Population has 15% weight. (R) is false because the 15th FC used the 2011 Census population data as mandated by its Terms of Reference.",
        "exp_ta": "(A) சரி, ஏனெனில் மக்கள் தொகைக்கு 15% எடை உள்ளது. ஆனால் (R) தவறு, ஏனெனில் 15வது ஆணையம் தனது பணிக் குறிப்புகளின்படி 2011 மக்கள் தொகை கணக்கெடுப்புத் தரவையே பயன்படுத்தியது.",
        "tip_en": "15th FC switched completely to 2011 Census for population and introduced Demographic Performance to balance.",
        "tip_ta": "15வது ஆணையம் 2011 மக்கள் தொகைக்கு முழுமையாக மாறியது, அதை சமன் செய்ய மக்கள்தொகை செயல்திறனை அறிமுகப்படுத்தியது.",
        "fact_en": "Previous commissions (8th to 14th) used 1971 population to protect family planning pioneers.",
        "fact_ta": "முந்தைய ஆணையங்கள் (8 முதல் 14 வரை) குடும்பக் கட்டுப்பாட்டு முன்னோடி மாநிலங்களைப் பாதுகாக்க 1971 மக்கள் தொகையைப் பயன்படுத்தின."
    },
    # 20: D
    {
        "subtopic": "CAG vs Finance Commission Confusion",
        "key": "D",
        "a_en": "Assertion (A): The Finance Commission audits the annual revenue accounts of the Union and State Governments.",
        "a_ta": "கூற்று (A): நிதி ஆணையம் மத்திய மற்றும் மாநில அரசுகளின் வருடாந்திர வருவாய்க் கணக்குகளைத் தணிக்கை செய்கிறது.",
        "r_en": "Reason (R): The Comptroller and Auditor General of India is the constitutional authority under Article 148 responsible for auditing public accounts.",
        "r_ta": "காரணம் (R): இந்தியக் கணக்குத் தணிக்கைத் தலைவர் (CAG) சரத்து 148-ன் கீழ் பொதுக் கணக்குகளைத் தணிக்கை செய்யும் அரசியலமைப்பு அதிகாரியாவார்.",
        "exp_en": "(A) is false because the Finance Commission recommends tax sharing and does not conduct audits. (R) is true as CAG is the supreme audit authority.",
        "exp_ta": "(A) தவறு, ஏனெனில் நிதி ஆணையம் வரிப் பகிர்வை மட்டுமே பரிந்துரைக்கிறது, தணிக்கை செய்வதில்லை. (R) சரி, ஏனெனில் சி.ஏ.ஜி உச்ச தணிக்கை அதிகாரி ஆவார்.",
        "tip_en": "FC = Fiscal devolution (Art 280). CAG = Public accounts audit (Art 148-151).",
        "tip_ta": "நிதி ஆணையம் = நிதிப் பகிர்வு (சரத்து 280). சி.ஏ.ஜி = பொதுக் கணக்கு தணிக்கை (சரத்து 148-151).",
        "fact_en": "The FC relies heavily on certified audit figures provided by the CAG.",
        "fact_ta": "நிதி ஆணையம் சி.ஏ.ஜி வழங்கும் சான்றளிக்கப்பட்ட தணிக்கை புள்ளிவிவரங்களை பெரிதும் நம்பியுள்ளது."
    },
    # 21: D
    {
        "subtopic": "State Borrowing Power Distortion",
        "key": "D",
        "a_en": "Assertion (A): A State Government can raise sovereign loans in international foreign financial markets without Central Government consent.",
        "a_ta": "கூற்று (A): ஒரு மாநில அரசு மத்திய அரசின் அனுமதியின்றி சர்வதேச வெளிநாட்டு நிதிச் சந்தைகளில் இறையாண்மைக் கடன்களைத் திரட்ட முடியும்.",
        "r_en": "Reason (R): Under Article 293(1), the executive power of a State to borrow is restricted to the territory of India upon the security of the Consolidated Fund of the State.",
        "r_ta": "காரணம் (R): சரத்து 293(1)-ன் கீழ், மாநிலத்தின் கடன் வாங்கும் அதிகாரம் மாநிலத் திரட்டப்பட்ட நிதியின் பாதுகாப்பில் இந்தியாவின் எல்லைக்குள் மட்டுமே மட்டுப்படுத்தப்பட்டுள்ளது.",
        "exp_en": "(A) is false because States have no constitutional power to borrow externally. (R) is true under Article 293(1).",
        "exp_ta": "(A) தவறு, ஏனெனில் மாநிலங்களுக்கு வெளிநாடுகளில் கடன் வாங்கும் அதிகாரம் இல்லை. (R) சரத்து 293(1)-ன் படி சரியானது.",
        "tip_en": "Only the Union Government can borrow externally under Article 292.",
        "tip_ta": "சரத்து 292-ன் கீழ் மத்திய அரசு மட்டுமே வெளிநாடுகளில் கடன் வாங்க முடியும்.",
        "fact_en": "External developmental loans (World Bank, ADB) are routed through the Union Government to States.",
        "fact_ta": "வெளிநாட்டு வளர்ச்சி கடன்கள் (உலக வங்கி, ADB) மத்திய அரசு மூலமாகவே மாநிலங்களுக்கு வழங்கப்படுகின்றன."
    },
    # 22: D
    {
        "subtopic": "Criminal Contempt Power Distortion",
        "key": "D",
        "a_en": "Assertion (A): The Finance Commission has the constitutional authority to sentence recalcitrant departmental witnesses to criminal imprisonment.",
        "a_ta": "கூற்று (A): ஒத்துழைக்காத துறைசார் சாட்சிகளுக்கு குற்றவியல் சிறைத்தண்டனை விதிக்கும் அரசியலமைப்பு அதிகாரம் நிதி ஆணையத்திற்கு உண்டு.",
        "r_en": "Reason (R): The Finance Commission possesses only the evidentiary powers of a Civil Court for summoning persons and requisitioning records.",
        "r_ta": "காரணம் (R): நபர்களை ஆஜராக அழைப்பதற்கும் ஆவணங்களைக் கோருவதற்கும் சிவில் நீதிமன்றத்தின் சாட்சிய அதிகாரங்கள் மட்டுமே நிதி ஆணையத்திற்கு உண்டு.",
        "exp_en": "(A) is false as the Commission has no criminal trial powers or penal sentencing jurisdiction. (R) is true under Section 8 of the 1951 Act.",
        "exp_ta": "(A) தவறு, ஏனெனில் ஆணையத்திற்கு குற்றவியல் விசாரணை அல்லது சிறைத்தண்டனை விதிக்கும் அதிகாரம் இல்லை. 1951 சட்டத்தின் பிரிவு 8-ன் கீழ் (R) சரியானது.",
        "tip_en": "Civil court powers under CPC: summoning, receiving affidavits, discovering documents.",
        "tip_ta": "சிவில் நீதிமன்ற அதிகாரங்கள்: அழைப்பாணை, வாக்குமூலம் பெறுதல், ஆவணங்களை ஆய்வு செய்தல்.",
        "fact_en": "Commission cannot impose criminal sanctions on any individual.",
        "fact_ta": "ஆணையம் எந்தவொரு நபர் மீதும் குற்றவியல் தண்டனைகளை விதிக்க முடியாது."
    },
    # 23: D
    {
        "subtopic": "Election by Parliament Distortion",
        "key": "D",
        "a_en": "Assertion (A): Members of the Finance Commission are elected through proportional representation by members of Parliament.",
        "a_ta": "கூற்று (A): நிதி ஆணைய உறுப்பினர்கள் நாடாளுமன்ற உறுப்பினர்களால் விகிதாசார பிரதிநிதித்துவ முறைப்படி தேர்ந்தெடுக்கப்படுகிறார்கள்.",
        "r_en": "Reason (R): Article 280(1) mandates that the Chairman and members shall be appointed directly by the President of India.",
        "r_ta": "காரணம் (R): தலைவர் மற்றும் உறுப்பினர்கள் நேரடியாக இந்தியக் குடியரசுத் தலைவரால் நியமிக்கப்பட வேண்டும் என்று சரத்து 280(1) கட்டாயப்படுத்துகிறது.",
        "exp_en": "(A) is false because members are appointed by the President by warrant, not elected by Parliament. (R) is true under Article 280(1).",
        "exp_ta": "(A) தவறு, ஏனெனில் உறுப்பினர்கள் குடியரசுத் தலைவரால் நியமிக்கப்படுகிறார்களே தவிர நாடாளுமன்றத்தால் தேர்ந்தெடுக்கப்படுவதில்லை. சரத்து 280(1)-ன் கீழ் (R) சரியானது.",
        "tip_en": "Appointment by President upon recommendation of the Union Cabinet.",
        "tip_ta": "மத்திய அமைச்சரவையின் பரிந்துரையின் பேரில் குடியரசுத் தலைவரால் நியமிக்கப்படுகிறார்கள்.",
        "fact_en": "Parliament's role is strictly legislative—defining qualifications under Article 280(2).",
        "fact_ta": "சரத்து 280(2)-ன் கீழ் தகுதிகளை வரையறுக்கும் சட்டமன்றப் பொறுப்பு மட்டுமே நாடாளுமன்றத்திற்கு உண்டு."
    },
    # 24: D
    {
        "subtopic": "State List Elimination Fallacy",
        "key": "D",
        "a_en": "Assertion (A): The recommendations of the Finance Commission have abolished all state indirect taxing powers under the State List.",
        "a_ta": "கூற்று (A): நிதி ஆணையத்தின் பரிந்துரைகள் மாநிலப் பட்டியலின் கீழான அனைத்து மாநில மறைமுக வரி அதிகாரங்களையும் ரத்து செய்துவிட்டன.",
        "r_en": "Reason (R): States retain independent constitutional authority to levy taxes on items like alcoholic liquor for human consumption and petroleum products.",
        "r_ta": "காரணம் (R): மனித நுகர்வுக்கான மதுபானம் மற்றும் பெட்ரோலியப் பொருட்கள் போன்ற பொருட்களின் மீது வரி விதிக்க மாநிலங்கள் சுயாதீன அரசியலமைப்பு அதிகாரத்தைத் தக்கவைத்துள்ளன.",
        "exp_en": "(A) is false as the FC cannot amend the Seventh Schedule or abolish state taxes. (R) is true under Entry 51 and 54 of List II.",
        "exp_ta": "(A) தவறு, ஏனெனில் நிதி ஆணையத்தால் ஏழாவது அட்டவணையைத் திருத்தவோ மாநில வரிகளை ரத்து செய்யவோ முடியாது. பட்டியல் II-ன் கீழ் (R) சரியானது.",
        "tip_en": "State VAT on alcohol and fuel remains a massive independent revenue source for States.",
        "tip_ta": "மது மற்றும் எரிபொருள் மீதான மாநில வாட் வரி மாநிலங்களுக்கு ஒரு பெரிய சுயாதீன வருவாய் ஆதாரமாக உள்ளது.",
        "fact_en": "The 101st Amendment modified tax powers, not the Finance Commission awards.",
        "fact_ta": "101வது அரசியலமைப்புத் திருத்தமே வரி அதிகாரங்களை மாற்றியமைத்ததே தவிர நிதி ஆணையம் அல்ல."
    },
    # 25: D
    {
        "subtopic": "Disaster Relief Executive Proclamation Fallacy",
        "key": "D",
        "a_en": "Assertion (A): The Union Cabinet Secretary can arbitrarily cancel SDRF statutory allocations to States by an executive memo.",
        "a_ta": "கூற்று (A): மத்திய அமைச்சரவைச் செயலாளர் ஒரு நிர்வாகக் குறிப்பின் மூலம் மாநிலங்களுக்கான SDRF சட்டப்பூர்வ ஒதுக்கீடுகளை தன்னிச்சையாக ரத்து செய்ய முடியும்.",
        "r_en": "Reason (R): SDRF allocations are institutionalized statutory transfers established under the Disaster Management Act 2005 based on Finance Commission awards.",
        "r_ta": "காரணம் (R): SDRF ஒதுக்கீடுகள் என்பது நிதி ஆணையத்தின் பரிந்துரைகளின் அடிப்படையில் 2005 பேரிடர் மேலாண்மைச் சட்டத்தின் கீழ் நிறுவப்பட்ட சட்டப்பூர்வ நிதியாகும்.",
        "exp_en": "(A) is false because executive bureaucrats cannot override statutory disaster allocations. (R) is true under Section 48 of the DM Act 2005.",
        "exp_ta": "(A) தவறு, ஏனெனில் நிர்வாக அதிகாரிகளால் சட்டப்பூர்வ பேரிடர் ஒதுக்கீடுகளை ரத்து செய்ய முடியாது. 2005 சட்டத்தின் பிரிவு 48-ன் படி (R) சரியானது.",
        "tip_en": "SDRF releases follow strict statutory rules notified under MHA guidelines.",
        "tip_ta": "மத்திய உள்துறை வழிகாட்டுதல்களின் கீழ் SDRF நிதி விடுவிப்பு கடுமையான விதிகளின்படி நடைபெறுகிறது.",
        "fact_en": "Allocations are credited in two equal installments annually in June and December.",
        "fact_ta": "ஒவ்வொரு ஆண்டும் ஜூன் மற்றும் டிசம்பர் மாதங்களில் இரண்டு சம தவணைகளாக இந்த நிதி வரவு வைக்கப்படுகிறது."
    }
]

def build_questions():
    questions = []
    for idx, item in enumerate(raw_reasoning_items, start=1):
        qid = f"FC_R_{idx:03d}"
        stem_en = f"{item['a_en']}\n{item['r_en']}\nIn the context of the statements above, which of the following is correct?"
        stem_ta = f"{item['a_ta']}\n{item['r_ta']}\nமேற்கண்ட கூற்றுகளின் பின்னணியில், பின்வருவனவற்றில் எது சரியானது?"
        
        correct_k = item["key"]
        
        why_en = {
            "A": "Option A: Both A and R are true and R is the correct explanation of A." if correct_k == "A" else "Option A is incorrect in this context.",
            "B": "Option B: Both A and R are true but R is not the correct explanation of A." if correct_k == "B" else "Option B is incorrect in this context.",
            "C": "Option C: A is true but R is false." if correct_k == "C" else "Option C is incorrect in this context.",
            "D": "Option D: A is false but R is true." if correct_k == "D" else "Option D is incorrect in this context."
        }
        why_ta = {
            "A": "தெரிவு A: (A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கம்." if correct_k == "A" else "தெரிவு A தவறானது.",
            "B": "தெரிவு B: (A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல." if correct_k == "B" else "தெரிவு B தவறானது.",
            "C": "தெரிவு C: (A) சரி ஆனால் (R) தவறு." if correct_k == "C" else "தெரிவு C தவறானது.",
            "D": "தெரிவு D: (A) தவறு ஆனால் (R) சரி." if correct_k == "D" else "தெரிவு D தவறானது."
        }
        
        q = make_fc_q(
            qid=qid,
            diff="Medium",
            qtype="Assertion and Reasoning",
            subtopic=item["subtopic"],
            en_stem=stem_en,
            ta_stem=stem_ta,
            en_a=opts_en[0],
            ta_a=opts_ta[0],
            en_b=opts_en[1],
            ta_b=opts_ta[1],
            en_c=opts_en[2],
            ta_c=opts_ta[2],
            en_d=opts_en[3],
            ta_d=opts_ta[3],
            correct_key=correct_k,
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
            tags=["polity", "finance_commission", "assertion_reasoning", item["subtopic"].lower().replace(" ", "_")]
        )
        questions.append(q)
    return questions

if __name__ == "__main__":
    qs = build_questions()
    print(f"Generated {len(qs)} raw Reasoning questions for Finance Commission.")
    assert len(qs) == 25, f"Expected 25 questions, got {len(qs)}"
    
    out_path = os.path.join("data", "questions", "polity", "fc_reasoning.json")
    alias_path = os.path.join("data", "questions", "polity", "fc_assertion_reason.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, ensure_ascii=False, indent=2)
    shutil.copyfile(out_path, alias_path)
    print(f"Saved Reasoning MCQs to {out_path} and alias {alias_path}")
    
    val = ContentValidator()
    report = val.validate_file(out_path, expected_count=25, expected_prefix="FC_R_")
    print(f"Validation Report: {'PASS' if report.is_valid else 'FAIL'} | Total: {report.total_audited}")
    if not report.is_valid:
        for iss in report.issues[:10]:
            print(f"  Issue: {iss}")
    print(f"Key Distribution: {report.key_distribution}")
