# -*- coding: utf-8 -*-
"""
Supreme Court Grand Test Block 4 (Questions 76 to 100)
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

from gt_sc_block1 import mk_q

def get_block4():
    b4 = []

    # Q76
    b4.append(mk_q(76, "Medium", "Direct",
        "Under Article 145(3) of the Constitution, what is the minimum number of Supreme Court judges required to sit for deciding any case involving a substantial question of law as to the interpretation of the Constitution?",
        "சரத்து 145(3)-ன் படி, அரசியலமைப்பு விளக்கமளித்தல் தொடர்பான முக்கிய சட்டக் கேள்வி அடங்கிய வழக்கை விசாரிக்கக் குறைந்தபட்சம் எத்தனை உச்ச நீதிமன்ற நீதிபதிகள் கொண்ட அமர்வு அமைய வேண்டும்?",
        {"A": "3 Judges", "B": "5 Judges", "C": "7 Judges", "D": "9 Judges"},
        {"A": "3 நீதிபதிகள்", "B": "5 நீதிபதிகள்", "C": "7 நீதிபதிகள்", "D": "9 நீதிபதிகள்"},
        "B",
        "Article 145(3) mandates that the minimum number of judges to sit for deciding any case involving a substantial question of law as to the interpretation of the Constitution shall be FIVE (Constitution Bench).",
        "சரத்து 145(3)-ன் படி அரசியலமைப்பு விளக்கமளிக்கும் வழக்குகளை விசாரிக்க அமைய வேண்டிய குறைந்தபட்ச நீதிபதிகளின் எண்ணிக்கை ஐந்து (5) ஆகும்.",
        "Such a 5+ judge bench is officially designated as a Constitution Bench.",
        "5 அல்லது அதற்கு மேற்பட்ட நீதிபதிகள் அமர்வு அரசியலமைப்பு அமர்வு எனப்படும்.",
        "Also required for hearing Article 143 Advisory References.",
        "சரத்து 143 ஆலோசனை வழக்குகளுக்கும் இது பொருந்தும்.",
        "Decisions are by majority of judges present.",
        "வருகை தந்த நீதிபதிகளின் பெரும்பான்மையால் தீர்ப்பு வழங்கப்படும்."))

    # Q77
    b4.append(mk_q(77, "Hard", "Statement",
        "Consider the following statements regarding the independence of the Supreme Court under Article 121 and Article 211:\n1. No discussion shall take place in Parliament or State Legislature with respect to the conduct of any SC or HC Judge in the discharge of his duties.\n2. The only exception when conduct of a judge can be discussed in Parliament is upon a motion for presenting an address to the President for removal of the judge.\n3. State Legislatures can NEVER discuss the conduct of a Supreme Court or High Court judge under any circumstances.\nWhich of the statements given above are correct?",
        "சரத்து 121 மற்றும் 211-ன் கீழ் உச்ச நீதிமன்றத்தின் சுதந்திரம் பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. நாடாளுமன்றத்திலோ அல்லது மாநில சட்டமன்றத்திலோ உச்ச நீதிமன்ற அல்லது உயர் நீதிமன்ற நீதிபதியின் கடமை சார்ந்த நடத்தை குறித்து எந்த விவாதமும் நடைபெறக் கூடாது.\n2. நீதிபதி மீது நீக்கத் தீர்மானம் கொண்டுவரப்பட்டு விவாதிக்கப்படும்போது மட்டுமே நாடாளுமன்றத்தில் நீதிபதியின் நடத்தை பற்றி விவாதிக்க ஒரே விதிவிலக்கு உண்டு.\n3. மாநில சட்டமன்றங்கள் எந்தச் சூழ்நிலையிலும் உச்ச நீதிமன்ற அல்லது உயர் நீதிமன்ற நீதிபதியின் நடத்தை பற்றி விவாதிக்க முடியாது.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
        {"A": "1, 2 and 3", "B": "1 and 2 only", "C": "2 and 3 only", "D": "1 and 3 only"},
        {"A": "1, 2 மற்றும் 3", "B": "1 மற்றும் 2 மட்டும்", "C": "2 மற்றும் 3 மட்டும்", "D": "1 மற்றும் 3 மட்டும்"},
        "A",
        "All three statements are correct. Article 121 bars discussion in Parliament (except on removal motion). Article 211 bars discussion in State Legislatures completely without any exception (State Assemblies cannot discuss removal motions).",
        "மூன்று கூற்றுகளும் சரியானவை. சரத்து 121 நாடாளுமன்றத்தில் விவாதத்தைத் தடுக்கிறது (நீக்கத் தீர்மானம் தவிர). சரத்து 211 மாநில சட்டமன்றங்களில் எந்த விதிவிலக்கும் இன்றி முழுமையாக விவாதத்தைத் தடுக்கிறது (மாநில அவைகளில் நீக்கத் தீர்மானம் வர முடியாது).",
        "Notice the difference: Parliament has 1 exception (removal motion under Art 121). State Assembly has ZERO exceptions (Art 211).",
        "நாடாளுமன்றத்திற்கு 1 விதிவிலக்கு உண்டு (நீக்கத் தீர்மானம்); மாநில சட்டமன்றத்திற்கு எந்த விதிவிலக்கும் இல்லை.",
        "Protects judges from political harassment by politicians.",
        "அரசியல்வாதிகளின் அச்சுறுத்தலிலிருந்து நீதிபதிகளைப் பாதுகாக்கிறது.",
        "Crucial safeguard for Judicial Independence.",
        "நீதித்துறை சுதந்திரத்தின் முக்கிய கவசம்."))

    # Q78
    b4.append(mk_q(78, "Medium", "Direct",
        "Under Article 125(2) of the Constitution, can the salaries, allowances, and rights in respect of leave of absence or pension of a Supreme Court Judge be varied to his disadvantage after his appointment?",
        "சரத்து 125(2)-ன் படி, உச்ச நீதிமன்ற நீதிபதி நியமிக்கப்பட்ட பிறகு அவருடைய சம்பளம், படிகள், விடுப்பு உரிமைகள் அல்லது ஓய்வூதியம் ஆகியவற்றைக் குறைக்கும் வகையில் மாற்றியமைக்க முடியுமா?",
        {"A": "No, they cannot be varied to his disadvantage after appointment under any circumstances EXCEPT during a Financial Emergency under Article 360", "B": "Yes, Parliament can reduce judge salaries at any time by simple majority", "C": "Yes, if the Law Minister issues an order", "D": "Yes, during National Emergency under Article 352"},
        {"A": "இல்லை, சரத்து 360 நிதி அவசரநிலையின் போது தவிர வேறு எந்தச் சூழ்நிலையிலும் நியமனத்திற்குப் பின் அவற்றைக் குறைக்க முடியாது", "B": "ஆம், நாடாளுமன்றம் சாதாரண பெரும்பான்மையால் எந்நேரமும் குறைக்கலாம்", "C": "ஆம், சட்ட அமைச்சர் உத்தரவு பிறப்பித்தால் குறைக்கலாம்", "D": "ஆம், சரத்து 352 தேசிய அவசரநிலையின் போது குறைக்கலாம்"},
        "A",
        "Proviso to Article 125(2) provides that neither the allowances of a judge nor his rights in respect of leave of absence or pension shall be VARIED TO HIS DISADVANTAGE after his appointment. The ONLY exception is during a Financial Emergency declared by President under Article 360(4)(b).",
        "சரத்து 125(2)-ன் படி நியமனத்திற்குப் பிறகு நீதிபதியின் சம்பளம் மற்றும் படிகளைக் குறைக்க முடியாது. இதற்கு ஒரே விதிவிலக்கு சரத்து 360 நிதி அவசரநிலை காலம் மட்டுமே ஆகும்.",
        "Financial Emergency (Art 360) is the ONLY exception where salaries of SC and HC judges can be reduced.",
        "நிதி அவசரநிலை (சரத்து 360) மட்டுமே நீதிപதிகளின் சம்பளத்தைக் குறைக்கக்கூடிய ஒரே விதிவிலக்காகும்.",
        "National Emergency (Art 352) does NOT allow reduction of judge salaries.",
        "தேசிய அவசரநிலை (சரத்து 352) நீதிபதிகள் சம்பளத்தைக் குறைக்க அனுமதிக்காது.",
        "Ensures financial independence of judges.",
        "நீதிபதிகளின் நிதி சுதந்திரத்தை உறுதி செய்கிறது."))

    # Q79
    b4.append(mk_q(79, "Hard", "Chronology",
        "Arrange the following Constitutional Amendments expanding the strength of Supreme Court Judges in chronological order of their enactment by Parliament:\n1. Supreme Court (Number of Judges) Amendment Act, 1977 (Increased strength from 14 to 18)\n2. Supreme Court (Number of Judges) Amendment Act, 1986 (Increased strength from 18 to 26)\n3. Supreme Court (Number of Judges) Amendment Act, 2009 (Increased strength from 26 to 31)\n4. Supreme Court (Number of Judges) Amendment Act, 2019 (Increased strength from 31 to 34)",
        "உச்ச நீதிமன்ற நீதிபதிகளின் எண்ணிக்கையை உயர்த்திய பின்வரும் நாடாளுமன்றத் திருத்தச் சட்டங்களை இயற்றப்பட்ட காலவரிசையில் அமைக்கவும்:\n1. 1977 சட்டம் (நீதிபதிகள் எண்ணிக்கை 14 லிருந்து 18 ஆக உயர்வு)\n2. 1986 சட்டம் (நீதிபதிகள் எண்ணிக்கை 18 லிருந்து 26 ஆக உயர்வு)\n3. 2009 சட்டம் (நீதிபதிகள் எண்ணிக்கை 26 லிருந்து 31 ஆக உயர்வு)\n4. 2019 சட்டம் (நீதிபதிகள் எண்ணிக்கை 31 லிருந்து 34 ஆக உயர்வு)",
        {"A": "1 -> 2 -> 3 -> 4", "B": "2 -> 1 -> 3 -> 4", "C": "1 -> 3 -> 2 -> 4", "D": "4 -> 3 -> 2 -> 1"},
        {"A": "1 -> 2 -> 3 -> 4", "B": "2 -> 1 -> 3 -> 4", "C": "1 -> 3 -> 2 -> 4", "D": "4 -> 3 -> 2 -> 1"},
        "A",
        "Chronological Expansion of SC Judge Strength (excluding CJI + including CJI total):\n1950: 8 (1 CJI + 7 Judges)\n1956: 11 (1 CJI + 10 Judges)\n1960: 14 (1 CJI + 13 Judges)\n1977: 18 (1 CJI + 17 Judges)\n1986: 26 (1 CJI + 25 Judges)\n2009: 31 (1 CJI + 30 Judges)\n2019: 34 (1 CJI + 33 Judges)\nHence, 1 -> 2 -> 3 -> 4.",
        "உச்ச நீதிமன்ற நீதிபதிகள் எண்ணிக்கை உயர்வு வரிசை:\n1950: 8 (1 CJI + 7)\n1956: 11 (1 CJI + 10)\n1960: 14 (1 CJI + 13)\n1977: 18 (1 CJI + 17)\n1986: 26 (1 CJI + 25)\n2009: 31 (1 CJI + 30)\n2019: 34 (1 CJI + 33)\nஎனவே சரியான வரிசை 1 -> 2 -> 3 -> 4.",
        "Present total strength of Supreme Court: 34 (1 Chief Justice + 33 Judges).",
        "தற்போதைய உச்ச நீதிமன்ற மொத்த நீதிபதிகள் எண்ணிக்கை: 34 (1 தலைமை நீதிபதி + 33 நீதிபதிகள்).",
        "Parliament increases judge strength by enacting an ordinary law under Article 124(1).",
        "நாடாளுமன்றம் சாதாரணச் சட்டம் இயற்றி நீதிபதிகள் எண்ணிக்கையை உயர்த்துகிறது.",
        "No constitutional amendment under Art 368 is required to change judge numbers.",
        "இதற்கு சரத்து 368 அரசியலமைப்புத் திருத்தம் தேவையில்லை."))

    # Q80
    b4.append(mk_q(80, "Hard", "Scenario",
        "In Supreme Court Bar Association v. Union of India (1998), the Supreme Court clarified its powers under Article 129 (Contempt of Court) and Article 142 (Complete Justice). What landmark limitation was established regarding punishing a lawyer for contempt?",
        "உச்ச நீதிமன்ற பார் அசோசியேஷன் எதிர் இந்திய யூனியன் (1998) வழக்கில், சரத்து 129 (அவமதிப்பு) மற்றும் சரத்து 142 (முழுமையான நீதி) பற்றிய என்ன முக்கிய வரம்பை உச்ச நீதிமன்றம் நிர்ணயித்தது?",
        {"A": "The Supreme Court CANNOT suspend an advocate from practicing law as a punishment for contempt, because that power belongs exclusively to the Bar Council under the Advocates Act, 1961", "B": "The Supreme Court can permanently cancel an advocate's license without hearing", "C": "Contempt proceedings cannot be initiated against lawyers", "D": "Supreme Court can sentence a lawyer only to fine, never to imprisonment"},
        {"A": "நீதிமன்ற அவமதிப்பிற்காக ஒரு வழக்கறிஞரை வழக்கறிஞர் பணியிலிருந்து இடைநீக்கம் செய்ய உச்ச நீதிமன்றத்திற்கு அதிகாரம் இல்லை; ஏனெனில் அந்த அதிகாரம் வழக்கறிஞர்கள் சட்டம் 1961-ன் கீழ் வழக்கறிஞர்கள் परिषத்திற்கு (Bar Council) மட்டுமே உரியது", "B": "விசாரணையின்றி வழக்கறிஞர் உரிமத்தை உச்ச நீதிமன்றம் நிரந்தரமாக ரத்து செய்யலாம்", "C": "வழக்கறிஞர்களுக்கு எதிராக அவமதிப்பு நடவடிக்கை எடுக்க முடியாது", "D": "வழக்கறிஞருக்கு அபராதம் மட்டுமே விதிக்க முடியும், சிறை தண்டனை விதிக்க முடியாது"},
        "A",
        "In Supreme Court Bar Association (1998), SC held that while it has power to punish for contempt under Art 129, it CANNOT debar an advocate from practice or suspend his license under Art 142, as that statutory power belongs exclusively to the Bar Council under the Advocates Act 1961.",
        "உச்ச நீதிமன்ற பார் அசோசியேஷன் (1998) வழக்கில், அவமதிப்புக்குத் தண்டிக்கும் அதிகாரம் உச்ச நீதிமன்றத்திற்கு இருந்தாலும், வழக்கறிஞர் உரிமத்தை இடைநீக்கம் செய்யவோ ரத்து செய்யவோ முடியாது; அது வழக்கறிஞர்கள் परिषத்தின் (Bar Council) பிரத்தியேக அதிகாரமாகும் எனத் தீர்ப்பளித்தது.",
        "Reiterated that Article 142 cannot be used to override statutory provisions of the Advocates Act 1961.",
        "சரத்து 142-ஐப் பயன்படுத்தி வழக்கறிஞர்கள் சட்ட விதிகளை மீற முடியாது என்பதை மீண்டும் வலியுறுத்தியது.",
        "Courts can punish with fine or imprisonment under Contempt Act.",
        "நீதிமன்றங்கள் அவமதிப்புச் சட்டப்படி அபராதம் அல்லது சிறைத் தண்டனை அளிக்கலாம்.",
        "Bar Council handles disciplinary license suspension.",
        "வழக்கறிஞர்கள் परिषம் உரிம இடைநீக்கத்தைக் கவனிக்கும்."))

    # Q81
    b4.append(mk_q(81, "Medium", "Direct",
        "Under Article 134(1)(a) and (b) of the Constitution, when does an appeal lie AS OF RIGHT (without needing a Certificate of Fitness) from a High Court to the Supreme Court in a criminal matter?",
        "சரத்து 134(1)(a) மற்றும் (b)-ன் படி, ஒரு குற்றவியல் வழக்கில் உயர் நீதிமன்ற சான்றிதழ் இன்றி நேரடியாக உரிமையாகவே (As of Right) உச்ச நீதிமன்றத்திற்கு மேல்முறையீடு செய்யும் நிலை எப்போது ஏற்படுகிறது?",
        {"A": "If the High Court on appeal has reversed an order of acquittal of an accused person and sentenced him to death", "B": "If the High Court imposes a fine of over Rs. 1 Lakh", "C": "If the accused is a Member of Parliament", "D": "If the case has been pending in High Court for more than 10 years"},
        {"A": "கீழ் நீதிமன்றத்தின் விடுதலையை உயர் நீதிமன்றம் ரத்து செய்து, குற்றம் சாட்டப்பட்டவருக்கு மரண தண்டனை விதித்திருந்தால்", "B": "உயர் நீதிமன்றம் ரூ. 1 லட்சத்திற்கு மேல் அபராதம் விதித்திருந்தால்", "C": "குற்றம் சாட்டப்பட்டவர் நாடாளுமன்ற உறுப்பினராக இருந்தால்", "D": "வழக்கு உயர் நீதிமன்றத்தில் 10 ஆண்டுகளுக்கு மேல் நிலுவையில் இருந்தால்"},
        "A",
        "Under Article 134(1)(a)&(b), an appeal lies to SC as of right if High Court: 1. Reverses an acquittal and sentences accused to death, OR 2. Withdraws a trial from subordinate court to itself and sentences accused to death.",
        "சரத்து 134(1)(a)&(b)-ன் படி, கீழ் நீதிமன்றத்தின் விடுதலையை உயர் நீதிமன்றம் ரத்து செய்து மரண தண்டனை விதித்தாலோ அல்லது வழக்கை தானே எடுத்து மரண தண்டனை விதித்தாலோ சான்றிதழ் இன்றியே நேரடியாக மேல்முறையீடு செய்ய உரிமை உண்டு.",
        "If HC upholds acquittal or passes lesser sentence than death, appeal requires Certificate under Art 134A or Special Leave under Art 136.",
        "மரண தண்டனை தவிர பிற தண்டனைகளுக்கு சான்றிதழ் அல்லது SLP தேவை.",
        "Guarantees highest protection when human life is at stake.",
        "உயிர் தண்டனை சார்ந்த வழக்குகளில் உயரிய பாதுகாப்பு அளிக்கிறது.",
        "Parliament can enlarge criminal appellate jurisdiction under Art 134(2).",
        "நாடாளுமன்றம் குற்றவியல் மேல்முறையீட்டு அதிகாரத்தை விரிவுபடுத்தலாம்."))

    # Q82
    b4.append(mk_q(82, "Medium", "Direct",
        "Under Article 133 of the Constitution, what is the core requirement for a Civil Appeal to lie from a High Court to the Supreme Court?",
        "சரத்து 133-ன் படி, உயர் நீதிமன்றத்திலிருந்து உச்ச நீதிமன்றத்திற்குச் சிவில் மேல்முறையீடு (Civil Appeal) செய்வதற்கான முக்கியத் தேவை என்ன?",
        {"A": "The High Court certifies under Article 134A that the case involves a substantial question of law of general importance and that in its opinion the question needs to be decided by the Supreme Court", "B": "The dispute value must be at least Rs. 10 Lakhs", "C": "The dispute must involve land property owned by the State Government", "D": "The appeal must be filed within 7 days of High Court judgment"},
        {"A": "வழக்கில் பொது முக்கியத்துவம் வாய்ந்த சட்டக் கேள்வி அடங்கியுள்ளது என்றும், அது உச்ச நீதிமன்றத்தால் தீர்மானிக்கப்பட வேண்டும் என்றும் உயர் நீதிமன்றம் சரத்து 134A-ன் கீழ் சான்றளித்தல்", "B": "வழக்கு மதிப்பு குறைந்தது ரூ. 10 லட்சமாக இருக்க வேண்டும்", "C": "வழக்கு மாநில அரசின் நிலச் சொத்து தொடர்பதாக இருக்க வேண்டும்", "D": "உயர் நீதிமன்ற தீர்ப்பு வந்த 7 நாட்களுக்குள் மேல்முறையீடு செய்ய வேண்டும்"},
        "A",
        "Under Article 133(1) (as amended by 30th CAA 1972), a civil appeal lies to SC if HC certifies under Art 134A: (a) that the case involves a substantial question of law of general importance, and (b) that in the opinion of the HC the said question needs to be decided by the SC.",
        "சரத்து 133(1)-ன் படி (30வது திருத்தம் 1972-க்குப் பின்), பொது முக்கியத்துவம் வாய்ந்த சட்டக் கேள்வி உள்ளதாகவும், அதை உச்ச நீதிமன்றம் விசாரிக்க வேண்டும் என்றும் உயர் நீதிமன்றம் சான்றளித்தால் சிவில் மேல்முறையீடு செய்ய முடியும்.",
        "The monetary limit requirement (Rs. 20,000) was ABOLISHED by the 30th Constitutional Amendment Act, 1972.",
        "பண வரம்பு நிபந்தனை (ரூ. 20,000) 1972-ன் 30வது திருத்தச் சட்டத்தால் ரத்து செய்யப்பட்டது.",
        "Focus shifted from monetary value of case to legal importance of question.",
        "பண மதிப்பிலிருந்து சட்டக் கேள்வியின் முக்கியத்துவத்திற்கு கவனம் மாறியது.",
        "High Court certificate under Art 134A is mandatory for Art 133.",
        "சரத்து 134A சான்றிதழ் அவசியம்."))

    # Q83
    b4.append(mk_q(83, "Hard", "Statement",
        "Consider the following statements regarding the Collegium System for Judicial Appointments in India:\n1. Supreme Court Judges appointment collegium consists of the CJI + 4 senior-most SC judges.\n2. High Court Judges appointment collegium in the Supreme Court consists of the CJI + 2 senior-most SC judges.\n3. Recommendation of CJI without consulting the collegium is NOT binding on the Government.\nWhich of the statements given above are correct?",
        "இந்தியாவில் நீதிபதிகள் நியமனத்திற்கான கொலீஜியம் முறை பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. உச்ச நீதிமன்ற நீதிபதிகள் நியமனக் கொலீஜியம் என்பது CJI + 4 மூத்த உச்ச நீதிமன்ற நீதிபதிகளைக் கொண்டது.\n2. உயர் நீதிமன்ற நீதிபதிகள் நியமனத்திற்கு உச்ச நீதிமன்றத்தில் உள்ள கொலீஜியம் CJI + 2 மூத்த உச்ச நீதிமன்ற நீதிபதிகளைக் கொண்டது.\n3. கொலீஜியத்தைக் கலந்தாலோசிக்காமல் தலைமை நீதிபதி அளிக்கும் பரிந்துரை அரசைக்கட்டுப்படுத்தாது.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
        {"A": "1, 2 and 3", "B": "1 and 2 only", "C": "2 and 3 only", "D": "1 and 3 only"},
        {"A": "1, 2 மற்றும் 3", "B": "1 மற்றும் 2 மட்டும்", "C": "2 மற்றும் 3 மட்டும்", "D": "1 மற்றும் 3 மட்டும்"},
        "A",
        "All three statements are correct (Third Judges Case 1998): 1. SC appointments = CJI + 4 senior SC judges. 2. HC appointments/transfers = CJI + 2 senior SC judges. 3. Non-collegium recommendation by CJI is non-binding.",
        "மூன்று கூற்றுகளும் சரியானவை (3வது நீதிபதிகள் வழக்கு 1998): 1. உச்ச நீதிமன்ற நியமனம் = CJI + 4 மூத்த நீதிபதிகள். 2. உயர் நீதிமன்ற நியமனம் = CJI + 2 மூத்த நீதிபதிகள். 3. கொலீஜியமில்லாத பரிந்துரை செல்லாது.",
        "Notice the difference: 4 senior judges for SC appointment, but 2 senior judges for HC appointment.",
        "உச்ச நீதிமன்றத்திற்கு 4 மூத்த நீதிபதிகள், உயர் நீதிமன்றத்திற்கு 2 மூத்த நீதிபதிகள் என்ற வேறுபாட்டைக் கவனிக்கவும்.",
        "Collegium decision requires consensus; if 2 judges give adverse opinion, CJI cannot recommend.",
        "இரண்டு நீதிபதிகள் எதிர்த்தால் CJI பரிந்துரைக்க முடியாது.",
        "3rd Judges Case 1998 formalized these numerical rules.",
        "1998 3வது நீதிபதிகள் வழக்கு எண்களை வரையறுத்தது."))

    # Q84
    b4.append(mk_q(84, "Medium", "Direct",
        "In Vishaka v. State of Rajasthan (1997), the Supreme Court laid down binding guidelines to prevent Sexual Harassment of Women at Workplace under which Articles of the Constitution?",
        "விசாக்கா எதிர் ராஜஸ்தான் மாநிலம் (1997) வழக்கில், பணியிடங்களில் பெண்களுக்கு எதிரான பாலியல் தொல்லையைத் தடுக்க உச்ச நீதிமன்றம் அரசியலமைப்பின் எந்தச் சரத்துகளின் கீழ் பிணைக்கும் வழிகாட்டுதல்களை வழங்கியது?",
        {"A": "Articles 14, 19, 21 read with Article 141 & 142", "B": "Article 370 and Article 356", "C": "Article 105 and Article 194", "D": "Article 280 and Article 315"},
        {"A": "சரத்துகள் 14, 19, 21 மற்றும் சரத்து 141 & 142", "B": "சரத்து 370 மற்றும் சரத்து 356", "C": "சரத்து 105 மற்றும் சரத்து 194", "D": "சரத்து 280 மற்றும் சரத்து 315"},
        "A",
        "In Vishaka (1997), SC used international conventions (CEDAW) and Articles 14, 19, and 21 to lay down binding guidelines under Articles 141 and 142 to protect women at workplaces until Parliament enacted a law.",
        "விசாக்கா (1997) வழக்கில், பன்னாட்டு உடன்படிக்கை (CEDAW) மற்றும் சரத்துகள் 14, 19, 21 ஆகியவற்றின் அடிப்படையில் சரத்து 141 மற்றும் 142-ன் கீழ் சட்டம் வரும் வரை பிணைக்கும் வழிகாட்டுதல்களை உச்ச நீதிமன்றம் வழங்கியது.",
        "These guidelines led to the enactment of the POSH Act, 2013.",
        "இவ்வழிகாட்டுதல்களே 2013 POSH சட்டம் வரக் காரணமாக அமைந்தன.",
        "Classic example of Judicial Legislation / Law-making by SC under Article 142.",
        "சரத்து 142-ன் கீழ் உச்ச நீதிமன்றத்தின் சட்டம் இயற்றும் அதிகாரத்திற்குச் சான்றாகும்.",
        "Protected Gender Equality and Dignity.",
        "பாலின சமத்துவம் மற்றும் கண்ணியத்தைப் பாதுகாத்தது."))

    # Q85
    b4.append(mk_q(85, "Medium", "Direct",
        "In Olga Tellis v. Bombay Municipal Corporation (1985), how did the Supreme Court expand the scope of 'Right to Life' under Article 21?",
        "ஓல்கா டெல்லிஸ் எதிர் பம்பாய் மாநகராட்சி (1985) வழக்கில், சரத்து 21-ன் கீழான 'வாழும் உரிமையை' (Right to Life) உச்ச நீதிமன்றம் எவ்வாறு விரிவுபடுத்தியது?",
        {"A": "Right to Life includes the Right to Livelihood", "B": "Right to Life includes the Right to Property", "C": "Right to Life applies only to citizens, not pavement dwellers", "D": "Right to Life guarantees government jobs for all graduates"},
        {"A": "வாழும் உரிமையில் 'வாழ்வாதார உரிமையும்' (Right to Livelihood) அடங்கும்", "B": "வாழும் உரிமையில் 'சொத்து உரிமையும்' அடங்கும்", "C": "வாழும் உரிமை குடிமக்களுக்கு மட்டுமே பொருந்தும், நடைபாதைவாசிகளுக்கு அல்ல", "D": "வாழும் உரிமை பட்டதாரிகள் அனைவருக்கும் அரசு வேலையை உத்தரவாதம் செய்கிறது"},
        "A",
        "In Olga Tellis (1985) (Pavement Dwellers Case), a 5-judge bench ruled that the Right to Life under Article 21 includes the Right to Livelihood, because no person can live without the means of living.",
        "ஓல்கா டெல்லிஸ் (1985) (நடைபாதைவாசிகள் வழக்கு) வழக்கில், 5 நீதிபதிகள் அமர்வு வாழும் உரிமையில் (Art 21) வாழ்வாதார உரிமையும் அடங்கும் எனக் கூறியது; ஏனெனில் வாழ்வாதாரமின்றி எவரும் வாழ முடியாது.",
        "Depriving a person of his livelihood deprives him of his life.",
        "ஒருவரின் வாழ்வாதாரத்தைப் பறிப்பது அவரது வாழ்வையே பறிப்பதாகும்.",
        "High-yield landmark case on Article 21 expansion.",
        "சரத்து 21 விரிவாக்கம் பற்றிய முக்கிய வழக்கு.",
        "Mandated procedural fairness before eviction.",
        "வெளியேற்றத்திற்கு முன் நியாயமான விசாரணை அவசியம் என்றது."))

    # Q86
    b4.append(mk_q(86, "Medium", "Direct",
        "In K.S. Puttaswamy v. Union of India (2017), what unanimous declaration did the 9-judge Constitution Bench make regarding the 'Right to Privacy'?",
        "கே.எஸ். புட்டசாமி எதிர் இந்திய யூனியன் (2017) வழக்கில், 9 நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வு 'தனிநபர் அந்தரங்க உரிமை' (Right to Privacy) பற்றி என்ன ஒருமனதான அறிவிப்பை வெளியிட்டது?",
        {"A": "Right to Privacy is an intrinsic part of the Right to Life and Personal Liberty under Article 21 and Part III", "B": "Right to Privacy is a statutory right, not a fundamental right", "C": "Right to Privacy applies only to corporate entities", "D": "Right to Privacy can be abolished by executive order"},
        {"A": "தனிநபர் அந்தரங்க உரிமை என்பது சரத்து 21 மற்றும் பகுதி III-ன் கீழான வாழ்வு மற்றும் தனிநபர் சுதந்திர உரிமையின் பிரிக்க முடியாத அடிப்படை உரிமையாகும்", "B": "அந்தரங்க உரிமை ஒரு சட்டப்பூர்வ உரிமையே தவிர அடிப்படை உரிமை அல்ல", "C": "அந்தரங்க உரிமை கார்ப்பரேட் நிறுவனங்களுக்கு மட்டுமே பொருந்தும்", "D": "அந்தரங்க உரிமையை நிர்வாக உத்தரவு மூலம் ரத்து செய்யலாம்"},
        "A",
        "In K.S. Puttaswamy (2017), all 9 judges unanimously held that Privacy is a Fundamental Right protected under Article 21 and Part III of the Constitution, overruling M.P. Sharma (1954) and Kharak Singh (1962).",
        "கே.எஸ். புட்டசாமி (2017) வழக்கில் 9 நீதிபதிகளும் ஒருமனதாக அந்தரங்க உரிமை என்பது சரத்து 21-ன் கீழான அடிப்படை உரிமை எனக் கூறி, எம்பி சர்மா (1954) மற்றும் கடக் சிங் (1962) தீர்ப்புகளை மாற்றினர்.",
        "Privacy includes Informational Privacy, Bodily Autonomy, and Spatial Privacy.",
        "தகவல் அந்தரங்கம், உடல் தன்னாட்சி மற்றும் இடஞ்சார்ந்த அந்தரங்கம் இதில் அடங்கும்.",
        "Overruled 8-judge bench in M.P. Sharma and 6-judge bench in Kharak Singh.",
        "முந்தைய பெரிய அமர்வு தீர்ப்புகளை மாற்றியமைத்தது.",
        "Subject only to reasonable restrictions (legitimate state aim, proportionality).",
        "விகிதாச்சார சோதனைக்கு (Proportionality Test) உட்பட்டது."))

    # Q87
    b4.append(mk_q(87, "Medium", "Direct",
        "In Navtej Singh Johar v. Union of India (2018), what did the Supreme Court strike down regarding Section 377 of the Indian Penal Code?",
        "நவ்தேஜ் சிங் ஜோஹர் எதிர் இந்திய யூனியன் (2018) வழக்கில், இந்திய தண்டனைச் சட்டத்தின் (IPC) பிரிவு 377 பற்றி உச்ச நீதிமன்றம் என்ன தீர்ப்பளித்தது?",
        {"A": "Decriminalized consensual homosexual acts between consenting adults under Section 377 IPC", "B": "Upheld Section 377 in its entirety", "C": "Increased punishment under Section 377", "D": "Abolished the Indian Penal Code completely"},
        {"A": "IPC பிரிவு 377-ன் கீழ் வயதுவந்த இருவரின் சம்மதத்துடனான ஒருபாலின உறவைக் குற்றமற்றதாக்கியது", "B": "பிரிவு 377-ஐ முழுமையாக உறுதி செய்தது", "C": "பிரிவு 377-ன் கீழான தண்டனையை உயர்த்தியது", "D": "இந்திய தண்டனைச் சட்டத்தை முற்றிலும் ரத்து செய்தது"},
        "A",
        "In Navtej Singh Johar (2018), SC held that Section 377 IPC, in so far as it criminalized consensual sexual acts between adults in private, violated Articles 14, 15, 19, and 21, overruling Suresh Kumar Koushal case (2013).",
        "நவ்தேஜ் சிங் ஜோஹர் (2018) வழக்கில், வயதுவந்தோரின் சம்மதத்துடனான உறவைக் குற்றமாக்கும் IPC 377-ன் பகுதி சரத்துகள் 14, 15, 19, 21-க்கு முரணானது எனக்கூறி, சுரேஷ் குமார் கௌஷல் (2013) தீர்ப்பை மாற்றியது.",
        "Recognized Constitutional Morality over Majoritarian Morality.",
        "பெரும்பான்மை ஒழுக்கத்தை விட அரசியலமைப்பு ஒழுக்கத்தை (Constitutional Morality) உயர்த்தியது.",
        "Affirmed LGBTQ+ community rights to equality and dignity.",
        "சமத்துவம் மற்றும் கண்ணிய உரிமையை உறுதி செய்தது.",
        "5-judge Constitution Bench judgment.",
        "5 நீதிபதிகள் அமர்வு தீர்ப்பு."))

    # Q88
    b4.append(mk_q(88, "Hard", "Direct",
        "Can the Supreme Court of India reduce or abolish its OWN Writ Jurisdiction under Article 32 by invoking administrative rules or statutory interpretations?",
        "உச்ச நீதிமன்றம் தனது சொந்த நிர்வாக விதிகள் அல்லது சட்ட விளக்கங்களைப் பயன்படுத்தி சரத்து 32-ன் கீழான தனது பேராணை அதிகாரத்தைக் குறைக்கவோ அல்லது ஒழிக்கவோ முடியுமா?",
        {"A": "No, because Article 32 is itself a Fundamental Right AND a core component of the unamendable Basic Structure of the Constitution", "B": "Yes, CJI can abolish writ jurisdiction during summer vacation", "C": "Yes, if Lok Sabha passes a resolution by 2/3rd majority", "D": "Yes, during financial emergency"},
        {"A": "இல்லை, ஏனெனில் சரத்து 32 என்பதே ஒரு அடிப்படை உரிமை மற்றும் அரசியலமைப்பின் திருத்தப்பட முடியாத அடிப்படை கட்டமைப்பின் முக்கிய அங்கமாகும்", "B": "ஆம், கோடை விடுமுறையில் CJI பேராணை அதிகாரத்தை ஒழிக்கலாம்", "C": "ஆம், மக்களவை 2/3 பெரும்பான்மையில் தீர்மானம் நிறைவேற்றினால்", "D": "ஆம், நிதி அவசரநிலையின் போது செய்யலாம்"},
        "A",
        "Article 32 is both a Fundamental Right (Heart and Soul of Constitution as per Dr. Ambedkar) and a part of the BASIC STRUCTURE (Fertilizer Corporation 1981, L. Chandra Kumar 1997). Neither SC nor Parliament can abrogate it.",
        "சரத்து 32 என்பது அடிப்படை உரிமை (டாக்டர் அம்பேத்கர் கூறிய இதயமும் ஆன்மாவும்) மற்றும் அடிப்படை கட்டமைப்பின் பகுதியாகும் (சந்திரகுமார் வழக்கு 1997). உச்ச நீதிமன்றமோ நாடாளுமன்றமோ அதை அழிக்க முடியாது.",
        "Classic TNPSC trap question on untouchable status of Article 32.",
        "சரத்து 32-ன் பாதுகாக்கப்பட்ட நிலை பற்றிய முக்கிய வினா.",
        "Guarantees direct access to the Supreme Court.",
        "நேரடியாக உச்ச நீதிமன்றத்தை அணுக உத்தரவாதம் அளிக்கிறது.",
        "Cannot be suspended except under Article 359 during National Emergency.",
        "தேசிய அவசரநிலை தவிர பிற நேரங்களில் நிறுத்த முடியாது."))

    # Q89
    b4.append(mk_q(89, "Hard", "Scenario",
        "Under Article 71 of the Constitution, which authority has EXCLUSIVE and ORIGINAL jurisdiction to inquire into and decide all doubts and disputes arising out of or in connection with the election of the President or Vice-President of India?",
        "அரசியலமைப்பின் சரத்து 71-ன் கீழ், இந்தியக் குடியரசுத் தலைவர் அல்லது குடியரசுத் துணைத் தலைவர் தேர்தல் தொடர்பான அனைத்து சந்தேகங்கள் மற்றும் சர்ச்சைகளை விசாரித்துத் தீர்மானிக்கும் பிரத்தியேக மூல அதிகாரம் (Exclusive Original Jurisdiction) யாருக்கு உள்ளது?",
        {"A": "Election Commission of India", "B": "Supreme Court of India", "C": "Parliament of India", "D": "Delhi High Court"},
        {"A": "இந்தியத் தேர்தல் ஆணையத்திற்கு", "B": "இந்திய உச்ச நீதிமன்றத்திற்கு", "C": "இந்திய நாடாளுமன்றத்திற்கு", "D": "டெல்லி உயர் நீதிமன்றத்திற்கு"},
        "B",
        "Under Article 71(1), all doubts and disputes arising out of or in connection with the election of a President or Vice-President shall be inquired into and decided by the SUPREME COURT whose decision shall be final.",
        "சரத்து 71(1)-ன் படி குடியரசுத் தலைவர் அல்லது குடியரசுத் துணைத் தலைவர் தேர்தல் குறித்த அனைத்துச் சர்ச்சைகளையும் விசாரித்து முடிவெடுக்கும் பிரத்தியேக அதிகாரம் உச்ச நீதிமன்றத்திற்கு மட்டுமே உண்டு; அதன் முடிவே இறுதியானது.",
        "TNPSC Trap Alert: Candidates mistakenly choose 'Election Commission of India' or 'Article 131'. Presidential election disputes fall under Article 71, decided exclusively by Supreme Court!",
        "TNPSC பொறி எச்சரிக்கை: தேர்வர்கள் தேர்தல் ஆணையம் அல்லது சரத்து 131 எனத் தவறாகத் தேர்ந்தெடுக்கின்றனர். குடியரசுத் தலைவர் தேர்தல் சர்ச்சை சரத்து 71-ன் கீழ் உச்ச நீதிமன்றத்திற்கு மட்டுமே உரியது!",
        "Decision of Supreme Court under Art 71 is final.",
        "உச்ச நீதிமன்ற தீர்ப்பே இறுதியானது.",
        "Election petition must be presented after election results are declared.",
        "தேர்தல் முடிவு வந்த பிறகே மனு தாக்கல் செய்ய முடியும்."))

    # Q90
    b4.append(mk_q(90, "Hard", "Statement",
        "Consider the following statements regarding Public Interest Litigation (PIL) guidelines issued by the Supreme Court in 1988/2003:\n1. Matters related to landlord-tenant disputes and eviction shall NOT be entertained as PIL.\n2. Matters related to admission to educational institutions shall NOT be entertained as PIL.\n3. Petitions against pollution, bonded labor, and atrocities on women CAN be entertained as PIL.\nWhich of the statements given above are correct?",
        "1988/2003-ல் உச்ச நீதிமன்றம் வெளியிட்ட பொது நல வழக்கு (PIL) வழிகாட்டுதல்கள் பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. வீட்டின் உரிமையாளர்-வாடகைதாரர் தகராறுகள் மற்றும் வெளியேற்றம் சார்ந்த விவகாரங்கள் PIL-ஆக ஏற்கப்படக் கூடாது.\n2. கல்வி நிறுவனங்களில் சேர்க்கை தொடர்பான விவகாரங்கள் PIL-ஆக ஏற்கப்படக் கூடாது.\n3. மாசுபடுதல், கொத்தடிமைகள் மற்றும் பெண்களுக்கு எதிரான கொடுமைகள் பற்றிய மனுக்கள் PIL-ஆக ஏற்கப்படலாம்.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
        {"A": "1, 2 and 3", "B": "1 and 2 only", "C": "2 and 3 only", "D": "1 and 3 only"},
        {"A": "1, 2 மற்றும் 3", "B": "1 மற்றும் 2 மட்டும்", "C": "2 மற்றும் 3 மட்டும்", "D": "1 மற்றும் 3 மட்டும்"},
        "A",
        "All three statements are correct according to SC PIL Guidelines (1988/2003). Private landlord-tenant disputes, service/employment matters, and college admissions are EXCLUDED from PIL to prevent abuse for private gain.",
        "மூன்று கூற்றுகளும் சரியானவை (SC PIL வழிகாட்டுதல்கள் 1988/2003). தனிநபர் வாடகைத் தகராறு, வேலைவாய்ப்பு மற்றும் கல்லூரிச் சேர்க்கை ஆகியவை தனிநபர் சுயநலத்திற்கு துஷ்பிரயோகம் செய்யப்படுவதைத் தடுக்க PIL-லிருந்து விலக்கப்பட்டுள்ளன.",
        "PIL is meant for public injury, enforcing public duty, or protecting vulnerable sections who cannot reach court.",
        "பொதுப்பாதிப்பு மற்றும் ஒடுக்கப்பட்ட மக்களின் நலனுக்காகவே PIL ஒதுக்கப்பட்டுள்ளது.",
        "Prevents clogging of Supreme Court with private civil litigation disguised as PIL.",
        "தனியார் வழக்குகள் PIL போர்வையில் வருவதை இது தடுக்கிறது.",
        "Frivolous PILs are penalized with heavy costs.",
        "போலியான PIL-களுக்கு அபராதம் விதிக்கப்படும்."))

    # Q91
    b4.append(mk_q(91, "Medium", "Direct",
        "What is the maximum number of judges permitted in the Supreme Court of India as per the Supreme Court (Number of Judges) Amendment Act, 2019?",
        "உச்ச நீதிமன்ற (நீதிபதிகள் எண்ணிக்கை) திருத்தச் சட்டம் 2019-ன் படி, இந்திய உச்ச நீதிமன்றத்தில் அனுமதிக்கப்பட்டுள்ள அதிகபட்ச நீதிபதிகளின் எண்ணிக்கை யாது?",
        {"A": "31 (1 CJI + 30 Judges)", "B": "34 (1 CJI + 33 Judges)", "C": "35 (1 CJI + 34 Judges)", "D": "40 (1 CJI + 39 Judges)"},
        {"A": "31 (1 CJI + 30 நீதிபதிகள்)", "B": "34 (1 CJI + 33 நீதிபதிகள்)", "C": "35 (1 CJI + 34 நீதிபதிகள்)", "D": "40 (1 CJI + 39 நீதிபதிகள்)"},
        "B",
        "The Supreme Court (Number of Judges) Amendment Act, 2019 increased the strength of SC judges from 31 to 34 (including the Chief Justice of India).",
        "2019-ன் திருத்தச் சட்டம் உச்ச நீதிமன்ற நீதிபதிகள் எண்ணிக்கையை (தலைமை நீதிபதி உட்பட) 31-லிருந்து 34 ஆக உயர்த்தியது.",
        "1950 (8) -> 1956 (11) -> 1960 (14) -> 1977 (18) -> 1986 (26) -> 2009 (31) -> 2019 (34).",
        "எண்ணிக்கை வளர்ச்சி: 1950 (8) முதல் 2019 (34) வரை.",
        "Parliament increases judge strength by simple law under Article 124(1).",
        "சரத்து 124(1)-ன் கீழ் நாடாளுமன்றச் சட்டத்தால் இது மாற்றப்படுகிறது.",
        "Present sanctioned strength is 34.",
        "தற்போதைய அனுமதிக்கப்பட்ட எண்ணிக்கை 34."))

    # Q92
    b4.append(mk_q(92, "Hard", "Scenario",
        "If a High Court judge is appointed as an Ad Hoc Judge of the Supreme Court under Article 127, what happens to his salary, allowances, and duties during his tenure in the Supreme Court?",
        "சரத்து 127-ன் கீழ் ஒரு உயர் நீதிமன்ற நீதிபதி உச்ச நீதிமன்றத் தற்காலிக (Ad Hoc) நீதிபதியாக நியமிக்கப்பட்டால், உச்ச நீதிமன்றத்தில் அவரது பணிக் காலத்தில் அவருடைய சம்பளம், படிகள் மற்றும் கடமைகள் என்னவாகும்?",
        {"A": "He shall have all the jurisdiction, powers and privileges, and shall discharge the duties of a Supreme Court judge, taking precedence over his High Court duties", "B": "He receives no extra allowances and cannot hear constitutional cases", "C": "He loses his High Court judgeship permanently", "D": "He functions only as a consultant without judicial voting power"},
        {"A": "அவர் உச்ச நீதிமன்ற நீதிபதியின் அனைத்து அதிகாரங்கள், சலுகைகள் மற்றும் அதிகார வரம்பைப் பெறுவார்; மேலும் உயர் நீதிமன்றப் பணிகளை விட உச்ச நீதிமன்றப் பணிகளுக்கு முன்னுரிமை அளித்து ஆற்றுவார்", "B": "அவருக்குக் கூடுதல் படிகள் கிடைக்காது, அரசியலமைப்பு வழக்குகளை விசாரிக்க முடியாது", "C": "அவர் தனது உயர் நீதிமன்ற நீதிபதி பதவியை நிரந்தரமாக இழப்பார்", "D": "அவர் வாக்களிக்கும் அதிகாரமின்றி ஆலோசகராக மட்டுமே செயல்படுவார்"},
        "A",
        "Under Article 127(2), it is the duty of the judge so requested to attend the sittings of the Supreme Court in priority over his other duties, and while so attending, he HAS ALL THE JURISDICTION, POWERS AND PRIVILEGES of a Supreme Court judge.",
        "சரத்து 127(2)-ன் படி, கோரப்பட்ட நீதிபதி தனது பிற பணிகளை விட உச்ச நீதிமன்ற அமர்வுகளுக்கு முன்னுரிமை அளிப்பது கடமையாகும்; மேலும் அவர் உச்ச நீதிமன்ற நீதிபதியின் அனைத்து அதிகாரங்களையும் சலுகைகளையும் பெறுவார்.",
        "Ad hoc judge receives such allowances as the President may by order determine.",
        "குடியரசுத் தலைவர் தீர்மானிக்கும் படிகளைப் பெறுவார்.",
        "He returns to his High Court after the SC session ends.",
        "அமர்வுக்குப் பின் உயர் நீதிமன்றப் பணிக்குத் திரும்புவார்.",
        "Maintains quorum in SC.",
        "கோரத்தைப் பராமரிக்க உதவுகிறார்."))

    # Q93
    b4.append(mk_q(93, "Medium", "Direct",
        "Which Constitutional Amendment Act added Article 134A empowering High Courts to issue certificates for appeal to the Supreme Court?",
        "உயர் நீதிமன்றங்கள் உச்ச நீதிமன்ற மேல்முறையீட்டுச் சான்றிதழை வழங்க அதிகாரம் அளிக்கும் சரத்து 134A-ஐ சேர்த்த அரசியலமைப்புத் திருத்தச் சட்டம் எது?",
        {"A": "42nd Constitutional Amendment Act, 1976", "B": "44th Constitutional Amendment Act, 1978", "C": "24th Constitutional Amendment Act, 1971", "D": "86th Constitutional Amendment Act, 2002"},
        {"A": "42வது அரசியலமைப்புத் திருத்தச் சட்டம், 1976", "B": "44வது அரசியலமைப்புத் திருத்தச் சட்டம், 1978", "C": "24வது அரசியலமைப்புத் திருத்தச் சட்டம், 1971", "D": "86வது அரசியலமைப்புத் திருத்தச் சட்டம், 2002"},
        "B",
        "Article 134A was inserted by the 44th Constitutional Amendment Act, 1978. It allows the High Court to determine whether to grant a certificate of fitness for appeal to SC under Art 132, 133, or 134 either suo motu or on oral application by the aggrieved party immediately after passing judgment.",
        "சரத்து 134A என்பது 1978-ன் 44வது திருத்தச் சட்டத்தால் சேர்க்கப்பட்டது. தீர்ப்பு வந்தவுடனே தானாக முன்வந்தோ அல்லது வாய்மொழி விண்ணப்பத்தின் பேரிலோ மேல்முறையீட்டுச் சான்றிதழ் அளிக்க இது வழிசெய்கிறது.",
        "Speeds up the appeal certification process.",
        "மேல்முறையீட்டு சான்றிதழ் வழங்கும் முறையை வேகப்படுத்தியது.",
        "Applies to Articles 132, 133, and 134.",
        "சரத்துகள் 132, 133, 134 ஆகிய மூன்றிற்கும் பொருந்தும்.",
        "Avoids separate written delay applications.",
        "தனி எழுத்துப்பூர்வ தாமத மனுக்களைத் தவிர்க்கிறது."))

    # Q94
    b4.append(mk_q(94, "Hard", "Statement",
        "Consider the following statements regarding the Supreme Court of India as the 'Guardian of the Constitution':\n1. It protects Fundamental Rights through Writ Jurisdiction under Article 32.\n2. It tests the constitutional validity of Parliamentary and State laws through Judicial Review.\n3. It resolves federal disputes between Centre and States under Original Jurisdiction (Article 131).\nWhich of the statements given above are correct?",
        "இந்திய அரசியலமைப்பின் 'பாதுகாவலனாக' (Guardian of the Constitution) உச்ச நீதிமன்றம் செயல்படுவது பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. சரத்து 32-ன் கீழான பேராணை அதிகாரம் மூலம் இது அடிப்படை உரிமைகளைப் பாதுகாக்கிறது.\n2. நீதித்துறை மறுஆய்வு மூலம் நாடாளுமன்ற மற்றும் மாநிலச் சட்டங்களின் அரசியலமைப்புச் செல்லுபடித் தன்மையை சோதிக்கிறது.\n3. மூல அதிகார வரம்பின் (சரத்து 131) கீழ் மத்திய-மாநில கூட்டாட்சி சர்ச்சைகளைத் தீர்க்கிறது.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
        {"A": "1, 2 and 3", "B": "1 and 2 only", "C": "2 and 3 only", "D": "1 and 3 only"},
        {"A": "1, 2 மற்றும் 3", "B": "1 மற்றும் 2 மட்டும்", "C": "2 மற்றும் 3 மட்டும்", "D": "1 மற்றும் 3 மட்டும்"},
        "A",
        "All three statements correctly summarize why the Supreme Court is called the 'Guardian and Protector of the Constitution' and 'Upholder of Fundamental Rights'.",
        "மூன்று கூற்றுகளும் உச்ச நீதிமன்றம் ஏன் 'அரசியலமைப்பின் பாதுகாவலன்' என்று அழைக்கப்படுகிறது என்பதைச் சரியாக விவரிக்கின்றன.",
        "Supreme Court balances federal power and protects individual rights.",
        "உச்ச நீதிமன்றம் கூட்டாட்சி அதிகாரத்தைச் சமநிலைப்படுத்தி தனிநபர் உரிமைகளைப் பாதுகாக்கிறது.",
        "Final interpreter of constitutional provisions.",
        "அரசியலமைப்பு விதிகளின் இறுதி விளக்கவுரையாளர்.",
        "Highest Judicial Court in India.",
        "இந்தியாவின் உயரிய நீதித்துறை மன்றம்."))

    # Q95
    b4.append(mk_q(95, "Medium", "Direct",
        "Under Article 146(3) of the Constitution, how are all administrative expenses of the Supreme Court, including salaries, allowances, and pensions of officers and servants, met?",
        "சரத்து 146(3)-ன் படி, அதிகாரிகள் மற்றும் ஊழியர்களின் சம்பளம், படிகள் மற்றும் ஓய்வூதியம் உள்ளிட்ட உச்ச நீதிமன்றத்தின் அனைத்து நிர்வாகச் செலவுகளும் எவ்வாறு வழங்கப்படுகின்றன?",
        {"A": "Charged upon the Consolidated Fund of India", "B": "Voted by Lok Sabha annually during Budget session", "C": "Paid out of Contingency Fund of India", "D": "Collected from court fee revenues directly"},
        {"A": "இந்தியாவின் தொகுப்பு நிதியில் (Consolidated Fund of India) பொறுப்பளிக்கப்பட்டவையாகும் (Charged)", "B": "பட்ஜெட் கூட்டத்தொடரில் மக்களவையால் ஆண்டுதோறும் வாக்களிக்கப்படும்", "C": "இந்திய அவசரகால நிதியிலிருந்து வழங்கப்படும்", "D": "நீதிமன்றக் கட்டண வருவாயிலிருந்து நேரடியாக வசூலிக்கப்படும்"},
        "A",
        "Article 146(3) explicitly declares: 'The administrative expenses of the Supreme Court, including all salaries, allowances and pensions payable to or in respect of the officers and servants of the Court, shall be CHARGED upon the Consolidated Fund of India.'",
        "சரத்து 146(3) வெளிப்படையாகக் கூறுகிறது: உச்ச நீதிமன்றத்தின் அதிகாரிகள் மற்றும் ஊழியர்களின் சம்பளம், படிகள் மற்றும் ஓய்வூதியம் உள்ளிட்ட நிர்வாகச் செலவுகள் இந்தியாவின் தொகுப்பு நிதியில் பொறுப்பளிக்கப்பட்டவையாகும் (Charged).",
        "Charged expenditure means non-votable by Parliament under Art 112(3)(d).",
        "பொறுப்பளிக்கப்பட்ட செலவு என்பது நாடாளுமன்ற வாக்கெடுப்பிற்கு உட்படாததாகும்.",
        "Insulates judicial administration from executive/legislative financial pressure.",
        "நிதி அழுத்தத்திலிருந்து நீதித்துறை நிர்வாகத்தைப் பாதுகாக்கிறது.",
        "Pensions of SC judges are also charged on Consolidated Fund of India.",
        "நீதிபதிகளின் ஓய்வூதியமும் தொகுப்பு நிதியில் பொறுப்பளிக்கப்பட்டுள்ளது."))

    # Q96
    b4.append(mk_q(96, "Hard", "Scenario",
        "If Parliament passes an ordinary law abolishing the Advisory Jurisdiction of the Supreme Court under Article 143, what will be the constitutional outcome?",
        "நாடாளுமன்றம் ஒரு சாதாரணச் சட்டம் இயற்றி சரத்து 143-ன் கீழான உச்ச நீதிமன்றத்தின் ஆலோசனை அதிகார வரம்பை ரத்து செய்தால், அதன் அரசியலமைப்பு முடிவு என்னவாகும்?",
        {"A": "The law will be declared unconstitutional and void by the Supreme Court because Parliament cannot alter constitutional provisions by an ordinary law", "B": "The law will take effect immediately", "C": "Advisory jurisdiction will transfer to High Courts", "D": "President will lose all advisory rights permanently"},
        {"A": "நாடாளுமன்றம் சாதாரணச் சட்டத்தால் அரசியலமைப்பு விதிகளை மாற்ற முடியாது என்பதால் அச்சட்டம் அரசியலமைப்புக்கு முரணானது எனக் கூறி உச்ச நீதிமன்றத்தால் ரத்து செய்யப்படும்", "B": "சட்டம் உடனடியாக அமலுக்கு வரும்", "C": "ஆலோசனை அதிகாரம் உயர் நீதிமன்றங்களுக்கு மாறும்", "D": "குடியரசுத் தலைவர் ஆலோசனை உரிமையை நிரந்தரமாக இழப்பார்"},
        "A",
        "Constitutional jurisdictions (Articles 124-147) can ONLY be altered by Constitutional Amendments under Article 368 (and subject to Basic Structure), NOT by ordinary parliamentary legislation.",
        "அரசியலமைப்பு அதிகார வரம்புகளைச் சாதாரண நாடாளுமன்றச் சட்டத்தால் மாற்ற முடியாது; சரத்து 368-ன் கீழான அரசியலமைப்புத் திருத்தம் மூலமே செய்ய முடியும் (அதுவும் அடிப்படை கட்டமைப்பிற்கு உட்பட்டு).",
        "Parliament can ENLARGE jurisdiction where permitted (e.g. Art 138/139), but CANNOT CURTAIL constitutional jurisdiction.",
        "நாடாளுமன்றம் அனுமதித்துள்ள இடங்களில் அதிகாரத்தை அதிகரிக்கலாம் (சரத்து 138); ஆனால் அரசியலமைப்பு அதிகாரத்தைக் குறைக்க முடியாது.",
        "Protects Supreme Court's constitutional role.",
        "உச்ச நீதிமன்ற அரசியலமைப்புப் பங்கைப் பாதுகாக்கிறது.",
        "Judicial review invalidates unconstitutional statutory laws.",
        "நீதித்துறை மறுஆய்வு செல்லாத சட்டங்களை ரத்து செய்கிறது."))

    # Q97
    b4.append(mk_q(97, "Medium", "Direct",
        "In Shankari Prasad (1951) and Sajjan Singh (1965), what stance did the Supreme Court take regarding Parliament's power to amend Fundamental Rights under Article 368?",
        "சங்கரி பிரசாத் (1951) மற்றும் சஜ்ஜன் சிங் (1965) வழக்குகளில், சரத்து 368-ன் கீழ் அடிப்படை உரிமைகளைத் திருத்துவதற்கான நாடாளுமன்ற அதிகாரம் குறித்து உச்ச நீதிமன்றம் என்ன நிலைப்பாட்டை எடுத்தது?",
        {"A": "Parliament has full power to amend any part of the Constitution including Fundamental Rights under Article 368", "B": "Fundamental Rights cannot be amended by Parliament under any circumstances", "C": "Parliament can amend Fundamental Rights only with 100% state approval", "D": "Constitutional amendments are subject to Article 13(2) as ordinary laws"},
        {"A": "சரத்து 368-ன் கீழ் அடிப்படை உரிமைகள் உட்பட அரசியலமைப்பின் எந்தப் பகுதியையும் திருத்த நாடாளுமன்றத்திற்கு முழு அதிகாரம் உண்டு", "B": "எந்தச் சூழ்நிலையிலும் அடிப்படை உரிமைகளை நாடாளுமன்றம் திருத்த முடியாது", "C": "100% மாநிலங்களின் ஒப்புதலுடன் மட்டுமே அடிப்படை உரிமைகளைத் திருத்த முடியும்", "D": "அரசியலமைப்புத் திருத்தங்கள் சரத்து 13(2)-ன் கீழ் சாதாரணச் சட்டங்களாகக் கருதப்படும்"},
        "A",
        "In Shankari Prasad (1951) and Sajjan Singh (1965), SC held that constitutional amendment under Art 368 is NOT a 'law' under Art 13(2), so Parliament can amend any Fundamental Right.",
        "சங்கரி பிரசாத் (1951) மற்றும் சஜ்ஜன் சிங் (1965) வழக்குகளில், சரத்து 368-ன் கீழான அரசியலமைப்புத் திருத்தம் என்பது சரத்து 13(2)-ன் கீழான 'சட்டம்' அல்ல; எனவே நாடாளுமன்றம் எந்தவொரு அடிப்படை உரிமையையும் திருத்தலாம் எனத் தீர்ப்பளித்தது.",
        "This view was later reversed by Golaknath (1967) and modified by Kesavananda Bharati (1973).",
        "இந்த நிலைப்பாடு பின்னர் கோலக்நாத் (1967) மற்றும் கேசவானந்த பாரதி (1973) வழக்குகளில் மாற்றப்பட்டது.",
        "Differentiated 'Constituent Power' from 'Ordinary Legislative Power'.",
        "அரசியலமைப்பு அதிகாரத்தை சாதாரண சட்ட அதிகாரத்திலிருந்து வேறுபடுத்தியது.",
        "Upheld 1st and 17th Constitutional Amendments.",
        "1வது மற்றும் 17வது திருத்தங்களை உறுதி செய்தது."))

    # Q98
    b4.append(mk_q(98, "Hard", "Direct",
        "Under Article 134(2) of the Constitution, who is authorized to confer on the Supreme Court further powers to entertain and hear appeals from any judgment, final order, or sentence in a criminal proceeding of a High Court?",
        "சரத்து 134(2)-ன் படி, உயர் நீதிமன்றக் குற்றவியல் வழக்குகளின் தீர்ப்புகளுக்கு எதிராக மேல்முறையீடுகளைப் பெற உச்ச நீதிமன்றத்திற்கு மேலும் கூடுதல் அதிகாரங்களை வழங்கும் அதிகாரம் யாருக்கு உள்ளது?",
        {"A": "The Parliament by Law", "B": "The President by Executive Order", "C": "The Bar Council of India", "D": "The Law Commission"},
        {"A": "நாடாளுமன்றத்திற்குச் சட்டம் இயற்றுவதன் மூலம்", "B": "குடியரசுத் தலைவருக்கு நிர்வாக உத்தரவு மூலம்", "C": "இந்திய வழக்கறிஞர்கள் परिषத்திற்கு", "D": "சட்ட ஆணையத்திற்கு"},
        "A",
        "Article 134(2) states: 'Parliament may by law confer on the Supreme Court any further powers to entertain and hear appeals from any judgment, final order or sentence in a criminal proceeding of a High Court in the territory of India subject to such conditions and limitations as may be specified in such law.'",
        "சரத்து 134(2)-ன் படி, உயர் நீதிமன்றக் குற்றவியல் தீர்ப்புகளுக்கு எதிரான மேல்முறையீடுகளைப் பெற உச்ச நீதிமன்றத்திற்குக் கூடுதல் அதிகாரங்களை நாடாளுமன்றம் சட்டத்தின் மூலம் வழங்கலாம்.",
        "Parliament passed the Supreme Court (Enlargement of Criminal Appellate Jurisdiction) Act, 1970 under Article 134(2).",
        "1970-ல் நாடாளுமன்றம் குற்றவியல் மேல்முறையீட்டு அதிகார விரிவாக்கச் சட்டத்தை சரத்து 134(2)-ன் கீழ் இயற்றியது.",
        "Allowed appeals where HC sentenced accused to 10+ years imprisonment.",
        "10 ஆண்டுகள் அல்லது அதற்கு மேற்பட்ட சிறைத் தண்டனை வழக்குகளுக்கு மேல்முறையீட்டு உரிமையை வழங்கியது.",
        "Parliament expands appellate jurisdiction.",
        "நாடாளுமன்றம் மேல்முறையீட்டு அதிகாரத்தை விரிவுபடுத்துகிறது."))

    # Q99
    b4.append(mk_q(99, "Hard", "Statement",
        "Consider the following statements regarding the Supreme Court of India as the Highest Court of Appeal:\n1. It replaced both the Federal Court of India and the Privy Council in London.\n2. Its decisions under Article 141 form binding judicial precedents for all courts in India.\n3. It has constitutional power to review its own judgments under Article 137.\nWhich of the statements given above are correct?",
        "இந்தியாவின் உயரிய மேல்முறையீட்டு நீதிமன்றமாக உச்ச நீதிமன்றம் செயல்படுவது பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. இது இந்தியக் கூட்டாட்சி நீதிமன்றம் மற்றும் லண்டன் பிரிவி கவுன்சில் ஆகிய இரண்டின் இடத்தையும் பிடித்தது.\n2. சரத்து 141-ன் கீழான இதன் தீர்ப்புகள் இந்தியாவின் அனைத்து நீதிமன்றங்களுக்கும் பிணைக்கும் முன்மாதிரிகளாக அமைகின்றன.\n3. சரத்து 137-ன் கீழ் தனது சொந்தத் தீர்ப்புகளை மறுஆய்வு செய்யும் அரசியலமைப்பு அதிகாரம் இதற்கு உண்டு.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
        {"A": "1, 2 and 3", "B": "1 and 2 only", "C": "2 and 3 only", "D": "1 and 3 only"},
        {"A": "1, 2 மற்றும் 3", "B": "1 மற்றும் 2 மட்டும்", "C": "2 மற்றும் 3 மட்டும்", "D": "1 மற்றும் 3 மட்டும்"},
        "A",
        "All three statements are correct. Supreme Court is the apex judicial forum in India, inheriting Privy Council appeals, laying down binding precedent under Art 141, and retaining power of review under Art 137.",
        "மூன்று கூற்றுகளும் சரியானவை. உச்ச நீதிமன்றம் இந்தியாவின் உயரிய நீதிமன்றமாகும்; பிரிவி கவுன்சில் அதிகாரத்தைப் பெற்றது, சரத்து 141 சட்டங்களை உருவாக்குகிறது, சரத்து 137 மறுஆய்வு அதிகாரத்தைக் கொண்டுள்ளது.",
        "Apex court in India's integrated single judicial hierarchy.",
        "இந்தியாவின் ஒருங்கிணைந்த ஒற்றை நீதித்துறை அமைப்பின் உச்ச நீதிமன்றம்.",
        "Guarantees rule of law and constitutional supremacy.",
        "சட்டத்தின் ஆட்சி மற்றும் அரசியலமைப்பு மேலாண்மையை உறுதி செய்கிறது.",
        "Protects individual rights and federal structure.",
        "தனிநபர் உரிமைகள் மற்றும் கூட்டாட்சியைப் பாதுகாக்கிறது."))

    # Q100
    b4.append(mk_q(100, "Hard", "Scenario",
        "A comprehensive review of the Constitutional position of the Supreme Court of India shows that it acts as:\n1. Federal Court under Article 131\n2. Protector of Fundamental Rights under Article 32\n3. Guardian of the Constitution through Judicial Review\n4. Advisory Body to the President under Article 143\nWhich combination best describes the multi-faceted role of the Supreme Court of India?",
        "இந்திய உச்ச நீதிமன்றத்தின் அரசியலமைப்பு நிலையை ஆராயும்போது, அது பின்வருவனவாகச் செயல்படுகிறது:\n1. சரத்து 131-ன் கீழ் கூட்டாட்சி நீதிமன்றம்\n2. சரத்து 32-ன் கீழ் அடிப்படை உரிமைகளின் பாதுகாப்பாளர்\n3. நீதித்துறை மறுஆய்வு மூலம் அரசியலமைப்பின் பாதுகாவலன்\n4. சரத்து 143-ன் கீழ் குடியரசுத் தலைவருக்கான ஆலோசனை அமைப்பு\nஉச்ச நீதிமன்றத்தின் பன்முகப் பங்கை விவரிக்கும் சரியான சேர்க்கை எது?",
        {"A": "1, 2, 3 and 4", "B": "1, 2 and 3 only", "C": "2, 3 and 4 only", "D": "1, 3 and 4 only"},
        {"A": "1, 2, 3 மற்றும் 4", "B": "1, 2 மற்றும் 3 மட்டும்", "C": "2, 3 மற்றும் 4 மட்டும்", "D": "1, 3 மற்றும் 4 மட்டும்"},
        "A",
        "The Supreme Court of India performs all four major roles: Federal Court (Art 131), Protector of Fundamental Rights (Art 32), Guardian of Constitution via Judicial Review, and Advisory Body to President (Art 143). It is the most powerful apex court in the democratic world.",
        "இந்திய உச்ச நீதிமன்றம் இந்த நான்கு முக்கியப் பங்கையும் ஆற்றுகிறது: கூட்டாட்சி நீதிமன்றம் (சரத்து 131), அடிப்படை உரிமைகளின் பாதுகாப்பாளர் (சரத்து 32), அரசியலமைப்பின் பாதுகாவலன் மற்றும் குடியரசுத் தலைவருக்கான ஆலோசனை அமைப்பு (சரத்து 143). இது உலகிலேயே மிக சக்திவாய்ந்த உச்ச நீதிமன்றங்களில் ஒன்றாகும்.",
        "Master synthesis question summarizing the entire Supreme Court Grand Test!",
        "உச்ச நீதிமன்ற கிராண்ட் டெஸ்ட் முழுமையையும் சுருக்கும் மாஸ்டர் வினா!",
        "All 4 roles are established by Part V of the Constitution.",
        "அனைத்து 4 பங்குகளும் பகுதி V-ல் நிறுவப்பட்டுள்ளன.",
        "Upholds Rule of Law across India.",
        "இந்தியா முழுவதும் சட்டத்தின் ஆட்சியை நிலைநிறுத்துகிறது."))

    return b4

if __name__ == "__main__":
    b4 = get_block4()
    print(f"Block 4 loaded with {len(b4)} questions.")
