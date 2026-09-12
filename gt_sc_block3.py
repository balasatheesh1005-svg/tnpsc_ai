# -*- coding: utf-8 -*-
"""
Supreme Court Grand Test Block 3 (Questions 51 to 75)
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

from gt_sc_block1 import mk_q

def get_block3():
    b3 = []

    # Q51
    b3.append(mk_q(51, "Medium", "Direct",
        "Under Article 136(2) of the Constitution, Special Leave Petition (SLP) CANNOT be granted by the Supreme Court against any judgment, determination, sentence or order passed by which of the following bodies?",
        "சரத்து 136(2)-ன் படி, பின்வரும் எந்த அமைப்பின் தீர்ப்பு, உத்தரவு அல்லது தண்டனைக்கு எதிராக உச்ச நீதிமன்றம் சிறப்பு விடுப்பு மனுவை (SLP) அனுமதிக்க முடியாது?",
        {"A": "State Administrative Tribunals", "B": "Courts or Tribunals constituted by or under any law relating to the Armed Forces", "C": "Central Administrative Tribunal (CAT)", "D": "National Green Tribunal (NGT)"},
        {"A": "மாநில நிர்வாகத் தீர்ப்பாயங்கள்", "B": "முப்படைகள் தொடர்பான சட்டத்தின் கீழ் அமைக்கப்பட்ட ராணுவ நீதிமன்றங்கள் அல்லது தீர்ப்பாயங்கள்", "C": "மத்திய நிர்வாகத் தீர்ப்பாயம் (CAT)", "D": "தேசிய பசுமைத் தீர்ப்பாயம் (NGT)"},
        "B",
        "Article 136(2) explicitly provides that nothing in Article 136(1) shall apply to any judgment, determination, sentence or order passed or made by any court or tribunal constituted by or under any law relating to the Armed Forces (Court Martial).",
        "சரத்து 136(2) வெளிப்படையாகக் கூறுகிறது: முப்படைகள் (ராணுவ நீதிமன்றங்கள்/Court Martial) தொடர்பான சட்டத்தின் கீழ் அமைக்கப்பட்ட எந்தவொரு நீதிமன்ற தீர்ப்புக்கும் சரத்து 136(1) பொருந்தாது.",
        "Candidates confuse civilian tribunals (CAT, NGT) with military tribunals. SLP applies to CAT/NGT, but NOT to Armed Forces Tribunals under Art 136(2).",
        "சிவில் தீர்ப்பாயங்களுக்கும் ராணுவத் தீர்ப்பாயங்களுக்கும் உள்ள வேறுபாட்டை கவனிக்கவும். ராணுவ நீதிமன்ற உத்தரவுகளுக்கு SLP கிடையாது.",
        "Armed Forces decisions are subject to High Court writ jurisdiction under Article 226.",
        "ராணுவ நீதிமன்ற உத்தரவுகள் சரத்து 226-ன் கீழ் உயர் நீதிமன்றப் பேராணை வரம்பிற்கு உட்பட்டவை.",
        "Article 136(2) protects military discipline and summary court martial proceedings.",
        "ராணுவ ஒழுக்கத்தைப் பாதுகாக்க சரத்து 136(2) விலக்களிக்கிறது."))

    # Q52
    b3.append(mk_q(52, "Hard", "Statement",
        "Consider the following matters regarding the Original Jurisdiction of the Supreme Court under Article 131:\n1. Inter-state river water disputes (Article 262).\n2. Matters referred to the Finance Commission (Article 280).\n3. Adjustment of expenses between Union and States under pre-constitution treaties.\nWhich of the above are EXCLUDED from the Original Jurisdiction of the Supreme Court under Article 131?",
        "சரத்து 131-ன் கீழ் உச்ச நீதிமன்றத்தின் மூல அதிகார வரம்பிலிருந்து (Original Jurisdiction) விலக்கப்பட்ட விவகாரங்கள் பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. மாநிலங்களுக்கு இடையேயான நதிநீர் சர்ச்சைகள் (சரத்து 262).\n2. நிதி ஆணையத்திற்கு அனுப்பப்படும் விவகாரங்கள் (சரத்து 280).\n3. அரசியலமைப்புக்கு முந்தைய உடன்படிக்கைகளின் கீழ் மத்திய-மாநில அரசுச் செலவுகள் சரிசெய்தல்.\nமேற்கூறியவற்றில் எவை சரத்து 131 மூல அதிகார வரம்பிலிருந்து விலக்கப்பட்டுள்ளன?",
        {"A": "1 and 2 only", "B": "2 and 3 only", "C": "1 and 3 only", "D": "1, 2 and 3"},
        {"A": "1 மற்றும் 2 மட்டும்", "B": "2 மற்றும் 3 மட்டும்", "C": "1 மற்றும் 3 மட்டும்", "D": "1, 2 மற்றும் 3"},
        "D",
        "All three matters are explicitly EXCLUDED from Article 131 Original Jurisdiction: 1. Pre-constitution treaties/agreements. 2. Inter-State River Water Disputes (Art 262). 3. Matters referred to Finance Commission (Art 280). 4. Adjustment of expenses between Centre and States.",
        "மூன்று விவகாரங்களும் சரத்து 131 மூல அதிகார வரம்பிலிருந்து வெளிப்படையாக விலக்கப்பட்டுள்ளன: 1. அரசியலமைப்புக்கு முந்தைய ஒப்பந்தங்கள். 2. நதிநீர் சர்ச்சைகள் (சரத்து 262). 3. நிதி ஆணைய விவகாரங்கள் (சரத்து 280). 4. மத்திய-மாநில அரசுச் செலவுகள் சரிசெய்தல்.",
        "Inter-State Water Disputes Tribunal decisions under Art 262 exclude Supreme Court's Article 131 jurisdiction.",
        "சரத்து 262-ன் கீழான நதிநீர் தீர்ப்பாய விவகாரங்கள் உச்ச நீதிமன்ற மூல அதிகார வரம்பிலிருந்து விலக்கப்பட்டவை.",
        "Commercial disputes between governments are also excluded if an agreement provides otherwise.",
        "வணிக ரீதியான சர்ச்சைகளும் ஒப்பந்தங்கள் அடிப்படையில் விலக்கப்படலாம்.",
        "Article 131 applies strictly to LEGAL RIGHTS of governments.",
        "சரத்து 131 சட்டபூர்வ உரிமைகளுக்கு மட்டுமே பொருந்தும்."))

    # Q53
    b3.append(mk_q(53, "Medium", "Direct",
        "Under Article 126 of the Constitution, an Acting Chief Justice of India is appointed by whom?",
        "அரசியலமைப்பின் சரத்து 126-ன் கீழ், இந்திய செயல் தலைமை நீதிபதி யாரால் நியமிக்கப்படுகிறார்?",
        {"A": "The President of India", "B": "The Senior-most judge of Supreme Court automatically", "C": "The Chief Justice of India before proceeding on leave", "D": "The Collegium of Supreme Court"},
        {"A": "இந்தியக் குடியரசுத் தலைவரால்", "B": "உச்ச நீதிமன்றத்தின் மூத்த நீதிபதி தானாகவே", "C": "விடுப்பில் செல்லும் முன் இந்தியத் தலைமை நீதிபதியால்", "D": "உச்ச நீதிமன்ற கொலீஜியத்தால்"},
        "A",
        "Article 126 states that when the office of Chief Justice of India is vacant or when the CJI is absent, the duties shall be performed by such one of the other judges of the court as the PRESIDENT may appoint for the purpose.",
        "சரத்து 126-ன் படி தலைமை நீதிபதி பதவி காலியாக இருக்கும்போதோ அல்லது அவர் இல்லாமலிருக்கும் போதோ குடியரசுத் தலைவரால் நியமிக்கப்படும் உச்ச நீதிமன்ற நீதிபதி அப்பொறுப்பை ஆற்றுவார்.",
        "Do not assume seniority operates automatically without a Presidential appointment order under Art 126.",
        "குடியரசுத் தலைவர் உத்தரவின்றி தானாகவே நியமனம் நடைபெறும் எனக் கருதக் கூடாது.",
        "Acting CJI has all the powers of the Chief Justice of India during his tenure.",
        "செயல் தலைமை நீதிபதி தலைமை நீதிபதியின் அனைத்து அதிகாரங்களையும் பெறுவார்.",
        "Appointed only from sitting Supreme Court judges.",
        "தற்போதைய உச்ச நீதிமன்ற நீதிபதிகளிலிருந்தே நியமிக்கப்படுகிறார்."))

    # Q54
    b3.append(mk_q(54, "Hard", "Statement",
        "Consider the following statements regarding the appointment of Ad Hoc Judges under Article 127 of the Constitution:\n1. Ad Hoc judges are appointed when there is a lack of quorum of sitting Supreme Court judges to hold or continue any session.\n2. The Chief Justice of India appoints a High Court judge (qualified for SC) as an Ad Hoc judge.\n3. The appointment requires previous consent of the President AND consultation with the Chief Justice of the High Court concerned.\nWhich of the statements given above are correct?",
        "சரத்து 127-ன் கீழ் தற்காலிக (அட் ஹாக்) நீதிபதிகள் நியமனம் பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. உச்ச நீதிமன்ற அமர்வை நடத்தத் தேவையான நீதிபதிகளின் எண்ணிக்கை (கோரம்) இல்லாதபோது தற்காலிக நீதிபதிகள் நியமிக்கப்படுகிறார்கள்.\n2. உச்ச நீதிமன்றத் தகுதியுடைய உயர் நீதிமன்ற நீதிபதியை இந்தியத் தலைமை நீதிபதி தற்காலிக நீதிபதியாக நியமிக்கிறார்.\n3. இந்த நியமனத்திற்கு குடியரசுத் தலைவரின் முன் ஒப்புதலும், சம்பந்தப்பட்ட உயர் நீதிமன்ற தலைமை நீதிபதியின் கலந்தாலோசனையும் கட்டாயமாகும்.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
        {"A": "1, 2 and 3", "B": "1 and 2 only", "C": "2 and 3 only", "D": "1 and 3 only"},
        {"A": "1, 2 மற்றும் 3", "B": "1 மற்றும் 2 மட்டும்", "C": "2 மற்றும் 3 மட்டும்", "D": "1 மற்றும் 3 மட்டும்"},
        "A",
        "All three statements are correct under Article 127. 1. Appointed for lack of quorum. 2. CJI appoints a qualified HC judge. 3. Requires previous consent of President + consultation with CJI of concerned High Court.",
        "மூன்று கூற்றுகளும் சரத்து 127-ன் கீழ் சரியானவை. 1. கோரம் இல்லாதபோது நியமனம். 2. CJI தகுதியான உயர் நீதிமன்ற நீதிபதியை நியமிக்கிறார். 3. குடியரசுத் தலைவர் முன் ஒப்புதல் + உயர் நீதிமன்ற தலைமை நீதிபதி கலந்தாலோசனை அவசியம்.",
        "Ad hoc judge is a SITTING High Court judge temporarily serving in Supreme Court.",
        "தற்காலிக நீதிபதி என்பவர் உச்ச நீதிமன்றத்தில் தற்காலிகமாகப் பணியாற்றும் தற்போதைய உயர் நீதிமன்ற நீதிபதியாவார்.",
        "Enjoys all powers, privileges, and duties of an SC judge while attending SC sittings.",
        "உச்ச நீதிமன்ற அமர்வுகளில் பங்கேற்கும்போது அனைத்து அதிகாரங்களையும் பெறுகிறார்.",
        "Duty of the HC judge to attend SC sittings in priority over HC duties.",
        "உயர் நீதிமன்றப் பணிகளை விட உச்ச நீதிமன்ற அமர்வுகளுக்கு முன்னுரிமை அளிக்க வேண்டும்."))

    # Q55
    b3.append(mk_q(55, "Hard", "Statement",
        "Consider the following statements regarding attendance of Retired Judges under Article 128 of the Constitution:\n1. The Chief Justice of India may at any time request a retired SC judge or retired HC judge (qualified for SC) to sit and act as a judge of the SC.\n2. Previous consent of the President AND consent of the retired judge himself are MANDATORY.\n3. A retired judge so requested shall be deemed to be a judge of the Supreme Court for all constitutional purposes including seniority.",
        "சரத்து 128-ன் கீழ் ஓய்வுபெற்ற நீதிபதிகளின் சேவை பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. இந்தியத் தலைமை நீதிபதி எந்நேரத்திலும் ஓய்வுபெற்ற உச்ச நீதிமன்ற நீதிபதி அல்லது ஓய்வுபெற்ற உயர் நீதிமன்ற நீதிபதியை (உச்ச நீதிமன்றத் தகுதியுடையவர்) அமர்வில் பங்கேற்குமாறு கோரலாம்.\n2. குடியரசுத் தலைவரின் முன் ஒப்புதலும், அந்த ஓய்வுபெற்ற நீதிபதியின் சம்மதமும் கட்டாயமாகும்.\n3. அவ்வாறு கோரப்படும் ஓய்வுபெற்ற நீதிபதி மூப்பு உட்பட அனைத்து அரசியலமைப்பு நோக்கங்களுக்கும் உச்ச நீதிமன்ற நீதிபதியாகவே கருதப்படுவார்.\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானது?",
        {"A": "1 and 2 only", "B": "2 and 3 only", "C": "1 and 3 only", "D": "1, 2 and 3"},
        {"A": "1 மற்றும் 2 மட்டும்", "B": "2 மற்றும் 3 மட்டும்", "C": "1 மற்றும் 3 மட்டும்", "D": "1, 2 மற்றும் 3"},
        "A",
        "Statements 1 and 2 are correct. Statement 3 is INCORRECT (Trap point). Article 128 explicitly specifies that such a retired judge shall NOT otherwise be deemed to be a judge of the Supreme Court.",
        "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது (TNPSC பொறி). சரத்து 128 வெளிப்படையாகக் கூறுகிறது: அவ்வாறு பணியாற்றும் ஓய்வுபெற்ற நீதிபதி மற்றபடி உச்ச நீதிமன்ற நீதிபதியாகக் கருதப்பட மாட்டார்.",
        "Retired judge gets allowances determined by President, but does NOT become a full-fledged SC judge.",
        "ஓய்வுபெற்ற நீதிபதி குடியரசுத் தலைவர் தீர்மானிக்கும் படிகளைப் பெறுவார், ஆனால் அவர் முழுமையான உச்ச நீதிமன்ற நீதிபதியாக மாட்டார்.",
        "Consent of the retired judge HIMSELF is compulsory (he cannot be forced).",
        "அந்த ஓய்வுபெற்ற நீதிபதியின் சம்மதம் கட்டாயமாகும் (அவரை நிர்ப்பந்திக்க முடியாது).",
        "Article 128 helps clear pending arrears of cases.",
        "நிலுவை வழக்குகளை விரைவில் முடிக்க சரத்து 128 உதவுகிறது."))

    # Q56
    b3.append(mk_q(56, "Medium", "Direct",
        "Can a 'Distinguished Jurist' in the opinion of the President be appointed directly as a judge of a High Court under Article 217?",
        "குடியரசுத் தலைவரின் பார்வையில் 'சிறந்த சட்ட நிபுணராக' (Distinguished Jurist) இருக்கும் ஒருவரை சரத்து 217-ன் கீழ் நேரடியாக உயர் நீதிமன்ற நீதிபதியாக நியமிக்க முடியுமா?",
        {"A": "No, distinguished jurist category exists ONLY for Supreme Court judge appointment under Article 124(3)(c), NOT for High Court", "B": "Yes, distinguished jurists can be appointed to both Supreme Court and High Courts", "C": "Yes, but only with the consent of the State Governor", "D": "Yes, if recommended by the Bar Council of the State"},
        {"A": "இல்லை, சிறந்த சட்ட நிபுணர் தகுதி என்பது சரத்து 124(3)(c)-ன் கீழ் உச்ச நீதிமன்ற நீதிபதி நியமனத்திற்கு மட்டுமே உண்டு, உயர் நீதிமன்றத்திற்கு இல்லை", "B": "ஆம், சிறந்த சட்ட நிபுணர்களை உச்ச நீதிமன்றம் மற்றும் உயர் நீதிமன்றம் இரண்டிற்கும் நியமிக்கலாம்", "C": "ஆம், ஆனால் மாநில ஆளுநரின் ஒப்புதலுடன் மட்டுமே நியமிக்கலாம்", "D": "ஆம், மாநில வழக்கறிஞர்கள் கழகம் (Bar Council) பரிந்துரைத்தால் நியமிக்கலாம்"},
        "A",
        "The category of 'distinguished jurist in the opinion of the President' exists ONLY under Article 124(3)(c) for appointment as a Supreme Court judge. It is NOT included in Article 217 for High Court judge appointment.",
        "குடியரசுத் தலைவரின் பார்வையில் 'சிறந்த சட்ட நிபுணர்' என்ற தகுதி சரத்து 124(3)(c)-ன் கீழ் உச்ச நீதிமன்றத்திற்கு மட்டுமே உண்டு; சரத்து 217-ன் கீழ் உயர் நீதிமன்றத்திற்கு அத்தகுதி இல்லை.",
        "Classic TNPSC trap question comparing SC (Art 124) and HC (Art 217) qualifications.",
        "உச்ச நீதிமன்றம் மற்றும் உயர் நீதிமன்ற நீதிபதிகளின் தகுதிகளை ஒப்பிடும் முக்கிய TNPSC வினா.",
        "High Court Judge qualifications (Art 217): 1. Citizen of India, 2. Judicial office in India for 10 years OR Advocate of HC for 10 years.",
        "உயர் நீதிமன்ற நீதிபதி தகுதிகள்: 1. இந்தியக் குடிமகன், 2. 10 ஆண்டுகள் நீதித்துறை பதவி அல்லது 10 ஆண்டுகள் வழக்கறிஞர் பணி.",
        "No distinguished jurist has ever been appointed to SC till date.",
        "இதுவரை சிறந்த சட்ட நிபுணர் பிரிவில் எவரும் உச்ச நீதிமன்றத்திற்கு நியமிக்கப்படவில்லை."))

    # Q57
    b3.append(mk_q(57, "Medium", "Direct",
        "Under the Judges (Inquiry) Act, 1968, what is the composition of the 3-member Judicial Committee constituted by the Speaker/Chairman to investigate charges against a Supreme Court judge?",
        "நீதிபதிகள் (விசாரணை) சட்டம் 1968-ன் கீழ், உச்ச நீதிமன்ற நீதிபதி மீதான குற்றச்சாட்டுகளை விசாரிக்க சபாநாயகர்/தலைவரால் அமைக்கப்படும் 3 உறுப்பினர் நீதித்துறை குழுவின் அமைப்பு என்ன?",
        {"A": "Chief Justice or SC Judge + Chief Justice of a High Court + A Distinguished Jurist", "B": "Three Senior-most Judges of the Supreme Court", "C": "Union Law Minister + Attorney General + Supreme Court Judge", "D": "CJI + Prime Minister + Speaker of Lok Sabha"},
        {"A": "தலைமை நீதிபதி அல்லது உச்ச நீதிமன்ற நீதிபதி + உயர் நீதிமன்ற தலைமை நீதிபதி + சிறந்த சட்ட நிபுணர்", "B": "உச்ச நீதிமன்றத்தின் மூன்று மூத்த நீதிபதிகள்", "C": "மத்திய சட்ட அமைச்சர் + தலைமை வழக்கறிஞர் + உச்ச நீதிமன்ற நீதிபதி", "D": "CJI + பிரதமர் + மக்களவை சபாநாயகர்"},
        "A",
        "Under Section 3(2) of Judges (Inquiry) Act 1968, the 3-member committee consists of: 1. Chief Justice of India or a sitting SC Judge. 2. A Chief Justice of a High Court. 3. A distinguished jurist.",
        "நீதிபதிகள் (விசாரணை) சட்டம் 1968-ன் பிரிவு 3(2)-ன் படி 3 உறுப்பினர் குழுவின் அமைப்பு: 1. CJI அல்லது உச்ச நீதிமன்ற நீதிபதி. 2. உயர் நீதிமன்ற தலைமை நீதிபதி. 3. ஒரு சிறந்த சட்ட நிபுணர்.",
        "If the committee finds the judge guilty of proved misbehaviour or incapacity, the House can take up the removal motion.",
        "குழு குற்றம் நிரூபிக்கப்பட்டதாகக் கூறினால் மட்டுமே அவையில் நீக்கத் தீர்மானம் மீது வாக்கெடுப்பு நடைபெறும்.",
        "If the committee acquits the judge, the motion is dropped immediately.",
        "குழு குற்றமற்றவர் எனக் கூறினால் தீர்மானம் உடனடியாகக் கைவிடப்படும்.",
        "The committee functions as a quasi-judicial body.",
        "இக்குழு ஒரு நீதி சார்ந்த அமைப்பாகச் செயல்படுகிறது."))

    # Q58
    b3.append(mk_q(58, "Hard", "Scenario",
        "What is the exact majority required in BOTH Houses of Parliament to pass an address to the President for the removal of a Supreme Court judge under Article 124(4)?",
        "சரத்து 124(4)-ன் கீழ் உச்ச நீதிமன்ற நீதிபதியை நீக்கக் குடியரசுத் தலைவருக்கு உரை அனுப்புவதற்கு நாடாளுமன்றத்தின் இரு அவைகளிலும் தேவைப்படும் சரியான பெரும்பான்மை எது?",
        {"A": "Simple Majority of members present and voting", "B": "Majority of total membership of the House AND a majority of not less than two-thirds of members present and voting", "C": "Two-thirds majority of total membership of the House", "D": "Three-fourths majority of members present and voting"},
        {"A": "வருகை தந்து வாக்களிக்கும் உறுப்பினர்களில் சாதாரண பெரும்பான்மை", "B": "அவையின் மொத்த உறுப்பினர்களில் பெரும்பான்மை மற்றும் வருகை தந்து வாக்களிப்பவர்களில் 2/3 பங்கு குறையாத பெரும்பான்மை", "C": "அவையின் மொத்த உறுப்பினர்களில் 2/3 பங்கு பெரும்பான்மை", "D": "வருகை தந்து வாக்களிக்கும் உறுப்பினர்களில் 3/4 பங்கு பெரும்பான்மை"},
        "B",
        "Article 124(4) mandates Special Majority: Supported by a majority of the TOTAL membership of that House AND by a majority of not less than TWO-THIRDS of the members of that House PRESENT AND VOTING in the same session.",
        "சரத்து 124(4)-ன் படி சிறப்பு பெரும்பான்மை தேவை: அந்த அவையின் மொத்த உறுப்பினர்களில் பெரும்பான்மை (Majority of Total Membership) மற்றும் அதே கூட்டத்தொடரில் வருகை தந்து வாக்களிப்பவர்களில் 2/3 பங்கு குறையாத பெரும்பான்மை (2/3 Present and Voting).",
        "This Special Majority must be obtained in BOTH Lok Sabha and Rajya Sabha in the SAME SESSION.",
        "இந்த சிறப்பு பெரும்பான்மை ஒரே கூட்டத்தொடரில் மக்களவை மற்றும் மாநிலங்களவை இரண்டிலும் பெறப்பட வேண்டும்.",
        "After address is passed by both Houses, the President passes an order removing the judge.",
        "இரு அவைகளிலும் உரை நிறைவேறிய பின் குடியரசுத் தலைவர் நீக்க உத்தரவைப் பிறப்பிக்கிறார்.",
        "Grounds: Proved Misbehaviour or Incapacity.",
        "காரணங்கள்: நிரூபிக்கப்பட்ட தவறான நடத்தை அல்லது திறனின்மை."))

    # Q59
    b3.append(mk_q(59, "Medium", "Direct",
        "Who was the FIRST judge of the Supreme Court of India against whom impeachment/removal proceedings were initiated in Parliament in 1991-1993?",
        "1991-1993 இல் நாடாளுமன்றத்தில் நீக்கத் தீர்மானம் (Impeachment/Removal) கொண்டுவரப்பட்ட இந்திய உச்ச நீதிமன்றத்தின் முதல் நீதிபதி யார்?",
        {"A": "Justice V. Ramaswami", "B": "Justice Soumitra Sen", "C": "Justice P.D. Dinakaran", "D": "Justice Dipak Misra"},
        {"A": "நீதிபதி வி. இராமசுவாமி", "B": "நீதிபதி சௌமித்ரா சென்", "C": "நீதிபதி பி.டி. தினகரன்", "D": "நீதிபதி தீபக் மிஸ்ரா"},
        "A",
        "Justice V. Ramaswami (1991-1993) was the FIRST SC judge against whom removal proceedings were initiated. The inquiry committee found him guilty of financial irregularities, but the motion failed in Lok Sabha in May 1993 because Congress party abstained, failing to secure 2/3 majority.",
        "நீதிபதி வி. இராமசுவாமி (1991-1993) மீதே முதன்முதலில் நீக்கத் தீர்மானம் கொண்டுவரப்பட்டது. விசாரணைக் குழு குற்றம் நிரூபிக்கப்பட்டதாகக் கூறியும், மே 1993-ல் காங்கிரஸ் கட்சி வாக்கெடுப்பில் பங்கேற்காததால் மக்களவையில் 2/3 பெரும்பான்மை கிடைக்காமல் தீர்மானம் தோற்றது.",
        "No Supreme Court judge has been impeached/removed by Parliament till date.",
        "இதுவரை எந்தவொரு உச்ச நீதிமன்ற நீதிபதியும் நாடாளுமன்றத்தால் நீக்கப்படவில்லை.",
        "Justice Soumitra Sen (Calcutta HC) resigned after Rajya Sabha passed removal motion in 2011.",
        "கொல்கத்தா உயர் நீதிமன்ற நீதிபதி சௌமித்ரா சென் மாநிலங்களவையில் தீர்மானம் வென்றதும் ராஜினாமா செய்தார்.",
        "Justice P.D. Dinakaran resigned before committee inquiry completed.",
        "நீதிபதி பி.டி. தினகரன் விசாரணை முடியும் முன் ராஜினாமா செய்தார்."))

    # Q60
    b3.append(mk_q(60, "Medium", "Direct",
        "Which of the following is correct regarding the nature of an Advisory Opinion given by the Supreme Court to the President under Article 143?",
        "சரத்து 143-ன் கீழ் உச்ச நீதிமன்றம் குடியரசுத் தலைவருக்கு வழங்கும் ஆலோசனை அபிப்பிராயத்தின் (Advisory Opinion) தன்மை குறித்த பின்வரும் கூற்றுகளில் எது சரியானது?",
        {"A": "The opinion is a binding judicial decree that must be mandatorily followed by the Union Government", "B": "The opinion is purely advisory and NOT binding on the President or lower courts, though it carries high persuasive value", "C": "The opinion becomes law of the land automatically under Article 141", "D": "The opinion can be challenged by citizens in the High Court"},
        {"A": "இந்த ஆலோசனை கருத்து மத்திய அரசால் கண்டிப்பாகப் பின்பற்றப்பட வேண்டிய கட்டுப்படுத்தும் நீதித்துறை உத்தரவாகும்", "B": "இந்த கருத்து வெறும் ஆலோசனையே அன்றி குடியரசுத் தலைவரையோ அல்லது கீழ் நீதிமன்றங்களையோ கட்டுப்படுத்தாது; ஆனால் அதிக வழிகாட்டுதல் மதிப்பைக் கொண்டது", "C": "இந்த கருத்து சரத்து 141-ன் கீழ் தானாகவே நாட்டின் சட்டமாக மாறுகிறது", "D": "இந்த ஆலோசனைக் கருத்தை குடிமக்கள் உயர் நீதிமன்றத்தில் சவால் செய்யலாம்"},
        "B",
        "An Advisory Opinion under Article 143 is NOT a judicial judgment or decree. It is purely ADVISORY in nature. The President is not bound to accept it, nor does it bind lower courts under Article 141 as a precedent.",
        "சரத்து 143-ன் கீழான ஆலோசனை அபிப்பிராயம் என்பது நீதித்துறை தீர்ப்பு அல்ல. அது வெறும் ஆலோசனையே ஆகும். குடியரசுத் தலைவர் அதை ஏற்க வேண்டிய கட்டாயமில்லை; சரத்து 141-ன் கீழ் கீழ் நீதிமன்றங்களையும் இது கட்டுப்படுத்தாது.",
        "Even though not binding under Art 141, SC advisory opinions carry high persuasive authority.",
        "சரத்து 141-ன் கீழ் சட்டப்பூர்வமாகப் பிணைக்கப்படாவிட்டாலும், இது மிகுந்த வழிகாட்டுதல் மதிப்புடையது.",
        "President refers questions of law or fact of public importance under Art 143.",
        "குடியரசுத் தலைவர் பொது முக்கியத்துவம் வாய்ந்த சட்ட வினாக்களை அனுப்புகிறார்.",
        "SC hears references in open court with Constitution Bench.",
        "அரசியலமைப்பு அமர்வு மூலமே விசாரிக்கப்படும்."))

    # Q61
    b3.append(mk_q(61, "Hard", "Match",
        "Match List-I (Presidential Reference under Article 143) with List-II (Subject Matter / Case Name):\n\nList-I:\na) Re Berubari Union (1960)\nb) Special Courts Bill (1978)\nc) Cauvery Water Disputes Tribunal (1991)\nd) Ayodhya Reference (1994)\n\nList-II:\n1. Power of Parliament to cede territory to foreign country\n2. Legality of creating special courts for trial of political offenses\n3. Validity of State Ordinance overriding Central Tribunal interim order\n4. Whether a Hindu temple existed before construction of Babri structure",
        "பட்டியல்-I (சரத்து 143 குடியரசுத் தலைவர் ஆலோசனை) பட்டியல்-II உடன் (பொருள்/வழக்கு) பொருத்துக:\n\nபட்டியல்-I:\na) பெருபாரி யூனியன் வழக்கு (1960)\nb) சிறப்பு நீதிமன்றங்கள் மசோதா (1978)\nc) காவேரி நதிநீர் தீர்ப்பாய வழக்கு (1991)\nd) அயோத்தி வழக்கு (1994)\n\nபட்டியல்-II:\n1. நிலப்பரப்பை வெளிநாட்டுக்கு விட்டுக்கொடுக்க நாடாளுமன்ற அதிகாரம்\n2. அரசியல் குற்றங்களை விசாரிக்க சிறப்பு நீதிமன்றங்கள் அமைப்பதன் சட்டபூர்வத்தன்மை\n3. மத்திய தீர்ப்பாய உத்தரவை மாநில அவசரச்சட்டம் முறியடிப்பதன் செல்லுபடித் தன்மை\n4. பாப்ரி மசூதிக்கு முன் இந்து கோயில் இருந்ததா என்ற கேள்வி",
        {"A": "a-1, b-2, c-3, d-4", "B": "a-2, b-1, c-4, d-3", "C": "a-1, b-3, c-2, d-4", "D": "a-4, b-2, c-3, d-1"},
        {"A": "a-1, b-2, c-3, d-4", "B": "a-2, b-1, c-4, d-3", "C": "a-1, b-3, c-2, d-4", "D": "a-4, b-2, c-3, d-1"},
        "A",
        "Correct Match:\na) Re Berubari (1960) -> Ceding territory to Pakistan (1)\nb) Special Courts Bill (1978) -> Trial of political emergency offenses (2)\nc) Cauvery Tribunal (1991) -> Karnataka Ordinance overriding tribunal order invalid (3)\nd) Ayodhya Reference (1994) -> Historical temple existence question (4 - SC refused to answer under Clause 1)",
        "சரியான பொருத்தம்:\na) பெருபாரி (1960) -> பாகிஸ்தானுக்கு நிலம் கொடுத்தல் (1)\nb) சிறப்பு நீதிமன்றங்கள் (1978) -> அரசியல் அவசரநிலை குற்ற வழக்குகள் (2)\nc) காவேரி தீர்ப்பாயம் (1991) -> கர்நாடக அவசரச்சட்டம் செல்லாது (3)\nd) அயோத்தி வழக்கு (1994) -> கோயில் இருந்ததா என்ற கேள்வி (4 - பதிலளிக்க SC மறுத்தது)",
        "In Ayodhya Reference (1994), SC REFUSED to answer the question, exercising discretion under Clause 1.",
        "அயோத்தி வழக்கில் (1994) பிரிவு 1-ன் கீழ் பதிலளிக்க உச்ச நீதிமன்றம் மறுத்துவிட்டது.",
        "In Cauvery reference (1991), SC held State Ordinance overriding tribunal order was unconstitutional.",
        "காவேரி வழக்கில் மாநில அவசரச்சட்டம் செல்லாது எனத் தீர்ப்பளித்தது.",
        "15 Presidential references have been made under Article 143 till date.",
        "இதுவரை 15 குடியரசுத் தலைவர் ஆலோசனைகள் சரத்து 143-ன் கீழ் அனுப்பப்பட்டுள்ளன."))

    # Q62
    b3.append(mk_q(62, "Hard", "Statement",
        "Consider the following statements comparing Original, Writ, and Appellate Jurisdictions of the Supreme Court:\n1. Original Jurisdiction (Art 131) deals exclusively with intergovernmental federal disputes.\n2. Writ Jurisdiction (Art 32) is an original jurisdiction exercisable by private citizens for enforcement of Fundamental Rights.\n3. Appellate Jurisdiction (Arts 132-136) can be exercised ONLY if the High Court certifies the case under Article 134A without exception.\nWhich of the statements given above are correct?",
        "உச்ச நீதிமன்றத்தின் மூல அதிகார வரம்பு, பேராணை அதிகாரம் மற்றும் மேல்முறையீட்டு அதிகார வரம்பு ஒப்பிடல் பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. மூல அதிகார வரம்பு (சரத்து 131) கூட்டாட்சி அரசாங்கங்களுக்கு இடையேயான சர்ச்சைகளை மட்டுமே கையாள்கிறது.\n2. பேராணை அதிகாரம் (சரத்து 32) என்பது அடிப்படை உரிமைகளை அமல்படுத்தத் தனிநபர்கள் அணுகும் ஒரு மூல அதிகார வரம்பாகும்.\n3. மேல்முறையீட்டு அதிகாரம் (சரத்துகள் 132-136) என்பது உயர் நீதிமன்றம் சரத்து 134A-ன் கீழ் சான்றளித்தால் மட்டுமே விதிவிலக்கின்றி பயன்படுத்த முடியும்.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
        {"A": "1 and 2 only", "B": "2 and 3 only", "C": "1 and 3 only", "D": "1, 2 and 3"},
        {"A": "1 மற்றும் 2 மட்டும்", "B": "2 மற்றும் 3 மட்டும்", "C": "1 மற்றும் 3 மட்டும்", "D": "1, 2 மற்றும் 3"},
        "A",
        "Statements 1 and 2 are correct. Statement 3 is INCORRECT because Article 136 (Special Leave Petition) allows Supreme Court to grant appeal WITHOUT High Court certificate, and criminal appeals under Art 134(1)(a)&(b) lie as of right without certificate.",
        "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் சரத்து 136-ன் கீழ் (SLP) உயர் நீதிமன்ற சான்றிதழ் இன்றியே உச்ச நீதிமன்றம் மேல்முறையீட்டை அனுமதிக்க முடியும்.",
        "SLP under Article 136 is an exception to the requirement of High Court certification under Article 134A.",
        "சரத்து 136-ன் கீழான SLP என்பது உயர் நீதிமன்ற சான்றிதழ் நிபந்தனைக்கு ஒரு விதிவிலக்காகும்.",
        "Writ jurisdiction under Art 32 is original in nature (citizen can go directly to SC).",
        "சரத்து 32-ன் கீழான பேராணை அதிகாரம் மூல அதிகாரத் தன்மையுடையது.",
        "Federal Original Jurisdiction under Art 131 is exclusive to Supreme Court.",
        "சரத்து 131 மூல அதிகார வரம்பு உச்ச நீதிமன்றத்திற்கு மட்டுமே உரியது."))

    # Q63
    b3.append(mk_q(63, "Hard", "Scenario",
        "Compare the Writ Jurisdiction of the Supreme Court under Article 32 with that of the High Court under Article 226. Which of the following is CONSTITUTIONALLY ACCURATE?",
        "சரத்து 32-ன் கீழ் உச்ச நீதிமன்ற பேராணை அதிகாரத்தையும், சரத்து 226-ன் கீழ் உயர் நீதிமன்ற பேராணை அதிகாரத்தையும் ஒப்பிடுக. அரசியலமைப்பு ரீதியாக எது சரியானது?",
        {"A": "Supreme Court's writ jurisdiction is NARROWER in scope (only for Fundamental Rights) but WIDER in territorial extent (all India); High Court's writ jurisdiction is WIDER in scope (Fundamental Rights + other legal rights) but NARROWER in territorial extent", "B": "Supreme Court's writ jurisdiction is wider in both scope and territorial extent than High Court", "C": "High Court's writ jurisdiction is narrower in both scope and territorial extent than Supreme Court", "D": "Both Supreme Court and High Court have identical writ jurisdiction in all respects"},
        {"A": "உச்ச நீதிமன்றத்தின் பேராணை அதிகாரம் நோக்கத்தில் குறுகியது (அடிப்படை உரிமைகளுக்கு மட்டுமே) ஆனால் நிலப்பரப்பில் பரந்தது (இந்தியா முழுவதும்); உயர் நீதிமன்றத்தின் பேராணை அதிகாரம் நோக்கத்தில் பரந்தது (அடிப்படை உரிமை + பிற சட்ட உரிமைகள்) ஆனால் நிலப்பரப்பில் குறுகியது", "B": "நோக்கத்திலும் நிலப்பரப்பிலும் உச்ச நீதிமன்ற பேராணை அதிகாரமே உயர் நீதிமன்றத்தை விடப் பெரியது", "C": "நோக்கத்திலும் நிலப்பரப்பிலும் உயர் நீதிமன்ற பேராணை அதிகாரமே உச்ச நீதிமன்றத்தை விடச் சிறியது", "D": "அனைத்து அம்சங்களிலும் உச்ச நீதிமன்றம் மற்றும் உயர் நீதிமன்றப் பேராணை அதிகாரங்கள் ஒரே மாதிரியானவை"},
        "A",
        "Classic Constitutional Distinction: SC writ power (Art 32) is narrower in scope (ONLY Fundamental Rights) but wider in territory (entire India). HC writ power (Art 226) is wider in scope (FR + Ordinary Legal Rights) but narrower in territory (state limits/cause of action).",
        "முக்கிய அரசியலமைப்பு வேறுபாடு: உச்ச நீதிமன்ற அதிகாரம் (சரத்து 32) நோக்கத்தில் குறுகியது (அடிப்படை உரிமைகளுக்கு மட்டுமே) ஆனால் இந்தியா முழுவதும் செல்லும். உயர் நீதிமன்ற அதிகாரம் (சரத்து 226) நோக்கத்தில் பரந்தது (அடிப்படை உரிமைகள் + பிற சட்ட உரிமைகள்) ஆனால் அம்மாநிலத்திற்கு மட்டுமே செல்லும்.",
        "Also, Article 32 is itself a Fundamental Right (SC cannot refuse), whereas Article 226 is discretionary (HC can refuse if alternate remedy exists).",
        "சரத்து 32 என்பதே ஒரு அடிப்படை உரிமை (SC மறுக்க முடியாது); சரத்து 226 என்பது விருப்ப உரிமை (HC மறுக்கலாம்).",
        "Chandrakumar Case (1997) held both Art 32 and Art 226 are part of Basic Structure.",
        "சந்திரகுமார் வழக்கு (1997) சரத்து 32 மற்றும் 226 இரண்டும் அடிப்படை கட்டமைப்பு என்றது.",
        "Very high-yield TNPSC Group 1 question!",
        "TNPSC குரூப் 1 தேர்வில் அடிக்கடி கேட்கப்படும் வினா!"))

    # Q64
    b3.append(mk_q(64, "Medium", "Match",
        "Match the Supreme Court Writs in List-I with their Target Authorities in List-II:\n\nList-I:\na) Habeas Corpus\nb) Mandamus\nc) Certiorari\nd) Quo-Warranto\n\nList-II:\n1. Public Official holding public statutory office\n2. Judicial or Quasi-Judicial Tribunal\n3. Person holding a public office created by statute\n4. Public authority or Private Individual detaining a citizen",
        "பட்டியல்-I ல் உள்ள பேராணைகளை பட்டியல்-II ல் உள்ள இலக்கு அதிகாரிகளுடன் பொருத்துக:\n\nபட்டியல்-I:\na) ஆட்கொணர்வுப் பேராணை (Habeas Corpus)\nb) கட்டளையுறுத்தும் பேராணை (Mandamus)\nc) நெறிமுறைப்படுத்தும் பேராணை (Certiorari)\nd) தகுதிகாண் பேராணை (Quo-Warranto)\n\nபட்டியல்-II:\n1. சட்டப்பூர்வ பொதுப் பதவியில் உள்ள அதிகாரி\n2. நீதி அல்லது நீதி சார்ந்த தீர்ப்பாயம்\n3. சட்டத்தால் உருவாக்கப்பட்ட பொதுப் பதவியைக் கைப்பற்றியவர்\n4. குடிமகனைச் சட்டவிரோதமாகக் காவலில் வைக்கும் பொது அதிகாரி அல்லது தனிநபர்",
        {"A": "a-4, b-1, c-2, d-3", "B": "a-1, b-4, c-3, d-2", "C": "a-4, b-2, c-1, d-3", "D": "a-2, b-1, c-4, d-3"},
        {"A": "a-4, b-1, c-2, d-3", "B": "a-1, b-4, c-3, d-2", "C": "a-4, b-2, c-1, d-3", "D": "a-2, b-1, c-4, d-3"},
        "A",
        "Correct Match:\na) Habeas Corpus -> Public or Private detainer (4)\nb) Mandamus -> Public official failing statutory duty (1)\nc) Certiorari -> Judicial/quasi-judicial tribunal (2)\nd) Quo-Warranto -> Person claiming public office (3)",
        "சரியான பொருத்தம்:\na) Habeas Corpus -> காவலில் வைக்கும் பொது அதிகாரி/தனிநபர் (4)\nb) Mandamus -> சட்டப்பூர்வ அதிகாரி (1)\nc) Certiorari -> நீதித் தீர்ப்பாயம் (2)\nd) Quo-Warranto -> பொதுப் பதவியைக் கைப்பற்றியவர் (3)",
        "Habeas corpus is unique because it applies to private individuals too.",
        "Habeas corpus தனிநபர்களுக்கும் பொருந்தும் ஒரே பேராணையாகும்.",
        "Certiorari quashes illegal orders of lower courts.",
        "Certiorari கீழ் நீதிமன்றங்களின் சட்டவிரோத உத்தரவுகளை ரத்து செய்கிறது.",
        "Mandamus forces performance of mandatory duty.",
        "Mandamus கடமையைச் செய்ய வற்புறுத்துகிறது."))

    # Q65
    b3.append(mk_q(65, "Hard", "Chronology",
        "Arrange the following landmark Supreme Court Judgments defining Judicial Review and Basic Structure in chronological order:\n1. Waman Rao v. Union of India\n2. Minerva Mills v. Union of India\n3. Kesavananda Bharati v. State of Kerala\n4. Indira Nehru Gandhi v. Raj Narain",
        "நீதித்துறை மறுஆய்வு மற்றும் அடிப்படை கட்டமைப்பை வரையறுத்த பின்வரும் உச்ச நீதிமன்ற தீர்ப்புகளைக் காலவரிசைப்படி அமைக்கவும்:\n1. வாமன் ராவ் எதிர் இந்திய யூனியன்\n2. மினர்வா மில்ஸ் எதிர் இந்திய யூனியன்\n3. கேசவானந்த பாரதி எதிர் கேரளா மாநிலம்\n4. இந்திரா நேரு காந்தி எதிர் ராஜ் நாரைன்",
        {"A": "3 -> 4 -> 2 -> 1", "B": "4 -> 3 -> 1 -> 2", "C": "3 -> 2 -> 4 -> 1", "D": "3 -> 4 -> 1 -> 2"},
        {"A": "3 -> 4 -> 2 -> 1", "B": "4 -> 3 -> 1 -> 2", "C": "3 -> 2 -> 4 -> 1", "D": "3 -> 4 -> 1 -> 2"},
        "A",
        "Chronological Order of Judgments:\n1. Kesavananda Bharati v. State of Kerala (April 1973)\n2. Indira Nehru Gandhi v. Raj Narain (Nov 1975)\n3. Minerva Mills v. Union of India (May 1980)\n4. Waman Rao v. Union of India (Nov 1980 / Nov 1981 - applied April 24, 1973 cut-off to 9th Schedule)\nHence, correct order is 3 -> 4 -> 2 -> 1.",
        "தீர்ப்புகளின் காலவரிசை:\n1. கேசவானந்த பாரதி வழக்கு (ஏப்ரல் 1973)\n2. இந்திரா நேரு காந்தி வழக்கு (நவம்பர் 1975)\n3. மினர்வா மில்ஸ் வழக்கு (மே 1980)\n4. வாமன் ராவ் வழக்கு (1981 - 9வது அட்டவணைக்கு ஏப்ரல் 24, 1973 எல்லையை நிர்ணயித்தது)\nஎனவே சரியான வரிசை 3 -> 4 -> 2 -> 1.",
        "Waman Rao (1981) drew the line that Ninth Schedule laws added AFTER April 24, 1973 are subject to Basic Structure test.",
        "வாமன் ராவ் வழக்கு ஏப்ரல் 24, 1973-க்கு பின் 9வது அட்டவணையில் சேர்க்கப்படும் சட்டங்களுக்கு எல்லைக் கோடு வரைந்தது.",
        "Indira Gandhi case (1975) applied Basic Structure for the 1st time.",
        "இந்திரா காந்தி வழக்கு முதன்முதலில் அடிப்படை கட்டமைப்பைப் பயன்படுத்தியது.",
        "Minerva Mills (1980) struck down Sec 55 of 42nd CAA.",
        "மினர்வா மில்ஸ் 42வது திருத்தப் பிரிவு 55-ஐ ரத்து செய்தது."))

    # Q66
    b3.append(mk_q(66, "Medium", "Direct",
        "What is meant by 'Epistolary Jurisdiction' of the Supreme Court in the context of Public Interest Litigation (PIL)?",
        "பொது நல வழக்கு (PIL) சூழலில் உச்ச நீதிமன்றத்தின் 'கடித அதிகார வரம்பு' (Epistolary Jurisdiction) என்பது எதனைக் குறிக்கிறது?",
        {"A": "The power of the Supreme Court to treat letters, telegrams, or postcards written by disadvantaged citizens or public-spirited individuals as formal writ petitions", "B": "The power of the Supreme Court to issue letters of request to foreign courts", "C": "The procedure of sending postal notices to respondents in civil suits", "D": "The power of President to write secret letters to CJI"},
        {"A": "பாதிக்கப்பட்ட ஏழை எளிய குடிமக்கள் அல்லது பொதுநல விரும்புவோர் எழுதும் கடிதங்கள், தம்பால்கள் அல்லது அஞ்சல் அட்டைகளை முறைப்படியான பேராணை மனுக்களாக ஏற்றுக்கொண்டு உச்ச நீதிமன்றம் விசாரிக்கும் அதிகாரம்", "B": "வெளிநாட்டு நீதிமன்றங்களுக்கு கோரிக்கை கடிதங்களை அனுப்பும் அதிகாரம்", "C": "சிவில் வழக்குகளில் எதிர்மனுதாரர்களுக்கு அஞ்சல் அறிவிப்புகள் அனுப்பும் நடைமுறை", "D": "தலைமை நீதிபதிக்குக் குடியரசுத் தலைவர் ரகசியக் கடிதம் எழுதும் அதிகாரம்"},
        "A",
        "Epistolary Jurisdiction refers to the SC relaxing procedural formalities by converting ordinary letters, postcards, or news reports written on behalf of poor/vulnerable victims into PIL writ petitions.",
        "எளிய மனிதர்கள், சிறைக் கைதிகள் அல்லது சமூக ஆர்வலர்கள் எழுதும் சாதாரணக் கடிதங்கள் மற்றும் அஞ்சல் அட்டைகளை பேராணை மனுக்களாக ஏற்றுக்கொண்டு நீதி வழங்கும் உச்ச நீதிமன்றத்தின் சிறப்பு நடைமுறை 'கடித அதிகார வரம்பு' (Epistolary Jurisdiction) எனப்படும்.",
        "Pioneered by Justice V.R. Krishna Iyer (Sunil Batra case - letter written by prisoner on brown paper) and Justice P.N. Bhagwati.",
        "நீதிபதி கிருஷ்ணய்யர் (சுனில் பாத்ரா வழக்கு) மற்றும் நீதிபதி பகவதியால் இக்கோட்பாடு வளர்க்கப்பட்டது.",
        "Removed financial barriers for poor litigants to access Supreme Court under Article 32.",
        "ஏழைகள் உச்ச நீதிமன்றத்தை அணுக இருந்த நிதித் தடைகளை இது நீக்கியது.",
        "A remarkable innovation of Indian Constitutional Law.",
        "இந்திய அரசியலமைப்பு சட்டத்தின் மிகச் சிறந்த புதிய கண்டுபிடிப்பு."))

    # Q67
    b3.append(mk_q(67, "Hard", "Match",
        "Match List-I (Pioneering PIL Landmark Case) with List-II (Human Rights Focus Area):\n\nList-I:\na) Hussainara Khatoon v. Home Secretary, Bihar (1979)\nb) Sunil Batra v. Delhi Administration (1978/1980)\nc) Bandhua Mukti Morcha v. Union of India (1984)\nd) Vishaka v. State of Rajasthan (1997)\n\nList-II:\n1. Protection of Bonded Labourers and Right to Live with Human Dignity\n2. Prevention of Sexual Harassment of Women at Workplace\n3. Protection of Rights of Undertrial Prisoners & Speedier Trial\n4. Protection of Prisoners against Torture and Cruel Treatment in Jails",
        "பட்டியல்-I (PIL மைல்கல் வழக்கு) பட்டியல்-II உடன் (மனித உரிமைப் பகுதி) பொருத்துக:\n\nபட்டியல்-I:\na) உசைனாரா காதுன் எதிர் பீகார் உள்துறை (1979)\nb) சுனில் பாத்ரா எதிர் டெல்லி நிர்வாகம் (1978/1980)\nc) பந்துவா முக்தி மோர்ச்சா எதிர் இந்திய யூனியன் (1984)\nd) விசாக்கா எதிர் ராஜஸ்தான் மாநிலம் (1997)\n\nபட்டியல்-II:\n1. கொத்தடிமைகள் பாதுகாப்பு மற்றும் மனிதக் கண்ணியத்துடன் வாழும் உரிமை\n2. பணியிடங்களில் பெண்களுக்கு எதிரான பாலியல் வன்கொடுமை தடுப்பு\n3. விசாரணைக்கடைச் சிறைவாசிகளின் உரிமைகள் மற்றும் விரைவு விசாரணை\n4. சிறைச்சாலைகளில் கைதிகள் மீதான சித்திரவதைக்கு எதிரான பாதுகாப்பு",
        {"A": "a-3, b-4, c-1, d-2", "B": "a-4, b-3, c-2, d-1", "C": "a-3, b-1, c-4, d-2", "D": "a-1, b-4, c-3, d-2"},
        {"A": "a-3, b-4, c-1, d-2", "B": "a-4, b-3, c-2, d-1", "C": "a-3, b-1, c-4, d-2", "D": "a-1, b-4, c-3, d-2"},
        "A",
        "Correct Match:\na) Hussainara Khatoon (1979) -> Undertrial prisoners rights & speedy trial (3)\nb) Sunil Batra (1978/1980) -> Jail torture protection & epistolary letter (4)\nc) Bandhua Mukti Morcha (1984) -> Rehabilitation of bonded labourers (1)\nd) Vishaka (1997) -> Workplace sexual harassment guidelines (2)",
        "சரியான பொருத்தம்:\na) உசைனாரா காதுன் (1979) -> விசாரணைக்கைதிகள் உரிமை & விரைவு விசாரணை (3)\nb) சுனில் பாத்ரா (1978/80) -> சிறைக் கைதிகள் சித்திரவதை தடுப்பு (4)\nc) பந்துவா முக்தி மோர்ச்சா (1984) -> கொத்தடிமைகள் மறுவாழ்வு (1)\nd) விசாக்கா (1997) -> பணியிடப் பாலியல் தொல்லை வழிகாட்டுதல் (2)",
        "Hussainara Khatoon case led to the release of over 40,000 undertrial prisoners in Bihar.",
        "உசைனாரா காதுன் வழக்கு பீகாரில் 40,000-க்கும் மேற்பட்ட விசாரணைக்கைதிகள் விடுதலையாக வழிவகுத்தது.",
        "Vishaka guidelines remained law until Sexual Harassment of Women at Workplace Act 2013 was enacted.",
        "விசாக்கா வழிகாட்டுதல்கள் 2013 சட்டம் வரும் வரை சட்டமாக நிலவின.",
        "All four cases are supreme examples of judicial protection of human rights.",
        "இந்நான்கு வழக்குகளும் மனித உரிமைகளைப் பாதுகாத்த உச்சகட்ட சான்றுகளாகும்."))

    # Q68
    b3.append(mk_q(68, "Medium", "Direct",
        "Where did the concept of 'Judicial Activism' originate, and who coined the term in 1947?",
        "'நீதித்துறை செயல்முனைவு' (Judicial Activism) என்ற கோட்பாடு முதன்முதலில் எந்த நாட்டில் தோன்றியது, மற்றும் 1947-ல் இச்சொல்லை முதன்முதலில் உருவாக்கியவர் யார்?",
        {"A": "USA; coined by Arthur Schlesinger Jr.", "B": "UK; coined by Lord Denning", "C": "France; coined by Montesquieu", "D": "India; coined by Dr. B.R. Ambedkar"},
        {"A": "அமெரிக்கா (USA); ஆர்தர் ஷ்லெசிங்கர் ஜூனியர் என்பவரால் உருவாக்கப்பட்டது", "B": "இங்கிலாந்து (UK); லார்ட் டென்னிங் என்பவரால் உருவாக்கப்பட்டது", "C": "பிரான்ஸ்; மாண்டெஸ்கியூ என்பவரால் உருவாக்கப்பட்டது", "D": "இந்தியா; டாக்டர் பி.ஆர். அம்பேத்கர் என்பவரால் உருவாக்கப்பட்டது"},
        "A",
        "The term 'Judicial Activism' was coined by American historian and journalist Arthur Schlesinger Jr. in a 1947 Fortune magazine article titled 'The Supreme Court: 1947'.",
        "'Judicial Activism' என்ற சொல் 1947-ல் அமெரிக்க வரலாற்றாசிரியர் ஆர்தர் ஷ்லெசிங்கர் ஜூனியர் (Arthur Schlesinger Jr.) என்பவரால் ஃபார்ச்சூன் இதழ் கட்டுரையில் முதன்முதலில் உருவாக்கப்பட்டது.",
        "Introduced in India in the late 1970s by Justices V.R. Krishna Iyer, P.N. Bhagwati, O. Chinnappa Reddy, and D.A. Desai.",
        "இந்தியாவில் 1970-களின் இறுதியில் நீதிபதிகள் கிருஷ்ணய்யர் மற்றும் பகவதியால் அறிமுகப்படுத்தப்பட்டது.",
        "Judicial Activism is also called 'Judicial Dynamism'.",
        "இது 'நீதித்துறை இயங்குதன்மை' என்றும் அழைக்கப்படுகிறது.",
        "Contrasted with Judicial Restraint where judges follow precedent strictly.",
        "நீதித்துறை கட்டுப்பாட்டுடன் (Judicial Restraint) இது வேறுபடுகிறது."))

    # Q69
    b3.append(mk_q(69, "Hard", "Statement",
        "Consider the following elements of the Indian Constitution:\n1. Supremacy of the Constitution\n2. Sovereign, Democratic and Republican nature of Indian polity\n3. Separation of Powers between Legislature, Executive and Judiciary\n4. Federal Character of the Constitution\n5. Absolute and Unamendable status of Part III Fundamental Rights in their entirety\nWhich of the above are recognized by the Supreme Court as components of the 'Basic Structure' of the Constitution?",
        "இந்திய அரசியலமைப்பின் பின்வரும் அம்சங்களைக் கருதுக:\n1. அரசியலமைப்பின் மேலாண்மை\n2. இந்திய அரசின் இறையாண்மை, ஜனநாயகம் மற்றும் குடியரசுத் தன்மை\n3. சட்டமன்றம், நிர்வாகம் மற்றும் நீதித்துறைக்கு இடையேயான அதிகாரப் பகிர்வு\n4. அரசியலமைப்பின் கூட்டாட்சித் தன்மை\n5. பகுதி III-ல் உள்ள அனைத்து அடிப்படை உரிமைகளும் முழுமையாகத் திருத்தப்பட முடியாத நிலை\nமேற்கூறியவற்றில் எவை 'அடிப்படை கட்டமைப்பின்' கூறுகளாக உச்ச நீதிமன்றத்தால் அங்கீகரிக்கப்பட்டுள்ளன?",
        {"A": "1, 2, 3 and 4 only", "B": "1, 2 and 3 only", "C": "2, 3, 4 and 5 only", "D": "1, 2, 3, 4 and 5"},
        {"A": "1, 2, 3 மற்றும் 4 மட்டும்", "B": "1, 2 மற்றும் 3 மட்டும்", "C": "2, 3, 4 மற்றும் 5 மட்டும்", "D": "1, 2, 3, 4 மற்றும் 5"},
        "A",
        "Statements 1, 2, 3, and 4 are elements of Basic Structure. Statement 5 is INCORRECT (Trap Point). Fundamental Rights IN THEIR ENTIRETY are NOT part of Basic Structure; Parliament CAN amend Fundamental Rights as long as the amendment does not destroy basic features (e.g., Right to Property was removed from FR in 1978).",
        "கூற்றுகள் 1, 2, 3 மற்றும் 4 சரியானவை. கூற்று 5 தவறானது (TNPSC பொறி). பகுதி III-ல் உள்ள அனைத்து அடிப்படை உரிமைகளும் முழுமையாக அடிப்படை கட்டமைப்பு அல்ல; அடிப்படை அம்சங்களைப் பாதிக்காத வரை அடிப்படை உரிமைகளை நாடாளுமன்றம் திருத்தலாம் (எ.கா. 1978-ல் சொத்து உரிமை நீக்கப்பட்டது).",
        "Golaknath (1967) held FRs unamendable, but Kesavananda Bharati (1973) OVERRULED Golaknath and held FRs CAN be amended except those forming Basic Structure.",
        "கோலக்நாத் தீர்ப்பு அடிப்படை உரிமைகளைத் திருத்த முடியாது என்றது; ஆனால் கேசவானந்த பாரதி தீர்ப்பு அதை மாற்றி, அடிப்படை கட்டமைப்பைப் பாதிக்காத வரை திருத்தலாம் என்றது.",
        "Basic Structure includes: Supremacy of Constitution, Federalism, Secularism, Judicial Review, Free & Fair Elections.",
        "அடிப்படை கட்டமைப்பில் அரசியலமைப்பு மேலாண்மை, கூட்டாட்சி, மதச்சார்பின்மை, நீதித்துறை மறுஆய்வு ஆகியவை அடங்கும்.",
        "Basic Structure list is open-ended and declared on a case-by-case basis.",
        "அடிப்படை கட்டமைப்புப் பட்டியல் வழக்குகளின் அடிப்படையில் விரிவடையும்."))

    # Q70
    b3.append(mk_q(70, "Medium", "Direct",
        "Under Section 2 of the Contempt of Courts Act, 1971, what constitutes 'Civil Contempt' as distinguished from 'Criminal Contempt'?",
        "நீதிமன்ற அவமதிப்புச் சட்டம் 1971-ன் பிரிவு 2-ன் கீழ், 'குற்றவியல் அவமதிப்பில்' இருந்து வேறுபடும் 'சிவில் அவமதிப்பு' (Civil Contempt) என்றால் என்ன?",
        {"A": "Willful disobedience to any judgment, decree, direction, order, writ or other process of a court, or willful breach of an undertaking given to a court", "B": "Publication of any matter which scandalises or lowers the authority of any court", "C": "Interfering with the due course of any judicial proceeding", "D": "Obstruction of administration of justice in any manner"},
        {"A": "நீதிமன்றத்தின் எந்தவொரு தீர்ப்பு, உத்தரவு, பேராணை அல்லது நடைமுறையை வேண்டுமென்றே மதிக்காமல் மீறுவது அல்லது நீதிமன்றத்திற்கு அளித்த உறுதிமொழியை வேண்டுமென்றே மீறுவது", "B": "நீதிமன்றத்தின் அதிகாரத்தைக் குறைக்கும் அல்லது அவதூறு செய்யும் செய்திகளை வெளியிடுவது", "C": "நீதிமன்ற நடவடிக்கைகளின் சீரான போக்கில் தலையிடுவது", "D": "நீதி நிர்வாகத்திற்கு எந்த வகையிலாவது இடையூறு செய்வது"},
        "A",
        "Section 2(b) defines Civil Contempt as 'willful disobedience to any judgment, decree, direction, order, writ or other process of a court or willful breach of an undertaking given to a court.' Options B, C, and D define Criminal Contempt under Section 2(c).",
        "பிரிவு 2(b)-ன் படி சிவில் அவமதிப்பு என்பது: 'நீதிமன்றத் தீர்ப்பு, உத்தரவு, பேராணை அல்லது உறுதிமொழியை வேண்டுமென்றே மீறுவது.' தெரிவுகள் B, C, D ஆகியவை பிரிவு 2(c)-ன் கீழான குற்றவியல் அவமதிப்பைக் குறிக்கின்றன.",
        "Civil Contempt = Willful disobedience of court order. Criminal Contempt = Scandalising court, interfering with proceedings, obstructing justice.",
        "சிவில் அவமதிப்பு = உத்தரவை மீறுதல். குற்றவியல் அவமதிப்பு = நீதிமன்றத்தை அவதூறு செய்தல் / நீதி நிர்வாகத்தைத் தடுத்தல்.",
        "Punishment for contempt: Simple imprisonment up to 6 months or fine up to Rs. 2,000 or both.",
        "அவமதிப்புத் தண்டனை: 6 மாதம் வரை சிறை அல்லது ரூ. 2,000 அபராதம் அல்லது இரண்டும்.",
        "Apology made to satisfaction of court may discharge the contemnor.",
        "மனமார்ந்த மன்னிப்பு கேட்டால் தண்டனையிலிருந்து விலக்கு அளிக்கப்படலாம்."))

    # Q71
    b3.append(mk_q(71, "Medium", "Match",
        "Match List-I (Institutional Feature) with List-II (Supreme Court vs High Court Constitutional Comparison):\n\nList-I:\na) Age of Retirement\nb) Constitutional Basis for Setup\nc) Power to Punish for Contempt\nd) Minimum Qualifications for Advocate\n\nList-II:\n1. Article 124 (SC) vs Article 217 (HC)\n2. 65 Years for SC vs 62 Years for HC\n3. Article 129 (SC) vs Article 215 (HC)\n4. 10 Years Advocate in HC for both SC & HC judge eligibility",
        "பட்டியல்-I (நிறுவன அம்சம்) பட்டியல்-II உடன் (உச்ச நீதிமன்றம் vs உயர் நீதிமன்றம் ஒப்பீடு) பொருத்துக:\n\nபட்டியல்-I:\na) ஓய்வுபெறும் வயது\nb) உருவாக்கம் பற்றிய அரசியலமைப்பு விதி\nc) அவமதிப்புக்குத் தண்டிக்கும் அதிகாரம்\nd) வழக்கறிஞருக்கான குறைந்தபட்ச தகுதி ஆண்டு\n\nபட்டியல்-II:\n1. சரத்து 124 (SC) vs சரத்து 217 (HC)\n2. SC-க்கு 65 வயது vs HC-க்கு 62 வயது\n3. சரத்து 129 (SC) vs சரத்து 215 (HC)\n4. SC & HC இரண்டிற்கும் 10 ஆண்டுகள் உயர் நீதிமன்ற வழக்கறிஞர் அனுபவம்",
        {"A": "a-2, b-1, c-3, d-4", "B": "a-1, b-2, c-3, d-4", "C": "a-2, b-3, c-1, d-4", "D": "a-3, b-1, c-2, d-4"},
        {"A": "a-2, b-1, c-3, d-4", "B": "a-1, b-2, c-3, d-4", "C": "a-2, b-3, c-1, d-4", "D": "a-3, b-1, c-2, d-4"},
        "A",
        "Correct Match:\na) Retirement Age -> SC (65 yrs) vs HC (62 yrs) (2)\nb) Setup Article -> Art 124 vs Art 217 (1)\nc) Contempt Court of Record -> Art 129 vs Art 215 (3)\nd) Advocate Qualification -> 10 years in High Court for both (4)",
        "சரியான பொருத்தம்:\na) ஓய்வு வயது -> SC (65 வயது) vs HC (62 வயது) (2)\nb) அமைவு விதி -> சரத்து 124 vs சரத்து 217 (1)\nc) அவமதிப்பு விதி -> சரத்து 129 vs சரத்து 215 (3)\nd) வழக்கறிஞர் காலம் -> இரண்டிற்கும் 10 ஆண்டுகள் உயர் நீதிமன்ற அனுபவம் (4)",
        "15th Amendment Act 1963 raised HC judge retirement age from 60 to 62 years.",
        "15வது திருத்தச் சட்டம் 1963 உயர் நீதிமன்ற நீதிபதி ஓய்வு வயதை 60 லிருந்து 62 ஆக உயர்த்தியது.",
        "SC retirement age has been 65 years since 1950.",
        "உச்ச நீதிமன்ற ஓய்வு வயது 1950 முதல் 65 ஆக உள்ளது.",
        "Advocate requirement is 10 years in HC for both courts.",
        "வழக்கறிஞருக்கான 10 ஆண்டுகள் உயர் நீதிமன்ற அனுபவத் தகுதி இரண்டிற்கும் பொதுவானது."))

    # Q72
    b3.append(mk_q(72, "Hard", "Scenario",
        "Under Article 137 of the Constitution and Supreme Court Rules, 2013, what is the limitation period for filing a Review Petition against a judgment or order of the Supreme Court?",
        "சரத்து 137 மற்றும் 2013 உச்ச நீதிமன்ற விதிகளின் படி, உச்ச நீதிமன்றத் தீர்ப்பு அல்லது உத்தரவுக்கு எதிராக மறுஆய்வு மனு (Review Petition) தாக்கல் செய்வதற்கான கால வரம்பு (Limitation Period) என்ன?",
        {"A": "Within 30 days from the date of the judgment or order", "B": "Within 60 days from the date of the judgment or order", "C": "Within 90 days from the date of the judgment or order", "D": "Within 1 year from the date of the judgment or order"},
        {"A": "தீர்ப்பு அல்லது உத்தரவு வழங்கப்பட்ட தேதியிலிருந்து 30 நாட்களுக்குள்", "B": "தீர்ப்பு வழங்கப்பட்ட தேதியிலிருந்து 60 நாட்களுக்குள்", "C": "தீர்ப்பு வழங்கப்பட்ட தேதியிலிருந்து 90 நாட்களுக்குள்", "D": "தீர்ப்பு வழங்கப்பட்ட தேதியிலிருந்து 1 ஆண்டுக்குள்"},
        "A",
        "Under Order XLVII of Supreme Court Rules 2013, a Review Petition under Article 137 must be filed within THIRTY (30) DAYS from the date of the judgment or order sought to be reviewed.",
        "2013 உச்ச நீதிமன்ற விதிகளின் படி, சரத்து 137-ன் கீழான மறுஆய்வு மனு தீர்ப்பு வந்த முப்பது (30) நாட்களுக்குள் தாக்கல் செய்யப்பட வேண்டும்.",
        "Review petition is ordinarily considered by circulation in CHAMBERS by the same bench of judges without open oral hearing, unless open court hearing is granted.",
        "மறுஆய்வு மனு வழக்கமாக நீதிபதிகளின் அறையிலேயே (Chambers) சுற்றறிக்கை மூலம் பரிசீலிக்கப்படும்; திறந்த நீதிமன்ற விசாரணை அரிதாகவே அளிக்கப்படும்.",
        "Grounds for Review: Discovery of new important evidence or error apparent on the face of the record.",
        "மறுஆய்வுக்கான காரணங்கள்: புதிய சான்றுகள் கிடைத்தல் அல்லது பதிவில் உள்ள வெளிப்படையான தவறு.",
        "Review is NOT a re-hearing of the original appeal.",
        "மறுஆய்வு என்பது வழக்கின் மீண்டும் ஒரு முழுமையான விசாரணையல்ல."))

    # Q73
    b3.append(mk_q(73, "Hard", "Statement",
        "Consider the following statements regarding 'Curative Petition' in the Supreme Court of India:\n1. It is a non-constitutional judicial remedy created by the SC in Rupa Ashok Hurra Case (2002).\n2. It can be entertained ONLY after a Review Petition under Article 137 has been dismissed.\n3. The petitioner must establish violation of natural justice or bias of a judge, and the petition must be certified by a Senior Advocate.\nWhich of the statements given above are correct?",
        "இந்திய உச்ச நீதிமன்றத்தில் 'சீராய்வு மனு' (Curative Petition) பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. இது ரூபா அசோக் ஹுர்ரா (2002) வழக்கில் உச்ச நீதிமன்றத்தால் உருவாக்கப்பட்ட அரசியலமைப்பிற்கு அப்பாற்பட்ட நீதித்துறை நிவாரணமாகும்.\n2. சரத்து 137-ன் கீழான மறுஆய்வு மனு (Review Petition) தள்ளுபடி செய்யப்பட்ட பிறகே இதை பரிசீலிக்க முடியும்.\n3. மனுதாரர் இயற்கை நீதி மீறல் அல்லது நீதிபதியின் சார்புத் தன்மையை நிரூபிக்க வேண்டும், மேலும் மனு மூத்த வழக்கறிஞரால் சான்றளிக்கப்பட வேண்டும்.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
        {"A": "1, 2 and 3", "B": "1 and 2 only", "C": "2 and 3 only", "D": "1 and 3 only"},
        {"A": "1, 2 மற்றும் 3", "B": "1 மற்றும் 2 மட்டும்", "C": "2 மற்றும் 3 மட்டும்", "D": "1 மற்றும் 3 மட்டும்"},
        "A",
        "All three statements are correct. Curative petition is the LAST judicial remedy invented in Rupa Ashok Hurra (2002). 1. Non-statutory judicial creation under inherent powers. 2. Allowed only after Art 137 Review dismissal. 3. Requires Senior Advocate certification + natural justice violation / bias grounds.",
        "மூன்று கூற்றுகளும் சரியானவை. சீராய்வு மனு (Curative Petition) என்பது ரூபா அசோக் ஹுர்ரா (2002) வழக்கில் உருவாக்கப்பட்ட இறுதி நீதித்துறை நிவாரணமாகும். 1. நீதித்துறையின் தன்னாட்சி உருவாக்கமாகும். 2. மறுஆய்வு மனு தள்ளுபடிக்குப் பின்பே வரும். 3. மூத்த வழக்கறிஞரின் சான்றிதழ் அவசியம்.",
        "Curative petition is first circulated to 3 senior-most SC judges + judges who passed the order.",
        "இம்மனு 3 மூத்த நீதிபதிகள் மற்றும் உத்தரவிட்ட நீதிபதிகளுக்குச் சுற்றறிக்கையாக அனுப்பப்படும்.",
        "Very rarely granted by the Supreme Court.",
        "மிகவும் அபூர்வமாகவே உச்ச நீதிமன்றத்தால் இது அனுமதிக்கப்படுகிறது.",
        "Prevents miscarriage of justice after final review dismissal.",
        "இறுதி மறுஆய்வு தள்ளுபடிக்கு பின் அநீதி நடப்பதைத் தடுக்கிறது."))

    # Q74
    b3.append(mk_q(74, "Hard", "Scenario",
        "Under Article 143(1) vs Article 143(2) of the Constitution, what is the key distinction regarding Supreme Court's obligation to tender an advisory opinion to the President?",
        "சரத்து 143(1) மற்றும் சரத்து 143(2) ஆகியவற்றுக்கு இடையே, குடியரசுத் தலைவருக்கு ஆலோசனை வழங்குவதில் உச்ச நீதிமன்றத்திற்கு உள்ள கடப்பாடு பற்றிய முக்கிய வேறுபாடு என்ன?",
        {"A": "Under Clause (1) on public importance, SC MAY refuse to give opinion; under Clause (2) on pre-constitution treaties, SC MUST obligatorily tender opinion", "B": "Under Clause (1), SC MUST give opinion; under Clause (2), SC MAY refuse", "C": "SC MUST give opinion under BOTH clauses", "D": "SC MAY refuse opinion under BOTH clauses"},
        {"A": "பிரிவு (1) பொது முக்கியத்துவம் விவகாரத்தில் SC கருத்து தெரிவிக்க மறுக்கலாம்; ஆனால் பிரிவு (2) அரசியலமைப்புக்கு முந்தைய உடன்படிக்கை விவகாரத்தில் SC கண்டிப்பாக கருத்து தெரிவிக்க வேண்டும்", "B": "பிரிவு (1)-ல் SC கண்டிப்பாக கருத்து தெரிவிக்க வேண்டும்; பிரிவு (2)-ல் மறுக்கலாம்", "C": "இரண்டு பிரிவுகளிலுமே SC கண்டிப்பாக கருத்து தெரிவிக்க வேண்டும்", "D": "இரண்டு பிரிவுகளிலுமே SC கருத்து தெரிவிக்க மறுக்கலாம்"},
        "A",
        "Crucial Distinction: Under Article 143(1) (Question of law/fact of public importance), SC 'may, after such hearing as it thinks fit, report to the President its opinion' (Discretionary - e.g. Ayodhya reference 1994 refused). Under Article 143(2) (Pre-constitution treaty/agreement), SC 'shall report to the President its opinion' (Mandatory obligation).",
        "முக்கிய வேறுபாடு: சரத்து 143(1)-ன் கீழ் (பொது முக்கியத்துவ வினா) கருத்து வழங்குவது உச்ச நீதிமன்றத்தின் விருப்ப உரிமை (மறுக்கலாம் - எ.கா. அயோத்தி வழக்கு 1994). ஆனால் சரத்து 143(2)-ன் கீழ் (அரசியலமைப்புக்கு முந்தைய ஒப்பந்தம்) கருத்து வழங்குவது உச்ச நீதிமன்றத்தின் கட்டாயக் கடமையாகும்.",
        "In Ayodhya Reference (1994), SC used Clause (1) discretion to refuse answering whether a temple existed before mosque.",
        "அயோத்தி வழக்கில் பிரிவு 1-ன் கீழ் உச்ச நீதிமன்றம் பதிலளிக்க மறுத்தது.",
        "In BOTH cases, opinion is NOT a binding judgment.",
        "இரண்டு பிரிவுகளிலுமே கருத்து பிணைக்கும் தீர்ப்பு அல்ல.",
        "Minimum 5 judges bench under Article 145(3).",
        "குறைந்தது 5 நீதிபதிகள் அமர்வு தேவை."))

    # Q75
    b3.append(mk_q(75, "Medium", "Direct",
        "Under Article 144 of the Constitution, what is the status of orders and decrees passed by the Supreme Court of India vis-a-vis civil and judicial authorities across all States and Union Territories?",
        "சரத்து 144-ன் படி, அனைத்து மாநிலங்கள் மற்றும் யூனியன் பிரதேசங்களில் உள்ள சிவில் மற்றும் நீதித்துறை அதிகாரிகளுடன் ஒப்பிடும்போது உச்ச நீதிமன்ற உத்தரவுகள் மற்றும் தீர்ப்புகளின் நிலை என்ன?",
        {"A": "All civil and judicial authorities in India are constitutionally bound to act in aid of the Supreme Court to execute its orders", "B": "State civil authorities must follow Supreme Court orders only if ratified by the Chief Minister", "C": "Judicial authorities in High Courts can suspend Supreme Court orders indefinitely", "D": "Article 144 applies only to Central Government officers, not State officers"},
        {"A": "இந்தியாவின் அனைத்து சிவில் மற்றும் நீதித்துறை அதிகாரிகளும் உச்ச நீதிமன்ற உத்தரவுகளை நிறைவேற்ற அதற்கு உதவியாகச் செயல்பட அரசியலமைப்பு ரீதியாகக் கடமைப்பட்டவர்கள்", "B": "முதலமைச்சர் ஒப்புதல் அளித்தால் மட்டுமே மாநில சிவில் அதிகாரி உச்ச நீதிமன்ற உத்தரவைப் பின்பற்ற வேண்டும்", "C": "உயர் நீதிமன்ற நீதித்துறை அதிகாரிகள் உச்ச நீதிமன்ற உத்தரவை காலவரையின்றி நிறுத்தி வைக்கலாம்", "D": "சரத்து 144 மத்திய அரசு அதிகாரிகளுக்கு மட்டுமே பொருந்தும், மாநில அதிகாரிகளுக்கு அல்ல"},
        "A",
        "Article 144 lays down that ALL civil and judicial authorities throughout the territory of India SHALL ACT IN AID OF THE SUPREME COURT. This ensures uniform execution of Supreme Court orders nationwide.",
        "சரத்து 144-ன் படி இந்தியாவின் அனைத்து நிலப்பரப்பிலும் உள்ள சிவில் மற்றும் நீதித்துறை அதிகாரிகள் அனைவரும் உச்ச நீதிமன்றத்திற்கு உதவியாகச் செயல்பட வேண்டும். இது நாடு முழுவதும் உச்ச நீதிமன்ற உத்தரவுகள் சீராக அமலாவதை உறுதி செய்கிறது.",
        "Failure to act in aid of SC under Art 144 attracts Contempt of Court under Art 129.",
        "சரத்து 144-ன் கீழ் உதவத் தவறுவது சரத்து 129 அவமதிப்பாகக் கருதப்படும்.",
        "Applies to police, IAS/IPS officers, revenue authorities, and all courts.",
        "காவல் துறை, IAS அதிகாரிகள் மற்றும் அனைத்து நீதிமன்றங்களுக்கும் பொருந்தும்.",
        "Binds both Union and State officials.",
        "மத்திய மற்றும் மாநில அதிகாரிகள் இருவரையும் கட்டுப்படுத்தும்."))

    return b3

if __name__ == "__main__":
    b3 = get_block3()
    print(f"Block 3 loaded with {len(b3)} questions.")
