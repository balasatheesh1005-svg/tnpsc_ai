# -*- coding: utf-8 -*-
"""
Batch 2: Grand Test MCQs ISR_GT_026 to ISR_GT_050
Key distribution: A: 6, B: 7, C: 6, D: 6 (Total: 25)
Difficulty: 15 Medium, 10 Hard
"""

from isr_gt_helper import make_q

def get_batch2():
    qs = []

    # 026 - Key A (Medium)
    qs.append(make_q(
        num=26, diff="Medium", qtype="Concept MCQ", subtopic="Inter-State Council",
        en_stem="In the context of the constitutional powers of the Inter-State Council under Article 263, what is the legal character of its advice and recommendations?",
        ta_stem="அரசியலமைப்பின் சரத்து 263-ன் கீழ் மாநிலங்களுக்கு இடையேயான கவுன்சிலின் அதிகாரங்கள் தொடர்பாக, அதன் ஆலோசனைகள் மற்றும் பரிந்துரைகளின் சட்டரீதியான தன்மை என்ன?",
        en_a="Purely advisory and not legally binding on either the Union or the State Governments", ta_a="முற்றிலும் ஆலோசனையானது மற்றும் மத்திய அல்லது மாநில அரசுகளை சட்டப்பூர்வமாகக் கட்டுப்படுத்தாது",
        en_b="Legally binding orders enforceable through writ jurisdiction under Article 32", ta_b="சரத்து 32-ன் கீழ் நீதிப்பேராணை மூலம் செயல்படுத்தக்கூடிய சட்டப்பூர்வக் கட்டுப்படுத்தும் ஆணைகள்",
        en_c="Direct legislative decrees having the force of an Ordinance under Article 123", ta_c="சரத்து 123-ன் கீழ் அவசரச் சட்டத்தின் சக்தியைக் கொண்ட நேரடி சட்டமன்றக் கட்டளைகள்",
        en_d="Binding arbitration awards subject to judicial appeal only before the International Court of Justice", ta_d="சர்வதேச நீதிமன்றத்தின் முன் மட்டுமே மேல்முறையீடு செய்யக்கூடிய கட்டுப்படுத்தும் நடுவர் தீர்ப்புகள்",
        correct_key="A",
        exp_en="The function of the Inter-State Council under Article 263 is strictly advisory. It can deliberate, investigate, and recommend policies to foster federal coordination, but its recommendations are not legally binding.",
        exp_ta="சரத்து 263-ன் கீழ் மாநிலங்களுக்கு இடையேயான கவுன்சிலின் பணி முற்றிலும் ஆலோசனையானது. இது கூட்டாட்சி ஒருங்கிணைப்பை வளர்ப்பதற்கான கொள்கைகளை விவாதிக்கலாம், ஆராயலாம் மற்றும் பரிந்துரைக்கலாம்; ஆனால் இதன் பரிந்துரைகள் சட்டப்பூர்வமாகக் கட்டுப்படுத்துபவை அல்ல.",
        why_a_en="Option A is correct; the Council has purely advisory jurisdiction.",
        why_a_ta="விருப்பம் A சரியானது; கவுன்சிலுக்கு ஆலோசனை அதிகாரம் மட்டுமே உள்ளது.",
        why_b_en="Option B is incorrect; its recommendations cannot be enforced as binding orders.",
        why_b_ta="விருப்பம் B தவறானது; இதன் பரிந்துரைகளை கட்டுப்படுத்தும் ஆணைகளாக நடைமுறைப்படுத்த முடியாது.",
        why_c_en="Option C is incorrect; it possesses no legislative or ordinance-making powers.",
        why_c_ta="விருப்பம் C தவறானது; இதற்கு சட்டமன்ற அல்லது அவசரச் சட்ட அதிகாரம் இல்லை.",
        why_d_en="Option D is incorrect; domestic federal matters do not go to the ICJ.",
        why_d_ta="விருப்பம் D தவறானது; உள்நாட்டு விவகாரங்கள் சர்வதேச நீதிமன்றத்திற்குச் செல்லாது.",
        tip_en="Article 263 = Advisory body. Article 131 = Binding judicial adjudication by Supreme Court.",
        tip_ta="சரத்து 263 = ஆலோசனை அமைப்பு. சரத்து 131 = உச்ச நீதிமன்றத்தின் கட்டுப்படுத்தும் நீதித்துறை தீர்ப்பு.",
        fact_en="Even in investigating disputes between states under Article 263(a), the Council can only tender advice, unlike courts which pronounce binding decrees.",
        fact_ta="சரத்து 263(a)-ன் கீழ் தகராறுகளை விசாரிக்கும் போது கூட, நீதிமன்றங்கள் போலன்றி கவுன்சில் ஆலோசனைகளை மட்டுமே வழங்க முடியும்."
    ))

    # 027 - Key B (Medium)
    qs.append(make_q(
        num=27, diff="Medium", qtype="Concept MCQ", subtopic="Inter-State Trade and Commerce",
        en_stem="Article 303(1) of the Constitution restricts the power of both Parliament and State Legislatures by prohibiting which of the following actions?",
        ta_stem="அரசியலமைப்பின் சரத்து 303(1) பாராளுமன்றம் மற்றும் மாநில சட்டமன்றங்கள் ஆகிய இரண்டின் அதிகாரத்தையும் பின்வரும் எந்தச் செயலைத் தடை செய்வதன் மூலம் கட்டுப்படுத்துகிறது?",
        en_a="Levying uniform excise duties on manufactured consumer goods", ta_a="உற்பத்தி செய்யப்படும் நுகர்வோர் பொருட்களின் மீது சீரான கலால் வரிகளை விதித்தல்",
        en_b="Making any law giving preference to one State over another or making discrimination between States by virtue of trade entries", ta_b="வர்த்தகப் பதிவுகளின் அடிப்படையில் ஒரு மாநிலத்திற்கு மற்றொரு மாநிலத்தை விட முன்னுரிமை அளிக்கும் அல்லது மாநிலங்களிடையே பாகுபாடு காட்டும் எந்தவொரு சட்டத்தையும் இயற்றுதல்",
        en_c="Regulating inter-state motor vehicles through transport permits", ta_c="போக்குவரத்து அனுமதிகள் மூலம் மாநிலங்களுக்கு இடையேயான மோட்டார் வாகனங்களை ஒழுங்குபடுத்துதல்",
        en_d="Imposing quarantine restrictions on diseased livestock entering a state", ta_d="மாநிலத்திற்குள் நுழையும் நோயுற்ற கால்நடைகள் மீது தனிமைப்படுத்தல் கட்டுப்பாடுகளை விதித்தல்",
        correct_key="B",
        exp_en="Article 303(1) explicitly prohibits Parliament and State Legislatures from making any law that gives preference to one state over another, or makes any discrimination between states, by virtue of any entry relating to trade and commerce in the Seventh Schedule.",
        exp_ta="சரத்து 303(1) பாராளுமன்றமும் மாநில சட்டமன்றங்களும் ஏழாவது அட்டவணையில் உள்ள வர்த்தகப் பதிவுகளின் மூலம் ஒரு மாநிலத்திற்கு முன்னுரிமை அளிக்கவோ அல்லது மாநிலங்களிடையே பாகுபாடு காட்டவோ சட்டம் இயற்றுவதைத் தடை செய்கிறது.",
        why_a_en="Option A is permitted under Union List taxing entries.",
        why_a_ta="விருப்பம் A மத்தியப் பட்டியல் வரிகளில் அனுமதிக்கப்படுகிறது.",
        why_b_en="Option B is the exact mandate of Article 303(1).",
        why_b_ta="விருப்பம் B என்பது சரத்து 303(1)-ன் நேரடி கட்டளையாகும்.",
        why_c_en="Option C is regulatory under Entry 35 List III.",
        why_c_ta="விருப்பம் C பொதுப்பட்டியல் பதிவு 35-ன் கீழான ஒழுங்குமுறை ஆகும்.",
        why_d_en="Option D is a valid public health / quarantine restriction.",
        why_d_ta="விருப்பம் D செல்லுபடியாகும் பொது சுகாதாரக் கட்டுப்பாடு.",
        tip_en="Article 303(1) prohibits preference or discrimination between States.",
        tip_ta="சரத்து 303(1) மாநிலங்களுக்கிடையே முன்னுரிமை அல்லது பாகுபாடு காட்டுவதைத் தடை செய்கிறது.",
        fact_en="Article 303 applies to both Parliament and State Legislatures, unlike Article 302 which applies only to Parliament.",
        fact_ta="பாராளுமன்றத்திற்கு மட்டுமே பொருந்தும் சரத்து 302 போலன்றி, சரத்து 303 பாராளுமன்றம் மற்றும் மாநில சட்டமன்றங்கள் இரண்டிற்கும் பொருந்தும்."
    ))

    # 028 - Key B (Hard)
    qs.append(make_q(
        num=28, diff="Hard", qtype="Concept MCQ", subtopic="Inter-State Trade and Commerce",
        en_stem="Under Article 303(2), Parliament (and NOT a State Legislature) can make discriminatory laws or give preference to one state over another under which specific circumstance?",
        ta_stem="சரத்து 303(2)-ன் கீழ், பாராளுமன்றம் (மாநில சட்டமன்றம் அல்ல) எந்த குறிப்பிட்ட சூழ்நிலையில் பாகுபாடான சட்டங்களை உருவாக்கலாம் அல்லது ஒரு மாநிலத்திற்கு முன்னுரிமை அளிக்கலாம்?",
        en_a="During national fiscal deficits exceeding targets", ta_a="இலக்குகளை விட தேசிய நிதிப் பற்றாக்குறை அதிகரிக்கும் போது",
        en_b="For dealing with a situation arising from scarcity of goods in any part of the territory of India", ta_b="இந்தியாவின் எந்தப் பகுதியிலும் நிலவும் பொருட்களின் தட்டுப்பாட்டினால் ஏற்படும் சூழ்நிலையைக் கையாள்வதற்காக",
        en_c="Whenever requested by a resolution of two or more State Governors", ta_c="இரண்டு அல்லது அதற்கு மேற்பட்ட மாநில ஆளுநர்கள் தீர்மானம் மூலம் கோரும் போதெல்லாம்",
        en_d="During the pendency of general elections to the Lok Sabha", ta_d="மக்களவைக்கான பொதுத் தேர்தல்கள் நடைபெறும் காலத்தில்",
        correct_key="B",
        exp_en="Article 303(2) contains an exception in favor of Parliament only: 'Nothing in clause (1) shall prevent Parliament from making any law giving any preference or making any discrimination if it is declared by such law that it is necessary to do so for the purpose of dealing with a situation arising from scarcity of goods in any part of the territory of India.'",
        exp_ta="சரத்து 303(2) பாராளுமன்றத்திற்கு மட்டுமே ஒரு விதிவிலக்கைக் கொண்டுள்ளது: இந்தியாவின் எந்தப் பகுதியிலும் பொருட்களின் தட்டுப்பாடு ஏற்படும் சூழ்நிலையைக் கையாள்வதற்காகத் தேவைப்பட்டால், பாராளுமன்றம் முன்னுரிமை அளிக்கவோ அல்லது பாகுபாடு காட்டவோ சட்டம் இயற்றலாம்.",
        why_a_en="Option A is incorrect; fiscal deficits do not justify discrimination under 303(2).",
        why_a_ta="விருப்பம் A தவறானது; நிதிப் பற்றாக்குறை இதற்குப் பொருந்தாது.",
        why_b_en="Option B is correct; scarcity of goods is the sole constitutional ground under 303(2).",
        why_b_ta="விருப்பம் B சரியானது; பண்டங்களின் தட்டுப்பாடு மட்டுமே சரத்து 303(2)-ன் கீழான ஒரே அரசியலமைப்பு காரணமாகும்.",
        why_c_en="Option C is incorrect; Governor resolutions do not trigger this power.",
        why_c_ta="விருப்பம் C தவறானது; ஆளுநர் தீர்மானங்கள் இதற்குப் பொருந்தாது.",
        why_d_en="Option D is incorrect; general elections have no bearing on Article 303(2).",
        why_d_ta="விருப்பம் D தவறானது; பொதுத் தேர்தல்களுக்கு இதில் தொடர்பில்லை.",
        tip_en="Article 303(2) = Parliament only + Scarcity of goods. State legislatures NEVER have this power.",
        tip_ta="சரத்து 303(2) = பாராளுமன்றத்திற்கு மட்டுமே + பண்டங்களின் தட்டுப்பாடு. மாநில சட்டமன்றங்களுக்கு இந்த அதிகாரம் ஒருபோதும் கிடையாது.",
        fact_en="This allows the Union Government to channel essential commodities like food grains or medicines to a drought-stricken state on priority.",
        fact_ta="இது வறட்சியால் பாதிக்கப்பட்ட ஒரு மாநிலத்திற்கு முன்னுரிமை அடிப்படையில் உணவு தானியங்கள் அல்லது மருந்துகளை அனுப்ப மத்திய அரசுக்கு உதவுகிறது."
    ))

    # 029 - Key C (Medium)
    qs.append(make_q(
        num=29, diff="Medium", qtype="Concept MCQ", subtopic="Public Acts, Records and Judicial Proceedings",
        en_stem="According to Article 261(2) of the Constitution, the manner in which and the conditions under which public acts, records, and judicial proceedings shall be proved shall be provided by:",
        ta_stem="அரசியலமைப்பின் சரத்து 261(2)-ன் படி, பொதுச் சட்டங்கள், ஆவணங்கள் மற்றும் நீதித்துறை நடவடிக்கைகள் நிரூபிக்கப்பட வேண்டிய விதம் மற்றும் நிபந்தனைகள் எதன் மூலம் வழங்கப்பட வேண்டும்?",
        en_a="Rules framed by the Supreme Court with the approval of the President", ta_a="குடியரசுத் தலைவரின் ஒப்புதலுடன் உச்ச நீதிமன்றத்தால் உருவாக்கப்பட்ட விதிகள்",
        en_b="Executive notifications issued by the Ministry of Law and Justice", ta_b="சட்டம் மற்றும் நீதி அமைச்சகம் வெளியிடும் நிர்வாக அறிவிப்புகள்",
        en_c="Law made by Parliament", ta_c="பாராளுமன்றத்தால் இயற்றப்பட்ட சட்டம்",
        en_d="Decrees passed by the respective State High Courts", ta_d="அந்தந்த மாநில உயர் நீதிமன்றங்கள் பிறப்பிக்கும் தீர்ப்புகள்",
        correct_key="C",
        exp_en="Article 261(2) provides: 'The manner in which and the conditions under which the acts, records and proceedings referred to in clause (1) shall be proved and the effect thereof determined shall be as provided by law made by Parliament.'",
        exp_ta="சரத்து 261(2) கூறுகிறது: 'பிரிவு (1)-ல் குறிப்பிடப்பட்டுள்ள சட்டங்கள், ஆவணங்கள் மற்றும் நடவடிக்கைகள் நிரூபிக்கப்பட வேண்டிய விதம், நிபந்தனைகள் மற்றும் அவற்றின் விளைவுகள் பாராளுமன்றத்தால் இயற்றப்பட்ட சட்டத்தின் மூலம் தீர்மானிக்கப்பட வேண்டும்.'",
        why_a_en="Option A is incorrect; it is Parliament by law, not Supreme Court rules.",
        why_a_ta="விருப்பம் A தவறானது; இது பாராளுமன்ற சட்டம், உச்ச நீதிமன்ற விதிகள் அல்ல.",
        why_b_en="Option B is incorrect; administrative notifications cannot replace Parliamentary legislation.",
        why_b_ta="விருப்பம் B தவறானது; நிர்வாக அறிவிப்புகள் பாராளுமன்ற சட்டத்திற்கு ஈடாகாது.",
        why_c_en="Option C is correct; Article 261(2) confers this power on Parliament by law.",
        why_c_ta="விருப்பம் C சரியானது; சரத்து 261(2) இந்த அதிகாரத்தை பாராளுமன்ற சட்டத்திற்கு வழங்குகிறது.",
        why_d_en="Option D is incorrect; High Courts have no rule-making authority under 261(2).",
        why_d_ta="விருப்பம் D தவறானது; உயர் நீதிமன்றங்களுக்கு இதில் அதிகாரம் இல்லை.",
        tip_en="Article 261(1) = Principle of Full Faith & Credit. Article 261(2) = Mode of proof provided by Parliament.",
        tip_ta="சரத்து 261(1) = முழு நம்பிக்கை மற்றும் மதிப்பு கொள்கை. சரத்து 261(2) = பாராளுமன்றத்தால் வழங்கப்படும் நிரூபிக்கும் முறை.",
        fact_en="The Indian Evidence Act, 1872 (now Bharatiya Sakshya Adhiniyam) contains the evidentiary rules for proving public acts and official documents.",
        fact_ta="இந்திய சாட்சியச் சட்டம் 1872 பொது ஆவணங்கள் மற்றும் சட்டங்களை நிரூபிப்பதற்கான விதிகளைக் கொண்டுள்ளது."
    ))

    # 030 - Key D (Medium)
    qs.append(make_q(
        num=30, diff="Medium", qtype="Concept MCQ", subtopic="Inter-State Water Disputes",
        en_stem="Section 11 of the Inter-State River Water Disputes Act, 1956 bars the jurisdiction of the Supreme Court in respect of water disputes. Under which constitutional provision does the Supreme Court nonetheless entertain appeals against river tribunal awards?",
        ta_stem="1956-ஆம் ஆண்டின் மாநிலங்களுக்கு இடையேயான நதிநீர் தகராறுகள் சட்டத்தின் பிரிவு 11 நதிநீர் தகராறுகளில் உச்ச நீதிமன்றத்தின் அதிகார வரம்பைத் தடுக்கிறது. ஆயினும் எந்த அரசியலமைப்பு விதியின் கீழ் உச்ச நீதிமன்றம் நதிநீர் தீர்ப்பாய தீர்ப்புகளுக்கு எதிரான மேல்முறையீடுகளை விசாரிக்கிறது?",
        en_a="Article 131 (Original Jurisdiction)", ta_a="சரத்து 131 (அசல் அதிகார வரம்பு)",
        en_b="Article 143 (Advisory Jurisdiction)", ta_b="சரத்து 143 (ஆலோசனை அதிகார வரம்பு)",
        en_c="Article 32 (Constitutional Remedies)", ta_c="சரத்து 32 (அரசியலமைப்பு பரிகாரங்கள்)",
        en_d="Article 136 (Special Leave to Appeal)", ta_d="சரத்து 136 (சிறப்பு விடுப்பு மேல்முறையீடு)",
        correct_key="D",
        exp_en="In several landmark decisions (including the Cauvery and Krishna cases), the Supreme Court affirmed that an ordinary parliamentary statute like Section 11 of the IRWD Act cannot override the extraordinary constitutional jurisdiction of the Supreme Court under Article 136 (Special Leave Petition).",
        exp_ta="பல முக்கிய தீர்ப்புகளில் (காவிரி மற்றும் கிருஷ்ணா வழக்குகள் உட்பட), ஐ.ஆர்.டபிள்யூ.டி சட்டத்தின் பிரிவு 11 போன்ற ஒரு சாதாரண பாராளுமன்ற சட்டம், சரத்து 136-ன் (சிறப்பு விடுப்பு மனு) கீழான உச்ச நீதிமன்றத்தின் அரசியலமைப்பு அதிகார வரம்பை நீக்க முடியாது என்று உச்ச நீதிமன்றம் உறுதிப்படுத்தியது.",
        why_a_en="Option A is incorrect; Article 131 suit is explicitly barred by Article 262(2) and Section 11.",
        why_a_ta="விருப்பம் A தவறானது; சரத்து 131 அசல் வழக்கு பிரிவு 11 மற்றும் சரத்து 262(2)-ஆல் தடை செய்யப்பட்டுள்ளது.",
        why_b_en="Option B is Presidential Reference, not an appeal filed by states.",
        why_b_ta="விருப்பம் B குடியரசுத் தலைவர் ஆலோசனை, மாநிலங்களின் மேல்முறையீடு அல்ல.",
        why_c_en="Option C is for enforcement of Fundamental Rights.",
        why_c_ta="விருப்பம் C அடிப்படை உரிமைகளை அமல்படுத்துவதற்கானது.",
        why_d_en="Option D is correct; Article 136 overrides statutory bars.",
        why_d_ta="விருப்பம் D சரியானது; சரத்து 136 சட்டப்பூர்வ தடைகளை மீறி அதிகாரம் அளிக்கிறது.",
        tip_en="Article 136 is a constitutional power that no ordinary Act of Parliament (like Section 11 IRWD Act) can take away.",
        tip_ta="சரத்து 136 என்பது எந்தவொரு சாதாரண பாராளுமன்ற சட்டத்தாலும் பறிக்க முடியாத அரசியலமைப்பு அதிகாரம் ஆகும்.",
        fact_en="The Supreme Court exercised its Article 136 jurisdiction to deliver the final binding judgment on the Cauvery Water dispute in February 2018.",
        fact_ta="உச்ச நீதிமன்றம் பிப்ரவரி 2018 இல் காவிரி நீர் தகராறில் இறுதித் தீர்ப்பை வழங்க தனது சரத்து 136 அதிகார வரம்பைப் பயன்படுத்தியது."
    ))

    # 031 - Key A (Hard)
    qs.append(make_q(
        num=31, diff="Hard", qtype="Concept MCQ", subtopic="Inter-State Water Disputes",
        en_stem="Which historic commission appointed by the Central Government in 1961 paved the way for constituting the Godavari and Krishna Water Disputes Tribunals?",
        ta_stem="1961 இல் மத்திய அரசால் நியமிக்கப்பட்ட எந்த வரலாற்றுச் சிறப்புமிக்க ஆணையம் கோதாவரி மற்றும் கிருஷ்ணா நதிநீர் தகராறு தீர்ப்பாயங்கள் அமைய வழிவகுத்தது?",
        en_a="N.D. Gulhati Commission", ta_a="என்.டி. குல்ஹாத்தி ஆணையம்",
        en_b="K.S. Radhakrishnan Commission", ta_b="கே.எஸ். ராதாகிருஷ்ணன் ஆணையம்",
        en_c="A.N. Khosla Committee", ta_c="ஏ.என். கோஸ்லா குழு",
        en_d="B.C. Roy Committee", ta_d="பி.சி. ராய் குழு",
        correct_key="A",
        exp_en="The Central Government appointed the Krishna-Godavari Commission under the chairmanship of Shri N.D. Gulhati in May 1961. Its report submitted in August 1962 documented water availability and ultimately led to the setting up of the KWDT-I and GWDT in April 1969.",
        exp_ta="மத்திய அரசு மே 1961 இல் ஸ்ரீ என்.டி. குல்ஹாத்தி தலைமையில் கிருஷ்ணா-கோதாவரி ஆணையத்தை நியமித்தது. ஆகஸ்ட் 1962 இல் சமர்ப்பிக்கப்பட்ட அதன் அறிக்கை ஏப்ரல் 1969 இல் KWDT-I மற்றும் GWDT அமைக்க வழிவகுத்தது.",
        why_a_en="Option A is correct; N.D. Gulhati Commission investigated the Krishna and Godavari river basins.",
        why_a_ta="விருப்பம் A சரியானது; என்.டி. குல்ஹாத்தி ஆணையம் கிருஷ்ணா மற்றும் கோதாவரி வடிநிலங்களை ஆய்வு செய்தது.",
        why_b_en="Option B is incorrect.",
        why_b_ta="விருப்பம் B தவறானது.",
        why_c_en="Option C is incorrect; Khosla Committee dealt with Narmada water dispute in 1964.",
        why_c_ta="விருப்பம் C தவறானது; கோஸ்லா குழு 1964 இல் நர்மதா நீர் தகராறைக் கையாண்டது.",
        why_d_en="Option D is incorrect.",
        why_d_ta="விருப்பம் D தவறானது.",
        tip_en="Gulhati Commission (1961) = Krishna and Godavari river basins. Khosla Committee (1964) = Narmada basin.",
        tip_ta="குல்ஹாத்தி ஆணையம் (1961) = கிருஷ்ணா மற்றும் கோதாவரி வடிநிலங்கள். கோஸ்லா குழு (1964) = நர்மதா வடிநிலம்.",
        fact_en="The Gulhati Commission concluded that comprehensive data on river flows and diversions was severely lacking across riparian states.",
        fact_ta="குல்ஹாத்தி ஆணையம் வடிநில மாநிலங்களிடையே நதி நீர் ஓட்டம் பற்றிய விரிவான புள்ளிவிவரங்கள் மிகவும் குறைவாக இருப்பதாகக் குறிப்பிட்டது."
    ))

    # 032 - Key B (Medium)
    qs.append(make_q(
        num=32, diff="Medium", qtype="Concept MCQ", subtopic="Inter-State Council",
        en_stem="Under Article 263(a) of the Constitution, what duty may be defined for the Inter-State Council by the President?",
        ta_stem="அரசியலமைப்பின் சரத்து 263(a)-ன் கீழ், குடியரசுத் தலைவரால் மாநிலங்களுக்கு இடையேயான கவுன்சிலுக்கு என்ன கடமை வரையறுக்கப்படலாம்?",
        en_a="Approving all interstate treaties entered into with foreign nations", ta_a="வெளிநாடுகளுடன் செய்துகொள்ளப்படும் அனைத்து மாநிலங்களுக்கு இடையேயான ஒப்பந்தங்களையும் அங்கீகரித்தல்",
        en_b="Inquiring into and advising upon disputes which may have arisen between States", ta_b="மாநிலங்களுக்கு இடையே ஏற்பட்டிருக்கக்கூடிய தகராறுகளை விசாரித்தல் மற்றும் அவை குறித்து ஆலோசனை வழங்குதல்",
        en_c="Directly dissolving state municipal bodies for financial mismanagement", ta_c="நிதி முறைகேடுகளுக்காக மாநில நகராட்சி அமைப்புகளை நேரடியாகக் கலைத்தல்",
        en_d="Impeaching Governors on grounds of constitutional delinquency", ta_d="அரசியலமைப்பு மீறல் அடிப்படையில் ஆளுநர்கள் மீது பதவி நீக்கத் தீர்மானம் கொண்டுவருதல்",
        correct_key="B",
        exp_en="Article 263(a) specifically empowers the Council with the duty of 'inquiring into and advising upon disputes which may have arisen between States.'",
        exp_ta="சரத்து 263(a) 'மாநிலங்களுக்கு இடையே ஏற்பட்டிருக்கக்கூடிய தகராறுகளை விசாரித்தல் மற்றும் அவை குறித்து ஆலோசனை வழங்குதல்' என்ற கடமையை கவுன்சிலுக்கு வழங்குகிறது.",
        why_a_en="Option A is incorrect; foreign treaties fall under Union Entry 14 List I.",
        why_a_ta="விருப்பம் A தவறானது; வெளிநாட்டு ஒப்பந்தங்கள் மத்தியப் பட்டியலில் உள்ளன.",
        why_b_en="Option B is the exact textual duty under Article 263(a).",
        why_b_ta="விருப்பம் B என்பது சரத்து 263(a)-ன் நேரடி வாசகமாகும்.",
        why_c_en="Option C is incorrect; municipal administration is purely a State subject.",
        why_c_ta="விருப்பம் C தவறானது; நகராட்சி என்பது மாநிலப் பட்டியல் துறை.",
        why_d_en="Option D is incorrect; Governors hold office during the pleasure of the President (Art 156).",
        why_d_ta="விருப்பம் D தவறானது; ஆளுநர்கள் குடியரசுத் தலைவரின் விருப்பத்தின் பேரில் பதவியில் நீடிக்கின்றனர்.",
        tip_en="Art 263(a) = Inquiring into disputes. Art 263(b) = Investigating common interest subjects. Art 263(c) = Policy recommendations.",
        tip_ta="சரத்து 263(a) = தகராறுகளை விசாரித்தல். சரத்து 263(b) = பொது நல விஷயங்களை ஆராய்தல். சரத்து 263(c) = கொள்கைப் பரிந்துரைகள்.",
        fact_en="While the Supreme Court exercises binding legal jurisdiction under Article 131, the Council performs an advisory conciliation role under Article 263(a).",
        fact_ta="உச்ச நீதிமன்றம் சரத்து 131-ன் கீழ் கட்டுப்படுத்தும் சட்ட அதிகார வரம்பைப் பயன்படுத்தும் போது, கவுன்சில் சரத்து 263(a)-ன் கீழ் ஆலோசனை நல்லிணக்கப் பணியைச் செய்கிறது."
    ))

    # 033 - Key C (Hard)
    qs.append(make_q(
        num=33, diff="Hard", qtype="Concept MCQ", subtopic="Inter-State Council",
        en_stem="How does the jurisdiction of the Inter-State Council under Article 263(a) differ fundamentally from the original jurisdiction of the Supreme Court under Article 131?",
        ta_stem="சரத்து 263(a)-ன் கீழான மாநிலங்களுக்கு இடையேயான கவுன்சிலின் அதிகார வரம்பு, சரத்து 131-ன் கீழான உச்ச நீதிமன்றத்தின் அசல் அதிகார வரம்பிலிருந்து எவ்வாறு அடிப்படையிலேயே வேறுபடுகிறது?",
        en_a="Article 131 is non-justiciable, whereas Article 263(a) is legally binding", ta_a="சரத்து 131 நீதிக்கு அப்பாற்பட்டது, ஆனால் சரத்து 263(a) சட்டப்பூர்வமாகக் கட்டுப்படுத்துகிறது",
        en_b="Article 263(a) can only hear water disputes, whereas Article 131 hears trade disputes", ta_b="சரத்து 263(a) நதிநீர் தகராறுகளை மட்டுமே விசாரிக்க முடியும், ஆனால் சரத்து 131 வர்த்தக தகராறுகளை விசாரிக்கிறது",
        en_c="The Supreme Court under Article 131 decides legal controversies by binding judgments, whereas the Council under Article 263(a) performs an advisory and political conciliation function", ta_c="உச்ச நீதிமன்றம் சரத்து 131-ன் கீழ் கட்டுப்படுத்தும் தீர்ப்புகள் மூலம் சட்ட மோதல்களைத் தீர்மானிக்கிறது, ஆனால் கவுன்சில் சரத்து 263(a)-ன் கீழ் ஓர் ஆலோசனை மற்றும் அரசியல் சமரசப் பணியைச் செய்கிறது",
        en_d="Article 131 is chaired by the Prime Minister, whereas Article 263 is chaired by the Chief Justice", ta_d="சரத்து 131-க்கு பிரதமர் தலைமை தாங்குகிறார், ஆனால் சரத்து 263-க்கு தலைமை நீதிபதி தலைமை தாங்குகிறார்",
        correct_key="C",
        exp_en="Under Article 131, the Supreme Court has exclusive original jurisdiction to decide legal disputes between the Centre and States or between States, producing binding judicial decrees. Under Article 263(a), the Council can inquire into political and extra-legal disputes and offer non-binding advisory recommendations.",
        exp_ta="சரத்து 131-ன் கீழ், உச்ச நீதிமன்றம் கட்டுப்படுத்தும் தீர்ப்புகளை வழங்கும் பிரத்யேக சட்ட அதிகார வரம்பைக் கொண்டுள்ளது. ஆனால் சரத்து 263(a)-ன் கீழ், கவுன்சில் அரசியல் மற்றும் சட்டம் சாராத தகராறுகளை விசாரித்து கட்டுப்படுத்தாத ஆலோசனைப் பரிந்துரைகளை மட்டுமே வழங்க முடியும்.",
        why_a_en="Option A is completely inverted.",
        why_a_ta="விருப்பம் A முற்றிலும் தலைகீழானது.",
        why_b_en="Option B is incorrect; water disputes are barred from Article 131 under Article 262.",
        why_b_ta="விருப்பம் B தவறானது; நதிநீர் தகராறுகள் சரத்து 131-லிருந்து விலக்கப்பட்டுள்ளன.",
        why_c_en="Option C correctly identifies the distinction between legal adjudication and advisory conciliation.",
        why_c_ta="விருப்பம் C சட்டத் தீர்ப்பு மற்றும் ஆலோசனை சமரசத்திற்கு இடையேயான வேறுபாட்டைச் சரியாகக் காட்டுகிறது.",
        why_d_en="Option D is absurd; courts are headed by CJI and Council by PM.",
        why_d_ta="விருப்பம் D தவறானது.",
        tip_en="Article 131 = Legal dispute + Supreme Court + Binding decree. Article 263(a) = Political/administrative dispute + Council + Advisory recommendation.",
        tip_ta="சரத்து 131 = சட்டத் தகராறு + உச்ச நீதிமன்றம் + கட்டுப்படுத்தும் தீர்ப்பு. சரத்து 263(a) = அரசியல்/நிர்வாகத் தகராறு + கவுன்சில் + ஆலோசனைப் பரிந்துரை.",
        fact_en="The Sarkaria Commission highlighted that Article 263 is uniquely suited for resolving disputes that involve political, administrative, and economic friction rather than pure legal questions.",
        fact_ta="சர்க்காரியா ஆணையம், வெறும் சட்டக் கேள்விகளுக்குப் பதிலாக அரசியல், நிர்வாக மற்றும் பொருளாதார உராய்வுகளைத் தீர்ப்பதற்கு சரத்து 263 மிகவும் பொருத்தமானது என்று சுட்டிக்காட்டியது."
    ))

    # 034 - Key D (Medium)
    qs.append(make_q(
        num=34, diff="Medium", qtype="Concept MCQ", subtopic="Zonal Councils and Reorganisation",
        en_stem="Who represents each State as members in the respective statutory Zonal Council under the States Reorganisation Act, 1956?",
        ta_stem="மாநில மறுசீரமைப்புச் சட்டம் 1956-ன் கீழ் அந்தந்த சட்டப்பூர்வ மண்டல கவுன்சிலில் உறுப்பினர்களாக ஒவ்வொரு மாநிலத்தையும் பிரதிநிதித்துவப்படுத்துபவர்கள் யார்?",
        en_a="The Governor and the Chief Secretary of the State", ta_a="மாநில ஆளுநர் மற்றும் தலைமைச் செயலாளர்",
        en_b="All elected Lok Sabha Members from that State", ta_b="அந்த மாநிலத்தைச் சேர்ந்த அனைத்து தேர்ந்தெடுக்கப்பட்ட மக்களவை உறுப்பினர்கள்",
        en_c="The Chief Minister only", ta_c="முதலமைச்சர் மட்டுமே",
        en_d="The Chief Minister and two other Ministers nominated by the Governor", ta_d="முதலமைச்சர் மற்றும் ஆளுநரால் பரிந்துரைக்கப்படும் இரண்டு அமைச்சர்கள்",
        correct_key="D",
        exp_en="Under Section 16(1)(b) of the States Reorganisation Act, 1956, each State is represented in the Zonal Council by its Chief Minister and two other Ministers nominated by the Governor.",
        exp_ta="மாநில மறுசீரமைப்புச் சட்டம் 1956 பிரிவு 16(1)(b)-ன் படி, ஒவ்வொரு மாநிலத்திலிருந்தும் அதன் முதலமைச்சர் மற்றும் ஆளுநரால் பரிந்துரைக்கப்படும் மற்ற இரண்டு அமைச்சர்கள் மண்டல கவுன்சிலில் உறுப்பினர்களாக இடம்பெறுவர்.",
        why_a_en="Option A is incorrect; Governor is not a member of the Zonal Council.",
        why_a_ta="விருப்பம் A தவறானது; ஆளுநர் இதில் உறுப்பினர் அல்ல.",
        why_b_en="Option B is incorrect; MPs are not ex-officio members.",
        why_b_ta="விருப்பம் B தவறானது; எம்பிக்கள் இதில் உறுப்பினர்கள் அல்ல.",
        why_c_en="Option C is incomplete; two other ministers also represent the state.",
        why_c_ta="விருப்பம் C முழுமையற்றது; மேலும் இரண்டு அமைச்சர்களும் பிரதிநிதித்துவப்படுத்துவர்.",
        why_d_en="Option D is the exact statutory composition under the 1956 Act.",
        why_d_ta="விருப்பம் D என்பது 1956 சட்டத்தின் கீழான சரியான சட்டப்பூர்வ கட்டமைப்பாகும்.",
        tip_en="Each State sends: Chief Minister + 2 Ministers nominated by the Governor.",
        tip_ta="ஒவ்வொரு மாநிலமும் அனுப்புவது: முதலமைச்சர் + ஆளுநரால் பரிந்துரைக்கப்படும் 2 அமைச்சர்கள்.",
        fact_en="In addition, the Chief Secretary of the State and the Development Commissioner act as advisors (without right to vote).",
        fact_ta="கூடுதலாக, மாநில தலைமைச் செயலாளர் மற்றும் வளர்ச்சி ஆணையர் ஆலோசகர்களாக (வாக்களிக்கும் உரிமையின்றி) செயல்படுகின்றனர்."
    ))

    # 035 - Key A (Hard)
    qs.append(make_q(
        num=35, diff="Hard", qtype="Concept MCQ", subtopic="Commissions and Inter-State Relations",
        en_stem="The Sarkaria Commission on Centre-State Relations recommended that the Inter-State Council set up under Article 263 should be designated as which of the following?",
        ta_stem="மத்திய-மாநில உறவுகள் குறித்த சர்க்காரியா ஆணையம், சரத்து 263-ன் கீழ் அமைக்கப்படும் மாநிலங்களுக்கு இடையேயான கவுன்சிலை பின்வருவனவற்றில் எவ்வாறு அழைக்க வேண்டும் என்று பரிந்துரைத்தது?",
        en_a="Inter-Governmental Council", ta_a="அரசுகளுக்கு இடையேயான கவுன்சில் (Inter-Governmental Council)",
        en_b="National Federal Council", ta_b="தேசிய கூட்டாட்சி கவுன்சில் (National Federal Council)",
        en_c="Union-States Consultative Board", ta_c="மத்திய-மாநில ஆலோசனை வாரியம் (Union-States Consultative Board)",
        en_d="Council of States and Union Territories", ta_d="மாநிலங்கள் மற்றும் யூனியன் பிரதேசங்களின் கவுன்சில்",
        correct_key="A",
        exp_en="The Sarkaria Commission specifically recommended that the Inter-State Council established under Article 263 should be named the 'Inter-Governmental Council' to distinguish it from other councils that may be set up under clauses (b) and (c) of Article 263.",
        exp_ta="சர்க்காரியா ஆணையம், சரத்து 263(b) மற்றும் (c)-ன் கீழ் அமைக்கப்படக்கூடிய பிற கவுன்சில்களிலிருந்து இதனை வேறுபடுத்துவதற்காக, சரத்து 263-ன் கீழ் அமைக்கப்படும் அமைப்பை 'அரசுகளுக்கு இடையேயான கவுன்சில்' (Inter-Governmental Council) என்று அழைக்க வேண்டும் என்று குறிப்பாகப் பரிந்துரைத்தது.",
        why_a_en="Option A is correct; Sarkaria Commission recommended the title 'Inter-Governmental Council'.",
        why_a_ta="விருப்பம் A சரியானது; சர்க்காரியா ஆணையம் 'அரசுகளுக்கு இடையேயான கவுன்சில்' என்ற பெயரை பரிந்துரைத்தது.",
        why_b_en="Option B is incorrect; this nomenclature was not proposed.",
        why_b_ta="விருப்பம் B தவறானது; இந்தப் பெயர் முன்மொழியப்படவில்லை.",
        why_c_en="Option C is incorrect.",
        why_c_ta="விருப்பம் C தவறானது.",
        why_d_en="Option D is incorrect; Council of States is the English translation of Rajya Sabha.",
        why_d_ta="விருப்பம் D தவறானது; இது மாநிலங்களவையின் ஆங்கிலப் பெயர்.",
        tip_en="Sarkaria Commission recommended name: 'Inter-Governmental Council'. But the 1990 order kept the name 'Inter-State Council'.",
        tip_ta="சர்க்காரியா ஆணையம் பரிந்துரைத்த பெயர்: 'அரசுகளுக்கு இடையேயான கவுன்சில்'. ஆனால் 1990 ஆணை 'மாநிலங்களுக்கு இடையேயான கவுன்சில்' என்ற பெயரையே வைத்தது.",
        fact_en="The Janata Dal government in 1990, however, retained the constitutional nomenclature 'Inter-State Council' in the Presidential Order.",
        fact_ta="எனினும் 1990 இல் ஜனதா தளம் அரசு குடியரசுத் தலைவர் ஆணையில் 'மாநிலங்களுக்கு இடையேயான கவுன்சில்' என்ற அரசியலமைப்புப் பெயரையே தக்க வைத்துக் கொண்டது."
    ))

    # 036 - Key B (Hard)
    qs.append(make_q(
        num=36, diff="Hard", qtype="Concept MCQ", subtopic="Commissions and Inter-State Relations",
        en_stem="The Justice M.M. Punchhi Commission on Centre-State Relations (2010) recommended which major institutional reform regarding the Secretariat of the Inter-State Council?",
        ta_stem="நீதிபதி எம்.எம். பூஞ்சி மத்திய-மாநில உறவுகள் ஆணையம் (2010) மாநிலங்களுக்கு இடையேயான கவுன்சில் செயலகம் தொடர்பாக எந்த முக்கிய நிறுவன சீர்திருத்தத்தைப் பரிந்துரைத்தது?",
        en_a="Abolishing the Secretariat and handing over duties to NITI Aayog", ta_a="செயலகத்தை ஒழித்துவிட்டு பணிகளை நிதி ஆயோக்கிடம் ஒப்படைத்தல்",
        en_b="Empowering the Inter-State Council Secretariat to function as the secretariat for all Zonal Councils and making it a truly independent federal body", ta_b="மாநிலங்களுக்கு இடையேயான கவுன்சில் செயலகத்தை அனைத்து மண்டல கவுன்சில்களுக்கும் செயலகமாகச் செயல்பட அதிகாரம் அளித்து, அதை உண்மையான சுதந்திரமான கூட்டாட்சி அமைப்பாக மாற்றுதல்",
        en_c="Placing the Secretariat directly under the administrative control of the Chief Justice of India", ta_c="செயலகத்தை நேரடியாக இந்திய தலைமை நீதிபதியின் நிர்வாகக் கட்டுப்பாட்டின் கீழ் வைத்தல்",
        en_d="Merging the Secretariat with the Election Commission of India", ta_d="செயலகத்தை இந்திய தேர்தல் ஆணையத்துடன் இணைத்தல்",
        correct_key="B",
        exp_en="The Punchhi Commission (2010) recommended strengthening the Inter-State Council by making its Secretariat independent and actively servicing all the Zonal Councils, thereby integrating regional and national federal consultation.",
        exp_ta="பூஞ்சி ஆணையம் (2010) மாநிலங்களுக்கு இடையேயான கவுன்சில் செயலகத்தை சுதந்திரமானதாக மாற்றி, அனைத்து மண்டல கவுன்சில்களுக்கும் சேவை செய்ய வைப்பதன் மூலம் பிராந்திய மற்றும் தேசிய கூட்டாட்சி ஆலோசனைகளை ஒருங்கிணைக்க பரிந்துரைத்தது.",
        why_a_en="Option A is incorrect; Punchhi Commission wanted to strengthen, not abolish, the ISC.",
        why_a_ta="விருப்பம் A தவறானது; பூஞ்சி ஆணையம் கவுன்சிலை வலுப்படுத்த விரும்பியது, ஒழிக்க அல்ல.",
        why_b_en="Option B is correct; Punchhi Commission recommended independent status and servicing Zonal Councils.",
        why_b_ta="விருப்பம் B சரியானது; சுதந்திர அந்தஸ்து மற்றும் மண்டல கவுன்சில்களுக்கு உதவும் நிலையை பரிந்துரைத்தது.",
        why_c_en="Option C is incorrect; judiciary has no role in executive council secretariats.",
        why_c_ta="விருப்பம் C தவறானது; நீதித்துறைக்கு இதில் தொடர்பு இல்லை.",
        why_d_en="Option D is incorrect.",
        why_d_ta="விருப்பம் D தவறானது.",
        tip_en="Punchhi Commission (2010) strongly advocated activating the Inter-State Council as an active federal forum.",
        tip_ta="பூஞ்சி ஆணையம் (2010) மாநிலங்களுக்கு இடையேயான கவுன்சிலை ஒரு தீவிர கூட்டாட்சி மன்றமாகச் செயல்படுத்த வலுவாக பரிந்துரைத்தது.",
        fact_en="The Punchhi Commission also recommended that the Inter-State Council should meet regularly, with a dedicated calendar of meetings fixed well in advance.",
        fact_ta="முன்கூட்டியே கூட்ட அட்டவணையை நிர்ணயித்து மாநிலங்களுக்கு இடையேயான கவுன்சில் தவறாமல் கூட வேண்டும் என்றும் பூஞ்சி ஆணையம் பரிந்துரைத்தது."
    ))

    # 037 - Key B (Medium)
    qs.append(make_q(
        num=37, diff="Medium", qtype="Concept MCQ", subtopic="Constitutional Framework",
        en_stem="Under Article 258(1) of the Constitution of India, the President may entrust executive functions of the Union to a State Government or its officers, subject to which condition?",
        ta_stem="இந்திய அரசியலமைப்பின் சரத்து 258(1)-ன் கீழ், குடியரசுத் தலைவர் மத்திய அரசின் நிர்வாகப் பணிகளை ஒரு மாநில அரசிடமோ அல்லது அதன் அதிகாரிகளிடமோ ஒப்படைக்கலாம்; ஆனால் அதற்குரிய நிபந்தனை என்ன?",
        en_a="Only with the prior approval of the Supreme Court of India", ta_a="இந்திய உச்ச நீதிமன்றத்தின் முன் அனுமதியுடன் மட்டுமே",
        en_b="Only with the consent of the Government of that State", ta_b="அந்த மாநில அரசின் ஒப்புதலுடன் மட்டுமே",
        en_c="Only after an emergency is proclaimed under Article 352", ta_c="சரத்து 352-ன் கீழ் அவசரநிலை பிரகடனம் செய்யப்பட்ட பின்னரே",
        en_d="Only if ratified by a two-thirds majority in the Rajya Sabha", ta_d="மாநிலங்களவையில் மூன்றில் இரண்டு பங்கு பெரும்பான்மையுடன் அங்கீகரிக்கப்பட்டால் மட்டுமே",
        correct_key="B",
        exp_en="Article 258(1) states: 'Notwithstanding anything in this Constitution, the President may, with the consent of the Government of a State, entrust either conditionally or unconditionally to that Government or to its officers functions in relation to any matter to which the executive power of the Union extends.'",
        exp_ta="சரத்து 258(1) கூறுகிறது: 'இந்த அரசியலமைப்பில் என்ன கூறப்பட்டிருந்தாலும், குடியரசுத் தலைவர் ஒரு மாநில அரசின் ஒப்புதலுடன், மத்திய அரசின் நிர்வாக அதிகாரம் நீட்டிக்கப்படும் எந்தவொரு விவகாரத்திலும் நிர்வாகப் பணிகளை நிபந்தனையுடனோ அல்லது நிபந்தனையின்றியோ அம்மாநில அரசிடமோ அல்லது அதன் அதிகாரிகளிடமோ ஒப்படைக்கலாம்.'",
        why_a_en="Option A is incorrect; Supreme Court approval is not needed.",
        why_a_ta="விருப்பம் A தவறானது; உச்ச நீதிமன்ற ஒப்புதல் தேவையில்லை.",
        why_b_en="Option B is correct; consent of the State Government is a constitutional prerequisite under 258(1).",
        why_b_ta="விருப்பம் B சரியானது; மாநில அரசின் ஒப்புதல் சரத்து 258(1)-ன் கீழ் கட்டாய நிபந்தனையாகும்.",
        why_c_en="Option C is incorrect; it applies in normal peacetime as well.",
        why_c_ta="விருப்பம் C தவறானது; இது சாதாரண அமைதிக் காலத்திலும் பொருந்தும்.",
        why_d_en="Option D is incorrect; Rajya Sabha ratification is not required.",
        why_d_ta="விருப்பம் D தவறானது; மாநிலங்களவை ஒப்புதல் தேவையில்லை.",
        tip_en="Article 258(1) = President entrusts Union functions with State consent. Article 258(2) = Parliament can entrust functions by law WITHOUT state consent.",
        tip_ta="சரத்து 258(1) = குடியரசுத் தலைவர் மாநில ஒப்புதலுடன் மத்திய பணிகளை ஒப்படைக்கிறார். சரத்து 258(2) = பாராளுமன்றம் சட்டம் மூலம் மாநில ஒப்புதல் இன்றியும் ஒப்படைக்கலாம்.",
        fact_en="Article 258(3) mandates that the Union Government shall pay to the State the extra cost of administration incurred in exercising those entrusted functions.",
        fact_ta="சரத்து 258(3)-ன் படி, அந்த ஒப்படைக்கப்பட்ட பணிகளைச் செய்வதற்காக மாநிலத்திற்கு ஏற்படும் கூடுதல் நிர்வாகச் செலவை மத்திய அரசே வழங்க வேண்டும்."
    ))

    # 038 - Key C (Hard)
    qs.append(make_q(
        num=38, diff="Hard", qtype="Concept MCQ", subtopic="Constitutional Framework",
        en_stem="Article 258A of the Constitution, which enables a State Governor to entrust State executive functions to the Union with the consent of the Government of India, was inserted by which Constitutional Amendment?",
        ta_stem="மத்திய அரசின் ஒப்புதலுடன் ஒரு மாநில ஆளுநர் மாநில நிர்வாகப் பணிகளை மத்திய அரசிடம் ஒப்படைக்க வகை செய்யும் அரசியலமைப்பின் சரத்து 258A எந்த அரசியலமைப்பு திருத்தத்தின் மூலம் சேர்க்கப்பட்டது?",
        en_a="1st Constitutional Amendment Act, 1951", ta_a="1-வது அரசியலமைப்பு திருத்தச் சட்டம், 1951",
        en_b="42nd Constitutional Amendment Act, 1976", ta_b="42-வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
        en_c="7th Constitutional Amendment Act, 1956", ta_c="7-வது அரசியலமைப்பு திருத்தச் சட்டம், 1956",
        en_d="44th Constitutional Amendment Act, 1978", ta_d="44-வது அரசியலமைப்பு திருத்தச் சட்டம், 1978",
        correct_key="C",
        exp_en="Article 258A was inserted by the 7th Constitutional Amendment Act, 1956 (following the States Reorganisation Act). While Article 258 allowed the Union to delegate functions to a State, there was no reciprocal provision allowing a State to delegate functions to the Union until Article 258A was introduced.",
        exp_ta="சரத்து 258A என்பது 7-வது அரசியலமைப்பு திருத்தச் சட்டம் 1956-ன் மூலம் சேர்க்கப்பட்டது. சரத்து 258 மத்திய அரசு மாநிலத்திற்கு அதிகாரங்களை வழங்க வழிசெய்த போதிலும், மாநில அரசு மத்திய அரசிடம் அதிகாரங்களை ஒப்படைக்க வழிவகை இல்லாததால் சரத்து 258A அறிமுகப்படுத்தப்பட்டது.",
        why_a_en="Option A is incorrect; 1st Amendment did not insert 258A.",
        why_a_ta="விருப்பம் A தவறானது; 1-வது திருத்தம் இதைச் சேர்க்கவில்லை.",
        why_b_en="Option B is incorrect; 42nd Amendment did not insert 258A.",
        why_b_ta="விருப்பம் B தவறானது; 42-வது திருத்தம் இதைச் சேர்க்கவில்லை.",
        why_c_en="Option C is correct; 7th Amendment Act, 1956 introduced Article 258A.",
        why_c_ta="விருப்பம் C சரியானது; 7-வது திருத்தச் சட்டம் 1956 சரத்து 258A-ஐ அறிமுகப்படுத்தியது.",
        why_d_en="Option D is incorrect.",
        why_d_ta="விருப்பம் D தவறானது.",
        tip_en="Article 258 = Union to State. Article 258A = State to Union (added by 7th Amendment, 1956).",
        tip_ta="சரத்து 258 = மத்தியிலிருந்து மாநிலத்திற்கு. சரத்து 258A = மாநிலத்திலிருந்து மத்தியிற்கு (7-வது திருத்தம், 1956 மூலம் சேர்க்கப்பட்டது).",
        fact_en="Article 258A is commonly utilized when a State Government entrusts the construction of major inter-state irrigation or infrastructure projects to central agencies like the CPWD.",
        fact_ta="ஒரு மாநில அரசு பெரிய நீர்ப்பாசன அல்லது கட்டமைப்புத் திட்டங்களை CPWD போன்ற மத்திய நிறுவனங்களிடம் ஒப்படைக்க சரத்து 258A பொதுவாகப் பயன்படுத்தப்படுகிறது."
    ))

    # 039 - Key D (Hard)
    qs.append(make_q(
        num=39, diff="Hard", qtype="Concept MCQ", subtopic="Inter-State Trade and Commerce",
        en_stem="In the landmark case Automobile Transport (Rajasthan) Ltd. v. State of Rajasthan (1962), a 7-judge bench of the Supreme Court introduced which major constitutional doctrine concerning Article 301?",
        ta_stem="வரலாற்றுச் சிறப்புமிக்க ஆட்டோமொபைல் டிரான்ஸ்போர்ட் (ராஜஸ்தான்) லிமிடெட் எதிர் ராஜஸ்தான் மாநிலம் (1962) வழக்கில், உச்ச நீதிமன்றத்தின் 7 நீதிபதிகள் கொண்ட அமர்வு சரத்து 301 தொடர்பாக எந்த முக்கிய அரசியலமைப்புக் கோட்பாட்டை அறிமுகப்படுத்தியது?",
        en_a="Doctrine of Pith and Substance", ta_a="அடிப்படைக் கோட்பாடு (Doctrine of Pith and Substance)",
        en_b="Doctrine of Severability", ta_b="பிரித்தெடுக்கும் கோட்பாடு (Doctrine of Severability)",
        en_c="Doctrine of Eclipse", ta_c="மறைவுக் கோட்பாடு (Doctrine of Eclipse)",
        en_d="Doctrine of Compensatory Taxes", ta_d="ஈட்டு வரிக் கோட்பாடு (Doctrine of Compensatory Taxes)",
        correct_key="D",
        exp_en="In Automobile Transport (1962), the 7-judge Constitution Bench held by a 4:3 majority that regulatory measures and 'compensatory taxes' levied for the provision of specific facilities (like roads, bridges, and infrastructure) do not impede freedom of trade and therefore do not violate Article 301.",
        exp_ta="ஆட்டோமொபைல் டிரான்ஸ்போர்ட் (1962) வழக்கில் 7 நீதிபதிகள் அரசியலமைப்பு அமர்வு, சாலைகள் மற்றும் பாலங்கள் போன்ற வசதிகளை வழங்குவதற்காக விதிக்கப்படும் 'ஈட்டு வரிகள்' (Compensatory Taxes) வர்த்தக சுதந்திரத்தைத் தடுக்காது, எனவே சரத்து 301-ஐ மீறாது என்று தீர்ப்பளித்தது.",
        why_a_en="Option A applies to legislative competence under Seventh Schedule entries.",
        why_a_ta="விருப்பம் A ஏழாவது அட்டவணை சட்டமன்றத் திறனுக்குப் பொருந்தும்.",
        why_b_en="Option B applies to Article 13 unconstitutional clauses.",
        why_b_ta="விருப்பம் B சரத்து 13 அரசியலமைப்பிற்கு முரணான விதிகளுக்குப் பொருந்தும்.",
        why_c_en="Option C applies to pre-constitutional laws under Article 13(1).",
        why_c_ta="விருப்பம் C சரத்து 13(1)-ன் கீழான அரசியலமைப்புக்கு முந்தைய சட்டங்களுக்குப் பொருந்தும்.",
        why_d_en="Option D is correct; the Compensatory Tax doctrine was created in this case.",
        why_d_ta="விருப்பம் D சரியானது; ஈட்டு வரிக் கோட்பாடு இவ்வழக்கில் உருவாக்கப்பட்டது.",
        tip_en="Automobile Transport (1962) = Compensatory tax does not violate Article 301. (Later overruled in Jindal Stainless, 2017).",
        tip_ta="ஆட்டோமொபைல் டிரான்ஸ்போர்ட் (1962) = ஈட்டு வரி சரத்து 301-ஐ மீறாது (பின்னர் 2017 ஜிண்டால் ஸ்டெயின்லெஸ் வழக்கில் ரத்து செய்யப்பட்டது).",
        fact_en="This compensatory tax doctrine held the field for over 50 years until it was officially discarded by the 9-judge bench in Jindal Stainless (2017).",
        fact_ta="இந்த ஈட்டு வரிக் கோட்பாடு 50 ஆண்டுகளுக்கும் மேலாக நீடித்தது, பின்னர் 2017 இல் ஜிண்டால் ஸ்டெயின்லெஸ் வழக்கில் 9 நீதிபதிகள் அமர்வால் கைவிடப்பட்டது."
    ))

    # 040 - Key A (Medium)
    qs.append(make_q(
        num=40, diff="Medium", qtype="Concept MCQ", subtopic="Zonal Councils and Reorganisation",
        en_stem="Which of the following groups of States and Union Territories constitutes the Western Zonal Council?",
        ta_stem="பின்வரும் எந்த மாநிலங்கள் மற்றும் யூனியன் பிரதேசங்களின் குழு மேற்கு மண்டல கவுன்சிலை உருவாக்குகிறது?",
        en_a="Goa, Gujarat, Maharashtra, and Union Territories of Dadra and Nagar Haveli and Daman and Diu", ta_a="கோவா, குஜராத், மகாராஷ்டிரா மற்றும் தாத்ரா & நாகர் ஹவேலி மற்றும் டாமன் & டையூ யூனியன் பிரதேசங்கள்",
        en_b="Rajasthan, Gujarat, Punjab, and Haryana", ta_b="ராஜஸ்தான், குஜராத், பஞ்சாப் மற்றும் ஹரியானா",
        en_c="Madhya Pradesh, Maharashtra, Chhattisgarh, and Goa", ta_c="மத்தியப் பிரதேசம், மகாராஷ்டிரா, சத்தீஸ்கர் மற்றும் கோவா",
        en_d="Karnataka, Kerala, Goa, and Maharashtra", ta_d="கர்நாடகா, கேரளா, கோவா மற்றும் மகாராஷ்டிரா",
        correct_key="A",
        exp_en="The Western Zonal Council comprises the States of Goa, Gujarat, and Maharashtra, along with the Union Territory of Dadra and Nagar Haveli and Daman and Diu. The headquarters is located in Mumbai.",
        exp_ta="மேற்கு மண்டல கவுன்சிலில் கோவா, குஜராத், மகாராஷ்டிரா ஆகிய மாநிலங்களும், தாத்ரா & நாகர் ஹவேலி மற்றும் டாமன் & டையூ யூனியன் பிரதேசமும் உள்ளன. இதன் தலைமையகம் மும்பையில் அமைந்துள்ளது.",
        why_a_en="Option A is the exact composition of the Western Zonal Council.",
        why_a_ta="விருப்பம் A என்பது மேற்கு மண்டல கவுன்சிலின் சரியான கட்டமைப்பு ஆகும்.",
        why_b_en="Option B mixes Northern Zone states (Rajasthan, Punjab, Haryana) with Gujarat.",
        why_b_ta="விருப்பம் B வடக்கு மண்டல மாநிலங்களை குஜராத்துடன் கலக்கிறது.",
        why_c_en="Option C mixes Central Zone states (MP, Chhattisgarh) with Western Zone.",
        why_c_ta="விருப்பம் C மத்திய மண்டல மாநிலங்களை மேற்கு மண்டலத்துடன் கலக்கிறது.",
        why_d_en="Option D mixes Southern Zone states (Karnataka, Kerala) with Western Zone.",
        why_d_ta="விருப்பம் D தெற்கு மண்டல மாநிலங்களை மேற்கு மண்டலத்துடன் கலக்கிறது.",
        tip_en="Western Zonal Council HQ: Mumbai. Members: Maharashtra, Gujarat, Goa + DNH & DD.",
        tip_ta="மேற்கு மண்டல கவுன்சில் தலைமையகம்: மும்பை. உறுப்பினர்கள்: மகாராஷ்டிரா, குஜராத், கோவா + DNH & DD.",
        fact_en="Goa was originally a Union Territory when admitted to the Western Zonal Council, and remained in the same Council upon attaining full statehood in 1987.",
        fact_ta="கோவா முதலில் யூனியன் பிரதேசமாக இருந்தபோது மேற்கு மண்டல கவுன்சிலில் சேர்க்கப்பட்டது, 1987 இல் முழு மாநிலமான பிறகும் அதே கவுன்சிலில் நீடிக்கிறது."
    ))

    # 041 - Key B (Medium)
    qs.append(make_q(
        num=41, diff="Medium", qtype="Concept MCQ", subtopic="Zonal Councils and Reorganisation",
        en_stem="Under the States Reorganisation Act of 1956, which premier metropolitan city was designated to host the permanent secretariat and headquarters of the Eastern Zonal Council?",
        ta_stem="1956-ஆம் ஆண்டின் மாநில மறுசீரமைப்புச் சட்டத்தின் கீழ், கிழக்கு மண்டல கவுன்சிலின் நிரந்தர செயலகம் மற்றும் தலைமையகத்தை அமைக்க தேர்ந்தெடுக்கப்பட்ட முக்கிய பெருநகரம் எது?",
        en_a="Bhubaneswar", ta_a="புவனேஸ்வர்",
        en_b="Kolkata", ta_b="கொல்கத்தா",
        en_c="Patna", ta_c="பாட்னா",
        en_d="Ranchi", ta_d="ராஞ்சி",
        correct_key="B",
        exp_en="The headquarters of the Eastern Zonal Council is located in Kolkata. Its members include Bihar, Jharkhand, Odisha, and West Bengal.",
        exp_ta="கிழக்கு மண்டல கவுன்சிலின் தலைமையகம் கொல்கத்தாவில் அமைந்துள்ளது. இதில் பீகார், ஜார்க்கண்ட், ஒடிசா மற்றும் மேற்கு வங்கம் ஆகிய மாநிலங்கள் உறுப்பினர்களாக உள்ளன.",
        why_a_en="Option A is Bhubaneswar, capital of Odisha, not the zonal HQ.",
        why_a_ta="விருப்பம் A புவனேஸ்வர் ஒடிசாவின் தலைநகரம், மண்டல தலைமையகம் அல்ல.",
        why_b_en="Option B is correct; Kolkata is the HQ of the Eastern Zonal Council.",
        why_b_ta="விருப்பம் B சரியானது; கொல்கத்தா கிழக்கு மண்டல கவுன்சிலின் தலைமையகமாகும்.",
        why_c_en="Option C is Patna, capital of Bihar.",
        why_c_ta="விருப்பம் C பாட்னா பீகாரின் தலைநகரம்.",
        why_d_en="Option D is Ranchi, capital of Jharkhand.",
        why_d_ta="விருப்பம் D ராஞ்சி ஜார்க்கண்டின் தலைநகரம்.",
        tip_en="Zonal HQs: Northern = New Delhi; Central = Prayagraj (Allahabad); Eastern = Kolkata; Western = Mumbai; Southern = Chennai.",
        tip_ta="மண்டல தலைமையகங்கள்: வடக்கு = புது தில்லி; மத்திய = பிரயாக்ராஜ்; கிழக்கு = கொல்கத்தா; மேற்கு = மும்பை; தெற்கு = சென்னை.",
        fact_en="Sikkim was originally in the Eastern Zonal Council before being integrated into the North Eastern Council in 2002.",
        fact_ta="2002 இல் வடகிழக்கு கவுன்சிலில் இணைக்கப்படுவதற்கு முன்பு சிக்கிம் கிழக்கு மண்டல கவுன்சிலில் இருந்தது."
    ))

    # 042 - Key C (Medium)
    qs.append(make_q(
        num=42, diff="Medium", qtype="Concept MCQ", subtopic="Zonal Councils and Reorganisation",
        en_stem="Which of the following combinations of states forms the Central Zonal Council?",
        ta_stem="பின்வரும் எந்த மாநிலங்களின் சேர்க்கை மத்திய மண்டல கவுன்சிலை உருவாக்குகிறது?",
        en_a="Rajasthan, Madhya Pradesh, Gujarat, and Maharashtra", ta_a="ராஜஸ்தான், மத்தியப் பிரதேசம், குஜராத் மற்றும் மகாராஷ்டிரா",
        en_b="Bihar, Jharkhand, Odisha, and West Bengal", ta_b="பீகார், ஜார்க்கண்ட், ஒடிசா மற்றும் மேற்கு வங்கம்",
        en_c="Chhattisgarh, Madhya Pradesh, Uttarakhand, and Uttar Pradesh", ta_c="சத்தீஸ்கர், மத்தியப் பிரதேசம், உத்தராகண்ட் மற்றும் உத்தரப் பிரதேசம்",
        en_d="Haryana, Punjab, Himachal Pradesh, and Uttar Pradesh", ta_d="ஹரியானா, பஞ்சாப், இமாச்சலப் பிரதேசம் மற்றும் உத்தரப் பிரதேசம்",
        correct_key="C",
        exp_en="The Central Zonal Council consists of Chhattisgarh, Madhya Pradesh, Uttarakhand, and Uttar Pradesh. Its headquarters is located in Prayagraj (Allahabad).",
        exp_ta="மத்திய மண்டல கவுன்சிலில் சத்தீஸ்கர், மத்தியப் பிரதேசம், உத்தராகண்ட் மற்றும் உத்தரப் பிரதேசம் ஆகிய மாநிலங்கள் உள்ளன. இதன் தலைமையகம் பிரயாக்ராஜில் (அலகாபாத்) அமைந்துள்ளது.",
        why_a_en="Option A mixes states across Northern, Central, and Western zones.",
        why_a_ta="விருப்பம் A பல்வேறு மண்டல மாநிலங்களைக் கலக்கிறது.",
        why_b_en="Option B is the Eastern Zonal Council.",
        why_b_ta="விருப்பம் B கிழக்கு மண்டல கவுன்சில் ஆகும்.",
        why_c_en="Option C is correct; Chhattisgarh, MP, Uttarakhand, and UP form the Central Zone.",
        why_c_ta="விருப்பம் C சரியானது; சத்தீஸ்கர், ம.பி, உத்தராகண்ட் மற்றும் உ.பி ஆகியவை மத்திய மண்டலத்தை உருவாக்குகின்றன.",
        why_d_en="Option D mixes Northern Zone states with UP.",
        why_d_ta="விருப்பம் D வடக்கு மண்டல மாநிலங்களை உ.பி-யுடன் கலக்கிறது.",
        tip_en="Central Zone = 4 States: UP, MP, Uttarakhand, Chhattisgarh. HQ: Prayagraj.",
        tip_ta="மத்திய மண்டலம் = 4 மாநிலங்கள்: உ.பி, ம.பி, உத்தராகண்ட், சத்தீஸ்கர். தலைமையகம்: பிரயாக்ராஜ்.",
        fact_en="Originally in 1956, the Central Zone comprised only UP and MP; Uttarakhand and Chhattisgarh joined upon their creation in 2000.",
        fact_ta="1956 இல் அசல் மத்திய மண்டலத்தில் உ.பி மற்றும் ம.பி மட்டுமே இருந்தன; 2000 இல் உருவான பிறகு உத்தராகண்ட் மற்றும் சத்தீஸ்கர் இணைந்தன."
    ))

    # 043 - Key D (Hard)
    qs.append(make_q(
        num=43, diff="Hard", qtype="Concept MCQ", subtopic="Zonal Councils and Reorganisation",
        en_stem="Following the Jammu and Kashmir Reorganisation Act, 2019, which of the following represents the updated membership of the Northern Zonal Council?",
        ta_stem="ஜம்மு-காஷ்மீர் மறுசீரமைப்புச் சட்டம் 2019-ஐத் தொடர்ந்து, பின்வருவனவற்றில் எது வடக்கு மண்டல கவுன்சிலின் புதுப்பிக்கப்பட்ட உறுப்பினர் அமைப்பைக் குறிக்கிறது?",
        en_a="Haryana, Punjab, Himachal Pradesh, Rajasthan only", ta_a="ஹரியானா, பஞ்சாப், இமாச்சலப் பிரதேசம், ராஜஸ்தான் மட்டுமே",
        en_b="States of Haryana, Punjab, Himachal Pradesh and UT of Chandigarh only", ta_b="ஹரியானா, பஞ்சாப், இமாச்சலப் பிரதேசம் மற்றும் சண்டிகர் யூனியன் பிரதேசம் மட்டுமே",
        en_c="States of Punjab, Haryana, Rajasthan, Uttar Pradesh, and Delhi", ta_c="பஞ்சாப், ஹரியானா, ராஜஸ்தான், உத்தரப் பிரதேசம் மற்றும் தில்லி",
        en_d="States of Haryana, Himachal Pradesh, Punjab, Rajasthan, and UTs of Chandigarh, Delhi, Jammu & Kashmir, and Ladakh", ta_d="ஹரியானா, இமாச்சலப் பிரதேசம், பஞ்சாப், ராஜஸ்தான் மாநிலங்கள் மற்றும் சண்டிகர், தில்லி, ஜம்மு & காஷ்மீர், லடாக் யூனியன் பிரதேசங்கள்",
        correct_key="D",
        exp_en="The Northern Zonal Council comprises 4 States (Haryana, Himachal Pradesh, Punjab, Rajasthan) and 4 Union Territories (Chandigarh, National Capital Territory of Delhi, Jammu & Kashmir, and Ladakh). Its headquarters is in New Delhi.",
        exp_ta="வடக்கு மண்டல கவுன்சிலில் 4 மாநிலங்கள் (ஹரியானா, இமாச்சலப் பிரதேசம், பஞ்சாப், ராஜஸ்தான்) மற்றும் 4 யூனியன் பிரதேசங்கள் (சண்டிகர், தில்லி தேசிய தலைநகர் பகுதி, ஜம்மு & காஷ்மீர், மற்றும் லடாக்) உள்ளன. இதன் தலைமையகம் புது தில்லியில் உள்ளது.",
        why_a_en="Option A omits all the Union Territories.",
        why_a_ta="விருப்பம் A அனைத்து யூனியன் பிரதேசங்களையும் விட்டுவிடுகிறது.",
        why_b_en="Option B omits Rajasthan, Delhi, J&K, and Ladakh.",
        why_b_ta="விருப்பம் B ராஜஸ்தான், தில்லி, ஜம்மு-காஷ்மீர் மற்றும் லடாக்கை விட்டுவிடுகிறது.",
        why_c_en="Option C incorrectly includes Uttar Pradesh (which is in Central Zone).",
        why_c_ta="விருப்பம் C உ.பி-யை தவறாகச் சேர்க்கிறது (உ.பி மத்திய மண்டலத்தில் உள்ளது).",
        why_d_en="Option D is the complete and accurate updated composition.",
        why_d_ta="விருப்பம் D என்பது முழுமையான மற்றும் புதுப்பிக்கப்பட்ட சரியான அமைப்பாகும்.",
        tip_en="Northern Zonal Council has the largest number of UTs (Chandigarh, Delhi, J&K, Ladakh).",
        tip_ta="வடக்கு மண்டல கவுன்சிலில்தான் அதிக எண்ணிக்கையிலான யூனியன் பிரதேசங்கள் உள்ளன (சண்டிகர், தில்லி, ஜம்மு-காஷ்மீர், லடாக்).",
        fact_en="Prior to October 31, 2019, Jammu and Kashmir was represented as a full State in the Northern Zonal Council.",
        fact_ta="அக்டோபர் 31, 2019-க்கு முன்பு ஜம்மு-காஷ்மீர் வடக்கு மண்டல கவுன்சிலில் ஒரு முழு மாநிலமாகப் பிரதிநிதித்துவப்படுத்தப்பட்டது."
    ))

    # 044 - Key A (Hard)
    qs.append(make_q(
        num=44, diff="Hard", qtype="Concept MCQ", subtopic="Inter-State Water Disputes",
        en_stem="In In re Special Reference No. 1 of 1991 (Cauvery Water Disputes Tribunal Reference), what did the Constitution Bench of the Supreme Court rule regarding the Karnataka Cauvery Basin Irrigation Protection Ordinance, 1991?",
        ta_stem="சிறப்பு குறிப்பு எண் 1 (1991) காவிரி நதிநீர் தகராறு தீர்ப்பாய ஆலோசனையில், கர்நாடக காவிரி வடிநில பாசனப் பாதுகாப்பு அவசரச் சட்டம் 1991 குறித்து உச்ச நீதிமன்ற அரசியலமைப்பு அமர்வு என்ன தீர்ப்பளித்தது?",
        en_a="The State Ordinance was unconstitutional as no state can pass a law nullifying the order of an inter-state tribunal constituted by Parliament", ta_a="மாநில அவசரச் சட்டம் அரசியலமைப்பிற்கு முரணானது; ஏனெனில் பாராளுமன்றத்தால் அமைக்கப்பட்ட ஒரு மாநிலங்களுக்கு இடையேயான தீர்ப்பாயத்தின் உத்தரவை ரத்து செய்ய எந்த மாநிலமும் சட்டம் இயற்ற முடியாது",
        en_b="The State Ordinance was valid under Entry 17 of the State List", ta_b="மாநிலப் பட்டியல் பதிவு 17-ன் கீழ் மாநில அவசரச் சட்டம் செல்லுபடியாகும்",
        en_c="The Tribunal's interim award was ultra vires because interim orders are never permitted", ta_c="இடைக்கால உத்தரவுகள் அனுமதிக்கப்படாததால் தீர்ப்பாயத்தின் இடைக்கால உத்தரவு அதிகார வரம்பிற்கு அப்பாற்பட்டது",
        en_d="The President was legally bound to dismiss the Karnataka government under Article 356", ta_d="சரத்து 356-ன் கீழ் கர்நாடக அரசைக் கலைக்க குடியரசுத் தலைவர் சட்டப்பூர்வமாகக் கடமைப்பட்டவர்",
        correct_key="A",
        exp_en="In the 1991 Cauvery Reference, the Supreme Court held that the Karnataka Ordinance nullifying the CWDT's interim order was unconstitutional and beyond state legislative power. An inter-state water tribunal's decision cannot be overridden by a state legislature.",
        exp_ta="1991 காவிரி குறிப்பு வழக்கில், CWDT-யின் இடைக்கால உத்தரவை ரத்து செய்யும் கர்நாடக அரசின் அவசரச் சட்டம் அரசியலமைப்பிற்கு முரணானது மற்றும் மாநில சட்டமன்ற அதிகாரத்திற்கு அப்பாற்பட்டது என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது. தீர்ப்பாயத்தின் உத்தரவை மாநில சட்டமன்றத்தால் ரத்து செய்ய முடியாது.",
        why_a_en="Option A is correct; the Supreme Court held the ordinance ultra vires the Constitution.",
        why_a_ta="விருப்பம் A சரியானது; அவசரச் சட்டம் அரசியலமைப்பிற்கு முரணானது என உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
        why_b_en="Option B is incorrect; Entry 17 List II is subject to Entry 56 List I.",
        why_b_ta="விருப்பம் B தவறானது; மாநிலப் பட்டியல் பதிவு 17 மத்தியப் பட்டியல் பதிவு 56-க்கு உட்பட்டது.",
        why_c_en="Option C is incorrect; the Supreme Court affirmed that CWDT had the power to grant interim relief.",
        why_c_ta="விருப்பம் C தவறானது; CWDT-க்கு இடைக்கால நிவாரணம் வழங்க அதிகாரம் உண்டு என நீதிமன்றம் உறுதிப்படுத்தியது.",
        why_d_en="Option D is incorrect; Article 143 reference does not issue directions to impose Article 356.",
        why_d_ta="விருப்பம் D தவறானது; சரத்து 143 ஆலோசனை வழக்கில் சரத்து 356 பிறப்பிக்க உத்தரவிடப்படாது.",
        tip_en="In re Special Reference 1 of 1991: CWDT had power to grant interim relief; State cannot override tribunal order by ordinance.",
        tip_ta="1991 சிறப்பு குறிப்பு வழக்கு: CWDT-க்கு இடைக்கால உத்தரவு பிறப்பிக்க அதிகாரம் உண்டு; மாநில அரசு அவசரச் சட்டம் மூலம் அதை ரத்து செய்ய முடியாது.",
        fact_en="This landmark advisory opinion firmly established the supremacy of central river dispute tribunals over conflicting state laws.",
        fact_ta="இந்த வரலாற்றுச் சிறப்புமிக்க ஆலோசனைத் தீர்ப்பு முரண்பட்ட மாநிலச் சட்டங்களை விட மத்திய நதிநீர் தகராறு தீர்ப்பாயங்களின் மேலாதிக்கத்தை உறுதியாக நிறுவியது."
    ))

    # 045 - Key D (Hard)
    qs.append(make_q(
        num=45, diff="Hard", qtype="Concept MCQ", subtopic="Inter-State Water Disputes",
        en_stem="On what statistical dependability standard did the First Krishna Water Disputes Tribunal (Bachawat Tribunal, 1976) allocate the yield of the river Krishna?",
        ta_stem="முதல் கிருஷ்ணா நதிநீர் தகராறு தீர்ப்பாயம் (பசாவத் தீர்ப்பாயம், 1976) எந்த புள்ளிவிவர நம்பகத்தன்மை தரநிலையின் அடிப்படையில் கிருஷ்ணா நதியின் நீர்ப்பகிர்வை ஒதுக்கீடு செய்தது?",
        en_a="50% dependability (Average flow)", ta_a="50% நம்பகத்தன்மை (சராசரி ஓட்டம்)",
        en_b="90% dependability (Drought year flow)", ta_b="90% நம்பகத்தன்மை (வறட்சி ஆண்டு ஓட்டம்)",
        en_c="100% dependability (Minimum recorded flow)", ta_c="100% நம்பகத்தன்மை (குறைந்தபட்ச பதிவு செய்யப்பட்ட ஓட்டம்)",
        en_d="75% dependability (Flow available in 75 out of 100 years)", ta_d="75% நம்பகத்தன்மை (100 ஆண்டுகளில் 75 ஆண்டுகளில் கிடைக்கும் ஓட்டம்)",
        correct_key="D",
        exp_en="The Bachawat Tribunal (KWDT-I) adopted the standard of 75% dependability, assessing the available water in the Krishna basin at 2060 TMC, and divided it among Maharashtra, Karnataka, and Andhra Pradesh.",
        exp_ta="பசாவத் தீர்ப்பாயம் (KWDT-I) 75% நம்பகத்தன்மை தரநிலையை ஏற்றுக்கொண்டு, கிருஷ்ணா வடிநிலத்தில் கிடைக்கும் தண்ணீரை 2060 டி.எம்.சி என மதிப்பிட்டு, அதை மகாராஷ்டிரா, கர்நாடகா மற்றும் ஆந்திரா இடையே பகிர்ந்தளித்தது.",
        why_a_en="Option A is average flow, which KWDT-II later considered for surplus water sharing.",
        why_a_ta="விருப்பம் A சராசரி ஓட்டம், இதை KWDT-II பின்னர் உபரி நீருக்காக பரிசீலித்தது.",
        why_b_en="Option B is 90% dependability, rarely used as base allocation.",
        why_b_ta="விருப்பம் B 90% நம்பகத்தன்மை, அடிப்படை ஒதுக்கீட்டிற்குப் பயன்படுத்தப்படுவதில்லை.",
        why_c_en="Option C is incorrect.",
        why_c_ta="விருப்பம் C தவறானது.",
        why_d_en="Option D is correct; 75% dependability was the fundamental baseline of the Bachawat award.",
        why_d_ta="விருப்பம் D சரியானது; 75% நம்பகத்தன்மை என்பது பசாவத் தீர்ப்பின் அடிப்படைக் கொள்கையாகும்.",
        tip_en="KWDT-I (Bachawat) = 75% dependability (2060 TMC). KWDT-II (Brijesh Kumar) = 65% dependability.",
        tip_ta="KWDT-I (பசாவத்) = 75% நம்பகத்தன்மை (2060 டி.எம்.சி). KWDT-II (பிரிஜேஷ் குமார்) = 65% நம்பகத்தன்மை.",
        fact_en="The Bachawat Award was accepted by all riparian states and operated smoothly until its 25-year review period expired in May 2000.",
        fact_ta="பசாவத் தீர்ப்பு அனைத்து வடிநில மாநிலங்களாலும் ஏற்றுக்கொள்ளப்பட்டு, மே 2000 இல் அதன் 25 ஆண்டு மறுஆய்வுக்காலம் முடியும் வரை சுமுகமாகச் செயல்பட்டது."
    ))

    # 046 - Key C (Medium)
    qs.append(make_q(
        num=46, diff="Medium", qtype="Concept MCQ", subtopic="Commissions and Inter-State Relations",
        en_stem="The Second Administrative Reforms Commission (headed by Veerappa Moily) dealt with Inter-State Conflict Resolution in which of its major reports?",
        ta_stem="இரண்டாவது நிர்வாக சீர்திருத்த ஆணையம் (வீரப்ப மொய்லி தலைமை) மாநிலங்களுக்கு இடையேயான மோதல் தீர்வு பற்றி தனது எந்த முக்கிய அறிக்கையில் கையாண்டது?",
        en_a="1st Report: Right to Information", ta_a="1-வது அறிக்கை: தகவல் அறியும் உரிமை",
        en_b="4th Report: Ethics in Governance", ta_b="4-வது அறிக்கை: ஆளுகையில் நெறிமுறைகள்",
        en_c="7th Report: Capacity Building for Peace and Conflict Resolution", ta_c="7-வது அறிக்கை: அமைதி மற்றும் மோதல் தீர்வுக்கான திறன் மேம்பாடு",
        en_d="12th Report: Citizen Centric Administration", ta_d="12-வது அறிக்கை: மக்களை மையமாகக் கொண்ட நிர்வாகம்",
        correct_key="C",
        exp_en="The Second ARC presented its 7th Report titled 'Capacity Building for Peace and Conflict Resolution' (February 2008), which extensively analysed inter-state river water conflicts and regional boundary disputes.",
        exp_ta="இரண்டாவது நிர்வாக சீர்திருத்த ஆணையம் தனது 7-வது அறிக்கையான 'அமைதி மற்றும் மோதல் தீர்வுக்கான திறன் மேம்பாடு' (பிப்ரவரி 2008) என்பதில் மாநிலங்களுக்கு இடையேயான நதிநீர் மோதல்கள் மற்றும் எல்லைத் தகராறுகளை விரிவாக ஆய்வு செய்தது.",
        why_a_en="Option A is on RTI (June 2006).",
        why_a_ta="விருப்பம் A தகவல் அறியும் உரிமை பற்றியது (ஜூன் 2006).",
        why_b_en="Option B is on Ethics in Governance (January 2007).",
        why_b_ta="விருப்பம் B ஆளுகையில் நெறிமுறைகள் பற்றியது (ஜனவரி 2007).",
        why_c_en="Option C is correct; the 7th Report specifically covers conflict resolution and inter-state water disputes.",
        why_c_ta="விருப்பம் C சரியானது; 7-வது அறிக்கை மோதல் தீர்வு மற்றும் நதிநீர் தகராறுகளைக் கையாள்கிறது.",
        why_d_en="Option D is on Citizen Centric Administration (February 2009).",
        why_d_ta="விருப்பம் D மக்களை மையமாகக் கொண்ட நிர்வாகம் பற்றியது (பிப்ரவரி 2009).",
        tip_en="2nd ARC 7th Report = 'Capacity Building for Peace and Conflict Resolution'.",
        tip_ta="2-வது ARC 7-வது அறிக்கை = 'அமைதி மற்றும் மோதல் தீர்வுக்கான திறன் மேம்பாடு'.",
        fact_en="The report recommended setting up river basin organizations with statutory dispute prevention mechanisms before issues escalate to tribunals.",
        fact_ta="பிரச்சனைகள் தீர்ப்பாயங்களுக்குச் செல்வதற்கு முன்பே தகராறைத் தடுக்கும் சட்டப்பூர்வ அமைப்புகளுடன் கூடிய நதி வடிநில அமைப்புகளை அமைக்க இந்த அறிக்கை பரிந்துரைத்தது."
    ))

    # 047 - Key D (Hard)
    qs.append(make_q(
        num=47, diff="Hard", qtype="Concept MCQ", subtopic="Inter-State River Water Disputes",
        en_stem="In its historic final judgment on the Cauvery River Water dispute in February 2018, what fundamental legal doctrine did the Supreme Court lay down regarding inter-state rivers?",
        ta_stem="பிப்ரவரி 2018 இல் காவிரி நதிநீர் தகராறு குறித்த வரலாற்றுச் சிறப்புமிக்க இறுதித் தீர்ப்பில், மாநிலங்களுக்கு இடையேயான நதிகள் குறித்து உச்ச நீதிமன்றம் வகுத்த அடிப்படைக் கோட்பாடு என்ன?",
        en_a="The upper riparian state has absolute sovereignty and unrestricted first right to use the entire river water", ta_a="மேல் வடிநில மாநிலத்திற்கு முழு இறையாண்மையும் நதிநீரை முழுமையாகப் பயன்படுத்த தடையற்ற முதல் உரிமையும் உண்டு",
        en_b="The lower riparian state holds absolute veto power over any dam construction upstream", ta_b="மேல் பகுதியில் எந்தவொரு அணை கட்டுவதற்கும் கீழ் வடிநில மாநிலத்திற்கு முழுமையான வீட்டோ அதிகாரம் உண்டு",
        en_c="Inter-state rivers are exclusively the private property of the Central Government under eminent domain", ta_c="மாநிலங்களுக்கு இடையேயான நதிகள் மத்திய அரசின் பிரத்யேக தனியார் சொத்து ஆகும்",
        en_d="Waters of an inter-state river are a national asset in which no single state can claim exclusive ownership, and equitable apportionment is the governing principle", ta_d="மாநிலங்களுக்கு இடையேயான ஒரு நதியின் நீர் என்பது ஒரு தேசிய சொத்து; அதில் எந்தவொரு தனி மாநிலமும் பிரத்யேக உரிமை கோர முடியாது; சமமான பங்கீடே ஆளுகை செய்யும் கோட்பாடாகும்",
        correct_key="D",
        exp_en="In State of Karnataka v. State of Tamil Nadu (February 2018), Chief Justice Dipak Misra writing for the 3-judge bench declared: 'Waters of an inter-State river passing through corridors of the riparian States is a national asset and no single State can claim exclusive ownership of its water.' The court upheld the doctrine of equitable apportionment.",
        exp_ta="பிப்ரவரி 2018 காவிரி இறுதித் தீர்ப்பில் உச்ச நீதிமன்றம், மாநிலங்கள் வழியே பாயும் நதிநீர் ஒரு தேசிய சொத்து என்றும், எந்தவொரு மாநிலமும் அதன் மீது பிரத்யேக உரிமை கோர முடியாது என்றும், சமமான பங்கீட்டுக் கோட்பாடே (Equitable Apportionment) ஆளுகை செய்யும் என்றும் திட்டவட்டமாக அறிவித்தது.",
        why_a_en="Option A is the Harmon Doctrine (territorial sovereignty), which was rejected by the Supreme Court.",
        why_a_ta="விருப்பம் A ஹார்மன் கோட்பாடு (முழு இறையாண்மை), இது உச்ச நீதிமன்றத்தால் நிராகரிக்கப்பட்டது.",
        why_b_en="Option B is the absolute territorial integrity doctrine, which was also rejected.",
        why_b_ta="விருப்பம் B முழுமையான பிராந்திய ஒருமைப்பாடு கோட்பாடு, இதுவும் நிராகரிக்கப்பட்டது.",
        why_c_en="Option C is incorrect; states have constitutional riparian rights subject to equitable sharing.",
        why_c_ta="விருப்பம் C தவறானது; மாநிலங்களுக்கு வடிநில உரிமைகள் உண்டு.",
        why_d_en="Option D is correct; inter-state rivers are a national asset governed by equitable apportionment.",
        why_d_ta="விருப்பம் D சரியானது; மாநிலங்களுக்கு இடையேயான நதிகள் சமமான பங்கீட்டிற்கு உட்பட்ட தேசிய சொத்து ஆகும்.",
        tip_en="Harmon Doctrine (absolute upper riparian right) is NOT followed in India. Equitable apportionment is the law.",
        tip_ta="ஹார்மன் கோட்பாடு (மேல் மாநிலத்தின் முழு உரிமை) இந்தியாவில் பின்பற்றப்படுவதில்லை. சமமான பங்கீடே இந்திய சட்டம்.",
        fact_en="The Supreme Court slightly reduced Tamil Nadu's share from 419 TMC (in 2007 CWDT award) to 404.25 TMC, citing groundwater availability in the delta.",
        fact_ta="காவிரி டெல்டாவில் நிலத்தடி நீர் இருப்பதைக் காரணம் காட்டி, உச்ச நீதிமன்றம் தமிழகத்தின் பங்கை 419 டி.எம்.சியில் இருந்து 404.25 டி.எம்.சியாகக் குறைத்தது."
    ))

    # 048 - Key A (Medium)
    qs.append(make_q(
        num=48, diff="Medium", qtype="Concept MCQ", subtopic="Inter-State River Water Disputes",
        en_stem="The historical Cauvery water agreements of 1892 and 1924 were entered into between which two historical political entities?",
        ta_stem="வரலாற்றுச் சிறப்புமிக்க 1892 மற்றும் 1924-ஆம் ஆண்டு காவிரி நதிநீர் ஒப்பந்தங்கள் எந்த இரண்டு வரலாற்று அரசியல் அமைப்புகளுக்கு இடையே கையெழுத்தாகின?",
        en_a="Madras Presidency and the Princely State of Mysore", ta_a="மெட்ராஸ் மாகாணம் மற்றும் மைசூர் சுதேச சமஸ்தானம்",
        en_b="Bombay Presidency and Hyderabad State", ta_b="பம்பாய் மாகாணம் மற்றும் ஹைதராபாத் சமஸ்தானம்",
        en_c="Madras Presidency and Travancore Kingdom", ta_c="மெட்ராஸ் மாகாணம் மற்றும் திருவிதாங்கூர் சமஸ்தானம்",
        en_d="Central Provinces and the Nizam of Hyderabad", ta_d="மத்திய மாகாணங்கள் மற்றும் ஹைதராபாத் நிஜாம்",
        correct_key="A",
        exp_en="The 1892 and 1924 Cauvery Agreements were concluded between the British-ruled Madras Presidency (representing lower riparian Tamil Nadu) and the Princely State of Mysore (upper riparian Karnataka).",
        exp_ta="1892 மற்றும் 1924 காவிரி ஒப்பந்தங்கள் பிரிட்டிஷ் ஆட்சியின் கீழிருந்த மெட்ராஸ் மாகாணம் (கீழ் வடிநில தமிழகம்) மற்றும் மைசூர் சுதேச சமஸ்தானம் (மேல் வடிநில கர்நாடகா) இடையே கையெழுத்தாகின.",
        why_a_en="Option A is correct; Madras Presidency and Mysore State signed both pacts.",
        why_a_ta="விருப்பம் A சரியானது; மெட்ராஸ் மாகாணமும் மைசூர் சமஸ்தானமும் இவ்விரு ஒப்பந்தங்களிலும் கையெழுத்திட்டன.",
        why_b_en="Option B deals with Krishna/Godavari disputes, not Cauvery.",
        why_b_ta="விருப்பம் B கிருஷ்ணா/கோதாவரி தொடர்பானது, காவிரி அல்ல.",
        why_c_en="Option C relates to Mullaperiyar / Periyar Lake Lease of 1886.",
        why_c_ta="விருப்பம் C முல்லைப் பெரியாறு 1886 குத்தகை ஒப்பந்தம் தொடர்பானது.",
        why_d_en="Option D is unrelated to the Cauvery river.",
        why_d_ta="விருப்பம் D காவிரி நதியுடன் தொடர்பில்லாதது.",
        tip_en="Cauvery 1892 & 1924 = Madras Presidency & Mysore. Periyar 1886 Lease = Madras Presidency & Travancore.",
        tip_ta="காவிரி 1892 & 1924 = மெட்ராஸ் மாகாணம் & மைசூர். பெரியாறு 1886 குத்தகை = மெட்ராஸ் & திருவிதாங்கூர்.",
        fact_en="The 1924 Agreement permitted Mysore to build the Krishnarajasagar Dam and Madras to construct the Mettur Dam.",
        fact_ta="1924 ஒப்பந்தம் மைசூர் கிருஷ்ணராஜ சாகர் அணையையும், மெட்ராஸ் மேட்டூர் அணையையும் கட்ட அனுமதித்தது."
    ))

    # 049 - Key B (Medium)
    qs.append(make_q(
        num=49, diff="Medium", qtype="Concept MCQ", subtopic="Inter-State River Water Disputes",
        en_stem="The Mahadayi Water Disputes Tribunal, constituted in November 2010, adjudicated disputes among which group of States?",
        ta_stem="நவம்பர் 2010 இல் அமைக்கப்பட்ட மகதாயி நதிநீர் தகராறு தீர்ப்பாயம், எந்த மாநிலங்களின் குழுவிற்கு இடையேயான தகராறுகளை விசாரித்தது?",
        en_a="Odisha, Andhra Pradesh, and Chhattisgarh", ta_a="ஒடிசா, ஆந்திரப் பிரதேசம் மற்றும் சத்தீஸ்கர்",
        en_b="Goa, Karnataka, and Maharashtra", ta_b="கோவா, கர்நாடகா மற்றும் மகாராஷ்டிரா",
        en_c="Punjab, Haryana, and Rajasthan", ta_c="பஞ்சாப், ஹரியானா மற்றும் ராஜஸ்தான்",
        en_d="Gujarat, Madhya Pradesh, and Rajasthan", ta_d="குஜராத், மத்தியப் பிரதேசம் மற்றும் ராஜஸ்தான்",
        correct_key="B",
        exp_en="The Mahadayi (Mandovi) River dispute involves Goa, Karnataka, and Maharashtra. The central point of contention is Karnataka's Kalasa-Banduri project to divert Mahadayi water to the Malaprabha basin.",
        exp_ta="மகதாயி (மாண்டோவி) நதிநீர் தகராறு கோவா, கர்நாடகா மற்றும் மகாராஷ்டிரா ஆகிய மாநிலங்களை உள்ளடக்கியது. மலபிரபா வடிநிலத்திற்கு தண்ணீரைத் திருப்ப கர்நாடகா முன்மொழிந்த கலசா-பண்டூரி திட்டமே இதன் முக்கிய சர்ச்சை.",
        why_a_en="Option A involves the Vansadhara and Mahanadi disputes.",
        why_a_ta="விருப்பம் A வம்சதாரா மற்றும் மகாநதி தகராறுகள் தொடர்பானது.",
        why_b_en="Option B is correct; Goa, Karnataka, and Maharashtra share the Mahadayi basin.",
        why_b_ta="விருப்பம் B சரியானது; கோவா, கர்நாடகா மற்றும் மகாராஷ்டிரா மகதாயி வடிநிலத்தைப் பகிர்ந்து கொள்கின்றன.",
        why_c_en="Option C involves the Ravi and Beas dispute.",
        why_c_ta="விருப்பம் C ரவி மற்றும் பியாஸ் தகராறு தொடர்பானது.",
        why_d_en="Option D involves the Narmada and Sabarmati disputes.",
        why_d_ta="விருப்பம் D நர்மதா தகராறு தொடர்பானது.",
        tip_en="Mahadayi River = Mandovi River = Goa, Karnataka, Maharashtra. Key project = Kalasa-Banduri Nala.",
        tip_ta="மகதாயி நதி = மாண்டோவி நதி = கோவா, கர்நாடகா, மகாராஷ்டிரா. முக்கிய திட்டம் = கலசா-பண்டூரி கால்வாய்.",
        fact_en="The Mahadayi Water Disputes Tribunal headed by Justice J.M. Panchal submitted its award in August 2018.",
        fact_ta="நீதிபதி ஜே.எம். பஞ்சால் தலைமையிலான மகதாயி நதிநீர் தீர்ப்பாயம் ஆகஸ்ட் 2018 இல் தனது தீர்ப்பை வழங்கியது."
    ))

    # 050 - Key C (Hard)
    qs.append(make_q(
        num=50, diff="Hard", qtype="Concept MCQ", subtopic="Inter-State River Water Disputes",
        en_stem="The Vansadhara Water Disputes Tribunal, constituted in February 2010, dealt with the construction of the Katragadda side weir involving which two neighboring States?",
        ta_stem="பிப்ரவரி 2010 இல் அமைக்கப்பட்ட வம்சதாரா நதிநீர் தகராறு தீர்ப்பாயம், கத்ரகட்டா பக்கவாட்டு அணைக்கட்டு கட்டுமானம் தொடர்பாக எந்த இரண்டு அண்டை மாநிலங்களுக்கு இடையேயான தகராறைக் கையாண்டது?",
        en_a="Tamil Nadu and Kerala", ta_a="தமிழ்நாடு மற்றும் கேரளா",
        en_b="Karnataka and Maharashtra", ta_b="கர்நாடகா மற்றும் மகாராஷ்டிரா",
        en_c="Andhra Pradesh and Odisha", ta_c="ஆந்திரப் பிரதேசம் மற்றும் ஒடிசா",
        en_d="West Bengal and Jharkhand", ta_d="மேற்கு வங்கம் மற்றும் ஜார்க்கண்ட்",
        correct_key="C",
        exp_en="The Vansadhara Water Disputes Tribunal was constituted in February 2010 to adjudicate the dispute between Andhra Pradesh and Odisha over the construction of a side weir at Katragadda by Andhra Pradesh.",
        exp_ta="வம்சதாரா நதிநீர் தகராறு தீர்ப்பாயம் பிப்ரவரி 2010 இல் அமைக்கப்பட்டது; ஆந்திரப் பிரதேசம் கத்ரகட்டாவில் ஒரு பக்கவாட்டு அணைக்கட்டைக் கட்டுவது தொடர்பாக ஆந்திரா மற்றும் ஒடிசா இடையேயான தகராறை இது விசாரித்தது.",
        why_a_en="Option A is Tamil Nadu and Kerala (Mullaperiyar / Parambikulam Aliyar).",
        why_a_ta="விருப்பம் A தமிழ்நாடு மற்றும் கேரளா (முல்லைப் பெரியாறு / பரம்பிக்குளம்).",
        why_b_en="Option B is Karnataka and Maharashtra (Krishna / Mahadayi).",
        why_b_ta="விருப்பம் B கர்நாடகா மற்றும் மகாராஷ்டிரா.",
        why_c_en="Option C is correct; Vansadhara flows between Odisha and Andhra Pradesh.",
        why_c_ta="விருப்பம் C சரியானது; வம்சதாரா நதி ஒடிசா மற்றும் ஆந்திரப் பிரதேசம் இடையே பாய்கிறது.",
        why_d_en="Option D is West Bengal and Jharkhand (Damodar / Subarnarekha).",
        why_d_ta="விருப்பம் D மேற்கு வங்கம் மற்றும் ஜார்க்கண்ட்.",
        tip_en="Vansadhara = Odisha & Andhra Pradesh. (Originates in Kalahandi, Odisha; empties into Bay of Bengal at Kalingapatnam, AP).",
        tip_ta="வம்சதாரா = ஒடிசா & ஆந்திரப் பிரதேசம் (ஒடிசாவின் காளஹாண்டியில் உற்பத்தியாகி, ஆந்திராவின் கலிங்கப்பட்டினத்தில் வங்காள விரிகுடாவில் கலக்கிறது).",
        fact_en="The Vansadhara Tribunal delivered its final report in September 2017, permitting Andhra Pradesh to construct the side weir with protective flood control embankments.",
        fact_ta="வம்சதாரா தீர்ப்பாயம் செப்டம்பர் 2017 இல் தனது இறுதி அறிக்கையை சமர்ப்பித்து, வெள்ளத் தடுப்பு கரைகளுடன் பக்கவாட்டு அணையைக் கட்ட ஆந்திராவிற்கு அனுமதி அளித்தது."
    ))

    return qs

if __name__ == "__main__":
    b2 = get_batch2()
    print(f"Batch 2 count: {len(b2)}")
    from collections import Counter
    print("Keys:", Counter([q["correct_answer"] for q in b2]))
    print("Diffs:", Counter([q["difficulty"] for q in b2]))
