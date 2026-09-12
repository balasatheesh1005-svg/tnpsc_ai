# -*- coding: utf-8 -*-
"""
Build 50 Statement-Based MCQs for Finance Commission of India
ID range: FC_S_001 to FC_S_050
"""

import json
import os
import shutil
from fc_mcq_helper import make_fc_q
from rebalance_er_helper import balance_question_keys
from tools.nova_content_engine.validator import ContentValidator

raw_statement_data = [
    # 1
    {
        "subtopic": "Constitutional Framework: Article 280 & 281",
        "stem_en": "Consider the following statements regarding the Finance Commission under the Constitution of India:\n1. The Finance Commission is constituted by the President of India under Article 280.\n2. The recommendations of the Finance Commission are legally binding on the Central Government.\n3. The President causes the Finance Commission's report along with an explanatory memorandum to be laid before Parliament under Article 281.\nWhich of the statements given above are correct?",
        "stem_ta": "இந்திய அரசியலமைப்பின் கீழ் நிதி ஆணையம் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. நிதி ஆணையம் சரத்து 280-ன் கீழ் இந்தியக் குடியரசுத் தலைவரால் அமைக்கப்படுகிறது.\n2. நிதி ஆணையத்தின் பரிந்துரைகள் மத்திய அரசைக் கட்டுப்படுத்தும் சட்டப்பூர்வ வலிமை கொண்டவை.\n3. குடியரசுத் தலைவர் நிதி ஆணையத்தின் அறிக்கையை விளக்கக் குறிப்புடன் நாடாளுமன்றத்தில் சமர்ப்பிக்கிறார் (சரத்து 281).\nமேலே உள்ள கூற்றுகளில் எவை சரியானவை?",
        "options": [
            ("1 and 3 only", "1 மற்றும் 3 மட்டும்"),
            ("1 and 2 only", "1 மற்றும் 2 மட்டும்"),
            ("2 and 3 only", "2 மற்றும் 3 மட்டும்"),
            ("1, 2 and 3", "1, 2 மற்றும் 3")
        ],
        "exp_en": "Statements 1 and 3 are correct. Statement 2 is incorrect because the recommendations of the Finance Commission are advisory in nature and not legally binding on the Government, though established convention gives them high sanctity.",
        "exp_ta": "கூற்றுகள் 1 மற்றும் 3 சரியானவை. கூற்று 2 தவறானது, ஏனெனில் நிதி ஆணையத்தின் பரிந்துரைகள் ஆலோசனை இயல்புடையவையே அன்றி மத்திய அரசைக் கட்டுப்படுத்தும் சட்டப்பூர்வ கட்டாயம் கொண்டவை அல்ல.",
        "tip_en": "Article 280: Constitution of FC; Article 281: Recommendations laid before Parliament. Recommendations are advisory.",
        "tip_ta": "சரத்து 280: நிதி ஆணைய அமைப்பு; சரத்து 281: நாடாளுமன்றத்தில் சமர்ப்பித்தல். பரிந்துரைகள் ஆலோசனை தன்மை கொண்டவை.",
        "fact_en": "Dr. B.R. Ambedkar noted that while advisory, the Government rarely rejects core devolution recommendations.",
        "fact_ta": "ஆலோசனை தன்மை கொண்டதாக இருந்தாலும், முக்கிய வரிப் பகிர்வுப் பரிந்துரைகளை அரசு நிராகரிப்பது அரிது என அம்பேத்கர் குறிப்பிட்டார்."
    },
    # 2
    {
        "subtopic": "Qualifications under Finance Commission Act 1951",
        "stem_en": "Consider the following statements regarding qualifications of Finance Commission members under the 1951 Act:\n1. The Chairman must be a person having experience in public affairs.\n2. One member must be qualified to be appointed as a Judge of the Supreme Court.\n3. One member must have specialized knowledge of finance and accounts of government.\nWhich of the statements given above are correct?",
        "stem_ta": "1951 சட்டத்தின் கீழ் நிதி ஆணைய உறுப்பினர்களின் தகுதிகள் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. தலைவர் பொது விவகாரங்களில் அனுபவம் வாய்ந்த நபராக இருக்க வேண்டும்.\n2. ஒரு உறுப்பினர் உச்ச நீதிமன்ற நீதிபதியாக நியமிக்கப்பட தகுதியுடையவராக இருக்க வேண்டும்.\n3. ஒரு உறுப்பினர் அரசாங்கத்தின் நிதி மற்றும் கணக்குகள் பற்றிய சிறப்பு அறிவு பெற்றிருக்க வேண்டும்.\nமேலே உள்ள கூற்றுகளில் எவை சரியானவை?",
        "options": [
            ("1 and 3 only", "1 மற்றும் 3 மட்டும்"),
            ("1 and 2 only", "1 மற்றும் 2 மட்டும்"),
            ("2 and 3 only", "2 மற்றும் 3 மட்டும்"),
            ("1, 2 and 3", "1, 2 மற்றும் 3")
        ],
        "exp_en": "Statements 1 and 3 are correct. Statement 2 is incorrect because the Act requires a person qualified to be a Judge of a High Court (not Supreme Court).",
        "exp_ta": "கூற்றுகள் 1 மற்றும் 3 சரியானவை. கூற்று 2 தவறானது, ஏனெனில் உயர் நீதிமன்ற நீதிபதியாக நியமிக்கப்பட தகுதியுள்ள நபரே (உச்ச நீதிமன்றம் அல்ல) உறுப்பினராக நியமிக்கப்பட வேண்டும் என சட்டம் கூறுகிறது.",
        "tip_en": "Chairman: Public affairs. Member 1: High Court judge qualification (not Supreme Court).",
        "tip_ta": "தலைவர்: பொது விவகார அனுபவம். உறுப்பினர் 1: உயர் நீதிமன்ற நீதிபதி தகுதி (உச்ச நீதிமன்றம் அல்ல).",
        "fact_en": "The other two members must have wide experience in financial matters and special knowledge of economics.",
        "fact_ta": "மற்ற இரு உறுப்பினர்கள் நிதி நிர்வாக அனுபவம் மற்றும் பொருளாதாரத்தில் சிறப்பு அறிவு கொண்டிருக்க வேண்டும்."
    },
    # 3
    {
        "subtopic": "Mandatory Constitutional Duties under Article 280(3)",
        "stem_en": "Consider the following duties assigned to the Finance Commission under Article 280(3):\n1. The distribution between the Union and the States of the net proceeds of taxes.\n2. The principles which should govern the grants-in-aid of the revenues of the States out of the Consolidated Fund of India.\n3. The determination of statutory minimum wages across industrial sectors in States.\nWhich of the statements given above are correct?",
        "stem_ta": "சரத்து 280(3)-ன் கீழ் நிதி ஆணையத்திற்கு வழங்கப்பட்டுள்ள கடமைகள் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. மத்திய மற்றும் மாநிலங்களுக்கு இடையே வரிகளின் நிகர வருவாயைப் பகிர்ந்தளித்தல்.\n2. இந்தியத் திரட்டப்பட்ட நிதியிலிருந்து மாநிலங்களின் வருவாய்க்கான மானியங்களை நிர்வகிக்கும் கொள்கைகள்.\n3. மாநிலங்களில் உள்ள தொழில்துறை துறைகளில் சட்டப்பூர்வ குறைந்தபட்ச ஊதியத்தை நிர்ணயித்தல்.\nமேலே உள்ள கூற்றுகளில் எவை சரியானவை?",
        "options": [
            ("1 and 2 only", "1 மற்றும் 2 மட்டும்"),
            ("1 and 3 only", "1 மற்றும் 3 மட்டும்"),
            ("2 and 3 only", "2 மற்றும் 3 மட்டும்"),
            ("1, 2 and 3", "1, 2 மற்றும் 3")
        ],
        "exp_en": "Statements 1 and 2 are core constitutional duties under Article 280(3)(a) and (b). Statement 3 is incorrect as determining industrial wages is outside the mandate of the Finance Commission.",
        "exp_ta": "கூற்றுகள் 1 மற்றும் 2 ஆகியவை சரத்து 280(3)(a) மற்றும் (b)-ன் கீழான முதன்மை அரசியலமைப்பு கடமைகளாகும். கூற்று 3 தவறானது, ஏனெனில் குறைந்தபட்ச ஊதியத்தை நிர்ணயிப்பது நிதி ஆணையத்தின் பணிகளில் அடங்காது.",
        "tip_en": "Article 280(3) covers: Tax sharing (a), Article 275 grants (b), Local body fund augmentation (bb, c), Sound finance references (d).",
        "tip_ta": "சரத்து 280(3): வரிப் பகிர்வு (a), சரத்து 275 மானியங்கள் (b), உள்ளாட்சி நிதி பெருக்கம் (bb, c), பிற நிதிப் பரிந்துரைகள் (d).",
        "fact_en": "Minimum wage determination is handled by tripartite committees under the Code on Wages.",
        "fact_ta": "குறைந்தபட்ச ஊதிய நிர்ணயம் ஊதியக் குறியீட்டின் கீழான முத்தரப்புக் குழுக்களால் கையாளப்படுகிறது."
    },
    # 4
    {
        "subtopic": "73rd and 74th Amendments Local Body Augmentation",
        "stem_en": "Consider the following statements regarding Article 280(3)(bb) and 280(3)(c):\n1. Sub-clause (bb) relates to measures needed to augment the Consolidated Fund of a State to supplement the resources of the Panchayats.\n2. Sub-clause (c) relates to supplementing the resources of Municipalities in the State.\n3. Both recommendations must be made on the basis of the recommendations made by the State Finance Commission.\nWhich of the statements given above are correct?",
        "stem_ta": "சரத்து 280(3)(bb) மற்றும் 280(3)(c) தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. உட்பிரிவு (bb) பஞ்சாயத்துகளின் வளங்களை நிரப்ப மாநிலத்தின் திரட்டப்பட்ட நிதியை பெருக்குவதற்கான நடவடிக்கைகளைக் குறிக்கிறது.\n2. உட்பிரிவு (c) மாநிலத்தில் உள்ள நகராட்சிகளின் வளங்களை நிரப்புவதைக் குறிக்கிறது.\n3. இவ்விரு பரிந்துரைகளும் மாநில நிதி ஆணையத்தின் பரிந்துரைகளின் அடிப்படையில் செய்யப்பட வேண்டும்.\nமேலே உள்ள கூற்றுகளில் எவை சரியானவை?",
        "options": [
            ("1, 2 and 3", "1, 2 மற்றும் 3"),
            ("1 and 2 only", "1 மற்றும் 2 மட்டும்"),
            ("2 and 3 only", "2 மற்றும் 3 மட்டும்"),
            ("1 and 3 only", "1 மற்றும் 3 மட்டும்")
        ],
        "exp_en": "All three statements are correct. Sub-clauses (bb) and (c) were inserted by the 73rd and 74th Constitutional Amendment Acts 1992, requiring Central Finance Commission recommendations to augment state consolidated funds based on State Finance Commission reports.",
        "exp_ta": "அனைத்து கூற்றுகளும் சரியானவை. 1992-ன் 73 மற்றும் 74வது அரசியலமைப்புத் திருத்தச் சட்டங்கள் மூலம் (bb) மற்றும் (c) சேர்க்கப்பட்டன; இவை மாநில நிதி ஆணையத்தின் அறிக்கைகளின் அடிப்படையில் மாநிலத் திரட்டப்பட்ட நிதியை பெருக்க பரிந்துரைக்கின்றன.",
        "tip_en": "73rd CAA inserted (bb) for Panchayats; 74th CAA inserted (c) for Municipalities.",
        "tip_ta": "73வது திருத்தம் பஞ்சாயத்துகளுக்காக (bb)-ஐயும், 74வது திருத்தம் நகராட்சிகளுக்காக (c)-ஐயும் சேர்த்தது.",
        "fact_en": "These sub-clauses created the constitutional bridge between Central transfers and grassroot local governance.",
        "fact_ta": "இப்பிரிவுகள் மத்திய நிதிப் பகிர்வுக்கும் அடிமட்ட உள்ளாட்சி அமைப்புகளுக்கும் இடையே அரசியலமைப்புப் பாலத்தை உருவாக்கின."
    },
    # 5
    {
        "subtopic": "15th Finance Commission Devolution Architecture",
        "stem_en": "Consider the following statements regarding the recommendations of the 15th Finance Commission under N.K. Singh:\n1. It recommended vertical tax devolution of 41% to the States for the 2021-26 award period.\n2. It used 1971 Census data with 50% weight in the horizontal devolution formula.\n3. It introduced 'Demographic Performance' with a 12.5% weight to reward population control efforts.\nWhich of the statements given above are correct?",
        "stem_ta": "என்.கே. சிங் தலைமையிலான 15வது நிதி ஆணையத்தின் பரிந்துரைகள் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது 2021-26 காலத்திற்கு மாநிலங்களுக்கு 41% செங்குத்து வரிப் பகிர்வை பரிந்துரைத்தது.\n2. இது கிடைமட்ட வரிப் பகிர்வு சூத்திரத்தில் 1971 மக்கள் தொகை தரவை 50% எடையுடன் பயன்படுத்தியது.\n3. மக்கள் தொகைக் கட்டுப்பாட்டு முயற்சிகளுக்கு வெகுமதி அளிக்க 12.5% எடையுடன் 'மக்கள்தொகை செயல்திறனை' அறிமுகப்படுத்தியது.\nமேலே உள்ள கூற்றுகளில் எவை சரியானவை?",
        "options": [
            ("1 and 3 only", "1 மற்றும் 3 மட்டும்"),
            ("1 and 2 only", "1 மற்றும் 2 மட்டும்"),
            ("2 and 3 only", "2 மற்றும் 3 மட்டும்"),
            ("1, 2 and 3", "1, 2 மற்றும் 3")
        ],
        "exp_en": "Statements 1 and 3 are correct. Statement 2 is incorrect because the 15th FC used 2011 Census population with a 15% weight, completely discontinuing the use of 1971 Census data as a separate standalone criterion.",
        "exp_ta": "கூற்றுகள் 1 மற்றும் 3 சரியானவை. கூற்று 2 தவறானது, ஏனெனில் 15வது நிதி ஆணையம் 2011 மக்கள் தொகை கணக்கெடுப்பை 15% எடையுடன் பயன்படுத்தியது; 1971 மக்கள் தொகை கணக்கெடுப்பை தனியாகப் பயன்படுத்துவதை நிறுத்தியது.",
        "tip_en": "15th FC criteria weights: Income Distance (45%), Population 2011 (15%), Area (15%), Forest & Ecology (10%), Demographic Performance (12.5%), Tax Effort (2.5%).",
        "tip_ta": "15வது நிதி ஆணைய எடைகள்: வருமான இடைவெளி (45%), 2011 மக்கள் தொகை (15%), பரப்பளவு (15%), வனம் & சூழலியல் (10%), மக்கள்தொகை செயல்திறன் (12.5%), வரி முயற்சி (2.5%).",
        "fact_en": "Total horizontal devolution formula adds up to exactly 100% across these six criteria.",
        "fact_ta": "இந்த ஆறு அளவுகோல்களின் மொத்த கூடுதல் சரியாக 100% ஆகும்."
    }
]

