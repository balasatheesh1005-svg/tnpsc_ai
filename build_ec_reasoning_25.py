"""
Generator for Election Commission Reasoning (Assertion-Reason) 25 MCQs (EC_R_001 to EC_R_025).
Conforms strictly to the 24-field TNPSC Nova AI schema.
"""

import json
import os
from ec_mcq_helper import make_ec_q

OUTPUT_PATH = os.path.join("data", "questions", "polity", "election_commission_reasoning.json")
ALIAS_PATH = os.path.join("data", "questions", "polity", "election_commission_assertion_reason.json")

OPT_TEMPLATES = {
    "A": {
        "en": "Both (A) and (R) are true and (R) is the correct explanation of (A)",
        "ta": "(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கம் ஆகும்"
    },
    "B": {
        "en": "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
        "ta": "(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல"
    },
    "C": {
        "en": "(A) is true but (R) is false",
        "ta": "(A) சரி, ஆனால் (R) தவறு"
    },
    "D": {
        "en": "(A) is false but (R) is true",
        "ta": "(A) தவறு, ஆனால் (R) சரி"
    }
}

RAW_REASONING = [
    # 1 - A
    {
        "id": "EC_R_001",
        "assertion_en": "Under Article 324(5), the Chief Election Commissioner cannot be removed from office except in like manner and on the like grounds as a Judge of the Supreme Court.",
        "assertion_ta": "சரத்து 324(5)-ன் கீழ், உச்ச நீதிமன்ற நீதிபதியை பதவி நீக்கம் செய்யும் அதே முறை மற்றும் காரணங்களின்றி தலைமைத் தேர்தல் ஆணையரை பதவி நீக்கம் செய்ய முடியாது.",
        "reason_en": "Constitutional protection of tenure was granted to the CEC to ensure institutional independence of the Election Commission from executive interference.",
        "reason_ta": "தேர்தல் ஆணையம் நிர்வாகத் தலையீடின்றி சுதந்திரமாகச் செயல்படுவதை உறுதி செய்வதற்காகவே தலைமைத் தேர்தல் ஆணையருக்கு இத்தகைய அரசியலமைப்பு பதவிப் பாதுகாப்பு வழங்கப்பட்டுள்ளது.",
        "correct_answer": "A",
        "difficulty": "Medium",
        "bloom_level": "Analyze",
        "exp_en": "Both statements are correct and (R) directly explains why Article 324(5) mirrors the removal procedure of an SC Judge (proven misbehavior or incapacity requiring a special majority in both Houses of Parliament).",
        "exp_ta": "இரண்டு கூற்றுகளும் சரியானவை. நிர்வாகத்தின் அழுத்தங்களுக்கு ஆட்படாமல் சுதந்திரமாகத் தேர்தலை நடத்தவே உச்ச நீதிமன்ற நீதிபதிக்கு இணையான பதவி நீக்கப் பாதுகாப்பு (சரத்து 324(5)) தலைமைத் தேர்தல் ஆணையருக்கு வழங்கப்பட்டுள்ளது.",
        "tnpsc_tip_en": "Remember: Other Election Commissioners do NOT have this same removal protection; they can be removed by the President simply on the recommendation of the CEC.",
        "tnpsc_tip_ta": "நினைவில் கொள்க: பிற தேர்தல் ஆணையர்களுக்கு இந்நீதிபதி இணையான பாதுகாப்பு இல்லை; தலைமைத் தேர்தல் ஆணையரின் பரிந்துரையின் பேரில் குடியரசுத் தலைவரால் அவர்கள் நீக்கப்படலாம்.",
        "revision_fact_en": "Article 324(5) explicitly safeguards CEC tenure, salary, and conditions of service which cannot be varied to his disadvantage after appointment.",
        "revision_fact_ta": "சரத்து 324(5) தலைமைத் தேர்தல் ஆணையரின் பதவிக்காலம் மற்றும் பணிக்கால நிபந்தனைகள் நியமனத்திற்குப் பின் அவருக்கு பாதகமாக மாற்றப்படக்கூடாது என்பதை உறுதி செய்கிறது.",
        "tags": ["Article 324", "CEC Removal", "Constitutional Safeguards"]
    },
    # 2 - B
    {
        "id": "EC_R_002",
        "assertion_en": "The Election Commission of India is an all-India body responsible for conducting elections to Parliament, State Legislatures, and the offices of President and Vice-President.",
        "assertion_ta": "இந்தியத் தேர்தல் ஆணையம் பாராளுமன்றம், மாநில சட்டமன்றங்கள் மற்றும் குடியரசுத் தலைவர், துணைக் குடியரசுத் தலைவர் பதவிகளுக்கான தேர்தல்களை நடத்தும் பொறுப்புடைய அகில இந்திய அமைப்பாகும்.",
        "reason_en": "Elections to local bodies (Panchayats and Municipalities) are governed by State Election Commissions established under Articles 243K and 243ZA.",
        "reason_ta": "உள்ளாட்சி அமைப்புகளுக்கான (ஊராட்சிகள் மற்றும் நகராட்சிகள்) தேர்தல்கள் சரத்து 243K மற்றும் 243ZA-ன் கீழ் அமைக்கப்பட்ட மாநிலத் தேர்தல் ஆணையங்களால் நடத்தப்படுகின்றன.",
        "correct_answer": "B",
        "difficulty": "Medium",
        "bloom_level": "Understand",
        "exp_en": "Both (A) and (R) are constitutionally true statements, but (R) describes local body election machinery which does not explain why ECI is an all-India body for central and state legislative elections.",
        "exp_ta": "(A) மற்றும் (R) இரண்டும் சரியானவை; ஆனால் உள்ளாட்சித் தேர்தல்கள் மாநிலத் தேர்தல் ஆணையத்தால் நடத்தப்படுவது என்பது ECI ஏன் அகில இந்திய அமைப்பாக உள்ளது என்பதற்கான காரணம் அல்ல.",
        "tnpsc_tip_en": "Trap alert: ECI has NO jurisdiction over Panchayats and Municipalities. That power rests entirely with the State Election Commission.",
        "tnpsc_tip_ta": "பொறி விழிப்புணர்வு: ஊராட்சிகள் மற்றும் நகராட்சிகள் தேர்தல்களில் இந்திய தேர்தல் ஆணையத்திற்கு எந்த அதிகார வரம்பும் இல்லை.",
        "revision_fact_en": "Articles 243K and 243ZA entrust superintendence, direction, and control of local body electoral rolls and elections to the State Election Commission.",
        "revision_fact_ta": "சரத்துகள் 243K மற்றும் 243ZA உள்ளாட்சித் தேர்தல் பட்டியல்கள் தயாரித்தல் மற்றும் தேர்தல்களை நடத்தும் அதிகாரத்தை மாநில தேர்தல் ஆணையத்திடம் ஒப்படைக்கின்றன.",
        "tags": ["ECI Jurisdiction", "State Election Commission", "Article 243K"]
    },
    # 3 - C
    {
        "id": "EC_R_003",
        "assertion_en": "The Model Code of Conduct (MCC) lacks statutory backing yet is strictly enforced by the Election Commission across all elections.",
        "assertion_ta": "மாதிரி நடத்தை விதிமுறைகளுக்கு (MCC) சட்டபூர்வ ஆதரவு இல்லை என்றாலும், அனைத்துத் தேர்தல்களிலும் தேர்தல் ஆணையத்தால் அது மிகக் கடுமையாக அமல்படுத்தப்படுகிறது.",
        "reason_en": "The Model Code of Conduct was formally enacted by Parliament as a schedule under the Representation of the People Act, 1951.",
        "reason_ta": "மாதிரி நடத்தை விதிமுறைகள் 1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் கீழ் ஒரு அட்டவணையாக பாராளுமன்றத்தால் முறைப்படி இயற்றப்பட்டது.",
        "correct_answer": "C",
        "difficulty": "Hard",
        "bloom_level": "Analyze",
        "exp_en": "Assertion (A) is true: MCC evolved through political consensus and is enforced under ECI's plenary constitutional powers (Art 324). Reason (R) is false because Parliament has never enacted MCC into statutory law.",
        "exp_ta": "கூற்று (A) சரி: மாதிரி நடத்தை விதிகள் அரசியல் கட்சிகளின் ஒருமித்த கருத்தால் உருவானவை, சரத்து 324-ன் கீழ் அமல்படுத்தப்படுகின்றன. காரணம் (R) தவறு: MCC பாராளுமன்ற சட்டமாக ஒருபோதும் இயற்றப்படவில்லை.",
        "tnpsc_tip_en": "Standing Committee on Personnel & Law recommended making MCC statutory, but ECI opposed it to prevent judicial stays during election cycles.",
        "tnpsc_tip_ta": "MCC-க்கு சட்ட அங்கீகாரம் வழங்க நிலைக்குழு பரிந்துரைத்தது, ஆனால் தேர்தல் நேரத்தில் நீதிமன்ற தடைகள் ஏற்படுவதைத் தவிர்க்க ECI அதனை எதிர்த்தது.",
        "revision_fact_en": "MCC was first evolved in Kerala during the 1960 Assembly elections and adopted nationally by ECI in 1962.",
        "revision_fact_ta": "1960 கேரள சட்டமன்றத் தேர்தலின் போது முதன்முதலில் உருவாக்கப்பட்ட MCC, 1962-ல் தேசிய அளவில் ECI-ஆல் ஏற்றுக்கொள்ளப்பட்டது.",
        "tags": ["Model Code of Conduct", "Article 324", "RPA 1951"]
    },
    # 4 - D
    {
        "id": "EC_R_004",
        "assertion_en": "The Chief Election Commissioner possesses absolute veto power and a casting vote to overrule decisions made by other Election Commissioners.",
        "assertion_ta": "தலைமைத் தேர்தல் ஆணையர் பிற தேர்தல் ஆணையர்களின் முடிவுகளை ரத்து செய்ய முழுமையான வீட்டோ அதிகாரம் மற்றும் முடிவாக்கும் வாக்குரிமையைக் கொண்டுள்ளார்.",
        "reason_en": "Under the law, the Chief Election Commissioner and other Election Commissioners enjoy equal status, compensation, and decide matters by majority in case of difference of opinion.",
        "reason_ta": "சட்டப்படி, தலைமைத் தேர்தல் ஆணையர் மற்றும் பிற தேர்தல் ஆணையர்கள் சம அந்தஸ்து, ஊதியம் பெறுகின்றனர் மற்றும் கருத்து வேறுபாட்டின் போது பெரும்பான்மை அடிப்படையில் முடிவெடுக்கின்றனர்.",
        "correct_answer": "D",
        "difficulty": "Medium",
        "bloom_level": "Evaluate",
        "exp_en": "Assertion (A) is false: The CEC has no veto or casting vote; the Commission acts as a multi-member collegiate body. Reason (R) is true: 1993 Act and 2023 Act mandate majority decision-making.",
        "exp_ta": "கூற்று (A) தவறு: தலைமைத் தேர்தல் ஆணையருக்கு வீட்டோ அல்லது தனி வாக்கு அதிகாரம் இல்லை; ஆணையம் ஒருமித்த அல்லது பெரும்பான்மை முடிவுகளையே எடுக்கிறது. காரணம் (R) சரி.",
        "tnpsc_tip_en": "Supreme Court in T.N. Seshan v. Union of India (1995) held CEC is merely primus inter pares (first among equals).",
        "tnpsc_tip_ta": "1995 டி.என். சேஷன் வழக்கில் தலைமைத் தேர்தல் ஆணையர் 'சமமானவர்களில் முதன்மையானவர்' மட்டுமே என்று உச்ச நீதிமன்றம் உறுதி செய்தது.",
        "revision_fact_en": "Section 10 of the 1993 EC Act (and 2023 Act) mandates that in case of difference of opinion, matters shall be decided according to the opinion of the majority.",
        "revision_fact_ta": "கருத்து வேறுபாடு ஏற்படும் போது பெரும்பான்மை ஆணையர்களின் கருத்தின்படியே முடிவெடுக்கப்பட வேண்டும் என்று சட்டம் கூறுகிறது.",
        "tags": ["Collegiate Body", "Majority Decision", "CEC Status"]
    },
    # 5 - A
    {
        "id": "EC_R_005",
        "assertion_en": "Under Article 329(b), an election to either House of Parliament or a State Legislature cannot be called into question except by an election petition.",
        "assertion_ta": "சரத்து 329(b)-ன் கீழ், பாராளுமன்றம் அல்லது மாநில சட்டமன்றத் தேர்தல்களை ஒரு தேர்தல் மனுவைத் தவிர வேறு எந்த வழக்கினாலும் கேள்விக்குள்ளாக்க முடியாது.",
        "reason_en": "The Constitution bars ordinary civil court interference in the ongoing electoral process to ensure elections are concluded smoothly without intermediate judicial injunctions.",
        "reason_ta": "தேர்தல் நடைமுறைகள் எவ்வித இடைக்காலத் தடையுமின்றி சுமூகமாக முடிவடைவதை உறுதி செய்வதற்காகவே சாதாரண உரிமையியல் நீதிமன்றங்கள் தலையிடுவதை அரசியலமைப்பு தடைசெய்கிறது.",
        "correct_answer": "A",
        "difficulty": "Hard",
        "bloom_level": "Analyze",
        "exp_en": "Both (A) and (R) are correct, and (R) correctly explains the non-obstante clause of Article 329, which bars civil court writ interference once election notification is issued.",
        "exp_ta": "இரண்டும் சரியானவை. தேர்தல் அறிவிப்பு வெளியிடப்பட்ட பின் இடைக்கால தடைகளைத் தவிர்த்து நடைமுறையைத் தடையின்றி முடிக்கவே சரத்து 329 உரிமையியல் நீதிமன்ற தலையீட்டைத் தடுக்கிறது.",
        "tnpsc_tip_en": "Election petitions can only be tried by the High Court (RPA 1951, Section 80A), with appeal lying to the Supreme Court under Section 116A.",
        "tnpsc_tip_ta": "தேர்தல் மனுக்களை விசாரிக்கும் அதிகாரம் உயர் நீதிமன்றத்திற்கு மட்டுமே உண்டு; மேல்முறையீடு உச்ச நீதிமன்றத்தில் செய்யப்படலாம்.",
        "revision_fact_en": "Article 329(a) bars questioning delimitation laws; Article 329(b) bars questioning elections except via election petition.",
        "revision_fact_ta": "சரத்து 329(a) தொகுதி மறுவரையறை சட்டங்களை நீதிமன்றத்தில் கேள்வி கேட்பதைத் தடை செய்கிறது; 329(b) தேர்தல் மனு மூலமே தேர்தல் முடிவை எதிர்க்க அனுமதிக்கிறது.",
        "tags": ["Article 329", "Election Petition", "Judicial Bar"]
    },
    # 6 - B
    {
        "id": "EC_R_006",
        "assertion_en": "Under Article 103, questions regarding the disqualification of a Member of Parliament under Article 102(1) are referred to the President of India.",
        "assertion_ta": "சரத்து 103-ன் கீழ், பாராளுமன்ற உறுப்பினர் ஒருவரின் தகுதி நீக்கம் (சரத்து 102(1)) தொடர்பான கேள்விகள் குடியரசுத் தலைவரின் முடிவுக்கு அனுப்பப்படுகின்றன.",
        "reason_en": "The President is constitutionally bound to obtain the opinion of the Election Commission and must act strictly according to such opinion.",
        "reason_ta": "குடியரசுத் தலைவர் தேர்தல் ஆணையத்தின் ஆலோசனையைப் பெற அரசியலமைப்பு ரீதியாகக் கடமைப்பட்டுள்ளார் மற்றும் அந்த ஆலோசனையின்படியே செயல்பட வேண்டும்.",
        "correct_answer": "B",
        "difficulty": "Medium",
        "bloom_level": "Understand",
        "exp_en": "Both statements are correct facts under Article 103, but (R) explains how the President must arrive at his decision rather than explaining why the matter is referred to him under (A).",
        "exp_ta": "இரண்டு கூற்றுகளும் அரசியலமைப்பு ரீதியாக உண்மையானவை. ஆனால் (R) குடியரசுத் தலைவர் முடிவெடுக்கும் முறையைக் கூறுகிறது, ஏன் குடியரசுத் தலைவரிடம் அனுப்பப்படுகிறது என்பதன் முழு விளக்கம் அல்ல.",
        "tnpsc_tip_en": "Disqualification on grounds of defection (10th Schedule) is decided by the Speaker/Chairman, NOT the President or ECI.",
        "tnpsc_tip_ta": "கட்சித்தாவல் தடைச் சட்டம் (10வது அட்டவணை) மூலம் ஏற்படும் தகுதி நீக்கத்தை சபாநாயகர்/தலைவர் தீர்மானிக்கிறார், குடியரசுத் தலைவர் அல்ல.",
        "revision_fact_en": "For State Legislature members, Article 192 mirrors Article 103: Governor decides in accordance with the opinion of ECI.",
        "revision_fact_ta": "மாநில சட்டமன்ற உறுப்பினர்களுக்கு சரத்து 192 பொருந்தும்: ஆளுநர் தேர்தல் ஆணையத்தின் ஆலோசனையின்படி செயல்படுகிறார்.",
        "tags": ["Article 103", "Article 192", "Disqualification of MPs"]
    },
    # 7 - C
    {
        "id": "EC_R_007",
        "assertion_en": "Under India's First-Past-The-Post (FPTP) system, a political party can secure a massive parliamentary majority even with a minority of the total popular vote.",
        "assertion_ta": "இந்தியாவின் 'முதலில் வந்தவருக்கு வெற்றி' (FPTP) முறையில், ஒரு அரசியல் கட்சி மொத்த மக்கள் வாக்குகளில் சிறுபான்மையைப் பெற்றிருந்தாலும் பாராளுமன்றத்தில் பெரும் பெரும்பான்மையைப் பெற முடியும்.",
        "reason_en": "The Constitution of India mandates the First-Past-The-Post system exclusively for elections to the Rajya Sabha and State Legislative Councils.",
        "reason_ta": "இந்திய அரசியலமைப்பு மாநிலங்களவை மற்றும் மாநில சட்ட மேலவைத் தேர்தல்களுக்கு மட்டுமே 'முதலில் வந்தவருக்கு வெற்றி' முறையைக் கட்டாயமாக்கியுள்ளது.",
        "correct_answer": "C",
        "difficulty": "Medium",
        "bloom_level": "Analyze",
        "exp_en": "Assertion (A) is true: In FPTP, legislative seat share often exaggerates the vote share plurality. Reason (R) is completely false: Rajya Sabha and Legislative Councils use Proportional Representation by Single Transferable Vote (PR-STV).",
        "exp_ta": "கூற்று (A) சரி: FPTP முறையில் 35% வாக்கு பெற்ற கட்சியும் 60% இடங்களை வெல்ல முடியும். காரணம் (R) முற்றிலும் தவறு: மாநிலங்களவைக்கு விகிதாசார பிரதிநிதித்துவ ஒற்றை மாற்று வாக்கு முறை பயன்படுத்தப்படுகிறது.",
        "tnpsc_tip_en": "FPTP is used for Lok Sabha and State Legislative Assemblies (direct elections), while PR-STV is used for Rajya Sabha, Legislative Councils, President, and VP.",
        "tnpsc_tip_ta": "மக்களவை மற்றும் சட்டமன்றங்களுக்கு FPTP முறை; மாநிலங்களவை, சட்ட மேலவை, குடியரசுத் தலைவர் தேர்தலுக்கு PR-STV முறை பயன்படுத்தப்படுகிறது.",
        "revision_fact_en": "In 1984 Lok Sabha elections, Congress won 48.1% popular vote but secured 76.5% of parliamentary seats due to FPTP characteristics.",
        "revision_fact_ta": "1984 தேர்தலில் காங்கிரஸ் 48.1% வாக்குகள் பெற்று 76.5% இடங்களைக் கைப்பற்றியது FPTP அமைப்பின் ஒரு முக்கிய சான்றாகும்.",
        "tags": ["FPTP System", "Electoral Systems", "Proportional Representation"]
    },
    # 8 - D
    {
        "id": "EC_R_008",
        "assertion_en": "The administrative expenses, salaries, and pensions of the Election Commission of India are charged upon the Consolidated Fund of India and are non-votable.",
        "assertion_ta": "இந்திய தேர்தல் ஆணையத்தின் நிர்வாகச் செலவுகள், ஊதியங்கள் மற்றும் ஓய்வூதியங்கள் இந்திய ஒருங்கிணைந்த நிதியத்திலிருந்து பெறப்படும் 'செலவினமாக' (charged) வைக்கப்பட்டு வாக்களிக்கப்பட முடியாதவை.",
        "reason_en": "Unlike the Supreme Court and CAG whose expenses are charged upon the Consolidated Fund of India, ECI's administrative expenditure is voted by Parliament.",
        "reason_ta": "இந்திய ஒருங்கிணைந்த நிதியிலிருந்து செலவிடப்படும் உச்ச நீதிமன்றம் மற்றும் CAG போலல்லாமல், ECI-ன் நிர்வாகச் செலவுகள் பாராளுமன்றத்தின் வாக்கெடுப்பிற்கு உட்பட்டவை.",
        "correct_answer": "D",
        "difficulty": "Hard",
        "bloom_level": "Evaluate",
        "exp_en": "Assertion (A) is false: ECI expenses are NOT charged upon the Consolidated Fund of India; they are subject to parliamentary vote. Reason (R) is true and highlights a major institutional difference between ECI and SC/CAG.",
        "exp_ta": "கூற்று (A) தவறு: தேர்தல் ஆணையத்தின் செலவுகள் இந்திய ஒருங்கிணைந்த நிதியில் 'செலவிடப்பட்டவை' (charged) அல்ல; அவை பாராளுமன்ற வாக்கெடுப்புக்கு உட்பட்டவை. காரணம் (R) சரி.",
        "tnpsc_tip_en": "Frequent TNPSC trap! Many students wrongly assume ECI's budget is 'charged' like SC and CAG. It is a parliamentary grant subject to vote.",
        "tnpsc_tip_ta": "அடிக்கடி கேட்கப்படும் TNPSC பொறி! ECI நிதி SC/CAG போன்று 'charged' அல்ல, பாராளுமன்றத்தால் வாக்களிக்கப்படும் மானியமாகும்.",
        "revision_fact_en": "Article 112(3) lists charged expenditure upon the CFI, which includes SC Judges and CAG, but conspicuously omits the Election Commission.",
        "revision_fact_ta": "சரத்து 112(3) ஒருங்கிணைந்த நிதியில் செலவிடப்படும் இனங்களைப் பட்டியலிடுகிறது, அதில் உச்ச நீதிமன்றம் மற்றும் CAG உள்ளது, ஆனால் தேர்தல் ஆணையம் சேர்க்கப்படவில்லை.",
        "tags": ["Consolidated Fund", "ECI Finances", "Charged Expenditure"]
    },
    # 9 - A
    {
        "id": "EC_R_009",
        "assertion_en": "In Lily Thomas v. Union of India (2013), the Supreme Court struck down Section 8(4) of the Representation of the People Act, 1951 as unconstitutional.",
        "assertion_ta": "லில்லி தாமஸ் எதிர் இந்திய ஒன்றியம் (2013) வழக்கில், 1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 8(4)-ஐ அரசியலமைப்பிற்கு முரணானது என உச்ச நீதிமன்றம் ரத்து செய்தது.",
        "reason_en": "Section 8(4) created an unconstitutional discrimination by granting an automatic 3-month protection against disqualification exclusively to sitting MPs and MLAs who filed an appeal.",
        "reason_ta": "பிரிவு 8(4) மேல்முறையீடு செய்த தற்போதைய எம்.பி மற்றும் எம்.எல்.ஏ-க்களுக்கு மட்டும் தகுதி நீக்கத்திலிருந்து 3 மாத கால தானியங்கி பாதுகாப்பை வழங்கி அரசியலமைப்புக்கு முரணான பாகுபாட்டை உருவாக்கியது.",
        "correct_answer": "A",
        "difficulty": "Medium",
        "bloom_level": "Analyze",
        "exp_en": "Both (A) and (R) are correct, and (R) provides the exact constitutional rationale: Parliament had no power under Articles 102(1)(e) and 191(1)(e) to treat sitting legislators differently from aspiring candidates.",
        "exp_ta": "இரண்டும் சரியானவை. சரத்துகள் 102(1)(e) மற்றும் 191(1)(e)-ன் கீழ் புதிய வேட்பாளர்களுக்கும் தற்போதைய உறுப்பினர்களுக்கும் இடையே பாகுபாடு காட்ட பாராளுமன்றத்திற்கு அதிகாரம் இல்லை என்பதே ரத்துக்கான காரணமாகும்.",
        "tnpsc_tip_en": "Following Lily Thomas (2013), conviction of 2 or more years under specified offences results in immediate disqualification.",
        "tnpsc_tip_ta": "லில்லி தாமஸ் தீர்ப்பைத் தொடர்ந்து, 2 ஆண்டுகள் அல்லது அதற்கு மேற்பட்ட சிறைத் தண்டனை விதிக்கப்பட்டால் உடனடியாக பதவி பறிபோகும்.",
        "revision_fact_en": "In Lok Prahari (2018), SC clarified that if the appellate court stays the conviction (not just sentence), disqualification ceases to operate.",
        "revision_fact_ta": "லோக் பிரஹாரி (2018) வழக்கில் தண்டனைக்கு (தண்டனை நிறுத்தம் மட்டுமல்லாமல்) மேல்முறையீட்டு நீதிமன்றம் தடை விதித்தால் தகுதிநீக்கம் செயல்படாது என தெளிவுபடுத்தப்பட்டது.",
        "tags": ["Lily Thomas Case", "Section 8(4)", "Criminalization of Politics"]
    },
    # 10 - B
    {
        "id": "EC_R_010",
        "assertion_en": "The Election Commission mandated 100% deployment of Voter Verifiable Paper Audit Trail (VVPAT) units along with EVMs in the 2019 Lok Sabha elections.",
        "assertion_ta": "2019 மக்களவைத் தேர்தலில் வாக்குப்பதிவு இயந்திரங்களுடன் (EVM) 100% விவிபேட் (VVPAT) அலகுகளைப் பயன்படுத்துவதை தேர்தல் ஆணையம் கட்டாயமாக்கியது.",
        "reason_en": "VVPAT slips are printed on specialized thermal paper and remain visible behind a transparent window to the voter for exactly 7 seconds.",
        "reason_ta": "விவிபேட் சீட்டுகள் சிறப்பு வெப்பத் தாளில் அச்சிடப்பட்டு, வாக்காளருக்கு வெளிப்படையான சாளரத்தின் பின்னால் சரியாக 7 வினாடிகள் தெரியும் வகையில் வைக்கப்படுகின்றன.",
        "correct_answer": "B",
        "difficulty": "Easy",
        "bloom_level": "Understand",
        "exp_en": "Both (A) and (R) are accurate factual statements regarding VVPAT specifications, but the 7-second slip display feature is a technical detail, not the reason why ECI deployed them 100% across the nation.",
        "exp_ta": "இரண்டு கூற்றுகளும் உண்மையானவை; ஆனால் 7 வினாடிகள் பார்வைக்கு தெரிவது என்பது தொழில்நுட்ப சிறப்பம்சமே தவிர, நாடு முழுவதும் 100% கட்டாயமாக்கப்பட்டதற்கான முழு விளக்கம் அல்ல.",
        "tnpsc_tip_en": "Supreme Court directed verification of VVPAT slips in 5 randomly selected polling stations per Assembly segment/constituency.",
        "tnpsc_tip_ta": "ஒரு சட்டமன்றத் தொகுதிக்கு தலா 5 வாக்குச்சாவடிகளில் விவிபேட் சீட்டுகளை எண்ணி சரிபார்க்க உச்ச நீதிமன்றம் உத்தரவிட்டது.",
        "revision_fact_en": "VVPAT was first used experimentally in the Noksen constituency of Nagaland in September 2013.",
        "revision_fact_ta": "2013 செப்டம்பரில் நாகாலாந்தின் நோக்சென் சட்டமன்றத் தொகுதி இடைத்தேர்தலில் முதன்முதலில் விவிபேட் பயன்படுத்தப்பட்டது.",
        "tags": ["VVPAT", "EVM", "2019 Elections"]
    },
    # 11 - C
    {
        "id": "EC_R_011",
        "assertion_en": "The Chief Election Commissioner and other Election Commissioners (Appointment, Conditions of Service and Term of Office) Act, 2023 established a statutory Selection Committee.",
        "assertion_ta": "தலைமைத் தேர்தல் ஆணையர் மற்றும் பிற தேர்தல் ஆணையர்கள் (நியமனம் மற்றும் பணிகள்) சட்டம் 2023 ஒரு சட்டப்பூர்வ தேர்வுக் குழுவை நிறுவியது.",
        "reason_en": "The Selection Committee established under the 2023 Act is chaired by the Chief Justice of India and includes the Prime Minister and Leader of the Opposition.",
        "reason_ta": "2023 சட்டத்தின் கீழ் அமைக்கப்பட்ட தேர்வுக் குழுவிற்கு தலைமை நீதிபதி தலைமை தாங்குவதோடு, பிரதமர் மற்றும் எதிர்க்கட்சித் தலைவரையும் உள்ளடக்கியுள்ளது.",
        "correct_answer": "C",
        "difficulty": "Hard",
        "bloom_level": "Analyze",
        "exp_en": "Assertion (A) is true: The 2023 Act established a statutory selection panel. Reason (R) is false: The Selection Committee consists of PM (Chair), Leader of Opposition/largest opposition party, and a Union Cabinet Minister nominated by the PM (CJI is NOT on the committee).",
        "exp_ta": "கூற்று (A) சரி: 2023 சட்டம் ஒரு தேர்வுக் குழுவை அமைத்தது. காரணம் (R) தவறு: இக்குழுவில் தலைமை நீதிபதி இல்லை; பிரதமர், எதிர்க்கட்சித் தலைவர் மற்றும் பிரதமரால் நியமிக்கப்படும் மத்திய கேபினட் அமைச்சர் மட்டுமே உள்ளனர்.",
        "tnpsc_tip_en": "Anoop Baranwal (March 2023) placed CJI on the committee until Parliament legislated; Parliament passed the 2023 Act replacing CJI with a Cabinet Minister.",
        "tnpsc_tip_ta": "அனூப் பரன்வால் வழக்கில் உச்ச நீதிமன்றம் தலைமை நீதிபதியை குழுவில் வைத்தது; பின்னர் இயற்றப்பட்ட 2023 சட்டம் தலைமை நீதிபதிக்கு பதிலாக கேபினட் அமைச்சரை சேர்த்தது.",
        "revision_fact_en": "Under the 2023 Act, a Search Committee headed by the Union Minister of Law prepares a panel of 5 persons for the Selection Committee.",
        "revision_fact_ta": "2023 சட்டத்தின் கீழ் சட்ட அமைச்சர் தலைமையிலான தேடுதல் குழு 5 பேர் கொண்ட பட்டியலை தயாரித்து தேர்வுக் குழுவிடம் அளிக்கிறது.",
        "tags": ["2023 EC Act", "Selection Committee", "Anoop Baranwal"]
    },
    # 12 - D
    {
        "id": "EC_R_012",
        "assertion_en": "A citizen of India owning residential properties in two different states is legally entitled to register as a voter in both constituencies.",
        "assertion_ta": "இரண்டு வெவ்வேறு மாநிலங்களில் குடியிருப்புச் சொத்துக்களை வைத்துள்ள ஒரு இந்தியக் குடிமகன் இரண்டு தொகுதிகளிலும் வாக்காளராகப் பதிவு செய்ய சட்டப்படி தகுதியுடையவர்.",
        "reason_en": "Sections 17 and 18 of the Representation of the People Act, 1950 strictly prohibit registration of an individual in more than one constituency or more than once in the same constituency.",
        "reason_ta": "1950 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவுகள் 17 மற்றும் 18 ஒரு நபர் ஒன்றுக்கு மேற்பட்ட தொகுதிகளிலோ அல்லது ஒரே தொகுதியில் ஒன்றுக்கு மேற்பட்ட முறையோ பதிவு செய்வதை கண்டிப்பாகத் தடை செய்கின்றன.",
        "correct_answer": "D",
        "difficulty": "Easy",
        "bloom_level": "Understand",
        "exp_en": "Assertion (A) is false: Dual registration is illegal and punishable under Section 31 of RPA 1950. Reason (R) is true and accurately states Sections 17 and 18.",
        "exp_ta": "கூற்று (A) தவறு: இரண்டு இடங்களில் வாக்காளராகப் பதிவு செய்வது சட்டவிரோதமானது மற்றும் தண்டனைக்குரியது. காரணம் (R) சரி: பிரிவுகள் 17 மற்றும் 18 இரட்டைப் பதிவைத் தடை செய்கின்றன.",
        "tnpsc_tip_en": "Voter registration is based on ordinary residence (Section 20 of RPA 1950), not mere property ownership.",
        "tnpsc_tip_ta": "வாக்காளர் பதிவு என்பது வழக்கமான வசிப்பிடத்தை அடிப்படையாகக் கொண்டது (பிரிவு 20), சொத்துடைமை மட்டுமே போதுமானதல்ல.",
        "revision_fact_en": "Section 31 of RPA 1950 provides for imprisonment up to 1 year or fine for making false declarations in connection with electoral rolls.",
        "revision_fact_ta": "வாக்காளர் பட்டியலில் தவறான அறிவிப்புகளைச் செய்வதற்கு 1 ஆண்டு வரை சிறை அல்லது அபராதம் விதிக்க பிரிவு 31 வகை செய்கிறது.",
        "tags": ["RPA 1950", "Voter Registration", "Ordinary Resident"]
    },
    # 13 - A
    {
        "id": "EC_R_013",
        "assertion_en": "The Constitution (61st Amendment) Act, 1988 amended Article 326 to lower the voting age from 21 years to 18 years.",
        "assertion_ta": "61வது அரசியலமைப்புத் திருத்தச் சட்டம் 1988, சரத்து 326-ஐத் திருத்தி வாக்குரிமை வயதை 21-லிருந்து 18 ஆகக் குறைத்தது.",
        "reason_en": "The amendment sought to provide the unrepresented youth of the country an opportunity to participate directly in the political process.",
        "reason_ta": "நாட்டின் இளைஞர்களுக்கு நாட்டின் அரசியல் நடைமுறைகளில் நேரடியாகப் பங்கேற்கும் வாய்ப்பை வழங்குவதற்காகவே இந்தத் திருத்தம் கொண்டுவரப்பட்டது.",
        "correct_answer": "A",
        "difficulty": "Easy",
        "bloom_level": "Understand",
        "exp_en": "Both (A) and (R) are correct, and (R) provides the official Statement of Objects and Reasons behind the 61st Constitutional Amendment.",
        "exp_ta": "இரண்டும் சரியானவை. நாட்டின் இளைஞர்களை ஜனநாயகத்தில் ஈடுபடுத்தவே 61வது திருத்தச் சட்டம் வாக்குரிமை வயதை 18 ஆகக் குறைத்தது.",
        "tnpsc_tip_en": "61st Amendment Act came into force on 28th March 1989 under the Rajiv Gandhi government.",
        "tnpsc_tip_ta": "61வது திருத்தச் சட்டம் மார்ச் 28, 1989 அன்று ராஜீவ் காந்தி அரசால் நடைமுறைக்கு கொண்டுவரப்பட்டது.",
        "revision_fact_en": "Article 326 guarantees adult suffrage without discrimination on grounds of religion, race, caste, or sex.",
        "revision_fact_ta": "சரத்து 326 மதம், இனம், சாதி அல்லது பாலின பாகுபாடின்றி வயதுவந்தோர் வாக்குரிமையை உறுதி செய்கிறது.",
        "tags": ["61st Amendment", "Article 326", "Voting Age"]
    },
    # 14 - B
    {
        "id": "EC_R_014",
        "assertion_en": "The Election Commission of India has the sole authority to specify, reserve, and allot election symbols to recognized political parties.",
        "assertion_ta": "அங்கீகரிக்கப்பட்ட அரசியல் கட்சிகளுக்கு தேர்தல் சின்னங்களை குறிப்பிடவும், ஒதுக்கவும், ஒதுக்குவதற்கும் இந்திய தேர்தல் ஆணையத்திற்கு மட்டுமே முழு அதிகாரம் உள்ளது.",
        "reason_en": "Registration of associations and bodies of citizens as political parties is governed by Section 29A of the Representation of the People Act, 1951.",
        "reason_ta": "குடிமக்களின் சங்கங்கள் மற்றும் அமைப்புகளை அரசியல் கட்சிகளாகப் பதிவு செய்வது 1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 29A-ஆல் நிர்வகிக்கப்படுகிறது.",
        "correct_answer": "B",
        "difficulty": "Medium",
        "bloom_level": "Analyze",
        "exp_en": "Both (A) and (R) are correct statements of electoral law, but (R) concerns party registration under Section 29A, which does not explain the Commission's symbol powers under the Symbols Order 1968.",
        "exp_ta": "இரண்டு கூற்றுகளும் உண்மையானவை. ஆனால் பிரிவு 29A கட்சிப் பதிவு பற்றியது; இது சின்னங்கள் ஒதுக்கீடு முறைக்கான காரணம் அல்ல.",
        "tnpsc_tip_en": "Election Symbols (Reservation and Allotment) Order was promulgated by ECI in 1968 under Article 324 read with Conduct of Elections Rules.",
        "tnpsc_tip_ta": "தேர்தல் சின்னங்கள் ஆணை 1968-ல் சரத்து 324 மற்றும் தேர்தல் நடத்தை விதிகளின் கீழ் ஆணையத்தால் வெளியிடப்பட்டது.",
        "revision_fact_en": "Under the Symbols Order, symbols are classified into 'Reserved' (for recognized parties) and 'Free' (for unrecognized registered parties and independents).",
        "revision_fact_ta": "சின்னங்கள் ஆணையின் கீழ், சின்னங்கள் 'ஒதுக்கப்பட்டவை' மற்றும் 'சுயேச்சை/அங்கீகாரமற்ற கட்சிகளுக்கான இலவச சின்னங்கள்' என வகைப்படுத்தப்பட்டுள்ளன.",
        "tags": ["Election Symbols Order 1968", "Section 29A", "Recognized Parties"]
    },
    # 15 - C
    {
        "id": "EC_R_015",
        "assertion_en": "Orders issued by the Delimitation Commission have the force of law and cannot be questioned in any court of law under Article 329(a).",
        "assertion_ta": "தொகுதி மறுவரையறை ஆணையத்தால் வெளியிடப்படும் ஆணைகள் சட்டத்தின் மதிப்பைப் பெறுகின்றன மற்றும் சரத்து 329(a)-ன் கீழ் எந்த நீதிமன்றத்திலும் கேள்வி கேட்க முடியாது.",
        "reason_en": "The Delimitation Commission is headed ex-officio by the Prime Minister of India and includes all State Chief Ministers as full voting members.",
        "reason_ta": "தொகுதி மறுவரையறை ஆணையத்திற்கு இந்தியப் பிரதமர் பதவிவழித் தலைமை தாங்குவதோடு அனைத்து மாநில முதல்வர்களையும் முழு வாக்குரிமை உறுப்பினர்களாகக் கொண்டுள்ளது.",
        "correct_answer": "C",
        "difficulty": "Medium",
        "bloom_level": "Analyze",
        "exp_en": "Assertion (A) is true: Delimitation orders published in Gazette have force of law and bar judicial review (Art 329(a)). Reason (R) is completely false: Delimitation Commission is chaired by a retired Supreme Court judge, not the Prime Minister.",
        "exp_ta": "கூற்று (A) சரி: அரசிதழில் வெளியிடப்படும் மறுவரையறை ஆணைகள் மீது நீதிமன்ற ஆய்வு தடை செய்யப்பட்டுள்ளது. காரணம் (R) முற்றிலும் தவறு: மறுவரையறை ஆணையத்தின் தலைவர் ஓய்வுபெற்ற உச்ச நீதிமன்ற நீதிபதியே தவிர பிரதமர் அல்ல.",
        "tnpsc_tip_en": "Associate members of the Delimitation Commission (MPs/MLAs) have no right to vote or sign the final report.",
        "tnpsc_tip_ta": "மறுவரையறை ஆணையத்தின் இணை உறுப்பினர்களான எம்.பி/எம்.எல்.ஏ-க்களுக்கு வாக்களிக்கும் உரிமையோ அல்லது இறுதி அறிக்கையில் கையெழுத்திடும் உரிமையோ இல்லை.",
        "revision_fact_en": "Delimitation Commissions were set up 4 times: 1952, 1962, 1972, and 2002.",
        "revision_fact_ta": "தொகுதி மறுவரையறை ஆணையங்கள் இதுவரை 4 முறை அமைக்கப்பட்டுள்ளன: 1952, 1962, 1972, மற்றும் 2002.",
        "tags": ["Delimitation Commission", "Article 329(a)", "Judicial Immunity"]
    },
    # 16 - D
    {
        "id": "EC_R_016",
        "assertion_en": "The State Election Commissioner can be removed from office by the State Governor at his sole discretion without any inquiry.",
        "assertion_ta": "மாநிலத் தேர்தல் ஆணையரை எவ்வித விசாரணையுமின்றி மாநில ஆளுநர் தனது விருப்பப்படி எந்த நேரத்திலும் பதவி நீக்கம் செய்யலாம்.",
        "reason_en": "Article 243K(2) explicitly provides that the State Election Commissioner shall not be removed from office except in like manner and on the like grounds as a Judge of a High Court.",
        "reason_ta": "சரத்து 243K(2), உயர் நீதிமன்ற நீதிபதியை பதவி நீக்கம் செய்யும் அதே முறை மற்றும் காரணங்களின்றி மாநில தேர்தல் ஆணையரை நீக்க முடியாது என்று தெளிவாகக் கூறுகிறது.",
        "correct_answer": "D",
        "difficulty": "Medium",
        "bloom_level": "Evaluate",
        "exp_en": "Assertion (A) is false: SEC enjoys High Court judge level tenure protection and cannot be removed at the Governor's pleasure. Reason (R) is true and accurately quotes Article 243K(2).",
        "exp_ta": "கூற்று (A) தவறு: மாநில தேர்தல் ஆணையரை ஆளுநர் தன்னிச்சையாக நீக்க முடியாது. காரணம் (R) சரி: உயர் நீதிமன்ற நீதிபதிக்கு இணையான பதவிப் பாதுகாப்பை சரத்து 243K(2) வழங்குகிறது.",
        "tnpsc_tip_en": "Remember: Governor appoints the State Election Commissioner, but removal can only be done by the President via Parliamentary impeachment process!",
        "tnpsc_tip_ta": "நினைவில் கொள்க: மாநில தேர்தல் ஆணையரை ஆளுநர் நியமிக்கிறார்; ஆனால் நீக்கம் செய்யும் அதிகாரம் பாராளுமன்ற தீர்மானத்தின் பேரில் குடியரசுத் தலைவருக்கே உண்டு!",
        "revision_fact_en": "In Rameshwar Prasad v. State of Bihar, SC reaffirmed independence of constitutional functionaries including election authorities.",
        "revision_fact_ta": "அரசியலமைப்புப் பதவி வகிக்கும் அதிகாரிகளின் சுதந்திரத்தைப் பாதுகாப்பதை உச்ச நீதிமன்ற தீர்ப்புகள் உறுதிப்படுத்தியுள்ளன.",
        "tags": ["State Election Commissioner", "Article 243K", "Removal Procedure"]
    },
    # 17 - A
    {
        "id": "EC_R_017",
        "assertion_en": "The open ballot system was introduced for elections to the Council of States (Rajya Sabha) by amending the Representation of the People Act in 2003.",
        "assertion_ta": "2003-ல் மக்கள் பிரதிநிதித்துவச் சட்டத்தைத் திருத்துவதன் மூலம் மாநிலங்களவைத் தேர்தலுக்கு திறந்த வாக்குச் சீட்டு முறை (open ballot) அறிமுகப்படுத்தப்பட்டது.",
        "reason_en": "Open ballot was introduced to curb corrupt practices and prevent cross-voting by MLAs acting against their party whip in exchange for monetary inducements.",
        "reason_ta": "பண பலத்தால் எம்.எல்.ஏ-க்கள் கட்சிக்கு எதிராக மாற்று வாக்களிப்பதைத் தடுக்கவும், ஊழல் நடவடிக்கைகளைக் கட்டுப்படுத்தவுமே திறந்த வாக்கு முறை கொண்டுவரப்பட்டது.",
        "correct_answer": "A",
        "difficulty": "Hard",
        "bloom_level": "Analyze",
        "exp_en": "Both (A) and (R) are correct, and (R) directly explains the intent of the 2003 amendment which was upheld by the Supreme Court in Kuldip Nayar v. Union of India (2006).",
        "exp_ta": "இரண்டும் சரியானவை. 2003 திருத்தம் குதிரை பேரம் மற்றும் மாற்று வாக்களிப்பைத் தடுக்கவே கொண்டுவரப்பட்டது; இதை 2006 குல்தீப் நய்யார் வழக்கில் உச்ச நீதிமன்றம் உறுதி செய்தது.",
        "tnpsc_tip_en": "Secrecy of ballot is not an absolute right; it is a means to ensure free and fair elections, which can be modified by Parliament.",
        "tnpsc_tip_ta": "வாக்கு ரகசியம் என்பது மாற்ற முடியாத அடிப்படை உரிமை அல்ல, சுதந்திரமான தேர்தலை உறுதி செய்வதற்கான வழிமுறையே என்று உச்ச நீதிமன்றம் கூறியது.",
        "revision_fact_en": "The 2003 amendment also removed the residential domicile requirement for candidates contesting Rajya Sabha elections from a particular state.",
        "revision_fact_ta": "2003 திருத்தம் ஒரு குறிப்பிட்ட மாநிலத்திலிருந்து மாநிலங்களவைக்கு போட்டியிட அந்த மாநிலத்திலேயே வசிக்க வேண்டும் என்ற விதியையும் நீக்கியது.",
        "tags": ["Rajya Sabha Elections", "Open Ballot", "Kuldip Nayar Case"]
    },
    # 18 - B
    {
        "id": "EC_R_018",
        "assertion_en": "Under Article 324(6), the President or the Governor of a State is bound to make available to the Election Commission staff necessary for discharge of its functions.",
        "assertion_ta": "சரத்து 324(6)-ன் கீழ், தேர்தல் ஆணையத்தின் பணிகளைச் செய்வதற்குத் தேவையான பணியாளர்களை குடியரசுத் தலைவர் அல்லது மாநில ஆளுநர் வழங்குவது கட்டாயமாகும்.",
        "reason_en": "Officers and staff deployed on election duty are legally deemed to be on deputation to the Election Commission of India and subject to its disciplinary control.",
        "reason_ta": "தேர்தல் பணியில் ஈடுபடுத்தப்படும் அதிகாரிகள் மற்றும் பணியாளர்கள் சட்டப்படி தேர்தல் ஆணையத்தின் பணி அயல்விருப்பில் (deputation) இருப்பதாகக் கருதப்பட்டு அதன் ஒழுங்கு நடவடிக்கைக் கட்டுப்பாட்டிற்கு உட்பட்டவர்கள்.",
        "correct_answer": "B",
        "difficulty": "Medium",
        "bloom_level": "Understand",
        "exp_en": "Both (A) and (R) are true statements under Art 324(6) and Section 28A/13CC of RPA. However, (R) details their disciplinary status during deployment rather than explaining why the constitutional obligation exists under (A).",
        "exp_ta": "இரண்டு கூற்றுகளும் சரியானவை. ஆனால் (R) தேர்தல் பணியாளர்களின் கட்டுப்பாட்டு விதியைக் கூறுகிறது, இது ஆளுநர்/குடியரசுத் தலைவர் பணியாளர்களை வழங்க வேண்டிய கட்டாயத்திற்கான காரணம் அல்ல.",
        "tnpsc_tip_en": "During elections, District Magistrates act as District Election Officers (DEOs) and report directly to the Chief Electoral Officer (CEO) and ECI.",
        "tnpsc_tip_ta": "தேர்தலின் போது மாவட்ட ஆட்சியர்கள் மாவட்ட தேர்தல் அதிகாரிகளாக (DEO) செயல்பட்டு நேரடியாக ECI-ன் கட்டுப்பாட்டில் இயங்குகின்றனர்.",
        "revision_fact_en": "Sections 28A and 13CC of RPA 1951 provide statutory deemed deputation to polling and returning staff under ECI.",
        "revision_fact_ta": "1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவுகள் 28A மற்றும் 13CC தேர்தல் பணியாளர்களை ஆணையத்தின் நேரடி கண்காணிப்பில் வைக்கின்றன.",
        "tags": ["Article 324(6)", "Deputation to ECI", "Returning Officers"]
    },
    # 19 - C
    {
        "id": "EC_R_019",
        "assertion_en": "Section 123 of the Representation of the People Act, 1951 defines corrupt practices including bribery, undue influence, and promotion of enmity on grounds of religion or caste.",
        "assertion_ta": "1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 123 கையூட்டு, தகாத செல்வாக்கு, மற்றும் மதம் அல்லது சாதியின் பெயரால் பகையை வளர்ப்பது போன்ற ஊழல் நடைமுறைகளை வரையறுக்கிறது.",
        "reason_en": "Allegations of corrupt practices are summarily investigated and adjudicated by the Returning Officer on the day of counting.",
        "reason_ta": "ஊழல் நடைமுறைகள் குறித்த குற்றச்சாட்டுகள் வாக்கு எண்ணிக்கையன்றே தேர்தல் நடத்தும் அதிகாரியால் சுருக்கமாக விசாரிக்கப்பட்டு தீர்ப்பளிக்கப்படுகின்றன.",
        "correct_answer": "C",
        "difficulty": "Hard",
        "bloom_level": "Analyze",
        "exp_en": "Assertion (A) is true: Section 123 details corrupt electoral practices. Reason (R) is false: Returning Officers have no judicial power to adjudicate corrupt practices; only High Courts can try them in an election petition under Section 80A.",
        "exp_ta": "கூற்று (A) சரி: பிரிவு 123 ஊழல் நடைமுறைகளை வரையறுக்கிறது. காரணம் (R) தவறு: தேர்தல் நடத்தும் அதிகாரிக்கு ஊழல் நடைமுறைகளை விசாரித்து தீர்ப்பளிக்கும் அதிகாரம் இல்லை; உயர் நீதிமன்றமே தேர்தல் மனு மூலம் விசாரிக்க முடியும்.",
        "tnpsc_tip_en": "If a High Court finds a candidate guilty of a corrupt practice, the President decides the disqualification period (up to 6 years) upon ECI advice (Section 8A).",
        "tnpsc_tip_ta": "ஊழல் நடைமுறையில் ஈடுபட்டதாக உயர்நீதிமன்றம் தீர்ப்பளித்தால், ECI ஆலோசனையின்படி குடியரசுத் தலைவர் 6 ஆண்டுகள் வரை தகுதி நீக்கம் செய்யலாம்.",
        "revision_fact_en": "In Abhiram Singh v. C.D. Commachen (2017), SC held that appeals to religion, race, caste, or community by any candidate or agent corrupt the electoral process.",
        "revision_fact_ta": "2017 அபிராம் சிங் வழக்கில் மத, சாதி ரீதியான வாக்கு சேகரிப்பு முற்றிலும் சட்டவிரோத ஊழல் நடைமுறை என உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
        "tags": ["Section 123", "Corrupt Practices", "RPA 1951"]
    },
    # 20 - D
    {
        "id": "EC_R_020",
        "assertion_en": "The Constitution of India explicitly fixes a term of six years or up to 65 years of age for Election Commissioners and prescribes qualifications in administrative law.",
        "assertion_ta": "இந்திய அரசியலமைப்பு தேர்தல் ஆணையர்களுக்கு ஆறு ஆண்டுகள் அல்லது 65 வயது வரை பதவிக்காலத்தை வெளிப்படையாக நிர்ணயித்துள்ளதுடன் நிர்வாகச் சட்டத்தில் தகுதிகளையும் வகுத்துள்ளது.",
        "reason_en": "The Constitution does not specify the tenure, eligibility qualifications, or debarment from post-retirement government employment for Election Commissioners.",
        "reason_ta": "அரசியலமைப்பு தேர்தல் ஆணையர்களின் பதவிக்காலம், கல்வித் தகுதிகள் அல்லது ஓய்வுக்குப் பின் அரசுப் பணிகளில் ஈடுபடுவதற்கான தடையை வெளிப்படையாகக் குறிப்பிடவில்லை.",
        "correct_answer": "D",
        "difficulty": "Hard",
        "bloom_level": "Evaluate",
        "exp_en": "Assertion (A) is false: The Constitution is silent on tenure and qualifications; these are governed by parliamentary statutes (1993 and 2023 Acts). Reason (R) is true and represents a notable constitutional flaw.",
        "exp_ta": "கூற்று (A) தவறு: அரசியலமைப்பு பதவிக்காலத்தையோ தகுதிகளையோ குறிப்பிடவில்லை; இவை பாராளுமன்ற சட்டங்களால் நிர்வகிக்கப்படுகின்றன. காரணம் (R) சரி.",
        "tnpsc_tip_en": "High-yield Polity trap: Constitution does NOT prescribe qualifications for ECs, nor does it bar them from further government appointments.",
        "tnpsc_tip_ta": "முக்கியமான TNPSC பொறி: அரசியலமைப்பு தேர்தல் ஆணையர்களுக்கான தகுதிகளைக் கூறவில்லை, ஓய்வுக்குப் பின் அரசுப் பதவிகளை ஏற்கவும் தடை விதிக்கவில்லை.",
        "revision_fact_en": "Article 324(2) leaves the strength and appointment conditions of the Commission to be determined by the President, subject to law made by Parliament.",
        "revision_fact_ta": "சரத்து 324(2) தேர்தல் ஆணையத்தின் எண்ணிக்கை மற்றும் பணிக்கால நிபந்தனைகளை பாராளுமன்ற சட்டத்திற்கு உட்பட்டு குடியரசுத் தலைவரின் முடிவுக்கு விட்டுவிடுகிறது.",
        "tags": ["Constitutional Omissions", "EC Qualifications", "Article 324(2)"]
    },
    # 21 - A
    {
        "id": "EC_R_021",
        "assertion_en": "In Mohinder Singh Gill v. Chief Election Commissioner (1978), the Supreme Court ruled that Article 324 operates as a plenary reservoir of power for the Election Commission.",
        "assertion_ta": "மோஹிந்தர் சிங் கில் எதிர் தலைமைத் தேர்தல் ஆணையர் (1978) வழக்கில், சரத்து 324 தேர்தல் ஆணையத்திற்கு முழுமையான அதிகாரங்களின் களஞ்சியமாகச் செயல்படுகிறது என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
        "reason_en": "Where enacted statutory laws and rules are silent or insufficient, the Election Commission possesses inherent constitutional executive power to ensure free and fair elections.",
        "reason_ta": "இயற்றப்பட்ட சட்டங்களும் விதிகளும் மௌனம் சாதிக்கும் அல்லது போதுமானதாக இல்லாத சூழல்களில், சுதந்திரமான மற்றும் நியாயமான தேர்தலை உறுதி செய்ய தேர்தல் ஆணையத்திற்கு உள்ளார்ந்த நிர்வாக அதிகாரம் உள்ளது.",
        "correct_answer": "A",
        "difficulty": "Hard",
        "bloom_level": "Analyze",
        "exp_en": "Both (A) and (R) are correct, and (R) accurately captures the doctrine of residual plenary power enunciated by Justice Krishna Iyer in the Mohinder Singh Gill landmark judgment.",
        "exp_ta": "இரண்டும் சரியானவை. சட்டம் இல்லாத இடங்களில் நியாயமான தேர்தலை நடத்த சரத்து 324-ன் கீழ் ஆணையத்திற்கு தன்னிச்சையான அதிகாரங்கள் உண்டு என்று நீதிபதி கிருஷ்ண ஐயர் தீர்ப்பளித்தார்.",
        "tnpsc_tip_en": "Plenary power under Article 324 cannot override or violate an enacted statute; it only supplements statutory gaps.",
        "tnpsc_tip_ta": "சரத்து 324-ன் கீழ் உள்ள முழு அதிகாரம் பாராளுமன்ற சட்டத்திற்கு முரணாக இருக்க முடியாது; சட்டத்தில் உள்ள இடைவெளிகளை நிரப்ப மட்டுமே பயன்படும்.",
        "revision_fact_en": "Mohinder Singh Gill arose when ECI ordered a repoll for the entire Ferozepur parliamentary constituency due to booth capturing and destruction of ballot papers.",
        "revision_fact_ta": "வாக்குச்சாவடி கைப்பற்றப்பட்டதால் பெரோஸ்பூர் தொகுதி முழுமைக்கும் மறுதேர்தல் நடத்த ECI உத்தரவிட்டபோது இத்தீர்ப்பு வழங்கப்பட்டது.",
        "tags": ["Mohinder Singh Gill Case", "Article 324", "Plenary Powers"]
    },
    # 22 - B
    {
        "id": "EC_R_022",
        "assertion_en": "Non-Resident Indians (NRIs) who have not acquired citizenship of any other country are eligible to be registered as overseas electors under Section 20A of RPA 1950.",
        "assertion_ta": "பிற நாட்டின் குடியுரிமையைப் பெறாத வெளிநாடு வாழ் இந்தியர்கள் (NRI) 1950 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 20A-ன் கீழ் வெளிநாட்டு வாக்காளர்களாகப் பதிவு செய்யத் தகுதியுடையவர்கள்.",
        "reason_en": "The Supreme Court of India in Anukul Chandra Pradhan v. Union of India held that the right to vote is a statutory right subject to legislative limitations, not a fundamental right.",
        "reason_ta": "வாக்களிக்கும் உரிமை என்பது ஒரு சட்டப்பூர்வ உரிமையே தவிர அடிப்படை உரிமை அல்ல என்றும், அது சட்ட வரம்புகளுக்கு உட்பட்டது என்றும் அனுகுல் சந்திர பிரதான் வழக்கில் உச்ச நீதிமன்றம் கூறியது.",
        "correct_answer": "B",
        "difficulty": "Medium",
        "bloom_level": "Understand",
        "exp_en": "Both (A) and (R) are legally accurate principles of Indian electoral law, but the nature of voting as a statutory right does not explain the specific registration mechanism of Section 20A.",
        "exp_ta": "இரண்டு கூற்றுகளும் சரியான சட்டக் கோட்பாடுகள்; ஆனால் வாக்களிக்கும் உரிமை சட்டப்பூர்வமானது என்பது வெளிநாடு வாழ் இந்தியர் பதிவு முறைக்கான விளக்கம் அல்ல.",
        "tnpsc_tip_en": "Overseas electors currently must vote in person at their registered polling station in India; proxy voting for NRIs has not been enacted into law.",
        "tnpsc_tip_ta": "வெளிநாடு வாழ் இந்தியர்கள் தற்போது இந்தியாவில் உள்ள தங்களின் வாக்குச்சாவடிக்கு நேரில் வந்தே வாக்களிக்க வேண்டும்; பதிலாள் வாக்கு முறை இன்னும் சட்டமாக்கப்படவில்லை.",
        "revision_fact_en": "Section 20A was inserted by the Representation of the People (Amendment) Act, 2010 to enfranchise non-resident citizens.",
        "revision_fact_ta": "2010 மக்கள் பிரதிநிதித்துவத் திருத்தச் சட்டத்தின் மூலம் வெளிநாடு வாழ் இந்தியர்களுக்கு வாக்களிக்கும் உரிமை வழங்க பிரிவு 20A சேர்க்கப்பட்டது.",
        "tags": ["NRI Voting", "Section 20A", "Right to Vote"]
    },
    # 23 - C
    {
        "id": "EC_R_023",
        "assertion_en": "The Election Commission cannot review or revoke the registration of a political party for ordinary violations of internal rules or electoral code.",
        "assertion_ta": "உட்புற விதிகளையோ அல்லது தேர்தல் நடத்தை விதிகளையோ மீறியதற்காக ஒரு அரசியல் கட்சியின் பதிவை தேர்தல் ஆணையம் தன்னிச்சையாக ரத்து செய்ய முடியாது.",
        "reason_en": "Section 29A of the Representation of the People Act, 1951 explicitly confers unfettered administrative discretion upon the Commission to deregister any party at will.",
        "reason_ta": "1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 29A, எந்தவொரு கட்சியையும் தனது விருப்பப்படி ரத்து செய்வதற்கு கட்டுப்பாடற்ற நிர்வாக அதிகாரத்தை தேர்தல் ஆணையத்திற்கு வெளிப்படையாக வழங்குகிறது.",
        "correct_answer": "C",
        "difficulty": "Hard",
        "bloom_level": "Analyze",
        "exp_en": "Assertion (A) is true: As held in Indian National Congress v. Institute of Social Welfare (2002), ECI lacks statutory power to deregister parties except in cases of fraud, declared unlawful associations, or constitutional breach. Reason (R) is false: Section 29A contains no deregistration provision.",
        "exp_ta": "கூற்று (A) சரி: மோசடி அல்லது சட்டவிரோத அமைப்பாக அறிவிக்கப்பட்ட வழக்குகளைத் தவிர கட்சிகளை ரத்து செய்யும் அதிகாரம் ஆணையத்திற்கு இல்லை. காரணம் (R) தவறு: பிரிவு 29A ரத்து செய்யும் அதிகாரத்தை வழங்கவில்லை.",
        "tnpsc_tip_en": "ECI has repeatedly requested Parliament to amend RPA 1951 to grant it explicit statutory power to deregister inactive or corrupt political parties.",
        "tnpsc_tip_ta": "செயல்படாத கட்சிகளை ரத்து செய்ய வெளிப்படையான சட்ட அதிகாரம் வழங்குமாறு தேர்தல் ஆணையம் பலமுறை பாராளுமன்றத்திற்கு கோரிக்கை விடுத்துள்ளது.",
        "revision_fact_en": "In Indian National Congress v. Institute of Social Welfare (2002), SC held that ECI's power under Section 29A is quasi-judicial at registration and cannot be reviewed administratively.",
        "revision_fact_ta": "2002 உச்ச நீதிமன்ற தீர்ப்பு ECI-க்கு கட்சிகளை ரத்து செய்யும் பொது அதிகாரம் இல்லை என்பதை தெளிவுபடுத்தியது.",
        "tags": ["Deregistration of Parties", "Section 29A", "Supreme Court Ruling"]
    },
    # 24 - D
    {
        "id": "EC_R_024",
        "assertion_en": "A citizen confined in lawful police custody or undergoing a sentence of imprisonment retains the fundamental right under Article 19(1)(a) to cast their ballot in general elections.",
        "assertion_ta": "காவல்துறை காவலில் உள்ள அல்லது சிறைத் தண்டனை அனுபவிக்கும் ஒரு குடிமகன் பொதுத் தேர்தலில் வாக்களிக்க சரத்து 19(1)(a)-ன் கீழ் அடிப்படை உரிமையைத் தக்க வைத்துக் கொண்டுள்ளார்.",
        "reason_en": "Section 62(5) of the Representation of the People Act, 1951 explicitly bars persons confined in prison or in lawful police custody from voting at any election.",
        "reason_ta": "1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 62(5), சிறையில் அடைக்கப்பட்டுள்ள அல்லது காவல்துறை காவலில் உள்ள நபர்கள் தேர்தலில் வாக்களிப்பதை வெளிப்படையாகத் தடை செய்கிறது.",
        "correct_answer": "D",
        "difficulty": "Medium",
        "bloom_level": "Evaluate",
        "exp_en": "Assertion (A) is false: Voting is not a fundamental right under Art 19(1)(a); prisoners have no right to vote. Reason (R) is true and accurately reproduces the statutory prohibition under Section 62(5).",
        "exp_ta": "கூற்று (A) தவறு: வாக்களிக்கும் உரிமை அடிப்படை உரிமை அல்ல, சிறையில் உள்ளவர்களுக்கு வாக்குரிமை இல்லை. காரணம் (R) சரி: பிரிவு 62(5) கைதிகள் வாக்களிப்பதைத் தடை செய்கிறது.",
        "tnpsc_tip_en": "Exception: Persons subjected to preventive detention under any law are permitted to vote via postal ballot under the proviso to Section 62(5)!",
        "tnpsc_tip_ta": "விதிவிலக்கு: தடுப்புக் காவல் சட்டத்தின் கீழ் அடைக்கப்பட்டுள்ள நபர்கள் தபால் வாக்கு மூலம் வாக்களிக்க பிரிவு 62(5) அனுமதிக்கிறது!",
        "revision_fact_en": "In Anukul Chandra Pradhan (1997), SC upheld the constitutional validity of Section 62(5), rejecting the plea that it violated Article 14.",
        "revision_fact_ta": "1997-ல் அனுகுல் சந்திர பிரதான் வழக்கில் பிரிவு 62(5)-ன் செல்லுபடியாகும் தன்மையை உச்ச நீதிமன்றம் உறுதி செய்தது.",
        "tags": ["Prisoners Voting Rights", "Section 62(5)", "Postal Ballot"]
    },
    # 25 - A
    {
        "id": "EC_R_025",
        "assertion_en": "In Sadiq Ali v. Election Commission of India (1972), the Supreme Court upheld the 'test of numerical majority' applied by the Commission in resolving party symbol disputes.",
        "assertion_ta": "சாதிக் அலி எதிர் இந்திய தேர்தல் ஆணையம் (1972) வழக்கில், கட்சிச் சின்ன தகராறுகளைத் தீர்ப்பதில் தேர்தல் ஆணையம் பயன்படுத்திய 'எண்ணிக்கை பெரும்பான்மை சோதனையை' உச்ச நீதிமன்றம் உறுதி செய்தது.",
        "reason_en": "Evaluating support among both the legislative wing (MPs/MLAs) and the organizational wing represents the most objective and democratic criterion for deciding which faction constitutes the party.",
        "reason_ta": "சட்டமன்றப் பிரிவு (எம்.பி/எம்.எல்.ஏக்கள்) மற்றும் அமைப்பின் பொதுக்குழு உறுப்பினர்களின் ஆதரவை மதிப்பீடு செய்வதே எந்தப் பிரிவு உண்மையான கட்சி என்பதைத் தீர்மானிக்கும் மிகவும் புறநிலை மற்றும் ஜனநாயக அளவுகோலாகும்.",
        "correct_answer": "A",
        "difficulty": "Hard",
        "bloom_level": "Analyze",
        "exp_en": "Both (A) and (R) are correct, and (R) provides the constitutional and democratic justification affirmed by the Supreme Court in the 1972 Sadiq Ali judgment under Paragraph 15 of the Symbols Order.",
        "exp_ta": "இரண்டும் சரியானவை. சட்டமன்ற மற்றும் கட்சி அமைப்பில் பெரும்பான்மை ஆதரவைப் பெற்ற பிரிவே உண்மையான கட்சி என அங்கீகரிப்பது ஜனநாயக நடைமுறைக்கு உகந்தது என நீதிமன்றம் தீர்ப்பளித்தது.",
        "tnpsc_tip_en": "Paragraph 15 of the Symbols Order empowers ECI to decide disputes between splinter groups or rival factions of a recognized political party.",
        "tnpsc_tip_ta": "சின்னங்கள் ஆணையின் பத்தி 15, பிளவுபட்ட அல்லது எதிரெதிர் பிரிவுகளுக்கு இடையேயான சின்னத் தகராறுகளைத் தீர்க்க ECI-க்கு அதிகாரம் அளிக்கிறது.",
        "revision_fact_en": "The Sadiq Ali precedent was recently applied by ECI in resolving the Shiv Sena and Nationalist Congress Party (NCP) disputes in 2023-2024.",
        "revision_fact_ta": "2023-2024 இல் சிவசேனா மற்றும் தேசியவாத காங்கிரஸ் கட்சி தகராறுகளைத் தீர்க்க இந்த சாதிக் அலி வழிகாட்டுதலே பயன்படுத்தப்பட்டது.",
        "tags": ["Sadiq Ali Case", "Symbols Order Para 15", "Party Splits"]
    }
]

