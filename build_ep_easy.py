# -*- coding: utf-8 -*-
"""
Generator for Emergency Provisions Easy MCQs (50 questions: EP_E_001 to EP_E_050)
Strictly adheres to:
1. 24-field schema verified by validator.py
2. Bilingual parity (English and Tamil)
3. Balanced answer distribution: A: 13, B: 13, C: 12, D: 12
4. Full coverage of foundational Emergency Provisions
"""

import json
import os
from collections import Counter
from ep_mcq_helper import make_ep_q
from tools.nova_content_engine.validator import ContentValidator

PREFIX = "EP_E_"
DIFF = "Easy"

def get_easy_questions():
    qs = []

    # 001 - Key A
    qs.append(make_ep_q(
        PREFIX, 1, DIFF, "Concept MCQ", "Overview of Emergency Provisions",
        "Which Part of the Constitution of India contains the Emergency Provisions (Articles 352 to 360)?",
        "இந்திய அரசியலமைப்பின் எந்தப் பகுதியில் அவசரநிலைப் பிரிவுகள் (சரத்துகள் 352 முதல் 360 வரை) இடம்பெற்றுள்ளன?",
        "Part XVIII", "பகுதி XVIII",
        "Part XVII", "பகுதி XVII",
        "Part XVI", "பகுதி XVI",
        "Part XIX", "பகுதி XIX",
        "A",
        "Part XVIII of the Indian Constitution encompasses Articles 352 to 360, dealing comprehensively with the three types of emergencies.",
        "இந்திய அரசியலமைப்பின் பகுதி XVIII சரத்துகள் 352 முதல் 360 வரை உள்ள மூன்று வகையான அவசரநிலைகள் குறித்து விரிவாகக் கையாள்கிறது.",
        "Option A is correct; Part XVIII contains Emergency Provisions.", "விருப்பம் A சரியானது; பகுதி XVIII அவசரநிலைப் பிரிவுகளைக் கொண்டுள்ளது.",
        "Option B contains Part XVII, which deals with Official Language (Articles 343-351).", "விருப்பம் B பகுதி XVII ஆட்சி மொழி தொடர்பானது.",
        "Option C contains Part XVI, which deals with Special Provisions relating to Certain Classes.", "விருப்பம் C பகுதி XVI குறிப்பிட்ட வகுப்பினருக்கான சிறப்பு விதிகள் தொடர்பானது.",
        "Option D contains Part XIX, which deals with Miscellaneous provisions.", "விருப்பம் D பகுதி XIX இதர விதிகள் தொடர்பானது.",
        "Remember: Part XVIII = Emergency Provisions (Articles 352 to 360).",
        "நினைவில் கொள்க: பகுதி XVIII = அவசரநிலைப் பிரிவுகள் (சரத்துகள் 352 முதல் 360 வரை).",
        "The emergency provisions enable the federal structure to convert into a unitary one during crises without a formal constitutional amendment.",
        "அவசரநிலைப் பிரிவுகள் முறையான அரசியலமைப்பு திருத்தமின்றி கூட்டாட்சி முறையை ஒற்றையாட்சி முறையாக மாற்ற உதவுகின்றன."
    ))

    # 002 - Key B
    qs.append(make_ep_q(
        PREFIX, 2, DIFF, "Concept MCQ", "Constitutional Sources",
        "From which foreign constitution was the provision for the 'suspension of Fundamental Rights during National Emergency' borrowed?",
        "தேசிய அவசரநிலையின் போது 'அடிப்படை உரிமைகள் இடைநிறுத்தம்' செய்யப்படும் முறை எந்த நாட்டின் அரசியலமைப்பிலிருந்து பெறப்பட்டது?",
        "Constitution of the United States of America", "அமெரிக்க ஐக்கிய நாடுகளின் அரசியலமைப்பு",
        "Weimar Constitution of Germany", "ஜெர்மனியின் வெய்மர் அரசியலமைப்பு",
        "Constitution of Australia", "ஆஸ்திரேலிய அரசியலமைப்பு",
        "Constitution of Canada", "கனடா அரசியலமைப்பு",
        "B",
        "The feature of suspension of Fundamental Rights during emergency was borrowed from the Weimar Constitution of Germany. (The emergency provisions themselves were largely drawn from the Government of India Act, 1935).",
        "அவசரநிலையின் போது அடிப்படை உரிமைகள் இடைநிறுத்தம் செய்யப்படும் அம்சம் ஜெர்மனியின் வெய்மர் அரசியலமைப்பிலிருந்து பெறப்பட்டது. (அவசரநிலை கட்டமைப்பு 1935 இந்திய அரசுச் சட்டத்திலிருந்து பெறப்பட்டது).",
        "Option A is incorrect; US Bill of Rights cannot be suspended in this manner.", "விருப்பம் A தவறானது; அமெரிக்க அடிப்படை உரிமைகள் இவ்வாறு இடைநிறுத்தப்படுவதில்லை.",
        "Option B is correct; Weimar Constitution of Germany is the direct source.", "விருப்பம் B சரியானது; ஜெர்மனியின் வெய்மர் அரசியலமைப்பே இதன் நேரடி மூலம்.",
        "Option C provided concurrent list and freedom of trade.", "விருப்பம் C பொதுப்பட்டியல் மற்றும் வர்த்தக சுதந்திரத்தை வழங்கியது.",
        "Option D provided federation with a strong Centre and residual powers.", "விருப்பம் D வலுவான மத்திய அரசைக் கொண்ட கூட்டாட்சியை வழங்கியது.",
        "TNPSC Trap: Emergency framework = GoI Act 1935; Suspension of Fundamental Rights = Weimar Constitution of Germany.",
        "TNPSC பொறி: அவசரநிலை கட்டமைப்பு = 1935 இந்திய அரசுச் சட்டம்; அடிப்படை உரிமைகள் இடைநிறுத்தம் = ஜெர்மனியின் வெய்மர் அரசியலமைப்பு.",
        "Articles 358 and 359 govern the suspension of fundamental rights and their judicial enforcement respectively.",
        "சரத்துகள் 358 மற்றும் 359 முறையே அடிப்படை உரிமைகள் மற்றும் அவற்றின் அமலாக்கத்தை இடைநிறுத்துவதை நிர்வகிக்கின்றன."
    ))

    # 003 - Key C
    qs.append(make_ep_q(
        PREFIX, 3, DIFF, "Concept MCQ", "National Emergency Grounds",
        "Under Article 352 of the Constitution, on which of the following three grounds can the President proclaim a National Emergency?",
        "அரசியலமைப்பின் சரத்து 352-ன் கீழ், குடியரசுத் தலைவர் பின்வரும் எந்த மூன்று காரணங்களின் அடிப்படையில் தேசிய அவசரநிலையைப் பிரகடனப்படுத்த முடியும்?",
        "War, Communal Riots, or Economic Depression", "போர், வகுப்புவாதக் கலவரங்கள், அல்லது பொருளாதார மந்தநிலை",
        "External Aggression, Natural Calamity, or General Strike", "வெளிநாட்டு ஆக்கிரமிப்பு, இயற்கை பேரிடர், அல்லது பொது வேலைநிறுத்தம்",
        "War, External Aggression, or Armed Rebellion", "போர், வெளிநாட்டு ஆக்கிரமிப்பு, அல்லது ஆயுதமேந்திய கிளர்ச்சி",
        "Internal Disturbance, Fiscal Deficit, or Insurgency", "உள்நாட்டு அமைதியின்மை, நிதிப் பற்றாக்குறை, அல்லது கிளர்ச்சி",
        "C",
        "Under Article 352(1), the President can proclaim a National Emergency when the security of India or any part thereof is threatened by 'War, External Aggression, or Armed Rebellion'.",
        "சரத்து 352(1)-ன் கீழ், 'போர், வெளிநாட்டு ஆக்கிரமிப்பு அல்லது ஆயுதமேந்திய கிளர்ச்சி' ஆகியவற்றால் இந்தியாவின் பாதுகாப்புக்கு அச்சுறுத்தல் ஏற்படும் போது குடியரசுத் தலைவர் தேசிய அவசரநிலையைப் பிரகடனம் செய்யலாம்.",
        "Option A includes economic depression which relates to Article 360, not 352.", "விருப்பம் A பொருளாதார மந்தநிலையைக் குறிப்பிடுகிறது, இது சரத்து 360 தொடர்பானது.",
        "Option B includes natural calamities which are managed under disaster management acts.", "விருப்பம் B இயற்கை பேரிடர்களைக் குறிப்பிடுகிறது, இது பேரிடர் மேலாண்மைச் சட்டத்தின் கீழ் வருகிறது.",
        "Option C is the exact constitutional triplet under Article 352.", "விருப்பம் C என்பது சரத்து 352-ன் கீழான துல்லியமான மூன்று காரணங்கள் ஆகும்.",
        "Option D includes 'Internal Disturbance', which was deleted by the 44th Amendment in 1978.", "விருப்பம் D 'உள்நாட்டு அமைதியின்மை' என்பதைக் கொண்டுள்ளது, இது 1978-ல் 44-வது திருத்தத்தால் நீக்கப்பட்டது.",
        "Remember: Present grounds under Art 352 = War, External Aggression, Armed Rebellion.",
        "நினைவில் கொள்க: சரத்து 352-ன் கீழான தற்போதைய காரணங்கள் = போர், வெளிநாட்டு ஆக்கிரமிப்பு, ஆயுதமேந்திய கிளர்ச்சி.",
        "An emergency declared on the grounds of 'War' or 'External Aggression' is known as 'External Emergency', while one declared on 'Armed Rebellion' is known as 'Internal Emergency'.",
        "'போர்' அல்லது 'வெளிநாட்டு ஆக்கிரமிப்பு' அடிப்படையில் அறிவிக்கப்படுவது 'வெளிப்புற அவசரநிலை' எனவும், 'ஆயுதமேந்திய கிளர்ச்சி' அடிப்படையில் அறிவிக்கப்படுவது 'உள்நாட்டு அவசரநிலை' எனவும் அழைக்கப்படுகிறது."
    ))

    # 004 - Key D
    qs.append(make_ep_q(
        PREFIX, 4, DIFF, "Concept MCQ", "44th Amendment Safeguards",
        "By which Constitutional Amendment Act was the vague ground 'Internal Disturbance' replaced by 'Armed Rebellion' in Article 352?",
        "சரத்து 352-ல் இருந்த தெளிவற்ற 'உள்நாட்டு அமைதியின்மை' என்ற சொல் எந்த அரசியலமைப்பு திருத்தச் சட்டத்தின் மூலம் 'ஆயுதமேந்திய கிளர்ச்சி' என மாற்றப்பட்டது?",
        "38th Constitutional Amendment Act, 1975", "38-வது அரசியலமைப்பு திருத்தச் சட்டம், 1975",
        "42nd Constitutional Amendment Act, 1976", "42-வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
        "43rd Constitutional Amendment Act, 1977", "43-வது அரசியலமைப்பு திருத்தச் சட்டம், 1977",
        "44th Constitutional Amendment Act, 1978", "44-வது அரசியலமைப்பு திருத்தச் சட்டம், 1978",
        "D",
        "The 44th Constitutional Amendment Act, 1978 substituted the words 'armed rebellion' for 'internal disturbance' to prevent the political misuse of emergency provisions as occurred in 1975.",
        "1975-ல் நிகழ்ந்தது போன்ற அவசரநிலைப் பிரிவுகளின் அரசியல் தவறான பயன்பாட்டைத் தடுப்பதற்காக 44-வது அரசியலமைப்பு திருத்தச் சட்டம் 1978, 'உள்நாட்டு அமைதியின்மை' என்ற சொல்லுக்குப் பதிலாக 'ஆயுதமேந்திய கிளர்ச்சி' என்ற சொல்லை மாற்றியது.",
        "Option A is the 38th Amendment (1975), which made the President's satisfaction non-justiciable.", "விருப்பம் A 38-வது திருத்தம் (1975), இது குடியரசுத் தலைவரின் திருப்தியை நீதிமன்ற ஆய்வுக்கு அப்பாற்பட்டதாக ஆக்கியது.",
        "Option B is the 42nd Amendment (1976), which enabled emergency in a part of India.", "விருப்பம் B 42-வது திருத்தம் (1976), இது இந்தியாவின் ஒரு பகுதிக்கு அவசரநிலையை அறிவிக்க அனுமதித்தது.",
        "Option C is the 43rd Amendment (1977), which restored certain Supreme Court powers.", "விருப்பம் C 43-வது திருத்தம் (1977), இது உச்ச நீதிமன்ற அதிகாரங்களை மீட்டெடுத்தது.",
        "Option D is correct; the 44th Amendment Act, 1978 introduced 'armed rebellion'.", "விருப்பம் D சரியானது; 44-வது திருத்தச் சட்டம் 1978 'ஆயுதமேந்திய கிளர்ச்சி' என்ற சொல்லை அறிமுகப்படுத்தியது.",
        "44th Amendment (1978) = Janata Government under Morarji Desai corrected emergency excesses.",
        "44-வது திருத்தம் (1978) = மொரார்ஜி தேசாய் தலைமையிலான ஜனதா அரசு அவசரநிலை அத்துமீறல்களை சரிசெய்தது.",
        "Before 1978, the phrase 'internal disturbance' was so broad that mere political opposition demonstrations were cited to impose emergency in June 1975.",
        "1978-க்கு முன்பு, 'உள்நாட்டு அமைதியின்மை' என்ற சொல் மிகவும் பரந்ததாக இருந்ததால், அரசியல் ஆர்ப்பாட்டங்களை வைத்தே ஜூன் 1975-ல் அவசரநிலை விதிக்கப்பட்டது."
    ))

    # 005 - Key A
    qs.append(make_ep_q(
        PREFIX, 5, DIFF, "Concept MCQ", "Cabinet Written Advice",
        "According to Article 352(3) inserted by the 44th Amendment Act, the President can proclaim a National Emergency only after receiving a written recommendation from:",
        "44-வது திருத்தச் சட்டத்தால் சேர்க்கப்பட்ட சரத்து 352(3)-ன் படி, குடியரசுத் தலைவர் யாரிடமிருந்து எழுத்துப்பூர்வ பரிந்துரையைப் பெற்ற பின்னரே தேசிய அவசரநிலையைப் பிரகடனப்படுத்த முடியும்?",
        "The Union Cabinet (Prime Minister and other Ministers of Cabinet rank)", "மத்திய அமைச்சரவை (பிரதமர் மற்றும் அமைச்சரவை அந்தஸ்துள்ள பிற அமைச்சர்கள்)",
        "The Prime Minister alone in his personal capacity", "தனது தனிப்பட்ட முறையில் பிரதமர் மட்டுமே",
        "The Chief Justice of India and the Attorney General", "இந்தியத் தலைமை நீதிபதி மற்றும் தலைமை அரசு வழக்கறிஞர்",
        "The National Security Advisor and Home Secretary", "தேசிய பாதுகாப்பு ஆலோசகர் மற்றும் உள்துறைச் செயலாளர்",
        "A",
        "Article 352(3) explicitly mandates that the President shall not issue a proclamation unless the decision of the Union Cabinet (i.e. Prime Minister and other Ministers of Cabinet rank) has been communicated to him in writing.",
        "சரத்து 352(3) மத்திய அமைச்சரவையின் (அதாவது பிரதமர் மற்றும் அமைச்சரவை அந்தஸ்துள்ள பிற அமைச்சர்கள்) முடிவு எழுத்துப்பூர்வமாகத் தெரிவிக்கப்படாமல் குடியரசுத் தலைவர் பிரகடனத்தை வெளியிடக் கூடாது என்று கட்டாயமாக்குகிறது.",
        "Option A is correct; written communication from the Union Cabinet is mandatory.", "விருப்பம் A சரியானது; மத்திய அமைச்சரவையின் எழுத்துப்பூர்வ பரிந்துரை கட்டாயமாகும்.",
        "Option B is incorrect; in 1975 Indira Gandhi advised the President alone, which was banned by the 44th Amendment.", "விருப்பம் B தவறானது; 1975-ல் இந்திரா காந்தி தன்னிச்சையாக ஆலோசனை வழங்கினார், இது 44-வது திருத்தத்தால் தடுக்கப்பட்டது.",
        "Option C is incorrect; judiciary has no executive role in emergency advice.", "விருப்பம் C தவறானது; நீதித்துறைக்கு இதில் நிர்வாகப் பங்கு இல்லை.",
        "Option D is incorrect; civil servants cannot advise the President directly.", "விருப்பம் D தவறானது; அதிகாரிகள் நேரடியாக குடியரசுத் தலைவருக்கு ஆலோசனை கூற முடியாது.",
        "This is the ONLY place in the entire Constitution of India where the word 'Cabinet' (அமைச்சரவை) is explicitly defined and used (Article 352(3)).",
        "முழு இந்திய அரசியலமைப்பிலும் 'அமைச்சரவை' (Cabinet) என்ற சொல் வெளிப்படையாக வரையறுக்கப்பட்டு பயன்படுத்தப்பட்டுள்ள ஒரே இடம் சரத்து 352(3) மட்டுமே ஆகும்.",
        "Article 352(3) was enacted specifically to safeguard against unilateral decisions by a Prime Minister without the knowledge of the Cabinet.",
        "அமைச்சரவைக்குத் தெரியாமல் பிரதமர் தன்னிச்சையாக முடிவெடுப்பதைத் தடுப்பதற்காகவே சரத்து 352(3) இயற்றப்பட்டது."
    ))

    # 006 - Key B
    qs.append(make_ep_q(
        PREFIX, 6, DIFF, "Concept MCQ", "Parliamentary Approval Window",
        "Within what time frame must a proclamation of National Emergency (Article 352) be approved by both Houses of Parliament?",
        "சரத்து 352-ன் கீழான தேசிய அவசரநிலைப் பிரகடனம் பாராளுமன்றத்தின் இரு அவைகளாலும் எத்தனை காலத்திற்குள் அங்கீகரிக்கப்பட வேண்டும்?",
        "Within two months from the date of its issue", "அது வெளியிடப்பட்ட தேதியிலிருந்து இரண்டு மாதங்களுக்குள்",
        "Within one month from the date of its issue", "அது வெளியிடப்பட்ட தேதியிலிருந்து ஒரு மாதத்திற்குள்",
        "Within six months from the date of its issue", "அது வெளியிடப்பட்ட தேதியிலிருந்து ஆறு மாதங்களுக்குள்",
        "Within fourteen days from the date of its issue", "அது வெளியிடப்பட்ட தேதியிலிருந்து பதினான்கு நாட்களுக்குள்",
        "B",
        "Originally the period allowed for approval was two months, but the 44th Constitutional Amendment Act, 1978 reduced this period to one month from the date of its issue.",
        "தொடக்கத்தில் ஒப்புதலுக்கான காலம் இரண்டு மாதங்களாக இருந்தது; ஆனால் 44-வது அரசியலமைப்பு திருத்தச் சட்டம் 1978 இக்காலத்தை வெளியிடப்பட்ட தேதியிலிருந்து ஒரு மாதமாகக் குறைத்தது.",
        "Option A was the original provision, but reduced to 1 month by 44th CAA; 2 months still applies to Arts 356 and 360.", "விருப்பம் A அசல் விதி, ஆனால் 44-வது திருத்தத்தால் 1 மாதமாகக் குறைக்கப்பட்டது; 2 மாதங்கள் சரத்துகள் 356 மற்றும் 360-க்கு பொருந்தும்.",
        "Option B is correct; exactly one month under Article 352(4).", "விருப்பம் B சரியானது; சரத்து 352(4)-ன் கீழ் சரியாக ஒரு மாதம்.",
        "Option C is the duration of an approved emergency, not the initial approval deadline.", "விருப்பம் C அங்கீகரிக்கப்பட்ட அவசரநிலையின் காலம், ஆரம்ப ஒப்புதல் காலக்கெடு அல்ல.",
        "Option D is the notice period for a special sitting to revoke emergency.", "விருப்பம் D அவசரநிலையை ரத்து செய்வதற்கான கூட்டத்திற்கான அறிவிப்பு காலம்.",
        "Remember the '1 - 2 - 2' Rule: National Emergency (Art 352) = 1 Month; President's Rule (Art 356) = 2 Months; Financial Emergency (Art 360) = 2 Months.",
        "'1 - 2 - 2' விதியை நினைவில் கொள்க: தேசிய அவசரநிலை (352) = 1 மாதம்; குடியரசுத் தலைவர் ஆட்சி (356) = 2 மாதங்கள்; நிதி அவசரநிலை (360) = 2 மாதங்கள்.",
        "If Lok Sabha is dissolved during this one month, the proclamation survives until 30 days from the first sitting of the reconstituted Lok Sabha, provided Rajya Sabha approved it in the meantime.",
        "இந்த ஒரு மாத காலத்தில் மக்களவை கலைக்கப்பட்டால், மாநிலங்களவை ஒப்புதல் அளித்திருந்தால், புதிய மக்களவை கூடிய 30 நாட்கள் வரை பிரகடனம் நீடிக்கும்."
    ))

    # 007 - Key C
    qs.append(make_ep_q(
        PREFIX, 7, DIFF, "Concept MCQ", "Approval Majority",
        "What type of majority is required in each House of Parliament to approve or extend a proclamation of National Emergency under Article 352?",
        "சரத்து 352-ன் கீழ் தேசிய அவசரநிலைப் பிரகடனத்தை அங்கீகரிக்க அல்லது நீட்டிக்க பாராளுமன்றத்தின் ஒவ்வொரு அவையிலும் என்ன வகையான பெரும்பான்மை தேவைப்படுகிறது?",
        "Simple majority of members present and voting", "கூட்டத்தில் பங்கேற்று வாக்களிக்கும் உறுப்பினர்களின் எளிய பெரும்பான்மை",
        "Effective majority of total remaining members", "மீதமுள்ள மொத்த உறுப்பினர்களின் பயனுள்ள பெரும்பான்மை",
        "Special majority: A majority of the total membership of that House and not less than two-thirds of the members present and voting", "சிறப்புப் பெரும்பான்மை: அந்த அவையின் மொத்த உறுப்பினர் எண்ணிக்கையில் பெரும்பான்மை மற்றும் வருகை தந்து வாக்களிக்கும் உறுப்பினர்களில் மூன்றில் இரண்டு பங்குக்கு குறையாமல்",
        "Absolute majority of all elected members together with ratification by half of the State Legislatures", "அனைத்து தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்களின் முழுமையான பெரும்பான்மை மற்றும் பாதி மாநில சட்டமன்றங்களின் ஒப்புதல்",
        "C",
        "Introduced by the 44th Amendment Act, 1978, every resolution approving or extending a National Emergency must be passed by a special majority in each House: majority of the total membership + 2/3rd of members present and voting.",
        "1978-ஆம் ஆண்டின் 44-வது திருத்தச் சட்டத்தால் அறிமுகப்படுத்தப்பட்டபடி, தேசிய அவசரநிலையை அங்கீகரிக்கும் அல்லது நீட்டிக்கும் ஒவ்வொரு தீர்மானமும் சிறப்புப் பெரும்பான்மையால் (மொத்த உறுப்பினர்களில் பெரும்பான்மை + வருகை தந்து வாக்களிப்பவர்களில் 2/3 பங்கு) நிறைவேற்றப்பட வேண்டும்.",
        "Option A applied prior to the 44th Amendment, and still applies to Articles 356 and 360.", "விருப்பம் A 44-வது திருத்தத்திற்கு முன்பு பொருந்தியது, மேலும் தற்போதும் சரத்துகள் 356 மற்றும் 360-க்கு பொருந்துகிறது.",
        "Option B is used for removing presiding officers.", "விருப்பம் B சபாநாயகர் போன்றோரை நீக்கப் பயன்படுகிறது.",
        "Option C is the exact constitutional majority under Article 352(6).", "விருப்பம் C என்பது சரத்து 352(6)-ன் கீழான துல்லியமான சிறப்புப் பெரும்பான்மை ஆகும்.",
        "Option D applies to federal constitutional amendments under Article 368.", "விருப்பம் D சரத்து 368-ன் கீழான கூட்டாட்சி திருத்தங்களுக்குப் பொருந்தும்.",
        "TNPSC Trap: National Emergency approval needs SPECIAL majority; President's Rule & Financial Emergency need SIMPLE majority.",
        "TNPSC பொறி: தேசிய அவசரநிலைக்கு சிறப்புப் பெரும்பான்மை தேவை; குடியரசுத் தலைவர் ஆட்சி மற்றும் நிதி அவசரநிலைக்கு எளிய பெரும்பான்மை போதுமானது.",
        "Before the 44th Amendment Act, 1978, a National Emergency could be approved by a simple majority.",
        "1978-ஆம் ஆண்டின் 44-வது திருத்தச் சட்டத்திற்கு முன்பு, தேசிய அவசரநிலையை எளிய பெரும்பான்மை மூலமே அங்கீகரிக்க முடியும் என்ற நிலை இருந்தது."
    ))

    # 008 - Key D
    qs.append(make_ep_q(
        PREFIX, 8, DIFF, "Concept MCQ", "Emergency Duration",
        "Once approved by both Houses of Parliament, for how long does a proclamation of National Emergency remain in force at a time?",
        "பாராளுமன்றத்தின் இரு அவைகளாலும் அங்கீகரிக்கப்பட்ட பிறகு, தேசிய அவசரநிலைப் பிரகடனம் ஒரு நேரத்தில் எவ்வளவு காலத்திற்கு அமலில் இருக்கும்?",
        "Three years", "மூன்று ஆண்டுகள்",
        "One year", "ஒரு ஆண்டு",
        "Indefinitely without any further parliamentary approval", "எந்தவொரு கூடுதல் பாராளுமன்ற ஒப்புதலும் இன்றி காலவரையின்றி",
        "Six months", "ஆறு மாதங்கள்",
        "D",
        "Under Article 352(5), once approved, the National Emergency continues for six months. It can be extended for an indefinite period with an approval of Parliament for every six months.",
        "சரத்து 352(5)-ன் படி, ஒப்புதல் அளிக்கப்பட்டதும் தேசிய அவசரநிலை ஆறு மாதங்களுக்கு நீடிக்கும். ஒவ்வொரு ஆறு மாதங்களுக்கும் பாராளுமன்ற ஒப்புதலைப் பெற்று இதை காலவரையின்றி நீட்டிக்க முடியும்.",
        "Option A is the maximum limit for President's Rule under Article 356.", "விருப்பம் A என்பது சரத்து 356-ன் கீழான குடியரசுத் தலைவர் ஆட்சிக்கான அதிகபட்ச வரம்பு.",
        "Option B is the duration by which the life of Lok Sabha can be extended at a time.", "விருப்பம் B என்பது மக்களவையின் ஆயுளை ஒரு நேரத்தில் நீட்டிக்கக்கூடிய காலம்.",
        "Option C applies to Financial Emergency under Article 360.", "விருப்பம் C சரத்து 360-ன் கீழான நிதி அவசரநிலைக்குப் பொருந்தும்.",
        "Option D is correct; exactly six months at a time under Article 352(5).", "விருப்பம் D சரியானது; சரத்து 352(5)-ன் கீழ் ஒரு நேரத்தில் சரியாக ஆறு மாதங்கள்.",
        "The provision for periodic approval by Parliament every six months was introduced by the 44th Amendment Act, 1978.",
        "ஒவ்வொரு ஆறு மாதங்களுக்கும் பாராளுமன்றத்தின் காலமுறை ஒப்புதல் பெற வேண்டும் என்ற விதி 44-வது திருத்தச் சட்டம் 1978 மூலம் கொண்டுவரப்பட்டது.",
        "Prior to 1978, once approved by Parliament, a National Emergency remained in force indefinitely until revoked by the executive.",
        "1978-க்கு முன்பு, பாராளுமன்றம் ஒப்புதல் அளித்தவுடன், நிர்வாகத்தால் ரத்து செய்யப்படும் வரை தேசிய அவசரநிலை காலவரையின்றி அமலில் இருந்தது."
    ))

    # 009 - Key A
    qs.append(make_ep_q(
        PREFIX, 9, DIFF, "Concept MCQ", "Revocation Mechanism",
        "A proclamation of National Emergency may be revoked by the President by a subsequent proclamation. Does such a revocation require parliamentary approval?",
        "தேசிய அவசரநிலைப் பிரகடனத்தை குடியரசுத் தலைவர் அடுத்த பிரகடனம் மூலம் திரும்பப் பெறலாம். அவ்வாறு திரும்பப் பெறுவதற்கு பாராளுமன்ற ஒப்புதல் தேவையா?",
        "No, parliamentary approval is not required to revoke a National Emergency", "இல்லை, தேசிய அவசரநிலையைத் திரும்பப் பெற பாராளுமன்ற ஒப்புதல் தேவையில்லை",
        "Yes, it requires a special majority in both Houses of Parliament", "ஆம், பாராளுமன்றத்தின் இரு அவைகளிலும் சிறப்புப் பெரும்பான்மை தேவை",
        "Yes, it requires approval by a simple majority of Lok Sabha only", "ஆம், மக்களவையின் எளிய பெரும்பான்மை ஒப்புதல் மட்டுமே தேவை",
        "Yes, it requires concurrence of the Supreme Court of India", "ஆம், இந்திய உச்ச நீதிமன்றத்தின் இசைவு தேவை",
        "A",
        "Under Article 352(2), a proclamation of emergency may be revoked or varied by a subsequent proclamation by the President. Revocation does NOT require any parliamentary approval.",
        "சரத்து 352(2)-ன் படி, அவசரநிலைப் பிரகடனத்தை குடியரசுத் தலைவர் மற்றொரு பிரகடனம் மூலம் ரத்து செய்யலாம் அல்லது மாற்றியமைக்கலாம். இவ்வாறு ரத்து செய்வதற்கு எந்தவொரு பாராளுமன்ற ஒப்புதலும் தேவையில்லை.",
        "Option A is correct; President can revoke the proclamation at any time without parliamentary approval.", "விருப்பம் A சரியானது; குடியரசுத் தலைவர் பாராளுமன்ற ஒப்புதலின்றி எப்போது வேண்டுமானாலும் ரத்து செய்யலாம்.",
        "Option B is incorrect; parliamentary approval is needed to continue, not to revoke.", "விருப்பம் B தவறானது; தொடர்வதற்குத்தான் ஒப்புதல் தேவை, ரத்து செய்ய அல்ல.",
        "Option C is incorrect; that applies when Lok Sabha forces revocation under Art 352(7).", "விருப்பம் C தவறானது; இது மக்களவை ரத்து செய்யக் கோரும் போது பொருந்தும்.",
        "Option D is incorrect; judiciary has no role in executive revocation.", "விருப்பம் D தவறானது; நீதித்துறைக்கு இதில் பங்கு இல்லை.",
        "Proclamation needs Parliamentary Approval (within 1 month, special majority); Revocation by President needs NO Parliamentary Approval.",
        "பிரகடனத்திற்கு பாராளுமன்ற ஒப்புதல் தேவை (1 மாதத்திற்குள், சிறப்புப் பெரும்பான்மை); குடியரசுத் தலைவரின் ரத்துக்கு பாராளுமன்ற ஒப்புதல் தேவையில்லை.",
        "Additionally, under Article 352(7) introduced by 44th CAA, the President MUST revoke the emergency if the Lok Sabha passes a resolution disapproving it by a simple majority.",
        "கூடுதலாக, 44-வது திருத்தத்தால் சேர்க்கப்பட்ட சரத்து 352(7)-ன் கீழ், மக்களவை எளிய பெரும்பான்மையுடன் நிராகரிப்புத் தீர்மானத்தை நிறைவேற்றினால், குடியரசுத் தலைவர் கட்டாயமாக அவசரநிலையை ரத்து செய்ய வேண்டும்."
    ))

    # 010 - Key B
    qs.append(make_ep_q(
        PREFIX, 10, DIFF, "Concept MCQ", "Lok Sabha Disapproval",
        "Under Article 352(7) and (8) introduced by the 44th Amendment Act, if notice in writing signed by not less than what proportion of the total members of Lok Sabha is given, a special sitting of the House must be held within 14 days to consider disapproving the emergency?",
        "44-வது திருத்தச் சட்டத்தால் சேர்க்கப்பட்ட சரத்து 352(7) மற்றும் (8)-ன் கீழ், மக்களவையின் மொத்த உறுப்பினர்களில் எத்தனையாவது பங்கு உறுப்பினர்கள் கையொப்பமிட்ட எழுத்துப்பூர்வ அறிவிப்பை அளித்தால், அவசரநிலையை நிராகரிப்பது குறித்து பரிசீலிக்க 14 நாட்களுக்குள் அவையின் சிறப்புக் கூட்டம் கூட்டப்பட வேண்டும்?",
        "Not less than one-fourth (1/4th) of the total members", "மொத்த உறுப்பினர்களில் நான்கில் ஒரு பங்குக்கு குறையாமல்",
        "Not less than one-tenth (1/10th) of the total members", "மொத்த உறுப்பினர்களில் பத்தில் ஒரு பங்குக்கு குறையாமல்",
        "Not less than one-third (1/3rd) of the total members", "மொத்த உறுப்பினர்களில் மூன்றில் ஒரு பங்குக்கு குறையாமல்",
        "Not less than half (1/2) of the total members", "மொத்த உறுப்பினர்களில் பாதியளவுக்கு குறையாமல்",
        "B",
        "Under Article 352(8), where a notice in writing signed by not less than one-tenth (1/10th) of the total number of members of the Lok Sabha is given to the Speaker (or to the President if the House is not in session), a special sitting of the House shall be held within 14 days to consider a resolution disapproving the proclamation.",
        "சரத்து 352(8)-ன் படி, மக்களவையின் மொத்த உறுப்பினர்களில் பத்தில் ஒரு பங்குக்கு (1/10) குறையாத உறுப்பினர்கள் கையொப்பமிட்ட அறிவிப்பை சபாநாயகரிடம் (அல்லது அவை கூடாதபோது குடியரசுத் தலைவரிடம்) அளித்தால், அவசரநிலையை நிராகரிக்கும் தீர்மானத்தை பரிசீலிக்க 14 நாட்களுக்குள் அவையின் சிறப்புக் கூட்டம் நடத்தப்பட வேண்டும்.",
        "Option A is incorrect; 1/4th applies to impeachment notice against the President (Art 61).", "விருப்பம் A தவறானது; 1/4 பங்கு குடியரசுத் தலைவர் மீதான பதவி நீக்க அறிவிப்புக்கு பொருந்தும்.",
        "Option B is correct; exactly 1/10th of total Lok Sabha members.", "விருப்பம் B சரியானது; மக்களவையின் மொத்த உறுப்பினர்களில் சரியாக 1/10 பங்கு.",
        "Option C is incorrect.", "விருப்பம் C தவறானது.",
        "Option D is incorrect.", "விருப்பம் D தவறானது.",
        "Remember: 1/10th Lok Sabha members + 14 days notice = Special Sitting to disapprove National Emergency (Simple Majority).",
        "நினைவில் கொள்க: 1/10 மக்களவை உறுப்பினர்கள் + 14 நாட்கள் அறிவிப்பு = தேசிய அவசரநிலையை நிராகரிக்க சிறப்புக் கூட்டம் (எளிய பெரும்பான்மை).",
        "Notice is given to the Speaker if the House is in session, or to the President if the House is not in session.",
        "அவை அமர்வில் இருந்தால் சபாநாயகரிடமும், அவை கூடாதபோது குடியரசுத் தலைவரிடமும் இந்த அறிவிப்பு வழங்கப்பட வேண்டும்."
    ))

    # 011 - Key C
    qs.append(make_ep_q(
        PREFIX, 11, DIFF, "Concept MCQ", "Disapproval vs Approval",
        "Which of the following statements correctly distinguishes a resolution of disapproval of National Emergency from a resolution of approval?",
        "தேசிய அவசரநிலையை நிராகரிக்கும் தீர்மானத்திற்கும் அங்கீகரிக்கும் தீர்மானத்திற்கும் உள்ள வேறுபாட்டை பின்வருவனவற்றில் எது சரியாகக் காட்டுகிறது?",
        "Disapproval requires both Houses, while approval requires only Lok Sabha", "நிராகரிப்புக்கு இரு அவைகளும் தேவை, ஆனால் அங்கீகாரத்திற்கு மக்களவை மட்டுமே போதுமானது",
        "Disapproval requires a special majority, while approval requires a simple majority", "நிராகரிப்புக்கு சிறப்புப் பெரும்பான்மை தேவை, ஆனால் அங்கீகாரத்திற்கு எளிய பெரும்பான்மை போதுமானது",
        "Disapproval requires passage by Lok Sabha only with a simple majority, whereas approval requires passage by both Houses with a special majority", "நிராகரிப்பு தீர்மானம் மக்களவையில் மட்டும் எளிய பெரும்பான்மையால் நிறைவேற்றப்பட வேண்டும், ஆனால் அங்கீகார தீர்மானம் இரு அவைகளாலும் சிறப்புப் பெரும்பான்மையால் நிறைவேற்றப்பட வேண்டும்",
        "Disapproval can only be initiated by the Rajya Sabha with the consent of the Vice-President", "நிராகரிப்பை துணை குடியரசுத் தலைவரின் ஒப்புதலுடன் மாநிலங்களவை மட்டுமே தொடங்க முடியும்",
        "C",
        "A resolution of disapproval is required to be passed by the Lok Sabha ONLY, and by a SIMPLE majority. In contrast, a resolution approving the emergency must be passed by BOTH Houses, and by a SPECIAL majority.",
        "நிராகரிப்புத் தீர்மானம் மக்களவையால் மட்டுமே மற்றும் எளிய பெரும்பான்மையால் நிறைவேற்றப்பட வேண்டும். மாறாக, அவசரநிலையை அங்கீகரிக்கும் தீர்மானம் இரு அவைகளாலும் மற்றும் சிறப்புப் பெரும்பான்மையால் நிறைவேற்றப்பட வேண்டும்.",
        "Option A is inverted; approval needs both Houses, disapproval needs only Lok Sabha.", "விருப்பம் A தலைகீழானது; அங்கீகாரத்திற்கு இரு அவைகளும், நிராகரிப்புக்கு மக்களவை மட்டுமே தேவை.",
        "Option B is inverted; disapproval needs simple majority, approval needs special majority.", "விருப்பம் B தலைகீழானது; நிராகரிப்புக்கு எளிய பெரும்பான்மையும், அங்கீகாரத்திற்கு சிறப்புப் பெரும்பான்மையும் தேவை.",
        "Option C accurately captures both distinctions (House requirement and majority requirement).", "விருப்பம் C இரண்டு வேறுபாடுகளையும் (அவை தேவை மற்றும் பெரும்பான்மை தேவை) துல்லியமாகப் படம்பிடிக்கிறது.",
        "Option D is incorrect; Rajya Sabha has no role in a resolution of disapproval under Art 352(7).", "விருப்பம் D தவறானது; சரத்து 352(7)-ன் கீழான நிராகரிப்புத் தீர்மானத்தில் மாநிலங்களவைக்கு பங்கு இல்லை.",
        "Approval = Both Houses + Special Majority. Disapproval = Lok Sabha Only + Simple Majority.",
        "அங்கீகாரம் = இரு அவைகளும் + சிறப்புப் பெரும்பான்மை. நிராகரிப்பு = மக்களவை மட்டும் + எளிய பெரும்பான்மை.",
        "This safeguard gives the directly elected representatives in Lok Sabha the power to end an unwanted emergency immediately.",
        "இந்த பாதுகாப்பு மக்களால் நேரடியாக தேர்ந்தெடுக்கப்பட்ட மக்களவை உறுப்பினர்களுக்கு தேவையற்ற அவசரநிலையை உடனடியாக முடிவுக்குக் கொண்டுவரும் அதிகாரத்தை அளிக்கிறது."
    ))

    # 012 - Key D
    qs.append(make_ep_q(
        PREFIX, 12, DIFF, "Concept MCQ", "Executive Impact",
        "During the operation of a National Emergency under Article 352, what happens to the executive power of the State Governments under Article 353(a)?",
        "சரத்து 352-ன் கீழ் தேசிய அவசரநிலை அமலில் உள்ள போது, சரத்து 353(a)-ன் கீழ் மாநில அரசுகளின் நிர்வாக அதிகாரத்திற்கு என்ன நிகழ்கிறது?",
        "The State Governments are completely dismissed and dissolved", "மாநில அரசுகள் முழுமையாகப் பதவி நீக்கம் செய்யப்பட்டு கலைக்கப்படுகின்றன",
        "The State executive power is placed under the direct control of the State High Court", "மாநில நிர்வாக அதிகாரம் மாநில உயர் நீதிமன்றத்தின் நேரடிக் கட்டுப்பாட்டின் கீழ் வைக்கப்படுகிறது",
        "The State executive power remains suspended until the emergency ends", "அவசரநிலை முடியும் வரை மாநில நிர்வாக அதிகாரம் இடைநிறுத்தப்பட்டிருக்கும்",
        "The State Governments continue to function, but are brought under the complete executive control of the Centre (Union can issue directions on any matter)", "மாநில அரசுகள் தொடர்ந்து செயல்படுகின்றன, ஆனால் அவை மத்திய அரசின் முழு நிர்வாகக் கட்டுப்பாட்டின் கீழ் கொண்டுவரப்படுகின்றன (மத்திய அரசு எந்த விஷயத்திலும் வழிகாட்டுதல்களை வழங்கலாம்)",
        "D",
        "Under Article 353(a), the executive power of the Union extends to giving directions to any State as to the manner in which its executive power is to be exercised. Crucially, the State Government is NOT suspended or dismissed; it continues to function under central direction.",
        "சரத்து 353(a)-ன் கீழ், மாநில அரசு எவ்வாறு தனது நிர்வாக அதிகாரத்தைப் பயன்படுத்த வேண்டும் என்பது குறித்து வழிகாட்டுதல்களை வழங்கும் அதிகாரம் மத்திய அரசுக்கு நீட்டிக்கப்படுகிறது. முக்கியமாக, மாநில அரசு கலைக்கப்படுவதோ இடைநிறுத்தப்படுவதோ இல்லை; மத்திய அரசின் வழிகாட்டுதலின் கீழ் அது தொடர்ந்து செயல்படுகிறது.",
        "Option A describes President's Rule (Article 356), not National Emergency.", "விருப்பம் A குடியரசுத் தலைவர் ஆட்சியை (சரத்து 356) விவரிக்கிறது, தேசிய அவசரநிலையை அல்ல.",
        "Option B is incorrect; courts do not take over the executive.", "விருப்பம் B தவறானது; நீதிமன்றங்கள் நிர்வாகத்தை ஏற்பதில்லை.",
        "Option C is incorrect; state government is not suspended.", "விருப்பம் C தவறானது; மாநில அரசு இடைநிறுத்தப்படுவதில்லை.",
        "Option D is the precise constitutional impact under Article 353(a).", "விருப்பம் D என்பது சரத்து 353(a)-ன் கீழான துல்லியமான அரசியலமைப்பு விளைவாகும்.",
        "In National Emergency: State Government operates under Union direction. In President's Rule: State Council of Ministers is dismissed.",
        "தேசிய அவசரநிலையில்: மாநில அரசு மத்திய வழிகாட்டுதலில் இயங்கும். குடியரசுத் தலைவர் ஆட்சியில்: மாநில அமைச்சரவை கலைக்கப்படுகிறது.",
        "In normal times, the Centre can give executive directions to states only on specified matters (Articles 256, 257); during emergency, it can direct on ANY matter.",
        "சாதாரண காலங்களில், மத்திய அரசு குறிப்பிட்ட சில விவகாரங்களில் மட்டுமே மாநிலங்களுக்கு வழிகாட்ட முடியும்; ஆனால் அவசரநிலையின் போது எந்தவொரு விவகாரத்திலும் வழிகாட்டலாம்."
    ))

    # 013 - Key A
    qs.append(make_ep_q(
        PREFIX, 13, DIFF, "Concept MCQ", "Legislative Impact",
        "Under Article 353(b), during a National Emergency, what power does Parliament acquire regarding subjects enumerated in the State List (List II)?",
        "சரத்து 353(b)-ன் கீழ், தேசிய அவசரநிலையின் போது, மாநிலப் பட்டியலில் (பட்டியல் II) உள்ள துறைகள் தொடர்பாக பாராளுமன்றம் என்ன அதிகாரத்தைப் பெறுகிறது?",
        "Parliament becomes empowered to make laws for the whole or any part of India with respect to any matter in the State List", "மாநிலப் பட்டியலில் உள்ள எந்தவொரு விவகாரம் தொடர்பாகவும் இந்தியா முழுமைக்கும் அல்லது அதன் எந்தப் பகுதிக்கும் சட்டம் இயற்றும் அதிகாரத்தை பாராளுமன்றம் பெறுகிறது",
        "The State Legislature is immediately dissolved and its members forfeit their seats", "மாநில சட்டமன்றம் உடனடியாகக் கலைக்கப்பட்டு அதன் உறுப்பினர்கள் தங்கள் பதவிகளை இழக்கின்றனர்",
        "The State List is permanently deleted and merged into the Union List", "மாநிலப் பட்டியல் நிரந்தரமாக நீக்கப்பட்டு மத்தியப் பட்டியலுடன் இணைக்கப்படுகிறது",
        "Parliament can only legislate if two-thirds of the States ratify by resolution", "இரண்டு அல்லது அதற்கு மேற்பட்ட மாநிலங்கள் தீர்மானம் மூலம் ஒப்புதல் அளித்தால் மட்டுமே பாராளுமன்றம் சட்டம் இயற்ற முடியும்",
        "A",
        "Under Article 353(b), Parliament becomes competent to make laws on any subject in the State List. However, the legislative power of the State Legislature is NOT suspended; it can still make laws, but parliamentary laws prevail in case of repugnancy (Article 251).",
        "சரத்து 353(b)-ன் கீழ், மாநிலப் பட்டியலில் உள்ள எந்தவொரு துறை மீதும் சட்டம் இயற்ற பாராளுமன்றத்திற்கு அதிகாரம் கிடைக்கிறது. இருப்பினும், மாநில சட்டமன்றத்தின் சட்டம் இயற்றும் அதிகாரம் பறிக்கப்படுவதில்லை; அதுவும் சட்டம் இயற்றலாம், ஆனால் முரண்பாடு ஏற்பட்டால் பாராளுமன்ற சட்டமே மேலோங்கும் (சரத்து 251).",
        "Option A is correct; Parliament acquires concurrent legislative power over State List subjects.", "விருப்பம் A சரியானது; மாநிலப் பட்டியல் துறைகள் மீது பாராளுமன்றம் சட்டம் இயற்றும் அதிகாரத்தைப் பெறுகிறது.",
        "Option B describes President's Rule (Art 356), not National Emergency.", "விருப்பம் B குடியரசுத் தலைவர் ஆட்சியை விவரிக்கிறது.",
        "Option C is incorrect; the 7th Schedule is not altered permanently.", "விருப்பம் C தவறானது; ஏழாவது அட்டவணை நிரந்தரமாக மாற்றப்படுவதில்லை.",
        "Option D describes Article 252, not Article 353(b).", "விருப்பம் D சரத்து 252-ஐ விவரிக்கிறது.",
        "During National Emergency, State Legislature is NOT dissolved; Parliament only acquires concurrent power to override state laws.",
        "தேசிய அவசரநிலையின் போது, மாநில சட்டமன்றம் கலைக்கப்படுவதில்லை; மாநில சட்டங்களை விட மேலோங்கும் பொதுவான அதிகாரத்தை மட்டுமே பாராளுமன்றம் பெறுகிறது.",
        "Under Article 250(2), laws made by Parliament on State subjects during emergency cease to have effect 6 months after the emergency ends.",
        "சரத்து 250(2)-ன் படி, அவசரநிலையின் போது மாநிலத் துறைகள் மீது பாராளுமன்றம் இயற்றிய சட்டங்கள் அவசரநிலை முடிந்த 6 மாதங்களுக்குப் பிறகு காலாவதியாகிவிடும்."
    ))

    # 014 - Key B
    qs.append(make_ep_q(
        PREFIX, 14, DIFF, "Concept MCQ", "Life of Lok Sabha",
        "While a proclamation of National Emergency is in operation, by what duration can the normal five-year term of the Lok Sabha be extended by Parliament by law?",
        "தேசிய அவசரநிலைப் பிரகடனம் அமலில் இருக்கும் போது, மக்களவையின் சாதாரண ஐந்தாண்டு பதவிக்காலத்தை பாராளுமன்றம் சட்டத்தின் மூலம் எவ்வளவு காலம் நீட்டிக்க முடியும்?",
        "For any period up to five years at a time", "ஒரு நேரத்தில் ஐந்து ஆண்டுகள் வரை எந்தக் காலத்திற்கும்",
        "For a period not exceeding one year at a time, and not exceeding six months after the emergency ceases to operate", "ஒரு நேரத்தில் ஒரு ஆண்டுக்கு மிகாமல், அவசரநிலை முடிவுக்கு வந்த பிறகு ஆறு மாதங்களுக்கு மிகாமல்",
        "For an indefinite period without any time limitation", "எந்தவொரு கால வரம்பும் இன்றி காலவரையின்றி",
        "For six months only in the entire history of that Parliament", "அந்த பாராளுமன்றத்தின் முழு வரலாற்றிலும் ஆறு மாதங்களுக்கு மட்டுமே",
        "B",
        "Under the Proviso to Article 83(2), the term of the Lok Sabha may, while a proclamation of Emergency is in operation, be extended by Parliament by law for a period not exceeding one year at a time, and not extending beyond six months after the proclamation has ceased to operate.",
        "சரத்து 83(2)-ன் வரம்புரையின் கீழ், அவசரநிலைப் பிரகடனம் அமலில் இருக்கும் போது, பாராளுமன்றம் சட்டத்தின் மூலம் மக்களவையின் பதவிக்காலத்தை ஒரு நேரத்தில் ஒரு ஆண்டுக்கு மிகாமல் நீட்டிக்கலாம்; அவசரநிலை முடிவுக்கு வந்த பிறகு இந்த நீட்டிப்பு ஆறு மாதங்களுக்கு மேல் நீடிக்கக் கூடாது.",
        "Option A is excessive and unconstitutional.", "விருப்பம் A வரம்பற்றது மற்றும் அரசியலமைப்பிற்கு முரணானது.",
        "Option B is the exact constitutional provision under Article 83(2) Proviso.", "விருப்பம் B என்பது சரத்து 83(2) வரம்புரையின் கீழான துல்லியமான விதி ஆகும்.",
        "Option C is incorrect; it cannot be extended indefinitely.", "விருப்பம் C தவறானது; காலவரையின்றி நீட்டிக்க முடியாது.",
        "Option D is incorrect.", "விருப்பம் D தவறானது.",
        "Lok Sabha term extension during Emergency: 1 year at a time; cannot extend beyond 6 months after emergency ends.",
        "அவசரநிலையின் போது மக்களவை பதவிக்கால நீட்டிப்பு: ஒரு நேரத்தில் 1 ஆண்டு; அவசரநிலை முடிந்த 6 மாதங்களுக்கு மேல் நீடிக்க முடியாது.",
        "The life of the 5th Lok Sabha (1971-1977) was extended twice by one year each during the 1975-1977 emergency.",
        "1975-1977 அவசரநிலையின் போது 5-வது மக்களவையின் (1971-1977) பதவிக்காலம் தலா ஒரு வருடம் வீதம் இரண்டு முறை நீட்டிக்கப்பட்டது."
    ))

    # 015 - Key C
    qs.append(make_ep_q(
        PREFIX, 15, DIFF, "Concept MCQ", "Life of State Legislative Assembly",
        "Under the Proviso to Article 172(1), during a National Emergency, Parliament can also extend the normal five-year term of a State Legislative Assembly by law for:",
        "சரத்து 172(1)-ன் வரம்புரையின் கீழ், தேசிய அவசரநிலையின் போது, ஒரு மாநில சட்டமன்றப் பேரவையின் சாதாரண ஐந்தாண்டு பதவிக்காலத்தையும் பாராளுமன்றம் சட்டத்தின் மூலம் எவ்வளவு காலம் நீட்டிக்க முடியும்?",
        "Two years at a time", "ஒரு நேரத்தில் இரண்டு ஆண்டுகள்",
        "Six months only in total", "மொத்தமாகவே ஆறு மாதங்கள் மட்டுமே",
        "One year at a time, subject to a maximum of six months after the emergency ceases to operate", "ஒரு நேரத்தில் ஒரு ஆண்டு வீதம், அவசரநிலை முடிவுக்கு வந்த பிறகு அதிகபட்சமாக ஆறு மாதங்களுக்கு உட்பட்டு",
        "Three years with the consent of the State Governor", "மாநில ஆளுநரின் ஒப்புதலுடன் மூன்று ஆண்டுகள்",
        "C",
        "Under Article 172(1) Proviso, Parliament may by law extend the term of a State Legislative Assembly during a National Emergency for a period not exceeding one year at a time and not extending beyond six months after the emergency has ceased to operate.",
        "சரத்து 172(1) வரம்புரையின் படி, தேசிய அவசரநிலையின் போது மாநில சட்டமன்றப் பேரவையின் பதவிக்காலத்தை பாராளுமன்றம் சட்டத்தின் மூலம் ஒரு நேரத்தில் ஒரு ஆண்டுக்கு மிகாமல் நீட்டிக்கலாம்; மேலும் அவசரநிலை முடிந்த 6 மாதங்களுக்குப் பிறகு இது நீடிக்கக் கூடாது.",
        "Option A is incorrect; extension is 1 year at a time.", "விருப்பம் A தவறானது; ஒரு நேரத்தில் 1 ஆண்டு மட்டுமே நீட்டிக்க முடியும்.",
        "Option B is the post-emergency expiration ceiling, not the yearly extension.", "விருப்பம் B அவசரநிலைக்குப் பிந்தைய காலாவதி வரம்பு.",
        "Option C is the exact constitutional rule under Article 172(1) Proviso.", "விருப்பம் C என்பது சரத்து 172(1) வரம்புரையின் கீழான சரியான விதி ஆகும்.",
        "Option D is incorrect; Governor consent does not alter the 1-year rule.", "விருப்பம் D தவறானது; ஆளுநர் ஒப்புதல் 1 ஆண்டு விதியை மாற்றாது.",
        "Both Lok Sabha (Art 83(2)) and State Legislative Assembly (Art 172(1)) terms can be extended by PARLIAMENT by 1 year at a time during National Emergency.",
        "தேசிய அவசரநிலையின் போது மக்களவை (சரத்து 83(2)) மற்றும் மாநில சட்டமன்றம் (சரத்து 172(1)) இரண்டின் பதவிக்காலத்தையும் பாராளுமன்றமே ஒரு நேரத்தில் 1 ஆண்டு நீட்டிக்க முடியும்.",
        "Note that it is PARLIAMENT, not the State Legislature, that has the constitutional power to extend the life of a State Assembly.",
        "மாநில சட்டமன்றத்தின் ஆயுளை நீட்டிக்கும் அதிகாரம் மாநில சட்டமன்றத்திற்கு இல்லை, பாராளுமன்றத்திற்கே உள்ளது என்பதை கவனத்தில் கொள்க."
    ))

    # 016 - Key D
    qs.append(make_ep_q(
        PREFIX, 16, DIFF, "Concept MCQ", "Article 358 Automatic Suspension",
        "According to Article 358 of the Constitution, which Fundamental Rights are automatically suspended as soon as a proclamation of National Emergency is issued?",
        "அரசியலமைப்பின் சரத்து 358-ன் படி, தேசிய அவசரநிலைப் பிரகடனம் வெளியிடப்பட்ட உடனேயே எந்த அடிப்படை உரிமைகள் தானாகவே இடைநிறுத்தப்படுகின்றன?",
        "Right to Constitutional Remedies under Article 32", "சரத்து 32-ன் கீழான அரசியலமைப்புப் பரிகார உரிமை",
        "Right to Equality under Articles 14 to 18", "சரத்துகள் 14 முதல் 18 வரையிலான சமத்துவ உரிமை",
        "Right to Life and Personal Liberty under Article 21", "சரத்து 21-ன் கீழான வாழ்வுரிமை மற்றும் தனிநபர் சுதந்திர உரிமை",
        "Six fundamental freedoms guaranteed under Article 19", "சரத்து 19-ன் கீழ் உத்தரவாதம் அளிக்கப்பட்ட ஆறு அடிப்படை சுதந்திரங்கள்",
        "D",
        "Under Article 358, as soon as a proclamation of National Emergency is made, the six fundamental freedoms guaranteed by Article 19 (speech, assembly, association, movement, residence, profession) are automatically suspended without requiring any separate presidential order.",
        "சரத்து 358-ன் கீழ், தேசிய அவசரநிலைப் பிரகடனம் செய்யப்பட்ட உடனேயே, சரத்து 19 உத்தரவாதம் அளிக்கும் ஆறு அடிப்படை சுதந்திரங்கள் (பேச்சு, கூட்டம் கூடுதல், சங்கம் அமைத்தல், நடமாட்டம், வசிப்பிடம், தொழில்) தனி குடியரசுத் தலைவர் ஆணை எதுவுமின்றி தானாகவே இடைநிறுத்தப்படுகின்றன.",
        "Option A is governed by Article 359, not automatically by Article 358.", "விருப்பம் A சரத்து 359-ஆல் நிர்வகிக்கப்படுகிறது, 358-ஆல் தானாக அல்ல.",
        "Option B is suspended only if specified by presidential order under Article 359.", "விருப்பம் B சரத்து 359-ன் கீழ் குடியரசுத் தலைவர் ஆணையில் குறிப்பிடப்பட்டால் மட்டுமே இடைநிறுத்தப்படும்.",
        "Option C can NEVER be suspended under any circumstance (44th CAA).", "விருப்பம் C எந்த சூழ்நிலையிலும் ஒருபோதும் இடைநிறுத்தப்பட முடியாது (44-வது திருத்தம்).",
        "Option D is correct; Article 19 freedoms are automatically suspended under Article 358.", "விருப்பம் D சரியானது; சரத்து 19 சுதந்திரங்கள் சரத்து 358-ன் கீழ் தானாக இடைநிறுத்தப்படுகின்றன.",
        "Article 358 = Automatic suspension of Article 19 only. Article 359 = Suspension of ENFORCEMENT of rights specified by President (except Arts 20 & 21).",
        "சரத்து 358 = சரத்து 19 மட்டுமே தானாக இடைநிறுத்தம். சரத்து 359 = குடியரசுத் தலைவர் குறிப்பிடும் உரிமைகளின் அமலாக்கம் இடைநிறுத்தம் (சரத்துகள் 20 & 21 தவிர).",
        "As soon as the emergency ceases to operate, Article 19 automatically revives and springs back into full legal force.",
        "அவசரநிலை முடிவுக்கு வந்த உடனேயே, சரத்து 19 தானாகவே புத்துயிர் பெற்று முழு சட்ட சக்தியுடன் செயல்படத் தொடங்குகிறது."
    ))

    # 017 - Key A
    qs.append(make_ep_q(
        PREFIX, 17, DIFF, "Concept MCQ", "Article 358 Restriction",
        "Following the 44th Constitutional Amendment Act, 1978, under which circumstance alone can the Fundamental Rights under Article 19 be automatically suspended under Article 358?",
        "1978-ஆம் ஆண்டின் 44-வது அரசியலமைப்பு திருத்தச் சட்டத்தைத் தொடர்ந்து, எந்த சூழ்நிலையில் மட்டுமே சரத்து 19-ன் கீழான அடிப்படை உரிமைகள் சரத்து 358-ன் கீழ் தானாகவே இடைநிறுத்தப்பட முடியும்?",
        "Only when the National Emergency is proclaimed on the grounds of War or External Aggression (and NOT on Armed Rebellion)", "போர் அல்லது வெளிநாட்டு ஆக்கிரமிப்பு காரணங்களுக்காக மட்டுமே தேசிய அவசரநிலை அறிவிக்கப்படும் போது (ஆயுதமேந்திய கிளர்ச்சிக்காக அல்ல)",
        "Only when the emergency is approved unanimously by both Houses of Parliament", "பாராளுமன்றத்தின் இரு அவைகளாலும் அவசரநிலை ஒருமனதாக அங்கீகரிக்கப்படும் போது மட்டுமே",
        "Only when Financial Emergency is proclaimed alongside National Emergency", "தேசிய அவசரநிலையுடன் நிதி அவசரநிலையும் சேர்த்து அறிவிக்கப்படும் போது மட்டுமே",
        "Only when the Chief Justice of India gives a written concurrence", "இந்தியத் தலைமை நீதிபதி எழுத்துப்பூர்வ ஒப்புதல் அளிக்கும் போது மட்டுமே",
        "A",
        "The 44th Amendment Act, 1978 restricted Article 358 by providing that Article 19 can be suspended ONLY when the National Emergency is declared on the grounds of 'war' or 'external aggression', and NOT when it is declared on the ground of 'armed rebellion'.",
        "44-வது திருத்தச் சட்டம் 1978, 'போர்' அல்லது 'வெளிநாட்டு ஆக்கிரமிப்பு' அடிப்படையில் தேசிய அவசரநிலை அறிவிக்கப்படும் போது மட்டுமே சரத்து 19 இடைநிறுத்தப்பட முடியும் என்றும், 'ஆயுதமேந்திய கிளர்ச்சி' அடிப்படையில் அறிவிக்கப்படும் போது சரத்து 19 இடைநிறுத்தப்பட முடியாது என்றும் வரம்பை விதித்தது.",
        "Option A is the exact constitutional limitation introduced by the 44th Amendment in Article 358(1).", "விருப்பம் A என்பது சரத்து 358(1)-ல் 44-வது திருத்தத்தால் கொண்டுவரப்பட்ட துல்லியமான வரம்பு ஆகும்.",
        "Option B is incorrect; unanimity is not required.", "விருப்பம் B தவறானது; ஒருமனதான முடிவு தேவையில்லை.",
        "Option C is incorrect; Financial Emergency has no connection to Article 358.", "விருப்பம் C தவறானது; நிதி அவசரநிலைக்கு இதனுடன் தொடர்பில்லை.",
        "Option D is incorrect; CJI has no role.", "விருப்பம் D தவறானது; தலைமை நீதிபதிக்கு இதில் பங்கு இல்லை.",
        "Armed Rebellion = Article 19 CANNOT be suspended! War / External Aggression = Article 19 is automatically suspended.",
        "ஆயுதமேந்திய கிளர்ச்சி = சரத்து 19-ஐ இடைநிறுத்த முடியாது! போர் / வெளிநாட்டு ஆக்கிரமிப்பு = சரத்து 19 தானாக இடைநிறுத்தப்படும்.",
        "This safeguard was added because in 1975, Article 19 was suspended on the ground of 'internal disturbance', leading to massive arrests of political dissidents.",
        "1975-ல் 'உள்நாட்டு அமைதியின்மை' என்ற காரணத்தால் சரத்து 19 இடைநிறுத்தப்பட்டு அரசியல் தலைவர்கள் கைது செய்யப்பட்டதால் இந்த பாதுகாப்பு சேர்க்கப்பட்டது."
    ))

    # 018 - Key B
    qs.append(make_ep_q(
        PREFIX, 18, DIFF, "Concept MCQ", "Inviolable Rights",
        "By virtue of the 44th Constitutional Amendment Act, 1978, the Presidential Order under Article 359 CANNOT suspend the right to move any court for the enforcement of which Fundamental Rights?",
        "1978-ஆம் ஆண்டின் 44-வது அரசியலமைப்பு திருத்தச் சட்டத்தின்படி, சரத்து 359-ன் கீழான குடியரசுத் தலைவர் ஆணை எந்த அடிப்படை உரிமைகளை அமல்படுத்துவதற்காக நீதிமன்றத்தை அணுகும் உரிமையை இடைநிறுத்த முடியாது?",
        "Articles 14 and 19", "சரத்துகள் 14 மற்றும் 19",
        "Articles 20 and 21", "சரத்துகள் 20 மற்றும் 21",
        "Articles 25 and 26", "சரத்துகள் 25 மற்றும் 26",
        "Articles 32 and 226", "சரத்துகள் 32 மற்றும் 226",
        "B",
        "The 44th Constitutional Amendment Act, 1978 amended Article 359 to provide that the President cannot suspend the right to move the court for the enforcement of Fundamental Rights guaranteed by Article 20 (protection in respect of conviction for offences) and Article 21 (protection of life and personal liberty).",
        "1978-ஆம் ஆண்டின் 44-வது அரசியலமைப்பு திருத்தச் சட்டம் சரத்து 359-ஐத் திருத்தி, சரத்து 20 (குற்றங்களுக்கான தண்டனை குறித்த பாதுகாப்பு) மற்றும் சரத்து 21 (வாழ்வுரிமை மற்றும் தனிநபர் சுதந்திரப் பாதுகாப்பு) ஆகிய உரிமைகளை அமல்படுத்துவதற்காக நீதிமன்றத்தை அணுகும் உரிமையை குடியரசுத் தலைவர் இடைநிறுத்த முடியாது எனத் திட்டவட்டமாக வகுத்தது.",
        "Option A can be suspended by presidential order under Article 359.", "விருப்பம் A சரத்து 359-ன் கீழ் குடியரசுத் தலைவர் ஆணையால் இடைநிறுத்தப்படலாம்.",
        "Option B is the famous non-derogable core: Articles 20 and 21 are INVIOLABLE even during emergency.", "விருப்பம் B என்பது புகழ்பெற்ற மாற்ற முடியாத முக்கிய அம்சம்: அவசரநிலையிலும் சரத்துகள் 20 & 21 புனிதமானவை.",
        "Option C (religious freedom) can be suspended if specified in the presidential order.", "விருப்பம் C (மத சுதந்திரம்) குடியரசுத் தலைவர் குறிப்பிட்டால் இடைநிறுத்தப்படலாம்.",
        "Option D is the remedial machinery itself.", "விருப்பம் D பரிகார வழிமுறையாகும்.",
        "Articles 20 & 21 are NEVER suspended under ANY emergency! (ADM Jabalpur infamous ruling was legislatively overruled by 44th CAA).",
        "எந்தவொரு அவசரநிலையிலும் சரத்துகள் 20 & 21 ஒருபோதும் இடைநிறுத்தப்பட முடியாது! (ஏ.டி.எம். ஜபல்பூர் சர்ச்சைக்குரிய தீர்ப்பு 44-வது திருத்தத்தால் ரத்து செய்யப்பட்டது).",
        "Article 20 protects against ex-post facto laws, double jeopardy, and self-incrimination; Article 21 protects life and personal liberty.",
        "சரத்து 20 பின்னோக்கிய சட்டங்கள், இரட்டை தண்டனை மற்றும் தனக்கு எதிராக சாட்சியமளிப்பதில் இருந்து பாதுகாக்கிறது; சரத்து 21 வாழ்வு மற்றும் தனிநபர் சுதந்திரத்தைப் பாதுகாக்கிறது."
    ))

    # 019 - Key C
    qs.append(make_ep_q(
        PREFIX, 19, DIFF, "Concept MCQ", "Article 358 vs 359 Scope",
        "What is the territorial extent of the suspension of Fundamental Rights under Article 358 compared to Article 359?",
        "சரத்து 359-உடன் ஒப்பிடும் போது சரத்து 358-ன் கீழ் அடிப்படை உரிமைகள் இடைநிறுத்தப்படுவதன் பிராந்திய எல்லை என்ன?",
        "Article 358 applies only to the border states, whereas Article 359 applies to Union Territories only", "சரத்து 358 எல்லை மாநிலங்களுக்கு மட்டுமே பொருந்தும், ஆனால் சரத்து 359 யூனியன் பிரதேசங்களுக்கு மட்டுமே பொருந்தும்",
        "Article 358 can be confined to a single district, whereas Article 359 always covers the entire globe", "சரத்து 358 ஒரு மாவட்டத்திற்கு மட்டுமே மட்டுப்படுத்தப்படலாம், ஆனால் சரத்து 359 எப்போதும் உலகம் முழுவதையும் உள்ளடக்கியது",
        "Article 358 extends to the entire country automatically, whereas Article 359 may extend to the entire country or to any specified part thereof", "சரத்து 358 தானாகவே நாடு முழுவதும் நீட்டிக்கப்படுகிறது, ஆனால் சரத்து 359 நாடு முழுமைக்கும் அல்லது அதன் ஏதேனும் குறிப்பிட்ட பகுதிக்கு நீட்டிக்கப்படலாம்",
        "Both articles are strictly confined to the National Capital Territory of Delhi", "இரு சரத்துகளும் தில்லி தேசிய தலைநகர் பகுதிக்கு மட்டுமே கண்டிப்பாக மட்டுப்படுத்தப்பட்டுள்ளன",
        "C",
        "Article 358 automatically extends to the entire territory of India without territorial restriction. In contrast, under Article 359, the presidential order suspending the enforcement of specified rights may apply to the entire country or only to any specified part thereof.",
        "சரத்து 358 பிராந்திய வரம்பின்றி தானாகவே இந்தியா முழுவதும் நீட்டிக்கப்படுகிறது. மாறாக, சரத்து 359-ன் கீழ் உரிமைகள் அமலாக்கத்தை இடைநிறுத்தும் குடியரசுத் தலைவர் ஆணை நாடு முழுமைக்கும் அல்லது ஏதேனும் குறிப்பிட்ட பகுதிக்கும் பொருந்தும் வகையில் வெளியிடப்படலாம்.",
        "Option A is incorrect.", "விருப்பம் A தவறானது.",
        "Option B is incorrect.", "விருப்பம் B தவறானது.",
        "Option C correctly highlights the difference in territorial application.", "விருப்பம் C பிராந்திய பயன்பாட்டில் உள்ள வேறுபாட்டைச் சரியாக விளக்குகிறது.",
        "Option D is incorrect.", "விருப்பம் D தவறானது.",
        "Article 358 = Entire country automatically. Article 359 = Entire country OR specific parts as notified in Presidential Order.",
        "சரத்து 358 = நாடு முழுவதும் தானாகவே. சரத்து 359 = நாடு முழுவதும் அல்லது குடியரசுத் தலைவர் ஆணையில் அறிவிக்கப்படும் குறிப்பிட்ட பகுதிகள்.",
        "Also, Article 358 suspends Article 19 for the ENTIRE duration of emergency, while Article 359 order can specify a shorter period.",
        "மேலும், சரத்து 358 அவசரநிலையின் முழு காலத்திற்கும் சரத்து 19-ஐ இடைநிறுத்துகிறது, ஆனால் சரத்து 359 ஆணை குறைந்த காலத்தை மட்டுமே குறிப்பிடலாம்."
    ))

    # 020 - Key D
    qs.append(make_ep_q(
        PREFIX, 20, DIFF, "Concept MCQ", "Article 355 Duty of Union",
        "Which article of the Constitution imposes an express constitutional duty on the Union to protect every State against external aggression and internal disturbance?",
        "ஒவ்வொரு மாநிலத்தையும் வெளிநாட்டு ஆக்கிரமிப்பு மற்றும் உள்நாட்டு அமைதியின்மையிலிருந்து பாதுகாக்கும் வெளிப்படையான அரசியலமைப்பு கடமையை மத்திய அரசுக்கு விதிக்கும் சரத்து எது?",
        "Article 352", "சரத்து 352",
        "Article 356", "சரத்து 356",
        "Article 360", "சரத்து 360",
        "Article 355", "சரத்து 355",
        "D",
        "Article 355 states: 'It shall be the duty of the Union to protect every State against external aggression and internal disturbance and to ensure that the government of every State is carried on in accordance with the provisions of this Constitution.'",
        "சரத்து 355 கூறுகிறது: 'ஒவ்வொரு மாநிலத்தையும் வெளிநாட்டு ஆக்கிரமிப்பு மற்றும் உள்நாட்டு அமைதியின்மையிலிருந்து பாதுகாப்பதும், ஒவ்வொரு மாநிலத்தின் அரசும் இந்த அரசியலமைப்பின் விதிகளுக்கு இணங்க நடத்தப்படுவதை உறுதி செய்வதும் மத்திய அரசின் கடமையாகும்.'",
        "Option A provides for proclamation of National Emergency.", "விருப்பம் A தேசிய அவசரநிலைப் பிரகடனத்தை வழங்குகிறது.",
        "Option B provides for President's Rule in States.", "விருப்பம் B மாநிலங்களில் குடியரசுத் தலைவர் ஆட்சியை வழங்குகிறது.",
        "Option C provides for Financial Emergency.", "விருப்பம் C நிதி அவசரநிலையை வழங்குகிறது.",
        "Option D is the exact constitutional text imposing the protective duty on the Union under Article 355.", "விருப்பம் D என்பது சரத்து 355-ன் கீழ் மத்திய அரசுக்கு பாதுகாப்பு கடமையை விதிக்கும் துல்லியமான அரசியலமைப்பு சரத்து ஆகும்.",
        "Article 355 is the constitutional justification and gateway for the Centre to intervene in States under Article 356.",
        "சரத்து 355 என்பது சரத்து 356-ன் கீழ் மாநிலங்களில் மத்திய அரசு தலையிடுவதற்கான அரசியலமைப்பு நியாயப்படுத்தல் மற்றும் நுழைவாயிலாகும்.",
        "Notice that while 'internal disturbance' was deleted from Article 352, it remains present in Article 355.",
        "சரத்து 352-லிருந்து 'உள்நாட்டு அமைதியின்மை' நீக்கப்பட்ட போதிலும், சரத்து 355-ல் அது தொடர்ந்து நீடிக்கிறது என்பதை கவனிக்கவும்."
    ))

    # 021 - Key A
    qs.append(make_ep_q(
        PREFIX, 21, DIFF, "Concept MCQ", "President's Rule Article",
        "Under which article of the Constitution can the President proclaim President's Rule (State Emergency) on the failure of constitutional machinery in a State?",
        "ஒரு மாநிலத்தில் அரசியலமைப்பு இயந்திரம் செயலிழக்கும் போது, எந்த அரசியலமைப்புச் சரத்தின் கீழ் குடியரசுத் தலைவர், குடியரசுத் தலைவர் ஆட்சியைப் (மாநில அவசரநிலை) பிரகடனப்படுத்த முடியும்?",
        "Article 356", "சரத்து 356",
        "Article 352", "சரத்து 352",
        "Article 360", "சரத்து 360",
        "Article 370", "சரத்து 370",
        "A",
        "Article 356 empowers the President to issue a proclamation of President's Rule in a State if he is satisfied, on receipt of a report from the Governor of the State or otherwise, that the government of the State cannot be carried on in accordance with the provisions of the Constitution.",
        "ஒரு மாநிலத்தின் ஆளுநரிடமிருந்து அறிக்கை பெறப்பட்டதன் பேரில் அல்லது வேறு வழியில், அந்த மாநிலத்தின் அரசு அரசியலமைப்பு விதிகளின்படி நடைபெற முடியாது என்று குடியரசுத் தலைவர் திருப்தியடைந்தால், சரத்து 356-ன் கீழ் குடியரசுத் தலைவர் ஆட்சியைப் பிரகடனம் செய்யலாம்.",
        "Option A is correct; Article 356 governs President's Rule.", "விருப்பம் A சரியானது; சரத்து 356 குடியரசுத் தலைவர் ஆட்சியை நிர்வகிக்கிறது.",
        "Option B governs National Emergency.", "விருப்பம் B தேசிய அவசரநிலையை நிர்வகிக்கிறது.",
        "Option C governs Financial Emergency.", "விருப்பம் C நிதி அவசரநிலையை நிர்வகிக்கிறது.",
        "Option D was temporary provisions regarding Jammu and Kashmir.", "விருப்பம் D ஜம்மு காஷ்மீர் தொடர்பான தற்காலிக விதிகளாக இருந்தது.",
        "President's Rule is popularly called 'State Emergency' or 'Constitutional Emergency', but the Constitution does not use the word 'emergency' for this situation.",
        "குடியரசுத் தலைவர் ஆட்சி பிரபலமாக 'மாநில அவசரநிலை' என்று அழைக்கப்படுகிறது, ஆனால் அரசியலமைப்பு இதற்கு 'அவசரநிலை' என்ற சொல்லைப் பயன்படுத்தவில்லை.",
        "Dr. B.R. Ambedkar hoped that Article 356 would remain a 'dead letter' of the Constitution, to be used only in the rarest of rare cases.",
        "டாக்டர் பி.ஆர். அம்பேத்கர், சரத்து 356 அரசியலமைப்பின் ஒரு 'பயன்படுத்தப்படாத கடிதமாக' (dead letter) இருக்கும் என்றும், அரிதிலும் அரிதான சூழ்நிலைகளில் மட்டுமே பயன்படுத்தப்படும் என்றும் நம்பினார்."
    ))

    # 022 - Key B
    qs.append(make_ep_q(
        PREFIX, 22, DIFF, "Concept MCQ", "Article 365 Failure to Comply",
        "Under Article 365 of the Constitution, when a State fails to comply with or give effect to any direction given by the Union Government, what is the constitutional consequence?",
        "அரசியலமைப்பின் சரத்து 365-ன் கீழ், மத்திய அரசு வழங்கும் எந்தவொரு வழிகாட்டுதலையும் ஒரு மாநிலம் பின்பற்றத் தவறினால் அல்லது செயல்படுத்தத் தவறினால் ஏற்படும் அரசியலமைப்பு விளைவு என்ன?",
        "The State Chief Minister is immediately disqualified by the Election Commission", "மாநில முதலமைச்சர் உடனடியாக தேர்தல் ஆணையத்தால் தகுதி நீக்கம் செய்யப்படுவார்",
        "It shall be lawful for the President to hold that a situation has arisen in which the government of the State cannot be carried on in accordance with the Constitution (invoking Article 356)", "அந்த மாநில அரசு அரசியலமைப்பு விதிகளின்படி செயல்பட முடியாத சூழ்நிலை ஏற்பட்டுவிட்டதாகக் கருதி குடியரசுத் தலைவர் ஆட்சி (சரத்து 356) விதிக்க குடியரசுத் தலைவருக்கு சட்டப்பூர்வ உரிமை உண்டு",
        "The State's share of central tax devolution is permanently confiscated", "மாநிலத்திற்குரிய மத்திய வரிப் பகிர்வு நிரந்தரமாகப் பறிமுதல் செய்யப்படும்",
        "The State territory is automatically converted into a Union Territory", "மாநிலப் பகுதி தானாகவே ஒரு யூனியன் பிரதேசமாக மாற்றப்படும்",
        "B",
        "Article 365 provides that where any State has failed to comply with, or give effect to, any directions given in the exercise of the executive power of the Union, it shall be lawful for the President to hold that a situation has arisen in which the government of the State cannot be carried on in accordance with the provisions of this Constitution (triggering Article 356).",
        "சரத்து 365-ன் படி, மத்திய அரசின் நிர்வாக அதிகாரத்தின் கீழ் வழங்கப்படும் எந்தவொரு வழிகாட்டுதலையும் ஒரு மாநிலம் செயல்படுத்தத் தவறினால், அந்த மாநிலத்தின் அரசு அரசியலமைப்பு விதிகளின்படி செயல்பட முடியாத நிலை ஏற்பட்டுவிட்டதாகக் கருதி குடியரசுத் தலைவர் ஆட்சி விதிக்க குடியரசுத் தலைவருக்கு சட்டப்பூர்வ உரிமை உண்டு.",
        "Option A is incorrect; Election Commission has no role in executive compliance.", "விருப்பம் A தவறானது; இதில் தேர்தல் ஆணையத்திற்குப் பங்கு இல்லை.",
        "Option B is the exact textual effect of Article 365.", "விருப்பம் B என்பது சரத்து 365-ன் துல்லியமான நேரடி வாசகமாகும்.",
        "Option C is incorrect; tax devolution is governed by Finance Commission formulas.", "விருப்பம் C தவறானது; வரிப் பகிர்வு நிதி ஆணையத்தால் நிர்வகிக்கப்படுகிறது.",
        "Option D is incorrect; altering state boundaries requires an Act under Article 3.", "விருப்பம் D தவறானது; எல்லைகளை மாற்ற சரத்து 3-ன் கீழ் சட்டம் தேவை.",
        "President's Rule can be imposed under TWO articles: Article 356 (Failure of constitutional machinery in the state) AND Article 365 (Failure to comply with Union directions).",
        "குடியரசுத் தலைவர் ஆட்சியை இரண்டு சரத்துகளின் கீழ் விதிக்கலாம்: சரத்து 356 (மாநிலத்தில் அரசியலமைப்பு இயந்திரம் செயலிழப்பு) மற்றும் சரத்து 365 (மத்திய அரசின் வழிகாட்டுதல்களைப் பின்பற்றத் தவறுதல்).",
        "Article 365 acts as a federal sanction to compel State obedience to lawful Union executive directions issued under Articles 256 and 257.",
        "சரத்துகள் 256 மற்றும் 257-ன் கீழ் வழங்கப்படும் சட்டப்பூர்வ மத்திய வழிகாட்டுதல்களுக்கு மாநிலங்கள் அடிபணிவதை உறுதி செய்யும் கூட்டாட்சித் தடையணையாக சரத்து 365 செயல்படுகிறது."
    ))

    # 023 - Key C
    qs.append(make_ep_q(
        PREFIX, 23, DIFF, "Concept MCQ", "President's Rule Approval Time",
        "Within what time limit must a proclamation imposing President's Rule in a State under Article 356 be approved by both Houses of Parliament?",
        "சரத்து 356-ன் கீழ் ஒரு மாநிலத்தில் குடியரசுத் தலைவர் ஆட்சியை விதிக்கும் பிரகடனம் பாராளுமன்றத்தின் இரு அவைகளாலும் எத்தனை காலத்திற்குள் அங்கீகரிக்கப்பட வேண்டும்?",
        "Within one month from the date of its issue", "அது வெளியிடப்பட்ட தேதியிலிருந்து ஒரு மாதத்திற்குள்",
        "Within six months from the date of its issue", "அது வெளியிடப்பட்ட தேதியிலிருந்து ஆறு மாதங்களுக்குள்",
        "Within two months from the date of its issue", "அது வெளியிடப்பட்ட தேதியிலிருந்து இரண்டு மாதங்களுக்குள்",
        "Within fourteen days from the date of its issue", "அது வெளியிடப்பட்ட தேதியிலிருந்து பதினான்கு நாட்களுக்குள்",
        "C",
        "Under Article 356(3), a proclamation imposing President's Rule must be approved by both Houses of Parliament within two months from the date of its issue.",
        "சரத்து 356(3)-ன் படி, குடியரசுத் தலைவர் ஆட்சியை விதிக்கும் பிரகடனம் வெளியிடப்பட்ட தேதியிலிருந்து இரண்டு மாதங்களுக்குள் பாராளுமன்றத்தின் இரு அவைகளாலும் அங்கீகரிக்கப்பட வேண்டும்.",
        "Option A is the approval period for National Emergency (Article 352).", "விருப்பம் A என்பது தேசிய அவசரநிலைக்கான (சரத்து 352) ஒப்புதல் காலம்.",
        "Option B is the duration of operation after approval.", "விருப்பம் B என்பது ஒப்புதலுக்குப் பிறகு செயல்படும் கால அளவு.",
        "Option C is correct; exactly two months under Article 356(3).", "விருப்பம் C சரியானது; சரத்து 356(3)-ன் கீழ் சரியாக இரண்டு மாதங்கள்.",
        "Option D is incorrect.", "விருப்பம் D தவறானது.",
        "Approval Window Comparison: Article 352 (National Emergency) = 1 Month; Article 356 (President's Rule) = 2 Months; Article 360 (Financial Emergency) = 2 Months.",
        "ஒப்புதல் கால ஒப்பீடு: சரத்து 352 (தேசிய அவசரநிலை) = 1 மாதம்; சரத்து 356 (குடியரசுத் தலைவர் ஆட்சி) = 2 மாதங்கள்; சரத்து 360 (நிதி அவசரநிலை) = 2 மாதங்கள்.",
        "If Lok Sabha is dissolved during these two months without approving, the proclamation survives for 30 days from the first sitting of the new Lok Sabha, provided Rajya Sabha approves it in the meantime.",
        "இந்த இரண்டு மாத காலத்திற்குள் ஒப்புதல் அளிக்காமல் மக்களவை கலைக்கப்பட்டால், மாநிலங்களவை ஒப்புதல் அளித்திருந்தால், புதிய மக்களவை கூடிய 30 நாட்கள் வரை பிரகடனம் நீடிக்கும்."
    ))

    # 024 - Key D
    qs.append(make_ep_q(
        PREFIX, 24, DIFF, "Concept MCQ", "President's Rule Majority",
        "What type of parliamentary majority is required to approve or extend President's Rule under Article 356?",
        "சரத்து 356-ன் கீழ் குடியரசுத் தலைவர் ஆட்சியை அங்கீகரிக்க அல்லது நீட்டிக்க என்ன வகையான பாராளுமன்றப் பெரும்பான்மை தேவைப்படுகிறது?",
        "Special majority of two-thirds of members present and voting", "வருகை தந்து வாக்களிக்கும் உறுப்பினர்களில் மூன்றில் இரண்டு பங்கு சிறப்புப் பெரும்பான்மை",
        "Absolute majority of the total membership of each House", "ஒவ்வொரு அவையின் மொத்த உறுப்பினர் எண்ணிக்கையில் முழுமையான பெரும்பான்மை",
        "Special majority with ratification by half of the States", "பாதி மாநிலங்களின் ஒப்புதலுடன் கூடிய சிறப்புப் பெரும்பான்மை",
        "Simple majority of members present and voting in each House", "ஒவ்வொரு அவையிலும் வருகை தந்து வாக்களிக்கும் உறுப்பினர்களின் எளிய பெரும்பான்மை",
        "D",
        "Every resolution approving the proclamation of President's Rule or its continuation can be passed by either House of Parliament only by a simple majority, that is, a majority of the members of that House present and voting.",
        "குடியரசுத் தலைவர் ஆட்சிப் பிரகடனத்தை அல்லது அதன் தொடர்ச்சியை அங்கீகரிக்கும் ஒவ்வொரு தீர்மானமும் பாராளுமன்றத்தின் இரு அவைகளிலும் எளிய பெரும்பான்மை (அவையில் வருகை தந்து வாக்களிக்கும் உறுப்பினர்களில் பெரும்பான்மை) மூலம் மட்டுமே நிறைவேற்றப்பட வேண்டும்.",
        "Option A applies to National Emergency under Article 352.", "விருப்பம் A சரத்து 352-ன் கீழான தேசிய அவசரநிலைக்குப் பொருந்தும்.",
        "Option B is incorrect.", "விருப்பம் B தவறானது.",
        "Option C applies to constitutional amendments affecting federal provisions.", "விருப்பம் C கூட்டாட்சித் திருத்தங்களுக்குப் பொருந்தும்.",
        "Option D is correct; President's Rule requires only a simple majority.", "விருப்பம் D சரியானது; குடியரசுத் தலைவர் ஆட்சிக்கு எளிய பெரும்பான்மையே போதுமானது.",
        "TNPSC Trap: Unlike National Emergency which requires a special majority, President's Rule requires only a SIMPLE majority!",
        "TNPSC பொறி: சிறப்புப் பெரும்பான்மை தேவைப்படும் தேசிய அவசரநிலை போலன்றி, குடியரசுத் தலைவர் ஆட்சிக்கு எளிய பெரும்பான்மை மட்டுமே தேவை!",
        "This lower threshold historically made it easier for ruling parties at the Centre to impose President's Rule on opposition-ruled States.",
        "இந்தக் குறைந்த பெரும்பான்மைத் தேவைதான், மத்தியில் ஆளும் கட்சிகள் எதிர்க்கட்சி ஆளும் மாநிலங்கள் மீது எளிதாக குடியரசுத் தலைவர் ஆட்சியைத் திணிக்க வரலாற்று ரீதியாக வழிவகுத்தது."
    ))

    # 025 - Key A
    qs.append(make_ep_q(
        PREFIX, 25, DIFF, "Concept MCQ", "President's Rule Maximum Duration",
        "Once approved by both Houses of Parliament, for how long does President's Rule operate, and what is its maximum permissible constitutional duration?",
        "பாராளுமன்றத்தின் இரு அவைகளாலும் அங்கீகரிக்கப்பட்ட பிறகு, குடியரசுத் தலைவர் ஆட்சி எவ்வளவு காலம் செயல்படும், மேலும் அதன் அதிகபட்ச அனுமதிக்கப்பட்ட அரசியலமைப்பு காலம் என்ன?",
        "Operates for 6 months at a time, up to a maximum constitutional limit of 3 years", "ஒரு நேரத்தில் 6 மாதங்கள் செயல்படும், அதிகபட்ச அரசியலமைப்பு வரம்பு 3 ஆண்டுகள் வரை",
        "Operates for 1 year at a time, up to a maximum constitutional limit of 5 years", "ஒரு நேரத்தில் 1 ஆண்டு செயல்படும், அதிகபட்ச அரசியலமைப்பு வரம்பு 5 ஆண்டுகள் வரை",
        "Operates for 3 months at a time, up to a maximum constitutional limit of 1 year", "ஒரு நேரத்தில் 3 மாதங்கள் செயல்படும், அதிகபட்ச அரசியலமைப்பு வரம்பு 1 ஆண்டு வரை",
        "Operates indefinitely without any maximum ceiling", "எந்தவொரு அதிகபட்ச வரம்பும் இன்றி காலவரையின்றி செயல்படும்",
        "A",
        "Under Article 356(4), once approved, President's Rule continues for 6 months. It can be extended for a maximum period of 3 years with the approval of Parliament, every 6 months.",
        "சரத்து 356(4)-ன் படி, ஒப்புதல் அளிக்கப்பட்டதும் குடியரசுத் தலைவர் ஆட்சி 6 மாதங்களுக்கு நீடிக்கும். ஒவ்வொரு 6 மாதங்களுக்கும் பாராளுமன்ற ஒப்புதலுடன் அதிகபட்சமாக 3 ஆண்டுகள் வரை இதை நீட்டிக்க முடியும்.",
        "Option A is the exact constitutional formulation under Article 356(4).", "விருப்பம் A என்பது சரத்து 356(4)-ன் கீழான சரியான அரசியலமைப்பு விதியாகும்.",
        "Option B is incorrect.", "விருப்பம் B தவறானது.",
        "Option C is incorrect.", "விருப்பம் C தவறானது.",
        "Option D describes National Emergency under Article 352, which has no maximum upper limit.", "விருப்பம் D சரத்து 352-ன் கீழான தேசிய அவசரநிலையை விவரிக்கிறது, அதற்கு அதிகபட்ச வரம்பு இல்லை.",
        "Duration Comparison: National Emergency (Art 352) = 6 months at a time, NO upper limit. President's Rule (Art 356) = 6 months at a time, MAXIMUM 3 YEARS.",
        "கால அளவு ஒப்பீடு: தேசிய அவசரநிலை (352) = ஒரு நேரத்தில் 6 மாதங்கள், அதிகபட்ச வரம்பு இல்லை. குடியரசுத் தலைவர் ஆட்சி (356) = ஒரு நேரத்தில் 6 மாதங்கள், அதிகபட்சம் 3 ஆண்டுகள்.",
        "Punjab was a historic exception where President's Rule was extended beyond 3 years up to 5 years through specific constitutional amendments (64th, 67th, 68th CAA).",
        "பஞ்சாப் ஒரு வரலாற்று விதிவிலக்காகும்; அங்கு குறிப்பிட்ட அரசியலமைப்பு திருத்தங்கள் மூலம் குடியரசுத் தலைவர் ஆட்சி 3 ஆண்டுகளுக்கு மேல் 5 ஆண்டுகள் வரை நீட்டிக்கப்பட்டது."
    ))

    return qs