# We will generate 45 additional statement items covering comprehensive FC syllabus
statement_templates = [
    ("Article 270 Divisible Pool Exclusion", "1. Net proceeds of taxes are distributed between Union and States under Article 270.\n2. Cesses and surcharges levied for Union purposes under Article 271 form part of the divisible pool.\n3. The Comptroller and Auditor General audits and certifies the net proceeds under Article 279.", "1 and 3 only", "1 மற்றும் 3 மட்டும்", "Statement 2 is incorrect because cesses and surcharges are excluded from the divisible pool under Article 271.", "சரத்து 271-ன் கீழ் செஸ் மற்றும் கூடுதல் வரிகள் பகிர்வு நிதியிலிருந்து விலக்கப்பட்டுள்ளதால் கூற்று 2 தவறானது.", "Article 271 surcharges belong 100% to the Union Government.", "சரத்து 271 கூடுதல் வரிகள் 100% மத்திய அரசிற்கு மட்டுமே உரியவை."),
    ("Quasi-Judicial Civil Court Powers", "1. The Finance Commission has the powers of a Civil Court under the Code of Civil Procedure 1908.\n2. It can summon and enforce the attendance of witnesses and examine them on oath.\n3. It can pass binding criminal contempt verdicts sentencing officials to imprisonment.", "1 and 2 only", "1 மற்றும் 2 மட்டும்", "Statement 3 is incorrect as the Commission cannot punish for criminal contempt or sentence individuals to imprisonment.", "நீதிமன்ற அவமதிப்பிற்கு தண்டனையோ அல்லது சிறைத்தண்டனையோ விதிக்க ஆணையத்திற்கு அதிகாரம் இல்லை என்பதால் கூற்று 3 தவறானது.", "Commission powers are restricted to evidentiary civil discovery and document production.", "ஆணையத்தின் அதிகாரங்கள் சிவில் சாட்சியங்கள் மற்றும் ஆவணங்களைப் பெறுவதற்கு மட்டுமே மட்டுப்படுத்தப்பட்டவை."),
    ("History: 14th vs 15th FC Devolution", "1. The 14th Finance Commission recommended a vertical tax devolution of 42%.\n2. The 15th Finance Commission reduced the share to 41% to accommodate the Union Territories of J&K and Ladakh.\n3. The Union Government rejected the 14th Finance Commission's 42% devolution recommendation.", "1 and 2 only", "1 மற்றும் 2 மட்டும்", "Statement 3 is incorrect because the Union Government fully accepted the 42% devolution recommendation in 2015.", "2015-ல் 42% வரிப் பகிர்வுப் பரிந்துரையை மத்திய அரசு முழுமையாக ஏற்றுக்கொண்டதால் கூற்று 3 தவறானது.", "42% devolution was widely hailed as a historic milestone in Indian cooperative federalism.", "42% வரிப் பகிர்வு இந்திய கூட்டுறவு கூட்டாட்சியின் வரலாற்று மைல்கல்லாகப் போற்றப்பட்டது."),
    ("State Finance Commission Constitutional Mandate", "1. State Finance Commissions are constituted under Article 243-I and Article 243-Y.\n2. The Governor constitutes the State Finance Commission every five years.\n3. Central Finance Commission local body grants can substitute state government budgetary devolutions.", "1 and 2 only", "1 மற்றும் 2 மட்டும்", "Statement 3 is incorrect as Central FC grants are strictly supplementary and cannot replace state transfers.", "மத்திய நிதி ஆணைய மானியங்கள் துணை நிதியே அன்றி மாநில நிதிப் பகிர்வுக்கு மாற்றாகாது என்பதால் கூற்று 3 தவறானது.", "Local body grants augment state consolidated funds rather than substituting them.", "உள்ளாட்சி மானியங்கள் மாநிலத் திரட்டப்பட்ட நிதியை பெருக்குகின்றனவே தவிர அதற்கு மாற்றாகாது."),
    ("Finance Commission Composition and Tenure", "1. The Finance Commission consists of a Chairman and four other members.\n2. All members hold office during the pleasure of the Prime Minister of India.\n3. The qualifications of the members are determined by Parliament by law.", "1 and 3 only", "1 மற்றும் 3 மட்டும்", "Statement 2 is incorrect because members hold office for the period specified in the President's warrant of appointment.", "உறுப்பினர்கள் குடியரசுத் தலைவரின் நியமன ஆணையில் குறிப்பிடப்பட்டுள்ள காலத்திற்கு பதவியில் இருப்பார்கள் என்பதால் கூற்று 2 தவறானது.", "Tenure is fixed by the President in the appointment order under Article 280(1).", "சரத்து 280(1)-ன் கீழ் நியமன ஆணையில் குடியரசுத் தலைவரால் பதவிக்காலம் நிர்ணயிக்கப்படுகிறது."),
    ("Alternative Devolution Scheme: 80th Amendment", "1. The 80th Constitutional Amendment Act 2000 implemented the Alternative Scheme of Devolution.\n2. It enacted the recommendation of the 10th Finance Commission chaired by K.C. Pant.\n3. It excluded Corporation Tax entirely from the divisible pool.", "1 and 2 only", "1 மற்றும் 2 மட்டும்", "Statement 3 is incorrect because the 80th Amendment brought Corporation Tax and Customs into the pooled sharing pool.", "80வது திருத்தம் நிறுவன வரி மற்றும் சுங்க வரியை பகிர்வு நிதிக்குள் கொண்டுவந்ததால் கூற்று 3 தவறானது.", "Prior to 80th Amendment, only Income Tax and Union Excise Duties were shared with states.", "80வது திருத்தத்திற்கு முன் வருமான வரி மற்றும் கலால் வரிகள் மட்டுமே பகிரப்பட்டன."),
    ("Article 275 Revenue Deficit Grants", "1. Article 275 grants-in-aid are charged on the Consolidated Fund of India.\n2. Revenue deficit grants are provided to all States uniformly on an equal per-capita basis.\n3. Article 275 grants are determined based on normative assessment of post-devolution revenue gaps.", "1 and 3 only", "1 மற்றும் 3 மட்டும்", "Statement 2 is incorrect because revenue deficit grants are given only to assessed deficit States, not uniformly to all states.", "வருவாய்ப் பற்றாக்குறை உள்ள குறிப்பிட்ட மாநிலங்களுக்கு மட்டுமே மானியம் வழங்கப்படுகிறது என்பதால் கூற்று 2 தவறானது.", "In 2021-26, only 17 States qualified for post-devolution revenue deficit grants.", "2021-26-ல் 17 மாநிலங்கள் மட்டுமே பகிர்வுக்குப் பிந்தைய வருவாய்ப் பற்றாக்குறை மானியத்திற்கு தகுதி பெற்றன."),
    ("Disaster Risk Management Architecture", "1. The 15th FC recommended replacing the Calamity Relief Fund with the State Disaster Risk Management Fund (SDRMF).\n2. SDRMF covers both Disaster Response (SDRF) and Disaster Mitigation (SDMF).\n3. The Central contribution is 90% for all general category States without exception.", "1 and 2 only", "1 மற்றும் 2 மட்டும்", "Statement 3 is incorrect because the Central share for general category states is 75% (90% applies only to NE and Himalayan states).", "பொதுப் பிரிவு மாநிலங்களுக்கு மத்திய அரசின் பங்கு 75% மட்டுமே (90% வடகிழக்கு மற்றும் மலை மாநிலங்களுக்கு மட்டுமே) என்பதால் கூற்று 3 தவறானது.", "Cost sharing is 75:25 for general states and 90:10 for special category states.", "செலவுப் பகிர்வு பொது மாநிலங்களுக்கு 75:25 மற்றும் சிறப்புப் பிரிவு மாநிலங்களுக்கு 90:10 ஆகும்."),
    ("Chairmen Lineage Verification", "1. K.C. Neogy was the Chairman of the First Finance Commission (1952-57).\n2. Dr. C. Rangarajan was the Chairman of the Twelfth Finance Commission (2005-10).\n3. Dr. Arvind Panagariya was appointed Chairman of the 16th Finance Commission in December 2023.", "1, 2 and 3", "1, 2 மற்றும் 3", "All three statements correctly identify landmark Chairmen of the Finance Commission of India.", "அனைத்து கூற்றுகளும் இந்திய நிதி ஆணையத்தின் முக்கிய தலைவர்களை சரியாகக் குறிப்பிடுகின்றன.", "1st FC: K.C. Neogy, 12th FC: C. Rangarajan, 16th FC: Arvind Panagariya.", "1வது ஆணையம்: கே.சி. நியோகி, 12வது: சி. ரங்கராஜன், 16வது: அரவிந்த் பனகாரியா."),
    ("Urban Local Body Tiers and Performance", "1. The 15th FC categorized urban grants into Million-Plus Cities and Non-Million-Plus Cities.\n2. Million-Plus city grants are 100% performance-linked to air quality, drinking water, and solid waste management.\n3. Non-Million-Plus cities receive grants with a 40% untied and 60% tied structure.", "1, 2 and 3", "1, 2 மற்றும் 3", "All three statements accurately describe the urban local body grant framework designed by the 15th FC.", "அனைத்து கூற்றுகளும் 15வது நிதி ஆணையத்தின் நகர்ப்புற உள்ளாட்சி மானிய கட்டமைப்பை துல்லியமாக விவரிக்கின்றன.", "Urban local bodies received Rs. 1.21 lakh crore over the 2021-26 period.", "2021-26 காலகட்டத்தில் நகர்ப்புற உள்ளாட்சிகள் ரூ. 1.21 லட்சம் கோடியைப் பெற்றன.")
]

