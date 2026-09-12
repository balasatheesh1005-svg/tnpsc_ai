# -*- coding: utf-8 -*-
"""
Generator for Emergency Provisions PYQ & Exam Trend MCQs (50 questions: EP_PYQ_001 to EP_PYQ_050)
Strictly adheres to:
1. 24-field schema verified by ContentValidator
2. Bilingual parity (English and Tamil)
3. Balanced answer distribution: A: 12, B: 13, C: 13, D: 12 (Total: 50)
4. Full coverage of authentic TNPSC Group 1, Group 2, Group 4 & UPSC PYQ trends
"""

import json
import os
from collections import Counter
from ep_mcq_helper import make_ep_q
from tools.nova_content_engine.validator import ContentValidator

PREFIX = "EP_PYQ_"
DIFF = "Medium"

def get_pyq_questions_batch1():
    qs = []

    # 001 - Key A
    qs.append(make_ep_q(
        PREFIX, 1, DIFF, "PYQ MCQ", "Constitutional Part",
        "In which Part of the Constitution of India are the Emergency Provisions contained? [TNPSC Group 1 2011, 2014]",
        "இந்திய அரசியலமைப்பின் எந்தப் பகுதியில் அவசரநிலைப் பிரிவுகள் இடம்பெற்றுள்ளன? [TNPSC குரூப் 1 2011, 2014]",
        "Part XVIII", "பகுதி XVIII",
        "Part XVII", "பகுதி XVII",
        "Part XVI", "பகுதி XVI",
        "Part XIX", "பகுதி XIX",
        "A",
        "Emergency Provisions are embodied in Part XVIII of the Constitution of India from Articles 352 to 360.",
        "இந்திய அரசியலமைப்பின் பகுதி XVIII-ல் சரத்துகள் 352 முதல் 360 வரை அவசரநிலைப் பிரிவுகள் விவரிக்கப்பட்டுள்ளன.",
        "Option A is correct; Part XVIII contains Emergency Provisions.", "விருப்பம் A சரியானது; பகுதி XVIII அவசரநிலைப் பிரிவுகளைக் கொண்டுள்ளது.",
        "Option B contains Part XVII (Official Language).", "விருப்பம் B பகுதி XVII (ஆட்சி மொழி) தொடர்பானது.",
        "Option C contains Part XVI (Special Provisions for Certain Classes).", "விருப்பம் C பகுதி XVI (குறிப்பிட்ட வகுப்பினருக்கான சிறப்பு விதிகள்) தொடர்பானது.",
        "Option D contains Part XIX (Miscellaneous provisions).", "விருப்பம் D பகுதி XIX (இதர விதிகள்) தொடர்பானது.",
        "PYQ Trend: TNPSC frequently tests Roman numerals for Constitutional Parts. Part XVIII = 18 = Emergency.",
        "PYQ போக்கு: TNPSC அடிக்கடி அரசியலமைப்பு பகுதிகளின் ரோமன் எண்களைக் கேட்கிறது. பகுதி XVIII = 18 = அவசரநிலை.",
        "Articles 352 to 360 form an integrated chapter dealing with external, constitutional, and financial crises.",
        "சரத்துகள் 352 முதல் 360 வரை வெளிப்புற, அரசியலமைப்பு மற்றும் நிதி நெருக்கடிகளைக் கையாளும் ஒரு ஒருங்கிணைந்த அத்தியாயத்தை உருவாக்குகின்றன."
    ))

    # 002 - Key B
    qs.append(make_ep_q(
        PREFIX, 2, DIFF, "PYQ MCQ", "Grounds for National Emergency",
        "Under Article 352 of the Indian Constitution, the President can proclaim a National Emergency on the grounds of: [TNPSC Group 2 2015, UPSC 2002]",
        "இந்திய அரசியலமைப்பின் சரத்து 352-ன் கீழ், குடியரசுத் தலைவர் எதன் அடிப்படையில் தேசிய அவசரநிலையைப் பிரகடனம் செய்ய முடியும்? [TNPSC குரூப் 2 2015, UPSC 2002]",
        "War, External Aggression, or Internal Disturbance", "போர், வெளிநாட்டு ஆக்கிரமிப்பு அல்லது உள்நாட்டு அமைதியின்மை",
        "War, External Aggression, or Armed Rebellion", "போர், வெளிநாட்டு ஆக்கிரமிப்பு அல்லது ஆயுதமேந்திய கிளர்ச்சி",
        "War, Armed Rebellion, or Financial Instability", "போர், ஆயுதமேந்திய கிளர்ச்சி அல்லது நிதி உறுதியற்ற தன்மை",
        "External Aggression, Insurgency, or Civil War", "வெளிநாட்டு ஆக்கிரமிப்பு, கிளர்ச்சி அல்லது உள்நாட்டுப் போர்",
        "B",
        "Under Article 352(1), the President can declare a National Emergency on grounds of War, External Aggression, or Armed Rebellion.",
        "சரத்து 352(1)-ன் கீழ், போர், வெளிநாட்டு ஆக்கிரமிப்பு அல்லது ஆயுதமேந்திய கிளர்ச்சி ஆகிய காரணங்களின் அடிப்படையில் குடியரசுத் தலைவர் தேசிய அவசரநிலையை அறிவிக்க முடியும்.",
        "Option A was the original ground prior to the 44th Amendment Act, 1978.", "விருப்பம் A என்பது 1978-ஆம் ஆண்டின் 44-வது திருத்தத்திற்கு முந்தைய மூலக் காரணமாகும்.",
        "Option B is correct; 'Armed Rebellion' replaced 'Internal Disturbance' in 1978.", "விருப்பம் B சரியானது; 1978-ல் 'உள்நாட்டு அமைதியின்மை' என்பதற்குப் பதிலாக 'ஆயுதமேந்திய கிளர்ச்சி' சேர்க்கப்பட்டது.",
        "Option C includes financial instability which pertains to Article 360.", "விருப்பம் C சரத்து 360-க்குரிய நிதி உறுதியற்ற தன்மையைக் கொண்டுள்ளது.",
        "Option D includes non-constitutional terms like civil war and insurgency.", "விருப்பம் D உள்நாட்டுப் போர் போன்ற அரசியலமைப்பில் இல்லாத சொற்களைக் கொண்டுள்ளது.",
        "TNPSC Favorite: 'Internal Disturbance' was replaced by 'Armed Rebellion' by the 44th CAA 1978.",
        "TNPSC விருப்பம்: 1978-ன் 44-வது திருத்தச் சட்டத்தால் 'உள்நாட்டு அமைதியின்மை' என்ற சொல் 'ஆயுதமேந்திய கிளர்ச்சி' என மாற்றப்பட்டது.",
        "External emergency is declared on grounds of war or external aggression, while internal emergency is on armed rebellion.",
        "போர் அல்லது வெளிநாட்டு ஆக்கிரமிப்பு அடிப்படையில் வெளிப்புற அவசரநிலையும், ஆயுதமேந்திய கிளர்ச்சி அடிப்படையில் உள்நாட்டு அவசரநிலையும் அறிவிக்கப்படுகிறது."
    ))

    # 003 - Key C
    qs.append(make_ep_q(
        PREFIX, 3, DIFF, "PYQ MCQ", "44th Amendment Safeguards",
        "Which Constitutional Amendment Act substituted the phrase 'Armed Rebellion' for 'Internal Disturbance' in Article 352? [TNPSC Group 1 2017, Group 2 2018]",
        "சரத்து 352-ல் 'உள்நாட்டு அமைதியின்மை' என்ற சொல்லுக்குப் பதிலாக 'ஆயுதமேந்திய கிளர்ச்சி' என்ற சொற்றொடரை மாற்றிய அரசியலமைப்பு திருத்தச் சட்டம் எது? [TNPSC குரூப் 1 2017, குரூப் 2 2018]",
        "42nd Constitutional Amendment Act, 1976", "42-வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
        "43rd Constitutional Amendment Act, 1977", "43-வது அரசியலமைப்பு திருத்தச் சட்டம், 1977",
        "44th Constitutional Amendment Act, 1978", "44-வது அரசியலமைப்பு திருத்தச் சட்டம், 1978",
        "45th Constitutional Amendment Act, 1980", "45-வது அரசியலமைப்பு திருத்தச் சட்டம், 1980",
        "C",
        "The 44th Constitutional Amendment Act of 1978 substituted 'armed rebellion' for 'internal disturbance' to prevent arbitrary executive emergencies like the one in 1975.",
        "1975-ல் நடந்தது போன்ற தன்னிச்சையான அவசரநிலைப் பிரகடனங்களைத் தடுப்பதற்காக, 1978-ன் 44-வது அரசியலமைப்பு திருத்தச் சட்டம் 'உள்நாட்டு அமைதியின்மை' என்பதற்குப் பதிலாக 'ஆயுதமேந்திய கிளர்ச்சி' என்பதை மாற்றியது.",
        "Option A (42nd CAA) added provisions making emergency easier and partially territorially flexible.", "விருப்பம் A (42-வது திருத்தம்) அவசரநிலையை எளிதாக்கியது.",
        "Option B (43rd CAA) restored certain civil liberties repealed during emergency.", "விருப்பம் B (43-வது திருத்தம்) அவசரநிலையின் போது நீக்கப்பட்ட சில உரிமைகளை மீட்டெடுத்தது.",
        "Option C is correct; the 44th CAA introduced comprehensive safeguards.", "விருப்பம் C சரியானது; 44-வது திருத்தச் சட்டம் விரிவான அவசரநிலைப் பாதுகாப்புகளை அறிமுகப்படுத்தியது.",
        "Option D (45th CAA) dealt with extending reservation for SCs/STs.", "விருப்பம் D (45-வது திருத்தம்) SC/ST இடஒதுக்கீடு நீட்டிப்பு தொடர்பானது.",
        "44th Amendment is the single most important amendment regarding Emergency Provisions in Indian polity.",
        "இந்திய அரசியலமைப்பில் அவசரநிலைப் பிரிவுகள் தொடர்பாக 44-வது திருத்தச் சட்டமே மிக முக்கியமான திருத்தமாகும்.",
        "The 44th CAA was enacted by the Janata Party government headed by Prime Minister Morarji Desai.",
        "பிரதமர் மொரார்ஜி தேசாய் தலைமையிலான ஜனதா கட்சி அரசால் 44-வது திருத்தச் சட்டம் இயற்றப்பட்டது."
    ))

    # 004 - Key D
    qs.append(make_ep_q(
        PREFIX, 4, DIFF, "PYQ MCQ", "Frequency of Financial Emergency",
        "How many times has Financial Emergency under Article 360 been declared in India so far? [TNPSC Group 4 2018, Group 2 2013, 2019]",
        "இந்தியாவில் இதுவரையிலும் சரத்து 360-ன் கீழான நிதி அவசரநிலை எத்தனை முறை அறிவிக்கப்பட்டுள்ளது? [TNPSC குரூப் 4 2018, குரூப் 2 2013, 2019]",
        "Once (during the 1991 Balance of Payments crisis)", "ஒரு முறை (1991 அன்னியச் செலாவணி நெருக்கடியின் போது)",
        "Twice (in 1965 and 1971)", "இரண்டு முறை (1965 மற்றும் 1971-ல்)",
        "Three times", "மூன்று முறை",
        "Never (Zero times)", "ஒரு முறை கூட இல்லை (பூஜ்ஜியம்)",
        "D",
        "Financial Emergency under Article 360 has never been proclaimed in India since the adoption of the Constitution in 1950.",
        "1950-ல் அரசியலமைப்பு ஏற்றுக்கொள்ளப்பட்டதிலிருந்து இந்தியாவில் சரத்து 360-ன் கீழான நிதி அவசரநிலை ஒருமுறை கூட அறிவிக்கப்படவில்லை.",
        "Option A is incorrect because even during the severe 1991 balance of payments crisis, Article 360 was not invoked.", "விருப்பம் A தவறு, ஏனெனில் 1991 கடுமையான நெருக்கடியின் போது கூட சரத்து 360 பயன்படுத்தப்படவில்லை.",
        "Option B describes wars, which triggered external emergency, not financial emergency.", "விருப்பம் B போர்களைக் குறிப்பிடுகிறது, அவை வெளிப்புற அவசரநிலையைத் தூண்டின.",
        "Option C refers to the number of National Emergencies under Article 352, not Article 360.", "விருப்பம் C சரத்து 352-ன் கீழான தேசிய அவசரநிலைகளின் எண்ணிக்கையைக் குறிக்கிறது.",
        "Option D is correct; Financial Emergency has NEVER been declared in India.", "விருப்பம் D சரியானது; இந்தியாவில் நிதி அவசரநிலை ஒருபோதும் அறிவிக்கப்பட்டதில்லை.",
        "TNPSC Standard Question: Always remember that Financial Emergency in India = 0 times.",
        "TNPSC நிலையான கேள்வி: இந்தியாவில் நிதி அவசரநிலை = 0 முறை என்பதை எப்போதும் நினைவில் கொள்க.",
        "Even during the COVID-19 pandemic, calls for economic emergency were rejected by the government.",
        "கோவிட்-19 பெருந்தொற்றின் போது கூட நிதி அவசரநிலைக்கான கோரிக்கைகளை அரசு நிராகரித்தது."
    ))

    # 005 - Key A
    qs.append(make_ep_q(
        PREFIX, 5, DIFF, "PYQ MCQ", "Non-Suspendable Fundamental Rights",
        "Which Fundamental Rights guaranteed by the Constitution of India CANNOT be suspended even during a National Emergency? [UPSC 2019, TNPSC Group 1 2021]",
        "இந்திய அரசியலமைப்பால் உத்தரவாதம் அளிக்கப்பட்ட எந்த அடிப்படை உரிமைகளை தேசிய அவசரநிலையின் போது கூட இடைநிறுத்த முடியாது? [UPSC 2019, TNPSC குரூப் 1 2021]",
        "Articles 20 and 21", "சரத்துகள் 20 மற்றும் 21",
        "Articles 19 and 20", "சரத்துகள் 19 மற்றும் 20",
        "Articles 21 and 22", "சரத்துகள் 21 மற்றும் 22",
        "Articles 14 and 19", "சரத்துகள் 14 மற்றும் 19",
        "A",
        "Under Article 359 as amended by the 44th Constitutional Amendment Act 1978, the right to move the court for enforcement of Articles 20 (protection in respect of conviction for offences) and 21 (protection of life and personal liberty) cannot be suspended.",
        "1978-ன் 44-வது அரசியலமைப்பு திருத்தச் சட்டத்தால் திருத்தப்பட்ட சரத்து 359-ன் கீழ், சரத்துகள் 20 (குற்றங்களுக்கான தண்டனையிலிருந்து பாதுகாப்பு) மற்றும் 21 (வாழ்வு மற்றும் தனிநபர் சுதந்திரப் பாதுகாப்பு) ஆகியவற்றை அமல்படுத்த நீதிமன்றத்தை அணுகும் உரிமையை இடைநிறுத்த முடியாது.",
        "Option A is correct; Articles 20 and 21 are absolute non-derogable rights during any emergency.", "விருப்பம் A சரியானது; சரத்துகள் 20 மற்றும் 21 ஆகியவை அவசரநிலையின் போது மாற்ற முடியாத முழுமையான உரிமைகளாகும்.",
        "Option B includes Article 19, which is suspended under Article 358 during external emergency.", "விருப்பம் B சரத்து 19-ஐக் கொண்டுள்ளது, இது வெளிப்புற அவசரநிலையின் போது சரத்து 358-ன் கீழ் இடைநிறுத்தப்படுகிறது.",
        "Option C includes Article 22, which can be suspended under Article 359.", "விருப்பம் C சரத்து 22-ஐக் கொண்டுள்ளது, இது சரத்து 359-ன் கீழ் இடைநிறுத்தப்படலாம்.",
        "Option D includes Articles 14 and 19, both of which can be affected during emergency.", "விருப்பம் D சரத்துகள் 14 மற்றும் 19-ஐக் கொண்டுள்ளது, இரண்டும் அவசரநிலையின் போது பாதிக்கப்படலாம்.",
        "Core Examination Concept: Articles 20 and 21 are the inviolable democratic bedrock of the Indian Constitution.",
        "மையத் தேர்வுக் கருத்து: சரத்துகள் 20 மற்றும் 21 ஆகியவை இந்திய அரசியலமைப்பின் மீற முடியாத ஜனநாயக அடித்தளமாகும்.",
        "This amendment was directly enacted to prevent a repeat of the infamous Habeas Corpus case ruling.",
        "புகழ்பெற்ற ஆட்கொணர்வு வழக்கு தீர்ப்பு மீண்டும் நிகழாமல் தடுப்பதற்காகவே இந்தத் திருத்தம் நேரடியாக இயற்றப்பட்டது."
    ))

    # 006 - Key B
    qs.append(make_ep_q(
        PREFIX, 6, DIFF, "PYQ MCQ", "Approval Time Period for Article 352",
        "Within what period must a proclamation of National Emergency be approved by both Houses of Parliament? [TNPSC Group 1 2017, Group 2 2018]",
        "தேசிய அவசரநிலைப் பிரகடனம் பாராளுமன்றத்தின் இரு அவைகளாலும் எத்தனை காலத்திற்குள் அங்கீகரிக்கப்பட வேண்டும்? [TNPSC குரூப் 1 2017, குரூப் 2 2018]",
        "Within 14 days", "14 நாட்களுக்குள்",
        "Within one month", "ஒரு மாதத்திற்குள்",
        "Within two months", "இரண்டு மாதங்களுக்குள்",
        "Within six months", "ஆறு மாதங்களுக்குள்",
        "B",
        "Under Article 352(4), a proclamation of National Emergency must be approved by both Houses of Parliament within one month from the date of its proclamation.",
        "சரத்து 352(4)-ன் கீழ், தேசிய அவசரநிலைப் பிரகடனம் வெளியிடப்பட்ட நாளிலிருந்து ஒரு மாதத்திற்குள் பாராளுமன்றத்தின் இரு அவைகளாலும் அங்கீகரிக்கப்பட வேண்டும்.",
        "Option A (14 days) is the notice period for requisitioning a special sitting of Lok Sabha.", "விருப்பம் A (14 நாட்கள்) மக்களவையின் சிறப்பு அமர்வைக் கோருவதற்கான அறிவிப்பு காலமாகும்.",
        "Option B is correct; the 44th Amendment Act 1978 reduced the period from 2 months to 1 month.", "விருப்பம் B சரியானது; 44-வது திருத்தச் சட்டம் கால அளவை 2 மாதங்களிலிருந்து 1 மாதமாகக் குறைத்தது.",
        "Option C (two months) applies to Article 356 (President's Rule) and Article 360 (Financial Emergency).", "விருப்பம் C (இரண்டு மாதங்கள்) சரத்து 356 மற்றும் 360-க்கு பொருந்தும்.",
        "Option D (six months) is the duration of emergency once approved.", "விருப்பம் D (ஆறு மாதங்கள்) ஒப்புதல் அளிக்கப்பட்ட பின் நீடிக்கும் கால அளவாகும்.",
        "TNPSC Trap: Many candidates confuse the 1 month for Art 352 with the 2 months for Art 356 and 360.",
        "TNPSC பொறி: பல தேர்வர்கள் சரத்து 352-க்கான 1 மாதத்தை, சரத்து 356 மற்றும் 360-க்கான 2 மாதங்களுடன் குழப்பிக் கொள்கிறார்கள்.",
        "If Lok Sabha is dissolved, Rajya Sabha must approve within one month, and reconstituted Lok Sabha within 30 days of its first sitting.",
        "மக்களவை கலைக்கப்பட்டிருந்தால், மாநிலங்களவை ஒரு மாதத்திற்குள்ளும், புதிய மக்களவை கூடிய 30 நாட்களுக்குள்ளும் ஒப்புதல் அளிக்க வேண்டும்."
    ))

    # 007 - Key C
    qs.append(make_ep_q(
        PREFIX, 7, DIFF, "PYQ MCQ", "Majority Required for Article 352",
        "What type of majority in Parliament is required to approve or continue a proclamation of National Emergency under Article 352? [UPSC 2018, TNPSC Group 1 2019]",
        "சரத்து 352-ன் கீழ் தேசிய அவசரநிலைப் பிரகடனத்திற்கு ஒப்புதல் அளிக்க அல்லது அதைத் தொடர பாராளுமன்றத்தில் எந்த வகையான பெரும்பான்மை தேவைப்படுகிறது? [UPSC 2018, TNPSC குரூப் 1 2019]",
        "Simple majority of members present and voting", "வருகை தந்து வாக்களிக்கும் உறுப்பினர்களில் எளிய பெரும்பான்மை",
        "Absolute majority of the total membership of the House", "அவையின் மொத்த உறுப்பினர்களில் முழுமையான பெரும்பான்மை",
        "Special majority (majority of total membership and 2/3 of members present and voting)", "சிறப்புப் பெரும்பான்மை (மொத்த உறுப்பினர்களில் பெரும்பான்மை மற்றும் வருகை தந்து வாக்களிப்போரில் 2/3 பங்கு)",
        "Effective majority of each House", "ஒவ்வொரு அவையின் பயனுள்ள பெரும்பான்மை",
        "C",
        "Under Article 352(6), every resolution approving the proclamation or its continuance must be passed by a special majority in each House: a majority of total membership and at least 2/3 of members present and voting.",
        "சரத்து 352(6)-ன் கீழ், பிரகடனத்திற்கு ஒப்புதல் அளிக்கும் அல்லது அதைத் தொடரச் செய்யும் ஒவ்வொரு தீர்மானமும் சிறப்புப் பெரும்பான்மையால் (மொத்த உறுப்பினர்களில் பெரும்பான்மை + வருகை தந்து வாக்களிப்போரில் 2/3 பங்கு) நிறைவேற்றப்பட வேண்டும்.",
        "Option A (simple majority) was the rule before the 44th Amendment and is still the rule for Article 356 and 360.", "விருப்பம் A (எளிய பெரும்பான்மை) 44-வது திருத்தத்திற்கு முன்பு இருந்தது, தற்போது சரத்து 356 மற்றும் 360-க்கு பொருந்துகிறது.",
        "Option B is only the first limb of the special majority requirement.", "விருப்பம் B சிறப்புப் பெரும்பான்மையின் ஒரு பகுதி மட்டுமே.",
        "Option C is correct; special majority was mandated by the 44th Amendment Act, 1978.", "விருப்பம் C சரியானது; சிறப்புப் பெரும்பான்மை 1978-ன் 44-வது திருத்தச் சட்டத்தால் கட்டாயமாக்கப்பட்டது.",
        "Option D refers to total membership minus vacancies, used for removing presiding officers.", "விருப்பம் D சபாநாயகர் போன்றோரை நீக்கப் பயன்படும் பயனுள்ள பெரும்பான்மையைக் குறிக்கிறது.",
        "Golden Rule: National Emergency approval requires SPECIAL MAJORITY; Disapproval requires only SIMPLE MAJORITY by Lok Sabha.",
        "பொன்விதி: தேசிய அவசரநிலை ஒப்புதலுக்கு சிறப்புப் பெரும்பான்மை தேவை; நிராகரிப்புக்கு மக்களவையின் எளிய பெரும்பான்மை மட்டுமே போதுமானது.",
        "This asymmetry prevents a minority government from maintaining an emergency against the democratic will of the House.",
        "இந்தச் சமச்சீரற்ற தன்மை ஒரு சிறுபான்மை அரசு அவையின் விருப்பத்திற்கு மாறாக அவசரநிலையைத் தொடர்வதைத் தடுக்கிறது."
    ))

    # 008 - Key D
    qs.append(make_ep_q(
        PREFIX, 8, DIFF, "PYQ MCQ", "Approval Time Period for President's Rule",
        "A proclamation imposing President's Rule under Article 356 must be approved by both Houses of Parliament within: [TNPSC Group 2 2018, Group 1 2014]",
        "சரத்து 356-ன் கீழ் குடியரசுத் தலைவர் ஆட்சியை விதிக்கும் பிரகடனம் பாராளுமன்றத்தின் இரு அவைகளாலும் எத்தனை காலத்திற்குள் அங்கீகரிக்கப்பட வேண்டும்? [TNPSC குரூப் 2 2018, குரூப் 1 2014]",
        "14 days", "14 நாட்கள்",
        "30 days", "30 நாட்கள்",
        "One month", "ஒரு மாதம்",
        "Two months", "இரண்டு மாதங்கள்",
        "D",
        "Under Article 356(3), a proclamation imposing President's Rule must be approved by both Houses of Parliament within two months from the date of its proclamation.",
        "சரத்து 356(3)-ன் கீழ், குடியரசுத் தலைவர் ஆட்சியை விதிக்கும் பிரகடனம் வெளியிடப்பட்ட நாளிலிருந்து இரண்டு மாதங்களுக்குள் பாராளுமன்றத்தின் இரு அவைகளாலும் அங்கீகரிக்கப்பட வேண்டும்.",
        "Option A is the time limit for special sitting notice under Article 352(8).", "விருப்பம் A சரத்து 352(8)-ன் கீழான சிறப்பு அமர்வு காலக்கெடுவாகும்.",
        "Option B is the survival duration after the reconstituted Lok Sabha meets.", "விருப்பம் B புதிய மக்களவை கூடிய பின் நீடிக்கும் கால அளவாகும்.",
        "Option C (one month) applies to Article 352 National Emergency.", "விருப்பம் C (ஒரு மாதம்) சரத்து 352 தேசிய அவசரநிலைக்கு பொருந்தும்.",
        "Option D is correct; Article 356 requires approval within two months.", "விருப்பம் D சரியானது; சரத்து 356-க்கு இரண்டு மாதங்களுக்குள் ஒப்புதல் அளிக்கப்பட வேண்டும்.",
        "Compare Timelines: Article 352 = 1 month; Article 356 = 2 months; Article 360 = 2 months.",
        "காலக்கெடு ஒப்பீடு: சரத்து 352 = 1 மாதம்; சரத்து 356 = 2 மாதங்கள்; சரத்து 360 = 2 மாதங்கள்.",
        "Approval of President's Rule requires only a simple majority in both Houses.",
        "குடியரசுத் தலைவர் ஆட்சிக்கு ஒப்புதல் அளிக்க இரு அவைகளிலும் எளிய பெரும்பான்மை மட்டுமே போதுமானது."
    ))

    # 009 - Key A
    qs.append(make_ep_q(
        PREFIX, 9, DIFF, "PYQ MCQ", "Landmark Case on Article 356 Misuse",
        "Which landmark Supreme Court judgment laid down definitive constitutional principles restricting the arbitrary imposition of President's Rule under Article 356? [TNPSC Group 1 2019, UPSC 2017]",
        "சரத்து 356-ன் கீழ் குடியரசுத் தலைவர் ஆட்சி தன்னிச்சையாக விதிக்கப்படுவதைக் கட்டுப்படுத்தி தீர்க்கமான அரசியலமைப்பு விதிகளையும் வழிகாட்டுதல்களையும் வகுத்த உச்ச நீதிமன்ற வரலாற்றுத் தீர்ப்பு எது? [TNPSC குரூப் 1 2019, UPSC 2017]",
        "S.R. Bommai v. Union of India (1994)", "எஸ்.ஆர். பொம்மை எதிர் இந்திய ஒன்றியம் (1994)",
        "Kesavananda Bharati v. State of Kerala (1973)", "கேசவானந்த பாரதி எதிர் கேரள அரசு (1973)",
        "Golaknath v. State of Punjab (1967)", "கோலக்நாத் எதிர் பஞ்சாப் அரசு (1967)",
        "Minerva Mills v. Union of India (1980)", "மினர்வா மில்ஸ் எதிர் இந்திய ஒன்றியம் (1980)",
        "A",
        "In S.R. Bommai v. Union of India (1994), a 9-judge bench of the Supreme Court held that Article 356 is subject to judicial review, floor testing of majority is mandatory, and assemblies cannot be dissolved prior to parliamentary approval.",
        "எஸ்.ஆர். பொம்மை எதிர் இந்திய ஒன்றியம் (1994) வழக்கில், 9 நீதிபதிகள் கொண்ட உச்ச நீதிமன்ற அமர்வு சரத்து 356 நீதித்துறை மறுஆய்வுக்கு உட்பட்டது, நம்பிக்கை வாக்கெடுப்பு கட்டாயமானது, மற்றும் பாராளுமன்ற ஒப்புதலுக்கு முன் சட்டமன்றத்தைக் கலைக்கக் கூடாது என்று தீர்ப்பளித்தது.",
        "Option A is correct; S.R. Bommai is the paramount precedent on Article 356.", "விருப்பம் A சரியானது; சரத்து 356 மீதான தலையாய முன்மாதிரி தீர்ப்பு எஸ்.ஆர். பொம்மை வழக்கே ஆகும்.",
        "Option B established the basic structure doctrine for constitutional amendments.", "விருப்பம் B அரசியலமைப்பு திருத்தங்களுக்கான அடிப்படைக் கட்டமைப்புக் கோட்பாட்டை வகுத்தது.",
        "Option C held that Parliament cannot abridge Fundamental Rights.", "விருப்பம் C அடிப்படை உரிமைகளை பாராளுமன்றத்தால் குறைக்க முடியாது என்று கூறியது.",
        "Option D reaffirmed basic structure and struck down parts of 42nd Amendment.", "விருப்பம் D அடிப்படைக் கட்டமைப்பை மீண்டும் உறுதிப்படுத்தி 42-வது திருத்தத்தின் பகுதிகளை ரத்து செய்தது.",
        "TNPSC Landmark: S.R. Bommai (1994) ended the era of rampant and unchecked dismissals of state governments.",
        "TNPSC மைல்கல்: எஸ்.ஆர். பொம்மை (1994) தீர்ப்பு மாநில அரசுகள் தன்னிச்சையாகக் கலைக்கப்படும் சகாப்தத்திற்கு முற்றுப்புள்ளி வைத்தது.",
        "The judgment also declared Secularism to be an essential part of the basic structure of the Constitution.",
        "இத்தீர்ப்பு மதச்சார்பின்மையை அரசியலமைப்பின் அடிப்படைக் கட்டமைப்பின் ஒரு முக்கிய அங்கமாக அறிவித்தது."
    ))

    # 010 - Key B
    qs.append(make_ep_q(
        PREFIX, 10, DIFF, "PYQ MCQ", "First State Under President's Rule",
        "In which State was President's Rule under Article 356 imposed for the first time in India? [TNPSC Group 2 2015, Group 4 2019]",
        "இந்தியாவில் முதன்முதலாக சரத்து 356-ன் கீழான குடியரசுத் தலைவர் ஆட்சி எந்த மாநிலத்தில் விதிக்கப்பட்டது? [TNPSC குரூப் 2 2015, குரூப் 4 2019]",
        "Kerala (1959)", "கேரளா (1959)",
        "Punjab (1951)", "பஞ்சாப் (1951)",
        "Tamil Nadu (1976)", "தமிழ்நாடு (1976)",
        "Uttar Pradesh (1968)", "உத்தரப் பிரதேசம் (1968)",
        "B",
        "President's Rule was imposed for the first time in Punjab (then East Punjab) in June 1951 due to political instability in the Congress party.",
        "1951 ஜூன் மாதத்தில் பஞ்சாபில் (அப்போது கிழக்கு பஞ்சாப்) காங்கிரஸ் கட்சியில் ஏற்பட்ட அரசியல் உறுதியற்ற தன்மை காரணமாக முதன்முதலாக குடியரசுத் தலைவர் ஆட்சி விதிக்கப்பட்டது.",
        "Option A (Kerala 1959) was the first dismissal of a democratically elected Communist ministry, but not the first state overall.", "விருப்பம் A (கேரளா 1959) முதல் கம்யூனிஸ்ட் அரசு கலைக்கப்பட்ட நிகழ்வாகும், ஆனால் முதல் மாநிலம் அல்ல.",
        "Option B is correct; Punjab in 1951 was the pioneering instance.", "விருப்பம் B சரியானது; 1951-ல் பஞ்சாபே முதல் நிகழ்வாகும்.",
        "Option C (Tamil Nadu 1976) was the dismissal of the DMK government during the Emergency.", "விருப்பம் C (தமிழ்நாடு 1976) அவசரநிலையின் போது திமுக அரசு கலைக்கப்பட்ட நிகழ்வாகும்.",
        "Option D refers to UP's first imposition in 1968.", "விருப்பம் D 1968-ல் உத்தரப் பிரதேசத்தில் முதன்முறை விதிக்கப்பட்டதைக் குறிக்கிறது.",
        "TNPSC Repeated Question: First President's Rule = Punjab (1951); Dismissal of EMS Namboodiripad govt = Kerala (1959).",
        "TNPSC மீண்டும் கேட்கப்படும் கேள்வி: முதல் குடியரசுத் தலைவர் ஆட்சி = பஞ்சாப் (1951); இ.எம்.எஸ். நம்பூதிரிபாட் அரசு கலைக்கப்பட்டது = கேரளா (1959).",
        "Punjab has also seen the longest continuous President's Rule from 1987 to 1992 (nearly 5 years), requiring multiple constitutional amendments.",
        "1987 முதல் 1992 வரை ஏறக்குறைய 5 ஆண்டுகள் மிக நீண்ட தொடர்ச்சியான குடியரசுத் தலைவர் ஆட்சியையும் பஞ்சாப் சந்தித்துள்ளது."
    ))

    return qs