def get_easy_questions_part2():
    qs = []

    # 026 - Key B
    qs.append(make_ep_q(
        PREFIX, 26, DIFF, "Concept MCQ", "Article 356(5) Conditions",
        "Under Article 356(5) introduced by the 44th Amendment Act, 1978, beyond what duration can President's Rule be extended only if two strict constitutional conditions are met?",
        "1978-ஆம் ஆண்டின் 44-வது திருத்தச் சட்டத்தால் சேர்க்கப்பட்ட சரத்து 356(5)-ன் கீழ், எந்த காலத்திற்கு மேல் குடியரசுத் தலைவர் ஆட்சியை நீட்டிக்க வேண்டுமானால் இரண்டு கடுமையான அரசியலமைப்பு நிபந்தனைகள் பூர்த்தியாக வேண்டும்?",
        "Beyond six months", "ஆறு மாதங்களுக்கு மேல்",
        "Beyond one year", "ஒரு ஆண்டிற்கு மேல்",
        "Beyond two years", "இரண்டு ஆண்டுகளுக்கு மேல்",
        "Beyond eighteen months", "பதினெட்டு மாதங்களுக்கு மேல்",
        "B",
        "The 44th Amendment Act, 1978 introduced Article 356(5) to curb misuse: President's Rule can be extended beyond one year (up to the 3-year maximum) ONLY if two conditions exist: 1. A National Emergency is in operation in whole or part of India; and 2. Election Commission certifies that general elections to the Legislative Assembly cannot be held.",
        "துஷ்பிரயோகத்தைத் தடுப்பதற்காக 44-வது திருத்தச் சட்டம் 1978 சரத்து 356(5)-ஐ அறிமுகப்படுத்தியது: இரண்டு நிபந்தனைகள் பூர்த்தியானால் மட்டுமே குடியரசுத் தலைவர் ஆட்சியை ஒரு ஆண்டிற்கு மேல் (3 ஆண்டுகள் வரை) நீட்டிக்க முடியும்: 1. இந்தியா முழுவதும் அல்லது ஏதேனும் ஒரு பகுதியில் தேசிய அவசரநிலை அமலில் இருக்க வேண்டும்; 2. சட்டமன்றப் பொதுத்தேர்தலை நடத்துவதில் சிரமங்கள் இருப்பதாக தேர்தல் ஆணையம் சான்றளிக்க வேண்டும்.",
        "Option A is incorrect; 6 months is the standard renewal period.", "விருப்பம் A தவறானது; 6 மாதங்கள் என்பது சாதாரண புதுப்பித்தல் காலம்.",
        "Option B is correct; beyond 1 year requires the Article 356(5) double conditions.", "விருப்பம் B சரியானது; 1 ஆண்டிற்கு மேல் நீட்டிக்க சரத்து 356(5)-ன் இரட்டை நிபந்தனைகள் தேவை.",
        "Option C is incorrect.", "விருப்பம் C தவறானது.",
        "Option D is incorrect.", "விருப்பம் D தவறானது.",
        "Beyond 1 Year Rule (Art 356(5)): 1. National Emergency in operation + 2. Election Commission certificate that assembly election cannot be held.",
        "1 ஆண்டிற்கு மேற்பட்ட விதி (சரத்து 356(5)): 1. தேசிய அவசரநிலை அமலில் இருக்க வேண்டும் + 2. சட்டமன்றத் தேர்தல் நடத்த முடியாது என தேர்தல் ஆணைய சான்றிதழ்.",
        "This ensures that President's Rule cannot be casually continued for 3 years without democratic elections.",
        "இது ஜனநாயகத் தேர்தல்கள் இல்லாமல் குடியரசுத் தலைவர் ஆட்சியை சாதாரணமாக 3 ஆண்டுகளுக்குத் தொடர முடியாது என்பதை உறுதி செய்கிறது."
    ))

    # 027 - Key C
    qs.append(make_ep_q(
        PREFIX, 27, DIFF, "Concept MCQ", "Executive Dismissal in State",
        "When President's Rule is imposed in a State under Article 356, what happens to the State Council of Ministers headed by the Chief Minister?",
        "சரத்து 356-ன் கீழ் ஒரு மாநிலத்தில் குடியரசுத் தலைவர் ஆட்சி விதிக்கப்படும் போது, முதலமைச்சர் தலைமையிலான மாநில அமைச்சரவைக்கு என்ன நிகழ்கிறது?",
        "The Council of Ministers continues to function under central supervision", "அமைச்சரவை மத்திய மேற்பார்வையில் தொடர்ந்து செயல்படுகிறது",
        "The Council of Ministers is temporarily transferred to the neighboring State", "அமைச்சரவை தற்காலிகமாக அண்டை மாநிலத்திற்கு மாற்றப்படுகிறது",
        "The Council of Ministers is dismissed by the President, and the Governor administers the State with the help of advisors", "அமைச்சரவை குடியரசுத் தலைவரால் பதவி நீக்கம் செய்யப்படுகிறது, மேலும் ஆளுநர் ஆலோசகர்களின் உதவியுடன் மாநிலத்தை நிர்வகிக்கிறார்",
        "The Chief Minister is appointed as the acting Chief Justice of the State High Court", "முதலமைச்சர் மாநில உயர் நீதிமன்றத்தின் தற்காலிக தலைமை நீதிபதியாக நியமிக்கப்படுகிறார்",
        "C",
        "Upon imposition of President's Rule under Article 356, the President dismisses the State Council of Ministers headed by the Chief Minister. The State Governor, on behalf of the President, carries on the administration of the State with the help of the Chief Secretary or advisors appointed by the President.",
        "சரத்து 356-ன் கீழ் குடியரசுத் தலைவர் ஆட்சி விதிக்கப்பட்டவுடன், முதலமைச்சர் தலைமையிலான மாநில அமைச்சரவையை குடியரசுத் தலைவர் பதவி நீக்கம் செய்கிறார். குடியரசுத் தலைவரின் சார்பில் மாநில ஆளுநர், தலைமைச் செயலாளர் அல்லது குடியரசுத் தலைவரால் நியமிக்கப்படும் ஆலோசகர்களின் உதவியுடன் மாநில நிர்வாகத்தை மேற்கொள்கிறார்.",
        "Option A describes National Emergency (Article 352), not President's Rule.", "விருப்பம் A தேசிய அவசரநிலையை விவரிக்கிறது.",
        "Option B is absurd.", "விருப்பம் B தவறானது.",
        "Option C is the exact constitutional and administrative consequence under Article 356.", "விருப்பம் C என்பது சரத்து 356-ன் கீழான துல்லியமான அரசியலமைப்பு மற்றும் நிர்வாக விளைவாகும்.",
        "Option D is unconstitutional.", "விருப்பம் D அரசியலமைப்பிற்கு முரணானது.",
        "National Emergency = State Government is NOT dismissed (governs under central direction). President's Rule = State Government IS dismissed (Governor rules).",
        "தேசிய அவசரநிலை = மாநில அரசு கலைக்கப்படுவதில்லை (மத்திய வழிகாட்டுதலில் இயங்குகிறது). குடியரசுத் தலைவர் ஆட்சி = மாநில அரசு கலைக்கப்படுகிறது (ஆளுநர் ஆட்சி செய்கிறார்).",
        "This is why President's Rule is a direct suspension of democratic self-governance at the state level.",
        "இதனால்தான் குடியரசுத் தலைவர் ஆட்சி என்பது மாநில அளவில் ஜனநாயக சுயஆட்சியை நேரடியாக இடைநிறுத்துவதாகும்."
    ))

    # 028 - Key D
    qs.append(make_ep_q(
        PREFIX, 28, DIFF, "Concept MCQ", "State Assembly Status",
        "Regarding the State Legislative Assembly, what action does the President take upon issuing a proclamation under Article 356?",
        "மாநில சட்டமன்றப் பேரவை தொடர்பாக, சரத்து 356-ன் கீழ் பிரகடனம் வெளியிடும் போது குடியரசுத் தலைவர் என்ன நடவடிக்கை எடுக்கிறார்?",
        "The State Assembly must be permanently abolished immediately", "மாநில சட்டமன்றம் உடனடியாக நிரந்தரமாக ஒழிக்கப்பட வேண்டும்",
        "The State Assembly continues to pass binding statutes without any parliamentary oversight", "மாநில சட்டமன்றம் எந்தவொரு பாராளுமன்றக் கண்காணிப்பும் இன்றி தொடர்ந்து சட்டங்களை நிறைவேற்றுகிறது",
        "The State Assembly is merged into the Lok Sabha", "மாநில சட்டமன்றம் மக்களவையுடன் இணைக்கப்படுகிறது",
        "The State Assembly is either suspended or dissolved by the President", "மாநில சட்டமன்றம் குடியரசுத் தலைவரால் இடைநிறுத்தி வைக்கப்படுகிறது அல்லது கலைக்கப்படுகிறது",
        "D",
        "The President either suspends or dissolves the State Legislative Assembly. Under the landmark S.R. Bommai judgment (1994), the Assembly should not be dissolved until Parliament has approved the proclamation; till then, it can only be kept in suspended animation.",
        "குடியரசுத் தலைவர் மாநில சட்டமன்றப் பேரவையை இடைநிறுத்தி வைக்கிறார் அல்லது கலைக்கிறார். வரலாற்றுச் சிறப்புமிக்க எஸ்.ஆர். பொம்மை தீர்ப்பின்படி (1994), பாராளுமன்றம் பிரகடனத்தை அங்கீகரிக்கும் வரை சட்டமன்றத்தைக் கலைக்கக் கூடாது; அதுவரை அதை தற்காலிகமாக இடைநிறுத்தி மட்டுமே வைக்க முடியும்.",
        "Option A is incorrect; assemblies cannot be permanently abolished.", "விருப்பம் A தவறானது; சட்டமன்றங்களை நிரந்தரமாக ஒழிக்க முடியாது.",
        "Option B is incorrect; legislative powers shift to Parliament under Art 356(1)(b).", "விருப்பம் B தவறானது; சட்டமன்ற அதிகாரங்கள் பாராளுமன்றத்திற்கு மாறுகின்றன.",
        "Option C is incorrect.", "விருப்பம் C தவறானது.",
        "Option D is correct; the Assembly is suspended or dissolved.", "விருப்பம் D சரியானது; சட்டமன்றம் இடைநிறுத்தப்படுகிறது அல்லது கலைக்கப்படுகிறது.",
        "Bommai Rule: Assembly can only be kept in 'suspended animation' initially; dissolution can happen ONLY AFTER Parliament approves the proclamation under Art 356(3).",
        "பொம்மை விதி: ஆரம்பத்தில் சட்டமன்றத்தை 'இடைநிறுத்தி' மட்டுமே வைக்க முடியும்; பாராளுமன்றம் ஒப்புதல் அளித்த பிறகே கலைக்க முடியும்.",
        "If Parliament fails to approve the proclamation within 2 months, the dismissed government and suspended assembly are revived.",
        "பாராளுமன்றம் 2 மாதங்களுக்குள் பிரகடனத்திற்கு ஒப்புதல் அளிக்கத் தவறினால், பதவி நீக்கம் செய்யப்பட்ட அரசும் சட்டமன்றமும் மீண்டும் புத்துயிர் பெறும்."
    ))

    # 029 - Key A
    qs.append(make_ep_q(
        PREFIX, 29, DIFF, "Concept MCQ", "High Court Immunity",
        "Under the Proviso to Article 356(1), which constitutional institution's powers CANNOT be assumed by the President or suspended during President's Rule?",
        "சரத்து 356(1)-ன் வரம்புரையின் கீழ், குடியரசுத் தலைவர் ஆட்சியின் போது எந்த அரசியலமைப்பு அமைப்பின் அதிகாரங்களை குடியரசுத் தலைவர் ஏற்கவோ அல்லது இடைநிறுத்தவோ முடியாது?",
        "The High Court of the State", "மாநில உயர் நீதிமன்றம்",
        "The State Public Service Commission", "மாநில அரசுப் பணியாளர் தேர்வாணையம்",
        "The State Secretariat and Chief Secretary", "மாநிலச் செயலகம் மற்றும் தலைமைச் செயலாளர்",
        "The State Finance Commission", "மாநில நிதி ஆணையம்",
        "A",
        "The Proviso to Article 356(1) explicitly states that nothing in this clause shall authorize the President to assume to himself any of the powers vested in or exercisable by a High Court, or to suspend in whole or in part the operation of any provision of this Constitution relating to High Courts.",
        "சரத்து 356(1)-ன் வரம்புரை தெளிவாகக் கூறுகிறது: இந்த பிரிவில் உள்ள எதுவும் உயர் நீதிமன்றத்திற்கு வழங்கப்பட்டுள்ள எந்தவொரு அதிகாரத்தையும் குடியரசுத் தலைவர் தமதாக்கிக் கொள்ளவோ அல்லது உயர் நீதிமன்றங்கள் தொடர்பான அரசியலமைப்பு விதிகளை இடைநிறுத்தவோ அதிகாரம் அளிக்காது.",
        "Option A is correct; High Court powers are totally immune from presidential takeover under Article 356(1) Proviso.", "விருப்பம் A சரியானது; சரத்து 356(1) வரம்புரையின் கீழ் உயர் நீதிமன்ற அதிகாரங்கள் குடியரசுத் தலைவரால் பறிக்கப்பட முடியாது.",
        "Option B is not protected; functions can be taken over.", "விருப்பம் B பாதுகாக்கப்படவில்லை.",
        "Option C is taken over by the Governor/President.", "விருப்பம் C ஆளுநர்/குடியரசுத் தலைவரால் ஏற்கப்படுகிறது.",
        "Option D is not immune.", "விருப்பம் D பாதுகாக்கப்படவில்லை.",
        "TNPSC Favorite: The constitutional position, powers, and jurisdiction of the State High Court remain completely intact during President's Rule.",
        "TNPSC முக்கிய கேள்வி: குடியரசுத் தலைவர் ஆட்சியின் போது மாநில உயர் நீதிமன்றத்தின் அரசியலமைப்பு அந்தஸ்து, அதிகாரங்கள் மற்றும் அதிகார வரம்பு முழுமையாகப் பாதுகாக்கப்படுகின்றன.",
        "This ensures that citizens can still challenge arbitrary state actions under Article 226 before the High Court even during President's Rule.",
        "குடியரசுத் தலைவர் ஆட்சியின் போது கூட குடிமக்கள் சரத்து 226-ன் கீழ் உயர் நீதிமன்றத்தில் அத்துமீறல்களுக்கு எதிராக வழக்குத் தொடர முடியும் என்பதை இது உறுதி செய்கிறது."
    ))

    # 030 - Key B
    qs.append(make_ep_q(
        PREFIX, 30, DIFF, "Concept MCQ", "Article 357 Legislative Powers",
        "Under Article 357(1)(a), when the powers of the State Legislature have been declared to be exercisable by or under the authority of Parliament, Parliament is competent to:",
        "சரத்து 357(1)(a)-ன் கீழ், மாநில சட்டமன்றத்தின் அதிகாரங்கள் பாராளுமன்றத்தின் அதிகாரத்தால் பயன்படுத்தப்பட வேண்டும் என்று அறிவிக்கப்படும் போது, பாராளுமன்றத்திற்கு என்ன அதிகாரம் உள்ளது?",
        "Abolish the State permanently and divide its assets among neighboring countries", "மாநிலத்தை நிரந்தரமாக ஒழித்து அதன் சொத்துக்களை அண்டை நாடுகளுக்குப் பகிர்ந்தளித்தல்",
        "Confer on the President the power of the Legislature of the State to make laws (Delegated Legislation)", "சட்டங்களை இயற்ற மாநில சட்டமன்றத்திற்குரிய அதிகாரத்தை குடியரசுத் தலைவருக்கு வழங்குதல் (அதிகாரப் பகிர்வு)",
        "Direct the Governor to hold elections within 48 hours", "48 மணி நேரத்திற்குள் தேர்தல் நடத்த ஆளுநருக்கு உத்தரவிடுதல்",
        "Abolish all local panchayats and municipal bodies in that State", "அந்த மாநிலத்தில் உள்ள அனைத்து கிராம பஞ்சாயத்துகள் மற்றும் நகராட்சி அமைப்புகளை ஒழித்தல்",
        "B",
        "Under Article 357(1)(a), it shall be competent for Parliament to confer on the President the power of the Legislature of the State to make laws, and to authorize the President to delegate such power to any other authority specified by him.",
        "சரத்து 357(1)(a)-ன் படி, மாநில சட்டமன்றத்திற்குரிய சட்டம் இயற்றும் அதிகாரத்தை குடியரசுத் தலைவருக்கு வழங்கவும், அந்த அதிகாரத்தை தாம் குறிப்பிடும் வேறு எந்த அதிகார அமைப்பிற்கும் வழங்க குடியரசுத் தலைவருக்கு அதிகாரம் அளிக்கவும் பாராளுமன்றத்திற்கு அதிகாரம் உண்டு.",
        "Option A is unconstitutional.", "விருப்பம் A அரசியலமைப்பிற்கு முரணானது.",
        "Option B is the exact statutory delegation mechanism under Article 357(1)(a).", "விருப்பம் B என்பது சரத்து 357(1)(a)-ன் கீழான துல்லியமான சட்டவாக்க பகிர்வு முறைமை ஆகும்.",
        "Option C is incorrect; Election Commission decides poll dates.", "விருப்பம் C தவறானது; தேர்தல் ஆணையமே தேர்தல் தேதியைத் தீர்மானிக்கிறது.",
        "Option D is incorrect; local bodies are not automatically abolished.", "விருப்பம் D தவறானது.",
        "Laws made by the President (or Parliament) for the State during President's Rule are called 'President's Acts'.",
        "குடியரசுத் தலைவர் ஆட்சியின் போது மாநிலத்திற்காக குடியரசுத் தலைவரால் (அல்லது பாராளுமன்றத்தால்) இயற்றப்படும் சட்டங்கள் 'குடியரசுத் தலைவரின் சட்டங்கள்' (President's Acts) என அழைக்கப்படுகின்றன.",
        "Under the 44th CAA, these laws do NOT automatically expire after President's Rule ends; they continue in force until altered, repealed, or amended by the re-established State Legislature.",
        "44-வது திருத்தத்தின்படி, இந்தச் சட்டங்கள் குடியரசுத் தலைவர் ஆட்சி முடிந்தவுடன் தானாக காலாவதியாகாது; மீண்டும் அமையும் மாநில சட்டமன்றம் அவற்றை மாற்றும் வரை தொடர்ந்து அமலில் இருக்கும்."
    ))

    # 031 - Key C
    qs.append(make_ep_q(
        PREFIX, 31, DIFF, "Concept MCQ", "Financial Emergency Grounds",
        "Under Article 360 of the Constitution, on what ground can the President proclaim a Financial Emergency?",
        "அரசியலமைப்பின் சரத்து 360-ன் கீழ், எந்தக் காரணத்தின் அடிப்படையில் குடியரசுத் தலைவர் நிதி அவசரநிலையைப் பிரகடனம் செய்ய முடியும்?",
        "When the Union Government fails to pass the Annual Financial Statement (Budget)", "மத்திய அரசு வருடாந்திர நிதிநிலை அறிக்கையை (பட்ஜெட்) நிறைவேற்றத் தவறினால்",
        "When the currency value of the Rupee drops by more than 10% against the US Dollar", "அமெரிக்க டாலருக்கு நிகரான இந்திய ரூபாயின் மதிப்பு 10%-க்கு மேல் குறைந்தால்",
        "If the President is satisfied that a situation has arisen whereby the financial stability or credit of India or of any part of the territory thereof is threatened", "இந்தியாவின் அல்லது அதன் எல்லைக்குள் உள்ள ஏதேனும் ஒரு பகுதியின் நிதி நிலைத்தன்மை அல்லது கடன் நம்பகத்தன்மைக்கு அச்சுறுத்தல் ஏற்படும் சூழ்நிலை உருவாகியுள்ளதாக குடியரசுத் தலைவர் திருப்தியடைந்தால்",
        "Whenever the Reserve Bank of India reports an inflation rate exceeding 8%", "பணவீக்க விகிதம் 8%-க்கு மேல் இருப்பதாக இந்திய ரிசர்வ் வங்கி அறிக்கை அளிக்கும் போதெல்லாம்",
        "C",
        "Article 360(1) states that if the President is satisfied that a situation has arisen whereby the financial stability or credit of India or of any part of the territory thereof is threatened, he may by a proclamation make a declaration to that effect.",
        "சரத்து 360(1) கூறுகிறது: இந்தியாவின் அல்லது அதன் எந்தவொரு பகுதியின் நிதி நிலைத்தன்மை அல்லது கடன் நம்பகத்தன்மைக்கு அச்சுறுத்தல் ஏற்படும் சூழ்நிலை உருவாகியுள்ளதாக குடியரசுத் தலைவர் திருப்தியடைந்தால், அவர் நிதி அவசரநிலைப் பிரகடனத்தை வெளியிடலாம்.",
        "Option A leads to the fall of the government, not Financial Emergency.", "விருப்பம் A அரசு கவிழ வழிவகுக்கும், நிதி அவசரநிலைக்கு அல்ல.",
        "Option B is a currency fluctuation handled by monetary policy.", "விருப்பம் B பணவியல் கொள்கையால் கையாளப்படும் நாணய ஏற்ற இறக்கம்.",
        "Option C is the exact constitutional text of Article 360(1).", "விருப்பம் C என்பது சரத்து 360(1)-ன் துல்லியமான அரசியலமைப்பு வாசகமாகும்.",
        "Option D is managed by the RBI's Monetary Policy Committee.", "விருப்பம் D ரிசர்வ் வங்கியின் பணவியல் கொள்கைக் குழுவால் நிர்வகிக்கப்படுகிறது.",
        "Ground for Financial Emergency: Threat to the financial stability or credit of India or any part of its territory.",
        "நிதி அவசரநிலைக்கான காரணம்: இந்தியாவின் அல்லது அதன் ஏதேனும் ஒரு பகுதியின் நிதி நிலைத்தன்மை அல்லது கடன் நம்பகத்தன்மைக்கு அச்சுறுத்தல்.",
        "Like Article 352, a Financial Emergency can be declared for the whole of India or any specific part of it (added by 42nd Amendment, 1976).",
        "சரத்து 352 போலவே, நிதி அவசரநிலையையும் இந்தியா முழுமைக்கும் அல்லது அதன் குறிப்பிட்ட பகுதிக்கும் அறிவிக்க முடியும் (42-வது திருத்தம் 1976 மூலம் சேர்க்கப்பட்டது)."
    ))

    # 032 - Key D
    qs.append(make_ep_q(
        PREFIX, 32, DIFF, "Concept MCQ", "Financial Emergency Approval",
        "Within what time limit must a proclamation of Financial Emergency under Article 360 be approved by both Houses of Parliament, and by what majority?",
        "சரத்து 360-ன் கீழான நிதி அவசரநிலைப் பிரகடனம் பாராளுமன்றத்தின் இரு அவைகளாலும் எத்தனை காலத்திற்குள் மற்றும் என்ன பெரும்பான்மையால் அங்கீகரிக்கப்பட வேண்டும்?",
        "Within one month by a special majority", "ஒரு மாதத்திற்குள் சிறப்புப் பெரும்பான்மையால்",
        "Within six months by an absolute majority", "ஆறு மாதங்களுக்குள் முழுமையான பெரும்பான்மையால்",
        "Within fourteen days by a two-thirds majority", "பதினான்கு நாட்களுக்குள் மூன்றில் இரண்டு பங்கு பெரும்பான்மையால்",
        "Within two months by a simple majority", "இரண்டு மாதங்களுக்குள் எளிய பெரும்பான்மையால்",
        "D",
        "Under Article 360(2), a proclamation of Financial Emergency must be approved by both Houses of Parliament within two months from the date of its issue, by a simple majority of members present and voting.",
        "சரத்து 360(2)-ன் படி, நிதி அவசரநிலைப் பிரகடனம் வெளியிடப்பட்ட தேதியிலிருந்து இரண்டு மாதங்களுக்குள் பாராளுமன்றத்தின் இரு அவைகளாலும் வருகை தந்து வாக்களிக்கும் உறுப்பினர்களின் எளிய பெரும்பான்மை மூலம் அங்கீகரிக்கப்பட வேண்டும்.",
        "Option A describes National Emergency (Article 352).", "விருப்பம் A தேசிய அவசரநிலையை (சரத்து 352) விவரிக்கிறது.",
        "Option B is incorrect.", "விருப்பம் B தவறானது.",
        "Option C is incorrect.", "விருப்பம் C தவறானது.",
        "Option D is the exact constitutional rule under Article 360(2).", "விருப்பம் D என்பது சரத்து 360(2)-ன் கீழான துல்லியமான விதி ஆகும்.",
        "Approval Window: National Emergency = 1 Month (Special Majority). Financial Emergency = 2 Months (Simple Majority).",
        "ஒப்புதல் காலம்: தேசிய அவசரநிலை = 1 மாதம் (சிறப்புப் பெரும்பான்மை). நிதி அவசரநிலை = 2 மாதங்கள் (எளிய பெரும்பான்மை).",
        "If Lok Sabha is dissolved during these two months, the proclamation continues for 30 days from the reconstitution of Lok Sabha, provided Rajya Sabha approved it.",
        "இந்த இரண்டு மாத காலத்தில் மக்களவை கலைக்கப்பட்டால், மாநிலங்களவை ஒப்புதல் அளித்திருந்தால், புதிய மக்களவை கூடிய 30 நாட்கள் வரை பிரகடனம் நீடிக்கும்."
    ))

    # 033 - Key A
    qs.append(make_ep_q(
        PREFIX, 33, DIFF, "Concept MCQ", "Financial Emergency Duration",
        "Once approved by both Houses of Parliament, how long does a Financial Emergency under Article 360 continue in force?",
        "பாராளுமன்றத்தின் இரு அவைகளாலும் அங்கீகரிக்கப்பட்ட பிறகு, சரத்து 360-ன் கீழான நிதி அவசரநிலை எவ்வளவு காலம் அமலில் இருக்கும்?",
        "It continues indefinitely until it is revoked by the President (no repeated parliamentary approval required)", "குடியரசுத் தலைவரால் ரத்து செய்யப்படும் வரை அது காலவரையின்றி தொடர்கிறது (மீண்டும் மீண்டும் பாராளுமன்ற ஒப்புதல் தேவையில்லை)",
        "For a maximum period of three years only", "அதிகபட்சமாக மூன்று ஆண்டுகள் மட்டுமே",
        "For exactly six months and then automatically lapses", "சரியாக ஆறு மாதங்கள் மட்டுமே, பின்னர் தானாகவே காலாவதியாகிவிடும்",
        "For one year, extendable up to a maximum of two years", "ஒரு ஆண்டுக்கு மட்டுமே, அதிகபட்சமாக இரண்டு ஆண்டுகள் வரை நீட்டிக்கப்படலாம்",
        "A",
        "Once approved by Parliament, a Financial Emergency continues indefinitely until it is revoked by the President. Unlike National Emergency and President's Rule, there is NO requirement for repeated parliamentary approval every six months, and there is NO maximum ceiling.",
        "பாராளுமன்றம் ஒப்புதல் அளித்தவுடன், குடியரசுத் தலைவரால் ரத்து செய்யப்படும் வரை நிதி அவசரநிலை காலவரையின்றி தொடர்கிறது. தேசிய அவசரநிலை மற்றும் குடியரசுத் தலைவர் ஆட்சி போலன்றி, இதற்கு ஒவ்வொரு ஆறு மாதங்களுக்கும் மீண்டும் பாராளுமன்ற ஒப்புதல் பெற வேண்டிய தேவையும் இல்லை, அதிகபட்ச வரம்பும் இல்லை.",
        "Option A is correct; once approved, it continues indefinitely until revoked.", "விருப்பம் A சரியானது; ஒப்புதல் அளிக்கப்பட்டதும் ரத்து செய்யப்படும் வரை காலவரையின்றி நீடிக்கும்.",
        "Option B describes the maximum limit for President's Rule (Article 356).", "விருப்பம் B குடியரசுத் தலைவர் ஆட்சிக்கான அதிகபட்ச வரம்பை விவரிக்கிறது.",
        "Option C describes the 6-month periodic cycle of Arts 352 and 356.", "விருப்பம் C சரத்துகள் 352 மற்றும் 356-ன் 6 மாத காலமுறை சுழற்சியை விவரிக்கிறது.",
        "Option D is incorrect.", "விருப்பம் D தவறானது.",
        "High-Yield Distinction: Financial Emergency (Art 360) requires NO periodic parliamentary renewal once approved! It continues until the President revokes it.",
        "முக்கிய வேறுபாடு: நிதி அவசரநிலைக்கு (360) ஒருமுறை ஒப்புதல் அளித்த பிறகு காலமுறை பாராளுமன்றப் புதுப்பித்தல் தேவையில்லை! குடியரசுத் தலைவர் ரத்து செய்யும் வரை அது நீடிக்கும்.",
        "Revocation of Financial Emergency, like National Emergency, can be done by the President at any time without parliamentary approval.",
        "நிதி அவசரநிலையை ரத்து செய்வதும், தேசிய அவசரநிலை போலவே, பாராளுமன்ற ஒப்புதலின்றி குடியரசுத் தலைவரால் எப்போது வேண்டுமானாலும் செய்யப்படலாம்."
    ))

    # 034 - Key B
    qs.append(make_ep_q(
        PREFIX, 34, DIFF, "Concept MCQ", "Salary Cuts Under Art 360",
        "During a Financial Emergency under Article 360, the President is empowered to issue directions for the reduction of salaries and allowances of which of the following categories of persons?",
        "சரத்து 360-ன் கீழான நிதி அவசரநிலையின் போது, பின்வரும் எந்தப் பிரிவினரின் சம்பளம் மற்றும் படிகளைக் குறைப்பதற்கான வழிகாட்டுதல்களை வழங்க குடியரசுத் தலைவருக்கு அதிகாரம் உண்டு?",
        "Only contractual private sector workers", "ஒப்பந்த அடிப்படையிலான தனியார் துறை ஊழியர்கள் மட்டுமே",
        "All persons serving in connection with the affairs of the Union or a State, including the Judges of the Supreme Court and High Courts", "உச்ச நீதிமன்ற மற்றும் உயர் நீதிமன்ற நீதிபதிகள் உட்பட மத்திய அல்லது மாநிலப் பணிகளில் பணியாற்றும் அனைத்து நபர்கள்",
        "Only the Members of the Legislative Assemblies of States", "மாநில சட்டமன்றப் பேரவைகளின் உறுப்பினர்கள் மட்டுமே",
        "Only non-gazetted municipal officers", "கெசட் பதிவு பெறாத நகராட்சி அதிகாரிகள் மட்டுமே",
        "B",
        "Under Article 360(4)(a) and (b), the executive directions of the Union may include: 1. Reduction of salaries and allowances of all or any class of persons serving in connection with the affairs of the State; and 2. Reduction of salaries and allowances of all or any class of persons serving the Union, INCLUDING the Judges of the Supreme Court and the High Courts.",
        "சரத்து 360(4)(a) மற்றும் (b)-ன் கீழ், மத்திய அரசின் வழிகாட்டுதல்களில்: 1. மாநிலப் பணிகளில் உள்ள அனைத்து அல்லது குறிப்பிட்ட வகுப்பினரின் சம்பளம் மற்றும் படிகளைக் குறைத்தல்; 2. உச்ச நீதிமன்றம் மற்றும் உயர் நீதிமன்ற நீதிபதிகள் உட்பட மத்தியப் பணிகளில் உள்ள அனைவரின் சம்பளம் மற்றும் படிகளைக் குறைத்தல் ஆகியவை அடங்கும்.",
        "Option A is incorrect; private sector is not covered.", "விருப்பம் A தவறானது; தனியார் துறை இதில் வராது.",
        "Option B is the exact constitutional provision under Article 360(4).", "விருப்பம் B என்பது சரத்து 360(4)-ன் கீழான சரியான அரசியலமைப்பு விதி ஆகும்.",
        "Option C is too narrow.", "விருப்பம் C மிகவும் குறுகியது.",
        "Option D is incorrect.", "விருப்பம் D தவறானது.",
        "TNPSC Classic Trap: Judicial salaries of Supreme Court and High Court judges CANNOT be reduced in normal times (Art 125/221), but CAN be reduced during FINANCIAL EMERGENCY under Article 360(4)(b)!",
        "TNPSC முக்கிய பொறி: சாதாரண காலங்களில் உச்ச நீதிமன்ற, உயர் நீதிமன்ற நீதிபதிகளின் சம்பளத்தைக் குறைக்க முடியாது; ஆனால் சரத்து 360-ன் கீழான நிதி அவசரநிலையின் போது குறைக்க முடியும்!",
        "Additionally, all Money Bills and other financial bills passed by State Legislatures can be reserved for the consideration of the President during Financial Emergency.",
        "கூடுதலாக, நிதி அவசரநிலையின் போது மாநில சட்டமன்றங்கள் நிறைவேற்றும் அனைத்து பண மசோதாக்களையும் குடியரசுத் தலைவரின் பரிசீலனைக்காக நிறுத்தி வைக்கலாம்."
    ))

    # 035 - Key C
    qs.append(make_ep_q(
        PREFIX, 35, DIFF, "Concept MCQ", "Financial Emergency Status in India",
        "How many times has a Financial Emergency under Article 360 been proclaimed in India since the commencement of the Constitution?",
        "அரசியலமைப்பு நடைமுறைக்கு வந்ததிலிருந்து இந்தியாவில் சரத்து 360-ன் கீழான நிதி அவசரநிலை எத்தனை முறை பிரகடனப்படுத்தப்பட்டுள்ளது?",
        "Once, during the 1991 Balance of Payments crisis", "ஒருமுறை, 1991 அந்நியச் செலாவணி இருப்பு நெருக்கடியின் போது",
        "Twice, in 1966 and 1991", "இரண்டு முறை, 1966 மற்றும் 1991-ல்",
        "Never (Zero times)", "ஒருமுறை கூட இல்லை (பூஜ்ஜியம் முறை)",
        "Thrice, coinciding with the three National Emergencies", "மூன்று முறை, மூன்று தேசிய அவசரநிலைகளுடன் இணைந்து",
        "C",
        "No Financial Emergency has ever been declared in India so far, though a severe financial crisis arose in 1991 (Balance of Payments crisis).",
        "1991-ல் கடுமையான நிதி நெருக்கடி (அந்நியச் செலாவணி இருப்பு நெருக்கடி) ஏற்பட்ட போதிலும், இந்தியாவில் இன்றுவரை ஒருமுறை கூட நிதி அவசரநிலை பிரகடனப்படுத்தப்படவில்லை.",
        "Option A is a common trap; the 1991 BoP crisis was resolved through economic reforms (LPG), without declaring Financial Emergency.", "விருப்பம் A பொதுவான பொறி; 1991 நெருக்கடி அவசரநிலையின்றி பொருளாதார சீர்திருத்தங்கள் (LPG) மூலம் தீர்க்கப்பட்டது.",
        "Option B is incorrect.", "விருப்பம் B தவறானது.",
        "Option C is correct; Financial Emergency has NEVER been proclaimed in India.", "விருப்பம் C சரியானது; இந்தியாவில் நிதி அவசரநிலை இதுவரை பிரகடனப்படுத்தப்பட்டதே இல்லை.",
        "Option D is incorrect.", "விருப்பம் D தவறானது.",
        "TNPSC Favorite Fact: Article 360 (Financial Emergency) has been invoked ZERO times in independent India.",
        "TNPSC முக்கிய உண்மை: சுதந்திர இந்தியாவில் சரத்து 360 (நிதி அவசரநிலை) இதுவரை ஒருமுறை கூட பயன்படுத்தப்படவில்லை.",
        "Even during the Covid-19 economic lockdown in 2020, Article 360 was not invoked; disaster management laws were used instead.",
        "2020 கோவிட்-19 பொதுமுடக்கத்தின் போது கூட சரத்து 360 பயன்படுத்தப்படவில்லை; பேரிடர் மேலாண்மைச் சட்டங்களே பயன்படுத்தப்பட்டன."
    ))

    # 036 - Key D
    qs.append(make_ep_q(
        PREFIX, 36, DIFF, "Concept MCQ", "First National Emergency",
        "When was the First National Emergency under Article 352 proclaimed in India, and what was the occasion?",
        "இந்தியாவில் சரத்து 352-ன் கீழான முதலாவது தேசிய அவசரநிலை எப்போது பிரகடனப்படுத்தப்பட்டது, அதற்கான காரணம் என்ன?",
        "December 1971, due to the Bangladesh Liberation War", "டிசம்பர் 1971, வங்கதேச விடுதலைப் போர் காரணமாக",
        "June 1975, due to internal political disturbance", "ஜூன் 1975, உள்நாட்டு அரசியல் அமைதியின்மை காரணமாக",
        "August 1947, due to the partition of India", "ஆகஸ்ட் 1947, இந்தியப் பிரிவினை காரணமாக",
        "October 1962, due to Chinese aggression in NEFA (Arunachal Pradesh)", "அக்டோபர் 1962, நெஃபா (அருணாச்சலப் பிரதேசம்) பகுதியில் சீன ஆக்கிரமிப்பு காரணமாக",
        "D",
        "The first proclamation of National Emergency was issued in October 1962 on account of Chinese aggression in the NEFA (North-East Frontier Agency, now Arunachal Pradesh), and remained in force until January 1968.",
        "முதலாவது தேசிய அவசரநிலைப் பிரகடனம் அக்டோபர் 1962-ல் நெஃபா (வடகிழக்கு எல்லைப்புற முகமை, தற்போதைய அருணாச்சலப் பிரதேசம்) மீதான சீன ஆக்கிரமிப்பு காரணமாக வெளியிடப்பட்டு, ஜனவரி 1968 வரை அமலில் இருந்தது.",
        "Option A was the Second National Emergency (December 1971).", "விருப்பம் A இரண்டாவது தேசிய அவசரநிலை (டிசம்பர் 1971).",
        "Option B was the Third National Emergency (June 1975).", "விருப்பம் B மூன்றாவது தேசிய அவசரநிலை (ஜூன் 1975).",
        "Option C predates the Constitution.", "விருப்பம் C அரசியலமைப்பிற்கு முந்தையது.",
        "Option D is correct; October 1962 Chinese aggression triggered the 1st National Emergency.", "விருப்பம் D சரியானது; அக்டோபர் 1962 சீன ஆக்கிரமிப்பு முதல் தேசிய அவசரநிலையைத் தூண்டியது.",
        "The 1962 Emergency also covered the 1965 war with Pakistan, before finally being revoked in January 1968.",
        "1962 அவசரநிலை 1965 இந்தியா-பாகிஸ்தான் போரையும் உள்ளடக்கியிருந்தது; இறுதியாக ஜனவரி 1968-ல் திரும்பப் பெறப்பட்டது.",
        "President Dr. S. Radhakrishnan issued the proclamation on the advice of Prime Minister Jawaharlal Nehru.",
        "பிரதமர் ஜவஹர்லால் நேருவின் ஆலோசனையின் பேரில் குடியரசுத் தலைவர் டாக்டர் எஸ். ராதாகிருஷ்ணன் இந்த பிரகடனத்தை வெளியிட்டார்."
    ))

    # 037 - Key A
    qs.append(make_ep_q(
        PREFIX, 37, DIFF, "Concept MCQ", "Second National Emergency",
        "The Second National Emergency under Article 352 was proclaimed in December 1971 in the wake of which major historical event?",
        "டிசம்பர் 1971-ல் சரத்து 352-ன் கீழான இரண்டாவது தேசிய அவசரநிலை எந்த முக்கிய வரலாற்று நிகழ்வைத் தொடர்ந்து பிரகடனப்படுத்தப்பட்டது?",
        "Indo-Pakistan War and the liberation of Bangladesh (External Aggression)", "இந்தியா-பாகிஸ்தான் போர் மற்றும் வங்கதேச விடுதலை (வெளிநாட்டு ஆக்கிரமிப்பு)",
        "Naxalbari peasant uprising in West Bengal", "மேற்கு வங்கத்தில் நக்சல்பாரி விவசாயிகளின் எழுச்சி",
        "Assam oil blockade agitation", "அசாம் எண்ணெய் முற்றுகைப் போராட்டம்",
        "Kargil conflict with Pakistani infiltrators", "பாகிஸ்தான் ஊடுருவல்காரர்களுடனான கார்கில் மோதல்",
        "A",
        "The Second National Emergency was declared on December 3, 1971 by President V.V. Giri following Pakistani air strikes and aggression, leading to the Indo-Pakistan war and the birth of Bangladesh.",
        "பாகிஸ்தானின் வான்வழித் தாக்குதல்கள் மற்றும் ஆக்கிரமிப்பைத் தொடர்ந்து, டிசம்பர் 3, 1971 அன்று குடியரசுத் தலைவர் வி.வி. கிரி இரண்டாவது தேசிய அவசரநிலையை அறிவித்தார்; இது இந்தியா-பாகிஸ்தான் போருக்கும் வங்கதேச உருவாக்கத்திற்கும் வழிவகுத்தது.",
        "Option A is correct; December 1971 Indo-Pak war was the reason.", "விருப்பம் A சரியானது; டிசம்பர் 1971 இந்தியா-பாகிஸ்தான் போரே இதற்குக் காரணம்.",
        "Option B is incorrect.", "விருப்பம் B தவறானது.",
        "Option C is incorrect.", "விருப்பம் C தவறானது.",
        "Option D took place in 1999, but no emergency was declared during Kargil.", "விருப்பம் D 1999-ல் நடந்தது, ஆனால் கார்கிலின் போது அவசரநிலை அறிவிக்கப்படவில்லை.",
        "Even while the December 1971 emergency was still active, a third emergency was superimposed on it in June 1975!",
        "டிசம்பர் 1971 அவசரநிலை அமலில் இருந்தபோதே, ஜூன் 1975-ல் அதன் மீது மூன்றாவது அவசரநிலை திணிக்கப்பட்டது!",
        "Both the 1971 and 1975 proclamations were revoked simultaneously in March 1977.",
        "1971 மற்றும் 1975 ஆகிய இரண்டு பிரகடனங்களும் மார்ச் 1977-ல் ஒரே நேரத்தில் திரும்பப் பெறப்பட்டன."
    ))

    # 038 - Key B
    qs.append(make_ep_q(
        PREFIX, 38, DIFF, "Concept MCQ", "Third National Emergency",
        "Who was the President of India who proclaimed the controversial Third National Emergency on June 25, 1975 on the ground of 'Internal Disturbance'?",
        "ஜூன் 25, 1975 அன்று 'உள்நாட்டு அமைதியின்மை' என்ற காரணத்தின் அடிப்படையில் சர்ச்சைக்குரிய மூன்றாவது தேசிய அவசரநிலையைப் பிரகடனப்படுத்திய இந்தியக் குடியரசுத் தலைவர் யார்?",
        "Dr. Zakir Husain", "டாக்டர் ஜாகிர் உசேன்",
        "Fakhruddin Ali Ahmed", "பக்ருதீன் அலி அகமது",
        "V.V. Giri", "வி.வி. கிரி",
        "Neelam Sanjiva Reddy", "நீலம் சஞ்சீவ ரெட்டி",
        "B",
        "President Fakhruddin Ali Ahmed issued the proclamation of the Third National Emergency on the night of June 25, 1975 on the sole advice of Prime Minister Indira Gandhi, without prior discussion in the Union Cabinet.",
        "மத்திய அமைச்சரவையில் முன்கூட்டியே விவாதிக்காமல், பிரதமர் இந்திரா காந்தியின் தனிப்பட்ட ஆலோசனையின் பேரில், குடியரசுத் தலைவர் பக்ருதீன் அலி அகமது ஜூன் 25, 1975 இரவில் மூன்றாவது தேசிய அவசரநிலைப் பிரகடனத்தை வெளியிட்டார்.",
        "Option A died in office in 1969.", "விருப்பம் A 1969-ல் பதவியில் இருக்கும்போதே காலமானார்.",
        "Option B is correct; Fakhruddin Ali Ahmed signed the 1975 proclamation.", "விருப்பம் B சரியானது; பக்ருதீன் அலி அகமது 1975 பிரகடனத்தில் கையெழுத்திட்டார்.",
        "Option C had demitted office in 1974.", "விருப்பம் C 1974-ல் பதவிக்காலம் முடிவடைந்தது.",
        "Option D became President later in 1977 under the Janata government.", "விருப்பம் D பின்னர் 1977-ல் ஜனதா ஆட்சியில் குடியரசுத் தலைவரானார்.",
        "President in 1962: Dr. S. Radhakrishnan; President in 1971: V.V. Giri; President in 1975: Fakhruddin Ali Ahmed.",
        "1962-ல் குடியரசுத் தலைவர்: டாக்டர் எஸ். ராதாகிருஷ்ணன்; 1971-ல்: வி.வி. கிரி; 1975-ல்: பக்ருதீன் அலி அகமது.",
        "This unilateral proclamation without Cabinet concurrence led directly to the insertion of Article 352(3) in the 44th Amendment Act, 1978.",
        "அமைச்சரவை ஒப்புதல் இன்றி தன்னிச்சையாக வெளியிடப்பட்ட இந்த பிரகடனமே 44-வது திருத்தத்தில் சரத்து 352(3) சேர்க்கப்பட நேரடிக் காரணமானது."
    ))

    # 039 - Key C
    qs.append(make_ep_q(
        PREFIX, 39, DIFF, "Concept MCQ", "Shah Commission",
        "Which commission was appointed by the Janata Party Government in May 1977 to inquire into the circumstances leading to the 1975 Emergency and the excesses committed during it?",
        "1975 அவசரநிலைக்கு வழிவகுத்த சூழ்நிலைகள் மற்றும் அதன் போது இழைக்கப்பட்ட அத்துமீறல்கள் குறித்து விசாரிக்க மே 1977-ல் ஜனதா அரசால் நியமிக்கப்பட்ட ஆணையம் எது?",
        "Sarkaria Commission", "சர்க்காரியா ஆணையம்",
        "Kothari Commission", "கோத்தாரி ஆணையம்",
        "Shah Commission", "ஷா ஆணையம்",
        "Thakkar Commission", "தக்கர் ஆணையம்",
        "C",
        "The Janata Party Government headed by Morarji Desai appointed the Shah Commission of Inquiry headed by former Chief Justice of India J.C. Shah in May 1977. Its findings paved the way for the 44th Constitutional Amendment Act, 1978.",
        "மொரார்ஜி தேசாய் தலைமையிலான ஜனதா அரசு மே 1977-ல் முன்னாள் தலைமை நீதிபதி ஜே.சி. ஷா தலைமையில் ஷா விசாரணை ஆணையத்தை அமைத்தது. இதன் கண்டுபிடிப்புகளே 44-வது அரசியலமைப்பு திருத்தச் சட்டம் 1978-க்கு வழிவகுத்தன.",
        "Option A was on Centre-State Relations (1983).", "விருப்பம் A மத்திய-மாநில உறவுகள் தொடர்பானது (1983).",
        "Option B was on Education Reforms (1964).", "விருப்பம் B கல்வி சீர்திருத்தங்கள் தொடர்பானது (1964).",
        "Option C is correct; Shah Commission investigated the 1975 Emergency excesses.", "விருப்பம் C சரியானது; ஷா ஆணையம் 1975 அவசரநிலை அத்துமீறல்களை விசாரித்தது.",
        "Option D was on the assassination of Indira Gandhi (1984).", "விருப்பம் D இந்திரா காந்தி படுகொலை தொடர்பானது (1984).",
        "Shah Commission (1977) = Investigated 1975 Emergency -> Led to 44th Amendment Act (1978).",
        "ஷா ஆணையம் (1977) = 1975 அவசரநிலையை விசாரித்தது -> 44-வது திருத்தச் சட்டத்திற்கு (1978) வழிவகுத்தது.",
        "The Shah Commission concluded that the declaration of emergency was not justified and was used to suppress political opponents and muzzle the press.",
        "அவசரநிலை அறிவிப்பு நியாயமற்றது என்றும், அரசியல் எதிரிகளை ஒடுக்கவும் பத்திரிகைகளை முடக்கவுமே பயன்படுத்தப்பட்டது என்றும் ஷா ஆணையம் முடிவுக்கு வந்தது."
    ))

    # 040 - Key D
    qs.append(make_ep_q(
        PREFIX, 40, DIFF, "Concept MCQ", "Minerva Mills Landmark",
        "In which landmark case (1980) did the Supreme Court hold that the proclamation of a National Emergency under Article 352 can be challenged in court on the grounds of mala fides or irrelevance?",
        "எந்த வரலாற்றுச் சிறப்புமிக்க வழக்கில் (1980), துர்நோக்கம் (Mala fides) அல்லது பொருத்தமற்ற காரணங்களின் அடிப்படையில் சரத்து 352-ன் கீழான தேசிய அவசரநிலைப் பிரகடனத்தை நீதிமன்றத்தில் சவால் செய்ய முடியும் என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது?",
        "Golak Nath v. State of Punjab", "கோலக் நாத் எதிர் பஞ்சாப் மாநிலம்",
        "Kesavananda Bharati v. State of Kerala", "கேசவாநந்த பாரதி எதிர் கேரள மாநிலம்",
        "Maneka Gandhi v. Union of India", "மேனகா காந்தி எதிர் இந்திய ஒன்றியம்",
        "Minerva Mills v. Union of India", "மினர்வா மில்ஸ் எதிர் இந்திய ஒன்றியம்",
        "D",
        "In Minerva Mills v. Union of India (1980), the Supreme Court observed that the proclamation of emergency under Article 352 is not immune from judicial review. It can be challenged if it is based on wholly extraneous or mala fide grounds.",
        "மினர்வா மில்ஸ் எதிர் இந்திய ஒன்றியம் (1980) வழக்கில், சரத்து 352-ன் கீழான அவசரநிலைப் பிரகடனம் நீதித்துறை மறுஆய்வுக்கு அப்பாற்பட்டது அல்ல என்றும், முற்றிலும் தொடர்பற்ற அல்லது துர்நோக்கமுள்ள காரணங்களின் அடிப்படையில் இருந்தால் அதை நீதிமன்றத்தில் சவால் செய்யலாம் என்றும் உச்ச நீதிமன்றம் குறிப்பிட்டது.",
        "Option A (1967) dealt with fundamental rights amendment limits.", "விருப்பம் A அடிப்படை உரிமைகள் திருத்த வரம்பு தொடர்பானது.",
        "Option B (1973) established the Basic Structure doctrine.", "விருப்பம் B அடிப்படைக் கட்டமைப்புக் கோட்பாட்டை நிறுவியது.",
        "Option C (1978) expanded Article 21 to include procedure established by law as fair, just, and reasonable.", "விருப்பம் C சரத்து 21-ஐ விரிவுபடுத்தியது.",
        "Option D is correct; Minerva Mills (1980) affirmed judicial review of emergency proclamations.", "விருப்பம் D சரியானது; மினர்வா மில்ஸ் (1980) அவசரநிலைப் பிரகடனத்தின் மீதான நீதித்துறை மறுஆய்வை உறுதி செய்தது.",
        "Minerva Mills (1980): Emergency proclamation CAN be challenged on grounds of mala fides or absurdity.",
        "மினர்வா மில்ஸ் (1980): துர்நோக்கம் அல்லது பொருத்தமற்ற காரணங்களின் அடிப்படையில் அவசரநிலைப் பிரகடனத்தை நீதிமன்றத்தில் சவால் செய்யலாம்.",
        "The 38th Amendment (1975) had made the President's satisfaction final and conclusive, but this bar was removed by the 44th Amendment (1978).",
        "38-வது திருத்தம் (1975) குடியரசுத் தலைவரின் முடிவை இறுதியானது என ஆக்கியிருந்தது, ஆனால் 44-வது திருத்தம் (1978) இந்தத் தடையை நீக்கியது."
    ))

    # 041 - Key A
    qs.append(make_ep_q(
        PREFIX, 41, DIFF, "Concept MCQ", "S.R. Bommai Landmark",
        "In the landmark nine-judge Constitution Bench decision in S.R. Bommai v. Union of India (1994), what major principle was laid down regarding the proclamation of President's Rule under Article 356?",
        "எஸ்.ஆர். பொம்மை எதிர் இந்திய ஒன்றியம் (1994) என்ற வரலாற்றுச் சிறப்புமிக்க 9 நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வுத் தீர்ப்பில், சரத்து 356-ன் கீழான குடியரசுத் தலைவர் ஆட்சிப் பிரகடனம் தொடர்பாக வகுக்கப்பட்ட முக்கியக் கொள்கை என்ன?",
        "The proclamation of President's Rule is subject to judicial review, and the court can revive a dismissed state government if the action was unconstitutional", "குடியரசுத் தலைவர் ஆட்சிப் பிரகடனம் நீதித்துறை மறுஆய்வுக்கு உட்பட்டது; அந்த நடவடிக்கை அரசியலமைப்பிற்கு முரணானது என்றால் பதவி நீக்கம் செய்யப்பட்ட மாநில அரசை நீதிமன்றம் மீண்டும் புத்துயிர் பெறச் செய்ய முடியும்",
        "The President's discretion under Article 356 is supreme and can never be questioned in any court", "சரத்து 356-ன் கீழான குடியரசுத் தலைவரின் விருப்ப அதிகாரம் முதன்மையானது, எந்த நீதிமன்றத்திலும் கேள்வி கேட்க முடியாது",
        "All States must have President's Rule every five years as a mandatory federal audit", "கட்டாயக் கூட்டாட்சித் தணிக்கையாக ஒவ்வொரு ஐந்து வருடங்களுக்கும் அனைத்து மாநிலங்களிலும் குடியரசுத் தலைவர் ஆட்சி விதிக்கப்பட வேண்டும்",
        "Only the Governor can dismiss the government, not the President", "குடியரசுத் தலைவர் அல்ல, ஆளுநர் மட்டுமே அரசாங்கத்தைப் பதவி நீக்கம் செய்ய முடியும்",
        "A",
        "In S.R. Bommai (1994), the 9-judge bench laid down that: 1. Article 356 proclamation is subject to judicial review; 2. Secularism is a basic feature of the Constitution; 3. If the court strikes down the proclamation, it can restore the dismissed government and revive the dissolved Assembly.",
        "எஸ்.ஆர். பொம்மை (1994) வழக்கில் 9 நீதிபதிகள் அமர்வு: 1. சரத்து 356 பிரகடனம் நீதித்துறை மறுஆய்வுக்கு உட்பட்டது; 2. மதச்சார்பின்மை அரசியலமைப்பின் அடிப்படைக் கட்டமைப்பு; 3. பிரகடனத்தை நீதிமன்றம் ரத்து செய்தால், பதவி நீக்கம் செய்யப்பட்ட அரசை மீட்டெடுக்கவும் கலைக்கப்பட்ட சட்டமன்றத்திற்கு மீண்டும் புத்துயிர் அளிக்கவும் நீதிமன்றத்திற்கு அதிகாரம் உண்டு என்று தீர்ப்பளித்தது.",
        "Option A is the historic holding of S.R. Bommai (1994).", "விருப்பம் A என்பது எஸ்.ஆர். பொம்மை (1994) வழக்கின் வரலாற்றுத் தீர்ப்பாகும்.",
        "Option B was the pre-Bommai executive stance, which was decisively rejected.", "விருப்பம் B பொம்மை வழக்கிற்கு முந்தைய நிலை, இது திட்டவட்டமாக நிராகரிக்கப்பட்டது.",
        "Option C is absurd.", "விருப்பம் C தவறானது.",
        "Option D is incorrect.", "விருப்பம் D தவறானது.",
        "Bommai Case (1994) = Article 356 subject to judicial review + Court can restore dismissed government + Floor test is mandatory.",
        "பொம்மை வழக்கு (1994) = சரத்து 356 நீதித்துறை மறுஆய்வுக்கு உட்பட்டது + கலைக்கப்பட்ட அரசை நீதிமன்றம் மீட்டெடுக்கலாம் + சட்டமன்றத்தில் பெரும்பான்மையை நிரூபிப்பது கட்டாயம்.",
        "The Bommai verdict drastically reduced the frivolous and partisan use of Article 356 by central governments.",
        "பொம்மை தீர்ப்பு மத்திய அரசுகள் சரத்து 356-ஐ அற்ப காரணங்களுக்காகவும் அரசியல் உள்நோக்கத்துடனும் பயன்படுத்துவதை பெருமளவில் கட்டுப்படுத்தியது."
    ))

    # 042 - Key B
    qs.append(make_ep_q(
        PREFIX, 42, DIFF, "Concept MCQ", "Floor Test Principle",
        "In S.R. Bommai v. Union of India (1994), what constitutional test was held to be the ONLY legitimate method to determine whether a Ministry has lost the confidence of the Legislative Assembly?",
        "எஸ்.ஆர். பொம்மை எதிர் இந்திய ஒன்றியம் (1994) வழக்கில், ஒரு அமைச்சரவை சட்டமன்றப் பேரவையின் நம்பிக்கையை இழந்துவிட்டதா என்பதைத் தீர்மானிப்பதற்கான ஒரே முறையான வழிமுறை எது என்று தீர்ப்பளிக்கப்பட்டது?",
        "The subjective personal impression of the Governor reported in a secret letter", "ரகசியக் கடிதத்தில் ஆளுநர் தெரிவிக்கும் தனது சொந்த தனிப்பட்ட கருத்து",
        "Floor test on the floor of the Legislative Assembly (Floor Test rule)", "சட்டமன்றப் பேரவையின் தளத்தில் நடத்தப்படும் வாக்கெடுப்பு (Floor Test விதி)",
        "Opinion poll conducted by independent public survey agencies", "சுயாதீன பொதுக் கருத்துக்கணிப்பு நிறுவனங்கள் நடத்தும் வாக்கெடுப்பு",
        "Resolution passed by the Rajya Sabha Committee on Petitions", "மனுக்களுக்கான மாநிலங்களவைக் குழு நிறைவேற்றும் தீர்மானம்",
        "B",
        "The Supreme Court in S.R. Bommai ruled that the floor of the House is the ONLY place to test whether the Council of Ministers commands majority support. The Governor cannot subjectively decide majority in the Raj Bhavan without a floor test.",
        "எஸ்.ஆர். பொம்மை வழக்கில் உச்ச நீதிமன்றம், அமைச்சரவைக்கு பெரும்பான்மை ஆதரவு உள்ளதா என்பதை சோதிக்கும் ஒரே இடம் சட்டமன்றத்தின் தளம் (Floor of the House) மட்டுமே என்று தீர்ப்பளித்தது. சட்டமன்றத்தில் வாக்கெடுப்பு நடத்தாமல் ஆளுநர் தனது ராஜ்பவனில் அமர்ந்து தன்னிச்சையாக முடிவு செய்ய முடியாது.",
        "Option A was the prevalent abusive practice that Bommai outlawed.", "விருப்பம் A தவறான நடைமுறை, இதை பொம்மை தீர்ப்பு தடை செய்தது.",
        "Option B is the core 'Floor Test' holding of Bommai.", "விருப்பம் B என்பது பொம்மை வழக்கின் முக்கிய 'சட்டமன்றத் தள வாக்கெடுப்பு' தீர்ப்பாகும்.",
        "Option C has no constitutional standing.", "விருப்பம் C அரசியலமைப்பு அந்தஸ்தற்றது.",
        "Option D is incorrect.", "விருப்பம் D தவறானது.",
        "Bommai Mandate: Floor Test on the floor of the Assembly is mandatory before dismissing a government on grounds of loss of majority.",
        "பொம்மை கட்டளை: பெரும்பான்மை இழப்பு என்ற காரணத்திற்காக ஒரு அரசைக் கலைப்பதற்கு முன் சட்டமன்றத்தில் வாக்கெடுப்பு நடத்துவது கட்டாயமாகும்.",
        "The assessment of majority cannot be done by the Governor through private verification or parade of MLAs in the Raj Bhavan.",
        "ராஜ்பவனில் எம்.எல்.ஏ-க்களை அணிவகுக்க வைப்பதன் மூலமோ அல்லது ஆளுநரின் தனிப்பட்ட சரிபார்ப்பு மூலமோ பெரும்பான்மையை மதிப்பிட முடியாது."
    ))

    # 043 - Key C
    qs.append(make_ep_q(
        PREFIX, 43, DIFF, "Concept MCQ", "Secularism in Bommai",
        "In S.R. Bommai v. Union of India (1994), the Supreme Court upheld the dismissal of the BJP governments in Madhya Pradesh, Rajasthan, and Himachal Pradesh on which fundamental ground?",
        "எஸ்.ஆர். பொம்மை எதிர் இந்திய ஒன்றியம் (1994) வழக்கில், மத்தியப் பிரதேசம், ராஜஸ்தான் மற்றும் இமாச்சலப் பிரதேசத்தில் இருந்த பாஜக அரசுகள் கலைக்கப்பட்டதை உச்ச நீதிமன்றம் எந்த அடிப்படைக் காரணத்திற்காக உறுதி செய்தது?",
        "Failure to achieve rural electrification targets", "கிராமப்புற மின்மயமாக்கல் இலக்குகளை அடையத் தவறியது",
        "Non-payment of civil service provident funds", "அரசு ஊழியர்களின் வருங்கால வைப்பு நிதியைச் செலுத்தாதது",
        "Secularism is a basic feature of the Constitution, and any state government pursuing anti-secular policies violates constitutional governance", "மதச்சார்பின்மை என்பது அரசியலமைப்பின் அடிப்படைக் கட்டமைப்பு; மதச்சார்பின்மைக்கு எதிரான கொள்கைகளைப் பின்பற்றும் எந்தவொரு மாநில அரசும் அரசியலமைப்பு ஆளுகையை மீறுகிறது",
        "Failure to implement compulsory Hindi education", "கட்டாய இந்திக் கல்வியை அமல்படுத்தத் தவறியது",
        "C",
        "The 9-judge bench in S.R. Bommai held that 'Secularism' is an essential component of the Basic Structure of the Indian Constitution. A State Government acting against secularism acts unconstitutionally, justifying intervention under Article 356.",
        "எஸ்.ஆர். பொம்மை வழக்கில் 9 நீதிபதிகள் அமர்வு, 'மதச்சார்பின்மை' என்பது இந்திய அரசியலமைப்பின் அடிப்படைக் கட்டமைப்பின் ஒரு முக்கிய அங்கம் என்று தீர்ப்பளித்தது. மதச்சார்பின்மைக்கு எதிராகச் செயல்படும் ஒரு மாநில அரசு அரசியலமைப்பிற்கு முரணாகச் செயல்படுவதால், சரத்து 356-ன் கீழ் அதன் மீது நடவடிக்கை எடுப்பது நியாயமானது என உறுதி செய்யப்பட்டது.",
        "Option A is a development issue, not ground for Art 356.", "விருப்பம் A வளர்ச்சிப் பிரச்சனை, சரத்து 356-க்கு காரணமல்ல.",
        "Option B is an administrative delay.", "விருப்பம் B நிர்வாகத் தாமதம்.",
        "Option C is the landmark holding elevating Secularism to Basic Structure.", "விருப்பம் C மதச்சார்பின்மையை அடிப்படைக் கட்டமைப்பாக உயர்த்திய வரலாற்றுத் தீர்ப்பாகும்.",
        "Option D is unconstitutional.", "விருப்பம் D அரசியலமைப்பிற்கு முரணானது.",
        "Bommai Landmark: Secularism is part of the Basic Structure of the Constitution.",
        "பொம்மை வரலாற்றுத் தீர்ப்பு: மதச்சார்பின்மை என்பது அரசியலமைப்பின் அடிப்படைக் கட்டமைப்பின் ஒரு பகுதியாகும்.",
        "State politics and state governments cannot pursue policies directed against any religious group or undermine constitutional secularism.",
        "மாநில அரசியலும் மாநில அரசுகளும் எந்தவொரு மதக் குழுவிற்கும் எதிரான அல்லது மதச்சார்பின்மையை சீர்குலைக்கும் கொள்கைகளைப் பின்பற்ற முடியாது."
    ))

    # 044 - Key D
    qs.append(make_ep_q(
        PREFIX, 44, DIFF, "Concept MCQ", "First State Under Art 356",
        "Which State in India was the FIRST to be placed under President's Rule under Article 356?",
        "இந்தியாவில் முதன்முதலில் சரத்து 356-ன் கீழ் குடியரசுத் தலைவர் ஆட்சி விதிக்கப்பட்ட முதல் மாநிலம் எது?",
        "Kerala in 1959", "கேரளா 1959-ல்",
        "Tamil Nadu in 1976", "தமிழ்நாடு 1976-ல்",
        "West Bengal in 1968", "மேற்கு வங்கம் 1968-ல்",
        "Punjab in June 1951", "பஞ்சாப் ஜூன் 1951-ல்",
        "D",
        "President's Rule was imposed for the very first time in India in Punjab on June 20, 1951, due to factional infighting within the ruling Congress party ministry headed by Gopi Chand Bhargava.",
        "இந்தியாவில் முதன்முதலாக குடியரசுத் தலைவர் ஆட்சி ஜூன் 20, 1951 அன்று பஞ்சாப் மாநிலத்தில் விதிக்கப்பட்டது; ஆளும் காங்கிரஸ் கட்சி அமைச்சரவைக்குள் நிலவிய கோபி சந்த் பார்கவா தலைமையிலான உட்கட்சிப் பூசல் காரணமாக இது விதிக்கப்பட்டது.",
        "Option A (Kerala 1959) was the dismissal of the first democratically elected Communist government under E.M.S. Namboodiripad, but was NOT the first state overall.", "விருப்பம் A (கேரளா 1959) இ.எம்.எஸ். நம்பூதிரிபாட் தலைமையிலான கம்யூனிஸ்ட் அரசு கலைக்கப்பட்டது, ஆனால் இது முதலாவது அல்ல.",
        "Option B was the DMK government dismissal during emergency in 1976.", "விருப்பம் B 1976 அவசரநிலையின் போது திமுக அரசு கலைக்கப்பட்டது.",
        "Option C was in 1968.", "விருப்பம் C 1968-ல் நடந்தது.",
        "Option D is correct; Punjab in June 1951 was the first instance of President's Rule in India.", "விருப்பம் D சரியானது; ஜூன் 1951-ல் பஞ்சாபில்தான் இந்தியாவில் முதன்முதலாக குடியரசுத் தலைவர் ஆட்சி விதிக்கப்பட்டது.",
        "First state under President's Rule = Punjab (June 1951).",
        "குடியரசுத் தலைவர் ஆட்சி விதிக்கப்பட்ட முதல் மாநிலம் = பஞ்சாப் (ஜூன் 1951).",
        "Since 1950, Article 356 has been invoked more than 125 times across various Indian States.",
        "1950 முதல், பல்வேறு இந்திய மாநிலங்களில் சரத்து 356 நூற்றுக்கும் மேற்பட்ட முறை பயன்படுத்தப்பட்டுள்ளது."
    ))

    # 045 - Key A
    qs.append(make_ep_q(
        PREFIX, 45, DIFF, "Concept MCQ", "Rameshwar Prasad Landmark",
        "In Rameshwar Prasad v. Union of India (2006), the Supreme Court declared unconstitutional the dissolution of the Legislative Assembly of which State under Article 356?",
        "ராமேஷ்வர் பிரசாத் எதிர் இந்திய ஒன்றியம் (2006) வழக்கில், சரத்து 356-ன் கீழ் எந்த மாநிலத்தின் சட்டமன்றப் பேரவை கலைக்கப்பட்டது அரசியலமைப்பிற்கு முரணானது என்று உச்ச நீதிமன்றம் அறிவித்தது?",
        "Bihar Legislative Assembly", "பீகார் சட்டமன்றப் பேரவை",
        "Karnataka Legislative Assembly", "கர்நாடக சட்டமன்றப் பேரவை",
        "Uttar Pradesh Legislative Assembly", "உத்தரப் பிரதேச சட்டமன்றப் பேரவை",
        "Goa Legislative Assembly", "கோவா சட்டமன்றப் பேரவை",
        "A",
        "In Rameshwar Prasad (2006), a 5-judge Constitution Bench held that the dissolution of the newly elected Bihar Assembly in 2005 by the Governor (Buta Singh) before it could even hold its first meeting, on the ground of preventing horse-trading, was completely mala fide and unconstitutional.",
        "ராமேஷ்வர் பிரசாத் (2006) வழக்கில் 5 நீதிபதிகள் அரசியலமைப்பு அமர்வு, புதிதாகத் தேர்ந்தெடுக்கப்பட்ட பீகார் சட்டமன்றம் தனது முதல் கூட்டத்தைக் கூட்டுவதற்கு முன்பே, குதிரை பேரத்தைத் தடுப்பது என்ற போலி காரணத்திற்காக ஆளுநர் (பூட்டா சிங்) அதை கலைத்தது முற்றிலும் துர்நோக்கமுடையது மற்றும் அரசியலமைப்பிற்கு முரணானது என்று தீர்ப்பளித்தது.",
        "Option A is correct; the 2005 dissolution of the Bihar Assembly was struck down.", "விருப்பம் A சரியானது; பீகார் சட்டமன்றம் கலைக்கப்பட்டது ரத்து செய்யப்பட்டது.",
        "Option B is Bommai case (1994).", "விருப்பம் B பொம்மை வழக்கு (1994).",
        "Option C is incorrect.", "விருப்பம் C தவறானது.",
        "Option D is incorrect.", "விருப்பம் D தவறானது.",
        "Rameshwar Prasad (2006) = Bihar Assembly dissolution struck down as mala fide. Governor cannot prevent a political party from staking claim on mere speculation.",
        "ராமேஷ்வர் பிரசாத் (2006) = பீகார் சட்டமன்றக் கலைப்பு துர்நோக்கமுடையது என ரத்து. வெறும் ஊகங்களின் அடிப்படையில் ஆட்சி அமைக்கக் கோருவதை ஆளுநர் தடுக்க முடியாது.",
        "The court held that a political party cannot be barred from attempting to form a coalition government unless illegal means are proven.",
        "சட்டவிரோத செயல்கள் நிரூபிக்கப்படாத வரை, ஒரு அரசியல் கட்சி கூட்டணி அரசு அமைக்க முயற்சிப்பதைத் தடுக்க முடியாது என்று நீதிமன்றம் கூறியது."
    ))

    # 046 - Key B
    qs.append(make_ep_q(
        PREFIX, 46, DIFF, "Concept MCQ", "Effect on Fundamental Rights Summary",
        "Under the Indian Constitution, during which of the following emergencies are Fundamental Rights affected?",
        "இந்திய அரசியலமைப்பின் கீழ், பின்வரும் எந்த அவசரநிலையின் போது மட்டுமே அடிப்படை உரிமைகள் பாதிக்கப்படுகின்றன?",
        "President's Rule under Article 356 only", "சரத்து 356-ன் கீழான குடியரசுத் தலைவர் ஆட்சியின் போது மட்டுமே",
        "National Emergency under Article 352 only", "சரத்து 352-ன் கீழான தேசிய அவசரநிலையின் போது மட்டுமே",
        "Financial Emergency under Article 360 only", "சரத்து 360-ன் கீழான நிதி அவசரநிலையின் போது மட்டுமே",
        "Both President's Rule and Financial Emergency", "குடியரசுத் தலைவர் ஆட்சி மற்றும் நிதி அவசரநிலை இரண்டிலும்",
        "B",
        "Fundamental Rights are affected ONLY during a National Emergency under Article 352 (via Articles 358 and 359). Neither President's Rule (Article 356) nor Financial Emergency (Article 360) has any effect whatsoever on Fundamental Rights.",
        "சரத்து 352-ன் கீழான தேசிய அவசரநிலையின் போது மட்டுமே (சரத்துகள் 358 மற்றும் 359 வழியாக) அடிப்படை உரிமைகள் பாதிக்கப்படுகின்றன. குடியரசுத் தலைவர் ஆட்சி (356) அல்லது நிதி அவசரநிலை (360) அடிப்படை உரிமைகள் மீது எந்தவொரு தாக்கத்தையும் ஏற்படுத்துவதில்லை.",
        "Option A is incorrect; President's Rule has zero impact on Fundamental Rights.", "விருப்பம் A தவறானது; குடியரசுத் தலைவர் ஆட்சிக்கு அடிப்படை உரிமைகளில் எந்த தாக்கமும் இல்லை.",
        "Option B is correct; National Emergency is the ONLY emergency affecting Fundamental Rights.", "விருப்பம் B சரியானது; தேசிய அவசரநிலை மட்டுமே அடிப்படை உரிமைகளைப் பாதிக்கிறது.",
        "Option C is incorrect; Financial Emergency has zero impact on Fundamental Rights.", "விருப்பம் C தவறானது; நிதி அவசரநிலை அடிப்படை உரிமைகளைப் பாதிப்பதில்லை.",
        "Option D is incorrect.", "விருப்பம் D தவறானது.",
        "Crucial TNPSC Rule: Fundamental Rights can be suspended or restricted ONLY during National Emergency (Art 352).",
        "முக்கிய TNPSC விதி: தேசிய அவசரநிலையின் (352) போது மட்டுமே அடிப்படை உரிமைகளை இடைநிறுத்தவோ கட்டுப்படுத்தவோ முடியும்.",
        "During President's Rule, citizens can still approach High Courts and the Supreme Court under Articles 226 and 32 to enforce all their fundamental rights.",
        "குடியரசுத் தலைவர் ஆட்சியின் போது, குடிமக்கள் தங்கள் அனைத்து அடிப்படை உரிமைகளையும் அமல்படுத்த நீதிமன்றங்களை தாராளமாக அணுகலாம்."
    ))

    # 047 - Key C
    qs.append(make_ep_q(
        PREFIX, 47, DIFF, "Concept MCQ", "Article 354 Financial Alterations",
        "Under Article 354 of the Constitution, during the operation of a National Emergency, the President is empowered to modify which constitutional arrangements?",
        "சரத்து 354-ன் கீழ், தேசிய அவசரநிலை அமலில் உள்ள போது, குடியரசுத் தலைவர் எந்த அரசியலமைப்பு ஏற்பாடுகளை மாற்றியமைக்க அதிகாரம் பெற்றுள்ளார்?",
        "The reservation quotas for Scheduled Castes and Scheduled Tribes", "பட்டியலின மற்றும் பழங்குடியினருக்கான இடஒதுக்கீட்டுப் பங்கீடுகள்",
        "The boundary lines between neighboring States", "அண்டை மாநிலங்களுக்கு இடையேயான எல்லைக் கோடுகள்",
        "The distribution of revenues between the Union and the States under Articles 268 to 279", "சரத்துகள் 268 முதல் 279 வரையிலான மத்திய மற்றும் மாநிலங்களுக்கு இடையேயான நிதி வருவாய் பங்கீடுகள்",
        "The number of judges in the Supreme Court of India", "இந்திய உச்ச நீதிமன்றத்தின் நீதிபதிகளின் எண்ணிக்கை",
        "C",
        "Under Article 354, while a National Emergency is in operation, the President may by order direct that all or any of the provisions of Articles 268 to 279 (relating to distribution of taxes and revenues between the Centre and States) shall have effect subject to such exceptions or modifications as he thinks fit.",
        "சரத்து 354-ன் படி, தேசிய அவசரநிலை அமலில் இருக்கும் போது, மத்திய மற்றும் மாநிலங்களுக்கு இடையேயான வரி மற்றும் வருவாய் பங்கீடு தொடர்பான சரத்துகள் 268 முதல் 279 வரையிலான விதிகளை தாம் தகுதியெனக் கருதும் மாற்றங்களுக்கு உட்படுத்தி குடியரசுத் தலைவர் உத்தரவிடலாம்.",
        "Option A is incorrect; reservation policies are not modified under 354.", "விருப்பம் A தவறானது.",
        "Option B is governed by Article 3, not 354.", "விருப்பம் B சரத்து 3 தொடர்பானது.",
        "Option C is the exact constitutional subject matter of Article 354.", "விருப்பம் C என்பது சரத்து 354-ன் துல்லியமான பொருள் ஆகும்.",
        "Option D is determined by Parliament under Article 124(1).", "விருப்பம் D பாராளுமன்றத்தால் தீர்மானிக்கப்படுகிறது.",
        "Article 354 allows the President to reduce or cancel financial transfers/grants to States during a National Emergency.",
        "தேசிய அவசரநிலையின் போது மாநிலங்களுக்கான நிதிப் பகிர்வு அல்லது மானியங்களைக் குறைக்க அல்லது ரத்து செய்ய குடியரசுத் தலைவருக்கு சரத்து 354 அதிகாரம் அளிக்கிறது.",
        "Such an executive order of modification must be laid before each House of Parliament as soon as may be after it is made.",
        "அவ்வாறு பிறப்பிக்கப்படும் நிதி மாற்றியமைப்பு ஆணை பிறப்பிக்கப்பட்ட உடனேயே பாராளுமன்றத்தின் இரு அவைகளிலும் சமர்ப்பிக்கப்பட வேண்டும்."
    ))

    # 048 - Key D
    qs.append(make_ep_q(
        PREFIX, 48, DIFF, "Concept MCQ", "Emergency Summary Matrix",
        "Which of the following pairings correctly matches the Emergency type with its constitutional article and maximum permissible duration?",
        "பின்வரும் இணைகளில் எது அவசரநிலை வகை, அதன் அரசியலமைப்புச் சரத்து மற்றும் அதிகபட்ச அனுமதிக்கப்பட்ட கால அளவைச் சரியாகப் பொருத்துகிறது?",
        "National Emergency — Article 356 — Maximum 3 years", "தேசிய அவசரநிலை — சரத்து 356 — அதிகபட்சம் 3 ஆண்டுகள்",
        "Financial Emergency — Article 352 — Maximum 1 year", "நிதி அவசரநிலை — சரத்து 352 — அதிகபட்சம் 1 ஆண்டு",
        "President's Rule — Article 360 — Maximum 6 months", "குடியரசுத் தலைவர் ஆட்சி — சரத்து 360 — அதிகபட்சம் 6 மாதங்கள்",
        "President's Rule — Article 356 — Maximum 3 years", "குடியரசுத் தலைவர் ஆட்சி — சரத்து 356 — அதிகபட்சம் 3 ஆண்டுகள்",
        "D",
        "President's Rule is governed by Article 356 and has a maximum permissible constitutional limit of 3 years (in 6-month blocks). National Emergency is governed by Article 352 and has NO maximum limit. Financial Emergency is governed by Article 360 and continues indefinitely until revoked.",
        "குடியரசுத் தலைவர் ஆட்சி சரத்து 356-ஆல் நிர்வகிக்கப்படுகிறது, மேலும் அதிகபட்சமாக 3 ஆண்டுகள் வரை அனுமதிக்கப்படுகிறது (6 மாதத் தவணைகளில்). தேசிய அவசரநிலை சரத்து 352-ஆல் நிர்வகிக்கப்படுகிறது, இதற்கு அதிகபட்ச வரம்பு இல்லை. நிதி அவசரநிலை சரத்து 360-ஆல் நிர்வகிக்கப்படுகிறது, இது ரத்து செய்யப்படும் வரை காலவரையின்றி தொடர்கிறது.",
        "Option A wrongly pairs National Emergency with Article 356.", "விருப்பம் A தேசிய அவசரநிலையை சரத்து 356-உடன் தவறாக இணைக்கிறது.",
        "Option B wrongly pairs Financial Emergency with Article 352.", "விருப்பம் B நிதி அவசரநிலையை சரத்து 352-உடன் தவறாக இணைக்கிறது.",
        "Option C wrongly pairs President's Rule with Article 360.", "விருப்பம் C குடியரசுத் தலைவர் ஆட்சியை சரத்து 360-உடன் தவறாக இணைக்கிறது.",
        "Option D is the perfectly accurate constitutional pairing.", "விருப்பம் D என்பது முற்றிலும் சரியான அரசியலமைப்பு இணையாகும்.",
        "Master Formula: Art 352 (National) = No Max Limit; Art 356 (State) = 3 Years Max; Art 360 (Financial) = No Max Limit.",
        "முக்கிய சூத்திரம்: சரத்து 352 (தேசியம்) = அதிகபட்ச வரம்பு இல்லை; சரத்து 356 (மாநிலம்) = அதிகபட்சம் 3 ஆண்டுகள்; சரத்து 360 (நிதி) = அதிகபட்ச வரம்பு இல்லை.",
        "Mastering these differences is essential for scoring full marks in TNPSC Polity questions.",
        "இந்த வேறுபாடுகளில் தேர்ச்சி பெறுவது TNPSC பாலிட்டி வினாக்களில் முழு மதிப்பெண் பெற அவசியமாகும்."
    ))

    # 049 - Key A
    qs.append(make_ep_q(
        PREFIX, 49, DIFF, "Concept MCQ", "Effect on Federalism",
        "During a National Emergency under Article 352, how does the nature of the Indian political system transform according to Dr. B.R. Ambedkar?",
        "சரத்து 352-ன் கீழான தேசிய அவசரநிலையின் போது, டாக்டர் பி.ஆர். அம்பேத்கரின் கூற்றுப்படி இந்திய அரசியல் அமைப்பின் தன்மை எவ்வாறு மாறுகிறது?",
        "It is transformed from a federal constitution into a unitary one without any formal constitutional amendment", "எந்தவொரு முறையான அரசியலமைப்பு திருத்தமும் இன்றி கூட்டாட்சி அரசியலமைப்பிலிருந்து ஒற்றையாட்சி முறையாக மாற்றப்படுகிறது",
        "It transforms into a direct military dictatorship under the Chief of Defence Staff", "முப்படைகளின் தலைமை தளபதியின் கீழான நேரடி ராணுவ சர்வாதிகாரமாக மாறுகிறது",
        "It becomes a confederation where states become fully independent sovereign nations", "மாநிலங்கள் முழு இறையாண்மை கொண்ட நாடுகளாக மாறும் ஒரு கூட்டமைப்பாக மாறுகிறது",
        "The Constitution is entirely annulled and replaced with martial law", "அரசியலமைப்பு முற்றிலும் ரத்து செய்யப்பட்டு ராணுவச் சட்டம் அமல்படுத்தப்படுகிறது",
        "A",
        "Dr. B.R. Ambedkar famously remarked in the Constituent Assembly that the Indian Constitution is designed to work as a federal system in normal times, but during war or emergency, it is so worked as to make it into a unitary system without a constitutional amendment.",
        "அரசியலமைப்பு நிர்ணய சபையில் டாக்டர் பி.ஆர். அம்பேத்கர் கூறியது போல: இந்திய அரசியலமைப்பு சாதாரண காலங்களில் கூட்டாட்சி அமைப்பாகவும், அவசரநிலையின் போது எந்தவொரு முறையான அரசியலமைப்பு திருத்தமும் இன்றியே ஒற்றையாட்சி அமைப்பாகவும் செயல்படும் வகையில் வடிவமைக்கப்பட்டுள்ளது.",
        "Option A is the famous quote and core design principle highlighted by Dr. Ambedkar.", "விருப்பம் A என்பது டாக்டர் அம்பேத்கர் விளக்கிய புகழ்பெற்ற தத்துவக் கொள்கையாகும்.",
        "Option B is incorrect; civilian democratic command is maintained.", "விருப்பம் B தவறானது; மக்களாட்சி அதிகாரமே நீடிக்கிறது.",
        "Option C is the complete opposite of a unitary transformation.", "விருப்பம் C ஒற்றையாட்சி மாற்றத்திற்கு முற்றிலும் எதிரானது.",
        "Option D is incorrect; the Constitution continues to be supreme law.", "விருப்பம் D தவறானது; அரசியலமைப்பே உச்ச சட்டமாக நீடிக்கிறது.",
        "Ambedkar's words: 'In normal times, it is framed to work as a federal system. But in times of war it is so designed that it may work as though it was a unitary system.'",
        "அம்பேத்கரின் வார்த்தைகள்: 'சாதாரண காலங்களில் இது கூட்டாட்சி அமைப்பாக செயல்பட வடிவமைக்கப்பட்டுள்ளது. ஆனால் போர் காலங்களில் இது ஒற்றையாட்சி முறை போல செயல்படும் வகையில் அமைக்கப்பட்டுள்ளது.'",
        "This unique flexibility is one of the most distinctive features of Indian federalism.",
        "இந்த தனித்துவமான நெகிழ்வுத்தன்மை இந்திய கூட்டாட்சியின் மிகச் சிறந்த அம்சங்களில் ஒன்றாகும்."
    ))

    # 050 - Key B
    qs.append(make_ep_q(
        PREFIX, 50, DIFF, "Concept MCQ", "Emergency Chapter Summary",
        "Which of the following constitutional articles correctly completes the sequence: National Emergency (Art 352), State Emergency / President's Rule (Art 356), and Financial Emergency (_______)?",
        "தேசிய அவசரநிலை (சரத்து 352), மாநில அவசரநிலை / குடியரசுத் தலைவர் ஆட்சி (சரத்து 356), மற்றும் நிதி அவசரநிலை (_______) என்ற வரிசையை பின்வரும் எந்த சரத்து சரியாக நிறைவு செய்கிறது?",
        "Article 358", "சரத்து 358",
        "Article 360", "சரத்து 360",
        "Article 365", "சரத்து 365",
        "Article 368", "சரத்து 368",
        "B",
        "The three types of emergencies in Part XVIII are: 1. National Emergency (Article 352); 2. President's Rule (Article 356); 3. Financial Emergency (Article 360).",
        "பகுதி XVIII-ல் உள்ள மூன்று வகையான அவசரநிலைகள்: 1. தேசிய அவசரநிலை (சரத்து 352); 2. குடியரசுத் தலைவர் ஆட்சி (சரத்து 356); 3. நிதி அவசரநிலை (சரத்து 360).",
        "Option A governs suspension of Article 19 during National Emergency.", "விருப்பம் A தேசிய அவசரநிலையின் போது சரத்து 19 இடைநிறுத்தம் தொடர்பானது.",
        "Option B is correct; Article 360 governs Financial Emergency.", "விருப்பம் B சரியானது; சரத்து 360 நிதி அவசரநிலையை நிர்வகிக்கிறது.",
        "Option C deals with failure to comply with Union directions.", "விருப்பம் C மத்திய வழிகாட்டுதல்களைப் பின்பற்றத் தவறுதல் தொடர்பானது.",
        "Option D deals with the procedure for amendment of the Constitution.", "விருப்பம் D அரசியலமைப்பு திருத்த நடைமுறை தொடர்பானது.",
        "Remember the '4-year gap' in article numbers: 352 + 4 = 356; 356 + 4 = 360!",
        "சரத்து எண்களில் உள்ள '4-ஆண்டு இடைவெளியை' நினைவில் கொள்க: 352 + 4 = 356; 356 + 4 = 360!",
        "Mastering Articles 352, 356, and 360 provides the complete structural foundation for TNPSC Emergency Provisions.",
        "சரத்துகள் 352, 356 மற்றும் 360-ல் தேர்ச்சி பெறுவது TNPSC அவசரநிலைப் பிரிவுகளுக்கான முழுமையான கட்டமைப்பு அடித்தளத்தை வழங்குகிறது."
    ))

    return qs

