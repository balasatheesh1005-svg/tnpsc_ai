# -*- coding: utf-8 -*-
"""
Emergency Provisions Grand Test - Batch 1 (Questions 1 to 25)
Prefix: EP_GT_
Keys: A: 7, B: 6, C: 6, D: 6 (Total: 25)
"""

from ep_mcq_helper import make_ep_q

PREFIX = "EP_GT_"

def get_gt_batch1():
    qs = []

    # 001 - Key A
    qs.append(make_ep_q(
        PREFIX, 1, "Easy", "Conceptual", "Constitutional Classification",
        "Under Part XVIII of the Constitution of India, how many distinct types of emergencies are stipulated?",
        "இந்திய அரசியலமைப்பின் பகுதி XVIII-ன் கீழ் எத்தனை வகையான அவசரநிலைகள் குறிப்பிடப்பட்டுள்ளன?",
        "Three types (National, President's Rule, Financial)", "மூன்று வகைகள் (தேசிய, குடியரசுத் தலைவர் ஆட்சி, நிதி)",
        "Two types (External and Internal)", "இரண்டு வகைகள் (வெளிப்புற மற்றும் உள்நாட்டு)",
        "Four types (Military, Civil, Economic, Political)", "நான்கு வகைகள் (இராணுவ, சிவில், பொருளாதார, அரசியல்)",
        "Five types (including Governor's emergency)", "ஐந்து வகைகள் (ஆளுநரின் அவசரநிலை உட்பட)",
        "A",
        "Part XVIII of the Constitution stipulates three types of emergencies: (1) National Emergency under Article 352, (2) President's Rule (State Emergency) under Article 356, and (3) Financial Emergency under Article 360.",
        "அரசியலமைப்பின் பகுதி XVIII மூன்று வகையான அவசரநிலைகளைக் குறிப்பிடுகிறது: (1) சரத்து 352-ன் கீழான தேசிய அவசரநிலை, (2) சரத்து 356-ன் கீழான குடியரசுத் தலைவர் ஆட்சி (மாநில அவசரநிலை), மற்றும் (3) சரத்து 360-ன் கீழான நிதி அவசரநிலை.",
        "Option A is correct; the Constitution specifies three distinct categories.", "விருப்பம் A சரியானது; அரசியலமைப்பு மூன்று தனித்துவமான வகைகளைக் குறிப்பிடுகிறது.",
        "Option B describes sub-categories of Article 352, not all emergency types.", "விருப்பம் B சரத்து 352-ன் துணைப் பிரிவுகளை விவரிக்கிறது.",
        "Option C mentions non-constitutional classifications.", "விருப்பம் C அரசியலமைப்பில் இல்லாத வகைப்பாடுகளைக் குறிப்பிடுகிறது.",
        "Option D is incorrect; there is no constitutional Governor's emergency in India.", "விருப்பம் D தவறு; இந்தியாவில் ஆளுநர் அவசரநிலை என்ற அரசியலமைப்பு வகை இல்லை.",
        "TNPSC Standard Fact: Part XVIII contains Articles 352 to 360 outlining three types of emergencies.",
        "TNPSC நிலையான உண்மை: பகுதி XVIII-ல் சரத்துகள் 352 முதல் 360 வரை மூன்று வகையான அவசரநிலைகள் உள்ளன.",
        "Dr. B.R. Ambedkar noted that these provisions are designed to protect the sovereignty, unity, and integrity of India.",
        "இந்தியாவின் இறைமை, ஒற்றுமை மற்றும் ஒருமைப்பாட்டைப் பாதுகாக்கவே இந்த விதிகள் வடிவமைக்கப்பட்டுள்ளன என்று டாக்டர் அம்பேத்கர் குறிப்பிட்டார்."
    ))

    # 002 - Key B
    qs.append(make_ep_q(
        PREFIX, 2, "Medium", "Conceptual", "Borrowing of Emergency Provisions",
        "The constitutional mechanism of suspending Fundamental Rights during an Emergency was borrowed from the constitution of which country?",
        "அவசரநிலையின் போது அடிப்படை உரிமைகளை இடைநிறுத்தும் அரசியலமைப்பு வழிமுறை எந்த நாட்டின் அரசியலமைப்பிலிருந்து பெறப்பட்டது?",
        "Government of India Act, 1935", "1935 இந்திய அரசுச் சட்டம்",
        "Weimar Constitution of Germany", "ஜெர்மனியின் வெய்மர் அரசியலமைப்பு",
        "United States Constitution", "அமெரிக்க அரசியலமைப்பு",
        "Constitution of USSR", "சோவியத் யூனியன் அரசியலமைப்பு",
        "B",
        "The suspension of Fundamental Rights during emergency is borrowed from the Weimar Constitution of Germany, while the structural scheme of emergency provisions was adapted from the Government of India Act 1935.",
        "அவசரநிலையின் போது அடிப்படை உரிமைகள் இடைநிறுத்தப்படும் முறை ஜெர்மனியின் வெய்மர் அரசியலமைப்பிலிருந்து பெறப்பட்டது; அதே சமயம் அவசரநிலைப் பிரிவுகளின் பொதுவான கட்டமைப்பு 1935 இந்திய அரசுச் சட்டத்திலிருந்து பெறப்பட்டது.",
        "Option A provided the general emergency framework, but not the fundamental rights suspension.", "விருப்பம் A பொதுவான கட்டமைப்பை வழங்கியது, அடிப்படை உரிமைகள் இடைநிறுத்தத்தை அல்ல.",
        "Option B is correct; Weimar Constitution of Germany is the direct source.", "விருப்பம் B சரியானது; ஜெர்மனியின் வெய்மர் அரசியலமைப்பே நேரடி மூலமாகும்.",
        "Option C has no constitutional suspension of bill of rights by executive fiat.", "விருப்பம் C-ல் நிர்வாக உத்தரவால் உரிமைகள் இடைநிறுத்தப்படும் முறை இல்லை.",
        "Option D provided Fundamental Duties, not emergency suspension.", "விருப்பம் D அடிப்படைக் கடமைகளை வழங்கியது.",
        "TNPSC Source Trap: Emergency framework = GoI Act 1935; Suspension of Fundamental Rights = Weimar Constitution.",
        "TNPSC மூலப் பொறி: அவசரநிலைக் கட்டமைப்பு = 1935 சட்டம்; அடிப்படை உரிமைகள் இடைநிறுத்தம் = வெய்மர் அரசியலமைப்பு.",
        "Articles 358 and 359 embody the provisions governing the suspension of rights during emergency.",
        "அவசரநிலையின் போது உரிமைகள் இடைநிறுத்தப்படுவதை நிர்வகிக்கும் விதிகளை சரத்துகள் 358 மற்றும் 359 கொண்டுள்ளன."
    ))

    # 003 - Key C
    qs.append(make_ep_q(
        PREFIX, 3, "Medium", "Conceptual", "Grounds for National Emergency",
        "Which of the following is NOT a constitutional ground for proclaiming a National Emergency under Article 352 today?",
        "இன்று சரத்து 352-ன் கீழ் தேசிய அவசரநிலையை அறிவிப்பதற்கான அரசியலமைப்பு காரணங்களில் இல்லாதது எது?",
        "War", "போர்",
        "External Aggression", "வெளிநாட்டு ஆக்கிரமிப்பு",
        "Internal Disturbance", "உள்நாட்டு அமைதியின்மை",
        "Armed Rebellion", "ஆயுதமேந்திய கிளர்ச்சி",
        "C",
        "'Internal Disturbance' was substituted by 'Armed Rebellion' by the 44th Constitutional Amendment Act, 1978. Therefore, internal disturbance is no longer a valid ground for proclaiming National Emergency.",
        "1978-ன் 44-வது அரசியலமைப்பு திருத்தச் சட்டத்தால் 'உள்நாட்டு அமைதியின்மை' என்ற சொல்லுக்குப் பதிலாக 'ஆயுதமேந்திய கிளர்ச்சி' சேர்க்கப்பட்டது. எனவே உள்நாட்டு அமைதியின்மை தற்போது செல்லுபடியாகும் காரணமல்ல.",
        "Option A is a valid ground under Article 352(1).", "விருப்பம் A சரத்து 352(1)-ன் கீழ் சரியான காரணமாகும்.",
        "Option B is a valid ground under Article 352(1).", "விருப்பம் B சரத்து 352(1)-ன் கீழ் சரியான காரணமாகும்.",
        "Option C is correct; 'Internal Disturbance' was deleted in 1978.", "விருப்பம் C சரியானது; 'உள்நாட்டு அமைதியின்மை' 1978-ல் நீக்கப்பட்டது.",
        "Option D is the valid ground inserted in 1978.", "விருப்பம் D என்பது 1978-ல் சேர்க்கப்பட்ட சரியான காரணமாகும்.",
        "TNPSC High-Yield Fact: The phrase 'Internal Disturbance' was deleted by 44th CAA 1978 to eliminate executive ambiguity.",
        "TNPSC உயர்-விளைச்சல் உண்மை: நிர்வாகக் குழப்பங்களைத் தவிர்க்க 1978-ன் 44-வது திருத்தச் சட்டத்தால் 'உள்நாட்டு அமைதியின்மை' நீக்கப்பட்டது.",
        "Internal Disturbance still appears in Article 355 as part of the Union's duty to protect states.",
        "மாநிலங்களைப் பாதுகாக்கும் மத்திய அரசின் கடமையின் ஒரு பகுதியாக சரத்து 355-ல் 'உள்நாட்டு அமைதியின்மை' என்ற சொல் இப்போதும் உள்ளது."
    ))

    # 004 - Key D
    qs.append(make_ep_q(
        PREFIX, 4, "Hard", "Constitutional Nuance", "Imminent Danger Declaration",
        "Can the President proclaim a National Emergency under Article 352 before the actual occurrence of war or armed rebellion?",
        "போர் அல்லது ஆயுதமேந்திய கிளர்ச்சி உண்மையில் நிகழ்வதற்கு முன்பே குடியரசுத் தலைவரால் சரத்து 352-ன் கீழ் தேசிய அவசரநிலையை அறிவிக்க முடியுமா?",
        "No, it can be declared only after actual hostilities break out", "இல்லை, உண்மையான மோதல்கள் வெடித்த பிறகு மட்டுமே அறிவிக்க முடியும்",
        "Only if approved by the Supreme Court beforehand", "முன்கூட்டியே உச்ச நீதிமன்றம் ஒப்புதல் அளித்தால் மட்டுமே முடியும்",
        "Only if the Rajya Sabha passes a special resolution beforehand", "மாநிலங்களவை முன்கூட்டியே சிறப்புத் தீர்மானம் நிறைவேற்றினால் மட்டுமே",
        "Yes, if satisfied that there is imminent danger of war or aggression or armed rebellion", "ஆம், போர், ஆக்கிரமிப்பு அல்லது ஆயுதமேந்திய கிளர்ச்சியின் உடனடி ஆபத்து இருப்பதாகத் திருப்தியடைந்தால் முடியும்",
        "D",
        "According to the Explanation to Article 352(1), a proclamation of emergency may be made before the actual occurrence of war or aggression or armed rebellion if the President is satisfied that there is imminent danger thereof.",
        "சரத்து 352(1)-ன் விளக்கத்தின்படி, போர், ஆக்கிரமிப்பு அல்லது ஆயுதமேந்திய கிளர்ச்சியின் உடனடி ஆபத்து உள்ளது என குடியரசுத் தலைவர் திருப்தியடைந்தால், அவை உண்மையில் நிகழ்வதற்கு முன்பே அவசரநிலைப் பிரகடனம் செய்யப்படலாம்.",
        "Option A is incorrect because actual occurrence is not mandatory.", "விருப்பம் A தவறு, ஏனெனில் நிகழ்வு உண்மையில் நடந்திருக்க வேண்டிய கட்டாயமில்லை.",
        "Option B is incorrect; Supreme Court prior approval is never required.", "விருப்பம் B தவறு; உச்ச நீதிமன்றத்தின் முன் அனுமதி தேவையில்லை.",
        "Option C is incorrect; Rajya Sabha prior resolution is not required.", "விருப்பம் C தவறு; மாநிலங்களவையின் முன் தீர்மானம் தேவையில்லை.",
        "Option D is correct; 'imminent danger' suffices under the constitutional text.", "விருப்பம் D சரியானது; 'உடனடி ஆபத்து' இருத்தலே போதுமானது.",
        "Exam Trap: Actual war is NOT required; imminent threat or danger is constitutionally sufficient.",
        "தேர்வுப் பொறி: உண்மையான போர் தேவையில்லை; உடனடி அச்சுறுத்தல் அல்லது ஆபத்தே போதுமானது.",
        "Both the 1962 and 1971 emergencies were declared under conditions of active hostilities, while 1975 was declared on imminent internal grounds.",
        "1962 மற்றும் 1971 அவசரநிலைகள் போரின் போது அறிவிக்கப்பட்டன; 1975 உள்நாட்டு காரணங்களுக்காக அறிவிக்கப்பட்டது."
    ))

    # 005 - Key A
    qs.append(make_ep_q(
        PREFIX, 5, "Hard", "Constitutional Amendment", "44th CAA Written Advice Clause",
        "Under Article 352(3), the President can proclaim a National Emergency only when the decision of the Cabinet is communicated in writing. What does 'Cabinet' mean in this context?",
        "சரத்து 352(3)-ன் கீழ், அமைச்சரவையின் முடிவு எழுத்துப்பூர்வமாகத் தெரிவிக்கப்படும் போது மட்டுமே குடியரசுத் தலைவர் தேசிய அவசரநிலையை அறிவிக்க முடியும். இந்தச் சூழலில் 'அமைச்சரவை' (Cabinet) என்பது எதனைக் குறிக்கிறது?",
        "The Council consisting of the Prime Minister and other Ministers of Cabinet rank", "பிரதமர் மற்றும் கேபினட் அந்தஸ்து கொண்ட பிற அமைச்சர்களைக் கொண்ட குழு",
        "The Prime Minister alone in consultation with the Home Minister", "உள்துறை அமைச்சருடன் கலந்தாலோசித்து பிரதமர் மட்டுமே எடுப்பது",
        "All Ministers of the Union including Ministers of State and Deputy Ministers", "இணை அமைச்சர்கள் மற்றும் துணை அமைச்சர்கள் உட்பட மத்திய அரசின் அனைத்து அமைச்சர்கள்",
        "The Cabinet Secretary and senior civil servants", "மத்திய அமைச்சரவைச் செயலாளர் மற்றும் மூத்த அரசு அதிகாரிகள்",
        "A",
        "Article 352(3) explicitly defines the Cabinet as 'the Council consisting of the Prime Minister and other Ministers of Cabinet rank appointed under Article 75'. This is the ONLY place where the word 'Cabinet' is defined in the Constitution of India.",
        "சரத்து 352(3) அமைச்சரவையை 'சரத்து 75-ன் கீழ் நியமிக்கப்பட்ட பிரதமர் மற்றும் கேபினட் அந்தஸ்து கொண்ட பிற அமைச்சர்களைக் கொண்ட குழு' என்று வெளிப்படையாக வரையறுக்கிறது. இந்திய அரசியலமைப்பில் 'அமைச்சரவை' என்ற சொல் வரையறுக்கப்பட்டுள்ள ஒரே இடம் இதுவேயாகும்.",
        "Option A is correct; exact definition under Article 352(3).", "விருப்பம் A சரியானது; சரத்து 352(3)-ன் கீழான துல்லியமான வரையறை.",
        "Option B is incorrect; the Prime Minister alone cannot tender this advice.", "விருப்பம் B தவறு; பிரதமர் தனித்து இந்த ஆலோசனையை வழங்க முடியாது.",
        "Option C describes the full Council of Ministers, not the smaller Cabinet.", "விருப்பம் C முழு அமைச்சரவைக் குழுவைக் குறிக்கிறது, சிறிய கேபினட்டை அல்ல.",
        "Option D refers to civil servants who have no political ministerial authority.", "விருப்பம் D அரசியல் அதிகாரமற்ற அரசு அதிகாரிகளைக் குறிக்கிறது.",
        "TNPSC Landmark Fact: The word 'Cabinet' appears only ONCE in the Indian Constitution — in Article 352(3), inserted by the 44th CAA 1978.",
        "TNPSC மைல்கல் உண்மை: இந்திய அரசியலமைப்பில் 'கேபினட்' (Cabinet) என்ற சொல் ஒரே ஒரு முறை மட்டுமே இடம்பெற்றுள்ளது — 1978-ன் 44-வது திருத்தத்தால் சேர்க்கப்பட்ட சரத்து 352(3)-ல்.",
        "This safeguard was introduced to prevent any Prime Minister from taking unilateral emergency decisions as occurred on June 25, 1975.",
        "1975 ஜூன் 25 அன்று நடந்தது போல எந்தவொரு பிரதமரும் தன்னிச்சையாக அவசரநிலை முடிவுகளை எடுப்பதைத் தடுக்கவே இந்தப் பாதுகாப்பு கொண்டுவரப்பட்டது."
    ))

    # 006 - Key B
    qs.append(make_ep_q(
        PREFIX, 6, "Medium", "Procedural", "Article 352 Parliamentary Approval Time",
        "A proclamation of National Emergency must be approved by both Houses of Parliament within what timeframe from its issuance?",
        "தேசிய அவசரநிலைப் பிரகடனம் வெளியிடப்பட்டதிலிருந்து எத்தனை கால அவகாசத்திற்குள் பாராளுமன்றத்தின் இரு அவைகளாலும் அங்கீகரிக்கப்பட வேண்டும்?",
        "Within fourteen days", "பதினான்கு நாட்களுக்குள்",
        "Within one month", "ஒரு மாதத்திற்குள்",
        "Within two months", "இரண்டு மாதங்களுக்குள்",
        "Within six months", "ஆறு மாதங்களுக்குள்",
        "B",
        "Under Article 352(4), a proclamation of National Emergency must be approved by both Houses of Parliament within one month from the date of its issue. Originally it was two months, but was reduced to one month by the 44th CAA, 1978.",
        "சரத்து 352(4)-ன் கீழ், தேசிய அவசரநிலைப் பிரகடனம் வெளியிடப்பட்ட தேதியிலிருந்து ஒரு மாதத்திற்குள் பாராளுமன்றத்தின் இரு அவைகளாலும் ஒப்புதல் அளிக்கப்பட வேண்டும். ஆரம்பத்தில் இது 2 மாதங்களாக இருந்தது, 1978-ன் 44-வது திருத்தத்தால் ஒரு மாதமாகக் குறைக்கப்பட்டது.",
        "Option A (14 days) is the time limit for convening a special sitting of Lok Sabha for disapproval.", "விருப்பம் A (14 நாட்கள்) நிராகரிப்புக்கான சிறப்புக் கூட்டத்தைக் கூட்டுவதற்கான காலக்கெடுவாகும்.",
        "Option B is correct; 1 month under Article 352(4).", "விருப்பம் B சரியானது; சரத்து 352(4)-ன் கீழ் 1 மாதம்.",
        "Option C (2 months) is the original pre-1978 period, and the current period for Articles 356 and 360.", "விருப்பம் C (2 மாதங்கள்) 1978-க்கு முந்தைய காலம் மற்றும் சரத்துகள் 356, 360-க்கான காலமாகும்.",
        "Option D (6 months) is the duration of operation once approved.", "விருப்பம் D (6 மாதங்கள்) ஒப்புதல் பெற்ற பிறகு செயல்படும் கால அளவாகும்.",
        "TNPSC Comparison Trap: Article 352 = 1 Month; Article 356 = 2 Months; Article 360 = 2 Months.",
        "TNPSC ஒப்பீட்டுப் பொறி: சரத்து 352 = 1 மாதம்; சரத்து 356 = 2 மாதங்கள்; சரத்து 360 = 2 மாதங்கள்.",
        "The reduction to one month reflects greater democratic urgency for national emergency oversight.",
        "ஒரு மாதமாகக் குறைக்கப்பட்டது தேசிய அவசரநிலையின் மீதான பாராளுமன்றக் கண்காணிப்பின் ஜனநாயக அவசியத்தைப் பிரதிபலிக்கிறது."
    ))

    # 007 - Key C
    qs.append(make_ep_q(
        PREFIX, 7, "Hard", "Procedural", "Majority for Article 352 Approval",
        "What majority is required in each House of Parliament to approve a resolution for proclamation or continuation of National Emergency?",
        "தேசிய அவசரநிலைப் பிரகடனம் அல்லது அதன் தொடர்ச்சிக்கான தீர்மானத்திற்கு ஒப்புதல் அளிக்க பாராளுமன்றத்தின் ஒவ்வொரு அவையிலும் என்ன பெரும்பான்மை தேவைப்படுகிறது?",
        "Simple majority of members present and voting", "வருகை தந்து வாக்களிக்கும் உறுப்பினர்களில் எளிய பெரும்பான்மை",
        "Absolute majority of the total membership of the House", "அவையின் மொத்த உறுப்பினர்களில் முழுமையான பெரும்பான்மை",
        "Special majority: Majority of total membership AND 2/3 of members present and voting", "சிறப்புப் பெரும்பான்மை: மொத்த உறுப்பினர்களில் பெரும்பான்மை மற்றும் வருகை தந்து வாக்களிப்போரில் 2/3 பங்கு",
        "Two-thirds majority of the total membership of the House", "அவையின் மொத்த உறுப்பினர்களில் மூன்றில் இரண்டு பங்கு பெரும்பான்மை",
        "C",
        "Under Article 352(6), every resolution approving the proclamation or continuation of emergency must be passed by a special majority: a majority of the total membership of that House AND not less than two-thirds of the members present and voting.",
        "சரத்து 352(6)-ன் கீழ், அவசரநிலைப் பிரகடனம் அல்லது அதன் தொடர்ச்சிக்கான தீர்மானம் சிறப்புப் பெரும்பான்மையால் நிறைவேற்றப்பட வேண்டும்: அவையின் மொத்த உறுப்பினர்களில் பெரும்பான்மை மற்றும் வருகை தந்து வாக்களிக்கும் உறுப்பினர்களில் மூன்றில் இரண்டு பங்கு குறையாமல் ஆதரவு.",
        "Option A was the requirement prior to the 44th Amendment Act, 1978.", "விருப்பம் A என்பது 1978-ன் 44-வது திருத்தச் சட்டத்திற்கு முந்தைய தேவையாகும்.",
        "Option B is insufficient on its own.", "விருப்பம் B தனித்து போதுமானதல்ல.",
        "Option C is correct; special majority introduced by the 44th CAA 1978.", "விருப்பம் C சரியானது; 1978-ன் 44-வது திருத்தத்தால் கொண்டுவரப்பட்ட சிறப்புப் பெரும்பான்மை.",
        "Option D applies strictly to presidential impeachment under Article 61.", "விருப்பம் D சரத்து 61-ன் கீழான குடியரசுத் தலைவர் பதவி நீக்கத்திற்கு மட்டுமே பொருந்தும்.",
        "Key Distinction: Article 352 = Special Majority; Article 356 = Simple Majority; Article 360 = Simple Majority.",
        "முக்கிய வேறுபாடு: சரத்து 352 = சிறப்புப் பெரும்பான்மை; சரத்து 356 = எளிய பெரும்பான்மை; சரத்து 360 = எளிய பெரும்பான்மை.",
        "Originally, a simple majority was sufficient for Article 352 as well; the 44th CAA elevated it to special majority to prevent abuse.",
        "முதலில் சரத்து 352-க்கும் எளிய பெரும்பான்மையே போதுமானதாக இருந்தது; தவறான பயன்பாட்டைத் தடுக்கவே 44-வது திருத்தம் அதை சிறப்புப் பெரும்பான்மையாக உயர்த்தியது."
    ))

    # 008 - Key D
    qs.append(make_ep_q(
        PREFIX, 8, "Medium", "Procedural", "Duration of Approved Emergency",
        "Once approved by both Houses of Parliament, for how long does a National Emergency remain in force at a time?",
        "பாராளுமன்றத்தின் இரு அவைகளாலும் அங்கீகரிக்கப்பட்டவுடன், தேசிய அவசரநிலை ஒரு நேரத்தில் எவ்வளவு காலம் தொடர்ந்து செயல்பாட்டில் இருக்கும்?",
        "For one month only", "ஒரு மாதம் மட்டுமே",
        "For three months", "மூன்று மாதங்கள்",
        "Indefinitely until revoked", "ரத்து செய்யப்படும் வரை காலவரையின்றி",
        "For six months from the date of passing of the resolution", "தீர்மானம் நிறைவேற்றப்பட்ட தேதியிலிருந்து ஆறு மாதங்கள்",
        "D",
        "Under Article 352(5), an approved proclamation of National Emergency remains in force for six months at a time, and can be extended for an indefinite period with parliamentary approval every six months.",
        "சரத்து 352(5)-ன் கீழ், அங்கீகரிக்கப்பட்ட தேசிய அவசரநிலைப் பிரகடனம் ஒரு நேரத்தில் ஆறு மாதங்கள் வரை செயல்பாட்டில் இருக்கும், மேலும் ஒவ்வொரு ஆறு மாதங்களுக்கும் பாராளுமன்ற ஒப்புதலுடன் காலவரையின்றி நீட்டிக்கப்படலாம்.",
        "Option A is the initial pre-approval duration.", "விருப்பம் A என்பது ஒப்புதலுக்கு முந்தைய ஆரம்ப கால அளவு.",
        "Option B is not a constitutional emergency interval.", "விருப்பம் B அரசியலமைப்பு அவசரநிலைக் கால இடைவெளி அல்ல.",
        "Option C describes the pre-1978 position (which was changed by 44th CAA).", "விருப்பம் C 1978-க்கு முந்தைய நிலையைக் குறிக்கிறது (44-வது திருத்தத்தால் மாற்றப்பட்டது).",
        "Option D is correct; exactly 6 months per approval cycle.", "விருப்பம் D சரியானது; ஒவ்வொரு ஒப்புதல் சுழற்சிக்கும் சரியாக 6 மாதங்கள்.",
        "Periodic Approval Rule: 6-month periodic approval for Article 352 was introduced by the 44th Constitutional Amendment Act 1978.",
        "காலமுறை ஒப்புதல் விதி: சரத்து 352-க்கான 6 மாத காலமுறை ஒப்புதல் 1978-ன் 44-வது அரசியலமைப்பு திருத்தச் சட்டத்தால் கொண்டுவரப்பட்டது.",
        "Before 1978, once approved by Parliament, the emergency continued indefinitely until the executive decided to revoke it.",
        "1978-க்கு முன், பாராளுமன்றம் ஒருமுறை ஒப்புதல் அளித்த பிறகு, நிர்வாகம் ரத்து செய்ய முடிவு செய்யும் வரை அவசரநிலை காலவரையின்றித் தொடர்ந்தது."
    ))

    # 009 - Key A
    qs.append(make_ep_q(
        PREFIX, 9, "Hard", "Procedural", "Disapproval Resolution Rules",
        "Which of the following statements is correct regarding a resolution for disapproving the continuation of a National Emergency?",
        "தேசிய அவசரநிலை தொடர்வதை நிராகரிக்கும் தீர்மானம் தொடர்பாக பின்வரும் கூற்றுகளில் எது சரியானது?",
        "It can be passed only by the Lok Sabha and requires a simple majority", "இது மக்களவையால் மட்டுமே நிறைவேற்றப்பட முடியும் மற்றும் எளிய பெரும்பான்மை போதுமானது",
        "It must be passed by both Houses of Parliament by a special majority", "இது பாராளுமன்றத்தின் இரு அவைகளாலும் சிறப்புப் பெரும்பான்மையால் நிறைவேற்றப்பட வேண்டும்",
        "It must be initiated by the President upon Cabinet advice", "இது அமைச்சரவை ஆலோசனையின் பேரில் குடியரசுத் தலைவரால் தொடங்கப்பட வேண்டும்",
        "It requires a joint sitting of both Houses of Parliament", "இதற்கு பாராளுமன்றத்தின் இரு அவைகளின் கூட்டுக்கூட்டம் தேவைப்படுகிறது",
        "A",
        "Under Article 352(7) and (8), a resolution disapproving the continuation of emergency needs to be passed ONLY by the Lok Sabha by a simple majority. The Rajya Sabha has no role in disapproving the emergency.",
        "சரத்து 352(7) மற்றும் (8)-ன் கீழ், அவசரநிலை தொடர்வதை நிராகரிக்கும் தீர்மானம் மக்களவையில் மட்டுமே எளிய பெரும்பான்மையால் நிறைவேற்றப்பட வேண்டும். அவசரநிலையை நிராகரிப்பதில் மாநிலங்களவைக்கு எந்தப் பங்கும் இல்லை.",
        "Option A is correct; Lok Sabha only + simple majority.", "விருப்பம் A சரியானது; மக்களவை மட்டுமே + எளிய பெரும்பான்மை.",
        "Option B describes approval, not disapproval.", "விருப்பம் B ஒப்புதலை விவரிக்கிறது, நிராகரிப்பை அல்ல.",
        "Option C describes revocation by the President, not resolution by Parliament.", "விருப்பம் C குடியரசுத் தலைவரின் ரத்தை விவரிக்கிறது.",
        "Option D is incorrect; there is no joint sitting provision for emergency resolutions.", "விருப்பம் D தவறு; அவசரநிலைத் தீர்மானங்களுக்கு கூட்டுக் கூட்டத்திற்கு இடமில்லை.",
        "Approval vs Disapproval Contrast: Approval = Both Houses (Special Majority); Disapproval = Lok Sabha Only (Simple Majority).",
        "ஒப்புதல் vs நிராகரிப்பு வேறுபாடு: ஒப்புதல் = இரு அவைகளும் (சிறப்புப் பெரும்பான்மை); நிராகரிப்பு = மக்களவை மட்டுமே (எளிய பெரும்பான்மை).",
        "This asymmetric mechanism empowers the directly elected house of the people to terminate an emergency against executive wishes.",
        "மக்களால் நேரடியாகத் தேர்ந்தெடுக்கப்பட்ட மக்களவை நிர்வாகத்தின் விருப்பத்திற்கு எதிராக அவசரநிலையை முடிவுக்குக் கொண்டுவர இந்த வழிமுறை அதிகாரம் அளிக்கிறது."
    ))

    # 010 - Key B
    qs.append(make_ep_q(
        PREFIX, 10, "Medium", "Procedural", "Notice for Disapproval Sitting",
        "Under Article 352(8), what proportion of Lok Sabha members must give written notice to demand a special sitting to disapprove an Emergency?",
        "சரத்து 352(8)-ன் கீழ், அவசரநிலையை நிராகரிக்க சிறப்புக் கூட்டத்தைக் கோர மக்களவை உறுப்பினர்களில் எத்தனை பங்கு உறுப்பினர்கள் எழுத்துப்பூர்வ அறிவிப்பு அளிக்க வேண்டும்?",
        "Not less than one-twentieth (1/20th) of the total members", "மொத்த உறுப்பினர்களில் இருபதில் ஒரு பங்கிற்கு குறையாமல் (1/20)",
        "Not less than one-tenth (1/10th) of the total members", "மொத்த உறுப்பினர்களில் பத்தில் ஒரு பங்கிற்கு குறையாமல் (1/10)",
        "Not less than one-fourth (1/4th) of the total members", "மொத்த உறுப்பினர்களில் நான்கில் ஒரு பங்கிற்கு குறையாமல் (1/4)",
        "Not less than one-third (1/3rd) of the total members", "மொத்த உறுப்பினர்களில் மூன்றில் ஒரு பங்கிற்கு குறையாமல் (1/3)",
        "B",
        "Under Article 352(8), a written notice signed by not less than one-tenth (1/10th) of the total number of members of the Lok Sabha may be given to the Speaker (or President if not in session) to convene a special sitting.",
        "சரத்து 352(8)-ன் கீழ், மக்களவையின் மொத்த உறுப்பினர்களில் பத்தில் ஒரு பங்கிற்கு (1/10) குறையாத உறுப்பினர்களால் கையொப்பமிடப்பட்ட எழுத்துப்பூர்வ அறிவிப்பு சபாநாயகரிடம் (அவை கூடாத போது குடியரசுத் தலைவரிடம்) சிறப்புக் கூட்டத்தைக் கூட்ட வழங்கப்படலாம்.",
        "Option A (1/20th) is too low and has no constitutional standing.", "விருப்பம் A (1/20) அரசியலமைப்பு விதிகளில் இல்லாதது.",
        "Option B is correct; 1/10th of the total members of the Lok Sabha.", "விருப்பம் B சரியானது; மக்களவையின் மொத்த உறுப்பினர்களில் 1/10 பங்கு.",
        "Option C (1/4th) applies to impeachment notice under Article 61.", "விருப்பம் C (1/4) சரத்து 61-ன் கீழான பதவி நீக்க அறிவிப்பிற்குப் பொருந்தும்.",
        "Option D (1/3rd) is not the quorum for emergency special sitting.", "விருப்பம் D அவசரநிலை சிறப்புக் கூட்டத்திற்கான கோரமல்ல.",
        "TNPSC Procedural Rule: 1/10th Lok Sabha notice -> Special sitting within 14 days -> Simple majority disapproval.",
        "TNPSC நடைமுறை விதி: 1/10 மக்களவை அறிவிப்பு -> 14 நாட்களில் சிறப்புக் கூட்டம் -> எளிய பெரும்பான்மை நிராகரிப்பு.",
        "The special sitting must be held within 14 days from the date on which such written notice is received.",
        "அத்தகைய எழுத்துப்பூர்வ அறிவிப்பு பெறப்பட்ட தேதியிலிருந்து 14 நாட்களுக்குள் சிறப்புக் கூட்டம் கூட்டப்பட வேண்டும்."
    ))

    # 011 - Key C
    qs.append(make_ep_q(
        PREFIX, 11, "Medium", "Historical", "Duration of First National Emergency",
        "The First National Emergency proclaimed in October 1962 remained in operation until which year?",
        "அக்டோபர் 1962-ல் பிரகடனப்படுத்தப்பட்ட முதல் தேசிய அவசரநிலை எந்த ஆண்டு வரை செயல்பாட்டில் இருந்தது?",
        "1963 (after China declared ceasefire)", "1963 (சீனா போர்நிறுத்தம் அறிவித்த பிறகு)",
        "1965 (until Pakistan war broke out)", "1965 (பாகிஸ்தான் போர் வெடிக்கும் வரை)",
        "January 1968", "ஜனவரி 1968",
        "December 1971", "டிசம்பர் 1971",
        "C",
        "The First National Emergency was proclaimed on October 26, 1962 in the wake of Chinese aggression in NEFA (now Arunachal Pradesh) and was revoked in January 1968. It thus covered both the 1962 China war and the 1965 Indo-Pak war.",
        "முதல் தேசிய அவசரநிலை நேபாவில் (தற்போதைய அருணாச்சலப் பிரதேசம்) சீன ஆக்கிரமிப்பைத் தொடர்ந்து அக்டோபர் 26, 1962 அன்று அறிவிக்கப்பட்டு, ஜனவரி 1968-ல் ரத்து செய்யப்பட்டது. எனவே இது 1962 சீனப் போர் மற்றும் 1965 பாகிஸ்தான் போர் இரண்டையும் உள்ளடக்கியது.",
        "Option A is wrong because emergency continued long after the ceasefire.", "விருப்பம் A தவறு, ஏனெனில் போர்நிறுத்தத்திற்குப் பின்னரும் அவசரநிலை தொடர்ந்தது.",
        "Option B is wrong because it covered the 1965 war without requiring a new proclamation.", "விருப்பம் B தவறு, ஏனெனில் 1965 போரின் போதும் இது செயல்பாட்டில் இருந்தது.",
        "Option C is correct; revoked in January 1968 (lasted over 5 years).", "விருப்பம் C சரியானது; ஜனவரி 1968-ல் ரத்து செய்யப்பட்டது (5 ஆண்டுகளுக்கு மேல் நீடித்தது).",
        "Option D was when the Second National Emergency was declared.", "விருப்பம் D இரண்டாவது தேசிய அவசரநிலை அறிவிக்கப்பட்ட ஆண்டாகும்.",
        "TNPSC Historical Fact: First Emergency = Oct 1962 to Jan 1968. Longest single National Emergency spell.",
        "TNPSC வரலாற்று உண்மை: முதல் அவசரநிலை = அக்டோபர் 1962 முதல் ஜனவரி 1968 வரை. மிக நீண்ட தேசிய அவசரநிலைக் காலம்.",
        "Because the 1962 proclamation was still active, no fresh emergency was needed during the 1965 war.",
        "1962 பிரகடனம் தொடர்ந்து செயல்பாட்டில் இருந்ததால், 1965 போரின் போது புதிய அவசரநிலை எதுவும் தேவையில்லை."
    ))

    # 012 - Key D
    qs.append(make_ep_q(
        PREFIX, 12, "Easy", "Historical", "External vs Internal Emergency Proclamations",
        "Out of the three proclamations of National Emergency in India, how many were External Emergencies and how many were Internal?",
        "இந்தியாவில் அறிவிக்கப்பட்ட மூன்று தேசிய அவசரநிலைப் பிரகடனங்களில், எத்தனை வெளிப்புற அவசரநிலைகள் மற்றும் எத்தனை உள்நாட்டு அவசரநிலைகள்?",
        "All three were External Emergencies", "மூன்றுமே வெளிப்புற அவசரநிலைகள்",
        "All three were Internal Emergencies", "மூன்றுமே உள்நாட்டு அவசரநிலைகள்",
        "One External (1971) and Two Internal (1962, 1975)", "ஒரு வெளிப்புற (1971) மற்றும் இரண்டு உள்நாட்டு (1962, 1975)",
        "Two External (1962, 1971) and One Internal (1975)", "இரண்டு வெளிப்புற (1962, 1971) மற்றும் ஒரு உள்நாட்டு (1975)",
        "D",
        "The 1962 and 1971 emergencies were External Emergencies declared on the ground of external aggression / war. The 1975 emergency was the only Internal Emergency declared on the ground of 'internal disturbance'.",
        "1962 மற்றும் 1971 அவசரநிலைகள் வெளிநாட்டு ஆக்கிரமிப்பு / போர் காரணமாக அறிவிக்கப்பட்ட வெளிப்புற அவசரநிலைகள் ஆகும். 1975 அவசரநிலை மட்டுமே 'உள்நாட்டு அமைதியின்மை' என்ற அடிப்படையில் அறிவிக்கப்பட்ட ஒரே உள்நாட்டு அவசரநிலையாகும்.",
        "Option A ignores the June 1975 internal emergency.", "விருப்பம் A ஜூன் 1975 உள்நாட்டு அவசரநிலையைப் புறக்கணிக்கிறது.",
        "Option B ignores the wars of 1962 and 1971.", "விருப்பம் B 1962 மற்றும் 1971 போர்களைப் புறக்கணிக்கிறது.",
        "Option C misclassifies 1962 as internal.", "விருப்பம் C 1962-ஐ உள்நாட்டு அவசரநிலை எனத் தவறாகக் குறிப்பிடுகிறது.",
        "Option D is correct; two external (1962, 1971) and one internal (1975).", "விருப்பம் D சரியானது; இரண்டு வெளிப்புற (1962, 1971) மற்றும் ஒரு உள்நாட்டு (1975).",
        "TNPSC Direct Question: External emergencies = 2 (1962, 1971); Internal emergencies = 1 (1975).",
        "TNPSC நேரடி வினா: வெளிப்புற அவசரநிலைகள் = 2 (1962, 1971); உள்நாட்டு அவசரநிலை = 1 (1975).",
        "The external emergency of 1971 and internal emergency of 1975 both ended simultaneously on March 21, 1977.",
        "1971 வெளிப்புற அவசரநிலையும் 1975 உள்நாட்டு அவசரநிலையும் மார்ச் 21, 1977 அன்று ஒரே நேரத்தில் முடிவுக்கு வந்தன."
    ))

    # 013 - Key A
    qs.append(make_ep_q(
        PREFIX, 13, "Hard", "Constitutional Impact", "Executive Power during National Emergency",
        "During the operation of a National Emergency, what is the exact constitutional effect on the State Executive under Article 353(a)?",
        "தேசிய அவசரநிலையின் போது, சரத்து 353(a)-ன் கீழ் மாநில நிர்வாகத்தின் மீது ஏற்படும் துல்லியமான அரசியலமைப்பு விளைவு என்ன?",
        "The Union executive power extends to giving binding directions to any state on how its executive power is exercised, but the State Government is NOT dismissed", "மாநில நிர்வாக அதிகாரத்தை எவ்வாறு செயல்படுத்த வேண்டும் என்பது குறித்து வழிகாட்டும் அதிகாரத்தை மத்திய அரசு பெறுகிறது, ஆனால் மாநில அரசு பதவி நீக்கம் செய்யப்படுவதில்லை",
        "The State Government is automatically suspended and the Governor assumes all powers", "மாநில அரசு தானாகவே இடைநிறுத்தப்பட்டு ஆளுநர் அனைத்து அதிகாரங்களையும் தன்வசம் எடுத்துக்கொள்கிறார்",
        "The State Ministry is dismissed and the President takes over direct administration", "மாநில அமைச்சரவை பதவி நீக்கம் செய்யப்பட்டு குடியரசுத் தலைவர் நேரடி நிர்வாகத்தை மேற்கொள்கிறார்",
        "The Chief Minister becomes directly subordinate to the Chief of Defence Staff", "முதலமைச்சர் நேரடியாக பாதுகாப்புப் படைத் தளபதியின் கீழ் கொண்டுவரப்படுகிறார்",
        "A",
        "Under Article 353(a), the executive power of the Union extends to giving directions to any State as to the manner in which the executive power thereof is to be exercised. The state government continues to function, but is brought under the complete direct control of the Union.",
        "சரத்து 353(a)-ன் கீழ், எந்தவொரு மாநிலத்திற்கும் அதன் நிர்வாக அதிகாரத்தை எவ்வாறு செயல்படுத்த வேண்டும் என்று உத்தரவுகளைப் பிறப்பிக்கும் அதிகாரம் மத்திய அரசுக்குக் கிடைக்கிறது. மாநில அரசு தொடர்ந்து செயல்படும், ஆனால் அது மத்திய அரசின் முழுமையான கட்டுப்பாட்டின் கீழ் கொண்டுவரப்படும்.",
        "Option A is correct; state government continues but under binding Union directions.", "விருப்பம் A சரியானது; மாநில அரசு நீடிக்கிறது ஆனால் மத்திய வழிகாட்டுதலுக்குக் கட்டுப்படுகிறது.",
        "Option B describes President's Rule under Article 356, not National Emergency.", "விருப்பம் B சரத்து 356 குடியரசுத் தலைவர் ஆட்சியை விவரிக்கிறது.",
        "Option C also describes Article 356.", "விருப்பம் C சரத்து 356-ஐ விவரிக்கிறது.",
        "Option D mentions non-constitutional military arrangements.", "விருப்பம் D அரசியலமைப்பில் இல்லாத இராணுவ ஏற்பாடுகளைக் குறிப்பிடுகிறது.",
        "Vital Concept: National Emergency (352) = State executive continues under Union control; President's Rule (356) = State executive dismissed.",
        "முக்கியக் கருத்து: தேசிய அவசரநிலை (352) = மாநில நிர்வாகம் மத்திய கட்டுப்பாட்டில் நீடிக்கிறது; குடியரசுத் தலைவர் ஆட்சி (356) = மாநில நிர்வாகம் கலைக்கப்படுகிறது.",
        "The 42nd Amendment Act 1976 extended this directive power even to states where emergency is not formally in operation, if their territory is affected by emergency activities.",
        "1976-ன் 42-வது திருத்தச் சட்டம், அவசரநிலை செயல்பாட்டில் இல்லாத மாநிலங்களுக்கும் கூட இந்த வழிகாட்டுதல் அதிகாரத்தை நீட்டித்தது."
    ))

    # 014 - Key B
    qs.append(make_ep_q(
        PREFIX, 14, "Hard", "Constitutional Impact", "Legislative Power under Article 250",
        "Under Article 250, what happens to the legislative powers of Parliament and State Legislatures during a National Emergency?",
        "சரத்து 250-ன் கீழ், தேசிய அவசரநிலையின் போது பாராளுமன்றம் மற்றும் மாநில சட்டமன்றங்களின் சட்டமன்ற அதிகாரங்களுக்கு என்ன நிகழ்கிறது?",
        "The State Legislature is dissolved and Parliament becomes the sole lawmaking body", "மாநில சட்டமன்றம் கலைக்கப்பட்டு பாராளுமன்றம் மட்டுமே ஒரே சட்டமியற்றும் அமைப்பாக மாறுகிறது",
        "Parliament gains concurrent power to make laws on State List subjects, while the State Legislature continues to legislate", "மாநில சட்டமன்றம் தொடர்ந்து சட்டம் இயற்றும் அதே வேளையில், மாநிலப் பட்டியல் விவகாரங்களில் சட்டம் இயற்றும் இணை அதிகாரத்தைப் பாராளுமன்றம் பெறுகிறது",
        "All state laws are automatically repealed and replaced by Central acts", "அனைத்து மாநில சட்டங்களும் தானாகவே ரத்து செய்யப்பட்டு மத்திய சட்டங்களால் மாற்றப்படுகின்றன",
        "Parliament can legislate on State List subjects only after obtaining consent of half the states", "பாதி மாநிலங்களின் ஒப்புதலைப் பெற்ற பிறகே பாராளுமன்றம் மாநிலப் பட்டியலில் சட்டம் இயற்ற முடியும்",
        "B",
        "Under Article 250, while a National Emergency is in operation, Parliament has the power to make laws for the whole or any part of India with respect to any of the matters enumerated in the State List. The State Legislature's legislative power is not suspended, but Parliament has concurrent overriding authority.",
        "சரத்து 250-ன் கீழ், தேசிய அவசரநிலையின் போது மாநிலப் பட்டியலில் உள்ள எந்தவொரு விவகாரத்தின் மீதும் சட்டம் இயற்றும் அதிகாரத்தைப் பாராளுமன்றம் பெறுகிறது. மாநில சட்டமன்றத்தின் அதிகாரம் இடைநிறுத்தப்படுவதில்லை, ஆனால் பாராளுமன்றம் மேலோங்கும் இணை அதிகாரத்தைப் பெறுகிறது.",
        "Option A describes Article 356, not Article 352.", "விருப்பம் A சரத்து 356-ஐ விவரிக்கிறது.",
        "Option B is correct; State Legislature continues with concurrent parliamentary supremacy.", "விருப்பம் B சரியானது; மாநில சட்டமன்றம் நீடிக்கிறது, பாராளுமன்றம் இணை மேலாதிக்கத்தைப் பெறுகிறது.",
        "Option C is factually and constitutionally wrong.", "விருப்பம் C தவறானது.",
        "Option D confuses Article 250 with Article 252 or constitutional amendment.", "விருப்பம் D சரத்து 250-ஐ சரத்து 252 அல்லது அரசியலமைப்பு திருத்தத்துடன் குழப்புகிறது.",
        "Article 251 Conflict Rule: If a State law conflicts with a Parliamentary law made under Article 250, the Parliamentary law prevails.",
        "சரத்து 251 முரண்பாட்டு விதி: சரத்து 250-ன் கீழ் இயற்றப்பட்ட பாராளுமன்ற சட்டத்துடன் மாநில சட்டம் முரண்பட்டால், பாராளுமன்ற சட்டமே மேலோங்கும்.",
        "The laws made by Parliament under Article 250 cease to have effect six months after the emergency ceases.",
        "சரத்து 250-ன் கீழ் பாராளுமன்றம் இயற்றிய சட்டங்கள் அவசரநிலை முடிவுக்கு வந்த ஆறு மாதங்களில் செயலிழந்துவிடும்."
    ))

    # 015 - Key C
    qs.append(make_ep_q(
        PREFIX, 15, "Medium", "Financial Effect", "Article 354 Revenue Distribution Modification",
        "Under Article 354, the President may modify the constitutional distribution of revenues between the Union and States during a National Emergency. How long can such an order remain valid?",
        "சரத்து 354-ன் கீழ், தேசிய அவசரநிலையின் போது மத்திய மற்றும் மாநிலங்களுக்கு இடையேயான அரசியலமைப்பு வருவாய் பகிர்வை குடியரசுத் தலைவர் மாற்றியமைக்கலாம். இத்தகைய உத்தரவு எவ்வளவு காலம் செல்லுபடியாகும்?",
        "Indefinitely until repealed by Parliament", "பாராளுமன்றத்தால் ரத்து செய்யப்படும் வரை காலவரையின்றி",
        "For exactly six months from the date of the order", "உத்தரவு பிறப்பிக்கப்பட்ட தேதியிலிருந்து சரியாக ஆறு மாதங்கள்",
        "Not extending beyond the financial year in which the emergency ceases to operate", "அவசரநிலை முடிவுக்கு வரும் நிதியாண்டுக்கு அப்பால் நீடிக்காமல் இருக்கும் வரை மட்டுமே",
        "Only for thirty days unless ratified by the Finance Commission", "நிதி ஆணையத்தால் அங்கீகரிக்கப்படாவிட்டால் முப்பது நாட்கள் மட்டுமே",
        "C",
        "Under Article 354(2), any presidential order modifying the financial provisions (Articles 268 to 279) shall not extend beyond the financial year in which the emergency proclamation ceases to operate. Every such order must also be laid before each House of Parliament.",
        "சரத்து 354(2)-ன் கீழ், நிதிப் பகிர்வு விதிகளை (சரத்துகள் 268 முதல் 279 வரை) மாற்றியமைக்கும் எந்தவொரு குடியரசுத் தலைவரின் உத்தரவும் அவசரநிலைப் பிரகடனம் முடிவுக்கு வரும் நிதியாண்டைத் தாண்டி நீடிக்காது. அத்தகைய ஒவ்வொரு உத்தரவும் பாராளுமன்றத்தின் இரு அவைகளின் முன்பும் வைக்கப்பட வேண்டும்.",
        "Option A is incorrect because financial modifications are strictly temporary.", "விருப்பம் A தவறு, ஏனெனில் நிதி மாற்றங்கள் தற்காலிகமானவை மட்டுமே.",
        "Option B is incorrect.", "விருப்பம் B தவறானது.",
        "Option C is correct; strictly tied to the end of the financial year in which emergency ceases.", "விருப்பம் C சரியானது; அவசரநிலை முடிவடையும் நிதியாண்டின் இறுதி வரை மட்டுமே.",
        "Option D incorrectly introduces the Finance Commission as a ratifying body.", "விருப்பம் D நிதி ஆணையத்தை தவறாகக் குறிப்பிடுகிறது.",
        "TNPSC Article 354 Nuance: Financial modification order lapses at the end of the financial year in which the Emergency ends.",
        "TNPSC சரத்து 354 நுணுக்கம்: அவசரநிலை முடிவுக்கு வரும் நிதியாண்டின் முடிவில் நிதி மாற்ற உத்தரவு காலாவதியாகிவிடும்.",
        "This allows the Union to reallocate financial resources to defense and national security during crisis periods.",
        "நெருக்கடிக் காலங்களில் பாதுகாப்பு மற்றும் தேசியப் பாதுகாப்பிற்கு நிதி ஆதாரங்களை மறுபங்கீடு செய்ய இது மத்திய அரசுக்கு அனுமதியளிக்கிறது."
    ))

    # 016 - Key D
    qs.append(make_ep_q(
        PREFIX, 16, "Hard", "Fundamental Rights", "Article 358 Automatic Suspension Scope",
        "Which Fundamental Rights are automatically suspended under Article 358 as soon as a National Emergency is declared on the grounds of war or external aggression?",
        "போர் அல்லது வெளிநாட்டு ஆக்கிரமிப்பு காரணங்களின் அடிப்படையில் தேசிய அவசரநிலை அறிவிக்கப்பட்டவுடன், சரத்து 358-ன் கீழ் தானாகவே இடைநிறுத்தப்படும் அடிப்படை உரிமைகள் எவை?",
        "All Fundamental Rights in Part III", "பகுதி III-ல் உள்ள அனைத்து அடிப்படை உரிமைகளும்",
        "Articles 14, 19, 21, and 32", "சரத்துகள் 14, 19, 21 மற்றும் 32",
        "Articles 20 and 21 only", "சரத்துகள் 20 மற்றும் 21 மட்டுமே",
        "The six freedoms guaranteed under Article 19 only", "சரத்து 19-ன் கீழ் உத்தரவாதம் அளிக்கப்பட்ட ஆறு சுதந்திரங்கள் மட்டுமே",
        "D",
        "Article 358 deals strictly with the automatic suspension of the six Fundamental Rights guaranteed under Article 19. No other Fundamental Right is automatically suspended under Article 358.",
        "சரத்து 358 என்பது சரத்து 19-ன் கீழ் உத்தரவாதம் அளிக்கப்பட்ட ஆறு அடிப்படை உரிமைகளைத் தானாக இடைநிறுத்துவதை மட்டுமே கையாள்கிறது. பகுதி III-ன் வேறு எந்த அடிப்படை உரிமையும் சரத்து 358-ன் கீழ் தானாக இடைநிறுத்தப்படுவதில்லை.",
        "Option A is a widespread misconception; not all rights are suspended.", "விருப்பம் A ஒரு தவறான கருத்தாகும்; அனைத்து உரிமைகளும் இடைநிறுத்தப்படுவதில்லை.",
        "Option B includes Article 21 which can never be suspended.", "விருப்பம் B ஒருபோதும் இடைநிறுத்த முடியாத சரத்து 21-ஐக் கொண்டுள்ளது.",
        "Option C refers to rights that can NEVER be suspended.", "விருப்பம் C எக்காலத்திலும் இடைநிறுத்த முடியாத உரிமைகளைக் குறிக்கிறது.",
        "Option D is correct; strictly Article 19 alone.", "விருப்பம் D சரியானது; சரத்து 19 மட்டுமே.",
        "TNPSC Core Rule: Article 358 = Article 19 ONLY, and ONLY during War or External Aggression (External Emergency).",
        "TNPSC முக்கிய விதி: சரத்து 358 = சரத்து 19 மட்டுமே, மற்றும் போர் அல்லது வெளிநாட்டு ஆக்கிரமிப்பின் போது மட்டுமே.",
        "Under Article 358, as soon as the emergency ceases, Article 19 automatically revives with full force.",
        "அவசரநிலை முடிவுக்கு வந்தவுடன், சரத்து 19 தானாகவே முழு வீச்சுடன் மீண்டும் உயிர்பெறுகிறது."
    ))

    # 017 - Key A
    qs.append(make_ep_q(
        PREFIX, 17, "Hard", "Fundamental Rights", "Article 359 Presidential Order Mechanism",
        "Unlike Article 358, the suspension of the right to move courts for enforcement of Fundamental Rights under Article 359 requires which of the following?",
        "சரத்து 358 போல் அல்லாமல், சரத்து 359-ன் கீழ் அடிப்படை உரிமைகளைச் செயல்படுத்த நீதிமன்றத்தை நாடும் உரிமையை இடைநிறுத்த பின்வருவனவற்றில் எது அவசியமாகும்?",
        "A specific Presidential Order specifying the exact Fundamental Rights to be suspended", "இடைநிறுத்தப்பட வேண்டிய குறிப்பிட்ட அடிப்படை உரிமைகளைக் குறிப்பிடும் ஒரு தனித்துவமான குடியரசுத் தலைவர் ஆணை",
        "A constitutional amendment approved by special majority", "சிறப்புப் பெரும்பான்மையால் அங்கீகரிக்கப்பட்ட அரசியலமைப்பு திருத்தம்",
        "Prior concurring resolution passed by the Supreme Court", "உச்ச நீதிமன்றம் நிறைவேற்றும் முன் ஒப்புதல் தீர்மானம்",
        "A referendum approved by a majority of Indian voters", "இந்திய வாக்காளர்களின் பெரும்பான்மையால் அங்கீகரிக்கப்பட்ட பொது வாக்கெடுப்பு",
        "A",
        "Under Article 359(1), the suspension of the right to move any court for the enforcement of Fundamental Rights does not occur automatically; it requires a specific Presidential Order specifying the precise rights suspended (excluding Articles 20 and 21).",
        "சரத்து 359(1)-ன் கீழ், அடிப்படை உரிமைகளைச் செயல்படுத்த நீதிமன்றத்தை நாடும் உரிமை தானாக இடைநிறுத்தப்படுவதில்லை; அதற்கு இடைநிறுத்தப்படும் குறிப்பிட்ட உரிமைகளைக் குறிப்பிடும் குடியரசுத் தலைவரின் வெளிப்படையான ஆணை தேவைப்படுகிறது (சரத்துகள் 20 மற்றும் 21 நீங்கலாக).",
        "Option A is correct; Presidential Order is constitutionally mandated under Article 359.", "விருப்பம் A சரியானது; சரத்து 359-ன் கீழ் குடியரசுத் தலைவரின் ஆணை அவசியமாகும்.",
        "Option B is incorrect; no constitutional amendment is required.", "விருப்பம் B தவறு; அரசியலமைப்பு திருத்தம் தேவையில்லை.",
        "Option C is incorrect; judicial concurrence is not required.", "விருப்பம் C தவறு; நீதித்துறையின் ஒப்புதல் தேவையில்லை.",
        "Option D has no place in Indian constitutional jurisprudence.", "விருப்பம் D இந்திய அரசியலமைப்பில் இல்லாத ஒன்று.",
        "Contrast 358 vs 359: Article 358 is AUTOMATIC (Art 19 only); Article 359 requires a PRESIDENTIAL ORDER (specified rights).",
        "358 vs 359 வேறுபாடு: சரத்து 358 தானியங்கியாகச் செயல்படும் (சரத்து 19 மட்டுமே); சரத்து 359-க்கு குடியரசுத் தலைவர் ஆணை தேவை (குறிப்பிட்ட உரிமைகள்).",
        "Every order made under Article 359 must be laid before each House of Parliament as soon as may be after it is made.",
        "சரத்து 359-ன் கீழ் பிறப்பிக்கப்படும் ஒவ்வொரு ஆணையும் இயற்றப்பட்ட பின்னர் விரைவில் பாராளுமன்றத்தின் இரு அவைகளின் முன்பும் வைக்கப்பட வேண்டும்."
    ))

    # 018 - Key B
    qs.append(make_ep_q(
        PREFIX, 18, "Medium", "Fundamental Rights", "Non-derogable Articles 20 and 21",
        "Which Constitutional Amendment Act explicitly prohibited the President from suspending the enforcement of Articles 20 and 21 under Article 359?",
        "சரத்து 359-ன் கீழ் சரத்துகள் 20 மற்றும் 21-ஐச் செயல்படுத்துவதை குடியரசுத் தலைவர் இடைநிறுத்துவதை வெளிப்படையாகத் தடை செய்த அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "42nd Constitutional Amendment Act, 1976", "42-வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
        "44th Constitutional Amendment Act, 1978", "44-வது அரசியலமைப்பு திருத்தச் சட்டம், 1978",
        "43rd Constitutional Amendment Act, 1977", "43-வது அரசியலமைப்பு திருத்தச் சட்டம், 1977",
        "52nd Constitutional Amendment Act, 1985", "52-வது அரசியலமைப்பு திருத்தச் சட்டம், 1985",
        "B",
        "The 44th Constitutional Amendment Act of 1978 amended Article 359 to provide that the right to move courts for the enforcement of Fundamental Rights guaranteed by Article 20 (protection against conviction) and Article 21 (right to life and personal liberty) CANNOT be suspended even during an emergency.",
        "1978-ன் 44-வது அரசியலமைப்பு திருத்தச் சட்டம் சரத்து 359-ஐத் திருத்தி, சரத்து 20 (குற்றங்களுக்கான தண்டனைக்கு எதிரான பாதுகாப்பு) மற்றும் சரத்து 21 (வாழ்வுரிமை மற்றும் தனிநபர் சுதந்திரம்) ஆகியவற்றைச் செயல்படுத்த நீதிமன்றங்களை நாடும் உரிமையை அவசரநிலையின் போதும் கூட இடைநிறுத்த முடியாது எனத் தெளிவுபடுத்தியது.",
        "Option A (42nd CAA) actually expanded executive emergency powers.", "விருப்பம் A (42-வது திருத்தம்) அவசரநிலை அதிகாரங்களை அதிகரித்தது.",
        "Option B is correct; 44th CAA enacted this historic shield.", "விருப்பம் B சரியானது; 44-வது திருத்தச் சட்டம் இந்த வரலாற்றுப் பாதுகாப்பை இயற்றியது.",
        "Option C dealt with other post-emergency remedial provisions.", "விருப்பம் C பிற திருத்தங்களைக் கையாண்டது.",
        "Option D is the Anti-Defection Law (10th Schedule).", "விருப்பம் D கட்சித் தாவல் தடைச் சட்டம் (10-வது அட்டவணை).",
        "TNPSC Golden Rule: Articles 20 and 21 are NON-DEROGABLE; they can never be suspended under any emergency.",
        "TNPSC பொன் விதி: சரத்துகள் 20 மற்றும் 21 பறிக்க முடியாதவை; எந்தவொரு அவசரநிலையிலும் அவை இடைநிறுத்தப்பட முடியாது.",
        "This amendment was specifically designed to overturn the catastrophic majority verdict in ADM Jabalpur (1976).",
        "ஏ.டி.எம். ஜபல்பூர் (1976) வழக்கில் பெரும்பான்மை வழங்கிய பேரழிவுத் தீர்ப்பை மாற்றியமைக்கவே இந்தத் திருத்தம் கொண்டுவரப்பட்டது."
    ))

    # 019 - Key C
    qs.append(make_ep_q(
        PREFIX, 19, "Hard", "Judicial Review", "Minerva Mills Judgment on Article 352",
        "In which landmark case did the Supreme Court explicitly rule that the proclamation of a National Emergency under Article 352 is subject to judicial review?",
        "சரத்து 352-ன் கீழான தேசிய அவசரநிலைப் பிரகடனம் நீதித்துறை மறுஆய்வுக்கு உட்பட்டது என்று உச்ச நீதிமன்றம் எந்த மைல்கல் வழக்கில் வெளிப்படையாகத் தீர்ப்பளித்தது?",
        "Golaknath v. State of Punjab (1967)", "கோலக்நாத் எதிர் பஞ்சாப் மாநிலம் (1967)",
        "Kesavananda Bharati v. State of Kerala (1973)", "கேசவானந்த பாரதி எதிர் கேரள மாநிலம் (1973)",
        "Minerva Mills v. Union of India (1980)", "மினர்வா மில்ஸ் எதிர் மத்திய அரசு (1980)",
        "Maneka Gandhi v. Union of India (1978)", "மேனகா காந்தி எதிர் மத்திய அரசு (1978)",
        "C",
        "In Minerva Mills v. Union of India (1980), the Supreme Court held that the proclamation of a National Emergency under Article 352 can be challenged in court on the grounds of mala fides, or that the declaration was based on wholly extraneous and irrelevant facts.",
        "மினர்வா மில்ஸ் எதிர் மத்திய அரசு (1980) வழக்கில், தவறான உள்நோக்கம் (mala fides) அல்லது முற்றிலும் தொடர்பற்ற புறம்பான உண்மைகளின் அடிப்படையில் அவசரநிலை அறிவிக்கப்பட்டது என்ற காரணங்களுக்காக சரத்து 352-ன் கீழான தேசிய அவசரநிலைப் பிரகடனத்தை நீதிமன்றத்தில் சவாலுக்கு உட்படுத்தலாம் என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
        "Option A dealt with fundamental rights amenability under Article 368.", "விருப்பம் A சரத்து 368-ன் திருத்தும் வரம்பு தொடர்பானது.",
        "Option B established the Basic Structure Doctrine.", "விருப்பம் B அடிப்படைக் கட்டமைப்பு கோட்பாட்டை நிறுவியது.",
        "Option C is correct; Minerva Mills (1980) confirmed judicial review of Article 352.", "விருப்பம் C சரியானது; மினர்வா மில்ஸ் (1980) சரத்து 352-ன் நீதி மறுஆய்வை உறுதிப்படுத்தியது.",
        "Option D revolutionized Article 21 due process.", "விருப்பம் D சரத்து 21-ன் நியாயமான நடைமுறையை புரட்சிகரமாக்கியது.",
        "Emergency Landmark: Minerva Mills (1980) confirmed Article 352 judicial review; S.R. Bommai (1994) confirmed Article 356 judicial review.",
        "அவசரநிலை மைல்கல்: மினர்வா மில்ஸ் (1980) சரத்து 352-ன் நீதி மறுஆய்வை உறுதி செய்தது; எஸ்.ஆர். பொம்மை (1994) சரத்து 356-ன் நீதி மறுஆய்வை உறுதி செய்தது.",
        "The Supreme Court observed that the power to declare emergency is not an unguided or unlimited executive discretion.",
        "அவசரநிலையை அறிவிக்கும் அதிகாரம் வழிகாட்டப்படாத அல்லது வரம்பற்ற நிர்வாக விருப்ப அதிகாரம் அல்ல என்று உச்ச நீதிமன்றம் குறிப்பிட்டது."
    ))

    # 020 - Key D
    qs.append(make_ep_q(
        PREFIX, 20, "Medium", "Grounds for President's Rule", "Articles 356 and 365 Interconnection",
        "President's Rule can be imposed in a State under Article 356 or which other Article of the Indian Constitution?",
        "மாநிலத்தில் குடியரசுத் தலைவர் ஆட்சி சரத்து 356 அல்லது இந்திய அரசியலமைப்பின் வேறு எந்தச் சரத்தின் கீழ் விதிக்கப்படலாம்?",
        "Article 352", "சரத்து 352",
        "Article 355", "சரத்து 355",
        "Article 358", "சரத்து 358",
        "Article 365", "சரத்து 365",
        "D",
        "A proclamation under Article 356 can be based on two constitutional grounds: (1) Article 356 itself (failure of constitutional machinery), and (2) Article 365 (failure of the State to comply with or give effect to lawful executive directions of the Union).",
        "சரத்து 356-ன் கீழான பிரகடனம் இரண்டு அரசியலமைப்பு காரணங்களின் அடிப்படையில் இருக்கலாம்: (1) சரத்து 356 (அரசியலமைப்பு இயந்திரத்தின் தோல்வி), மற்றும் (2) சரத்து 365 (மத்திய அரசின் சட்டப்பூர்வ நிர்வாக வழிகாட்டுதல்களை மாநில அரசு பின்பற்றத் தவறுதல்).",
        "Option A deals with National Emergency.", "விருப்பம் A தேசிய அவசரநிலையைக் கையாள்கிறது.",
        "Option B sets out the duty of the Union to protect states, but is not the operational trigger.", "விருப்பம் B மத்திய அரசின் கடமையை விவரிக்கிறது.",
        "Option C deals with suspension of Article 19.", "விருப்பம் C சரத்து 19 இடைநிறுத்தத்தைக் கையாள்கிறது.",
        "Option D is correct; Article 365 directly triggers Article 356 imposition.", "விருப்பம் D சரியானது; சரத்து 365 நேரடியாக சரத்து 356-ஐத் தூண்டுகிறது.",
        "TNPSC Core Linkage: Article 365 creates a legal fiction of constitutional breakdown when a state defies Union directions, enabling Article 356.",
        "TNPSC முக்கிய இணைப்பு: ஒரு மாநிலம் மத்திய வழிகாட்டுதல்களை மீறும் போது, அரசியலமைப்பு முறிந்துவிட்டது என்ற சட்டப்பூர்வ நிலையை சரத்து 365 உருவாக்கி, சரத்து 356-க்கு வழிவகுக்கிறது.",
        "Article 365 states: 'Where any State has failed to comply with any directions given in the exercise of the executive power of the Union, it shall be lawful for the President to hold that a situation has arisen in which the government of the State cannot be carried on in accordance with the provisions of this Constitution.'",
        "சரத்து 365 கூறுகிறது: மத்திய அரசின் நிர்வாக வழிகாட்டுதல்களை ஒரு மாநிலம் பின்பற்றத் தவறினால், அந்த மாநில அரசு அரசியலமைப்பு விதிகளின்படி இயங்க முடியாத சூழ்நிலை ஏற்பட்டுள்ளது எனக் குடியரசுத் தலைவர் கருதுவது சட்டப்பூர்வமானதாகும்."
    ))

    # 021 - Key A
    qs.append(make_ep_q(
        PREFIX, 21, "Medium", "Procedural", "Article 356 Parliamentary Approval Deadline",
        "A proclamation imposing President's Rule under Article 356 must be approved by both Houses of Parliament within what period from its issue?",
        "சரத்து 356-ன் கீழ் குடியரசுத் தலைவர் ஆட்சியை விதிக்கும் பிரகடனம் வெளியிடப்பட்டதிலிருந்து எத்தனை காலத்திற்குள் பாராளுமன்றத்தின் இரு அவைகளாலும் அங்கீகரிக்கப்பட வேண்டும்?",
        "Within two months", "இரண்டு மாதங்களுக்குள்",
        "Within one month", "ஒரு மாதத்திற்குள்",
        "Within fourteen days", "பதினான்கு நாட்களுக்குள்",
        "Within six months", "ஆறு மாதங்களுக்குள்",
        "A",
        "Under Article 356(3), every proclamation imposing President's Rule must be laid before both Houses of Parliament and ceases to operate at the expiration of two months unless approved by resolutions of both Houses.",
        "சரத்து 356(3)-ன் கீழ், குடியரசுத் தலைவர் ஆட்சியை விதிக்கும் ஒவ்வொரு பிரகடனமும் பாராளுமன்றத்தின் இரு அவைகளிலும் வைக்கப்பட வேண்டும், மேலும் இரு அவைகளின் தீர்மானங்களால் அங்கீகரிக்கப்படாவிட்டால் இரண்டு மாதங்களின் முடிவில் அது காலாவதியாகிவிடும்.",
        "Option A is correct; two months under Article 356(3).", "விருப்பம் A சரியானது; சரத்து 356(3)-ன் கீழ் இரண்டு மாதங்கள்.",
        "Option B (1 month) is the deadline strictly for Article 352 National Emergency.", "விருப்பம் B (1 மாதம்) சரத்து 352 தேசிய அவசரநிலைக்கு மட்டுமே பொருந்தும்.",
        "Option C (14 days) is for disapproval special sittings.", "விருப்பம் C (14 நாட்கள்) நிராகரிப்பு சிறப்புக் கூட்டங்களுக்கானது.",
        "Option D (6 months) is the operational duration once approved.", "விருப்பம் D (6 மாதங்கள்) ஒப்புதல் பெற்ற பின் செயல்படும் காலமாகும்.",
        "Approval Timeline Rule: Article 352 = 1 Month; Article 356 = 2 Months; Article 360 = 2 Months.",
        "ஒப்புதல் காலக்கெடு விதி: சரத்து 352 = 1 மாதம்; சரத்து 356 = 2 மாதங்கள்; சரத்து 360 = 2 மாதங்கள்.",
        "If Lok Sabha is dissolved during the two months, Rajya Sabha must approve within two months, and the new Lok Sabha within 30 days of its first sitting.",
        "இரண்டு மாத காலத்திற்குள் மக்களவை கலைக்கப்பட்டால், மாநிலங்களவை 2 மாதங்களில் ஒப்புதல் அளிக்க வேண்டும், மேலும் புதிய மக்களவை அதன் முதல் கூட்டத்திலிருந்து 30 நாட்களுக்குள் ஒப்புதல் அளிக்க வேண்டும்."
    ))

    # 022 - Key B
    qs.append(make_ep_q(
        PREFIX, 22, "Medium", "Procedural", "Article 356 Voting Majority",
        "What type of majority is required in Parliament to pass a resolution approving the imposition of President's Rule under Article 356?",
        "சரத்து 356-ன் கீழ் குடியரசுத் தலைவர் ஆட்சியை விதிப்பதை அங்கீகரிக்கும் தீர்மானத்தை நிறைவேற்ற பாராளுமன்றத்தில் எந்த வகையான பெரும்பான்மை தேவைப்படுகிறது?",
        "Special majority in both Houses", "இரு அவைகளிலும் சிறப்புப் பெரும்பான்மை",
        "Simple majority of members present and voting in each House", "ஒவ்வொரு அவையிலும் வருகை தந்து வாக்களிக்கும் உறுப்பினர்களில் எளிய பெரும்பான்மை",
        "Absolute majority of the total membership of both Houses", "இரு அவைகளின் மொத்த உறுப்பினர்களில் முழுமையான பெரும்பான்மை",
        "Simple majority of the Lok Sabha alone", "மக்களவையின் எளிய பெரும்பான்மை மட்டுமே",
        "B",
        "Under Article 356(3), a resolution approving the proclamation of President's Rule can be passed by either House of Parliament only by a simple majority, that is, a majority of the members of that House present and voting.",
        "சரத்து 356(3)-ன் கீழ், குடியரசுத் தலைவர் ஆட்சிப் பிரகடனத்திற்கு ஒப்புதல் அளிக்கும் தீர்மானம் பாராளுமன்றத்தின் இரு அவைகளிலும் வருகை தந்து வாக்களிக்கும் உறுப்பினர்களில் எளிய பெரும்பான்மையால் (simple majority) மட்டுமே நிறைவேற்றப்பட முடியும்.",
        "Option A describes Article 352 approval post-1978.", "விருப்பம் A 1978-க்குப் பிந்தைய சரத்து 352 ஒப்புதலை விவரிக்கிறது.",
        "Option B is correct; simple majority governs Article 356.", "விருப்பம் B சரியானது; எளிய பெரும்பான்மையே சரத்து 356-ஐ நிர்வகிக்கிறது.",
        "Option C is not the standard required.", "விருப்பம் C தேவையான தரநிலை அல்ல.",
        "Option D is wrong because Rajya Sabha must also approve.", "விருப்பம் D தவறு, ஏனெனில் மாநிலங்களவையும் ஒப்புதல் அளிக்க வேண்டும்.",
        "Key Distinction: Article 352 requires Special Majority; Article 356 requires only Simple Majority.",
        "முக்கிய வேறுபாடு: சரத்து 352-க்கு சிறப்புப் பெரும்பான்மை தேவை; சரத்து 356-க்கு எளிய பெரும்பான்மை மட்டுமே தேவை.",
        "The 44th CAA raised Article 352 to special majority, but deliberately retained simple majority for Article 356.",
        "44-வது திருத்தம் சரத்து 352-ஐ சிறப்புப் பெரும்பான்மையாக உயர்த்திய போதும், சரத்து 356-க்கு எளிய பெரும்பான்மையையே தக்கவைத்தது."
    ))

    # 023 - Key C
    qs.append(make_ep_q(
        PREFIX, 23, "Hard", "Constitutional Ceilings", "Maximum Normal Limit of President's Rule",
        "Under normal circumstances and subject to periodic six-month parliamentary renewals, what is the maximum permissible duration for President's Rule in a State under Article 356?",
        "இயல்பான சூழ்நிலைகளில் மற்றும் ஆறு மாத காலமுறை பாராளுமன்றப் புதுப்பித்தலுக்கு உட்பட்டு, சரத்து 356-ன் கீழ் ஒரு மாநிலத்தில் குடியரசுத் தலைவர் ஆட்சி அதிகபட்சமாக எவ்வளவு காலம் வரை நீடிக்கலாம்?",
        "One year", "ஒரு வருடம்",
        "Two years", "இரண்டு ஆண்டுகள்",
        "Three years", "மூன்று ஆண்டுகள்",
        "Indefinitely like National Emergency", "தேசிய அவசரநிலை போல காலவரையின்றி",
        "C",
        "Under the proviso to Article 356(4), no proclamation of President's Rule shall in any case remain in force for more than three years. Beyond three years, it can be extended ONLY by a constitutional amendment enacted under Article 368.",
        "சரத்து 356(4)-ன் வரம்புரையின் கீழ், எந்தவொரு சூழ்நிலையிலும் குடியரசுத் தலைவர் ஆட்சி மூன்று ஆண்டுகளுக்கு மேல் தொடர்ந்து செயல்பாட்டில் இருக்க முடியாது. மூன்று ஆண்டுகளுக்கு மேல் நீட்டிக்க வேண்டுமானால் சரத்து 368-ன் கீழ் அரசியலமைப்பு திருத்தம் மட்டுமே செய்யப்பட வேண்டும்.",
        "Option A is the threshold beyond which special conditions apply under Article 356(5).", "விருப்பம் A என்பது சரத்து 356(5)-ன் கீழ் சிறப்பு நிபந்தனைகள் தொடங்கும் கால வரம்பாகும்.",
        "Option B is not a constitutional ceiling.", "விருப்பம் B அரசியலமைப்பு உச்சவரம்பு அல்ல.",
        "Option C is correct; three years is the ultimate constitutional ceiling under Article 356(4).", "விருப்பம் C சரியானது; மூன்று ஆண்டுகளே சரத்து 356(4)-ன் கீழான இறுதி அரசியலமைப்பு உச்சவரம்பாகும்.",
        "Option D describes National Emergency, not President's Rule.", "விருப்பம் D தேசிய அவசரநிலையை விவரிக்கிறது.",
        "TNPSC Standard Fact: Maximum duration of President's Rule = 3 years (except Punjab where it was extended to 5 years via amendments).",
        "TNPSC நிலையான உண்மை: குடியரசுத் தலைவர் ஆட்சியின் அதிகபட்ச கால அளவு = 3 ஆண்டுகள் (பஞ்சாப் விதிவிலக்கு, அங்கு திருத்தங்கள் மூலம் 5 ஆண்டுகள் வரை நீட்டிக்கப்பட்டது).",
        "The 44th Amendment Act introduced strict controls for extending President's Rule beyond one year within this three-year ceiling.",
        "இந்த 3 ஆண்டு உச்சவரம்பிற்குள்ளேயே, ஒரு வருடத்திற்கு மேல் நீட்டிப்பதற்கு 44-வது திருத்தச் சட்டம் கடுமையான கட்டுப்பாடுகளை அறிமுகப்படுத்தியது."
    ))

    # 024 - Key D
    qs.append(make_ep_q(
        PREFIX, 24, "Hard", "Constitutional Safeguards", "Article 356 Beyond One Year Conditions",
        "Under Article 356(5), President's Rule can be extended beyond one year only if which two conditions are simultaneously satisfied?",
        "சரத்து 356(5)-ன் கீழ், எந்த இரண்டு நிபந்தனைகளும் ஒரே நேரத்தில் பூர்த்தியானால் மட்டுமே குடியரசுத் தலைவர் ஆட்சியை ஒரு வருடத்திற்கு மேல் நீட்டிக்க முடியும்?",
        "State Governor recommends it AND High Court certifies it", "மாநில ஆளுநர் பரிந்துரைக்க வேண்டும் மற்றும் உயர் நீதிமன்றம் சான்றளிக்க வேண்டும்",
        "Financial Emergency is in operation AND Supreme Court approves", "நிதி அவசரநிலை செயல்பாட்டில் இருக்க வேண்டும் மற்றும் உச்ச நீதிமன்றம் ஒப்புதல் அளிக்க வேண்டும்",
        "Two-thirds of State Assembly members petition the President AND Rajya Sabha consents", "மாநில சட்டமன்ற உறுப்பினர்களில் 2/3 பங்கு குடியரசுத் தலைவரிடம் மனு அளிக்க வேண்டும் மற்றும் மாநிலங்களவை சம்மதிக்க வேண்டும்",
        "National Emergency is in operation in whole or part of the state AND Election Commission certifies difficulty in holding general elections", "மாநிலத்தின் முழு பகுதியிலோ அல்லது பகுதியிலோ தேசிய அவசரநிலை செயல்பட வேண்டும் மற்றும் பொதுத்தேர்தல் நடத்துவதில் சிரமம் உள்ளதாக தேர்தல் ஆணையம் சான்றளிக்க வேண்டும்",
        "D",
        "Article 356(5), inserted by the 44th CAA 1978, provides two stringent conditions for extending President's Rule beyond one year: (1) A National Emergency must be in operation in the whole of India or any part of the State, and (2) The Election Commission must certify that holding general elections to the Legislative Assembly is difficult.",
        "1978-ன் 44-வது திருத்தத்தால் சேர்க்கப்பட்ட சரத்து 356(5) ஒரு வருடத்திற்கு மேல் நீட்டிக்க இரண்டு கடுமையான நிபந்தனைகளை விதிக்கிறது: (1) இந்தியா முழுவதிலும் அல்லது மாநிலத்தின் ஏதேனும் ஒரு பகுதியிலும் தேசிய அவசரநிலை செயல்பாட்டில் இருக்க வேண்டும், மற்றும் (2) மாநில சட்டமன்றத்திற்கு பொதுத்தேர்தல் நடத்துவது கடினம் என்று தேர்தல் ஆணையம் சான்றளிக்க வேண்டும்.",
        "Option A is incorrect; High Court has no role in certifying elections.", "விருப்பம் A தவறு; உயர் நீதிமன்றத்திற்குத் தேர்தல் சான்றளிக்கும் பங்கு இல்லை.",
        "Option B is incorrect; Financial Emergency does not satisfy this clause.", "விருப்பம் B தவறு; நிதி அவசரநிலை இதற்குப் பொருந்தாது.",
        "Option C is incorrect; assembly petition has no constitutional relevance.", "விருப்பம் C தவறு; சட்டமன்ற மனுவிற்கு அரசியலமைப்பு தொடர்பு இல்லை.",
        "Option D is correct; National Emergency + Election Commission Certificate.", "விருப்பம் D சரியானது; தேசிய அவசரநிலை + தேர்தல் ஆணைய சான்றிதழ்.",
        "TNPSC High-Yield Rule: Beyond 1 year, Article 356 requires BOTH National Emergency + Election Commission Certificate.",
        "TNPSC உயர்-விளைச்சல் விதி: 1 வருடத்திற்கு மேல் சரத்து 356 நீடிக்க தேசிய அவசரநிலை + தேர்தல் ஆணைய சான்றிதழ் இரண்டும் கட்டாயம்.",
        "These twin conditions effectively shut down the executive loophole of arbitrarily prolonging President's Rule in states.",
        "மாநிலங்களில் குடியரசுத் தலைவர் ஆட்சியைத் தன்னிச்சையாக நீட்டிக்கும் நிர்வாகத் துஷ்பிரயோகத்தை இந்த இரட்டை நிபந்தனைகள் திறம்படத் தடுத்தன."
    ))

    # 025 - Key A
    qs.append(make_ep_q(
        PREFIX, 25, "Hard", "Constitutional Impact", "High Court Powers under Article 356",
        "What is the constitutional status of the State High Court during the operation of President's Rule under Article 356?",
        "சரத்து 356-ன் கீழான குடியரசுத் தலைவர் ஆட்சியின் போது மாநில உயர் நீதிமன்றத்தின் அரசியலமைப்பு நிலை என்ன?",
        "Its powers and jurisdiction are completely unaffected, and the President cannot assume any power vested in the High Court", "அதன் அதிகாரங்களும் அதிகார வரம்பும் முற்றிலும் பாதிக்கப்படாது, மேலும் உயர் நீதிமன்றத்திற்குரிய எந்தவொரு அதிகாரத்தையும் குடியரசுத் தலைவர் தன்வசம் ஏற்றுக்கொள்ள முடியாது",
        "The High Court is placed under the direct administrative control of the Union Law Ministry", "உயர் நீதிமன்றம் மத்திய சட்ட அமைச்சகத்தின் நேரடி நிர்வாகக் கட்டுப்பாட்டின் கீழ் கொண்டுவரப்படுகிறது",
        "The President can suspend High Court writ jurisdiction under Article 226", "சரத்து 226-ன் கீழான உயர் நீதிமன்ற நீதிப்பேராணை அதிகார வரம்பை குடியரசுத் தலைவர் இடைநிறுத்த முடியும்",
        "The Chief Justice of the High Court assumes the post of Governor automatically", "உயர் நீதிமன்றத் தலைமை நீதிபதி தானாகவே ஆளுநர் பதவியை ஏற்றுக்கொள்கிறார்",
        "A",
        "Under the proviso to Article 356(1), nothing in the proclamation shall authorize the President to assume to himself any of the powers vested in or exercisable by a High Court, or to suspend in whole or in part the operation of any provision of the Constitution relating to High Courts. The High Court continues to function completely independently.",
        "சரத்து 356(1)-ன் வரம்புரையின் கீழ், பிரகடனத்தில் உள்ள எதுவும் உயர் நீதிமன்றத்திற்கு வழங்கப்பட்ட அல்லது அதனால் செயல்படுத்தக்கூடிய எந்தவொரு அதிகாரத்தையும் குடியரசுத் தலைவர் தன்வசம் எடுத்துக்கொள்ளவோ அல்லது உயர் நீதிமன்றங்கள் தொடர்பான அரசியலமைப்பு விதிகளை இடைநிறுத்தவோ அனுமதியளிக்காது. உயர் நீதிமன்றம் முற்றிலும் சுதந்திரமாகத் தொடர்ந்து இயங்குகிறது.",
        "Option A is correct; High Court powers are constitutionally inviolable under Article 356.", "விருப்பம் A சரியானது; சரத்து 356-ன் கீழ் உயர் நீதிமன்ற அதிகாரங்கள் அரசியலமைப்பு ரீதியாக மீற முடியாதவை.",
        "Option B is false; judiciary remains separate and independent under Article 50.", "விருப்பம் B தவறு; நீதித்துறை சுதந்திரமாக நீடிக்கிறது.",
        "Option C is false; President's Rule cannot touch Article 226 writ powers.", "விருப்பம் C தவறு; குடியரசுத் தலைவர் ஆட்சி சரத்து 226 நீதிப்பேராணை அதிகாரங்களைத் தொட முடியாது.",
        "Option D is incorrect.", "விருப்பம் D தவறானது.",
        "Golden Rule of Article 356: The President can take over State Government and Governor powers, but CANNOT touch High Court powers.",
        "சரத்து 356-ன் பொன் விதி: குடியரசுத் தலைவர் மாநில அரசு மற்றும் ஆளுநர் அதிகாரங்களை ஏற்கலாம், ஆனால் உயர் நீதிமன்ற அதிகாரங்களைத் தொட முடியாது.",
        "This ensures that citizens retain their constitutional remedy to challenge arbitrary executive actions even during President's Rule.",
        "குடியரசுத் தலைவர் ஆட்சியின் போதும் தன்னிச்சையான நிர்வாக நடவடிக்கைகளை எதிர்த்து வழக்கு தொடரும் அரசியலமைப்பு தீர்வை இது குடிமக்களுக்கு உறுதி செய்கிறது."
    ))

    return qs

print("Batch 1 (Q001-Q025) ready.")
