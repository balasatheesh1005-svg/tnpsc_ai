# -*- coding: utf-8 -*-
"""
Grand Test Batch 3: SCH_GT_051 to SCH_GT_075
Covers:
- Seventh Schedule (051-058)
- Eighth Schedule (059-068)
- Ninth Schedule (069-075)
"""
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.insert(0, os.path.dirname(__file__))

from sch_mcq_helper import make_sch_q

def get_batch3():
    qs = []

    # GT051
    qs.append(make_sch_q(
        "SCH_GT_051", "Easy", "Conceptual", "Seventh Schedule",
        "In which List of the Seventh Schedule is 'Public health and sanitation; hospitals and dispensaries' placed?",
        "ஏழாவது அட்டவணையின் எந்தப் பட்டியலில் 'பொது சுகாதாரம் மற்றும் துப்புரவு; மருத்துவமனைகள் மற்றும் மருந்தகங்கள்' வைக்கப்பட்டுள்ளன?",
        "List II (State List) – Entry 6", "பட்டியல் II (மாநிலப் பட்டியல்) – பதிவு 6",
        "List I (Union List) – Entry 12", "பட்டியல் I (மத்திய பட்டியல்) – பதிவு 12",
        "List III (Concurrent List) – Entry 20", "பட்டியல் III (பொதுப் பட்டியல்) – பதிவு 20",
        "Residuary Powers under Article 248", "சரத்து 248-ன் கீழான எஞ்சிய அதிகாரங்கள்",
        "A",
        "Entry 6 of List II (State List) covers 'Public health and sanitation; hospitals and dispensaries'.",
        "பட்டியல் II-ன் (மாநிலப் பட்டியல்) பதிவு 6 'பொது சுகாதாரம் மற்றும் துப்புரவு; மருத்துவமனைகள் மற்றும் மருந்தகங்கள்' ஆகியவற்றைக் குறிப்பிடுகிறது.",
        "Correct. Public health is Entry 6 of the State List.", "சரியானது. பொது சுகாதாரம் மாநிலப் பட்டியலின் பதிவு 6 ஆகும்.",
        "Incorrect. Union List covers port quarantine, not local public health.", "தவறானது. மத்திய பட்டியல் துறைமுக தனிமைப்படுத்தலைக் கையாள்கிறது.",
        "Incorrect. Concurrent List covers economic planning and social security.", "தவறானது. பொதுப் பட்டியல் பொருளாதாரத் திட்டமிடலைக் கையாள்கிறது.",
        "Incorrect. It is an enumerated entry, not residuary.", "தவறானது. இது பட்டியலிடப்பட்ட பதிவு, எஞ்சிய அதிகாரம் அல்ல.",
        "Public Health: State List Entry 6. Hence, healthcare delivery is primarily a State responsibility.",
        "பொது சுகாதாரம்: மாநிலப் பட்டியல் பதிவு 6. எனவே, சுகாதாரப் பராமரிப்பு முதன்மையாக மாநிலத்தின் பொறுப்பாகும்."
    ))

    # GT052
    qs.append(make_sch_q(
        "SCH_GT_052", "Medium", "Conceptual", "Seventh Schedule",
        "Which Entry in the Union List (List I) of the Seventh Schedule provides for the audit of the accounts of the Union and of the States?",
        "ஏழாவது அட்டவணையின் மத்திய பட்டியலில் (பட்டியல் I) எந்தப் பதிவு மத்திய மற்றும் மாநிலங்களின் கணக்குகளைத் தணிக்கை செய்வதை வழங்குகிறது?",
        "Entry 76 of List I", "பட்டியல் I-ன் பதிவு 76",
        "Entry 45 of List I", "பட்டியல் I-ன் பதிவு 45",
        "Entry 60 of List I", "பட்டியல் I-ன் பதிவு 60",
        "Entry 97 of List I", "பட்டியல் I-ன் பதிவு 97",
        "A",
        "Entry 76 of List I covers: 'Audit of the accounts of the Union and of the States.' This provides the legislative backing for the duties and powers of the CAG under Article 149.",
        "பட்டியல் I-ன் பதிவு 76 குறிப்பிடுகிறது: 'மத்திய மற்றும் மாநிலங்களின் கணக்குகளைத் தணிக்கை செய்தல்.' இது சரத்து 149-ன் கீழ் சிஏஜியின் அதிகாரங்களுக்கு சட்டப்பூர்வ ஆதரவை வழங்குகிறது.",
        "Correct. Entry 76 List I covers audit of Union and State accounts.", "சரியானது. பட்டியல் I பதிவு 76 மத்திய மற்றும் மாநிலக் கணக்குகள் தணிக்கையைக் குறிக்கிறது.",
        "Incorrect. Entry 45 covers Banking.", "தவறானது. பதிவு 45 வங்கித் தொழிலைக் குறிக்கிறது.",
        "Incorrect. Entry 60 covers Sanctioning of cinematograph films.", "தவறானது. பதிவு 60 திரைப்படங்களுக்கு அனுமதி அளிப்பதைக் குறிக்கிறது.",
        "Incorrect. Entry 97 is the Residuary entry.", "தவறானது. பதிவு 97 என்பது எஞ்சிய அதிகாரப் பதிவு.",
        "Entry 76 List I: Explains why a single central authority (CAG) audits both Centre and States.",
        "பட்டியல் I பதிவு 76: ஏன் ஒரே மத்திய அதிகாரி (சிஏஜி) மத்திய மற்றும் மாநிலங்கள் இரண்டையும் தணிக்கை செய்கிறார் என்பதை விளக்குகிறது."
    ))

    # GT053
    qs.append(make_sch_q(
        "SCH_GT_053", "Medium", "Conceptual", "Seventh Schedule",
        "In which List of the Seventh Schedule is 'Bankruptcy and insolvency' enumerated?",
        "ஏழாவது அட்டவணையின் எந்தப் பட்டியலில் 'திவால் மற்றும் நொடிப்பு நிலை' (Bankruptcy and insolvency) பட்டியலிடப்பட்டுள்ளது?",
        "List III (Concurrent List) – Entry 9", "பட்டியல் III (பொதுப் பட்டியல்) – பதிவு 9",
        "List I (Union List) – Entry 43", "பட்டியல் I (மத்திய பட்டியல்) – பதிவு 43",
        "List II (State List) – Entry 30", "பட்டியல் II (மாநிலப் பட்டியல்) – பதிவு 30",
        "Residuary Powers under Article 248", "சரத்து 248-ன் கீழான எஞ்சிய அதிகாரங்கள்",
        "A",
        "Entry 9 of List III (Concurrent List) specifies 'Bankruptcy and insolvency'. Under this entry, Parliament enacted the Insolvency and Bankruptcy Code (IBC), 2016.",
        "பட்டியல் III-ன் (பொதுப் பட்டியல்) பதிவு 9 'திவால் மற்றும் நொடிப்பு நிலை'யைக் குறிப்பிடுகிறது. இந்த பதிவின் கீழ் பாராளுமன்றம் திவால் மற்றும் நொடிப்பு குறியீடு (IBC) 2016-ஐ இயற்றியது.",
        "Correct. Bankruptcy and insolvency is Entry 9 of the Concurrent List.", "சரியானது. திவால் மற்றும் நொடிப்பு நிலை என்பது பொதுப் பட்டியல் பதிவு 9.",
        "Incorrect. Entry 43 of List I deals with incorporation of trading corporations.", "தவறானது. பட்டியல் I பதிவு 43 வர்த்தகக் கழகங்களை உருவாக்குவதைக் கையாள்கிறது.",
        "Incorrect. Entry 30 of List II deals with money-lending and money-lenders.", "தவறானது. பட்டியல் II பதிவு 30 கந்துவட்டி மற்றும் கடன் வழங்குபவர்களைக் கையாள்கிறது.",
        "Incorrect. It is explicitly listed in List III.", "தவறானது. இது வெளிப்படையாக பட்டியல் III-ல் பட்டியலிடப்பட்டுள்ளது.",
        "Insolvency and Bankruptcy Code (IBC) 2016: Enacted under List III Entry 9 (Concurrent List).",
        "திவால் மற்றும் நொடிப்பு குறியீடு (IBC) 2016: பட்டியல் III பதிவு 9-ன் கீழ் இயற்றப்பட்டது."
    ))

    # GT054
    qs.append(make_sch_q(
        "SCH_GT_054", "Hard", "Conceptual", "Seventh Schedule",
        "Which Entry in the Union List empowers Parliament to declare regulation and development of inter-State rivers and river valleys expedient in the public interest?",
        "பொதுநலன் கருதி மாநிலங்களுக்கு இடையேயான நதிகள் மற்றும் நதிப் பள்ளத்தாக்குகளின் ஒழுங்குமுறை மற்றும் மேம்பாட்டை பாராளுமன்றம் அறிவிக்க அதிகாரம் அளிக்கும் மத்திய பட்டியல் பதிவு எது?",
        "Entry 56 of List I", "பட்டியல் I-ன் பதிவு 56",
        "Entry 17 of List II", "பட்டியல் II-ன் பதிவு 17",
        "Entry 54 of List I", "பட்டியல் I-ன் பதிவு 54",
        "Entry 20 of List III", "பட்டியல் III-ன் பதிவு 20",
        "A",
        "Entry 56 of List I covers: 'Regulation and development of inter-State rivers and river valleys to the extent to which such regulation and development under the control of the Union is declared by Parliament by law to be expedient in the public interest.' This qualifies Entry 17 of List II (Water).",
        "பட்டியல் I-ன் பதிவு 56 குறிப்பிடுகிறது: மாநிலங்களுக்கு இடையேயான நதிகள் மற்றும் நதிப் பள்ளத்தாக்குகளை மத்திய அரசின் கட்டுப்பாட்டின் கீழ் ஒழுங்குபடுத்துவதும் மேம்படுத்துவதும் பொதுநலனுக்கு உகந்தது என பாராளுமன்றம் சட்டம் மூலம் அறிவிக்கும் அளவிற்கு உள்ள அதிகாரம். இது மாநிலப் பட்டியலின் பதிவு 17-ஐ (நீர்) கட்டுப்படுத்துகிறது.",
        "Correct. Entry 56 of List I governs inter-State rivers under Parliamentary declaration.", "சரியானது. பட்டியல் I பதிவு 56 மாநிலங்களுக்கு இடையேயான நதிகளை நிர்வகிக்கிறது.",
        "Incorrect. Entry 17 of List II is State control over water, subject to Entry 56 of List I.", "தவறானது. பட்டியல் II பதிவு 17 என்பது மத்திய பட்டியல் பதிவு 56-க்கு உட்பட்ட மாநில நீர் அதிகாரம்.",
        "Incorrect. Entry 54 of List I covers regulation of mines.", "தவறானது. பட்டியல் I பதிவு 54 சுரங்கங்கள் ஒழுங்குமுறையைக் குறிக்கிறது.",
        "Incorrect. Entry 20 of List III covers economic and social planning.", "தவறானது. பட்டியல் III பதிவு 20 பொருளாதாரத் திட்டமிடலைக் குறிக்கிறது.",
        "Inter-State Water Disputes: Entry 17 of List II is subject to Entry 56 of List I and Article 262.",
        "மாநிலங்களுக்கு இடையேயான நதிநீர் தகராறுகள்: பட்டியல் II பதிவு 17 ஆனது பட்டியல் I பதிவு 56 மற்றும் சரத்து 262-க்கு உட்பட்டது."
    ))

    # GT055
    qs.append(make_sch_q(
        "SCH_GT_055", "Medium", "Conceptual", "Seventh Schedule",
        "Under which List of the Seventh Schedule does the subject 'Betting and gambling' fall, enabling States to regulate or ban online gaming?",
        "ஏழாவது அட்டவணையின் எந்தப் பட்டியலின் கீழ் 'பந்தயம் மற்றும் சூதாட்டம்' வருகிறது, இது ஆன்லைன் விளையாட்டுகளை ஒழுங்குபடுத்த அல்லது தடை செய்ய மாநிலங்களுக்கு அதிகாரம் அளிக்கிறது?",
        "List II (State List) – Entry 34", "பட்டியல் II (மாநிலப் பட்டியல்) – பதிவு 34",
        "List I (Union List) – Entry 40", "பட்டியல் I (மத்திய பட்டியல்) – பதிவு 40",
        "List III (Concurrent List) – Entry 28", "பட்டியல் III (பொதுப் பட்டியல்) – பதிவு 28",
        "Residuary Powers under Article 248", "சரத்து 248-ன் கீழான எஞ்சிய அதிகாரங்கள்",
        "A",
        "Entry 34 of List II (State List) covers 'Betting and gambling'. Under this entry, States like Tamil Nadu have enacted laws prohibiting or regulating online gambling and games of chance.",
        "பட்டியல் II-ன் (மாநிலப் பட்டியல்) பதிவு 34 'பந்தயம் மற்றும் சூதாட்டம்' என்பதைக் குறிக்கிறது. இதன் கீழ் தமிழ்நாடு போன்ற மாநிலங்கள் ஆன்லைன் சூதாட்டத்தைத் தடைசெய்ய அல்லது ஒழுங்குபடுத்த சட்டங்களை இயற்றியுள்ளன.",
        "Correct. Betting and gambling is Entry 34 of the State List.", "சரியானது. பந்தயம் மற்றும் சூதாட்டம் என்பது மாநிலப் பட்டியல் பதிவு 34.",
        "Incorrect. Entry 40 of List I covers Lotteries organized by the Government of India or the Government of a State.", "தவறானது. பட்டியல் I பதிவு 40 அரசு நடத்தும் லாட்டரிகளைக் கையாள்கிறது.",
        "Incorrect. Entry 28 of List III covers charities and religious endowments.", "தவறானது. பட்டியல் III பதிவு 28 தொண்டு நிறுவனங்கள் மற்றும் அறக்கட்டளைகளைக் கையாள்கிறது.",
        "Incorrect. Betting and gambling is a specific enumerated state entry.", "தவறானது. இது மாநிலப் பட்டியலில் தெளிவாகக் குறிப்பிடப்பட்டுள்ளது.",
        "TN Online Gaming Law: Enacted under Entry 34 of the State List (Betting and Gambling).",
        "தமிழ்நாடு ஆன்லைன் விளையாட்டு சட்டம்: மாநிலப் பட்டியல் பதிவு 34-ன் கீழ் (பந்தயம் மற்றும் சூதாட்டம்) இயற்றப்பட்டது."
    ))

    # GT056
    qs.append(make_sch_q(
        "SCH_GT_056", "Hard", "Conceptual", "Seventh Schedule",
        "Which judicial doctrine is applied by the Supreme Court when a statute enacted by a legislature under its assigned List incidentally encroaches upon a subject in another List?",
        "ஒரு சட்டமன்றம் தனக்கு ஒதுக்கப்பட்ட பட்டியலின் கீழ் இயற்றிய சட்டம் மற்றொரு பட்டியலில் உள்ள ஒரு விஷயத்தில் தற்செயலாக தலையிடும் போது உச்சநீதிமன்றத்தால் பயன்படுத்தப்படும் நீதித்துறை கோட்பாடு எது?",
        "Doctrine of Pith and Substance", "சாரம் மற்றும் உட்பொருள் கோட்பாடு (Doctrine of Pith and Substance)",
        "Doctrine of Colorable Legislation", "வண்ணமயமான சட்டமியற்றல் கோட்பாடு (Doctrine of Colorable Legislation)",
        "Doctrine of Severability", "பிரித்தெடுக்கும் கோட்பாடு (Doctrine of Severability)",
        "Doctrine of Eclipse", "கிரகணக் கோட்பாடு (Doctrine of Eclipse)",
        "A",
        "The Doctrine of Pith and Substance examines the true nature and character of the legislation. If the enactment in its substance falls within the competence of the legislature enacting it, an incidental encroachment into another list does not invalidate it.",
        "சாரம் மற்றும் உட்பொருள் கோட்பாடு ஒரு சட்டத்தின் உண்மையான தன்மை மற்றும் சாராம்சத்தை ஆராய்கிறது. ஒரு சட்டம் அடிப்படையில் அதை இயற்றும் சட்டமன்றத்தின் அதிகார வரம்பிற்குள் வந்தால், மற்றொரு பட்டியலில் ஏற்படும் தற்செயலான தலையீடு அதை செல்லாததாக்காது.",
        "Correct. Pith and Substance validates legislation with incidental encroachment.", "சரியானது. தற்செயலான தலையீடு கொண்ட சட்டத்தை சாரம் மற்றும் உட்பொருள் கோட்பாடு செல்லுபடியாக்குகிறது.",
        "Incorrect. Colorable legislation means 'what cannot be done directly cannot be done indirectly'.", "தவறானது. வண்ணமயமான சட்டமியற்றல் என்பது மறைமுகமாக அதிகார அத்துமீறல் செய்வதைக் குறிக்கிறது.",
        "Incorrect. Severability separates valid portions from invalid portions under Art 13.", "தவறானது. பிரித்தெடுக்கும் கோட்பாடு செல்லுபடியாகும் பகுதிகளைப் பிரிக்கிறது.",
        "Incorrect. Eclipse applies to pre-constitutional laws overshadowed by fundamental rights.", "தவறானது. கிரகணக் கோட்பாடு அரசியலமைப்புக்கு முந்தைய சட்டங்களுக்குப் பொருந்தும்.",
        "Pith and Substance: Originates from Canadian constitutional jurisprudence; widely applied under Seventh Schedule.",
        "சாரம் மற்றும் உட்பொருள் கோட்பாடு: கனடிய அரசியலமைப்புச் சட்டத்திலிருந்து பெறப்பட்டு, ஏழாவது அட்டவணையில் பரவலாகப் பயன்படுத்தப்படுகிறது."
    ))

    # GT057
    qs.append(make_sch_q(
        "SCH_GT_057", "Medium", "Conceptual", "Seventh Schedule",
        "Under Article 254(1), what happens when a State law enacted on a Concurrent List subject directly conflicts with a Parliamentary enactment on the same subject?",
        "சரத்து 254(1)-ன் கீழ், பொதுப் பட்டியல் விஷயத்தில் இயற்றப்பட்ட மாநிலச் சட்டம் பாராளுமன்றச் சட்டத்துடன் நேரடியாக முரண்படும் போது என்ன நிகழ்கிறது?",
        "The Parliamentary law prevails, and the State law is void to the extent of the repugnancy", "பாராளுமன்றச் சட்டம் மேலோங்கும், மேலும் முரண்பாட்டின் அளவிற்கு மாநிலச் சட்டம் செல்லாததாகும்",
        "The State law automatically supersedes the Parliamentary law within that State", "மாநிலச் சட்டம் அந்த மாநிலத்திற்குள் தானாகவே பாராளுமன்றச் சட்டத்தை விட மேலோங்கும்",
        "Both laws are struck down, and the Supreme Court must frame administrative rules", "இரு சட்டங்களும் ரத்து செய்யப்பட்டு, உச்சநீதிமன்றம் நிர்வாக விதிகளை உருவாக்க வேண்டும்",
        "The Governor of the State decides which law to enforce based on public feedback", "பொதுமக்களின் கருத்தின் அடிப்படையில் எந்தச் சட்டத்தை அமல்படுத்துவது என்பதை ஆளுநர் தீர்மானிக்கிறார்",
        "A",
        "Article 254(1) lays down the rule of Federal Supremacy: if any provision of a law made by the Legislature of a State is repugnant to any provision of a law made by Parliament on a Concurrent List subject, the Parliamentary law prevails, and the State law is void to the extent of repugnancy.",
        "சரத்து 254(1) கூட்டாட்சி மேலாதிக்க விதியைக் கூறுகிறது: பொதுப் பட்டியல் விஷயத்தில் மாநில சட்டமன்றத்தின் சட்டம் பாராளுமன்றத்தின் சட்டத்திற்கு முரணாக இருந்தால், பாராளுமன்றச் சட்டமே மேலோங்கும், மேலும் முரண்பட்ட அளவிற்கு மாநிலச் சட்டம் செல்லாததாகும்.",
        "Correct. Federal law prevails in case of repugnancy under Article 254(1).", "சரியானது. சரத்து 254(1)-ன் கீழ் முரண்பாட்டின் போது மத்திய சட்டமே மேலோங்கும்.",
        "Incorrect. State law prevails only if reserved for and assented to by the President under Article 254(2).", "தவறானது. சரத்து 254(2)-ன் கீழ் குடியரசுத் தலைவரின் ஒப்புதலைப் பெற்றால் மட்டுமே மாநிலச் சட்டம் மேலோங்கும்.",
        "Incorrect. Supreme Court does not strike down both laws.", "தவறானது. உச்சநீதிமன்றம் இரு சட்டங்களையும் ரத்து செய்வதில்லை.",
        "Incorrect. Governor has no discretion to arbitrate repugnancy.", "தவறானது. ஆளுநருக்கு இதில் தன்னிச்சை அதிகாரம் இல்லை.",
        "Article 254 Exception: State law on Concurrent List prevails over central law in that State ONLY if it receives Presidential Assent (Art 254(2)).",
        "சரத்து 254 விதிவிலக்கு: பொதுப் பட்டியல் மாநில சட்டம் குடியரசுத் தலைவரின் ஒப்புதலைப் பெற்றால் மட்டுமே மத்திய சட்டத்தை விட மேலோங்கும் (சரத்து 254(2))."
    ))

    # GT058
    qs.append(make_sch_q(
        "SCH_GT_058", "Hard", "Conceptual", "Seventh Schedule",
        "Under Entry 84 of List I (amended by the 101st Constitutional Amendment Act, 2016), Union excise duties can now only be levied on which specific goods?",
        "101வது அரசியலமைப்புத் திருத்தச் சட்டம் 2016 மூலம் திருத்தப்பட்ட பட்டியல் I-ன் பதிவு 84-ன் கீழ், மத்திய கலால் வரி தற்போது எந்தக் குறிப்பிட்ட பொருட்கள் மீது மட்டுமே விதிக்கப்பட முடியும்?",
        "Petroleum crude, high-speed diesel, motor spirit (petrol), natural gas, aviation turbine fuel, and tobacco products", "கச்சா பெட்ரோலியம், அதிவேக டீசல், மோட்டார் ஸ்பிரிட் (பெட்ரோல்), இயற்கை எரிவாயு, விமான டர்பைன் எரிபொருள் மற்றும் புகையிலைப் பொருட்கள்",
        "All manufactured electronic equipment, textiles, and imported automobiles", "அனைத்து உற்பத்தி செய்யப்பட்ட மின்னணு உபகரணங்கள், ஜவுளிகள் மற்றும் இறக்குமதி செய்யப்பட்ட கார்கள்",
        "Alcoholic liquors for human consumption and opium", "மனித பயன்பாட்டிற்கான மதுபானங்கள் மற்றும் அபின்",
        "Agricultural seeds, fertilizers, and raw cotton produce", "விவசாய விதைகள், உரங்கள் மற்றும் மூலப் பருத்தி பொருட்கள்",
        "A",
        "Following GST (101st CAA 2016), Entry 84 of List I was amended to restrict Union excise duties to six items: petroleum crude, high-speed diesel, motor spirit (petrol), natural gas, aviation turbine fuel, and tobacco/tobacco products. All other manufactured goods shifted to GST.",
        "ஜிஎஸ்டிக்குப் பிறகு (101வது திருத்தம் 2016), பட்டியல் I பதிவு 84 திருத்தப்பட்டு, மத்திய கலால் வரியை ஆறு பொருட்களுக்கு மட்டுமே மட்டுப்படுத்தியது: கச்சா பெட்ரோலியம், அதிவேக டீசல், பெட்ரோல், இயற்கை எரிவாயு, விமான எரிபொருள் மற்றும் புகையிலைப் பொருட்கள்.",
        "Correct. Entry 84 List I is restricted to 5 petroleum items + tobacco.", "சரியானது. பட்டியல் I பதிவு 84 ஆனது 5 பெட்ரோலியப் பொருட்கள் + புகையிலைக்கு மட்டுமே மட்டுப்படுத்தப்பட்டுள்ளது.",
        "Incorrect. Electronics and automobiles are subsumed under GST.", "தவறானது. மின்னணுவியல் மற்றும் கார்கள் ஜிஎஸ்டி-க்குள் கொண்டுவரப்பட்டுள்ளன.",
        "Incorrect. Alcoholic liquor for human consumption is under State List Entry 51.", "தவறானது. மனித நுகர்வுக்கான மதுபானம் மாநிலப் பட்டியல் பதிவு 51-ன் கீழ் உள்ளது.",
        "Incorrect. Agricultural inputs are exempt from central excise.", "தவறானது. விவசாய உள்ளீடுகளுக்கு மத்திய கலால் வரியிலிருந்து விலக்கு அளிக்கப்பட்டுள்ளது.",
        "Post-GST Entry 84: Only 5 petroleum products + tobacco remain under Central Excise.",
        "ஜிஎஸ்டிக்குப் பிந்தைய பதிவு 84: 5 பெட்ரோலியப் பொருட்கள் + புகையிலை மட்டுமே மத்திய கலால் வரியின் கீழ் உள்ளன."
    ))

    # GT059
    qs.append(make_sch_q(
        "SCH_GT_059", "Medium", "Conceptual", "Eighth Schedule",
        "Under Article 344(1), after how many years from the commencement of the Constitution was the President mandated to constitute the first Official Language Commission?",
        "சரத்து 344(1)-ன் கீழ், அரசியலமைப்பு தொடங்கப்பட்டதிலிருந்து எத்தனை ஆண்டுகளுக்குப் பிறகு முதல் அதிகாரப்பூர்வ மொழிகள் ஆணையத்தைக் குடியரசுத் தலைவர் அமைக்க வேண்டும் எனக் கட்டாயப்படுத்தப்பட்டது?",
        "At the expiration of 5 years from the commencement of the Constitution", "அரசியலமைப்பு தொடங்கப்பட்டதிலிருந்து 5 ஆண்டுகள் முடிவடைந்தவுடன்",
        "At the expiration of 10 years from the commencement of the Constitution", "அரசியலமைப்பு தொடங்கப்பட்டதிலிருந்து 10 ஆண்டுகள் முடிவடைந்தவுடன்",
        "At the expiration of 15 years from the commencement of the Constitution", "அரசியலமைப்பு தொடங்கப்பட்டதிலிருந்து 15 ஆண்டுகள் முடிவடைந்தவுடன்",
        "Every 20 years concurrently with the Finance Commission", "நிதி ஆணையத்துடன் இணைந்து ஒவ்வொரு 20 ஆண்டுகளுக்கும் ஒருமுறை",
        "A",
        "Article 344(1) mandates that the President shall, at the expiration of five years from the commencement of this Constitution and thereafter at the expiration of ten years, constitute a Commission representing different languages specified in the Eighth Schedule (The B.G. Kher Commission was appointed in 1955).",
        "சரத்து 344(1) கூறுகிறது: அரசியலமைப்பு தொடங்கப்பட்டதிலிருந்து ஐந்து ஆண்டுகள் முடிவடைந்தவுடனும், பின்னர் பத்து ஆண்டுகள் முடிவடைந்தவுடனும், எட்டாவது அட்டவணையில் குறிப்பிடப்பட்டுள்ள பல்வேறு மொழிகளைப் பிரதிநிதித்துவப்படுத்தும் ஆணையத்தை குடியரசுத் தலைவர் அமைக்க வேண்டும் (1955-ல் பி.ஜி. கேர் ஆணையம் அமைக்கப்பட்டது).",
        "Correct. Article 344(1) mandates the first commission at 5 years (1955).", "சரியானது. சரத்து 344(1) முதல் ஆணையத்தை 5 ஆண்டுகளில் (1955) கட்டாயமாக்குகிறது.",
        "Incorrect. 10 years was the milestone for the second commission.", "தவறானது. 10 ஆண்டுகள் என்பது இரண்டாவது ஆணையத்திற்கான மைல்கல்.",
        "Incorrect. 15 years was the initial transitional period for English under Art 343(2).", "தவறானது. 15 ஆண்டுகள் என்பது சரத்து 343(2)-ன் கீழ் ஆங்கிலத்திற்கான தொடக்க மாற்றுக் காலம்.",
        "Incorrect. Finance Commission is constituted every 5 years under Art 280.", "தவறானது. நிதி ஆணையம் சரத்து 280-ன் கீழ் 5 ஆண்டுகளுக்கு ஒருமுறை அமைக்கப்படுகிறது.",
        "First Official Language Commission: Appointed in 1955 under B.G. Kher; submitted report in 1956.",
        "முதல் அதிகாரப்பூர்வ மொழி ஆணையம்: 1955-ல் பி.ஜி. கேர் தலைமையில் அமைக்கப்பட்டு 1956-ல் அறிக்கை சமர்ப்பித்தது."
    ))

    # GT060
    qs.append(make_sch_q(
        "SCH_GT_060", "Hard", "Conceptual", "Eighth Schedule",
        "Under Article 351 of the Constitution, which Eighth Schedule language is specifically designated as the primary source from which Hindi should draw for its vocabulary?",
        "அரசியலமைப்பின் சரத்து 351-ன் கீழ், இந்தி மொழி தனது சொல்லகராதியை முதன்மையாகப் பெறுவதற்கு எந்த எட்டாவது அட்டவணை மொழி குறிப்பிட்ட மூலமாக நியமிக்கப்பட்டுள்ளது?",
        "Sanskrit", "சமஸ்கிருதம்",
        "Prakrit", "பிராகிருதம்",
        "Pali", "பாலி",
        "Persian", "பாரசீகம்",
        "A",
        "Article 351 states that it shall be the duty of the Union to promote the spread of the Hindi language and to develop it so that it may serve as a medium of expression, drawing for its vocabulary primarily on Sanskrit and secondarily on other languages.",
        "சரத்து 351 குறிப்பிடுகிறது: இந்தி மொழியின் பயன்பாட்டைப் பரப்புவதும், அது ஒரு வெளிப்பாட்டு ஊடகமாகச் செயல்படும் வகையில் அதன் சொல்லகராதியை முதன்மையாக சமஸ்கிருதத்திலிருந்தும், இரண்டாவதாக பிற மொழிகளிலிருந்தும் பெற்று வளர்ப்பதும் மத்திய அரசின் கடமையாகும்.",
        "Correct. Article 351 explicitly names Sanskrit as the primary source of Hindi vocabulary.", "சரியானது. சரத்து 351 இந்தி சொல்லகராதிக்கான முதன்மை மூலமாக சமஸ்கிருதத்தைக் குறிப்பிடுகிறது.",
        "Incorrect. Prakrit is an ancient language not named in Article 351.", "தவறானது. பிராகிருதம் சரத்து 351-ல் குறிப்பிடப்படவில்லை.",
        "Incorrect. Pali is not named in Article 351.", "தவறானது. பாலி சரத்து 351-ல் குறிப்பிடப்படவில்லை.",
        "Incorrect. Persian is not an Eighth Schedule language nor named in Article 351.", "தவறானது. பாரசீகம் எட்டாவது அட்டவணை மொழியோ அல்லது சரத்து 351-ல் குறிப்பிடப்பட்டதோ அல்ல.",
        "Article 351: Directive for development of Hindi; draws primarily on Sanskrit and secondarily on other Eighth Schedule languages.",
        "சரத்து 351: இந்தி வளர்ச்சிக்கான வழிகாட்டுதல்; சொல்லகராதி முதன்மையாக சமஸ்கிருதத்திலிருந்தும் இரண்டாவதாக பிற அட்டவணை மொழிகளிலிருந்தும் பெறப்பட வேண்டும்."
    ))

    # GT061
    qs.append(make_sch_q(
        "SCH_GT_061", "Easy", "Conceptual", "Eighth Schedule",
        "Which of the following was the FIRST language to be officially declared a 'Classical Language' in India by the Union Government in 2004?",
        "2004-ல் மத்திய அரசால் இந்தியாவில் அதிகாரப்பூர்வமாக 'செம்மொழி' (Classical Language) என அறிவிக்கப்பட்ட முதல் மொழி எது?",
        "Tamil", "தமிழ்",
        "Sanskrit", "சமஸ்கிருதம்",
        "Telugu", "தெலுங்கு",
        "Kannada", "கன்னடம்",
        "A",
        "Tamil was the first language to be accorded Classical Language status in India in 2004. Sanskrit followed in 2005, Telugu and Kannada in 2008, Malayalam in 2013, Odia in 2014, and recently Marathi, Pali, Prakrit, Assamese, and Bengali in 2024.",
        "இந்தியாவில் 2004-ல் செம்மொழி அந்தஸ்து வழங்கப்பட்ட முதல் மொழி தமிழ் ஆகும். சமஸ்கிருதம் 2005-லும், தெலுங்கு மற்றும் கன்னடம் 2008-லும், மலையாளம் 2013-லும், ஒடியா 2014-லும் அறிவிக்கப்பட்டன.",
        "Correct. Tamil was declared the first Classical Language in October 2004.", "சரியானது. 2004 அக்டோபரில் தமிழ் முதல் செம்மொழியாக அறிவிக்கப்பட்டது.",
        "Incorrect. Sanskrit was declared Classical in 2005.", "தவறானது. சமஸ்கிருதம் 2005-ல் செம்மொழியாக அறிவிக்கப்பட்டது.",
        "Incorrect. Telugu was declared Classical in 2008.", "தவறானது. தெலுங்கு 2008-ல் செம்மொழியாக அறிவிக்கப்பட்டது.",
        "Incorrect. Kannada was declared Classical in 2008.", "தவறானது. கன்னடம் 2008-ல் செம்மொழியாக அறிவிக்கப்பட்டது.",
        "Classical Languages Chronology: Tamil (2004) -> Sanskrit (2005) -> Kannada & Telugu (2008) -> Malayalam (2013) -> Odia (2014).",
        "செம்மொழிகள் காலவரிசை: தமிழ் (2004) -> சமஸ்கிருதம் (2005) -> கன்னடம் & தெலுங்கு (2008) -> மலையாளம் (2013) -> ஒடியா (2014)."
    ))

    # GT062
    qs.append(make_sch_q(
        "SCH_GT_062", "Medium", "Conceptual", "Eighth Schedule",
        "Which language spoken predominantly in the Jammu region of Jammu and Kashmir was added to the Eighth Schedule by the 92nd Constitutional Amendment Act, 2003?",
        "92வது அரசியலமைப்புத் திருத்தச் சட்டம் 2003 மூலம் எட்டாவது அட்டவணையில் சேர்க்கப்பட்ட ஜம்மு காஷ்மீரின் ஜம்மு பகுதியில் முதன்மையாகப் பேசப்படும் மொழி எது?",
        "Dogri", "டோக்ரி",
        "Kashmiri", "காஷ்மீரி",
        "Ladakhi", "லடாக்கி",
        "Balti", "பால்டி",
        "A",
        "Dogri was added to the Eighth Schedule along with Bodo, Maithili, and Santhali by the 92nd Constitutional Amendment Act, 2003. Kashmiri was already one of the original 14 languages in 1950.",
        "92வது அரசியலமைப்புத் திருத்தச் சட்டம் 2003 மூலம் போடோ, மைதிலி மற்றும் சந்தாலியுடன் டோக்ரி மொழியும் எட்டாவது அட்டவணையில் சேர்க்கப்பட்டது. காஷ்மீரி 1950-லேயே மூல 14 மொழிகளில் ஒன்றாக இருந்தது.",
        "Correct. Dogri was added by the 92nd CAA 2003.", "சரியானது. டோக்ரி 92வது திருத்தம் 2003 மூலம் சேர்க்கப்பட்டது.",
        "Incorrect. Kashmiri was an original 1950 Eighth Schedule language.", "தவறானது. காஷ்மீரி 1950-ன் மூல எட்டாவது அட்டவணை மொழி.",
        "Incorrect. Ladakhi is not in the Eighth Schedule.", "தவறானது. லடாக்கி எட்டாவது அட்டவணையில் இல்லை.",
        "Incorrect. Balti is not an Eighth Schedule language.", "தவறானது. பால்டி எட்டாவது அட்டவணை மொழி அல்ல.",
        "92nd CAA 2003 Mnemonic 'BDMS': Bodo, Dogri, Maithili, Santhali.",
        "92வது திருத்தம் 2003 நினைவுக் குறிப்பு 'BDMS': போடோ, டோக்ரி, மைதிலி, சந்தாலி."
    ))

    # GT063
    qs.append(make_sch_q(
        "SCH_GT_063", "Hard", "Conceptual", "Eighth Schedule",
        "Which Eighth Schedule language belongs to the Tibeto-Burman language family and is historically associated with the Meitei Mayek script?",
        "எட்டாவது அட்டவணை மொழிகளில் எது திபெத்தோ-பர்மிய மொழிக்குடும்பத்தைச் சேர்ந்தது மற்றும் வரலாற்று ரீதியாக மீதேய் மாயேக் எழுத்துமுறையுடன் தொடர்புடையது?",
        "Manipuri (Meitei)", "மணிப்பூரி (மீதேய்)",
        "Assamese", "அசாமி",
        "Nepali", "நேபாள",
        "Konkani", "கொங்கணி",
        "A",
        "Manipuri (Meitei), added to the Eighth Schedule by the 71st CAA in 1992, belongs to the Tibeto-Burman branch of the Sino-Tibetan language family and has its indigenous script Meitei Mayek.",
        "1992-ல் 71வது திருத்தத்தின் மூலம் எட்டாவது அட்டவணையில் சேர்க்கப்பட்ட மணிப்பூரி (மீதேய்), சீன-திபெத்திய மொழிக் குடும்பத்தின் திபெத்தோ-பர்மிய கிளையைச் சேர்ந்தது மற்றும் அதன் சொந்த மீதேய் மாயேக் எழுத்துமுறையைக் கொண்டுள்ளது.",
        "Correct. Manipuri (Meitei) is a Tibeto-Burman language using Meitei Mayek.", "சரியானது. மணிப்பூரி (மீதேய்) மீதேய் மாயேக் எழுத்துமுறையைப் பயன்படுத்தும் திபெத்தோ-பர்மிய மொழி.",
        "Incorrect. Assamese is an Indo-Aryan language.", "தவறானது. அசாமி ஒரு இந்தோ-ஆரிய மொழி.",
        "Incorrect. Nepali is an Indo-Aryan language written in Devanagari.", "தவறானது. நேபாளி தேவநாகரி எழுத்தில் எழுதப்படும் இந்தோ-ஆரிய மொழி.",
        "Incorrect. Konkani is an Indo-Aryan language written in Devanagari/Roman.", "தவறானது. கொங்கணி ஒரு இந்தோ-ஆரிய மொழி.",
        "71st CAA 1992: Added Konkani, Manipuri, and Nepali ('KMN').",
        "71வது திருத்தம் 1992: கொங்கணி, மணிப்பூரி மற்றும் நேபாளி ('KMN') ஆகியவற்றைச் சேர்த்தது."
    ))

    # GT064
    qs.append(make_sch_q(
        "SCH_GT_064", "Easy", "Conceptual", "Eighth Schedule",
        "Under Article 348(1)(a) of the Constitution, what is the authoritative language for all proceedings in the Supreme Court of India until Parliament by law otherwise provides?",
        "சரத்து 348(1)(a)-ன் கீழ், பாராளுமன்றம் சட்டத்தின் மூலம் வேறுவிதமாக வழங்கும் வரை இந்திய உச்சநீதிமன்றத்தின் அனைத்து நடவடிக்கைகளுக்குமான அதிகாரப்பூர்வ மொழி எது?",
        "English", "ஆங்கிலம்",
        "Hindi in Devanagari script", "தேவநாகரி எழுத்து வடிவிலான இந்தி",
        "Sanskrit", "சமஸ்கிருதம்",
        "Any language listed in the Eighth Schedule", "எட்டாவது அட்டவணையில் பட்டியலிடப்பட்டுள்ள ஏதேனும் ஒரு மொழி",
        "A",
        "Article 348(1)(a) explicitly provides that until Parliament by law otherwise provides, all proceedings in the Supreme Court and in every High Court shall be in the English language.",
        "சரத்து 348(1)(a) தெளிவாகக் குறிப்பிடுகிறது: பாராளுமன்றம் சட்டத்தின் மூலம் வேறுவிதமாக வழங்கும் வரை, உச்சநீதிமன்றம் மற்றும் ஒவ்வொரு உயர்நீதிமன்றத்தின் அனைத்து நடவடிக்கைகளும் ஆங்கில மொழியிலேயே இருக்க வேண்டும்.",
        "Correct. English is mandatory for Supreme Court proceedings under Article 348(1)(a).", "சரியானது. சரத்து 348(1)(a)-ன் கீழ் உச்சநீதிமன்ற நடவடிக்கைகளுக்கு ஆங்கிலம் கட்டாயமானது.",
        "Incorrect. Hindi is not the authoritative language for Supreme Court proceedings.", "தவறானது. இந்தி உச்சநீதிமன்ற நடவடிக்கைகளுக்கான அதிகாரப்பூர்வ மொழி அல்ல.",
        "Incorrect. Sanskrit is not used for judicial proceedings.", "தவறானது. சமஸ்கிருதம் நீதிமன்ற நடவடிக்கைகளுக்குப் பயன்படுவதில்லை.",
        "Incorrect. Eighth Schedule languages cannot be used in the Supreme Court without parliamentary law.", "தவறானது. பாராளுமன்ற சட்டமின்றி அட்டவணை மொழிகளை உச்சநீதிமன்றத்தில் பயன்படுத்த முடியாது.",
        "Judicial Language: English remains the sole authoritative language of the Supreme Court under Article 348(1).",
        "நீதிமன்ற மொழி: சரத்து 348(1)-ன் கீழ் ஆங்கிலமே உச்சநீதிமன்றத்தின் ஒரே அதிகாரப்பூர்வ மொழியாகத் தொடர்கிறது."
    ))

    # GT065
    qs.append(make_sch_q(
        "SCH_GT_065", "Medium", "Conceptual", "Eighth Schedule",
        "In which year was Sindhi added to the Eighth Schedule of the Indian Constitution by the 21st Constitutional Amendment Act?",
        "21வது அரசியலமைப்புத் திருத்தச் சட்டம் மூலம் எந்த ஆண்டு சிந்தி மொழி எட்டாவது அட்டவணையில் 15வது மொழியாகச் சேர்க்கப்பட்டது?",
        "1967", "1967",
        "1956", "1956",
        "1971", "1971",
        "1992", "1992",
        "A",
        "The Constitution (Twenty-first Amendment) Act, 1967 added Sindhi as the 15th language to the Eighth Schedule, marking the very first addition of a language after the Constitution's commencement.",
        "அரசியலமைப்பு (இருபத்தியொன்றாவது திருத்தச்) சட்டம் 1967, சிந்தி மொழியை 15வது மொழியாக எட்டாவது அட்டவணையில் சேர்த்தது; இது அரசியலமைப்பு அமலுக்கு வந்த பிறகு சேர்க்கப்பட்ட முதல் மொழியாகும்.",
        "Correct. Sindhi was added in 1967 via the 21st Amendment.", "சரியானது. சிந்தி 1967-ல் 21வது திருத்தம் மூலம் சேர்க்கப்பட்டது.",
        "Incorrect. 1956 was the year of States Reorganisation.", "தவறானது. 1956 என்பது மாநிலங்கள் மறுசீரமைப்பு ஆண்டு.",
        "Incorrect. 1971 saw the 24th and 25th Amendments, not Sindhi.", "தவறானது. 1971-ல் 24வது மற்றும் 25வது திருத்தங்கள் வந்தன.",
        "Incorrect. 1992 was the 71st Amendment (Konkani, Manipuri, Nepali).", "தவறானது. 1992 என்பது 71வது திருத்தம்.",
        "Language Amendment Formula: 21st CAA (1967: Sindhi) + 71st CAA (1992: KMN) = 92nd CAA (2003: BDMS). Notice 21 + 71 = 92!",
        "மொழித் திருத்தக் கணித சூத்திரம்: 21வது திருத்தம் (1967) + 71வது திருத்தம் (1992) = 92வது திருத்தம் (2003). 21 + 71 = 92!"
    ))

    # GT066
    qs.append(make_sch_q(
        "SCH_GT_066", "Easy", "Conceptual", "Eighth Schedule",
        "Which three languages were added to the Eighth Schedule by the 71st Constitutional Amendment Act in 1992?",
        "1992-ல் 71வது அரசியலமைப்புத் திருத்தச் சட்டம் மூலம் எட்டாவது அட்டவணையில் சேர்க்கப்பட்ட மூன்று மொழிகள் எவை?",
        "Konkani, Manipuri, and Nepali", "கொங்கணி, மணிப்பூரி மற்றும் நேபாளி",
        "Bodo, Dogri, and Maithili", "போடோ, டோக்ரி மற்றும் மைதிலி",
        "Sindhi, Sanskrit, and Urdu", "சிந்தி, சமஸ்கிருதம் மற்றும் உருது",
        "Santhali, Kashmiri, and Punjabi", "சந்தாலி, காஷ்மீரி மற்றும் பஞ்சாபி",
        "A",
        "The 71st Constitutional Amendment Act, 1992 added Konkani, Manipuri, and Nepali to the Eighth Schedule, raising the total number of recognized languages from 15 to 18.",
        "71வது அரசியலமைப்புத் திருத்தச் சட்டம் 1992, கொங்கணி, மணிப்பூரி மற்றும் நேபாளி ஆகிய மொழிகளை எட்டாவது அட்டவணையில் சேர்த்தது; இதன் மூலம் அங்கீகரிக்கப்பட்ட மொழிகளின் எண்ணிக்கை 15-லிருந்து 18 ஆக உயர்ந்தது.",
        "Correct. 71st CAA added Konkani, Manipuri, Nepali ('KMN').", "சரியானது. 71வது திருத்தம் கொங்கணி, மணிப்பூரி, நேபாளியைச் சேர்த்தது.",
        "Incorrect. Bodo, Dogri, Maithili were added by the 92nd CAA 2003.", "தவறானது. போடோ, டோக்ரி, மைதிலி 92வது திருத்தம் 2003 மூலம் சேர்க்கப்பட்டன.",
        "Incorrect. Sindhi was added in 1967; Sanskrit and Urdu were original.", "தவறானது. சிந்தி 1967-ல் சேர்க்கப்பட்டது; சமஸ்கிருதம் மற்றும் உருது மூல மொழிகள்.",
        "Incorrect. Santhali was 92nd CAA; Kashmiri and Punjabi were original.", "தவறானது. சந்தாலி 92வது திருத்தம்; காஷ்மீரி மற்றும் பஞ்சாபி மூல மொழிகள்.",
        "71st Amendment (1992): Added Konkani, Manipuri, Nepali. Mnemonic: K-M-N or 'NAMAK' (Nepali, Manipuri, Konkani).",
        "71வது திருத்தம் (1992): கொங்கணி, மணிப்பூரி, நேபாளி சேர்க்கப்பட்டன. நினைவுக்குறிப்பு: K-M-N அல்லது 'நமக்' (நேபாளி, மணிப்பூரி, கொங்கணி)."
    ))

    # GT067
    qs.append(make_sch_q(
        "SCH_GT_067", "Hard", "Conceptual", "Eighth Schedule",
        "Which tribal language spoken in Jharkhand, West Bengal, and Odisha was added to the Eighth Schedule by the 92nd Amendment Act, 2003, using the Ol Chiki script?",
        "ஜார்க்கண்ட், மேற்கு வங்காளம் மற்றும் ஒடிசாவில் பேசப்படும், 'ஒல் சிக்கி' (Ol Chiki) எழுத்துமுறையைப் பயன்படுத்தும் எந்த பழங்குடி மொழி 92வது திருத்தச் சட்டம் 2003 மூலம் எட்டாவது அட்டவணையில் சேர்க்கப்பட்டது?",
        "Santhali", "சந்தாலி",
        "Ho", "ஹோ",
        "Mundari", "முண்டாரி",
        "Kurukh (Oraon)", "குரூக் (ஒராவோன்)",
        "A",
        "Santhali, written in the indigenous Ol Chiki script created by Pandit Raghunath Murmu, was added to the Eighth Schedule by the 92nd Constitutional Amendment Act, 2003.",
        "பண்டிட் ரகுநாத் முர்மு உருவாக்கிய 'ஒல் சிக்கி' எழுத்துமுறையில் எழுதப்படும் சந்தாலி மொழி, 92வது அரசியலமைப்புத் திருத்தச் சட்டம் 2003 மூலம் எட்டாவது அட்டவணையில் சேர்க்கப்பட்டது.",
        "Correct. Santhali uses Ol Chiki and was added by the 92nd CAA 2003.", "சரியானது. சந்தாலி ஒல் சிக்கி எழுத்துமுறையைப் பயன்படுத்துகிறது மற்றும் 92வது திருத்தம் மூலம் சேர்க்கப்பட்டது.",
        "Incorrect. Ho is not in the Eighth Schedule.", "தவறானது. ஹோ மொழி எட்டாவது அட்டவணையில் இல்லை.",
        "Incorrect. Mundari is not an Eighth Schedule language.", "தவறானது. முண்டாரி எட்டாவது அட்டவணை மொழி அல்ல.",
        "Incorrect. Kurukh is not in the Eighth Schedule.", "தவறானது. குரூக் எட்டாவது அட்டவணையில் இல்லை.",
        "Santhali: The only Austroasiatic (Munda) language included in the Eighth Schedule.",
        "சந்தாலி: எட்டாவது அட்டவணையில் சேர்க்கப்பட்டுள்ள ஒரே ஆஸ்ட்ரோ-ஆசியாட்டிக் (முண்டா) மொழி."
    ))

    # GT068
    qs.append(make_sch_q(
        "SCH_GT_068", "Easy", "Conceptual", "Eighth Schedule",
        "Is English one of the 22 languages specified in the Eighth Schedule of the Constitution of India?",
        "இந்திய அரசியலமைப்பின் எட்டாவது அட்டவணையில் குறிப்பிடப்பட்டுள்ள 22 மொழிகளில் ஆங்கிலமும் ஒன்றா?",
        "No, English is not included in the Eighth Schedule", "இல்லை, ஆங்கிலம் எட்டாவது அட்டவணையில் சேர்க்கப்படவில்லை",
        "Yes, it was included as an original language in 1950", "ஆம், இது 1950-ல் மூல மொழியாகச் சேர்க்கப்பட்டது",
        "Yes, it was added by the 21st Amendment in 1967", "ஆம், இது 1967-ல் 21வது திருத்தம் மூலம் சேர்க்கப்பட்டது",
        "Yes, it was added following the Official Languages Act of 1963", "ஆம், 1963-ன் அதிகாரப்பூர்வ மொழிகள் சட்டத்தைத் தொடர்ந்து சேர்க்கப்பட்டது",
        "A",
        "English is NOT one of the 22 languages listed in the Eighth Schedule of the Constitution of India. It functions as an associate official language of the Union under the Official Languages Act, 1963.",
        "இந்திய அரசியலமைப்பின் எட்டாவது அட்டவணையில் பட்டியலிடப்பட்டுள்ள 22 மொழிகளில் ஆங்கிலம் இடம் பெறவில்லை. இது 1963-ன் அதிகாரப்பூர்வ மொழிகள் சட்டத்தின் கீழ் மத்திய அரசின் இணை அதிகாரப்பூர்வ மொழியாகச் செயல்படுகிறது.",
        "Correct. English is NOT an Eighth Schedule language.", "சரியானது. ஆங்கிலம் எட்டாவது அட்டவணை மொழி அல்ல.",
        "Incorrect. English was never in the Eighth Schedule.", "தவறானது. ஆங்கிலம் ஒருபோதும் எட்டாவது அட்டவணையில் இருந்ததில்லை.",
        "Incorrect. 21st Amendment added Sindhi, not English.", "தவறானது. 21வது திருத்தம் சிந்தியைச் சேர்த்தது, ஆங்கிலத்தை அல்ல.",
        "Incorrect. Official Languages Act did not insert English into the Eighth Schedule.", "தவறானது. அதிகாரப்பூர்வ மொழிகள் சட்டம் ஆங்கிலத்தை அட்டவணையில் சேர்க்கவில்லை.",
        "Common Trap: English is the official language of Nagaland, Meghalaya, and Arunachal Pradesh, yet NOT in the Eighth Schedule!",
        "பொதுவான பொறி: நாகாலாந்து, மேகாலயா மற்றும் அருணாச்சல பிரதேசத்தின் அதிகாரப்பூர்வ மொழி ஆங்கிலம், இருப்பினும் அது எட்டாவது அட்டவணையில் இல்லை!"
    ))

    # GT069
    qs.append(make_sch_q(
        "SCH_GT_069", "Medium", "Conceptual", "Ninth Schedule",
        "How many Acts were initially placed into the Ninth Schedule when it was created by the 1st Constitutional Amendment Act, 1951?",
        "1951-ன் 1வது அரசியலமைப்புத் திருத்தச் சட்டம் மூலம் உருவாக்கப்பட்ட போது ஒன்பதாவது அட்டவணையில் தொடக்கத்தில் எத்தனை சட்டங்கள் வைக்கப்பட்டன?",
        "13 Acts", "13 சட்டங்கள்",
        "1 Act (Bihar Land Reforms Act only)", "1 சட்டம் (பீகார் நிலச் சீர்திருத்தச் சட்டம் மட்டுமே)",
        "25 Acts", "25 சட்டங்கள்",
        "64 Acts", "64 சட்டங்கள்",
        "A",
        "When the Ninth Schedule was created by the 1st Constitutional Amendment Act in 1951 along with Article 31B, it originally contained exactly 13 State land reform enactments.",
        "1951-ல் சரத்து 31B-யுடன் 1வது அரசியலமைப்புத் திருத்தச் சட்டம் மூலம் ஒன்பதாவது அட்டவணை உருவாக்கப்பட்ட போது, அதில் தொடக்கத்தில் சரியாக 13 மாநில நிலச் சீர்திருத்தச் சட்டங்கள் வைக்கப்பட்டன.",
        "Correct. Originally 13 Acts were placed in the Ninth Schedule in 1951.", "சரியானது. 1951-ல் தொடக்கத்தில் 13 சட்டங்கள் ஒன்பதாவது அட்டவணையில் வைக்கப்பட்டன.",
        "Incorrect. Bihar Land Reforms Act was one among the 13, not the sole Act.", "தவறானது. பீகார் நிலச் சீர்திருத்தச் சட்டம் 13 சட்டங்களில் ஒன்று மட்டுமே.",
        "Incorrect. 25 is incorrect.", "தவறானது. 25 என்பது தவறானது.",
        "Incorrect. 64 is incorrect (64 was reached by 1964 via 17th CAA).", "தவறானது. 64 என்பது 1964-ல் 17வது திருத்தம் மூலம் எட்டப்பட்டது.",
        "Ninth Schedule Growth: Began with 13 Acts in 1951; expanded to 284 Acts today.",
        "ஒன்பதாவது அட்டவணை வளர்ச்சி: 1951-ல் 13 சட்டங்களுடன் தொடங்கி; இன்று 284 சட்டங்களாக விரிவடைந்துள்ளது."
    ))

    # GT070
    qs.append(make_sch_q(
        "SCH_GT_070", "Medium", "Conceptual", "Ninth Schedule",
        "Under Article 31B, what specific constitutional protection is granted to laws included in the Ninth Schedule?",
        "சரத்து 31B-ன் கீழ், ஒன்பதாவது அட்டவணையில் சேர்க்கப்பட்டுள்ள சட்டங்களுக்கு என்ன குறிப்பிட்ட அரசியலமைப்புப் பாதுகாப்பு வழங்கப்படுகிறது?",
        "Immunity from being declared void on the ground that they violate any of the Fundamental Rights in Part III", "பகுதி III-ல் உள்ள அடிப்படை உரிமைகளில் எதையும் மீறுகின்றன என்ற அடிப்படையில் அவை செல்லாததாக்கப்படுவதிலிருந்து விலக்குரிமை",
        "Immunity from being repealed or amended by subsequent state legislatures", "பிற்கால மாநில சட்டமன்றங்களால் ரத்து செய்யப்படுவதிலிருந்தோ அல்லது திருத்தப்படுவதிலிருந்தோ விலக்குரிமை",
        "Total exemption from scrutiny by the Comptroller and Auditor-General", "இந்திய தலைமை கணக்குத் தணிக்கையாளரின் தணிக்கையிலிருந்து முழுமையான விலக்கு",
        "Exemption from requiring presidential assent before becoming state law", "மாநில சட்டமாவதற்கு முன் குடியரசுத் தலைவரின் ஒப்புதல் தேவைப்படுவதிலிருந்து விலக்கு",
        "A",
        "Article 31B states that none of the Acts and Regulations specified in the Ninth Schedule shall be deemed to be void on the ground that they take away or abridge any of the rights conferred by Part III of the Constitution.",
        "சரத்து 31B கூறுகிறது: ஒன்பதாவது அட்டவணையில் குறிப்பிடப்பட்டுள்ள சட்டங்கள் மற்றும் ஒழுங்குமுறைகள் எதுவும் அரசியலமைப்பின் பகுதி III-ல் வழங்கப்பட்டுள்ள உரிமைகளில் எதையும் பறிக்கின்றன அல்லது குறைக்கின்றன என்ற அடிப்படையில் செல்லாததாகக் கருதப்படாது.",
        "Correct. Article 31B protects Ninth Schedule laws from Fundamental Rights challenge.", "சரியானது. சரத்து 31B ஒன்பதாவது அட்டவணை சட்டங்களை அடிப்படை உரிமைகள் மீறல் சவாலிலிருந்து பாதுகாக்கிறது.",
        "Incorrect. State legislatures can still repeal or amend their own laws.", "தவறானது. மாநில சட்டமன்றங்கள் தங்கள் சட்டங்களை இன்னும் ரத்து செய்யவோ திருத்தவோ முடியும்.",
        "Incorrect. It has nothing to do with financial audit exemptions.", "தவறானது. இதற்கும் நிதித் தணிக்கை விலக்கிற்கும் தொடர்பில்லை.",
        "Incorrect. Presidential assent is still required.", "தவறானது. குடியரசுத் தலைவர் ஒப்புதல் இன்னமும் தேவைப்படுகிறது.",
        "Article 31B: Operates as an umbrella shield over laws placed in the Ninth Schedule.",
        "சரத்து 31B: ஒன்பதாவது அட்டவணையில் வைக்கப்பட்டுள்ள சட்டங்களுக்கு ஒரு குடை போன்ற பாதுகாப்பாக செயல்படுகிறது."
    ))

    # GT071
    qs.append(make_sch_q(
        "SCH_GT_071", "Hard", "Conceptual", "Ninth Schedule",
        "In which historic case did the Supreme Court first uphold the constitutional validity of the 1st Amendment Act, 1951, that created Article 31B and the Ninth Schedule?",
        "சரத்து 31B மற்றும் ஒன்பதாவது அட்டவணையை உருவாக்கிய 1951-ன் 1வது திருத்தச் சட்டத்தின் அரசியலமைப்புச் செல்லுபடியாகும் தன்மையை உச்சநீதிமன்றம் முதலில் உறுதிசெய்த வரலாற்று சிறப்புமிக்க வழக்கு எது?",
        "Shankari Prasad v. Union of India (1951)", "சங்கரி பிரசாத் எதிர் இந்திய யூனியன் (1951)",
        "Golak Nath v. State of Punjab (1967)", "கோலக் நாத் எதிர் பஞ்சாப் அரசு (1967)",
        "Kesavananda Bharati v. State of Kerala (1973)", "கேசவானந்த பாரதி எதிர் கேரள அரசு (1973)",
        "Minerva Mills v. Union of India (1980)", "மினர்வா மில்ஸ் எதிர் இந்திய யூனியன் (1980)",
        "A",
        "In Shankari Prasad v. Union of India (1951), a Constitution Bench upheld the 1st Constitutional Amendment Act, 1951, holding that Parliament's constituent power under Article 368 includes the power to amend Fundamental Rights and create the Ninth Schedule.",
        "சங்கரி பிரசாத் எதிர் இந்திய யூனியன் (1951) வழக்கில், அரசியலமைப்பு அமர்வு 1951-ன் 1வது திருத்தச் சட்டத்தை உறுதிசெய்தது; சரத்து 368-ன் கீழான பாராளுமன்றத்தின் அரசியலமைப்புத் திருத்தும் அதிகாரம் அடிப்படை உரிமைகளைத் திருத்துவதையும் ஒன்பதாவது அட்டவணையை உருவாக்குவதையும் உள்ளடக்கியது என்று தீர்ப்பளித்தது.",
        "Correct. Shankari Prasad (1951) was the first case validating 1st CAA and Ninth Schedule.", "சரியானது. சங்கரி பிரசாத் (1951) 1வது திருத்தம் மற்றும் 9வது அட்டவணையை உறுதிசெய்த முதல் வழக்கு.",
        "Incorrect. Golak Nath (1967) later held that Parliament cannot amend Fundamental Rights.", "தவறானது. கோலக் நாத் (1967) பாராளுமன்றம் அடிப்படை உரிமைகளைத் திருத்த முடியாது என்று தீர்ப்பளித்தது.",
        "Incorrect. Kesavananda Bharati (1973) introduced the Basic Structure doctrine.", "தவறானது. கேசவானந்த பாரதி (1973) அடிப்படை கட்டமைப்புக் கோட்பாட்டை அறிமுகப்படுத்தியது.",
        "Incorrect. Minerva Mills (1980) struck down clauses (4) and (5) of Article 368.", "தவறானது. மினர்வா மில்ஸ் (1980) சரத்து 368-ன் பிரிவுகள் (4) மற்றும் (5)-ஐ ரத்து செய்தது.",
        "Judicial Evolution: Shankari Prasad (1951: Upheld) -> Golak Nath (1967: Curtailed) -> Kesavananda (1973: Basic Structure) -> I.R. Coelho (2007: Judicial Review of Ninth Schedule).",
        "நீதித்துறை பரிணாமம்: சங்கரி பிரசாத் (1951: உறுதி) -> கோலக் நாத் (1967: கட்டுப்பாடு) -> கேசவானந்தா (1973: அடிப்படை கட்டமைப்பு) -> ஐ.ஆர். கோயல்ஹோ (2007: 9வது அட்டவணை நீதிப் புனராய்வு)."
    ))

    # GT072
    qs.append(make_sch_q(
        "SCH_GT_072", "Medium", "Conceptual", "Ninth Schedule",
        "In the landmark I.R. Coelho case (2007), which specific cut-off date was established by the Supreme Court for subjecting Ninth Schedule laws to judicial review under the Basic Structure doctrine?",
        "வரலாற்றுச் சிறப்புமிக்க ஐ.ஆர். கோயல்ஹோ வழக்கில் (2007), அடிப்படை கட்டமைப்புக் கோட்பாட்டின் கீழ் ஒன்பதாவது அட்டவணைச் சட்டங்களை நீதிப் புனராய்வுக்கு உட்படுத்துவதற்கு உச்சநீதிமன்றத்தால் நிர்ணயிக்கப்பட்ட குறிப்பிட்ட தேதி எது?",
        "April 24, 1973 (Date of the Kesavananda Bharati judgment)", "1973 ஏப்ரல் 24 (கேசவானந்த பாரதி தீர்ப்பு வழங்கப்பட்ட தேதி)",
        "January 26, 1950 (Commencement of the Constitution)", "1950 ஜனவரி 26 (அரசியலமைப்பு நடைமுறைக்கு வந்த தேதி)",
        "June 25, 1975 (Proclamation of National Emergency)", "1975 ஜூன் 25 (தேசிய அவசரநிலை பிரகடனம் செய்யப்பட்ட தேதி)",
        "November 16, 1992 (Date of the Indra Sawhney judgment)", "1992 நவம்பர் 16 (இந்திரா சஹானி தீர்ப்பு வழங்கப்பட்ட தேதி)",
        "A",
        "In I.R. Coelho v. State of Tamil Nadu (2007), a 9-judge Constitution Bench held that any law inserted into the Ninth Schedule on or after April 24, 1973 (the day Kesavananda Bharati was delivered) does not enjoy blanket immunity and is open to judicial review if it violates the basic structure of the Constitution.",
        "ஐ.ஆர். கோயல்ஹோ எதிர் தமிழ்நாடு அரசு (2007) வழக்கில், 9 நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வு, 1973 ஏப்ரல் 24-க்கு (கேசவானந்த பாரதி தீர்ப்பு வெளியான நாள்) பின்னரோ அல்லது அன்றோ ஒன்பதாவது அட்டவணையில் சேர்க்கப்பட்ட எந்தவொரு சட்டமும் முழுமையான விலக்குரிமையைப் பெறாது என்றும், அது அரசியலமைப்பின் அடிப்படைக் கட்டமைப்பை மீறினால் நீதிப் புனராய்வுக்கு உட்பட்டது என்றும் தீர்ப்பளித்தது.",
        "Correct. April 24, 1973 is the historic cut-off date established in I.R. Coelho.", "சரியானது. 1973 ஏப்ரல் 24 என்பது ஐ.ஆர். கோயல்ஹோ வழக்கில் நிர்ணயிக்கப்பட்ட வரலாற்றுத் தேதி.",
        "Incorrect. January 26, 1950 is commencement date, not the basic structure cut-off.", "தவறானது. 1950 ஜனவரி 26 என்பது அரசியலமைப்பு அமலுக்கு வந்த நாள்.",
        "Incorrect. June 25, 1975 is the declaration of Emergency.", "தவறானது. 1975 ஜூன் 25 என்பது அவசரநிலை பிரகடனத் தேதி.",
        "Incorrect. November 16, 1992 was the Mandal case ruling.", "தவறானது. 1992 நவம்பர் 16 மண்டல் வழக்கு தீர்ப்புத் தேதி.",
        "I.R. Coelho Ruling (2007): Laws added to Ninth Schedule post-April 24, 1973 can be challenged for violating Articles 14, 19, 21 and the Basic Structure.",
        "ஐ.ஆர். கோயல்ஹோ தீர்ப்பு (2007): 1973 ஏப்ரல் 24-க்குப் பின் ஒன்பதாவது அட்டவணையில் சேர்க்கப்பட்ட சட்டங்களை சரத்து 14, 19, 21 மற்றும் அடிப்படை கட்டமைப்பை மீறுவதாக சவால் செய்யலாம்."
    ))

    # GT073
    qs.append(make_sch_q(
        "SCH_GT_073", "Easy", "Conceptual", "Ninth Schedule",
        "Approximately how many legislative enactments and regulations are currently included in the Ninth Schedule of the Indian Constitution?",
        "இந்திய அரசியலமைப்பின் ஒன்பதாவது அட்டவணையில் தற்போது தோராயமாக எத்தனை சட்டமியற்றல்கள் மற்றும் ஒழுங்குமுறைகள் சேர்க்கப்பட்டுள்ளன?",
        "284 Acts and Regulations", "284 சட்டங்கள் மற்றும் ஒழுங்குமுறைகள்",
        "100 Acts and Regulations", "100 சட்டங்கள் மற்றும் ஒழுங்குமுறைகள்",
        "500 Acts and Regulations", "500 சட்டங்கள் மற்றும் ஒழுங்குமுறைகள்",
        "13 Acts and Regulations", "13 சட்டங்கள் மற்றும் ஒழுங்குமுறைகள்",
        "A",
        "The Ninth Schedule currently contains 284 legislative entries (laws, regulations, and amending acts), protected under Article 31B.",
        "ஒன்பதாவது அட்டவணை தற்போது சரத்து 31B-ன் கீழ் பாதுகாக்கப்பட்ட 284 சட்டப் பதிவுகளைக் (சட்டங்கள், ஒழுங்குமுறைகள் மற்றும் திருத்தச் சட்டங்கள்) கொண்டுள்ளது.",
        "Correct. Ninth Schedule has 284 entries.", "சரியானது. ஒன்பதாவது அட்டவணையில் 284 பதிவுகள் உள்ளன.",
        "Incorrect. 100 is far too low.", "தவறானது. 100 என்பது மிகவும் குறைவு.",
        "Incorrect. 500 is far too high.", "தவறானது. 500 என்பது மிகவும் அதிகம்.",
        "Incorrect. 13 was the initial 1951 count, not the current count.", "தவறானது. 13 என்பது 1951 தொடக்க எண்ணிக்கை, தற்போதைய எண்ணிக்கை அல்ல.",
        "Ninth Schedule Size: Grew from 13 in 1951 to 284 entries today through successive constitutional amendments.",
        "ஒன்பதாவது அட்டவணை அளவு: அடுத்தடுத்த திருத்தங்கள் மூலம் 1951-ல் 13-லிருந்து இன்று 284 பதிவுகளாக விரிவடைந்துள்ளது."
    ))

    # GT074
    qs.append(make_sch_q(
        "SCH_GT_074", "Medium", "Conceptual", "Ninth Schedule",
        "Which Tamil Nadu reservation legislation was inserted into the Ninth Schedule (as Entry 257A) by the 76th Constitutional Amendment Act, 1994, to protect it from judicial invalidation?",
        "நீதிமன்றத்தால் செல்லாததாக்கப்படுவதிலிருந்து பாதுகாக்க 76வது அரசியலமைப்புத் திருத்தச் சட்டம் 1994 மூலம் ஒன்பதாவது அட்டவணையில் (பதிவு 257A ஆக) சேர்க்கப்பட்ட தமிழக இடஒதுக்கீட்டுச் சட்டம் எது?",
        "Tamil Nadu Act 45 of 1994 (providing 69% reservation in educational institutions and government jobs)", "தமிழ்நாடு சட்டம் 45/1994 (கல்வி நிறுவனங்கள் மற்றும் அரசுப் பணிகளில் 69% இடஒதுக்கீடு வழங்கும் சட்டம்)",
        "Tamil Nadu Panchayats Act, 1994", "தமிழ்நாடு பஞ்சாயத்துகள் சட்டம், 1994",
        "Tamil Nadu Land Reforms (Fixation of Ceiling on Land) Act, 1961", "தமிழ்நாடு நிலச் சீர்திருத்தங்கள் (நில உச்சவரம்பு நிர்ணயம்) சட்டம், 1961",
        "Tamil Nadu Hindu Religious and Charitable Endowments Act, 1959", "தமிழ்நாடு இந்து சமய அறநிலையச் சட்டம், 1959",
        "A",
        "The Tamil Nadu Backward Classes, Scheduled Castes and Scheduled Tribes (Reservation of Seats in Educational Institutions and of Appointments or Posts in the Services under the State) Act, 1993 (TN Act 45 of 1994), which provides 69% reservation, was placed into the Ninth Schedule by the 76th CAA 1994.",
        "கல்வி நிறுவனங்கள் மற்றும் அரசுப் பணிகளில் 69% இடஒதுக்கீடு வழங்கும் தமிழ்நாடு பிற்படுத்தப்பட்டோர், பட்டியல் சாதிகள் மற்றும் பட்டியல் பழங்குடியினர் சட்டம் 1993 (1994-ன் தமிழ்நாடு சட்டம் 45), 1994-ன் 76வது திருத்தச் சட்டம் மூலம் ஒன்பதாவது அட்டவணையில் சேர்க்கப்பட்டது.",
        "Correct. TN Act 45 of 1994 (69% reservation) was shielded via 76th CAA 1994.", "சரியானது. தமிழ்நாடு சட்டம் 45/1994 (69% இடஒதுக்கீடு) 76வது திருத்தம் மூலம் பாதுகாக்கப்பட்டது.",
        "Incorrect. Panchayats Act is not in Ninth Schedule.", "தவறானது. பஞ்சாயத்துகள் சட்டம் ஒன்பதாவது அட்டவணையில் இல்லை.",
        "Incorrect. TN Land Reforms Act 1961 was added earlier by the 17th CAA 1964.", "தவறானது. நிலச் சீர்திருத்தச் சட்டம் 1964-ல் 17வது திருத்தம் மூலம் முன்பே சேர்க்கப்பட்டது.",
        "Incorrect. HR&CE Act is not entry 257A.", "தவறானது. அறநிலையச் சட்டம் பதிவு 257A அல்ல.",
        "Tamil Nadu 69% Reservation: Shielded under Ninth Schedule Entry 257A by the 76th Amendment Act, 1994.",
        "தமிழ்நாடு 69% இடஒதுக்கீடு: 1994-ன் 76வது திருத்தச் சட்டம் மூலம் ஒன்பதாவது அட்டவணை பதிவு 257A-ன் கீழ் பாதுகாக்கப்பட்டுள்ளது."
    ))

    # GT075
    qs.append(make_sch_q(
        "SCH_GT_075", "Hard", "Conceptual", "Ninth Schedule",
        "Under the Supreme Court's verdict in I.R. Coelho (2007), what dual test must be applied to determine whether a Ninth Schedule law is unconstitutional?",
        "ஐ.ஆர். கோயல்ஹோ வழக்கில் (2007) உச்சநீதிமன்றத்தின் தீர்ப்பின்படி, ஒரு ஒன்பதாவது அட்டவணைச் சட்டம் அரசியலமைப்பிற்கு முரணானதா என்பதைத் தீர்மானிக்க எந்த இரட்டைப் பரிசோதனை பயன்படுத்தப்பட வேண்டும்?",
        "The 'Rights Test' (whether fundamental rights are infringed) followed by the 'Essence of the Right / Basic Structure Test'", "'உரிமைகள் பரிசோதனை' (அடிப்படை உரிமைகள் மீறப்பட்டுள்ளதா) அதைத் தொடர்ந்து 'உரிமையின் சாரம் / அடிப்படை கட்டமைப்புக் கோட்பாட்டுப் பரிசோதனை'",
        "The 'Financial Viability Test' followed by the 'Comptroller Audit Certification'", "'நிதி சாத்தியக்கூறு பரிசோதனை' அதைத் தொடர்ந்து 'கணக்குத் தணிக்கையாளர் சான்றளிப்பு'",
        "The 'Legislative Competence Test' followed by a 'State Referendum Vote'", "'சட்டமன்றத் தகுதிப் பரிசோதனை' அதைத் தொடர்ந்து 'மாநில வாக்கெடுப்பு'",
        "The 'Preamble Conformity Test' followed by 'Law Commission Re-evaluation'", "'முகப்புரை இணக்கப் பரிசோதனை' அதைத் தொடர்ந்து 'சட்ட ஆணைய மறுமதிப்பீடு'",
        "A",
        "In I.R. Coelho (2007), the Supreme Court ruled that to test a post-1973 Ninth Schedule law, courts first apply the 'Rights Test' (has a fundamental right been violated?), and if so, apply the 'Essence of the Right Test' to determine if the violation touches the core basic structure of the Constitution.",
        "ஐ.ஆர். கோயல்ஹோ வழக்கில் (2007), உச்சநீதிமன்றம் தீர்ப்பளித்தது: 1973-க்குப் பிந்தைய ஒன்பதாவது அட்டவணைச் சட்டத்தை ஆராய, நீதிமன்றங்கள் முதலில் 'உரிமைகள் பரிசோதனை'யையும், மீறல் இருந்தால், அது அரசியலமைப்பின் அடிப்படைக் கட்டமைப்பைச் சிதைக்கிறதா என்பதை அறிய 'உரிமையின் சாராம்சப் பரிசோதனை'யையும் பயன்படுத்த வேண்டும்.",
        "Correct. The Rights Test and Essence of the Right (Basic Structure) Test are the dual standards.", "சரியானது. உரிமைகள் பரிசோதனை மற்றும் உரிமையின் சாரம் (அடிப்படை கட்டமைப்பு) பரிசோதனை ஆகியவையே இரட்டைத் தரநிலைகள்.",
        "Incorrect. Financial viability is not a constitutional review standard.", "தவறானது. நிதி சாத்தியக்கூறு அரசியலமைப்பு ஆய்வுத் தரம் அல்ல.",
        "Incorrect. India has no provision for state referendum on laws.", "தவறானது. இந்தியாவில் சட்டங்களின் மீது பொது வாக்கெடுப்புக்கு இடமில்லை.",
        "Incorrect. Law Commission does not perform judicial review.", "தவறானது. சட்ட ஆணையம் நீதிப் புனராய்வு செய்வதில்லை.",
        "I.R. Coelho Dual Test: (1) Rights Test + (2) Essence of the Right / Impact on Basic Structure Test.",
        "ஐ.ஆர். கோயல்ஹோ இரட்டைப் பரிசோதனை: (1) உரிமைகள் பரிசோதனை + (2) உரிமையின் சாரம் / அடிப்படைக் கட்டமைப்பு மீதான தாக்கப் பரிசோதனை."
    ))

    return qs

if __name__ == "__main__":
    qs = get_batch3()
    print(f"Batch 3 generated {len(qs)} questions.")