def build_questions():
    questions = []
    for item in RAW_REASONING:
        qid = item["id"]
        q_en = (
            f"Given below are two statements, one is labelled as Assertion (A) and the other as Reason (R):\n"
            f"Assertion (A): {item['assertion_en']}\n"
            f"Reason (R): {item['reason_en']}\n"
            f"Select the correct answer using the codes given below:"
        )
        q_ta = (
            f"கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன. ஒன்று கூற்று (A) என்றும், மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\n"
            f"கூற்று (A): {item['assertion_ta']}\n"
            f"காரணம் (R): {item['reason_ta']}\n"
            f"கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:"
        )

        corr = item["correct_answer"]
        whys = {}
        for opt_id in ["A", "B", "C", "D"]:
            if opt_id == corr:
                whys[opt_id] = {
                    "en": f"Correct. {item['exp_en']}",
                    "ta": f"சரியான விடை. {item['exp_ta']}"
                }
            else:
                whys[opt_id] = {
                    "en": f"Incorrect. Under electoral jurisprudence, option {corr} accurately describes the relationship between Assertion and Reason.",
                    "ta": f"தவறான தேர்வு. அரசியலமைப்பு தேர்தல் விதிகளின்படி, விருப்பம் {corr} மட்டுமே கூற்று மற்றும் காரணத்திற்கான சரியான தொடர்பைக் குறிக்கிறது."
                }

        q = make_ec_q(
            qid=qid,
            diff=item["difficulty"],
            qtype="Assertion-Reason",
            subtopic="Constitutional Framework",
            en_stem=q_en,
            ta_stem=q_ta,
            en_a=OPT_TEMPLATES["A"]["en"],
            ta_a=OPT_TEMPLATES["A"]["ta"],
            en_b=OPT_TEMPLATES["B"]["en"],
            ta_b=OPT_TEMPLATES["B"]["ta"],
            en_c=OPT_TEMPLATES["C"]["en"],
            ta_c=OPT_TEMPLATES["C"]["ta"],
            en_d=OPT_TEMPLATES["D"]["en"],
            ta_d=OPT_TEMPLATES["D"]["ta"],
            correct_key=corr,
            exp_en=item["exp_en"],
            exp_ta=item["exp_ta"],
            why_a_en=whys["A"]["en"],
            why_a_ta=whys["A"]["ta"],
            why_b_en=whys["B"]["en"],
            why_b_ta=whys["B"]["ta"],
            why_c_en=whys["C"]["en"],
            why_c_ta=whys["C"]["ta"],
            why_d_en=whys["D"]["en"],
            why_d_ta=whys["D"]["ta"],
            tip_en=item["tnpsc_tip_en"],
            tip_ta=item["tnpsc_tip_ta"],
            fact_en=item["revision_fact_en"],
            fact_ta=item["revision_fact_ta"],
            tags=item["tags"]
        )
        questions.append(q)

    # Save to primary path
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print(f"[SUCCESS] Wrote 25 Reasoning MCQs to {OUTPUT_PATH}")

    # Also save to alias path
    with open(ALIAS_PATH, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print(f"[SUCCESS] Wrote alias to {ALIAS_PATH}")

if __name__ == "__main__":
    build_questions()

