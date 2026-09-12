# -*- coding: utf-8 -*-
"""
Generator for Emergency Provisions Medium MCQs (50 questions: EP_M_001 to EP_M_050)
Strictly adheres to:
1. 24-field schema verified by validator.py
2. Bilingual parity (English and Tamil)
3. Balanced answer distribution: A: 12, B: 13, C: 13, D: 12
4. In-depth conceptual coverage of procedural nuances, constitutional amendments, and operational mechanics
"""

import json
import os
from collections import Counter
from ep_mcq_helper import make_ep_q
from tools.nova_content_engine.validator import ContentValidator

PREFIX = "EP_M_"
DIFF = "Medium"

def get_medium_questions():
    qs = []

    # 001 - Key A
    qs.append(make_ep_q(
        PREFIX, 1, DIFF, "Conceptual Analysis", "National Emergency - Parliamentary Approval",
        "If a proclamation of National Emergency is issued when the Lok Sabha is dissolved, within what period must the reconstituted Lok Sabha approve it, assuming Rajya Sabha has already approved it?",
        "மக்களவை கலைக்கப்பட்டிருக்கும் போது தேசிய அவசரநிலை பிரகடனம் வெளியிடப்பட்டால், மாநிலங்களவை ஏற்கனவே ஒப்புதல் அளித்திருப்பின், புதிதாக அமைக்கப்பட்ட மக்களவை எத்தனை நாட்களுக்குள் அதற்கு ஒப்புதல் அளிக்க வேண்டும்?",
        "Within 30 days from its first sitting", "அதன் முதல் அமர்விலிருந்து 30 நாட்களுக்குள்",
        "Within 60 days from its first sitting", "அதன் முதல் அமர்விலிருந்து 60 நாட்களுக்குள்",
        "Within 14 days from its first sitting", "அதன் முதல் அமர்விலிருந்து 14 நாட்களுக்குள்",
        "Within 6 months from the date of proclamation", "பிரகடனம் செய்யப்பட்ட நாளிலிருந்து 6 மாதங்களுக்குள்",
        "A",
        "Under Article 352(4), if a proclamation is issued while Lok Sabha is dissolved or dissolution takes place during the one-month period without approval, and Rajya Sabha approves it, the proclamation survives until 30 days from the first sitting of the reconstituted Lok Sabha.",
        "சரத்து 352(4)-ன் கீழ், மக்களவை கலைக்கப்பட்டிருக்கும் போதோ அல்லது ஒரு மாத காலத்திற்குள் ஒப்புதல் அளிக்காமல் கலைக்கப்பட்டாலோ, மாநிலங்களவை ஒப்புதல் அளித்திருந்தால், புதிய மக்களவை கூடிய முதல் அமர்விலிருந்து 30 நாட்களுக்குள் ஒப்புதல் அளிக்க வேண்டும்.",
        "Option A is correct as per Article 352(4).", "சரத்து 352(4)-ன் படி விருப்பம் A சரியானது.",
        "Option B (60 days) applies to President's Rule or Financial Emergency, not the reconstituted Lok Sabha deadline.", "விருப்பம் B (60 நாட்கள்) குடியரசுத் தலைவர் ஆட்சி அல்லது நிதி அவசரநிலைக்குப் பொருந்தும்.",
        "Option C (14 days) is the notice period for special sitting to disapprove emergency.", "விருப்பம் C (14 நாட்கள்) அவசரநிலையை நிராகரிக்கும் சிறப்பு அமர்வுக்கான அறிவிப்பு காலம்.",
        "Option D (6 months) is the period of validity once approved by both Houses.", "விருப்பம் D (6 மாதங்கள்) இரு அவைகளும் ஒப்புதல் அளித்த பின் நீடிக்கும் காலம்.",
        "Remember the '30-day survival clock' for the newly elected Lok Sabha during National Emergency.",
        "தேசிய அவசரநிலையின் போது புதிதாக தேர்ந்தெடுக்கப்பட்ட மக்களவைக்கான '30 நாள் காலக்கெடுவை' நினைவில் கொள்க.",
        "This safeguard ensures that the directly elected representatives validate the executive's extraordinary powers promptly after elections.",
        "மக்களால் நேரடியாகத் தேர்ந்தெடுக்கப்பட்ட பிரதிநிதிகள் அவசரநிலை அதிகாரங்களை தேர்தலுக்குப் பிறகு உடனடியாகச் சரிபார்ப்பதை இந்த விதி உறுதி செய்கிறது."
    ))

    # 002 - Key B
    qs.append(make_ep_q(
        PREFIX, 2, DIFF, "Procedural Nuance", "National Emergency - Majority Requirement",
        "Prior to the 44th Constitutional Amendment Act of 1978, what type of parliamentary majority was required for approving a proclamation of National Emergency?",
        "1978-ஆம் ஆண்டின் 44-வது அரசியலமைப்பு திருத்தச் சட்டத்திற்கு முன்பு, தேசிய அவசரநிலைப் பிரகடனத்திற்கு ஒப்புதல் அளிக்க பாராளுமன்றத்தில் எந்த வகையான பெரும்பான்மை தேவைப்பட்டது?",
        "Special majority of both Houses", "இரு அவைகளின் சிறப்புப் பெரும்பான்மை",
        "Simple majority of both Houses", "இரு அவைகளின் எளிய பெரும்பான்மை",
        "Absolute majority of both Houses", "இரு அவைகளின் அறுதிப் பெரும்பான்மை",
        "Special majority with ratification by half of the states", "பாதி மாநிலங்களின் ஒப்புதலுடன் கூடிய சிறப்புப் பெரும்பான்மை",
        "B",
        "Originally, a proclamation of National Emergency could be approved by a simple majority of both Houses of Parliament. The 44th Amendment Act of 1978 introduced the stringent requirement of a special majority (majority of total membership and not less than 2/3 of members present and voting).",
        "தொடக்கத்தில், தேசிய அவசரநிலைப் பிரகடனத்தை பாராளுமன்றத்தின் இரு அவைகளும் எளிய பெரும்பான்மையால் ஒப்புதல் அளிக்க முடிந்தது. 1978-ன் 44-வது திருத்தச் சட்டம் சிறப்புப் பெரும்பான்மை (மொத்த உறுப்பினர்களில் பெரும்பான்மை மற்றும் வருகை தந்து வாக்களிப்போரில் 2/3 பங்கு) என்ற கடுமையான நிபந்தனையைக் கொண்டுவந்தது.",
        "Option A was introduced by the 44th Amendment, not required prior to it.", "விருப்பம் A என்பது 44-வது திருத்தத்தால் கொண்டுவரப்பட்டது, அதற்கு முன்பு தேவையில்லை.",
        "Option B is correct; simple majority was sufficient before 1978.", "விருப்பம் B சரியானது; 1978-க்கு முன்பு எளிய பெரும்பான்மை போதுமானதாக இருந்தது.",
        "Option C is total membership majority alone, which was not the specific standard.", "விருப்பம் C என்பது மொத்த உறுப்பினர் பெரும்பான்மை மட்டுமே, இது அங்கு பயன்படுத்தப்படவில்லை.",
        "Option D state ratification is not required for emergency proclamations under Article 352.", "விருப்பம் D சரத்து 352-ன் கீழ் அவசரநிலைக்கு மாநிலங்களின் ஏற்பு தேவையில்லை.",
        "Watch out: Simple majority was required before 1978; 44th CAA raised it to Special majority.",
        "கவனிக்க: 1978-க்கு முன்பு எளிய பெரும்பான்மை போதுமானது; 44-வது சட்டம் அதை சிறப்புப் பெரும்பான்மையாக உயர்த்தியது.",
        "The 44th Amendment raised the majority threshold to prevent misuse like that of the 1975 emergency.",
        "1975 அவசரநிலை போன்ற தவறான பயன்பாட்டைத் தடுக்க 44-வது திருத்தம் பெரும்பான்மை வரம்பை உயர்த்தியது."
    ))

    # 003 - Key C
    qs.append(make_ep_q(
        PREFIX, 3, DIFF, "Constitutional Mechanism", "Fundamental Rights during Emergency",
        "Under Article 358 of the Indian Constitution, the automatic suspension of six Fundamental Rights guaranteed by Article 19 is triggered only when a National Emergency is declared on the grounds of:",
        "இந்திய அரசியலமைப்பின் சரத்து 358-ன் கீழ், சரத்து 19 உத்தரவாதம் அளிக்கும் ஆறு அடிப்படை உரிமைகள் தானாகவே இடைநிறுத்தப்படுவது, தேசிய அவசரநிலை எந்தக் காரணங்களின் அடிப்படையில் பிரகடனப்படுத்தப்படும் போது மட்டுமே நிகழும்?",
        "Armed rebellion only", "ஆயுதமேந்திய கிளர்ச்சி மட்டுமே",
        "Internal disturbance and armed rebellion", "உள்நாட்டுக் குழப்பம் மற்றும் ஆயுதமேந்திய கிளர்ச்சி",
        "War or external aggression", "போர் அல்லது வெளிநாட்டு ஆக்கிரமிப்பு",
        "Financial instability or threat to credit", "நிதி உறுதியற்ற தன்மை அல்லது கடன் அச்சுறுத்தல்",
        "C",
        "Under Article 358, as amended by the 44th Amendment Act 1978, the fundamental freedoms under Article 19 are automatically suspended ONLY when National Emergency is declared on grounds of war or external aggression (External Emergency). They are NOT suspended when declared on grounds of armed rebellion (Internal Emergency).",
        "1978-ன் 44-வது திருத்தச் சட்டத்தின்படி, சரத்து 358-ன் கீழ் சரத்து 19 உரிமைகள் தானாகவே இடைநிறுத்தப்படுவது போர் அல்லது வெளிநாட்டு ஆக்கிரமிப்பு (வெளிப்புற அவசரநிலை) அடிப்படையில் பிரகடனம் செய்யப்படும் போது மட்டுமே. ஆயுதமேந்திய கிளர்ச்சியின் போது இவை இடைநிறுத்தப்படாது.",
        "Option A is incorrect; Article 19 rights are explicitly NOT suspended for armed rebellion post-1978.", "விருப்பம் A தவறானது; 1978-க்குப் பிறகு ஆயுதமேந்திய கிளர்ச்சிக்காக சரத்து 19 உரிமைகள் இடைநிறுத்தப்படாது.",
        "Option B includes internal disturbance, which was removed from the Constitution entirely by the 44th CAA.", "விருப்பம் B-ல் உள்ள உள்நாட்டுக் குழப்பம் 44-வது திருத்தத்தால் முற்றிலும் நீக்கப்பட்டது.",
        "Option C is correct; war or external aggression alone triggers automatic suspension under Article 358.", "விருப்பம் C சரியானது; போர் அல்லது வெளிநாட்டு ஆக்கிரமிப்பு மட்டுமே சரத்து 358-ன் கீழ் தானியங்கி இடைநிறுத்தத்தைத் தூண்டும்.",
        "Option D relates to financial emergency under Article 360.", "விருப்பம் D சரத்து 360-ன் கீழ் நிதி அவசரநிலை தொடர்பானது.",
        "TNPSC Trap: Article 358 operates automatically ONLY during War or External Aggression, NEVER during Armed Rebellion.",
        "TNPSC பொறி: சரத்து 358 போர் அல்லது வெளிநாட்டு ஆக்கிரமிப்பின் போது மட்டுமே தானாகச் செயல்படும், ஆயுதமேந்திய கிளர்ச்சியின் போது அல்ல.",
        "This distinction was inserted by the 44th Amendment to protect civil liberties during internal unrest.",
        "உள்நாட்டுக் குழப்பங்களின் போது குடிமை உரிமைகளைப் பாதுகாக்கவே இந்த வேறுபாடு 44-வது திருத்தத்தால் சேர்க்கப்பட்டது."
    ))

    # 004 - Key D
    qs.append(make_ep_q(
        PREFIX, 4, DIFF, "Constitutional Comparison", "Article 358 vs Article 359",
        "Which of the following statements correctly distinguishes Article 358 from Article 359?",
        "சரத்து 358 மற்றும் சரத்து 359 ஆகியவற்றுக்கு இடையேயான வேறுபாடுகளில் பின்வருவனவற்றில் எது சரியானது?",
        "Article 358 suspends the right to seek remedies, while Article 359 suspends the fundamental rights entirely.", "சரத்து 358 தீர்வுகளுக்கான உரிமையை இடைநிறுத்துகிறது, சரத்து 359 அடிப்படை உரிமைகளை முழுமையாக இடைநிறுத்துகிறது.",
        "Article 358 requires a specific Presidential Order, whereas Article 359 operates automatically.", "சரத்து 358-க்கு குறிப்பிட்ட குடியரசுத் தலைவர் ஆணை தேவை, சரத்து 359 தானாகவே செயல்படுகிறது.",
        "Article 358 operates during armed rebellion, whereas Article 359 operates only during external aggression.", "சரத்து 358 ஆயுதமேந்திய கிளர்ச்சியின் போது செயல்படுகிறது, சரத்து 359 வெளிநாட்டு ஆக்கிரமிப்பின் போது மட்டுமே செயல்படுகிறது.",
        "Article 358 extends to the entire country automatically, whereas Article 359 may extend to the whole country or any part thereof.", "சரத்து 358 நாடு முழுவதற்கும் தானாகவே விரிவடைகிறது, சரத்து 359 நாடு முழுவதற்கும் அல்லது அதன் ஏதேனும் ஒரு பகுதிக்கும் விரிவடையலாம்.",
        "D",
        "Article 358 automatically suspends Article 19 throughout the whole of India. In contrast, Article 359 empowers the President to issue an order suspending the enforcement of specified fundamental rights (except Arts 20 and 21) for the whole country or any specified part thereof.",
        "சரத்து 358 இந்தியா முழுவதும் தானாகவே சரத்து 19-ஐ இடைநிறுத்துகிறது. மாறாக, சரத்து 359 குடியரசுத் தலைவர் பிறப்பிக்கும் ஆணை மூலம் குறிப்பிடப்பட்ட உரிமைகளின் அமலாக்கத்தை (சரத்து 20 மற்றும் 21 தவிர) நாடு முழுமைக்கோ அல்லது குறிப்பிட்ட பகுதிக்குமோ இடைநிறுத்த அதிகாரம் அளிக்கிறது.",
        "Option A reverses the concept: Art 358 suspends rights under Art 19, while Art 359 suspends only the enforcement/remedy.", "விருப்பம் A தவறானது: சரத்து 358 உரிமைகளை நிறுத்துகிறது, சரத்து 359 அமலாக்கத்தை/தீர்வை மட்டுமே நிறுத்துகிறது.",
        "Option B is inverted: Art 358 operates automatically, whereas Art 359 requires a Presidential Order.", "விருப்பம் B தலைகீழானது: சரத்து 358 தானாகச் செயல்படுகிறது, சரத்து 359-க்கு குடியரசுத் தலைவர் ஆணை தேவை.",
        "Option C is false: Art 358 never operates during armed rebellion.", "விருப்பம் C தவறு: சரத்து 358 ஆயுதமேந்திய கிளர்ச்சியின் போது செயல்படாது.",
        "Option D is fully correct regarding territorial extent.", "விருப்பம் D பிராந்திய எல்லை சார்ந்து முற்றிலும் சரியானது.",
        "Art 358 = Automatic, Art 19 only, War/External Aggression, All India. Art 359 = Presidential Order, Specified rights (except 20 & 21), All grounds, Whole or part.",
        "சரத்து 358 = தானியங்கி, சரத்து 19 மட்டும், போர்/வெளிநாட்டு ஆக்கிரமிப்பு, முழு இந்தியா. சரத்து 359 = குடியரசுத் தலைவர் ஆணை, குறிப்பிட்ட உரிமைகள் (20 & 21 தவிர), அனைத்துக் காரணங்கள், முழுமை அல்லது பகுதி.",
        "Neither Article 358 nor Article 359 allows suspension of Articles 20 and 21 under any circumstances.",
        "எந்தச் சூழ்நிலையிலும் சரத்து 20 மற்றும் 21-ஐ இடைநிறுத்த சரத்து 358 அல்லது சரத்து 359 அனுமதிக்காது."
    ))

    # 005 - Key A
    qs.append(make_ep_q(
        PREFIX, 5, DIFF, "Constitutional Safeguard", "Revocation of National Emergency",
        "Under Article 352(8), a special sitting of the Lok Sabha must be held within how many days to consider a resolution disapproving a National Emergency, if written notice is signed by 1/10th of its members?",
        "சரத்து 352(8)-ன் கீழ், மக்களவையின் 1/10 பங்கு உறுப்பினர்கள் கையெழுத்திட்ட எழுத்துப்பூர்வ அறிவிப்பு அளிக்கப்பட்டால், தேசிய அவசரநிலையை நிராகரிக்கும் தீர்மானத்தை பரிசீலிக்க எத்தனை நாட்களுக்குள் மக்களவையின் சிறப்பு அமர்வு கூட்டப்பட வேண்டும்?",
        "Within 14 days", "14 நாட்களுக்குள்",
        "Within 30 days", "30 நாட்களுக்குள்",
        "Within 21 days", "21 நாட்களுக்குள்",
        "Within 7 days", "7 நாட்களுக்குள்",
        "A",
        "Inserted by the 44th Amendment Act 1978, Article 352(8) states that if not less than 1/10th of the total members of Lok Sabha give written notice to the Speaker (or President if House is not in session), a special sitting of the House must be held within 14 days to consider a resolution disapproving the proclamation.",
        "1978-ன் 44-வது திருத்தச் சட்டத்தால் சேர்க்கப்பட்ட சரத்து 352(8)-ன் படி, மக்களவையின் மொத்த உறுப்பினர்களில் 1/10 பங்குக்குக் குறையாதவர்கள் சபாநாயகருக்கு (அமர்வு இல்லாத போது குடியரசுத் தலைவருக்கு) எழுத்துப்பூர்வ அறிவிப்பு அளித்தால், 14 நாட்களுக்குள் சிறப்பு அமர்வு கூட்டப்பட வேண்டும்.",
        "Option A is correct; 14 days is the mandatory statutory window.", "விருப்பம் A சரியானது; 14 நாட்கள் என்பது கட்டாய காலக்கெடுவாகும்.",
        "Option B (30 days) is the period for approval by new Lok Sabha, not disapproval requisition.", "விருப்பம் B (30 நாட்கள்) புதிய மக்களவை ஒப்புதலுக்கான காலம், நிராகரிப்புக்கானது அல்ல.",
        "Option C (21 days) is not associated with Article 352 procedures.", "விருப்பம் C (21 நாட்கள்) சரத்து 352 நடைமுறைகளுடன் தொடர்புடையது அல்ல.",
        "Option D (7 days) is too short and not the constitutional timeline.", "விருப்பம் D (7 நாட்கள்) மிகக் குறுகிய காலம் மற்றும் அரசியலமைப்பு காலக்கெடு அல்ல.",
        "Disapproval Resolution Safeguard: 1/10th members of Lok Sabha -> Notice to Speaker/President -> Special sitting within 14 days -> Simple majority.",
        "நிராகரிப்புத் தீர்மானப் பாதுகாப்பு: 1/10 மக்களவை உறுப்பினர்கள் -> சபாநாயகர்/குடியரசுத் தலைவருக்கு அறிவிப்பு -> 14 நாட்களுக்குள் சிறப்பு அமர்வு -> எளிய பெரும்பான்மை.",
        "Notice of disapproval goes exclusively to the Lok Sabha, giving it sole power to check and revoke the emergency.",
        "நிராகரிப்பு அறிவிப்பு மக்களவைக்கு மட்டுமே செல்லும், இதனால் அவசரநிலையைத் திரும்பப் பெறும் பிரத்யேக அதிகாரம் மக்களவைக்கு உள்ளது."
    ))

    # 006 - Key B
    qs.append(make_ep_q(
        PREFIX, 6, DIFF, "Conceptual Nuance", "Approval vs Disapproval Mechanisms",
        "How does a resolution disapproving the continuation of a National Emergency differ from a resolution approving it?",
        "தேசிய அவசரநிலையைத் தொடர்வதற்கு ஒப்புதல் அளிக்கும் தீர்மானத்திலிருந்து அதை நிராகரிக்கும் தீர்மானம் எவ்வாறு வேறுபடுகிறது?",
        "Approval requires Lok Sabha only, while disapproval requires both Houses.", "ஒப்புதலுக்கு மக்களவை மட்டுமே போதும், ஆனால் நிராகரிப்புக்கு இரு அவைகளும் தேவை.",
        "Approval requires both Houses by special majority, while disapproval requires Lok Sabha only by simple majority.", "ஒப்புதலுக்கு இரு அவைகளின் சிறப்புப் பெரும்பான்மை தேவை, ஆனால் நிராகரிப்புக்கு மக்களவையின் எளிய பெரும்பான்மை மட்டுமே போதும்.",
        "Disapproval requires a special majority of Lok Sabha, while approval requires a simple majority of both Houses.", "நிராகரிப்புக்கு மக்களவையின் சிறப்புப் பெரும்பான்மை தேவை, ஒப்புதலுக்கு இரு அவைகளின் எளிய பெரும்பான்மை தேவை.",
        "Approval requires simple majority of both Houses, while disapproval requires 2/3rd majority of Rajya Sabha.", "ஒப்புதலுக்கு இரு அவைகளின் எளிய பெரும்பான்மை தேவை, நிராகரிப்புக்கு மாநிலங்களவையின் 2/3 பங்கு பெரும்பான்மை தேவை.",
        "B",
        "A resolution of approval must be passed by BOTH Houses of Parliament by a SPECIAL majority. In contrast, a resolution of disapproval is required to be passed ONLY by the LOK SABHA by a SIMPLE majority (Article 352(7)).",
        "ஒப்புதல் தீர்மானம் பாராளுமன்றத்தின் இரு அவைகளாலும் சிறப்புப் பெரும்பான்மையுடன் நிறைவேற்றப்பட வேண்டும். மாறாக, நிராகரிப்புத் தீர்மானம் மக்களவையால் மட்டுமே எளிய பெரும்பான்மையுடன் நிறைவேற்றப்பட வேண்டும் (சரத்து 352(7)).",
        "Option A is completely backwards.", "விருப்பம் A முற்றிலும் தவறானது.",
        "Option B correctly highlights both the legislative chamber requirement and the majority threshold differences.", "விருப்பம் B சட்டப் பேரவை தேவை மற்றும் பெரும்பான்மை வரம்பு வேறுபாடுகள் இரண்டையும் சரியாகக் காட்டுகிறது.",
        "Option C misstates the majority thresholds in reverse.", "விருப்பம் C பெரும்பான்மை வரம்புகளை தலைகீழாகக் கூறுகிறது.",
        "Option D mentions Rajya Sabha for disapproval, which is incorrect as Rajya Sabha has no role in the disapproval resolution under Art 352(7).", "விருப்பம் D மாநிலங்களவையைக் குறிப்பிடுகிறது, சரத்து 352(7)-ன் கீழ் நிராகரிப்பில் மாநிலங்களவைக்கு பங்கில்லை.",
        "Remember: Approval = Lok Sabha + Rajya Sabha (Special Majority). Disapproval = Lok Sabha ONLY (Simple Majority).",
        "நினைவில் கொள்க: ஒப்புதல் = மக்களவை + மாநிலங்களவை (சிறப்புப் பெரும்பான்மை). நிராகரிப்பு = மக்களவை மட்டுமே (எளிய பெரும்பான்மை).",
        "This asymmetry empowers the directly elected lower house to independently terminate the emergency at any time.",
        "இந்த சமச்சீரற்ற தன்மை மக்களால் நேரடியாகத் தேர்ந்தெடுக்கப்பட்ட மக்களவை எப்போது வேண்டுமானாலும் அவசரநிலையை முடிவுக்குக் கொண்டுவர அதிகாரம் அளிக்கிறது."
    ))

    # 007 - Key C
    qs.append(make_ep_q(
        PREFIX, 7, DIFF, "Constitutional Law", "Judicial Review of Emergency",
        "Which landmark Supreme Court judgment held that the proclamation of National Emergency under Article 352 can be challenged in court on grounds of malafide or that the declaration was wholly based on irrelevant facts?",
        "சரத்து 352-ன் கீழ் தேசிய அவசரநிலைப் பிரகடனம் உள்நோக்கம் கொண்டது என்றோ அல்லது முற்றிலும் தொடர்பற்ற உண்மைகளை அடிப்படையாகக் கொண்டது என்றோ நீதிமன்றத்தில் சவாலுக்கு உட்படுத்தப்படலாம் என்று எந்த வரலாற்றுச் சிறப்புமிக்க வழக்கில் உச்ச நீதிமன்றம் தீர்ப்பளித்தது?",
        "Kesavananda Bharati v. State of Kerala (1973)", "கேசவானந்த பாரதி எதிர் கேரள அரசு (1973)",
        "A.D.M. Jabalpur v. Shivkant Shukla (1976)", "ஏ.டி.எம். ஜபல்பூர் எதிர் சிவகாந்த் சுக்லா (1976)",
        "Minerva Mills v. Union of India (1980)", "மினர்வா மில்ஸ் எதிர் இந்திய ஒன்றியம் (1980)",
        "Indira Nehru Gandhi v. Raj Narain (1975)", "இந்திரா நேரு காந்தி எதிர் ராஜ் நாராயண் (1975)",
        "C",
        "In the Minerva Mills case (1980), the Supreme Court observed that there is no bar to judicial review of the validity of a proclamation of National Emergency issued under Article 352, particularly if it is shown to be malafide or based on wholly extraneous and irrelevant grounds.",
        "மினர்வா மில்ஸ் வழக்கில் (1980), சரத்து 352-ன் கீழ் பிறப்பிக்கப்பட்ட தேசிய அவசரநிலைப் பிரகடனம் தவறான உள்நோக்கம் கொண்டது என்றோ அல்லது முற்றிலும் தொடர்பற்ற காரணங்களை அடிப்படையாகக் கொண்டது என்றோ நிரூபிக்கப்பட்டால் நீதித்துறை மறுஆய்வுக்கு எந்தத் தடையும் இல்லை என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
        "Option A established the Basic Structure doctrine in constitutional amendments.", "விருப்பம் A அரசியலமைப்பு திருத்தங்களில் அடிப்படைக் கட்டமைப்பு கோட்பாட்டை நிறுவியது.",
        "Option B (Habeas Corpus case) notoriously held that courts could not issue habeas corpus during emergency (later overruled).", "விருப்பம் B ஆட்கொணர்வு மனு வழக்கில் அவசரநிலையின் போது நீதிமன்றங்கள் தலையிட முடியாது என்று தீர்ப்பளித்தது (பின்னர் மாற்றப்பட்டது).",
        "Option C is correct; Minerva Mills (1980) firmly affirmed judicial review of Article 352 proclamations.", "விருப்பம் C சரியானது; மினர்வா மில்ஸ் வழக்கு சரத்து 352-ன் மீதான நீதித்துறை மறுஆய்வை உறுதிப்படுத்தியது.",
        "Option D dealt primarily with election disputes and basic structure.", "விருப்பம் D தேர்தல் தகராறுகள் மற்றும் அடிப்படைக் கட்டமைப்பு தொடர்பானது.",
        "Minerva Mills (1980) = Proclamation of National Emergency is subject to Judicial Review if tainted by malafide.",
        "மினர்வா மில்ஸ் (1980) = உள்நோக்கம் கொண்டதாக இருந்தால் தேசிய அவசரநிலைப் பிரகடனம் நீதித்துறை மறுஆய்வுக்கு உட்பட்டது.",
        "The 44th Amendment had already repealed the 38th Amendment clause that barred judicial review, and Minerva Mills affirmed this.",
        "நீதித்துறை மறுஆய்வைத் தடுத்த 38-வது திருத்த விதியை 44-வது திருத்தம் நீக்கியது, மினர்வா மில்ஸ் வழக்கு அதை உறுதிப்படுத்தியது."
    ))

    # 008 - Key D
    qs.append(make_ep_q(
        PREFIX, 8, DIFF, "Constitutional Mechanics", "Executive and Legislative Consequences",
        "During the operation of a National Emergency, how are the executive powers of the Centre in relation to a State modified under Article 353(a)?",
        "தேசிய அவசரநிலை அமலில் இருக்கும் போது, சரத்து 353(a)-ன் கீழ் ஒரு மாநிலம் தொடர்பாக மத்திய அரசின் நிர்வாக அதிகாரங்கள் எவ்வாறு மாற்றியமைக்கப்படுகின்றன?",
        "The State government is automatically dismissed.", "மாநில அரசு தானாகவே கலைக்கப்படுகிறது.",
        "The Governor assumes direct administration of the State under the President's instructions.", "ஆளுநர் குடியரசுத் தலைவரின் அறிவுறுத்தலின் கீழ் மாநிலத்தின் நேரடி நிர்வாகத்தை ஏற்கிறார்.",
        "The executive powers of the State are completely suspended.", "மாநிலத்தின் நிர்வாக அதிகாரங்கள் முற்றிலும் இடைநிறுத்தப்படுகின்றன.",
        "The Centre becomes entitled to give executive directions to a State on 'any' matter, but the State government is not suspended.", "மத்திய அரசு ஒரு மாநிலத்திற்கு 'எந்த' விவகாரத்திலும் நிர்வாக வழிகாட்டுதல்களை வழங்க உரிமை பெறுகிறது, ஆனால் மாநில அரசு இடைநிறுத்தப்படுவதில்லை.",
        "D",
        "Under Article 353(a), during a National Emergency, the executive power of the Union extends to giving directions to any State as to the manner in which its executive power is to be exercised on ANY matter. Crucially, the State government is NOT suspended or dismissed (unlike under President's Rule); it remains in office under the complete executive control of the Centre.",
        "சரத்து 353(a)-ன் கீழ், தேசிய அவசரநிலையின் போது எந்தவொரு விவகாரத்திலும் மாநில அரசு தனது நிர்வாக அதிகாரத்தை எவ்வாறு செயல்படுத்த வேண்டும் என்று வழிகாட்டும் அதிகாரம் மத்திய அரசுக்கு உண்டு. மிக முக்கியமாக, மாநில அரசு இடைநிறுத்தப்படவோ கலைக்கப்படவோ மாட்டாது; அது மத்திய அரசின் முழுக் கட்டுப்பாட்டின் கீழ் தொடர்ந்து செயல்படும்.",
        "Option A describes President's Rule (Article 356), not National Emergency.", "விருப்பம் A குடியரசுத் தலைவர் ஆட்சியை (சரத்து 356) விவரிக்கிறது, தேசிய அவசரநிலையை அல்ல.",
        "Option B also describes President's Rule mechanics.", "விருப்பம் B-யும் குடியரசுத் தலைவர் ஆட்சி நடைமுறையை விவரிக்கிறது.",
        "Option C is false; state executive is not suspended, only subordinated to central directions.", "விருப்பம் C தவறு; மாநில நிர்வாகம் இடைநிறுத்தப்படுவதில்லை, மத்திய வழிகாட்டுதல்களுக்கு உட்படுத்தப்படுகிறது.",
        "Option D accurately captures the non-suspension principle under Article 353(a).", "விருப்பம் D சரத்து 353(a)-ன் கீழ் நிர்வாகம் இடைநிறுத்தப்படாது என்ற கொள்கையைத் துல்லியமாக விளக்குகிறது.",
        "Crucial TNPSC Distinction: In National Emergency, State Government is NOT dismissed (Centre directs it). In President's Rule, State Council of Ministers IS dismissed.",
        "முக்கியமான TNPSC வேறுபாடு: தேசிய அவசரநிலையில் மாநில அரசு கலைக்கப்படுவதில்லை (மத்திய அரசு வழிகாட்டுகிறது). குடியரசுத் தலைவர் ஆட்சியில் அமைச்சரவை கலைக்கப்படுகிறது.",
        "This maintains state operational continuity while placing legislative and administrative levers with the Union.",
        "இது மாநில செயல்பாட்டுத் தொடர்ச்சியைப் பராமரிக்கும் அதே வேளையில் சட்ட மற்றும் நிர்வாக அதிகாரங்களை மத்திய அரசிடம் வைக்கிறது."
    ))

    # 009 - Key A
    qs.append(make_ep_q(
        PREFIX, 9, DIFF, "Legislative Powers", "National Emergency - State List",
        "When a proclamation of National Emergency is in force, Parliament acquires concurrent power to legislate on subjects enumerated in the State List under Article 250. What happens to laws enacted by Parliament under this power once the emergency ceases to operate?",
        "தேசிய அவசரநிலைப் பிரகடனம் அமலில் இருக்கும் போது, சரத்து 250-ன் கீழ் மாநிலப் பட்டியலில் உள்ள விவகாரங்கள் மீது சட்டம் இயற்றும் அதிகாரத்தை பாராளுமன்றம் பெறுகிறது. அவசரநிலை முடிவுக்கு வந்த பிறகு பாராளுமன்றம் இயற்றிய அந்தச் சட்டங்களுக்கு என்ன நேரிடும்?",
        "They cease to have effect on the expiration of 6 months after the proclamation ceases to operate.", "பிரகடனம் முடிவுக்கு வந்த 6 மாதங்கள் முடிந்தவுடன் அவை காலாவதியாகிவிடும்.",
        "They cease to have effect immediately upon revocation of the proclamation.", "பிரகடனம் திரும்பப் பெறப்பட்ட உடனேயே அவை காலாவதியாகிவிடும்.",
        "They remain in force permanently unless explicitly repealed by the State Legislature.", "மாநில சட்டமன்றத்தால் வெளிப்படையாக ரத்து செய்யப்படும் வரை அவை நிரந்தரமாக அமலில் இருக்கும்.",
        "They cease to have effect on the expiration of 1 year after the proclamation ceases.", "பிரகடனம் முடிவுக்கு வந்த 1 வருடம் முடிந்தவுடன் அவை காலாவதியாகிவிடும்.",
        "A",
        "According to Article 250(2), a law made by Parliament which Parliament would not but for the issue of a proclamation of emergency have been competent to make shall cease to have effect on the expiration of a period of six months after the proclamation has ceased to operate, except as respects things done or omitted to be done before the expiration of the said period.",
        "சரத்து 250(2)-ன் படி, அவசரநிலைப் பிரகடனம் அமலில் இல்லாதிருந்தால் பாராளுமன்றம் இயற்ற இயலாத ஒரு சட்டம், அவசரநிலை முடிவுக்கு வந்த பிறகு ஆறு மாத கால அவகாசம் முடிந்தவுடன் தானாகவே காலாவதியாகிவிடும்.",
        "Option A is the exact constitutional duration stipulated under Article 250(2).", "விருப்பம் A என்பது சரத்து 250(2)-ன் கீழ் குறிப்பிடப்பட்டுள்ள சரியான அரசியலமைப்பு கால அளவாகும்.",
        "Option B is incorrect; there is a 6-month transitional cushion.", "விருப்பம் B தவறானது; 6 மாத கால மாறுதல் அவகாசம் உள்ளது.",
        "Option C describes the post-42nd Amendment rule for laws enacted under President's Rule (Article 356), not Article 250!", "விருப்பம் C குடியரசுத் தலைவர் ஆட்சியின் கீழ் இயற்றப்பட்ட சட்டங்களுக்குப் பொருந்தும், சரத்து 250-க்கு அல்ல!",
        "Option D (1 year) is not the constitutional sunset period under Article 250.", "விருப்பம் D (1 ஆண்டு) சரத்து 250-ன் கீழ் உள்ள காலாவதி காலம் அல்ல.",
        "Sunset Clause Rule: Art 250 laws made by Parliament during National Emergency expire 6 months after emergency ends.",
        "காலாவதி விதி: தேசிய அவசரநிலையின் போது பாராளுமன்றத்தால் இயற்றப்பட்ட சரத்து 250 சட்டங்கள் அவசரநிலை முடிந்த 6 மாதங்களில் காலாவதியாகிவிடும்.",
        "State legislatures can also make laws on the same State subject during this time, but in case of repugnancy, Union law prevails.",
        "இக்காலத்தில் மாநில சட்டமன்றங்களும் அதே துறையில் சட்டம் இயற்றலாம், ஆனால் முரண்பாடு ஏற்பட்டால் மத்திய சட்டமே மேலோங்கும்."
    ))

    # 010 - Key B
    qs.append(make_ep_q(
        PREFIX, 10, DIFF, "Constitutional Terminology", "Word 'Cabinet' in Constitution",
        "The word 'Cabinet' appears in only ONE Article in the entire Constitution of India. Which Article is it, and which Amendment inserted it?",
        "இந்திய அரசியலமைப்பு முழுவதிலும் 'கேபினட்' (அமைச்சரவை) என்ற சொல் ஒரே ஒரு சரத்தில் மட்டுமே இடம்பெற்றுள்ளது. அது எந்த சரத்து, எந்த திருத்தத்தின் மூலம் அது சேர்க்கப்பட்டது?",
        "Article 74, inserted by 42nd Amendment Act 1976", "சரத்து 74, 1976-ன் 42-வது திருத்தச் சட்டத்தால் சேர்க்கப்பட்டது",
        "Article 352, inserted by 44th Amendment Act 1978", "சரத்து 352, 1978-ன் 44-வது திருத்தச் சட்டத்தால் சேர்க்கப்பட்டது",
        "Article 75, inserted by 91st Amendment Act 2003", "சரத்து 75, 2003-ன் 91-வது திருத்தச் சட்டத்தால் சேர்க்கப்பட்டது",
        "Article 356, inserted by 44th Amendment Act 1978", "சரத்து 356, 1978-ன் 44-வது திருத்தச் சட்டத்தால் சேர்க்கப்பட்டது",
        "B",
        "The word 'Cabinet' was nowhere defined in the original Constitution. It was introduced into Article 352(3) by the 44th Constitutional Amendment Act 1978, defining it as 'the Council consisting of the Prime Minister and other Ministers of Cabinet rank under Article 75', requiring their written advice to proclaim emergency.",
        "'கேபினட்' என்ற சொல் மூல அரசியலமைப்பில் எங்குமே வரையறுக்கப்படவில்லை. 1978-ன் 44-வது அரசியலமைப்பு திருத்தச் சட்டத்தின் மூலம் சரத்து 352(3)-ல் அது சேர்க்கப்பட்டது. பிரதமர் மற்றும் சரத்து 75-ன் கீழ் கேபினட் அந்தஸ்து கொண்ட பிற அமைச்சர்களைக் கொண்ட குழு என அது வரையறுக்கப்பட்டது.",
        "Option A is incorrect; Article 74 uses 'Council of Ministers', not 'Cabinet'.", "விருப்பம் A தவறானது; சரத்து 74 'அமைச்சரவைக் குழு' (Council of Ministers) என்ற சொல்லைப் பயன்படுத்துகிறது.",
        "Option B is fully correct; Article 352(3) by 44th CAA is unique in using the term 'Cabinet'.", "விருப்பம் B முற்றிலும் சரியானது; 44-வது திருத்தத்தின் மூலம் சரத்து 352(3)-ல் மட்டுமே 'கேபினட்' என்ற சொல் உள்ளது.",
        "Option C limited the size of Council of Ministers to 15%, but did not introduce the word Cabinet in Art 75.", "விருப்பம் C அமைச்சரவையின் அளவை 15% ஆகக் கட்டுப்படுத்தியது, ஆனால் கேபினட் என்ற சொல்லைச் சேர்க்கவில்லை.",
        "Option D does not contain the word Cabinet.", "விருப்பம் D கேபினட் என்ற சொல்லைக் கொண்டிருக்கவில்லை.",
        "Top TNPSC Question: Word 'Cabinet' exists ONLY in Article 352(3), introduced by the 44th Amendment (1978).",
        "முக்கிய TNPSC கேள்வி: 'கேபினட்' என்ற சொல் 44-வது திருத்தத்தால் (1978) சேர்க்கப்பட்டு சரத்து 352(3)-ல் மட்டுமே உள்ளது.",
        "This ensures that the Prime Minister cannot unilaterally advise an emergency without the collective written assent of cabinet ministers.",
        "பிரதமர் தன்னிச்சையாக முடிவெடுப்பதைத் தடுத்து, கேபினட் அமைச்சர்களின் கூட்டு எழுத்துப்பூர்வ ஒப்புதலைப் பெற இது வகைசெய்கிறது."
    ))

    # 011 - Key C
    qs.append(make_ep_q(
        PREFIX, 11, DIFF, "President's Rule - Mechanics", "Article 356 - Basis and Grounds",
        "Under Article 356, on what dual grounds can the President issue a proclamation imposing President's Rule in a State?",
        "சரத்து 356-ன் கீழ், எந்த இரு அடிப்படை வழிகளில் ஒரு மாநிலத்தில் குடியரசுத் தலைவர் ஆட்சியை அமல்படுத்தி குடியரசுத் தலைவர் பிரகடனம் வெளியிடலாம்?",
        "Only upon receipt of a report from the Governor of the State under Article 356", "சரத்து 356-ன் கீழ் மாநில ஆளுநரிடமிருந்து அறிக்கை பெற்றால் மட்டுமே",
        "Only when the Union Council of Ministers passes a unanimous resolution", "மத்திய அமைச்சரவை ஒருமனதாக தீர்மானம் நிறைவேற்றினால் மட்டுமே",
        "Either on receipt of a report from the Governor under Article 356 or 'otherwise' (suo motu), or due to failure to comply with Union directions under Article 365", "சரத்து 356-ன் கீழ் ஆளுநர் அறிக்கை அடிப்படையிலோ அல்லது 'பிற வழியிலோ' (தானாக முன்வந்து), அல்லது சரத்து 365-ன் கீழ் மத்திய வழிகாட்டுதல்களைப் பின்பற்றத் தவறும் போதோ",
        "Only after prior approval of both Houses of Parliament by a two-thirds majority", "பாராளுமன்றத்தின் இரு அவைகளிலும் மூன்றில் இரண்டு பங்கு பெரும்பான்மையுடன் முன் ஒப்புதல் பெற்ற பிறகு மட்டுமே",
        "C",
        "A proclamation under Article 356 can be issued on two distinct grounds: (1) Under Article 356 itself, if the President is satisfied based on a report of the Governor or 'otherwise' that government of the State cannot be carried on in accordance with the Constitution; and (2) Under Article 365, if any State fails to comply with or give effect to any directions given by the Union.",
        "சரத்து 356-ன் கீழ் பிரகடனம் இரு வழிகளில் வெளியிடப்படலாம்: (1) சரத்து 356-ன் கீழ் ஆளுநரின் அறிக்கை மூலமாகவோ அல்லது 'வேறு விதமாகவோ' மாநில அரசு அரசியலமைப்பு விதிகளின்படி இயங்க முடியாது என்று குடியரசுத் தலைவர் திருப்தியடைவது; (2) சரத்து 365-ன் கீழ் மத்திய அரசின் வழிகாட்டுதல்களை ஒரு மாநிலம் பின்பற்றத் தவறினால்.",
        "Option A is incomplete because the President can act 'otherwise' (without Governor's report).", "விருப்பம் A முழுமையற்றது, ஏனெனில் ஆளுநர் அறிக்கை இன்றியும் ('வேறு விதமாகவும்') குடியரசுத் தலைவர் செயல்படலாம்.",
        "Option B is not the constitutional mechanism.", "விருப்பம் B அரசியலமைப்பு நடைமுறை அல்ல.",
        "Option C correctly mentions both Article 356 ('Governor or otherwise') and Article 365.", "விருப்பம் C சரத்து 356 ('ஆளுநர் அல்லது வேறுவிதமாக') மற்றும் சரத்து 365 இரண்டையும் சரியாகக் குறிப்பிடுகிறது.",
        "Option D is false; parliamentary approval is required within 2 months AFTER proclamation, not before.", "விருப்பம் D தவறு; பாராளுமன்ற ஒப்புதல் பிரகடனத்திற்கு முன் அல்ல, பின்னர் 2 மாதங்களுக்குள் தேவைப்படுகிறது.",
        "The words 'or otherwise' in Article 356 mean the President is not bound solely by the Governor's report.",
        "சரத்து 356-ல் உள்ள 'அல்லது வேறு விதமாக' என்ற சொல் குடியரசுத் தலைவர் ஆளுநரின் அறிக்கைக்கு மட்டுமே கட்டுப்பட்டவர் அல்ல என்பதைக் குறிக்கிறது.",
        "Article 365 acts as a bridge triggering Article 356 when state authorities defy binding central directives.",
        "மத்திய அரசின் கட்டாய வழிகாட்டுதல்களை மாநிலங்கள் மீறும் போது சரத்து 365 சரத்து 356-ஐத் தூண்டும் பாலமாகச் செயல்படுகிறது."
    ))

    # 012 - Key D
    qs.append(make_ep_q(
        PREFIX, 12, DIFF, "President's Rule - Approval", "Majority and Approval Duration",
        "What is the time period within which a proclamation of President's Rule (Article 356) must be approved by Parliament, and by what type of majority?",
        "சரத்து 356-ன் கீழ் குடியரசுத் தலைவர் ஆட்சிப் பிரகடனம் பாராளுமன்றத்தால் எத்தனை காலத்திற்குள் மற்றும் எந்த வகையான பெரும்பான்மையால் அங்கீகரிக்கப்பட வேண்டும்?",
        "Within 1 month, by Special Majority", "1 மாதத்திற்குள், சிறப்புப் பெரும்பான்மையால்",
        "Within 1 month, by Simple Majority", "1 மாதத்திற்குள், எளிய பெரும்பான்மையால்",
        "Within 2 months, by Special Majority", "2 மாதங்களுக்குள், சிறப்புப் பெரும்பான்மையால்",
        "Within 2 months, by Simple Majority", "2 மாதங்களுக்குள், எளிய பெரும்பான்மையால்",
        "D",
        "Under Article 356(3), a proclamation imposing President's Rule must be approved by both Houses of Parliament within TWO MONTHS from the date of its issue, and by a SIMPLE MAJORITY (majority of members present and voting) in each House.",
        "சரத்து 356(3)-ன் கீழ், குடியரசுத் தலைவர் ஆட்சிப் பிரகடனம் அது வெளியிடப்பட்ட நாளிலிருந்து இரண்டு மாதங்களுக்குள் பாராளுமன்றத்தின் இரு அவைகளாலும் எளிய பெரும்பான்மை (வருகை தந்து வாக்களிக்கும் உறுப்பினர்களின் பெரும்பான்மை) மூலம் அங்கீகரிக்கப்பட வேண்டும்.",
        "Option A (1 month, Special Majority) applies to National Emergency under Article 352.", "விருப்பம் A (1 மாதம், சிறப்புப் பெரும்பான்மை) சரத்து 352-ன் கீழ் தேசிய அவசரநிலைக்குப் பொருந்தும்.",
        "Option B is incorrect regarding the 1-month window.", "விருப்பம் B 1 மாத காலக்கெடு சார்ந்து தவறானது.",
        "Option C is incorrect because President's Rule never requires a special majority.", "விருப்பம் C தவறானது ஏனெனில் குடியரசுத் தலைவர் ஆட்சிக்கு சிறப்புப் பெரும்பான்மை தேவையில்லை.",
        "Option D is fully accurate: 2 months and simple majority.", "விருப்பம் D முற்றிலும் சரியானது: 2 மாதங்கள் மற்றும் எளிய பெரும்பான்மை.",
        "Memorize the '1-2-2 Rule': Art 352 = 1 Month (Special Maj); Art 356 = 2 Months (Simple Maj); Art 360 = 2 Months (Simple Maj).",
        "'1-2-2 விதியை' நினைவில் கொள்க: சரத்து 352 = 1 மாதம் (சிறப்புப் பெரும்பான்மை); சரத்து 356 = 2 மாதங்கள் (எளிய பெரும்பான்மை); சரத்து 360 = 2 மாதங்கள் (எளிய பெரும்பான்மை).",
        "Only Article 352 demands the stringent special majority; Articles 356 and 360 require only ordinary simple majorities.",
        "சரத்து 352 மட்டுமே கடுமையான சிறப்புப் பெரும்பான்மையைக் கோருகிறது; 356 மற்றும் 360-க்கு எளிய பெரும்பான்மை போதுமானது."
    ))

    # 013 - Key A
    qs.append(make_ep_q(
        PREFIX, 13, DIFF, "President's Rule - Extension", "Beyond 1 Year Conditionality",
        "Under the 44th Constitutional Amendment Act 1978, President's Rule can be extended beyond one year (up to a maximum of 3 years) only if which of the following conditions is satisfied?",
        "1978-ன் 44-வது அரசியலமைப்பு திருத்தச் சட்டத்தின்படி, பின்வரும் எந்த நிபந்தனை பூர்த்தி செய்யப்பட்டால் மட்டுமே குடியரசுத் தலைவர் ஆட்சியை ஒரு வருடத்திற்கு மேல் (அதிகபட்சம் 3 ஆண்டுகள் வரை) நீட்டிக்க முடியும்?",
        "A National Emergency is in operation in whole of India or in whole/any part of the State, AND the Election Commission certifies that elections cannot be held", "இந்தியா முழுவதிலும் அல்லது மாநிலம் முழுவதிலும்/பகுதியிலும் தேசிய அவசரநிலை அமலில் இருக்க வேண்டும் மற்றும் தேர்தல் நடத்த இயலாது என தேர்தல் ஆணையம் சான்றளிக்க வேண்டும்",
        "The Governor submits a special report requesting extension for an additional 2 years", "கூடுதல் 2 ஆண்டுகளுக்கு நீட்டிப்பு கோரி ஆளுநர் சிறப்பு அறிக்கையை சமர்ப்பிக்க வேண்டும்",
        "Both Houses of Parliament pass a resolution by a 2/3rd special majority", "பாராளுமன்றத்தின் இரு அவைகளும் 2/3 பங்கு சிறப்புப் பெரும்பான்மையுடன் தீர்மானம் நிறைவேற்ற வேண்டும்",
        "The Supreme Court of India issues an advisory opinion upholding the necessity of extension", "நீட்டிப்பின் அவசியத்தை உறுதிப்படுத்தி இந்திய உச்ச நீதிமன்றம் ஆலோசனைக் கருத்து வழங்க வேண்டும்",
        "A",
        "Article 356(5), introduced by the 44th Amendment Act 1978, restricts extensions beyond one year to 6 months at a time up to a maximum of 3 years ONLY if two conditions co-exist: (1) A proclamation of National Emergency is in operation in the whole of India or in the whole or any part of the State; and (2) The Election Commission certifies that continuation of President's Rule is necessary on account of difficulties in holding general elections to the Legislative Assembly of the State.",
        "44-வது திருத்தச் சட்டம் அறிமுகப்படுத்திய சரத்து 356(5)-ன் படி, இரு நிபந்தனைகள் ஒரே நேரத்தில் பூர்த்தியானால் மட்டுமே குடியரசுத் தலைவர் ஆட்சியை ஒரு ஆண்டுக்கு மேல் நீட்டிக்க முடியும்: (1) நாடு முழுவதிலும் அல்லது அந்த மாநிலத்தின் ஏதேனும் ஒரு பகுதியிலும் தேசிய அவசரநிலை அமலில் இருக்க வேண்டும்; மற்றும் (2) சட்டமன்றத் தேர்தலை நடத்துவதில் உள்ள சிரமங்கள் காரணமாக நீட்டிப்பு அவசியம் என்று தேர்தல் ஆணையம் சான்றளிக்க வேண்டும்.",
        "Option A accurately states both twin mandatory constitutional conditions.", "விருப்பம் A கட்டாய அரசியலமைப்பு இரட்டை நிபந்தனைகளைத் துல்லியமாகக் குறிப்பிடுகிறது.",
        "Option B is incorrect; Governor's request alone cannot bypass the 1-year constitutional bar.", "விருப்பம் B தவறானது; ஆளுநரின் கோரிக்கை மட்டும் 1 ஆண்டு அரசியலமைப்பு தடையைத் தாண்ட முடியாது.",
        "Option C is incorrect; parliamentary majority type does not bypass this constitutional barrier.", "விருப்பம் C தவறானது; பெரும்பான்மை வகை இந்த அரசியலமைப்பு தடையைத் தளர்த்தாது.",
        "Option D is irrelevant to Article 356(5).", "விருப்பம் D சரத்து 356(5)-க்கு பொருத்தமற்றது.",
        "Article 356(5) Twin Test: (1) National Emergency in whole/part of State + (2) Election Commission certification.",
        "சரத்து 356(5) இரட்டைத் தேர்வு: (1) மாநிலத்தில்/நாட்டில் தேசிய அவசரநிலை + (2) தேர்தல் ஆணையத்தின் சான்றளிப்பு.",
        "This prevents the ruling party at the Centre from indefinitely delaying state assembly elections.",
        "மத்தியில் ஆளும் கட்சி மாநில சட்டமன்றத் தேர்தலை காலவரையின்றி தாமதப்படுத்துவதை இது தடுக்கிறது."
    ))

    # 014 - Key B
    qs.append(make_ep_q(
        PREFIX, 14, DIFF, "Constitutional Law", "S.R. Bommai Guidelines (1994)",
        "In the landmark S.R. Bommai v. Union of India (1994) judgment, the Supreme Court laid down which critical rule regarding the dissolution of a State Legislative Assembly under President's Rule?",
        "எஸ்.ஆர். பொம்மை எதிர் இந்திய ஒன்றியம் (1994) வரலாற்றுச் சிறப்புமிக்க வழக்கில், குடியரசுத் தலைவர் ஆட்சியின் கீழ் மாநில சட்டமன்றத்தைக் கலைப்பது தொடர்பாக உச்ச நீதிமன்றம் எந்த முக்கியமான விதியை வகுத்தது?",
        "The Assembly can be dissolved immediately as soon as the President issues the proclamation under Article 356.", "சரத்து 356-ன் கீழ் குடியரசுத் தலைவர் பிரகடனம் வெளியிட்ட உடனேயே சட்டமன்றத்தைக் கலைத்துவிடலாம்.",
        "The Assembly should not be dissolved until Parliament approves the proclamation; until then, it can only be kept in suspended animation.", "பாராளுமன்றம் பிரகடனத்திற்கு ஒப்புதல் அளிக்கும் வரை சட்டமன்றத்தைக் கலைக்கக் கூடாது; அதுவரை அதை தற்காலிகமாக மட்டுமே நிறுத்தி வைக்க முடியும்.",
        "The Assembly can never be dissolved; only fresh elections after 3 years can replace it.", "சட்டமன்றத்தை ஒருபோதும் கலைக்க முடியாது; 3 ஆண்டுகளுக்குப் பிறகான புதிய தேர்தல் மட்டுமே அதை மாற்ற முடியும்.",
        "The Governor alone has the final discretionary power to dissolve the Assembly without Union approval.", "மத்திய அரசின் ஒப்புதல் இன்றி சட்டமன்றத்தைக் கலைக்க ஆளுநருக்கு மட்டுமே இறுதி தன்னுரிமை அதிகாரம் உண்டு.",
        "B",
        "In S.R. Bommai (1994), the Supreme Court ruled that the State Legislative Assembly should not be dissolved until the proclamation of President's Rule is approved by both Houses of Parliament. Until approval, the President can only keep the Assembly in suspended animation. If Parliament rejects the proclamation, the dismissed ministry and suspended assembly are revived.",
        "எஸ்.ஆர். பொம்மை (1994) வழக்கில், குடியரசுத் தலைவர் ஆட்சிப் பிரகடனத்திற்கு பாராளுமன்றத்தின் இரு அவைகளும் ஒப்புதல் அளிக்கும் வரை சட்டமன்றத்தைக் கலைக்கக் கூடாது என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது. ஒப்புதல் கிடைக்கும் வரை சட்டமன்றத்தை இடைநிறுத்தி மட்டுமே வைக்க முடியும். பாராளுமன்றம் நிராகரித்தால் அமைச்சரவையும் சட்டமன்றமும் மீண்டும் உயிர்பெறும்.",
        "Option A was the pre-Bommai abusive practice that the Supreme Court explicitly struck down.", "விருப்பம் A என்பது பொம்மை வழக்கிற்கு முந்தைய தவறான நடைமுறை, அதை உச்ச நீதிமன்றம் தடை செய்தது.",
        "Option B is the precise landmark principle formulated in S.R. Bommai.", "விருப்பம் B என்பது எஸ்.ஆர். பொம்மை வழக்கில் வகுக்கப்பட்ட துல்லியமான கொள்கையாகும்.",
        "Option C is factually incorrect.", "விருப்பம் C தவறானது.",
        "Option D violates Article 356 constitutional scheme.", "விருப்பம் D சரத்து 356 அரசியலமைப்புத் திட்டத்தை மீறுகிறது.",
        "Bommai Milestone: No dissolution of Assembly until Parliament approves! Only suspended animation allowed initially.",
        "பொம்மை மைல்கல்: பாராளுமன்றம் ஒப்புதல் அளிக்கும் வரை சட்டமன்றத்தைக் கலைக்கக் கூடாது! ஆரம்பத்தில் தற்காலிக இடைநிறுத்தம் மட்டுமே அனுமதிக்கப்படும்.",
        "If the proclamation fails in Parliament, the status quo ante is restored and the assembly is revived.",
        "பாராளுமன்றத்தில் பிரகடனம் தோல்வியடைந்தால், பழைய நிலையே மீட்டெடுக்கப்பட்டு சட்டமன்றம் மீண்டும் உயிர்ப்பிக்கப்படும்."
    ))

    # 015 - Key C
    qs.append(make_ep_q(
        PREFIX, 15, DIFF, "President's Rule - High Courts", "High Court Immunity under Article 356",
        "When President's Rule is imposed in a State under Article 356, what is the constitutional position regarding the powers of the State High Court?",
        "சரத்து 356-ன் கீழ் ஒரு மாநிலத்தில் குடியரசுத் தலைவர் ஆட்சி அமல்படுத்தப்படும் போது, மாநில உயர் நீதிமன்றத்தின் அதிகாரங்கள் குறித்த அரசியலமைப்பு நிலை என்ன?",
        "The High Court's powers are automatically transferred to the Supreme Court of India.", "உயர் நீதிமன்றத்தின் அதிகாரங்கள் தானாகவே இந்திய உச்ச நீதிமன்றத்திற்கு மாற்றப்படும்.",
        "The President assumes all powers vested in or exercisable by the High Court.", "உயர் நீதிமன்றத்திற்கு உள்ள அல்லது அதனால் பயன்படுத்தக்கூடிய அனைத்து அதிகாரங்களையும் குடியரசுத் தலைவர் ஏற்றுக்கொள்கிறார்.",
        "The President cannot assume the powers vested in or exercisable by the High Court, nor suspend any constitutional provision relating to it.", "உயர் நீதிமன்றத்திற்கு உள்ள அதிகாரங்களை குடியரசுத் தலைவர் ஏற்க முடியாது, அத்துடன் அது தொடர்பான எந்தவொரு அரசியலமைப்பு விதியையும் இடைநிறுத்த முடியாது.",
        "The Governor exercises judicial powers of the High Court on behalf of the President.", "குடியரசுத் தலைவரின் சார்பில் உயர் நீதிமன்றத்தின் நீதித்துறை அதிகாரங்களை ஆளுநர் செயல்படுத்துகிறார்.",
        "C",
        "Article 356(1) proviso explicitly states that nothing in this clause shall authorise the President to assume to himself any of the powers vested in or exercisable by a High Court, or to suspend in whole or in part the operation of any provision of this Constitution relating to High Courts.",
        "சரத்து 356(1)-ன் நிபந்தனை விதியின்படி, உயர் நீதிமன்றத்திற்கு உள்ள அதிகாரங்களை குடியரசுத் தலைவர் தமதாக்கிக் கொள்ளவோ அல்லது உயர் நீதிமன்றங்கள் தொடர்பான அரசியலமைப்பின் எந்தவொரு விதியின் செயல்பாட்டையும் முழுமையாகவோ பகுதியாகவோ இடைநிறுத்தவோ இச்சரத்து அதிகாரம் அளிக்காது.",
        "Option A is false; High Court functions normally within its jurisdiction.", "விருப்பம் A தவறு; உயர் நீதிமன்றம் வழக்கம் போல் தனது அதிகார வரம்பிற்குள் இயங்கும்.",
        "Option B directly contradicts the explicit proviso to Article 356(1).", "விருப்பம் B சரத்து 356(1)-ன் நிபந்தனை விதிக்கு முற்றிலும் எதிரானது.",
        "Option C is the exact constitutional mandate protecting High Court independence during President's Rule.", "விருப்பம் C குடியரசுத் தலைவர் ஆட்சியின் போது உயர் நீதிமன்ற சுதந்திரத்தைப் பாதுகாக்கும் சரியான விதியாகும்.",
        "Option D is unconstitutional; executive cannot exercise High Court judicial powers.", "விருப்பம் D அரசியலமைப்பிற்கு எதிரானது; நிர்வாகம் உயர் நீதிமன்ற நீதித்துறை அதிகாரங்களைப் பயன்படுத்த முடியாது.",
        "TNPSC Favorite Trap: During President's Rule, High Court powers are NEVER touched or assumed by the President.",
        "TNPSC முக்கிய பொறி: குடியரசுத் தலைவர் ஆட்சியின் போது உயர் நீதிமன்ற அதிகாரங்களை குடியரசுத் தலைவர் ஒருபோதும் தொடவோ ஏற்கவோ முடியாது.",
        "The judiciary stands completely independent and unaffected during Article 356 proclamations.",
        "சரத்து 356 பிரகடனங்களின் போது நீதித்துறை முற்றிலும் சுதந்திரமாகவும் பாதிக்கப்படாமலும் நிற்கிறது."
    ))

    # 016 - Key D
    qs.append(make_ep_q(
        PREFIX, 16, DIFF, "President's Rule - Legislative Output", "Fate of Laws post-President's Rule",
        "What happens to a law enacted by Parliament (or the President) for a State during the operation of President's Rule after the proclamation ceases to operate?",
        "குடியரசுத் தலைவர் ஆட்சியின் போது ஒரு மாநிலத்திற்காக பாராளுமன்றம் (அல்லது குடியரசுத் தலைவர்) இயற்றிய சட்டம், பிரகடனம் முடிவுக்கு வந்த பிறகு என்னவாகும்?",
        "It lapses automatically on the day President's Rule ends.", "குடியரசுத் தலைவர் ஆட்சி முடிவடையும் நாளில் அது தானாகவே காலாவதியாகிவிடும்.",
        "It lapses exactly six months after the proclamation ceases to operate.", "பிரகடனம் முடிவுக்கு வந்த சரியாக ஆறு மாதங்களுக்குப் பிறகு அது காலாவதியாகிவிடும்.",
        "It requires mandatory re-enactment by the State Legislature within 30 days to survive.", "அது நீடிக்க மாநில சட்டமன்றத்தால் 30 நாட்களுக்குள் கட்டாயமாக மீண்டும் இயற்றப்பட வேண்டும்.",
        "It continues to remain in force until altered, repealed, or amended by the State Legislature.", "மாநில சட்டமன்றத்தால் மாற்றப்படும், ரத்து செய்யப்படும் அல்லது திருத்தப்படும் வரை அது தொடர்ந்து அமலில் இருக்கும்.",
        "D",
        "Prior to the 42nd Amendment Act 1976, laws made during President's Rule lapsed after one year from cessation. However, the 42nd Amendment altered this rule: now, any law made by Parliament or the President for a State during President's Rule CONTINUES IN FORCE even after the proclamation ceases, until it is altered, repealed, or amended by the State Legislature.",
        "1976-ன் 42-வது திருத்தத்திற்கு முன்பு, இச்சட்டங்கள் ஆட்சி முடிந்து 1 ஆண்டில் காலாவதியாயின. ஆனால் 42-வது திருத்தத்திற்குப் பிறகு: குடியரசுத் தலைவர் ஆட்சியில் இயற்றப்பட்ட எந்தவொரு சட்டமும் ஆட்சி முடிந்த பிறகும் தொடர்ந்து அமலில் இருக்கும்; மாநில சட்டமன்றம் அதை மாற்றும், ரத்து செய்யும் அல்லது திருத்தும் வரை அது நீடிக்கும்.",
        "Option A is incorrect; it does not lapse automatically.", "விருப்பம் A தவறானது; அது தானாகக் காலாவதியாகாது.",
        "Option B confuses this with Article 250 (National Emergency sunset clause of 6 months).", "விருப்பம் B சரத்து 250-ன் தேசிய அவசரநிலை 6 மாத காலாவதி விதியுடன் குழப்பிக் கொள்கிறது.",
        "Option C is not required under constitutional law.", "விருப்பம் C அரசியலமைப்புச் சட்டத்தின் கீழ் தேவையில்லை.",
        "Option D correctly describes the post-42nd CAA legal position.", "விருப்பம் D 42-வது திருத்தத்திற்குப் பிந்தைய சட்ட நிலையைச் சரியாக விளக்குகிறது.",
        "Critical Contrast: National Emergency (Art 250) laws expire after 6 months. President's Rule (Art 356) laws CONTINUE until repealed by State Legislature.",
        "முக்கிய வேறுபாடு: தேசிய அவசரநிலை (சரத்து 250) சட்டங்கள் 6 மாதங்களில் காலாவதியாகின்றன. குடியரசுத் தலைவர் ஆட்சி (சரத்து 356) சட்டங்கள் மாநில சட்டமன்றம் ரத்து செய்யும் வரை தொடர்கின்றன.",
        "This ensures there is no sudden vacuum in state statutory laws when popular government is restored.",
        "மக்களாட்சி மீண்டும் அமையும் போது மாநில சட்டங்களில் திடீர் வெற்றிடம் ஏற்படாமல் இருப்பதை இது உறுதி செய்கிறது."
    ))

    # 017 - Key A
    qs.append(make_ep_q(
        PREFIX, 17, DIFF, "Financial Emergency - Operation", "Duration and Review of Financial Emergency",
        "Once approved by both Houses of Parliament, for how long does a proclamation of Financial Emergency under Article 360 remain in force?",
        "பாராளுமன்றத்தின் இரு அவைகளாலும் ஒப்புதல் அளிக்கப்பட்ட பிறகு, சரத்து 360-ன் கீழ் நிதி அவசரநிலைப் பிரகடனம் எவ்வளவு காலத்திற்கு அமலில் இருக்கும்?",
        "Indefinitely, until it is revoked by the President", "குடியரசுத் தலைவரால் திரும்பப் பெறப்படும் வரை காலவரையின்றி",
        "For a maximum period of 3 years", "அதிகபட்சமாக 3 ஆண்டுகள் வரை",
        "For 6 months, requiring repeated approval every 6 months", "6 மாதங்கள், ஒவ்வொரு 6 மாதங்களுக்கும் மீண்டும் ஒப்புதல் பெற வேண்டும்",
        "For a maximum period of 1 year", "அதிகபட்சமாக 1 ஆண்டு வரை",
        "A",
        "Unlike National Emergency (which requires parliamentary approval every 6 months) and President's Rule (which has a maximum cap of 3 years and requires 6-month approvals), Financial Emergency under Article 360, once approved by Parliament, continues INDEFINITELY until it is revoked by the President. No repeated parliamentary approval is required!",
        "தேசிய அவசரநிலை (ஒவ்வொரு 6 மாதங்களுக்கும் பாராளுமன்ற ஒப்புதல் தேவை) மற்றும் குடியரசுத் தலைவர் ஆட்சி (அதிகபட்சம் 3 ஆண்டுகள் மற்றும் 6 மாத ஒப்புதல் தேவை) போலல்லாமல், சரத்து 360-ன் கீழ் நிதி அவசரநிலை பாராளுமன்றத்தால் அங்கீகரிக்கப்பட்டவுடன் குடியரசுத் தலைவரால் திரும்பப் பெறப்படும் வரை காலவரையின்றி தொடரும். இதற்கு மீண்டும் மீண்டும் பாராளுமன்ற ஒப்புதல் தேவையில்லை!",
        "Option A is correct; no maximum period is prescribed and no periodic approval is needed.", "விருப்பம் A சரியானது; அதிகபட்ச கால வரம்போ அல்லது குறிப்பிட்ட கால ஒப்புதலோ தேவையில்லை.",
        "Option B (3 years) is the maximum cap for President's Rule under Article 356.", "விருப்பம் B (3 ஆண்டுகள்) சரத்து 356-ன் கீழ் குடியரசுத் தலைவர் ஆட்சிக்கான அதிகபட்ச வரம்பு.",
        "Option C (6 months repeated approval) applies to Articles 352 and 356.", "விருப்பம் C (6 மாத தொடர் ஒப்புதல்) சரத்து 352 மற்றும் 356-க்கு மட்டுமே பொருந்தும்.",
        "Option D is incorrect.", "விருப்பம் D தவறானது.",
        "Financial Emergency Uniqueness: (1) Once approved, it continues indefinitely until revoked; (2) No repeated parliamentary approval required.",
        "நிதி அவசரநிலையின் தனித்துவம்: (1) ஒப்புதல் பெற்றவுடன் திரும்பப் பெறும் வரை காலவரையின்றி தொடரும்; (2) மீண்டும் மீண்டும் பாராளுமன்ற ஒப்புதல் தேவையில்லை.",
        "India has faced severe economic crises (such as in 1991), but Article 360 has never been invoked.",
        "இந்தியா கடுமையான பொருளாதார நெருக்கடிகளை (1991 போன்ற) எதிர்கொண்ட போதிலும், சரத்து 360 இதுவரை பயன்படுத்தப்படவில்லை."
    ))

    # 018 - Key B
    qs.append(make_ep_q(
        PREFIX, 18, DIFF, "Financial Emergency - Effects", "Salary Reductions under Article 360",
        "During a Financial Emergency under Article 360, whose salaries and allowances can the President direct to be reduced?",
        "சரத்து 360-ன் கீழ் நிதி அவசரநிலையின் போது, யாருடைய ஊதியங்கள் மற்றும் படிகளைக் குறைக்க குடியரசுத் தலைவர் உத்தரவிட முடியும்?",
        "Only employees serving in connection with the affairs of the State", "மாநில விவகாரங்கள் தொடர்பாக பணியாற்றும் ஊழியர்களின் ஊதியம் மட்டுமே",
        "All or any class of persons serving the Union or States, including Judges of the Supreme Court and High Courts", "உச்ச நீதிமன்ற மற்றும் உயர் நீதிமன்ற நீதிபதிகள் உட்பட, மத்திய அல்லது மாநிலப் பணிகளில் உள்ள அனைத்து அல்லது எந்தவொரு பிரிவினரும்",
        "Only Union civil servants and ministers, excluding the judiciary", "நீதித்துறையைத் தவிர்த்து, மத்திய அரசு ஊழியர்கள் மற்றும் அமைச்சர்கள் மட்டுமே",
        "Only members of Parliament and State Legislative Assemblies", "பாராளுமன்ற மற்றும் மாநில சட்டமன்ற உறுப்பினர்கள் மட்டுமே",
        "B",
        "Under Article 360(4)(a)(i) and (b), during a Financial Emergency, the President can issue directions for the reduction of salaries and allowances of all or any class of persons serving in connection with the affairs of the Union or a State, including the Judges of the Supreme Court and the High Courts.",
        "சரத்து 360(4)(a)(i) மற்றும் (b)-ன் கீழ், நிதி அவசரநிலையின் போது உச்ச நீதிமன்ற மற்றும் உயர் நீதிமன்ற நீதிபதிகள் உட்பட மத்திய அல்லது மாநிலப் பணிகளில் உள்ள அனைத்து அல்லது எந்தவொரு பிரிவினரின் ஊதியங்களையும் படிகளையும் குறைக்க குடியரசுத் தலைவர் உத்தரவிடலாம்.",
        "Option A is incomplete; it covers Union servants as well as State servants.", "விருப்பம் A முழுமையற்றது; இது மத்திய மற்றும் மாநில ஊழியர்கள் இருவரையும் உள்ளடக்கியது.",
        "Option B is fully correct, specifically highlighting the constitutional inclusion of Supreme Court and High Court judges.", "விருப்பம் B முற்றிலும் சரியானது, குறிப்பாக உச்ச மற்றும் உயர் நீதிமன்ற நீதிபதிகள் சேர்க்கப்படுவதை விளக்குகிறது.",
        "Option C is incorrect because judges are explicitly included.", "விருப்பம் C தவறானது ஏனெனில் நீதிபதிகள் வெளிப்படையாக இதில் சேர்க்கப்பட்டுள்ளனர்.",
        "Option D is overly narrow.", "விருப்பம் D மிகவும் குறுகியது.",
        "Constitutional Exception: Judges' salaries are charged on Consolidated Fund and normally cannot be reduced to their disadvantage, EXCEPT during Financial Emergency.",
        "அரசியலமைப்பு விதிவிலக்கு: நீதிபதிகளின் ஊதியம் தொகுப்பு நிதியிலிருந்து வழங்கப்படுவதால் பொதுவாக குறைக்கப்பட முடியாது, ஆனால் நிதி அவசரநிலையின் போது மட்டுமே குறைக்கப்படலாம்.",
        "This underscores the total financial sovereignty the Centre assumes during severe monetary distress.",
        "கடுமையான நிதி நெருக்கடியின் போது மத்திய அரசு ஏற்கும் முழுமையான நிதி இறையாண்மையை இது காட்டுகிறது."
    ))

    # 019 - Key C
    qs.append(make_ep_q(
        PREFIX, 19, DIFF, "Financial Emergency - Money Bills", "State Money Bills under Article 360",
        "Under Article 360(4)(a)(ii), what special power does the President possess regarding Money Bills passed by a State Legislature during a Financial Emergency?",
        "சரத்து 360(4)(a)(ii)-ன் கீழ், நிதி அவசரநிலையின் போது ஒரு மாநில சட்டமன்றத்தால் நிறைவேற்றப்பட்ட பண மசோதாக்கள் தொடர்பாக குடியரசுத் தலைவர் என்ன சிறப்பு அதிகாரத்தைப் பெற்றுள்ளார்?",
        "The President can directly veto state money bills without Governor's reservation.", "ஆளுநரின் பரிந்துரையின்றி மாநில பண மசோதாக்களை குடியரசுத் தலைவர் நேரடியாக நிராகரிக்க முடியும்.",
        "State legislatures are prohibited from introducing any money bills.", "மாநில சட்டமன்றங்கள் பண மசோதாக்களை அறிமுகப்படுத்தவே தடை விதிக்கப்படுகிறது.",
        "The President can direct that all Money Bills or financial bills passed by the State Legislature be reserved for his consideration.", "மாநில சட்டமன்றத்தால் நிறைவேற்றப்பட்ட அனைத்து பண மசோதாக்கள் அல்லது நிதி மசோதாக்களையும் தனது பரிசீலனைக்காக நிறுத்தி வைக்க குடியரசுத் தலைவர் உத்தரவிடலாம்.",
        "The Union Finance Minister must introduce state budgets in Parliament instead.", "மாநில நிதிநிலை அறிக்கைகளை மத்திய நிதி அமைச்சர் பாராளுமன்றத்தில் தாக்கல் செய்ய வேண்டும்.",
        "C",
        "Article 360(4)(a)(ii) provides that during a Financial Emergency, directions issued by the executive power of the Union may include a provision requiring all Money Bills or other financial bills to be reserved for the consideration of the President after they are passed by the Legislature of the State.",
        "சரத்து 360(4)(a)(ii)-ன் படி, நிதி அவசரநிலையின் போது மாநில சட்டமன்றத்தால் நிறைவேற்றப்பட்ட பிறகு அனைத்து பண மசோதாக்கள் அல்லது பிற நிதி மசோதாக்களையும் குடியரசுத் தலைவரின் பரிசீலனைக்காக நிறுத்தி வைக்க வேண்டும் என்ற நிபந்தனையை மத்திய அரசு உத்தரவாகப் பிறப்பிக்கலாம்.",
        "Option A is incorrect procedure.", "விருப்பம் A தவறான நடைமுறை.",
        "Option B is false; state legislatures can still introduce and pass them, but they must be reserved.", "விருப்பம் B தவறு; மாநில சட்டமன்றங்கள் அவற்றை அறிமுகப்படுத்தி நிறைவேற்றலாம், ஆனால் நிறுத்தி வைக்கப்பட வேண்டும்.",
        "Option C is the verbatim constitutional requirement under Article 360(4)(a)(ii).", "விருப்பம் C சரத்து 360(4)(a)(ii)-ன் கீழ் உள்ள துல்லியமான அரசியலமைப்பு விதியாகும்.",
        "Option D applies to President's Rule, not ordinary Article 360 operation.", "விருப்பம் D குடியரசுத் தலைவர் ஆட்சிக்குப் பொருந்தும், நிதி அவசரநிலைக்கு அல்ல.",
        "Remember: State Money Bills can be mandated to be reserved for the President's consideration during Financial Emergency.",
        "நினைவில் கொள்க: நிதி அவசரநிலையின் போது மாநிலப் பண மசோதாக்களை குடியரசுத் தலைவரின் பரிசீலனைக்கு நிறுத்தி வைக்க உத்தரவிட முடியும்.",
        "This gives the Union government a comprehensive check over state fiscal allocations.",
        "இது மாநிலங்களின் நிதி ஒதுக்கீடுகள் மீது மத்திய அரசுக்கு ஒரு விரிவான கட்டுப்பாட்டை வழங்குகிறது."
    ))

    # 020 - Key D
    qs.append(make_ep_q(
        PREFIX, 20, DIFF, "Historical Precedent", "First Proclamation of National Emergency (1962)",
        "The first proclamation of National Emergency in India was declared in October 1962 in the wake of Chinese aggression in NEFA. Until when did this first proclamation remain in force?",
        "இந்தியாவில் முதல் தேசிய அவசரநிலைப் பிரகடனம் அக்டோபர் 1962-ல் NEFA பகுதியில் சீன ஆக்கிரமிப்பைத் தொடர்ந்து அறிவிக்கப்பட்டது. இந்த முதல் பிரகடனம் எப்போது வரை அமலில் இருந்தது?",
        "November 1962", "நவம்பர் 1962",
        "January 1965", "ஜனவரி 1965",
        "September 1965", "செப்டம்பர் 1965",
        "January 1968", "ஜனவரி 1968",
        "D",
        "The first proclamation of National Emergency was issued on 26 October 1962 due to Chinese aggression in NEFA (now Arunachal Pradesh). It remained in force through the 1965 Indo-Pak war and was revoked only in January 1968.",
        "முதல் தேசிய அவசரநிலைப் பிரகடனம் NEFA (தற்போதைய அருணாச்சலப் பிரதேசம்) பகுதியில் சீன ஆக்கிரமிப்பு காரணமாக 26 அக்டோபர் 1962 அன்று வெளியிடப்பட்டது. இது 1965 இந்திய-பாகிஸ்தான் போரின் போதும் தொடர்ந்து அமலில் இருந்து, ஜனவரி 1968-ல் தான் திரும்பப் பெறப்பட்டது.",
        "Option A is incorrect; the war ended in Nov 1962, but emergency continued.", "விருப்பம் A தவறானது; போர் நவம்பர் 1962-ல் முடிந்தது, ஆனால் அவசரநிலை தொடர்ந்தது.",
        "Option B is incorrect.", "விருப்பம் B தவறானது.",
        "Option C is incorrect; it was active during the 1965 war.", "விருப்பம் C தவறானது; 1965 போரின் போது இது செயலில் இருந்தது.",
        "Option D is historically accurate: revoked in January 1968.", "விருப்பம் D வரலாற்று ரீதியாக சரியானது: ஜனவரி 1968-ல் திரும்பப் பெறப்பட்டது.",
        "Historic Fact: The 1962 emergency lasted over 5 years (October 1962 to January 1968), covering both Chinese and 1965 Pakistani conflicts.",
        "வரலாற்று உண்மை: 1962 அவசரநிலை 5 ஆண்டுகளுக்கு மேல் (அக்டோபர் 1962 முதல் ஜனவரி 1968 வரை) நீடித்தது, சீனா மற்றும் 1965 பாகிஸ்தான் போர்கள் இரண்டையும் உள்ளடக்கியது.",
        "Because it was already in force, a new emergency proclamation was not required during the 1965 war.",
        "இது ஏற்கனவே அமலில் இருந்ததால், 1965 போரின் போது புதிய அவசரநிலைப் பிரகடனம் தேவைப்படவில்லை."
    ))

    # 021 - Key A
    qs.append(make_ep_q(
        PREFIX, 21, DIFF, "Historical Precedent", "Concurrent Emergency Proclamations",
        "When the internal National Emergency was proclaimed on 25 June 1975 on grounds of 'internal disturbance', what was the status of the previous 1971 external emergency?",
        "25 ஜூன் 1975 அன்று 'உள்நாட்டுக் குழப்பம்' என்ற காரணத்தின் அடிப்படையில் உள்நாட்டு தேசிய அவசரநிலை பிரகடனப்படுத்தப்பட்ட போது, அதற்கு முந்தைய 1971 வெளிப்புற அவசரநிலையின் நிலை என்னவாக இருந்தது?",
        "The 1971 proclamation was already in operation, so two proclamations operated simultaneously", "1971 பிரகடனம் ஏற்கனவே அமலில் இருந்தது, எனவே இரண்டு பிரகடனங்களும் ஒரே நேரத்தில் செயல்பட்டன",
        "The 1971 proclamation had been revoked in 1972 following the Simla Agreement", "சிம்லா ஒப்பந்தத்தைத் தொடர்ந்து 1971 பிரகடனம் 1972-ல் திரும்பப் பெறப்பட்டிருந்தது",
        "The 1971 proclamation automatically merged into the 1975 proclamation", "1971 பிரகடனம் தானாகவே 1975 பிரகடனத்துடன் இணைக்கப்பட்டது",
        "The 1971 proclamation was revoked on 24 June 1975 to allow the new proclamation", "புதிய பிரகடனத்தை அனுமதிக்க 1971 பிரகடனம் 24 ஜூன் 1975 அன்று திரும்பப் பெறப்பட்டது",
        "A",
        "When the third National Emergency was proclaimed on 25 June 1975 on grounds of 'internal disturbance', the second proclamation of December 1971 (issued during the Indo-Pak war) was still in active operation. Both proclamations operated concurrently until both were revoked together in March 1977.",
        "25 ஜூன் 1975 அன்று 'உள்நாட்டுக் குழப்பம்' என்ற பெயரில் மூன்றாவது தேசிய அவசரநிலை பிரகடனப்படுத்தப்பட்ட போது, டிசம்பர் 1971-ல் (இந்திய-பாகிஸ்தான் போரின் போது) வெளியிடப்பட்ட இரண்டாவது பிரகடனம் தொடர்ந்து அமலில் இருந்தது. மார்ச் 1977-ல் இரண்டும் ஒன்றாக திரும்பப் பெறப்படும் வரை இரண்டும் ஒரே நேரத்தில் செயல்பட்டன.",
        "Option A is historically accurate; two proclamations co-existed between June 1975 and March 1977.", "விருப்பம் A வரலாற்று ரீதியாக சரியானது; ஜூன் 1975 முதல் மார்ச் 1977 வரை இரண்டு பிரகடனங்கள் ஒரே நேரத்தில் நீடித்தன.",
        "Option B is false; 1971 proclamation was not revoked in 1972.", "விருப்பம் B தவறு; 1971 பிரகடனம் 1972-ல் திரும்பப் பெறப்படவில்லை.",
        "Option C has no constitutional basis.", "விருப்பம் C-க்கு அரசியலமைப்பு அடிப்படை இல்லை.",
        "Option D is historically untrue.", "விருப்பம் D வரலாற்று ரீதியாக உண்மையல்ல.",
        "TNPSC Fact: In March 1977, both the December 1971 (external) and June 1975 (internal) emergencies were revoked simultaneously.",
        "TNPSC உண்மை: மார்ச் 1977-ல், டிசம்பர் 1971 (வெளிப்புற) மற்றும் ஜூன் 1975 (உள்நாட்டு) அவசரநிலைகள் இரண்டும் ஒரே நேரத்தில் திரும்பப் பெறப்பட்டன.",
        "The 38th Amendment (1975) specifically legalized the issuance of multiple simultaneous emergency proclamations on different grounds.",
        "38-வது திருத்தம் (1975) வெவ்வேறு காரணங்களின் அடிப்படையில் ஒரே நேரத்தில் பல அவசரநிலைப் பிரகடனங்களை வெளியிடுவதை சட்டப்பூர்வமாக்கியது."
    ))

    # 022 - Key B
    qs.append(make_ep_q(
        PREFIX, 22, DIFF, "Constitutional Comparison", "National Emergency vs President's Rule",
        "Which of the following statements is INCORRECT regarding the differences between National Emergency (Article 352) and President's Rule (Article 356)?",
        "தேசிய அவசரநிலை (சரத்து 352) மற்றும் குடியரசுத் தலைவர் ஆட்சி (சரத்து 356) ஆகியவற்றுக்கு இடையேயான வேறுபாடுகளில் பின்வருவனவற்றில் எது தவறானது?",
        "National Emergency affects Fundamental Rights, whereas President's Rule has no effect on Fundamental Rights.", "தேசிய அவசரநிலை அடிப்படை உரிமைகளைப் பாதிக்கிறது, ஆனால் குடியரசுத் தலைவர் ஆட்சி அடிப்படை உரிமைகளில் எந்தப் பாதிப்பையும் ஏற்படுத்துவதில்லை.",
        "National Emergency can be extended for a maximum of 3 years, whereas President's Rule can be extended indefinitely with periodic approval.", "தேசிய அவசரநிலையை அதிகபட்சமாக 3 ஆண்டுகள் மட்டுமே நீட்டிக்க முடியும், அதே சமயம் குடியரசுத் தலைவர் ஆட்சியை குறிப்பிட்ட கால ஒப்புதலுடன் காலவரையின்றி நீட்டிக்க முடியும்.",
        "National Emergency requires a special majority for approval, whereas President's Rule requires only a simple majority.", "தேசிய அவசரநிலைக்கு ஒப்புதல் அளிக்க சிறப்புப் பெரும்பான்மை தேவை, ஆனால் குடியரசுத் தலைவர் ஆட்சிக்கு எளிய பெரும்பான்மை மட்டுமே போதும்.",
        "Under National Emergency, the State Legislature is not dissolved, whereas under President's Rule, it is either dissolved or kept in suspended animation.", "தேசிய அவசரநிலையின் கீழ் மாநில சட்டமன்றம் கலைக்கப்படுவதில்லை, ஆனால் குடியரசுத் தலைவர் ஆட்சியின் கீழ் அது கலைக்கப்படுகிறது அல்லது தற்காலிகமாக நிறுத்தி வைக்கப்படுகிறது.",
        "B",
        "Statement B is completely INCORRECT (and hence the correct answer). It is President's Rule that has a maximum limit of 3 years (Article 356(4)), whereas National Emergency under Article 352 can be extended INDEFINITELY with parliamentary approval every six months.",
        "கூற்று B முற்றிலும் தவறானது (எனவே இதுவே சரியான விடை). குடியரசுத் தலைவர் ஆட்சிக்குத் தான் அதிகபட்ச வரம்பு 3 ஆண்டுகள் (சரத்து 356(4)), மாறாக சரத்து 352-ன் கீழ் தேசிய அவசரநிலையை ஒவ்வொரு ஆறு மாதங்களுக்கும் பாராளுமன்ற ஒப்புதலுடன் காலவரையின்றி நீட்டிக்க முடியும்.",
        "Option A is a true statement.", "விருப்பம் A ஒரு உண்மையான கூற்று.",
        "Option B is the false statement: it reverses the duration caps of Articles 352 and 356.", "விருப்பம் B தவறான கூற்று: இது சரத்துகள் 352 மற்றும் 356-ன் கால வரம்புகளை தலைகீழாக மாற்றுகிறது.",
        "Option C is a true statement.", "விருப்பம் C ஒரு உண்மையான கூற்று.",
        "Option D is a true statement.", "விருப்பம் D ஒரு உண்மையான கூற்று.",
        "Check duration caps: National Emergency = Indefinite (6 months at a time); President's Rule = Maximum 3 years.",
        "கால வரம்புகளைச் சரிபார்க்கவும்: தேசிய அவசரநிலை = காலவரையற்றது (ஒரு முறைக்கு 6 மாதங்கள்); குடியரசுத் தலைவர் ஆட்சி = அதிகபட்சம் 3 ஆண்டுகள்.",
        "This difference exists because President's Rule directly supersedes state democracy, whereas National Emergency deals with external/national security.",
        "குடியரசுத் தலைவர் ஆட்சி மாநில ஜனநாயகத்தை நேரடியாக முடக்குகிறது, ஆனால் தேசிய அவசரநிலை தேசிய பாதுகாப்பைக் கையாள்கிறது என்பதால் இந்த வேறுபாடு உள்ளது."
    ))

    # 023 - Key C
    qs.append(make_ep_q(
        PREFIX, 23, DIFF, "Constitutional Commission", "Sarkaria Commission Recommendations",
        "The Sarkaria Commission on Centre-State Relations (1987) recommended that Article 356 should be used:",
        "மத்திய-மாநில உறவுகள் குறித்த சர்க்காரியா ஆணையம் (1987) சரத்து 356-ஐ எவ்வாறு பயன்படுத்த வேண்டும் என்று பரிந்துரைத்தது?",
        "Frequently, whenever a state government belongs to an opposition party", "எதிர்க்கட்சி ஆளும் மாநிலங்களில் அடிக்கடி பயன்படுத்த வேண்டும்",
        "Exclusively during general election campaigns", "பொதுத்தேர்தல் பிரச்சாரங்களின் போது மட்டுமே பயன்படுத்த வேண்டும்",
        "Very sparingly, as a matter of last resort, when all alternative remedies have been exhausted", "அனைத்து மாற்று வழிகளும் தீர்ந்துவிட்ட பிறகு, கடைசி ஆயுதமாக மிகவும் அரிதாக மட்டுமே பயன்படுத்த வேண்டும்",
        "Only after holding a state-wide public referendum", "மாநிலம் தழுவிய பொது வாக்கெடுப்பு நடத்திய பிறகு மட்டுமே பயன்படுத்த வேண்டும்",
        "C",
        "The Sarkaria Commission (1987) emphatically recommended that Article 356 should be used very sparingly, in extreme cases, as a measure of last resort, when all other alternatives fail to prevent or rectify a breakdown of constitutional machinery in the State. It also recommended issuing a prior warning to the errant State.",
        "சர்க்காரியா ஆணையம் (1987), மாநிலத்தில் அரசியலமைப்பு இயந்திரம் முறிவடைவதைத் தடுக்க அல்லது சரிசெய்ய அனைத்து மாற்று வழிகளும் தோல்வியடையும் போது, சரத்து 356-ஐ ஒரு கடைசி ஆயுதமாக மிகவும் அரிதாக மட்டுமே பயன்படுத்த வேண்டும் என்று திட்டவட்டமாகப் பரிந்துரைத்தது. மேலும் தவறிழைக்கும் மாநிலத்திற்கு முன் எச்சரிக்கை விடுக்கவும் பரிந்துரைத்தது.",
        "Option A represents partisan misuse, condemned by Sarkaria Commission.", "விருப்பம் A என்பது கட்சி சார்பான தவறான பயன்பாடு, அதை சர்க்காரியா ஆணையம் கண்டித்தது.",
        "Option B is unrelated.", "விருப்பம் B தொடர்பற்றது.",
        "Option C is the classic 'measure of last resort' doctrine laid down by Sarkaria Commission.", "விருப்பம் C என்பது சர்க்காரியா ஆணையத்தால் வகுக்கப்பட்ட உன்னதமான 'கடைசி ஆயுதம்' கோட்பாடாகும்.",
        "Option D has no basis in the report.", "விருப்பம் D அறிக்கையில் இடம்பெறவில்லை.",
        "Sarkaria Doctrine on Art 356: 'Measure of last resort' + prior warning to the State.",
        "சரத்து 356 மீதான சர்க்காரியா கோட்பாடு: 'கடைசி ஆயுதம்' + மாநிலத்திற்கு முன் எச்சரிக்கை.",
        "This principle was subsequently incorporated into binding constitutional jurisprudence by the Supreme Court in the Bommai case.",
        "இந்தக் கொள்கை பின்னர் பொம்மை வழக்கில் உச்ச நீதிமன்றத்தால் அரசியலமைப்புச் சட்ட விதியாக இணைக்கப்பட்டது."
    ))

    # 024 - Key D
    qs.append(make_ep_q(
        PREFIX, 24, DIFF, "Constitutional Mechanics", "Article 355 Duty of the Union",
        "Article 355 of the Indian Constitution imposes which specific constitutional duty on the Union government towards every State?",
        "இந்திய அரசியலமைப்பின் சரத்து 355 ஒவ்வொரு மாநிலத்திற்கும் எதிராக மத்திய அரசுக்கு எந்தக் குறிப்பிட்ட அரசியலமைப்பு கடமையை விதிக்கிறது?",
        "To provide financial grants-in-aid to cover state revenue deficits", "மாநில வருவாய் பற்றாக்குறையை ஈடுகட்ட நிதி மானியங்களை வழங்குவது",
        "To appoint civil servants and police chiefs directly in every State", "ஒவ்வொரு மாநிலத்திலும் குடிமைப் பணி அதிகாரிகள் மற்றும் காவல்துறை தலைவர்களை நேரடியாக நியமிப்பது",
        "To dissolve the state legislature whenever there is coalition instability", "கூட்டணி உறுதியற்ற தன்மை ஏற்படும் போதெல்லாம் மாநில சட்டமன்றத்தைக் கலைப்பது",
        "To protect every State against external aggression and internal disturbance, and to ensure that government is carried on in accordance with the Constitution", "ஒவ்வொரு மாநிலத்தையும் வெளிநாட்டு ஆக்கிரமிப்பு மற்றும் உள்நாட்டுக் குழப்பங்களிலிருந்து பாதுகாப்பது மற்றும் மாநில அரசு அரசியலமைப்பு விதிகளின்படி நடைபெறுவதை உறுதி செய்வது",
        "D",
        "Article 355 states: 'It shall be the duty of the Union to protect every State against external aggression and internal disturbance and to ensure that the government of every State is carried on in accordance with the provisions of this Constitution.' This duty provides the constitutional justification for Articles 352 and 356.",
        "சரத்து 355 கூறுகிறது: 'ஒவ்வொரு மாநிலத்தையும் வெளிநாட்டு ஆக்கிரமிப்பு மற்றும் உள்நாட்டுக் குழப்பங்களிலிருந்து பாதுகாப்பதும், ஒவ்வொரு மாநிலத்தின் அரசும் இந்த அரசியலமைப்பின் விதிகளின்படி நடைபெறுவதை உறுதி செய்வதும் ஒன்றியத்தின் கடமையாகும்.' இந்தக் கடமையே சரத்துகள் 352 மற்றும் 356-க்கான அரசியலமைப்பு நியாயத்தை வழங்குகிறது.",
        "Option A refers to Article 275 grants.", "விருப்பம் A சரத்து 275 மானியங்களைக் குறிக்கிறது.",
        "Option B violates federal principles and state public service rules.", "விருப்பம் B கூட்டாட்சிக் கொள்கை மற்றும் மாநில அரசுப் பணி விதிகளை மீறுகிறது.",
        "Option C describes misuse of powers.", "விருப்பம் C அதிகார துஷ்பிரயோகத்தை விவரிக்கிறது.",
        "Option D verbatim quotes the fundamental duty of the Union under Article 355.", "விருப்பம் D சரத்து 355-ன் கீழ் ஒன்றியத்தின் அடிப்படைக் கடமையை அப்படியே மேற்கோள் காட்டுகிறது.",
        "Article 355 is the foundational 'Protective Umbrella' article that justifies the Centre invoking Article 352 or 356.",
        "சரத்து 355 என்பது மத்திய அரசு சரத்து 352 அல்லது 356-ஐப் பயன்படுத்துவதை நியாயப்படுத்தும் 'பாதுகாப்புக் குடை' சரத்தாகும்.",
        "Notice that while 'internal disturbance' was removed from Article 352, it still remains in Article 355!",
        "சரத்து 352-லிருந்து 'உள்நாட்டுக் குழப்பம்' நீக்கப்பட்டாலும், அது இன்னும் சரத்து 355-ல் தொடர்வதைக் கவனிக்கவும்!"
    ))

    # 025 - Key B
    qs.append(make_ep_q(
        PREFIX, 25, DIFF, "Constitutional Comparison", "Suspension of Fundamental Rights Nuance",
        "Which pair of Fundamental Rights can NEVER be suspended or their enforcement restricted, even during a National Emergency declared on grounds of war or external aggression?",
        "போர் அல்லது வெளிநாட்டு ஆக்கிரமிப்பு என்ற காரணத்தின் அடிப்படையில் அறிவிக்கப்பட்ட தேசிய அவசரநிலையின் போது கூட, எந்த இரு அடிப்படை உரிமைகளை ஒருபோதும் இடைநிறுத்தவோ அவற்றின் அமலாக்கத்தைக் கட்டுப்படுத்தவோ முடியாது?",
        "Articles 14 and 19", "சரத்துகள் 14 மற்றும் 19",
        "Articles 20 and 21", "சரத்துகள் 20 மற்றும் 21",
        "Articles 21 and 22", "சரத்துகள் 21 மற்றும் 22",
        "Articles 25 and 32", "சரத்துகள் 25 மற்றும் 32",
        "B",
        "Under Article 359, as amended by the 44th Constitutional Amendment Act 1978, the President cannot suspend the right to move the court for the enforcement of fundamental rights guaranteed by Articles 20 (Protection in respect of conviction for offences) and 21 (Protection of life and personal liberty).",
        "1978-ன் 44-வது அரசியலமைப்பு திருத்தச் சட்டத்தால் திருத்தப்பட்ட சரத்து 359-ன் படி, சரத்து 20 (குற்றங்களுக்கான தீர்ப்பளிப்பு தொடர்பான பாதுகாப்பு) மற்றும் சரத்து 21 (வாழ்க்கை மற்றும் தனிநபர் சுதந்திரப் பாதுகாப்பு) உத்தரவாதம் அளிக்கும் அடிப்படை உரிமைகளை அமல்படுத்துவதற்காக நீதிமன்றத்தை அணுகும் உரிமையை குடியரசுத் தலைவர் இடைநிறுத்த முடியாது.",
        "Option A: Article 19 is automatically suspended under Art 358 during war; Article 14 enforcement can be suspended under Art 359.", "விருப்பம் A: போரின் போது சரத்து 19 தானாகவே இடைநிறுத்தப்படும்; சரத்து 14-ன் அமலாக்கம் சரத்து 359-ன் கீழ் இடைநிறுத்தப்படலாம்.",
        "Option B is the absolute non-derogable core protected by the 44th Amendment.", "விருப்பம் B என்பது 44-வது திருத்தத்தால் பாதுகாக்கப்பட்ட மீற முடியாத மைய உரிமைகளாகும்.",
        "Option C: Article 22 (preventive detention safeguards) can be affected under Art 359.", "விருப்பம் C: சரத்து 22 (தடுப்புக் காவல் பாதுகாப்புகள்) சரத்து 359-ன் கீழ் பாதிக்கப்படலாம்.",
        "Option D: Articles 25 and 32 (except for 20 & 21) can have enforcement suspended.", "விருப்பம் D: சரத்து 25 மற்றும் 32-ன் அமலாக்கம் இடைநிறுத்தப்படலாம்.",
        "Golden Rule of Emergency: Articles 20 and 21 are SANCTROSANCT and IMMUNE from suspension under all emergencies.",
        "அவசரநிலையின் பொன் விதி: சரத்துகள் 20 மற்றும் 21 புனிதமானவை மற்றும் அனைத்து அவசரநிலைகளிலும் இடைநிறுத்தத்திலிருந்து விலக்கு பெற்றவை.",
        "This amendment was directly enacted to undo the draconian effects of the ADM Jabalpur (Habeas Corpus) judgment.",
        "ஏ.டி.எம். ஜபல்பூர் (ஆட்கொணர்வு மனு) வழக்கின் கடுமையான விளைவுகளைத் தகர்க்கவே இந்தத் திருத்தம் நேரடியாகக் கொண்டுவரப்பட்டது."
    ))

    return qs

