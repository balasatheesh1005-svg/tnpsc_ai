# -*- coding: utf-8 -*-
"""
Build 25 Match the Following MCQs for CAG (Comptroller & Auditor General of India)
ID range: CAG_MF_001 to CAG_MF_025
Target key balance: 7 A, 6 B, 6 C, 6 D
"""

import json
import os
from cag_mcq_helper import make_cag_q
from tools.nova_content_engine.validator import ContentValidator

raw_match_data = [
    # 1
    {
        "subtopic": "Constitutional Articles",
        "intro_en": "Match List-I (Constitutional Articles) with List-II (Subject Matter relating to the CAG) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (அரசியலமைப்புச் சரத்துகள்) பட்டியல்-II உடன் (சி.ஏ.ஜி தொடர்பான பொருள்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": ["Article 148", "Article 149", "Article 150", "Article 151"],
        "list1_ta": ["சரத்து 148", "சரத்து 149", "சரத்து 150", "சரத்து 151"],
        "list2_en": [
            "Office, appointment, tenure, and removal of the CAG",
            "Duties and powers of the CAG prescribed by parliamentary law",
            "Form of accounts of the Union and States prescribed on CAG's advice",
            "Submission of CAG audit reports to the President and Governors"
        ],
        "list2_ta": [
            "சி.ஏ.ஜி அலுவலகம், நியமனம், பதவிக்காலம் மற்றும் பதவி நீக்கம்",
            "நாடாளுமன்ற சட்டத்தால் நிர்ணயிக்கப்படும் சி.ஏ.ஜியின் கடமைகள் மற்றும் அதிகாரங்கள்",
            "சி.ஏ.ஜி ஆலோசனையின் பேரில் மத்திய, மாநில கணக்குகளின் படிவம் நிர்ணயம்",
            "குடியரசுத் தலைவர் மற்றும் ஆளுநர்களிடம் சி.ஏ.ஜி தணிக்கை அறிக்கைகளை சமர்ப்பித்தல்"
        ],
        # mapping: a->1, b->2, c->3, d->4
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "Article 148 establishes the office and independence of the CAG; Article 149 prescribes duties and powers; Article 150 governs the form of accounts; Article 151 provides for the tabling of audit reports.",
        "exp_ta": "சரத்து 148 சி.ஏ.ஜி அலுவலகத்தை நிறுவுகிறது; சரத்து 149 பணிகள் மற்றும் அதிகாரங்களை வகுக்கிறது; சரத்து 150 கணக்குப் படிவங்களை நிர்ணயிக்கிறது; சரத்து 151 தணிக்கை அறிக்கைகளை சமர்ப்பிக்க வகைசெய்கிறது.",
        "tip_en": "Memorize Articles 148-151 sequentially: Office -> Duties -> Form of Accounts -> Audit Reports.",
        "tip_ta": "சரத்துகள் 148-151 வரிசையை நினைவில் வையுங்கள்: பதவி -> கடமைகள் -> கணக்குப் படிவம் -> தணிக்கை அறிக்கை.",
        "fact_en": "Chapter V of Part V contains only these four pivotal articles.",
        "fact_ta": "பகுதி V, அத்தியாயம் V இந்த நான்கு முக்கிய சரத்துகளை மட்டுமே கொண்டுள்ளது."
    },
    # 2
    {
        "subtopic": "Sections of CAG (DPC) Act 1971",
        "intro_en": "Match List-I (Sections of the CAG Act 1971) with List-II (Statutory Mandate) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (1971 சி.ஏ.ஜி சட்டப் பிரிவுகள்) பட்டியல்-II உடன் (சட்டப்பூர்வ பணி) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": ["Section 13", "Section 14", "Section 15", "Section 16"],
        "list1_ta": ["பிரிவு 13", "பிரிவு 14", "பிரிவு 15", "பிரிவு 16"],
        "list2_en": [
            "Audit of all expenditure from the Consolidated Fund of India and States",
            "Audit of bodies substantially financed by government grants/loans",
            "Audit of procedures relating to grants or loans for specific purposes",
            "Audit of all tax and non-tax receipts payable to Consolidated Funds"
        ],
        "list2_ta": [
            "மத்திய மற்றும் மாநில திரட்டப்பட்ட நிதியிலிருந்து செய்யப்படும் அனைத்து செலவினத் தணிக்கை",
            "அரசு மானியங்கள்/கடன்கள் மூலம் கணிசமாக நிதியளிக்கப்படும் அமைப்புகளின் தணிக்கை",
            "குறிப்பிட்ட நோக்கத்திற்கான மானியங்கள் அல்லது கடன்கள் தொடர்பான நடைமுறைத் தணிக்கை",
            "திரட்டப்பட்ட நிதிகளுக்குச் சேர வேண்டிய அனைத்து வரி மற்றும் வரி அல்லாத வரவுத் தணிக்கை"
        ],
        # mapping: a->1, b->2, c->3, d->4
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "Section 13 mandates expenditure audit; Section 14 mandates audit of substantially funded autonomous bodies; Section 15 governs specific grants/loans; Section 16 governs receipts audit.",
        "exp_ta": "பிரிவு 13 செலவினத் தணிக்கையையும்; பிரிவு 14 தன்னாட்சி அமைப்புகளின் தணிக்கையையும்; பிரிவு 15 குறிப்பிட்ட மானியங்கள் தணிக்கையையும்; பிரிவு 16 வரவுத் தணிக்கையையும் நிர்ணயிக்கிறது.",
        "tip_en": "Sections 13 to 16 form the operational audit core of the 1971 Act.",
        "tip_ta": "பிரிவுகள் 13 முதல் 16 வரை 1971 சட்டத்தின் முக்கிய தணிக்கைப் பிரிவுகளாகும்.",
        "fact_en": "Section 16 enables auditing the assessment, levy, and collection of GST and Income Tax.",
        "fact_ta": "பிரிவு 16 ஜி.எஸ்.டி மற்றும் வருமான வரி மதிப்பீடு, வசூல் ஆகியவற்றைத் தணிக்கை செய்ய வழிவகுக்கிறது."
    },
    # 3
    {
        "subtopic": "Further Sections of CAG Act 1971",
        "intro_en": "Match List-I (Sections of the CAG Act 1971) with List-II (Functional Power) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (1971 சி.ஏ.ஜி சட்டப் பிரிவுகள்) பட்டியல்-II உடன் (செயல்பாட்டு அதிகாரம்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": ["Section 17", "Section 18", "Section 19", "Section 20"],
        "list1_ta": ["பிரிவு 17", "பிரிவு 18", "பிரிவு 19", "பிரிவு 20"],
        "list2_en": [
            "Audit of stores and stock in government departments",
            "Powers of inspection and requisition of official books and records",
            "Audit of Government Companies and statutory corporations",
            "Audit of other authorities/bodies entrusted by President or Governor"
        ],
        "list2_ta": [
            "அரசுத் துறைகளில் உள்ள சரக்குகள் மற்றும் இருப்புக் கணக்குகள் மீதான தணிக்கை",
            "அரசுப் புத்தகங்கள் மற்றும் ஆவணங்களை ஆய்வு செய்து கோரும் அதிகாரங்கள்",
            "அரசு நிறுவனங்கள் மற்றும் சட்டப்பூர்வ கழகங்களின் தணிக்கை",
            "குடியரசுத் தலைவர் அல்லது ஆளுநரால் ஒப்படைக்கப்படும் பிற அமைப்புகளின் தணிக்கை"
        ],
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "Section 17 governs stores and stock; Section 18 gives inspection and record requisition powers; Section 19 regulates government companies; Section 20 allows audit entrustment in public interest.",
        "exp_ta": "பிரிவு 17 சரக்குத் தணிக்கையையும்; பிரிவு 18 ஆவண ஆய்வு அதிகாரத்தையும்; பிரிவு 19 அரசு நிறுவனத் தணிக்கையையும்; பிரிவு 20 பொது நலன் கருதி பிற அமைப்புகளின் தணிக்கை ஒப்படைப்பையும் கையாள்கிறது.",
        "tip_en": "Section 18 is the legal bedrock ensuring audit access to official records.",
        "tip_ta": "பிரிவு 18 தணிக்கைக்கான ஆவண அணுகலை உறுதி செய்யும் சட்ட அடித்தளமாகும்.",
        "fact_en": "Section 20 requires prior consultation with the CAG before entrustment.",
        "fact_ta": "பிரிவு 20 தணிக்கையை ஒப்படைக்கும் முன் சி.ஏ.ஜியுடன் கலந்தாலோசிக்க வேண்டும் எனக் கூறுகிறது."
    },
    # 4
    {
        "subtopic": "Key Constitutional Articles on Financial Control",
        "intro_en": "Match List-I (Constitutional Article) with List-II (Financial Provision) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (அரசியலமைப்புச் சரத்து) பட்டியல்-II உடன் (நிதி விதிமுறை) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": ["Article 114", "Article 115", "Article 266", "Article 267"],
        "list1_ta": ["சரத்து 114", "சரத்து 115", "சரத்து 266", "சரத்து 267"],
        "list2_en": [
            "Appropriation Bills authorizing withdrawal of money from the Consolidated Fund",
            "Supplementary, additional, or excess grants regularized by Parliament",
            "Consolidated Funds and Public Accounts of India and the States",
            "Contingency Fund of India placed at the disposal of the President"
        ],
        "list2_ta": [
            "திரட்டப்பட்ட நிதியிலிருந்து பணம் எடுக்க அனுமதிக்கும் நிதி ஒதுக்கீட்டு மசோதாக்கள்",
            "நாடாளுமன்றத்தால் முறைப்படுத்தப்படும் கூடுதல் அல்லது மிகுதி மானியங்கள்",
            "இந்தியா மற்றும் மாநிலங்களின் திரட்டப்பட்ட நிதிகள் மற்றும் பொதுக் கணக்குகள்",
            "குடியரசுத் தலைவரின் வசம் வைக்கப்பட்டுள்ள இந்திய அவசரகால நிதி"
        ],
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "Article 114 deals with Appropriation Bills; Article 115 covers supplementary/excess grants (flagged by CAG); Article 266 establishes Consolidated Fund & Public Account; Article 267 establishes Contingency Fund.",
        "exp_ta": "சரத்து 114 நிதி ஒதுக்கீட்டு மசோதாக்களையும்; சரத்து 115 கூடுதல் மானியங்களையும்; சரத்து 266 திரட்டப்பட்ட நிதி மற்றும் பொதுக் கணக்கையும்; சரத்து 267 அவசரகால நிதியையும் நிறுவுகிறது.",
        "tip_en": "CAG's Appropriation audit directly enforces parliamentary limits under Article 114.",
        "tip_ta": "சி.ஏ.ஜியின் ஒதுக்கீட்டுத் தணிக்கை சரத்து 114-ன் கீழ் நாடாளுமன்ற வரம்புகளை நிலைநிறுத்துகிறது.",
        "fact_en": "Withdrawal from Consolidated Fund without an Appropriation Act violates Article 114(3).",
        "fact_ta": "ஒதுக்கீட்டுச் சட்டமின்றி திரட்டப்பட்ட நிதியிலிருந்து பணம் எடுப்பது சரத்து 114(3)-ஐ மீறுவதாகும்."
    },
    # 5
    {
        "subtopic": "Pioneering Indian CAGs",
        "intro_en": "Match List-I (Pioneering CAG of India) with List-II (Historic Contribution/Tenure) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (முன்னோடி இந்திய சி.ஏ.ஜி) பட்டியல்-II உடன் (வரலாற்றுப் பங்களிப்பு/பதவிக்காலம்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": ["V. Narahari Rao", "A.K. Chanda", "T.N. Chaturvedi", "Vinod Rai"],
        "list1_ta": ["வி. நரஹரி ராவ்", "ஏ.கே. சந்தா", "டி.என். சதுர்வேதி", "வினோத் ராய்"],
        "list2_en": [
            "First Indian CAG who established the institutional foundation of IA&AD (1948-1954)",
            "Second CAG who advocated performance auditing and separation of accounts (1954-1960)",
            "CAG who submitted the landmark Bofors Howitzer procurement audit report (1984-1990)",
            "CAG who spearheaded aggressive 2G spectrum and Coal allocation audits (2008-2013)"
        ],
        "list2_ta": [
            "IA&AD துறையின் நிறுவன அடித்தளத்தை அமைத்த முதல் இந்திய சி.ஏ.ஜி (1948-1954)",
            "செயல்திறன் தணிக்கை மற்றும் கணக்குப் பிரிப்பை ஆதரித்த இரண்டாவது சி.ஏ.ஜி (1954-1960)",
            "வரலாற்று சிறப்புமிக்க போஃபோர்ஸ் பீரங்கி கொள்முதல் தணிக்கை அறிக்கையை சமர்ப்பித்த சி.ஏ.ஜி (1984-1990)",
            "2G அலைக்கற்றை மற்றும் நிலக்கரி சுரங்க ஒதுக்கீடு தணிக்கைகளை முன்னெடுத்த சி.ஏ.ஜி (2008-2013)"
        ],
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "V. Narahari Rao set up modern IA&AD; A.K. Chanda developed early performance audit concepts; T.N. Chaturvedi authored the Bofors report; Vinod Rai transformed audit public communication in 2G/Coal audits.",
        "exp_ta": "வி. நரஹரி ராவ் IA&AD-ஐ அமைத்தார்; ஏ.கே. சந்தா செயல்திறன் தணிக்கைக் கருத்துக்களை உருவாக்கினார்; டி.என். சதுர்வேதி போஃபோர்ஸ் அறிக்கையைத் தந்தார்; வினோத் ராய் 2G மற்றும் நிலக்கரி தணிக்கைகளை முன்னெடுத்தார்.",
        "tip_en": "Rao = First CAG; Chanda = Second CAG; Chaturvedi = Bofors; Rai = 2G & Coal.",
        "tip_ta": "ராவ் = முதல் சி.ஏ.ஜி; சந்தா = இரண்டாவது சி.ஏ.ஜி; சதுர்வேதி = போஃபோர்ஸ்; ராய் = 2G & நிலக்கரி.",
        "fact_en": "Vinod Rai was awarded the Padma Bhushan in 2016.",
        "fact_ta": "வினோத் ராய்க்கு 2016-ல் பத்ம பூஷண் விருது வழங்கப்பட்டது."
    },
    # 6
    {
        "subtopic": "Types of Government Audit",
        "intro_en": "Match List-I (Type of Audit) with List-II (Core Focus and Methodology) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (தணிக்கை வகை) பட்டியல்-II உடன் (முக்கிய நோக்கம் மற்றும் வழிமுறை) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": ["Compliance/Regulatory Audit", "Financial Attest Audit", "Performance Audit", "Propriety Audit"],
        "list1_ta": ["விதிமுறை/இணக்கத் தணிக்கை", "நிதி உறுதிப்படுத்தல் தணிக்கை", "செயல்திறன் தணிக்கை", "விவேக/நாணயத் தணிக்கை"],
        "list2_en": [
            "Verifies adherence to statutory laws, rules, regulations, and budgetary sanctions",
            "Expresses an audit opinion on whether financial statements reflect a true and fair view",
            "Evaluates economy, efficiency, and effectiveness (3Es) of government programs",
            "Scrutinizes whether expenditure was prudent, wise, and economical beyond legal forms"
        ],
        "list2_ta": [
            "சட்டங்கள், விதிகள், ஒழுங்குமுறைகள் மற்றும் பட்ஜெட் அனுமதிகள் பின்பற்றப்படுவதை சரிபார்த்தல்",
            "நிதிநிலை அறிக்கைகள் உண்மையான மற்றும் நியாயமான பார்வையைத் தருகின்றனவா என தணிக்கைக் கருத்து அளித்தல்",
            "அரசுத் திட்டங்களின் சிக்கனம், செயல்திறன் மற்றும் செயலூக்கம் (3Es) ஆகியவற்றை மதிப்பீடு செய்தல்",
            "சட்ட வடிவங்களைத் தாண்டி பொதுச் செலவு விவேகமாகவும் சிக்கனமாகவும் செய்யப்பட்டதா என ஆராய்தல்"
        ],
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "Compliance audit checks legality; Financial audit certifies accounts; Performance audit evaluates the 3Es; Propriety audit assesses wisdom and avoidance of waste.",
        "exp_ta": "இணக்கத் தணிக்கை சட்ட விதிகளையும்; நிதித் தணிக்கை கணக்குகளின் உண்மையையும்; செயல்திறன் தணிக்கை 3Es திறனையும்; நாணயத் தணிக்கை விவேகம் மற்றும் சிக்கனத்தையும் சோதிக்கிறது.",
        "tip_en": "The four pillars of public audit: Compliance, Financial, Performance, and Propriety.",
        "tip_ta": "அரசு தணிக்கையின் நான்கு தூண்கள்: இணக்கம், நிதி, செயல்திறன் மற்றும் விவேகம்.",
        "fact_en": "Performance auditing is now the most widely analyzed category of CAG reports.",
        "fact_ta": "செயல்திறன் தணிக்கை தற்போது சி.ஏ.ஜி அறிக்கைகளில் மிகவும் பரவலாக விவாதிக்கப்படும் பிரிவாகும்."
    },
    # 7
    {
        "subtopic": "Specialized Audit Centres and Directorates",
        "intro_en": "Match List-I (Specialized Institutional Unit) with List-II (Headquarters/Mandate) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (சிறப்பு நிறுவன பிரிவு) பட்டியல்-II உடன் (தலைமையகம்/பணி) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": ["iCED", "CDMA", "NAPA", "iCISA"],
        "list1_ta": ["iCED", "CDMA", "NAPA", "iCISA"],
        "list2_en": [
            "Jaipur - International Centre for Environment Audit and Sustainable Development",
            "New Delhi - Centre for Data Management and Analytics utilizing Big Data & AI",
            "Shimla - National Academy of Audit and Accounts training IA&AS officers",
            "Noida - International Centre for Information Systems and Audit"
        ],
        "list2_ta": [
            "ஜெய்ப்பூர் - சுற்றுச்சூழல் தணிக்கை மற்றும் நிலையான வளர்ச்சிக்கான சர்வதேச மையம்",
            "புது தில்லி - பெருந்தரவு மற்றும் AI தணிக்கைக்கான தரவு மேலாண்மை மற்றும் பகுப்பாய்வு மையம்",
            "சிம்லா - IA&AS அதிகாரிகளுக்கு பயிற்சி அளிக்கும் தேசிய தணிக்கை மற்றும் கணக்கு அகாடமி",
            "நொய்டா - தகவல் அமைப்புகள் மற்றும் தணிக்கைக்கான சர்வதேச மையம்"
        ],
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "iCED is in Jaipur for environmental audit; CDMA is in New Delhi for data analytics; NAPA is in Shimla for civil service training; iCISA is in Noida for IT/IS audit training.",
        "exp_ta": "iCED ஜெய்ப்பூரில் சுற்றுச்சூழல் தணிக்கைக்காகவும்; CDMA தில்லியில் தரவு பகுப்பாய்விற்காகவும்; NAPA சிம்லாவில் IA&AS பயிற்சிக்காகவும்; iCISA நொய்டாவில் தகவல் தணிக்கைக்காகவும் இயங்குகின்றன.",
        "tip_en": "iCED: Jaipur; CDMA: Delhi; NAPA: Shimla; iCISA: Noida.",
        "tip_ta": "iCED: ஜெய்ப்பூர்; CDMA: தில்லி; NAPA: சிம்லா; iCISA: நொய்டா.",
        "fact_en": "iCISA is recognized by the UN as a premier training institution for global auditors.",
        "fact_ta": "iCISA சர்வதேச தணிக்கையாளர்களுக்கான முதன்மை பயிற்சி நிறுவனமாக ஐ.நாவால் அங்கீகரிக்கப்பட்டுள்ளது."
    },
    # 8
    {
        "subtopic": "Parliamentary Committees and Audit Interface",
        "intro_en": "Match List-I (Parliamentary Financial Committee) with List-II (Audit Role and Composition) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (நாடாளுமன்ற நிதிக் குழு) பட்டியல்-II உடன் (தணிக்கைப் பங்கு மற்றும் அமைப்பு) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": [
            "Public Accounts Committee (PAC)",
            "Committee on Public Undertakings (COPU)",
            "Estimates Committee",
            "Department-related Standing Committees (DRSCs)"
        ],
        "list1_ta": [
            "பொதுக் கணக்குக் குழு (PAC)",
            "பொதுத்துறை நிறுவனங்களுக்கான குழு (COPU)",
            "மதிப்பீட்டுக் குழு (Estimates Committee)",
            "துறைசார் நிலைக்குழுக்கள் (DRSCs)"
        ],
        "list2_en": [
            "22 members (15 LS + 7 RS) examining CAG's Appropriation and Finance accounts reports",
            "22 members (15 LS + 7 RS) examining CAG's commercial audit reports on PSUs",
            "30 members (all LS) examining budget policy economies with zero CAG guidance",
            "31 members examining Demands for Grants of specific ministries"
        ],
        "list2_ta": [
            "சி.ஏ.ஜியின் ஒதுக்கீடு மற்றும் நிதிக் கணக்கு அறிக்கைகளை ஆய்வு செய்யும் 22 உறுப்பினர்கள் (15 LS + 7 RS)",
            "பொதுத்துறை நிறுவனங்கள் மீதான சி.ஏ.ஜியின் வணிகத் தணிக்கை அறிக்கைகளை ஆய்வு செய்யும் 22 உறுப்பினர்கள் (15 LS + 7 RS)",
            "சி.ஏ.ஜி வழிகாட்டுதலின்றி பட்ஜெட் கொள்கை சிக்கனங்களை ஆய்வு செய்யும் 30 உறுப்பினர்கள் (அனைத்தும் LS)",
            "குறிப்பிட்ட அமைச்சகங்களின் மானியக் கோரிக்கைகளை ஆய்வு செய்யும் 31 உறுப்பினர்கள்"
        ],
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "PAC examines regular audit reports; COPU examines PSU audit reports; Estimates Committee deals with policy economies without CAG; DRSCs examine Demands for Grants.",
        "exp_ta": "PAC வழக்கமான தணிக்கை அறிக்கைகளையும்; COPU பொதுத்துறை அறிக்கைகளையும்; மதிப்பீட்டுக் குழு சி.ஏ.ஜி தொடர்பின்றி பட்ஜெட் சிக்கனங்களையும்; DRSC மானியக் கோரிக்கைகளையும் ஆராய்கின்றன.",
        "tip_en": "CAG assists PAC and COPU, but NOT Estimates Committee.",
        "tip_ta": "சி.ஏ.ஜி PAC மற்றும் COPU குழுக்களுக்கு உதவுகிறார்; மதிப்பீட்டுக் குழுவிற்கு அல்ல.",
        "fact_en": "Ministers cannot be elected to PAC, COPU, or the Estimates Committee.",
        "fact_ta": "அமைச்சர்கள் PAC, COPU அல்லது மதிப்பீட்டுக் குழுவில் உறுப்பினராகத் தேர்ந்தெடுக்கப்பட முடியாது."
    },
    # 9
    {
        "subtopic": "Audit Reports Submitted under Article 151",
        "intro_en": "Match List-I (CAG Audit Report Category) with List-II (Content and Subject Matter) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (சி.ஏ.ஜி தணிக்கை அறிக்கை வகை) பட்டியல்-II உடன் (உள்ளடக்கம் மற்றும் பொருள்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": [
            "Audit Report on Appropriation Accounts",
            "Audit Report on Finance Accounts",
            "Audit Report on Public Undertakings",
            "State Local Bodies Audit Report"
        ],
        "list1_ta": [
            "ஒதுக்கீட்டுக் கணக்குகள் மீதான தணிக்கை அறிக்கை",
            "நிதிக் கணக்குகள் மீதான தணிக்கை அறிக்கை",
            "பொதுத்துறை நிறுவனங்கள் மீதான தணிக்கை அறிக்கை",
            "மாநில உள்ளாட்சி அமைப்புகள் மீதான தணிக்கை அறிக்கை"
        ],
        "list2_en": [
            "Compares voted parliamentary budget appropriations with actual departmental expenditure",
            "Presents the overall financial health, annual revenue/capital receipts, and public debt",
            "Scrutinizes commercial performance, profitability, and investments of statutory PSUs",
            "Presents findings under Technical Guidance and Supervision for Panchayats and ULBs"
        ],
        "list2_ta": [
            "நாடாளுமன்றத்தால் வாக்களிக்கப்பட்ட பட்ஜெட் ஒதுக்கீடுகளுடன் உண்மையான துறை செலவினங்களை ஒப்பிடுகிறது",
            "ஒட்டுமொத்த நிதி நிலைமை, வருவாய்/மூலதன வரவுகள் மற்றும் பொதுக்கடனை முன்வைக்கிறது",
            "பொதுத்துறை நிறுவனங்களின் வணிகச் செயல்பாடு, லாபத்தன்மை மற்றும் முதலீடுகளை ஆய்வு செய்கிறது",
            "பஞ்சாயத்துகள் மற்றும் நகர்ப்புற உள்ளாட்சிகளுக்கான TGS வழிகாட்டுதலின் கீழ் கண்டுபிடிப்புகளை முன்வைக்கிறது"
        ],
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "Appropriation Report covers grant compliance; Finance Report covers balance sheet & debt; Public Undertakings Report covers PSUs; Local Bodies Report covers Panchayats/ULBs.",
        "exp_ta": "ஒதுக்கீட்டு அறிக்கை மானிய இணக்கத்தையும்; நிதி அறிக்கை இருப்புநிலை மற்றும் கடனையும்; பொதுத்துறை அறிக்கை நிறுவன செயல்பாட்டையும்; உள்ளாட்சி அறிக்கை பஞ்சாயத்து கணக்குகளையும் விவரிக்கிறது.",
        "tip_en": "Union CAG submits three mandatory reports: Appropriation, Finance, and Public Undertakings.",
        "tip_ta": "மத்திய அரசுக்கு சி.ஏ.ஜி மூன்று கட்டாய அறிக்கைகளை சமர்ப்பிக்கிறார்: ஒதுக்கீடு, நிதி, மற்றும் பொதுத்துறை.",
        "fact_en": "CAG's State audit reports are placed before State Legislatures under Article 151(2).",
        "fact_ta": "சரத்து 151(2)-ன் கீழ் சி.ஏ.ஜியின் மாநில தணிக்கை அறிக்கைகள் மாநில சட்டமன்றங்களில் சமர்ப்பிக்கப்படுகின்றன."
    },
    # 10
    {
        "subtopic": "International Audit Organizations",
        "intro_en": "Match List-I (International Audit Body) with List-II (Description and Function) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (சர்வதேச தணிக்கை அமைப்பு) பட்டியல்-II உடன் (விளக்கம் மற்றும் பணி) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": ["INTOSAI", "ASOSAI", "UN Board of Auditors", "ISSAI"],
        "list1_ta": ["INTOSAI", "ASOSAI", "ஐ.நா தணிக்கையாளர் வாரியம்", "ISSAI"],
        "list2_en": [
            "Global non-governmental umbrella organization of Supreme Audit Institutions",
            "Regional grouping of 48 Supreme Audit Institutions across the Asian continent",
            "Three-member external audit board appointed by UN General Assembly to audit UN entities",
            "Authoritative international professional standards framework for public sector auditing"
        ],
        "list2_ta": [
            "உச்ச தணிக்கை அமைப்புகளின் உலகளாவிய அரசு சாரா குடை அமைப்பு",
            "ஆசியக் கண்டம் முழுவதிலும் உள்ள 48 உச்ச தணிக்கை அமைப்புகளின் பிராந்தியக் கூட்டமைப்பு",
            "ஐ.நா அமைப்புகளைத் தணிக்கை செய்ய ஐ.நா பொதுச்சபையால் நியமிக்கப்படும் மூன்று உறுப்பினர்கள் கொண்ட வெளித் தணிக்கை வாரியம்",
            "பொதுத்துறை தணிக்கைக்கான அதிகாரப்பூர்வ சர்வதேச தொழில்முறை தரநிலைகள் கட்டமைப்பு"
        ],
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "INTOSAI is the global body; ASOSAI is the Asian regional group; UN Board of Auditors audits UN organs; ISSAI comprises the professional standards issued by INTOSAI.",
        "exp_ta": "INTOSAI என்பது உலகளாவிய அமைப்பு; ASOSAI என்பது ஆசியக் கூட்டமைப்பு; ஐ.நா தணிக்கை வாரியம் ஐ.நா நிறுவனங்களைத் தணிக்கை செய்கிறது; ISSAI என்பது INTOSAI-ன் தொழில்முறை தரநிலைகளாகும்.",
        "tip_en": "India is a founding leader in both INTOSAI and ASOSAI.",
        "tip_ta": "INTOSAI மற்றும் ASOSAI ஆகிய இரண்டிலுமே இந்தியா ஒரு நிறுவனத் தலைவராக உள்ளது.",
        "fact_en": "INTOSAI operates as an official consultative NGO to the United Nations Economic and Social Council (ECOSOC).",
        "fact_ta": "INTOSAI அமைப்பு ஐ.நா பொருளாதார மற்றும் சமூக சபையின் அதிகாரப்பூர்வ ஆலோசனை அமைப்பாக செயல்படுகிறது."
    },
    # 11
    {
        "subtopic": "Audit Jurisdiction Categories",
        "intro_en": "Match List-I (Entity Category) with List-II (CAG Audit Jurisdiction Scope) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (நிறுவன வகை) பட்டியல்-II உடன் (சி.ஏ.ஜி தணிக்கை அதிகார வரம்பு) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": [
            "Government Departments (Railways, Defence)",
            "Government Companies (BHEL, SAIL)",
            "Statutory Financial Corporations (RBI, LIC, SBI)",
            "Substantially Financed Autonomous Bodies (IITs, AIIMS)"
        ],
        "list1_ta": [
            "அரசுத் துறைகள் (ரயில்வே, பாதுகாப்பு)",
            "அரசு நிறுவனங்கள் (BHEL, SAIL)",
            "சட்டப்பூர்வ நிதி நிறுவனங்கள் (RBI, LIC, SBI)",
            "கணிசமாக நிதியளிக்கப்படும் தன்னாட்சி அமைப்புகள் (IIT, AIIMS)"
        ],
        "list2_en": [
            "Direct 100% statutory audit of receipts, disbursements, stores, and operations",
            "CAG appoints chartered accountants as statutory auditors and conducts supplementary audit",
            "Exclusively audited by independent private auditors with zero CAG audit involvement",
            "Direct audit of accounts under Section 14 with Separate Audit Reports (SARs)"
        ],
        "list2_ta": [
            "வரவுகள், செலவுகள், சரக்குகள் மற்றும் செயல்பாடுகள் மீதான நேரடி 100% சட்டப்பூர்வ தணிக்கை",
            "பட்டயக் கணக்காளர்களை நியமிப்பதுடன் சி.ஏ.ஜி துணைத் தணிக்கையை நடத்துதல்",
            "சி.ஏ.ஜி தலையீடின்றி முற்றிலும் தனியார் தணிக்கையாளர்களால் மட்டுமே தணிக்கை செய்யப்படுதல்",
            "பிரிவு 14-ன் கீழ் தனித் தணிக்கை அறிக்கைகளுடன் (SARs) நேரடி கணக்குத் தணிக்கை"
        ],
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "Departments are directly audited; Govt companies have chartered accountants appointed by CAG plus supplementary audit; RBI/LIC are exempt from CAG; Autonomous bodies are audited under Section 14.",
        "exp_ta": "அரசுத் துறைகள் நேரடியாகத் தணிக்கை செய்யப்படுகின்றன; அரசு நிறுவனங்களுக்கு பட்டயக் கணக்காளர்கள் + துணைத் தணிக்கை; RBI/LIC சி.ஏ.ஜி தணிக்கையிலிருந்து விலக்கு; தன்னாட்சி அமைப்புகள் பிரிவு 14-ன் கீழ் தணிக்கை.",
        "tip_en": "Exempted from CAG audit: RBI, SBI, LIC, FCI (partially private audit).",
        "tip_ta": "சி.ஏ.ஜி தணிக்கையிலிருந்து விலக்கு பெற்றவை: RBI, SBI, LIC.",
        "fact_en": "Private audit of financial institutions preserves commercial flexibility and confidentiality.",
        "fact_ta": "வங்கி நிறுவனங்களுக்கு விலக்கு அளிப்பது அவற்றின் வணிக ரகசியத்தைப் பாதுகாக்கிறது."
    },
    # 12
    {
        "subtopic": "Key Legal and Constitutional Phrases",
        "intro_en": "Match List-I (Constitutional/Legal Phrase) with List-II (Meaning and Application to CAG) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (அரசியலமைப்பு/சட்ட சொற்றொடர்) பட்டியல்-II உடன் (பொருள் மற்றும் சி.ஏ.ஜி பயன்பாடு) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": [
            "Warrant under hand and seal",
            "Charged on Consolidated Fund",
            "Ineligible for further office",
            "Ascertained and certified"
        ],
        "list1_ta": [
            "கையொப்பம் மற்றும் முத்திரையிட்ட ஆணை",
            "திரட்டப்பட்ட நிதியில் பொறுப்பாக்கப்பட்டது",
            "மறுபதவி வகிக்கத் தகுதியற்றவர்",
            "கணக்கிடப்பட்டு சான்றளிக்கப்பட்டது"
        ],
        "list2_en": [
            "Formal presidential instrument signifying supreme dignity of appointment under Article 148(1)",
            "Expenditure that is non-votable by Parliament under Article 148(6) protecting financial autonomy",
            "Absolute post-retirement disqualification under Article 148(4) preventing executive inducement",
            "Conclusive and final determination of net tax proceeds by CAG under Article 279"
        ],
        "list2_ta": [
            "சரத்து 148(1)-ன் கீழ் உயர் அரசியலமைப்பு அந்தஸ்தைக் குறிக்கும் குடியரசுத் தலைவரின் முறையான ஆணை",
            "நிதி சுதந்திரத்தைப் பாதுகாக்கும் சரத்து 148(6)-ன் கீழ் நாடாளுமன்ற வாக்கெடுப்பிற்கு உட்படாத செலவினம்",
            "நிர்வாகச் செல்வாக்கைத் தடுக்கும் சரத்து 148(4)-ன் கீழ் ஓய்வுக்குப் பிந்தைய முழுமையான தகுதி நீக்கம்",
            "சரத்து 279-ன் கீழ் சி.ஏ.ஜியால் நிகர வரி வருவாயை முடிவாகவும் இறுதியாகவும் தீர்மானித்தல்"
        ],
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "Warrant under hand and seal denotes dignity; Charged expenditure ensures financial independence; Post-retirement ban ensures impartiality; Net proceeds certification guarantees finality.",
        "exp_ta": "முத்திரையிட்ட ஆணை உயர் அந்தஸ்தைக் குறிக்கிறது; பொறுப்பாக்கப்பட்ட செலவு நிதி சுதந்திரத்தை அளிக்கிறது; மறுபதவித் தடை நடுநிலையை உறுதி செய்கிறது; நிகர வருவாய் சான்றிதழ் முடிவானது.",
        "tip_en": "These four legal phrases embody the constitutional independence of the CAG.",
        "tip_ta": "இந்த நான்கு சட்டச் சொற்றொடர்களும் சி.ஏ.ஜியின் அரசியலமைப்பு சுதந்திரத்தை வெளிப்படுத்துகின்றன.",
        "fact_en": "Dr. Ambedkar specifically framed these protections to place the CAG above executive temptation.",
        "fact_ta": "நிர்வாகத் தூண்டுதல்களுக்கு அப்பாற்பட்டு சி.ஏ.ஜி இயங்கவே டாக்டர் அம்பேத்கர் இப் பாதுகாப்புகளை வடிவமைத்தார்."
    },
    # 13
    {
        "subtopic": "21st Century CAGs of India and Portfolios",
        "intro_en": "Match List-I (CAG of India) with List-II (Pre-Appointment Civil Service Role) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (இந்திய சி.ஏ.ஜி) பட்டியல்-II உடன் (நியமனத்திற்கு முந்தைய குடிமைப் பணி பதவி) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": ["Vinod Rai", "Shashi Kant Sharma", "Rajiv Mehrishi", "G.C. Murmu"],
        "list1_ta": ["வினோத் ராய்", "சசி காந்த் சர்மா", "ராஜீவ் மெஹ்ரிஷி", "ஜி.சி. முர்மு"],
        "list2_en": [
            "Secretary, Financial Services, Union Ministry of Finance",
            "Defence Secretary, Union Ministry of Defence",
            "Union Home Secretary and Finance Secretary",
            "First Lieutenant Governor of Union Territory of Jammu and Kashmir"
        ],
        "list2_ta": [
            "மத்திய நிதி அமைச்சகத்தின் நிதிச் சேவைகள் துறைச் செயலாளர்",
            "மத்திய பாதுகாப்பு அமைச்சகத்தின் பாதுகாப்புச் செயலாளர்",
            "மத்திய உள்துறைச் செயலாளர் மற்றும் நிதிச் செயலாளர்",
            "ஜம்மு காஷ்மீர் ஒன்றியப் பிரதேசத்தின் முதல் துணைநிலை ஆளுநர்"
        ],
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "Vinod Rai was Financial Services Secretary; Shashi Kant Sharma was Defence Secretary; Rajiv Mehrishi was Home Secretary; G.C. Murmu was the first LG of J&K.",
        "exp_ta": "வினோத் ராய் நிதிச் சேவை செயலாளராகவும்; சசி காந்த் சர்மா பாதுகாப்புச் செயலாளராகவும்; ராஜீவ் மெஹ்ரிஷி உள்துறை செயலாளராகவும்; ஜி.சி. முர்மு ஜம்மு காஷ்மீரின் முதல் துணைநிலை ஆளுநராகவும் பணியாற்றினர்.",
        "tip_en": "Most modern CAGs were senior IAS officers heading critical Union ministries before appointment.",
        "tip_ta": "பெரும்பாலான நவீன சி.ஏ.ஜிக்கள் நியமனத்திற்கு முன் மூத்த ஐ.ஏ.எஸ் அதிகாரிகளாகப் பணியாற்றினர்.",
        "fact_en": "Shashi Kant Sharma's appointment as CAG was challenged in court over conflict of interest with past defence deals.",
        "fact_ta": "கடந்த கால பாதுகாப்பு ஒப்பந்தங்கள் தொடர்பான நலன் முரண்பாடு காரணமாக சசி காந்த் சர்மா நியமனம் நீதிமன்றத்தில் சவாலுக்கு உட்படுத்தப்பட்டது."
    },
    # 14
    {
        "subtopic": "INTOSAI Declarations and Themes",
        "intro_en": "Match List-I (International Audit Declaration) with List-II (Core Theme and Year) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (சர்வதேச தணிக்கைப் பிரகடனம்) பட்டியல்-II உடன் (முக்கிய நோக்கம் மற்றும் ஆண்டு) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": [
            "Lima Declaration (1977)",
            "Mexico Declaration (2007)",
            "Beijing Declaration (2013)",
            "Moscow Declaration (2019)"
        ],
        "list1_ta": [
            "லிமா பிரகடனம் (1977)",
            "மெக்ஸிகோ பிரகடனம் (2007)",
            "பெய்ஜிங் பிரகடனம் (2013)",
            "மாஸ்கோ பிரகடனம் (2019)"
        ],
        "list2_en": [
            "Magna Carta of public audit establishing financial and operational autonomy of SAIs",
            "Institutionalizing eight core principles of Supreme Audit Institution independence",
            "Promoting good governance and national sustainable development through public audit",
            "Leveraging Big Data, Artificial Intelligence, and data analytics in modern auditing"
        ],
        "list2_ta": [
            "தணிக்கை அமைப்புகளின் நிதி மற்றும் செயல்பாட்டு சுயாட்சியை நிறுவிய பொது தணிக்கையின் மகாசாசனம்",
            "உச்ச தணிக்கை அமைப்புகளின் சுதந்திரத்திற்கான எட்டு அடிப்படைக் கொள்கைகளை முறைப்படுத்துதல்",
            "பொது தணிக்கை மூலம் நல்லாட்சி மற்றும் நிலையான தேசிய வளர்ச்சியை ஊக்குவித்தல்",
            "நவீன தணிக்கையில் பெருந்தரவு, செயற்கை நுண்ணறிவு மற்றும் தரவுப் பகுப்பாய்வைப் பயன்படுத்துதல்"
        ],
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "Lima = Magna Carta of audit autonomy; Mexico = 8 principles of SAI independence; Beijing = Good governance; Moscow = AI and Big Data in audit.",
        "exp_ta": "லிமா = தணிக்கை சுயாட்சியின் மகாசாசனம்; மெக்ஸிகோ = தணிக்கை சுதந்திரத்தின் 8 கொள்கைகள்; பெய்ஜிங் = நல்லாட்சி; மாஸ்கோ = AI மற்றும் பெருந்தரவு தணிக்கை.",
        "tip_en": "Lima (1977) and Mexico (2007) are the two most cited declarations on auditor independence.",
        "tip_ta": "லிமா (1977) மற்றும் மெக்ஸிகோ (2007) தணிக்கை சுதந்திரம் குறித்து அதிகம் குறிப்பிடப்படும் பிரகடனங்களாகும்.",
        "fact_en": "The UN General Assembly endorsed both Lima and Mexico declarations via formal resolutions.",
        "fact_ta": "ஐ.நா பொதுச்சபை முறையான தீர்மானங்கள் மூலம் இவ்விரு பிரகடனங்களையும் அங்கீகரித்துள்ளது."
    },
    # 15
    {
        "subtopic": "CAG Audit Paragraph Lifecycle",
        "intro_en": "Match List-I (Audit Document Stage) with List-II (Definition and Process) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (தணிக்கை ஆவணக் கட்டம்) பட்டியல்-II உடன் (விளக்கம் மற்றும் செயல்முறை) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": [
            "Audit Query / Memo",
            "Half Margin Memorandum",
            "Draft Audit Paragraph",
            "Action Taken Note (ATN)"
        ],
        "list1_ta": [
            "தணிக்கை வினா / குறிப்பு (Audit Query)",
            "அரை ஓரக் குறிப்பாணை (Half Margin Memo)",
            "வரைவு தணிக்கைப் பத்தி (Draft Paragraph)",
            "நடவடிக்கை குறிப்பு (Action Taken Note)"
        ],
        "list2_en": [
            "Initial observation issued during field audit seeking factual verification and departmental records",
            "Formal written memo requiring point-by-point explanation from the audited entity",
            "Consolidated vetted audit finding forwarded to Ministry Secretary for formal response",
            "Departmental reply submitted to PAC detailing remedial action taken on CAG audit findings"
        ],
        "list2_ta": [
            "உண்மைச் சரிபார்ப்பு மற்றும் ஆவணங்களைக் கோரி கள ஆய்வின் போது அனுப்பப்படும் ஆரம்பக் குறிப்பு",
            "தணிக்கை செய்யப்படும் துறையிடமிருந்து புள்ளி வாரியாக விளக்கம் கோரும் முறையான எழுத்துப்பூர்வ குறிப்பாணை",
            "அமைச்சகச் செயலாளருக்கு முறையான பதிலுக்காக அனுப்பப்படும் ஒருங்கிணைந்த வரைவு தணிக்கைக் கண்டுபிடிப்பு",
            "சி.ஏ.ஜி கண்டுபிடிப்புகள் மீது எடுக்கப்பட்ட சீர்திருத்த நடவடிக்கைகளை விவரித்து PAC-க்கு அளிக்கப்படும் துறைசார் பதில்"
        ],
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "Audit query is the first field query; Half margin is formal memo; Draft paragraph is vetted report sent to Secretary; ATN is executive action reported to PAC.",
        "exp_ta": "தணிக்கை வினா என்பது முதல் களக் கேள்வி; அரை ஓரக் குறிப்பாணை என்பது முறையான குறிப்பு; வரைவுப் பத்தி என்பது செயலாளருக்கு அனுப்பப்படும் அறிக்கை; ATN என்பது PAC-க்கு நிர்வாகம் அளிக்கும் நடவடிக்கைக் குறிப்பு.",
        "tip_en": "Audit lifecycle: Query -> Half Margin -> Draft Paragraph -> Audit Report -> ATN.",
        "tip_ta": "தணிக்கை சுழற்சி: வினா -> அரை ஓரக் குறிப்பு -> வரைவுப் பத்தி -> தணிக்கை அறிக்கை -> ATN.",
        "fact_en": "Audit paragraphs are included in the final report only after considering the Ministry's reply.",
        "fact_ta": "அமைச்சகத்தின் பதிலைப் பரிசீலித்த பிறகே இறுதி அறிக்கையில் தணிக்கைப் பத்திகள் சேர்க்கப்படுகின்றன."
    },
    # 16
    {
        "subtopic": "Government Funds under the Constitution",
        "intro_en": "Match List-I (Constitutional Fund) with List-II (Constitutional Provision and Operational Custody) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (அரசியலமைப்பு நிதி) பட்டியல்-II உடன் (அரசியலமைப்பு விதி மற்றும் நிர்வாகப் பொறுப்பு) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": [
            "Consolidated Fund of India",
            "Contingency Fund of India",
            "Public Account of India",
            "State Consolidated Fund"
        ],
        "list1_ta": [
            "இந்தியத் திரட்டப்பட்ட நிதி",
            "இந்திய அவசரகால நிதி",
            "இந்தியப் பொதுக் கணக்கு",
            "மாநிலத் திரட்டப்பட்ட நிதி"
        ],
        "list2_en": [
            "Article 266(1) - All revenues, loans, and recoveries received by the Government of India",
            "Article 267(1) - Held by the Finance Secretary on behalf of the President for unforeseen expenses",
            "Article 266(2) - Provident funds, small savings, and judicial deposits held in trust",
            "Article 266(1) - All revenues received by a State Government audited by State AGs"
        ],
        "list2_ta": [
            "சரத்து 266(1) - இந்திய அரசால் பெறப்படும் அனைத்து வருவாய்கள், கடன்கள் மற்றும் வசூல்கள்",
            "சரத்து 267(1) - எதிர்பாராத செலவுகளுக்காக குடியரசுத் தலைவரின் சார்பில் நிதிச் செயலாளரால் நிர்வகிக்கப்படுவது",
            "சரத்து 266(2) - அரசு வசம் அறக்கட்டளைப் பொறுப்பில் வைக்கப்படும் வருங்கால வைப்பு நிதி, சிறு சேமிப்புகள்",
            "சரத்து 266(1) - மாநில அரசு பெறும் அனைத்து வருவாய்களும்; மாநில AG-களால் தணிக்கை செய்யப்படுவது"
        ],
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "Consolidated Fund = Article 266(1); Contingency Fund = Article 267(1); Public Account = Article 266(2); State Consolidated Fund = Article 266(1) for States.",
        "exp_ta": "திரட்டப்பட்ட நிதி = சரத்து 266(1); அவசரகால நிதி = சரத்து 267(1); பொதுக் கணக்கு = சரத்து 266(2); மாநிலத் திரட்டப்பட்ட நிதி = மாநிலங்களுக்கான சரத்து 266(1).",
        "tip_en": "Withdrawals: Consolidated Fund requires parliamentary vote; Contingency Fund requires executive order + recoupment.",
        "tip_ta": "திரட்டப்பட்ட நிதிக்கு நாடாளுமன்ற வாக்கெடுப்பு தேவை; அவசரகால நிதிக்கு குடியரசுத் தலைவர் உத்தரவு போதுமானது.",
        "fact_en": "All three funds are fully subject to audit by the CAG under Section 13.",
        "fact_ta": "மூன்று நிதிகளுமே பிரிவு 13-ன் கீழ் சி.ஏ.ஜியின் முழுமையான தணிக்கைக்கு உட்பட்டவை."
    },
    # 17
    {
        "subtopic": "Historic PAC Reports Driven by Audit Findings",
        "intro_en": "Match List-I (Historic Financial Controversy) with List-II (Audit Finding and Core Subject) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (வரலாற்று நிதி சர்ச்சை) பட்டியல்-II உடன் (தணிக்கைக் கண்டுபிடிப்பு மற்றும் முக்கிய பொருள்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": [
            "Jeep Scandal (1948-51)",
            "Mundhra LIC Affair (1957)",
            "Bofors Howitzer Audit (1989)",
            "2G Spectrum Allocation (2010)"
        ],
        "list1_ta": [
            "ஜீப் ஊழல் (1948-51)",
            "முந்த்ரா எல்.ஐ.சி விவகாரம் (1957)",
            "போஃபோர்ஸ் பீரங்கி தணிக்கை (1989)",
            "2G அலைக்கற்றை ஒதுக்கீடு (2010)"
        ],
        "list2_en": [
            "First major financial irregularity in independent India involving UK defence jeep procurement",
            "Improper investment of public life insurance funds into sinking private corporate equities",
            "Evaluation of gun trials, cost escalation, and commission payments to middlemen",
            "Computation of presumptive loss of Rs. 1.76 lakh crore due to non-auction of telecom spectrum"
        ],
        "list2_ta": [
            "பிரிட்டனில் ராணுவ ஜீப் கொள்முதல் தொடர்பாக சுதந்திர இந்தியாவில் நிகழ்ந்த முதல் பெரிய நிதி முறைகேடு",
            "நலிவடைந்த தனியார் நிறுவனப் பங்குகளில் பொது ஆயுள் காப்பீட்டு நிதியை முறையற்ற முறையில் முதலீடு செய்தல்",
            "துப்பாக்கி சோதனைகள், செலவு அதிகரிப்பு மற்றும் இடைத்தரகர்களுக்கு தரகுத் தொகை வழங்கியதை மதிப்பீடு செய்தல்",
            "அலைக்கற்றை ஏலம் விடப்படாததால் ஏற்பட்ட ரூ. 1.76 லட்சம் கோடி உத்தேச இழப்பீட்டுக் கணக்கீடு"
        ],
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "Jeep scandal involved defence vehicles; Mundhra involved fraudulent LIC investments; Bofors involved artillery trials and middlemen; 2G involved presumptive loss from non-transparent spectrum allocation.",
        "exp_ta": "ஜீப் விவகாரம் ராணுவ வாகனங்களையும்; முந்த்ரா முறையற்ற எல்.ஐ.சி முதலீடுகளையும்; போஃபோர்ஸ் பீரங்கி சோதனைகள் மற்றும் கமிஷன்களையும்; 2G அலைக்கற்றை உத்தேச இழப்பையும் வெளிப்படுத்தின.",
        "tip_en": "These four landmark audits shaped Indian administrative law and anti-corruption jurisprudence.",
        "tip_ta": "இந்த நான்கு முக்கிய தணிக்கைகளும் இந்திய நிர்வாகச் சட்டம் மற்றும் ஊழல் தடுப்புக் கோட்பாடுகளை வடிவமைத்தன.",
        "fact_en": "The Mundhra case led to the appointment of the M.C. Chagla Commission of Inquiry.",
        "fact_ta": "முந்த்ரா விவகாரம் நீதிபதி எம்.சி. சாக்லா விசாரணை ஆணையம் அமைக்க வழிவகுத்தது."
    },
    # 18
    {
        "subtopic": "Evolution of Auditing Cadres and Ranks",
        "intro_en": "Match List-I (IA&AD Official Designation) with List-II (Administrative Role and Station) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (IA&AD அலுவல் பதவி) பட்டியல்-II உடன் (நிர்வாகப் பங்கு மற்றும் பணி இடம்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": [
            "Deputy Comptroller and Auditor General (DA&CG)",
            "Principal Accountant General (PAG)",
            "Director General of Audit (Central)",
            "Senior Audit Officer (SAO)"
        ],
        "list1_ta": [
            "துணைத் தலைமைக் கணக்குத் தணிக்கையாளர் (DA&CG)",
            "முதன்மை கணக்குத் தலைவர் (PAG)",
            "தணிக்கை தலைமை இயக்குநர் (மத்திய)",
            "மூத்த தணிக்கை அதிகாரி (SAO)"
        ],
        "list2_en": [
            "Apex headquarters official overseeing operational wings (Commercial, Defence, States)",
            "Senior IA&AS officer heading Audit or Accounts & Entitlement in a State capital",
            "Senior officer heading specialized audit of central government departments and civil receipts",
            "Group 'B' Gazetted supervisory officer leading field inspection parties on the ground"
        ],
        "list2_ta": [
            "தலைமையகத்தில் வணிக, பாதுகாப்பு மற்றும் மாநிலப் பிரிவுகளை மேற்பார்வையிடும் உச்ச அதிகாரி",
            "மாநிலத் தலைநகரில் தணிக்கை அல்லது கணக்குகள் & உரிமைகளை வழிநடத்தும் மூத்த IA&AS அதிகாரி",
            "மத்திய அரசுத் துறைகள் மற்றும் வரவுகளைத் தணிக்கை செய்யும் மூத்த அதிகாரி",
            "கள ஆய்வுக் குழுக்களை வழிநடத்தும் குரூப் 'B' கெசட்டட் தணிக்கை மேற்பார்வை அதிகாரி"
        ],
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "Dy CAG assists CAG at apex headquarters; PAG heads state offices; DG Audit handles central civil audit; SAO is the frontline supervisory officer leading audit parties.",
        "exp_ta": "துணை சி.ஏ.ஜி தலைமையக உச்ச அதிகாரியாவார்; PAG மாநில அலுவலகத்திற்கு தலைமை தாங்குகிறார்; DG Audit மத்திய தணிக்கையைக் கவனிக்கிறார்; SAO கள ஆய்வுக் குழுக்களை நடத்துகிறார்.",
        "tip_en": "IA&AS officers are recruited through UPSC Civil Services; field staff through SSC CGL.",
        "tip_ta": "IA&AS அதிகாரிகள் UPSC மூலமாகவும்; களப் பணியாளர்கள் SSC CGL மூலமாகவும் தேர்ந்தெடுக்கப்படுகின்றனர்.",
        "fact_en": "The Principal Accountant General (Audit) is the primary constitutional audit authority in each State.",
        "fact_ta": "ஒவ்வொரு மாநிலத்திலும் முதன்மை கணக்குத் தலைவர் (தணிக்கை) முதன்மை தணிக்கை அதிகாரியாவார்."
    },
    # 19
    {
        "subtopic": "Specialized Audit Guidelines and Frameworks",
        "intro_en": "Match List-I (Audit Guideline / Manual) with List-II (Subject Focus and Application) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (தணிக்கை வழிகாட்டுதல் / கையேடு) பட்டியல்-II உடன் (பொருள் நோக்கம் மற்றும் பயன்பாடு) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": [
            "Performance Audit Guidelines",
            "Compliance Audit Guidelines",
            "Revenue Audit Manual",
            "Environment Audit Guidelines"
        ],
        "list1_ta": [
            "செயல்திறன் தணிக்கை வழிகாட்டுதல்கள்",
            "இணக்கத் தணிக்கை வழிகாட்டுதல்கள்",
            "வருவாய் தணிக்கைக் கையேடு",
            "சுற்றுச்சூழல் தணிக்கை வழிகாட்டுதல்கள்"
        ],
        "list2_en": [
            "Establishes methodologies for assessing the 3Es: Economy, Efficiency, and Effectiveness",
            "Guides auditors in determining whether activities follow legal authorities and rules",
            "Specialized instructions for auditing GST, Customs, Income Tax, and Non-Tax revenues",
            "Standards developed via iCED Jaipur for auditing ecological and sustainable projects"
        ],
        "list2_ta": [
            "சிக்கனம், செயல்திறன் மற்றும் செயலூக்கம் (3Es) ஆகியவற்றை மதிப்பிடுவதற்கான வழிமுறைகளை நிறுவுதல்",
            "செயல்பாடுகள் சட்ட விதிகள் மற்றும் அதிகாரங்களைப் பின்பற்றுகின்றனவா என்பதை நிர்ணயிக்க வழிகாட்டுதல்",
            "ஜி.எஸ்.டி, சுங்கம், வருமான வரி மற்றும் வரி அல்லாத வருவாய்களைத் தணிக்கை செய்வதற்கான சிறப்பு அறிவுறுத்தல்கள்",
            "சுற்றுச்சூழல் திட்டங்களைத் தணிக்கை செய்ய ஜெய்ப்பூர் iCED மூலம் உருவாக்கப்பட்ட தரநிலைகள்"
        ],
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "Performance guidelines govern 3Es; Compliance guidelines govern legal regularity; Revenue manual governs tax audits; Environment guidelines govern green audit.",
        "exp_ta": "செயல்திறன் வழிகாட்டுதல் 3Es திறனையும்; இணக்க வழிகாட்டுதல் சட்ட விதிகளையும்; வருவாய் கையேடு வரிகளையும்; சுற்றுச்சூழல் வழிகாட்டுதல் பசுமைத் தணிக்கையையும் வழிநடத்துகின்றன.",
        "tip_en": "These manuals operationalize the broad principles set out in Section 23 Regulations.",
        "tip_ta": "இந்த கையேடுகள் பிரிவு 23 ஒழுங்குமுறைகளின் அடிப்படைக் கொள்கைகளை நடைமுறைப்படுத்துகின்றன.",
        "fact_en": "Audit manuals are revised periodically to incorporate international ISSAI standards.",
        "fact_ta": "சர்வதேச ISSAI தரநிலைகளை இணைக்க தணிக்கை கையேடுகள் அவ்வப்போது திருத்தப்படுகின்றன."
    },
    # 20
    {
        "subtopic": "Comparison of Global Auditor Models",
        "intro_en": "Match List-I (Country) with List-II (Institutional Audit Model and Designation) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (நாடு) பட்டியல்-II உடன் (நிறுவன தணிக்கை மாதிரி மற்றும் பதவிப் பெயர்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": ["India", "United Kingdom", "United States", "France"],
        "list1_ta": ["இந்தியா", "பிரிட்டன்", "அமெரிக்கா", "பிரான்ஸ்"],
        "list2_en": [
            "Comptroller and Auditor General - Independent single-member authority with ex-post audit remit",
            "Comptroller and Auditor General - Officer of the House of Commons with ex-ante exchequer control",
            "Comptroller General - Head of Government Accountability Office (GAO), an arm of Congress",
            "Cour des Comptes - Judicial audit court with powers to impose fines and penalize accountants"
        ],
        "list2_ta": [
            "தலைமைக் கணக்குத் தணிக்கையாளர் - செலவுக்குப் பிந்தைய தணிக்கை கொண்ட சுயாதீன ஒற்றை உறுப்பினர் அதிகாரி",
            "தலைமைக் கணக்குத் தணிக்கையாளர் - கருவூலப் பண வழங்கல் முன் கட்டுப்பாடு கொண்ட காமன்ஸ் சபை அதிகாரி",
            "கம்ப்ரோலர் ஜெனரல் - காங்கிரசின் ஒரு பிரிவான அரசுப் பொறுப்புடைமை அலுவலகத்தின் (GAO) தலைவர்",
            "Cour des Comptes - அதிகாரிகளுக்கு அபராதம் மற்றும் தண்டனை விதிக்கும் நீதித்துறை தணிக்கை நீதிமன்றம்"
        ],
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "India uses Westminster single-member audit without ex-ante control; UK has true ex-ante control; USA has GAO under Congress; France has the judicial Cour des Comptes.",
        "exp_ta": "இந்தியா முன் கட்டுப்பாடற்ற ஒற்றை உறுப்பினர் மாதிரியைக் கொண்டுள்ளது; பிரிட்டன் முன் அனுமதி கட்டுப்பாட்டைக் கொண்டுள்ளது; அமெரிக்கா GAO அமைப்பைக் கொண்டுள்ளது; பிரான்ஸ் தணிக்கை நீதிமன்ற முறையைக் கொண்டுள்ளது.",
        "tip_en": "Global audit systems: Westminster (India, UK), Congressional (USA), Judicial/Napoleonic (France).",
        "tip_ta": "உலகளாவிய தணிக்கை முறைகள்: வெஸ்ட்மின்ஸ்டர் (இந்தியா, UK), நாடாளுமன்ற முறை (USA), நீதித்துறை மாதிரி (பிரான்ஸ்).",
        "fact_en": "French Cour des Comptes magistrates possess judicial status.",
        "fact_ta": "பிரெஞ்சு தணிக்கை நீதிமன்ற நடுவர்கள் நீதித்துறை அந்தஸ்தைப் பெற்றுள்ளனர்."
    },
    # 21
    {
        "subtopic": "CAG Audit Entitlements and Pensions in States",
        "intro_en": "Match List-I (Function in State Accounts) with List-II (Designated Authority / Cadre) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (மாநில கணக்குகளில் உள்ள பணி) பட்டியல்-II உடன் (நியமிக்கப்பட்ட அதிகாரி / பிரிவு) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": [
            "Compilation of State Monthly Civil Accounts",
            "State Government Employee Pension Authorization",
            "State GPF Maintenance and Statements",
            "Primary Audit of Village Panchayats"
        ],
        "list1_ta": [
            "மாநில மாதாந்திர சிவில் கணக்குகளைத் தொகுத்தல்",
            "மாநில அரசு ஊழியர் ஓய்வூதிய அங்கீகாரம்",
            "மாநில GPF பராமரிப்பு மற்றும் வருடாந்திர அறிக்கை",
            "கிராம பஞ்சாயத்துகளின் முதன்மை நேரடித் தணிக்கை"
        ],
        "list2_en": [
            "Office of the Principal Accountant General (Accounts & Entitlement)",
            "State AG (A&E) verifying qualifying service and pension admissibility",
            "State AG (A&E) crediting monthly subscriptions and annual interest",
            "Director of Local Fund Audit (DLFA) under State Government"
        ],
        "list2_ta": [
            "முதன்மை கணக்குத் தலைவர் அலுவலகம் (கணக்குகள் மற்றும் உரிமைகள் - A&E)",
            "தகுதி வாய்ந்த சேவை மற்றும் ஓய்வூதியத்தை சரிபார்க்கும் மாநில AG (A&E)",
            "மாதாந்திர சந்தா மற்றும் வருடாந்திர வட்டியை வரவு வைக்கும் மாநில AG (A&E)",
            "மாநில அரசின் கீழ் இயங்கும் உள்ளாட்சி நிதி தணிக்கை இயக்குநர் (DLFA)"
        ],
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "State monthly accounts, pensions, and GPF are handled by AG (A&E) under the CAG; Primary local fund audit is handled by State DLFA with CAG providing TGS.",
        "exp_ta": "மாநில கணக்குகள், ஓய்வூதியம் மற்றும் GPF ஆகியவை சி.ஏ.ஜியின் கீழ் உள்ள AG (A&E) அலுவலகத்தால் நிர்வகிக்கப்படுகின்றன; உள்ளாட்சி முதன்மை தணிக்கை மாநில DLFA-வால் செய்யப்படுகிறது.",
        "tip_en": "AG (A&E) = Accounts and Entitlement; AG (Audit) = Audit.",
        "tip_ta": "AG (A&E) = கணக்குகள் மற்றும் உரிமைகள்; AG (Audit) = தணிக்கை.",
        "fact_en": "Tamil Nadu has separate AG (Audit-I), AG (Audit-II), and AG (A&E) offices in Chennai.",
        "fact_ta": "சென்னையில் AG (தணிக்கை-I), AG (தணிக்கை-II) மற்றும் AG (A&E) தனித்தனி அலுவலகங்கள் இயங்குகின்றன."
    },
    # 22
    {
        "subtopic": "21st Century Digital Audit Applications",
        "intro_en": "Match List-I (Digital Platform in Government) with List-II (CAG Audit Scrutiny Focus) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (அரசின் டிஜிட்டல் தளம்) பட்டியல்-II உடன் (சி.ஏ.ஜி தணிக்கை ஆய்வு நோக்கம்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": [
            "GSTN (GST Network)",
            "PFMS (Public Financial Management System)",
            "GeM (Government e-Marketplace)",
            "DBT (Direct Benefit Transfer)"
        ],
        "list1_ta": [
            "GSTN (ஜி.எஸ்.டி நெட்வொர்க்)",
            "PFMS (பொது நிதி மேலாண்மை அமைப்பு)",
            "GeM (அரசு மின்-சந்தை)",
            "DBT (நேரடிப் பணப் பரிமாற்றம்)"
        ],
        "list2_en": [
            "Verification of Input Tax Credit integrity and settlement of IGST between Centre and States",
            "Tracking real-time expenditure sanction, fund flow, and idle balances in bank accounts",
            "Scrutinizing procurement prices, tender fairness, and vendor cartelization in purchases",
            "Validating beneficiary Aadhaar seeding and detecting ghost beneficiaries in welfare schemes"
        ],
        "list2_ta": [
            "உள்ளீட்டு வரி வரவு நேர்மை மற்றும் மத்திய-மாநில IGST தீர்வை சரிபார்த்தல்",
            "நிகழ்நேர செலவின அனுமதி, நிதி ஓட்டம் மற்றும் வங்கிக் கணக்குகளில் முடங்கிய நிதியைக் கண்காணித்தல்",
            "கொள்முதல் விலைகள், டெண்டர் நியாயம் மற்றும் வணிகர்களின் கூட்டு விலையேற்றத்தை ஆய்வு செய்தல்",
            "நலத்திட்டங்களில் ஆதார் இணைப்பைச் சரிபார்த்து போலிப் பயனாளிகளைக் கண்டறிதல்"
        ],
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "GSTN audit tests tax credit settlement; PFMS tests fund utilization; GeM tests transparent procurement; DBT tests targeted welfare delivery without leakages.",
        "exp_ta": "GSTN வரித் தீர்வை சோதிக்கிறது; PFMS நிதிப் பயன்பாட்டை சோதிக்கிறது; GeM கொள்முதல் வெளிப்படைத்தன்மையை சோதிக்கிறது; DBT போலிப் பயனாளிகளைத் தடுக்கிறது.",
        "tip_en": "Big Data audit enables automated rule-based checks across 100% of digital transactions.",
        "tip_ta": "பெருந்தரவு தணிக்கை 100% டிஜிட்டல் பரிவர்த்தனைகளையும் தானியங்கி முறையில் சரிபார்க்க உதவுகிறது.",
        "fact_en": "CAG's CDMA uses advanced data pipelines to analyze GeM procurement anomalies.",
        "fact_ta": "சி.ஏ.ஜியின் CDMA மையம் GeM கொள்முதல் முறைகேடுகளை பகுப்பாய்வு செய்ய நவீன தரவு கட்டமைப்புகளைப் பயன்படுத்துகிறது."
    },
    # 23
    {
        "subtopic": "Key Constitutional Amendments Relevant to Audit",
        "intro_en": "Match List-I (Constitutional Amendment) with List-II (Impact on Financial Governance and Audit) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (அரசியலமைப்புத் திருத்தம்) பட்டியல்-II உடன் (நிதி ஆளுகை மற்றும் தணிக்கை மீதான தாக்கம்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": [
            "42nd Amendment Act 1976",
            "44th Amendment Act 1978",
            "73rd Amendment Act 1992",
            "101st Amendment Act 2016"
        ],
        "list1_ta": [
            "42வது திருத்தச் சட்டம் 1976",
            "44வது திருத்தச் சட்டம் 1978",
            "73வது திருத்தச் சட்டம் 1992",
            "101வது திருத்தச் சட்டம் 2016"
        ],
        "list2_en": [
            "Altered Article 150 to empower President to prescribe accounts after consultation with CAG",
            "Restored Article 150 to prescribe form of accounts strictly 'on the advice of the CAG'",
            "Inserted Article 243J authorizing state legislature laws for maintenance and audit of Panchayat accounts",
            "Created Goods and Services Tax regime requiring unified CAG audit of central and integrated taxes"
        ],
        "list2_ta": [
            "சி.ஏ.ஜியுடன் கலந்தாலோசித்து கணக்குப் படிவத்தை நிர்ணயிக்க குடியரசுத் தலைவருக்கு அதிகாரம் அளிக்க சரத்து 150-ஐ மாற்றியது",
            "சி.ஏ.ஜியின் 'ஆலோசனையின் பேரில்' மட்டுமே கணக்குப் படிவம் நிர்ணயிக்கப்பட வேண்டும் என சரத்து 150-ஐ மீட்டெடுத்தது",
            "பஞ்சாயத்து கணக்குகள் பராமரிப்பு மற்றும் தணிக்கைக்கான சட்டங்களை இயற்ற வகைசெய்யும் சரத்து 243J-ஐ சேர்த்தது",
            "மத்திய மற்றும் ஒருங்கிணைந்த வரிகளின் ஒருங்கிணைந்த தணிக்கை தேவைப்படும் ஜி.எஸ்.டி முறையை உருவாக்கியது"
        ],
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "42nd Amdt altered Art 150; 44th Amdt mandated 'on advice of CAG'; 73rd Amdt added Art 243J; 101st Amdt established GST audit framework.",
        "exp_ta": "42வது திருத்தம் சரத்து 150-ஐ மாற்றியது; 44வது திருத்தம் 'சி.ஏ.ஜி ஆலோசனையின் பேரில்' என மாற்றியது; 73வது திருத்தம் சரத்து 243J சேர்த்தது; 101வது திருத்தம் ஜிஎஸ்டியை உருவாக்கியது.",
        "tip_en": "44th Amendment restored CAG's binding constitutional advice in framing accounts under Article 150.",
        "tip_ta": "44வது திருத்தம் சரத்து 150-ன் கீழ் கணக்குப் படிவங்களை வகுப்பதில் சி.ஏ.ஜியின் ஆலோசனையை நிலைநிறுத்தியது.",
        "fact_en": "Article 243Z similarly governs the audit of accounts of Municipalities under 74th Amendment.",
        "fact_ta": "74வது திருத்தத்தின் கீழ் சரத்து 243Z நகராட்சிகளின் கணக்குத் தணிக்கையை முறைப்படுத்துகிறது."
    },
    # 24
    {
        "subtopic": "Types of Reports Tabled by PAC",
        "intro_en": "Match List-I (Parliamentary Report Type) with List-II (Stage and Purpose) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (நாடாளுமன்ற அறிக்கை வகை) பட்டியல்-II உடன் (கட்டம் மற்றும் நோக்கம்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": [
            "Original PAC Examination Report",
            "Action Taken Report (ATR)",
            "Action Taken Action Taken Report (ATATR)",
            "CAG Separate Audit Report (SAR)"
        ],
        "list1_ta": [
            "அசல் PAC ஆய்வு அறிக்கை",
            "நடவடிக்கை அறிக்கை (ATR)",
            "நடவடிக்கை மீதான நடவடிக்கை அறிக்கை (ATATR)",
            "சி.ஏ.ஜி தனித் தணிக்கை அறிக்கை (SAR)"
        ],
        "list2_en": [
            "First detailed parliamentary report containing conclusions and recommendations on CAG audit paragraphs",
            "Follow-up PAC report evaluating the adequacy of government action taken on initial recommendations",
            "Final parliamentary scrutiny report where PAC rejects inadequate government replies",
            "Specialized annual audit report presented on individual autonomous bodies and statutory authorities"
        ],
        "list2_ta": [
            "சி.ஏ.ஜி தணிக்கைப் பத்திகள் மீது முடிவுகள் மற்றும் பரிந்துரைகளைக் கொண்ட முதல் விரிவான நாடாளுமன்ற அறிக்கை",
            "ஆரம்பப் பரிந்துரைகள் மீது அரசு எடுத்த நடவடிக்கைகளின் போதுமான தன்மையை மதிப்பிடும் தொடர் PAC அறிக்கை",
            "அரசின் போதாத பதில்களை நிராகரித்து PAC சமர்ப்பிக்கும் இறுதி நாடாளுமன்ற ஆய்வு அறிக்கை",
            "தனிப்பட்ட தன்னாட்சி அமைப்புகள் மற்றும் சட்டப்பூர்வ அமைப்புகள் மீது சமர்ப்பிக்கப்படும் சிறப்பு வருடாந்திர தணிக்கை அறிக்கை"
        ],
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "PAC original report gives recommendations; ATR evaluates ministry replies; ATATR is final closure on unsatisfactory replies; SAR is CAG's report on autonomous institutions.",
        "exp_ta": "அசல் PAC அறிக்கை பரிந்துரைகளைத் தருகிறது; ATR அரசின் பதில்களை மதிப்பிடுகிறது; ATATR திருப்தியற்ற பதில்கள் மீதான இறுதி அறிக்கை; SAR என்பது தன்னாட்சி அமைப்புகள் மீதான சி.ஏ.ஜி அறிக்கை.",
        "tip_en": "The multi-stage PAC process ensures ministries cannot quietly bury uncomfortable CAG findings.",
        "tip_ta": "பல கட்ட PAC செயல்முறை அமைச்சகங்கள் சி.ஏ.ஜி தணிக்கைக் கண்டுபிடிப்புகளை மறைக்க முடியாதபடி செய்கிறது.",
        "fact_en": "PAC recommendations are accepted by convention, and rejections must be explained to Parliament.",
        "fact_ta": "PAC பரிந்துரைகள் மரபுப்படி ஏற்றுக்கொள்ளப்படுகின்றன; நிராகரித்தால் நாடாளுமன்றத்திற்கு விளக்கம் அளிக்க வேண்டும்."
    },
    # 25
    {
        "subtopic": "Landmark Telecom Audit Findings (2010)",
        "intro_en": "Match List-I (Telecom Audit Metric / Entity) with List-II (CAG Finding in 2G Spectrum Report) and select the correct code:",
        "intro_ta": "பட்டியல்-I-ஐ (தொலைத்தொடர்பு தணிக்கை அளவுரு / அமைப்பு) பட்டியல்-II உடன் (2G தணிக்கை அறிக்கையில் சி.ஏ.ஜி கண்டுபிடிப்பு) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "list1_en": [
            "Presumptive Loss Figure",
            "First-Come-First-Served (FCFS) Rule",
            "Dual Technology Allocation",
            "Entry Fee Valuation Basis"
        ],
        "list1_ta": [
            "உத்தேச இழப்பீட்டுத் தொகை",
            "முதலில் வந்தவருக்கு முன்னுரிமை (FCFS) விதி",
            "இரட்டை தொழில்நுட்ப ஒதுக்கீடு (Dual Technology)",
            "நுழைவுக் கட்டண மதிப்பீட்டு அடிப்படை"
        ],
        "list2_en": [
            "Estimated at Rs. 1.76 lakh crore based on 3G auction rates",
            "Procedural cut-off date advanced arbitrarily favouring select private telecom applicants",
            "Cross-allocation of CDMA and GSM spectrum permitted without fair market valuation",
            "Pegged to 2001 prices for licenses allocated in 2008 ignoring seven years of telecom boom"
        ],
        "list2_ta": [
            "3G ஏல விலைகளின் அடிப்படையில் கணக்கிடப்பட்ட ரூ. 1.76 லட்சம் கோடி உத்தேச இழப்பு",
            "தேர்ந்தெடுக்கப்பட்ட சில விண்ணப்பதாரர்களுக்கு சாதகமாக கடைசி தேதியை தன்னிச்சையாக முன்கூட்டியே மாற்றியது",
            "நியாயமான சந்தை மதிப்பீடு இல்லாமல் CDMA மற்றும் GSM அலைக்கற்றையை குறுக்கு ஒதுக்கீடு செய்ய அனுமதித்தது",
            "ஏழு ஆண்டு தொலைத்தொடர்பு வளர்ச்சியைப் புறக்கணித்து 2008 உரிமங்களுக்கு 2001 விலையை நிர்ணயித்தது"
        ],
        "correct_mapping": (1, 2, 3, 4),
        "exp_en": "2G report calculated Rs. 1.76 lakh crore presumptive loss; highlighted manipulation of FCFS dates; flagged dual technology approvals; criticized applying 2001 entry fees in 2008.",
        "exp_ta": "2G அறிக்கை ரூ. 1.76 லட்சம் கோடி உத்தேச இழப்பீட்டைக் கணக்கிட்டது; FCFS தேதி மாற்றங்களைச் சுட்டிக்காட்டியது; இரட்டை தொழில்நுட்ப முறைகேடுகளை வெளிப்படுத்தியது; 2001 கட்டணத்தை 2008-ல் வசூலித்ததை விமர்சித்தது.",
        "tip_en": "The 2G report by Vinod Rai led to the cancellation of 122 telecom licenses by the Supreme Court in 2012.",
        "tip_ta": "வினோத் ராயின் 2G அறிக்கை 2012-ல் 122 உரிமங்களை உச்ச நீதிமன்றம் ரத்து செய்ய வழிவகுத்தது.",
        "fact_en": "The Supreme Court mandated that all scarce natural resources must be allocated through open auctions.",
        "fact_ta": "இயற்கை வளங்கள் அனைத்தும் வெளிப்படையான ஏலம் மூலமே ஒதுக்கப்பட வேண்டும் என உச்ச நீதிமன்றம் உத்தரவிட்டது."
    }
]

