# -*- coding: utf-8 -*-
"""
Build 50 PYQ Practice MCQs for Finance Commission of India
ID range: FC_PYQ_001 to FC_PYQ_050
Target key balance: {'A': 13, 'B': 13, 'C': 12, 'D': 12}
"""

import json
import os
import shutil
from fc_mcq_helper import make_fc_q
from tools.nova_content_engine.validator import ContentValidator

raw_pyq_items = [
    # 1: A
    {
        "subtopic": "Constitutional Article (TNPSC Gr 1 2017)",
        "key": "A",
        "en_stem": "According to the Indian Constitution, under which Article is the Finance Commission of India constituted by the President?",
        "ta_stem": "இந்திய அரசியலமைப்பின்படி, எந்தச் சரத்தின் கீழ் குடியரசுத் தலைவரால் இந்திய நிதி ஆணையம் அமைக்கப்படுகிறது?",
        "a": ("Article 280", "சரத்து 280"),
        "b": ("Article 275", "சரத்து 275"),
        "c": ("Article 268", "சரத்து 268"),
        "d": ("Article 282", "சரத்து 282"),
        "exp_en": "Article 280 of the Constitution mandates the constitution of a Finance Commission by the President every five years.",
        "exp_ta": "அரசியலமைப்பின் சரத்து 280, ஒவ்வொரு ஐந்து வருடங்களுக்கும் குடியரசுத் தலைவரால் நிதி ஆணையம் அமைக்கப்பட வேண்டும் என்று கட்டாயப்படுத்துகிறது.",
        "tip_en": "PYQ recurring classic: Article 280 governs the Finance Commission.",
        "tip_ta": "அடிக்கடி கேட்கப்படும் வினா: சரத்து 280 நிதி ஆணையத்தை நிர்வகிக்கிறது.",
        "fact_en": "Article 280 was moved in the Constituent Assembly to ensure periodic adjustment of federal revenues.",
        "fact_ta": "கூட்டாட்சி வருவாய்களை அவ்வப்போது சீரமைப்பதை உறுதி செய்வதற்காக சரத்து 280 கொண்டுவரப்பட்டது."
    },
    # 2: B
    {
        "subtopic": "First Chairman (TNPSC Gr 2 2015)",
        "key": "B",
        "en_stem": "Who was the Chairman of the First Finance Commission of India constituted in 1951?",
        "ta_stem": "1951 ஆம் ஆண்டு அமைக்கப்பட்ட இந்தியாவின் முதலாவது நிதி ஆணையத்தின் தலைவர் யார்?",
        "a": ("K. Santhanam", "கே. சந்தானம்"),
        "b": ("K.C. Neogy", "கே.சி. நியோகி"),
        "c": ("A.K. Chanda", "ஏ.கே. சந்தா"),
        "d": ("Mahavir Tyagi", "மகாவீர் தியாகி"),
        "exp_en": "Kshitish Chandra Neogy (K.C. Neogy) was appointed the Chairman of the First Finance Commission on November 22, 1951.",
        "exp_ta": "ஷிதிஷ் சந்திர நியோகி (கே.சி. நியோகி) நவம்பர் 22, 1951 அன்று முதலாவது நிதி ஆணையத்தின் தலைவராக நியமிக்கப்பட்டார்.",
        "tip_en": "K.C. Neogy served as the 1st FC Chairman; K. Santhanam was the 2nd.",
        "tip_ta": "கே.சி. நியோகி 1வது தலைவராக இருந்தார்; கே. சந்தானம் 2வது தலைவராக இருந்தார்.",
        "fact_en": "The First Commission submitted its report in 1952 recommending 55% income tax devolution.",
        "fact_ta": "முதலாவது ஆணையம் 1952-ல் அறிக்கை சமர்ப்பித்து 55% வருமான வரிப் பகிர்வை பரிந்துரைத்தது."
    },
    # 3: C
    {
        "subtopic": "Appointment Authority (TNPSC Gr 4 2018)",
        "key": "C",
        "en_stem": "Who appoints the Chairman and other members of the Finance Commission of India?",
        "ta_stem": "இந்திய நிதி ஆணையத்தின் தலைவர் மற்றும் பிற உறுப்பினர்களை நியமிப்பவர் யார்?",
        "a": ("The Prime Minister of India", "இந்தியப் பிரதமர்"),
        "b": ("The Speaker of Lok Sabha", "மக்களவைத் தலைவர்"),
        "c": ("The President of India", "இந்தியக் குடியரசுத் தலைவர்"),
        "d": ("The Union Finance Minister", "மத்திய நிதி அமைச்சர்"),
        "exp_en": "Under Article 280(1), the Chairman and four other members of the Finance Commission are appointed by the President of India.",
        "exp_ta": "சரத்து 280(1)-ன் கீழ், நிதி ஆணையத்தின் தலைவர் மற்றும் நான்கு பிற உறுப்பினர்கள் இந்தியக் குடியரசுத் தலைவரால் நியமிக்கப்படுகிறார்கள்.",
        "tip_en": "All members are appointed by Presidential order under Article 280.",
        "tip_ta": "அனைத்து உறுப்பினர்களும் சரத்து 280-ன் கீழ் குடியரசுத் தலைவர் ஆணையால் நியமிக்கப்படுகிறார்கள்.",
        "fact_en": "Appointments are made on the advice of the Union Cabinet.",
        "fact_ta": "மத்திய அமைச்சரவையின் ஆலோசனையின் பேரிலேயே இந்த நியமனங்கள் செய்யப்படுகின்றன."
    },
    # 4: D
    {
        "subtopic": "Tabling Requirement (TNPSC Gr 1 2019)",
        "key": "D",
        "en_stem": "Under Article 281 of the Indian Constitution, before whom is the recommendation of the Finance Commission laid?",
        "ta_stem": "இந்திய அரசியலமைப்பின் சரத்து 281-ன் கீழ், நிதி ஆணையத்தின் பரிந்துரைகள் யாருக்கு முன்னால் சமர்ப்பிக்கப்படுகின்றன?",
        "a": ("The Supreme Court of India", "இந்திய உச்ச நீதிமன்றம்"),
        "b": ("The NITI Aayog Governing Council", "நிதி ஆயோக் ஆளும் குழு"),
        "c": ("The Inter-State Council", "மாநிலங்களுக்கு இடையேயான கவுன்சில்"),
        "d": ("Each House of Parliament", "நாடாளுமன்றத்தின் இரு அவைகள்"),
        "exp_en": "Article 281 requires the President to cause every recommendation made by the Finance Commission together with an explanatory memorandum to be laid before each House of Parliament.",
        "exp_ta": "சரத்து 281, நிதி ஆணையத்தின் ஒவ்வொரு பரிந்துரையையும் அதற்கான விளக்கக் குறிப்புடன் நாடாளுமன்றத்தின் இரு அவைகளிலும் வைக்க குடியரசுத் தலைவரைப் பணிக்கிறது.",
        "tip_en": "Article 281: Tabling before both Lok Sabha and Rajya Sabha.",
        "tip_ta": "சரத்து 281: மக்களவை மற்றும் மாநிலங்களவை ஆகிய இரு அவைகளிலும் சமர்ப்பித்தல்.",
        "fact_en": "The explanatory memorandum details action taken on the recommendations.",
        "fact_ta": "விளக்கக் குறிப்பு பரிந்துரைகள் மீது எடுக்கப்பட்ட நடவடிக்கைகளை விவரிக்கிறது."
    },
    # 5: A
    {
        "subtopic": "Statutory Act (TNPSC Gr 2 2018)",
        "key": "A",
        "en_stem": "In which year did the Indian Parliament enact the Finance Commission (Miscellaneous Provisions) Act to prescribe qualifications for members?",
        "ta_stem": "உறுப்பினர்களுக்கான தகுதிகளை நிர்ணயிப்பதற்காக இந்திய நாடாளுமன்றம் எந்த ஆண்டில் நிதி ஆணைய (இதர விதிகள்) சட்டத்தை இயற்றியது?",
        "a": ("1951", "1951"),
        "b": ("1950", "1950"),
        "c": ("1952", "1952"),
        "d": ("1955", "1955"),
        "exp_en": "The Finance Commission (Miscellaneous Provisions) Act was enacted by Parliament in 1951 pursuant to Article 280(2).",
        "exp_ta": "சரத்து 280(2)-ன் படி நாடாளுமன்றத்தால் 1951-ல் நிதி ஆணைய (இதர விதிகள்) சட்டம் இயற்றப்பட்டது.",
        "tip_en": "Enacted in 1951, the same year the First Finance Commission was appointed.",
        "tip_ta": "முதலாவது நிதி ஆணையம் அமைக்கப்பட்ட அதே 1951 ஆம் ஆண்டிலேயே இச்சட்டம் இயற்றப்பட்டது.",
        "fact_en": "The Act has eight sections laying down composition, qualifications, and powers.",
        "fact_ta": "இச்சட்டம் அமைப்பு, தகுதிகள் மற்றும் அதிகாரங்களை வகுக்கும் எட்டு பிரிவுகளைக் கொண்டுள்ளது."
    },
    # 6: B
    {
        "subtopic": "Total Membership (TNPSC Gr 4 2016)",
        "key": "B",
        "en_stem": "What is the total membership of the Finance Commission including the Chairman as per Article 280?",
        "ta_stem": "சரத்து 280-ன் படி தலைவரையும் சேர்த்து நிதி ஆணையத்தின் மொத்த உறுப்பினர்களின் எண்ணிக்கை யாது?",
        "a": ("3 members", "3 உறுப்பினர்கள்"),
        "b": ("5 members", "5 உறுப்பினர்கள்"),
        "c": ("7 members", "7 உறுப்பினர்கள்"),
        "d": ("4 members", "4 உறுப்பினர்கள்"),
        "exp_en": "Article 280(1) prescribes that the Finance Commission shall consist of a Chairman and four other members, making a total of 5 members.",
        "exp_ta": "சரத்து 280(1), நிதி ஆணையம் ஒரு தலைவர் மற்றும் நான்கு பிற உறுப்பினர்களைக் கொண்டிருக்கும் என்று கூறுகிறது, எனவே மொத்தம் 5 உறுப்பினர்கள்.",
        "tip_en": "1 Chairman + 4 Members = 5 total members.",
        "tip_ta": "1 தலைவர் + 4 உறுப்பினர்கள் = மொத்தம் 5 உறுப்பினர்கள்.",
        "fact_en": "Members can be appointed on a full-time or part-time basis.",
        "fact_ta": "உறுப்பினர்கள் முழுநேர அல்லது பகுதிநேர அடிப்படையில் நியமிக்கப்படலாம்."
    },
    # 7: C
    {
        "subtopic": "14th FC Chairman (TNPSC Gr 1 2015)",
        "key": "C",
        "en_stem": "Who served as the Chairman of the Fourteenth Finance Commission of India?",
        "ta_stem": "இந்தியாவின் பதினான்காவது நிதி ஆணையத்தின் தலைவராகப் பணியாற்றியவர் யார்?",
        "a": ("Dr. C. Rangarajan", "டாக்டர் சி. ரங்கராஜன்"),
        "b": ("Dr. Vijay Kelkar", "டாக்டர் விஜய் கேல்கர்"),
        "c": ("Dr. Y.V. Reddy", "டாக்டர் ஒய்.வி. ரெட்டி"),
        "d": ("N.K. Singh", "என்.கே. சிங்"),
        "exp_en": "Former RBI Governor Dr. Y.V. Reddy chaired the Fourteenth Finance Commission constituted in January 2013.",
        "exp_ta": "ரிசர்வ் வங்கியின் முன்னாள் ஆளுநர் டாக்டர் ஒய்.வி. ரெட்டி ஜனவரி 2013-ல் அமைக்கப்பட்ட 14வது நிதி ஆணையத்திற்கு தலைமை தாங்கினார்.",
        "tip_en": "14th FC: Dr. Y.V. Reddy; 15th FC: N.K. Singh.",
        "tip_ta": "14வது ஆணையம்: டாக்டர் ஒய்.வி. ரெட்டி; 15வது ஆணையம்: என்.கே. சிங்.",
        "fact_en": "The 14th FC made the landmark recommendation of 42% tax devolution.",
        "fact_ta": "14வது ஆணையம் 42% வரிப் பகிர்வு என்ற வரலாற்றுப் பரிந்துரையை வழங்கியது."
    },
    # 8: D
    {
        "subtopic": "14th FC Devolution Share (TNPSC Gr 2 2016)",
        "key": "D",
        "en_stem": "What percentage of net shareable central tax proceeds was recommended for States by the 14th Finance Commission?",
        "ta_stem": "14வது நிதி ஆணையத்தால் மாநிலங்களுக்கு நிகர மத்திய வரி வருவாயில் எத்தனை சதவீதம் பரிந்துரைக்கப்பட்டது?",
        "a": ("32%", "32%"),
        "b": ("38%", "38%"),
        "c": ("40%", "40%"),
        "d": ("42%", "42%"),
        "exp_en": "The 14th Finance Commission recommended a historic jump in vertical devolution from 32% to 42% of the divisible pool.",
        "exp_ta": "14வது நிதி ஆணையம் பகிர்வு நிதியில் செங்குத்து வரிப் பகிர்வை 32%-லிருந்து வரலாற்றுச் சிறப்புமிக்க 42% ஆக உயர்த்த பரிந்துரைத்தது.",
        "tip_en": "Peak devolution in Indian fiscal history was 42% under 14th FC.",
        "tip_ta": "இந்திய நிதி வரலாற்றில் உச்சபட்ச வரிப் பகிர்வு 14வது ஆணையத்தின் கீழான 42% ஆகும்.",
        "fact_en": "This provided unprecedented untied fiscal space to state budgets.",
        "fact_ta": "இது மாநில பட்ஜெட்டுகளுக்கு முன்னோடியில்லாத நிபந்தனையற்ற நிதி தன்னாட்சியை வழங்கியது."
    },
    # 9: A
    {
        "subtopic": "Nature of Recommendations (TNPSC Gr 1 2014)",
        "key": "A",
        "en_stem": "What is the legal character of the recommendations submitted by the Finance Commission to the Central Government?",
        "ta_stem": "மத்திய அரசுக்கு நிதி ஆணையம் சமர்ப்பிக்கும் பரிந்துரைகளின் சட்டப்பூர்வ தன்மை யாது?",
        "a": ("Advisory in nature and not legally binding", "ஆலோசனை இயல்புடையவை மற்றும் சட்டப்பூர்வமாகக் கட்டுப்படுத்தாதவை"),
        "b": ("Mandatory and legally binding as a court decree", "கட்டாயமானவை மற்றும் நீதிமன்றத் தீர்ப்பு போல கட்டுப்படுத்துபவை"),
        "c": ("Subject to presidential veto without explanation", "விளக்கமின்றி குடியரசுத் தலைவரின் மறுப்புரிமைக்கு உட்பட்டவை"),
        "d": ("Statutorily enforceable by the Supreme Court", "உச்ச நீதிமன்றத்தால் சட்டப்பூர்வமாக செயல்படுத்தப்படக் கூடியவை"),
        "exp_en": "The recommendations of the Finance Commission are advisory in nature and not legally binding on the Government.",
        "exp_ta": "நிதி ஆணையத்தின் பரிந்துரைகள் ஆலோசனை இயல்புடையவையே தவிர மத்திய அரசைக் கட்டுப்படுத்தும் சட்டப்பூர்வ கட்டாயம் கொண்டவை அல்ல.",
        "tip_en": "By convention, Central Governments accept the core devolution recommendations.",
        "tip_ta": "பாரம்பரிய மரபின்படி, மத்திய அரசுகள் முக்கிய வரிப் பகிர்வு பரிந்துரைகளை ஏற்றுக்கொள்கின்றன.",
        "fact_en": "Dr. P.V. Rajamannar noted that as a constitutional body, its advice carries enormous moral authority.",
        "fact_ta": "ஓர் அரசியலமைப்பு அமைப்பு என்பதால் இதன் ஆலோசனை மகத்தான தார்மீக அதிகாரத்தைக் கொண்டுள்ளது என ராஜமன்னார் குறிப்பிட்டார்."
    },
    # 10: B
    {
        "subtopic": "Panchayats Augmentation (TNPSC Gr 2A 2017)",
        "key": "B",
        "en_stem": "Which clause of Article 280(3) empowers the Finance Commission to recommend measures to augment the Consolidated Fund of a State to supplement the resources of the Panchayats?",
        "ta_stem": "பஞ்சாயத்துகளின் வளங்களை நிரப்புவதற்காக மாநிலத் திரட்டப்பட்ட நிதியை பெருக்குவதற்கான நடவடிக்கைகளை பரிந்துரைக்க நிதி ஆணையத்திற்கு சரத்து 280(3)-ன் எந்த உட்பிரிவு அதிகாரம் அளிக்கிறது?",
        "a": ("Clause (b)", "பிரிவு (b)"),
        "b": ("Clause (bb)", "பிரிவு (bb)"),
        "c": ("Clause (c)", "பிரிவு (c)"),
        "d": ("Clause (d)", "பிரிவு (d)"),
        "exp_en": "Article 280(3)(bb), inserted by the 73rd Constitutional Amendment Act 1992, mandates recommendations for augmenting state funds for Panchayats.",
        "exp_ta": "1992-ன் 73வது அரசியலமைப்பு திருத்தச் சட்டம் மூலம் சேர்க்கப்பட்ட சரத்து 280(3)(bb), பஞ்சாயத்துகளுக்காக மாநில நிதியை பெருக்குவதை கட்டாயமாக்குகிறது.",
        "tip_en": "(bb) is for Panchayats; (c) is for Municipalities.",
        "tip_ta": "(bb) என்பது பஞ்சாயத்துகளுக்கு; (c) என்பது நகராட்சிகளுக்கு.",
        "fact_en": "These measures must be based on recommendations of State Finance Commissions.",
        "fact_ta": "இந்நடவடிக்கைகள் மாநில நிதி ஆணையங்களின் பரிந்துரைகளின் அடிப்படையில் அமைய வேண்டும்."
    },
    # 11: C
    {
        "subtopic": "Municipalities Augmentation (TNPSC Gr 1 2021)",
        "key": "C",
        "en_stem": "Which constitutional provision directs the Finance Commission to recommend measures to augment state funds to supplement the resources of Municipalities?",
        "ta_stem": "நகராட்சிகளின் வளங்களை நிரப்புவதற்காக மாநில நிதியை பெருக்குவதற்கான நடவடிக்கைகளை பரிந்துரைக்க நிதி ஆணையத்திற்கு வழிகாட்டும் அரசியலமைப்பு விதி எது?",
        "a": ("Article 280(3)(a)", "சரத்து 280(3)(a)"),
        "b": ("Article 280(3)(bb)", "சரத்து 280(3)(bb)"),
        "c": ("Article 280(3)(c)", "சரத்து 280(3)(c)"),
        "d": ("Article 280(3)(d)", "சரத்து 280(3)(d)"),
        "exp_en": "Article 280(3)(c), inserted by the 74th Constitutional Amendment Act 1992, requires recommendations to supplement the resources of Municipalities.",
        "exp_ta": "1992-ன் 74வது அரசியலமைப்பு திருத்தச் சட்டத்தால் சேர்க்கப்பட்ட சரத்து 280(3)(c), நகராட்சிகளின் வளங்களை நிரப்ப பரிந்துரைக்கக் கோருகிறது.",
        "tip_en": "Sub-clause (c) was inserted specifically by the 74th Amendment Act.",
        "tip_ta": "உட்பிரிவு (c) பிரத்யேகமாக 74வது திருத்தச் சட்டத்தால் சேர்க்கப்பட்டது.",
        "fact_en": "Eleventh Finance Commission was the first to give full effect to these sub-clauses.",
        "fact_ta": "இப்பிரிவுகளுக்கு முழுமையான செயல்வடிவம் கொடுத்த முதல் ஆணையம் 11வது நிதி ஆணையமாகும்."
    },
    # 12: D
    {
        "subtopic": "Balancing Wheel Concept (TNPSC Gr 1 2013)",
        "key": "D",
        "en_stem": "Which constitutional body is described as the 'balancing wheel of fiscal federalism in India'?",
        "ta_stem": "எந்த அரசியலமைப்பு அமைப்பு 'இந்தியாவில் நிதி கூட்டாட்சியின் சமநிலைப்படுத்தும் சக்கரம்' என்று வர்ணிக்கப்படுகிறது?",
        "a": ("GST Council", "ஜிஎஸ்டி கவுன்சில்"),
        "b": ("Comptroller and Auditor General", "கணக்குத் தணிக்கைத் தலைவர்"),
        "c": ("Inter-State Council", "மாநிலங்களுக்கு இடையேயான கவுன்சில்"),
        "d": ("Finance Commission of India", "இந்திய நிதி ஆணையம்"),
        "exp_en": "The Finance Commission of India is traditionally characterized as the balancing wheel of fiscal federalism because it rectifies vertical and horizontal resource disparities.",
        "exp_ta": "மத்திய-மாநில மற்றும் மாநிலங்களுக்கு இடையிலான வள ஏற்றத்தாழ்வுகளை சீர்செய்வதால் இந்திய நிதி ஆணையம் நிதி கூட்டாட்சியின் சமநிலைப்படுத்தும் சக்கரம் என அழைக்கப்படுகிறது.",
        "tip_en": "Famous quote associated with K.V. Rao's analysis of the Constitution.",
        "tip_ta": "கே.வி. ராவின் அரசியலமைப்பு ஆய்வோடு தொடர்புடைய புகழ்பெற்ற மேற்கோள்.",
        "fact_en": "The Planning Commission previously challenged this balancing role before 2014.",
        "fact_ta": "2014-க்கு முன் திட்டக் குழு இந்த சமநிலைப்படுத்தும் பாத்திரத்திற்கு பெரும் சவாலாக இருந்தது."
    },
    # 13: A
    {
        "subtopic": "Disaster Management Act Year (TNPSC Gr 2 2019)",
        "key": "A",
        "en_stem": "In which year was the Disaster Management Act passed by the Indian Parliament, establishing the NDRF and SDRF?",
        "ta_stem": "NDRF மற்றும் SDRF ஆகியவற்றை நிறுவிய பேரிடர் மேலாண்மைச் சட்டம் இந்திய நாடாளுமன்றத்தால் எந்த ஆண்டில் நிறைவேற்றப்பட்டது?",
        "a": ("2005", "2005"),
        "b": ("2001", "2001"),
        "c": ("2008", "2008"),
        "d": ("2010", "2010"),
        "exp_en": "The Disaster Management Act was enacted in 2005 following the 2004 Indian Ocean Tsunami, providing the statutory basis for disaster funds assessed by Finance Commissions.",
        "exp_ta": "2004 சுனாமி பேரலைக்கு பின்னர் 2005-ல் பேரிடர் மேலாண்மைச் சட்டம் இயற்றப்பட்டது, இது நிதி ஆணையத்தால் மதிப்பிடப்படும் பேரிடர் நிதிகளுக்கு சட்டப்பூர்வ அடித்தளத்தை அமைத்தது.",
        "tip_en": "Enacted in December 2005 (Act No. 53 of 2005).",
        "tip_ta": "டிசம்பர் 2005-ல் இயற்றப்பட்டது (2005-ன் சட்டம் எண் 53).",
        "fact_en": "Section 48 governs State Disaster Response and Mitigation Funds.",
        "fact_ta": "பிரிவு 48 மாநில பேரிடர் மீட்பு மற்றும் தணிப்பு நிதிகளை நிர்வகிக்கிறது."
    },
    # 14: B
    {
        "subtopic": "12th FC Chairman (TNPSC Gr 1 2011)",
        "key": "B",
        "en_stem": "Who was the Chairman of the Twelfth Finance Commission which formulated the Debt Consolidation and Relief Facility (DCRF)?",
        "ta_stem": "கடன் ஒருங்கிணைப்பு மற்றும் நிவாரண வசதியை (DCRF) உருவாக்கிய பன்னிரண்டாவது நிதி ஆணையத்தின் தலைவர் யார்?",
        "a": ("A.M. Khusro", "ஏ.எம். குஸ்ரோ"),
        "b": ("Dr. C. Rangarajan", "டாக்டர் சி. ரங்கராஜன்"),
        "c": ("K.C. Pant", "கே.சி. பந்த்"),
        "d": ("Vijay Kelkar", "விஜய் கேல்கர்"),
        "exp_en": "Dr. C. Rangarajan chaired the Twelfth Finance Commission (2002-2004), which linked central debt relief to the enactment of state-level FRBM Acts.",
        "exp_ta": "டாக்டர் சி. ரங்கராஜன் 12வது நிதி ஆணையத்திற்கு (2002-2004) தலைமை தாங்கினார், இது மத்திய கடன் நிவாரணத்தை மாநில அளவிலான FRBM சட்டங்களை இயற்றுவதோடு இணைத்தது.",
        "tip_en": "Dr. C. Rangarajan was former Governor of RBI and Governor of Andhra Pradesh.",
        "tip_ta": "டாக்டர் சி. ரங்கராஜன் ரிசர்வ் வங்கியின் முன்னாள் ஆளுநர் மற்றும் ஆந்திர மாநில முன்னாள் ஆளுநராவார்.",
        "fact_en": "The DCRF restructured high-interest central loans to 7.5% interest rate.",
        "fact_ta": "DCRF அதிக வட்டி கொண்ட மத்திய கடன்களை 7.5% வட்டி விகிதமாக மாற்றியமைத்தது."
    },
    # 15: C
    {
        "subtopic": "Article 275 Grants (TNPSC Gr 2 2012)",
        "key": "C",
        "en_stem": "Grants-in-aid of the revenues of States in need of assistance are provided by Parliament under which Article?",
        "ta_stem": "உதவி தேவைப்படும் மாநிலங்களின் வருவாய்க்கான மானியங்கள் நாடாளுமன்றத்தால் எந்தச் சரத்தின் கீழ் வழங்கப்படுகின்றன?",
        "a": ("Article 265", "சரத்து 265"),
        "b": ("Article 270", "சரத்து 270"),
        "c": ("Article 275", "சரத்து 275"),
        "d": ("Article 282", "சரத்து 282"),
        "exp_en": "Article 275 provides for statutory grants-in-aid from the Consolidated Fund of India to States declared to be in need of assistance.",
        "exp_ta": "உதவி தேவைப்படும் மாநிலங்களுக்கு இந்தியத் திரட்டப்பட்ட நிதியிலிருந்து சட்டப்பூர்வ மானியங்களை வழங்க சரத்து 275 வகைசெய்கிறது.",
        "tip_en": "Article 275: Statutory grants; Article 282: Discretionary grants.",
        "tip_ta": "சரத்து 275: சட்டப்பூர்வ மானியங்கள்; சரத்து 282: விருப்ப மானியங்கள்.",
        "fact_en": "Grants under Article 275(1) are charged on the Consolidated Fund of India.",
        "fact_ta": "சரத்து 275(1)-ன் கீழான மானியங்கள் இந்தியத் திரட்டப்பட்ட நிதியில் பொறுப்பாக்கப்பட்டுள்ளன."
    },
    # 16: D
    {
        "subtopic": "15th FC Chairman (TNPSC Gr 1 2020)",
        "key": "D",
        "en_stem": "Who was appointed as the Chairman of the Fifteenth Finance Commission of India in November 2017?",
        "ta_stem": "நவம்பர் 2017-ல் இந்தியாவின் பதினைந்தாவது நிதி ஆணையத்தின் தலைவராக நியமிக்கப்பட்டவர் யார்?",
        "a": ("Arvind Subramanian", "அரவிந்த் சுப்பிரமணியன்"),
        "b": ("Urjit Patel", "உர்ஜித் படேல்"),
        "c": ("Raghuram Rajan", "ரகுராம் ராஜன்"),
        "d": ("N.K. Singh", "என்.கே. சிங்"),
        "exp_en": "Nand Kishore Singh (N.K. Singh), former bureaucrat and Member of Parliament, was appointed Chairman of the 15th FC on November 27, 2017.",
        "exp_ta": "முன்னாள் உயர் அதிகாரி மற்றும் நாடாளுமன்ற உறுப்பினரான நந்த் கிஷோர் சிங் (என்.கே. சிங்) நவம்பர் 27, 2017 அன்று 15வது நிதி ஆணையத்தின் தலைவராக நியமிக்கப்பட்டார்.",
        "tip_en": "N.K. Singh also chaired the FRBM Review Committee in 2016-17.",
        "tip_ta": "என்.கே. சிங் 2016-17ல் FRBM மறுஆய்வுக் குழுவிற்கும் தலைமை தாங்கினார்.",
        "fact_en": "The 15th FC submitted its report titled 'Finance Commission in COVID Times'.",
        "fact_ta": "15வது ஆணையம் 'கோவிட் காலத்தில் நிதி ஆணையம்' என்ற தலைப்பில் தனது அறிக்கையை சமர்ப்பித்தது."
    },
    # 17: A
    {
        "subtopic": "15th FC Devolution Percentage (TNPSC Gr 1 2022)",
        "key": "A",
        "en_stem": "What was the vertical tax devolution percentage recommended by the 15th Finance Commission for the period 2021-26?",
        "ta_stem": "2021-26 காலத்திற்கு 15வது நிதி ஆணையத்தால் பரிந்துரைக்கப்பட்ட செங்குத்து வரிப் பகிர்வு சதவீதம் என்ன?",
        "a": ("41%", "41%"),
        "b": ("42%", "42%"),
        "c": ("40%", "40%"),
        "d": ("39%", "39%"),
        "exp_en": "The 15th Finance Commission recommended a vertical devolution of 41% to States, retaining 1% adjustment for Jammu & Kashmir and Ladakh.",
        "exp_ta": "15வது நிதி ஆணையம் மாநிலங்களுக்கு 41% செங்குத்து வரிப் பகிர்வை பரிந்துரைத்தது, ஜம்மு காஷ்மீர் மற்றும் லடாக்கிற்காக 1% சரிசெய்யப்பட்டது.",
        "tip_en": "41% for 28 States; 1% retained by Centre for UTs of J&K and Ladakh.",
        "tip_ta": "28 மாநிலங்களுக்கு 41%; ஜம்மு காஷ்மீர் மற்றும் லடாக் யூனியன் பிரதேசங்களுக்காக மத்திய அரசால் 1% தக்கவைக்கப்பட்டது.",
        "fact_en": "Vertical devolution share under 14th FC was 42%.",
        "fact_ta": "14வது நிதி ஆணையத்தின் கீழ் செங்குத்துப் பகிர்வு 42% ஆக இருந்தது."
    },
    # 18: B
    {
        "subtopic": "16th FC Chairman (Current Affairs PYQ 2024)",
        "key": "B",
        "en_stem": "Who has been appointed as the Chairman of the Sixteenth Finance Commission constituted in December 2023?",
        "ta_stem": "டிசம்பர் 2023-ல் அமைக்கப்பட்ட பதினாறாவது நிதி ஆணையத்தின் தலைவராக நியமிக்கப்பட்டுள்ளவர் யார்?",
        "a": ("Bibek Debroy", "பிபக் தேப்ராய்"),
        "b": ("Dr. Arvind Panagariya", "டாக்டர் அரவிந்த் பனகாரியா"),
        "c": ("Suman Bery", "சுமன் பெரி"),
        "d": ("V. Anantha Nageswaran", "வி. அனந்த நாகேஸ்வரன்"),
        "exp_en": "Dr. Arvind Panagariya, former Vice Chairman of NITI Aayog and Columbia University Professor, was appointed Chairman of the 16th Finance Commission on December 31, 2023.",
        "exp_ta": "நிதி ஆயோக்கின் முன்னாள் துணைத் தலைவரும் கொலம்பியா பல்கலைக்கழக பேராசிரியருமான டாக்டர் அரவிந்த் பனகாரியா டிசம்பர் 31, 2023 அன்று 16வது நிதி ஆணையத்தின் தலைவராக நியமிக்கப்பட்டார்.",
        "tip_en": "16th FC Chairman: Dr. Arvind Panagariya.",
        "tip_ta": "16வது நிதி ஆணையத் தலைவர்: டாக்டர் அரவிந்த் பனகாரியா.",
        "fact_en": "The Commission's recommendations will cover the five-year period starting April 1, 2026.",
        "fact_ta": "இவ்வாணையத்தின் பரிந்துரைகள் ஏப்ரல் 1, 2026 முதல் தொடங்கும் ஐந்து ஆண்டுகளை உள்ளடக்கும்."
    },
    # 19: C
    {
        "subtopic": "Single Divisible Pool Amendment (TNPSC Gr 1 2017)",
        "key": "C",
        "en_stem": "Which Constitutional Amendment Act created a single divisible pool of Central taxes based on the Alternative Scheme of Devolution?",
        "ta_stem": "மாற்று வரிப் பகிர்வுத் திட்டத்தின் அடிப்படையில் மத்திய வரிகளின் ஒற்றைப் பகிர்வு நிதியை உருவாக்கிய அரசியலமைப்புத் திருத்தச் சட்டம் எது?",
        "a": ("73rd Amendment Act", "73வது திருத்தச் சட்டம்"),
        "b": ("74th Amendment Act", "74வது திருத்தச் சட்டம்"),
        "c": ("80th Amendment Act", "80வது திருத்தச் சட்டம்"),
        "d": ("101st Amendment Act", "101வது திருத்தச் சட்டம்"),
        "exp_en": "The 80th Constitutional Amendment Act 2000 amended Article 270 to pool all central taxes (with minor exceptions) into a common divisible pool.",
        "exp_ta": "2000 ஆம் ஆண்டின் 80வது அரசியலமைப்புத் திருத்தச் சட்டம் சரத்து 270-ஐ திருத்தி அனைத்து மத்திய வரிகளையும் பொதுப் பகிர்வு நிதிக்குள் கொண்டுவந்தது.",
        "tip_en": "80th Amendment implemented Tenth FC recommendation retrospectively from 1996.",
        "tip_ta": "80வது திருத்தம் 10வது நிதி ஆணையத்தின் பரிந்துரையை 1996 முதல் முன்தேதியிட்டு செயல்படுத்தியது.",
        "fact_en": "It ended the distinction between income tax and corporation tax sharing.",
        "fact_ta": "இது வருமான வரி மற்றும் நிறுவன வரிப் பகிர்வுக்கு இடையிலான வேறுபாட்டை முடிவுக்குக் கொண்டுவந்தது."
    },
    # 20: D
    {
        "subtopic": "Disaster Financing Ratio (TNPSC Gr 2 2018)",
        "key": "D",
        "en_stem": "What is the Central Government's contribution percentage to the State Disaster Response Fund (SDRF) for General Category States?",
        "ta_stem": "பொதுப் பிரிவு மாநிலங்களுக்கான மாநில பேரிடர் மீட்பு நிதியில் (SDRF) மத்திய அரசின் பங்களிப்பு சதவீதம் என்ன?",
        "a": ("50%", "50%"),
        "b": ("60%", "60%"),
        "c": ("90%", "90%"),
        "d": ("75%", "75%"),
        "exp_en": "For General Category States, the SDRF is contributed 75% by the Central Government and 25% by the State Government.",
        "exp_ta": "பொதுப் பிரிவு மாநிலங்களுக்கு, SDRF நிதியில் 75% மத்திய அரசாலும் 25% மாநில அரசாலும் பங்களிக்கப்படுகிறது.",
        "tip_en": "75:25 for General Category; 90:10 for North-Eastern and Himalayan States.",
        "tip_ta": "பொதுப் பிரிவுக்கு 75:25; வடகிழக்கு மற்றும் இமயமலை மாநிலங்களுக்கு 90:10.",
        "fact_en": "Funds are released in two semi-annual installments.",
        "fact_ta": "ஆண்டுக்கு இருமுறை சம தவணைகளாக இந்த நிதி விடுவிக்கப்படுகிறது."
    },
    # 21: A
    {
        "subtopic": "10th FC Chairman (TNPSC Gr 2 2011)",
        "key": "A",
        "en_stem": "Who was the Chairman of the Tenth Finance Commission that recommended the Alternative Scheme of Devolution?",
        "ta_stem": "மாற்று வரிப் பகிர்வுத் திட்டத்தை பரிந்துரைத்த பத்தாவது நிதி ஆணையத்தின் தலைவர் யார்?",
        "a": ("K.C. Pant", "கே.சி. பந்த்"),
        "b": ("Y.B. Chavan", "ஒய்.பி. சவான்"),
        "c": ("A.M. Khusro", "ஏ.எம். குஸ்ரோ"),
        "d": ("N.K.P. Salve", "என்.கே.பி. சால்வே"),
        "exp_en": "Krishna Chandra Pant (K.C. Pant) chaired the Tenth Finance Commission (1992-1994) which proposed pooling all central taxes.",
        "exp_ta": "கிருஷ்ண சந்திர பந்த் (கே.சி. பந்த்) பத்தாவது நிதி ஆணையத்திற்கு (1992-1994) தலைமை தாங்கினார், இது அனைத்து மத்திய வரிகளையும் ஒன்றிணைக்க பரிந்துரைத்தது.",
        "tip_en": "K.C. Pant was later Deputy Chairman of the Planning Commission.",
        "tip_ta": "கே.சி. பந்த் பின்னர் திட்டக் குழுவின் துணைத் தலைவராகப் பணியாற்றினார்.",
        "fact_en": "The Alternative Scheme suggested giving 29% of gross central taxes to states.",
        "fact_ta": "மாற்றுத் திட்டம் மொத்த மத்திய வரிகளில் 29% மாநிலங்களுக்கு வழங்க பரிந்துரைத்தது."
    },
    # 22: B
    {
        "subtopic": "Civil Court Powers (TNPSC Gr 1 2016)",
        "key": "B",
        "en_stem": "Under the Finance Commission Act 1951, which court's powers are conferred upon the Commission for summoning witnesses and requisitioning documents?",
        "ta_stem": "1951 நிதி ஆணையச் சட்டத்தின் கீழ், சாட்சிகளை அழைக்கவும் ஆவணங்களைக் கோரவும் எந்த நீதிமன்றத்தின் அதிகாரங்கள் ஆணையத்திற்கு வழங்கப்பட்டுள்ளன?",
        "a": ("High Court", "உயர் நீதிமன்றம்"),
        "b": ("Civil Court under the Code of Civil Procedure", "சிவில் நடைமுறைச் சட்டத்தின் கீழான சிவில் நீதிமன்றம்"),
        "c": ("Criminal Sessions Court", "குற்றவியல் அமர்வு நீதிமன்றம்"),
        "d": ("Supreme Court of India", "இந்திய உச்ச நீதிமன்றம்"),
        "exp_en": "Section 8 of the 1951 Act vests the Commission with all powers of a Civil Court under the Code of Civil Procedure 1908.",
        "exp_ta": "1951 சட்டத்தின் பிரிவு 8, 1908 சிவில் நடைமுறைச் சட்டத்தின் கீழ் ஒரு சிவில் நீதிமன்றத்தின் அனைத்து அதிகாரங்களையும் ஆணையத்திற்கு வழங்குகிறது.",
        "tip_en": "Civil court powers: summoning, examining on oath, discovery of public documents.",
        "tip_ta": "சிவில் நீதிமன்ற அதிகாரங்கள்: அழைப்பாணை, உறுதிமொழி விசாரணை, பொது ஆவணங்களை ஆய்வு செய்தல்.",
        "fact_en": "Commission has no criminal trial or sentencing powers.",
        "fact_ta": "ஆணையத்திற்கு குற்றவியல் விசாரணை அல்லது சிறைத்தண்டனை விதிக்கும் அதிகாரம் இல்லை."
    },
    # 23: C
    {
        "subtopic": "11th FC Chairman (TNPSC Gr 1 2009)",
        "key": "C",
        "en_stem": "Who was the Chairman of the Eleventh Finance Commission of India (1998-2000)?",
        "ta_stem": "இந்தியாவின் பதினோராவது நிதி ஆணையத்தின் (1998-2000) தலைவராக இருந்தவர் யார்?",
        "a": ("Dr. Raja Chelliah", "டாக்டர் ராஜா செல்லையா"),
        "b": ("Dr. Bimal Jalan", "டாக்டர் பிமல் ஜலான்"),
        "c": ("Prof. A.M. Khusro", "பேராசிரியர் ஏ.எம். குஸ்ரோ"),
        "d": ("Dr. C. Rangarajan", "டாக்டர் சி. ரங்கராஜன்"),
        "exp_en": "Eminent economist Prof. A.M. Khusro chaired the Eleventh Finance Commission.",
        "exp_ta": "புகழ்பெற்ற பொருளாதார நிபுணர் பேராசிரியர் ஏ.எம். குஸ்ரோ 11வது நிதி ஆணையத்திற்கு தலைமை தாங்கினார்.",
        "tip_en": "Prof. A.M. Khusro was also Editor of Financial Express and President of Indian Economic Association.",
        "tip_ta": "பேராசிரியர் ஏ.எம். குஸ்ரோ பைனான்சியல் எக்ஸ்பிரஸ் பத்திரிகையின் ஆசிரியராகவும் இந்திய பொருளாதார சங்கத்தின் தலைவராகவும் இருந்தார்.",
        "fact_en": "The 11th FC recommended a vertical devolution of 29.5%.",
        "fact_ta": "11வது ஆணையம் 29.5% செங்குத்து வரிப் பகிர்வை பரிந்துரைத்தது."
    },
    # 24: D
    {
        "subtopic": "Qualifications of Members Source (TNPSC Gr 2 2013)",
        "key": "D",
        "en_stem": "Who is constitutionally empowered to determine the qualifications requisite for appointment as members of the Finance Commission?",
        "ta_stem": "நிதி ஆணைய உறுப்பினர்களாக நியமிக்கப்படுவதற்கு தேவையான தகுதிகளை தீர்மானிக்க அரசியலமைப்பு ரீதியாக யாருக்கு அதிகாரம் அளிக்கப்பட்டுள்ளது?",
        "a": ("The President by executive order", "நிர்வாக ஆணை மூலம் குடியரசுத் தலைவர்"),
        "b": ("The Supreme Court of India", "இந்திய உச்ச நீதிமன்றம்"),
        "c": ("The Union Finance Ministry", "மத்திய நிதி அமைச்சகம்"),
        "d": ("Parliament by law", "சட்டத்தின் மூலம் நாடாளுமன்றம்"),
        "exp_en": "Article 280(2) states that Parliament may by law determine the qualifications requisite for appointment as members of the Commission.",
        "exp_ta": "சரத்து 280(2), ஆணையத்தின் உறுப்பினர்களாக நியமிக்கப்பட தேவையான தகுதிகளை நாடாளுமன்றம் சட்டத்தின் மூலம் தீர்மானிக்கலாம் என்று கூறுகிறது.",
        "tip_en": "Parliament determined these qualifications via the Finance Commission Act 1951.",
        "tip_ta": "1951 நிதி ஆணையச் சட்டம் மூலம் நாடாளுமன்றம் இத்தகுதிகளை நிர்ணயித்தது.",
        "fact_en": "The President appoints them, but the qualifications are set by Parliament.",
        "fact_ta": "குடியரசுத் தலைவர் நியமிக்கிறார், ஆனால் தகுதிகளை நாடாளுமன்றமே நிர்ணயிக்கிறது."
    },
    # 25: A
    {
        "subtopic": "Judicial Member Qualification (TNPSC Gr 1 2018)",
        "key": "A",
        "en_stem": "Under the Finance Commission Act 1951, a person qualified to be appointed to which judicial office is eligible as one of the four members?",
        "ta_stem": "1951 நிதி ஆணையச் சட்டத்தின் கீழ், எந்த நீதித்துறை பதவிக்கு நியமிக்கப்பட தகுதியுடைய ஒருவர் நான்கு உறுப்பினர்களில் ஒருவராக நியமிக்கப்பட தகுதியுடையவர்?",
        "a": ("Judge of a High Court", "உயர் நீதிமன்ற நீதிபதி"),
        "b": ("Judge of the Supreme Court", "உச்ச நீதிமன்ற நீதிபதி"),
        "c": ("District and Sessions Judge", "மாவட்ட மற்றும் அமர்வு நீதிபதி"),
        "d": ("Advocate General of a State", "மாநில அட்வகேட் ஜெனரல்"),
        "exp_en": "Section 4(a) of the 1951 Act states that one member must be qualified to be appointed as a Judge of a High Court.",
        "exp_ta": "1951 சட்டத்தின் பிரிவு 4(a), ஒரு உறுப்பினர் உயர் நீதிமன்ற நீதிபதியாக நியமிக்கப்பட தகுதியுடையவராக இருக்க வேண்டும் என்று கூறுகிறது.",
        "tip_en": "High Court qualification is specified, not Supreme Court.",
        "tip_ta": "உயர் நீதிமன்றத் தகுதியே குறிப்பிடப்பட்டுள்ளது, உச்ச நீதிமன்றம் அல்ல.",
        "fact_en": "This ensures legal and quasi-judicial competence in interpreting fiscal statutes.",
        "fact_ta": "இது நிதிச் சட்டங்களை விளக்குவதில் சட்டப்பூர்வ மற்றும் அரை-நீதித்துறை திறனை உறுதி செய்கிறது."
    },
    # 26: B
    {
        "subtopic": "2nd FC Chairman (TNPSC Gr 2 2014)",
        "key": "B",
        "en_stem": "Who was the Chairman of the Second Finance Commission constituted in 1956?",
        "ta_stem": "1956 ஆம் ஆண்டு அமைக்கப்பட்ட இரண்டாவது நிதி ஆணையத்தின் தலைவர் யார்?",
        "a": ("A.K. Chanda", "ஏ.கே. சந்தா"),
        "b": ("K. Santhanam", "கே. சந்தானம்"),
        "c": ("P.V. Rajamannar", "பி.வி. ராஜமன்னார்"),
        "d": ("K.C. Neogy", "கே.சி. நியோகி"),
        "exp_en": "Kasturiranga Santhanam (K. Santhanam) chaired the Second Finance Commission (1956-1957).",
        "exp_ta": "கஸ்தூரிரங்க சந்தானம் (கே. சந்தானம்) இரண்டாவது நிதி ஆணையத்திற்கு (1956-1957) தலைமை தாங்கினார்.",
        "tip_en": "K. Santhanam was from Tamil Nadu and also chaired the Committee on Prevention of Corruption.",
        "tip_ta": "கே. சந்தானம் தமிழ்நாட்டைச் சேர்ந்தவர், ஊழல் தடுப்புக் குழுவிற்கும் (சந்தானம் குழு) தலைமை தாங்கினார்.",
        "fact_en": "The 2nd FC raised state income tax share from 55% to 60%.",
        "fact_ta": "2வது ஆணையம் மாநில வருமான வரிப் பங்கை 55%-லிருந்து 60% ஆக உயர்த்தியது."
    },
    # 27: C
    {
        "subtopic": "4th FC Chairman (TNPSC Gr 1 2012)",
        "key": "C",
        "en_stem": "Which eminent jurist from Tamil Nadu chaired the Fourth Finance Commission constituted in 1964?",
        "ta_stem": "1964-ல் அமைக்கப்பட்ட நான்காவது நிதி ஆணையத்திற்கு தலைமை தாங்கிய தமிழ்நாட்டைச் சேர்ந்த புகழ்பெற்ற சட்ட நிபுணர் யார்?",
        "a": ("M. Patanjali Sastri", "எம். பதஞ்சலி சாஸ்திரி"),
        "b": ("K. Subba Rao", "கே. சுப்பா ராவ்"),
        "c": ("Dr. P.V. Rajamannar", "டாக்டர் பி.வி. ராஜமன்னார்"),
        "d": ("V.R. Krishna Iyer", "வி.ஆர். கிருஷ்ண ஐயர்"),
        "exp_en": "Dr. P.V. Rajamannar, former Chief Justice of the Madras High Court, chaired the Fourth Finance Commission.",
        "exp_ta": "சென்னை உயர் நீதிமன்றத்தின் முன்னாள் தலைமை நீதிபதி டாக்டர் பி.வி. ராஜமன்னார் 4வது நிதி ஆணையத்திற்கு தலைமை தாங்கினார்.",
        "tip_en": "Dr. P.V. Rajamannar also headed the famous Rajamannar Committee on Centre-State Relations in 1969.",
        "tip_ta": "டாக்டர் பி.வி. ராஜமன்னார் 1969-ல் மத்திய-மாநில உறவுகள் குறித்த புகழ்பெற்ற ராஜமன்னார் குழுவிற்கும் தலைமை தாங்கினார்.",
        "fact_en": "The 4th FC recommended raising state income tax share to 75%.",
        "fact_ta": "4வது ஆணையம் மாநில வருமான வரிப் பங்கை 75% ஆக உயர்த்த பரிந்துரைத்தது."
    },
    # 28: D
    {
        "subtopic": "13th FC Chairman (TNPSC Gr 1 2011)",
        "key": "D",
        "en_stem": "Who was the Chairman of the Thirteenth Finance Commission that provided the roadmap for GST rollout?",
        "ta_stem": "ஜிஎஸ்டி அமலாக்கத்திற்கான வரைபடத்தை வழங்கிய பதின்மூன்றாவது நிதி ஆணையத்தின் தலைவர் யார்?",
        "a": ("Montek Singh Ahluwalia", "மாண்டேக் சிங் அலுவாலியா"),
        "b": ("C. Rangarajan", "சி. ரங்கராஜன்"),
        "c": ("Bimal Jalan", "பிமல் ஜலான்"),
        "d": ("Dr. Vijay Kelkar", "டாக்டர் விஜய் கேல்கர்"),
        "exp_en": "Dr. Vijay Kelkar chaired the Thirteenth Finance Commission (2007-2009), famous for proposing a grand bargain for GST.",
        "exp_ta": "டாக்டர் விஜய் கேல்கர் 13வது நிதி ஆணையத்திற்கு (2007-2009) தலைமை தாங்கினார், ஜிஎஸ்டிக்கான ஒப்பந்தத்தை முன்மொழிந்ததில் இவர் புகழ்பெற்றவர்.",
        "tip_en": "Dr. Kelkar recommended 32% vertical devolution.",
        "tip_ta": "டாக்டர் கேல்கர் 32% செங்குத்து வரிப் பகிர்வை பரிந்துரைத்தார்.",
        "fact_en": "Kelkar introduced environmental incentive grants for forest maintenance.",
        "fact_ta": "கேல்கர் வனப் பராமரிப்பிற்கான சுற்றுச்சூழல் ஊக்க மானியங்களை அறிமுகப்படுத்தினார்."
    },
    # 29: A
    {
        "subtopic": "Net Proceeds Certification (TNPSC Gr 1 2019)",
        "key": "A",
        "en_stem": "Under Article 279 of the Constitution, whose certificate regarding the net proceeds of any tax or duty is final and binding?",
        "ta_stem": "அரசியலமைப்பின் சரத்து 279-ன் கீழ், எந்தவொரு வரி அல்லது கட்டணத்தின் நிகர வருவாய் குறித்த யாருடைய சான்றிதழ் இறுதியானது மற்றும் கட்டுப்படுத்துவது?",
        "a": ("Comptroller and Auditor General of India", "இந்தியக் கணக்குத் தணிக்கைத் தலைவர் (CAG)"),
        "b": ("Governor of the Reserve Bank of India", "இந்திய ரிசர்வ் வங்கி ஆளுநர்"),
        "c": ("Chairman of the Finance Commission", "நிதி ஆணையத்தின் தலைவர்"),
        "d": ("Union Finance Secretary", "மத்திய நிதிச் செயலாளர்"),
        "exp_en": "Article 279(2) explicitly provides that the net proceeds of any tax or duty shall be ascertained and certified by the CAG, whose certificate shall be final.",
        "exp_ta": "சரத்து 279(2), வரிகளின் நிகர வருவாய் சி.ஏ.ஜியால் கண்டறியப்பட்டு சான்றளிக்கப்பட வேண்டும் என்றும், அவரது சான்றிதழே இறுதியானது என்றும் தெளிவாகக் கூறுகிறது.",
        "tip_en": "Article 279: CAG certificate on net proceeds is final.",
        "tip_ta": "சரத்து 279: நிகர வருவாய் குறித்த சி.ஏ.ஜி சான்றிதழ் இறுதியானது.",
        "fact_en": "Net proceeds = Gross tax collection minus costs of collection.",
        "fact_ta": "நிகர வருவாய் = மொத்த வரி வசூல் கழித்தல் வசூல் செலவுகள்."
    },
    # 30: B
    {
        "subtopic": "Quorum of Commission (TNPSC Gr 2 2017)",
        "key": "B",
        "en_stem": "What is the statutory quorum required to hold a formal meeting of the Finance Commission under the 1951 rules?",
        "ta_stem": "1951 விதிகளின் கீழ் நிதி ஆணையத்தின் முறையான கூட்டத்தை நடத்துவதற்கு தேவையான சட்டப்பூர்வ குறைந்தபட்ச வருகை (Quorum) என்ன?",
        "a": ("2 members", "2 உறுப்பினர்கள்"),
        "b": ("3 members including the presiding Chairman/Member", "தலைவர்/உறுப்பினர் உட்பட 3 உறுப்பினர்கள்"),
        "c": ("All 5 members unanimously", "அனைத்து 5 உறுப்பினர்களும் ஒருமனதாக"),
        "d": ("4 members", "4 உறுப்பினர்கள்"),
        "exp_en": "Under the Finance Commission rules framed under the 1951 Act, three members constitute the quorum for meetings of the Commission.",
        "exp_ta": "1951 சட்டத்தின் கீழ் உருவாக்கப்பட்ட நிதி ஆணைய விதிகளின்படி, மூன்று உறுப்பினர்கள் கூட்டத்திற்கான குறைந்தபட்ச வருகையை (Quorum) அமைக்கின்றனர்.",
        "tip_en": "Quorum of 3 ensures decisions can be taken even if a member is indisposed.",
        "tip_ta": "3 என்ற குறைந்தபட்ச வருகை, ஓர் உறுப்பினர் விடுப்பில் இருந்தாலும் முடிவெடுப்பதை உறுதி செய்கிறது.",
        "fact_en": "Dissenting members may record a formal Note of Dissent.",
        "fact_ta": "மாறுபட்ட கருத்துடைய உறுப்பினர்கள் முறையான மாற்றுக் குறிப்பை (Note of Dissent) பதிவு செய்யலாம்."
    },
    # 31: C
    {
        "subtopic": "Cesses Exclusion Article (TNPSC Gr 1 2021)",
        "key": "C",
        "en_stem": "Which Article of the Constitution empowers the Union Parliament to levy surcharges on taxes exclusively for Union purposes, excluding them from the divisible pool?",
        "ta_stem": "வரிகள் மீது மத்திய தேவைகளுக்காக மட்டுமே கூடுதல் வரிகளை (Surcharges) விதித்து, அவற்றை பகிர்வு நிதியிலிருந்து விலக்க நாடாளுமன்றத்திற்கு அதிகாரம் அளிக்கும் அரசியலமைப்புச் சரத்து எது?",
        "a": ("Article 269", "சரத்து 269"),
        "b": ("Article 270", "சரத்து 270"),
        "c": ("Article 271", "சரத்து 271"),
        "d": ("Article 275", "சரத்து 275"),
        "exp_en": "Article 271 permits Parliament to impose surcharges on taxes referred to in Articles 269 and 270 entirely for Union purposes.",
        "exp_ta": "சரத்து 271, மத்திய தேவைகளுக்காக மட்டுமே கூடுதல் வரிகளை விதித்து அவற்றை முழுமையாக மத்திய அரசே வைத்துக்கொள்ள நாடாளுமன்றத்திற்கு அனுமதி அளிக்கிறது.",
        "tip_en": "Article 271 is a major point of fiscal debate between Centre and States.",
        "tip_ta": "சரத்து 271 மத்திய-மாநில அரசுகளுக்கு இடையிலான ஒரு முக்கிய நிதி விவாதப் புள்ளியாகும்.",
        "fact_en": "GST excluded Article 271 surcharges on GST goods and services.",
        "fact_ta": "ஜிஎஸ்டி சரக்கு மற்றும் சேவைகள் மீதான சரத்து 271 கூடுதல் வரிகளை விலக்கியது."
    },
    # 32: D
    {
        "subtopic": "Demographic Performance Weight (TNPSC Gr 1 2022)",
        "key": "D",
        "en_stem": "What percentage weight was assigned to 'Demographic Performance' by the 15th Finance Commission?",
        "ta_stem": "15வது நிதி ஆணையத்தால் 'மக்கள்தொகை செயல்திறனுக்கு' எத்தனை சதவீத எடை ஒதுக்கப்பட்டது?",
        "a": ("5.0%", "5.0%"),
        "b": ("7.5%", "7.5%"),
        "c": ("10.0%", "10.0%"),
        "d": ("12.5%", "12.5%"),
        "exp_en": "The 15th Finance Commission allocated 12.5% weight to Demographic Performance to reward states that lowered fertility rates.",
        "exp_ta": "பிறப்பு விகிதத்தைக் குறைத்த மாநிலங்களை ஊக்குவிப்பதற்காக 15வது நிதி ஆணையம் மக்கள்தொகை செயல்திறனுக்கு 12.5% எடையை ஒதுக்கியது.",
        "tip_en": "Demographic Performance (12.5%) compensated states penalized by 2011 population data.",
        "tip_ta": "மக்கள்தொகை செயல்திறன் (12.5%) 2011 கணக்கெடுப்பால் பாதிக்கப்பட்ட மாநிலங்களுக்கு ஈடுசெய்தது.",
        "fact_en": "It was calculated using the inverse of the Total Fertility Rate (TFR).",
        "fact_ta": "இது மொத்த கருவுறுதல் விகிதத்தின் (TFR) தலைகீழ் மதிப்பைப் பயன்படுத்தி கணக்கிடப்பட்டது."
    },
    # 33: A
    {
        "subtopic": "Income Distance Definition (TNPSC Gr 1 2015)",
        "key": "A",
        "en_stem": "In Finance Commission devolution formulas, how is 'Income Distance' calculated?",
        "ta_stem": "நிதி ஆணையப் பகிர்வு சூத்திரங்களில், 'வருமான இடைவெளி' எவ்வாறு கணக்கிடப்படுகிறது?",
        "a": ("Distance of a State's per capita GSDP from the state with the highest per capita GSDP", "மிக அதிக தனிநபர் வருமானம் கொண்ட மாநிலத்திலிருந்து ஒரு மாநிலத்தின் தனிநபர் GSDP உள்ள தூரம்"),
        "b": ("Difference between state tax revenue and central excise collection", "மாநில வரி வருவாய்க்கும் மத்திய கலால் வரி வசூலுக்கும் இடையிலான வேறுபாடு"),
        "c": ("Ratio of urban income to rural per capita income within the State", "மாநிலத்திற்குள் நகர்ப்புற வருவாய்க்கும் ஊரக தனிநபர் வருவாய்க்கும் உள்ள விகிதம்"),
        "d": ("Percentage gap between state budget deficit and central fiscal deficit", "மாநில பட்ஜெட் பற்றாக்குறைக்கும் மத்திய நிதிப் பற்றாக்குறைக்கும் உள்ள சதவீத இடைவெளி"),
        "exp_en": "Income distance is measured as the distance of a State's per capita income (GSDP) from the benchmark state having the highest per capita income.",
        "exp_ta": "வருமான இடைவெளி என்பது மிக உயர்ந்த தனிநபர் வருமானம் கொண்ட மாநிலத்தின் மதிப்பிலிருந்து ஒரு மாநிலத்தின் தனிநபர் வருமானம் (GSDP) எவ்வளவு குறைவாக உள்ளது என அளவிடப்படுகிறது.",
        "tip_en": "Goa/Haryana/Punjab typically served as the benchmark top income states.",
        "tip_ta": "பொதுவாக கோவா அல்லது ஹரியானா போன்ற மாநிலங்கள் உச்ச வரம்பாகக் கொள்ளப்படுகின்றன.",
        "fact_en": "Income distance is the most progressive redistributive element in the devolution formula.",
        "fact_ta": "வருமான இடைவெளி என்பது பகிர்வு சூத்திரத்தில் மிகவும் முற்போக்கான மறுபகிர்வு காரணியாகும்."
    },
    # 34: B
    {
        "subtopic": "Local Body Grants Scale (TNPSC Gr 2 2022)",
        "key": "B",
        "en_stem": "Approximately what total amount was recommended by the 15th Finance Commission as grants to local governments for 2021-26?",
        "ta_stem": "2021-26 காலத்திற்கு உள்ளாட்சி அமைப்புகளுக்கான மானியங்களாக 15வது நிதி ஆணையத்தால் தோராயமாக பரிந்துரைக்கப்பட்ட மொத்தத் தொகை எவ்வளவு?",
        "a": ("Rs. 2.87 lakh crore", "ரூ. 2.87 லட்சம் கோடி"),
        "b": ("Rs. 4.36 lakh crore", "ரூ. 4.36 லட்சம் கோடி"),
        "c": ("Rs. 5.50 lakh crore", "ரூ. 5.50 லட்சம் கோடி"),
        "d": ("Rs. 1.80 lakh crore", "ரூ. 1.80 லட்சம் கோடி"),
        "exp_en": "The 15th FC recommended a total grant of Rs. 4,36,361 crore (approx Rs. 4.36 lakh crore) to local governments (Panchayats and Municipalities).",
        "exp_ta": "15வது நிதி ஆணையம் உள்ளாட்சி அமைப்புகளுக்கு (பஞ்சாயத்துகள் மற்றும் நகராட்சிகள்) மொத்தம் ரூ. 4,36,361 கோடி (தோராயமாக ரூ. 4.36 லட்சம் கோடி) மானியங்களை பரிந்துரைத்தது.",
        "tip_en": "Rs. 4.36 lakh crore: Rs. 2.36 lakh crore for PRIs + Rs. 1.21 lakh crore for ULBs + Rs. 70,051 cr health.",
        "tip_ta": "ரூ. 4.36 லட்சம் கோடி: பஞ்சாயத்துகளுக்கு ரூ. 2.36 லட்சம் கோடி + நகராட்சிகளுக்கு ரூ. 1.21 லட்சம் கோடி + சுகாதாரம் ரூ. 70,051 கோடி.",
        "fact_en": "14th FC had allocated Rs. 2.87 lakh crore for local bodies.",
        "fact_ta": "14வது நிதி ஆணையம் உள்ளாட்சிகளுக்கு ரூ. 2.87 லட்சம் கோடியை ஒதுக்கியிருந்தது."
    },
    # 35: C
    {
        "subtopic": "Constituent Assembly Drafting (TNPSC Gr 1 2011)",
        "key": "C",
        "en_stem": "Who chaired the Expert Committee on the Financial Provisions of the Union Constitution (1947) during the drafting of the Indian Constitution?",
        "ta_stem": "இந்திய அரசியலமைப்பு வரைவின் போது மத்திய அரசியலமைப்பின் நிதி விதிகள் குறித்த நிபுணர் குழுவிற்கு (1947) தலைமை தாங்கியவர் யார்?",
        "a": ("B.R. Ambedkar", "பி.ஆர். அம்பேத்கர்"),
        "b": ("Alladi Krishnaswamy Iyer", "அல்லாடி கிருஷ்ணசுவாமி ஐயர்"),
        "c": ("Nalini Ranjan Sarkar", "நளினி ரஞ்சன் சர்க்கார்"),
        "d": ("K.M. Munshi", "கே.எம். முன்ஷி"),
        "exp_en": "The Expert Committee on Financial Provisions appointed by the Constituent Assembly was chaired by Nalini Ranjan Sarkar (Sarkar Committee).",
        "exp_ta": "அரசியலமைப்பு நிர்ணய சபையால் நியமிக்கப்பட்ட நிதி விதிகள் குறித்த நிபுணர் குழுவிற்கு நளினி ரஞ்சன் சர்க்கார் (சர்க்கார் குழு) தலைமை தாங்கினார்.",
        "tip_en": "Nalini Ranjan Sarkar Committee recommended creating a Finance Commission.",
        "tip_ta": "நளினி ரஞ்சன் சர்க்கார் குழுவே நிதி ஆணையத்தை உருவாக்க பரிந்துரைத்தது.",
        "fact_en": "The Sarkar Committee report directly shaped Articles 270, 275, and 280.",
        "fact_ta": "சர்க்கார் குழுவின் அறிக்கை சரத்துகள் 270, 275 மற்றும் 280-ஐ நேரடியாக வடிவமைத்தது."
    },
    # 36: D
    {
        "subtopic": "Disqualification Ground (TNPSC Gr 2 2015)",
        "key": "D",
        "en_stem": "Under Section 5 of the Finance Commission Act 1951, which of the following is NOT a statutory ground for disqualification of a member?",
        "ta_stem": "1951 நிதி ஆணையச் சட்டத்தின் பிரிவு 5-ன் கீழ், பின்வருவனவற்றில் எது ஓர் உறுப்பினரின் சட்டப்பூர்வ தகுதியிழப்புக்கான காரணம் அல்ல?",
        "a": ("Being adjudged of unsound mind by a competent court", "திறமையான நீதிமன்றத்தால் மனநலம் குன்றியவர் என அறிவிக்கப்படுதல்"),
        "b": ("Being an un-discharged insolvent", "திவால் நிலை நீங்காதவராக இருத்தல்"),
        "c": ("Being convicted of an offence involving moral turpitude", "ஒழுக்கக்கேடான குற்றம் ஒன்றிற்காக தண்டிக்கப்பட்டிருத்தல்"),
        "d": ("Holding an academic degree from a foreign university", "வெளிநாட்டுப் பல்கலைக்கழகத்தில் கல்விப் பட்டம் பெற்றிருத்தல்"),
        "exp_en": "Holding a foreign university degree is not a disqualification; the statutory grounds are unsound mind, undischarged insolvency, moral turpitude conviction, or conflicting financial interests.",
        "exp_ta": "வெளிநாட்டுப் பல்கலைக்கழகப் பட்டம் பெற்றிருப்பது தகுதியிழப்பு அல்ல; மனநலமின்மை, திவால் நிலை, ஒழுக்கக்கேடான தண்டனை மற்றும் சார்புடைய நிதி ஆர்வமே சட்டப்பூர்வ தகுதியிழப்புகளாகும்.",
        "tip_en": "Academic qualifications are celebrated assets, never disqualifications.",
        "tip_ta": "கல்வித் தகுதிகள் வரவேற்கத்தக்க சொத்துக்கள், ஒருபோதும் தகுதியிழப்புகள் அல்ல.",
        "fact_en": "Section 5 mirrors standard constitutional integrity criteria.",
        "fact_ta": "பிரிவு 5 வழக்கமான அரசியலமைப்பு நேர்மை அளவுகோல்களை பிரதிபலிக்கிறது."
    },
    # 37: A
    {
        "subtopic": "Special Category Disaster Matching (TNPSC Gr 1 2017)",
        "key": "A",
        "en_stem": "What is the Central Government share in the SDRF for North-Eastern and Himalayan States as approved under Finance Commission norms?",
        "ta_stem": "நிதி ஆணைய விதிகளின் கீழ் அங்கீகரிக்கப்பட்டபடி வடகிழக்கு மற்றும் இமயமலை மாநிலங்களுக்கான SDRF நிதியில் மத்திய அரசின் பங்கு என்ன?",
        "a": ("90%", "90%"),
        "b": ("75%", "75%"),
        "c": ("80%", "80%"),
        "d": ("100%", "100%"),
        "exp_en": "Under Finance Commission recommendations, North-Eastern and Himalayan States receive 90% of their SDRF allocation from the Central Government.",
        "exp_ta": "நிதி ஆணையப் பரிந்துரைகளின் கீழ், வடகிழக்கு மற்றும் இமயமலை மாநிலங்கள் தங்களது SDRF ஒதுக்கீட்டில் 90%-ஐ மத்திய அரசிடமிருந்து பெறுகின்றன.",
        "tip_en": "90:10 ratio applies to Assam, HP, Uttarakhand, J&K, and NE states.",
        "tip_ta": "90:10 விகிதம் அசாம், இமாச்சலப் பிரதேசம், உத்தராகண்ட், மற்றும் வடகிழக்கு மாநிலங்களுக்கு பொருந்தும்.",
        "fact_en": "General category states contribute 25% from their state budgets.",
        "fact_ta": "பொதுப் பிரிவு மாநிலங்கள் தங்களது மாநில பட்ஜெட்டிலிருந்து 25% பங்களிக்கின்றன."
    },
    # 38: B
    {
        "subtopic": "Tenure Flexibility (TNPSC Gr 2 2016)",
        "key": "B",
        "en_stem": "Can the President constitute a Finance Commission earlier than the expiration of five years as per Article 280(1)?",
        "ta_stem": "சரத்து 280(1)-ன் படி ஐந்து ஆண்டுகள் முடிவதற்கு முன்னரே குடியரசுத் தலைவரால் நிதி ஆணையத்தை அமைக்க முடியுமா?",
        "a": ("No, exactly five full years must elapse between commissions", "இல்லை, ஆணையங்களுக்கு இடையே சரியாக ஐந்து முழு ஆண்டுகள் முடிய வேண்டும்"),
        "b": ("Yes, at such earlier time as the President considers necessary", "ஆம், குடியரசுத் தலைவர் அவசியமெனக் கருதும் முந்தைய நேரத்திலும் அமைக்கலாம்"),
        "c": ("Only if the Lok Sabha is dissolved prematurely", "மக்களவை முன்கூட்டியே கலைக்கப்பட்டால் மட்டுமே முடியும்"),
        "d": ("Only upon a joint resolution passed by two-thirds of State Assemblies", "மூன்றில் இரண்டு பங்கு மாநில சட்டமன்றங்கள் கூட்டுத் தீர்மானம் நிறைவேற்றினால் மட்டுமே"),
        "exp_en": "Article 280(1) states the President shall constitute the Commission 'at the expiration of every fifth year or at such earlier time as the President considers necessary'.",
        "exp_ta": "சரத்து 280(1), 'ஒவ்வொரு ஐந்தாவது ஆண்டின் முடிவிலும் அல்லது குடியரசுத் தலைவர் அவசியமெனக் கருதும் முந்தைய நேரத்திலும்' ஆணையத்தை அமைக்கலாம் என்று தெளிவாகக் கூறுகிறது.",
        "tip_en": "Key phrase: 'or at such earlier time as the President considers necessary'.",
        "tip_ta": "முக்கிய வாசகம்: 'அல்லது குடியரசுத் தலைவர் அவசியமெனக் கருதும் முந்தைய நேரத்திலும்'.",
        "fact_en": "Commissions are frequently constituted 2-3 years prior to the expiration of the ongoing award.",
        "fact_ta": "நடப்பு பரிந்துரைக் காலம் முடிவதற்கு 2-3 ஆண்டுகளுக்கு முன்னரே புதிய ஆணையங்கள் அமைக்கப்படுவது வழக்கம்."
    },
    # 39: C
    {
        "subtopic": "Reappointment Eligibility (TNPSC Gr 4 2014)",
        "key": "C",
        "en_stem": "Are the Chairman and members of the Finance Commission of India eligible for reappointment under the Finance Commission Act 1951?",
        "ta_stem": "1951 நிதி ஆணையச் சட்டத்தின் கீழ் இந்திய நிதி ஆணையத்தின் தலைவர் மற்றும் உறுப்பினர்கள் மீண்டும் நியமிக்கப்பட தகுதியுடையவர்களா?",
        "a": ("No, there is an absolute constitutional bar on reappointment", "இல்லை, மீண்டும் நியமிக்கப்படுவதற்கு முழுமையான அரசியலமைப்புத் தடை உள்ளது"),
        "b": ("Only the Chairman is eligible for reappointment", "தலைவர் மட்டுமே மீண்டும் நியமிக்கப்பட தகுதியுடையவர்"),
        "c": ("Yes, every member is eligible for reappointment unless disqualified", "ஆம், தகுதியிழப்பு இல்லாத வரை ஒவ்வொரு உறுப்பினரும் மீண்டும் நியமிக்கப்பட தகுதியுடையவர்"),
        "d": ("Only after a mandatory 5-year cooling-off period", "ஐந்து வருட கட்டாய இடைவெளிக்குப் பிறகு மட்டுமே தகுதியுடையவர்"),
        "exp_en": "Under Section 6 of the Finance Commission Act 1951, every member of the Commission shall be eligible for reappointment.",
        "exp_ta": "1951 நிதி ஆணையச் சட்டத்தின் பிரிவு 6-ன் கீழ், ஆணையத்தின் ஒவ்வொரு உறுப்பினரும் மீண்டும் நியமிக்கப்பட தகுதியுடையவராவார்.",
        "tip_en": "Unlike CAG or UPSC members, FC members CAN be reappointed.",
        "tip_ta": "சி.ஏ.ஜி அல்லது யு.பி.எஸ்.சி உறுப்பினர்களைப் போலன்றி, நிதி ஆணைய உறுப்பினர்கள் மீண்டும் நியமிக்கப்படலாம்.",
        "fact_en": "Several distinguished economists have served across multiple Finance Commissions.",
        "fact_ta": "பல புகழ்பெற்ற பொருளாதார வல்லுநர்கள் ஒன்றுக்கும் மேற்பட்ட நிதி ஆணையங்களில் பணியாற்றியுள்ளனர்."
    },
    # 40: D
    {
        "subtopic": "Post-Devolution Revenue Deficit Grants (TNPSC Gr 1 2020)",
        "key": "D",
        "en_stem": "Under which constitutional article are Post-Devolution Revenue Deficit (PDRD) grants recommended to bridge assessed gaps in state revenues?",
        "ta_stem": "மாநில வருவாய்களில் கணிக்கப்பட்ட நிதி இடைவெளிகளை நிரப்ப எந்த அரசியலமைப்புச் சரத்தின் கீழ் பகிர்வுக்குப் பிந்தைய வருவாய்ப் பற்றாக்குறை (PDRD) மானியங்கள் பரிந்துரைக்கப்படுகின்றன?",
        "a": ("Article 268", "சரத்து 268"),
        "b": ("Article 270", "சரத்து 270"),
        "c": ("Article 282", "சரத்து 282"),
        "d": ("Article 275", "சரத்து 275"),
        "exp_en": "Post-Devolution Revenue Deficit grants are recommended under Article 275 of the Constitution to assist States that face revenue deficits even after tax devolution.",
        "exp_ta": "வரிப் பகிர்வுக்குப் பின்னரும் வருவாய்ப் பற்றாக்குறையைச் சந்திக்கும் மாநிலங்களுக்கு உதவ அரசியலமைப்பின் சரத்து 275-ன் கீழ் PDRD மானியங்கள் பரிந்துரைக்கப்படுகின்றன.",
        "tip_en": "PDRD grants act as the final fiscal safety net for deficit states.",
        "tip_ta": "PDRD மானியங்கள் பற்றாக்குறை மாநிலங்களுக்கான இறுதி நிதிப் பாதுகாப்பு வலையாக செயல்படுகின்றன.",
        "fact_en": "15th FC recommended Rs. 2.94 lakh crore as PDRD grants to 17 States.",
        "fact_ta": "15வது ஆணையம் 17 மாநிலங்களுக்கு PDRD மானியங்களாக ரூ. 2.94 லட்சம் கோடியை பரிந்துரைத்தது."
    },
    # 41: A
    {
        "subtopic": "Forest and Ecology Weight (TNPSC Gr 1 2021)",
        "key": "A",
        "en_stem": "What percentage weight did the 15th Finance Commission assign to 'Forest and Ecology' in its horizontal tax devolution formula?",
        "ta_stem": "15வது நிதி ஆணையம் தனது கிடைமட்ட வரிப் பகிர்வு சூத்திரத்தில் 'வனம் மற்றும் சூழலியலுக்கு' எத்தனை சதவீத எடையை ஒதுக்கியது?",
        "a": ("10.0%", "10.0%"),
        "b": ("7.5%", "7.5%"),
        "c": ("15.0%", "15.0%"),
        "d": ("12.5%", "12.5%"),
        "exp_en": "The 15th FC assigned 10.0% weight to Forest and Ecology, calculated based on very dense and moderately dense forest cover.",
        "exp_ta": "15வது நிதி ஆணையம் அடர்ந்த மற்றும் மிதமான வனப் பரப்பின் அடிப்படையில் வனம் மற்றும் சூழலியலுக்கு 10.0% எடையை ஒதுக்கியது.",
        "tip_en": "Increased from 7.5% in 14th FC to 10.0% in 15th FC.",
        "tip_ta": "14வது ஆணையத்தில் 7.5% ஆக இருந்தது 15வது ஆணையத்தில் 10.0% ஆக உயர்த்தப்பட்டது.",
        "fact_en": "It compensates states for the opportunity cost of not diverting forest land for economic development.",
        "fact_ta": "பொருளாதார வளர்ச்சிக்காக வன நிலங்களை அழிக்காமல் பாதுகாப்பதால் மாநிலங்களுக்கு ஏற்படும் இழப்பை இது ஈடுசெய்கிறது."
    },
    # 42: B
    {
        "subtopic": "Secretariat Head (TNPSC Gr 2 2018)",
        "key": "B",
        "en_stem": "Who heads the permanent administrative secretariat that supports the Finance Commission during its tenure?",
        "ta_stem": "நிதி ஆணையத்தின் செயல்பாட்டுக் காலத்தில் அதற்கு உதவும் நிர்வாகச் செயலகத்திற்கு தலைமை தாங்குபவர் யார்?",
        "a": ("Cabinet Secretary", "மத்திய அமைச்சரவைச் செயலாளர்"),
        "b": ("Secretary to the Finance Commission (Senior IAS Officer)", "நிதி ஆணையத்தின் செயலாளர் (மூத்த ஐ.ஏ.எஸ் அதிகாரி)"),
        "c": ("Union Finance Secretary", "மத்திய நிதிச் செயலாளர்"),
        "d": ("Chief Economic Adviser", "தலைமைப் பொருளாதார ஆலோசகர்"),
        "exp_en": "The Secretariat of the Finance Commission is headed by a Secretary to the Commission, usually a senior civil servant of Additional Secretary or Secretary rank.",
        "exp_ta": "நிதி ஆணையச் செயலகத்திற்கு கூடுதல் செயலாளர் அல்லது செயலாளர் அந்தஸ்தில் உள்ள ஒரு மூத்த ஐ.ஏ.எஸ் அதிகாரி (ஆணையத்தின் செயலாளர்) தலைமை தாங்குகிறார்.",
        "tip_en": "Ritvik Ranjanam Pandey serves as Secretary to the 16th Finance Commission.",
        "tip_ta": "ரித்விக் ரஞ்சனம் பாண்டே 16வது நிதி ஆணையத்தின் செயலாளராகப் பணியாற்றுகிறார்.",
        "fact_en": "The Secretariat coordinates data collection across all 28 States and Central Ministries.",
        "fact_ta": "இச்செயலகம் அனைத்து 28 மாநிலங்கள் மற்றும் மத்திய அமைச்சகங்களிடமிருந்து தரவுகளைத் திரட்டுகிறது."
    },
    # 43: C
    {
        "subtopic": "First FC Submission Year (TNPSC Gr 4 2013)",
        "key": "C",
        "en_stem": "In which year did the First Finance Commission submit its final report to the President?",
        "ta_stem": "முதலாவது நிதி ஆணையம் தனது இறுதி அறிக்கையை எந்த ஆண்டில் குடியரசுத் தலைவரிடம் சமர்ப்பித்தது?",
        "a": ("1951", "1951"),
        "b": ("1954", "1954"),
        "c": ("1952", "1952"),
        "d": ("1950", "1950"),
        "exp_en": "Constituted in November 1951, the First Finance Commission submitted its report in December 1952 covering 1952-1957.",
        "exp_ta": "நவம்பர் 1951-ல் அமைக்கப்பட்ட முதலாவது நிதி ஆணையம் 1952-1957 காலகட்டத்தை உள்ளடக்கிய தனது அறிக்கையை டிசம்பர் 1952-ல் சமர்ப்பித்தது.",
        "tip_en": "Appointed: 1951; Report Submitted: 1952.",
        "tip_ta": "நியமனம்: 1951; அறிக்கை சமர்ப்பிப்பு: 1952.",
        "fact_en": "Report was laid before Parliament in early 1953.",
        "fact_ta": "அறிக்கை 1953-ன் ஆரம்பத்தில் நாடாளுமன்றத்தில் சமர்ப்பிக்கப்பட்டது."
    },
    # 44: D
    {
        "subtopic": "7th FC Milestone (TNPSC Gr 1 2012)",
        "key": "D",
        "en_stem": "Which Finance Commission doubled the States' share of Union Excise Duties from 20% to 40%?",
        "ta_stem": "மத்திய கலால் வரியில் மாநிலங்களின் பங்கை 20%-லிருந்து 40% ஆக இரட்டிப்பாக்கிய நிதி ஆணையம் எது?",
        "a": ("Fourth Finance Commission", "நான்காவது நிதி ஆணையம்"),
        "b": ("Fifth Finance Commission", "ஐந்தாவது நிதி ஆணையம்"),
        "c": ("Sixth Finance Commission", "ஆறாவது நிதி ஆணையம்"),
        "d": ("Seventh Finance Commission", "ஏழாவது நிதி ஆணையம்"),
        "exp_en": "The Seventh Finance Commission (1977-78) headed by Justice J.M. Shelat doubled the excise devolution to 40% to reduce state dependence on deficit grants.",
        "exp_ta": "நீதிபதி ஜே.எம். ஷெலத் தலைமையிலான ஏழாவது நிதி ஆணையம் (1977-78) மாநிலங்கள் மானியங்களைச் சார்ந்திருப்பதை குறைக்க கலால் வரிப் பங்கை 40% ஆக இரட்டிப்பாக்கியது.",
        "tip_en": "7th FC Chairman: Justice J.M. Shelat.",
        "tip_ta": "7வது நிதி ஆணையத் தலைவர்: நீதிபதி ஜே.எம். ஷெலத்.",
        "fact_en": "This drastically boosted the untied statutory resources of States.",
        "fact_ta": "இது மாநிலங்களின் நிபந்தனையற்ற சட்டப்பூர்வ வளங்களை பெருமளவில் உயர்த்தியது."
    },
    # 45: A
    {
        "subtopic": "Area Devolution Weight (TNPSC Gr 1 2021)",
        "key": "A",
        "en_stem": "What percentage weight was allocated to 'Area' in the horizontal devolution formula of the 15th Finance Commission?",
        "ta_stem": "15வது நிதி ஆணையத்தின் கிடைமட்ட வரிப் பகிர்வு சூத்திரத்தில் 'நிலப்பரப்பிற்கு' எத்தனை சதவீத எடை ஒதுக்கப்பட்டது?",
        "a": ("15.0%", "15.0%"),
        "b": ("10.0%", "10.0%"),
        "c": ("7.5%", "7.5%"),
        "d": ("20.0%", "20.0%"),
        "exp_en": "The 15th Finance Commission assigned 15.0% weight to geographical Area to address the administrative costs of providing civic services across vast spatial terrain.",
        "exp_ta": "பரந்த புவியியல் பரப்பில் பொதுச் சேவைகளை வழங்குவதற்கான நிர்வாகச் செலவுகளை ஈடுகட்ட 15வது நிதி ஆணையம் நிலப்பரப்பிற்கு 15.0% எடையை ஒதுக்கியது.",
        "tip_en": "Area weight remained identical at 15.0% in both 14th and 15th FC.",
        "tip_ta": "14 மற்றும் 15வது ஆகிய இரு ஆணையங்களிலும் நிலப்பரப்பு எடை 15.0% என்றே சமமாக இருந்தது.",
        "fact_en": "Rajasthan and Madhya Pradesh derive significant benefit from this criterion.",
        "fact_ta": "ராஜஸ்தான் மற்றும் மத்தியப் பிரதேசம் போன்ற பெரிய மாநிலங்கள் இவ்வளவுகோலால் அதிக பலன் பெறுகின்றன."
    },
    # 46: B
    {
        "subtopic": "Tax Effort Weight (TNPSC Gr 2 2022)",
        "key": "B",
        "en_stem": "What weight did the 15th Finance Commission assign to 'Tax and Fiscal Effort' to reward own revenue mobilization?",
        "ta_stem": "சொந்த வரி வருவாய் திரட்டலை ஊக்குவிக்க 15வது நிதி ஆணையம் 'வரி மற்றும் நிதி முயற்சிக்கு' எத்தனை சதவீத எடையை ஒதுக்கியது?",
        "a": ("5.0%", "5.0%"),
        "b": ("2.5%", "2.5%"),
        "c": ("7.5%", "7.5%"),
        "d": ("1.0%", "1.0%"),
        "exp_en": "The 15th Finance Commission assigned 2.5% weight to Tax Effort, measured as the ratio of own tax revenue to GSDP compared against a 3-year moving average.",
        "exp_ta": "15வது நிதி ஆணையம் 3 ஆண்டு நகரும் சராசரியின் அடிப்படையில் கணக்கிடப்பட்ட சொந்த வரி-GSDP விகிதத்தைக் கொண்டு வரி முயற்சிக்கு 2.5% எடையை ஒதுக்கியது.",
        "tip_en": "Tax effort re-introduced an efficiency principle into horizontal devolution.",
        "tip_ta": "வரி முயற்சி கிடைமட்டப் பகிர்வில் செயல்திறன் கோட்பாட்டை மீண்டும் கொண்டுவந்தது.",
        "fact_en": "States with higher tax buoyancy gain an advantage from this 2.5% weight.",
        "fact_ta": "அதிக வரி வளர்ச்சி கொண்ட மாநிலங்கள் இந்த 2.5% எடை மூலம் கூடுதல் பலன் பெறுகின்றன."
    },
    # 47: C
    {
        "subtopic": "Union Territory Funding Mechanism (TNPSC Gr 1 2021)",
        "key": "C",
        "en_stem": "How are Union Territories (such as Ladakh and Chandigarh) financially funded relative to the Finance Commission divisible pool?",
        "ta_stem": "நிதி ஆணைய பகிர்வு நிதியுடன் ஒப்பிடுகையில் யூனியன் பிரதேசங்கள் (லடாக் மற்றும் சண்டிகர் போன்றவை) எவ்வாறு நிதி பெறுகின்றன?",
        "a": ("They receive direct shares from the 41% state divisible pool", "அவை 41% மாநில பகிர்வு நிதியிலிருந்து நேரடிப் பங்கைப் பெறுகின்றன"),
        "b": ("They are entirely self-funded through local stamp duties", "அவை உள்ளூர் முத்திரைத்தாள் வரிகள் மூலம் முழுமையாக சுயநிதி பெறுகின்றன"),
        "c": ("They are funded by the Central Government directly from its retainable share", "மத்திய அரசால் அதன் வசம் உள்ள பங்கிலிருந்து நேரடியாக நிதியளிக்கப்படுகின்றன"),
        "d": ("They are funded exclusively through international grants", "அவை பிரத்யேகமாக சர்வதேச மானியங்கள் மூலம் மட்டுமே நிதியளிக்கப்படுகின்றன"),
        "exp_en": "Union Territories are the constitutional responsibility of the Union Government and are funded directly from the Centre's retainable share (59% under 15th FC).",
        "exp_ta": "யூனியன் பிரதேசங்கள் மத்திய அரசின் அரசியலமைப்புப் பொறுப்பாகும், அவை மத்திய அரசின் வசம் உள்ள பங்கிலிருந்து (15வது FC-ன் கீழ் 59%) நேரடியாக நிதியளிக்கப்படுகின்றன.",
        "tip_en": "This is why devolution was reduced from 42% to 41% when J&K became UTs.",
        "tip_ta": "இதனால்தான் ஜம்மு காஷ்மீர் யூனியன் பிரதேசங்களாக மாறியபோது பகிர்வு 42%-லிருந்து 41% ஆகக் குறைக்கப்பட்டது.",
        "fact_en": "UTs without legislatures have no separate Consolidated Fund.",
        "fact_ta": "சட்டமன்றம் இல்லாத யூனியன் பிரதேசங்களுக்கு தனித் திரட்டப்பட்ட நிதி கிடையாது."
    },
    # 48: D
    {
        "subtopic": "Rajamannar Committee Setup Year (TNPSC Gr 2 2015)",
        "key": "D",
        "en_stem": "In which year did the Tamil Nadu Government constitute the historic Rajamannar Committee on Centre-State financial relations?",
        "ta_stem": "மத்திய-மாநில நிதி உறவுகள் குறித்து தமிழ்நாடு அரசு வரலாற்றுச் சிறப்புமிக்க ராஜமன்னார் குழுவை எந்த ஆண்டில் அமைத்தது?",
        "a": ("1965", "1965"),
        "b": ("1972", "1972"),
        "c": ("1975", "1975"),
        "d": ("1969", "1969"),
        "exp_en": "The Tamil Nadu Government under Chief Minister M. Karunanidhi constituted the Centre-State Relations Inquiry Committee under Dr. P.V. Rajamannar in September 1969.",
        "exp_ta": "முதலமைச்சர் மு. கருணாநிதி தலைமையிலான தமிழ்நாடு அரசு செப்டம்பர் 1969-ல் டாக்டர் பி.வி. ராஜமன்னார் தலைமையில் மத்திய-மாநில உறவுகள் ஆய்வுக் குழுவை அமைத்தது.",
        "tip_en": "Constituted: 1969; Report submitted: 1971.",
        "tip_ta": "அமைக்கப்பட்டது: 1969; அறிக்கை சமர்ப்பிக்கப்பட்டது: 1971.",
        "fact_en": "The Committee strongly advocated making the Finance Commission a permanent constitutional body.",
        "fact_ta": "இக்குழு நிதி ஆணையத்தை நிரந்தர அரசியலமைப்பு அமைப்பாக மாற்ற வேண்டும் என வலுவாக பரிந்துரைத்தது."
    },
    # 49: A
    {
        "subtopic": "Urban Health Earmark (TNPSC Gr 1 2022)",
        "key": "A",
        "en_stem": "Which sector received an unprecedented earmarked grant of Rs. 70,051 crore through local bodies under the 15th Finance Commission recommendations?",
        "ta_stem": "15வது நிதி ஆணையப் பரிந்துரைகளின் கீழ் உள்ளாட்சி அமைப்புகள் மூலம் முன்னெப்போதும் இல்லாத வகையில் ரூ. 70,051 கோடி பிரத்யேக மானியம் பெற்ற துறை எது?",
        "a": ("Primary Health and Diagnostics", "ஆரம்ப சுகாதாரம் மற்றும் நோய் கண்டறிதல்"),
        "b": ("Solar Rooftop Subsidies", "சூரிய சக்தி கூரை மானியங்கள்"),
        "c": ("Digital Literacy Centers", "டிஜிட்டல் எழுத்தறிவு மையங்கள்"),
        "d": ("Highway Tolling Infrastructure", "நெடுஞ்சாலை சுங்கச்சாவடி உள்கட்டமைப்பு"),
        "exp_en": "The 15th FC earmarked Rs. 70,051 crore specifically for strengthening the primary health sector and diagnostic infrastructure through rural and urban local bodies.",
        "exp_ta": "15வது நிதி ஆணையம் ஊரக மற்றும் நகர்ப்புற உள்ளாட்சிகள் மூலம் ஆரம்ப சுகாதாரத் துறை மற்றும் நோய் கண்டறியும் கட்டமைப்பை வலுப்படுத்த ரூ. 70,051 கோடியை பிரத்யேகமாக ஒதுக்கியது.",
        "tip_en": "A direct policy response to gaps exposed by the COVID-19 pandemic.",
        "tip_ta": "கோவிட்-19 பெருந்தொற்றால் வெளிப்பட்ட இடைவெளிகளுக்கான நேரடி கொள்கை பதில் இதுவாகும்.",
        "fact_en": "Funds upgraded sub-centres into functional Health and Wellness Centres (HWCs).",
        "fact_ta": "இந்நிதி துணை சுகாதார நிலையங்களை செயல்படும் நலவாழ்வு மையங்களாக (HWCs) மேம்படுத்தியது."
    },
    # 50: B
    {
        "subtopic": "16th FC Secretarial Appointment (Current Affairs 2024)",
        "key": "B",
        "en_stem": "Who was appointed as the Secretary to the Sixteenth Finance Commission in January 2024?",
        "ta_stem": "ஜனவரி 2024-ல் பதினாறாவது நிதி ஆணையத்தின் செயலாளராக நியமிக்கப்பட்டவர் யார்?",
        "a": ("Ajay Narayan Jha", "அஜய் நாராயண் ஜா"),
        "b": ("Ritvik Ranjanam Pandey", "ரித்விக் ரஞ்சனம் பாண்டே"),
        "c": ("T.V. Somanathan", "டி.வி. சோமநாதன்"),
        "d": ("Anirudh Tewari", "அனிருத் திவாரி"),
        "exp_en": "Senior IAS officer Ritvik Ranjanam Pandey was appointed Secretary to the Sixteenth Finance Commission.",
        "exp_ta": "மூத்த ஐ.ஏ.எஸ் அதிகாரி ரித்விக் ரஞ்சனம் பாண்டே 16வது நிதி ஆணையத்தின் செயலாளராக நியமிக்கப்பட்டார்.",
        "tip_en": "Ritvik Pandey is a 1998-batch Karnataka cadre IAS officer.",
        "tip_ta": "ரித்விக் பாண்டே 1998 தொகுதி கர்நாடக பிரிவு ஐ.ஏ.எஸ் அதிகாரியாவார்.",
        "fact_en": "The Secretary oversees the research, administrative, and technical wings of the Commission.",
        "fact_ta": "செயலாளர் ஆணையத்தின் ஆராய்ச்சி, நிர்வாக மற்றும் தொழில்நுட்ப பிரிவுகளை மேற்பார்வையிடுகிறார்."
    }
]

