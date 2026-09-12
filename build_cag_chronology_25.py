# -*- coding: utf-8 -*-
"""
Build 25 Chronology MCQs for CAG (Comptroller & Auditor General of India)
ID range: CAG_C_001 to CAG_C_025
Strictly satisfies all ChronologyValidator rules:
- Events 1, 2, 3, 4 in stem are presented in non-chronological order.
- Correct sequence is NEVER 1-2-3-4.
- Options are valid permutations of [1, 2, 3, 4].
- Explanation has 4-digit years and '->' arrow sequence.
- Keys are balanced: 7 A, 6 B, 6 C, 6 D.
"""

import json
import os
import random
from itertools import permutations
from cag_mcq_helper import make_cag_q
from tools.nova_content_engine.chronology_validator import ChronologyValidator
from tools.nova_content_engine.validator import ContentValidator

raw_chronology_data = [
    # 1
    {
        "subtopic": "Early CAGs of Independent India",
        "intro_en": "Arrange the following early Comptrollers and Auditors General of India in chronological order of their appointment to office:",
        "intro_ta": "சுதந்திர இந்தியாவின் பின்வரும் ஆரம்பகால தலைமைத் தணிக்கையாளர்களை அவர்கள் பதவியேற்ற காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events_en": [
            "A.K. Roy appointed as third CAG",
            "V. Narahari Rao appointed as first CAG",
            "S. Ranganathan appointed as fourth CAG",
            "A.K. Chanda appointed as second CAG"
        ],
        "events_ta": [
            "ஏ.கே. ராய் மூன்றாவது சி.ஏ.ஜியாக நியமிக்கப்படுதல்",
            "வி. நரஹரி ராவ் முதல் சி.ஏ.ஜியாக நியமிக்கப்படுதல்",
            "எஸ். ரங்கநாதன் நான்காவது சி.ஏ.ஜியாக நியமிக்கப்படுதல்",
            "ஏ.கே. சந்தா இரண்டாவது சி.ஏ.ஜியாக நியமிக்கப்படுதல்"
        ],
        # Chronological order of event indices (1-indexed): 2 (1948) -> 4 (1954) -> 1 (1960) -> 3 (1966)
        "correct_seq": [2, 4, 1, 3],
        "details_en": "2. V. Narahari Rao (1948)\n4. A.K. Chanda (1954)\n1. A.K. Roy (1960)\n3. S. Ranganathan (1966)",
        "details_ta": "2. வி. நரஹரி ராவ் (1948)\n4. ஏ.கே. சந்தா (1954)\n1. ஏ.கே. ராய் (1960)\n3. எஸ். ரங்கநாதன் (1966)",
        "tip_en": "V. Narahari Rao (1948-1954) was the first CAG of independent India.",
        "tip_ta": "வி. நரஹரி ராவ் (1948-1954) சுதந்திர இந்தியாவின் முதல் சி.ஏ.ஜி ஆவார்.",
        "fact_en": "S. Ranganathan served as CAG from 1966 to 1972.",
        "fact_ta": "எஸ். ரங்கநாதன் 1966 முதல் 1972 வரை சி.ஏ.ஜியாகப் பணியாற்றினார்."
    },
    # 2
    {
        "subtopic": "21st Century CAGs of India",
        "intro_en": "Arrange the following Comptrollers and Auditors General of India in chronological order of their assumption of office:",
        "intro_ta": "இந்தியாவின் பின்வரும் தலைமைத் தணிக்கையாளர்களை அவர்கள் பதவியேற்ற காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events_en": [
            "Rajiv Mehrishi appointed as CAG",
            "Vinod Rai appointed as CAG",
            "G.C. Murmu appointed as CAG",
            "Shashi Kant Sharma appointed as CAG"
        ],
        "events_ta": [
            "ராஜீவ் மெஹ்ரிஷி சி.ஏ.ஜியாக நியமிக்கப்படுதல்",
            "வினோத் ராய் சி.ஏ.ஜியாக நியமிக்கப்படுதல்",
            "ஜி.சி. முர்மு சி.ஏ.ஜியாக நியமிக்கப்படுதல்",
            "சசி காந்த் சர்மா சி.ஏ.ஜியாக நியமிக்கப்படுதல்"
        ],
        # Order: 2 (2008) -> 4 (2013) -> 1 (2017) -> 3 (2020)
        "correct_seq": [2, 4, 1, 3],
        "details_en": "2. Vinod Rai (2008)\n4. Shashi Kant Sharma (2013)\n1. Rajiv Mehrishi (2017)\n3. G.C. Murmu (2020)",
        "details_ta": "2. வினோத் ராய் (2008)\n4. சசி காந்த் சர்மா (2013)\n1. ராஜீவ் மெஹ்ரிஷி (2017)\n3. ஜி.சி. முர்மு (2020)",
        "tip_en": "Vinod Rai (2008-2013) presided over landmark 2G spectrum and Coal block audit reports.",
        "tip_ta": "வினோத் ராய் (2008-2013) 2G அலைக்கற்றை மற்றும் நிலக்கரி தணிக்கை அறிக்கைகளை வெளியிட்டார்.",
        "fact_en": "G.C. Murmu took office in August 2020.",
        "fact_ta": "ஜி.சி. முர்மு ஆகஸ்ட் 2020-ல் பதவியேற்றார்."
    },
    # 3
    {
        "subtopic": "Pre-Independence Audit Milestones",
        "intro_en": "Arrange the following pre-independence financial audit developments in chronological order:",
        "intro_ta": "சுதந்திரத்திற்கு முந்தைய பின்வரும் நிதித் தணிக்கை மைல்கற்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events_en": [
            "Statutory independence granted to Auditor General under Government of India Act 1935",
            "Creation of the office of Accountant General under Lord Canning in 1858",
            "Auditor General made statutory under Montagu-Chelmsford Reforms (1919 Act)",
            "Appointment of Sir Edward Drummond as the first Auditor General in 1860"
        ],
        "events_ta": [
            "1935 இந்திய அரசுச் சட்டத்தின் கீழ் தணிக்கைத் தலைவருக்கு சட்டப்பூர்வ சுதந்திரம் வழங்கப்படுதல்",
            "1858-ல் கானிங் பிரபுவின் கீழ் கணக்குத் தலைவர் அலுவலகம் உருவாக்கப்படுதல்",
            "மான்டேகு-செம்ஸ்போர்டு சீர்திருத்தங்களின் கீழ் (1919 சட்டம்) தணிக்கைத் தலைவர் சட்டப்பூர்வமாக்கப்படுதல்",
            "1860-ல் சர் எட்வர்ட் டிரம்மாண்ட் முதல் தணிக்கைத் தலைவராக நியமிக்கப்படுதல்"
        ],
        # Order: 2 (1858) -> 4 (1860) -> 3 (1919) -> 1 (1935)
        "correct_seq": [2, 4, 3, 1],
        "details_en": "2. Office of Accountant General created (1858)\n4. Sir Edward Drummond appointed first Auditor General (1860)\n3. Auditor General made statutory under 1919 Act (1919)\n1. Statutory independence under Government of India Act 1935 (1935)",
        "details_ta": "2. கணக்குத் தலைவர் அலுவலகம் உருவாக்கப்படுதல் (1858)\n4. சர் எட்வர்ட் டிரம்மாண்ட் முதல் தணிக்கைத் தலைவராக நியமிக்கப்படுதல் (1860)\n3. 1919 சட்டத்தின் கீழ் சட்டப்பூர்வமாக்கப்படுதல் (1919)\n1. 1935 இந்திய அரசுச் சட்டத்தின் கீழ் தன்னாட்சி பெறுதல் (1935)",
        "tip_en": "1858: Office created; 1860: First Auditor General; 1919: Montagu-Chelmsford Act; 1935: GoI Act.",
        "tip_ta": "1858: அலுவலகம் உருவாக்கம்; 1860: முதல் தணிக்கைத் தலைவர்; 1919: மான்டேகு சட்டம்; 1935: இந்திய அரசுச் சட்டம்.",
        "fact_en": "The 1935 Act mandated appointment of the Auditor General under the Royal sign manual.",
        "fact_ta": "1935 சட்டம் பிரிட்டிஷ் மன்னரின் நேரடி முத்திரையின் கீழ் நியமனம் செய்ய வகைசெய்தது."
    },
    # 4
    {
        "subtopic": "Post-Independence Legislative Milestones",
        "intro_en": "Arrange the following legislative and administrative milestones concerning the CAG in chronological order:",
        "intro_ta": "சி.ஏ.ஜி தொடர்பான பின்வரும் சட்ட மற்றும் நிர்வாக மைல்கற்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events_en": [
            "Enactment of the Comptroller and Auditor General's (DPC) Act",
            "Commencement of the Constitution of India establishing Article 148",
            "Promulgation of the Regulations on Audit and Accounts under Section 23",
            "Separation of accounting from audit at the Union level through DPC Amendment"
        ],
        "events_ta": [
            "தலைமைத் தணிக்கையாளர் (DPC) சட்டம் நாடாளுமன்றத்தால் இயற்றப்படுதல்",
            "சரத்து 148-ஐ நிறுவிய இந்திய அரசியலமைப்பு நடைமுறைக்கு வருதல்",
            "பிரிவு 23-ன் கீழ் தணிக்கை மற்றும் கணக்குகள் ஒழுங்குமுறைகள் வெளியிடப்படுதல்",
            "DPC திருத்தத்தின் மூலம் மத்திய அளவில் தணிக்கையிலிருந்து கணக்கு பிரிக்கப்படுதல்"
        ],
        # Order: 2 (1950) -> 1 (1971) -> 4 (1976) -> 3 (2007)
        "correct_seq": [2, 1, 4, 3],
        "details_en": "2. Constitution establishes Article 148 (1950)\n1. Enactment of CAG (DPC) Act (1971)\n4. Separation of accounts and audit at Union (1976)\n3. Regulations on Audit and Accounts promulgated (2007)",
        "details_ta": "2. அரசியலமைப்பு சரத்து 148 தொடக்கம் (1950)\n1. சி.ஏ.ஜி (DPC) சட்டம் இயற்றப்படுதல் (1971)\n4. மத்திய அளவில் கணக்கு மற்றும் தணிக்கைப் பிரிப்பு (1976)\n3. தணிக்கை மற்றும் கணக்குகள் ஒழுங்குமுறைகள் (2007)",
        "tip_en": "1950: Constitution; 1971: DPC Act; 1976: Separation of accounts; 2007: Audit regulations.",
        "tip_ta": "1950: அரசியலமைப்பு; 1971: DPC சட்டம்; 1976: கணக்குப் பிரிப்பு; 2007: தணிக்கை ஒழுங்குமுறைகள்.",
        "fact_en": "The Regulations on Audit and Accounts were further updated and strengthened in 2020.",
        "fact_ta": "தணிக்கை மற்றும் கணக்குகள் ஒழுங்குமுறைகள் 2020-ல் மேலும் புதுப்பிக்கப்பட்டன."
    },
    # 5
    {
        "subtopic": "Evolution of Audit Scope",
        "intro_en": "Arrange the following developments in the audit jurisdiction of the CAG in chronological order:",
        "intro_ta": "சி.ஏ.ஜியின் தணிக்கை அதிகார வரம்பில் ஏற்பட்ட பின்வரும் முன்னேற்றங்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events_en": [
            "Supreme Court upholds CAG audit of private telecom revenue share (AUTSPI case)",
            "Audit of Government Companies institutionalized under Companies Act 1956",
            "Eleventh Finance Commission recommends Technical Guidance and Supervision (TGS) for Local Bodies",
            "Statutory threshold for audit of substantially financed autonomous bodies fixed under Section 14"
        ],
        "events_ta": [
            "தனியார் தொலைத்தொடர்பு வருவாய்ப் பகிர்வை சி.ஏ.ஜி தணிக்கை செய்வதை உச்ச நீதிமன்றம் உறுதி செய்தல் (AUTSPI வழக்கு)",
            "நிறுவனங்கள் சட்டம் 1956-ன் கீழ் அரசு நிறுவனங்களின் தணிக்கை முறைப்படுத்தப்படுதல்",
            "உள்ளாட்சி அமைப்புகளுக்கான தொழில்நுட்ப வழிகாட்டுதல் மற்றும் மேற்பார்வையை (TGS) 11வது நிதி ஆணையம் பரிந்துரைத்தல்",
            "பிரிவு 14-ன் கீழ் தன்னாட்சி அமைப்புகளின் தணிக்கைக்கான சட்டப்பூர்வ வரம்பு நிர்ணயிக்கப்படுதல்"
        ],
        # Order: 2 (1956) -> 4 (1971) -> 3 (2000) -> 1 (2014)
        "correct_seq": [2, 4, 3, 1],
        "details_en": "2. Government Companies audit under Companies Act (1956)\n4. Section 14 autonomous bodies threshold enacted (1971)\n3. 11th Finance Commission recommends TGS for local bodies (2000)\n1. Supreme Court AUTSPI telecom revenue audit ruling (2014)",
        "details_ta": "2. நிறுவனங்கள் சட்டம் அரசு நிறுவன தணிக்கை (1956)\n4. பிரிவு 14 தன்னாட்சி அமைப்புகள் வரம்பு சட்டம் (1971)\n3. 11வது நிதி ஆணைய TGS பரிந்துரை (2000)\n1. உச்ச நீதிமன்ற தொலைத்தொடர்பு தணிக்கை தீர்ப்பு (2014)",
        "tip_en": "1956: PSUs under Companies Act; 1971: Sec 14; 2000: Local bodies TGS; 2014: Telecom audit.",
        "tip_ta": "1956: பொதுத்துறை தணிக்கை; 1971: பிரிவு 14; 2000: உள்ளாட்சி TGS; 2014: தொலைத்தொடர்பு தீர்ப்பு.",
        "fact_en": "The 2014 telecom ruling expanded CAG scrutiny to revenue-sharing private natural resource concessionaires.",
        "fact_ta": "2014 தீர்ப்பு இயற்கை வளங்களை வருவாய் பகிர்வு முறையில் பயன்படுத்தும் தனியார் நிறுவனங்களை சி.ஏ.ஜி தணிக்கைக்கு உட்படுத்தியது."
    },
    # 6
    {
        "subtopic": "Constitutional Amendments Affecting CAG",
        "intro_en": "Arrange the following Constitutional Amendments affecting the functions of the CAG in chronological order:",
        "intro_ta": "சி.ஏ.ஜியின் பணிகளைப் பாதித்த பின்வரும் அரசியலமைப்புத் திருத்தங்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events_en": [
            "44th Amendment modifying Article 150 wording to 'on the advice of the CAG'",
            "42nd Amendment altering Article 150 regarding prescription of accounting form",
            "101st Amendment introducing GST requiring new audit of IGST and ITC",
            "73rd Amendment empowering state legislatures to direct panchayat audit"
        ],
        "events_ta": [
            "சரத்து 150-ல் 'சி.ஏ.ஜியின் ஆலோசனையின் பேரில்' என மாற்றியமைத்த 44வது திருத்தம்",
            "கணக்குப் படிவம் நிர்ணயிப்பது தொடர்பான சரத்து 150-ஐ மாற்றிய 42வது திருத்தம்",
            "IGST மற்றும் ITC புதிய தணிக்கை முறையை ஏற்படுத்திய 101வது ஜி.எஸ்.டி திருத்தம்",
            "பஞ்சாயத்து கணக்குத் தணிக்கைக்கு வழிவகுத்த 73வது அரசியலமைப்புத் திருத்தம்"
        ],
        # Order: 2 (1976) -> 1 (1978) -> 4 (1992) -> 3 (2016)
        "correct_seq": [2, 1, 4, 3],
        "details_en": "2. 42nd Amendment modifies Article 150 (1976)\n1. 44th Amendment finalizes 'on the advice of CAG' (1978)\n4. 73rd Amendment introduces local body audit framework (1992)\n3. 101st Amendment introduces GST audit architecture (2016)",
        "details_ta": "2. 42வது திருத்தம் சரத்து 150 மாற்றம் (1976)\n1. 44வது திருத்தம் 'சி.ஏ.ஜி ஆலோசனையின் பேரில்' என இறுதி செய்தல் (1978)\n4. 73வது திருத்தம் உள்ளாட்சி தணிக்கை கட்டமைப்பு (1992)\n3. 101வது திருத்தம் ஜி.எஸ்.டி தணிக்கை அறிமுகம் (2016)",
        "tip_en": "1976: 42nd Amdt; 1978: 44th Amdt; 1992: 73rd Amdt; 2016: 101st GST Amdt.",
        "tip_ta": "1976: 42வது திருத்தம்; 1978: 44வது திருத்தம்; 1992: 73வது திருத்தம்; 2016: 101வது ஜிஎஸ்டி திருத்தம்.",
        "fact_en": "Article 150 was amended twice within two years (1976 and 1978).",
        "fact_ta": "சரத்து 150 இரண்டு ஆண்டுகளுக்குள் இரண்டு முறை திருத்தப்பட்டது (1976 மற்றும் 1978)."
    },
    # 7
    {
        "subtopic": "CAG Tenures in 1970s and 1980s",
        "intro_en": "Arrange the following Comptrollers and Auditors General of India in chronological order of their assumption of office:",
        "intro_ta": "இந்தியாவின் பின்வரும் தலைமைத் தணிக்கையாளர்களை அவர்கள் பதவியேற்ற காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events_en": [
            "T.N. Chaturvedi assumes office as CAG",
            "A. Baksi assumes office as CAG",
            "C.G. Somiah assumes office as CAG",
            "Gian Prakash assumes office as CAG"
        ],
        "events_ta": [
            "டி.என். சதுர்வேதி சி.ஏ.ஜியாகப் பொறுப்பேற்றல்",
            "ஏ. பக்ஷி சி.ஏ.ஜியாகப் பொறுப்பேற்றல்",
            "சி.ஜி. சோமையா சி.ஏ.ஜியாகப் பொறுப்பேற்றல்",
            "கியான் பிரகாஷ் சி.ஏ.ஜியாகப் பொறுப்பேற்றல்"
        ],
        # Order: 2 (1972) -> 4 (1978) -> 1 (1984) -> 3 (1990)
        "correct_seq": [2, 4, 1, 3],
        "details_en": "2. A. Baksi (1972)\n4. Gian Prakash (1978)\n1. T.N. Chaturvedi (1984)\n3. C.G. Somiah (1990)",
        "details_ta": "2. ஏ. பக்ஷி (1972)\n4. கியான் பிரகாஷ் (1978)\n1. டி.என். சதுர்வேதி (1984)\n3. சி.ஜி. சோமையா (1990)",
        "tip_en": "T.N. Chaturvedi (1984-1990) submitted the historic Bofors audit report in 1989.",
        "tip_ta": "டி.என். சதுர்வேதி (1984-1990) 1989-ல் வரலாற்று சிறப்புமிக்க போஃபோர்ஸ் தணிக்கை அறிக்கையை சமர்ப்பித்தார்.",
        "fact_en": "T.N. Chaturvedi later served as Governor of Karnataka (2002-2007).",
        "fact_ta": "டி.என். சதுர்வேதி பின்னர் கர்நாடக ஆளுநராகப் பணியாற்றினார் (2002-2007)."
    },
    # 8
    {
        "subtopic": "CAG Tenures in 1990s and 2000s",
        "intro_en": "Arrange the following Comptrollers and Auditors General of India in chronological order of their assumption of office:",
        "intro_ta": "இந்தியாவின் பின்வரும் தலைமைத் தணிக்கையாளர்களை அவர்கள் பதவியேற்ற காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events_en": [
            "V.N. Kaul appointed as CAG",
            "C.G. Somiah appointed as CAG",
            "Vinod Rai appointed as CAG",
            "V.K. Shunglu appointed as CAG"
        ],
        "events_ta": [
            "வி.என். கவுல் சி.ஏ.ஜியாக நியமிக்கப்படுதல்",
            "சி.ஜி. சோமையா சி.ஏ.ஜியாக நியமிக்கப்படுதல்",
            "வினோத் ராய் சி.ஏ.ஜியாக நியமிக்கப்படுதல்",
            "வி.கே. ஷுங்லு சி.ஏ.ஜியாக நியமிக்கப்படுதல்"
        ],
        # Order: 2 (1990) -> 4 (1996) -> 1 (2002) -> 3 (2008)
        "correct_seq": [2, 4, 1, 3],
        "details_en": "2. C.G. Somiah (1990)\n4. V.K. Shunglu (1996)\n1. V.N. Kaul (2002)\n3. Vinod Rai (2008)",
        "details_ta": "2. சி.ஜி. சோமையா (1990)\n4. வி.கே. ஷுங்லு (1996)\n1. வி.என். கவுல் (2002)\n3. வினோத் ராய் (2008)",
        "tip_en": "1990: Somiah; 1996: Shunglu; 2002: Kaul; 2008: Vinod Rai.",
        "tip_ta": "1990: சோமையா; 1996: ஷுங்லு; 2002: கவுல்; 2008: வினோத் ராய்.",
        "fact_en": "V.K. Shunglu subsequently headed the high-level committee investigating 2010 Commonwealth Games irregularities.",
        "fact_ta": "வி.கே. ஷுங்லு பின்னர் 2010 காமன்வெல்த் போட்டி முறைகேடுகளை விசாரித்த உயர் மட்டக் குழுவின் தலைவராக இருந்தார்."
    },
    # 9
    {
        "subtopic": "Historic Audit Reports that Impacted Polity",
        "intro_en": "Arrange the following historic CAG audit reports that impacted Indian governance in chronological order:",
        "intro_ta": "இந்திய ஆட்சி முறையில் தாக்கத்தை ஏற்படுத்திய பின்வரும் வரலாற்று சிறப்புமிக்க சி.ஏ.ஜி தணிக்கை அறிக்கைகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events_en": [
            "CAG Audit Report on 2G Spectrum Allocation tabled in Parliament",
            "Jeep Scandal audit scrutiny by early audit machinery",
            "CAG Performance Audit on 155mm Bofors Gun purchase tabled",
            "Mundhra Affair involving LIC investments highlighted in audit findings"
        ],
        "events_ta": [
            "2G அலைக்கற்றை ஒதுக்கீடு மீதான சி.ஏ.ஜி தணிக்கை அறிக்கை நாடாளுமன்றத்தில் வைக்கப்படுதல்",
            "ஜீப் ஊழல் மீதான ஆரம்பகால தணிக்கை ஆய்வு",
            "155மிமீ போஃபோர்ஸ் பீரங்கி கொள்முதல் மீதான சி.ஏ.ஜி செயல்திறன் தணிக்கை அறிக்கை சமர்ப்பிக்கப்படுதல்",
            "எல்.ஐ.சி முதலீடுகள் தொடர்பான முந்த்ரா விவகாரம் தணிக்கைக் குறிப்புகளில் வெளிப்படுதல்"
        ],
        # Order: 2 (1951) -> 4 (1957) -> 3 (1989) -> 1 (2010)
        "correct_seq": [2, 4, 3, 1],
        "details_en": "2. Jeep Scandal scrutiny (1951)\n4. Mundhra affair audit findings (1957)\n3. Bofors gun purchase audit report (1989)\n1. 2G spectrum allocation audit report (2010)",
        "details_ta": "2. ஜீப் ஒப்பந்த ஆய்வு (1951)\n4. முந்த்ரா எல்.ஐ.சி விவகாரம் (1957)\n3. போஃபோர்ஸ் பீரங்கி தணிக்கை அறிக்கை (1989)\n1. 2G அலைக்கற்றை தணிக்கை அறிக்கை (2010)",
        "tip_en": "1951: Jeep Scandal; 1957: Mundhra LIC; 1989: Bofors; 2010: 2G Spectrum.",
        "tip_ta": "1951: ஜீப் ஊழல்; 1957: முந்த்ரா விவகாரம்; 1989: போஃபோர்ஸ்; 2010: 2G அலைக்கற்றை.",
        "fact_en": "The Mundhra affair led to the resignation of Finance Minister T.T. Krishnamachari in 1958.",
        "fact_ta": "முந்த்ரா விவகாரம் 1958-ல் நிதி அமைச்சர் டி.டி. கிருஷ்ணமாச்சாரி ராஜினாமா செய்ய வழிவகுத்தது."
    },
    # 10
    {
        "subtopic": "Disinvestment and Major Resource Audits",
        "intro_en": "Arrange the following major resource allocation and disinvestment audits by the CAG in chronological order:",
        "intro_ta": "சி.ஏ.ஜியின் பின்வரும் முக்கிய வள ஒதுக்கீடு மற்றும் பங்கு விலக்கல் தணிக்கைகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events_en": [
            "CAG Performance Audit on Allocation of Coal Blocks and Augmentation of Coal Production",
            "BALCO Strategic Disinvestment Performance Audit Report",
            "CAG Performance Audit Report on Capital Acquisition in the Indian Air Force (Rafale)",
            "Commonwealth Games Delhi 2011 Mega Infrastructure Audit Report"
        ],
        "events_ta": [
            "நிலக்கரி சுரங்க ஒதுக்கீடு மீதான சி.ஏ.ஜி செயல்திறன் தணிக்கை அறிக்கை",
            "பால்கோ (BALCO) நிறுவன பங்கு விலக்கல் மீதான தணிக்கை அறிக்கை",
            "இந்திய விமானப்படை மூலதனக் கொள்முதல் (ரஃபேல்) மீதான சி.ஏ.ஜி தணிக்கை அறிக்கை",
            "காமன்வெல்த் விளையாட்டுப் போட்டிகள் உள்கட்டமைப்பு தணிக்கை அறிக்கை"
        ],
        # Order: 2 (2001) -> 4 (2011) -> 1 (2012) -> 3 (2019)
        "correct_seq": [2, 4, 1, 3],
        "details_en": "2. BALCO Disinvestment Audit (2001)\n4. Commonwealth Games Audit (2011)\n1. Coal Block Allocation Audit (2012)\n3. Rafale Capital Acquisition Audit (2019)",
        "details_ta": "2. பால்கோ பங்கு விலக்கல் தணிக்கை (2001)\n4. காமன்வெல்த் போட்டி உள்கட்டமைப்பு தணிக்கை (2011)\n1. நிலக்கரி சுரங்க ஒதுக்கீடு தணிக்கை (2012)\n3. ரஃபேல் கொள்முதல் தணிக்கை (2019)",
        "tip_en": "2001: BALCO; 2011: CWG; 2012: Coal Blocks; 2019: Rafale.",
        "tip_ta": "2001: பால்கோ; 2011: காமன்வெல்த்; 2012: நிலக்கரி; 2019: ரஃபேல்.",
        "fact_en": "The Coal block allocation audit estimated a potential financial gain of Rs. 1.86 lakh crore to private allocatees.",
        "fact_ta": "நிலக்கரி சுரங்க தணிக்கை தனியார் நிறுவனங்களுக்கு ரூ. 1.86 லட்சம் கோடி நிதி ஆதாயம் கிடைத்ததாக மதிப்பிட்டது."
    },
    # 11
    {
        "subtopic": "International Audit Milestones of Indian CAG",
        "intro_en": "Arrange the following international audit leadership milestones involving the CAG of India in chronological order:",
        "intro_ta": "இந்திய சி.ஏ.ஜி சம்பந்தப்பட்ட பின்வரும் சர்வதேச தணிக்கைத் தலைமை மைல்கற்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events_en": [
            "CAG elected External Auditor of the World Health Organization (WHO)",
            "Founding of INTOSAI (International Organization of Supreme Audit Institutions)",
            "Establishment of ASOSAI (Asian Organization of Supreme Audit Institutions)",
            "CAG appointed Chairman of the United Nations Board of Auditors for the 1993 session"
        ],
        "events_ta": [
            "உலக சுகாதார நிறுவனத்தின் (WHO) வெளித் தணிக்கையாளராக சி.ஏ.ஜி தேர்ந்தெடுக்கப்படுதல்",
            "INTOSAI சர்வதேச உச்ச தணிக்கை அமைப்புகள் கூட்டமைப்பு நிறுவப்படுதல்",
            "ASOSAI ஆசிய உச்ச தணிக்கை அமைப்புகள் கூட்டமைப்பு நிறுவப்படுதல்",
            "1993 கூட்டத்தொடருக்கு ஐ.நா தணிக்கையாளர் வாரியத்தின் தலைவராக இந்திய சி.ஏ.ஜி நியமிக்கப்படுதல்"
        ],
        # Order: 2 (1953) -> 3 (1979) -> 4 (1993) -> 1 (2020)
        "correct_seq": [2, 3, 4, 1],
        "details_en": "2. Founding of INTOSAI (1953)\n3. Establishment of ASOSAI (1979)\n4. CAG becomes UN Board of Auditors Chairman (1993)\n1. CAG elected External Auditor of WHO (2020)",
        "details_ta": "2. INTOSAI தோற்றம் (1953)\n3. ASOSAI தொடக்கம் (1979)\n4. ஐ.நா தணிக்கை வாரியத் தலைவராக சி.ஏ.ஜி (1993)\n1. WHO வெளித் தணிக்கையாளராக சி.ஏ.ஜி தேர்வு (2020)",
        "tip_en": "1953: INTOSAI; 1979: ASOSAI; 1993: UN Board of Auditors Chair; 2020: WHO External Auditor.",
        "tip_ta": "1953: INTOSAI; 1979: ASOSAI; 1993: ஐ.நா தணிக்கை வாரியம்; 2020: WHO வெளித் தணிக்கையாளர்.",
        "fact_en": "CAG GC Murmu was re-elected as WHO External Auditor for 2024-2027.",
        "fact_ta": "சி.ஏ.ஜி ஜி.சி. முர்மு 2024-2027 காலகட்டத்திற்கும் WHO வெளித் தணிக்கையாளராக மீண்டும் தேர்ந்தெடுக்கப்பட்டார்."
    },
    # 12
    {
        "subtopic": "Modern Audit Initiatives & Centres",
        "intro_en": "Arrange the following institutional modernization initiatives by the CAG in chronological order:",
        "intro_ta": "சி.ஏ.ஜியின் பின்வரும் நிறுவன நவீனமயமாக்கல் முயற்சிகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events_en": [
            "Full nationwide deployment of One IA&AD One System (OIOS)",
            "Inauguration of International Centre for Environment Audit (iCED) in Jaipur",
            "CAG of India assumes Chairmanship of ASOSAI during 16th Assembly in New Delhi",
            "Establishment of Centre for Data Management and Analytics (CDMA)"
        ],
        "events_ta": [
            "One IA&AD One System (OIOS) தளம் நாடு முழுவதும் முழுமையாக செயல்படுத்தப்படுதல்",
            "ஜெய்ப்பூரில் சுற்றுச்சூழல் தணிக்கை சர்வதேச மையம் (iCED) தொடங்கப்படுதல்",
            "புது தில்லியில் 16வது பொதுக்குழுவில் ASOSAI அமைப்பின் தலைவராக இந்திய சி.ஏ.ஜி பொறுப்பேற்றல்",
            "தரவு மேலாண்மை மற்றும் பகுப்பாய்வு மையம் (CDMA) அமைக்கப்படுதல்"
        ],
        # Order: 2 (2013) -> 4 (2016) -> 1 (2020) -> 3 (2024)
        "correct_seq": [2, 4, 1, 3],
        "details_en": "2. iCED inaugurated in Jaipur (2013)\n4. CDMA established for Big Data (2016)\n1. OIOS nationwide rollout (2020)\n3. ASOSAI Chairmanship assumed in New Delhi (2024)",
        "details_ta": "2. ஜெய்ப்பூர் iCED மையம் தொடக்கம் (2013)\n4. பெருந்தரவு CDMA மையம் அமைப்பு (2016)\n1. OIOS தளம் நாடு தழுவிய அறிமுகம் (2020)\n3. புது தில்லியில் ASOSAI தலைவர் பொறுப்பேற்பு (2024)",
        "tip_en": "2013: iCED Jaipur; 2016: CDMA; 2020: OIOS; 2024: ASOSAI Chairmanship.",
        "tip_ta": "2013: iCED ஜெய்ப்பூர்; 2016: CDMA; 2020: OIOS; 2024: ASOSAI தலைவர்.",
        "fact_en": "In September 2024, India hosted 48 SAI delegates at the 16th ASOSAI Assembly.",
        "fact_ta": "செப்டம்பர் 2024-ல் 16வது ASOSAI கூட்டத்தில் 48 தணிக்கை அமைப்புகளின் பிரதிநிதிகளை இந்தியா நடத்தியது."
    },
    # 13
    {
        "subtopic": "Evolution of Parliamentary Financial Committees",
        "intro_en": "Arrange the following milestones in the evolution of parliamentary financial committees linked with the CAG in chronological order:",
        "intro_ta": "சி.ஏ.ஜியுடன் தொடர்புடைய நாடாளுமன்ற நிதிக் குழுக்களின் வளர்ச்சியில் உள்ள பின்வரும் மைல்கற்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events_en": [
            "Formal constitution of the Committee on Public Undertakings (COPU)",
            "Public Accounts Committee (PAC) first established under Government of India Act 1919",
            "Krishna Menon Committee recommends creation of a dedicated committee for public enterprises",
            "PAC becomes a parliamentary committee under the Speaker in independent India"
        ],
        "events_ta": [
            "பொதுத்துறை நிறுவனங்களுக்கான நாடாளுமன்றக் குழு (COPU) அதிகாரப்பூர்வமாக அமைக்கப்படுதல்",
            "1919 இந்திய அரசுச் சட்டத்தின் கீழ் பொதுக் கணக்குக் குழு (PAC) முதன்முதலில் அமைக்கப்படுதல்",
            "பொதுத்துறை நிறுவனங்களுக்காக பிரத்யேகக் குழுவை அமைக்க கிருஷ்ண மேனன் குழு பரிந்துரைத்தல்",
            "சுதந்திர இந்தியாவில் மக்களவைத் தலைவரின் கீழ் PAC ஒரு நாடாளுமன்றக் குழுவாக மாறுதல்"
        ],
        # Order: 2 (1921) -> 4 (1950) -> 3 (1959) -> 1 (1964)
        "correct_seq": [2, 4, 3, 1],
        "details_en": "2. PAC established under 1919 Act (1921)\n4. PAC becomes parliamentary committee under Speaker (1950)\n3. Krishna Menon Committee report (1959)\n1. Formal constitution of COPU (1964)",
        "details_ta": "2. 1919 சட்டத்தின் கீழ் PAC அமைப்பு (1921)\n4. சபாநாயகரின் கீழ் நாடாளுமன்றக் குழுவாக PAC மாறுதல் (1950)\n3. கிருஷ்ண மேனன் குழு அறிக்கை (1959)\n1. COPU குழு அதிகாரப்பூர்வ அமைப்பு (1964)",
        "tip_en": "1921: PAC born; 1950: Modern PAC under Speaker; 1959: Krishna Menon; 1964: COPU born.",
        "tip_ta": "1921: PAC தோற்றம்; 1950: சபாநாயகரின் கீழ் நவீன PAC; 1959: கிருஷ்ண மேனன் குழு; 1964: COPU தோற்றம்.",
        "fact_en": "PAC celebrated its centenary in 2021, marking 100 years of financial oversight.",
        "fact_ta": "பொதுக் கணக்குக் குழு 2021-ல் தனது நூற்றாண்டு விழாவைக் கொண்டாடியது."
    },
    # 14
    {
        "subtopic": "PAC Conventions and Milestones",
        "intro_en": "Arrange the following key conventions and events regarding the Public Accounts Committee in chronological order:",
        "intro_ta": "பொதுக் கணக்குக் குழு தொடர்பான பின்வரும் முக்கிய மரபுகள் மற்றும் நிகழ்வுகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events_en": [
            "Celebration of the Centenary of Public Accounts Committee in Central Hall of Parliament",
            "B. Das becomes the first Chairman of PAC in independent India",
            "Diamond Jubilee celebration of Public Accounts Committee",
            "Convention established of appointing a prominent Opposition member as PAC Chairman"
        ],
        "events_ta": [
            "நாடாளுமன்ற மத்திய மண்டபத்தில் பொதுக் கணக்குக் குழுவின் நூற்றாண்டு விழா கொண்டாடப்படுதல்",
            "சுதந்திர இந்தியாவின் முதல் PAC தலைவராக பி. தாஸ் பொறுப்பேற்றல்",
            "பொதுக் கணக்குக் குழுவின் வைர விழா கொண்டாடப்படுதல்",
            "முக்கிய எதிர்க்கட்சி உறுப்பினர் ஒருவரை PAC தலைவராக நியமிக்கும் மரபு நிலைநாட்டப்படுதல்"
        ],
        # Order: 2 (1950) -> 4 (1967) -> 3 (1981) -> 1 (2021)
        "correct_seq": [2, 4, 3, 1],
        "details_en": "2. B. Das becomes first PAC Chairman (1950)\n4. Opposition Chairman convention established (1967)\n3. PAC Diamond Jubilee celebrated (1981)\n1. PAC Centenary celebrated (2021)",
        "details_ta": "2. பி. தாஸ் முதல் PAC தலைவர் (1950)\n4. எதிர்க்கட்சித் தலைவர் நியமன மரபு நிலைநாட்டப்படுதல் (1967)\n3. PAC வைர விழா கொண்டாட்டம் (1981)\n1. PAC நூற்றாண்டு விழா கொண்டாட்டம் (2021)",
        "tip_en": "1950: B. Das; 1967: Minoo Masani becomes first Opposition PAC Chairman; 1981: Diamond Jubilee; 2021: Centenary.",
        "tip_ta": "1950: பி. தாஸ்; 1967: மினு மசானி முதல் எதிர்க்கட்சித் தலைவர்; 1981: வைர விழா; 2021: நூற்றாண்டு விழா.",
        "fact_en": "Minoo Masani of the Swatantra Party was the first Opposition leader to chair PAC in 1967.",
        "fact_ta": "சுதந்திரா கட்சியின் மினூ மசானி 1967-ல் முதல் எதிர்க்கட்சி PAC தலைவரானார்."
    },
    # 15
    {
        "subtopic": "State Accounts Milestones",
        "intro_en": "Arrange the following milestones in State accounts and treasury management by the CAG in chronological order:",
        "intro_ta": "சி.ஏ.ஜியின் மாநில கணக்குகள் மற்றும் கருவூல மேலாண்மையில் உள்ள பின்வரும் மைல்கற்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events_en": [
            "Rollout of Voucher Level Computerisation (VLC) across state Accountant General offices",
            "CAG relieved of Union accounting duties under 1976 DPC Amendment while retaining State accounts",
            "Goa separates state accounts compilation from the CAG through Section 10 notification",
            "Integration of State VLC systems with Public Financial Management System (PFMS)"
        ],
        "events_ta": [
            "மாநில கணக்குத் தலைவர் அலுவலகங்களில் வவுச்சர் அளவிலான கணினிமயமாக்கல் (VLC) அறிமுகப்படுத்தப்படுதல்",
            "1976 DPC திருத்தத்தின் கீழ் மாநில கணக்குகளைத் தக்கவைத்துக்கொண்டு மத்திய கணக்கிலிருந்து சி.ஏ.ஜி விடுவிக்கப்படுதல்",
            "பிரிவு 10 அறிவிக்கையின் மூலம் கோவா மாநில கணக்குத் தொகுப்பை சி.ஏ.ஜியிடமிருந்து பிரித்தல்",
            "மாநில VLC அமைப்புகள் பொது நிதி மேலாண்மை அமைப்புடன் (PFMS) ஒருங்கிணைக்கப்படுதல்"
        ],
        # Order: 2 (1976) -> 3 (1987) -> 1 (2004) -> 4 (2018)
        "correct_seq": [2, 3, 1, 4],
        "details_en": "2. 1976 DPC Amendment retains State accounts with CAG (1976)\n3. Goa separates state accounts (1987)\n1. VLC rolled out across State AG offices (2004)\n4. VLC integrated with PFMS platform (2018)",
        "details_ta": "2. 1976 சட்டம் மாநில கணக்குகளை சி.ஏ.ஜியிடம் தக்கவைத்தல் (1976)\n3. கோவா மாநில கணக்குப் பிரிப்பு (1987)\n1. மாநில AG அலுவலகங்களில் VLC அறிமுகம் (2004)\n4. PFMS தளத்துடன் VLC இணைப்பு (2018)",
        "tip_en": "1976: Separation at Union; 1987: Goa separation; 2004: VLC system; 2018: PFMS integration.",
        "tip_ta": "1976: மத்திய பிரிப்பு; 1987: கோவா பிரிப்பு; 2004: VLC அமைப்பு; 2018: PFMS இணைப்பு.",
        "fact_en": "Goa and Puducherry are rare exceptions where state/UT accounts are separated from CAG.",
        "fact_ta": "கோவா மற்றும் புதுச்சேரி கணக்குகள் சி.ஏ.ஜியிடமிருந்து பிரிக்கப்பட்ட அரிய விதிவிலக்குகளாகும்."
    },
    # 16
    {
        "subtopic": "Drafting of Articles 148-151",
        "intro_en": "Arrange the following steps in the constitutional drafting of Articles 148 to 151 in chronological order:",
        "intro_ta": "சரத்துகள் 148 முதல் 151 வரையிலான அரசியலமைப்பு வரைவுப் பணிகளின் பின்வரும் படிகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events_en": [
            "Constituent Assembly debates and adopts provisions establishing the Comptroller and Auditor General",
            "Publication of Draft Constitution containing Article 124 regarding the Auditor General",
            "Notification of the Indian Audit and Accounts Department (Administrative Powers) Rules",
            "Commencement of the Constitution of India bringing Articles 148 to 151 into legal effect"
        ],
        "events_ta": [
            "தலைமைத் தணிக்கையாளரை நிறுவும் விதிகளை அரசியலமைப்பு நிர்ணய சபை விவாதித்து ஏற்றுக்கொள்வது",
            "தணிக்கைத் தலைவர் தொடர்பான சரத்து 124-ஐக் கொண்ட வரைவு அரசியலமைப்பு வெளியிடப்படுதல்",
            "இந்திய தணிக்கை மற்றும் கணக்குத் துறை (நிர்வாக அதிகாரங்கள்) விதிகள் அறிவிக்கப்படுதல்",
            "இந்திய அரசியலமைப்பு நடைமுறைக்கு வந்து சரத்துகள் 148 முதல் 151 வரை சட்டப்பூர்வ அமலுக்கு வருதல்"
        ],
        # Order: 2 (1948) -> 1 (1949) -> 4 (1950) -> 3 (1959)
        "correct_seq": [2, 1, 4, 3],
        "details_en": "2. Draft Constitution published (1948)\n1. Constituent Assembly adopts CAG provisions (1949)\n4. Constitution commences on 26 January (1950)\n3. IA&AD administrative rules notified under Article 148(5) (1959)",
        "details_ta": "2. வரைவு அரசியலமைப்பு வெளியீடு (1948)\n1. நிர்ணய சபை சி.ஏ.ஜி விதிகளை ஏற்றல் (1949)\n4. ஜனவரி 26 அரசியலமைப்பு தொடக்கம் (1950)\n3. சரத்து 148(5) கீழ் IA&AD விதிகள் அறிவிப்பு (1959)",
        "tip_en": "1948: Draft Constitution; 1949: Constituent Assembly adoption; 1950: Enactment; 1959: Service rules.",
        "tip_ta": "1948: வரைவு அரசியலமைப்பு; 1949: நிர்ணய சபை ஏற்பு; 1950: அரசியலமைப்பு தொடக்கம்; 1959: சேவை விதிகள்.",
        "fact_en": "In May 1949, the Assembly adopted the change of designation from 'Auditor-General' to 'Comptroller and Auditor-General'.",
        "fact_ta": "மே 1949-ல் 'தணிக்கைத் தலைவர்' என்ற பதவியை 'தலைமை கணக்குத் தணிக்கையாளர்' என மாற்ற நிர்ணய சபை ஒப்புக்கொண்டது."
    },
    # 17
    {
        "subtopic": "Judicial Precedents on Public Accountability",
        "intro_en": "Arrange the following landmark Supreme Court cases affirming financial accountability and public trust in chronological order:",
        "intro_ta": "நிதிப் பொறுப்புடைமை மற்றும் பொது அறக்கட்டளையை உறுதிப்படுத்திய பின்வரும் உச்ச நீதிமன்ற முக்கிய வழக்குகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events_en": [
            "Centre for Public Interest Litigation v. Union of India (2G spectrum cancellation citing audit findings)",
            "Ramana Dayaram Shetty v. International Airport Authority (Government contract transparency)",
            "Association of Unified Telecom Service Providers v. Union of India (CAG revenue audit of private licensees)",
            "S.R. Bommai v. Union of India (Strict financial federalism and governance accountability principles)"
        ],
        "events_ta": [
            "பொது நல வழக்கு மையம் எதிர் இந்திய யூனியன் (தணிக்கை அடிப்படையில் 2G அலைக்கற்றை ரத்து)",
            "ரமணா தயாராம் ஷெட்டி எதிர் சர்வதேச விமான நிலைய ஆணையம் (அரசு ஒப்பந்த வெளிப்படைத்தன்மை)",
            "ஒருங்கிணைந்த தொலைத்தொடர்பு சேவை வழங்குநர்கள் சங்கம் எதிர் இந்திய யூனியன் (சி.ஏ.ஜி தொலைத்தொடர்பு தணிக்கை)",
            "எஸ்.ஆர். பொம்மை எதிர் இந்திய யூனியன் (கடுமையான நிதி கூட்டாட்சி மற்றும் பொறுப்புடைமை கோட்பாடுகள்)"
        ],
        # Order: 2 (1979) -> 4 (1994) -> 1 (2012) -> 3 (2014)
        "correct_seq": [2, 4, 1, 3],
        "details_en": "2. Ramana Dayaram Shetty case (1979)\n4. S.R. Bommai ruling (1994)\n1. 2G spectrum judgment (2012)\n3. AUTSPI CAG telecom audit judgment (2014)",
        "details_ta": "2. ரமணா தயாராம் ஷெட்டி வழக்கு (1979)\n4. எஸ்.ஆர். பொம்மை தீர்ப்பு (1994)\n1. 2G அலைக்கற்றை தீர்ப்பு (2012)\n3. AUTSPI சி.ஏ.ஜி தொலைத்தொடர்பு தணிக்கை தீர்ப்பு (2014)",
        "tip_en": "1979: Ramana Shetty; 1994: SR Bommai; 2012: 2G Spectrum; 2014: AUTSPI Telecom.",
        "tip_ta": "1979: ரமணா ஷெட்டி; 1994: எஸ்.ஆர். பொம்மை; 2012: 2G அலைக்கற்றை; 2014: AUTSPI தொலைத்தொடர்பு.",
        "fact_en": "The 2014 AUTSPI case cemented the doctrine that private corporations handling natural resources are accountable to CAG.",
        "fact_ta": "2014 AUTSPI வழக்கு இயற்கை வளங்களைக் கையாளும் தனியார் நிறுவனங்கள் சி.ஏ.ஜிக்கு பொறுப்பானவர்கள் என்ற விதியை நிலைநாட்டியது."
    },
    # 18
    {
        "subtopic": "21st Century Appointments Progression",
        "intro_en": "Arrange the following modern Comptrollers and Auditors General of India in chronological order of their assumption of office:",
        "intro_ta": "இந்தியாவின் பின்வரும் நவீன கால தலைமைத் தணிக்கையாளர்களை அவர்கள் பதவியேற்ற காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events_en": [
            "Shashi Kant Sharma assumes office as CAG",
            "V.N. Kaul assumes office as CAG",
            "K. Sanjay Murthy assumes office as CAG",
            "Rajiv Mehrishi assumes office as CAG"
        ],
        "events_ta": [
            "சசி காந்த் சர்மா சி.ஏ.ஜியாகப் பொறுப்பேற்றல்",
            "வி.என். கவுல் சி.ஏ.ஜியாகப் பொறுப்பேற்றல்",
            "கே. சஞ்சய் மூர்த்தி சி.ஏ.ஜியாகப் பொறுப்பேற்றல்",
            "ராஜீவ் மெஹ்ரிஷி சி.ஏ.ஜியாகப் பொறுப்பேற்றல்"
        ],
        # Order: 2 (2002) -> 1 (2013) -> 4 (2017) -> 3 (2024)
        "correct_seq": [2, 1, 4, 3],
        "details_en": "2. V.N. Kaul (2002)\n1. Shashi Kant Sharma (2013)\n4. Rajiv Mehrishi (2017)\n3. K. Sanjay Murthy (2024)",
        "details_ta": "2. வி.என். கவுல் (2002)\n1. சசி காந்த் சர்மா (2013)\n4. ராஜீவ் மெஹ்ரிஷி (2017)\n3. கே. சஞ்சய் மூர்த்தி (2024)",
        "tip_en": "2002: Kaul; 2013: Sharma; 2017: Mehrishi; 2024: K. Sanjay Murthy.",
        "tip_ta": "2002: கவுல்; 2013: சர்மா; 2017: மெஹ்ரிஷி; 2024: கே. சஞ்சய் மூர்த்தி.",
        "fact_en": "K. Sanjay Murthy took the oath of office as CAG in November 2024.",
        "fact_ta": "கே. சஞ்சய் மூர்த்தி நவம்பர் 2024-ல் சி.ஏ.ஜியாகப் பதவிப் பிரமாணம் செய்தார்."
    },
    # 19
    {
        "subtopic": "Budget and Audit Cycle in a Financial Year",
        "intro_en": "Arrange the stages of the governmental financial accountability cycle in their correct operational sequence:",
        "intro_ta": "அரசின் நிதிப் பொறுப்புடைமை சுழற்சியின் பின்வரும் கட்டங்களை அவற்றின் சரியான செயல்பாட்டு வரிசையில் ஒழுங்குபடுத்தவும்:",
        "events_en": [
            "Compilation of annual Appropriation and Finance Accounts for the completed fiscal year",
            "Enactment of the Appropriation Act by Parliament voting budget grants",
            "Examination of CAG audit reports and departmental witness depositions by the PAC",
            "Tabling of the CAG's audited annual accounts and reports before Parliament under Article 151"
        ],
        "events_ta": [
            "முடிவடைந்த நிதியாண்டிற்கான வருடாந்திர ஒதுக்கீடு மற்றும் நிதிக் கணக்குகள் தொகுக்கப்படுதல்",
            "நாடாளுமன்றத்தால் பட்ஜெட் மானியங்களை அங்கீகரிக்கும் நிதி ஒதுக்கீட்டுச் சட்டம் நிறைவேற்றப்படுதல்",
            "பொதுக் கணக்குக் குழுவால் (PAC) தணிக்கை அறிக்கைகள் மற்றும் துறை சாட்சிகள் ஆய்வு செய்யப்படுதல்",
            "சரத்து 151-ன் கீழ் தணிக்கை செய்யப்பட்ட கணக்குகள் மற்றும் அறிக்கைகள் நாடாளுமன்றத்தில் சமர்ப்பிக்கப்படுதல்"
        ],
        # Order: 2 (Budget grant voted) -> 1 (Accounts compiled) -> 4 (CAG report tabled) -> 3 (PAC scrutiny)
        "correct_seq": [2, 1, 4, 3],
        "details_en": "2. Appropriation Act enacted by Parliament (Year 1, March)\n1. Appropriation & Finance Accounts compiled (Year 2, April-June)\n4. CAG reports tabled in Parliament under Article 151 (Year 2, Monsoon/Winter)\n3. PAC examines audit reports and witness depositions (Year 2-3)",
        "details_ta": "2. நிதி ஒதுக்கீட்டுச் சட்டம் நிறைவேற்றப்படுதல் (ஆண்டு 1, மார்ச்)\n1. ஒதுக்கீடு மற்றும் நிதிக் கணக்குகள் தொகுக்கப்படுதல் (ஆண்டு 2, ஏப்ரல்-ஜூன்)\n4. சரத்து 151-ன் கீழ் அறிக்கைகள் நாடாளுமன்றத்தில் சமர்ப்பிக்கப்படுதல் (ஆண்டு 2)\n3. பொதுக் கணக்குக் குழு சாட்சிகளை விசாரித்து ஆய்வு செய்தல் (ஆண்டு 2-3)",
        "tip_en": "Cycle: Budget Appropriation -> Compilation of Accounts -> CAG Audit Tabling -> PAC Scrutiny.",
        "tip_ta": "சுழற்சி: பட்ஜெட் ஒதுக்கீடு -> கணக்குத் தொகுப்பு -> சி.ஏ.ஜி அறிக்கை சமர்ப்பிப்பு -> PAC ஆய்வு.",
        "fact_en": "This unbroken cycle of financial accountability was conceptualized in the Government of India Act 1919.",
        "fact_ta": "இந்த தொடர்ச்சியான நிதிப் பொறுப்புடைமை சுழற்சி 1919 இந்திய அரசுச் சட்டத்தில் வடிவமைக்கப்பட்டது."
    },
    # 20
    {
        "subtopic": "Performance Audit Execution Stages",
        "intro_en": "Arrange the following operational stages of conducting a CAG Performance Audit in chronological order:",
        "intro_ta": "சி.ஏ.ஜி செயல்திறன் தணிக்கையை நடத்துவதில் உள்ள பின்வரும் செயல்பாட்டுக் கட்டங்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events_en": [
            "Conducting Entry Conference with departmental heads to discuss audit scope and criteria",
            "Strategic risk assessment, topic selection, and preliminary audit planning",
            "Holding Exit Conference to discuss draft findings and incorporate departmental replies",
            "Execution of field audit, evidence collection, and issuance of audit queries"
        ],
        "events_ta": [
            "தணிக்கை வரம்பு மற்றும் அளவுகோல்களை விவாதிக்க துறைத் தலைவர்களுடன் தொடக்கக் கூட்டம் (Entry Conference) நடத்துதல்",
            "மூலோபாய இடர் மதிப்பீடு, தலைப்பு தேர்வு மற்றும் ஆரம்ப தணிக்கைத் திட்டமிடல்",
            "வரைவு தணிக்கைக் குறிப்புகளை விவாதித்து துறைசார் பதில்களைப் பெற இறுதிக் கூட்டம் (Exit Conference) நடத்துதல்",
            "கள ஆய்வு நடத்துதல், சான்றுகள் சேகரித்தல் மற்றும் தணிக்கை வினாக்களை அனுப்புதல்"
        ],
        # Order: 2 (Planning) -> 1 (Entry Conference) -> 4 (Field audit) -> 3 (Exit Conference)
        "correct_seq": [2, 1, 4, 3],
        "details_en": "2. Strategic planning and topic selection (Stage 1)\n1. Entry Conference with audited department (Stage 2)\n4. Field audit execution and evidence collection (Stage 3)\n3. Exit Conference on draft findings (Stage 4)",
        "details_ta": "2. திட்டமிடல் மற்றும் தலைப்பு தேர்வு (கட்டம் 1)\n1. தொடக்கக் கூட்டம் நடத்துதல் (கட்டம் 2)\n4. கள ஆய்வு மற்றும் சான்றுகள் சேகரிப்பு (கட்டம் 3)\n3. முடிவுக் கூட்டம் மற்றும் பதில் பெறுதல் (கட்டம் 4)",
        "tip_en": "Audit lifecycle: Topic Selection -> Entry Conference -> Field Work -> Exit Conference -> Final Report.",
        "tip_ta": "தணிக்கை சுழற்சி: தலைப்பு தேர்வு -> தொடக்கக் கூட்டம் -> கள ஆய்வு -> முடிவுக் கூட்டம் -> இறுதி அறிக்கை.",
        "fact_en": "Exit conferences are mandatory under CAG's Regulations on Audit and Accounts to ensure natural justice.",
        "fact_ta": "இயற்கை நீதியை நிலைநாட்ட முடிவுக் கூட்டங்களை நடத்துவது தணிக்கை ஒழுங்குமுறைகளின் கீழ் கட்டாயமாகும்."
    },
    # 21
    {
        "subtopic": "Local Government Audit Milestones",
        "intro_en": "Arrange the following milestones concerning local bodies audit in India in chronological order:",
        "intro_ta": "இந்தியாவில் உள்ளாட்சி அமைப்புகளின் தணிக்கை தொடர்பான பின்வரும் மைல்கற்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events_en": [
            "CAG issues Model Accounting System for Panchayati Raj Institutions (PRIs)",
            "73rd and 74th Constitutional Amendments passed establishing Panchayats and Municipalities",
            "Fifteenth Finance Commission makes CAG-audited accounts a mandatory condition for local body grants",
            "Eleventh Finance Commission recommends entrusting Technical Guidance and Supervision (TGS) to CAG"
        ],
        "events_ta": [
            "பஞ்சாயத்து ராஜ் அமைப்புகளுக்கான மாதிரி கணக்கு முறையை (MAS) சி.ஏ.ஜி வெளியிடுதல்",
            "பஞ்சாயத்துகள் மற்றும் நகராட்சிகளை நிறுவிய 73 மற்றும் 74வது அரசியலமைப்புத் திருத்தங்கள் நிறைவேற்றப்படுதல்",
            "15வது நிதி ஆணையம் உள்ளாட்சி மானியங்களுக்கு சி.ஏ.ஜி தணிக்கை செய்யப்பட்ட கணக்குகளை கட்டாய நிபந்தனையாக்குதல்",
            "11வது நிதி ஆணையம் சி.ஏ.ஜியிடம் தொழில்நுட்ப வழிகாட்டுதல் மற்றும் மேற்பார்வையை (TGS) ஒப்படைக்க பரிந்துரைத்தல்"
        ],
        # Order: 2 (1992) -> 4 (2000) -> 1 (2009) -> 3 (2020)
        "correct_seq": [2, 4, 1, 3],
        "details_en": "2. 73rd and 74th Amendments passed (1992)\n4. 11th Finance Commission recommends TGS (2000)\n1. CAG issues Model Accounting System for PRIs (2009)\n3. 15th Finance Commission ties grants to audited accounts (2020)",
        "details_ta": "2. 73 மற்றும் 74வது திருத்தங்கள் சட்டம் (1992)\n4. 11வது நிதி ஆணைய TGS பரிந்துரை (2000)\n1. பஞ்சாயத்து மாதிரி கணக்கு முறை வெளியீடு (2009)\n3. 15வது நிதி ஆணைய நிபந்தனை மானியங்கள் (2020)",
        "tip_en": "1992: 73rd/74th Amdt; 2000: 11th FC TGS; 2009: Model Accounting System; 2020: 15th FC grants.",
        "tip_ta": "1992: 73/74வது திருத்தம்; 2000: 11வது நிதி ஆணையம்; 2009: மாதிரி கணக்கு முறை; 2020: 15வது நிதி ஆணையம்.",
        "fact_en": "The Model Accounting System classifies PRI expenditure into functional and schematic codes.",
        "fact_ta": "மாதிரி கணக்கு முறை பஞ்சாயத்து செலவினங்களை செயல்பாட்டு மற்றும் திட்டக் குறியீடுகளாக வகைப்படுத்துகிறது."
    },
    # 22
    {
        "subtopic": "Evolution of Global Auditing Standards",
        "intro_en": "Arrange the following landmark international declarations on Supreme Audit Institutions in chronological order:",
        "intro_ta": "உச்ச தணிக்கை அமைப்புகள் தொடர்பான பின்வரும் வரலாற்று சர்வதேச பிரகடனங்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events_en": [
            "Mexico Declaration on SAI Independence",
            "Lima Declaration of Guidelines on Auditing Precepts",
            "Moscow Declaration on Artificial Intelligence and Big Data in Public Audit",
            "Adoption of the International Standards of Supreme Audit Institutions (ISSAI) framework"
        ],
        "events_ta": [
            "உச்ச தணிக்கை அமைப்புகளின் சுதந்திரம் குறித்த மெக்ஸிகோ பிரகடனம்",
            "தணிக்கைக் கோட்பாடுகள் வழிகாட்டுதல்கள் மீதான லிமா பிரகடனம் (Lima Declaration)",
            "பொதுத் தணிக்கையில் செயற்கை நுண்ணறிவு மற்றும் பெருந்தரவு பயன்பாடு குறித்த மாஸ்கோ பிரகடனம்",
            "சர்வதேச உச்ச தணிக்கை அமைப்புகளின் தரநிலைகள் (ISSAI) கட்டமைப்பை அதிகாரப்பூர்வமாக ஏற்றுக்கொள்ளுதல்"
        ],
        # Order: 2 (1977) -> 1 (2007) -> 4 (2010) -> 3 (2019)
        "correct_seq": [2, 1, 4, 3],
        "details_en": "2. Lima Declaration adopted (1977)\n1. Mexico Declaration on SAI Independence (2007)\n4. ISSAI framework adopted by INTOSAI (2010)\n3. Moscow Declaration on AI and Big Data (2019)",
        "details_ta": "2. லிமா பிரகடனம் ஏற்றுக்கொள்ளப்படுதல் (1977)\n1. மெக்ஸிகோ சுதந்திரப் பிரகடனம் (2007)\n4. ISSAI தரநிலைகள் ஏற்பு (2010)\n3. மாஸ்கோ AI பிரகடனம் (2019)",
        "tip_en": "1977: Lima (Magna Carta of audit); 2007: Mexico (SAI independence); 2010: ISSAI; 2019: Moscow.",
        "tip_ta": "1977: லிமா பிரகடனம்; 2007: மெக்ஸிகோ பிரகடனம்; 2010: ISSAI தரநிலைகள்; 2019: மாஸ்கோ பிரகடனம்.",
        "fact_en": "The Lima Declaration (1977) is revered worldwide as the Magna Carta of government auditing.",
        "fact_ta": "லிமா பிரகடனம் (1977) உலகளவில் அரசு தணிக்கையின் மகாசாசனம் (Magna Carta) என்று போற்றப்படுகிறது."
    },
    # 23
    {
        "subtopic": "Evolution of IT and Digital Auditing in CAG",
        "intro_en": "Arrange the following milestones in IT and digital auditing by the CAG of India in chronological order:",
        "intro_ta": "இந்திய சி.ஏ.ஜியின் தகவல் தொழில்நுட்பம் மற்றும் டிஜிட்டல் தணிக்கையின் பின்வரும் மைல்கற்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events_en": [
            "Establishment of the specialized Information Systems (IS) Audit Directorate",
            "First edition of Guidelines on Auditing in an Information Technology Environment issued",
            "Adoption of the Big Data Management Policy by the CAG of India",
            "Full integration of AI and machine learning audit models into OIOS enterprise system"
        ],
        "events_ta": [
            "தகவல் அமைப்புகள் (IS) தணிக்கைக்கான சிறப்பு இயக்குநரகம் நிறுவப்படுதல்",
            "தகவல் தொழில்நுட்ப சூழலில் தணிக்கை செய்வதற்கான முதல் வழிகாட்டுதல்கள் வெளியிடப்படுதல்",
            "இந்திய சி.ஏ.ஜியால் பெருந்தரவு மேலாண்மைக் கொள்கை (Big Data Policy) ஏற்றுக்கொள்ளப்படுதல்",
            "OIOS தளத்தில் AI மற்றும் இயந்திர கற்றல் தணிக்கை மாதிரிகள் முழுமையாக ஒருங்கிணைக்கப்படுதல்"
        ],
        # Order: 2 (1998) -> 1 (2004) -> 3 (2016) -> 4 (2022)
        "correct_seq": [2, 1, 3, 4],
        "details_en": "2. First IT Audit Guidelines issued (1998)\n1. IS Audit Directorate established (2004)\n3. Big Data Management Policy adopted (2016)\n4. AI and ML models integrated into OIOS (2022)",
        "details_ta": "2. முதல் தகவல் தொழில்நுட்ப தணிக்கை வழிகாட்டுதல்கள் (1998)\n1. IS தணிக்கை இயக்குநரகம் தொடக்கம் (2004)\n3. பெருந்தரவு மேலாண்மைக் கொள்கை (2016)\n4. OIOS தளத்தில் AI மாதிரிகள் இணைப்பு (2022)",
        "tip_en": "1998: IT Guidelines; 2004: IS Directorate; 2016: Big Data; 2022: AI-driven OIOS.",
        "tip_ta": "1998: IT வழிகாட்டுதல்; 2004: IS இயக்குநரகம்; 2016: பெருந்தரவு; 2022: AI-சார்ந்த OIOS.",
        "fact_en": "The Big Data Policy established standardized protocols for acquiring structured government data.",
        "fact_ta": "பெருந்தரவுக் கொள்கை அரசுத் தரவுகளைப் பெறுவதற்கான நிலையான நெறிமுறைகளை நிறுவியது."
    },
    # 24
    {
        "subtopic": "Landmark Defence Procurement Audits",
        "intro_en": "Arrange the following historic defence procurement audits by the CAG in chronological order:",
        "intro_ta": "சி.ஏ.ஜியின் பின்வரும் முக்கிய பாதுகாப்பு கொள்முதல் தணிக்கை அறிக்கைகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events_en": [
            "Audit Review on Operation Vijay (Kargil) Special Ammunition and Equipment Purchases",
            "Performance Audit Report on 155mm Bofors Howitzer Gun System",
            "CAG Performance Audit on Capital Acquisition in the Indian Air Force (Rafale Deal)",
            "Audit Report on Design and Construction of Indigenous Aircraft Carrier and Submarines"
        ],
        "events_ta": [
            "ஆபரேஷன் விஜய் (கார்கில்) சிறப்பு வெடிமருந்து கொள்முதல் மீதான தணிக்கை மதிப்பாய்வு",
            "155மிமீ போஃபோர்ஸ் பீரங்கி அமைப்பு மீதான செயல்திறன் தணிக்கை அறிக்கை",
            "விமானப்படை மூலதனக் கொள்முதல் (ரஃபேல் ஒப்பந்தம்) மீதான சி.ஏ.ஜி தணிக்கை அறிக்கை",
            "உள்நாட்டு விமானம் தாங்கி கப்பல் மற்றும் நீர்மூழ்கிக் கப்பல் கட்டுமானம் மீதான தணிக்கை"
        ],
        # Order: 2 (1989) -> 1 (2001) -> 4 (2016) -> 3 (2019)
        "correct_seq": [2, 1, 4, 3],
        "details_en": "2. Bofors Howitzer gun audit report (1989)\n1. Operation Vijay (Kargil) procurement review (2001)\n4. Indigenous Aircraft Carrier and submarine audit (2016)\n3. Rafale aircraft acquisition audit report (2019)",
        "details_ta": "2. போஃபோர்ஸ் பீரங்கி தணிக்கை அறிக்கை (1989)\n1. ஆபரேஷன் விஜய் (கார்கில்) கொள்முதல் தணிக்கை (2001)\n4. உள்நாட்டு போர்க்கப்பல் மற்றும் நீர்மூழ்கிக் கப்பல் தணிக்கை (2016)\n3. ரஃபேல் போர் விமான கொள்முதல் தணிக்கை (2019)",
        "tip_en": "1989: Bofors; 2001: Kargil; 2016: Aircraft Carrier; 2019: Rafale.",
        "tip_ta": "1989: போஃபோர்ஸ்; 2001: கார்கில்; 2016: போர்க்கப்பல்; 2019: ரஃபேல்.",
        "fact_en": "The Kargil procurement review scrutinised expedited emergency foreign purchases made under relaxed rules.",
        "fact_ta": "கார்கில் தணிக்கை அவசர விதிகளின் கீழ் வெளிநாடுகளிலிருந்து செய்யப்பட்ட கொள்முதல்களை ஆய்வு செய்தது."
    },
    # 25
    {
        "subtopic": "21st Century Succession of Indian CAGs",
        "intro_en": "Arrange the following 21st-century Comptrollers and Auditors General of India in chronological order of their assumption of office:",
        "intro_ta": "21ஆம் நூற்றாண்டின் பின்வரும் இந்தியத் தலைமைத் தணிக்கையாளர்களை அவர்கள் பதவியேற்ற காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events_en": [
            "Rajiv Mehrishi assumes office as 13th CAG",
            "Vinod Rai assumes office as 11th CAG",
            "K. Sanjay Murthy assumes office as 15th CAG",
            "G.C. Murmu assumes office as 14th CAG"
        ],
        "events_ta": [
            "ராஜீவ் மெஹ்ரிஷி 13வது சி.ஏ.ஜியாகப் பொறுப்பேற்றல்",
            "வினோத் ராய் 11வது சி.ஏ.ஜியாகப் பொறுப்பேற்றல்",
            "கே. சஞ்சய் மூர்த்தி 15வது சி.ஏ.ஜியாகப் பொறுப்பேற்றல்",
            "ஜி.சி. முர்மு 14வது சி.ஏ.ஜியாகப் பொறுப்பேற்றல்"
        ],
        # Order: 2 (2008) -> 1 (2017) -> 4 (2020) -> 3 (2024)
        "correct_seq": [2, 1, 4, 3],
        "details_en": "2. Vinod Rai (11th CAG, 2008)\n1. Rajiv Mehrishi (13th CAG, 2017)\n4. G.C. Murmu (14th CAG, 2020)\n3. K. Sanjay Murthy (15th CAG, 2024)",
        "details_ta": "2. வினோத் ராய் (11வது சி.ஏ.ஜி, 2008)\n1. ராஜீவ் மெஹ்ரிஷி (13வது சி.ஏ.ஜி, 2017)\n4. ஜி.சி. முர்மு (14வது சி.ஏ.ஜி, 2020)\n3. கே. சஞ்சய் மூர்த்தி (15வது சி.ஏ.ஜி, 2024)",
        "tip_en": "2008: Vinod Rai; 2017: Rajiv Mehrishi; 2020: G.C. Murmu; 2024: K. Sanjay Murthy.",
        "tip_ta": "2008: வினோத் ராய்; 2017: ராஜீவ் மெஹ்ரிஷி; 2020: ஜி.சி. முர்மு; 2024: கே. சஞ்சய் மூர்த்தி.",
        "fact_en": "K. Sanjay Murthy previously served as Secretary, Higher Education in the Government of India.",
        "fact_ta": "கே. சஞ்சய் மூர்த்தி இதற்கு முன் மத்திய அரசின் உயர் கல்வித் துறைச் செயலாளராகப் பணியாற்றினார்."
    }
]

