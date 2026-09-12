# -*- coding: utf-8 -*-
"""
Generator for UPSC & State Public Service Commissions Easy MCQs (50 Questions: UPSC_E_001 to UPSC_E_050).
Strictly adheres to:
- Full 24-field TNPSC Nova AI schema
- Balanced answer keys (13 A, 13 B, 12 C, 12 D)
- Fully bilingual (English and authentic Tamil)
- Complete why_not_others dict with A, B, C, D in both languages
"""

import json
import os
from upsc_mcq_helper import make_upsc_q
from tools.nova_content_engine.answer_randomizer import randomize_and_balance_dataset, audit_answer_pattern
from tools.nova_content_engine.validator import ContentValidator

raw_easy_data = [
    # 1
    {
        "subtopic": "Constitutional Articles",
        "stem_en": "Which Article of the Constitution of India provides for the establishment of the Union Public Service Commission (UPSC) and State Public Service Commissions (SPSC)?",
        "stem_ta": "மத்திய அரசுப் பணியாளர் தேர்வாணையம் (UPSC) மற்றும் மாநில அரசுப் பணியாளர் தேர்வாணையங்களை (SPSC) அமைப்பதற்கு வகை செய்யும் இந்திய அரசியலமைப்புச் சரத்து எது?",
        "options": [
            ("Article 315", "சரத்து 315"),
            ("Article 324", "சரத்து 324"),
            ("Article 280", "சரத்து 280"),
            ("Article 148", "சரத்து 148")
        ],
        "exp_en": "Article 315 of the Constitution provides for a Public Service Commission for the Union and a Public Service Commission for each State.",
        "exp_ta": "இந்திய அரசியலமைப்பின் சரத்து 315, ஒன்றியத்திற்கு ஒரு அரசுப் பணியாளர் தேர்வாணையமும், ஒவ்வொரு மாநிலத்திற்கும் ஒரு அரசுப் பணியாளர் தேர்வாணையமும் இருக்க வேண்டும் என வகை செய்கிறது.",
        "tip_en": "Article 315: UPSC & SPSC; Article 324: Election Commission; Article 280: Finance Commission; Article 148: CAG.",
        "tip_ta": "சரத்து 315: UPSC & SPSC; சரத்து 324: தேர்தல் ஆணையம்; சரத்து 280: நிதி ஆணையம்; சரத்து 148: சி.ஏ.ஜி.",
        "fact_en": "Part XIV, Chapter II (Articles 315 to 323) of the Indian Constitution deals with the Public Service Commissions.",
        "fact_ta": "இந்திய அரசியலமைப்பின் பகுதி XIV, அத்தியாயம் II (சரத்துகள் 315 முதல் 323 வரை) அரசுப் பணியாளர் தேர்வாணையங்களைப் பற்றிக் கூறுகிறது."
    },
    # 2
    {
        "subtopic": "Appointment of UPSC Members",
        "stem_en": "Who appoints the Chairman and other members of the Union Public Service Commission (UPSC)?",
        "stem_ta": "மத்திய அரசுப் பணியாளர் தேர்வாணையத்தின் (UPSC) தலைவர் மற்றும் பிற உறுப்பினர்களை நியமிப்பவர் யார்?",
        "options": [
            ("The President of India", "இந்தியக் குடியரசுத் தலைவர்"),
            ("The Prime Minister of India", "இந்தியப் பிரதமர்"),
            ("The Chief Justice of India", "இந்தியத் தலைமை நீதிபதி"),
            ("A parliamentary committee headed by the Speaker", "சபாநாயகர் தலைமையிலான நாடாளுமன்றக் குழு")
        ],
        "exp_en": "Under Article 316(1) of the Constitution, the Chairman and other members of the UPSC are appointed by the President of India.",
        "exp_ta": "அரசியலமைப்பின் சரத்து 316(1)-ன் படி, UPSC-யின் தலைவர் மற்றும் பிற உறுப்பினர்கள் இந்தியக் குடியரசுத் தலைவரால் நியமிக்கப்படுகின்றனர்.",
        "tip_en": "UPSC and Joint PSC members are appointed by the President; SPSC members are appointed by the Governor.",
        "tip_ta": "UPSC மற்றும் இணைப் பணியாளர் தேர்வாணைய உறுப்பினர்களை குடியரசுத் தலைவரும், SPSC உறுப்பினர்களை ஆளுநரும் நியமிக்கின்றனர்.",
        "fact_en": "The Constitution does not specify the exact strength of the UPSC; it is left to the discretion of the President.",
        "fact_ta": "UPSC-யின் மொத்த உறுப்பினர் எண்ணிக்கையை அரசியலமைப்பு நிர்ணயிக்கவில்லை; அது குடியரசுத் தலைவரின் விருப்பத்திற்கே விடப்பட்டுள்ளது."
    },
    # 3
    {
        "subtopic": "Appointment of SPSC Members",
        "stem_en": "Who appoints the Chairman and members of a State Public Service Commission (SPSC)?",
        "stem_ta": "ஒரு மாநில அரசுப் பணியாளர் தேர்வாணையத்தின் (SPSC) தலைவர் மற்றும் உறுப்பினர்களை நியமிப்பவர் யார்?",
        "options": [
            ("The Governor of the concerned State", "சம்பந்தப்பட்ட மாநிலத்தின் ஆளுநர்"),
            ("The Chief Minister of the State", "மாநிலத்தின் முதலமைச்சர்"),
            ("The President of India", "இந்தியக் குடியரசுத் தலைவர்"),
            ("The Chief Justice of the High Court", "உயர் நீதிமன்றத் தலைமை நீதிபதி")
        ],
        "exp_en": "Under Article 316(1), the Chairman and other members of a State Public Service Commission are appointed by the Governor of the State.",
        "exp_ta": "சரத்து 316(1)-ன் படி, மாநில அரசுப் பணியாளர் தேர்வாணையத்தின் தலைவர் மற்றும் உறுப்பினர்கள் அந்தந்த மாநில ஆளுநரால் நியமிக்கப்படுகின்றனர்.",
        "tip_en": "SPSC members are appointed by the Governor, but they can be removed ONLY by the President!",
        "tip_ta": "SPSC உறுப்பினர்களை ஆளுநர் நியமித்தாலும், அவர்களை குடியரசுத் தலைவர் மட்டுமே பதவி நீக்கம் செய்ய முடியும்!",
        "fact_en": "Although appointed by the Governor, SPSC members enjoy constitutional security of tenure.",
        "fact_ta": "ஆளுநரால் நியமிக்கப்பட்டாலும், SPSC உறுப்பினர்களுக்கு அரசியலமைப்பு ரீதியான பணிப் பாதுகாப்பு உண்டு."
    },
    # 4
    {
        "subtopic": "Tenure of UPSC Members",
        "stem_en": "What is the term of office for the Chairman and members of the Union Public Service Commission?",
        "stem_ta": "மத்திய அரசுப் பணியாளர் தேர்வாணையத்தின் தலைவர் மற்றும் உறுப்பினர்களின் பதவிக்காலம் என்ன?",
        "options": [
            ("6 years or up to 65 years of age, whichever is earlier", "6 ஆண்டுகள் அல்லது 65 வயது நிறைவடையும் வரை, எது முந்தையதோ அது"),
            ("5 years or up to 65 years of age, whichever is earlier", "5 ஆண்டுகள் அல்லது 65 வயது நிறைவடையும் வரை, எது முந்தையதோ அது"),
            ("6 years or up to 62 years of age, whichever is earlier", "6 ஆண்டுகள் அல்லது 62 வயது நிறைவடையும் வரை, எது முந்தையதோ அது"),
            ("5 years or up to 60 years of age, whichever is earlier", "5 ஆண்டுகள் அல்லது 60 வயது நிறைவடையும் வரை, எது முந்தையதோ அது")
        ],
        "exp_en": "Under Article 316(2), members of the UPSC hold office for a term of 6 years or until they attain the age of 65 years, whichever is earlier.",
        "exp_ta": "சரத்து 316(2)-ன் படி, UPSC உறுப்பினர்கள் 6 ஆண்டுகள் அல்லது 65 வயது நிறைவடையும் வரை, எது முந்தையதோ அதுவரை பதவி வகிப்பர்.",
        "tip_en": "UPSC retirement age is 65 years; SPSC retirement age is 62 years. Both have a 6-year tenure.",
        "tip_ta": "UPSC ஓய்வு பெறும் வயது 65; SPSC ஓய்வு பெறும் வயது 62. இரண்டிற்கும் பதவிக்காலம் 6 ஆண்டுகள்.",
        "fact_en": "Members may resign at any time by addressing their resignation letter in writing to the President.",
        "fact_ta": "உறுப்பினர்கள் குடியரசுத் தலைவரிடம் எழுத்துப்பூர்வமாக கடிதம் அளித்து எப்போது வேண்டுமானாலும் பதவி விலகலாம்."
    },
    # 5
    {
        "subtopic": "Tenure of SPSC Members",
        "stem_en": "What is the term of office for the Chairman and members of a State Public Service Commission?",
        "stem_ta": "மாநில அரசுப் பணியாளர் தேர்வாணையத்தின் தலைவர் மற்றும் உறுப்பினர்களின் பதவிக்காலம் என்ன?",
        "options": [
            ("6 years or up to 62 years of age, whichever is earlier", "6 ஆண்டுகள் அல்லது 62 வயது நிறைவடையும் வரை, எது முந்தையதோ அது"),
            ("6 years or up to 65 years of age, whichever is earlier", "6 ஆண்டுகள் அல்லது 65 வயது நிறைவடையும் வரை, எது முந்தையதோ அது"),
            ("5 years or up to 62 years of age, whichever is earlier", "5 ஆண்டுகள் அல்லது 62 வயது நிறைவடையும் வரை, எது முந்தையதோ அது"),
            ("5 years or up to 60 years of age, whichever is earlier", "5 ஆண்டுகள் அல்லது 60 வயது நிறைவடையும் வரை, எது முந்தையதோ அது")
        ],
        "exp_en": "Under Article 316(2), members of an SPSC hold office for a term of 6 years or until they attain the age of 62 years, whichever is earlier.",
        "exp_ta": "சரத்து 316(2)-ன் படி, SPSC உறுப்பினர்கள் 6 ஆண்டுகள் அல்லது 62 வயது நிறைவடையும் வரை, எது முந்தையதோ அதுவரை பதவி வகிப்பர்.",
        "tip_en": "Retirement age of SPSC was raised from 60 to 62 years by the 41st Constitutional Amendment Act, 1976.",
        "tip_ta": "SPSC உறுப்பினர்களின் ஓய்வு வயது 60-லிருந்து 62 ஆக 1976-ம் ஆண்டின் 41-வது அரசியலமைப்புத் திருத்தச் சட்டத்தின் மூலம் உயர்த்தப்பட்டது.",
        "fact_en": "SPSC members address their resignation letter to the Governor of the State.",
        "fact_ta": "SPSC உறுப்பினர்கள் தங்களது பதவி விலகல் கடிதத்தை மாநில ஆளுநருக்கு முகவரியிட்டு அனுப்புகின்றனர்."
    },
    # 6
    {
        "subtopic": "Removal Authority for SPSC",
        "stem_en": "Who has the constitutional authority to remove the Chairman or any member of a State Public Service Commission?",
        "stem_ta": "மாநில அரசுப் பணியாளர் தேர்வாணையத்தின் தலைவர் அல்லது எந்தவொரு உறுப்பினரையும் பதவி நீக்கம் செய்யும் அரசியலமைப்பு அதிகாரம் யாருக்கு உள்ளது?",
        "options": [
            ("The President of India", "இந்தியக் குடியரசுத் தலைவர்"),
            ("The Governor of the State", "மாநில ஆளுநர்"),
            ("The Chief Minister of the State", "மாநில முதலமைச்சர்"),
            ("The State Legislative Assembly", "மாநில சட்டமன்றப் பேரவை")
        ],
        "exp_en": "Under Article 317(1), although the Chairman and members of an SPSC are appointed by the Governor, they can be removed from office ONLY by the President of India.",
        "exp_ta": "சரத்து 317(1)-ன் படி, SPSC தலைவர் மற்றும் உறுப்பினர்கள் ஆளுநரால் நியமிக்கப்பட்டாலும், அவர்களை இந்தியக் குடியரசுத் தலைவர் மட்டுமே பதவி நீக்கம் செய்ய முடியும்.",
        "tip_en": "Crucial distinction: Governor appoints SPSC members, but President alone can remove them.",
        "tip_ta": "முக்கிய வேறுபாடு: ஆளுநர் SPSC உறுப்பினர்களை நியமிக்கிறார், ஆனால் குடியரசுத் தலைவர் மட்டுமே நீக்க முடியும்.",
        "fact_en": "The Governor can only suspend an SPSC member pending an inquiry by the Supreme Court.",
        "fact_ta": "உச்ச நீதிமன்ற விசாரணை நிலுவையில் உள்ளபோது SPSC உறுப்பினரை தற்காலிகமாக இடைநீக்கம் (suspend) மட்டுமே ஆளுநரால் செய்ய முடியும்."
    },
    # 7
    {
        "subtopic": "Grounds for Removal",
        "stem_en": "On the ground of misbehaviour, the President can remove a UPSC member only after an inquiry and report by which authority?",
        "stem_ta": "தவறான நடத்தை என்ற அடிப்படையில், UPSC உறுப்பினரை குடியரசுத் தலைவர் பதவி நீக்கம் செய்வதற்கு முன் எந்த அமைப்பின் விசாரணை அறிக்கை தேவைப்படுகிறது?",
        "options": [
            ("The Supreme Court of India", "இந்திய உச்ச நீதிமன்றம்"),
            ("The Central Vigilance Commission", "மத்திய விழிப்புணர்வு ஆணையம்"),
            ("A Joint Parliamentary Committee", "கூட்டு நாடாளுமன்றக் குழு"),
            ("The Union Law Ministry", "மத்திய சட்ட அமைச்சகம்")
        ],
        "exp_en": "Under Article 317(1), a member can be removed for misbehaviour only after the President refers the matter to the Supreme Court, which conducts an inquiry under Article 145 and reports its findings.",
        "exp_ta": "சரத்து 317(1)-ன் படி, தவறான நடத்தைக்காக நீக்குவதற்கு முன் குடியரசுத் தலைவர் விவகாரத்தை உச்ச நீதிமன்றத்திற்கு அனுப்ப வேண்டும்; சரத்து 145-ன் கீழ் உச்ச நீதிமன்றம் விசாரித்து அறிக்கை அளிக்கிறது.",
        "tip_en": "The advice tendered by the Supreme Court on an inquiry under Article 317 is BINDING on the President.",
        "tip_ta": "சரத்து 317-ன் கீழ் உச்ச நீதிமன்றம் அளிக்கும் விசாரணைப் பரிந்துரையை குடியரசுத் தலைவர் கட்டாயமாக ஏற்க வேண்டும் (கட்டுப்படுத்தும்).",
        "fact_en": "Pending the Supreme Court's inquiry report, the President (for UPSC) or the Governor (for SPSC) may suspend the member.",
        "fact_ta": "உச்ச நீதிமன்ற அறிக்கை வரும் வரை குடியரசுத் தலைவர் (UPSC) அல்லது ஆளுநர் (SPSC) சம்பந்தப்பட்ட உறுப்பினரை இடைநீக்கம் செய்யலாம்."
    },
    # 8
    {
        "subtopic": "Qualifications of Members",
        "stem_en": "What constitutional qualification is prescribed for at least one-half of the members of the UPSC and SPSC?",
        "stem_ta": "UPSC மற்றும் SPSC-யின் உறுப்பினர்களில் குறைந்தது பாதி பேருக்கு அரசியலமைப்பில் பரிந்துரைக்கப்பட்டுள்ள தகுதி என்ன?",
        "options": [
            ("Must have held office for at least 10 years under Government of India or State Government", "மத்திய அல்லது மாநில அரசின் கீழ் குறைந்தது 10 ஆண்டுகள் அரசுப் பதவி வகித்திருக்க வேண்டும்"),
            ("Must be an advocate of the Supreme Court for at least 10 years", "உச்ச நீதிமன்றத்தில் குறைந்தது 10 ஆண்டுகள் வழக்கறிஞராகப் பணியாற்றியிருக்க வேண்டும்"),
            ("Must have served as a Vice-Chancellor of a recognized university", "அங்கீகரிக்கப்பட்ட பல்கலைக்கழகத்தின் துணைவேந்தராகப் பணியாற்றியிருக்க வேண்டும்"),
            ("Must be an Indian Administrative Service officer with 15 years experience", "15 ஆண்டுகள் அனுபவமுள்ள இந்திய ஆட்சிப் பணி (IAS) அதிகாரியாக இருக்க வேண்டும்")
        ],
        "exp_en": "Under the proviso to Article 316(1), as nearly as may be one-half of the members of every Public Service Commission must be persons who have held office for at least 10 years under the Government of India or a State Government.",
        "exp_ta": "சரத்து 316(1)-ன் நிபந்தனைப்படி, தேர்வாணைய உறுப்பினர்களில் ஏறத்தாழ பாதி பேர் மத்திய அல்லது மாநில அரசின் கீழ் குறைந்தது 10 ஆண்டுகள் பணிபுரிந்தவர்களாக இருக்க வேண்டும்.",
        "tip_en": "No other qualifications (educational, administrative) are specifically prescribed in the Constitution!",
        "tip_ta": "அரசியலமைப்பில் வேறு எந்தக் குறிப்பிட்ட கல்வி அல்லது நிர்வாகத் தகுதிகளும் நிர்ணயிக்கப்படவில்லை!",
        "fact_en": "The remaining half are appointed from various non-official backgrounds, academia, sciences, etc.",
        "fact_ta": "மீதமுள்ள பாதி உறுப்பினர்கள் கல்வி, அறிவியல் உள்ளிட்ட பல்வேறு அரசு சாரா துறைகளிலிருந்து நியமிக்கப்படுகின்றனர்."
    },
    # 9
    {
        "subtopic": "Re-appointment Prohibition",
        "stem_en": "Under Article 316(3), is a person who holds office as a member of a Public Service Commission eligible for re-appointment to that office?",
        "stem_ta": "சரத்து 316(3)-ன் கீழ், ஒரு அரசுப் பணியாளர் தேர்வாணையத்தின் உறுப்பினராகப் பதவி வகித்த ஒருவர் அதே பதவிக்கு மீண்டும் நியமிக்கப்பட தகுதியானவரா?",
        "options": [
            ("No, completely ineligible for re-appointment to that same office", "இல்லை, அதே பதவிக்கு மீண்டும் நியமிக்கப்பட முற்றிலும் தகுதியற்றவர்"),
            ("Yes, eligible for one additional consecutive term", "ஆம், தொடர்ந்து ஒரு கூடுதல் தவணைக்கு நியமிக்கப்படலாம்"),
            ("Yes, eligible after a cooling-off period of three years", "ஆம், மூன்று ஆண்டுகள் இடைவெளிக்குப் பின் நியமிக்கப்படலாம்"),
            ("Yes, subject to approval by a two-thirds majority in Parliament", "ஆம், நாடாளுமன்றத்தில் மூன்றில் இரண்டு பங்கு பெரும்பான்மை ஒப்புதலுடன் நியமிக்கப்படலாம்")
        ],
        "exp_en": "Article 316(3) explicitly provides that a person who holds office as a member of a Public Service Commission is, on the expiration of his term of office, ineligible for re-appointment to that office.",
        "exp_ta": "சரத்து 316(3) தெளிவாகக் குறிப்பிடுவது: அரசுப் பணியாளர் தேர்வாணைய உறுப்பினராகப் பதவி வகித்த ஒருவர், தனது பதவிக்காலம் முடிந்தவுடன் மீண்டும் அதே பதவிக்கு நியமிக்கப்பட தகுதியற்றவர் ஆவார்.",
        "tip_en": "Article 316(3) bars re-appointment to the SAME office, to preserve independence and prevent executive favouritism.",
        "tip_ta": "சுயாதீனத்தைப் பாதுகாக்கவும், நிர்வாகச் சார்புநிலையைத் தவிர்க்கவும் சரத்து 316(3) அதே பதவிக்கு மறுநியமனம் செய்வதைத் தடை செய்கிறது.",
        "fact_en": "However, a member can be appointed as Chairman of the same or another PSC under Article 319.",
        "fact_ta": "இருப்பினும், சரத்து 319-ன் கீழ் ஒரு உறுப்பினர் அதே தேர்வாணையத்தின் தலைவராகவோ அல்லது மற்றொரு தேர்வாணையத்தின் தலைவராகவோ நியமிக்கப்படலாம்."
    },
    # 10
    {
        "subtopic": "Post-Retirement Bar for UPSC Chairman",
        "stem_en": "What restriction applies to the Chairman of the Union Public Service Commission on ceasing to hold office under Article 319(a)?",
        "stem_ta": "சரத்து 319(a)-ன் படி, UPSC தலைவர் தனது பதவிக்காலம் முடிந்த பிறகு எந்தக் கட்டுப்பாட்டிற்கு உட்படுகிறார்?",
        "options": [
            ("Ineligible for any further employment under the Government of India or the Government of a State", "மத்திய அரசு அல்லது மாநில அரசின் கீழ் எவ்வித கூடுதல் வேலைவாய்ப்பையும் பெற தகுதியற்றவர்"),
            ("Eligible to be appointed as the Governor of a State", "ஒரு மாநிலத்தின் ஆளுநராக நியமிக்கப்பட தகுதியுடையவர்"),
            ("Eligible to be appointed as the Chairman of a State PSC", "ஒரு மாநில தேர்வாணையத்தின் தலைவராக நியமிக்கப்பட தகுதியுடையவர்"),
            ("Eligible for appointment to any international tribunal", "எந்தவொரு சர்வதேச தீர்ப்பாயத்திலும் நியமிக்கப்பட தகுதியுடையவர்")
        ],
        "exp_en": "Article 319(a) states that the Chairman of the UPSC is ineligible for further employment either under the Government of India or under the Government of a State.",
        "exp_ta": "சரத்து 319(a)-ன் படி, UPSC-யின் தலைவர் பதவிக்காலம் முடிந்த பிறகு, மத்திய அரசின்கீழோ அல்லது மாநில அரசின்கீழோ வேறு எந்த வேலைவாய்ப்பையும் பெற முற்றிலும் தகுதியற்றவர் ஆவார்.",
        "tip_en": "Both CAG (Art 148(4)) and UPSC Chairman (Art 319(a)) face absolute post-retirement employment bars under Union and State govts.",
        "tip_ta": "CAG (சரத்து 148(4)) மற்றும் UPSC தலைவர் (சரத்து 319(a)) ஆகிய இருவருமே ஓய்வுக்குப் பின் மத்திய, மாநில அரசுப் பணிகளை ஏற்க முழுமையான தடை உண்டு.",
        "fact_en": "This absolute bar ensures that the Chairman performs duties without expecting post-retirement executive rewards.",
        "fact_ta": "பணி ஓய்வுக்குப் பின் அரசுப் பதவிகளை எதிர்பார்த்துச் செயல்படுவதைத் தடுக்கவே இந்த முழுமையான தடை விதிக்கப்பட்டுள்ளது."
    },
    # 11
    {
        "subtopic": "Expenses Charged",
        "stem_en": "On which fund are the administrative expenses, salaries, and pensions of the UPSC charged under Article 322?",
        "stem_ta": "சரத்து 322-ன் கீழ், UPSC-யின் நிர்வாகச் செலவுகள், ஊதியங்கள் மற்றும் ஓய்வூதியங்கள் எந்த நிதியிலிருந்து பெறப்படுகின்றன?",
        "options": [
            ("Charged on the Consolidated Fund of India (non-votable)", "இந்தியத் தொகுப்பு நிதியில் சுமத்தப்படுகிறது (வாக்கெடுப்பிற்கு உட்படாதது)"),
            ("Voted annually by the Lok Sabha as part of the General Budget", "பொது பட்ஜெட்டின் பகுதியாக மக்களவையால் ஆண்டுதோறும் வாக்கெடுப்பு மூலம் ஒதுக்கப்படுகிறது"),
            ("Drawn from the Contingency Fund of India", "இந்திய அவசரகால நிதியிலிருந்து பெறப்படுகிறது"),
            ("Funded through application fees collected from candidates", "தேர்வர்களிடமிருந்து பெறப்படும் விண்ணப்பக் கட்டணம் மூலம் நிர்வகிக்கப்படுகிறது")
        ],
        "exp_en": "Under Article 322, the administrative expenses of the UPSC, including salaries, allowances, and pensions of members and staff, are charged upon the Consolidated Fund of India and are not subject to parliamentary vote.",
        "exp_ta": "சரத்து 322-ன் படி, UPSC-யின் ஊதியங்கள், படிகள் மற்றும் ஓய்வூதியங்கள் உள்ளிட்ட நிர்வாகச் செலவுகள் அனைத்தும் இந்தியத் தொகுப்பு நிதியில் சுமத்தப்பட்ட செலவுகளாகும்; அவை நாடாளுமன்ற வாக்கெடுப்பிற்கு உட்படாதவை.",
        "tip_en": "Expenses charged on the Consolidated Fund cannot be voted upon, ensuring institutional financial independence.",
        "tip_ta": "தொகுப்பு நிதியில் சுமத்தப்படும் செலவுகள் வாக்கெடுப்பிற்கு உட்படுத்தப்பட மாட்டாது, இது நிதி ரீதியான தன்னாட்சியை உறுதி செய்கிறது.",
        "fact_en": "Similarly, the expenses of an SPSC are charged on the Consolidated Fund of the State.",
        "fact_ta": "அதேபோன்று, SPSC-யின் அனைத்துச் செலவுகளும் சம்பந்தப்பட்ட மாநிலத் தொகுப்பு நிதியில் சுமத்தப்படுகின்றன."
    },
    # 12
    {
        "subtopic": "Annual Report of UPSC",
        "stem_en": "To whom does the UPSC present its annual report on its performance under Article 323(1)?",
        "stem_ta": "சரத்து 323(1)-ன் கீழ், தனது செயல்பாடுகள் குறித்த வருடாந்திர அறிக்கையை UPSC யாரிடம் சமர்ப்பிக்கிறது?",
        "options": [
            ("The President of India", "இந்தியக் குடியரசுத் தலைவர்"),
            ("The Prime Minister of India", "இந்தியப் பிரதமர்"),
            ("The Speaker of the Lok Sabha", "மக்களவை சபாநாயகர்"),
            ("The Minister of Personnel, Public Grievances and Pensions", "பணியாளர், பொதுமக்கள் குறைதீர்ப்பு மற்றும் ஓய்வூதியத் துறை அமைச்சர்")
        ],
        "exp_en": "Under Article 323(1), it is the duty of the UPSC to present annually to the President a report as to the work done by the Commission.",
        "exp_ta": "சரத்து 323(1)-ன் படி, தேர்வாணையம் ஆற்றிய பணிகள் குறித்த வருடாந்திர அறிக்கையை இந்தியக் குடியரசுத் தலைவரிடம் சமர்ப்பிப்பது UPSC-யின் கடமையாகும்.",
        "tip_en": "The President causes the report to be laid before each House of Parliament, along with an explanatory memorandum.",
        "tip_ta": "குடியரசுத் தலைவர் அந்த அறிக்கையை விளக்கக் குறிப்புடன் நாடாளுமன்றத்தின் இரு அவைகளிலும் வைக்கச் செய்கிறார்.",
        "fact_en": "If any advice of the UPSC was not accepted by the Government, reasons must be explained in the memorandum.",
        "fact_ta": "UPSC-யின் பரிந்துரையை அரசு ஏற்கவில்லை என்றால், அதற்கான காரணங்கள் விளக்கக் குறிப்பில் தெரிவிக்கப்பட வேண்டும்."
    },
    # 13
    {
        "subtopic": "Annual Report of SPSC",
        "stem_en": "Under Article 323(2), to whom does a State Public Service Commission present its annual report?",
        "stem_ta": "சரத்து 323(2)-ன் கீழ், ஒரு மாநில அரசுப் பணியாளர் தேர்வாணையம் தனது வருடாந்திர அறிக்கையை யாரிடம் சமர்ப்பிக்கிறது?",
        "options": [
            ("The Governor of the State", "மாநில ஆளுநர்"),
            ("The Chief Minister of the State", "மாநில முதலமைச்சர்"),
            ("The Speaker of the Legislative Assembly", "சட்டமன்றப் பேரவை சபாநாயகர்"),
            ("The President of India", "இந்தியக் குடியரசுத் தலைவர்")
        ],
        "exp_en": "Under Article 323(2), the State Public Service Commission presents its annual report to the Governor of the State.",
        "exp_ta": "சரத்து 323(2)-ன் படி, மாநில அரசுப் பணியாளர் தேர்வாணையம் தனது வருடாந்திர அறிக்கையை மாநில ஆளுநரிடம் சமர்ப்பிக்கிறது.",
        "tip_en": "The Governor causes the report to be laid before the State Legislature along with an explanatory memorandum.",
        "tip_ta": "ஆளுநர் இந்த அறிக்கையை விளக்கக் குறிப்புடன் மாநில சட்டமன்றத்தில் சமர்ப்பிக்கச் செய்கிறார்.",
        "fact_en": "Non-acceptance of SPSC advice must be approved by the State Appointments Committee / Cabinet.",
        "fact_ta": "SPSC பரிந்துரையை நிராகரிப்பது மாநில அமைச்சரவையின் ஒப்புதலுடன் மட்டுமே சாத்தியமாகும்."
    },
    # 14
    {
        "subtopic": "Joint State Public Service Commission Creation",
        "stem_en": "How can a Joint State Public Service Commission (JSPSC) be established for two or more States under Article 315(2)?",
        "stem_ta": "சரத்து 315(2)-ன் படி, இரண்டு அல்லது அதற்கு மேற்பட்ட மாநிலங்களுக்கு ஒரு கூட்டு மாநில அரசுப் பணியாளர் தேர்வாணையத்தை (JSPSC) எவ்வாறு உருவாக்க முடியும்?",
        "options": [
            ("By an Act of Parliament following resolutions passed by the concerned State Legislatures", "சம்பந்தப்பட்ட மாநில சட்டமன்றங்கள் தீர்மானம் நிறைவேற்றியதைத் தொடர்ந்து நாடாளுமன்றச் சட்டத்தின் மூலம்"),
            ("By an executive order of the President of India", "இந்தியக் குடியரசுத் தலைவரின் நிர்வாக ஆணை மூலம்"),
            ("By an agreement between the Governors of the concerned States", "சம்பந்தப்பட்ட மாநில ஆளுநர்களுக்கு இடையேயான ஒப்பந்தம் மூலம்"),
            ("By an order of the Supreme Court of India", "இந்திய உச்ச நீதிமன்றத்தின் உத்தரவு மூலம்")
        ],
        "exp_en": "Under Article 315(2), if the Legislatures of two or more States pass resolutions to that effect, Parliament may by law provide for the appointment of a Joint State Public Service Commission (JSPSC).",
        "exp_ta": "சரத்து 315(2)-ன் படி, இரண்டு அல்லது அதற்கு மேற்பட்ட மாநில சட்டமன்றங்கள் தீர்மானம் நிறைவேற்றினால், நாடாளுமன்றம் ஒரு சட்டத்தின் மூலம் கூட்டு மாநில அரசுப் பணியாளர் தேர்வாணையத்தை அமைக்கலாம்.",
        "tip_en": "A JSPSC is a STATUTORY body created by Parliament, not a constitutional body directly created by the Constitution!",
        "tip_ta": "JSPSC என்பது நாடாளுமன்றச் சட்டத்தால் உருவாக்கப்பட்ட ஒரு சட்டப்பூர்வ அமைப்பாகும் (Statutory Body), அரசியலமைப்பு அமைப்பல்ல!",
        "fact_en": "Punjab and Haryana had a Joint PSC for a short period after the bifurcation of Punjab in 1966.",
        "fact_ta": "1966-ல் பஞ்சாப் பிரிக்கப்பட்ட பிறகு, பஞ்சாப் மற்றும் அரியானா மாநிலங்களுக்கு ஒரு குறுகிய காலத்திற்கு கூட்டுத் தேர்வாணையம் இருந்தது."
    },
    # 15
    {
        "subtopic": "Appointment of JSPSC Members",
        "stem_en": "Who appoints the Chairman and members of a Joint State Public Service Commission (JSPSC)?",
        "stem_ta": "கூட்டு மாநில அரசுப் பணியாளர் தேர்வாணையத்தின் (JSPSC) தலைவர் மற்றும் உறுப்பினர்களை நியமிப்பவர் யார்?",
        "options": [
            ("The President of India", "இந்தியக் குடியரசுத் தலைவர்"),
            ("The Governors of the concerned States jointly", "சம்பந்தப்பட்ட மாநிலங்களின் ஆளுநர்கள் கூட்டாக"),
            ("The Chief Ministers of the concerned States by rotation", "சுழற்சி முறையில் சம்பந்தப்பட்ட மாநிலங்களின் முதலமைச்சர்கள்"),
            ("The Chief Justice of the Common High Court", "பொது உயர் நீதிமன்றத்தின் தலைமை நீதிபதி")
        ],
        "exp_en": "Under Article 316(1), the Chairman and other members of a Joint Commission are appointed by the President of India.",
        "exp_ta": "சரத்து 316(1)-ன் படி, கூட்டுத் தேர்வாணையத்தின் (JSPSC) தலைவர் மற்றும் உறுப்பினர்களை இந்தியக் குடியரசுத் தலைவர் நியமிக்கிறார்.",
        "tip_en": "JSPSC members are appointed and removed by the President, even though it serves States.",
        "tip_ta": "மாநிலங்களுக்குப் பணியாற்றினாலும், JSPSC உறுப்பினர்களை குடியரசுத் தலைவரே நியமிக்கவும் நீக்கவும் செய்கிறார்.",
        "fact_en": "Tenure of JSPSC members is 6 years or 62 years of age, whichever is earlier (same as SPSC).",
        "fact_ta": "JSPSC உறுப்பினர்களின் பதவிக்காலம் 6 ஆண்டுகள் அல்லது 62 வயது, எது முந்தையதோ அதுவாகும் (SPSC போன்றே)."
    },
    # 16
    {
        "subtopic": "Historical Evolution - Lee Commission",
        "stem_en": "Which British Commission in 1923-24 recommended the immediate establishment of a Public Service Commission in India?",
        "stem_ta": "1923-24 ஆம் ஆண்டில் இந்தியாவில் உடனடியாக ஒரு அரசுப் பணியாளர் தேர்வாணையத்தை அமைக்கப் பரிந்துரைத்த பிரிட்டிஷ் ஆணையம் எது?",
        "options": [
            ("Lee Commission (Royal Commission on Superior Civil Services)", "லீ ஆணையம் (உயர் குடிமைப் பணிகளுக்கான ராயல் கமிஷன்)"),
            ("Simon Commission", "சைமன் கமிஷன்"),
            ("Hunter Commission", "ஹண்டர் கமிஷன்"),
            ("Macaulay Committee", "மெக்காலே குழு")
        ],
        "exp_en": "The Royal Commission on Superior Civil Services in India (Lee Commission, 1923-24), chaired by Lord Lee of Fareham, recommended the immediate establishment of a Public Service Commission.",
        "exp_ta": "லார்ட் லீ தலைமையிலான இந்திய உயர் குடிமைப் பணிகளுக்கான ராயல் கமிஷன் (லீ ஆணையம், 1923-24), தாமதமின்றி உடனடியாக அரசுப் பணியாளர் தேர்வாணையம் அமைக்கப்பட வேண்டும் என்று பரிந்துரைத்தது.",
        "tip_en": "Lee Commission (1923-24) led to the setting up of the Central Public Service Commission in 1926.",
        "tip_ta": "லீ ஆணையத்தின் (1923-24) பரிந்துரையின்படி 1926-ல் மத்திய அரசுப் பணியாளர் தேர்வாணையம் அமைக்கப்பட்டது.",
        "fact_en": "Section 96C of the Government of India Act 1919 had originally provided for such a Commission.",
        "fact_ta": "1919-ம் ஆண்டின் இந்திய அரசுச் சட்டத்தின் பிரிவு 96C முதன்முதலில் இத்தகைய தேர்வாணையத்திற்கு வகை செய்திருந்தது."
    },
    # 17
    {
        "subtopic": "First Central PSC Setup",
        "stem_en": "In which year was the Central Public Service Commission established in India for the first time?",
        "stem_ta": "இந்தியாவில் முதன்முதலில் மத்திய அரசுப் பணியாளர் தேர்வாணையம் எந்த ஆண்டு நிறுவப்பட்டது?",
        "options": [
            ("1926 (October 1)", "1926 (அக்டோபர் 1)"),
            ("1919 (December 23)", "1919 (டிசம்பர் 23)"),
            ("1935 (August 2)", "1935 (ஆகஸ்ட் 2)"),
            ("1950 (January 26)", "1950 (ஜனவரி 26)")
        ],
        "exp_en": "The Central Public Service Commission was set up on October 1, 1926, pursuant to the recommendations of the Lee Commission.",
        "exp_ta": "லீ ஆணையத்தின் பரிந்துரைகளைத் தொடர்ந்து, 1926 அக்டோபர் 1 அன்று மத்திய அரசுப் பணியாளர் தேர்வாணையம் அமைக்கப்பட்டது.",
        "tip_en": "Setup: October 1, 1926. First Chairman was Sir Ross Barker.",
        "tip_ta": "தொடக்கம்: அக்டோபர் 1, 1926. இதன் முதல் தலைவர் சர் ராஸ் பார்கர் ஆவார்.",
        "fact_en": "Sir Ross Barker was a senior member of the British Home Civil Service.",
        "fact_ta": "சர் ராஸ் பார்கர் பிரிட்டிஷ் உள்நாட்டு குடிமைப் பணியின் மூத்த அதிகாரி ஆவார்."
    },
    # 18
    {
        "subtopic": "First Chairman of Central PSC",
        "stem_en": "Who was the first Chairman of the Central Public Service Commission established in 1926?",
        "stem_ta": "1926-ல் நிறுவப்பட்ட மத்திய அரசுப் பணியாளர் தேர்வாணையத்தின் முதல் தலைவர் யார்?",
        "options": [
            ("Sir Ross Barker", "சர் ராஸ் பார்கர்"),
            ("Sir David Petrie", "சர் டேவிட் பெட்ரி"),
            ("Sir Eyre Gordon", "சர் அயர் கார்டன்"),
            ("H.K. Kripalani", "எச்.கே. கிருபளானி")
        ],
        "exp_en": "Sir Ross Barker was appointed as the first Chairman of the Central Public Service Commission in October 1926.",
        "exp_ta": "1926 அக்டோபரில் மத்திய அரசுப் பணியாளர் தேர்வாணையத்தின் முதல் தலைவராக சர் ராஸ் பார்கர் நியமிக்கப்பட்டார்.",
        "tip_en": "First Chairman: Sir Ross Barker (1926). First Indian Chairman after Independence: H.K. Kripalani (1949).",
        "tip_ta": "முதல் தலைவர்: சர் ராஸ் பார்கர் (1926). சுதந்திரத்திற்குப் பின் முதல் இந்தியத் தலைவர்: எச்.கே. கிருபளானி (1949).",
        "fact_en": "The Commission initially consisted of four members in addition to the Chairman.",
        "fact_ta": "தொடக்கத்தில் இத்தேர்வாணையத்தில் தலைவர் தவிர நான்கு உறுப்பினர்கள் இருந்தனர்."
    },
    # 19
    {
        "subtopic": "First Indian Chairman of UPSC",
        "stem_en": "Who was the first Indian to become the Chairman of the Union Public Service Commission?",
        "stem_ta": "மத்திய அரசுப் பணியாளர் தேர்வாணையத்தின் (UPSC) தலைவரான முதல் இந்தியர் யார்?",
        "options": [
            ("H.K. Kripalani", "எச்.கே. கிருபளானி"),
            ("R.N. Banerjee", "ஆர்.என். பானர்ஜி"),
            ("Dr. A. Lakshmanaswami Mudaliar", "டாக்டர் ஏ. லட்சுமணசுவாமி முதலியார்"),
            ("V.V. Giri", "வி.வி. கிரி")
        ],
        "exp_en": "H.K. Kripalani was the first Indian Chairman of the Union Public Service Commission, serving from 1949 to 1955.",
        "exp_ta": "எச்.கே. கிருபளானி UPSC-யின் முதல் இந்தியத் தலைவராக 1949 முதல் 1955 வரை பணியாற்றினார்.",
        "tip_en": "H.K. Kripalani presided over the transition from Federal PSC to UPSC on 26 January 1950.",
        "tip_ta": "1950 ஜனவரி 26 அன்று கூட்டாட்சித் தேர்வாணையம் UPSC ஆக மாறியபோது எச்.கே. கிருபளானி தலைவராக இருந்தார்.",
        "fact_en": "Before 1949, all Chairmen of the Central and Federal Public Service Commissions were British.",
        "fact_ta": "1949-க்கு முன்பு மத்திய மற்றும் கூட்டாட்சித் தேர்வாணையங்களின் அனைத்துத் தலைவர்களும் பிரிட்டிஷாராகவே இருந்தனர்."
    },
    # 20
    {
        "subtopic": "Government of India Act 1935",
        "stem_en": "Under the Government of India Act 1935, the Central Public Service Commission was renamed as what?",
        "stem_ta": "1935-ம் ஆண்டின் இந்திய அரசுச் சட்டத்தின் கீழ், மத்திய அரசுப் பணியாளர் தேர்வாணையம் எவ்வாறு பெயர் மாற்றம் செய்யப்பட்டது?",
        "options": [
            ("Federal Public Service Commission", "கூட்டாட்சி அரசுப் பணியாளர் தேர்வாணையம் (Federal PSC)"),
            ("Union Public Service Commission", "மத்திய அரசுப் பணியாளர் தேர்வாணையம் (UPSC)"),
            ("Imperial Public Service Commission", "இம்பீரியல் அரசுப் பணியாளர் தேர்வாணையம்"),
            ("National Public Service Commission", "தேசிய அரசுப் பணியாளர் தேர்வாணையம்")
        ],
        "exp_en": "The Government of India Act 1935 provided for the establishment of a Federal Public Service Commission and Provincial Public Service Commissions.",
        "exp_ta": "1935-ம் ஆண்டின் இந்திய அரசுச் சட்டம் ஒரு கூட்டாட்சி அரசுப் பணியாளர் தேர்வாணையம் (Federal PSC) மற்றும் மாகாண தேர்வாணையங்களை அமைக்க வகை செய்தது.",
        "tip_en": "Evolution: Central PSC (1926) -> Federal PSC (1937) -> UPSC (1950).",
        "tip_ta": "பரிணாமம்: மத்திய PSC (1926) -> கூட்டாட்சி PSC (1937) -> UPSC (1950).",
        "fact_en": "On January 26, 1950, with the inauguration of the Constitution, Federal PSC became the Union Public Service Commission.",
        "fact_ta": "1950 ஜனவரி 26-ல் அரசியலமைப்பு நடைமுறைக்கு வந்தபோது, கூட்டாட்சி PSC மத்திய அரசுப் பணியாளர் தேர்வாணையமாக (UPSC) மாறியது."
    },
    # 21
    {
        "subtopic": "First Provincial PSC in India",
        "stem_en": "Which was the first province in British India to establish a Public Service Commission under a local enactment in 1929?",
        "stem_ta": "1929-ம் ஆண்டில் உள்ளூர் சட்டத்தின் கீழ் அரசுப் பணியாளர் தேர்வாணையத்தை அமைத்த பிரிட்டிஷ் இந்தியாவின் முதல் மாகாணம் எது?",
        "options": [
            ("Madras Presidency (Madras Service Commission)", "சென்னை மாகாணம் (மெட்ராஸ் சர்வீஸ் கமிஷன்)"),
            ("Bombay Presidency", "பம்பாய் மாகாணம்"),
            ("Bengal Presidency", "வங்காள மாகாணம்"),
            ("United Provinces", "ஐக்கிய மாகாணம்")
        ],
        "exp_en": "The Madras Service Commission was established in 1929 under the Madras Service Commission Act, 1929, becoming the first provincial public service commission in India.",
        "exp_ta": "1929-ம் ஆண்டின் மெட்ராஸ் சர்வீஸ் கமிஷன் சட்டத்தின்படி 1929-ல் அமைக்கப்பட்ட சென்னை சேவை ஆணையமே இந்தியாவின் முதல் மாகாண தேர்வாணையமாகும்.",
        "tip_en": "Madras Service Commission (1929) is the historic predecessor of today's TNPSC!",
        "tip_ta": "1929-ல் தொடங்கப்பட்ட மெட்ராஸ் சர்வீஸ் கமிஷனே இன்றைய TNPSC-யின் வரலாற்று முன்னோடியாகும்!",
        "fact_en": "It initially had three members including the Chairman, Sir Norman Marjoribanks.",
        "fact_ta": "தொடக்கத்தில் இதன் முதல் தலைவராக சர் நார்மன் மார்ஜோரிபேங்க்ஸ் உள்ளிட்ட மூன்று உறுப்பினர்கள் இருந்தனர்."
    },
    # 22
    {
        "subtopic": "Renaming of TNPSC",
        "stem_en": "In which year was the Madras Public Service Commission officially renamed as the Tamil Nadu Public Service Commission (TNPSC)?",
        "stem_ta": "சென்னை அரசுப் பணியாளர் தேர்வாணையம் எந்த ஆண்டு தமிழ்நாடு அரசுப் பணியாளர் தேர்வாணையம் (TNPSC) என அதிகாரப்பூர்வமாகப் பெயர் மாற்றம் செய்யப்பட்டது?",
        "options": [
            ("1970", "1970"),
            ("1967", "1967"),
            ("1969", "1969"),
            ("1972", "1972")
        ],
        "exp_en": "Following the renaming of Madras State as Tamil Nadu in January 1969, the Madras Public Service Commission was renamed as the Tamil Nadu Public Service Commission (TNPSC) in 1970.",
        "exp_ta": "1969 ஜனவரியில் மெட்ராஸ் மாநிலம் தமிழ்நாடு எனப் பெயர் மாற்றம் செய்யப்பட்டதைத் தொடர்ந்து, 1970-ல் சென்னை அரசுப் பணியாளர் தேர்வாணையம் TNPSC எனப் பெயர் மாற்றப்பட்டது.",
        "tip_en": "Madras State became Tamil Nadu: 1969; PSC renamed as TNPSC: 1970.",
        "tip_ta": "மெட்ராஸ் மாநிலம் தமிழ்நாடு என மாறியது: 1969; தேர்வாணையம் TNPSC எனப் பெயர் மாறியது: 1970.",
        "fact_en": "TNPSC is headquartered in Chennai and conducts recruitment for various state civil services.",
        "fact_ta": "TNPSC சென்னையைத் தலைமையிடமாகக் கொண்டு மாநிலக் குடிமைப் பணிகளுக்கான தேர்வுகளை நடத்துகிறது."
    },
    # 23
    {
        "subtopic": "First Chairman of Madras PSC",
        "stem_en": "Who served as the first Chairman of the Madras Service Commission established in 1929?",
        "stem_ta": "1929-ல் நிறுவப்பட்ட சென்னை சேவை ஆணையத்தின் முதல் தலைவராகப் பணியாற்றியவர் யார்?",
        "options": [
            ("Sir Norman Marjoribanks", "சர் நார்மன் மார்ஜோரிபேங்க்ஸ்"),
            ("Sir Ross Barker", "சர் ராஸ் பார்கர்"),
            ("Sir Archibald Nye", "சர் ஆர்ச்சிபால்ட் நை"),
            ("P.T. Rajan", "பி.டி. ராஜன்")
        ],
        "exp_en": "Sir Norman Marjoribanks was appointed as the first Chairman of the Madras Service Commission in 1929.",
        "exp_ta": "1929-ல் சென்னை சேவை ஆணையத்தின் முதல் தலைவராக சர் நார்மன் மார்ஜோரிபேங்க்ஸ் நியமிக்கப்பட்டார்.",
        "tip_en": "Central PSC First Chairman: Sir Ross Barker; Madras PSC First Chairman: Sir Norman Marjoribanks.",
        "tip_ta": "மத்திய PSC முதல் தலைவர்: சர் ராஸ் பார்கர்; சென்னை PSC முதல் தலைவர்: சர் நார்மன் மார்ஜோரிபேங்க்ஸ்.",
        "fact_en": "The Commission started functioning with two other members: Muhammad Bazlullah and Diwan Bahadur A. Ramaswami Mudaliar.",
        "fact_ta": "முகமது பஸ்லுல்லா மற்றும் திவான் பகதூர் ஏ. ராமசுவாமி முதலியார் ஆகிய இரண்டு உறுப்பினர்களுடன் இவ்வாணையம் செயல்படத் தொடங்கியது."
    },
    # 24
    {
        "subtopic": "Acting Chairman Appointment",
        "stem_en": "Under Article 316(1A), who has the power to appoint an acting Chairman of the UPSC when the office is vacant?",
        "stem_ta": "சரத்து 316(1A)-ன் கீழ், UPSC தலைவர் பதவி காலியாகும்போது தற்காலிகத் தலைவரை நியமிக்கும் அதிகாரம் யாருக்கு உள்ளது?",
        "options": [
            ("The President of India", "இந்தியக் குடியரசுத் தலைவர்"),
            ("The senior-most member of UPSC automatically", "UPSC-யின் மிக மூத்த உறுப்பினர் தானாகவே"),
            ("The Prime Minister of India", "இந்தியப் பிரதமர்"),
            ("The Chief Justice of India", "இந்தியத் தலைமை நீதிபதி")
        ],
        "exp_en": "Under Article 316(1A), if the office of the Chairman becomes vacant, the President may appoint one of the other members of the Commission to perform the duties of the office.",
        "exp_ta": "சரத்து 316(1A)-ன் படி, தலைவர் பதவி காலியாகும்போது, ஆணையத்தின் பிற உறுப்பினர்களில் ஒருவரை தற்காலிகத் தலைவராகப் பணியாற்ற இந்தியக் குடியரசுத் தலைவர் நியமிக்கலாம்.",
        "tip_en": "Article 316(1A) was inserted by the 15th Constitutional Amendment Act, 1963.",
        "tip_ta": "சரத்து 316(1A) 1963-ம் ஆண்டின் 15-வது அரசியலமைப்புத் திருத்தச் சட்டத்தின் மூலம் சேர்க்கப்பட்டது.",
        "fact_en": "For an SPSC, the Governor appoints an acting Chairman under the same Article.",
        "fact_ta": "SPSC-யைப் பொறுத்தவரை, அதே சரத்தின் கீழ் மாநில ஆளுநர் தற்காலிகத் தலைவரை நியமிக்கிறார்."
    },
    # 25
    {
        "subtopic": "SPSC Member Promotion to UPSC",
        "stem_en": "Under Article 319, can a member of a State Public Service Commission be appointed as the Chairman of the UPSC?",
        "stem_ta": "சரத்து 319-ன் கீழ், ஒரு மாநில அரசுப் பணியாளர் தேர்வாணையத்தின் உறுப்பினர் UPSC-யின் தலைவராக நியமிக்கப்பட முடியுமா?",
        "options": [
            ("Yes, eligible to be appointed as Chairman or member of the UPSC", "ஆம், UPSC-யின் தலைவர் அல்லது உறுப்பினராக நியமிக்கப்பட தகுதியுடையவர்"),
            ("No, strictly barred from any post in the UPSC", "இல்லை, UPSC-யின் எந்தப் பதவிக்கும் நியமிக்கப்பட முற்றிலும் தடை விதிக்கப்பட்டுள்ளது"),
            ("Yes, but only after resigning and waiting for 2 years", "ஆம், ஆனால் பதவி விலகி 2 ஆண்டுகள் காத்திருந்த பிறகே சாத்தியம்"),
            ("No, can only become Chairman of another State PSC", "இல்லை, மற்றொரு மாநில தேர்வாணையத்தின் தலைவராக மட்டுமே ஆக முடியும்")
        ],
        "exp_en": "Under Article 319(d), a member of an SPSC is eligible for appointment as the Chairman or any other member of the UPSC, or as the Chairman of that or any other SPSC.",
        "exp_ta": "சரத்து 319(d)-ன் படி, ஒரு SPSC உறுப்பினர் UPSC-யின் தலைவராகவோ அல்லது உறுப்பினராகவோ அல்லது அதே அல்லது மற்றொரு SPSC-யின் தலைவராகவோ நியமிக்கப்பட தகுதியுடையவர் ஆவார்.",
        "tip_en": "Movement upward is permitted under Article 319; lateral or downward movement under government is barred.",
        "tip_ta": "சரத்து 319-ன் கீழ் உயர் பதவிகளுக்குச் செல்ல அனுமதியுண்டு; அரசுப் பணிகளில் பக்கவாட்டு அல்லது கீழ்நிலைப் பணிகளுக்குச் செல்ல தடை உண்டு.",
        "fact_en": "This allows experienced PSC members to bring their expertise to higher commission roles.",
        "fact_ta": "இது அனுபவம் வாய்ந்த தேர்வாணைய உறுப்பினர்கள் உயர் தேர்வாணையப் பதவிகளுக்குச் செல்ல வழிவகுக்கிறது."
    },
    # 26
    {
        "subtopic": "Primary Function of UPSC",
        "stem_en": "What is the primary function of the UPSC under Article 320(1) of the Constitution?",
        "stem_ta": "அரசியலமைப்பின் சரத்து 320(1)-ன் கீழ் UPSC-யின் முதன்மையான பணி என்ன?",
        "options": [
            ("To conduct examinations for appointments to the services of the Union", "ஒன்றியத்தின் குடிமைப் பணிகளுக்கான நியமனத் தேர்வுகளை நடத்துதல்"),
            ("To frame pay scales and salaries for civil servants", "குடிமைப் பணியாளர்களுக்கான ஊதிய விகிதங்களை நிர்ணயித்தல்"),
            ("To allocate service cadres to selected candidates", "தேர்ந்தெடுக்கப்பட்ட தேர்வர்களுக்குப் பணிப் பிரிவுகளை (Cadre) ஒதுக்கீடு செய்தல்"),
            ("To supervise training academies for civil services", "குடிமைப் பணிகளுக்கான பயிற்சிப் பள்ளிகளைக் கண்காணித்தல்")
        ],
        "exp_en": "Under Article 320(1), it is the duty of the Union and State Public Service Commissions to conduct examinations for appointments to the services of the Union and States respectively.",
        "exp_ta": "சரத்து 320(1)-ன் படி, ஒன்றியம் மற்றும் மாநிலங்களின் பணிகளுக்கான நியமனங்களுக்குத் தேர்வுகளை நடத்துவது முறையே UPSC மற்றும் SPSC-யின் முதன்மைக் கடமையாகும்.",
        "tip_en": "Cadre allocation is done by the DoPT (Department of Personnel and Training), not by UPSC!",
        "tip_ta": "பணிப்பிரிவு (Cadre) ஒதுக்கீட்டை பணியாளர் மற்றும் பயிற்சித் துறை (DoPT) செய்கிறது, UPSC அல்ல!",
        "fact_en": "UPSC is a recruiting agency; service conditions and training are managed by the executive government.",
        "fact_ta": "UPSC என்பது தேர்வு முகமை மட்டுமே; பணி நிபந்தனைகள் மற்றும் பயிற்சிகள் நிர்வாக அரசால் நிர்வகிக்கப்படுகின்றன."
    },
    # 27
    {
        "subtopic": "Advisory Nature of UPSC",
        "stem_en": "What is the constitutional status of the recommendations made by the UPSC to the Government?",
        "stem_ta": "அரசாங்கத்திற்கு UPSC வழங்கும் பரிந்துரைகளின் அரசியலமைப்புத் தன்மை என்ன?",
        "options": [
            ("They are advisory in nature and not legally binding on the Government", "அவை ஆலோசனைத் தன்மை கொண்டவை மற்றும் அரசை சட்டப்பூர்வமாகக் கட்டுப்படுத்தாது"),
            ("They are mandatory and strictly binding on the Cabinet", "அவை கட்டாயமானவை மற்றும் அமைச்சரவையை முழுமையாகக் கட்டுப்படுத்தும்"),
            ("They have the force of an executive decree", "அவை நிர்வாக ஆணைக்கு இணையான சட்ட வலுவுடையவை"),
            ("They become binding only after approval by the Supreme Court", "உச்ச நீதிமன்றத்தின் ஒப்புதலுக்குப் பிறகே அவை கட்டுப்படுத்தும் நிலையைப் பெறும்")
        ],
        "exp_en": "The recommendations of the UPSC are advisory in nature. The Government can depart from its advice, but must explain the reasons to Parliament.",
        "exp_ta": "UPSC-யின் பரிந்துரைகள் ஆலோசனைத் தன்மை கொண்டவையே. அரசு அதன் ஆலோசனையிலிருந்து மாறுபடலாம், ஆனால் அதற்கான காரணங்களை நாடாளுமன்றத்தில் விளக்க வேண்டும்.",
        "tip_en": "UPSC's role is advisory; however, executive convention usually treats its advice with high respect.",
        "tip_ta": "UPSC ஆலோசனை அமைப்பாக இருந்தாலும், நிர்வாக மரபின்படி அதன் பரிந்துரைகள் மிகுந்த மரியாதையுடன் ஏற்கப்படுகின்றன.",
        "fact_en": "Non-acceptance of UPSC advice requires approval of the Appointments Committee of the Cabinet (ACC).",
        "fact_ta": "UPSC பரிந்துரையை நிராகரிக்க மத்திய அமைச்சரவையின் நியமனக் குழுவின் (ACC) ஒப்புதல் தேவை."
    },
    # 28
    {
        "subtopic": "Exemption from Consultation",
        "stem_en": "On which of the following matters is consultation with the UPSC NOT mandatory under Article 320(4)?",
        "stem_ta": "சரத்து 320(4)-ன் கீழ் பின்வரும் எந்த விவகாரத்தில் UPSC-யைக் கலந்தாலோசிப்பது கட்டாயமில்லை?",
        "options": [
            ("Making reservations in appointments for backward classes of citizens", "பிற்படுத்தப்பட்ட குடிமக்களுக்குப் பணி நியமனங்களில் இடஒதுக்கீடு வழங்குதல்"),
            ("Methods of recruitment to civil services", "குடிமைப் பணிகளுக்கான ஆளெடுப்பு முறைகள்"),
            ("Suitability of candidates for appointments and promotions", "நியமனங்கள் மற்றும் பதவி உயர்வுகளுக்கான தகுதியைத் தீர்மானித்தல்"),
            ("Disciplinary matters affecting civil servants", "குடிமைப் பணியாளர்களைப் பாதிக்கும் ஒழுங்கு நடவடிக்கை விவகாரங்கள்")
        ],
        "exp_en": "Article 320(4) explicitly states that nothing in clause (3) requires a Public Service Commission to be consulted regarding the manner of making reservations under Article 16(4).",
        "exp_ta": "சரத்து 320(4) தெளிவாகக் கூறுவது: சரத்து 16(4)-ன் கீழ் பிற்படுத்தப்பட்ட வகுப்பினருக்கான இடஒதுக்கீடு முறைகள் தொடர்பாக தேர்வாணையத்தைக் கலந்தாலோசிக்க வேண்டிய அவசியமில்லை.",
        "tip_en": "UPSC is NOT consulted on reservations (Art 16(4)) or SC/ST claims (Art 335).",
        "tip_ta": "இடஒதுக்கீடு (சரத்து 16(4)) அல்லது SC/ST கோரிக்கைகள் (சரத்து 335) ஆகியவற்றில் UPSC கலந்தாலோசிக்கப்படுவதில்லை.",
        "fact_en": "Reservation policies are sovereign executive and legislative policy decisions.",
        "fact_ta": "இடஒதுக்கீட்டுக் கொள்கைகள் அரசின் இறையாண்மை மற்றும் சட்டமன்றக் கொள்கை முடிவுகளாகும்."
    },
    # 29
    {
        "subtopic": "Extension of Functions",
        "stem_en": "Under Article 321, who has the power to confer additional functions on the Union Public Service Commission?",
        "stem_ta": "சரத்து 321-ன் கீழ், UPSC-க்குக் கூடுதல் பணிகளை வழங்கும் அதிகாரம் யாருக்கு உள்ளது?",
        "options": [
            ("The Parliament of India by law", "நாடாளுமன்றம் சட்டமியற்றுவதன் மூலம்"),
            ("The President of India by executive decree", "குடியரசுத் தலைவர் நிர்வாக ஆணை மூலம்"),
            ("The Prime Minister's Office directly", "பிரதமர் அலுவலகம் நேரடியாக"),
            ("The Supreme Court of India", "இந்திய உச்ச நீதிமன்றம்")
        ],
        "exp_en": "Article 321 provides that an Act made by Parliament may provide for the exercise of additional functions by the UPSC in respect of the services of the Union, local authorities, or other bodies corporate.",
        "exp_ta": "சரத்து 321-ன் படி, நாடாளுமன்றம் இயற்றும் ஒரு சட்டம், ஒன்றியத்தின் பணிகள் அல்லது உள்ளாட்சி அமைப்புகள் அல்லது சட்டப்பூர்வ நிறுவனங்கள் தொடர்பாக UPSC-க்கு கூடுதல் பணிகளை வழங்கலாம்.",
        "tip_en": "Parliament extends UPSC functions; State Legislature extends SPSC functions (Article 321).",
        "tip_ta": "நாடாளுமன்றம் UPSC-யின் பணிகளையும், மாநில சட்டமன்றம் SPSC-யின் பணிகளையும் விரிவுபடுத்தலாம் (சரத்து 321).",
        "fact_en": "Parliament can place any local authority or public institution under UPSC purview by enacting a law.",
        "fact_ta": "நாடாளுமன்றம் ஒரு சட்டத்தை இயற்றி எந்தவொரு உள்ளாட்சி அமைப்பு அல்லது பொது நிறுவனத்தையும் UPSC வரம்பிற்குள் கொண்டுவரலாம்."
    },
    # 30
    {
        "subtopic": "Service Conditions Regulations",
        "stem_en": "Under Article 318, who makes regulations determining the number of members of the UPSC and their conditions of service?",
        "stem_ta": "சரத்து 318-ன் கீழ், UPSC உறுப்பினர்களின் எண்ணிக்கை மற்றும் அவர்களது பணி நிபந்தனைகளைத் தீர்மானிக்கும் விதிகளை உருவாக்குபவர் யார்?",
        "options": [
            ("The President of India", "இந்தியக் குடியரசுத் தலைவர்"),
            ("The Parliament of India", "இந்திய நாடாளுமன்றம்"),
            ("The Chairman of UPSC", "UPSC-யின் தலைவர்"),
            ("The Chief Justice of India", "இந்தியத் தலைமை நீதிபதி")
        ],
        "exp_en": "Under Article 318(a), the President is empowered to determine the number of members of the UPSC and their conditions of service by regulations.",
        "exp_ta": "சரத்து 318(a)-ன் படி, விதிகளின் மூலம் UPSC-யின் உறுப்பினர் எண்ணிக்கை மற்றும் அவர்களது பணி நிபந்தனைகளைத் தீர்மானிக்கும் அதிகாரம் இந்தியக் குடியரசுத் தலைவருக்கு உண்டு.",
        "tip_en": "President makes regulations for UPSC; Governor makes regulations for SPSC (Article 318).",
        "tip_ta": "UPSC-க்கு குடியரசுத் தலைவரும், SPSC-க்கு ஆளுநரும் பணி நிபந்தனை விதிகளை உருவாக்குகின்றனர் (சரத்து 318).",
        "fact_en": "Conditions of service of a member cannot be varied to his disadvantage after appointment.",
        "fact_ta": "நியமனத்திற்குப் பிறகு ஒரு உறுப்பினரின் பணி நிபந்தனைகளை அவருக்குப் பாதகமாக மாற்ற முடியாது."
    },
    # 31
    {
        "subtopic": "Constitutional Safeguards",
        "stem_en": "Can the conditions of service of a member of the UPSC be varied to his disadvantage after his appointment?",
        "stem_ta": "UPSC உறுப்பினரின் பணி நிபந்தனைகளை அவரது நியமனத்திற்குப் பிறகு அவருக்குப் பாதகமாக மாற்ற முடியுமா?",
        "options": [
            ("No, proviso to Article 318 strictly prohibits variation to disadvantage", "முடியாது, சரத்து 318-ன் நிபந்தனை அவருக்குப் பாதகமாக மாற்றுவதை கண்டிப்பாகத் தடை செய்கிறது"),
            ("Yes, during an operational national emergency", "ஆம், செயல்பாட்டில் உள்ள தேசிய அவசரநிலையின் போது மாற்றலாம்"),
            ("Yes, with the consent of both Houses of Parliament", "ஆம், நாடாளுமன்றத்தின் இரு அவைகளின் ஒப்புதலுடன் மாற்றலாம்"),
            ("Yes, at the discretion of the Union Finance Ministry", "ஆம், மத்திய நிதி அமைச்சகத்தின் விருப்பப்படி மாற்றலாம்")
        ],
        "exp_en": "The proviso to Article 318 guarantees that the conditions of service of a member of a Public Service Commission shall not be varied to his disadvantage after his appointment.",
        "exp_ta": "சரத்து 318-ன் நிபந்தனையானது, அரசுப் பணியாளர் தேர்வாணைய உறுப்பினர் ஒருவரின் பணி நிபந்தனைகள் அவரது நியமனத்திற்குப் பிறகு அவருக்குப் பாதகமாக மாற்றப்படக் கூடாது என உறுதி செய்கிறது.",
        "tip_en": "Similar protection exists for Judges of Supreme Court and High Courts, and the CAG.",
        "tip_ta": "இதேபோன்ற பாதுகாப்பு உச்ச/உயர் நீதிமன்ற நீதிபதிகள் மற்றும் சி.ஏ.ஜி-க்கும் வழங்கப்பட்டுள்ளது.",
        "fact_en": "This safeguard insulates members from executive pressure or retaliation.",
        "fact_ta": "இந்தப் பாதுகாப்பு நிர்வாகத்தின் அழுத்தத்திலிருந்தும் பழிவாங்கும் நடவடிக்கைகளிலிருந்தும் உறுப்பினர்களைக் காக்கிறது."
    },
    # 32
    {
        "subtopic": "Disciplinary Proceedings Consultation",
        "stem_en": "Under Article 320(3)(c), is the UPSC consulted on all disciplinary matters affecting a person serving in a civil capacity?",
        "stem_ta": "சரத்து 320(3)(c)-ன் கீழ், குடிமைப் பணியில் உள்ள ஒரு நபரைப் பாதிக்கும் அனைத்து ஒழுங்கு நடவடிக்கை விவகாரங்களிலும் UPSC கலந்தாலோசிக்கப்படுகிறதா?",
        "options": [
            ("Yes, on all disciplinary matters affecting a civil servant", "ஆம், ஒரு குடிமைப் பணியாளரைப் பாதிக்கும் அனைத்து ஒழுங்கு நடவடிக்கை விவகாரங்களிலும்"),
            ("No, only on criminal trials before a Magistrate", "இல்லை, குற்றவியல் நீதிமன்ற விசாரணைகளில் மட்டுமே"),
            ("No, only when an officer is demoted by two ranks", "இல்லை, ஓர் அதிகாரி இரண்டு நிலைகள் பதவி இறக்கம் செய்யப்படும்போது மட்டுமே"),
            ("No, consultation was abolished by the 44th Amendment", "இல்லை, 44-வது திருத்தச் சட்டத்தால் இந்தக் கலந்தாலோசனை ரத்து செய்யப்பட்டது")
        ],
        "exp_en": "Under Article 320(3)(c), the UPSC must be consulted on all disciplinary matters affecting a person serving under the Government of India in a civil capacity, including memorials or petitions.",
        "exp_ta": "சரத்து 320(3)(c)-ன் படி, மத்திய அரசின் கீழ் குடிமைப் பணியில் உள்ள ஒரு நபரைப் பாதிக்கும் அனைத்து ஒழுங்கு நடவடிக்கை விவகாரங்களிலும் மனுக்கள் மற்றும் மேல்முறையீடுகள் உட்பட UPSC கலந்தாலோசிக்கப்பட வேண்டும்.",
        "tip_en": "Disciplinary matters include censure, withholding increments, demotion, compulsory retirement, and dismissal.",
        "tip_ta": "கண்டனம், ஊதிய உயர்வு நிறுத்தம், பதவி இறக்கம், கட்டாய ஓய்வு மற்றும் பணிநீக்கம் ஆகியவை ஒழுங்கு நடவடிக்கைகளில் அடங்கும்.",
        "fact_en": "Failure to consult UPSC does not invalidate the Government's disciplinary order (State of UP v. Manbodhan Lal Srivastava, 1957).",
        "fact_ta": "UPSC-யைக் கலந்தாலோசிக்கத் தவறுவது அரசாங்கத்தின் ஒழுங்கு நடவடிக்கை ஆணையை செல்லாததாக்காது (மன்மோதன் லால் ஸ்ரீவஸ்தவா வழக்கு, 1957)."
    },
    # 33
    {
        "subtopic": "Joint PSC Report Submission",
        "stem_en": "To whom does a Joint State Public Service Commission (JSPSC) present its annual report under Article 323(2)?",
        "stem_ta": "சரத்து 323(2)-ன் கீழ், கூட்டு மாநில அரசுப் பணியாளர் தேர்வாணையம் (JSPSC) தனது வருடாந்திர அறிக்கையை யாரிடம் சமர்ப்பிக்கிறது?",
        "options": [
            ("To the Governors of each of the concerned States", "சம்பந்தப்பட்ட ஒவ்வொரு மாநிலத்தின் ஆளுநர்களிடமும்"),
            ("Directly to the President of India only", "நேரடியாக இந்தியக் குடியரசுத் தலைவரிடம் மட்டுமே"),
            ("To the Union Ministry of Home Affairs", "மத்திய உள்துறை அமைச்சகத்திடம்"),
            ("To the Inter-State Council", "மாநிலங்களுக்கு இடையேயான கவுன்சிலிடம்")
        ],
        "exp_en": "Under Article 323(2), a Joint Commission presents its annual report to the Governor of each of the States which that Commission serves.",
        "exp_ta": "சரத்து 323(2)-ன் படி, கூட்டுத் தேர்வாணையம் தான் பணியாற்றும் சம்பந்தப்பட்ட ஒவ்வொரு மாநிலத்தின் ஆளுநரிடமும் தனது வருடாந்திர அறிக்கையைச் சமர்ப்பிக்கிறது.",
        "tip_en": "Each Governor then places the report before their respective State Legislature.",
        "tip_ta": "ஒவ்வொரு ஆளுநரும் அந்தந்த மாநில சட்டமன்றத்தில் அவ்வறிக்கையைச் சமர்ப்பிக்கச் செய்கிறார்.",
        "fact_en": "This maintains legislative accountability to all participating States.",
        "fact_ta": "இது சம்பந்தப்பட்ட அனைத்து மாநில சட்டமன்றங்களுக்கும் பொறுப்புடைமையை உறுதி செய்கிறது."
    },
    # 34
    {
        "subtopic": "Strength of UPSC",
        "stem_en": "What is the typical composition and strength of the Union Public Service Commission as determined by the President?",
        "stem_ta": "குடியரசுத் தலைவரால் தீர்மானிக்கப்படும் UPSC-யின் பொதுவான கட்டமைப்பு மற்றும் உறுப்பினர் எண்ணிக்கை என்ன?",
        "options": [
            ("A Chairman and 9 to 11 other members", "ஒரு தலைவர் மற்றும் 9 முதல் 11 பிற உறுப்பினர்கள்"),
            ("A Chairman and fixed 3 other members", "ஒரு தலைவர் மற்றும் நிலையான 3 பிற உறுப்பினர்கள்"),
            ("A Chairman and 25 other members representing each State", "ஒரு தலைவர் மற்றும் ஒவ்வொரு மாநிலத்தையும் பிரதிநிதித்துவப்படுத்தும் 25 உறுப்பினர்கள்"),
            ("A Chairman and 5 judges of High Courts", "ஒரு தலைவர் மற்றும் உயர் நீதிமன்றங்களின் 5 நீதிபதிகள்")
        ],
        "exp_en": "Usually, the UPSC consists of 9 to 11 members including the Chairman, as determined from time to time by the President.",
        "exp_ta": "பொதுவாக, குடியரசுத் தலைவரால் அவ்வப்போது தீர்மானிக்கப்படுவதற்கேற்ப, UPSC தலைவர் உட்பட 9 முதல் 11 உறுப்பினர்களைக் கொண்டதாக இருக்கும்.",
        "tip_en": "The Constitution has not fixed the strength; it is regulated by UPSC (Members) Regulations, 1969.",
        "tip_ta": "அரசியலமைப்பு உறுப்பினர் எண்ணிக்கையை நிர்ணயிக்கவில்லை; அது 1969-ம் ஆண்டின் UPSC விதிகள் மூலம் நிர்வகிக்கப்படுகிறது.",
        "fact_en": "Members are appointed from diverse fields including civil services, academics, and professions.",
        "fact_ta": "உறுப்பினர்கள் குடிமைப் பணிகள், கல்வித்துறை, தொழிற்துறைகள் உள்ளிட்ட பல்வேறு துறைகளிலிருந்து நியமிக்கப்படுகின்றனர்."
    },
    # 35
    {
        "subtopic": "Removal for Insolvency",
        "stem_en": "Under Article 317(3), can the President remove a member of a Public Service Commission without a Supreme Court inquiry if the member is adjudged an insolvent?",
        "stem_ta": "சரத்து 317(3)-ன் கீழ், ஒரு தேர்வாணைய உறுப்பினர் நொடித்துப்போனவர் (insolvent) என அறிவிக்கப்பட்டால், உச்ச நீதிமன்ற விசாரணையின்றி குடியரசுத் தலைவர் அவரை நீக்க முடியுமா?",
        "options": [
            ("Yes, SC reference is NOT required for insolvency or infirmity of mind/body", "ஆம், திவால் அல்லது உடல்/மன நலிவு ஆகிய காரணங்களுக்கு உச்ச நீதிமன்ற விசாரணை தேவையில்லை"),
            ("No, Supreme Court inquiry is mandatory for all grounds of removal", "இல்லை, அனைத்து பதவி நீக்கக் காரணங்களுக்கும் உச்ச நீதிமன்ற விசாரணை கட்டாயமாகும்"),
            ("Yes, but only with the prior concurrence of the Chief Justice of India", "ஆம், ஆனால் இந்தியத் தலைமை நீதிபதியின் முன் ஒப்புதலுடன் மட்டுமே"),
            ("No, Parliament must first pass an impeachment motion", "இல்லை, நாடாளுமன்றம் முதலில் பதவி நீக்கத் தீர்மானத்தை நிறைவேற்ற வேண்டும்")
        ],
        "exp_en": "Under Article 317(3), the President can remove a member without an SC inquiry if the member is adjudged an insolvent, engages in paid employment outside duties, or is unfit by reason of infirmity of mind or body.",
        "exp_ta": "சரத்து 317(3)-ன் படி, உறுப்பினர் நொடித்துப்போனவராக அறிவிக்கப்பட்டாலோ, வெளி ஊதியப் பணியில் ஈடுபட்டாலோ, உடல் அல்லது மன நலிவு காரணமாகப் பணியாற்றத் தகுதியற்றவரானாலோ உச்ச நீதிமன்ற விசாரணையின்றி குடியரசுத் தலைவர் நேரடியாக நீக்கலாம்.",
        "tip_en": "Supreme Court inquiry is required ONLY for the ground of 'misbehaviour' under Article 317(1).",
        "tip_ta": "சரத்து 317(1)-ன் கீழ் 'தவறான நடத்தை' என்ற காரணத்திற்காக மட்டுமே உச்ச நீதிமன்ற விசாரணை கட்டாயமாகும்.",
        "fact_en": "This distinction frequently appears in TNPSC and UPSC examinations.",
        "fact_ta": "இந்த வேறுபாடு TNPSC மற்றும் UPSC தேர்வுகளில் அடிக்கடி கேட்கப்படும் பகுதியாகும்."
    },
    # 36
    {
        "subtopic": "Suspension Power",
        "stem_en": "Who can suspend the Chairman or a member of an SPSC pending an inquiry by the Supreme Court on charges of misbehaviour?",
        "stem_ta": "தவறான நடத்தை குற்றச்சாட்டு குறித்த உச்ச நீதிமன்ற விசாரணை நிலுவையில் உள்ளபோது, SPSC தலைவர் அல்லது உறுப்பினரை இடைநீக்கம் செய்யும் அதிகாரம் யாருக்கு உள்ளது?",
        "options": [
            ("The Governor of the State", "மாநில ஆளுநர்"),
            ("The President of India", "இந்தியக் குடியரசுத் தலைவர்"),
            ("The Chief Justice of the High Court", "உயர் நீதிமன்றத் தலைமை நீதிபதி"),
            ("The State Home Minister", "மாநில உள்துறை அமைச்சர்")
        ],
        "exp_en": "Under Article 317(2), the Governor in the case of a State Commission, and the President in the case of the Union or a Joint Commission, may suspend the Chairman or member pending the Supreme Court's report.",
        "exp_ta": "சரத்து 317(2)-ன் படி, உச்ச நீதிமன்ற அறிக்கை வரும் வரை மாநில தேர்வாணைய உறுப்பினரை ஆளுநரும், மத்திய அல்லது கூட்டுத் தேர்வாணைய உறுப்பினரை குடியரசுத் தலைவரும் இடைநீக்கம் செய்யலாம்.",
        "tip_en": "Remember: Governor can SUSPEND an SPSC member, but only President can REMOVE him!",
        "tip_ta": "நினைவில் கொள்க: ஆளுநர் SPSC உறுப்பினரை இடைநீக்கம் (suspend) மட்டுமே செய்யலாம், குடியரசுத் தலைவர் மட்டுமே நீக்க (remove) முடியும்!",
        "fact_en": "Suspension is an interim measure to protect the integrity of the institution during the inquiry.",
        "fact_ta": "விசாரணையின் போது அமைப்பின் கண்ணியத்தைப் பாதுகாக்க எடுக்கப்படும் ஒரு தற்காலிக நடவடிக்கையே இடைநீக்கமாகும்."
    },
    # 37
    {
        "subtopic": "First Woman Chairman of UPSC",
        "stem_en": "Who was the first woman to be appointed as the Chairman of the Union Public Service Commission?",
        "stem_ta": "மத்திய அரசுப் பணியாளர் தேர்வாணையத்தின் (UPSC) தலைவராக நியமிக்கப்பட்ட முதல் பெண்மணி யார்?",
        "options": [
            ("Rose Millian Bethew (Rose Mary Bathew)", "ரோஸ் மிலியன் பெத்யூ (ரோஸ் மேரி பாத்யூ)"),
            ("Anna Rajam Malhotra", "அன்னா ராஜம் மல்ஹோத்ரா"),
            ("C.B. Muthamma", "சி.பி. முத்தம்மா"),
            ("Margaret Alva", "மார்கரெட் ஆல்வா")
        ],
        "exp_en": "Rose Millian Bethew (Bathew) was the first woman Chairman of the UPSC, serving from 1992 to 1996.",
        "exp_ta": "ரோஸ் மிலியன் பெத்யூ UPSC-யின் முதல் பெண் தலைவராக 1992 முதல் 1996 வரை பணியாற்றினார்.",
        "tip_en": "Rose Bethew was the first woman UPSC Chairman (1992); Anna Rajam Malhotra was the first woman IAS officer (1951).",
        "tip_ta": "ரோஸ் பெத்யூ UPSC-யின் முதல் பெண் தலைவர் (1992); அன்னா ராஜம் மல்ஹோத்ரா இந்தியாவின் முதல் பெண் IAS அதிகாரி (1951).",
        "fact_en": "She was from Meghalaya and made significant contributions to civil service recruitment reforms.",
        "fact_ta": "இவர் மேகாலயாவைச் சேர்ந்தவர் மற்றும் குடிமைப் பணி தேர்வுச் சீர்திருத்தங்களில் முக்கியப் பங்காற்றினார்."
    },
    # 38
    {
        "subtopic": "Watchdog of Merit System",
        "stem_en": "Why is the Union Public Service Commission described as the 'watchdog of merit system' in India?",
        "stem_ta": "இந்தியாவில் மத்திய அரசுப் பணியாளர் தேர்வாணையம் ஏன் 'தகுதி முறையின் கண்காணிப்பாளர்' (Watchdog of merit system) என்று அழைக்கப்படுகிறது?",
        "options": [
            ("Because it conducts open, competitive, and impartial examinations based on merit", "தகுதியின் அடிப்படையில் திறந்த, போட்டி மற்றும் நடுநிலையான தேர்வுகளை நடத்துவதால்"),
            ("Because it sets the national minimum wage standards", "தேசிய குறைந்தபட்ச ஊதியத் தரங்களை அது நிர்ணயிப்பதால்"),
            ("Because it audits all financial accounts of government offices", "அரசு அலுவலகங்களின் அனைத்து நிதி கணக்குகளையும் தணிக்கை செய்வதால்"),
            ("Because it manages promotions of Armed Forces officers", "முப்படைகளின் அதிகாரிகளுக்கான பதவி உயர்வுகளை நிர்வகிப்பதால்")
        ],
        "exp_en": "The UPSC is regarded as the 'watchdog of the merit system' in India because it ensures that recruitment to civil posts is conducted purely on merit through fair and competitive examinations.",
        "exp_ta": "UPSC 'தகுதி முறையின் கண்காணிப்பாளர்' என அழைக்கப்படுகிறது, ஏனெனில் நியாயமான போட்டித் தேர்வுகள் மூலம் தகுதியின் அடிப்படையில் மட்டுமே குடிமைப் பணிகளுக்கான ஆளெடுப்பு நடைபெறுவதை இது உறுதி செய்கிறது.",
        "tip_en": "UPSC is the watchdog of merit; CVC is the watchdog against corruption; CAG is the watchdog of public purse.",
        "tip_ta": "UPSC தகுதியின் கண்காணிப்பாளர்; CVC ஊழல் தடுப்புக் கண்காணிப்பாளர்; CAG பொது நிதியின் கண்காணிப்பாளர்.",
        "fact_en": "Dr. B.R. Ambedkar envisioned the PSC as an independent constitutional bulwark against political patronage.",
        "fact_ta": "அரசியல் சார்பு மற்றும் பரிந்துரைகளுக்கு எதிரான ஒரு சுயாதீன அரசியலமைப்பு அரணாக அம்பேத்கர் தேர்வாணையத்தை வடிவமைத்தார்."
    },
    # 39
    {
        "subtopic": "CVC vs UPSC Dynamics",
        "stem_en": "When both the Central Vigilance Commission (CVC) and UPSC are consulted on disciplinary matters, whose advice prevails in case of conflict?",
        "stem_ta": "ஒழுங்கு நடவடிக்கை விவகாரங்களில் மத்திய விழிப்புணர்வு ஆணையம் (CVC) மற்றும் UPSC இரண்டும் ஆலோசிக்கப்படும்போது, முரண்பாடு ஏற்பட்டால் யாருடைய ஆலோசனை மேலோங்கும்?",
        "options": [
            ("UPSC has constitutional primacy, though Government makes the final decision", "UPSC அரசியலமைப்பு முதன்மைத் தன்மை கொண்டது, இருப்பினும் அரசே இறுதி முடிவெடுக்கிறது"),
            ("CVC being an anti-corruption body automatically overrides the UPSC", "CVC ஊழல் தடுப்பு அமைப்பு என்பதால் அது தானாகவே UPSC-யை மேலோங்கும்"),
            ("The Central Administrative Tribunal decides which advice to adopt", "எந்த ஆலோசனையை ஏற்பது என்பதை மத்திய நிர்வாகத் தீர்ப்பாயம் முடிவு செய்கிறது"),
            ("The matter is referred to the Attorney General for binding arbitration", "கட்டுப்படுத்தும் நடுவர் தீர்ப்புக்காக விவகாரம் தலைமை வழக்கறிஞருக்கு அனுப்பப்படுகிறது")
        ],
        "exp_en": "Because UPSC is a constitutional body (Art 315) whereas CVC was created by statute, UPSC has higher constitutional status. In case of conflict, the Government decides, but UPSC advice is given great weight.",
        "exp_ta": "UPSC ஒரு அரசியலமைப்பு அமைப்பு (சரத்து 315) மற்றும் CVC ஒரு சட்டப்பூர்வ அமைப்பு என்பதால், UPSC உயரிய அரசியலமைப்பு அந்தஸ்தைப் பெற்றுள்ளது. முரண்பாட்டின் போது அரசே இறுதி முடிவெடுக்கிறது.",
        "tip_en": "Constitutional body (UPSC) vs Statutory body (CVC): UPSC holds constitutional primacy.",
        "tip_ta": "அரசியலமைப்பு அமைப்பு (UPSC) vs சட்டப்பூர்வ அமைப்பு (CVC): UPSC அரசியலமைப்பு ரீதியான முதன்மையைப் பெற்றுள்ளது.",
        "fact_en": "The DoPT issued guidelines in 2011 to resolve divergence of views between CVC and UPSC.",
        "fact_ta": "CVC மற்றும் UPSC இடையே கருத்து வேறுபாடுகளைத் தீர்க்க 2011-ல் DoPT வழிகாட்டுதல்களை வெளியிட்டது."
    },
    # 40
    {
        "subtopic": "All-India Services Role",
        "stem_en": "Which constitutional provision empowers Parliament to create one or more All-India Services common to the Union and States, for which UPSC recruits?",
        "stem_ta": "ஒன்றியம் மற்றும் மாநிலங்களுக்குப் பொதுவான ஒன்று அல்லது அதற்கு மேற்பட்ட அகில இந்தியப் பணிகளை உருவாக்க நாடாளுமன்றத்திற்கு அதிகாரமளிக்கும் அரசியலமைப்புச் சரத்து எது?",
        "options": [
            ("Article 312", "சரத்து 312"),
            ("Article 315", "சரத்து 315"),
            ("Article 311", "சரத்து 311"),
            ("Article 309", "சரத்து 309")
        ],
        "exp_en": "Article 312 provides that if the Rajya Sabha passes a resolution supported by not less than two-thirds of members present and voting, Parliament may by law create one or more All-India Services.",
        "exp_ta": "சரத்து 312-ன் படி, அவைக்கு வந்து வாக்களிக்கும் உறுப்பினர்களில் மூன்றில் இரண்டு பங்கு பெரும்பான்மையுடன் மாநிலங்களவை தீர்மானம் நிறைவேற்றினால், நாடாளுமன்றம் சட்டத்தின் மூலம் புதிய அகில இந்தியப் பணிகளை உருவாக்கலாம்.",
        "tip_en": "Rajya Sabha has special federal power under Article 312 to initiate new All-India Services.",
        "tip_ta": "புதிய அகில இந்தியப் பணிகளைத் தொடங்குவதற்கு மாநிலங்களவைக்கு சரத்து 312-ன் கீழ் சிறப்பு கூட்டாட்சி அதிகாரம் உண்டு.",
        "fact_en": "UPSC conducts the Civil Services Examination to recruit for IAS, IPS, and IFS.",
        "fact_ta": "IAS, IPS மற்றும் IFS ஆகிய பணிகளுக்கு ஆளெடுப்பு செய்ய UPSC குடிமைப் பணிகள் தேர்வை நடத்துகிறது."
    },
    # 41
    {
        "subtopic": "Article 311 Protections",
        "stem_en": "Article 311 of the Constitution provides procedural safeguards against which actions for civil servants?",
        "stem_ta": "இந்திய அரசியலமைப்பின் சரத்து 311 குடிமைப் பணியாளர்களுக்கு எந்த நடவடிக்கைகளுக்கு எதிராக நடைமுறைப் பாதுகாப்புகளை வழங்குகிறது?",
        "options": [
            ("Dismissal, removal, or reduction in rank without an inquiry", "விசாரணையின்றி பணிநீக்கம் செய்தல், பதவியிலிருந்து அகற்றுதல் அல்லது பதவி இறக்கம் செய்தல்"),
            ("Transfer to distant districts without hardship allowance", "இடர்படி இன்றி தொலைதூர மாவட்டங்களுக்குப் பணியிட மாற்றம் செய்தல்"),
            ("Compulsory deduction of provident fund contributions", "வருங்கால வைப்பு நிதி பிடித்தங்களை கட்டாயமாகப் பிடித்தம் செய்தல்"),
            ("Deputation to public sector undertakings without consent", "ஒப்புதல் இன்றி பொதுத்துறை நிறுவனங்களுக்குப் பணி அயல்முறைக்கு அனுப்புதல்")
        ],
        "exp_en": "Article 311 provides that no civil servant shall be dismissed, removed, or reduced in rank except after an inquiry in which he is informed of the charges and given a reasonable opportunity of being heard.",
        "exp_ta": "சரத்து 311-ன் படி, குற்றச்சாட்டுகள் குறித்து தெரிவிக்கப்பட்டு, நியாயமான விசாரணை மற்றும் விளக்கம் அளிக்க வாய்ப்பளிக்கப்படாமல் எந்தவொரு குடிமைப் பணியாளரையும் பணிநீக்கம் செய்யவோ, பதவியிலிருந்து அகற்றவோ அல்லது பதவி இறக்கம் செய்யவோ முடியாது.",
        "tip_en": "Article 311 protects civil servants from arbitrary dismissal; Article 320(3)(c) mandates UPSC consultation.",
        "tip_ta": "சரத்து 311 தன்னிச்சையான பணிநீக்கத்திலிருந்து பாதுகாக்கிறது; சரத்து 320(3)(c) UPSC ஆலோசனையைக் கட்டாயமாக்குகிறது.",
        "fact_en": "Article 311 applies to civil servants of the Union, All-India Services, and State civil services.",
        "fact_ta": "சரத்து 311 ஒன்றிய, அகில இந்திய மற்றும் மாநில குடிமைப் பணியாளர்கள் அனைவருக்கும் பொருந்தும்."
    },
    # 42
    {
        "subtopic": "Staff Regulations",
        "stem_en": "Under Article 318(b), who determines the number of staff members of the UPSC and their conditions of service?",
        "stem_ta": "சரத்து 318(b)-ன் கீழ், UPSC பணியாளர்களின் எண்ணிக்கை மற்றும் அவர்களது பணி நிபந்தனைகளைத் தீர்மானிப்பவர் யார்?",
        "options": [
            ("The President of India", "இந்தியக் குடியரசுத் தலைவர்"),
            ("The UPSC Chairman independently", "UPSC தலைவர் தன்னிச்சையாக"),
            ("The Union Public Accounts Committee", "மத்திய பொதுக் கணக்குக் குழு"),
            ("The Staff Selection Commission", "பணியாளர் தேர்வாணையம் (SSC)")
        ],
        "exp_en": "Under Article 318(b), the President makes regulations regarding the number of staff members of the Commission and their conditions of service.",
        "exp_ta": "சரத்து 318(b)-ன் படி, தேர்வாணையத்தின் பணியாளர் எண்ணிக்கை மற்றும் அவர்களது பணி நிபந்தனைகள் குறித்த விதிகளை இந்தியக் குடியரசுத் தலைவர் உருவாக்குகிறார்.",
        "tip_en": "For UPSC, President regulates staff; for SPSC, Governor regulates staff under Article 318(b).",
        "tip_ta": "UPSC பணியாளர் விதிகளை குடியரசுத் தலைவரும், SPSC பணியாளர் விதிகளை ஆளுநரும் சரத்து 318(b)-ன் கீழ் உருவாக்குகின்றனர்.",
        "fact_en": "The Secretariat of the UPSC is headed by a Secretary who is an IAS officer of Additional Secretary rank.",
        "fact_ta": "UPSC செயலகம் கூடுதல் செயலாளர் அந்தஸ்துள்ள IAS அதிகாரியான ஒரு செயலாளரால் வழிநடத்தப்படுகிறது."
    },
    # 43
    {
        "subtopic": "Oaths and Affirmations",
        "stem_en": "Does the Constitution of India prescribe a specific oath of office for the Chairman and members of the UPSC in the Third Schedule?",
        "stem_ta": "மூன்றாவது அட்டவணையில் UPSC தலைவர் மற்றும் உறுப்பினர்களுக்கு குறிப்பிட்ட பதவிப் பிரமாணத்தை இந்திய அரசியலமைப்பு பரிந்துரைத்துள்ளதா?",
        "options": [
            ("No, the Third Schedule does not prescribe an oath for UPSC members", "இல்லை, மூன்றாவது அட்டவணை UPSC உறுப்பினர்களுக்கு பதவிப் பிரமாணத்தை பரிந்துரைக்கவில்லை"),
            ("Yes, Form IV of the Third Schedule prescribes their oath", "ஆம், மூன்றாவது அட்டவணையின் படிவம் IV அவர்களது பிரமாணத்தைப் பரிந்துரைக்கிறது"),
            ("Yes, identical to the oath of the Chief Justice of India", "ஆம், இந்தியத் தலைமை நீதிபதியின் பிரமாணத்திற்கு சமமானது"),
            ("Yes, administered by the Chief Election Commissioner", "ஆம், தலைமைத் தேர்தல் ஆணையரால் பதவிப் பிரமாணம் செய்து வைக்கப்படுகிறது")
        ],
        "exp_en": "Unlike Ministers, Judges, and the CAG, the Constitution does NOT prescribe a specific oath of office for UPSC or SPSC members in the Third Schedule.",
        "exp_ta": "அமைச்சர்கள், நீதிபதிகள் மற்றும் சி.ஏ.ஜி. போன்று அல்லாமல், UPSC அல்லது SPSC உறுப்பினர்களுக்கு மூன்றாவது அட்டவணையில் அரசியலமைப்பு எந்தவொரு குறிப்பிட்ட பதவிப் பிரமாணத்தையும் பரிந்துரைக்கவில்லை.",
        "tip_en": "Important test trap: Third Schedule contains oaths for Ministers, Judges, MPs, MLAs, and CAG — but NOT for UPSC/SPSC members!",
        "tip_ta": "முக்கியத் தேர்வுப் பொறி: 3-வது அட்டவணையில் அமைச்சர்கள், நீதிபதிகள், எம்.பி, எம்.எல்.ஏ மற்றும் CAG-க்கு பிரமாணம் உண்டு — ஆனால் UPSC/SPSC உறுப்பினர்களுக்கு இல்லை!",
        "fact_en": "Members subscribe to an oath administered by the Chairman under internal regulations.",
        "fact_ta": "உள் விதிகளின்படி ஆணையத்தின் தலைவரால் உறுப்பினர்களுக்குப் பிரமாணம் செய்து வைக்கப்படுகிறது."
    },
    # 44
    {
        "subtopic": "Secretariat Location",
        "stem_en": "Where is the permanent headquarters of the Union Public Service Commission located?",
        "stem_ta": "மத்திய அரசுப் பணியாளர் தேர்வாணையத்தின் (UPSC) நிரந்தரத் தலைமையகம் எங்கு அமைந்துள்ளது?",
        "options": [
            ("Dholpur House, Shahjahan Road, New Delhi", "தோல்பூர் ஹவுஸ், ஷாஜகான் சாலை, புது தில்லி"),
            ("North Block, Central Secretariat, New Delhi", "வடக்கு பிளாக், மத்திய செயலகம், புது தில்லி"),
            ("South Block, Raisina Hill, New Delhi", "தெற்கு பிளாக், ரைசினா குன்று, புது தில்லி"),
            ("Sardar Patel Bhawan, Parliament Street, New Delhi", "சர்தார் படேல் பவன், நாடாளுமன்ற வீதி, புது தில்லி")
        ],
        "exp_en": "The permanent headquarters of the UPSC is Dholpur House, situated on Shahjahan Road in New Delhi.",
        "exp_ta": "UPSC-யின் நிரந்தரத் தலைமையகம் புது தில்லியில் உள்ள ஷாஜகான் சாலையில் அமைந்துள்ள தோல்பூர் ஹவுஸ் ஆகும்.",
        "tip_en": "UPSC: Dholpur House, New Delhi; TNPSC: TNPSC Road, Park Town, Chennai.",
        "tip_ta": "UPSC: தோல்பூர் ஹவுஸ், புது தில்லி; TNPSC: TNPSC சாலை, பார்க் டவுன், சென்னை.",
        "fact_en": "Dholpur House was the historic residence of the Maharaja of Dholpur in Delhi.",
        "fact_ta": "தோல்பூர் ஹவுஸ் தில்லியில் தோல்பூர் மகாராஜாவின் வரலாற்றுச் சிறப்புமிக்க இல்லமாக இருந்தது."
    },
    # 45
    {
        "subtopic": "Civil Services Examination Scheme",
        "stem_en": "Which committee appointed by UPSC in 1974-76 recommended the present three-stage Civil Services Examination structure?",
        "stem_ta": "1974-76-ல் UPSC-யால் நியமிக்கப்பட்ட எந்தக் குழு தற்போதைய மூன்று கட்ட குடிமைப் பணி தேர்வு முறையைப் பரிந்துரைத்தது?",
        "options": [
            ("Kothari Committee (1976)", "கோத்தாரி குழு (1976)"),
            ("Satish Chandra Committee (1989)", "சதீஷ் சந்திரா குழு (1989)"),
            ("Y.K. Alagh Committee (2001)", "ஒய்.கே. அலக் குழு (2001)"),
            ("Baswan Committee (2016)", "பஸ்வான் குழு (2016)"),
        ],
        "exp_en": "The Committee on Recruitment Policy and Selection Methods chaired by Dr. D.S. Kothari (1974-1976) recommended the unified three-stage examination structure: Preliminary, Main, and Interview.",
        "exp_ta": "டாக்டர் டி.எஸ். கோத்தாரி தலைமையிலான தேர்வுக் கொள்கை மற்றும் ஆளெடுப்பு முறைக் குழு (1974-1976), முதல்நிலை, முதன்மை மற்றும் நேர்முகத் தேர்வு என்ற ஒருங்கிணைந்த மூன்று கட்ட தேர்வு முறையைப் பரிந்துரைத்தது.",
        "tip_en": "Kothari Committee (1976) created the modern CSE system introduced in 1979.",
        "tip_ta": "கோத்தாரி குழு (1976) பரிந்துரைத்த முறையே 1979-ல் நவீன குடிமைப் பணிகள் தேர்வாக அறிமுகப்படுத்தப்பட்டது.",
        "fact_en": "Satish Chandra Committee later introduced the essay paper in the Main examination in 1993.",
        "fact_ta": "சதீஷ் சந்திரா குழு பின்னர் 1993-ல் முதன்மைத் தேர்வில் கட்டுரைத் தாளை அறிமுகப்படுத்தியது."
    },
    # 46
    {
        "subtopic": "CSAT Introduction",
        "stem_en": "In which year was the Civil Services Aptitude Test (CSAT) introduced in the UPSC Civil Services Preliminary Examination?",
        "stem_ta": "UPSC குடிமைப் பணி முதல்நிலைத் தேர்வில் குடிமைப் பணிகள் திறனறித் தேர்வு (CSAT) எந்த ஆண்டு அறிமுகப்படுத்தப்பட்டது?",
        "options": [
            ("2011", "2011"),
            ("2008", "2008"),
            ("2014", "2014"),
            ("2015", "2015")
        ],
        "exp_en": "The Civil Services Aptitude Test (CSAT) as Paper-II of the Preliminary Examination was introduced in 2011, replacing the optional subject paper.",
        "exp_ta": "விருப்பப் பாடத் தாளுக்குப் பதிலாக, முதல்நிலைத் தேர்வின் தாள்-II ஆக குடிமைப் பணிகள் திறனறித் தேர்வு (CSAT) 2011-ல் அறிமுகப்படுத்தப்பட்டது.",
        "tip_en": "CSAT was made a qualifying paper (33% passing mark) in 2015.",
        "tip_ta": "2015-ல் CSAT தகுதித் தாளாக (33% தகுதி மதிப்பெண்) மாற்றப்பட்டது.",
        "fact_en": "The reform was based on the recommendations of the Prof. Y.K. Alagh Committee.",
        "fact_ta": "இந்தச் சீர்திருத்தம் பேராசிரியர் ஒய்.கே. அலக் குழுவின் பரிந்துரைகளின் அடிப்படையில் அமைந்தது."
    },
    # 47
    {
        "subtopic": "SPSC Member Resignation",
        "stem_en": "To whom must a member of a State Public Service Commission address their written resignation under Article 316(2)?",
        "stem_ta": "சரத்து 316(2)-ன் கீழ், மாநில அரசுப் பணியாளர் தேர்வாணையத்தின் உறுப்பினர் தனது எழுத்துப்பூர்வ பதவி விலகல் கடிதத்தை யாரிடம் அளிக்க வேண்டும்?",
        "options": [
            ("The Governor of the State", "மாநில ஆளுநர்"),
            ("The President of India", "இந்தியக் குடியரசுத் தலைவர்"),
            ("The Chief Minister of the State", "மாநில முதலமைச்சர்"),
            ("The Chairman of the SPSC", "மாநில தேர்வாணையத்தின் தலைவர்")
        ],
        "exp_en": "Under Article 316(2)(a), a member of an SPSC may, by writing under his hand addressed to the Governor of the State, resign his office.",
        "exp_ta": "சரத்து 316(2)(a)-ன் படி, SPSC உறுப்பினர் தனது கைப்பட எழுதிய கடிதத்தை மாநில ஆளுநருக்கு அனுப்பி தனது பதவியை விலகலாம்.",
        "tip_en": "Resignation: UPSC member -> President; SPSC member -> Governor; JSPSC member -> President.",
        "tip_ta": "பதவி விலகல்: UPSC உறுப்பினர் -> குடியரசுத் தலைவர்; SPSC உறுப்பினர் -> ஆளுநர்; JSPSC உறுப்பினர் -> குடியரசுத் தலைவர்.",
        "fact_en": "The resignation takes effect from the date it is accepted by the Governor.",
        "fact_ta": "ஆளுநரால் ஏற்றுக்கொள்ளப்பட்ட நாளிலிருந்து பதவி விலகல் நடைமுறைக்கு வருகிறது."
    },
    # 48
    {
        "subtopic": "Salary and Allowances of Members",
        "stem_en": "The salary and allowances of the Chairman and members of the UPSC are equivalent to which constitutional dignitaries?",
        "stem_ta": "UPSC தலைவர் மற்றும் உறுப்பினர்களின் ஊதியம் மற்றும் படிகள் எந்த அரசியலமைப்புப் பதவிக்கு இணையானவை?",
        "options": [
            ("Supreme Court Judges and High Court Chief Justices", "உச்ச நீதிமன்ற நீதிபதிகள் மற்றும் உயர் நீதிமன்றத் தலைமை நீதிபதிகள்"),
            ("Cabinet Ministers of the Union", "மத்திய அமைச்சரவை அமைச்சர்கள்"),
            ("Members of Parliament", "நாடாளுமன்ற உறுப்பினர்கள்"),
            ("Lieutenant Governors of Union Territories", "யூனியன் பிரதேசங்களின் துணைநிலை ஆளுநர்கள்")
        ],
        "exp_en": "Under prevailing rules, the salary of the UPSC Chairman is equivalent to that of a Supreme Court Judge, and members receive salaries equivalent to High Court Judges.",
        "exp_ta": "நடைமுறையில் உள்ள விதிகளின்படி, UPSC தலைவரின் ஊதியம் உச்ச நீதிமன்ற நீதிபதிக்கும், உறுப்பினர்களின் ஊதியம் உயர் நீதிமன்ற நீதிபதிகளுக்கும் இணையானதாகும்.",
        "tip_en": "UPSC Chairman salary = Supreme Court Judge salary (charged on Consolidated Fund of India).",
        "tip_ta": "UPSC தலைவர் ஊதியம் = உச்ச நீதிமன்ற நீதிபதி ஊதியம் (இந்தியத் தொகுப்பு நிதியில் சுமத்தப்படுவது).",
        "fact_en": "Their pensions and allowances are also protected by constitutional guarantee under Article 322.",
        "fact_ta": "அவர்களின் ஓய்வூதியங்கள் மற்றும் படிகளும் சரத்து 322-ன் கீழ் அரசியலமைப்பு ரீதியாகப் பாதுகாக்கப்படுகின்றன."
    },
    # 49
    {
        "subtopic": "TNPSC Constitutional Composition",
        "stem_en": "Under the Tamil Nadu Public Service Commission Regulations, what is the sanctioned strength of the TNPSC including the Chairman?",
        "stem_ta": "தமிழ்நாடு அரசுப் பணியாளர் தேர்வாணைய விதிகளின்படி, தலைவர் உட்பட TNPSC-யின் அங்கீகரிக்கப்பட்ட மொத்த உறுப்பினர் எண்ணிக்கை என்ன?",
        "options": [
            ("A Chairman and 14 other members (Total 15)", "ஒரு தலைவர் மற்றும் 14 பிற உறுப்பினர்கள் (மொத்தம் 15)"),
            ("A Chairman and 8 other members (Total 9)", "ஒரு தலைவர் மற்றும் 8 பிற உறுப்பினர்கள் (மொத்தம் 9)"),
            ("A Chairman and 20 other members (Total 21)", "ஒரு தலைவர் மற்றும் 20 பிற உறுப்பினர்கள் (மொத்தம் 21)"),
            ("A Chairman and 5 other members (Total 6)", "ஒரு தலைவர் மற்றும் 5 பிற உறுப்பினர்கள் (மொத்தம் 6)")
        ],
        "exp_en": "As per the Tamil Nadu Public Service Commission Regulations, the Commission consists of a Chairman and 14 other members, making a total strength of 15.",
        "exp_ta": "தமிழ்நாடு அரசுப் பணியாளர் தேர்வாணைய விதிகளின்படி, தலைவர் உட்பட 14 பிற உறுப்பினர்கள் என மொத்தம் 15 உறுப்பினர்களைக் கொண்டதாக TNPSC இயங்குகிறது.",
        "tip_en": "Sanctioned strength of TNPSC: 1 Chairman + 14 Members = 15.",
        "tip_ta": "TNPSC-யின் அங்கீகரிக்கப்பட்ட மொத்த எண்ணிக்கை: 1 தலைவர் + 14 உறுப்பினர்கள் = 15.",
        "fact_en": "The strength is determined by the Governor of Tamil Nadu under Article 318 of the Constitution.",
        "fact_ta": "அரசியலமைப்பின் சரத்து 318-ன் கீழ் தமிழ்நாடு ஆளுநரால் இந்த எண்ணிக்கை நிர்ணயிக்கப்படுகிறது."
    },
    # 50
    {
        "subtopic": "SPSC Chairman Further Employment",
        "stem_en": "Under Article 319(b), the Chairman of a State Public Service Commission is eligible for appointment to which of the following offices?",
        "stem_ta": "சரத்து 319(b)-ன் கீழ், ஒரு மாநில அரசுப் பணியாளர் தேர்வாணையத்தின் தலைவர் பின்வரும் எந்தப் பதவிகளுக்கு நியமிக்கப்பட தகுதியுடையவர்?",
        "options": [
            ("Chairman or member of the UPSC, or Chairman of any other State PSC", "UPSC-யின் தலைவர் அல்லது உறுப்பினர், அல்லது மற்றொரு மாநில தேர்வாணையத்தின் தலைவர்"),
            ("Chief Election Commissioner of India", "இந்தியத் தலைமைத் தேர்தல் ஆணையர்"),
            ("Governor of any Indian State", "எந்தவொரு இந்திய மாநிலத்தின் ஆளுநர்"),
            ("Chief Justice of a High Court", "உயர் நீதிமன்றத் தலைமை நீதிபதி")
        ],
        "exp_en": "Under Article 319(b), the Chairman of an SPSC is eligible for appointment as the Chairman or any other member of the UPSC, or as the Chairman of any other State Public Service Commission, but not for any other government employment.",
        "exp_ta": "சரத்து 319(b)-ன் படி, SPSC தலைவர் UPSC-யின் தலைவராகவோ அல்லது உறுப்பினராகவோ, அல்லது மற்றொரு மாநில அரசுப் பணியாளர் தேர்வாணையத்தின் தலைவராகவோ மட்டுமே நியமிக்கப்பட தகுதியுடையவர்; வேறு அரசுப் பணிகளை ஏற்க முடியாது.",
        "tip_en": "SPSC Chairman can go to: (1) UPSC Chairman, (2) UPSC Member, (3) Other SPSC Chairman. Nowhere else in Govt.",
        "tip_ta": "SPSC தலைவர் செல்லக்கூடிய பதவிகள்: (1) UPSC தலைவர், (2) UPSC உறுப்பினர், (3) பிற SPSC தலைவர். வேறு எங்கும் இல்லை.",
        "fact_en": "This ensures complete impartiality during his tenure as State PSC Chairman.",
        "fact_ta": "இது மாநிலத் தேர்வாணையத் தலைவராகப் பணியாற்றும் காலத்தில் அவரது முழுமையான நடுநிலைமையை உறுதி செய்கிறது."
    }
]