def get_pyq_questions_batch2():
    qs = []

    # 011 - Key C
    qs.append(make_ep_q(
        PREFIX, 11, DIFF, "PYQ MCQ", "Constitutional Borrowing Source",
        "The provision for the 'suspension of Fundamental Rights during emergency' was borrowed from which country's constitution? [TNPSC Group 4 2019, Group 2 2012]",
        "'அவசரநிலையின் போது அடிப்படை உரிமைகள் இடைநிறுத்தம்' செய்யப்படும் முறை எந்த நாட்டின் அரசியலமைப்பிலிருந்து பெறப்பட்டது? [TNPSC குரூப் 4 2019, குரூப் 2 2012]",
        "Constitution of the USA", "அமெரிக்க அரசியலமைப்பு",
        "Constitution of the USSR", "சோவியத் ஒன்றிய அரசியலமைப்பு",
        "Weimar Constitution of Germany", "ஜெர்மனியின் வெய்மர் அரசியலமைப்பு",
        "Constitution of South Africa", "தென்னாப்பிரிக்க அரசியலமைப்பு",
        "C",
        "The feature of suspension of Fundamental Rights during National Emergency was borrowed from the Weimar Constitution of Germany (Article 48).",
        "தேசிய அவசரநிலையின் போது அடிப்படை உரிமைகள் இடைநிறுத்தப்படும் அம்சம் ஜெர்மனியின் வெய்மர் அரசியலமைப்பிலிருந்து (சரத்து 48) பெறப்பட்டது.",
        "Option A (USA) contributed Fundamental Rights and Judicial Review.", "விருப்பம் A (அமெரிக்கா) அடிப்படை உரிமைகள் மற்றும் நீதித்துறை மறுஆய்வை வழங்கியது.",
        "Option B (USSR) contributed Fundamental Duties and ideals of Justice.", "விருப்பம் B (சோவியத் ஒன்றியம்) அடிப்படைக் கடமைகள் மற்றும் நீதியின் இலட்சியங்களை வழங்கியது.",
        "Option C is correct; Weimar Constitution of Germany is the direct source.", "விருப்பம் C சரியானது; ஜெர்மனியின் வெய்மர் அரசியலமைப்பே நேரடி மூலமாகும்.",
        "Option D (South Africa) contributed amendment procedure and election of Rajya Sabha members.", "விருப்பம் D (தென்னாப்பிரிக்கா) திருத்த நடைமுறை மற்றும் மாநிலங்களவை உறுப்பினர் தேர்தலை வழங்கியது.",
        "Remember Distinction: Framework of emergencies = GoI Act 1935; Suspension of Fundamental Rights = Weimar Constitution of Germany.",
        "வேறுபாட்டை நினைவில் கொள்க: அவசரநிலைகளின் கட்டமைப்பு = 1935 இந்திய அரசுச் சட்டம்; அடிப்படை உரிமைகள் இடைநிறுத்தம் = ஜெர்மனியின் வெய்மர் அரசியலமைப்பு.",
        "Article 48 of the Weimar Constitution was famously utilized in 1933 to suspend civil liberties in Germany.",
        "1933-ல் ஜெர்மனியில் குடிமை உரிமைகளை இடைநிறுத்த வெய்மர் அரசியலமைப்பின் சரத்து 48 பயன்படுத்தப்பட்டது."
    ))

    # 012 - Key D
    qs.append(make_ep_q(
        PREFIX, 12, DIFF, "PYQ MCQ", "Administrative Framework Source",
        "The administrative machinery and detailed operational structure of Emergency Provisions in the Indian Constitution were largely drawn from: [TNPSC Group 1 2011, Group 2 2015]",
        "இந்திய அரசியலமைப்பின் அவசரநிலைப் பிரிவுகளின் நிர்வாக இயந்திரம் மற்றும் விரிவான செயல்பாட்டுக் கட்டமைப்பு பெரும்பாலும் எதிலிருந்து பெறப்பட்டது? [TNPSC குரூப் 1 2011, குரூப் 2 2015]",
        "US Constitution of 1787", "1787 அமெரிக்க அரசியலமைப்பு",
        "British Parliamentary Conventions", "பிரிட்டிஷ் பாராளுமன்ற மரபுகள்",
        "French Constitution of the Fifth Republic", "ஐந்தாவது குடியரசின் பிரெஞ்சு அரசியலமைப்பு",
        "Government of India Act, 1935", "1935-ஆம் ஆண்டின் இந்திய அரசுச் சட்டம்",
        "D",
        "The structural framework of emergency provisions was largely adapted from the Government of India Act, 1935 (specifically Section 93 and Section 102).",
        "அவசரநிலைப் பிரிவுகளின் கட்டமைப்பு பெரும்பாலும் 1935-ஆம் ஆண்டின் இந்திய அரசுச் சட்டத்திலிருந்து (குறிப்பாக பிரிவு 93 மற்றும் பிரிவு 102) ஏற்றுக்கொள்ளப்பட்டது.",
        "Option A (US) has no constitutional chapter dedicated to emergencies.", "விருப்பம் A (அமெரிக்கா) அவசரநிலைகளுக்கென தனி அரசியலமைப்பு அத்தியாயத்தைக் கொண்டிருக்கவில்லை.",
        "Option B (UK) operates under common law and prerogative powers without a codified constitution.", "விருப்பம் B (பிரிட்டன்) எழுதப்படாத அரசியலமைப்பின் கீழ் பொதுச் சட்டத்தின்படி செயல்படுகிறது.",
        "Option C (French) was adopted in 1958, after the Indian Constitution was framed.", "விருப்பம் C (பிரான்ஸ்) இந்திய அரசியலமைப்பு உருவாக்கப்பட்ட பிறகு 1958-ல் ஏற்றுக்கொள்ளப்பட்டது.",
        "Option D is correct; the 1935 Act provided the direct legislative blueprint for Articles 352 and 356.", "விருப்பம் D சரியானது; 1935 சட்டம் சரத்துகள் 352 மற்றும் 356-க்கான நேரடி சட்ட வரைவை வழங்கியது.",
        "Historical Continuity: Dr. Ambedkar acknowledged adapting Sections 93 and 102 of the 1935 Act into the Draft Constitution.",
        "வரலாற்றுத் தொடர்ச்சி: 1935 சட்டத்தின் பிரிவுகள் 93 மற்றும் 102-ஐ வரைவு அரசியலமைப்பில் ஏற்றுக்கொண்டதை டாக்டர் அம்பேத்கர் ஒப்புக்கொண்டார்.",
        "Section 93 gave Governors autocratic emergency powers to suspend provincial autonomy.",
        "பிரிவு 93 மாகாண சுயாட்சியை இடைநிறுத்த ஆளுநர்களுக்கு எதேச்சதிகார அவசரநிலை அதிகாரங்களை வழங்கியது."
    ))

    # 013 - Key A
    qs.append(make_ep_q(
        PREFIX, 13, DIFF, "PYQ MCQ", "Article 365 Consequences",
        "If any State fails to comply with or give effect to any direction given by the Union in exercise of its executive power, which Article empowers the President to hold that governance cannot be carried on in accordance with the Constitution? [TNPSC Group 1 2015, UPSC 2013]",
        "மத்திய அரசு தனது நிர்வாக அதிகாரத்தைப் பயன்படுத்தி வழங்கும் எந்தவொரு வழிகாட்டுதலையும் ஒரு மாநிலம் பின்பற்றவோ அல்லது செயல்படுத்தவோ தவறினால், அரசியலமைப்புப்படி ஆட்சி நடைபெற முடியாது என்று குடியரசுத் தலைவர் கருத எந்த சரத்து அதிகாரம் அளிக்கிறது? [TNPSC குரூப் 1 2015, UPSC 2013]",
        "Article 365", "சரத்து 365",
        "Article 356", "சரத்து 356",
        "Article 355", "சரத்து 355",
        "Article 360", "சரத்து 360",
        "A",
        "Under Article 365, where any State fails to comply with or give effect to any direction given in the exercise of the executive power of the Union, it shall be lawful for the President to hold that a situation has arisen in which the government of the State cannot be carried on in accordance with the provisions of the Constitution (triggering Article 356).",
        "சரத்து 365-ன் கீழ், மத்திய அரசின் நிர்வாக அதிகாரத்தின் கீழ் வழங்கப்படும் வழிகாட்டுதல்களை ஒரு மாநிலம் பின்பற்றத் தவறினால், அங்கு அரசியலமைப்பு விதிகளின்படி ஆட்சி நடைபெற முடியாத சூழ்நிலை ஏற்பட்டுள்ளது எனக் குடியரசுத் தலைவர் கருதுவது சட்டபூர்வமானது (இது சரத்து 356-ஐத் தூண்டுகிறது).",
        "Option A is correct; Article 365 provides the sanction for non-compliance with Union directions.", "விருப்பம் A சரியானது; மத்திய வழிகாட்டுதல்களை மீறுவதற்கான தண்டனை விதியை சரத்து 365 வழங்குகிறது.",
        "Option B (Article 356) is the actual proclamation article for President's Rule.", "விருப்பம் B (சரத்து 356) குடியரசுத் தலைவர் ஆட்சிக்கான பிரகடன சரத்தாகும்.",
        "Option C (Article 355) imposes the duty on the Union to protect states.", "விருப்பம் C (சரத்து 355) மாநிலங்களைப் பாதுகாக்க மத்திய அரசுக்குக் கடமையை விதிக்கிறது.",
        "Option D (Article 360) deals with Financial Emergency.", "விருப்பம் D (சரத்து 360) நிதி அவசரநிலையைக் கையாள்கிறது.",
        "Crucial Link: Article 365 is the bridge that turns administrative defiance into a constitutional failure under Article 356.",
        "முக்கிய இணைப்பு: சரத்து 365 என்பது நிர்வாக மீறலை சரத்து 356-ன் கீழான அரசியலமைப்பு முறிவாக மாற்றும் பாலமாகும்.",
        "Article 365 is located in Part XIX (Miscellaneous), while Article 356 is in Part XVIII (Emergency).",
        "சரத்து 365 பகுதி XIX-ல் (இதர விதிகள்) உள்ளது, ஆனால் சரத்து 356 பகுதி XVIII-ல் (அவசரநிலை) உள்ளது."
    ))

    # 014 - Key B
    qs.append(make_ep_q(
        PREFIX, 14, DIFF, "PYQ MCQ", "Article 355 Duty of Union",
        "Which Article of the Indian Constitution makes it the duty of the Union to protect every State against external aggression and internal disturbance? [UPSC 2008, TNPSC Group 1 2017]",
        "இந்திய அரசியலமைப்பின் எந்த சரத்து, ஒவ்வொரு மாநிலத்தையும் வெளிநாட்டு ஆக்கிரமிப்பு மற்றும் உள்நாட்டு அமைதியின்மையிலிருந்து பாதுகாக்க வேண்டிய கடமையை மத்திய அரசுக்கு விதிக்கிறது? [UPSC 2008, TNPSC குரூப் 1 2017]",
        "Article 352", "சரத்து 352",
        "Article 355", "சரத்து 355",
        "Article 356", "சரத்து 356",
        "Article 360", "சரத்து 360",
        "B",
        "Article 355 declares that 'it shall be the duty of the Union to protect every State against external aggression and internal disturbance and to ensure that the government of every State is carried on in accordance with the provisions of this Constitution.'",
        "சரத்து 355 'வெளிநாட்டு ஆக்கிரமிப்பு மற்றும் உள்நாட்டு அமைதியின்மையிலிருந்து ஒவ்வொரு மாநிலத்தையும் பாதுகாப்பதும், ஒவ்வொரு மாநில அரசும் அரசியலமைப்பு விதிகளின்படி நடைபெறுவதை உறுதி செய்வதும் மத்திய அரசின் கடமையாகும்' என்று கூறுகிறது.",
        "Option A (Article 352) empowers the proclamation of National Emergency.", "விருப்பம் A (சரத்து 352) தேசிய அவசரநிலையைப் பிரகடனப்படுத்த அதிகாரம் அளிக்கிறது.",
        "Option B is correct; Article 355 is the foundational 'Duty of Union' article.", "விருப்பம் B சரியானது; சரத்து 355 என்பது 'மத்திய அரசின் கடமை' தொடர்பான அடிப்படை சரத்தாகும்.",
        "Option C (Article 356) empowers President's Rule.", "விருப்பம் C (சரத்து 356) குடியரசுத் தலைவர் ஆட்சிக்கு அதிகாரம் அளிக்கிறது.",
        "Option D (Article 360) empowers Financial Emergency.", "விருப்பம் D (சரத்து 360) நிதி அவசரநிலைக்கு அதிகாரம் அளிக்கிறது.",
        "TNPSC Trap: Article 355 is NOT an emergency proclamation; it is a constitutional justification and duty of the Union.",
        "TNPSC பொறி: சரத்து 355 என்பது அவசரநிலைப் பிரகடனம் அல்ல; இது மத்திய அரசின் அரசியலமைப்பு நியாயமும் கடமையுமாகும்.",
        "The Sarkaria Commission recommended that prior warnings under Article 355 should be mandatory before using Article 356.",
        "சரத்து 356-ஐப் பயன்படுத்துவதற்கு முன்பு சரத்து 355-ன் கீழ் முன் எச்சரிக்கை விடுப்பது கட்டாயமாக்கப்பட வேண்டும் என்று சர்க்காரியா ஆணையம் பரிந்துரைத்தது."
    ))

    # 015 - Key C
    qs.append(make_ep_q(
        PREFIX, 15, DIFF, "PYQ MCQ", "Financial Emergency and Salary Reduction",
        "During the operation of a Financial Emergency under Article 360, the President of India has the power to issue directions for the reduction of salaries and allowances of: [TNPSC Group 1 2017, Group 2 2018]",
        "சரத்து 360-ன் கீழான நிதி அவசரநிலை செயல்பாட்டில் இருக்கும் போது, பின்வரும் யாருடைய ஊதியங்கள் மற்றும் படிகளைக் குறைப்பதற்கான வழிகாட்டுதல்களைப் பிறப்பிக்க இந்தியக் குடியரசுத் தலைவருக்கு அதிகாரம் உண்டு? [TNPSC குரூப் 1 2017, குரூப் 2 2018]",
        "Ministers and members of Parliament only", "அமைச்சர்கள் மற்றும் பாராளுமன்ற உறுப்பினர்கள் மட்டுமே",
        "All civil servants serving the Union and States, excluding judicial officers", "நீதித்துறை அதிகாரிகளைத் தவிர, மத்திய மற்றும் மாநில அரசுகளில் பணியாற்றும் அனைத்து அரசு ஊழியர்கள்",
        "All persons serving the Union and States, including judges of the Supreme Court and High Courts", "உச்ச நீதிமன்ற மற்றும் உயர் நீதிமன்ற நீதிபதிகள் உட்பட, மத்திய மற்றும் மாநில அரசுகளில் பணியாற்றும் அனைத்து நபர்கள்",
        "Employees of public sector banks and undertakings only", "பொதுத்துறை வங்கிகள் மற்றும் நிறுவனங்களின் ஊழியர்கள் மட்டுமே",
        "C",
        "Under Article 360(4)(b), the President can direct the reduction of salaries and allowances of all or any class of persons serving in connection with the affairs of the Union, including the judges of the Supreme Court and the High Courts.",
        "சரத்து 360(4)(b)-ன் கீழ், உச்ச நீதிமன்ற மற்றும் உயர் நீதிமன்ற நீதிபதிகள் உட்பட மத்திய மற்றும் மாநில அரசுகளின் கீழ் பணியாற்றும் அனைத்து அல்லது குறிப்பிட்ட வகுப்பினரின் ஊதியங்களையும் படிகளையும் குறைக்க குடியரசுத் தலைவர் உத்தரவிட முடியும்.",
        "Option A is too narrow; it applies to all public servants and judges.", "விருப்பம் A மிகவும் குறுகியது; இது அனைத்து அரசு ஊழியர்களுக்கும் நீதிபதிகளுக்கும் பொருந்தும்.",
        "Option B erroneously excludes judges; judges are explicitly included.", "விருப்பம் B நீதிபதிகளைத் தவறாக விலக்குகிறது; நீதிபதிகள் வெளிப்படையாக இதில் சேர்க்கப்பட்டுள்ளனர்.",
        "Option C is correct; judicial salaries can be reduced ONLY during Financial Emergency.", "விருப்பம் C சரியானது; நிதி அவசரநிலையின் போது மட்டுமே நீதிபதிகளின் ஊதியத்தைக் குறைக்க முடியும்.",
        "Option D is factually incorrect and restrictive.", "விருப்பம் D உண்மையற்றது மற்றும் கட்டுப்படுத்தப்பட்டது.",
        "High-Yield Concept: Under normal times, salaries of SC and HC judges cannot be varied to their disadvantage; Article 360 is the ONLY exception.",
        "உயர்-விளைச்சல் கருத்து: சாதாரண காலங்களில் உச்ச நீதிமன்ற மற்றும் உயர் நீதிமன்ற நீதிபதிகளின் ஊதியத்தைக் குறைக்க முடியாது; சரத்து 360 மட்டுமே இதற்கு ஒரே விதிவிலக்கு.",
        "The President can also reserve all money bills passed by state legislatures for consideration.",
        "மாநில சட்டமன்றங்கள் நிறைவேற்றும் அனைத்து பண மசோதாக்களையும் தனது பரிசீலனைக்கு நிறுத்தி வைக்கவும் குடியரசுத் தலைவர் உத்தரவிடலாம்."
    ))

    # 016 - Key D
    qs.append(make_ep_q(
        PREFIX, 16, DIFF, "PYQ MCQ", "Automatic Suspension of Article 19",
        "Under which Article of the Constitution of India are the six Fundamental Freedoms guaranteed by Article 19 automatically suspended during an external National Emergency? [UPSC 2015, TNPSC Group 1 2019]",
        "இந்திய அரசியலமைப்பின் எந்த சரத்தின் கீழ், வெளிப்புற தேசிய அவசரநிலையின் போது சரத்து 19 உத்தரவாதம் அளிக்கும் ஆறு அடிப்படைச் சுதந்திரங்கள் தானாகவே இடைநிறுத்தப்படுகின்றன? [UPSC 2015, TNPSC குரூப் 1 2019]",
        "Article 352", "சரத்து 352",
        "Article 356", "சரத்து 356",
        "Article 359", "சரத்து 359",
        "Article 358", "சரத்து 358",
        "D",
        "Article 358 provides for the automatic suspension of the Fundamental Rights guaranteed by Article 19 as soon as a proclamation of emergency is issued on grounds of War or External Aggression.",
        "போர் அல்லது வெளிநாட்டு ஆக்கிரமிப்பு அடிப்படையில் அவசரநிலைப் பிரகடனம் வெளியிடப்பட்ட உடனேயே, சரத்து 19 உத்தரவாதம் அளிக்கும் அடிப்படை உரிமைகள் தானாகவே இடைநிறுத்தப்படுவதை சரத்து 358 வழங்குகிறது.",
        "Option A (Article 352) empowers the proclamation itself.", "விருப்பம் A (சரத்து 352) பிரகடனத்திற்கு அதிகாரம் அளிக்கிறது.",
        "Option B (Article 356) deals with President's Rule.", "விருப்பம் B (சரத்து 356) குடியரசுத் தலைவர் ஆட்சி தொடர்பானது.",
        "Option C (Article 359) deals with presidential order suspending enforcement of specified rights.", "விருப்பம் C (சரத்து 359) குறிப்பிட்ட உரிமைகளின் அமலாக்கத்தை குடியரசுத் தலைவர் ஆணை மூலம் இடைநிறுத்துவது தொடர்பானது.",
        "Option D is correct; Article 358 automatically suspends Article 19.", "விருப்பம் D சரியானது; சரத்து 358 தானாகவே சரத்து 19-ஐ இடைநிறுத்துகிறது.",
        "Remember: Article 358 = Automatic suspension of Article 19 (War/External Aggression only); Article 359 = Non-automatic suspension of remedies for other rights by presidential order.",
        "நினைவில் கொள்க: சரத்து 358 = சரத்து 19 தானாக இடைநிறுத்தம் (போர்/வெளிநாட்டு ஆக்கிரமிப்பு மட்டுமே); சரத்து 359 = குடியரசுத் தலைவர் ஆணை மூலம் மற்ற உரிமைகளின் பரிகாரங்கள் இடைநிறுத்தம்.",
        "The 44th Amendment Act ensured Article 358 does not apply to armed rebellion.",
        "44-வது திருத்தச் சட்டம் சரத்து 358 ஆயுதமேந்திய கிளர்ச்சிக்குப் பொருந்தாது என்பதை உறுதி செய்தது."
    ))

    # 017 - Key A
    qs.append(make_ep_q(
        PREFIX, 17, DIFF, "PYQ MCQ", "Internal Emergency Definition",
        "A National Emergency declared under Article 352 on the ground of 'Armed Rebellion' is termed as: [TNPSC Group 2 2012, Group 1 2014]",
        "'ஆயுதமேந்திய கிளர்ச்சி' என்ற அடிப்படையில் சரத்து 352-ன் கீழ் அறிவிக்கப்படும் தேசிய அவசரநிலை எவ்வாறு அழைக்கப்படுகிறது? [TNPSC குரூப் 2 2012, குரூப் 1 2014]",
        "Internal Emergency", "உள்நாட்டு அவசரநிலை",
        "External Emergency", "வெளிப்புற அவசரநிலை",
        "Constitutional Emergency", "அரசியலமைப்பு அவசரநிலை",
        "Civil Emergency", "குடிமை அவசரநிலை",
        "A",
        "A National Emergency proclaimed on the ground of 'War' or 'External Aggression' is called 'External Emergency', whereas an emergency proclaimed on the ground of 'Armed Rebellion' is called 'Internal Emergency'.",
        "'போர்' அல்லது 'வெளிநாட்டு ஆக்கிரமிப்பு' அடிப்படையில் பிரகடனப்படுத்தப்படும் தேசிய அவசரநிலை 'வெளிப்புற அவசரநிலை' எனவும், 'ஆயுதமேந்திய கிளர்ச்சி' அடிப்படையில் அறிவிக்கப்படுவது 'உள்நாட்டு அவசரநிலை' எனவும் அழைக்கப்படுகிறது.",
        "Option A is correct; Armed Rebellion triggers Internal Emergency.", "விருப்பம் A சரியானது; ஆயுதமேந்திய கிளர்ச்சி உள்நாட்டு அவசரநிலையைத் தூண்டுகிறது.",
        "Option B refers to emergency on grounds of War or External Aggression.", "விருப்பம் B போர் அல்லது வெளிநாட்டு ஆக்கிரமிப்பு அடிப்படையிலான அவசரநிலையைக் குறிக்கிறது.",
        "Option C refers to President's Rule under Article 356.", "விருப்பம் C சரத்து 356-ன் கீழான குடியரசுத் தலைவர் ஆட்சியைக் குறிக்கிறது.",
        "Option D is a colloquial term not found in the Constitution.", "விருப்பம் D அரசியலமைப்பில் இல்லாத பொதுவான சொல்லாகும்.",
        "Crucial Impact: During an Internal Emergency, Article 19 is NOT automatically suspended under Article 358!",
        "முக்கியத் தாக்கம்: உள்நாட்டு அவசரநிலையின் போது, சரத்து 358-ன் கீழ் சரத்து 19 தானாகவே இடைநிறுத்தப்படாது!",
        "This safeguard was introduced by the 44th Constitutional Amendment Act 1978.",
        "இந்தப் பாதுகாப்பு 1978-ன் 44-வது அரசியலமைப்பு திருத்தச் சட்டத்தால் அறிமுகப்படுத்தப்பட்டது."
    ))

    # 018 - Key B
    qs.append(make_ep_q(
        PREFIX, 18, DIFF, "PYQ MCQ", "Restoration of Judicial Review",
        "Which Constitutional Amendment Act restored the power of judicial review over the proclamation of emergencies, which had been ousted by the 38th Amendment? [TNPSC Group 1 2017, UPSC 2016]",
        "38-வது திருத்தச் சட்டத்தால் நீக்கப்பட்ட அவசரநிலைப் பிரகடனங்கள் மீதான நீதித்துறை மறுஆய்வு அதிகாரத்தை மீண்டும் மீட்டெடுத்த அரசியலமைப்பு திருத்தச் சட்டம் எது? [TNPSC குரூப் 1 2017, UPSC 2016]",
        "42nd Constitutional Amendment Act, 1976", "42-வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
        "44th Constitutional Amendment Act, 1978", "44-வது அரசியலமைப்பு திருத்தச் சட்டம், 1978",
        "43rd Constitutional Amendment Act, 1977", "43-வது அரசியலமைப்பு திருத்தச் சட்டம், 1977",
        "52nd Constitutional Amendment Act, 1985", "52-வது அரசியலமைப்பு திருத்தச் சட்டம், 1985",
        "B",
        "The 38th Amendment Act of 1975 had made the President's satisfaction in proclaiming emergencies final and non-justiciable. The 44th Constitutional Amendment Act of 1978 deleted these clauses, restoring judicial review.",
        "1975-ன் 38-வது திருத்தச் சட்டம் அவசரநிலைகளைப் பிரகடனப்படுத்துவதில் குடியரசுத் தலைவரின் திருப்தியே இறுதியானது மற்றும் நீதிமன்றத்தில் கேள்வி கேட்க முடியாதது என மாற்றியிருந்தது. 1978-ன் 44-வது அரசியலமைப்பு திருத்தச் சட்டம் இந்தப் பிரிவுகளை நீக்கி நீதித்துறை மறுஆய்வை மீட்டெடுத்தது.",
        "Option A (42nd CAA) further curtailed judicial powers.", "விருப்பம் A (42-வது திருத்தம்) நீதித்துறை அதிகாரங்களை மேலும் குறைத்தது.",
        "Option B is correct; the 44th Amendment Act 1978 restored the jurisdiction of courts.", "விருப்பம் B சரியானது; 44-வது திருத்தச் சட்டம் நீதிமன்றங்களின் அதிகார வரம்பை மீட்டெடுத்தது.",
        "Option C (43rd CAA) repealed parts of the 42nd Amendment relating to anti-national activities.", "விருப்பம் C (43-வது திருத்தம்) தேசவிரோத நடவடிக்கைகள் தொடர்பான 42-வது திருத்தத்தின் பகுதிகளை ரத்து செய்தது.",
        "Option D (52nd CAA) introduced the Anti-Defection Law.", "விருப்பம் D (52-வது திருத்தம்) கட்சித் தாவல் தடைச் சட்டத்தை அறிமுகப்படுத்தியது.",
        "Milestone Ruling: In Minerva Mills (1980), the Supreme Court confirmed that the proclamation of National Emergency can be challenged on ground of mala fides.",
        "மைல்கல் தீர்ப்பு: மினர்வா மில்ஸ் (1980) வழக்கில், உள்நோக்கத்தின் அடிப்படையில் தேசிய அவசரநிலைப் பிரகடனத்தை சவாலுக்கு உட்படுத்தலாம் என்று உச்ச நீதிமன்றம் உறுதிப்படுத்தியது.",
        "Judicial review is a basic feature of the Constitution that cannot be abrogated.",
        "நீதித்துறை மறுஆய்வு என்பது அரசியலமைப்பின் அடிப்படைக் கட்டமைப்பாகும், அதை நீக்க முடியாது."
    ))

    # 019 - Key C
    qs.append(make_ep_q(
        PREFIX, 19, DIFF, "PYQ MCQ", "Shah Commission Purpose",
        "The Shah Commission of Inquiry (1977) was appointed by the Government of India to investigate: [TNPSC Group 1 2015, Group 2 2018]",
        "ஷா விசாரணைக் குழு (1977) இந்திய அரசால் எதனை விசாரிப்பதற்காக நியமிக்கப்பட்டது? [TNPSC குரூப் 1 2015, குரூப் 2 2018]",
        "Centre-State relations in India", "இந்தியாவில் மத்திய-மாநில உறவுகள்",
        "Administrative reforms in government departments", "அரசுத் துறைகளில் நிர்வாகச் சீர்திருத்தங்கள்",
        "Excesses and abuses of power committed during the 1975 National Emergency", "1975 தேசிய அவசரநிலையின் போது நிகழ்ந்த அதிகார அத்துமீறல்கள் மற்றும் முறைகேடுகள்",
        "Electoral funding and political corruption", "தேர்தல் நிதி மற்றும் அரசியல் ஊழல்",
        "C",
        "The Shah Commission, appointed in May 1977 under former Chief Justice of India J.C. Shah, investigated the circumstances leading to the 1975 Emergency, misuse of censorship, arbitrary arrests, and administrative excesses.",
        "இந்தியாவின் முன்னாள் தலைமை நீதிபதி ஜே.சி. ஷா தலைமையில் மே 1977-ல் அமைக்கப்பட்ட ஷா ஆணையம், 1975 அவசரநிலைக்கு வழிவகுத்த சூழ்நிலைகள், தணிக்கை முறைகேடு, தன்னிச்சையான கைதுகள் மற்றும் நிர்வாக அத்துமீறல்களை விசாரித்தது.",
        "Option A describes the Sarkaria and Punchhi Commissions.", "விருப்பம் A சர்க்காரியா மற்றும் பூஞ்சி ஆணையங்களை விவரிக்கிறது.",
        "Option B describes the Administrative Reforms Commissions (ARC).", "விருப்பம் B நிர்வாகச் சீர்திருத்த ஆணையங்களை (ARC) விவரிக்கிறது.",
        "Option C is correct; Shah Commission investigated 1975 Emergency excesses.", "விருப்பம் C சரியானது; ஷா ஆணையம் 1975 அவசரநிலை அத்துமீறல்களை விசாரித்தது.",
        "Option D describes Dinesh Goswami and Indrajit Gupta committees.", "விருப்பம் D தினேஷ் கோஸ்வாமி மற்றும் இந்திரஜித் குப்தா குழுக்களை விவரிக்கிறது.",
        "Direct Consequence: Findings of the Shah Commission formed the foundation for the landmark 44th Constitutional Amendment Act, 1978.",
        "நேரடி விளைவு: ஷா ஆணையத்தின் கண்டுபிடிப்புகளே 1978-ஆம் ஆண்டின் வரலாற்றுச் சிறப்புமிக்க 44-வது அரசியலமைப்பு திருத்தச் சட்டத்திற்கு அடித்தளமாக அமைந்தன.",
        "The Commission submitted three reports detailing the breakdown of the rule of law during 1975-1977.",
        "1975-1977 காலகட்டத்தில் சட்டத்தின் ஆட்சி முறிந்ததை விவரிக்கும் மூன்று அறிக்கைகளை ஆணையம் சமர்ப்பித்தது."
    ))

    # 020 - Key D
    qs.append(make_ep_q(
        PREFIX, 20, DIFF, "PYQ MCQ", "1975 Emergency Prime Minister",
        "Who was the Prime Minister of India when the third National Emergency (Internal Emergency) was proclaimed in June 1975? [TNPSC Group 4 2018, Group 2 2015]",
        "ஜூன் 1975-ல் மூன்றாவது தேசிய அவசரநிலை (உள்நாட்டு அவசரநிலை) அறிவிக்கப்பட்ட போது இந்தியாவின் பிரதமராக இருந்தவர் யார்? [TNPSC குரூப் 4 2018, குரூப் 2 2015]",
        "Jawaharlal Nehru", "ஜவஹர்லால் நேரு",
        "Lal Bahadur Shastri", "லால் பகதூர் சாஸ்திரி",
        "Morarji Desai", "மொரார்ஜி தேசாய்",
        "Indira Gandhi", "இந்திரா காந்தி",
        "D",
        "Indira Gandhi was the Prime Minister of India when President Fakhruddin Ali Ahmed declared the third National Emergency on June 25, 1975 on the ground of 'internal disturbance'.",
        "1975 ஜூன் 25 அன்று 'உள்நாட்டு அமைதியின்மை' என்ற அடிப்படையில் குடியரசுத் தலைவர் பக்ருதீன் அலி அகமது மூன்றாவது தேசிய அவசரநிலையை அறிவித்த போது இந்திரா காந்தி இந்தியாவின் பிரதமராக இருந்தார்.",
        "Option A (Nehru) was Prime Minister during the 1962 China war emergency.", "விருப்பம் A (நேரு) 1962 சீனப் போர் அவசரநிலையின் போது பிரதமராக இருந்தார்.",
        "Option B (Shastri) was Prime Minister during the 1965 war.", "விருப்பம் B (சாஸ்திரி) 1965 போரின் போது பிரதமராக இருந்தார்.",
        "Option C (Morarji Desai) became Prime Minister in 1977 after the Emergency ended.", "விருப்பம் C (மொரார்ஜி தேசாய்) அவசரநிலை முடிவுக்கு வந்த பின் 1977-ல் பிரதமர் ஆனார்.",
        "Option D is correct; Indira Gandhi recommended the 1975 emergency.", "விருப்பம் D சரியானது; இந்திரா காந்தி 1975 அவசரநிலையைப் பரிந்துரைத்தார்.",
        "Prime Ministers during Emergencies: 1962 = Jawaharlal Nehru; 1971 = Indira Gandhi; 1975 = Indira Gandhi.",
        "அவசரநிலைகளின் போது பிரதமர்கள்: 1962 = ஜவஹர்லால் நேரு; 1971 = இந்திரா காந்தி; 1975 = இந்திரா காந்தி.",
        "The 1975 emergency was recommended by the Prime Minister alone without prior consultation with the Cabinet.",
        "1975 அவசரநிலை அமைச்சரவையைக் கலந்தாலோசிக்காமல் பிரதமரால் மட்டுமே தனிப்பட்ட முறையில் பரிந்துரைக்கப்பட்டது."
    ))

    return qs