def build_questions():
    questions = []
    for idx, item in enumerate(raw_pyq_items, start=1):
        qid = f"FC_PYQ_{idx:03d}"
        correct_k = item["key"]
        
        opts_en = [item["a"][0], item["b"][0], item["c"][0], item["d"][0]]
        opts_ta = [item["a"][1], item["b"][1], item["c"][1], item["d"][1]]
        
        why_en = {
            "A": f"Option A is correct: {item['exp_en']}" if correct_k == "A" else "Option A is not the correct answer.",
            "B": f"Option B is correct: {item['exp_en']}" if correct_k == "B" else "Option B is not the correct answer.",
            "C": f"Option C is correct: {item['exp_en']}" if correct_k == "C" else "Option C is not the correct answer.",
            "D": f"Option D is correct: {item['exp_en']}" if correct_k == "D" else "Option D is not the correct answer."
        }
        why_ta = {
            "A": f"தெரிவு A சரியானது: {item['exp_ta']}" if correct_k == "A" else "தெரிவு A சரியான விடை அல்ல.",
            "B": f"தெரிவு B சரியானது: {item['exp_ta']}" if correct_k == "B" else "தெரிவு B சரியான விடை அல்ல.",
            "C": f"தெரிவு C சரியானது: {item['exp_ta']}" if correct_k == "C" else "தெரிவு C சரியான விடை அல்ல.",
            "D": f"தெரிவு D சரியானது: {item['exp_ta']}" if correct_k == "D" else "தெரிவு D சரியான விடை அல்ல."
        }
        
        q = make_fc_q(
            qid=qid,
            diff="Medium",
            qtype="PYQ Practice",
            subtopic=item["subtopic"],
            en_stem=item["en_stem"],
            ta_stem=item["ta_stem"],
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
            tags=["polity", "finance_commission", "pyq_practice", item["subtopic"].lower().replace(" ", "_")]
        )
        questions.append(q)
    return questions

if __name__ == "__main__":
    qs = build_questions()
    print(f"Generated {len(qs)} raw PYQ questions for Finance Commission.")
    assert len(qs) == 50, f"Expected 50 questions, got {len(qs)}"
    
    out_path = os.path.join("data", "questions", "polity", "fc_pyq.json")
    alias_path = os.path.join("data", "questions", "polity", "fc_pyq_practice.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, ensure_ascii=False, indent=2)
    shutil.copyfile(out_path, alias_path)
    print(f"Saved PYQ MCQs to {out_path} and alias {alias_path}")
    
    val = ContentValidator()
    report = val.validate_file(out_path, expected_count=50, expected_prefix="FC_PYQ_")
    print(f"Validation Report: {'PASS' if report.is_valid else 'FAIL'} | Total: {report.total_audited}")
    if not report.is_valid:
        for iss in report.issues[:10]:
            print(f"  Issue: {iss}")
    print(f"Key Distribution: {report.key_distribution}")
