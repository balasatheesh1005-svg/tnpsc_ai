# -*- coding: utf-8 -*-
"""
CAG Grand Test Part 1: Questions 1 to 50 (CAG_GT_001 to CAG_GT_050)
Fresh stems designed to have zero overlap with Core 325 questions.
"""

from cag_mcq_helper import make_cag_q

raw_gt_part1_data = [
    # 1
    {
        "subtopic": "Sovereign Audit Sovereignty",
        "stem_en": "Which of the following constitutional provisions prevents the Parliament from reducing the powers of the CAG as compared to those exercised immediately before the commencement of the Constitution?",
        "stem_ta": "அரசியலமைப்பு தொடங்குவதற்கு சற்று முன் நடைமுறையில் இருந்த அதிகாரங்களுடன் ஒப்பிடும்போது சி.ஏ.ஜியின் அதிகாரங்களை நாடாளுமன்றம் குறைப்பதைத் தடுக்கும் அரசியலமைப்பு விதி எது?",
        "options": [
            ("Proviso to Article 149", "சரத்து 149-ன் வரம்புரை"),
            ("Clause (3) of Article 148", "சரத்து 148-ன் பிரிவு (3)"),
            ("Article 151(1)", "சரத்து 151(1)"),
            ("Second Proviso to Article 150", "சரத்து 150-ன் இரண்டாவது வரம்புரை")
        ],
        "exp_en": "The proviso to Article 149 guarantees that until Parliament enacts a law, the CAG shall exercise such powers and perform such duties in relation to the accounts of the Union and the States as were conferred on or exercisable by the Auditor General of India immediately before the commencement of the Constitution.",
        "exp_ta": "சரத்து 149-ன் வரம்புரை, நாடாளுமன்றம் சட்டம் இயற்றும் வரை, அரசியலமைப்பு தொடங்குவதற்கு சற்று முன் இந்தியத் தணிக்கைத் தலைவரால் செலுத்தப்பட்ட அதே அதிகாரங்களையும் கடமைகளையும் சி.ஏ.ஜி தொடர்ந்து செலுத்துவார் என்று உத்தரவாதம் அளிக்கிறது.",
        "tip_en": "Article 149 Proviso provided unbroken institutional continuity until the 1971 DPC Act was enacted.",
        "tip_ta": "1971 DPC சட்டம் இயற்றப்படும் வரை சரத்து 149-ன் வரம்புரை நிறுவனத் தொடர்ச்சியை வழங்கியது.",
        "fact_en": "It took 21 years (from 1950 to 1971) for Parliament to enact the comprehensive CAG Act under Article 149.",
        "fact_ta": "சரத்து 149-ன் கீழ் விரிவான சி.ஏ.ஜி சட்டத்தை நாடாளுமன்றம் இயற்ற 21 ஆண்டுகள் (1950 முதல் 1971 வரை) ஆனது."
    },
    # 2
    {
        "subtopic": "Pensions Charged on CFI",
        "stem_en": "According to Article 112(3)(e) of the Constitution, what is specifically charged on the Consolidated Fund of India regarding the CAG?",
        "stem_ta": "அரசியலமைப்பின் சரத்து 112(3)(e)-ன் படி, சி.ஏ.ஜி தொடர்பாக இந்தியத் திரட்டப்பட்ட நிதியில் குறிப்பாகப் பொறுப்பாக்கப்பட்டது எது?",
        "options": [
            ("The salary, allowances and pension payable to or in respect of the Comptroller and Auditor General", "தலைமைக் கணக்குத் தணிக்கையாளருக்கு வழங்கப்படும் அல்லது அது தொடர்பான ஊதியம், படிகள் மற்றும் ஓய்வூதியம்"),
            ("Only the travel allowances incurred by the CAG during foreign official delegations", "சி.ஏ.ஜி வெளிநாட்டு அதிகாரப்பூர்வ பயணங்களின் போது செய்யும் பயணப் படிகள் மட்டுமே"),
            ("The discretionary contingency grant placed at the disposal of the CAG", "சி.ஏ.ஜியின் வசம் வைக்கப்பட்டுள்ள விருப்ப அவசரகால மானியம்"),
            ("The legal fees paid to private counsel defending CAG audit findings", "சி.ஏ.ஜி தணிக்கைக் குறிப்புகளை ஆதரிக்கும் தனியார் வழக்கறிஞர்களுக்கான கட்டணம்")
        ],
        "exp_en": "Article 112(3)(e) explicitly enumerates as expenditure charged on the CFI: 'the salary, allowances and pension payable to or in respect of the Comptroller and Auditor-General of India'.",
        "exp_ta": "சரத்து 112(3)(e) சி.ஏ.ஜிக்கு அல்லது அது தொடர்பாக வழங்கப்படும் ஊதியம், படிகள் மற்றும் ஓய்வூதியத்தை இந்தியத் திரட்டப்பட்ட நிதியில் பொறுப்பாக்கப்பட்ட செலவினமாக வெளிப்படையாகப் பட்டியலிடுகிறது.",
        "tip_en": "Article 112(3)(e) protects CAG's remuneration from parliamentary vote reduction.",
        "tip_ta": "சரத்து 112(3)(e) சி.ஏ.ஜியின் ஊதியத்தை நாடாளுமன்ற வாக்கெடுப்பு வெட்டுகளிலிருந்து பாதுகாக்கிறது.",
        "fact_en": "Pensions of all staff of the IA&AD are also charged on the CFI under Article 148(6).",
        "fact_ta": "சரத்து 148(6)-ன் கீழ் IA&AD ஊழியர்களின் ஓய்வூதியங்களும் CFI-ல் பொறுப்பாக்கப்பட்டுள்ளன."
    },
    # 3
    {
        "subtopic": "Audit of Multi-State Cooperatives",
        "stem_en": "Under what statutory arrangement can the CAG conduct an audit of a Multi-State Cooperative Society receiving financial aid from the Central Government?",
        "stem_ta": "மத்திய அரசிடமிருந்து நிதி உதவி பெறும் பல மாநில கூட்டுறவுச் சங்கத்தை சி.ஏ.ஜி எந்த சட்டப்பூர்வ ஏற்பாட்டின் கீழ் தணிக்கை செய்ய முடியும்?",
        "options": [
            ("Under Section 14 or Section 20 of the CAG (DPC) Act 1971 read with the Multi-State Co-operative Societies Act", "பல மாநில கூட்டுறவுச் சங்கங்கள் சட்டத்துடன் இணைந்த 1971 சி.ஏ.ஜி சட்டத்தின் பிரிவு 14 அல்லது பிரிவு 20-ன் கீழ்"),
            ("Under the administrative executive orders issued by the Ministry of Cooperation", "கூட்டுறவு அமைச்சகத்தால் வெளியிடப்படும் நிர்வாக உத்தரவுகளின் கீழ் மட்டுமே"),
            ("Under the Reserve Bank of India Urban Cooperative Banking Regulations", "ரிசர்வ் வங்கியின் நகர்ப்புற கூட்டுறவு வங்கி ஒழுங்குமுறைகளின் கீழ்"),
            ("Under Article 243ZJ of Part IXB without requiring statutory reference", "சட்டப்பூர்வ பரிந்துரை தேவையின்றி பகுதி IXB-ன் சரத்து 243ZJ-ன் கீழ் நேரடியாக")
        ],
        "exp_en": "If a multi-state cooperative receives substantial grants or loans, it can be audited under Section 14, or under Section 20 upon entrustment by the President in the public interest.",
        "exp_ta": "ஒரு பல மாநில கூட்டுறவுச் சங்கம் கணிசமான மானியங்கள் அல்லது கடன்களைப் பெற்றால், அது பிரிவு 14-ன் கீழ் அல்லது பொது நலன் கருதி குடியரசுத் தலைவரால் ஒப்படைக்கப்படும் போது பிரிவு 20-ன் கீழ் தணிக்கை செய்யப்படலாம்.",
        "tip_en": "Multi-state cooperative audit: Section 14 applies if grants exceed threshold; otherwise Section 20 entrustment.",
        "tip_ta": "கூட்டுறவுச் சங்க தணிக்கை: மானியம் வரம்பை மீறினால் பிரிவு 14; இல்லையெனில் பிரிவு 20 ஒப்படைப்பு பொருந்தும்.",
        "fact_en": "The Multi-State Co-operative Societies (Amendment) Act 2023 reinforced fiscal transparency.",
        "fact_ta": "2023 பல மாநில கூட்டுறவுச் சங்கங்கள் திருத்தச் சட்டம் நிதி வெளிப்படைத்தன்மையை வலுப்படுத்தியது."
    },
    # 4
    {
        "subtopic": "CAG and Public Accounts Committee Synergy",
        "stem_en": "How does the CAG actively participate during the oral evidence sessions of the Public Accounts Committee?",
        "stem_ta": "பொதுக் கணக்குக் குழுவின் (PAC) வாய்மொழி சாட்சி அமர்வுகளின் போது சி.ஏ.ஜி எவ்வாறு தீவிரமாகப் பங்கேற்கிறார்?",
        "options": [
            ("The CAG sits alongside the Chairman, assists in framing penetrating questions, and points out factual contradictions in witness depositions", "சி.ஏ.ஜி தலைவருக்கு அருகில் அமர்ந்து, கூர்மையான வினாக்களை எழுப்ப உதவுகிறார் மற்றும் சாட்சிகளின் பதில்களில் உள்ள முரண்பாடுகளைச் சுட்டிக்காட்டுகிறார்"),
            ("The CAG acts as the defence attorney for the audited government ministry", "சி.ஏ.ஜி தணிக்கை செய்யப்பட்ட அரசு அமைச்சகத்தின் வழக்கறிஞராக வாதாடுகிறார்"),
            ("The CAG casts a decisive casting vote in case of tied committee decisions", "குழுவின் வாக்கெடுப்பு சமநிலையில் முடியும் போது சி.ஏ.ஜி தீர்க்கமான வாக்கைச் செலுத்துகிறார்"),
            ("The CAG exercises contempt powers to imprison uncooperative departmental secretaries", "ஒத்துழைக்காத துறைச் செயலாளர்களை சிறையில் அடைக்க நீதிமன்ற அவமதிப்பு அதிகாரங்களை சி.ஏ.ஜி செலுத்துகிறார்")
        ],
        "exp_en": "The CAG sits with the PAC during oral hearings, assists the Committee in cross-examining administrative secretaries, and clarifies technical accounting nuances, functioning as its institutional expert.",
        "exp_ta": "சாட்சி விசாரணையின் போது சி.ஏ.ஜி PAC தலைவருடன் அமர்ந்து, நிர்வாகச் செயலாளர்களை குறுக்கு விசாரணை செய்ய உதவுகிறார் மற்றும் கணக்கியல் சிக்கல்களை விளக்குகிறார்.",
        "tip_en": "The CAG attends PAC meetings as an expert adviser, not as an elected voting member.",
        "tip_ta": "சி.ஏ.ஜி வாக்களிக்கும் உறுப்பினராக அல்லாமல் ஒரு நிபுணர் ஆலோசகராகவே PAC கூட்டங்களில் கலந்து கொள்கிறார்.",
        "fact_en": "PAC witnesses depose under official oath or affirmation.",
        "fact_ta": "PAC சாட்சிகள் முறையான உறுதிமொழி அல்லது பிரமாணத்தின் கீழ் வாக்குமூலம் அளிக்கின்றனர்."
    },
    # 5
    {
        "subtopic": "Environmental Audit Mandate",
        "stem_en": "Which international framework forms the benchmark for the CAG of India when auditing renewable energy and carbon offset mechanisms?",
        "stem_ta": "புதுப்பிக்கத்தக்க எரிசக்தி மற்றும் கார்பன் சமன் செய்யும் வழிமுறைகளைத் தணிக்கை செய்யும் போது இந்திய சி.ஏ.ஜிக்கு எந்த சர்வதேச கட்டமைப்பு அளவுகோலாக அமைகிறது?",
        "options": [
            ("INTOSAI Working Group on Environmental Auditing (WGEA) standards and ISSAI 5110", "சுற்றுச்சூழல் தணிக்கைக்கான INTOSAI பணிக்குழு (WGEA) தரநிலைகள் மற்றும் ISSAI 5110"),
            ("World Economic Forum Davos Ecological Declaration", "உலகப் பொருளாதார மன்றத்தின் டாவோஸ் சுற்றுச்சூழல் பிரகடனம்"),
            ("International Maritime Organization Safety Code", "சர்வதேச கடல்சார் அமைப்பின் பாதுகாப்பு விதிகள்"),
            ("Basel Committee on Banking Supervision Green Taxonomy", "வங்கி மேற்பார்வைக்கான பாசல் குழுவின் பசுமை வகைப்பாடு")
        ],
        "exp_en": "The CAG conducts environmental audits based on the international standards and audit methodologies developed by the INTOSAI Working Group on Environmental Auditing (WGEA) and ISSAI 5110.",
        "exp_ta": "INTOSAI சுற்றுச்சூழல் தணிக்கை பணிக்குழு (WGEA) மற்றும் ISSAI 5110 ஆகியவற்றால் உருவாக்கப்பட்ட சர்வதேச தரநிலைகளின் அடிப்படையிலேயே சி.ஏ.ஜி சுற்றுச்சூழல் தணிக்கைகளை நடத்துகிறது.",
        "tip_en": "iCED Jaipur acts as the hub for training in INTOSAI WGEA methodologies.",
        "tip_ta": "ஜெய்ப்பூர் iCED மையம் INTOSAI WGEA வழிமுறைகளுக்கான சர்வதேச பயிற்சி மையமாகச் செயல்படுகிறது.",
        "fact_en": "CAG has audited the National Clean Energy Fund, Ganga Rejuvenation, and National Solar Mission.",
        "fact_ta": "கங்கை தூய்மைத் திட்டம், தேசிய சூரியசக்தி திட்டம் ஆகியவற்றை சி.ஏ.ஜி தணிக்கை செய்துள்ளது."
    },
    # 6
    {
        "subtopic": "Separation of State Accounts Feasibility",
        "stem_en": "Why has the separation of accounts from audit NOT been implemented across the majority of Indian States, unlike the Union Government?",
        "stem_ta": "மத்திய அரசைப் போலன்றி, பெரும்பாலான இந்திய மாநிலங்களில் தணிக்கையிலிருந்து கணக்குப் பிரிப்பு ஏன் இன்னும் செயல்படுத்தப்படவில்லை?",
        "options": [
            ("States face severe fiscal and administrative constraints in setting up parallel organized accounting cadres", "மாநிலங்களில் இணையான தனி கணக்குத் துறைகளை உருவாக்க கடுமையான நிதி மற்றும் நிர்வாகச் சிக்கல்கள் உள்ளன"),
            ("Article 150 strictly prohibits States from ever compiling their own civil accounts", "சரத்து 150 மாநிலங்கள் தங்களது சொந்த கணக்குகளைத் தொகுப்பதை முற்றிலுமாகத் தடை செய்கிறது"),
            ("The Supreme Court struck down the departmentalization of state accounts as ultra vires", "மாநிலக் கணக்குகளைத் துறைமயமாக்குவது அரசியலமைப்புக்கு எதிரானது என உச்ச நீதிமன்றம் ரத்து செய்தது"),
            ("State legislative assemblies lack constitutional authority to vote on departmental budgets", "மாநில சட்டமன்றங்களுக்கு துறைசார் பட்ஜெட் மீது வாக்களிக்க அரசியலமைப்பு அதிகாரம் இல்லை")
        ],
        "exp_en": "The high administrative cost and shortage of trained accounting manpower prevented States from departmentalizing accounts. Consequently, under Section 10 proviso of the 1971 Act, CAG continues to maintain state accounts.",
        "exp_ta": "அதிக நிர்வாகச் செலவு மற்றும் பயிற்சி பெற்ற கணக்கு பணியாளர்கள் பற்றாக்குறை காரணமாக மாநிலங்களால் கணக்குகளைப் பிரிக்க முடியவில்லை. இதனால் 1971 சட்டத்தின் பிரிவு 10 வரம்புரையின் கீழ் சி.ஏ.ஜியே மாநிலக் கணக்குகளைப் பராமரித்து வருகிறார்.",
        "tip_en": "Except Goa and Puducherry, all States rely on the CAG's Principal Accountants General (A&E) to compile monthly accounts.",
        "tip_ta": "கோவா மற்றும் புதுச்சேரி தவிர, அனைத்து மாநிலங்களும் கணக்குகளைத் தொகுக்க சி.ஏ.ஜியின் PAG (A&E) அலுவலகங்களையே சார்ந்துள்ளன.",
        "fact_en": "State Finance Accounts prepared by the CAG are tabled annually in State Legislatures.",
        "fact_ta": "சி.ஏ.ஜியால் தயாரிக்கப்படும் மாநில நிதிக் கணக்குகள் ஆண்டுதோறும் மாநில சட்டமன்றங்களில் வைக்கப்படுகின்றன."
    },
    # 7
    {
        "subtopic": "Specialized Role in Net Proceeds Devolution",
        "stem_en": "What happens if a State Government formally disputes the CAG's certification of net proceeds under Article 279?",
        "stem_ta": "சரத்து 279-ன் கீழ் நிகர வருமானம் குறித்து சி.ஏ.ஜி அளித்த சான்றிதழை ஒரு மாநில அரசு முறையாக எதிர்த்தால் என்ன நிகழும்?",
        "options": [
            ("The dispute cannot be entertained in court because the Constitution makes the CAG's certificate final and conclusive", "அரசியலமைப்பு சி.ஏ.ஜியின் சான்றிதழை இறுதியானது என அறிவித்துள்ளதால் இந்த ஆட்சேபனையை நீதிமன்றத்தில் தொடர முடியாது"),
            ("The dispute is automatically referred to a five-judge Constitution Bench of the Supreme Court", "இச்சர்ச்சை உச்ச நீதிமன்றத்தின் ஐந்து நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வுக்கு தானாகவே அனுப்பப்படும்"),
            ("The Inter-State Council has statutory jurisdiction to overrule the CAG's figures", "சி.ஏ.ஜியின் புள்ளிவிவரங்களை ரத்து செய்ய மாநிலங்களுக்கு இடையேயான கவுன்சிலுக்கு சட்டப்பூர்வ அதிகாரம் உள்ளது"),
            ("The Governor of the aggrieved State can issue an executive ordinance revising the net proceeds", "பாதிக்கப்பட்ட மாநில ஆளுநர் அவசரச் சட்டம் பிறப்பித்து நிகர வருமானத்தை மாற்றியமைக்கலாம்")
        ],
        "exp_en": "Article 279(1) explicitly mandates: 'the net proceeds... shall be ascertained and certified by the Comptroller and Auditor-General of India, whose certificate shall be final.' This constitutional finality bars judicial or intergovernmental challenges.",
        "exp_ta": "சரத்து 279(1) திட்டவட்டமாகக் கூறுகிறது: 'நிகர வருவாய் இந்தியத் தலைமைக் கணக்குத் தணிக்கையாளரால் கணக்கிடப்பட்டு சான்றளிக்கப்படும்; அவரது சான்றிதழ் இறுதியானது.' இது நீதிமன்ற அல்லது அரசுகளுக்கிடையேயான வழக்குகளைத் தடுக்கிறது.",
        "tip_en": "Article 279 certificate is final, conclusive, and non-justiciable.",
        "tip_ta": "சரத்து 279 சான்றிதழ் இறுதியானது, முடிவானது மற்றும் நீதிமன்றத்தில் கேள்வி கேட்க முடியாதது.",
        "fact_en": "Net proceeds determines the exact divisible pool shared via Finance Commission awards.",
        "fact_ta": "நிகர வருவாயே நிதி ஆணையப் பரிந்துரைகளின்படி பகிர்ந்தளிக்கப்படும் தொகையைத் தீர்மானிக்கிறது."
    },
    # 8
    {
        "subtopic": "Audit of Capitalized Interest in Infra Projects",
        "stem_en": "When auditing mega infrastructure projects funded by external sovereign loans, how does the CAG treat Interest During Construction (IDC)?",
        "stem_ta": "வெளிநாட்டு இறையாண்மைக் கடன்களால் நிதியளிக்கப்படும் மெகா உள்கட்டமைப்புத் திட்டங்களைத் தணிக்கை செய்யும் போது, கட்டுமானத்தின் போதான வட்டியை (IDC) சி.ஏ.ஜி எவ்வாறு கையாள்கிறது?",
        "options": [
            ("Scrutinizes whether IDC was improperly capitalized beyond the commercial commissioning date to mask cost overruns", "செலவு அதிகரிப்பை மறைக்க வணிகரீதியான தொடக்கத் தேதியைத் தாண்டியும் IDC முறையற்ற முறையில் மூலதனமாக்கப்பட்டதா என்பதை ஆய்வு செய்கிறது"),
            ("Orders the immediate deduction of interest from the contractor's performance bank guarantee", "ஒப்பந்தக்காரரின் வங்கி உத்தரவாதத்திலிருந்து வட்டியை உடனடியாகப் பிடித்தம் செய்ய உத்தரவிடுகிறது"),
            ("Recommends conversion of all sovereign loans into non-repayable equity grants", "அனைத்து இறையாண்மைக் கடன்களையும் திரும்பச் செலுத்தத் தேவையில்லாத பங்கு மானியங்களாக மாற்ற பரிந்துரைக்கிறது"),
            ("Ignores IDC as it falls strictly under private international commercial law", "IDC சர்வதேச வணிகச் சட்டத்தின் கீழ் வருவதால் அதை முற்றிலும் புறக்கணிக்கிறது")
        ],
        "exp_en": "In infrastructure project audits (e.g. thermal power, metros, ports), CAG rigorously tests whether Interest During Construction (IDC) was artificially inflated or continued past commercial operation dates, creating undue tariff burdens on consumers.",
        "exp_ta": "உள்கட்டமைப்புத் திட்டத் தணிக்கைகளில், வணிக ரீதியான இயக்கம் தொடங்கிய பிறகும் வட்டி தவறாக திட்டச் செலவில் சேர்க்கப்பட்டு நுகர்வோர் மீது அதிகக் கட்டணச் சுமை சுமத்தப்பட்டதா என்பதை சி.ஏ.ஜி தீவிரமாக ஆராய்கிறது.",
        "tip_en": "IDC capitalization audit protects tariff-payers from project delays and executive inefficiency.",
        "tip_ta": "IDC மூலதனமாக்கல் தணிக்கை திட்டத் தாமதங்கள் மற்றும் வீண் செலவுகளிலிருந்து மின்/சேவைக் கட்டண செலுத்துவோரைப் பாதுகாக்கிறது.",
        "fact_en": "CAG's power sector audits frequently expose unjustified IDC inflations.",
        "fact_ta": "மின் துறை மீதான சி.ஏ.ஜி தணிக்கைகள் நியாயமற்ற IDC உயர்வுகளை அடிக்கடி வெளிப்படுத்துகின்றன."
    },
    # 9
    {
        "subtopic": "Section 15 Specific Purpose Grants Scrutiny",
        "stem_en": "Under Section 15 of the CAG Act 1971, what specific power is conferred on the CAG regarding grants or loans given for specific purposes?",
        "stem_ta": "1971 சி.ஏ.ஜி சட்டத்தின் பிரிவு 15-ன் கீழ், குறிப்பிட்ட நோக்கங்களுக்காக வழங்கப்படும் மானியங்கள் அல்லது கடன்கள் தொடர்பாக சி.ஏ.ஜிக்கு வழங்கப்படும் பிரத்யேக அதிகாரம் என்ன?",
        "options": [
            ("Right to scrutinize the procedures by which the sanctioning authority satisfies itself as to the fulfillment of grant conditions", "அனுமதி வழங்கும் அதிகாரம் மானிய நிபந்தனைகள் நிறைவேற்றப்பட்டதை உறுதி செய்யும் நடைமுறைகளை ஆய்வு செய்யும் உரிமை"),
            ("Power to attach and auction the personal property of default grant recipients", "மானிய நிபந்தனையை மீறியவர்களின் தனிப்பட்ட சொத்துக்களை பறிமுதல் செய்து ஏலம் விடும் அதிகாரம்"),
            ("Power to take over direct administrative management of the aided body", "உதவி பெறும் அமைப்பின் நேரடி நிர்வாகத்தை சி.ஏ.ஜியே கையகப்படுத்தும் அதிகாரம்"),
            ("Power to convert central tied grants into untied general revenues", "குறிப்பிட்ட நோக்கத்திற்கான மானியங்களை பொது வருவாயாக மாற்றும் அதிகாரம்")
        ],
        "exp_en": "Section 15 empowers the CAG to scrutinize the administrative procedures by which the sanctioning authority satisfies itself as to the due fulfillment of the conditions subject to which such grants or loans were given.",
        "exp_ta": "பிரிவு 15, மானியங்கள் அல்லது கடன்கள் எந்த நிபந்தனைகளின் கீழ் வழங்கப்பட்டனவோ, அந்த நிபந்தனைகள் முறையாக நிறைவேற்றப்பட்டனவா என்பதை அனுமதி வழங்கிய அதிகாரி எவ்வாறு உறுதி செய்தார் என்ற நடைமுறையை ஆய்வு செய்ய சி.ஏ.ஜிக்கு அதிகாரம் அளிக்கிறது.",
        "tip_en": "Section 15 targets the monitoring mechanism of the granting ministry.",
        "tip_ta": "பிரிவு 15 மானியம் வழங்கிய அமைச்சகத்தின் கண்காணிப்பு நடைமுறைகளை ஆய்வு செய்கிறது.",
        "fact_en": "Utilization Certificates (UCs) submitted by grant recipients are scrutinized under Section 15.",
        "fact_ta": "மானியப் பயன்பாட்டுச் சான்றிதழ்கள் (UCs) பிரிவு 15-ன் கீழ் ஆய்வு செய்யப்படுகின்றன."
    },
    # 10
    {
        "subtopic": "Audit Memos and Natural Justice",
        "stem_en": "Why does the CAG audit process mandate the holding of an 'Exit Conference' with audited departments prior to finalizing an audit report?",
        "stem_ta": "தணிக்கை அறிக்கையை இறுதி செய்வதற்கு முன், தணிக்கை செய்யப்பட்ட துறைகளுடன் 'இறுதிக் கூட்டம்' (Exit Conference) நடத்துவதை சி.ஏ.ஜி தணிக்கை நடைமுறை ஏன் கட்டாயமாக்குகிறது?",
        "options": [
            ("To satisfy the principles of natural justice by giving the executive an opportunity to explain audit findings and place counter-facts on record", "நிர்வாகத்திற்கு தனது விளக்கத்தை அளிக்கவும் எதிர் உண்மைகளை ஆவணப்படுத்தவும் வாய்ப்பளித்து இயற்கை நீதிக் கொள்கைகளை பூர்த்தி செய்ய"),
            ("To negotiate and tone down uncomfortable political findings with ministers", "அமைச்சர்களுடன் பேசி சங்கடமான அரசியல் கண்டுபிடிப்புகளை சமரசம் செய்து குறைக்க"),
            ("To obtain prior written approval from the Cabinet Secretary for publishing the report", "அறிக்கையை வெளியிட அமைச்சரவைச் செயலாளரிடம் முன் எழுத்துப்பூர்வ ஒப்புதல் பெற"),
            ("To determine the exact financial penalty to be deducted from civil servants' salaries", "அரசு ஊழியர்களின் ஊதியத்திலிருந்து பிடித்தம் செய்யப்பட வேண்டிய அபராதத் தொகையை நிர்ணயிக்க")
        ],
        "exp_en": "The Exit Conference embodies the core administrative law doctrine of audi alteram partem (hear the other side), ensuring audit reports are objective, balanced, and reflect the verified formal position of the executive.",
        "exp_ta": "இறுதிக் கூட்டம் என்பது 'மறுதரப்பு நியாயத்தைக் கேட்டல்' என்ற இயற்கை நீதிக் கோட்பாட்டை நிலைநிறுத்துகிறது; இது தணிக்கை அறிக்கைகள் ஒருதலைப்பட்சமாக இல்லாமல் நடுநிலையாக இருப்பதை உறுதி செய்கிறது.",
        "tip_en": "Exit Conference is mandatory under Regulations on Audit and Accounts 2007/2020.",
        "tip_ta": "தணிக்கை மற்றும் கணக்குகள் ஒழுங்குமுறைகளின் கீழ் முடிவுக் கூட்டத்தை நடத்துவது கட்டாயமாகும்.",
        "fact_en": "If the department's reply refutes an audit observation with verified facts, the paragraph is dropped.",
        "fact_ta": "துறையின் பதில் உண்மைகளுடன் தணிக்கைக் குறிப்பை மறுத்தால், அந்த தணிக்கைப் பத்தி கைவிடப்படும்."
    }
]