def generate_match_options(correct_mapping):
    """
    correct_mapping: tuple of 4 integers, e.g. (1, 2, 3, 4) representing a->1, b->2, c->3, d->4
    Returns 4 unique option strings: 1 correct + 3 plausible distractors
    """
    correct_str = f"a-{correct_mapping[0]}, b-{correct_mapping[1]}, c-{correct_mapping[2]}, d-{correct_mapping[3]}"
    # 3 distractors
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
        qid = f"CAG_MF_{idx:03d}"
        correct_key = key_assignment[idx - 1]
        
        # Build stem
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
                
        q = make_cag_q(
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
            tags=["polity", "comptroller_and_auditor_general", "match_the_following", item["subtopic"].lower().replace(" ", "_")]
        )
        questions.append(q)
    return questions

if __name__ == "__main__":
    qs = build_questions()
    print(f"Generated {len(qs)} raw Match the Following questions for CAG.")
    
    out_path = os.path.join("data", "questions", "polity", "cag_match_the_following.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, ensure_ascii=False, indent=2)
    print(f"Saved Match the Following MCQs to {out_path}")
    
    # Also save alias
    alias_path = os.path.join("data", "questions", "polity", "cag_match.json")
    with open(alias_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, ensure_ascii=False, indent=2)
    print(f"Saved alias to {alias_path}")
    
    val = ContentValidator()
    report = val.validate_file(out_path, expected_count=25, expected_prefix="CAG_MF_")
    print(f"Validation Report: {'PASS' if report.is_valid else 'FAIL'} | Total: {report.total_audited}")
    if not report.is_valid:
        for iss in report.issues[:10]:
            print(f"  Issue: {iss}")
    print(f"Key Distribution: {report.key_distribution}")