def get_pyq_questions_batch3():
    qs = []

    # 021 - Key A
    qs.append(make_ep_q(
        PREFIX, 21, DIFF, "PYQ MCQ", "1975 Emergency President",
        "Who was the President of India who proclaimed the National Emergency on June 25, 1975? [TNPSC Group 1 2014, Group 2 2017]",
        "ஜூன் 25, 1975 அன்று தேசிய அவசரநிலையைப் பிரகடனப்படுத்திய இந்தியக் குடியரசுத் தலைவர் யார்? [TNPSC குரூப் 1 2014, குரூப் 2 2017]",
        "Fakhruddin Ali Ahmed", "பக்ருதீன் அலி அகமது",
        "V.V. Giri", "வி.வி. கிரி",
        "Dr. S. Radhakrishnan", "டாக்டர் எஸ். ராதாகிருஷ்ணன்",
        "Dr. Zakir Husain", "டாக்டர் ஜாகிர் உசேன்",
        "A",
        "Fakhruddin Ali Ahmed was the fifth President of India who signed the proclamation of National Emergency on the night of June 25, 1975, on the advice of Prime Minister Indira Gandhi.",
        "பிரதமர் இந்திரா காந்தியின் ஆலோசனையின் பேரில் ஜூன் 25, 1975 இரவில் தேசிய அவசரநிலைப் பிரகடனத்தில் கையெழுத்திட்ட இந்தியாவின் ஐந்தாவது குடியரசுத் தலைவர் பக்ருதீன் அலி அகமது ஆவார்.",
        "Option A is correct; Fakhruddin Ali Ahmed issued the 1975 proclamation.", "விருப்பம் A சரியானது; பக்ருதீன் அலி அகமது 1975 பிரகடனத்தை வெளியிட்டார்.",
        "Option B (V.V. Giri) proclaimed the 1971 external emergency.", "விருப்பம் B (வி.வி. கிரி) 1971 வெளிப்புற அவசரநிலையைப் பிரகடனப்படுத்தினார்.",
        "Option C (Dr. S. Radhakrishnan) proclaimed the 1962 China war emergency.", "விருப்பம் C (டாக்டர் எஸ். ராதாகிருஷ்ணன்) 1962 சீனப் போர் அவசரநிலையைப் பிரகடனப்படுத்தினார்.",
        "Option D (Dr. Zakir Husain) was President from 1967 to 1969.", "விருப்பம் D (டாக்டர் ஜாகிர் உசேன்) 1967 முதல் 1969 வரை குடியரசுத் தலைவராக இருந்தார்.",
        "Exam Anchor: Presidents during emergencies: 1962 = S. Radhakrishnan; 1971 = V.V. Giri; 1975 = Fakhruddin Ali Ahmed.",
        "தேர்வு நங்கூரம்: அவசரநிலைகளின் போது குடியரசுத் தலைவர்கள்: 1962 = எஸ். ராதாகிருஷ்ணன்; 1971 = வி.வி. கிரி; 1975 = பக்ருதீன் அலி அகமது.",
        "Fakhruddin Ali Ahmed passed away in office in February 1977, shortly before the emergency was revoked.",
        "அவசரநிலை ரத்து செய்யப்படுவதற்குச் சற்று முன்பு, பிப்ரவரி 1977-ல் பக்ருதீன் அலி அகமது பதவியில் இருந்தபோதே காலமானார்."
    ))

    # 022 - Key B
    qs.append(make_ep_q(
        PREFIX, 22, DIFF, "PYQ MCQ", "1962 Emergency President",
        "Who was the President of India who proclaimed the first National Emergency in October 1962 following Chinese aggression? [TNPSC Group 2 2013, Group 1 2015]",
        "அக்டோபர் 1962-ல் சீன ஆக்கிரமிப்பைத் தொடர்ந்து முதல் தேசிய அவசரநிலையைப் பிரகடனப்படுத்திய இந்தியக் குடியரசுத் தலைவர் யார்? [TNPSC குரூப் 2 2013, குரூப் 1 2015]",
        "Dr. Rajendra Prasad", "டாக்டர் ராஜேந்திர பிரசாத்",
        "Dr. S. Radhakrishnan", "டாக்டர் எஸ். ராதாகிருஷ்ணன்",
        "Dr. Zakir Husain", "டாக்டர் ஜாகிர் உசேன்",
        "V.V. Giri", "வி.வி. கிரி",
        "B",
        "Dr. Sarvepalli Radhakrishnan, the second President of India, proclaimed the first National Emergency on October 26, 1962, following the Chinese invasion in the North-East Frontier Agency (NEFA).",
        "வடகிழக்கு எல்லைப்புற முகமை (NEFA) பகுதியில் சீன ஊடுருவலைத் தொடர்ந்து, இந்தியாவின் இரண்டாவது குடியரசுத் தலைவரான டாக்டர் சர்வபள்ளி ராதாகிருஷ்ணன் அக்டோபர் 26, 1962 அன்று முதல் தேசிய அவசரநிலையைப் பிரகடனப்படுத்தினார்.",
        "Option A (Dr. Rajendra Prasad) demitted office in May 1962.", "விருப்பம் A (டாக்டர் ராஜேந்திர பிரசாத்) மே 1962-ல் பதவியிலிருந்து ஓய்வு பெற்றார்.",
        "Option B is correct; Dr. S. Radhakrishnan issued the 1962 proclamation.", "விருப்பம் B சரியானது; டாக்டர் எஸ். ராதாகிருஷ்ணன் 1962 பிரகடனத்தை வெளியிட்டார்.",
        "Option C (Dr. Zakir Husain) assumed office in May 1967.", "விருப்பம் C (டாக்டர் ஜாகிர் உசேன்) மே 1967-ல் பதவியேற்றார்.",
        "Option D (V.V. Giri) proclaimed the 1971 emergency.", "விருப்பம் D (வி.வி. கிரி) 1971 அவசரநிலையைப் பிரகடனப்படுத்தினார்.",
        "Historical Detail: The 1962 proclamation remained in force through the 1965 Indo-Pak war and was revoked only in January 1968.",
        "வரலாற்று விவரம்: 1962 பிரகடனம் 1965 இந்திய-பாகிஸ்தான் போரிலும் தொடர்ந்து நீடித்து, ஜனவரி 1968-ல் மட்டுமே திரும்பப் பெறப்பட்டது.",
        "It lasted for over 5 years, making it the longest single emergency proclamation in Indian history.",
        "இது 5 ஆண்டுகளுக்கும் மேலாக நீடித்தது, இதுவே இந்திய வரலாற்றில் மிக நீண்ட ஒற்றை அவசரநிலைப் பிரகடனமாகும்."
    ))

    # 023 - Key C
    qs.append(make_ep_q(
        PREFIX, 23, DIFF, "PYQ MCQ", "Lok Sabha Special Sitting Notice Requisition",
        "Under Article 352(8), what fraction of the total number of members of the Lok Sabha can give a written notice to requisition a special sitting to disapprove National Emergency? [UPSC 2018, TNPSC Group 1 2021]",
        "சரத்து 352(8)-ன் கீழ், தேசிய அவசரநிலையை நிராகரிப்பதற்காக சிறப்பு அமர்வைக் கூட்டக் கோரி மக்களவையின் மொத்த உறுப்பினர்களில் எத்தனை பங்கு உறுப்பினர்கள் எழுத்துப்பூர்வ அறிவிப்பை அளிக்க வேண்டும்? [UPSC 2018, TNPSC குரூப் 1 2021]",
        "One-fourth (1/4)", "நான்கில் ஒரு பங்கு (1/4)",
        "One-fifth (1/5)", "ஐந்தில் ஒரு பங்கு (1/5)",
        "One-tenth (1/10)", "பத்தில் ஒரு பங்கு (1/10)",
        "One-third (1/3)", "மூன்றில் ஒரு பங்கு (1/3)",
        "C",
        "Under Article 352(8), introduced by the 44th Constitutional Amendment Act 1978, if not less than 1/10th of the total members of the Lok Sabha give written notice, a special sitting must be held within 14 days to consider disapproving the emergency.",
        "1978-ன் 44-வது அரசியலமைப்பு திருத்தச் சட்டத்தால் அறிமுகப்படுத்தப்பட்ட சரத்து 352(8)-ன் கீழ், மக்களவையின் மொத்த உறுப்பினர்களில் 1/10 பங்குக்கு குறையாத உறுப்பினர்கள் எழுத்துப்பூர்வ அறிவிப்பை அளித்தால், அவசரநிலையை நிராகரிப்பது குறித்து பரிசீலிக்க 14 நாட்களுக்குள் சிறப்பு அமர்வு கூட்டப்பட வேண்டும்.",
        "Option A (1/4th) is required to give notice for impeachment of President under Article 61.", "விருப்பம் A (1/4 பங்கு) சரத்து 61-ன் கீழ் குடியரசுத் தலைவர் பதவி நீக்க அறிவிப்புக்குத் தேவைப்படுகிறது.",
        "Option B is an incorrect fraction.", "விருப்பம் B தவறான பின்னமாகும்.",
        "Option C is correct; 1/10th is the exact constitutional quorum requirement.", "விருப்பம் C சரியானது; 1/10 பங்கு என்பதே துல்லியமான அரசியலமைப்புத் தேவையாகும்.",
        "Option D (1/3rd) is the proportion of Rajya Sabha members retiring every two years.", "விருப்பம் D (1/3 பங்கு) இரண்டு ஆண்டுகளுக்கு ஒருமுறை ஓய்வுபெறும் மாநிலங்களவை உறுப்பினர்களின் விகிதமாகும்.",
        "Quorum Link: 1/10th is also the normal quorum to constitute a meeting of either House of Parliament under Article 100(3).",
        "கோரம் இணைப்பு: சரத்து 100(3)-ன் கீழ் பாராளுமன்ற அவைகளின் குறைந்தபட்ச வருகை நிறைவெண்ணும் (Quorum) 1/10 பங்கு ஆகும்.",
        "The written notice is given to the Speaker if the House is in session, or to the President if not in session.",
        "அவை கூட்டத்தொடரில் இருந்தால் சபாநாயகரிடமும், கூட்டத்தொடரில் இல்லாவிட்டால் குடியரசுத் தலைவரிடமும் அறிவிப்பு வழங்கப்படுகிறது."
    ))

    # 024 - Key D
    qs.append(make_ep_q(
        PREFIX, 24, DIFF, "PYQ MCQ", "Time Limit for Special Sitting",
        "Within how many days must a special sitting of the Lok Sabha be held after receiving a valid written notice under Article 352(8) to disapprove a National Emergency? [TNPSC Group 1 2019, Group 2 2015]",
        "தேசிய அவசரநிலையை நிராகரிக்கக் கோரி சரத்து 352(8)-ன் கீழ் சரியான எழுத்துப்பூர்வ அறிவிப்பைப் பெற்ற பிறகு எத்தனை நாட்களுக்குள் மக்களவையின் சிறப்பு அமர்வு கூட்டப்பட வேண்டும்? [TNPSC குரூப் 1 2019, குரூப் 2 2015]",
        "Within 7 days", "7 நாட்களுக்குள்",
        "Within 10 days", "10 நாட்களுக்குள்",
        "Within 30 days", "30 நாட்களுக்குள்",
        "Within 14 days", "14 நாட்களுக்குள்",
        "D",
        "Under Article 352(8), a special sitting of the Lok Sabha must be held within 14 days from the date on which such written notice is received by the Speaker or the President.",
        "சரத்து 352(8)-ன் கீழ், சபாநாயகர் அல்லது குடியரசுத் தலைவரால் இத்தகைய எழுத்துப்பூர்வ அறிவிப்பு பெறப்பட்ட நாளிலிருந்து 14 நாட்களுக்குள் மக்களவையின் சிறப்பு அமர்வு கூட்டப்பட வேண்டும்.",
        "Option A (7 days) is too short.", "விருப்பம் A (7 நாட்கள்) மிகவும் குறுகியது.",
        "Option B (10 days) is incorrect.", "விருப்பம் B (10 நாட்கள்) தவறானது.",
        "Option C (30 days) applies to newly reconstituted Lok Sabha approval.", "விருப்பம் C (30 நாட்கள்) புதிய மக்களவையின் ஒப்புதலுக்குப் பொருந்தும்.",
        "Option D is correct; 14 days is the mandatory constitutional deadline.", "விருப்பம் D சரியானது; 14 நாட்கள் என்பது கட்டாய அரசியலமைப்பு காலக்கெடுவாகும்.",
        "Special Sitting Rule: Notice by 1/10th members -> Special sitting within 14 days -> Disapproval by simple majority.",
        "சிறப்பு அமர்வு விதி: 1/10 பங்கு உறுப்பினர்களின் அறிவிப்பு -> 14 நாட்களுக்குள் சிறப்பு அமர்வு -> எளிய பெரும்பான்மையால் நிராகரிப்பு.",
        "At this sitting, if the House passes a disapproval resolution, the President is bound to revoke the emergency.",
        "இந்த அமர்வில் அவை நிராகரிப்புத் தீர்மானத்தை நிறைவேற்றினால், குடியரசுத் தலைவர் அவசரநிலையைத் திரும்பப் பெறக் கட்டுப்பட்டவர்."
    ))

    # 025 - Key A
    qs.append(make_ep_q(
        PREFIX, 25, DIFF, "PYQ MCQ", "Extension of Lok Sabha Duration",
        "By how much time can the term of the Lok Sabha be extended by Parliament at a time during the operation of a National Emergency? [TNPSC Group 1 2014, Group 2 2018]",
        "தேசிய அவசரநிலை செயல்பாட்டில் இருக்கும் போது பாராளுமன்றத்தால் ஒரு நேரத்தில் மக்களவையின் ஆயுட்காலத்தை எவ்வளவு காலத்திற்கு நீட்டிக்க முடியும்? [TNPSC குரூப் 1 2014, குரூப் 2 2018]",
        "For one year at a time", "ஒரு நேரத்தில் ஒரு வருடம்",
        "For six months at a time", "ஒரு நேரத்தில் ஆறு மாதங்கள்",
        "For two years at a time", "ஒரு நேரத்தில் இரண்டு ஆண்டுகள்",
        "Indefinitely without any yearly limit", "வருடாந்திர வரம்பின்றி காலவரையின்றி",
        "A",
        "Under the proviso to Article 83(2), while a proclamation of emergency is in operation, the normal 5-year term of the Lok Sabha may be extended by Parliament by law for a period not exceeding one year at a time.",
        "சரத்து 83(2)-ன் வரம்புரையின் கீழ், அவசரநிலைப் பிரகடனம் செயல்பாட்டில் இருக்கும் போது, பாராளுமன்றச் சட்டத்தின் மூலம் மக்களவையின் 5 ஆண்டு பதவிக்காலத்தை ஒரு நேரத்தில் ஒரு வருடத்திற்கு மிகாமல் நீட்டிக்க முடியும்.",
        "Option A is correct; it can be extended by one year at a time for any length of time.", "விருப்பம் A சரியானது; ஒரு நேரத்தில் ஒரு வருடம் என எத்தனை முறை வேண்டுமானாலும் நீட்டிக்கலாம்.",
        "Option B (six months) is the maximum period it can continue after the emergency ceases.", "விருப்பம் B (ஆறு மாதங்கள்) அவசரநிலை முடிந்த பின் நீடிக்கக்கூடிய அதிகபட்ச காலமாகும்.",
        "Option C (two years) cannot be granted in a single legislative stroke.", "விருப்பம் C (இரண்டு ஆண்டுகள்) ஒரே சட்டத்தின் மூலம் வழங்கப்பட முடியாது.",
        "Option D ignores the yearly statutory check.", "விருப்பம் D வருடாந்திர சட்டப்பூர்வ கட்டுப்பாட்டைப் புறக்கணிக்கிறது.",
        "Historical Example: During the 1975 Emergency, the term of the 5th Lok Sabha was extended twice, by one year each time.",
        "வரலாற்று உதாரணம்: 1975 அவசரநிலையின் போது, 5-வது மக்களவையின் பதவிக்காலம் தலா ஒரு வருடம் என இரண்டு முறை நீட்டிக்கப்பட்டது.",
        "The same provision applies to State Legislative Assemblies under Article 172(1).",
        "இதே விதி சரத்து 172(1)-ன் கீழ் மாநில சட்டப் பேரவைகளுக்கும் பொருந்தும்."
    ))

    # 026 - Key B
    qs.append(make_ep_q(
        PREFIX, 26, DIFF, "PYQ MCQ", "Post-Emergency Lok Sabha Extension Ceiling",
        "The extension of the term of the Lok Sabha during a National Emergency cannot continue beyond what period after the proclamation of emergency ceases to operate? [TNPSC Group 2 2015, Group 1 2017]",
        "தேசிய அவசரநிலைப் பிரகடனம் முடிவுக்கு வந்த பிறகு, மக்களவையின் பதவிக்கால நீட்டிப்பு எத்தனை காலத்திற்கு மேல் நீடிக்க முடியாது? [TNPSC குரூப் 2 2015, குரூப் 1 2017]",
        "Three months", "மூன்று மாதங்கள்",
        "Six months", "ஆறு மாதங்கள்",
        "One year", "ஒரு வருடம்",
        "Nine months", "ஒன்பது மாதங்கள்",
        "B",
        "Under the proviso to Article 83(2), any extension of the term of the Lok Sabha cannot continue beyond a period of six months after the proclamation has ceased to operate.",
        "சரத்து 83(2)-ன் வரம்புரையின் கீழ், அவசரநிலைப் பிரகடனம் முடிவுக்கு வந்த பிறகு மக்களவையின் எந்தவொரு பதவிக்கால நீட்டிப்பும் ஆறு மாதங்களுக்கு மேல் நீடிக்க முடியாது.",
        "Option A (three months) is incorrect.", "விருப்பம் A (மூன்று மாதங்கள்) தவறானது.",
        "Option B is correct; six months is the constitutional ceiling.", "விருப்பம் B சரியானது; ஆறு மாதங்கள் என்பது அரசியலமைப்பு உச்சவரம்பாகும்.",
        "Option C (one year) is the maximum extension at a time during emergency, not after it ends.", "விருப்பம் C (ஒரு வருடம்) அவசரநிலையின் போது ஒரு முறை நீட்டிக்கப்படும் காலமாகும், முடிந்த பின் அல்ல.",
        "Option D (nine months) is incorrect.", "விருப்பம் D (ஒன்பது மாதங்கள்) தவறானது.",
        "Democratic Safeguard: General elections must be conducted and a new Lok Sabha constituted within 6 months of emergency revocation.",
        "ஜனநாயகப் பாதுகாப்பு: அவசரநிலை திரும்பப் பெறப்பட்ட 6 மாதங்களுக்குள் பொதுத் தேர்தல்கள் நடத்தப்பட்டு புதிய மக்களவை அமைக்கப்பட வேண்டும்.",
        "The 6th Lok Sabha elections were held in March 1977 as soon as the emergency was revoked.",
        "அவசரநிலை ரத்து செய்யப்பட்டவுடன் 1977 மார்ச் மாதத்தில் 6-வது மக்களவைத் தேர்தல்கள் நடத்தப்பட்டன."
    ))

    # 027 - Key C
    qs.append(make_ep_q(
        PREFIX, 27, DIFF, "PYQ MCQ", "Sarkaria Commission Recommendation on Art 356",
        "Which Commission on Centre-State Relations famously recommended that Article 356 should be used only as a 'measure of last resort'? [TNPSC Group 1 2015, Group 2 2019]",
        "சரத்து 356 என்பது 'கடைசிப் புகலிடமாக' மட்டுமே பயன்படுத்தப்பட வேண்டும் என்று பிரபலமாகப் பரிந்துரைத்த மத்திய-மாநில உறவுகள் குறித்த ஆணையம் எது? [TNPSC குரூப் 1 2015, குரூப் 2 2019]",
        "Rajamannar Committee (1969)", "ராஜமன்னார் குழு (1969)",
        "Punchhi Commission (2010)", "பூஞ்சி ஆணையம் (2010)",
        "Sarkaria Commission (1988)", "சர்க்காரியா ஆணையம் (1988)",
        "Administrative Reforms Commission (1966)", "நிர்வாகச் சீர்திருத்த ஆணையம் (1966)",
        "C",
        "The Sarkaria Commission on Centre-State Relations (1988) recommended that Article 356 should be used very sparingly, in extreme cases, as a measure of last resort, when all other alternatives fail.",
        "மத்திய-மாநில உறவுகள் குறித்த சர்க்காரியா ஆணையம் (1988), மற்ற அனைத்து வழிகளும் தோல்வியடையும் போது மட்டுமே தீவிர நிகழ்வுகளில் கடைசிப் புகலிடமாக சரத்து 356 மிகவும் அரிதாகப் பயன்படுத்தப்பட வேண்டும் என்று பரிந்துரைத்தது.",
        "Option A (Rajamannar Committee) set up by Tamil Nadu government recommended the complete deletion of Articles 356 and 357.", "விருப்பம் A (ராஜமன்னார் குழு) சரத்துகள் 356 மற்றும் 357-ஐ முற்றிலும் நீக்கப் பரிந்துரைத்தது.",
        "Option B (Punchhi Commission) proposed the concept of Localised Emergency.", "விருப்பம் B (பூஞ்சி ஆணையம்) உள்ளூர் அவசரநிலைக் கருத்தை முன்வைத்தது.",
        "Option C is correct; Sarkaria Commission coined the 'measure of last resort' doctrine.", "விருப்பம் C சரியானது; சர்க்காரியா ஆணையமே 'கடைசிப் புகலிடக்' கோட்பாட்டை வகுத்தது.",
        "Option D (ARC 1966) dealt with general administrative reforms.", "விருப்பம் D (ARC 1966) பொது நிர்வாகச் சீர்திருத்தங்களைக் கையாண்டது.",
        "TNPSC Standard Question: Rajamannar Committee wanted Articles 356, 357, and 365 completely deleted; Sarkaria Commission wanted strict safeguards and last-resort usage.",
        "TNPSC நிலையான கேள்வி: ராஜமன்னார் குழு சரத்துகள் 356, 357, 365-ஐ நீக்கக் கோரியது; சர்க்காரியா ஆணையம் கடுமையான பாதுகாப்புகளையும் கடைசிப் புகலிடப் பயன்பாட்டையும் கோரியது.",
        "The Supreme Court in S.R. Bommai (1994) adopted most of the Sarkaria Commission recommendations.",
        "எஸ்.ஆர். பொம்மை (1994) வழக்கில் உச்ச நீதிமன்றம் சர்க்காரியா ஆணையத்தின் பெரும்பாலான பரிந்துரைகளை ஏற்றுக்கொண்டது."
    ))

    # 028 - Key D
    qs.append(make_ep_q(
        PREFIX, 28, DIFF, "PYQ MCQ", "Punchhi Commission Localised Emergency",
        "Which Commission recommended that the Constitution should be amended to incorporate 'Localised Emergency' under Article 355? [TNPSC Group 1 2021, UPSC 2018]",
        "சரத்து 355-ன் கீழ் 'உள்ளூர் அவசரநிலை' (Localised Emergency) கொண்டு வரப்படும் வகையில் அரசியலமைப்பு திருத்தப்பட வேண்டும் என்று பரிந்துரைத்த ஆணையம் எது? [TNPSC குரூப் 1 2021, UPSC 2018]",
        "Sarkaria Commission", "சர்க்காரியா ஆணையம்",
        "Venkatachaliah Commission", "வெங்கடாசலையா ஆணையம்",
        "Kothari Commission", "கோத்தாரி ஆணையம்",
        "Punchhi Commission", "பூஞ்சி ஆணையம்",
        "D",
        "The Punchhi Commission on Centre-State Relations (2010), headed by former CJI M.M. Punchhi, recommended 'Localised Emergency' to handle trouble in specific areas without bringing the entire state under central rule.",
        "முன்னாள் தலைமை நீதிபதி எம்.எம். பூஞ்சி தலைமையிலான மத்திய-மாநில உறவுகள் குறித்த பூஞ்சி ஆணையம் (2010), முழு மாநிலத்தையும் மத்திய ஆட்சியின் கீழ் கொண்டுவராமல் குறிப்பிட்ட பகுதிகளில் உள்ள சிக்கல்களைக் கையாள 'உள்ளூர் அவசரநிலை' முறையைப் பரிந்துரைத்தது.",
        "Option A (Sarkaria Commission 1988) recommended last resort usage and Article 355 warnings.", "விருப்பம் A (சர்க்காரியா ஆணையம் 1988) கடைசிப் புகலிடப் பயன்பாட்டையும் சரத்து 355 எச்சரிக்கைகளையும் பரிந்துரைத்தது.",
        "Option B (Venkatachaliah Commission 2002) was the National Commission to Review the Working of the Constitution.", "விருப்பம் B (வெங்கடாசலையா ஆணையம் 2002) அரசியலமைப்புச் செயல்பாட்டை மறுஆய்வு செய்வதற்கான தேசிய ஆணையமாகும்.",
        "Option C (Kothari Commission 1964) dealt with national education policies.", "விருப்பம் C (கோத்தாரி ஆணையம் 1964) தேசியக் கல்விக் கொள்கைகளைக் கையாண்டது.",
        "Option D is correct; Punchhi Commission is the originator of the 'Localised Emergency' proposal.", "விருப்பம் D சரியானது; பூஞ்சி ஆணையமே 'உள்ளூர் அவசரநிலை' திட்டத்தின் மூல கர்த்தா ஆகும்.",
        "Concept Nuance: Localised emergency was proposed for periods not exceeding 3 months to protect local public order without dissolving state governments.",
        "கருத்து நுணுக்கம்: மாநில அரசுகளைக் கலைக்காமல் உள்ளூர் பொது ஒழுங்கைப் பாதுகாக்க 3 மாதங்களுக்கு மிகாத காலத்திற்கு உள்ளூர் அவசரநிலை முன்மொழியப்பட்டது.",
        "The Commission submitted its comprehensive 7-volume report in March 2010.",
        "ஆணையம் தனது விரிவான 7 தொகுதிகள் கொண்ட அறிக்கையை மார்ச் 2010-ல் சமர்ப்பித்தது."
    ))

    # 029 - Key A
    qs.append(make_ep_q(
        PREFIX, 29, DIFF, "PYQ MCQ", "Minerva Mills Landmark Case",
        "In which landmark case did the Supreme Court hold that the proclamation of National Emergency under Article 352 is subject to judicial review on grounds of mala fides? [UPSC 2014, TNPSC Group 1 2019]",
        "சரத்து 352-ன் கீழான தேசிய அவசரநிலைப் பிரகடனம் உள்நோக்கத்தின் அடிப்படையில் நீதித்துறை மறுஆய்வுக்கு உட்பட்டது என்று உச்ச நீதிமன்றம் எந்த வரலாற்று வழக்கில் தீர்ப்பளித்தது? [UPSC 2014, TNPSC குரூப் 1 2019]",
        "Minerva Mills v. Union of India (1980)", "மினர்வா மில்ஸ் எதிர் இந்திய ஒன்றியம் (1980)",
        "Maneka Gandhi v. Union of India (1978)", "மேனகா காந்தி எதிர் இந்திய ஒன்றியம் (1978)",
        "Waman Rao v. Union of India (1981)", "வாமன் ராவ் எதிர் இந்திய ஒன்றியம் (1981)",
        "Indra Sawhney v. Union of India (1992)", "இந்திரா சாவ்னி எதிர் இந்திய ஒன்றியம் (1992)",
        "A",
        "In Minerva Mills v. Union of India (1980), the Supreme Court affirmed that a proclamation of emergency under Article 352 can be challenged in court on the ground that it was made mala fide or that it was based on wholly extraneous facts.",
        "மினர்வா மில்ஸ் எதிர் இந்திய ஒன்றியம் (1980) வழக்கில், உள்நோக்கத்துடனோ அல்லது முற்றிலும் தொடர்பற்ற காரணங்களின் அடிப்படையிலோ அமைந்திருந்தால் சரத்து 352-ன் கீழான அவசரநிலைப் பிரகடனத்தை நீதிமன்றத்தில் சவாலுக்கு உட்படுத்தலாம் என்று உச்ச நீதிமன்றம் உறுதிப்படுத்தியது.",
        "Option A is correct; Minerva Mills settled judicial review over Article 352.", "விருப்பம் A சரியானது; மினர்வா மில்ஸ் வழக்கு சரத்து 352 மீதான நீதித்துறை மறுஆய்வை நிலைநிறுத்தியது.",
        "Option B expanded the scope of personal liberty under Article 21.", "விருப்பம் B சரத்து 21-ன் கீழான தனிநபர் சுதந்திரத்தின் எல்லையை விரிவுபடுத்தியது.",
        "Option C dealt with the Ninth Schedule and Basic Structure cut-off date (April 24, 1973).", "விருப்பம் C ஒன்பதாவது அட்டவணை மற்றும் அடிப்படைக் கட்டமைப்பு காலக்கெடுவைக் கையாண்டது.",
        "Option D dealt with OBC reservations and the 50% ceiling.", "விருப்பம் D ஓபிசி இடஒதுக்கீடு மற்றும் 50% உச்சவரம்பைக் கையாண்டது.",
        "Twin Judicial Precedents: Article 352 Judicial Review = Minerva Mills (1980); Article 356 Judicial Review = S.R. Bommai (1994).",
        "இரட்டை நீதித்துறை முன்மாதிரிகள்: சரத்து 352 நீதித்துறை மறுஆய்வு = மினர்வா மில்ஸ் (1980); சரத்து 356 நீதித்துறை மறுஆய்வு = எஸ்.ஆர். பொம்மை (1994).",
        "Minerva Mills also struck down Section 4 and Section 55 of the 42nd Amendment Act.",
        "மினர்வா மில்ஸ் வழக்கு 42-வது திருத்தச் சட்டத்தின் பிரிவு 4 மற்றும் பிரிவு 55-ஐயும் ரத்து செய்தது."
    ))

    # 030 - Key B
    qs.append(make_ep_q(
        PREFIX, 30, DIFF, "PYQ MCQ", "Habeas Corpus Case Title",
        "The infamous 'Habeas Corpus case' decided by the Supreme Court during the 1975 Emergency is officially known as: [TNPSC Group 1 2017, UPSC 2019]",
        "1975 அவசரநிலையின் போது உச்ச நீதிமன்றத்தால் தீர்ப்பளிக்கப்பட்ட பிரபலமற்ற 'ஆட்கொணர்வு வழக்கு' அதிகாரப்பூர்வமாக எவ்வாறு அழைக்கப்படுகிறது? [TNPSC குரூப் 1 2017, UPSC 2019]",
        "A.K. Gopalan v. State of Madras (1950)", "ஏ.கே. கோபாலன் எதிர் மதராஸ் அரசு (1950)",
        "A.D.M. Jabalpur v. Shivkant Shukla (1976)", "ஏ.டி.எம். ஜபல்பூர் எதிர் சிவகாந்த் சுக்லா (1976)",
        "Sunil Batra v. Delhi Administration (1980)", "சுனில் பத்ரா எதிர் தில்லி நிர்வாகம் (1980)",
        "R.C. Cooper v. Union of India (1970)", "ஆர்.சி. கூப்பர் எதிர் இந்திய ஒன்றியம் (1970)",
        "B",
        "A.D.M. Jabalpur v. Shivkant Shukla (1976), commonly known as the Habeas Corpus case, was a 4:1 ruling holding that during emergency, a citizen had no locus standi to approach courts to enforce Article 21.",
        "பொதுவாக ஆட்கொணர்வு வழக்கு என அழைக்கப்படும் ஏ.டி.எம். ஜபல்பூர் எதிர் சிவகாந்த் சுக்லா (1976), அவசரநிலையின் போது சரத்து 21-ஐ நிலைநாட்ட குடிமக்கள் நீதிமன்றங்களை அணுக எந்த முகாந்திரமும் இல்லை என்று கூறிய 4:1 பெரும்பான்மைத் தீர்ப்பாகும்.",
        "Option A was an early preventive detention case dealing with 'procedure established by law'.", "விருப்பம் A 'சட்டத்தால் நிலைநாட்டப்பட்ட நடைமுறை' தொடர்பான ஆரம்பகாலத் தடுப்புக் காவல் வழக்காகும்.",
        "Option B is correct; A.D.M. Jabalpur is the landmark Habeas Corpus case.", "விருப்பம் B சரியானது; ஏ.டி.எம். ஜபல்பூர் வழக்கே புகழ்பெற்ற ஆட்கொணர்வு வழக்காகும்.",
        "Option C dealt with prison reforms and rights of prisoners.", "விருப்பம் C சிறைச் சீர்திருத்தங்கள் மற்றும் கைதிகளின் உரிமைகள் தொடர்பானது.",
        "Option D was the Bank Nationalisation case.", "விருப்பம் D வங்கி தேசியமயமாக்கல் வழக்காகும்.",
        "Judicial Overruling: A.D.M. Jabalpur was explicitly declared an erroneous and overruled judgment by a 9-judge bench in K.S. Puttaswamy (2017).",
        "நீதித்துறை ரத்து: ஏ.டி.எம். ஜபல்பூர் தவறான தீர்ப்பு என்று கே.எஸ். புட்டசுவாமி (2017) வழக்கில் 9 நீதிபதிகள் கொண்ட அமர்வால் வெளிப்படையாக ரத்து செய்யப்பட்டது.",
        "The Supreme Court observed that Justice H.R. Khanna's dissent was the correct interpretation of the Constitution.",
        "நீதிபதி எச்.ஆர். கண்ணாவின் மாறுபட்ட தீர்ப்பே அரசியலமைப்பின் சரியான விளக்கம் என்று உச்ச நீதிமன்றம் குறிப்பிட்டது."
    ))

    return qs

