# -*- coding: utf-8 -*-
"""
Build 50 Easy MCQs for Finance Commission of India
ID range: FC_E_001 to FC_E_050
"""

import json
import os
from fc_mcq_helper import make_fc_q
from rebalance_er_helper import balance_question_keys
from tools.nova_content_engine.validator import ContentValidator

raw_easy_data = [
    # 1
    {
        "subtopic": "Constitutional Article",
        "stem_en": "Which Article of the Constitution of India provides for the constitution of a Finance Commission?",
        "stem_ta": "இந்திய அரசியலமைப்பின் எந்தச் சரத்து நிதி ஆணையத்தை அமைக்க வகைசெய்கிறது?",
        "options": [
            ("Article 280", "சரத்து 280"),
            ("Article 270", "சரத்து 270"),
            ("Article 282", "சரத்து 282"),
            ("Article 300", "சரத்து 300")
        ],
        "exp_en": "Article 280 of the Constitution provides that the President shall, within two years from the commencement of the Constitution and thereafter at the expiration of every fifth year or earlier, constitute a Finance Commission.",
        "exp_ta": "அரசியலமைப்பின் சரத்து 280, அரசியலமைப்பு தொடங்கிய இரண்டு ஆண்டுகளுக்குள்ளும், அதன் பிறகு ஒவ்வொரு ஐந்தாம் ஆண்டின் முடிவிலும் அல்லது அதற்கு முன்னதாகவும் குடியரசுத் தலைவர் ஒரு நிதி ஆணையத்தை அமைக்க வேண்டும் என வகைசெய்கிறது.",
        "tip_en": "Article 280 = Finance Commission. Article 281 = Recommendations of Finance Commission.",
        "tip_ta": "சரத்து 280 = நிதி ஆணையம். சரத்து 281 = நிதி ஆணையத்தின் பரிந்துரைகள்.",
        "fact_en": "The Finance Commission is a quasi-judicial body constituted by the President.",
        "fact_ta": "நிதி ஆணையம் என்பது குடியரசுத் தலைவரால் அமைக்கப்படும் ஒரு பகுதி-நீதித்துறை சார்ந்த அமைப்பாகும்."
    },
    # 2
    {
        "subtopic": "Appointing Authority",
        "stem_en": "Who constitutes the Finance Commission of India?",
        "stem_ta": "இந்திய நிதி ஆணையத்தை அமைப்பவர் யார்?",
        "options": [
            ("The President of India", "இந்தியக் குடியரசுத் தலைவர்"),
            ("The Prime Minister of India", "இந்தியப் பிரதமர்"),
            ("The Speaker of the Lok Sabha", "மக்களவைத் தலைவர் (சபாநாயகர்)"),
            ("The Union Finance Minister", "மத்திய நிதி அமைச்சர்")
        ],
        "exp_en": "Under Article 280(1), the Finance Commission is constituted by the President of India.",
        "exp_ta": "சரத்து 280(1)-ன் கீழ் இந்திய நிதி ஆணையம் இந்தியக் குடியரசுத் தலைவரால் அமைக்கப்படுகிறது.",
        "tip_en": "The President constitutes the Finance Commission every 5th year or earlier.",
        "tip_ta": "குடியரசுத் தலைவர் ஒவ்வொரு 5வது ஆண்டும் அல்லது தேவைப்பட்டால் அதற்கு முன்னதாகவும் நிதி ஆணையத்தை அமைக்கிறார்.",
        "fact_en": "The first Finance Commission was constituted by the President in November 1951.",
        "fact_ta": "முதல் நிதி ஆணையம் நவம்பர் 1951-ல் குடியரசுத் தலைவரால் அமைக்கப்பட்டது."
    },
    # 3
    {
        "subtopic": "Frequency of Constitution",
        "stem_en": "How often is the Finance Commission generally constituted by the President?",
        "stem_ta": "பொதுவாக எத்தனை ஆண்டுகளுக்கு ஒருமுறை நிதி ஆணையம் குடியரசுத் தலைவரால் அமைக்கப்படுகிறது?",
        "options": [
            ("Every fifth year or earlier", "ஒவ்வொரு ஐந்தாவது ஆண்டும் அல்லது அதற்கு முன்னதாக"),
            ("Every sixth year", "ஒவ்வொரு ஆறாவது ஆண்டும்"),
            ("Every third year", "ஒவ்வொரு மூன்றாவது ஆண்டும்"),
            ("Every ten years", "ஒவ்வொரு பத்து ஆண்டுகளுக்கும் ஒருமுறை")
        ],
        "exp_en": "Article 280(1) mandates the President to constitute the Finance Commission at the expiration of every fifth year or at such earlier time as he considers necessary.",
        "exp_ta": "சரத்து 280(1)-ன் படி, ஒவ்வொரு ஐந்தாவது ஆண்டின் முடிவிலும் அல்லது குடியரசுத் தலைவர் அவசியமெனக் கருதும் முன்னதான காலத்திலும் நிதி ஆணையம் அமைக்கப்படுகிறது.",
        "tip_en": "Normal interval: 5 years (can be earlier if required).",
        "tip_ta": "வழக்கமான இடைவெளி: 5 ஆண்டுகள் (தேவையெனில் அதற்கு முன்னதாகவும் அமைக்கப்படலாம்).",
        "fact_en": "The 15th Finance Commission was given an extension to submit two reports covering 6 years (2020-2026).",
        "fact_ta": "15வது நிதி ஆணையத்திற்கு 6 ஆண்டுகளை (2020-2026) உள்ளடக்கிய இரண்டு அறிக்கைகளை சமர்ப்பிக்க காலநீட்டிப்பு வழங்கப்பட்டது."
    },
    # 4
    {
        "subtopic": "Composition of the Commission",
        "stem_en": "What is the total membership of the Finance Commission under Article 280(1)?",
        "stem_ta": "சரத்து 280(1)-ன் கீழ் நிதி ஆணையத்தின் மொத்த உறுப்பினர்கள் எண்ணிக்கை எவ்வளவு?",
        "options": [
            ("A Chairman and four other members (Total: 5)", "ஒரு தலைவர் மற்றும் நான்கு உறுப்பினர்கள் (மொத்தம்: 5)"),
            ("A Chairman and three other members (Total: 4)", "ஒரு தலைவர் மற்றும் மூன்று உறுப்பினர்கள் (மொத்தம்: 4)"),
            ("A Chairman and five other members (Total: 6)", "ஒரு தலைவர் மற்றும் ஐந்து உறுப்பினர்கள் (மொத்தம்: 6)"),
            ("A Chairman and six other members (Total: 7)", "ஒரு தலைவர் மற்றும் ஆறு உறுப்பினர்கள் (மொத்தம்: 7)")
        ],
        "exp_en": "Article 280(1) specifies that the Finance Commission shall consist of a Chairman and four other members to be appointed by the President.",
        "exp_ta": "சரத்து 280(1) நிதி ஆணையமானது குடியரசுத் தலைவரால் நியமிக்கப்படும் ஒரு தலைவர் மற்றும் நான்கு பிற உறுப்பினர்களைக் கொண்டிருக்கும் எனக் குறிப்பிடுகிறது.",
        "tip_en": "Finance Commission = 1 Chairman + 4 Members = 5 total.",
        "tip_ta": "நிதி ஆணையம் = 1 தலைவர் + 4 உறுப்பினர்கள் = மொத்தம் 5 பேர்.",
        "fact_en": "The Secretary to the Commission assists the Commission but is not one of the constitutional members.",
        "fact_ta": "ஆணையத்தின் செயலாளர் ஆணையத்திற்கு உதவுகிறார்; ஆனால் அவர் அரசியலமைப்பு உறுப்பினர் அல்ல."
    },
    # 5
    {
        "subtopic": "Qualifications Determination",
        "stem_en": "Who is authorized under Article 280(2) to determine the qualifications of the members of the Finance Commission?",
        "stem_ta": "சரத்து 280(2)-ன் கீழ் நிதி ஆணைய உறுப்பினர்களின் தகுதிகளை நிர்ணயிக்க அதிகாரம் பெற்றவர் யார்?",
        "options": [
            ("Parliament by law", "நாடாளுமன்றம் சட்டத்தின் மூலம்"),
            ("The President by executive order", "குடியரசுத் தலைவர் நிர்வாக உத்தரவின் மூலம்"),
            ("The Supreme Court of India", "இந்திய உச்ச நீதிமன்றம்"),
            ("The Union Finance Minister", "மத்திய நிதி அமைச்சர்")
        ],
        "exp_en": "Article 280(2) states that Parliament may by law determine the qualifications which shall be requisite for appointment as members of the Commission and the manner in which they shall be selected.",
        "exp_ta": "சரத்து 280(2)-ன் படி, நிதி ஆணைய உறுப்பினர்களாக நியமிக்கப்படுவதற்கான தகுதிகளையும் அவர்கள் தேர்ந்தெடுக்கப்படும் முறையையும் நாடாளுமன்றம் சட்டத்தின் மூலம் தீர்மானிக்கலாம்.",
        "tip_en": "Parliament enacted the Finance Commission (Miscellaneous Provisions) Act, 1951 for this purpose.",
        "tip_ta": "இதற்காக நாடாளுமன்றம் 1951-ல் நிதி ஆணைய (பல்வேறு விதிகள்) சட்டத்தை இயற்றியது.",
        "fact_en": "The qualifications are not specified directly in the Constitution itself.",
        "fact_ta": "தகுதிகள் அரசியலமைப்பில் நேரடியாகக் குறிப்பிடப்படவில்லை; நாடாளுமன்ற சட்டத்தில் உள்ளன."
    },
    # 6
    {
        "subtopic": "First Finance Commission Chairman",
        "stem_en": "Who was the Chairman of the First Finance Commission of India?",
        "stem_ta": "இந்தியாவின் முதல் நிதி ஆணையத்தின் தலைவர் யார்?",
        "options": [
            ("K.C. Neogy", "கே.சி. நியோகி"),
            ("K. Santhanam", "கே. சந்தானம்"),
            ("A.K. Chanda", "ஏ.கே. சந்தா"),
            ("P.V. Rajamannar", "பி.வி. ராஜமன்னார்")
        ],
        "exp_en": "K.C. Neogy was the Chairman of the First Finance Commission of India, constituted in 1951, covering the period 1952-1957.",
        "exp_ta": "1951 ஆம் ஆண்டு அமைக்கப்பட்ட முதல் இந்திய நிதி ஆணையத்தின் தலைவர் கே.சி. நியோகி ஆவார்; இதன் பரிந்துரைக் காலம் 1952-1957 ஆகும்.",
        "tip_en": "1st FC Chairman = K.C. Neogy (1951).",
        "tip_ta": "1வது நிதி ஆணையத் தலைவர் = கே.சி. நியோகி (1951).",
        "fact_en": "The First Finance Commission recommended sharing 55% of income tax net proceeds with the States.",
        "fact_ta": "முதல் நிதி ஆணையம் வருமான வரி நிகர வருவாயில் 55%-ஐ மாநிலங்களுடன் பகிர்ந்துகொள்ள பரிந்துரைத்தது."
    },
    # 7
    {
        "subtopic": "Tabling of Recommendations (Article 281)",
        "stem_en": "To whom does the Finance Commission submit its report and recommendations?",
        "stem_ta": "நிதி ஆணையம் தனது அறிக்கை மற்றும் பரிந்துரைகளை யாரிடம் சமர்ப்பிக்கிறது?",
        "options": [
            ("The President of India", "இந்தியக் குடியரசுத் தலைவர்"),
            ("The Prime Minister", "பிரதமர்"),
            ("The Speaker of Lok Sabha", "மக்களவைத் தலைவர்"),
            ("The Chief Justice of India", "இந்தியத் தலைமை நீதிபதி")
        ],
        "exp_en": "The Finance Commission submits its report to the President of India, who under Article 281 causes it to be laid before each House of Parliament.",
        "exp_ta": "நிதி ஆணையம் தனது அறிக்கையை இந்தியக் குடியரசுத் தலைவரிடம் சமர்ப்பிக்கிறது; சரத்து 281-ன் கீழ் அவர் அதை நாடாளுமன்றத்தின் இரு அவைகளிலும் வைக்கச் செய்கிறார்.",
        "tip_en": "Report goes to President -> President tables it in Parliament under Article 281.",
        "tip_ta": "அறிக்கை குடியரசுத் தலைவரிடம் செல்கிறது -> சரத்து 281-ன் கீழ் அவர் நாடாளுமன்றத்தில் வைக்கிறார்.",
        "fact_en": "An explanatory memorandum on action taken must accompany the report when laid in Parliament.",
        "fact_ta": "நாடாளுமன்றத்தில் வைக்கப்படும் போது எடுக்கப்பட்ட நடவடிக்கை மீதான விளக்கக் குறிப்பும் இணைக்கப்பட வேண்டும்."
    },
    # 8
    {
        "subtopic": "Nature of Recommendations",
        "stem_en": "What is the legal nature of the recommendations made by the Finance Commission?",
        "stem_ta": "நிதி ஆணையத்தின் பரிந்துரைகளின் சட்டப்பூர்வ தன்மை என்ன?",
        "options": [
            ("Advisory in nature and not legally binding on the Government", "ஆலோசனைத் தன்மை கொண்டவை மற்றும் அரசை சட்டப்பூர்வமாகக் கட்டுப்படுத்தாது"),
            ("Strictly binding on the Union Government as a judicial decree", "நீதிமன்றத் தீர்ப்பு போல மத்திய அரசை முழுமையாகக் கட்டுப்படுத்துபவை"),
            ("Binding only on the State Governments but not on the Centre", "மாநில அரசுகளை மட்டுமே கட்டுப்படுத்தும்; மத்திய அரசைக் கட்டுப்படுத்தாது"),
            ("Enforceable as a money bill through executive ordinance", "நிர்வாக அவசரச் சட்டம் மூலம் நிதி மசோதாவாக அமல்படுத்தப்படக்கூடியவை")
        ],
        "exp_en": "The recommendations of the Finance Commission are only of an advisory nature and are not legally binding on the Union Government, though by strong convention they are accepted.",
        "exp_ta": "நிதி ஆணையத்தின் பரிந்துரைகள் ஆலோசனைத் தன்மை கொண்டவை மட்டுமே; அவை மத்திய அரசை சட்டப்பூர்வமாகக் கட்டுப்படுத்தாது, எனினும் வலுவான மரபின்படி அவை ஏற்றுக்கொள்ளப்படுகின்றன.",
        "tip_en": "Advisory in nature, but conventionally accepted by the Union Cabinet.",
        "tip_ta": "ஆலோசனைத் தன்மை வாய்ந்தது, ஆனால் மத்திய அமைச்சரவையால் மரபுப்படி ஏற்றுக்கொள்ளப்படுகிறது.",
        "fact_en": "Dr. P.V. Rajamannar noted that as a constitutional body, its recommendations should ordinarily not be rejected.",
        "fact_ta": "அரசியலமைப்பு அமைப்பு என்பதால் அதன் பரிந்துரைகளை சாதாரணமாக நிராகரிக்கக் கூடாது என ராஜமன்னார் குறிப்பிட்டார்."
    },
    # 9
    {
        "subtopic": "Chairman Qualification",
        "stem_en": "Under the Finance Commission Act 1951, the Chairman of the Commission must be a person selected from among persons who have had experience in:",
        "stem_ta": "1951 நிதி ஆணையச் சட்டத்தின் கீழ், ஆணையத்தின் தலைவர் எந்தத் துறையில் அனுபவம் உள்ள நபர்களில் இருந்து தேர்ந்தெடுக்கப்பட வேண்டும்?",
        "options": [
            ("Public affairs", "பொது விவகாரங்கள் (Public affairs)"),
            ("Active military command", "ராணுவப் படைத் தளபதி பணி"),
            ("International corporate banking", "சர்வதேச கார்ப்பரேட் வங்கி"),
            ("Commercial software engineering", "வணிக மென்பொருள் பொறியியல்")
        ],
        "exp_en": "Section 3 of the Finance Commission (Miscellaneous Provisions) Act 1951 specifies that the Chairman shall be selected from among persons who have had experience in public affairs.",
        "exp_ta": "1951 நிதி ஆணையச் சட்டத்தின் பிரிவு 3, ஆணையத்தின் தலைவர் பொது விவகாரங்களில் அனுபவம் கொண்ட நபர்களில் இருந்து தேர்ந்தெடுக்கப்பட வேண்டும் எனக் குறிப்பிடுகிறது.",
        "tip_en": "Chairman qualification = Experience in public affairs.",
        "tip_ta": "தலைவர் தகுதி = பொது விவகாரங்களில் அனுபவம்.",
        "fact_en": "Members, by contrast, have specific technical qualifications in law, accounts, administration, or economics.",
        "fact_ta": "உறுப்பினர்கள் சட்டம், கணக்கு, நிர்வாகம் அல்லது பொருளாதாரத்தில் குறிப்பிட்ட தொழில்நுட்பத் தகுதிகளைக் கொண்டிருக்க வேண்டும்."
    },
    # 10
    {
        "subtopic": "Members Qualifications in Law",
        "stem_en": "Under the Finance Commission Act 1951, one of the four members can be a person who is qualified to be appointed as:",
        "stem_ta": "1951 நிதி ஆணையச் சட்டத்தின் கீழ், நான்கு உறுப்பினர்களில் ஒருவர் எந்தப் பதவிக்கு நியமிக்கப்பட தகுதி வாய்ந்தவராக இருக்க வேண்டும்?",
        "options": [
            ("A Judge of a High Court", "உயர் நீதிமன்ற நீதிபதி"),
            ("The Attorney General of India", "இந்தியத் தலைமை வழக்கறிஞர்"),
            ("The Governor of the Reserve Bank of India", "இந்திய ரிசர்வ் வங்கி ஆளுநர்"),
            ("A Member of Parliament", "நாடாளுமன்ற உறுப்பினர்")
        ],
        "exp_en": "Under Section 3(a) of the 1951 Act, one category of qualification for members is: 'a person who is, or has been, or is qualified to be appointed as a Judge of a High Court'.",
        "exp_ta": "1951 சட்டத்தின் பிரிவு 3(a)-ன் படி, உறுப்பினர்களுக்கான ஒரு தகுதி: 'உயர் நீதிமன்ற நீதிபதியாக இருப்பவர் அல்லது இருந்தவர் அல்லது நியமிக்கப்பட தகுதியுள்ளவர்' என்பதாகும்.",
        "tip_en": "Member Category 1: High Court judge or qualified to be appointed as such.",
        "tip_ta": "உறுப்பினர் வகை 1: உயர் நீதிமன்ற நீதிபதி அல்லது அதற்கான தகுதி பெற்றவர்.",
        "fact_en": "This judicial background reinforces the quasi-judicial character of the Commission.",
        "fact_ta": "இந்த நீதித்துறை பின்னணி ஆணையத்தின் பகுதி-நீதித்துறை தன்மையை வலுப்படுத்துகிறது."
    },
    # 11
    {
        "subtopic": "Quasi-Judicial Powers",
        "stem_en": "Under the Finance Commission Act 1951, what specific legal powers are vested in the Finance Commission?",
        "stem_ta": "1951 நிதி ஆணையச் சட்டத்தின் கீழ் நிதி ஆணையத்திற்கு எந்த குறிப்பிட்ட சட்டப்பூர்வ அதிகாரங்கள் வழங்கப்பட்டுள்ளன?",
        "options": [
            ("Powers of a Civil Court under the Code of Civil Procedure, 1908", "1908 சிவில் நடைமுறைச் சட்டத்தின் கீழ் ஒரு சிவில் நீதிமன்றத்தின் அதிகாரங்கள்"),
            ("Powers of a Criminal Court to sentence defaulting states", "தவறிழைக்கும் மாநிலங்களுக்கு தண்டனை வழங்க குற்றவியல் நீதிமன்ற அதிகாரங்கள்"),
            ("Powers to issue writs of mandamus under Article 32", "சரத்து 32-ன் கீழ் கட்டளைப் பேராணைகளை வெளியிடும் அதிகாரங்கள்"),
            ("Powers to dissolve state legislative assemblies under Article 356", "சரத்து 356-ன் கீழ் மாநில சட்டமன்றங்களைக் கலைக்கும் அதிகாரங்கள்")
        ],
        "exp_en": "Under Section 8 of the 1951 Act, the Commission has all the powers of a civil court under the Code of Civil Procedure 1908 while summoning witnesses, requiring discovery and production of documents, and requisitioning public records.",
        "exp_ta": "1951 சட்டத்தின் பிரிவு 8-ன் படி, சாட்சிகளை அழைப்பது, ஆவணங்களைக் கோருவது மற்றும் பொது ஆவணங்களைப் பெறுவதில் 1908 சிவில் நடைமுறைச் சட்டத்தின் கீழ் சிவில் நீதிமன்றத்திற்குரிய அனைத்து அதிகாரங்களையும் நிதி ஆணையம் கொண்டுள்ளது.",
        "tip_en": "Finance Commission = Civil Court powers for evidence and document discovery.",
        "tip_ta": "நிதி ஆணையம் = சாட்சியங்கள் மற்றும் ஆவணங்களைப் பெறுவதில் சிவில் நீதிமன்ற அதிகாரங்கள்.",
        "fact_en": "Hearings before the Commission are deemed judicial proceedings under Sections 193 and 228 of the IPC.",
        "fact_ta": "ஆணையத்தின் முன் நடைபெறும் விசாரணைகள் இந்திய தண்டனைச் சட்டத்தின் கீழ் நீதிமன்ற நடவடிக்கைகளாகக் கருதப்படுகின்றன."
    },
    # 12
    {
        "subtopic": "Core Duty: Net Proceeds Distribution",
        "stem_en": "Under Article 280(3)(a), what is the primary duty of the Finance Commission regarding taxes?",
        "stem_ta": "சரத்து 280(3)(a)-ன் கீழ் வரிகள் தொடர்பாக நிதி ஆணையத்தின் முதன்மைக் கடமை என்ன?",
        "options": [
            ("Distribution between the Union and the States of the net proceeds of taxes divisible between them", "மத்திய மற்றும் மாநில அரசுகளுக்கு இடையே பகிர்ந்தளிக்கப்பட வேண்டிய வரிகளின் நிகர வருவாயைப் பகிர்ந்தளித்தல்"),
            ("Direct collection of all income taxes from corporate citizens", "கார்ப்பரேட் நிறுவனங்களிடமிருந்து அனைத்து வருமான வரிகளையும் நேரடியாக வசூலிப்பது"),
            ("Abolishing state value added taxes without compensation", "இழப்பீடு இன்றி மாநில மதிப்புக்கூட்டு வரிகளை ரத்து செய்வது"),
            ("Determining individual income tax slabs for salaried employees", "ஊதியம் பெறும் ஊழியர்களுக்கான தனிநபர் வருமான வரி அடுக்குகளை நிர்ணயிப்பது")
        ],
        "exp_en": "Article 280(3)(a) mandates the Commission to recommend the distribution between the Union and the States of the net proceeds of taxes which are to be, or may be, divided between them and the allocation between the States of the respective shares of such proceeds.",
        "exp_ta": "சரத்து 280(3)(a), மத்திய மற்றும் மாநிலங்களுக்கு இடையே பிரிக்கப்பட வேண்டிய வரிகளின் நிகர வருவாயை பகிர்ந்தளிப்பது மற்றும் மாநிலங்களுக்கு இடையேயான பங்கை ஒதுக்கீடு செய்வது குறித்து பரிந்துரைக்க ஆணையத்திற்கு உத்தரவிடுகிறது.",
        "tip_en": "Vertical devolution: Centre to States. Horizontal devolution: Among the States.",
        "tip_ta": "செங்குத்துப் பகிர்வு: மத்தியிலிருந்து மாநிலங்களுக்கு. கிடைமட்டப் பகிர்வு: மாநிலங்களுக்கு இடையே.",
        "fact_en": "Cesses and surcharges levied under Article 271 are not part of this divisible pool.",
        "fact_ta": "சரத்து 271-ன் கீழ் விதிக்கப்படும் கூடுதல் கட்டணங்கள் (Surcharges) மற்றும் செஸ் வரிகள் இதில் சேராது."
    },
    # 13
    {
        "subtopic": "Grants-in-Aid Recommendation (Article 275)",
        "stem_en": "Under Article 280(3)(b), the Finance Commission recommends principles governing which grants?",
        "stem_ta": "சரத்து 280(3)(b)-ன் கீழ் எந்த மானியங்களை நிர்வகிக்கும் கொள்கைகளை நிதி ஆணையம் பரிந்துரைக்கிறது?",
        "options": [
            ("Grants-in-aid of the revenues of the States out of the Consolidated Fund of India under Article 275", "சரத்து 275-ன் கீழ் இந்தியத் திரட்டப்பட்ட நிதியிலிருந்து மாநிலங்களின் வருவாய்க்கான மானியங்கள்"),
            ("Discretionary grants under Article 282 for political campaigns", "அரசியல் பிரச்சாரங்களுக்கான சரத்து 282-ன் கீழ் உள்ள விருப்ப மானியங்கள்"),
            ("Subsidies paid to private international airlines", "தனியார் சர்வதேச விமான நிறுவனங்களுக்கு வழங்கப்படும் மானியங்கள்"),
            ("Foreign aid grants disbursed to neighbouring countries", "அண்டை நாடுகளுக்கு வழங்கப்படும் வெளிநாட்டு உதவி மானியங்கள்")
        ],
        "exp_en": "Article 280(3)(b) requires the Commission to recommend the principles which should govern the grants-in-aid of the revenues of the States out of the Consolidated Fund of India under Article 275.",
        "exp_ta": "சரத்து 280(3)(b), சரத்து 275-ன் கீழ் இந்தியத் திரட்டப்பட்ட நிதியிலிருந்து மாநிலங்களின் வருவாய்க்கான மானியங்களை நிர்வகிக்க வேண்டிய கொள்கைகளை பரிந்துரைக்கக் கோருகிறது.",
        "tip_en": "Article 275 = Statutory grants recommended by FC. Article 282 = Discretionary grants by Centre.",
        "tip_ta": "சரத்து 275 = நிதி ஆணையத்தால் பரிந்துரைக்கப்படும் சட்டப்பூர்வ மானியங்கள். சரத்து 282 = விருப்ப மானியங்கள்.",
        "fact_en": "Revenue Deficit Grants are recommended under Article 275 to bridge post-devolution gaps.",
        "fact_ta": "வரிப் பகிர்வுக்குப் பிந்தைய பற்றாக்குறையை ஈடுசெய்ய சரத்து 275-ன் கீழ் வருவாய்ப் பற்றாக்குறை மானியங்கள் வழங்கப்படுகின்றன."
    },
    # 14
    {
        "subtopic": "Augmenting Consolidated Fund for Panchayats",
        "stem_en": "Sub-clause (bb) of Article 280(3), added by the 73rd Constitutional Amendment Act 1992, mandates the Finance Commission to recommend measures to augment the Consolidated Fund of a State to supplement the resources of:",
        "stem_ta": "73வது அரசியலமைப்புத் திருத்தச் சட்டம் 1992-ன் மூலம் சேர்க்கப்பட்ட சரத்து 280(3)(bb), யாருடைய நிதி ஆதாரங்களுக்கு உதவ மாநில திரட்டப்பட்ட நிதியை பெருக்குவதற்கான நடவடிக்கைகளை பரிந்துரைக்க ஆணையத்திற்கு உத்தரவிடுகிறது?",
        "options": [
            ("Panchayats in the State", "மாநிலத்தில் உள்ள பஞ்சாயத்துகள்"),
            ("Public Sector Commercial Banks", "பொதுத்துறை வணிக வங்கிகள்"),
            ("State Police Forces", "மாநில காவல் படைகள்"),
            ("State Bar Councils", "மாநில வழக்கறிஞர் மன்றங்கள்")
        ],
        "exp_en": "Article 280(3)(bb), inserted by the 73rd Amendment, requires the Commission to recommend measures needed to augment the Consolidated Fund of a State to supplement the resources of the Panchayats in the State on the basis of the recommendations made by the State Finance Commission.",
        "exp_ta": "73வது திருத்தத்தால் சேர்க்கப்பட்ட சரத்து 280(3)(bb), மாநில நிதி ஆணையத்தின் பரிந்துரைகளின் அடிப்படையில் கிராம பஞ்சாயத்துகளின் வளங்களுக்கு உதவ மாநில திரட்டப்பட்ட நிதியைப் பெருக்குவதற்கான நடவடிக்கைகளை பரிந்துரைக்கக் கோருகிறது.",
        "tip_en": "Article 280(3)(bb) = Panchayats (73rd Amendment). Article 280(3)(c) = Municipalities (74th Amendment).",
        "tip_ta": "சரத்து 280(3)(bb) = பஞ்சாயத்துகள் (73வது திருத்தம்). சரத்து 280(3)(c) = நகராட்சிகள் (74வது திருத்தம்).",
        "fact_en": "These local body grants are made on the basis of recommendations of the State Finance Commission.",
        "fact_ta": "இந்த உள்ளாட்சி மானியங்கள் மாநில நிதி ஆணையத்தின் பரிந்துரைகளின் அடிப்படையில் வழங்கப்படுகின்றன."
    },
    # 15
    {
        "subtopic": "Augmenting Consolidated Fund for Municipalities",
        "stem_en": "Sub-clause (c) of Article 280(3), added by the 74th Constitutional Amendment Act 1992, mandates the Finance Commission to recommend measures to supplement the resources of:",
        "stem_ta": "74வது அரசியலமைப்புத் திருத்தச் சட்டம் 1992-ன் மூலம் சேர்க்கப்பட்ட சரத்து 280(3)(c), யாருடைய வளங்களை பெருக்குவதற்கான நடவடிக்கைகளை பரிந்துரைக்க ஆணையத்திற்கு உத்தரவிடுகிறது?",
        "options": [
            ("The Municipalities in the State", "மாநிலத்தில் உள்ள நகராட்சிகள்"),
            ("Private Real Estate Developers", "தனியார் ரியல் எஸ்டேட் நிறுவனங்கள்"),
            ("The High Court of the State", "மாநில உயர் நீதிமன்றம்"),
            ("District Civil Hospitals exclusively", "மாவட்ட அரசு மருத்துவமனைகள் மட்டுமே")
        ],
        "exp_en": "Article 280(3)(c), inserted by the 74th Amendment, requires the Commission to recommend measures needed to augment the Consolidated Fund of a State to supplement the resources of the Municipalities in the State based on State Finance Commission recommendations.",
        "exp_ta": "74வது திருத்தத்தால் சேர்க்கப்பட்ட சரத்து 280(3)(c), மாநில நிதி ஆணையத்தின் பரிந்துரைகளின் அடிப்படையில் மாநில நகராட்சிகளின் வளங்களுக்கு உதவ மாநில திரட்டப்பட்ட நிதியைப் பெருக்குவதற்கான நடவடிக்கைகளை பரிந்துரைக்கிறது.",
        "tip_en": "Local bodies mandate: 280(3)(bb) for Panchayats, 280(3)(c) for Municipalities.",
        "tip_ta": "உள்ளாட்சி அமைப்புகள் பணி: பஞ்சாயத்துகளுக்கு 280(3)(bb), நகராட்சிகளுக்கு 280(3)(c).",
        "fact_en": "Local body grants recommended by 15th FC amounted to Rs. 4.36 lakh crore.",
        "fact_ta": "15வது நிதி ஆணையத்தால் பரிந்துரைக்கப்பட்ட உள்ளாட்சி மானியங்கள் ரூ. 4.36 லட்சம் கோடியாகும்."
    },
    # 16
    {
        "subtopic": "Sound Finance Matters",
        "stem_en": "Under Article 280(3)(d), what additional matters can the Finance Commission consider?",
        "stem_ta": "சரத்து 280(3)(d)-ன் கீழ் நிதி ஆணையம் கூடுதல் விஷயமாக எதனைப் பரிசீலிக்கலாம்?",
        "options": [
            ("Any other matter referred to the Commission by the President in the interests of sound finance", "செம்மையான நிதி மேலாண்மை நலன் கருதி குடியரசுத் தலைவரால் ஆணையத்திற்கு அனுப்பப்படும் பிற விஷயங்கள்"),
            ("Determining military war strategy during emergency", "நெருக்கடி நிலையின் போது ராணுவப் போர் உத்திகளைத் தீர்மானித்தல்"),
            ("Selecting candidates for governor posts in states", "மாநில ஆளுநர் பதவிக்கான நபர்களைத் தேர்ந்தெடுத்தல்"),
            ("Appointing judges to the Supreme Court of India", "இந்திய உச்ச நீதிமன்ற நீதிபதிகளை நியமித்தல்")
        ],
        "exp_en": "Article 280(3)(d) provides that the Commission shall perform duties regarding 'any other matter referred to the Commission by the President in the interests of sound finance'.",
        "exp_ta": "சரத்து 280(3)(d), 'செம்மையான நிதி மேலாண்மை நலன் கருதி குடியரசுத் தலைவரால் ஆணையத்திற்கு பரிந்துரைக்கப்படும் பிற விஷயங்கள்' குறித்து கடமைகளை ஆற்ற வகைசெய்கிறது.",
        "tip_en": "Terms of Reference (ToR) issued by the President under 280(3)(d) can include disaster relief, debt relief, defence funding, etc.",
        "tip_ta": "சரத்து 280(3)(d)-ன் கீழ் குடியரசுத் தலைவர் வழங்கும் பணிக் குறிப்புகள் (ToR) பேரிடர் நிதி, கடன் நிவாரணம் போன்றவற்றை உள்ளடக்கும்.",
        "fact_en": "15th FC was specifically asked to examine a separate defence and internal security funding mechanism under this clause.",
        "fact_ta": "இப்பிரிவின் கீழ் பாதுகாப்பு மற்றும் உள்நாட்டுப் பாதுகாப்புக்கான தனி நிதியை ஆராய 15வது நிதி ஆணையம் கேட்கப்பட்டது."
    },
    # 17
    {
        "subtopic": "Fourteenth Finance Commission Chairman",
        "stem_en": "Who chaired the Fourteenth Finance Commission of India (2015-2020)?",
        "stem_ta": "இந்தியாவின் 14வது நிதி ஆணையத்தின் (2015-2020) தலைவர் யார்?",
        "options": [
            ("Dr. Y.V. Reddy", "டாக்டர் ஒய்.வி. ரெட்டி"),
            ("Dr. C. Rangarajan", "டாக்டர் சி. ரங்கராஜன்"),
            ("Dr. Vijay Kelkar", "டாக்டர் விஜய் கேல்கர்"),
            ("N.K. Singh", "என்.கே. சிங்")
        ],
        "exp_en": "Dr. Y.V. Reddy, former Governor of the Reserve Bank of India, was the Chairman of the Fourteenth Finance Commission (2015-2020).",
        "exp_ta": "முன்னாள் ரிசர்வ் வங்கி ஆளுநர் டாக்டர் ஒய்.வி. ரெட்டி 14வது நிதி ஆணையத்தின் (2015-2020) தலைவராகப் பணியாற்றினார்.",
        "tip_en": "14th FC = Dr. Y.V. Reddy. Landmark achievement = 42% devolution to States.",
        "tip_ta": "14வது நிதி ஆணையம் = டாக்டர் ஒய்.வி. ரெட்டி. முக்கிய மைல்கல் = மாநிலங்களுக்கு 42% வரிப் பகிர்வு.",
        "fact_en": "The 14th FC recommended the largest ever increase in vertical tax devolution from 32% to 42%.",
        "fact_ta": "14வது நிதி ஆணையம் செங்குத்து வரிப் பகிர்வை 32%-லிருந்து 42%-ஆக வரலாறு காணாத அளவில் உயர்த்தியது."
    },
    # 18
    {
        "subtopic": "Fifteenth Finance Commission Chairman",
        "stem_en": "Who served as the Chairman of the Fifteenth Finance Commission of India (2020-2026)?",
        "stem_ta": "இந்தியாவின் 15வது நிதி ஆணையத்தின் (2020-2026) தலைவராகப் பணியாற்றியவர் யார்?",
        "options": [
            ("N.K. Singh", "என்.கே. சிங்"),
            ("Dr. Arvind Panagariya", "டாக்டர் அரவிந்த் பனகாரியா"),
            ("Bimal Jalan", "பிமல் ஜலான்"),
            ("Raghuram Rajan", "ரகுராம் ராஜன்")
        ],
        "exp_en": "N.K. Singh, a former senior bureaucrat and Member of Parliament, served as the Chairman of the Fifteenth Finance Commission.",
        "exp_ta": "முன்னாள் மூத்த அதிகாரி மற்றும் நாடாளுமன்ற உறுப்பினரான என்.கே. சிங் 15வது நிதி ஆணையத்தின் தலைவராகப் பணியாற்றினார்.",
        "tip_en": "15th FC Chairman = N.K. Singh (Report title: 'Finance Commission in COVID Times').",
        "tip_ta": "15வது நிதி ஆணையத் தலைவர் = என்.கே. சிங் (அறிக்கையின் தலைப்பு: 'கோவிட் காலத்தில் நிதி ஆணையம்').",
        "fact_en": "The 15th FC was constituted in November 2017.",
        "fact_ta": "15வது நிதி ஆணையம் நவம்பர் 2017-ல் அமைக்கப்பட்டது."
    },
    # 19
    {
        "subtopic": "Sixteenth Finance Commission Chairman",
        "stem_en": "Who was appointed as the Chairman of the Sixteenth Finance Commission constituted in December 2023?",
        "stem_ta": "டிசம்பர் 2023-ல் அமைக்கப்பட்ட 16வது நிதி ஆணையத்தின் தலைவராக நியமிக்கப்பட்டவர் யார்?",
        "options": [
            ("Dr. Arvind Panagariya", "டாக்டர் அரவிந்த் பனகாரியா"),
            ("Dr. Rajiv Kumar", "டாக்டர் ராஜீவ் குமார்"),
            ("Bibek Debroy", "பிபேக் தேப்ராய்"),
            ("Suman Bery", "சுமன் பெரி")
        ],
        "exp_en": "Dr. Arvind Panagariya, former Vice-Chairman of NITI Aayog and Professor at Columbia University, was appointed as the Chairman of the Sixteenth Finance Commission constituted on December 31, 2023.",
        "exp_ta": "நிதி ஆயோக்கின் முன்னாள் துணைத் தலைவரும் கொலம்பியா பல்கலைக்கழகப் பேராசிரியருமான டாக்டர் அரவிந்த் பனகாரியா டிசம்பர் 31, 2023 அன்று அமைக்கப்பட்ட 16வது நிதி ஆணையத்தின் தலைவராக நியமிக்கப்பட்டார்.",
        "tip_en": "16th FC Chairman = Dr. Arvind Panagariya (Award period: 2026-2031).",
        "tip_ta": "16வது நிதி ஆணையத் தலைவர் = டாக்டர் அரவிந்த் பனகாரியா (பரிந்துரைக் காலம்: 2026-2031).",
        "fact_en": "The report of the 16th Finance Commission is due by October 31, 2025.",
        "fact_ta": "16வது நிதி ஆணையத்தின் அறிக்கை அக்டோபர் 31, 2025-க்குள் சமர்ப்பிக்கப்பட வேண்டும்."
    },
    # 20
    {
        "subtopic": "Vertical Tax Devolution Percentage (15th FC)",
        "stem_en": "What vertical tax devolution share to the States was recommended by the 15th Finance Commission for 2021-2026?",
        "stem_ta": "2021-2026 காலத்திற்கு மாநிலங்களுக்கான செங்குத்து வரிப் பகிர்வு சதவீதமாக 15வது நிதி ஆணையம் எவ்வளவு பரிந்துரைத்தது?",
        "options": [
            ("41%", "41%"),
            ("42%", "42%"),
            ("32%", "32%"),
            ("50%", "50%")
        ],
        "exp_en": "The 15th Finance Commission recommended that the States' share in the net proceeds of Union taxes be 41%, adjusting 1% from the 14th FC's 42% for the newly created Union Territories of Jammu & Kashmir and Ladakh.",
        "exp_ta": "15வது நிதி ஆணையம் மத்திய வரிகளில் மாநிலங்களின் பங்கை 41% ஆக பரிந்துரைத்தது; 14வது ஆணையத்தின் 42%-லிருந்து 1% குறைக்கப்பட்டது புதிதாக உருவாக்கப்பட்ட ஜம்மு காஷ்மீர் மற்றும் லடாக் ஒன்றியப் பிரதேசங்களுக்காக சரிசெய்யப்பட்டது.",
        "tip_en": "14th FC = 42%. 15th FC = 41% (1% reserved for UTs of J&K and Ladakh).",
        "tip_ta": "14வது நிதி ஆணையம் = 42%. 15வது நிதி ஆணையம் = 41% (1% ஜம்மு காஷ்மீர் மற்றும் லடாக் யூனியன் பிரதேசங்களுக்கு).",
        "fact_en": "Union Territories are funded directly by the Centre, so they are not part of the States' divisible pool.",
        "fact_ta": "ஒன்றியப் பிரதேசங்களுக்கு மத்திய அரசு நேரடியாக நிதியளிப்பதால் அவை மாநிலங்களின் பகிர்வு நிதியில் சேராது."
    },
    # 21
    {
        "subtopic": "Alternative Devolution Scheme (80th Amendment)",
        "stem_en": "Which Constitutional Amendment Act introduced the 'Alternative Scheme of Devolution' based on the Tenth Finance Commission's recommendation?",
        "stem_ta": "10வது நிதி ஆணையத்தின் பரிந்துரையின் அடிப்படையில் 'மாற்று வரிப் பகிர்வு முறையை' அறிமுகப்படுத்திய அரசியலமைப்புத் திருத்தச் சட்டம் எது?",
        "options": [
            ("80th Constitutional Amendment Act, 2000", "80வது அரசியலமைப்புத் திருத்தச் சட்டம், 2000"),
            ("42nd Constitutional Amendment Act, 1976", "42வது அரசியலமைப்புத் திருத்தச் சட்டம், 1976"),
            ("44th Constitutional Amendment Act, 1978", "44வது அரசியலமைப்புத் திருத்தச் சட்டம், 1978"),
            ("91st Constitutional Amendment Act, 2003", "91வது அரசியலமைப்புத் திருத்தச் சட்டம், 2003")
        ],
        "exp_en": "The 80th Amendment Act 2000 implemented the Alternative Scheme of Devolution recommended by the 10th FC (under K.C. Pant), sharing 29% of all central taxes (with few exceptions) with States, replacing the earlier selective tax-sharing regime.",
        "exp_ta": "2000 ஆம் ஆண்டின் 80வது திருத்தச் சட்டம், 10வது நிதி ஆணையம் (கே.சி. பந்த்) பரிந்துரைத்த மாற்றுப் பகிர்வு முறையை அமல்படுத்தி, அனைத்து மத்திய வரிகளிலிருந்தும் 29%-ஐ மாநிலங்களுடன் பகிர்ந்துகொள்ள வகைசெய்தது.",
        "tip_en": "80th Amendment 2000 = All central taxes pooled for devolution (Tenth FC recommendation).",
        "tip_ta": "80வது திருத்தம் 2000 = அனைத்து மத்திய வரிகளும் பகிர்வுக்காக ஒருங்கிணைக்கப்பட்டன (10வது நிதி ஆணையப் பரிந்துரை).",
        "fact_en": "Prior to the 80th Amendment, only Income Tax and Union Excise Duties were shared with States.",
        "fact_ta": "80வது திருத்தத்திற்கு முன்பு வருமான வரி மற்றும் மத்திய கலால் வரி மட்டுமே மாநிலங்களுடன் பகிரப்பட்டன."
    },
    # 22
    {
        "subtopic": "Exclusion of Cesses and Surcharges",
        "stem_en": "Under Article 271 of the Constitution, which levies are excluded from the divisible tax pool shared with the States?",
        "stem_ta": "அரசியலமைப்பின் சரத்து 271-ன் கீழ், மாநிலங்களுடன் பகிரப்படும் வரி நிதியிலிருந்து விலக்கப்பட்டுள்ள வரிகள் எவை?",
        "options": [
            ("Surcharges and cesses levied for specific Union purposes", "குறிப்பிட்ட மத்திய நோக்கங்களுக்காக விதிக்கப்படும் கூடுதல் வரிகள் (Surcharges) மற்றும் செஸ் (Cess) வரிகள்"),
            ("Corporation Tax", "நிறுவன வரி (Corporation Tax)"),
            ("Central Goods and Services Tax (CGST)", "மத்திய சரக்கு மற்றும் சேவை வரி (CGST)"),
            ("Personal Income Tax", "தனிநபர் வருமான வரி")
        ],
        "exp_en": "Under Article 271, Parliament may at any time increase any duties or taxes by a surcharge for the purposes of the Union and the whole proceeds of any such surcharge form part of the Consolidated Fund of India and are not divisible with the States.",
        "exp_ta": "சரத்து 271-ன் கீழ், மத்திய அரசின் தேவைகளுக்காக நாடாளுமன்றம் எந்தவொரு வரி மீதும் கூடுதல் கட்டணத்தை (Surcharge/Cess) விதிக்கலாம்; அதன் முழு வருவாயும் மத்திய அரசே வைத்துக் கொள்ளும்; மாநிலங்களுடன் பகிரப்படாது.",
        "tip_en": "Cesses and surcharges bypass the divisible pool, a frequent complaint of State Governments.",
        "tip_ta": "செஸ் மற்றும் கூடுதல் வரிகள் பகிர்வு நிதியில் சேராது என்பது மாநில அரசுகளின் தொடர் புகாராகும்.",
        "fact_en": "Cesses and surcharges currently constitute about 18-20% of the Centre's gross tax revenue.",
        "fact_ta": "தற்போது மத்திய அரசின் மொத்த வரி வருவாயில் செஸ் மற்றும் கூடுதல் வரிகள் சுமார் 18-20% ஆக உள்ளன."
    },
    # 23
    {
        "subtopic": "Horizontal Devolution Criteria: Income Distance",
        "stem_en": "In the 15th Finance Commission's horizontal devolution formula, which criterion carries the highest weight?",
        "stem_ta": "15வது நிதி ஆணையத்தின் கிடைமட்ட வரிப் பகிர்வு சூத்திரத்தில் எந்த அளவுகோல் அதிக எடையைக் கொண்டுள்ளது?",
        "options": [
            ("Income Distance (45%)", "வருமான இடைவெளி - Income Distance (45%)"),
            ("Population (15%)", "மக்கள் தொகை (15%)"),
            ("Area (15%)", "பரப்பளவு (15%)"),
            ("Forest and Ecology (10%)", "காடு மற்றும் சூழலியல் (10%)")
        ],
        "exp_en": "The 15th Finance Commission assigned the highest weight of 45% to 'Income Distance' (the difference of each State's per capita GSDP from that of the benchmark top state), ensuring fiscal equity.",
        "exp_ta": "15வது நிதி ஆணையம் 'வருமான இடைவெளிக்கு' (Income Distance) அதிகபட்சமாக 45% எடையை ஒதுக்கியது; இது பின்தங்கிய மாநிலங்களுக்கு அதிக நிதி கிடைக்கச் செய்து நிதிச் சமத்துவத்தை உறுதி செய்கிறது.",
        "tip_en": "Income Distance has consistently been the largest single weight in horizontal devolution (45%-50%).",
        "tip_ta": "கிடைமட்டப் பகிர்வில் எப்போதும் அதிகபட்ச எடையைக் கொண்டிருப்பது வருமான இடைவெளி (45%-50%).",
        "fact_en": "Haryana / Goa is typically used as the benchmark highest per capita income State.",
        "fact_ta": "ஹரியானா / கோவா வழக்கமாக அதிக தனிநபர் வருமானம் கொண்ட ஒப்பீட்டு மாநிலமாகப் பயன்படுத்தப்படுகிறது."
    },
    # 24
    {
        "subtopic": "2011 Census Usage in 15th FC",
        "stem_en": "Which Census population data was exclusively used by the 15th Finance Commission for its devolution formula?",
        "stem_ta": "15வது நிதி ஆணையம் தனது வரிப் பகிர்வு சூத்திரத்திற்காக எந்த மக்கள் தொகை கணக்கெடுப்புத் தரவை மட்டுமே பயன்படுத்தியது?",
        "options": [
            ("2011 Census", "2011 மக்கள் தொகை கணக்கெடுப்பு"),
            ("1971 Census", "1971 மக்கள் தொகை கணக்கெடுப்பு"),
            ("2001 Census", "2001 மக்கள் தொகை கணக்கெடுப்பு"),
            ("1991 Census", "1991 மக்கள் தொகை கணக்கெடுப்பு")
        ],
        "exp_en": "The Terms of Reference (ToR) of the 15th Finance Commission mandated the use of population data from the 2011 Census, departing from the earlier practice of using 1971 Census data.",
        "exp_ta": "15வது நிதி ஆணையத்தின் பணிக் குறிப்பு (ToR) 2011 மக்கள் தொகை கணக்கெடுப்புத் தரவை மட்டுமே பயன்படுத்த உத்தரவிட்டது; இது முந்தைய 1971 கணக்கெடுப்பைப் பயன்படுத்தும் முறையிலிருந்து மாறுபட்டது.",
        "tip_en": "15th FC used 2011 Census with 15% weight for population and added 12.5% for Demographic Performance.",
        "tip_ta": "15வது நிதி ஆணையம் 2011 மக்கள் தொகைக்கு 15% எடையும், மக்கள் தொகை கட்டுப்பாட்டு செயல்திறனுக்கு 12.5% எடையும் ஒதுக்கியது.",
        "fact_en": "Southern states had raised concerns that using 2011 Census would penalize them for successful population control.",
        "fact_ta": "மக்கள் தொகையைக் கட்டுப்படுத்தியதற்காக தென் மாநிலங்கள் பாதிக்கப்படும் என்ற கவலை எழுப்பப்பட்டது."
    },
    # 25
    {
        "subtopic": "Demographic Performance Criterion",
        "stem_en": "To incentivize states that successfully controlled population growth, the 15th Finance Commission introduced which criterion?",
        "stem_ta": "மக்கள் தொகை வளர்ச்சியைக் கட்டுப்படுத்திய மாநிலங்களை ஊக்குவிக்க 15வது நிதி ஆணையம் அறிமுகப்படுத்திய அளவுகோல் எது?",
        "options": [
            ("Demographic Performance (12.5% weight)", "மக்கள்தொகை செயல்திறன் - Demographic Performance (12.5% எடை)"),
            ("Urban Literacy Index", "நகர்ப்புற எழுத்தறிவு குறியீடு"),
            ("Infant Vaccination Coverage", "குழந்தை தடுப்பூசி பாதுகாப்பு"),
            ("Digital Health Card Adoption", "டிஜிட்டல் சுகாதார அட்டை பயன்பாடு")
        ],
        "exp_en": "To reward States with lower fertility rates (Total Fertility Rate - TFR) and address concerns of Southern States regarding 2011 Census usage, the 15th FC introduced 'Demographic Performance' with a 12.5% weight.",
        "exp_ta": "குறைந்த பிறப்பு விகிதத்தை (TFR) எட்டிய மாநிலங்களை கௌரவிக்கவும் 2011 மக்கள் தொகையால் தென் மாநிலங்களுக்கு ஏற்படும் பாதிப்பை ஈடுசெய்யவும் 12.5% எடையுடன் 'மக்கள்தொகை செயல்திறன்' அளவுகோலை 15வது நிதி ஆணையம் அறிமுகப்படுத்தியது.",
        "tip_en": "Demographic Performance rewards lower Total Fertility Rates (TFR).",
        "tip_ta": "மக்கள்தொகை செயல்திறன் என்பது குறைந்த கருவுறுதல் விகிதத்தை (TFR) எட்டியதற்கு வெகுமதி அளிக்கிறது.",
        "fact_en": "States with TFR below replacement rate (2.1) scored maximum marks in this criterion.",
        "fact_ta": "மாற்று நிலைக்குக் கீழே (2.1) கருவுறுதல் விகிதம் கொண்ட மாநிலங்கள் இதில் அதிக மதிப்பெண்களைப் பெற்றன."
    },
    # 26
    {
        "subtopic": "Forest and Ecology Criterion",
        "stem_en": "What was the weight assigned to 'Forest and Ecology' by the 15th Finance Commission in horizontal devolution?",
        "stem_ta": "15வது நிதி ஆணையத்தால் கிடைமட்ட வரிப் பகிர்வில் 'காடு மற்றும் சூழலியல்' அளவுகோலுக்கு ஒதுக்கப்பட்ட எடை என்ன?",
        "options": [
            ("10%", "10%"),
            ("7.5%", "7.5%"),
            ("15%", "15%"),
            ("5%", "5%")
        ],
        "exp_en": "The 15th Finance Commission assigned a 10% weight to 'Forest and Ecology' to compensate and incentivize States maintaining dense forest cover for ecological services.",
        "exp_ta": "சூழலியல் சேவைகளுக்காக அடர்ந்த காடுகளைப் பராமரிக்கும் மாநிலங்களை ஊக்குவிக்கவும் ஈடுசெய்யவும் 'காடு மற்றும் சூழலியல்' அளவுகோலுக்கு 15வது நிதி ஆணையம் 10% எடையை ஒதுக்கியது.",
        "tip_en": "14th FC had assigned 7.5% to Forest cover; 15th FC raised it to 10% under 'Forest and Ecology'.",
        "tip_ta": "14வது நிதி ஆணையம் 7.5% ஒதுக்கியது; 15வது நிதி ஆணையம் அதை 10% ஆக உயர்த்தியது.",
        "fact_en": "Calculated based on share of dense and moderately dense forest cover reported by Forest Survey of India.",
        "fact_ta": "இந்திய வன ஆய்வு அறிக்கை வெளியிடும் அடர்ந்த மற்றும் மிதமான காடுகளின் பரப்பளவு அடிப்படையில் இது கணக்கிடப்படுகிறது."
    },
    # 27
    {
        "subtopic": "Tax and Fiscal Effort Criterion",
        "stem_en": "What weight was allocated to 'Tax and Fiscal Effort' by the 15th Finance Commission?",
        "stem_ta": "15வது நிதி ஆணையத்தால் 'வரி மற்றும் நிதி முயற்சி' அளவுகோலுக்கு ஒதுக்கப்பட்ட எடை என்ன?",
        "options": [
            ("2.5%", "2.5%"),
            ("5%", "5%"),
            ("7.5%", "7.5%"),
            ("10%", "10%")
        ],
        "exp_en": "The 15th Finance Commission allocated 2.5% weight to 'Tax and Fiscal Effort' to reward States that demonstrated higher tax collection efficiency relative to their economic potential.",
        "exp_ta": "தங்கள் பொருளாதாரத் திறனுடன் ஒப்பிடும்போது அதிக வரி வசூல் செயல்திறனைக் காட்டிய மாநிலங்களை ஊக்குவிக்க 'வரி மற்றும் நிதி முயற்சி' அளவுகோலுக்கு 15வது நிதி ஆணையம் 2.5% எடையை ஒதுக்கியது.",
        "tip_en": "Tax Effort = 2.5% weight (incentivizes higher own tax revenue generation).",
        "tip_ta": "வரி முயற்சி = 2.5% எடை (சொந்த வரி வருவாயைப் பெருக்குவதை ஊக்குவிக்கிறது).",
        "fact_en": "Measured by the ratio of own tax revenue to GSDP over a three-year period.",
        "fact_ta": "மூன்றாண்டு காலத்தில் மாநிலத்தின் சொந்த வரி வருவாய்க்கும் GSDP-க்கும் உள்ள விகிதத்தின் அடிப்படையில் இது அளவிடப்படுகிறது."
    },
    # 28
    {
        "subtopic": "Full 15th FC Horizontal Devolution Weights",
        "stem_en": "Which of the following correctly lists all criteria and weights used by the 15th Finance Commission (2021-26)?",
        "stem_ta": "15வது நிதி ஆணையம் (2021-26) பயன்படுத்திய அனைத்து அளவுகோல்கள் மற்றும் எடைகளை சரியாகக் குறிப்பிடுவது எது?",
        "options": [
            ("Income Distance: 45%, Population: 15%, Area: 15%, Forest & Ecology: 10%, Demographic Performance: 12.5%, Tax Effort: 2.5%", "வருமான இடைவெளி: 45%, மக்கள் தொகை: 15%, பரப்பளவு: 15%, காடு & சூழலியல்: 10%, மக்கள்தொகை செயல்திறன்: 12.5%, வரி முயற்சி: 2.5%"),
            ("Income Distance: 50%, Population: 25%, Area: 10%, Forest: 10%, Infrastructure: 5%", "வருமான இடைவெளி: 50%, மக்கள் தொகை: 25%, பரப்பளவு: 10%, காடு: 10%, உள்கட்டமைப்பு: 5%"),
            ("Income Distance: 40%, Population: 30%, Area: 20%, Fiscal Discipline: 10%", "வருமான இடைவெளி: 40%, மக்கள் தொகை: 30%, பரப்பளவு: 20%, நிதி ஒழுங்கு: 10%"),
            ("Income Distance: 60%, Area: 20%, Population: 20%", "வருமான இடைவெளி: 60%, பரப்பளவு: 20%, மக்கள் தொகை: 20%")
        ],
        "exp_en": "Total 100% weight in 15th FC horizontal formula: Income Distance (45%) + Population (15%) + Area (15%) + Forest & Ecology (10%) + Demographic Performance (12.5%) + Tax Effort (2.5%) = 100%.",
        "exp_ta": "15வது நிதி ஆணையத்தின் 100% பகிர்வு சூத்திரம்: வருமான இடைவெளி (45%) + மக்கள் தொகை (15%) + பரப்பளவு (15%) + காடு & சூழலியல் (10%) + மக்கள்தொகை செயல்திறன் (12.5%) + வரி முயற்சி (2.5%) = 100%.",
        "tip_en": "Memorize the 6 criteria: 45 + 15 + 15 + 10 + 12.5 + 2.5 = 100%.",
        "tip_ta": "இந்த 6 அளவுகோல்களை நினைவில் வையுங்கள்: 45 + 15 + 15 + 10 + 12.5 + 2.5 = 100%.",
        "fact_en": "Area and Population share equal weight (15% each) in the 15th FC formula.",
        "fact_ta": "பரப்பளவு மற்றும் மக்கள் தொகை இரண்டும் சமமான எடையைப் (தலா 15%) பெற்றுள்ளன."
    },
    # 29
    {
        "subtopic": "State Finance Commission Linkage (Article 243-I)",
        "stem_en": "Under which Article of the Constitution is a State Finance Commission (SFC) constituted by the Governor?",
        "stem_ta": "அரசியலமைப்பின் எந்தச் சரத்தின் கீழ் மாநில ஆளுநரால் மாநில நிதி ஆணையம் (SFC) அமைக்கப்படுகிறது?",
        "options": [
            ("Article 243-I", "சரத்து 243-I"),
            ("Article 243-K", "சரத்து 243-K"),
            ("Article 243-D", "சரத்து 243-D"),
            ("Article 280", "சரத்து 280")
        ],
        "exp_en": "Article 243-I provides that the Governor of a State shall, within one year from the commencement of the 73rd Amendment and thereafter every fifth year, constitute a Finance Commission to review the financial position of the Panchayats.",
        "exp_ta": "சரத்து 243-I, பஞ்சாயத்துகளின் நிதி நிலையை மறுஆய்வு செய்வதற்காக ஒவ்வொரு ஐந்தாவது ஆண்டும் ஆளுநர் ஒரு மாநில நிதி ஆணையத்தை அமைக்க வேண்டும் என வகைசெய்கிறது.",
        "tip_en": "Article 243-I = State Finance Commission for Panchayats. Article 243-Y = Application to Municipalities.",
        "tip_ta": "சரத்து 243-I = பஞ்சாயத்துகளுக்கான மாநில நிதி ஆணையம். சரத்து 243-Y = நகராட்சிகளுக்கான பயன்பாடு.",
        "fact_en": "The recommendations of the State Finance Commission are submitted to the Governor.",
        "fact_ta": "மாநில நிதி ஆணையத்தின் பரிந்துரைகள் மாநில ஆளுநரிடம் சமர்ப்பிக்கப்படுகின்றன."
    },
    # 30
    {
        "subtopic": "State Finance Commission for Municipalities (Article 243-Y)",
        "stem_en": "Which Article applies the provisions of the State Finance Commission to Municipalities?",
        "stem_ta": "மாநில நிதி ஆணையத்தின் விதிகளை நகராட்சிகளுக்கும் பொருந்தச் செய்யும் சரத்து எது?",
        "options": [
            ("Article 243-Y", "சரத்து 243-Y"),
            ("Article 243-Z", "சரத்து 243-Z"),
            ("Article 243-W", "சரத்து 243-W"),
            ("Article 243-T", "சரத்து 243-T")
        ],
        "exp_en": "Article 243-Y mandates that the Finance Commission constituted under Article 243-I shall also review the financial position of the Municipalities and make recommendations to the Governor.",
        "exp_ta": "சரத்து 243-Y, சரத்து 243-I-ன் கீழ் அமைக்கப்பட்ட நிதி ஆணையமே நகராட்சிகளின் நிதி நிலையை மறுஆய்வு செய்து ஆளுநருக்குப் பரிந்துரைகளை வழங்க வேண்டும் என உத்தரவிடுகிறது.",
        "tip_en": "243-I (Panchayats) and 243-Y (Municipalities) are twin SFC articles.",
        "tip_ta": "243-I (பஞ்சாயத்துகள்) மற்றும் 243-Y (நகராட்சிகள்) இரட்டை SFC சரத்துகளாகும்.",
        "fact_en": "Both local body tiers share a single unified State Finance Commission in each State.",
        "fact_ta": "ஒவ்வொரு மாநிலத்திலும் இரு உள்ளாட்சி அமைப்புகளுக்கும் ஒரே ஒருங்கிணைந்த மாநில நிதி ஆணையமே செயல்படுகிறது."
    },
    # 31
    {
        "subtopic": "Twelfth Finance Commission Chairman",
        "stem_en": "Who chaired the Twelfth Finance Commission of India (2005-2010)?",
        "stem_ta": "இந்தியாவின் 12வது நிதி ஆணையத்தின் (2005-2010) தலைவர் யார்?",
        "options": [
            ("Dr. C. Rangarajan", "டாக்டர் சி. ரங்கராஜன்"),
            ("Dr. Vijay Kelkar", "டாக்டர் விஜய் கேல்கர்"),
            ("A.M. Khusro", "ஏ.எம். குஸ்ரோ"),
            ("K.C. Pant", "கே.சி. பந்த்")
        ],
        "exp_en": "Dr. C. Rangarajan, eminent economist and former Governor of RBI, served as the Chairman of the Twelfth Finance Commission (2005-2010).",
        "exp_ta": "புகழ்பெற்ற பொருளாதார நிபுணரும் முன்னாள் ரிசர்வ் வங்கி ஆளுநருமான டாக்டர் சி. ரங்கராஜன் 12வது நிதி ஆணையத்தின் (2005-2010) தலைவராகப் பணியாற்றினார்.",
        "tip_en": "12th FC = Dr. C. Rangarajan. Pioneered debt consolidation and relief facility linked to state FRBMs.",
        "tip_ta": "12வது நிதி ஆணையம் = டாக்டர் சி. ரங்கராஜன். மாநில FRBM சட்டங்களுடன் இணைக்கப்பட்ட கடன் நிவாரண முறையை உருவாக்கினார்.",
        "fact_en": "12th FC recommended sharing 30.5% of central divisible taxes with States.",
        "fact_ta": "12வது நிதி ஆணையம் மத்திய வரிகளில் 30.5%-ஐ மாநிலங்களுக்குப் பகிர பரிந்துரைத்தது."
    },
    # 32
    {
        "subtopic": "Thirteenth Finance Commission Chairman",
        "stem_en": "Who chaired the Thirteenth Finance Commission of India (2010-2015)?",
        "stem_ta": "இந்தியாவின் 13வது நிதி ஆணையத்தின் (2010-2015) தலைவர் யார்?",
        "options": [
            ("Dr. Vijay Kelkar", "டாக்டர் விஜய் கேல்கர்"),
            ("Dr. Y.V. Reddy", "டாக்டர் ஒய்.வி. ரெட்டி"),
            ("Montek Singh Ahluwalia", "மாண்டேக் சிங் அலுவாலியா"),
            ("Bimal Jalan", "பிமல் ஜலான்")
        ],
        "exp_en": "Dr. Vijay Kelkar chaired the Thirteenth Finance Commission (2010-2015), which recommended a 32% vertical devolution share.",
        "exp_ta": "டாக்டர் விஜய் கேல்கர் 13வது நிதி ஆணையத்தின் (2010-2015) தலைவராகப் பணியாற்றினார்; இது 32% செங்குத்து வரிப் பகிர்வைப் பரிந்துரைத்தது.",
        "tip_en": "13th FC = Dr. Vijay Kelkar. First to lay down the fiscal architecture and compensation design for GST.",
        "tip_ta": "13வது நிதி ஆணையம் = டாக்டர் விஜய் கேல்கர். ஜி.எஸ்.டி-க்கான நிதி இழப்பீட்டு கட்டமைப்பை முதலில் வடிவமைத்தவர்.",
        "fact_en": "The 13th FC recommended a landmark Rs. 50,000 crore grant for the implementation of GST.",
        "fact_ta": "ஜி.எஸ்.டி அமலாக்கத்திற்காக ரூ. 50,000 கோடி மானியத்தை 13வது நிதி ஆணையம் பரிந்துரைத்தது."
    },
    # 33
    {
        "subtopic": "Post-Devolution Revenue Deficit Grants",
        "stem_en": "Under which Article does the Finance Commission recommend Post-Devolution Revenue Deficit Grants (PDRDG)?",
        "stem_ta": "வரிப் பகிர்வுக்குப் பிந்தைய வருவாய்ப் பற்றாக்குறை மானியங்களை (PDRDG) எந்தச் சரத்தின் கீழ் நிதி ஆணையம் பரிந்துரைக்கிறது?",
        "options": [
            ("Article 275", "சரத்து 275"),
            ("Article 282", "சரத்து 282"),
            ("Article 269", "சரத்து 269"),
            ("Article 270", "சரத்து 270")
        ],
        "exp_en": "Post-Devolution Revenue Deficit Grants are recommended under Article 275 of the Constitution to meet the assessed revenue deficits of States after taking into account tax devolution.",
        "exp_ta": "வரிப் பகிர்வை கணக்கில் கொண்ட பிறகும் மாநிலங்களுக்கு ஏற்படும் வருவாய்ப் பற்றாக்குறையை ஈடுசெய்ய அரசியலமைப்பின் சரத்து 275-ன் கீழ் இந்த மானியங்கள் பரிந்துரைக்கப்படுகின்றன.",
        "tip_en": "PDRDG = Article 275 statutory grant to bridge post-tax-devolution deficits.",
        "tip_ta": "PDRDG = வரிப் பகிர்வுக்குப் பிந்தைய பற்றாக்குறையை தீர்க்க சரத்து 275-ன் கீழான சட்டப்பூர்வ மானியம்.",
        "fact_en": "The 15th FC recommended Rs. 2.94 lakh crore as revenue deficit grants for 17 States over 2021-2026.",
        "fact_ta": "15வது நிதி ஆணையம் 2021-2026 காலத்தில் 17 மாநிலங்களுக்கு ரூ. 2.94 லட்சம் கோடி வருவாய்ப் பற்றாக்குறை மானியங்களை பரிந்துரைத்தது."
    },
    # 34
    {
        "subtopic": "Disaster Management Financing Recommendation",
        "stem_en": "Which two funds for disaster financing were recommended to be set up at the State level by the 15th Finance Commission?",
        "stem_ta": "15வது நிதி ஆணையத்தால் மாநில அளவில் அமைக்க பரிந்துரைக்கப்பட்ட இரண்டு பேரிடர் நிதிகள் எவை?",
        "options": [
            ("State Disaster Response Fund (SDRF) and State Disaster Mitigation Fund (SDMF)", "மாநில பேரிடர் மீட்பு நிதி (SDRF) மற்றும் மாநில பேரிடர் தணிப்பு நிதி (SDMF)"),
            ("State Drought Relief Trust and State Flood Cess", "மாநில வறட்சி நிவாரண அறக்கட்டளை மற்றும் வெள்ள வரி"),
            ("State Civil Defence Pool and Police Modernization Fund", "மாநில சிவில் பாதுகாப்பு நிதி மற்றும் போலீஸ் நவீனமயமாக்கல் நிதி"),
            ("Emergency Revenue Reserve and Municipal Bond Pool", "அவசர வருவாய் இருப்பு மற்றும் நகராட்சி பத்திர நிதி")
        ],
        "exp_en": "The 15th Finance Commission recommended setting up the State Disaster Risk Management Fund (SDRMF), which comprises both the State Disaster Response Fund (SDRF) for relief and the State Disaster Mitigation Fund (SDMF) for prevention.",
        "exp_ta": "15வது நிதி ஆணையம் மாநில பேரிடர் இடர் மேலாண்மை நிதியை (SDRMF) பரிந்துரைத்தது; இது நிவாரணத்திற்கான SDRF மற்றும் தடுப்புக்கான SDMF ஆகிய இரண்டையும் உள்ளடக்கியது.",
        "tip_en": "Disaster funding ratio: 75:25 for general states; 90:10 for North-East & Himalayan states.",
        "tip_ta": "பேரிடர் நிதி பகிர்வு: பொது மாநிலங்களுக்கு 75:25; வடகிழக்கு மற்றும் இமயமலை மாநிலங்களுக்கு 90:10.",
        "fact_en": "SDRMF funding is shared between the Union and the States.",
        "fact_ta": "SDRMF நிதி மத்திய மற்றும் மாநில அரசுகளுக்கு இடையே பகிரப்படுகிறது."
    },
    # 35
    {
        "subtopic": "Net Proceeds Calculation Certificate",
        "stem_en": "Who ascertains and certifies the 'net proceeds' of taxes distributed by the Finance Commission?",
        "stem_ta": "நிதி ஆணையத்தால் பகிர்ந்தளிக்கப்படும் வரிகளின் 'நிகர வருமானத்தை' கணக்கிட்டு சான்றளிப்பவர் யார்?",
        "options": [
            ("The Comptroller and Auditor General of India (CAG)", "இந்தியத் தலைமைக் கணக்குத் தணிக்கையாளர் (சி.ஏ.ஜி)"),
            ("The Governor of the Reserve Bank of India", "இந்திய ரிசர்வ் வங்கி ஆளுநர்"),
            ("The Chairman of the Finance Commission", "நிதி ஆணையத்தின் தலைவர்"),
            ("The Union Revenue Secretary", "மத்திய வருவாய்த் துறைச் செயலாளர்")
        ],
        "exp_en": "Under Article 279(1), the net proceeds of any tax or duty are ascertained and certified by the Comptroller and Auditor General of India, whose certificate is final and conclusive.",
        "exp_ta": "சரத்து 279(1)-ன் படி, எந்தவொரு வரியின் நிகர வருவாயும் இந்தியத் தலைமைக் கணக்குத் தணிக்கையாளரால் (சி.ஏ.ஜி) கணக்கிடப்பட்டு சான்றளிக்கப்படுகிறது; அவரது சான்றிதழ் இறுதியானது.",
        "tip_en": "Net proceeds = Gross collections minus cost of collection (certified by CAG under Art 279).",
        "tip_ta": "நிகர வருமானம் = மொத்த வசூல் - வசூல் செலவு (சரத்து 279-ன் கீழ் சி.ஏ.ஜி சான்றளிக்கிறார்).",
        "fact_en": "Finance Commission uses this CAG net proceeds data to calculate the exact divisible pool.",
        "fact_ta": "நிதி ஆணையம் இந்த சி.ஏ.ஜி தரவைப் பயன்படுத்தியே பிரிக்கக்கூடிய தொகையைக் கணக்கிடுகிறது."
    },
    # 36
    {
        "subtopic": "Disqualification of Members",
        "stem_en": "Under Section 5 of the Finance Commission Act 1951, which of the following is a statutory disqualification for appointment as a member?",
        "stem_ta": "1951 நிதி ஆணையச் சட்டத்தின் பிரிவு 5-ன் கீழ் உறுப்பினராக நியமிக்கப்படுவதற்கு சட்டப்பூர்வ தகுதியிழப்பு எது?",
        "options": [
            ("Being of unsound mind or an undischarged insolvent", "மனநிலை சரியில்லாதவராக இருத்தல் அல்லது தீர்க்கப்படாத திவாலானவராக இருத்தல்"),
            ("Holding a doctorate degree in public finance", "பொது நிதியில் முனைவர் பட்டம் பெற்றிருத்தல்"),
            ("Having served as a civil servant in a state government", "மாநில அரசில் அரசு ஊழியராகப் பணியாற்றியிருத்தல்"),
            ("Having authored books on macroeconomics", "பேரியல் பொருளாதாரம் குறித்து புத்தகங்கள் எழுதியிருத்தல்")
        ],
        "exp_en": "Section 5 of the 1951 Act enumerates disqualifications: of unsound mind, an undischarged insolvent, convicted of an offence involving moral turpitude, or having financial or other interests likely to affect prejudicially his functions.",
        "exp_ta": "1951 சட்டத்தின் பிரிவு 5 தகுதியிழப்புகளைக் குறிப்பிடுகிறது: மனநிலை சரியில்லாதவர், தீர்க்கப்படாத திவாலானவர், ஒழுக்கக்கேடான குற்றத்திற்கு தண்டனை பெற்றவர் அல்லது பாரபட்சத்தை ஏற்படுத்தும் நிதி நலன் கொண்டவர்.",
        "tip_en": "Standard statutory disqualifications: Unsound mind, insolvency, moral turpitude, conflict of interest.",
        "tip_ta": "வழக்கமான சட்ட தகுதியிழப்புகள்: மனநிலை, திவால், குற்றப் பின்னணி, நலன் முரண்பாடு.",
        "fact_en": "A member must disclose any conflicting financial interest to the President.",
        "fact_ta": "உறுப்பினர் ஏதேனும் முரண்பட்ட நிதி நலன் இருந்தால் அதை குடியரசுத் தலைவரிடம் தெரிவிக்க வேண்டும்."
    },
    # 37
    {
        "subtopic": "Secretariat of the Finance Commission",
        "stem_en": "Who heads the operational secretariat that executes the administrative and research work of the Finance Commission?",
        "stem_ta": "நிதி ஆணையத்தின் நிர்வாக மற்றும் ஆராய்ச்சிப் பணிகளை மேற்கொள்ளும் செயலகத்திற்கு தலைமை தாங்குபவர் யார்?",
        "options": [
            ("Secretary to the Finance Commission (Senior IAS officer)", "நிதி ஆணையத்தின் செயலாளர் (மூத்த ஐ.ஏ.எஸ் அதிகாரி)"),
            ("Cabinet Secretary of India", "இந்திய அமைச்சரவைச் செயலாளர்"),
            ("Chief Economic Adviser to the Government", "அரசின் முதன்மை பொருளாதார ஆலோசகர்"),
            ("Director of the Enforcement Directorate", "அமலாக்க இயக்கக இயக்குநர்")
        ],
        "exp_en": "The Finance Commission is supported by a dedicated secretariat headed by a Secretary to the Commission, usually a senior IAS officer of Secretary/Additional Secretary rank to the Government of India.",
        "exp_ta": "நிதி ஆணையத்திற்கு உதவ ஒரு பிரத்யேக செயலகம் உள்ளது; அதற்கு இந்திய அரசின் செயலாளர் அந்தஸ்தில் உள்ள மூத்த ஐ.ஏ.எஸ் அதிகாரி தலைமை தாங்குகிறார்.",
        "tip_en": "16th FC Secretary = Ritvik Ranjanam Pandey, IAS.",
        "tip_ta": "16வது நிதி ஆணையச் செயலாளர் = ரித்விக் ரஞ்சனம் பாண்டே, ஐ.ஏ.எஸ்.",
        "fact_en": "15th FC Secretary was Arvind Mehta, followed by other senior officers.",
        "fact_ta": "15வது நிதி ஆணையத்தின் செயலாளராக அரவிந்த் மேத்தா பணியாற்றினார்."
    },
    # 38
    {
        "subtopic": "Tenth Finance Commission Chairman",
        "stem_en": "Who was the Chairman of the Tenth Finance Commission (1995-2000)?",
        "stem_ta": "10வது நிதி ஆணையத்தின் (1995-2000) தலைவர் யார்?",
        "options": [
            ("K.C. Pant", "கே.சி. பந்த்"),
            ("N.K.P. Salve", "என்.கே.பி. சால்வே"),
            ("A.M. Khusro", "ஏ.எம். குஸ்ரோ"),
            ("J.M. Shelat", "ஜே.எம். ஷெலத்")
        ],
        "exp_en": "K.C. Pant chaired the Tenth Finance Commission (1995-2000). He recommended the historic Alternative Scheme of Devolution.",
        "exp_ta": "கே.சி. பந்த் 10வது நிதி ஆணையத்தின் (1995-2000) தலைவராகப் பணியாற்றினார்; அவர் வரலாற்று சிறப்புமிக்க மாற்று வரிப் பகிர்வு முறையைப் பரிந்துரைத்தார்.",
        "tip_en": "10th FC = K.C. Pant. Resulted in 80th Amendment Act 2000.",
        "tip_ta": "10வது நிதி ஆணையம் = கே.சி. பந்த். இதன் விளைவாக 80வது திருத்தச் சட்டம் 2000 உருவானது.",
        "fact_en": "K.C. Pant was a former Union Defence Minister and Deputy Chairman of Planning Commission.",
        "fact_ta": "கே.சி. பந்த் முன்னாள் மத்திய பாதுகாப்பு அமைச்சராகவும் திட்டக் குழுவின் துணைத் தலைவராகவும் பணியாற்றியவர்."
    },
    # 39
    {
        "subtopic": "Eleventh Finance Commission Chairman",
        "stem_en": "Who chaired the Eleventh Finance Commission of India (2000-2005)?",
        "stem_ta": "இந்தியாவின் 11வது நிதி ஆணையத்தின் (2000-2005) தலைவர் யார்?",
        "options": [
            ("Prof. A.M. Khusro", "பேராசிரியர் ஏ.எம். குஸ்ரோ"),
            ("Dr. C. Rangarajan", "டாக்டர் சி. ரங்கராஜன்"),
            ("B.P. Jeevan Reddy", "பி.பி. ஜீவன் ரெட்டி"),
            ("Raja Chelliah", "ராஜா செல்லையா")
        ],
        "exp_en": "Prof. A.M. Khusro, noted agricultural economist and diplomat, chaired the Eleventh Finance Commission (2000-2005).",
        "exp_ta": "புகழ்பெற்ற வேளாண் பொருளாதார நிபுணரும் தூதருமான பேராசிரியர் ஏ.எம். குஸ்ரோ 11வது நிதி ஆணையத்தின் (2000-2005) தலைவராகப் பணியாற்றினார்.",
        "tip_en": "11th FC = A.M. Khusro. First commission to formally operationalize grants to Panchayats and Municipalities under 280(3)(bb)/(c).",
        "tip_ta": "11வது நிதி ஆணையம் = ஏ.எம். குஸ்ரோ. 280(3)(bb)/(c)-ன் கீழ் உள்ளாட்சி அமைப்புகளுக்கு முதன்முதலில் முறையான மானியங்களை வழங்கியவர்.",
        "fact_en": "The 11th FC recommended a total local body grant of Rs. 10,000 crore.",
        "fact_ta": "11வது நிதி ஆணையம் உள்ளாட்சி அமைப்புகளுக்கு மொத்தம் ரூ. 10,000 கோடி மானியத்தை பரிந்துரைத்தது."
    },
    # 40
    {
        "subtopic": "Article 280 Location in Constitution",
        "stem_en": "In which Part and Chapter of the Constitution of India is Article 280 placed?",
        "stem_ta": "இந்திய அரசியலமைப்பின் எந்தப் பகுதி மற்றும் அத்தியாயத்தில் சரத்து 280 அமைந்துள்ளது?",
        "options": [
            ("Part XII, Chapter I (Finance)", "பகுதி XII, அத்தியாயம் I (நிதி)"),
            ("Part XI, Chapter II (Administrative Relations)", "பகுதி XI, அத்தியாயம் II (நிர்வாக உறவுகள்)"),
            ("Part XII, Chapter II (Borrowing)", "பகுதி XII, அத்தியாயம் II (கடன் வாங்குதல்)"),
            ("Part XIV, Chapter I (Services)", "பகுதி XIV, அத்தியாயம் I (பணிகள்)")
        ],
        "exp_en": "Article 280 is situated in Part XII ('Finance, Property, Contracts and Suits'), Chapter I ('Finance') of the Constitution.",
        "exp_ta": "சரத்து 280 அரசியலமைப்பின் பகுதி XII ('நிதி, சொத்து, ஒப்பந்தங்கள் மற்றும் வழக்குகள்'), அத்தியாயம் I ('நிதி') இல் அமைந்துள்ளது.",
        "tip_en": "Part XII covers financial relations between the Union and States (Articles 264 to 300A).",
        "tip_ta": "பகுதி XII மத்திய மற்றும் மாநில அரசுகளுக்கு இடையேயான நிதி உறவுகளைக் கையாள்கிறது (சரத்துகள் 264 முதல் 300A வரை).",
        "fact_en": "Chapter I of Part XII spans Articles 264 to 291.",
        "fact_ta": "பகுதி XII-ன் அத்தியாயம் I சரத்துகள் 264 முதல் 291 வரை பரவியுள்ளது."
    },
    # 41
    {
        "subtopic": "Second Finance Commission Chairman",
        "stem_en": "Who chaired the Second Finance Commission of India (1956)?",
        "stem_ta": "இந்தியாவின் இரண்டாவது நிதி ஆணையத்தின் (1956) தலைவர் யார்?",
        "options": [
            ("K. Santhanam", "கே. சந்தானம்"),
            ("A.K. Chanda", "ஏ.கே. சந்தா"),
            ("P.V. Rajamannar", "பி.வி. ராஜமன்னார்"),
            ("Mahavir Tyagi", "மகாவீர் தியாகி")
        ],
        "exp_en": "K. Santhanam, eminent freedom fighter, statesman, and Chairman of the Anti-Corruption Committee, chaired the Second Finance Commission (1956, covering 1957-1962).",
        "exp_ta": "சுதந்திரப் போராட்ட வீரரும் ஊழல் தடுப்புக் குழுவின் தலைவருமான கே. சந்தானம் இரண்டாவது நிதி ஆணையத்தின் (1956, பரிந்துரைக் காலம் 1957-1962) தலைவராகப் பணியாற்றினார்.",
        "tip_en": "2nd FC Chairman = K. Santhanam.",
        "tip_ta": "2வது நிதி ஆணையத் தலைவர் = கே. சந்தானம்.",
        "fact_en": "K. Santhanam famously noted the overlapping roles between the Finance Commission and the Planning Commission.",
        "fact_ta": "நிதி ஆணையம் மற்றும் திட்டக் குழுவின் பணிகள் ஒன்றோடொன்று மோதுவதை சந்தானம் சுட்டிக்காட்டினார்."
    },
    # 42
    {
        "subtopic": "Third Finance Commission Chairman",
        "stem_en": "Who was the Chairman of the Third Finance Commission of India (1960)?",
        "stem_ta": "இந்தியாவின் மூன்றாவது நிதி ஆணையத்தின் (1960) தலைவர் யார்?",
        "options": [
            ("A.K. Chanda", "ஏ.கே. சந்தா"),
            ("K.C. Neogy", "கே.சி. நியோகி"),
            ("P.V. Rajamannar", "பி.வி. ராஜமன்னார்"),
            ("K. Brahmananda Reddy", "கே. பிரம்மானந்த ரெட்டி")
        ],
        "exp_en": "A.K. Chanda, former Comptroller and Auditor General of India (1954-1960), served as the Chairman of the Third Finance Commission (1960, covering 1962-1966).",
        "exp_ta": "முன்னாள் இந்தியத் தலைமைக் கணக்குத் தணிக்கையாளரான (1954-1960) ஏ.கே. சந்தா மூன்றாவது நிதி ஆணையத்தின் (1960, பரிந்துரைக் காலம் 1962-1966) தலைவராகப் பணியாற்றினார்.",
        "tip_en": "3rd FC Chairman = A.K. Chanda (former CAG).",
        "tip_ta": "3வது நிதி ஆணையத் தலைவர் = ஏ.கே. சந்தா (முன்னாள் சி.ஏ.ஜி).",
        "fact_en": "A.K. Chanda recommended that the Planning Commission be transformed into the Finance Commission.",
        "fact_ta": "திட்டக் குழுவை நிதி ஆணையமாக மாற்ற வேண்டும் என ஏ.கே. சந்தா பரிந்துரைத்தார்."
    },
    # 43
    {
        "subtopic": "Fourth Finance Commission Chairman",
        "stem_en": "Who chaired the Fourth Finance Commission of India (1964)?",
        "stem_ta": "இந்தியாவின் நான்காவது நிதி ஆணையத்தின் (1964) தலைவர் யார்?",
        "options": [
            ("Dr. P.V. Rajamannar", "டாக்டர் பி.வி. ராஜமன்னார்"),
            ("Mahavir Tyagi", "மகாவீர் தியாகி"),
            ("J.M. Shelat", "ஜே.எம். ஷெலத்"),
            ("Y.B. Chavan", "ஒய்.பி. சவான்")
        ],
        "exp_en": "Dr. P.V. Rajamannar, former Chief Justice of Madras High Court, chaired the Fourth Finance Commission (1964, covering 1966-1969).",
        "exp_ta": "சென்னை உயர் நீதிமன்றத்தின் முன்னாள் தலைமை நீதிபதி டாக்டர் பி.வி. ராஜமன்னார் நான்காவது நிதி ஆணையத்தின் (1964, பரிந்துரைக் காலம் 1966-1969) தலைவராகப் பணியாற்றினார்.",
        "tip_en": "4th FC = Dr. P.V. Rajamannar (also headed the TN Centre-State Relations Inquiry Committee 1969).",
        "tip_ta": "4வது நிதி ஆணையம் = டாக்டர் பி.வி. ராஜமன்னார் (1969 தமிழ்நாடு மத்திய-மாநில உறவுகள் குழுவின் தலைவரும் இவரே).",
        "fact_en": "Dr. Rajamannar strongly argued for making Finance Commission recommendations permanent or binding.",
        "fact_ta": "நிதி ஆணையத்தின் பரிந்துரைகளை நிலையானதாக அல்லது கட்டாயமாக்க வேண்டும் என ராஜமன்னார் வலியுறுத்தினார்."
    },
    # 44
    {
        "subtopic": "Fifth Finance Commission Chairman",
        "stem_en": "Who served as the Chairman of the Fifth Finance Commission of India (1968)?",
        "stem_ta": "இந்தியாவின் ஐந்தாவது நிதி ஆணையத்தின் (1968) தலைவராகப் பணியாற்றியவர் யார்?",
        "options": [
            ("Mahavir Tyagi", "மகாவீர் தியாகி"),
            ("K. Brahmananda Reddy", "கே. பிரம்மானந்த ரெட்டி"),
            ("J.M. Shelat", "ஜே.எம். ஷெலத்"),
            ("N.K.P. Salve", "என்.கே.பி. சால்வே")
        ],
        "exp_en": "Mahavir Tyagi, prominent parliamentarian and freedom fighter, chaired the Fifth Finance Commission (1968, covering 1969-1974).",
        "exp_ta": "முக்கிய நாடாளுமன்றவாதியும் விடுதலைப் போராட்ட வீரருமான மகாவீர் தியாகி ஐந்தாவது நிதி ஆணையத்தின் (1968, பரிந்துரைக் காலம் 1969-1974) தலைவராகப் பணியாற்றினார்.",
        "tip_en": "5th FC Chairman = Mahavir Tyagi.",
        "tip_ta": "5வது நிதி ஆணையத் தலைவர் = மகாவீர் தியாகி.",
        "fact_en": "The 5th FC introduced the concept of assessing states' tax effort in determining grants-in-aid.",
        "fact_ta": "மானியங்களை நிர்ணயிப்பதில் மாநிலங்களின் வரி முயற்சியை மதிப்பிடும் கருத்தை 5வது நிதி ஆணையம் அறிமுகப்படுத்தியது."
    },
    # 45
    {
        "subtopic": "Sixth Finance Commission Chairman",
        "stem_en": "Who chaired the Sixth Finance Commission of India (1972)?",
        "stem_ta": "இந்தியாவின் ஆறாவது நிதி ஆணையத்தின் (1972) தலைவர் யார்?",
        "options": [
            ("K. Brahmananda Reddy", "கே. பிரம்மானந்த ரெட்டி"),
            ("J.M. Shelat", "ஜே.எம். ஷெலத்"),
            ("Y.B. Chavan", "ஒய்.பி. சவான்"),
            ("A.K. Chanda", "ஏ.கே. சந்தா")
        ],
        "exp_en": "K. Brahmananda Reddy, former Chief Minister of Andhra Pradesh and Union Home Minister, chaired the Sixth Finance Commission (1972, covering 1974-1979).",
        "exp_ta": "ஆந்திரப் பிரதேசத்தின் முன்னாள் முதலமைச்சரும் மத்திய உள்துறை அமைச்சருமான கே. பிரம்மானந்த ரெட்டி ஆறாவது நிதி ஆணையத்தின் (1972, பரிந்துரைக் காலம் 1974-1979) தலைவராகப் பணியாற்றினார்.",
        "tip_en": "6th FC Chairman = K. Brahmananda Reddy.",
        "tip_ta": "6வது நிதி ஆணையத் தலைவர் = கே. பிரம்மானந்த ரெட்டி.",
        "fact_en": "First commission to recommend non-plan capital grants for upgradation of standards of administration.",
        "fact_ta": "நிர்வாகத் தரத்தை மேம்படுத்துவதற்காக திட்டமில்லா மூலதன மானியங்களை பரிந்துரைத்த முதல் ஆணையம் இதுவாகும்."
    },
    # 46
    {
        "subtopic": "Seventh Finance Commission Chairman",
        "stem_en": "Who was the Chairman of the Seventh Finance Commission of India (1977)?",
        "stem_ta": "இந்தியாவின் ஏழாவது நிதி ஆணையத்தின் (1977) தலைவர் யார்?",
        "options": [
            ("Justice J.M. Shelat", "நீதிபதி ஜே.எம். ஷெலத்"),
            ("Justice H.R. Khanna", "நீதிபதி எச்.ஆர். கண்ணா"),
            ("Justice V.R. Krishna Iyer", "நீதிபதி வி.ஆர். கிருஷ்ண அய்யர்"),
            ("Justice P.N. Bhagwati", "நீதிபதி பி.என். பகவதி")
        ],
        "exp_en": "Justice J.M. Shelat, retired Judge of the Supreme Court of India, chaired the Seventh Finance Commission (1977, covering 1979-1984).",
        "exp_ta": "ஓய்வுபெற்ற உச்ச நீதிமன்ற நீதிபதி ஜே.எம். ஷெலத் ஏழாவது நிதி ஆணையத்தின் (1977, பரிந்துரைக் காலம் 1979-1984) தலைவராகப் பணியாற்றினார்.",
        "tip_en": "7th FC Chairman = Justice J.M. Shelat. Doubled the Union Excise Duty share to States from 20% to 40%.",
        "tip_ta": "7வது நிதி ஆணையத் தலைவர் = நீதிபதி ஜே.எம். ஷெலத். மத்திய கலால் வரிப் பகிர்வை 20%-லிருந்து 40%-ஆக இரட்டிப்பாக்கினார்.",
        "fact_en": "Justice Shelat was one of the dissenting judges who resigned after being superseded for Chief Justice of India in 1973.",
        "fact_ta": "1973-ல் தலைமை நீதிபதி நியமனத்தில் புறக்கணிக்கப்பட்டதால் பதவி விலகிய மூத்த நீதிபதிகளில் ஷெலத்தும் ஒருவர்."
    },
    # 47
    {
        "subtopic": "Eighth Finance Commission Chairman",
        "stem_en": "Who chaired the Eighth Finance Commission of India (1982)?",
        "stem_ta": "இந்தியாவின் எட்டாவது நிதி ஆணையத்தின் (1982) தலைவர் யார்?",
        "options": [
            ("Y.B. Chavan", "ஒய்.பி. சவான்"),
            ("N.K.P. Salve", "என்.கே.பி. சால்வே"),
            ("C. Subramaniam", "சி. சுப்பிரமணியம்"),
            ("Pranab Mukherjee", "பிரணாப் முகர்ஜி")
        ],
        "exp_en": "Y.B. Chavan, former Deputy Prime Minister and Union Finance Minister, chaired the Eighth Finance Commission (1982, covering 1984-1989).",
        "exp_ta": "முன்னாள் துணைப் பிரதமரும் மத்திய நிதி அமைச்சருமான ஒய்.பி. சவான் எட்டாவது நிதி ஆணையத்தின் (1982, பரிந்துரைக் காலம் 1984-1989) தலைவராகப் பணியாற்றினார்.",
        "tip_en": "8th FC Chairman = Y.B. Chavan.",
        "tip_ta": "8வது நிதி ஆணையத் தலைவர் = ஒய்.பி. சவான்.",
        "fact_en": "The 8th FC recommended sharing 85% of Income Tax and 45% of Union Excise Duties with the States.",
        "fact_ta": "8வது நிதி ஆணையம் வருமான வரியில் 85% மற்றும் கலால் வரியில் 45%-ஐ மாநிலங்களுக்குப் பகிர பரிந்துரைத்தது."
    },
    # 48
    {
        "subtopic": "Ninth Finance Commission Chairman",
        "stem_en": "Who was the Chairman of the Ninth Finance Commission of India (1987)?",
        "stem_ta": "இந்தியாவின் ஒன்பதாவது நிதி ஆணையத்தின் (1987) தலைவர் யார்?",
        "options": [
            ("N.K.P. Salve", "என்.கே.பி. சால்வே"),
            ("K.C. Pant", "கே.சி. பந்த்"),
            ("Madhavrao Scindia", "மாதவராவ் சிந்தியா"),
            ("V.P. Singh", "வி.பி. சிங்")
        ],
        "exp_en": "N.K.P. Salve, veteran parliamentarian and Union Minister, chaired the Ninth Finance Commission (1987, covering 1989-1995 across two reports).",
        "exp_ta": "மூத்த நாடாளுமன்றவாதியும் மத்திய அமைச்சருமான என்.கே.பி. சால்வே ஒன்பதாவது நிதி ஆணையத்தின் (1987, இரண்டு அறிக்கைகள் மூலம் 1989-1995 காலம்) தலைவராகப் பணியாற்றினார்.",
        "tip_en": "9th FC Chairman = N.K.P. Salve. Adopted normative approach to assess revenue and expenditure.",
        "tip_ta": "9வது நிதி ஆணையத் தலைவர் = என்.கே.பி. சால்வே. வருவாய் மற்றும் செலவினங்களை மதிப்பிட நெறிமுறை அணுகுமுறையைக் கையாண்டார்.",
        "fact_en": "The Ninth FC was the first to submit two separate reports for 1989-90 and 1990-95.",
        "fact_ta": "1989-90 மற்றும் 1990-95 என இரண்டு தனித்தனி அறிக்கைகளை சமர்ப்பித்த முதல் ஆணையம் 9வது நிதி ஆணையமாகும்."
    },
    # 49
    {
        "subtopic": "Term of Office of Members",
        "stem_en": "Under Section 6 of the Finance Commission Act 1951, what determines the term of office of a member of the Finance Commission?",
        "stem_ta": "1951 நிதி ஆணையச் சட்டத்தின் பிரிவு 6-ன் கீழ் நிதி ஆணைய உறுப்பினரின் பதவிக்காலத்தை தீர்மானிப்பது எது?",
        "options": [
            ("Specified in the order of the President appointing him and eligible for reappointment", "குடியரசுத் தலைவர் நியமன ஆணையில் குறிப்பிடும் காலம் வரை மற்றும் மறுநியமனத்திற்கு தகுதியுடையவர்"),
            ("Fixed by the Constitution strictly at 6 years or 65 years of age", "அரசியலமைப்பால் கண்டிப்பாக 6 ஆண்டுகள் அல்லது 65 வயது என நிர்ணயிக்கப்பட்டுள்ளது"),
            ("Co-terminus with the tenure of the Lok Sabha", "மக்களவையின் பதவிக்காலத்துடன் முடிவடையும்"),
            ("Until the pleasure of the Chief Justice of India", "இந்தியத் தலைமை நீதிபதியின் விருப்பம் உள்ளவரை")
        ],
        "exp_en": "Section 6 of the 1951 Act provides that every member of the Commission shall hold office for such period as may be specified in the order of the President appointing him, and shall be eligible for reappointment.",
        "exp_ta": "1951 சட்டத்தின் பிரிவு 6, ஆணையத்தின் ஒவ்வொரு உறுப்பினரும் அவரை நியமிக்கும் குடியரசுத் தலைவரின் ஆணையில் குறிப்பிடப்படும் காலம் வரை பதவியில் இருப்பார் என்றும் மறுநியமனத்திற்கு தகுதியுடையவர் என்றும் கூறுகிறது.",
        "tip_en": "Tenure is temporary and specified in the Presidential order (usually 2-3 years to complete the report).",
        "tip_ta": "பதவிக்காலம் தற்காலிகமானது மற்றும் குடியரசுத் தலைவரின் ஆணையில் குறிப்பிடப்படுகிறது (வழக்கமாக அறிக்கை முடியும் வரை 2-3 ஆண்டுகள்).",
        "fact_en": "Unlike CAG or EC, the Finance Commission is not a permanent standing commission; it dissolves once its report is accepted.",
        "fact_ta": "சி.ஏ.ஜி அல்லது தேர்தல் ஆணையம் போலன்றி, நிதி ஆணையம் நிரந்தர அமைப்பு அல்ல; அறிக்கை முடிந்ததும் கலைக்கப்படும்."
    },
    # 50
    {
        "subtopic": "Distinction between Article 275 and Article 282",
        "stem_en": "What is the primary constitutional difference between grants under Article 275 and grants under Article 282?",
        "stem_ta": "சரத்து 275 மற்றும் சரத்து 282 ஆகியவற்றின் கீழான மானியங்களுக்கு இடையிலான முதன்மை அரசியலமைப்பு வேறுபாடு என்ன?",
        "options": [
            ("Article 275 provides statutory grants recommended by the Finance Commission, while Article 282 provides discretionary grants by the Union executive", "சரத்து 275 நிதி ஆணையத்தால் பரிந்துரைக்கப்படும் சட்டப்பூர்வ மானியங்களை வழங்குகிறது; சரத்து 282 மத்திய நிர்வாகத்தின் விருப்ப மானியங்களை வழங்குகிறது"),
            ("Article 275 grants are repayable with interest; Article 282 grants are interest-free", "சரத்து 275 மானியங்கள் வட்டியுடன் திருப்பிச் செலுத்தப்பட வேண்டும்; சரத்து 282 வட்டியற்றவை"),
            ("Article 275 grants are paid from the Contingency Fund; Article 282 from Public Account", "சரத்து 275 அவசரகால நிதியிலிருந்தும்; சரத்து 282 பொதுக் கணக்கிலிருந்தும் வழங்கப்படுகிறது"),
            ("Article 275 applies only to Union Territories; Article 282 applies only to States", "சரத்து 275 ஒன்றியப் பிரதேசங்களுக்கு மட்டுமே பொருந்தும்; சரத்து 282 மாநிலங்களுக்கு மட்டுமே பொருந்தும்")
        ],
        "exp_en": "Article 275 provides for statutory grants-in-aid recommended by the constitutional Finance Commission and charged on the Consolidated Fund of India. Article 282 is a spending power permitting the Union to make discretionary grants for any public purpose (like Centrally Sponsored Schemes).",
        "exp_ta": "சரத்து 275 என்பது அரசியலமைப்பு நிதி ஆணையத்தால் பரிந்துரைக்கப்பட்டு இந்தியத் திரட்டப்பட்ட நிதியில் பொறுப்பாக்கப்படும் சட்டப்பூர்வ மானியமாகும். சரத்து 282 என்பது மத்திய அரசு பொது நோக்கங்களுக்காக (மத்திய திட்டங்கள்) விருப்பப்படி வழங்கும் மானியமாகும்.",
        "tip_en": "Article 275 = Constitutional/Statutory grants. Article 282 = Discretionary executive grants.",
        "tip_ta": "சரத்து 275 = அரசியலமைப்பு / சட்டப்பூர்வ மானியங்கள். சரத்து 282 = நிர்வாக விருப்ப மானியங்கள்.",
        "fact_en": "Critics argue excessive reliance on Article 282 undermines the constitutional primacy of the Finance Commission.",
        "fact_ta": "சரத்து 282-ஐ அதிகம் பயன்படுத்துவது நிதி ஆணையத்தின் அரசியலமைப்பு முதன்மையை பலவீனப்படுத்துகிறது என்ற விமர்சனம் உள்ளது."
    }
]

def build_questions():
    questions = []
    for idx, item in enumerate(raw_easy_data, start=1):
        qid = f"FC_E_{idx:03d}"
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
            diff="Easy",
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
            tags=["polity", "finance_commission", "easy", item["subtopic"].lower().replace(" ", "_")]
        )
        questions.append(q)
    return questions

if __name__ == "__main__":
    qs = build_questions()
    print(f"Generated {len(qs)} raw Easy questions for Finance Commission.")
    
    balanced_qs = balance_question_keys(qs)
    
    out_path = os.path.join("data", "questions", "polity", "fc_easy.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(balanced_qs, f, ensure_ascii=False, indent=2)
    print(f"Saved balanced Easy MCQs to {out_path}")
    
    val = ContentValidator()
    report = val.validate_file(out_path, expected_count=50, expected_prefix="FC_E_")
    print(f"Validation Report: {'PASS' if report.is_valid else 'FAIL'} | Total: {report.total_audited}")
    if not report.is_valid:
        for iss in report.issues[:10]:
            print(f"  Issue: {iss}")
    print(f"Key Distribution: {report.key_distribution}")