# Let's add questions 11 to 50 programmatically or in structured list
raw_gt_part1_continued = [
    # 11
    {
        "subtopic": "Net Proceeds and Local Bodies",
        "stem_en": "Can the CAG's calculation of net proceeds under Article 279 include collections from non-tax penalties and confiscations?",
        "stem_ta": "சரத்து 279-ன் கீழ் சி.ஏ.ஜியின் நிகர வருமானக் கணக்கீட்டில் வரி அல்லாத அபராதங்கள் மற்றும் பறிமுதல்கள் மூலம் வரும் வருவாயைச் சேர்க்க முடியுமா?",
        "options": [
            ("No, net proceeds relates strictly to taxes and duties levied and collected by the Union", "இல்லை, நிகர வருமானம் என்பது மத்திய அரசால் விதிக்கப்பட்டு வசூலிக்கப்படும் வரிகள் மற்றும் தீர்வைக்கு மட்டுமே பொருந்தும்"),
            ("Yes, all penal fines are automatically treated as divisible direct income taxes", "ஆம், அனைத்து அபராதங்களும் தானாகவே பிரிக்கக்கூடிய நேரடி வருமான வரியாகக் கருதப்படும்"),
            ("Yes, but only if the Supreme Court approves the inclusion by a special reference", "ஆம், ஆனால் உச்ச நீதிமன்றம் சிறப்பு குறிப்புரை மூலம் அனுமதித்தால் மட்டுமே சேர்க்கலாம்"),
            ("No, net proceeds includes only state excise duties", "இல்லை, நிகர வருமானம் மாநில கலால் வரிகளை மட்டுமே உள்ளடக்கியது")
        ],
        "exp_en": "Article 279 defines net proceeds in relation to any tax or duty as the proceeds thereof reduced by the cost of collection. It strictly governs tax revenue divisible between the Union and States.",
        "exp_ta": "சரத்து 279 நிகர வருவாயை வரிகள் அல்லது தீர்வைகளின் வருவாயிலிருந்து வசூல் செலவைக் கழித்த தொகையாக வரையறுக்கிறது. இது மத்திய-மாநில வரிப் பகிர்வுக்கு மட்டுமே பொருந்தும்.",
        "tip_en": "Net proceeds excludes general non-tax revenues like spectrum auction proceeds or railway tariffs.",
        "tip_ta": "நிகர வருமானம் அலைக்கற்றை ஏலம் அல்லது ரயில்வே கட்டணம் போன்ற வரி அல்லாத வருவாய்களை உள்ளடக்காது.",
        "fact_en": "Cost of collection is determined on an actual audited basis by the CAG.",
        "fact_ta": "வசூல் செலவு சி.ஏ.ஜியால் உண்மையான தணிக்கை அடிப்படையில் கணக்கிடப்படுகிறது."
    },
    # 12
    {
        "subtopic": "Audit of Discoms Jurisprudence",
        "stem_en": "In Delhi High Court's ruling on private electricity distribution companies (Discoms), what was held regarding CAG audit?",
        "stem_ta": "தனியார் மின் விநியோக நிறுவனங்கள் (Discoms) தொடர்பான டெல்லி உயர் நீதிமன்றத் தீர்ப்பில் சி.ஏ.ஜி தணிக்கை குறித்து என்ன கூறப்பட்டது?",
        "options": [
            ("Private discoms operating on public licenses can be audited under Section 20 if ordered in the public interest", "பொது உரிமத்தில் இயங்கும் தனியார் மின் நிறுவனங்களை பொது நலன் கருதி உத்தரவிட்டால் பிரிவு 20-ன் கீழ் தணிக்கை செய்யலாம்"),
            ("Private companies are absolutely immune from constitutional audit under all circumstances", "தனியார் நிறுவனங்கள் அனைத்து சூழ்நிலைகளிலும் அரசியலமைப்பு தணிக்கையிலிருந்து முழு விலக்கு பெற்றவை"),
            ("Discom audits can only be conducted by international chartered accountant syndicates", "மின் நிறுவன தணிக்கையை சர்வதேச பட்டயக் கணக்காளர்கள் கூட்டமைப்பு மட்டுமே நடத்த முடியும்"),
            ("The CAG can only audit companies where the Government owns 100% of equity", "அரசு 100% பங்குகளை வைத்துள்ள நிறுவனங்களை மட்டுமே சி.ஏ.ஜி தணிக்கை செய்ய முடியும்")
        ],
        "exp_en": "The Delhi High Court upheld the Lieutenant Governor's direction entrusting CAG audit of private discoms under Section 20 of the 1971 Act, holding that consumer welfare and public revenue tariffs involve deep public interest.",
        "exp_ta": "1971 சட்டத்தின் பிரிவு 20-ன் கீழ் தனியார் மின் நிறுவனங்களை சி.ஏ.ஜி தணிக்கை செய்ய துணைநிலை ஆளுநர் பிறப்பித்த உத்தரவை டெல்லி உயர் நீதிமன்றம் உறுதி செய்தது, ஏனெனில் நுகர்வோர் நலன் பொது நலனுடன் தொடர்புடையது.",
        "tip_en": "Section 20 allows audit of private utilities where public interest and state revenue are involved.",
        "tip_ta": "பொது நலனும் அரசு வருவாயும் சம்பந்தப்பட்டிருக்கும் போது பிரிவு 20 தனியார் நிறுவனத் தணிக்கையை அனுமதிக்கிறது.",
        "fact_en": "Discoms appealed this decision to the Supreme Court where the jurisdictional interplay with DERC was argued.",
        "fact_ta": "DERC ஒழுங்குமுறை அதிகாரத்துடன் உள்ள தொடர்பு குறித்து உச்ச நீதிமன்றத்தில் மேல்முறையீடு செய்யப்பட்டது."
    },
    # 13
    {
        "subtopic": "Appointment of Additional Deputy CAGs",
        "stem_en": "Who sanctions the creation of posts of Deputy Comptroller and Auditor General (Dy CAG)?",
        "stem_ta": "துணைத் தலைமைக் கணக்குத் தணிக்கையாளர் (Dy CAG) பணியிடங்களை உருவாக்குவதற்கு ஒப்புதல் அளிப்பவர் யார்?",
        "options": [
            ("The President of India on the advice of the Union Government in consultation with the CAG", "சி.ஏ.ஜியுடன் கலந்தாலோசித்து மத்திய அரசின் ஆலோசனையின் பேரில் இந்தியக் குடியரசுத் தலைவர்"),
            ("The Public Accounts Committee by passing a resolution in Lok Sabha", "மக்களவையில் தீர்மானம் நிறைவேற்றுவதன் மூலம் பொதுக் கணக்குக் குழு"),
            ("The UPSC under its autonomous civil service creation powers", "யு.பி.எஸ்.சி தனது குடிமைப் பணி உருவாக்கும் அதிகாரத்தின் கீழ்"),
            ("The Supreme Court of India under Article 142", "சரத்து 142-ன் கீழ் இந்திய உச்ச நீதிமன்றம்")
        ],
        "exp_en": "Deputy CAGs are created by the Union Government and appointed under rules framed under Article 148(5) by the President after consultation with the CAG.",
        "exp_ta": "சரத்து 148(5)-ன் கீழ் சி.ஏ.ஜியுடன் கலந்தாலோசித்து குடியரசுத் தலைவரால் உருவாக்கப்பட்ட விதிகளின் கீழ் மத்திய அரசால் துணை சி.ஏ.ஜி பணியிடங்கள் உருவாக்கப்படுகின்றன.",
        "tip_en": "Deputy CAGs are the apex administrative heads below the constitutional CAG.",
        "tip_ta": "துணை சி.ஏ.ஜிக்கள் அரசியலமைப்பு சி.ஏ.ஜிக்கு அடுத்த நிலையில் உள்ள உச்ச நிர்வாகத் தலைவர்களாவர்.",
        "fact_en": "Deputy CAGs are drawn from the senior-most ranks of the Indian Audit and Accounts Service (IA&AS).",
        "fact_ta": "துணை சி.ஏ.ஜிக்கள் IA&AS பணியின் மிக மூத்த அதிகாரிகளிலிருந்து நியமிக்கப்படுகின்றனர்."
    },
    # 14
    {
        "subtopic": "Audit of Public Accounts Receipts",
        "stem_en": "Under Section 13 of the 1971 Act, how does the CAG audit transactions in the Public Account of India?",
        "stem_ta": "1971 சட்டத்தின் பிரிவு 13-ன் கீழ், இந்தியப் பொதுக் கணக்கில் உள்ள பரிவர்த்தனைகளை சி.ஏ.ஜி எவ்வாறு தணிக்கை செய்கிறார்?",
        "options": [
            ("Audits all transactions relating to debt, deposits, sinking funds, advances, and suspense accounts", "கடன், வைப்புத்தொகை, மூழ்கும் நிதி, முன்பணங்கள் மற்றும் இடைநிறுத்தக் கணக்குகள் தொடர்பான அனைத்து பரிவர்த்தனைகளையும் தணிக்கை செய்கிறது"),
            ("Public Account transactions are exempt from CAG audit as they belong to private depositors", "பொதுக் கணக்கு பரிவர்த்தனைகள் தனியார் முதலீட்டாளர்களுக்கு உரியவை என்பதால் சி.ஏ.ஜி தணிக்கையிலிருந்து விலக்கு பெற்றவை"),
            ("Audits only transactions where the interest rate exceeds 10% per annum", "ஆண்டுக்கு 10%-க்கு மேல் வட்டி விகிதம் உள்ள பரிவர்த்தனைகளை மட்டுமே தணிக்கை செய்கிறது"),
            ("Entrusts the entire Public Account audit to district cooperative banks", "முழு பொதுக் கணக்குத் தணிக்கையையும் மாவட்ட கூட்டுறவு வங்கிகளிடம் ஒப்படைக்கிறது")
        ],
        "exp_en": "Section 13 mandates the CAG to audit all transactions of the Union and States relating to debt, deposits, sinking funds, advances, suspense accounts, and remittance business in the Public Account.",
        "exp_ta": "பிரிவு 13 பொதுக் கணக்கில் உள்ள கடன், வைப்புத்தொகை, கடனைத் தீர்க்கும் நிதி, முன்பணங்கள் மற்றும் இடைநிறுத்தக் கணக்குகள் தொடர்பான அனைத்து மத்திய, மாநில பரிவர்த்தனைகளையும் தணிக்கை செய்ய சி.ஏ.ஜிக்கு உத்தரவிடுகிறது.",
        "tip_en": "Public Account funds are held by the government in a fiduciary/banking capacity.",
        "tip_ta": "பொதுக் கணக்கு நிதிகள் அரசின் வசம் அறக்கட்டளைப் பொறுப்பில் வைக்கப்பட்டுள்ளன.",
        "fact_en": "Balances in the Public Account are scrutinized to detect unauthorized parking of budgetary funds.",
        "fact_ta": "பட்ஜெட் நிதியை செலவிடாமல் பதுக்கி வைப்பதைக் கண்டறிய பொதுக் கணக்கு நிலுவைகள் தீவிரமாக ஆய்வு செய்யப்படுகின்றன."
    },
    # 15
    {
        "subtopic": "Performance Audit Guidelines Publication",
        "stem_en": "Under which statutory power does the CAG issue official Performance Audit and Compliance Audit Guidelines?",
        "stem_ta": "எந்த சட்டப்பூர்வ அதிகாரத்தின் கீழ் சி.ஏ.ஜி அதிகாரப்பூர்வ செயல்திறன் தணிக்கை மற்றும் இணக்கத் தணிக்கை வழிகாட்டுதல்களை வெளியிடுகிறார்?",
        "options": [
            ("Section 23 of the CAG (DPC) Act 1971", "1971 சி.ஏ.ஜி (DPC) சட்டத்தின் பிரிவு 23"),
            ("Section 5 of the RTI Act 2005", "2005 தகவல் அறியும் உரிமைச் சட்டத்தின் பிரிவு 5"),
            ("Article 76 of the Constitution", "அரசியலமைப்பின் சரத்து 76"),
            ("Section 133 of the Companies Act 2013", "நிறுவனங்கள் சட்டம் 2013-ன் பிரிவு 133")
        ],
        "exp_en": "Section 23 of the CAG (DPC) Act 1971 empowers the CAG to make regulations for carrying into effect the provisions of the Act in so far as they relate to the scope and extent of audit.",
        "exp_ta": "1971 சி.ஏ.ஜி சட்டத்தின் பிரிவு 23, தணிக்கையின் வரம்பு மற்றும் அளவு தொடர்பான சட்ட விதிகளுக்குச் செயல்வடிவம் கொடுக்க ஒழுங்குமுறைகளை வகுக்க சி.ஏ.ஜிக்கு அதிகாரம் அளிக்கிறது.",
        "tip_en": "Section 23 = Rule-making power of CAG for audit scope and guidelines.",
        "tip_ta": "பிரிவு 23 = தணிக்கை வரம்பு மற்றும் ஒழுங்குமுறைகளை வகுக்கும் சி.ஏ.ஜியின் சட்டப்பூர்வ அதிகாரம்.",
        "fact_en": "Regulations on Audit and Accounts 2007 (updated 2020) were notified under Section 23.",
        "fact_ta": "2007 தணிக்கை ஒழுங்குமுறைகள் பிரிவு 23-ன் கீழேயே அரசிதழில் வெளியிடப்பட்டன."
    }
]
raw_gt_part1_data.extend(raw_gt_part1_continued)

