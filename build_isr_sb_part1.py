# -*- coding: utf-8 -*-
"""
Builder for Inter-State Relations Statement-Based Part 1 (ISR_S_001 to ISR_S_025)
"""
import json
from gen_isr_statement_helper import make_q

def get_sb_part1():
    q = []

    # 001 - Ans A
    q.append(make_q(
        "ISR_S_001", "Medium",
        "Consider the following statements regarding the 'Full Faith and Credit' clause under Article 261 of the Constitution:\n1. Full faith and credit shall be given throughout the territory of India to public acts, records, and judicial proceedings of the Union and of every State.\n2. The clause extends equal constitutional evidentiary immunity to private commercial contracts executed between citizens of different States.\nWhich of the statements given above is/are correct?",
        "அரசியலமைப்பின் 261-வது உறுப்பின் கீழ் உள்ள 'முழு நம்பிக்கையும் சான்றும்' விதி தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. ஒன்றியம் மற்றும் ஒவ்வொரு மாநிலத்தின் பொதுச் சட்டங்கள், பதிவேடுகள் மற்றும் நீதித்துறை நடவடிக்கைகளுக்கு இந்தியா முழுவதும் முழு நம்பிக்கையும் சான்றும் வழங்கப்பட வேண்டும்.\n2. வெவ்வேறு மாநிலங்களின் குடிமக்களுக்கு இடையே நிறைவேற்றப்பட்ட தனியார் வணிக ஒப்பந்தங்களுக்கும் இந்த விதி சமமான அரசியலமைப்பு சான்றளிப்பு பாதுகாப்பை நீட்டிக்கிறது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "A",
        "Statement 1 is correct: Article 261(1) expressly mandates that full faith and credit shall be given throughout the territory of India to public acts, records, and judicial proceedings of the Union and of every State. Statement 2 is incorrect: The full faith and credit clause applies strictly to 'public' acts, official records, and judicial proceedings, and does not extend to private contracts between individuals.",
        "கூற்று 1 சரி: உறுப்பு 261(1) ஒன்றியம் மற்றும் ஒவ்வொரு மாநிலத்தின் பொதுச் சட்டங்கள், பதிவேடுகள் மற்றும் நீதித்துறை நடவடிக்கைகளுக்கு இந்தியா முழுவதும் முழு நம்பிக்கையும் சான்றும் அளிக்கப்பட வேண்டும் என்று தெளிவாகக் கூறுகிறது. கூற்று 2 தவறு: இந்த விதி பொதுச் சட்டங்கள் மற்றும் அதிகாரப்பூர்வ பதிவேடுகளுக்கு மட்டுமே பொருந்தும், தனியார் ஒப்பந்தங்களுக்குப் பொருந்தாது.",
        "Option A is correct because statement 1 accurately reflects Article 261(1) while statement 2 is legally erroneous.", "கூற்று 1 உறுப்பு 261(1)-ஐச் சரியாகக் குறிப்பிடுவதால் விருப்பம் A சரியானது.",
        "Option B is incorrect because statement 2 falsely claims private contracts fall under Article 261.", "விருப்பம் B தவறு, ஏனெனில் தனியார் ஒப்பந்தங்கள் உறுப்பு 261-ன் கீழ் வராது.",
        "Option C is incorrect because statement 2 is false.", "கூற்று 2 தவறாக இருப்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because statement 1 is an exact constitutional provision.", "கூற்று 1 சரியான அரசியலமைப்பு விதி என்பதால் விருப்பம் D தவறு.",
        "Remember that Article 261 applies only to PUBLIC acts, records, and judicial proceedings, never to private transactions.",
        "உறுப்பு 261 பொதுச் சட்டங்கள் மற்றும் பதிவேடுகளுக்கு மட்டுமே பொருந்தும் என்பதை நினைவில் கொள்க.",
        "Article 261(1) ensures territorial universality for public acts and judicial records of Union and States.",
        "உறுப்பு 261(1) ஒன்றியம் மற்றும் மாநிலங்களின் பொது நடவடிக்கைகளுக்கு நாடு தழுவிய அங்கீகாரத்தை உறுதி செய்கிறது.",
        tags=["Article 261", "Full Faith and Credit", "Constitutional Framework"]
    ))

    # 002 - Ans B
    q.append(make_q(
        "ISR_S_002", "Hard",
        "Consider the following statements regarding the execution of decrees and orders under Article 261(3) of the Constitution:\n1. Final judgments or orders delivered by civil or criminal courts in any part of India are capable of direct execution anywhere in the territory of India.\n2. The rule of direct execution under Article 261(3) applies exclusively to civil court decrees and orders, completely excluding penal or criminal sentences.\nWhich of the statements given above is/are correct?",
        "அரசியலமைப்பின் 261(3) உறுப்பின் கீழ் தீர்ப்பாணைகள் மற்றும் ஆணைகளை நிறைவேற்றுவது தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இந்தியாவின் எந்தப் பகுதியிலும் உள்ள உரிமையியல் அல்லது குற்றவியல் நீதிமன்றங்களால் வழங்கப்படும் இறுதித் தீர்ப்புகள் அல்லது ஆணைகள் இந்தியாவில் எங்கு வேண்டுமானாலும் நேரடியாக நிறைவேற்றப்படலாம்.\n2. உறுப்பு 261(3)-ன் கீழ் நேரடி நிறைவேற்ற விதி உரிமையியல் நீதிமன்றங்களின் தீர்ப்பாணைகளுக்கு மட்டுமே பொருந்தும், குற்றவியல் தண்டனைகளுக்குப் பொருந்தாது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "B",
        "Statement 1 is incorrect: Article 261(3) states that final judgments or orders delivered or passed by 'civil courts' in any part of the territory of India shall be capable of execution anywhere within that territory. It does not apply to criminal courts. Statement 2 is correct: Penal and criminal laws and decrees are excluded from the operation of the full faith and credit execution clause; a state does not execute the penal laws of another state.",
        "கூற்று 1 தவறு: உறுப்பு 261(3) உரிமையியல் நீதிமன்றங்களால் (civil courts) வழங்கப்படும் இறுதித் தீர்ப்புகள் மட்டுமே இந்தியா முழுவதும் நிறைவேற்றப்படத் தக்கவை எனக் கூறுகிறது. குற்றவியல் நீதிமன்றங்களுக்கு இது பொருந்தாது. கூற்று 2 சரி: தண்டனை மற்றும் குற்றவியல் சட்டங்களின் தீர்ப்புகளுக்கு இந்த விதி பொருந்தாது.",
        "Option A is incorrect because statement 1 mistakenly includes criminal courts.", "குற்றவியல் நீதிமன்றங்களையும் கூற்று 1 தவறாக உள்ளடக்கியுள்ளதால் விருப்பம் A தவறு.",
        "Option B is correct because statement 2 correctly identifies that Article 261(3) is confined to civil court judgments.", "உறுப்பு 261(3) உரிமையியல் நீதிமன்றத் தீர்ப்புகளுக்கு மட்டுமே பொருந்தும் என்பதை கூற்று 2 சரியாகக் குறிப்பிடுவதால் விருப்பம் B சரி.",
        "Option C is incorrect because statement 1 is inaccurate.", "கூற்று 1 தவறாக இருப்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because statement 2 is fully accurate.", "கூற்று 2 சரியானது என்பதால் விருப்பம் D தவறு.",
        "A classic TNPSC trap: Article 261(3) applies strictly to CIVIL court decrees, NOT criminal or penal decrees.",
        "TNPSC பொறி: உறுப்பு 261(3) உரிமையியல் (Civil) நீதிமன்றத் தீர்ப்புகளுக்கு மட்டுமே பொருந்தும், குற்றவியல் தீர்ப்புகளுக்கு அல்ல.",
        "Article 261(3) enables extra-territorial execution of civil court decrees according to law.",
        "உறுப்பு 261(3) உரிமையியல் நீதிமன்றத் தீர்ப்பாணைகளை மாநில எல்லைகளைத் தாண்டி நிறைவேற்ற வகை செய்கிறது.",
        tags=["Article 261(3)", "Civil Court Decrees", "Penal Law Exclusion"]
    ))

    # 003 - Ans C
    q.append(make_q(
        "ISR_S_003", "Medium",
        "Consider the following statements regarding the adjudication of inter-State water disputes under Article 262:\n1. Parliament may by law provide for the adjudication of any dispute or complaint with respect to the use, distribution, or control of the waters of any inter-State river or river valley.\n2. Parliament may by law exclude the jurisdiction of both the Supreme Court and any other court in respect of any such water dispute or complaint.\nWhich of the statements given above is/are correct?",
        "உறுப்பு 262-ன் கீழ் மாநிலங்களுக்கு இடையேயான நதிநீர் தகராறுகளைத் தீர்ப்பது தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. மாநிலங்களுக்கு இடையிலான நதி அல்லது நதிப் பள்ளத்தாக்கின் நீரைப் பயன்படுத்துதல், பகிர்ந்தளித்தல் அல்லது கட்டுப்படுத்துதல் தொடர்பான தகராறுகளைத் தீர்ப்பதற்கு நாடாளுமன்றம் சட்டத்தின் மூலம் வகை செய்யலாம்.\n2. அத்தகைய தகராறு அல்லது புகார் தொடர்பாக உச்ச நீதிமன்றம் மற்றும் பிற எந்த நீதிமன்றத்தின் அதிகார வரம்பையும் நாடாளுமன்றம் சட்டத்தின் மூலம் விலக்கலாம்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "C",
        "Both statements are correct: Under Article 262(1), Parliament is empowered to legislate for the adjudication of inter-state river water disputes. Under Article 262(2), Parliament may enact a law providing that neither the Supreme Court nor any other court shall exercise jurisdiction in respect of any such dispute or complaint.",
        "இரண்டு கூற்றுகளும் சரியானவை: உறுப்பு 262(1)-ன் கீழ் நதிநீர் தகராறுகளைத் தீர்க்க நாடாளுமன்றத்திற்குச் சட்டம் இயற்ற அதிகாரம் உண்டு. உறுப்பு 262(2)-ன் கீழ் உச்ச நீதிமன்றம் உட்பட எந்த நீதிமன்றத்தின் அதிகார வரம்பையும் விலக்க நாடாளுமன்றத்திற்கு அதிகாரம் உண்டு.",
        "Option A is incorrect because statement 2 is also an authentic provision of Article 262(2).", "கூற்று 2-ம் சரியான அரசியலமைப்பு விதி என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because statement 1 is equally correct under Article 262(1).", "கூற்று 1-ம் சரியானது என்பதால் விருப்பம் B தவறு.",
        "Option C is correct as both statements accurately articulate Article 262(1) and (2).", "இரண்டு கூற்றுகளும் உறுப்பு 262(1) மற்றும் (2)-ஐச் சரியாக விளக்குவதால் விருப்பம் C சரி.",
        "Option D is incorrect because both statements are factually and constitutionally true.", "இரண்டு கூற்றுகளும் உண்மையானவை என்பதால் விருப்பம் D தவறு.",
        "Article 262 is unique because it permits Parliament to completely bar the Supreme Court's jurisdiction.",
        "உறுப்பு 262 உச்ச நீதிமன்றத்தின் அதிகார வரம்பையே சட்டத்தின் மூலம் விலக்க நாடாளுமன்றத்திற்கு அதிகாரம் அளிக்கும் தனித்துவமான விதியாகும்.",
        "Article 262 empowers Parliament to adjudicate inter-state river disputes and bar all judicial interference.",
        "உறுப்பு 262 நதிநீர் தகராறுகளைத் தீர்க்கவும் அனைத்து நீதிமன்ற அதிகார வரம்பை விலக்கவும் நாடாளுமன்றத்திற்கு அதிகாரம் அளிக்கிறது.",
        tags=["Article 262", "River Water Disputes", "Supreme Court Bar"]
    ))

    # 004 - Ans D
    q.append(make_q(
        "ISR_S_004", "Hard",
        "Consider the following statements regarding the River Boards Act, 1956:\n1. River Boards established under the Act have binding statutory powers to adjudicate interstate water apportionment disputes between contesting States.\n2. The Central Government has successfully constituted over ten active River Boards under this Act for major rivers across India.\nWhich of the statements given above is/are correct?",
        "1956-ஆம் ஆண்டின் நதி வாரியங்கள் சட்டம் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இச்சட்டத்தின் கீழ் அமைக்கப்படும் நதி வாரியங்கள் மாநிலங்களுக்கு இடையிலான நதிநீர்ப் பகிர்வு தகராறுகளைத் தீர்க்கும் பிணைப்புள்ள சட்டப்பூர்வ அதிகாரத்தைக் கொண்டுள்ளன.\n2. மத்திய அரசு இச்சட்டத்தின் கீழ் இந்தியாவில் உள்ள முக்கிய நதிகளுக்காக பத்து தீவிர நதி வாரியங்களை வெற்றிகரமாக அமைத்துள்ளது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "D",
        "Both statements are incorrect: Statement 1 is incorrect because River Boards under the River Boards Act, 1956 are purely advisory bodies meant for regulation and development of inter-state rivers, not for binding dispute adjudication. Statement 2 is incorrect because in reality, no River Board has ever been constituted by the Central Government under the River Boards Act, 1956 till date.",
        "இரண்டு கூற்றுகளும் தவறானவை: கூற்று 1 தவறு, ஏனெனில் நதி வாரியங்கள் சட்டம் 1956-ன் கீழ் அமைக்கப்பட்ட வாரியங்கள் ஒழுங்குமுறை மற்றும் மேம்பாட்டிற்கான ஆலோசனைக் குழுக்களே தவிர, பிணைப்புள்ள தகராறு தீர்க்கும் அமைப்புகள் அல்ல. கூற்று 2 தவறு, ஏனெனில் நடைமுறையில் இச்சட்டத்தின் கீழ் இதுவரை எந்த ஒரு நதி வாரியமும் அமைக்கப்படவில்லை.",
        "Option A is incorrect because statement 1 is false.", "கூற்று 1 தவறாக இருப்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because statement 2 is false.", "கூற்று 2 தவறாக இருப்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because both statements are demonstrably false.", "இரண்டு கூற்றுகளும் தவறானவை என்பதால் விருப்பம் C தவறு.",
        "Option D is correct because River Boards are advisory, and astonishingly, zero River Boards have been constituted under the 1956 Act.",
        "நதி வாரியங்கள் ஆலோசனைக் குழுக்கள் மற்றும் இச்சட்டத்தின் கீழ் இதுவரை ஒரு வாரியமும் அமைக்கப்படவில்லை என்பதால் விருப்பம் D சரி.",
        "High-yield fact: No River Board has ever been established under the River Boards Act of 1956.",
        "முக்கிய உண்மை: 1956 நதி வாரியச் சட்டத்தின் கீழ் இதுவரை ஒரு நதி வாரியமும் மத்திய அரசால் அமைக்கப்படவில்லை.",
        "River Boards Act 1956 provides for advisory boards on inter-state rivers, but none has been constituted.",
        "1956 நதி வாரியங்கள் சட்டம் ஆலோசனைக் குழுக்களை ஏற்படுத்த வகை செய்தாலும், இதுவரை ஒன்று கூட அமைக்கப்படவில்லை.",
        tags=["River Boards Act 1956", "Entry 56 Union List", "Advisory Nature"]
    ))

    # 005 - Ans A
    q.append(make_q(
        "ISR_S_005", "Medium",
        "Consider the following statements regarding the Inter-State River Water Disputes (IRWD) Act, 1956:\n1. A water disputes tribunal is constituted by the Central Government only upon receiving a formal request/complaint from a State Government that a dispute cannot be resolved by negotiations.\n2. The members of an Inter-State River Water Disputes Tribunal are appointed by the President on the advice of the Prime Minister.\nWhich of the statements given above is/are correct?",
        "1956-ஆம் ஆண்டின் மாநிலங்களுக்கு இடையேயான நதிநீர் தகராறுகள் சட்டம் (IRWD Act) தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. பேச்சுவார்த்தை மூலம் தகராறைத் தீர்க்க முடியாது என்று மாநில அரசு அதிகாரப்பூர்வ கோரிக்கை/புகார் அளித்த பின்னரே மத்திய அரசு நதிநீர் தீர்ப்பாயத்தை அமைக்கிறது.\n2. மாநிலங்களுக்கு இடையிலான நதிநீர் தகராறுகள் தீர்ப்பாயத்தின் உறுப்பினர்கள் பிரதமரின் ஆலோசனையின் பேரில் குடியரசுத் தலைவரால் நியமிக்கப்படுகிறார்கள்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "A",
        "Statement 1 is correct: Under Section 4 of the IRWD Act, 1956, when a request is received from any State Government and the Central Government is of the opinion that the dispute cannot be settled by negotiations, it constitutes a Tribunal. Statement 2 is incorrect: Members of the Tribunal are nominated by the Chief Justice of India (from sitting or retired judges of the Supreme Court or High Courts), not by the President on PM's advice.",
        "கூற்று 1 சரி: IRWD சட்டம் பிரிவு 4-ன் படி, மாநில அரசின் கோரிக்கையைப் பெற்று பேச்சுவார்த்தை மூலம் தீர்க்க முடியாது என மத்திய அரசு கருதினால் தீர்ப்பாயத்தை அமைக்கும். கூற்று 2 தவறு: தீர்ப்பாய உறுப்பினர்களை இந்தியத் தலைமை நீதிபதி (CJI) பரிந்துரைக்கிறார், குடியரசுத் தலைவர் பிரதமரின் ஆலோசனையின் பேரில் நியமிப்பதில்லை.",
        "Option A is correct because statement 1 matches Section 4 while statement 2 misstates the appointing authority.", "கூற்று 1 சரியானது மற்றும் கூற்று 2 நியமன அதிகாரியைத் தவறாகக் குறிப்பிடுவதால் விருப்பம் A சரி.",
        "Option B is incorrect because Tribunal judges are nominated by the CJI.", "தீர்ப்பாய நீதிபதிகள் தலைமை நீதிபதியால் பரிந்துரைக்கப்படுவதால் விருப்பம் B தவறு.",
        "Option C is incorrect because statement 2 is false.", "கூற்று 2 தவறாக இருப்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because statement 1 is completely accurate.", "கூற்று 1 முற்றிலும் சரியானது என்பதால் விருப்பம் D தவறு.",
        "Crucial trap: The Chief Justice of India nominates Tribunal members, guaranteeing judicial independence.",
        "முக்கிய பொறி: நதிநீர் தீர்ப்பாயத்தின் உறுப்பினர்களை இந்தியத் தலைமை நீதிபதி (CJI) பரிந்துரைக்கிறார்.",
        "IRWD Act tribunals are formed by the Centre on state complaints, with members nominated by the CJI.",
        "மாநில அரசின் புகாரின் பேரில் மத்திய அரசால் தீர்ப்பாயம் அமைக்கப்படுகிறது; உறுப்பினர்களைத் தலைமை நீதிபதி நியமிக்கிறார்.",
        tags=["IRWD Act 1956", "Tribunal Constitution", "CJI Nomination"]
    ))

    # 006 - Ans B
    q.append(make_q(
        "ISR_S_006", "Hard",
        "Consider the following statements regarding the 2002 amendments to the Inter-State River Water Disputes Act, 1956:\n1. The amendment made it mandatory for the Central Government to establish a Tribunal within 6 months of receiving a dispute reference from any State.\n2. The amendment stipulated that a Tribunal must give its final decision within a period of three years, extendable by a maximum of two years by the Central Government.\nWhich of the statements given above is/are correct?",
        "1956-ஆம் ஆண்டின் மாநிலங்களுக்கு இடையேயான நதிநீர் தகராறுகள் சட்டத்தில் 2002-ல் செய்யப்பட்ட திருத்தங்கள் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. எந்தவொரு மாநிலத்திடமிருந்தும் கோரிக்கை பெறப்பட்ட 6 மாதங்களுக்குள் மத்திய அரசு தீர்ப்பாயத்தை அமைப்பதை இத்திருத்தம் கட்டாயமாக்கியது.\n2. ஒரு தீர்ப்பாயம் தனது இறுதித் தீர்ப்பை மூன்று ஆண்டுகளுக்குள் வழங்க வேண்டும் என்றும், மத்திய அரசால் அதிகபட்சமாக இரண்டு ஆண்டுகள் வரை நீட்டிக்கப்படலாம் என்றும் இத்திருத்தம் நிர்ணயித்தது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "B",
        "Statement 1 is incorrect: The 2002 amendment (based on Sarkaria Commission recommendations) introduced a timeline of one year (not 6 months) for the Central Government to refer the dispute to a tribunal once a request is received. Statement 2 is correct: Under Section 5(2) inserted by the 2002 amendment, the Tribunal shall investigate and forward its report within three years, which may be extended by the Central Government for a further period not exceeding two years.",
        "கூற்று 1 தவறு: 2002 திருத்தம் (சர்க்காரியா ஆணைய பரிந்துரைப்படி) மாநில அரசின் கோரிக்கை பெறப்பட்ட 1 வருடத்திற்குள் (6 மாதங்கள் அல்ல) தீர்ப்பாயத்திற்கு அனுப்ப வேண்டும் எனக் கூறுகிறது. கூற்று 2 சரி: பிரிவு 5(2)-ன் படி தீர்ப்பாயம் 3 ஆண்டுகளுக்குள் தனது அறிக்கையை அளிக்க வேண்டும்; தேவைப்பட்டால் மேலும் 2 ஆண்டுகள் வரை நீட்டிக்கப்படலாம்.",
        "Option A is incorrect because the statutory window for tribunal referral is 1 year, not 6 months.", "தீர்ப்பாய பரிந்துரைக்கான கால வரம்பு 1 ஆண்டு என்பதால் விருப்பம் A தவறு.",
        "Option B is correct because statement 2 precisely states the 3-year + 2-year award timeline.", "கூற்று 2 மூன்று ஆண்டுகள் + இரண்டு ஆண்டுகள் கால வரம்பைச் சரியாகக் குறிப்பிடுவதால் விருப்பம் B சரி.",
        "Option C is incorrect because statement 1 is inaccurate.", "கூற்று 1 தவறாக இருப்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because statement 2 is legally verified under the 2002 amendment.", "கூற்று 2 சட்டப்பூர்வமாகச் சரியானது என்பதால் விருப்பம் D தவறு.",
        "Key 2002 Amendment timelines: 1 year to constitute tribunal; 3 years to give award (+ up to 2 years extension).",
        "முக்கிய 2002 திருத்த கால வரம்புகள்: தீர்ப்பாயம் அமைக்க 1 ஆண்டு; தீர்ப்பு வழங்க 3 ஆண்டுகள் (+2 ஆண்டுகள் வரை நீட்டிப்பு).",
        "2002 IRWD amendment prescribed a 1-year referral timeline and a 3-year (+2 max) award timeline.",
        "2002 IRWD திருத்தம் 1 ஆண்டு தீர்ப்பாய அமைப்பு காலத்தையும், 3 ஆண்டுகள் (+2 அதிகபட்சம்) தீர்ப்பு காலத்தையும் நிர்ணயித்தது.",
        tags=["2002 Amendment", "IRWD Act Timelines", "Sarkaria Commission"]
    ))

    # 007 - Ans C
    q.append(make_q(
        "ISR_S_007", "Hard",
        "Consider the following statements regarding the legal status of an award published under the Inter-State River Water Disputes Act, 1956:\n1. Upon publication in the Official Gazette by the Central Government, the decision of the Tribunal has the same force as an order or decree of the Supreme Court.\n2. Despite the finality of the award and the bar under Section 11, the Supreme Court has ruled that it maintains jurisdiction under Article 136 to hear Special Leave Petitions against Tribunal awards.\nWhich of the statements given above is/are correct?",
        "1956-ஆம் ஆண்டின் மாநிலங்களுக்கு இடையேயான நதிநீர் தகராறுகள் சட்டத்தின் கீழ் வெளியிடப்படும் தீர்ப்பின் சட்டப்பூர்வ நிலை தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. மத்திய அரசால் அதிகாரப்பூர்வ அரசிதழில் வெளியிடப்பட்டவுடன், தீர்ப்பாயத்தின் முடிவு உச்ச நீதிமன்றத்தின் ஆணை அல்லது தீர்ப்பாணையின் அதே வலிமையைக் கொண்டிருக்கும்.\n2. தீர்ப்பின் இறுடித்தன்மை மற்றும் பிரிவு 11-ன் கீழான தடை இருந்தபோதிலும், தீர்ப்பாயத்தின் முடிவுகளுக்கு எதிராக சிறப்பு விடுப்பு மனுக்களை (SLP) விசாரிக்க உறுப்பு 136-ன் கீழ் தனக்கு அதிகாரம் உள்ளது என்று உச்ச நீதிமன்றம் தீர்ப்பளித்துள்ளது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "C",
        "Both statements are correct: Statement 1 is correct: As per Section 6(2) of the IRWD Act (inserted via the 2002 amendment), the decision of the Tribunal, upon publication in the Official Gazette, has the same force as an order or decree of the Supreme Court. Statement 2 is correct: In the landmark Cauvery Water Disputes case (State of Karnataka v. State of Tamil Nadu, 2018), a 3-judge bench headed by CJI Dipak Misra affirmed that Article 136 is an overarching constitutional power that cannot be ousted by statutory bars under Section 11 of the 1956 Act.",
        "இரண்டு கூற்றுகளும் சரியானவை: கூற்று 1 சரி: IRWD சட்டம் பிரிவு 6(2)-ன் படி (2002 திருத்தம்), அரசிதழில் வெளியானவுடன் தீர்ப்பாய முடிவு உச்ச நீதிமன்ற ஆணைக்கு சமமான வலிமை பெறுகிறது. கூற்று 2 சரி: காவிரி வழக்கில் (2018), உறுப்பு 136-ன் கீழான உச்ச நீதிமன்றத்தின் சிறப்பு விடுப்பு மனு அதிகாரத்தை சாதாரண சட்டப் பிரிவால் (பிரிவு 11) தடுக்க முடியாது எனத் தீர்ப்பளிக்கப்பட்டது.",
        "Option A is incorrect because statement 2 is also a verified constitutional reality established in the 2018 Cauvery judgment.", "கூற்று 2-ம் 2018 காவிரி தீர்ப்பில் உறுதிப்படுத்தப்பட்ட உண்மை என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because statement 1 reflects statutory Section 6(2).", "கூற்று 1 சட்டப் பிரிவு 6(2)-ஐக் குறிப்பிடுவதால் விருப்பம் B தவறு.",
        "Option C is correct as both statutory equivalence to an SC decree and Article 136 reviewability are legally sound.", "இரண்டு கூற்றுகளும் சட்டப்பூர்வமாகச் சரியானவை என்பதால் விருப்பம் C சரி.",
        "Option D is incorrect because both statements are true.", "இரண்டு கூற்றுகளும் உண்மையானவை என்பதால் விருப்பம் D தவறு.",
        "Remember: Gazetted award = SC decree (Section 6(2)), but Supreme Court can still hear SLPs under Article 136!",
        "நினைவில் கொள்க: அரசிதழில் வெளியான தீர்ப்பு = உச்ச நீதிமன்ற ஆணை (பிரிவு 6(2)), ஆனால் உறுப்பு 136-ன் கீழ் SLP விசாரிக்க உச்ச நீதிமன்றத்திற்கு அதிகாரம் உண்டு!",
        "Gazetted IRWD awards hold Supreme Court decree status, subject to Article 136 review.",
        "அரசிதழில் வெளியான நதிநீர் தீர்ப்பு உச்ச நீதிமன்ற ஆணைக்கு நிகரானது; உறுப்பு 136-ன் கீழ் மறுஆய்வுக்கு உட்பட்டது.",
        tags=["Award Legal Status", "Article 136", "Cauvery Judgment 2018"]
    ))

    # 008 - Ans D
    q.append(make_q(
        "ISR_S_008", "Hard",
        "Consider the following statements regarding the jurisdictional interplay between Article 131 and Article 262:\n1. A State can invoke the original jurisdiction of the Supreme Court under Article 131 to determine inter-State river water allocations even if a law under Article 262 is in operation.\n2. The exclusion of court jurisdiction under Article 262(2) automatically applies to all interstate disputes, requiring no specific enactment of parliamentary legislation.\nWhich of the statements given above is/are correct?",
        "உறுப்பு 131 மற்றும் உறுப்பு 262 ஆகியவற்றுக்கு இடையேயான அதிகார வரம்புத் தொடர்பு தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. உறுப்பு 262-ன் கீழான ஒரு சட்டம் நடைமுறையில் இருந்தாலும், மாநிலங்களுக்கு இடையிலான நதிநீர்ப் பகிர்வை தீர்மானிக்க ஒரு மாநிலம் உறுப்பு 131-ன் கீழ் உச்ச நீதிமன்றத்தின் மூல அதிகார வரம்பை நாடலாம்.\n2. உறுப்பு 262(2)-ன் கீழ் நீதிமன்ற அதிகார வரம்பு விலக்கு என்பது அனைத்து மாநிலங்களுக்கிடையேயான தகராறுகளுக்கும் தானாகவே பொருந்தும்; இதற்கு நாடாளுமன்றத்தின் தனிச் சட்டம் எதுவும் தேவையில்லை.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "D",
        "Both statements are incorrect: Statement 1 is incorrect: Article 131 begins with 'Subject to the provisions of this Constitution...', which means Article 131 original jurisdiction is expressly excluded when Parliament enacts a law under Article 262 barring court jurisdiction. Statement 2 is incorrect: Article 262(2) does not automatically exclude jurisdiction; it states 'Parliament may by law provide...', meaning jurisdiction is barred only when Parliament specifically enacts legislation containing an ouster clause (such as Section 11 of IRWD Act, 1956).",
        "இரண்டு கூற்றுகளும் தவறானவை: கூற்று 1 தவறு: உறுப்பு 131 'இந்த அரசியலமைப்பின் விதிகளுக்கு உட்பட்டு' தொடங்குகிறது, எனவே உறுப்பு 262-ன் கீழ் நாடாளுமன்றம் சட்டம் இயற்றியிருந்தால் உறுப்பு 131 மூல அதிகார வரம்பு செயல்படாது. கூற்று 2 தவறு: உறுப்பு 262(2) நீதிமன்ற வரம்பைத் தானாகவே விலக்காது; நாடாளுமன்றம் சட்டத்தின் மூலம் விலக்கினால் மட்டுமே வரம்பு விலக்கப்படும்.",
        "Option A is incorrect because Article 131 is subordinate to Article 262.", "உறுப்பு 131 உறுப்பு 262-க்கு உட்பட்டது என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because court exclusion requires explicit parliamentary legislation.", "நீதிமன்ற அதிகார வரம்பு விலக்குக்கு நாடாளுமன்றச் சட்டம் தேவைப்படுவதால் விருப்பம் B தவறு.",
        "Option C is incorrect because both statements misrepresent constitutional interaction.", "இரண்டு கூற்றுகளும் அரசியலமைப்பு விதிகளைத் தவறாகச் சித்தரிப்பதால் விருப்பம் C தவறு.",
        "Option D is correct because both statements are legally false.", "இரண்டு கூற்றுகளும் சட்டப்படி தவறானவை என்பதால் விருப்பம் D சரி.",
        "Article 131 is 'Subject to the provisions of this Constitution', making it subordinate to Article 262 ouster laws.",
        "உறுப்பு 131 அரசியலமைப்பு விதிகளுக்கு உட்பட்டது என்பதால் அது உறுப்பு 262-ன் கீழ் இயற்றப்படும் சட்டங்களுக்குக் கட்டுப்பட்டது.",
        "Article 131 original jurisdiction is barred in water disputes only when Parliament explicitly enacts a law under Article 262.",
        "உறுப்பு 262-ன் கீழ் நாடாளுமன்றம் தெளிவாகச் சட்டம் இயற்றினால் மட்டுமே நதிநீர் தகராறுகளில் உறுப்பு 131 வரம்பு தடுக்கப்படும்.",
        tags=["Article 131", "Article 262 Interplay", "Original Jurisdiction Bar"]
    ))

    # 009 - Ans A
    q.append(make_q(
        "ISR_S_009", "Medium",
        "Consider the following statements regarding the Cauvery Water Management Scheme notified in 2018:\n1. The Scheme established two bodies: the Cauvery Water Management Authority (CWMA) and the Cauvery Water Regulation Committee (CWRC).\n2. The Cauvery basin covers territories in three States (Tamil Nadu, Karnataka, Kerala) and two Union Territories (Puducherry and Lakshadweep).\nWhich of the statements given above is/are correct?",
        "2018-ல் அறிவிக்கப்பட்ட காவிரி நீர் மேலாண்மைத் திட்டம் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இத்திட்டம் காவிரி நீர் மேலாண்மை ஆணையம் (CWMA) மற்றும் காவிரி நீர் ஒழுங்குமுறைக் குழு (CWRC) ஆகிய இரண்டு அமைப்புகளை நிறுவியது.\n2. காவிரி வடிநிலப் பகுதி மூன்று மாநிலங்கள் (தமிழ்நாடு, கர்நாடகா, கேரளா) மற்றும் இரண்டு யூனியன் பிரதேசங்களின் (புதுச்சேரி மற்றும் லட்சத்தீவு) பகுதிகளை உள்ளடக்கியது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "A",
        "Statement 1 is correct: In June 2018, following the Supreme Court directive, the Central Government notified the Cauvery Water Management Scheme constituting the CWMA and CWRC. Statement 2 is incorrect: The Cauvery basin spans three States (Tamil Nadu, Karnataka, Kerala) and ONLY ONE Union Territory (Puducherry, Karaikal region). Lakshadweep is an island territory with no connection to the Cauvery basin.",
        "கூற்று 1 சரி: ஜூன் 2018-ல் உச்ச நீதிமன்ற உத்தரவுப்படி மத்திய அரசு CWMA மற்றும் CWRC ஆகியவற்றை நிறுவியது. கூற்று 2 தவறு: காவிரி வடிநிலம் தமிழ்நாடு, கர்நாடகா, கேரளா மற்றும் ஒரே ஒரு யூனியன் பிரதேசமான புதுச்சேரியை (காரைக்கால்) மட்டுமே உள்ளடக்கியது. லட்சத்தீவுக்கு இதனுடன் தொடர்பில்லை.",
        "Option A is correct because statement 1 is accurate and statement 2 erroneously adds Lakshadweep.", "கூற்று 1 சரியானது மற்றும் கூற்று 2 லட்சத்தீவைத் தவறாகச் சேர்த்துள்ளதால் விருப்பம் A சரி.",
        "Option B is incorrect because Lakshadweep is not a riparian territory.", "லட்சத்தீவு வடிநிலப் பகுதி அல்ல என்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because statement 2 is false.", "கூற்று 2 தவறாக இருப்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because statement 1 is factually true.", "கூற்று 1 உண்மையானது என்பதால் விருப்பம் D தவறு.",
        "Riparian units in Cauvery: Tamil Nadu, Karnataka, Kerala, and Puducherry (4 entities total).",
        "காவிரி வடிநிலப் பகுதிகள்: தமிழ்நாடு, கர்நாடகா, கேரளா மற்றும் புதுச்சேரி (மொத்தம் 4 பகுதிகள்).",
        "Cauvery Water Management Authority (CWMA) was constituted in 2018 covering TN, KA, KL, and PY.",
        "காவிரி நீர் மேலாண்மை ஆணையம் (CWMA) 2018-ல் தமிழ்நாடு, கர்நாடகா, கேரளா, புதுச்சேரியை உள்ளடக்கி அமைக்கப்பட்டது.",
        tags=["Cauvery Dispute", "CWMA 2018", "Riparian States"]
    ))

    # 010 - Ans A
    q.append(make_q(
        "ISR_S_010", "Hard",
        "Consider the following statements regarding the Krishna Water Disputes Tribunals:\n1. The First Krishna Water Disputes Tribunal (KWDT-I) was constituted in 1969 under the chairmanship of Justice R.S. Bachawat.\n2. The Second Krishna Water Disputes Tribunal (KWDT-II) was constituted in 2004 under the chairmanship of Justice Brijesh Kumar and dealt with Maharashtra, Karnataka, and unified Andhra Pradesh.\nWhich of the statements given above is/are correct?",
        "கிருஷ்ணா நதிநீர் தகராறுகள் தீர்ப்பாயங்கள் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. முதல் கிருஷ்ணா நதிநீர் தகராறுகள் தீர்ப்பாயம் (KWDT-I) 1969-ல் நீதிபதி ஆர்.எஸ். பச்சாவத் தலைமையில் அமைக்கப்பட்டது.\n2. இரண்டாவது கிருஷ்ணா நதிநீர் தகராறுகள் தீர்ப்பாயம் (KWDT-II) 2004-ல் நீதிபதி பிரிஜேஷ் குமார் தலைமையில் அமைக்கப்பட்டு மகாராஷ்டிரா, கர்நாடகா மற்றும் ஒருங்கிணைந்த ஆந்திரப் பிரதேசம் இடையே செயல்பட்டது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "2 only", "2 மட்டும்",
        "1 only", "1 மட்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "A",
        "Both statements are correct: KWDT-I was constituted in April 1969 headed by Justice R.S. Bachawat and gave its final award in 1976. KWDT-II was constituted in April 2004 under Justice Brijesh Kumar to allocate Krishna waters among Maharashtra, Karnataka, and Andhra Pradesh (subsequently extended after Telangana formation).",
        "இரண்டு கூற்றுகளும் சரியானவை: KWDT-I 1969 ஏப்ரலில் நீதிபதி ஆர்.எஸ். பச்சாவத் தலைமையில் அமைக்கப்பட்டு 1976-ல் இறுதித் தீர்ப்பை வழங்கியது. KWDT-II 2004 ஏப்ரலில் நீதிபதி பிரிஜேஷ் குமார் தலைமையில் மகாராஷ்டிரா, கர்நாடகா மற்றும் ஆந்திரா இடையே அமைக்கப்பட்டது.",
        "Option A is correct as both Bachawat Tribunal (1969) and Brijesh Kumar Tribunal (2004) are historically and legally accurate.", "பச்சாவத் தீர்ப்பாயம் (1969) மற்றும் பிரிஜேஷ் குமார் தீர்ப்பாயம் (2004) ஆகிய இரண்டும் சரியானவை என்பதால் விருப்பம் A சரி.",
        "Option B is incorrect because statement 1 is also completely true.", "கூற்று 1-ம் முற்றிலும் உண்மை என்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because statement 2 is also completely true.", "கூற்று 2-ம் முற்றிலும் உண்மை என்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because neither statement is false.", "எந்தக் கூற்றும் தவறானது அல்ல என்பதால் விருப்பம் D தவறு.",
        "KWDT-I = R.S. Bachawat (1969); KWDT-II = Brijesh Kumar (2004). Memorize both chairpersons.",
        "KWDT-I = ஆர்.எஸ். பச்சாவத் (1969); KWDT-II = பிரிஜேஷ் குமார் (2004). இரண்டையும் நினைவில் கொள்க.",
        "Krishna Water Disputes Tribunals were chaired by Justice Bachawat (1969) and Justice Brijesh Kumar (2004).",
        "கிருஷ்ணா நதிநீர் தீர்ப்பாயங்கள் நீதிபதி பச்சாவத் (1969) மற்றும் நீதிபதி பிரிஜேஷ் குமார் (2004) தலைமையில் அமைக்கப்பட்டன.",
        tags=["Krishna Tribunal", "KWDT I & II", "Bachawat and Brijesh Kumar"]
    ))

    # 011 - Ans C
    q.append(make_q(
        "ISR_S_011", "Medium",
        "Consider the following statements regarding the Godavari Water Disputes Tribunal (GWDT):\n1. The Godavari Water Disputes Tribunal was constituted in April 1969 under the chairmanship of Justice R.S. Bachawat.\n2. The dispute involved the States of Maharashtra, Andhra Pradesh, Madhya Pradesh, Chhattisgarh, Odisha, and Karnataka.\nWhich of the statements given above is/are correct?",
        "கோதாவரி நதிநீர் தகராறுகள் தீர்ப்பாயம் (GWDT) தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. கோதாவரி நதிநீர் தகராறுகள் தீர்ப்பாயம் 1969 ஏப்ரலில் நீதிபதி ஆர்.எஸ். பச்சாவத் தலைமையில் அமைக்கப்பட்டது.\n2. இந்தத் தகராறில் மகாராஷ்டிரா, ஆந்திரப் பிரதேசம், மத்தியப் பிரதேசம், சத்தீஸ்கர், ஒடிசா மற்றும் கர்நாடகா ஆகிய மாநிலங்கள் ஈடுபட்டன.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "C",
        "Both statements are correct: Statement 1 is correct: The GWDT was constituted in April 1969 simultaneously with the Krishna Tribunal under Justice R.S. Bachawat. Statement 2 is correct: The riparian States involved were Maharashtra, Andhra Pradesh, Madhya Pradesh (later Chhattisgarh), Odisha, and Karnataka.",
        "இரண்டு கூற்றுகளும் சரியானவை: கூற்று 1 சரி: கோதாவரி தீர்ப்பாயம் 1969 ஏப்ரலில் நீதிபதி ஆர்.எஸ். பச்சாவத் தலைமையில் அமைக்கப்பட்டது. கூற்று 2 சரி: இதில் மகாராஷ்டிரா, ஆந்திரா, மத்தியப் பிரதேசம் (பின்னர் சத்தீஸ்கர்), ஒடிசா மற்றும் கர்நாடகா ஆகியவை வடிநில மாநிலங்களாகப் பங்கேற்றன.",
        "Option A is incorrect because statement 2 is equally valid.", "கூற்று 2-ம் சரியானது என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because statement 1 is equally valid.", "கூற்று 1-ம் சரியானது என்பதால் விருப்பம் B தவறு.",
        "Option C is correct because both statements accurately describe the Godavari Tribunal.", "இரண்டு கூற்றுகளும் கோதாவரி தீர்ப்பாயத்தைச் சரியாக விளக்குவதால் விருப்பம் C சரி.",
        "Option D is incorrect because neither statement is inaccurate.", "எந்தக் கூற்றும் தவறானது அல்ல என்பதால் விருப்பம் D தவறு.",
        "Justice R.S. Bachawat simultaneously headed both the Krishna and Godavari Water Disputes Tribunals from 1969.",
        "நீதிபதி ஆர்.எஸ். பச்சாவத் 1969-ல் கிருஷ்ணா மற்றும் கோதாவரி ஆகிய இரண்டு தீர்ப்பாயங்களுக்கும் ஒரே நேரத்தில் தலைமை தாங்கினார்.",
        "Godavari Tribunal was established in 1969 under Justice Bachawat covering six riparian states.",
        "கோதாவரி தீர்ப்பாயம் 1969-ல் நீதிபதி பச்சாவத் தலைமையில் ஆறு மாநிலங்களை உள்ளடக்கி அமைக்கப்பட்டது.",
        tags=["Godavari Tribunal", "Justice Bachawat", "Inter-State Rivers"]
    ))

    # 012 - Ans D
    q.append(make_q(
        "ISR_S_012", "Hard",
        "Consider the following statements regarding the Narmada Water Disputes Tribunal (NWDT):\n1. Rajasthan was excluded from receiving any share of Narmada waters because it is strictly a non-riparian State.\n2. The Narmada Water Disputes Tribunal was constituted under the chairmanship of Justice Chittatosh Mookerjee in 1990.\nWhich of the statements given above is/are correct?",
        "நர்மதா நதிநீர் தகராறுகள் தீர்ப்பாயம் (NWDT) தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. ராஜஸ்தான் நர்மதா வடிநில மாநிலம் அல்லாததால் (non-riparian), நர்மதா நீரில் எந்தப் பங்கும் பெறாமல் முற்றிலுமாக விலக்கப்பட்டது.\n2. நர்மதா நதிநீர் தகராறுகள் தீர்ப்பாயம் 1990-ல் நீதிபதி சிட்டதோஷ் முகர்ஜி தலைமையில் அமைக்கப்பட்டது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "D",
        "Both statements are incorrect: Statement 1 is incorrect: Even though Rajasthan is non-riparian to the Narmada basin, the NWDT award allocated 0.50 Million Acre Feet (MAF) of Narmada water to Rajasthan (for arid regions of Barmer and Jalore) pursuant to an interstate agreement. Statement 2 is incorrect: The NWDT was constituted in October 1969 under Justice V. Ramaswami, not Chittatosh Mookerjee (who chaired the Cauvery Tribunal in 1990).",
        "இரண்டு கூற்றுகளும் தவறானவை: கூற்று 1 தவறு: ராஜஸ்தான் வடிநில மாநிலமாக இல்லாவிட்டாலும், மாநிலங்களுக்கு இடையேயான உடன்படிக்கையின்படி NWDT ராஜஸ்தானுக்கு 0.50 MAF தண்ணீரை ஒதுக்கியது. கூற்று 2 தவறு: நர்மதா தீர்ப்பாயம் 1969-ல் நீதிபதி வி. ராமசுவாமி தலைமையில் அமைக்கப்பட்டது; சிட்டதோஷ் முகர்ஜி 1990-ல் காவிரி தீர்ப்பாயத்திற்குத் தலைமை தாங்கினார்.",
        "Option A is incorrect because Rajasthan received 0.50 MAF of Narmada waters.", "ராஜஸ்தானுக்கு நர்மதா நீரில் 0.50 MAF நீர் ஒதுக்கப்பட்டதால் விருப்பம் A தவறு.",
        "Option B is incorrect because NWDT was constituted in 1969 under Justice V. Ramaswami.", "நர்மதா தீர்ப்பாயம் 1969-ல் நீதிபதி வி. ராமசுவாமி தலைமையில் அமைக்கப்பட்டதால் விருப்பம் B தவறு.",
        "Option C is incorrect because both statements are factually flawed.", "இரண்டு கூற்றுகளும் தவறானவை என்பதால் விருப்பம் C தவறு.",
        "Option D is correct as both statements contain clear historical and factual errors.", "இரண்டு கூற்றுகளும் தவறான தகவல்களைக் கொண்டுள்ளதால் விருப்பம் D சரி.",
        "Rajasthan got Narmada water despite being non-riparian; NWDT was headed by Justice V. Ramaswami (1969).",
        "வடிநில மாநிலமாக இல்லாவிட்டாலும் ராஜஸ்தானுக்கு நர்மதா நீர் கிடைத்தது; NWDT 1969-ல் நீதிபதி வி. ராமசுவாமி தலைமையில் அமைக்கப்பட்டது.",
        "NWDT was set up in 1969 under Justice V. Ramaswami, allocating water to MP, GJ, MH, and RJ.",
        "நர்மதா தீர்ப்பாயம் 1969-ல் நீதிபதி வி. ராமசுவாமி தலைமையில் மத்திய பிரதேசம், குஜராத், மகாராஷ்டிரா, ராஜஸ்தானுக்கு நீர் ஒதுக்கியது.",
        tags=["Narmada Tribunal", "NWDT 1969", "Non-Riparian Allocation"]
    ))

    # 013 - Ans A
    q.append(make_q(
        "ISR_S_013", "Medium",
        "Consider the following statements regarding the Ravi and Beas Waters Tribunal:\n1. The Ravi and Beas Waters Tribunal was constituted in April 1986 under the chairmanship of Justice V. Balakrishna Eradi pursuant to the Rajiv–Longowal Accord (Punjab Accord).\n2. The dispute over Ravi and Beas waters involves the States of Punjab, Haryana, and Himachal Pradesh only, excluding Rajasthan.\nWhich of the statements given above is/are correct?",
        "ராவி மற்றும் பியாஸ் நதிநீர் தீர்ப்பாயம் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. ராவி மற்றும் பியாஸ் நதிநீர் தீர்ப்பாயம் ராஜீவ்-லாங்கோவால் ஒப்பந்தத்தின் (பஞ்சாப் ஒப்பந்தம்) அடிப்படையில் 1986 ஏப்ரலில் நீதிபதி வி. பாலகிருஷ்ணா எராடி தலைமையில் அமைக்கப்பட்டது.\n2. ராவி மற்றும் பியாஸ் நதிநீர் தகராறு பஞ்சாப், ஹரியானா மற்றும் இமாச்சலப் பிரதேசம் ஆகிய மாநிலங்களை மட்டுமே உள்ளடக்கியது; ராஜஸ்தான் இதில் சேர்க்கப்படவில்லை.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "A",
        "Statement 1 is correct: Following the Rajiv-Longowal Punjab Accord of July 1985, the Ravi and Beas Waters Tribunal was set up in April 1986 under Justice V. Balakrishna Eradi. Statement 2 is incorrect: Rajasthan is a major beneficiary and party to the Ravi and Beas water allocation along with Punjab and Haryana.",
        "கூற்று 1 சரி: 1985 ஜூலை ராஜீவ்-லாங்கோவால் பஞ்சாப் ஒப்பந்தத்தைத் தொடர்ந்து, 1986 ஏப்ரலில் நீதிபதி வி. பாலகிருஷ்ணா எராடி தலைமையில் தீர்ப்பாயம் அமைக்கப்பட்டது. கூற்று 2 தவறு: பஞ்சாப் மற்றும் ஹரியானாவுடன் ராஜஸ்தானும் ராவி-பியாஸ் நீர் பகிர்வில் ஒரு முக்கிய பங்குதாரர் மாநிலமாகும்.",
        "Option A is correct because statement 1 accurately reflects the 1986 Eradi Tribunal and statement 2 falsely omits Rajasthan.", "கூற்று 1 எராடி தீர்ப்பாயத்தைச் சரியாகக் குறிப்பிடுகிறது, ஆனால் கூற்று 2 ராஜஸ்தானைத் தவறாக நீக்கியுள்ளது என்பதால் விருப்பம் A சரி.",
        "Option B is incorrect because Rajasthan is deeply involved in the Ravi-Beas dispute.", "ராவி-பியாஸ் விவகாரத்தில் ராஜஸ்தானுக்கு முக்கிய பங்குண்டு என்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because statement 2 is false.", "கூற்று 2 தவறாக இருப்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because statement 1 is factually verified.", "கூற்று 1 சரிபார்க்கப்பட்ட உண்மை என்பதால் விருப்பம் D தவறு.",
        "The Eradi Tribunal (1986) was formed under the Rajiv-Longowal Accord for Punjab, Haryana, and Rajasthan.",
        "எராடி தீர்ப்பாயம் (1986) ராஜீவ்-லாங்கோவால் ஒப்பந்தத்தின் கீழ் பஞ்சாப், ஹரியானா, ராஜஸ்தானுக்காக அமைக்கப்பட்டது.",
        "Ravi and Beas Tribunal was constituted in 1986 headed by Justice V. Balakrishna Eradi.",
        "ராவி மற்றும் பியாஸ் தீர்ப்பாயம் 1986-ல் நீதிபதி வி. பாலகிருஷ்ணா எராடி தலைமையில் அமைக்கப்பட்டது.",
        tags=["Ravi Beas Tribunal", "Eradi Commission", "Punjab Accord"]
    ))

    # 014 - Ans B
    q.append(make_q(
        "ISR_S_014", "Hard",
        "Consider the following statements regarding the Mahadayi (Mandovi) Water Disputes Tribunal:\n1. The Mahadayi Water Disputes Tribunal was constituted in November 2010 to resolve water sharing disputes between Goa, Karnataka, and Kerala.\n2. The dispute specifically centers around Karnataka's Kalasa-Banduri Nala project aimed at diverting Mahadayi water to the Malaprabha river basin for drinking needs.\nWhich of the statements given above is/are correct?",
        "மகதாயி (மாண்டோவி) நதிநீர் தகராறுகள் தீர்ப்பாயம் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. மகதாயி நதிநீர் தகராறுகள் தீர்ப்பாயம் கோவா, கர்நாடகா மற்றும் கேரளா இடையே நதிநீர்ப் பகிர்வு சிக்கலைத் தீர்க்க 2010 நவம்பரில் அமைக்கப்பட்டது.\n2. இத்தகராறு குடிநீர் தேவைகளுக்காக மகதாயி நதிநீரை மலபிரபா நதி வடிநிலத்திற்குத் திருப்பிவிடும் கர்நாடகாவின் கலசா-பண்டூரி நாலா திட்டத்தை மையமாகக் கொண்டுள்ளது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "B",
        "Statement 1 is incorrect: The Mahadayi dispute involves Goa, Karnataka, and MAHARASHTRA, not Kerala. Statement 2 is correct: The core issue was Karnataka's Kalasa-Banduri Nala drinking water project diverting Mahadayi waters to the parched Hubballi-Dharwad region via the Malaprabha basin, which Goa strongly opposed on ecological grounds.",
        "கூற்று 1 தவறு: மகதாயி தகராறு கோவா, கர்நாடகா மற்றும் மகாராஷ்டிரா இடையே உள்ளதே தவிர, கேரளாவுடன் அல்ல. கூற்று 2 சரி: குடிநீர் தேவைகளுக்காக மலபிரபா வடிநிலத்திற்கு நீரைக் கொண்டு செல்லும் கலசா-பண்டூரி நாலா திட்டமே இத்தகராறின் மையப் புள்ளியாகும்.",
        "Option A is incorrect because Kerala is not a riparian party to the Mahadayi river.", "கேரளா மகதாயி வடிநில மாநிலம் அல்ல என்பதால் விருப்பம் A தவறு.",
        "Option B is correct because statement 2 accurately describes the Kalasa-Banduri project.", "கூற்று 2 கலசா-பண்டூரி திட்டத்தைச் சரியாக விவரிப்பதால் விருப்பம் B சரி.",
        "Option C is incorrect because statement 1 incorrectly lists Kerala.", "கூற்று 1 கேரளாவைத் தவறாகக் குறிப்பிடுவதால் விருப்பம் C தவறு.",
        "Option D is incorrect because statement 2 is factually sound.", "கூற்று 2 உண்மையானது என்பதால் விருப்பம் D தவறு.",
        "Mahadayi parties: Goa, Karnataka, Maharashtra (NOT Kerala). Kalasa-Banduri is the focal project.",
        "மகதாயி மாநிலங்கள்: கோவா, கர்நாடகா, மகாராஷ்டிரா (கேரளா அல்ல). கலசா-பண்டூரி நாலா முக்கிய திட்டம்.",
        "Mahadayi Tribunal was formed in 2010 for Goa, Karnataka, and Maharashtra over the Kalasa-Banduri dispute.",
        "மகதாயி தீர்ப்பாயம் 2010-ல் கோவா, கர்நாடகா, மகாராஷ்டிரா இடையே கலசா-பண்டூரி விவகாரத்திற்காக அமைக்கப்பட்டது.",
        tags=["Mahadayi Tribunal", "Kalasa Banduri", "Goa Karnataka Maharashtra"]
    ))

    # 015 - Ans C
    q.append(make_q(
        "ISR_S_015", "Medium",
        "Consider the following statements regarding the Mahanadi Water Disputes Tribunal:\n1. The Mahanadi Water Disputes Tribunal was constituted in March 2018 under the chairmanship of Justice A.M. Khanwilkar.\n2. The dispute arose primarily over the construction of barrages by Chhattisgarh upstream, impacting flow into Odisha's Hirakud reservoir.\nWhich of the statements given above is/are correct?",
        "மகாநதி நதிநீர் தகராறுகள் தீர்ப்பாயம் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. மகாநதி நதிநீர் தகராறுகள் தீர்ப்பாயம் 2018 மார்ச்சில் நீதிபதி ஏ.எம். கான்வில்கர் தலைமையில் அமைக்கப்பட்டது.\n2. சத்தீஸ்கர் மேல்நோக்கி தடுப்பணைகளைக் கட்டியதால் ஒடிசாவின் ஹிராகுட் நீர்த்தேக்கத்திற்கு வரும் நீர்வரத்து பாதிக்கப்பட்டது தொடர்பாக இத்தகராறு எழுந்தது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "C",
        "Both statements are correct: Following a complaint from Odisha in 2016 and an order of the Supreme Court, the Central Government constituted the Mahanadi Water Disputes Tribunal in March 2018 headed by Justice A.M. Khanwilkar to adjudicate water disputes between Odisha and Chhattisgarh concerning the Hirakud dam inflows.",
        "இரண்டு கூற்றுகளும் சரியானவை: ஒடிசா அரசின் புகார் மற்றும் உச்ச நீதிமன்ற உத்தரவின் பேரில், 2018 மார்ச்சில் நீதிபதி ஏ.எம். கான்வில்கர் தலைமையில் மகாநதி நதிநீர் தீர்ப்பாயம் சத்தீஸ்கர் மற்றும் ஒடிசா இடையே உள்ள ஹிராகுட் அணை நீர்வரத்து சிக்கலைத் தீர்க்க அமைக்கப்பட்டது.",
        "Option A is incorrect because statement 2 is also an accurate depiction of the dispute.", "கூற்று 2-ம் தகராறைச் சரியாக விவரிப்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because statement 1 is also completely accurate.", "கூற்று 1-ம் முற்றிலும் சரியானது என்பதால் விருப்பம் B தவறு.",
        "Option C is correct as both statements accurately depict the genesis and chairmanship of the Mahanadi Tribunal.", "மகாநதி தீர்ப்பாயத்தின் தோற்றம் மற்றும் தலைவரை இரண்டு கூற்றுகளும் சரியாகக் குறிப்பிடுவதால் விருப்பம் C சரி.",
        "Option D is incorrect because neither statement is false.", "எந்தக் கூற்றும் தவறானது அல்ல என்பதால் விருப்பம் D தவறு.",
        "Mahanadi Tribunal = Justice A.M. Khanwilkar (2018); states involved = Odisha & Chhattisgarh.",
        "மகாநதி தீர்ப்பாயம் = நீதிபதி ஏ.எம். கான்வில்கர் (2018); தொடர்புடைய மாநிலங்கள் = ஒடிசா & சத்தீஸ்கர்.",
        "Mahanadi Water Disputes Tribunal was established in 2018 under Justice A.M. Khanwilkar for Odisha and Chhattisgarh.",
        "மகாநதி நதிநீர் தீர்ப்பாயம் 2018-ல் நீதிபதி ஏ.எம். கான்வில்கர் தலைமையில் ஒடிசா மற்றும் சத்தீஸ்கருக்காக அமைக்கப்பட்டது.",
        tags=["Mahanadi Tribunal", "Justice Khanwilkar", "Odisha Chhattisgarh"]
    ))

    # 016 - Ans D
    q.append(make_q(
        "ISR_S_016", "Hard",
        "Consider the following statements regarding the Vansadhara Water Disputes Tribunal:\n1. The Vansadhara Water Disputes Tribunal was constituted to resolve water disputes between the States of Tamil Nadu and Andhra Pradesh.\n2. The Tribunal was constituted under the Inter-State River Water Disputes Act, 1956 in the year 1990.\nWhich of the statements given above is/are correct?",
        "வம்சதாரா நதிநீர் தகராறுகள் தீர்ப்பாயம் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. வம்சதாரா நதிநீர் தகராறுகள் தீர்ப்பாயம் தமிழ்நாடு மற்றும் ஆந்திரப் பிரதேசம் ஆகிய மாநிலங்களுக்கு இடையிலான நதிநீர் சிக்கலைத் தீர்க்க அமைக்கப்பட்டது.\n2. இத்தீர்ப்பாயம் 1956-ஆம் ஆண்டின் மாநிலங்களுக்கு இடையேயான நதிநீர் தகராறுகள் சட்டத்தின் கீழ் 1990-ஆம் ஆண்டில் அமைக்கப்பட்டது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "D",
        "Both statements are incorrect: Statement 1 is incorrect: The Vansadhara dispute involves Andhra Pradesh and ODISHA (not Tamil Nadu), primarily regarding the construction of the Neradi Barrage by Andhra Pradesh. Statement 2 is incorrect: The Vansadhara Tribunal was constituted in February 2010 (under Justice Mukundakam Sharma), not in 1990 (when the Cauvery Tribunal was constituted).",
        "இரண்டு கூற்றுகளும் தவறானவை: கூற்று 1 தவறு: வம்சதாரா தகராறு ஆந்திரப் பிரதேசம் மற்றும் ஒடிசா இடையே உள்ளதே தவிர, தமிழ்நாட்டுடன் அல்ல (நேரடி தடுப்பணை விவகாரம்). கூற்று 2 தவறு: வம்சதாரா தீர்ப்பாயம் 2010 பிப்ரவரியில் நீதிபதி முகுந்தகம் சர்மா தலைமையில் அமைக்கப்பட்டது, 1990-ல் அல்ல.",
        "Option A is incorrect because Tamil Nadu has no geographical connection with river Vansadhara.", "வம்சதாரா நதியுடன் தமிழ்நாட்டிற்கு எந்தத் தொடர்பும் இல்லை என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because the Vansadhara Tribunal was established in 2010, not 1990.", "வம்சதாரா தீர்ப்பாயம் 2010-ல் அமைக்கப்பட்டதால் விருப்பம் B தவறு.",
        "Option C is incorrect because both statements are demonstrably false.", "இரண்டு கூற்றுகளும் முற்றிலும் தவறானவை என்பதால் விருப்பம் C தவறு.",
        "Option D is correct because Vansadhara involves AP and Odisha, and was formed in 2010.", "வம்சதாரா ஆந்திரா-ஒடிசா தொடர்புடையது மற்றும் 2010-ல் அமைக்கப்பட்டது என்பதால் விருப்பம் D சரி.",
        "Vansadhara River = Andhra Pradesh and Odisha (Neradi Barrage dispute), constituted in 2010.",
        "வம்சதாரா நதி = ஆந்திரப் பிரதேசம் மற்றும் ஒடிசா (நேரடி அணை தகராறு), 2010-ல் அமைக்கப்பட்டது.",
        "Vansadhara Tribunal was constituted in 2010 to resolve the AP-Odisha river dispute.",
        "வம்சதாரா தீர்ப்பாயம் ஆந்திரா-ஒடிசா நதிநீர் தகராறைத் தீர்க்க 2010-ல் அமைக்கப்பட்டது.",
        tags=["Vansadhara Tribunal", "Andhra Odisha", "Neradi Barrage"]
    ))

    # 017 - Ans A
    q.append(make_q(
        "ISR_S_017", "Medium",
        "Consider the following statements regarding the Inter-State River Water Disputes (Amendment) Bill, 2019:\n1. It proposes the establishment of a single standalone Inter-State River Water Disputes Tribunal with multiple benches, replacing existing ad-hoc tribunals.\n2. It completely eliminates the Dispute Resolution Committee (DRC) mechanism to allow direct unmediated litigation before the Tribunal.\nWhich of the statements given above is/are correct?",
        "2019-ஆம் ஆண்டின் மாநிலங்களுக்கு இடையேயான நதிநீர் தகராறுகள் (திருத்த) மசோதா தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது தற்போதுள்ள தற்காலிகத் தீர்ப்பாயங்களுக்குப் பதிலாக, பல அமர்வுகளைக் கொண்ட ஒரே நிரந்தர நதிநீர் தகராறுகள் தீர்ப்பாயத்தை நிறுவ முன்மொழிகிறது.\n2. இது தீர்ப்பாயத்தின் முன் நேரடி வழக்காடலை அனுமதிக்க தகராறு தீர்வு குழு (DRC) முறையை முற்றிலுமாக நீக்குகிறது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "A",
        "Statement 1 is correct: The Amendment Bill provides for a single, permanent Tribunal with multiple benches to dissolve standalone ad-hoc tribunals. Statement 2 is incorrect: On the contrary, the Bill mandates the creation of a Dispute Resolution Committee (DRC) to attempt amicable negotiations within 1 year (extendable by 6 months) BEFORE a dispute can be referred to the Tribunal.",
        "கூற்று 1 சரி: தனித்தனி தற்காலிக தீர்ப்பாயங்களை நீக்கி, பல அமர்வுகளைக் கொண்ட ஒரே நிரந்தரத் தீர்ப்பாயத்தை உருவாக்க மசோதா வகை செய்கிறது. கூற்று 2 தவறு: மாறாக, தீர்ப்பாயத்திற்குச் செல்வதற்கு முன் பேச்சுவார்த்தை மூலம் தீர்க்க 1 ஆண்டு கால அவகாசத்துடன் தகராறு தீர்வு குழுவை (DRC) அமைப்பதை மசோதா கட்டாயமாக்குகிறது.",
        "Option A is correct because statement 1 reflects the institutional reform while statement 2 misrepresents the DRC requirement.", "கூற்று 1 நிறுவன சீர்திருத்தத்தைச் சரியாகக் குறிப்பிடுவதால் விருப்பம் A சரி.",
        "Option B is incorrect because the DRC is an integral mandatory precursor in the Bill.", "DRC என்பது மசோதாவின் கட்டாய முதற்கட்ட அமைப்பு என்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because statement 2 is false.", "கூற்று 2 தவறாக இருப்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because statement 1 is accurate.", "கூற்று 1 சரியானது என்பதால் விருப்பம் D தவறு.",
        "Key reform in the 2019 Bill: Single permanent tribunal + mandatory Dispute Resolution Committee (DRC).",
        "2019 மசோதாவின் முக்கிய சீர்திருத்தம்: ஒரே நிரந்தர தீர்ப்பாயம் + கட்டாய தகராறு தீர்வு குழு (DRC).",
        "The IRWD Amendment Bill proposes a single permanent tribunal with multiple benches and a DRC.",
        "IRWD திருத்த மசோதா பல அமர்வுகளைக் கொண்ட ஒரே நிரந்தர தீர்ப்பாயத்தையும் DRC-யையும் முன்மொழிகிறது.",
        tags=["IRWD Bill 2019", "Dispute Resolution Committee", "Permanent Tribunal"]
    ))

    # 018 - Ans B
    q.append(make_q(
        "ISR_S_018", "Medium",
        "Consider the following statements regarding the constitutional nature of the Inter-State Council under Article 263:\n1. The Inter-State Council is automatically established by the Constitution itself as a permanent continuous judicial organ.\n2. The Inter-State Council is established by an order of the President whenever it appears to him that the public interests would be served by its establishment.\nWhich of the statements given above is/are correct?",
        "உறுப்பு 263-ன் கீழ் மாநிலங்களுக்கு இடையிலான மன்றத்தின் அரசியலமைப்புத் தன்மை தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. மாநிலங்களுக்கு இடையிலான மன்றம் அரசியலமைப்பால் ஒரு நிரந்தர தொடர்ச்சியான நீதித்துறை அமைப்பாக தானாகவே நிறுவப்பட்டுள்ளது.\n2. அத்தகைய மன்றத்தை அமைப்பது பொது நலனுக்கு உகந்தது என்று தோன்றும் போதெல்லாம் குடியரசுத் தலைவரின் ஆணை மூலம் இது நிறுவப்படுகிறது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "B",
        "Statement 1 is incorrect: Article 263 does not automatically establish a council; it empowers the President to establish it. Furthermore, it is not a judicial organ but an advisory and deliberative body. Statement 2 is correct: Article 263 explicitly opens with: 'If at any time it appears to the President that the public interests would be served by the establishment of a Council... it shall be lawful for the President by order to establish such a Council'.",
        "கூற்று 1 தவறு: உறுப்பு 263 தானாகவே மன்றத்தை நிறுவவில்லை; குடியரசுத் தலைவர் ஆணை மூலம் நிறுவ அதிகாரம் அளிக்கிறது. மேலும் இது நீதித்துறை அமைப்பு அல்ல, ஆலோசனைக் குழுவாகும். கூற்று 2 சரி: பொது நலனுக்குத் தேவைப்படும் போது குடியரசுத் தலைவர் தனது ஆணை மூலம் இதனை நிறுவலாம் என்று உறுப்பு 263 தெளிவாகக் கூறுகிறது.",
        "Option A is incorrect because Article 263 is enabling and the ISC is strictly advisory.", "உறுப்பு 263 ஆலோசனைக் குழுவை அமைக்க அதிகாரம் மட்டுமே அளிக்கிறது என்பதால் விருப்பம் A தவறு.",
        "Option B is correct because statement 2 captures the precise constitutional wording of Article 263.", "கூற்று 2 உறுப்பு 263-ன் வாசகங்களைச் சரியாகக் குறிப்பிடுவதால் விருப்பம் B சரி.",
        "Option C is incorrect because statement 1 is erroneous.", "கூற்று 1 தவறாக இருப்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because statement 2 is an exact constitutional rule.", "கூற்று 2 சரியான விதி என்பதால் விருப்பம் D தவறு.",
        "Article 263 is an enabling provision: the Council exists by Presidential Order, not automatic perpetual mandate.",
        "உறுப்பு 263 அதிகாரம் அளிக்கும் விதி: மன்றம் குடியரசுத் தலைவரின் ஆணை மூலமே நடைமுறைக்கு வருகிறது.",
        "Inter-State Council is constituted by Presidential Order under Article 263 to serve the public interest.",
        "பொது நலனைக் கருதி உறுப்பு 263-ன் கீழ் குடியரசுத் தலைவரின் ஆணை மூலம் மாநிலங்களுக்கு இடையிலான மன்றம் அமைக்கப்படுகிறது.",
        tags=["Article 263", "Presidential Order", "Advisory Body"]
    ))

    # 019 - Ans A
    q.append(make_q(
        "ISR_S_019", "Hard",
        "Consider the following statements regarding the recommendations of the Sarkaria Commission (1987–88) concerning the Inter-State Council:\n1. The Commission strongly recommended the establishment of a permanent Inter-State Council under Article 263.\n2. The Commission suggested that to differentiate it from other ad-hoc bodies created under Article 263, it should be designated as the 'Inter-Governmental Council'.\nWhich of the statements given above is/are correct?",
        "மாநிலங்களுக்கு இடையிலான மன்றம் தொடர்பாக சர்க்காரியா ஆணையத்தின் (1987-88) பரிந்துரைகள் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. உறுப்பு 263-ன் கீழ் ஒரு நிரந்தர மாநிலங்களுக்கு இடையிலான மன்றத்தை நிறுவ வேண்டும் என்று ஆணையம் வலுவாகப் பரிந்துரைத்தது.\n2. உறுப்பு 263-ன் கீழ் உருவாக்கப்பட்ட பிற தற்காலிக அமைப்புகளிலிருந்து இதை வேறுபடுத்திக் காட்ட, இதற்கு 'அரசாங்கங்களுக்கு இடையிலான மன்றம்' (Inter-Governmental Council) என்று பெயரிடலாம் என ஆணையம் பரிந்துரைத்தது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "2 only", "2 மட்டும்",
        "1 only", "1 மட்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "A",
        "Both statements are correct: The Sarkaria Commission on Centre-State Relations (1988) recommended that a permanent Inter-State Council be set up under Article 263. It specifically recommended that it should be called the 'Inter-Governmental Council' to distinguish it from various other councils established under Article 263 (such as the Central Council of Health, Central Council of Local Self-Government).",
        "இரண்டு கூற்றுகளும் சரியானவை: சர்க்காரியா ஆணையம் உறுப்பு 263-ன் கீழ் ஒரு நிரந்தர மன்றத்தை அமைக்கப் பரிந்துரைத்தது. மேலும், சுகாதாரம் மற்றும் உள்ளாட்சி போன்ற பிற அமைப்புகளிலிருந்து வேறுபடுத்த, இதற்கு 'அரசாங்கங்களுக்கு இடையிலான மன்றம்' எனப் பெயரிடலாம் என்றும் பரிந்துரைத்தது.",
        "Option A is correct because both recommendations were prominently emphasized in the Sarkaria Commission Report.", "இரண்டு பரிந்துரைகளும் சர்க்காரியா அறிக்கையில் முக்கியமாக இடம்பெற்றதால் விருப்பம் A சரி.",
        "Option B is incorrect because statement 1 is equally correct.", "கூற்று 1-ம் சரியானது என்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because statement 2 is also an authentic Sarkaria recommendation.", "கூற்று 2-ம் சர்க்காரியா ஆணையத்தின் உண்மைப் பரிந்துரை என்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because both statements are true.", "இரண்டு கூற்றுகளும் உண்மையானவை என்பதால் விருப்பம் D தவறு.",
        "Sarkaria Commission coined the term 'Inter-Governmental Council' to avoid confusion with ad-hoc Art 263 bodies.",
        "பிற உறுப்பு 263 அமைப்புகளுடன் குழப்பத்தைத் தவிர்க்க 'அரசாங்கங்களுக்கு இடையிலான மன்றம்' என்ற பெயரை சர்க்காரியா ஆணையம் முன்மொழிந்தது.",
        "Sarkaria Commission recommended a permanent council under Article 263 called Inter-Governmental Council.",
        "சர்க்காரியா ஆணையம் உறுப்பு 263-ன் கீழ் அரசாங்கங்களுக்கு இடையிலான மன்றம் என்ற நிரந்தர மன்றத்தை அமைக்கப் பரிந்துரைத்தது.",
        tags=["Sarkaria Commission", "Inter-Governmental Council", "Article 263"]
    ))

    # 020 - Ans D
    q.append(make_q(
        "ISR_S_020", "Medium",
        "Consider the following statements regarding the composition of the Inter-State Council established in 1990:\n1. The Chief Justice of India serves as the permanent Chairman of the Inter-State Council.\n2. The Leader of the Opposition in the Lok Sabha is an ex-officio member of the Inter-State Council.\nWhich of the statements given above is/are correct?",
        "1990-ல் நிறுவப்பட்ட மாநிலங்களுக்கு இடையிலான மன்றத்தின் கட்டமைப்பு தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இந்தியத் தலைமை நீதிபதி மாநிலங்களுக்கு இடையிலான மன்றத்தின் நிரந்தரத் தலைவராகச் செயல்படுகிறார்.\n2. மக்களவை எதிர்க்கட்சித் தலைவர் மாநிலங்களுக்கு இடையிலான மன்றத்தின் அலுவல்சார் உறுப்பினராக உள்ளார்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "D",
        "Both statements are incorrect: Statement 1 is incorrect: The Prime Minister is the Chairman of the Inter-State Council, not the Chief Justice of India. Statement 2 is incorrect: The composition consists of the PM (Chairman), Chief Ministers of all States and UTs with legislative assemblies, Administrators of UTs without legislative assemblies, and six Union Cabinet Ministers (nominated by the PM). The Leader of the Opposition is NOT a member of the Inter-State Council.",
        "இரண்டு கூற்றுகளும் தவறானவை: கூற்று 1 தவறு: பிரதமர் மாநிலங்களுக்கு இடையிலான மன்றத்தின் தலைவராக உள்ளார், தலைமை நீதிபதி அல்ல. கூற்று 2 தவறு: இதன் உறுப்பினர்கள் பிரதமர் (தலைவர்), அனைத்து மாநில முதலமைச்சர்கள், யூனியன் பிரதேச முதலமைச்சர்கள்/நிர்வாகிகள் மற்றும் பிரதமரால் நியமிக்கப்படும் 6 மத்திய அமைச்சரவை அமைச்சர்கள் ஆவர். மக்களவை எதிர்க்கட்சித் தலைவர் இதில் உறுப்பினர் அல்ல.",
        "Option A is incorrect because the Prime Minister chairs the Council.", "பிரதமரே மன்றத்தின் தலைவர் என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because Leader of Opposition is not an ex-officio member.", "எதிர்க்கட்சித் தலைவர் அலுவல்சார் உறுப்பினர் அல்ல என்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because both statements are factually wrong.", "இரண்டு கூற்றுகளும் தவறானவை என்பதால் விருப்பம் C தவறு.",
        "Option D is correct as both statements incorrectly identify the ISC leadership and membership.", "இரண்டு கூற்றுகளும் தலைமை மற்றும் உறுப்பினர்களைத் தவறாகக் குறிப்பிடுவதால் விருப்பம் D சரி.",
        "Inter-State Council composition: PM (Chairman) + All State CMs + UT CMs/Administrators + 6 Union Cabinet Ministers.",
        "மன்றத்தின் கட்டமைப்பு: பிரதமர் (தலைவர்) + அனைத்து மாநில முதலமைச்சர்கள் + யூனியன் பிரதேச முதலமைச்சர்கள்/நிர்வாகிகள் + 6 மத்திய அமைச்சர்கள்.",
        "The Prime Minister chairs the Inter-State Council, comprising all CMs and 6 nominated Union Cabinet Ministers.",
        "அனைத்து முதலமைச்சர்கள் மற்றும் 6 மத்திய அமைச்சர்களைக் கொண்ட மாநிலங்களுக்கு இடையிலான மன்றத்திற்குப் பிரதமர் தலைமை தாங்குகிறார்.",
        tags=["ISC Composition", "Prime Minister Chairman", "No CJI Role"]
    ))

    # 021 - Ans A
    q.append(make_q(
        "ISR_S_021", "Hard",
        "Consider the following statements regarding the Standing Committee of the Inter-State Council:\n1. The Standing Committee was set up in 1996 for continuous consultation and processing of matters for the consideration of the Council.\n2. The Prime Minister acts as the Chairman of the Standing Committee.\nWhich of the statements given above is/are correct?",
        "மாநிலங்களுக்கு இடையிலான மன்றத்தின் நிலைக்குழு தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. மன்றத்தின் பரிசீலனைக்குரிய விஷயங்களைத் தொடர்ந்து ஆலோசிக்கவும் செயல்படுத்தவும் 1996-ல் நிலைக்குழு அமைக்கப்பட்டது.\n2. பிரதமர் இந்த நிலைக்குழுவின் தலைவராகச் செயல்படுகிறார்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "A",
        "Statement 1 is correct: The Standing Committee of the Inter-State Council was set up in 1996 to process matters and maintain continuous consultation. Statement 2 is incorrect: The Union Home Minister is the Chairman of the Standing Committee, not the Prime Minister. The Committee consists of the Union Home Minister (Chairman), 5 Union Cabinet Ministers, and 9 Chief Ministers.",
        "கூற்று 1 சரி: தொடர் ஆலோசனை மற்றும் பணிகளைச் செயல்படுத்த 1996-ல் நிலைக்குழு அமைக்கப்பட்டது. கூற்று 2 தவறு: மத்திய உள்துறை அமைச்சர் இந்த நிலைக்குழுவின் தலைவராக உள்ளார், பிரதமர் அல்ல. இக்குழுவில் உள்துறை அமைச்சர் (தலைவர்), 5 மத்திய அமைச்சர்கள் மற்றும் 9 முதலமைச்சர்கள் உள்ளனர்.",
        "Option A is correct because statement 1 is accurate while statement 2 confuses the Home Minister with the Prime Minister.", "கூற்று 1 சரியானது மற்றும் கூற்று 2 உள்துறை அமைச்சருக்குப் பதிலாகப் பிரதமரைக் குறிப்பிடுவதால் விருப்பம் A சரி.",
        "Option B is incorrect because the Home Minister chairs the Standing Committee.", "உள்துறை அமைச்சரே நிலைக்குழுவின் தலைவர் என்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because statement 2 is false.", "கூற்று 2 தவறாக இருப்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because statement 1 is true.", "கூற்று 1 உண்மையானது என்பதால் விருப்பம் D தவறு.",
        "Important distinction: Full Inter-State Council is chaired by PM; Standing Committee is chaired by Home Minister!",
        "முக்கிய வேறுபாடு: முழு மாநிலங்களுக்கு இடையிலான மன்றத்திற்குப் பிரதமர் தலைவர்; நிலைக்குழுவிற்கு மத்திய உள்துறை அமைச்சர் தலைவர்!",
        "Standing Committee of ISC was established in 1996 and is chaired by the Union Home Minister.",
        "மன்றத்தின் நிலைக்குழு 1996-ல் அமைக்கப்பட்டது; இதற்கு மத்திய உள்துறை அமைச்சர் தலைமை தாங்குகிறார்.",
        tags=["Standing Committee", "Home Minister Chairman", "Continuous Consultation"]
    ))

    # 022 - Ans B
    q.append(make_q(
        "ISR_S_022", "Medium",
        "Consider the following statements regarding the functions and powers of the Inter-State Council under Article 263:\n1. The Council can deliver a legally binding judgment on inter-State legal disputes, enjoying powers identical to the Supreme Court under Article 131.\n2. The Council can inquire into and advise upon disputes which may have arisen between States, acting purely as an advisory and deliberative body.\nWhich of the statements given above is/are correct?",
        "உறுப்பு 263-ன் கீழ் மாநிலங்களுக்கு இடையிலான மன்றத்தின் பணிகள் மற்றும் அதிகாரங்கள் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. மாநிலங்களுக்கு இடையேயான சட்டத் தகராறுகளில் சட்டப்பூர்வமாகப் பிணைக்கும் தீர்ப்பை வழங்கும் அதிகாரம் இம்மன்றத்திற்கு உண்டு; இது உறுப்பு 131-ன் கீழ் உச்ச நீதிமன்றத்திற்கு இணையான அதிகாரங்களைக் கொண்டுள்ளது.\n2. மாநிலங்களுக்கு இடையே எழுந்த தகராறுகள் குறித்து விசாரித்து ஆலோசனை வழங்க மட்டுமே மன்றத்திற்கு அதிகாரம் உண்டு; இது முற்றிலும் ஆலோசனைக் குழுவாக மட்டுமே செயல்படுகிறது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "B",
        "Statement 1 is incorrect: The Inter-State Council has no adjudicatory or judicial powers; it cannot render binding legal decisions. Legal disputes involving rights must be decided by the Supreme Court under Article 131. Statement 2 is correct: Under Article 263(a), the Council is tasked with 'inquiring into and advising upon disputes which may have arisen between States'. Its function is purely advisory and non-binding.",
        "கூற்று 1 தவறு: மன்றத்திற்கு எந்த நீதித்துறை அதிகாரமும் இல்லை; இது பிணைக்கும் சட்டப்பூர்வத் தீர்ப்புகளை வழங்க முடியாது. உரிமை தொடர்பான சட்டத் தகராறுகளை உச்ச நீதிமன்றமே உறுப்பு 131-ன் கீழ் தீர்க்க முடியும். கூற்று 2 சரி: உறுப்பு 263(a)-ன் படி மாநிலங்களுக்கிடையேயான தகராறுகளை விசாரித்து ஆலோசனை வழங்குவதே இதன் பணியாகும்; இது ஆலோசனைக் குழு மட்டுமே.",
        "Option A is incorrect because the ISC possesses zero judicial authority.", "மன்றத்திற்கு எந்த நீதித்துறை அதிகாரமும் இல்லை என்பதால் விருப்பம் A தவறு.",
        "Option B is correct because statement 2 captures Article 263(a)'s advisory scope.", "கூற்று 2 உறுப்பு 263(a)-ன் ஆலோசனைக் கட்டமைப்பைச் சரியாகக் குறிப்பிடுவதால் விருப்பம் B சரி.",
        "Option C is incorrect because statement 1 is legally false.", "கூற்று 1 சட்டப்படி தவறாக இருப்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because statement 2 is completely true.", "கூற்று 2 முற்றிலும் சரியானது என்பதால் விருப்பம் D தவறு.",
        "ISC advises under Article 263; Supreme Court adjudicates under Article 131. Advisory vs Binding.",
        "மன்றம் உறுப்பு 263-ன் கீழ் ஆலோசனை கூறுகிறது; உச்ச நீதிமன்றம் உறுப்பு 131-ன் கீழ் பிணைக்கும் தீர்ப்பை வழங்குகிறது.",
        "Article 263 Inter-State Council is purely advisory and holds no binding adjudicatory authority.",
        "உறுப்பு 263-ன் கீழான மாநிலங்களுக்கு இடையிலான மன்றம் ஆலோசனைக் குழுவே அன்றி பிணைக்கும் தீர்ப்பளிக்கும் அமைப்பு அல்ல.",
        tags=["Article 263 Functions", "Advisory vs Adjudicatory", "Article 131 Distinction"]
    ))

    # 023 - Ans C
    q.append(make_q(
        "ISR_S_023", "Hard",
        "Consider the following statements regarding the procedure and meetings of the Inter-State Council:\n1. The Council is mandated by its rules of procedure to meet at least thrice every year.\n2. All questions at a meeting of the Council are decided by consensus, and meetings are held in camera.\nWhich of the statements given above is/are correct?",
        "மாநிலங்களுக்கு இடையிலான மன்றத்தின் நடைமுறைகள் மற்றும் கூட்டங்கள் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. மன்றத்தின் நடைமுறை விதிகளின்படி, இது ஒவ்வொரு ஆண்டும் குறைந்தது மூன்று முறையாவது கூட வேண்டும்.\n2. மன்றக் கூட்டத்தில் எழும் அனைத்துக் கேள்விகளும் ஒருமனதாக (consensus) முடிவு செய்யப்படுகின்றன, மற்றும் கூட்டங்கள் ரகசியமாக (in camera) நடத்தப்படுகின்றன.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "C",
        "Both statements are correct: Under the Inter-State Council procedure: (1) The Council is supposed to meet at least thrice a year; (2) Its meetings are held in camera (not open to media/public) and all questions are decided by consensus rather than formal voting.",
        "இரண்டு கூற்றுகளும் சரியானவை: மாநிலங்களுக்கு இடையிலான மன்ற நடைமுறை விதிகளின்படி: (1) மன்றம் ஆண்டில் குறைந்தது மூன்று முறையாவது கூட வேண்டும்; (2) இதன் கூட்டங்கள் ரகசியமாக (in camera) நடத்தப்பட்டு அனைத்து முடிவுகளும் வாக்கெடுப்பின்றி ஒருமனதாக (consensus) எட்டப்படுகின்றன.",
        "Option A is incorrect because statement 2 is also an established procedural rule.", "கூற்று 2-ம் மன்றத்தின் நடைமுறை விதி என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because statement 1 is equally accurate.", "கூற்று 1-ம் சரியானது என்பதால் விருப்பம் B தவறு.",
        "Option C is correct because both three-annual-meeting mandate and consensus/in camera rules are true.", "ஆண்டுக்கு மூன்று முறை கூடுதல் மற்றும் ஒருமனதான ரகசியக் கூட்ட விதிகள் இரண்டும் சரியானவை என்பதால் விருப்பம் C சரி.",
        "Option D is incorrect because neither statement is false.", "எந்தக் கூற்றும் தவறானது அல்ல என்பதால் விருப்பம் D தவறு.",
        "ISC procedures: At least 3 meetings/year; held in camera; decisions taken by consensus.",
        "மன்ற நடைமுறைகள்: ஆண்டுக்குக் குறைந்தது 3 கூட்டங்கள்; ரகசியக் கூட்டங்கள்; முடிவுகள் ஒருமனதாக எடுக்கப்படுகின்றன.",
        "Inter-State Council is mandated to meet thrice yearly; meetings are in camera and decided by consensus.",
        "மன்றம் ஆண்டுக்கு மூன்று முறை கூட வேண்டும்; கூட்டங்கள் ரகசியமாகவும் ஒருமனதான முடிவுகளுடனும் நடைபெறும்.",
        tags=["ISC Procedure", "Consensus Decision", "In Camera Meetings"]
    ))

    # 024 - Ans D
    q.append(make_q(
        "ISR_S_024", "Hard",
        "Consider the following statements regarding the Inter-State Council Secretariat (ISCS):\n1. The Secretariat was established as a statutory body under the States Reorganisation Act, 1956.\n2. The Secretariat is headed by the Union Cabinet Secretary in an ex-officio capacity.\nWhich of the statements given above is/are correct?",
        "மாநிலங்களுக்கு இடையிலான மன்றச் செயலகம் (ISCS) தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இச்செயலகம் 1956-ஆம் ஆண்டின் மாநில மறுசீரமைப்புச் சட்டத்தின் கீழ் ஒரு சட்டப்பூர்வ அமைப்பாக நிறுவப்பட்டது.\n2. இச்செயலகத்திற்கு மத்திய அமைச்சரவைச் செயலாளர் (Cabinet Secretary) அலுவல்சார் தலைமை வகிக்கிறார்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "D",
        "Both statements are incorrect: Statement 1 is incorrect: The Inter-State Council Secretariat was set up in 1991 by the Government of India (not under the States Reorganisation Act 1956). Since April 2011, it also functions as the Secretariat to the Zonal Councils. Statement 2 is incorrect: It is headed by a Secretary to the Government of India (a Secretary-rank IAS officer), NOT the Cabinet Secretary.",
        "இரண்டு கூற்றுகளும் தவறானவை: கூற்று 1 தவறு: இச்செயலகம் 1991-ல் மத்திய அரசால் அமைக்கப்பட்டது (1956 சட்டத்தின் கீழ் அல்ல). 2011 முதல் இது மண்டலக் குழுக்களின் செயலகமாகவும் செயல்படுகிறது. கூற்று 2 தவறு: இதற்கு இந்திய அரசின் செயலாளர் அந்தஸ்தில் உள்ள அதிகாரி தலைமை தாங்குகிறார், கேபினட் செயலாளர் அல்ல.",
        "Option A is incorrect because ISCS was established in 1991 by executive order.", "இச்செயலகம் 1991-ல் நிர்வாக ஆணை மூலம் அமைக்கப்பட்டதால் விருப்பம் A தவறு.",
        "Option B is incorrect because it is headed by a Secretary to GoI, not the Cabinet Secretary.", "கேபினட் செயலாளருக்குப் பதிலாக இந்திய அரசின் செயலாளர் தலைமை வகிப்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because both statements are inaccurate.", "இரண்டு கூற்றுகளும் தவறானவை என்பதால் விருப்பம் C தவறு.",
        "Option D is correct as both statements misstate the statutory and administrative status of ISCS.", "இரண்டு கூற்றுகளும் செயலகத்தின் நிலை குறித்துத் தவறான தகவலைக் கொண்டுள்ளதால் விருப்பம் D சரி.",
        "ISCS was set up in 1991, headed by Secretary to GoI; serves Zonal Councils too since 2011.",
        "மன்றச் செயலகம் 1991-ல் அமைக்கப்பட்டது; இந்திய அரசுச் செயலாளர் இதன் தலைவர்; 2011 முதல் மண்டலக் குழுக்களுக்கும் உதவுகிறது.",
        "Inter-State Council Secretariat was established in 1991 and functions under a Secretary to GoI.",
        "மாநிலங்களுக்கு இடையிலான மன்றச் செயலகம் 1991-ல் நிறுவப்பட்டு இந்திய அரசுச் செயலாளரின் கீழ் இயங்குகிறது.",
        tags=["ISC Secretariat", "Secretary to GoI", "Zonal Councils Secretariat"]
    ))

    # 025 - Ans A
    q.append(make_q(
        "ISR_S_025", "Medium",
        "Consider the following statements regarding the institutional nature of Zonal Councils:\n1. Zonal Councils are statutory bodies created by an Act of Parliament (States Reorganisation Act, 1956), not constitutional bodies.\n2. Zonal Councils possess binding legislative authority to pass regional ordinances applicable to all member States.\nWhich of the statements given above is/are correct?",
        "மண்டலக் குழுக்களின் நிறுவனத் தன்மை தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. மண்டலக் குழுக்கள் நாடாளுமன்றத்தின் சட்டத்தால் (1956 மாநில மறுசீரமைப்புச் சட்டம்) உருவாக்கப்பட்ட சட்டப்பூர்வ அமைப்புகளே தவிர, அரசியலமைப்பு அமைப்புகள் அல்ல.\n2. மண்டலக் குழுக்கள் அனைத்து உறுப்பு மாநிலங்களுக்கும் பொருந்தும் வகையிலான பிராந்திய அவசரச் சட்டங்களை இயற்றும் பிணைப்புள்ள சட்டமியற்றும் அதிகாரத்தைக் கொண்டுள்ளன.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "A",
        "Statement 1 is correct: Unlike the Inter-State Council (which is constitutional under Article 263), Zonal Councils are statutory bodies established under Part III of the States Reorganisation Act, 1956. Statement 2 is incorrect: Zonal Councils have no legislative authority whatsoever; they are purely deliberative and advisory bodies.",
        "கூற்று 1 சரி: உறுப்பு 263-ன் கீழ் அரசியலமைப்பு அமைப்பாக உள்ள மாநிலங்களுக்கு இடையிலான மன்றம் போலல்லாமல், மண்டலக் குழுக்கள் 1956 மாநில மறுசீரமைப்புச் சட்டத்தின் கீழ் உருவாக்கப்பட்ட சட்டப்பூர்வ அமைப்புகள் ஆகும். கூற்று 2 தவறு: மண்டலக் குழுக்களுக்கு எந்தவித சட்டமியற்றும் அதிகாரமும் இல்லை; அவை முற்றிலும் ஆலோசனைக் குழுக்களே.",
        "Option A is correct because statement 1 highlights the vital distinction between statutory Zonal Councils and constitutional Article 263.", "மண்டலக் குழுக்கள் சட்டப்பூர்வ அமைப்புகள் என்பதை கூற்று 1 சரியாகக் குறிப்பிடுவதால் விருப்பம் A சரி.",
        "Option B is incorrect because Zonal Councils have zero legislative power.", "மண்டலக் குழுக்களுக்குச் சட்டமியற்றும் அதிகாரம் இல்லை என்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because statement 2 is false.", "கூற்று 2 தவறாக இருப்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because statement 1 is a cornerstone factual truth.", "கூற்று 1 உண்மையானது என்பதால் விருப்பம் D தவறு.",
        "Key distinction: Inter-State Council = Constitutional (Art 263); Zonal Councils = Statutory (1956 Act).",
        "முக்கிய வேறுபாடு: மாநிலங்களுக்கு இடையிலான மன்றம் = அரசியலமைப்பு சார்ந்தது (உறுப்பு 263); மண்டலக் குழுக்கள் = சட்டப்பூர்வமானது (1956 சட்டம்).",
        "Zonal Councils are statutory bodies under the States Reorganisation Act 1956 with deliberative and advisory powers.",
        "மண்டலக் குழுக்கள் 1956 மாநில மறுசீரமைப்புச் சட்டத்தின் கீழ் ஆலோசனைக் குழுக்களாக அமைக்கப்பட்ட சட்டப்பூர்வ அமைப்புகளாகும்.",
        tags=["Zonal Councils", "Statutory vs Constitutional", "States Reorganisation Act 1956"]
    ))

    return q
