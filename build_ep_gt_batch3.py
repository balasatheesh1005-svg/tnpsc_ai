# -*- coding: utf-8 -*-
"""
Emergency Provisions Grand Test - Batch 3 (Questions 51 to 75)
Prefix: EP_GT_
Keys: A: 6, B: 6, C: 7, D: 6 (Total: 25)
"""

from ep_mcq_helper import make_ep_q

PREFIX = "EP_GT_"

def get_gt_batch3():
    qs = []

    # 051 - Key C
    qs.append(make_ep_q(
        PREFIX, 51, "Medium", "Constitutional Ground", "Article 360 Ground",
        "Under Article 360 of the Constitution of India, on what ground can the President proclaim a Financial Emergency?",
        "இந்திய அரசியலமைப்பின் சரத்து 360-ன் கீழ், எந்தக் காரணத்தின் அடிப்படையில் குடியரசுத் தலைவர் நிதி அவசரநிலையைப் பிரகடனம் செய்ய முடியும்?",
        "When the fiscal deficit of the Union exceeds five percent of GDP", "மத்திய அரசின் நிதிப் பற்றாக்குறை மொத்த உள்நாட்டு உற்பத்தியில் ஐந்து சதவீதத்தைத் தாண்டும் போது",
        "When the Reserve Bank of India exhausts its foreign currency reserves", "இந்திய ரிசர்வ் வங்கியின் அன்னியச் செலாவணி இருப்பு தீர்ந்து போகும் போது",
        "If satisfied that a situation has arisen whereby the financial stability or credit of India or of any part of the territory thereof is threatened", "இந்தியாவின் அல்லது அதன் பிராந்தியத்தின் ஏதேனும் ஒரு பகுதியின் நிதி நிலைத்தன்மை அல்லது கடன் நம்பகத்தன்மை அச்சுறுத்தலுக்கு உள்ளாகியுள்ளதாகத் திருப்தியடைந்தால்",
        "When all state governments fail to pay salaries to government employees", "அனைத்து மாநில அரசுகளும் அரசு ஊழியர்களுக்கு ஊதியம் வழங்கத் தவறும் போது",
        "C",
        "Article 360(1) empowers the President to declare a Financial Emergency if he is satisfied that a situation has arisen whereby the financial stability or credit of India or of any part of the territory thereof is threatened.",
        "சரத்து 360(1)-ன் கீழ், இந்தியாவின் அல்லது அதன் பிராந்தியத்தின் ஏதேனும் ஒரு பகுதியின் நிதி நிலைத்தன்மை அல்லது கடன் நம்பகத்தன்மைக்கு அச்சுறுத்தல் ஏற்பட்டுள்ளது என குடியரசுத் தலைவர் திருப்தியடைந்தால் நிதி அவசரநிலையை அறிவிக்க முடியும்.",
        "Option A is a statutory fiscal target under the FRBM Act, not a constitutional ground.", "விருப்பம் A என்பது FRBM சட்டத்தின் கீழ் உள்ள நிதி இலக்கு, அரசியலமைப்பு காரணம் அல்ல.",
        "Option B describes an economic crisis indicator.", "விருப்பம் B பொருளாதார நெருக்கடி அறிகுறியைக் குறிக்கிறது.",
        "Option C is correct; exact constitutional ground under Article 360(1).", "விருப்பம் C சரியானது; சரத்து 360(1)-ன் கீழான துல்லியமான அரசியலமைப்பு விதி.",
        "Option D is an extreme consequence, not the constitutional definition.", "விருப்பம் D தீவிர விளைவே தவிர, அரசியலமைப்பு வரையறை அல்ல.",
        "TNPSC Article 360 Ground: 'Financial stability or credit of India or of any part thereof is threatened'.",
        "TNPSC சரத்து 360 காரணம்: 'இந்தியாவின் அல்லது அதன் பகுதியின் நிதி நிலைத்தன்மை அல்லது கடன் நம்பகத்தன்மை அச்சுறுத்தலுக்கு உள்ளாதல்'.",
        "The 38th Amendment made the President's satisfaction final and conclusive, but the 44th Amendment deleted that clause to restore judicial review.",
        "38-வது திருத்தம் குடியரசுத் தலைவரின் திருப்தியை இறுதியானது என்றாக்கியது, ஆனால் 44-வது திருத்தம் அதை நீக்கி நீதி மறுஆய்வை மீட்டெடுத்தது."
    ))

    # 052 - Key A
    qs.append(make_ep_q(
        PREFIX, 52, "Medium", "Procedural", "Article 360 Parliamentary Approval Deadline",
        "A proclamation of Financial Emergency under Article 360 must be approved by both Houses of Parliament within what timeframe?",
        "சரத்து 360-ன் கீழான நிதி அவசரநிலைப் பிரகடனம் பாராளுமன்றத்தின் இரு அவைகளாலும் எந்தக் காலக்கெடுவிற்குள் அங்கீகரிக்கப்பட வேண்டும்?",
        "Within two months from the date of its issue", "வெளியிடப்பட்ட தேதியிலிருந்து இரண்டு மாதங்களுக்குள்",
        "Within one month from the date of its issue", "வெளியிடப்பட்ட தேதியிலிருந்து ஒரு மாதத்திற்குள்",
        "Within fourteen days from the date of its issue", "வெளியிடப்பட்ட தேதியிலிருந்து பதினான்கு நாட்களுக்குள்",
        "Within six months from the date of its issue", "வெளியிடப்பட்ட தேதியிலிருந்து ஆறு மாதங்களுக்குள்",
        "A",
        "Under Article 360(2), a proclamation of Financial Emergency must be approved by both Houses of Parliament within two months from the date of its issue.",
        "சரத்து 360(2)-ன் கீழ், நிதி அவசரநிலைப் பிரகடனம் வெளியிடப்பட்ட தேதியிலிருந்து இரண்டு மாதங்களுக்குள் பாராளுமன்றத்தின் இரு அவைகளாலும் அங்கீகரிக்கப்பட வேண்டும்.",
        "Option A is correct; two months under Article 360(2).", "விருப்பம் A சரியானது; சரத்து 360(2)-ன் கீழ் இரண்டு மாதங்கள்.",
        "Option B (one month) applies strictly to Article 352.", "விருப்பம் B (1 மாதம்) சரத்து 352-க்கு மட்டுமே பொருந்தும்.",
        "Option C (14 days) is for disapproval notice sittings.", "விருப்பம் C (14 நாட்கள்) நிராகரிப்பு சிறப்புக் கூட்டங்களுக்கானது.",
        "Option D (six months) is the renewal duration for Articles 352 and 356.", "விருப்பம் D (6 மாதங்கள்) சரத்துகள் 352, 356-ன் புதுப்பித்தல் காலமாகும்.",
        "Approval Timelines Summary: Article 352 = 1 Month; Article 356 = 2 Months; Article 360 = 2 Months.",
        "ஒப்புதல் காலக்கெடு சுருக்கம்: சரத்து 352 = 1 மாதம்; சரத்து 356 = 2 மாதங்கள்; சரத்து 360 = 2 மாதங்கள்.",
        "If Lok Sabha is dissolved during the two months, Rajya Sabha must approve within two months, and the new Lok Sabha within 30 days of its first sitting.",
        "இரண்டு மாத காலத்தில் மக்களவை கலைக்கப்பட்டால், மாநிலங்களவை 2 மாதங்களிலும், புதிய மக்களவை கூடிய 30 நாட்களுக்குள்ளும் ஒப்புதல் அளிக்க வேண்டும்."
    ))

    # 053 - Key B
    qs.append(make_ep_q(
        PREFIX, 53, "Medium", "Procedural", "Article 360 Parliamentary Majority",
        "What type of majority in Parliament is required to approve a resolution for proclamation of Financial Emergency under Article 360?",
        "சரத்து 360-ன் கீழான நிதி அவசரநிலைப் பிரகடனத் தீர்மானத்திற்கு ஒப்புதல் அளிக்க பாராளுமன்றத்தில் எந்த வகையான பெரும்பான்மை தேவைப்படுகிறது?",
        "Special majority of total membership and 2/3 present and voting", "மொத்த உறுப்பினர்களில் பெரும்பான்மை மற்றும் வருகை தந்து வாக்களிப்போரில் 2/3 பங்கு சிறப்புப் பெரும்பான்மை",
        "Simple majority of members present and voting in each House", "ஒவ்வொரு அவையிலும் வருகை தந்து வாக்களிக்கும் உறுப்பினர்களில் எளிய பெரும்பான்மை",
        "Two-thirds majority of the total membership of each House", "ஒவ்வொரு அவையின் மொத்த உறுப்பினர்களில் மூன்றில் இரண்டு பங்கு பெரும்பான்மை",
        "Absolute majority of the Lok Sabha alone", "மக்களவையின் முழுமையான பெரும்பான்மை மட்டுமே",
        "B",
        "Under Article 360(2), a resolution approving Financial Emergency can be passed by either House of Parliament only by a simple majority, that is, a majority of the members of that House present and voting.",
        "சரத்து 360(2)-ன் கீழ், நிதி அவசரநிலைக்கு ஒப்புதல் அளிக்கும் தீர்மானத்தை பாராளுமன்றத்தின் இரு அவைகளும் எளிய பெரும்பான்மையால் (வருகை தந்து வாக்களிக்கும் உறுப்பினர்களில் பெரும்பான்மை) மட்டுமே நிறைவேற்ற முடியும்.",
        "Option A (special majority) is required strictly for Article 352 National Emergency.", "விருப்பம் A சரத்து 352 தேசிய அவசரநிலைக்கு மட்டுமே தேவைப்படுகிறது.",
        "Option B is correct; simple majority governs Article 360 approval.", "விருப்பம் B சரியானது; எளிய பெரும்பான்மையே சரத்து 360-ன் ஒப்புதலை நிர்வகிக்கிறது.",
        "Option C applies to presidential impeachment under Article 61.", "விருப்பம் C சரத்து 61 பதவி நீக்கத்திற்குப் பொருந்தும்.",
        "Option D is incorrect because Rajya Sabha has equal approval power.", "விருப்பம் D தவறு, ஏனெனில் மாநிலங்களவைக்கும் சமமான ஒப்புதல் அதிகாரம் உண்டு.",
        "Majority Summary: Article 352 = Special Majority; Article 356 = Simple Majority; Article 360 = Simple Majority.",
        "பெரும்பான்மை சுருக்கம்: சரத்து 352 = சிறப்புப் பெரும்பான்மை; சரத்து 356 = எளிய பெரும்பான்மை; சரத்து 360 = எளிய பெரும்பான்மை.",
        "Both Houses of Parliament have co-equal powers in approving a Financial Emergency.",
        "நிதி அவசரநிலைக்கு ஒப்புதல் அளிப்பதில் பாராளுமன்றத்தின் இரு அவைகளுக்கும் சமமான அதிகாரங்கள் உள்ளன."
    ))

    # 054 - Key D
    qs.append(make_ep_q(
        PREFIX, 54, "Hard", "Constitutional Duration", "Article 360 Duration Nuance",
        "Once approved by both Houses of Parliament, for how long does a Financial Emergency under Article 360 continue to operate?",
        "பாராளுமன்றத்தின் இரு அவைகளாலும் அங்கீகரிக்கப்பட்டவுடன், சரத்து 360-ன் கீழான நிதி அவசரநிலை எவ்வளவு காலம் தொடர்ந்து செயல்பாட்டில் இருக்கும்?",
        "For a maximum period of six months unless renewed", "புதுப்பிக்கப்படாவிட்டால் அதிகபட்சமாக ஆறு மாத காலம்",
        "For a maximum period of one year", "அதிகபட்சமாக ஒரு வருட காலம்",
        "For a maximum period of three years like President's Rule", "குடியரசுத் தலைவர் ஆட்சி போல அதிகபட்சமாக மூன்று ஆண்டுகள்",
        "Indefinitely until it is revoked by the President, with NO periodic parliamentary renewal required", "குடியரசுத் தலைவரால் ரத்து செய்யப்படும் வரை காலவரையின்றி; மேலும் காலமுறை பாராளுமன்றப் புதுப்பித்தல் எதுவும் தேவையில்லை",
        "D",
        "Once approved by both Houses of Parliament, a Financial Emergency continues INDEFINITELY until it is revoked by the President. There is NO maximum period prescribed for its operation, and repeated periodic parliamentary approval is NOT required for its continuation.",
        "பாராளுமன்றத்தின் இரு அவைகளாலும் ஒப்புதல் அளிக்கப்பட்டவுடன், குடியரசுத் தலைவரால் ரத்து செய்யப்படும் வரை நிதி அவசரநிலை காலவரையின்றித் தொடர்கிறது. அதன் செயல்பாட்டிற்கு எந்தவொரு அதிகபட்ச கால வரம்பும் நிர்ணயிக்கப்படவில்லை, மேலும் அது தொடர்வதற்கு மீண்டும் மீண்டும் பாராளுமன்ற ஒப்புதல் தேவையில்லை.",
        "Option A describes Article 352 and 356, which require 6-month renewal.", "விருப்பம் A சரத்துகள் 352 மற்றும் 356-ஐ விவரிக்கிறது.",
        "Option B is not a constitutional duration under Article 360.", "விருப்பம் B சரத்து 360-ன் கீழான கால அளவு அல்ல.",
        "Option C describes the upper ceiling of Article 356.", "விருப்பம் C சரத்து 356-ன் உச்சவரம்பை விவரிக்கிறது.",
        "Option D is correct; continues indefinitely without periodic renewal until revoked.", "விருப்பம் D சரியானது; ரத்து செய்யப்படும் வரை புதுப்பித்தலின்றி காலவரையின்றித் தொடர்கிறது.",
        "TNPSC High-Yield Contrast: Articles 352 and 356 require parliamentary renewal every 6 months; Article 360 requires NO renewal once approved!",
        "TNPSC உயர்-விளைச்சல் ஒப்பீடு: சரத்துகள் 352 மற்றும் 356-க்கு ஒவ்வொரு 6 மாதங்களுக்கும் பாராளுமன்றப் புதுப்பித்தல் தேவை; சரத்து 360-க்கு ஒருமுறை ஒப்புதல் பெற்ற பின் புதுப்பித்தல் தேவையில்லை!",
        "Its revocation can be done at any time by the President by a subsequent proclamation without parliamentary approval.",
        "பாராளுமன்ற ஒப்புதலின்றி குடியரசுத் தலைவரால் எந்த நேரத்திலும் இதனை ரத்து செய்ய முடியும்."
    ))

    # 055 - Key C
    qs.append(make_ep_q(
        PREFIX, 55, "Hard", "Constitutional Impact", "Salaries of Judges under Article 360",
        "Under Article 360(4)(b), whose salaries and allowances can the President direct to be reduced during a Financial Emergency?",
        "சரத்து 360(4)(b)-ன் கீழ், நிதி அவசரநிலையின் போது யாருடைய ஊதியங்கள் மற்றும் படிகளைக் குறைக்க குடியரசுத் தலைவர் உத்தரவிட முடியும்?",
        "Only members of the Union Council of Ministers and Governors", "மத்திய அமைச்சரவை உறுப்பினர்கள் மற்றும் ஆளுநர்கள் மட்டுமே",
        "Only officers of the All India Services (IAS, IPS, IFS)", "அகில இந்தியப் பணி அதிகாரிகள் (IAS, IPS, IFS) மட்டுமே",
        "All persons serving the Union, INCLUDING the Judges of the Supreme Court and the High Courts", "உச்ச நீதிமன்ற மற்றும் உயர் நீதிமன்ற நீதிபதிகள் உட்பட மத்திய அரசின் கீழ் பணியாற்றும் அனைத்து நபர்களும்",
        "Private sector bank employees and central public sector executives only", "தனியார் வங்கி ஊழியர்கள் மற்றும் பொதுத்துறை நிறுவனங்களின் அதிகாரிகள் மட்டுமே",
        "C",
        "Under Article 360(4)(b), the President may issue directions for the reduction of salaries and allowances of all or any class of persons serving in connection with the affairs of the Union, including the Judges of the Supreme Court and the High Courts.",
        "சரத்து 360(4)(b)-ன் கீழ், உச்ச நீதிமன்ற மற்றும் உயர் நீதிமன்ற நீதிபதிகள் உட்பட, மத்திய அரசின் விவகாரங்கள் தொடர்பாகப் பணியாற்றும் அனைத்து அல்லது ஏதேனும் ஒரு வகுப்பைச் சேர்ந்த நபர்களின் ஊதியங்கள் மற்றும் படிகளைக் குறைக்கக் குடியரசுத் தலைவர் வழிகாட்டலாம்.",
        "Option A is too narrow and misses judicial officers.", "விருப்பம் A மிகவும் குறுகியது மற்றும் நீதிபதிகளை விடுக்கிறது.",
        "Option B is incomplete.", "விருப்பம் B முழுமையற்றது.",
        "Option C is correct; specifically includes Supreme Court and High Court judges.", "விருப்பம் C சரியானது; உச்ச மற்றும் உயர் நீதிமன்ற நீதிபதிகளை வெளிப்படையாக உள்ளடக்குகிறது.",
        "Option D mentions private employees over whom Constitution gives no direct emergency reduction power.", "விருப்பம் D தனியார் ஊழியர்களைக் குறிப்பிடுகிறது.",
        "Constitutional Exception: Normally, judicial salaries cannot be varied to their disadvantage (Articles 125 & 221); Financial Emergency (Article 360) is the ONLY exception!",
        "அரசியலமைப்பு விதிவிலக்கு: பொதுவாக நீதிபதிகளின் ஊதியத்தைக் குறைக்க முடியாது (சரத்துகள் 125 & 221); நிதி அவசரநிலை (சரத்து 360) மட்டுமே இதற்குரிய ஒரே விதிவிலக்காகும்!",
        "This unique provision emphasizes the comprehensive sacrifice expected from all constitutional functionaries during a national financial crisis.",
        "தேசிய நிதி நெருக்கடியின் போது அனைத்து அரசியலமைப்புப் பதவியாளர்களிடமிருந்தும் எதிர்பார்க்கப்படும் முழுமையான அர்ப்பணிப்பை இந்த விதி உணர்த்துகிறது."
    ))

    # 056 - Key A
    qs.append(make_ep_q(
        PREFIX, 56, "Hard", "State Financial Control", "Money Bills Reservation under Article 360",
        "During the operation of a Financial Emergency under Article 360, what special power can the President require states to observe regarding financial legislation?",
        "சரத்து 360-ன் கீழான நிதி அவசரநிலையின் போது, நிதிச் சட்டங்கள் தொடர்பாக மாநிலங்கள் கடைப்பிடிக்க வேண்டும் என்று குடியரசுத் தலைவர் என்ன சிறப்பு அதிகாரத்தை உத்தரவிடலாம்?",
        "That all Money Bills or other Financial Bills passed by the State Legislature be reserved for the consideration of the President", "மாநில சட்டமன்றத்தால் நிறைவேற்றப்படும் அனைத்து பண மசோதாக்கள் அல்லது பிற நிதி மசோதாக்களும் குடியரசுத் தலைவரின் பரிசீலனைக்காக ஒதுக்கப்பட வேண்டும் என்பது",
        "That the State Legislature can pass only one budget every three years", "மாநில சட்டமன்றம் மூன்று ஆண்டுகளுக்கு ஒருமுறை மட்டுமே ஒரு வரவு-செலவுத் திட்டத்தை நிறைவேற்ற முடியும் என்பது",
        "That all state commercial taxes be collected directly by the Reserve Bank of India", "அனைத்து மாநில வணிக வரிகளும் இந்திய ரிசர்வ் வங்கியால் நேரடியாக வசூலிக்கப்பட வேண்டும் என்பது",
        "That the state governor be replaced by a Union Finance Ministry joint secretary", "மாநில ஆளுநருக்குப் பதிலாக மத்திய நிதி அமைச்சக இணைச் செயலாளர் நியமிக்கப்பட வேண்டும் என்பது",
        "A",
        "Under Article 360(4)(a)(ii), the executive directions issued during a Financial Emergency may include a provision requiring all Money Bills or other Financial Bills to be reserved for the consideration of the President after they are passed by the Legislature of the State.",
        "சரத்து 360(4)(a)(ii)-ன் கீழ், நிதி அவசரநிலையின் போது வழங்கப்படும் நிர்வாக வழிகாட்டுதல்கள், மாநில சட்டமன்றத்தால் நிறைவேற்றப்பட்ட பிறகு அனைத்து பண மசோதாக்களும் அல்லது பிற நிதி மசோதாக்களும் குடியரசுத் தலைவரின் பரிசீலனைக்காக ஒதுக்கப்பட வேண்டும் என்ற விதியை உள்ளடக்கலாம்.",
        "Option A is correct; mandatory reservation of all state Money Bills for President.", "விருப்பம் A சரியானது; அனைத்து மாநில பண மசோதாக்களையும் குடியரசுத் தலைவருக்கு கட்டாயமாக ஒதுக்குதல்.",
        "Option B is false; budget cycle remains annual.", "விருப்பம் B தவறு; வரவு-செலவுத் திட்டம் ஆண்டுதோறும் சமர்ப்பிக்கப்படுகிறது.",
        "Option C is baseless.", "விருப்பம் C ஆதாரமற்றது.",
        "Option D is constitutionally absurd.", "விருப்பம் D அரசியலமைப்பில் இல்லாதது.",
        "Financial Centralization: Article 360(4)(a)(ii) gives the Union total control over every state's purse strings.",
        "நிதி மையப்படுத்தல்: சரத்து 360(4)(a)(ii) ஒவ்வொரு மாநிலத்தின் நிதிப் பெட்டகத்தின் மீதும் மத்திய அரசுக்கு முழுமையான கட்டுப்பாட்டை அளிக்கிறது.",
        "Normally, reservation of state bills for the President under Article 200 is at the discretion of the Governor; under Article 360, it becomes a mandatory requirement.",
        "பொதுவாக சரத்து 200-ன் கீழ் குடியரசுத் தலைவருக்கு மசோதாக்களை ஒதுக்குவது ஆளுநரின் விருப்ப அதிகாரம்; ஆனால் சரத்து 360-ல் அது ஒரு கட்டாயத் தேவையாக மாறுகிறது."
    ))

    # 057 - Key B
    qs.append(make_ep_q(
        PREFIX, 57, "Medium", "Union Directives", "Canons of Financial Propriety",
        "Under Article 360(3), the executive authority of the Union extends to giving directions to any State to observe such canons of what nature?",
        "சரத்து 360(3)-ன் கீழ், எந்தவொரு மாநிலத்திற்கும் எந்த வகையான கோட்பாடுகளைக் கடைப்பிடிக்குமாறு வழிகாட்டுதல்களை வழங்கும் அதிகாரம் மத்திய அரசுக்கு உண்டு?",
        "Canons of criminal procedure and judicial discipline", "குற்றவியல் நடைமுறை மற்றும் நீதித்துறை ஒழுங்குமுறைக் கோட்பாடுகள்",
        "Canons of financial propriety as may be specified in the directions", "வழிகாட்டுதல்களில் குறிப்பிடப்படக்கூடிய நிதி ஒழுங்குமுறைக் கோட்பாடுகள் (canons of financial propriety)",
        "Canons of military protocol and defense preparedness", "இராணுவ மரபு மற்றும் பாதுகாப்புத் தயார்நிலைக் கோட்பாடுகள்",
        "Canons of international trade and maritime law", "சர்வதேச வர்த்தகம் மற்றும் கடல்சார் சட்டக் கோட்பாடுகள்",
        "B",
        "Under Article 360(3), during the period a Financial Emergency is in operation, the executive authority of the Union extends to the giving of directions to any State to observe such canons of financial propriety as may be specified in the directions, and to the giving of such other directions as the President may deem necessary and adequate for the purpose.",
        "சரத்து 360(3)-ன் கீழ், நிதி அவசரநிலை செயல்பாட்டில் உள்ள காலத்தில், வழிகாட்டுதல்களில் குறிப்பிடப்படக்கூடிய நிதி ஒழுங்குமுறைக் கோட்பாடுகளைக் கடைப்பிடிக்குமாறு எந்தவொரு மாநிலத்திற்கும் வழிகாட்டுதல்களை வழங்கும் அதிகாரம் மத்திய அரசுக்கு உண்டு, மேலும் இக்குறிக்கோளுக்காகக் குடியரசுத் தலைவர் அவசியமெனக் கருதும் பிற வழிகாட்டுதல்களையும் வழங்கலாம்.",
        "Option A deals with criminal law under Concurrent List.", "விருப்பம் A பொதுப்பட்டியலின் குற்றவியல் சட்டம் தொடர்பானது.",
        "Option B is correct; canons of financial propriety.", "விருப்பம் B சரியானது; நிதி ஒழுங்குமுறைக் கோட்பாடுகள்.",
        "Option C deals with defense under Union List.", "விருப்பம் C மத்தியப் பட்டியலின் பாதுகாப்பு தொடர்பானது.",
        "Option D pertains to international law.", "விருப்பம் D சர்வதேச சட்டம் தொடர்பானது.",
        "Constitutional Phrase: 'Canons of financial propriety' is the exact constitutional terminology in Article 360(3).",
        "அரசியலமைப்பு சொற்றொடர்: 'நிதி ஒழுங்குமுறைக் கோட்பாடுகள்' என்பதே சரத்து 360(3)-ன் துல்லியமான அரசியலமைப்புச் சொல்லாகும்.",
        "Under these canons, the Union can order a state to reduce expenditure, stop subsidies, or curtail discretionary borrowing.",
        "இந்தக் கோட்பாடுகளின் கீழ், செலவினங்களைக் குறைக்கவும், மானியங்களை நிறுத்தவும் அல்லது கடன்களைக் கட்டுப்படுத்தவும் மத்திய அரசு மாநிலத்திற்கு உத்தரவிடலாம்."
    ))

    # 058 - Key D
    qs.append(make_ep_q(
        PREFIX, 58, "Easy", "Historical", "Frequency of Financial Emergency",
        "How many times has a Financial Emergency under Article 360 been proclaimed in India since January 26, 1950?",
        "ஜனவரி 26, 1950 முதல் இந்தியாவில் சரத்து 360-ன் கீழான நிதி அவசரநிலை எத்தனை முறை பிரகடனப்படுத்தப்பட்டுள்ளது?",
        "Three times (1962, 1971, 1975)", "மூன்று முறை (1962, 1971, 1975)",
        "Twice (1966 and 1991)", "இரண்டு முறை (1966 மற்றும் 1991)",
        "Once (during the balance of payments crisis of 1991)", "ஒரு முறை (1991 அன்னியச் செலாவணி நெருக்கடியின் போது)",
        "Zero times (Never proclaimed so far)", "பூஜ்ஜியம் முறை (இதுவரை ஒருமுறை கூட அறிவிக்கப்படவில்லை)",
        "D",
        "No Financial Emergency under Article 360 has ever been proclaimed in India since the adoption of the Constitution in 1950. Even during the critical economic balance-of-payments crisis of 1991, India avoided declaring financial emergency.",
        "1950-ல் அரசியலமைப்பு ஏற்றுக்கொள்ளப்பட்டதிலிருந்து இந்தியாவில் சரத்து 360-ன் கீழான நிதி அவசரநிலை ஒருமுறை கூட அறிவிக்கப்படவில்லை. 1991-ல் மிகக் கடுமையான அன்னியச் செலாவணி பொருளாதார நெருக்கடி ஏற்பட்டபோது கூட, இந்தியா நிதி அவசரநிலையை அறிவிப்பதைத் தவிர்த்தது.",
        "Option A lists the three National Emergency proclamations.", "விருப்பம் A மூன்று தேசிய அவசரநிலைப் பிரகடனங்களைக் குறிப்பிடுகிறது.",
        "Option B is factually incorrect.", "விருப்பம் B தவறானது.",
        "Option C is a common misconception; 1991 saw economic reforms, not Article 360.", "விருப்பம் C தவறான பொதுக் கருத்தாகும்; 1991 பொருளாதார சீர்திருத்தங்களைக் கண்டதே தவிர சரத்து 360-ஐ அல்ல.",
        "Option D is correct; exactly zero times.", "விருப்பம் D சரியானது; சரியாக பூஜ்ஜியம் முறை.",
        "TNPSC Standard Fact: Article 360 has NEVER been used in India (0 times).",
        "TNPSC நிலையான உண்மை: சரத்து 360 இந்தியாவில் ஒருபோதும் பயன்படுத்தப்படவில்லை (0 முறை).",
        "Dr. H.N. Kunzru in the Constituent Assembly had criticized Article 360 as posing a serious threat to state financial autonomy.",
        "அரசியலமைப்பு நிர்ணய சபையில் டாக்டர் எச்.என். குன்ஸ்ரு சரத்து 360-ஐ மாநிலங்களின் நிதி சுயாட்சிக்கு கடுமையான அச்சுறுத்தல் என்று விமர்சித்திருந்தார்."
    ))

    # 059 - Key C
    qs.append(make_ep_q(
        PREFIX, 59, "Medium", "Historical Economics", "1991 Crisis and Article 360",
        "During the severe balance of payments crisis of 1991, why was Financial Emergency under Article 360 NOT proclaimed in India?",
        "1991-ன் கடுமையான அன்னியச் செலாவணி நெருக்கடியின் போது, இந்தியாவில் சரத்து 360-ன் கீழான நிதி அவசரநிலை ஏன் அறிவிக்கப்படவில்லை?",
        "Because the Supreme Court had struck down Article 360 in 1980", "1980-ல் உச்ச நீதிமன்றம் சரத்து 360-ஐ ரத்து செய்துவிட்டதால்",
        "Because Parliament was permanently dissolved at that time", "அக்காலத்தில் பாராளுமன்றம் நிரந்தரமாகக் கலைக்கப்பட்டிருந்ததால்",
        "Because the Government chose economic structural reforms (LPG), pledged gold reserves, and secured IMF assistance rather than resorting to constitutional emergency", "அரசியலமைப்பு அவசரநிலையை நாடுவதற்குப் பதிலாக, பொருளாதார கட்டமைப்பு சீர்திருத்தங்கள் (தாராளமயமாக்கல், தனியார்மயமாக்கல், உலகமயமாக்கல்), தங்கக் கையிருப்பு அடமானம் மற்றும் IMF நிதி உதவி ஆகியவற்றை அரசு தேர்ந்தெடுத்ததால்",
        "Because Article 360 can only be proclaimed during wartime", "போர்க்காலத்தில் மட்டுமே சரத்து 360-ஐ அறிவிக்க முடியும் என்பதால்",
        "C",
        "During the acute 1991 crisis, India's foreign exchange reserves plummeted to under three weeks of imports. Rather than declaring a Financial Emergency under Article 360 (which could have damaged international investor confidence), Prime Minister P.V. Narasimha Rao and Finance Minister Dr. Manmohan Singh initiated structural economic reforms (LPG policy), secured an IMF loan, and temporarily pledged gold reserves.",
        "1991-ன் கடுமையான நெருக்கடியின் போது, இந்தியாவின் அன்னியச் செலாவணி இருப்பு மூன்று வார இறக்குமதிக்கு மட்டுமே போதுமானதாகக் குறைந்தது. சரத்து 360-ன் கீழ் நிதி அவசரநிலையை அறிவித்தால் சர்வதேச முதலீட்டாளர்களின் நம்பிக்கை பாழாகும் என்பதால், பிரதமர் பி.வி. நரசிம்ம ராவ் மற்றும் நிதி அமைச்சர் டாக்டர் மன்மோகன் சிங் கட்டமைப்பு சீர்திருத்தங்களை (LPG கொள்கை) அறிமுகப்படுத்தினர், IMF கடனைப் பெற்றனர் மற்றும் தங்கக் கையிருப்பை அடமானம் வைத்தனர்.",
        "Option A is false; Article 360 remains fully valid in the Constitution.", "விருப்பம் A தவறு; சரத்து 360 அரசியலமைப்பில் தொடர்ந்து செல்லுபடியாகிறது.",
        "Option B is false.", "விருப்பம் B தவறானது.",
        "Option C is correct; economic and policy solutions were preferred over emergency powers.", "விருப்பம் C சரியானது; அவசரநிலைக்குப் பதிலாக பொருளாதாரக் கொள்கை தீர்வுகள் தேர்ந்தெடுக்கப்பட்டன.",
        "Option D is false; Article 360 is completely independent of war.", "விருப்பம் D தவறு; சரத்து 360 போருடன் தொடர்பற்றது.",
        "Economic History: The 1991 BoP crisis led to the historic New Economic Policy (NEP) of Liberalisation, Privatisation, and Globalisation, avoiding Article 360.",
        "பொருளாதார வரலாறு: 1991 அன்னியச் செலாவணி நெருக்கடி சரத்து 360-ஐத் தவிர்த்து, வரலாற்றுச் சிறப்புமிக்க புதிய பொருளாதாரக் கொள்கைக்கு (LPG) வழிவகுத்தது.",
        "This demonstrated that normal constitutional and economic mechanisms are adequate to navigate even severe financial stress.",
        "கடுமையான நிதி நெருக்கடியைக் கூடக் கடக்க இயல்பான அரசியலமைப்பு மற்றும் பொருளாதார வழிமுறைகளே போதுமானவை என்பதை இது நிரூபித்தது."
    ))

    # 060 - Key A
    qs.append(make_ep_q(
        PREFIX, 60, "Medium", "Procedural", "Revocation of Article 360",
        "Under Article 360(2)(a), how may a proclamation of Financial Emergency be revoked?",
        "சரத்து 360(2)(a)-ன் கீழ், நிதி அவசரநிலைப் பிரகடனம் எவ்வாறு ரத்து செய்யப்படலாம்?",
        "By a subsequent proclamation issued by the President at any time, requiring no parliamentary approval", "குடியரசுத் தலைவரால் எந்த நேரத்திலும் வெளியிடப்படும் பிந்தைய பிரகடனம் மூலம்; இதற்கு பாராளுமன்ற ஒப்புதல் தேவையில்லை",
        "By a resolution passed by a special majority in both Houses of Parliament", "பாராளுமன்றத்தின் இரு அவைகளிலும் சிறப்புப் பெரும்பான்மையால் நிறைவேற்றப்படும் தீர்மானத்தின் மூலம்",
        "By an order issued by the Governor of the Reserve Bank of India", "இந்திய ரிசர்வ் வங்கி ஆளுநர் பிறப்பிக்கும் உத்தரவின் மூலம்",
        "By a resolution passed by a majority of State Legislatures", "மாநில சட்டமன்றங்களின் பெரும்பான்மையால் நிறைவேற்றப்படும் தீர்மானத்தின் மூலம்",
        "A",
        "Under Article 360(2)(a), a proclamation of Financial Emergency may be revoked or varied by a subsequent proclamation by the President. Like Article 352 and 356 revocations, this does NOT require parliamentary approval.",
        "சரத்து 360(2)(a)-ன் கீழ், நிதி அவசரநிலைப் பிரகடனம் குடியரசுத் தலைவரால் பிந்தைய பிரகடனம் மூலம் ரத்து செய்யப்படலாம் அல்லது மாற்றப்படலாம். சரத்துகள் 352 மற்றும் 356-ஐப் போலவே, இதற்கும் பாராளுமன்ற ஒப்புதல் எதுவும் தேவையில்லை.",
        "Option A is correct; President by subsequent proclamation.", "விருப்பம் A சரியானது; பிந்தைய பிரகடனம் மூலம் குடியரசுத் தலைவர் ரத்து செய்யலாம்.",
        "Option B describes approval, not revocation.", "விருப்பம் B ஒப்புதலை விவரிக்கிறது.",
        "Option C is baseless.", "விருப்பம் C ஆதாரமற்றது.",
        "Option D is wrong; State Legislatures have no power to revoke emergency.", "விருப்பம் D தவறு; மாநில சட்டமன்றங்களுக்கு ரத்து செய்யும் அதிகாரம் இல்லை.",
        "Revocation Consistency: All three emergencies (National, State, Financial) can be revoked by the President unilaterally without Parliament.",
        "ரத்து சீரான தன்மை: மூன்று அவசரநிலைகளையும் (தேசிய, மாநில, நிதி) பாராளுமன்ற ஒப்புதலின்றி குடியரசுத் தலைவர் தன்னிச்சையாக ரத்து செய்ய முடியும்.",
        "The only parliamentary check on revocation is for Article 352, where Lok Sabha can PASS A RESOLUTION disapproving continuation.",
        "ரத்து செய்வதில் ஒரே பாராளுமன்றக் கட்டுப்பாடு சரத்து 352-க்கு மட்டுமே உண்டு, அங்கு மக்களவை தொடர்ச்சியை நிராகரித்து தீர்மானம் நிறைவேற்ற முடியும்."
    ))

    # 061 - Key B
    qs.append(make_ep_q(
        PREFIX, 61, "Hard", "Constitutional Amendment", "Article 360 Judicial Review History",
        "The 38th Constitutional Amendment Act, 1975 had made the President's satisfaction in declaring Financial Emergency final and non-justiciable. Which Amendment deleted this provision?",
        "1975-ன் 38-வது அரசியலமைப்பு திருத்தச் சட்டம் நிதி அவசரநிலையை அறிவிப்பதில் குடியரசுத் தலைவரின் திருப்தியை இறுதியானது மற்றும் நீதிமன்ற விசாரணைக்கு அப்பாற்பட்டது என ஆக்கியது. இந்த விதியை நீக்கிய திருத்தச் சட்டம் எது?",
        "42nd Constitutional Amendment Act, 1976", "42-வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
        "44th Constitutional Amendment Act, 1978", "44-வது அரசியலமைப்பு திருத்தச் சட்டம், 1978",
        "43rd Constitutional Amendment Act, 1977", "43-வது அரசியலமைப்பு திருத்தச் சட்டம், 1977",
        "52nd Constitutional Amendment Act, 1985", "52-வது அரசியலமைப்பு திருத்தச் சட்டம், 1985",
        "B",
        "The 44th Constitutional Amendment Act of 1978 deleted clause (5) of Article 360 (which had been inserted by the 38th CAA in 1975), thereby ensuring that the satisfaction of the President in proclaiming Financial Emergency is open to judicial review.",
        "1978-ன் 44-வது அரசியலமைப்பு திருத்தச் சட்டம் சரத்து 360-ன் பிரிவு (5)-ஐ (1975-ல் 38-வது திருத்தத்தால் சேர்க்கப்பட்டது) நீக்கியது; இதன் மூலம் நிதி அவசரநிலையைப் பிரகடனம் செய்வதில் குடியரசுத் தலைவரின் திருப்தி நீதித்துறை மறுஆய்வுக்கு உட்பட்டது என்பதை உறுதி செய்தது.",
        "Option A (42nd CAA) did not restore judicial review.", "விருப்பம் A நீதி மறுஆய்வை மீட்டெடுக்கவில்லை.",
        "Option B is correct; 44th CAA restored judicial review of Article 360.", "விருப்பம் B சரியானது; 44-வது திருத்தம் சரத்து 360-ன் நீதி மறுஆய்வை மீட்டெடுத்தது.",
        "Option C dealt with other aspects.", "விருப்பம் C பிற அம்சங்களைக் கையாண்டது.",
        "Option D is the Anti-Defection Law.", "விருப்பம் D கட்சித் தாவல் தடைச் சட்டம்.",
        "Unified Judicial Review: Post-44th CAA, ALL THREE emergencies (352, 356, and 360) are subject to judicial review for mala fide or irrelevant considerations.",
        "ஒருங்கிணைந்த நீதி மறுஆய்வு: 44-வது திருத்தத்திற்குப் பிறகு, மூன்று அவசரநிலைகளுமே (352, 356, 360) தவறான உள்நோக்கம் அல்லது தேவையற்ற காரணங்களுக்காக நீதி மறுஆய்வுக்கு உட்பட்டவை.",
        "Courts can examine whether the jurisdictional conditions precedent existed when the President declared satisfaction.",
        "குடியரசுத் தலைவர் திருப்தியடைந்ததாக அறிவித்த போது அதற்குரிய முன் நிபந்தனைகள் உண்மையில் இருந்தனவா என்பதை நீதிமன்றங்கள் ஆய்வு செய்ய முடியும்."
    ))

    # 062 - Key D
    qs.append(make_ep_q(
        PREFIX, 62, "Hard", "Constitutional Impact", "Financial Emergency Federal Impact",
        "During the operation of a Financial Emergency under Article 360, what is the impact on state financial autonomy?",
        "சரத்து 360-ன் கீழான நிதி அவசரநிலையின் போது, மாநிலங்களின் நிதி சுயாட்சியின் மீது ஏற்படும் தாக்கம் என்ன?",
        "State financial autonomy remains completely intact and undisturbed", "மாநில நிதி சுயாட்சி முற்றிலும் முழுமையாகவும் பாதிக்கப்படாமலும் நீடிக்கிறது",
        "State taxes are abolished and replaced by a single national sales tax", "மாநில வரிகள் ரத்து செய்யப்பட்டு ஒரே தேசிய விற்பனை வரியாக மாற்றப்படுகின்றன",
        "States are prohibited from spending any money without prior approval of the Supreme Court", "உச்ச நீதிமன்றத்தின் முன் அனுமதியின்றி மாநிலங்கள் எந்தப் பணத்தையும் செலவழிக்கத் தடை விதிக்கப்படுகிறது",
        "The Centre acquires complete financial subordination over states, directing financial propriety, reducing salaries, and reserving state money bills", "நிதி ஒழுங்குமுறையை வழிகாட்டுதல், ஊதியங்களைக் குறைத்தல் மற்றும் மாநில பண மசோதாக்களை ஒதுக்குதல் மூலம் மாநிலங்கள் மீது மத்திய அரசு முழுமையான நிதிக் கட்டுப்பாட்டைப் பெறுகிறது",
        "D",
        "During a Financial Emergency, the federal division of financial resources and powers is virtually suspended. The Union acquires total control over state financial management, directing cuts in salaries, prescribing canons of propriety, and requiring state money bills to be approved by the President.",
        "நிதி அவசரநிலையின் போது, நிதி ஆதாரங்கள் மற்றும் அதிகாரங்களின் கூட்டாட்சிப் பகிர்வு நடைமுறையில் இடைநிறுத்தப்படுகிறது. ஊதியக் குறைப்புகளை உத்தரவிடுதல், நிதி ஒழுங்குமுறைக் கோட்பாடுகளை நிர்ணயித்தல் மற்றும் மாநில பண மசோதாக்களைக் குடியரசுத் தலைவரின் ஒப்புதலுக்கு உட்படுத்துதல் மூலம் மாநில நிதி மேலாண்மையின் மீது மத்திய அரசு முழுமையான கட்டுப்பாட்டைப் பெறுகிறது.",
        "Option A is false; financial autonomy is severely curtailed.", "விருப்பம் A தவறு; நிதி சுயாட்சி கடுமையாகக் குறைக்கப்படுகிறது.",
        "Option B is false; tax systems are not abolished.", "விருப்பம் B தவறு; வரி முறைகள் ரத்து செய்யப்படுவதில்லை.",
        "Option C is false; Supreme Court does not manage financial budgets.", "விருப்பம் C தவறு; உச்ச நீதிமன்றம் பட்ஜெட்டை நிர்வகிப்பதில்லை.",
        "Option D is correct; comprehensive financial subordination of States to the Union.", "விருப்பம் D சரியானது; மத்திய அரசிடம் மாநிலங்கள் முழுமையாக நிதி ரீதியாக அடிபணியும் நிலை.",
        "Federal Impact: In normal times, states have independent financial spheres (State List taxes); in Financial Emergency, the Centre dictates state finances entirely.",
        "கூட்டாட்சித் தாக்கம்: இயல்பு காலத்தில் மாநிலங்களுக்குத் தனி நிதி அதிகாரம் உண்டு; நிதி அவசரநிலையில் மத்திய அரசே மாநில நிதியை முழுமையாக வழிநடத்துகிறது.",
        "Dr. B.R. Ambedkar defended this provision, stating that financial stability of the Union is indivisible from that of the States.",
        "மத்திய அரசின் நிதி நிலைத்தன்மை என்பது மாநிலங்களின் நிதி நிலைத்தன்மையிலிருந்து பிரிக்க முடியாதது என்று கூறி அம்பேத்கர் இந்த விதியை ஆதரித்தார்."
    ))

    # 063 - Key C
    qs.append(make_ep_q(
        PREFIX, 63, "Medium", "Comparative Matrix", "Parliamentary Approval Comparison",
        "Compare the parliamentary approval windows required for the three types of emergencies in India:",
        "இந்தியாவில் உள்ள மூன்று வகையான அவசரநிலைகளுக்கும் தேவையான பாராளுமன்ற ஒப்புதல் கால அவகாசங்களை ஒப்பிடுக:",
        "Article 352: 2 months; Article 356: 1 month; Article 360: 1 month", "சரத்து 352: 2 மாதங்கள்; சரத்து 356: 1 மாதம்; சரத்து 360: 1 மாதம்",
        "Article 352: 14 days; Article 356: 1 month; Article 360: 2 months", "சரத்து 352: 14 நாட்கள்; சரத்து 356: 1 மாதம்; சரத்து 360: 2 மாதங்கள்",
        "Article 352: 1 month; Article 356: 2 months; Article 360: 2 months", "சரத்து 352: 1 மாதம்; சரத்து 356: 2 மாதங்கள்; சரத்து 360: 2 மாதங்கள்",
        "Article 352: 6 months; Article 356: 6 months; Article 360: 6 months", "சரத்து 352: 6 மாதங்கள்; சரத்து 356: 6 மாதங்கள்; சரத்து 360: 6 மாதங்கள்",
        "C",
        "A proclamation of National Emergency (Article 352) must be approved within 1 month. A proclamation of President's Rule (Article 356) and Financial Emergency (Article 360) must both be approved within 2 months.",
        "தேசிய அவசரநிலைப் பிரகடனம் (சரத்து 352) 1 மாதத்திற்குள் அங்கீகரிக்கப்பட வேண்டும். குடியரசுத் தலைவர் ஆட்சி (சரத்து 356) மற்றும் நிதி அவசரநிலை (சரத்து 360) ஆகிய இரண்டு பிரகடனங்களும் 2 மாதங்களுக்குள் அங்கீகரிக்கப்பட வேண்டும்.",
        "Option A inverts the timeline for Article 352 and 356.", "விருப்பம் A சரத்து 352 மற்றும் 356-ன் கால அளவுகளை மாற்றுகிறது.",
        "Option B gives wrong periods.", "விருப்பம் B தவறான கால அளவுகளைத் தருகிறது.",
        "Option C is correct; 352 = 1 month; 356 = 2 months; 360 = 2 months.", "விருப்பம் C சரியானது; 352 = 1 மாதம்; 356 = 2 மாதங்கள்; 360 = 2 மாதங்கள்.",
        "Option D lists the renewal period, not initial approval.", "விருப்பம் D ஆரம்ப ஒப்புதலை விடுக்கிறது.",
        "TNPSC Comparison Matrix: Art 352 = 1 Month; Art 356 = 2 Months; Art 360 = 2 Months.",
        "TNPSC ஒப்பீட்டு அட்டவணை: சரத்து 352 = 1 மாதம்; சரத்து 356 = 2 மாதங்கள்; சரத்து 360 = 2 மாதங்கள்.",
        "Originally, all three were 2 months; the 44th Amendment Act 1978 reduced Article 352 to 1 month.",
        "முதலில் மூன்றுமே 2 மாதங்களாக இருந்தன; 1978-ன் 44-வது திருத்தச் சட்டம் சரத்து 352-ஐ 1 மாதமாகக் குறைத்தது."
    ))

    # 064 - Key A
    qs.append(make_ep_q(
        PREFIX, 64, "Medium", "Comparative Matrix", "Approval Majority Comparison",
        "Compare the parliamentary majority required to approve each of the three emergencies:",
        "மூன்று அவசரநிலைகளுக்கும் ஒப்புதல் அளிக்கத் தேவையான பாராளுமன்றப் பெரும்பான்மையை ஒப்பிடுக:",
        "Article 352: Special Majority; Article 356: Simple Majority; Article 360: Simple Majority", "சரத்து 352: சிறப்புப் பெரும்பான்மை; சரத்து 356: எளிய பெரும்பான்மை; சரத்து 360: எளிய பெரும்பான்மை",
        "Article 352: Simple Majority; Article 356: Special Majority; Article 360: Simple Majority", "சரத்து 352: எளிய பெரும்பான்மை; சரத்து 356: சிறப்புப் பெரும்பான்மை; சரத்து 360: எளிய பெரும்பான்மை",
        "Article 352: Special Majority; Article 356: Special Majority; Article 360: Special Majority", "சரத்து 352: சிறப்புப் பெரும்பான்மை; சரத்து 356: சிறப்புப் பெரும்பான்மை; சரத்து 360: சிறப்புப் பெரும்பான்மை",
        "Article 352: Absolute Majority; Article 356: Absolute Majority; Article 360: Absolute Majority", "சரத்து 352: முழுமையான பெரும்பான்மை; சரத்து 356: முழுமையான பெரும்பான்மை; சரத்து 360: முழுமையான பெரும்பான்மை",
        "A",
        "Approval of National Emergency (Article 352) requires a SPECIAL MAJORITY in each House (majority of total membership + 2/3 present & voting). Both President's Rule (Article 356) and Financial Emergency (Article 360) require only a SIMPLE MAJORITY in each House.",
        "தேசிய அவசரநிலைக்கு (சரத்து 352) ஒவ்வொரு அவையிலும் சிறப்புப் பெரும்பான்மை (மொத்தத்தில் பெரும்பான்மை + 2/3 வருகை பெரும்பான்மை) தேவை. குடியரசுத் தலைவர் ஆட்சி (சரத்து 356) மற்றும் நிதி அவசரநிலை (சரத்து 360) ஆகிய இரண்டிற்கும் ஒவ்வொரு அவையிலும் எளிய பெரும்பான்மை மட்டுமே தேவை.",
        "Option A is correct; 352 is the only emergency requiring a special majority.", "விருப்பம் A சரியானது; சிறப்புப் பெரும்பான்மை தேவைப்படும் ஒரே அவசரநிலை சரத்து 352 மட்டுமே.",
        "Option B inverts 352 and 356.", "விருப்பம் B 352 மற்றும் 356-ஐ மாற்றுகிறது.",
        "Option C claims all three need special majority.", "விருப்பம் C மூன்றுக்கும் சிறப்புப் பெரும்பான்மை தேவை எனக் கூறுகிறது.",
        "Option D is factually incorrect.", "விருப்பம் D தவறானது.",
        "TNPSC High-Yield Rule: Special Majority = Article 352 ONLY; Simple Majority = Articles 356 and 360.",
        "TNPSC உயர்-விளைச்சல் விதி: சிறப்புப் பெரும்பான்மை = சரத்து 352 மட்டுமே; எளிய பெரும்பான்மை = சரத்துகள் 356 மற்றும் 360.",
        "The special majority for Article 352 was introduced by the 44th Constitutional Amendment Act 1978.",
        "சரத்து 352-க்கான சிறப்புப் பெரும்பான்மை 1978-ன் 44-வது அரசியலமைப்பு திருத்தச் சட்டத்தால் கொண்டுவரப்பட்டது."
    ))

    # 065 - Key B
    qs.append(make_ep_q(
        PREFIX, 65, "Hard", "Comparative Matrix", "Periodic Renewal Comparison",
        "Compare the periodic parliamentary renewal requirements for the three emergency types:",
        "மூன்று அவசரநிலை வகைகளுக்கான காலமுறை பாராளுமன்றப் புதுப்பித்தல் தேவைகளை ஒப்பிடுக:",
        "All three require parliamentary approval every six months indefinitely", "மூன்றுக்குமே ஒவ்வொரு ஆறு மாதங்களுக்கும் காலவரையின்றி பாராளுமன்ற ஒப்புதல் தேவை",
        "Article 352: Every 6 months indefinitely; Article 356: Every 6 months up to max 3 years; Article 360: NO periodic renewal required", "சரத்து 352: ஒவ்வொரு 6 மாதங்களுக்கும் காலவரையின்றி; சரத்து 356: அதிகபட்சம் 3 ஆண்டுகள் வரை ஒவ்வொரு 6 மாதங்களுக்கும்; சரத்து 360: காலமுறைப் புதுப்பித்தல் தேவையில்லை",
        "Article 352: Every 1 year; Article 356: Every 6 months; Article 360: Every 3 years", "சரத்து 352: ஒவ்வொரு 1 ஆண்டும்; சரத்து 356: ஒவ்வொரு 6 மாதமும்; சரத்து 360: ஒவ்வொரு 3 ஆண்டும்",
        "None of the three emergencies require periodic renewal once approved", "ஒருமுறை ஒப்புதல் பெற்ற பிறகு மூன்று அவசரநிலைகளுக்கும் காலமுறைப் புதுப்பித்தல் தேவையில்லை",
        "B",
        "Article 352 can continue indefinitely with parliamentary approval every 6 months. Article 356 can continue with approval every 6 months up to a maximum ceiling of 3 years. Article 360 continues indefinitely without requiring any repeated parliamentary renewal.",
        "சரத்து 352 ஒவ்வொரு 6 மாதங்களுக்கும் பாராளுமன்ற ஒப்புதலுடன் காலவரையின்றித் தொடரலாம். சரத்து 356 அதிகபட்சமாக 3 ஆண்டுகள் வரை ஒவ்வொரு 6 மாதங்களுக்கும் ஒப்புதலுடன் தொடரலாம். சரத்து 360 எவ்வித தொடர் பாராளுமன்ற ஒப்புதலும் இன்றி காலவரையின்றித் தொடர்கிறது.",
        "Option A overlooks the 3-year limit on 356 and the non-renewal nature of 360.", "விருப்பம் A சரத்து 356-ன் 3 ஆண்டு வரம்பையும் சரத்து 360-ன் தன்மையையும் புறக்கணிக்கிறது.",
        "Option B is correct; captures the precise duration and renewal regime of each emergency.", "விருப்பம் B சரியானது; ஒவ்வொரு அவசரநிலையின் துல்லியமான கால அளவு மற்றும் புதுப்பித்தல் முறையைப் படம்பிடிக்கிறது.",
        "Option C gives incorrect intervals.", "விருப்பம் C தவறான கால இடைவெளிகளைத் தருகிறது.",
        "Option D describes pre-1978 position for Article 352.", "விருப்பம் D 1978-க்கு முந்தைய சரத்து 352 நிலையைக் குறிப்பிடுகிறது.",
        "Renewal Matrix: Art 352 = Every 6 months (indefinite); Art 356 = Every 6 months (max 3 yrs); Art 360 = No renewal (indefinite).",
        "புதுப்பித்தல் அட்டவணை: சரத்து 352 = ஒவ்வொரு 6 மாதமும் (முடிவின்றி); சரத்து 356 = ஒவ்வொரு 6 மாதமும் (அதிகபட்சம் 3 ஆண்டுகள்); சரத்து 360 = புதுப்பித்தல் இல்லை (முடிவின்றி).",
        "Article 360 has no provision for repeated approval because financial emergencies are expected to continue until market stability is restored and executive revokes it.",
        "சந்தை நிலைத்தன்மை மீட்டெடுக்கப்பட்டு நிர்வாகம் அதை ரத்து செய்யும் வரை நிதி அவசரநிலை தொடரும் என்று எதிர்பார்க்கப்படுவதால் அதற்கு மீண்டும் மீண்டும் ஒப்புதல் தேவைப்படுவதில்லை."
    ))

    # 066 - Key D
    qs.append(make_ep_q(
        PREFIX, 66, "Hard", "Comparative Matrix", "Impact on Fundamental Rights Comparison",
        "Compare the constitutional impact of the three types of emergencies on citizens' Fundamental Rights:",
        "குடிமக்களின் அடிப்படை உரிமைகள் மீது மூன்று வகையான அவசரநிலைகள் ஏற்படுத்தும் அரசியலமைப்புத் தாக்கத்தை ஒப்பிடுக:",
        "All three emergencies suspend all Fundamental Rights under Part III", "மூன்று அவசரநிலைகளுமே பகுதி III-ல் உள்ள அனைத்து அடிப்படை உரிமைகளையும் இடைநிறுத்துகின்றன",
        "Article 356 suspends Fundamental Rights, while Articles 352 and 360 do not", "சரத்து 356 அடிப்படை உரிமைகளை இடைநிறுத்துகிறது, ஆனால் சரத்துகள் 352 மற்றும் 360 இடைநிறுத்துவதில்லை",
        "Articles 352 and 360 suspend Article 19, while Article 356 suspends Article 21", "சரத்துகள் 352 மற்றும் 360 சரத்து 19-ஐ இடைநிறுத்துகின்றன, ஆனால் சரத்து 356 சரத்து 21-ஐ இடைநிறுத்துகிறது",
        "Article 352 can suspend Article 19 and enforcement of specified rights (except 20 & 21); Articles 356 and 360 have ZERO impact on Fundamental Rights", "சரத்து 352 சரத்து 19 மற்றும் குறிப்பிட்ட உரிமைகளைச் செயல்படுத்துவதை இடைநிறுத்தலாம் (20, 21 தவிர); சரத்துகள் 356 மற்றும் 360 அடிப்படை உரிமைகள் மீது எந்தவொரு தாக்கத்தையும் ஏற்படுத்துவதில்லை",
        "D",
        "National Emergency (Article 352) is the ONLY emergency that impacts Fundamental Rights (under Articles 358 and 359). Neither President's Rule (Article 356) nor Financial Emergency (Article 360) has any effect on Fundamental Rights whatsoever.",
        "தேசிய அவசரநிலை (சரத்து 352) மட்டுமே அடிப்படை உரிமைகள் மீது தாக்கத்தை ஏற்படுத்தும் ஒரே அவசரநிலையாகும் (சரத்துகள் 358 மற்றும் 359-ன் கீழ்). குடியரசுத் தலைவர் ஆட்சி (சரத்து 356) மற்றும் நிதி அவசரநிலை (சரத்து 360) ஆகிய இரண்டும் அடிப்படை உரிமைகள் மீது எந்தவொரு தாக்கத்தையும் ஏற்படுத்துவதில்லை.",
        "Option A is a major error.", "விருப்பம் A பெரிய பிழையாகும்.",
        "Option B inverts the impact.", "விருப்பம் B தாக்கத்தைத் தலைகீழாக மாற்றுகிறது.",
        "Option C contains multiple factual errors; Article 21 can never be suspended.", "விருப்பம் C பல பிழைகளைக் கொண்டுள்ளது; சரத்து 21 ஒருபோதும் இடைநிறுத்தப்பட முடியாது.",
        "Option D is correct; ONLY Article 352 touches Fundamental Rights.", "விருப்பம் D சரியானது; சரத்து 352 மட்டுமே அடிப்படை உரிமைகளைத் தொடுகிறது.",
        "TNPSC Golden Distinction: Fundamental Rights impact: Article 352 = YES (via Arts 358/359); Article 356 = NO; Article 360 = NO.",
        "TNPSC பொன் வேறுபாடு: அடிப்படை உரிமைகள் மீதான தாக்கம்: சரத்து 352 = உண்டு (358/359 வழியாக); சரத்து 356 = இல்லை; சரத்து 360 = இல்லை.",
        "During President's Rule or Financial Emergency, citizens retain full recourse to courts under Article 32 and Article 226 for all fundamental rights.",
        "குடியரசுத் தலைவர் ஆட்சி அல்லது நிதி அவசரநிலையின் போது, அனைத்து அடிப்படை உரிமைகளுக்காகவும் சரத்து 32 மற்றும் 226-ன் கீழ் நீதிமன்றங்களை நாடும் முழு உரிமையை குடிமக்கள் தக்கவைத்துக்கொள்கின்றனர்."
    ))

    # 067 - Key C
    qs.append(make_ep_q(
        PREFIX, 67, "Hard", "Comparative Matrix", "State Executive Status Comparison",
        "Compare the constitutional status of the State Government (Council of Ministers) under Article 352 and Article 356:",
        "சரத்து 352 மற்றும் சரத்து 356-ன் கீழ் மாநில அரசின் (அமைச்சரவை) அரசியலமைப்பு நிலையை ஒப்பிடுக:",
        "Under both Article 352 and 356, the State Ministry is dismissed immediately", "சரத்து 352 மற்றும் 356 ஆகிய இரண்டின் கீழும் மாநில அமைச்சரவை உடனடியாகப் பதவி நீக்கம் செய்யப்படுகிறது",
        "Under both Article 352 and 356, the State Ministry continues with full autonomous powers", "சரத்து 352 மற்றும் 356 இரண்டிலும் மாநில அமைச்சரவை முழு சுயாட்சி அதிகாரங்களுடன் தொடர்கிறது",
        "Under Article 352, the State Ministry continues to function under Union executive directions; under Article 356, the State Ministry is dismissed and its powers are assumed by the President", "சரத்து 352-ன் கீழ், மாநில அமைச்சரவை மத்திய அரசின் நிர்வாக வழிகாட்டுதலின் கீழ் தொடர்ந்து செயல்படுகிறது; சரத்து 356-ன் கீழ், மாநில அமைச்சரவை பதவி நீக்கம் செய்யப்பட்டு அதன் அதிகாரங்கள் குடியரசுத் தலைவரால் ஏற்றுக்கொள்ளப்படுகின்றன",
        "Under Article 352, the Chief Minister is dismissed, but cabinet ministers continue", "சரத்து 352-ன் கீழ் முதலமைச்சர் பதவி நீக்கம் செய்யப்படுகிறார், ஆனால் அமைச்சர்கள் தொடர்கின்றனர்",
        "C",
        "Under Article 352, the State Ministry continues to function, although the Union acquires the power to issue binding directions on any matter. Under Article 356, the State Ministry is dismissed, and the President assumes all functions of the State Government.",
        "சரத்து 352-ன் கீழ், எந்தவொரு விவகாரத்திலும் வழிகாட்டும் அதிகாரத்தை மத்திய அரசு பெற்றாலும் மாநில அமைச்சரவை தொடர்ந்து செயல்படுகிறது. சரத்து 356-ன் கீழ், மாநில அமைச்சரவை பதவி நீக்கம் செய்யப்பட்டு, மாநில அரசின் அனைத்து செயல்பாடுகளையும் குடியரசுத் தலைவர் தன்வசம் ஏற்றுக்கொள்கிறார்.",
        "Option A wrongly claims ministry is dismissed under Article 352.", "விருப்பம் A சரத்து 352-ல் அமைச்சரவை கலைக்கப்படுகிறது எனத் தவறாகக் கூறுகிறது.",
        "Option B overlooks Union overriding powers.", "விருப்பம் B மத்திய அரசின் மேலோங்கும் அதிகாரங்களைப் புறக்கணிக்கிறது.",
        "Option C is correct; continuous under directions (352) vs dismissed and assumed (356).", "விருப்பம் C சரியானது; வழிகாட்டுதலின் கீழ் நீடித்தல் (352) vs கலைக்கப்பட்டு ஏற்றுக்கொள்ளப்படுதல் (356).",
        "Option D has no basis in constitutional law.", "விருப்பம் D அரசியலமைப்புச் சட்டத்தில் இல்லாதது.",
        "Executive Contrast: Article 352 subordinates the state executive; Article 356 replaces the state executive.",
        "நிர்வாக ஒப்பீடு: சரத்து 352 மாநில நிர்வாகத்தைக் கட்டுப்படுத்துகிறது; சரத்து 356 மாநில நிர்வாகத்தை இடமாற்றம் செய்கிறது.",
        "Under Article 356, the Governor administers the state on behalf of the President, assisted by advisors.",
        "சரத்து 356-ன் கீழ், ஆலோசகர்களின் உதவியுடன் குடியரசுத் தலைவரின் சார்பில் ஆளுநர் மாநிலத்தை நிர்வகிக்கிறார்."
    ))

    # 068 - Key A
    qs.append(make_ep_q(
        PREFIX, 68, "Hard", "Comparative Matrix", "State Legislative Assembly Status Comparison",
        "Compare the constitutional status of the State Legislative Assembly under Article 352 and Article 356:",
        "சரத்து 352 மற்றும் சரத்து 356-ன் கீழ் மாநில சட்டமன்றத்தின் அரசியலமைப்பு நிலையை ஒப்பிடுக:",
        "Under Article 352, the Assembly continues to make laws concurrently; under Article 356, the Assembly is suspended or dissolved and Parliament makes laws for the State", "சரத்து 352-ன் கீழ், சட்டமன்றம் பாராளுமன்றத்துடன் இணைந்து தொடர்ந்து சட்டம் இயற்றுகிறது; சரத்து 356-ன் கீழ், சட்டமன்றம் இடைநிறுத்தப்படுகிறது அல்லது கலைக்கப்படுகிறது மற்றும் பாராளுமன்றம் மாநிலத்திற்கான சட்டங்களை இயற்றுகிறது",
        "Under Article 352, the Assembly is dissolved; under Article 356, the Assembly continues normally", "சரத்து 352-ன் கீழ் சட்டமன்றம் கலைக்கப்படுகிறது; சரத்து 356-ன் கீழ் சட்டமன்றம் சாதாரணமாகத் தொடர்கிறது",
        "Under both Article 352 and Article 356, the Assembly is permanently abolished", "சரத்து 352 மற்றும் 356 ஆகிய இரண்டின் கீழும் சட்டமன்றம் நிரந்தரமாக ஒழிக்கப்படுகிறது",
        "Under both Article 352 and Article 356, the Assembly's strength is reduced by half", "சரத்து 352 மற்றும் 356 இரண்டிலும் சட்டமன்ற உறுப்பினர்களின் எண்ணிக்கை பாதியாகக் குறைக்கப்படுகிறது",
        "A",
        "Under Article 352, the State Legislature is NOT suspended; it continues to enact laws, while Parliament gets concurrent overriding power under Article 250. Under Article 356, the State Legislature's powers are declared exercisable by Parliament, and the Assembly is initially suspended and later may be dissolved.",
        "சரத்து 352-ன் கீழ், மாநில சட்டமன்றம் இடைநிறுத்தப்படுவதில்லை; அது தொடர்ந்து சட்டங்களை இயற்றுகிறது, அதே சமயம் சரத்து 250-ன் கீழ் பாராளுமன்றம் மேலோங்கும் இணை அதிகாரத்தைப் பெறுகிறது. சரத்து 356-ன் கீழ், மாநில சட்டமன்ற அதிகாரங்களைப் பாராளுமன்றம் செயல்படுத்துகிறது, மேலும் சட்டமன்றம் இடைநிறுத்தப்படுகிறது அல்லது கலைக்கப்படுகிறது.",
        "Option A is correct; exact operational distinction regarding legislative power.", "விருப்பம் A சரியானது; சட்டமன்ற அதிகாரம் குறித்த துல்லியமான செயல்பாட்டு வேறுபாடு.",
        "Option B inverts the status of the two assemblies.", "விருப்பம் B இரண்டு அவைகளின் நிலையை மாற்றுகிறது.",
        "Option C is incorrect because assemblies are not abolished.", "விருப்பம் C தவறு, ஏனெனில் சட்டமன்றங்கள் ஒழிக்கப்படுவதில்லை.",
        "Option D is incorrect because assembly strength is unchanged.", "விருப்பம் D தவறு, ஏனெனில் சட்டமன்ற பலம் மாற்றப்படுவதில்லை.",
        "Legislative Matrix: Article 352 = Concurrent powers (Parliament overrides under Art 251); Article 356 = Exclusive Parliamentary exercise (delegated under Art 357).",
        "சட்டமன்ற அட்டவணை: சரத்து 352 = இணை அதிகாரம் (சரத்து 251-ல் பாராளுமன்றம் மேலோங்கும்); சரத்து 356 = பிரத்தியேக பாராளுமன்ற அதிகாரம் (சரத்து 357-ல் வழங்கப்படுகிறது).",
        "During National Emergency, the tenure of the State Legislative Assembly can also be extended by Parliament by law for one year at a time under Article 172(1) proviso.",
        "தேசிய அவசரநிலையின் போது, சரத்து 172(1) வரம்புரையின் கீழ் பாராளுமன்றம் சட்டத்தின் மூலம் மாநில சட்டமன்றத்தின் பதவிக்காலத்தையும் ஒரு முறைக்கு ஓராண்டு வரை நீட்டிக்க முடியும்."
    ))

    # 069 - Key B
    qs.append(make_ep_q(
        PREFIX, 69, "Medium", "Constituent Assembly Debates", "Prof. K.T. Shah Critique",
        "In the Constituent Assembly debates, which prominent member described the Emergency Provisions as a 'chapter of reaction and retrogression'?",
        "அரசியலமைப்பு நிர்ணய சபை விவாதங்களில், அவசரநிலைப் பிரிவுகளை 'பிற்போக்குத்தனமான மற்றும் பின்னடைவுக்கான அத்தியாயம்' என்று விவரித்த முக்கிய உறுப்பினர் யார்?",
        "Dr. B.R. Ambedkar", "டாக்டர் பி.ஆர். அம்பேத்கர்",
        "Prof. K.T. Shah", "பேராசிரியர் கே.டி. ஷா",
        "Sardar Vallabhbhai Patel", "சர்தார் வல்லபாய் படேல்",
        "Jawaharlal Nehru", "ஜவஹர்லால் நேரு",
        "B",
        "Prof. K.T. Shah vigorously opposed the Emergency Provisions in the Constituent Assembly, characterizing them as a 'chapter of reaction and retrogression' that gave the executive excessive powers capable of suppressing constitutional democracy.",
        "பேராசிரியர் கே.டி. ஷா அரசியலமைப்பு நிர்ணய சபையில் அவசரநிலைப் பிரிவுகளைக் கடுமையாக எதிர்த்தார்; நிர்வாகத்திற்கு மிதமிஞ்சிய அதிகாரங்களை வழங்கி அரசியலமைப்பு ஜனநாயகத்தை ஒடுக்கும் திறன் கொண்ட ஒரு 'பிற்போக்குத்தனமான மற்றும் பின்னடைவுக்கான அத்தியாயம்' என்று அவற்றை வர்ணித்தார்.",
        "Option A defended the provisions as necessary safety valves.", "விருப்பம் A இப்பிரிவுகளைத் தேவையான பாதுகாப்பு வால்வுகள் என ஆதரித்தது.",
        "Option B is correct; Prof. K.T. Shah made this famous critical remark.", "விருப்பம் B சரியானது; பேராசிரியர் கே.டி. ஷா இந்த வரலாற்று விமர்சனத்தை முன்வைத்தார்.",
        "Option C was a key architect of the Union framework.", "விருப்பம் C மத்திய அமைப்பின் முக்கிய சிற்பியாவார்.",
        "Option D supported strong central powers.", "விருப்பம் D வலுவான மத்திய அதிகாரங்களை ஆதரித்தார்.",
        "CAD Famous Quote: Prof. K.T. Shah: 'This is a chapter of reaction and retrogression... It treats the people of India as children or criminals.'",
        "CAD புகழ்பெற்ற கூற்று: பேராசிரியர் கே.டி. ஷா: 'இது பிற்போக்குத்தனமான மற்றும் பின்னடைவுக்கான ஒரு அத்தியாயம்... இது இந்திய மக்களைக் குழந்தைகளாக அல்லது குற்றவாளிகளாக நடத்துகிறது.'",
        "Despite such criticisms, the drafting committee retained the provisions, viewing them as essential to protect national security against centrifugal forces.",
        "இத்தகைய விமர்சனங்கள் இருந்தபோதிலும், பிரிவினை சக்திகளிடமிருந்து தேசியப் பாதுகாப்பைப் பாதுகாக்க இவை அவசியம் எனக் கருதி வரைவுக்குழு இப்பிரிவுகளைத் தக்கவைத்துக் கொண்டது."
    ))

    # 070 - Key D
    qs.append(make_ep_q(
        PREFIX, 70, "Medium", "Constituent Assembly Debates", "H.V. Kamath Warning",
        "In the Constituent Assembly debates, who issued the famous warning: 'I fear that by this single chapter we are seeking to lay the foundation of a totalitarian state'?",
        "அரசியலமைப்பு நிர்ணய சபை விவாதங்களில், 'இந்த ஒற்றை அத்தியாயத்தின் மூலம் நாம் ஒரு சர்வாதிகார அரசிற்கு அடித்தளம் அமைக்க முனைகிறோமோ என்று நான் அஞ்சுகிறேன்' என்று புகழ்பெற்ற எச்சரிக்கையை விடுத்தவர் யார்?",
        "Dr. Rajendra Prasad", "டாக்டர் ராஜேந்திர பிரசாத்",
        "Alladi Krishnaswami Iyer", "அல்லாடி கிருஷ்ணசுவாமி அய்யர்",
        "K.M. Munshi", "கே.எம். முன்ஷி",
        "H.V. Kamath", "எச்.வி. காமத்",
        "D",
        "H.V. Kamath issued this prophetic warning in the Constituent Assembly, fearing that Part XVIII would be weaponized by future executive governments to dismantle civil liberties and federalism, laying the foundation of a totalitarian police state.",
        "எச்.வி. காமத் அரசியலமைப்பு நிர்ணய சபையில் இந்த தீர்க்கதரிசன எச்சரிக்கையை விடுத்தார்; பகுதி XVIII எதிர்கால நிர்வாக அரசுகளால் குடிமை உரிமைகள் மற்றும் கூட்டாட்சியைச் சிதைக்கப் பயன்படுத்தப்பட்டு, ஒரு சர்வாதிகார காவல்துறை அரசுக்கு அடித்தளமிட்டுவிடுமோ என்று அவர் அஞ்சினார்.",
        "Option A was the President of the Constituent Assembly.", "விருப்பம் A நிர்ணய சபையின் தலைவராக இருந்தார்.",
        "Option B defended the emergency provisions.", "விருப்பம் B அவசரநிலைப் பிரிவுகளை ஆதரித்துப் பேசினார்.",
        "Option C was on the Drafting Committee and defended Part XVIII.", "விருப்பம் C வரைவுக் குழுவில் இருந்து பகுதி XVIII-ஐ ஆதரித்தார்.",
        "Option D is correct; H.V. Kamath delivered this celebrated warning.", "விருப்பம் D சரியானது; எச்.வி. காமத் இந்த வரலாற்று எச்சரிக்கையை விடுத்தார்.",
        "CAD Historic Warning: H.V. Kamath warned of the rise of a 'totalitarian state' or 'police raj' through Part XVIII.",
        "CAD வரலாற்று எச்சரிக்கை: பகுதி XVIII மூலம் ஒரு 'சர்வாதிகார அரசு' அல்லது 'காவல்துறை ராஜ்ஜியம்' உருவாகும் என்று எச்.வி. காமத் எச்சரித்தார்.",
        "The events of the 1975–1977 Emergency proved that Kamath's fears were remarkably farsighted.",
        "1975-1977 அவசரநிலை நிகழ்வுகள் காமத்தின் அச்சங்கள் வியக்கத்தக்க தொலைநோக்குப் பார்வை கொண்டவை என்பதை நிரூபித்தன."
    ))

    # 071 - Key C
    qs.append(make_ep_q(
        PREFIX, 71, "Medium", "Constituent Assembly Debates", "T.T. Krishnamachari Defense",
        "In the Constituent Assembly, who defended the Emergency Provisions by arguing that without them, the Constitution could not survive against extraordinary threats to national security?",
        "அரசியலமைப்பு நிர்ணய சபையில், அவசரநிலைப் பிரிவுகள் இல்லாவிட்டால் தேசியப் பாதுகாப்பிற்கு ஏற்படும் அசாதாரண அச்சுறுத்தல்களை எதிர்த்து அரசியலமைப்பு நீடிக்க முடியாது என்று வாதிட்டு அவற்றை ஆதரித்தவர் யார்?",
        "Dr. B.R. Ambedkar and Jawaharlal Nehru", "டாக்டர் பி.ஆர். அம்பேத்கர் மற்றும் ஜவஹர்லால் நேரு",
        "Shibban Lal Saksena and K.T. Shah", "சிபன் லால் சக்சேனா மற்றும் கே.டி. ஷா",
        "T.T. Krishnamachari and Alladi Krishnaswami Iyer", "டி.டி. கிருஷ்ணமாச்சாரி மற்றும் அல்லாடி கிருஷ்ணசுவாமி அய்யர்",
        "Jayaprakash Narayan and Acharya Kripalani", "ஜெயபிரகாஷ் நாராயண் மற்றும் ஆச்சார்யா கிருபளானி",
        "C",
        "T.T. Krishnamachari and Sir Alladi Krishnaswami Iyer strongly defended the emergency provisions in the Constituent Assembly. Alladi observed that the very life of the State was at stake during an emergency, and individual freedom must yield to the preservation of the State.",
        "டி.டி. கிருஷ்ணமாச்சாரி மற்றும் சர் அல்லாடி கிருஷ்ணசுவாமி அய்யர் ஆகியோர் அரசியலமைப்பு நிர்ணய சபையில் அவசரநிலைப் பிரிவுகளை மிக உறுதியாக ஆதரித்தனர். அவசரநிலையின் போது நாட்டின் இருப்புக்கே அச்சுறுத்தல் ஏற்படுகிறது என்றும், நாட்டின் பாதுகாப்பிற்காக தனிநபர் சுதந்திரம் வழிவிட வேண்டும் என்றும் அல்லாடி குறிப்பிட்டார்.",
        "Option A were leaders, but the primary speeches on safety valves were made by Krishnamachari and Alladi.", "விருப்பம் A தலைவர்கள், ஆனால் முதன்மை வாதங்களை கிருஷ்ணமாச்சாரியும் அல்லாடியும் முன்வைத்தனர்.",
        "Option B were fierce critics, not defenders.", "விருப்பம் B கடுமையான விமர்சகர்கள், ஆதரவாளர்கள் அல்ல.",
        "Option C is correct; T.T. Krishnamachari and Alladi Krishnaswami Iyer.", "விருப்பம் C சரியானது; டி.டி. கிருஷ்ணமாச்சாரி மற்றும் அல்லாடி கிருஷ்ணசுவாமி அய்யர்.",
        "Option D were socialist leaders outside the drafting core.", "விருப்பம் D சோசலிசத் தலைவர்கள்.",
        "CAD Defense: Alladi Krishnaswami Iyer remarked that emergency provisions were the 'very life of the Constitution' to save democracy from destruction.",
        "CAD ஆதரவு: ஜனநாயகத்தை அழிவிலிருந்து காப்பாற்றுவதற்கான 'அரசியலமைப்பின் உயிரே' அவசரநிலைப் பிரிவுகள் என்று அல்லாடி கிருஷ்ணசுவாமி அய்யர் குறிப்பிட்டார்.",
        "T.T. Krishnamachari pointed out that individual liberties exist only so long as the State itself survives.",
        "நாடு நீடித்திருக்கும் வரை மட்டுமே தனிநபர் சுதந்திரங்கள் நீடிக்க முடியும் என்று டி.டி. கிருஷ்ணமாச்சாரி சுட்டிக்காட்டினார்."
    ))

    # 072 - Key A
    qs.append(make_ep_q(
        PREFIX, 72, "Hard", "Constituent Assembly Debates", "Dr. Ambedkar's Response to Misuse Fears",
        "How did Dr. B.R. Ambedkar respond in the Constituent Assembly to the criticism that the Emergency Provisions could be abused by future rulers?",
        "எதிர்கால ஆட்சியாளர்களால் அவசரநிலைப் பிரிவுகள் தவறாகப் பயன்படுத்தப்படலாம் என்ற விமர்சனத்திற்கு அரசியலமைப்பு நிர்ணய சபையில் டாக்டர் அம்பேத்கர் எவ்வாறு பதிலளித்தார்?",
        "He conceded that the possibility of abuse of power cannot be an argument for the non-conferment of power, and hoped Article 356 would remain a dead letter", "அதிகாரம் தவறாகப் பயன்படுத்தப்படலாம் என்ற சாத்தியக்கூறு அதிகாரத்தை வழங்காமல் இருப்பதற்கான வாதமாக அமைய முடியாது என்பதை ஒப்புக்கொண்டார், மேலும் சரத்து 356 ஒரு செயலற்ற எழுத்தாக இருக்கும் என நம்பினார்",
        "He assured that the Supreme Court would automatically strike down any emergency within 24 hours", "24 மணி நேரத்திற்குள் எந்தவொரு அவசரநிலையையும் உச்ச நீதிமன்றம் தானாகவே ரத்து செய்துவிடும் என்று உறுதியளித்தார்",
        "He agreed to remove Article 356 altogether before the third reading", "மூன்றாவது வாசிப்பிற்கு முன்பாக சரத்து 356-ஐ முற்றிலும் நீக்க அவர் ஒப்புக்கொண்டார்",
        "He stated that emergency provisions would expire automatically after 10 years", "10 ஆண்டுகளுக்குப் பிறகு அவசரநிலைப் பிரிவுகள் தானாகவே காலாவதியாகிவிடும் என்று கூறினார்",
        "A",
        "Dr. B.R. Ambedkar delivered two classic answers: First, on the fear of misuse, he stated that 'the possibility of abuse of power is no argument against its conferment'. Second, on Article 356, he famously expressed the hope that 'such articles will never be called into operation and that they would remain a dead letter'.",
        "டாக்டர் அம்பேத்கர் இரண்டு வரலாற்றுச் சிறப்புமிக்க பதில்களை அளித்தார்: முதலாவதாக, தவறான பயன்பாடு குறித்த அச்சத்திற்கு, 'அதிகாரம் தவறாகப் பயன்படுத்தப்படலாம் என்பது அதிகாரத்தை வழங்காமல் இருப்பதற்கான வாதமாகாது' என்றார். இரண்டாவதாக, சரத்து 356 குறித்து, 'இத்தகைய விதிகள் ஒருபோதும் பயன்பாட்டிற்கு வராமல் அவை ஒரு செயலற்ற எழுத்தாகவே (dead letter) இருக்கும்' என்று நம்புவதாகக் கூறினார்.",
        "Option A is correct; captures Ambedkar's twin famous defenses in the CAD.", "விருப்பம் A சரியானது; நிர்ணய சபையில் அம்பேத்கரின் இரண்டு புகழ்பெற்ற வாதங்களைப் படம்பிடிக்கிறது.",
        "Option B is false; no 24-hour court rule existed.", "விருப்பம் B தவறு; 24 மணி நேர நீதிமன்ற விதி எதுவும் இல்லை.",
        "Option C is false; Article 356 was retained.", "விருப்பம் C தவறு; சரத்து 356 தக்கவைக்கப்பட்டது.",
        "Option D is false; emergency provisions have no sunset clause.", "விருப்பம் D தவறு; அவசரநிலைப் பிரிவுகளுக்கு காலாவதி தேதி இல்லை.",
        "CAD Historic Landmark: Ambedkar: 'I hope that they would remain a dead letter... and will be used only as a last resort.'",
        "CAD வரலாற்று மைல்கல்: அம்பேத்கர்: 'அவை ஒரு செயலற்ற எழுத்தாகவே இருக்கும்... மேலும் இறுதி நடவடிக்கையாக மட்டுமே பயன்படுத்தப்படும் என்று நான் நம்புகிறேன்.'",
        "Regrettably, subsequent Indian political history saw Article 356 invoked more than 125 times, contradicting Ambedkar's noble hope.",
        "துரதிர்ஷ்டவசமாக, சுதந்திரத்திற்குப் பிந்தைய இந்திய அரசியல் வரலாறு சரத்து 356-ஐ 125-க்கும் மேற்பட்ட முறை பயன்படுத்தி, அம்பேத்கரின் உன்னத நம்பிக்கைக்கு முரணாக அமைந்தது."
    ))

    # 073 - Key B
    qs.append(make_ep_q(
        PREFIX, 73, "Hard", "Sarkaria Commission", "Publication of Governor's Report",
        "What specific recommendation did the Sarkaria Commission (1988) make regarding the Governor's report recommending President's Rule?",
        "குடியரசுத் தலைவர் ஆட்சியைப் பரிந்துரைக்கும் ஆளுநரின் அறிக்கை தொடர்பாக சர்க்காரியா ஆணையம் (1988) என்ன குறிப்பிட்ட பரிந்துரையைச் செய்தது?",
        "It should be kept strictly confidential as an official secret", "அது அரசு ரகசியமாக கடுமையான ரகசியத்தன்மையுடன் வைக்கப்பட வேண்டும்",
        "The Governor's report should be a speaking document containing precise facts, and should be given wide publicity and laid before Parliament", "ஆளுநரின் அறிக்கை துல்லியமான உண்மைகளைக் கொண்ட ஒரு பேசும் ஆவணமாக (speaking document) இருக்க வேண்டும், மேலும் அதற்கு பரந்த விளம்பரம் அளிக்கப்பட்டு பாராளுமன்றத்தின் முன் வைக்கப்பட வேண்டும்",
        "It should be submitted directly to the President without showing it to the Prime Minister", "பிரதமருக்குக் காட்டாமல் குடியரசுத் தலைவரிடம் நேரடியாக சமர்ப்பிக்கப்பட வேண்டும்",
        "It must be co-signed by the Leader of the Opposition in the State Assembly", "மாநில சட்டமன்ற எதிர்க்கட்சித் தலைவர் அதில் கட்டாயம் இணைந்து கையொப்பமிட வேண்டும்",
        "B",
        "The Sarkaria Commission recommended that the Governor's report under Article 356 must be a 'speaking document' containing a clear, objective narration of facts and circumstances that justify the breakdown. Furthermore, it recommended that the report should be given wide publicity so that the public and Parliament can scrutinize its objective basis.",
        "சரத்து 356-ன் கீழான ஆளுநரின் அறிக்கை, நிர்வாக முறிவை நியாயப்படுத்தும் உண்மைகள் மற்றும் சூழ்நிலைகளின் தெளிவான, புறநிலை விளக்கத்தைக் கொண்ட ஒரு 'பேசும் ஆவணமாக' (speaking document) இருக்க வேண்டும் என்று சர்க்காரியா ஆணையம் பரிந்துரைத்தது. மேலும், பொதுமக்களும் பாராளுமன்றமும் அதன் உண்மைத்தன்மையை ஆய்வு செய்ய ஏதுவாக அதற்கு பரந்த விளம்பரம் அளிக்கப்பட வேண்டும் என்றும் பரிந்துரைத்தது.",
        "Option A recommends the opposite of transparency.", "விருப்பம் A வெளிப்படைத்தன்மைக்கு எதிரானது.",
        "Option B is correct; speaking document + wide publicity.", "விருப்பம் B சரியானது; பேசும் ஆவணம் + பரந்த விளம்பரம் அளித்தல்.",
        "Option C is contrary to Cabinet government principles.", "விருப்பம் C அமைச்சரவை அரசுக் கொள்கைகளுக்கு எதிரானது.",
        "Option D is not a constitutional requirement.", "விருப்பம் D அரசியலமைப்புத் தேவை அல்ல.",
        "Transparency Principle: Sarkaria Commission insisted that secret or vague Governor's reports breed subjective and partisan abuse.",
        "வெளிப்படைத்தன்மைக் கொள்கை: ரகசியமான அல்லது தெளிவற்ற ஆளுநர் அறிக்கைகள் ஒரு சார்புடைய தவறான பயன்பாட்டிற்கு வழிவகுக்கும் என்று சர்க்காரியா ஆணையம் எச்சரித்தது.",
        "In S.R. Bommai (1994), the Supreme Court confirmed that the Governor's report is open to full judicial scrutiny to check if relevant material existed.",
        "எஸ்.ஆர். பொம்மை (1994) வழக்கில், தொடர்புடைய ஆதாரங்கள் இருந்தனவா என்பதைச் சரிபார்க்க ஆளுநர் அறிக்கை முழு நீதித்துறை ஆய்வுக்கு உட்பட்டது என்பதை உச்ச நீதிமன்றம் உறுதிப்படுத்தியது."
    ))

    # 074 - Key D
    qs.append(make_ep_q(
        PREFIX, 74, "Hard", "Sarkaria Commission", "Reasons in Proclamation Recommendation",
        "What did the Sarkaria Commission recommend regarding the text of the Presidential Proclamation issued under Article 356?",
        "சரத்து 356-ன் கீழ் வெளியிடப்படும் குடியரசுத் தலைவர் பிரகடனத்தின் உரை தொடர்பாக சர்க்காரியா ஆணையம் என்ன பரிந்துரைத்தது?",
        "It should be written in Sanskrit and English only", "அது சமஸ்கிருதம் மற்றும் ஆங்கிலத்தில் மட்டுமே எழுதப்பட வேண்டும்",
        "It should be countersigned by the Chief Justice of India", "அதில் இந்தியத் தலைமை நீதிபதி கட்டாயம் கையொப்பமிட வேண்டும்",
        "It should be kept under seal for twenty-five years before release", "வெளியிடுவதற்கு முன் இருபத்தைந்து ஆண்டுகளுக்கு அது முத்திரையிட்டு வைக்கப்பட வேண்டும்",
        "The proclamation should contain the specific reasons and grounds on which the President arrived at his satisfaction", "எந்தக் காரணங்கள் மற்றும் அடிப்படைகளின் மீது குடியரசுத் தலைவர் தனது திருப்தியை அடைந்தார் என்ற குறிப்பிட்ட காரணங்களை அப்பிரகடனம் கொண்டிருக்க வேண்டும்",
        "D",
        "The Sarkaria Commission recommended that the Presidential Proclamation issued under Article 356 should not merely recite boiler-plate constitutional language, but should state the precise grounds and reasons on which the President reached the conclusion that constitutional governance had failed in the State.",
        "சரத்து 356-ன் கீழ் வெளியிடப்படும் குடியரசுத் தலைவர் பிரகடனம் வெறும் வெற்று அரசியலமைப்பு வாசகங்களை மட்டும் கொண்டிருக்காமல், அந்த மாநிலத்தில் அரசியலமைப்பு ஆட்சி தோல்வியடைந்துவிட்டது என்ற முடிவுக்குக் குடியரசுத் தலைவர் வந்ததற்கான துல்லியமான காரணங்கள் மற்றும் அடிப்படைகளைக் கொண்டிருக்க வேண்டும் என்று சர்க்காரியா ஆணையம் பரிந்துரைத்தது.",
        "Option A is linguistically absurd.", "விருப்பம் A மொழியியல் ரீதியாக அபத்தமானது.",
        "Option B violates judicial separation of powers.", "விருப்பம் B நீதித்துறை அதிகாரப் பகிர்வை மீறுகிறது.",
        "Option C prevents democratic accountability.", "விருப்பம் C ஜனநாயகப் பொறுப்புடைமையைத் தடுக்கிறது.",
        "Option D is correct; speaking proclamation detailing explicit reasons.", "விருப்பம் D சரியானது; தெளிவான காரணங்களை விவரிக்கும் பிரகடனம்.",
        "Accountability Principle: Giving explicit reasons in the proclamation enables Parliament and the judiciary to test whether the satisfaction is bona fide.",
        "பொறுப்புடைமைக் கொள்கை: பிரகடனத்தில் வெளிப்படையான காரணங்களைக் குறிப்பிடுவது, குடியரசுத் தலைவரின் திருப்தி உண்மையானதா என்பதை பாராளுமன்றமும் நீதித்துறையும் ஆய்வு செய்ய வழிவகுக்கிறது.",
        "This prevents the Centre from issuing blanket, unreasoned proclamations to topple opposition governments.",
        "எதிர்க்கட்சி அரசுகளைக் கவிழ்ப்பதற்காக மத்திய அரசு காரணமற்ற பொத்தாம் பொதுவான பிரகடனங்களை வெளியிடுவதை இது தடுக்கிறது."
    ))

    # 075 - Key C
    qs.append(make_ep_q(
        PREFIX, 75, "Hard", "Venkatachaliah Commission", "NCRWC Recommendations on Article 356",
        "The National Commission to Review the Working of the Constitution (Venkatachaliah Commission, 2002) made which crucial recommendation regarding Article 356?",
        "அரசியலமைப்பு செயல்பாட்டை மறுஆய்வு செய்வதற்கான தேசிய ஆணையம் (வெங்கடாசலையா ஆணையம், 2002) சரத்து 356 தொடர்பாக என்ன முக்கியமான பரிந்துரையைச் செய்தது?",
        "Article 356 should be repealed immediately and completely", "சரத்து 356 உடனடியாகவும் முற்றிலுமாகவும் ரத்து செய்யப்பட வேண்டும்",
        "Article 356 should be invoked automatically every five years in every state", "ஒவ்வொரு ஐந்து ஆண்டுகளுக்கும் ஒவ்வொரு மாநிலத்திலும் சரத்து 356 தானாகவே பயன்படுத்தப்பட வேண்டும்",
        "Article 356 should NOT be deleted, but should be amended to incorporate the safeguards and guidelines laid down in the S.R. Bommai judgment", "சரத்து 356 நீக்கப்படக் கூடாது, ஆனால் எஸ்.ஆர். பொம்மை தீர்ப்பில் வகுக்கப்பட்ட பாதுகாப்புகள் மற்றும் வழிகாட்டுதல்களை அரசியலமைப்பு விதிகளாக இணைக்கும் வகையில் அது திருத்தப்பட வேண்டும்",
        "Article 356 should be placed under the exclusive jurisdiction of the NITI Aayog", "சரத்து 356 நிதி ஆயோக்கின் பிரத்தியேக அதிகார வரம்பின் கீழ் வைக்கப்பட வேண்டும்",
        "C",
        "The Venkatachaliah Commission (NCRWC, 2002) recommended that Article 356 should NOT be deleted from the Constitution because it is a necessary safety valve for extraordinary situations. However, it strongly recommended amending Article 356 to write the procedural and substantive safeguards laid down by the Supreme Court in S.R. Bommai (1994) directly into the constitutional text.",
        "வெங்கடாசலையா ஆணையம் (NCRWC, 2002) சரத்து 356 அரசியலமைப்பிலிருந்து நீக்கப்படக் கூடாது என்று பரிந்துரைத்தது, ஏனெனில் அது அசாதாரண சூழ்நிலைகளுக்கான அவசியமான பாதுகாப்பு வால்வாகும். இருப்பினும், எஸ்.ஆர். பொம்மை (1994) தீர்ப்பில் உச்ச நீதிமன்றம் வழங்கிய நடைமுறை மற்றும் உள்ளடக்கப் பாதுகாப்புகளை நேரடியாக அரசியலமைப்பு உரையிலேயே இணைக்கும் வகையில் சரத்து 356 திருத்தப்பட வேண்டும் என்று அது கடுமையாகப் பரிந்துரைத்தது.",
        "Option A was the recommendation of the Rajamannar Committee (1971), not the NCRWC.", "விருப்பம் A என்பது ராஜமன்னார் குழுவின் (1971) பரிந்துரையாகும், NCRWC அல்ல.",
        "Option B is absurd.", "விருப்பம் B அபத்தமானது.",
        "Option C is correct; retain Article 356 but constitutionalize Bommai safeguards.", "விருப்பம் C சரியானது; சரத்து 356-ஐத் தக்கவைத்து பொம்மை பாதுகாப்புகளை அரசியலமைப்பு விதிகளாக்குதல்.",
        "Option D is anachronistic and incorrect.", "விருப்பம் D காலப்பொருத்தமற்றது மற்றும் தவறானது.",
        "NCRWC (2002) Vision: Codify the S.R. Bommai judgment into the text of Article 356 to make the safeguards permanent and immune to future judicial dilution.",
        "NCRWC (2002) பார்வை: எதிர்காலத்தில் நீதிமன்றங்களால் தளர்த்தப்படுவதைத் தடுக்க எஸ்.ஆர். பொம்மை தீர்ப்பின் வழிகாட்டுதல்களை சரத்து 356-ன் நேரடி விதிகளாக மாற்றுதல்.",
        "The NCRWC was appointed by the Atal Bihari Vajpayee government and submitted its comprehensive report in March 2002.",
        "அடல் பிகாரி வாஜ்பாய் அரசால் நியமிக்கப்பட்ட இந்த ஆணையம் மார்ச் 2002-ல் தனது விரிவான அறிக்கையை சமர்ப்பித்தது."
    ))

    return qs

print("Batch 3 (Q051-Q075) ready.")