def build_and_validate_easy():
    qs = get_easy_questions() + get_easy_questions_part2()
    print(f"[EASY] Total questions generated: {len(qs)}")
    assert len(qs) == 50, f"Expected 50 questions, got {len(qs)}"

    # Check key balance
    dist = dict(Counter([q["correct_answer"] for q in qs]))
    print(f"[EASY] Key Distribution: {dist}")
    assert dist == {"A": 13, "B": 13, "C": 12, "D": 12}, f"Distribution mismatch: {dist}"

    # Check uniqueness
    stems = [q["question_en"].strip().lower() for q in qs]
    assert len(stems) == len(set(stems)), "Duplicate stems found in Easy set!"
    print("[EASY] Stems are 100% unique.")

    out_file = "data/questions/polity/emergency_provisions_easy.json"
    os.makedirs(os.path.dirname(out_file), exist_ok=True)
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2, ensure_ascii=False)
    print(f"[EASY] Saved to {out_file}")

    rep = ContentValidator.validate_file(out_file, expected_count=50, expected_prefix=PREFIX)
    print(f"[EASY] Validator Status: {'PASS' if rep.is_valid else 'FAIL'} | Audited: {rep.total_audited}")
    if rep.issues:
        for iss in rep.issues:
            print(f"  [{iss.severity}] {iss.question_id}: {iss.message}")
        assert False, "Validation failed!"
    print("[EASY] Validation PASSED with 0 issues!")

if __name__ == "__main__":
    build_and_validate_easy()
