# -*- coding: utf-8 -*-
"""
Supreme Court Grand Test Block 2 (Questions 26 to 50)
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

from gt_sc_block1 import mk_q

def get_block2():
    b2 = []

    # Q26
    b2.append(mk_q(26, "Medium", "Direct",
        "Under Article 140 of the Constitution, who is empowered to confer ancillary powers upon the Supreme Court to enable it to perform its constitutional functions effectively?",
        "அரசியலமைப்பின் சரத்து 140-ன் கீழ், உச்ச நீதிமன்றம் தனது பணிகளைத் திறம்பட ஆற்ற ஏதுவாக கூடுதல் (துணை) அதிகாரங்களை (Ancillary Powers) வழங்கும் அதிகாரம் யாருக்கு உள்ளது?",
        {"A": "The President of India by an Executive Order", "B": "The Parliament by Law", "C": "The Chief Justice of India by issuing court rules", "D": "The Law Commission of India"},
        {"A": "நிர்வாக உத்தரவு மூலம் இந்தியக் குடியரசுத் தலைவருக்கு", "B": "சட்டம் இயற்றுவதன் மூலம் நாடாளுமன்றத்திற்கு", "C": "நீதிமன்ற விதிகளை வெளியிடுவதன் மூலம் இந்தியத் தலைமை நீதிபதிக்கு", "D": "இந்திய சட்ட ஆணையத்திற்கு"},
        "B",
        "Article 140 states that Parliament may by law make provision for conferring upon the Supreme Court such supplemental powers, not inconsistent with any provisions of the Constitution, as may appear necessary.",
        "சரத்து 140-ன் படி, அரசியலமைப்பு விதிகளுக்கு முரண்படாத வகையில் உச்ச நீதிமன்றத்திற்குத் தேவையான துணை அதிகாரங்களைச் சட்டத்தின் மூலம் வழங்க நாடாளுமன்றத்திற்கு அதிகாரம் உண்டு.",
        "Candidates confuse President's rule-making approval (Art 145) with Parliament's ancillary power legislation (Art 140).",
        "சரத்து 145-ன் கீழான குடியரசுத் தலைவரின் ஒப்புதலையும், சரத்து 140-ன் கீழான நாடாளுமன்றத்தின் துணை அதிகாரச் சட்டத்தையும் குழப்பிக் கொள்ள வேண்டாம்.",
        "Ancillary powers help enforce decrees and orders effectively.",
        "துணை அதிகாரங்கள் நீதிமன்ற உத்தரவுகளைச் சீராக அமல்படுத்த உதவுகின்றன.",
        "Article 140 powers must not contradict any existing Constitutional provision.",
        "சரத்து 140 அதிகாரங்கள் அரசியலமைப்புக்கு முரண்படக் கூடாது."))

    # Q27
    b2.append(mk_q(27, "Hard", "Direct",
        "What does Article 144 of the Constitution explicitly mandate regarding civil and judicial authorities in the territory of India?",
        "இந்திய அரசியலமைப்பின் சரத்து 144 இந்தியாவின் எல்லைக்குள் உள்ள சிவில் மற்றும் நீதித்துறை அதிகாரிகளுக்கு என்ன வெளிப்படையான கட்டளையை அளிக்கிறது?",
        {"A": "All civil and judicial authorities shall act in aid of the Supreme Court", "B": "All High Courts shall submit annual performance reports to the Union Law Ministry", "C": "All subordinate courts must seek prior permission from Supreme Court before issuing injunctions", "D": "Civil authorities can ignore Supreme Court orders if State Legislature passes a resolution"},
        {"A": "அனைத்து சிவில் மற்றும் நீதித்துறை அதிகாரிகளும் உச்ச நீதிமன்றத்திற்கு உதவியாகச் செயல்பட வேண்டும்", "B": "அனைத்து உயர் நீதிமன்றங்களும் மத்திய சட்ட அமைச்சகத்திற்கு ஆண்டறிக்கை சமர்ப்பிக்க வேண்டும்", "C": "அனைத்துக் கீழ் நீதிமன்றங்களும் உத்தரவு பிறப்பிக்கும் முன் உச்ச நீதிமன்ற அனுமதி பெற வேண்டும்", "D": "மாநில சட்டமன்றம் தீர்மானம் நிறைவேற்றினால் சிவில் அதிகாரிகள் உச்ச நீதிமன்ற உத்தரவைப் புறக்கணிக்கலாம்"},
        "A",
        "Article 144 contains a mandatory constitutional directive: 'All authorities, civil and judicial, in the territory of India shall act in aid of the Supreme Court.'",
        "சரத்து 144 வெளிப்படையாகக் கட்டளையிடுகிறது: 'இந்திய நிலப்பரப்பில் உள்ள அனைத்து சிவில் மற்றும் நீதித்துறை அதிகாரிகளும் உச்ச நீதிமன்றத்திற்கு உதவியாகச் செயல்பட வேண்டும்.'",
        "Article 144 applies to executive officers, police, tax authorities, and all lower courts.",
        "சரத்து 144 என்பது அனைத்து நிர்வாக அதிகாரிகள், காவல் துறை, வருவாய் துறை மற்றும் கீழ் நீதிமன்றங்களுக்கும் பொருந்தும்.",
        "Refusal to act in aid of SC under Article 144 constitutes Contempt of Court.",
        "சரத்து 144-ன் கீழ் உதவ மறுப்பது நீதிமன்ற அவமதிப்பாகக் கருதப்படும்.",
        "Article 144 ensures execution of Supreme Court orders across the country.",
        "நாடெங்கிலும் உச்ச நீதிமன்ற உத்தரவுகள் அமலாவதை சரத்து 144 உறுதி செய்கிறது."))

    # Q28
    b2.append(mk_q(28, "Medium", "Statement",
        "Consider the following statements regarding the administration and staff of the Supreme Court under Article 146:\n1. Appointments of officers and servants of the Supreme Court are made by the Chief Justice of India or such other judge/officer as he may direct.\n2. The administrative expenses of the Supreme Court, including all salaries, allowances, and pensions payable to officers and servants, are charged upon the Consolidated Fund of India.\n3. The conditions of service of officers and servants are determined by rules made by CJI, but rules relating to salaries/pensions require the approval of the President.\nWhich of the statements given above are correct?",
        "சரத்து 146-ன் கீழ் உச்ச நீதிமன்றத்தின் நிர்வாகம் மற்றும் ஊழியர்கள் பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. உச்ச நீதிமன்றத்தின் அதிகாரிகள் மற்றும் ஊழியர்களின் நியமனங்கள் இந்தியத் தலைமை நீதிபதியால் அல்லது அவர் பணிக்கும் நீதிபதி/அதிகாரியால் செய்யப்படுகின்றன.\n2. அதிகாரிகள் மற்றும் ஊழியர்களின் சம்பளம், படிகள் மற்றும் ஓய்வூதியம் உள்ளிட்ட உச்ச நீதிமன்றத்தின் நிர்வாகச் செலவுகள் இந்தியாவின் தொகுப்பு நிதியில் பொறுப்பளிக்கப்பட்டவையாகும் (Charged).\n3. ஊழியர்களின் சேவை நிபந்தனைகள் CJI இயற்றும் விதிகளால் தீர்மானிக்கப்படுகின்றன, ஆனால் சம்பளம்/ஓய்வூதியம் தொடர்பான விதிகளுக்குக் குடியரசுத் தலைவரின் ஒப்புதல் தேவை.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
        {"A": "1, 2 and 3", "B": "1 and 2 only", "C": "2 and 3 only", "D": "1 and 3 only"},
        {"A": "1, 2 மற்றும் 3", "B": "1 மற்றும் 2 மட்டும்", "C": "2 மற்றும் 3 மட்டும்", "D": "1 மற்றும் 3 மட்டும்"},
        "A",
        "All three statements are correct under Article 146. 1. Appointments made by CJI. 2. Expenses charged on Consolidated Fund of India (non-votable). 3. CJI makes service rules, but rules regarding salary/allowances require President's approval.",
        "மூன்று கூற்றுகளும் சரத்து 146-ன் கீழ் சரியானவை. 1. CJI நியமனம் செய்கிறார். 2. செலவுகள் தொகுப்பு நிதியில் பொறுப்பளிக்கப்பட்டவை. 3. சம்பள விதிகளுக்கு குடியரசுத் தலைவரின் ஒப்புதல் தேவை.",
        "Notice that general service rules do not require approval, but rules involving money (salary/pensions) require President's consent.",
        "பொது சேவை விதிகளுக்கு ஒப்புதல் தேவையில்லை, ஆனால் பணம் சார்ந்த (சம்பளம்/ஓய்வூதியம்) விதிகளுக்கு குடியரசுத் தலைவர் ஒப்புதல் தேவை.",
        "Article 146 secures administrative independence of the judiciary from executive interference.",
        "சரத்து 146 நீதித்துறையின் நிர்வாகச் சுதந்திரத்தைப் பாதுகாக்கிறது.",
        "Administrative expenses are non-votable by Parliament under Art 112(3)(d).",
        "நிர்வாகச் செலவுகள் நாடாளுமன்ற வாக்கெடுப்பிற்கு உட்படாதவை."))

    # Q29
    b2.append(mk_q(29, "Hard", "Scenario",
        "Under Article 145(3) of the Constitution, what is the minimum number of Supreme Court Judges required to sit for deciding any case involving a substantial question of law as to the interpretation of the Constitution, or for hearing any reference under Article 143?",
        "சரத்து 145(3)-ன் கீழ், அரசியலமைப்பு விளக்கமளித்தல் தொடர்பான முக்கிய சட்டக் கேள்வி அடங்கிய வழக்கை விசாரிக்க அல்லது சரத்து 143 ஆலோசனை வழக்கை விசாரிக்க குறைந்தபட்சம் எத்தனை உச்ச நீதிமன்ற நீதிபதிகள் கொண்ட அமர்வு அமைய வேண்டும்?",
        {"A": "3 Judges", "B": "5 Judges", "C": "7 Judges", "D": "9 Judges"},
        {"A": "3 நீதிபதிகள்", "B": "5 நீதிபதிகள்", "C": "7 நீதிபதிகள்", "D": "9 நீதிபதிகள்"},
        "B",
        "Article 145(3) mandates that the minimum number of judges who are to sit for the purpose of deciding any case involving a substantial question of law as to the interpretation of the Constitution or for hearing an Article 143 reference shall be FIVE.",
        "சரத்து 145(3)-ன் படி அரசியலமைப்பு விளக்கமளித்தல் வழக்கு அல்லது சரத்து 143 ஆலோசனை வழக்கை விசாரிக்க அமர வேண்டிய குறைந்தபட்ச நீதிபதிகளின் எண்ணிக்கை ஐந்து (5) ஆகும்.",
        "Such a bench of 5 or more judges is constitutionally designated as a 'Constitution Bench'.",
        "ஐந்து அல்லது அதற்கு மேற்பட்ட நீதிபதிகள் கொண்ட அமர்வு 'அரசியலமைப்பு அமர்வு' (Constitution Bench) என்று அழைக்கப்படுகிறது.",
        "Ordinary benches: Division Bench (2 judges), Full Bench (3 judges), Constitution Bench (5+ judges).",
        "சாதாரண அமர்வுகள்: இரட்டை நீதிபதி அமர்வு (2), முழு அமர்வு (3), அரசியலமைப்பு அமர்வு (5+).",
        "Largest Constitution Bench: Kesavananda Bharati case (13 judges).",
        "மிகப்பெரிய அரசியலமைப்பு அமர்வு: கேசவானந்த பாரதி வழக்கு (13 நீதிபதிகள்)."))

    # Q30
    b2.append(mk_q(30, "Medium", "Direct",
        "Under Article 124(7) of the Constitution, what restriction is placed on a person who has held office as a judge of the Supreme Court after retirement or demission of office?",
        "சரத்து 124(7)-ன் படி, உச்ச நீதிமன்ற நீதிபதியாகப் பணியாற்றி ஓய்வுபெற்ற ஒருவர் மீது என்ன அரசியலமைப்புத் தடை விதிக்கப்பட்டுள்ளது?",
        {"A": "He shall not plead or act in any court or before any authority within the territory of India", "B": "He can practice only in High Courts, but not in Subordinate Courts", "C": "He can practice in Supreme Court after a cooling-off period of 2 years", "D": "He cannot accept any government commission appointment"},
        {"A": "அவர் இந்தியாவின் எல்லைக்குள் உள்ள எந்தவொரு நீதிமன்றத்திலும் அல்லது அதிகார அமைப்பின் முன்பும் வழக்கறிஞராகப் பணியாற்றவோ அல்லது வழக்காடவோ முடியாது", "B": "அவர் உயர் நீதிமன்றங்களில் மட்டுமே பணியாற்றலாம், கீழ் நீதிமன்றங்களில் முடியாது", "C": "2 ஆண்டுகள் இடைவெளிக்குப் பிறகு அவர் உச்ச நீதிமன்றத்தில் வழக்காடலாம்", "D": "அவர் எந்தவொரு அரசு ஆணையப் பொறுப்பையும் ஏற்க முடியாது"},
        "A",
        "Article 124(7) explicitly lays down a TOTAL BAN: 'No person who has held office as a Judge of the Supreme Court shall plead or act in any court or before any authority within the territory of India.'",
        "சரத்து 124(7) முழுமையான தடையை விதிக்கிறது: 'உச்ச நீதிமன்ற நீதிபதியாகப் பணியாற்றிய நபர் இந்தியாவின் எந்தவொரு நீதிமன்றத்திலும் அல்லது அதிகார அமைப்பின் முன்பும் வழக்கறிஞராகப் பணியாற்றவோ அல்லது வழக்காடவோ முடியாது.'",
        "Compare with High Court Judge (Art 220): Retired HC judge CAN practice in Supreme Court and other High Courts where he was not a permanent judge.",
        "உயர் நீதிமன்ற நீதிபதியுடன் ஒப்பிடுக (சரத்து 220): ஓய்வுபெற்ற உயர் நீதிமன்ற நீதிபதி உச்ச நீதிமன்றத்திலும், தான் நிரந்தர நீதிபதியாக இல்லாத பிற உயர் நீதிமன்றங்களிலும் வழக்காடலாம்.",
        "SC judge ban is total across ALL Indian courts.",
        "உச்ச நீதிமன்ற நீதிபதிக்கு இந்தியாவின் அனைத்து நீதிமன்றங்களிலும் முழுமையான தடை உண்டு.",
        "However, retired SC judges can be appointed to tribunals, commissions, or as Ad Hoc/Retired judges under Art 128.",
        "இருப்பினும், ஓய்வுபெற்ற நீதிபதிகள் தீர்ப்பாயங்கள் மற்றும் ஆணையங்களின் தலைவர்களாக நியமிக்கப்படலாம்."))

    # Q31
    b2.append(mk_q(31, "Hard", "Statement",
        "Consider the following statements regarding the 99th Constitutional Amendment Act, 2014 and the National Judicial Appointments Commission (NJAC):",
        "99வது அரசியலமைப்புத் திருத்தச் சட்டம், 2014 மற்றும் தேசிய நீதிபதிகள் நியமன ஆணையம் (NJAC) பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. NJAC replaced the Collegium System and proposed a 6-member body headed by the CJI.\n2. In Supreme Court Advocates-on-Record Association v. Union of India (2015) (Fourth Judges Case), a 5-judge bench struck down the 99th Amendment and NJAC Act as unconstitutional.\n3. The Supreme Court held that executive involvement in NJAC compromised the Independence of Judiciary, which is a Basic Feature of the Constitution.\nWhich of the statements given above are correct?",
        {"A": "1, 2 and 3", "B": "1 and 2 only", "C": "2 and 3 only", "D": "1 and 3 only"},
        {"A": "1, 2 மற்றும் 3", "B": "1 மற்றும் 2 மட்டும்", "C": "2 மற்றும் 3 மட்டும்", "D": "1 மற்றும் 3 மட்டும்"},
        "A",
        "All three statements are correct. The 99th CAA (2014) created NJAC (6 members: CJI + 2 senior SC judges + Law Minister + 2 eminent persons). In 2015, SC struck it down by 4:1 majority (4th Judges Case) to protect Judicial Independence as a Basic Feature.",
        "மூன்று கூற்றுகளும் சரியானவை. 99வது திருத்தம் (2014) NJAC-ஐ உருவாக்கியது (6 உறுப்பினர்கள்). 2015-ல் 4வது நீதிபதிகள் வழக்கில் 4:1 பெரும்பான்மையில் உச்ச நீதிமன்றம் அதை ரத்து செய்து கொலீஜியத்தை மீண்டும் மீட்டெடுத்தது.",
        "Justice J. Chelameswar was the lone dissenting judge who upheld the NJAC Act.",
        "நீதிபதி ஜே. செல்லமேஸ்வர் NJAC-க்கு ஆதரவாக மாறுபட்ட தீர்ப்பளித்த ஒரே நீதிபதியாவார்.",
        "NJAC composition: CJI (Chairman) + 2 SC Judges + Law Minister + 2 Eminent Persons (nominated by CJI, PM, Leader of Opposition).",
        "NJAC அமைப்பு: CJI + 2 மூத்த நீதிபதிகள் + சட்ட அமைச்சர் + 2 முக்கிய நபர்கள்.",
        "Fourth Judges Case restored the Collegium System (CJI + 4).",
        "4வது நீதிபதிகள் வழக்கு கொலீஜியம் முறையை மீண்டும் நிறுவியது."))

    # Q32
    b2.append(mk_q(32, "Medium", "Direct",
        "Under the Contempt of Courts Act, 1971, what is the limitation period for initiating proceedings for contempt of court from the date on which the contempt is alleged to have been committed?",
        "நீதிமன்ற அவமதிப்புச் சட்டம், 1971-ன் படி, அவமதிப்பு இழைக்கப்பட்டதாகக் கூறப்படும் தேதியிலிருந்து எந்தக் கால வரம்பிற்குள் (Limitation Period) அவமதிப்பு நடவடிக்கையைத் தொடங்க வேண்டும்?",
        {"A": "6 months", "B": "1 year", "C": "2 years", "D": "3 years"},
        {"A": "6 மாதங்கள்", "B": "1 ஆண்டு", "C": "2 ஆண்டுகள்", "D": "3 ஆண்டுகள்"},
        "B",
        "Under Section 20 of the Contempt of Courts Act, 1971, no court shall initiate any proceedings for contempt, either on its own motion or otherwise, after the expiry of a period of ONE YEAR from the date on which the contempt is alleged to have been committed.",
        "நீதிமன்ற அவமதிப்புச் சட்டம் 1971-ன் பிரிவு 20-ன் படி, அவமதிப்பு நிகழ்ந்த தேதியிலிருந்து 1 ஆண்டு முடிந்த பிறகு எந்தவொரு நீதிமன்றமும் அவமதிப்பு நடவடிக்கையைத் தொடங்க முடியாது.",
        "Candidates assume no limitation period exists for Supreme Court. While Art 129 gives constitutional power, statutory limitation under 1971 Act is 1 year.",
        "கால வரம்பு இல்லை என தேர்வர்கள் தவறாகக் கருதுகின்றனர். 1971 சட்டத்தின் படி கால வரம்பு 1 ஆண்டாகும்.",
        "Civil Contempt: Willful disobedience of court order/judgment.",
        "சிவில் அவமதிப்பு: நீதிமன்ற உத்தரவை வேண்டுமென்றே மீறுவது.",
        "Criminal Contempt: Scandalising court, prejudicing judicial proceeding, or obstructing administration of justice.",
        "குற்றவியல் அவமதிப்பு: நீதிமன்றத்தை அவதூறு செய்வது அல்லது நீதி நிர்வாகத்தைத் தடுப்பது."))

    # Q33
    b2.append(mk_q(33, "Hard", "Scenario",
        "The Supreme Court directs the Government to frame policy guidelines for night shelters for homeless persons and monitors its implementation. Which concept of judicial role does this best illustrate?",
        "உச்ச நீதிமன்றம் அரசுக்கு வீடற்றவர்களுக்கான இரவு தங்குமிடக் கொள்கை வழிகாட்டுதல்களை உருவாக்குமாறு உத்தரவிட்டு, அதை அமல்படுத்துவதைக் கண்காணிக்கிறது. இது நீதித்துறையின் எந்தக் கோட்பாட்டைச் சிறப்பாக விளக்குகிறது?",
        {"A": "Judicial Restraint", "B": "Judicial Activism", "C": "Judicial Overreach / Judicial Tyranny", "D": "Judicial Immunity"},
        {"A": "நீதித்துறை கட்டுப்பாடு (Judicial Restraint)", "B": "நீதித்துறை செயல்முனைவு (Judicial Activism)", "C": "நீதித்துறை எல்லை மீறல் (Judicial Overreach)", "D": "நீதித்துறை விலக்குரிமை (Judicial Immunity)"},
        "B",
        "Judicial Activism refers to proactive judicial role in enforcing constitutional rights, directing executive policy action to protect vulnerable sections when executive fails.",
        "நிர்வாகம் செயல்படத் தவறும்போது, பாதிக்கப்படக்கூடியப் பிரிவினரைப் பாதுகாக்க நீதித்துறை முன்னின்று வழிகாட்டுதல்களை வழங்குவது 'நீதித்துறை செயல்முனைவு' (Judicial Activism) ஆகும்.",
        "Judicial Activism = Proactive protection of rights within constitutional limits. Judicial Overreach = Usurping legislative/executive function completely.",
        "செயல்முனைவு (Activism) என்பது உரிமைகளைப் பாதுகாத்தல்; எல்லை மீறல் (Overreach) என்பது சட்டமன்ற/நிர்வாகப் பணிகளைத் தானே எடுத்துச் செய்வது.",
        "Judicial Activism was initiated by Justices V.R. Krishna Iyer and P.N. Bhagwati.",
        "நீதித்துறை செயல்முனைவு நீதிபதிகள் கிருஷ்ணய்யர் மற்றும் பகவதியால் தொடங்கப்பட்டது.",
        "Key cases: Bandhua Mukti Morcha, Vishaka guidelines, Clean Ganga directives.",
        "விசாக்கா வழிகாட்டுதல்கள் மற்றும் பந்துவா முக்தி மோர்ச்சா போன்றவை இதன் எடுத்துக்காட்டுகளாகும்."))

    # Q34
    b3 = [] # placeholder

    b2.append(mk_q(34, "Medium", "Direct",
        "What is the crucial procedural distinction between the Writ of Prohibition and the Writ of Certiorari?",
        "தடைகேட்கும் பேராணை (Prohibition) மற்றும் நெறிமுறைப்படுத்தும் பேராணை (Certiorari) ஆகியவற்றுக்கு இடையேயான முக்கிய நடைமுறை வேறுபாடு என்ன?",
        {"A": "Prohibition is issued when proceedings are pending to prevent excess of jurisdiction, whereas Certiorari is issued after an order has been passed to quash it", "B": "Prohibition is issued against executive authorities, while Certiorari is issued against legislative bodies", "C": "Certiorari can be issued against private bodies, whereas Prohibition cannot", "D": "Prohibition is available only in Supreme Court, while Certiorari is available only in High Court"},
        {"A": "வழக்கு நிலுவையில் இருக்கும்போதே அதிகார வரம்பு மீறலைத் தடுக்க Prohibition வெளியிடப்படுகிறது; ஆனால் உத்தரவு பிறப்பிக்கப்பட்ட பிறகு அதை ரத்து செய்ய Certiorari வெளியிடப்படுகிறது", "B": "நிர்வாக அதிகாரிகளுக்கு எதிராக Prohibition வெளியிடப்படுகிறது, சட்டமன்றத்திற்கு எதிராக Certiorari வெளியிடப்படுகிறது", "C": "தனியார் அமைப்புகளுக்கு எதிராக Certiorari வெளியிடலாம், Prohibition வெளியிட முடியாது", "D": "உச்ச நீதிமன்றத்தில் மட்டுமே Prohibition கிடைக்கும், உயர் நீதிமன்றத்தில் மட்டுமே Certiorari கிடைக்கும்"},
        "A",
        "Prohibition is PREVENTIVE (issued while proceedings are pending to stop lower court from exceeding jurisdiction). Certiorari is both PREVENTIVE and CURATIVE (issued after order is passed to quash illegal decision).",
        "தடைகேட்கும் பேராணை (Prohibition) என்பது வழக்கு நடக்கும்போதே தடுக்கும் நோக்கமுடையது (Preventive). நெறிமுறைப்படுத்தும் பேராணை (Certiorari) என்பது உத்தரவு வந்த பிறகு அதை ரத்து செய்யும் நிவாரண நோக்கமுடையது (Curative).",
        "Remember phrase: 'Prevention is better than cure' -> Prohibition is preventive, Certiorari is curative.",
        "நினைவில் கொள்க: 'தடுப்பது குணப்படுத்துவதை விட மேலானது' -> Prohibition தடுப்பது, Certiorari குணப்படுத்துவது.",
        "Both Prohibition and Certiorari are issued ONLY against judicial and quasi-judicial bodies (Certiorari expanded to administrative bodies in 1991).",
        "இரண்டு பேராணைகளும் நீதி மற்றும் நீதி சார்ந்த அமைப்புகளுக்கு எதிராகவே வெளியிடப்படுகின்றன.",
        "Neither writ is available against private individuals or legislative bodies.",
        "தனியார் நபர்கள் அல்லது சட்டமன்றங்களுக்கு எதிராக இவை வெளியாகாது."))

    # Q35
    b2.append(mk_q(35, "Hard", "Direct",
        "Which of the following writs can be petitioned by ANY public-spirited citizen, even if he is NOT the personally aggrieved party (Exception to Locus Standi)?",
        "பாதிக்கப்பட்ட நபர் மட்டுமே வழக்குத் தொடர வேண்டும் என்ற பாரம்பரிய விதியைத் (Locus Standi) தளர்த்தி, எந்தவொரு பொதுநலன் விரும்பும் குடிமகனும் மனு தாக்கல் செய்யக்கூடிய பேராணை எது?",
        {"A": "Mandamus", "B": "Certiorari", "C": "Quo-Warranto", "D": "Prohibition"},
        {"A": "கட்டளையுறுத்தும் பேராணை (Mandamus)", "B": "நெறிமுறைப்படுத்தும் பேராணை (Certiorari)", "C": "தகுதிகாண் பேராணை (Quo-Warranto)", "D": "தடைகேட்கும் பேராணை (Prohibition)"},
        "C",
        "The writ of Quo-Warranto can be sought by any person, and not necessarily by the aggrieved party. It challenges the legality of a person's claim to a public office created by statute.",
        "தகுதிகாண் பேராணையை (Quo-Warranto) பாதிக்கப்பட்ட நபர் மட்டுமே கேட்க வேண்டியதில்லை; எந்தவொரு நபரும் கேட்கலாம். இது சட்டப்பூர்வ பொதுப் பதவியில் ஒருவர் அமர்வதைக் கேள்வி கேட்கிறது.",
        "Candidates assume Mandamus has relaxed locus standi. For Mandamus, applicant must have a legal right.",
        "Mandamus பேராணைக்கு தளர்வு உண்டு எனத் தவறாகக் கருதுகின்றனர். Mandamus-க்கு சட்டப்பூர்வ உரிமை தேவை.",
        "Quo-Warranto prevents illegal usurpation of a public office.",
        "பொதுப் பதவியை சட்டவிரோதமாகக் கைப்பற்றுவதை தகுதிகாண் பேராணை தடுக்கிறது.",
        "Office must be public and created by Constitution or Statute (not private office).",
        "பதவியானது அரசியலமைப்பு அல்லது சட்டத்தால் உருவாக்கப்பட்ட பொதுப் பதவியாக இருக்க வேண்டும்."))

    # Q36
    b2.append(mk_q(36, "Medium", "Direct",
        "The Writ of Mandamus ('We Command') CANNOT be issued against which of the following authorities?",
        "கட்டளையுறுத்தும் பேராணை (Mandamus) பின்வரும் எந்த அதிகாரிகளுக்கு எதிராக வெளியிடப்பட முடியாது?",
        {"A": "President of India and State Governors", "B": "Public Corporations performing statutory duties", "C": "Subordinate Courts failing to exercise jurisdiction", "D": "Government Departments violating statutory duties"},
        {"A": "இந்தியக் குடியரசுத் தலைவர் மற்றும் மாநில ஆளுநர்கள்", "B": "சட்டப்பூர்வ கடமைகளை ஆற்றும் பொது நிறுவனங்கள்", "C": "அதிகார வரம்பைப் பயன்படுத்தத் தவறும் கீழ் நீதிமன்றங்கள்", "D": "சட்டப்பூர்வ கடமைகளை மீறும் அரசுத் துறைகள்"},
        "A",
        "Mandamus CANNOT be issued against: 1. President of India or State Governors (Art 361 immunity), 2. Private individuals/bodies, 3. Chief Justice of High Court acting in judicial capacity, 4. Non-statutory departmental instructions.",
        "Mandamus பின்வருபவர்களுக்கு எதிராகப் பிறப்பிக்க முடியாது: 1. குடியரசுத் தலைவர் அல்லது மாநில ஆளுநர்கள் (சரத்து 361 விலக்கு), 2. தனிநபர்கள், 3. நீதித்துறைப் பணியாற்றும் உயர் நீதிமன்ற தலைமை நீதிபதி, 4. சட்டப்பூர்வமற்ற துறைசார் அறிவுறுத்தல்கள்.",
        "Candidates miss the constitutional immunity granted to President and Governor under Article 361.",
        "சரத்து 361-ன் கீழ் குடியரசுத் தலைவர் மற்றும் ஆளுநருக்கு உள்ள விலக்குரிமையை தேர்வர்கள் நினைவில் கொள்ள வேண்டும்.",
        "Mandamus is issued to compel performance of a MANDATORY public duty.",
        "கட்டாயப் பொதுக் கடமையை ஆற்ற வைப்பதே Mandamus-ன் நோக்கமாகும்.",
        "It cannot be issued to enforce a discretionary duty or private contract.",
        "விருப்பக் கடமை அல்லது தனியார் ஒப்பந்தத்தை அமல்படுத்த இதை வெளியிட முடியாது."))

    # Q37
    b2.append(mk_q(37, "Medium", "Direct",
        "Which of the following Constitutional Writs can be issued against BOTH public authorities and private individuals?",
        "பின்வரும் அரசியலமைப்புப் பேராணைகளில் எது பொது அதிகார அமைப்புகள் மற்றும் தனிநபர்கள் ஆகிய இருவருக்கு எதிராகவும் வெளியிடப்பட முடியும்?",
        {"A": "Mandamus", "B": "Habeas Corpus", "C": "Certiorari", "D": "Prohibition"},
        {"A": "கட்டளையுறுத்தும் பேராணை (Mandamus)", "B": "ஆட்கொணர்வுப் பேராணை (Habeas Corpus)", "C": "நெறிமுறைப்படுத்தும் பேராணை (Certiorari)", "D": "தடைகேட்கும் பேராணை (Prohibition)"},
        "B",
        "The writ of Habeas Corpus ('To have the body of') can be issued against BOTH public authorities and private individuals who illegally detain a person.",
        "ஆட்கொணர்வுப் பேராணை (Habeas Corpus) என்பது சட்டவிரோதமாகக் காவலில் வைக்கும் பொது அதிகாரிகள் மற்றும் தனிநபர்கள் ஆகிய இருவருக்கு எதிராகவும் வெளியிடப்படலாம்.",
        "All other writs (Mandamus, Certiorari, Prohibition, Quo-Warranto) are generally restricted to public authorities / courts.",
        "மற்ற அனைத்துப் பேராணைகளும் பொது அதிகாரிகள் / நீதிமன்றங்களுக்கு மட்டுமே பொருந்தும்.",
        "Habeas Corpus is a bulwark of individual liberty against arbitrary detention.",
        "தன்னிச்சையான காவலுக்கு எதிரான தனிநபர் சுதந்திரத்தின் கவசமாக Habeas Corpus திகழ்கிறது.",
        "It cannot be issued if detention is lawful or by a competent court.",
        "காவல் சட்டப்பூர்வமானது என்றால் Habeas Corpus வெளியாகாது."))

    # Q38
    b2.append(mk_q(38, "Hard", "Direct",
        "What does Article 135 of the Constitution deal with?",
        "இந்திய அரசியலமைப்பின் சரத்து 135 எதைப் பற்றிக் கூறுகிறது?",
        {"A": "Jurisdiction and powers of the Federal Court under existing law to be exercisable by the Supreme Court", "B": "Power of Parliament to modify Fundamental Rights during Emergency", "C": "Salaries of High Court Judges transferred to Supreme Court", "D": "Rules regarding appointment of Supreme Court registrars"},
        {"A": "நிலவும் சட்டத்தின் கீழ் கூட்டாட்சி நீதிமன்றத்திற்கு இருந்த அதிகார வரம்பு மற்றும் அதிகாரங்களை உச்ச நீதிமன்றம் செயல்படுத்துதல்", "B": "அவசரநிலையின் போது அடிப்படை உரிமைகளை மாற்றியமைக்க நாடாளுமன்றத்திற்கு உள்ள அதிகாரம்", "C": "உச்ச நீதிமன்றத்திற்கு மாற்றப்படும் உயர் நீதிமன்ற நீதிபதிகளின் சம்பளம்", "D": "உச்ச நீதிமன்றப் பதிவாளர்கள் நியமனம் பற்றிய விதிகள்"},
        "A",
        "Article 135 states that until Parliament by law otherwise provides, the Supreme Court shall also have jurisdiction and powers with respect to any matter to which the provisions of Article 133 or Article 134 do not apply, if jurisdiction and powers in relation to that matter were exercisable by the Federal Court immediately before the commencement of this Constitution.",
        "சரத்து 135-ன் படி, அரசியலமைப்பு தொடங்குவதற்கு முன் கூட்டாட்சி நீதிமன்றத்திற்கு இருந்த, சரத்து 133/134-ல் வராத அதிகார வரம்புகளை உச்ச நீதிமன்றம் தொடர்ந்து செயல்படுத்த அதிகாரம் பெற்றுள்ளது.",
        "Article 135 is a bridge provision connecting the 1935 Federal Court powers with the post-1950 Supreme Court.",
        "சரத்து 135 என்பது 1935 கூட்டாட்சி நீதிமன்ற அதிகாரங்களை உச்ச நீதிமன்றத்திற்கு மாற்றிய இணைப்பு விதியாகும்.",
        "It ensures no legal vacuum occurred upon commencement of the Constitution on Jan 26, 1950.",
        "1950 ஜனவரி 26-ல் சட்டம் காலியாகாமல் இருக்க இது உதவியது.",
        "Applies to matters not covered under Articles 133 and 134.",
        "சரத்து 133 மற்றும் 134-ல் வராத விவகாரங்களுக்கு இது பொருந்தும்."))

    # Q39
    b2.append(mk_q(39, "Medium", "Direct",
        "Under Article 138 of the Constitution, how can the jurisdiction and powers of the Supreme Court be enlarged with respect to any of the matters in the Union List or any other matter?",
        "சரத்து 138-ன் கீழ், மத்தியப் பட்டியலிலுள்ள விவகாரங்கள் அல்லது பிற விவகாரங்கள் தொடர்பாக உச்ச நீதிமன்றத்தின் அதிகார வரம்பை எவ்வாறு விரிவாக்கம் செய்யலாம்?",
        {"A": "By President issuing an Ordinance", "B": "By Parliament by Law", "C": "By Chief Justice of India with Cabinet approval", "D": "By Constitutional Amendment requiring 2/3rd majority of states"},
        {"A": "குடியரசுத் தலைவர் அவசரச் சட்டம் பிறப்பிப்பதன் மூலம்", "B": "நாடாளுமன்றம் சட்டம் இயற்றுவதன் மூலம்", "C": "அமைச்சரவை ஒப்புதலுடன் இந்தியத் தலைமை நீதிபதியால்", "D": "2/3 பங்கு மாநிலங்களின் ஒப்புதலுடன் அரசியலமைப்புத் திருத்தம் மூலம்"},
        "B",
        "Article 138(1) states that the Supreme Court shall have such further jurisdiction and powers with respect to any of the matters in the Union List as Parliament may by law confer.",
        "சரத்து 138(1)-ன் படி, மத்தியப் பட்டியலில் உள்ள எந்தவொரு விவகாரம் தொடர்பாகவும் உச்ச நீதிமன்றத்திற்கு கூடுதல் அதிகார வரம்பை நாடாளுமன்றம் சட்டத்தின் மூலம் வழங்கலாம்.",
        "Notice that Parliament can ENLARGE Supreme Court jurisdiction, but CANNOT curtail or reduce its constitutional jurisdiction.",
        "நாடாளுமன்றம் உச்ச நீதிமன்ற அதிகார வரம்பை அதிகரிக்கலாம்; ஆனால் அரசியலமைப்பு அதிகாரத்தைக் குறைக்க முடியாது.",
        "Article 138(2) allows enlargement over any matter if Union Government and State Government agree by special agreement.",
        "சரத்து 138(2) மத்திய-மாநில அரசுகளின் ஒப்பந்தம் மூலமும் அதிகாரத்தை விரிவுபடுத்த அனுமதிக்கிறது.",
        "Enlargement of SC jurisdiction requires simple parliamentary law.",
        "அதிகார விரிவாக்கத்திற்குச் சாதாரண நாடாளுமன்றச் சட்டமே போதுமானது."))

    # Q40
    b2.append(mk_q(40, "Hard", "Direct",
        "Under Article 139 of the Constitution, who is authorized to confer on the Supreme Court the power to issue directions, orders, or writs for purposes OTHER THAN the enforcement of Fundamental Rights?",
        "அரசியலமைப்பின் சரத்து 139-ன் கீழ், அடிப்படை உரிமைகளை அமல்படுத்துவது தவிர பிற நோக்கங்களுக்காகப் பேராணைகளை (Writs) வெளியிடும் அதிகாரத்தை உச்ச நீதிமன்றத்திற்கு வழங்கும் அதிகாரம் யாருக்கு உள்ளது?",
        {"A": "The President of India", "B": "The Parliament by Law", "C": "The Bar Council of India", "D": "The High Courts by unanimous resolution"},
        {"A": "இந்தியக் குடியரசுத் தலைவருக்கு", "B": "நாடாளுமன்றத்திற்குச் சட்டம் இயற்றுவதன் மூலம்", "C": "இந்திய வழக்கறிஞர்கள் परिषத்திற்கு (Bar Council)", "D": "உயர் நீதிமன்றங்களின் ஒருமனதான தீர்மானத்தின் மூலம்"},
        "B",
        "Article 139 provides that Parliament may by law confer on the Supreme Court power to issue directions, orders or writs for any purposes OTHER THAN those mentioned in Article 32(2).",
        "சரத்து 139-ன் படி, சரத்து 32(2)-ல் கூறப்பட்டுள்ள அடிப்படை உரிமைகள் தவிர பிற நோக்கங்களுக்காகப் பேராணைகளை வெளியிடும் அதிகாரத்தை நாடாளுமன்றம் சட்டத்தின் மூலம் உச்ச நீதிமன்றத்திற்கு வழங்கலாம்.",
        "Crucial Trap: Under Art 32, SC has writ power ONLY for Fundamental Rights. Under Art 226, HC has writ power for FR and other legal rights. Art 139 allows Parliament to give SC writ power for other rights too!",
        "சரத்து 32-ன் கீழ் உச்ச நீதிமன்ற பேராணை அதிகாரம் அடிப்படை உரிமைகளுக்கு மட்டுமே உண்டு. சரத்து 139 மூலம் நாடாளுமன்றம் மற்ற உரிமைகளுக்கும் பேராணை அதிகாரத்தை வழங்க முடியும்.",
        "Article 139 bridges the gap between Supreme Court and High Court writ scopes.",
        "சரத்து 139 உச்ச நீதிமன்றத்தின் பேராணை வரம்பை விரிவாக்க உதவுகிறது.",
        "It requires a Parliamentary legislation.",
        "இதற்கு நாடாளுமன்றச் சட்டம் தேவை."))

    # Q41
    b2.append(mk_q(41, "Medium", "Direct",
        "What does Article 147 of the Constitution specify regarding the 'Interpretation' of constitutional provisions?",
        "இந்திய அரசியலமைப்பின் சரத்து 147 அரசியலமைப்பு விதிகளை 'விளக்கமளித்தல்' (Interpretation) பற்றி என்ன குறிப்பிடுகிறது?",
        {"A": "It clarifies that references to interpretation of the Constitution include references to interpretation of the Government of India Act 1935 and Indian Independence Act 1947", "B": "It specifies that only the President can interpret constitutional provisions", "C": "It states that Tamil and Hindi texts override English text in interpretation", "D": "It mandates that constitutional interpretation must be reviewed by NITI Aayog"},
        {"A": "அரசியலமைப்பு விளக்கக் குறிப்புகளில் 1935 இந்திய அரசாங்கச் சட்டம் மற்றும் 1947 இந்திய சுதந்திரச் சட்டம் ஆகியவற்றின் விளக்கங்களும் அடங்கும் என்பதைத் தெளிவுபடுத்துகிறது", "B": "குடியரசுத் தலைவர் மட்டுமே அரசியலமைப்பு விதிகளுக்கு விளக்கமளிக்க முடியும் எனக் குறிப்பிடுகிறது", "C": "தமிழ் மற்றும் இந்தி உரைகள் ஆங்கில உரையை விட மேலானவை எனக் கூறுகிறது", "D": "அரசியலமைப்பு விளக்கம் நிதி ஆயோக்கால் மறுஆய்வு செய்யப்பட வேண்டும் எனக் கட்டாயப்படுத்துகிறது"},
        "A",
        "Article 147 is the interpretation clause for Chapter IV of Part V. It clarifies that references to substantial questions of law as to interpretation of Constitution include interpretation of GOI Act 1935, Indian Independence Act 1947, or any Order in Council made thereunder.",
        "சரத்து 147 என்பது பகுதி V அத்தியாயம் IV-ன் விளக்க விதியாகும். அரசியலமைப்பு விளக்கம் என்பதன் கீழ் 1935 இந்திய அரசாங்கச் சட்டம் மற்றும் 1947 இந்திய சுதந்திரச் சட்டம் ஆகியவற்றின் விளக்கங்களும் அடங்கும் என்பதை அது தெளிவுபடுத்துகிறது.",
        "Article 147 completes the interpretation provisions spanning Articles 145 and 146.",
        "சரத்து 147 பகுதி V அத்தியாயம் IV-ன் இறுதி விதியாகும்.",
        "Chapter IV of Part V ends with Article 147 (Articles 124 to 147).",
        "பகுதி V அத்தியாயம் IV சரத்து 147 உடன் முடிவடைகிறது (சரத்துகள் 124 முதல் 147 வரை).",
        "It links historic constitutional enactments to present constitutional interpretation.",
        "வரலாற்றுச் சட்டங்களை தற்போதைய அரசியலமைப்பு விளக்கத்துடன் இணைக்கிறது."))

    # Q42
    b2.append(mk_q(42, "Medium", "Direct",
        "To whom must a judge of the Supreme Court of India address his resignation letter in writing under Article 124(2)(a)?",
        "சரத்து 124(2)(a)-ன் படி, இந்திய உச்ச நீதிமன்ற நீதிபதி தனது ராஜினாமா கடிதத்தை யாருக்கு முகவரியிட்டு எழுத வேண்டும்?",
        {"A": "The Chief Justice of India", "B": "The President of India", "C": "The Speaker of Lok Sabha", "D": "The Union Minister of Law and Justice"},
        {"A": "இந்தியத் தலைமை நீதிபதிக்கு", "B": "இந்தியக் குடியரசுத் தலைவருக்கு", "C": "மக்களவை சபாநாயகருக்கு", "D": "மத்திய சட்ட அமைச்சருக்கு"},
        "B",
        "Under proviso (a) to Article 124(2), a Judge of the Supreme Court may, by writing under his hand addressed to the PRESIDENT, resign his office.",
        "சரத்து 124(2)(a)-ன் படி, உச்ச நீதிமன்ற நீதிபதி குடியரசுத் தலைவருக்குத் தன் கையொப்பமிட்ட கடிதம் மூலம் ராஜினாமா செய்ய வேண்டும்.",
        "Candidates assume a judge resigns to the Chief Justice of India. Since President appoints judges, resignation is addressed to President.",
        "நீதிபதி தலைமை நீதிபதியிடம் ராஜினாமா செய்வார் என தேர்வர்கள் தவறாக நினைக்கின்றனர். நியமிக்கும் அதிகாரியான குடியரசுத் தலைவரிடமே ராஜினாமா அளிக்கப்பட வேண்டும்.",
        "Resignation takes effect immediately upon receipt or specified date.",
        "ராஜினாமா உடனடியாக அமலுக்கு வரும்.",
        "Applies to both CJI and other SC judges.",
        "தலைமை நீதிபதி மற்றும் பிற நீதிபதிகள் இருவருக்குமே இது பொருந்தும்."))

    # Q43
    b2.append(mk_q(43, "Medium", "Direct",
        "Before entering upon his office, every person appointed to be a judge of the Supreme Court must make and subscribe an Oath or Affirmation under Article 124(6). According to which Schedule of the Constitution is this oath prescribed?",
        "பதவியேற்கும் முன், உச்ச நீதிமன்ற நீதிபதியாக நியமிக்கப்படும் ஒவ்வொரு நபரும் சரத்து 124(6)-ன் கீழ் உறுதிமொழி அல்லது ప్రమాணம் எடுத்துக்கொள்ள வேண்டும். இந்த உறுதிமொழி அரசியலமைப்பின் எந்த அட்டவணையில் குறிப்பிடப்பட்டுள்ளது?",
        {"A": "Second Schedule", "B": "Third Schedule", "C": "Fourth Schedule", "D": "Ninth Schedule"},
        {"A": "இரண்டாவது அட்டவணை", "B": "மூன்றாவது அட்டவணை", "C": "நான்காவது அட்டவணை", "D": "ஒன்பதாவது அட்டவணை"},
        "B",
        "Article 124(6) specifies that SC judges must take oath according to the form set out for the purpose in the THIRD SCHEDULE before the President or some person appointed by him.",
        "சரத்து 124(6)-ன் படி உச்ச நீதிமன்ற நீதிபதிகள் மூன்றாவது அட்டவணையில் (Third Schedule) குறிப்பிடப்பட்டுள்ள படிவத்தின் படி குடியரசுத் தலைவர் அல்லது அவரால் நியமிக்கப்பட்ட நபர் முன்னிலையில் பதவியேற்க வேண்டும்.",
        "2nd Schedule = Salaries and Allowances; 3rd Schedule = Oaths and Affirmations. Do not swap 2nd and 3rd Schedules!",
        "2வது அட்டவணை = சம்பளம் மற்றும் படிகள்; 3வது அட்டவணை = பதவியேற்பு உறுதிமொழிகள். இரண்டையும் குழப்ப வேண்டாம்!",
        "Form of oath includes upholding Sovereignty and Integrity of India and Constitution.",
        "உறுதிமொழியில் இந்தியாவின் இறையாண்மை, ஒருமைப்பாடு மற்றும் அரசியலமைப்பைப் பாதுகாப்பேன் என உரைக்கப்படும்.",
        "President or his designated representative administers the oath.",
        "குடியரசுத் தலைவர் அல்லது அவரால் நியமிக்கப்பட்ட பிரதிநிதி பதவியேற்பு உறுதிமொழி அளிக்கிறார்."))

    # Q44
    b2.append(mk_q(44, "Hard", "Scenario",
        "Under Article 124(2A) inserted by the 15th Constitutional Amendment Act, 1963, how is any question regarding the age of a Supreme Court judge determined?",
        "15வது அரசியலமைப்புத் திருத்தச் சட்டம் 1963 மூலம் சேர்க்கப்பட்ட சரத்து 124(2A)-ன் படி, உச்ச நீதிமன்ற நீதிபதியின் வயது பற்றிய ஏதேனும் கேள்வி எழுந்தால் அது எவ்வாறு தீர்மானிக்கப்படுகிறது?",
        {"A": "By the Chief Justice of India in his sole discretion", "B": "By such authority and in such manner as Parliament may by law provide", "C": "By a Medical Board constituted by Union Ministry of Health", "D": "By the Election Commission of India"},
        {"A": "இந்தியத் தலைமை நீதிபதியின் தனிப்பட்ட விருப்ப அதிகாரத்தால்", "B": "நாடாளுமன்றம் சட்டத்தால் வழங்கும் அதிகாரம் மற்றும் வழிமுறையின் மூலம்", "C": "மத்திய சுகாதார அமைச்சகத்தால் அமைக்கப்படும் மருத்துவக் குழுவால்", "D": "இந்தியத் தேர்தல் ஆணையத்தால்"},
        "B",
        "Article 124(2A) states: 'The age of a Judge of the Supreme Court shall be determined by such authority and in such manner as Parliament may by law provide.'",
        "சரத்து 124(2A)-ன் படி: 'உச்ச நீதிமன்ற நீதிபதியின் வயது நாடாளுமன்றம் சட்டத்தின் மூலம் வழங்கும் அதிகாரம் மற்றும் வழிமுறையின் படி தீர்மானிக்கப்படும்.'",
        "Compare with High Court Judge age determination (Art 217(3)): Age of HC judge is decided by the PRESIDENT after consultation with CJI, and President's decision is final.",
        "உயர் நீதிமன்ற நீதிபதியின் வயதுத் தீர்மானத்துடன் ஒப்பிடுக (சரத்து 217(3)): உயர் நீதிமன்ற நீதிபதியின் வயதை CJI கலந்தாலோசனைக்குப் பின் குடியரசுத் தலைவர் தீர்மானிப்பார். உச்ச நீதிமன்ற நீதிபதி வயதை நாடாளுமன்றச் சட்டம் தீர்மானிக்கும்.",
        "Notice the fundamental contrast between Art 124(2A) [Parliament law] and Art 217(3) [President consultation with CJI].",
        "சரத்து 124(2A) [நாடாளுமன்றச் சட்டம்] மற்றும் சரத்து 217(3) [குடியரசுத் தலைவர் + CJI] ஆகியவற்றுக்கு இடையேயான வேறுபாட்டை கவனிக்கவும்.",
        "Retirement age for SC judge is 65 years.",
        "உச்ச நீதிமன்ற நீதிபதியின் ஓய்வுபெறும் வயது 65."))

    # Q45
    b2.append(mk_q(45, "Medium", "Direct",
        "Under Article 145 of the Constitution, who makes rules for regulating the practice and procedure of the Supreme Court, and whose approval is mandatory?",
        "சரத்து 145-ன் படி, உச்ச நீதிமன்ற நடைமுறை மற்றும் விவாதங்களை ஒழுங்குபடுத்தும் விதிகளை உருவாக்குபவர் யார் மற்றும் யாருடைய ஒப்புதல் கட்டாயமாகும்?",
        {"A": "Chief Justice of India makes rules independently without approval", "B": "Supreme Court makes rules with the approval of the President", "C": "Union Law Minister makes rules with approval of Parliament", "D": "Law Commission makes rules with approval of Law Minister"},
        {"A": "எந்த ஒப்புதலும் இன்றி இந்தியத் தலைமை நீதிபதி சுயாதீனமாக விதிகளை உருவாக்குகிறார்", "B": "குடியரசுத் தலைவரின் ஒப்புதலுடன் உச்ச நீதிமன்றம் விதிகளை உருவாக்குகிறது", "C": "நாடாளுமன்ற ஒப்புதலுடன் மத்திய சட்ட அமைச்சர் விதிகளை உருவாக்குகிறார்", "D": "சட்ட அமைச்சரின் ஒப்புதலுடன் சட்ட ஆணையம் விதிகளை உருவாக்குகிறது"},
        "B",
        "Article 145(1) states that subject to the provisions of any law made by Parliament, the Supreme Court may from time to time, with the approval of the PRESIDENT, make rules for regulating generally the practice and procedure of the Court.",
        "சரத்து 145(1)-ன் படி, நாடாளுமன்ற சட்டத்திற்கு உட்பட்டு, குடியரசுத் தலைவரின் ஒப்புதலுடன் உச்ச நீதிமன்றம் தனது நடைமுறை மற்றும் விவாதங்களை ஒழுங்குபடுத்தும் விதிகளை உருவாக்குகிறது.",
        "SC makes rules subject to Parliamentary laws and previous approval of President.",
        "விதிகளை உச்ச நீதிமன்றமே உருவாக்குகிறது; ஆனால் குடியரசுத் தலைவர் ஒப்புதல் கட்டாயமாகும்.",
        "Rules cover stays, bail, appeals, fee structure, and bench configurations.",
        "ஜாமீன், மேல்முறையீடு, கட்டணம் மற்றும் அமர்வுகள் பற்றிய விதிகள் இதில் அடங்கும்.",
        "Article 145 rules are subordinate to Parliamentary legislation.",
        "நாடாளுமன்றச் சட்டங்களுக்கு உட்பட்டது."))

    # Q46
    b2.append(mk_q(46, "Medium", "Direct",
        "In 1973, Justice A.N. Ray was appointed as Chief Justice of India superseding three senior judges. Which three senior judges of the Supreme Court were superseded?",
        "1973-ல் நீதிபதி ஏ.என். ரே மூன்று மூத்த நீதிபதிகளை மீறி இந்தியத் தலைமை நீதிபதியாக நியமிக்கப்பட்டார். மீறப்பட்ட அந்த மூன்று மூத்த நீதிபதிகள் யார்?",
        {"A": "Justices J.M. Shelat, K.S. Hegde, and A.N. Grover", "B": "Justices H.R. Khanna, M.H. Beg, and V.R. Krishna Iyer", "C": "Justices P.N. Bhagwati, Y.V. Chandrachud, and D.A. Desai", "D": "Justices S.M. Sikri, R.S. Sarkaria, and O. Chinnappa Reddy"},
        {"A": "நீதிபதிகள் ஜே.எம். ஷெலாட், கே.எஸ். ஹெக்டே மற்றும் ஏ.என். குரோவர்", "B": "நீதிபதிகள் எச்.ஆர். கண்ணா, எம்.எச். பேக் மற்றும் வி.ஆர். கிருஷ்ணய்யர்", "C": "நீதிபதிகள் பி.என். பகவதி, ஒய்.வி. சந்திரசூட் மற்றும் டி.ஏ. தேசாய்", "D": "நீதிபதிகள் எஸ்.எம். சிக்ரி, ஆர்.எஸ். சர்க்காரியா மற்றும் ஓ. சின்னப்ப ரெட்டி"},
        "A",
        "In April 1973, after the Kesavananda Bharati judgment, the Union Government departed from the convention of appointing the senior-most judge as CJI and appointed Justice A.N. Ray, superseding Justices J.M. Shelat, K.S. Hegde, and A.N. Grover.",
        "ஏப்ரல் 1973-ல் கேசவானந்த பாரதி தீர்ப்பிற்குப் பிறகு, மூத்த நீதிபதியைத் தலைமை நீதிபதியாக்கும் மரபை மீறி, நீதிபதிகள் ஜே.எம். ஷெலாட், கே.எஸ். ஹெக்டே மற்றும் ஏ.என். குரோவர் ஆகிய மூவரை மீறி ஏ.என். ரே தலைமை நீதிபதியாக நியமிக்கப்பட்டார்.",
        "Second supersession occurred in January 1977 when Justice M.U. Beg superseded Justice H.R. Khanna (famous ADM Jabalpur dissenter).",
        "இரண்டாவது மீறல் ஜனவரி 1977-ல் நடைபெற்றது (நீதிபதி எச்.ஆர். கண்ணாவை மீறி எம்.யு. பேக் நியமனம்).",
        "Seniority convention was restored and formalized by 2nd Judges Case (1993).",
        "1993-ல் 2வது நீதிபதிகள் வழக்கு மூப்பு மரபை மீண்டும் கட்டாயமாக்கியது.",
        "Superseded judges resigned in protest in 1973.",
        "பாதிக்கப்பட்ட மூன்று நீதிபதிகளும் எதிர்ப்ப தெரிவித்து ராஜினாமா செய்தனர்."))

    # Q47
    b2.append(mk_q(47, "Hard", "Scenario",
        "In S.R. Bommai v. Union of India (1994), what major constitutional principle regarding Article 356 (President's Rule) and Judicial Review was laid down by the Supreme Court?",
        "எஸ்.ஆர். பொம்மை எதிர் இந்திய யூனியன் (1994) வழக்கில், சரத்து 356 (குடியரசுத் தலைவர் ஆட்சி) மற்றும் நீதித்துறை மறுஆய்வு குறித்து உச்ச நீதிமன்றம் வழங்கிய முக்கிய தீர்ப்பு என்ன?",
        {"A": "Proclamation of President's Rule under Article 356 is subject to Judicial Review, and Secularism is a Basic Feature of the Constitution", "B": "President's Rule is beyond judicial review under any circumstances", "C": "President can dissolve State Legislative Assembly before Parliamentary approval", "D": "State Assemblies can never be dissolved by Central Government"},
        {"A": "சரத்து 356-ன் கீழ் குடியரசுத் தலைவர் ஆட்சி பிரகடனம் நீதித்துறை மறுஆய்வுக்கு உட்பட்டது, மேலும் மதச்சார்பின்மை என்பது அரசியலமைப்பின் அடிப்படை அம்சமாகும்", "B": "குடியரசுத் தலைவர் ஆட்சி எந்தச் சூழ்நிலையிலும் நீதித்துறை மறுஆய்வுக்கு அப்பாற்பட்டது", "C": "நாடாளுமன்ற ஒப்புதலுக்கு முன்பே குடியரசுத் தலைவர் மாநில சட்டமன்றத்தைக் கலைக்கலாம்", "D": "மாநில சட்டமன்றங்களை மத்திய அரசு ஒருபோதும் கலைக்க முடியாது"},
        "A",
        "In S.R. Bommai (1994), a 9-judge bench held that: 1. Proclamation under Art 356 is subject to judicial review. 2. Secularism is part of Basic Structure. 3. Assembly should not be dissolved until Parliament approves the Proclamation.",
        "எஸ்.ஆர். பொம்மை வழக்கில் (1994) 9 நீதிபதிகள் கொண்ட அமர்வு: 1. சரத்து 356 நீதித்துறை மறுஆய்வுக்கு உட்பட்டது. 2. மதச்சார்பின்மை அடிப்படை கட்டமைப்பு. 3. நாடாளுமன்ற ஒப்புதல் பெறும் வரை சட்டமன்றத்தைக் கலைக்கக் கூடாது எனத் தீர்ப்பளித்தது.",
        "Floor Test in Legislative Assembly is the only ultimate test for proving majority of a government.",
        "சட்டமன்றத்தில் நடைபெறும் பெரும்பான்மை சோதனையே (Floor Test) ஒரு அரசின் பெரும்பான்மையை நிரூபிக்கும் ஒரே வழியாகும்.",
        "S.R. Bommai judgment drastically reduced arbitrary misuse of Article 356.",
        "சரத்து 356 துஷ்பிரயோகத்தை பொம்மை தீர்ப்பு வெகுவாகக் குறைத்தது.",
        "Secularism was affirmed as an essential feature of constitutional governance.",
        "மதச்சார்பின்மை முக்கிய அம்சமாக உறுதி செய்யப்பட்டது."))

    # Q48
    b2.append(mk_q(48, "Medium", "Direct",
        "In Maneka Gandhi v. Union of India (1978), how did the Supreme Court re-interpret 'Procedure Established by Law' under Article 21?",
        "மேனகா காந்தி எதிர் இந்திய யூனியன் (1978) வழக்கில், சரத்து 21-ல் உள்ள 'சட்டத்தால் அமைக்கப்பட்ட நடைமுறை' (Procedure Established by Law) என்பதை உச்ச நீதிமன்றம் எவ்வாறு மறுவிளக்கம் செய்தது?",
        {"A": "Procedure established by law must be just, fair, and reasonable, effectively introducing American 'Due Process of Law'", "B": "Procedure established by law requires only literal compliance with statutory provisions passed by Parliament", "C": "Article 21 applies only to administrative actions, not legislative enactments", "D": "Fundamental Rights can be suspended by executive orders without law"},
        {"A": "சட்டத்தால் அமைக்கப்பட்ட நடைமுறை என்பது நீதியானதாகவும், நேர்மையானதாகவும், நியாயமானதாகவும் (Just, Fair and Reasonable) இருக்க வேண்டும்; இதன் மூலம் அமெரிக்க 'Due Process of Law' தத்துவம் அறிமுகப்படுத்தப்பட்டது", "B": "நாடாளுமன்றம் இயற்றிய சட்டத்தின் எழுத்துவடிவத்தை மட்டும் பின்பற்றினால் போதுமானது", "C": "சரத்து 21 நிர்வாக நடவடிக்கைகளுக்கு மட்டுமே பொருந்தும், சட்டங்களுக்கு அல்ல", "D": "சட்டமின்றி நிர்வாக உத்தரவு மூலம் அடிப்படை உரிமைகளை நிறுத்தி வைக்கலாம்"},
        "A",
        "In Maneka Gandhi (1978), SC overruled Gopalan case (1950) and held that procedure under Art 21 must not be arbitrary, oppressive, or fanciful; it must be JUST, FAIR, AND REASONABLE, infusing the American concept of 'Due Process of Law'.",
        "மேனகா காந்தி (1978) வழக்கில், கோபாலன் (1950) தீர்ப்பை மாற்றி, சரத்து 21-ன் கீழான நடைமுறை தன்னிச்சையானதாக இருக்கக் கூடாது; அது நீதியானதாகவும், நேர்மையானதாகவும், நியாயமானதாகவும் இருக்க வேண்டும் எனக் கூறி 'Due Process of Law' தத்துவத்தை இணைத்தது.",
        "Maneka Gandhi case established Inter-relationship between Articles 14, 19, and 21 (Golden Triangle of Constitution).",
        "சரத்துகள் 14, 19 மற்றும் 21 ஆகிய மூன்றையும் இணைத்து 'தங்க முக்கோணம்' (Golden Triangle) கோட்பாட்டை உருவாக்கியது.",
        "Expanded Right to Life to include Right to Live with Human Dignity, Right to Travel Abroad, Clean Environment, Privacy.",
        "வாழும் உரிமையை மனிதக் கண்ணியத்துடன் வாழும் உரிமையாக விரிவுபடுத்தியது.",
        "AK Gopalan case (1950) had taken a narrow textual view; Maneka Gandhi broadened it.",
        "கோபாலன் வழக்கில் இருந்த குறுகிய பார்வையை மேனகா காந்தி வழக்கு விரிவுபடுத்தியது."))

    # Q49
    b2.append(mk_q(49, "Hard", "Scenario",
        "In I.R. Coelho v. State of Tamil Nadu (2007), what unanimous ruling did the 9-judge Constitution Bench lay down regarding laws placed in the Ninth Schedule of the Constitution?",
        "ஐ.ஆர். கோயல்ஹோ எதிர் தமிழ்நாடு அரசு (2007) வழக்கில், அரசியலமைப்பின் ஒன்பதாவது அட்டவணையில் சேர்க்கப்படும் சட்டங்கள் குறித்து 9 நீதிபதிகள் கொண்ட அமர்வு வழங்கிய ஒருமனதான தீர்ப்பு என்ன?",
        {"A": "Laws placed in the Ninth Schedule AFTER April 24, 1973 are open to judicial review if they violate the Basic Structure of the Constitution", "B": "All laws placed in Ninth Schedule since 1951 are completely immune from judicial review", "C": "Ninth Schedule was declared unconstitutional and struck down", "D": "Only State land reform laws can be placed in Ninth Schedule"},
        {"A": "ஏப்ரல் 24, 1973-க்குக்குப் பிறகு ஒன்பதாவது அட்டவணையில் சேர்க்கப்பட்ட சட்டங்கள் அடிப்படை கட்டமைப்பை மீறினால் நீதித்துறை மறுஆய்வுக்கு உட்பட்டவை", "B": "1951 முதல் ஒன்பதாவது அட்டவணையில் உள்ள அனைத்துச் சட்டங்களுக்கும் நீதித்துறை மறுஆய்விலிருந்து முழு விலக்கு உண்டு", "C": "ஒன்பதாவது அட்டவணை அரசியலமைப்புக்கு முரணானது என ரத்து செய்யப்பட்டது", "D": "மாநில நிலசீர்திருத்தச் சட்டங்கள் மட்டுமே ஒன்பதாவது அட்டவணையில் சேர்க்கப்பட முடியும்"},
        "A",
        "In I.R. Coelho (2007), SC held that any law inserted in the Ninth Schedule AFTER April 24, 1973 (date of Kesavananda Bharati judgment) does not enjoy immunity and is subject to judicial review if it infringes Part III rights violating the Basic Structure.",
        "ஐ.ஆர். கோயல்ஹோ (2007) வழக்கில், ஏப்ரல் 24, 1973 (கேசவானந்த பாரதி தீர்ப்பு நாள்)க்குப் பிறகு 9வது அட்டவணையில் சேர்க்கப்படும் எந்தவொரு சட்டமும் அடிப்படை கட்டமைப்பை மீறினால் நீதித்துறை மறுஆய்வுக்கு உட்பட்டது எனத் தீர்ப்பளித்தது.",
        "Cut-off date for Ninth Schedule immunity check: April 24, 1973.",
        "9வது அட்டவணை சோதனைக்கான கடைசி எல்லை நாள்: ஏப்ரல் 24, 1973.",
        "Ninth Schedule was added by the 1st Constitutional Amendment Act, 1951 (Art 31B).",
        "9வது அட்டவணை 1வது திருத்தச் சட்டம் 1951-ன் மூலம் சேர்க்கப்பட்டது (சரத்து 31B).",
        "Prevents Parliament from creating 'safe havens' for unconstitutional laws.",
        "அரசியலமைப்புக்கு முரணான சட்டங்களைப் பாதுகாக்கும் புகலிடமாக 9வது அட்டவணை மாறுவதை இது தடுத்தது."))

    # Q50
    b2.append(mk_q(50, "Hard", "Direct",
        "In Indira Nehru Gandhi v. Raj Narain (1975), the Supreme Court struck down Clause 4 of Article 329A inserted by the 39th Constitutional Amendment Act, 1975. Which new feature was added to the 'Basic Structure Doctrine' in this case?",
        "இந்திரா நேரு காந்தி எதிர் ராஜ் நாரைன் (1975) வழக்கில், 39வது திருத்தத்தால் சேர்க்கப்பட்ட சரத்து 329A(4)-ஐ உச்ச நீதிமன்றம் ரத்து செய்தது. இவ்வழக்கில் 'அடிப்படை கட்டமைப்பு கோட்பாட்டில்' சேர்க்கப்பட்ட புதிய அம்சம் எது?",
        {"A": "Free and Fair Elections and Judicial Review", "B": "Panchayati Raj and Local Self Government", "C": "Uniform Civil Code", "D": "Right to Property"},
        {"A": "சுதந்திரமான மற்றும் நேர்மையான தேர்தல்கள் மற்றும் நீதித்துறை மறுஆய்வு", "B": "பஞ்சாயத்து ராஜ் மற்றும் உள்ளாட்சி அரசு", "C": "பொது சிவில் சட்டம்", "D": "சொத்து உரிமை"},
        "A",
        "In Indira Gandhi v. Raj Narain (1975), SC applied the Basic Structure doctrine for the FIRST TIME to invalidate a Constitutional Amendment (39th CAA Clause 4 which placed PM's election beyond judicial review). SC added 'Free and Fair Elections' and 'Judicial Review' to Basic Structure.",
        "இந்திரா காந்தி வழக்கில் (1975) முதன்முதலாக அரசியலமைப்புத் திருத்தத்தை ரத்து செய்ய அடிப்படை கட்டமைப்பு கோட்பாடு பயன்படுத்தப்பட்டது. 'சுதந்திரமான மற்றும் நேர்மையான தேர்தல்கள்' மற்றும் 'நீதித்துறை மறுஆய்வு' ஆகியவை அடிப்படை கட்டமைப்பாகச் சேர்க்கப்பட்டன.",
        "First case where a Constitutional Amendment was actually invalidated using Basic Structure doctrine.",
        "அடிப்படை கட்டமைப்பு கோட்பாட்டைப் பயன்படுத்தி அரசியலமைப்புத் திருத்தம் ரத்து செய்யப்பட்ட முதல் வழக்கு இதுவே.",
        "39th Amendment (1975) tried to place election of PM and Speaker beyond court challenge.",
        "39வது திருத்தம் பிரதமர் மற்றும் சபாநாயகர் தேர்தலை நீதிமன்ற சோதனைக்கு அப்பாற்படுத்த முயன்றது.",
        "Reaffirmed that democracy requires free and fair elections.",
        "ஜனநாயகத்திற்கு சுதந்திரமான தேர்தல்கள் அவசியம் என்பதை மீண்டும் உறுதிப்படுத்தியது."))

    return b2

if __name__ == "__main__":
    b2 = get_block2()
    print(f"Block 2 loaded with {len(b2)} questions.")