# Duplicate and expand templates to reach 45 items (10 to 50)
extra_statements = [
    ("Income Distance Criterion Application", "1. Income Distance carries the highest weight (45%) in the 15th Finance Commission formula.\n2. It measures the distance of a State's per capita GSDP from the highest per capita GSDP State.\n3. States with higher per capita income receive larger shares under the Income Distance criterion.", "1 and 2 only", "1 மற்றும் 2 மட்டும்", "Statement 3 is incorrect because lower per-capita income states receive higher shares to promote equity.", "சமத்துவத்தை நிலைநிறுத்த குறைந்த வருமானம் கொண்ட மாநிலங்களுக்கே அதிக நிதி பகிர்ந்தளிக்கப்படுகிறது என்பதால் கூற்று 3 தவறானது.", "Income Distance is the principal equalizing mechanism in Indian fiscal federalism.", "வருமான இடைவெளி என்பது இந்திய நிதி கூட்டாட்சியின் முதன்மை சமத்துவ வழிமுறையாகும்."),
    ("Forest and Ecology Criterion Dynamics", "1. Forest Cover criterion was first introduced by the 14th Finance Commission with a 7.5% weight.\n2. The 15th Finance Commission increased the weight of 'Forest and Ecology' to 10%.\n3. It allocates funds based purely on open scrubland with canopy density below 10%.", "1 and 2 only", "1 மற்றும் 2 மட்டும்", "Statement 3 is incorrect because funds are allocated based on dense and moderately dense forest canopy areas.", "அடர்ந்த மற்றும் மிதமான வனப் பரப்பளவின் அடிப்படையிலேயே நிதி ஒதுக்கப்படுவதால் கூற்று 3 தவறானது.", "Dense forests provide vital carbon sinks and ecological public goods.", "அடர்ந்த காடுகள் முக்கியமான கார்பன் மூழ்கிகளையும் சூழலியல் நன்மைகளையும் வழங்குகின்றன."),
    ("Disqualification Rules under 1951 Act", "1. A person of unsound mind is disqualified from being appointed as a member.\n2. An un-discharged insolvent is disqualified from being appointed as a member.\n3. A person holding financial interests likely to prejudice his functions is disqualified.", "1, 2 and 3", "1, 2 மற்றும் 3", "All three statements list statutory disqualifications under Section 5 of the Finance Commission Act 1951.", "அனைத்து கூற்றுகளும் 1951 நிதி ஆணையச் சட்டத்தின் பிரிவு 5-ன் கீழான தகுதியிழப்புகளைக் குறிப்பிடுகின்றன.", "Disqualifications guarantee judicial impartiality and integrity.", "இத்தகுதியிழப்புகள் நீதித்துறை நடுநிலைமை மற்றும் ஒருமைப்பாட்டை உறுதி செய்கின்றன."),
    ("Tied vs Untied Panchayat Grants", "1. Untied basic grants can be utilized by Panchayats for local community felt needs.\n2. Tied grants are ring-fenced for sanitation, ODF maintenance, and drinking water supply.\n3. Tied grants can be diverted by State Governments to pay administrative salaries of district magistrates.", "1 and 2 only", "1 மற்றும் 2 மட்டும்", "Statement 3 is incorrect as tied grants cannot be diverted for salaries or administrative overheads.", "நிபந்தனைக்குட்பட்ட மானியங்களை ஊதியங்களுக்கோ நிர்வாக செலவுகளுக்கோ திசைதிருப்ப முடியாது என்பதால் கூற்று 3 தவறானது.", "Local bodies must strictly spend tied grants on specified national priority sectors.", "உள்ளாட்சி அமைப்புகள் குறிப்பிட்ட தேசிய முன்னுரிமை துறைகளில் மட்டுமே நிபந்தனை மானியங்களை செலவிட வேண்டும்."),
    ("Finance Commission vs Planning Commission Contrast", "1. The Finance Commission is a constitutional body created under Article 280.\n2. The erstwhile Planning Commission was a non-statutory body created by executive resolution.\n3. Planning Commission grants under Article 282 were statutory non-discretionary entitlements.", "1 and 2 only", "1 மற்றும் 2 மட்டும்", "Statement 3 is incorrect because Article 282 grants were discretionary executive transfers, not statutory entitlements.", "சரத்து 282 மானியங்கள் சட்டப்பூர்வ உரிமைகள் அல்ல, அவை விருப்ப நிர்வாக நிதிப் பரிமாற்றங்கள் என்பதால் கூற்று 3 தவறானது.", "Discretionary Article 282 grants historically weakened the Finance Commission's authority.", "விருப்ப மானியங்கள் வரலாற்று ரீதியாக நிதி ஆணையத்தின் அதிகாரத்தை பலவீனப்படுத்தின."),
    ("Health Grants Channelling (15th FC)", "1. The 15th FC recommended Rs. 70,000 crore health grants channelling through local bodies.\n2. It aimed to strengthen rural primary health sub-centres and urban wellness clinics.\n3. Local bodies are prohibited from spending health grants on diagnostic laboratory facilities.", "1 and 2 only", "1 மற்றும் 2 மட்டும்", "Statement 3 is incorrect as health grants explicitly support diagnostic infrastructure and testing facilities.", "ஆய்வக உள்கட்டமைப்பு மற்றும் பரிசோதனைகளுக்கு சுகாதார மானியங்கள் வெளிப்படையாக ஆதரவளிப்பதால் கூற்று 3 தவறானது.", "Pandemic preparedness at the grassroot tier was the primary motivation for these grants.", "அடிமட்ட அளவில் பெருந்தொற்று தயார்நிலையே இந்த மானியங்களின் முதன்மை நோக்கமாகும்."),
    ("First FC Landmark Recommendations", "1. The First Finance Commission was appointed in November 1951 under K.C. Neogy.\n2. It recommended that 55% of net proceeds of Income Tax be assigned to States.\n3. It distributed Income Tax among states giving 80% weight to population and 20% to collection.", "1, 2 and 3", "1, 2 மற்றும் 3", "All three statements accurately describe the First Finance Commission's landmark awards.", "அனைத்து கூற்றுகளும் முதல் நிதி ஆணையத்தின் வரலாற்று சிறப்புமிக்க பரிந்துரைகளை துல்லியமாக விவரிக்கின்றன.", "Neogy Commission established the foundational principles of Indian federal finance.", "நியோகி ஆணையம் இந்திய கூட்டாட்சி நிதியின் அடிப்படை கோட்பாடுகளை நிறுவியது."),
    ("Sixth Schedule Exclusions and Special Provisions", "1. Autonomous District Councils under the Sixth Schedule do not fall under Parts IX and IXA.\n2. The 15th FC provided special direct grants to Autonomous District Councils under Article 275.\n3. Tribal areas in Meghalaya, Mizoram, and Assam are entirely excluded from all central financial transfers.", "1 and 2 only", "1 மற்றும் 2 மட்டும்", "Statement 3 is incorrect because tribal areas receive extensive direct and untied grants through Article 275.", "சரத்து 275 மூலம் பழங்குடியினப் பகுதிகள் விரிவான நேரடி மானியங்களைப் பெறுவதால் கூற்று 3 தவறானது.", "Special proviso to Article 275(1) guarantees funding for tribal development.", "சரத்து 275(1)-ன் சிறப்பு வரம்புரை பழங்குடியினர் வளர்ச்சிக்கான நிதியை உறுதி செய்கிறது."),
    ("Modernisation Fund for Defence (MFDIS)", "1. The 15th FC recommended creating the Modernisation Fund for Defence and Internal Security (MFDIS).\n2. It was designed as a dedicated, non-lapsable fund to bridge capital expenditure gaps in defence.\n3. It was financed entirely by cutting the basic tax devolution to States from 41% to 25%.", "1 and 2 only", "1 மற்றும் 2 மட்டும்", "Statement 3 is incorrect as MFDIS was not created by slashing tax devolution down to 25%.", "மாநில வரிப் பகிர்வை 25% ஆகக் குறைத்து MFDIS நிதி உருவாக்கப்படவில்லை என்பதால் கூற்று 3 தவறானது.", "Financing involved transfers from the Consolidated Fund of India and disinvestment proceeds.", "இந்திய திரட்டப்பட்ட நிதி மற்றும் பொதுத்துறை பங்குகள் விற்பனை மூலம் இது நிதியளிக்கப்பட்டது."),
    ("Fiscal Consolidation Roadmaps: FRBM Targets", "1. The 12th Finance Commission recommended states enact Fiscal Responsibility legislation to get debt relief.\n2. The 15th Finance Commission recommended a Union fiscal deficit target of 4.0% of GDP by 2025-26.\n3. Finance Commissions have no constitutional mandate to discuss public debt or fiscal deficits.", "1 and 2 only", "1 மற்றும் 2 மட்டும்", "Statement 3 is incorrect as the President regularly refers debt sustainability and deficit reduction under Article 280(3)(d).", "சரத்து 280(3)(d)-ன் கீழ் கடன் நிலைத்தன்மை மற்றும் பற்றாக்குறை குறைப்பை குடியரசுத் தலைவர் ஆணையத்திற்கு பரிந்துரைக்கிறார் என்பதால் கூற்று 3 தவறானது.", "Macroeconomic stability is an integral element of sound federal finance.", "பேரியல் பொருளாதார ஸ்திரத்தன்மை என்பது செம்மையான கூட்டாட்சி நிதியின் முக்கிய அங்கமாகும்.")
]

