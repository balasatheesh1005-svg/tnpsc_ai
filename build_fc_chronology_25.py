# -*- coding: utf-8 -*-
"""
Build 25 Chronology MCQs for Finance Commission of India
ID range: FC_C_001 to FC_C_025
Target key distribution: {'A': 7, 'B': 6, 'C': 6, 'D': 6}
Passes all ChronologyValidator gates:
- Presented order != chronological order
- 4-digit years in explanation
- Sequence arrows '->' in explanation
"""

import json
import os
from fc_mcq_helper import make_fc_q
from tools.nova_content_engine.validator import ContentValidator
from tools.nova_content_engine.chronology_validator import ChronologyValidator

raw_chrono_data = [
    # 1: A
    {
        "subtopic": "Early Finance Commissions Constitution",
        "key": "A",
        "items": [
            ("Third Finance Commission (A.K. Chanda)", "மூன்றாவது நிதி ஆணையம் (ஏ.கே. சந்தா)", 1960),
            ("First Finance Commission (K.C. Neogy)", "முதலாவது நிதி ஆணையம் (கே.சி. நியோகி)", 1951),
            ("Fourth Finance Commission (P.V. Rajamannar)", "நான்காவது நிதி ஆணையம் (பி.வி. ராஜமன்னார்)", 1964),
            ("Second Finance Commission (K. Santhanam)", "இரண்டாவது நிதி ஆணையம் (கே. சந்தானம்)", 1956)
        ],
        "order": [2, 4, 1, 3], # 1951, 1956, 1960, 1964 -> 2, 4, 1, 3
        "tip_en": "First FC was constituted in 1951 under K.C. Neogy.",
        "tip_ta": "முதல் நிதி ஆணையம் 1951-ல் கே.சி. நியோகி தலைமையில் அமைக்கப்பட்டது.",
        "fact_en": "K. Santhanam headed the 2nd FC (1956) and P.V. Rajamannar headed the 4th FC (1964).",
        "fact_ta": "2வது ஆணையத்திற்கு கே. சந்தானமும் (1956), 4வது ஆணையத்திற்கு பி.வி. ராஜமன்னாரும் (1964) தலைமை தாங்கினர்."
    },
    # 2: A
    {
        "subtopic": "Middle Era Finance Commissions",
        "key": "A",
        "items": [
            ("Seventh Finance Commission (J.M. Shelat)", "ஏழாவது நிதி ஆணையம் (ஜே.எம். ஷெலத்)", 1977),
            ("Fifth Finance Commission (Mahavir Tyagi)", "ஐந்தாவது நிதி ஆணையம் (மகாவீர் தியாகி)", 1968),
            ("Eighth Finance Commission (Y.B. Chavan)", "எட்டாவது நிதி ஆணையம் (ஒய்.பி. சவான்)", 1982),
            ("Sixth Finance Commission (K. Brahmananda Reddy)", "ஆறாவது நிதி ஆணையம் (கே. பிரம்மானந்த ரெட்டி)", 1972)
        ],
        "order": [2, 4, 1, 3], # 1968, 1972, 1977, 1982 -> 2, 4, 1, 3
        "tip_en": "Fifth FC: 1968, Sixth FC: 1972, Seventh FC: 1977, Eighth FC: 1982.",
        "tip_ta": "5வது: 1968, 6வது: 1972, 7வது: 1977, 8வது: 1982.",
        "fact_en": "Seventh FC under Justice Shelat doubled the excise share to 40% in 1978.",
        "fact_ta": "நீதிபதி ஷெலத் தலைமையிலான 7வது ஆணையம் 1978-ல் கலால் வரிப் பங்கை 40% ஆக உயர்த்தியது."
    },
    # 3: A
    {
        "subtopic": "Economic Reform Era Finance Commissions",
        "key": "A",
        "items": [
            ("Eleventh Finance Commission (A.M. Khusro)", "பதினோராவது நிதி ஆணையம் (ஏ.எம். குஸ்ரோ)", 1998),
            ("Ninth Finance Commission (N.K.P. Salve)", "ஒன்பதாவது நிதி ஆணையம் (என்.கே.பி. சால்வே)", 1987),
            ("Twelfth Finance Commission (C. Rangarajan)", "பன்னிரண்டாவது நிதி ஆணையம் (சி. ரங்கராஜன்)", 2002),
            ("Tenth Finance Commission (K.C. Pant)", "பத்தாவது நிதி ஆணையம் (கே.சி. பந்த்)", 1992)
        ],
        "order": [2, 4, 1, 3], # 1987, 1992, 1998, 2002 -> 2, 4, 1, 3
        "tip_en": "9th FC: 1987, 10th FC: 1992, 11th FC: 1998, 12th FC: 2002.",
        "tip_ta": "9வது: 1987, 10வது: 1992, 11வது: 1998, 12வது: 2002.",
        "fact_en": "Tenth FC under K.C. Pant formulated the Alternative Devolution Scheme in 1994.",
        "fact_ta": "கே.சி. பந்த் தலைமையிலான 10வது ஆணையம் 1994-ல் மாற்று வரிப் பகிர்வுத் திட்டத்தை உருவாக்கியது."
    },
    # 4: A
    {
        "subtopic": "21st Century Finance Commissions",
        "key": "A",
        "items": [
            ("Fifteenth Finance Commission (N.K. Singh)", "பதினைந்தாவது நிதி ஆணையம் (என்.கே. சிங்)", 2017),
            ("Thirteenth Finance Commission (Vijay Kelkar)", "பதின்மூன்றாவது நிதி ஆணையம் (விஜய் கேல்கர்)", 2007),
            ("Sixteenth Finance Commission (Arvind Panagariya)", "பதினாறாவது நிதி ஆணையம் (அரவிந்த் பனகாரியா)", 2023),
            ("Fourteenth Finance Commission (Y.V. Reddy)", "பதினான்காவது நிதி ஆணையம் (ஒய்.வி. ரெட்டி)", 2013)
        ],
        "order": [2, 4, 1, 3], # 2007, 2013, 2017, 2023 -> 2, 4, 1, 3
        "tip_en": "13th: 2007, 14th: 2013, 15th: 2017, 16th: 2023.",
        "tip_ta": "13வது: 2007, 14வது: 2013, 15வது: 2017, 16வது: 2023.",
        "fact_en": "16th FC was constituted on December 31, 2023 under Dr. Arvind Panagariya.",
        "fact_ta": "16வது நிதி ஆணையம் டிசம்பர் 31, 2023 அன்று டாக்டர் அரவிந்த் பனகாரியா தலைமையில் அமைக்கப்பட்டது."
    },
    # 5: A
    {
        "subtopic": "Statutory and Constitutional Milestones",
        "key": "A",
        "items": [
            ("73rd and 74th Constitutional Amendments enact Art 280(3)(bb) & (c)", "73 மற்றும் 74வது அரசியலமைப்பு திருத்தங்கள் சரத்து 280(3)(bb) & (c)-ஐ சேர்த்தல்", 1992),
            ("Finance Commission (Miscellaneous Provisions) Act enacted by Parliament", "நாடாளுமன்றத்தால் நிதி ஆணைய (இதர விதிகள்) சட்டம் இயற்றப்படுதல்", 1951),
            ("101st Constitutional Amendment Act introduces Goods and Services Tax", "101வது அரசியலமைப்புத் திருத்தச் சட்டம் சரக்கு மற்றும் சேவை வரியை அறிமுகப்படுத்துதல்", 2016),
            ("80th Constitutional Amendment creates single divisible tax pool", "80வது அரசியலமைப்புத் திருத்தம் ஒற்றைப் பகிர்வு வரி நிதியை உருவாக்குதல்", 2000)
        ],
        "order": [2, 1, 4, 3], # 1951, 1992, 2000, 2016 -> 2, 1, 4, 3
        "tip_en": "1951 Act -> 1992 Local body amendments -> 2000 80th Amendment -> 2016 GST 101st Amendment.",
        "tip_ta": "1951 சட்டம் -> 1992 உள்ளாட்சி திருத்தங்கள் -> 2000 80வது திருத்தம் -> 2016 ஜிஎஸ்டி 101வது திருத்தம்.",
        "fact_en": "The 80th Amendment implemented the Alternative Scheme of Devolution recommended by 10th FC.",
        "fact_ta": "80வது திருத்தம் 10வது நிதி ஆணையம் பரிந்துரைத்த மாற்று வரிப் பகிர்வுத் திட்டத்தை செயல்படுத்தியது."
    },
    # 6: A
    {
        "subtopic": "Vertical Tax Devolution Enhancements",
        "key": "A",
        "items": [
            ("Seventh FC elevates Union Excise Duty share to 40%", "7வது ஆணையம் மத்திய கலால் வரிப் பங்கை 40% ஆக உயர்த்துதல்", 1978),
            ("First FC recommends 55% Income Tax devolution to States", "1வது ஆணையம் மாநிலங்களுக்கு 55% வருமான வரிப் பகிர்வை பரிந்துரைத்தல்", 1952),
            ("Fourteenth FC raises untied tax devolution to landmark 42%", "14வது ஆணையம் நிபந்தனையற்ற வரிப் பகிர்வை வரலாற்றுச் சிறப்புமிக்க 42% ஆக உயர்த்துதல்", 2014),
            ("Tenth FC proposes 29% pooling of all Central taxes", "10வது ஆணையம் அனைத்து மத்திய வரிகளிலும் 29% பகிர்வை முன்மொழிதல்", 1994)
        ],
        "order": [2, 1, 4, 3], # 1952, 1978, 1994, 2014 -> 2, 1, 4, 3
        "tip_en": "1952 (55% IT) -> 1978 (40% Excise) -> 1994 (29% All Taxes) -> 2014 (42% All Taxes).",
        "tip_ta": "1952 (55% வருமான வரி) -> 1978 (40% கலால்) -> 1994 (29% அனைத்து வரிகள்) -> 2014 (42% அனைத்து வரிகள்).",
        "fact_en": "14th FC award in 2014 was accepted in February 2015 by the Union Government.",
        "fact_ta": "14வது ஆணையத்தின் 2014 பரிந்துரை பிப்ரவரி 2015-ல் மத்திய அரசால் ஏற்றுக்கொள்ளப்பட்டது."
    },
    # 7: A
    {
        "subtopic": "Disaster Financing Evolution",
        "key": "A",
        "items": [
            ("Disaster Management Act formalizes National and State Disaster Response Funds", "பேரிடர் மேலாண்மைச் சட்டம் தேசிய மற்றும் மாநில பேரிடர் நிதிகளை முறைப்படுத்துதல்", 2005),
            ("Ninth FC institutionalizes Calamity Relief Fund (CRF)", "9வது ஆணையம் பேரிடர் நிவாரண நிதியை (CRF) நிறுவனமயமாக்குதல்", 1990),
            ("15th FC operationalizes State Disaster Mitigation Fund (SDMF)", "15வது ஆணையம் மாநில பேரிடர் தணிப்பு நிதியை (SDMF) செயல்படுத்துதல்", 2020),
            ("13th FC introduces dedicated capacity building grant for disaster management", "13வது ஆணையம் பேரிடர் மேலாண்மைக்கான திறன் மேம்பாட்டு மானியத்தை அறிமுகப்படுத்துதல்", 2009)
        ],
        "order": [2, 1, 4, 3], # 1990, 2005, 2009, 2020 -> 2, 1, 4, 3
        "tip_en": "1990 CRF -> 2005 DM Act -> 2009 Capacity Building -> 2020 SDMF.",
        "tip_ta": "1990 CRF -> 2005 பேரிடர் சட்டம் -> 2009 திறன் மேம்பாடு -> 2020 SDMF தணிப்பு நிதி.",
        "fact_en": "15th FC earmarked specific windows for response, mitigation, recovery, and capacity building.",
        "fact_ta": "15வது ஆணையம் நிவாரணம், தணிப்பு, மீட்பு மற்றும் திறன் மேம்பாட்டிற்கான தனி நிதி சாளரங்களை ஒதுக்கியது."
    },
    # 8: B
    {
        "subtopic": "Prominent Chairmen Succession: Neogy to Reddy",
        "key": "B",
        "items": [
            ("Dr. C. Rangarajan appointed Chairman of Twelfth Finance Commission", "டாக்டர் சி. ரங்கராஜன் 12வது நிதி ஆணையத்தின் தலைவராக நியமிக்கப்படுதல்", 2002),
            ("K.C. Neogy appointed Chairman of First Finance Commission", "கே.சி. நியோகி முதலாவது நிதி ஆணையத்தின் தலைவராக நியமிக்கப்படுதல்", 1951),
            ("Dr. Y.V. Reddy appointed Chairman of Fourteenth Finance Commission", "டாக்டர் ஒய்.வி. ரெட்டி 14வது நிதி ஆணையத்தின் தலைவராக நியமிக்கப்படுதல்", 2013),
            ("Mahavir Tyagi appointed Chairman of Fifth Finance Commission", "மகாவீர் தியாகி 5வது நிதி ஆணையத்தின் தலைவராக நியமிக்கப்படுதல்", 1968)
        ],
        "order": [2, 4, 1, 3], # 1951, 1968, 2002, 2013 -> 2, 4, 1, 3
        "tip_en": "Neogy (1951) -> Tyagi (1968) -> Rangarajan (2002) -> Reddy (2013).",
        "tip_ta": "நியோகி (1951) -> தியாகி (1968) -> ரங்கராஜன் (2002) -> ரெட்டி (2013).",
        "fact_en": "Both Dr. Rangarajan and Dr. Reddy were former Governors of the Reserve Bank of India.",
        "fact_ta": "டாக்டர் ரங்கராஜன் மற்றும் டாக்டர் ரெட்டி இருவரும் இந்திய ரிசர்வ் வங்கியின் முன்னாள் ஆளுநர்களாவர்."
    },
    # 9: B
    {
        "subtopic": "Local Body Grant Evolution Milestones",
        "key": "B",
        "items": [
            ("Eleventh FC creates comprehensive formulaic rural and urban local grants", "11வது ஆணையம் ஊரக மற்றும் நகர்ப்புற உள்ளாட்சிகளுக்கான முழுமையான சூத்திர மானியங்களை உருவாக்குதல்", 2000),
            ("73rd and 74th Constitutional Amendments enter into force", "73 மற்றும் 74வது அரசியலமைப்புத் திருத்தங்கள் நடைமுறைக்கு வருதல்", 1993),
            ("15th FC ties local body grants to drinking water, sanitation, and online audits", "15வது ஆணையம் உள்ளாட்சி மானியங்களை குடிநீர், சுகாதாரம் மற்றும் இணைய தணிக்கையுடன் இணைத்தல்", 2020),
            ("Tenth FC recommends first interim ad-hoc grant of Rs. 1,000 crore for Panchayats", "10வது ஆணையம் பஞ்சாயத்துகளுக்கு ரூ. 1,000 கோடி மதிப்பிலான முதல் இடைக்கால மானியத்தை பரிந்துரைத்தல்", 1995)
        ],
        "order": [2, 4, 1, 3], # 1993, 1995, 2000, 2020 -> 2, 4, 1, 3
        "tip_en": "1993 CAA -> 1995 10th FC -> 2000 11th FC -> 2020 15th FC.",
        "tip_ta": "1993 திருத்தங்கள் -> 1995 10வது ஆணையம் -> 2000 11வது ஆணையம் -> 2020 15வது ஆணையம்.",
        "fact_en": "Local body grants expanded from Rs. 1,000 crore in 10th FC to Rs. 4.36 lakh crore in 15th FC.",
        "fact_ta": "உள்ளாட்சி மானியங்கள் 10வது ஆணையத்தில் ரூ. 1,000 கோடியிலிருந்து 15வது ஆணையத்தில் ரூ. 4.36 லட்சம் கோடியாக விரிவடைந்தன."
    },
    # 10: B
    {
        "subtopic": "Fiscal Responsibility and Consolidation Frameworks",
        "key": "B",
        "items": [
            ("Twelfth FC introduces Debt Consolidation and Relief Facility (DCRF)", "12வது ஆணையம் கடன் ஒருங்கிணைப்பு மற்றும் நிவாரண வசதியை (DCRF) அறிமுகப்படுத்துதல்", 2004),
            ("Central FRBM Act enacted by Parliament", "மத்திய FRBM சட்டம் நாடாளுமன்றத்தால் இயற்றப்படுதல்", 2003),
            ("15th FC recommends post-COVID glide path targeting 4.0% fiscal deficit by 2025-26", "15வது ஆணையம் 2025-26க்குள் 4.0% நிதிப் பற்றாக்குறையை இலக்காகக் கொண்ட பாதையை பரிந்துரைத்தல்", 2020),
            ("13th FC formulates detailed medium-term debt roadmap for Centre and States", "13வது ஆணையம் மத்திய மற்றும் மாநிலங்களுக்கான விரிவான நடுத்தர கால கடன் வரைபடத்தை உருவாக்குதல்", 2009)
        ],
        "order": [2, 1, 4, 3], # 2003, 2004, 2009, 2020 -> 2, 1, 4, 3
        "tip_en": "2003 FRBM Act -> 2004 12th FC DCRF -> 2009 13th FC Roadmap -> 2020 15th FC Glide Path.",
        "tip_ta": "2003 FRBM சட்டம் -> 2004 12வது DCRF -> 2009 13வது வரைபடம் -> 2020 15வது பாதை.",
        "fact_en": "DCRF incentivized almost all Indian states to enact state-level FRBM legislation.",
        "fact_ta": "DCRF முறை அனைத்து இந்திய மாநிலங்களும் சொந்த FRBM சட்டங்களை இயற்ற ஊக்கமளித்தது."
    },
    # 11: B
    {
        "subtopic": "Horizontal Devolution Formula Evolution",
        "key": "B",
        "items": [
            ("14th FC introduces Forest Cover with 7.5% weight", "14வது ஆணையம் வனப் பரப்பளவை 7.5% எடையுடன் அறிமுகப்படுத்துதல்", 2014),
            ("First FC introduces 80% Population and 20% Collection formula", "1வது ஆணையம் 80% மக்கள் தொகை மற்றும் 20% வசூல் சூத்திரத்தை அறிமுகப்படுத்துதல்", 1952),
            ("15th FC incorporates Demographic Performance with 12.5% weight", "15வது ஆணையம் மக்கள்தொகை செயல்திறனை 12.5% எடையுடன் இணைத்தல்", 2020),
            ("8th FC unifies horizontal criteria based heavily on economic backwardness", "8வது ஆணையம் பொருளாதார பின்னடைவை அடிப்படையாகக் கொண்டு கிடைமட்ட அளவுகோல்களை ஒருங்கிணைத்தல்", 1984)
        ],
        "order": [2, 4, 1, 3], # 1952, 1984, 2014, 2020 -> 2, 4, 1, 3
        "tip_en": "1952 First FC -> 1984 8th FC -> 2014 14th FC -> 2020 15th FC.",
        "tip_ta": "1952 1வது ஆணையம் -> 1984 8வது ஆணையம் -> 2014 14வது ஆணையம் -> 2020 15வது ஆணையம்.",
        "fact_en": "Income distance and demographic indicators gradually replaced collection to enhance equity.",
        "fact_ta": "சமத்துவத்தை அதிகரிக்க வசூல் அளவுகோலுக்குப் பதிலாக வருமான இடைவெளி மற்றும் மக்கள் தொகை குறிகாட்டிகள் கொண்டுவரப்பட்டன."
    },
    # 12: B
    {
        "subtopic": "Finance Commission Reports Submission Chronology",
        "key": "B",
        "items": [
            ("14th FC submits final report for 2015-20 to President Pranab Mukherjee", "14வது ஆணையம் 2015-20 அறிக்கையை குடியரசுத் தலைவர் பிரணாப் முகர்ஜியிடம் சமர்ப்பித்தல்", 2014),
            ("10th FC submits Alternative Devolution report to President Shankar Dayal Sharma", "10வது ஆணையம் மாற்று வரிப் பகிர்வு அறிக்கையை குடியரசுத் தலைவர் சங்கர் தயாள் சர்மாவிடம் சமர்ப்பித்தல்", 1994),
            ("15th FC submits full 2021-26 report to President Ram Nath Kovind", "15வது ஆணையம் முழுமையான 2021-26 அறிக்கையை குடியரசுத் தலைவர் ராம் நாத் கோவிந்திடம் சமர்ப்பித்தல்", 2020),
            ("12th FC submits restructuring report to President A.P.J. Abdul Kalam", "12வது ஆணையம் நிதி மறுசீரமைப்பு அறிக்கையை குடியரசுத் தலைவர் அப்துல் கலாமிடம் சமர்ப்பித்தல்", 2004)
        ],
        "order": [2, 4, 1, 3], # 1994, 2004, 2014, 2020 -> 2, 4, 1, 3
        "tip_en": "1994 (10th FC) -> 2004 (12th FC) -> 2014 (14th FC) -> 2020 (15th FC).",
        "tip_ta": "1994 (10வது) -> 2004 (12வது) -> 2014 (14வது) -> 2020 (15வது).",
        "fact_en": "All reports are submitted to the President under Article 280 and laid before Parliament under Article 281.",
        "fact_ta": "அனைத்து அறிக்கைகளும் சரத்து 280-ன் கீழ் குடியரசுத் தலைவரிடம் சமர்ப்பிக்கப்பட்டு சரத்து 281-ன் கீழ் நாடாளுமன்றத்தில் வைக்கப்படுகின்றன."
    },
    # 13: B
    {
        "subtopic": "Landmark Federal Commissions on Union-State Finance",
        "key": "B",
        "items": [
            ("Punchhi Commission on Centre-State Relations submits its report", "மத்திய-மாநில உறவுகள் குறித்த பூஞ்சி ஆணையம் அறிக்கை சமர்ப்பித்தல்", 2010),
            ("Rajamannar Committee constituted by Tamil Nadu Government on federal finance", "கூட்டாட்சி நிதி குறித்து தமிழ்நாடு அரசால் ராஜமன்னார் குழு அமைக்கப்படுதல்", 1969),
            ("N.K. Singh FRBM Review Committee submits fiscal roadmap", "என்.கே. சிங் FRBM மறுஆய்வுக் குழு நிதி வரைபடத்தை சமர்ப்பித்தல்", 2017),
            ("Sarkaria Commission on Centre-State Relations submits recommendations", "மத்திய-மாநில உறவுகள் குறித்த சர்க்காரியா ஆணையம் பரிந்துரைகளை சமர்ப்பித்தல்", 1988)
        ],
        "order": [2, 4, 1, 3], # 1969, 1988, 2010, 2017 -> 2, 4, 1, 3
        "tip_en": "1969 Rajamannar -> 1988 Sarkaria -> 2010 Punchhi -> 2017 NK Singh Committee.",
        "tip_ta": "1969 ராஜமன்னார் -> 1988 சர்க்காரியா -> 2010 பூஞ்சி -> 2017 என்.கே. சிங் குழு.",
        "fact_en": "All these expert panels advocated strengthening the constitutional Finance Commission.",
        "fact_ta": "இந்த நிபுணர் குழுக்கள் அனைத்தும் அரசியலமைப்பு நிதி ஆணையத்தை வலுப்படுத்த பரிந்துரைத்தன."
    },
    # 14: C
    {
        "subtopic": "Finance Commission Member Lineage",
        "key": "C",
        "items": [
            ("Dr. C. Rangarajan heads Twelfth Finance Commission", "டாக்டர் சி. ரங்கராஜன் 12வது நிதி ஆணையத்திற்கு தலைமை தாங்குதல்", 2002),
            ("K.C. Neogy heads First Finance Commission", "கே.சி. நியோகி முதலாவது நிதி ஆணையத்திற்கு தலைமை தாங்குதல்", 1951),
            ("N.K. Singh heads Fifteenth Finance Commission", "என்.கே. சிங் 15வது நிதி ஆணையத்திற்கு தலைமை தாங்குதல்", 2017),
            ("K. Santhanam heads Second Finance Commission", "கே. சந்தானம் இரண்டாவது நிதி ஆணையத்திற்கு தலைமை தாங்குதல்", 1956)
        ],
        "order": [2, 4, 1, 3], # 1951, 1956, 2002, 2017 -> 2, 4, 1, 3
        "tip_en": "Neogy (1951) -> Santhanam (1956) -> Rangarajan (2002) -> NK Singh (2017).",
        "tip_ta": "நியோகி (1951) -> சந்தானம் (1956) -> ரங்கராஜன் (2002) -> என்.கே. சிங் (2017).",
        "fact_en": "K. Santhanam was a prominent member of the Constituent Assembly from Madras.",
        "fact_ta": "கே. சந்தானம் சென்னையைச் சேர்ந்த அரசியலமைப்பு நிர்ணய சபையின் முக்கிய உறுப்பினராவார்."
    },
    # 15: C
    {
        "subtopic": "Special Grant Innovations Chronology",
        "key": "C",
        "items": [
            ("13th FC introduces dedicated incentive grants for environmental forest cover", "13வது ஆணையம் சுற்றுச்சூழல் வனப் பரப்பிற்கான பிரத்யேக ஊக்க மானியங்களை அறிமுகப்படுத்துதல்", 2009),
            ("Sixth FC introduces non-plan capital grants for administrative upgradation", "6வது ஆணையம் நிர்வாக மேம்பாட்டிற்கான திட்டமில்லா மூலதன மானியங்களை அறிமுகப்படுத்துதல்", 1973),
            ("15th FC introduces performance grants for Million-Plus urban agglomerations", "15வது ஆணையம் பத்து லட்சத்திற்கும் அதிகமான மக்கள்தொகை கொண்ட நகரங்களுக்கான செயல்திறன் மானியங்களை அறிமுகப்படுத்துதல்", 2020),
            ("Eleventh FC introduces explicit funding earmarked for maintenance of civic roads", "11வது ஆணையம் நகர்ப்புற சாலைகள் பராமரிப்பிற்கான பிரத்யேக நிதியை அறிமுகப்படுத்துதல்", 2000)
        ],
        "order": [2, 4, 1, 3], # 1973, 2000, 2009, 2020 -> 2, 4, 1, 3
        "tip_en": "1973 (6th FC) -> 2000 (11th FC) -> 2009 (13th FC) -> 2020 (15th FC).",
        "tip_ta": "1973 (6வது) -> 2000 (11வது) -> 2009 (13வது) -> 2020 (15வது).",
        "fact_en": "Special grants have increasingly shifted from administrative brick-and-mortar to outcome-based metrics.",
        "fact_ta": "சிறப்பு மானியங்கள் நிர்வாக உள்கட்டமைப்பிலிருந்து இலக்கு சார்ந்த செயல்திறன் அளவீடுகளுக்கு மாறியுள்ளன."
    },
    # 16: C
    {
        "subtopic": "Decennial Census Integration Timeline",
        "key": "C",
        "items": [
            ("14th FC incorporates 2011 Census with 10% weight alongside 1971 Census (17.5%)", "14வது ஆணையம் 1971 கணக்கெடுப்புடன் (17.5%) 2011 கணக்கெடுப்பை 10% எடையுடன் இணைத்தல்", 2014),
            ("8th FC establishes practice of freezing population base strictly at 1971 Census", "8வது ஆணையம் மக்கள் தொகை அடிப்படையை 1971 கணக்கெடுப்பில் மட்டுமே முடக்கும் வழக்கத்தை நிறுவுதல்", 1984),
            ("15th FC uses 2011 Census exclusively for population with 15% weight", "15வது ஆணையம் மக்கள் தொகைக்கு 2011 கணக்கெடுப்பை மட்டுமே 15% எடையுடன் பயன்படுத்துதல்", 2020),
            ("First FC uses 1951 Census data for initial population allocation", "1வது ஆணையம் ஆரம்ப மக்கள் தொகை ஒதுக்கீட்டிற்கு 1951 கணக்கெடுப்புத் தரவைப் பயன்படுத்துதல்", 1952)
        ],
        "order": [4, 2, 1, 3], # 1952, 1984, 2014, 2020 -> 4, 2, 1, 3
        "tip_en": "1952 (1951 Census) -> 1984 (1971 Freeze) -> 2014 (Dual Census) -> 2020 (2011 Census exclusive).",
        "tip_ta": "1952 (1951 கணக்கெடுப்பு) -> 1984 (1971 முடக்கம்) -> 2014 (இரட்டை கணக்கெடுப்பு) -> 2020 (2011 மட்டுமே).",
        "fact_en": "The 1971 freeze was introduced to avoid penalizing states that controlled population growth.",
        "fact_ta": "மக்கள் தொகையைக் கட்டுப்படுத்திய மாநிலங்கள் பாதிக்கப்படுவதைத் தவிர்க்க 1971 முடக்கம் அறிமுகப்படுத்தப்பட்டது."
    },
    # 17: C
    {
        "subtopic": "GST and Indirect Tax Milestones",
        "key": "C",
        "items": [
            ("101st Constitutional Amendment Act brings CGST into Article 270 pool", "101வது அரசியலமைப்புத் திருத்தம் CGST-ஐ சரத்து 270 பகிர்வு நிதிக்குள் கொண்டுவருதல்", 2016),
            ("CENVAT introduced replacing the old MODVAT system", "பழைய MODVAT முறைக்கு பதிலாக CENVAT அறிமுகப்படுத்தப்படுதல்", 2000),
            ("15th FC recommends structural rationalization of inverted duty structures in GST", "15வது ஆணையம் ஜிஎஸ்டியில் தலைகீழ் வரி விகிதங்களை சீரமைக்க பரிந்துரைத்தல்", 2020),
            ("State VAT introduced across majority of Indian states", "பெரும்பாலான இந்திய மாநிலங்களில் மாநில வாட் (VAT) வரி அறிமுகப்படுத்தப்படுதல்", 2005)
        ],
        "order": [2, 4, 1, 3], # 2000, 2005, 2016, 2020 -> 2, 4, 1, 3
        "tip_en": "2000 CENVAT -> 2005 State VAT -> 2016 GST 101st CAA -> 2020 15th FC Recommendations.",
        "tip_ta": "2000 CENVAT -> 2005 வாட் வரி -> 2016 ஜிஎஸ்டி 101வது திருத்தம் -> 2020 15வது பரிந்துரைகள்.",
        "fact_en": "The GST Council was established under Article 279A following the 101st Amendment in 2016.",
        "fact_ta": "2016-ல் 101வது திருத்தத்தைத் தொடர்ந்து சரத்து 279A-ன் கீழ் ஜிஎஸ்டி கவுன்சில் அமைக்கப்பட்டது."
    },
    # 18: C
    {
        "subtopic": "Award Period Implementation Timeline",
        "key": "C",
        "items": [
            ("Award period of 14th Finance Commission (2015-2020)", "14வது நிதி ஆணையத்தின் செயல்பாட்டுக் காலம் (2015-2020)", 2015),
            ("Award period of 12th Finance Commission (2005-2010)", "12வது நிதி ஆணையத்தின் செயல்பாட்டுக் காலம் (2005-2010)", 2005),
            ("Award period of 15th Finance Commission main report (2021-2026)", "15வது நிதி ஆணையத்தின் முதன்மை அறிக்கை செயல்பாட்டுக் காலம் (2021-2026)", 2021),
            ("Award period of 13th Finance Commission (2010-2015)", "13வது நிதி ஆணையத்தின் செயல்பாட்டுக் காலம் (2010-2015)", 2010)
        ],
        "order": [2, 4, 1, 3], # 2005, 2010, 2015, 2021 -> 2, 4, 1, 3
        "tip_en": "12th FC (2005-10) -> 13th FC (2010-15) -> 14th FC (2015-20) -> 15th FC (2021-26).",
        "tip_ta": "12வது (2005-10) -> 13வது (2010-15) -> 14வது (2015-20) -> 15வது (2021-26).",
        "fact_en": "The 15th FC covered six years in total (interim year 2020-21 plus five years 2021-26).",
        "fact_ta": "15வது ஆணையம் மொத்தம் ஆறு ஆண்டுகளை உள்ளடக்கியது (இடைக்கால ஆண்டு 2020-21 + ஐந்து ஆண்டுகள் 2021-26)."
    },
    # 19: C
    {
        "subtopic": "Sixteenth Finance Commission Operational Timeline",
        "key": "C",
        "items": [
            ("Appointment of four full-time and part-time members of 16th FC", "16வது ஆணையத்தின் நான்கு முழுநேர மற்றும் பகுதிநேர உறுப்பினர்கள் நியமனம்", 2024),
            ("Presidential notification constituting 16th FC under Dr. Arvind Panagariya", "டாக்டர் அரவிந்த் பனகாரியா தலைமையில் 16வது ஆணையத்தை அமைக்கும் குடியரசுத் தலைவர் அறிவிக்கை", 2023),
            ("Commencement of 16th Finance Commission award period", "16வது நிதி ஆணையத்தின் செயல்பாட்டுக் காலம் தொடங்குதல்", 2026),
            ("Mandated deadline for submission of 16th FC report to President", "குடியரசுத் தலைவரிடம் 16வது ஆணைய அறிக்கை சமர்ப்பிப்பதற்கான காலக்கெடு", 2025)
        ],
        "order": [2, 1, 4, 3], # 2023, 2024, 2025, 2026 -> 2, 1, 4, 3
        "tip_en": "Dec 2023 (Notification) -> Jan 2024 (Members) -> Oct 2025 (Submission) -> April 2026 (Award Period).",
        "tip_ta": "டிச 2023 (அறிவிக்கை) -> ஜன 2024 (உறுப்பினர்கள்) -> அக் 2025 (சமர்ப்பிப்பு) -> ஏப் 2026 (செயல்பாட்டுக் காலம்).",
        "fact_en": "The 16th FC award period will run for five years from April 1, 2026 to March 31, 2031.",
        "fact_ta": "16வது ஆணையத்தின் பரிந்துரைக் காலம் ஏப்ரல் 1, 2026 முதல் மார்ச் 31, 2031 வரை ஐந்து ஆண்டுகள் நீடிக்கும்."
    },
    # 20: D
    {
        "subtopic": "Chairmen Lineage: Tyagi to Panagariya",
        "key": "D",
        "items": [
            ("Dr. Vijay Kelkar appointed Chairman of Thirteenth Finance Commission", "டாக்டர் விஜய் கேல்கர் 13வது நிதி ஆணையத்தின் தலைவராக நியமிக்கப்படுதல்", 2007),
            ("Mahavir Tyagi appointed Chairman of Fifth Finance Commission", "மகாவீர் தியாகி 5வது நிதி ஆணையத்தின் தலைவராக நியமிக்கப்படுதல்", 1968),
            ("Dr. Arvind Panagariya appointed Chairman of Sixteenth Finance Commission", "டாக்டர் அரவிந்த் பனகாரியா 16வது நிதி ஆணையத்தின் தலைவராக நியமிக்கப்படுதல்", 2023),
            ("N.K.P. Salve appointed Chairman of Ninth Finance Commission", "என்.கே.பி. சால்வே 9வது நிதி ஆணையத்தின் தலைவராக நியமிக்கப்படுதல்", 1987)
        ],
        "order": [2, 4, 1, 3], # 1968, 1987, 2007, 2023 -> 2, 4, 1, 3
        "tip_en": "Tyagi (1968) -> Salve (1987) -> Kelkar (2007) -> Panagariya (2023).",
        "tip_ta": "தியாகி (1968) -> சால்வே (1987) -> கேல்கர் (2007) -> பனகாரியா (2023).",
        "fact_en": "Dr. Panagariya previously served as the first Vice Chairman of NITI Aayog.",
        "fact_ta": "டாக்டர் பனகாரியா முன்னர் நிதி ஆயோக்கின் முதல் துணைத் தலைவராகப் பணியாற்றினார்."
    },
    # 21: D
    {
        "subtopic": "Historic Fiscal Milestones of Indian Union",
        "key": "D",
        "items": [
            ("80th Constitutional Amendment Act passes into law", "80வது அரசியலமைப்புத் திருத்தச் சட்டம் சட்டமாக நிறைவேறுதல்", 2000),
            ("Constitution of India enters into force containing Articles 280-281", "சரத்துகள் 280-281 கொண்ட இந்திய அரசியலமைப்பு நடைமுறைக்கு வருதல்", 1950),
            ("Goods and Services Tax (GST) rollout across India", "இந்தியா முழுவதும் சரக்கு மற்றும் சேவை வரி (GST) அமல்படுத்தப்படுதல்", 2017),
            ("Abolition of the Planning Commission of India", "இந்திய திட்டக் குழு கலைக்கப்படுதல்", 2014)
        ],
        "order": [2, 1, 4, 3], # 1950, 2000, 2014, 2017 -> 2, 1, 4, 3
        "tip_en": "1950 Constitution -> 2000 80th CAA -> 2014 Planning Commission Abolition -> 2017 GST Rollout.",
        "tip_ta": "1950 அரசியலமைப்பு -> 2000 80வது திருத்தம் -> 2014 திட்டக் குழு கலைப்பு -> 2017 ஜிஎஸ்டி அமல்.",
        "fact_en": "GST replaced multi-tiered indirect taxes with a unified national value-added tax.",
        "fact_ta": "ஜிஎஸ்டி பல அடுக்கு மறைமுக வரிகளுக்கு பதிலாக ஒரு ஒருங்கிணைந்த தேசிய மதிப்புக் கூட்டு வரியைக் கொண்டுவந்தது."
    },
    # 22: D
    {
        "subtopic": "Evolution of Equalization Criteria",
        "key": "D",
        "items": [
            ("12th FC refines Income Distance calculation using comparable GSDP series", "12வது ஆணையம் ஒப்பீட்டு GSDP தொடரைப் பயன்படுத்தி வருமான இடைவெளியைச் செம்மைப்படுத்துதல்", 2004),
            ("7th FC introduces poverty ratio as an explicit redistribution indicator", "7வது ஆணையம் வறுமை விகிதத்தை ஒரு வெளிப்படையான மறுபகிர்வு குறிகாட்டியாக அறிமுகப்படுத்துதல்", 1978),
            ("15th FC introduces Tax Effort with 2.5% weight to reward own revenue mobilization", "15வது ஆணையம் சொந்த வருவாய் திரட்டலை ஊக்குவிக்க 2.5% எடையுடன் வரி முயற்சியை அறிமுகப்படுத்துதல்", 2020),
            ("10th FC adopts Area criterion with 5% weight for the first time", "10வது ஆணையம் பரப்பளவு அளவுகோலை முதல்முறையாக 5% எடையுடன் ஏற்றுக்கொள்வது", 1994)
        ],
        "order": [2, 4, 1, 3], # 1978, 1994, 2004, 2020 -> 2, 4, 1, 3
        "tip_en": "1978 (7th FC) -> 1994 (10th FC) -> 2004 (12th FC) -> 2020 (15th FC).",
        "tip_ta": "1978 (7வது) -> 1994 (10வது) -> 2004 (12வது) -> 2020 (15வது).",
        "fact_en": "The Tax Effort criterion prevents states from under-taxing while expecting central compensation.",
        "fact_ta": "மத்திய மானியங்களை எதிர்பார்த்து மாநிலங்கள் வேண்டுமென்றே வரி வசூலைக் குறைப்பதைத் தடுக்க வரி முயற்சி உதவுகிறது."
    },
    # 23: D
    {
        "subtopic": "Major Landmark Constitutional Amendments",
        "key": "D",
        "items": [
            ("88th Constitutional Amendment proposes Service Tax insertion under Art 268A", "88வது அரசியலமைப்புத் திருத்தம் சரத்து 268A-ன் கீழ் சேவை வரியைச் சேர்க்க முன்மொழிதல்", 2003),
            ("7th Constitutional Amendment Act reorganizes Indian States", "7வது அரசியலமைப்புத் திருத்தச் சட்டம் இந்திய மாநிலங்களை மறுசீரமைத்தல்", 1956),
            ("101st Constitutional Amendment Act introduces GST and GST Council", "101வது திருத்தச் சட்டம் GST மற்றும் GST கவுன்சிலை அறிமுகப்படுத்துதல்", 2016),
            ("80th Constitutional Amendment Act pools central tax revenues", "80வது அரசியலமைப்புத் திருத்தச் சட்டம் மத்திய வரி வருவாய்களை ஒன்றிணைத்தல்", 2000)
        ],
        "order": [2, 4, 1, 3], # 1956, 2000, 2003, 2016 -> 2, 4, 1, 3
        "tip_en": "1956 7th CAA -> 2000 80th CAA -> 2003 88th CAA -> 2016 101st CAA.",
        "tip_ta": "1956 7வது திருத்தம் -> 2000 80வது திருத்தம் -> 2003 88வது திருத்தம் -> 2016 101வது திருத்தம்.",
        "fact_en": "Article 268A proposed by the 88th CAA was never formally notified and was later omitted by GST.",
        "fact_ta": "88வது திருத்தத்தால் முன்மொழியப்பட்ட சரத்து 268A அறிவிக்கப்படவே இல்லை; பின்னர் GST மூலம் நீக்கப்பட்டது."
    },
    # 24: D
    {
        "subtopic": "Modern Commission Devolution Milestones",
        "key": "D",
        "items": [
            ("13th FC recommends vertical devolution of 32%", "13வது ஆணையம் 32% செங்குத்து வரிப் பகிர்வை பரிந்துரைத்தல்", 2009),
            ("11th FC recommends vertical devolution of 29.5%", "11வது ஆணையம் 29.5% செங்குத்து வரிப் பகிர்வை பரிந்துரைத்தல்", 2000),
            ("15th FC recommends vertical devolution of 41%", "15வது ஆணையம் 41% செங்குத்து வரிப் பகிர்வை பரிந்துரைத்தல்", 2020),
            ("14th FC recommends vertical devolution of 42%", "14வது ஆணையம் 42% செங்குத்து வரிப் பகிர்வை பரிந்துரைத்தல்", 2014)
        ],
        "order": [2, 1, 4, 3], # 2000, 2009, 2014, 2020 -> 2, 1, 4, 3
        "tip_en": "2000 (29.5%) -> 2009 (32%) -> 2014 (42%) -> 2020 (41%).",
        "tip_ta": "2000 (29.5%) -> 2009 (32%) -> 2014 (42%) -> 2020 (41%).",
        "fact_en": "The leap from 32% to 42% in 2014 was the largest single-step vertical increase in FC history.",
        "fact_ta": "2014-ல் 32%-லிருந்து 42%-ஆக உயர்ந்ததே நிதி ஆணைய வரலாற்றின் மிகப்பெரிய ஒற்றை படி உயர்வு ஆகும்."
    },
    # 25: D
    {
        "subtopic": "Panchayati Raj Financial Milestones",
        "key": "D",
        "items": [
            ("Ashok Mehta Committee recommends strengthening Panchayat financial powers", "அசோக் மேத்தா குழு பஞ்சாயத்துகளின் நிதி அதிகாரங்களை வலுப்படுத்த பரிந்துரைத்தல்", 1978),
            ("Balwant Rai Mehta Committee recommends three-tier Panchayati Raj system", "பல்வந்த் ராய் மேத்தா குழு மூன்றடுக்கு பஞ்சாயத்து ராஜ் முறையை பரிந்துரைத்தல்", 1957),
            ("15th Finance Commission mandates AuditOnline transparency for PRIs", "15வது நிதி ஆணையம் பஞ்சாயத்துகளுக்கு AuditOnline வெளிப்படைத்தன்மையை கட்டாயமாக்குதல்", 2020),
            ("73rd Constitutional Amendment Act adds Eleventh Schedule (29 matters)", "73வது அரசியலமைப்புத் திருத்தச் சட்டம் பதினோராவது அட்டவணையைச் சேர்த்தல் (29 துறைகள்)", 1992)
        ],
        "order": [2, 1, 4, 3], # 1957, 1978, 1992, 2020 -> 2, 1, 4, 3
        "tip_en": "1957 Balwant Rai -> 1978 Ashok Mehta -> 1992 73rd CAA -> 2020 15th FC AuditOnline.",
        "tip_ta": "1957 பல்வந்த் ராய் -> 1978 அசோக் மேத்தா -> 1992 73வது திருத்தம் -> 2020 15வது AuditOnline.",
        "fact_en": "AuditOnline ensures all local body spending is publicly visible with verified digital audit trails.",
        "fact_ta": "AuditOnline தளம் அனைத்து உள்ளாட்சி செலவினங்களும் சரிபார்க்கப்பட்ட டிஜிட்டல் தணிக்கையுடன் பொதுமக்களுக்குத் தெரிவதை உறுதி செய்கிறது."
    }
]

