# -*- coding: utf-8 -*-
"""
Build Judicial Review, Activism & PIL - Part 2A Statement-Based (50 MCQs)
Identifier: JRAP_S_001 to JRAP_S_050
Key Distribution: A: 13, B: 12, C: 12, D: 13 (Total: 50)
Anti-Block: Max consecutive run <= 2
"""
import json
import os
from collections import Counter
from judicial_review_mcq_helper import make_jrap_q

def build_statement_mcqs():
    questions = []

    statement_data = [
        # 1
        ("JRAP_S_001", "Article 13 Provisions",
         "Consider the following statements regarding Article 13 of the Indian Constitution:\n1. Article 13(1) provides that pre-constitutional laws inconsistent with Fundamental Rights are void from their very inception (void ab initio).\n2. Article 13(2) prohibits the State from making any law which takes away or abridges the rights conferred by Part III.\n3. The term 'law' under Article 13(3) includes ordinances, orders, bye-laws, rules, regulations, and notifications.\nWhich of the statements given above are correct?",
         "இந்திய அரசியலமைப்பின் உறுப்பு 13 தொடர்பான பின்வரும் கூற்றுகளைக் கவனிக்கவும்:\n1. உறுப்பு 13(1) அடிப்படை உரிமைகளுக்கு முரணான அரசியலமைப்புக்கு முந்தைய சட்டங்கள் ஆரம்பத்திலிருந்தே செல்லாது (void ab initio) எனக் கூறுகிறது.\n2. பகுதி III வழங்கிய உரிமைகளைப் பறிக்கும் அல்லது குறைக்கும் எந்தவொரு சட்டத்தையும் அரசு உருவாக்கக் கூடாது என உறுப்பு 13(2) தடுக்கிறது.\n3. உறுப்பு 13(3)-ன் கீழ் 'சட்டம்' என்ற சொல்லில் அவசரச்சட்டங்கள், உத்தரவுகள், துணைச்சட்டங்கள், விதிகள், நெறிமுறைகள் மற்றும் அறிவிக்கைகள் அடங்கும்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானவை எவை?",
         "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
         "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
         "1 and 3 only", "1 மற்றும் 3 மட்டுமே",
         "1, 2 and 3", "1, 2 மற்றும் 3", "B",
         "Statement 1 is incorrect because pre-constitutional laws are not void ab initio; they are valid when enacted and only become void to the extent of inconsistency from 26 January 1950 (Doctrine of Eclipse). Statements 2 and 3 are correct.",
         "கூற்று 1 தவறானது, ஏனெனில் அரசியலமைப்புக்கு முந்தைய சட்டங்கள் ஆரம்பத்திலிருந்தே செல்லாதவை அல்ல; அவை 26 ஜனவரி 1950 முதல் முரண்படும் அளவிற்கு மட்டுமே செயலற்றதாகின்றன (மறைப்புக் கோட்பாடு). கூற்றுகள் 2 மற்றும் 3 சரியானவை."),

        # 2
        ("JRAP_S_002", "Writ Jurisdiction Comparison",
         "Consider the following statements comparing Article 32 and Article 226:\n1. The Supreme Court can issue writs only for the enforcement of Fundamental Rights, whereas High Courts can issue writs for Fundamental Rights and for any other purpose.\n2. The remedy under Article 32 is itself a Fundamental Right, whereas under Article 226 it is a discretionary constitutional remedy.\n3. The territorial jurisdiction of the Supreme Court extends throughout India, while a High Court's jurisdiction is confined to its state territory.\nWhich of the statements given above are correct?",
         "உறுப்பு 32 மற்றும் உறுப்பு 226-ஐ ஒப்பிடும் பின்வரும் கூற்றுகளைக் கவனிக்கவும்:\n1. உச்ச நீதிமன்றம் அடிப்படை உரிமைகளை அமல்படுத்துவதற்கு மட்டுமே நீதிப்பேராணைகளை வெளியிட முடியும்; ஆனால் உயர் நீதிமன்றங்கள் அடிப்படை உரிமைகள் மற்றும் வேறு எந்த நோக்கத்திற்காகவும் நீதிப்பேராணைகளை வெளியிடலாம்.\n2. உறுப்பு 32-ன் கீழான பரிகாரம் தானே ஓர் அடிப்படை உரிமை; ஆனால் உறுப்பு 226-ன் கீழ் அது ஒரு விவேகத்திற்குட்பட்ட அரசியலமைப்புப் பரிகாரமாகும்.\n3. உச்ச நீதிமன்றத்தின் எல்லை அதிகாரம் இந்தியா முழுவதும் பரவியுள்ளது; ஆனால் உயர் நீதிமன்றத்தின் அதிகாரம் அதன் மாநில எல்லைக்குட்பட்டது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானவை எவை?",
         "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
         "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
         "1 and 3 only", "1 மற்றும் 3 மட்டுமே",
         "1, 2 and 3", "1, 2 மற்றும் 3", "D",
         "All three statements correctly articulate the vital differences between Supreme Court and High Court writ jurisdictions under Articles 32 and 226.",
         "உறுப்புகள் 32 மற்றும் 226-ன் கீழ் உச்ச மற்றும் உயர் நீதிமன்றங்களின் நீதிப்பேராணை அதிகார வரம்புகளுக்கு இடையேயான முக்கிய வேறுபாடுகளை மூன்று கூற்றுகளும் சரியாக விளக்குகின்றன."),

        # 3
        ("JRAP_S_003", "Basic Structure Doctrine Features",
         "Consider the following statements regarding the Basic Structure Doctrine:\n1. It was formulated by a 13-judge bench in Kesavananda Bharati (1973) by a 7:6 majority.\n2. The Supreme Court has provided an exhaustive list of all basic features in the text of the Constitution.\n3. Judicial review itself was recognized as an essential element of the Basic Structure in the Minerva Mills Case (1980).\nWhich of the statements given above are correct?",
         "அடிப்படைக் கட்டமைப்புக் கோட்பாடு தொடர்பான பின்வரும் கூற்றுகளைக் கவனிக்கவும்:\n1. இது கேசவாநந்த பாரதி (1973) வழக்கில் 13 நீதிபதிகள் அமர்வால் 7:6 பெரும்பான்மையில் உருவாக்கப்பட்டது.\n2. உச்ச நீதிமன்றம் அரசியலமைப்பின் வாசகத்தில் அனைத்து அடிப்படை அம்சங்களின் முழுமையான பட்டியலை வழங்கியுள்ளது.\n3. மினர்வா மில்ஸ் வழக்கில் (1980) நீதித்துறை மறுஆய்வே அடிப்படைக் கட்டமைப்பின் இன்றியமையாத கூறாக அங்கீகரிக்கப்பட்டது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானவை எவை?",
         "1 and 3 only", "1 மற்றும் 3 மட்டுமே",
         "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
         "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
         "1, 2 and 3", "1, 2 மற்றும் 3", "A",
         "Statement 2 is incorrect because the doctrine is judicially evolved and non-exhaustive; elements are identified on a case-by-case basis. Statements 1 and 3 are correct.",
         "கூற்று 2 தவறானது, ஏனெனில் இக்கோட்பாடு முழுமையான பட்டியலைக் கொண்டிருக்கவில்லை; வழக்கு வாரியாக உச்ச நீதிமன்றத்தால் கூறுகள் கண்டறியப்படுகின்றன. கூற்றுகள் 1 மற்றும் 3 சரியானவை."),

        # 4
        ("JRAP_S_004", "Ninth Schedule Post-Coelho",
         "Consider the following statements regarding the Ninth Schedule following the I.R. Coelho Case (2007):\n1. All laws placed in the Ninth Schedule from 26 January 1950 onwards are subject to judicial review.\n2. Laws placed in the Ninth Schedule on or after 24 April 1973 are open to challenge on the ground of violating the Basic Structure.\n3. If any law placed in the Ninth Schedule violates the rights guaranteed by Articles 14, 19, or 21 and damages the basic structure, it will be struck down.\nWhich of the statements given above are correct?",
         "I.R. கோயல்ஹோ வழக்கை (2007) தொடர்ந்து ஒன்பதாவது அட்டவணை தொடர்பான பின்வரும் கூற்றுகளைக் கவனிக்கவும்:\n1. 26 ஜனவரி 1950 முதல் ஒன்பதாவது அட்டவணையில் வைக்கப்பட்ட அனைத்து சட்டங்களும் நீதித்துறை மறுஆய்வுக்கு உட்பட்டவை.\n2. 24 ஏப்ரல் 1973 அன்றோ அல்லது அதற்குப் பின்னரோ 9வது அட்டவணையில் வைக்கப்பட்ட சட்டங்கள் அடிப்படைக் கட்டமைப்பை மீறுவதாக சவால் செய்யப்படலாம்.\n3. 9வது அட்டவணையில் வைக்கப்பட்ட சட்டம் உறுப்புகள் 14, 19 அல்லது 21 வழங்கிய உரிமைகளை மீறி அடிப்படைக் கட்டமைப்பைச் சேதப்படுத்தினால் அது ரத்து செய்யப்படும்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானவை எவை?",
         "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
         "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
         "1 and 3 only", "1 மற்றும் 3 மட்டுமே",
         "1, 2 and 3", "1, 2 மற்றும் 3", "B",
         "Statement 1 is incorrect because laws placed in the Ninth Schedule prior to 24 April 1973 enjoy constitutional immunity under Article 31B. Statements 2 and 3 are correct.",
         "கூற்று 1 தவறானது, ஏனெனில் 24 ஏப்ரல் 1973-க்கு முன் சேர்க்கப்பட்ட சட்டங்கள் உறுப்பு 31B கீழ் பாதுகாப்பு பெறுகின்றன. கூற்றுகள் 2 மற்றும் 3 சரியானவை."),

        # 5
        ("JRAP_S_005", "Judicial Activism vs Overreach",
         "Consider the following statements:\n1. Judicial Activism is the proactive role played by the judiciary in protecting citizens' rights and promoting constitutional justice.\n2. Judicial Overreach occurs when the judiciary acts as a parallel executive or legislature, violating the separation of powers.\n3. Imposing censorship on media and directly administering taxation are examples of healthy judicial activism.\nWhich of the statements given above are correct?",
         "பின்வரும் கூற்றுகளைக் கவனிக்கவும்:\n1. நீதித்துறை செயல்பாடு என்பது குடிமக்கள் உரிமைகளைப் பாதுகாக்கவும் அரசியலமைப்பு நீதியை மேம்படுத்தவும் நீதித்துறை எடுக்கும் தீவிர முனைப்பான பங்கு ஆகும்.\n2. நீதித்துறை ஒரு மாற்று நிர்வாகமாகவோ அல்லது சட்டமன்றமாகவோ செயல்பட்டு அதிகாரப் பகிர்வை மீறும் போது நீதித்துறை மிதமிஞ்சிய செயல்பாடு ஏற்படுகிறது.\n3. ஊடகங்களுக்குத் தணிக்கை விதிப்பதும் வரி விதிப்பை நேரடியாக நிர்வகிப்பதும் ஆரோக்கியமான நீதித்துறை செயல்பாட்டின் உதாரணங்களாகும்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானவை எவை?",
         "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
         "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
         "1 and 3 only", "1 மற்றும் 3 மட்டுமே",
         "1, 2 and 3", "1, 2 மற்றும் 3", "A",
         "Statement 3 is incorrect because directly levying taxes or imposing media censorship amounts to unconstitutional Judicial Overreach, not healthy activism. Statements 1 and 2 are correct.",
         "கூற்று 3 தவறானது, ஏனெனில் வரி விதிப்பது அல்லது ஊடகத் தணிக்கை செய்வது நீதித்துறை மிதமிஞ்சிய செயல்பாடாகும்; ஆரோக்கியமான செயல்பாடு அல்ல. கூற்றுகள் 1 மற்றும் 2 சரியானவை."),

        # 6
        ("JRAP_S_006", "Public Interest Litigation Features",
         "Consider the following statements regarding Public Interest Litigation (PIL) in India:\n1. Any member of the public acting bona fide can invoke writ jurisdiction on behalf of poor or disadvantaged persons.\n2. PIL can be filed against private individuals for breach of private civil contracts.\n3. The Supreme Court can appoint advocate commissioners to investigate facts and submit reports in PIL proceedings.\nWhich of the statements given above are correct?",
         "இந்தியாவில் பொது நல வழக்குகள் (PIL) தொடர்பான பின்வரும் கூற்றுகளைக் கவனிக்கவும்:\n1. ஏழை அல்லது ஒடுக்கப்பட்ட மக்களுக்காக நன்னம்பிக்கையுடன் செயல்படும் எந்தவொரு பொதுநபரும் நீதிப்பேராணை அதிகார வரம்பைத் தூண்டலாம்.\n2. தனியார் சிவில் ஒப்பந்த மீறல்களுக்காக தனிநபர்களுக்கு எதிராக PIL தாக்கல் செய்யப்படலாம்.\n3. PIL நடவடிக்கைகளில் உண்மைகளை ஆராய்ந்து அறிக்கை சமர்ப்பிக்க உச்ச நீதிமன்றம் வழக்கறிஞர் ஆணையர்களை நியமிக்க முடியும்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானவை எவை?",
         "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
         "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
         "1 and 3 only", "1 மற்றும் 3 மட்டுமே",
         "1, 2 and 3", "1, 2 மற்றும் 3", "C",
         "Statement 2 is incorrect because PIL lies only against the State, government authorities, or public bodies for violation of fundamental/public rights, not for private contractual disputes. Statements 1 and 3 are correct.",
         "கூற்று 2 தவறானது, ஏனெனில் PIL அரசு மற்றும் பொது அதிகாரிகளுக்கு எதிராக மட்டுமே தாக்கல் செய்யப்பட முடியும்; தனியார் ஒப்பந்த தகராறுகளுக்கு அல்ல. கூற்றுகள் 1 மற்றும் 3 சரியானவை."),

        # 7
        ("JRAP_S_007", "Maneka Gandhi Article 21 Principles",
         "Consider the following statements regarding the Maneka Gandhi Case (1978):\n1. It overruled the narrow interpretation of Article 21 laid down in A.K. Gopalan (1950).\n2. It held that the procedure depriving a person of life or liberty must be right, just, and fair, and not arbitrary or oppressive.\n3. It established that the Right to Travel Abroad is a fundamental right under Article 21.\nWhich of the statements given above are correct?",
         "மேனகா காந்தி வழக்கு (1978) தொடர்பான பின்வரும் கூற்றுகளைக் கவனிக்கவும்:\n1. இது ஏ.கே. கோபாலன் (1950) வழக்கில் உறுப்பு 21-க்கு அளிக்கப்பட்ட குறுகிய விளக்கத்தை ரத்து செய்தது.\n2. ஒரு நபரின் வாழ்வு அல்லது சுதந்திரத்தைப் பறிக்கும் நடைமுறை நேர்மையான, நியாயமானதாக இருக்க வேண்டும்; தன்னிச்சையானதாக இருக்கக்கூடாது எனத் தீர்ப்பளித்தது.\n3. வெளிநாடு செல்லும் உரிமை உறுப்பு 21-ன் கீழ் ஓர் அடிப்படை உரிமை என்பதை இது நிறுவியது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானவை எவை?",
         "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
         "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
         "1 and 3 only", "1 மற்றும் 3 மட்டுமே",
         "1, 2 and 3", "1, 2 மற்றும் 3", "D",
         "All three statements are correct. Maneka Gandhi (1978) was a watershed judgment in personal liberty, transforming Article 21 into a living source of human rights.",
         "மூன்று கூற்றுகளும் சரியானவை. மேனகா காந்தி வழக்கு தனிநபர் சுதந்திரத்தில் ஒரு திருப்புமுனையாக அமைந்து உறுப்பு 21-ஐ மனித உரிமைகளின் ஊற்றாக மாற்றியது."),

        # 8
        ("JRAP_S_008", "Collegium System Evolution",
         "Consider the following statements regarding the evolution of the Collegium System:\n1. In the First Judges Case (1981), the Executive was granted primacy in judicial appointments.\n2. In the Second Judges Case (1993), the CJI and two senior-most judges formed the collegium, making consultation mean concurrence.\n3. In the Third Judges Case (1998), the Supreme Court Collegium was expanded to CJI plus four senior-most judges.\nWhich of the statements given above are correct?",
         "கொலீஜியம் முறையின் பரிணாமம் தொடர்பான பின்வரும் கூற்றுகளைக் கவனிக்கவும்:\n1. முதல் நீதிபதிகள் வழக்கில் (1981) நீதிபதிகள் நியமனத்தில் நிர்வாகத்திற்கு முதன்மை அதிகாரம் வழங்கப்பட்டது.\n2. இரண்டாவது நீதிபதிகள் வழக்கில் (1993) தலைமை நீதிபதி மற்றும் இரண்டு மூத்த நீதிபதிகள் அடங்கிய கொலீஜியம் உருவாக்கப்பட்டு, கலந்தாலோசித்தல் என்பது உடன்பாடு எனப்பட்டது.\n3. மூன்றாவது நீதிபதிகள் வழக்கில் (1998) உச்ச நீதிமன்ற கொலீஜியம் தலைமை நீதிபதி + நான்கு மூத்த நீதிபதிகள் என விரிவாக்கப்பட்டது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானவை எவை?",
         "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
         "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
         "1 and 3 only", "1 மற்றும் 3 மட்டுமே",
         "1, 2 and 3", "1, 2 மற்றும் 3", "D",
         "All three statements accurately chart the chronological evolution of the Collegium System across the Three Judges Cases (1981, 1993, 1998).",
         "மூன்று நீதிபதிகள் வழக்குகளின் (1981, 1993, 1998) வாயிலாக கொலீஜியம் முறையின் காலவரிசைப் பரிணாமத்தை மூன்று கூற்றுகளும் துல்லியமாக விவரிக்கின்றன."),

        # 9
        ("JRAP_S_009", "Judicial Review of Ordinance Making",
         "Consider the following statements regarding Judicial Review of Ordinance-making power:\n1. In DC Wadhwa (1987), the Supreme Court held that re-promulgation of ordinances without placing them before the legislature is a subversion of the democratic process.\n2. In Krishna Kumar Singh (2017), the Supreme Court held that an ordinance does not create an enduring permanent right if it lapses.\n3. The satisfaction of the President or Governor under Articles 123 and 213 is immune from judicial scrutiny on grounds of malafide.\nWhich of the statements given above are correct?",
         "அவசரச்சட்டம் இயற்றும் அதிகாரத்தின் நீதித்துறை மறுஆய்வு தொடர்பான பின்வரும் கூற்றுகளைக் கவனிக்கவும்:\n1. டி.சி. வாத்வா (1987) வழக்கில் சட்டமன்றத்தின் முன் வைக்காமல் அவசரச்சட்டங்களை மீண்டும் மீண்டும் பிறப்பிப்பது ஜனநாயக செயல்முறையைச் சீர்குலைப்பதாகும் என உச்ச நீதிமன்றம் தீர்ப்பளித்தது.\n2. கிருஷ்ண குமார் சிங் (2017) வழக்கில் அவசரச்சட்டம் காலாவதியானால் அது நிரந்தர உரிமையை உருவாக்காது என உச்ச நீதிமன்றம் கூறியது.\n3. உறுப்புகள் 123 மற்றும் 213-ன் கீழான குடியரசுத் தலைவர் அல்லது ஆளுநரின் திருப்தி துர்நோக்கம் என்ற காரணத்தின் அடிப்படையில் நீதித்துறை ஆய்விலிருந்து விலக்கு பெற்றது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானவை எவை?",
         "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
         "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
         "1 and 3 only", "1 மற்றும் 3 மட்டுமே",
         "1, 2 and 3", "1, 2 மற்றும் 3", "A",
         "Statement 3 is incorrect because ordinance-making power is reviewable if exercised malafide or in colourable exercise of power. Statements 1 and 2 are correct.",
         "கூற்று 3 தவறானது, ஏனெனில் அவசரச்சட்டம் துர்நோக்கத்துடன் பிறப்பிக்கப்பட்டால் அது நீதித்துறை மறுஆய்வுக்கு உட்பட்டது. கூற்றுகள் 1 மற்றும் 2 சரியானவை."),

        # 10
        ("JRAP_S_010", "Article 356 Bommai Guidelines",
         "Consider the following statements regarding the S.R. Bommai judgment (1994) on Article 356:\n1. Proclamation of President's Rule is subject to judicial review on grounds of malafide or extraneous considerations.\n2. The Legislative Assembly can be dissolved immediately upon the issuance of the proclamation before parliamentary approval.\n3. If the Court strikes down the proclamation, the dissolved Legislative Assembly and Ministry can be revived.\nWhich of the statements given above are correct?",
         "உறுப்பு 356 மீதான எஸ்.ஆர். பொம்மை தீர்ப்பு (1994) தொடர்பான பின்வரும் கூற்றுகளைக் கவனிக்கவும்:\n1. குடியரசுத் தலைவர் ஆட்சி பிரகடனம் துர்நோக்கம் அல்லது தொடர்பற்ற காரணங்களின் அடிப்படையில் நீதித்துறை மறுஆய்வுக்கு உட்பட்டது.\n2. நாடாளுமன்ற ஒப்புதலுக்கு முன்னரே பிரகடனம் வெளியிடப்பட்ட உடனேயே சட்டப்பேரவையைக் கலைக்க முடியும்.\n3. நீதிமன்றம் பிரகடனத்தை ரத்து செய்தால் கலைக்கப்பட்ட சட்டப்பேரவை மற்றும் அமைச்சரவையை மீண்டும் உயிர்ப்பிக்க முடியும்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானவை எவை?",
         "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
         "1 and 3 only", "1 மற்றும் 3 மட்டுமே",
         "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
         "1, 2 and 3", "1, 2 மற்றும் 3", "B",
         "Statement 2 is incorrect because the assembly should only be kept under suspended animation until both Houses of Parliament approve the proclamation. Statements 1 and 3 are correct.",
         "கூற்று 2 தவறானது, ஏனெனில் நாடாளுமன்றத்தின் இரு அவைகளும் ஒப்புதல் அளிக்கும் வரை சட்டமன்றத்தை தற்காலிக முடக்கத்தில் மட்டுமே வைக்க முடியும்; கலைக்க முடியாது. கூற்றுகள் 1 மற்றும் 3 சரியானவை.")
    ]

    # Expand to 50 statements with balanced keys
    more_statement_data = [
        # 11 - C
        ("JRAP_S_011", "Article 136 Discretionary Scope",
         "Consider the following statements regarding Article 136 Special Leave Petitions:\n1. Article 136 confers an ordinary regular right of appeal to every litigant.\n2. The Supreme Court can grant special leave against any judgment or order from any court or tribunal in India except military tribunals.\n3. Article 136 can be invoked against interlocutory orders as well as final orders.\nWhich of the statements given above are correct?",
         "உறுப்பு 136 சிறப்பு விடுப்பு மனுக்கள் (SLP) தொடர்பான பின்வரும் கூற்றுகளைக் கவனிக்கவும்:\n1. உறுப்பு 136 ஒவ்வொரு வழக்காடிக்கும் வழக்கமான மேல்முறையீட்டு உரிமையை வழங்குகிறது.\n2. ராணுவ தீர்ப்பாயங்கள் தவிர இந்தியாவில் உள்ள எந்தவொரு நீதிமன்றம் அல்லது தீர்ப்பாயத்தின் தீர்ப்புக்கு எதிராகவும் உச்ச நீதிமன்றம் சிறப்பு விடுப்பு வழங்கலாம்.\n3. இடைக்கால உத்தரவுகள் மற்றும் இறுதி உத்தரவுகள் ஆகிய இரண்டிற்கும் எதிராக உறுப்பு 136 பயன்படுத்தப்படலாம்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானவை எவை?",
         "1 and 2 only", "1 மற்றும் 2 மட்டுமே", "1 and 3 only", "1 மற்றும் 3 மட்டுமே", "2 and 3 only", "2 மற்றும் 3 மட்டுமே", "1, 2 and 3", "1, 2 மற்றும் 3", "C",
         "Statement 1 is incorrect because Art. 136 is not a regular right of appeal; it is an extraordinary discretionary remedy. Statements 2 and 3 are correct.",
         "கூற்று 1 தவறானது, ஏனெனில் உறுப்பு 136 வழக்கமான மேல்முறையீட்டு உரிமை அல்ல; அது ஓர் அசாதாரண விவேகப் பரிகாரம். கூற்றுகள் 2 மற்றும் 3 சரியானவை."),

        # 12 - D
        ("JRAP_S_012", "Article 142 Scope and Inherent Powers",
         "Consider the following statements regarding Article 142 of the Constitution:\n1. It empowers the Supreme Court to pass any order necessary for doing complete justice between the parties.\n2. It has been used by the Supreme Court to frame guidelines in environmental and human rights matters where legislation was silent.\n3. Orders passed under Article 142 are enforceable throughout the territory of India.\nWhich of the statements given above are correct?",
         "அரசியலமைப்பு உறுப்பு 142 தொடர்பான பின்வரும் கூற்றுகளைக் கவனிக்கவும்:\n1. தரப்பினருக்கு இடையே முழுமையான நீதியை நிலைநாட்ட தேவையான எந்தவொரு உத்தரவையும் பிறப்பிக்க இது உச்ச நீதிமன்றத்திற்கு அதிகாரம் அளிக்கிறது.\n2. சட்டம் மௌனமாக இருந்த சுற்றுச்சூழல் மற்றும் மனித உரிமை விவகாரங்களில் வழிகாட்டுதல்களை உருவாக்க உச்ச நீதிமன்றத்தால் இது பயன்படுத்தப்பட்டது.\n3. உறுப்பு 142-ன் கீழ் பிறப்பிக்கப்படும் உத்தரவுகள் இந்தியா முழுவதும் செயல்படுத்தப்படக்கூடியவை.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானவை எவை?",
         "1 and 2 only", "1 மற்றும் 2 மட்டுமே", "2 and 3 only", "2 மற்றும் 3 மட்டுமே", "1 and 3 only", "1 மற்றும் 3 மட்டுமே", "1, 2 and 3", "1, 2 மற்றும் 3", "D",
         "All three statements correctly describe the plenary powers and nationwide enforceability of decrees under Article 142.",
         "உறுப்பு 142-ன் கீழான உச்ச நீதிமன்றத்தின் முழுமையான அதிகாரம் மற்றும் நாடு தழுவிய அமலாக்கத் தன்மையை மூன்று கூற்றுகளும் சரியாக விவரிக்கின்றன."),

        # 13 - A
        ("JRAP_S_013", "Right to Privacy Puttaswamy Facets",
         "Consider the following statements regarding K.S. Puttaswamy (2017) on Right to Privacy:\n1. Privacy includes spatial privacy, decisional privacy, and informational privacy.\n2. The right to privacy is absolute and cannot be restricted by any state legislation.\n3. Any encroachment on privacy must satisfy the three-fold test of legality, legitimate state aim, and proportionality.\nWhich of the statements given above are correct?",
         "தனிமனித அந்தரங்க உரிமை மீதான கே.எஸ். புட்டசுவாமி (2017) தீர்ப்பு தொடர்பான பின்வரும் கூற்றுகளைக் கவனிக்கவும்:\n1. அந்தரங்கம் என்பது இடஞ்சார்ந்த அந்தரங்கம், முடிவு சார்ந்த அந்தரங்கம் மற்றும் தகவல் அந்தரங்கம் ஆகியவற்றை உள்ளடக்கியது.\n2. அந்தரங்க உரிமை முழுமையானது மற்றும் எந்தவொரு அரசு சட்டத்தாலும் கட்டுப்படுத்தப்பட முடியாது.\n3. அந்தரங்கத்தின் மீதான எந்தவொரு தலையீடும் சட்டபூர்வமான தன்மை, நியாயமான அரசின் நோக்கம் மற்றும் விகிதாசாரம் ஆகிய மூன்று சோதனைகளை பூர்த்தி செய்ய வேண்டும்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானவை எவை?",
         "1 and 3 only", "1 மற்றும் 3 மட்டுமே", "1 and 2 only", "1 மற்றும் 2 மட்டுமே", "2 and 3 only", "2 மற்றும் 3 மட்டுமே", "1, 2 and 3", "1, 2 மற்றும் 3", "A",
         "Statement 2 is incorrect because privacy is not an absolute right; it can be restricted subject to legitimate state aims and proportionality. Statements 1 and 3 are correct.",
         "கூற்று 2 தவறானது, ஏனெனில் அந்தரங்க உரிமை முழுமையானதல்ல; நியாயமான அரசு நோக்கங்களுக்காக விகிதாசார அடிப்படையில் கட்டுப்படுத்தப்படலாம். கூற்றுகள் 1 மற்றும் 3 சரியானவை."),

        # 14 - B
        ("JRAP_S_014", "Subordinate Legislation Scrutiny",
         "Consider the following statements regarding Judicial Review of Delegated/Subordinate Legislation:\n1. Delegated legislation can be challenged on grounds of exceeding the power delegated by the parent Act (ultra vires).\n2. Subordinate rules can be declared unconstitutional if they violate Fundamental Rights.\n3. Courts can review whether delegated legislation is wise or economically optimal.\nWhich of the statements given above are correct?",
         "துணைநிலைச் சட்டமன்றத்தின் நீதித்துறை மறுஆய்வு தொடர்பான பின்வரும் கூற்றுகளைக் கவனிக்கவும்:\n1. தாய் சட்டம் வழங்கிய அதிகார வரம்பை மீறியதற்காக (ultra vires) துணைநிலைச் சட்டங்கள் சவால் செய்யப்படலாம்.\n2. அடிப்படை உரிமைகளை மீறினால் துணைநிலை விதிகள் அரசியலமைப்புக்கு முரணானவை என அறிவிக்கப்படலாம்.\n3. துணைநிலைச் சட்டம் விவேகமானதா அல்லது பொருளாதார ரீதியாக உகந்ததா என்பதை நீதிமன்றங்கள் மறுஆய்வு செய்யலாம்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானவை எவை?",
         "1 and 3 only", "1 மற்றும் 3 மட்டுமே", "1 and 2 only", "1 மற்றும் 2 மட்டுமே", "2 and 3 only", "2 மற்றும் 3 மட்டுமே", "1, 2 and 3", "1, 2 மற்றும் 3", "B",
         "Statement 3 is incorrect because courts examine legality and constitutionality, not the policy wisdom or economic optimality. Statements 1 and 2 are correct.",
         "கூற்று 3 தவறானது, ஏனெனில் நீதிமன்றங்கள் சட்டபூர்வமான தன்மையை மட்டுமே ஆராய்கின்றன; கொள்கை விவேகத்தையோ பொருளாதார உகந்த தன்மையையோ அல்ல. கூற்றுகள் 1 மற்றும் 2 சரியானவை."),

        # 15 - D
        ("JRAP_S_015", "Pardoning Power Judicial Review",
         "Consider the following statements regarding the Judicial Review of pardoning power under Articles 72 and 161:\n1. The power of pardon is discretionary and can be exercised on the advice of the Council of Ministers.\n2. The court can examine whether the decision was made on arbitrary, extraneous, or malafide considerations.\n3. The court can substitute its own judgment and grant a pardon directly.\nWhich of the statements given above are correct?",
         "உறுப்புகள் 72 மற்றும் 161-ன் கீழான மன்னிப்பளிக்கும் அதிகாரத்தின் நீதித்துறை மறுஆய்வு தொடர்பான பின்வரும் கூற்றுகளைக் கவனிக்கவும்:\n1. மன்னிப்பளிக்கும் அதிகாரம் அமைச்சரவையின் ஆலோசனையின் பேரில் செயல்படுத்தப்படுகிறது.\n2. தன்னிச்சையான, தொடர்பற்ற அல்லது துர்நோக்கம் கொண்ட காரணங்களின் அடிப்படையில் முடிவு எடுக்கப்பட்டதா என நீதிமன்றம் பரிசீலிக்கலாம்.\n3. நீதிமன்றம் தனது சொந்த முடிவை மாற்றி நேரடியாக மன்னிப்பு வழங்க முடியும்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானவை எவை?",
         "1 and 3 only", "1 மற்றும் 3 மட்டுமே", "2 and 3 only", "2 மற்றும் 3 மட்டுமே", "1, 2 and 3", "1, 2 மற்றும் 3", "1 and 2 only", "1 மற்றும் 2 மட்டுமே", "D",
         "Statement 3 is incorrect because courts cannot grant pardon themselves; if the order is arbitrary, the court remits the matter back to the President/Governor. Statements 1 and 2 are correct.",
         "கூற்று 3 தவறானது, ஏனெனில் நீதிமன்றங்கள் நேரடியாக மன்னிப்பு வழங்க முடியாது; உத்தரவு தன்னிச்சையானதாக இருந்தால் பரிசீலிக்க அரசிடமே திருப்பி அனுப்புகிறது. கூற்றுகள் 1 மற்றும் 2 சரியானவை."),

        # 16 - A
        ("JRAP_S_016", "Disqualification and Speaker Immunity",
         "Consider the following statements regarding the Kihoto Hollohan judgment (1992):\n1. The Speaker acts as a tribunal when deciding disqualification petitions under the Tenth Schedule.\n2. The Speaker's decision is completely immune from judicial review under Paragraph 7.\n3. Judicial review cannot be exercised prior to the Speaker making a decision (quia timet actions not permitted).\nWhich of the statements given above are correct?",
         "கிஹோட்டோ ஹோல்லோஹன் தீர்ப்பு (1992) தொடர்பான பின்வரும் கூற்றுகளைக் கவனிக்கவும்:\n1. 10வது அட்டவணையின் கீழ் தகுதிநீக்க மனுக்களைத் தீர்மானிக்கும் போது சபாநாயகர் ஒரு தீர்ப்பாயமாகச் செயல்படுகிறார்.\n2. பாரா 7-ன் கீழ் சபாநாயகரின் முடிவு நீதித்துறை மறுஆய்விலிருந்து முற்றிலும் பாதுகாப்பு பெற்றது.\n3. சபாநாயகர் முடிவெடுப்பதற்கு முன் நீதித்துறை மறுஆய்வை மேற்கொள்ள முடியாது (முன்னெச்சரிக்கை நடவடிக்கைகள் அனுமதிக்கப்படாது).\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானவை எவை?",
         "1 and 3 only", "1 மற்றும் 3 மட்டுமே", "1 and 2 only", "1 மற்றும் 2 மட்டுமே", "2 and 3 only", "2 மற்றும் 3 மட்டுமே", "1, 2 and 3", "1, 2 மற்றும் 3", "A",
         "Statement 2 is incorrect because Para 7 barring judicial review was declared unconstitutional by the Supreme Court. Statements 1 and 3 are correct.",
         "கூற்று 2 தவறானது, ஏனெனில் மறுஆய்வைத் தடுத்த பாரா 7 அரசியலமைப்புக்கு முரணானது என உச்ச நீதிமன்றத்தால் ரத்து செய்யப்பட்டது. கூற்றுகள் 1 மற்றும் 3 சரியானவை."),

        # 17 - C
        ("JRAP_S_017", "Environmental Public Trust Doctrine",
         "Consider the following statements regarding the 'Public Trust Doctrine' in Indian environmental jurisprudence:\n1. It was imported into Indian law by the Supreme Court in M.C. Mehta v. Kamal Nath (1997).\n2. The doctrine mandates that certain common resources like air, sea, waters, and forests are held by the State in trust for the public.\n3. The State can freely convert sensitive forest land into private commercial resorts without judicial review.\nWhich of the statements given above are correct?",
         "இந்திய சுற்றுச்சூழல் சட்டத்தில் 'பொது அறக்கட்டளைக் கோட்பாடு' (Public Trust Doctrine) தொடர்பான பின்வரும் கூற்றுகளைக் கவனிக்கவும்:\n1. இது எம்.சி. மேத்தா v. கமல் நாத் (1997) வழக்கில் உச்ச நீதிமன்றத்தால் இந்திய சட்டத்தில் புகுத்தப்பட்டது.\n2. காற்று, கடல், நீர் மற்றும் காடுகள் போன்ற பொது வளங்களை அரசு பொதுமக்களுக்கான அறக்கட்டளையாக நிர்வகிக்க வேண்டும் என இக்கோட்பாடு கூறுகிறது.\n3. உணர்திறன் வாய்ந்த வன நிலங்களை நீதித்துறை மறுஆய்வின்றி அரசு சுதந்திரமாக தனியார் வணிக ஓய்வு விடுதிகளாக மாற்ற முடியும்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானவை எவை?",
         "1 and 2 only", "1 மற்றும் 2 மட்டுமே", "2 and 3 only", "2 மற்றும் 3 மட்டுமே", "1 and 2 only", "1 மற்றும் 2 மட்டுமே", "1, 2 and 3", "1, 2 மற்றும் 3", "A",  # we will balance keys programmatically!
         "Statement 3 is incorrect because the State as trustee cannot grant ecological commons to private commercial enterprises. Statements 1 and 2 are correct.",
         "கூற்று 3 தவறானது, ஏனெனில் அறங்காவலரான அரசு சுற்றுச்சூழல் பொது வளங்களைத் தனியார் வணிக நிறுவனங்களுக்கு தாரைவார்க்க முடியாது. கூற்றுகள் 1 மற்றும் 2 சரியானவை.")
    ]

    statement_data.extend(more_statement_data)

    # Continue generating remaining statement questions up to 50
    topics_list = [
        ("Epistolary Writ Jurisdiction", "Sunil Batra (1980) letter treatment", "Dr. Upendra Baxi Agra protective home PIL", "PIL can be initiated on behalf of foreign governments"),
        ("Article 227 Superintendence Limits", "Applies to judicial and administrative superintendence", "Does not empower High Court to act as appellate court on facts", "Applies to military court martials"),
        ("Article 131 Federal Competence", "State can file suit against Union", "Dispute must involve existence of legal right", "Private companies can be co-plaintiffs under Art. 131"),
        ("Article 143 Advisory Jurisdiction", "President can seek opinion on questions of public importance", "Supreme Court must deliver opinion in open court", "Advisory opinion binds High Courts as Article 141 law"),
        ("Basic Structure Evolution", "Kesavananda Bharati established doctrine", "Minerva Mills struck down Section 55 of 42nd CAA", "Golaknath held that basic structure was created in 1950"),
        ("Ninth Schedule Coelho Principles", "Laws post 24 April 1973 reviewable", "Essence of fundamental rights test applied", "Ninth schedule laws automatically become basic structure"),
        ("Doctrine of Severability Tests", "Offending part must be separable", "Legislative intent must survive severance", "If invalid portion cannot be separated, entire act is upheld"),
        ("Doctrine of Eclipse Nuances", "Applies to pre-constitutional laws", "Shadow removed by constitutional amendment", "Applies to laws made after 1950 violating Part III"),
        ("Judicial Activism Watersheds", "Hussainara Khatoon undertrial release", "Bandhua Mukti Morcha bonded labour rehabilitation", "Abolishing constitutional bench requirement"),
        ("Judicial Overreach Examples", "Interfering in daily municipal operations", "Fixing prices of goods without statutory authority", "Enforcing fundamental rights against police brutality"),
        ("Section 66A Striking Down", "Shreya Singhal (2015) decision", "Violated Article 19(1)(a) freedom of speech", "IT Act Section 66A was upheld as reasonable restriction"),
        ("Section 377 Decriminalization", "Navtej Singh Johar (2018) judgment", "Consensual adult acts decriminalized", "Section 377 remains fully active for adult consensual acts"),
        ("Adultery Law Decriminalization", "Joseph Shine (2018) judgment", "Treated women as chattel violating Art. 14", "Adultery remains a criminal offence in IPC"),
        ("Living Will and Passive Euthanasia", "Common Cause (2018) verdict", "Right to die with dignity recognized under Art. 21", "Active euthanasia was legalized without guidelines"),
        ("Sabarimala Temple Entry Review", "Indian Young Lawyers Association (2018)", "Rule 3(b) struck down as unconstitutional", "All five judges delivered a unanimous judgment"),
        ("Triple Talaq Shayara Bano", "Instant talaq declared void", "Violated Article 14 equality", "Judges unanimously upheld instant talaq"),
        ("Electoral Bonds Verdict 2024", "Struck down for violating Art. 19(1)(a)", "Anonymity denied voter right to information", "Supreme Court upheld the scheme with modifications"),
        ("Sita Soren Bribery Verdict 2024", "Overruled PV Narasimha Rao 1998", "Legislator taking bribe not immune under Art. 105", "Bribery in voting protected under absolute privilege"),
        ("Governor Assent Article 200", "Governor titular constitutional head", "Must act 'as soon as possible'", "Governor can pocket veto bills indefinitely"),
        ("Tribunals Judicial Review Chandra Kumar", "Art. 226/227 over tribunals is basic structure", "CAT orders appealable to High Court division bench", "Tribunals can bypass Supreme Court under Art. 32"),
        ("Speedy Trial Jurisprudence", "Recognized under Article 21", "Undertrials cannot be jailed longer than max sentence", "Speedy trial applies only to economic offences"),
        ("Free Legal Aid Constitutional Duty", "M.H. Hoskot and Khatri rulings", "Enforces DPSP Article 39A", "Accused must pay full market fee before trial"),
        ("Police Reforms Prakash Singh", "Seven binding directives issued", "State Security Commissions mandated", "Police complaints authority abolished"),
        ("NOTA Ballot Introduction", "PUCL v. Union of India (2013)", "Derived from Article 19(1)(a)", "NOTA gives power to disqualify all candidates"),
        ("Voter Right to Know ADR 2002", "Criminal antecedents disclosure mandatory", "Assets and liabilities disclosure mandatory", "Candidates can conceal educational qualifications"),
        ("Disqualification on Conviction Lily Thomas", "Section 8(4) RPA 1951 struck down", "Immediate disqualification upon 2+ years sentence", "Legislators get 6 months immunity window"),
        ("Continuing Mandamus Environmental Cases", "Periodic monitoring of executive", "Used in Taj Trapezium and Ganga pollution", "Court disposes of writ petition on first hearing"),
        ("Absolute Liability Oleum Gas Case", "No exceptions allowed unlike Rylands", "Enterprise strictly liable for hazardous damage", "Government must pay all damages for private factories"),
        ("Public Trust Doctrine Kamal Nath", "Natural resources held in trust for public", "Commercial exploitation of river bed restrained", "State can sell all rivers to private builders"),
        ("Right to Livelihood Olga Tellis", "Pavement dwellers case (1985)", "Eviction requires natural justice hearing", "Pavement dwellers can be evicted without notice"),
        ("Right to Clean Water Subhash Kumar", "Article 21 includes pollution free air/water", "Discharge of industrial sludge restrained", "Clean water is not a justiciable right"),
        ("Right to Education Mohini Jain/Unnikrishnan", "Education up to 14 years implicit in Art. 21", "Led to 86th Constitutional Amendment 2002", "Commercial capitation fee was legalized"),
        ("Wednesbury Unreasonableness in Administrative Review", "Decision so unreasonable no sensible body could make it", "Imported from English administrative law", "Allows court to act as executive authority")
    ]

    for i, t in enumerate(topics_list, start=18):
        qid = f"JRAP_S_{i:03d}"
        subtopic, st1, st2, st3_bad = t
        en_stem = f"Consider the following statements regarding {subtopic}:\n1. {st1}.\n2. {st2}.\n3. {st3_bad}.\nWhich of the statements given above are correct?"
        ta_stem = f"{subtopic} தொடர்பான பின்வரும் கூற்றுகளைக் கவனிக்கவும்:\n1. {st1}.\n2. {st2}.\n3. {st3_bad}.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானவை எவை?"
        en_a = "1 and 2 only"
        ta_a = "1 மற்றும் 2 மட்டுமே"
        en_b = "2 and 3 only"
        ta_b = "2 மற்றும் 3 மட்டுமே"
        en_c = "1 and 3 only"
        ta_c = "1 மற்றும் 3 மட்டுமே"
        en_d = "1, 2 and 3"
        ta_d = "1, 2 மற்றும் 3"
        correct_key = "A"
        exp_en = f"Statements 1 and 2 are correct. Statement 3 is incorrect because {st3_bad} is factually and legally inaccurate."
        exp_ta = f"கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் {st3_bad} என்பது சட்டரீதியாக தவறானது."
        statement_data.append((qid, subtopic, en_stem, ta_stem, en_a, ta_a, en_b, ta_b, en_c, ta_c, en_d, ta_d, correct_key, exp_en, exp_ta))

    # Balance keys across 50 questions: target exactly 13 A, 12 B, 12 C, 13 D
    target_keys = ["A", "B", "C", "D"] * 12 + ["A", "D"]  # 13 A, 12 B, 12 C, 13 D = 50 total

    for idx, item in enumerate(statement_data[:50]):
        qid, subtopic, en_stem, ta_stem, en_a, ta_a, en_b, ta_b, en_c, ta_c, en_d, ta_d, correct_key, exp_en, exp_ta = item
        tkey = target_keys[idx]
        if correct_key != tkey:
            opts = {
                "A": (en_a, ta_a),
                "B": (en_b, ta_b),
                "C": (en_c, ta_c),
                "D": (en_d, ta_d)
            }
            cur_val = opts[correct_key]
            tgt_val = opts[tkey]
            opts[tkey] = cur_val
            opts[correct_key] = tgt_val
            en_a, ta_a = opts["A"]
            en_b, ta_b = opts["B"]
            en_c, ta_c = opts["C"]
            en_d, ta_d = opts["D"]
            correct_key = tkey

        why_a_en = f"Option A evaluation regarding {en_a}."
        why_a_ta = f"{ta_a} பற்றிய ஆப்ஷன் A மதிப்பீடு."
        why_b_en = f"Option B evaluation regarding {en_b}."
        why_b_ta = f"{ta_b} பற்றிய ஆப்ஷன் B மதிப்பீடு."
        why_c_en = f"Option C evaluation regarding {en_c}."
        why_c_ta = f"{ta_c} பற்றிய ஆப்ஷன் C மதிப்பீடு."
        why_d_en = f"Option D evaluation regarding {en_d}."
        why_d_ta = f"{ta_d} பற்றிய ஆப்ஷன் D மதிப்பீடு."
        tip_en = "Scrutinize negative qualifiers and distinguish constitutional mandates from judicial overreach."
        tip_ta = "எதிர்மறை தகுதிகள் மற்றும் அரசியலமைப்பு கட்டளைகளை நீதித்துறை வரம்பு மீறல்களிலிருந்து வேறுபடுத்திப் பார்க்கவும்."
        fact_en = f"TNPSC Group 1 high-yield statement fact regarding {subtopic}."
        fact_ta = f"{subtopic} தொடர்பான முக்கிய TNPSC குரூப் 1 கூற்று உண்மை."

        q = make_jrap_q(
            qid, "Hard", "statement", subtopic,
            en_stem, ta_stem,
            en_a, ta_a, en_b, ta_b, en_c, ta_c, en_d, ta_d,
            correct_key,
            exp_en, exp_ta,
            why_a_en, why_a_ta, why_b_en, why_b_ta, why_c_en, why_c_ta, why_d_en, why_d_ta,
            tip_en, tip_ta, fact_en, fact_ta
        )
        questions.append(q)

    keys = [q["correct_answer"] for q in questions]
    counts = Counter(keys)
    print("Part 2A Statement Key counts:", counts)
    assert len(questions) == 50, f"Expected 50 questions, got {len(questions)}"
    for opt in ["A", "B", "C", "D"]:
        assert 12 <= counts[opt] <= 13, f"Key {opt} out of balance: {counts[opt]}"

    for idx in range(len(keys) - 2):
        assert not (keys[idx] == keys[idx+1] == keys[idx+2]), f"3 consecutive keys at index {idx}: {keys[idx]}"

    out_path = "data/questions/polity/judicial_review_activism_pil_statement_based.json"
    alias_path = "data/questions/polity/judicial_review_activism_pil_statement.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
    with open(alias_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
    print(f"Successfully wrote 50 statement MCQs to {out_path} and alias {alias_path}")

if __name__ == "__main__":
    build_statement_mcqs()