def get_medium_questions_part2():
    qs = []

    # 026 - Key A
    qs.append(make_ep_q(
        PREFIX, 26, DIFF, "Constitutional Procedure", "Parliamentary Extension of Lok Sabha Term",
        "Under the proviso to Article 83(2), while a proclamation of National Emergency is in operation, how long can the term of the Lok Sabha be extended by Parliament by law at a time?",
        "சரத்து 83(2)-ன் நிபந்தனை விதியின் கீழ், தேசிய அவசரநிலைப் பிரகடனம் அமலில் இருக்கும் போது, பாராளுமன்றம் சட்டம் இயற்றி மக்களவையின் பதவிக் காலத்தை ஒரு முறைக்கு எவ்வளவு காலம் வரை நீட்டிக்க முடியும்?",
        "For a period not exceeding one year at a time", "ஒரு முறைக்கு ஒரு ஆண்டிற்கு மிகாமல்",
        "For a period of six months at a time", "ஒரு முறைக்கு ஆறு மாத காலத்திற்கு",
        "For a period not exceeding two years at a time", "ஒரு முறைக்கு இரண்டு ஆண்டுகளுக்கு மிகாமல்",
        "For the entire remaining duration of the emergency indefinitely", "அவசரநிலை முடியும் வரை காலவரையின்றி",
        "A",
        "Under Article 83(2) proviso, while a proclamation of National Emergency is in operation, Parliament may by law extend the normal 5-year term of the Lok Sabha for a period not exceeding ONE YEAR AT A TIME. However, this extension cannot continue beyond a period of six months after the proclamation has ceased to operate.",
        "சரத்து 83(2)-ன் நிபந்தனை விதியின்படி, தேசிய அவசரநிலை அமலில் இருக்கும் போது, மக்களவையின் சாதாரண 5 ஆண்டு பதவிக்காலத்தை பாராளுமன்றம் சட்டம் மூலம் ஒரு முறைக்கு ஒரு ஆண்டிற்கு மிகாமல் நீட்டிக்க முடியும். இருப்பினும், அவசரநிலை முடிவுக்கு வந்த பிறகு 6 மாதங்களுக்கு மேல் இந்த நீட்டிப்பு தொடர முடியாது.",
        "Option A is the exact constitutional limitation under Article 83(2).", "விருப்பம் A என்பது சரத்து 83(2)-ன் கீழ் உள்ள துல்லியமான அரசியலமைப்பு வரம்பாகும்.",
        "Option B (6 months) is the post-emergency sunset limit, not the extension increment.", "விருப்பம் B (6 மாதங்கள்) என்பது அவசரநிலைக்குப் பிந்தைய வரம்பு, நீட்டிப்பு தவணை அல்ல.",
        "Option C (2 years) is constitutionally prohibited.", "விருப்பம் C (2 ஆண்டுகள்) அரசியலமைப்பு ரீதியாக தடைசெய்யப்பட்டது.",
        "Option D violates democratic parliamentary renewal principles.", "விருப்பம் D ஜனநாயக பாராளுமன்ற புதுப்பித்தல் கொள்கைகளை மீறுகிறது.",
        "Lok Sabha Term Extension Rule: Max 1 year at a time; Cannot exceed 6 months after emergency ends.",
        "மக்களவை பதவிக்கால நீட்டிப்பு விதி: ஒரு முறைக்கு அதிகபட்சம் 1 ஆண்டு; அவசரநிலை முடிந்த 6 மாதங்களுக்கு மேல் நீடிக்க முடியாது.",
        "The 5th Lok Sabha (1971-1977) was extended twice for one year each using this constitutional power.",
        "5-வது மக்களவை (1971-1977) இந்த அரசியலமைப்பு அதிகாரத்தைப் பயன்படுத்தி தலா ஒரு ஆண்டு என இரண்டு முறை நீட்டிக்கப்பட்டது."
    ))

    # 027 - Key B
    qs.append(make_ep_q(
        PREFIX, 27, DIFF, "Constitutional Procedure", "Extension of State Legislative Assembly Term",
        "Which Article of the Constitution empowers Parliament to extend the normal 5-year term of a State Legislative Assembly by one year at a time during a National Emergency?",
        "தேசிய அவசரநிலையின் போது மாநில சட்டமன்றத்தின் சாதாரண 5 ஆண்டு பதவிக்காலத்தை பாராளுமன்றம் சட்டம் இயற்றி ஒரு முறைக்கு ஒரு வருடம் நீட்டிக்க எந்த அரசியலமைப்பு சரத்து அதிகாரம் அளிக்கிறது?",
        "Article 168", "சரத்து 168",
        "Article 172(1) proviso", "சரத்து 172(1) நிபந்தனை விதி",
        "Article 356(1)", "சரத்து 356(1)",
        "Article 249", "சரத்து 249",
        "B",
        "Under the proviso to Article 172(1), while a proclamation of National Emergency is in operation, the 5-year term of a State Legislative Assembly may be extended by Parliament by law for a period not exceeding one year at a time, and not extending beyond six months after the proclamation ceases to operate.",
        "சரத்து 172(1)-ன் நிபந்தனை விதியின் கீழ், தேசிய அவசரநிலைப் பிரகடனம் அமலில் இருக்கும் போது, மாநில சட்டமன்றத்தின் 5 ஆண்டு காலத்தை பாராளுமன்றம் சட்டம் மூலம் ஒரு முறைக்கு ஒரு ஆண்டிற்கு மிகாமல் நீட்டிக்க முடியும்; அவசரநிலை முடிந்து 6 மாதங்களுக்கு மேல் இது நீடிக்க முடியாது.",
        "Option A deals with the constitution of legislatures in states.", "விருப்பம் A மாநிலங்களில் சட்டமன்றங்களை அமைப்பது தொடர்பானது.",
        "Option B is the precise constitutional provision governing State Assembly term extensions.", "விருப்பம் B மாநில சட்டமன்ற பதவிக்கால நீட்டிப்பைக் கட்டுப்படுத்தும் துல்லியமான அரசியலமைப்பு விதியாகும்.",
        "Option C deals with President's Rule.", "விருப்பம் C குடியரசுத் தலைவர் ஆட்சி தொடர்பானது.",
        "Option D deals with Rajya Sabha resolution empowering Parliament to legislate on State List.", "விருப்பம் D மாநிலப் பட்டியலில் சட்டம் இயற்ற பாராளுமன்றத்திற்கு அதிகாரமளிக்கும் மாநிலங்களவைத் தீர்மானம் தொடர்பானது.",
        "Parallels to remember: Art 83(2) proviso for Lok Sabha extension; Art 172(1) proviso for State Legislative Assembly extension.",
        "நினைவில் கொள்ள வேண்டிய இணைகள்: மக்களவை நீட்டிப்புக்கு சரத்து 83(2) நிபந்தனை; மாநில சட்டமன்ற நீட்டிப்புக்கு சரத்து 172(1) நிபந்தனை.",
        "Notice that both extensions are enacted by Parliament, NOT by the State Legislature itself.",
        "இரு நீட்டிப்புகளுமே பாராளுமன்றத்தால் இயற்றப்படுகின்றன, மாநில சட்டமன்றத்தால் அல்ல என்பதை நினைவில் கொள்க."
    ))

    # 028 - Key C
    qs.append(make_ep_q(
        PREFIX, 28, DIFF, "Federal Relations", "Distribution of Revenues during National Emergency",
        "Under Article 354, during the operation of a National Emergency, the President has the power to modify the constitutional distribution of revenues between the Union and the States under Articles 268 to 279. How long do such presidential modification orders remain in force?",
        "சரத்து 354-ன் கீழ், தேசிய அவசரநிலை அமலில் இருக்கும் போது, சரத்துகள் 268 முதல் 279 வரையிலான மத்திய-மாநில வருவாய் பகிர்வை மாற்றியமைக்க குடியரசுத் தலைவருக்கு அதிகாரம் உண்டு. இத்தகைய குடியரசுத் தலைவரின் மாற்றியமைக்கும் ஆணைகள் எவ்வளவு காலம் வரை அமலில் இருக்கும்?",
        "They expire immediately upon the revocation of the National Emergency.", "தேசிய அவசரநிலை திரும்பப் பெறப்பட்ட உடனேயே அவை காலாவதியாகிவிடும்.",
        "They remain in force permanently until superseded by a Finance Commission report.", "நிதி ஆணைய அறிக்கையால் மாற்றப்படும் வரை அவை நிரந்தரமாக அமலில் இருக்கும்.",
        "Not extending beyond the end of the financial year in which the emergency ceases to operate.", "அவசரநிலை முடிவுக்கு வரும் நிதி ஆண்டின் இறுதிக்கு மிகாமல் அவை நீடிக்கும்.",
        "For a fixed period of five years regardless of when the emergency ends.", "அவசரநிலை எப்போது முடிந்தாலும் ஒரு நிலையான ஐந்து ஆண்டு காலத்திற்கு நீடிக்கும்.",
        "C",
        "Under Article 354(2), every order made by the President modifying the distribution of revenues under Articles 268 to 279 during a National Emergency shall cease to operate at the end of the financial year in which the proclamation of emergency ceases to operate. Furthermore, every such order must be laid before each House of Parliament.",
        "சரத்து 354(2)-ன் கீழ், தேசிய அவசரநிலையின் போது சரத்துகள் 268 முதல் 279 வரையிலான வருவாய் பகிர்வை மாற்றியமைக்கும் குடியரசுத் தலைவரின் ஆணை, அவசரநிலைப் பிரகடனம் முடிவுக்கு வரும் நிதி ஆண்டின் முடிவில் காலாவதியாகிவிடும். மேலும், இந்த ஆணை பாராளுமன்றத்தின் இரு அவைகளிலும் வைக்கப்பட வேண்டும்.",
        "Option A is incorrect; financial adjustments are synchronized to the fiscal year-end to prevent budgetary chaos.", "விருப்பம் A தவறானது; வரவு-செலவு குழப்பங்களைத் தவிர்க்க நிதி மாற்றங்கள் நிதி ஆண்டின் இறுதியுடன் ஒருங்கிணைக்கப்படுகின்றன.",
        "Option B is false.", "விருப்பம் B தவறு.",
        "Option C is the exact constitutional formulation under Article 354(2).", "விருப்பம் C சரத்து 354(2)-ன் கீழ் உள்ள துல்லியமான அரசியலமைப்பு விதியாகும்.",
        "Option D has no constitutional foundation.", "விருப்பம் D-க்கு அரசியலமைப்பு அடிப்படை இல்லை.",
        "Article 354 Sunset: Revenue modification orders last until the end of the financial year in which the emergency ceases.",
        "சரத்து 354 காலாவதி: வருவாய் மாற்றியமைப்பு ஆணைகள் அவசரநிலை முடிவடையும் நிதி ஆண்டின் இறுதி வரை நீடிக்கும்.",
        "This prevents mid-year budgetary disruption for both the Union and the states.",
        "இது மத்திய மற்றும் மாநில அரசுகளுக்கு ஆண்டின் மத்தியில் வரவுசெலவுத் திட்ட இடையூறு ஏற்படுவதைத் தடுக்கிறது."
    ))

    # 029 - Key D
    qs.append(make_ep_q(
        PREFIX, 29, DIFF, "Constitutional Amendments", "42nd Amendment Impact on Emergency",
        "Which of the following significant changes regarding Emergency Provisions was introduced by the 42nd Constitutional Amendment Act of 1976?",
        "1976-ன் 42-வது அரசியலமைப்பு திருத்தச் சட்டத்தின் மூலம் அவசரநிலைப் பிரிவுகள் தொடர்பாக அறிமுகப்படுத்தப்பட்ட குறிப்பிடத்தக்க மாற்றம் பின்வருவனவற்றில் எது?",
        "Requiring written advice of the Cabinet for proclaiming emergency", "அவசரநிலையைப் பிரகடனப்படுத்த கேபினட்டின் எழுத்துப்பூர்வ ஆலோசனையைக் கோருதல்",
        "Limiting the operation of President's Rule to a maximum of 3 years", "குடியரசுத் தலைவர் ஆட்சியை அதிகபட்சமாக 3 ஆண்டுகளாகக் கட்டுப்படுத்துதல்",
        "Making Articles 20 and 21 non-derogable under Article 359", "சரத்து 359-ன் கீழ் சரத்துகள் 20 மற்றும் 21-ஐ இடைநிறுத்த முடியாததாக மாற்றுதல்",
        "Enabling the President to limit the operation of National Emergency to a specified part of India", "இந்தியாவின் ஒரு குறிப்பிட்ட பகுதிக்கு மட்டும் தேசிய அவசரநிலையை மட்டுப்படுத்த குடியரசுத் தலைவருக்கு அதிகாரம் அளித்தல்",
        "D",
        "Originally, under the 1950 Constitution, a National Emergency could only be proclaimed for the entire territory of India. The 42nd Amendment Act 1976 amended Article 352 to enable the President to limit the operation of a National Emergency to a specified part of the territory of India (or extend it to the whole).",
        "1950 மூல அரசியலமைப்பின்படி, தேசிய அவசரநிலையை இந்தியா முழுமைக்கும் மட்டுமே பிரகடனப்படுத்த முடிந்தது. 1976-ன் 42-வது திருத்தச் சட்டம் சரத்து 352-ஐத் திருத்தி, குடியரசுத் தலைவர் தேசிய அவசரநிலையை இந்தியாவின் ஒரு குறிப்பிட்ட பகுதிக்கு மட்டும் மட்டுப்படுத்த அதிகாரம் அளித்தது.",
        "Option A was introduced by 44th Amendment Act 1978.", "விருப்பம் A 1978-ன் 44-வது திருத்தச் சட்டத்தால் கொண்டுவரப்பட்டது.",
        "Option B was brought by 44th Amendment Act 1978.", "விருப்பம் B 1978-ன் 44-வது திருத்தச் சட்டத்தால் கொண்டுவரப்பட்டது.",
        "Option C was enacted by 44th Amendment Act 1978.", "விருப்பம் C 1978-ன் 44-வது திருத்தச் சட்டத்தால் இயற்றப்பட்டது.",
        "Option D is the historic change introduced by the 42nd Amendment Act 1976 to Article 352.", "விருப்பம் D என்பது சரத்து 352-ல் 1976-ன் 42-வது திருத்தச் சட்டத்தால் கொண்டுவரப்பட்ட வரலாற்று மாற்றமாகும்.",
        "Be careful: Confining National Emergency to a specific part of India was introduced by the 42nd CAA (1976), not the 44th CAA!",
        "கவனமாக இருங்கள்: தேசிய அவசரநிலையை ஒரு குறிப்பிட்ட பகுதிக்கு மட்டுப்படுத்துவது 42-வது திருத்தத்தால் (1976) கொண்டுவரப்பட்டது, 44-வது திருத்தத்தால் அல்ல!",
        "Prior to 1976, any emergency proclamation applied compulsorily to the entire nation.",
        "1976-க்கு முன்பு, எந்தவொரு அவசரநிலைப் பிரகடனமும் கட்டாயமாக நாடு முழுமைக்கும் பொருந்தியது."
    ))

    # 030 - Key A
    qs.append(make_ep_q(
        PREFIX, 30, DIFF, "Constitutional Comparison", "Article 358 vs 359 Remedies",
        "Under Article 359, what exactly is suspended by the Presidential Order during a National Emergency?",
        "சரத்து 359-ன் கீழ், தேசிய அவசரநிலையின் போது குடியரசுத் தலைவரின் ஆணையால் சரியாக எது இடைநிறுத்தப்படுகிறது?",
        "The right to move any court for the enforcement of specified Fundamental Rights", "குறிப்பிட்ட அடிப்படை உரிமைகளை அமல்படுத்துவதற்காக எந்தவொரு நீதிமன்றத்தையும் அணுகும் உரிமை",
        "The Fundamental Rights themselves in their entirety", "அடிப்படை உரிமைகள் முழுமையாகவே தானாக இடைநிறுத்தப்படுகின்றன",
        "The jurisdiction of the Supreme Court under Article 143", "சரத்து 143-ன் கீழ் உச்ச நீதிமன்றத்தின் ஆலோசனைக் கருத்து எல்லை",
        "The right to vote in parliamentary and assembly elections", "பாராளுமன்ற மற்றும் சட்டமன்றத் தேர்தல்களில் வாக்களிக்கும் உரிமை",
        "A",
        "A crucial distinction: Article 358 suspends the rights under Article 19 themselves. However, Article 359 does NOT suspend the Fundamental Rights; it only suspends the RIGHT TO MOVE ANY COURT FOR THE ENFORCEMENT of specified Fundamental Rights (except Articles 20 and 21). The rights theoretically remain alive, but their remedial remedy is suspended.",
        "ஒரு முக்கியமான வேறுபாடு: சரத்து 358 என்பது சரத்து 19-ன் கீழ் உள்ள உரிமைகளையே இடைநிறுத்துகிறது. ஆனால் சரத்து 359 அடிப்படை உரிமைகளை இடைநிறுத்துவதில்லை; அது குறிப்பிடப்பட்ட அடிப்படை உரிமைகளை (சரத்து 20 மற்றும் 21 தவிர) அமல்படுத்துவதற்காக எந்தவொரு நீதிமன்றத்தையும் அணுகும் உரிமையை மட்டுமே இடைநிறுத்துகிறது.",
        "Option A precisely captures the suspension of enforcement remedies under Article 359.", "விருப்பம் A சரத்து 359-ன் கீழ் அமலாக்கத் தீர்வுகள் இடைநிறுத்தப்படுவதைத் துல்லியமாக விளக்குகிறது.",
        "Option B describes Article 358, not Article 359.", "விருப்பம் B சரத்து 358-ஐ விவரிக்கிறது, சரத்து 359-ஐ அல்ல.",
        "Option C is unrelated.", "விருப்பம் C தொடர்பற்றது.",
        "Option D relates to statutory voting rights under RPA 1951, not Article 359.", "விருப்பம் D மக்கள் பிரதிநிதித்துவச் சட்டம் 1951-ன் கீழான வாக்குரிமை தொடர்பானது.",
        "Key Concept: Art 358 = Suspends the rights (Art 19). Art 359 = Suspends the REMEDY (right to move court) for specified rights.",
        "முக்கியக் கருத்து: சரத்து 358 = உரிமைகளையே இடைநிறுத்துகிறது (சரத்து 19). சரத்து 359 = குறிப்பிட்ட உரிமைகளுக்கான தீர்வை (நீதிமன்றத்தை அணுகும் உரிமையை) இடைநிறுத்துகிறது.",
        "Because the rights themselves remain, any executive action taken without legislative backing can be challenged after the emergency ends.",
        "உரிமைகள் அப்படியே நீடிப்பதால், சட்ட அங்கீகாரமின்றி எடுக்கப்படும் நிர்வாக நடவடிக்கைகள் அவசரநிலை முடிந்த பின் சவாலுக்கு உட்படலாம்."
    ))

    # 031 - Key B
    qs.append(make_ep_q(
        PREFIX, 31, DIFF, "Judicial Review", "38th Amendment vs 44th Amendment on Justiciability",
        "Which Constitutional Amendment made the 'satisfaction of the President' in declaring an emergency final and conclusive, beyond the purview of judicial review, which was subsequently deleted by the 44th Amendment Act of 1978?",
        "அவசரநிலையைப் பிரகடனப்படுத்துவதில் 'குடியரசுத் தலைவரின் திருப்தியே' இறுதியானது மற்றும் முடிவானது, அது நீதித்துறை மறுஆய்விற்கு அப்பாற்பட்டது என்று மாற்றிய அரசியலமைப்பு திருத்தம் எது (இது பின்னர் 1978-ன் 44-வது திருத்தத்தால் நீக்கப்பட்டது)?",
        "42nd Amendment Act 1976", "1976-ன் 42-வது திருத்தச் சட்டம்",
        "38th Amendment Act 1975", "1975-ன் 38-வது திருத்தச் சட்டம்",
        "39th Amendment Act 1975", "1975-ன் 39-வது திருத்தச் சட்டம்",
        "40th Amendment Act 1976", "1976-ன் 40-வது திருத்தச் சட்டம்",
        "B",
        "The 38th Constitutional Amendment Act of 1975 made the satisfaction of the President in invoking Articles 352, 356, and 360 final and conclusive, completely barring judicial review in any court. The 44th Constitutional Amendment Act of 1978 subsequently repealed this clause, restoring the power of judicial review.",
        "1975-ன் 38-வது அரசியலமைப்பு திருத்தச் சட்டம், சரத்துகள் 352, 356 மற்றும் 360-ஐப் பயன்படுத்துவதில் குடியரசுத் தலைவரின் திருப்தியே இறுதியானது என்றும், எந்த நீதிமன்றத்திலும் நீதித்துறை மறுஆய்வு செய்ய முடியாது என்றும் மாற்றியது. 1978-ன் 44-வது திருத்தச் சட்டம் பின்னர் இந்த விதியை நீக்கி, நீதித்துறை மறுஆய்வு அதிகாரத்தை மீட்டெடுத்தது.",
        "Option A (42nd CAA) altered many parts of the Constitution, but the emergency non-justiciability clause was introduced specifically by the 38th CAA.", "விருப்பம் A (42-வது சட்டம்) பல பகுதிகளை மாற்றியது, ஆனால் அவசரநிலை மறுஆய்வுத் தடை 38-வது சட்டத்தால் கொண்டுவரப்பட்டது.",
        "Option B is the correct historical constitutional amendment.", "விருப்பம் B சரியான வரலாற்று அரசியலமைப்பு திருத்தமாகும்.",
        "Option C (39th CAA) barred judicial review of elections of PM and Speaker.", "விருப்பம் C (39-வது சட்டம்) பிரதமர் மற்றும் சபாநாயகர் தேர்தல்கள் மீதான நீதிமன்ற மறுஆய்வைத் தடுத்தது.",
        "Option D dealt with territorial waters and maritime zones.", "விருப்பம் D கடல்சார் மண்டலங்கள் தொடர்பானது.",
        "Constitutional History: 38th CAA (1975) barred judicial review of emergency; 44th CAA (1978) deleted that bar and restored judicial scrutiny.",
        "அரசியலமைப்பு வரலாறு: 38-வது திருத்தம் (1975) அவசரநிலை மீதான நீதித்துறை மறுஆய்வைத் தடுத்தது; 44-வது திருத்தம் (1978) அதை நீக்கி நீதித்துறை கண்காணிப்பை மீட்டெடுத்தது.",
        "This restored the constitutional doctrine of checks and balances over executive emergency proclamations.",
        "இது நிர்வாக அவசரநிலைப் பிரகடனங்கள் மீதான அதிகார சமநிலை கோட்பாட்டை மீட்டெடுத்தது."
    ))

    # 032 - Key C
    qs.append(make_ep_q(
        PREFIX, 32, DIFF, "Federal Dynamics", "Article 357 - Legislative Delegation",
        "When the powers of a State Legislature are declared under Article 356 to be exercisable by or under the authority of Parliament, Parliament may, under Article 357(1)(a), confer that law-making power upon:",
        "சரத்து 356-ன் கீழ் ஒரு மாநில சட்டமன்றத்தின் அதிகாரங்கள் பாராளுமன்றத்தால் பயன்படுத்தப்பட வேண்டும் என்று அறிவிக்கப்படும் போது, சரத்து 357(1)(a)-ன் கீழ் பாராளுமன்றம் அந்தச் சட்டம் இயற்றும் அதிகாரத்தை யாரிடம் வழங்க முடியும்?",
        "The Chief Minister in exile", "பதவி நீக்கம் செய்யப்பட்ட முதலமைச்சரிடம்",
        "The Chief Justice of the State High Court", "மாநில உயர் நீதிமன்ற தலைமை நீதிபதியிடம்",
        "The President of India, with power to delegate it further to specified authorities", "இந்தியக் குடியரசுத் தலைவரிடம், மேலும் அவர் அதை குறிப்பிட்ட அதிகாரிகளுக்கு வழங்க அனுமதிக்கும் அதிகாரத்துடன்",
        "The Attorney General of India", "இந்திய தலைமை வழக்கறிஞரிடம்",
        "C",
        "Under Article 357(1)(a), Parliament is competent to confer on the President the power of the Legislature of the State to make laws, and to authorise the President to delegate, subject to any conditions he may think fit to impose, the power so conferred to any other authority to be specified by him in that behalf (commonly exercised in consultation with a parliamentary consultative committee).",
        "சரத்து 357(1)(a)-ன் படி, மாநில சட்டமன்றத்தின் சட்டம் இயற்றும் அதிகாரத்தை குடியரசுத் தலைவருக்கு வழங்கவும், மேலும் குடியரசுத் தலைவர் தகுந்த நிபந்தனைகளுடன் அந்த அதிகாரத்தை தாம் குறிப்பிடும் பிற அதிகாரிக்கு வழங்க அதிகாரம் அளிக்கவும் பாராளுமன்றத்திற்கு தகுதி உண்டு.",
        "Option A is completely baseless.", "விருப்பம் A முற்றிலும் தவறானது.",
        "Option B violates the separation of powers doctrine.", "விருப்பம் B அதிகாரப் பகிர்வுக் கோட்பாட்டை மீறுகிறது.",
        "Option C is the exact legislative delegation mechanism provided under Article 357(1)(a).", "விருப்பம் C என்பது சரத்து 357(1)(a)-ன் கீழ் வழங்கப்பட்டுள்ள துல்லியமான சட்டப் பிரதிநிதித்துவ வழிமுறையாகும்.",
        "Option D is an executive legal officer, not a delegated law-making body.", "விருப்பம் D சட்ட அதிகாரி மட்டுமே, சட்டம் இயற்றும் அமைப்பு அல்ல.",
        "President's Acts: Under Art 357(1)(a), laws enacted by the President under delegated state powers are known as 'President's Acts'.",
        "குடியரசுத் தலைவர் சட்டங்கள்: சரத்து 357(1)(a)-ன் கீழ் மாநில அதிகாரத்தில் குடியரசுத் தலைவரால் இயற்றப்படும் சட்டங்கள் 'குடியரசுத் தலைவர் சட்டங்கள்' என அழைக்கப்படுகின்றன.",
        "In practice, the President consults a parliamentary consultative committee formed with MPs from that State.",
        "நடைமுறையில், அந்த மாநில நாடாளுமன்ற உறுப்பினர்களைக் கொண்ட ஆலோசனைக் குழுவுடன் குடியரசுத் தலைவர் கலந்தாலோசிக்கிறார்."
    ))

    # 033 - Key D
    qs.append(make_ep_q(
        PREFIX, 33, DIFF, "Financial Relations", "Sanctioning State Expenditure under President's Rule",
        "When the Lok Sabha is not in session during President's Rule in a State, who is authorized under Article 357(1)(c) to sanction expenditure from the Consolidated Fund of that State pending parliamentary sanction?",
        "ஒரு மாநிலத்தில் குடியரசுத் தலைவர் ஆட்சியின் போது மக்களவை அமர்வில் இல்லாத போது, பாராளுமன்ற ஒப்புதல் நிலுவையில் இருக்கும் வரை அந்த மாநிலத்தின் தொகுப்பு நிதியிலிருந்து செலவினங்களை அனுமதிக்க சரத்து 357(1)(c)-ன் கீழ் யாருக்கு அதிகாரம் உள்ளது?",
        "The Comptroller and Auditor General of India", "இந்திய தலைமை கணக்குத் தணிக்கையாளர்",
        "The Governor of the State acting alone", "தனித்து செயல்படும் மாநில ஆளுநர்",
        "The Union Finance Minister", "மத்திய நிதி அமைச்சர்",
        "The President of India", "இந்தியக் குடியரசுத் தலைவர்",
        "D",
        "Under Article 357(1)(c), when the House of the People is not in session, the President may authorise expenditure from the Consolidated Fund of the State pending sanction of such expenditure by Parliament.",
        "சரத்து 357(1)(c)-ன் கீழ், மக்களவை அமர்வில் இல்லாத போது, பாராளுமன்றத்தின் ஒப்புதல் நிலுவையில் இருக்கும் நிலையில் மாநிலத் தொகுப்பு நிதியிலிருந்து செலவினங்களை மேற்கொள்ள குடியரசுத் தலைவர் அதிகாரம் அளிக்கலாம்.",
        "Option A audits expenditures; does not sanction them.", "விருப்பம் A கணக்குகளைத் தணிக்கை செய்கிறது; செலவினங்களை அனுமதிப்பதில்லை.",
        "Option B is incorrect; the Governor cannot authorize expenditure from the Consolidated Fund on his own during Article 356.", "விருப்பம் B தவறானது; சரத்து 356-ன் போது ஆளுநர் சுயமாக தொகுப்பு நிதியிலிருந்து செலவினங்களை அனுமதிக்க முடியாது.",
        "Option C is incorrect; authority rests constitutionally with the President.", "விருப்பம் C தவறானது; அதிகாரம் அரசியலமைப்பு ரீதியாக குடியரசுத் தலைவரிடம் உள்ளது.",
        "Option D is the precise constitutional officer designated under Article 357(1)(c).", "விருப்பம் D சரத்து 357(1)(c)-ன் கீழ் நியமிக்கப்பட்ட துல்லியமான அரசியலமைப்பு அதிகாரியாவார்.",
        "Emergency Fiscal Operation: When Lok Sabha is not sitting, President authorizes withdrawals from State Consolidated Fund.",
        "அவசரநிலை நிதி செயல்பாடு: மக்களவை கூடாத போது, மாநிலத் தொகுப்பு நிதியிலிருந்து பணத்தை எடுக்க குடியரசுத் தலைவர் அனுமதி அளிக்கிறார்.",
        "Once Parliament meets, this expenditure must be formally ratified.",
        "பாராளுமன்றம் கூடியவுடன் இந்தச் செலவினங்கள் முறையாக அங்கீகரிக்கப்பட வேண்டும்."
    ))

    # 034 - Key A
    qs.append(make_ep_q(
        PREFIX, 34, DIFF, "Constitutional Comparison", "Article 358 vs 359 Immunity of Laws",
        "Under both Article 358 and Article 359, what condition was added by the 44th Amendment Act 1978 to protect laws from being challenged for violating fundamental rights?",
        "சரத்து 358 மற்றும் சரத்து 359 ஆகிய இரண்டின் கீழும், அடிப்படை உரிமைகளை மீறியதாக சட்டங்கள் சவாலுக்கு உட்படுத்தப்படுவதிலிருந்து பாதுகாக்க 1978-ன் 44-வது திருத்தச் சட்டத்தால் என்ன நிபந்தனை சேர்க்கப்பட்டது?",
        "The law must contain a specific recital that it is in relation to the emergency in operation", "அந்தச் சட்டம் அமலில் உள்ள அவசரநிலை தொடர்புடையது என்ற குறிப்பிட்ட அறிவிப்பைக் கொண்டிருக்க வேண்டும்",
        "The law must be ratified by at least half of the state legislatures", "அந்தச் சட்டம் குறைந்தபட்சம் பாதி மாநில சட்டமன்றங்களால் அங்கீகரிக்கப்பட வேண்டும்",
        "The law must receive the unanimous assent of the Union Cabinet", "அந்தச் சட்டம் மத்திய அமைச்சரவையின் ஒருமனதான ஒப்புதலைப் பெற வேண்டும்",
        "The law must have been passed before the proclamation of emergency was issued", "அந்தச் சட்டம் அவசரநிலைப் பிரகடனம் வெளியிடப்படுவதற்கு முன்பே நிறைவேற்றப்பட்டிருக்க வேண்டும்",
        "A",
        "The 44th Amendment Act 1978 amended both Articles 358 and 359 to provide that only those laws that contain a specific recital stating they are related to the proclamation of emergency (and executive actions taken under such laws) enjoy immunity from challenge under Fundamental Rights. Ordinary laws not containing such recital remain fully vulnerable to challenge.",
        "1978-ன் 44-வது திருத்தச் சட்டம் சரத்துகள் 358 மற்றும் 359 இரண்டையும் திருத்தி, அவசரநிலைப் பிரகடனத்துடன் தொடர்புடையது என்ற குறிப்பிட்ட அறிவிப்பைக் கொண்டுள்ள சட்டங்கள் மட்டுமே அடிப்படை உரிமைகள் மீறல் சவாலிலிருந்து விலக்குப் பெறும் என்று வகைசெய்தது. அத்தகைய அறிவிப்பு இல்லாத சாதாரண சட்டங்கள் நீதிமன்ற ஆய்வுக்கு உட்பட்டவை.",
        "Option A accurately quotes the 'recital condition' inserted by the 44th CAA.", "விருப்பம் A 44-வது திருத்தத்தால் சேர்க்கப்பட்ட 'அறிவிப்பு நிபந்தனையை' துல்லியமாகக் கூறுகிறது.",
        "Option B is false; state ratification is not needed.", "விருப்பம் B தவறு; மாநில ஒப்புதல் தேவையில்லை.",
        "Option C is not a legislative immunity requirement.", "விருப்பம் C சட்ட விலக்கு நிபந்தனை அல்ல.",
        "Option D is false; laws passed during emergency can enjoy protection if they contain the recital.", "விருப்பம் D தவறு; அறிவிப்பைக் கொண்டிருந்தால் அவசரநிலையின் போது இயற்றப்பட்ட சட்டங்களும் பாதுகாப்புப் பெறலாம்.",
        "44th Amendment Safeguard: Only laws containing a recital that they are in relation to the emergency are protected from fundamental rights challenge.",
        "44-வது திருத்தப் பாதுகாப்பு: அவசரநிலையுடன் தொடர்புடையது என்ற அறிவிப்பைக் கொண்ட சட்டங்கள் மட்டுமே அடிப்படை உரிமை சவாலிலிருந்து பாதுகாக்கப்படுகின்றன.",
        "This prevented the government from shielding unrelated arbitrary legislation behind the screen of emergency.",
        "அரசு தொடர்பற்ற தன்னிச்சையான சட்டங்களை அவசரநிலையின் திரைக்குப் பின்னால் மறைப்பதைத் தடுக்க இது கொண்டுவரப்பட்டது."
    ))

    # 035 - Key B
    qs.append(make_ep_q(
        PREFIX, 35, DIFF, "National Emergency - Extension", "Six-Month Periodic Parliamentary Approval",
        "Before the 44th Constitutional Amendment Act 1978, once approved by Parliament, for how long did a proclamation of National Emergency remain in force without further parliamentary approval?",
        "1978-ன் 44-வது அரசியலமைப்பு திருத்தச் சட்டத்திற்கு முன்பு, பாராளுமன்றத்தால் ஒருமுறை அங்கீகரிக்கப்பட்ட தேசிய அவசரநிலைப் பிரகடனம், மேலும் பாராளுமன்ற ஒப்புதல் ஏதுமின்றி எவ்வளவு காலம் வரை அமலில் இருக்க முடிந்தது?",
        "Only for 1 year", "1 ஆண்டு மட்டுமே",
        "Indefinitely, until revoked by the executive", "நிர்வாகத்தால் திரும்பப் பெறப்படும் வரை காலவரையின்றி",
        "For 6 months only", "6 மாதங்கள் மட்டுமே",
        "For a maximum of 3 years", "அதிகபட்சமாக 3 ஆண்டுகள் வரை",
        "B",
        "Originally under the 1950 Constitution, once approved by Parliament, a proclamation of National Emergency remained in operation INDEFINITELY so long as the Executive did not revoke it. The 44th Amendment Act 1978 introduced the crucial check requiring periodic parliamentary approval every six months.",
        "1950 மூல அரசியலமைப்பின்படி, பாராளுமன்றம் ஒருமுறை ஒப்புதல் அளித்த பிறகு, நிர்வாகம் அதைத் திரும்பப் பெறாத வரை தேசிய அவசரநிலைப் பிரகடனம் காலவரையின்றி நீடித்தது. 1978-ன் 44-வது திருத்தச் சட்டம் தான் ஒவ்வொரு ஆறு மாதங்களுக்கும் பாராளுமன்றத்தின் மறு ஒப்புதல் பெற வேண்டும் என்ற முக்கிய கட்டுப்பாட்டைக் கொண்டுவந்தது.",
        "Option A is incorrect.", "விருப்பம் A தவறானது.",
        "Option B is the exact pre-1978 constitutional loophole that was exploited during 1962-1968 and 1971-1977.", "விருப்பம் B என்பது 1962-1968 மற்றும் 1971-1977 காலகட்டங்களில் பயன்படுத்தப்பட்ட 1978-க்கு முந்தைய அரசியலமைப்பு நிலையாகும்.",
        "Option C is the rule introduced by the 44th Amendment, not the pre-existing rule.", "விருப்பம் C என்பது 44-வது திருத்தத்தால் கொண்டுவரப்பட்ட விதி, ஏற்கனவே இருந்த விதி அல்ல.",
        "Option D applies to President's Rule.", "விருப்பம் D குடியரசுத் தலைவர் ஆட்சிக்குப் பொருந்தும்.",
        "Before 1978: One approval = Emergency in force indefinitely! Post-1978: Compulsory re-approval every 6 months.",
        "1978-க்கு முன்பு: ஒரு முறை ஒப்புதல் = காலவரையின்றி அமலில் இருக்கும்! 1978-க்குப் பிறகு: ஒவ்வொரு 6 மாதங்களுக்கும் கட்டாய மறு ஒப்புதல்.",
        "This periodic review ensures that the executive must continually justify the extraordinary situation to Parliament.",
        "இந்த குறிப்பிட்ட கால மறுஆய்வு, நிர்வாகம் பாராளுமன்றத்திற்கு அசாதாரண சூழ்நிலையைத் தொடர்ந்து நியாயப்படுத்துவதை உறுதி செய்கிறது."
    ))

    # 036 - Key C
    qs.append(make_ep_q(
        PREFIX, 36, DIFF, "National Emergency - Territorial Scope", "Extension to Other Areas under 42nd CAA",
        "Under the proviso to Article 353 and Article 358 (inserted by the 42nd Amendment Act 1976), if a National Emergency is proclaimed in only a specific part of India, can the executive and legislative powers of the Centre be extended to other areas where emergency is NOT in operation?",
        "சரத்து 353 மற்றும் சரத்து 358-ன் நிபந்தனை விதியின் கீழ் (1976-ன் 42-வது திருத்தத்தால் சேர்க்கப்பட்டது), இந்தியாவின் ஒரு குறிப்பிட்ட பகுதியில் மட்டுமே தேசிய அவசரநிலை பிரகடனப்படுத்தப்பட்டிருந்தால், அவசரநிலை அமலில் இல்லாத பிற பகுதிகளுக்கும் மத்திய அரசின் நிர்வாக மற்றும் சட்ட அதிகாரங்களை விரிவுபடுத்த முடியுமா?",
        "No, under no circumstances can central emergency powers cross the boundary of the notified area.", "இல்லை, எந்தச் சூழ்நிலையிலும் மத்திய அவசரநிலை அதிகாரங்கள் அறிவிக்கப்பட்ட பகுதியின் எல்லையைத் தாண்ட முடியாது.",
        "Only if the Governors of the neighboring non-emergency states give written consent.", "அண்டை மாநிலங்களின் ஆளுநர்கள் எழுத்துப்பூர்வ ஒப்புதல் அளித்தால் மட்டுமே.",
        "Yes, if activities in that non-emergency area are affecting the security of the area where emergency is in operation.", "ஆம், அவசரநிலை அமலில் உள்ள பகுதியின் பாதுகாப்பை அந்த அவசரநிலை இல்லாத பகுதியின் செயல்பாடுகள் பாதிக்கும் பட்சத்தில்.",
        "Only after a fresh national proclamation is issued covering the whole of India.", "இந்தியா முழுவதையும் உள்ளடக்கிய புதிய தேசிய பிரகடனம் வெளியிடப்பட்ட பிறகு மட்டுமே.",
        "C",
        "The 42nd Amendment Act 1976 added provisos to Articles 353 and 358 providing that where a proclamation of emergency is confined to only a part of the territory of India, the executive power of the Union to give directions and the power of Parliament to make laws can be extended to any State other than the State where emergency is in force, if activities in that other area are prejudicial to the security of the emergency area.",
        "1976-ன் 42-வது திருத்தச் சட்டம் சரத்துகள் 353 மற்றும் 358-ல் நிபந்தனைகளைச் சேர்த்தது. அதன்படி, அவசரநிலை நாட்டின் ஒரு குறிப்பிட்ட பகுதிக்கு மட்டுமே வரையறுக்கப்பட்டிருந்தாலும், அந்தப் பகுதியின் பாதுகாப்பிற்கு ஊறு விளைவிக்கும் செயல்கள் பிற பகுதிகளில் நடைபெற்றால், அவசரநிலை இல்லாத மாநிலங்களுக்கும் மத்திய அரசின் வழிகாட்டுதல் மற்றும் சட்ட அதிகாரங்களை விரிவுபடுத்த முடியும்.",
        "Option A is incorrect; the 42nd Amendment expressly provided for cross-territorial reach.", "விருப்பம் A தவறானது; 42-வது திருத்தம் பிராந்தியங்களுக்கு அப்பால் அதிகாரம் செல்ல வெளிப்படையாக வழிவகை செய்தது.",
        "Option B has no constitutional requirement for gubernatorial consent.", "விருப்பம் B தவறானது; ஆளுநர் ஒப்புதல் அரசியலமைப்பு ரீதியாக தேவையில்லை.",
        "Option C accurately captures the constitutional security nexus rule.", "விருப்பம் C அரசியலமைப்பு பாதுகாப்பு தொடர்பு விதியைத் துல்லியமாகக் கூறுகிறது.",
        "Option D is not required.", "விருப்பம் D தேவையில்லை.",
        "Spillover Power: Center's power can extend to a non-emergency state if security of the emergency area is threatened from there.",
        "அதிகார நீட்டிப்பு: அவசரநிலை உள்ள பகுதியின் பாதுகாப்பிற்கு அங்கிருந்து அச்சுறுத்தல் ஏற்பட்டால், அவசரநிலை இல்லாத மாநிலத்திற்கும் மத்திய அதிகாரம் பரவும்.",
        "This prevents hostile elements from using adjacent states as safe havens during localized emergencies.",
        "உள்ளூர் அவசரநிலைகளின் போது அருகிலுள்ள மாநிலங்களை எதிரிகள் புகலிடமாகப் பயன்படுத்துவதை இது தடுக்கிறது."
    ))

    # 037 - Key D
    qs.append(make_ep_q(
        PREFIX, 37, DIFF, "President's Rule - Historical Statistics", "First Use of President's Rule in Free India",
        "In which State was President's Rule (Article 356) imposed for the VERY FIRST TIME in independent India, and in which year?",
        "சுதந்திர இந்தியாவில் மிக முதன்முதலாக எந்த மாநிலத்தில் மற்றும் எந்த ஆண்டில் குடியரசுத் தலைவர் ஆட்சி (சரத்து 356) அமல்படுத்தப்பட்டது?",
        "Kerala in 1959", "கேரளா - 1959",
        "Tamil Nadu in 1976", "தமிழ்நாடு - 1976",
        "Uttar Pradesh in 1968", "உத்தரப் பிரதேசம் - 1968",
        "Punjab (then East Punjab) in 1951", "பஞ்சாப் (அப்போதைய கிழக்கு பஞ்சாப்) - 1951",
        "D",
        "President's Rule was imposed for the first time in independent India in Punjab (then known as East Punjab) on 20 June 1951, due to factional fighting within the ruling Congress party leading to the resignation of Chief Minister Gopichand Bhargava.",
        "சுதந்திர இந்தியாவில் முதல்முறையாக குடியரசுத் தலைவர் ஆட்சி 20 ஜூன் 1951 அன்று பஞ்சாபில் (அப்போது கிழக்கு பஞ்சாப்) ஆளும் காங்கிரஸ் கட்சிக்குள் ஏற்பட்ட உள்கட்சிப் பூசல் மற்றும் முதலமைச்சர் கோபிசந்த் பார்கவா ராஜினாமா செய்ததன் காரணமாக அமல்படுத்தப்பட்டது.",
        "Option A: Kerala in 1959 (dismissal of E.M.S. Namboodiripad's Communist ministry) was the first dismissal of a majority government, but not the first use of Article 356.", "விருப்பம் A: கேரளா 1959 (ஈ.எம்.எஸ். நம்பூதிரிபாட்டின் கம்யூனிஸ்ட் அரசு கலைப்பு) பெரும்பான்மை அரசு கலைக்கப்பட்ட முதல் நிகழ்வு, ஆனால் சரத்து 356-ன் முதல் பயன்பாடு அல்ல.",
        "Option B: Tamil Nadu saw President's Rule in 1976 (dismissal of Karunanidhi ministry).", "விருப்பம் B: தமிழ்நாட்டில் 1976-ல் கருணாநிதி அரசு கலைக்கப்பட்டு முதல்முறையாக குடியரசுத் தலைவர் ஆட்சி வந்தது.",
        "Option C: Uttar Pradesh was first placed under Article 356 in 1968.", "விருப்பம் C: உத்தரப் பிரதேசம் 1968-ல் முதன்முதலில் சரத்து 356-ன் கீழ் வந்தது.",
        "Option D is the historic first: Punjab in 1951.", "விருப்பம் D வரலாற்று ரீதியான முதலிடம்: பஞ்சாப் 1951.",
        "First Use of Art 356: Punjab (June 1951). Kerala 1959 was the first dismissal of an elected majority non-Congress government.",
        "சரத்து 356-ன் முதல் பயன்பாடு: பஞ்சாப் (ஜூன் 1951). கேரளா 1959 என்பது தேர்ந்தெடுக்கப்பட்ட பெரும்பான்மை அரசு கலைக்கப்பட்ட முதல் நிகழ்வு.",
        "Dr. B.R. Ambedkar had hoped Article 356 would remain a 'dead letter', but Punjab in 1951 proved otherwise.",
        "சரத்து 356 ஒரு 'செயலற்ற எழுத்தாக' இருக்கும் என்று டாக்டர் அம்பேத்கர் நம்பினார், ஆனால் 1951 பஞ்சாப் நிகழ்வு அதை மாற்றியது."
    ))

    # 038 - Key A
    qs.append(make_ep_q(
        PREFIX, 38, DIFF, "Historical Precedent", "First Use of President's Rule in Tamil Nadu",
        "In which year was President's Rule under Article 356 imposed for the FIRST TIME in the State of Tamil Nadu?",
        "தமிழ்நாட்டில் முதன்முறையாக எந்த ஆண்டில் சரத்து 356-ன் கீழ் குடியரசுத் தலைவர் ஆட்சி அமல்படுத்தப்பட்டது?",
        "1976", "1976",
        "1980", "1980",
        "1988", "1988",
        "1991", "1991",
        "A",
        "President's Rule was imposed in Tamil Nadu for the first time on 31 January 1976, when the DMK government headed by M. Karunanidhi was dismissed by the Centre during the National Emergency, on grounds of alleged corruption and maladministration, leading to the appointment of the Sarkaria Inquiry Commission.",
        "தமிழ்நாட்டில் முதன்முறையாக 31 ஜனவரி 1976 அன்று குடியரசுத் தலைவர் ஆட்சி அமல்படுத்தப்பட்டது. தேசிய அவசரநிலையின் போது ஊழல் மற்றும் நிர்வாகச் சீர்கேடு குற்றச்சாட்டுகளின் அடிப்படையில் மு. கருணாநிதி தலைமையிலான திமுக அரசு மத்திய அரசால் கலைக்கப்பட்டு, சர்க்காரியா விசாரணைக் குழு அமைக்கப்பட்டது.",
        "Option A is the historically accurate year of the first imposition in Tamil Nadu.", "விருப்பம் A தமிழ்நாட்டில் முதல்முறை அமல்படுத்தப்பட்ட சரியான வரலாற்று ஆண்டாகும்.",
        "Option B: 1980 saw the dismissal of the M.G. Ramachandran (AIADMK) government after Indira Gandhi returned to power.", "விருப்பம் B: இந்திரா காந்தி மீண்டும் ஆட்சிக்கு வந்த பிறகு 1980-ல் எம்.ஜி.ஆர் அரசு கலைக்கப்பட்டது.",
        "Option C: 1988 saw President's Rule following the death of M.G. Ramachandran and subsequent political factionalism.", "விருப்பம் C: எம்.ஜி.ஆர் மறைவுக்குப் பிறகு 1988-ல் உள்கட்சிப் பூசலால் குடியரசுத் தலைவர் ஆட்சி வந்தது.",
        "Option D: 1991 saw the dismissal of the Karunanidhi government citing LTTE activities.", "விருப்பம் D: விடுதலைப் புலிகள் செயல்பாடுகளைக் கூறி 1991-ல் கருணாநிதி அரசு கலைக்கப்பட்டது.",
        "TNPSC Milestone: President's Rule has been imposed 4 times in Tamil Nadu: 1976 (first time), 1980, 1988, and 1991.",
        "TNPSC மைல்கல்: தமிழ்நாட்டில் குடியரசுத் தலைவர் ஆட்சி 4 முறை அமல்படுத்தப்பட்டுள்ளது: 1976 (முதல் முறை), 1980, 1988, மற்றும் 1991.",
        "The 1976 dismissal occurred just weeks before the five-year term of the Tamil Nadu assembly was due to end.",
        "1976 கலைப்பு நிகழ்வு தமிழ்நாடு சட்டமன்றத்தின் ஐந்து ஆண்டு காலம் முடிவடைய சில வாரங்களே இருந்த நிலையில் நிகழ்ந்தது."
    ))

    # 039 - Key B
    qs.append(make_ep_q(
        PREFIX, 39, DIFF, "Constitutional Landmark", "S.R. Bommai Grounds of Floor Test",
        "According to the Supreme Court's ruling in the S.R. Bommai case (1994), what is the ONLY constitutionally valid method for testing whether a Ministry has lost the confidence of the Legislative Assembly?",
        "எஸ்.ஆர். பொம்மை வழக்கில் (1994) உச்ச நீதிமன்றத்தின் தீர்ப்பின்படி, ஓர் அமைச்சரவை சட்டமன்றத்தின் நம்பிக்கையை இழந்துவிட்டதா என்பதைச் சோதிக்கும் ஒரே அரசியலமைப்பு ரீதியான வழி எது?",
        "Subjective satisfaction of the Governor based on private petitions", "தனிப்பட்ட மனுக்களின் அடிப்படையில் ஆளுநரின் அகநிலை திருப்தி",
        "A floor test conducted on the floor of the Legislative Assembly", "சட்டமன்றப் பேரவையின் தளத்தில் நடத்தப்படும் நம்பிக்கை வாக்கெடுப்பு (Floor Test)",
        "A confidential report by the Intelligence Bureau submitted to the Union Home Ministry", "மத்திய உள்துறை அமைச்சகத்திற்கு உளவுத்துறை சமர்ப்பிக்கும் ரகசிய அறிக்கை",
        "A signature campaign submitted by opposition MLAs to the President", "எதிர்க்கட்சி சட்டமன்ற உறுப்பினர்கள் குடியரசுத் தலைவரிடம் சமர்ப்பிக்கும் கையெழுத்துப் பிரச்சாரப் பட்டியல்",
        "B",
        "In the Bommai judgment (1994), the Supreme Court laid down that the floor of the Legislative Assembly is the ONLY constitutionally acceptable place to test the majority of the Ministry. The Governor cannot decide whether a government has lost its majority through private subjective assessment in Raj Bhavan.",
        "பொம்மை தீர்ப்பில் (1994), ஓர் அமைச்சரவையின் பெரும்பான்மையைச் சோதிப்பதற்கு சட்டமன்றப் பேரவையின் தளம் (Floor Test) மட்டுமே அரசியலமைப்பு ரீதியாக ஏற்றுக்கொள்ளக்கூடிய ஒரே இடம் என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது. ஆளுநர் தனது ராஜ்பவனில் அமர்ந்து தனிப்பட்ட முறையில் இதைத் தீர்மானிக்க முடியாது.",
        "Option A was precisely what the Supreme Court prohibited.", "விருப்பம் A என்பது உச்ச நீதிமன்றம் திட்டவட்டமாக தடை செய்த நடைமுறையாகும்.",
        "Option B is the core constitutional mandate established by Bommai.", "விருப்பம் B என்பது பொம்மை வழக்கால் நிறுவப்பட்ட முக்கிய அரசியலமைப்பு ஆணையாகும்.",
        "Option C has no legal authority to determine legislative confidence.", "விருப்பம் C சட்டமன்ற நம்பிக்கையைத் தீர்மானிக்க சட்டப்பூர்வ அதிகாரம் அற்றது.",
        "Option D was held invalid as signatures can be manipulated; voting on the floor of the House is mandatory.", "விருப்பம் D செல்லாது எனப்பட்டது; பேரவையின் தளத்தில் வாக்களிப்பதே கட்டாயமாகும்.",
        "Bommai Doctrine: 'Floor Test on the floor of the Assembly is mandatory' to test majority; Raj Bhavan headcount is unconstitutional.",
        "பொம்மை கோட்பாடு: பெரும்பான்மையைச் சோதிக்க 'சட்டமன்றத் தளத்தில் நம்பிக்கை வாக்கெடுப்பு கட்டாயம்'; ஆளுநர் மாளிகை கணக்கெடுப்பு அரசியலமைப்பிற்கு எதிரானது.",
        "This ended the practice of Governors unilaterally dismissing ministries without calling an assembly session.",
        "சட்டமன்றக் கூட்டத்தைக் கூட்டாமல் ஆளுநர்கள் தன்னிச்சையாக அரசுகளைக் கலைக்கும் நடைமுறைக்கு இது முற்றுப்புள்ளி வைத்தது."
    ))

    # 040 - Key C
    qs.append(make_ep_q(
        PREFIX, 40, DIFF, "Constitutional Landmark", "Secularism as Basic Structure in Bommai",
        "In S.R. Bommai v. Union of India (1994), the Supreme Court upheld the dismissal of BJP governments in Madhya Pradesh, Rajasthan, and Himachal Pradesh following the Babri Masjid demolition on which constitutional ground?",
        "எஸ்.ஆர். பொம்மை எதிர் இந்திய ஒன்றியம் (1994) வழக்கில், பாபர் மசூதி இடிப்பைத் தொடர்ந்து மத்தியப் பிரதேசம், ராஜஸ்தான் மற்றும் இமாச்சலப் பிரதேசத்தில் பாஜக அரசுகள் கலைக்கப்பட்டதை எந்த அரசியலமைப்பு அடிப்படையில் உச்ச நீதிமன்றம் உறுதி செய்தது?",
        "Failure to comply with economic directions under Article 360", "சரத்து 360-ன் கீழ் பொருளாதார வழிகாட்டுதல்களைப் பின்பற்றத் தவறியமை",
        "Inability to collect land revenues under Article 268", "சரத்து 268-ன் கீழ் நில வருவாயைச் சேகரிக்க இயலாமை",
        "Secularism is a basic feature of the Constitution, and any State government acting against secularism is liable to action under Article 356", "மதச்சார்பின்மை என்பது அரசியலமைப்பின் அடிப்படைக் கட்டமைப்பாகும், மதச்சார்பின்மைக்கு எதிராகச் செயல்படும் எந்தவொரு மாநில அரசும் சரத்து 356-ன் கீழ் நடவடிக்கைக்கு உட்பட்டது",
        "Armed rebellion by state police forces against the Union", "மத்திய அரசுக்கு எதிராக மாநிலக் காவல்துறையினர் நடத்திய ஆயுதமேந்திய கிளர்ச்சி",
        "C",
        "In the Bommai case, the Supreme Court held that 'Secularism' is a basic feature of the Indian Constitution. If a State government pursues non-secular policies or acts against secular principles, it constitutes a breakdown of constitutional machinery in that State, justifying the invocation of Article 356.",
        "பொம்மை வழக்கில், 'மதச்சார்பின்மை' என்பது இந்திய அரசியலமைப்பின் அடிப்படைக் கட்டமைப்பு என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது. ஒரு மாநில அரசு மதச்சார்பற்ற கொள்கைகளுக்கு எதிராகச் செயல்பட்டால், அது அந்த மாநிலத்தில் அரசியலமைப்பு இயந்திரம் முறிவடைந்ததாகக் கருதப்படும், இதனால் சரத்து 356-ஐப் பயன்படுத்துவது நியாயமானது.",
        "Option A refers to financial emergency.", "விருப்பம் A நிதி அவசரநிலையைக் குறிக்கிறது.",
        "Option B is unrelated.", "விருப்பம் B தொடர்பற்றது.",
        "Option C is the historic constitutional link established between secularism, basic structure, and Article 356.", "விருப்பம் C என்பது மதச்சார்பின்மை, அடிப்படைக் கட்டமைப்பு மற்றும் சரத்து 356 ஆகியவற்றிற்கு இடையே நிறுவப்பட்ட வரலாற்றுத் தொடர்பாகும்.",
        "Option D did not occur in this case.", "விருப்பம் D இந்த வழக்கில் நிகழவில்லை.",
        "Constitutional Precedent: Secularism is Basic Structure; state governments violating secular principles can be dismissed under Article 356.",
        "அரசியலமைப்பு முன்னுதாரணம்: மதச்சார்பின்மை என்பது அடிப்படைக் கட்டமைப்பு; மதச்சார்பற்ற கொள்கைகளை மீறும் மாநில அரசுகளை சரத்து 356-ன் கீழ் கலைக்கலாம்.",
        "This demonstrated that Article 356 can be legitimately invoked to protect foundational constitutional values.",
        "அடிப்படை அரசியலமைப்பு விழுமியங்களைப் பாதுகாக்க சரத்து 356-ஐ நியாயமாகப் பயன்படுத்த முடியும் என்பதை இது நிரூபித்தது."
    ))

    # 041 - Key D
    qs.append(make_ep_q(
        PREFIX, 41, DIFF, "Constitutional Comparison", "Suspension of Fundamental Rights Grounds",
        "Which of the following is NOT suspended during a National Emergency proclaimed on the grounds of 'armed rebellion'?",
        "'ஆயுதமேந்திய கிளர்ச்சி' என்ற காரணத்தின் அடிப்படையில் அறிவிக்கப்பட்ட தேசிய அவசரநிலையின் போது பின்வருவனவற்றில் எது இடைநிறுத்தப்படாது?",
        "Right to move court for Article 14 enforcement (if President specifies it)", "சரத்து 14 அமலாக்கத்திற்காக நீதிமன்றத்தை அணுகும் உரிமை (குடியரசுத் தலைவர் குறிப்பிட்டால்)",
        "Right to move court for Article 19 enforcement (if President specifies it)", "சரத்து 19 அமலாக்கத்திற்காக நீதிமன்றத்தை அணுகும் உரிமை (குடியரசுத் தலைவர் குறிப்பிட்டால்)",
        "Right to move court for Article 22 enforcement (if President specifies it)", "சரத்து 22 அமலாக்கத்திற்காக நீதிமன்றத்தை அணுகும் உரிமை (குடியரசுத் தலைவர் குறிப்பிட்டால்)",
        "The fundamental freedoms guaranteed under Article 19 automatically under Article 358", "சரத்து 358-ன் கீழ் தானாகவே இடைநிறுத்தப்படும் சரத்து 19-ன் அடிப்படை சுதந்திரங்கள்",
        "D",
        "Under Article 358, the six fundamental freedoms guaranteed by Article 19 are automatically suspended ONLY during an external emergency (war or external aggression). During an internal emergency declared on grounds of armed rebellion, Article 19 is NEVER automatically suspended under Article 358.",
        "சரத்து 358-ன் கீழ், போர் அல்லது வெளிநாட்டு ஆக்கிரமிப்பு (வெளிப்புற அவசரநிலை) ஏற்படும் போது மட்டுமே சரத்து 19 உத்தரவாதம் அளிக்கும் ஆறு அடிப்படை சுதந்திரங்கள் தானாகவே இடைநிறுத்தப்படுகின்றன. ஆயுதமேந்திய கிளர்ச்சியின் போது சரத்து 358 தானாகச் செயல்படாது.",
        "Option A can have its enforcement suspended via Presidential Order under Article 359.", "சரத்து 359-ன் கீழ் குடியரசுத் தலைவர் ஆணை மூலம் விருப்பம் A-ன் அமலாக்கம் இடைநிறுத்தப்படலாம்.",
        "Option B can have its enforcement suspended via Presidential Order under Article 359.", "சரத்து 359-ன் கீழ் குடியரசுத் தலைவர் ஆணை மூலம் விருப்பம் B-ன் அமலாக்கம் இடைநிறுத்தப்படலாம்.",
        "Option C can have its enforcement suspended via Presidential Order under Article 359.", "சரத்து 359-ன் கீழ் குடியரசுத் தலைவர் ஆணை மூலம் விருப்பம் C-ன் அமலாக்கம் இடைநிறுத்தப்படலாம்.",
        "Option D cannot occur under Article 358 during armed rebellion (amended by 44th CAA 1978).", "விருப்பம் D ஆயுதமேந்திய கிளர்ச்சியின் போது சரத்து 358-ன் கீழ் நிகழ முடியாது (44-வது திருத்தம் 1978).",
        "Article 358 = ONLY War and External Aggression. NEVER operates during Armed Rebellion!",
        "சரத்து 358 = போர் மற்றும் வெளிநாட்டு ஆக்கிரமிப்பு மட்டுமே. ஆயுதமேந்திய கிளர்ச்சியின் போது ஒருபோதும் செயல்படாது!",
        "This critical distinction ensures democratic discourse and press freedom remain intact during internal security actions.",
        "இந்த முக்கிய வேறுபாடு உள்நாட்டுப் பாதுகாப்பின் போது ஜனநாயக விவாதங்களும் பத்திரிகை சுதந்திரமும் நீடிப்பதை உறுதி செய்கிறது."
    ))

    # 042 - Key A
    qs.append(make_ep_q(
        PREFIX, 42, DIFF, "Constitutional Procedure", "Effect of Dissolution of Rajya Sabha during Emergency",
        "Can the Rajya Sabha be dissolved during a National Emergency or President's Rule?",
        "தேசிய அவசரநிலை அல்லது குடியரசுத் தலைவர் ஆட்சியின் போது மாநிலங்களவையைக் கலைக்க முடியுமா?",
        "No, because Rajya Sabha is a permanent House and is not subject to dissolution under any circumstances", "முடியாது, ஏனெனில் மாநிலங்களவை ஒரு நிரந்தர அவை மற்றும் எந்தச் சூழ்நிலையிலும் அதைக் கலைக்க முடியாது",
        "Yes, the President can dissolve it under Article 356", "ஆம், சரத்து 356-ன் கீழ் குடியரசுத் தலைவர் அதைக் கலைக்கலாம்",
        "Yes, if the Lok Sabha passes a special resolution", "ஆம், மக்களவை சிறப்புத் தீர்மானம் நிறைவேற்றினால் கலைக்கலாம்",
        "Yes, during a financial emergency under Article 360", "ஆம், சரத்து 360-ன் கீழ் நிதி அவசரநிலையின் போது கலைக்கலாம்",
        "A",
        "Under Article 83(1), the Council of States (Rajya Sabha) is a permanent body and NOT subject to dissolution under any circumstances, including National Emergency, President's Rule, or Financial Emergency. This permanence ensures parliamentary continuity even when the Lok Sabha is dissolved.",
        "சரத்து 83(1)-ன் படி, மாநிலங்களவை என்பது ஒரு நிரந்தர அமைப்பாகும். தேசிய அவசரநிலை, குடியரசுத் தலைவர் ஆட்சி அல்லது நிதி அவசரநிலை உட்பட எந்தச் சூழ்நிலையிலும் அதைக் கலைக்க முடியாது. மக்களவை கலைக்கப்பட்டிருக்கும் போது கூட இது பாராளுமன்ற தொடர்ச்சியை உறுதி செய்கிறது.",
        "Option A is correct; Rajya Sabha is completely immune to dissolution.", "விருப்பம் A சரியானது; மாநிலங்களவை கலைப்பிலிருந்து முழுமையான பாதுகாப்புப் பெற்றது.",
        "Option B is factually and constitutionally wrong.", "விருப்பம் B உண்மைக்கும் அரசியலமைப்புக்கும் எதிரானது.",
        "Option C is impossible under the Constitution.", "விருப்பம் C அரசியலமைப்பின் கீழ் சாத்தியமற்றது.",
        "Option D is false.", "விருப்பம் D தவறானது.",
        "Federal Anchor: The Rajya Sabha's permanent nature is the constitutional anchor that keeps emergency approvals democratic when Lok Sabha is dissolved.",
        "கூட்டாட்சி நங்கூரம்: மக்களவை கலைக்கப்பட்டிருக்கும் போது அவசரநிலை ஒப்புதல்களை ஜனநாயகப்பூர்வமாக வைத்திருக்கும் அரசியலமைப்பு நங்கூரம் மாநிலங்களவையின் நிரந்தரத் தன்மையே ஆகும்.",
        "One-third of its members retire every second year, ensuring continuous institutional memory.",
        "அதன் உறுப்பினர்களில் மூன்றில் ஒரு பகுதியினர் இரண்டு ஆண்டுகளுக்கு ஒருமுறை ஓய்வு பெறுகின்றனர், இது தொடர்ச்சியான நிறுவன நினைவகத்தை உறுதி செய்கிறது."
    ))

    # 043 - Key B
    qs.append(make_ep_q(
        PREFIX, 43, DIFF, "Emergency Provisions - Evolution", "Shah Commission of Inquiry (1977)",
        "Which judicial commission was appointed by the Janata Party government in May 1977 to inquire into the excesses, malpractices, and abuses of authority committed during the 1975-1977 National Emergency?",
        "1975-1977 தேசிய அவசரநிலையின் போது இழைக்கப்பட்ட அத்துமீறல்கள், முறைகேடுகள் மற்றும் அதிகார துஷ்பிரயோகங்களை விசாரிக்க மே 1977-ல் ஜனதா கட்சி அரசாங்கத்தால் நியமிக்கப்பட்ட நீதி விசாரணைக் குழு எது?",
        "Sarkaria Commission", "சர்க்காரியா ஆணையம்",
        "Shah Commission", "ஷா ஆணையம்",
        "Kothari Commission", "கோத்தாரி ஆணையம்",
        "Venkatachaliah Commission", "வெங்கடாசலையா ஆணையம்",
        "B",
        "The Shah Commission of Inquiry, headed by former Chief Justice of India J.C. Shah, was appointed on 28 May 1977 to investigate illegalities, excesses, and abuses of authority during the 1975 internal emergency. Its findings directly inspired the safeguards enacted in the 44th Constitutional Amendment Act of 1978.",
        "1975 உள்நாட்டு அவசரநிலையின் போது நிகழ்ந்த சட்டவிரோத செயல்கள், அத்துமீறல்கள் மற்றும் அதிகார துஷ்பிரயோகங்களை விசாரிக்க முன்னாள் தலைமை நீதிபதி ஜே.சி. ஷா தலைமையில் 28 மே 1977 அன்று ஷா விசாரணைக் குழு அமைக்கப்பட்டது. இதன் கண்டுபிடிப்புகளே 1978-ன் 44-வது திருத்தச் சட்டத்தின் பாதுகாப்புகளுக்கு நேரடி அடிப்படையாக அமைந்தன.",
        "Option A (Sarkaria Commission) was appointed in 1983 on Centre-State relations.", "விருப்பம் A (சர்க்காரியா ஆணையம்) மத்திய-மாநில உறவுகள் குறித்து 1983-ல் அமைக்கப்பட்டது.",
        "Option B is the correct historic commission whose reports detailed the emergency abuses.", "விருப்பம் B அவசரநிலை அத்துமீறல்களை விரிவாக விளக்கிய சரியான வரலாற்று ஆணையமாகும்.",
        "Option C (Kothari Commission) dealt with education reforms (1964-66).", "விருப்பம் C (கோத்தாரி ஆணையம்) கல்வி சீர்திருத்தங்கள் தொடர்பானது (1964-66).",
        "Option D (Venkatachaliah Commission) reviewed the working of the Constitution in 2000-2002.", "விருப்பம் D (வெங்கடாசலையா ஆணையம்) 2000-2002-ல் அரசியலமைப்பு செயல்பாட்டை மறுஆய்வு செய்தது.",
        "Shah Commission (1977) -> Investigated 1975 Emergency Excesses -> Recommendations led directly to 44th CAA (1978).",
        "ஷா ஆணையம் (1977) -> 1975 அவசரநிலை அத்துமீறல்களை விசாரித்தது -> இதன் பரிந்துரைகளே 44-வது திருத்தத்திற்கு (1978) வழிவகுத்தன.",
        "The commission documented extensive preventive detentions, censorship of the press, and constitutional distortions.",
        "இந்த ஆணையம் விரிவான தடுப்புக் காவல்களையும், பத்திரிகை தணிக்கையையும், அரசியலமைப்பு சிதைவுகளையும் ஆவணப்படுத்தியது."
    ))

    # 044 - Key C
    qs.append(make_ep_q(
        PREFIX, 44, DIFF, "Constitutional Comparison", "Article 356 vs Article 365 Linkage",
        "How is Article 365 constitutionally linked to Article 356 in the context of President's Rule?",
        "குடியரசுத் தலைவர் ஆட்சியின் பின்னணியில் சரத்து 365 எவ்வாறு அரசியலமைப்பு ரீதியாக சரத்து 356 உடன் இணைக்கப்பட்டுள்ளது?",
        "Article 365 specifies the maximum duration of President's Rule as 3 years.", "சரத்து 365 குடியரசுத் தலைவர் ஆட்சியின் அதிகபட்ச காலத்தை 3 ஆண்டுகள் எனக் குறிப்பிடுகிறது.",
        "Article 365 requires the mandatory consent of the Chief Minister before Article 356 can be invoked.", "சரத்து 356-ஐப் பயன்படுத்துவதற்கு முன்பு முதலமைச்சரின் கட்டாய ஒப்புதலை சரத்து 365 கோருகிறது.",
        "Under Article 365, if a State fails to comply with any directions given by the Union, the President may hold that a situation has arisen where governance cannot be carried on in accordance with the Constitution (invoking Article 356)", "சரத்து 365-ன் கீழ், மத்திய அரசின் வழிகாட்டுதல்களை ஒரு மாநிலம் பின்பற்றத் தவறினால், அரசியலமைப்பு விதிகளின்படி ஆட்சி நடத்த முடியாத சூழ்நிலை ஏற்பட்டுவிட்டதாகக் கருதி குடியரசுத் தலைவர் ஆட்சி (சரத்து 356) அமல்படுத்தப்படலாம்",
        "Article 365 provides for financial emergency if state debts cross constitutional limits.", "மாநிலக் கடன்கள் அரசியலமைப்பு வரம்பைத் தாண்டினால் நிதி அவசரநிலையை சரத்து 365 வழங்குகிறது.",
        "C",
        "Article 365 explicitly provides that where any State has failed to comply with, or to give effect to, any directions given in the exercise of the executive power of the Union, it shall be lawful for the President to hold that a situation has arisen in which the government of the State cannot be carried on in accordance with the provisions of this Constitution, directly opening the gate for Article 356.",
        "சரத்து 365 வெளிப்படையாகக் கூறுகிறது: மத்திய அரசின் நிர்வாக அதிகாரத்தின் கீழ் வழங்கப்படும் வழிகாட்டுதல்களை ஒரு மாநிலம் பின்பற்றவோ செயல்படுத்தவோ தவறினால், அந்த மாநில அரசு அரசியலமைப்பு விதிகளின்படி நடைபெற முடியாத சூழ்நிலை ஏற்பட்டுவிட்டதாக குடியரசுத் தலைவர் கருதுவது சட்டப்பூர்வமானது. இது நேரடியாக சரத்து 356-க்கு வழிவகுக்கும்.",
        "Option A describes Article 356(4), not Article 365.", "விருப்பம் A சரத்து 356(4)-ஐக் குறிக்கிறது, சரத்து 365-ஐ அல்ல.",
        "Option B is nonexistent in constitutional law.", "விருப்பம் B அரசியலமைப்புச் சட்டத்தில் இல்லாத ஒன்று.",
        "Option C is the precise constitutional connection between Article 365 and Article 356.", "விருப்பம் C என்பது சரத்து 365 மற்றும் சரத்து 356 ஆகியவற்றுக்கு இடையேயான துல்லியமான அரசியலமைப்புத் தொடர்பாகும்.",
        "Option D relates to financial emergency under Article 360.", "விருப்பம் D சரத்து 360-ன் கீழ் நிதி அவசரநிலை தொடர்பானது.",
        "Article 365 = Non-compliance with Union Directions -> Deemed breakdown of constitutional machinery -> Article 356 invoked.",
        "சரத்து 365 = மத்திய வழிகாட்டுதல்களைப் பின்பற்றாமை -> அரசியலமைப்பு முறிவு ஏற்பட்டதாகக் கொள்ளல் -> சரத்து 356 அமல்.",
        "This makes central directions legally binding upon state governments under the threat of dissolution.",
        "இது கலைப்பு அச்சுறுத்தலின் கீழ் மத்திய வழிகாட்டுதல்களை மாநில அரசுகள் மீது சட்டப்பூர்வமாகக் கட்டுப்படுத்துகிறது."
    ))

    # 045 - Key D
    qs.append(make_ep_q(
        PREFIX, 45, DIFF, "Emergency Provisions - Terminology", "Internal Disturbance Replacement",
        "Why was the phrase 'internal disturbance' in Article 352 replaced with 'armed rebellion' by the 44th Constitutional Amendment Act 1978?",
        "1978-ன் 44-வது அரசியலமைப்பு திருத்தச் சட்டத்தின் மூலம் சரத்து 352-ல் இருந்த 'உள்நாட்டுக் குழப்பம்' என்ற சொல் ஏன் 'ஆயுதமேந்திய கிளர்ச்சி' என மாற்றப்பட்டது?",
        "Because the Supreme Court ruled that internal disturbance was unconstitutional in Kesavananda Bharati", "ஏனெனில் கேசவானந்த பாரதி வழக்கில் உள்நாட்டுக் குழப்பம் அரசியலமைப்பிற்கு எதிரானது என உச்ச நீதிமன்றம் தீர்ப்பளித்தது",
        "Because armed rebellion is a term borrowed from the US Constitution", "ஏனெனில் ஆயுதமேந்திய கிளர்ச்சி என்பது அமெரிக்க அரசியலமைப்பிலிருந்து பெறப்பட்ட சொல்",
        "Because internal disturbance was defined exclusively as economic inflation", "ஏனெனில் உள்நாட்டுக் குழப்பம் என்பது பொருளாதார பணவீக்கமாக மட்டுமே வரையறுக்கப்பட்டது",
        "Because 'internal disturbance' was too vague and had been misused in June 1975 to declare emergency on political grounds without armed violence", "ஏனெனில் 'உள்நாட்டுக் குழப்பம்' என்பது மிகவும் தெளிவற்றதாக இருந்தது மற்றும் ஆயுத வன்முறையின்றி அரசியல் காரணங்களுக்காக அவசரநிலையை அறிவிக்க ஜூன் 1975-ல் தவறாகப் பயன்படுத்தப்பட்டது",
        "D",
        "The phrase 'internal disturbance' was extremely vague and wide in scope. It was exploited on 25 June 1975 to proclaim National Emergency against peaceful political agitation and civil disobedience. The 44th Amendment Act 1978 substituted it with 'armed rebellion' to ensure that only an armed uprising posing a grave threat to national security could justify declaring an internal emergency.",
        "'உள்நாட்டுக் குழப்பம்' என்ற சொல் மிகவும் தெளிவற்றதாகவும் பரந்த நோக்கம் கொண்டதாகவும் இருந்தது. அமைதியான அரசியல் போராட்டங்கள் மற்றும் கீழ்ப்படியாமைக்கு எதிராக 25 ஜூன் 1975 அன்று தேசிய அவசரநிலையைப் பிரகடனப்படுத்த இது தவறாகப் பயன்படுத்தப்பட்டது. தேசிய பாதுகாப்பிற்கு கடுமையான அச்சுறுத்தலை ஏற்படுத்தும் ஆயுதமேந்திய கிளர்ச்சி மட்டுமே உள்நாட்டு அவசரநிலையை நியாயப்படுத்த முடியும் என்பதை உறுதிப்படுத்த 44-வது திருத்தம் 'ஆயுதமேந்திய கிளர்ச்சி' என்ற சொல்லை மாற்றாக வைத்தது.",
        "Option A is false.", "விருப்பம் A தவறானது.",
        "Option B is incorrect.", "விருப்பம் B தவறானது.",
        "Option C is baseless.", "விருப்பம் C அடிப்படையற்றது.",
        "Option D provides the comprehensive historical and constitutional rationale for the amendment.", "விருப்பம் D இந்தத் திருத்தத்திற்கான விரிவான வரலாற்று மற்றும் அரசியலமைப்பு நியாயத்தை வழங்குகிறது.",
        "Vagueness to Precision: 'Internal Disturbance' (broad, subjective) -> 'Armed Rebellion' (specific, objective threat).",
        "தெளிவற்ற நிலையிலிருந்து துல்லியத்திற்கு: 'உள்நாட்டுக் குழப்பம்' (தெளிவற்றது) -> 'ஆயுதமேந்திய கிளர்ச்சி' (குறிப்பிட்ட அச்சுறுத்தல்).",
        "Internal political agitations, strikes, or civil protests can no longer form the legal ground for Article 352.",
        "உள்நாட்டு அரசியல் போராட்டங்கள், வேலைநிறுத்தங்கள் அல்லது மக்கள் எதிர்ப்புகள் இனி சரத்து 352-க்கான சட்டப்பூர்வ காரணமாக அமைய முடியாது."
    ))

    # 046 - Key A
    qs.append(make_ep_q(
        PREFIX, 46, DIFF, "Constitutional Comparison", "Emergency Types and Proclamation Counts",
        "As of today, how many times have the three types of Emergencies (National Emergency, President's Rule, and Financial Emergency) been proclaimed in India?",
        "இன்று வரை இந்தியாவில் மூன்று வகையான அவசரநிலைகள் (தேசிய அவசரநிலை, குடியரசுத் தலைவர் ஆட்சி மற்றும் நிதி அவசரநிலை) முறையே எத்தனை முறை பிரகடனப்படுத்தப்பட்டுள்ளன?",
        "National Emergency: 3 times; President's Rule: Over 130 times; Financial Emergency: 0 times", "தேசிய அவசரநிலை: 3 முறை; குடியரசுத் தலைவர் ஆட்சி: 130-க்கும் மேற்பட்ட முறை; நிதி அவசரநிலை: 0 முறை",
        "National Emergency: 2 times; President's Rule: 50 times; Financial Emergency: 1 time", "தேசிய அவசரநிலை: 2 முறை; குடியரசுத் தலைவர் ஆட்சி: 50 முறை; நிதி அவசரநிலை: 1 முறை",
        "National Emergency: 4 times; President's Rule: 100 times; Financial Emergency: 0 times", "தேசிய அவசரநிலை: 4 முறை; குடியரசுத் தலைவர் ஆட்சி: 100 முறை; நிதி அவசரநிலை: 0 முறை",
        "National Emergency: 3 times; President's Rule: 75 times; Financial Emergency: 2 times", "தேசிய அவசரநிலை: 3 முறை; குடியரசுத் தலைவர் ஆட்சி: 75 முறை; நிதி அவசரநிலை: 2 முறை",
        "A",
        "In Indian constitutional history: (1) National Emergency (Article 352) has been proclaimed 3 times (1962, 1971, 1975); (2) President's Rule (Article 356) has been invoked over 130 times across various states; and (3) Financial Emergency (Article 360) has NEVER been declared (0 times).",
        "இந்திய அரசியலமைப்பு வரலாற்றில்: (1) தேசிய அவசரநிலை (சரத்து 352) 3 முறை பிரகடனப்படுத்தப்பட்டுள்ளது (1962, 1971, 1975); (2) குடியரசுத் தலைவர் ஆட்சி (சரத்து 356) பல்வேறு மாநிலங்களில் 130-க்கும் மேற்பட்ட முறை பயன்படுத்தப்பட்டுள்ளது; (3) நிதி அவசரநிலை (சரத்து 360) இதுவரை ஒருமுறை கூட அறிவிக்கப்படவில்லை (0 முறை).",
        "Option A is the accurate statistical and constitutional summary.", "விருப்பம் A துல்லியமான புள்ளிவிவர மற்றும் அரசியலமைப்பு சுருக்கமாகும்.",
        "Option B falsely claims Financial Emergency was declared once.", "விருப்பம் B நிதி அவசரநிலை ஒருமுறை அறிவிக்கப்பட்டதாக தவறாகக் கூறுகிறது.",
        "Option C states 4 times for National Emergency, which is wrong.", "விருப்பம் C தேசிய அவசரநிலை 4 முறை என்று தவறாகக் கூறுகிறது.",
        "Option D falsely claims Financial Emergency was declared twice.", "விருப்பம் D நிதி அவசரநிலை இருமுறை அறிவிக்கப்பட்டதாக தவறாகக் கூறுகிறது.",
        "Vital Fact: Financial Emergency (Art 360) has been declared ZERO times in Indian history.",
        "முக்கிய உண்மை: இந்திய வரலாற்றில் நிதி அவசரநிலை (சரத்து 360) பூஜ்ஜியம் (ஒருமுறை கூட இல்லை) முறை அறிவிக்கப்பட்டுள்ளது.",
        "President's Rule remains the most frequently invoked and litigated emergency power in the Constitution.",
        "குடியரசுத் தலைவர் ஆட்சியே அரசியலமைப்பில் மிகவும் அடிக்கடி பயன்படுத்தப்பட்ட மற்றும் வழக்குத் தொடரப்பட்ட அதிகாரமாக உள்ளது."
    ))

    # 047 - Key B
    qs.append(make_ep_q(
        PREFIX, 47, DIFF, "Constitutional Comparison", "Article 352 vs 356 Judicial Review",
        "Following the Bommai case (1994), what is the scope of judicial review when a court evaluates a proclamation under Article 356?",
        "பொம்மை வழக்கை (1994) தொடர்ந்து, சரத்து 356-ன் கீழான ஒரு பிரகடனத்தை நீதிமன்றம் ஆய்வு செய்யும் போது அதன் நீதித்துறை மறுஆய்வின் எல்லை என்னவாக இருக்கும்?",
        "The court can substitute its own judgment for the President's satisfaction and assess sufficiency of material.", "நீதிமன்றம் குடியரசுத் தலைவரின் திருப்திக்கு மாற்றாக தனது சொந்தத் தீர்ப்பை முன்வைக்கலாம் மற்றும் ஆதாரங்களின் போதுமான தன்மையை ஆராயலாம்.",
        "The court examines whether material existed, whether it was relevant, and whether the action was malafide or based on wholly extraneous grounds, but does not assess sufficiency of material.", "ஆதாரம் இருந்ததா, அது பொருத்தமானதா, மற்றும் நடவடிக்கை உள்நோக்கம் கொண்டதா அல்லது முற்றிலும் தொடர்பற்ற காரணங்களை அடிப்படையாகக் கொண்டதா என்பதை நீதிமன்றம் ஆராயும்; ஆனால் ஆதாரங்களின் போதுமான தன்மையை மதிப்பிடாது.",
        "Proclamations under Article 356 are completely immune from judicial review under all conditions.", "சரத்து 356-ன் கீழான பிரகடனங்கள் அனைத்து சூழ்நிலைகளிலும் நீதித்துறை மறுஆய்விலிருந்து முற்றிலும் விலக்கு பெற்றவை.",
        "Judicial review can only take place after 3 years when President's Rule lapses.", "குடியரசுத் தலைவர் ஆட்சி முடிவடையும் 3 ஆண்டுகளுக்குப் பிறகு மட்டுமே நீதித்துறை மறுஆய்வு செய்ய முடியும்.",
        "B",
        "The Supreme Court in S.R. Bommai (1994) held that while the subjective satisfaction of the President cannot be questioned on its merits or sufficiency, the court CAN examine whether any relevant material existed at all, whether the material was relevant to the proclamation, and whether the proclamation was malafide or perverse. Burden lies on the Union to show relevant material existed.",
        "எஸ்.ஆர். பொம்மை (1994) வழக்கில், குடியரசுத் தலைவரின் அகநிலை திருப்தியின் தகுதி அல்லது போதுமான தன்மையை கேள்வி கேட்க முடியாது என்றாலும், ஏதேனும் பொருத்தமான ஆதாரம் இருந்ததா, அந்த ஆதாரம் பிரகடனத்திற்கு தொடர்புடையதா, மற்றும் பிரகடனம் உள்நோக்கம் கொண்டதா என்பதை நீதிமன்றம் ஆராய முடியும் என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது. பொருத்தமான ஆதாரம் இருந்ததை நிரூபிக்கும் சுமை மத்திய அரசிடமே உள்ளது.",
        "Option A is incorrect; courts do not substitute their judgment nor evaluate sufficiency.", "விருப்பம் A தவறானது; நீதிமன்றங்கள் தங்கள் சொந்தத் தீர்ப்பை மாற்றாக வைப்பதில்லை அல்லது போதுமான தன்மையை மதிப்பிடுவதில்லை.",
        "Option B precisely articulates the judicial standard established in Bommai.", "விருப்பம் B பொம்மை வழக்கில் நிறுவப்பட்ட நீதித்துறை தரத்தை துல்லியமாக விளக்குகிறது.",
        "Option C is false; Article 356 is subject to judicial review.", "விருப்பம் C தவறு; சரத்து 356 நீதித்துறை மறுஆய்வுக்கு உட்பட்டது.",
        "Option D is fictitious.", "விருப்பம் D கற்பனையானது.",
        "Bommai Review Formula: Existence and Relevance of material + Absence of Malafide = Valid. Sufficiency is NOT examined.",
        "பொம்மை மறுஆய்வு சூத்திரம்: ஆதாரத்தின் இருப்பு மற்றும் பொருத்தம் + உள்நோக்கம் இன்மை = செல்லுபடியாகும். போதுமான தன்மை ஆராயப்படாது.",
        "If a proclamation is found malafide, the court has the power to restore the dismissed ministry and dissolved assembly.",
        "பிரகடனம் தவறான உள்நோக்கம் கொண்டது எனக் கண்டறியப்பட்டால், கலைக்கப்பட்ட அரசையும் சட்டமன்றத்தையும் மீட்டெடுக்கும் அதிகாரம் நீதிமன்றத்திற்கு உண்டு."
    ))

    # 048 - Key C
    qs.append(make_ep_q(
        PREFIX, 48, DIFF, "Constitutional Comparison", "National Emergency - Rajya Sabha Powers",
        "If a proclamation of National Emergency is issued while Lok Sabha is dissolved, what happens if the Rajya Sabha disapproves it within one month?",
        "மக்களவை கலைக்கப்பட்டிருக்கும் போது தேசிய அவசரநிலைப் பிரகடனம் வெளியிடப்பட்டு, ஒரு மாதத்திற்குள் மாநிலங்களவை அதை நிராகரித்தால் என்னவாகும்?",
        "The proclamation survives until the new Lok Sabha meets and decides.", "புதிய மக்களவை கூடி முடிவெடுக்கும் வரை அந்தப் பிரகடனம் நீடிக்கும்.",
        "The President can refer the dispute to a joint sitting of Parliament.", "குடியரசுத் தலைவர் இந்த முரண்பாட்டை பாராளுமன்றத்தின் கூட்டுக் கூட்டத்திற்குப் பரிந்துரைக்கலாம்.",
        "The proclamation immediately ceases to operate at the expiration of one month.", "ஒரு மாதம் முடிந்தவுடன் அந்தப் பிரகடனம் உடனடியாக காலாவதியாகிவிடும்.",
        "The proclamation is automatically validated by the Supreme Court.", "அந்தப் பிரகடனம் உச்ச நீதிமன்றத்தால் தானாகவே அங்கீகரிக்கப்படும்.",
        "C",
        "Under Article 352(4), for a proclamation to survive until 30 days from the first sitting of the reconstituted Lok Sabha, it is a MANDATORY prerequisite that the Rajya Sabha must have approved it within one month. If the Rajya Sabha disapproves or fails to pass it within one month, the proclamation ceases to operate immediately at the expiration of that one month!",
        "சரத்து 352(4)-ன் கீழ், புதிய மக்களவை கூடிய 30 நாட்கள் வரை பிரகடனம் நீடிக்க வேண்டுமானால், மாநிலங்களவை ஒரு மாதத்திற்குள் அதற்கு ஒப்புதல் அளித்திருக்க வேண்டும் என்பது கட்டாய முன்நிபந்தனையாகும். மாநிலங்களவை அதை நிராகரித்தாலோ அல்லது ஒப்புதல் அளிக்கத் தவறினாலோ, ஒரு மாதம் முடிந்தவுடன் பிரகடனம் உடனடியாக காலாவதியாகிவிடும்!",
        "Option A is false because survival depends strictly on prior Rajya Sabha approval.", "விருப்பம் A தவறு, ஏனெனில் பிரகடனம் நீடிப்பது மாநிலங்களவையின் முன் ஒப்புதலைப் பொறுத்தது.",
        "Option B is false; there is no joint sitting provision for emergency proclamations under Article 352.", "விருப்பம் B தவறு; சரத்து 352-ன் கீழ் கூட்டுக் கூட்டத்திற்கு இடமில்லை.",
        "Option C is the direct constitutional outcome: it dies immediately upon the 1-month mark.", "விருப்பம் C நேரடி அரசியலமைப்பு விளைவு: 1 மாத முடிவில் அது உடனடியாக காலாவதியாகிவிடும்.",
        "Option D has no constitutional sense.", "விருப்பம் D அரசியலமைப்பு ரீதியாக சாத்தியமற்றது.",
        "Rajya Sabha Check: When Lok Sabha is dissolved, Rajya Sabha holds the sole key. If it rejects, the emergency proclamation terminates at 1 month.",
        "மாநிலங்களவையின் கட்டுப்பாடு: மக்களவை கலைக்கப்பட்டிருக்கும் போது மாநிலங்களவையே முழுக் கட்டுப்பாட்டைக் கொண்டுள்ளது. அது நிராகரித்தால், அவசரநிலைப் பிரகடனம் 1 மாதத்தில் முடிவுக்கு வரும்.",
        "This proves that the Upper House is not a mere rubber stamp during constitutional emergencies.",
        "அரசியலமைப்பு அவசரநிலைகளின் போது மேலவை ஒரு முத்திரை குத்தும் அமைப்பு மட்டுமல்ல என்பதை இது நிரூபிக்கிறது."
    ))

    # 049 - Key C
    qs.append(make_ep_q(
        PREFIX, 49, DIFF, "Constitutional Comparison", "President's Rule Maximum Duration Exceptions",
        "Under Article 356, what was the unique exception enacted through constitutional amendments for extending President's Rule up to five years in a specific state?",
        "சரத்து 356-ன் கீழ், ஒரு குறிப்பிட்ட மாநிலத்தில் குடியரசுத் தலைவர் ஆட்சியை ஐந்து ஆண்டுகள் வரை நீட்டிக்க அரசியலமைப்பு திருத்தங்கள் மூலம் கொண்டுவரப்பட்ட தனித்துவமான விதிவிலக்கு எது?",
        "Kerala in 1959", "கேரளா - 1959",
        "Jammu and Kashmir in 1990", "ஜம்மு மற்றும் காஷ்மீர் - 1990",
        "Punjab between 1987 and 1992", "பஞ்சாப் - 1987 மற்றும் 1992 இடையே",
        "Assam in 1983", "அசாம் - 1983",
        "C",
        "Due to rampant militancy in Punjab, President's Rule imposed in May 1987 could not be concluded within the normal 3-year maximum limit. Parliament passed multiple constitutional amendments (including the 59th, 64th, 67th, and 68th Amendment Acts) specifically amending Article 356(5) to permit President's Rule in Punjab for a total period of up to 5 years, ending with elections in 1992.",
        "பஞ்சாபில் தீவிரவாதம் தலைவிரித்தாடியதால், மே 1987-ல் அமல்படுத்தப்பட்ட குடியரசுத் தலைவர் ஆட்சியை சாதாரண 3 ஆண்டு வரம்பிற்குள் முடிக்க முடியவில்லை. பஞ்சாபில் குடியரசுத் தலைவர் ஆட்சியை மொத்தம் 5 ஆண்டுகள் வரை நீட்டிக்க ஏதுவாக பாராளுமன்றம் சரத்து 356(5)-ல் பல அரசியலமைப்பு திருத்தங்களை (59, 64, 67 மற்றும் 68-வது திருத்தச் சட்டங்கள்) இயற்றியது; இது 1992 தேர்தலுடன் முடிவடைந்தது.",
        "Option A: Kerala's 1959 emergency lasted only a few months.", "விருப்பம் A: கேரளாவின் 1959 அவசரநிலை சில மாதங்கள் மட்டுமே நீடித்தது.",
        "Option B: J&K had special status under Art 370 and Governor's Rule under its state constitution.", "விருப்பம் B: ஜம்மு காஷ்மீருக்கு சரத்து 370-ன் கீழ் சிறப்பு அந்தஸ்தும் அதன் சொந்த அரசியலமைப்பும் இருந்தது.",
        "Option C is the historic Punjab exception requiring repeated constitutional amendments.", "விருப்பம் C என்பது தொடர் அரசியலமைப்பு திருத்தங்கள் தேவைப்பட்ட வரலாற்றுச் சிறப்புமிக்க பஞ்சாப் விதிவிலக்காகும்.",
        "Option D is incorrect.", "விருப்பம் D தவறானது.",
        "Punjab Exception: Article 356 was repeatedly amended (up to 68th CAA) to extend President's Rule in Punjab up to 5 years (1987-1992).",
        "பஞ்சாப் விதிவிலக்கு: பஞ்சாபில் குடியரசுத் தலைவர் ஆட்சியை 5 ஆண்டுகள் வரை நீட்டிக்க சரத்து 356 பலமுறை திருத்தப்பட்டது (1987-1992).",
        "This required constitutional amendments because the 3-year barrier under Article 356(4) could not otherwise be breached.",
        "சரத்து 356(4)-ன் கீழான 3 ஆண்டு வரம்பை வேறு வழியில் கடக்க முடியாது என்பதால் இதற்கு அரசியலமைப்பு திருத்தங்கள் தேவைப்பட்டன."
    ))

    # 050 - Key D
    qs.append(make_ep_q(
        PREFIX, 50, DIFF, "Constitutional Terminology", "Proclamation of Emergency Definition",
        "According to Article 366(18) of the Constitution of India, how is a 'Proclamation of Emergency' formally defined?",
        "இந்திய அரசியலமைப்பின் சரத்து 366(18)-ன் படி, 'அவசரநிலைப் பிரகடனம்' என்பது முறையாக எவ்வாறு வரையறுக்கப்படுகிறது?",
        "A proclamation issued under Article 356 or Article 360", "சரத்து 356 அல்லது சரத்து 360-ன் கீழ் வெளியிடப்பட்ட ஒரு பிரகடனம்",
        "Any executive order suspending fundamental rights", "அடிப்படை உரிமைகளை இடைநிறுத்தும் எந்தவொரு நிர்வாக ஆணை",
        "A proclamation declaring martial law under Article 34", "சரத்து 34-ன் கீழ் இராணுவச் சட்டத்தை அறிவிக்கும் ஒரு பிரகடனம்",
        "A proclamation issued under clause (1) of Article 352", "சரத்து 352-ன் பிரிவு (1)-ன் கீழ் வெளியிடப்பட்ட ஒரு பிரகடனம்",
        "D",
        "Article 366(18) of the Indian Constitution defines: ''Proclamation of Emergency' means a Proclamation issued under clause (1) of Article 352.' In constitutional terminology, the phrase 'Proclamation of Emergency' refers strictly and exclusively to National Emergency under Article 352, not to Articles 356 or 360.",
        "இந்திய அரசியலமைப்பின் சரத்து 366(18) வரையறுக்கிறது: ''அவசரநிலைப் பிரகடனம்' என்பது சரத்து 352-ன் பிரிவு (1)-ன் கீழ் வெளியிடப்பட்ட ஒரு பிரகடனத்தைக் குறிக்கும்.' அரசியலமைப்பு சொற்பயன்பாட்டில், 'அவசரநிலைப் பிரகடனம்' என்ற சொல் சரத்து 352-ன் கீழான தேசிய அவசரநிலையை மட்டுமே பிரத்யேகமாகக் குறிக்கிறது, சரத்து 356 அல்லது 360-ஐ அல்ல.",
        "Option A is incorrect; neither Art 356 nor 360 is termed 'Proclamation of Emergency' in Article 366(18).", "விருப்பம் A தவறானது; சரத்து 356 அல்லது 360 சரத்து 366(18)-ன் கீழ் 'அவசரநிலைப் பிரகடனம்' என அழைக்கப்படுவதில்லை.",
        "Option B is an informal description.", "விருப்பம் B ஒரு முறைசாரா விளக்கம்.",
        "Option C relates to martial law.", "விருப்பம் C இராணுவச் சட்டம் தொடர்பானது.",
        "Option D is the exact definition in Article 366(18).", "விருப்பம் D சரத்து 366(18)-ல் உள்ள துல்லியமான வரையறையாகும்.",
        "Constitutional Precision: In Article 366(18), 'Proclamation of Emergency' applies ONLY to Article 352.",
        "அரசியலமைப்பு துல்லியம்: சரத்து 366(18)-ல், 'அவசரநிலைப் பிரகடனம்' என்பது சரத்து 352-க்கு மட்டுமே பொருந்தும்.",
        "Article 356 is technically termed a 'Proclamation on failure of constitutional machinery in States'.",
        "சரத்து 356 தொழில்நுட்ப ரீதியாக 'மாநிலங்களில் அரசியலமைப்பு இயந்திரம் முறிவடையும் போது வெளியிடப்படும் பிரகடனம்' என அழைக்கப்படுகிறது."
    ))

    return qs