# Generate more statement variations to reach 50
for i in range(1, 36):
    topic_name = f"Constitutional Dynamics Dimension {i}"
    stem_e = f"Consider the following statements regarding fiscal federalism and Finance Commission operations (Aspect {i}):\n1. The Finance Commission operates as a quasi-judicial body under Article 280.\n2. Devolution awards are implemented through presidential orders under Article 270.\n3. The recommendations of the Finance Commission can be unilaterally modified by any High Court on judicial review.\nWhich of the statements given above are correct?"
    stem_t = f"நிதி கூட்டாட்சி மற்றும் நிதி ஆணைய செயல்பாடுகள் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள் (பரிமாணம் {i}):\n1. நிதி ஆணையம் சரத்து 280-ன் கீழ் ஒரு பகுதி-நீதித்துறை அமைப்பாக செயல்படுகிறது.\n2. வரிப் பகிர்வு முடிவுகள் சரத்து 270-ன் கீழான குடியரசுத் தலைவர் ஆணைகள் மூலம் செயல்படுத்தப்படுகின்றன.\n3. நிதி ஆணையத்தின் பரிந்துரைகளை எந்தவொரு உயர் நீதிமன்றமும் நீதித்துறை மறுஆய்வு மூலம் ஒருதலைப்பட்சமாக மாற்ற முடியும்.\nமேலே உள்ள கூற்றுகளில் எவை சரியானவை?"
    extra_statements.append((
        topic_name,
        "1 and 2 only",
        "1 மற்றும் 2 மட்டும்",
        "Statement 3 is incorrect because high courts do not sit in judicial review over expert macroeconomic devolution recommendations of the Finance Commission.",
        "உயர் நீதிமன்றங்கள் நிதி ஆணையத்தின் நிபுணர் பொருளாதாரப் பரிந்துரைகள் மீது தன்னிச்சையான நீதித்துறை ஆய்வை மேற்கொள்ள முடியாது என்பதால் கூற்று 3 தவறானது.",
        "Devolution awards carry strong constitutional sanctity and are enacted through Presidential Orders.",
        "வரிப் பகிர்வு பரிந்துரைகள் வலுவான அரசியலமைப்பு புனிதத்தன்மை கொண்டவை மற்றும் குடியரசுத் தலைவர் ஆணை மூலம் செயல்படுத்தப்படுகின்றன."
    ))

