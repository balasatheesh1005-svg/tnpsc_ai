# -*- coding: utf-8 -*-
"""
Generator for Comptroller & Auditor General of India (CAG) Medium MCQs (50 Questions: CAG_M_001 to CAG_M_050).
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

raw_medium_data = [
    # 1
    {
        "subtopic": "CAG and Public Accounts Committee",
        "stem_en": "How does the Comptroller and Auditor General of India actively assist the Public Accounts Committee (PAC) during its examination of audit reports?",
        "stem_ta": "தணிக்கை அறிக்கைகளை ஆராயும் போது நாடாளுமன்றப் பொதுக் கணக்குக் குழுவிற்கு (PAC) இந்தியத் தலைமைக் கணக்குத் தணிக்கையாளர் எவ்வாறு தீவிரமாக உதவுகிறார்?",
        "options": [
            ("Attends PAC meetings, explains complex accounting nuances, and assists in questioning departmental witnesses", "PAC கூட்டங்களில் கலந்துகொண்டு, சிக்கலான கணக்கு நுணுக்கங்களை விளக்கி, துறைசார் சாட்சிகளை விசாரிப்பதில் உதவுகிறார்"),
            ("Directly casts a deciding vote when PAC members are equally divided", "PAC உறுப்பினர்களிடையே சமநிலை ஏற்படும் போது நேரடியாகத் தீர்க்கும் வாக்கைச் செலுத்துகிறார்"),
            ("Replaces the Chairman of the PAC whenever a financial crisis occurs", "நிதி நெருக்கடி ஏற்படும் போதெல்லாம் PAC தலைவரின் இடத்தைப் பிடிக்கிறார்"),
            ("Directs police to arrest any witness refusing to answer PAC queries", "PAC கேள்விகளுக்குப் பதிலளிக்க மறுக்கும் சாட்சிகளைக் கைது செய்ய காவல்துறைக்கு உத்தரவிடுகிறார்")
        ],
        "exp_en": "The CAG attends all meetings of the PAC, prepares a list of important points for examination, and assists the Committee in cross-examining witnesses from executive ministries.",
        "exp_ta": "பொதுக் கணக்குக் குழுவின் அனைத்து கூட்டங்களிலும் CAG பங்கேற்று, முக்கிய ஆய்வுப் புள்ளிகளைத் தயாரித்து, அமைச்சக சாட்சிகளை குறுக்கு விசாரணை செய்வதில் குழுவுக்கு உதவுகிறார்.",
        "tip_en": "CAG assists PAC as friend, philosopher, and guide; he participates in discussions but CANNOT vote.",
        "tip_ta": "சி.ஏ.ஜி பொதுக் கணக்குக் குழுவின் நண்பனாக, தத்துவவாதியாக உதவுகிறார்; விவாதங்களில் பங்கேற்பார், ஆனால் வாக்களிக்க முடியாது.",
        "fact_en": "The PAC is described as the legislative counterpart of the CAG in financial scrutiny.",
        "fact_ta": "நிதி ஆய்வில் பொதுக் கணக்குக் குழு என்பது சி.ஏ.ஜி-யின் சட்டமன்ற இணையாக வர்ணிக்கப்படுகிறது."
    },
    # 2
    {
        "subtopic": "Audit of Public-Private Partnerships",
        "stem_en": "In what manner does the Comptroller and Auditor General audit Public-Private Partnership (PPP) projects involving government concessions?",
        "stem_ta": "அரசு சலுகைகள் சம்பந்தப்பட்ட அரசு-தனியார் கூட்டாண்மை (PPP) திட்டங்களை தலைமைக் கணக்குத் தணிக்கையாளர் எவ்வாறு தணிக்கை செய்கிறார்?",
        "options": [
            ("Audits the government's share of revenues, royalty payments, and compliance with the concession agreement", "அரசுக்கான வருவாய்ப் பங்கு, ராயல்டி செலுத்துதல்கள் மற்றும் ஒப்பந்த நிபந்தனைகளை முறையாகப் பின்பற்றுவதை தணிக்கை செய்கிறார்"),
            ("Directly takes over the private company's factory operations", "தனியார் நிறுவனத்தின் தொழிற்சாலை செயல்பாடுகளை நேரடியாகக் கையகப்படுத்துகிறார்"),
            ("Sets the daily retail pricing of all consumer goods produced under the project", "திட்டத்தின் கீழ் உற்பத்தி செய்யப்படும் அனைத்து நுகர்வோர் பொருட்களின் தினசரி சில்லறை விலையை நிர்ணயிக்கிறார்"),
            ("Is barred by the Constitution from examining any PPP project", "எந்தவொரு PPP திட்டத்தையும் ஆய்வு செய்ய அரசியலமைப்பால் தடை செய்யப்பட்டுள்ளார்")
        ],
        "exp_en": "The CAG audits PPP projects to ensure that public resources, revenue shares, user fees, and concession terms are faithfully enforced in the government's financial interest.",
        "exp_ta": "அரசு-தனியார் கூட்டாண்மைத் திட்டங்களில் பொது வளங்கள், வருவாய்ப் பங்குகள் மற்றும் ஒப்பந்த விதிகள் அரசின் நிதி நலன்களுக்கு ஏற்ப சரியாக செயல்படுத்தப்படுகிறதா என்பதை CAG தணிக்கை செய்கிறார்.",
        "tip_en": "CAG does not audit the internal commercial management of the private partner, but audits revenue-sharing and public risk.",
        "tip_ta": "தனியார் கூட்டாளியின் உள் வணிக நிர்வாகத்தை CAG தணிக்கை செய்வதில்லை; வருவாய் பகிர்வு மற்றும் அரசு நலனை மட்டுமே தணிக்கை செய்கிறார்.",
        "fact_en": "Major PPP audits have included Delhi/Mumbai airport privatizations and highway toll concessions.",
        "fact_ta": "தில்லி/மும்பை விமான நிலைய தனியார்மயம் மற்றும் நெடுஞ்சாலை சுங்கச் சாவடி ஒப்பந்தங்கள் முக்கிய PPP தணிக்கைகளில் அடங்கும்."
    },
    # 3
    {
        "subtopic": "Telecom Revenue Share Audit",
        "stem_en": "In Association of Unified Telecom Service Providers of India (2014), what did the Supreme Court rule regarding the CAG's power to audit private telecom companies?",
        "stem_ta": "ஒருங்கிணைந்த தொலைத்தொடர்பு சேவை வழங்குநர்கள் சங்கம் (2014) வழக்கில், தனியார் தொலைத்தொடர்பு நிறுவனங்களை தணிக்கை செய்யும் சி.ஏ.ஜி-யின் அதிகாரம் குறித்து உச்ச நீதிமன்றம் என்ன தீர்ப்பளித்தது?",
        "options": [
            ("CAG has the authority to audit the revenue records of private telecom operators to verify government revenue share", "அரசுக்கான வருவாய்ப் பங்கைச் சரிபார்க்க தனியார் தொலைத்தொடர்பு நிறுவனங்களின் வருவாய் ஆவணங்களைத் தணிக்கை செய்ய CAG-க்கு அதிகாரம் உண்டு"),
            ("CAG has no jurisdiction over private telecom operators under any circumstances", "எந்த சூழ்நிலையிலும் தனியார் தொலைத்தொடர்பு நிறுவனங்கள் மீது CAG-க்கு அதிகார வரம்பு இல்லை"),
            ("CAG can determine mobile phone call rates directly", "மொபைல் போன் அழைப்பு கட்டணங்களை CAG நேரடியாகத் தீர்மானிக்க முடியும்"),
            ("Private companies are exempt from all constitutional oversight permanently", "தனியார் நிறுவனங்களுக்கு அனைத்து அரசியலமைப்பு மேற்பார்வையிலிருந்தும் நிரந்தர விலக்கு உண்டு")
        ],
        "exp_en": "The Supreme Court held that since natural resources like spectrum belong to the people, the CAG under Section 16 of the 1971 Act is entitled to examine the accounts of private telecom licensees to verify gross revenue and license fee shares.",
        "exp_ta": "அலைக்கற்றை போன்ற இயற்கை வளங்கள் மக்களுக்குச் சொந்தமானது என்பதால், அரசின் வருவாய்ப் பங்கைச் சரிபார்க்க தனியார் நிறுவனங்களின் கணக்குகளை ஆய்வு செய்ய 1971 சட்டத்தின் பிரிவு 16-ன் கீழ் CAG-க்கு உரிமை உண்டு என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
        "tip_en": "2014 Supreme Court ruling affirmed CAG's jurisdiction to audit private firms where revenue-sharing of sovereign natural resources is involved.",
        "tip_ta": "இறையாண்மை இயற்கை வளங்களின் வருவாய் பகிர்வு உள்ள தனியார் நிறுவனங்களைத் தணிக்கை செய்ய CAG-க்கு உள்ள அதிகாரத்தை 2014 உச்ச நீதிமன்றத் தீர்ப்பு உறுதிப்படுத்தியது.",
        "fact_en": "This verdict expanded constitutional accountability into revenue-sharing contracts.",
        "fact_ta": "இந்தத் தீர்ப்பு அரசியலமைப்பு பொறுப்புடைமையை வருவாய் பகிர்வு ஒப்பந்தங்களுக்கும் விரிவுபடுத்தியது."
    },
    # 4
    {
        "subtopic": "Section 20 of CAG Act",
        "stem_en": "Under Section 20 of the CAG's (DPC) Act, 1971, how can the audit of an authority not ordinarily covered under the Act be entrusted to the CAG?",
        "stem_ta": "1971-ம் ஆண்டின் CAG சட்டத்தின் பிரிவு 20-ன் கீழ், பொதுவாக சட்டத்தில் வராத ஓர் அமைப்பின் தணிக்கையை சி.ஏ.ஜி-யிடம் எவ்வாறு ஒப்படைக்க முடியும்?",
        "options": [
            ("By the President or Governor in public interest, after consultation with the CAG and giving reasonable opportunity to the body", "பொது நலன் கருதி, CAG-ஐக் கலந்தாலோசித்து, அந்த அமைப்பிற்கு நியாயமான வாய்ப்பளித்த பின்னர் குடியரசுத் தலைவர் அல்லது ஆளுநரால் ஒப்படைக்கப்படலாம்"),
            ("By the Supreme Court issuing an ex-parte judicial warrant", "உச்ச நீதிமன்றம் ஒருதலைப்பட்சமாக நீதித்துறை ஆணை பிறப்பிப்பதன் மூலம்"),
            ("By the local municipal councillor passing an oral resolution", "உள்ளூர் நகர்மன்ற உறுப்பினர் வாய்மொழித் தீர்மானம் நிறைவேற்றுவதன் மூலம்"),
            ("By the private external auditor surrendering his license", "தனியார் வெளித் தணிக்கையாளர் தனது உரிமத்தை ஒப்படைப்பதன் மூலம்")
        ],
        "exp_en": "Section 20 allows the President or Governor to request the CAG to undertake the audit of accounts of any authority or body in the public interest, provided the CAG is consulted and the body is given reasonable opportunity to represent.",
        "exp_ta": "பிரிவு 20 பொது நலன் கருதி, சி.ஏ.ஜி-யுடன் கலந்தாலோசித்து, சம்பந்தப்பட்ட அமைப்புக்கு உரிய வாய்ப்பளித்த பிறகு, எந்தவொரு அமைப்பின் தணிக்கையையும் சி.ஏ.ஜி-யிடம் ஒப்படைக்க குடியரசுத் தலைவர் அல்லது ஆளுநருக்கு அதிகாரம் அளிக்கிறது.",
        "tip_en": "Section 20 = Consent audit of other authorities on request of President/Governor.",
        "tip_ta": "பிரிவு 20 = குடியரசுத் தலைவர்/ஆளுநரின் கோரிக்கையின் பேரில் பிற அமைப்புகளின் ஒப்புதல் தணிக்கை.",
        "fact_en": "This provision is often used to audit major trusts, sports bodies, or cooperative societies involving public funds.",
        "fact_ta": "பொது நிதி சம்பந்தப்பட்ட முக்கிய அறக்கட்டளைகள் அல்லது கூட்டுறவு அமைப்புகளைத் தணிக்கை செய்ய இந்த விதி பெரும்பாலும் பயன்படுத்தப்படுகிறது."
    },
    # 5
    {
        "subtopic": "Limitations on CAG Audit Scope",
        "stem_en": "What is the recognized constitutional limitation on the Comptroller and Auditor General regarding government policies formulated by the executive and Parliament?",
        "stem_ta": "நிர்வாகம் மற்றும் நாடாளுமன்றத்தால் வகுக்கப்படும் அரசாங்கக் கொள்கைகள் குறித்து தலைமைக் கணக்குத் தணிக்கையாளருக்கு உள்ள அரசியலமைப்பு வரம்பு என்ன?",
        "options": [
            ("CAG can examine whether policy execution is wasteful or inefficient, but cannot question the policy itself", "கொள்கை செயல்படுத்தல் வீணானதா அல்லது திறமையற்றதா என்பதை CAG ஆராயலாமே தவிர, கொள்கையையே கேள்வி கேட்க முடியாது"),
            ("CAG has the absolute constitutional authority to repeal any economic policy bill", "எந்தவொரு பொருளாதாரக் கொள்கை மசோதாவையும் ரத்து செய்ய CAG-க்கு முழுமையான அரசியலமைப்பு அதிகாரம் உண்டு"),
            ("CAG must ratify all political party election manifestos before elections", "தேர்தலுக்கு முன் அனைத்து அரசியல் கட்சிகளின் தேர்தல் அறிக்கைகளையும் CAG அங்கீகரிக்க வேண்டும்"),
            ("CAG can dismiss cabinet ministers whose policies result in fiscal deficits", "கொள்கைகள் நிதிப் பற்றாக்குறையை ஏற்படுத்தும் அமைச்சர்களை CAG பதவிநீக்கம் செய்யலாம்")
        ],
        "exp_en": "The CAG has no constitutional competence to question the wisdom of policies sanctioned by Parliament; his audit is confined to evaluating the execution, legality, economy, and financial outcome of those policies.",
        "exp_ta": "நாடாளுமன்றத்தால் அங்கீகரிக்கப்பட்ட கொள்கைகளின் விவேகத்தை கேள்வி கேட்க சி.ஏ.ஜி-க்கு அதிகாரம் இல்லை; அக்கொள்கைகளை செயல்படுத்துவதில் உள்ள சட்ட ஒழுங்கு, சிக்கனம் மற்றும் நிதி விளைவுகளை மட்டுமே அவரால் ஆராய முடியும்.",
        "tip_en": "CAG audits the EXECUTION and EFFICIENCY of policy, NOT the political policy decision itself.",
        "tip_ta": "சி.ஏ.ஜி கொள்கை முடிவை அல்ல, கொள்கையைச் செயல்படுத்துவதில் உள்ள திறமையையும் சிக்கனத்தையுமே தணிக்கை செய்கிறார்.",
        "fact_en": "Paul H. Appleby in his administrative reports cautioned that the CAG should not exceed his mandate by interfering in policy formulation.",
        "fact_ta": "பால் எச். ஆப்பிள்ஸ்பை தனது நிர்வாக அறிக்கைகளில் சி.ஏ.ஜி கொள்கை வகுப்பில் தலையிடக்கூடாது என்று எச்சரித்தார்."
    },
    # 6
    {
        "subtopic": "Controller General of Accounts (CGA)",
        "stem_en": "Following the 1976 reform separating accounting from audit, which authority prepares the Monthly and Annual Accounts of the Union Government?",
        "stem_ta": "கணக்குகளைத் தணிக்கையிலிருந்து பிரித்த 1976 சீர்திருத்தத்திற்குப் பிறகு, மத்திய அரசின் மாதாந்திர மற்றும் வருடாந்திரக் கணக்குகளைத் தயாரிக்கும் அதிகாரம் எது?",
        "options": [
            ("Controller General of Accounts (CGA)", "கணக்குத் துறை கட்டுப்பாட்டு அதிகாரி (CGA)"),
            ("Comptroller and Auditor General of India (CAG)", "இந்தியத் தலைமைக் கணக்குத் தணிக்கையாளர் (CAG)"),
            ("Governor of the Reserve Bank of India", "இந்திய ரிசர்வ் வங்கியின் ஆளுநர்"),
            ("Chairman of the Finance Commission", "நிதி ஆணையத்தின் தலைவர்")
        ],
        "exp_en": "The Controller General of Accounts (CGA) in the Department of Expenditure, Ministry of Finance, is the principal accounting adviser to the Government of India and prepares the monthly and annual accounts of the Union.",
        "exp_ta": "நிதி அமைச்சகத்தின் செலவினத் துறையில் உள்ள கணக்குத் துறை கட்டுப்பாட்டு அதிகாரி (CGA), மத்திய அரசின் முதன்மை கணக்கியல் ஆலோசகராக செயல்பட்டு மத்திய அரசின் மாதாந்திர மற்றும் வருடாந்திரக் கணக்குகளைத் தயாரிக்கிறார்.",
        "tip_en": "CGA compiles Accounts for Union; CAG Audits the Accounts prepared by the CGA.",
        "tip_ta": "CGA மத்திய அரசுக் கணக்குகளைத் தயாரிக்கிறார்; CGA தயாரித்த கணக்குகளை CAG தணிக்கை செய்கிறார்.",
        "fact_en": "The CGA heads the Indian Civil Accounts Service (ICAS).",
        "fact_ta": "CGA இந்திய சிவில் கணக்குப் பணிக்கு (ICAS) தலைமை தாங்குகிறார்."
    },
    # 7
    {
        "subtopic": "State Accounts Compilation",
        "stem_en": "Why does the Comptroller and Auditor General continue to compile the accounts of most State Governments, unlike the Union Government?",
        "stem_ta": "மத்திய அரசைப் போலன்றி, பெரும்பாலான மாநில அரசுகளின் கணக்குகளை சி.ஏ.ஜி தொடர்ந்து தொகுத்து பராமரிப்பது ஏன்?",
        "options": [
            ("Most States have not separated accounting from audit due to high financial costs and administrative unwillingness", "அதிக நிதிச் செலவு மற்றும் நிர்வாகத் தயக்கம் காரணமாக பெரும்பாலான மாநிலங்கள் கணக்கைத் தணிக்கையிலிருந்து பிரிக்கவில்லை"),
            ("The Constitution strictly prohibits any State from maintaining its own treasury", "எந்தவொரு மாநிலமும் தனது சொந்த கருவூலத்தைப் பராமரிக்க அரசியலமைப்பு கண்டிப்பாகத் தடை செய்துள்ளது"),
            ("State Assemblies passed constitutional amendments abolishing State Finance Departments", "மாநில நிதித் துறைகளை ஒழித்து மாநில சட்டமன்றங்கள் அரசியலமைப்புத் திருத்தங்களை நிறைவேற்றின"),
            ("State Chief Ministers are legally barred from signing financial cheques", "மாநில முதலமைச்சர்கள் நிதிக் காசோலைகளில் கையொப்பமிட சட்டப்பூர்வமாகத் தடை செய்யப்பட்டுள்ளனர்")
        ],
        "exp_en": "In 1976, accounting was separated from audit only at the Union level. Most States could not afford separate accounting departments and requested the CAG to continue compiling state accounts.",
        "exp_ta": "1976-ல் மத்திய அளவில் மட்டுமே கணக்குகள் தணிக்கையிலிருந்து பிரிக்கப்பட்டன. பெரும்பாலான மாநிலங்களால் தனி கணக்குத் துறைகளை அமைக்க நிதி வசதி இல்லாததால், சி.ஏ.ஜி-யையே மாநில கணக்குகளைத் தொடரக் கேட்டுக்கொண்டன.",
        "tip_en": "Union: Accounts separated from Audit (1976). States: CAG still maintains both Accounts and Audit in most States.",
        "tip_ta": "மத்திய அரசு: கணக்கு தணிக்கையிலிருந்து பிரிக்கப்பட்டது (1976). மாநிலங்கள்: பெரும்பாலான மாநிலங்களில் CAG கணக்கு மற்றும் தணிக்கை இரண்டையுமே செய்கிறார்.",
        "fact_en": "Only a few states (like Goa) have departmentalised their accounts completely.",
        "fact_ta": "கோவா போன்ற மிகச்சில மாநிலங்கள் மட்டுமே தங்கள் கணக்குகளை முழுமையாகத் துறைமயமாக்கியுள்ளன."
    },
    # 8
    {
        "subtopic": "Disallowance and Surcharge",
        "stem_en": "Does the Comptroller and Auditor General of India possess the power to 'surcharge' or disallow an expenditure and recover money directly from officials?",
        "stem_ta": "இந்தியத் தலைமைக் கணக்குத் தணிக்கையாளருக்கு செலவினத்தை நிராகரித்து அதிகாரிகளிடமிருந்து பணத்தை நேரடியாக வசூலிக்கும் (Surcharge / Disallowance) அதிகாரம் உண்டா?",
        "options": [
            ("No, the CAG is an audit and reporting authority without executive power to disallow or surcharge", "இல்லை, CAG தணிக்கை செய்து அறிக்கை அளிக்கும் அதிகாரம் மட்டுமே கொண்டவர்; செலவை நிராகரிக்கவோ பணத்தை வசூலிக்கவோ நிர்வாக அதிகாரம் இல்லை"),
            ("Yes, the CAG can attach personal bank accounts of defaulting bureaucrats directly", "ஆம், விதிமீறும் அதிகாரிகளின் தனிப்பட்ட வங்கிக் கணக்குகளை நேரடியாக முடக்கலாம்"),
            ("Yes, but only for expenditures below one thousand rupees", "ஆம், ஆனால் ஆயிரம் ரூபாய்க்குக் குறைவான செலவினங்களுக்கு மட்டுமே"),
            ("Yes, with the prior oral permission of the Speaker of Lok Sabha", "ஆம், மக்களவை சபாநாயகரின் வாய்மொழி அனுமதியுடன் செய்யலாம்")
        ],
        "exp_en": "The CAG is only an auditing and reporting body. He does not have quasi-judicial powers of surcharge or disallowance (unlike local fund audit in some States); enforcement is left to the executive and legislature.",
        "exp_ta": "சி.ஏ.ஜி தணிக்கை செய்து அறிக்கை அளிக்கும் அமைப்பே தவிர, செலவை நிராகரிக்கும் அல்லது தண்டித்து வசூலிக்கும் (surcharge) அதிகாரம் அவருக்குக் கிடையாது; அமலாக்கம் நிர்வாகத்திடமே விடப்பட்டுள்ளது.",
        "tip_en": "CAG has no power of surcharge or disallowance; his duty ends with submitting the audit report to the legislature.",
        "tip_ta": "சி.ஏ.ஜி-க்கு அபராதம் விதிக்கும் (surcharge) அதிகாரம் இல்லை; சட்டமன்றத்திற்கு தணிக்கை அறிக்கை சமர்ப்பிப்பதோடு அவரது கடமை முடிவடைகிறது.",
        "fact_en": "Action on CAG audit observations is pursued by the Public Accounts Committee and action-taken reports.",
        "fact_ta": "CAG-யின் தணிக்கைக் கருத்துக்கள் மீது பொதுக் கணக்குக் குழு மற்றும் எடுக்கப்பட்ட நடவடிக்கை அறிக்கைகள் மூலம் நடவடிக்கை எடுக்கப்படுகிறது."
    },
    # 9
    {
        "subtopic": "Audit of Non-Tax Revenues",
        "stem_en": "Which of the following non-tax revenues is audited by the Comptroller and Auditor General of India?",
        "stem_ta": "பின்வரும் வரியல்லா வருவாய்களில் (Non-tax revenues) எது இந்தியத் தலைமைக் கணக்குத் தணிக்கையாளரால் தணிக்கை செய்யப்படுகிறது?",
        "options": [
            ("Dividends and profits from public sector enterprises, user charges, and interest receipts on loans", "பொதுத்துறை நிறுவனங்களின் ஈவுத்தொகை மற்றும் லாபம், பயனர் கட்டணங்கள் மற்றும் கடன்கள் மீதான வட்டி வரவுகள்"),
            ("Private charitable donations to temple hundials", "கோயில் உண்டியல்களுக்கு வழங்கப்படும் தனியார் அறக்கட்டளை நன்கொடைகள்"),
            ("Tuition fees collected by unrecognised private coaching centres", "அங்கீகரிக்கப்படாத தனியார் பயிற்சி மையங்கள் வசூலிக்கும் கல்விக் கட்டணம்"),
            ("Admission tickets sold by private cinema multiplexes", "தனியார் சினிமா திரையரங்குகள் விற்கும் நுழைவுச் சீட்டுகள்")
        ],
        "exp_en": "Under Section 16 of the 1971 Act, the CAG audits all non-tax revenues credited to the Consolidated Fund, including dividends from public enterprises, mining royalties, user fees, and interest receipts.",
        "exp_ta": "1971 சட்டத்தின் பிரிவு 16-ன் கீழ், பொதுத்துறை நிறுவனங்களின் ஈவுத்தொகை, சுரங்க ராயல்டி, பயனர் கட்டணங்கள் மற்றும் வட்டி வரவுகள் உட்பட திரட்டப்பட்ட நிதியில் சேரும் அனைத்து வரியல்லா வருவாய்களையும் CAG தணிக்கை செய்கிறார்.",
        "tip_en": "Section 16 covers both TAX revenues and NON-TAX revenues credited into the Consolidated Fund.",
        "tip_ta": "பிரிவு 16 திரட்டப்பட்ட நிதியில் செலுத்தப்படும் வரி வருவாய் மற்றும் வரியல்லா வருவாய் இரண்டையுமே உள்ளடக்கியது.",
        "fact_en": "Non-tax revenue audits frequently examine concession agreements and royalty under-recoveries.",
        "fact_ta": "வரியல்லா வருவாய்த் தணிக்கை பெரும்பாலும் சுரங்க ராயல்டி மற்றும் சலுகை ஒப்பந்தங்களை ஆய்வு செய்கிறது."
    },
    # 10
    {
        "subtopic": "Constituent Assembly Drafting History",
        "stem_en": "In Draft Article 124 of the Draft Constitution, what was the initial designation proposed before the Drafting Committee finalized 'Comptroller and Auditor-General'?",
        "stem_ta": "வரைவு அரசியலமைப்பின் வரைவு சரத்து 124-ல், 'தலைமைக் கணக்குத் தணிக்கையாளர்' என்று வரைவுக் குழு இறுதி செய்வதற்கு முன் முன்மொழியப்பட்ட ஆரம்பப் பெயர் என்ன?",
        "options": [
            ("Auditor-General", "தணிக்கை ஜெனரல் (Auditor-General)"),
            ("Chancellor of the Exchequer", "கருவூலத் தலைவர்"),
            ("Governor of Public Finance", "பொது நிதி ஆளுநர்"),
            ("Accountant General of Bharat", "பாரதக் கணக்காயர்")
        ],
        "exp_en": "The Draft Constitution initially used the term 'Auditor-General'. The Drafting Committee under Dr. Ambedkar added the word 'Comptroller' to emulate the British nomenclature, though actual comptroller powers were not provided.",
        "exp_ta": "வரைவு அரசியலமைப்பு ஆரம்பத்தில் 'Auditor-General' என்ற சொல்லையே பயன்படுத்தியது. பின்னர் பிரிட்டிஷ் முறையைப் பிரதிபலிக்க டாக்டர் அம்பேத்கர் தலைமையிலான வரைவுக் குழு 'Comptroller' என்ற சொல்லைச் சேர்த்தது.",
        "tip_en": "Draft Constitution had 'Auditor-General'; 'Comptroller' was added later by Dr. Ambedkar's committee.",
        "tip_ta": "வரைவு அரசியலமைப்பில் 'Auditor-General' என்றே இருந்தது; பின்னரே 'Comptroller' என்ற சொல் சேர்க்கப்பட்டது.",
        "fact_en": "K.M. Munshi and T.T. Krishnamachari supported the change in the Constituent Assembly.",
        "fact_ta": "கே.எம். முன்ஷி மற்றும் டி.டி. கிருஷ்ணமாச்சாரி ஆகியோர் அரசியல் நிர்ணய சபையில் இந்த மாற்றத்தை ஆதரித்தனர்."
    },
    # 11
    {
        "subtopic": "Social Audit Interface",
        "stem_en": "What is the relationship between the Comptroller and Auditor General's formal audits and the 'Social Audits' mandated under schemes like MGNREGA?",
        "stem_ta": "சி.ஏ.ஜி-யின் முறையான தணிக்கைகளுக்கும் மகாத்மா காந்தி ஊரக வேலைவாய்ப்புத் திட்டம் (MGNREGA) போன்ற திட்டங்களின் கீழான 'சமூகத் தணிக்கைகளுக்கும்' (Social Audits) இடையிலான உறவு என்ன?",
        "options": [
            ("CAG formulated the Social Audit Standards (SAS) to institutionalize grassroots community audits", "அடிமட்ட சமூகத் தணிக்கைகளை முறைப்படுத்துவதற்காக சமூகத் தணிக்கைத் தரங்களை (SAS) CAG உருவாக்கியுள்ளார்"),
            ("CAG has banned all social audits by village citizens as unconstitutional", "கிராம மக்களால் நடத்தப்படும் அனைத்து சமூகத் தணிக்கைகளையும் அரசியலமைப்பிற்கு முரணானது என CAG தடை செய்துள்ளார்"),
            ("CAG personally conducts every village panchayat social audit meeting in person", "ஒவ்வொரு கிராம ஊராட்சியின் சமூகத் தணிக்கைக் கூட்டத்தையும் சி.ஏ.ஜி நேரில் நடத்துகிறார்"),
            ("Social audits have completely replaced the CAG's constitutional office", "சமூகத் தணிக்கைகள் சி.ஏ.ஜி-யின் அரசியலமைப்பு அலுவலகத்தை முழுமையாக மாற்றியமைத்துவிட்டன")
        ],
        "exp_en": "The CAG partnered with the Ministry of Rural Development to formulate the first-ever 'Social Audit Standards' (SAS) in the world to ensure rigorous, evidence-based social auditing of welfare schemes.",
        "exp_ta": "கிராமப்புற நலத்திட்டங்களின் சமூகத் தணிக்கையை ஆதாரபூர்வமாக உறுதி செய்வதற்காக, உலகிலேயே முதன்முறையாக 'சமூகத் தணிக்கைத் தரங்களை' (SAS) ஊரக வளர்ச்சி அமைச்சகத்துடன் இணைந்து CAG உருவாக்கியுள்ளார்.",
        "tip_en": "CAG formulated Social Audit Standards (SAS) to guide grassroots public scrutiny.",
        "tip_ta": "அடிமட்ட பொது ஆய்வை வழிநடத்த சமூகத் தணிக்கைத் தரங்களை (SAS) CAG வகுத்துள்ளார்.",
        "fact_en": "Social Audit is mandated under Section 17 of the MGNREGA Act, 2005.",
        "fact_ta": "மகாத்மா காந்தி ஊரக வேலைவாய்ப்புச் சட்டம் 2005 பிரிவு 17-ன் கீழ் சமூகத் தணிக்கை கட்டாயமாக்கப்பட்டுள்ளது."
    },
    # 12
    {
        "subtopic": "Environmental Audit",
        "stem_en": "Which specialized wing within the office of the CAG conducts audits on biodiversity conservation, pollution control, and climate change initiatives?",
        "stem_ta": "பல்லுயிர் பாதுகாப்பு, மாசுக் கட்டுப்பாடு மற்றும் பருவநிலை மாற்ற முன்முயற்சிகள் மீதான தணிக்கைகளை நடத்தும் சி.ஏ.ஜி அலுவலகத்தின் சிறப்புப் பிரிவு எது?",
        "options": [
            ("International Centre for Environment Audit and Sustainable Development (iCED)", "சுற்றுச்சூழல் தணிக்கை மற்றும் நிலையான வளர்ச்சிக்கான சர்வதேச மையம் (iCED)"),
            ("National Green Tribunal Audit Bench", "தேசிய பசுமைத் தீர்ப்பாய தணிக்கை அமர்வு"),
            ("Pollution Control Board Accounting Wing", "மாசுக் கட்டுப்பாட்டு வாரிய கணக்குப் பிரிவு"),
            ("Ministry of Environment Vigilance Cell", "சுற்றுச்சூழல் அமைச்சக ஊழல் தடுப்புப் பிரிவு")
        ],
        "exp_en": "The CAG established the International Centre for Environment Audit and Sustainable Development (iCED) at Jaipur, Rajasthan, as a global centre of excellence for environmental audit.",
        "exp_ta": "ராஜஸ்தான் மாநிலம் ஜெய்ப்பூரில் சுற்றுச்சூழல் தணிக்கை மற்றும் நிலையான வளர்ச்சிக்கான சர்வதேச மையத்தை (iCED) உலகளாவிய சிறந்த மையமாக CAG நிறுவியுள்ளார்.",
        "tip_en": "iCED is located at Jaipur, Rajasthan, specializing in environmental audits and sustainable development.",
        "tip_ta": "iCED ராஜஸ்தான் மாநிலம் ஜெய்ப்பூரில் அமைந்துள்ளது; சுற்றுச்சூழல் தணிக்கைகளில் நிபுணத்துவம் பெற்றது.",
        "fact_en": "iCED also trains international auditors from supreme audit institutions across the globe.",
        "fact_ta": "உலகெங்கிலும் உள்ள உச்ச தணிக்கை நிறுவனங்களைச் சேர்ந்த சர்வதேசத் தணிக்கையாளர்களுக்கும் iCED பயிற்சி அளிக்கிறது."
    },
    # 13
    {
        "subtopic": "Audit of Disinvestment",
        "stem_en": "When the Government of India disinvests its shares in a Central Public Sector Enterprise (CPSE), what does the CAG's audit examine?",
        "stem_ta": "மத்திய பொதுத்துறை நிறுவனத்தில் (CPSE) தனது பங்குகளை மத்திய அரசு திரும்பப் பெறும் போது (Disinvestment), சி.ஏ.ஜி தணிக்கை எதனை ஆராய்கிறது?",
        "options": [
            ("Whether valuation methodology was transparent, competitive bidding followed, and maximum realization secured", "மதிப்பீட்டு முறை வெளிப்படையானதா, போட்டி ஏலம் பின்பற்றப்பட்டதா மற்றும் அதிகபட்ச நிதி ஈட்டப்பட்டதா என்பதை ஆராய்கிறது"),
            ("Decides the political timing of the disinvestment announcement", "பங்கு விலக்கல் அறிவிப்பின் அரசியல் நேரத்தை முடிவு செய்கிறது"),
            ("Distributes the disinvestment revenue directly to political parties", "பங்கு விலக்கல் வருவாயை நேரடியாக அரசியல் கட்சிகளுக்குப் பகிர்ந்தளிக்கிறது"),
            ("Orders the re-nationalization of all private buyers automatically", "தனியார் வாங்குபவர்களை மீண்டும் தானாக தேசியமயமாக்க உத்தரவிடுகிறது")
        ],
        "exp_en": "The CAG examines disinvestment transactions to ensure that asset valuation was fair and robust, competitive bidding procedures were maintained, and public assets were not sold below intrinsic value.",
        "exp_ta": "சொத்துக்களின் மதிப்பீடு நியாயமானதாக இருந்ததா, போட்டி ஏல நடைமுறைகள் பின்பற்றப்பட்டனவா மற்றும் பொதுச் சொத்துக்கள் குறைந்த விலைக்கு விற்கப்படவில்லையா என்பதை உறுதி செய்ய CAG தணிக்கை செய்கிறது.",
        "tip_en": "Disinvestment audit focuses on valuation methodology, reserve price setting, and bidding transparency.",
        "tip_ta": "பங்கு விலக்கல் தணிக்கை சொத்து மதிப்பீடு, அடிப்படை விலை நிர்ணயம் மற்றும் ஏல வெளிப்படைத்தன்மையில் கவனம் செலுத்துகிறது.",
        "fact_en": "Notable disinvestment audits included BALCO, Centaur Hotel, and VSNL sales.",
        "fact_ta": "பால்கோ (BALCO) மற்றும் சென்டார் ஹோட்டல் விற்பனை மீதான தணிக்கைகள் குறிப்பிடத்தக்கவை."
    },
    # 14
    {
        "subtopic": "Information Technology Audit",
        "stem_en": "In modern times, what guidelines does the CAG follow when auditing large IT systems like GSTN, Income Tax portal, or Aadhaar database integration?",
        "stem_ta": "நவீன காலத்தில், ஜி.எஸ்.டி.என் (GSTN), வருமான வரி தளம் போன்ற பெரிய தகவல் தொழில்நுட்ப அமைப்புகளைத் தணிக்கை செய்யும் போது சி.ஏ.ஜி எந்த வழிகாட்டுதல்களைப் பின்பற்றுகிறார்?",
        "options": [
            ("Information Systems Audit Guidelines benchmarked against COBIT and international IT standards", "COBIT மற்றும் சர்வதேச IT தரநிலைகளுக்கு ஏற்ப வரையறுக்கப்பட்ட தகவல் அமைப்புகள் தணிக்கை வழிகாட்டுதல்கள்"),
            ("General postal manual guidelines from 1885", "1885-ம் ஆண்டின் பொது அஞ்சல் கையேடு வழிகாட்டுதல்கள்"),
            ("Telecommunications telegraph code rules", "தொலைத்தொடர்பு தந்தி குறியீட்டு விதிகள்"),
            ("Railway passenger luggage ticket rules", "ரயில்வே பயணிகள் லக்கேஜ் பயணச்சீட்டு விதிகள்")
        ],
        "exp_en": "The CAG has institutionalized Information Systems (IS) Audit Guidelines benchmarked against global standards like COBIT to evaluate IT security, data integrity, and system efficiency.",
        "exp_ta": "தகவல் தொழில்நுட்பப் பாதுகாப்பு, தரவு ஒருமைப்பாடு மற்றும் அமைப்பின் செயல்திறனை மதிப்பீடு செய்ய COBIT போன்ற சர்வதேசத் தரநிலைகளுடன் கூடிய தகவல் அமைப்புகள் (IS) தணிக்கை வழிகாட்டுதல்களை CAG முறைப்படுத்தியுள்ளார்.",
        "tip_en": "IS Audit examines controls, cyber security, data validity, and business continuity in government IT.",
        "tip_ta": "IS தணிக்கை அரசு தகவல் தொழில்நுட்பத்தில் உள்ள கட்டுப்பாடுகள், சைபர் பாதுகாப்பு மற்றும் தரவு நம்பகத்தன்மையை ஆராய்கிறது.",
        "fact_en": "The CAG audited the systems and architecture of the Goods and Services Tax Network (GSTN).",
        "fact_ta": "சரக்கு மற்றும் சேவை வரி நெட்வொர்க்கின் (GSTN) கட்டமைப்பை சி.ஏ.ஜி தணிக்கை செய்துள்ளார்."
    },
    # 15
    {
        "subtopic": "Audit of Goods and Services Tax",
        "stem_en": "How does the Comptroller and Auditor General verify the allocation of Integrated GST (IGST) between the Centre and the States?",
        "stem_ta": "மத்திய மற்றும் மாநிலங்களுக்கு இடையே ஒருங்கிணைந்த ஜிஎஸ்டி (IGST) பகிர்ந்தளிக்கப்படுவதை தலைமைக் கணக்குத் தணிக்கையாளர் எவ்வாறு சரிபார்க்கிறார்?",
        "options": [
            ("Audits the monthly IGST settlement accounts, verifying that apportionment formulas conform to the IGST Act", "மாதாந்திர IGST தீர்வு கணக்குகளைத் தணிக்கை செய்து, பகிர்வு சூத்திரங்கள் IGST சட்டத்திற்கு உட்பட்டுள்ளதா என்பதைச் சரிபார்க்கிறார்"),
            ("Cancels tax collections whenever state revenue falls", "மாநில வருவாய் குறையும் போதெல்லாம் வரி வசூலை ரத்து செய்கிறார்"),
            ("Directs states to leave the GST Council unilaterally", "ஜிஎஸ்டி கவுன்சிலிலிருந்து தன்னிச்சையாக வெளியேறுமாறு மாநிலங்களுக்கு உத்தரவிடுகிறார்"),
            ("Has no jurisdiction to examine any indirect tax accounts", "எந்தவொரு மறைமுக வரிக் கணக்குகளையும் ஆய்வு செய்ய அதிகார வரம்பு இல்லை")
        ],
        "exp_en": "Under Section 16 of the 1971 Act, the CAG audits the accounts of IGST settlement and compensation cess collections, highlighting unapportioned balances in audit reports to Parliament.",
        "exp_ta": "1971 சட்டத்தின் பிரிவு 16-ன் கீழ், IGST தீர்வு மற்றும் இழப்பீட்டு செஸ் கணக்குகளை CAG தணிக்கை செய்து, பகிர்ந்தளிக்கப்படாத இருப்புக்களை நாடாளுமன்ற அறிக்கைகளில் சுட்டிக்காட்டுகிறார்.",
        "tip_en": "CAG audit ensures accurate devolution of IGST and timely release of GST compensation cess to States.",
        "tip_ta": "IGST துல்லியமாகப் பகிரப்படுவதையும் மாநிலங்களுக்கான ஜிஎஸ்டி இழப்பீடு முறையாக வழங்கப்படுவதையும் CAG தணிக்கை உறுதி செய்கிறது.",
        "fact_en": "CAG pointed out significant delays in IGST apportionment in consecutive union finance audit reports.",
        "fact_ta": "மத்திய நிதித் தணிக்கை அறிக்கைகளில் IGST பகிர்வில் ஏற்பட்ட குறிப்பிடத்தக்க தாமதங்களை CAG சுட்டிக்காட்டியுள்ளார்."
    },
    # 16
    {
        "subtopic": "Audit of Disaster Management Funds",
        "stem_en": "Under the Disaster Management Act, 2005, which statutory funds are audited by the Comptroller and Auditor General?",
        "stem_ta": "பேரிடர் மேலாண்மைச் சட்டம் 2005-ன் கீழ், தலைமைக் கணக்குத் தணிக்கையாளரால் தணிக்கை செய்யப்படும் சட்டப்பூர்வ நிதிகள் எவை?",
        "options": [
            ("National Disaster Response Fund (NDRF) and State Disaster Response Funds (SDRF)", "தேசிய பேரிடர் மீட்பு நிதி (NDRF) மற்றும் மாநில பேரிடர் மீட்பு நிதிகள் (SDRF)"),
            ("Only private international charitable calamity foundations", "தனியார் சர்வதேச தொண்டு அமைப்புகளின் பேரிடர் நிதிகள் மட்டுமே"),
            ("Personal life insurance policies of relief workers", "நிவாரணப் பணியாளர்களின் தனிப்பட்ட ஆயுள் காப்பீட்டுக் கொள்கைகள்"),
            ("Foreign disaster relief aid given to neighboring nations", "அண்டை நாடுகளுக்கு வழங்கப்படும் வெளிநாட்டு பேரிடர் நிவாரண உதவிகள்")
        ],
        "exp_en": "The accounts of the National Disaster Response Fund (NDRF) and State Disaster Response Funds (SDRF) are audited annually by the CAG in accordance with the Disaster Management Act, 2005.",
        "exp_ta": "2005-ம் ஆண்டின் பேரிடர் மேலாண்மைச் சட்டத்தின்படி தேசிய பேரிடர் மீட்பு நிதி (NDRF) மற்றும் மாநில பேரிடர் மீட்பு நிதிகளின் (SDRF) கணக்குகள் ஆண்டுதோறும் சி.ஏ.ஜி-யால் தணிக்கை செய்யப்படுகின்றன.",
        "tip_en": "NDRF and SDRF are statutory public funds; CAG audits both allocation and field utilization.",
        "tip_ta": "NDRF மற்றும் SDRF ஆகியவை சட்டப்பூர்வ பொது நிதிகள்; நிதி ஒதுக்கீடு மற்றும் களப் பயன்பாடு இரண்டையுமே CAG தணிக்கை செய்கிறார்.",
        "fact_en": "CAG performance audits have highlighted delays in establishing disaster mitigation funds.",
        "fact_ta": "பேரிடர் தணிப்பு நிதிகளை அமைப்பதில் ஏற்பட்ட தாமதங்களை சி.ஏ.ஜி செயல்திறன் தணிக்கைகள் வெளிப்படுத்தியுள்ளன."
    },
    # 17
    {
        "subtopic": "External Audit for United Nations",
        "stem_en": "What prestigious international role is frequently performed by the Comptroller and Auditor General of India for international organizations?",
        "stem_ta": "சர்வதேச நிறுவனங்களுக்காக இந்தியத் தலைமைக் கணக்குத் தணிக்கையாளரால் அடிக்கடி செய்யப்படும் மதிப்புமிக்க சர்வதேசப் பணி எது?",
        "options": [
            ("External Auditor of United Nations specialized agencies, including WHO, ILO, and IAEA", "உலக சுகாதார நிறுவனம் (WHO), சர்வதேச தொழிலாளர் அமைப்பு (ILO), சர்வதேச அணுசக்தி முகமை (IAEA) உள்ளிட்ட ஐ.நா அமைப்புகளின் வெளித் தணிக்கையாளர்"),
            ("Permanent Ambassador of India to the UN General Assembly", "ஐ.நா பொதுச் சபைக்கான இந்தியாவின் நிரந்தரத் தூதர்"),
            ("Judge of the International Court of Justice at The Hague", "ஹேக்கில் உள்ள சர்வதேச நீதிமன்றத்தின் நீதிபதி"),
            ("Director General of the World Bank", "உலக வங்கியின் தலைமை இயக்குநர்")
        ],
        "exp_en": "Due to its impeccable professional reputation, the CAG of India is repeatedly elected as the External Auditor for UN agencies, including WHO, Food and Agriculture Organization (FAO), and IAEA.",
        "exp_ta": "தனது சிறந்த தொழில்முறை நம்பகத்தன்மையின் காரணமாக, உலக சுகாதார நிறுவனம் (WHO), FAO மற்றும் IAEA உள்ளிட்ட ஐ.நா அமைப்புகளின் வெளித் தணிக்கையாளராக இந்திய CAG தொடர்ந்து தேர்ந்தெடுக்கப்படுகிறார்.",
        "tip_en": "CAG of India has served as External Auditor for WHO, WIPO, ILO, and Chair of the UN Board of Auditors.",
        "tip_ta": "இந்திய CAG, WHO, WIPO, ILO ஆகியவற்றின் வெளித் தணிக்கையாளராகவும் ஐ.நா தணிக்கையாளர்கள் குழுவின் தலைவராகவும் பணியாற்றியுள்ளார்.",
        "fact_en": "India is one of the most sought-after supreme audit institutions in the United Nations system.",
        "fact_ta": "ஐ.நா அமைப்பில் சர்வதேச தணிக்கைக்காக அதிகம் நாடப்படும் தணிக்கை நிறுவனங்களில் இந்தியாவும் ஒன்றாகும்."
    },
    # 18
    {
        "subtopic": "Action Taken Notes (ATNs)",
        "stem_en": "What are 'Action Taken Notes' (ATNs) in the parliamentary audit follow-up process involving the CAG and PAC?",
        "stem_ta": "சி.ஏ.ஜி மற்றும் PAC சம்பந்தப்பட்ட நாடாளுமன்ற தணிக்கை தொடர் நடவடிக்கையில் 'நடவடிக்கை எடுக்கப்பட்ட குறிப்புகள்' (ATNs) என்பது எதனைக் குறிக்கிறது?",
        "options": [
            ("Formal explanatory responses submitted by ministries detailing remedial action taken on CAG audit paras", "CAG தணிக்கைப் பத்திகள் மீது எடுக்கப்பட்ட தீர்வு நடவடிக்கைகளை விளக்கி அமைச்சகங்களால் சமர்ப்பிக்கப்படும் முறையான பதில்கள்"),
            ("Secret police reports filed against government auditors", "அரசு தணிக்கையாளர்களுக்கு எதிராகத் தாக்கல் செய்யப்படும் ரகசியக் காவல் அறிக்கைகள்"),
            ("Judicial judgments passed by the Supreme Court in contempt cases", "நீதிமன்ற அவமதிப்பு வழக்குகளில் உச்ச நீதிமன்றம் பிறப்பிக்கும் தீர்ப்புகள்"),
            ("Political leaflets distributed to voters during general elections", "பொதுத் தேர்தலின் போது வாக்காளர்களுக்கு விநியோகிக்கப்படும் அரசியல் துண்டுப் பிரசுரங்கள்")
        ],
        "exp_en": "Ministries must submit Action Taken Notes (ATNs) within a prescribed timeframe (usually 4 to 6 months) explaining corrective steps taken on CAG audit findings, which are vetted by CAG before PAC review.",
        "exp_ta": "CAG தணிக்கைக் கண்டுபிடிப்புகள் மீது எடுக்கப்பட்ட திருத்த நடவடிக்கைகளை விளக்கி அமைச்சகங்கள் குறிப்பிட்ட காலத்திற்குள் (4 முதல் 6 மாதங்கள்) நடவடிக்கை குறிப்புகளை (ATNs) சமர்ப்பிக்க வேண்டும்; இதை PAC ஆய்வுக்கு முன் CAG சரிபார்க்கிறார்.",
        "tip_en": "CAG audits -> PAC examines -> Ministries submit Action Taken Notes (ATNs) vetted by CAG.",
        "tip_ta": "CAG தணிக்கை செய்கிறார் -> PAC ஆராய்கிறது -> அமைச்சகங்கள் நடவடிக்கை குறிப்புகளை (ATN) சமர்ப்பிக்கின்றன.",
        "fact_en": "Failure to submit ATNs is treated as contempt of the parliamentary committee.",
        "fact_ta": "ATN சமர்ப்பிக்கத் தவறுவது நாடாளுமன்றக் குழுவை அவமதித்ததாகக் கருதப்படுகிறது."
    },
    # 19
    {
        "subtopic": "Borrowings and Public Debt Audit",
        "stem_en": "Under Articles 292 and 293 of the Constitution, what is the CAG's audit focus regarding Government borrowings and public debt?",
        "stem_ta": "சரத்துகள் 292 மற்றும் 293-ன் கீழ், அரசாங்கத்தின் கடன்கள் மற்றும் பொதுக் கடன் தொடர்பாக சி.ஏ.ஜி தணிக்கையின் முக்கியக் கவனம் என்ன?",
        "options": [
            ("Verifying that borrowings comply with limits set by law, debt servicing is accounted for, and funds utilized productively", "கடன்கள் சட்டத்தால் நிர்ணயிக்கப்பட்ட வரம்புகளுக்குள் உள்ளதா, கடன் திருப்பிச் செலுத்துதல் சரியாகக் கணக்கிடப்படுகிறதா மற்றும் நிதி ஆக்கப்பூர்வமாகப் பயன்படுத்தப்படுகிறதா என்பதைச் சரிபார்த்தல்"),
            ("Issuing sovereign bonds directly to foreign stock markets", "வெளிநாட்டு பங்குச் சந்தைகளுக்கு இறையாண்மைப் பத்திரங்களை நேரடியாக வெளியிடுதல்"),
            ("Cancelling the national debt unilaterally by executive proclamation", "நிர்வாகப் பிரகடனம் மூலம் தேசியக் கடனைத் தன்னிச்சையாக ரத்து செய்தல்"),
            ("Prohibiting State Governments from preparing any budget", "மாநில அரசாங்கங்கள் எந்தவொரு பட்ஜெட்டையும் தயாரிப்பதைத் தடை செய்தல்")
        ],
        "exp_en": "The CAG audits public debt transactions to ensure borrowings conform to constitutional limits under Articles 292 (Union) and 293 (States), interest payments are accurate, and debt sustainability norms observed.",
        "exp_ta": "கடன்கள் சரத்து 292 (மத்திய அரசு) மற்றும் 293 (மாநிலங்கள்) ஆகியவற்றின் அரசியலமைப்பு வரம்புகளுக்கு உட்பட்டுள்ளதா, வட்டி செலுத்தல்கள் சரியாக உள்ளதா மற்றும் கடன் நிலைத்தன்மை விதிகள் பின்பற்றப்படுகின்றனவா என்பதை CAG தணிக்கை செய்கிறார்.",
        "tip_en": "Article 292 = Borrowing by the Union; Article 293 = Borrowing by States.",
        "tip_ta": "சரத்து 292 = மத்திய அரசின் கடன்கள்; சரத்து 293 = மாநில அரசுகளின் கடன்கள்.",
        "fact_en": "CAG audit reports monitor compliance with State FRBM debt-to-GSDP targets.",
        "fact_ta": "மாநில FRBM சட்டத்தின் கடன்-மாநில மொத்த உற்பத்தி விகித இலக்குகளை சி.ஏ.ஜி அறிக்கைகள் கண்காணிக்கின்றன."
    },
    # 20
    {
        "subtopic": "C.G. Somiah Era",
        "stem_en": "Which Comptroller and Auditor General served during the transition period of 1990 to 1996 and authored the memoir 'The Honest Always Stand Alone'?",
        "stem_ta": "1990 முதல் 1996 வரையிலான மாற்றுக் காலத்தில் பணியாற்றி, 'The Honest Always Stand Alone' என்ற நினைவுக் குறிப்பை எழுதிய தலைமைக் கணக்குத் தணிக்கையாளர் யார்?",
        "options": [
            ("C.G. Somiah", "சி.ஜி. சோமையா"),
            ("T.N. Chaturvedi", "டி.என். சதுர்வேதி"),
            ("V.K. Shunglu", "வி.கே. சுங்லு"),
            ("A.K. Roy", "ஏ.கே. ராய்")
        ],
        "exp_en": "C.G. Somiah was the 8th CAG of India (1990-1996). He was an IAS officer from the Odisha cadre who authored 'The Honest Always Stand Alone' documenting his tenure in high constitutional offices.",
        "exp_ta": "சி.ஜி. சோமையா இந்தியாவின் 8-வது CAG (1990-1996) ஆவார். ஒடிசா கேடரைச் சேர்ந்த இவர், உயர் அரசியலமைப்புப் பதவிகளில் பணியாற்றிய தனது அனுபவங்களை 'The Honest Always Stand Alone' என்ற நூலாக எழுதினார்.",
        "tip_en": "C.G. Somiah: 8th CAG (1990-1996); book: 'The Honest Always Stand Alone'.",
        "tip_ta": "சி.ஜி. சோமையா: 8-வது CAG (1990-1996); நூல்: 'The Honest Always Stand Alone'.",
        "fact_en": "He previously served as Union Home Secretary before being appointed CAG.",
        "fact_ta": "சி.ஏ.ஜி-யாக நியமிக்கப்படுவதற்கு முன் இவர் மத்திய உள்துறைச் செயலாளராகப் பணியாற்றினார்."
    },
    # 21
    {
        "subtopic": "Audit of Defence Procurement",
        "stem_en": "How does the CAG balance national security confidentiality with financial accountability when auditing defence weapon procurements?",
        "stem_ta": "பாதுகாப்பு ஆயுதக் கொள்முதல்களைத் தணிக்கை செய்யும் போது தேசியப் பாதுகாப்பு ரகசியத்தன்மையையும் நிதிப் பொறுப்புடைமையையும் சி.ஏ.ஜி எவ்வாறு சமநிலைப்படுத்துகிறார்?",
        "options": [
            ("Examines all financial and technical processes while redacting sensitive operational details in the public report", "அனைத்து நிதி மற்றும் தொழில்நுட்ப நடைமுறைகளையும் ஆய்வு செய்து, பொது அறிக்கையில் முக்கிய பாதுகாப்பு விவரங்களை மறைத்து சமர்ப்பிக்கிறார்"),
            ("Completely exempts all military purchases from any financial audit", "அனைத்து ராணுவக் கொள்முதல்களுக்கும் எவ்வித நிதித் தணிக்கையிலிருந்தும் முழு விலக்கு அளிக்கிறார்"),
            ("Conducts live public press conferences revealing secret military radar frequencies", "ரகசிய ராணுவ ரேடார் அலைவரிசைகளை வெளிப்படுத்தி நேரடி செய்தியாளர் சந்திப்புகளை நடத்துகிறார்"),
            ("Demands that all fighter jets be tested by the CAG personal staff before delivery", "போர் விமானங்கள் ஒப்படைக்கப்படும் முன் சி.ஏ.ஜி ஊழியர்களால் சோதிக்கப்பட வேண்டும் எனக் கோருகிறார்")
        ],
        "exp_en": "In defence audits (such as the Rafale aircraft procurement audit of 2019), the CAG audits all comparative cost figures and procurement steps, but redacts commercially sensitive or operational security data in the published report.",
        "exp_ta": "பாதுகாப்புத் தணிக்கைகளில் (2019 ரஃபேல் தணிக்கை போன்ற) அனைத்து செலவுகளையும் கொள்முதல் படிகளையும் CAG தணிக்கை செய்கிறார், ஆனால் பொது அறிக்கையில் வணிக மற்றும் செயல்பாட்டு ரகசியங்களை மறைத்து வெளியிடுகிறார்.",
        "tip_en": "Redaction of sensitive operational parameters allows scrutiny of commercial pricing without harming national security.",
        "tip_ta": "செயல்பாட்டு ரகசியங்களை மறைப்பது தேசியப் பாதுகாப்பிற்கு குந்தகமின்றி வணிக விலையை ஆய்வு செய்ய உதவுகிறது.",
        "fact_en": "The 2019 CAG audit report on Capital Acquisition in the Indian Air Force was tabled in both Houses of Parliament.",
        "fact_ta": "இந்திய விமானப்படையின் மூலதனக் கொள்முதல் மீதான 2019 சி.ஏ.ஜி அறிக்கை நாடாளுமன்றத்தின் இரு அவைகளிலும் வைக்கப்பட்டது."
    },
    # 22
    {
        "subtopic": "Role in National Clean Ganga Mission",
        "stem_en": "What did the CAG's performance audit of the 'Namami Gange' program highlight regarding fund utilization and pollution control?",
        "stem_ta": "'நமாமி கங்கே' திட்டம் மீதான சி.ஏ.ஜி-யின் செயல்திறன் தணிக்கை, நிதிப் பயன்பாடு மற்றும் மாசுக் கட்டுப்பாடு குறித்து எதனைச் சுட்டிக்காட்டியது?",
        "options": [
            ("Substantial unutilized funds, delays in sewage treatment plant (STP) construction, and lack of long-term ecological planning", "பயன்படுத்தப்படாத பெருமளவிலான நிதி, கழிவுநீர் சுத்திகரிப்பு நிலையங்கள் (STP) அமைப்பதில் தாமதம் மற்றும் நீண்டகால சூழலியல் திட்டமிடல் இல்லாமை"),
            ("Certified that the river Ganga was 100% clean and free of all bacteria", "கங்கை நதி 100% தூய்மையடைந்து அனைத்து பாக்டீரியாக்களும் இன்றி உள்ளது என சான்றளித்தது"),
            ("Ordered the complete diversion of the river into the Arabian Sea", "கங்கை நதியை முழுமையாக அரபிக்கடலுக்குத் திருப்பிவிட உத்தரவிட்டது"),
            ("Recommended the immediate closure of all municipal corporations along the river", "நதிக்கரையோர அனைத்து மாநகராட்சிகளையும் உடனடியாக மூடப் பரிந்துரைத்தது")
        ],
        "exp_en": "The CAG's 2017 performance audit on the Rejuvenation of River Ganga highlighted slow utilization of funds, deficiencies in sewage treatment infrastructure, and shortfalls in water quality monitoring.",
        "exp_ta": "கங்கை நதியை புனரமைத்தல் மீதான சி.ஏ.ஜி-யின் 2017 செயல்திறன் தணிக்கை, நிதிப் பயன்பாட்டில் உள்ள மந்தநிலை, கழிவுநீர் சுத்திகரிப்பு உள்கட்டமைப்பு குறைபாடுகள் மற்றும் நீர் தரக் கண்காணிப்பு பற்றாக்குறைகளை சுட்டிக்காட்டியது.",
        "tip_en": "Performance audits of environmental missions examine physical progress against financial outlays.",
        "tip_ta": "சுற்றுச்சூழல் திட்டங்களின் செயல்திறன் தணிக்கை நிதி ஒதுக்கீட்டிற்கு எதிரான கள முன்னேற்றத்தை ஆராய்கிறது.",
        "fact_en": "The audit report was extensively examined by the Public Accounts Committee.",
        "fact_ta": "இந்த தணிக்கை அறிக்கை பொதுக் கணக்குக் குழுவால் விரிவாக ஆராயப்பட்டது."
    },
    # 23
    {
        "subtopic": "Audit of Centrally Sponsored Schemes",
        "stem_en": "How does the CAG audit Centrally Sponsored Schemes (CSS) where implementation is carried out by State Governments?",
        "stem_ta": "மாநில அரசாங்கங்களால் செயல்படுத்தப்படும் மத்திய நிதியுதவித் திட்டங்களை (CSS) சி.ஏ.ஜி எவ்வாறு தணிக்கை செய்கிறார்?",
        "options": [
            ("Conducts an all-India coordinated audit covering both Central ministries and state implementing departments", "மத்திய அமைச்சகங்கள் மற்றும் மாநில செயலாக்கத் துறைகள் ஆகிய இரண்டையுமே உள்ளடக்கிய அகில இந்திய ஒருங்கிணைந்த தணிக்கையை நடத்துகிறார்"),
            ("Audits only the central government ministry and completely ignores state field offices", "மத்திய அமைச்சகத்தை மட்டுமே தணிக்கை செய்து, மாநில கள அலுவலகங்களை முற்றிலும் புறக்கணிக்கிறார்"),
            ("Directs states to stop funding centrally sponsored schemes immediately", "மத்திய நிதியுதவித் திட்டங்களுக்கு நிதி வழங்குவதை உடனடியாக நிறுத்துமாறு மாநிலங்களுக்கு உத்தரவிடுகிறார்"),
            ("Appoints foreign private auditors to inspect village beneficiaries", "கிராமப்புறப் பயனாளிகளை ஆய்வு செய்ய வெளிநாட்டுத் தனியார் தணிக்கையாளர்களை நியமிக்கிறார்")
        ],
        "exp_en": "For major Centrally Sponsored Schemes (like Samagra Shiksha, PM Awas Yojana, Ayushman Bharat), the CAG designs a pan-India audit guidelines framework executed simultaneously across all States by local Accountants General.",
        "exp_ta": "சமக்ர சிக்ஷா, பி.எம் ஆவாஸ் யோஜனா போன்ற திட்டங்களுக்கு, நாடு தழுவிய தணிக்கை வழிகாட்டுதலை CAG உருவாக்கி, அனைத்து மாநிலங்களிலும் உள்ள உள்ளூர் கணக்காயர்கள் மூலம் ஒரே நேரத்தில் தணிக்கை செய்கிறார்.",
        "tip_en": "Pan-India coordinated audits provide Parliament a comprehensive picture of national scheme delivery across all States.",
        "tip_ta": "நாடு தழுவிய ஒருங்கிணைந்த தணிக்கைகள் அனைத்து மாநிலங்களிலும் மத்தியத் திட்டங்கள் செயல்படும் நிலையை நாடாளுமன்றத்திற்கு முழுமையாகக் காட்டுகின்றன.",
        "fact_en": "State-specific findings are also tabled in respective State Assemblies by the Governor.",
        "fact_ta": "மாநிலம் சார்ந்த தணிக்கை முடிவுகள் ஆளுநர் மூலம் அந்தந்த மாநில சட்டமன்றங்களிலும் வைக்கப்படுகின்றன."
    },
    # 24
    {
        "subtopic": "Indian Audit and Accounts Service (IA&AS)",
        "stem_en": "Through which competitive examination are officers of the Indian Audit and Accounts Service (IA&AS) recruited?",
        "stem_ta": "இந்தியத் தணிக்கை மற்றும் கணக்குப் பணி (IA&AS) அதிகாரிகள் எந்தப் போட்டித் தேர்வின் மூலம் தேர்ந்தெடுக்கப்படுகிறார்கள்?",
        "options": [
            ("UPSC Civil Services Examination", "UPSC குடிமைப் பணிகள் தேர்வு (Civil Services Examination)"),
            ("Staff Selection Commission Combined Graduate Level Exam", "Staff Selection Commission ஒருங்கிணைந்த பட்டதாரி நிலைத் தேர்வு"),
            ("Institute of Chartered Accountants of India Final Exam", "இந்தியப் பட்டயக் கணக்காளர்கள் நிறுவன இறுதித் தேர்வு"),
            ("Reserve Bank of India Grade B Officer Exam", "இந்திய ரிசர்வ் வங்கி கிரேடு பி அதிகாரி தேர்வு")
        ],
        "exp_en": "Officers of the IA&AS are Group 'A' central civil servants recruited through the annual Civil Services Examination conducted by the Union Public Service Commission (UPSC).",
        "exp_ta": "IA&AS அதிகாரிகள், மத்திய அரசுப் பணியாளர் தேர்வாணையம் (UPSC) நடத்தும் வருடாந்திர குடிமைப் பணிகள் தேர்வு மூலம் தேர்ந்தெடுக்கப்படும் குரூப் 'A' மத்திய சிவில் சேவை அதிகாரிகள் ஆவர்.",
        "tip_en": "IA&AS is an All-India/Central Group A service trained at the National Academy of Audit and Accounts, Shimla.",
        "tip_ta": "IA&AS என்பது சிம்லாவில் உள்ள தேசிய தணிக்கை மற்றும் கணக்கு அகாடமியில் பயிற்சி பெறும் குரூப் A மத்தியப் பணியாகும்.",
        "fact_en": "The National Academy of Audit and Accounts (NAAA) is located at Shimla, Himachal Pradesh.",
        "fact_ta": "தேசிய தணிக்கை மற்றும் கணக்கு அகாடமி (NAAA) இமாச்சலப் பிரதேசத்தின் சிம்லாவில் அமைந்துள்ளது."
    },
    # 25
    {
        "subtopic": "National Academy of Audit and Accounts",
        "stem_en": "Where is the premier training institution of the Indian Audit and Accounts Service, the National Academy of Audit and Accounts (NAAA), located?",
        "stem_ta": "இந்தியத் தணிக்கை மற்றும் கணக்குப் பணியின் முதன்மைப் பயிற்சி நிறுவனமான தேசிய தணிக்கை மற்றும் கணக்கு அகாடமி (NAAA) எங்கு அமைந்துள்ளது?",
        "options": [
            ("Shimla, Himachal Pradesh", "சிம்லா, இமாச்சலப் பிரதேசம்"),
            ("Mussoorie, Uttarakhand", "முசோரி, உத்தராகண்ட்"),
            ("Hyderabad, Telangana", "ஹைதராபாத், தெலங்கானா"),
            ("Nagpur, Maharashtra", "நாக்பூர், மகாராஷ்டிரா")
        ],
        "exp_en": "The National Academy of Audit and Accounts (NAAA), which trains officers of the Indian Audit and Accounts Service (IA&AS), is located in Shimla, Himachal Pradesh.",
        "exp_ta": "IA&AS அதிகாரிகளுக்குப் பயிற்சி அளிக்கும் முதன்மை நிறுவனமான தேசிய தணிக்கை மற்றும் கணக்கு அகாடமி (NAAA), இமாச்சலப் பிரதேச மாநிலம் சிம்லாவில் அமைந்துள்ளது.",
        "tip_en": "IAS = Mussoorie (LBSNAA); IPS = Hyderabad (SVPNPA); IA&AS = Shimla (NAAA).",
        "tip_ta": "IAS = முசோரி (LBSNAA); IPS = ஹைதராபாத் (SVPNPA); IA&AS = சிம்லா (NAAA).",
        "fact_en": "NAAA is housed in the historic Yarrows estate in Shimla.",
        "fact_ta": "NAAA சிம்லாவில் உள்ள வரலாற்று சிறப்புமிக்க யாரோஸ் (Yarrows) வளாகத்தில் அமைந்துள்ளது."
    },
    # 26
    {
        "subtopic": "Principal Accountant General in States",
        "stem_en": "Who represents the Comptroller and Auditor General at the State level to manage state audit and accounts?",
        "stem_ta": "மாநில அளவில் மாநிலத் தணிக்கை மற்றும் கணக்குகளை நிர்வகிக்க சி.ஏ.ஜி-யைப் பிரதிநிதித்துவப்படுத்துபவர் யார்?",
        "options": [
            ("Principal Accountant General (PAG) / Accountant General (AG)", "முதன்மைக் கணக்காயர் (PAG) / கணக்காயர் (AG)"),
            ("State Finance Secretary", "மாநில நிதிச் செயலாளர்"),
            ("Director of Local Fund Audit", "உள்ளாட்சி நிதித் தணிக்கை இயக்குநர்"),
            ("Advocate General of the State", "மாநில அட்வகேட் ஜெனரல்")
        ],
        "exp_en": "The Principal Accountant General (PAG) or Accountant General (AG), an officer of the IA&AS, heads the state audit and accounts directorates on behalf of the CAG.",
        "exp_ta": "IA&AS அதிகாரியான முதன்மைக் கணக்காயர் (PAG) அல்லது கணக்காயர் (AG), சி.ஏ.ஜி சார்பாக மாநிலத் தணிக்கை மற்றும் கணக்கு இயக்குநரகங்களுக்குத் தலைமை தாங்குகிறார்.",
        "tip_en": "Principal Accountant General works directly under the CAG, NOT under the State Government.",
        "tip_ta": "முதன்மைக் கணக்காயர் மாநில அரசின் கீழ் அல்ல, நேரடியாக CAG-ன் கீழேயே பணியாற்றுகிறார்.",
        "fact_en": "In Tamil Nadu, the office of the Principal Accountant General is located at Teynampet, Chennai.",
        "fact_ta": "தமிழ்நாட்டில் முதன்மைக் கணக்காயர் அலுவலகம் சென்னை தேனாம்பேட்டையில் அமைந்துள்ளது."
    },
    # 27
    {
        "subtopic": "Audit of Food Corporation of India",
        "stem_en": "How is the Food Corporation of India (FCI) audited under the Food Corporations Act, 1964?",
        "stem_ta": "உணவுக் கழகச் சட்டம் 1964-ன் கீழ் இந்திய உணவுக் கழகம் (FCI) எவ்வாறு தணிக்கை செய்யப்படுகிறது?",
        "options": [
            ("Audited by qualified auditors appointed by the Central Government on the advice of the CAG, with CAG conducting supplementary audits", "சி.ஏ.ஜி-யின் ஆலோசனையின் பேரில் மத்திய அரசால் நியமிக்கப்படும் தணிக்கையாளர்களால் தணிக்கை செய்யப்படுகிறது, மேலும் CAG துணைத் தணிக்கைகளையும் நடத்துகிறார்"),
            ("Audited exclusively by local private flour mills", "உள்ளூர் தனியார் மாவு ஆலைகளால் மட்டுமே தணிக்கை செய்யப்படுகிறது"),
            ("Completely exempt from all accounting scrutiny", "அனைத்து கணக்கியல் ஆய்விலிருந்தும் முழு விலக்கு பெற்றது"),
            ("Audited by the United Nations World Food Programme directly", "ஐ.நா உலக உணவுத் திட்டத்தால் நேரடியாகத் தணிக்கை செய்யப்படுகிறது")
        ],
        "exp_en": "Under the Food Corporations Act 1964, the accounts of FCI are audited by auditors appointed by the Government on the advice of the CAG, and the CAG has the right to conduct supplementary or test audits.",
        "exp_ta": "1964 சட்டத்தின்படி, CAG ஆலோசனையின் பேரில் அரசால் நியமிக்கப்படும் தணிக்கையாளர்கள் FCI கணக்குகளைத் தணிக்கை செய்கின்றனர், மேலும் துணை அல்லது மாதிரித் தணிக்கை நடத்த CAG-க்கு உரிமை உண்டு.",
        "tip_en": "Statutory corporations like FCI, ONGC have supplementary audit oversight by the CAG.",
        "tip_ta": "FCI போன்ற சட்டப்பூர்வ நிறுவனங்களில் CAG துணைத் தணிக்கை மேற்பார்வையைக் கொண்டுள்ளார்.",
        "fact_en": "CAG audit reports on FCI frequently scrutinize food subsidy management and buffer stock storage losses.",
        "fact_ta": "FCI மீதான CAG தணிக்கை உணவு மானிய மேலாண்மை மற்றும் சேமிப்புக் கிடங்கு இழப்புகளை விரிவாக ஆராய்கிறது."
    },
    # 28
    {
        "subtopic": "Commonwealth Games Audit",
        "stem_en": "The 2011 high-level committee appointed to investigate irregularities in the 2010 Commonwealth Games in Delhi was headed by which former CAG?",
        "stem_ta": "தில்லியில் நடைபெற்ற 2010 காமன்வெல்த் போட்டிகளின் முறைகேடுகளை விசாரிக்க அமைக்கப்பட்ட 2011 உயர்மட்டக் குழுவிற்குத் தலைமை தாங்கிய முன்னாள் சி.ஏ.ஜி யார்?",
        "options": [
            ("V.K. Shunglu", "வி.கே. சுங்லு"),
            ("Vinod Rai", "வினோத் ராய்"),
            ("C.G. Somiah", "சி.ஜி. சோமையா"),
            ("T.N. Chaturvedi", "டி.என். சதுர்வேதி")
        ],
        "exp_en": "Former CAG V.K. Shunglu was appointed to head the High-Level Committee (Shunglu Committee) in October 2010 to investigate financial mismanagement in the Delhi Commonwealth Games.",
        "exp_ta": "தில்லி காமன்வெல்த் போட்டிகளில் நடந்த நிதி முறைகேடுகளை விசாரிக்க அக்டோபர் 2010-ல் அமைக்கப்பட்ட உயர்மட்டக் குழுவிற்கு (சுங்லு குழு) முன்னாள் CAG வி.கே. சுங்லு தலைமை தாங்கினார்.",
        "tip_en": "V.K. Shunglu: 9th CAG of India (1996-2002); headed CWG probe committee in 2010-11.",
        "tip_ta": "வி.கே. சுங்லு: இந்தியாவின் 9-வது CAG (1996-2002); 2010-11 காமன்வெல்த் விசாரணைக் குழுவின் தலைவர்.",
        "fact_en": "The Shunglu Committee submitted six detailed reports exposing systemic tender rigging and cost overruns.",
        "fact_ta": "சுங்லு குழு டெண்டர் முறைகேடுகள் மற்றும் அதிகப்படியான செலவுகளை வெளிப்படுத்தும் ஆறு விரிவான அறிக்கைகளைச் சமர்ப்பித்தது."
    },
    # 29
    {
        "subtopic": "Rajiv Mehrishi Tenure",
        "stem_en": "Who served as the 13th Comptroller and Auditor General of India from 2017 to 2020, having previously served as Union Home Secretary and Finance Secretary?",
        "stem_ta": "முன்னதாக மத்திய உள்துறைச் செயலாளராகவும் நிதிச் செயலாளராகவும் இருந்து, பின்னர் 2017 முதல் 2020 வரை இந்தியாவின் 13-வது தலைமைக் கணக்குத் தணிக்கையாளராகப் பணியாற்றியவர் யார்?",
        "options": [
            ("Rajiv Mehrishi", "ராஜீவ் மெஹ்ரிஷி"),
            ("Shashi Kant Sharma", "சசி காந்த் சர்மா"),
            ("Vinod Rai", "வினோத் ராய்"),
            ("G.C. Murmu", "ஜி.சி. முர்மு")
        ],
        "exp_en": "Rajiv Mehrishi, a 1978-batch IAS officer, served as the 13th CAG of India from September 2017 to August 2020.",
        "exp_ta": "1978-ம் ஆண்டு பேட்ச் ஐ.ஏ.எஸ் அதிகாரியான ராஜீவ் மெஹ்ரிஷி, செப்டம்பர் 2017 முதல் ஆகஸ்ட் 2020 வரை இந்தியாவின் 13-வது சி.ஏ.ஜி-யாகப் பணியாற்றினார்.",
        "tip_en": "Rajiv Mehrishi: 13th CAG of India (2017-2020). Preceded G.C. Murmu.",
        "tip_ta": "ராஜீவ் மெஹ்ரிஷி: இந்தியாவின் 13-வது CAG (2017-2020). ஜி.சி. முர்முவுக்கு முன் பணியாற்றியவர்.",
        "fact_en": "During his tenure, the CAG published audit reports on the GST implementation and the Rafale procurement.",
        "fact_ta": "இவரது பதவிக்காலத்தில் ஜி.எஸ்.டி அமலாக்கம் மற்றும் ரஃபேல் கொள்முதல் மீதான தணிக்கை அறிக்கைகள் வெளியிடப்பட்டன."
    },
    # 30
    {
        "subtopic": "Audit of Municipal Corporations",
        "stem_en": "Why does the CAG audit the implementation of urban flagship missions like the Smart Cities Mission and AMRUT in Municipal Corporations?",
        "stem_ta": "மாநகராட்சிகளில் ஸ்மார்ட் சிட்டி திட்டம் மற்றும் அம்ருத் (AMRUT) போன்ற நகர்ப்புற முதன்மைத் திட்டங்களை சி.ஏ.ஜி ஏன் தணிக்கை செய்கிறார்?",
        "options": [
            ("Because these missions are substantially funded by grants from the Consolidated Fund of India under Section 14/15", "ஏனெனில் இத்திட்டங்கள் பிரிவு 14/15-ன் கீழ் இந்தியத் திரட்டப்பட்ட நிதியிலிருந்து கணிசமான மானியங்களைப் பெறுகின்றன"),
            ("Because the Constitution abolished local self-government autonomy in 1992", "ஏனெனில் 1992-ல் அரசியலமைப்பு உள்ளாட்சி சுயாட்சியை ஒழித்துவிட்டது"),
            ("Because municipal commissioners are all appointed as Supreme Court judges", "ஏனெனில் நகராட்சி ஆணையர்கள் அனைவரும் உச்ச நீதிமன்ற நீதிபதிகளாக நியமிக்கப்படுகிறார்கள்"),
            ("Because the CAG directly collects property tax from all urban households", "ஏனெனில் அனைத்து நகர்ப்புற வீடுகளிலிருந்தும் சொத்து வரியை CAG நேரடியாக வசூலிக்கிறார்")
        ],
        "exp_en": "Under Sections 14 and 15 of the 1971 Act, when Central and State governments finance urban missions through grants, the CAG audits the utilization of these funds and achievement of project milestones.",
        "exp_ta": "1971 சட்டத்தின் பிரிவுகள் 14 மற்றும் 15-ன் கீழ், நகர்ப்புற திட்டங்களுக்கு மத்திய மற்றும் மாநில அரசுகள் மானியங்கள் வழங்கும் போது, நிதியின் பயன்பாடு மற்றும் திட்ட மைல்கற்களை CAG தணிக்கை செய்கிறார்.",
        "tip_en": "Where public revenue flows, CAG audit follows.",
        "tip_ta": "பொது நிதி எங்கு செல்கிறதோ, அங்கு சி.ஏ.ஜி தணிக்கையும் தொடர்கிறது.",
        "fact_en": "Audit of municipal execution ensures that urban grants improve citizens' civic infrastructure as promised.",
        "fact_ta": "மாநகராட்சி தணிக்கை, நகர்ப்புற மானியங்கள் குடிமக்களின் உள்கட்டமைப்பை மேம்படுத்துவதை உறுதி செய்கிறது."
    },
    # 31
    {
        "subtopic": "CAG and Indian Railways",
        "stem_en": "How does the Comptroller and Auditor General conduct the audit of Indian Railways finances after the merger of the Railway Budget with the Union Budget in 2017?",
        "stem_ta": "2017-ல் ரயில்வே பட்ஜெட் மத்திய பட்ஜெட்டுடன் இணைக்கப்பட்ட பிறகு, இந்திய ரயில்வேயின் நிதியை சி.ஏ.ஜி எவ்வாறு தணிக்கை செய்கிறார்?",
        "options": [
            ("Presents a dedicated Railway Audit Report to Parliament covering operating ratio, capital investments, and passenger amenities", "செயல்பாட்டு விகிதம் (Operating Ratio), மூலதன முதலீடுகள் மற்றும் பயணிகள் வசதிகளை உள்ளடக்கிய பிரத்யேக ரயில்வே தணிக்கை அறிக்கையை நாடாளுமன்றத்தில் சமர்ப்பிக்கிறார்"),
            ("Stopped all railway auditing permanently following the merger", "பட்ஜெட் இணைப்பிற்குப் பிறகு அனைத்து ரயில்வே தணிக்கையையும் நிரந்தரமாக நிறுத்திவிட்டார்"),
            ("Allows private travel agents to conduct railway safety inspections", "தனியார் பயண முகவர்களை ரயில்வே பாதுகாப்பு ஆய்வுகளை நடத்த அனுமதிக்கிறார்"),
            ("Abolished all railway accounting departments across all zones", "அனைத்து மண்டலங்களிலும் உள்ள ரயில்வே கணக்குத் துறைகளை ஒழித்துவிட்டார்")
        ],
        "exp_en": "The CAG continues to audit Indian Railways thoroughly, presenting an annual dedicated audit report analyzing the Operating Ratio, safety fund expenditures, freight operations, and project execution.",
        "exp_ta": "CAG தொடர்ந்து இந்திய ரயில்வேயை விரிவாகத் தணிக்கை செய்து, செயல்பாட்டு விகிதம், பாதுகாப்பு நிதிச் செலவுகள், சரக்குப் போக்குவரத்து மற்றும் திட்டப் பணிகளை ஆராயும் வருடாந்திர பிரத்யேக அறிக்கையைச் சமர்ப்பிக்கிறார்.",
        "tip_en": "CAG reports on Railways closely track the 'Operating Ratio' (how much money is spent to earn Rs. 100).",
        "tip_ta": "ரயில்வே மீதான CAG அறிக்கைகள் 'செயல்பாட்டு விகிதத்தை' (ரூ. 100 சம்பாதிக்க எவ்வளவு செலவாகிறது) உன்னிப்பாகக் கண்காணிக்கின்றன.",
        "fact_en": "A high operating ratio (e.g., above 98%) indicates low profitability and limited surplus for capital investment.",
        "fact_ta": "அதிக செயல்பாட்டு விகிதம் (98%-க்கு மேல்) குறைந்த லாபத்தையும் மூலதன முதலீட்டிற்கு நிதி பற்றாக்குறையையும் காட்டுகிறது."
    },
    # 32
    {
        "subtopic": "Audit of Defense Canteens (CSD)",
        "stem_en": "Are the commercial transactions of the Canteen Stores Department (CSD) of the Armed Forces audited by the CAG?",
        "stem_ta": "முப்படைகளின் கேண்டீன் ஸ்டோர்ஸ் துறையின் (CSD) வணிகப் பரிவர்த்தனைகள் சி.ஏ.ஜி-யால் தணிக்கை செய்யப்படுகின்றனவா?",
        "options": [
            ("Yes, the CSD is audited by the CAG as a commercial departmental undertaking", "ஆம், ஒரு வணிகத் துறைசார் நிறுவனமாக CSD சி.ஏ.ஜி-யால் தணிக்கை செய்யப்படுகிறது"),
            ("No, military canteens are completely exempt from all financial audit", "இல்லை, ராணுவ கேண்டீன்களுக்கு அனைத்து நிதித் தணிக்கையிலிருந்தும் முழு விலக்கு உண்டு"),
            ("No, military canteens are audited by the United Nations Peacekeeping Force", "இல்லை, ராணுவ கேண்டீன்கள் ஐ.நா அமைதிப் படையால் தணிக்கை செய்யப்படுகின்றன"),
            ("Only if soldiers file written petitions to the Supreme Court", "சிப்பாய்கள் உச்ச நீதிமன்றத்தில் எழுத்துப்பூர்வ மனு தாக்கல் செய்தால் மட்டுமே")
        ],
        "exp_en": "The Canteen Stores Department (CSD) is a departmentally run commercial undertaking under the Ministry of Defence. Its accounts, inventory management, and profit distribution are audited by the CAG.",
        "exp_ta": "கேண்டீன் ஸ்டோர்ஸ் துறை (CSD) என்பது பாதுகாப்பு அமைச்சகத்தின் கீழ் இயங்கும் ஒரு வணிக நிறுவனமாகும். இதன் கணக்குகள், சரக்கு மேலாண்மை மற்றும் லாபப் பகிர்வு ஆகியவை சி.ஏ.ஜி-யால் தணிக்கை செய்யப்படுகின்றன.",
        "tip_en": "CSD is audited by the Principal Director of Audit (Defence Services) under the CAG.",
        "tip_ta": "CSD சி.ஏ.ஜி-யின் கீழ் உள்ள பாதுகாப்புப் பணிகள் முதன்மைத் தணிக்கை இயக்குநரால் தணிக்கை செய்யப்படுகிறது.",
        "fact_en": "CSD is one of the largest retail retail networks in India, serving millions of serving and retired armed forces personnel.",
        "fact_ta": "CSD இந்தியாவில் உள்ள மிகப்பெரிய சில்லறை விற்பனை வலையமைப்புகளில் ஒன்றாகும்."
    },
    # 33
    {
        "subtopic": "Section 19 of CAG Act",
        "stem_en": "Under Section 19(2) of the CAG's (DPC) Act, 1971, how are statutory corporations created by Parliament audited by the CAG?",
        "stem_ta": "1971-ம் ஆண்டின் CAG சட்டத்தின் பிரிவு 19(2)-ன் கீழ், நாடாளுமன்றத்தால் உருவாக்கப்பட்ட சட்டப்பூர்வ நிறுவனங்கள் சி.ஏ.ஜி-யால் எவ்வாறு தணிக்கை செய்யப்படுகின்றன?",
        "options": [
            ("In accordance with the provisions of the respective parliamentary statute establishing the corporation", "அந்தக் கழகத்தை நிறுவிய நாடாளுமன்றச் சட்டத்தின் விதிகளுக்கு இணங்க தணிக்கை செய்யப்படுகின்றன"),
            ("By conducting a secret ballot of all corporate shareholders", "அனைத்து கார்ப்பரேட் பங்குதாரர்களின் இரகசிய வாக்கெடுப்பு நடத்துவதன் மூலம்"),
            ("By selling the corporate shares on the foreign stock exchange", "வெளிநாட்டு பங்குச் சந்தையில் நிறுவனப் பங்குகளை விற்பதன் மூலம்"),
            ("CAG has no power to enter any statutory corporation", "எந்தவொரு சட்டப்பூர்வ நிறுவனத்திலும் நுழைய CAG-க்கு அதிகாரம் இல்லை")
        ],
        "exp_en": "Section 19(2) provides that the duties and powers of the CAG in relation to the audit of accounts of corporations established by law made by Parliament shall be performed and exercised in accordance with the provisions of the respective legislations.",
        "exp_ta": "பிரிவு 19(2) நாடாளுமன்றச் சட்டத்தால் உருவாக்கப்பட்ட நிறுவனங்களின் கணக்குகளைத் தணிக்கை செய்வதில் CAG-யின் அதிகாரங்கள் அந்தந்த சட்டங்களின் விதிகளின்படி பயன்படுத்தப்பட வேண்டும் என்று கூறுகிறது.",
        "tip_en": "Section 19(1) = Government Companies; Section 19(2) = Corporations established by Parliament.",
        "tip_ta": "பிரிவு 19(1) = அரசு நிறுவனங்கள்; பிரிவு 19(2) = நாடாளுமன்றச் சட்டத்தால் அமைக்கப்பட்ட கழகங்கள்.",
        "fact_en": "Each enabling Act specifies whether CAG audit is sole, supplementary, or absent.",
        "fact_ta": "ஒவ்வொரு சட்டமும் CAG தணிக்கை நேரடியானதா, துணையானதா அல்லது இல்லையா என்பதைக் குறிப்பிடுகிறது."
    },
    # 34
    {
        "subtopic": "Audit of Subsidies",
        "stem_en": "What is the primary objective of the CAG's compliance and performance audit of major government subsidies (such as food, fertilizer, and petroleum)?",
        "stem_ta": "முக்கிய அரசு மானியங்கள் (உணவு, உரம், பெட்ரோலியம் போன்றவை) மீதான சி.ஏ.ஜி-யின் தணிக்கையின் முதன்மை நோக்கம் என்ன?",
        "options": [
            ("Verifying that subsidies reach intended genuine beneficiaries, claims are properly verified, and fiscal leakages are checked", "மானியங்கள் தகுதியான உண்மையான பயனாளிகளைச் சென்றடைவதை உறுதி செய்தல், கோரிக்கைகள் சரிபார்க்கப்படுதல் மற்றும் நிதி கசிவுகள் தடுக்கப்படுதல்"),
            ("Ordering the immediate abolition of all welfare subsidies", "அனைத்து நலத்திட்ட மானியங்களையும் உடனடியாக ரத்து செய்ய உத்தரவிடுதல்"),
            ("Personally manufacturing chemical fertilizers in audit laboratories", "தணிக்கை ஆய்வகங்களில் ரசாயன உரங்களை நேரடியாக உற்பத்தி செய்தல்"),
            ("Determining international crude oil prices on world exchanges", "உலகச் சந்தைகளில் சர்வதேச கச்சா எண்ணெய் விலைகளைத் தீர்மானித்தல்")
        ],
        "exp_en": "CAG audits of subsidies evaluate whether budget allocations were disbursed according to statutory guidelines, subsidy calculations by manufacturing companies were accurate, and unintended benefits or ghost claims were minimized.",
        "exp_ta": "மானியங்கள் மீதான CAG தணிக்கை, நிதி ஒதுக்கீடுகள் உரிய விதிகளின்படி வழங்கப்பட்டதா, நிறுவனங்களின் மானியக் கணக்கீடுகள் சரியானவையா மற்றும் போலி கோரிக்கைகள் தடுக்கப்பட்டனவா என்பதை மதிப்பீடு செய்கிறது.",
        "tip_en": "Subsidy audits check targeting, verification of claims, and prevention of leakages.",
        "tip_ta": "மானியத் தணிக்கை சரியான பயனாளிகளை அடைதல், கோரிக்கைகளைச் சரிபார்த்தல் மற்றும் கசிவுகளைத் தடுப்பதில் கவனம் செலுத்துகிறது.",
        "fact_en": "Direct Benefit Transfer (DBT) has significantly assisted in minimizing subsidy leakages identified in past CAG reports.",
        "fact_ta": "நேரடிப் பயன் பரிமாற்றம் (DBT) கடந்த கால CAG அறிக்கைகளில் சுட்டிக்காட்டப்பட்ட மானியக் கசிவுகளைக் கணிசமாகக் குறைத்துள்ளது."
    },
    # 35
    {
        "subtopic": "Environmental Clearance Audits",
        "stem_en": "What systemic issue did the CAG's audit of environmental clearances and monitoring by the Ministry of Environment highlight?",
        "stem_ta": "சுற்றுச்சூழல் அமைச்சகத்தின் சுற்றுச்சூழல் அனுமதிகள் மற்றும் கண்காணிப்பு மீதான சி.ஏ.ஜி-யின் தணிக்கை எந்த அமைப்புசார் பிரச்சினையைச் சுட்டிக்காட்டியது?",
        "options": [
            ("Severe shortfall in post-clearance monitoring and widespread failure to enforce environmental compliance conditions", "சுற்றுச்சூழல் அனுமதிக்குப் பிந்தைய கண்காணிப்பில் கடுமையான குறைபாடு மற்றும் நிபந்தனைகளை அமல்படுத்துவதில் ஏற்பட்ட பரவலான தோல்வி"),
            ("Recommended the immediate cutting down of all reserved forests", "அனைத்து பாதுகாக்கப்பட்ட காடுகளையும் உடனடியாக வெட்டி அழிக்கப் பரிந்துரைத்தது"),
            ("Abolished the Central Pollution Control Board completely", "மத்திய மாசுக் கட்டுப்பாட்டு வாரியத்தை முற்றிலும் ஒழித்துவிட்டது"),
            ("Directed all industrial factories in India to shut down permanently", "இந்தியாவில் உள்ள அனைத்து தொழிற்சாலைகளையும் நிரந்தரமாக மூட உத்தரவிட்டது")
        ],
        "exp_en": "The CAG's performance audit on environmental clearances highlighted that regional offices of the Ministry failed to monitor project compliance post-approval, leading to unchecked violations of green norms.",
        "exp_ta": "சுற்றுச்சூழல் அனுமதிகள் மீதான சி.ஏ.ஜி செயல்திறன் தணிக்கை, அனுமதிக்குப் பிறகு அமைச்சகத்தின் மண்டல அலுவலகங்கள் திட்டங்களைக் கண்காணிக்கத் தவறியதால் சுற்றுச்சூழல் விதிமீறல்கள் கண்காணிக்கப்படாமல் போனதை சுட்டிக்காட்டியது.",
        "tip_en": "CAG environmental audits focus heavily on post-clearance monitoring and compliance enforcement.",
        "tip_ta": "சி.ஏ.ஜி-யின் சுற்றுச்சூழல் தணிக்கைகள் அனுமதிக்குப் பிந்தைய கண்காணிப்பு மற்றும் விதி அமலாக்கத்தில் பெரிதும் கவனம் செலுத்துகின்றன.",
        "fact_en": "These audit findings prompted judicial intervention in the National Green Tribunal and Supreme Court.",
        "fact_ta": "இந்த தணிக்கை முடிவுகள் தேசிய பசுமைத் தீர்ப்பாயம் மற்றும் உச்ச நீதிமன்றத்தில் நீதித்துறை தலையீட்டிற்கு வழிவகுத்தன."
    },
    # 36
    {
        "subtopic": "Public Debt Management",
        "stem_en": "In its audit of Union Finance Accounts, how does the CAG analyze the 'Fiscal Deficit' and 'Revenue Deficit' of the Government?",
        "stem_ta": "மத்திய நிதிக் கணக்குகள் மீதான தனது தணிக்கையில், அரசாங்கத்தின் 'நிதிப் பற்றாக்குறை' மற்றும் 'வருவாய்ப் பற்றாக்குறையை' சி.ஏ.ஜி எவ்வாறு ஆய்வு செய்கிறார்?",
        "options": [
            ("Verifies whether borrowed funds were used for productive capital creation rather than consumption, and assesses off-budget borrowings", "கடன் வாங்கப்பட்ட நிதி நுகர்வுக்குப் பதிலாக ஆக்கப்பூர்வ மூலதன உருவாக்கத்திற்குப் பயன்பட்டதா என்பதைச் சரிபார்க்கிறார் மற்றும் பட்ஜெட்டுக்கு புறம்பான கடன்களைக் கணக்கிடுகிறார்"),
            ("Declares the country bankrupt whenever fiscal deficit exceeds 3%", "நிதிப் பற்றாக்குறை 3%-ஐத் தாண்டும் போதெல்லாம் நாட்டை திவாலானதாக அறிவிக்கிறார்"),
            ("Mandates that the Government cannot borrow money under any circumstances", "எந்த சூழ்நிலையிலும் அரசாங்கம் கடன் வாங்க முடியாது என்று கட்டளையிடுகிறார்"),
            ("Directs the printing of unlimited paper currency by private commercial firms", "தனியார் வணிக நிறுவனங்கள் மூலம் வரம்பற்ற காகிதப் பணத்தை அச்சிட உத்தரவிடுகிறார்")
        ],
        "exp_en": "The CAG examines whether fiscal deficits meet statutory FRBM targets, highlights 'off-budget borrowings' (borrowings through public sector entities not shown in the budget deficit), and checks debt sustainability.",
        "exp_ta": "நிதிப் பற்றாக்குறை FRBM சட்ட இலக்குகளுக்கு உட்பட்டுள்ளதா என்பதை CAG ஆராய்கிறார், பட்ஜெட்டில் காட்டப்படாத 'பட்ஜெட்டுக்கு புறம்பான கடன்களை' (Off-budget borrowings) வெளிச்சமிட்டுக் காட்டுகிறார்.",
        "tip_en": "Off-budget borrowings: CAG reports were instrumental in bringing off-budget debt into formal government balance sheets.",
        "tip_ta": "பட்ஜெட்டுக்கு புறம்பான கடன்களை முறையான அரசு நிதிநிலைக் குறிப்பில் கொண்டுவருவதில் சி.ஏ.ஜி அறிக்கைகள் முக்கியப் பங்காற்றின.",
        "fact_en": "Transparency in debt reporting ensures Parliament gets an accurate picture of total sovereign liabilities.",
        "fact_ta": "கடன் அறிக்கையிடலில் உள்ள வெளிப்படைத்தன்மை நாடாளுமன்றம் மொத்த அரசுப் பொறுப்புகளைத் துல்லியமாக அறிய உதவுகிறது."
    },
    # 37
    {
        "subtopic": "Audit of Direct Taxes",
        "stem_en": "What is the primary scope of the CAG's audit of Direct Taxes (Income Tax and Corporation Tax)?",
        "stem_ta": "நேர்முக வரிகள் (வருமான வரி மற்றும் கார்ப்பரேட் வரி) மீதான சி.ஏ.ஜி தணிக்கையின் முதன்மை நோக்கம் என்ன?",
        "options": [
            ("Checking whether tax assessments comply with the Income Tax Act, exemptions correctly granted, and arithmetic calculations accurate", "வரி மதிப்பீடுகள் வருமான வரிச் சட்டத்திற்கு உட்பட்டுள்ளதா, விலக்குகள் சரியாக அளிக்கப்பட்டுள்ளனவா மற்றும் கணக்கீடுகள் துல்லியமாக உள்ளதா என்பதைச் சரிபார்த்தல்"),
            ("Directly interrogating individual citizens inside their homes", "தனிநபர் குடிமக்களை அவர்களின் வீடுகளில் நேரடியாக விசாரித்தல்"),
            ("Abolishing income tax for all government employees", "அனைத்து அரசு ஊழியர்களுக்கும் வருமான வரியை ரத்து செய்தல்"),
            ("Setting the monthly gold price for wealth tax calculations", "செல்வ வரி கணக்கீட்டிற்கான மாதாந்திர தங்க விலையை நிர்ணயித்தல்")
        ],
        "exp_en": "The CAG examines assessment files to detect tax under-assessments, incorrect deductions, irregular allowances, or mathematical errors by assessing officers, recovering thousands of crores for the public purse.",
        "exp_ta": "வரி மதிப்பீட்டு அதிகாரிகளின் தவறான வரி மதிப்பீடுகள், முறையற்ற கழிவுகள் மற்றும் கணிதப் பிழைகளைக் கண்டறிந்து, அரசு கருவூலத்திற்கு ஆயிரக்கணக்கான கோடிகளை மீட்க சி.ஏ.ஜி தணிக்கை உதவுகிறது.",
        "tip_en": "Audit of Direct Taxes checks compliance with statutory tax codes; CAG audit paras often lead to retrospective recoveries.",
        "tip_ta": "நேர்முக வரிகள் தணிக்கை சட்டப்பூர்வ வரி விதிகளைச் சரிபார்க்கிறது; CAG தணிக்கைக் குறிப்புகள் பலமுறை வரி வசூலுக்கு வழிவகுத்துள்ளன.",
        "fact_en": "Audit paras accepted by the Central Board of Direct Taxes (CBDT) result in demands raised against assessees.",
        "fact_ta": "நேரடி வரிகள் மத்திய வாரியம் (CBDT) ஏற்றுக்கொள்ளும் தணிக்கைக் குறிப்புகள் வரி செலுத்துவோர் மீது கூடுதல் வரி விதிப்புக்கு வழிவகுக்கின்றன."
    },
    # 38
    {
        "subtopic": "National Cleanliness / Swachh Bharat Audit",
        "stem_en": "In performance audits of the Swachh Bharat Mission, what did the CAG's field verification primarily evaluate?",
        "stem_ta": "தூய்மை இந்தியா இயக்கம் (Swachh Bharat Mission) மீதான செயல்திறன் தணிக்கைகளில், சி.ஏ.ஜி-யின் கள ஆய்வு எதனை முதன்மையாக மதிப்பீடு செய்தது?",
        "options": [
            ("Actual physical existence, usability, water connectivity, and sustainability of constructed household toilets", "கட்டப்பட்ட கழிப்பறைகளின் உண்மையான இருப்பு, பயன்பாடு, தண்ணீர் இணைப்பு மற்றும் அவற்றின் தொடர் பயன்பாட்டுத் தன்மை"),
            ("Solely counting the number of billboards erected along highways", "நெடுஞ்சாலைகளில் வைக்கப்பட்ட விளம்பரப் பலகைகளின் எண்ணிக்கையை மட்டும் எண்ணுதல்"),
            ("Directly manufacturing ceramic sanitary tiles in audit offices", "தணிக்கை அலுவலகங்களில் பீங்கான் ஓடுகளை நேரடியாக உற்பத்தி செய்தல்"),
            ("Banning all private soap manufacturing corporations", "அனைத்து தனியார் சோப்பு உற்பத்தி நிறுவனங்களையும் தடை செய்தல்")
        ],
        "exp_en": "CAG performance audits cross-verify administrative Open Defecation Free (ODF) claims with physical field samples to check whether toilets actually exist, have water supply, and are actively used by beneficiaries.",
        "exp_ta": "திறந்தவெளிக் கழிப்பிடமற்ற (ODF) நிர்வாகக் கூற்றுக்களை கள ஆய்வுகள் மூலம் சி.ஏ.ஜி தணிக்கை சரிபார்த்து, கழிப்பறைகள் உண்மையில் உள்ளதா, தண்ணீர் வசதி உள்ளதா மற்றும் பயன்படுத்தப்படுகிறதா என்பதை ஆராய்கிறது.",
        "tip_en": "Field verification audits prevent paper compliance and verify grassroots ground reality.",
        "tip_ta": "கள ஆய்வுத் தணிக்கைகள் வெறும் காகித அளவிலான அறிக்கைகளைத் தடுத்து தரைமட்ட உண்மையை உறுதி செய்கின்றன.",
        "fact_en": "CAG's performance audit on rural sanitation revealed substantial gaps between reported data and field reality.",
        "fact_ta": "ஊரகத் தூய்மை மீதான சி.ஏ.ஜி அறிக்கை நிர்வாகத் தரவுகளுக்கும் கள உண்மைக்கும் இடையிலான இடைவெளிகளை வெளிப்படுத்தியது."
    },
    # 39
    {
        "subtopic": "Audit of Central Autonomous Educational Institutions",
        "stem_en": "Under what authority does the CAG audit central universities, IITs, IIMs, and AIIMS?",
        "stem_ta": "எந்த அதிகாரத்தின் கீழ் மத்தியப் பல்கலைக்கழகங்கள், ஐ.ஐ.டி (IIT), ஐ.ஐ.எம் (IIM) மற்றும் எய்ம்ஸ் (AIIMS) ஆகியவற்றை சி.ஏ.ஜி தணிக்கை செய்கிறார்?",
        "options": [
            ("As statutory bodies substantially funded by Central Government grants under Section 14/19(2) of the 1971 Act", "1971 சட்டத்தின் பிரிவு 14/19(2)-ன் கீழ் மத்திய அரசு மானியங்களால் கணிசமாக நிதியளிக்கப்படும் சட்டப்பூர்வ அமைப்புகளாக"),
            ("Under the University Grants Commission Act as an educational chancellor", "பல்கலைக்கழக மானியக் குழுச் சட்டத்தின் கீழ் கல்வி வேந்தராக"),
            ("As private commercial tutoring centres under the Trade Marks Act", "வணிக முத்திரைகள் சட்டத்தின் கீழ் தனியார் பயிற்சி மையங்களாக"),
            ("Only during semester examinations to check question papers", "வினாத்தாள்களைச் சரிபார்க்க செமஸ்டர் தேர்வுகளின் போது மட்டுமே")
        ],
        "exp_en": "Central educational institutions like IITs, IIMs, and Central Universities receive massive grants from the Consolidated Fund of India; their annual accounts are audited and separate audit reports (SARs) tabled in Parliament by CAG.",
        "exp_ta": "ஐ.ஐ.டி, ஐ.ஐ.எம் மற்றும் மத்தியப் பல்கலைக்கழகங்கள் திரட்டப்பட்ட நிதியிலிருந்து பெரும் மானியங்களைப் பெறுகின்றன; அவற்றின் கணக்குகள் தணிக்கை செய்யப்பட்டு தனித் தணிக்கை அறிக்கைகள் (SARs) நாடாளுமன்றத்தில் வைக்கப்படுகின்றன.",
        "tip_en": "Separate Audit Reports (SARs) of autonomous educational institutions are presented to Parliament annually.",
        "tip_ta": "தன்னாட்சி கல்வி நிறுவனங்களின் தனித் தணிக்கை அறிக்கைகள் (SARs) ஆண்டுதோறும் நாடாளுமன்றத்தில் சமர்ப்பிக்கப்படுகின்றன.",
        "fact_en": "CAG audits of IITs frequently review research grant utilization, campus infrastructure delays, and patent filings.",
        "fact_ta": "ஐ.ஐ.டி-க்கள் மீதான தணிக்கைகள் ஆராய்ச்சி மானியப் பயன்பாடு மற்றும் உள்கட்டமைப்புத் தாமதங்களை ஆய்வு செய்கின்றன."
    },
    # 40
    {
        "subtopic": "Right to Formulate Audit Regulations",
        "stem_en": "Under Section 23 of the CAG's (DPC) Act 1971, what regulation-making power is vested in the Comptroller and Auditor General?",
        "stem_ta": "1971-ம் ஆண்டின் CAG சட்டத்தின் பிரிவு 23-ன் கீழ், தலைமைக் கணக்குத் தணிக்கையாளருக்கு வழங்கப்பட்டுள்ள ஒழுங்குமுறை உருவாக்கும் அதிகாரம் என்ன?",
        "options": [
            ("Power to make regulations for conducting audit, specifying standards, and governing audit methodology", "தணிக்கை நடத்துதல், தரநிலைகளைக் குறிப்பிடுதல் மற்றும் தணிக்கை முறைகளை நிர்வகிப்பதற்கான ஒழுங்குமுறைகளை உருவாக்கும் அதிகாரம்"),
            ("Power to declare war against foreign nations violating financial treaties", "நிதி ஒப்பந்தங்களை மீறும் வெளிநாடுகளுக்கு எதிராகப் போர் பிரகடனம் செய்யும் அதிகாரம்"),
            ("Authority to amend the fundamental rights in Part III of the Constitution", "அரசியலமைப்பின் பகுதி III-ல் உள்ள அடிப்படை உரிமைகளைத் திருத்தும் அதிகாரம்"),
            ("Power to dissolve the State Legislative Assemblies at will", "தனது விருப்பப்படி மாநில சட்டமன்றப் பேரவைகளைக் கலைக்கும் அதிகாரம்")
        ],
        "exp_en": "Section 23 of the 1971 Act empowers the CAG to make regulations for carrying into effect the provisions of the Act regarding the scope, extent, and methodology of audits.",
        "exp_ta": "1971 சட்டத்தின் பிரிவு 23, தணிக்கையின் நோக்கம், வரம்பு மற்றும் முறைகள் தொடர்பான சட்டத்தின் விதிகளைச் செயல்படுத்த ஒழுங்குமுறைகளை உருவாக்க CAG-க்கு அதிகாரம் அளிக்கிறது.",
        "tip_en": "Section 23 = Regulations on Audit and Accounts formulated by the CAG himself (Regulations on Audit and Accounts, 2007).",
        "tip_ta": "பிரிவு 23 = சி.ஏ.ஜி-யால் நேரடியாக வகுக்கப்படும் தணிக்கை மற்றும் கணக்குகள் ஒழுங்குமுறைகள் (2007 ஒழுங்குமுறைகள்).",
        "fact_en": "In 2007, the CAG notified comprehensive 'Regulations on Audit and Accounts' exercising power under Section 23.",
        "fact_ta": "2007-ல் பிரிவு 23-ன் அதிகாரத்தைப் பயன்படுத்தி 'தணிக்கை மற்றும் கணக்குகள் ஒழுங்குமுறைகளை' சி.ஏ.ஜி அறிவித்தார்."
    },
    # 41
    {
        "subtopic": "Audit of National Highways Authority",
        "stem_en": "Under which framework is the National Highways Authority of India (NHAI) audited by the CAG?",
        "stem_ta": "இந்திய தேசிய நெடுஞ்சாலைகள் ஆணையம் (NHAI) எந்தக் கட்டமைப்பின் கீழ் சி.ஏ.ஜி-யால் தணிக்கை செய்யப்படுகிறது?",
        "options": [
            ("Section 19(2) as a statutory corporation, with dedicated audit of toll revenue, concession agreements, and highway quality", "பிரிவு 19(2)-ன் கீழ் சட்டப்பூர்வ கழகமாக, சுங்கக் கட்டண வருவாய், சலுகை ஒப்பந்தங்கள் மற்றும் சாலைத் தரம் ஆகியவற்றின் பிரத்யேகத் தணிக்கையுடன்"),
            ("As a private automobile driving school under state motor vehicle rules", "மோட்டார் வாகன விதிகளின் கீழ் இயங்கும் தனியார் ஓட்டுநர் பள்ளியாக"),
            ("NHAI is completely exempt from all audit scrutiny forever", "NHAI அனைத்து தணிக்கை ஆய்விலிருந்தும் எப்போதும் முழு விலக்கு பெற்றது"),
            ("Audited only by international tourist associations", "சர்வதேச சுற்றுலாப் பயணிகள் சங்கங்களால் மட்டுமே தணிக்கை செய்யப்படுகிறது")
        ],
        "exp_en": "NHAI is a statutory corporation established under the NHAI Act 1988. The CAG audits its annual accounts, highway construction contracts, toll fee collections, and debt servicing.",
        "exp_ta": "NHAI என்பது 1988-ம் ஆண்டின் NHAI சட்டத்தின் கீழ் நிறுவப்பட்ட ஒரு சட்டப்பூர்வ அமைப்பாகும். இதன் வருடாந்திரக் கணக்குகள், சாலை ஒப்பந்தங்கள், சுங்கக் கட்டண வசூல் ஆகியவற்றை CAG தணிக்கை செய்கிறார்.",
        "tip_en": "NHAI audit reports highlight cost escalations, toll plaza revenue leakages, and delayed project completions.",
        "tip_ta": "NHAI தணிக்கை அறிக்கைகள் திட்டச் செலவு உயர்வு, சுங்கச்சாவடி வருவாய்க் கசிவு மற்றும் திட்டத் தாமதங்களைச் சுட்டிக்காட்டுகின்றன.",
        "fact_en": "The 2023 CAG performance audit of NHAI projects under Bharatmala Pariyojana generated widespread parliamentary discussion.",
        "fact_ta": "பாரத்மாலா பரியோஜனா திட்டத்தின் கீழ் NHAI மீதான 2023 சி.ஏ.ஜி தணிக்கை அறிக்கை நாடாளுமன்றத்தில் பெரும் விவாதத்தை ஏற்படுத்தியது."
    },
    # 42
    {
        "subtopic": "Role in Special Purpose Vehicles (SPVs)",
        "stem_en": "When governments create Special Purpose Vehicles (SPVs) for smart cities, metro rails, or infrastructure corridors, what gives the CAG audit jurisdiction?",
        "stem_ta": "ஸ்மார்ட் சிட்டிகள், மெட்ரோ ரயில் அல்லது உள்கட்டமைப்பு வழித்தடங்களுக்காக அரசாங்கம் சிறப்பு நோக்க நிறுவனங்களை (SPVs) உருவாக்கும் போது, சி.ஏ.ஜி-க்கு தணிக்கை அதிகாரத்தை வழங்குவது எது?",
        "options": [
            ("Government shareholding exceeding 51% (Sec 19) or substantial financial assistance through grants/loans (Sec 14)", "51%-க்கு அதிகமான அரசுப் பங்குகள் (பிரிவு 19) அல்லது மானியங்கள்/கடன்கள் மூலம் கணிசமான நிதி உதவி (பிரிவு 14)"),
            ("An oral invitation from the local traffic police inspector", "உள்ளூர் போக்குவரத்து காவல் ஆய்வாளரின் வாய்மொழி அழைப்பு"),
            ("The presence of foreign advertising posters on metro pillars", "மெட்ரோ தூண்களில் வெளிநாட்டு விளம்பர சுவரொட்டிகள் இருப்பது"),
            ("SPVs are completely immune from all public audit under all laws", "அனைத்து சட்டங்களின் கீழும் SPV நிறுவனங்கள் அனைத்து பொதுத் தணிக்கையிலிருந்தும் முழு விலக்கு பெற்றவை")
        ],
        "exp_en": "If an SPV is incorporated as a government company (where Union/State holds >= 51% shares), it is audited under Section 19 of the CAG Act. If established as a society/trust, substantial funding triggers Section 14.",
        "exp_ta": "ஒரு SPV அரசு நிறுவனமாகப் பதிவு செய்யப்பட்டால் (51% அல்லது அதற்கு மேற்பட்ட பங்குகள்) பிரிவு 19-ன் கீழும், சங்கம் அல்லது அறக்கட்டளையாக இருந்தால் கணிசமான நிதி உதவி மூலம் பிரிவு 14-ன் கீழும் CAG தணிக்கைக்கு உட்படுகிறது.",
        "tip_en": "Executive cannot escape CAG audit simply by routing public funds through Special Purpose Vehicles (SPVs).",
        "tip_ta": "சிறப்பு நோக்க நிறுவனங்கள் (SPVs) மூலம் பொது நிதியைச் செலவிடுவதன் மூலம் மட்டும் சி.ஏ.ஜி தணிக்கையிலிருந்து தப்ப முடியாது.",
        "fact_en": "Metro rail corporations (like Chennai Metro Rail Limited - CMRL) are joint ventures audited by the CAG.",
        "fact_ta": "சென்னை மெட்ரோ ரயில் நிறுவனம் (CMRL) போன்ற கூட்டு நிறுவனங்கள் சி.ஏ.ஜி-யால் தணிக்கை செய்யப்படுகின்றன."
    },
    # 43
    {
        "subtopic": "CAG Audit of Defence Pensions",
        "stem_en": "Which specialized office under the CAG audits defence pensions, military salaries, and ordnance factory expenditures?",
        "stem_ta": "பாதுகாப்புப் படைகளின் ஓய்வூதியம், ராணுவச் சம்பளம் மற்றும் ஆயுதத் தொழிற்சாலைகளின் செலவினங்களைத் தணிக்கை செய்யும் சி.ஏ.ஜி-யின் கீழான சிறப்பு அலுவலகம் எது?",
        "options": [
            ("Director General of Audit (Defence Services)", "பாதுகாப்புப் பணிகள் தணிக்கைத் தலைமை இயக்குநர் (DGADS)"),
            ("Reserve Bank Currency Vault Directorate", "ரிசர்வ் வங்கி நாணயப் பெட்டக இயக்குநரகம்"),
            ("Central Vigilance Commission Anti-Terror Cell", "மத்திய ஊழல் கண்காணிப்பு ஆணைய பயங்கரவாத எதிர்ப்புப் பிரிவு"),
            ("Supreme Court Military Appeal Registry", "உச்ச நீதிமன்ற ராணுவ மேல்முறையீட்டுப் பதிவகம்")
        ],
        "exp_en": "The Director General of Audit, Defence Services (DGADS), an officer of the IA&AS operating under the CAG, oversees the specialized audit of defence services, pensions, and equipment.",
        "exp_ta": "சி.ஏ.ஜி-யின் கீழ் செயல்படும் IA&AS அதிகாரியான பாதுகாப்புப் பணிகள் தணிக்கைத் தலைமை இயக்குநர் (DGADS), பாதுகாப்புப் படைகள், ஓய்வூதியங்கள் மற்றும் தளவாடங்களின் சிறப்புத் தணிக்கையை மேற்பார்வையிடுகிறார்.",
        "tip_en": "DGADS audits army, navy, air force, and defence research establishments (DRDO).",
        "tip_ta": "DGADS தரைப்படை, கடற்படை, விமானப்படை மற்றும் பாதுகாப்பு ஆராய்ச்சி அமைப்புகளை (DRDO) தணிக்கை செய்கிறது.",
        "fact_en": "Defence audit reports cover over 15% of the central government's total expenditure.",
        "fact_ta": "பாதுகாப்புத் தணிக்கை அறிக்கைகள் மத்திய அரசின் மொத்த செலவினத்தில் 15%-க்கும் அதிகமான பகுதியைக் கையாள்கின்றன."
    },
    # 44
    {
        "subtopic": "CAG and Cooperative Societies",
        "stem_en": "Are private cooperative societies that receive no government funding subject to direct audit by the CAG?",
        "stem_ta": "அரசு நிதி உதவி எதனையும் பெறாத தனியார் கூட்டுறவுச் சங்கங்கள் சி.ஏ.ஜி-யின் நேரடித் தணிக்கைக்கு உட்பட்டவையா?",
        "options": [
            ("No, purely private cooperatives without government funding or statutory request under Section 20 are outside the CAG's scope", "இல்லை, அரசு நிதி அல்லது பிரிவு 20-ன் கீழான கோரிக்கை இல்லாத தூய தனியார் கூட்டுறவுச் சங்கங்கள் CAG-ன் தணிக்கை வரம்பிற்கு அப்பாற்பட்டவை"),
            ("Yes, the CAG audits every private shop, club, and cooperative society in India", "ஆம், இந்தியாவில் உள்ள ஒவ்வொரு தனியார் கடை, சங்கம் மற்றும் கூட்டுறவுச் சங்கத்தை CAG தணிக்கை செய்கிறார்"),
            ("Yes, under Article 19(1)(c) of the Constitution directly", "ஆம், அரசியலமைப்பின் சரத்து 19(1)(c)-ன் கீழ் நேரடியாக"),
            ("Yes, if ordered by the local police sub-inspector", "ஆம், உள்ளூர் காவல் சார்பு ஆய்வாளர் உத்தரவிட்டால் செய்யலாம்")
        ],
        "exp_en": "Purely private cooperatives without state equity, grants, or government guarantees fall under the State Registrar of Cooperative Societies, not the CAG, unless Section 20 is invoked.",
        "exp_ta": "அரசுப் பங்கு, மானியம் அல்லது அரசு உத்தரவாதம் இல்லாத தனியார் கூட்டுறவுச் சங்கங்கள் மாநிலக் கூட்டுறவுச் சங்கப் பதிவாளரின் கீழ் வருகின்றனவே தவிர, பிரிவு 20 பயன்படுத்தப்படாவிட்டால் CAG வரம்பில் வராது.",
        "tip_en": "CAG audits PUBLIC money; private entities with no government funds are outside his purview.",
        "tip_ta": "CAG பொது நிதியை மட்டுமே தணிக்கை செய்கிறார்; அரசு நிதி இல்லாத தனியார் அமைப்புகள் அவரது வரம்பிற்கு அப்பாற்பட்டவை.",
        "fact_en": "However, multi-state cooperatives receiving government subsidies can be audited for those specific subsidies.",
        "fact_ta": "எனினும் அரசு மானியம் பெறும் பல மாநிலக் கூட்டுறவுச் சங்கங்கள் அந்த குறிப்பிட்ட மானியங்களுக்காகத் தணிக்கை செய்யப்படலாம்."
    },
    # 45
    {
        "subtopic": "CAG Audit of Direct Taxes Code",
        "stem_en": "What is the constitutional significance of the CAG's audit of tax exemptions and concessions granted by the Ministry of Finance?",
        "stem_ta": "நிதி அமைச்சகத்தால் வழங்கப்படும் வரி விலக்குகள் மற்றும் சலுகைகள் மீதான சி.ஏ.ஜி தணிக்கையின் அரசியலமைப்பு முக்கியத்துவம் என்ன?",
        "options": [
            ("Ensures that tax exemptions are authorized by parliamentary law and do not result in arbitrary revenue forgone", "வரி விலக்குகள் நாடாளுமன்றச் சட்டத்தால் அங்கீகரிக்கப்பட்டவை என்பதையும் தன்னிச்சையான வரி வருவாய் இழப்பிற்கு வழிவகுக்கவில்லை என்பதையும் உறுதி செய்கிறது"),
            ("Allows the CAG to seize properties of exempt non-profit trusts", "வரி விலக்கு பெற்ற தொண்டு நிறுவனங்களின் சொத்துக்களைப் பறிமுதல் செய்ய CAG-க்கு உதவுகிறது"),
            ("Directs all citizens to deposit 50% of their wealth into the CAG's account", "குடிமக்கள் தங்கள் சொத்தில் 50%-ஐ CAG கணக்கில் டெபாசிட் செய்ய கட்டளையிடுகிறது"),
            ("Abolishes all parliamentary power over tax legislations", "வரி சட்டங்கள் மீதான நாடாளுமன்றத்தின் அனைத்து அதிகாரங்களையும் ரத்து செய்கிறது")
        ],
        "exp_en": "Under Article 265 ('No tax shall be levied or collected except by authority of law'), the CAG examines whether tax exemptions grant unauthorized benefits that undermine tax equity and parliamentary control.",
        "exp_ta": "சரத்து 265-ன் கீழ் ('சட்டத்தின் அதிகாரமின்றி எந்த வரியும் விதிக்கப்படவோ வசூலிக்கப்படவோ கூடாது'), வரி விலக்குகள் நாடாளுமன்றக் கட்டுப்பாட்டை மீறி தன்னிச்சையான பலன்களை அளிக்கிறதா என்பதை CAG ஆராய்கிறார்.",
        "tip_en": "Article 265 + CAG Receipt Audit = Protection against illegal or arbitrary tax concessions.",
        "tip_ta": "சரத்து 265 + CAG வரவுத் தணிக்கை = சட்டவிரோத அல்லது தன்னிச்சையான வரிச் சலுகைகளுக்கு எதிரான பாதுகாப்பு.",
        "fact_en": "CAG reports on 'Revenue Forgone' regularly highlight the scale of corporate tax incentives in India.",
        "fact_ta": "இந்தியாவில் கார்ப்பரேட் வரிச் சலுகைகளின் அளவை சி.ஏ.ஜி-யின் 'விட்டுக்கொடுக்கப்பட்ட வருவாய்' (Revenue Forgone) அறிக்கைகள் தொடர்ந்து சுட்டிக்காட்டுகின்றன."
    },
    # 46
    {
        "subtopic": "Audit of Goods and Services Tax Network (GSTN)",
        "stem_en": "Why was the audit of the Goods and Services Tax Network (GSTN) special purpose vehicle considered a landmark development in CAG audit jurisprudence?",
        "stem_ta": "சரக்கு மற்றும் சேவை வரி நெட்வொர்க் (GSTN) மீதான தணிக்கை சி.ஏ.ஜி-யின் தணிக்கை வரலாற்றில் ஒரு மைல்கல் நிகழ்வாகக் கருதப்பட்டது ஏன்?",
        "options": [
            ("It established the principle that non-government SPVs managing core sovereign financial infrastructure are subject to CAG audit scrutiny", "இறையாண்மை நிதி உள்கட்டமைப்பை நிர்வகிக்கும் அரசு சாரா சிறப்பு நோக்க நிறுவனங்களும் (SPV) CAG தணிக்கைக்கு உட்பட்டவை என்ற கொள்கையை நிறுவியதால்"),
            ("It resulted in the immediate physical closure of all computerized servers in India", "இந்தியாவில் உள்ள அனைத்து கணினி சேவையகங்களையும் உடனடியாக மூட வழிவகுத்ததால்"),
            ("It made the CAG the permanent Chairman of the GST Council", "CAG-ஐ ஜிஎஸ்டி கவுன்சிலின் நிரந்தரத் தலைவராக மாற்றியதால்"),
            ("It replaced all indirect taxes with an ancient bartering system", "அனைத்து மறைமுக வரிகளையும் ஒழித்து பழங்கால பண்டமாற்று முறைக்கு மாற்றியதால்")
        ],
        "exp_en": "Although GSTN was originally set up as a non-government private company (51% private equity initially, later converted to 100% government), the CAG established jurisdiction to audit its IT architecture, data security, and settlement systems.",
        "exp_ta": "GSTN ஆரம்பத்தில் ஒரு தனியார் நிறுவனமாகத் தொடங்கப்பட்டாலும், அதன் தகவல் தொழில்நுட்பக் கட்டமைப்பு, தரவுப் பாதுகாப்பு மற்றும் வரித் தீர்வு அமைப்புகளைத் தணிக்கை செய்யும் அதிகாரத்தை CAG நிலைநாட்டினார்.",
        "tip_en": "Public data and sovereign taxation systems cannot be hidden behind corporate veil structures.",
        "tip_ta": "கார்ப்பரேட் நிறுவனக் கட்டமைப்புகளுக்குப் பின்னால் பொதுத் தரவுகளையோ இறையாண்மை வரி அமைப்புகளையோ மறைக்க முடியாது.",
        "fact_en": "GSTN was subsequently converted into a 100% government-owned company following public and parliamentary demands.",
        "fact_ta": "பொதுமக்கள் மற்றும் நாடாளுமன்ற கோரிக்கைகளைத் தொடர்ந்து GSTN பின்னர் 100% அரசுக்குச் சொந்தமான நிறுவனமாக மாற்றப்பட்டது."
    },
    # 47
    {
        "subtopic": "CAG and Monetary Policy Committee",
        "stem_en": "Does the Comptroller and Auditor General audit the interest-rate setting decisions of the Monetary Policy Committee (MPC) of the Reserve Bank of India?",
        "stem_ta": "இந்திய ரிசர்வ் வங்கியின் நாணயக் கொள்கைக் குழுவின் (MPC) வட்டி விகித நிர்ணய முடிவுகளை தலைமைக் கணக்குத் தணிக்கையாளர் தணிக்கை செய்கிறாரா?",
        "options": [
            ("No, monetary policy decisions are macroeconomic policy functions outside the audit scope of the CAG", "இல்லை, நாணயக் கொள்கை முடிவுகள் மேக்ரோ பொருளாதாரக் கொள்கைப் பணிகள் என்பதால் CAG தணிக்கை வரம்பிற்கு அப்பாற்பட்டவை"),
            ("Yes, the CAG personally fixes the repo rate and reverse repo rate every two months", "ஆம், இரண்டு மாதங்களுக்கு ஒருமுறை ரெப்போ மற்றும் ரிவர்ஸ் ரெப்போ விகிதங்களை CAG தனிப்பட்ட முறையில் நிர்ணயிக்கிறார்"),
            ("Yes, the CAG can veto any monetary policy resolution passed by the RBI Governor", "ஆம், ரிசர்வ் வங்கி ஆளுநர் நிறைவேற்றும் எந்தவொரு நாணயக் கொள்கைத் தீர்மானத்தையும் CAG ரத்து செய்யலாம்"),
            ("Only during leap years under Article 360", "சரத்து 360-ன் கீழ் லீப் ஆண்டுகளில் மட்டுமே")
        ],
        "exp_en": "The setting of the repo rate and monetary policy under the RBI Act is an independent central banking function. The CAG does not audit monetary policy or macroeconomic rate determinations.",
        "exp_ta": "ரிசர்வ் வங்கிச் சட்டத்தின் கீழ் நாணயக் கொள்கை மற்றும் ரெப்போ விகிதங்களை நிர்ணயிப்பது மத்திய வங்கியின் சுதந்திரமான பணியாகும். நாணயக் கொள்கை முடிவுகளை CAG தணிக்கை செய்வதில்லை.",
        "tip_en": "Fiscal policy and government spending = Audited by CAG. Monetary policy (RBI) = Outside CAG scope.",
        "tip_ta": "நிதிநிலை கொள்கை மற்றும் அரசு செலவினம் = CAG தணிக்கை உண்டு. நாணயக் கொள்கை (RBI) = CAG வரம்பிற்கு அப்பாற்பட்டது.",
        "fact_en": "Central bank independence in monetary decisions is respected worldwide.",
        "fact_ta": "நாணயக் கொள்கை முடிவுகளில் மத்திய வங்கியின் சுயாட்சி உலகம் முழுவதும் மதிக்கப்படுகிறது."
    },
    # 48
    {
        "subtopic": "Separate Audit Reports (SARs)",
        "stem_en": "What are 'Separate Audit Reports' (SARs) prepared by the Comptroller and Auditor General?",
        "stem_ta": "தலைமைக் கணக்குத் தணிக்கையாளரால் தயாரிக்கப்படும் 'தனித் தணிக்கை அறிக்கைகள்' (SARs) என்பவை யாவை?",
        "options": [
            ("Individual audit reports on autonomous bodies, authorities, and statutory corporations presented separately to Parliament or State Legislatures", "நாடாளுமன்றம் அல்லது மாநில சட்டமன்றங்களில் தனித்தனியாக வைக்கப்படும் தன்னாட்சி அமைப்புகள் மற்றும் கழகங்கள் மீதான தனித் தணிக்கை அறிக்கைகள்"),
            ("Secret personal diaries written by the CAG for his family", "சி.ஏ.ஜி தனது குடும்பத்திற்காக எழுதும் ரகசிய தனிப்பட்ட குறிப்புகள்"),
            ("Judicial bail orders issued to government accountants", "அரசு கணக்காளர்களுக்கு வழங்கப்படும் நீதித்துறை பிணை உத்தரவுகள்"),
            ("Commercial advertising brochures of public sector banks", "பொதுத்துறை வங்கிகளின் வணிக விளம்பர கையேடுகள்")
        ],
        "exp_en": "Separate Audit Reports (SARs) are comprehensive audit reports containing the audited annual statement of accounts along with the CAG's audit observations for individual statutory bodies and autonomous institutions.",
        "exp_ta": "தனித் தணிக்கை அறிக்கைகள் (SARs) என்பவை தனிப்பட்ட சட்டப்பூர்வ அமைப்புகள் மற்றும் தன்னாட்சி நிறுவனங்களின் தணிக்கை செய்யப்பட்ட கணக்குகள் மற்றும் CAG-யின் தணிக்கைக் கருத்துக்களைக் கொண்ட தனித்தனி அறிக்கைகளாகும்.",
        "tip_en": "SARs are placed on the table of Parliament alongside the annual report of the respective autonomous body.",
        "tip_ta": "சம்பந்தப்பட்ட தன்னாட்சி அமைப்பின் வருடாந்திர அறிக்கையுடன் SARs நாடாளுமன்றத்தின் மேசையில் வைக்கப்படுகின்றன.",
        "fact_en": "Hundreds of SARs are laid in Parliament annually, covering Port Trusts, regulatory commissions, and autonomous councils.",
        "fact_ta": "துறைமுகப் பொறுப்புக் கழகங்கள், ஒழுங்குமுறை ஆணையங்கள் ஆகியவற்றின் நூற்றுக்கணக்கான SAR-கள் ஆண்டுதோறும் நாடாளுமன்றத்தில் வைக்கப்படுகின்றன."
    },
    # 49
    {
        "subtopic": "Constitutional Amendment Impact",
        "stem_en": "How did the 42nd and 44th Constitutional Amendment Acts impact Article 150 of the Constitution concerning the form of accounts?",
        "stem_ta": "கணக்குகளின் படிவம் தொடர்பான அரசியலமைப்பின் சரத்து 150-ல் 42-வது மற்றும் 44-வது அரசியலமைப்புத் திருத்தச் சட்டங்கள் என்ன தாக்கத்தை ஏற்படுத்தின?",
        "options": [
            ("Restored the mandatory role of the CAG by specifying that the President prescribes the form 'on the advice of' the CAG", "குடியரசுத் தலைவர் CAG-ன் 'ஆலோசனையின் பேரில்' படிவத்தைப் பரிந்துரைப்பார் எனக் கூறி CAG-யின் கட்டாயப் பங்கை மீட்டெடுத்தன"),
            ("Abolished the CAG's advisory role completely and gave it to the Law Minister", "CAG-ன் ஆலோசனைப் பங்கை முற்றிலும் ஒழித்து சட்ட அமைச்சரிடம் ஒப்படைத்தன"),
            ("Ordered that all accounts must be written only in ancient Sanskrit", "அனைத்து கணக்குகளும் சமஸ்கிருதத்தில் மட்டுமே எழுதப்பட வேண்டும் என உத்தரவிட்டன"),
            ("Transferred Article 150 to the Ninth Schedule permanently", "சரத்து 150-ஐ ஒன்பதாவது அட்டவணைக்கு நிரந்தரமாக மாற்றின")
        ],
        "exp_en": "The 42nd Amendment had diluted Article 150 by substituting 'in consultation with' the CAG. The 44th Amendment in 1978 restored the phrasing 'on the advice of the Comptroller and Auditor-General of India', strengthening the CAG's authority.",
        "exp_ta": "42-வது திருத்தம் 'CAG-ன் கலந்தாலோசனையுடன்' என மாற்றி அதிகாரத்தைக் குறைத்தது. 1978-ல் 44-வது திருத்தம் மீண்டும் 'CAG-ன் ஆலோசனையின் பேரில்' என்று மாற்றி சி.ஏ.ஜி-யின் அதிகாரத்தை மீட்டெடுத்தது.",
        "tip_en": "44th Amendment (1978): Restored 'on the advice of the CAG' in Article 150.",
        "tip_ta": "44-வது திருத்தம் (1978): சரத்து 150-ல் 'CAG-ன் ஆலோசனையின் பேரில்' என்பதை மீட்டெடுத்தது.",
        "fact_en": "This wording ensures that the executive cannot prescribe account formats without the CAG's technical advice.",
        "fact_ta": "இந்த வாசகம் சி.ஏ.ஜி-யின் தொழில்நுட்ப ஆலோசனையின்றி நிர்வாகம் கணக்கு படிவங்களை மாற்ற முடியாது என்பதை உறுதி செய்கிறது."
    },
    # 50
    {
        "subtopic": "Comprehensive Constitutional Status",
        "stem_en": "Which of the following constitutional provisions most conclusively ensures that the Comptroller and Auditor General is completely independent of the executive government?",
        "stem_ta": "தலைமைக் கணக்குத் தணிக்கையாளர் நிர்வாக அரசாங்கத்திடமிருந்து முற்றிலும் சுதந்திரமானவர் என்பதை பின்வரும் எந்த அரசியலமைப்பு விதி மிகத் தீர்மானமாக உறுதி செய்கிறது?",
        "options": [
            ("Security of tenure identical to an SC Judge, expenses charged on Consolidated Fund, and complete post-retirement government employment ban", "உச்ச நீதிமன்ற நீதிபதிக்கு இணையான பதவிப் பாதுகாப்பு, திரட்டப்பட்ட நிதியில் சார்ஜ் செய்யப்பட்ட செலவுகள் மற்றும் ஓய்வுக்குப் பிந்தைய அரசு வேலைவாய்ப்பிற்கான முழுத் தடை"),
            ("Right to participate as a cabinet minister in foreign treaty discussions", "வெளிநாட்டு ஒப்பந்த விவாதங்களில் அமைச்சரவை அமைச்சராகப் பங்கேற்கும் உரிமை"),
            ("Power to dissolve the Parliament in consultation with the Chief of Defence Staff", "முப்படைகளின் தலைமைத் தளபதியுடன் கலந்தாலோசித்து நாடாளுமன்றத்தைக் கலைக்கும் அதிகாரம்"),
            ("Authority to declare emergency under Article 352 in financial crisis", "நிதி நெருக்கடியில் சரத்து 352-ன் கீழ் அவசரநிலையைப் பிரகடனம் செய்யும் அதிகாரம்")
        ],
        "exp_en": "The triad of independence guarantees in Article 148: (1) Removal only like a Supreme Court judge, (2) Administrative expenses and salary charged on the Consolidated Fund (non-votable), and (3) Total ineligibility for future office under Union or State governments.",
        "exp_ta": "சரத்து 148-ல் உள்ள மூன்று முக்கிய சுதந்திர உத்தரவாதங்கள்: (1) உச்ச நீதிமன்ற நீதிபதி போல மட்டுமே நீக்கப்படுதல், (2) செலவுகள் திரட்டப்பட்ட நிதியில் சார்ஜ் செய்யப்படுதல் (வாக்கெடுப்பற்றது), (3) ஓய்வுக்குப் பிறகு மத்திய/மாநில அரசுகளில் மேலும் எந்தப் பதவியும் வகிக்க முழுத் தடை.",
        "tip_en": "The three pillars of CAG independence: Removal like SC Judge (148(1)), Non-variation of salary (148(3)), and Post-retirement ban (148(4)).",
        "tip_ta": "CAG சுதந்திரத்தின் மூன்று தூண்கள்: SC நீதிபதி போல நீக்கம் (148(1)), ஊதியப் பாதுகாப்பு (148(3)), ஓய்வுக்குப் பிந்தைய அரசுப் பதவித் தடை (148(4)).",
        "fact_en": "These safeguards make the CAG accountable to Parliament and the public, never to the ruling executive.",
        "fact_ta": "இந்த பாதுகாப்புகள் சி.ஏ.ஜி ஆளும் நிர்வாகத்திற்கு அல்லாமல், நாடாளுமன்றத்திற்கும் பொதுமக்களுக்கும் மட்டுமே பொறுப்பானவராக இருப்பதை உறுதி செய்கின்றன."
    }
]

def build_questions():
    questions = []
    for i, item in enumerate(raw_medium_data):
        qid = f"CAG_M_{i+1:03d}"
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
            tags=["polity", "comptroller_and_auditor_general", "medium", item["subtopic"].lower().replace(" ", "_")]
        )
        questions.append(q)
    return questions

if __name__ == "__main__":
    qs = build_questions()
    print(f"Generated {len(qs)} raw Medium questions for CAG.")
    
    balanced_qs = balance_question_keys(qs)
    
    out_path = os.path.join("data", "questions", "polity", "cag_medium.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(balanced_qs, f, ensure_ascii=False, indent=2)
        
    print(f"Saved balanced Medium MCQs to {out_path}")
    
    val = ContentValidator()
    report = val.validate_file(out_path, expected_count=50, expected_prefix="CAG_M_")
    print(f"Validation Report: {'PASS' if report.is_valid else 'FAIL'} | Total: {report.total_audited}")
    if not report.is_valid:
        for iss in report.issues[:10]:
            print(f"  Issue: {iss}")
    print(f"Key Distribution: {report.key_distribution}")