def get_pyq_questions_batch4():
    qs = []

    # 031 - Key C
    qs.append(make_ep_q(
        PREFIX, 31, DIFF, "PYQ MCQ", "Sole Dissenter in Habeas Corpus Case",
        "Who was the lone dissenting judge in A.D.M. Jabalpur v. Shivkant Shukla (1976) who upheld that the right to life cannot be extinguished even during an emergency? [TNPSC Group 1 2019, UPSC 2018]",
        "அவசரநிலையின் போது கூட வாழ்வுரிமையை அழிக்க முடியாது என்று கூறி, ஏ.டி.எம். ஜபல்பூர் எதிர் சிவகாந்த் சுக்லா (1976) வழக்கில் தனித்து மாறுபட்ட தீர்ப்பை வழங்கிய ஒரே நீதிபதி யார்? [TNPSC குரூப் 1 2019, UPSC 2018]",
        "Justice P.N. Bhagwati", "நீதிபதி பி.என். பகவதி",
        "Justice Y.V. Chandrachud", "நீதிபதி ஒய்.வி. சந்திரசூட்",
        "Justice H.R. Khanna", "நீதிபதி எச்.ஆர். கண்ணா",
        "Chief Justice A.N. Ray", "தலைமை நீதிபதி ஏ.என். ரே",
        "C",
        "Justice Hans Raj Khanna was the sole dissenter in A.D.M. Jabalpur (1976). He famously wrote that 'detention without trial is an anathema to all those who love personal liberty.' He was subsequently superseded for the post of Chief Justice of India by Justice M.H. Beg.",
        "ஏ.டி.எம். ஜபல்பூர் (1976) வழக்கில் தனித்து மாறுபட்ட தீர்ப்பை வழங்கிய ஒரே நீதிபதி ஹன்ஸ் ராஜ் கண்ணா ஆவார். 'விசாரணையின்றி சிறை வைப்பது என்பது தனிநபர் சுதந்திரத்தை நேசிக்கும் அனைவருக்கும் ஒரு சாபக்கேடு' என்று அவர் புகழ்பெற்ற வரிகளை எழுதினார். இதன் காரணமாக தலைமை நீதிபதி பதவியில் நீதிபதி எம்.எச். பெக்கால் அவர் புறக்கணிக்கப்பட்டார்.",
        "Option A (Justice Bhagwati) concurred with the majority, though he later expressed regret.", "விருப்பம் A (நீதிபதி பகவதி) பெரும்பான்மையுடன் உடன்பட்டார், பின்னர் வருத்தம் தெரிவித்தார்.",
        "Option B (Justice Chandrachud) was part of the majority bench.", "விருப்பம் B (நீதிபதி சந்திரசூட்) பெரும்பான்மை அமர்வில் இடம்பெற்றிருந்தார்.",
        "Option C is correct; Justice H.R. Khanna is celebrated for his courageous dissent.", "விருப்பம் C சரியானது; நீதிபதி எச்.ஆர். கண்ணா தனது துணிச்சலான மாறுபட்ட தீர்ப்பிற்காகப் போற்றப்படுகிறார்.",
        "Option D (CJI A.N. Ray) authored the majority judgment.", "விருப்பம் D (தலைமை நீதிபதி ஏ.என். ரே) பெரும்பான்மைத் தீர்ப்பை எழுதினார்.",
        "Judicial Legend: Justice Khanna's portrait hangs in Courtroom 2 of the Supreme Court of India in tribute to judicial integrity.",
        "நீதித்துறை ஜாம்பவான்: நீதித்துறை நேர்மைக்கு அஞ்சலி செலுத்தும் வகையில் இந்திய உச்ச நீதிமன்றத்தின் 2-வது நீதிமன்ற அறையில் நீதிபதி கண்ணாவின் உருவப்படம் வைக்கப்பட்டுள்ளது.",
        "His courageous dissent inspired the worldwide legal community and shaped the 44th Amendment safeguards.",
        "அவரது துணிச்சலான மாறுபட்ட தீர்ப்பு உலகெங்கிலும் உள்ள சட்ட சமூகத்தை ஈர்த்ததுடன் 44-வது திருத்தப் பாதுகாப்புகளையும் வடிவமைத்தது."
    ))

    # 032 - Key D
    qs.append(make_ep_q(
        PREFIX, 32, DIFF, "PYQ MCQ", "Overruling of Habeas Corpus Case",
        "In which landmark 9-judge Constitution Bench judgment was the majority ruling in A.D.M. Jabalpur v. Shivkant Shukla (1976) formally and expressly overruled? [TNPSC Group 1 2021, UPSC 2019]",
        "ஏ.டி.எம். ஜபல்பூர் எதிர் சிவகாந்த் சுக்லா (1976) வழக்கின் பெரும்பான்மைத் தீர்ப்பானது எந்த வரலாற்றுச் சிறப்புமிக்க 9 நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வுத் தீர்ப்பில் முறையாகவும் வெளிப்படையாகவும் ரத்து செய்யப்பட்டது? [TNPSC குரூப் 1 2021, UPSC 2019]",
        "Shayara Bano v. Union of India (2017)", "ஷயாரா பானோ எதிர் இந்திய ஒன்றியம் (2017)",
        "Navtej Singh Johar v. Union of India (2018)", "நவ்தேஜ் சிங் ஜோஹர் எதிர் இந்திய ஒன்றியம் (2018)",
        "Joseph Shine v. Union of India (2018)", "ஜோசப் ஷைன் எதிர் இந்திய ஒன்றியம் (2018)",
        "Justice K.S. Puttaswamy v. Union of India (2017)", "நீதிபதி கே.எஸ். புட்டசுவாமி எதிர் இந்திய ஒன்றியம் (2017)",
        "D",
        "In Justice K.S. Puttaswamy v. Union of India (2017 - Right to Privacy case), a 9-judge bench unanimously overruled A.D.M. Jabalpur. Justice D.Y. Chandrachud (son of Justice Y.V. Chandrachud who had been on the 1976 bench) expressly declared the 1976 decision 'seriously flawed'.",
        "நீதிபதி கே.எஸ். புட்டசுவாமி எதிர் இந்திய ஒன்றியம் (2017 - தனிஉரிமை வழக்கு) வழக்கில், 9 நீதிபதிகள் கொண்ட அமர்வு ஏ.டி.எம். ஜபல்பூர் தீர்ப்பை ஏகமனதாக ரத்து செய்தது. 1976 அமர்வில் இருந்த நீதிபதி ஒய்.வி. சந்திரசூட்டின் மகனான நீதிபதி டி.ஒய். சந்திரசூட், 1976 தீர்ப்பை 'கடுமையான குறைபாடுடையது' என்று வெளிப்படையாக அறிவித்தார்.",
        "Option A was the Triple Talaq ruling.", "விருப்பம் A முத்தலாக் வழக்காகும்.",
        "Option B decriminalized Section 377 IPC.", "விருப்பம் B ஐபிசி பிரிவு 377-ஐ குற்றமற்றதாக்கியது.",
        "Option C decriminalized adultery under Section 497 IPC.", "விருப்பம் C ஐபிசி பிரிவு 497-ன் கீழான திருமணத்திற்கு புறம்பான உறவைக் குற்றமற்றதாக்கியது.",
        "Option D is correct; the 9-judge Puttaswamy bench overruled A.D.M. Jabalpur.", "விருப்பம் D சரியானது; 9 நீதிபதிகள் கொண்ட புட்டசுவாமி அமர்வு ஏ.டி.எம். ஜபல்பூரை ரத்து செய்தது.",
        "Historic Judicial Redemption: Dr. D.Y. Chandrachud overruled his own father's judgment in this landmark decision.",
        "வரலாற்று நீதித்துறைத் திருத்தம்: இந்த வரலாற்றுத் தீர்ப்பில் டாக்டர் டி.ஒய். சந்திரசூட் தனது சொந்த தந்தையின் தீர்ப்பையே ரத்து செய்தார்.",
        "The judgment recognized the Right to Privacy as an intrinsic part of the Right to Life under Article 21.",
        "இத்தீர்ப்பு தனிஉரிமையை (Right to Privacy) சரத்து 21-ன் கீழான வாழ்வுரிமையின் உள்ளார்ந்த பகுதியாக அங்கீகரித்தது."
    ))

    # 033 - Key A
    qs.append(make_ep_q(
        PREFIX, 33, DIFF, "PYQ MCQ", "President's Acts Definition",
        "During the operation of President's Rule under Article 356, when Parliament confers legislative powers on the President, the laws made by the President are known as: [TNPSC Group 1 2015, Group 2 2017]",
        "சரத்து 356-ன் கீழான குடியரசுத் தலைவர் ஆட்சியின் போது, பாராளுமன்றம் சட்டம் இயற்றும் அதிகாரத்தை குடியரசுத் தலைவருக்கு வழங்கும் போது, குடியரசுத் தலைவரால் இயற்றப்படும் சட்டங்கள் எவ்வாறு அழைக்கப்படுகின்றன? [TNPSC குரூப் 1 2015, குரூப் 2 2017]",
        "President's Acts", "குடியரசுத் தலைவர் சட்டங்கள்",
        "President's Ordinances", "குடியரசுத் தலைவர் அவசரச் சட்டங்கள்",
        "Executive Decrees", "நிர்வாக ஆணைகள்",
        "Governor's Regulations", "ஆளுநர் ஒழுங்குமுறைகள்",
        "A",
        "Under Article 357(1)(a), Parliament can delegate its law-making power for the State to the President. Laws enacted by the President under this delegated authority are officially styled as 'President's Acts'.",
        "சரத்து 357(1)(a)-ன் கீழ், மாநிலத்திற்கான தனது சட்டவாக்க அதிகாரத்தை பாராளுமன்றம் குடியரசுத் தலைவருக்கு வழங்க முடியும். இந்த அதிகாரத்தின் கீழ் குடியரசுத் தலைவரால் இயற்றப்படும் சட்டங்கள் அதிகாரப்பூர்வமாக 'குடியரசுத் தலைவர் சட்டங்கள்' (President's Acts) என அழைக்கப்படுகின்றன.",
        "Option A is correct; they are enacted as President's Acts.", "விருப்பம் A சரியானது; அவை குடியரசுத் தலைவர் சட்டங்களாக இயற்றப்படுகின்றன.",
        "Option B refers to temporary ordinances issued under Article 123.", "விருப்பம் B சரத்து 123-ன் கீழ் பிறப்பிக்கப்படும் தற்காலிக அவசரச் சட்டங்களைக் குறிக்கிறது.",
        "Option C is a term used in civil law jurisdictions, not India.", "விருப்பம் C இந்தியாவிற்குப் பொருந்தாத வெளிநாட்டுச் சொல்லாகும்.",
        "Option D refers to tribal area regulations under Fifth/Sixth Schedules.", "விருப்பம் D ஐந்து/ஆறாவது அட்டவணைகளின் கீழான பழங்குடியின ஒழுங்குமுறைகளைக் குறிக்கிறது.",
        "Consultative Process: The President usually enacts such laws in consultation with a Parliamentary Consultative Committee comprising MPs from that State.",
        "ஆலோசனைக் குழு: குடியரசுத் தலைவர் வழக்கமாக அந்த மாநிலத்தைச் சேர்ந்த பாராளுமன்ற உறுப்பினர்களைக் கொண்ட ஆலோசனைக் குழுவுடன் கலந்தாலோசித்து இத்தகைய சட்டங்களை இயற்றுகிறார்.",
        "These laws have the same legal force and effect as Acts passed by the State Legislature.",
        "இச்சட்டங்கள் மாநில சட்டமன்றத்தால் நிறைவேற்றப்பட்ட சட்டங்களைப் போன்றே அதே சட்ட வலிமையையும் விளைவையும் கொண்டுள்ளன."
    ))

    # 034 - Key B
    qs.append(make_ep_q(
        PREFIX, 34, DIFF, "PYQ MCQ", "Continuance of Laws After President's Rule",
        "Under Article 357(2) as amended by the 44th Constitutional Amendment Act 1978, how long do laws made by Parliament or the President during President's Rule continue in force after the proclamation ends? [TNPSC Group 1 2019, Group 2 2018]",
        "1978-ன் 44-வது அரசியலமைப்பு திருத்தச் சட்டத்தால் திருத்தப்பட்ட சரத்து 357(2)-ன் படி, குடியரசுத் தலைவர் ஆட்சி முடிவுக்கு வந்த பிறகு பாராளுமன்றம் அல்லது குடியரசுத் தலைவரால் இயற்றப்பட்ட சட்டங்கள் எவ்வளவு காலம் வரை தொடர்ந்து நடைமுறையில் இருக்கும்? [TNPSC குரூப் 1 2019, குரூப் 2 2018]",
        "They lapse automatically immediately upon the revocation of President's Rule", "குடியரசுத் தலைவர் ஆட்சி ரத்தான உடனேயே அவை தானாகவே காலாவதியாகிவிடும்",
        "They continue in force until altered, repealed, or amended by the State Legislature", "மாநில சட்டமன்றம் அவற்றை மாற்றும், ரத்து செய்யும் அல்லது திருத்தும் வரை அவை தொடர்ந்து நடைமுறையில் இருக்கும்",
        "They expire exactly six months after the revocation of the proclamation", "பிரகடனம் ரத்து செய்யப்பட்ட நாளிலிருந்து சரியாக ஆறு மாதங்களுக்குப் பிறகு அவை காலாவதியாகிவிடும்",
        "They expire exactly one year after the revocation of the proclamation", "பிரகடனம் ரத்து செய்யப்பட்ட நாளிலிருந்து சரியாக ஒரு வருடத்திற்குப் பிறகு அவை காலாவதியாகிவிடும்",
        "B",
        "Under Article 357(2) as amended by the 44th Constitutional Amendment Act 1978, any law made by Parliament or the President during President's Rule continues in force until altered, repealed, or amended by a competent Legislature or other authority.",
        "1978-ன் 44-வது அரசியலமைப்பு திருத்தச் சட்டத்தால் திருத்தப்பட்ட சரத்து 357(2)-ன் கீழ், குடியரசுத் தலைவர் ஆட்சியின் போது இயற்றப்பட்ட எந்தவொரு சட்டமும் தகுதிவாய்ந்த சட்டமன்றத்தால் அல்லது அதிகார அமைப்பால் மாற்றப்படும், ரத்து செய்யப்படும் அல்லது திருத்தப்படும் வரை தொடர்ந்து நடைமுறையில் இருக்கும்.",
        "Option A is incorrect because automatic lapsing does not occur.", "விருப்பம் A தவறு, ஏனெனில் தானியங்கு காலாவதி ஏற்படுவதில்லை.",
        "Option B is correct; the laws continue indefinitely until altered by the state assembly.", "விருப்பம் B சரியானது; மாநில சட்டமன்றம் மாற்றும் வரை சட்டங்கள் காலவரையின்றித் தொடரும்.",
        "Option C confuses this with Article 250(2) National Emergency laws.", "விருப்பம் C இதை சரத்து 250(2) தேசிய அவசரநிலைச் சட்டங்களுடன் குழப்பிக் கொள்கிறது.",
        "Option D was the rule before the 44th Amendment Act, 1978.", "விருப்பம் D என்பது 1978-ஆம் ஆண்டின் 44-வது திருத்தத்திற்கு முந்தைய விதியாகும்.",
        "Historical Shift: Prior to 1978, laws lapsed 1 year after the proclamation ceased. The 44th Amendment eliminated the one-year clause to prevent statutory vacuums.",
        "வரலாற்று மாற்றம்: 1978-க்கு முன்பு, பிரகடனம் முடிந்து 1 வருடத்தில் சட்டங்கள் காலாவதியாயின. சட்ட வெற்றிடத்தைத் தவிர்க்க 44-வது திருத்தம் 1 ஆண்டு விதியை நீக்கியது.",
        "The newly elected State Legislature has full sovereign power to either retain, modify, or repeal these laws.",
        "புதிதாகத் தேர்ந்தெடுக்கப்பட்ட மாநில சட்டமன்றத்திற்கு இச்சட்டங்களைத் தக்கவைக்கவோ, மாற்றவோ அல்லது ரத்து செய்யவோ முழு இறையாண்மை அதிகாரம் உண்டு."
    ))

    # 035 - Key C
    qs.append(make_ep_q(
        PREFIX, 35, DIFF, "PYQ MCQ", "Article 354 Revenue Distribution Modification",
        "Under Article 354, the President of India can modify the distribution of revenues between the Union and the States during which type of emergency? [TNPSC Group 1 2017, Group 2 2015]",
        "சரத்து 354-ன் கீழ், எந்த வகையான அவசரநிலையின் போது மத்திய மற்றும் மாநிலங்களுக்கு இடையிலான வருவாய் பகிர்வைக் குடியரசுத் தலைவர் மாற்றியமைக்க முடியும்? [TNPSC குரூப் 1 2017, குரூப் 2 2015]",
        "President's Rule under Article 356 only", "சரத்து 356-ன் கீழான குடியரசுத் தலைவர் ஆட்சியின் போது மட்டுமே",
        "Financial Emergency under Article 360 only", "சரத்து 360-ன் கீழான நிதி அவசரநிலையின் போது மட்டுமே",
        "National Emergency under Article 352", "சரத்து 352-ன் கீழான தேசிய அவசரநிலையின் போது",
        "Any localized crisis declared by the Governor", "ஆளுநரால் அறிவிக்கப்படும் ஏதேனும் உள்ளூர் நெருக்கடியின் போது",
        "C",
        "Under Article 354, while a proclamation of National Emergency under Article 352 is in operation, the President may by order direct that all or any of the provisions of Articles 268 to 279 relating to the distribution of revenues shall have effect subject to such exceptions or modifications as he thinks fit.",
        "சரத்து 354-ன் கீழ், சரத்து 352-ன் கீழான தேசிய அவசரநிலை செயல்பாட்டில் இருக்கும் போது, வருவாய் பகிர்வு தொடர்பான சரத்துகள் 268 முதல் 279 வரையிலான விதிகளைத் தான் தகுதியெனக் கருதும் விதிவிலக்குகள் அல்லது மாற்றங்களுக்கு உட்பட்டுச் செயல்பட குடியரசுத் தலைவர் ஆணையிடலாம்.",
        "Option A is incorrect because Article 354 applies specifically to National Emergency, not President's Rule.", "விருப்பம் A தவறு, ஏனெனில் சரத்து 354 தேசிய அவசரநிலைக்குப் பொருந்துமே தவிர குடியரசுத் தலைவர் ஆட்சிக்கு அல்ல.",
        "Option B is incorrect; Financial Emergency is governed by Article 360.", "விருப்பம் B தவறு; நிதி அவசரநிலை சரத்து 360-ஆல் நிர்வகிக்கப்படுகிறது.",
        "Option C is correct; Article 354 operates during National Emergency under Article 352.", "விருப்பம் C சரியானது; சரத்து 354 சரத்து 352-ன் கீழான தேசிய அவசரநிலையின் போது செயல்படுகிறது.",
        "Option D is non-constitutional.", "விருப்பம் D அரசியலமைப்பில் இல்லாததாகும்.",
        "Duration Rule: An order made under Article 354 cannot extend beyond the financial year in which the emergency ceases.",
        "கால அளவு விதி: சரத்து 354-ன் கீழ் பிறப்பிக்கப்படும் ஆணை அவசரநிலை முடிவுக்கு வரும் நிதியாண்டிற்கு அப்பால் நீடிக்க முடியாது.",
        "All such presidential orders must be laid before each House of Parliament.",
        "இத்தகைய அனைத்து குடியரசுத் தலைவர் ஆணைகளும் பாராளுமன்றத்தின் இரு அவைகளிலும் வைக்கப்பட வேண்டும்."
    ))

    # 036 - Key D
    qs.append(make_ep_q(
        PREFIX, 36, DIFF, "PYQ MCQ", "Immunity of High Courts Under Article 356",
        "During President's Rule in a State under Article 356, which constitutional institution's powers CANNOT be assumed or suspended by the President? [TNPSC Group 1 2014, Group 2 2019, UPSC 2013]",
        "சரத்து 356-ன் கீழ் ஒரு மாநிலத்தில் குடியரசுத் தலைவர் ஆட்சி நடைபெறும் போது, எந்த அரசியலமைப்பு அமைப்பின் அதிகாரங்களை குடியரசுத் தலைவர் ஏற்கவோ அல்லது இடைநிறுத்தவோ முடியாது? [TNPSC குரூப் 1 2014, குரூப் 2 2019, UPSC 2013]",
        "The State Legislative Assembly", "மாநில சட்டமன்றப் பேரவை",
        "The State Council of Ministers", "மாநில அமைச்சரவை",
        "The State Public Service Commission", "மாநில அரசுப் பணியாளர் தேர்வாணையம்",
        "The High Court of the State", "மாநில உயர்நீதிமன்றம்",
        "D",
        "The proviso to Article 356(1) explicitly states: 'Provided that nothing in this clause shall authorise the President to assume to himself any of the powers vested in or exercisable by a High Court, or to suspend in whole or in part the operation of any provision of this Constitution relating to High Courts.'",
        "சரத்து 356(1)-ன் வரம்புரை தெளிவாகக் கூறுகிறது: 'உயர்நீதிமன்றத்திற்கு வழங்கப்பட்டுள்ள அல்லது பயன்படுத்தக்கூடிய அதிகாரங்கள் எதனையும் தாமே ஏற்பதற்கோ அல்லது உயர்நீதிமன்றங்கள் தொடர்பான அரசியலமைப்பு விதிகளை முழுமையாகவோ பகுதியாகவோ இடைநிறுத்துவதற்கோ இந்த விதியில் உள்ள எதுவும் குடியரசுத் தலைவருக்கு அதிகாரம் அளிக்காது.'",
        "Option A can be suspended or dissolved.", "விருப்பம் A இடைநிறுத்தப்படலாம் அல்லது கலைக்கப்படலாம்.",
        "Option B is dismissed immediately upon proclamation.", "விருப்பம் B பிரகடனப்படுத்தப்பட்ட உடனேயே பதவி நீக்கம் செய்யப்படுகிறது.",
        "Option C functions under governor's administration.", "விருப்பம் C ஆளுநரின் நிர்வாகத்தின் கீழ் செயல்படுகிறது.",
        "Option D is correct; the High Court enjoys absolute constitutional immunity during President's Rule.", "விருப்பம் D சரியானது; குடியரசுத் தலைவர் ஆட்சியின் போது உயர்நீதிமன்றம் முழுமையான அரசியலமைப்புப் பாதுகாப்பைப் பெறுகிறது.",
        "Separation of Powers: Even when the state executive and legislature are displaced, the state judiciary functions completely independently.",
        "அதிகாரப் பகிர்வு: மாநில நிர்வாகமும் சட்டமன்றமும் மாற்றப்படும் போது கூட, மாநில நீதித்துறை முற்றிலும் சுதந்திரமாகச் செயல்படுகிறது.",
        "Citizens can continue to move the High Court under Article 226 for enforcement of fundamental and legal rights during President's Rule.",
        "குடியரசுத் தலைவர் ஆட்சியின் போது குடிமக்கள் தங்களின் அடிப்படை மற்றும் சட்ட உரிமைகளுக்காக சரத்து 226-ன் கீழ் உயர்நீதிமன்றத்தை தொடர்ந்து அணுக முடியும்."
    ))

    # 037 - Key A
    qs.append(make_ep_q(
        PREFIX, 37, DIFF, "PYQ MCQ", "Article 357 Scope",
        "Which Article of the Constitution of India deals with the 'Exercise of Legislative Powers under proclamation issued under Article 356'? [TNPSC Group 2 2015, Group 1 2017]",
        "சரத்து 356-ன் கீழ் வெளியிடப்பட்ட பிரகடனத்தின் கீழ் 'சட்டவாக்க அதிகாரங்களைப் பயன்படுத்துதல்' பற்றிக் கையாளும் இந்திய அரசியலமைப்பின் சரத்து எது? [TNPSC குரூப் 2 2015, குரூப் 1 2017]",
        "Article 357", "சரத்து 357",
        "Article 358", "சரத்து 358",
        "Article 359", "சரத்து 359",
        "Article 353", "சரத்து 353",
        "A",
        "Article 357 governs the exercise of legislative powers under President's Rule (Article 356), enabling Parliament to confer law-making powers on the President and authorize expenditure from the State Consolidated Fund.",
        "சரத்து 357 குடியரசுத் தலைவர் ஆட்சியின் (சரத்து 356) கீழான சட்டவாக்க அதிகாரங்களைப் பயன்படுத்துவதை நிர்வகிக்கிறது; இது பாராளுமன்றம் சட்டம் இயற்றும் அதிகாரத்தைக் குடியரசுத் தலைவருக்கு வழங்கவும், மாநிலத் தொகுப்பு நிதியிலிருந்து செலவினங்களை அங்கீகரிக்கவும் உதவுகிறது.",
        "Option A is correct; Article 357 is the legislative companion to Article 356.", "விருப்பம் A சரியானது; சரத்து 357 என்பது சரத்து 356-ன் சட்டவாக்கத் துணையாகும்.",
        "Option B (Article 358) suspends Article 19 during external emergency.", "விருப்பம் B (சரத்து 358) வெளிப்புற அவசரநிலையின் போது சரத்து 19-ஐ இடைநிறுத்துகிறது.",
        "Option C (Article 359) suspends enforcement of specified fundamental rights.", "விருப்பம் C (சரத்து 359) குறிப்பிட்ட அடிப்படை உரிமைகளின் அமலாக்கத்தை இடைநிறுத்துகிறது.",
        "Option D (Article 353) deals with executive and legislative effects during National Emergency.", "விருப்பம் D (சரத்து 353) தேசிய அவசரநிலையின் போது நிர்வாக மற்றும் சட்டவாக்க விளைவுகளைக் கையாள்கிறது.",
        "Article Mapping: Article 356 = Proclamation of President's Rule; Article 357 = Exercise of Legislative Powers under Article 356.",
        "சரத்து வரைபடம்: சரத்து 356 = குடியரசுத் தலைவர் ஆட்சி பிரகடனம்; சரத்து 357 = சரத்து 356-ன் கீழான சட்டவாக்க அதிகாரங்களைப் பயன்படுத்துதல்.",
        "Article 357 also empowers the President to make laws when the Lok Sabha is not in session.",
        "மக்களவை கூட்டத்தொடரில் இல்லாத போது சட்டங்களை இயற்றவும் குடியரசுத் தலைவருக்கு சரத்து 357 அதிகாரம் அளிக்கிறது."
    ))

    # 038 - Key B
    qs.append(make_ep_q(
        PREFIX, 38, DIFF, "PYQ MCQ", "Periodic Extension of President's Rule",
        "Once approved by Parliament, for what period does President's Rule under Article 356 continue at a time? [TNPSC Group 1 2012, Group 2 2018]",
        "பாராளுமன்றத்தால் ஒப்புதல் அளிக்கப்பட்டவுடன், சரத்து 356-ன் கீழான குடியரசுத் தலைவர் ஆட்சி ஒரு நேரத்தில் எவ்வளவு காலம் நீடிக்கும்? [TNPSC குரூப் 1 2012, குரூப் 2 2018]",
        "Three months", "மூன்று மாதங்கள்",
        "Six months", "ஆறு மாதங்கள்",
        "One year", "ஒரு வருடம்",
        "Two years", "இரண்டு ஆண்டுகள்",
        "B",
        "Under Article 356(4), once approved by both Houses of Parliament, President's Rule continues for a period of six months from the date of proclamation (or previous expiry), and can be extended every six months up to a maximum of three years.",
        "சரத்து 356(4)-ன் கீழ், பாராளுமன்றத்தின் இரு அவைகளாலும் ஒப்புதல் அளிக்கப்பட்டவுடன், குடியரசுத் தலைவர் ஆட்சி பிரகடனப்படுத்தப்பட்ட நாளிலிருந்து ஆறு மாத காலத்திற்கு நீடிக்கும், மேலும் ஒவ்வொரு ஆறு மாதங்களுக்கும் நீட்டிக்கப்பட்டு அதிகபட்சமாக மூன்று ஆண்டுகள் வரை செல்லலாம்.",
        "Option A (three months) is incorrect.", "விருப்பம் A (மூன்று மாதங்கள்) தவறானது.",
        "Option B is correct; six months is the statutory renewal period.", "விருப்பம் B சரியானது; ஆறு மாதங்கள் என்பது சட்டப்பூர்வ புதுப்பித்தல் காலமாகும்.",
        "Option C (one year) is the normal maximum threshold beyond which Article 356(5) conditions apply.", "விருப்பம் C (ஒரு வருடம்) சாதாரண அதிகபட்ச வரம்பாகும், அதற்கு மேல் சரத்து 356(5) நிபந்தனைகள் பொருந்தும்.",
        "Option D (two years) is incorrect.", "விருப்பம் D (இரண்டு ஆண்டுகள்) தவறானது.",
        "Universal 6-Month Renewal: Both Article 352 and Article 356 continue for 6 months at a time upon parliamentary approval.",
        "பொதுவான 6 மாத புதுப்பித்தல்: சரத்து 352 மற்றும் சரத்து 356 ஆகிய இரண்டும் பாராளுமன்ற ஒப்புதலுக்குப் பின் ஒரு நேரத்தில் 6 மாதங்கள் நீடிக்கும்.",
        "However, Article 352 has no maximum ceiling, while Article 356 has a strict 3-year constitutional ceiling.",
        "இருப்பினும் சரத்து 352-க்கு அதிகபட்ச வரம்பு இல்லை, ஆனால் சரத்து 356-க்கு 3 ஆண்டுகள் என்ற கடுமையான உச்சவரம்பு உண்டு."
    ))

    # 039 - Key C
    qs.append(make_ep_q(
        PREFIX, 39, DIFF, "PYQ MCQ", "Authority to Certify Election Impossibility",
        "Under Article 356(5), which constitutional authority must certify that general elections to the Legislative Assembly cannot be held in order to extend President's Rule beyond one year? [TNPSC Group 1 2019, UPSC 2015]",
        "சரத்து 356(5)-ன் கீழ், குடியரசுத் தலைவர் ஆட்சியை ஒரு வருடத்திற்கு மேல் நீட்டிப்பதற்கு, சட்டமன்றப் பொதுத் தேர்தலை நடத்த முடியாது என்று எந்த அரசியலமைப்பு அமைப்பு சான்றளிக்க வேண்டும்? [TNPSC குரூப் 1 2019, UPSC 2015]",
        "The Governor of the concerned State", "சம்பந்தப்பட்ட மாநில ஆளுநர்",
        "The Union Cabinet", "மத்திய அமைச்சரவை",
        "The Election Commission of India", "இந்திய தேர்தல் ஆணையம்",
        "The Supreme Court of India", "இந்திய உச்ச நீதிமன்றம்",
        "C",
        "Under Article 356(5)(b) (inserted by the 44th Amendment Act, 1978), extension beyond one year requires that the Election Commission certify that difficulties in holding general elections to the Legislative Assembly justify the continuance in force of the proclamation.",
        "1978-ன் 44-வது திருத்தச் சட்டத்தால் சேர்க்கப்பட்ட சரத்து 356(5)(b)-ன் படி, ஒரு வருடத்திற்கு மேல் நீட்டிக்க சட்டமன்றப் பொதுத் தேர்தலை நடத்துவதில் உள்ள சிரமங்கள் இத்தகைய நீட்டிப்பை நியாயப்படுத்துகின்றன என்று இந்திய தேர்தல் ஆணையம் சான்றளிக்க வேண்டும்.",
        "Option A (Governor) sends the initial report under Article 356(1), not the election certificate.", "விருப்பம் A (ஆளுநர்) ஆரம்ப அறிக்கையை அனுப்புகிறார், தேர்தல் சான்றிதழை அல்ல.",
        "Option B (Cabinet) advises the President.", "விருப்பம் B (அமைச்சரவை) குடியரசுத் தலைவருக்கு ஆலோசிக்கிறது.",
        "Option C is correct; Election Commission of India is the designated certifying authority.", "விருப்பம் C சரியானது; இந்திய தேர்தல் ஆணையமே இதற்கான அங்கீகரிக்கப்பட்ட அமைப்பாகும்.",
        "Option D (Supreme Court) exercises judicial review, not administrative election certification.", "விருப்பம் D (உச்ச நீதிமன்றம்) நீதித்துறை மறுஆய்வை மேற்கொள்கிறது, தேர்தல் சான்றளிப்பை அல்ல.",
        "Twin Conditions of Art 356(5): 1. National Emergency in operation; AND 2. Election Commission certificate.",
        "சரத்து 356(5)-ன் இரட்டை நிபந்தனைகள்: 1. தேசிய அவசரநிலை செயல்பாட்டில் இருக்க வேண்டும்; மற்றும் 2. தேர்தல் ஆணையத்தின் சான்றிதழ் தேவை.",
        "Both conditions must co-exist to permit extension beyond one year up to the maximum limit of three years.",
        "அதிகபட்ச வரம்பான மூன்று ஆண்டுகள் வரை ஒரு வருடத்திற்கு மேல் நீட்டிக்க இவ்விரண்டு நிபந்தனைகளும் ஒன்றாக இருக்க வேண்டும்."
    ))

    # 040 - Key D
    qs.append(make_ep_q(
        PREFIX, 40, DIFF, "PYQ MCQ", "Constitutional Term for Article 356",
        "Which phrase is explicitly used in the Constitution of India for the proclamation issued under Article 356? [TNPSC Group 1 2011, Group 2 2014]",
        "சரத்து 356-ன் கீழ் வெளியிடப்படும் பிரகடனத்திற்காக இந்திய அரசியலமைப்பில் வெளிப்படையாகப் பயன்படுத்தப்பட்டுள்ள சொற்றொடர் எது? [TNPSC குரூப் 1 2011, குரூப் 2 2014]",
        "State Emergency", "மாநில அவசரநிலை",
        "Constitutional Emergency", "அரசியலமைப்பு அவசரநிலை",
        "Governor's Rule", "ஆளுநர் ஆட்சி",
        "Proclamation on Failure of Constitutional Machinery in States", "மாநிலங்களில் அரசியலமைப்பு இயந்திர முறிவிற்கான பிரகடனம்",
        "D",
        "The Constitution of India does NOT use the word 'Emergency' in Article 356. The marginal heading of Article 356 reads: 'Provisions in case of failure of constitutional machinery in States'. Popular terms like 'President's Rule', 'State Emergency', or 'Constitutional Emergency' are descriptive conventions.",
        "சரத்து 356-ல் இந்திய அரசியலமைப்பு 'அவசரநிலை' (Emergency) என்ற சொல்லைப் பயன்படுத்தவில்லை. சரத்து 356-ன் தலைப்பு: 'மாநிலங்களில் அரசியலமைப்பு இயந்திரம் தோல்வியடையும் போது உள்ள விதிகள்' என்று குறிப்பிடுகிறது. 'குடியரசுத் தலைவர் ஆட்சி', 'மாநில அவசரநிலை' போன்ற சொற்கள் நடைமுறை வழக்கமான சொற்களாகும்.",
        "Option A (State Emergency) is a popular political term, not constitutional text.", "விருப்பம் A (மாநில அவசரநிலை) நடைமுறைச் சொல்லே தவிர அரசியலமைப்பு வாசகம் அல்ல.",
        "Option B (Constitutional Emergency) is a descriptive label.", "விருப்பம் B ஒரு விளக்கக் குறியீடாகும்.",
        "Option C (Governor's Rule) applied formerly in Jammu & Kashmir under its separate constitution.", "விருப்பம் C முன்பு ஜம்மு-காஷ்மீருக்கு அதன் தனி அரசியலமைப்பின் கீழ் பொருந்தியது.",
        "Option D is correct; 'failure of constitutional machinery' is the precise constitutional terminology.", "விருப்பம் D சரியானது; 'அரசியலமைப்பு இயந்திர முறிவு' என்பதே துல்லியமான அரசியலமைப்புச் சொல்லாகும்.",
        "High-Yield Nuance: Article 352 uses 'Proclamation of Emergency'; Article 360 uses 'Financial Emergency'; Article 356 avoids the word 'Emergency' entirely!",
        "உயர்-விளைச்சல் நுணுக்கம்: சரத்து 352 'அவசரநிலைப் பிரகடனம்' என்றும்; சரத்து 360 'நிதி அவசரநிலை' என்றும் குறிப்பிடுகிறது; ஆனால் சரத்து 356 'அவசரநிலை' என்ற சொல்லையே முற்றிலும் தவிர்க்கிறது!",
        "Dr. Ambedkar specifically framed it as a mechanism for failure of machinery rather than an overarching emergency power.",
        "டாக்டர் அம்பேத்கர் இதனை ஒரு பொதுவான அவசரநிலை அதிகாரமாக இல்லாமல் இயந்திர முறிவுக்கான வழிமுறையாகவே வடிவமைத்தார்."
    ))

    return qs