# We will generate questions 16 to 50 using comprehensive high-yield items
more_gt_part1_items = [
    ("Audit of PM CARES Fund Status", "Why is the PM CARES Fund not audited by the CAG of India?", "It is established as a public charitable trust funded purely by voluntary private contributions, not budgetary appropriations from the CFI", "இது பொதுத் தொண்டு அறக்கட்டளையாக தனியார் பங்களிப்புகள் மூலம் நிறுவப்பட்டதால், CFI பட்ஜெட் ஒதுக்கீட்டைப் பெறாததால் சி.ஏ.ஜியால் தணிக்கை செய்யப்படுவதில்லை", "Consolidated Fund of India funding is the jurisdictional trigger for mandatory constitutional audit.", "CFI பொது நிதி ஒதுக்கீடு இருந்தால்தான் அரசியலமைப்பு கட்டாயத் தணிக்கை பொருந்தும்.", "PM CARES is audited by an independent chartered accountant firm appointed by its trustees.", "PM CARES அறக்கட்டளை நியமிக்கும் பட்டயக் கணக்காளர்களால் தணிக்கை செய்யப்படுகிறது."),
    ("Audit of Defense Secret Projects", "How does the CAG audit sensitive defense research laboratories like DRDO?", "Examines financial propriety and procurement compliance while redacting classified weapon specifications in published reports", "ரகசிய ஆயுத விவரங்களை பொது அறிக்கையிலிருந்து நீக்கிவிட்டு நிதி ஒழுங்கு மற்றும் கொள்முதல் இணக்கத்தை மட்டுமே தணிக்கை செய்கிறது", "National security redaction protects classified defense data without compromising financial accountability.", "தேசிய பாதுகாப்பு ரகசியங்கள் நீக்கப்பட்டு நிதிப் பொறுப்புடைமை உறுதி செய்யப்படுகிறது.", "CAG tabled a comprehensive performance audit of DRDO missile projects in 2022.", "2022-ல் DRDO ஏவுகணைத் திட்டங்கள் மீதான தணிக்கை அறிக்கையை சி.ஏ.ஜி சமர்ப்பித்தது."),
    ("Audit of Autonomous Port Trusts", "Under what authority are Major Port Authorities in India audited by the CAG?", "Under Major Port Authorities Act 2021 read with Section 19(2) of the CAG Act", "2021 முக்கிய துறைமுகங்கள் சட்டத்துடன் இணைந்த 1971 சி.ஏ.ஜி சட்டத்தின் பிரிவு 19(2)-ன் கீழ்", "Statutory corporations are audited under Section 19(2) as mandated by their founding parliamentary statutes.", "நாடாளுமன்ற சட்டங்களால் உருவாக்கப்பட்ட சட்டப்பூர்வ கழகங்கள் பிரிவு 19(2)-ன் கீழ் தணிக்கை செய்யப்படுகின்றன.", "Major Ports submit annual Separate Audit Reports (SARs) to Parliament.", "முக்கிய துறைமுகங்கள் நாடாளுமன்றத்தில் தனித் தணிக்கை அறிக்கைகளை (SARs) சமர்ப்பிக்கின்றன."),
    ("Audit of Compensatory Afforestation Fund (CAMPA)", "What did the CAG highlight in its performance audit of the CAMPA Fund?", "Massive unspent funds parked in commercial banks and sluggish tree plantation monitoring", "செலவிடப்படாத பெரும் நிதி வங்கிகளில் முடக்கப்பட்டதையும் மரக்கன்றுகள் நடும் பணிகளில் போதிய கண்காணிப்பு இல்லாததையும் சுட்டிக்காட்டியது", "CAMPA funds must be transferred to the Public Account of India under the CAMPA Act 2016.", "CAMPA நிதிகள் 2016 சட்டத்தின் கீழ் பொதுக் கணக்கிற்கு மாற்றப்பட வேண்டும்.", "CAG found thousands of crores lying idle in bank accounts for years.", "ஆயிரக்கணக்கான கோடி ரூபாய் வங்கிக் கணக்குகளில் பல ஆண்டுகளாக முடங்கிக் கிடந்ததை சி.ஏ.ஜி வெளிப்படுத்தியது."),
    ("Audit of National Highway Concessions", "How does the CAG audit NHAI toll concession agreements with private concessionaires?", "Verifies traffic census data, toll fee collections, and compliance with revenue sharing formulas", "போக்குவரத்து கணக்கெடுப்பு தரவு, சுங்கக் கட்டண வசூல் மற்றும் வருவாய்ப் பகிர்வு சூத்திரங்களை சரிபார்க்கிறது", "Toll concession audit protects the road users and ensures the public exchequer receives its lawful revenue share.", "சுங்கத் தணிக்கை சாலைப் பயணிகளைப் பாதுகாப்பதுடன் அரசுக்குரிய வருவாய் கிடைப்பதை உறுதி செய்கிறது.", "NHAI performance audit reports are heavily scrutinized by the PAC.", "NHAI செயல்திறன் தணிக்கை அறிக்கைகள் PAC-ஆல் தீவிரமாக ஆய்வு செய்யப்படுகின்றன."),
    ("Role of Principal Director of Audit", "What is the primary role of a Principal Director of Audit (PDA) in the IA&AD?", "Heads a specialized central audit office overseeing a major railway zone or defense command", "முக்கிய ரயில்வே மண்டலம் அல்லது ராணுவப் பிரிவை மேற்பார்வையிடும் சிறப்பு மத்திய தணிக்கை அலுவலகத்திற்கு தலைமை தாங்குகிறார்", "PDAs handle specialized central government sectors across geographical zones.", "PDA அதிகாரிகள் மண்டலங்கள் முழுவதும் குறிப்பிட்ட மத்திய அரசுத் துறைகளைக் கையாள்கின்றனர்.", "PDA Railway offices are co-located with Zonal Railway headquarters.", "ரயில்வே மண்டலத் தலைமையகங்களில் PDA அலுவலகங்கள் அமைந்துள்ளன."),
    ("Audit of Indian Embassies Abroad", "Which specialized wing of the CAG audits Indian diplomatic missions and embassies overseas?", "Director General of Audit, Central Expenditure (Foreign Audit Wing)", "தணிக்கை தலைமை இயக்குநர், மத்திய செலவினம் (வெளிநாட்டுத் தணிக்கைப் பிரிவு)", "Foreign missions are audited on a multi-year rotational cycle by specialized audit teams dispatched from New Delhi.", "புது தில்லியிலிருந்து அனுப்பப்படும் சிறப்புத் தணிக்கைக் குழுக்கள் வெளிநாட்டு தூதரகங்களைத் தணிக்கை செய்கின்றன.", "Scrutinizes visa fee collections, property leases, and consular expenditures.", "விசா கட்டண வசூல், கட்டிட வாடகைகள் மற்றும் தூதரகச் செலவினங்களை ஆய்வு செய்கிறது."),
    ("Audit of Railway Commercial Operations", "What is the primary focus of CAG's audit of Indian Railways commercial operations?", "Operating ratio, wagon turnaround time, freight earnings, and punctuality performance", "செயல்பாட்டு விகிதம் (Operating Ratio), வேகன் பயன்பாட்டு நேரம், சரக்கு வருவாய் மற்றும் ரயில் இயக்க நேரம்", "The operating ratio reflects the proportion of working expenses to gross traffic receipts.", "செயல்பாட்டு விகிதம் மொத்த வருவாயில் அன்றாட செலவினங்களின் சதவீதத்தைக் காட்டுகிறது.", "CAG repeatedly warned that Railways' operating ratio has remained above 95%.", "ரயில்வேயின் செயல்பாட்டு விகிதம் 95%-க்கு மேல் இருப்பதை சி.ஏ.ஜி தொடர்ந்து எச்சரித்துள்ளது."),
    ("Audit of Air India Sale Process", "In the performance audit of Air India disinvestment, what key aspect was analyzed by CAG?", "Reserve price valuation, transfer of non-core assets to AIAHL, and debt carve-out mechanisms", "அடிப்படை விலை நிர்ணயம், முதன்மையற்ற சொத்துக்கள் AIAHL-க்கு மாற்றம் மற்றும் கடன் தள்ளுபடி வழிமுறைகள்", "CAG ensures that public assets are transferred to private bidders without sovereign under-recovery.", "பொதுச் சொத்துக்கள் தனியார் ஏலதாரர்களுக்கு குறைத்து விற்கப்படாமல் இருப்பதை சி.ஏ.ஜி உறுதி செய்கிறது.", "Air India was officially handed over to the Tata Group in January 2022.", "ஜனவரி 2022-ல் ஏர் இந்தியா அதிகாரப்பூர்வமாக டாடா குழுமத்திடம் ஒப்படைக்கப்பட்டது."),
    ("Audit of Coastal Zone Management", "What was the main finding in CAG's audit of Coastal Regulation Zone (CRZ) enforcement?", "Illegal commercial constructions, absence of Coastal Zone Management Plans, and mangrove destruction", "சட்டவிரோத வணிகக் கட்டுமானங்கள், மண்டல மேலாண்மைத் திட்டங்கள் இல்லாமை மற்றும் அலையாத்தி காடுகள் அழிப்பு", "CRZ audit checks statutory compliance with MoEFCC environmental notifications.", "CRZ தணிக்கை மத்திய சுற்றுச்சூழல் அமைச்சகத்தின் சட்டப்பூர்வ விதிமுறைகளைச் சோதிக்கிறது.", "States were severely pulled up for delaying the notification of coastal maps.", "கடலோர வரைபடங்களை வெளியிட தாமதித்ததற்காக மாநில அரசுகள் கண்டிக்கப்பட்டன."),
    ("CAG's Code of Ethics", "The Code of Ethics promulgated by the CAG of India is based on which INTOSAI standard?", "ISSAI 130 (Code of Ethics for Supreme Audit Institutions)", "ISSAI 130 (உச்ச தணிக்கை அமைப்புகளுக்கான நெறிமுறை விதிமுறைகள்)", "ISSAI 130 sets the global benchmark for auditor integrity, independence, objectivity, and confidentiality.", "ISSAI 130 நேர்மை, சுதந்திரம் மற்றும் ரகசியக் காப்பிற்கான உலகளாவிய தரநிலையாகும்.", "All IA&AD personnel must subscribe annually to this ethical pledge.", "IA&AD துறையின் அனைத்துப் பணியாளர்களும் இந்த நெறிமுறை உறுதிமொழியை ஏற்க வேண்டும்."),
    ("Audit of Centrally Sponsored Schemes (CSS)", "How does the CAG audit Centrally Sponsored Schemes implemented through State Societies?", "Directly audits both Union line ministry releases and field implementation by State implementing agencies", "மத்திய அமைச்சக நிதி விடுவிப்பு மற்றும் மாநில முகமைகளின் களச் செயல்பாடு இரண்டையுமே நேரடியாகத் தணிக்கை செய்கிறது", "CSS funding flows from Consolidated Fund of India down to district implementation bodies.", "மத்திய திட்டம் CFI-லிருந்து மாவட்ட அளவிலான முகமைகள் வரை நிதியைப் பாய்ச்சுகிறது.", "Audit covers flagship schemes like Samagra Shiksha, PMGSY, and Jal Jeevan Mission.", "சமக்ர சிக்ஷா, கிராம சாலைத் திட்டம், ஜல் ஜீவன் இயக்கம் ஆகியவை தணிக்கைக்கு உட்பட்டவை."),
    ("Audit of Disaster Mitigation Fund (NDMF)", "How does CAG audit verify the statutory allocation to the National Disaster Mitigation Fund?", "Ensures that 20% of total disaster risk management funding is ring-fenced for prevention and mitigation", "மொத்த பேரிடர் மேலாண்மை நிதியில் 20% தடுப்பு மற்றும் தணிப்புப் பணிகளுக்கு பிரத்யேகமாக ஒதுக்கப்படுவதை உறுதி செய்கிறது", "Section 47 of the Disaster Management Act 2005 mandates dedicated mitigation funding.", "2005 பேரிடர் மேலாண்மைச் சட்டத்தின் பிரிவு 47 பிரத்யேக தணிப்பு நிதியை கட்டாயமாக்குகிறது.", "Mitigation funds cannot be diverted for ex-gratia relief or immediate sustenance.", "தணிப்பு நிதியை உடனடி நிவாரணம் அல்லது இழப்பீட்டுக்கு மாற்ற முடியாது."),
    ("CAG Audit of Export Incentives (RoDTEP)", "What does the CAG scrutinize in the audit of export incentive schemes like RoDTEP?", "Whether tax refund rates were computed on verified embedded taxes without over-compensating exporters", "உண்மையான வரிச் சுமைகளின் அடிப்படையில் பணத்தைத் திருப்பி அளிக்கும் விகிதம் கணக்கிடப்பட்டதா என ஆராய்கிறது", "Export subsidies must comply with WTO rules and accurate fiscal cost verification.", "ஏற்றுமதி ஊக்கத்தொகைகள் WTO விதிகள் மற்றும் உண்மையான நிதிச் செலவு சரிபார்ப்பிற்கு உட்பட வேண்டும்.", "RoDTEP replaced the earlier Merchandise Exports from India Scheme (MEIS).", "RoDTEP திட்டம் முந்தைய MEIS திட்டத்திற்குப் பதிலாக அறிமுகப்படுத்தப்பட்டது."),
    ("Audit of Central Vista Project", "What was the audit focus of the CAG on the Central Vista Redevelopment Project?", "Statutory environmental clearances, tender transparency, cost variations, and contractor milestone compliance", "சட்டப்பூர்வ சுற்றுச்சூழல் அனுமதிகள், டெண்டர் வெளிப்படைத்தன்மை மற்றும் செலவு மாறுபாடுகள்", "Large capital works undergo comprehensive compliance and propriety audit during execution.", "பெரிய மூலதனக் கட்டுமானங்கள் செயல்படுத்தலின் போதே முழுமையான இணக்க மற்றும் நாணயத் தணிக்கைக்கு உட்படுகின்றன.", "Monitored under the Ministry of Housing and Urban Affairs budget grants.", "மத்திய வீட்டுவசதி மற்றும் நகர்ப்புற விவகாரங்கள் அமைச்சக மானியத்தின் கீழ் கண்காணிக்கப்படுகிறது."),
    ("Audit of Inland Waterways Projects", "What is the primary evaluation metric in CAG's audit of the Jal Marg Vikas Project on NW-1?", "Capacity utilization of multi-modal terminals, fairway dredging maintenance, and cargo tonnage achieved", "பன்முக முனையங்களின் பயன்பாட்டுத் திறன், ஆற்றுப் படுகை தூர்வாருதல் மற்றும் சரக்கு போக்குவரத்து அளவு", "Assesses whether capital dredging investments yielded the projected cargo throughput.", "மூலதன முதலீடுகள் திட்டமிடப்பட்ட சரக்குப் போக்குவரத்தை உருவாக்கினவா என மதிப்பிடுகிறது.", "National Waterway 1 spans the Ganga-Bhagirathi-Hooghly river system from Varanasi to Haldia.", "தேசிய நீர்வழி 1 வாரணாசி முதல் ஹால்டியா வரை கங்கை ஆற்று அமைப்பில் அமைந்துள்ளது."),
    ("Audit of Direct Benefit Transfer for LPG (PAHAL)", "What systemic irregularity was unmasked by the CAG in the PAHAL LPG subsidy scheme audit?", "Commercial diversion of subsidized domestic cylinders and ghost consumer records receiving bank subsidies", "மானியம் பெறும் சிலிண்டர்கள் வணிக பயன்பாட்டிற்கு மாற்றப்பட்டது மற்றும் போலி நுகர்வோர் வங்கிக் கணக்குகளில் மானியம் பெற்றது", "Big Data analytics cross-matched consumer booking patterns to detect anomalies.", "பெருந்தரவு பகுப்பாய்வு நுகர்வோர் முன்பதிவு முறைகளை ஒப்பிட்டு முறைகேடுகளைக் கண்டறிந்தது.", "Saved the exchequer substantial subsidy leakages through Aadhaar de-duplication.", "ஆதார் சரிபார்ப்பு மூலம் அரசு கருவூலத்திற்கு பெரும் மானியக் கசிவுகள் தடுக்கப்பட்டன."),
    ("Audit of Supreme Court Registry Accounts", "Does the CAG have constitutional authority to audit the accounts and administrative expenditure of the Supreme Court?", "Yes, all administrative expenses of the Supreme Court charged on the CFI under Article 146(3) are audited by the CAG", "ஆம், சரத்து 146(3)-ன் கீழ் CFI-ல் பொறுப்பாக்கப்பட்ட உச்ச நீதிமன்றத்தின் அனைத்து நிர்வாகச் செலவுகளையும் சி.ஏ.ஜி தணிக்கை செய்கிறது", "Judicial decisions are immune, but administrative financial transactions of the Court are public accounts.", "தீர்ப்புகள் தணிக்கைக்கு உட்படாது; ஆனால் நீதிமன்ற நிர்வாக நிதிப் பரிவர்த்தனைகள் பொதுக் கணக்காகும்.", "Audit reports on the Supreme Court are tabled annually before Parliament.", "உச்ச நீதிமன்றம் மீதான தணிக்கை அறிக்கைகள் ஆண்டுதோறும் நாடாளுமன்றத்தில் வைக்கப்படுகின்றன."),
    ("Audit of Election Commission Expenditure", "How does the CAG audit election expenditure incurred across States during parliamentary elections?", "Scrutinizes the 50:50 expenditure sharing formula between the Union and State Governments", "மத்திய மற்றும் மாநில அரசுகளுக்கு இடையே உள்ள 50:50 செலவு பகிர்வு சூத்திரத்தை ஆய்வு செய்கிறது", "Lok Sabha election costs are shared equally between the Centre and States; Assembly election costs are borne by States.", "மக்களவைத் தேர்தல் செலவு சரிசமமாகப் பகிரப்படுகிறது; சட்டமன்றத் தேர்தல் செலவை மாநிலங்கள் ஏற்கின்றன.", "CAG audits both polling station logistics and EVM/VVPAT procurement accounts.", "வாக்குச்சாவடி செலவுகள் மற்றும் EVM/VVPAT கொள்முதல் கணக்குகள் இரண்டையும் சி.ஏ.ஜி தணிக்கை செய்கிறது."),
    ("Audit of Special Economic Zones (SEZs)", "What was a major irregularity exposed by the CAG in the performance audit of Special Economic Zones?", "Idle unutilized land allotted to private developers and failure to achieve positive Net Foreign Exchange", "தனியார் நிறுவனங்களுக்கு ஒதுக்கப்பட்ட நிலம் பயன்படுத்தப்படாமல் முடங்கியது மற்றும் ஏற்றுமதி இலக்குகளை அடையத் தவறியது", "SEZ Act 2005 requires developers to generate positive Net Foreign Exchange (NFE) within five years.", "2005 SEZ சட்டம் ஐந்து ஆண்டுகளுக்குள் நிகர அந்நியச் செலாவணியை ஈட்டுவதை கட்டாயமாக்குகிறது.", "CAG exposed tax concessions availed without fulfilling export commitments.", "ஏற்றுமதி கடமைகளை நிறைவேற்றாமல் வரிச் சலுகைகள் பெறப்பட்டதை சி.ஏ.ஜி வெளிப்படுத்தியது."),
    ("Audit of Pradhan Mantri Awas Yojana (PMAY)", "What does the CAG verify in geo-tagging audits of houses constructed under PMAY?", "Verifies latitude-longitude coordinates of houses to prevent fraudulent multiple payments for the same physical unit", "ஒரே வீட்டிற்கு பலமுறை மோசடியாக நிதி வழங்கப்படுவதைத் தடுக்க வீடுகளின் புவிசார் குறியீடுகளை (Geo-tagging) சரிபார்க்கிறது", "Digital evidence integration into audit workflows ensures factual ground verification.", "டிஜிட்டல் சான்றுகளை தணிக்கையில் இணைப்பது துல்லியமான கள சரிபார்ப்பை உறுதி செய்கிறது.", "PMAY-G utilizes the AwaasSoft digital platform monitored by the CAG.", "PMAY-G திட்டத்தின் AwaasSoft டிஜிட்டல் தளத்தை சி.ஏ.ஜி கண்காணிக்கிறது."),
    ("Audit of State Power Generation Utilities (Gencos)", "How does the CAG assess the financial viability of State Power Generation Companies (Gencos)?", "Examines Plant Load Factor (PLF), coal blending costs, auxiliary power consumption, and overdue receivables from Discoms", "ஆலை சுமை காரணி (PLF), நிலக்கரி கலப்பு செலவு மற்றும் மின் நிறுவனங்களிடமிருந்து வர வேண்டிய நிலுவைத் தொகையை ஆராய்கிறது", "Thermal plant efficiency directly governs retail consumer electricity tariffs.", "அனல் மின் நிலையத்தின் செயல்திறன் நுகர்வோர் மின் கட்டணத்தை நேரடியாக நிர்ணயிக்கிறது.", "Low PLF and excessive auxiliary power consumption are frequently flagged by the CAG.", "குறைந்த PLF மற்றும் அதிக மின் இழப்புகளை சி.ஏ.ஜி தொடர்ந்து சுட்டிக்காட்டுகிறது."),
    ("Audit of Fertilizer Subsidies", "What is the primary scrutiny focus in CAG's audit of nutrient-based fertilizer subsidies?", "Verifying Point of Sale (PoS) Aadhaar authentication and factory dispatch gate reconciliations", "விற்பனை முனைய (PoS) ஆதார் சரிபார்ப்பு மற்றும் தொழிற்சாலை விநியோகப் பதிவேடுகளை சரிபார்த்தல்", "Subsidies are disbursed to manufacturers only upon verified retailer PoS sales to farmers.", "விவசாயிகளுக்கு விற்பனை செய்யப்பட்டதாக PoS இயந்திரத்தில் பதிவான பிறகே நிறுவனங்களுக்கு மானியம் விடுவிக்கப்படுகிறது.", "Prevents commercial cross-border smuggling of subsidized agricultural urea.", "மானியம் பெறும் விவசாய யூரியா எல்லை தாண்டி கடத்தப்படுவதை இது தடுக்கிறது."),
    ("Audit of National Health Mission (NHM)", "What was highlighted in CAG's audit of primary healthcare centres under NHM?", "Severe deficits of specialist doctors, non-functioning diagnostic equipment, and medicine stockouts", "நிபுணத்துவ மருத்துவர்கள் பற்றாக்குறை, இயங்காத பரிசோதனை உபகரணங்கள் மற்றும் மருந்து தட்டுப்பாடு", "Assesses whether National Health Mission infrastructure translated into reduced maternal mortality.", "NHM உள்கட்டமைப்பு தாய்மார்கள் இறப்பு விகிதத்தைக் குறைத்ததா என்பதை மதிப்பிடுகிறது.", "Unspent NHM grant balances lying in State Health Societies are audited annually.", "மாநில சுகாதார சங்கங்களில் தேங்கிக் கிடக்கும் செலவிடப்படாத மானியங்கள் தணிக்கை செய்யப்படுகின்றன."),
    ("Audit of Smart Cities Mission", "What was a key audit finding in CAG's performance review of the Smart Cities Mission?", "Over-reliance on private Project Management Consultants (PMCs) and delayed Integrated Command Centres", "திட்ட மேலாண்மை ஆலோசகர்களை (PMCs) அதிகம் சார்ந்திருத்தல் மற்றும் கட்டுப்பாட்டு மையங்களை அமைப்பதில் தாமதம்", "Public funds transferred to Special Purpose Vehicles (SPVs) are scrutinized under Section 14.", "சிறப்பு நோக்க முகமைகளுக்கு (SPVs) மாற்றப்பட்ட பொது நிதி பிரிவு 14-ன் கீழ் தணிக்கை செய்யப்படுகிறது.", "SPVs established under Companies Act are classified as government-controlled entities.", "நிறுவனங்கள் சட்டத்தின் கீழ் அமைக்கப்பட்ட SPV முகமைகள் அரசு நிறுவனங்களாகக் கருதப்படுகின்றன."),
    ("Audit of Inland Fisheries Subsidies", "What is the primary compliance check in CAG's audit of PM Matsya Sampada Yojana?", "Beneficiary physical verification, cold chain infrastructure survival, and aquaculture subsidy release timings", "பயனாளிகள் நேரடி சரிபார்ப்பு, குளிர்பதனக் கிடங்கு உள்கட்டமைப்பு மற்றும் மானியம் விடுவிக்கப்பட்ட நேரம்", "Pradhan Mantri Matsya Sampada Yojana (PMMSY) is audited across maritime and inland states.", "மத்திய மீன்வள மேம்பாட்டுத் திட்டம் கடலோர மற்றும் உள்நாட்டு மாநிலங்களில் தணிக்கை செய்யப்படுகிறது.", "Prevents diversion of aquaculture infrastructure grants to private real estate.", "மீன்வள மானியங்கள் ரியல் எஸ்டேட் வணிகத்திற்கு திருப்பிவிடப்படுவதைத் தடுக்கிறது."),
    ("Audit of Public Debt Management", "How does the CAG evaluate sovereign debt sustainability in the Union Finance Accounts Report?", "Analyzes Debt-to-GDP ratio, interest payments as a percentage of revenue receipts, and maturity profiles", "கடன்-ஜிடிபி விகிதம், வருவாயில் வட்டி செலுத்துதலின் சதவீதம் மற்றும் கடன் முதிர்வு காலத்தை பகுப்பாய்வு செய்கிறது", "Fiscal Responsibility and Budget Management (FRBM) targets are benchmarked against actual debt data.", "FRBM நிதிப் பொறுப்புடைமை இலக்குகளுடன் உண்மையான கடன் தரவுகள் ஒப்பிடப்படுகின்றன.", "CAG cautions against using high-cost off-budget borrowings to finance current expenditure.", "அன்றாட செலவுகளுக்கு பட்ஜெட்டுக்கு புறம்பான அதிக வட்டி கடன்களை வாங்குவதை சி.ஏ.ஜி எச்சரிக்கிறது."),
    ("Audit of Defence Pensions (SPARSH)", "What did the CAG verify in its compliance audit of the SPARSH defense pension platform?", "Timely migration of legacy pensioner records, calculation of OROP arrears, and zero pension stoppages", "பழைய ஓய்வூதிய ஆவணங்களை மாற்றுதல், OROP நிலுவைத் தொகைக் கணக்கீடு மற்றும் ஓய்வூதியத் தடங்கல் இன்மை", "System for Pension Administration (Raksha) - SPARSH is a web-based automated digital pension system.", "SPARSH என்பது பாதுகாப்புத் துறை ஓய்வூதியதாரர்களுக்கான தானியங்கி டிஜிட்டல் தளமாகும்.", "Directly credits pensions from the Ministry of Defence to pensioners' bank accounts.", "பாதுகாப்பு அமைச்சகத்திலிருந்து ஓய்வூதியதாரர்களின் வங்கிக் கணக்குகளுக்கு நேரடியாகப் பணம் செலுத்துகிறது."),
    ("Audit of Agricultural Crop Insurance (PMFBY)", "What critical issue was exposed by the CAG in the audit of Pradhan Mantri Fasal Bima Yojana?", "Delayed settlement of farmer insurance claims by private insurers and delayed release of state subsidy share", "தனியார் காப்பீட்டு நிறுவனங்கள் இழப்பீட்டுத் தொகையை வழங்க தாமதித்தது மற்றும் மாநில அரசு மானியப் பங்கு தாமதம்", "Examines whether crop cutting experiments (CCEs) were conducted objectively for yield loss assessment.", "விளைச்சல் இழப்பை மதிப்பிட பயிர் அறுவடை சோதனைகள் நடுநிலையாக நடத்தப்பட்டனவா என ஆராய்கிறது.", "States defaulting on subsidy shares delay claim payments to distressed farmers.", "மாநில அரசுகள் மானியப் பங்கை வழங்க தாமதித்தால் விவசாயிகளுக்கு காப்பீட்டுப் பணம் கிடைப்பது தாமதமாகிறது."),
    ("Audit of Forest Clearances and Net Present Value", "How does the CAG audit the diversion of forest land for mining and infrastructure?", "Verifies recovery of Net Present Value (NPV) and execution of equivalent compensatory afforestation", "நிகர தற்போதைய மதிப்பை (NPV) முழுமையாக வசூலிப்பது மற்றும் ஈடுசெய்யும் காடு வளர்ப்பை செயல்படுத்துவதை சரிபார்க்கிறது", "Supreme Court laid down strict NPV rates in the landmark T.N. Godavarman forest conservation case.", "டி.என். கோதாவர்மன் வனப் பாதுகாப்பு வழக்கில் உச்ச நீதிமன்றம் கடுமையான NPV கட்டணங்களை நிர்ணயித்தது.", "NPV collections are credited to the statutory CAMPA fund audited by the CAG.", "NPV வசூல்கள் சி.ஏ.ஜியால் தணிக்கை செய்யப்படும் சட்டப்பூர்வ CAMPA நிதியில் வரவு வைக்கப்படுகின்றன."),
    ("Audit of National Highway Toll Automation (FASTag)", "What is the focus of CAG's performance audit on the FASTag electronic toll collection system?", "Reconciliation of electronic toll transactions between acquiring banks, NPCI, and the NHAI concessionaires", "வங்கிகள், NPCI மற்றும் NHAI ஒப்பந்ததாரர்களுக்கு இடையேயான மின்னணு பரிவர்த்தனைகளை சரிபார்த்தல்", "Automated RFID tolls reduce leakage and idling emissions at national highway toll plazas.", "RFID தொழில்நுட்பம் சுங்கச் சாவடிகளில் பணக் கசிவைத் தடுத்து வாகன இயக்கத்தை விரைவுபடுத்துகிறது.", "Discrepancies in toll transaction settlement files are flagged for systemic recovery.", "பரிவர்த்தனை தீர்வு கோப்புகளில் உள்ள முரண்பாடுகளை சி.ஏ.ஜி சுட்டிக்காட்டி மீட்பு செய்கிறது."),
    ("Audit of Atomic Energy Regulatory Safeguards", "How does the CAG audit expenditure of the Department of Atomic Energy (DAE)?", "Audits financial accounts and non-strategic industrial project milestones while protecting nuclear safety secrets", "அணுசக்தி பாதுகாப்பு ரகசியங்களைப் பாதுகாத்து நிதி கணக்குகள் மற்றும் தொழில்துறை திட்ட மைல்கற்களைத் தணிக்கை செய்கிறது", "Commercial nuclear power reactors (NPCIL) are audited under the Companies Act and Section 19.", "அணுமின் கழகம் (NPCIL) நிறுவனங்கள் சட்டம் மற்றும் பிரிவு 19-ன் கீழ் தணிக்கை செய்யப்படுகிறது.", "CAG reported on the decommissioning costs and waste management reserves of nuclear plants.", "அணு உலைகளை மூடுவதற்கான செலவுகள் மற்றும் கழிவு மேலாண்மை நிதி குறித்து சி.ஏ.ஜி அறிக்கை அளித்துள்ளது."),
    ("Audit of Inland Container Depots (ICDs)", "What does the CAG audit examine regarding customs revenue collection at Inland Container Depots?", "Assessment of customs duties on imported container cargo and prevention of bonded warehouse revenue loss", "இறக்குமதி கொள்கலன் சரக்குகளுக்கான சுங்க வரி மதிப்பீடு மற்றும் கிடங்கு வரி இழப்புகளைத் தடுத்தல்", "Inland dry ports handle intermodal cargo transfer under bonded customs supervision.", "உள்நாட்டு உலர் துறைமுகங்கள் சுங்கக் கண்காணிப்பின் கீழ் சரக்கு மாற்றங்களை நிர்வகிக்கின்றன.", "Delayed physical de-stuffing of long-standing containers attracts severe audit observations.", "நீண்ட காலமாக முடங்கிக் கிடக்கும் கொள்கலன்கள் மீது தணிக்கைக் குறிப்புகள் எழுப்பப்படுகின்றன."),
    ("Audit of National Food Security Act (NFSA)", "What was a major systemic finding in CAG's audit of foodgrain management under NFSA?", "High storage losses in FCI godowns, delays in milling of paddy, and non-automation of Fair Price Shops", "FCI கிடங்குகளில் அதிக சேமிப்புக் கிடங்கு இழப்புகள், நெல் அரைப்பதில் தாமதம் மற்றும் நியாயவிலைக் கடை தானியங்கி தாமதம்", "Food Corporation of India (FCI) operations involve massive central food subsidies from the CFI.", "இந்திய உணவுக் கழகத்தின் (FCI) செயல்பாடுகள் மத்திய அரசின் பெரும் உணவு மானியத்தை உள்ளடக்கியவை.", "CAG audited the digitization of ration cards and installation of electronic PoS devices.", "ரேஷன் அட்டை டிஜிட்டல் மயம் மற்றும் மின்னணு PoS இயந்திரங்கள் நிறுவலை சி.ஏ.ஜி தணிக்கை செய்தது."),
    ("Audit of Tribal Sub-Plan Grants", "What did the CAG expose in its performance audit of Scheduled Tribe Component (STC) funds?", "Diversion of earmarked tribal welfare funds for general municipal roads and administrative buildings", "பழங்குடியினர் நலனுக்காக ஒதுக்கப்பட்ட பிரத்யேக நிதியை பொதுவான நகராட்சி சாலைகள் மற்றும் கட்டிடங்களுக்கு மாற்றியது", "Earmarked funds under the STC cannot be diverted for non-tribal schemes or general administrative expenses.", "பழங்குடியினர் திட்ட நிதி பிற திட்டங்களுக்கோ பொது நிர்வாகச் செலவுகளுக்கோ மாற்றப்படக் கூடாது.", "CAG recommended strict Treasury verification before clearing STC expenditure vouchers.", "STC செலவின வவுச்சர்களை அனுமதிக்கும் முன் கடுமையான கருவூல சரிபார்ப்பை சி.ஏ.ஜி பரிந்துரைத்தது.")
]