def build_questions():
    questions = []
    for idx, item in enumerate(raw_easy_data, start=1):
        qid = f"PSC_E_{idx:03d}"
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
        
        q = make_upsc_q(
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
            tags=["polity", "upsc_state_psc", "easy", item["subtopic"].lower().replace(" ", "_")]
        )
        questions.append(q)
    return questions

if __name__ == "__main__":
    qs = build_questions()
    print(f"Generated {len(qs)} raw Easy questions for UPSC & State PSC.")
    
    balanced_qs = randomize_and_balance_dataset(qs, seed=42)
    
    out_path = os.path.join("data", "questions", "polity", "upsc_state_psc_easy.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(balanced_qs, f, ensure_ascii=False, indent=2)
        
    print(f"Saved balanced Easy MCQs to {out_path}")
    
    val = ContentValidator()
    report = val.validate_file(out_path, expected_count=50, expected_prefix="PSC_E_")
    print(f"Validation Report: {'PASS' if report.is_valid else 'FAIL'} | Total: {report.total_audited}")
    if not report.is_valid:
        for iss in report.issues[:10]:
            print(f"  Issue: {iss}")
    print(f"Key Distribution: {report.key_distribution}")
    
    keys = [q["correct_answer"] for q in balanced_qs]
    pat_ok, pat_issues = audit_answer_pattern(keys, 50)
    print(f"Answer Pattern Audit: {'PASS' if pat_ok else 'FAIL'} | Issues: {pat_issues}")