def get_pyq_questions_batch5():
    qs = []

    # 041 - Key A
    qs.append(make_ep_q(
        PREFIX, 41, DIFF, "PYQ MCQ", "Article 353 Executive Directions",
        "Under Article 353(a), during the operation of a National Emergency, the executive power of the Union extends to: [TNPSC Group 1 2017, UPSC 2016]",
        "சரத்து 353(a)-ன் கீழ், தேசிய அவசரநிலை செயல்பாட்டில் இருக்கும் போது, மத்திய அரசின் நிர்வாக அதிகாரம் எதற்கு விரிவடைகிறது? [TNPSC குரூப் 1 2017, UPSC 2016]",
        "Giving directions to any State as to the manner in which its executive power is to be exercised", "எந்தவொரு மாநிலமும் தனது நிர்வாக அதிகாரத்தை எவ்வாறு செயல்படுத்த வேண்டும் என்பது குறித்த வழிகாட்டுதல்களை வழங்குவதற்கு",
        "Dismissing the Governor of the State immediately", "மாநில ஆளுநரை உடனடியாகப் பதவி நீக்கம் செய்வதற்கு",
        "Suspending all local bodies and panchayats in the State", "மாநிலத்தில் உள்ள அனைத்து உள்ளாட்சி அமைப்புகளையும் பஞ்சாயத்துகளையும் இடைநிறுத்துவதற்கு",
        "Dissolving the State High Court and transferring judges", "மாநில உயர்நீதிமன்றத்தைக் கலைத்து நீதிபதிகளை இடமாற்றம் செய்வதற்கு",
        "A",
        "Under Article 353(a), during a National Emergency, the executive power of the Union extends to the giving of directions to any State as to the manner in which the executive power thereof is to be exercised.",
        "சரத்து 353(a)-ன் கீழ், தேசிய அவசரநிலையின் போது, எந்தவொரு மாநிலமும் தனது நிர்வாக அதிகாரத்தை எவ்வாறு செயல்படுத்த வேண்டும் என்பது குறித்து வழிகாட்டுதல்களை வழங்க மத்திய அரசின் நிர்வாக அதிகாரம் விரிவடைகிறது.",
        "Option A is correct; it verbatim quotes Article 353(a).", "விருப்பம் A சரியானது; இது சரத்து 353(a)-ன் நேரடி வாசகமாகும்.",
        "Option B is wrong because Governor serves at the pleasure of President normally; emergency does not alter that.", "விருப்பம் B தவறு, ஏனெனில் ஆளுநர் எப்போதும் குடியரசுத் தலைவரின் விருப்பப்படி பதவியில் நீடிக்கிறார்.",
        "Option C is wrong because local bodies are not automatically suspended.", "விருப்பம் C தவறு, ஏனெனில் உள்ளாட்சி அமைப்புகள் தானாக இடைநிறுத்தப்படுவதில்லை.",
        "Option D is wrong because judicial institutions are independent.", "விருப்பம் D தவறு, ஏனெனில் நீதித்துறை அமைப்புகள் சுதந்திரமானவை.",
        "Core Shift: In normal times, Centre gives directions to states only on specific subjects under Articles 256 and 257. In emergency, directions can cover ANY topic.",
        "முக்கிய மாற்றம்: சாதாரண காலங்களில், சரத்துகள் 256 மற்றும் 257-ன் கீழ் குறிப்பிட்ட சில தலைப்புகளில் மட்டுமே வழிகாட்ட முடியும். ஆனால் அவசரநிலையின் போது எந்தவொரு தலைப்பிலும் வழிகாட்டலாம்.",
        "The state government is brought under the complete control of the Centre, though it is not suspended.",
        "மாநில அரசு இடைநிறுத்தப்படாவிட்டாலும், அது மத்திய அரசின் முழுக் கட்டுப்பாட்டின் கீழ் கொண்டுவரப்படுகிறது."
    ))

    # 042 - Key B
    qs.append(make_ep_q(
        PREFIX, 42, DIFF, "PYQ MCQ", "Article 250 Legislative Powers",
        "Under Article 250 of the Constitution of India, during a National Emergency, Parliament has the power to make laws with respect to: [TNPSC Group 2 2015, Group 1 2014]",
        "இந்திய அரசியலமைப்பின் சரத்து 250-ன் கீழ், தேசிய அவசரநிலையின் போது, பாராளுமன்றத்திற்கு எதன் மீது சட்டங்களை இயற்ற அதிகாரம் உண்டு? [TNPSC குரூப் 2 2015, குரூப் 1 2014]",
        "Union List subjects only", "மத்தியப் பட்டியல் விவகாரங்கள் மீது மட்டுமே",
        "Any matter in the State List for the whole or any part of the territory of India", "இந்தியாவின் முழு பகுதிக்கும் அல்லது ஏதேனும் ஒரு பகுதிக்கும் மாநிலப் பட்டியலில் உள்ள எந்தவொரு விவகாரத்தின் மீதும்",
        "Residuary subjects only", "எஞ்சிய அதிகாரங்கள் மீது மட்டுமே",
        "International treaties and agreements only", "சர்வதேச ஒப்பந்தங்கள் மீது மட்டுமே",
        "B",
        "Under Article 250(1), while a Proclamation of Emergency is in operation, Parliament has the power to make laws for the whole or any part of the territory of India with respect to any of the matters enumerated in the State List.",
        "சரத்து 250(1)-ன் கீழ், அவசரநிலைப் பிரகடனம் செயல்பாட்டில் இருக்கும் போது, மாநிலப் பட்டியலில் குறிப்பிடப்பட்டுள்ள எந்தவொரு விவகாரத்தின் மீதும் இந்தியா முழுமைக்கோ அல்லது அதன் ஏதேனும் ஒரு பகுதிக்கோ சட்டங்களை இயற்ற பாராளுமன்றத்திற்கு அதிகாரம் உண்டு.",
        "Option A is too narrow; Parliament already has power over the Union List under normal times (Article 246).", "விருப்பம் A மிகவும் குறுகியது; சாதாரண காலங்களிலேயே மத்தியப் பட்டியலில் பாராளுமன்றத்திற்கு அதிகாரம் உண்டு.",
        "Option B is correct; Article 250 extends parliamentary competence to the State List.", "விருப்பம் B சரியானது; சரத்து 250 பாராளுமன்றத்தின் அதிகாரத்தை மாநிலப் பட்டியலுக்கும் விரிவுபடுத்துகிறது.",
        "Option C refers to Article 248.", "விருப்பம் C சரத்து 248-ஐக் குறிக்கிறது.",
        "Option D refers to Article 253.", "விருப்பம் D சரத்து 253-ஐக் குறிக்கிறது.",
        "Six-Month Rule: Under Article 250(2), laws made by Parliament on State subjects cease to have effect 6 months after the emergency ceases to operate.",
        "ஆறு மாத விதி: சரத்து 250(2)-ன் கீழ், மாநில விவகாரங்களில் பாராளுமன்றம் இயற்றிய சட்டங்கள் அவசரநிலை முடிவுக்கு வந்து 6 மாதங்களுக்குப் பிறகு செயலிழந்துவிடும்.",
        "During this period, the State Legislature also retains power to make laws on the State List, but in case of conflict, parliamentary law prevails.",
        "இக்காலகட்டத்தில் மாநில சட்டமன்றமும் சட்டம் இயற்றலாம், ஆனால் முரண்பாடு ஏற்பட்டால் பாராளுமன்றச் சட்டமே மேலோங்கும்."
    ))

    # 043 - Key C
    qs.append(make_ep_q(
        PREFIX, 43, DIFF, "PYQ MCQ", "Article 358 Geographically Automatic",
        "Which of the following is an accurate feature of Article 358 during an external National Emergency? [TNPSC Group 1 2019, UPSC 2017]",
        "வெளிப்புற தேசிய அவசரநிலையின் போது சரத்து 358-ன் துல்லியமான அம்சம் பின்வருவனவற்றில் எது? [TNPSC குரூப் 1 2019, UPSC 2017]",
        "It requires a specific Presidential Order specifying which freedoms of Article 19 are suspended", "சரத்து 19-ன் எந்தெந்த சுதந்திரங்கள் இடைநிறுத்தப்படுகின்றன என்பதைக் குறிப்பிடும் தனிப்பட்ட குடியரசுத் தலைவர் ஆணை இதற்குத் தேவைப்படுகிறது",
        "It can be challenged in the Supreme Court on grounds of violating Article 14", "சரத்து 14-ஐ மீறியதாக உச்ச நீதிமன்றத்தில் இதனை சவாலுக்கு உட்படுத்தலாம்",
        "It automatically suspends Article 19 for the entire country without requiring any separate presidential order", "எந்தவொரு தனி குடியரசுத் தலைவர் ஆணையும் தேவையின்றி நாடு முழுவதும் தானாகவே சரத்து 19-ஐ இடைநிறுத்துகிறது",
        "It applies only to the border states directly adjoining the war zone", "போர் மண்டலத்தை ஒட்டியுள்ள எல்லை மாநிலங்களுக்கு மட்டுமே இது பொருந்தும்",
        "C",
        "Article 358 is self-executing and automatically suspends the six freedoms under Article 19 for the entire territory of India without requiring any special notification or presidential order, as long as the emergency is on grounds of war or external aggression.",
        "போர் அல்லது வெளிநாட்டு ஆக்கிரமிப்பு அடிப்படையில் அவசரநிலை இருக்கும் வரை, சரத்து 358 என்பது தானாகவே செயல்படுத்தக்கூடியது மற்றும் எந்தவொரு சிறப்பு அறிவிப்போ அல்லது குடியரசுத் தலைவர் ஆணையோ இன்றி நாடு முழுவதும் சரத்து 19-ன் ஆறு சுதந்திரங்களையும் தானாகவே இடைநிறுத்துகிறது.",
        "Option A is wrong because Article 358 requires no presidential order (unlike Article 359).", "விருப்பம் A தவறு, ஏனெனில் சரத்து 358-க்கு குடியரசுத் தலைவர் ஆணை தேவையில்லை (சரத்து 359 போல அல்ல).",
        "Option B is wrong because Article 358 suspends Article 19, not Article 14.", "விருப்பம் B தவறு, ஏனெனில் சரத்து 358 சரத்து 19-ஐ இடைநிறுத்துகிறது, 14-ஐ அல்ல.",
        "Option C is correct; Article 358 is automatic and nationwide.", "விருப்பம் C சரியானது; சரத்து 358 தானியங்கு மற்றும் நாடு தழுவியதாகும்.",
        "Option D is wrong because it applies to the entire territory of India.", "விருப்பம் D தவறு, ஏனெனில் இது இந்தியா முழுவதும் பொருந்தும்.",
        "High-Yield Contrast: Article 358 = Automatic + Article 19 only + Entire nation; Article 359 = Non-automatic + Specified rights + Can be localized.",
        "உயர்-விளைச்சல் ஒப்பீடு: சரத்து 358 = தானியங்கு + சரத்து 19 மட்டுமே + நாடு முழுவதும்; சரத்து 359 = தானியங்காதது + குறிப்பிட்ட உரிமைகள் + பகுதிவாரியாக இருக்கலாம்.",
        "Laws passed must contain a recital that they are in relation to the emergency to claim immunity.",
        "பாதுகாப்பைப் பெற சட்டங்கள் அவசரநிலையுடன் தொடர்புடையவை என்ற குறிப்பைக் கொண்டிருக்க வேண்டும்."
    ))

    # 044 - Key D
    qs.append(make_ep_q(
        PREFIX, 44, DIFF, "PYQ MCQ", "1971 National Emergency Context",
        "The second National Emergency proclaimed in India on December 3, 1971 was triggered by: [TNPSC Group 2 2012, Group 4 2016]",
        "டிசம்பர் 3, 1971 அன்று இந்தியாவில் பிரகடனப்படுத்தப்பட்ட இரண்டாவது தேசிய அவசரநிலை எதனால் தூண்டப்பட்டது? [TNPSC குரூப் 2 2012, குரூப் 4 2016]",
        "Armed rebellion in northeastern states", "வடகிழக்கு மாநிலங்களில் ஆயுதமேந்திய கிளர்ச்சி",
        "Internal disturbance and civil disobedience", "உள்நாட்டு அமைதியின்மை மற்றும் சட்டமறுப்பு இயக்கம்",
        "Chinese border aggression across Ladakh", "லடாக் பகுதியில் சீன எல்லை ஆக்கிரமிப்பு",
        "External aggression by Pakistan (Indo-Pakistani War of 1971)", "பாகிஸ்தானின் வெளிநாட்டு ஆக்கிரமிப்பு (1971 இந்திய-பாகிஸ்தான் போர்)",
        "D",
        "The second National Emergency was proclaimed on December 3, 1971 by President V.V. Giri following Pakistani air strikes and aggression, leading to the Indo-Pakistani War and the liberation of Bangladesh.",
        "பாகிஸ்தானின் வான்வழித் தாக்குதல்கள் மற்றும் ஆக்கிரமிப்பைத் தொடர்ந்து, 1971 டிசம்பர் 3 அன்று குடியரசுத் தலைவர் வி.வி. கிரியால் இரண்டாவது தேசிய அவசரநிலை அறிவிக்கப்பட்டது; இது இந்திய-பாகிஸ்தான் போருக்கும் வங்கதேச விடுதலைக்கும் வழிவகுத்தது.",
        "Option A is incorrect.", "விருப்பம் A தவறானது.",
        "Option B describes the 1975 emergency.", "விருப்பம் B 1975 அவசரநிலையை விவரிக்கிறது.",
        "Option C describes the 1962 emergency.", "விருப்பம் C 1962 அவசரநிலையை விவரிக்கிறது.",
        "Option D is correct; Pakistani aggression in December 1971 prompted the 2nd emergency.", "விருப்பம் D சரியானது; டிசம்பர் 1971-ல் பாகிஸ்தான் ஆக்கிரமிப்பே 2-வது அவசரநிலைக்குக் காரணமாக அமைந்தது.",
        "Historical Continuity: The 1971 external emergency was NOT revoked after the war ended; it continued until March 1977, coexisting with the 1975 internal emergency!",
        "வரலாற்றுத் தொடர்ச்சி: 1971 வெளிப்புற அவசரநிலை போர் முடிந்தவுடன் திரும்பப் பெறப்படவில்லை; அது மார்ச் 1977 வரை நீடித்து, 1975 உள்நாட்டு அவசரநிலையுடன் இணைந்து செயல்பட்டது!",
        "Both the 2nd and 3rd emergencies were revoked simultaneously on March 21, 1977.",
        "2-வது மற்றும் 3-வது அவசரநிலைகள் இரண்டும் மார்ச் 21, 1977 அன்று ஒரே நேரத்தில் ரத்து செய்யப்பட்டன."
    ))

    # 045 - Key A
    qs.append(make_ep_q(
        PREFIX, 45, DIFF, "PYQ MCQ", "Constituent Assembly Critic of Emergency",
        "Which prominent member of the Constituent Assembly famously warned that the Emergency Provisions were 'a chapter of reactions and retrogression' laying the foundation for a totalitarian state? [TNPSC Group 1 2017, 2019]",
        "அவசரநிலைப் பிரிவுகள் என்பது 'பிற்போக்குத்தனமான மற்றும் ஜனநாயக விரோத அத்தியாயம்' என்றும், அவை ஒரு சர்வாதிகார அரசுக்கான அடித்தளத்தை அமைக்கும் என்றும் அரசியலமைப்பு நிர்ணய சபையில் எச்சரித்த பிரபல உறுப்பினர் யார்? [TNPSC குரூப் 1 2017, 2019]",
        "H.V. Kamath", "எச்.வி. காமத்",
        "Alladi Krishnaswamy Iyer", "அல்லாடி கிருஷ்ணசுவாமி அய்யர்",
        "K.M. Munshi", "கே.எம். முன்ஷி",
        "Dr. B.R. Ambedkar", "டாக்டர் பி.ஆர். அம்பேத்கர்",
        "A",
        "H.V. Kamath vehemently opposed emergency powers in the Constituent Assembly, declaring: 'I fear that by this single chapter we are seeking to lay the foundation of a totalitarian state, a Police State... a chapter of reactions and retrogression.'",
        "அரசியலமைப்பு நிர்ணய சபையில் அவசரநிலை அதிகாரங்களை கடுமையாக எதிர்த்த எச்.வி. காமத்: 'இந்த ஒற்றை அத்தியாயத்தின் மூலம் நாம் ஒரு சர்வாதிகார அரசுக்கான, ஒரு காவல் அரசுக்கான அடித்தளத்தை அமைக்க முயல்கிறோம்... இது பிற்போக்குத்தனமான ஒரு அத்தியாயம்' என்று எச்சரித்தார்.",
        "Option A is correct; H.V. Kamath made this celebrated speech.", "விருப்பம் A சரியானது; எச்.வி. காமத் இந்த புகழ்பெற்ற உரையை ஆற்றினார்.",
        "Option B supported emergency powers as the 'very life of the Constitution'.", "விருப்பம் B அவசரநிலை அதிகாரங்களை 'அரசியலமைப்பின் உயிர்நாடி' என ஆதரித்தார்.",
        "Option C supported the emergency provisions as necessary safeguards.", "விருப்பம் C அவசரநிலைப் பிரிவுகளை அவசியமான பாதுகாப்பு என ஆதரித்தார்.",
        "Option D defended Article 356 hoping it would remain a dead letter.", "விருப்பம் D சரத்து 356 ஒரு பயன்படுத்தப்படாத விதியாக இருக்கும் என்று நம்பி அதனை ஆதரித்தார்.",
        "Assembly Debates: H.N. Kunzru, Shibban Lal Saksena, and K.T. Shah also sharply criticized emergency provisions as dangerous to civil liberty.",
        "நிர்ணய சபை விவாதங்கள்: எச்.என். குன்ஸ்ரு, சிபன் லால் சக்சேனா மற்றும் கே.டி. ஷா ஆகியோரும் அவசரநிலைப் பிரிவுகளைக் கடுமையாக விமர்சித்தனர்.",
        "Prof. K.T. Shah called it a 'monstrous power' that destroyed provincial autonomy.", "பேராசிரியர் கே.டி. ஷா இது மாகாண சுயாட்சியை அழிக்கும் ஒரு 'அசுரத்தனமான அதிகாரம்' என்று அழைத்தார்."
    ))

    # 046 - Key B
    qs.append(make_ep_q(
        PREFIX, 46, DIFF, "PYQ MCQ", "Cabinet Word Occurrence in Constitution",
        "The word 'Cabinet' appears in which Article of the Constitution of India? [TNPSC Group 1 2015, Group 2 2017, UPSC 2016]",
        "'அமைச்சரவை' (Cabinet) என்ற சொல் இந்திய அரசியலமைப்பின் எந்த சரத்தில் இடம்பெற்றுள்ளது? [TNPSC குரூப் 1 2015, குரூப் 2 2017, UPSC 2016]",
        "Article 74", "சரத்து 74",
        "Article 352", "சரத்து 352",
        "Article 75", "சரத்து 75",
        "Article 78", "சரத்து 78",
        "B",
        "The word 'Cabinet' appears ONLY ONCE in the entire text of the Constitution of India, under Article 352(3), inserted by the 44th Constitutional Amendment Act 1978. Everywhere else (including Articles 74 and 75), the Constitution uses the phrase 'Council of Ministers'.",
        "'அமைச்சரவை' (Cabinet) என்ற சொல் இந்திய அரசியலமைப்பு முழுவதிலும் ஒரே ஒரு முறை மட்டுமே, 1978-ன் 44-வது திருத்தச் சட்டத்தால் சேர்க்கப்பட்ட சரத்து 352(3)-ன் கீழ் இடம்பெற்றுள்ளது. மற்ற அனைத்து இடங்களிலும் (சரத்துகள் 74 மற்றும் 75 உட்பட) அரசியலமைப்பு 'அமைச்சர்கள் குழு' (Council of Ministers) என்ற சொற்றொடரையே பயன்படுத்துகிறது.",
        "Option A (Article 74) uses 'Council of Ministers to aid and advise President'.", "விருப்பம் A (சரத்து 74) 'குடியரசுத் தலைவருக்கு உதவ அமைச்சர்கள் குழு' என்ற சொல்லைப் பயன்படுத்துகிறது.",
        "Option B is correct; Article 352 is the exclusive home of the word 'Cabinet'.", "விருப்பம் B சரியானது; சரத்து 352 மட்டுமே 'கேபினட்' என்ற சொல்லைக் கொண்டுள்ளது.",
        "Option C (Article 75) uses 'other provisions as to Ministers'.", "விருப்பம் C (சரத்து 75) அமைச்சர்கள் பற்றிய இதர விதிகளைக் கையாள்கிறது.",
        "Option D (Article 78) deals with duties of Prime Minister.", "விருப்பம் D (சரத்து 78) பிரதமரின் கடமைகள் தொடர்பானது.",
        "High-Yield TNPSC Fact: 'Cabinet' is defined in Article 352(3) as the Council consisting of the Prime Minister and other Ministers of Cabinet rank appointed under Article 75.",
        "உயர்-விளைச்சல் TNPSC உண்மை: சரத்து 75-ன் கீழ் நியமிக்கப்பட்ட பிரதமர் மற்றும் கேபினட் அந்தஸ்துள்ள அமைச்சர்களைக் கொண்ட குழுவே 'கேபினட்' என சரத்து 352(3)-ல் வரையறுக்கப்பட்டுள்ளது.",
        "This definition was added precisely so that an emergency could not be declared without the collective written agreement of the senior-most ministers.",
        "மூத்த அமைச்சர்களின் கூட்டு எழுத்துப்பூர்வ உடன்பாடின்றி அவசரநிலை அறிவிக்கப்படுவதைத் தடுக்கவே இந்த வரையறை சேர்க்கப்பட்டது."
    ))

    # 047 - Key C
    qs.append(make_ep_q(
        PREFIX, 47, DIFF, "PYQ MCQ", "Effect on State High Courts Jurisdiction",
        "During the operation of a National Emergency under Article 352, does the writ jurisdiction of the State High Courts under Article 226 get automatically abolished? [TNPSC Group 1 2017, Group 2 2019]",
        "சரத்து 352-ன் கீழான தேசிய அவசரநிலை செயல்பாட்டில் இருக்கும் போது, சரத்து 226-ன் கீழான மாநில உயர்நீதிமன்றங்களின் நீதிப்பேராணை அதிகாரம் தானாகவே ரத்து செய்யப்படுகிறதா? [TNPSC குரூப் 1 2017, குரூப் 2 2019]",
        "Yes, all High Court powers are abolished automatically", "ஆம், அனைத்து உயர்நீதிமன்ற அதிகாரங்களும் தானாகவே ரத்து செய்யப்படுகின்றன",
        "Yes, High Courts cannot hear any matters during emergency", "ஆம், அவசரநிலையின் போது உயர்நீதிமன்றங்கள் எந்த விவகாரத்தையும் விசாரிக்க முடியாது",
        "No, High Courts continue to function and can issue writs for non-suspended rights and legal rights", "இல்லை, உயர்நீதிமன்றங்கள் தொடர்ந்து செயல்படுகின்றன மற்றும் இடைநிறுத்தப்படாத உரிமைகள் மற்றும் சட்ட உரிமைகளுக்காக நீதிப்பேராணைகளை வெளியிட முடியும்",
        "Yes, but only in states bordering foreign countries", "ஆம், ஆனால் வெளிநாட்டு எல்லையை ஒட்டியுள்ள மாநிலங்களில் மட்டுமே",
        "C",
        "Article 226 writ jurisdiction is NOT abolished during emergency. Citizens can continue to approach High Courts to enforce rights not covered by a Presidential Order under Article 359, as well as non-fundamental statutory and legal rights, and to challenge actions not protected by valid emergency legislation.",
        "அவசரநிலையின் போது சரத்து 226 நீதிப்பேராணை அதிகாரம் ரத்து செய்யப்படுவதில்லை. சரத்து 359-ன் கீழான குடியரசுத் தலைவர் ஆணையில் சேர்க்கப்படாத உரிமைகள், மற்றும் சட்டப்பூர்வ உரிமைகளை நிலைநாட்டவும், சட்டவிரோத நடவடிக்கைகளை சவாலுக்கு உட்படுத்தவும் குடிமக்கள் உயர்நீதிமன்றங்களைத் தொடர்ந்து அணுக முடியும்.",
        "Option A is incorrect because judicial power is never extinguished.", "விருப்பம் A தவறு, ஏனெனில் நீதித்துறை அதிகாரம் ஒருபோதும் அழிக்கப்படுவதில்லை.",
        "Option B is wrong because courts function continuously.", "விருப்பம் B தவறு, ஏனெனில் நீதிமன்றங்கள் தொடர்ந்து செயல்படுகின்றன.",
        "Option C is correct; High Courts continue to exercise judicial powers within constitutional limits.", "விருப்பம் C சரியானது; உயர்நீதிமன்றங்கள் தங்களின் அதிகார வரம்பிற்குள் தொடர்ந்து செயல்படுகின்றன.",
        "Option D is baseless.", "விருப்பம் D ஆதாரமற்றது.",
        "Post-Puttaswamy Rule: Arbitrary executive actions violating Article 21 can ALWAYS be challenged under Article 226, even during emergency.",
        "புட்டசுவாமிக்குப் பிந்தைய விதி: அவசரநிலையின் போது கூட சரத்து 21-ஐ மீறும் தன்னிச்சையான நிர்வாக நடவடிக்கைகளை சரத்து 226-ன் கீழ் எப்போதும் எதிர்க்க முடியும்.",
        "Articles 20 and 21 remain fully enforceable through Article 226 and Article 32.",
        "சரத்துகள் 20 மற்றும் 21 சரத்து 226 மற்றும் சரத்து 32 மூலம் முழுமையாக அமல்படுத்தக்கூடியவையாக உள்ளன."
    ))

    # 048 - Key D
    qs.append(make_ep_q(
        PREFIX, 48, DIFF, "PYQ MCQ", "Article 356 Upper Limit Exceptions",
        "In which State was President's Rule extended up to nearly 5 years (1987 to 1992) by passing special constitutional amendments (59th, 64th, 67th, and 68th CAAs)? [TNPSC Group 1 2015, Group 2 2018]",
        "சிறப்பு அரசியலமைப்பு திருத்தங்களை (59, 64, 67 மற்றும் 68-வது திருத்தங்கள்) நிறைவேற்றுவதன் மூலம் எந்த மாநிலத்தில் குடியரசுத் தலைவர் ஆட்சி ஏறக்குறைய 5 ஆண்டுகள் (1987 முதல் 1992 வரை) நீட்டிக்கப்பட்டது? [TNPSC குரூப் 1 2015, குரூப் 2 2018]",
        "Jammu and Kashmir", "ஜம்மு மற்றும் காஷ்மீர்",
        "Assam", "அசாம்",
        "Nagaland", "நாகாலாந்து",
        "Punjab", "பஞ்சாப்",
        "D",
        "President's Rule was imposed in Punjab on May 11, 1987, and continued till February 25, 1992. Because the constitutional maximum under Article 356 is three years, Parliament enacted the 59th, 64th, 67th, and 68th Constitutional Amendment Acts specifically to extend President's Rule in Punjab up to nearly five years due to terrorism.",
        "பஞ்சாபில் மே 11, 1987 அன்று விதிக்கப்பட்ட குடியரசுத் தலைவர் ஆட்சி பிப்ரவரி 25, 1992 வரை நீடித்தது. சரத்து 356-ன் கீழ் அரசியலமைப்பு அதிகபட்ச வரம்பு 3 ஆண்டுகள் என்பதால், பயங்கரவாத அச்சுறுத்தல் காரணமாக பஞ்சாபில் குடியரசுத் தலைவர் ஆட்சியை 5 ஆண்டுகள் வரை நீட்டிக்க 59, 64, 67 மற்றும் 68-வது அரசியலமைப்பு திருத்தச் சட்டங்களை பாராளுமன்றம் இயற்றியது.",
        "Option A (J&K) operated under separate state constitutional provisions.", "விருப்பம் A (ஜம்மு-காஷ்மீர்) அதன் தனி மாநில அரசியலமைப்பு விதிகளின் கீழ் செயல்பட்டது.",
        "Option B (Assam) had emergency during the Assam agitation but not continuous 5-year CAA extensions.", "விருப்பம் B (அசாம்) தொடர்ச்சியான 5 ஆண்டு திருத்த நீட்டிப்புகளைக் கொண்டிருக்கவில்லை.",
        "Option C (Nagaland) is incorrect.", "விருப்பம் C (நாகாலாந்து) தவறானது.",
        "Option D is correct; Punjab required four successive constitutional amendments to extend beyond 3 years.", "விருப்பம் D சரியானது; 3 ஆண்டுகளுக்கு மேல் நீட்டிக்க பஞ்சாபிற்கு நான்கு அடுத்தடுத்த அரசியலமைப்பு திருத்தங்கள் தேவைப்பட்டன.",
        "Constitutional Doctrine: The 3-year maximum limit of Article 356 is absolute; it CANNOT be breached without a formal Constitutional Amendment under Article 368!",
        "அரசியலமைப்பு கோட்பாடு: சரத்து 356-ன் 3 ஆண்டு அதிகபட்ச வரம்பு முழுமையானது; சரத்து 368-ன் கீழான முறையான அரசியலமைப்பு திருத்தமின்றி அதனை மீற முடியாது!",
        "Normal elections were finally held in Punjab in February 1992, restoring popular government.",
        "இறுதியாக பிப்ரவரி 1992-ல் பஞ்சாபில் இயல்பான தேர்தல்கள் நடத்தப்பட்டு மக்களாட்சி மீண்டும் நிலைநாட்டப்பட்டது."
    ))

    # 049 - Key A
    qs.append(make_ep_q(
        PREFIX, 49, DIFF, "PYQ MCQ", "Article 360 Simple Majority Rule",
        "What type of majority in Parliament is required to approve a proclamation of Financial Emergency under Article 360? [TNPSC Group 2 2015, Group 4 2018]",
        "சரத்து 360-ன் கீழான நிதி அவசரநிலைப் பிரகடனத்திற்கு ஒப்புதல் அளிக்க பாராளுமன்றத்தில் எந்த வகையான பெரும்பான்மை தேவைப்படுகிறது? [TNPSC குரூப் 2 2015, குரூப் 4 2018]",
        "Two-thirds majority of the total membership of each House", "ஒவ்வொரு அவையின் மொத்த உறுப்பினர்களில் மூன்றில் இரண்டு பங்கு பெரும்பான்மை",
        "Special majority of total membership and 2/3 present and voting", "மொத்த உறுப்பினர்களில் பெரும்பான்மை மற்றும் வருகை தந்து வாக்களிப்போரில் 2/3 பங்கு சிறப்புப் பெரும்பான்மை",
        "Simple majority of members present and voting in each House", "ஒவ்வொரு அவையிலும் வருகை தந்து வாக்களிக்கும் உறுப்பினர்களில் எளிய பெரும்பான்மை",
        "Absolute majority of the Lok Sabha alone", "மக்களவையின் முழுமையான பெரும்பான்மை மட்டுமே",
        "C",
        "Under Article 360(2), a resolution approving Financial Emergency can be passed by either House of Parliament only by a simple majority, that is, a majority of the members of that House present and voting.",
        "சரத்து 360(2)-ன் கீழ், நிதி அவசரநிலைக்கு ஒப்புதல் அளிக்கும் தீர்மானத்தை பாராளுமன்றத்தின் இரு அவைகளும் எளிய பெரும்பான்மையால் (வருகை தந்து வாக்களிக்கும் உறுப்பினர்களில் பெரும்பான்மை) மட்டுமே நிறைவேற்ற முடியும்.",
        "Option A applies to presidential impeachment under Article 61.", "விருப்பம் A சரத்து 61-ன் கீழ் குடியரசுத் தலைவர் பதவி நீக்கத்திற்குப் பொருந்தும்.",
        "Option B (special majority) is required strictly for Article 352 National Emergency only.", "விருப்பம் B (சிறப்புப் பெரும்பான்மை) சரத்து 352 தேசிய அவசரநிலைக்கு மட்டுமே தேவைப்படுகிறது.",
        "Option C is correct; simple majority governs Article 360 approval.", "விருப்பம் C சரியானது; எளிய பெரும்பான்மையே சரத்து 360-ன் ஒப்புதலை நிர்வகிக்கிறது.",
        "Option D is wrong because Rajya Sabha has co-equal approval power under Article 360.", "விருப்பம் D தவறு, ஏனெனில் சரத்து 360-ல் மாநிலங்களவைக்கும் சமமான ஒப்புதல் அதிகாரம் உண்டு.",
        "Approval Summary: Article 352 = Special Majority; Article 356 = Simple Majority; Article 360 = Simple Majority.",
        "ஒப்புதல் சுருக்கம்: சரத்து 352 = சிறப்புப் பெரும்பான்மை; சரத்து 356 = எளிய பெரும்பான்மை; சரத்து 360 = எளிய பெரும்பான்மை.",
        "Both Houses of Parliament must approve it within two months.",
        "பாராளுமன்றத்தின் இரு அவைகளும் இரண்டு மாதங்களுக்குள் இதற்கு ஒப்புதல் அளிக்க வேண்டும்."
    ))

    # 050 - Key B
    qs.append(make_ep_q(
        PREFIX, 50, DIFF, "PYQ MCQ", "Article 360 Duration Nuance",
        "Once approved by both Houses of Parliament, for how long does a Financial Emergency under Article 360 remain in operation? [TNPSC Group 1 2017, Group 2 2019, UPSC 2016]",
        "பாராளுமன்றத்தின் இரு அவைகளாலும் அங்கீகரிக்கப்பட்டவுடன், சரத்து 360-ன் கீழான நிதி அவசரநிலை எவ்வளவு காலம் தொடர்ந்து செயல்பாட்டில் இருக்கும்? [TNPSC குரூப் 1 2017, குரூப் 2 2019, UPSC 2016]",
        "For a maximum period of six months unless renewed", "புதுப்பிக்கப்படாவிட்டால் அதிகபட்சமாக ஆறு மாத காலம்",
        "Indefinitely until it is revoked by the President", "குடியரசுத் தலைவரால் ரத்து செய்யப்படும் வரை காலவரையின்றி",
        "For a maximum period of three years", "அதிகபட்சமாக மூன்று ஆண்டுகள்",
        "For a period of one year, extendable up to three years", "ஒரு வருட காலம், மூன்று ஆண்டுகள் வரை நீட்டிக்கத்தக்கது",
        "B",
        "Once approved by both Houses of Parliament, a Financial Emergency continues INDEFINITELY until it is revoked by the President. There is NO maximum period prescribed for its operation, and repeated parliamentary approval is NOT required for its continuation.",
        "பாராளுமன்றத்தின் இரு அவைகளாலும் ஒப்புதல் அளிக்கப்பட்டவுடன், குடியரசுத் தலைவரால் ரத்து செய்யப்படும் வரை நிதி அவசரநிலை காலவரையின்றித் தொடர்கிறது. அதன் செயல்பாட்டிற்கு எந்தவொரு அதிகபட்ச கால வரம்பும் நிர்ணயிக்கப்படவில்லை, மேலும் அது தொடர்வதற்கு மீண்டும் மீண்டும் பாராளுமன்ற ஒப்புதல் தேவையில்லை.",
        "Option A describes Article 352 and 356, which require 6-month renewal.", "விருப்பம் A 6 மாத புதுப்பித்தல் தேவைப்படும் சரத்துகள் 352 மற்றும் 356-ஐ விவரிக்கிறது.",
        "Option B is correct; Article 360 continues indefinitely without periodic renewal.", "விருப்பம் B சரியானது; காலமுறை புதுப்பித்தலின்றி சரத்து 360 காலவரையின்றித் தொடர்கிறது.",
        "Option C describes the upper limit of Article 356.", "விருப்பம் C சரத்து 356-ன் உச்சவரம்பை விவரிக்கிறது.",
        "Option D describes the 1-to-3 year structure of Article 356.", "விருப்பம் D சரத்து 356-ன் 1 முதல் 3 ஆண்டு கட்டமைப்பை விவரிக்கிறது.",
        "TNPSC High-Yield Contrast: Articles 352 and 356 require parliamentary renewal every 6 months; Article 360 requires NO renewal once approved!",
        "TNPSC உயர்-விளைச்சல் ஒப்பீடு: சரத்துகள் 352 மற்றும் 356-க்கு ஒவ்வொரு 6 மாதங்களுக்கும் பாராளுமன்றப் புதுப்பித்தல் தேவை; சரத்து 360-க்கு ஒருமுறை ஒப்புதல் பெற்ற பின் புதுப்பித்தல் தேவையில்லை!",
        "Its revocation can be done at any time by the President without parliamentary approval.",
        "பாராளுமன்ற ஒப்புதலின்றி குடியரசுத் தலைவரால் எந்த நேரத்திலும் இதனை ரத்து செய்ய முடியும்."
    ))

    return qs