for item in more_gt_part1_items:
    topic, stem, correct_en, correct_ta, tip_en, tip_ta, fact_en, fact_ta = item
    raw_gt_part1_data.append({
        "subtopic": topic,
        "stem_en": f"{stem}?",
        "stem_ta": f"{correct_ta[:40]}... தொடர்பாக {stem}?",
        "options": [
            (correct_en, correct_ta),
            ("Subject to summary approval by the Union Cabinet Secretary without legislative scrutiny", "சட்டமன்ற ஆய்வின்றி மத்திய அமைச்சரவைச் செயலாளரின் சுருக்கமான ஒப்புதலுக்கு உட்பட்டது"),
            ("Completely exempt from any form of constitutional audit under judicial doctrine", "நீதிமன்றக் கோட்பாட்டின் கீழ் எந்தவொரு அரசியலமைப்பு தணிக்கையிலிருந்தும் முற்றிலும் விலக்கு பெற்றது"),
            ("Audited exclusively by private commercial banks operating at district level", "மாவட்ட அளவில் இயங்கும் தனியார் வணிக வங்கிகளால் மட்டுமே தணிக்கை செய்யப்படுவது")
        ],
        "exp_en": f"{correct_en}. This constitutional and statutory rule ensures public funds are audited in accordance with established administrative law principles.",
        "exp_ta": f"{correct_ta}. இந்த அரசியலமைப்பு மற்றும் சட்டப்பூர்வ விதி பொது நிதி உரிய நிர்வாகக் கொள்கைகளின்படி தணிக்கை செய்யப்படுவதை உறுதி செய்கிறது.",
        "tip_en": tip_en,
        "tip_ta": tip_ta,
        "fact_en": fact_en,
        "fact_ta": fact_ta
    })

def get_gt_part1_questions():
    questions = []
    for idx, item in enumerate(raw_gt_part1_data, start=1):
        qid = f"CAG_GT_{idx:03d}"
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
            tags=["polity", "comptroller_and_auditor_general", "grand_test", item["subtopic"].lower().replace(" ", "_")]
        )
        questions.append(q)
    return questions

if __name__ == "__main__":
    qs = get_gt_part1_questions()
    print(f"Generated {len(qs)} questions for CAG GT Part 1.")