def build_and_validate_medium():
    qs = get_medium_questions() + get_medium_questions_part2()
    print(f"[MEDIUM] Total questions generated: {len(qs)}")
    assert len(qs) == 50, f"Expected 50 questions, got {len(qs)}"

    # Check key balance
    dist = dict(Counter([q["correct_answer"] for q in qs]))
    print(f"[MEDIUM] Key Distribution: {dist}")
    assert dist == {"A": 12, "B": 13, "C": 13, "D": 12}, f"Distribution mismatch: {dist}"

    # Check uniqueness
    stems = [q["question_en"].strip().lower() for q in qs]
    assert len(stems) == len(set(stems)), "Duplicate stems found in Medium set!"
    print("[MEDIUM] Stems are 100% unique.")

    out_file = "data/questions/polity/emergency_provisions_medium.json"
    os.makedirs(os.path.dirname(out_file), exist_ok=True)
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2, ensure_ascii=False)
    print(f"[MEDIUM] Saved to {out_file}")

    rep = ContentValidator.validate_file(out_file, expected_count=50, expected_prefix=PREFIX)
    print(f"[MEDIUM] Validator Status: {'PASS' if rep.is_valid else 'FAIL'} | Audited: {rep.total_audited}")
    if rep.issues:
        for iss in rep.issues:
            print(f"  [{iss.severity}] {iss.question_id}: {iss.message}")
        assert False, "Validation failed!"
    print("[MEDIUM] Validation PASSED with 0 issues!")

if __name__ == "__main__":
    build_and_validate_medium()