def generate_chronology_options(correct_seq):
    """
    Generate 4 unique option sequences including the correct one.
    Returns: list of 4 tuples (seq_list, str_repr)
    """
    correct_tuple = tuple(correct_seq)
    all_perms = [p for p in permutations([1, 2, 3, 4]) if p != (1, 2, 3, 4) and p != correct_tuple]
    # Pick 3 unique distractor permutations
    random.seed(42 + sum(correct_seq))
    distractors = random.sample(all_perms, 3)
    
    options = [correct_tuple] + distractors
    return options

def build_questions():
    # Target key balance for 25 questions: 7 A, 6 B, 6 C, 6 D
    target_keys = ["A"] * 7 + ["B"] * 6 + ["C"] * 6 + ["D"] * 6
    # Deterministic assignment
    key_assignment = ["A", "B", "C", "D", "A", "B", "C", "D", "A", "B", "C", "D", 
                      "A", "B", "C", "D", "A", "B", "C", "D", "A", "B", "C", "D", "A"]
    
    questions = []
    for idx, item in enumerate(raw_chronology_data, start=1):
        qid = f"CAG_C_{idx:03d}"
        correct_key = key_assignment[idx - 1]
        
        # Build stem with 4 numbered items
        stem_en = f"{item['intro_en']}\n1. {item['events_en'][0]}\n2. {item['events_en'][1]}\n3. {item['events_en'][2]}\n4. {item['events_en'][3]}"
        stem_ta = f"{item['intro_ta']}\n1. {item['events_ta'][0]}\n2. {item['events_ta'][1]}\n3. {item['events_ta'][2]}\n4. {item['events_ta'][3]}"
        
        correct_seq = item["correct_seq"]
        all_opts = generate_chronology_options(correct_seq)
        # all_opts[0] is correct. Place it at the position corresponding to correct_key
        key_to_pos = {"A": 0, "B": 1, "C": 2, "D": 3}
        target_pos = key_to_pos[correct_key]
        
        arranged_opts = list(all_opts[1:])
        arranged_opts.insert(target_pos, all_opts[0])
        
        opt_strings = [" - ".join(map(str, opt)) for opt in arranged_opts]
        
        correct_arrow_str = " -> ".join(map(str, correct_seq))
        exp_en = f"The correct chronological order is: {correct_arrow_str}.\nKey chronological dates and progression:\n{item['details_en']}"
        exp_ta = f"சரியான காலவரிசை ஒழுங்கு: {correct_arrow_str}.\nமுக்கிய காலவரிசை நிகழ்வுகள்:\n{item['details_ta']}"
        
        why_en = {}
        why_ta = {}
        for k_idx, k in enumerate(["A", "B", "C", "D"]):
            if k == correct_key:
                why_en[k] = f"Option {k} ({opt_strings[k_idx]}) accurately reflects the chronological sequence: {correct_arrow_str}."
                why_ta[k] = f"தெரிவு {k} ({opt_strings[k_idx]}) சரியான காலவரிசையைத் துல்லியமாகப் பிரதிபலிக்கிறது: {correct_arrow_str}."
            else:
                why_en[k] = f"Option {k} ({opt_strings[k_idx]}) contains an incorrect chronological sequence."
                why_ta[k] = f"தெரிவு {k} ({opt_strings[k_idx]}) தவறான காலவரிசையைக் கொண்டுள்ளது."
                
        q = make_cag_q(
            qid=qid,
            diff="Hard",
            qtype="Chronology",
            subtopic=item["subtopic"],
            en_stem=stem_en,
            ta_stem=stem_ta,
            en_a=opt_strings[0],
            ta_a=opt_strings[0],
            en_b=opt_strings[1],
            ta_b=opt_strings[1],
            en_c=opt_strings[2],
            ta_c=opt_strings[2],
            en_d=opt_strings[3],
            ta_d=opt_strings[3],
            correct_key=correct_key,
            exp_en=exp_en,
            exp_ta=exp_ta,
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
            tags=["polity", "comptroller_and_auditor_general", "chronology", item["subtopic"].lower().replace(" ", "_")]
        )
        questions.append(q)
    return questions

if __name__ == "__main__":
    qs = build_questions()
    print(f"Generated {len(qs)} raw Chronology questions for CAG.")
    
    out_path = os.path.join("data", "questions", "polity", "cag_chronology.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, ensure_ascii=False, indent=2)
    print(f"Saved Chronology MCQs to {out_path}")
    
    # 1. Validate with ContentValidator
    val = ContentValidator()
    report = val.validate_file(out_path, expected_count=25, expected_prefix="CAG_C_")
    print(f"ContentValidator: {'PASS' if report.is_valid else 'FAIL'} | Total: {report.total_audited}")
    if not report.is_valid:
        for iss in report.issues[:10]:
            print(f"  Issue: {iss}")
    print(f"Key Distribution: {report.key_distribution}")
    
    # 2. Validate with dedicated ChronologyValidator
    chron_rep = ChronologyValidator.validate_file(out_path)
    print(f"\nChronologyValidator Gate: {'PASS' if chron_rep.is_valid else 'FAIL'}")
    print(chron_rep.format_final_report())
    if not chron_rep.is_valid:
        for iss in chron_rep.issues:
            print("  Chron Issue:", iss)