def build_questions():
    questions = []
    for idx, item in enumerate(raw_chrono_data, start=1):
        qid = f"FC_C_{idx:03d}"
        itms = item["items"]
        
        # Presented order is 1, 2, 3, 4 as given in item["items"]
        stem_items_en = "\n".join([f"{i+1}. {itms[i][0]}" for i in range(4)])
        stem_items_ta = "\n".join([f"{i+1}. {itms[i][1]}" for i in range(4)])
        
        stem_en = f"Arrange the following events in the history of Indian fiscal federalism and the Finance Commission in correct chronological order:\n{stem_items_en}\nSelect the correct answer using the code given below:"
        stem_ta = f"இந்திய நிதி கூட்டாட்சி மற்றும் நிதி ஆணைய வரலாற்றில் பின்வரும் நிகழ்வுகளை சரியான காலவரிசைப்படி ஒழுங்கமைக்கவும்:\n{stem_items_ta}\nகீழே கொடுக்கப்பட்டுள்ள குறியீட்டைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:"
        
        c_order = item["order"] # correct order of indices e.g. [2, 4, 1, 3]
        correct_seq_str = " - ".join(str(x) for x in c_order)
        
        # Create distractors
        dist1 = f"{c_order[1]} - {c_order[0]} - {c_order[2]} - {c_order[3]}"
        dist2 = f"{c_order[0]} - {c_order[2]} - {c_order[1]} - {c_order[3]}"
        dist3 = f"{c_order[3]} - {c_order[2]} - {c_order[1]} - {c_order[0]}"
        
        correct_k = item["key"]
        
        if correct_k == "A":
            o_en = [correct_seq_str, dist1, dist2, dist3]
        elif correct_k == "B":
            o_en = [dist1, correct_seq_str, dist2, dist3]
        elif correct_k == "C":
            o_en = [dist1, dist2, correct_seq_str, dist3]
        else: # D
            o_en = [dist1, dist2, dist3, correct_seq_str]
            
        o_ta = [x for x in o_en]
        
        # Build explanation with 4-digit years and sequence arrows '->'
        exp_lines_en = []
        for rank, item_idx in enumerate(c_order, start=1):
            name = itms[item_idx-1][0]
            yr = itms[item_idx-1][2]
            exp_lines_en.append(f"{rank}. {name} ({yr})")
        seq_arrow_en = " -> ".join([str(x) for x in c_order])
        full_exp_en = "The correct chronological sequence is " + seq_arrow_en + ":\n" + "\n".join(exp_lines_en)
        
        exp_lines_ta = []
        for rank, item_idx in enumerate(c_order, start=1):
            name = itms[item_idx-1][1]
            yr = itms[item_idx-1][2]
            exp_lines_ta.append(f"{rank}. {name} ({yr})")
        full_exp_ta = "சரியான காலவரிசை " + seq_arrow_en + " ஆகும்:\n" + "\n".join(exp_lines_ta)
        
        why_en = {
            "A": f"Option A matches the chronological sequence: {seq_arrow_en}." if correct_k == "A" else "Option A does not reflect the chronological order.",
            "B": f"Option B matches the chronological sequence: {seq_arrow_en}." if correct_k == "B" else "Option B does not reflect the chronological order.",
            "C": f"Option C matches the chronological sequence: {seq_arrow_en}." if correct_k == "C" else "Option C does not reflect the chronological order.",
            "D": f"Option D matches the chronological sequence: {seq_arrow_en}." if correct_k == "D" else "Option D does not reflect the chronological order."
        }
        why_ta = {
            "A": f"தெரிவு A சரியான காலவரிசையோடு பொருந்துகிறது: {seq_arrow_en}." if correct_k == "A" else "தெரிவு A சரியான காலவரிசை அல்ல.",
            "B": f"தெரிவு B சரியான காலவரிசையோடு பொருந்துகிறது: {seq_arrow_en}." if correct_k == "B" else "தெரிவு B சரியான காலவரிசை அல்ல.",
            "C": f"தெரிவு C சரியான காலவரிசையோடு பொருந்துகிறது: {seq_arrow_en}." if correct_k == "C" else "தெரிவு C சரியான காலவரிசை அல்ல.",
            "D": f"தெரிவு D சரியான காலவரிசையோடு பொருந்துகிறது: {seq_arrow_en}." if correct_k == "D" else "தெரிவு D சரியான காலவரிசை அல்ல."
        }
        
        q = make_fc_q(
            qid=qid,
            diff="Hard",
            qtype="Chronology",
            subtopic=item["subtopic"],
            en_stem=stem_en,
            ta_stem=stem_ta,
            en_a=o_en[0],
            ta_a=o_ta[0],
            en_b=o_en[1],
            ta_b=o_ta[1],
            en_c=o_en[2],
            ta_c=o_ta[2],
            en_d=o_en[3],
            ta_d=o_ta[3],
            correct_key=correct_k,
            exp_en=full_exp_en,
            exp_ta=full_exp_ta,
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
            tags=["polity", "finance_commission", "chronology", item["subtopic"].lower().replace(" ", "_")]
        )
        questions.append(q)
    return questions

if __name__ == "__main__":
    qs = build_questions()
    print(f"Generated {len(qs)} Chronology questions for Finance Commission.")
    assert len(qs) == 25, f"Expected 25 questions, got {len(qs)}"
    
    out_path = os.path.join("data", "questions", "polity", "fc_chronology.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, ensure_ascii=False, indent=2)
    print(f"Saved Chronology MCQs to {out_path}")
    
    val = ContentValidator()
    report = val.validate_file(out_path, expected_count=25, expected_prefix="FC_C_")
    print(f"ContentValidator: {'PASS' if report.is_valid else 'FAIL'} | Total: {report.total_audited}")
    if not report.is_valid:
        for iss in report.issues[:10]:
            print(f"  Issue: {iss}")
    print(f"Key Distribution: {report.key_distribution}")
    
    chrono_val = ChronologyValidator()
    c_report = chrono_val.validate_file(out_path)
    print(f"ChronologyValidator: {'PASS' if c_report.is_valid else 'FAIL'}")
    if not c_report.is_valid:
        for iss in c_report.issues[:10]:
            print(f"  Chrono Issue: {iss}")