def build_and_validate_pyq():
    qs = (get_pyq_questions_batch1() + 
          get_pyq_questions_batch2() + 
          get_pyq_questions_batch3() + 
          get_pyq_questions_batch4() + 
          get_pyq_questions_batch5())
    
    print(f"[PYQ] Total questions generated: {len(qs)}")
    assert len(qs) == 50, f"Expected 50 questions, got {len(qs)}"

    # Check key distribution
    dist = dict(Counter([q["correct_answer"] for q in qs]))
    print(f"[PYQ] Key Distribution: {dist}")
    assert dist == {"A": 12, "B": 13, "C": 13, "D": 12}, f"Distribution mismatch: {dist}"

    # Check uniqueness of stems
    stems = [q["question_en"].strip().lower() for q in qs]
    assert len(stems) == len(set(stems)), "Duplicate stems found in PYQ set!"
    print("[PYQ] Stems are 100% unique.")

    out_file = "data/questions/polity/emergency_provisions_pyq.json"
    alias_file = "data/questions/polity/emergency_provisions_pyq_practice.json"
    os.makedirs(os.path.dirname(out_file), exist_ok=True)
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2, ensure_ascii=False)
    with open(alias_file, "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2, ensure_ascii=False)
    print(f"[PYQ] Saved to {out_file} and {alias_file}")

    rep = ContentValidator.validate_file(out_file, expected_count=50, expected_prefix=PREFIX)
    print(f"[PYQ] Validator Status: {'PASS' if rep.is_valid else 'FAIL'} | Audited: {rep.total_audited}")
    if rep.issues:
        for iss in rep.issues:
            print(f"  [{iss.severity}] {iss.question_id}: {iss.message}")
        assert False, "Validation failed!"
    print("[PYQ] Validation PASSED with 0 issues!")

if __name__ == "__main__":
    build_and_validate_pyq()
