# -*- coding: utf-8 -*-
"""
Batch 4: Grand Test MCQs ISR_GT_076 to ISR_GT_100
Key distribution: A: 6, B: 6, C: 6, D: 7 (Total: 25)
Difficulty: 7 Easy, 8 Medium, 10 Hard
"""

from isr_gt_helper import make_q

def get_batch4():
    qs = []

    # 076 - Key A (Easy)
    qs.append(make_q(
        num=76, diff="Easy", qtype="Concept MCQ", subtopic="Constitutional Framework",
        en_stem="Under which legislative entry in the Union List (List I) did Parliament enact the Inter-State Migrant Workmen (Regulation of Employment and Conditions of Service) Act, 1979?",
        ta_stem="மத்தியப் பட்டியலில் (பட்டியல் I) உள்ள எந்த சட்டமன்றப் பதிவின் கீழ் பாராளுமன்றம் மாநிலங்களுக்கு இடையேயான புலம்பெயர்ந்த தொழிலாளர்கள் (வேலைவாய்ப்பு மற்றும் சேவை நிபந்தனைகள் ஒழுங்குமுறை) சட்டம் 1979-ஐ இயற்றியது?",
        en_a="Entry 81: Inter-state migration; inter-state quarantine", ta_a="பதிவு 81: மாநிலங்களுக்கு இடையேயான இடம்பெயர்வு; மாநிலங்களுக்கு இடையேயான தனிமைப்படுத்தல்",
        en_b="Entry 14: Agriculture including agricultural education and research", ta_b="பதிவு 14: விவசாயக் கல்வி மற்றும் ஆராய்ச்சி உள்ளிட்ட விவசாயம்",
        en_c="Entry 18: Land and rights in or over land", ta_c="பதிவு 18: நிலம் மற்றும் நிலத்தின் மீதான உரிமைகள்",
        en_d="Entry 2: Police including railway and village police", ta_d="பதிவு 2: ரயில்வே மற்றும் கிராமக் காவல் உள்ளிட்ட காவல் துறை",
        correct_key="A",
        exp_en="Parliament derived its legislative competence to enact the Inter-State Migrant Workmen Act, 1979 from Entry 81 of the Union List (Seventh Schedule), which covers 'Inter-State migration; inter-State quarantine.'",
        exp_ta="ஏழாவது அட்டவணையின் மத்தியப் பட்டியல் பதிவு 81-ல் ('மாநிலங்களுக்கு இடையேயான இடம்பெயர்வு; மாநிலங்களுக்கு இடையேயான தனிமைப்படுத்தல்') உள்ள அதிகாரத்தின் கீழேயே பாராளுமன்றம் 1979-ஆம் ஆண்டின் மாநிலங்களுக்கு இடையேயான புலம்பெயர்ந்த தொழிலாளர்கள் சட்டத்தை இயற்றியது.",
        why_a_en="Option A is correct; Entry 81 of List I governs inter-state migration.",
        why_a_ta="விருப்பம் A சரியானது; மத்தியப் பட்டியல் பதிவு 81 மாநிலங்களுக்கு இடையேயான இடம்பெயர்வை நிர்வகிக்கிறது.",
        why_b_en="Option B is Entry 14 of List II (State List).",
        why_b_ta="விருப்பம் B மாநிலப் பட்டியல் பதிவு 14.",
        why_c_en="Option C is Entry 18 of List II (State List).",
        why_c_ta="விருப்பம் C மாநிலப் பட்டியல் பதிவு 18.",
        why_d_en="Option D is Entry 2 of List II (State List).",
        why_d_ta="விருப்பம் D மாநிலப் பட்டியல் பதிவு 2.",
        tip_en="Entry 81 List I = Inter-State migration & quarantine. Governs rights of migrant workers moving across states.",
        tip_ta="மத்தியப் பட்டியல் பதிவு 81 = மாநிலங்களுக்கு இடையேயான இடம்பெயர்வு & தனிமைப்படுத்தல்.",
        fact_en="This Act was designed to prevent exploitation of vulnerable migrant labourers hired through contractors in their home states for work in host states.",
        fact_ta="சொந்த மாநிலத்தில் ஒப்பந்ததாரர்கள் மூலம் பிற மாநிலங்களுக்கு வேலைக்கு அழைத்துச் செல்லப்படும் புலம்பெயர்ந்த தொழிலாளர்களின் சுரண்டலைத் தடுக்க இந்தச் சட்டம் கொண்டுவரப்பட்டது."
    ))

    # 077 - Key B (Easy)
    qs.append(make_q(
        num=77, diff="Easy", qtype="Concept MCQ", subtopic="Constitutional Framework",
        en_stem="Which constitutional body, inserted by the 101st Constitutional Amendment Act, 2016 under Article 279A, represents the apex institutional forum for cooperative fiscal federalism between the Centre and the States?",
        ta_stem="101-வது அரசியலமைப்பு திருத்தச் சட்டம் 2016-ன் மூலம் சரத்து 279A-ன் கீழ் சேர்க்கப்பட்ட எந்த அரசியலமைப்பு அமைப்பு, மத்திய மற்றும் மாநிலங்களுக்கு இடையேயான கூட்டுறவு நிதி கூட்டாட்சியின் உச்ச நிறுவன மன்றமாகத் திகழ்கிறது?",
        en_a="Finance Commission of India", ta_a="இந்திய நிதி ஆணையம்",
        en_b="Goods and Services Tax (GST) Council", ta_b="சரக்கு மற்றும் சேவை வரி (GST) கவுன்சில்",
        en_c="National Development Council", ta_c="தேசிய வளர்ச்சிக் குழு",
        en_d="Inter-State Commerce Authority", ta_d="மாநிலங்களுக்கு இடையேயான வர்த்தக ஆணையம்",
        correct_key="B",
        exp_en="Article 279A, introduced by the 101st Constitutional Amendment Act, 2016, created the Goods and Services Tax (GST) Council as a constitutional body to make recommendations to the Union and States on GST rates, exemptions, and dispute settlement.",
        exp_ta="101-வது அரசியலமைப்பு திருத்தச் சட்டம் 2016-ன் மூலம் அறிமுகப்படுத்தப்பட்ட சரத்து 279A, ஜிஎஸ்டி விகிதங்கள், விலக்குகள் மற்றும் தகராறு தீர்வு குறித்து மத்திய மற்றும் மாநிலங்களுக்குப் பரிந்துரைகளை வழங்க ஜிஎஸ்டி கவுன்சிலை ஓர் அரசியலமைப்பு அமைப்பாக நிறுவியது.",
        why_a_en="Option A is constituted under Article 280.",
        why_a_ta="விருப்பம் A சரத்து 280-ன் கீழ் அமைக்கப்படுகிறது.",
        why_b_en="Option B is correct; GST Council was inserted under Article 279A.",
        why_b_ta="விருப்பம் B சரியானது; ஜிஎஸ்டி கவுன்சில் சரத்து 279A-ன் கீழ் சேர்க்கப்பட்டது.",
        why_c_en="Option C was an extra-constitutional executive body set up in 1952.",
        why_c_ta="விருப்பம் C 1952 இல் அமைக்கப்பட்ட அரசியலமைப்பு சாரா அமைப்பு.",
        why_d_en="Option D has never been established under Article 307.",
        why_d_ta="விருப்பம் D சரத்து 307-ன் கீழ் இதுவரை அமைக்கப்படவில்லை.",
        tip_en="Article 279A = GST Council (101st Amendment, 2016). Article 280 = Finance Commission.",
        tip_ta="சரத்து 279A = ஜிஎஸ்டி கவுன்சில் (101-வது திருத்தம், 2016). சரத்து 280 = நிதி ஆணையம்.",
        fact_en="The GST Council brought together the Union and all State finance ministers to replace the fragmented inter-state checkpost taxation regime.",
        fact_ta="ஜிஎஸ்டி கவுன்சில் பிளவுபட்ட மாநிலங்களுக்கு இடையேயான சோதனைச் சாவடி வரி முறையை மாற்ற மத்திய மற்றும் அனைத்து மாநில நிதி அமைச்சர்களையும் ஒன்றிணைத்தது."
    ))

    # 078 - Key C (Easy)
    qs.append(make_q(
        num=78, diff="Easy", qtype="Concept MCQ", subtopic="Constitutional Framework",
        en_stem="Who serves as the Chairperson of the Goods and Services Tax (GST) Council established under Article 279A?",
        ta_stem="சரத்து 279A-ன் கீழ் நிறுவப்பட்ட சரக்கு மற்றும் சேவை வரி (GST) கவுன்சிலின் தலைவராகச் செயல்படுபவர் யார்?",
        en_a="Prime Minister of India", ta_a="இந்தியப் பிரதமர்",
        en_b="Governor of the Reserve Bank of India", ta_b="இந்திய ரிசர்வ் வங்கி ஆளுநர்",
        en_c="Union Finance Minister", ta_c="மத்திய நிதி அமைச்சர்",
        en_d="Chairman of the Finance Commission", ta_d="நிதி ஆணையத்தின் தலைவர்",
        correct_key="C",
        exp_en="Under Article 279A(2)(a), the Union Finance Minister is the Chairperson of the GST Council. The Union Minister of State in charge of Revenue or Finance is a member, along with the Ministers in charge of Finance or Taxation of each State Government.",
        exp_ta="சரத்து 279A(2)(a)-ன் படி, மத்திய நிதி அமைச்சர் ஜிஎஸ்டி கவுன்சிலின் தலைவராக இருக்கிறார். மத்திய நிதி இணை அமைச்சர் மற்றும் ஒவ்வொரு மாநில அரசுகளின் நிதி அல்லது வரித்துறை அமைச்சர்கள் இதில் உறுப்பினர்களாக உள்ளனர்.",
        why_a_en="Option A is incorrect; Prime Minister chairs the Inter-State Council and NITI Aayog.",
        why_a_ta="விருப்பம் A தவறானது; பிரதமர் மாநிலங்களுக்கு இடையேயான கவுன்சில் மற்றும் நிதி ஆயோக்கின் தலைவர்.",
        why_b_en="Option B is incorrect; RBI Governor is not a member.",
        why_b_ta="விருப்பம் B தவறானது; ரிசர்வ் வங்கி ஆளுநர் இதில் உறுப்பினர் அல்ல.",
        why_c_en="Option C is correct; Union Finance Minister is Chairperson.",
        why_c_ta="விருப்பம் C சரியானது; மத்திய நிதி அமைச்சரே தலைவர் ஆவார்.",
        why_d_en="Option D is incorrect.",
        why_d_ta="விருப்பம் D தவறானது.",
        tip_en="GST Council Chairperson = Union Finance Minister. Vice-Chairperson = Chosen from among State Finance Ministers.",
        tip_ta="ஜிஎஸ்டி கவுன்சில் தலைவர் = மத்திய நிதி அமைச்சர். துணைத் தலைவர் = மாநில நிதி அமைச்சர்களிலிருந்து தேர்ந்தெடுக்கப்படுபவர்.",
        fact_en="The members of the GST Council from the States choose one amongst themselves to be the Vice-Chairperson of the Council for such period as they may decide.",
        fact_ta="மாநில நிதி அமைச்சர்கள் தங்களில் ஒருவரை ஜிஎஸ்டி கவுன்சிலின் துணைத் தலைவராகத் தேர்ந்தெடுக்கின்றனர்."
    ))

    # 079 - Key D (Easy)
    qs.append(make_q(
        num=79, diff="Easy", qtype="Concept MCQ", subtopic="Constitutional Framework",
        en_stem="In the voting mechanism of the GST Council under Article 279A(9), what is the weightage allocated to the vote of the Central Government?",
        ta_stem="சரத்து 279A(9)-ன் கீழ் ஜிஎஸ்டி கவுன்சிலின் வாக்குப்பதிவு முறையில், மத்திய அரசின் வாக்கிற்கு ஒதுக்கப்பட்டுள்ள எடை (பங்கு) என்ன?",
        en_a="One-half (50%) of the total votes cast", ta_a="பதிவான மொத்த வாக்குகளில் பாதி (50%)",
        en_b="One-fourth (25%) of the total votes cast", ta_b="பதிவான மொத்த வாக்குகளில் நான்கில் ஒரு பங்கு (25%)",
        en_c="Three-fourths (75%) of the total votes cast", ta_c="பதிவான மொத்த வாக்குகளில் நான்கில் மூன்று பங்கு (75%)",
        en_d="One-third (33.33%) of the total votes cast", ta_d="பதிவான மொத்த வாக்குகளில் மூன்றில் ஒரு பங்கு (33.33%)",
        correct_key="D",
        exp_en="Under Article 279A(9)(a), the vote of the Central Government has a weightage of one-third (33.33%) of the total votes cast, while the votes of all the State Governments taken together have a weightage of two-thirds (66.67%) of the total votes cast.",
        exp_ta="சரத்து 279A(9)(a)-ன் படி, மத்திய அரசின் வாக்கிற்கு பதிவான மொத்த வாக்குகளில் மூன்றில் ஒரு பங்கு (33.33%) எடையும்; அனைத்து மாநில அரசுகளின் வாக்குகளுக்கும் சேர்த்து மூன்றில் இரண்டு பங்கு (66.67%) எடையும் ஒதுக்கப்பட்டுள்ளது.",
        why_a_en="Option A is incorrect; Central vote is not 50%.",
        why_a_ta="விருப்பம் A தவறானது; மத்திய வாக்கு 50% அல்ல.",
        why_b_en="Option B is incorrect.",
        why_b_ta="விருப்பம் B தவறானது.",
        why_c_en="Option C is the required threshold to pass a resolution, not the Centre's voting weightage.",
        why_c_ta="விருப்பம் C என்பது முடிவை நிறைவேற்றத் தேவையான பெரும்பான்மை, மத்திய அரசின் வாக்கு எடை அல்ல.",
        why_d_en="Option D is correct; the Central Government holds one-third (1/3rd) weighted vote.",
        why_d_ta="விருப்பம் D சரியானது; மத்திய அரசு மூன்றில் ஒரு பங்கு (1/3) வாக்கு எடையைக் கொண்டுள்ளது.",
        tip_en="GST Council Voting: Centre = 1/3 (33.33%); All States combined = 2/3 (66.67%).",
        tip_ta="ஜிஎஸ்டி கவுன்சில் வாக்கு: மத்திய அரசு = 1/3 (33.33%); அனைத்து மாநிலங்களும் சேர்ந்து = 2/3 (66.67%).",
        fact_en="This weighted structure ensures that neither the Centre nor the States alone can push through a decision without substantial consensus from the other.",
        fact_ta="இந்த வாக்கு எடை கட்டமைப்பு, மற்றவரின் ஒருமித்த ஆதரவின்றி மத்திய அரசோ அல்லது மாநிலங்களோ மட்டும் தனித்து எந்த முடிவையும் திணிக்க முடியாது என்பதை உறுதி செய்கிறது."
    ))

    # 080 - Key A (Easy)
    qs.append(make_q(
        num=80, diff="Easy", qtype="Concept MCQ", subtopic="Constitutional Framework",
        en_stem="What is the minimum majority required for the GST Council to adopt any decision at its meetings under Article 279A(9)?",
        ta_stem="சரத்து 279A(9)-ன் கீழ் ஜிஎஸ்டி கவுன்சில் தனது கூட்டங்களில் எந்தவொரு முடிவையும் ஏற்றுக்கொள்வதற்குத் தேவையான குறைந்தபட்ச பெரும்பான்மை என்ன?",
        en_a="Not less than three-fourths (75%) of the weighted votes of the members present and voting", ta_a="கூட்டத்தில் பங்கேற்று வாக்களிக்கும் உறுப்பினர்களின் எடையிடப்பட்ட வாக்குகளில் நான்கில் மூன்று பங்குக்கு (75%) குறையாமல்",
        en_b="A simple majority of 51% of members present", ta_b="பங்கேற்கும் உறுப்பினர்களில் 51% எளிய பெரும்பான்மை",
        en_c="A unanimous vote (100%) of all members present", ta_c="பங்கேற்கும் அனைத்து உறுப்பினர்களின் ஒருமனதான வாக்கு (100%)",
        en_d="A two-thirds (66.67%) majority of total membership", ta_d="மொத்த உறுப்பினர்களில் மூன்றில் இரண்டு பங்கு (66.67%) பெரும்பான்மை",
        correct_key="A",
        exp_en="Article 279A(9) mandates that every decision of the GST Council shall be taken at a meeting by a majority of not less than three-fourths (75%) of the weighted votes of the members present and voting.",
        exp_ta="சரத்து 279A(9) ஜிஎஸ்டி கவுன்சிலின் ஒவ்வொரு முடிவும் கூட்டத்தில் பங்கேற்று வாக்களிக்கும் உறுப்பினர்களின் எடையிடப்பட்ட வாக்குகளில் நான்கில் மூன்று பங்குக்கு (75%) குறையாத பெரும்பான்மையால் எடுக்கப்பட வேண்டும் என்று கட்டாயமாக்குகிறது.",
        why_a_en="Option A is the exact constitutional majority: three-fourths (75%) weighted votes.",
        why_a_ta="விருப்பம் A என்பது சரியான அரசியலமைப்பு பெரும்பான்மை: 75% எடையிடப்பட்ட வாக்குகள்.",
        why_b_en="Option B is incorrect; simple majority is not enough.",
        why_b_ta="விருப்பம் B தவறானது; எளிய பெரும்பான்மை போதாது.",
        why_c_en="Option C is incorrect; unanimity is not mandatory, though aimed for in practice.",
        why_c_ta="விருப்பம் C தவறானது; ஒருமனதான முடிவு கட்டாயமில்லை.",
        why_d_en="Option D is incorrect.",
        why_d_ta="விருப்பம் D தவறானது.",
        tip_en="GST Decision Threshold = 75% (3/4th) weighted votes. Quorum = 50% of total members.",
        tip_ta="ஜிஎஸ்டி முடிவு வரம்பு = 75% (3/4) எடையிடப்பட்ட வாக்குகள். குறைந்தபட்ச வருகை (கோரம்) = 50% உறுப்பினர்கள்.",
        fact_en="Since the Centre holds 33.33% and the required majority is 75%, the Central Government holds an effective veto over any decision.",
        fact_ta="மத்திய அரசு 33.33% வாக்குகளைக் கொண்டிருப்பதாலும், தேவைப்படும் பெரும்பான்மை 75% என்பதாலும், மத்திய அரசுக்கு நடைமுறையில் ஒரு வீட்டோ அதிகாரம் உள்ளது."
    ))

    # 081 - Key B (Easy)
    qs.append(make_q(
        num=81, diff="Easy", qtype="Concept MCQ", subtopic="Constitutional Framework",
        en_stem="Under Section 6 of the Delhi Special Police Establishment (DSPE) Act, 1946, what is required before the Central Bureau of Investigation (CBI) can exercise jurisdiction to investigate an offence within a State?",
        ta_stem="1946-ஆம் ஆண்டின் தில்லி சிறப்பு காவல் ஸ்தாபன (DSPE) சட்டத்தின் பிரிவு 6-ன் கீழ், ஒரு மாநிலத்திற்குள் ஒரு குற்றத்தை விசாரிக்க மத்திய புலனாய்வு அமைப்பு (CBI) தனது அதிகார வரம்பைப் பயன்படுத்துவதற்கு முன் என்ன தேவைப்படுகிறது?",
        en_a="Prior warrant issued by the International Criminal Police Organization (Interpol)", ta_a="சர்வதேச குற்றவியல் காவல் அமைப்பு (இன்டர்போல்) பிறப்பிக்கும் முன் பிடியாணை",
        en_b="Consent of the Government of that State", ta_b="அந்த மாநில அரசின் ஒப்புதல்",
        en_c="Formal resolution passed by the Lok Sabha Privileges Committee", ta_c="மக்களவை உரிமைக்குழு நிறைவேற்றும் முறையான தீர்மானம்",
        en_d="Written concurrence of all Chief Justices of neighboring High Courts", ta_d="அண்டை மாநில உயர் நீதிமன்றத் தலைமை நீதிபதிகள் அனைவரின் எழுத்துப்பூர்வ இசைவு",
        correct_key="B",
        exp_en="Section 6 of the DSPE Act explicitly provides: 'Nothing contained in section 5 shall be deemed to enable any member of the Delhi Special Police Establishment to exercise powers and jurisdiction in any area in a State, not being a Union territory or railway area, without the consent of the Government of that State.'",
        exp_ta="DSPE சட்டத்தின் பிரிவு 6, ஒரு யூனியன் பிரதேசம் அல்லது ரயில்வே பகுதி அல்லாத ஒரு மாநிலத்திற்குள் சி.பி.ஐ அதிகார வரம்பைப் பயன்படுத்த வேண்டுமானால், அந்த மாநில அரசின் ஒப்புதல் (Consent) பெறப்பட வேண்டும் என்று தெளிவாகக் கூறுகிறது.",
        why_a_en="Option A is irrelevant to domestic criminal investigations.",
        why_a_ta="விருப்பம் A உள்நாட்டு குற்ற விசாரணைகளுக்கு தொடர்பற்றது.",
        why_b_en="Option B is correct; Section 6 mandates the consent of the State Government.",
        why_b_ta="விருப்பம் B சரியானது; பிரிவு 6 மாநில அரசின் ஒப்புதலைக் கட்டாயமாக்குகிறது.",
        why_c_en="Option C is incorrect.",
        why_c_ta="விருப்பம் C தவறானது.",
        why_d_en="Option D is incorrect.",
        why_d_ta="விருப்பம் D தவறானது.",
        tip_en="Section 6 DSPE Act: CBI needs State Government consent (general consent or case-specific consent).",
        tip_ta="DSPE சட்டம் பிரிவு 6: சிபிஐ மாநிலத்திற்குள் நுழைய மாநில அரசின் ஒப்புதல் (பொது ஒப்புதல் அல்லது குறிப்பிட்ட வழக்கு ஒப்புதல்) தேவை.",
        fact_en="Several States (such as Tamil Nadu, West Bengal, and Kerala) have periodically withdrawn 'general consent' to the CBI, requiring case-specific consent.",
        fact_ta="தமிழ்நாடு, மேற்கு வங்கம் மற்றும் கேரளா உள்ளிட்ட பல மாநிலங்கள் அவ்வப்போது சிபிஐ-க்கு வழங்கப்பட்ட 'பொது ஒப்புதலை' திரும்பப் பெற்றுள்ளன."
    ))

    # 082 - Key C (Easy)
    qs.append(make_q(
        num=82, diff="Easy", qtype="Concept MCQ", subtopic="Public Acts, Records and Judicial Proceedings",
        en_stem="While international transfer of fugitive criminals is governed by the Extradition Act, 1962, how is the arrest and inter-state transfer of an accused person executed between different States within India?",
        ta_stem="வெளிநாட்டு குற்றவாளிகளை நாடு கடத்துவது 1962-ஆம் ஆண்டின் ஒப்படைப்புச் சட்டத்தால் நிர்வகிக்கப்படும் அதே வேளையில், இந்தியாவிற்குள் வெவ்வேறு மாநிலங்களுக்கு இடையே குற்றம் சாட்டப்பட்ட ஒருவரைக் கைது செய்து மாற்றுவது எவ்வாறு செயல்படுத்தப்படுகிறது?",
        en_a="By filing a formal diplomatic treaty through the Ministry of External Affairs", ta_a="வெளியுறவு அமைச்சகம் மூலம் முறையான தூதரக ஒப்பந்தத்தை தாக்கல் செய்வதன் மூலம்",
        en_b="By seeking prior sanction from the Inter-State Council Standing Committee", ta_b="மாநிலங்களுக்கு இடையேயான கவுன்சில் நிலைக்குழுவிடம் முன் அனுமதி பெறுவதன் மூலம்",
        en_c="Under the provisions of the Code of Criminal Procedure / BNSS through execution of warrants outside local jurisdiction (with local magistrate transit remand)", ta_c="உள்ளூர் அதிகார வரம்பிற்கு வெளியே பிடியாணைகளை நிறைவேற்றுவதன் மூலம் (உள்ளூர் மாஜிஸ்திரேட் இடைக்கால காவல் அனுமதியுடன்) குற்றவியல் நடைமுறைச் சட்டம் / BNSS விதிகளின் கீழ்",
        en_d="Exclusively by deploying central paramilitary forces with Governor's approval", ta_d="ஆளுநரின் ஒப்புதலுடன் மத்திய துணை ராணுவப் படைகளை நிலைநிறுத்துவதன் மூலம் மட்டுமே",
        correct_key="C",
        exp_en="Within India, inter-state arrests and transfers are governed by the Code of Criminal Procedure, 1973 (Sections 78-81) / Bharatiya Nagarik Suraksha Sanhita (BNSS). Police from one state executing an arrest warrant in another state must produce the accused before the nearest local Magistrate for transit remand within 24 hours under Article 22(2).",
        exp_ta="இந்தியாவிற்குள் மாநிலங்களுக்கு இடையேயான கைதுகள் குற்றவியல் நடைமுறைச் சட்டம் 1973 (பிரிவுகள் 78-81) / BNSS மூலம் நிர்வகிக்கப்படுகின்றன. ஒரு மாநிலக் காவல்துறை மற்றொரு மாநிலத்தில் கைது செய்யும் போது, சரத்து 22(2)-ன் கீழ் 24 மணி நேரத்திற்குள் அருகிலுள்ள மாஜிஸ்திரேட்டிடம் ஆஜர்படுத்தி டிரான்சிட் ரிமாண்ட் (Transit Remand) பெற வேண்டும்.",
        why_a_en="Option A applies to sovereign foreign nations, not Indian states.",
        why_a_ta="விருப்பம் A வெளிநாடுகளுக்கு மட்டுமே பொருந்தும்.",
        why_b_en="Option B is incorrect; ISC has no role in police warrants.",
        why_b_ta="விருப்பம் B தவறானது; கவுன்சிலுக்கு இதில் பங்கு இல்லை.",
        why_c_en="Option C is the established criminal procedural law across Indian states.",
        why_c_ta="விருப்பம் C என்பது இந்திய மாநிலங்களுக்கிடையேயான சரியான குற்றவியல் நடைமுறைச் சட்டம் ஆகும்.",
        why_d_en="Option D is incorrect.",
        why_d_ta="விருப்பம் D தவறானது.",
        tip_en="Inter-state police arrest within India requires transit remand from local Magistrate under Section 80/81 CrPC and Article 22(2).",
        tip_ta="மாநிலங்களுக்கு இடையேயான கைதுக்கு பிரிவு 80/81 CrPC மற்றும் சரத்து 22(2)-ன் கீழ் உள்ளூர் மாஜிஸ்திரேட்டிடம் டிரான்சிட் ரிமாண்ட் பெற வேண்டும்.",
        fact_en="Article 22(2) constitutional guarantee mandates that every arrested person must be produced before the nearest magistrate within 24 hours excluding journey time.",
        fact_ta="கைது செய்யப்பட்ட எவரும் பயண நேரத்தைத் தவிர்த்து 24 மணி நேரத்திற்குள் அருகிலுள்ள மாஜிஸ்திரேட்டிடம் ஆஜர்படுத்தப்பட வேண்டும் என்று சரத்து 22(2) உத்தரவாதம் அளிக்கிறது."
    ))

    # 083 - Key D (Medium)
    qs.append(make_q(
        num=83, diff="Medium", qtype="Concept MCQ", subtopic="Constitutional Framework",
        en_stem="In the landmark Constitution Bench judgment State of West Bengal v. Committee for Protection of Democratic Rights (2010), what did the Supreme Court hold regarding Section 6 of the DSPE Act and constitutional courts?",
        ta_stem="மேற்கு வங்க மாநிலம் எதிர் ஜனநாயக உரிமைகள் பாதுகாப்புக்கான குழு (2010) என்ற வரலாற்றுத் தீர்ப்பில், DSPE சட்டத்தின் பிரிவு 6 மற்றும் அரசியலமைப்பு நீதிமன்றங்கள் குறித்து உச்ச நீதிமன்றம் என்ன தீர்ப்பளித்தது?",
        en_a="The Supreme Court and High Courts can never direct a CBI investigation without state consent under any circumstances", ta_a="எந்த சூழ்நிலையிலும் மாநில அரசின் ஒப்புதல் இல்லாமல் உச்ச நீதிமன்றமும் உயர் நீதிமன்றங்களும் சிபிஐ விசாரணைக்கு உத்தரவிடவே முடியாது",
        en_b="Section 6 was declared totally unconstitutional and struck down", ta_b="பிரிவு 6 முற்றிலும் அரசியலமைப்பிற்கு முரணானது என்று அறிவிக்கப்பட்டு ரத்து செய்யப்பட்டது",
        en_c="The CBI was permanently disbanded and replaced with State Vigilance Bureaus", ta_c="சிபிஐ நிரந்தரமாகக் கலைக்கப்பட்டு மாநில லஞ்ச ஒழிப்புத் துறைகள் மாற்றப்பட்டன",
        en_d="The Supreme Court and High Courts under Articles 32 and 226 have constitutional power to direct the CBI to investigate an offence within a State without the consent of that State Government", ta_d="சரத்துகள் 32 மற்றும் 226-ன் கீழ் உச்ச நீதிமன்றம் மற்றும் உயர் நீதிமன்றங்கள் மாநில அரசின் ஒப்புதல் இன்றியே அந்த மாநிலத்திற்குள் ஒரு குற்றத்தை விசாரிக்க சிபிஐ-க்கு உத்தரவிட அரசியலமைப்பு அதிகாரம் கொண்டுள்ளன",
        correct_key="D",
        exp_en="In CPDR (2010), the Constitution Bench held that while Section 6 of the DSPE Act restricts the Central Government from sending the CBI without state consent, it cannot fetter the extraordinary constitutional writ jurisdiction of the Supreme Court (Art 32) or High Courts (Art 226) to direct CBI probe without state consent to protect fundamental rights.",
        exp_ta="2010 CPDR வழக்கில் அரசியலமைப்பு அமர்வு, DSPE சட்டத்தின் பிரிவு 6 மத்திய அரசு சிபிஐ-யை அனுப்புவதைக் கட்டுப்படுத்தினாலும், அடிப்படை உரிமைகளைப் பாதுகாக்க சரத்து 32 அல்லது 226-ன் கீழ் உச்ச நீதிமன்றம் அல்லது உயர் நீதிமன்றங்கள் மாநில ஒப்புதல் இன்றியே சிபிஐ விசாரணைக்கு உத்தரவிடலாம் என்று தீர்ப்பளித்தது.",
        why_a_en="Option A was the State's argument, which was rejected by the Court.",
        why_a_ta="விருப்பம் A மாநில அரசின் வாதம், இது நீதிமன்றத்தால் நிராகரிக்கப்பட்டது.",
        why_b_en="Option B is incorrect; Section 6 remains valid for executive references by the Union.",
        why_b_ta="விருப்பம் B தவறானது; பிரிவு 6 மத்திய அரசின் நிர்வாக உத்தரவுகளுக்கு தொடர்ந்து செல்லுபடியாகும்.",
        why_c_en="Option C is frivolous.",
        why_c_ta="விருப்பம் C தவறானது.",
        why_d_en="Option D is the exact holding of the Constitution Bench.",
        why_d_ta="விருப்பம் D என்பது அரசியலமைப்பு அமர்வின் துல்லியமான முக்கிய தீர்ப்பாகும்.",
        tip_en="Executive CBI reference needs State consent (Sec 6 DSPE). Judicial CBI order under Art 32/226 DOES NOT need State consent.",
        tip_ta="மத்திய அரசின் சிபிஐ விசாரணைக்கு மாநில ஒப்புதல் தேவை (பிரிவு 6). சரத்து 32/226-ன் கீழான நீதிமன்ற உத்தரவிற்கு மாநில ஒப்புதல் தேவையில்லை.",
        fact_en="The Supreme Court cautioned that this extraordinary power should be exercised sparingly and only in rare and exceptional cases.",
        fact_ta="இந்த அசாதாரண அதிகாரத்தை அரிதான மற்றும் விதிவிலக்கான வழக்குகளில் மட்டுமே சிக்கனமாகப் பயன்படுத்த வேண்டும் என்று உச்ச நீதிமன்றம் எச்சரித்தது."
    ))

    # 084 - Key A (Medium)
    qs.append(make_q(
        num=84, diff="Medium", qtype="Concept MCQ", subtopic="Inter-State Border Disputes",
        en_stem="In March 2022, a historic Memorandum of Understanding (MoU) was signed in New Delhi in the presence of the Union Home Minister to partially resolve a 50-year-old inter-state border dispute between which two North-Eastern States?",
        ta_stem="மார்ச் 2022 இல் புது தில்லியில் மத்திய உள்துறை அமைச்சர் முன்னிலையில் 50 ஆண்டுகால மாநிலங்களுக்கு இடையேயான எல்லைத் தகராறைப் பகுதியாகத் தீர்க்க எந்த இரண்டு வடகிழக்கு மாநிலங்களுக்கு இடையே வரலாற்றுச் சிறப்புமிக்க புரிந்துணர்வு ஒப்பந்தம் (MoU) கையெழுத்தானது?",
        en_a="Assam and Meghalaya", ta_a="அசாம் மற்றும் மேகாலயா",
        en_b="Tripura and Mizoram", ta_b="திரிபுரா மற்றும் மிசோரம்",
        en_c="Nagaland and Manipur", ta_c="நாகாலாந்து மற்றும் மணிப்பூர்",
        en_d="Arunachal Pradesh and Sikkim", ta_d="அருணாச்சலப் பிரதேசம் மற்றும் சிக்கிம்",
        correct_key="A",
        exp_en="On March 29, 2022, the Chief Ministers of Assam (Himanta Biswa Sarma) and Meghalaya (Conrad Sangma) signed a historic agreement in the presence of Union Home Minister Amit Shah to resolve 6 out of 12 disputed border sectors along their 884-km boundary.",
        exp_ta="மார்ச் 29, 2022 அன்று, அசாம் முதலமைச்சர் (ஹிமந்த பிஸ்வா சர்மா) மற்றும் மேகாலயா முதலமைச்சர் (கான்ராட் சங்மா) ஆகியோர் மத்திய உள்துறை அமைச்சர் அமித் ஷா முன்னிலையில் 884 கி.மீ எல்லையில் உள்ள 12 தகராறுக்குரிய பகுதிகளில் 6 பகுதிகளைத் தீர்க்க வரலாற்று ஒப்பந்தத்தில் கையெழுத்திட்டனர்.",
        why_a_en="Option A is correct; Assam and Meghalaya signed the landmark March 2022 boundary pact.",
        why_a_ta="விருப்பம் A சரியானது; அசாம் மற்றும் மேகாலயா மார்ச் 2022 எல்லை ஒப்பந்தத்தில் கையெழுத்திட்டன.",
        why_b_en="Option B involves the Bru/Reang refugee settlement pact (January 2020).",
        why_b_ta="விருப்பம் B புரூ/ரியாங் அகதிகள் மறுவாழ்வு ஒப்பந்தம் தொடர்பானது (ஜனவரி 2020).",
        why_c_en="Option C is incorrect.",
        why_c_ta="விருப்பம் C தவறானது.",
        why_d_en="Option D is incorrect.",
        why_d_ta="விருப்பம் D தவறானது.",
        tip_en="Assam-Meghalaya Border Pact (March 2022) resolved 6 out of 12 disputed sectors. Later, Assam-Arunachal Pradesh signed the Namsai Declaration (July 2022).",
        tip_ta="அசாம்-மேகாலயா எல்லை ஒப்பந்தம் (மார்ச் 2022) 12-ல் 6 பகுதிகளைத் தீர்த்தது. பின்னர் அசாம்-அருணாச்சலப் பிரதேசம் நம்சாய் பிரகடனத்தில் (ஜூலை 2022) கையெழுத்திட்டன.",
        fact_en="Meghalaya was carved out of Assam originally as an autonomous state in 1970 and became a full state in 1972, leading to boundary demarcation disputes.",
        fact_ta="மேகாலயா 1970 இல் அசாமுக்குள் ஒரு தன்னாட்சி மாநிலமாகவும், 1972 இல் முழு மாநிலமாகவும் பிரிக்கப்பட்டதால் எல்லை வரையறை தகராறுகள் நீடித்தன."
    ))

    # 085 - Key B (Medium)
    qs.append(make_q(
        num=85, diff="Medium", qtype="Concept MCQ", subtopic="Inter-State Border Disputes",
        en_stem="The contentious dispute over the ownership and administrative control of the Kotia cluster of villages is an active inter-state conflict between which two States?",
        ta_stem="கோட்டியா கிராமக் குழுவின் உரிமை மற்றும் நிர்வாகக் கட்டுப்பாடு தொடர்பான சர்ச்சை எந்த இரண்டு மாநிலங்களுக்கு இடையேயான தீவிர மோதலாக உள்ளது?",
        en_a="Tamil Nadu and Karnataka", ta_a="தமிழ்நாடு மற்றும் கர்நாடகா",
        en_b="Andhra Pradesh and Odisha", ta_b="ஆந்திரப் பிரதேசம் மற்றும் ஒடிசா",
        en_c="Chhattisgarh and Jharkhand", ta_c="சத்தீஸ்கர் மற்றும் ஜார்க்கண்ட்",
        en_d="Maharashtra and Madhya Pradesh", ta_d="மகாராஷ்டிரா மற்றும் மத்தியப் பிரதேசம்",
        correct_key="B",
        exp_en="The Kotia dispute involves 28 mineral-rich villages in the Eastern Ghats claimed by both Odisha (Koraput district) and Andhra Pradesh (Parvathipuram Manyam district). The dispute has been contested before the Supreme Court under Article 131 since 1968.",
        exp_ta="கோட்டியா தகராறு என்பது கிழக்குத் தொடர்ச்சி மலையில் உள்ள கனிம வளம் மிக்க 28 கிராமங்களை உள்ளடக்கியது; இதை ஒடிசா (கோராபுட் மாவட்டம்) மற்றும் ஆந்திரப் பிரதேசம் (பார்வதிபுரம் மண்யம் மாவட்டம்) ஆகிய இரண்டும் உரிமை கோருகின்றன. 1968 முதல் இது சரத்து 131-ன் கீழ் உச்ச நீதிமன்றத்தில் நிலுவையில் உள்ளது.",
        why_a_en="Option A is incorrect.",
        why_a_ta="விருப்பம் A தவறானது.",
        why_b_en="Option B is correct; Kotia dispute is between Andhra Pradesh and Odisha.",
        why_b_ta="விருப்பம் B சரியானது; கோட்டியா தகராறு ஆந்திரப் பிரதேசம் மற்றும் ஒடிசா இடையேயானது.",
        why_c_en="Option C is incorrect.",
        why_c_ta="விருப்பம் C தவறானது.",
        why_d_en="Option D is incorrect.",
        why_d_ta="விருப்பம் D தவறானது.",
        tip_en="Kotia villages dispute = Andhra Pradesh vs Odisha (Article 131 litigation).",
        tip_ta="கோட்டியா கிராமங்கள் தகராறு = ஆந்திரப் பிரதேசம் vs ஒடிசா (சரத்து 131 வழக்கு).",
        fact_en="Both States have set up administrative offices, schools, and conducted local body elections simultaneously in these disputed villages.",
        fact_ta="இந்த தகராறுக்குரிய கிராமங்களில் இரண்டு மாநிலங்களும் ஒரே நேரத்தில் நிர்வாக அலுவலகங்கள், பள்ளிகளை அமைத்து உள்ளாட்சித் தேர்தல்களையும் நடத்தியுள்ளன."
    ))

    # 086 - Key C (Medium)
    qs.append(make_q(
        num=86, diff="Medium", qtype="Concept MCQ", subtopic="Public Acts, Records and Judicial Proceedings",
        en_stem="How does the constitutional recognition of domestic judicial decrees under Article 261(3) differ fundamentally from the recognition of foreign judgments under Section 13 of the Code of Civil Procedure, 1908?",
        ta_stem="சரத்து 261(3)-ன் கீழான உள்நாட்டு நீதித்துறை தீர்ப்புகளுக்கான அரசியலமைப்பு அங்கீகாரம், சிபிசி 1908 பிரிவு 13-ன் கீழான வெளிநாட்டுத் தீர்ப்புகளின் அங்கீகாரத்திலிருந்து எவ்வாறு அடிப்படையிலேயே வேறுபடுகிறது?",
        en_a="Foreign judgments are automatically executable, whereas domestic judgments require a treaty", ta_a="வெளிநாட்டுத் தீர்ப்புகள் தானாகவே நிறைவேற்றப்படலாம், ஆனால் உள்நாட்டுத் தீர்ப்புகளுக்கு ஒப்பந்தம் தேவை",
        en_b="Domestic decrees can only be executed in the state of origin", ta_b="உள்நாட்டுத் தீர்ப்புகளை அவை பிறப்பிக்கப்பட்ட மாநிலத்திற்குள் மட்டுமே நிறைவேற்ற முடியும்",
        en_c="Domestic civil decrees enjoy full constitutional faith and credit across all States, whereas foreign judgments can be challenged and impeached on grounds of jurisdiction, fraud, or violation of natural justice under Section 13 of CPC", ta_c="உள்நாட்டு சிவில் தீர்ப்புகள் அனைத்து மாநிலங்களிலும் முழு அரசியலமைப்பு மதிப்பைப் பெறுகின்றன; ஆனால் வெளிநாட்டுத் தீர்ப்புகளை அதிகார வரம்பு இன்மை, மோசடி அல்லது இயற்கை நீதி மீறல் அடிப்படையில் சிபிசி பிரிவு 13-ன் கீழ் மறுக்க முடியும்",
        en_d="Domestic judgments are valid for only 30 days outside the state", ta_d="உள்நாட்டுத் தீர்ப்புகள் மாநிலத்திற்கு வெளியே 30 நாட்களுக்கு மட்டுமே செல்லும்",
        correct_key="C",
        exp_en="Article 261(3) mandates that final civil decrees of any Indian court are capable of execution anywhere in India as a constitutional rule of federal unity. In contrast, under Section 13 of CPC, a foreign judgment is subject to judicial scrutiny and can be refused enforcement if it violates natural justice, jurisdiction, or international law.",
        exp_ta="சரத்து 261(3) கூட்டாட்சி ஒருமைப்பாட்டின் அடிப்படையில் இந்தியாவில் எங்கும் பிறப்பிக்கப்படும் சிவில் தீர்ப்புகள் நாடு முழுவதும் நிறைவேற்றப்படலாம் என்று கூறுகிறது. மாறாக, சிபிசி பிரிவு 13-ன் கீழ் ஒரு வெளிநாட்டுத் தீர்ப்பு இயற்கை நீதியை மீறினாலோ அல்லது மோசடியால் பெறப்பட்டாலோ அதை ஏற்க நீதிமன்றம் மறுக்க முடியும்.",
        why_a_en="Option A is completely upside down.",
        why_a_ta="விருப்பம் A தலைகீழானது.",
        why_b_en="Option B contradicts the plain text of Article 261(3).",
        why_b_ta="விருப்பம் B சரத்து 261(3)-க்கு எதிரானது.",
        why_c_en="Option C accurately captures the difference between constitutional full faith & credit and private international law scrutiny.",
        why_c_ta="விருப்பம் C அரசியலமைப்பு முழு மதிப்பு மற்றும் சர்வதேச சட்ட ஆய்வுக்கு இடையேயான வேறுபாட்டைச் சரியாக விளக்குகிறது.",
        why_d_en="Option D is incorrect; limitation periods apply under the Limitation Act.",
        why_d_ta="விருப்பம் D தவறானது.",
        tip_en="Article 261(3) removes inter-state friction: No Indian state court can treat a sister state's civil decree as a foreign judgment.",
        tip_ta="சரத்து 261(3): எந்தவொரு இந்திய நீதிமன்றமும் மற்றொரு மாநிலத்தின் சிவில் தீர்ப்பை வெளிநாட்டுத் தீர்ப்பாகக் கருத முடியாது.",
        fact_en="Section 44A of the CPC provides for execution of foreign decrees only from reciprocating territories specifically notified by the Central Government.",
        fact_ta="சிபிசி பிரிவு 44A மத்திய அரசால் அறிவிக்கப்பட்ட பரஸ்பர ஒப்பந்தம் கொண்ட நாடுகளின் தீர்ப்புகளுக்கு மட்டுமே பொருந்தும்."
    ))

    # 087 - Key D (Medium)
    qs.append(make_q(
        num=87, diff="Medium", qtype="Concept MCQ", subtopic="Zonal Councils and Reorganisation",
        en_stem="By which legislation was the State of Sikkim formally integrated as the eighth member state of the North Eastern Council (NEC)?",
        ta_stem="எந்தச் சட்டத்தின் மூலம் சிக்கிம் மாநிலம் வடகிழக்கு கவுன்சிலின் (NEC) எட்டாவது உறுப்பு மாநிலமாக முறைப்படி இணைக்கப்பட்டது?",
        en_a="36th Constitutional Amendment Act, 1975", ta_a="36-வது அரசியலமைப்பு திருத்தச் சட்டம், 1975",
        en_b="North Eastern Areas (Reorganisation) Act, 1971", ta_b="வடகிழக்கு பகுதிகள் (மறுசீரமைப்பு) சட்டம், 1971",
        en_c="States Reorganisation (Amendment) Act, 1986", ta_c="மாநில மறுசீரமைப்பு (திருத்தச்) சட்டம், 1986",
        en_d="North Eastern Council (Amendment) Act, 2002", ta_d="வடகிழக்கு கவுன்சில் (திருத்தச்) சட்டம், 2002",
        correct_key="D",
        exp_en="Parliament enacted the North Eastern Council (Amendment) Act, 2002 (effective December 2002), which formally inducted Sikkim as the eighth member state of the North Eastern Council. Prior to this, the NEC had only 7 members (the 'Seven Sisters').",
        exp_ta="பாராளுமன்றம் வடகிழக்கு கவுன்சில் (திருத்தச்) சட்டம் 2002-ஐ (டிசம்பர் 2002 முதல் நடைமுறைக்கு வந்தது) இயற்றியது; இது சிக்கிமை வடகிழக்கு கவுன்சிலின் எட்டாவது உறுப்பு மாநிலமாக அதிகாரப்பூர்வமாக இணைத்தது. இதற்கு முன்பு NEC-யில் 7 மாநிலங்கள் மட்டுமே இருந்தன.",
        why_a_en="Option A made Sikkim the 22nd state of India, but did not add it to the NEC.",
        why_a_ta="விருப்பம் A சிக்கிமை இந்தியாவின் 22-வது மாநிலமாக்கியது, ஆனால் NEC-யில் சேர்க்கவில்லை.",
        why_b_en="Option B created Manipur, Meghalaya, and Tripura.",
        why_b_ta="விருப்பம் B மணிப்பூர், மேகாலயா மற்றும் திரிபுராவை உருவாக்கியது.",
        why_c_en="Option C is incorrect.",
        why_c_ta="விருப்பம் C தவறானது.",
        why_d_en="Option D is correct; the 2002 amendment added Sikkim to the NEC.",
        why_d_ta="விருப்பம் D சரியானது; 2002 திருத்தச் சட்டம் சிக்கிமை NEC-யில் சேர்த்தது.",
        tip_en="Sikkim became Indian State: 1975 (36th Amendment). Sikkim joined NEC: 2002 (NEC Amendment Act).",
        tip_ta="சிக்கிம் இந்திய மாநிலமானது: 1975 (36-வது திருத்தம்). சிக்கிம் NEC-யில் சேர்ந்தது: 2002 (NEC திருத்தச் சட்டம்).",
        fact_en="With Sikkim's inclusion, the Ministry of DoNER covers all 8 North Eastern States for regional infrastructure funding.",
        fact_ta="சிக்கிமின் சேர்க்கையுடன், DoNER அமைச்சகம் பிராந்திய உள்கட்டமைப்பு நிதி ஒதுக்கீட்டிற்காக அனைத்து 8 வடகிழக்கு மாநிலங்களையும் உள்ளடக்கியுள்ளது."
    ))

    # 088 - Key A (Medium)
    qs.append(make_q(
        num=88, diff="Medium", qtype="Concept MCQ", subtopic="Inter-State River Water Disputes",
        en_stem="The controversial Babhali Barrage dispute on the Godavari river, decided by the Supreme Court in February 2013 under Article 131, involved which two States?",
        ta_stem="பிப்ரவரி 2013 இல் சரத்து 131-ன் கீழ் உச்ச நீதிமன்றத்தால் தீர்ப்பளிக்கப்பட்ட கோதாவரி நதியின் மீதான பாப்லி அணைக்கட்டு சர்ச்சை எந்த இரண்டு மாநிலங்களை உள்ளடக்கியது?",
        en_a="Maharashtra and Andhra Pradesh", ta_a="மகாராஷ்டிரா மற்றும் ஆந்திரப் பிரதேசம்",
        en_b="Karnataka and Tamil Nadu", ta_b="கர்நாடகா மற்றும் தமிழ்நாடு",
        en_c="Kerala and Tamil Nadu", ta_c="கேரளா மற்றும் தமிழ்நாடு",
        en_d="Madhya Pradesh and Gujarat", ta_d="மத்தியப் பிரதேசம் மற்றும் குஜராத்",
        correct_key="A",
        exp_en="In State of Andhra Pradesh v. State of Maharashtra (February 2013), the Supreme Court resolved the Babhali Barrage dispute under Article 131, allowing Maharashtra to construct the barrage on the Godavari subject to strict water release conditions monitored by a supervisory committee.",
        exp_ta="ஆந்திரப் பிரதேசம் எதிர் மகாராஷ்டிரா (பிப்ரவரி 2013) வழக்கில், உச்ச நீதிமன்றம் சரத்து 131-ன் கீழ் பாப்லி அணைக்கட்டு தகராறைத் தீர்த்து, ஒரு கண்காணிப்புக் குழுவின் மேற்பார்வையில் குறிப்பிட்ட நீர் வெளியீட்டு நிபந்தனைகளுக்கு உட்பட்டு அணையைக் கட்ட மகாராஷ்டிராவிற்கு அனுமதித்தது.",
        why_a_en="Option A is correct; Babhali Barrage dispute was between Maharashtra and Andhra Pradesh.",
        why_a_ta="விருப்பம் A சரியானது; பாப்லி அணைக்கட்டு சர்ச்சை மகாராஷ்டிரா மற்றும் ஆந்திரா தொடர்பானது.",
        why_b_en="Option B is Cauvery.",
        why_b_ta="விருப்பம் B காவிரி.",
        why_c_en="Option C is Mullaperiyar.",
        why_c_ta="விருப்பம் C முல்லைப் பெரியாறு.",
        why_d_en="Option D is Narmada.",
        why_d_ta="விருப்பம் D நர்மதா.",
        tip_en="Babhali Barrage on Godavari = Maharashtra vs Andhra Pradesh (Article 131 suit).",
        tip_ta="கோதாவரியின் மீதான பாப்லி அணைக்கட்டு = மகாராஷ்டிரா vs ஆந்திரப் பிரதேசம் (சரத்து 131 வழக்கு).",
        fact_en="The Supreme Court set up a three-member supervisory committee (CWC, Maharashtra, AP) to operate the barrage gates between October and June.",
        fact_ta="அணை மதகுகளை இயக்குவதைக் கண்காணிக்க CWC மற்றும் இரு மாநிலப் பிரதிநிதிகளைக் கொண்ட 3 உறுப்பினர்கள் குழுவை உச்ச நீதிமன்றம் அமைத்தது."
    ))

    # 089 - Key B (Medium)
    qs.append(make_q(
        num=89, diff="Medium", qtype="Concept MCQ", subtopic="Inter-State River Water Disputes",
        en_stem="The Polavaram National Irrigation Project on the river Godavari, declared a National Project under the Andhra Pradesh Reorganisation Act, 2014, has raised inter-state submergence concerns primarily in which neighboring States?",
        ta_stem="ஆந்திரப் பிரதேச மறுசீரமைப்புச் சட்டம் 2014-ன் கீழ் தேசியத் திட்டமாக அறிவிக்கப்பட்ட கோதாவரி நதியின் மீதான போலவரம் தேசிய நீர்ப்பாசனத் திட்டம், நீரில் மூழ்குதல் தொடர்பான பிரச்சனைகளை முதன்மையாக எந்த அண்டை மாநிலங்களில் ஏற்படுத்தியுள்ளது?",
        en_a="Tamil Nadu and Kerala", ta_a="தமிழ்நாடு மற்றும் கேரளா",
        en_b="Odisha and Chhattisgarh (along with Telangana)", ta_b="ஒடிசா மற்றும் சத்தீஸ்கர் (மற்றும் தெலுங்கானா)",
        en_c="Karnataka and Goa", ta_c="கர்நாடகா மற்றும் கோவா",
        en_d="West Bengal and Bihar", ta_d="மேற்கு வங்கம் மற்றும் பீகார்",
        correct_key="B",
        exp_en="The Polavaram Project in Andhra Pradesh has raised serious inter-state concerns regarding backwater flooding and submergence of tribal lands in Odisha (Malkangiri district), Chhattisgarh (Sukma district), and parts of Telangana (Khammam/Bhadradri Kothagudem).",
        exp_ta="ஆந்திராவில் உள்ள போலவரம் திட்டம், ஒடிசா (மல்காங்கிரி), சத்தீஸ்கர் (சுக்மா) மற்றும் தெலுங்கானாவின் பழங்குடியின நிலங்கள் நீரில் மூழ்குவது தொடர்பான கடுமையான மாநிலங்களுக்கு இடையேயான கவலைகளை எழுப்பியுள்ளது.",
        why_a_en="Option A is completely outside the Godavari basin.",
        why_a_ta="விருப்பம் A கோதாவரி வடிநிலத்திற்கு முற்றிலும் வெளியே உள்ளது.",
        why_b_en="Option B correctly identifies the affected riparian states: Odisha, Chhattisgarh, and Telangana.",
        why_b_ta="விருப்பம் B பாதிக்கப்பட்ட மாநிலங்களான ஒடிசா, சத்தீஸ்கர் மற்றும் தெலுங்கானாவைச் சரியாகக் காட்டுகிறது.",
        why_c_en="Option C is outside the Godavari project area.",
        why_c_ta="விருப்பம் C திட்டப் பகுதிக்கு வெளியே உள்ளது.",
        why_d_en="Option D is incorrect.",
        why_d_ta="விருப்பம் D தவறானது.",
        tip_en="Polavaram Project = Godavari river in Andhra Pradesh. Backwater submergence disputes with Odisha, Chhattisgarh, Telangana.",
        tip_ta="போலவரம் திட்டம் = ஆந்திராவில் கோதாவரி நதி. ஒடிசா, சத்தீஸ்கர், தெலுங்கானாவுடன் நீரில் மூழ்குதல் தகராறுகள்.",
        fact_en="Section 90 of the Andhra Pradesh Reorganisation Act, 2014 declared Polavaram to be a National Project, making the Central Government responsible for its execution.",
        fact_ta="ஆந்திர மறுசீரமைப்புச் சட்டம் 2014 பிரிவு 90 போலவரத்தை ஒரு தேசியத் திட்டமாக அறிவித்து, அதை நிறைவேற்றும் பொறுப்பை மத்திய அரசிடம் ஒப்படைத்தது."
    ))

    # 090 - Key C (Medium)
    qs.append(make_q(
        num=90, diff="Medium", qtype="Concept MCQ", subtopic="Inter-State River Water Disputes",
        en_stem="The historic Parambikulam-Aliyar Project (PAP) agreement, signed in May 1970 with retrospective effect from 1958, is an inter-state river water sharing accord between which two States?",
        ta_stem="1958 முதல் முன் ரெட்ரோஸ்பெக்டிவ் விளைவுடன் மே 1970 இல் கையெழுத்தான வரலாற்றுச் சிறப்புமிக்க பரம்பிக்குளம்-ஆழியாறு திட்டம் (PAP) ஒப்பந்தம் எந்த இரண்டு மாநிலங்களுக்கு இடையேயான நதிநீர் பகிர்வு ஒப்பந்தமாகும்?",
        en_a="Karnataka and Andhra Pradesh", ta_a="கர்நாடகா மற்றும் ஆந்திரப் பிரதேசம்",
        en_b="Maharashtra and Goa", ta_b="மகாராஷ்டிரா மற்றும் கோவா",
        en_c="Tamil Nadu and Kerala", ta_c="தமிழ்நாடு மற்றும் கேரளா",
        en_d="Odisha and Andhra Pradesh", ta_d="ஒடிசா மற்றும் ஆந்திரப் பிரதேசம்",
        correct_key="C",
        exp_en="The Parambikulam-Aliyar Project (PAP) agreement was signed on May 29, 1970 between Tamil Nadu (Chief Minister M. Karunanidhi) and Kerala (Chief Minister C. Achutha Menon), regulating the diversion and sharing of water from west-flowing rivers to the drought-prone Coimbatore and Tiruppur regions.",
        exp_ta="பரம்பிக்குளம்-ஆழியாறு திட்டம் (PAP) ஒப்பந்தம் மே 29, 1970 அன்று தமிழ்நாடு (முதலமைச்சர் மு. கருணாநிதி) மற்றும் கேரளா (முதலமைச்சர் சி. அச்சுத மேனன்) இடையே கையெழுத்தானது; இது மேற்கு நோக்கிப் பாயும் நதிகளிலிருந்து வறண்ட கோவை மற்றும் திருப்பூர் பகுதிகளுக்கு நீரைப் பகிர்வதை ஒழுங்குபடுத்துகிறது.",
        why_a_en="Option A is incorrect.",
        why_a_ta="விருப்பம் A தவறானது.",
        why_b_en="Option B is incorrect.",
        why_b_ta="விருப்பம் B தவறானது.",
        why_c_en="Option C is correct; PAP is an inter-state pact between Tamil Nadu and Kerala.",
        why_c_ta="விருப்பம் C சரியானது; PAP என்பது தமிழ்நாடு மற்றும் கேரளா இடையேயான ஒப்பந்தம்.",
        why_d_en="Option D is incorrect.",
        why_d_ta="விருப்பம் D தவறானது.",
        tip_en="PAP Agreement (1970) = Tamil Nadu and Kerala. Inter-basin transfer of west-flowing rivers.",
        tip_ta="PAP ஒப்பந்தம் (1970) = தமிழ்நாடு மற்றும் கேரளா. மேற்கு நோக்கிப் பாயும் நதிகளின் வடிநிலங்களுக்கு இடையேயான நீர் மாற்றம்.",
        fact_en="The PAP integrates eight rivers (six on the Anamalai hills and two on the plains) across both states, generating hydroelectric power and irrigation.",
        fact_ta="PAP திட்டம் இரு மாநிலங்களிலும் உள்ள எட்டு நதிகளை ஒருங்கிணைத்து நீர்மின் உற்பத்தி மற்றும் பாசன வசதியை வழங்குகிறது."
    ))

    # 091 - Key D (Hard)
    qs.append(make_q(
        num=91, diff="Hard", qtype="Concept MCQ", subtopic="Inter-State River Water Disputes",
        en_stem="The Cauvery Water Management Authority (CWMA) and the Cauvery Water Regulation Committee (CWRC) were formally constituted by the Central Government on June 1, 2018 under which statutory provision?",
        ta_stem="காவிரி நீர் மேலாண்மை ஆணையம் (CWMA) மற்றும் காவிரி நீர் ஒழுங்குமுறைக் குழு (CWRC) ஆகியவை ஜூன் 1, 2018 அன்று மத்திய அரசால் எந்த சட்ட விதியின் கீழ் முறைப்படி அமைக்கப்பட்டன?",
        en_a="Article 263 of the Indian Constitution", ta_a="இந்திய அரசியலமைப்பின் சரத்து 263",
        en_b="Section 16 of the States Reorganisation Act, 1956", ta_b="மாநில மறுசீரமைப்புச் சட்டம் 1956-ன் பிரிவு 16",
        en_c="Section 3 of the Dam Safety Act, 2021", ta_c="அணை பாதுகாப்புச் சட்டம் 2021-ன் பிரிவு 3",
        en_d="Section 6A of the Inter-State River Water Disputes Act, 1956 (pursuant to the Supreme Court February 2018 verdict)", ta_d="1956-ஆம் ஆண்டின் மாநிலங்களுக்கு இடையேயான நதிநீர் தகராறுகள் சட்டத்தின் பிரிவு 6A (உச்ச நீதிமன்றத்தின் பிப்ரவரி 2018 தீர்ப்பின்படி)",
        correct_key="D",
        exp_en="Pursuant to the Supreme Court's final directive on February 16, 2018, the Central Government notified the Cauvery Water Management Scheme, 2018 on June 1, 2018 under Section 6A of the Inter-State River Water Disputes Act, 1956, establishing the CWMA and CWRC.",
        exp_ta="உச்ச நீதிமன்றத்தின் பிப்ரவரி 16, 2018 உத்தரவைத் தொடர்ந்து, மத்திய அரசு ஜூன் 1, 2018 அன்று 1956-ஆம் ஆண்டின் மாநிலங்களுக்கு இடையேயான நதிநீர் தகராறுகள் சட்டத்தின் பிரிவு 6A-ன் கீழ் காவிரி நீர் மேலாண்மைத் திட்டத்தை அறிவித்து, CWMA மற்றும் CWRC ஆகியவற்றை அமைத்தது.",
        why_a_en="Option A is Inter-State Council.",
        why_a_ta="விருப்பம் A மாநிலங்களுக்கு இடையேயான கவுன்சில்.",
        why_b_en="Option B is Zonal Councils.",
        why_b_ta="விருப்பம் B மண்டல கவுன்சில்கள்.",
        why_c_en="Option C was enacted years later in 2021.",
        why_c_ta="விருப்பம் C 2021 இல் பின்னர் இயற்றப்பட்டது.",
        why_d_en="Option D is correct; Section 6A of IRWD Act governs schemes to give effect to tribunal decisions.",
        why_d_ta="விருப்பம் D சரியானது; தீர்ப்பாயத் தீர்ப்புகளை அமல்படுத்தும் திட்டங்களுக்கு IRWD சட்டத்தின் பிரிவு 6A பொருந்தும்.",
        tip_en="CWMA and CWRC were notified on 1 June 2018 under Section 6A of the IRWD Act, 1956.",
        tip_ta="CWMA மற்றும் CWRC ஆகியவை 1 ஜூன் 2018 அன்று IRWD சட்டம் 1956 பிரிவு 6A-ன் கீழ் அறிவிக்கப்பட்டன.",
        fact_en="Section 6A enables the Central Government to frame a scheme for establishing authorities to implement and monitor tribunal awards.",
        fact_ta="பிரிவு 6A தீர்ப்பாயத் தீர்ப்புகளைச் செயல்படுத்தவும் கண்காணிக்கவும் அதிகார அமைப்புகளை நிறுவுவதற்கான திட்டத்தை உருவாக்க மத்திய அரசுக்கு அதிகாரம் அளிக்கிறது."
    ))

    # 092 - Key A (Hard)
    qs.append(make_q(
        num=92, diff="Hard", qtype="Concept MCQ", subtopic="Inter-State River Water Disputes",
        en_stem="What is the tenure and qualifications required for the Chairman of the Cauvery Water Management Authority (CWMA) as per the 2018 Scheme?",
        ta_stem="2018 திட்டத்தின்படி காவிரி நீர் மேலாண்மை ஆணையத்தின் (CWMA) தலைவருக்குத் தேவையான பதவிக்காலம் மற்றும் தகுதிகள் என்ன?",
        en_a="A senior and eminent engineer with experience in water resource management, appointed for a term of 5 years or until age 65", ta_a="நீர் வள மேலாண்மையில் அனுபவமிக்க மூத்த பொறியாளர், 5 ஆண்டுகள் அல்லது 65 வயது வரை நியமிக்கப்படுவார்",
        en_b="A sitting Chief Minister of one of the riparian states appointed for one year by rotation", ta_b="வடிநில மாநிலங்களில் ஒன்றின் பதவியில் உள்ள முதலமைச்சர் சுழற்சி முறையில் ஒரு வருடத்திற்கு",
        en_c="A retired High Court judge appointed for life", ta_c="வாழ்நாள் முழுவதும் நியமிக்கப்படும் ஓய்வுபெற்ற உயர் நீதிமன்ற நீதிபதி",
        en_d="A serving Union Cabinet Minister holding the Jal Shakti portfolio", ta_d="ஜல் சக்தி துறையை வகிக்கும் பதவியில் உள்ள மத்திய அமைச்சரவை அமைச்சர்",
        correct_key="A",
        exp_en="Under the Cauvery Water Management Scheme, 2018, the Chairman of the CWMA shall be an eminent engineer with wide experience in water resource handling, holding the rank of Secretary or Additional Secretary to the Government of India, appointed for a tenure not exceeding 5 years or until attaining 65 years of age.",
        exp_ta="காவிரி நீர் மேலாண்மைத் திட்டம் 2018-ன் படி, CWMA தலைவர் இந்திய அரசின் செயலாளர் அல்லது கூடுதல் செயலாளர் அந்தஸ்தில் உள்ள அனுபவமிக்க மூத்த பொறியாளராக இருக்க வேண்டும்; இவர் 5 ஆண்டுகள் அல்லது 65 வயது வரை பதவியில் இருப்பார்.",
        why_a_en="Option A accurately states the qualifications and tenure under the 2018 scheme.",
        why_a_ta="விருப்பம் A 2018 திட்டத்தின் கீழான தகுதிகள் மற்றும் பதவிக்காலத்தை துல்லியமாகக் கூறுகிறது.",
        why_b_en="Option B is incorrect; Chief Ministers are not chairmen of river management authorities.",
        why_b_ta="விருப்பம் B தவறானது; முதலமைச்சர்கள் இதன் தலைவர்கள் அல்ல.",
        why_c_en="Option C is incorrect; it is a technical engineer post, not a judicial post.",
        why_c_ta="விருப்பம் C தவறானது; இது தொழில்நுட்பப் பதவி, நீதித்துறைப் பதவி அல்ல.",
        why_d_en="Option D is incorrect.",
        why_d_ta="விருப்பம் D தவறானது.",
        tip_en="CWMA Chairman = Eminent Engineer (Secretary/Addl Secretary rank), 5 years or 65 years age limit.",
        tip_ta="CWMA தலைவர் = மூத்த பொறியாளர் (செயலாளர் அந்தஸ்து), 5 ஆண்டுகள் அல்லது 65 வயது வரை.",
        fact_en="The CWMA includes one representative from each of the four riparian states/UTs (Tamil Nadu, Karnataka, Kerala, Puducherry) and central representatives.",
        fact_ta="CWMA-ல் நான்கு வடிநில மாநிலங்கள்/யூ.பி ஆகியவற்றின் தலா ஒரு பிரதிநிதியும் மத்திய அரசின் பிரதிநிதிகளும் இடம்பெற்றுள்ளனர்."
    ))

    # 093 - Key B (Hard)
    qs.append(make_q(
        num=93, diff="Hard", qtype="Concept MCQ", subtopic="Inter-State Trade and Commerce",
        en_stem="Which article of the Constitution protects existing laws and laws providing for State monopolies (nationalization of road transport, railways, etc.) from being challenged as violative of Article 301 and Article 303?",
        ta_stem="சரத்துகள் 301 மற்றும் 303-ஐ மீறுவதாக சவால் செய்யப்படுவதிலிருந்து ஏற்கனவே நடைமுறையில் உள்ள சட்டங்களையும், அரசு ஏகபோகங்களை (சாலைப் போக்குவரத்து, ரயில்வே தேசியமயமாக்கல் போன்றவை) வழங்கும் சட்டங்களையும் பாதுகாக்கும் அரசியலமைப்புச் சரத்து எது?",
        en_a="Article 301 Proviso", ta_a="சரத்து 301 வரம்புரை",
        en_b="Article 305", ta_b="சரத்து 305",
        en_c="Article 306 (Repealed)", ta_c="சரத்து 306 (நீக்கப்பட்டது)",
        en_d="Article 308", ta_d="சரத்து 308",
        correct_key="B",
        exp_en="Article 305 specifically saves existing laws and laws creating State monopolies from the operation of Articles 301 and 303. Thus, if a State Government or the Union Government creates an exclusive monopoly in running passenger buses or railways to the exclusion of private citizens, it cannot be challenged under Article 301.",
        exp_ta="சரத்து 305 நடைமுறையில் உள்ள சட்டங்களையும், அரசு ஏகபோகங்களை உருவாக்கும் சட்டங்களையும் சரத்துகள் 301 மற்றும் 303-ன் செயல்பாட்டிலிருந்து பாதுகாக்கிறது. எனவே பேருந்துகள் அல்லது ரயில்வேயை அரசு மட்டுமே இயக்கும் போது அதை சரத்து 301-ன் கீழ் சவால் செய்ய முடியாது.",
        why_a_en="Option A is incorrect; Article 301 has no separate saving proviso for state monopolies.",
        why_a_ta="விருப்பம் A தவறானது.",
        why_b_en="Option B is correct; Article 305 protects existing laws and state monopolies.",
        why_b_ta="விருப்பம் B சரியானது; சரத்து 305 அரசு ஏகபோகங்களை பாதுகாக்கிறது.",
        why_c_en="Option C was repealed by the 7th Amendment, 1956.",
        why_c_ta="விருப்பம் C 7-வது திருத்தத்தால் நீக்கப்பட்டது.",
        why_d_en="Option D begins Part XIV (Services under the Union and States).",
        why_d_ta="விருப்பம் D பகுதி XIV-ன் தொடக்கமாகும்.",
        tip_en="Article 305 = Saving of existing laws and laws creating State Monopolies (inserted/amended by 4th Amendment, 1955).",
        tip_ta="சரத்து 305 = நடைமுறையில் உள்ள சட்டங்கள் மற்றும் அரசு ஏகபோகங்களைப் பாதுகாத்தல் (4-வது திருத்தம், 1955).",
        fact_en="Article 305 was amended by the 4th Constitutional Amendment Act, 1955 to protect socialist nationalisation schemes from judicial invalidation.",
        fact_ta="சோசலிச தேசியமயமாக்கல் திட்டங்களை நீதிமன்ற ரத்து செய்வதிலிருந்து பாதுகாக்க 1955-ல் 4-வது திருத்தத்தின் மூலம் சரத்து 305 திருத்தப்பட்டது."
    ))

    # 094 - Key C (Hard)
    qs.append(make_q(
        num=94, diff="Hard", qtype="Concept MCQ", subtopic="Inter-State Trade and Commerce",
        en_stem="When a State Legislature enacts a law under Article 304(b) imposing reasonable restrictions on inter-state trade in the public interest with Presidential sanction, who has the final authority to determine whether the restriction is actually 'reasonable'?",
        ta_stem="சரத்து 304(b)-ன் கீழ் குடியரசுத் தலைவரின் அனுமதியுடன் பொது நலன் கருதி மாநிலங்களுக்கு இடையேயான வர்த்தகத்தின் மீது ஒரு மாநில சட்டமன்றம் நியாயமான கட்டுப்பாடுகளை விதிக்கும் போது, அந்தக் கட்டுப்பாடு உண்மையில் 'நியாயமானதா' என்பதைத் தீர்மானிக்கும் இறுதி அதிகாரம் யாரிடம் உள்ளது?",
        en_a="The Governor of that State alone", ta_a="அந்த மாநில ஆளுநரிடம் மட்டுமே",
        en_b="The Speaker of the State Legislative Assembly", ta_b="மாநில சட்டமன்ற சபாநாயகரிடம்",
        en_c="The Courts of Law (Judicial Review by Supreme Court and High Courts)", ta_c="நீதிமன்றங்கள் (உச்ச நீதிமன்றம் மற்றும் உயர் நீதிமன்றங்களின் நீதித்துறை மறுஆய்வு)",
        en_d="The Inter-State Council Standing Committee exclusively", ta_d="மாநிலங்களுக்கு இடையேயான கவுன்சில் நிலைக்குழுவிடம் மட்டுமே",
        correct_key="C",
        exp_en="Under Article 304(b), the requirement of 'reasonable restrictions in the public interest' is a justiciable constitutional condition. The courts (Supreme Court and High Courts) possess full judicial review authority to examine whether a restriction imposed by state law is truly reasonable and in the public interest.",
        exp_ta="சரத்து 304(b)-ன் கீழ், 'பொது நலனுக்கான நியாயமான கட்டுப்பாடுகள்' என்பது நீதிமன்ற ஆய்வுக்குட்பட்ட ஒரு நிபந்தனையாகும். மாநிலச் சட்டம் விதிக்கும் கட்டுப்பாடு உண்மையில் நியாயமானதா என்பதை ஆராயும் முழு நீதித்துறை மறுஆய்வு அதிகாரம் நீதிமன்றங்களுக்கு உண்டு.",
        why_a_en="Option A is incorrect; Governor's assent does not immunize a law from reasonableness tests.",
        why_a_ta="விருப்பம் A தவறானது; ஆளுநர் ஒப்புதல் சட்டத்தை நீதிமன்ற ஆய்விலிருந்து காப்பாற்றாது.",
        why_b_en="Option B is incorrect; Speaker has no judicial review power.",
        why_b_ta="விருப்பம் B தவறானது; சபாநாயகருக்கு நீதி மறுஆய்வு அதிகாரம் இல்லை.",
        why_c_en="Option C is correct; 'reasonableness' is always subject to judicial determination by the courts.",
        why_c_ta="விருப்பம் C சரியானது; 'நியாயத்தன்மை' எப்போதும் நீதிமன்றங்களின் முடிவுக்கு உட்பட்டது.",
        why_d_en="Option D is incorrect; ISC is not a judicial organ.",
        why_d_ta="விருப்பம் D தவறானது; கவுன்சில் நீதித்துறை அமைப்பு அல்ல.",
        tip_en="Two conditions under Article 304(b): 1. Previous sanction of the President (Procedural); 2. Reasonable restrictions in public interest (Substantive & Justiciable in court).",
        tip_ta="சரத்து 304(b)-ன் கீழ் 2 நிபந்தனைகள்: 1. குடியரசுத் தலைவரின் முன் அனுமதி; 2. பொது நலனுக்கான நியாயமான கட்டுப்பாடு (நீதிமன்ற ஆய்வுக்குட்பட்டது).",
        fact_en="In Tika Ramji v. State of UP (1956), the Supreme Court upheld state regulation of sugarcane supply as a reasonable restriction in public interest under Article 304(b).",
        fact_ta="டிகா ராம்ஜி எதிர் உ.பி மாநிலம் (1956) வழக்கில், கரும்பு விநியோகத்தை ஒழுங்குபடுத்தும் மாநிலச் சட்டம் நியாயமான கட்டுப்பாடு என உறுதி செய்யப்பட்டது."
    ))

    # 095 - Key D (Hard)
    qs.append(make_q(
        num=95, diff="Hard", qtype="Concept MCQ", subtopic="Inter-State Trade and Commerce",
        en_stem="In State of Tamil Nadu v. Sanjeetha Trading Co. (1994), what did the Supreme Court hold regarding Tamil Nadu's total prohibition on the export of timber outside the State?",
        ta_stem="தமிழ்நாடு மாநிலம் எதிர் சஞ்சீதா டிரேடிங் கோ. (1994) வழக்கில், மாநிலத்திற்கு வெளியே மரம் ஏற்றுமதி செய்வதற்கு தமிழ்நாடு அரசு விதித்த முழுமையான தடையை உச்ச நீதிமன்றம் எவ்வாறு உறுதி செய்தது?",
        en_a="Total ban was declared unconstitutional because freedom of trade under Article 301 is absolute", ta_a="சரத்து 301-ன் கீழான வர்த்தக சுதந்திரம் முழுமையானது என்பதால் முழுத் தடை அரசியலமைப்பிற்கு முரணானது என அறிவிக்கப்பட்டது",
        en_b="Timber was held to be a prohibited narcotic drug outside Part XIII", ta_b="மரம் என்பது பகுதி XIII-க்கு வெளியே உள்ள தடைசெய்யப்பட்ட போதைப்பொருள் எனக் கருதப்பட்டது",
        en_c="The ban was struck down because only Parliament can regulate forest produce", ta_c="பாராளுமன்றம் மட்டுமே வனப் பொருட்களை ஒழுங்குபடுத்த முடியும் என்பதால் தடை ரத்து செய்யப்பட்டது",
        en_d="A complete ban can constitute a 'reasonable restriction' under Article 304(b) in exceptional circumstances, to prevent raw material starvation of local industries and conserve forest ecology", ta_d="உள்ளூர் தொழில்களுக்கு மூலப்பொருள் தட்டுப்பாடு ஏற்படுவதைத் தடுக்கவும் வனச் சூழலியலைப் பாதுகாக்கவும் விதிவிலக்கான சூழ்நிலைகளில் முழுமையான தடையும் சரத்து 304(b)-ன் கீழ் ஒரு 'நியாயமான கட்டுப்பாடாக' இருக்க முடியும்",
        correct_key="D",
        exp_en="In Sanjeetha Trading Co. (1994), the Supreme Court held that the word 'restriction' in Article 304(b) can, in appropriate circumstances, include complete 'prohibition'. Tamil Nadu's ban on exporting timber was upheld as a reasonable restriction in the public interest to protect local wood-based industries and preserve ecological balance.",
        exp_ta="சஞ்சீதா டிரேடிங் கோ. (1994) வழக்கில் உச்ச நீதிமன்றம், சரத்து 304(b)-ல் உள்ள 'கட்டுப்பாடு' என்ற சொல் பொருத்தமான சூழ்நிலைகளில் 'முழுமையான தடையையும்' உள்ளடக்கும் என்று தீர்ப்பளித்தது. உள்ளூர் தொழில்களைப் பாதுகாக்கவும் சுற்றுச்சூழல் சமநிலையைப் பேணவும் தமிழ்நாடு விதித்த மரம் ஏற்றுமதித் தடை செல்லும் என உறுதி செய்யப்பட்டது.",
        why_a_en="Option A is incorrect; Article 301 is not absolute.",
        why_a_ta="விருப்பம் A தவறானது; சரத்து 301 முழுமையானது அல்ல.",
        why_b_en="Option B is absurd.",
        why_b_ta="விருப்பம் B தவறானது.",
        why_c_en="Option C is incorrect; Forests are Entry 17A List III (Concurrent).",
        why_c_ta="விருப்பம் C தவறானது; காடுகள் பொதுப்பட்டியல் துறை.",
        why_d_en="Option D is the landmark holding that 'restriction' includes total 'prohibition' if justified by public interest.",
        why_d_ta="விருப்பம் D சரியானது; பொது நலன் தேவைப்பட்டால் 'கட்டுப்பாடு' என்பது 'முழுத் தடையையும்' குறிக்கும் என்று இவ்வழக்கு தீர்ப்பளித்தது.",
        tip_en="Sanjeetha Trading Co. (1994): 'Restriction' under Article 304(b) can include total 'Prohibition' in public interest.",
        tip_ta="சஞ்சீதா டிரேடிங் கோ. (1994): சரத்து 304(b)-ன் கீழான 'கட்டுப்பாடு' என்பது பொது நலன் கருதி 'முழுத் தடையையும்' உள்ளடக்கும்.",
        fact_en="This was an extension of the principle first laid down in Narendra Kumar v. Union of India (1960) under Article 19(6).",
        fact_ta="இது நரேந்திர குமார் வழக்கில் (1960) சரத்து 19(6)-ன் கீழ் வகுக்கப்பட்ட கொள்கையின் விரிவாக்கமாகும்."
    ))

    # 096 - Key D (Hard)
    qs.append(make_q(
        num=96, diff="Hard", qtype="Concept MCQ", subtopic="Inter-State River Water Disputes",
        en_stem="In State of Andhra Pradesh v. State of Maharashtra (2013), how did the Supreme Court reconcile its Article 131 jurisdiction with the bar under Article 262 and Section 11 of the IRWD Act?",
        ta_stem="ஆந்திரப் பிரதேச மாநிலம் எதிர் மகாராஷ்டிர மாநிலம் (2013) வழக்கில், சரத்து 262 மற்றும் IRWD சட்டத்தின் பிரிவு 11-ன் கீழான தடையை தனது சரத்து 131 அதிகார வரம்புடன் உச்ச நீதிமன்றம் எவ்வாறு சமரசம் செய்தது?",
        en_a="By declaring Section 11 completely null and void", ta_a="பிரிவு 11-ஐ முற்றிலும் செல்லாது என்று அறிவிப்பதன் மூலம்",
        en_b="By delegating its Article 131 powers to the Union Home Ministry", ta_b="தனது சரத்து 131 அதிகாரங்களை மத்திய உள்துறை அமைச்சகத்திடம் ஒப்படைப்பதன் மூலம்",
        en_c="By ruling that the President of India must hear all suits under Article 131", ta_c="சரத்து 131-ன் கீழான அனைத்து வழக்குகளையும் குடியரசுத் தலைவரே விசாரிக்க வேண்டும் என்று தீர்ப்பளிப்பதன் மூலம்",
        en_d="By holding that while water-sharing disputes are barred from Article 131, disputes regarding the breach of an existing inter-state agreement or construction of an unapproved project that infringes legal rights can be entertained under Article 131", ta_d="நதிநீர் பகிர்வு தகராறுகள் சரத்து 131-லிருந்து தடை செய்யப்பட்டிருந்தாலும், ஏற்கனவே உள்ள ஒப்பந்தத்தை மீறுவது அல்லது சட்ட உரிமைகளைப் பாதிக்கும் அங்கீகரிக்கப்படாத திட்டத்தை அமைப்பது தொடர்பான தகராறுகளை சரத்து 131-ன் கீழ் விசாரிக்க முடியும் என்று தீர்ப்பளிப்பதன் மூலம்",
        correct_key="D",
        exp_en="The Supreme Court clarified that where the dispute does not involve determining riparian water shares (which is for the water tribunal under Art 262), but concerns the enforcement of legal rights under an already adjudicated agreement or breach of terms by building an unapproved barrage, an original suit under Article 131 is maintainable.",
        exp_ta="நதிநீர் பங்கீட்டை நிர்ணயிப்பது தீர்ப்பாயத்தின் வேலை என்றாலும், ஏற்கனவே உள்ள ஒப்பந்தத்தை மீறி புதிய அணையைக் கட்டுவது போன்ற சட்டப்பூர்வ உரிமைகள் மீறப்படும் போது, சரத்து 131-ன் கீழான அசல் வழக்கு செல்லுபடியாகும் என்று உச்ச நீதிமன்றம் தெளிவுபடுத்தியது.",
        why_a_en="Option A is incorrect; Section 11 was not struck down.",
        why_a_ta="விருப்பம் A தவறானது; பிரிவு 11 ரத்து செய்யப்படவில்லை.",
        why_b_en="Option B is incorrect; judicial power cannot be delegated to the executive.",
        why_b_ta="விருப்பம் B தவறானது; நீதித்துறை அதிகாரத்தை நிர்வாகத்திடம் ஒப்படைக்க முடியாது.",
        why_c_en="Option C is incorrect.",
        why_c_ta="விருப்பம் C தவறானது.",
        why_d_en="Option D accurately captures the legal distinction drawn by the Supreme Court.",
        why_d_ta="விருப்பம் D உச்ச நீதிமன்றம் சுட்டிக்காட்டிய சட்டரீதியான வேறுபாட்டை துல்லியமாகக் காட்டுகிறது.",
        tip_en="Article 262 bars water apportionment disputes. Article 131 can hear legal enforcement of existing water pacts.",
        tip_ta="சரத்து 262 நீர் பங்கீட்டுத் தகராறுகளைத் தடுக்கிறது. ஆனால் சரத்து 131 ஒப்பந்த மீறல் தொடர்பான சட்ட வழக்குகளை விசாரிக்கலாம்.",
        fact_en="This distinction allowed Andhra Pradesh's challenge against Maharashtra's Babhali Barrage to be heard on merits under Article 131.",
        fact_ta="இந்த வேறுபாடே பாப்லி அணைக்கட்டுக்கு எதிரான ஆந்திராவின் வழக்கை சரத்து 131-ன் கீழ் தகுதி அடிப்படையில் விசாரிக்க அனுமதித்தது."
    ))

    # 097 - Key A (Hard)
    qs.append(make_q(
        num=97, diff="Hard", qtype="Concept MCQ", subtopic="Inter-State Council",
        en_stem="Long before the general Inter-State Council was established in 1990, the President had established several subject-specific councils under Article 263(c). Which of the following was the FIRST council established under Article 263?",
        ta_stem="1990 இல் பொதுவான மாநிலங்களுக்கு இடையேயான கவுன்சில் நிறுவப்படுவதற்கு நீண்ட காலத்திற்கு முன்பே, குடியரசுத் தலைவர் சரத்து 263(c)-ன் கீழ் பல துறைசார் கவுன்சில்களை நிறுவினார். சரத்து 263-ன் கீழ் நிறுவப்பட்ட முதல் கவுன்சில் எது?",
        en_a="Central Council of Health (established in August 1952)", ta_a="மத்திய சுகாதார கவுன்சில் (ஆகஸ்ட் 1952-ல் நிறுவப்பட்டது)",
        en_b="Central Council of Local Self-Government (established in September 1954)", ta_b="மத்திய உள்ளாட்சி கவுன்சில் (செப்டம்பர் 1954-ல் நிறுவப்பட்டது)",
        en_c="Transport Development Council (established in 1958)", ta_c="போக்குவரத்து வளர்ச்சிக் கவுன்சில் (1958-ல் நிறுவப்பட்டது)",
        en_d="National Integration Council (established in 1961)", ta_d="தேசிய ஒருமைப்பாட்டுக் கவுன்சில் (1961-ல் நிறுவப்பட்டது)",
        correct_key="A",
        exp_en="The very first council established under Article 263 was the Central Council of Health, constituted by a Presidential Order in August 1952 to consider and recommend broad outlines of policy relating to health administration across States.",
        exp_ta="சரத்து 263-ன் கீழ் முதன்முதலில் நிறுவப்பட்ட அமைப்பு மத்திய சுகாதார கவுன்சில் (Central Council of Health) ஆகும்; இது மாநிலங்களிடையே சுகாதார நிர்வாகக் கொள்கைகளைப் பரிந்துரைக்க ஆகஸ்ட் 1952 இல் குடியரசுத் தலைவர் ஆணை மூலம் அமைக்கப்பட்டது.",
        why_a_en="Option A is correct; Central Council of Health was established in August 1952.",
        why_a_ta="விருப்பம் A சரியானது; மத்திய சுகாதார கவுன்சில் ஆகஸ்ட் 1952 இல் அமைக்கப்பட்டது.",
        why_b_en="Option B was established later in September 1954 under Article 263.",
        why_b_ta="விருப்பம் B செப்டம்பர் 1954 இல் பின்னர் அமைக்கப்பட்டது.",
        why_c_en="Option C was created later in 1958.",
        why_c_ta="விருப்பம் C 1958 இல் உருவாக்கப்பட்டது.",
        why_d_en="Option D is an extra-constitutional body set up in 1961.",
        why_d_ta="விருப்பம் D 1961 இல் அமைக்கப்பட்ட அரசியலமைப்பு சாரா அமைப்பு.",
        tip_en="Article 263 Subject Councils: 1. Central Council of Health (1952); 2. Central Council of Local Self-Govt (1954); 3. Four Regional Sales Tax Councils.",
        tip_ta="சரத்து 263 துறைசார் கவுன்சில்கள்: 1. மத்திய சுகாதார கவுன்சில் (1952); 2. மத்திய உள்ளாட்சி கவுன்சில் (1954); 3. நான்கு பிராந்திய விற்பனை வரி கவுன்சில்கள்.",
        fact_en="Article 263 does not mandate only ONE council; the President can establish multiple single-purpose councils under its clauses.",
        fact_ta="சரத்து 263 ஒரே ஒரு கவுன்சிலை மட்டுமே அனுமதிக்கவில்லை; குடியரசுத் தலைவர் குறிப்பிட்ட நோக்கங்களுக்காக பல கவுன்சில்களை அமைக்கலாம்."
    ))

    # 098 - Key B (Hard)
    qs.append(make_q(
        num=98, diff="Hard", qtype="Concept MCQ", subtopic="Inter-State Council",
        en_stem="What is the constitutional quorum and decision-making rule governing meetings of the full Inter-State Council?",
        ta_stem="முழு மாநிலங்களுக்கு இடையேயான கவுன்சிலின் கூட்டங்களை நிர்வகிக்கும் அரசியலமைப்பு குறைந்தபட்ச வருகை (Quorum) மற்றும் முடிவெடுக்கும் விதி என்ன?",
        en_a="Quorum is 5 members, and decisions are taken by a two-thirds majority vote", ta_a="குறைந்தபட்ச வருகை 5 உறுப்பினர்கள், முடிவுகள் மூன்றில் இரண்டு பங்கு பெரும்பான்மை வாக்குகளால் எடுக்கப்படுகின்றன",
        en_b="Quorum is 10 members (including at least 5 Chief Ministers), and all decisions are taken by consensus without voting", ta_b="குறைந்தபட்ச வருகை 10 உறுப்பினர்கள் (குறைந்தது 5 முதலமைச்சர்கள் உட்பட), மற்றும் அனைத்து முடிவுகளும் வாக்கெடுப்பின்றி ஒருமித்த கருத்தின் (Consensus) மூலம் எடுக்கப்படுகின்றன",
        en_c="Quorum is 50% of total strength, and Prime Minister exercises a casting vote", ta_c="குறைந்தபட்ச வருகை 50% உறுப்பினர்கள், பிரதமர் தனது தீர்மானிக்கும் வாக்கை (Casting vote) பயன்படுத்துகிறார்",
        en_d="Quorum is not required, and decisions are determined by the Cabinet Secretary", ta_d="குறைந்தபட்ச வருகை தேவையில்லை, முடிவுகள் அமைச்சரவைச் செயலாளரால் தீர்மானிக்கப்படுகின்றன",
        correct_key="B",
        exp_en="As per the rules of procedure of the Inter-State Council, the quorum for a meeting of the Council is ten members, including at least five Chief Ministers of States. All questions are decided by consensus, and no formal voting takes place.",
        exp_ta="மாநிலங்களுக்கு இடையேயான கவுன்சிலின் நடைமுறை விதிகளின்படி, கூட்டத்திற்கான குறைந்தபட்ச வருகை (Quorum) 10 உறுப்பினர்கள் ஆகும்; இதில் குறைந்தது 5 மாநில முதலமைச்சர்கள் இடம்பெற வேண்டும். அனைத்து முடிவுகளும் வாக்கெடுப்பு இன்றி ஒருமித்த கருத்தின் (Consensus) அடிப்படையிலேயே எடுக்கப்படுகின்றன.",
        why_a_en="Option A is incorrect.",
        why_a_ta="விருப்பம் A தவறானது.",
        why_b_en="Option B is the exact procedural rule: 10 members (min 5 CMs) + consensus-based decisions.",
        why_b_ta="விருப்பம் B என்பது துல்லியமான விதி: 10 உறுப்பினர்கள் (குறைந்தது 5 முதலமைச்சர்கள்) + ஒருமித்த கருத்து முறை.",
        why_c_en="Option C is incorrect; there is no casting vote because there is no voting.",
        why_c_ta="விருப்பம் C தவறானது; வாக்கெடுப்பே இல்லாததால் தீர்மானிக்கும் வாக்குக்கு இடமில்லை.",
        why_d_en="Option D is incorrect.",
        why_d_ta="விருப்பம் D தவறானது.",
        tip_en="Inter-State Council Quorum = 10 members (minimum 5 Chief Ministers). Decision mode = Consensus (no voting).",
        tip_ta="மாநிலங்களுக்கு இடையேயான கவுன்சில் கோரம் = 10 உறுப்பினர்கள் (குறைந்தது 5 முதலமைச்சர்கள்). முடிவு முறை = ஒருமித்த கருத்து (வாக்கெடுப்பு இல்லை).",
        fact_en="The consensus rule is deliberately designed to foster federal harmony rather than allowing numerical majorities to alienate dissenting States.",
        fact_ta="பெரும்பான்மை வாக்குகள் மூலம் கருத்து வேறுபாடு கொண்ட மாநிலங்களை தனிமைப்படுத்தாமல், கூட்டாட்சி நல்லிணக்கத்தை வளர்ப்பதற்காகவே ஒருமித்த கருத்து விதி வடிவமைக்கப்பட்டது."
    ))

    # 099 - Key C (Hard)
    qs.append(make_q(
        num=99, diff="Hard", qtype="Concept MCQ", subtopic="Constitutional Framework",
        en_stem="Under the Occupational Safety, Health and Working Conditions Code, 2020 (which subsumed the Inter-State Migrant Workmen Act, 1979), how was the definition of an 'Inter-State Migrant Worker' expanded?",
        ta_stem="1979-ஆம் ஆண்டின் மாநிலங்களுக்கு இடையேயான புலம்பெயர்ந்த தொழிலாளர்கள் சட்டத்தை தன்னுள் இணைத்துக் கொண்ட தொழில்சார் பாதுகாப்பு, சுகாதாரம் மற்றும் பணிச்சூழல் குறியீடு 2020-ன் கீழ், 'மாநிலங்களுக்கு இடையேயான புலம்பெயர்ந்த தொழிலாளர்' என்பதன் வரையறை எவ்வாறு விரிவுபடுத்தப்பட்டது?",
        en_a="Restricted only to workers holding a postgraduate degree in engineering", ta_a="பொறியியலில் முதுகலை பட்டம் பெற்ற தொழிலாளர்களுக்கு மட்டுமே கட்டுப்படுத்தப்பட்டது",
        en_b="Limited strictly to government employees on central deputation", ta_b="மத்திய பணிக்கு அனுப்பப்படும் அரசு ஊழியர்களுக்கு மட்டுமே மட்டுப்படுத்தப்பட்டது",
        en_c="Expanded to include workers recruited directly by an employer or coming on their own to another State for employment, earning up to statutory wage ceilings, moving beyond contractor-only recruitment", ta_c="ஒப்பந்ததாரர் மூலம் வரும் தொழிலாளர்களைத் தாண்டி, ஒரு முதலாளியால் நேரடியாக நியமிக்கப்பட்ட அல்லது வேலைக்காகத் தாமாகவே மற்றொரு மாநிலத்திற்கு வரும் குறிப்பிட்ட ஊதிய வரம்பிற்கு உட்பட்ட தொழிலாளர்களையும் உள்ளடக்கும் வகையில் விரிவுபடுத்தப்பட்டது",
        en_d="Abolished entirely, removing all welfare protections for inter-state workers", ta_d="முற்றிலும் ஒழிக்கப்பட்டு, புலம்பெயர்ந்த தொழிலாளர்களுக்கான அனைத்து நலப் பாதுகாப்புகளும் நீக்கப்பட்டன",
        correct_key="C",
        exp_en="Under the 1979 Act, only migrant workers recruited through licensed contractors were protected. The 2020 Code significantly expanded the definition of 'inter-state migrant worker' to cover workers recruited directly by employers, as well as workers who migrate on their own seeking employment in another state, earning up to statutory monthly wage ceilings.",
        exp_ta="1979 சட்டத்தின் கீழ் உரிமம் பெற்ற ஒப்பந்ததாரர்கள் மூலம் வரும் தொழிலாளர்கள் மட்டுமே பாதுகாக்கப்பட்டனர். ஆனால் 2020 புதிய குறியீடு, நேரடியாக நியமிக்கப்படும் தொழிலாளர்களையும், வேலை தேடி தாங்களாகவே மற்றொரு மாநிலத்திற்கு இடம்பெயரும் தொழிலாளர்களையும் உள்ளடக்கி வரையறையை கணிசமாக விரிவுபடுத்தியது.",
        why_a_en="Option A is absurd.",
        why_a_ta="விருப்பம் A தவறானது.",
        why_b_en="Option B is incorrect.",
        why_b_ta="விருப்பம் B தவறானது.",
        why_c_en="Option C is correct; it covers self-migrating and directly recruited workers.",
        why_c_ta="விருப்பம் C சரியானது; இது தாமாக இடம்பெயரும் தொழிலாளர்களையும் நேரடியாக நியமிக்கப்படுபவர்களையும் பாதுகாக்கிறது.",
        why_d_en="Option D is contrary to the welfare enhancement in the Code.",
        why_d_ta="விருப்பம் D நலத்திட்ட விரிவாக்கத்திற்கு எதிரானது.",
        tip_en="OSH Code 2020 expanded migrant worker definition to include self-employed/directly recruited migrants, not just contractor-hired workers.",
        tip_ta="OSH குறியீடு 2020: ஒப்பந்ததாரர்கள் மூலம் வருபவர்கள் மட்டுமன்றி, தாமாக இடம்பெயரும் புலம்பெயர் தொழிலாளர்களையும் பாதுகாக்கிறது.",
        fact_en="The 2020 Code also introduced provisions for a National Migration Portal (e-Shram) and portability of ration cards (One Nation One Ration Card).",
        fact_ta="2020 குறியீடு தேசிய இடம்பெயர்வு போர்ட்டல் (இ-ஷ்ரம்) மற்றும் ரேஷன் கார்டு பெயர்வுத்திறன் (ஒரே நாடு ஒரே ரேஷன் கார்டு) விதிகளையும் வலுப்படுத்தியது."
    ))

    # 100 - Key D (Hard)
    qs.append(make_q(
        num=100, diff="Hard", qtype="Concept MCQ", subtopic="Constitutional Framework",
        en_stem="Which renowned constitutional scholar coined the term 'Cooperative Federalism' to describe the Indian constitutional model, where strong central authority coexists with inter-state cooperation and regional diversity?",
        ta_stem="வலுவான மத்திய அதிகாரம், மாநிலங்களுக்கு இடையேயான ஒத்துழைப்பு மற்றும் பிராந்திய பன்முகத்தன்மையுடன் இணைந்து செயல்படும் இந்திய அரசியலமைப்பு மாதிரியை விவரிக்க 'கூட்டுறவு கூட்டாட்சி' (Cooperative Federalism) என்ற புகழ்பெற்ற சொல்லை உருவாக்கிய அரசியலமைப்பு அறிஞர் யார்?",
        en_a="K.C. Wheare (who characterized it as 'Quasi-Federal')", ta_a="கே.சி. வேர் (இவர் 'அரை-கூட்டாட்சி' எனக் குறிப்பிட்டார்)",
        en_b="Ivor Jennings (who called it a 'Federation with a strong centralising tendency')", ta_b="ஐவர் ஜென்னிங்ஸ் (இவர் 'வலுவான மையப்படுத்தும் போக்கு கொண்ட கூட்டாட்சி' என்றார்)",
        en_c="Paul Appleby (who described it as an 'Extremely Federal' system)", ta_c="பால் ஆப்பிள் பை (இவர் 'மிகவும் கூட்டாட்சி' அமைப்பு என்றார்)",
        en_d="Granville Austin (who highlighted the interdependent comity between the Union and the States)", ta_d="கிரான்வில் ஆஸ்டின் (இவர் மத்திய மற்றும் மாநிலங்களுக்கு இடையேயான ஒன்றையொன்று சார்ந்திருக்கும் நல்லிணக்கத்தை விளக்கினார்)",
        correct_key="D",
        exp_en="In his seminal work 'The Indian Constitution: Cornerstone of a Nation', Granville Austin characterized the Indian federal architecture as 'Cooperative Federalism'. It produces a strong central government, yet it does not result in the states being weak or administrative agencies of the Centre; rather, they are inter-dependent partners.",
        exp_ta="தனது புகழ்பெற்ற நூலான 'இந்திய அரசியலமைப்பு: ஒரு தேசத்தின் மூலைக்கல்' என்பதில், கிரான்வில் ஆஸ்டின் இந்திய கூட்டாட்சி அமைப்பை 'கூட்டுறவு கூட்டாட்சி' (Cooperative Federalism) என்று வர்ணித்தார். இது ஒரு வலுவான மத்திய அரசை உருவாக்கினாலும், மாநிலங்களை வெறும் அடிமை அமைப்புகளாக மாற்றாமல், இரண்டும் ஒன்றையொன்று சார்ந்த கூட்டாளிகளாகச் செயல்படுகின்றன.",
        why_a_en="Option A is K.C. Wheare, who described India as 'Quasi-Federal'.",
        why_a_ta="விருப்பம் A கே.சி. வேர், இவர் இந்தியாவை 'அரை-கூட்டாட்சி' (Quasi-Federal) என்றார்.",
        why_b_en="Option B is Ivor Jennings, who described it as a 'Federation with a strong centralising tendency'.",
        why_b_ta="விருப்பம் B ஐவர் ஜென்னிங்ஸ், இவர் 'வலுவான மையப்படுத்தும் போக்கு கொண்ட கூட்டாட்சி' என்றார்.",
        why_c_en="Option C is Paul Appleby, who focused on administrative federalism.",
        why_c_ta="விருப்பம் C பால் ஆப்பிள் பை, நிர்வாக கூட்டாட்சி பற்றி கூறினார்.",
        why_d_en="Option D is correct; Granville Austin famously coined 'Cooperative Federalism' for India.",
        why_d_ta="விருப்பம் D சரியானது; கிரான்வில் ஆஸ்டின் இந்தியாவை 'கூட்டுறவு கூட்டாட்சி' என்று அழைத்தார்.",
        tip_en="Constitutional Scholarly Views: Granville Austin = 'Cooperative Federalism'; K.C. Wheare = 'Quasi-Federal'; Ivor Jennings = 'Strong centralising tendency'; Morris-Jones = 'Bargaining Federalism'.",
        tip_ta="அரசியலமைப்பு அறிஞர்களின் பார்வைகள்: கிரான்வில் ஆஸ்டின் = 'கூட்டுறவு கூட்டாட்சி'; கே.சி. வேர் = 'அரை-கூட்டாட்சி'; ஐவர் ஜென்னிங்ஸ் = 'மையப்படுத்தும் போக்கு'; மோரிஸ்-ஜோன்ஸ் = 'பேரம்பேசும் கூட்டாட்சி'.",
        fact_en="The constitutional mechanisms for inter-state relations (Articles 261, 262, 263, Part XIII, and Zonal Councils) constitute the structural backbone of this cooperative federalism.",
        fact_ta="மாநிலங்களுக்கு இடையேயான உறவுகளுக்கான அரசியலமைப்பு வழிமுறைகள் (சரத்துகள் 261, 262, 263, பகுதி XIII மற்றும் மண்டல கவுன்சில்கள்) இந்த கூட்டுறவு கூட்டாட்சியின் கட்டமைப்பு முதுகெலும்பாக அமைகின்றன."
    ))

    return qs

if __name__ == "__main__":
    b4 = get_batch4()
    print(f"Batch 4 count: {len(b4)}")
    from collections import Counter
    print("Keys:", Counter([q["correct_answer"] for q in b4]))
    print("Diffs:", Counter([q["difficulty"] for q in b4]))
