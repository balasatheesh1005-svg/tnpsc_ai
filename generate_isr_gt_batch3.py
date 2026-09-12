# -*- coding: utf-8 -*-
"""
Batch 3: Grand Test MCQs ISR_GT_051 to ISR_GT_075
Key distribution: A: 6, B: 6, C: 7, D: 6 (Total: 25)
Difficulty: 8 Easy, 9 Medium, 8 Hard
"""

from isr_gt_helper import make_q

def get_batch3():
    qs = []

    # 051 - Key A (Easy)
    qs.append(make_q(
        num=51, diff="Easy", qtype="Concept MCQ", subtopic="Inter-State Trade and Commerce",
        en_stem="In the constitutional phrase 'Trade, Commerce and Intercourse' under Article 301, what does the term 'Intercourse' specifically denote?",
        ta_stem="சரத்து 301-ன் கீழான 'வர்த்தகம், வணிகம் மற்றும் உடனுறைவு' என்ற அரசியலமைப்புச் சொல்லாட்சியில், 'உடனுறைவு' (Intercourse) என்பது எதைக் குறிக்கிறது?",
        en_a="Non-commercial movement of persons, vehicles, and intangible communications across state boundaries", ta_a="மாநில எல்லைகளைக் கடந்து மனிதர்கள், வாகனங்கள் மற்றும் தகவல்தொடர்புகளின் வணிக நோக்கமற்ற நகர்வு",
        en_b="Exclusive trade in precious metals like gold and silver", ta_b="தங்கம் மற்றும் வெள்ளி போன்ற விலையுயர்ந்த உலோகங்களின் பிரத்யேக வர்த்தகம்",
        en_c="Formal diplomatic negotiations conducted between State Governors", ta_c="மாநில ஆளுநர்களுக்கு இடையே நடத்தப்படும் முறையான தூதரகப் பேச்சுவார்த்தைகள்",
        en_d="Military troop mobilizations ordered during national emergencies", ta_d="தேசிய அவசரநிலைகளின் போது உத்தரவிடப்படும் ராணுவப் படை நகர்வுகள்",
        correct_key="A",
        exp_en="The term 'intercourse' in Article 301 extends the constitutional protection beyond mere commercial trade to cover the movement of citizens, travellers, vehicles, and the transmission of non-commercial communications and ideas across state borders.",
        exp_ta="சரத்து 301-ல் உள்ள 'உடனுறைவு' (Intercourse) என்ற சொல் வெறும் வணிக வர்த்தகத்தைத் தாண்டி, மாநில எல்லைகளைக் கடந்து குடிமக்கள், பயணிகள், வாகனங்களின் நகர்வு மற்றும் வணிக நோக்கமற்ற கருத்துப் பரிமாற்றங்களையும் உள்ளடக்கியது.",
        why_a_en="Option A is correct; it covers non-commercial transit and communication across state borders.",
        why_a_ta="விருப்பம் A சரியானது; இது மாநில எல்லைகளைக் கடந்த வணிக நோக்கமற்ற போக்குவரத்து மற்றும் தொடர்புகளை உள்ளடக்கியது.",
        why_b_en="Option B is incorrect; it is not limited to precious metals.",
        why_b_ta="விருப்பம் B தவறானது; இது உலோகங்களுக்கு மட்டுமே உரியதல்ல.",
        why_c_en="Option C is incorrect; diplomatic negotiations are not termed intercourse.",
        why_c_ta="விருப்பம் C தவறானது; தூதரகப் பேச்சுவார்த்தைகள் இதில் வராது.",
        why_d_en="Option D is incorrect; military operations fall under Union defence powers.",
        why_d_ta="விருப்பம் D தவறானது; ராணுவ நடவடிக்கைகள் மத்திய பாதுகாப்பு அதிகாரத்திற்கு உட்பட்டது.",
        tip_en="Article 301: Trade = Buying & Selling; Commerce = Transportation of goods; Intercourse = Free movement of persons and communications.",
        tip_ta="சரத்து 301: வர்த்தகம் = வாங்குதல் & விற்றல்; வணிகம் = பொருட்கள் போக்குவரத்து; உடனுறைவு = நபர்கள் மற்றும் தகவல்களின் தடையற்ற இயக்கம்.",
        fact_en="This broad interpretation was borrowed from Chief Justice Marshall's classic formulation in Gibbons v. Ogden (1824) in US constitutional law.",
        fact_ta="இந்த பரந்த விளக்கம் அமெரிக்க அரசியலமைப்புச் சட்டத்தின் கிப்பன்ஸ் எதிர் ஆக்டன் (1824) வழக்கின் தீர்ப்பிலிருந்து பெறப்பட்டது."
    ))

    # 052 - Key B (Easy)
    qs.append(make_q(
        num=52, diff="Easy", qtype="Concept MCQ", subtopic="Inter-State Trade and Commerce",
        en_stem="Under Article 304(a) of the Constitution, a State Legislature may impose taxes on goods imported from other States, provided that:",
        ta_stem="அரசியலமைப்பின் சரத்து 304(a)-ன் கீழ், பிற மாநிலங்களிலிருந்து இறக்குமதி செய்யப்படும் பொருட்களின் மீது ஒரு மாநில சட்டமன்றம் வரி விதிக்கலாம், ஆனால் அதற்குரிய நிபந்தனை என்ன?",
        en_a="The tax rate is at least double the rate levied on locally manufactured goods", ta_a="உள்ளூரில் உற்பத்தி செய்யப்படும் பொருட்களின் மீதான வரி விகிதத்தை விட வரி விகிதம் குறைந்தது இருமடங்காக இருக்க வேண்டும்",
        en_b="No discrimination is made between goods so imported and similar goods manufactured or produced in that State", ta_b="அவ்வாறு இறக்குமதி செய்யப்படும் பொருட்களுக்கும் அந்த மாநிலத்தில் உற்பத்தி செய்யப்படும் அதே போன்ற பொருட்களுக்கும் இடையே எந்தப் பாகுபாடும் காட்டப்படக் கூடாது",
        en_c="Prior approval is granted by the NITI Aayog Governing Council", ta_c="நிதி ஆயோக் ஆளுகை கவுன்சிலால் முன் ஒப்புதல் வழங்கப்பட வேண்டும்",
        en_d="All revenues collected are immediately remitted to the Consolidated Fund of India", ta_d="வசூலிக்கப்படும் அனைத்து வருவாயும் உடனடியாக இந்திய ஒருங்கிணைந்த நிதியில் செலுத்தப்பட வேண்டும்",
        correct_key="B",
        exp_en="Article 304(a) enables a State Legislature to impose on goods imported from other states any tax to which similar goods manufactured or produced in that State are subject, so, however, as not to discriminate between goods so imported and goods so manufactured or produced.",
        exp_ta="சரத்து 304(a) பிற மாநிலங்களிலிருந்து இறக்குமதி செய்யப்படும் பொருட்களின் மீது வரி விதிக்க மாநிலத்திற்கு அதிகாரம் அளிக்கிறது; ஆனால், இறக்குமதி செய்யப்படும் பொருட்களுக்கும் உள்ளூர் பொருட்களுக்கும் இடையே எந்தவிதப் பாகுபாடும் காட்டக் கூடாது.",
        why_a_en="Option A is completely contrary to Article 304(a) non-discrimination.",
        why_a_ta="விருப்பம் A பாகுபாடின்மைக் கொள்கைக்கு முற்றிலும் எதிரானது.",
        why_b_en="Option B is the exact constitutional requirement of Article 304(a).",
        why_b_ta="விருப்பம் B என்பது சரத்து 304(a)-ன் நேரடி அரசியலமைப்பு நிபந்தனையாகும்.",
        why_c_en="Option C is incorrect; NITI Aayog has no constitutional taxing clearance role.",
        why_c_ta="விருப்பம் C தவறானது; நிதி ஆயோக்கிற்கு இதில் பங்கு இல்லை.",
        why_d_en="Option D is incorrect; state taxes flow into the Consolidated Fund of the State.",
        why_d_ta="விருப்பம் D தவறானது; மாநில வரிகள் மாநிலத்தின் ஒருங்கிணைந்த நிதிக்குச் செல்லும்.",
        tip_en="Article 304(a) = Non-discriminatory taxation on imported vs locally manufactured goods.",
        tip_ta="சரத்து 304(a) = இறக்குமதி செய்யப்படும் பொருட்கள் மற்றும் உள்ளூர் பொருட்களுக்கு இடையே பாகுபாடற்ற வரி விதிப்பு.",
        fact_en="Article 304(a) prevents states from creating tariff walls that protect local manufacturers against out-of-state competitors.",
        fact_ta="சரத்து 304(a) உள்ளூர் உற்பத்தியாளர்களைப் பாதுகாப்பதற்காக வெளிமாநில பொருட்களுக்கு எதிராக வரிச்சுவர்களை மாநிலங்கள் உருவாக்குவதைத் தடுக்கிறது."
    ))

    # 053 - Key C (Easy)
    qs.append(make_q(
        num=53, diff="Easy", qtype="Concept MCQ", subtopic="Zonal Councils and Reorganisation",
        en_stem="Where is the permanent headquarters of the North Eastern Council located?",
        ta_stem="வடகிழக்கு கவுன்சிலின் நிரந்தர தலைமையகம் எங்கு அமைந்துள்ளது?",
        en_a="Guwahati, Assam", ta_a="கவுகாத்தி, அசாம்",
        en_b="Agartala, Tripura", ta_b="அகர்தலா, திரிபுரா",
        en_c="Shillong, Meghalaya", ta_c="ஷில்லாங், மேகாலயா",
        en_d="Imphal, Manipur", ta_d="இம்பால், மணிப்பூர்",
        correct_key="C",
        exp_en="The North Eastern Council, established under the North Eastern Council Act, 1971, has its permanent secretariat and headquarters located in Shillong, Meghalaya.",
        exp_ta="1971-ஆம் ஆண்டின் வடகிழக்கு கவுன்சில் சட்டத்தின் கீழ் நிறுவப்பட்ட வடகிழக்கு கவுன்சிலின் நிரந்தர செயலகம் மற்றும் தலைமையகம் மேகாலயாவின் ஷில்லாங்கில் அமைந்துள்ளது.",
        why_a_en="Option A is Guwahati, the largest commercial city in Assam, not the NEC headquarters.",
        why_a_ta="விருப்பம் A கவுகாத்தி அசாமின் பெரிய நகரம், ஆனால் NEC தலைமையகம் அல்ல.",
        why_b_en="Option B is Agartala, capital of Tripura.",
        why_b_ta="விருப்பம் B அகர்தலா திரிபுராவின் தலைநகரம்.",
        why_c_en="Option C is correct; Shillong is the headquarters of the NEC.",
        why_c_ta="விருப்பம் C சரியானது; ஷில்லாங் வடகிழக்கு கவுன்சிலின் தலைமையகமாகும்.",
        why_d_en="Option D is Imphal, capital of Manipur.",
        why_d_ta="விருப்பம் D இம்பால் மணிப்பூரின் தலைநகரம்.",
        tip_en="North Eastern Council HQ = Shillong, Meghalaya.",
        tip_ta="வடகிழக்கு கவுன்சில் தலைமையகம் = ஷில்லாங், மேகாலயா.",
        fact_en="The NEC was formally inaugurated on November 7, 1972 by then Prime Minister Indira Gandhi.",
        fact_ta="வடகிழக்கு கவுன்சில் அப்போதைய பிரதமர் இந்திரா காந்தியால் நவம்பர் 7, 1972 அன்று முறைப்படி துவக்கி வைக்கப்பட்டது."
    ))

    # 054 - Key D (Easy)
    qs.append(make_q(
        num=54, diff="Easy", qtype="Concept MCQ", subtopic="Zonal Councils and Reorganisation",
        en_stem="Following the administrative restructuring in June 2018, who serves as the Chairman of the North Eastern Council?",
        ta_stem="ஜூன் 2018-ல் செய்யப்பட்ட நிர்வாக மறுசீரமைப்பைத் தொடர்ந்து, வடகிழக்கு கவுன்சிலின் தலைவராகச் செயல்படுபவர் யார்?",
        en_a="Prime Minister of India", ta_a="இந்தியப் பிரதமர்",
        en_b="Governor of Assam", ta_b="அசாம் மாநில ஆளுநர்",
        en_c="Minister of State for Development of North Eastern Region (DoNER)", ta_c="வடகிழக்கு பிராந்திய மேம்பாட்டு இணை அமைச்சர் (DoNER)",
        en_d="Union Minister of Home Affairs", ta_d="மத்திய உள்துறை அமைச்சர்",
        correct_key="D",
        exp_en="In June 2018, the Union Cabinet chaired by Prime Minister Narendra Modi designated the Union Minister of Home Affairs as the ex-officio Chairman of the North Eastern Council, and the Minister of State (Independent Charge) for DoNER as the Vice-Chairman.",
        exp_ta="ஜூன் 2018-ல் மத்திய அமைச்சரவை, மத்திய உள்துறை அமைச்சரை வடகிழக்கு கவுன்சிலின் தலைவராகவும், DoNER அமைச்சரை துணைத் தலைவராகவும் நியமித்தது.",
        why_a_en="Option A is incorrect; Prime Minister chairs the Inter-State Council.",
        why_a_ta="விருப்பம் A தவறானது; பிரதமர் மாநிலங்களுக்கு இடையேயான கவுன்சிலின் தலைவர்.",
        why_b_en="Option B was the convention in the early decades, but is no longer the chairman.",
        why_b_ta="விருப்பம் B ஆரம்ப தசாப்தங்களில் அசாம் ஆளுநர் தலைவராக இருந்தார், தற்போது இல்லை.",
        why_c_en="Option C is incorrect; the Minister of DoNER is the Vice-Chairman.",
        why_c_ta="விருப்பம் C தவறானது; DoNER அமைச்சர் துணைத் தலைவர் ஆவார்.",
        why_d_en="Option D is correct; Union Home Minister is the Chairman.",
        why_d_ta="விருப்பம் D சரியானது; மத்திய உள்துறை அமைச்சர் தலைவர் ஆவார்.",
        tip_en="Union Home Minister is the Chairman of ALL 5 Zonal Councils AND the North Eastern Council.",
        tip_ta="மத்திய உள்துறை அமைச்சர் அனைத்து 5 மண்டல கவுன்சில்கள் மற்றும் வடகிழக்கு கவுன்சிலின் தலைவராக உள்ளார்.",
        fact_en="The Governors and Chief Ministers of all eight North Eastern states (Arunachal Pradesh, Assam, Manipur, Meghalaya, Mizoram, Nagaland, Sikkim, and Tripura) are members of the NEC.",
        fact_ta="எட்டு வடகிழக்கு மாநிலங்களின் ஆளுநர்கள் மற்றும் முதலமைச்சர்கள் வடகிழக்கு கவுன்சிலில் உறுப்பினர்களாக உள்ளனர்."
    ))

    # 055 - Key A (Medium)
    qs.append(make_q(
        num=55, diff="Medium", qtype="Concept MCQ", subtopic="Constitutional Framework",
        en_stem="Under Article 239(2) of the Constitution, when the Governor of a State is appointed as an Administrator of an adjoining Union Territory, in what manner does he exercise his functions as such administrator?",
        ta_stem="அரசியலமைப்பின் சரத்து 239(2)-ன் கீழ், ஒரு மாநிலத்தின் ஆளுநர் அருகில் உள்ள யூனியன் பிரதேசத்தின் நிர்வாகியாக நியமிக்கப்படும் போது, அவர் எவ்வாறு தனது நிர்வாகப் பணிகளைச் செய்கிறார்?",
        en_a="Independently of his Council of Ministers in that State", ta_a="அந்த மாநிலத்தின் அமைச்சரவையைச் சாராமல் முற்றிலும் சுதந்திரமாக",
        en_b="Strictly upon the binding advice of the Council of Ministers of the parent State", ta_b="அம்மாநில அமைச்சரவையின் கட்டுப்படுத்தும் ஆலோசனையின் அடிப்படையில் மட்டுமே",
        en_c="Subject to the prior approval of the State Legislative Assembly", ta_c="மாநில சட்டமன்றத்தின் முன் ஒப்புதலுக்கு உட்பட்டு",
        en_d="Jointly with the Chief Justice of the State High Court", ta_d="மாநில உயர் நீதிமன்றத் தலைமை நீதிபதியுடன் இணைந்து",
        correct_key="A",
        exp_en="Article 239(2) explicitly provides: 'Where a Governor is so appointed, he shall exercise his functions as such Administrator independently of his Council of Ministers.'",
        exp_ta="சரத்து 239(2) தெளிவாகக் கூறுகிறது: 'ஒரு ஆளுநர் அவ்வாறு நிர்வாகியாக நியமிக்கப்படும் போது, அவர் தனது மாநில அமைச்சரவையைச் சாராமல் முற்றிலும் சுதந்திரமாக தனது பணிகளைச் செய்வார்.'",
        why_a_en="Option A is the exact constitutional mandate of Article 239(2).",
        why_a_ta="விருப்பம் A என்பது சரத்து 239(2)-ன் நேரடி அரசியலமைப்பு வாசகமாகும்.",
        why_b_en="Option B is completely contrary to the independent exercise under 239(2).",
        why_b_ta="விருப்பம் B சரத்து 239(2)-ன் விதிகளுக்கு எதிரானது.",
        why_c_en="Option C is incorrect; State Assembly has no jurisdiction over the UT.",
        why_c_ta="விருப்பம் C தவறானது; மாநில சட்டமன்றத்திற்கு யூனியன் பிரதேசத்தின் மீது அதிகாரம் இல்லை.",
        why_d_en="Option D is incorrect; judiciary has no executive administrative role.",
        why_d_ta="விருப்பம் D தவறானது; நீதித்துறைக்கு இதில் பங்கு இல்லை.",
        tip_en="Article 239(2): Governor acting as UT Administrator acts independently of his State Council of Ministers.",
        tip_ta="சரத்து 239(2): யூனியன் பிரதேச நிர்வாகியாக செயல்படும் ஆளுநர் தனது மாநில அமைச்சரவைக்கு கட்டுப்படாமல் செயல்படுகிறார்.",
        fact_en="This dual capacity is commonly seen when the Governor of Punjab acts as the Administrator of Chandigarh.",
        fact_ta="பஞ்சாப் ஆளுநர் சண்டிகரின் நிர்வாகியாகச் செயல்படும் போது இந்த இரட்டைப் பொறுப்பு நடைமுறையில் காணப்படுகிறது."
    ))

    # 056 - Key B (Medium)
    qs.append(make_q(
        num=56, diff="Medium", qtype="Concept MCQ", subtopic="Zonal Councils and Reorganisation",
        en_stem="Under Section 22 of the States Reorganisation Act, 1956, two or more Zonal Councils may hold a joint meeting to discuss matters of common interest. Who presides over such a joint meeting?",
        ta_stem="மாநில மறுசீரமைப்புச் சட்டம் 1956 பிரிவு 22-ன் கீழ், இரண்டு அல்லது அதற்கு மேற்பட்ட மண்டல கவுன்சில்கள் பொதுவான விஷயங்களை விவாதிக்க கூட்டுக் கூட்டத்தை நடத்தலாம். அத்தகைய கூட்டுக் கூட்டத்திற்கு தலைமை தாங்குபவர் யார்?",
        en_a="Prime Minister of India", ta_a="இந்தியப் பிரதமர்",
        en_b="Union Minister of Home Affairs", ta_b="மத்திய உள்துறை அமைச்சர்",
        en_c="The senior-most Governor among the participating states", ta_c="பங்கேற்கும் மாநிலங்களில் உள்ள மிக மூத்த ஆளுநர்",
        en_d="A rotating Chief Minister chosen by lot", ta_d="குலுக்கல் முறையில் தேர்ந்தெடுக்கப்படும் சுழற்சி முதலமைச்சர்",
        correct_key="B",
        exp_en="Under Section 22(2) of the States Reorganisation Act, 1956, the Union Home Minister, as the Chairman of the Zonal Councils, presides over any joint meeting of two or more Zonal Councils.",
        exp_ta="மாநில மறுசீரமைப்புச் சட்டம் 1956 பிரிவு 22(2)-ன் படி, மண்டல கவுன்சில்களின் தலைவரான மத்திய உள்துறை அமைச்சரே இரண்டு அல்லது அதற்கு மேற்பட்ட மண்டல கவுன்சில்களின் கூட்டுக் கூட்டத்திற்கு தலைமை தாங்குவார்.",
        why_a_en="Option A is incorrect; PM does not preside over Zonal Council meetings.",
        why_a_ta="விருப்பம் A தவறானது; பிரதமர் மண்டல கவுன்சில் கூட்டங்களுக்கு தலைமை தாங்குவதில்லை.",
        why_b_en="Option B is correct; Union Home Minister presides over joint zonal meetings.",
        why_b_ta="விருப்பம் B சரியானது; மத்திய உள்துறை அமைச்சர் மண்டல கூட்டுக் கூட்டத்திற்கு தலைமை தாங்குவார்.",
        why_c_en="Option C is incorrect; Governors are not members.",
        why_c_ta="விருப்பம் C தவறானது; ஆளுநர்கள் உறுப்பினர்கள் அல்ல.",
        why_d_en="Option D is incorrect; Chief Ministers are Vice-Chairmen of their respective individual councils.",
        why_d_ta="விருப்பம் D தவறானது; முதலமைச்சர்கள் துணைத் தலைவர்கள் மட்டுமே.",
        tip_en="Section 22 of States Reorganisation Act: Joint meetings of Zonal Councils are presided over by the Union Home Minister.",
        tip_ta="மாநில மறுசீரமைப்புச் சட்டம் பிரிவு 22: மண்டல கவுன்சில்களின் கூட்டுக் கூட்டங்களுக்கு மத்திய உள்துறை அமைச்சர் தலைமை தாங்குகிறார்.",
        fact_en="Joint meetings are particularly useful for resolving inter-zonal transport corridors, border disputes, or inter-basin water projects.",
        fact_ta="மண்டலங்களுக்கு இடையேயான போக்குவரத்து, எல்லைத் தகராறுகள் அல்லது நதிநீர் திட்டங்களைத் தீர்க்க கூட்டுக் கூட்டங்கள் பயன்படுகின்றன."
    ))

    # 057 - Key C (Medium)
    qs.append(make_q(
        num=57, diff="Medium", qtype="Concept MCQ", subtopic="Constitutional Framework",
        en_stem="Article 260 of the Indian Constitution deals with the jurisdiction of the Union Government in relation to which of the following?",
        ta_stem="இந்திய அரசியலமைப்பின் சரத்து 260 பின்வருவனவற்றில் எதன் மீதான மத்திய அரசின் அதிகார வரம்பைக் கையாள்கிறது?",
        en_a="Tribal areas specified under the Sixth Schedule", ta_a="ஆறாவது அட்டவணையின் கீழ் குறிப்பிடப்பட்டுள்ள பழங்குடியினர் பகுதிகள்",
        en_b="Union Territories lacking a Legislative Assembly", ta_b="சட்டமன்றம் இல்லாத யூனியன் பிரதேசங்கள்",
        en_c="Territories outside the territory of India by virtue of international agreement", ta_c="சர்வதேச ஒப்பந்தத்தின் அடிப்படையில் இந்திய எல்லைக்கு வெளியே உள்ள பகுதிகள்",
        en_d="Inter-state coastal economic zones beyond territorial waters", ta_d="கடலோர எல்லைக்கு அப்பாற்பட்ட மாநிலங்களுக்கு இடையேயான பொருளாதார மண்டலங்கள்",
        correct_key="C",
        exp_en="Article 260 provides: 'The Government of India may by agreement with the Government of any territory not being part of the territory of India undertake any executive, legislative or judicial functions vested in the Government of such territory.'",
        exp_ta="சரத்து 260 கூறுகிறது: 'இந்திய எல்லைக்கு உட்படாத எந்தவொரு பகுதியின் அரசுடன் செய்துகொள்ளும் ஒப்பந்தத்தின் மூலம், அப்பகுதியின் அரசுக்குரிய நிர்வாக, சட்டமன்ற அல்லது நீதித்துறை பணிகளை இந்திய அரசு ஏற்றுக்கொள்ளலாம்.'",
        why_a_en="Option A deals with Article 244 and Sixth Schedule.",
        why_a_ta="விருப்பம் A சரத்து 244 மற்றும் 6-வது அட்டவணை தொடர்பானது.",
        why_b_en="Option B deals with Article 239.",
        why_b_ta="விருப்பம் B சரத்து 239 தொடர்பானது.",
        why_c_en="Option C is the exact subject matter of Article 260.",
        why_c_ta="விருப்பம் C என்பது சரத்து 260-ன் நேரடிப் பொருளாகும்.",
        why_d_en="Option D deals with Article 297.",
        why_d_ta="விருப்பம் D சரத்து 297 தொடர்பானது.",
        tip_en="Article 260: Jurisdiction of the Union in relation to foreign territories outside India by agreement.",
        tip_ta="சரத்து 260: ஒப்பந்தம் மூலம் இந்திய எல்லைக்கு வெளியே உள்ள வெளிநாட்டுப் பகுதிகள் மீதான மத்திய அரசின் அதிகாரம்.",
        fact_en="Article 260 was historically used during transitional periods when foreign enclaves (like French Pondicherry or Portuguese Goa) were being integrated into India.",
        fact_ta="பாண்டிச்சேரி அல்லது கோவா போன்ற வெளிநாட்டுப் பகுதிகள் இந்தியாவுடன் இணைக்கப்பட்ட இடைக்காலத்தின் போது சரத்து 260 பயன்படுத்தப்பட்டது."
    ))

    # 058 - Key D (Medium)
    qs.append(make_q(
        num=58, diff="Medium", qtype="Concept MCQ", subtopic="Zonal Councils and Reorganisation",
        en_stem="Under Section 20 of the States Reorganisation Act, 1956, how is the Secretariat of each Zonal Council staffed?",
        ta_stem="மாநில மறுசீரமைப்புச் சட்டம் 1956 பிரிவு 20-ன் கீழ், ஒவ்வொரு மண்டல கவுன்சிலின் செயலகமும் எவ்வாறு பணியமர்த்தப்படுகிறது?",
        en_a="Recruited exclusively through the Union Public Service Commission (UPSC)", ta_a="மத்திய அரசுப் பணியாளர் தேர்வாணையம் (UPSC) மூலம் மட்டுமே பணியமர்த்தப்படுகிறது",
        en_b="Directly appointed on permanent basis by the Chief Justice of India", ta_b="இந்திய தலைமை நீதிபதியால் நிரந்தர அடிப்படையில் நேரடியாக நியமிக்கப்படுகிறது",
        en_c="Managed by the Army Corps of Engineers", ta_c="ராணுவ பொறியாளர் பிரிவால் நிர்வகிக்கப்படுகிறது",
        en_d="Provided with a Secretary chosen from the Chief Secretaries of member states by rotation, along with administrative officers sanctioned by the Chairman", ta_d="உறுப்பு மாநிலங்களின் தலைமைச் செயலாளர்களிலிருந்து சுழற்சி முறையில் தேர்ந்தெடுக்கப்படும் ஒரு செயலாளர் மற்றும் தலைவரால் அனுமதிக்கப்படும் நிர்வாக அதிகாரிகளைக் கொண்டு வழங்கப்படுகிறது",
        correct_key="D",
        exp_en="Section 20 of the States Reorganisation Act provides that each Zonal Council shall have a secretarial staff, with the Chief Secretaries of the member states acting as the Secretary to the Council by rotation for a period of one year at a time.",
        exp_ta="மாநில மறுசீரமைப்புச் சட்டம் பிரிவு 20-ன் படி, ஒவ்வொரு மண்டல கவுன்சிலுக்கும் ஒரு செயலகம் இருக்கும்; உறுப்பு மாநிலங்களின் தலைமைச் செயலாளர்கள் சுழற்சி முறையில் தலா ஒரு வருடத்திற்கு கவுன்சிலின் செயலாளராகச் செயல்படுவர்.",
        why_a_en="Option A is incorrect; secretarial staff is not recruited as a separate UPSC cadre.",
        why_a_ta="விருப்பம் A தவறானது; இது தனி UPSC பணியிடம் அல்ல.",
        why_b_en="Option B is incorrect; judiciary has no role.",
        why_b_ta="விருப்பம் B தவறானது; நீதித்துறைக்கு இதில் தொடர்பு இல்லை.",
        why_c_en="Option C is incorrect.",
        why_c_ta="விருப்பம் C தவறானது.",
        why_d_en="Option D accurately reflects Section 20 of the 1956 Act.",
        why_d_ta="விருப்பம் D 1956 சட்டத்தின் பிரிவு 20-ஐ துல்லியமாகக் காட்டுகிறது.",
        tip_en="Zonal Council Secretary = Chief Secretaries of member states by rotation for 1 year.",
        tip_ta="மண்டல கவுன்சில் செயலாளர் = உறுப்பு மாநிலங்களின் தலைமைச் செயலாளர்கள் சுழற்சி முறையில் 1 ஆண்டிற்கு.",
        fact_en="Since 1991, the Inter-State Council Secretariat in New Delhi also provides continuous institutional support to all Zonal Councils.",
        fact_ta="1991 முதல், புது தில்லியில் உள்ள மாநிலங்களுக்கு இடையேயான கவுன்சில் செயலகமும் அனைத்து மண்டல கவுன்சில்களுக்கும் தொடர்ச்சியான நிறுவன ஆதரவை வழங்கி வருகிறது."
    ))

    # 059 - Key A (Hard)
    qs.append(make_q(
        num=59, diff="Hard", qtype="Concept MCQ", subtopic="Inter-State Trade and Commerce",
        en_stem="In the landmark 9-judge Constitution Bench ruling in Jindal Stainless Ltd. v. State of Haryana (2017), on what constitutional ground was the 55-year-old 'Compensatory Tax Theory' overruled?",
        ta_stem="ஜிண்டால் ஸ்டெயின்லெஸ் லிமிடெட் எதிர் ஹரியானா மாநிலம் (2017) என்ற 9 நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வின் வரலாற்றுத் தீர்ப்பில், 55 ஆண்டுகால 'ஈட்டு வரிக் கோட்பாடு' எந்த அரசியலமைப்பு அடிப்படையில் ரத்து செய்யப்பட்டது?",
        en_a="The concept of compensatory tax has no foundation in the constitutional text of Part XIII and introduces unnecessary judicial vagueness into sovereign state taxing powers", ta_a="ஈட்டு வரி என்ற கருத்துக்கு பகுதி XIII-ன் அரசியலமைப்பு உரையில் எந்த அடிப்படையும் இல்லை; மேலும் இது மாநிலங்களின் இறையாண்மை வரி விதிப்பு அதிகாரத்தில் தேவையற்ற தெளிவின்மையை அறிமுகப்படுத்துகிறது",
        en_b="States have no constitutional power whatsoever to levy taxes on motor vehicles or entry of goods", ta_b="மோட்டார் வாகனங்கள் அல்லது பொருட்கள் நுழைவு மீது வரி விதிக்க மாநிலங்களுக்கு அரசியலமைப்பு ரீதியாக எந்த அதிகாரமும் இல்லை",
        en_c="The GST Council declared all state entry taxes illegal under Article 279A", ta_c="சரத்து 279A-ன் கீழ் ஜிஎஸ்டி கவுன்சில் அனைத்து மாநில நுழைவு வரிகளையும் சட்டவிரோதமானது என்று அறிவித்தது",
        en_d="The President issued an ordinance prohibiting all local body cesses across India", ta_d="இந்தியா முழுவதும் உள்ள அனைத்து உள்ளாட்சி வரிகளையும் தடை செய்து குடியரசுத் தலைவர் அவசரச் சட்டம் பிறப்பித்தார்",
        correct_key="A",
        exp_en="By a 7:2 majority, the 9-judge bench in Jindal Stainless (2017) held that the 'compensatory tax theory' devised in Automobile Transport (1962) was judicially crafted without any constitutional text in Part XIII. Taxes per se do not violate Article 301 unless they are discriminatory under Article 304(a).",
        exp_ta="2017 ஜிண்டால் ஸ்டெயின்லெஸ் வழக்கில் 7:2 பெரும்பான்மையுடன் 9 நீதிபதிகள் அமர்வு, பகுதி XIII-ல் ஈட்டு வரி என்ற சொல்லோ கருத்தோ இல்லை என்றும், வரிகள் நேரடியாக பாகுபாடானதாக இல்லாதவரை சரத்து 301-ஐ மீறாது என்றும் கூறி ஈட்டு வரிக் கோட்பாட்டை ரத்து செய்தது.",
        why_a_en="Option A is correct; the court held compensatory tax had no constitutional textual basis.",
        why_a_ta="விருப்பம் A சரியானது; ஈட்டு வரிக்கு அரசியலமைப்பு அடிப்படை இல்லை என நீதிமன்றம் கூறியது.",
        why_b_en="Option B is incorrect; Entry 52 and 57 of List II clearly empower the States.",
        why_b_ta="விருப்பம் B தவறானது; மாநிலப் பட்டியல் பதிவுகள் 52 மற்றும் 57 மாநிலங்களுக்கு அதிகாரம் அளிக்கின்றன.",
        why_c_en="Option C is incorrect; GST rolled out later in July 2017.",
        why_c_ta="விருப்பம் C தவறானது; ஜிஎஸ்டி பின்னர் ஜூலை 2017 இல் அமலானது.",
        why_d_en="Option D is incorrect.",
        why_d_ta="விருப்பம் D தவறானது.",
        tip_en="Jindal Stainless (2017, 9 Judges) officially overruled Automobile Transport (1962, 7 Judges).",
        tip_ta="ஜிண்டால் ஸ்டெயின்லெஸ் (2017, 9 நீதிபதிகள்) ஆட்டோமொபைல் டிரான்ஸ்போர்ட் (1962, 7 நீதிபதிகள்) தீர்ப்பை அதிகாரப்பூர்வமாக ரத்து செய்தது.",
        fact_en="Chief Justice T.S. Thakur headed the 9-judge bench that delivered this historic decision settling half a century of entry tax litigation.",
        fact_ta="தலைமை நீதிபதி டி.எஸ். தாக்கூர் இந்த வரலாற்றுச் சிறப்புமிக்க தீர்ப்பை வழங்கிய 9 நீதிபதிகள் கொண்ட அமர்விற்கு தலைமை தாங்கினார்."
    ))

    # 060 - Key B (Hard)
    qs.append(make_q(
        num=60, diff="Hard", qtype="Concept MCQ", subtopic="Inter-State Trade and Commerce",
        en_stem="Following the 9-judge bench verdict in Jindal Stainless Ltd. (2017), what is the sole test to determine whether a State tax on goods imported from other states violates Article 301?",
        ta_stem="2017 ஜிண்டால் ஸ்டெயின்லெஸ் 9 நீதிபதிகள் அமர்வுத் தீர்ப்பைத் தொடர்ந்து, பிற மாநிலங்களிலிருந்து இறக்குமதி செய்யப்படும் பொருட்கள் மீதான மாநில வரி சரத்து 301-ஐ மீறுகிறதா என்பதைத் தீர்மானிப்பதற்கான ஒரே சோதனை என்ன?",
        en_a="Whether the collected revenue is deposited into the local panchayat treasury", ta_a="வசூலிக்கப்பட்ட வருவாய் உள்ளூர் பஞ்சாயத்து கருவூலத்தில் டெபாசிட் செய்யப்படுகிறதா என்பது",
        en_b="Whether the state tax discriminates between goods imported from other states and similar goods manufactured within the state (Article 304(a) test)", ta_b="பிற மாநிலங்களிலிருந்து இறக்குமதி செய்யப்படும் பொருட்களுக்கும் மாநிலத்திற்குள் உற்பத்தி செய்யப்படும் அதே போன்ற பொருட்களுக்கும் இடையே வரி பாகுபாடு காட்டுகிறதா என்பது (சரத்து 304(a) சோதனை)",
        en_c="Whether the state legislature had unanimous assent of all opposition parties", ta_c="அனைத்து எதிர்க்கட்சிகளின் ஒருமனதான ஒப்புதலை மாநில சட்டமன்றம் பெற்றிருந்ததா என்பது",
        en_d="Whether the tax has been cleared in advance by the Union Finance Commission", ta_d="மத்திய நிதி ஆணையத்தால் அந்த வரி முன்கூட்டியே அங்கீகரிக்கப்பட்டதா என்பது",
        correct_key="B",
        exp_en="The 9-judge bench in Jindal Stainless (2017) ruled that non-discriminatory taxes do not curtail freedom under Article 301. The sole test of validity for a state entry or sales tax is whether it complies with Article 304(a) by treating imported and locally produced goods on equal footing without economic discrimination.",
        exp_ta="2017 ஜிண்டால் ஸ்டெயின்லெஸ் வழக்கில் 9 நீதிபதிகள் அமர்வு, பாகுபாடற்ற வரிகள் சரத்து 301-ன் கீழான சுதந்திரத்தைக் குறைக்காது என்றும்; இறக்குமதி செய்யப்படும் பொருட்களையும் உள்ளூர் பொருட்களையும் சமமாக நடத்தி பாகுபாடு காட்டாமல் சரத்து 304(a)-க்கு இணங்குகிறதா என்பதே ஒரே சோதனை என்றும் தீர்ப்பளித்தது.",
        why_a_en="Option A is irrelevant to Article 301.",
        why_a_ta="விருப்பம் A சரத்து 301-க்கு தொடர்பற்றது.",
        why_b_en="Option B is the precise holding of the 9-judge bench under Article 304(a).",
        why_b_ta="விருப்பம் B என்பது சரத்து 304(a)-ன் கீழான 9 நீதிபதிகள் அமர்வின் துல்லியமான தீர்ப்பாகும்.",
        why_c_en="Option C is irrelevant to constitutional validity.",
        why_c_ta="விருப்பம் C அரசியலமைப்பு செல்லுபடியாகும் தன்மைக்கு தொடர்பற்றது.",
        why_d_en="Option D is incorrect; Finance Commission has no role in tax clearance.",
        why_d_ta="விருப்பம் D தவறானது; நிதி ஆணையத்திற்கு இதில் பங்கு இல்லை.",
        tip_en="Post-2017 rule: If tax is non-discriminatory under 304(a), it does NOT violate 301. Compensatory concept is DEAD.",
        tip_ta="2017-க்குப் பிந்தைய விதி: வரி சரத்து 304(a)-ன் கீழ் பாகுபாடற்றதாக இருந்தால், அது சரத்து 301-ஐ மீறாது. ஈட்டு வரிக் கோட்பாடு கைவிடப்பட்டது.",
        fact_en="This verdict upheld state entry taxes levied by Haryana, Uttar Pradesh, Tamil Nadu, and several other states.",
        fact_ta="இந்தத் தீர்ப்பு ஹரியானா, உத்தரப் பிரதேசம், தமிழ்நாடு மற்றும் பல மாநிலங்கள் விதித்த நுழைவு வரிகளை உறுதி செய்தது."
    ))

    # 061 - Key C (Hard)
    qs.append(make_q(
        num=61, diff="Hard", qtype="Concept MCQ", subtopic="Inter-State River Water Disputes",
        en_stem="Under the Inter-State River Water Disputes (Amendment) Bill passed by the Lok Sabha in 2019, what new institutional mechanism is proposed to attempt amicable settlement before a dispute is referred to the Tribunal?",
        ta_stem="2019-ல் மக்களவையால் நிறைவேற்றப்பட்ட மாநிலங்களுக்கு இடையேயான நதிநீர் தகராறுகள் (திருத்த) மசோதாவின் கீழ், தகராறு தீர்ப்பாயத்திற்கு அனுப்பப்படுவதற்கு முன் சுமுகமான தீர்வுக்கு முயல முன்மொழியப்பட்ட புதிய அமைப்பு எது?",
        en_a="National Water Commission Collegium", ta_a="தேசிய நீர் ஆணைய கொலீஜியம்",
        en_b="Inter-State Judicial Mediation Cell", ta_b="மாநிலங்களுக்கு இடையேயான நீதித்துறை மத்தியஸ்த பிரிவு",
        en_c="Dispute Resolution Committee (DRC)", ta_c="தகராறு தீர்வுக் குழு (DRC - Dispute Resolution Committee)",
        en_d="Supreme Court River Lok Adalat", ta_d="உச்ச நீதிமன்ற நதிநீர் லோக் அதாலத்",
        correct_key="C",
        exp_en="The 2019 Amendment Bill provides for the establishment of a Dispute Resolution Committee (DRC) by the Central Government, comprising relevant domain experts, to resolve inter-state water disputes amicably within 1 year (extendable by 6 months). Only if the DRC fails will the dispute go to the Tribunal.",
        exp_ta="2019 திருத்த மசோதா, நதிநீர் தகராறுகளை 1 ஆண்டுக்குள் (மேலும் 6 மாதங்கள் நீட்டிக்கப்படலாம்) சுமுகமாகத் தீர்ப்பதற்காக வல்லுநர்களைக் கொண்ட 'தகராறு தீர்வுக் குழுவை' (DRC) மத்திய அரசு அமைக்க வழிவகை செய்கிறது. DRC தோல்வியடைந்தால் மட்டுமே தகராறு தீர்ப்பாயத்திற்குச் செல்லும்.",
        why_a_en="Option A is incorrect.",
        why_a_ta="விருப்பம் A தவறானது.",
        why_b_en="Option B is incorrect.",
        why_b_ta="விருப்பம் B தவறானது.",
        why_c_en="Option C is the exact statutory body created in the 2019 Bill.",
        why_c_ta="விருப்பம் C என்பது 2019 மசோதாவில் முன்மொழியப்பட்ட சரியான அமைப்பாகும்.",
        why_d_en="Option D is incorrect.",
        why_d_ta="விருப்பம் D தவறானது.",
        tip_en="2019 Bill: Dispute Resolution Committee (DRC) first (1 yr + 6 months). If DRC fails -> Single Permanent Tribunal.",
        tip_ta="2019 மசோதா: முதலில் தகராறு தீர்வுக் குழு (DRC) (1 ஆண்டு + 6 மாதங்கள்). அது தவறினால் -> ஒற்றை நிரந்தர தீர்ப்பாயம்.",
        fact_en="The DRC is intended to filter out unnecessary tribunal references by resolving technical differences through institutional mediation.",
        fact_ta="தொழில்நுட்ப ரீதியான வேறுபாடுகளை மத்தியஸ்தம் மூலம் தீர்த்து தேவையற்ற தீர்ப்பாய வழக்குகளைத் தவிர்ப்பதே DRC-ன் நோக்கமாகும்."
    ))

    # 062 - Key C (Medium)
    qs.append(make_q(
        num=62, diff="Medium", qtype="Concept MCQ", subtopic="Inter-State River Water Disputes",
        en_stem="What structural transformation does the Inter-State River Water Disputes (Amendment) Bill, 2019 propose regarding water dispute tribunals?",
        ta_stem="2019-ஆம் ஆண்டின் மாநிலங்களுக்கு இடையேயான நதிநீர் தகராறுகள் (திருத்த) மசோதா நதிநீர் தகராறு தீர்ப்பாயங்கள் தொடர்பாக எந்த கட்டமைப்பு மாற்றத்தை முன்மொழிகிறது?",
        en_a="Handing over all water adjudication exclusively to state High Courts", ta_a="அனைத்து நதிநீர் விசாரணைகளையும் பிரத்யேகமாக மாநில உயர் நீதிமன்றங்களிடம் ஒப்படைத்தல்",
        en_b="Abolishing all tribunals and leaving water allocation to the Prime Minister's discretion", ta_b="அனைத்து தீர்ப்பாயங்களையும் ஒழித்துவிட்டு நீர் ஒதுக்கீட்டை பிரதமரின் விருப்பத்திற்கு விட்டுவிடுதல்",
        en_c="Replacing multiple ad-hoc tribunals with a Single Permanent Inter-State River Water Disputes Tribunal with multiple benches", ta_c="பல தற்காலிக தீர்ப்பாயங்களுக்குப் பதிலாக பல அமர்வுகளைக் கொண்ட ஒரே நிரந்தர மாநிலங்களுக்கு இடையேயான நதிநீர் தகராறு தீர்ப்பாயத்தை நிறுவுதல்",
        en_d="Transferring water dispute resolution to the United Nations Environment Programme", ta_d="நதிநீர் தகராறு தீர்வை ஐக்கிய நாடுகள் சுற்றுச்சூழல் திட்டத்திற்கு மாற்றுதல்",
        correct_key="C",
        exp_en="The 2019 Amendment Bill proposes to replace the existing system of separate ad-hoc tribunals for each river with a single, standalone, permanent Inter-State River Water Disputes Tribunal having multiple benches.",
        exp_ta="2019 திருத்த மசோதா ஒவ்வொரு நதிக்கும் தனித்தனி தற்காலிக தீர்ப்பாயங்களை அமைக்கும் தற்போதைய முறைக்கு மாற்றாக, பல அமர்வுகளைக் கொண்ட ஒரே நிரந்தர நதிநீர் தகராறு தீர்ப்பாயத்தை உருவாக்க முன்மொழிகிறது.",
        why_a_en="Option A is incorrect; High Courts remain barred under Article 262.",
        why_a_ta="விருப்பம் A தவறானது; சரத்து 262-ன் கீழ் உயர் நீதிமன்றங்கள் தடை செய்யப்பட்டுள்ளன.",
        why_b_en="Option B is incorrect; independent adjudication is retained.",
        why_b_ta="விருப்பம் B தவறானது.",
        why_c_en="Option C is the core structural reform of the 2019 Bill.",
        why_c_ta="விருப்பம் C என்பது 2019 மசோதாவின் மைய கட்டமைப்பு சீர்திருத்தம் ஆகும்.",
        why_d_en="Option D is incorrect.",
        why_d_ta="விருப்பம் D தவறானது.",
        tip_en="2019 Bill core reform = Standalone Single Permanent Tribunal with multiple benches.",
        tip_ta="2019 மசோதாவின் முக்கிய சீர்திருத்தம் = பல அமர்வுகளைக் கொண்ட ஒரே நிரந்தர தீர்ப்பாயம்.",
        fact_en="Existing tribunals will be dissolved and their ongoing adjudications will be subsumed as benches of the new permanent tribunal.",
        fact_ta="நடைமுறையில் உள்ள தற்காலிக தீர்ப்பாயங்கள் கலைக்கப்பட்டு அவற்றின் விசாரணைகள் புதிய நிரந்தர தீர்ப்பாயத்தின் அமர்வுகளாக மாற்றப்படும்."
    ))

    # 063 - Key D (Hard)
    qs.append(make_q(
        num=63, diff="Hard", qtype="Concept MCQ", subtopic="Inter-State Trade and Commerce",
        en_stem="In State of Bombay v. R.M.D. Chamarbaugwala (1957), what did the Supreme Court hold regarding prize competitions and gambling under Article 301?",
        ta_stem="பம்பாய் மாநிலம் எதிர் ஆர்.எம்.டி. சாமர்பாக்வாலா (1957) வழக்கில், சரத்து 301-ன் கீழ் பரிசுப் போட்டிகள் மற்றும் சூதாட்டம் குறித்து உச்ச நீதிமன்றம் என்ன தீர்ப்பளித்தது?",
        en_a="Gambling is a fundamental right of trade under Article 19(1)(g)", ta_a="சூதாட்டம் என்பது சரத்து 19(1)(g)-ன் கீழான ஒரு அடிப்படை வர்த்தக உரிமை",
        en_b="Gambling between states can only be taxed by the Central Government", ta_b="மாநிலங்களுக்கிடையேயான சூதாட்டத்திற்கு மத்திய அரசு மட்டுமே வரி விதிக்க முடியும்",
        en_c="States are constitutionally required to permit online betting across state lines", ta_c="மாநில எல்லைகளைக் கடந்த ஆன்லைன் பந்தயங்களை அனுமதிக்க மாநிலங்கள் அரசியலமைப்பு ரீதியாகக் கடமைப்பட்டுள்ளன",
        en_d="Gambling and gambling-like activities are 'res extra commercium' (outside commerce) and cannot claim the constitutional freedom of trade under Article 301", ta_d="சூதாட்டம் போன்ற தீய நடவடிக்கைகள் 'வணிகத்திற்கு அப்பாற்பட்டவை' (res extra commercium) என்பதால் அவை சரத்து 301-ன் கீழான வர்த்தக சுதந்திரத்தைப் பெற முடியாது",
        correct_key="D",
        exp_en="The Supreme Court held that gambling activities, prize competitions of a gambling nature, trafficking in women, or illicit liquor are 'res extra commercium' (outside commerce). They are inherently harmful activities and do not constitute 'trade, commerce or intercourse' under Article 301.",
        exp_ta="உச்ச நீதிமன்றம் சூதாட்டம், விபச்சாரம் அல்லது கள்ளச்சாராயம் போன்ற தீய நடவடிக்கைகள் 'வணிகத்திற்கு அப்பாற்பட்டவை' (res extra commercium) என்றும், அவற்றுக்கு சரத்து 301-ன் கீழ் எந்த வர்த்தக பாதுகாப்பும் கிடைக்காது என்றும் தீர்ப்பளித்தது.",
        why_a_en="Option A is incorrect; fundamental rights do not protect criminal or harmful trades.",
        why_a_ta="விருப்பம் A தவறானது; அடிப்படை உரிமைகள் தீய செயல்களைப் பாதுகாக்காது.",
        why_b_en="Option B is incorrect; Betting and Gambling is Entry 34 of the State List.",
        why_b_ta="விருப்பம் B தவறானது; சூதாட்டம் மாநிலப் பட்டியல் பதிவு 34 ஆகும்.",
        why_c_en="Option C is incorrect.",
        why_c_ta="விருப்பம் C தவறானது.",
        why_d_en="Option D is the historic ruling establishing the doctrine of 'res extra commercium'.",
        why_d_ta="விருப்பம் D சரியானது; 'வணிகத்திற்கு அப்பாற்பட்டவை' என்ற வரலாற்றுக் கோட்பாட்டை இது நிறுவியது.",
        tip_en="Chamarbaugwala (1957) = Gambling is 'res extra commercium' -> NOT protected by Article 301.",
        tip_ta="சாமர்பாக்வாலா (1957) = சூதாட்டம் வணிகத்திற்கு அப்பாற்பட்டது -> சரத்து 301-ன் கீழ் பாதுகாப்பு இல்லை.",
        fact_en="This principle allows individual States to totally ban lotteries, gambling, and alcohol imported from other States without violating Article 301.",
        fact_ta="இந்தக் கொள்கை, சரத்து 301-ஐ மீறாமல் பிற மாநிலங்களிலிருந்து வரும் லாட்டரிகள், சூதாட்டம் மற்றும் மதுபானங்களை முழுமையாகத் தடை செய்ய மாநிலங்களுக்கு அதிகாரம் அளிக்கிறது."
    ))

    # 064 - Key A (Hard)
    qs.append(make_q(
        num=64, diff="Hard", qtype="Concept MCQ", subtopic="Inter-State Trade and Commerce",
        en_stem="In Fatehchand Himmatlal v. State of Maharashtra (1977), how did the Supreme Court treat moneylending under Part XIII of the Constitution?",
        ta_stem="பதேச்சந்த் ஹிம்மத்லால் எதிர் மகாராஷ்டிர மாநிலம் (1977) வழக்கில், அரசியலமைப்பின் பகுதி XIII-ன் கீழ் கந்துவட்டி/கடன் வழங்குதலை உச்ச நீதிமன்றம் எவ்வாறு கருதியது?",
        en_a="Extortionate moneylending to rural debtors is not trade or commerce within Article 301, and debt relief laws do not violate freedom of trade", ta_a="கிராமப்புற ஏழை எளியவர்களிடம் அநியாய வட்டிக்கு கடன் வழங்குவது சரத்து 301-ன் கீழ் வர்த்தகம் அல்ல; கடன் நிவாரணச் சட்டங்கள் வர்த்தக சுதந்திரத்தை மீறாது",
        en_b="Moneylending is an essential public utility protected against all state laws", ta_b="கடன் வழங்குதல் என்பது அனைத்து மாநிலச் சட்டங்களிலிருந்தும் பாதுகாக்கப்பட்ட அத்தியாவசிய பொதுச் சேவை",
        en_c="Only the Reserve Bank of India can regulate moneylending under Article 302", ta_c="சரத்து 302-ன் கீழ் இந்திய ரிசர்வ் வங்கி மட்டுமே கடன் வழங்குதலை ஒழுங்குபடுத்த முடியும்",
        en_d="Moneylending is a treaty function governed by the Inter-State Council", ta_d="கடன் வழங்குதல் என்பது மாநிலங்களுக்கு இடையேயான கவுன்சிலால் நிர்வகிக்கப்படும் ஒரு ஒப்பந்தப் பணி",
        correct_key="A",
        exp_en="In Fatehchand Himmatlal (1977), the Supreme Court ruled that exploitative, extortionate moneylending to impoverished rural debtors is not 'trade' within the meaning of Article 301. The Maharashtra Debt Relief Act, 1975, which liquidated rural debts, was therefore upheld as constitutional.",
        exp_ta="பதேச்சந்த் ஹிம்மத்லால் (1977) வழக்கில் உச்ச நீதிமன்றம், ஏழைகளைச் சுரண்டும் அநியாயக் கந்துவட்டி சரத்து 301-ன் கீழான 'வர்த்தகம்' அல்ல என்றும், கிராமப்புற கடன்களை ரத்து செய்த மகாராஷ்டிர கடன் நிவாரணச் சட்டம் 1975 அரசியலமைப்பு ரீதியாகச் செல்லும் என்றும் தீர்ப்பளித்தது.",
        why_a_en="Option A is correct; exploitative moneylending does not enjoy Article 301 protection.",
        why_a_ta="விருப்பம் A சரியானது; சுரண்டல் வட்டித் தொழில் சரத்து 301 பாதுகாப்பைப் பெறாது.",
        why_b_en="Option B is incorrect.",
        why_b_ta="விருப்பம் B தவறானது.",
        why_c_en="Option C is incorrect; moneylending is Entry 30 List II (State List).",
        why_c_ta="விருப்பம் C தவறானது; கடன் வழங்குதல் மாநிலப் பட்டியல் பதிவு 30 ஆகும்.",
        why_d_en="Option D is incorrect.",
        why_d_ta="விருப்பம் D தவறானது.",
        tip_en="Fatehchand (1977): Social welfare legislation liquidating usurious debts does NOT violate Article 301.",
        tip_ta="பதேச்சந்த் (1977): கந்துவட்டிக் கடன்களை ரத்து செய்யும் சமூக நலச் சட்டங்கள் சரத்து 301-ஐ மீறாது.",
        fact_en="Justice V.R. Krishna Iyer authored the eloquent judgment emphasizing that freedom of trade cannot protect the exploitation of the weak.",
        fact_ta="நீதிபதி வி.ஆர். கிருஷ்ண ஐயர் தனது வரலாற்றுத் தீர்ப்பில் வர்த்தக சுதந்திரம் ஏழைகளைச் சுரண்டுவதைப் பாதுகாக்க முடியாது என்று வலியுறுத்தினார்."
    ))

    # 065 - Key B (Hard)
    qs.append(make_q(
        num=65, diff="Hard", qtype="Concept MCQ", subtopic="Inter-State Trade and Commerce",
        en_stem="In Indian Cement v. State of Andhra Pradesh (1988), why did the Supreme Court strike down the Andhra Pradesh Government's notification reducing sales tax exclusively on cement manufactured within the State?",
        ta_stem="இந்தியன் சிமெண்ட் எதிர் ஆந்திரப் பிரதேச மாநிலம் (1988) வழக்கில், மாநிலத்திற்குள் உற்பத்தியாகும் சிமெண்டிற்கு மட்டும் விற்பனை வரியைக் குறைத்த ஆந்திர அரசின் அறிவிக்கையை உச்ச நீதிமன்றம் ஏன் ரத்து செய்தது?",
        en_a="Because cement is an exclusive subject in the Union List", ta_a="ஏனெனில் சிமெண்ட் மத்தியப் பட்டியலில் உள்ள ஒரு பிரத்யேக துறை",
        en_b="Because creating a tax disparity in favor of local manufacturers against imported cement violates Article 304(a) and impedes the free flow of inter-state trade under Article 301", ta_b="வெளிமாநில சிமெண்டிற்கு எதிராக உள்ளூர் உற்பத்தியாளர்களுக்கு சாதகமாக வரி வேறுபாட்டை உருவாக்குவது சரத்து 304(a)-ஐ மீறுகிறது மற்றும் சரத்து 301-ன் கீழான தடையற்ற வர்த்தகத்தைத் தடுக்கிறது",
        en_c="Because the notification lacked the signature of the Chief Minister", ta_c="ஏனெனில் அறிவிக்கையில் முதலமைச்சரின் கையொப்பம் இல்லை",
        en_d="Because the State of Andhra Pradesh had not obtained a loan from the World Bank", ta_d="ஏனெனில் ஆந்திரப் பிரதேச மாநிலம் உலக வங்கியிடமிருந்து கடன் பெறவில்லை",
        correct_key="B",
        exp_en="In Indian Cement (1988), the Supreme Court struck down the AP notification that reduced sales tax on local cement from 13.75% to 4% while maintaining higher rates on cement imported from neighboring states. This created hostile tariff discrimination violating Article 304(a) and Article 301.",
        exp_ta="இந்தியன் சிமெண்ட் (1988) வழக்கில் உச்ச நீதிமன்றம், உள்ளூர் சிமெண்டிற்கு மட்டும் விற்பனை வரியை 13.75% இலிருந்து 4% ஆகக் குறைத்து, அண்டை மாநில சிமெண்டிற்கு அதிக வரியை வைத்திருந்த ஆந்திர அரசின் அறிவிக்கையை ரத்து செய்தது. இது சரத்து 304(a) மற்றும் 301-ஐ அப்பட்டமாக மீறியது.",
        why_a_en="Option A is incorrect; manufacture is a state matter and sales tax was Entry 54 List II.",
        why_a_ta="விருப்பம் A தவறானது; விற்பனை வரி மாநிலப் பட்டியலில் இருந்தது.",
        why_b_en="Option B is the exact holding of the Supreme Court.",
        why_b_ta="விருப்பம் B என்பது உச்ச நீதிமன்றத்தின் துல்லியமான தீர்ப்பாகும்.",
        why_c_en="Option C is trivial and incorrect.",
        why_c_ta="விருப்பம் C தவறானது.",
        why_d_en="Option D is irrelevant.",
        why_d_ta="விருப்பம் D தொடர்பற்றது.",
        tip_en="A state cannot use differential tax rates to create trade barriers or benefit local producers over out-of-state producers (Indian Cement case).",
        tip_ta="உள்ளூர் உற்பத்தியாளர்களுக்கு சாதகமாக வெளிமாநில பொருட்களுக்கு கூடுதல் வரி விதித்து வர்த்தகத் தடைகளை உருவாக்க முடியாது (இந்தியன் சிமெண்ட் வழக்கு).",
        fact_en="This principle ensures that India remains an economic union and single common market without internal protectionist barriers.",
        fact_ta="இந்தக் கொள்கை இந்தியா உள்நாட்டு வர்த்தகத் தடைகள் இல்லாத ஒற்றை பொதுவான சந்தையாக நீடிப்பதை உறுதி செய்கிறது."
    ))

    # 066 - Key C (Medium)
    qs.append(make_q(
        num=66, diff="Medium", qtype="Concept MCQ", subtopic="Inter-State Council",
        en_stem="What is the exact composition of the Standing Committee of the Inter-State Council as constituted by the Central Government?",
        ta_stem="மத்திய அரசால் அமைக்கப்பட்ட மாநிலங்களுக்கு இடையேயான கவுன்சிலின் நிலைக்குழுவின் சரியான கட்டமைப்பு என்ன?",
        en_a="Prime Minister as Chairman + 10 Chief Ministers", ta_a="பிரதமர் தலைவராக + 10 முதலமைச்சர்கள்",
        en_b="Union Home Minister as Chairman + all 28 Chief Ministers", ta_b="மத்திய உள்துறை அமைச்சர் தலைவராக + அனைத்து 28 முதலமைச்சர்கள்",
        en_c="Union Home Minister as Chairman + 5 Union Cabinet Ministers + 9 Chief Ministers nominated by the Chairman", ta_c="மத்திய உள்துறை அமைச்சர் தலைவராக + 5 மத்திய அமைச்சரவை அமைச்சர்கள் + தலைவரால் பரிந்துரைக்கப்படும் 9 முதலமைச்சர்கள்",
        en_d="Cabinet Secretary as Chairman + all Chief Secretaries of States", ta_d="அமைச்சரவைச் செயலாளர் தலைவராக + அனைத்து மாநிலத் தலைமைச் செயலாளர்கள்",
        correct_key="C",
        exp_en="The Standing Committee of the Inter-State Council comprises: Union Home Minister (Chairman), five Union Cabinet Ministers, and nine Chief Ministers nominated by the Chairman of the Inter-State Council.",
        exp_ta="மாநிலங்களுக்கு இடையேயான கவுன்சிலின் நிலைக்குழுவில்: மத்திய உள்துறை அமைச்சர் (தலைவர்), 5 மத்திய அமைச்சரவை அமைச்சர்கள் மற்றும் கவுன்சில் தலைவரால் நியமிக்கப்படும் 9 முதலமைச்சர்கள் உள்ளனர்.",
        why_a_en="Option A is incorrect; Home Minister chairs the Standing Committee, not PM.",
        why_a_ta="விருப்பம் A தவறானது; நிலைக்குழுவிற்கு உள்துறை அமைச்சரே தலைவர்.",
        why_b_en="Option B is incorrect; only 9 CMs are on the Standing Committee.",
        why_b_ta="விருப்பம் B தவறானது; 9 முதலமைச்சர்கள் மட்டுமே இதில் உள்ளனர்.",
        why_c_en="Option C is the exact composition: Home Minister + 5 Union Ministers + 9 Chief Ministers.",
        why_c_ta="விருப்பம் C என்பது சரியான கட்டமைப்பு: உள்துறை அமைச்சர் + 5 மத்திய அமைச்சர்கள் + 9 முதலமைச்சர்கள்.",
        why_d_en="Option D is incorrect; this is not a bureaucratic committee.",
        why_d_ta="விருப்பம் D தவறானது.",
        tip_en="Standing Committee of ISC: Union Home Minister (Chairman) + 5 Union Cabinet Ministers + 9 Chief Ministers.",
        tip_ta="ISC நிலைக்குழு: மத்திய உள்துறை அமைச்சர் (தலைவர்) + 5 மத்திய அமைச்சர்கள் + 9 முதலமைச்சர்கள்.",
        fact_en="The Standing Committee was set up in 1996 to maintain continuous consultation and process matters for the consideration of the Council.",
        fact_ta="கவுன்சிலின் பரிசீலனைக்கான விஷயங்களை தொடர்ச்சியாக விவாதித்துத் தயாரிக்க 1996 இல் நிலைக்குழு அமைக்கப்பட்டது."
    ))

    # 067 - Key D (Medium)
    qs.append(make_q(
        num=67, diff="Medium", qtype="Concept MCQ", subtopic="Commissions and Inter-State Relations",
        en_stem="The First Administrative Reforms Commission (1966-1969) under K. Hanumanthaiah recommended establishing an Inter-State Council under Article 263. For what specific duration did it propose the Council be appointed initially?",
        ta_stem="கே. ஹனுமந்தையா தலைமையிலான முதலாவது நிர்வாக சீர்திருத்த ஆணையம் (1966-1969) சரத்து 263-ன் கீழ் மாநிலங்களுக்கு இடையேயான கவுன்சிலை அமைக்கப் பரிந்துரைத்தது. ஆரம்பத்தில் எத்தனை காலத்திற்கு இந்த கவுன்சில் நியமிக்கப்பட வேண்டும் என்று அது முன்மொழிந்தது?",
        en_a="For an indefinite permanent duration immediately", ta_a="உடனடியாக ஒரு காலவரையறையற்ற நிரந்தர காலத்திற்கு",
        en_b="For exactly one year on a trial basis", ta_b="சோதனை அடிப்படையில் சரியாக ஒரு வருடத்திற்கு",
        en_c="For two years only during national emergencies", ta_c="தேசிய அவசரநிலைகளின் போது இரண்டு ஆண்டுகளுக்கு மட்டுமே",
        en_d="For a preliminary period of two years to evaluate its working before making it permanent", ta_d="நிரந்தரமாக்குவதற்கு முன்பு அதன் செயல்பாட்டை மதிப்பீடு செய்ய இரண்டு ஆண்டுகள் ஆரம்ப காலத்திற்கு",
        correct_key="D",
        exp_en="The First ARC in its 1969 report on Centre-State Relations recommended setting up an Inter-State Council under Article 263 on an experimental basis for a preliminary period of two years, to test its effectiveness in resolving federal tensions.",
        exp_ta="முதல் நிர்வாக சீர்திருத்த ஆணையம் (1969) கூட்டாட்சிப் பதற்றங்களைத் தீர்ப்பதில் அதன் செயல்திறனைச் சோதிப்பதற்காக ஆரம்பத்தில் இரண்டு ஆண்டுகள் சோதனைக் காலத்திற்கு கவுன்சிலை அமைக்கப் பரிந்துரைத்தது.",
        why_a_en="Option A was Sarkaria Commission's recommendation, not First ARC's.",
        why_a_ta="விருப்பம் A சர்க்காரியா ஆணையத்தின் பரிந்துரை, முதல் ARC-ன் பரிந்துரை அல்ல.",
        why_b_en="Option B is incorrect.",
        why_b_ta="விருப்பம் B தவறானது.",
        why_c_en="Option C is incorrect.",
        why_c_ta="விருப்பம் C தவறானது.",
        why_d_en="Option D is correct; First ARC specifically proposed a 2-year trial period.",
        why_d_ta="விருப்பம் D சரியானது; முதல் ARC குறிப்பாக 2 ஆண்டு சோதனைக் காலத்தை முன்மொழிந்தது.",
        tip_en="First ARC (1969) = 2-year experimental Inter-State Council. Sarkaria Commission (1988) = Permanent Council.",
        tip_ta="முதல் ARC (1969) = 2 ஆண்டு சோதனை மாநிலங்களுக்கு இடையேயான கவுன்சில். சர்க்காரியா ஆணையம் (1988) = நிரந்தர கவுன்சில்.",
        fact_en="The Central Government did not accept the First ARC's recommendation at the time, delaying the Council's creation until 1990.",
        fact_ta="அப்போதைய மத்திய அரசு முதல் ARC-ன் பரிந்துரையை ஏற்றுக்கொள்ளாததால், கவுன்சில் அமைப்பது 1990 வரை தாமதமானது."
    ))

    # 068 - Key A (Easy)
    qs.append(make_q(
        num=68, diff="Easy", qtype="Concept MCQ", subtopic="Commissions and Inter-State Relations",
        en_stem="The Rajamannar Committee (1971), constituted by the Government of Tamil Nadu, recommended which of the following regarding parliamentary legislation affecting the States?",
        ta_stem="தமிழ்நாடு அரசால் அமைக்கப்பட்ட ராஜமன்னார் குழு (1971), மாநிலங்களைப் பாதிக்கும் பாராளுமன்ற சட்டங்கள் தொடர்பாக பின்வருவனவற்றில் எதைப் பரிந்துரைத்தது?",
        en_a="Every Bill of national importance or affecting state interests should be referred to the Inter-State Council before being introduced in Parliament", ta_a="தேசிய முக்கியத்துவம் வாய்ந்த அல்லது மாநில நலன்களைப் பாதிக்கும் ஒவ்வொரு மசோதாவும் பாராளுமன்றத்தில் அறிமுகப்படுத்தப்படுவதற்கு முன்பு மாநிலங்களுக்கு இடையேயான கவுன்சிலுக்கு அனுப்பப்பட வேண்டும்",
        en_b="Parliament should be permanently stripped of all powers to legislate on List I subjects", ta_b="பட்டியல் I துறைகள் மீது சட்டம் இயற்றும் அனைத்து அதிகாரங்களும் பாராளுமன்றத்திடமிருந்து நிரந்தரமாகப் பறிக்கப்பட வேண்டும்",
        en_c="The Supreme Court should be abolished and replaced with state benches", ta_c="உச்ச நீதிமன்றம் ஒழிக்கப்பட்டு அதற்கு பதிலாக மாநில அமர்வுகள் அமைக்கப்பட வேண்டும்",
        en_d="Governors should be granted absolute monarchical powers over states", ta_d="மாநிலங்களின் மீது ஆளுநர்களுக்கு முழுமையான மன்னராட்சி அதிகாரங்கள் வழங்கப்பட வேண்டும்",
        correct_key="A",
        exp_en="The Rajamannar Committee strongly recommended that an Inter-State Council should be constituted immediately under Article 263, and that every Bill of national importance or affecting one or more States should be placed before it for consideration before introduction in Parliament.",
        exp_ta="ராஜமன்னார் குழு, சரத்து 263-ன் கீழ் மாநிலங்களுக்கு இடையேயான கவுன்சில் உடனடியாக அமைக்கப்பட வேண்டும் என்றும், மாநிலங்களைப் பாதிக்கும் ஒவ்வொரு மசோதாவும் பாராளுமன்றத்தில் தாக்கல் செய்யப்படும் முன் கவுன்சிலின் முன் வைக்கப்பட வேண்டும் என்றும் வலுவாகப் பரிந்துரைத்தது.",
        why_a_en="Option A is the exact landmark recommendation of the Rajamannar Committee.",
        why_a_ta="விருப்பம் A என்பது ராஜமன்னார் குழுவின் வரலாற்றுச் சிறப்புமிக்க முக்கிய பரிந்துரையாகும்.",
        why_b_en="Option B is absurd; List I was not sought to be abolished entirely.",
        why_b_ta="விருப்பம் B தவறானது; பட்டியல் I-ஐ ஒழிக்கக் கோரவில்லை.",
        why_c_en="Option C is incorrect.",
        why_c_ta="விருப்பம் C தவறானது.",
        why_d_en="Option D is contrary to Rajamannar's recommendation to curb gubernatorial discretion.",
        why_d_ta="விருப்பம் D ஆளுநர் அதிகாரத்தைக் குறைக்கக் கோரிய குழுவின் கருத்திற்கு எதிரானது.",
        tip_en="Rajamannar Committee (1971) = Pre-legislative consultation with Inter-State Council on all Bills affecting States.",
        tip_ta="ராஜமன்னார் குழு (1971) = மாநிலங்களைப் பாதிக்கும் அனைத்து மசோதாக்கள் மீதும் அறிமுகத்திற்கு முன்பே கவுன்சிலுடன் ஆலோசனை.",
        fact_en="The Rajamannar Committee also recommended the deletion of Articles 356, 357, and 365 regarding President's Rule.",
        fact_ta="குடியரசுத் தலைவர் ஆட்சி தொடர்பான சரத்துகள் 356, 357 மற்றும் 365 ஆகியவற்றை நீக்க வேண்டும் என்றும் ராஜமன்னார் குழு பரிந்துரைத்தது."
    ))

    # 069 - Key B (Easy)
    qs.append(make_q(
        num=69, diff="Easy", qtype="Concept MCQ", subtopic="Commissions and Inter-State Relations",
        en_stem="The historic Anandpur Sahib Resolution, adopted in October 1973 by the Shiromani Akali Dal, demanded restricting the authority of the Central Government to which four subjects?",
        ta_stem="அக்டோபர் 1973 இல் சிரோமணி அகாலி தளத்தால் ஏற்றுக்கொள்ளப்பட்ட வரலாற்றுச் சிறப்புமிக்க ஆனந்த்பூர் சாகிப் தீர்மானம், மத்திய அரசின் அதிகாரத்தை எந்த நான்கு துறைகளுக்கு மட்டுமே மட்டுப்படுத்த வேண்டும் என்று கோரியது?",
        en_a="Agriculture, Health, Education, and Police", ta_a="விவசாயம், சுகாதாரம், கல்வி மற்றும் காவல் துறை",
        en_b="Defence, Foreign Affairs, Communications, and Currency", ta_b="பாதுகாப்பு, வெளியுறவு, தகவல் தொடர்பு மற்றும் நாணயம்",
        en_c="Railways, Shipping, Aviation, and Space", ta_c="ரயில்வே, கப்பல் போக்குவரத்து, விமானப் போக்குவரத்து மற்றும் விண்வெளி",
        en_d="Forests, Fisheries, Mining, and Waterways", ta_d="காடுகள், மீன்வளம், சுரங்கம் மற்றும் நீர்வழிப் பாதைகள்",
        correct_key="B",
        exp_en="The Anandpur Sahib Resolution (1973) demanded a true federal structure wherein the Central jurisdiction should be restricted exclusively to four departments: Defence, Foreign Affairs, Communications, and Currency. All other residual powers should vest in the States.",
        exp_ta="ஆனந்த்பூர் சாகிப் தீர்மானம் (1973) உண்மையான கூட்டாட்சிக் கட்டமைப்பைக் கோரியது; அதில் மத்திய அரசின் அதிகாரம் பாதுகாப்பு, வெளியுறவு, தகவல் தொடர்பு மற்றும் நாணயம் ஆகிய நான்கு துறைகளுக்கு மட்டுமே மட்டுப்படுத்தப்பட வேண்டும் என்றும், மற்ற அனைத்து அதிகாரங்களும் மாநிலங்களுக்கே இருக்க வேண்டும் என்றும் கோரியது.",
        why_a_en="Option A consists of State List subjects.",
        why_a_ta="விருப்பம் A மாநிலப் பட்டியல் துறைகள்.",
        why_b_en="Option B is the famous four-subject formulation of the Anandpur Sahib Resolution.",
        why_b_ta="விருப்பம் B என்பது ஆனந்த்பூர் சாகிப் தீர்மானத்தின் புகழ்பெற்ற நான்கு துறைகள் ஆகும்.",
        why_c_en="Option C is incorrect.",
        why_c_ta="விருப்பம் C தவறானது.",
        why_d_en="Option D is incorrect.",
        why_d_ta="விருப்பம் D தவறானது.",
        tip_en="Anandpur Sahib (1973) = Union limited to Defence, Foreign Affairs, Communications, Currency (like Cabinet Mission Plan).",
        tip_ta="ஆனந்த்பூர் சாகிப் (1973) = மத்திய அரசுக்கு பாதுகாப்பு, வெளியுறவு, தகவல் தொடர்பு, நாணயம் மட்டுமே.",
        fact_en="This was one of the most radical federal restructuring proposals in post-independence Indian political history.",
        fact_ta="சுதந்திரத்திற்குப் பிந்தைய இந்திய அரசியல் வரலாற்றில் மிகவும் தீவிரமான கூட்டாட்சி மறுசீரமைப்பு முன்மொழிவுகளில் இதுவும் ஒன்றாகும்."
    ))

    # 070 - Key C (Easy)
    qs.append(make_q(
        num=70, diff="Easy", qtype="Concept MCQ", subtopic="Commissions and Inter-State Relations",
        en_stem="The West Bengal Memorandum on Centre-State Relations, published by the Left Front Government in December 1977, proposed that what percentage of total tax revenues collected by the Centre should be devolved to the States?",
        ta_stem="டிசம்பர் 1977 இல் இடது முன்னணி அரசால் வெளியிடப்பட்ட மத்திய-மாநில உறவுகள் குறித்த மேற்கு வங்க நினைவுக் குறிப்பு, மத்திய அரசால் வசூலிக்கப்படும் மொத்த வரி வருவாயில் எத்தனை சதவீதம் மாநிலங்களுக்குப் பகிர்ந்தளிக்கப்பட வேண்டும் என்று முன்மொழிந்தது?",
        en_a="25%", ta_a="25%",
        en_b="50%", ta_b="50%",
        en_c="75%", ta_c="75%",
        en_d="100%", ta_d="100%",
        correct_key="C",
        exp_en="The West Bengal Memorandum (1977) suggested that 75% of the total revenue raised by the Centre from all sources for each year should be allocated to the States to correct the acute vertical fiscal imbalance.",
        exp_ta="செங்குத்து நிதி சமநிலையின்மையை சரிசெய்வதற்காக, மத்திய அரசால் அனைத்து வழிகளிலும் திரட்டப்படும் மொத்த வரி வருவாயில் 75% மாநிலங்களுக்குப் பகிர்ந்தளிக்கப்பட வேண்டும் என்று மேற்கு வங்க நினைவுக் குறிப்பு (1977) முன்மொழிந்தது.",
        why_a_en="Option A is too low.",
        why_a_ta="விருப்பம் A மிகவும் குறைவானது.",
        why_b_en="Option B is incorrect.",
        why_b_ta="விருப்பம் B தவறானது.",
        why_c_en="Option C is correct; 75% was the exact share proposed in the 1977 memorandum.",
        why_c_ta="விருப்பம் C சரியானது; 75% என்பது 1977 குறிப்பில் முன்மொழியப்பட்ட சரியான பங்காகும்.",
        why_d_en="Option D is unrealistic and not proposed.",
        why_d_ta="விருப்பம் D சாத்தியமற்றது மற்றும் முன்மொழியப்படவில்லை.",
        tip_en="West Bengal Memorandum (1977) = 75% tax devolution to States + Word 'Union' to be replaced by 'Federation'.",
        tip_ta="மேற்கு வங்க நினைவுக் குறிப்பு (1977) = மாநிலங்களுக்கு 75% வரிப் பகிர்வு + 'ஒன்றியம்' என்ற சொல்லுக்குப் பதில் 'கூட்டாட்சி' என மாற்றக் கோரியது.",
        fact_en="The memorandum also demanded that the preamble to the Constitution should be modified to declare India a 'Sovereign, Democratic Republic of Federal character'.",
        fact_ta="இந்தக் குறிப்பு இந்தியாவை ஒரு 'கூட்டாட்சித் தன்மை கொண்ட இறையாண்மைமிக்க ஜனநாயகக் குடியரசு' என்று அறிவிக்க முகப்புரையைத் திருத்த வேண்டும் என்றும் கோரியது."
    ))

    # 071 - Key D (Hard)
    qs.append(make_q(
        num=71, diff="Hard", qtype="Concept MCQ", subtopic="Inter-State Water Disputes",
        en_stem="In State of Tamil Nadu v. State of Kerala (2014), on what primary constitutional basis did the 5-judge Constitution Bench strike down the Kerala Irrigation and Water Conservation (Amendment) Act, 2006 regarding Mullaperiyar Dam?",
        ta_stem="தமிழ்நாடு மாநிலம் எதிர் கேரள மாநிலம் (2014) வழக்கில், முல்லைப் பெரியாறு அணை தொடர்பாக கேரள பாசனம் மற்றும் நீர் பாதுகாப்பு (திருத்தச்) சட்டம் 2006-ஐ 5 நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வு எந்த முதன்மை அரசியலமைப்பு அடிப்படையில் ரத்து செய்தது?",
        en_a="Violation of the Right to Equality of the fish population in the reservoir", ta_a="நீர்த்தேக்கத்தில் உள்ள மீன் இனங்களின் சமத்துவ உரிமை மீறல்",
        en_b="Failure of the Kerala Governor to seek permission from the Zonal Council", ta_b="மண்டல கவுன்சிலிடம் அனுமதி பெற கேரள ஆளுநர் தவறியது",
        en_c="Lack of legislative competence under Entry 17 of List II", ta_c="பட்டியல் II-ன் பதிவு 17-ன் கீழ் சட்டமன்றத் திறன் இல்லாதது",
        en_d="Violation of the doctrine of Separation of Powers, as the State Legislature enacted a law to overturn and nullify a binding inter-state judicial decree of the Supreme Court", ta_d="அதிகாரப் பகிர்வுக் கோட்பாட்டின் மீறல்; உச்ச நீதிமன்றத்தின் கட்டுப்படுத்தும் மாநிலங்களுக்கு இடையேயான நீதித்துறை தீர்ப்பை ரத்து செய்வதற்காக மாநில சட்டமன்றம் ஒரு சட்டத்தை இயற்றியது",
        correct_key="D",
        exp_en="The Supreme Court 5-judge bench held that the Kerala legislation violated the separation of powers. A legislature cannot sit in judgment over an inter-state judicial verdict (the Feb 2006 ruling allowing 142 ft) and enact an amendment to nullify that judicial decision between two disputing States.",
        exp_ta="உச்ச நீதிமன்றத்தின் 5 நீதிபதிகள் அமர்வு, கேரள சட்டம் அதிகாரப் பகிர்வுக் கோட்பாட்டை மீறியதாகத் தீர்ப்பளித்தது. ஒரு சட்டமன்றம் உச்ச நீதிமன்றத்தின் நீதித்துறைத் தீர்ப்பை (142 அடிக்கு அனுமதித்த பிப்ரவரி 2006 தீர்ப்பு) ரத்து செய்யும் வகையில் சட்டம் இயற்றி தலையிட முடியாது.",
        why_a_en="Option A is frivolous.",
        why_a_ta="விருப்பம் A பொருத்தமற்றது.",
        why_b_en="Option B is incorrect; Zonal Councils have no veto over state legislation.",
        why_b_ta="விருப்பம் B தவறானது; மண்டல கவுன்சிலுக்கு இதில் அதிகாரம் இல்லை.",
        why_c_en="Option C is incomplete; the primary violation was of separation of powers and judicial finality.",
        why_c_ta="விருப்பம் C முழுமையற்றது; முதன்மைக் காரணம் அதிகாரப் பகிர்வு மீறல்.",
        why_d_en="Option D is the exact core holding of the Constitution Bench.",
        why_d_ta="விருப்பம் D என்பது அரசியலமைப்பு அமர்வின் துல்லியமான முக்கிய தீர்ப்பாகும்.",
        tip_en="A state legislature cannot declare a judgment of the Supreme Court invalid or enact a law to undo a judicial decree (State of TN v. State of Kerala, 2014).",
        tip_ta="ஒரு மாநில சட்டமன்றம் உச்ச நீதிமன்றத்தின் தீர்ப்பை செல்லாது என அறிவிக்கவோ அல்லது அதை ரத்து செய்ய சட்டம் இயற்றவோ முடியாது (2014 முல்லைப் பெரியாறு வழக்கு).",
        fact_en="The judgment reaffirmed that the 1886 Periyar Lease Deed was legally valid and binding on both States.",
        fact_ta="இந்தத் தீர்ப்பு 1886 பெரியாறு குத்தகை ஒப்பந்தம் சட்டப்பூர்வமாகச் செல்லுபடியாகும் என்றும் இரு மாநிலங்களையும் கட்டுப்படுத்தும் என்றும் மீண்டும் உறுதிப்படுத்தியது."
    ))

    # 072 - Key D (Hard)
    qs.append(make_q(
        num=72, diff="Hard", qtype="Concept MCQ", subtopic="Inter-State Water Disputes",
        en_stem="Which high-powered Empowered Committee was appointed by the Supreme Court in April 2010 to comprehensively investigate the safety and water level of the Mullaperiyar Dam?",
        ta_stem="முல்லைப் பெரியாறு அணையின் பாதுகாப்பு மற்றும் நீர்மட்டத்தை விரிவாக ஆய்வு செய்வதற்காக ஏப்ரல் 2010 இல் உச்ச நீதிமன்றத்தால் நியமிக்கப்பட்ட உயர்மட்ட அதிகாரமளிக்கப்பட்ட குழு எது?",
        en_a="Justice Chittatosh Mookerjee Committee", ta_a="நீதிபதி சித்ததோஷ் முகர்ஜி குழு",
        en_b="Justice R.S. Bachawat Committee", ta_b="நீதிபதி ஆர்.எஸ். பசாவத் குழு",
        en_c="Justice K.S. Hegde Committee", ta_c="நீதிபதி கே.எஸ். ஹெக்டே குழு",
        en_d="Justice A.S. Anand Empowered Committee", ta_d="நீதிபதி ஏ.எஸ். ஆனந்த் அதிகாரமளிக்கப்பட்ட குழு",
        correct_key="D",
        exp_en="The Supreme Court in April 2010 constituted a five-member Empowered Committee headed by former Chief Justice of India Justice A.S. Anand (with former Supreme Court judge Justice K.T. Thomas representing Kerala and Justice A.R. Lakshmanan representing Tamil Nadu) to examine all aspects of the Mullaperiyar Dam.",
        exp_ta="உச்ச நீதிமன்றம் ஏப்ரல் 2010 இல் முன்னாள் இந்திய தலைமை நீதிபதி ஏ.எஸ். ஆனந்த் தலைமையில் (கேரளா சார்பில் நீதிபதி கே.டி. தாமஸ் மற்றும் தமிழ்நாடு சார்பில் நீதிபதி ஏ.ஆர். லட்சுமணன் ஆகியோர் இடம்பெற்ற) 5 உறுப்பினர்களைக் கொண்ட அதிகாரமளிக்கப்பட்ட குழுவை அமைத்தது.",
        why_a_en="Option A was Chairman of the Cauvery Water Disputes Tribunal.",
        why_a_ta="விருப்பம் A காவிரி தீர்ப்பாயத்தின் தலைவர்.",
        why_b_en="Option B was Chairman of KWDT-I and Godavari tribunals.",
        why_b_ta="விருப்பம் B கிருஷ்ணா-I மற்றும் கோதாவரி தீர்ப்பாயங்களின் தலைவர்.",
        why_c_en="Option C is incorrect.",
        why_c_ta="விருப்பம் C தவறானது.",
        why_d_en="Option D is correct; Justice A.S. Anand headed the Empowered Committee on Mullaperiyar.",
        why_d_ta="விருப்பம் D சரியானது; நீதிபதி ஏ.எஸ். ஆனந்த் முல்லைப் பெரியாறு அதிகாரமளிக்கப்பட்ட குழுவிற்கு தலைமை தாங்கினார்.",
        tip_en="Mullaperiyar Empowered Committee (2010-2012) = Headed by Justice A.S. Anand (former CJI). Reported dam is hydrologically and seismically safe at 142 ft.",
        tip_ta="முல்லைப் பெரியாறு அதிகாரமளிக்கப்பட்ட குழு (2010-2012) = நீதிபதி ஏ.எஸ். ஆனந்த் தலைமை. அணை 142 அடியில் பாதுகாப்பானது என அறிக்கை அளித்தது.",
        fact_en="The Empowered Committee submitted its report in April 2012, finding the dam structurally and seismically safe, which formed the bedrock of the 2014 SC judgment.",
        fact_ta="இந்தக் குழு ஏப்ரல் 2012 இல் அணை கட்டமைப்பு ரீதியாகவும் பூகம்ப ரீதியாகவும் பாதுகாப்பானது என அறிக்கை சமர்ப்பித்தது; இதுவே 2014 உச்ச நீதிமன்றத் தீர்ப்பிற்கு அடிப்படையாக அமைந்தது."
    ))

    # 073 - Key A (Easy)
    qs.append(make_q(
        num=73, diff="Easy", qtype="Concept MCQ", subtopic="Inter-State Border Disputes",
        en_stem="The decades-old Belgaum (Belagavi) border dispute is an inter-state territorial controversy between which two neighboring States?",
        ta_stem="பல தசாப்தங்களாக நீடிக்கும் பெல்காம் (பெலகாவி) எல்லைத் தகராறு எந்த இரண்டு அண்டை மாநிலங்களுக்கு இடையேயான பிராந்திய சர்ச்சையாகும்?",
        en_a="Maharashtra and Karnataka", ta_a="மகாராஷ்டிரா மற்றும் கர்நாடகா",
        en_b="Karnataka and Kerala", ta_b="கர்நாடகா மற்றும் கேரளா",
        en_c="Tamil Nadu and Andhra Pradesh", ta_c="தமிழ்நாடு மற்றும் ஆந்திரப் பிரதேசம்",
        en_d="Odisha and West Bengal", ta_d="ஒடிசா மற்றும் மேற்கு வங்கம்",
        correct_key="A",
        exp_en="The Belgaum (Belagavi) dispute is a prominent linguistic boundary dispute between Maharashtra and Karnataka. Maharashtra claims Belgaum along with 814 Marathi-speaking villages that were merged with Mysore (Karnataka) under the States Reorganisation Act, 1956.",
        exp_ta="பெல்காம் (பெலகாவி) எல்லைத் தகராறு மகாராஷ்டிரா மற்றும் கர்நாடகா இடையேயான ஒரு முக்கிய மொழிவாரி எல்லைத் தகராறாகும். மாநில மறுசீரமைப்புச் சட்டம் 1956-ன் கீழ் மைசூருடன் (கர்நாடகா) இணைக்கப்பட்ட பெல்காம் மற்றும் 814 மராத்தி பேசும் கிராமங்களை மகாராஷ்டிரா உரிமை கோருகிறது.",
        why_a_en="Option A is correct; Belgaum dispute is between Maharashtra and Karnataka.",
        why_a_ta="விருப்பம் A சரியானது; பெல்காம் தகராறு மகாராஷ்டிரா மற்றும் கர்நாடகா தொடர்பானது.",
        why_b_en="Option B involves the Kasaragod border dispute.",
        why_b_ta="விருப்பம் B காசர்கோடு எல்லைத் தகராறு தொடர்பானது.",
        why_c_en="Option C was resolved by the Pataskar Award in 1957.",
        why_c_ta="விருப்பம் C 1957 படாஸ்கர் தீர்ப்பால் தீர்க்கப்பட்டது.",
        why_d_en="Option D is incorrect.",
        why_d_ta="விருப்பம் D தவறானது.",
        tip_en="Belgaum (Belagavi) = Maharashtra vs Karnataka. Kasaragod = Karnataka vs Kerala.",
        tip_ta="பெல்காம் (பெலகாவி) = மகாராஷ்டிரா vs கர்நாடகா. காசர்கோடு = கர்நாடகா vs கேரளா.",
        fact_en="Maharashtra filed an original suit in the Supreme Court under Article 131 in 2004 claiming territorial jurisdiction over Belgaum.",
        fact_ta="பெல்காம் மீது பிராந்திய உரிமை கோரி மகாராஷ்டிரா 2004 இல் சரத்து 131-ன் கீழ் உச்ச நீதிமன்றத்தில் அசல் வழக்கை தொடர்ந்தது."
    ))

    # 074 - Key B (Medium)
    qs.append(make_q(
        num=74, diff="Medium", qtype="Concept MCQ", subtopic="Inter-State Border Disputes",
        en_stem="The Kasaragod border dispute involves a territorial claim between which two Southern States?",
        ta_stem="காசர்கோடு எல்லைத் தகராறு எந்த இரண்டு தென்னிந்திய மாநிலங்களுக்கு இடையேயான பிராந்தியக் கோரிக்கையை உள்ளடக்கியது?",
        en_a="Tamil Nadu and Kerala", ta_a="தமிழ்நாடு மற்றும் கேரளா",
        en_b="Karnataka and Kerala", ta_b="கர்நாடகா மற்றும் கேரளா",
        en_c="Andhra Pradesh and Odisha", ta_c="ஆந்திரப் பிரதேசம் மற்றும் ஒடிசா",
        en_d="Telangana and Karnataka", ta_d="தெலுங்கானா மற்றும் கர்நாடகா",
        correct_key="B",
        exp_en="The Kasaragod dispute involves Karnataka and Kerala. Kasaragod was transferred to Kerala upon reorganisation in 1956, but Karnataka claimed that northern Kasaragod (north of the Chandragiri river) has Kannada-speaking majority and should belong to Karnataka.",
        exp_ta="காசர்கோடு தகராறு கர்நாடகா மற்றும் கேரளா இடையேயானது. 1956 மறுசீரமைப்பின் போது காசர்கோடு கேரளாவுடன் இணைக்கப்பட்டது; ஆனால் சந்திரகிரி நதிக்கு வடக்கே உள்ள பகுதிகளில் கன்னட மொழி பேசுவோர் அதிகமாக இருப்பதால் அதைத் தனக்குத் தர வேண்டும் என்று கர்நாடகா கோருகிறது.",
        why_a_en="Option A is incorrect.",
        why_a_ta="விருப்பம் A தவறானது.",
        why_b_en="Option B is correct; Kasaragod dispute is between Karnataka and Kerala.",
        why_b_ta="விருப்பம் B சரியானது; காசர்கோடு தகராறு கர்நாடகா மற்றும் கேரளா தொடர்பானது.",
        why_c_en="Option C involves Kotia village dispute.",
        why_c_ta="விருப்பம் C கோட்டியா கிராம தகராறு தொடர்பானது.",
        why_d_en="Option D is incorrect.",
        why_d_ta="விருப்பம் D தவறானது.",
        tip_en="Kasaragod boundary dispute = Karnataka vs Kerala. Mahajan Commission recommended transferring Kasaragod north of Chandragiri river to Karnataka.",
        tip_ta="காசர்கோடு எல்லைத் தகராறு = கர்நாடகா vs கேரளா. சந்திரகிரி நதிக்கு வடக்கே உள்ள காசர்கோட்டை கர்நாடகாவிற்கு மாற்ற மகாஜன் ஆணையம் பரிந்துரைத்தது.",
        fact_en="Kerala rejected the Mahajan Commission's recommendation to transfer Kasaragod, maintaining the status quo.",
        fact_ta="காசர்கோட்டை மாற்றும் மகாஜன் ஆணையத்தின் பரிந்துரையை கேரளா நிராகரித்து, தற்போதைய நிலையையே தொடர்கிறது."
    ))

    # 075 - Key C (Medium)
    qs.append(make_q(
        num=75, diff="Medium", qtype="Concept MCQ", subtopic="Inter-State Border Disputes",
        en_stem="The Mahajan Commission, constituted by the Central Government in October 1966 under former CJI Mehar Chand Mahajan, was tasked with resolving boundary disputes between:",
        ta_stem="அக்டோபர் 1966 இல் முன்னாள் தலைமை நீதிபதி மெஹர் சந்த் மகாஜன் தலைமையில் மத்திய அரசால் அமைக்கப்பட்ட மகாஜன் ஆணையம், எந்த மாநிலங்களுக்கு இடையேயான எல்லைத் தகராறுகளைத் தீர்க்க பணிக்கப்பட்டது?",
        en_a="Assam and Nagaland", ta_a="அசாம் மற்றும் நாகாலாந்து",
        en_b="Punjab and Haryana", ta_b="பஞ்சாப் மற்றும் ஹரியானா",
        en_c="Maharashtra, Karnataka, and Kerala", ta_c="மகாராஷ்டிரா, கர்நாடகா மற்றும் கேரளா",
        en_d="Bihar and West Bengal", ta_d="பீகார் மற்றும் மேற்கு வங்கம்",
        correct_key="C",
        exp_en="The Mahajan Commission was appointed in October 1966 to investigate the inter-state boundary disputes involving Maharashtra, Mysore (now Karnataka), and Kerala (covering Belgaum, Nippani, Karwar, and Kasaragod).",
        exp_ta="மகாஜன் ஆணையம் அக்டோபர் 1966 இல் மகாராஷ்டிரா, மைசூர் (இப்போது கர்நாடகா) மற்றும் கேரளா (பெல்காம், நிப்பானி, கார்வார் மற்றும் காசர்கோடு உள்ளடக்கியது) எல்லைத் தகராறுகளை ஆய்வு செய்ய அமைக்கப்பட்டது.",
        why_a_en="Option A was investigated by the Sundaram Commission (1971).",
        why_a_ta="விருப்பம் A சுந்தரம் ஆணையத்தால் (1971) ஆய்வு செய்யப்பட்டது.",
        why_b_en="Option B was investigated by the Shah Commission (1966).",
        why_b_ta="விருப்பம் B ஷா ஆணையத்தால் (1966) ஆய்வு செய்யப்பட்டது.",
        why_c_en="Option C is correct; Mahajan Commission dealt with Maharashtra-Karnataka-Kerala boundary disputes.",
        why_c_ta="விருப்பம் C சரியானது; மகாஜன் ஆணையம் மகாராஷ்டிரா-கர்நாடகா-கேரளா எல்லைத் தகராறுகளைக் கையாண்டது.",
        why_d_en="Option D is incorrect.",
        why_d_ta="விருப்பம் D தவறானது.",
        tip_en="Mahajan Commission (1966) = Maharashtra, Karnataka (Mysore), and Kerala border disputes.",
        tip_ta="மகாஜன் ஆணையம் (1966) = மகாராஷ்டிரா, கர்நாடகா மற்றும் கேரளா எல்லைத் தகராறுகள்.",
        fact_en="The Mahajan Commission submitted its report in August 1967, recommending that Belgaum continue in Karnataka while transferring Nippani to Maharashtra.",
        fact_ta="மகாஜன் ஆணையம் ஆகஸ்ட் 1967 இல் அறிக்கை சமர்ப்பித்து, பெல்காம் கர்நாடகாவிலேயே நீடிக்கவும், நிப்பானியை மகாராஷ்டிராவிற்கு மாற்றவும் பரிந்துரைத்தது."
    ))

    return qs

if __name__ == "__main__":
    b3 = get_batch3()
    print(f"Batch 3 count: {len(b3)}")
    from collections import Counter
    print("Keys:", Counter([q["correct_answer"] for q in b3]))
    print("Diffs:", Counter([q["difficulty"] for q in b3]))