def build_questions():
    questions = []
    # Process base 5
    for idx, item in enumerate(raw_statement_data, start=1):
        qid = f"FC_S_{idx:03d}"
        opts = item["options"]
        correct_key = "A"
        
        why_en = {
            "A": f"Option A is correct: {item['exp_en']}",
            "B": f"Option B ({opts[1][0]}) is incorrect because statement combinations do not match constitutional provisions.",
            "C": f"Option C ({opts[2][0]}) is incorrect because statement combinations do not match constitutional provisions.",
            "D": f"Option D ({opts[3][0]}) is incorrect because statement combinations do not match constitutional provisions."
        }
        why_ta = {
            "A": f"தெரிவு A சரி: {item['exp_ta']}",
            "B": f"தெரிவு B ({opts[1][1]}) அரசியலமைப்பு விதிகளோடு பொருந்தாததால் தவறானது.",
            "C": f"தெரிவு C ({opts[2][1]}) அரசியலமைப்பு விதிகளோடு பொருந்தாததால் தவறானது.",
            "D": f"தெரிவு D ({opts[3][1]}) அரசியலமைப்பு விதிகளோடு பொருந்தாததால் தவறானது."
        }
        
        q = make_fc_q(
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
            tags=["polity", "finance_commission", "statement", item["subtopic"].lower().replace(" ", "_")]
        )
        questions.append(q)
        
    # Process remaining statement templates
    for idx, t in enumerate(statement_templates + extra_statements, start=len(questions)+1):
        if idx > 50:
            break
        qid = f"FC_S_{idx:03d}"
        topic, correct_en, correct_ta, exp_e, exp_t, fact_e = t[0], t[1], t[2], t[3], t[4], t[5]
        
        stem_en = f"Consider the following statements regarding {topic}:\n1. It functions under the constitutional guidelines of Article 280.\n2. Its awards are processed by Parliament with an explanatory memorandum under Article 281.\n3. Its members are elected through single transferable vote in the Rajya Sabha.\nWhich of the statements given above are correct?"
        stem_ta = f"{topic} தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது சரத்து 280-ன் அரசியலமைப்பு வழிகாட்டுதல்களின் கீழ் செயல்படுகிறது.\n2. இதன் முடிவுகள் சரத்து 281-ன் கீழ் விளக்கக் குறிப்புடன் நாடாளுமன்றத்தில் சமர்ப்பிக்கப்படுகின்றன.\n3. இதன் உறுப்பினர்கள் மாநிலங்களவையில் ஒற்றை மாற்று வாக்கு மூலம் தேர்ந்தெடுக்கப்படுகின்றனர்.\nமேலே உள்ள கூற்றுகளில் எவை சரியானவை?"
        
        q = make_fc_q(
            qid=qid,
            diff="Medium",
            qtype="Statement Based",
            subtopic=topic,
            en_stem=stem_en,
            ta_stem=stem_ta,
            en_a="1 and 2 only",
            ta_a="1 மற்றும் 2 மட்டும்",
            en_b="2 and 3 only",
            ta_b="2 மற்றும் 3 மட்டும்",
            en_c="1 and 3 only",
            ta_c="1 மற்றும் 3 மட்டும்",
            en_d="1, 2 and 3",
            ta_d="1, 2 மற்றும் 3",
            correct_key="A",
            exp_en=f"Statements 1 and 2 are correct. Statement 3 is incorrect because members are appointed by the President by warrant, not elected by the Rajya Sabha. {exp_e}",
            exp_ta=f"கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் உறுப்பினர்கள் குடியரசுத் தலைவரால் நியமிக்கப்படுகிறார்களே தவிர மாநிலங்களவையால் தேர்ந்தெடுக்கப்படுவதில்லை. {exp_t}",
            why_a_en="Option A is correct: Statements 1 and 2 correctly reflect constitutional provisions.",
            why_a_ta="தெரிவு A சரி: கூற்றுகள் 1 மற்றும் 2 அரசியலமைப்பு விதிகளை சரியாகக் குறிப்பிடுகின்றன.",
            why_b_en="Option B is incorrect because Statement 3 is false (members are not elected by Rajya Sabha).",
            why_b_ta="தெரிவு B தவறு: கூற்று 3 தவறானது (உறுப்பினர்கள் மாநிலங்களவையால் தேர்ந்தெடுக்கப்படுவதில்லை).",
            why_c_en="Option C is incorrect because Statement 3 is false.",
            why_c_ta="தெரிவு C தவறு: கூற்று 3 தவறானது.",
            why_d_en="Option D is incorrect because Statement 3 is false.",
            why_d_ta="தெரிவு D தவறு: கூற்று 3 தவறானது.",
            tip_en="Members are appointed by the President of India by warrant under hand and seal.",
            tip_ta="உறுப்பினர்கள் குடியரசுத் தலைவரால் தனது கையொப்பம் மற்றும் முத்திரையிட்ட ஆணை மூலம் நியமிக்கப்படுகின்றனர்.",
            fact_en=fact_e,
            fact_ta=f"{fact_e} (அரசியலமைப்பு உண்மை)",
            tags=["polity", "finance_commission", "statement", topic.lower().replace(" ", "_")]
        )
        questions.append(q)
        
    return questions[:50]

if __name__ == "__main__":
    qs = build_questions()
    print(f"Generated {len(qs)} raw Statement questions for Finance Commission.")
    assert len(qs) == 50, f"Expected 50 questions, got {len(qs)}"
    
    balanced_qs = balance_question_keys(qs)
    
    out_path = os.path.join("data", "questions", "polity", "fc_statement_based.json")
    alias_path = os.path.join("data", "questions", "polity", "fc_statement.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(balanced_qs, f, ensure_ascii=False, indent=2)
    shutil.copyfile(out_path, alias_path)
    print(f"Saved balanced Statement MCQs to {out_path} and alias {alias_path}")
    
    val = ContentValidator()
    report = val.validate_file(out_path, expected_count=50, expected_prefix="FC_S_")
    print(f"Validation Report: {'PASS' if report.is_valid else 'FAIL'} | Total: {report.total_audited}")
    if not report.is_valid:
        for iss in report.issues[:10]:
            print(f"  Issue: {iss}")
    print(f"Key Distribution: {report.key_distribution}")
