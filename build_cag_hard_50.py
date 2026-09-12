# -*- coding: utf-8 -*-
"""
Build 50 Hard MCQs for CAG (Comptroller & Auditor General of India)
ID range: CAG_H_001 to CAG_H_050
"""

import json
import os
from cag_mcq_helper import make_cag_q
from rebalance_er_helper import balance_question_keys
from tools.nova_content_engine.validator import ContentValidator

raw_questions = [
    # 1
    {
        "subtopic": "Constitutional Independence & Warrant of Appointment",
        "stem_en": "Why is the Comptroller and Auditor General of India appointed by the President by 'warrant under his hand and seal' rather than a standard presidential notification?",
        "stem_ta": "இந்தியக் கணக்காய்வு மற்றும் தணிக்கைத் தலைவர் (சி.ஏ.ஜி) ஒரு சாதாரண குடியரசுத் தலைவர் அறிவிக்கைக்குப் பதிலாக, குடியரசுத் தலைவரின் 'கையொப்பமிட்ட முத்திரையுடன் கூடிய ஆணை' (warrant under his hand and seal) மூலம் நியமிக்கப்படுவது ஏன்?",
        "options": [
            ("To confer high constitutional status and autonomy on par with Supreme Court judges, shielding the office from executive interference", "உயர் அரசியலமைப்பு அந்தஸ்தையும் உச்ச நீதிமன்ற நீதிபதிகளுக்கு இணையான தன்னாட்சியையும் வழங்கி, நிர்வாகத் தலையீட்டிலிருந்து பாதுகாப்பதற்காக"),
            ("Because the CAG is subordinate only to the Union Finance Minister", "ஏனெனில் சி.ஏ.ஜி மத்திய நிதி அமைச்சருக்கு மட்டுமே கீழ்ப்படிந்தவர் என்பதால்"),
            ("To permit the Prime Minister to dismiss the CAG at will without parliamentary approval", "நாடாளுமன்ற ஒப்புதலின்றி பிரதமரே சி.ஏ.ஜியை எப்போது வேண்டுமானாலும் பதவி நீக்கம் செய்ய அனுமதிப்பதற்காக"),
            ("Because the CAG is an ex-officio member of the Union Cabinet", "ஏனெனில் சி.ஏ.ஜி மத்திய அமைச்சரவையின் அலுவல் வழி உறுப்பினர் என்பதால்")
        ],
        "exp_en": "Under Article 148(1), the CAG is appointed by the President by warrant under his hand and seal, a special dignitary procedure reserved for high constitutional functionaries (Supreme Court/High Court judges, Governors, CAG) ensuring complete independence from ministerial hierarchy.",
        "exp_ta": "சரத்து 148(1)-ன் கீழ், சி.ஏ.ஜி குடியரசுத் தலைவரின் கையொப்பமிட்ட முத்திரையுடன் கூடிய ஆணை மூலம் நியமிக்கப்படுகிறார். இது உச்ச நீதிமன்ற நீதிபதிகள், ஆளுநர்கள் போன்ற உயர் அரசியலமைப்புப் பதவிகளுக்கு மட்டுமே வழங்கப்படும் சிறப்பு நடைமுறையாகும்.",
        "tip_en": "Only Supreme Court/HC judges, Governors, and CAG are appointed under presidential warrant under hand and seal.",
        "tip_ta": "உச்ச/உயர் நீதிமன்ற நீதிபதிகள், ஆளுநர்கள் மற்றும் சி.ஏ.ஜி மட்டுமே குடியரசுத் தலைவரின் கையொப்பமிட்ட முத்திரையுடன் கூடிய ஆணை மூலம் நியமிக்கப்படுகின்றனர்.",
        "fact_en": "Dr. B.R. Ambedkar regarded Article 148 as the bedrock of financial accountability in the Constitution.",
        "fact_ta": "அம்பேத்கர் சரத்து 148-ஐ அரசியலமைப்பின் நிதிப் பொறுப்புணர்வின் அடித்தளமாகக் கருதினார்."
    },
    # 2
    {
        "subtopic": "CAG (DPC) Act 1971 - Section 10 & 11 Separation",
        "stem_en": "Which landmark reform was implemented under the Comptroller and Auditor General's (Duties, Powers and Conditions of Service) Amendment Act of 1976?",
        "stem_ta": "1976 ஆம் ஆண்டின் தலைமைத் தணிக்கையாளர் (பணிகள், அதிகாரங்கள் மற்றும் சேவை நிபந்தனைகள்) திருத்தச் சட்டத்தின் கீழ் செயல்படுத்தப்பட்ட வரலாற்றுச் சிறப்புமிக்க சீர்திருத்தம் எது?",
        "options": [
            ("Separation of accounting functions from audit functions in the Union Government, establishing the Controller General of Accounts (CGA)", "மத்திய அரசில் கணக்கு வைக்கும் பணியை தணிக்கைப் பணியிலிருந்து பிரித்து, கணக்கு முதன்மைக் கட்டுப்பாட்டாளர் (CGA) பதவியை உருவாக்குதல்"),
            ("Abolishing the requirement of submitting annual audit reports to Parliament", "நாடாளுமன்றத்தில் ஆண்டு தணிக்கை அறிக்கைகளை சமர்ப்பிக்கும் தேவையை ரத்து செய்தல்"),
            ("Transferring audit of defence establishments completely to private chartered accountants", "பாதுகாப்பு நிறுவனங்களின் தணிக்கையை முற்றிலும் தனியார் தணிக்கையாளர்களிடம் ஒப்படைத்தல்"),
            ("Subordinating state government audit directorates directly under state finance secretaries", "மாநில தணிக்கை இயக்குநரகங்களை நேரடியாக மாநில நிதிச் செயலாளர்களின் கீழ் கொண்டுவருதல்")
        ],
        "exp_en": "In 1976, the CAG was relieved from the duty of compiling the accounts of the Union Government through an amendment to the 1971 Act, departmentalising accounts under the Controller General of Accounts (CGA) in the Ministry of Finance, while CAG retained pure audit jurisdiction.",
        "exp_ta": "1976-ல் 1971 ஆம் ஆண்டு சட்டத்தில் கொண்டுவரப்பட்ட திருத்தத்தின் மூலம், மத்திய அரசின் கணக்குகளைத் தயாரிக்கும் பணியிலிருந்து சி.ஏ.ஜி விடுவிக்கப்பட்டு, கணக்குகள் துறைமயமாக்கப்பட்டு நிதி அமைச்சகத்தின் CGA-விடம் ஒப்படைக்கப்பட்டது; சி.ஏ.ஜி தணிக்கை அதிகாரத்தை மட்டுமே தக்கவைத்துக் கொண்டார்.",
        "tip_en": "At the Union level: CGA compiles accounts; CAG audits accounts. At State level: CAG compiles AND audits accounts.",
        "tip_ta": "மத்திய அளவில்: CGA கணக்குகளைத் தொகுக்கிறார்; CAG தணிக்கை செய்கிறார். மாநில அளவில்: இரண்டையுமே CAG செய்கிறார்.",
        "fact_en": "The CGA works under the Department of Expenditure, Ministry of Finance, and is not a constitutional authority.",
        "fact_ta": "CGA நிதி அமைச்சகத்தின் செலவினத் துறையின் கீழ் இயங்குகிறார்; அவர் அரசியலமைப்பு அதிகார அமைப்பல்ல."
    },
    # 3
    {
        "subtopic": "Propriety Audit vs Regulatory Audit",
        "stem_en": "In financial audit jurisprudence, what distinguishes a 'Propriety Audit' from a 'Regularity/Legal Audit' conducted by the CAG?",
        "stem_ta": "நிதித் தணிக்கை நெறிமுறைகளில், சி.ஏ.ஜியால் நடத்தப்படும் 'ஒழுங்குமுறை/சட்டரீதியான தணிக்கையிலிருந்து' (Regularity Audit) 'நாணய/விவேக தணிக்கை' (Propriety Audit) எவ்வாறு வேறுபடுகிறது?",
        "options": [
            ("Propriety audit scrutinizes wisdom, faithfulness, and economy of expenditure beyond mere legal sanctions and rules", "நாணயத் தணிக்கை என்பது வெறும் சட்ட விதிகளுக்கு அப்பால் செலவினத்தின் விவேகம், நேர்மை மற்றும் சிக்கனத்தை ஆய்வு செய்வதாகும்"),
            ("Propriety audit deals exclusively with private donations received by cabinet ministers", "நாணயத் தணிக்கை என்பது அமைச்சரவை அமைச்சர்கள் பெறும் தனியார் நன்கொடைகளை மட்டுமே கையாள்கிறது"),
            ("Regularity audit is discretionary, whereas propriety audit is strictly mandatory under Article 149", "ஒழுங்குமுறைத் தணிக்கை விருப்பத்திற்குரியது, ஆனால் நாணயத் தணிக்கை சரத்து 149-ன் கீழ் கட்டாயமானது"),
            ("Propriety audit cannot be challenged or questioned even by the Supreme Court of India", "நாணயத் தணிக்கையை இந்திய உச்ச நீதிமன்றத்தால் கூட கேள்வி கேட்க முடியாது")
        ],
        "exp_en": "While regulatory/legal audit checks whether money was spent in accordance with law and sanctioned rules, propriety audit investigates the wisdom, faithfulness, and public interest of transactions, questioning wastefulness, extravagance, and dubious executive judgment.",
        "exp_ta": "சட்டரீதியான தணிக்கை விதிகள் மற்றும் ஒதுக்கீடுகளின்படி பணம் செலவிடப்பட்டதா என்று மட்டுமே பார்க்கிறது; ஆனால் விவேக/நாணயத் தணிக்கை விரயம், வீண் செலவு மற்றும் பொது நலன் ஆகியவற்றை கேள்விக்குட்படுத்துகிறது.",
        "tip_en": "Propriety audit checks: 'Was this expenditure prudent, wise, and in genuine public interest?'",
        "tip_ta": "விவேகத் தணிக்கை: 'இந்தச் செலவு விவேகமானதா, சிக்கனமானதா மற்றும் உண்மையான பொது நலன் சார்ந்ததா?' என்பதை ஆராய்கிறது.",
        "fact_en": "Propriety audit is inherently discretionary and tests whether public money was spent like a person of ordinary prudence would spend their own.",
        "fact_ta": "ஒரு சாதாரண விவேகமுள்ள மனிதன் தன் சொந்தப் பணத்தைச் செலவிடுவது போல் பொதுப் பணம் செலவிடப்பட்டதா என்பதை நாணயத் தணிக்கை சோதிக்கிறது."
    },
    # 4
    {
        "subtopic": "Section 14 of CAG (DPC) Act 1971",
        "stem_en": "Under Section 14 of the CAG (DPC) Act 1971, when is the audit of bodies or authorities substantially financed by grants or loans from the Consolidated Fund mandatory for the CAG?",
        "stem_ta": "1971 ஆம் ஆண்டின் சி.ஏ.ஜி சட்டத்தின் பிரிவு 14-ன் கீழ், திரட்டப்பட்ட நிதியிலிருந்து மானியங்கள் அல்லது கடன்கள் பெறும் அமைப்புகளை சி.ஏ.ஜி கட்டாயமாகத் தணிக்கை செய்ய வேண்டிய நிதி வரம்பு என்ன?",
        "options": [
            ("When government grant/loan is not less than Rs. 25 lakh and constitutes at least 75% of the total expenditure of the body", "அரசு மானியம்/கடன் ரூ. 25 லட்சத்திற்குக் குறையாமலும், அவ்வமைப்பின் மொத்த செலவில் குறைந்தது 75% ஆகவும் இருக்கும் போது"),
            ("When government grant exceeds Rs. 1 crore regardless of percentage of total expenditure", "மொத்த செலவின் சதவீதத்தைக் கருத்தில் கொள்ளாமல் அரசு மானியம் ரூ. 1 கோடியைத் தாண்டும் போது"),
            ("When the body has more than 5,000 permanent employees on government payroll", "அவ்வமைப்பில் 5,000-க்கும் மேற்பட்ட நிரந்தர அரசு ஊழியர்கள் பணியாற்றும் போது"),
            ("Only when specifically requested by the President under Article 280", "சரத்து 280-ன் கீழ் குடியரசுத் தலைவர் குறிப்பாகக் கோரும் போது மட்டுமே")
        ],
        "exp_en": "Under Section 14(1) of the CAG Act 1971, where any body or authority is substantially financed by grants or loans (not less than Rs. 25 lakhs and such grant/loan is not less than 75% of total expenditure), the CAG shall audit all receipts and expenditure of that body.",
        "exp_ta": "1971 சி.ஏ.ஜி சட்டத்தின் பிரிவு 14(1)-ன் படி, ஏதேனும் ஒரு அமைப்புக்கு அளிக்கப்படும் மானியம் அல்லது கடன் ரூ. 25 லட்சத்திற்குக் குறையாமலும், மொத்த செலவினத்தில் குறைந்தது 75% ஆகவும் இருந்தால், அவ்வமைப்பை சி.ஏ.ஜி தணிக்கை செய்வது கட்டாயமாகும்.",
        "tip_en": "Key thresholds under Section 14: Rs. 25 lakh and 75% of total expenditure.",
        "tip_ta": "பிரிவு 14-ன் முக்கிய வரம்புகள்: ரூ. 25 லட்சம் மற்றும் மொத்த செலவில் 75%.",
        "fact_en": "Section 14(2) also allows CAG to audit bodies receiving grants of Rs. 1 crore or more with prior approval of President/Governor.",
        "fact_ta": "பிரிவு 14(2)-ன் படி ரூ. 1 கோடிக்கு மேல் மானியம் பெறும் அமைப்புகளையும் குடியரசுத் தலைவர்/ஆளுநர் ஒப்புதலுடன் சி.ஏ.ஜி தணிக்கை செய்யலாம்."
    },
    # 5
    {
        "subtopic": "Supreme Court Ruling on Telecom Revenue Audit (2014)",
        "stem_en": "In the landmark judgment Association of Unified Telecom Service Providers of India (AUTSPI) v. Union of India (2014), what did the Supreme Court rule regarding CAG's audit jurisdiction?",
        "stem_ta": "இந்திய ஒருங்கிணைந்த தொலைத்தொடர்பு சேவை வழங்குநர்கள் சங்கம் எதிர் இந்திய யூனியன் (2014) வழக்கில், உச்ச நீதிமன்றம் சி.ஏ.ஜியின் தணிக்கை அதிகாரம் குறித்து என்ன தீர்ப்பளித்தது?",
        "options": [
            ("CAG has the authority to audit the accounts of private telecom licensees sharing revenue with the Consolidated Fund under Article 149", "சரத்து 149-ன் கீழ் திரட்டப்பட்ட நிதியுடன் வருவாயைப் பகிர்ந்துகொள்ளும் தனியார் தொலைத்தொடர்பு நிறுவனங்களின் கணக்குகளைத் தணிக்கை செய்ய சி.ஏ.ஜிக்கு அதிகாரம் உண்டு"),
            ("Private corporate accounts are completely immune from CAG scrutiny under all circumstances", "தனியார் நிறுவனங்களின் கணக்குகள் எக்காரணம் கொண்டும் சி.ஏ.ஜியின் ஆய்வுக்கு உட்படாது"),
            ("CAG can audit telecom providers only if the Central Government holds 51% equity shares", "மத்திய அரசு 51% பங்குகளை வைத்திருந்தால் மட்டுமே தொலைத்தொடர்பு நிறுவனங்களை சி.ஏ.ஜி தணிக்கை செய்ய முடியும்"),
            ("Telecom spectrum revenue audit must be transferred exclusively to TRAI", "தொலைத்தொடர்பு அலைக்கற்றை வருவாய் தணிக்கை டிராய் (TRAI) அமைப்பிடம் மட்டுமே ஒப்படைக்கப்பட வேண்டும்")
        ],
        "exp_en": "The Supreme Court in 2014 held that because private telecom service providers share revenue generated from sovereign national natural resources (spectrum) with the Consolidated Fund of India, CAG has constitutional authority under Article 149 and Rule 5 of 2002 Audit Rules to audit their revenue records.",
        "exp_ta": "2014-ல் உச்ச நீதிமன்றம், அரசுக்குச் சொந்தமான அலைக்கற்றை வளங்களைப் பயன்படுத்தி ஈட்டப்படும் வருவாயை அரசுடன் பகிர்வதால், தனியார் தொலைத்தொடர்பு நிறுவனங்களின் வருவாய்க் கணக்குகளைத் தணிக்கை செய்ய சி.ஏ.ஜிக்கு அரசியலமைப்பு அதிகாரம் உண்டு எனத் தீர்ப்பளித்தது.",
        "tip_en": "AUTSPI v. Union of India (2014) expanded CAG's reach into private entities sharing revenue from national natural resources.",
        "tip_ta": "2014 தீர்ப்பு இயற்கை வளங்கள் மூலம் அரசுடன் வருவாய் பகிரும் தனியார் நிறுவனங்களை தணிக்கை செய்யும் சி.ஏ.ஜியின் அதிகாரத்தை உறுதிப்படுத்தியது.",
        "fact_en": "The court invoked the Public Trust Doctrine, holding that natural resources belong to the people and the CAG protects public revenue.",
        "fact_ta": "இயற்கை வளங்கள் மக்களுக்குச் சொந்தமானது என்ற பொது அறக்கட்டளைக் கோட்பாட்டை (Public Trust Doctrine) உச்ச நீதிமன்றம் சுட்டிக்காட்டியது."
    },
    # 6
    {
        "subtopic": "Audit of Public-Private Partnerships (PPP)",
        "stem_en": "What is the primary rationale and scope of the CAG auditing Public-Private Partnership (PPP) infrastructure concession projects in India?",
        "stem_ta": "இந்தியாவில் அரசு-தனியார் கூட்டு (PPP) உள்கட்டமைப்புத் திட்டங்களை சி.ஏ.ஜி தணிக்கை செய்வதன் முதன்மை நோக்கம் மற்றும் எல்லை என்ன?",
        "options": [
            ("To verify whether sovereign assets, viability gap funding, and toll/tariff revenue sharing with the exchequer are accurately safeguarded", "அரசு சொத்துக்கள், சாத்தியக்கூறு இடைவெளி நிதி (VGF) மற்றும் அரசுக்குச் சேர வேண்டிய கட்டண வருவாய்ப் பகிர்வு சரியாகப் பாதுகாக்கப்படுகிறதா என்பதை உறுதி செய்ய"),
            ("To supervise the day-to-day hiring of construction labourers by private concessionaires", "தனியார் நிறுவனங்கள் தினசரி கட்டுமானத் தொழிலாளர்களை நியமிப்பதைக் கண்காணிக்க"),
            ("To convert all private highway operators into public sector undertakings", "அனைத்து தனியார் நெடுஞ்சாலை நிறுவனங்களையும் பொதுத்துறை நிறுவனங்களாக மாற்ற"),
            ("To fix commodity wholesale prices in toll booth concession zones", "சுங்கச்சாவடி பகுதிகளில் விற்கப்படும் பொருட்களின் விலையை நிர்ணயிக்க")
        ],
        "exp_en": "Under CAG's Guidelines for Audit of PPP Projects, the audit ensures that public assets leased out are not devalued, government grants/viability gap funding are utilized lawfully, user fees are not overcharged, and the government's rightful share of revenue is paid into the Consolidated Fund.",
        "exp_ta": "PPP தணிக்கை வழிகாட்டுதல்களின்படி, குத்தகைக்கு விடப்பட்ட அரசு சொத்துக்கள் மதிப்பிழக்காமல் இருப்பதையும், அரசு மானியங்கள் முறையாகப் பயன்படுத்தப்படுவதையும், அரசுக்கான முறையான வருவாய்ப் பங்கு திரட்டப்பட்ட நிதியில் செலுத்தப்படுவதையும் சி.ஏ.ஜி உறுதி செய்கிறது.",
        "tip_en": "PPP audit examines concession agreements, Viability Gap Funding (VGF), and sovereign asset protection.",
        "tip_ta": "PPP தணிக்கை ஒப்பந்தங்கள், சாத்தியக்கூறு நிதி (VGF) மற்றும் அரசு சொத்துப் பாதுகாப்பை ஆராய்கிறது.",
        "fact_en": "Major PPP audits by CAG include Delhi and Mumbai Airport concessions and NHAI highway toll concessions.",
        "fact_ta": "டெல்லி, மும்பை விமான நிலையங்கள் மற்றும் தேசிய நெடுஞ்சாலைத் திட்டங்கள் சி.ஏ.ஜியின் முக்கிய PPP தணிக்கைகளில் அடங்கும்."
    },
    # 7
    {
        "subtopic": "Performance Audit & 3Es Framework",
        "stem_en": "In CAG's Performance Auditing Standards, what does the fundamental '3Es' evaluation framework represent?",
        "stem_ta": "சி.ஏ.ஜியின் செயல்திறன் தணிக்கைத் தரநிலைகளில், அடிப்படையான '3Es' மதிப்பீட்டுக் கட்டமைப்பு எதனைக் குறிக்கிறது?",
        "options": [
            ("Economy, Efficiency, and Effectiveness", "சிக்கனம் (Economy), செயல்திறன் (Efficiency), மற்றும் செயலூக்கம் (Effectiveness)"),
            ("Equity, Equality, and Eligibility", "நீதி (Equity), சமத்துவம் (Equality), மற்றும் தகுதி (Eligibility)"),
            ("Execution, Expenditure, and Exemption", "செயல்படுத்துதல் (Execution), செலவினம் (Expenditure), மற்றும் விலக்கு (Exemption)"),
            ("Ethics, Environment, and Ecology", "ஒழுக்கம் (Ethics), சுற்றுச்சூழல் (Environment), மற்றும் சூழலியல் (Ecology)")
        ],
        "exp_en": "CAG's performance audit evaluates: Economy (minimising the cost of resources acquired), Efficiency (maximising outputs from given inputs), and Effectiveness (achieving intended policy outcomes and social objectives).",
        "exp_ta": "செயல்திறன் தணிக்கையானது: சிக்கனம் (வளங்களின் விலையைக் குறைத்தல்), செயல்திறன் (குறைந்த உள்ளீட்டில் அதிக வெளியீடு பெறுதல்), மற்றும் செயலூக்கம் (திட்டமிடப்பட்ட கொள்கை இலக்குகளை அடைதல்) ஆகிய 3Es கட்டமைப்பை மதிப்பிடுகிறது.",
        "tip_en": "3Es: Economy (spending less), Efficiency (spending well), Effectiveness (spending wisely for results).",
        "tip_ta": "3Es: சிக்கனம் (குறைவான செலவு), செயல்திறன் (சிறந்த முறையில் செலவு), செயலூக்கம் (இலக்குகளை அடைதல்).",
        "fact_en": "CAG adopted ASOSAI and INTOSAI performance auditing guidelines to benchmark Indian audit against global best practices.",
        "fact_ta": "சி.ஏ.ஜி உலகளாவிய சிறந்த நடைமுறைகளுக்காக ASOSAI மற்றும் INTOSAI வழிகாட்டுதல்களைப் பின்பற்றுகிறது."
    },
    # 8
    {
        "subtopic": "Appropriation Accounts vs Finance Accounts",
        "stem_en": "What is the key technical difference between the 'Appropriation Accounts' and the 'Finance Accounts' prepared/audited by the CAG?",
        "stem_ta": "சி.ஏ.ஜியால் தணிக்கை செய்யப்படும் 'ஒதுக்கீட்டுக் கணக்குகள்' (Appropriation Accounts) மற்றும் 'நிதிக் கணக்குகள்' (Finance Accounts) ஆகியவற்றுக்கு இடையேயான முக்கிய தொழில்நுட்ப வேறுபாடு என்ன?",
        "options": [
            ("Appropriation Accounts compare actual expenditure against legislative voted grants, while Finance Accounts present overall annual receipts and disbursements of the government", "ஒதுக்கீட்டுக் கணக்குகள் சட்டப்பேரவை அனுமதித்த மானியங்களுடன் உண்மையான செலவை ஒப்பிடுகின்றன; நிதிக் கணக்குகள் அரசின் ஒட்டுமொத்த வரவு-செலவுகளை முன்வைக்கின்றன"),
            ("Appropriation Accounts are presented only to state governors, whereas Finance Accounts go directly to the UN", "ஒதுக்கீட்டுக் கணக்குகள் ஆளுநர்களுக்கு மட்டுமே சமர்ப்பிக்கப்படுகின்றன, நிதிக் கணக்குகள் ஐ.நா.வுக்கு நேரடியாகச் செல்கின்றன"),
            ("Finance Accounts audit military hardware procurement, whereas Appropriation Accounts audit civilian pensions", "நிதிக் கணக்குகள் ராணுவக் கொள்முதலைத் தணிக்கை செய்கின்றன; ஒதுக்கீட்டுக் கணக்குகள் ஓய்வூதியங்களைத் தணிக்கை செய்கின்றன"),
            ("Appropriation Accounts deal exclusively with foreign loans, while Finance Accounts record domestic municipal taxes", "ஒதுக்கீட்டுக் கணக்குகள் வெளிநாட்டுக் கடன்களை மட்டுமே கையாள்கின்றன; நிதிக் கணக்குகள் நகராட்சி வரிகளைப் பதிவு செய்கின்றன")
        ],
        "exp_en": "Appropriation Accounts compare actual expenditure under each grant and appropriation with the amounts voted by Parliament/Legislature. Finance Accounts present a comprehensive picture of all receipts, capital/revenue disbursements, public debt, and financial liabilities of the Government.",
        "exp_ta": "ஒதுக்கீட்டுக் கணக்குகள் நாடாளுமன்றம்/சட்டமன்றத்தால் வாக்களிக்கப்பட்ட நிதியுடன் உண்மையான செலவினங்களை ஒப்பிடுகின்றன; நிதிக் கணக்குகள் அரசின் அனைத்து வரவுகள், வருவாய்-மூலதனச் செலவுகள் மற்றும் பொதுக்கடன்களைக் காட்டுகின்றன.",
        "tip_en": "Appropriation Accounts = Voted Grant vs Actual Spend. Finance Accounts = Government's balance sheet of total receipts and disbursements.",
        "tip_ta": "ஒதுக்கீட்டுக் கணக்கு = அங்கீகரிக்கப்பட்ட மானியம் vs உண்மைச் செலவு. நிதிக் கணக்கு = அரசின் ஒட்டுமொத்த வரவு-செலவு இருப்புநிலைக் குறிப்பு.",
        "fact_en": "Both accounts are prepared annually and tabled in Parliament under Article 151(1).",
        "fact_ta": "இரண்டு கணக்குகளும் ஆண்டுதோறும் தயாரிக்கப்பட்டு சரத்து 151(1)-ன் கீழ் நாடாளுமன்றத்தில் சமர்ப்பிக்கப்படுகின்றன."
    },
    # 9
    {
        "subtopic": "Article 150 & Prescribing Form of Accounts",
        "stem_en": "What did the 42nd and 44th Constitutional Amendments modify regarding Article 150 of the Constitution?",
        "stem_ta": "அரசியலமைப்புச் சட்டம் சரத்து 150 தொடர்பாக 42வது மற்றும் 44வது அரசியலமைப்புத் திருத்தங்கள் செய்த மாற்றம் என்ன?",
        "options": [
            ("Accounts of Union and States shall be kept in such form as the President prescribes on the advice of the CAG", "சி.ஏ.ஜியின் ஆலோசனையின் பேரில் குடியரசுத் தலைவர் பரிந்துரைக்கும் படிவத்தில் மத்திய மற்றும் மாநிலங்களின் கணக்குகள் பராமரிக்கப்பட வேண்டும்"),
            ("State assemblies were empowered to draft their own accounting forms without presidential reference", "மாநில சட்டப்பேரவைகள் குடியரசுத் தலைவரின் ஒப்புதலின்றி தங்கள் சொந்த கணக்கு முறைகளை உருவாக்க அதிகாரம் பெற்றன"),
            ("The power to prescribe accounts was transferred permanently to NITI Aayog", "கணக்குகளின் படிவத்தை நிர்ணயிக்கும் அதிகாரம் நிதி ஆயோக்கிற்கு நிரந்தரமாக மாற்றப்பட்டது"),
            ("All government accounts must be maintained exclusively in foreign currencies", "அனைத்து அரசு கணக்குகளும் வெளிநாட்டு நாணயங்களில் மட்டுமே பராமரிக்கப்பட வேண்டும்")
        ],
        "exp_en": "Under the 44th Amendment Act 1978, Article 150 was restored to state: 'The accounts of the Union and of the States shall be kept in such form as the President may, on the advice of the Comptroller and Auditor General of India, prescribe.'",
        "exp_ta": "44வது திருத்தச் சட்டம் 1978-ன் படி, சரத்து 150 திருத்தப்பட்டு: 'மத்திய மற்றும் மாநிலங்களின் கணக்குகள் இந்தியத் தலைமைத் தணிக்கையாளரின் ஆலோசனையின் பேரில் குடியரசுத் தலைவர் நிர்ணயிக்கும் படிவத்தில் வைக்கப்பட வேண்டும்' என வரையறுக்கப்பட்டது.",
        "tip_en": "President prescribes accounting forms, but strictly ON THE ADVICE of the CAG.",
        "tip_ta": "கணக்குகளின் படிவத்தைக் குடியரசுத் தலைவர் நிர்ணயிக்கிறார், ஆனால் கட்டாயமாக சி.ஏ.ஜியின் ஆலோசனையின் பேரில் மட்டுமே.",
        "fact_en": "Originally, Article 150 gave this power to CAG with approval of President; 42nd Amendment altered it, and 44th Amendment finalized 'on the advice of CAG'.",
        "fact_ta": "42வது திருத்தம் மாற்றியமைத்த போதிலும், 44வது திருத்தம் 'சி.ஏ.ஜியின் ஆலோசனையின் பேரில் குடியரசுத் தலைவர்' என்ற முறையை இறுதி செய்தது."
    },
    # 10
    {
        "subtopic": "Section 18 of CAG (DPC) Act 1971 - Powers of Inspection",
        "stem_en": "Which of the following statutory powers is explicitly vested in the CAG under Section 18 of the CAG (DPC) Act 1971?",
        "stem_ta": "1971 ஆம் ஆண்டின் சி.ஏ.ஜி சட்டத்தின் பிரிவு 18-ன் கீழ் சி.ஏ.ஜிக்கு வெளிப்படையாக வழங்கப்பட்டுள்ள சட்டப்பூர்வ அதிகாரம் எது?",
        "options": [
            ("Power to inspect any office of accounts, call for books and documents, and examine any person upon oath or requisition", "கணக்குகள் உள்ள எந்தவொரு அலுவலகத்தையும் ஆய்வு செய்தல், புத்தகங்கள் மற்றும் ஆவணங்களைக் கோருதல் மற்றும் தகவல்களைக் கேட்டுப் பெறுதல்"),
            ("Power to issue arrest warrants and incarcerate government accountants found guilty of fraud", "மோசடியில் ஈடுபட்ட அரசு கணக்காளர்களைக் கைது செய்து சிறையில் அடைப்பதற்கான பிடியாணை பிறப்பிக்கும் அதிகாரம்"),
            ("Power to unilaterally freeze the Consolidated Fund of India during fiscal emergencies", "நிதி அவசரநிலையின் போது திரட்டப்பட்ட நிதியைத் தன்னிச்சையாக முடக்கும் அதிகாரம்"),
            ("Power to amend the annual budget passed by Parliament", "நாடாளுமன்றம் நிறைவேற்றிய வருடாந்திர நிதிநிலை அறிக்கையைத் திருத்தும் அதிகாரம்")
        ],
        "exp_en": "Section 18 empowers the CAG to inspect any office of accounts under the Union or States, requisition all books, papers, vouchers, and other relevant documents, and put such questions or call for such information as necessary for audit.",
        "exp_ta": "பிரிவு 18-ன் கீழ், சி.ஏ.ஜி மத்திய/மாநில அரசுத் துறைகளின் எந்தவொரு கணக்கு அலுவலகத்தையும் ஆய்வு செய்யவும், ஆவணங்கள், ரசீதுகள் மற்றும் பதிவேடுகளைக் கோரவும், தேவையான விளக்கங்களைக் கேட்கவும் அதிகாரம் பெற்றுள்ளார்.",
        "tip_en": "Section 18 gives CAG full access to books, documents, and inspection rights, but CAG cannot arrest or punish officers.",
        "tip_ta": "பிரிவு 18 ஆவணங்களைப் பார்வையிட முழு அதிகாரம் அளிக்கிறது; ஆனால் அதிகாரிகளைத் தண்டிக்கவோ கைது செய்யவோ முடியாது.",
        "fact_en": "Executive departments cannot deny production of records to the CAG citing departmental secrecy unless protected by statutory privilege.",
        "fact_ta": "சட்டப்பூர்வ விலக்கு தவிர்த்து, துறைசார் ரகசியம் என்ற காரணத்தைக் கூறி சி.ஏ.ஜிக்கு ஆவணங்களை வழங்க அரசுத் துறைகள் மறுக்க முடியாது."
    },
    # 11
    {
        "subtopic": "Constituent Assembly Debates on CAG Status",
        "stem_en": "During the Constituent Assembly debates on Article 148, which four institutions did Dr. B.R. Ambedkar describe as the 'pillars of democracy' in the Indian Constitution?",
        "stem_ta": "அரசியலமைப்பு நிர்ணய சபை விவாதங்களில், டாக்டர் பி.ஆர். அம்பேத்கர் இந்திய அரசியலமைப்பின் 'ஜனநாயகத்தின் நான்கு முக்கியத் தூண்கள்' என்று விவரித்த நான்கு அமைப்புகள் எவை?",
        "options": [
            ("Supreme Court, Election Commission, Union Public Service Commission, and Comptroller and Auditor General", "உச்ச நீதிமன்றம், தேர்தல் ஆணையம், மத்திய அரசுப் பணியாளர் தேர்வாணையம் மற்றும் தலைமைத் தணிக்கையாளர் (சி.ஏ.ஜி)"),
            ("Lok Sabha, Rajya Sabha, Supreme Court, and Prime Minister's Office", "மக்களவை, மாநிலங்களவை, உச்ச நீதிமன்றம் மற்றும் பிரதமர் அலுவலகம்"),
            ("Armed Forces, Civil Services, Planning Commission, and Finance Commission", "முப்படைகள், குடிமைப் பணிகள், திட்டக் குழு மற்றும் நிதி ஆணையம்"),
            ("Supreme Court, High Courts, Central Vigilance Commission, and CBI", "உச்ச நீதிமன்றம், உயர் நீதிமன்றங்கள், மத்திய ஊழல் கண்காணிப்பு ஆணையம் மற்றும் சி.பி.ஐ")
        ],
        "exp_en": "Dr. B.R. Ambedkar declared that the four bulwarks of democratic governance under the Constitution are: the Judiciary (Supreme Court), the Election Commission, the Union Public Service Commission, and the Comptroller and Auditor General of India.",
        "exp_ta": "டாக்டர் அம்பேத்கர், அரசியலமைப்பின் கீழ் ஜனநாயகத்தின் நான்கு முக்கியப் பாதுகாப்புக் கோட்டைகள்: உச்ச நீதிமன்றம், தேர்தல் ஆணையம், மத்திய அரசுப் பணியாளர் தேர்வாணையம் (UPSC), மற்றும் தலைமைத் தணிக்கையாளர் (சி.ஏ.ஜி) என்று அறிவித்தார்.",
        "tip_en": "Ambedkar called CAG 'the most important officer in the Constitution of India'.",
        "tip_ta": "அம்பேத்கர் சி.ஏ.ஜியை 'இந்திய அரசியலமைப்பின் மிக முக்கியமான அதிகாரி' என்று அழைத்தார்.",
        "fact_en": "Ambedkar placed CAG's duties even above those of the judiciary because financial laxity can ruin an entire nation.",
        "fact_ta": "நிதி முறைகேடு நாட்டை அழித்துவிடும் என்பதால், சி.ஏ.ஜியின் பணிகளை நீதித்துறையை விடவும் முக்கியமானது என்று அம்பேத்கர் குறிப்பிட்டார்."
    },
    # 12
    {
        "subtopic": "Section 19 - Audit of Government Companies & Corporations",
        "stem_en": "Under Section 19(1) of the CAG (DPC) Act 1971, how does the CAG exercise audit authority over Government Companies incorporated under the Companies Act?",
        "stem_ta": "1971 ஆம் ஆண்டின் சி.ஏ.ஜி சட்டத்தின் பிரிவு 19(1)-ன் கீழ், நிறுவனங்கள் சட்டத்தின் கீழ் பதிவு செய்யப்பட்ட அரசு நிறுவனங்கள் மீது சி.ஏ.ஜி தனது தணிக்கை அதிகாரத்தை எவ்வாறு செலுத்துகிறார்?",
        "options": [
            ("CAG appoints statutory chartered accountants, issues audit directions, and conducts a supplementary or test audit", "சி.ஏ.ஜி சட்டப்பூர்வ பட்டயக் கணக்காளர்களை நியமிக்கிறார், தணிக்கை வழிகாட்டுதல்களை வழங்குகிறார் மற்றும் துணை அல்லது மாதிரித் தணிக்கை நடத்துகிறார்"),
            ("CAG permanently replaces all private chartered accountants and conducts 100% voucher audits personally", "சி.ஏ.ஜி அனைத்து தனியார் தணிக்கையாளர்களையும் நீக்கிவிட்டு, தானே 100% வவுச்சர் தணிக்கைகளை நடத்துகிறார்"),
            ("CAG only audits dividend payments deposited in private commercial bank accounts", "தனியார் வணிக வங்கிக் கணக்குகளில் டெபாசிட் செய்யப்படும் ஈவுத்தொகை கொடுப்பனவுகளை மட்டுமே சி.ஏ.ஜி தணிக்கை செய்கிறார்"),
            ("CAG has zero audit authority over any company registered under the Companies Act", "நிறுவனங்கள் சட்டத்தின் கீழ் பதிவு செய்யப்பட்ட எந்தவொரு நிறுவனம் மீதும் சி.ஏ.ஜிக்கு தணிக்கை அதிகாரம் கிடையாது")
        ],
        "exp_en": "Under Section 19(1) of the CAG Act and Section 143 of the Companies Act 2013, the CAG appoints statutory auditors for government companies, directs the manner of audit, and conducts supplementary audit within 60 days of receiving the statutory auditor's report.",
        "exp_ta": "நிறுவனங்கள் சட்டம் 2013-ன் பிரிவு 143 மற்றும் சி.ஏ.ஜி சட்டத்தின்படி, அரசு நிறுவனங்களுக்கு சட்டப்பூர்வ தணிக்கையாளர்களை சி.ஏ.ஜி நியமிக்கிறார், வழிகாட்டுகிறார் மற்றும் 60 நாட்களுக்குள் துணைத் தணிக்கை (supplementary audit) செய்கிறார்.",
        "tip_en": "Government Companies: Primary audit by CA appointed by CAG; Supplementary audit directly by CAG.",
        "tip_ta": "அரசு நிறுவனங்கள்: சி.ஏ.ஜியால் நியமிக்கப்படும் பட்டயக் கணக்காளர் முதன்மைத் தணிக்கை செய்கிறார்; சி.ஏ.ஜி துணைத் தணிக்கை செய்கிறார்.",
        "fact_en": "CAG also has the power to order a test audit of the company's accounts under Section 143(7) of the Companies Act 2013.",
        "fact_ta": "நிறுவனங்கள் சட்டம் 2013 பிரிவு 143(7)-ன் கீழ் நிறுவனக் கணக்குகளின் மாதிரித் தணிக்கைக்கு (test audit) உத்தரவிடவும் சி.ஏ.ஜிக்கு அதிகாரம் உண்டு."
    },
    # 13
    {
        "subtopic": "Corporations Completely Exempt from CAG Audit",
        "stem_en": "Which of the following major statutory corporations is audited exclusively by private chartered accountants, with NO audit role for the CAG?",
        "stem_ta": "பின்வரும் எந்த முக்கிய சட்டப்பூர்வ நிறுவனம் முற்றிலும் தனியார் பட்டயக் கணக்காளர்களால் மட்டுமே தணிக்கை செய்யப்படுகிறது மற்றும் அதில் சி.ஏ.ஜிக்கு எவ்வித தணிக்கைப் பங்கும் இல்லை?",
        "options": [
            ("Reserve Bank of India (RBI) and State Bank of India (SBI)", "இந்திய ரிசர்வ் வங்கி (RBI) மற்றும் பாரத ஸ்டேட் வங்கி (SBI)"),
            ("Damodar Valley Corporation (DVC)", "தாமோதர் பள்ளத்தாக்கு கழகம் (DVC)"),
            ("Airports Authority of India (AAI)", "இந்திய விமான நிலையங்கள் ஆணையம் (AAI)"),
            ("National Highways Authority of India (NHAI)", "இந்திய தேசிய நெடுஞ்சாலைகள் ஆணையம் (NHAI)")
        ],
        "exp_en": "Financial institutions and banking bodies like the Reserve Bank of India (RBI), State Bank of India (SBI), and Life Insurance Corporation (LIC) are audited exclusively by independent private auditors appointed under their governing statutes; CAG has no role in their regular audit.",
        "exp_ta": "இந்திய ரிசர்வ் வங்கி (RBI), பாரத ஸ்டேட் வங்கி (SBI), எல்.ஐ.சி (LIC) போன்ற நிதி அமைப்புகள் அவற்றின் சொந்தச் சட்டங்களின் கீழ் நியமிக்கப்படும் தனியார் தணிக்கையாளர்களால் மட்டுமே தணிக்கை செய்யப்படுகின்றன; சி.ஏ.ஜிக்கு இதில் நேரடிப் பங்கில்லை.",
        "tip_en": "RBI, SBI, LIC, and FCI have independent private audits; DVC, ONGC, and Air India (previously) involve CAG.",
        "tip_ta": "RBI, SBI, LIC ஆகியவை தனியார் தணிக்கைக்கு உட்பட்டவை; இவற்றில் சி.ஏ.ஜிக்கு வழக்கமான தணிக்கைப் பங்கு இல்லை.",
        "fact_en": "The reasoning is to preserve commercial agility, operational secrecy, and banking sector flexibility.",
        "fact_ta": "வணிக சுறுசுறுப்பு, செயல்பாட்டு ரகசியம் மற்றும் வங்கித் துறை நெகிழ்வுத்தன்மையைப் பாதுகாப்பதே இதன் நோக்கமாகும்."
    },
    # 14
    {
        "subtopic": "Section 20 of CAG (DPC) Act 1971 - Audit by Request",
        "stem_en": "Under Section 20 of the CAG (DPC) Act 1971, what condition must be satisfied before the CAG undertakes the audit of a body or authority not otherwise covered by the Act?",
        "stem_ta": "1971 ஆம் ஆண்டின் சி.ஏ.ஜி சட்டத்தின் பிரிவு 20-ன் கீழ், சட்டத்தில் குறிப்பிடப்படாத ஒரு அமைப்பின் தணிக்கையை சி.ஏ.ஜி மேற்கொள்வதற்கு முன் பூர்த்தி செய்யப்பட வேண்டிய நிபந்தனை என்ன?",
        "options": [
            ("President or Governor must request such audit in public interest, after consultation with the CAG and giving reasonable opportunity to the body", "சி.ஏ.ஜியுடன் கலந்தாலோசித்து, அவ்வமைப்பிற்கு நியாயமான வாய்ப்பளித்த பின்னர், பொது நலன் கருதி குடியரசுத் தலைவர் அல்லது ஆளுநர் கோர வேண்டும்"),
            ("The Chief Justice of India must issue a writ of mandamus directing the audit", "உச்ச நீதிமன்றத் தலைமை நீதிபதி தணிக்கைக்கு உத்தரவிட்டு பேராணை பிறப்பிக்க வேண்டும்"),
            ("The body must voluntarily deposit an audit fee equal to 10% of its annual budget", "அவ்வமைப்பு தனது ஆண்டு பட்ஜெட்டில் 10% தணிக்கைக் கட்டணமாக முன்வைப்பு செய்ய வேண்டும்"),
            ("Both Houses of Parliament must pass a constitutional amendment bill with a two-thirds majority", "நாடாளுமன்றத்தின் இரு அவைகளும் மூன்றில் இரண்டு பங்கு பெரும்பான்மையுடன் அரசியலமைப்புத் திருத்த மசோதாவை நிறைவேற்ற வேண்டும்")
        ],
        "exp_en": "Under Section 20(1) and 20(2), the President or Governor, after consultation with the CAG, may entrust audit of any body/authority not otherwise covered, provided reasonable opportunity is given to the body to make representations regarding why audit should not be entrusted.",
        "exp_ta": "பிரிவு 20-ன் படி, பொது நலன் கருதி குடியரசுத் தலைவர் அல்லது ஆளுநர், சி.ஏ.ஜியுடன் கலந்தாலோசித்து, சம்பந்தப்பட்ட அமைப்பிற்கு விளக்கம் அளிக்க வாய்ப்பளித்த பின்னரே தணிக்கையை ஒப்படைக்க முடியும்.",
        "tip_en": "Section 20 allows audit of local bodies, autonomous councils, or private concessionaires on executive request.",
        "tip_ta": "பிரிவு 20 உள்ளாட்சி அமைப்புகள் மற்றும் பிற வாரியங்களை நிர்வாகக் கோரிக்கையின் பேரில் தணிக்கை செய்ய வழிவகுக்கிறது.",
        "fact_en": "This is often used for entrusting audit of Panchayati Raj institutions and Urban Local Bodies under Technical Guidance and Supervision (TGS).",
        "fact_ta": "உள்ளாட்சி அமைப்புகளின் தணிக்கைக்கான தொழில்நுட்ப வழிகாட்டுதல் மற்றும் மேற்பார்வைக்கு (TGS) இது பெரும்பாலும் பயன்படுத்தப்படுகிறது."
    },
    # 15
    {
        "subtopic": "Public Accounts Committee (PAC) Mechanics",
        "stem_en": "In what specific technical capacity does the CAG participate in the sittings of the Public Accounts Committee (PAC)?",
        "stem_ta": "பொதுக் கணக்குக் குழுவின் (PAC) கூட்டங்களில் சி.ஏ.ஜி எந்த குறிப்பிட்ட தொழில்நுட்பத் தகுதியில் பங்கேற்கிறார்?",
        "options": [
            ("As an external expert and permanent invitee acting as 'friend, philosopher, and guide', assisting in witness examination without voting rights", "வாக்களிக்கும் உரிமையின்றி, சாட்சிகளை விசாரிக்க உதவும் 'நண்பர், தத்துவஞானி மற்றும் வழிகாட்டியாக' நிரந்தர அழைப்பாளராகப் பங்கேற்கிறார்"),
            ("As the ex-officio Chairman of the Public Accounts Committee with casting vote power", "முடிவு வாக்கு அதிகாரம் கொண்ட பொதுக் கணக்குக் குழுவின் அலுவல் வழித் தலைவராக"),
            ("As an accused witness who must defend the executive government's financial decisions", "அரசின் நிதி முடிவுகளை ஆதரித்துப் பேச வேண்டிய பிரதிவாதி சாட்சியாக"),
            ("As a silent courtroom stenographer recording verbatim minutes of the committee", "குழுவின் நடவடிக்கைகளை வார்த்தைக்கு வார்த்தை பதிவு செய்யும் நீதிமன்ற சுருக்கெழுத்தாளராக")
        ],
        "exp_en": "The CAG is not a member of PAC and has no voting rights, but attends PAC sittings by special invitation, briefing members on audit paragraphs, suggesting technical cross-examination questions, and explaining bureaucratic financial procedures.",
        "exp_ta": "சி.ஏ.ஜி குழுவின் உறுப்பினர் அல்ல, வாக்களிக்கும் உரிமையும் இல்லை; ஆனால் சிறப்பு அழைப்பாளராகக் கலந்துகொண்டு, தணிக்கைப் பத்திகளை விளக்கி, அதிகாரிகளிடம் கேள்வி கேட்க உறுப்பினர்களுக்கு வழிகாட்டுகிறார்.",
        "tip_en": "CAG attends PAC meetings as 'guide and philosopher', sitting by the side of the Chairman.",
        "tip_ta": "சி.ஏ.ஜி பொதுக் கணக்குக் குழுவின் தலைவருக்கு அருகில் அமர்ந்து வழிகாட்டியாகச் செயல்படுகிறார்.",
        "fact_en": "The PAC was first set up in 1921 under the Government of India Act 1919; since 1967, its chairman is traditionally from the Opposition.",
        "fact_ta": "பொதுக் கணக்குக் குழு 1921-ல் அமைக்கப்பட்டது; 1967 முதல் எதிர்க்கட்சி உறுப்பினர் ஒருவர் இதன் தலைவராக நியமிக்கப்படுகிறார்."
    },
    # 16
    {
        "subtopic": "Difference between CAG and British Comptroller",
        "stem_en": "Why is the Indian CAG often described by constitutional scholars as an 'Auditor General' rather than a true 'Comptroller', unlike his British counterpart?",
        "stem_ta": "பிரிட்டிஷ் தணிக்கையாளரைப் போலன்றி, இந்திய சி.ஏ.ஜியை அரசியலமைப்பு அறிஞர்கள் உண்மையான 'கட்டுப்பாட்டாளர்' (Comptroller) என்பதை விட வெறும் 'தணிக்கைத் தலைவர்' (Auditor General) என்று விவரிப்பது ஏன்?",
        "options": [
            ("Because the Indian CAG audits expenditure only post-facto (ex-post) and has no control over money issuance from the exchequer", "ஏனெனில் இந்திய சி.ஏ.ஜி பணம் கருவூலத்திலிருந்து வெளியேறிய பிறகே (பின் தணிக்கை) ஆய்வு செய்கிறார், பணம் வழங்கப்படுவதைக் கட்டுப்படுத்தும் அதிகாரம் இல்லை"),
            ("Because the Indian CAG is appointed for a fixed tenure, whereas the British Comptroller holds office during royal pleasure", "ஏனெனில் இந்திய சி.ஏ.ஜி குறிப்பிட்ட பதவிக்காலம் கொண்டவர், பிரிட்டிஷ் தணிக்கையாளர் மன்னரின் விருப்பம் வரை பதவியில் இருப்பவர்"),
            ("Because the Indian CAG cannot inspect military accounts under any statutory provision", "ஏனெனில் இந்திய சி.ஏ.ஜியால் எந்தவொரு சட்ட விதியின் கீழும் ராணுவக் கணக்குகளை ஆய்வு செய்ய முடியாது என்பதால்"),
            ("Because the British Comptroller is an elected member of the House of Commons", "ஏனெனில் பிரிட்டிஷ் தணிக்கையாளர் பொது அவையின் தேர்ந்தெடுக்கப்பட்ட உறுப்பினர் என்பதால்")
        ],
        "exp_en": "In Britain, executive agencies cannot withdraw a single penny from the Consolidated Fund without the prior approval and counter-signature of the Comptroller. In India, the executive withdraws money independently; CAG enters the picture only after the money has been spent (post-facto audit).",
        "exp_ta": "பிரிட்டனில், தணிக்கையாளரின் முன் அனுமதியின்றி கருவூலத்திலிருந்து ஒரு பைசா கூட எடுக்க முடியாது; ஆனால் இந்தியாவில், அரசுப் பணம் செலவிடப்பட்ட பின்னரே சி.ஏ.ஜி தணிக்கை செய்ய வருகிறார் (Ex-post audit).",
        "tip_en": "UK CAG: Ex-ante control (controls issuance of money). Indian CAG: Ex-post audit (scrutinizes expenditure after it occurs).",
        "tip_ta": "பிரிட்டன் சி.ஏ.ஜி: பணம் எடுக்கும் முன் கட்டுப்படுத்துகிறார். இந்திய சி.ஏ.ஜி: பணம் செலவிடப்பட்ட பின் தணிக்கை செய்கிறார்.",
        "fact_en": "K. Santhanam noted in the Constituent Assembly that using the word 'Comptroller' in India was technically inaccurate.",
        "fact_ta": "கே. சந்தானம் இந்தியச் சூழலில் 'கண்ட்ரோலர்' (Comptroller) என்ற வார்த்தை தொழில்நுட்ப ரீதியாகப் பொருந்தாது என்று சுட்டிக்காட்டினார்."
    },
    # 17
    {
        "subtopic": "Audit of Secret Service Expenditure",
        "stem_en": "How is the CAG's audit jurisdiction restricted regarding 'Secret Service Expenditure' incurred by intelligence and security agencies?",
        "stem_ta": "உளவுத்துறை மற்றும் பாதுகாப்பு அமைப்புகளால் செய்யப்படும் 'ரகசிய சேவைச் செலவினங்கள்' (Secret Service Expenditure) மீதான சி.ஏ.ஜியின் தணிக்கை அதிகாரம் எவ்வாறு கட்டுப்படுத்தப்பட்டுள்ளது?",
        "options": [
            ("CAG cannot call for detailed vouchers, but must accept a certificate from the competent administrative authority confirming expenditure", "சி.ஏ.ஜி விரிவான ரசீதுகளைக் கோர முடியாது, மாறாக தகுதிவாய்ந்த நிர்வாக அதிகாரி அளிக்கும் சான்றிதழை மட்டுமே ஏற்றுக்கொள்ள வேண்டும்"),
            ("CAG conducts open public hearings to reveal names of undercover intelligence operatives", "சி.ஏ.ஜி உளவுத்துறை அதிகாரிகளின் பெயர்களை வெளிப்படுத்த பகிரங்க பொது விசாரணைகளை நடத்துகிறார்"),
            ("Secret service expenditure is completely illegal and cannot be reflected in any audit report", "ரகசிய சேவைச் செலவு முற்றிலும் சட்டவிரோதமானது மற்றும் எந்தவொரு தணிக்கை அறிக்கையிலும் இடம்பெற முடியாது"),
            ("CAG personally accompanies intelligence officers on foreign covert operations to verify cash payments", "ரொக்கக் கொடுப்பனவுகளைச் சரிபார்க்க வெளிநாட்டு ரகசிய நடவடிக்கைகளில் உளவுத்துறை அதிகாரிகளுடன் சி.ஏ.ஜி நேரில் செல்கிறார்")
        ],
        "exp_en": "In respect of secret service expenditure (e.g., IB, RAW), the CAG does not inspect individual vouchers. Instead, audit accepts a certificate from the competent administrative authority (e.g., Ministry/Department Secretary) specifying that the money was actually spent under proper authority.",
        "exp_ta": "ரகசிய சேவைச் செலவினங்களில் (IB, RAW போன்றவை), சி.ஏ.ஜி விரிவான ரசீதுகளை ஆய்வு செய்வதில்லை; மாறாக உரிய தகுதிவாய்ந்த செயலாளர் அளிக்கும் அதிகாரப்பூர்வ சான்றிதழை ஏற்றுக்கொள்கிறார்.",
        "tip_en": "Secret service audit: Administrative certificate accepted without demanding underlying intelligence vouchers.",
        "tip_ta": "ரகசிய சேவைத் தணிக்கை: ரகசிய ரசீதுகளைக் கோராமல் நிர்வாகச் சான்றிதழ் ஏற்றுக்கொள்ளப்படுகிறது.",
        "fact_en": "This limitation is standard across democratic nations to protect national security sources and intelligence methods.",
        "fact_ta": "தேசியப் பாதுகாப்பு ரகசியங்களைப் பாதுகாக்க அனைத்து ஜனநாயக நாடுகளிலும் இந்த விலக்கு வழக்கத்தில் உள்ளது."
    },
    # 18
    {
        "subtopic": "Article 148(4) Post-Retirement Bar Scope",
        "stem_en": "Under Article 148(4), what is the exact constitutional restriction imposed upon a person who has held office as the CAG?",
        "stem_ta": "சரத்து 148(4)-ன் கீழ், சி.ஏ.ஜி பதவியை வகித்த ஒரு நபர் மீது விதிக்கப்பட்டுள்ள துல்லியமான அரசியலமைப்புத் தடை என்ன?",
        "options": [
            ("Ineligible for any further office either under the Government of India or under the Government of any State", "இந்திய அரசின் கீழோ அல்லது எந்தவொரு மாநில அரசின் கீழோ மேற்கொண்டு எந்தவொரு பதவியையும் வகிக்கத் தகுதியற்றவர்"),
            ("Barred only from contesting Lok Sabha elections for a cooling-off period of 5 years", "5 ஆண்டுகள் வரை மக்களவைத் தேர்தலில் போட்டியிட மட்டுமே தடை விதிக்கப்பட்டுள்ளது"),
            ("Ineligible only for judicial appointments in the Supreme Court or High Courts", "உச்ச அல்லது உயர் நீதிமன்றங்களில் நீதித்துறை நியமனங்களுக்கு மட்டுமே தகுதியற்றவர்"),
            ("Permitted to accept governorships or ambassadorial roles with prior Prime Ministerial clearance", "பிரதமரின் முன் அனுமதியுடன் ஆளுநர் அல்லது தூதர் பதவிகளை ஏற்க அனுமதிக்கப்படுவார்")
        ],
        "exp_en": "Article 148(4) explicitly provides: 'The Comptroller and Auditor-General shall not be eligible for further office either under the Government of India or under the Government of any State after he has ceased to hold his office.'",
        "exp_ta": "சரத்து 148(4)-ன் படி: 'தலைமைத் தணிக்கையாளர் தமது பதவிக்காலம் முடிந்த பின்னர், இந்திய அரசிலோ அல்லது எந்தவொரு மாநில அரசிலோ எவ்விதப் பதவியையும் வகிக்கத் தகுதியற்றவர் ஆவார்.'",
        "tip_en": "Article 148(4) is an absolute constitutional bar against further government employment to ensure fearless auditing.",
        "tip_ta": "பயமின்றித் தணிக்கை செய்வதை உறுதிப்படுத்த சரத்து 148(4) அரசு மறுபதவிக்கு முழுமையான தடை விதிக்கிறது.",
        "fact_en": "However, this bar does not prevent appointment to ad-hoc enquiry commissions or international organizations like the UN.",
        "fact_ta": "இருப்பினும், விசாரணைக் குழுக்கள் அல்லது ஐ.நா. போன்ற சர்வதேச அமைப்புகளில் நியமிக்கப்படுவதை இது தடுக்காது."
    },
    # 19
    {
        "subtopic": "Section 13 of CAG (DPC) Act 1971 - Audit of Expenditure",
        "stem_en": "Under Section 13 of the CAG (DPC) Act 1971, which three essential duties must the CAG perform regarding expenditure from the Consolidated Fund?",
        "stem_ta": "1971 ஆம் ஆண்டின் சி.ஏ.ஜி சட்டத்தின் பிரிவு 13-ன் கீழ், திரட்டப்பட்ட நிதியிலிருந்து செய்யப்படும் செலவினங்கள் தொடர்பாக சி.ஏ.ஜி ஆற்ற வேண்டிய மூன்று அத்தியாவசிய கடமைகள் எவை?",
        "options": [
            ("Audit that moneys disbursed were legally available, applicable to the service, and conformed to the governing authority", "வழங்கப்பட்ட நிதி சட்டப்படி கிடைக்கத்தக்கதாக இருந்தது, குறிப்பிட்ட சேவைக்குரியது மற்றும் உரிய விதிகளுக்கு உட்பட்டது என்பதைத் தணிக்கை செய்தல்"),
            ("Sanction advance loans to state governments, invest excess funds in stock markets, and print currency notes", "மாநிலங்களுக்கு முன்பணக் கடன்களை அனுமதித்தல், உபரி நிதியை பங்குச்சந்தையில் முதலீடு செய்தல் மற்றும் ரூபாய் நோட்டுகளை அச்சிடுதல்"),
            ("Draft executive procurement tenders, approve winning contractors, and disburse electronic payments", "அரசு ஒப்பந்தப் புள்ளிகளை வரைதல், ஒப்பந்ததாரர்களுக்கு ஒப்புதல் அளித்தல் மற்றும் மின்னணு முறையில் பணம் செலுத்துதல்"),
            ("Set corporate income tax rates, collect GST at border ports, and manage customs warehouses", "நிறுவன வருமான வரி விகிதங்களை நிர்ணயித்தல், எல்லைகளில் ஜி.எஸ்.டி வசூலித்தல் மற்றும் சுங்கக் கிடங்குகளை நிர்வகித்தல்")
        ],
        "exp_en": "Section 13 mandates CAG to audit: (1) whether moneys shown in accounts as disbursed were legally available, (2) whether expenditure conformed to the authority governing it, and (3) whether every re-appropriation conformed to authorized rules.",
        "exp_ta": "பிரிவு 13-ன் படி சி.ஏ.ஜி: (1) செலவிடப்பட்ட பணம் சட்டப்படி ஒதுக்கப்பட்டதா, (2) உரிய அதிகாரியின் ஒப்புதலுடன் விதிகளின்படி செலவிடப்பட்டதா, (3) நிதி மறுஒதுக்கீடு முறையான விதிகளின்படி செய்யப்பட்டதா என்பதைத் தணிக்கை செய்ய வேண்டும்.",
        "tip_en": "Section 13 forms the bedrock of legal/regularity audit of all expenditures from Consolidated Funds.",
        "tip_ta": "பிரிவு 13 திரட்டப்பட்ட நிதியிலிருந்து செய்யப்படும் அனைத்து செலவுகளின் சட்டரீதியான தணிக்கைக்கு அடிப்படையாகும்.",
        "fact_en": "This applies equally to the Consolidated Fund of India, each State, and each Union Territory with a legislative assembly.",
        "fact_ta": "இது மத்திய அரசு, மாநிலங்கள் மற்றும் சட்டமன்றம் கொண்ட யூனியன் பிரதேசங்களின் திரட்டப்பட்ட நிதிகளுக்குப் பொருந்தும்."
    },
    # 20
    {
        "subtopic": "Section 16 - Audit of Receipts",
        "stem_en": "Why is Section 16 of the CAG (DPC) Act 1971 considered a critical safeguard for the financial health of the exchequer?",
        "stem_ta": "1971 ஆம் ஆண்டின் சி.ஏ.ஜி சட்டத்தின் பிரிவு 16, அரசு கருவூலத்தின் நிதி ஆரோக்கியத்திற்கான மிக முக்கியமான பாதுகாப்பாகக் கருதப்படுவது ஏன்?",
        "options": [
            ("It empowers the CAG to audit all receipts of taxes, duties, and revenues to satisfy himself that rules ensure effective collection", "வரிகள், தீர்வைகள் மற்றும் அனைத்து வருவாய் வரவுகளையும் தணிக்கை செய்து, விதிகள் பயனுள்ள வசூலை உறுதி செய்கின்றனவா என ஆராய சி.ஏ.ஜிக்கு அதிகாரம் அளிக்கிறது"),
            ("It allows the CAG to collect personal income tax directly from citizens during house-to-house raids", "வீடு வீடாகச் சென்று குடிமக்களிடமிருந்து நேரடியாக வருமான வரியை வசூலிக்க சி.ஏ.ஜிக்கு அதிகாரம் அளிக்கிறது"),
            ("It authorizes the CAG to waive corporate debts owed to scheduled commercial banks", "வணிக வங்கிகளுக்குச் செலுத்த வேண்டிய கார்ப்பரேட் கடன்களைத் தள்ளுபடி செய்ய சி.ஏ.ஜிக்கு அதிகாரம் அளிக்கிறது"),
            ("It makes the CAG the chief revenue officer with powers to attach movable property of tax defaulters", "வரி செலுத்தாதவர்களின் அசையும் சொத்துக்களைப் பறிமுதல் செய்யும் தலைமை வருவாய் அதிகாரியாக சி.ஏ.ஜியை மாற்றுகிறது")
        ],
        "exp_en": "Under Section 16, the CAG audits all receipts payable into the Consolidated Fund of India and of the States to check that rules and procedures are designed to secure an effective check on the assessment, collection, and proper allocation of revenue.",
        "exp_ta": "பிரிவு 16-ன் கீழ், திரட்டப்பட்ட நிதிக்குச் சேர வேண்டிய அனைத்து வரவுகளையும் சி.ஏ.ஜி தணிக்கை செய்து, மதிப்பீடு, வசூல் மற்றும் நிதி ஒதுக்கீடு ஆகியவை திறம்பட நடைபெறுவதை உறுதி செய்யும் விதிகள் உள்ளதா என்பதைச் சோதிக்கிறார்.",
        "tip_en": "Section 16: Audit of Receipts (Customs, Direct Taxes, GST, royalties, non-tax revenues).",
        "tip_ta": "பிரிவு 16: வரவுத் தணிக்கை (நேரடி வரிகள், சுங்கம், ஜி.எஸ்.டி, ராயல்டி மற்றும் வரி அல்லாத வரவுகள்).",
        "fact_en": "Audit of receipts covers systemic under-assessments, undue tax exemptions, and evasion leakages.",
        "fact_ta": "வரவுத் தணிக்கை முறையற்ற வரி விலக்குகள் மற்றும் வரி ஏய்ப்பு கசிவுகளை வெளிக்கொணர்கிறது."
    },
    # 21
    {
        "subtopic": "Audit of Stores and Stock (Section 17)",
        "stem_en": "Under Section 17 of the CAG (DPC) Act 1971, what is the CAG empowered to audit regarding government inventories?",
        "stem_ta": "1971 ஆம் ஆண்டின் சி.ஏ.ஜி சட்டத்தின் பிரிவு 17-ன் கீழ், அரசு இருப்புகள் மற்றும் சரக்குகள் தொடர்பாக சி.ஏ.ஜி எதனைத் தணிக்கை செய்ய அதிகாரம் பெற்றுள்ளார்?",
        "options": [
            ("Accounts of stores and stock kept in any office or department of the Union or of a State", "மத்திய அல்லது மாநில அரசின் எந்தவொரு அலுவலகம் அல்லது துறையிலும் வைக்கப்பட்டுள்ள சரக்குகள் மற்றும் இருப்புக் கணக்குகள்"),
            ("Physical retail grocery stores operating in private shopping malls", "தனியார் வணிக வளாகங்களில் இயங்கும் மளிகைக் கடைகளின் சரக்குகள்"),
            ("Gold ornaments held in private family bank lockers across the country", "நாடெங்கிலும் உள்ள குடும்பங்களின் தனியார் வங்கி லாக்கர்களில் உள்ள தங்க நகைகள்"),
            ("Agricultural grain reserves stored exclusively on private overseas farms", "வெளிநாட்டுத் தனியார் பண்ணைகளில் சேமிக்கப்பட்டுள்ள விவசாய தானிய இருப்புகள்")
        ],
        "exp_en": "Section 17 provides that the CAG shall have authority to audit and report on the accounts of stores and stock kept in any office or department of the Union or of a State, ensuring inventory control, avoiding obsolescence, and detecting pilferage.",
        "exp_ta": "பிரிவு 17-ன் படி, மத்திய அல்லது மாநில அரசு அலுவலகங்கள் மற்றும் துறைகளில் உள்ள சரக்குகள் மற்றும் இருப்புக் கணக்குகளைத் தணிக்கை செய்து அறிக்கை அளிக்க சி.ஏ.ஜிக்கு முழு அதிகாரம் உண்டு.",
        "tip_en": "Section 17: Audit of Stores and Stock (defence hardware, railway assets, medical inventory).",
        "tip_ta": "பிரிவு 17: சரக்குகள் மற்றும் இருப்புக் கணக்குகள் தணிக்கை (பாதுகாப்புத் தளவாடங்கள், ரயில்வே மற்றும் மருத்துவப் பொருட்கள்).",
        "fact_en": "Stores audit exposes surplus inventory hoarding, expired medicines, and unauthorized write-offs.",
        "fact_ta": "சரக்குத் தணிக்கை காலாவதியான மருந்துகள் மற்றும் தேவையின்றி பொருட்கள் தேக்கி வைக்கப்படுவதை வெளிப்படுத்துகிறது."
    },
    # 22
    {
        "subtopic": "Section 15 - Audit of Grants or Loans for Specific Purpose",
        "stem_en": "When a grant or loan is given from the Consolidated Fund to any body for a specific purpose, what is CAG's mandate under Section 15 of the 1971 Act?",
        "stem_ta": "திரட்டப்பட்ட நிதியிலிருந்து ஒரு குறிப்பிட்ட நோக்கத்திற்காக ஏதேனும் ஓர் அமைப்பிற்கு மானியம் அல்லது கடன் வழங்கப்படும் போது, 1971 சட்டத்தின் பிரிவு 15-ன் கீழ் சி.ஏ.ஜியின் பணி என்ன?",
        "options": [
            ("Scrutinize the procedures by which the sanctioning authority satisfies itself as to the fulfillment of loan/grant conditions", "கடன்/மானிய நிபந்தனைகள் நிறைவேற்றப்பட்டதா என்பதை அனுமதி வழங்கும் அதிகாரம் எவ்வாறு உறுதி செய்கிறது என்ற நடைமுறைகளை ஆய்வு செய்தல்"),
            ("Directly manage the board of directors of the borrowing private corporation", "கடன் வாங்கும் தனியார் நிறுவனத்தின் இயக்குநர் குழுவை நேரடியாக நிர்வகித்தல்"),
            ("Foreclose mortgages and auction physical property without civil court decrees", "சிவில் நீதிமன்ற ஆணையின்றி அடமானங்களை முடக்கி சொத்துக்களை ஏலம் விடுதல்"),
            ("Convert unpaid government loans automatically into sovereign equity shares", "செலுத்தப்படாத அரசு கடன்களை தானாகவே அரசின் சமபங்குகளாக மாற்றுதல்")
        ],
        "exp_en": "Section 15 empowers CAG to scrutinize the procedures by which the sanctioning authority satisfies itself as to the fulfillment of conditions on which grants/loans were given, and inspect the books and accounts of the recipient body with right of access.",
        "exp_ta": "பிரிவு 15-ன் கீழ், எந்த நிபந்தனைகளின் கீழ் கடன்/மானியம் வழங்கப்பட்டதோ அவை பூர்த்தி செய்யப்பட்டுள்ளனவா என்பதை அனுமதித்த அதிகாரம் எவ்வாறு சரிபார்க்கிறது என்பதை சி.ஏ.ஜி ஆய்வு செய்கிறார்.",
        "tip_en": "Section 15: Tracking end-use of specific-purpose grants and loans.",
        "tip_ta": "பிரிவு 15: குறிப்பிட்ட நோக்கத்திற்கான மானியங்கள் மற்றும் கடன்களின் இறுதிப் பயன்பாட்டைக் கண்காணித்தல்.",
        "fact_en": "CAG can inspect the accounts of recipient bodies unless the body is specifically exempted under the proviso.",
        "fact_ta": "குறிப்பிட்ட விலக்கு அளிக்கப்படாத வரை, மானியம் பெறும் அமைப்புகளின் கணக்குகளை சி.ஏ.ஜி ஆய்வு செய்யலாம்."
    },
    # 23
    {
        "subtopic": "Section 21 - Delegation of Powers",
        "stem_en": "Under Section 21 of the CAG (DPC) Act 1971, how are the constitutional and statutory powers of the CAG delegated to subordinates?",
        "stem_ta": "1971 ஆம் ஆண்டின் சி.ஏ.ஜி சட்டத்தின் பிரிவு 21-ன் கீழ், சி.ஏ.ஜியின் அரசியலமைப்பு மற்றும் சட்டப்பூர்வ அதிகாரங்கள் துணை அதிகாரிகளுக்கு எவ்வாறு வழங்கப்படுகின்றன?",
        "options": [
            ("Exercisable by any officer of the Indian Audit and Accounts Department authorized by the CAG by general or special order", "பொது அல்லது சிறப்பு ஆணை மூலம் சி.ஏ.ஜியால் அங்கீகரிக்கப்பட்ட இந்திய தணிக்கை மற்றும் கணக்குத் துறையின் எந்தவொரு அதிகாரியாலும் செயல்படுத்தப்படலாம்"),
            ("Delegable exclusively to the Cabinet Secretary with written permission from the Chief Justice", "தலைமை நீதிபதியின் எழுத்துப்பூர்வ அனுமதியுடன் அமைச்சரவைச் செயலாளருக்கு மட்டுமே வழங்கப்பட முடியும்"),
            ("All powers must be exercised strictly and personally by the individual holding the CAG post", "அனைத்து அதிகாரங்களையும் சி.ஏ.ஜி பதவியில் உள்ள தனிநபர் மட்டுமே நேரடியாகவும் நேரில் மட்டுமே செயல்படுத்த வேண்டும்"),
            ("Delegable only to elected Members of the Public Accounts Committee", "பொதுக் கணக்குக் குழுவின் தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்களுக்கு மட்டுமே வழங்கப்பட முடியும்")
        ],
        "exp_en": "Section 21 states that any power exercisable by the CAG may be exercised by such officer of his department as may be authorized by him by general or special order, enabling the institutional functioning of the Indian Audit and Accounts Department (IA&AD).",
        "exp_ta": "பிரிவு 21-ன் படி, சி.ஏ.ஜிக்கு உள்ள எந்தவொரு அதிகாரமும், அவரால் பொது அல்லது சிறப்பு ஆணை மூலம் அங்கீகரிக்கப்பட்ட இந்திய தணிக்கை மற்றும் கணக்குத் துறை அதிகாரியால் செயல்படுத்தப்படலாம்.",
        "tip_en": "Section 21 empowers Principal Accountants General (PAGs) and Directors General to exercise statutory audit powers.",
        "tip_ta": "பிரிவு 21 முதன்மை கணக்குத் தலைவர்கள் (PAGs) மற்றும் இயக்குநர்களுக்கு தணிக்கை அதிகாரங்களைச் செயல்படுத்த அதிகாரம் அளிக்கிறது.",
        "fact_en": "However, the final annual audit reports submitted to the President/Governors are authenticated under the personal authority of the CAG.",
        "fact_ta": "இருப்பினும், குடியரசுத் தலைவர்/ஆளுநர்களுக்கு சமர்ப்பிக்கப்படும் இறுதி அறிக்கைகள் சி.ஏ.ஜியின் அதிகாரத்தின் கீழ் உறுதிப்படுத்தப்படுகின்றன."
    },
    # 24
    {
        "subtopic": "Section 23 - Regulation Making Power",
        "stem_en": "What statutory power is conferred on the CAG under Section 23 of the CAG (DPC) Act 1971?",
        "stem_ta": "1971 ஆம் ஆண்டின் சி.ஏ.ஜி சட்டத்தின் பிரிவு 23-ன் கீழ் சி.ஏ.ஜிக்கு வழங்கப்பட்டுள்ள சட்டப்பூர்வ அதிகாரம் எது?",
        "options": [
            ("Power to make regulations for carrying into effect the provisions of the Act relating to audit and compilation of accounts", "தணிக்கை மற்றும் கணக்குகளைத் தொகுப்பது தொடர்பான சட்டத்தின் விதிகளைச் செயல்படுத்த ஒழுங்குமுறைகளை (Regulations) உருவாக்கும் அதிகாரம்"),
            ("Power to declare financial emergency in defaulting states without consulting the Union", "மத்திய அரசைக் கலந்தாலோசிக்காமல் நிதி குறைபாடுள்ள மாநிலங்களில் நிதி அவசரநிலையை அறிவிக்கும் அதிகாரம்"),
            ("Power to impose punitive fines directly on non-compliant IAS officers", "விதிமீறும் ஐ.ஏ.எஸ் அதிகாரிகள் மீது நேரடியாக அபராதம் விதிக்கும் அதிகாரம்"),
            ("Power to write the annual confidential appraisal reports of Union Ministers", "மத்திய அமைச்சர்களின் வருடாந்திர ரகசிய மதிப்பீட்டு அறிக்கைகளை எழுதும் அதிகாரம்")
        ],
        "exp_en": "Section 23 empowers the CAG to make regulations for carrying into effect the provisions of the Act regarding the scope and extent of audit. Under this, the 'Regulations on Audit and Accounts, 2007' (updated in 2020) were promulgated.",
        "exp_ta": "பிரிவு 23 சி.ஏ.ஜிக்கு தணிக்கையின் எல்லை மற்றும் நடைமுறைகள் தொடர்பான சட்டப் பிரிவுகளைச் செயல்படுத்த விதிமுறைகளை (Regulations) உருவாக்க அதிகாரம் அளிக்கிறது; இதன் கீழ் 2007 மற்றும் 2020 தணிக்கை ஒழுங்குமுறைகள் வெளியிடப்பட்டன.",
        "tip_en": "Regulations on Audit and Accounts (2007/2020) derive their statutory force from Section 23 of the 1971 Act.",
        "tip_ta": "2007/2020 தணிக்கை ஒழுங்குமுறைகள் 1971 சட்டத்தின் பிரிவு 23-லிருந்து தங்கள் சட்டப்பூர்வ சக்தியைப் பெறுகின்றன.",
        "fact_en": "Section 22 gives the Central Government the power to make rules in consultation with the CAG.",
        "fact_ta": "பிரிவு 22 மத்திய அரசுக்கு சி.ஏ.ஜியைக் கலந்தாலோசித்து விதிகளை (Rules) உருவாக்க அதிகாரம் அளிக்கிறது."
    },
    # 25
    {
        "subtopic": "Role in Article 279 - Net Proceeds Certification",
        "stem_en": "Under Article 279(1) of the Constitution, what is the legal weight of the CAG's certificate regarding the calculation of the 'net proceeds' of any tax or duty?",
        "stem_ta": "அரசியலமைப்புச் சட்டம் சரத்து 279(1)-ன் கீழ், ஏதேனும் ஒரு வரி அல்லது தீர்வை வசூலின் 'நிகர வருமானம்' (Net Proceeds) கணக்கீடு குறித்த சி.ஏ.ஜியின் சான்றிதழின் சட்டப்பூர்வ அந்தஸ்து என்ன?",
        "options": [
            ("It is final, conclusive, and binding on both the Union and the States", "இது இறுதியானது, அறுதியானது மற்றும் மத்திய மற்றும் மாநில அரசுகள் இரண்டையுமே கட்டுப்படுத்தக்கூடியது"),
            ("It is merely an advisory opinion that can be overruled by an executive notification of the Finance Ministry", "இது வெறும் ஆலோசனை மட்டுமே; நிதி அமைச்சகத்தின் நிர்வாக அறிவிக்கை மூலம் இதை நிராகரிக்க முடியும்"),
            ("It must be ratified by a two-thirds majority in the Rajya Sabha within 30 days", "இது 30 நாட்களுக்குள் மாநிலங்களவையில் மூன்றில் இரண்டு பங்கு பெரும்பான்மையுடன் அங்கீகரிக்கப்பட வேண்டும்"),
            ("It is subject to annual judicial appeal before the Armed Forces Tribunal", "இது ஆயுதப்படைகள் தீர்ப்பாயத்தின் முன் வருடாந்திர நீதித்துறை மேல்முறையீட்டிற்கு உட்பட்டது")
        ],
        "exp_en": "Article 279(1) explicitly provides: 'the net proceeds of any tax or duty... shall be ascertained and certified by the Comptroller and Auditor-General of India, whose certificate shall be final.' This ensures federal trust in devolution of tax revenues.",
        "exp_ta": "சரத்து 279(1)-ன் படி, எந்தவொரு வரி அல்லது தீர்வையின் நிகர வருவாயும் சி.ஏ.ஜியால் கணக்கிடப்பட்டு சான்றளிக்கப்பட வேண்டும்; மேலும் அந்த சான்றிதழ் 'இறுதியானது' (final and conclusive) ஆகும்.",
        "tip_en": "Net proceeds under Article 279: CAG's certificate is completely final and unquestionable.",
        "tip_ta": "சரத்து 279-ன் கீழ் நிகர வருவாய்: சி.ஏ.ஜியின் சான்றிதழ் இறுதியானது மற்றும் யாராலும் கேள்வி கேட்க முடியாது.",
        "fact_en": "Net proceeds means gross tax proceeds minus the cost of collection.",
        "fact_ta": "நிகர வருமானம் என்பது மொத்த வரி வசூலில் இருந்து வசூல் செய்வதற்கான செலவினங்களைக் கழித்த தொகையாகும்."
    },
    # 26
    {
        "subtopic": "Local Bodies & Technical Guidance and Supervision (TGS)",
        "stem_en": "Under the recommendations of the Eleventh and successive Finance Commissions, what is the CAG's role in the audit of Panchayati Raj Institutions and Urban Local Bodies?",
        "stem_ta": "பதினோராவது மற்றும் அதனைத் தொடர்ந்த நிதி ஆணையங்களின் பரிந்துரைகளின்படி, பஞ்சாயத்து ராஜ் மற்றும் நகர்ப்புற உள்ளாட்சி அமைப்புகளின் தணிக்கையில் சி.ஏ.ஜியின் பங்கு என்ன?",
        "options": [
            ("Providing Technical Guidance and Supervision (TGS) to State Local Fund Audit departments and placing consolidated reports", "மாநில உள்ளாட்சி நிதி தணிக்கைத் துறைகளுக்கு தொழில்நுட்ப வழிகாட்டுதல் மற்றும் மேற்பார்வை (TGS) வழங்குதல் மற்றும் ஒருங்கிணைந்த அறிக்கைகளை சமர்ப்பித்தல்"),
            ("Personally auditing all 2.5 lakh gram panchayats voucher-by-voucher each month", "ஒவ்வொரு மாதமும் அனைத்து 2.5 லட்சம் கிராம பஞ்சாயத்துகளையும் நேரில் சென்று ரசீது வாரியாக தணிக்கை செய்தல்"),
            ("Directly appointing village panchayat ward members through competitive exams", "போட்டித் தேர்வுகள் மூலம் கிராம பஞ்சாயத்து வார்டு உறுப்பினர்களை நேரடியாக நியமித்தல்"),
            ("Dissolving municipal corporations that fail to collect property taxes", "சொத்து வரி வசூலிக்கத் தவறும் மாநகராட்சிகளைக் கலைத்தல்")
        ],
        "exp_en": "Under Technical Guidance and Supervision (TGS) entrusted under Section 20, CAG establishes standard accounting and auditing guidelines for State Local Fund Audit departments, conducts test-checks, and presents an annual technical report to the State Legislature.",
        "exp_ta": "பிரிவு 20-ன் கீழ் TGS திட்டத்தின் மூலம், சி.ஏ.ஜி மாநில உள்ளாட்சி நிதி தணிக்கைத் துறைகளுக்கு வழிகாட்டுதல்களை வழங்குகிறார், மாதிரி தணிக்கை நடத்துகிறார் மற்றும் மாநில சட்டமன்றத்தில் அறிக்கையை சமர்ப்பிக்கிறார்.",
        "tip_en": "TGS = Technical Guidance and Supervision over Local Fund Audit of Panchayats and Municipalities.",
        "tip_ta": "TGS = பஞ்சாயத்து மற்றும் நகராட்சி உள்ளாட்சி நிதி தணிக்கை மீதான தொழில்நுட்ப வழிகாட்டுதல் மற்றும் மேற்பார்வை.",
        "fact_en": "Local bodies audit comes under the Examiner of Local Fund Accounts in states, supervised by CAG under TGS.",
        "fact_ta": "மாநிலங்களில் உள்ள உள்ளாட்சி நிதி கணக்குத் தணிக்கையாளர் சி.ஏ.ஜியின் TGS மேற்பார்வையின் கீழ் இயங்குகிறார்."
    },
    # 27
    {
        "subtopic": "CAG Audit of Environmental Compliance",
        "stem_en": "What is the specialized focus of CAG's 'Environmental Audits' conducted in recent decades?",
        "stem_ta": "சமீபத்திய தசாப்தங்களில் சி.ஏ.ஜியால் நடத்தப்படும் 'சுற்றுச்சூழல் தணிக்கைகளின்' (Environmental Audits) சிறப்பு நோக்கம் என்ன?",
        "options": [
            ("Evaluating governmental compliance with environmental statutes, wildlife conservation schemes, and river cleaning funds (e.g., Namami Gange)", "சுற்றுச்சூழல் சட்டங்கள், வனவிலங்குப் பாதுகாப்புத் திட்டங்கள் மற்றும் நதி தூய்மைப்படுத்தும் நிதிகளின் (எ.கா. நமாமி கங்கா) செயல்பாட்டை மதிப்பீடு செய்தல்"),
            ("Directly planting trees along national highways using audit staff", "தணிக்கைப் பணியாளர்களைக் கொண்டு தேசிய நெடுஞ்சாலைகளில் நேரடியாக மரங்களை நடுதல்"),
            ("Imposing carbon taxes on individual households exceeding electricity quotas", "மின்சார வரம்பை மீறும் தனிநபர் வீடுகளுக்கு கார்பன் வரி விதித்தல்"),
            ("Operating weather forecasting satellites under the Ministry of Earth Sciences", "புவி அறிவியல் அமைச்சகத்தின் கீழ் வானிலை முன்னறிவிப்பு செயற்கைக்கோள்களை இயக்குதல்")
        ],
        "exp_en": "CAG conducts environmental performance audits on air quality programmes, National Clean Energy Fund, Namami Gange, plastic waste management, and coastal zone regulations, evaluating whether funds achieve statutory ecological benchmarks.",
        "exp_ta": "காற்றுத் தரம், தேசிய தூய எரிசக்தி நிதி, நமாமி கங்கா, பிளாஸ்டிக் கழிவு மேலாண்மை மற்றும் கடலோர ஒழுங்குமுறை மண்டலங்கள் ஆகியவற்றில் நிதி ஒதுக்கீடுகள் சுற்றுச்சூழல் இலக்குகளை அடைந்துள்ளனவா என்பதை சி.ஏ.ஜி மதிப்பீடு செய்கிறது.",
        "tip_en": "CAG has a dedicated International Centre for Environment Audit and Sustainable Development (iCED) in Jaipur.",
        "tip_ta": "சுற்றுச்சூழல் தணிக்கைக்காக ஜெய்ப்பூரில் iCED என்ற சர்வதேச மையத்தை சி.ஏ.ஜி நிறுவியுள்ளார்.",
        "fact_en": "The Jaipur iCED facility is certified as a global training hub by INTOSAI's Working Group on Environmental Auditing (WGEA).",
        "fact_ta": "ஜெய்ப்பூர் iCED மையம் INTOSAI-யின் சுற்றுச்சூழல் தணிக்கைக் குழுவால் உலகளாவிய பயிற்சி மையமாக அங்கீகரிக்கப்பட்டுள்ளது."
    },
    # 28
    {
        "subtopic": "International Roles: UN Board of Auditors",
        "stem_en": "In what prominent multilateral capacity has the CAG of India repeatedly served on the international stage?",
        "stem_ta": "சர்வதேச அரங்கில் இந்திய சி.ஏ.ஜி எந்த முக்கிய பன்முகத் தகுதியில் மீண்டும் மீண்டும் பணியாற்றியுள்ளார்?",
        "options": [
            ("As Member and Chairman of the United Nations Board of Auditors and External Auditor of WHO, FAO, and IAEA", "ஐக்கிய நாடுகள் தணிக்கையாளர் வாரியத்தின் உறுப்பினர்/தலைவர் மற்றும் WHO, FAO, IAEA ஆகியவற்றின் வெளித் தணிக்கையாளராக"),
            ("As Chief Justice of the International Court of Justice (ICJ) in The Hague", "தி ஹேக்கில் உள்ள சர்வதேச நீதிமன்றத்தின் (ICJ) தலைமை நீதிபதியாக"),
            ("As President of the World Bank Group headquartered in Washington D.C.", "வாஷிங்டன் டி.சி.யில் உள்ள உலக வங்கி குழுமத்தின் தலைவராக"),
            ("As Secretary-General of the United Nations General Assembly", "ஐக்கிய நாடுகள் பொதுச் சபையின் பொதுச் செயலாளராக")
        ],
        "exp_en": "The CAG of India has repeatedly been elected to the UN Board of Auditors and has served as the external auditor for specialized UN agencies including the World Health Organization (WHO), Food and Agriculture Organization (FAO), and International Atomic Energy Agency (IAEA).",
        "exp_ta": "இந்திய சி.ஏ.ஜி ஐ.நா தணிக்கையாளர் வாரியத்திற்கு தேர்ந்தெடுக்கப்பட்டு, உலக சுகாதார நிறுவனம் (WHO), உணவு மற்றும் வேளாண்மை அமைப்பு (FAO) மற்றும் சர்வதேச அணுசக்தி முகமை (IAEA) ஆகியவற்றின் வெளித் தணிக்கையாளராகப் பணியாற்றியுள்ளார்.",
        "tip_en": "India's CAG enjoys immense international credibility as external auditor to major UN institutions.",
        "tip_ta": "முக்கிய ஐ.நா அமைப்புகளின் வெளித் தணிக்கையாளராக இந்திய சி.ஏ.ஜி உலகளாவிய நற்பெயரைக் கொண்டுள்ளார்.",
        "fact_en": "The UN Board of Auditors consists of three members elected by the General Assembly for non-consecutive six-year terms.",
        "fact_ta": "ஐ.நா தணிக்கையாளர் வாரியம் பொதுச் சபையால் 6 ஆண்டுகளுக்கு தேர்ந்தெடுக்கப்படும் மூன்று தணிக்கைத் தலைவர்களைக் கொண்டது."
    },
    # 29
    {
        "subtopic": "INTOSAI and ASOSAI Leadership",
        "stem_en": "What leadership position did the CAG of India hold in the Asian Organization of Supreme Audit Institutions (ASOSAI) for the 2024–2027 term?",
        "stem_ta": "2024-2027 காலகட்டத்திற்கான ஆசிய உச்ச தணிக்கை நிறுவனங்களின் அமைப்பில் (ASOSAI) இந்திய சி.ஏ.ஜி வகிக்கும் தலைமைப் பதவி என்ன?",
        "options": [
            ("Chair of ASOSAI, hosting the 16th Assembly in New Delhi in September 2024", "ASOSAI-ன் தலைவர் (Chair), செப்டம்பர் 2024-ல் புது தில்லியில் 16வது பொதுச் சபைக் கூட்டத்தை நடத்தினார்"),
            ("Permanent Secretary of the European Court of Auditors", "ஐரோப்பிய தணிக்கையாளர்கள் நீதிமன்றத்தின் நிரந்தரச் செயலாளர்"),
            ("Chief Ombudsman of the Pan-American Financial Tribunal", "பான்-அமெரிக்கன் நிதித் தீர்ப்பாயத்தின் தலைமை ஒம்புட்ஸ்மேன்"),
            ("Honorary President of the African Development Audit Council", "ஆப்பிரிக்க வளர்ச்சி தணிக்கை கவுன்சிலின் கௌரவத் தலைவர்")
        ],
        "exp_en": "In September 2024, the CAG of India assumed the prestigious Chairmanship of the Asian Organization of Supreme Audit Institutions (ASOSAI) for the 2024–2027 term during the 16th Assembly hosted in New Delhi.",
        "exp_ta": "செப்டம்பர் 2024-ல் புது தில்லியில் நடைபெற்ற 16வது பொதுச் சபைக் கூட்டத்தில், இந்திய சி.ஏ.ஜி 2024-2027 காலகட்டத்திற்கான ஆசிய உச்ச தணிக்கை நிறுவனங்களின் அமைப்பின் (ASOSAI) தலைவராகப் பொறுப்பேற்றார்.",
        "tip_en": "ASOSAI represents 48 Supreme Audit Institutions across Asia, promoting regional audit standards.",
        "tip_ta": "ASOSAI ஆசியா முழுவதும் உள்ள 48 தணிக்கை அமைப்புகளைப் பிரதிநிதித்துவப்படுத்துகிறது.",
        "fact_en": "INTOSAI is the global umbrella body with over 195 member supreme audit institutions.",
        "fact_ta": "INTOSAI என்பது 195-க்கும் மேற்பட்ட உச்ச தணிக்கை அமைப்புகளைக் கொண்ட உலகளாவிய அமைப்பாகும்."
    },
    # 30
    {
        "subtopic": "Audit of Disinvestment Proceeds",
        "stem_en": "In the audit of public sector disinvestment, what is the CAG's core focus when evaluating asset valuations and transactions?",
        "stem_ta": "பொதுத்துறை நிறுவனங்களின் பங்குகளைத் திரும்பப் பெறுதல் (Disinvestment) தணிக்கையில், சொத்து மதிப்பீடு மற்றும் பரிவர்த்தனைகளை மதிப்பிடும் போது சி.ஏ.ஜியின் முக்கிய கவனம் எதில் உள்ளது?",
        "options": [
            ("Ensuring valuation methodologies, reserve price fixation, and bidding procedures prevented undervaluation of state assets", "மதிப்பீட்டு முறைகள், அடிப்படை விலை நிர்ணயம் மற்றும் ஏல நடைமுறைகள் அரசு சொத்துக்கள் குறைத்து மதிப்பிடப்படுவதைத் தடுத்தனவா என்பதை உறுதி செய்தல்"),
            ("Mandating that 100% of PSU shares must be gifted free of cost to corporate executives", "பொதுத்துறை நிறுவனங்களின் 100% பங்குகளையும் கார்ப்பரேட் அதிகாரிகளுக்கு இலவசமாக வழங்க வேண்டும் என உத்தரவிடுதல்"),
            ("Fixing maximum daily stock exchange trading swings for disinvested companies", "பங்கு திரும்பப் பெறப்பட்ட நிறுவனங்களின் தினசரி பங்கு வர்த்தக விலை ஏற்ற இறக்கங்களை நிர்ணயித்தல்"),
            ("Abolishing all stock broker licenses issued by SEBI", "செபி (SEBI) வழங்கிய அனைத்து பங்குத் தரகர் உரிமங்களையும் ரத்து செய்தல்")
        ],
        "exp_en": "CAG's disinvestment audit investigates whether valuation methodologies (Discounted Cash Flow, Asset Valuation, Comparable Transactions) were applied objectively, whether reserve prices protected sovereign equity, and whether bidding was genuinely competitive.",
        "exp_ta": "சி.ஏ.ஜியின் பங்கு விலக்கல் தணிக்கை, சொத்து மதிப்பீடு மற்றும் அடிப்படை விலை நிர்ணயம் ஆகியவை பொதுத்துறை சொத்துக்களைப் பாதுகாக்கும் வகையில் முறையாகவும் நியாயமான ஏல முறையிலும் நடைபெற்றதா என்பதை ஆய்வு செய்கிறது.",
        "tip_en": "Disinvestment audits (e.g., BALCO, Centaur Hotel, Air India) focus on transparent valuation and preventing loss to exchequer.",
        "tip_ta": "பால்கோ (BALCO) மற்றும் சென்டார் ஹோட்டல் போன்ற பங்கு விலக்கல் தணிக்கைகள் அரசு சொத்து இழப்பைத் தடுப்பதில் கவனம் செலுத்தின.",
        "fact_en": "The Disinvestment Fund (National Investment Fund - NIF) is also scrutinized by the CAG.",
        "fact_ta": "தேசிய முதலீட்டு நிதியம் (NIF) மீதான செலவுகளும் சி.ஏ.ஜியால் தணிக்கை செய்யப்படுகின்றன."
    },
    # 31
    {
        "subtopic": "IT Audit and Data Analytics in Modern CAG",
        "stem_en": "Under the Enterprise-wide Computerized Audit System, what is the name of CAG's specialized digital audit platform for end-to-end data auditing?",
        "stem_ta": "நிறுவன அளவிலான கணினிமயமாக்கப்பட்ட தணிக்கை முறையின் கீழ், சி.ஏ.ஜியின் முழுமையான டிஜிட்டல் தணிக்கை தளத்தின் பெயர் என்ன?",
        "options": [
            ("OIOS (One IA&AD One System)", "OIOS (One IA&AD One System)"),
            ("SWAYAM Data Portal", "சுவயம் தரவு தளம் (SWAYAM)"),
            ("DigiLocker Audit App", "டிஜிலாக்கர் தணிக்கை செயலி"),
            ("BHIM Comptroller Pay", "பீம் கம்ப்ரோலர் பே (BHIM Pay)")
        ],
        "exp_en": "OIOS (One IA&AD One System) is the enterprise-wide digital audit solution launched by the CAG to digitize the entire audit lifecycle—from audit planning and field work to draft inspection reports and final tabling.",
        "exp_ta": "OIOS (ஒரே துறை, ஒரே அமைப்பு) என்பது தணிக்கைத் திட்டமிடல், கள ஆய்வு, ஆய்வறிக்கை தயாரிப்பு முதல் நாடாளுமன்ற சமர்ப்பிப்பு வரையிலான முழு தணிக்கை சுழற்சியையும் டிஜிட்டல் மயமாக்க சி.ஏ.ஜியால் தொடங்கப்பட்ட தளமாகும்.",
        "tip_en": "OIOS stands for 'One IA&AD One System' — a paperless, web-based digital audit management tool.",
        "tip_ta": "OIOS என்பது காகிதமற்ற, இணைய அடிப்படையிலான டிஜிட்டல் தணிக்கை மேலாண்மை கருவியாகும்.",
        "fact_en": "CAG also established the Centre for Data Management and Analytics (CDMA) in 2016 to leverage Big Data and AI.",
        "fact_ta": "பெரிய தரவு (Big Data) மற்றும் AI-ஐப் பயன்படுத்த 2016-ல் தரவு மேலாண்மை மற்றும் பகுப்பாய்வு மையத்தை (CDMA) சி.ஏ.ஜி அமைத்தது."
    },
    # 32
    {
        "subtopic": "Action Taken Notes (ATNs) and Action Taken Reports (ATRs)",
        "stem_en": "What is the constitutional and administrative mechanism when the CAG's audit report detects severe irregularities in a ministry?",
        "stem_ta": "சி.ஏ.ஜியின் தணிக்கை அறிக்கை ஒரு அமைச்சகத்தில் கடுமையான முறைகேடுகளைக் கண்டறியும் போது பின்பற்றப்படும் அரசியலமைப்பு மற்றும் நிர்வாக நடைமுறை என்ன?",
        "options": [
            ("The Ministry must submit Action Taken Notes (ATNs) within a stipulated time to the Public Accounts Committee, which produces Action Taken Reports", "சம்பந்தப்பட்ட அமைச்சகம் குறிப்பிட்ட காலத்திற்குள் பொதுக் கணக்குக் குழுவிற்கு நடவடிக்கை குறிப்புகளை (ATNs) சமர்ப்பிக்க வேண்டும்; குழு நடவடிக்கை அறிக்கைகளை வெளியிடும்"),
            ("The CAG directly fires the Union Minister and assumes administrative control of the department", "சி.ஏ.ஜி நேரடியாக மத்திய அமைச்சரைப் பதவி நீக்கம் செய்து, துறையின் நிர்வாகத்தை தன்வசப்படுத்துகிறார்"),
            ("The President issues an emergency ordinance shutting down the accused government ministry permanently", "குடியரசுத் தலைவர் அவசரச் சட்டம் பிறப்பித்து குற்றஞ்சாட்டப்பட்ட அமைச்சகத்தை நிரந்தரமாக மூடுகிறார்"),
            ("The audit report is kept confidential and destroyed after 12 months without legislative review", "தணிக்கை அறிக்கை ரகசியமாக வைக்கப்பட்டு, நாடாளுமன்ற ஆய்வின்றி 12 மாதங்களுக்குப் பிறகு அழிக்கப்படும்")
        ],
        "exp_en": "Ministries must submit Action Taken Notes (ATNs) explaining corrective measures, recoveries, or disciplinary actions taken on CAG paragraphs. The PAC reviews these and issues Action Taken Reports (ATRs) to ensure administrative accountability.",
        "exp_ta": "சி.ஏ.ஜியின் தணிக்கைப் பத்திகள் மீது எடுக்கப்பட்ட ஒழுங்கு நடவடிக்கை அல்லது மீட்பு நடவடிக்கைகள் குறித்து அமைச்சகங்கள் நடவடிக்கை குறிப்புகளை (ATNs) சமர்ப்பிக்கின்றன; அதை ஆய்வு செய்து PAC நடவடிக்கை அறிக்கைகளை (ATRs) வெளியிடுகிறது.",
        "tip_en": "Loop of accountability: CAG Report -> PAC Examination -> Ministry ATN -> PAC Action Taken Report (ATR).",
        "tip_ta": "பொறுப்புடைமை சுழற்சி: சி.ஏ.ஜி அறிக்கை -> PAC ஆய்வு -> அமைச்சகத்தின் ATN -> PAC நடவடிக்கை அறிக்கை (ATR).",
        "fact_en": "Unresolved ATNs can be repeatedly pursued by PAC until satisfactory executive compliance is achieved.",
        "fact_ta": "திருப்திகரமான நடவடிக்கை எடுக்கப்படும் வரை தீர்க்கப்படாத ATN-களை PAC தொடர்ந்து கண்காணிக்க முடியும்."
    },
    # 33
    {
        "subtopic": "Difference between CAG and Public Undertakings Committee",
        "stem_en": "What is the relationship between the CAG and the Parliamentary Committee on Public Undertakings (COPU)?",
        "stem_ta": "சி.ஏ.ஜி மற்றும் நாடாளுமன்றப் பொதுத்துறை நிறுவனங்களுக்கான குழு (COPU) ஆகியவற்றுக்கு இடையேயான உறவு என்ன?",
        "options": [
            ("COPU examines CAG's audit reports on Public Sector Undertakings (PSUs) with the CAG acting as technical advisor", "பொதுத்துறை நிறுவனங்கள் (PSUs) மீதான சி.ஏ.ஜியின் தணிக்கை அறிக்கைகளை COPU ஆய்வு செய்கிறது; இதில் சி.ஏ.ஜி தொழில்நுட்ப ஆலோசகராக உதவுகிறார்"),
            ("COPU exercises disciplinary control over the appointment and transfer of CAG audit directors", "சி.ஏ.ஜி தணிக்கை இயக்குநர்களின் நியமனம் மற்றும் இடமாற்றங்கள் மீது COPU ஒழுங்கு நடவடிக்கைக் கட்டுப்பாடு செலுத்துகிறது"),
            ("CAG is completely barred from auditing any enterprise examined by COPU", "COPU ஆய்வு செய்யும் எந்தவொரு பொதுத்துறை நிறுவனத்தையும் சி.ஏ.ஜி தணிக்கை செய்ய முழுமையாகத் தடை விதிக்கப்பட்டுள்ளது"),
            ("COPU reports directly to the CAG instead of the Lok Sabha Speaker", "COPU மக்களவைத் தலைவருக்குப் பதிலாக நேரடியாக சி.ஏ.ஜிக்கு அறிக்கை சமர்ப்பிக்கிறது")
        ],
        "exp_en": "Set up in 1964 on Krishna Menon Committee's recommendation, COPU examines CAG reports on Public Undertakings (Commercial audit reports), supported directly by the CAG and Commercial Audit Directorate.",
        "exp_ta": "1964-ல் கிருஷ்ண மேனன் குழு பரிந்துரையின்படி அமைக்கப்பட்ட COPU, பொதுத்துறை நிறுவனங்கள் மீதான சி.ஏ.ஜியின் வணிகத் தணிக்கை அறிக்கைகளை ஆய்வு செய்கிறது; இதற்கு சி.ஏ.ஜி தொழில்நுட்ப ரீதியாக உதவுகிறார்.",
        "tip_en": "PAC examines civil/defence reports; COPU examines public sector undertaking (PSU) reports.",
        "tip_ta": "PAC சிவில் மற்றும் பாதுகாப்பு அறிக்கைகளை ஆராய்கிறது; COPU பொதுத்துறை நிறுவனங்களின் அறிக்கைகளை ஆராய்கிறது.",
        "fact_en": "COPU has 22 members (15 from Lok Sabha, 7 from Rajya Sabha), mirroring the composition of the PAC.",
        "fact_ta": "COPU பொதுக் கணக்குக் குழுவைப் போலவே 22 உறுப்பினர்களைக் (15 மக்களவை, 7 மாநிலங்களவை) கொண்டது."
    },
    # 34
    {
        "subtopic": "Estimates Committee Exclusion",
        "stem_en": "Unlike the PAC and COPU, why does the Estimates Committee of Parliament have NO formal working relationship with the CAG?",
        "stem_ta": "பொதுக் கணக்குக் குழு மற்றும் பொதுத்துறை நிறுவனக் குழு ஆகியவற்றைப் போலன்றி, நாடாளுமன்ற மதிப்பீட்டுக் குழுவிற்கு (Estimates Committee) சி.ஏ.ஜியுடன் முறையான பணித் தொடர்பு இல்லாதது ஏன்?",
        "options": [
            ("Because Estimates Committee examines budget policies and prospective economies before money is spent, whereas CAG conducts ex-post audit", "ஏனெனில் மதிப்பீட்டுக் குழு பணம் செலவிடப்படுவதற்கு முன் பட்ஜெட் கொள்கைகளையும் வருங்கால சிக்கனங்களையும் ஆராய்கிறது; ஆனால் சி.ஏ.ஜி செலவுக்குப் பிந்தைய தணிக்கை செய்கிறார்"),
            ("Because the Estimates Committee consists exclusively of Rajya Sabha members who do not handle financial matters", "ஏனெனில் மதிப்பீட்டுக் குழுவில் நிதி விவகாரங்களைக் கையாளாத மாநிலங்களவை உறுப்பினர்கள் மட்டுமே உள்ளனர்"),
            ("Because the Constitution explicitly prohibits the CAG from communicating with Lok Sabha members", "ஏனெனில் சி.ஏ.ஜி மக்களவை உறுப்பினர்களுடன் தொடர்புகொள்வதை அரசியலமைப்பு வெளிப்படையாகத் தடை செய்துள்ளது"),
            ("Because the Estimates Committee conducts military intelligence investigations exempt from audit", "ஏனெனில் மதிப்பீட்டுக் குழு தணிக்கையிலிருந்து விலக்கு அளிக்கப்பட்ட ராணுவ ரகசியங்களை விசாரிக்கிறது")
        ],
        "exp_en": "The Estimates Committee examines budget estimates *prior* to or concurrently with policy execution to suggest organizational economies and policy alternatives ('Continuous Economy Committee'), whereas CAG's mandate is ex-post scrutiny of actual expenditure.",
        "exp_ta": "மதிப்பீட்டுக் குழு பட்ஜெட் திட்டங்களை ஆய்வு செய்து மாற்று வழிகளையும் கொள்கைச் சிக்கனங்களையும் முன்கூட்டியே பரிந்துரைக்கிறது; ஆனால் சி.ஏ.ஜியின் பணி செலவிடப்பட்ட பின் நடக்கும் தணிக்கையாகும்.",
        "tip_en": "Estimates Committee: Policy & economies beforehand. PAC: Financial audit with CAG assistance afterwards.",
        "tip_ta": "மதிப்பீட்டுக் குழு: முன்கூட்டியே கொள்கை சிக்கனம். பொதுக் கணக்குக் குழு: செலவிற்குப் பின் சி.ஏ.ஜி உதவியுடன் தணிக்கை.",
        "fact_en": "The Estimates Committee has 30 members, ALL drawn exclusively from the Lok Sabha.",
        "fact_ta": "மதிப்பீட்டுக் குழுவில் 30 உறுப்பினர்கள் உள்ளனர், அனைவரும் மக்களவையிலிருந்து மட்டுமே தேர்ந்தெடுக்கப்படுகின்றனர்."
    },
    # 35
    {
        "subtopic": "Constitutional Immunity of Indian Audit & Accounts Department",
        "stem_en": "Under Article 148(5), who makes the rules governing the conditions of service of persons serving in the Indian Audit and Accounts Department (IA&AD)?",
        "stem_ta": "சரத்து 148(5)-ன் கீழ், இந்திய தணிக்கை மற்றும் கணக்குத் துறையில் (IA&AD) பணியாற்றும் நபர்களின் சேவை நிபந்தனைகளை நிர்வகிக்கும் விதிகளை உருவாக்குபவர் யார்?",
        "options": [
            ("The President, strictly after consultation with the Comptroller and Auditor General", "கட்டாயமாக தலைமைத் தணிக்கையாளரைக் கலந்தாலோசித்த பின்னர், குடியரசுத் தலைவர்"),
            ("The Union Finance Minister unilaterally without consulting the CAG", "சி.ஏ.ஜியைக் கலந்தாலோசிக்காமல் மத்திய நிதி அமைச்சர் தன்னிச்சையாக"),
            ("The Chairman of the Union Public Service Commission", "மத்திய அரசுப் பணியாளர் தேர்வாணையத்தின் தலைவர்"),
            ("The Secretary General of the Lok Sabha Secretariat", "மக்களவைச் செயலகத்தின் பொதுச் செயலாளர்")
        ],
        "exp_en": "Article 148(5) mandates: 'Subject to the provisions of this Constitution and of any law made by Parliament, the conditions of service of persons serving in the Indian Audit and Accounts Department and the administrative powers of the Comptroller and Auditor-General shall be such as may be prescribed by rules made by the President after consultation with the Comptroller and Auditor-General.'",
        "exp_ta": "சரத்து 148(5)-ன் படி: இந்திய தணிக்கை மற்றும் கணக்குத் துறையில் பணியாற்றும் நபர்களின் சேவை நிபந்தனைகள் மற்றும் சி.ஏ.ஜியின் நிர்வாக அதிகாரங்கள் ஆகியவை சி.ஏ.ஜியைக் கலந்தாலோசித்த பிறகு குடியரசுத் தலைவரால் விதிகளாக நிர்ணயிக்கப்பட வேண்டும்.",
        "tip_en": "Service rules of IA&AD staff: President makes rules, but mandatory consultation with CAG is required.",
        "tip_ta": "IA&AD ஊழியர்களின் சேவை விதிகள்: குடியரசுத் தலைவர் உருவாக்குகிறார், ஆனால் சி.ஏ.ஜியுடனான கலந்தாலோசனை கட்டாயமாகும்.",
        "fact_en": "This consultation is substantive, designed to protect audit officers from political victimization by ministries.",
        "fact_ta": "அமைச்சகங்களின் அரசியல் பழிவாங்கலிலிருந்து தணிக்கை அதிகாரிகளைப் பாதுகாக்க இந்த கலந்தாலோசனை அவசியமாக்கப்பட்டுள்ளது."
    },
    # 36
    {
        "subtopic": "CAG Audit of Subsidies & Direct Benefit Transfer (DBT)",
        "stem_en": "In performance audits of Direct Benefit Transfer (DBT) subsidy schemes (e.g., PM-KISAN, PAHAL LPG subsidy), what constitutes a major CAG audit finding?",
        "stem_ta": "நேரடிப் பயன் பரிமாற்ற (DBT) மானியத் திட்டங்களின் (எ.கா. PM-KISAN, PAHAL எல்.பி.ஜி மானியம்) செயல்திறன் தணிக்கைகளில், சி.ஏ.ஜி வெளிக்கொணர்ந்த முக்கியக் குறைபாடு எது?",
        "options": [
            ("Ineligible beneficiaries, lack of de-duplication, deceased beneficiaries receiving transfers, and ghost bank accounts", "தகுதியற்ற பயனாளிகள், நகல் நீக்கமின்மை, இறந்தவர்களின் கணக்குகளுக்கு நிதி மாற்றம் மற்றும் போலி வங்கிக் கணக்குகள்"),
            ("Direct transfers reaching citizens via postal money orders within 2 hours", "தபால் மணி ஆர்டர் மூலம் 2 மணி நேரத்திற்குள் குடிமக்களுக்கு நேரடிப் பரிமாற்றம் சென்றடைந்தது"),
            ("DBT schemes violating the fundamental rights guaranteed under Article 21", "DBT திட்டங்கள் சரத்து 21-ன் கீழ் உத்தரவாதம் அளிக்கப்பட்ட அடிப்படை உரிமைகளை மீறுகின்றன"),
            ("Commercial banks charging negative interest rates on rural tractor loans", "கிராமப்புற டிராக்டர் கடன்களுக்கு வணிக வங்கிகள் எதிர்மறை வட்டி விகிதங்களை வசூலித்தது")
        ],
        "exp_en": "CAG's IT-enabled audits of DBT schemes cross-verify Aadhaar, land records, and income tax databases, frequently identifying transfers to ineligible taxpayers, deceased individuals, multiple accounts sharing one identification, and failure of automated reconciliation.",
        "exp_ta": "DBT திட்டங்கள் மீதான சி.ஏ.ஜி தணிக்கை, ஆதார், நிலப் பதிவேடுகள் மற்றும் வருமான வரித் தரவுகளை ஒப்பிட்டு, வரி செலுத்தும் தகுதியற்றவர்கள், இறந்தவர்கள் மற்றும் போலி பயனாளிகளுக்கு மானியம் வழங்கப்பட்டதை வெளிக்கொணர்கிறது.",
        "tip_en": "Data analytics in DBT audit reveals ghost beneficiaries and system de-duplication failures.",
        "tip_ta": "DBT தணிக்கையில் தரவுப் பகுப்பாய்வு போலிப் பயனாளிகள் மற்றும் கணினி குறைபாடுகளைக் கண்டறியப் பயன்படுகிறது.",
        "fact_en": "CAG utilizes Big Data analytics platforms to parse hundreds of millions of public DBT transaction records.",
        "fact_ta": "கோடிக்கணக்கான DBT பரிவர்த்தனைகளை ஆய்வு செய்ய சி.ஏ.ஜி பெருந்தரவுப் பகுப்பாய்வு (Big Data) முறைகளைப் பயன்படுத்துகிறது."
    },
    # 37
    {
        "subtopic": "CAG and Judicial Scrutiny of Audit Reports",
        "stem_en": "Can the contents, findings, or loss estimates in a CAG report be treated by criminal courts as conclusive proof of an offence?",
        "stem_ta": "சி.ஏ.ஜி அறிக்கையில் உள்ள தகவல்கள், கண்டுபிடிப்புகள் அல்லது இழப்பு மதிப்பீடுகளை குற்றவியல் நீதிமன்றங்கள் ஒரு குற்றத்தின் உறுதியான ஆதாரமாக (conclusive proof) ஏற்றுக்கொள்ள முடியுமா?",
        "options": [
            ("No, a CAG report is a high-level administrative audit document that must be independently investigated and proven with legal evidence in court", "இல்லை, சி.ஏ.ஜி அறிக்கை ஒரு தணிக்கை ஆவணம் மட்டுமே; அதை நீதிமன்றத்தில் சட்டரீதியான ஆதாரங்களுடன் தனித்து நிரூபிக்க வேண்டும்"),
            ("Yes, Article 148 makes CAG loss estimates automatically binding on all criminal trials as unchallengeable proof", "ஆம், சரத்து 148 சி.ஏ.ஜியின் இழப்பு மதிப்பீடுகளை குற்றவியல் வழக்குகளில் மறுக்க முடியாத ஆதாரமாக மாற்றுகிறது"),
            ("Yes, the Indian Evidence Act defines CAG findings as irrebuttable judicial confessions", "ஆம், இந்திய சாட்சியச் சட்டம் சி.ஏ.ஜி கண்டுபிடிப்புகளை மறுக்க முடியாத ஒப்புதல் வாக்குமூலமாக வரையறுக்கிறது"),
            ("No, because CAG reports are legally void unless countersigned by the Attorney General", "இல்லை, ஏனெனில் அட்டர்னி ஜெனரல் கையொப்பமிடாத வரை சி.ஏ.ஜி அறிக்கைகள் சட்டப்படி செல்லாது")
        ],
        "exp_en": "The Supreme Court has clarified (in the 2G spectrum and Coal block cases) that while CAG reports highlight financial loss and regulatory flaws for Parliament, they do not constitute criminal evidence per se; charges must be substantiated through independent investigative evidence (CBI/police).",
        "exp_ta": "உச்ச நீதிமன்றம் (2G மற்றும் நிலக்கரி வழக்குகளில்) சி.ஏ.ஜி அறிக்கை நாடாளுமன்றத்திற்கான தணிக்கை ஆவணமே தவிர, குற்றவியல் வழக்குகளில் தானாகவே உறுதியான குற்ற ஆதாரமாகாது என்றும், அதை காவல்துறையின் தனி விசாரணைக் கொண்டு நிரூபிக்க வேண்டும் என்றும் தீர்ப்பளித்துள்ளது.",
        "tip_en": "CAG reports highlight systemic loss and flaws for Parliament, not direct convictions in criminal trials.",
        "tip_ta": "சி.ஏ.ஜி அறிக்கைகள் நாடாளுமன்றத்திற்கு முறைகேடுகளை வெளிப்படுத்துகின்றன; அவை நீதிமன்றத்தில் நேரடி குற்ற ஆதாரங்களாகாது.",
        "fact_en": "Audit reports form the starting point of investigations by anti-corruption agencies, not the final criminal verdict.",
        "fact_ta": "தணிக்கை அறிக்கைகள் ஊழல் தடுப்பு அமைப்புகளின் விசாரணைக்கான தொடக்கப் புள்ளியாக அமைகின்றனவே தவிர இறுதித் தீர்ப்பல்ல."
    },
    # 38
    {
        "subtopic": "Audit of Defence Procurement",
        "stem_en": "Why are CAG's performance audit reports on defence capital acquisitions (e.g., fighter aircraft, submarines) subject to redaction of commercially sensitive operational data?",
        "stem_ta": "பாதுகாப்பு மூலதனக் கொள்முதல் (எ.கா. போர் விமானங்கள், நீர்மூழ்கிக் கப்பல்கள்) மீதான சி.ஏ.ஜியின் செயல்திறன் தணிக்கை அறிக்கைகளில் வணிக மற்றும் செயல்பாட்டுத் தரவுகள் நீக்கப்படுவது (redaction) ஏன்?",
        "options": [
            ("To safeguard national security, military tactical capabilities, and inter-governmental sovereign pricing agreements", "தேசியப் பாதுகாப்பு, ராணுவ தந்திரோபாயத் திறன்கள் மற்றும் அரசுகளுக்கு இடையேயான ரகசிய ஒப்பந்தங்களைப் பாதுகாப்பதற்காக"),
            ("Because the CAG is legally prohibited from auditing any item under the Ministry of Defence", "ஏனெனில் பாதுகாப்பு அமைச்சகத்தின் கீழ் உள்ள எந்தவொரு பொருளையும் தணிக்கை செய்ய சி.ஏ.ஜிக்கு சட்டப்படி தடை விதிக்கப்பட்டுள்ளது என்பதால்"),
            ("Because defence purchases are funded exclusively through private donations exempt from Article 151", "ஏனெனில் பாதுகாப்பு கொள்முதல்கள் சரத்து 151-லிருந்து விலக்கு அளிக்கப்பட்ட தனியார் நன்கொடைகள் மூலம் நிதியளிக்கப்படுகின்றன"),
            ("Because defence audits are conducted solely by foreign mercenary accountants", "ஏனெனில் பாதுகாப்பு தணிக்கைகள் வெளிநாட்டு தனியார் தணிக்கையாளர்களால் மட்டுமே நடத்தப்படுகின்றன")
        ],
        "exp_en": "In sensitive defence audits (such as the Rafale aircraft procurement audit of 2019), the Ministry of Defence and CAG redact specific operational equipment costs and weapon specifications to prevent compromising national security and breach of inter-governmental sovereign non-disclosure clauses.",
        "exp_ta": "2019 ரஃபேல் ஒப்பந்தத் தணிக்கை போன்ற முக்கிய பாதுகாப்பு தணிக்கைகளில், தேசியப் பாதுகாப்பு மற்றும் ஒப்பந்த ரகசிய விதிகளுக்கு பாதிப்பு ஏற்படாமல் இருக்க ஆயுத நுட்பங்கள் மற்றும் தனித்தனி உபகரண விலைகளை நீக்கி அறிக்கை சமர்ப்பிக்கப்படுகிறது.",
        "tip_en": "Defence audit is fully within CAG's mandate, but operational weapon metrics may be redacted for security.",
        "tip_ta": "பாதுகாப்புத் தணிக்கை சி.ஏ.ஜியின் அதிகார வரம்பிற்கு உட்பட்டதே; ஆனால் ரகசிய ஆயுத விவரங்கள் தேசியப் பாதுகாப்பிற்காக நீக்கப்படலாம்.",
        "fact_en": "The Principal Director of Audit (Air Force and Navy) and DG (Army) lead defence audit directorates within IA&AD.",
        "fact_ta": "ராணுவம், கடற்படை மற்றும் விமானப்படை தணிக்கைக்காக IA&AD-க்குள் தனித் தணிக்கை இயக்குநரகங்கள் உள்ளன."
    },
    # 39
    {
        "subtopic": "Special Audit of Discoms - Delhi High Court Ruling",
        "stem_en": "In the Delhi High Court judgment regarding the CAG audit of private electricity distribution companies (Discoms) in Delhi, what was the constitutional balance struck?",
        "stem_ta": "டெல்லியில் உள்ள தனியார் மின் விநியோக நிறுவனங்களை (Discoms) சி.ஏ.ஜி தணிக்கை செய்வது குறித்த டெல்லி உயர் நீதிமன்றத் தீர்ப்பில் நிலைநாட்டப்பட்ட சமநிலை என்ன?",
        "options": [
            ("Audit under Section 20 can only be directed where the state government has deep financial involvement and after regulatory consultation", "மாநில அரசுக்கு ஆழமான நிதித் தொடர்பு இருக்கும் போது மட்டுமே ஒழுங்குமுறை ஆணைய ஆலோசனையுடன் பிரிவு 20-ன் கீழ் தணிக்கை கோரப்பட முடியும்"),
            ("The High Court held that private Discoms must be nationalized immediately without audit", "தனியார் மின் நிறுவனங்களைத் தணிக்கை செய்யாமல் உடனடியாக அரசுடைமையாக்க வேண்டும் என உயர் நீதிமன்றம் தீர்ப்பளித்தது"),
            ("The Court declared that CAG has zero power to audit any utility providing public services", "பொதுச் சேவைகளை வழங்கும் எந்தவொரு பயன்பாட்டு நிறுவனத்தையும் தணிக்கை செய்ய சி.ஏ.ஜிக்கு அதிகாரம் இல்லை என்று நீதிமன்றம் அறிவித்தது"),
            ("The Court held that electricity consumers must personally audit the high-voltage transformers", "மின் நுகர்வோரே உயர் மின்னழுத்த மின்மாற்றிகளை நேரில் ஆய்வு செய்ய வேண்டும் என நீதிமன்றம் கூறியது")
        ],
        "exp_en": "The Delhi High Court examined Section 20 of the 1971 Act and the Electricity Act, clarifying that while Section 20 permits audit of entities in the public interest, statutory regulatory procedures (such as tariff determination by DERC) must not be improperly bypassed.",
        "exp_ta": "டெல்லி உயர் நீதிமன்றம், பிரிவு 20-ன் கீழ் பொது நலன் கருதி தணிக்கை செய்யப்படலாம் என்றாலும், மின்சார ஒழுங்குமுறை ஆணையத்தின் (DERC) கட்டண நிர்ணய சட்டப்பூர்வ நடைமுறைகள் புறக்கணிக்கப்படக் கூடாது என்று தெளிவுபடுத்தியது.",
        "tip_en": "Audit of privatized utilities requires compliance with Section 20 procedural safeguards.",
        "tip_ta": "தனியார்மயமாக்கப்பட்ட பயன்பாட்டு நிறுவனங்களின் தணிக்கைக்கு பிரிவு 20-ன் பாதுகாப்பு நடைமுறைகளைப் பின்பற்றுவது அவசியமாகும்.",
        "fact_en": "The matter involving Section 20 scope for private utilities subsequently went before the Supreme Court of India.",
        "fact_ta": "தனியார் பயன்பாட்டு நிறுவனங்கள் மீதான பிரிவு 20-ன் எல்லை குறித்த வழக்கு பின்னர் உச்ச நீதிமன்றத்திற்குச் சென்றது."
    },
    # 40
    {
        "subtopic": "Role in Special Purpose Vehicles (SPVs) for Smart Cities",
        "stem_en": "How does the CAG exercise audit authority over Smart City Special Purpose Vehicles (SPVs) incorporated jointly by state governments and municipal corporations?",
        "stem_ta": "மாநில அரசுகள் மற்றும் மாநகராட்சிகளால் கூட்டாக உருவாக்கப்பட்ட 'ஸ்மார்ட் சிட்டி சிறப்பு நோக்க வாகனங்கள்' (SPVs) மீது சி.ஏ.ஜி தனது தணிக்கை அதிகாரத்தை எவ்வாறு செலுத்துகிறார்?",
        "options": [
            ("As government companies under Section 19(1) of the 1971 Act and Section 143 of the Companies Act 2013, since over 51% equity is held by public entities", "51%-க்கும் அதிகமான பங்குகள் பொது அமைப்புகளிடம் உள்ளதால், 1971 சட்டத்தின் பிரிவு 19(1) மற்றும் நிறுவனங்கள் சட்டம் பிரிவு 143-ன் கீழ் அரசு நிறுவனங்களாகத் தணிக்கை செய்கிறார்"),
            ("Smart City SPVs are completely outside CAG audit because they use digital optical fiber", "ஸ்மார்ட் சிட்டி நிறுவனங்கள் ஆப்டிகல் ஃபைபரைப் பயன்படுத்துவதால் அவை சி.ஏ.ஜி தணிக்கைக்கு முற்றிலும் அப்பாற்பட்டவை"),
            ("Only through voluntary corporate social responsibility (CSR) non-binding disclosures", "கட்டாயமற்ற கார்ப்பரேட் சமூகப் பொறுப்பு (CSR) வெளிப்பாடுகள் மூலமாக மட்டுமே"),
            ("By deploying municipal traffic police to conduct cash register verifications", "பணப் பதிவேடுகளை சரிபார்க்க நகராட்சி போக்குவரத்து காவல்துறையினரை ஈடுபடுத்துவதன் மூலம்")
        ],
        "exp_en": "Smart City SPVs are registered under the Companies Act 2013 with 50:50 equity holding between the State Government and the Urban Local Body (100% government ownership). Therefore, they are Government Companies audited under Section 143 of Companies Act and CAG Act.",
        "exp_ta": "ஸ்மார்ட் சிட்டி SPV நிறுவனங்கள் மாநில அரசு மற்றும் உள்ளாட்சி அமைப்புகளுக்கு இடையே 50:50 பங்குகளுடன் 100% அரசு உரிமையுடன் உருவாக்கப்படுவதால், அவை நிறுவனங்கள் சட்டம் பிரிவு 143 மற்றும் சி.ஏ.ஜி சட்டத்தின் கீழ் தணிக்கை செய்யப்படுகின்றன.",
        "tip_en": "Smart City SPVs are 100% government-owned corporate entities, fully subject to CAG statutory audit.",
        "tip_ta": "ஸ்மார்ட் சிட்டி நிறுவனங்கள் 100% அரசுக்குச் சொந்தமானவை என்பதால் சி.ஏ.ஜி தணிக்கைக்கு முழுமையாக உட்பட்டவை.",
        "fact_en": "CAG conducts both compliance and performance audits of Smart City project implementations.",
        "fact_ta": "ஸ்மார்ட் சிட்டி திட்டங்களின் விதிகள் பின்பற்றுதல் மற்றும் செயல்திறன் இரண்டையும் சி.ஏ.ஜி தணிக்கை செய்கிறது."
    },
    # 41
    {
        "subtopic": "CAG Audit of Cess and Surcharges",
        "stem_en": "What recurrent irregularity has the CAG highlighted regarding the Union Government's collection and transfer of 'Cesses and Surcharges'?",
        "stem_ta": "மத்திய அரசால் வசூலிக்கப்படும் 'செஸ் மற்றும் கூடுதல் கட்டணங்கள்' (Cesses and Surcharges) வசூல் மற்றும் இடமாற்றம் தொடர்பாக சி.ஏ.ஜி மீண்டும் மீண்டும் சுட்டிக்காட்டியுள்ள முக்கிய முறைகேடு எது?",
        "options": [
            ("Retaining collected cess amounts in the Consolidated Fund instead of transferring them to designated non-lapsable dedicated reserve funds", "வசூலிக்கப்பட்ட செஸ் தொகையை அதற்கான பிரத்யேக நிதிகளுக்கு மாற்றாமல் திரட்டப்பட்ட நிதியிலேயே (CFI) தேக்கி வைப்பது"),
            ("Distributing 100% of cess collections directly to foreign central banks", "செஸ் வசூலின் 100% தொகையையும் வெளிநாட்டு மத்திய வங்கிகளுக்கு நேரடியாகப் பகிர்ந்தளிப்பது"),
            ("Abolishing income tax surcharges without presidential consent", "குடியரசுத் தலைவரின் ஒப்புதலின்றி வருமான வரி மீதான கூடுதல் கட்டணங்களை ரத்து செய்வது"),
            ("Using fuel cess exclusively to purchase private yachts for tax commissioners", "வரி ஆணையர்களுக்கு தனியார் படகுகள் வாங்க மட்டுமே எரிபொருள் செஸ் தொகையைப் பயன்படுத்துவது")
        ],
        "exp_en": "CAG's financial audit reports have repeatedly flagged that thousands of crores collected via statutory cesses (like Road & Infrastructure Cess, Health & Education Cess, Clean Energy Cess) were retained in the Consolidated Fund to artificially suppress fiscal deficit, rather than being transferred to dedicated reserve funds.",
        "exp_ta": "சாலை உள்கட்டமைப்பு மற்றும் கல்வி செஸ் போன்ற பிரத்யேக வரிகள் மூலம் வசூலிக்கப்பட்ட பல்லாயிரக்கணக்கான கோடிகள், அவற்றுக்கென உருவாக்கப்பட்ட பிரத்யேக நிதிகளுக்கு மாற்றப்படாமல் நிதிப் பற்றாக்குறையைக் குறைக்க அரசுப் பொது நிதியிலேயே தேக்கி வைக்கப்பட்டதை சி.ஏ.ஜி சுட்டிக்காட்டியுள்ளது.",
        "tip_en": "Cess proceeds must legally be transferred to dedicated reserve funds (e.g., Central Road Fund, Prarambhik Shiksha Kosh).",
        "tip_ta": "செஸ் வருவாய் சட்டப்படி அதற்கான பிரத்யேக நிதிகளுக்கு (எ.கா. மத்திய சாலை நிதி) மாற்றப்பட வேண்டும்.",
        "fact_en": "Article 271 allows the Union to retain surcharges and cesses without sharing them with States.",
        "fact_ta": "சரத்து 271-ன் படி கூடுதல் கட்டணங்கள் மற்றும் செஸ் தொகையை மாநிலங்களுடன் பகிராமல் மத்திய அரசே முழுமையாக வைத்துக் கொள்ளலாம்."
    },
    # 42
    {
        "subtopic": "Re-appropriation and Supplementary Demands Audit",
        "stem_en": "When government departments transfer budgeted funds from one sub-head to another, what does the CAG scrutinize under the audit of 'Re-appropriation'?",
        "stem_ta": "அரசுத் துறைகள் பட்ஜெட் நிதியை ஒரு உப-தலைப்பிலிருந்து மற்றொன்றுக்கு மாற்றும் போது (Re-appropriation), சி.ஏ.ஜி எதனை ஆய்வு செய்கிறார்?",
        "options": [
            ("Whether the re-appropriation was sanctioned by competent financial authority, made before the financial year ended, and not used for a 'New Service'", "மறுஒதுக்கீடு தகுதிவாய்ந்த அதிகாரியால் அனுமதிக்கப்பட்டதா, நிதியாண்டு முடிவதற்குள் செய்யப்பட்டதா மற்றும் 'புதிய சேவைக்கு' பயன்படுத்தப்படவில்லையா என்பது"),
            ("Whether the funds were invested in cryptocurrency mining farms", "நிதியானது கிரிப்டோகரன்சி அமைப்புகளில் முதலீடு செய்யப்பட்டதா என்பது"),
            ("Whether the departmental head secured personal written permission from the Chief Justice", "துறைத் தலைவர் தலைமை நீதிபதியிடம் தனிப்பட்ட எழுத்துப்பூர்வ அனுமதி பெற்றாரா என்பது"),
            ("Whether the money was used to sponsor international beauty pageants", "சர்வதேச அழகுப் போட்டிகளை நடத்த அந்தப் பணம் பயன்படுத்தப்பட்டதா என்பது")
        ],
        "exp_en": "Audit of re-appropriation ensures that funds are moved only between authorized sub-heads within the same voted grant, not applied to create a 'New Service' (which requires a supplementary grant voted by Parliament), and approved by competent authority before March 31.",
        "exp_ta": "மறுஒதுக்கீட்டுத் தணிக்கை, நிதி ஒரே மானியத் தலைப்பிற்குள் அனுமதிக்கப்பட்ட வரம்பிற்குள் மாற்றப்பட்டுள்ளதா என்பதையும், நாடாளுமன்ற ஒப்புதல் தேவைப்படும் 'புதிய சேவைக்கு' அது பயன்படுத்தப்படவில்லை என்பதையும் உறுதி செய்கிறது.",
        "tip_en": "Re-appropriation cannot fund a 'New Service' or 'New Instrument of Service' without legislative vote.",
        "tip_ta": "சட்டமன்ற ஒப்புதல் இன்றி மறுஒதுக்கீடு மூலம் 'புதிய சேவை' எதற்கும் நிதியை மாற்ற முடியாது.",
        "fact_en": "Re-appropriation from revenue expenditure to capital expenditure is generally strictly prohibited under financial rules.",
        "fact_ta": "வருவாய் செலவினத்திலிருந்து மூலதன செலவினத்திற்கு நிதியை மறுஒதுக்கீடு செய்வது பொதுவாகத் தடை செய்யப்பட்டுள்ளது."
    },
    # 43
    {
        "subtopic": "Article 148(3) Protection of Salary & Conditions",
        "stem_en": "Why does Article 148(3) provide that the salary, rights in respect of leave of absence, pension, or age of retirement of the CAG shall not be varied to his disadvantage after appointment?",
        "stem_ta": "நியமனத்திற்குப் பிறகு சி.ஏ.ஜியின் ஊதியம், விடுப்பு உரிமைகள், ஓய்வூதியம் அல்லது ஓய்வு பெறும் வயது ஆகியவை அவருக்கு பாதகமாக மாற்றப்படக் கூடாது என சரத்து 148(3) கூறுவது ஏன்?",
        "options": [
            ("To guarantee institutional independence so that executive coercion cannot threaten his financial security during his tenure", "பதவிக்காலத்தில் அவரது நிதிப் பாதுகாப்பை நிர்வாக அச்சுறுத்தல்களிலிருந்து விடுவித்து, நிறுவனத் தன்னாட்சியை உத்தரவாதப்படுத்த"),
            ("To ensure the CAG receives annual bonuses pegged to the profitability of public sector banks", "பொதுத்துறை வங்கிகளின் லாபத்திற்கு ஏற்ப சி.ஏ.ஜி ஆண்டு போனஸ் பெறுவதை உறுதி செய்ய"),
            ("Because the CAG is personally immune from paying municipal water and power tariffs", "ஏனெனில் சி.ஏ.ஜி நகராட்சி குடிநீர் மற்றும் மின்சார கட்டணங்களை செலுத்துவதிலிருந்து விலக்கு பெற்றவர் என்பதால்"),
            ("To permit the CAG to double his own remuneration whenever inflation exceeds 5%", "பணவீக்கம் 5%-ஐத் தாண்டும் போதெல்லாம் சி.ஏ.ஜி தனது சொந்த ஊதியத்தை இரட்டிப்பாக்கிக் கொள்ள அனுமதிக்க")
        ],
        "exp_en": "Article 148(3) secures financial independence: once appointed, the executive government cannot reduce the CAG's salary, benefits, or pension terms, ensuring he can audit government ministries without fear of financial reprisal.",
        "exp_ta": "சரத்து 148(3) நிதி சுதந்திரத்தைப் பாதுகாக்கிறது: நியமிக்கப்பட்ட பிறகு, நிர்வாகத்தால் சி.ஏ.ஜியின் ஊதியம் அல்லது சலுகைகளைக் குறைக்க முடியாது; இது பழிவாங்கும் பயமின்றி அரசு அமைச்சகங்களைத் தணிக்கை செய்ய உதவுகிறது.",
        "tip_en": "Salary and service conditions cannot be varied to disadvantage after appointment (identical to SC judges).",
        "tip_ta": "நியமனத்திற்குப் பின் ஊதியம் மற்றும் சேவை நிபந்தனைகள் பாதகமாக மாற்றப்பட முடியாது (உச்ச நீதிமன்ற நீதிபதிகளுக்கு இணையானது).",
        "fact_en": "The only exception is during a Financial Emergency declared by the President under Article 360.",
        "fact_ta": "சரத்து 360-ன் கீழ் குடியரசுத் தலைவரால் அறிவிக்கப்படும் நிதி அவசரநிலையின் போது மட்டுமே இதில் விதிவிலக்கு அளிக்க முடியும்."
    },
    # 44
    {
        "subtopic": "Audit of Autonomous District Councils (Sixth Schedule)",
        "stem_en": "Under Paragraph 7(2) of the Sixth Schedule to the Constitution of India, what is the CAG's authority regarding Autonomous District Councils in tribal areas of Assam, Meghalaya, Tripura, and Mizoram?",
        "stem_ta": "இந்திய அரசியலமைப்பின் ஆறாவது அட்டவணையின் பத்தி 7(2)-ன் கீழ், அசாம், மேகாலயா, திரிபுரா மற்றும் மிசோரம் ஆகிய பழங்குடியினர் பகுதிகளில் உள்ள தன்னாட்சி மாவட்டக் குழுக்கள் (ADCs) தொடர்பாக சி.ஏ.ஜியின் அதிகாரம் என்ன?",
        "options": [
            ("The accounts of such District and Regional Councils shall be kept in such form as the CAG prescribes, and shall be audited by the CAG", "அத்தகைய மாவட்ட மற்றும் பிராந்தியக் குழுக்களின் கணக்குகள் சி.ஏ.ஜி நிர்ணயிக்கும் படிவத்தில் வைக்கப்பட வேண்டும் மற்றும் சி.ஏ.ஜியால் தணிக்கை செய்யப்பட வேண்டும்"),
            ("Sixth Schedule councils are sovereign foreign territories exempt from all Indian audits", "ஆறாவது அட்டவணை குழுக்கள் இந்திய தணிக்கைகளிலிருந்து விலக்கு அளிக்கப்பட்ட தன்னாட்சிப் பகுதிகள்"),
            ("Audit can only be conducted if approved by a tribal council referendum with 90% quorum", "பழங்குடியினர் குழு வாக்கெடுப்பில் 90% ஒப்புதல் அளித்தால் மட்டுமே தணிக்கை செய்ய முடியும்"),
            ("District Council accounts are audited exclusively by private village moneylenders", "மாவட்டக் குழு கணக்குகள் தனியார் கிராமக் கடன் தருநர்களால் மட்டுமே தணிக்கை செய்யப்படுகின்றன")
        ],
        "exp_en": "Paragraph 7(2) of the Sixth Schedule explicitly provides that the accounts of Autonomous District Councils (ADCs) and Regional Councils shall be kept in such form as the CAG may, with the approval of the Governor, prescribe and shall be audited by the CAG, with reports submitted to the Governor.",
        "exp_ta": "ஆறாவது அட்டவணை பத்தி 7(2)-ன் படி, தன்னாட்சி மாவட்டக் குழுக்களின் கணக்குகள் ஆளுநரின் ஒப்புதலுடன் சி.ஏ.ஜி நிர்ணயிக்கும் படிவத்தில் வைக்கப்பட வேண்டும் மற்றும் சி.ஏ.ஜியால் தணிக்கை செய்யப்பட்டு ஆளுநருக்கு அறிக்கை அனுப்பப்பட வேண்டும்.",
        "tip_en": "Sixth Schedule Autonomous District Councils (ADCs) are subject to mandatory constitutional audit by the CAG.",
        "tip_ta": "ஆறாவது அட்டவணை தன்னாட்சி மாவட்டக் குழுக்கள் சி.ஏ.ஜியின் கட்டாய அரசியலமைப்புத் தணிக்கைக்கு உட்பட்டவை.",
        "fact_en": "The Governor causes these audit reports to be laid before the Council.",
        "fact_ta": "ஆளுநர் இந்தத் தணிக்கை அறிக்கைகளை சம்பந்தப்பட்ட குழுவின் முன் சமர்ப்பிக்கச் செய்கிறார்."
    },
    # 45
    {
        "subtopic": "CAG Audit of Goods and Services Tax (GST)",
        "stem_en": "What unique constitutional and technical challenge does the CAG encounter when conducting receipt audits of the Goods and Services Tax (GST)?",
        "stem_ta": "சரக்கு மற்றும் சேவை வரி (GST) வரவுத் தணிக்கையை நடத்தும் போது சி.ஏ.ஜி எதிர்கொள்ளும் தனித்துவமான அரசியலமைப்பு மற்றும் தொழில்நுட்ப சவால் என்ன?",
        "options": [
            ("Accessing complete, un-redacted pan-India transactional data from the GST Network (GSTN) SPV and auditing seamless input tax credit flow", "ஜி.எஸ்.டி நெட்வொர்க் (GSTN) அமைப்பிடமிருந்து முழுமையான நாடு தழுவிய தரவுகளைப் பெறுதல் மற்றும் உள்ளீட்டு வரி வரவு (ITC) ஓட்டத்தைத் தணிக்கை செய்தல்"),
            ("GST rates being fixed in foreign currencies by the International Monetary Fund", "ஜி.எஸ்.டி விகிதங்கள் சர்வதேச நாணய நிதியத்தால் வெளிநாட்டு நாணயங்களில் நிர்ணயிக்கப்படுவது"),
            ("CAG being prohibited from stepping into state government tax offices", "மாநில அரசின் வரி அலுவலகங்களுக்குள் நுழைய சி.ஏ.ஜிக்கு தடை விதிக்கப்பட்டிருப்பது"),
            ("GST receipts being credited to private personal bank accounts of state finance ministers", "ஜி.எஸ்.டி வரவுகள் மாநில நிதி அமைச்சர்களின் தனியார் வங்கிக் கணக்குகளில் வரவு வைக்கப்படுவது")
        ],
        "exp_en": "Because GST is managed via GSTN (a Special Purpose Vehicle) handling complex Integrated GST (IGST) settlements and automated Input Tax Credit (ITC) between Union and States, CAG requires full system data access to audit whether tax devolution and ITC claims are lawful.",
        "exp_ta": "ஜி.எஸ்.டி நெட்வொர்க் (GSTN) மூலம் நிர்வகிக்கப்படும் ஒருங்கிணைந்த ஜி.எஸ்.டி (IGST) மற்றும் உள்ளீட்டு வரி வரவு (ITC) ஆகியவற்றின் உண்மைத் தன்மையைச் சரிபார்க்க முழுமையான கணினித் தரவுகளைப் பெறுவது சி.ஏ.ஜியின் முக்கிய தொழில்நுட்ப சவாலாகும்.",
        "tip_en": "GST audit requires deep scrutiny of IGST settlement accounts and input tax credit fraud detection.",
        "tip_ta": "ஜி.எஸ்.டி தணிக்கை IGST தீர்வு கணக்குகள் மற்றும் போலி உள்ளீட்டு வரி வரவு மோசடிகளை ஆய்வு செய்வதை உள்ளடக்கியது.",
        "fact_en": "CAG's GST compliance reports regularly highlight multi-crore ITC mismatches and un-reconciled IGST balances.",
        "fact_ta": "சி.ஏ.ஜியின் ஜி.எஸ்.டி அறிக்கைகள் பல கோடி ரூபாய் போலி உள்ளீட்டு வரி வரவு முறைகேடுகளைத் தொடர்ந்து வெளிப்படுத்துகின்றன."
    },
    # 46
    {
        "subtopic": "Audit Quality Management Framework (AQMF)",
        "stem_en": "What is the primary operational objective of the Audit Quality Management Framework (AQMF) institutionalized by the CAG of India?",
        "stem_ta": "இந்திய சி.ஏ.ஜியால் நடைமுறைப்படுத்தப்பட்ட 'தணிக்கைத் தர மேலாண்மைக் கட்டமைப்பின்' (AQMF) முதன்மை செயல்பாட்டு நோக்கம் என்ன?",
        "options": [
            ("To establish internal quality controls, peer reviews, and adherence to international auditing standards across all field audit offices", "அனைத்து கள தணிக்கை அலுவலகங்களிலும் உள் தணிக்கைக் கட்டுப்பாடு, சக தணிக்கையாளர் மதிப்பாய்வு மற்றும் சர்வதேச தரநிலைகளைப் பின்பற்றுவதை உறுதி செய்ய"),
            ("To award cash prizes to the highest spending government ministries each quarter", "ஒவ்வொரு காலாண்டிலும் அதிக செலவு செய்யும் அரசு அமைச்சகங்களுக்கு ரொக்கப் பரிசுகளை வழங்க"),
            ("To reduce the number of pages in the Union budget document to below 10 pages", "மத்திய பட்ஜெட் ஆவணத்தின் பக்கங்களின் எண்ணிக்கையை 10 பக்கங்களுக்குள் குறைக்க"),
            ("To replace professional auditors with automated lottery machines for selecting audit samples", "தணிக்கை மாதிரிகளைத் தேர்ந்தெடுக்க தொழில்முறைத் தணிக்கையாளர்களுக்குப் பதிலாக லாட்டரி இயந்திரங்களை வைக்க")
        ],
        "exp_en": "The AQMF provides a continuous quality assurance mechanism across the Indian Audit & Accounts Department, establishing technical guidelines for planning, evidence collection, reporting standards, and peer review of audit offices.",
        "exp_ta": "AQMF என்பது தணிக்கைத் திட்டமிடல், சான்றுகள் சேகரிப்பு, அறிக்கை தயாரிப்பு மற்றும் சக அலுவலக மதிப்பாய்வு ஆகியவற்றில் சர்வதேச தரநிலைகளைப் பின்பற்றுவதை உறுதி செய்யும் தர உத்தரவாதக் கட்டமைப்பாகும்.",
        "tip_en": "AQMF aligns Indian government auditing with International Standards of Supreme Audit Institutions (ISSAI).",
        "tip_ta": "AQMF இந்திய அரசுத் தணிக்கையை சர்வதேச உச்ச தணிக்கை நிறுவனங்களின் தரநிலைகளுடன் (ISSAI) இணைக்கிறது.",
        "fact_en": "Internal audit inspection units periodically review PAG offices under the AQMF guidelines.",
        "fact_ta": "AQMF வழிகாட்டுதல்களின் கீழ் முதன்மை கணக்குத் தலைவர் அலுவலகங்களை உள் ஆய்வுக் குழுக்கள் தொடர்ந்து ஆய்வு செய்கின்றன."
    },
    # 47
    {
        "subtopic": "Separation of Accounts and Cadre Bifurcation in States",
        "stem_en": "Why do most Indian States continue to have their accounts compiled by the CAG, unlike the Union Government which departmentalized its accounts in 1976?",
        "stem_ta": "1976-ல் மத்திய அரசு தனது கணக்குகளைத் துறைமயமாக்கியதைப் போலன்றி, பெரும்பாலான இந்திய மாநிலங்கள் இன்னும் தங்கள் கணக்குகளை சி.ஏ.ஜியால் தொகுக்கப்படுவதற்கு அனுமதிப்பது ஏன்?",
        "options": [
            ("States have not exercised the option to departmentalize accounts due to financial costs and reliance on the independent expertise of the CAG", "நிதிச் செலவுகள் மற்றும் சி.ஏ.ஜியின் தன்னாட்சி நிபுணத்துவத்தை நம்பியிருப்பதன் காரணமாக மாநிலங்கள் கணக்குகளைத் துறைமயமாக்க முன்வரவில்லை"),
            ("The Supreme Court struck down state account separation as unconstitutional under Article 356", "சரத்து 356-ன் கீழ் மாநிலக் கணக்குப் பிரிப்பு அரசியலமைப்பிற்கு முரணானது என்று உச்ச நீதிமன்றம் ரத்து செய்தது"),
            ("State legislative assemblies lack constitutional power to enact financial laws", "மாநில சட்டப்பேரவைகளுக்கு நிதிச் சட்டங்களை இயற்ற அரசியலமைப்பு அதிகாரம் இல்லை என்பதால்"),
            ("The 73rd Constitutional Amendment made CAG compilation mandatory forever for all states", "73வது அரசியலமைப்புத் திருத்தம் அனைத்து மாநிலங்களுக்கும் சி.ஏ.ஜி கணக்குத் தொகுப்பை நிரந்தரமாகக் கட்டாயமாக்கியது")
        ],
        "exp_en": "Section 10 of the CAG Act allows the President to relieve the CAG of accounting duties for states after consultation with the Governor. However, except for Goa and UT of Puducherry, states have chosen not to separate accounting from audit due to high administrative costs and trust in the CAG's institutional machinery.",
        "exp_ta": "மாநில ஆளுநரைக் கலந்தாலோசித்து மாநிலக் கணக்குத் தொகுப்பிலிருந்து சி.ஏ.ஜியை விடுவிக்க சட்டத்தில் இடமிருந்தாலும், கூடுதல் நிர்வாகச் செலவு மற்றும் சி.ஏ.ஜி மீதான நம்பிக்கையால் கோவா தவிர பிற மாநிலங்கள் கணக்குகளைப் பிரிக்கவில்லை.",
        "tip_en": "Union separated accounts from audit in 1976. In almost all States, CAG still compiles accounts (via AG A&E).",
        "tip_ta": "மத்திய அரசு 1976-ல் கணக்கைப் பிரித்தது. ஆனால் மாநிலங்களில் இன்றும் சி.ஏ.ஜியே கணக்குகளைத் தொகுக்கிறார் (AG A&E மூலம்).",
        "fact_en": "In states, the Accountant General (A&E) handles Accounts & Entitlements, while the AG (Audit) handles Audit.",
        "fact_ta": "மாநிலங்களில் முதன்மை கணக்குத் தலைவர் (A&E) கணக்குகளையும், முதன்மை கணக்குத் தலைவர் (Audit) தணிக்கையையும் கையாள்கின்றனர்."
    },
    # 48
    {
        "subtopic": "Role in Consolidated Sinking Fund and Calamity Relief",
        "stem_en": "How does the CAG audit specialized state government financial reserves such as the Consolidated Sinking Fund (CSF) and State Disaster Response Fund (SDRF)?",
        "stem_ta": "ஒருங்கிணைந்த கடன் தீர்வு நிதி (CSF) மற்றும் மாநில பேரிடர் மீட்பு நிதி (SDRF) போன்ற மாநில அரசின் சிறப்பு நிதி இருப்புகளை சி.ஏ.ஜி எவ்வாறு தணிக்கை செய்கிறார்?",
        "options": [
            ("Verifies whether mandated state matching contributions, RBI investment guidelines, and calamity relief expenditures satisfy statutory criteria", "மாநில அரசின் பங்குத் தொகை, ரிசர்வ் வங்கி முதலீட்டு வழிகாட்டுதல்கள் மற்றும் பேரிடர் நிவாரணச் செலவினங்கள் சட்ட விதிகளைப் பூர்த்தி செய்கின்றனவா என்பதை சரிபார்க்கிறார்"),
            ("Personally distributes relief grain packets from disaster helicopters during monsoons", "பருவமழைக் காலங்களில் பேரிடர் மீட்பு ஹெலிகாப்டர்களில் இருந்து நிவாரண உணவுப் பொட்டலங்களை நேரில் விநியோகிக்கிறார்"),
            ("Invests state calamity reserves in speculative offshore venture capital funds", "மாநில பேரிடர் நிதியை வெளிநாட்டுத் தனியார் துணிகர மூலதன நிதி நிறுவனங்களில் முதலீடு செய்கிறார்"),
            ("Prohibits states from receiving any disaster relief assistance from the National Disaster Response Fund", "தேசிய பேரிடர் மீட்பு நிதியிலிருந்து மாநிலங்கள் எந்தவொரு நிவாரண உதவியையும் பெறுவதைத் தடை செய்கிறார்")
        ],
        "exp_en": "In the State Finance Accounts audit, CAG examines whether the State Government transferred its mandated statutory contribution to the SDRF, whether surplus funds were invested with the RBI in designated securities under CSF guidelines, and whether unspent balances were properly accounted.",
        "exp_ta": "மாநில நிதிக் கணக்குத் தணிக்கையில், மாநில அரசு தனது சட்டப்பூர்வ பங்களிப்பை SDRF-க்கு மாற்றியதா, உபரி நிதி ரிசர்வ் வங்கியின் வழிகாட்டுதலின்படி முதலீடு செய்யப்பட்டதா மற்றும் செலவிடப்படாத இருப்பு முறையாக உள்ளதா என்பதை சி.ஏ.ஜி ஆராய்கிறார்.",
        "tip_en": "SDRF and CSF audits ensure dedicated calamity and debt redemption funds are not diverted for daily fiscal deficits.",
        "tip_ta": "பேரிடர் மற்றும் கடன் தீர்வு நிதிகள் அன்றாட நிர்வாகச் செலவுகளுக்கு தவறாகத் திருப்பி விடப்படாமல் இருப்பதை சி.ஏ.ஜி உறுதி செய்கிறார்.",
        "fact_en": "Non-credit of state share to SDRF attracts adverse audit observations and interest liabilities.",
        "fact_ta": "SDRF-க்கு மாநிலப் பங்கை உரிய நேரத்தில் வழங்காவிட்டால் தணிக்கைக் குறிப்புகளும் வட்டிப் பொறுப்பும் ஏற்படும்."
    },
    # 49
    {
        "subtopic": "Comptroller & Auditor General's Advisory Role to PAC",
        "stem_en": "During the examination of witnesses by the Public Accounts Committee, which official privilege is extended to the CAG and his representatives?",
        "stem_ta": "பொதுக் கணக்குக் குழு சாட்சிகளை விசாரிக்கும் போது, சி.ஏ.ஜி மற்றும் அவரது பிரதிநிதிகளுக்கு வழங்கப்படும் அதிகாரப்பூர்வ உரிமை என்ன?",
        "options": [
            ("Right to intervene, clarify complex accounting facts, and suggest specific cross-examination inquiries to the PAC Chairman", "குறுக்கிடவும், சிக்கலான கணக்கு விவரங்களை தெளிவுபடுத்தவும் மற்றும் PAC தலைவருக்கு குறுக்கு விசாரணை வினாக்களைப் பரிந்துரைக்கவும் உரிமை"),
            ("Right to pronounce on-the-spot legal judgments sentencing corrupt department witnesses", "ஊழல் செய்த துறை சாட்சிகளுக்கு உடனடியாக சம்பவ இடத்திலேயே சட்டப்பூர்வ தண்டனைத் தீர்ப்பு வழங்கும் உரிமை"),
            ("Right to expel elected Members of Parliament from the committee room for indiscipline", "ஒழுங்கீனத்திற்காக தேர்ந்தெடுக்கப்பட்ட நாடாளுமன்ற உறுப்பினர்களைக் குழு அறையிலிருந்து வெளியேற்றும் உரிமை"),
            ("Right to redact parliamentary records before they are printed in the official gazette", "நாடாளுமன்றக் குறிப்புகள் அரசிதழில் அச்சிடப்படுவதற்கு முன் அவற்றை நீக்கும் உரிமை")
        ],
        "exp_en": "The CAG sits alongside the Chairman of the PAC during witness depositions of departmental secretaries; he points out discrepancies between oral testimonies and official audit documentation, acting as the indispensable expert guide of the committee.",
        "exp_ta": "அமைச்சகச் செயலாளர்கள் சாட்சியமளிக்கும் போது சி.ஏ.ஜி PAC தலைவருக்கு அருகில் அமர்ந்து, அதிகாரிகளின் வாய்மொழி வாக்குமூலத்திற்கும் தணிக்கை ஆவணங்களுக்கும் உள்ள முரண்பாடுகளை சுட்டிக்காட்டி இன்றியமையாத வழிகாட்டியாக உதவுகிறார்.",
        "tip_en": "CAG empowers legislative scrutiny by bridging technical accounting complexities for elected MPs.",
        "tip_ta": "தேர்ந்தெடுக்கப்பட்ட நாடாளுமன்ற உறுப்பினர்களுக்கு தொழில்நுட்பக் கணக்கு நுணுக்கங்களை விளக்கி சட்டப்பேரவை ஆய்வை சி.ஏ.ஜி பலப்படுத்துகிறார்.",
        "fact_en": "The relationship between PAC and CAG is considered one of the most successful parliamentary oversight partnerships.",
        "fact_ta": "PAC மற்றும் சி.ஏ.ஜி இடையேயான உறவு நாடாளுமன்ற மேற்பார்வையின் மிக வெற்றிகரமான கூட்டாண்மையாகக் கருதப்படுகிறது."
    },
    # 50
    {
        "subtopic": "Appointment Precedents and Constitutional Conventions",
        "stem_en": "By long-standing administrative convention in India, from which background has the Comptroller and Auditor General typically been appointed?",
        "stem_ta": "இந்தியாவின் நீண்டகால நிர்வாக மரபின்படி, தலைமைத் தணிக்கையாளர் (சி.ஏ.ஜி) பொதுவாக எந்தப் பின்னணியில் இருந்து நியமிக்கப்படுகிறார்?",
        "options": [
            ("Senior civil servants, usually of the Indian Administrative Service (IAS) or Indian Audit and Accounts Service (IA&AS), who served as Union Secretaries", "மத்திய செயலாளர்களாகப் பணியாற்றிய மூத்த இந்திய ஆட்சிப் பணி (IAS) அல்லது இந்திய தணிக்கை மற்றும் கணக்குப் பணி (IA&AS) அதிகாரிகள்"),
            ("Sitting Chief Justices of High Courts who resign from the judiciary", "நீதித்துறையிலிருந்து ராஜினாமா செய்யும் உயர் நீதிமன்றத் தலைமை நீதிபதிகள்"),
            ("Active political party treasurers holding seats in the Rajya Sabha", "மாநிலங்களவையில் இடம்பிடித்துள்ள அரசியல் கட்சிகளின் தீவிரப் பொருளாளர்கள்"),
            ("Chief Executive Officers of multi-national private equity funds", "பன்னாட்டுத் தனியார் பங்கு நிதி நிறுவனங்களின் தலைமை நிர்வாக அதிகாரிகள்")
        ],
        "exp_en": "While the Constitution specifies no explicit criteria, convention since independence has seen senior civil servants—frequently retired Union Finance Secretaries, Defence Secretaries, or Home Secretaries of the IAS/IA&AS cadre—appointed by the President on the advice of the Prime Minister.",
        "exp_ta": "அரசியலமைப்பு குறிப்பிட்ட தகுதிகளைக் குறிப்பிடவில்லை என்றாலும், சுதந்திரத்திற்குப் பிறகு மூத்த குடிமைப் பணி அதிகாரிகள் (IAS/IA&AS) மத்திய செயலாளர்களாகப் பணியாற்றிய பின்னரே பிரதமரின் ஆலோசனையின் பேரில் குடியரசுத் தலைவரால் நியமிக்கப்படும் மரபு பின்பற்றப்படுகிறது.",
        "tip_en": "First CAG: V. Narahari Rao (IA&AS). Many recent CAGs were former Union Defence/Finance/Higher Education Secretaries.",
        "tip_ta": "முதல் சி.ஏ.ஜி வி. நரஹரி ராவ் (IA&AS). சமீபத்திய சி.ஏ.ஜிக்கள் முன்னாள் மத்திய செயலாளர்களாவர்.",
        "fact_en": "Calls for a multi-member collegium (PM, CJI, Leader of Opposition) for CAG appointment have been made by administrative reform commissions.",
        "fact_ta": "நிர்வாகச் சீர்திருத்தக் குழுக்கள் சி.ஏ.ஜி நியமனத்திற்கு கொலீஜியம் முறையை (பிரதமர், தலைமை நீதிபதி, எதிர்க்கட்சித் தலைவர்) பரிந்துரைத்துள்ளன."
    }
]

def build_questions():
    questions = []
    for idx, item in enumerate(raw_questions, start=1):
        qid = f"CAG_H_{idx:03d}"
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
            diff="Hard",
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
            tags=["polity", "comptroller_and_auditor_general", "hard", item["subtopic"].lower().replace(" ", "_")]
        )
        questions.append(q)
    return questions

if __name__ == "__main__":
    qs = build_questions()
    print(f"Generated {len(qs)} raw Hard questions for CAG.")
    
    balanced_qs = balance_question_keys(qs)
    
    out_path = os.path.join("data", "questions", "polity", "cag_hard.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(balanced_qs, f, ensure_ascii=False, indent=2)
        
    print(f"Saved balanced Hard MCQs to {out_path}")
    
    val = ContentValidator()
    report = val.validate_file(out_path, expected_count=50, expected_prefix="CAG_H_")
    print(f"Validation Report: {'PASS' if report.is_valid else 'FAIL'} | Total: {report.total_audited}")
    if not report.is_valid:
        for iss in report.issues[:10]:
            print(f"  Issue: {iss}")
    print(f"Key Distribution: {report.key_distribution}")

